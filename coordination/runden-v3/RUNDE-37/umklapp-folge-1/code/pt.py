#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PACHNER-TAKT-1 mit TAKT-KOMMUTATOR-1 (fmhc-physics, Runde 41/42), Code-Agent fuer die Leitung claude-primary.

Modi:
  kc          Kontrolle reines C: Summenregel der Mittelpunktshoehen, Winkel des Rueckwechsels.
  takt        linearisiertes kanonisches Regge (Hoehn 2014) fuer die Takt-Varianten TT, B, C2, C3 auf einer B1-Kopie
              (fcc, Tetraeder-Oktaeder-Wabe, eine Diagonale je Oktaeder); Rang des effektiven Lagrange-Zweiforms
              Omega~ zwischen Sigma_0 und Sigma_T ueber m Takte.
  kommutator  zwei Zeltzuege an Nachbarecken A, B in der Reihenfolge AB gegen BA; Innenkanten nichtlinear nach Regge
              geloest (Newton), Vergleich der Randimpulse; dazu der lineare Koeffizient aus den flachen Hesse-Formen.
Einheiten: kubische Kante 1, Stablaenge a = 1/sqrt2. Euklidischer R^4 mit Koordinaten (x, y, z, t).
"""
import argparse, json, sys, time, platform, os, resource, hashlib, copy
import numpy as np

PAARE5 = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
PIDX = {p: i for i, p in enumerate(PAARE5)}
DREI5 = [tuple(x for x in range(5) if x not in p) for p in PAARE5]          # Dreieck gegenueber Paar k
DREI_KANTEN = [[PIDX[(t[0], t[1])], PIDX[(t[0], t[2])], PIDX[(t[1], t[2])]] for t in DREI5]
PAARE4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

A1 = np.array([0, 1, 1]); A2 = np.array([1, 0, 1]); A3 = np.array([1, 1, 0])   # ganzzahlig (2 x kubisch)
OKT_OFF = [A1, A2, A3, A1 + A2, A2 + A3, A3 + A1]
OKT_ACHSE = {0: (0, 4), 1: (1, 5), 2: (2, 3)}                                # x, y, z (Diagonalenden)
PAR2KL = {(0, 0, 0): 0, (0, 1, 1): 1, (1, 0, 1): 2, (1, 1, 0): 3}             # Klassen 0, X, Y, Z


def norm(refs):
    refs = sorted(refs, key=lambda r: r[0])
    s0 = refs[0][1]
    return tuple((v, (s[0] - s0[0], s[1] - s0[1], s[2] - s0[2])) for v, s in refs)


def kkey(r1, r2):
    (v1, s1), (v2, s2) = r1, r2
    if v1 > v2:
        (v1, s1), (v2, s2) = (v2, s2), (v1, s1)
    assert v1 != v2
    return (v1, v2, s2[0] - s1[0], s2[1] - s1[1], s2[2] - s1[2])


# ================================================================================================= Netz und Zuege
class Netz:
    def __init__(self, n, hoehen='klasse', variante='C2', zentrum=False):
        self.n = n
        N2 = 2 * n
        self.X, self.t, self.kl, self.orig, self.gen = [], [], [], [], []
        self.idx = {}
        for i in range(N2):
            for j in range(N2):
                for k in range(N2):
                    if (i + j + k) % 2 == 0:
                        self.idx[(i, j, k)] = len(self.X)
                        kl = PAR2KL[(i % 2, j % 2, k % 2)]
                        self.X.append(np.array([i, j, k], float) / 2.0)
                        self.t.append(0.25 * kl if hoehen == 'klasse' else 0.0)
                        self.kl.append(kl)
                        self.orig.append(len(self.X) - 1)
                        self.gen.append(0)
        self.V0 = len(self.X)
        self.cur = list(range(self.V0))
        self.klasse_orig = [[v for v in range(self.V0) if self.kl[v] == K] for K in range(4)]
        self.sigma = set()
        self.stern = {}
        self.simp = []
        self.simp_typ = []
        self.okt = []
        self.tet2 = []
        for (i, j, k), v in self.idx.items():
            r = np.array([i, j, k])
            self._add(norm([self.wrap(r), self.wrap(r + A1), self.wrap(r + A2), self.wrap(r + A3)]))      # tet1
            t2 = [self.wrap(r), self.wrap(r - A1), self.wrap(r - A2), self.wrap(r - A3)]                  # tet2
            self._add(norm(t2))
            self.tet2.append(t2)
            refs6 = [self.wrap(r + o) for o in OKT_OFF]
            M = self.kl[v]
            achse_kl = {ax: self.kl[refs6[OKT_ACHSE[ax][0]][0]] for ax in range(3)}
            kl_achse = {c: ax for ax, c in achse_kl.items()}
            paar = [(M + 1) % 4, (M + 3) % 4]
            if variante == 'C3':
                d0 = max(c for c in range(4) if c != M)
            else:
                d0 = max(paar)
            okt = {'refs': refs6, 'M': M, 'achse_kl': achse_kl, 'kl_achse': kl_achse, 'paar': paar,
                   'diag_kl': d0}
            self.okt.append(okt)
            p, q = OKT_ACHSE[kl_achse[d0]]
            others = [ax for ax in range(3) if ax != kl_achse[d0]]
            for a in OKT_ACHSE[others[0]]:
                for b in OKT_ACHSE[others[1]]:
                    self._add(norm([refs6[p], refs6[q], refs6[a], refs6[b]]))

    def wrap(self, q):
        N2 = 2 * self.n
        base = np.mod(q, N2)
        s = (np.asarray(q) - base) // N2
        return (self.idx[tuple(int(x) for x in base)], (int(s[0]), int(s[1]), int(s[2])))

    def _add(self, key):
        assert key not in self.sigma, key
        self.sigma.add(key)
        for v, s in key:
            self.stern.setdefault(v, set()).add(key)

    def _del(self, key):
        self.sigma.remove(key)
        for v, s in key:
            self.stern[v].remove(key)

    def neue_ecke(self, X, t, kl, orig, gen):
        self.X.append(np.asarray(X, float)); self.t.append(float(t)); self.kl.append(kl)
        self.orig.append(orig); self.gen.append(gen)
        return len(self.X) - 1

    def pos(self, ref):
        v, s = ref
        return np.r_[self.X[v] + self.n * np.array(s, float), self.t[v]]

    def zelt(self, v, dt):
        v2 = self.neue_ecke(self.X[v], self.t[v] + dt, self.kl[v], self.orig[v], self.gen[v] + 1)
        for key in list(self.stern.get(v, ())):
            sv = [s for (w, s) in key if w == v][0]
            self.simp.append(list(key) + [(v2, sv)])
            self.simp_typ.append('zelt')
            neu = norm([(v2, s) if w == v else (w, s) for (w, s) in key])
            self._del(key)
            self._add(neu)
        if 0 <= self.orig[v] < self.V0 and self.cur[self.orig[v]] == v:
            self.cur[self.orig[v]] = v2
        return v2

    def flip(self, okt, K):
        refs6 = [(self.cur[o], s) for (o, s) in okt['refs']]
        d = okt['kl_achse'][okt['diag_kl']]
        k = okt['kl_achse'][K]
        m = 3 - d - k
        p, q = OKT_ACHSE[d]; k1, k2 = OKT_ACHSE[k]; m1, m2 = OKT_ACHSE[m]
        for a in (k1, k2):
            for b in (m1, m2):
                self._del(norm([refs6[p], refs6[q], refs6[a], refs6[b]]))
        self.simp.append([refs6[i] for i in (p, q, k1, k2, m2)]); self.simp_typ.append('flip')
        self.simp.append([refs6[i] for i in (p, q, k1, k2, m1)]); self.simp_typ.append('flip')
        for a in (p, q):
            for b in (m1, m2):
                self._add(norm([refs6[k1], refs6[k2], refs6[a], refs6[b]]))
        okt['diag_kl'] = K

    def eins_vier(self, key, dh=0.1):
        P = np.array([self.pos(r) for r in key])
        vs = self.neue_ecke(P[:, :3].mean(0), P[:, 3].mean() + dh, -1, -1, 0)
        self.simp.append(list(key) + [(vs, (0, 0, 0))]); self.simp_typ.append('1-4')
        self._del(key)
        for i in range(4):
            self._add(norm([(vs, (0, 0, 0)) if j == i else key[j] for j in range(4)]))
        return vs

    def vier_eins(self, vs):
        keys = list(self.stern[vs])
        assert len(keys) == 4
        pts = {}
        for key in keys:
            sv = [s for (w, s) in key if w == vs][0]
            for (w, s) in key:
                if w != vs:
                    pts[(w, (s[0] - sv[0], s[1] - sv[1], s[2] - sv[2]))] = 1
        assert len(pts) == 4, pts
        refs4 = list(pts)
        self.simp.append(refs4 + [(vs, (0, 0, 0))]); self.simp_typ.append('4-1')
        for key in keys:
            self._del(key)
        self._add(norm(refs4))

    def takt(self, variante):
        neu = []
        if variante == 'B':
            for refs in self.tet2:
                key = norm([(self.cur[o], s) for (o, s) in refs])
                neu.append(self.eins_vier(key))
        for K in range(4):
            for o in self.klasse_orig[K]:
                self.zelt(self.cur[o], 1.0)
            if variante in ('C2', 'C3'):
                for okt in self.okt:
                    ok = (K in okt['paar']) if variante == 'C2' else (K != okt['M'])
                    if ok and okt['diag_kl'] != K:
                        self.flip(okt, K)
        for vs in neu:
            self.vier_eins(vs)


# ================================================================================================= Geometrie
def winkel(X):
    """Innere Diederwinkel (S,10) eines 4-Simplex an den Dreiecken gegenueber PAARE5; komplexer Schritt erlaubt."""
    E = X[:, 1:, :] - X[:, :1, :]
    F = np.swapaxes(np.linalg.inv(E), 1, 2)
    Fa = np.concatenate([-F.sum(1, keepdims=True), F], 1)
    G = np.einsum('spi,sqi->spq', Fa, Fa)
    out = [np.arccos(-G[:, p, q] / np.sqrt(G[:, p, p] * G[:, q, q])) for (p, q) in PAARE5]
    return np.stack(out, 1)


def geometrie(X, h=1e-20):
    S = X.shape[0]
    th = winkel(X).real
    J = np.zeros((S, 10, 20))
    for c in range(20):
        Xc = X.astype(complex)
        Xc[:, c // 4, c % 4] += 1j * h
        J[:, :, c] = winkel(Xc).imag / h
    C = np.zeros((S, 10, 20)); l = np.zeros((S, 10))
    for i, (a, b) in enumerate(PAARE5):
        d = X[:, b, :] - X[:, a, :]
        ll = np.linalg.norm(d, axis=1); l[:, i] = ll
        nrm = d / ll[:, None]
        C[:, i, 4 * b:4 * b + 4] = nrm
        C[:, i, 4 * a:4 * a + 4] = -nrm
    Ct = np.swapaxes(C, 1, 2)
    dth = J @ (Ct @ np.linalg.inv(C @ Ct))
    A = np.zeros((S, 10)); dA = np.zeros((S, 10, 10))
    for k, (e1, e2, e3) in enumerate(DREI_KANTEN):
        a, b, c = l[:, e1], l[:, e2], l[:, e3]
        Ak = 0.25 * np.sqrt((a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c))
        A[:, k] = Ak
        dA[:, k, e1] = a * (b * b + c * c - a * a) / (8 * Ak)
        dA[:, k, e2] = b * (a * a + c * c - b * b) / (8 * Ak)
        dA[:, k, e3] = c * (a * a + b * b - c * c) / (8 * Ak)
    M = np.swapaxes(dA, 1, 2) @ dth
    schl = float(np.abs(np.einsum('sk,ske->se', A, dth)).max() / (np.abs(A).max() * np.abs(dth).max()))
    sym = float(np.abs(M - np.swapaxes(M, 1, 2)).max() / np.abs(M).max())
    vol = np.linalg.det(X[:, 1:, :] - X[:, :1, :]) / 24.0
    vol_rel = np.abs(vol) / l.max(1) ** 4
    return {'th': th, 'A': A, 'M': M, 'l': l, 'schlaefli': schl, 'M_sym': sym, 'vol_rel': vol_rel}


def koord_aus_laengen(Ls):
    S = Ls.shape[0]
    l2 = Ls ** 2
    G = np.zeros((S, 4, 4))
    for i in range(1, 5):
        for j in range(1, 5):
            if i == j:
                G[:, i - 1, j - 1] = l2[:, PIDX[(0, i)]]
            else:
                a, b = min(i, j), max(i, j)
                G[:, i - 1, j - 1] = 0.5 * (l2[:, PIDX[(0, i)]] + l2[:, PIDX[(0, j)]] - l2[:, PIDX[(a, b)]])
    X = np.zeros((S, 5, 4))
    X[:, 1:, :] = np.linalg.cholesky(G)
    return X


def flaechen(la, lb, lc):
    A = 0.25 * np.sqrt((la + lb + lc) * (-la + lb + lc) * (la - lb + lc) * (la + lb - lc))
    dA = np.stack([la * (lb * lb + lc * lc - la * la), lb * (la * la + lc * lc - lb * lb),
                   lc * (la * la + lb * lb - lc * lc)], 1) / (8 * A[:, None])
    return A, dA


# ================================================================================================= Schicht (4D-Komplex)
class Schicht:
    def __init__(self, nz, sig0, sigT, simp=None):
        self.nz = nz
        simp = nz.simp if simp is None else simp
        self.simp = simp
        S = len(simp)
        self.ekey, self.tkey = {}, {}
        self.egid = np.zeros((S, 10), int); self.tgid = np.zeros((S, 10), int)
        for s, refs in enumerate(simp):
            for i, (a, b) in enumerate(PAARE5):
                k = kkey(refs[a], refs[b])
                self.egid[s, i] = self.ekey.setdefault(k, len(self.ekey))
            for i, tr in enumerate(DREI5):
                k = norm([refs[x] for x in tr])
                self.tgid[s, i] = self.tkey.setdefault(k, len(self.tkey))
        self.NE, self.NT = len(self.ekey), len(self.tkey)
        self.Xs = np.array([[nz.pos(r) for r in refs] for refs in simp])
        e0, eT, t0, tT, v0, vT = set(), set(), set(), set(), set(), set()
        for sig, es, ts, vs in ((sig0, e0, t0, v0), (sigT, eT, tT, vT)):
            for key in sig:
                for (a, b) in PAARE4:
                    k = kkey(key[a], key[b])
                    if k in self.ekey:
                        es.add(self.ekey[k])
                for tr in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)):
                    k = norm([key[x] for x in tr])
                    if k in self.tkey:
                        ts.add(self.tkey[k])
                for v, s in key:
                    vs.add(v)
        self.e0, self.eT = sorted(e0), sorted(eT)
        self.bd = sorted(e0 | eT)
        self.inn = sorted(set(range(self.NE)) - e0 - eT)
        self.tri_bd = np.zeros(self.NT, bool)
        self.tri_bd[sorted(t0 | tT)] = True
        alle_v = set(v for refs in simp for v, s in refs)
        self.v0, self.vT = sorted(v0 & alle_v), sorted(vT & alle_v)
        self.v_inn = sorted(alle_v - v0 - vT)
        self.ueberlapp = len(e0 & eT)
        # Dreieckskanten (globale Ids)
        self.tri_edges = np.zeros((self.NT, 3), int)
        for s in range(S):
            for k in range(10):
                self.tri_edges[self.tgid[s, k]] = self.egid[s, DREI_KANTEN[k]]
        # flache Kantenvektoren
        self.evec = np.zeros((self.NE, 4)); self.emid = np.zeros((self.NE, 4))
        for k, i in self.ekey.items():
            v1, v2 = k[0], k[1]
            p1 = nz.pos((v1, (0, 0, 0))); p2 = nz.pos((v2, (k[2], k[3], k[4])))
            self.evec[i] = p2 - p1; self.emid[i] = 0.5 * (p1 + p2)
        self.lflat = np.linalg.norm(self.evec, axis=1)

    def hesse(self, geo):
        S = len(self.simp)
        rows = np.repeat(self.egid, 10, axis=1).ravel()
        cols = np.tile(self.egid, (1, 10)).ravel()
        H = np.bincount(rows * self.NE + cols, weights=(-geo['M']).reshape(S, 100).ravel(),
                        minlength=self.NE * self.NE).reshape(self.NE, self.NE)
        return H

    def eich(self, verts, edges):
        """Laengenaenderung der Kanten 'edges' unter 4D-Verschiebung der Ecken 'verts' (flacher Hintergrund)."""
        col = {v: j for j, v in enumerate(verts)}
        inv = {i: k for k, i in self.ekey.items()}
        Y = np.zeros((len(edges), 4 * len(verts)))
        for r, e in enumerate(edges):
            k = inv[e]
            u = self.evec[e] / self.lflat[e]
            if k[0] in col:
                Y[r, 4 * col[k[0]]:4 * col[k[0]] + 4] -= u
            if k[1] in col:
                Y[r, 4 * col[k[1]]:4 * col[k[1]] + 4] += u
        return Y

    def defizite(self, th):
        Th = np.bincount(self.tgid.ravel(), th.ravel(), minlength=self.NT)
        return np.where(self.tri_bd, np.pi - Th, 2 * np.pi - Th)

    def bewerte(self, l):
        X = koord_aus_laengen(l[self.egid])
        th = winkel(X).real
        phi = self.defizite(th)
        A, dA = flaechen(l[self.tri_edges[:, 0]], l[self.tri_edges[:, 1]], l[self.tri_edges[:, 2]])
        Sw = float((A * phi).sum())
        g = np.bincount(self.tri_edges.ravel(), (dA * phi[:, None]).ravel(), minlength=self.NE)
        return Sw, g, X, phi


def rang(s, tol):
    if len(s) == 0 or s[0] == 0:
        return 0, None
    r = int((s > tol * s[0]).sum())
    gap = float(s[r - 1] / s[r]) if 0 < r < len(s) else None
    return r, gap


def analyse_takt(nz, sig0, sigT, tol_null=1e-10, tol_rang=1e-9):
    t0 = time.time()
    sch = Schicht(nz, sig0, sigT)
    geo = geometrie(sch.Xs)
    out = {'S': len(sch.simp), 'NE': sch.NE, 'NT': sch.NT, 'E0': len(sch.e0), 'ET': len(sch.eT),
           'V0': len(sch.v0), 'VT': len(sch.vT), 'n_innen': len(sch.v_inn), 'n_bulk': len(sch.inn),
           'ueberlapp_kanten': sch.ueberlapp,
           'typen': {t: nz.simp_typ.count(t) for t in sorted(set(nz.simp_typ))},
           'schlaefli': geo['schlaefli'], 'M_sym': geo['M_sym'], 'vol_rel_min': float(geo['vol_rel'].min())}
    phi = sch.defizite(geo['th'])
    out['innen_fehlwinkel_max'] = float(np.abs(phi[~sch.tri_bd]).max()) if (~sch.tri_bd).any() else 0.0
    out['rand_psi_min_max'] = [float(phi[sch.tri_bd].min()), float(phi[sch.tri_bd].max())]
    H = sch.hesse(geo)
    Hn = float(np.abs(H).max())
    inn, e0, eT = sch.inn, sch.e0, sch.eT
    Hii = H[np.ix_(inn, inn)]
    w, U = np.linalg.eigh(Hii)
    wmax = float(np.abs(w).max())
    nz_ = np.abs(w) > tol_null * wmax
    out['bulk_null'] = int((~nz_).sum())
    aw = np.sort(np.abs(w)) / wmax
    out['bulk_eig_klein'] = [float(x) for x in aw[:min(len(aw), out['bulk_null'] + 3)]]
    # Eichung der inneren Ecken
    if sch.v_inn:
        Yi = sch.eich(sch.v_inn, inn)
        out['eich_innen_rang'] = int(np.linalg.matrix_rank(Yi))
        HY = H[:, inn] @ Yi
        out['H_Y_innen_rel'] = float(np.abs(HY).max() / (Hn * np.abs(Yi).max()))
    else:
        Yi = np.zeros((len(inn), 0))
        out['eich_innen_rang'] = 0
        out['H_Y_innen_rel'] = 0.0
    null = U[:, ~nz_]
    n_x, kopp = 0, 0.0
    if null.shape[1] > 0:
        if Yi.shape[1] > 0:
            Uy, sy, _ = np.linalg.svd(Yi, full_matrices=False)
            Qy = Uy[:, sy > 1e-10 * sy.max()]
            R = null - Qy @ (Qy.T @ null)
        else:
            R = null
        Ur, sr, _ = np.linalg.svd(R, full_matrices=False)
        n_x = int((sr > 1e-6).sum())
        if n_x > 0:
            Z = Ur[:, :n_x]
            bd = e0 + eT
            kopp = float(np.abs(Z.T @ H[np.ix_(inn, bd)]).max() / Hn)
    out['n_x'] = n_x
    out['n_x_kopplung_rel'] = kopp
    Unz = U[:, nz_]
    Q = H[np.ix_(e0, eT)] - (H[np.ix_(e0, inn)] @ Unz) @ ((Unz.T @ H[np.ix_(inn, eT)]) / w[nz_][:, None])
    s = np.linalg.svd(Q, compute_uv=False)
    r, gap = rang(s, tol_rang)
    out['r'] = r
    out['r_luecke'] = gap
    out['sv_um_r'] = [float(x / s[0]) for x in s[max(0, r - 3):r + 3]]
    Y0 = sch.eich(sch.v0, e0); YT = sch.eich(sch.vT, eT)
    out['G0'] = int(np.linalg.matrix_rank(Y0)); out['GT'] = int(np.linalg.matrix_rank(YT))
    Qn = float(np.abs(Q).max())
    out['Omega_Y_T_rel'] = float(np.abs(Q @ YT).max() / (Qn * np.abs(YT).max()))
    out['Omega_Y_0_rel'] = float(np.abs(Y0.T @ Q).max() / (Qn * np.abs(Y0).max()))
    out['pre'] = len(e0) - r; out['post'] = len(eT) - r
    out['pre_nicht_eich'] = out['pre'] - out['G0']; out['post_nicht_eich'] = out['post'] - out['GT']
    out['t_analyse_s'] = time.time() - t0
    return out


def lauf_takt(variante, n, m):
    t0 = time.time()
    nz = Netz(n, 'klasse', variante)
    sig0 = set(nz.sigma)
    for _ in range(m):
        nz.takt(variante)
    sigT = set(nz.sigma)
    t_bau = time.time() - t0
    res = analyse_takt(nz, sig0, sigT)
    res.update({'variante': variante, 'n': n, 'm': m, 'V': nz.V0, 't_bau_s': t_bau,
                'E_sigma0': len({kkey(k[a], k[b]) for k in sig0 for (a, b) in PAARE4}),
                'E_sigmaT': len({kkey(k[a], k[b]) for k in sigT for (a, b) in PAARE4}),
                'tet_sigma0': len(sig0), 'tet_sigmaT': len(sigT), 't_gesamt_s': time.time() - t0})
    return res


# ================================================================================================= Kontrolle reines C
def lauf_kc(seed=7, nversuch=200):
    nz = Netz(2, 'klasse', 'C2')
    rng = np.random.default_rng(seed)
    V = nz.V0
    summen, anteile = [], []
    for _ in range(nversuch):
        h = rng.uniform(0, 1, V)
        tau = rng.normal(size=3)

        def hoehe(ref):
            v, s = ref
            return h[v] + tau @ (nz.X[v] + nz.n * np.array(s, float))
        dif = []
        for okt in nz.okt:
            r6 = okt['refs']
            mx = 0.5 * (hoehe(r6[0]) + hoehe(r6[4]))
            mz = 0.5 * (hoehe(r6[2]) + hoehe(r6[3]))
            dif.append(mx - mz)
        dif = np.array(dif)
        summen.append(float(dif.sum()))
        anteile.append(float((dif > 0).mean()))
    # Rueckwechsel: ein Oktaeder, z-Enden 0, y-Enden 0,1, x-Enden 0,3 (Wechsel z -> x vorwaerts)
    P = np.zeros((6, 4))
    for i, o in enumerate(OKT_OFF):
        P[i, :3] = o / 2.0
    P[[2, 3], 3] = 0.0; P[[1, 5], 3] = 0.1; P[[0, 4], 3] = 0.3
    s1 = P[[2, 3, 0, 4, 5]][None]          # alle ohne -y (Index 1): (-z, +z, -x, +x, +y)
    s2 = P[[2, 3, 0, 4, 1]][None]          # alle ohne +y
    th1 = winkel(s1).real[0]
    th_rueck = float(th1[PIDX[(0, 1)]])    # Dreieck (-x, +x, +y) liegt gegenueber dem Paar (-z, +z) = lokal (0, 1)
    vol = [float(np.linalg.det(x[0, 1:] - x[0, :1]) / 24) for x in (s1, s2)]
    return {'summenregel_max_abs': float(np.abs(summen).max()), 'anteil_x_ueber_z_max': float(max(anteile)),
            'anteil_x_ueber_z_min': float(min(anteile)), 'n_versuche': nversuch, 'n_okt': len(nz.okt),
            'rueckwechsel_theta': th_rueck, 'rueckwechsel_noetig': float(2 * np.pi - th_rueck),
            'rueckwechsel_noetig_gt_pi': bool(2 * np.pi - th_rueck > np.pi), 'flip_volumen': vol}


# ================================================================================================= Kommutator
def welle_laengen(sch, eps, La, xA):
    Lc = La / np.sqrt(2.0)
    k = 2 * np.pi / Lc
    c = np.cos(k * (sch.emid[:, 0] - xA[0]))
    E = sch.evec
    q = E[:, 0] ** 2 + E[:, 1] ** 2 * (1 + eps * c) + E[:, 2] ** 2 * (1 - eps * c) + E[:, 3] ** 2
    w = (E[:, 1] ** 2 - E[:, 2] ** 2) * c / (2 * sch.lflat)
    return np.sqrt(q), w


def flach_laengen(sch, eps, La):
    Lc = La / np.sqrt(2.0)
    kv = 2 * np.pi / Lc * np.array([1.0, 0.3, 0.2])

    def xi(P):
        ph = P[:, :3] @ kv
        return np.stack([0.7 * np.sin(ph), 0.4 * np.cos(ph), 0.3 * np.sin(2 * ph), 0.5 * np.cos(ph + 0.4 * P[:, 3])], 1)
    p1 = sch.emid - 0.5 * sch.evec
    p2 = sch.emid + 0.5 * sch.evec
    return np.linalg.norm(p2 + eps * xi(p2) - p1 - eps * xi(p1), axis=1)


def loese(sch, lbd, maxit=40):
    l = sch.lflat.copy()
    l[sch.bd] = lbd[sch.bd]
    inn = sch.inn
    res_verlauf = []
    for it in range(maxit):
        Sw, g, X, phi = sch.bewerte(l)
        gi = g[inn]
        res = float(np.abs(gi).max())
        res_verlauf.append(res)
        if res < 1e-15:
            break
        geo = geometrie(X)
        H = sch.hesse(geo)
        dl = np.linalg.solve(H[np.ix_(inn, inn)], -gi)
        l[inn] += dl
    Sw, g, X, phi = sch.bewerte(l)
    return l, Sw, g, float(np.abs(g[inn]).max()), len(res_verlauf), phi


def etikett(nz, sch, e):
    inv = {i: k for k, i in sch.ekey.items()}
    k = inv[e]
    a = (nz.orig[k[0]], nz.gen[k[0]]); b = (nz.orig[k[1]], nz.gen[k[1]])
    d = (k[2], k[3], k[4])
    if a > b:
        a, b, d = b, a, (-d[0], -d[1], -d[2])
    return (a, b, d)


def lauf_kommutator(eps_liste, La_liste, eps_L=1e-3, La_eps=4.0, eps_flach=3e-2):
    n = 4
    basis = Netz(n, 'klasse', 'C2')     # geknickte Ausgangsflaeche (eben: H_ii singulaer, Rauchlauf r1)
    A = basis.idx[(n, n, n)]
    B = basis.idx[(n + 1, n + 1, n)]
    xA = basis.X[A]
    out = {'A': int(A), 'B': int(B), 'kl_A': basis.kl[A], 'kl_B': basis.kl[B]}
    for var, (NA, NB) in (('L', (0.3, 0.5)), ('G', (0.4, 0.4))):
        sch = {}
        for ordnung in ('AB', 'BA'):
            nz = copy.deepcopy(basis)
            sig0 = set(nz.sigma)
            if ordnung == 'AB':
                nz.zelt(A, NA); nz.zelt(B, NB)
            else:
                nz.zelt(B, NB); nz.zelt(A, NA)
            sch[ordnung] = (nz, Schicht(nz, sig0, set(nz.sigma)))
        (nzA, sA), (nzB, sB) = sch['AB'], sch['BA']
        labA = [etikett(nzA, sA, e) for e in sA.bd]
        labB = [etikett(nzB, sB, e) for e in sB.bd]
        assert sorted(labA) == sorted(labB)
        oA = np.argsort([str(x) for x in labA]); oB = np.argsort([str(x) for x in labB])
        bdA = np.array(sA.bd)[oA]; bdB = np.array(sB.bd)[oB]
        v = {'N_A': NA, 'N_B': NB, 'n_simp': [len(sA.simp), len(sB.simp)], 'n_inn': [len(sA.inn), len(sB.inn)],
             'n_bd': len(sA.bd), 'v_innen': [len(sA.v_inn), len(sB.v_inn)],
             'max_kantenverschiebung': int(max(abs(np.array(list(sA.ekey.keys()))[:, 2:]).max(),
                                               abs(np.array(list(sB.ekey.keys()))[:, 2:]).max()))}
        # flach: Defizite, Gradient
        for nm, s in (('AB', sA), ('BA', sB)):
            Sw, g, X, phi = s.bewerte(s.lflat)
            v['flach_innen_fehlwinkel_' + nm] = float(np.abs(phi[~s.tri_bd]).max()) if (~s.tri_bd).any() else 0.0
            v['flach_grad_innen_' + nm] = float(np.abs(g[s.inn]).max())
            geo = geometrie(s.Xs)
            v['vol_rel_min_' + nm] = float(geo['vol_rel'].min())
            v['schlaefli_' + nm] = geo['schlaefli']
        # linearer Koeffizient
        Q = {}
        for nm, s, bdo in (('AB', sA, bdA), ('BA', sB, bdB)):
            H = s.hesse(geometrie(s.Xs))
            ii = s.inn
            Hii = H[np.ix_(ii, ii)]
            v['Hii_cond_' + nm] = float(np.linalg.cond(Hii))
            Q[nm] = H[np.ix_(bdo, bdo)] - H[np.ix_(bdo, ii)] @ np.linalg.solve(Hii, H[np.ix_(ii, bdo)])
        dQ = Q['AB'] - Q['BA']
        lin = []
        for La in La_liste:
            _, w = welle_laengen(sA, 1.0, La, xA)
            lin.append({'La': La, 'D1': float(np.linalg.norm(dQ @ w[bdA])), 'w_norm': float(np.linalg.norm(w[bdA]))})
        v['linear'] = lin
        v['dQ_max_rel'] = float(np.abs(dQ).max() / np.abs(Q['AB']).max())
        # Flachprobe der linearen Form: Verschiebungsrichtungen
        Ybd = sA.eich(sorted(set(sA.v0) | set(sA.vT)), list(bdA))
        v['dQ_flach_rel'] = float(np.abs(dQ @ Ybd).max() / (np.abs(Q['AB']).max() * np.abs(Ybd).max()))

        def paar(eps, La, art):
            r = {}
            for nm, s, bdo in (('AB', sA, bdA), ('BA', sB, bdB)):
                if art == 'welle':
                    lbd, _ = welle_laengen(s, eps, La, xA)
                else:
                    lbd = flach_laengen(s, eps, La)
                l, Sw, g, res, nit, phi = loese(s, lbd)
                r[nm] = (Sw, g[bdo], res, nit)
            D = float(np.linalg.norm(r['AB'][1] - r['BA'][1]))
            return {'eps': eps, 'La': La, 'art': art, 'D': D, 'p_norm': float(np.linalg.norm(r['AB'][1])),
                    'D_rel': D / float(np.linalg.norm(r['AB'][1])), 'DS': abs(r['AB'][0] - r['BA'][0]),
                    'newton_rest': max(r['AB'][2], r['BA'][2]), 'newton_it': [r['AB'][3], r['BA'][3]]}
        v['eps_scan'] = [paar(e, La_eps, 'welle') for e in eps_liste]
        v['L_scan'] = [paar(eps_L, La, 'welle') for La in La_liste]
        v['flach'] = paar(eps_flach, La_eps, 'flach')
        v['null'] = paar(0.0, La_eps, 'welle')
        out[var] = v
    return out


# ================================================================================================= main
def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['kc', 'takt', 'kommutator'])
    ap.add_argument('--variante', default='TT,B,C2,C3')
    ap.add_argument('--n', type=int, default=2)
    ap.add_argument('--m', default='1')
    ap.add_argument('--eps', default='1e-3,3e-3,1e-2,3e-2')
    ap.add_argument('--La', default='4,8,16,32')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__))}
    res = {'info': info}
    if a.modus == 'kc':
        res['kc'] = lauf_kc()
    elif a.modus == 'takt':
        res['faelle'] = []
        for var in a.variante.split(','):
            for m in [int(x) for x in a.m.split(',')]:
                r = lauf_takt(var, a.n, m)
                res['faelle'].append(r)
                print('takt %s n=%d m=%d fertig nach %.1f s (rss %.0f MB)' % (var, a.n, m, time.time() - t0,
                      resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0), flush=True)
    else:
        res['ko'] = lauf_kommutator([float(x) for x in a.eps.split(',')], [float(x) for x in a.La.split(',')])
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
