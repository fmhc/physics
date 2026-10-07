#!/usr/bin/env python3
"""INDUZIERT-ZUFALL-2D (Runde 38, Code-Agent): induzierte Steifigkeit eines masselosen P1-Skalars auf zufaelligen
periodischen Delaunay-Netzen (2D-Torus) und auf dem regelmaessigen Netz aus INDUZIERT-1 Teil A.

Konvention (wie INDUZIERT-1 Teil A, Variante P):
  Gamma = 1/2 log det' K; K = P1-Steifigkeit (Kotangens-Laplace) allein aus den Kantenlaengen, masselos.
  det' K = N det K_(0), K_(0) = K ohne Zeile und Spalte des Knotens 0. Exakt fuer symmetrisches K mit K 1 = 0 und
  Rang N - 1, denn adj K = (det' K / N) 1 1^T. log det K_(0) per duenner LU (scipy splu: MMD_AT_PLUS_A,
  SymmetricMode, diag_pivot_thresh 0, keine Equilibrierung), Summe log U_ii (math.fsum).
  Konforme Mode (Ecken-Skalierung, INDUZIERT-1 [F3]): l_ij(s) = l_ij exp(s (sig_i + sig_j)/2), sig = cos(k.x_i).
  c_P = Gamma''(0)/(k^2 A), A = Torusflaeche (= N bei Dichte 1).
  c_D = c_P - 1/2 (sum_i log m_i)''/(k^2 A): det'(M^-1 K) ohne Flaechenglied, m_i = sum_{T an i} A_T/3 (Heron).
  Knotenverschiebung: x_i(s) = x_i + s e cos(k.x_i), e = k/|k| (laengs) oder e senkrecht dazu (quer); neue Laengen
  aus den verschobenen Punkten.
  Zweite Ableitung: symmetrische Differenzen mit h und 2h, Richardson R = (4 D(h) - D(2h))/3.
  Kantenlaengen-Norm einer Mode: sum_e (dl_e/ds)^2; kappa = Gamma''/Norm.

Aufruf (nur ueber kleintest.sh):
  python zufall2d.py kontrolle <aus.json>
  python zufall2d.py regulaer <L> <aus.json> <n-Liste, z. B. 1,2,4>
  python zufall2d.py zufall <N> <saat_start> <anzahl> <aus.json> <n-Liste> [versch=<n-Liste mit Verschiebungsmoden>]
"""
import json
import math
import os
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.spatial import Delaunay

POLYAKOV = -1.0 / (24.0 * math.pi)
H_KONF = 1e-2          # Schritt der konformen Mode (Amplitude von sigma)
ETA_VERSCH = 1e-2      # Schritt der Knotenverschiebung als Dehnungsamplitude: h = ETA_VERSCH/|k|
RICHTUNGEN = {"r000": (1, 0), "r045": (1, 1), "r090": (0, 1), "r135": (-1, 1)}
SAAT_BASIS = 20261004


def flaeche_kahan(a, b, c):
    """Dreiecksflaeche aus Kantenlaengen, numerisch stabile Heron-Form (Kahan)."""
    s = -np.sort(-np.stack([a, b, c], axis=1), axis=1)
    x, y, z = s[:, 0], s[:, 1], s[:, 2]
    p = (x + (y + z)) * (z - (x - y)) * (z + (x - y)) * (x + (y - z))
    return 0.25 * np.sqrt(np.maximum(p, 0.0))


class Netz:
    """Dreiecksnetz auf dem Torus [0, L)^2. Kanten eindeutig, Kantenvektoren im minimalen Bild."""

    def __init__(self, pos, tri, L, art):
        pos = np.asarray(pos, dtype=float)
        tri = np.asarray(tri, dtype=np.int64)
        N = pos.shape[0]
        self.N, self.L, self.A, self.art = N, float(L), float(L) * float(L), art
        self.pos, self.tri = pos, tri
        lok = np.stack([tri[:, [1, 2]], tri[:, [2, 0]], tri[:, [0, 1]]], axis=1)   # Kante gegenueber Ecke 0, 1, 2
        a = np.minimum(lok[..., 0], lok[..., 1])
        b = np.maximum(lok[..., 0], lok[..., 1])
        uniq, inv, cnt = np.unique((a * N + b).ravel(), return_inverse=True, return_counts=True)
        self.E, self.F = int(uniq.size), int(tri.shape[0])
        self.ki, self.kj = uniq // N, uniq % N
        self.tk = inv.reshape(-1, 3)
        self.kanten_zaehl = cnt
        d = pos[self.kj] - pos[self.ki]
        d -= self.L * np.round(d / self.L)
        self.ev = d
        self.l0 = np.hypot(d[:, 0], d[:, 1])
        e01 = pos[tri[:, 1]] - pos[tri[:, 0]]
        e01 -= self.L * np.round(e01 / self.L)
        e02 = pos[tri[:, 2]] - pos[tri[:, 0]]
        e02 -= self.L * np.round(e02 / self.L)
        self.orient = 0.5 * (e01[:, 0] * e02[:, 1] - e01[:, 1] * e02[:, 0])
        # festes Muster der geerdeten Matrix K_(0)
        m = (self.ki != 0) & (self.kj != 0)
        self._off = np.nonzero(m)[0]
        r = np.concatenate([self.ki[m] - 1, self.kj[m] - 1, np.arange(N - 1)])
        c = np.concatenate([self.kj[m] - 1, self.ki[m] - 1, np.arange(N - 1)])
        M = sp.csc_matrix((np.arange(1, r.size + 1, dtype=float), (r, c)), shape=(N - 1, N - 1))
        M.sort_indices()
        assert M.nnz == r.size
        self._perm = M.data.astype(np.int64) - 1
        self._indices, self._indptr = M.indices.copy(), M.indptr.copy()
        self.lu_info = {"aufrufe": 0, "min_U": float("inf"), "neg_U": 0, "perm_ungleich": 0, "sekunden": 0.0,
                        "nnz_LU": 0}

    # ------------------------------------------------------------------ Geometrie
    def kanten_dreieck(self, l):
        return l[self.tk[:, 0]], l[self.tk[:, 1]], l[self.tk[:, 2]]

    def gewichte(self, l):
        """Kotangens-Gewichte w_e = 1/2 sum cot(Gegenwinkel); K_ij = -w_ij, K_ii = sum_j w_ij."""
        a, b, c = self.kanten_dreieck(l)
        A = flaeche_kahan(a, b, c)
        a2, b2, c2 = a * a, b * b, c * c
        q = 0.125 / A
        w = (np.bincount(self.tk[:, 0], (b2 + c2 - a2) * q, self.E)
             + np.bincount(self.tk[:, 1], (c2 + a2 - b2) * q, self.E)
             + np.bincount(self.tk[:, 2], (a2 + b2 - c2) * q, self.E))
        return w, A

    def matrix(self, w):
        N = self.N
        diag = np.bincount(self.ki, w, N) + np.bincount(self.kj, w, N)
        werte = np.concatenate([-w[self._off], -w[self._off], diag[1:]])
        return sp.csc_matrix((werte[self._perm], self._indices, self._indptr), shape=(N - 1, N - 1))

    def matrix_voll_dicht(self, w):
        N = self.N
        K = np.zeros((N, N))
        np.add.at(K, (self.ki, self.kj), -w)
        np.add.at(K, (self.kj, self.ki), -w)
        diag = np.bincount(self.ki, w, N) + np.bincount(self.kj, w, N)
        K[np.arange(N), np.arange(N)] += diag
        return K

    def gamma(self, l):
        """1/2 log det' K aus den Kantenlaengen l (je eindeutiger Kante)."""
        t0 = time.time()
        w, A = self.gewichte(l)
        if not np.all(A > 0):
            raise RuntimeError("entartetes Dreieck")
        lu = spla.splu(self.matrix(w), permc_spec="MMD_AT_PLUS_A", diag_pivot_thresh=0.0,
                       options={"SymmetricMode": True, "Equil": False})
        d = lu.U.diagonal()
        info = self.lu_info
        info["aufrufe"] += 1
        info["min_U"] = min(info["min_U"], float(np.min(d)))
        info["neg_U"] += int(np.sum(d < 0))
        info["perm_ungleich"] += int(not np.array_equal(lu.perm_r, lu.perm_c))
        info["nnz_LU"] = int(lu.L.nnz + lu.U.nnz)
        g = 0.5 * (math.fsum(np.log(np.abs(d)).tolist()) + math.log(self.N))
        info["sekunden"] += time.time() - t0
        return g

    def summe_log_m(self, l):
        a, b, c = self.kanten_dreieck(l)
        A = flaeche_kahan(a, b, c)
        m = np.bincount(self.tri.ravel(), np.repeat(A / 3.0, 3), self.N)
        return math.fsum(np.log(m).tolist())

    def pruefen(self):
        """Topologie (Euler, jede Kante in genau zwei Dreiecken), Orientierung, Flaeche, Delaunay (Gegenwinkel)."""
        w, A = self.gewichte(self.l0)
        a, b, c = self.kanten_dreieck(self.l0)
        a2, b2, c2 = a * a, b * b, c * c
        w0 = np.arctan2(4 * A, b2 + c2 - a2)
        w1 = np.arctan2(4 * A, c2 + a2 - b2)
        w2 = np.arctan2(4 * A, a2 + b2 - c2)
        summe = (np.bincount(self.tk[:, 0], w0, self.E) + np.bincount(self.tk[:, 1], w1, self.E)
                 + np.bincount(self.tk[:, 2], w2, self.E))
        winkel = np.concatenate([w0, w1, w2])
        verschieden = bool(np.all((self.tri[:, 0] != self.tri[:, 1]) & (self.tri[:, 1] != self.tri[:, 2])
                                  & (self.tri[:, 0] != self.tri[:, 2])))
        return {
            "V": self.N, "E": self.E, "F": self.F, "euler": int(self.N - self.E + self.F),
            "kanten_genau_zwei": bool(np.all(self.kanten_zaehl == 2)), "ecken_verschieden": verschieden,
            "orient_min": float(np.min(self.orient)),
            "orient_gegen_heron_max_rel": float(np.max(np.abs(self.orient - A)) / np.mean(A)),
            "flaeche_summe_rel_abw": float(abs(math.fsum(A.tolist()) / self.A - 1.0)),
            "winkelsumme_minus_2pi_max": float(np.max(np.abs(w0 + w1 + w2 - np.pi))),
            "delaunay_max_gegenwinkel_minus_pi": float(np.max(summe - np.pi)),
            "delaunay_verletzt_1e-9": int(np.sum(summe > np.pi + 1e-9)),
            "w_min": float(np.min(w)), "w_max": float(np.max(w)),
            "l_min": float(np.min(self.l0)), "l_max": float(np.max(self.l0)), "l_mittel": float(np.mean(self.l0)),
            "l2_mittel": float(np.mean(self.l0 ** 2)),
            "winkel_min_grad": float(np.degrees(np.min(winkel))), "winkel_max_grad": float(np.degrees(np.max(winkel))),
            "flaeche_min": float(np.min(A)), "l_max_durch_L": float(np.max(self.l0) / self.L),
        }


# ---------------------------------------------------------------------- Netze
def zufallsnetz(N, saat):
    """N gleichverteilte Punkte in [0, L)^2, L = sqrt(N) (Dichte 1). Delaunay der 9 Kopien (scipy/Qhull);
    behalten werden die Dreiecke, deren Schwerpunkt im Grundbereich liegt (genau ein Bild je Torusdreieck),
    Ecken modulo N zurueckgefaltet, Orientierung positiv gemacht."""
    rng = np.random.default_rng([SAAT_BASIS, int(N), int(saat)])
    L = math.sqrt(N)
    pos = rng.uniform(0.0, L, size=(N, 2))
    versatz = np.array([(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)], dtype=float) * L
    P = (versatz[:, None, :] + pos[None, :, :]).reshape(-1, 2)
    S = Delaunay(P).simplices
    cen = P[S].mean(axis=1)
    halte = (cen[:, 0] >= 0) & (cen[:, 0] < L) & (cen[:, 1] >= 0) & (cen[:, 1] < L)
    S = S[halte]
    Q = P[S]
    cr = (Q[:, 1, 0] - Q[:, 0, 0]) * (Q[:, 2, 1] - Q[:, 0, 1]) - (Q[:, 1, 1] - Q[:, 0, 1]) * (Q[:, 2, 0] - Q[:, 0, 0])
    tri = S % N
    flip = cr < 0
    tri[flip] = tri[flip][:, [0, 2, 1]]
    return Netz(pos, tri, L, "zufall")


def regulaeres_netz(L):
    """INDUZIERT-1 Teil A: Quadrate mit (1,1)-Diagonale; Knotenindex x L + y wie induziert.vidx."""
    x, y = np.meshgrid(np.arange(L), np.arange(L), indexing="ij")
    x, y = x.ravel(), y.ravel()
    pos = np.stack([x, y], axis=1).astype(float)

    def idx(a, b):
        return (a % L) * L + (b % L)

    t1 = np.stack([idx(x, y), idx(x + 1, y), idx(x + 1, y + 1)], axis=1)
    t2 = np.stack([idx(x, y), idx(x + 1, y + 1), idx(x, y + 1)], axis=1)
    return Netz(pos, np.concatenate([t1, t2]), L, "regulaer")


# ---------------------------------------------------------------------- Moden
def l_konform(netz, kvec, s):
    sig = np.cos(netz.pos @ kvec)
    return netz.l0 * np.exp(0.5 * s * (sig[netz.ki] + sig[netz.kj]))


def l_versch(netz, kvec, e, s):
    c = np.cos(netz.pos @ kvec)
    d = netz.ev + s * (c[netz.kj] - c[netz.ki])[:, None] * e[None, :]
    return np.hypot(d[:, 0], d[:, 1])


def zweite(f, h, f0):
    fp1, fm1, fp2, fm2 = f(h), f(-h), f(2 * h), f(-2 * h)
    D1 = (fp1 - 2 * f0 + fm1) / (h * h)
    D2 = (fp2 - 2 * f0 + fm2) / (4 * h * h)
    R = (4 * D1 - D2) / 3.0
    g1 = (8 * (fp1 - fm1) - (fp2 - fm2)) / (12 * h)
    return R, D1, D2, g1


def punkt(netz, kint, g0, sm0, mit_versch=True, h_konf=H_KONF, eta=ETA_VERSCH):
    kvec = 2 * np.pi * np.asarray(kint, dtype=float) / netz.L
    kb = float(np.linalg.norm(kvec))
    k2A = kb * kb * netz.A
    sig = np.cos(netz.pos @ kvec)
    out = {"kint": [int(x) for x in kint], "betrag": kb, "k2A": k2A}
    R, D1, D2, g1 = zweite(lambda s: netz.gamma(l_konform(netz, kvec, s)), h_konf, g0)
    Rm, _, _, _ = zweite(lambda s: netz.summe_log_m(l_konform(netz, kvec, s)), h_konf, sm0)
    dl = netz.l0 * 0.5 * (sig[netz.ki] + sig[netz.kj])
    nrm = float(np.sum(dl * dl))
    out["konform"] = {"gamma2": R, "D_h": D1, "D_2h": D2, "richardson_abw_rel": abs(D1 - R) / max(abs(R), 1e-300),
                      "gamma1": g1, "schritt": h_konf, "c_P": R / k2A, "c_D": (R - 0.5 * Rm) / k2A,
                      "summe_log_m_2": Rm, "kantennorm": nrm, "kappa": R / nrm}
    if mit_versch:
        khat = kvec / kb
        quer = np.array([-khat[1], khat[0]])
        h = eta / kb
        cc = np.cos(netz.pos @ kvec)
        ehat = netz.ev / netz.l0[:, None]
        for name, e in (("versch_laengs", khat), ("versch_quer", quer)):
            R, D1, D2, g1 = zweite(lambda s, e=e: netz.gamma(l_versch(netz, kvec, e, s)), h, g0)
            dl = (ehat @ e) * (cc[netz.kj] - cc[netz.ki])
            nrm = float(np.sum(dl * dl))
            out[name] = {"gamma2": R, "D_h": D1, "D_2h": D2,
                         "richardson_abw_rel": abs(D1 - R) / max(abs(R), 1e-300), "gamma1": g1, "schritt": h,
                         "c": R / k2A, "kantennorm": nrm, "kappa": R / nrm,
                         "verhaeltnis_zu_konform": (R / nrm) / abs(out["konform"]["kappa"])}
    return out


# ---------------------------------------------------------------------- exakte Blasensumme (INDUZIERT-1)
def blase_regulaer(L, kints):
    """Exakte Werte auf dem regelmaessigen Torus aus INDUZIERT-1 (induziert.py unveraendert): konforme Mode
    (Ecken-Skalierung) und Knotenverschiebungen, jeweils Gamma'' = (N/2) u^+ Pi u + Tadpole-Glied."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import induziert as ind
    kg = ind.Kuhn(2)
    ko = ind.Koeff(kg, 0.0)
    gi = ind.Gitterintegrale(ko, L, torus_nullmode=True)
    Gp, _ = ind.tadpole(ko, gi)
    N = L * L
    dirs = kg.dirs.astype(float)
    erg = {}
    for kint in kints:
        kint = np.array(kint, dtype=np.int64)
        k = 2 * np.pi * kint / L
        kb = float(np.linalg.norm(k))
        Pb = ind.pi_base(ko, gi, k, gi.bR(kint=kint))[0]
        ph = np.exp(1j * (dirs @ k))
        u_c = kg.s0 * (1 + ph)
        Qh = 0.5 * N * float(np.real(u_c.conj() @ Pb @ u_c))
        Qt = N * float(np.sum(Gp * kg.s0 * (1 + np.cos(dirs @ k))))
        e_l = k / kb
        e_q = np.array([-e_l[1], e_l[0]])
        ver = {}
        for name, e in (("versch_laengs", e_l), ("versch_quer", e_q)):
            u = 2.0 * (dirs @ e) * (ph - 1.0)
            Qh_e = 0.5 * N * float(np.real(u.conj() @ Pb @ u))
            Qt_e = 2.0 * N * float(np.sum(Gp * (1 - np.cos(dirs @ k))))
            ver[name] = Qh_e + Qt_e
        erg[tuple(int(x) for x in kint)] = {"gamma2_konform": Qh + Qt, "c_P": (Qh + Qt) / (kb * kb * N),
                                            "gamma2_versch_laengs": ver["versch_laengs"],
                                            "gamma2_versch_quer": ver["versch_quer"]}
    return erg, Gp.tolist()


# ---------------------------------------------------------------------- Modi
def modus_kontrolle(protokoll):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import induziert as ind
    out = {}
    rng = np.random.default_rng(SAAT_BASIS + 7)
    # (K1) Kotangens-Formel gegen die Gram-Formel aus INDUZIERT-1 (lokal_K_batch)
    p = rng.uniform(0, 1, size=(500, 3, 2))

    def dist(i, j):
        return np.linalg.norm(p[:, i] - p[:, j], axis=1)

    sq = np.stack([dist(0, 1) ** 2, dist(0, 2) ** 2, dist(1, 2) ** 2], axis=1)
    Kg = ind.lokal_K_batch(2, 0.0, sq)
    a, b, c = dist(1, 2), dist(0, 2), dist(0, 1)
    A = flaeche_kahan(a, b, c)
    w12 = (b * b + c * c - a * a) / (8 * A)
    w02 = (c * c + a * a - b * b) / (8 * A)
    w01 = (a * a + b * b - c * c) / (8 * A)
    Kc = np.zeros_like(Kg)
    for (i, j), w in (((0, 1), w01), ((0, 2), w02), ((1, 2), w12)):
        Kc[:, i, j] -= w
        Kc[:, j, i] -= w
        Kc[:, i, i] += w
        Kc[:, j, j] += w
    rel = np.max(np.abs(Kc - Kg), axis=(1, 2)) / np.max(np.abs(Kg), axis=(1, 2))
    out["K1_kotangens_gegen_gram_max_rel"] = float(np.max(rel))
    protokoll(f"K1 Kotangens gegen Gram: {np.max(rel):.2e}")
    # (K2) regelmaessiges Netz L = 16: Matrix und log det' gegen induziert.torus_K / torus_gamma
    L = 16
    kg = ind.Kuhn(2)
    nr = regulaeres_netz(L)
    s_k = np.tile(kg.s0, (L * L, 1))
    Kind = ind.torus_K(kg, L, 0.0, s_k)
    w, _ = nr.gewichte(nr.l0)
    Kmein = nr.matrix_voll_dicht(w)
    g_ind = ind.torus_gamma(kg, L, 0.0, s_k, True)[0]
    g_mein = nr.gamma(nr.l0)
    out["K2_regulaer_L16"] = {"matrix_max_abs": float(np.max(np.abs(Kind - Kmein))), "gamma_induziert": g_ind,
                              "gamma_lu": g_mein, "gamma_abw": abs(g_ind - g_mein),
                              "pruefung": nr.pruefen()}
    protokoll(f"K2 regulaer L=16: Matrix {np.max(np.abs(Kind - Kmein)):.2e}, Gamma {abs(g_ind - g_mein):.2e}")
    # (K3) kleines Zufallsnetz: LU (geerdet) gegen dichte slogdet(K + 1 1^T/N) und Eigenwerte
    k3 = []
    for Nk, saat in ((400, 0), (400, 1), (900, 0)):
        nz = zufallsnetz(Nk, saat)
        w, _ = nz.gewichte(nz.l0)
        K = nz.matrix_voll_dicht(w)
        sgn, ld = np.linalg.slogdet(K + 1.0 / Nk)
        ev = np.linalg.eigvalsh(K)
        g_ev = 0.5 * math.fsum(np.log(ev[1:]).tolist())
        g_lu = nz.gamma(nz.l0)
        k3.append({"N": Nk, "saat": saat, "gamma_lu": g_lu, "gamma_slogdet": 0.5 * ld, "vorzeichen": float(sgn),
                   "gamma_eigen": g_ev, "abw_slogdet": abs(g_lu - 0.5 * ld), "abw_eigen": abs(g_lu - g_ev),
                   "kleinster_eigenwert_betrag": float(abs(ev[0])), "zweiter_eigenwert": float(ev[1]),
                   "symmetrie": float(np.max(np.abs(K - K.T))), "zeilensumme": float(np.max(np.abs(K.sum(1)))),
                   "pruefung": nz.pruefen()})
        protokoll(f"K3 N={Nk} saat={saat}: LU gegen slogdet {k3[-1]['abw_slogdet']:.2e}, gegen Eigenwerte "
                  f"{k3[-1]['abw_eigen']:.2e}")
    out["K3_logdet"] = k3
    # (K4) Differenzenschema gegen die exakte Blasensumme, regelmaessig L = 16 und 64
    k4 = []
    for L in (16, 64):
        nr = regulaeres_netz(L)
        g0 = nr.gamma(nr.l0)
        sm0 = nr.summe_log_m(nr.l0)
        kints = [(n * r[0], n * r[1]) for r in RICHTUNGEN.values() for n in (1, 2)]
        exakt, _ = blase_regulaer(L, kints)
        for kint in kints:
            pt = punkt(nr, kint, g0, sm0)
            ex = exakt[kint]
            k4.append({"L": L, "kint": list(kint), "c_P_fd": pt["konform"]["c_P"], "c_P_exakt": ex["c_P"],
                       "rel_konform": abs(pt["konform"]["gamma2"] / ex["gamma2_konform"] - 1),
                       "rel_laengs": abs(pt["versch_laengs"]["gamma2"] / ex["gamma2_versch_laengs"] - 1),
                       "rel_quer": abs(pt["versch_quer"]["gamma2"] / ex["gamma2_versch_quer"] - 1),
                       "gamma2_laengs_fd": pt["versch_laengs"]["gamma2"],
                       "gamma2_laengs_exakt": ex["gamma2_versch_laengs"],
                       "gamma2_quer_fd": pt["versch_quer"]["gamma2"], "gamma2_quer_exakt": ex["gamma2_versch_quer"],
                       "richardson_konform": pt["konform"]["richardson_abw_rel"]})
        protokoll(f"K4 L={L}: max rel konform {max(x['rel_konform'] for x in k4 if x['L'] == L):.2e}, "
                  f"versch {max(max(x['rel_laengs'], x['rel_quer']) for x in k4 if x['L'] == L):.2e}")
    out["K4_fd_gegen_blase"] = k4
    # (K5) Schrittweiten auf einem Zufallsnetz N = 4000 (eigene Saat 999, nicht in den Hauptlaeufen)
    nz = zufallsnetz(4000, 999)
    g0 = nz.gamma(nz.l0)
    sm0 = nz.summe_log_m(nz.l0)
    k5 = []
    for kint in ((1, 0), (1, 1)):
        for hk, eta in ((5e-3, 5e-3), (1e-2, 1e-2), (2e-2, 2e-2)):
            pt = punkt(nz, kint, g0, sm0, True, hk, eta)
            k5.append({"kint": list(kint), "h_konf": hk, "eta": eta, "c_P": pt["konform"]["c_P"],
                       "c_D": pt["konform"]["c_D"], "c_laengs": pt["versch_laengs"]["c"],
                       "c_quer": pt["versch_quer"]["c"],
                       "richardson": [pt[x]["richardson_abw_rel"] for x in ("konform", "versch_laengs",
                                                                             "versch_quer")]})
            protokoll(f"K5 kint={kint} h={hk}: c_P {pt['konform']['c_P']:.8f} laengs {pt['versch_laengs']['c']:.8f} "
                      f"quer {pt['versch_quer']['c']:.8f}")
    out["K5_schritte"] = k5
    out["K5_pruefung"] = nz.pruefen()
    out["lu_info_K5"] = nz.lu_info
    return out


def modus_regulaer(L, nlist, protokoll):
    t0 = time.time()
    nr = regulaeres_netz(L)
    pr = nr.pruefen()
    g0 = nr.gamma(nr.l0)
    sm0 = nr.summe_log_m(nr.l0)
    kints = [(n * r[0], n * r[1]) for r in RICHTUNGEN.values() for n in nlist]
    exakt, Gp = blase_regulaer(L, kints)
    pts = []
    for name, r in RICHTUNGEN.items():
        for n in nlist:
            kint = (n * r[0], n * r[1])
            pt = punkt(nr, kint, g0, sm0)
            pt["richtung"], pt["n"] = name, n
            pt["exakt"] = exakt[kint]
            pts.append(pt)
            protokoll(f"regulaer L={L} {name} n={n}: c_P {pt['konform']['c_P']:.8f} (exakt {exakt[kint]['c_P']:.8f})"
                      f", kappa laengs/konform {pt['versch_laengs']['verhaeltnis_zu_konform']:.3f}")
    return {"L": L, "N": L * L, "pruefung": pr, "gamma0": g0, "tadpole_Gp": Gp, "punkte": pts,
            "lu": nr.lu_info, "sekunden": time.time() - t0}


def modus_zufall(N, saat0, anzahl, ziel, nlist, mit_versch, protokoll, out):
    out.update({"N": N, "L": math.sqrt(N), "nlist": nlist, "mit_versch": mit_versch, "h_konf": H_KONF,
                "eta_versch": ETA_VERSCH, "saaten": []})
    for saat in range(saat0, saat0 + anzahl):
        t0 = time.time()
        nz = zufallsnetz(N, saat)
        t_netz = time.time() - t0
        pr = nz.pruefen()
        g0 = nz.gamma(nz.l0)
        sm0 = nz.summe_log_m(nz.l0)
        pts = []
        for name, r in RICHTUNGEN.items():
            for n in nlist:
                pt = punkt(nz, (n * r[0], n * r[1]), g0, sm0, n in mit_versch)
                pt["richtung"], pt["n"] = name, n
                pts.append(pt)
        dauer = time.time() - t0
        out["saaten"].append({"saat": saat, "pruefung": pr, "gamma0": g0, "summe_log_m0": sm0, "punkte": pts,
                              "lu": dict(nz.lu_info), "sek_netz": t_netz, "sekunden": dauer})
        cp = {p["richtung"] + f"/n{p['n']}": round(p["konform"]["c_P"], 5) for p in pts}
        protokoll(f"N={N} saat={saat}: {dauer:.1f} s (Netz {t_netz:.1f} s, LU {nz.lu_info['sekunden']:.1f} s in "
                  f"{nz.lu_info['aufrufe']} Aufrufen, nnz(LU) {nz.lu_info['nnz_LU']}); Delaunay verletzt "
                  f"{pr['delaunay_verletzt_1e-9']}, Euler {pr['euler']}; c_P {cp}")
        with open(ziel + ".tmp", "w") as f:
            json.dump(out, f)
        os.replace(ziel + ".tmp", ziel)
    return out


def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    out = {"modus": modus, "argv": sys.argv[1:], "numpy": np.__version__}
    try:
        import scipy
        out["scipy"] = scipy.__version__
    except Exception:  # pragma: no cover
        pass
    if modus == "kontrolle":
        ziel = sys.argv[2]
        out.update(modus_kontrolle(protokoll))
    elif modus == "regulaer":
        L, ziel = int(sys.argv[2]), sys.argv[3]
        nlist = [int(x) for x in sys.argv[4].split(",")]
        out.update(modus_regulaer(L, nlist, protokoll))
    elif modus == "zufall":
        N, saat0, anzahl, ziel = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        nlist = [int(x) for x in sys.argv[6].split(",")]
        mit_versch = nlist if len(sys.argv) <= 7 else [int(x) for x in sys.argv[7].split("=")[1].split(",") if x]
        modus_zufall(N, saat0, anzahl, ziel, nlist, mit_versch, protokoll, out)
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["protokoll"] = log
    with open(ziel + ".tmp", "w") as f:
        json.dump(out, f)
    os.replace(ziel + ".tmp", ziel)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
