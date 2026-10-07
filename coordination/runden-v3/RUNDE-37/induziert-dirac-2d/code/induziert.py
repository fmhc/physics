#!/usr/bin/env python3
"""INDUZIERT-1 (Runde 37, Code-Agent): induzierte Wirkung eines P1-Skalars auf dem Kuhn-Netz (Sakharov-Test).

Gamma(s) = 1/2 log det K(s); K = P1-Steifigkeit + m^2 * konzentrierte Massenmatrix (V_sigma/(n+1) je Ecke);
s = Kantenlaengenquadrate (wie REGGE-4D-1, PLAN [F1]). Ein Knoten je Zelle, also ist G(q) skalar.

Hesse-Matrix pro Zelle in Fusspunkt-Konvention (Kante (x, d) von x nach x + d):
    Pi_dd'(k) = sum_R Hess_{(0,d),(R,d')} e^{ik.R}
              = 1/2 sum_Delta w_dd'Delta(k) g(Delta) - 1/2 [c(k) B(k) c(k)^+]_dd'
    V_d(p, p+k) = sum_Delta c_dDelta(k) e^{-ip.Delta}  (Vertexfunktion der ersten Ableitung)
    g(R) = int_q G(q) e^{-iqR},  b(R) = int_q G(q) G(q+k) e^{-iqR},  B_{Delta,Delta'} = b(Delta - Delta')
Die Gitterintegrale sind Riemann-Summen auf einem L_q^n-Gitter, per FFT; auf dem Torus L = L_q mit k auf dem
Gitter ist das exakt (Nullmode: G(0) = 0, also K^+).

Aufruf:
  python induziert.py kontrolle <aus.json>
  python induziert.py teilA <aus.json> [rauch]
  python induziert.py teilB <n> <m2> <Lq> <aus.json> [rauch]
"""
import itertools
import json
import math
import sys
import time

import numpy as np
import scipy.fft as sfft
import scipy.linalg as sla

BETRAEGE_B = [0.025, 0.05, 0.1, 0.2, 0.4]


# ----------------------------------------------------------------------------------------------- Gitter
class Kuhn:
    """Kuhn-Zerlegung des n-Wuerfels; Kantenrichtungen in derselben Reihenfolge wie regge4d.py."""

    def __init__(self, n):
        self.n = n
        dirs = [d for d in itertools.product((0, 1), repeat=n) if any(d)]
        dirs.sort(key=lambda d: (sum(d), tuple(-x for x in d)))
        self.dirs = np.array(dirs, dtype=np.int64)
        self.nE = len(dirs)
        self.dir_index = {tuple(d): i for i, d in enumerate(dirs)}
        self.perms = list(itertools.permutations(range(n)))
        self.paare = list(itertools.combinations(range(n + 1), 2))
        E = np.eye(n, dtype=np.int64)
        self.ecken = []
        for p in self.perms:
            v = [np.zeros(n, dtype=np.int64)]
            for a in p:
                v.append(v[-1] + E[a])
            self.ecken.append(np.array(v))
        self.lok_kanten = [[(v[a].copy(), self.dir_index[tuple(v[b] - v[a])]) for a, b in self.paare]
                           for v in self.ecken]
        D = set()
        for v in self.ecken:
            for c in range(n + 1):
                for cc in range(n + 1):
                    D.add(tuple(int(x) for x in v[c] - v[cc]))
        self.D = sorted(D)
        self.D_index = {d: i for i, d in enumerate(self.D)}
        self.nD = len(self.D)
        R = sorted(set(tuple(int(x) for x in np.array(a) - np.array(b)) for a in self.D for b in self.D))
        self.R = R
        self.R_index = {r: i for i, r in enumerate(R)}
        self.RidxDD = np.array([[self.R_index[tuple(int(x) for x in np.array(a) - np.array(b))] for b in self.D]
                                for a in self.D])
        self.s0 = np.sum(self.dirs ** 2, axis=1).astype(float)


def gram_E(n):
    """E_e = dG/ds_e, G_ab = (s_0a + s_0b - s_ab)/2 (a, b = 1..n); G = sum_e s_e E_e."""
    paare = list(itertools.combinations(range(n + 1), 2))
    Ee = np.zeros((len(paare), n, n))
    for k, (i, j) in enumerate(paare):
        X = np.zeros((n + 1, n + 1))
        X[i, j] = X[j, i] = 1.0
        Ee[k] = 0.5 * (X[0, 1:, None] + X[0, None, 1:] - X[1:, 1:])
    return Ee


def lokal(n, m2, sq, ordnung=2):
    """Lokale Matrix K = V P^T G^-1 P + m2 V/(n+1) I und ihre Ableitungen nach s (analytisch).

    sq: Kantenquadrate in der Reihenfolge combinations(range(n+1), 2); reell oder komplex (komplexer Schritt).
    """
    Ee = gram_E(n)
    G = np.einsum("e,eab->ab", sq, Ee)
    Ginv = np.linalg.inv(G)
    V = np.sqrt(np.linalg.det(G)) / math.factorial(n)
    P = np.hstack([-np.ones((n, 1)), np.eye(n)])
    Gam = P.T @ Ginv @ P
    I = np.eye(n + 1)
    cm = m2 / (n + 1)
    K = V * Gam + cm * V * I
    if ordnung == 0:
        return K
    A = np.einsum("ab,ebc->eac", Ginv, Ee)          # G^-1 E_e
    tr = np.einsum("eaa->e", A)
    dV = 0.5 * V * tr
    dGinv = -np.einsum("eab,bc->eac", A, Ginv)
    dGam = np.einsum("ai,eab,bj->eij", P, dGinv, P)
    dK = dV[:, None, None] * Gam + V * dGam + cm * dV[:, None, None] * I
    if ordnung == 1:
        return K, dK, V, dV
    AA = np.einsum("eab,fbc->efac", A, A)            # G^-1 E_e G^-1 E_f
    trAA = np.einsum("efaa->ef", AA)
    d2V = 0.25 * V * np.outer(tr, tr) - 0.5 * V * trAA
    d2Ginv = np.einsum("efab,bc->efac", AA, Ginv)
    d2Ginv = d2Ginv + np.swapaxes(d2Ginv, 0, 1)
    d2Gam = np.einsum("ai,efab,bj->efij", P, d2Ginv, P)
    d2K = (d2V[:, :, None, None] * Gam + dV[:, None, None, None] * dGam[None, :]
           + dV[None, :, None, None] * dGam[:, None] + V * d2Gam + cm * d2V[:, :, None, None] * I)
    return K, dK, d2K, V, dV, d2V


def lokal_K_batch(n, m2, sq):
    """Nur K, vektorisiert ueber Simplizes (Ns, nE) -> (Ns, n+1, n+1)."""
    Ee = gram_E(n)
    G = np.einsum("se,eab->sab", sq, Ee)
    Ginv = np.linalg.inv(G)
    V = np.sqrt(np.linalg.det(G)) / math.factorial(n)
    P = np.hstack([-np.ones((n, 1)), np.eye(n)])
    Gam = np.einsum("ai,sab,bj->sij", P, Ginv, P)
    return V[:, None, None] * (Gam + (m2 / (n + 1)) * np.eye(n + 1))


def heron_flaeche(sq):
    a, b, c = sq[:, 0], sq[:, 1], sq[:, 2]
    return 0.25 * np.sqrt(2 * a * b + 2 * b * c + 2 * c * a - a * a - b * b - c * c)


# ----------------------------------------------------------------------------------------------- Koeffizienten
class Koeff:
    """Termlisten fuer c(k), w(k), V''(k) und der Stencil der flachen Matrix, aus den analytischen Ableitungen."""

    def __init__(self, kg, m2):
        n = kg.n
        self.kg = kg
        self.m2 = m2
        kappa = np.zeros(kg.nD)
        cd, ci, cp, cv = [], [], [], []
        wd, wd2, wi, wp, wv = [], [], [], [], []
        vd, vd2, vp, vv = [], [], [], []
        Vp = np.zeros(kg.nE)
        Vtot = 0.0
        for t, v in enumerate(kg.ecken):
            sq = np.array([kg.s0[d] for _, d in kg.lok_kanten[t]])
            K, dK, d2K, V, dV, d2V = lokal(n, m2, sq)
            Vtot += V
            for c in range(n + 1):
                for cc in range(n + 1):
                    kappa[kg.D_index[tuple(int(x) for x in v[c] - v[cc])]] += K[c, cc]
            for e, (a, b) in enumerate(kg.paare):
                d = kg.lok_kanten[t][e][1]
                Vp[d] += dV[e]
                for c in range(n + 1):
                    for cc in range(n + 1):
                        cd.append(d)
                        ci.append(kg.D_index[tuple(int(x) for x in v[c] - v[cc])])
                        cp.append(v[cc] - v[a])
                        cv.append(dK[e, c, cc])
                for f, (a2, b2) in enumerate(kg.paare):
                    d2 = kg.lok_kanten[t][f][1]
                    vd.append(d)
                    vd2.append(d2)
                    vp.append(v[a2] - v[a])
                    vv.append(d2V[e, f])
                    for c in range(n + 1):
                        for cc in range(n + 1):
                            wd.append(d)
                            wd2.append(d2)
                            wi.append(kg.D_index[tuple(int(x) for x in v[c] - v[cc])])
                            wp.append(v[a2] - v[a])
                            wv.append(d2K[e, f, c, cc])
        self.kappa = kappa
        self.Vp = Vp
        self.Vzelle = Vtot
        self.c_idx = np.array(cd) * kg.nD + np.array(ci)
        self.c_phi = np.array(cp, float)
        self.c_val = np.array(cv)
        self.w_idx = (np.array(wd) * kg.nE + np.array(wd2)) * kg.nD + np.array(wi)
        self.w_phi = np.array(wp, float)
        self.w_val = np.array(wv)
        self.v_idx = np.array(vd) * kg.nE + np.array(vd2)
        self.v_phi = np.array(vp, float)
        self.v_val = np.array(vv)

    @staticmethod
    def _summe(idx, phi, val, k, laenge):
        ph = np.exp(1j * (phi @ k)) * val
        return (np.bincount(idx, weights=ph.real, minlength=laenge)
                + 1j * np.bincount(idx, weights=ph.imag, minlength=laenge))

    def c(self, k):
        kg = self.kg
        return self._summe(self.c_idx, self.c_phi, self.c_val, k, kg.nE * kg.nD).reshape(kg.nE, kg.nD)

    def w(self, k):
        kg = self.kg
        return self._summe(self.w_idx, self.w_phi, self.w_val, k, kg.nE * kg.nE * kg.nD).reshape(kg.nE, kg.nE,
                                                                                                    kg.nD)

    def V2(self, k):
        kg = self.kg
        return self._summe(self.v_idx, self.v_phi, self.v_val, k, kg.nE * kg.nE).reshape(kg.nE, kg.nE)


# ----------------------------------------------------------------------------------------------- Gitterintegrale
class Gitterintegrale:
    """G(q) auf dem L_q^n-Gitter, g(Delta), b(R) per FFT."""

    def __init__(self, ko, Lq, torus_nullmode=False):
        kg = ko.kg
        n = kg.n
        self.kg, self.ko, self.Lq, self.n = kg, ko, Lq, n
        self.Nq = Lq ** n
        st = np.zeros((Lq,) * n)
        for iD, Dv in enumerate(kg.D):
            st[tuple(int(x) % Lq for x in Dv)] += ko.kappa[iD]
        Kgen = sfft.fftn(st, workers=1)
        self.symbol_imag = float(np.max(np.abs(Kgen.imag)))
        Kgen = Kgen.real
        del st
        self.q1 = 2 * np.pi * np.arange(Lq) / Lq
        self.masse = float(np.sum(ko.kappa))       # K(q = 0) = m2 * Massenmatrix
        Ksep = self.separabel(np.zeros(n))
        self.separabel_abw = float(np.max(np.abs(Kgen - Ksep)))
        self.nutze_separabel = self.separabel_abw <= 1e-12 * float(np.max(np.abs(Kgen)))
        self.K = Kgen
        del Ksep
        self.nullmode = torus_nullmode
        with np.errstate(divide="ignore"):
            G = 1.0 / self.K
        if torus_nullmode:
            G[(0,) * n] = 0.0
        assert np.all(np.isfinite(G)), "G nicht endlich (masselos ohne Nullmoden-Behandlung?)"
        self.G = G
        Xg = sfft.rfftn(G, workers=1)
        self.gD = np.array([self._wert(Xg, Dv) for Dv in kg.D]).real / self.Nq
        self.gD_imag = float(np.max(np.abs(np.array([self._wert(Xg, Dv) for Dv in kg.D]).imag))) / self.Nq
        del Xg

    def separabel(self, k):
        n, Lq = self.n, self.Lq
        out = np.full((Lq,) * n, self.masse)
        for mu in range(n):
            form = [1] * n
            form[mu] = Lq
            out = out + (2.0 - 2.0 * np.cos(self.q1 + k[mu])).reshape(form)
        return out

    def K_verschoben(self, k):
        if self.nutze_separabel:
            return self.separabel(k)
        kg, Lq = self.kg, self.Lq
        st = np.zeros((Lq,) * self.n, complex)
        for iD, Dv in enumerate(kg.D):
            st[tuple(int(x) % Lq for x in Dv)] += self.ko.kappa[iD] * np.exp(-1j * np.dot(k, Dv))
        return sfft.fftn(st, workers=1).real

    def _wert(self, X, R):
        Lq = self.Lq
        R = np.array(R, dtype=np.int64)
        if int(R[-1]) % Lq <= Lq // 2:
            return X[tuple(int(x) % Lq for x in R)]
        return np.conj(X[tuple(int(x) % Lq for x in -R)])

    def bR(self, k=None, kint=None):
        """b(R) fuer alle R in kg.R; k frei (G(q+k) aus dem verschobenen Symbol) oder kint auf dem Gitter (roll)."""
        if kint is not None:
            Gk = np.roll(self.G, shift=tuple(-int(x) for x in kint), axis=tuple(range(self.n)))
        else:
            Gk = 1.0 / self.K_verschoben(k)
        F = self.G * Gk
        del Gk
        X = sfft.rfftn(F, workers=1)
        del F
        return np.array([self._wert(X, R) for R in self.kg.R]) / self.Nq


def pi_base(ko, gi, k, bR):
    """Pi(k) in Fusspunkt-Konvention; dazu Tadpole- und Blasenanteil."""
    kg = ko.kg
    ck = ko.c(k)
    wk = ko.w(k)
    B = bR[kg.RidxDD]
    Pb = -0.5 * ck @ B @ ck.conj().T
    Pt = 0.5 * np.einsum("abD,D->ab", wk, gi.gD)
    return Pt + Pb, Pt, Pb


def tadpole(ko, gi):
    """dGamma/ds_d pro Zelle: 1/2 sum_Delta c_dDelta(0) g(Delta)."""
    c0 = ko.c(np.zeros(ko.kg.n))
    return 0.5 * (c0 @ gi.gD).real, float(np.max(np.abs((c0 @ gi.gD).imag)))


def herm_rel(P):
    return float(np.max(np.abs(P - P.conj().T)) / max(np.max(np.abs(P)), 1e-300))


def mat_json(P):
    return {"re": np.real(P).tolist(), "im": np.imag(P).tolist()}


# ----------------------------------------------------------------------------------------------- direkter Torus
def vidx(y, L):
    y = np.mod(y, L)
    r = np.zeros(y.shape[0], dtype=np.int64)
    for c in range(y.shape[1]):
        r = r * L + y[:, c]
    return r


def torus_K(kg, L, m2, s_kante):
    n = kg.n
    coords = np.array(list(itertools.product(range(L), repeat=n)), dtype=np.int64)
    N = L ** n
    K = np.zeros((N, N))
    for t, v in enumerate(kg.ecken):
        sq = np.stack([s_kante[vidx(coords + b, L), d] for b, d in kg.lok_kanten[t]], axis=1)
        Kl = lokal_K_batch(n, m2, sq)
        idx = np.stack([vidx(coords + v[c], L) for c in range(n + 1)], axis=1)
        np.add.at(K, (idx[:, :, None], idx[:, None, :]), Kl)
    return K


def torus_gamma(kg, L, m2, s_kante, nullmode):
    K = torus_K(kg, L, m2, s_kante)
    N = K.shape[0]
    if nullmode:
        K = K + 1.0 / N
    sign, ld = np.linalg.slogdet(K)
    return 0.5 * ld, float(sign)


def zweite_differenz(f, eps):
    f0 = f(0.0)

    def D(h):
        return (f(h) - 2 * f0 + f(-h)) / (h * h)

    d1, d2 = D(eps), D(eps / 2)
    return (4 * d2 - d1) / 3.0, abs(d2 - d1)


def erste_differenz(f, eps):
    def D(h):
        return (f(h) - f(-h)) / (2 * h)

    return (4 * D(eps / 2) - D(eps)) / 3.0


# ----------------------------------------------------------------------------------------------- Modus kontrolle
def modus_kontrolle(protokoll):
    out = {}
    rng = np.random.default_rng(20261004)
    # (K5) lokale Ableitungen: analytisch gegen komplexen Schritt bzw. Differenz komplexer Schritte
    abl = {}
    for n in (2, 3, 4):
        kg = Kuhn(n)
        m2 = 0.04
        e1, e2, e3 = 0.0, 0.0, 0.0
        for t in range(len(kg.ecken)):
            sq0 = np.array([kg.s0[d] for _, d in kg.lok_kanten[t]])
            # leicht verzerrt, damit keine Symmetrie hilft
            sq = sq0 * (1 + 0.05 * rng.standard_normal(len(sq0)))
            K, dK, d2K, V, dV, d2V = lokal(n, m2, sq)
            hc = 1e-20
            nE = len(sq)
            for e in range(nE):
                z = sq.astype(complex)
                z[e] += 1j * hc
                dK_cs = lokal(n, m2, z, ordnung=0).imag / hc
                e1 = max(e1, float(np.max(np.abs(dK_cs - dK[e]))))
                _, dKz, _, _ = lokal(n, m2, z, ordnung=1)
                d2K_cs = dKz.imag / hc          # Zeile e: d/ds_e von dK_f
                e2 = max(e2, float(np.max(np.abs(d2K_cs - d2K[e]))))
                # unabhaengig: zentrale Differenz komplexer Schritte
                h = 1e-4
                for f in range(nE):
                    zp = sq.astype(complex)
                    zp[e] += h
                    zp[f] += 1j * hc
                    zm = sq.astype(complex)
                    zm[e] -= h
                    zm[f] += 1j * hc
                    fd = (lokal(n, m2, zp, ordnung=0).imag - lokal(n, m2, zm, ordnung=0).imag) / (2 * h * hc)
                    e3 = max(e3, float(np.max(np.abs(fd - d2K[e, f]))))
        abl[f"n{n}"] = {"dK_analytisch_gegen_komplex": e1, "d2K_analytisch_gegen_komplex_von_dK": e2,
                        "d2K_analytisch_gegen_zentral_komplex": e3}
        protokoll(f"Ableitungen n={n}: {e1:.2e} {e2:.2e} {e3:.2e}")
    out["ableitungen"] = abl
    # (K6) Symbol: P1 auf dem flachen Kuhn-Netz gegen sum 4 sin^2(q/2)
    sym = {}
    for n in (2, 3, 4):
        kg = Kuhn(n)
        ko = Koeff(kg, 0.0)
        qs = rng.uniform(-np.pi, np.pi, size=(64, n))
        Kq = np.array([np.sum(ko.kappa * np.exp(-1j * (np.array(kg.D) @ q))) for q in qs])
        ref = np.sum(4 * np.sin(qs / 2) ** 2, axis=1)
        sym[f"n{n}"] = {"max_abs": float(np.max(np.abs(Kq - ref))), "max_imag": float(np.max(np.abs(Kq.imag))),
                        "kappa": {str(kg.D[i]): float(ko.kappa[i]) for i in range(kg.nD) if abs(ko.kappa[i]) > 1e-14}}
        # Gewicht der Diagonalkanten: Stencil-Eintraege ausserhalb der Achsen
        achsen = [i for i, Dv in enumerate(kg.D) if sum(abs(x) for x in Dv) <= 1]
        sym[f"n{n}"]["max_abs_nichtachsen_stencil"] = float(max(abs(ko.kappa[i]) for i in range(kg.nD)
                                                                if i not in achsen))
        protokoll(f"Symbol n={n}: {sym[f'n{n}']['max_abs']:.2e}")
    out["symbol"] = sym
    # (K1-K4) Torus: Blasensumme gegen direkte zweite Differenz von 1/2 log det
    tor = []
    faelle = [(2, 16, 0.0, [(1, 0), (3, 2)]), (2, 16, 0.04, [(1, 0), (3, 2)]),
              (3, 6, 0.04, [(1, 0, 0), (1, 2, 1)]), (4, 5, 0.04, [(1, 0, 0, 0), (1, 2, 0, 1)]),
              (4, 5, 0.0, [(1, 0, 0, 0), (2, 1, 1, 0)])]
    for n, L, m2, kliste in faelle:
        t0 = time.time()
        kg = Kuhn(n)
        ko = Koeff(kg, m2)
        null = (m2 == 0.0)
        gi = Gitterintegrale(ko, L, torus_nullmode=null)
        N = L ** n
        coords = np.array(list(itertools.product(range(L), repeat=n)), dtype=np.int64)
        Gp, _ = tadpole(ko, gi)

        def gam(s_k):
            return torus_gamma(kg, L, m2, s_k, null)[0]

        s0k = np.tile(kg.s0, (N, 1))
        # erste Ableitungen: alle Kanten eines Typs gleichzeitig
        tad_dir = []
        for d in range(kg.nE):
            ed = np.zeros(kg.nE)
            ed[d] = 1.0
            fd = erste_differenz(lambda h: gam(s0k + h * ed[None, :]), 2e-3)
            tad_dir.append(abs(fd - N * Gp[d]) / max(abs(N * Gp[d]), 1e-300))
        for kint in kliste:
            k = 2 * np.pi * np.array(kint, float) / L
            bR = gi.bR(kint=np.array(kint))
            Pb, _, _ = pi_base(ko, gi, k, bR)
            for wdh in range(2):
                u = rng.standard_normal(kg.nE) + 1j * rng.standard_normal(kg.nE)
                welle = np.real(u[None, :] * np.exp(1j * (coords @ k))[:, None])
                Q_b = 0.5 * N * float(np.real(u.conj() @ Pb @ u))
                Q_d, fehl = zweite_differenz(lambda h: gam(s0k + h * welle), 2.5e-3)
                tor.append({"n": n, "L": L, "m2": m2, "kint": list(kint), "art": "ebene_welle",
                            "blase": Q_b, "direkt": Q_d, "rel_abw": abs(Q_d - Q_b) / abs(Q_b),
                            "richardson_schaetzung": fehl, "herm_rel": herm_rel(Pb)})
            if n == 2 and m2 == 0.0:
                # konforme Mode (Ecken-Skalierung) wie in Teil A
                sig = np.cos(coords @ k)
                ss = np.stack([sig + sig[vidx(coords + kg.dirs[d], L)] for d in range(kg.nE)], axis=1)
                u_c = kg.s0 * (1 + np.exp(1j * (kg.dirs @ k)))
                Qh = 0.5 * N * float(np.real(u_c.conj() @ Pb @ u_c))
                Qt = N * float(np.sum(Gp * kg.s0 * (1 + np.cos(kg.dirs @ k))))
                Q_d, fehl = zweite_differenz(lambda h: gam(s0k * np.exp(h * ss)), 2.5e-3)
                tor.append({"n": n, "L": L, "m2": m2, "kint": list(kint), "art": "konform_eckenskalierung",
                            "blase": Qh + Qt, "blase_hesse": Qh, "blase_tadpole": Qt, "direkt": Q_d,
                            "rel_abw": abs(Q_d - Qh - Qt) / abs(Qh + Qt), "richardson_schaetzung": fehl})
        tor.append({"n": n, "L": L, "m2": m2, "art": "tadpole_erste_ableitung",
                    "rel_abw_max": float(max(tad_dir)), "Gamma_strich": Gp.tolist()})
        protokoll(f"Torus n={n} L={L} m2={m2}: fertig ({time.time() - t0:.1f} s), "
                  f"max rel {max(x.get('rel_abw', x.get('rel_abw_max', 0)) for x in tor if x['n'] == n and x['L'] == L and x['m2'] == m2):.2e}")
    out["torus"] = tor
    return out


# ----------------------------------------------------------------------------------------------- Teil A (2D)
def modus_teilA(protokoll, rauch):
    kg = Kuhn(2)
    ko = Koeff(kg, 0.0)
    erg = {"polyakov": -1.0 / (24 * np.pi), "laeufe": []}
    groessen = [64, 128] if rauch else [256, 512, 1024]
    richt = {"achse_10": (1, 0), "diag_11": (1, 1), "gegen_1m1": (1, -1)}
    for L in groessen:
        t0 = time.time()
        gi = Gitterintegrale(ko, L, torus_nullmode=True)
        Gp, Gp_im = tadpole(ko, gi)
        N = L * L
        coords = None
        P0b = pi_base(ko, gi, np.zeros(2), gi.bR(kint=np.zeros(2, dtype=np.int64)))[0]
        lauf = {"L": L, "Gamma_strich": Gp.tolist(), "Gamma_strich_imag": Gp_im, "Pi0": mat_json(P0b),
                "symbol_separabel_abw": gi.separabel_abw, "punkte": []}
        nlist = [1, 2, 4, 8, 16, 32, 64] if L >= 512 else [1, 2, 4, 8, 16]
        if rauch:
            nlist = [1, 2, 4, 8]
        for name, rv in richt.items():
            for nn in nlist:
                kint = nn * np.array(rv, dtype=np.int64)
                k = 2 * np.pi * kint / L
                if np.linalg.norm(k) > 0.8:
                    continue
                bR = gi.bR(kint=kint)
                Pb, Pt, Pbb = pi_base(ko, gi, k, bR)
                u_c = kg.s0 * (1 + np.exp(1j * (kg.dirs @ k)))
                Qh = 0.5 * N * float(np.real(u_c.conj() @ Pb @ u_c))
                Qt = N * float(np.sum(Gp * kg.s0 * (1 + np.cos(kg.dirs @ k))))
                k2A = float(k @ k) * N
                # Massterm (konzentrierte Massenmatrix) entlang der Ecken-Skalierung, im Ortsraum
                if coords is None:
                    coords = np.array(list(itertools.product(range(L), repeat=2)), dtype=np.int64)
                    nb = [vidx(coords + kg.dirs[d], L) for d in range(kg.nE)]
                    ecken_idx = [[vidx(coords + v[c], L) for c in range(3)] for v in kg.ecken]
                    kant_idx = [[(vidx(coords + b, L), d) for b, d in kg.lok_kanten[t]] for t in range(2)]
                sig = np.cos(coords @ k)
                ss = np.stack([sig + sig[nb[d]] for d in range(kg.nE)], axis=1)

                def summe_log_m(h):
                    s_k = kg.s0[None, :] * np.exp(h * ss)
                    m = np.zeros(N)
                    for t in range(2):
                        sq = np.stack([s_k[i, d] for i, d in kant_idx[t]], axis=1)
                        A_T = heron_flaeche(sq)
                        for c in range(3):
                            m += np.bincount(ecken_idx[t][c], weights=A_T / 3.0, minlength=N)
                    return float(np.sum(np.log(m)))

                Mpp, Mfehl = zweite_differenz(summe_log_m, 2.5e-3)
                # Eichmoden (Knotenverschiebungen), Mittelpunktskonvention, je Einheit Kantenquadrat-Aenderung
                ph = np.exp(1j * (kg.dirs @ k) / 2)
                Pm = np.conj(ph)[:, None] * Pb * ph[None, :]
                Pm = 0.5 * (Pm + Pm.conj().T)
                P0 = 0.5 * (P0b + P0b.conj().T).real
                cosf = np.cos(0.5 * (kg.dirs @ k)[None, :] - 0.5 * (kg.dirs @ k)[:, None])
                Gb = np.sin(0.5 * (kg.dirs @ k))[:, None] * kg.dirs.astype(float)
                M = Gb.T @ Gb
                eich_roh = sla.eigh(Gb.T @ Pm @ Gb, M, eigvals_only=True)
                eich_ct = sla.eigh(Gb.T @ (Pm - P0 * cosf) @ Gb, M, eigvals_only=True)
                uc_m = kg.s0 * 2 * np.cos(0.5 * (kg.dirs @ k))
                konf_ct = float(np.real(uc_m @ (Pm - P0 * cosf) @ uc_m) / (uc_m @ uc_m))
                konf_roh = float(np.real(uc_m @ Pm @ uc_m) / (uc_m @ uc_m))
                lauf["punkte"].append({
                    "richtung": name, "n": int(nn), "kint": kint.tolist(), "betrag": float(np.linalg.norm(k)),
                    "Q_hesse": Qh, "Q_tadpole_eckenskalierung": Qt, "Q_massterm_sum_log_m": Mpp,
                    "Q_massterm_fehler": Mfehl,
                    "c_P_eckenskalierung": (Qh + Qt) / k2A, "c_l_linear": (Qh + 0.5 * Qt) / k2A,
                    "c_s_linear": Qh / k2A, "c_D_mit_mass": (Qh + Qt - 0.5 * Mpp) / k2A,
                    "herm_rel": herm_rel(Pb), "Pi_base": mat_json(Pb),
                    "eich_roh_durch_k2": (eich_roh / float(k @ k)).tolist(),
                    "eich_ct_durch_k2": (eich_ct / float(k @ k)).tolist(),
                    "konform_rayleigh_roh_durch_k2": konf_roh / float(k @ k),
                    "konform_rayleigh_ct_durch_k2": konf_ct / float(k @ k)})
        protokoll(f"Teil A L={L}: {len(lauf['punkte'])} Punkte ({time.time() - t0:.1f} s)")
        erg["laeufe"].append(lauf)
    # Teil A2 (beschreibend): k^2-Form in h fuer viele Richtungen, fuer die 4phi-Harmonische (Polyakov-Anteil)
    import regge4d
    B2 = regge4d.Gitter(2, 3).B0()
    assert np.array_equal(regge4d.Gitter(2, 3).dirs, kg.dirs)
    erg["harmonische"] = []
    for L in ([128] if rauch else [512, 1024]):
        t0 = time.time()
        gi = Gitterintegrale(ko, L, torus_nullmode=True)
        z = np.zeros(2, dtype=np.int64)
        P0b = pi_base(ko, gi, np.zeros(2), gi.bR(kint=z))[0]
        K0 = B2.T @ (0.5 * (P0b + P0b.conj().T)).real @ B2
        pts = []
        for n1 in range(-12, 13):
            for n2 in range(0, 13):
                if n2 == 0 and n1 <= 0:
                    continue
                nn = math.hypot(n1, n2)
                if nn < 4 or nn > 12:
                    continue
                kint = np.array([n1, n2], dtype=np.int64)
                k = 2 * np.pi * kint / L
                Pb = pi_base(ko, gi, k, gi.bR(kint=kint))[0]
                ph = np.exp(1j * (kg.dirs @ k) / 2)
                Pm = np.conj(ph)[:, None] * Pb * ph[None, :]
                Pm = 0.5 * (Pm + Pm.conj().T)
                K = B2.T @ Pm.real @ B2
                k2 = float(k @ k)
                pts.append({"kint": kint.tolist(), "betrag": math.sqrt(k2), "phi": math.atan2(k[1], k[0]),
                            "K2": ((K - K0) / k2).tolist(),
                            "imag_rel": float(np.max(np.abs(Pm.imag)) / np.max(np.abs(Pm)))})
        erg["harmonische"].append({"L": L, "K0": K0.tolist(), "punkte": pts})
        protokoll(f"Teil A2 L={L}: {len(pts)} Richtungen ({time.time() - t0:.1f} s)")
    return erg


# ----------------------------------------------------------------------------------------------- Teil B (n-D)
def richtungen_n(n):
    import regge4d
    return regge4d.richtungen(n)


def modus_teilB(n, m2, Lq, protokoll, rauch):
    t0 = time.time()
    kg = Kuhn(n)
    ko = Koeff(kg, m2)
    gi = Gitterintegrale(ko, Lq, torus_nullmode=False)
    protokoll(f"n={n} m2={m2} Lq={Lq}: Gitter fertig ({time.time() - t0:.1f} s), separabel {gi.nutze_separabel} "
              f"(Abw. {gi.separabel_abw:.1e})")
    Gp, Gp_im = tadpole(ko, gi)
    out = {"n": n, "m2": m2, "Lq": Lq, "dirs": kg.dirs.tolist(), "s0": kg.s0.tolist(),
           "Gamma_strich": Gp.tolist(), "Gamma_strich_imag": Gp_im, "V_strich": ko.Vp.tolist(),
           "V_zelle": ko.Vzelle, "masse_zelle": gi.masse, "symbol_separabel_abw": gi.separabel_abw,
           "symbol_imag": gi.symbol_imag, "gD": gi.gD.tolist(), "gD_imag": gi.gD_imag,
           "D": [list(x) for x in kg.D], "punkte": []}
    R = richtungen_n(n)
    punkte = [("null", 0.0, np.zeros(n))]
    betr = [0.05, 0.2] if rauch else BETRAEGE_B
    namen = list(R)[:3] if rauch else list(R)
    for name in namen:
        for b in betr:
            punkte.append((name, b, b * R[name]))
    for name, b, k in punkte:
        t1 = time.time()
        bR = gi.bR(k=k)
        Pb, Pt, Pbb = pi_base(ko, gi, k, bR)
        out["punkte"].append({"richtung": name, "betrag_nominal": b, "k": k.tolist(), "Pi_base": mat_json(Pb),
                              "herm_rel": herm_rel(Pb), "norm_tadpole": float(np.linalg.norm(Pt)),
                              "norm_blase": float(np.linalg.norm(Pbb)), "V2_base": mat_json(ko.V2(k)),
                              "sekunden": time.time() - t1})
    out["laufzeit_s"] = time.time() - t0
    protokoll(f"n={n} m2={m2} Lq={Lq}: {len(punkte)} k-Punkte fertig ({time.time() - t0:.1f} s)")
    return out


def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    if modus == "kontrolle":
        ziel = sys.argv[2]
        out = modus_kontrolle(protokoll)
    elif modus == "teilA":
        ziel = sys.argv[2]
        out = modus_teilA(protokoll, len(sys.argv) > 3 and sys.argv[3] == "rauch")
    elif modus == "teilB":
        n, m2, Lq, ziel = int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        out = modus_teilB(n, m2, Lq, protokoll, len(sys.argv) > 6 and sys.argv[6] == "rauch")
    else:
        raise SystemExit("unbekannter Modus")
    out["modus"] = modus
    out["numpy"] = np.__version__
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["protokoll"] = log
    with open(ziel, "w") as f:
        json.dump(out, f)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
