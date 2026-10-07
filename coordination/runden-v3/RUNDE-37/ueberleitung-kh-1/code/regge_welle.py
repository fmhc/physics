#!/usr/bin/env python3
"""REGGE-WELLE-1 (Runde 37, Code-Agent): euklidische Hesse-Form des 4D-Kuhn-Gitters, fortgesetzt zu echter Zeit.

Grundlage: RUNDE-36/regge-4d-1/code/regge4d.py (Gitter, Weg T, Ableitungen), unveraendert importiert.

  k = (k_tau, k_s), tau = Gitterachse 0 (PLAN [F1]). M(k) = A(-k)^T E(k) ist analytisch in k und fuer reelles k gleich
  A(k)^+ E(k) aus REGGE-4D-1. Nach Abzug der Dreiecksschwerpunkte (hebt sich heraus) haben alle Zeitversaetze die Form
  m/2, also M(k_tau, k_s) = sum_m C_m(k_s) z^m mit z = exp(i k_tau / 2) = exp(-omega / 2) fuer k_tau = i omega.
  Reduktion: festes reelles Komplement Q0 der 5 Nullvektoren bei k_tau = 0 (4 Gitter-Eichmoden + Hyperdiagonale),
  F(omega) = Q0^T M(i omega, k_s) Q0 (10 x 10, analytisch in omega). Nullstellen von d = det F in der komplexen
  omega-Ebene: alle per Polynom-Eigenwertproblem in z, Verfeinerung (Aberth) auf F, Zaehlung per Windungszahl auf dem
  Rand von R = [0, 3|k|] x [-0,5|k|, 0,5|k|], Pruefungen (PLAN Abschnitt 3 und 5).

Aufruf: python regge_welle.py <modus: rauch | haupt> <ausgabe.json>
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import regge4d as R4  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
R4_SHA = hashlib.sha256(open(os.path.join(HIER, "regge4d.py"), "rb").read()).hexdigest()

TAU = 0
SP = [1, 2, 3]
BETRAEGE = [0.05, 0.1, 0.2, 0.4, 0.8]         # Karte
RAUCH_BETRAEGE = [0.3, 0.6]                    # Rauchlauf: nicht geurteilte Betraege (PLAN Abschnitt 8)
R_RE, R_IM = 3.0, 0.5                          # Bereich R (PLAN [F4])
N_ACHSE = 1500                                 # reelle Achse (0, 3|k|]
N_RAND_H, N_RAND_V = 2000, 400                 # Randpunkte je waagrechter / senkrechter Seite
PHASE_MAX = 0.5                                # groesster Phasensprung zwischen Randpunkten (rad)
RHO_MIN = 0.05                                 # Sperre Komplement (PLAN [F7])
S_WURZEL = 1e-9                                # Sperre Wurzelpruefung
PHYS_MIN = 0.1                                 # Sperre: Kernvektor ausserhalb des Nullraums
GEIST_RE_MAX = 2.4                             # beschreibend: alle Nullstellen mit Re omega <= 2,4
TRIM_REL = 1e-10                               # Laurent-Koeffizienten unter TRIM_REL * max werden im PEP weggelassen
H_KOMPLEX = 1e-20
BATCH = 4096


def protokoll(log, s):
    print(s, flush=True)
    log.append(s)


def richtungen():
    """24 raeumliche Richtungen (PLAN [F3]): 12 feste (mit Paaren n/-n und einer S3-Kopie) + 12 Fibonacci-Punkte."""
    roh = [("x+", (1, 0, 0)), ("x-", (-1, 0, 0)), ("xy+", (1, 1, 0)), ("xy-", (-1, -1, 0)), ("x-y", (1, -1, 0)),
           ("xyz+", (1, 1, 1)), ("xyz-", (-1, -1, -1)), ("xy-z", (1, 1, -1)), ("-x-yz", (-1, -1, 1)),
           ("123", (1, 2, 3)), ("312", (3, 1, 2)), ("-1-2-3", (-1, -2, -3))]
    ga = np.pi * (3.0 - np.sqrt(5.0))
    for i in range(12):
        zz = 1.0 - (2.0 * i + 1.0) / 12.0
        r = np.sqrt(1.0 - zz * zz)
        roh.append((f"fib{i:02d}", (r * np.cos(i * ga), r * np.sin(i * ga), zz)))
    return [(nm, np.array(v, float) / np.linalg.norm(v)) for nm, v in roh]


# ======================================================================= Form als Laurent-Polynom in z
class Form:
    def __init__(self, git, eT):
        self.git = git
        Et, Ed, Ep, Ev = [], [], [], []
        for d in range(git.nE):
            tau, Rp, val = eT[d]
            Et.append(np.asarray(tau))
            Ed.append(np.full(len(tau), d))
            Ep.append(Rp + 0.5 * git.dirs[d][None, :])
            Ev.append(np.asarray(val))
        self.Et, self.Ed = np.concatenate(Et), np.concatenate(Ed)
        self.Ep, self.Ev = np.concatenate(Ep).astype(float), np.concatenate(Ev)
        At, Ad, Ap, Av = [], [], [], []
        for t in range(git.nH):
            for (be, d), a in zip(git.g_kanten[t], git.gelenk_ableitung(t)):
                At.append(t)
                Ad.append(d)
                Ap.append(be + 0.5 * git.dirs[d])
                Av.append(a)
        self.At, self.Ad = np.array(At), np.array(Ad)
        self.Ap, self.Av = np.array(Ap, float), np.array(Av)
        self.pe = np.rint(2 * self.Ep[:, TAU]).astype(int)
        self.pa = np.rint(2 * self.Ap[:, TAU]).astype(int)
        assert np.max(np.abs(2 * self.Ep[:, TAU] - self.pe)) < 1e-12
        assert np.max(np.abs(2 * self.Ap[:, TAU] - self.pa)) < 1e-12

    def koeffizienten(self, ks):
        """C_m(k_s) fuer reelles k_s: dict m -> (nE, nE) komplex; M = sum_m C_m z^m, z = exp(i k_tau/2)."""
        git = self.git
        phE = self.Ev * np.exp(1j * (self.Ep[:, SP] @ ks))
        phA = self.Av * np.exp(-1j * (self.Ap[:, SP] @ ks))
        Er, Aq = {}, {}
        for r in sorted(set(self.pe.tolist())):
            m = self.pe == r
            X = np.zeros((git.nH, git.nE), complex)
            np.add.at(X, (self.Et[m], self.Ed[m]), phE[m])
            Er[r] = X
        for q in sorted(set(self.pa.tolist())):
            m = self.pa == q
            X = np.zeros((git.nH, git.nE), complex)
            np.add.at(X, (self.At[m], self.Ad[m]), phA[m])
            Aq[q] = X
        C = {}
        for r, X in Er.items():
            for q, Y in Aq.items():
                mm = int(r - q)
                C[mm] = C.get(mm, 0) + Y.T @ X
        return C


def laurent(C, z, abl=False):
    """sum_m C_m z^m (und d/d omega = sum_m (-m/2) C_m z^m) fuer ein Feld z."""
    z = np.atleast_1d(np.asarray(z, complex))
    n = next(iter(C.values())).shape[0]
    F = np.zeros((len(z), n, n), complex)
    dF = np.zeros((len(z), n, n), complex) if abl else None
    for m, Cm in C.items():
        zm = z ** m
        F += zm[:, None, None] * Cm[None]
        if abl:
            dF += (-0.5 * m) * zm[:, None, None] * Cm[None]
    return (F, dF) if abl else F


def nullbasis(git, ktau, ks):
    """Analytische Nullvektoren je k = (k_tau, k_s): Gitter-Eichmoden sin(k.d/2) d_mu (4) und e_top: (Nz, nE, 5)."""
    ktau = np.atleast_1d(np.asarray(ktau, complex))
    dirs = git.dirs.astype(float)
    ph = 0.5 * (ktau[:, None] * dirs[None, :, TAU] + (dirs[:, SP] @ ks)[None, :])
    G = np.sin(ph)[:, :, None] * dirs[None, :, :]
    et = np.zeros((len(ktau), git.nE, 1), complex)
    et[:, git.top, 0] = 1.0
    return np.concatenate([G, et], axis=2)


def rho(Qn0, N):
    """Regularitaet des Komplements: sigma_min(Qn0^T Qn(omega)), Qn orthonormale Basis von range N (PLAN [F7])."""
    Qn, _ = np.linalg.qr(N)
    return np.linalg.svd(np.einsum("ai,kaj->kij", Qn0, Qn), compute_uv=False)[:, -1]


# ======================================================================= Nullstellen
def pep_wurzeln(Fm):
    """Alle Nullstellen von det sum_m F_m z^m (Begleitmatrix), als omega = -2 log z (Hauptzweig)."""
    mx = max(np.max(np.abs(v)) for v in Fm.values())
    behalten = {m: v for m, v in Fm.items() if np.max(np.abs(v)) > TRIM_REL * mx}
    weg = max([float(np.max(np.abs(v))) / mx for m, v in Fm.items() if m not in behalten] + [0.0])
    ms = sorted(behalten)
    m0, D = ms[0], ms[-1] - ms[0]
    n = next(iter(Fm.values())).shape[0]
    P = [behalten.get(m0 + j, np.zeros((n, n), complex)) for j in range(D + 1)]
    A = np.zeros((n * D, n * D), complex)
    B = np.eye(n * D, dtype=complex)
    if D > 1:
        A[:n * (D - 1), n:] = np.eye(n * (D - 1))
    for j in range(D):
        A[n * (D - 1):, n * j:n * (j + 1)] = -P[j]
    B[n * (D - 1):, n * (D - 1):] = P[D]
    al, be = sla.eig(A, B, right=False, homogeneous_eigvals=True)
    ok = (np.abs(be) > 1e-13 * np.abs(al)) & (np.abs(al) > 1e-300)
    zz = al[ok] / be[ok]
    zz = zz[np.abs(zz) > 1e-300]
    return -2.0 * np.log(zz), {"m_bereich": [int(m0), int(ms[-1])], "grad": int(D), "weggelassen_rel_max": weg,
                               "eigenwerte_endlich": int(len(zz)), "eigenwerte_gesamt": int(n * D)}


def logabl(Fm, w):
    F, dF = laurent(Fm, np.exp(-0.5 * np.asarray(w)), abl=True)
    return np.trace(np.linalg.solve(F, dF), axis1=1, axis2=2)


def aberth(Fm, w0, skala, maxit=80):
    w = np.array(w0, complex)
    schritt = np.inf
    for it in range(maxit):
        L = logabl(Fm, w)
        diff = w[:, None] - w[None, :]
        np.fill_diagonal(diff, np.inf)
        S = np.sum(1.0 / diff, axis=1)
        st = 1.0 / (L - S)
        w = w - st
        schritt = float(np.max(np.abs(st)))
        if schritt < 1e-14 * skala:
            break
    return w, it + 1, schritt


def s_wert(Fm, w):
    F = laurent(Fm, np.exp(-0.5 * np.asarray(w)))
    sv = np.linalg.svd(F, compute_uv=False)
    return sv[:, -1] / sv[:, 0], sv


def randpunkte(kb, faktor):
    """Rand von R gegen den Uhrzeigersinn: unten, rechts, oben, links (geschlossen)."""
    nh, nv = N_RAND_H * faktor, N_RAND_V * faktor
    a, b, h = 0.0, R_RE * kb, R_IM * kb
    unten = np.linspace(a, b, nh, endpoint=False) - 1j * h
    rechts = b + 1j * np.linspace(-h, h, nv, endpoint=False)
    oben = np.linspace(b, a, nh, endpoint=False) + 1j * h
    links = a + 1j * np.linspace(h, -h, nv, endpoint=False)
    p = np.concatenate([unten, rechts, oben, links])
    return np.concatenate([p, p[:1]])


def windung(Fm, kb):
    for faktor in (1, 2, 4):
        p = randpunkte(kb, faktor)
        ph = []
        for a in range(0, len(p), BATCH):
            F = laurent(Fm, np.exp(-0.5 * p[a:a + BATCH]))
            sgn, _ = np.linalg.slogdet(F)
            ph.append(np.angle(sgn))
        ph = np.concatenate(ph)
        dph = np.angle(np.exp(1j * np.diff(ph)))
        mx = float(np.max(np.abs(dph)))
        w = float(np.sum(dph) / (2 * np.pi))
        if mx < PHASE_MAX:
            break
    return {"windung": w, "zahl": int(round(w)), "rest": abs(w - round(w)), "max_phasensprung": mx,
            "faktor": faktor, "punkte": int(len(p))}


def h_basis(git):
    basis, namen = git.sym_basis()
    return basis, namen


def h_tensor(basis, hv):
    return sum(c * X for c, X in zip(hv, basis))


def tt_anteil(H, n):
    """Anteil des raeumlichen TT-Teils (transversal zu n, spurfrei) an der Frobeniusnorm von H (4 x 4)."""
    Hs = H[1:, 1:]
    P = np.eye(3) - np.outer(n, n)
    Htt = P @ Hs @ P - 0.5 * P * np.trace(P @ Hs)
    nl = np.linalg.norm(H)
    zeit = np.sqrt(abs(H[0, 0]) ** 2 + 2 * np.sum(np.abs(H[0, 1:]) ** 2))
    return float(np.linalg.norm(Htt) / nl), float(zeit / nl)


def tt_kanten(git, B, n):
    """Orthonormalbasis (15 x 2) der Kontinuums-TT-Moden h_+, h_x (raeumlich, transversal zu n, spurfrei) im
    Kantenraum: B0 h."""
    basis, _ = git.sym_basis()
    U, _, _ = np.linalg.svd(np.outer(n, n))
    Ea, Eb = np.concatenate([[0.0], U[:, 1]]), np.concatenate([[0.0], U[:, 2]])
    hp = (np.outer(Ea, Ea) - np.outer(Eb, Eb)) / np.sqrt(2)
    hx = (np.outer(Ea, Eb) + np.outer(Eb, Ea)) / np.sqrt(2)
    T = np.array([[np.sum(X * hp) for X in basis], [np.sum(X * hx) for X in basis]]).T
    QT, _ = np.linalg.qr(B @ T)
    return QT


def tt_klasse(u, Nw, QT):
    """Eichinvarianter TT-Anteil der Klasse u + range(N) (Fassung nach Rauchlauf 1, PLAN Abschnitt 9):
    w = u + N c mit c = argmin abs((I - P_T)(u + N c)); Rueckgabe abs(P_T w)/abs(w) und w."""
    R = np.eye(len(u)) - QT @ QT.T
    c, *_ = np.linalg.lstsq(R @ Nw, -(R @ u), rcond=None)
    w = u + Nw @ c
    return float(np.linalg.norm(QT.T @ w) / np.linalg.norm(w)), w


def v0_basis(git, n):
    """6-dim. h-Unterraum ohne Komponenten laengs n (Kontinuums-Komplement bei k_tau = 0), Frobenius-orthonormal.
    Spalten: tt, t ea, t eb (Lapse/Shift), ea ea, eb eb, ea eb."""
    basis, _ = git.sym_basis()
    U, _, _ = np.linalg.svd(np.outer(n, n))
    ea, eb = U[:, 1], U[:, 2]
    t = np.array([1.0, 0, 0, 0])
    Ea, Eb = np.concatenate([[0.0], ea]), np.concatenate([[0.0], eb])
    T = [np.outer(t, t), (np.outer(t, Ea) + np.outer(Ea, t)) / np.sqrt(2), (np.outer(t, Eb) + np.outer(Eb, t)) / np.sqrt(2),
         np.outer(Ea, Ea), np.outer(Eb, Eb), (np.outer(Ea, Eb) + np.outer(Eb, Ea)) / np.sqrt(2)]
    return np.array([[np.sum(X * Tj) for Tj in T] for X in basis])


# ======================================================================= Analyse je (Richtung, Betrag)
def analyse(git, form, B, basis, nm, nhat, kb, mit_eigen=False):
    t0 = time.time()
    ks = kb * nhat
    C = form.koeffizienten(ks)
    N0 = nullbasis(git, [0.0], ks)[0].real
    U, sv0, _ = np.linalg.svd(N0, full_matrices=True)
    Qn0, Q0 = U[:, :5], U[:, 5:]
    Fm = {m: Q0.T @ Cm @ Q0 for m, Cm in C.items()}
    out = {"richtung": nm, "n": nhat.tolist(), "betrag": kb, "N0_sing_rel_min": float(sv0[-1] / sv0[0])}
    # --- reelle Achse
    om = R_RE * kb * np.arange(1, N_ACHSE + 1) / N_ACHSE
    z = np.exp(-0.5 * om)
    M = laurent(C, z)
    F = np.einsum("ai,kab,bj->kij", Q0, M, Q0)
    svF = np.linalg.svd(F, compute_uv=False)
    s = svF[:, -1] / svF[:, 0]
    s2 = svF[:, -2] / svF[:, 0]
    Nn = nullbasis(git, 1j * om, ks)
    MN = np.einsum("kab,kbj->kaj", M, Nn)
    normM = np.linalg.norm(M, 2, axis=(1, 2))
    res = np.max(np.linalg.norm(MN, axis=1) / np.linalg.norm(Nn, axis=1), axis=1) / normM
    sym = np.max(np.abs(M - np.swapaxes(M, 1, 2)), axis=(1, 2)) / np.max(np.abs(M), axis=(1, 2))
    Fm_neg = laurent(C, np.exp(0.5 * om))
    Fneg = np.einsum("ai,kab,bj->kij", Q0, Fm_neg, Q0)
    zeitumkehr = np.linalg.norm(Fneg - np.conj(F), axis=(1, 2)) / np.linalg.norm(F, axis=(1, 2))
    rho_achse = rho(Qn0, Nn)
    lokmin = [int(i) for i in range(1, len(s) - 1) if s[i] < s[i - 1] and s[i] <= s[i + 1]]
    sgn_d, _ = np.linalg.slogdet(F)
    out["achse"] = {"omega": om[4::5].tolist(), "s": s[4::5].tolist(), "s2": s2[4::5].tolist(),
                    "phase_det": np.angle(sgn_d[4::5]).tolist(),
                    "imag_F_rel_max": float(np.max(np.abs(F.imag)) / np.max(np.abs(F))),
                    "lokale_minima": [{"omega": float(om[i]), "s": float(s[i])} for i in lokmin],
                    "null_residuum_max": float(np.max(res)), "symmetrie_max": float(np.max(sym)),
                    "zeitumkehr_max": float(np.max(zeitumkehr)), "rho_min": float(np.min(rho_achse))}
    # Feinsuche der Minima (Brent, beschreibend)
    from scipy.optimize import minimize_scalar
    fein = []
    for i in lokmin:
        a, b = om[max(i - 1, 0)], om[min(i + 1, len(om) - 1)]
        r = minimize_scalar(lambda x: float(s_wert(Fm, np.array([x]))[0][0]), bounds=(a, b), method="bounded",
                            options={"xatol": 1e-13 * kb})
        fein.append({"omega": float(r.x), "s": float(r.fun)})
    out["achse"]["minima_fein"] = fein
    # --- alle Nullstellen (PEP), Verfeinerung in R' (R um 20 % vergroessert)
    wurz, pep_info = pep_wurzeln(Fm)
    out["pep"] = pep_info
    inR2 = (wurz.real >= -0.2 * kb) & (wurz.real <= 1.2 * R_RE * kb) & (np.abs(wurz.imag) <= 1.2 * R_IM * kb)
    kand = wurz[inR2]
    if len(kand):
        verf, nit, letzter = aberth(Fm, kand, kb)
    else:
        verf, nit, letzter = kand, 0, 0.0
    out["aberth"] = {"iterationen": int(nit), "letzter_schritt": float(letzter),
                     "max_verschiebung_rel": float(np.max(np.abs(verf - kand)) / kb) if len(kand) else 0.0}
    inR = (verf.real > 0) & (verf.real <= R_RE * kb) & (np.abs(verf.imag) <= R_IM * kb)
    wR = verf[inR]
    wR = wR[np.argsort(wR.real)]
    sR, _ = s_wert(Fm, wR) if len(wR) else (np.array([]), None)
    # --- Windung
    wd = windung(Fm, kb)
    p = randpunkte(kb, wd["faktor"])
    rho_rand = float(np.min(rho(Qn0, nullbasis(git, 1j * p, ks))))
    wd["rho_rand_min"] = rho_rand
    out["windung"] = wd
    # --- je Nullstelle: Kern, h-Struktur, Physikalitaet, Regularitaet
    QT = tt_kanten(git, B, nhat)
    nst = []
    for w, sw in zip(wR, sR):
        zw = np.exp(-0.5 * w)
        Fw = laurent(Fm, zw)[0]
        _, svw, Vh = np.linalg.svd(Fw)
        v = np.conj(Vh[-1])
        u = Q0 @ v
        Nw = nullbasis(git, [1j * w], ks)[0]
        Qn, _ = np.linalg.qr(Nw)
        phys = float(np.linalg.norm(u - Qn @ (np.conj(Qn).T @ u)) / np.linalg.norm(u))
        # eichinvarianter TT-Anteil (Klasse u + range N), h-Struktur des besten Vertreters
        tt, wv = tt_klasse(u, Nw, QT)
        hv, *_ = np.linalg.lstsq(B.astype(complex), wv, rcond=None)
        gitter_rest = float(np.linalg.norm(wv - B @ hv) / np.linalg.norm(wv))
        _, zeitanteil = tt_anteil(h_tensor(basis, hv), nhat)
        # zweiter Kernvektor (fuer entartete Paare)
        v2 = np.conj(Vh[-2])
        tt2, _ = tt_klasse(Q0 @ v2, Nw, QT)
        nst.append({"re": float(w.real), "im": float(w.imag), "v_re": float(w.real / kb), "v_im": float(w.imag / kb),
                    "s": float(sw), "s2_rel": float(svw[-2] / svw[0]),
                    "rho": float(rho(Qn0, Nw[None])[0]), "physikalisch": phys, "tt_anteil": tt,
                    "zeit_anteil": zeitanteil, "gitter_rest": gitter_rest, "tt_anteil_2": tt2})
    out["nullstellen"] = nst
    # --- Geister (beschreibend): alle PEP-Wurzeln mit 0 < Re <= 2,4 und |Im| <= 0,5 |k| ausserhalb R
    g = wurz[(wurz.real > R_RE * kb) & (wurz.real <= GEIST_RE_MAX) & (np.abs(wurz.imag) <= R_IM * kb)]
    out["geister"] = [{"re": float(x.real), "im": float(x.imag)} for x in np.sort_complex(g)]
    out["pep_naechste_ausserhalb"] = [{"re": float(x.real), "im": float(x.imag)} for x in
                                      sorted(wurz[~inR2], key=lambda x: abs(x - kb))[:4]]
    # --- Kinetik-Matrix der direkten h-Form (beschreibend, Zwangsbedingungen): omega^2-Koeffizient
    K2 = sum((m * m / 8.0) * (B.T @ Cm @ B) for m, Cm in C.items())
    V0 = v0_basis(git, nhat)
    K2r = V0.T @ K2 @ V0
    imag_rel = float(np.max(np.abs(K2r.imag)) / np.max(np.abs(K2r)))
    Uk, sk, Vk = np.linalg.svd(K2r.real)
    W = Vk[3:].T
    out["kinetik"] = {"sing": sk.tolist(), "imag_rel": imag_rel,
                      "lapse_shift_anteil_klein3": float(np.sum(W[:3, :] ** 2) / 3.0),
                      "lapse_shift_anteil_gross3": float(np.sum(Vk[:3].T[:3, :] ** 2) / 3.0),
                      "luecke_s4_durch_s3": float(sk[3] / sk[2])}
    if mit_eigen:
        om2 = R_RE * kb * np.arange(1, 201) / 200
        M2 = laurent(C, np.exp(-0.5 * om2))
        ev = np.linalg.eigvals(M2)
        mod = np.sort(np.abs(ev), axis=1) / np.max(np.abs(ev), axis=1)[:, None]
        out["eigen_M"] = {"omega": om2.tolist(), "betrag_rel_sortiert": mod.tolist()}
    out["laufzeit_s"] = time.time() - t0
    return out, Fm


def stichproben_w0(git, form, eT, rng, log):
    """W0 (a): Laurent-Form bei reellem k gegen git.matrizen (REGGE-4D-1); (b) Nullvektoren bei komplexem k_tau."""
    R = R4.richtungen(4)
    ks = [b * nh for nh in R.values() for b in [0.05, 0.1, 0.2, 0.4]]
    ks = np.array(ks + list(rng.uniform(-np.pi, np.pi, size=(64, 4))))
    _, _, M4 = git.matrizen(ks, eT)
    abw = []
    for k, Mref in zip(ks, M4):
        C = form.koeffizienten(k[SP])
        M = laurent(C, np.exp(0.5j * k[TAU]))[0]
        abw.append(float(np.max(np.abs(M - Mref)) / np.max(np.abs(Mref))))
    # (b) 64 zufaellige komplexe k_tau
    res = []
    for _ in range(64):
        ktau = rng.uniform(-np.pi, np.pi) + 1j * rng.uniform(-2.4, 2.4)
        kss = rng.uniform(-np.pi, np.pi, size=3)
        C = form.koeffizienten(kss)
        M = laurent(C, np.exp(0.5j * ktau))[0]
        N = nullbasis(git, [ktau], kss)[0]
        r = np.max(np.linalg.norm(M @ N, axis=0) / np.linalg.norm(N, axis=0)) / np.linalg.norm(M, 2)
        res.append(float(r))
    protokoll(log, f"W0: (a) max {max(abw):.2e}, (b) zufaellig komplex max {max(res):.2e}")
    return {"a_abw_je_punkt": abw, "a_max": max(abw), "a_punkte": len(abw),
            "b_zufall_residuen": res, "b_zufall_max": max(res)}


# ======================================================================= Gegenprobe Weg K (komplexer Schritt)
def kosinus_gram(git, sq):
    """aus RUNDE-37/regge-zeit-1/code/regge_zeit.py (unveraendert uebernommen)."""
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


def eK_stencil(git):
    sq0 = np.array([[float(np.sum(git.dirs[d] ** 2)) for _, d in git.p_kanten[ip]] for ip in range(git.nP)])
    nEs = len(git.paare)
    J = np.zeros((git.nP, len(git.lok_gelenke), nEs))
    for e in range(nEs):
        sq = sq0.astype(complex)
        sq[:, e] += 1j * H_KOMPLEX
        c = kosinus_gram(git, sq)
        J[:, :, e] = -(c.imag / H_KOMPLEX) / np.sqrt(1.0 - c.real ** 2)
    dic = git.eT_aus_J(J)
    eT = []
    for d in range(git.nE):
        keys = sorted((t, Rr) for (t, dd, Rr) in dic if dd == d)
        tau = np.array([q[0] for q in keys], dtype=np.int64)
        Rp = np.array([q[1] for q in keys], dtype=np.int64).reshape(len(keys), git.n)
        val = np.array([dic[(q[0], d, q[1])] for q in keys])
        eT.append((tau, Rp, val))
    return eT


# ======================================================================= Hauptlauf
def main():
    modus, ziel = sys.argv[1], sys.argv[2]
    t0 = time.time()
    log = []
    res = {"skript_sha256": SKRIPT_SHA, "regge4d_sha256": R4_SHA, "numpy": np.__version__, "modus": modus,
           "zeit_utc_start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "festlegungen": {"R_RE": R_RE, "R_IM": R_IM, "N_ACHSE": N_ACHSE, "RHO_MIN": RHO_MIN,
                            "S_WURZEL": S_WURZEL, "PHYS_MIN": PHYS_MIN, "PHASE_MAX": PHASE_MAX, "TRIM_REL": TRIM_REL}}
    git = R4.Gitter(4, 4)
    eps0 = git.fehlwinkel(git.s0)
    eT, fehler, _ = git.ableitung_T()
    form = Form(git, eT)
    res["geometrie"] = {"flach_max_abs_eps": float(np.max(np.abs(eps0))), "weg_T_fehlerschaetzung": float(max(fehler)),
                        "laurent_pe": sorted(set(form.pe.tolist())), "laurent_pa": sorted(set(form.pa.tolist()))}
    protokoll(log, f"Geometrie: flach {res['geometrie']['flach_max_abs_eps']:.1e}, Weg T {max(fehler):.1e} "
                   f"({time.time() - t0:.1f} s)")
    rng = np.random.default_rng(20261004)
    res["w0"] = stichproben_w0(git, form, eT, rng, log)
    B = git.B0()
    basis, _ = h_basis(git)
    R = richtungen()
    betraege = BETRAEGE if modus == "haupt" else RAUCH_BETRAEGE
    if modus != "haupt":
        R = [r for r in R if r[0] in ("x+", "xyz+", "fib05")]
    eigen_r = ("x+", "xy+", "x-y", "xyz+", "123", "fib05")
    erg = []
    for nm, nh in R:
        for kb in betraege:
            a, _ = analyse(git, form, B, basis, nm, nh, kb, mit_eigen=nm in eigen_r)
            erg.append(a)
            nst = a["nullstellen"]
            protokoll(log, f"{nm:>7s} |k|={kb}: Windung {a['windung']['windung']:.3f}, Nullstellen {len(nst)}, "
                           f"Geister {len(a['geister'])}, Res {a['achse']['null_residuum_max']:.1e} "
                           f"({a['laufzeit_s']:.1f} s)")
        with open(ziel + ".teil", "w") as f:
            json.dump(dict(res, punkte=erg), f)
    res["punkte"] = erg
    # Gegenprobe Weg K (beschreibend)
    eK = eK_stencil(git)
    formK = Form(git, eK)
    gk = []
    for nm, nh in [r for r in richtungen() if r[0] in ("x+", "xyz+", "123", "fib05")]:
        for kb in ([0.05, 0.8] if modus == "haupt" else [0.3]):
            aK, _ = analyse(git, formK, B, basis, nm, nh, kb)
            gk.append({"richtung": nm, "betrag": kb, "nullstellen": [[x["re"], x["im"]] for x in aK["nullstellen"]],
                       "windung": aK["windung"]["zahl"]})
    res["gegenprobe_weg_K"] = gk
    protokoll(log, f"Gegenprobe Weg K fertig ({time.time() - t0:.1f} s)")
    res["laufzeit_s"] = time.time() - t0
    res["protokoll"] = log
    with open(ziel, "w") as f:
        json.dump(res, f, indent=1)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
