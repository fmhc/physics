#!/usr/bin/env python3
"""INDUZIERT-DICHTE-4D (Runde 38, Code-Agent): induzierte Steifigkeit der konformen Mode eines masselosen
P1-Skalars in 4D, wenn die Punkte nach physikalischem Volumen gestreut und neu vernetzt werden ("Zahl = Volumen"),
gegen die Variante "festes Netz" (nur die Kantenlaengen aendern sich).

Geometrie: Torus [0, L1) x [0, Lq)^3 in Koordinaten, N Punkte, mittlerer Koordinatenabstand h0 = (V/N)^(1/4),
V = L1 Lq^3. Metrik g = e^(2 sigma) delta, sigma = s cos(k.x), k = 2 pi n/L1 laengs Achse 1.

Wiederverwendet (unveraendert): induziert.py aus INDUZIERT-1 (gram_E, lokal_K_batch). P1-Steifigkeit je Simplex
K_T = V P^T G^-1 P, G = Gram-Matrix aus den 10 Kantenlaengenquadraten, V = sqrt(det G)/24.
Gamma = 1/2 log det' K, det' K = N det K_(0) (Knoten 0 geerdet), duenne LU (scipy splu, MMD_AT_PLUS_A,
SymmetricMode, diag_pivot_thresh 0, keine Equilibrierung) wie INDUZIERT-ZUFALL-2D.

Kopplung (gemeinsame Zufallszahlen) wie INDUZIERT-DICHTE-2D, mit Dichte e^(4 sigma):
  phi = k.z, phi' = Phi_s^(-1)(phi), Phi_s(t) = int_0^t e^(4 s cos u) du / I0(4s)
       = t + sum_m 2 I_m(4s)/(m I0(4s)) sin(m t); x = z + khat (phi' - phi)/|k|, Querkoordinaten fest.
  Die Bildpunkte sind exakt unabhaengig mit Koordinatendichte e^(4 sigma(x))/I0(4s) verteilt (N fest).
Netz: Delaunay der Punkte in Koordinaten mit periodischem Saum (Kopien nur bis zur Breite W0 lokale Abstaende),
  behalten werden die Simplizes mit Schwerpunkt im Grundbereich (genau ein Bild je Torus-Simplex); Ecken modulo N,
  Koordinaten der Ecken unverfaltet (Kantenvektoren direkt).
Physikalische Kantenlaengen (geo): Geodaete zweiter Ordnung um den Kantenmittelpunkt m,
  log l = log|d| + sigma(m) + [b + a^2 - (|d|^2 |grad sigma|^2 - a^2)]/24, a = d.grad sigma(m), b = (d.grad)^2 sigma(m).
Messgroesse: D(S) = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/S^2, y = D/V.

Aufruf (nur ueber kleintest.sh):
  python dichte4d.py netztest <aus.json> <N,L1,Lq;N,L1,Lq;...> [S=0.5] [n=1] [ordnungen=MMD_AT_PLUS_A,COLAMD,RCM]
  python dichte4d.py kontrolle <aus.json> <N> <L1> <Lq> <S> <n-Liste> [K1,K2,...]
  python dichte4d.py dichte <N> <L1> <Lq> <saat0> <anzahl> <aus.json> <n-Liste> <S-Liste> [blind=0/1] [fest=0/1]
  python dichte4d.py einbettung <aus.json> <N> <L1> <Lq> <saat> <n-Liste> <s-Liste>
"""
import itertools
import json
import math
import os
import resource
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.spatial import Delaunay, cKDTree
from scipy.special import iv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import induziert as ind  # noqa: E402  (unveraendert aus INDUZIERT-1)

SAAT_BASIS = 20261004
FOURIER_M = 30
H_FEST = 1e-2              # Richardson-Schritt der Kontrolle "festes Netz" (wie INDUZIERT-DICHTE-2D)
W0 = 2.5                   # Saumbreite in lokalen mittleren Koordinatenabstaenden
PAARE = list(itertools.combinations(range(5), 2))
PA = np.array([a for a, _ in PAARE])
PB = np.array([b for _, b in PAARE])
EE = ind.gram_E(4)         # (10, 4, 4): G = sum_e s_e E_e, Reihenfolge combinations(range(5), 2)
PMAT = np.hstack([-np.ones((4, 1)), np.eye(4)])
OFFS = np.array([o for o in itertools.product((-1, 0, 1), repeat=4) if any(o)], dtype=float)
TEILMENGEN = {k: np.array(list(itertools.combinations(range(5), k))) for k in (2, 3, 4)}


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


# ---------------------------------------------------------------------- Grundpunkte, Abbildung psi
def geometrie(N, L1, Lq):
    Lv = np.array([L1, Lq, Lq, Lq], dtype=float)
    V = float(np.prod(Lv))
    return Lv, V, (V / N) ** 0.25


def grundpunkte(N, Lv, saat):
    rng = np.random.default_rng([SAAT_BASIS, 4, int(N), int(saat)])
    return rng.uniform(0.0, 1.0, size=(N, 4)) * Lv[None, :]


def falten(x, Lv):
    y = x - Lv[None, :] * np.floor(x / Lv[None, :])
    y = np.where(y >= Lv[None, :], y - Lv[None, :], y)
    return np.where(y < 0, y + Lv[None, :], y)


def kvektor(n, Lv):
    return np.array([2.0 * np.pi * n / Lv[0], 0.0, 0.0, 0.0])


def phi_vorwaerts(t, s):
    """Phi_s(t) = int_0^t e^(4 s cos u) du / I0(4s) und Ableitung."""
    a = 4.0 * s
    i0 = iv(0, a)
    m = np.arange(1, FOURIER_M + 1)
    coef = 2.0 * iv(m, a) / (i0 * m)
    return t + np.sin(np.outer(t, m)) @ coef, np.exp(a * np.cos(t)) / i0


def psi(z, kvec, s, Lv):
    """Bildpunkte mit Koordinatendichte e^(4 s cos(k.x))/I0(4s); exakte Umkehr der Verteilungsfunktion laengs k."""
    if s == 0.0:
        return z.copy(), {"newton_iter": 0, "residuum": 0.0}
    kb = float(np.linalg.norm(kvec))
    khat = kvec / kb
    phi = np.mod(z @ kvec, 2 * np.pi)
    a = 4.0 * s
    x = phi - 2.0 * (iv(1, a) / iv(0, a)) * np.sin(phi)
    it = 0
    for it in range(1, 100):
        F, dF = phi_vorwaerts(x, s)
        dx = np.clip((F - phi) / dF, -0.5, 0.5)
        x = x - dx
        if np.max(np.abs(dx)) < 1e-14:
            break
    F, _ = phi_vorwaerts(x, s)
    res = float(np.max(np.abs(F - phi)))
    y = z + np.outer((x - phi) / kb, khat)
    return falten(y, Lv), {"newton_iter": it, "residuum": res}


def lokaler_abstand(q, kvec, s, h0):
    """Lokaler mittlerer Koordinatenabstand der Bildpunkte (Koordinatendichte e^(4 sigma)/I0(4s) mal N/V)."""
    if s == 0.0:
        return np.full(q.shape[0], h0)
    return h0 * np.exp(-s * np.cos(q @ kvec)) * float(iv(0, 4.0 * s)) ** 0.25


# ---------------------------------------------------------------------- periodisches 4D-Delaunay mit Saum
def schluessel(ts, idx, N):
    sub = ts[:, idx]
    key = np.zeros(sub.shape[:2], dtype=np.int64)
    for j in range(sub.shape[2]):
        key = key * N + sub[:, :, j]
    return key.ravel()


class Netz4:
    """Simplizialnetz auf dem 4-Torus: tri (F, 5) Knoten modulo N, X (F, 5, 4) unverfaltete Eckkoordinaten,
    pos die gefalteten Punkte (fuer die Periodenversaetze der Ecken)."""

    def __init__(self, tri, X, Lv, N, art, pos):
        self.tri = np.ascontiguousarray(tri, dtype=np.int64)
        self.X = X
        self.Lv = Lv
        self.N = int(N)
        self.F = int(tri.shape[0])
        self.art = art
        self.pos = pos
        self.saum = {}
        self.ts = np.sort(self.tri, axis=1)
        self._kanten = None

    def kanten_schluessel(self):
        if self._kanten is None:
            self._kanten = np.unique(schluessel(self.ts, TEILMENGEN[2], self.N))
        return self._kanten

    def simplex_schluessel(self):
        return np.unique(schluessel(self.ts, np.arange(5)[None, :], self.N))

    def teilflaechen(self, k):
        """Eindeutige k-Teilsimplizes mit Periodenversatz: (Knotenschluessel, Versatzschluessel) je Zeile."""
        order = np.argsort(self.tri, axis=1, kind="stable")
        ts = np.take_along_axis(self.tri, order, axis=1)
        o = np.rint((self.X - self.pos[self.tri]) / self.Lv[None, None, :]).astype(np.int64)
        os_ = np.take_along_axis(o, order[:, :, None], axis=1)
        idx = TEILMENGEN[k]
        kk = schluessel(ts, idx, self.N)
        rel = os_[:, idx[:, 1:], :] - os_[:, idx[:, :1], :] + 1          # Werte 0..2 (Nachbarkopien)
        code = np.zeros(rel.shape[:2], dtype=np.int64)
        for j in range(rel.shape[2]):
            for mu in range(4):
                code = code * 3 + rel[:, :, j, mu]
        return np.stack([kk, code.ravel()], axis=1), bool(np.all((rel >= 0) & (rel <= 2)))

    def pruefen(self):
        N, F, X = self.N, self.F, self.X
        vol = np.linalg.det(X[:, 1:, :] - X[:, :1, :]) / 24.0
        out = {"V": N, "S4": F, "verschieden": bool(np.all(np.diff(self.ts, axis=1) > 0)),
               "alle_knoten": bool(np.unique(self.tri).size == N), "orient_min": float(np.min(vol)),
               "koord_vol_rel_abw": float(abs(math.fsum(vol.tolist()) / float(np.prod(self.Lv)) - 1.0))}
        anz = {}
        versatz_ok = True
        for k in (2, 3, 4):
            zeilen, ok = self.teilflaechen(k)
            versatz_ok = versatz_ok and ok
            if k < 4 and float(N) ** k * 81.0 ** (k - 1) < 9.0e18:
                u, c = np.unique(zeilen[:, 0] * (81 ** (k - 1)) + zeilen[:, 1], return_counts=True)
                u = u[:, None]
            else:
                u, c = np.unique(zeilen, axis=0, return_counts=True)
            anz[k] = (u, c)
        out["E"], out["F2"], out["T3"] = int(anz[2][0].shape[0]), int(anz[3][0].shape[0]), int(anz[4][0].shape[0])
        out["euler"] = int(N - out["E"] + out["F2"] - out["T3"] + F)
        out["facetten_genau_zwei"] = bool(np.all(anz[4][1] == 2))
        out["versatz_ok"] = versatz_ok
        out["simplizes_je_knoten"] = F / N
        out["grad_mittel"] = 2.0 * out["E"] / N
        d = X[:, PB, :] - X[:, PA, :]
        out["kante_max_rel_L"] = float(np.max(np.abs(d) / self.Lv[None, None, :]))
        dl = np.sqrt(np.einsum("fei,fei->fe", d, d))
        out["l_min"], out["l_max"], out["l_mittel"] = float(dl.min()), float(dl.max()), float(dl.mean())
        out.update(self.saum)
        return out


def gueltig(p):
    return bool(p["verschieden"] and p["alle_knoten"] and p["orient_min"] > 0 and p["koord_vol_rel_abw"] <= 1e-9
                and p["facetten_genau_zwei"] and p["euler"] == 0 and p.get("versatz_ok", False)
                and p["saum_marge_min"] > 0)


def periodisches_netz(pos, Lv, kvec, s, h0, art, w0=W0, mit_punkten=False):
    """Delaunay der Punkte plus Saum aus den 80 Nachbarkopien (nur Kopien innerhalb w0 lokaler Abstaende vom
    Grundbereich); behalten werden die Simplizes mit Schwerpunkt im Grundbereich."""
    N = pos.shape[0]
    tp, ti = [pos], [np.arange(N)]
    for o in OFFS:
        q = pos + o[None, :] * Lv[None, :]
        w = w0 * lokaler_abstand(q, kvec, s, h0)
        m = np.all((q > -w[:, None]) & (q < Lv[None, :] + w[:, None]), axis=1)
        if np.any(m):
            tp.append(q[m])
            ti.append(np.nonzero(m)[0])
    P = np.concatenate(tp)
    I = np.concatenate(ti)
    t0 = time.time()
    S = Delaunay(P).simplices
    t_qh = time.time() - t0
    cen = np.zeros((S.shape[0], 4))
    for j in range(5):
        cen += P[S[:, j]]
    cen /= 5.0
    halte = np.all((cen >= 0) & (cen < Lv[None, :]), axis=1)
    del cen
    S = S[halte].astype(np.int64)
    X = P[S]
    det = np.linalg.det(X[:, 1:, :] - X[:, :1, :])
    flip = det < 0
    S[flip] = S[flip][:, [1, 0, 2, 3, 4]]
    X = P[S]
    nz = Netz4(I[S], X, Lv, N, art, pos)
    # Saumpruefung: Umkugel jedes behaltenen Simplex liegt im Saum (sonst koennte ein fehlender Punkt darin liegen)
    E = X[:, 1:, :] - X[:, :1, :]
    rhs = 0.5 * np.einsum("fij,fij->fi", E, E)
    cc = np.linalg.solve(E, rhs[..., None])[..., 0]
    R = np.linalg.norm(cc, axis=1)
    c = X[:, 0, :] + cc
    kb = float(np.linalg.norm(kvec))
    wl = w0 * lokaler_abstand(c, kvec, s, h0) * np.exp(-abs(s) * kb * R)
    marge = np.minimum(c - R[:, None] + wl[:, None], Lv[None, :] + wl[:, None] - c - R[:, None]).min(axis=1)
    nz.saum = {"punkte_qhull": int(P.shape[0]), "faktor_qhull": P.shape[0] / N, "sek_qhull": t_qh,
               "saum_marge_min": float(marge.min()), "umkugel_R_max": float(R.max()),
               "umkugel_R_mittel": float(R.mean()), "rss_mb": rss_mb()}
    if mit_punkten:
        nz.P, nz.c, nz.R, nz.S = P, c, R, S
    return nz


# ---------------------------------------------------------------------- Laengen, P1, log det'
def laengen_geo(X, kvec, s):
    """Geodaete zweiter Ordnung um den Kantenmittelpunkt; (F, 10) je Simplex."""
    d = X[:, PB, :] - X[:, PA, :]
    d2 = np.einsum("fei,fei->fe", d, d)
    if s == 0.0:
        return np.sqrt(d2)
    m = X[:, PA, :] + 0.5 * d
    ph = m @ kvec
    kd = d @ kvec
    k2 = float(kvec @ kvec)
    c, sn = np.cos(ph), np.sin(ph)
    korr = (-s * kd * kd * c + s * s * sn * sn * (2.0 * kd * kd - d2 * k2)) / 24.0
    return np.sqrt(d2) * np.exp(s * c + korr)


def laengen_schwerpunkt(X, kvec, s):
    """Schwerpunktregel: alle Kanten eines Simplex mit e^(sigma(Schwerpunkt)) skaliert, also K_T = e^(2 sigma(c_T))
    mal Koordinaten-Steifigkeit (Simplex aehnlich zum Koordinatensimplex, immer einbettbar)."""
    d = X[:, PB, :] - X[:, PA, :]
    l0 = np.sqrt(np.einsum("fei,fei->fe", d, d))
    if s == 0.0:
        return l0
    c = X.mean(axis=1)
    return l0 * np.exp(s * np.cos(c @ kvec))[:, None]


def laengen_regel(X, kvec, s, regel):
    """Rueckgabe (l, ersetzt). regel: 'sp' (Schwerpunkt), 'geo+' (Geodaete; nicht einbettbare Simplizes durch die
    Schwerpunktregel ersetzt), 'geo' (rein, kann nicht einbettbar sein)."""
    if regel == "sp":
        return laengen_schwerpunkt(X, kvec, s), 0
    l = laengen_geo(X, kvec, s)
    if regel == "geo" or s == 0.0:
        return l, 0
    G = np.einsum("fe,eab->fab", l * l, EE)
    schlecht = ~(np.linalg.eigvalsh(G)[:, 0] > 0)
    if np.any(schlecht):
        l = l.copy()
        l[schlecht] = laengen_schwerpunkt(X[schlecht], kvec, s)
    return l, int(np.sum(schlecht))


REGELN = ("sp", "geo+")


def laengen_mitte(X, kvec, s):
    d = X[:, PB, :] - X[:, PA, :]
    m = X[:, PA, :] + 0.5 * d
    return np.sqrt(np.einsum("fei,fei->fe", d, d)) * np.exp(s * np.cos(m @ kvec))


def p1_lokal(sq):
    """Lokale P1-Steifigkeit V P^T G^-1 P (wie induziert.lokal_K_batch, m2 = 0) plus Gram-Eigenwert-Minimum."""
    G = np.einsum("fe,eab->fab", sq, EE)
    lam = np.linalg.eigvalsh(G)[:, 0]
    Ginv = np.linalg.inv(G)
    V = np.sqrt(np.maximum(np.linalg.det(G), 0.0)) / 24.0
    Gam = np.matmul(PMAT.T[None, :, :], np.matmul(Ginv, PMAT[None, :, :]))
    Kl = V[:, None, None] * Gam
    return 0.5 * (Kl + np.swapaxes(Kl, 1, 2)), V, lam


def matrix_voll(nz, Kl):
    r = np.repeat(nz.tri, 5, axis=1).ravel()
    c = np.tile(nz.tri, (1, 5)).ravel()
    K = sp.coo_matrix((Kl.ravel(), (r, c)), shape=(nz.N, nz.N)).tocsc()
    K.sum_duplicates()
    return K


def gamma(nz, l, ordnung="MMD_AT_PLUS_A"):
    """1/2 log det' K aus den Kantenlaengen l (F, 10); NaN, wenn ein Simplex nicht einbettbar ist."""
    t0 = time.time()
    Kl, Vphys, lam = p1_lokal(l * l)
    info = {"lam_min": float(lam.min()), "nicht_einbettbar": int(np.sum(~(lam > 0))),
            "vol_phys": math.fsum(Vphys.tolist())}
    if info["nicht_einbettbar"] > 0:
        info["sek"] = time.time() - t0
        return float("nan"), info
    K = matrix_voll(nz, Kl)
    zs = np.abs(np.asarray(K.sum(axis=1))).max()
    info["zeilensumme_rel"] = float(zs / np.abs(K.data).max())
    K0 = K[1:, 1:].tocsc()
    K0.sort_indices()
    t1 = time.time()
    if ordnung == "RCM":
        from scipy.sparse.csgraph import reverse_cuthill_mckee
        p = reverse_cuthill_mckee(K0, symmetric_mode=True)
        K0 = K0[p][:, p].tocsc()
        K0.sort_indices()
        ordnung_lu = "NATURAL"
    else:
        ordnung_lu = ordnung
    lu = spla.splu(K0, permc_spec=ordnung_lu, diag_pivot_thresh=0.0,
                   options={"SymmetricMode": True, "Equil": False})
    d = lu.U.diagonal()
    info.update({"sek_lu": time.time() - t1, "nnz_K0": int(K0.nnz), "nnz_LU": int(lu.L.nnz + lu.U.nnz),
                 "min_U": float(np.min(d)), "neg_U": int(np.sum(d < 0)),
                 "perm_gleich": bool(np.array_equal(lu.perm_r, lu.perm_c))})
    g = 0.5 * (math.fsum(np.log(np.abs(d)).tolist()) + math.log(nz.N))
    info["sek"] = time.time() - t0
    info["rss_mb"] = rss_mb()
    return g, info


def lu_ok(info):
    return bool(info.get("nicht_einbettbar", 1) == 0 and info.get("neg_U", 1) == 0 and info.get("perm_gleich", False)
                and info.get("min_U", -1.0) > 0)


# ---------------------------------------------------------------------- eine Auswertung bei (k, s)
def gamma_regeln(nz, kvec, s, regeln=REGELN):
    """Gamma je Laengenregel auf demselben Netz; dazu LU-Information und Zahl der ersetzten Simplizes."""
    g, lus, ers = {}, {}, {}
    for r in regeln:
        l, n_ers = laengen_regel(nz.X, kvec, s, r)
        g[r], lus[r] = gamma(nz, l)
        ers[r] = n_ers
    return g, lus, ers


def bildnetz(z, Lv, h0, kvec, s, kanten0, simpl0):
    t0 = time.time()
    x, pinfo = psi(z, kvec, s, Lv)
    nz = periodisches_netz(x, Lv, kvec, s, h0, "bild")
    pr = nz.pruefen()
    g, lus, ers = gamma_regeln(nz, kvec, s)
    ke = nz.kanten_schluessel()
    se = nz.simplex_schluessel()
    out = {"s": s, "psi": pinfo, "pruefung": pr, "lu": lus, "gamma": g, "ersetzt": ers,
           "neue_kanten_anteil": float(np.mean(~np.isin(ke, kanten0, assume_unique=True))),
           "neue_simplizes_anteil": float(np.mean(~np.isin(se, simpl0, assume_unique=True))),
           "sek": time.time() - t0}
    return out


# ---------------------------------------------------------------------- Modi
def speichern(ziel, out):
    with open(ziel + ".tmp", "w") as f:
        json.dump(out, f)
    os.replace(ziel + ".tmp", ziel)


def modus_netztest(konf, S, n, ordnungen, protokoll, out, ziel):
    """Laufzeit, Speicher und Netzpruefung (keine Messgroesse): Grundnetz und je ein Bildnetz bei +S und -S."""
    out["netztest"] = []
    for N, L1, Lq in konf:
        Lv, V, h0 = geometrie(N, L1, Lq)
        z = grundpunkte(N, Lv, 900)
        t0 = time.time()
        n0 = periodisches_netz(z, Lv, kvektor(n, Lv), 0.0, h0, "basis")
        t_netz = time.time() - t0
        p0 = n0.pruefen()
        e = {"N": N, "Lv": Lv.tolist(), "h0": h0, "sek_netz": t_netz, "pruefung": p0, "gueltig": gueltig(p0),
             "lu": {}}
        protokoll(f"N={N} Lv={Lv.tolist()}: Netz {t_netz:.1f} s (Qhull {p0['sek_qhull']:.1f} s, "
                  f"{p0['punkte_qhull']} Punkte), S4/N {p0['simplizes_je_knoten']:.2f}, Grad {p0['grad_mittel']:.1f}, "
                  f"Euler {p0['euler']}, Facetten {p0['facetten_genau_zwei']}, Marge {p0['saum_marge_min']:.2f}, "
                  f"gueltig {gueltig(p0)}, RSS {rss_mb():.0f} MB")
        l0 = laengen_geo(n0.X, np.zeros(4), 0.0)
        for o in ordnungen:
            g, info = gamma(n0, l0, o)
            e["lu"][o] = info
            protokoll(f"  LU {o}: {info['sek_lu']:.1f} s, nnz(K0) {info['nnz_K0']}, nnz(LU) {info['nnz_LU']}, "
                      f"lu_ok {lu_ok(info)}, RSS {rss_mb():.0f} MB")
        e["bild"] = []
        k0 = n0.kanten_schluessel()
        s0 = n0.simplex_schluessel()
        for s in (S, -S):
            b = bildnetz(z, Lv, h0, kvektor(n, Lv), s, k0, s0)
            b.pop("gamma")
            e["bild"].append(b)
            pb = b["pruefung"]
            protokoll(f"  Bild s={s:+.2f} n={n}: {b['sek']:.1f} s (Qhull {pb['sek_qhull']:.1f} s, "
                      f"{pb['punkte_qhull']} Punkte), gueltig {gueltig(pb)}, Marge {pb['saum_marge_min']:.2f}, "
                      f"ersetzt {b['ersetzt']}, lu_ok {[lu_ok(v) for v in b['lu'].values()]}, LU "
                      f"{[round(v.get('sek_lu', -1), 1) for v in b['lu'].values()]} s, RSS {rss_mb():.0f} MB")
        out["netztest"].append(e)
        speichern(ziel, out)


def modus_dichte(N, L1, Lq, saat0, anzahl, ziel, nlist, Slist, blind, mit_fest, protokoll, out):
    """Je Saat: Grundnetz (Gamma0), je k und S die Bildnetze bei +S und -S (Dichte-Variante) und, falls mit_fest,
    dasselbe Grundnetz mit den Laengen bei +S und -S (Variante festes Netz). Beide Laengenregeln je Netz."""
    Lv, V, h0 = geometrie(N, L1, Lq)
    out.update({"N": N, "Lv": Lv.tolist(), "V": V, "h0": h0, "rho": N / V, "nlist": nlist, "S": Slist,
                "regeln": list(REGELN), "blind": blind, "mit_fest": mit_fest, "saaten": []})
    blindwerte = {}
    for saat in range(saat0, saat0 + anzahl):
        t0 = time.time()
        z = grundpunkte(N, Lv, saat)
        n0 = periodisches_netz(z, Lv, kvektor(1, Lv), 0.0, h0, "basis")
        p0 = n0.pruefen()
        g0, lu0 = gamma(n0, laengen_geo(n0.X, np.zeros(4), 0.0))
        k0 = n0.kanten_schluessel()
        s0 = n0.simplex_schluessel()
        pts = []
        for n in nlist:
            kvec = kvektor(n, Lv)
            kb = float(np.linalg.norm(kvec))
            pt = {"n": n, "betrag": kb, "betrag_mal_h0": kb * h0, "je_S": []}
            for S in Slist:
                plus = bildnetz(z, Lv, h0, kvec, S, k0, s0)
                minus = bildnetz(z, Lv, h0, kvec, -S, k0, s0)
                e = {"S": S, "plus": plus, "minus": minus, "y": {}}
                for r in REGELN:
                    e["y"][r] = (plus["gamma"][r] + minus["gamma"][r] - 2.0 * g0) / (S * S * V)
                if mit_fest:
                    gfp, lfp, efp = gamma_regeln(n0, kvec, S)
                    gfm, lfm, efm = gamma_regeln(n0, kvec, -S)
                    e["fest"] = {"lu_plus": lfp, "lu_minus": lfm, "ersetzt_plus": efp, "ersetzt_minus": efm,
                                 "y": {r: (gfp[r] + gfm[r] - 2.0 * g0) / (S * S * V) for r in REGELN}}
                if blind:
                    for r in REGELN:
                        blindwerte.setdefault((n, S, "dichte", r), []).append(e["y"][r])
                        if mit_fest:
                            blindwerte.setdefault((n, S, "fest", r), []).append(e["fest"]["y"][r])
                    for x in (plus, minus):
                        x.pop("gamma")
                    e.pop("y")
                    if mit_fest:
                        e["fest"].pop("y")
                pt["je_S"].append(e)
                protokoll(f"N={N} saat={saat} n={n} |k|h0={kb * h0:.3f} S={S}: "
                          + ("" if blind else f"y {e['y']}" + (f" fest {e['fest']['y']}; " if mit_fest else "; "))
                          + f"gueltig {gueltig(plus['pruefung'])}/{gueltig(minus['pruefung'])}, "
                          f"lu {[lu_ok(v) for v in plus['lu'].values()]}/{[lu_ok(v) for v in minus['lu'].values()]}, "
                          f"ersetzt {plus['ersetzt']['geo+']}/{minus['ersetzt']['geo+']}, neue Simplizes "
                          f"{plus['neue_simplizes_anteil']:.3f}/{minus['neue_simplizes_anteil']:.3f}, "
                          f"{plus['sek']:.1f}+{minus['sek']:.1f} s")
            pts.append(pt)
        rec = {"saat": saat, "pruefung0": p0, "lu0": lu0, "punkte": pts, "sekunden": time.time() - t0,
               "rss_mb": rss_mb()}
        if not blind:
            rec["gamma0"] = g0
        out["saaten"].append(rec)
        if blind:
            out["blind_streuung"] = {f"n{k[0]}/S{k[1]}/{k[2]}/{k[3]}": {
                "std_y": float(np.std(v, ddof=1)) if len(v) > 1 else None, "anzahl": len(v)}
                for k, v in blindwerte.items()}
        speichern(ziel, out)
        protokoll(f"N={N} saat={saat} fertig in {time.time() - t0:.1f} s, RSS {rss_mb():.0f} MB")
    return out


def ind_zweite(f, h, f0):
    """Symmetrische zweite Differenzen mit h und 2h, Richardson (wie zufall2d.zweite)."""
    fp1, fm1, fp2, fm2 = f(h), f(-h), f(2 * h), f(-2 * h)
    D1 = (fp1 - 2 * f0 + fm1) / (h * h)
    D2 = (fp2 - 2 * f0 + fm2) / (4 * h * h)
    return (4 * D1 - D2) / 3.0, D1, D2, (8 * (fp1 - fm1) - (fp2 - fm2)) / (12 * h)


def geodaete_numerisch(x0, d, kvec, s, ordnung=64):
    """Laenge der kuerzesten Kurve der Familie x0 + t d + nv (c1 t(1-t) + c2 t(1-t)(2t-1)) in der Metrik
    e^(2 sigma); nv in der Ebene aus d und k (dort liegt die Geodaete aus Symmetriegruenden); Gauss-Legendre."""
    from scipy.optimize import minimize
    tg, wg = np.polynomial.legendre.leggauss(ordnung)
    t = 0.5 * (tg + 1)
    w = 0.5 * wg
    l = np.linalg.norm(d)
    kq = kvec - (kvec @ d) / (l * l) * d
    nv = kq / np.linalg.norm(kq)

    def laenge(c):
        b1, b2 = t * (1 - t), t * (1 - t) * (2 * t - 1)
        db1, db2 = 1 - 2 * t, (1 - t) * (2 * t - 1) - t * (2 * t - 1) + 2 * t * (1 - t)
        g = x0[None, :] + t[:, None] * d[None, :] + (c[0] * b1 + c[1] * b2)[:, None] * nv[None, :]
        dg = d[None, :] + (c[0] * db1 + c[1] * db2)[:, None] * nv[None, :]
        return float(np.sum(w * np.exp(s * np.cos(g @ kvec)) * np.linalg.norm(dg, axis=1)))

    r = minimize(laenge, np.zeros(2), method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-15,
                                                                         "maxiter": 4000})
    return r.fun, laenge(np.zeros(2))


def modus_kontrolle(N, L1, Lq, S, nlist, teile, protokoll, out, ziel):
    Lv, V, h0 = geometrie(N, L1, Lq)
    out.update({"N": N, "Lv": Lv.tolist(), "h0": h0, "S": S, "nlist": nlist, "teile": sorted(teile)})
    z = grundpunkte(N, Lv, 990)
    if "K1" in teile:
        # (K1) Abbildung psi
        k1 = []
        for n in sorted(set(nlist)):
            kvec = kvektor(n, Lv)
            for s in (S, -S, 0.5 * S, -0.5 * S):
                x, info = psi(z, kvec, s, Lv)
                ph = np.mod(x @ kvec, 2 * np.pi)
                F, _ = phi_vorwaerts(np.sort(ph), s)
                emp = (np.arange(1, N + 1) - 0.5) / N
                ks = float(np.max(np.abs(F / (2 * np.pi) - emp)))
                a = 4.0 * s
                e4 = np.exp(-a * np.cos(ph))
                cs = np.cos(ph)
                dq = (x - z)[:, 1:]
                dq = dq - Lv[None, 1:] * np.round(dq / Lv[None, 1:])
                k1.append({"n": n, "s": s, "newton": info, "ks_mal_wurzelN": ks * math.sqrt(N),
                           "z_e^-4sigma": float((e4.mean() - 1 / iv(0, a)) / (e4.std() / math.sqrt(N))),
                           "z_cos": float((cs.mean() - iv(1, a) / iv(0, a)) / (cs.std() / math.sqrt(N))),
                           "querkoordinaten_unveraendert": float(np.max(np.abs(dq)))})
                protokoll(f"K1 n={n} s={s:+.3f}: Newton {info}, KS*sqrt(N) {ks * math.sqrt(N):.3f}, "
                          f"z {k1[-1]['z_e^-4sigma']:+.2f} / {k1[-1]['z_cos']:+.2f}, "
                          f"quer {k1[-1]['querkoordinaten_unveraendert']:.1e}")
        out["K1_psi"] = k1
        speichern(ziel, out)
    if "K2" in teile:
        # (K2) Saum: w0 = 2,5 gegen 4,0 (gleiche Simplexmenge) und leere Umkugeln (kd-Baum ueber die Saumpunkte)
        k2 = []
        n = max(nlist)
        kvec = kvektor(n, Lv)
        for s in (0.0, S, -S):
            x, _ = psi(z, kvec, s, Lv)
            a = periodisches_netz(x, Lv, kvec, s, h0, "a", W0, mit_punkten=True)
            b = periodisches_netz(x, Lv, kvec, s, h0, "b", 4.0)
            gleich = bool(np.array_equal(a.simplex_schluessel(), b.simplex_schluessel()))
            baum = cKDTree(a.P)
            innen = baum.query_ball_point(a.c, r=a.R * (1 - 1e-9), return_length=True)
            k2.append({"s": s, "n": n, "gleich_w4": gleich, "F": a.F, "F_w4": b.F,
                       "umkugeln_mit_punkt_innen": int(np.sum(innen > 0)), "pruefung": a.pruefen(),
                       "pruefung_w4": b.pruefen()})
            protokoll(f"K2 s={s:+.2f}: Saum 2,5 = Saum 4,0 {gleich}, Umkugeln mit Punkt innen "
                      f"{int(np.sum(innen > 0))}, gueltig {gueltig(k2[-1]['pruefung'])}/{gueltig(k2[-1]['pruefung_w4'])}")
            del a, b, baum
        out["K2_saum"] = k2
        speichern(ziel, out)
    if "K3" in teile:
        # (K3) Laengenformel gegen numerische Geodaete (abs(s) k l bis etwa 0,5 wie in 2D)
        rng = np.random.default_rng(SAAT_BASIS + 3)
        k3 = []
        for _ in range(60):
            kb = rng.uniform(0.1, 0.6)
            kvec = kb * np.array([1.0, 0.0, 0.0, 0.0])
            s = 0.25 * rng.choice([-1, 1])
            x0 = rng.uniform(0, 10, 4)
            l = rng.uniform(0.3, 3.5)
            d = rng.standard_normal(4)
            d = l * d / np.linalg.norm(d)
            X = np.stack([x0, x0 + d] + [x0] * 3)[None, :, :]
            lg = float(laengen_geo(X, kvec, s)[0, 0])
            lm = float(laengen_mitte(X, kvec, s)[0, 0])
            lnum, lline = geodaete_numerisch(x0, d, kvec, s)
            k3.append({"k": kb, "s": s, "l": l, "kl_s": abs(s) * kb * l, "rel_geo": lg / lnum - 1,
                       "rel_mitte": lm / lnum - 1, "rel_linie": lline / lnum - 1})
        arr = {key: np.array([x[key] for x in k3]) for key in ("kl_s", "rel_geo", "rel_mitte")}
        out["K3_geodaete"] = {"einzeln": k3, "max_abs_rel_geo": float(np.max(np.abs(arr["rel_geo"]))),
                              "max_abs_rel_mitte": float(np.max(np.abs(arr["rel_mitte"]))),
                              "max_kl_s": float(np.max(arr["kl_s"]))}
        protokoll(f"K3 Geodaete (max |s| k l = {np.max(arr['kl_s']):.3f}): geo {np.max(np.abs(arr['rel_geo'])):.2e}, "
                  f"mitte {np.max(np.abs(arr['rel_mitte'])):.2e}")
        speichern(ziel, out)
    if "K4" in teile:
        # (K4) log det' per LU gegen dicht (kleines Netz, beide Regeln) und P1 gegen induziert.lokal_K_batch
        k4 = []
        Nk, Lk = 1500, (1500.0) ** 0.25
        Lvk, Vk, h0k = geometrie(Nk, Lk, Lk)
        zk = grundpunkte(Nk, Lvk, 991)
        kveck = kvektor(1, Lvk)
        for s in (0.0, S, -S):
            x, _ = psi(zk, kveck, s, Lvk)
            nz = periodisches_netz(x, Lvk, kveck, s, h0k, "k4")
            pr = nz.pruefen()
            for r in REGELN:
                l, ers = laengen_regel(nz.X, kveck, s, r)
                g, info = gamma(nz, l)
                Kl, _, lam = p1_lokal(l * l)
                Kref = ind.lokal_K_batch(4, 0.0, l * l)
                K = matrix_voll(nz, Kl).toarray()
                sgn, ld = np.linalg.slogdet(K + 1.0 / Nk)
                ev = np.linalg.eigvalsh(K)
                k4.append({"s": s, "regel": r, "ersetzt": ers, "N": Nk, "gueltig": gueltig(pr), "gamma_lu": g,
                           "abw_slogdet": abs(g - 0.5 * ld),
                           "abw_eigen": abs(g - 0.5 * math.fsum(np.log(ev[1:]).tolist())), "vorzeichen": float(sgn),
                           "eigen_min_abs": float(abs(ev[0])), "eigen_2": float(ev[1]),
                           "p1_gegen_induziert_max_rel": float(np.max(np.abs(Kl - Kref)) / np.max(np.abs(Kref))),
                           "lu": info})
                protokoll(f"K4 N={Nk} s={s:+.2f} {r}: LU gegen slogdet {k4[-1]['abw_slogdet']:.2e}, Eigenwerte "
                          f"{k4[-1]['abw_eigen']:.2e}, P1 gegen INDUZIERT-1 {k4[-1]['p1_gegen_induziert_max_rel']:.1e}, "
                          f"ersetzt {ers}, gueltig {gueltig(pr)}")
        out["K4_logdet"] = k4
        speichern(ziel, out)
    if "K5" in teile:
        # (K5) Kippen gegen s (ohne LU): neue Kanten und Simplizes gegenueber s = 0, Einbettbarkeit (geodaetisch)
        k5 = []
        n0 = periodisches_netz(z, Lv, kvektor(1, Lv), 0.0, h0, "basis")
        n0.pruefen()
        ke0, se0 = n0.kanten_schluessel(), n0.simplex_schluessel()
        for n in sorted(set(nlist)):
            kvec = kvektor(n, Lv)
            for s in (1e-4, 1e-3, 1e-2, 0.1, 0.5 * S, S):
                x, _ = psi(z, kvec, s, Lv)
                nz = periodisches_netz(x, Lv, kvec, s, h0, "k5")
                pr = nz.pruefen()
                _, _, lam = p1_lokal(laengen_geo(nz.X, kvec, s) ** 2)
                _, _, lamf = p1_lokal(laengen_geo(n0.X, kvec, s) ** 2)
                k5.append({"n": n, "s": s, "E": pr["E"], "F": nz.F,
                           "neue_kanten": int(np.sum(~np.isin(nz.kanten_schluessel(), ke0, assume_unique=True))),
                           "neue_simplizes": int(np.sum(~np.isin(nz.simplex_schluessel(), se0, assume_unique=True))),
                           "lam_min_bild": float(lam.min()), "nicht_einbettbar_bild": int(np.sum(~(lam > 0))),
                           "lam_min_fest": float(lamf.min()), "nicht_einbettbar_fest": int(np.sum(~(lamf > 0))),
                           "gueltig": gueltig(pr)})
                protokoll(f"K5 n={n} s={s}: neue Kanten {k5[-1]['neue_kanten']} von {pr['E']}, neue Simplizes "
                          f"{k5[-1]['neue_simplizes']} von {nz.F}, nicht einbettbar Bild/fest "
                          f"{k5[-1]['nicht_einbettbar_bild']}/{k5[-1]['nicht_einbettbar_fest']}")
            speichern(ziel, out | {"K5_kippen": k5})
        out["K5_kippen"] = k5
        speichern(ziel, out)
    if "K6" in teile:
        # (K6, beschreibend) Gamma(s) (Regel sp) eines Bildnetzes und des festen Netzes auf feinem s-Gitter
        k6 = []
        Nk6, Lk6 = 1500, (1500.0) ** 0.25
        Lv6, V6, h06 = geometrie(Nk6, Lk6, Lk6)
        z6 = grundpunkte(Nk6, Lv6, 992)
        kv6 = kvektor(1, Lv6)
        n06 = periodisches_netz(z6, Lv6, kv6, 0.0, h06, "k6")
        n06.pruefen()
        se06 = n06.simplex_schluessel()
        for s in np.linspace(0.0, 0.02, 11):
            x, _ = psi(z6, kv6, float(s), Lv6)
            nz = periodisches_netz(x, Lv6, kv6, float(s), h06, "k6")
            nz.pruefen()
            g, info = gamma(nz, laengen_schwerpunkt(nz.X, kv6, float(s)))
            gf, _ = gamma(n06, laengen_schwerpunkt(n06.X, kv6, float(s)))
            k6.append({"s": float(s), "gamma_bild": g, "gamma_fest": gf,
                       "neue_simplizes": int(np.sum(~np.isin(nz.simplex_schluessel(), se06, assume_unique=True)))})
        out["K6_sprung"] = {"N": Nk6, "werte": k6}
        protokoll("K6 Gamma(s) Bild minus fest (sp): " + ", ".join(
            f"{x['s']:.3f}:{x['gamma_bild'] - x['gamma_fest']:+.4f}({x['neue_simplizes']})" for x in k6))
    return out




def modus_einbettung(N, L1, Lq, saat, nlist, slist, protokoll, out, ziel):
    """Rauch (keine Messgroesse): Splitter im Grundnetz und nicht einbettbare Simplizes gegen s, festes Netz und
    Bildnetz."""
    Lv, V, h0 = geometrie(N, L1, Lq)
    z = grundpunkte(N, Lv, 900 + saat)
    n0 = periodisches_netz(z, Lv, kvektor(1, Lv), 0.0, h0, "basis")
    p0 = n0.pruefen()
    l0 = laengen_geo(n0.X, np.zeros(4), 0.0)
    _, V0, lam0 = p1_lokal(l0 * l0)
    lm = l0.mean(axis=1)
    eps = V0 / (lm ** 4 * math.sqrt(5.0) / 96.0)      # Volumen relativ zum regulaeren Simplex gleicher Kantenlaenge
    out.update({"N": N, "Lv": Lv.tolist(), "h0": h0, "pruefung0": p0, "splitter": {
        f"eps<{t}": int(np.sum(eps < t)) for t in (1e-4, 1e-3, 1e-2, 3e-2, 0.1, 0.3)} | {"F": n0.F,
                                                                                         "eps_min": float(eps.min())},
                "werte": []})
    protokoll(f"Grundnetz N={N} Lv={Lv.tolist()}: F={n0.F}, Splitter {out['splitter']}")
    k0, s0 = n0.kanten_schluessel(), n0.simplex_schluessel()
    for n in nlist:
        kvec = kvektor(n, Lv)
        for s in slist:
            for vz in (1, -1):
                lf = laengen_geo(n0.X, kvec, vz * s)
                _, _, lamf = p1_lokal(lf * lf)
                x, _ = psi(z, kvec, vz * s, Lv)
                nb = periodisches_netz(x, Lv, kvec, vz * s, h0, "bild")
                pb = nb.pruefen()
                lb = laengen_geo(nb.X, kvec, vz * s)
                _, _, lamb = p1_lokal(lb * lb)
                e = {"n": n, "kh0": float(np.linalg.norm(kvec)) * h0, "s": vz * s,
                     "fest_nicht_einbettbar": int(np.sum(~(lamf > 0))), "bild_nicht_einbettbar": int(np.sum(~(lamb > 0))),
                     "bild_gueltig": gueltig(pb), "bild_marge": pb["saum_marge_min"],
                     "bild_kante_max_rel_L": pb["kante_max_rel_L"], "F_bild": nb.F,
                     "neue_simplizes": float(np.mean(~np.isin(nb.simplex_schluessel(), s0, assume_unique=True)))}
                out["werte"].append(e)
                protokoll(f"n={n} kh0={e['kh0']:.3f} s={vz * s:+.4f}: nicht einbettbar fest {e['fest_nicht_einbettbar']}, "
                          f"Bild {e['bild_nicht_einbettbar']} von {nb.F}; Bild gueltig {e['bild_gueltig']} (Marge "
                          f"{e['bild_marge']:.2f}, Kante/L {e['bild_kante_max_rel_L']:.2f}); neue Simplizes "
                          f"{e['neue_simplizes']:.3f}")
            speichern(ziel, out)
    return out


def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    import scipy
    out = {"modus": modus, "argv": sys.argv[1:], "numpy": np.__version__, "scipy": scipy.__version__}
    if modus == "netztest":
        ziel = sys.argv[2]
        konf = [tuple(float(v) if i else int(v) for i, v in enumerate(c.split(","))) for c in sys.argv[3].split(";")]
        opt = dict(a.split("=", 1) for a in sys.argv[4:])
        modus_netztest(konf, float(opt.get("S", "0.5")), int(opt.get("n", "1")),
                       opt.get("ordnungen", "MMD_AT_PLUS_A").split(","), protokoll, out, ziel)
    elif modus == "einbettung":
        ziel = sys.argv[2]
        N, L1, Lq, saat = int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6])
        modus_einbettung(N, L1, Lq, saat, [int(x) for x in sys.argv[7].split(",")],
                         [float(x) for x in sys.argv[8].split(",")], protokoll, out, ziel)
    elif modus == "kontrolle":
        ziel = sys.argv[2]
        N, L1, Lq, S = int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
        nlist = [int(x) for x in sys.argv[7].split(",")]
        teile = set(sys.argv[8].split(",")) if len(sys.argv) > 8 else {"K1", "K2", "K3", "K4", "K5", "K6"}
        modus_kontrolle(N, L1, Lq, S, nlist, teile, protokoll, out, ziel)
    elif modus == "dichte":
        N, L1, Lq = int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
        saat0, anzahl, ziel = int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
        nlist = [int(x) for x in sys.argv[8].split(",")]
        Slist = [float(x) for x in sys.argv[9].split(",")]
        opt = dict(a.split("=", 1) for a in sys.argv[10:])
        modus_dichte(N, L1, Lq, saat0, anzahl, ziel, nlist, Slist, opt.get("blind", "0") == "1",
                     opt.get("fest", "0") == "1", protokoll, out)
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["rss_mb_ende"] = rss_mb()
    out["protokoll"] = log
    speichern(ziel, out)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
