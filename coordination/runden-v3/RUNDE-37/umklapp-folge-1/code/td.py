#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TAKT-DYNAMIK-1 (Runde 47, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Eine stehende TT-Mode laeuft durch ein periodisches Tetraedernetz (Glas N = 128 aus TT-GLAS-1, V_D als 2 x 2 x 2 aus
TAKT-UMKLAPP-1). Lineares Hamilton-Netz wie tg.py (EINE-WELT-LOCH-1, R1) im Kasten (Bloch-k = 0):
  H = 1/2 y^T A_red y + 1/2 x^T B_red x,  a = S x (Kantenwerte delta l / l), S = Komplement von Bild[M, c].
Integrator Stoermer-Verlet (Kick-Drift-Kick), fester Zeitschritt. Drei Arme:
  a: feste Zerlegung; b: Delaunay-gesteuerte 2-3/3-2-Zuege, sobald eine Flaeche im gedehnten Netz l = l0 (1 + a)
     die Delaunay-Bedingung verletzt (Doppelpyramide intrinsisch eingebettet, Ereigniszeit per Bisektion);
  c: gleich viele zufaellige zulaessige Zuege gleicher Typen zu denselben Zeiten (feste Saat).
Lesart H (PLAN): Operatoren auf den ungedehnten Lagen (Hintergrund) mit der jeweils aktuellen Zerlegung.
Abbildung ueber einen Zug: Lesart R (Laengen und Raten stetig, neue Kante linearisiert aus der flachen Einbettung der
Doppelpyramide, wegfallende Kante gestrichen, dann orthogonale Projektion auf die neue Zwangsflaeche); Nebenarm
Lesart P (Impulse: 2-3 Null-Fortsetzung, 3-2 zurueckgezogen mit J^T).
Unveraendert importiert: tg.py, tg_auswertung.py, tp.py (TT-GLAS-1), uk.py (UMKLAPP-1), tu.py (TAKT-UMKLAPP-1),
ew.py, mn.py.
"""
import argparse, json, os, sys, time, hashlib, platform, resource, glob
import numpy as np
import scipy
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import uk  # noqa: E402
import tu  # noqa: E402

H_CS = 1e-20
SAAT_ZUF = 4543
TAU_REL = 1e-12            # wachsend: omega^2 < -TAU_REL * max|omega^2| (wie tg.TAU_REL)
NULL_REL = 1e-9            # Nullmoden: |omega^2| <= NULL_REL * max|omega^2|
VMIN_B = 1e-10             # Arm b: neue Tetraeder im Hintergrund mit Volumen > VMIN_B * mittleres Volumen
BISEKT = 60                # Bisektionsschritte (Intervall dt * 2^-60)
MIT_EINS = True            # Bloch-k = 0: gleichmaessige Streckung 1_E zusaetzlich entfernt (PLAN), sonst A_red indefinit
PT = np.full((4, 4), -1, int)
for _p, (_i, _j, _, _) in enumerate(tg.PAARE):
    PT[_i, _j] = PT[_j, _i] = _p
SYM6 = []
for (_i, _j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
    _m = np.zeros((3, 3))
    _m[_i, _j] = _m[_j, _i] = 1.0
    SYM6.append(_m)
SYM6 = np.array(SYM6)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ------------------------------------------------------------------------------------------------ Geometrie aus Laengen
def bipyr(L9):
    """Doppelpyramide (Flaeche a b c, Spitzen d oben, e unten) aus 9 Laengen (ab, bc, ca, ad, bd, cd, ae, be, ce).
    Rueckgabe Koordinaten a, b, c, d, e (je (..., 3)); komplexer Schritt erlaubt."""
    lab, lbc, lca, lad, lbd, lcd, lae, lbe, lce = [L9[..., q] for q in range(9)]
    cx = (lab ** 2 + lca ** 2 - lbc ** 2) / (2 * lab)
    cy = np.sqrt(lca ** 2 - cx ** 2)
    z0 = 0 * lab

    def spitze(la, lb, lc, sg):
        x = (lab ** 2 + la ** 2 - lb ** 2) / (2 * lab)
        y = (la ** 2 - lc ** 2 + cx ** 2 + cy ** 2 - 2 * x * cx) / (2 * cy)
        z = sg * np.sqrt(la ** 2 - x ** 2 - y ** 2)
        return np.stack([x, y, z], -1)
    A = np.stack([z0, z0, z0], -1)
    B = np.stack([lab, z0, z0], -1)
    C = np.stack([cx, cy, z0], -1)
    return A, B, C, spitze(lad, lbd, lcd, 1.0), spitze(lae, lbe, lce, -1.0)


def mu_bipyr(L9):
    """mu = (|e - C|^2 - R^2) / R^2 bezueglich der Umkugel von (a, b, c, d), wie uk.raender."""
    A, B, C, D, E = bipyr(L9)
    lab = B[..., 0]
    Cx = lab / 2
    Cy = (C[..., 0] ** 2 + C[..., 1] ** 2 - 2 * C[..., 0] * Cx) / (2 * C[..., 1])
    Cz = ((D ** 2).sum(-1) - 2 * D[..., 0] * Cx - 2 * D[..., 1] * Cy) / (2 * D[..., 2])
    R2 = Cx ** 2 + Cy ** 2 + Cz ** 2
    return ((E[..., 0] - Cx) ** 2 + (E[..., 1] - Cy) ** 2 + (E[..., 2] - Cz) ** 2 - R2) / R2


def l_de_flach(L9):
    A, B, C, D, E = bipyr(L9)
    return np.sqrt(((D - E) ** 2).sum(-1))


def vol_bipyr(L9):
    A, B, C, D, E = bipyr(L9)
    return np.array([uk.vol6(A, B, D, E), uk.vol6(B, C, D, E), uk.vol6(C, A, D, E)]) / 6.0


def jrow_flach(L9):
    """a_de = sum_q j_q a_q: Linearisierung der flachen Laenge d-e nach den 9 Kanten (komplexer Schritt)."""
    l0 = float(l_de_flach(L9))
    g = np.zeros(9)
    for q in range(9):
        Lc = L9.astype(complex)
        Lc[q] += 1j * H_CS
        g[q] = np.imag(l_de_flach(Lc)) / H_CS
    return g * L9 / l0, l0


def tet_X_aus_laengen(L6):
    """Ein Tetraeder (n, 6) Laengen in tg.PAARE-Reihenfolge (01, 02, 03, 12, 13, 23) -> Koordinaten (n, 4, 3)."""
    l01, l02, l03, l12, l13, l23 = [L6[:, q] for q in range(6)]
    x2 = (l01 ** 2 + l02 ** 2 - l12 ** 2) / (2 * l01)
    y2 = np.sqrt(np.maximum(l02 ** 2 - x2 ** 2, 0.0))
    x3 = (l01 ** 2 + l03 ** 2 - l13 ** 2) / (2 * l01)
    y3 = (l03 ** 2 - l23 ** 2 + x2 ** 2 + y2 ** 2 - 2 * x3 * x2) / (2 * y2)
    z3 = np.sqrt(np.maximum(l03 ** 2 - x3 ** 2 - y3 ** 2, 0.0))
    n = len(L6)
    X = np.zeros((n, 4, 3))
    X[:, 1, 0] = l01
    X[:, 2, 0], X[:, 2, 1] = x2, y2
    X[:, 3, 0], X[:, 3, 1], X[:, 3, 2] = x3, y3, z3
    return X


def hodge_teile(X):
    """Wie tu.hodge je Tetraeder: A*_e,t (n, 6) und Abstaende Flaechenumkreismitte -> Umkugelmitte hf (n, 4)."""
    ct = tu.umkreis_tet(X)
    Ast = np.zeros((len(X), 6))
    for p, (i, j, k, l) in enumerate(tg.PAARE):
        Xi, Xj, Xk, Xl = X[:, i], X[:, j], X[:, k], X[:, l]
        m = 0.5 * (Xi + Xj)
        e = tu.einheit(Xj - Xi)
        hs, hh = [], []
        for Xo, Xa in ((Xk, Xl), (Xl, Xk)):
            u = (Xo - Xi) - ((Xo - Xi) * e).sum(-1)[:, None] * e
            u = tu.einheit(u)
            cf = tu.umkreis_drei(Xi, Xj, Xo)
            hs.append(((cf - m) * u).sum(-1))
            nrm = np.cross(Xj - Xi, Xo - Xi)
            nrm = tu.einheit(nrm * np.sign((nrm * (Xa - Xi)).sum(-1))[:, None])
            hh.append(((ct - cf) * nrm).sum(-1))
        Ast[:, p] = 0.5 * (hs[0] * hh[0] + hs[1] * hh[1])
    hf = np.zeros((len(X), 4))
    af = np.zeros((len(X), 4))
    for i in range(4):
        a_, b_, c_ = [X[:, q] for q in uk.FL[i]]
        cf = tu.umkreis_drei(a_, b_, c_)
        nrm = np.cross(b_ - a_, c_ - a_)
        af[:, i] = 0.5 * np.linalg.norm(nrm, axis=1)
        nrm = tu.einheit(nrm * np.sign((nrm * (X[:, i] - a_)).sum(-1))[:, None])
        hf[:, i] = ((ct - cf) * nrm).sum(-1)
    return Ast, hf, af


# ------------------------------------------------------------------------------------------------ Netze
def netz_bauen(name):
    if name.startswith('glas-'):
        _, nN, ns = name.split('-')
        LV, pos, G, O, pr = tg.zufallsnetz(int(nN[1:]), int(ns[1:]))
        return LV, pos, G, O, {'N': int(nN[1:]), 'saat': int(ns[1:]), 'pruefung': pr}
    if name == 'VD2':
        LV, pos, G, O, _ = tg.netz_V()
        G, O, st = tu.reparatur(LV, pos, G, O)
        LV2, pos2, G2, O2, _ = tu.superzelle(LV, pos, G, O, 2)
        return LV2, pos2, G2, O2, {'N': int(len(pos2)), 'saat': 0, 'reparatur_je_zelle': st}
    raise ValueError(name)


def polarisation(k):
    kh = k / np.linalg.norm(k)
    u = tu.einheit(np.cross(kh, [0.3, 0.5, 0.7]))
    v = np.cross(kh, u)
    return (np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)


class Netz:
    """Operatoren einer Zerlegung auf den Hintergrundlagen bei Bloch-k = 0, reduziert auf die Zwangsflaeche."""

    def __init__(self, LV, pos, G, O, k1, hp, hx, eigen=True):
        t0 = time.time()
        self.LV, self.pos, self.G, self.O = LV, pos, G, O
        nV = len(pos)
        self.nV = nV
        mod = tg.modell(LV, pos, G, O, {})
        self.mod = mod
        E = mod['E']
        self.E = E
        ed = np.rint(mod['Tedge'] @ np.linalg.inv(LV)).astype(np.int64)
        self.keys = (((mod['es'].astype(np.int64) * nV + mod['es2']) * 16 + ed[:, 0] + 8) * 16 + ed[:, 1] + 8) * 16 + ed[:, 2] + 8
        assert np.all(np.diff(self.keys) > 0)
        self.l0 = mod['l']
        B, A, M, c = tg.ops(mod, np.zeros(3))
        self.B = B.real.tocsr()
        self.A = A.real.tocsr()
        M = np.ascontiguousarray(M.real[:, 3:])
        c = np.ascontiguousarray(c.real[:, 1:])
        self.mit_eins = MIT_EINS
        X = np.concatenate([M, c, np.ones((E, 1))], 1) if MIT_EINS else np.concatenate([M, c], 1)
        nX = X.shape[1]
        Q, R = np.linalg.qr(X, mode='complete')
        d = np.abs(np.diag(R[:nX]))
        self.rang_rel = float(d.min() / d.max())
        if self.rang_rel < 1e-9:
            U, s_, _ = np.linalg.svd(X)
            r = int((s_ > 1e-9 * s_.max()).sum())
            S = U[:, r:]
            Q1 = U[:, :r]
            self.weg = 'svd'
        else:
            S = Q[:, nX:]
            Q1 = Q[:, :M.shape[1]]
            self.weg = 'qr'
        self.S = np.ascontiguousarray(S)
        self.m = S.shape[1]
        Ar = S.T @ (self.A @ S)
        Br = S.T @ (self.B @ S)
        self.Ar = 0.5 * (Ar + Ar.T)
        self.Br = 0.5 * (Br + Br.T)
        self.lu = sla.lu_factor(self.Ar)
        eA = np.linalg.eigvalsh(self.Ar)
        self.n_A_neg = int((eA < -1e-12 * np.abs(eA).max()).sum())
        self.A_min_rel = float(eA.min() / np.abs(eA).max())
        try:
            self.L = np.linalg.cholesky(self.Ar)
            self.A_pd = True
        except np.linalg.LinAlgError:
            self.L = None
            self.A_pd = False
        # Gegenprobe Zwangsflaeche: S^T M = 0, S^T c = 0
        self.kontr_S = float(max(np.abs(S.T @ M).max() / np.abs(M).max(), np.abs(S.T @ c).max() / np.abs(c).max()))
        # Flaechen und die 9 Kanten je Doppelpyramide
        fl = uk.flaechen(G, O)
        self.fl = fl
        t1, i1, t2, i2 = fl['t1'], fl['i1'], fl['t2'], fl['i2']
        F = fl['F']
        loc1 = uk.FL[i1]
        ga = G[t1[:, None], loc1]
        G2 = G[t2]
        loc2 = np.argmax(G2[:, None, :] == ga[:, :, None], axis=2)
        assert np.all(G2[np.arange(F)[:, None], loc2] == ga)
        e = mod['eidx']
        a_, b_, c_ = loc1[:, 0], loc1[:, 1], loc1[:, 2]
        self.f9 = np.stack([e[t1, PT[a_, b_]], e[t1, PT[b_, c_]], e[t1, PT[c_, a_]],
                            e[t1, PT[a_, i1]], e[t1, PT[b_, i1]], e[t1, PT[c_, i1]],
                            e[t2, PT[loc2[:, 0], i2]], e[t2, PT[loc2[:, 1], i2]], e[t2, PT[loc2[:, 2], i2]]], 1)
        self.l9_0 = self.l0[self.f9]
        self.S9 = None
        self.fkeys = uk.flaechen_je_tet(G, O).reshape(-1, 12)
        # TT-Leser: a ~ sum_s x_s n^T SYM6_s n (cos, sin)(k1 . Kantenmitte) + M xi
        n = mod['n']
        Es = np.einsum('ei,sij,ej->es', n, SYM6, n)
        ph = mod['mitte'] @ k1
        Xf = np.concatenate([Es * np.cos(ph)[:, None], Es * np.sin(ph)[:, None]], 1)
        Z = Xf - Q1 @ (Q1.T @ Xf)
        Zp = np.linalg.pinv(Z)
        Cm = np.zeros((4, 12))
        for s in range(6):
            Cm[0, s] = np.sum(SYM6[s] * hp)
            Cm[1, s] = np.sum(SYM6[s] * hx)
            Cm[2, 6 + s] = np.sum(SYM6[s] * hp)
            Cm[3, 6 + s] = np.sum(SYM6[s] * hx)
        self.R4S = (Cm @ Zp) @ self.S
        self.vbar = float(uk.tet_vol(LV, pos, G, O).mean())
        self.eig = None
        if eigen:
            self.spektrum()
        self.t_bau = time.time() - t0

    def spektrum(self):
        if self.A_pd:
            Wm = self.L.T @ self.Br @ self.L
            w2 = np.linalg.eigvalsh(0.5 * (Wm + Wm.T))
            w2im = np.zeros_like(w2)
        else:
            wc = np.linalg.eigvals(self.Ar @ self.Br)
            o = np.argsort(wc.real)
            w2, w2im = wc.real[o], wc.imag[o]
        s = float(np.abs(w2 + 1j * w2im).max())
        tau = TAU_REL * s
        wachs = (w2 < -tau) | (np.abs(w2im) > tau)
        null = (~wachs) & (np.abs(w2) <= NULL_REL * s)
        self.eig = {'w2_max': float(w2.max()), 'n_wachsend': int(wachs.sum()), 'n_null': int(null.sum()),
                    'w2_min': float(w2.min()), 'w2im_max': float(np.abs(w2im).max()),
                    'w2_wachsend': [float(x) for x in w2[wachs][:8]], 'A_pd': bool(self.A_pd)}
        return self.eig

    # ---------------------------------------------------------------- Zustand
    def energie(self, x, y):
        K = 0.5 * float(y @ (self.Ar @ y))
        V = 0.5 * float(x @ (self.Br @ x))
        return K + V, V, K

    def mu_alle(self, x):
        a9 = (self.S @ x)[self.f9]
        return mu_bipyr(self.l9_0 * (1.0 + a9))

    def mu_eine(self, j, x):
        a9 = self.S[self.f9[j]] @ x
        return float(mu_bipyr((self.l9_0[j] * (1.0 + a9))[None, :])[0])

    def tt(self, x):
        return self.R4S @ x

    def idx_von_keys(self, keys):
        i = np.searchsorted(self.keys, keys)
        i = np.minimum(i, self.E - 1)
        ok = self.keys[i] == keys
        return i, ok


def kdk(N, x, y, tau, Bx=None):
    if Bx is None:
        Bx = N.Br @ x
    y = y - 0.5 * tau * Bx
    x = x + tau * (N.Ar @ y)
    Bx = N.Br @ x
    y = y - 0.5 * tau * Bx
    return x, y, Bx


# ------------------------------------------------------------------------------------------------ Zuege
def flaechen_ecken(N, j):
    """(Ecke, Versatz) von a, b, c, d, e der Flaeche j im Rahmen von t1."""
    fl = N.fl
    t1, i1, t2, i2, sh = fl['t1'][j], fl['i1'][j], fl['t2'][j], fl['i2'][j], fl['sh'][j]
    abc = [(int(N.G[t1, q]), N.O[t1, q].copy()) for q in uk.FL[i1]]
    d = (int(N.G[t1, i1]), N.O[t1, i1].copy())
    e = (int(N.G[t2, i2]), (N.O[t2, i2] + sh).copy())
    return abc, d, e


def kkey(N, p, q):
    return int(uk.kanten_schluessel(np.array([p[0]]), np.array([p[1]]), np.array([q[0]]), np.array([q[1]]), N.nV)[0])


def keys9(N, abc, d, e):
    a, b, c = abc
    return np.array([kkey(N, a, b), kkey(N, b, c), kkey(N, c, a), kkey(N, a, d), kkey(N, b, d), kkey(N, c, d),
                     kkey(N, a, e), kkey(N, b, e), kkey(N, c, e)], np.int64)


def region_tets(N, x, tets, l_extra=None):
    """Hodge-Teile der Tetraeder (Liste von 4 (Ecke, Versatz)) aus Hintergrund- und gedehnten Laengen."""
    a = N.S @ x
    out = {}
    for art in ('hg', 'gd'):
        L6 = np.zeros((len(tets), 6))
        for ti, tt in enumerate(tets):
            for p, (i, j, _, _) in enumerate(tg.PAARE):
                k = kkey(N, tt[i], tt[j])
                if l_extra is not None and k in l_extra:
                    L6[ti, p] = l_extra[k][art]
                else:
                    idx, ok = N.idx_von_keys(np.array([k]))
                    assert ok[0], 'Kante fehlt'
                    L6[ti, p] = N.l0[idx[0]] * (1.0 + (a[idx[0]] if art == 'gd' else 0.0))
        X = tet_X_aus_laengen(L6)
        Ast, hf, af = hodge_teile(X)
        out[art] = (L6, Ast, hf, af)
    return out


def td0_messung(N, x, alt, neu, typ, skala, l_extra):
    """Duales Mass der neuen bzw. wegfallenden Kante und Flaeche, Sprung von *1 und P (8 d0^T *1 d0) in der Region."""
    R_alt = region_tets(N, x, alt, l_extra)
    R_neu = region_tets(N, x, neu, l_extra)
    res = {}
    for art in ('hg', 'gd'):
        s1 = {}
        for sgn, tets, Rr in ((-1.0, alt, R_alt[art]), (1.0, neu, R_neu[art])):
            L6, Ast, hf, af = Rr
            for ti, tt in enumerate(tets):
                for p, (i, j, _, _) in enumerate(tg.PAARE):
                    k = (kkey(N, tt[i], tt[j]), )
                    s1.setdefault(k[0], [0.0, 0.0, L6[ti, p], (tt[i][0], tt[j][0])])
                    s1[k[0]][0 if sgn < 0 else 1] += Ast[ti, p]
        # Kante, die nur auf einer Seite vorkommt (neu bzw. wegfallend)
        einz = [k for k, v in s1.items() if (v[0] == 0.0) != (v[1] == 0.0)]
        ds1 = {k: (v[1] - v[0]) / v[2] for k, v in s1.items()}
        verts = sorted(set([q for v in s1.values() for q in v[3]]))
        vi = {v: i for i, v in enumerate(verts)}
        dP = np.zeros((len(verts), len(verts)))
        for k, v in s1.items():
            i_, j_ = vi[v[3][0]], vi[v[3][1]]
            w = 8.0 * ds1[k]
            dP[i_, i_] += w
            dP[j_, j_] += w
            dP[i_, j_] -= w
            dP[j_, i_] -= w
        stern1_einz = [(v[1] - v[0]) / v[2] for k, v in s1.items() if k in einz]
        # Flaeche: 2-3 -> wegfallende Flaeche abc (alt: t1, t2 teilen sie), 3-2 -> neue Flaeche (neu: beide teilen sie)
        L6, Ast, hf, af = (R_alt if typ == 23 else R_neu)[art]
        fi = 3 if typ == 23 else 0
        fl_l = hf[0, fi] + hf[1, fi]
        fl_a = af[0, fi]
        res[art] = {'stern1_einzel': [float(s) for s in stern1_einz],
                    'stern1_einzel_rel': float(max(abs(s) for s in stern1_einz) / skala['s1max']) if stern1_einz else None,
                    'stern2_flaeche': float(fl_l / fl_a), 'stern2_flaeche_rel': float(abs(fl_l / fl_a) / skala['s2max']),
                    'dstern1_max_rel': float(max(abs(v) for v in ds1.values()) / skala['s1max']),
                    'dP_max_rel': float(np.abs(dP).max() / skala['Pmax'])}
    return res


def skalen(N):
    h, s1, s2, Ast = tu.hodge(N.LV, N.pos, N.G, N.O, N.mod)
    L1diag = np.bincount(N.mod['es'], s1, N.nV) + np.bincount(N.mod['es2'], s1, N.nV)
    return {'s1max': float(np.abs(s1).max()), 's2max': float(np.abs(s2).max()), 'Pmax': float(8.0 * np.abs(L1diag).max()),
            'stern1_neg': h['stern1_n_neg'], 'stern2_neg': h['stern2_n_neg'], 'mu_min': h['mu_min'],
            'mu_n_verletzt': h['mu_n_verletzt']}


def zug_ausfuehren(N, j, typ, r, vmin):
    """2-3 (typ 23) an Flaeche j oder 3-2 (typ 32, Kante r der Flaeche) auf den Hintergrundlagen. Rueckgabe neue G, O
    und Beschreibung (alte und neue Tetraeder, neue/wegfallende Kante, 9 Kanten der flachen Fortsetzung) oder None."""
    LV, pos, G, O = N.LV, N.pos, N.G, N.O
    fl, geo = tu.flaechen_geo(LV, pos, G, O)
    abc, d, e = flaechen_ecken(N, j)
    t1, t2 = int(fl['t1'][j]), int(fl['t2'][j])
    if typ == 23:
        km = set(N.keys.tolist())
        if not tu.zug23_ok(LV, pos, G, O, geo, j, km, vmin):
            return None
        Gn, On = uk.zug23(LV, pos, G, O, fl, j)
        a, b, c = abc
        alt = [[a, b, c, d], [a, b, c, e]]
        neu = [[a, b, d, e], [b, c, d, e], [c, a, d, e]]
        k9 = keys9(N, abc, d, e)
        return Gn, On, {'alt': alt, 'neu': neu, 'kante_neu': kkey(N, d, e), 'kante_weg': None, 'k9': k9,
                        'tets_alt_idx': [t1, t2]}
    tdict = tu.tet_dict(G, O)
    info = tu.zug32_vorbereiten(LV, pos, G, O, fl, geo, j, r, tdict, vmin)
    if info is None:
        return None
    Gn, On = tu.zug32(LV, pos, G, O, info)
    p, q, s = tu.PQR[r]
    P, Q, Rr = abc[p], abc[q], abc[s]
    alt = [[abc[0], abc[1], abc[2], d], [abc[0], abc[1], abc[2], e], [P, Q, d, e]]
    neu = [[P, Rr, d, e], [Q, Rr, d, e]]
    # neue Flaeche R d e mit Spitzen P (oben) und Q (unten): 9 Kanten fuer die flache Laenge P-Q
    k9 = np.array([kkey(N, Rr, d), kkey(N, d, e), kkey(N, e, Rr), kkey(N, Rr, P), kkey(N, d, P), kkey(N, e, P),
                   kkey(N, Rr, Q), kkey(N, d, Q), kkey(N, e, Q)], np.int64)
    return Gn, On, {'alt': alt, 'neu': neu, 'kante_neu': None, 'kante_weg': kkey(N, P, Q), 'k9': k9,
                    'tets_alt_idx': list(info['t'])}


def abbilden(N, N2, x, y, besch, lesart):
    """Zustand (x, y) der Zerlegung N auf N2. Rueckgabe x2, y2 und Kennzahlen."""
    a = N.S @ x
    ad = N.S @ (N.Ar @ y)
    p = N.S @ y
    idx, ok = N2.idx_von_keys(N.keys)
    gem = ok
    a2 = np.zeros(N2.E)
    ad2 = np.zeros(N2.E)
    p2 = np.zeros(N2.E)
    a2[idx[gem]] = a[gem]
    ad2[idx[gem]] = ad[gem]
    p2[idx[gem]] = p[gem]
    k9 = besch['k9']
    info = {}
    if besch['kante_neu'] is not None:                      # 2-3: neue Kante aus der flachen Doppelpyramide
        i9, ok9 = N.idx_von_keys(k9)
        assert ok9.all()
        jr, lde = jrow_flach(N.l0[i9])
        inew, okn = N2.idx_von_keys(np.array([besch['kante_neu']]))
        assert okn[0]
        a2[inew[0]] = jr @ a[i9]
        ad2[inew[0]] = jr @ ad[i9]
        p2[inew[0]] = 0.0
        info['l_de_hg_flach'] = lde
        info['l_de_hg_netz'] = float(N2.l0[inew[0]])
        info['jrow'] = jr.tolist()
        assert np.sum(~gem) == 0
    else:                                                    # 3-2: wegfallende Kante gestrichen
        iw, okw = N.idx_von_keys(np.array([besch['kante_weg']]))
        assert okw[0] and np.sum(~gem) == 1 and not gem[iw[0]]
        i9n, ok9 = N2.idx_von_keys(k9)
        assert ok9.all()
        jr, lpq = jrow_flach(N2.l0[i9n])
        info['l_pq_hg_flach'] = lpq
        info['l_pq_hg_netz'] = float(N.l0[iw[0]])
        info['jrow'] = jr.tolist()
        info['delta_nichtflach'] = float(a[iw[0]] - jr @ a2[i9n])
        if lesart == 'P':
            p2[i9n] += jr * p[iw[0]]
    x2 = N2.S.T @ a2
    xd2 = N2.S.T @ ad2
    info['proj_rest_a'] = float(np.linalg.norm(a2 - N2.S @ x2) / max(np.linalg.norm(a2), 1e-300))
    info['proj_rest_ad'] = float(np.linalg.norm(ad2 - N2.S @ xd2) / max(np.linalg.norm(ad2), 1e-300))
    if lesart == 'R':
        y2 = sla.lu_solve(N2.lu, xd2)
    else:
        y2 = N2.S.T @ p2
        info['proj_rest_p'] = float(np.linalg.norm(p2 - N2.S @ y2) / max(np.linalg.norm(p2), 1e-300))
    return x2, y2, info


# ------------------------------------------------------------------------------------------------ Lauf
def tt_mode(N, A, k1):
    """Mode mit dem groessten Energieanteil der idealen TT-Welle (cos(k1 . m) n^T h+ n), normiert auf TT-Amplitude A."""
    w2, Qm = np.linalg.eigh(0.5 * (N.L.T @ N.Br @ N.L + (N.L.T @ N.Br @ N.L).T))
    n = N.mod['n']
    hp = N.hp
    aTT = np.einsum('ei,ij,ej->e', n, hp, n) * np.cos(N.mod['mitte'] @ k1)
    xTT = N.S.T @ aTT
    q = Qm.T @ sla.solve_triangular(N.L, xTT, lower=True)
    s = float(np.abs(w2).max())
    gut = w2 > NULL_REL * s
    en = np.where(gut, w2 * q ** 2, 0.0)
    anteil = en / en.sum()
    j = int(np.argmax(anteil))
    xm = N.L @ Qm[:, j]
    c = N.tt(xm)
    cn = float(np.linalg.norm(c))
    alpha = A / cn
    o = np.argsort(-anteil)[:6]
    return {'j': j, 'w2': float(w2[j]), 'omega': float(np.sqrt(w2[j])), 'anteil_TT_welle': float(anteil[j]),
            'naechste_anteile': [[int(i), float(w2[i]), float(anteil[i])] for i in o],
            'tt_leser_mode': (c * alpha).tolist(), 'alpha': float(alpha), 'tt_richtung': (c / cn).tolist(),
            'n_null': int((np.abs(w2) <= NULL_REL * s).sum()), 'w2_max': float(w2.max()),
            'w2_min_pos': float(w2[gut].min())}, alpha * xm, w2, Qm


def modal(N0, Qm, w2, x, y, j):
    u = sla.solve_triangular(N0.L, x, lower=True)
    q = Qm.T @ u
    qd = Qm.T @ (N0.L.T @ y)
    e = 0.5 * (qd ** 2 + w2 * q ** 2)
    s = float(np.abs(w2).max())
    null = np.abs(w2) <= NULL_REL * s
    H = float(e.sum())
    return {'H': H, 'anteil_TT': float(e[j] / H), 'anteil_null': float(e[null].sum() / H),
            'anteil_rest': float(1.0 - e[j] / H - e[null].sum() / H),
            'q_TT': float(q[j]), 'qd_TT': float(qd[j])}


def lauf(args):
    T0w = time.time()
    LV, pos, G0, O0, ninfo = netz_bauen(args.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = polarisation(k1)
    N0 = Netz(LV, pos, G0, O0, k1, hp, hx)
    N0.hp = hp
    if not N0.A_pd:
        raise RuntimeError('A_red nicht positiv definit: n_neg = %d, min_rel = %g, m = %d' % (N0.n_A_neg, N0.A_min_rel, N0.m))
    mode, xm, w2, Qm = tt_mode(N0, args.A, k1)
    om = mode['omega']
    Tper = 2 * np.pi / om
    wmax = np.sqrt(N0.eig['w2_max'])
    NT = int(np.ceil(Tper * wmax / args.h))
    dt = Tper / NT
    nges = NT * args.perioden
    ds = max(1, NT // args.proben)
    sk = skalen(N0)
    fkeys0 = set(map(tuple, N0.fkeys.tolist()))
    zfile = args.out + '.zustand.npz'
    if os.path.exists(zfile):
        z = np.load(zfile, allow_pickle=False)
        G, O = z['G'], z['O']
        meta = json.load(open(args.out + '.zustand.json'))
        x, y, n = z['x'], z['y'], int(z['n'])
        N = N0 if (len(G) == len(G0) and np.array_equal(G, G0) and np.array_equal(O, O0)) else Netz(LV, pos, G, O, k1, hp, hx)
        N.hp = hp
        proben, ereig, perioden, gesperrt = meta['proben'], meta['ereignisse'], meta['perioden'], set(tuple(g) for g in meta['gesperrt'])
        rng = np.random.default_rng([SAAT_ZUF, ninfo['N'], ninfo['saat'], int(round(-np.log10(args.A)))])
        if meta.get('rng_state'):
            rng.bit_generator.state = meta['rng_state']
        abschnitt = meta['abschnitt'] + 1
    else:
        N = N0
        x = np.zeros(N0.m)
        y = sla.lu_solve(N0.lu, om * xm)          # xdot(0) = omega * Mode, x(0) = 0
        n = 0
        proben, ereig, perioden = [], [], []
        gesperrt = set()
        rng = np.random.default_rng([SAAT_ZUF, ninfo['N'], ninfo['saat'], int(round(-np.log10(args.A)))])
        abschnitt = 0
    H0 = N0.energie(np.zeros(N0.m), sla.lu_solve(N0.lu, om * xm))[0]
    xref = float(np.linalg.norm(xm))
    abbruch = None
    plan_c = []
    if args.arm == 'c':
        eb = json.load(open(args.ereignisse))
        plan_c = [(ev['t'], ev['typ']) for ev in eb['ergebnis']['ereignisse'] if ev.get('ausgefuehrt')]
        n_c_done = sum(1 for ev in ereig if ev.get('ausgefuehrt'))
        plan_c = plan_c[n_c_done:] if n_c_done <= len(plan_c) else []
    vmin_c = uk.VMIN_REL * N0.vbar

    def probe(N, x, y, t, n):
        H, V, K = N.energie(x, y)
        mu = N.mu_alle(x)
        c4 = N.tt(x)
        proben.append([t, H, V, K] + [float(v) for v in c4] + [len([e for e in ereig if e.get('ausgefuehrt')]),
                                                               int((mu < 0).sum()), float(mu.min())])

    if n == 0 and not proben:
        probe(N, x, y, 0.0, 0)
    Bx = None
    fertig = False
    while n < nges:
        if time.time() - T0w > args.budget:
            break
        t_cur = n * dt
        rem = dt
        while rem > 0:
            x1, y1, Bx1 = kdk(N, x, y, rem, Bx)
            ev = None
            if args.arm == 'b':
                mu1 = N.mu_alle(x1)
                kand = np.nonzero(mu1 < 0)[0]
                kand = [j for j in kand if tuple(N.fkeys[N.fl['t1'][j] * 4 + N.fl['i1'][j]].tolist()) not in gesperrt]
                if kand:
                    v1 = N.Ar @ y
                    v2 = N.Ar @ (N.Br @ x)
                    best = None
                    for j in kand:
                        lo, hi = 0.0, rem
                        if N.mu_eine(j, x) < 0:
                            continue
                        for _ in range(BISEKT):
                            mid = 0.5 * (lo + hi)
                            if N.mu_eine(j, x + mid * v1 - 0.5 * mid * mid * v2) < 0:
                                hi = mid
                            else:
                                lo = mid
                        if best is None or hi < best[1]:
                            best = (j, hi)
                    if best is not None:
                        ev = best
            elif args.arm == 'c' and plan_c:
                if plan_c[0][0] <= t_cur + rem + 1e-15 * dt:
                    ev = (None, max(min(plan_c[0][0] - t_cur, rem), 0.0))
            if ev is None:
                x, y, Bx = x1, y1, Bx1
                rem = 0.0
                break
            j, tau = ev
            xe, ye, _ = kdk(N, x, y, tau, Bx)
            te = t_cur + tau
            H1, V1, K1 = N.energie(xe, ye)
            rec = {'t': te, 'n': n, 'tau_rel': tau / dt}
            if args.arm == 'b':
                abc, d, e = flaechen_ecken(N, j)
                L9 = N.l9_0[j] * (1.0 + N.S[N.f9[j]] @ xe)
                vv = vol_bipyr(L9)
                if np.all(vv > 0) or np.all(vv < 0):
                    typ, r = 23, None
                else:
                    typ, r = 32, tu.ungerade(vv)
                rec.update({'typ': typ, 'mu_rechts': N.mu_eine(j, xe), 'mu_hg': float(mu_bipyr(N.l9_0[j][None, :])[0]),
                            'flaeche': [int(abc[0][0]), int(abc[1][0]), int(abc[2][0])], 'spitzen': [d[0], e[0]]})
                aus = None if (typ == 32 and r is None) else zug_ausfuehren(N, j, typ, r, VMIN_B * N0.vbar)
            else:
                typ = plan_c.pop(0)[1]
                rec['typ'] = typ
                aus = None
                if typ == 23:
                    kd = uk.kandidaten(N.LV, N.pos, N.G, N.O, N.nV, vmin_c)
                    idx = np.nonzero(kd['ok'])[0]
                    if len(idx):
                        jz = int(idx[rng.integers(len(idx))])
                        aus = zug_ausfuehren(N, jz, 23, None, vmin_c)
                        if aus is not None:
                            rec['mu_hg'] = float(uk.raender(N.LV, N.pos, N.G, N.O, kd['fl'])[jz])
                else:
                    cands = tu.kandidaten32(N.LV, N.pos, N.G, N.O, vmin_c)
                    if cands:
                        info = cands[rng.integers(len(cands))]
                        Gn, On = tu.zug32(N.LV, N.pos, N.G, N.O, info)
                        # Beschreibung wie zug_ausfuehren (Ecken aus info)
                        P_ = (int(info['Gn'][0, 0]), info['On'][0, 0].copy())
                        Rr = (int(info['Gn'][0, 1]), info['On'][0, 1].copy())
                        d_ = (int(info['Gn'][0, 2]), info['On'][0, 2].copy())
                        e_ = (int(info['Gn'][0, 3]), info['On'][0, 3].copy())
                        Q_ = (int(info['Gn'][1, 0]), info['On'][1, 0].copy())
                        k9 = np.array([kkey(N, Rr, d_), kkey(N, d_, e_), kkey(N, e_, Rr), kkey(N, Rr, P_), kkey(N, d_, P_),
                                       kkey(N, e_, P_), kkey(N, Rr, Q_), kkey(N, d_, Q_), kkey(N, e_, Q_)], np.int64)
                        aus = (Gn, On, {'alt': [[P_, Q_, Rr, d_], [P_, Q_, Rr, e_], [P_, Q_, d_, e_]],
                                        'neu': [[P_, Rr, d_, e_], [Q_, Rr, d_, e_]], 'kante_neu': None,
                                        'kante_weg': kkey(N, P_, Q_), 'k9': k9, 'tets_alt_idx': list(info['t'])})
            if aus is None:
                rec['ausgefuehrt'] = False
                if args.arm == 'b':
                    gesperrt.add(tuple(N.fkeys[N.fl['t1'][j] * 4 + N.fl['i1'][j]].tolist()))
                ereig.append(rec)
                x, y, Bx = xe, ye, None
                rem -= tau
                t_cur = te
                continue
            Gn, On, besch = aus
            N2 = Netz(N.LV, N.pos, Gn, On, k1, hp, hx)
            N2.hp = hp
            # neue Kante: gedehnte Laenge nichtlinear aus der Doppelpyramide (fuer TD0)
            l_extra = {}
            if besch['kante_neu'] is not None:
                i9, ok9 = N.idx_von_keys(besch['k9'])
                a_ = N.S @ xe
                L9g = N.l0[i9] * (1.0 + a_[i9])
                L9h = N.l0[i9]
                l_extra[besch['kante_neu']] = {'gd': float(l_de_flach(L9g[None, :])[0]), 'hg': float(l_de_flach(L9h[None, :])[0])}
            try:
                rec['td0'] = td0_messung(N, xe, besch['alt'], besch['neu'], rec['typ'], sk, l_extra)
            except Exception as exc:          # Messung darf den Lauf nicht abbrechen
                rec['td0'] = {'fehler': repr(exc)}
            x2, y2, minfo = abbilden(N, N2, xe, ye, besch, args.lesart)
            if besch['kante_neu'] is not None:
                inew, _ = N2.idx_von_keys(np.array([besch['kante_neu']]))
                a2 = N2.S @ x2
                lin = N2.l0[inew[0]] * (1.0 + a2[inew[0]])
                minfo['l_de_gedehnt_flach'] = l_extra[besch['kante_neu']]['gd']
                minfo['l_de_gedehnt_linear'] = float(lin)
            H2, V2, K2 = N2.energie(x2, y2)
            rec.update({'ausgefuehrt': True, 'H_vor': H1, 'V_vor': V1, 'K_vor': K1, 'H_nach': H2, 'V_nach': V2, 'K_nach': K2,
                        'dH_rel': (H2 - H1) / H0, 'dV_rel': (V2 - V1) / H0, 'dK_rel': (K2 - K1) / H0,
                        'abbildung': minfo, 'E_nach': N2.E, 'T_nach': int(len(Gn)), 'eig_nach': N2.eig,
                        'stabil_dt': float(np.sqrt(max(N2.eig['w2_max'], 0.0)) * dt), 't_bau_s': N2.t_bau})
            ereig.append(rec)
            N = N2
            x, y, Bx = x2, y2, None
            if args.arm == 'b':
                mu_n = N.mu_alle(x)
                for jj in np.nonzero(mu_n < 0)[0]:
                    gesperrt.add(tuple(N.fkeys[N.fl['t1'][jj] * 4 + N.fl['i1'][jj]].tolist()))
                rec['nach_zug_verletzt'] = int((mu_n < 0).sum())
            rem -= tau
            t_cur = te
        n += 1
        if args.arm == 'b' and gesperrt:
            mu_n = N.mu_alle(x)
            fk = N.fkeys[N.fl['t1'] * 4 + N.fl['i1']]
            frei = set(tuple(r) for r in fk[mu_n > 0].tolist())
            gesperrt -= frei
        if not np.all(np.isfinite(x)) or float(np.linalg.norm(x)) > 1e6 * xref:
            abbruch = {'t': n * dt, 'n': n, 'grund': 'Zustand > 1e6 x Anfangsmode oder nicht endlich'}
            break
        if n % ds == 0 or n == nges:
            probe(N, x, y, n * dt, n)
        if n % NT == 0:
            fk = set(map(tuple, N.fkeys.tolist()))
            gleich = (len(N.G) == len(G0)) and fk == fkeys0
            pz = {'periode': n // NT, 't': n * dt, 'flaechen_wie_anfang': len(fkeys0 & fk) / len(fkeys0),
                  'flaechen_neu': len(fk - fkeys0), 'gleiche_zerlegung': bool(gleich), 'eig': N.eig,
                  'n_zuege': len([e for e in ereig if e.get('ausgefuehrt')])}
            if gleich:
                pz['modal'] = modal(N0, Qm, w2, x, y, mode['j'])
            perioden.append(pz)
    fertig = (n >= nges) or (abbruch is not None)
    meta = {'proben': proben, 'ereignisse': ereig, 'perioden': perioden, 'gesperrt': [list(g) for g in gesperrt],
            'abschnitt': abschnitt, 'rng_state': rng.bit_generator.state if args.arm == 'c' else None}
    if not fertig:
        with open(args.out + '.zustand.json.tmp', 'w') as fh:
            json.dump(meta, fh, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
        np.savez(args.out + '.zustand.tmp.npz', x=x, y=y, n=n, G=N.G, O=N.O)
        os.replace(args.out + '.zustand.json.tmp', args.out + '.zustand.json')
        os.replace(args.out + '.zustand.tmp.npz', zfile)
    else:
        for f in (zfile, args.out + '.zustand.json'):
            if os.path.exists(f):
                os.rename(f, f + '.erledigt')
    res = {'netz': args.netz, 'ninfo': {k: v for k, v in ninfo.items() if k != 'pruefung'}, 'A': args.A, 'arm': args.arm,
           'lesart': args.lesart, 'h': args.h, 'perioden_soll': args.perioden, 'fertig': fertig, 'abschnitt': abschnitt,
           'n': n, 'nges': nges, 'NT': NT, 'dt': dt, 'T': Tper, 'omega_max': float(wmax), 'mode': mode, 'H0': H0,
           'N0': {'E': N0.E, 'T': int(len(G0)), 'nV': N0.nV, 'm': N0.m, 'weg': N0.weg, 'rang_rel': N0.rang_rel,
                  'kontr_S': N0.kontr_S, 'n_A_neg': N0.n_A_neg, 'A_min_rel': N0.A_min_rel, 'eig': N0.eig, 't_bau_s': N0.t_bau, 'skalen': sk, 'F': int(N0.fl['F'])},
           'k1': k1.tolist(), 'proben_spalten': ['t', 'H', 'V', 'K', 'cos+', 'cosx', 'sin+', 'sinx', 'n_zuege', 'n_mu_neg', 'mu_min'],
           'proben': proben, 'ereignisse': ereig, 'perioden': perioden, 'abbruch': abbruch, 'wand_s': time.time() - T0w}
    return res


# ------------------------------------------------------------------------------------------------ Auswertung
def amp_phase(P, om, t0, t1, richt):
    P = np.array(P)
    m = (P[:, 0] >= t0 - 1e-12) & (P[:, 0] <= t1 + 1e-12)
    t = P[m, 0]
    c = P[m, 4:8] @ np.array(richt)
    X = np.stack([np.sin(om * t), np.cos(om * t)], 1)
    co, *_ = np.linalg.lstsq(X, c, rcond=None)
    return float(np.hypot(co[0], co[1])), float(np.arctan2(co[1], co[0])), int(m.sum())


def kennzahlen(d):
    P = np.array(d['proben'])
    H0 = d['H0']
    T = d['T']
    om = 2 * np.pi / T
    ende = P[-1]
    out = {'netz': d['netz'], 'A': d['A'], 'arm': d['arm'], 'lesart': d['lesart'], 'h': d['h'], 'fertig': d['fertig'],
           't_ende_durch_T': float(ende[0] / T), 'drift_ende': float((ende[1] - H0) / H0),
           'drift_max': float(np.abs(P[:, 1] - H0).max() / H0)}
    ev = [e for e in d['ereignisse'] if e.get('ausgefuehrt')]
    out['n_zuege'] = len(ev)
    out['n_23'] = sum(1 for e in ev if e['typ'] == 23)
    out['n_32'] = sum(1 for e in ev if e['typ'] == 32)
    out['n_nicht_ausgefuehrt'] = sum(1 for e in d['ereignisse'] if not e.get('ausgefuehrt'))
    nper = max(ende[0] / T, 1e-300)
    out['zuege_je_periode'] = len(ev) / nper
    if ev:
        dH = np.array([e['dH_rel'] for e in ev])
        dV = np.array([e['dV_rel'] for e in ev])
        dK = np.array([e['dK_rel'] for e in ev])
        out['dH_summe'] = float(dH.sum())
        out['dH_betrag_mittel'] = float(np.abs(dH).mean())
        out['dH_betrag_max'] = float(np.abs(dH).max())
        for typ in (23, 32):
            s = [e for e in ev if e['typ'] == typ]
            if s:
                out['dV_%d_betrag_max' % typ] = float(max(abs(e['dV_rel']) for e in s))
                out['dK_%d_mittel' % typ] = float(np.mean([e['dK_rel'] for e in s]))
                out['dV_%d_mittel' % typ] = float(np.mean([e['dV_rel'] for e in s]))
        t0s = [e['td0'] for e in ev if 'td0' in e and 'gd' in e['td0']]
        for art in ('gd', 'hg'):
            for typ in (23, 32):
                s = [e['td0'][art] for e in ev if e['typ'] == typ and 'td0' in e and art in e['td0']]
                if s:
                    out['td0_%s_%d' % (art, typ)] = {
                        'n': len(s),
                        'stern1_rel_max': float(max(x['stern1_einzel_rel'] for x in s if x['stern1_einzel_rel'] is not None)),
                        'stern2_rel_max': float(max(x['stern2_flaeche_rel'] for x in s)),
                        'dstern1_rel_max': float(max(x['dstern1_max_rel'] for x in s)),
                        'dP_rel_max': float(max(x['dP_max_rel'] for x in s)),
                        'dP_rel_median': float(np.median([x['dP_max_rel'] for x in s]))}
        out['n_td0'] = len(t0s)
        out['stabil_dt_max'] = float(max(e['stabil_dt'] for e in ev))
        out['wachsend_max'] = int(max(e['eig_nach']['n_wachsend'] for e in ev))
        out['A_nicht_pd'] = int(sum(1 for e in ev if not e['eig_nach']['A_pd']))
        out['proj_rest_a_max'] = float(max(e['abbildung']['proj_rest_a'] for e in ev))
        dn = [e['abbildung']['delta_nichtflach'] for e in ev if 'delta_nichtflach' in e['abbildung']]
        if dn:
            out['delta_nichtflach_betrag_max'] = float(np.abs(dn).max())
        ll = [abs(e['abbildung']['l_de_gedehnt_linear'] / e['abbildung']['l_de_gedehnt_flach'] - 1) for e in ev
              if 'l_de_gedehnt_flach' in e['abbildung']]
        if ll:
            out['l_neu_linear_gegen_flach_max'] = float(max(ll))
        out['nach_zug_verletzt_max'] = int(max((e.get('nach_zug_verletzt', 0) for e in ev), default=0))
    per = d['perioden']
    out['perioden'] = len(per)
    if per:
        out['flaechen_wie_anfang_min'] = float(min(p['flaechen_wie_anfang'] for p in per))
        out['flaechen_wie_anfang_ende'] = float(per[-1]['flaechen_wie_anfang'])
        out['gleiche_zerlegung_n'] = int(sum(1 for p in per if p['gleiche_zerlegung']))
        out['wachsend_ende'] = int(per[-1]['eig']['n_wachsend'])
        mo = [p for p in per if 'modal' in p]
        if mo:
            out['modal_letzte'] = mo[-1]['modal']
            out['modal_letzte_periode'] = mo[-1]['periode']
    out['abbruch'] = d.get('abbruch')
    if d['fertig'] and not d.get('abbruch'):
        Tn = d['perioden_soll'] * T
        out['amp'], out['phase'], out['n_amp'] = amp_phase(d['proben'], om, Tn - T, Tn, d['mode']['tt_richtung'])
    out['mode'] = {k: d['mode'][k] for k in ('omega', 'anteil_TT_welle', 'w2', 'n_null')}
    out['dt'] = d['dt']
    out['NT'] = d['NT']
    out['omega_max'] = d['omega_max']
    out['n_mu_neg_max'] = int(P[:, 9].max())
    return out


def auswertung(ordner):
    L = {}
    ein = {}
    for p in sorted(glob.glob(os.path.join(ordner, 'td-*.json'))):
        if p.endswith('zustand.json'):
            continue
        d = json.load(open(p))
        if 'ergebnis' not in d:
            continue
        ein[os.path.basename(p)] = sha(p)
        e = d['ergebnis']
        L[(e['netz'], e['A'], e['arm'], e['lesart'], e['h'])] = kennzahlen(e)
    zeilen = list(L.values())
    U = {}
    glas = ['glas-N128-s%d' % s for s in (1, 2, 3, 4)]

    def get(netz, A, arm, lesart='R', h=0.5):
        z = L.get((netz, A, arm, lesart, h))
        return z if (z is not None and z['fertig']) else None
    # TD0
    t0w, t0p, nt = [], [], 0
    for z in zeilen:
        if z['arm'] == 'b' and z['lesart'] == 'R':
            for typ in (23, 32):
                q = z.get('td0_gd_%d' % typ)
                if q:
                    nt += q['n']
                    t0w.append(max(q['stern1_rel_max'], q['stern2_rel_max'], q['dP_rel_max']))
                    t0p.append((typ, q['stern1_rel_max'], q['stern2_rel_max'], q['dP_rel_max'], q['dstern1_rel_max']))
    if nt:
        w = max(t0w) < 1e-10
        U['TD0'] = {'wortlaut': 'eingetroffen' if w else 'verfehlt', 'plan': 'eingetroffen' if w else 'verfehlt',
                    'n_zuege': nt, 'max_rel': float(max(t0w)),
                    'max_rel_23': float(max([t[1] for t in t0p if t[0] == 23] + [t[2] for t in t0p if t[0] == 23] + [t[3] for t in t0p if t[0] == 23] or [float('nan')])),
                    'max_rel_32': float(max([t[1] for t in t0p if t[0] == 32] + [t[2] for t in t0p if t[0] == 32] + [t[3] for t in t0p if t[0] == 32] or [float('nan')]))}
    else:
        U['TD0'] = {'wortlaut': 'nicht entscheidbar', 'plan': 'nicht entscheidbar', 'n_zuege': 0}
    # TD1
    paare = [(get(n, 1e-3, 'b'), get(n, 1e-3, 'a')) for n in glas]
    paare = [(b, a) for b, a in paare if b and a]
    if paare:
        wort = all(abs(b['drift_ende']) < 2 * abs(a['drift_ende']) for b, a in paare)
        plan = all(b['drift_max'] < 2 * a['drift_max'] for b, a in paare)
        U['TD1'] = {'wortlaut': 'eingetroffen' if wort else 'verfehlt', 'plan': 'eingetroffen' if plan else 'verfehlt',
                    'n_netze': len(paare), 'je_netz': [[b['netz'], b['drift_ende'], a['drift_ende'], b['drift_max'], a['drift_max'], b['n_zuege']] for b, a in paare]}
    else:
        U['TD1'] = {'wortlaut': 'nicht entscheidbar', 'plan': 'nicht entscheidbar'}
    # TD2
    tri = [(get(n, 1e-3, 'c'), get(n, 1e-3, 'a')) for n in glas]
    tri = [(c, a) for c, a in tri if c and a]
    if tri:
        verh = [abs(c['drift_ende']) / max(abs(a['drift_ende']), 1e-300) for c, a in tri]
        verh_m = [c['drift_max'] / max(a['drift_max'], 1e-300) for c, a in tri]
        wachs = [max(c.get('wachsend_max', 0), c.get('wachsend_ende', 0)) for c, a in tri]
        wort = (float(np.median(verh)) >= 10) and any(w > 0 for w in wachs)
        plan = all(v >= 10 for v in verh_m) and all(w > 0 for w in wachs)
        U['TD2'] = {'wortlaut': 'eingetroffen' if wort else 'verfehlt', 'plan': 'eingetroffen' if plan else 'verfehlt',
                    'n_netze': len(tri), 'verh_ende': verh, 'verh_max': verh_m, 'wachsend': wachs}
    else:
        U['TD2'] = {'wortlaut': 'nicht entscheidbar', 'plan': 'nicht entscheidbar'}
    # TD3
    v3, v2, m3, m2 = [], [], [], []
    for n in glas:
        b3, a3, b2, a2 = get(n, 1e-3, 'b'), get(n, 1e-3, 'a'), get(n, 1e-2, 'b'), get(n, 1e-2, 'a')
        if b3 and a3:
            v3.append(abs(b3['amp'] / a3['amp'] - 1))
            if 'modal_letzte' in b3:
                m3.append(1 - b3['modal_letzte']['anteil_TT'])
        if b2 and a2:
            v2.append(abs(b2['amp'] / a2['amp'] - 1))
            if 'modal_letzte' in b2:
                m2.append(1 - b2['modal_letzte']['anteil_TT'])
    if v3:
        teil1 = float(np.mean(v3)) < 1e-3
        U['TD3'] = {'verlust_1e-3': v3, 'verlust_1e-2': v2, 'streu_modal_1e-3': m3, 'streu_modal_1e-2': m2}
        if v2:
            ex = float(np.log10(np.mean(v2) / max(np.mean(v3), 1e-300)))
            U['TD3']['exponent'] = ex
            U['TD3']['wortlaut'] = 'eingetroffen' if (teil1 and ex >= 1.5) else 'verfehlt'
            if m3 and m2:
                exm = float(np.log10(np.mean(m2) / max(np.mean(m3), 1e-300)))
                U['TD3']['exponent_modal'] = exm
                U['TD3']['plan'] = 'eingetroffen' if (float(np.mean(m3)) < 1e-3 and exm >= 1.5) else 'verfehlt'
            else:
                U['TD3']['plan'] = 'nicht entscheidbar'
        else:
            U['TD3']['wortlaut'] = 'verfehlt' if not teil1 else 'nicht entscheidbar'
            U['TD3']['plan'] = U['TD3']['wortlaut']
    else:
        U['TD3'] = {'wortlaut': 'nicht entscheidbar', 'plan': 'nicht entscheidbar'}
    # TD4
    q = [(z['netz'], z['A'], z.get('flaechen_wie_anfang_min'), z.get('gleiche_zerlegung_n'), z.get('perioden'))
         for z in zeilen if z['arm'] == 'b' and z['lesart'] == 'R' and z['h'] == 0.5 and z['fertig']]
    if q:
        wort = all(x[2] >= 0.99 for x in q)
        U['TD4'] = {'wortlaut': 'eingetroffen' if wort else 'verfehlt', 'plan': 'eingetroffen' if wort else 'verfehlt',
                    'je_lauf': q}
    else:
        U['TD4'] = {'wortlaut': 'nicht entscheidbar', 'plan': 'nicht entscheidbar'}
    return {'eingaben_sha256': ein, 'urteile': U, 'zeilen': zeilen}


def bild(ordner, pfad):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    D = {}
    for p in sorted(glob.glob(os.path.join(ordner, 'td-*.json'))):
        if p.endswith('zustand.json'):
            continue
        d = json.load(open(p))
        if 'ergebnis' in d:
            e = d['ergebnis']
            D[(e['netz'], e['A'], e['arm'], e['lesart'], e['h'])] = e
    fig, ax = plt.subplots(2, 3, figsize=(18, 9))
    farben = {'a': '#1f77b4', 'b': '#d62728', 'c': '#2ca02c'}
    for row, A in enumerate((1e-3, 1e-2)):
        for arm in ('a', 'b', 'c'):
            for s in (1, 2, 3, 4):
                e = D.get(('glas-N128-s%d' % s, A, arm, 'R', 0.5))
                if e is None:
                    continue
                P = np.array(e['proben'])
                lab = 'Arm %s' % arm if s == 1 else None
                ax[row, 0].plot(P[:, 0] / e['T'], (P[:, 1] - e['H0']) / e['H0'], color=farben[arm], lw=0.8, label=lab)
                ax[row, 1].plot(P[:, 0] / e['T'], P[:, 8], color=farben[arm], lw=0.8, label=lab)
                if s == 1:
                    ax[row, 2].plot(P[:, 0] / e['T'], (P[:, 4:8] @ np.array(e['mode']['tt_richtung'])) / A, color=farben[arm], lw=0.6, label=lab)
        ax[row, 0].set_title('Energie (H - H0)/H0, A = %g (Glas N = 128, Saaten 1-4)' % A)
        ax[row, 0].set_xlabel('t / T')
        ax[row, 0].set_yscale('symlog', linthresh=1e-10)
        ax[row, 1].set_title('Zahl der Zuege (kumuliert), A = %g' % A)
        ax[row, 1].set_xlabel('t / T')
        ax[row, 2].set_title('TT-Amplitude cos+ / A, Saat 1, A = %g' % A)
        ax[row, 2].set_xlabel('t / T')
        for c in range(3):
            ax[row, c].legend(fontsize=8)
    fig.suptitle('TAKT-DYNAMIK-1 (synthetische Gitterrechnung, keine Messdaten)')
    fig.tight_layout()
    fig.savefig(pfad + '.tmp.png', dpi=100)
    os.replace(pfad + '.tmp.png', pfad)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf', 'auswertung', 'bild', 'probe'])
    ap.add_argument('--netz', default='glas-N128-s1')
    ap.add_argument('--A', type=float, default=1e-3)
    ap.add_argument('--arm', default='a', choices=['a', 'b', 'c'])
    ap.add_argument('--lesart', default='R', choices=['R', 'P'])
    ap.add_argument('--h', type=float, default=0.5, help='omega_max * dt')
    ap.add_argument('--perioden', type=int, default=10)
    ap.add_argument('--proben', type=int, default=200, help='Proben je Periode')
    ap.add_argument('--budget', type=float, default=500.0, help='Wanduhr-Budget je Abschnitt (s)')
    ap.add_argument('--ereignisse', default=None)
    ap.add_argument('--ordner', default='lauf')
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)),
            'module_sha256': {m.__name__: sha(os.path.abspath(m.__file__)) for m in (tg, uk, tu)},
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'lauf':
        erg = lauf(a)
    elif a.modus == 'auswertung':
        erg = auswertung(a.ordner)
    elif a.modus == 'bild':
        bild(a.ordner, a.out)
        print('fertig bild', flush=True)
        return
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        e = erg
        res = {'info': info, 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'],
               'schluessel': tg.nur_schluessel(erg), 'fertig': e.get('fertig'), 'n': e.get('n'), 'nges': e.get('nges'),
               'NT': e.get('NT'), 'dt': e.get('dt'), 'omega_max': e.get('omega_max'), 'mode_omega': e.get('mode', {}).get('omega'), 'mode_anteil': e.get('mode', {}).get('anteil_TT_welle'), 't_bau_N0': e.get('N0', {}).get('t_bau_s'), 'm': e.get('N0', {}).get('m'), 'n_ereig': len(e.get('ereignisse', [])), 'wand_s': e.get('wand_s')}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
