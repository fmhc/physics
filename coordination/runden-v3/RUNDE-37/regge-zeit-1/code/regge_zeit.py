#!/usr/bin/env python3
"""REGGE-ZEIT-1 (Runde 37, Code-Agent): ruhende Punktmasse auf einer Weltlinie entlang tau im 4D-Kuhn-Gitter.

Euklidisch, statisch (k_tau = 0), linear. Reines numpy, float64. Grundlage: RUNDE-36/regge-4d-1/code/regge4d.py
(Gitter, Weg T, M(k) = A^+ E in Mittelpunktskonvention), unveraendert importiert.

  Wirkung  S_E = -(1/(8 pi G)) sum_t A_t eps_t + M sum_WL l_e  ->  M(k) u(k) = 4 pi G M e_tau  (PLAN Abschnitt 2)
  Loesung  auf dem Komplement des analytischen Nullraums (4 Gitter-Eichmoden + Hyperdiagonale), k = 0 entfaellt
  Fixierung der Hyperdiagonale: u_top = -(v^+ eps)/(v^+ v), v = E(k) e_top (kleinste Fehlwinkel je k, PLAN [F2])
  Fehlwinkel eps_t(x) per inverser FFT (Schwerpunktphase), Torus-Korrektur: Hintergrund aus dem Kleink-Mittel des
  Spektrums plus Bildsumme (kubisch) der Kontinuumskruemmung ueber die kalibrierte Antwort (PLAN Abschnitt 5)
  Kalibrierung: konstante Kruemmung (quadratisches h, Linienintegral), Gittermoden C4 versklavt (PLAN Abschnitt 4)
  3D-Kontrolle: Kuhn 3D, Gelenke = Kanten, Ableitungen per komplexem Schritt (Gram-Inverse)

Aufruf: python regge_zeit.py <ausgabe.json> <L-Liste, z. B. 16,24,32,64> <L3>
"""
import hashlib
import itertools
import json
import os
import sys
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import regge4d as R4  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
GM = 1.0                       # G der Wirkung = 1, M = 1 (linear: alles skaliert mit G M)
QUELLE = 4.0 * np.pi * GM      # rechte Seite: M(k) u = 4 pi G M e_tau (dl/ds = 1/2 an Zeitkanten der Laenge 1)
KAPPA = (0.02, 0.01)           # kleine |k| fuer den Hintergrund, Richardson
N_BILD = 16                    # Bildsumme |n|_inf <= N_BILD (kubisch)
XI = -2.837297                 # Torus-Konstante [L], nur fuer die beschreibende Potentialprobe
BATCH = 4096
H_KOMPLEX = 1e-20
TAU, XA, YA, ZA = 0, 1, 2, 3


def protokoll(log, s):
    print(s, flush=True)
    log.append(s)


# ======================================================================= Ableitungen, komplexer Schritt (Gram-Inverse)
def kosinus_gram(git, sq):
    """cos der Diederwinkel je lokalem Gelenk aus Kantenquadraten; analytisch in sq (komplexer Schritt erlaubt)."""
    n = git.n
    Ns = sq.shape[0]
    S = np.zeros((Ns, n + 1, n + 1), dtype=sq.dtype)
    for k, (i, j) in enumerate(git.paare):
        S[:, i, j] = sq[:, k]
        S[:, j, i] = sq[:, k]
    G = 0.5 * (S[:, 0, 1:, None] + S[:, 0, None, 1:] - S[:, 1:, 1:])
    Gi = np.linalg.inv(G)
    D = np.zeros((Ns, n + 1, n + 1), dtype=sq.dtype)
    D[:, 1:, 1:] = Gi
    D[:, 0, 1:] = -Gi.sum(axis=1)
    D[:, 1:, 0] = -Gi.sum(axis=2)
    D[:, 0, 0] = Gi.sum(axis=(1, 2))
    out = [-D[:, m, mm] / np.sqrt(D[:, m, m] * D[:, mm, mm]) for _, (m, mm) in git.lok_gelenke]
    return np.stack(out, 1)


def jacobi_komplex(git):
    """d theta / d s je Simplextyp (nP, Gelenke, Kanten) per komplexem Schritt; dazu Vergleich der Winkel mit winkel()."""
    sq0 = np.array([[float(np.sum(git.dirs[d] ** 2)) for _, d in git.p_kanten[ip]] for ip in range(git.nP)])
    nEs = len(git.paare)
    J = np.zeros((git.nP, len(git.lok_gelenke), nEs))
    for e in range(nEs):
        sq = sq0.astype(complex)
        sq[:, e] += 1j * H_KOMPLEX
        c = kosinus_gram(git, sq)
        J[:, :, e] = -(c.imag / H_KOMPLEX) / np.sqrt(1.0 - c.real ** 2)
    winkel_diff = float(np.max(np.abs(np.arccos(kosinus_gram(git, sq0.astype(float))) - git.winkel(sq0))))
    return J, winkel_diff


def eT_aus_dic(git, dic):
    eT = []
    for d in range(git.nE):
        keys = sorted((t, R) for (t, dd, R) in dic if dd == d)
        tau = np.array([k[0] for k in keys], dtype=np.int64)
        Rp = np.array([k[1] for k in keys], dtype=np.int64).reshape(len(keys), git.n)
        val = np.array([dic[(k[0], d, k[1])] for k in keys])
        eT.append((tau, Rp, val))
    return eT


def eT_dic(eT):
    out = {}
    for d in range(len(eT)):
        tau, Rp, val = eT[d]
        for t_, r_, v_ in zip(tau, Rp, val):
            out[(int(t_), d, tuple(int(x) for x in r_))] = float(v_)
    return out


def vergleich_stencil(eA, eB):
    a, b = eT_dic(eA), eT_dic(eB)
    keys = set(a) | set(b)
    return float(max(abs(a.get(q, 0.0) - b.get(q, 0.0)) for q in keys))


# ======================================================================= Loesung im Fourierraum
def nullbasis(git, ks):
    """Analytischer Nullraum je k: Gitter-Eichmoden sin(k.d/2) d_mu (n Stueck), in 4D dazu e_top. Orthonormiert."""
    dirs = git.dirs.astype(float)
    G = np.sin(0.5 * ks @ dirs.T)[:, :, None] * dirs[None, :, :]
    if git.n == 4:
        et = np.zeros((len(ks), git.nE, 1))
        et[:, git.top, 0] = 1.0
        G = np.concatenate([G, et], axis=2)
    sv = np.linalg.svd(G, compute_uv=False)
    Qn, _ = np.linalg.qr(G)
    return Qn, sv[:, -1] / sv[:, 0]


def projiziere(v, eps):
    """Fixierung der Hyperdiagonale nach kleinsten Fehlwinkeln (PLAN [F2], Fassung nach Rauchlauf 2):
    u_top = c = -(v^+ eps)/(v^+ v) mit v = E(k) e_top, also eps -> eps + c v (Projektion senkrecht zu v).
    Exakt frei von Diagonalmode und Eichmoden, 2 pi-periodisch in k. Die sinc-Regel der ersten Fassung war nicht
    periodisch (Imaginaerteil 0,19 im Rauchlauf 2) und ist verworfen."""
    c = -np.einsum("...t,...t->...", v.conj(), eps) / np.einsum("...t,...t->...", v.conj(), v).real
    return eps + c[..., None] * v, c


def spektrum(git, eT, ks, B, quelle_index, mit_kontrollen=False):
    """Loesung u(k), Fehlwinkel eps(k) und F(k) = exp(i k.c_t) eps(k) fuer eine Liste statischer k (k != 0)."""
    Am, Em, M = git.matrizen(ks, eT)
    imag = float(np.max(np.abs(M.imag)) / np.max(np.abs(M.real)))
    Mr = 0.5 * (M.real + np.swapaxes(M.real, 1, 2))
    herm = float(np.max(np.abs(M - np.conj(np.swapaxes(M, 1, 2)))) / np.max(np.abs(M)))
    s = np.zeros(git.nE)
    s[quelle_index] = QUELLE
    Qn, svmin = nullbasis(git, ks)
    P = np.eye(git.nE)[None] - np.einsum("kai,kbi->kab", Qn, Qn)
    w, V = np.linalg.eigh(P)
    nn = Qn.shape[2]
    Qc = V[:, :, nn:]
    Mc = np.einsum("kai,kab,kbj->kij", Qc, Mr, Qc)
    sc = np.einsum("kai,a->ki", Qc, s)
    yc = np.linalg.solve(Mc, sc[:, :, None])[:, :, 0]
    u = np.einsum("kai,ki->ka", Qc, yc)
    phase = np.exp(1j * ks @ git.g_mitte.T)
    eps = np.einsum("kta,ka->kt", Em, u)
    F_ohne = phase * eps                                       # Hyperdiagonale unveraendert (u_top = 0), nur Bericht
    if git.n == 4:
        eps, c = projiziere(Em[:, :, git.top], eps)
        u = u.astype(complex)
        u[:, git.top] = c
    F = phase * eps
    out = {"u": u, "eps": eps, "F": F, "F_ohne": F_ohne}
    if mit_kontrollen:
        Lam = np.max(np.abs(np.linalg.eigvalsh(Mr)), axis=1)
        proj = np.linalg.norm(np.einsum("kai,a->ki", Qn, s), axis=1) / np.linalg.norm(s)
        res = np.linalg.norm(np.einsum("kab,kb->ka", Mr, u) - s[None], axis=1) / np.linalg.norm(s)
        nullres = np.linalg.norm(np.einsum("kab,kbi->kai", Mr, Qn), axis=(1, 2)) / Lam
        evc = np.abs(np.linalg.eigvalsh(Mc))
        # Fehlwinkel einer Eichmode und der Hyperdiagonale (roh, ohne Fixierung)
        dirs = git.dirs.astype(float)
        g1 = np.sin(0.5 * ks @ dirs.T) * dirs[None, :, 1]
        eich_eps = np.linalg.norm(np.einsum("kta,ka->kt", Em, g1), axis=1) / (
            np.linalg.norm(Em, axis=(1, 2)) * np.linalg.norm(g1, axis=1))
        out["kontrollen"] = {
            "quelle_auf_nullraum_rel_max": float(np.max(proj)),
            "residuum_gleichung_rel_max": float(np.max(res)),
            "nullraum_residuum_rel_max": float(np.max(nullres)),
            "komplement_min_eigen_rel": float(np.min(np.min(evc, axis=1) / Lam)),
            "nullbasis_min_singulaer_rel": float(np.min(svmin)),
            "M_imag_rel_max": imag,
            "M_hermitesch_rel_max": herm,
            "eps_eichmode_rel_max": float(np.max(eich_eps)),
        }
        if git.n == 4:
            out["kontrollen"]["E_top_norm_min"] = float(np.min(np.linalg.norm(Em[:, :, git.top], axis=1)))
    return out


def loese_torus(git, eT, L, B, quelle_index, log):
    """Ganzes statisches Gitter L^(n-1); F(k) fuer alle k != 0; Ruecktransformation."""
    n = git.n
    f = np.fft.fftfreq(L) * 2.0 * np.pi
    gitter = np.meshgrid(*([f] * (n - 1)), indexing="ij")
    ksp = np.stack([g.ravel() for g in gitter], 1)
    ks = np.column_stack([np.zeros(len(ksp)), ksp])
    Nk = len(ks)
    F = np.zeros((Nk, git.nH), complex)
    F_ohne = np.zeros((Nk, git.nH), complex)
    utau = np.zeros(Nk, complex)
    kon = []
    t0 = time.time()
    for a in range(1, Nk, BATCH):
        b = min(a + BATCH, Nk)
        sp = spektrum(git, eT, ks[a:b], B, quelle_index, mit_kontrollen=True)
        F[a:b] = sp["F"]
        F_ohne[a:b] = sp["F_ohne"]
        utau[a:b] = sp["u"][:, quelle_index]
        kon.append(sp["kontrollen"])
    kont = {}
    for key in kon[0]:
        vals = [c[key] for c in kon]
        kont[key] = float(min(vals)) if key.endswith("_min") or "min_" in key else float(max(vals))
    shape = (L,) * (n - 1)
    eps = np.empty((git.nH,) + shape)
    eps_ohne = np.empty((git.nH,) + shape)
    imag_max = 0.0
    for t in range(git.nH):
        z = np.fft.ifftn(F[:, t].reshape(shape))
        eps[t] = z.real
        imag_max = max(imag_max, float(np.max(np.abs(z.imag))))
        eps_ohne[t] = np.fft.ifftn(F_ohne[:, t].reshape(shape)).real
    ds_tau = np.fft.ifftn(utau.reshape(shape))
    kont["eps_imag_max"] = imag_max
    kont["eps_real_max"] = float(np.max(np.abs(eps)))
    kont["ds_tau_imag_max"] = float(np.max(np.abs(ds_tau.imag)))
    protokoll(log, f"n={n} L={L}: {Nk} k-Punkte geloest ({time.time() - t0:.1f} s)")
    return eps, ds_tau.real, kont, eps_ohne


def hintergrund(git, eT, B, quelle_index):
    """Kleink-Mittel <F(k -> 0)> ueber +-Achsenrichtungen, Richardson in kappa (PLAN Abschnitt 5)."""
    n = git.n
    werte = []
    for kap in KAPPA:
        ks = []
        for i in range(1, n):
            for sg in (1.0, -1.0):
                k = np.zeros(n)
                k[i] = sg * kap
                ks.append(k)
        sp = spektrum(git, eT, np.array(ks), B, quelle_index)
        werte.append(np.mean(sp["F"], axis=0).real)
    rich = (4.0 * werte[1] - werte[0]) / 3.0
    return rich, float(np.max(np.abs(werte[1] - werte[0])))


# ======================================================================= Kalibrierung (konstante Kruemmung)
def hd_statisch(phi, teil):
    """Zweite Ableitungen Hd[m,n,a,b] = d_a d_b h_mn fuer h_tt = 2 Phi_q (N) bzw. h_ij = -2 Phi_q delta_ij (S)."""
    Hd = np.zeros((4, 4, 4, 4))
    if teil == "N":
        Hd[TAU, TAU, 1:, 1:] = 2.0 * phi
    else:
        for k in range(1, 4):
            Hd[k, k, 1:, 1:] = -2.0 * phi
    return Hd


def riemann(Hd):
    """R_mnrs = 1/2 (d_n d_r h_ms + d_m d_s h_nr - d_m d_r h_ns - d_n d_s h_mr)."""
    return 0.5 * (np.einsum("msnr->mnrs", Hd) + np.einsum("nrms->mnrs", Hd)
                  - np.einsum("nsmr->mnrs", Hd) - np.einsum("mrns->mnrs", Hd))


def hd_rnc(R):
    """Riemann-Normalkoordinaten h_mn = -(1/3) R_manb x^a x^b."""
    return -(1.0 / 3.0) * (np.einsum("manb->mnab", R) + np.einsum("mbna->mnab", R))


def ds_quadratisch(git, Hd, pos, d):
    """Linienintegral von h = 1/2 Hd x x laengs der Kante (pos, d): exakt fuer quadratisches h."""
    dv = git.dirs[d].astype(float)
    p = pos.astype(float)
    Q = np.einsum("m,n,mnab->ab", dv, dv, Hd)
    return 0.5 * (np.einsum("ia,ab,ib->i", p, Q, p) + p @ (Q @ dv) + dv @ Q @ dv / 3.0)


def eps_kinematisch(git, eT, Hd, p0=None):
    p0 = np.zeros(4, dtype=np.int64) if p0 is None else p0
    eps = np.zeros(git.nH)
    for d in range(git.nE):
        tau, Rp, val = eT[d]
        np.add.at(eps, tau, val * ds_quadratisch(git, Hd, Rp + p0[None, :], d))
    return eps


class Kalibrierung:
    def __init__(self, git, eT, B):
        self.git, self.eT = git, eT
        Am, Em, M = git.matrizen(np.zeros((1, 4)), eT)
        self.A0, self.E0, self.M0 = Am[0].real, Em[0].real, 0.5 * (M[0].real + M[0].real.T)
        C, _ = R4.komplement(git, B)
        self.C4 = C[:, 1:]
        self.K44 = self.C4.T @ self.M0 @ self.C4

    def antwort(self, Hd, versklavt=True, projiziert=True):
        e = eps_kinematisch(self.git, self.eT, Hd)
        if versklavt:
            r = self.A0.T @ e
            w = -np.linalg.solve(self.K44, self.C4.T @ r)
            e = e + self.E0 @ (self.C4 @ w)
        if projiziert:
            e = projiziere(self.E0[:, self.git.top], e)[0]
        return e

    def basis(self, versklavt=True, projiziert=True):
        """Antwort auf die 6 Basis-Phi (xx, yy, zz, xy, xz, yz) je Teil N und S: (50, 6)."""
        out = {}
        for teil in ("N", "S"):
            cols = []
            for (a, b) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
                phi = np.zeros((3, 3))
                phi[a, b] = phi[b, a] = 1.0
                cols.append(self.antwort(hd_statisch(phi, teil), versklavt, projiziert))
            out[teil] = np.array(cols).T
        return out


def phi_vektor(phi):
    """Koeffizienten zur Basis (xx, yy, zz, xy, xz, yz) fuer symmetrisches phi (Basis xy = E_xy + E_yx)."""
    return np.stack([phi[..., 0, 0], phi[..., 1, 1], phi[..., 2, 2], phi[..., 0, 1], phi[..., 0, 2], phi[..., 1, 2]], -1)


def phi_punkt(y):
    """d_i d_j Phi fuer Phi = -G M/r an den Orten y (m, 3)."""
    r2 = np.sum(y * y, -1)
    r = np.sqrt(r2)
    return -GM * (3.0 * y[..., :, None] * y[..., None, :] - r2[..., None, None] * np.eye(3)) / r[..., None, None] ** 5


def phi_bilder(c, L):
    """Kubische Bildsumme sum_{n != 0, |n|_inf <= N_BILD} d_i d_j Phi(c + n L)."""
    rng = np.arange(-N_BILD, N_BILD + 1)
    nn = np.array([v for v in itertools.product(rng, rng, rng) if any(v)], float)
    out = np.zeros((len(c), 3, 3))
    for i, ci in enumerate(c):
        out[i] = np.sum(phi_punkt(ci[None, :] + L * nn), axis=0)
    return out


# ======================================================================= Auswertung je L (4D)
def typ(git, a, b):
    ea = tuple(1 if i == a else 0 for i in range(4))
    eb = tuple(1 if i == b else 0 for i in range(4))
    return git.gtyp_index[(ea, eb)], git.gtyp_index[(eb, ea)]


def quadrate(git, eps, L, ebene, basen, bg, resp, resp_kin=None):
    """Paar-gemittelte Quadrate (ebene = (mu, nu)) an raeumlichen Basen; Rohwert, Hintergrund, Bild, Vorhersagen."""
    mu, nu = ebene
    t1, t2 = typ(git, mu, nu)
    basen = np.array(basen, dtype=np.int64)
    off = np.zeros(3)
    for a in (mu, nu):
        if a != TAU:
            off[a - 1] += 0.5
    cen = basen + off[None, :]
    roh = np.array([0.5 * (eps[t1][tuple(np.mod(p, L))] + eps[t2][tuple(np.mod(p, L))]) for p in basen])
    hg = 0.5 * (bg[t1] + bg[t2]) / L ** 3 * np.ones(len(basen))
    rN = 0.5 * (resp["N"][t1] + resp["N"][t2])
    rS = 0.5 * (resp["S"][t1] + resp["S"][t2])
    pv = phi_vektor(phi_punkt(cen))
    bv = phi_vektor(phi_bilder(cen, L))
    out = {"ebene": [int(mu), int(nu)], "basen": basen.tolist(), "zentren": cen.tolist(),
           "r": np.linalg.norm(cen, axis=1).tolist(), "roh": roh.tolist(), "hintergrund": hg.tolist(),
           "bild": (bv @ (rN + rS)).tolist(), "PN": (pv @ rN).tolist(), "PS": (pv @ rS).tolist()}
    if resp_kin is not None:
        kN = 0.5 * (resp_kin["N"][t1] + resp_kin["N"][t2])
        kS = 0.5 * (resp_kin["S"][t1] + resp_kin["S"][t2])
        out["PN_kin"] = (pv @ kN).tolist()
        out["PS_kin"] = (pv @ kS).tolist()
    return out


def mittel(q):
    """Mittel ueber die Quadrate einer Gruppe; korrigiert = roh + Hintergrund - Bild."""
    roh, hg, bild = np.mean(q["roh"]), np.mean(q["hintergrund"]), np.mean(q["bild"])
    out = {"roh": float(roh), "korr": float(roh + hg - bild), "hintergrund": float(hg), "bild": float(bild),
           "PN": float(np.mean(q["PN"])), "PS": float(np.mean(q["PS"]))}
    if "PN_kin" in q:
        out["PN_kin"] = float(np.mean(q["PN_kin"]))
        out["PS_kin"] = float(np.mean(q["PS_kin"]))
    return out


def gamma_kin(a, b):
    """Bericht: 2x2-Loesung mit kinematischer (nicht versklavter) Kalibrierung."""
    Mm = np.array([[a["PN_kin"], a["PS_kin"]], [b["PN_kin"], b["PS_kin"]]])
    al, be = np.linalg.solve(Mm, np.array([a["korr"], b["korr"]]))
    return float(be / al), float(al)


def zwei_mal_zwei(a, b):
    """[a_korr; b_korr] = [[a_PN, a_PS]; [b_PN, b_PS]] [alpha; beta]."""
    Mm = np.array([[a["PN"], a["PS"]], [b["PN"], b["PS"]]])
    al, be = np.linalg.solve(Mm, np.array([a["korr"], b["korr"]]))
    return float(al), float(be), float(np.linalg.cond(Mm))


def auswertung_L(git, eps, ds_tau, L, bg, resp, resp_kin):
    out = {"L": L}
    # Achse: tau-x-Quadrate auf der Achse (Zentren x0 + 1/2), y-z-Quadrate um die Achse (Zentren (x0, +-1/2, +-1/2))
    achse = []
    for x0 in range(1, L // 2):
        qa = quadrate(git, eps, L, (TAU, XA), [(x0 - 1, 0, 0), (x0, 0, 0)], bg, resp, resp_kin)
        qb = quadrate(git, eps, L, (YA, ZA), [(x0, 0, 0), (x0, -1, 0), (x0, 0, -1), (x0, -1, -1)], bg, resp, resp_kin)
        a, b = mittel(qa), mittel(qb)
        al, be, cond = zwei_mal_zwei(a, b)
        gk, ak = gamma_kin(a, b)
        achse.append({"x0": x0, "r": float(x0), "tx": a, "yz": b, "alpha": al, "beta": be, "gamma": be / al,
                      "kondition": cond, "verhaeltnis_naiv": a["korr"] / b["korr"],
                      "verhaeltnis_ort": (a["korr"] / (a["PN"] + a["PS"])) / (b["korr"] / (b["PN"] + b["PS"])),
                      "gamma_kin": gk, "alpha_kin": ak})
    out["achse"] = achse
    # Einzelquadrate (tau, x) auf der Achse fuer r^3-Profil, Zentren r = x0 + 1/2
    out["tx_quadrate"] = quadrate(git, eps, L, (TAU, XA), [(x0, 0, 0) for x0 in range(0, L // 2)], bg, resp)
    # Diagonale (1,1,0): (tau, z)-Quadrate (Zentren (n,n,+-1/2)) gegen (x, y)-Quadrate (Zentren (n+-1/2, n+-1/2, 0))
    diag = []
    for nd in range(1, int((L // 2 - 1) / np.sqrt(2.0)) + 1):
        qa = quadrate(git, eps, L, (TAU, ZA), [(nd, nd, 0), (nd, nd, -1)], bg, resp, resp_kin)
        qb = quadrate(git, eps, L, (XA, YA), [(nd, nd, 0), (nd - 1, nd - 1, 0), (nd - 1, nd, 0), (nd, nd - 1, 0)],
                      bg, resp, resp_kin)
        a, b = mittel(qa), mittel(qb)
        al, be, cond = zwei_mal_zwei(a, b)
        gk, ak = gamma_kin(a, b)
        diag.append({"n": nd, "r": float(nd * np.sqrt(2.0)), "tz": a, "xy": b, "alpha": al, "beta": be,
                     "gamma": be / al, "kondition": cond, "verhaeltnis_naiv": a["korr"] / b["korr"],
                     "gamma_kin": gk, "alpha_kin": ak})
    out["diagonale"] = diag
    # Potentialprobe (beschreibend): delta s_tau = 2 Phi_L, Phi_L = -GM/r - GM xi/L - (2 pi/3) GM r^2/L^3
    pot = []
    for x0 in range(1, L // 2 + 1):
        v = ds_tau[x0, 0, 0]
        korr = v + 2 * GM * XI / L + (4 * np.pi / 3) * GM * x0 ** 2 / L ** 3
        pot.append({"r": x0, "ds_tau": float(v), "f": float(-x0 * korr / (2 * GM))})
    out["potential_achse"] = pot
    out["ds_tau_quelle"] = float(ds_tau[0, 0, 0])
    return out


# ======================================================================= 3D-Kontrolle
def kontrolle_3d(L3, log):
    t0 = time.time()
    g3 = R4.Gitter(3, 4)
    J, wdiff = jacobi_komplex(g3)
    eK = eT_aus_dic(g3, g3.eT_aus_J(J))
    eT3, fehler, _ = g3.ableitung_T()
    out = {"winkel_gram_gegen_winkel": wdiff, "weg_K_gegen_T": vergleich_stencil(eK, eT3),
           "weg_T_fehlerschaetzung": float(max(fehler)),
           "flach_max_abs_eps": float(np.max(np.abs(g3.fehlwinkel(g3.s0))))}
    eps, _, kont, _ = loese_torus(g3, eK, L3, None, 0, log)
    bg, bgd = hintergrund(g3, eK, None, 0)
    tz = g3.gtyp_index[((1, 0, 0),)]
    korr = eps + (bg / L3 ** 2)[:, None, None]
    soll = 8.0 * np.pi * GM
    wl = float(korr[tz, 0, 0])
    maske = np.ones_like(korr, bool)
    maske[tz, 0, 0] = False
    out.update({"kontrollen_loesung": kont, "hintergrund": bg.tolist(), "hintergrund_kappa_diff": bgd,
                "zeit_gelenk": int(tz), "eps_weltlinie": wl, "soll_8piGM": soll,
                "weltlinie_rel_abw": abs(wl / soll - 1.0),
                "ausserhalb_max_rel": float(np.max(np.abs(korr[maske])) / soll),
                "roh_ausserhalb_max_rel": float(np.max(np.abs(np.where(maske, eps, 0.0))) / soll),
                "L3": L3, "laufzeit_s": time.time() - t0})
    # Bilddaten: |eps_korr| der Zeitgelenke und groesster Wert ueber die Raumgelenke je Ort
    out["bild_zeit"] = np.abs(korr[tz]).tolist()
    raum = [h for h in range(g3.nH) if h != tz]
    out["bild_raum_max"] = np.max(np.abs(korr[raum]), axis=0).tolist()
    protokoll(log, f"3D: WL {wl:.15g} (soll {soll:.15g}), ausserhalb {out['ausserhalb_max_rel']:.2e}")
    return out


# ======================================================================= Hauptlauf
def main():
    ziel = sys.argv[1]
    Ls = [int(x) for x in sys.argv[2].split(",")]
    L3 = int(sys.argv[3])
    t0 = time.time()
    log = []
    res = {"skript_sha256": SKRIPT_SHA, "numpy": np.__version__, "Ls": Ls, "L3": L3,
           "zeit_utc_start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    git = R4.Gitter(4, 4)
    eps0 = git.fehlwinkel(git.s0)
    eT, fehler, betroffen = git.ableitung_T()
    J4, wdiff4 = jacobi_komplex(git)
    eK4 = eT_aus_dic(git, git.eT_aus_J(J4))
    res["geometrie"] = {"flach_max_abs_eps": float(np.max(np.abs(eps0))),
                        "weg_T_fehlerschaetzung": float(max(fehler)), "weg_T_betroffen": betroffen,
                        "weg_K_gegen_T": vergleich_stencil(eK4, eT), "winkel_gram_gegen_winkel": wdiff4}
    protokoll(log, f"4D Geometrie: flach {res['geometrie']['flach_max_abs_eps']:.1e}, K gegen T "
                   f"{res['geometrie']['weg_K_gegen_T']:.1e} ({time.time() - t0:.1f} s)")
    B = git.B0()
    typen = {"tx": typ(git, TAU, XA), "yz": typ(git, YA, ZA), "tz": typ(git, TAU, ZA), "xy": typ(git, XA, YA)}
    res["typen"] = {k: [int(v[0]), int(v[1])] for k, v in typen.items()}
    res["gelenktypen"] = [[list(map(int, s)) for s in t] for t in git.gtypen]
    # Kalibrierung und ihre Kontrollen
    kal = Kalibrierung(git, eT, B)
    resp = kal.basis(True)
    resp_kin = kal.basis(False)
    rng = np.random.default_rng(20261004)
    kk = {}
    for teil in ("N", "S"):
        A = rng.standard_normal((3, 3))
        phi = A + A.T
        Hd = hd_statisch(phi, teil)
        R = riemann(Hd)
        e_stat = eps_kinematisch(git, eT, Hd)
        e_rnc = eps_kinematisch(git, eT, hd_rnc(R))
        e_versch = eps_kinematisch(git, eT, Hd, p0=np.array([2, 3, -2, 1]))
        kk[teil] = {"rnc_gegen_statisch_rel": float(np.max(np.abs(e_rnc - e_stat)) / np.max(np.abs(e_stat))),
                    "rnc_riemann_rel": float(np.max(np.abs(riemann(hd_rnc(R)) - R)) / np.max(np.abs(R))),
                    "verschiebung_rel": float(np.max(np.abs(e_versch - e_stat)) / np.max(np.abs(e_stat))),
                    "versklavung_rel": float(np.max(np.abs(kal.antwort(Hd, True, True) - kal.antwort(Hd, False, True)))
                                             / np.max(np.abs(kal.antwort(Hd, False, True)))),
                    "projektion_rel": float(np.max(np.abs(kal.antwort(Hd, False, True) - e_stat))
                                            / np.max(np.abs(e_stat)))}
    # Antwort auf die Punktmassen-Kruemmung auf der Achse (Einheit 2GM/r^3 = 1, d. h. Phi = diag(-1, 1/2, 1/2))
    phi_ax = np.diag([-1.0, 0.5, 0.5])
    ant = {}
    for teil in ("N", "S"):
        for nm, rr in (("versklavt", resp), ("kinematisch", resp_kin)):
            v = rr[teil] @ phi_vektor(phi_ax)
            ant[f"{teil}_{nm}"] = {k: [float(v[t[0]]), float(v[t[1]])] for k, t in typen.items()}
    # Sektionalkruemmungen der beiden Teile (Kontrolle der Formeln)
    sek = {}
    for teil in ("N", "S"):
        R = riemann(hd_statisch(phi_ax, teil))
        sek[teil] = {f"K{a}{b}": float(R[a, b, a, b]) for a, b in itertools.combinations(range(4), 2)}
    res["kalibrierung"] = {"kontrollen": kk, "antwort_achse_einheit": ant, "sektional_achse": sek,
                           "K44_eigen": np.linalg.eigvalsh(kal.K44).tolist(),
                           "resp_N": resp["N"].tolist(), "resp_S": resp["S"].tolist(),
                           "resp_kin_N": resp_kin["N"].tolist(), "resp_kin_S": resp_kin["S"].tolist()}
    protokoll(log, f"Kalibrierung fertig ({time.time() - t0:.1f} s): {json.dumps(kk)}")
    # Fixierung: Kontrollen (frei von Diagonalmode und Eichmoden, 2 pi-periodisch)
    ks_t = np.column_stack([np.zeros(16), rng.uniform(-np.pi, np.pi, (16, 3))])
    dirs = git.dirs.astype(float)
    _, Em_t, _ = git.matrizen(ks_t, eT)
    v_t = Em_t[:, :, git.top]
    u_r = rng.standard_normal((16, git.nE))
    e1 = projiziere(v_t, np.einsum("kta,ka->kt", Em_t, u_r))[0]
    u2 = u_r.copy()
    u2[:, git.top] += 3.7
    e2 = projiziere(v_t, np.einsum("kta,ka->kt", Em_t, u2))[0]
    g1 = np.sin(0.5 * ks_t @ dirs.T) * dirs[None, :, 2]
    e3 = projiziere(v_t, np.einsum("kta,ka->kt", Em_t, u_r + 5.0 * g1))[0]
    ks_p = ks_t.copy()
    ks_p[:, 1] += 2.0 * np.pi
    sp1 = spektrum(git, eT, ks_t, B, 0)
    sp2 = spektrum(git, eT, ks_p, B, 0)
    sp3 = spektrum(git, eT, -ks_t, B, 0)
    res["fixierung_kontrollen"] = {
        "diagonalmode_rel": float(np.max(np.abs(e2 - e1)) / np.max(np.abs(e1))),
        "eichmode_rel": float(np.max(np.abs(e3 - e1)) / np.max(np.abs(e1))),
        "periodisch_F_rel": float(np.max(np.abs(sp2["F"] - sp1["F"])) / np.max(np.abs(sp1["F"]))),
        "periodisch_F_ohne_rel": float(np.max(np.abs(sp2["F_ohne"] - sp1["F_ohne"])) / np.max(np.abs(sp1["F_ohne"]))),
        "reell_F_minus_k_rel": float(np.max(np.abs(sp3["F"] - np.conj(sp1["F"]))) / np.max(np.abs(sp1["F"]))),
        "E_top_norm_min_stichprobe": float(np.min(np.linalg.norm(v_t, axis=1)))}
    # Hintergrund (Kleink-Mittel)
    bg, bgd = hintergrund(git, eT, B, 0)
    res["hintergrund"] = {"F0_mittel": bg.tolist(), "kappa_diff_max": bgd}
    protokoll(log, f"Hintergrund: max |F0| {np.max(np.abs(bg)):.4g}, kappa-Diff {bgd:.2e}")
    # Torus je L
    res["laeufe"] = []
    for L in Ls:
        eps, ds_tau, kont, eps_ohne = loese_torus(git, eT, L, B, 0, log)
        aus = auswertung_L(git, eps, ds_tau, L, bg, resp, resp_kin)
        aus["kontrollen"] = kont
        # Bericht: Achsenquadrate ohne Fixierung der Hyperdiagonale (u_top = 0), roh, nicht torus-korrigiert
        t_tx, t_yz = typ(git, TAU, XA), typ(git, YA, ZA)
        ohne = []
        for x0 in range(1, L // 2):
            vtx = np.mean([0.5 * (eps_ohne[t_tx[0]][p] + eps_ohne[t_tx[1]][p]) for p in ((x0 - 1, 0, 0), (x0, 0, 0))])
            vyz = np.mean([0.5 * (eps_ohne[t_yz[0]][tuple(np.mod(p, L))] + eps_ohne[t_yz[1]][tuple(np.mod(p, L))])
                           for p in ((x0, 0, 0), (x0, -1, 0), (x0, 0, -1), (x0, -1, -1))])
            ohne.append({"x0": x0, "tx_roh": float(vtx), "yz_roh": float(vyz)})
        aus["achse_ohne_fixierung"] = ohne
        res["laeufe"].append(aus)
        g6 = [a["gamma"] for a in aus["achse"] if 6 <= a["r"] <= L // 2 - 2]
        protokoll(log, f"L={L}: Kontrollen {json.dumps(kont)}; Punkte im Bereich {len(g6)} "
                       f"({time.time() - t0:.1f} s)")
        with open(ziel + ".teil", "w") as f:
            json.dump(res, f)
    res["kontrolle_3d"] = kontrolle_3d(L3, log)
    res["laufzeit_s"] = time.time() - t0
    res["protokoll"] = log
    with open(ziel, "w") as f:
        json.dump(res, f, indent=1)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
