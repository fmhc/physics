#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-KH-1 (fmhc-physics, Runde 49), Code-Agent fuer die Leitung claude-primary.

Ueberleitung Regime K (4D-Regge, Kuhn-Gitter, Zeltstangenhoehe h) -> Regime H (stetige Zeit) im Grenzfall h -> 0.
Unveraendert importiert: rk.py, pt.py (REGIME-K-1), tg.py, hm.py, ew.py, tp.py, tti.py, dn.py, nachtrag_kinetik.py
(HODGE-MASSE-1), regge_welle.py, regge4d.py (REGGE-WELLE-1). Plan: PLAN.md (Abschnitte 1 bis 6).

4D: H_a(k_s, w) = sum_m C_m z^m, z = exp(i w h) (Basispunkt-Konvention rk, a = dl/l); Variablen x = (q[7], n, beta[3],
L[4]) ueber J(w) (PLAN 1.2); P(w) = -(1/h) J^+ H_a J; Schur der lebenden L; Bloecke S_p(h); Extrapolation h -> 0.
3D: Kuhn-Netz ueber tg.modell; Paarungen (a), (a'), (b), (c) und beschreibende (PLAN 3.3).

Modi:
  rauch1   technische Kontrollen und Konvergenznormen (keine Spektren, kein Vergleich mit A2L)
  rauch2   UL0-Maschine an |k| = 0,3 (nur Zahl der Wurzeln und Laufzeit)
  raster   Raster R13 x Betraege (PLAN 3.4) + Kontrollen K1 bis K7
  bz       BZ-Gitter L = 8 (Teil 0 oder 1)
  ul0      UL0 (24 Richtungen, |k| = 0,05) + beschreibende Dispersion
  auswertung  Urteile UL0 bis UL4 nach PLAN 5
"""
import argparse, json, sys, os, time, hashlib, platform, resource, itertools
import numpy as np
import scipy
import scipy.linalg as sla

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import rk  # noqa: E402
import tg  # noqa: E402
import hm  # noqa: E402
import tti  # noqa: E402
import regge_welle as RW  # noqa: E402

H_LISTE = [2.0 ** -j for j in range(11)]
FIT_IDX = [0, 1, 2, 3]         # kubisch (PLAN 1.4, nach Rauchtest r3 verschoben)
FIT2_IDX = [1, 2, 3]           # quadratisch (Fehlerschaetzung)
PMAX = 4
TOL_S = 1e-6
KL_RASTER = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2]
KL_FIT = [0.005, 0.01, 0.02, 0.05, 0.1]
EPS_HM = [1e-3, 2e-3]
DS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
DL = [(1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
IQ = list(range(7)); IN = 7; IB = [8, 9, 10]; IL = [11, 12, 13]; ITOP = 14
IK = list(range(11))


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def herm(X):
    return 0.5 * (X + np.conj(np.swapaxes(X, -1, -2)))


def fro(X):
    return float(np.linalg.norm(X))


# ================================================================================================= 4D-Seite
class Vier:
    """4D-Kuhn-Gitter mit Zeltstangenhoehe h (rk.baue('KW', tau=h)), Laurent-Form und Jacobi-Matrix J."""

    def __init__(self, h):
        self.h = float(h)
        g = rk.baue('KW', tau=self.h)
        self.g = g
        self.NE = g.NE
        self.l = np.array(g.l, float)
        self.raum, self.zeit = {}, {}
        for e, (b1, b2, d) in enumerate(g.ekeys):
            d = tuple(int(x) for x in d)
            assert b1 == 0 and b2 == 0 and d[3] in (0, 1) and all(x in (0, 1) for x in d[:3]), (e, d)
            (self.raum if d[3] == 0 else self.zeit)[d[:3]] = e
        assert len(self.raum) == 7 and len(self.zeit) == 8
        self.top = self.zeit[(1, 1, 1)]
        # Laurent-Daten
        T = g.Tphys
        dT = T[:, None, :, :] - T[:, :, None, :]                      # T_j - T_i
        mm = np.rint(dT[..., 3] / self.h).astype(int)
        assert np.abs(dT[..., 3] - mm * self.h).max() < 1e-12 and set(np.unique(mm)) <= {-1, 0, 1}
        self.rows = np.repeat(g.egid[:, :, None], 10, 2).ravel()
        self.cols = np.repeat(g.egid[:, None, :], 10, 1).ravel()
        self.mm = mm.ravel()
        self.dTs = dT[..., :3].reshape(-1, 3)
        self.W = g.Hloc.ravel()
        # Jacobi-Matrix (Zeilen: rk-Kanten in a-Variablen; Spalten: q[7], n, beta[3], L[4])
        h = self.h
        J1 = np.zeros((self.NE, 15)); Jz = np.zeros((self.NE, 15))
        for i, d in enumerate(DS):
            J1[self.raum[d], i] = 1.0
        for d, e in self.zeit.items():
            d2 = float(sum(d))
            s = h * h + d2
            J1[e, IN] += 2 * h * h / (2 * s)
            for c in range(3):
                J1[e, IB[c]] += 2 * h * d[c] / (2 * s)
            if d2 >= 2:
                J1[e, 11 + DL.index(d)] += 1.0 / (2 * s)
            if d2 >= 1:
                J1[e, DS.index(d)] += 2 * d2 / (2 * s)
                Jz[e, DS.index(d)] = d2 / (2 * s)
        self.J1, self.Jz = J1, Jz

    def laurent(self, ks):
        """C_m (m = -1, 0, 1), NE x NE, in Kantenlaengen, H = Hesse(Summe A eps) wie rk."""
        ph = self.W * np.exp(1j * (self.dTs @ np.asarray(ks, float)))
        C = {}
        for m in (-1, 0, 1):
            sel = self.mm == m
            X = np.zeros(self.NE * self.NE, complex)
            np.add.at(X, self.rows[sel] * self.NE + self.cols[sel], ph[sel])
            C[m] = X.reshape(self.NE, self.NE)
        return C

    def form(self, C, w):
        """H(k_s, w) aus den Laurent-Koeffizienten, w komplex erlaubt (analytisch)."""
        return sum(Cm * np.exp(1j * m * w * self.h) for m, Cm in C.items())

    def bloecke(self, ks, gz=1.0):
        """S_p (p = 0..PMAX) auf (q, n, beta) nach Schur der lebenden L; dazu Diagnose."""
        h = self.h
        C = self.laurent(ks)
        lD = np.diag(self.l)
        Ca = {m: lD @ Cm @ lD for m, Cm in C.items()}
        fak = [1.0, 1.0, 2.0, 6.0, 24.0]
        Hp = [sum(Ca[m] * (1j * m * h) ** p for m in Ca) / fak[p] for p in range(PMAX + 1)]
        Jz = gz * self.Jz
        Jp = [self.J1.astype(complex)] + [Jz * (1j * h) ** p / fak[p] for p in range(1, PMAX + 1)]
        JpH = [np.conj(J.T) for J in Jp]
        P = []
        for p in range(PMAX + 1):
            X = np.zeros((15, 15), complex)
            for a in range(p + 1):
                for b in range(p + 1 - a):
                    c = p - a - b
                    X += JpH[a] @ Hp[b] @ Jp[c]
            P.append(-X / h)
        top_col = max(float(np.abs(Pp[:, 14]).max()) for Pp in P)
        A = [Pp[np.ix_(IK, IK)] for Pp in P]
        B = [Pp[np.ix_(IK, IL)] for Pp in P]
        Bt = [Pp[np.ix_(IL, IK)] for Pp in P]
        D = [Pp[np.ix_(IL, IL)] for Pp in P]
        evD = np.linalg.eigvalsh(herm(D[0]))
        E = [np.linalg.inv(D[0])]
        for p in range(1, PMAX + 1):
            E.append(-E[0] @ sum(D[j] @ E[p - j] for j in range(1, p + 1)))
        S = []
        for p in range(PMAX + 1):
            X = A[p].copy()
            for a in range(p + 1):
                for b in range(p + 1 - a):
                    c = p - a - b
                    X -= B[a] @ E[b] @ Bt[c]
            S.append(X)
        return np.array(S), {'D0_min_rel': float(np.abs(evD).min() / np.abs(evD).max()), 'top_spalte': top_col}


def lagrange0(hs):
    """Gewichte der Polynom-Interpolation, ausgewertet bei h = 0."""
    hs = np.asarray(hs, float)
    w = []
    for j in range(len(hs)):
        o = [i for i in range(len(hs)) if i != j]
        w.append(np.prod(hs[o] / (hs[o] - hs[j])))
    return np.array(w)


W_FIT = lagrange0([H_LISTE[j] for j in FIT_IDX])
W_FIT2 = lagrange0([H_LISTE[j] for j in FIT2_IDX])


def grenzform(vier, ks, gz=1.0, voll=False):
    """S_p(h) fuer alle h, Grenzwert Q0 (kubisch) und Q0' (quadratisch)."""
    Sh, diag = [], []
    for V in vier:
        S, d = V.bloecke(ks, gz)
        Sh.append(S); diag.append(d)
    Sh = np.array(Sh)                                          # (nh, P+1, 11, 11)
    Q0 = np.einsum('j,jpab->pab', W_FIT, Sh[FIT_IDX])
    Q0p = np.einsum('j,jpab->pab', W_FIT2, Sh[FIT2_IDX])
    out = {'Q0': Q0, 'Q0p': Q0p, 'D0_min_rel': min(d['D0_min_rel'] for d in diag),
           'top_spalte': max(d['top_spalte'] for d in diag)}
    # Konvergenz (beschreibend): ||X(h_j) - X(h_j+1)|| relativ, fuer M (S2 qq) und V (S0 qq)
    for nm, (p, I) in {'M': (2, IQ), 'V': (0, IQ), 'C': (0, None)}.items():
        if I is None:
            X = Sh[:, 0, IQ, IN]
        else:
            X = Sh[:, p][:, I][:, :, I]
        ref = fro(X[-1])
        out['konv_' + nm] = [fro(X[j] - X[j + 1]) / ref for j in range(len(vier) - 1)]
    if voll:
        out['Sh'] = Sh
    return out


# ================================================================================================= 3D-Seite
def kuhn3d():
    O = []
    for perm in itertools.permutations(range(3)):
        v = [0, 0, 0]
        verts = [tuple(v)]
        for a in perm:
            v = list(v); v[a] += 1
            verts.append(tuple(v))
        O.append(verts)
    G = np.zeros((6, 4), np.int64)
    O = np.array(O, np.int64)
    LV = np.eye(3); pos = np.zeros((1, 3))
    mod = tg.modell(LV, pos, G, O, {})
    geo = hm.tet_geo(LV, pos, G, O, mod)
    # Zuordnung tg-Kante -> DS-Index und Versatz der Startecke gegen die untere Ecke
    zu, off = [], []
    for e in range(mod['E']):
        vec = mod['n'][e] * mod['l'][e]
        vi = np.rint(vec).astype(int)
        assert np.abs(vec - vi).max() < 1e-12
        if all(x >= 0 for x in vi):
            zu.append(DS.index(tuple(vi))); off.append(np.zeros(3))
        else:
            zu.append(DS.index(tuple(-vi))); off.append(-vi.astype(float))
    mod['zu_DS'] = zu
    mod['start_off'] = np.array(off)        # Startecke (tg) = untere Ecke + off
    return mod, geo


def U_matrix(mod, ks):
    """q_my = U q_tg (PLAN 2): U[DS-Index, tg-Kante] = exp(i k . off)."""
    U = np.zeros((7, 7), complex)
    for e, i in enumerate(mod['zu_DS']):
        U[i, e] = np.exp(1j * (mod['start_off'][e] @ ks))
    return U


def M_disp_my(ks):
    M = np.zeros((7, 3), complex)
    for i, d in enumerate(DS):
        dv = np.array(d, float)
        M[i] = dv / (dv @ dv) * (np.exp(1j * (dv @ ks)) - 1.0)
    return M


def passdefekt(A, Cv, M):
    """||(1 - P_M) A C|| / ||A C||."""
    Q, _ = np.linalg.qr(M)
    x = A @ Cv
    r = x - Q @ (np.conj(Q.T) @ x)
    return float(np.linalg.norm(r) / max(np.linalg.norm(x), 1e-300))


def sinus(a, b):
    a = np.ravel(a); b = np.ravel(b)
    c = abs(np.vdot(a, b)) / (np.linalg.norm(a) * np.linalg.norm(b))
    return float(np.sqrt(max(0.0, 1.0 - c * c)))


def inv_sicher(X):
    """Inverse; bei Singularitaet Pseudo-Inverse (Fall wird ueber Meff_min_rel bzw. 'fehler' sichtbar)."""
    try:
        return np.linalg.inv(X)
    except np.linalg.LinAlgError:
        return np.linalg.pinv(X)


def paar(A, Bm, M, Cv, eps, art):
    try:
        return paar_kern(A, Bm, M, Cv, eps, art)
    except (np.linalg.LinAlgError, ValueError) as ex:
        return {'definiert': False, 'fehler': str(ex), 'ok': False, 'n_neg': 0}


def paar_kern(A, Bm, M, Cv, eps, art):
    """Spektrum einer Paarung (PLAN 3.3): art 'R1' (Komplement von Bild[M, C]) oder 'RH' (Dirac-Paar mit C)."""
    S, Q, Cn, weg, svrel = hm.zerlege(M, Cv)
    out = {'dim': int(S.shape[1]), 'weg': weg}
    Sh = np.conj(S.T)
    if art == 'R1':
        Ar = Sh @ A @ S
    else:
        x = np.conj(Cn.T) @ A @ Cn
        rel = float(np.abs(x).max() / (np.linalg.norm(A, 2) * max(np.linalg.norm(Cn) ** 2, 1e-300)))
        out['CAC_rel'] = rel
        if rel <= 1e-10:
            out['definiert'] = False
            return out
        Ar = hm.rh_A(A, S, Cn)
    out['definiert'] = True
    Br = herm(Sh @ Bm @ S)
    try:
        L = np.linalg.cholesky(Br)
        Li = sla.solve_triangular(L, np.eye(L.shape[0]), lower=True)
        r = hm.z_auswerten(hm.Z_A(Li, Ar), eps)
        out.update(r)
        out['B_red_pd'] = True
    except np.linalg.LinAlgError:
        lam = np.linalg.eigvals(Ar @ Br)
        s = max(float(np.abs(lam).max()), 1e-300)
        out['B_red_pd'] = bool(np.all(np.linalg.eigvalsh(Br) > 0))
        out['n_neg'] = int(((lam.real < -1e-9 * s) | (np.abs(lam.imag) > 1e-9 * s)).sum())
        out['ok'] = False
        out['w2k2'] = None
        out['ausweich_eig'] = True
    return out


def punkt(vier, mod, geo, ks, mit_einseitig=False):
    t0 = time.time()
    eps = float(np.linalg.norm(ks))
    gf = grenzform(vier, ks)
    U = U_matrix(mod, ks)
    T11 = np.eye(11, dtype=complex); T11[:7, :7] = U
    T11H = np.conj(T11.T)
    out = {'k': [float(x) for x in ks], 'eps': eps, 'D0_min_rel': gf['D0_min_rel'], 'top_spalte': gf['top_spalte'],
           'konv_M': gf['konv_M'], 'konv_V': gf['konv_V'], 'konv_C': gf['konv_C']}
    Bs, A1s, M, c = tg.ops(mod, ks)
    B = Bs.toarray()
    out['M_disp_gegen_my'] = fro(np.conj(U.T) @ M_disp_my(ks) - M) / fro(M)
    K_A2L = hm.assemble(mod, geo['Kt'], ks)
    K_LR = geo['vref'] * K_A2L
    A1 = hm.assemble(mod, geo['A1t'], ks)
    res = {}
    for tag in ('Q0', 'Q0p'):
        S = np.array([T11H @ Sp @ T11 for Sp in gf[tag]])          # q-Bloecke in tg-Konvention
        Meff = herm(S[2][np.ix_(IQ, IQ)])
        Veff = herm(S[0][np.ix_(IQ, IQ)])
        Cv = S[0][IQ, IN][:, None]
        X = S[1][np.ix_(IQ, IB)]
        res[tag] = (S, Meff, Veff, Cv, X)
    S, Meff, Veff, Cv, X = res['Q0']
    Sp_, Meffp, Veffp, Cvp, Xp = res['Q0p']
    # Extrapolationsfehler
    out['e_M'] = fro(Meff - Meffp) / fro(Meff)
    out['e_V'] = fro(Veff - Veffp) / fro(Veff)
    out['e_C'] = fro(Cv - Cvp) / fro(Cv)
    # UL1
    out['r_UL1'] = fro(Meff - K_LR) / fro(K_LR)
    out['r_UL1_Q0p'] = fro(Meffp - K_LR) / fro(K_LR)
    out['trKM'] = float(np.real(np.trace(np.conj(K_LR.T) @ Meff)))
    out['nK2'] = fro(K_LR) ** 2
    evM = np.linalg.eigvalsh(Meff)
    out['Meff_eig'] = [float(x) for x in evM]
    out['KLR_eig'] = [float(x) for x in np.linalg.eigvalsh(herm(K_LR))]
    out['Meff_min_rel'] = float(np.abs(evM).min() / np.abs(evM).max())
    out['Meff_herm'] = fro(S[2][np.ix_(IQ, IQ)] - np.conj(S[2][np.ix_(IQ, IQ)].T)) / fro(Meff)
    # Regel-Kennzahlen (PLAN 3.2)
    sig = max(fro(S[p]) * eps ** p for p in range(3))
    lap = [abs(S[0][IN, IN]), abs(S[1][IN, IN]) * eps, abs(S[2][IN, IN]) * eps ** 2,
           fro(S[1][IQ, IN]) * eps, fro(S[2][IQ, IN]) * eps ** 2]
    lap += [fro(S[p][IN, IB]) * eps ** p for p in range(3)] + [fro(S[p][IB, IN]) * eps ** p for p in range(3)]
    out['R_L'] = float(max(lap) / sig)
    out['R_K'] = fro(S[1][np.ix_(IQ, IQ)]) * eps / sig
    MM = Meff @ M
    Y, *_ = np.linalg.lstsq(MM, X, rcond=None)
    out['R_S_rest'] = fro(X - MM @ Y) / fro(X)
    Sbb = S[0][np.ix_(IB, IB)]
    out['R_S_bb'] = fro(Sbb - np.conj(Y.T) @ np.conj(M.T) @ Meff @ M @ Y) / fro(Sbb)
    out['R_S_hoeher'] = float(max(fro(S[2][np.ix_(IQ, IB)]) * eps ** 2, fro(S[1][np.ix_(IB, IB)]) * eps,
                                  fro(S[2][np.ix_(IB, IB)]) * eps ** 2) / sig)
    out['R_H'] = float(max(fro(S[3]) * eps ** 3, fro(S[4]) * eps ** 4) / sig)
    Aeff = inv_sicher(Meff)
    out['R_P'] = passdefekt(Aeff, Cv, M)
    out['R_P_Mc'] = passdefekt(Aeff, c, M)
    KLRi = inv_sicher(herm(K_LR))
    out['R_P_Kc'] = passdefekt(KLRi, c, M)
    out['R_P_KC'] = passdefekt(KLRi, Cv, M)
    out['sin_Cc'] = sinus(Cv, c)
    out['kappa_Cc_re'] = float(np.real(np.vdot(c, Cv) / np.vdot(c, c)))
    out['kappa_Cc_im'] = float(np.imag(np.vdot(c, Cv) / np.vdot(c, c)))
    out['r_V'] = fro(Veff - herm(B)) / fro(B)
    out['VM_null'] = fro(Veff @ M) / (fro(Veff) * fro(M))
    out['CM_null'] = fro(np.conj(Cv.T) @ M) / (fro(Cv) * fro(M))
    ok_adm = (out['R_L'] <= TOL_S and out['R_K'] <= TOL_S and out['R_S_rest'] <= TOL_S and out['R_S_bb'] <= TOL_S
              and out['R_S_hoeher'] <= TOL_S and out['R_H'] <= TOL_S)
    out['adm'] = bool(ok_adm)
    out['pass'] = bool(out['R_P'] <= TOL_S)
    # Paarungen
    sp = {}
    art_a = 'R1' if out['pass'] else 'RH'
    sp['a'] = paar(Aeff, B, M, Cv, eps, art_a)
    sp['a']['art'] = art_a
    Aeffp = inv_sicher(Meffp)
    art_ap = 'R1' if passdefekt(Aeffp, Cvp, M) <= TOL_S else 'RH'
    sp['a_Q0p'] = paar(Aeffp, B, M, Cvp, eps, art_ap)
    sp['a_Q0p']['art'] = art_ap
    sp['a_strich'] = paar(Aeff, Veff, M, Cv, eps, art_a)
    A2L = inv_sicher(K_A2L)
    sp['b'] = paar(A2L, B, M, c, eps, 'R1')
    sp['c'] = paar(A2L, B, M, c, eps, 'RH')
    sp['M_R1'] = paar(Aeff, B, M, c, eps, 'R1')
    sp['M_RH'] = paar(Aeff, B, M, c, eps, 'RH')
    sp['A1R1'] = paar(A1, B, M, c, eps, 'R1')
    out['sp'] = sp
    if mit_einseitig:
        g1 = grenzform(vier, ks, gz=2.0)
        S1 = T11H @ g1['Q0'][2] @ T11
        out['einseitig_rel'] = fro(herm(S1[np.ix_(IQ, IQ)]) - Meff) / fro(Meff)
    out['t_s'] = time.time() - t0
    return out


# ================================================================================================= Kontrollen
def kontrollen(vier, mod, geo):
    rng = np.random.default_rng(20261005)
    out = {}
    # K1, K2
    for V in (vier[0], vier[3]):
        g = V.g
        k1, k2, herm_, dead = 0.0, 0.0, 0.0, 0.0
        for _ in range(8):
            k = rng.uniform(-np.pi, np.pi, 4)
            k[3] = rng.uniform(-np.pi, np.pi) / V.h
            C = V.laurent(k[:3])
            Hl = V.form(C, k[3])
            Hr = g.H(k)
            k1 = max(k1, float(np.abs(Hl - Hr).max() / np.abs(Hr).max()))
            herm_ = max(herm_, float(np.abs(C[-1] - np.conj(C[1].T)).max() / np.abs(C[1]).max()))
            dead = max(dead, max(float(np.abs(Cm[V.top]).max() + np.abs(Cm[:, V.top]).max()) for Cm in C.values()))
            wk = k[3] + 1j * rng.uniform(-2, 2) / V.h
            Hc = V.form(C, wk)
            Gk = g.G(np.r_[k[:3], wk])
            k2 = max(k2, float(np.linalg.norm(Hc @ Gk) / (np.linalg.norm(Hc) * np.linalg.norm(Gk))))
        out['h=%g' % V.h] = {'K1_laurent_gegen_rkH': k1, 'K2_herm': herm_, 'K2_eich_komplex': k2, 'K2_tot': dead}
    # K3
    k3 = {}
    for V in vier:
        kk = V.g.kontrollen()
        k3['%g' % V.h] = {x: kk[x] for x in ('fehlwinkel_max_abs', 'schlaefli', 'M_sym', 'vol_summe_rel_fehler',
                                              'vol_min_rel', 'tote_kanten', 'NE', 'S')}
    out['K3_4d'] = k3
    out['K3_3d'] = {x: mod['pruefung'][x] for x in ('T', 'E', 'nV', 'dieder_summe_minus_2pi_max', 'D_sym_max',
                                                     'schlaefli_lD_max', 'volumen_summe_rel_abw', 'Vbox')}
    out['K3_3d']['geo_kontr'] = geo['kontr']
    out['K3_3d']['vref'] = geo['vref']
    out['K3_3d']['l_mittel'] = float(mod['l'].mean())
    kz = rng.uniform(-np.pi, np.pi, 3)
    Bs, A1s, M, c = tg.ops(mod, kz)
    out['K3_3d']['ops'] = tg.kontr_ops(Bs, A1s, M, c)
    return out


def k4_reproduktion(ref_pfad):
    erg = hm.lauf_spanne('V')
    with open(ref_pfad) as fh:
        ref = json.load(fh)['ergebnis']['spannen']
    def diff(x, y):
        if x is None and y is None:
            return 0.0
        if x is None or y is None:
            return float('inf')
        return abs(x - y)
    d = {v: diff(erg['spannen'][v]['spanne_alle'], ref[v]['spanne_alle']) for v in ref}
    return {'abw_je_variante': d, 'abw_max': float(max(d.values())), 'ref_sha256': sha(ref_pfad),
            'A1R1': erg['spannen']['A1R1']['spanne_alle'], 'A2LR1': erg['spannen']['A2LR1']['spanne_alle']}


def k6_symmetrie(vier, mod, geo):
    out = []
    for v in ((2, 1, 0), (3, 2, 1), (1, 1, 0)):
        for kb in (0.1, 1.0):
            r = []
            base = np.array(v, float) / np.linalg.norm(v)
            for perm in ((0, 1, 2), (1, 0, 2), (2, 0, 1)):
                ks = kb * base[list(perm)]
                gf = grenzform(vier, ks)
                U = U_matrix(mod, ks)
                Me = herm(np.conj(U.T) @ gf['Q0'][2][np.ix_(IQ, IQ)] @ U)
                K = herm(geo['vref'] * hm.assemble(mod, geo['Kt'], ks))
                r.append((np.linalg.eigvalsh(Me), np.linalg.eigvalsh(K)))
            dM = max(float(np.abs(r[i][0] - r[0][0]).max() / np.abs(r[0][0]).max()) for i in (1, 2))
            dK = max(float(np.abs(r[i][1] - r[0][1]).max() / np.abs(r[0][1]).max()) for i in (1, 2))
            out.append({'v': v, 'betrag': kb, 'Meff_spektrum_perm': dM, 'KLR_spektrum_perm': dK})
    return out


# ================================================================================================= UL0
def ul0_punkt(V, ks, kb):
    h = V.h
    C = V.laurent(ks)
    N0 = np.concatenate([V.g.G(np.r_[ks, 0.0]), np.eye(V.NE)[:, [V.top]]], 1)
    U_, s_, _ = np.linalg.svd(N0, full_matrices=True)
    Q0 = U_[:, 5:]
    Fm = {2 * m: np.conj(Q0.T) @ Cm @ Q0 for m, Cm in C.items()}
    kbp = kb * h
    wurz, info = RW.pep_wurzeln(Fm)
    inR2 = (wurz.real >= -0.2 * kbp) & (wurz.real <= 1.2 * RW.R_RE * kbp) & (np.abs(wurz.imag) <= 1.2 * RW.R_IM * kbp)
    kand = wurz[inR2]
    aberth_fehler = False
    if len(kand):
        try:
            verf, nit, letzter = RW.aberth(Fm, kand, kbp)
        except np.linalg.LinAlgError:
            verf, nit, letzter, aberth_fehler = kand, 0, float('nan'), True
    else:
        verf, nit, letzter = kand, 0, 0.0
    inR = (verf.real > 0) & (verf.real <= RW.R_RE * kbp) & (np.abs(verf.imag) <= RW.R_IM * kbp)
    wR = np.sort_complex(verf[inR])
    wd = RW.windung(Fm, kbp)
    return {'n_R': int(len(wR)), 'windung': wd['windung'], 'windung_zahl': wd['zahl'],
            'v': [float(x.real / kbp) for x in wR], 'v_im': [float(x.imag / kbp) for x in wR],
            'N0_sv_min_rel': float(s_[-1] / s_[0]), 'pep': info, 'aberth_letzter': float(letzter),
            'aberth_fehler': aberth_fehler}


def lauf_ul0(vier, rauch=False, probe=False):
    out = {'haupt': [], 'beschreibend': []}
    R = RW.richtungen()
    if rauch:
        V = vier[0]
        for nm, nh in R[:2]:
            r = ul0_punkt(V, 0.3 * nh, 0.3)
            out['haupt'].append({'richtung': nm, 'n_R': r['n_R'], 'windung_zahl': r['windung_zahl']})
        return out
    V = vier[0]
    kb0 = 0.3 if probe else 0.05
    for nm, nh in (R[:2] if probe else R):
        r = ul0_punkt(V, kb0 * nh, kb0)
        r['richtung'] = nm
        out['haupt'].append(r)
    for j in ((1,) if probe else (0, 1, 2, 3)):
        V = vier[j]
        for nm, nh in R:
            if nm not in ('x+', 'xy+', 'xyz+', '123', 'fib05'):
                continue
            for kb in (0.05, 0.2):
                if j == 0 and kb == 0.05:
                    continue
                r = ul0_punkt(V, kb * nh, kb)
                r['richtung'] = nm; r['h'] = V.h; r['betrag'] = kb
                out['beschreibend'].append(r)
    return out


# ================================================================================================= Laeufe
def bau_alles():
    t0 = time.time()
    vier = [Vier(h) for h in H_LISTE]
    mod, geo = kuhn3d()
    return vier, mod, geo, time.time() - t0


def lauf_raster(vier, mod, geo, ref_pfad, probe=False):
    lm = float(mod['l'].mean())
    R = tti.richtungen13()[:2] if probe else tti.richtungen13()
    pts = []
    for ir, (nm, d) in enumerate(R):
        for kl in KL_RASTER:
            p = punkt(vier, mod, geo, (kl / lm) * d, mit_einseitig=True)
            p.update({'ridx': ir, 'richtung': nm, 'kl': kl, 'art': 'kl'})
            pts.append(p)
        for e in EPS_HM:
            p = punkt(vier, mod, geo, e * d)
            p.update({'ridx': ir, 'richtung': nm, 'kl': e * lm, 'art': 'hm', 'betrag_hm': e})
            pts.append(p)
    out = {'punkte': pts, 'l_mittel': lm}
    out['kontrollen'] = kontrollen(vier, mod, geo)
    out['K6'] = k6_symmetrie(vier, mod, geo)
    out['K4'] = k4_reproduktion(ref_pfad)
    return out


def bz_k(teil):
    L = 8
    ms = [m for m in itertools.product(range(L), repeat=3) if any(m)]
    ms = ms[:256] if teil == 0 else ms[256:]
    return [(m, 2 * np.pi * np.array(m, float) / L) for m in ms]


def lauf_bz(vier, mod, geo, teil, probe=False):
    pts = []
    for m, ks in (bz_k(teil)[:8] if probe else bz_k(teil)):
        p = punkt(vier, mod, geo, ks)
        p['m'] = list(m)
        pts.append(p)
    return {'punkte': pts, 'teil': teil}


def lauf_rauch3(vier, mod, geo):
    """Technisch: Normen aller Bloecke S_p(h) je h an zwei k (h-Abhaengigkeit; kein Vergleich mit A2L)."""
    lm = float(mod['l'].mean())
    bl = {'qq': (IQ, IQ), 'qn': (IQ, [IN]), 'qb': (IQ, IB), 'nn': ([IN], [IN]), 'nb': ([IN], IB), 'bb': (IB, IB)}
    out = []
    for ks in ((0.1 / lm) * np.array([2.0, 1.0, 0.0]) / np.sqrt(5.0), np.array([np.pi / 2, np.pi / 4, 0.0])):
        gf = grenzform(vier, ks, voll=True)
        Sh = gf['Sh']
        z = {'k': ks.tolist()}
        for p in range(PMAX + 1):
            for nm, (I, Jx) in bl.items():
                z['S%d_%s' % (p, nm)] = [fro(Sh[j, p][np.ix_(I, Jx)]) for j in range(len(vier))]
        out.append(z)
    return out


def lauf_rauch1(vier, mod, geo):
    out = {'kontrollen': kontrollen(vier, mod, geo)}
    lm = float(mod['l'].mean())
    konv = []
    for nm, d in tti.richtungen13()[:3]:
        for kl in (0.01, 0.2):
            gf = grenzform(vier, (kl / lm) * d)
            konv.append({'richtung': nm, 'kl': kl, 'konv_M': gf['konv_M'], 'konv_V': gf['konv_V'],
                         'konv_C': gf['konv_C'], 'D0_min_rel': gf['D0_min_rel'], 'top_spalte': gf['top_spalte']})
    for m, ks in bz_k(0)[::64]:
        gf = grenzform(vier, ks)
        konv.append({'m': list(m), 'konv_M': gf['konv_M'], 'konv_V': gf['konv_V'], 'konv_C': gf['konv_C'],
                     'D0_min_rel': gf['D0_min_rel']})
    out['konvergenz'] = konv
    t = time.time()
    _ = punkt(vier, mod, geo, 0.01 * np.array([1.0, 0, 0]), mit_einseitig=True)
    out['t_punkt_s'] = time.time() - t
    out['punkt_schluessel'] = sorted(_.keys())
    return out


# ================================================================================================= Auswertung
def fit_kl(kls, ws):
    x = np.asarray(kls, float) ** 2
    Am = np.stack([np.ones_like(x), x, x ** 2], 1)
    cf, *_ = np.linalg.lstsq(Am, np.asarray(ws, float), rcond=None)
    return cf


def spanne_variante(pts, var):
    """Spanne0 (Fit je Richtung und Zweig ueber KL_FIT), Spanne je kl (PLAN 3.4)."""
    W = {}
    for p in pts:
        if p['art'] != 'kl':
            continue
        r = p['sp'][var]
        ok = bool(r.get('definiert', True) and r.get('ok') and r.get('w2k2') is not None and len(r['w2k2']) == 2)
        W[(p['ridx'], p['kl'])] = (ok, r['w2k2'] if ok else [np.nan, np.nan])
    nr = 1 + max(i for i, _ in W)
    je = {}
    for kl in KL_RASTER:
        ww = np.array([W[(i, kl)][1] for i in range(nr)], float)
        oks = [W[(i, kl)][0] for i in range(nr)]
        je['%g' % kl] = {'spanne': float(np.nanmax(ww) / np.nanmin(ww) - 1) if np.isfinite(ww).any() else None,
                         'alle_ok': bool(all(oks)), 'n_ok': int(sum(oks))}
    w0, alle_ok = [], True
    for i in range(nr):
        for b in range(2):
            ws = [W[(i, kl)][1][b] for kl in KL_FIT]
            alle_ok &= all(W[(i, kl)][0] for kl in KL_FIT)
            if np.all(np.isfinite(ws)):
                w0.append(fit_kl(KL_FIT, ws)[0])
    w0 = np.array(w0)
    s0 = float(w0.max() / w0.min() - 1) if len(w0) and w0.min() > 0 else None
    return {'spanne0': s0, 'alle_ok_fit': bool(alle_ok), 'w0_min': float(w0.min()) if len(w0) else None,
            'w0_max': float(w0.max()) if len(w0) else None, 'je_kl': je}


def wachsend(pts, var):
    n_def, n_undef, n_grow, kmax = 0, 0, 0, 0
    orte = []
    for p in pts:
        r = p['sp'][var]
        if not r.get('definiert', True):
            n_undef += 1
            continue
        n_def += 1
        nn = int(r.get('n_neg', 0))
        if nn > 0:
            n_grow += 1
            kmax = max(kmax, nn)
            if len(orte) < 12:
                orte.append(p.get('m', p['k']))
    return {'k_definiert': n_def, 'k_nicht_definiert': n_undef, 'k_wachsend': n_grow, 'max_je_k': kmax, 'orte': orte}


def lauf_auswertung(pfade):
    J = {nm: json.load(open(p)) for nm, p in pfade.items()}
    ras = J['raster']['ergebnis']['punkte']
    bz = J['bz0']['ergebnis']['punkte'] + J['bz1']['ergebnis']['punkte']
    alle = ras + bz
    out = {'eingaben': {nm: {'pfad': p, 'sha256': sha(p), 'skript': J[nm]['info']['skript_sha256']}
                        for nm, p in pfade.items()}}
    U = {}
    # UL0
    h0 = J['ul0']['ergebnis']['haupt']
    vv = [v for r in h0 for v in r['v']]
    ok0 = all(r['n_R'] == 2 and r['windung_zahl'] == 2 and all(0.9997 <= v <= 0.9999 for v in r['v']) for r in h0)
    U['UL0'] = {'plan': 'eingetroffen' if ok0 else 'nicht eingetroffen', 'n_richtungen': len(h0),
                'n_R': sorted(set(r['n_R'] for r in h0)), 'windung': sorted(set(r['windung_zahl'] for r in h0)),
                'v_min': min(vv) if vv else None, 'v_max': max(vv) if vv else None,
                'v_im_max': max(abs(x) for r in h0 for x in r['v_im']) if vv else None}
    # UL1
    rp = [p['r_UL1'] + p['e_M'] for p in alle]
    rm = [p['r_UL1'] - p['e_M'] for p in alle]
    if max(rp) < 1e-6:
        u1 = 'eingetroffen'
    elif max(rm) >= 1e-6:
        u1 = 'nicht eingetroffen'
    else:
        u1 = 'nicht entscheidbar'
    kap = sum(p['trKM'] for p in alle) / sum(p['nK2'] for p in alle)
    U['UL1'] = {'plan': u1, 'r_max': max(p['r_UL1'] for p in alle), 'r_min': min(p['r_UL1'] for p in alle),
                'r_max_raster': max(p['r_UL1'] for p in ras), 'r_max_bz': max(p['r_UL1'] for p in bz),
                'r_kl_0005_max': max(p['r_UL1'] for p in ras if p['art'] == 'kl' and p['kl'] == 0.005),
                'r_hm_1e-3_max': max(p['r_UL1'] for p in ras if p['art'] == 'hm' and p.get('betrag_hm') == 1e-3),
                'e_M_max': max(p['e_M'] for p in alle), 'kappa_stern': kap,
                'r_Q0p_max': max(p['r_UL1_Q0p'] for p in alle)}
    # Regeln
    reg = {}
    for key in ('R_L', 'R_K', 'R_S_rest', 'R_S_bb', 'R_S_hoeher', 'R_H', 'R_P', 'R_P_Mc', 'R_P_Kc', 'R_P_KC',
                'sin_Cc', 'r_V', 'VM_null', 'CM_null', 'e_M', 'e_V', 'e_C', 'D0_min_rel', 'Meff_min_rel',
                'M_disp_gegen_my', 'Meff_herm', 'top_spalte'):
        xs = [p[key] for p in alle]
        xk = [p[key] for p in ras if p['eps'] < 0.05]
        reg[key] = {'max': float(max(xs)), 'min': float(min(xs)), 'max_raster_klein': float(max(xk))}
    reg['adm_alle'] = bool(all(p['adm'] for p in alle))
    reg['adm_anzahl'] = int(sum(p['adm'] for p in alle))
    reg['pass_alle'] = bool(all(p['pass'] for p in alle))
    reg['pass_anzahl'] = int(sum(p['pass'] for p in alle))
    reg['kappa_Cc_re'] = [float(min(p['kappa_Cc_re'] for p in alle)), float(max(p['kappa_Cc_re'] for p in alle))]
    reg['kappa_Cc_im_max'] = float(max(abs(p['kappa_Cc_im']) for p in alle))
    reg['art_a'] = sorted(set(p['sp']['a']['art'] for p in alle))
    reg['einseitig_rel'] = [float(min(p['einseitig_rel'] for p in ras if 'einseitig_rel' in p)),
                            float(max(p['einseitig_rel'] for p in ras if 'einseitig_rel' in p))]
    out['regeln'] = reg
    # Spannen und wachsende Moden
    var = ('a', 'a_Q0p', 'a_strich', 'b', 'c', 'M_R1', 'M_RH', 'A1R1')
    out['spannen'] = {v: spanne_variante(ras, v) for v in var}
    out['wachsend'] = {v: {'raster': wachsend(ras, v), 'bz': wachsend(bz, v), 'alle': wachsend(alle, v)} for v in var}
    hmsp = {}
    for v in var:
        ww = [x for p in ras if p['art'] == 'hm' and p['sp'][v].get('w2k2') for x in p['sp'][v]['w2k2']]
        oks = [bool(p['sp'][v].get('ok')) for p in ras if p['art'] == 'hm']
        hmsp[v] = {'spanne_hm': float(max(ww) / min(ww) - 1) if ww and min(ww) > 0 else None, 'alle_ok': bool(all(oks))}
    out['spannen_hm_raster'] = hmsp
    # UL2
    s_a, s_ap = out['spannen']['a'], out['spannen']['a_Q0p']
    w_a, w_ap = out['wachsend']['a']['alle'], out['wachsend']['a_Q0p']['alle']
    voraus = reg['adm_alle'] and min(p['Meff_min_rel'] for p in alle) > 1e-12
    if not voraus or s_a['spanne0'] is None or not s_a['alle_ok_fit'] or s_ap['spanne0'] is None:
        u2 = 'nicht entscheidbar'
        delta = None
    else:
        delta = abs(s_a['spanne0'] - s_ap['spanne0'])
        grow_beide = any(p['sp']['a'].get('n_neg', 0) > 0 and p['sp']['a_Q0p'].get('n_neg', 0) > 0 for p in alle)
        grow_eins = w_a['k_wachsend'] > 0 or w_ap['k_wachsend'] > 0
        undef = w_a['k_nicht_definiert'] > 0
        if s_a['spanne0'] + delta < 1e-6 and not grow_eins and not undef:
            u2 = 'eingetroffen'
        elif s_a['spanne0'] - delta >= 1e-6 or grow_beide:
            u2 = 'nicht eingetroffen'
        else:
            u2 = 'nicht entscheidbar'
    U['UL2'] = {'plan': u2, 'voraussetzung_adm_legendre': bool(voraus), 'spanne0': s_a['spanne0'], 'delta': delta,
                'k_wachsend': w_a['k_wachsend'], 'k_wachsend_Q0p': w_ap['k_wachsend'], 'art_a': reg['art_a']}
    # UL3
    s_b = out['spannen']['b']
    if s_b['spanne0'] is None or not s_b['alle_ok_fit']:
        u3 = 'nicht entscheidbar'
    else:
        u3 = 'eingetroffen' if s_b['spanne0'] > 0.01 else 'nicht eingetroffen'
    U['UL3'] = {'plan': u3, 'spanne0': s_b['spanne0'], 'alle_ok_fit': s_b['alle_ok_fit']}
    # UL4
    w_c = out['wachsend']['c']['alle']
    if w_c['k_wachsend'] > 0:
        u4 = 'eingetroffen'
    elif w_c['k_nicht_definiert'] == 0:
        u4 = 'nicht eingetroffen'
    else:
        u4 = 'nicht entscheidbar'
    U['UL4'] = {'plan': u4, 'k_wachsend': w_c['k_wachsend'], 'k_nicht_definiert': w_c['k_nicht_definiert'],
                'k_definiert': w_c['k_definiert'], 'max_je_k': w_c['max_je_k']}
    out['urteile'] = U
    # Kontrollen-Zusammenfassung
    ko = J['raster']['ergebnis']['kontrollen']
    out['kontrollen'] = {'K1_K2': {k: v for k, v in ko.items() if k.startswith('h=')},
                         'K3_fehlwinkel_max': max(v['fehlwinkel_max_abs'] for v in ko['K3_4d'].values()),
                         'K3_tote_kanten': {h: v['tote_kanten'] for h, v in ko['K3_4d'].items()},
                         'K3_3d': ko['K3_3d'], 'K4': J['raster']['ergebnis']['K4'],
                         'K6': J['raster']['ergebnis']['K6']}
    out['ul0_beschreibend'] = J['ul0']['ergebnis']['beschreibend']
    return out


# ================================================================================================= main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch1', 'rauch2', 'rauch3', 'raster', 'bz', 'ul0', 'auswertung'])
    ap.add_argument('--teil', type=int, default=0)
    ap.add_argument('--probe', action='store_true', help='Codeprobe mit wenigen Punkten (Werte nicht ansehen)')
    ap.add_argument('--ref', default=None)
    ap.add_argument('--ein', nargs='*', default=[])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'skript_sha256': sha(os.path.abspath(__file__)),
            'module_sha256': {nm: sha(os.path.abspath(sys.modules[nm].__file__))
                              for nm in ('rk', 'pt', 'tg', 'hm', 'ew', 'tp', 'tti', 'dn', 'nachtrag_kinetik',
                                         'regge_welle', 'regge4d') if nm in sys.modules}}
    if a.modus == 'auswertung':
        erg = lauf_auswertung(dict(x.split('=', 1) for x in a.ein))
    else:
        vier, mod, geo, tb = bau_alles()
        info['t_aufbau_s'] = tb
        if a.modus == 'rauch1':
            erg = lauf_rauch1(vier, mod, geo)
        elif a.modus == 'rauch2':
            erg = lauf_ul0(vier, rauch=True)
        elif a.modus == 'rauch3':
            erg = lauf_rauch3(vier, mod, geo)
        elif a.modus == 'raster':
            erg = lauf_raster(vier, mod, geo, a.ref, probe=a.probe)
        elif a.modus == 'bz':
            erg = lauf_bz(vier, mod, geo, a.teil, probe=a.probe)
        else:
            erg = lauf_ul0(vier, probe=a.probe)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
