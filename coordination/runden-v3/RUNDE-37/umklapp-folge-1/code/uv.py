#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-V-1 (fmhc-physics, Runde 49), Code-Agent fuer die Leitung claude-primary.

Grenzfall kleiner Zeltstangen (h -> 0) der 4D-Regge-Wirkung auf Finns gefuelltem Netz V mal Zeit (REGIME-K-2, Arm V-A,
tau = h) und Kontrolle auf dem Kuhn-Gitter (UEBERLEITUNG-KH-1). Plan: PLAN.md (Abschnitte 1 bis 12).
Unveraendert importiert: rk.py, pt.py, rk2.py, ew.py, tp.py (REGIME-K-2), tg.py, hm.py, tti.py, dn.py,
nachtrag_kinetik.py (HODGE-MASSE-1).

Modi:
  rauch1     technische Kontrollen K1 bis K5 und Laufzeit je k (keine h-Differenzen, keine Spektren)
  kw         Kuhn: Raster + BZ, Schemata achse (UV0) und ls (beschreibend)
  vraster    V: Raster (104 k), Schemata ls (Haupt), ls2 und lsa (beschreibend)
  vbz        V: BZ-Teil 0 oder 1 (Teil 1 mit K, U)
  hoeher     V: Bloecke bis p = 4 an 4 k je h (beschreibend)
  auswertung Urteile UV0 bis UV4 nach PLAN 10
"""
import argparse, json, sys, os, time, hashlib, platform, resource, itertools
import numpy as np
import scipy
import scipy.linalg as sla

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import rk  # noqa: E402
import rk2  # noqa: E402
import tg  # noqa: E402
import hm  # noqa: E402
import tti  # noqa: E402
import tp  # noqa: E402

H7 = [2.0 ** -j for j in range(7)]
FIT_A = [0, 1, 2, 3]          # kubisch durch 1, 1/2, 1/4, 1/8 (Q0)
FIT_B = [1, 2, 3]             # quadratisch durch 1/2, 1/4, 1/8 (Q0')
FIT_C = [3, 4, 5, 6]          # kubisch durch 1/8 ... 1/64 (Q0'')
KL_RASTER = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2]
KL_FIT = [0.005, 0.01, 0.02, 0.05, 0.1]
EPS_HM = [1e-3, 2e-3]
TOL_W = 1e-9
LUECKE_MAX = hm.LUECKE_MAX
SCHEMA_W = {'achse': (1.0, 0.0), 'ls': (0.5, 0.5), 'ls2': (0.5, 0.5), 'lsa': (0.5, 0.5)}


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def herm(X):
    return 0.5 * (X + np.conj(np.swapaxes(X, -1, -2)))


def fro(X):
    return float(np.linalg.norm(X))


def lagrange0(hs):
    hs = np.asarray(hs, float)
    w = []
    for j in range(len(hs)):
        o = [i for i in range(len(hs)) if i != j]
        w.append(np.prod(hs[o] / (hs[o] - hs[j])))
    return np.array(w)


W_A = lagrange0([H7[j] for j in FIT_A])
W_B = lagrange0([H7[j] for j in FIT_B])
W_C = lagrange0([H7[j] for j in FIT_C])


# ================================================================================================= 4D-Seite
def baue_gitter(netz, h):
    if netz == 'KW':
        return rk.baue('KW', tau=h)
    xb, tets, arten = rk2.netz_raum('V')
    NV = len(xb)
    rang = {b: b for b in range(NV)}                      # Hubfolge A (REGIME-K-2, V-A)
    hb = [rang[b] / float(NV) for b in range(NV)]
    return rk.Gitter('V-A', xb, hb, tp.AV.T, tets, rk2.ord_rang(rang), h)


class Vier:
    """Zeltstangen-Gitter mit Hoehe h; Abbildung J (PLAN 2), Taylor-Bloecke und Schur ueber L (PLAN 3)."""

    def __init__(self, netz, h):
        self.netz, self.h = netz, float(h)
        g = baue_gitter(netz, h)
        self.g = g
        self.NE, self.NV = g.NE, g.NV
        self.lau = rk2.Laurent(g)
        assert set(self.lau.ms) <= {-1, 0, 1}, self.lau.ms
        self.tot = set(rk2.tote_idx(g))
        keys = g.ekeys
        self.raum = [e for e, k in enumerate(keys) if k[2][3] == 0]
        self.ridx = {(keys[e][0], keys[e][1], tuple(int(x) for x in keys[e][2][:3])): i for i, e in enumerate(self.raum)}
        self.zelt = {}
        dg = []
        for e, (b1, b2, d4) in enumerate(keys):
            if d4[3] == 0:
                continue
            if b1 == b2 and all(int(x) == 0 for x in d4[:3]):
                assert int(d4[3]) == 1
                self.zelt[int(b1)] = e
            else:
                dg.append(e)
        assert len(self.zelt) == self.NV
        self.diag = dg
        nq = len(self.raum)
        self.nq = nq
        A3 = g.A3
        self.d_e = np.array([keys[e][2][:3] for e in dg], float)
        self.Rd = self.d_e @ A3.T                              # raeumlicher Zellversatz der Endecke
        self.dt = np.array([int(keys[e][2][3]) for e in dg])
        assert set(self.dt.tolist()) <= {-1, 1}
        self.b1 = np.array([int(keys[e][0]) for e in dg])
        self.b2 = np.array([int(keys[e][1]) for e in dg])
        self.partner = np.array([self.ridx[(keys[e][0], keys[e][1], tuple(int(x) for x in keys[e][2][:3]))] for e in dg])
        self.dx = g.E[dg, :3]
        self.dT = g.E[dg, 3]
        self.s = g.l[dg] ** 2
        self.dx2 = np.sum(self.dx ** 2, 1)
        rr = self.raum
        self.r_dx = g.E[rr, :3]
        self.r_dT = g.E[rr, 3]                                  # Schichtkanten sind bei gestaffelten Hoehen geneigt
        self.r_s = g.l[rr] ** 2
        self.r_dx2 = np.sum(self.r_dx ** 2, 1)
        self.r_b1 = np.array([int(keys[e][0]) for e in rr])
        self.r_b2 = np.array([int(keys[e][1]) for e in rr])
        self.r_Rd = np.array([keys[e][2][:3] for e in rr], float) @ A3.T
        assert np.abs(self.dx2 - self.r_dx2[self.partner]).max() < 1e-12
        self.lebend = np.array([e not in self.tot for e in dg])
        self.achse = np.array([int(np.sum(np.abs(self.d_e[j]))) == 1 and self.netz == 'KW' for j in range(len(dg))])

    @staticmethod
    def schichten(dT, dt):
        """Startschicht der zeitlich ausgerichteten Zeltstangen an Start- und Endecke (PLAN 2): die Zeltstange, die von
        der Ecke zur Zeit der anderen Ecke hin reicht."""
        if dT > 0:
            return 0, dt - 1
        return -1, dt

    def shift_matrix(self, ks, w1, w2, lebend_only=True):
        """B_s in y-Koordinaten (sigma / (2 |dx|^2)) bei z = 1: Zeilen Diagonalen, Spalten 3 NV."""
        ph = np.exp(1j * (self.Rd @ ks))
        n = len(self.diag)
        By = np.zeros((n, 3 * self.NV), complex)
        for c in range(3):
            fac = 2.0 * self.dT * self.dx[:, c] / (2.0 * self.dx2)
            np.add.at(By, (np.arange(n), 3 * self.b1 + c), w1 * fac)
            np.add.at(By, (np.arange(n), 3 * self.b2 + c), w2 * fac * ph)
        if lebend_only:
            By = By[self.lebend]
        return By

    def L_basis(self, ks, schema):
        """Orthonormalbasis des Gitterrest-Unterraums in y-Koordinaten der lebenden Diagonalen (PLAN 2)."""
        nl = int(self.lebend.sum())
        if schema == 'achse':
            idx = [j for j, jj in enumerate(np.nonzero(self.lebend)[0]) if not self.achse[jj]]
            Q = np.zeros((nl, len(idx)), complex)
            for c, j in enumerate(idx):
                Q[j, c] = 1.0
            By = self.shift_matrix(ks, 1.0, 0.0)
            rB = int(np.linalg.matrix_rank(By, tol=1e-9 * max(np.abs(By).max(), 1e-300)))
            return Q, rB
        w1, w2 = SCHEMA_W[schema]
        By = self.shift_matrix(ks, w1, w2)
        if schema == 'ls2':
            # Komplement in der Metrik von sigma selbst (sigma = 2 |dx|^2 y), zurueck in y-Koordinaten
            f = 2.0 * self.dx2[self.lebend]
            U, sv, _ = np.linalg.svd(f[:, None] * By, full_matrices=True)
            rB = int((sv > 1e-9 * sv[0]).sum())
            return U[:, rB:] / f[:, None], rB
        U, sv, _ = np.linalg.svd(By, full_matrices=True)
        rB = int((sv > 1e-9 * sv[0]).sum())
        return U[:, rB:], rB

    def J_mats(self, ks, schema):
        """J^(m), m = -1, 0, 1 (Zeilen: alle Kanten in a-Variablen; Spalten: q, n, beta, lambda)."""
        w1, w2 = SCHEMA_W[schema]
        QL, rB = self.L_basis(ks, schema)
        nq, NV = self.nq, self.NV
        nL = QL.shape[1]
        ncol = nq + NV + 3 * NV + nL
        J = {m: np.zeros((self.NE, ncol), complex) for m in (-1, 0, 1)}

        def lapse_shift(e, b1, b2, phb2, dT, dt, dxv, s, ww1, ww2):
            s1, s2 = self.schichten(dT, dt)
            J[s1][e, nq + b1] += ww1 * 2 * dT * dT / (2 * s)
            J[s2][e, nq + b2] += ww2 * phb2 * 2 * dT * dT / (2 * s)
            for c in range(3):
                J[s1][e, nq + NV + 3 * b1 + c] += ww1 * 2 * dT * dxv[c] / (2 * s)
                J[s2][e, nq + NV + 3 * b2 + c] += ww2 * phb2 * 2 * dT * dxv[c] / (2 * s)

        q_ist_a = schema in ('achse', 'lsa')
        rph = np.exp(1j * (self.r_Rd @ ks))
        for i, e in enumerate(self.raum):
            if q_ist_a:
                J[0][e, i] = 1.0                               # q = a der Schichtkante (Planfassung A)
            else:
                # q = raeumlicher Metrikanteil der (geneigten) Schichtkante; Lapse/Shift wie an den Diagonalen (Fassung B)
                J[0][e, i] = self.r_dx2[i] / self.r_s[i]
                lapse_shift(e, self.r_b1[i], self.r_b2[i], rph[i], self.r_dT[i], 0, self.r_dx[i], self.r_s[i], w1, w2)
        for b, e in self.zelt.items():
            J[0][e, nq + b] = 1.0
        ph = np.exp(1j * (self.Rd @ ks))
        lebend_pos = {jj: c for c, jj in enumerate(np.nonzero(self.lebend)[0])}
        for j, e in enumerate(self.diag):
            s, dx2, dT, dt = self.s[j], self.dx2[j], self.dT[j], int(self.dt[j])
            i = self.partner[j]
            J[0][e, i] += dx2 / (2 * s)
            J[dt][e, i] += dx2 / (2 * s)
            lapse_shift(e, self.b1[j], self.b2[j], ph[j], dT, dt, self.dx[j], s, w1, w2)
            if self.lebend[j]:
                J[0][e, nq + 4 * NV:] += (dx2 / s) * QL[lebend_pos[j]]
        return J, nL, rB

    def bloecke(self, ks, schema, pmax=2):
        """S_p (p = 0..pmax) auf (q, n, beta) nach Schur ueber L; Diagnose."""
        h = self.h
        C = self.lau.koeff(np.asarray(ks, float))
        lD = self.g.l
        Ca = {m: lD[:, None] * Cm * lD[None, :] for m, Cm in C.items()}
        fak = [1.0, 1.0, 2.0, 6.0, 24.0]
        Hp = [sum(Ca[m] * (1j * m * h) ** p for m in Ca) / fak[p] for p in range(pmax + 1)]
        Jm, nL, rB = self.J_mats(ks, schema)
        Jp = [sum(Jm[m] * (1j * m * h) ** p for m in Jm) / fak[p] for p in range(pmax + 1)]
        JpH = [np.conj(X.T) for X in Jp]
        HJ = {}
        for b in range(pmax + 1):
            for c in range(pmax + 1 - b):
                HJ[(b, c)] = Hp[b] @ Jp[c]
        P = []
        for p in range(pmax + 1):
            X = 0.0
            for a in range(p + 1):
                for b in range(p + 1 - a):
                    X = X + JpH[a] @ HJ[(b, p - a - b)]
            P.append(-X / h)
        nK = self.nq + 4 * self.NV
        IK = list(range(nK))
        IL = list(range(nK, nK + nL))
        rows_live = [e for e in range(self.NE) if e not in self.tot]
        J1 = Jp[0][rows_live]
        sv = np.linalg.svd(J1, compute_uv=False)
        diag = {'rang_B_s': rB, 'n_L': nL, 'J_sv_min_rel': float(sv[-1] / sv[0]),
                'J_rang_ok': bool(sv[-1] > 1e-10 * sv[0] and J1.shape[1] <= J1.shape[0] and rB == 3 * self.NV)}
        if not diag['J_rang_ok']:
            diag['grund'] = 'schema_rang'
            return None, diag
        if nL == 0:
            return np.array(P), diag
        A = [Pp[np.ix_(IK, IK)] for Pp in P]
        B = [Pp[np.ix_(IK, IL)] for Pp in P]
        Bt = [Pp[np.ix_(IL, IK)] for Pp in P]
        D = [Pp[np.ix_(IL, IL)] for Pp in P]
        evD = np.linalg.eigvalsh(herm(D[0]))
        diag['D0_min_rel'] = float(np.abs(evD).min() / np.abs(evD).max())
        if diag['D0_min_rel'] < 1e-10:
            diag['grund'] = 'D0_singulaer'
            return None, diag
        E = [np.linalg.inv(D[0])]
        for p in range(1, pmax + 1):
            E.append(-E[0] @ sum(D[j] @ E[p - j] for j in range(1, p + 1)))
        S = []
        for p in range(pmax + 1):
            X = A[p].copy()
            for a in range(p + 1):
                for b in range(p + 1 - a):
                    X = X - B[a] @ E[b] @ Bt[p - a - b]
            S.append(X)
        return np.array(S), diag


def schur_reihe(S, IK, IL):
    """Schur-Komplement einer Taylor-Reihe S_p ueber IL (Reihe der Inversen)."""
    pmax = len(S) - 1
    A = [Sp[np.ix_(IK, IK)] for Sp in S]
    B = [Sp[np.ix_(IK, IL)] for Sp in S]
    Bt = [Sp[np.ix_(IL, IK)] for Sp in S]
    D = [Sp[np.ix_(IL, IL)] for Sp in S]
    evD = np.linalg.eigvalsh(herm(D[0]))
    kond = float(np.abs(evD).max() / max(np.abs(evD).min(), 1e-300))
    if kond > 1e12:
        return None, kond
    E = [np.linalg.inv(D[0])]
    for p in range(1, pmax + 1):
        E.append(-E[0] @ sum(D[j] @ E[p - j] for j in range(1, p + 1)))
    out = []
    for p in range(pmax + 1):
        X = A[p].copy()
        for a in range(p + 1):
            for b in range(p + 1 - a):
                X = X - B[a] @ E[b] @ Bt[p - a - b]
        out.append(X)
    return np.array(out), kond


# ================================================================================================= 3D-Seite
def kuhn3d():
    """Wie ukh.kuhn3d (UEBERLEITUNG-KH-1)."""
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
    return mod, geo, LV


def netz3d(netz):
    if netz == 'KW':
        return kuhn3d()
    LV, pos, G, O, info = hm.netz('V')
    mod = tg.modell(LV, pos, G, O, {})
    return mod, None, LV


class Zuordnung:
    """rk-Raumkante <-> tg-Kante (PLAN 6): q_rk = U q_tg."""

    def __init__(self, vier, mod, LV):
        ed = np.rint(mod['Tedge'] @ np.linalg.inv(LV)).astype(int)
        self.E = mod['E']
        self.i_rk, self.umg, self.R = [], [], []
        A3 = vier.g.A3
        for e in range(mod['E']):
            es, es2, d = int(mod['es'][e]), int(mod['es2'][e]), tuple(int(x) for x in ed[e])
            if (es, es2, d) in vier.ridx:
                self.i_rk.append(vier.ridx[(es, es2, d)]); self.umg.append(False); self.R.append(np.zeros(3))
            else:
                key = (es2, es, tuple(-x for x in d))
                self.i_rk.append(vier.ridx[key]); self.umg.append(True); self.R.append(A3 @ np.array(key[2], float))
        assert sorted(self.i_rk) == list(range(len(vier.raum)))
        self.R = np.array(self.R)

    def U(self, ks):
        U = np.zeros((self.E, self.E), complex)
        for e in range(self.E):
            U[self.i_rk[e], e] = np.exp(1j * (self.R[e] @ ks)) if self.umg[e] else 1.0
        return U


def M_disp_rk(vier, ks):
    g = vier.g
    M = np.zeros((vier.nq, 3 * vier.NV), complex)
    for i, e in enumerate(vier.raum):
        b1, b2 = g.b1[e], g.b2[e]
        u = vier.r_dx[i] / vier.r_dx2[i]                    # raeumlicher Anteil (Schichtkanten koennen geneigt sein)
        ph = np.exp(1j * (g.Rd[e, :3] @ ks))
        M[i, 3 * b2:3 * b2 + 3] += u * ph
        M[i, 3 * b1:3 * b1 + 3] -= u
    return M


# ================================================================================================= Grenzwert je k
def grenze(vl, ks, schema, pmax=2, voll=False):
    """S_p(h) fuer h in H7, Grenzwerte Q0, Q0', Q0'' und UV1-Kennzahlen."""
    Sh, dg = [], []
    for V in vl:
        S, d = V.bloecke(ks, schema, pmax)
        Sh.append(S); dg.append(d)
    if any(S is None for S in Sh):
        return {'undefiniert': True, 'grund': sorted(set(d.get('grund', '') for d in dg if d.get('grund'))),
                'rang_B_s': sorted(set(d['rang_B_s'] for d in dg)), 'n_L': sorted(set(d['n_L'] for d in dg)),
                'J_rang_ok': False}
    Sh = np.array(Sh)
    Q0 = np.einsum('j,jpab->pab', W_A, Sh[FIT_A])
    Q0p = np.einsum('j,jpab->pab', W_B, Sh[FIT_B])
    Q0pp = np.einsum('j,jpab->pab', W_C, Sh[FIT_C])
    V0 = vl[0]
    nq, NV = V0.nq, V0.NV
    IQ = list(range(nq)); IN = list(range(nq, nq + NV)); IB = list(range(nq + NV, nq + 4 * NV))
    bl = {'M': (2, IQ, IQ), 'V': (0, IQ, IQ), 'C': (0, IQ, IN), 'X': (1, IQ, IB)}
    uv1 = {}
    for nm, (p, I, Jx) in bl.items():
        ref = Sh[0, p][np.ix_(I, Jx)]
        dd = [fro(Sh[j, p][np.ix_(I, Jx)] - ref) / fro(ref) for j in range(len(vl))]
        uv1[nm] = {'d_je_h': dd, 'd': float(max(dd))}
    out = {'Q0': Q0, 'Q0p': Q0p, 'Q0pp': Q0pp, 'uv1': uv1,
           'D0_min_rel': float(min(d.get('D0_min_rel', 1.0) for d in dg)),
           'rang_B_s': sorted(set(d['rang_B_s'] for d in dg)), 'n_L': sorted(set(d['n_L'] for d in dg)),
           'J_sv_min_rel': float(min(d['J_sv_min_rel'] for d in dg)), 'J_rang_ok': bool(all(d['J_rang_ok'] for d in dg))}
    fe = {}
    for nm, (p, I, Jx) in bl.items():
        a = Q0[p][np.ix_(I, Jx)]
        fe[nm] = float(max(fro(a - Q0p[p][np.ix_(I, Jx)]), fro(a - Q0pp[p][np.ix_(I, Jx)])) / max(fro(a), 1e-300))
    out['e'] = fe
    if voll:
        out['Sh'] = Sh
    return out


# ================================================================================================= Regime H
def rest_proj(Y, x):
    if Y.size == 0:
        return 1.0
    U, s, _ = np.linalg.svd(Y, full_matrices=False)
    r = int((s > 1e-9 * s[0]).sum()) if s.size and s[0] > 0 else 0
    Q = U[:, :r]
    res = x - Q @ (np.conj(Q.T) @ x)
    return float(np.linalg.norm(res) / max(np.linalg.norm(x), 1e-300))


def reduktion(Meff, Bm, cv, Md, eps, tol_null, mit_vek=False):
    """PLAN 5, Schritte 1 bis 5 (bindend): statische Richtungen per Schur im Potential, dann R1."""
    out = {}
    ev, Uv = np.linalg.eigh(herm(Meff))
    smax = float(np.abs(ev).max())
    null = np.abs(ev) <= tol_null * smax
    nu = int(null.sum())
    out.update({'n_u': nu, 'M_min_rel': float(np.abs(ev).min() / smax), 'M_n_neg': int((ev < -tol_null * smax).sum())})
    nz = np.abs(ev[~null])
    out['M_min_nichtnull_rel'] = float(nz.min() / smax) if nz.size else None
    u, W = Uv[:, null], Uv[:, ~null]
    Um, sm, _ = np.linalg.svd(Md, full_matrices=False)
    rm = int((sm > 1e-9 * sm[0]).sum())
    Qm = Um[:, :rm]
    out['rang_Mdisp'] = rm
    if nu > 0:
        R = u - Qm @ (np.conj(Qm.T) @ u)
        sres = np.linalg.svd(R, compute_uv=False)
        out['n_ug'] = int((sres <= 1e-8).sum())
        if out['n_ug'] > 0:
            out.update({'definiert': False, 'grund': 'statisch_mit_eichanteil'})
            return out
        Buu = herm(np.conj(u.T) @ Bm @ u)
        eu = np.linalg.eigvalsh(Buu)
        out['Buu_kond'] = float(np.abs(eu).max() / max(np.abs(eu).min(), 1e-300))
        out['Buu_n_neg'] = int((eu < 0).sum())
        if out['Buu_kond'] > 1e10:
            out.update({'definiert': False, 'grund': 'Buu_singulaer'})
            return out
        Bwu = np.conj(W.T) @ Bm @ u
        Tsl = -np.linalg.solve(Buu, np.conj(Bwu.T))         # s = Tsl p
        Bp = herm(np.conj(W.T) @ Bm @ W + Bwu @ Tsl)
        cp = np.conj(W.T) @ cv + np.conj(Tsl.T) @ (np.conj(u.T) @ cv)
        Mdp = np.conj(W.T) @ Md
        Ap = np.diag(1.0 / ev[~null])
        Mp = np.diag(ev[~null])
    else:
        out['n_ug'] = 0
        W = np.eye(Meff.shape[0]); Tsl = None
        Bp, cp, Mdp = herm(Bm), cv, Md
        Mp = herm(Meff)
        Ap = np.linalg.inv(Mp)
    S, Q, Cn, weg, svrel = hm.zerlege(Mdp, cp)
    Sh = np.conj(S.T)
    Ar = herm(Sh @ Ap @ S)
    Br = herm(Sh @ Bp @ S)
    dim = int(S.shape[1])
    out.update({'definiert': True, 'dim_red': dim, 'weg': weg, 'pass_rest': rest_proj(Mp @ Mdp, cp)})
    eA = np.linalg.eigvalsh(Ar)
    out['A_red_n_neg'] = int((eA < -1e-12 * np.abs(eA).max()).sum())
    if dim == 0:
        out.update({'ok': False, 'n_wachsend': 0, 'w2k2': None})
        return out
    try:
        L = np.linalg.cholesky(Br)
        out['B_red_pd'] = True
        Mh = herm(np.conj(L.T) @ Ar @ L)
        if mit_vek:
            w2, Y = np.linalg.eigh(Mh)
        else:
            w2 = np.linalg.eigvalsh(Mh)
        w2c = w2.astype(complex)
    except np.linalg.LinAlgError:
        out['B_red_pd'] = False
        eB = np.linalg.eigvalsh(Br)
        out['B_red_n_neg'] = int((eB < 0).sum())
        w2c = np.linalg.eigvals(Ar @ Br)
        L, Y = None, None
    s = max(float(np.abs(w2c).max()), 1e-300)
    wachs = (w2c.real < -TOL_W * s) | (np.abs(w2c.imag) > TOL_W * s)
    out['n_wachsend'] = int(wachs.sum())
    out['w2_min_rel'] = float(w2c.real.min() / s)
    out['w2_im_max_rel'] = float(np.abs(w2c.imag).max() / s)
    o = np.argsort(np.abs(w2c))
    top = w2c[o[:2]]
    out['pos2'] = bool(len(top) == 2 and np.all(top.real > 0) and np.all(np.abs(top.imag) <= TOL_W * s))
    out['luecke'] = float(abs(w2c[o[1]]) / abs(w2c[o[2]])) if dim > 2 else 0.0
    out['ok'] = bool(out['pos2'] and out['luecke'] < LUECKE_MAX)
    out['w2k2'] = sorted(float(x.real) / eps ** 2 for x in top) if len(top) == 2 else None
    out['w2_klein'] = [float(x.real) / eps ** 2 for x in sorted(w2c, key=lambda z: z.real)[:4]]
    if mit_vek and L is not None:
        Li = sla.solve_triangular(L, np.eye(L.shape[0]), lower=True)
        vek = []
        for j in o[:2]:
            x = np.conj(Li.T) @ Y[:, j]
            p = S @ x
            q = W @ p + (u @ (Tsl @ p) if Tsl is not None else 0.0)
            vek.append(q)
        out['_vek'] = vek
    return out


def tt_anteil(mod, vek, ks, M):
    tt = []
    for q in vek:
        H, rr = tg.tensor_fit(mod, q, ks, M)
        tt.append(float(tp.tt_anteil(H, ks)[0]))
    return tt


def punkt(vl, mod, geo, zu, ks, schemata, haupt, kontr_3d=False, mit_tt=False):
    """Ein k: Grenzform je Schema, Kennzahlen (PLAN 3, 4, 9), Paarungen (PLAN 5)."""
    t0 = time.time()
    eps = float(np.linalg.norm(ks))
    Bs, A1s, M, c = tg.ops(mod, ks)
    B = herm(Bs.toarray())
    U = zu.U(ks)
    UH = np.conj(U.T)
    V0 = vl[0]
    nq, NV = V0.nq, V0.NV
    IQ = list(range(nq)); IN = list(range(nq, nq + NV)); IB = list(range(nq + NV, nq + 4 * NV))
    out = {'k': [float(x) for x in ks], 'eps': eps}
    Mrk = M_disp_rk(V0, ks)
    out['K4_Mdisp'] = fro(UH @ Mrk - M) / fro(M)
    for sch in schemata:
        gz = grenze(vl, ks, sch)
        if gz.get('undefiniert'):
            nd = {'definiert': False, 'grund': 'schema:' + ','.join(gz['grund'])}
            sp = {'a': dict(nd), 'a_Q0p': dict(nd)}
            if sch == haupt:
                sp['a_C'] = dict(nd); sp['a_V'] = dict(nd)
            out[sch] = {'undefiniert': True, 'grund': gz['grund'], 'rang_B_s': gz['rang_B_s'], 'n_L': gz['n_L'],
                        'J_rang_ok': False, 'uv1': None, 'e': None, 'tol_null': None, 'sp': sp}
            continue
        r = {'uv1': gz['uv1'], 'e': gz['e'], 'D0_min_rel': gz['D0_min_rel'], 'rang_B_s': gz['rang_B_s'],
             'n_L': gz['n_L'], 'J_sv_min_rel': gz['J_sv_min_rel'], 'J_rang_ok': gz['J_rang_ok']}
        tol_null = max(1e-10, 100.0 * gz['e']['M'])
        r['tol_null'] = tol_null
        Z = {}
        for tag in ('Q0', 'Q0p'):
            S = gz[tag]
            Meff = herm(UH @ S[2][np.ix_(IQ, IQ)] @ U)
            Veff = herm(UH @ S[0][np.ix_(IQ, IQ)] @ U)
            Cv = UH @ S[0][np.ix_(IQ, IN)]
            X = UH @ S[1][np.ix_(IQ, IB)]
            Z[tag] = (S, Meff, Veff, Cv, X)
        S, Meff, Veff, Cv, X = Z['Q0']
        r['Meff_herm'] = fro(S[2][np.ix_(IQ, IQ)] - np.conj(S[2][np.ix_(IQ, IQ)].T)) / fro(S[2][np.ix_(IQ, IQ)])
        ev = np.linalg.eigvalsh(Meff)
        r['Meff_eig'] = [float(x) for x in ev]
        r['r_V'] = fro(Veff - B) / fro(B)
        r['VM_null'] = fro(Veff @ M) / (fro(Veff) * fro(M))
        # C gegen c
        Qc, _ = np.linalg.qr(c)
        QC, _ = np.linalg.qr(Cv)
        r['sin_Cc'] = float(np.linalg.norm(QC - Qc @ (np.conj(Qc.T) @ QC), 2))
        kap = np.vdot(c, Cv) / np.vdot(c, c)
        r['kappa_Cc'] = [float(kap.real), float(kap.imag)]
        r['C_rest_kappa'] = fro(Cv - kap * c) / fro(Cv)
        # Regeln (PLAN 9)
        sig = max(fro(S[p]) * eps ** p for p in range(3))
        lap = [fro(S[0][np.ix_(IN, IN)]), fro(S[1][np.ix_(IN, IN)]) * eps,
               fro(S[2][np.ix_(IN, IN)]) * eps ** 2, fro(S[1][np.ix_(IQ, IN)]) * eps, fro(S[2][np.ix_(IQ, IN)]) * eps ** 2]
        lap += [fro(S[p][np.ix_(IN, IB)]) * eps ** p for p in range(3)]
        r['R_L'] = float(max(lap) / sig)
        Gk = UH @ S[1][np.ix_(IQ, IQ)] @ U
        r['R_K'] = fro(Gk) * eps / sig
        MM = Meff @ M
        Y, *_ = np.linalg.lstsq(MM, X, rcond=None)
        r['R_S_rest'] = fro(X - MM @ Y) / max(fro(X), 1e-300)
        Sbb = S[0][np.ix_(IB, IB)]
        r['R_S_bb'] = fro(Sbb - np.conj(Y.T) @ np.conj(M.T) @ Meff @ M @ Y) / max(fro(Sbb), 1e-300)
        r['R_S_hoeher'] = float(max(fro(S[2][np.ix_(IQ, IB)]) * eps ** 2, fro(S[1][np.ix_(IB, IB)]) * eps,
                                    fro(S[2][np.ix_(IB, IB)]) * eps ** 2) / sig)
        # Lage der Nullrichtungen
        smax = float(np.abs(ev).max())
        evv, Uv = np.linalg.eigh(Meff)
        null = np.abs(evv) <= tol_null * smax
        if null.any():
            u = Uv[:, null]
            r['uC_rel'] = fro(np.conj(u.T) @ Cv) / fro(Cv)
            r['uc_rel'] = fro(np.conj(u.T) @ c) / fro(c)
            r['uX_rel'] = fro(np.conj(u.T) @ X) / max(fro(X), 1e-300)
            r['uG_rel'] = fro(np.conj(u.T) @ Gk) / max(fro(Gk), 1e-300)
            r['uM_rel'] = fro(np.conj(u.T) @ M) / fro(M)
            if geo is not None:
                e111 = [e for e in range(mod['E'])
                        if tuple(int(abs(round(y))) for y in mod['n'][e] * mod['l'][e]) == (1, 1, 1)][0]
                r['u_111'] = float(np.sum(np.abs(u[e111]) ** 2))
        # M_perp (schemafrei, PLAN 4)
        Sp2, kond = schur_reihe(S, IQ + IN, IB)
        r['Dbb_kond'] = kond
        if Sp2 is not None:
            Mperp = herm(UH @ Sp2[2][np.ix_(IQ, IQ)] @ U)
            ep = np.abs(np.linalg.eigvalsh(Mperp))
            nperp = int((ep <= tol_null * ep.max()).sum())
            Um_, sm_, _ = np.linalg.svd(M, full_matrices=False)
            r['n_u_perp'] = nperp - int((sm_ > 1e-9 * sm_[0]).sum())
            r['Mperp_M_rel'] = fro(Mperp @ M) / (fro(Mperp) * fro(M))
        # UV0-Groesse (Kuhn)
        if geo is not None:
            K_LR = herm(geo['vref'] * hm.assemble(mod, geo['Kt'], ks))
            r['r_UV0'] = fro(Meff - K_LR) / fro(K_LR)
        # Paarungen
        sp = {}
        rv = reduktion(Meff, B, c, M, eps, tol_null, mit_vek=mit_tt)
        vek = rv.pop('_vek', None)
        if mit_tt and vek is not None:
            rv["tt_anteil"] = tt_anteil(mod, vek, ks, M)
        sp['a'] = rv
        S2, Meff2, Veff2, Cv2, X2 = Z['Q0p']

        sp['a_Q0p'] = reduktion(Meff2, B, c, M, eps, tol_null)
        if sch == haupt:
            sp['a_C'] = reduktion(Meff, B, Cv, M, eps, tol_null)
            sp['a_V'] = reduktion(Meff, Veff, c, M, eps, tol_null)
        for v in sp.values():
            v.pop('_vek', None)
        r['sp'] = sp
        out[sch] = r
    out['t_s'] = time.time() - t0
    return out


# ================================================================================================= k-Mengen
def raster(lm):
    pts = []
    for ir, (nm, d) in enumerate(tti.richtungen13()):
        for kl in KL_RASTER:
            pts.append({'ridx': ir, 'richtung': nm, 'kl': kl, 'art': 'kl', 'ks': (kl / lm) * d})
        for e in EPS_HM:
            pts.append({'ridx': ir, 'richtung': nm, 'kl': e * lm, 'art': 'hm', 'betrag_hm': e, 'ks': e * d})
    return pts


def bz(LV, teil=None):
    BVc = 2 * np.pi * np.linalg.inv(LV).T
    ms = [m for m in itertools.product(range(8), repeat=3) if any(m)]
    if teil == 0:
        ms = ms[:256]
    elif teil == 1:
        ms = ms[256:]
    pts = [{'m': list(m), 'art': 'bz', 'rand': bool(any(x == 4 for x in m)), 'ks': (np.array(m, float) / 8) @ BVc}
           for m in ms]
    return pts


def extra_V():
    return [{'m': None, 'art': 'bz_extra', 'name': nm, 'rand': True, 'ks': 2 * np.pi * np.array(v, float)}
            for nm, v in (('K', (0.75, 0.75, 0.0)), ('U', (1.0, 0.25, 0.25)))]


# ================================================================================================= Kontrollen
def kontrollen(vl, mod, LV, zu):
    rng = np.random.default_rng(20261005)
    out = {}
    for V in (vl[0], vl[-1]):
        g = V.g
        k1 = k2 = 0.0
        for _ in range(6):
            k = rng.uniform(-np.pi, np.pi, 4)
            k[3] = rng.uniform(-np.pi, np.pi) / V.h
            C = V.lau.koeff(k[:3])
            z = np.exp(1j * k[3] * V.h)
            Hl = sum(Cm * z ** m for m, Cm in C.items())
            Hr = g.H(k)
            k1 = max(k1, float(np.abs(Hl - Hr).max() / np.abs(Hr).max()))
            kt = k[3] + 1j * rng.uniform(-2, 2) / V.h
            Hc = sum(Cm * np.exp(1j * kt * V.h) ** m for m, Cm in C.items())
            Gk = rk2.G_batch(g, np.r_[k[:3], kt][None, :])[0]
            k2 = max(k2, float(np.linalg.norm(Hc @ Gk) / (np.linalg.norm(Hc) * np.linalg.norm(Gk))))
        out['h=%g' % V.h] = {'K1': k1, 'K2': k2}
    k3 = {}
    for V in vl:
        kk = V.g.kontrollen()
        k3['%g' % V.h] = {x: kk[x] for x in ('fehlwinkel_max_abs', 'schlaefli', 'M_sym', 'vol_summe_rel_fehler',
                                              'vol_min_rel', 'tote_kanten', 'NE', 'S')}
    out['K3'] = k3
    kz = rng.uniform(-np.pi, np.pi, 3)
    Bs, A1s, M, c = tg.ops(mod, kz)
    out['K3_3d_ops'] = tg.kontr_ops(Bs, A1s, M, c)
    out['K3_3d_pruefung'] = {x: mod['pruefung'][x] for x in ('T', 'E', 'nV', 'dieder_summe_minus_2pi_max', 'Vbox')}
    out['K4_Mdisp_zufall'] = fro(np.conj(zu.U(kz).T) @ M_disp_rk(vl[0], kz) - M) / fro(M)
    out['struktur'] = {'NE': vl[0].NE, 'NV': vl[0].NV, 'nq': vl[0].nq, 'n_diag': len(vl[0].diag),
                       'dt': sorted(set(vl[0].dt.tolist())), 'tot': sorted(vl[0].tot),
                       'n_lebend_diag': int(vl[0].lebend.sum())}
    return out


# ================================================================================================= Laeufe
def bau(netz):
    t0 = time.time()
    vl = [Vier(netz, h) for h in H7]
    mod, geo, LV = netz3d(netz)
    zu = Zuordnung(vl[0], mod, LV)
    return vl, mod, geo, LV, zu, time.time() - t0


def lauf_punkte(vl, mod, geo, zu, pts, schemata, haupt, tt_richt=()):
    out = []
    for p in pts:
        ks = p['ks']
        mit_tt = p.get('art') == 'kl' and p.get('kl') == 0.01 and p.get('richtung') in tt_richt
        r = punkt(vl, mod, geo, zu, ks, schemata, haupt, mit_tt=mit_tt)
        r.update({x: y for x, y in p.items() if x != 'ks'})
        out.append(r)
    return out


def lauf_rauch1(netz):
    vl, mod, geo, LV, zu, tb = bau(netz)
    out = {'t_aufbau_s': tb, 'kontrollen': kontrollen(vl, mod, LV, zu)}
    lm = float(mod['l'].mean())
    out['l_mittel'] = lm
    tech = []
    schemata = ('achse', 'ls') if netz == 'KW' else ('ls', 'ls2', 'lsa')
    pts = raster(lm)[::17][:3] + bz(LV)[::200][:3]
    for p in pts:
        for sch in schemata:
            t = time.time()
            ds = [V.bloecke(p['ks'], sch)[1] for V in vl]
            tech.append({'schema': sch, 'art': p['art'], 'D0_min_rel': float(min(d.get('D0_min_rel', 1.0) for d in ds)),
                         'rang_B_s': sorted(set(d['rang_B_s'] for d in ds)), 'n_L': sorted(set(d['n_L'] for d in ds)),
                         'J_sv_min_rel': float(min(d['J_sv_min_rel'] for d in ds)),
                         'J_rang_ok': bool(all(d['J_rang_ok'] for d in ds)), 't_s': time.time() - t})
    out['technik'] = tech
    t = time.time()
    r = punkt(vl, mod, geo, zu, pts[0]['ks'], schemata, schemata[0] if netz == 'KW' else 'ls')
    out['t_punkt_s'] = time.time() - t
    out['punkt_schluessel'] = sorted(r.keys())
    return out


def lauf_hoeher(netz):
    vl, mod, geo, LV, zu, tb = bau(netz)
    lm = float(mod['l'].mean())
    R = dict((nm, d) for nm, d in tti.richtungen13())
    ks_l = [(0.05 / lm) * R['100'], (0.2 / lm) * R['100'], (0.1 / lm) * R['321'], bz(LV)[100]['ks']]
    V0 = vl[0]
    nq, NV = V0.nq, V0.NV
    bl = {'qq': (list(range(nq)), list(range(nq))), 'qn': (list(range(nq)), list(range(nq, nq + NV))),
          'qb': (list(range(nq)), list(range(nq + NV, nq + 4 * NV))),
          'nn': (list(range(nq, nq + NV)), list(range(nq, nq + NV))),
          'nb': (list(range(nq, nq + NV)), list(range(nq + NV, nq + 4 * NV))),
          'bb': (list(range(nq + NV, nq + 4 * NV)), list(range(nq + NV, nq + 4 * NV)))}
    out = []
    for ks in ks_l:
        z = {'k': [float(x) for x in ks]}
        Sh = [V.bloecke(ks, 'ls', pmax=4)[0] for V in vl]
        for p in range(5):
            for nm, (I, Jx) in bl.items():
                z['S%d_%s' % (p, nm)] = [fro(Sh[j][p][np.ix_(I, Jx)]) for j in range(len(vl))]
        out.append(z)
    return {'punkte': out, 'h': H7}


# ================================================================================================= Auswertung
def fit_kl(kls, ws):
    x = np.asarray(kls, float) ** 2
    Am = np.stack([np.ones_like(x), x, x ** 2], 1)
    cf, *_ = np.linalg.lstsq(Am, np.asarray(ws, float), rcond=None)
    return cf


def spanne(pts, sch, var):
    W = {}
    for p in pts:
        if p.get('art') != 'kl':
            continue
        r = p[sch]['sp'][var]
        ok = bool(r.get('definiert') and r.get('ok') and r.get('w2k2') is not None)
        W[(p['ridx'], p['kl'])] = (ok, r['w2k2'] if ok else [np.nan, np.nan])
    if not W:
        return None
    nr = 1 + max(i for i, _ in W)
    je = {}
    for kl in KL_RASTER:
        ww = np.array([W.get((i, kl), (False, [np.nan, np.nan]))[1] for i in range(nr)], float)
        oks = [W.get((i, kl), (False, None))[0] for i in range(nr)]
        je['%g' % kl] = {'spanne': float(np.nanmax(ww) / np.nanmin(ww) - 1) if np.isfinite(ww).any() else None,
                         'n_ok': int(sum(oks))}
    w0, alle_ok = [], True
    for i in range(nr):
        for b in range(2):
            ws = [W.get((i, kl), (False, [np.nan, np.nan]))[1][b] for kl in KL_FIT]
            alle_ok &= all(W.get((i, kl), (False, None))[0] for kl in KL_FIT)
            if np.all(np.isfinite(ws)):
                w0.append(fit_kl(KL_FIT, ws)[0])
    w0 = np.array(w0)
    s0 = float(w0.max() / w0.min() - 1) if len(w0) and w0.min() > 0 else None
    hmw = [x for p in pts if p.get('art') == 'hm' and p[sch]['sp'][var].get('ok') for x in p[sch]['sp'][var]['w2k2']]
    return {'spanne0': s0, 'alle_ok_fit': bool(alle_ok), 'w0_min': float(w0.min()) if len(w0) else None,
            'w0_max': float(w0.max()) if len(w0) else None, 'je_kl': je,
            'spanne_hm': float(max(hmw) / min(hmw) - 1) if hmw and min(hmw) > 0 else None,
            'n_hm_ok': int(sum(1 for p in pts if p.get('art') == 'hm' and p[sch]['sp'][var].get('ok')))}


def zaehle(pts, sch, var):
    nd, nund, nw, gr = 0, 0, 0, {}
    orte = []
    for p in pts:
        if var not in p[sch]['sp']:
            continue
        r = p[sch]['sp'][var]
        if not r.get('definiert'):
            nund += 1
            g = r.get('grund', '?')
            gr[g] = gr.get(g, 0) + 1
            continue
        nd += 1
        if r.get('n_wachsend', 0) > 0:
            nw += 1
            if len(orte) < 12:
                orte.append(p.get('m') or p.get('name') or [p.get('richtung'), p.get('kl')])
    return {'k_definiert': nd, 'k_nicht_definiert': nund, 'gruende': gr, 'k_wachsend': nw, 'orte': orte}


def mm(xs):
    xs = [x for x in xs if x is not None]
    return [float(min(xs)), float(max(xs))] if xs else None


def lauf_auswertung(pfade):
    J = {nm: json.load(open(p)) for nm, p in pfade.items()}
    out = {'eingaben': {nm: {'pfad': p, 'sha256': sha(p), 'skript': J[nm]['info']['skript_sha256']}
                        for nm, p in pfade.items()}}
    U = {}
    # ---------------- UV0 (Kuhn, Schema achse)
    kw = J['kw']['ergebnis']
    kp = kw['raster'] + kw['bz']
    rr = [p['achse'].get('r_UV0') for p in kp]
    red = [p for p in kw['raster'] if p['art'] == 'kl'] + [p for p in kw['bz'] if not p['rand']]
    a_ok = [p['achse']['sp']['a'] for p in red]
    t2 = all(r.get('definiert') and r.get('n_u') == 1 and r.get('dim_red') == 2 for r in a_ok)
    t2b = all(p['achse'].get('u_111', 0) >= 0.999 for p in red)
    sp_kw = spanne(kw['raster'], 'achse', 'a')
    t1 = all(x is not None and 0.745 <= x < 0.775 for x in rr)
    t1w = all(x is not None and 0.75 <= x <= 0.77 for x in rr)
    t3 = sp_kw is not None and sp_kw['alle_ok_fit'] and sp_kw['spanne0'] is not None and sp_kw['spanne0'] < 1e-8
    u0 = 'eingetroffen' if (t1 and t2 and t2b and t3) else 'nicht eingetroffen'
    u0w = 'eingetroffen' if (t1w and t2 and t2b and t3) else 'nicht eingetroffen'
    U['UV0'] = {'plan': u0, 'karte': u0 if u0 == u0w else 'unklar', 'karte_woertlich_r': u0w,
                'r_min_max': mm(rr), 'r_teil_gerundet': t1, 'r_teil_woertlich': t1w,
                'reduktion_n_u1_dim2': t2, 'u111_ge_0999': t2b, 'u111_min': min(p['achse'].get('u_111', 0) for p in red),
                'spanne0': sp_kw['spanne0'] if sp_kw else None, 'spanne_ok_fit': sp_kw['alle_ok_fit'] if sp_kw else None,
                'n_red_k': len(red), 'wachsend_red': sum(1 for r in a_ok if r.get('n_wachsend', 0) > 0)}
    # Kuhn beschreibend: Schema ls, Rand
    out['kuhn'] = {'achse': {'wachsend_raster': zaehle(kw['raster'], 'achse', 'a'), 'wachsend_bz': zaehle(kw['bz'], 'achse', 'a'),
                             'wachsend_bz_rand': zaehle([p for p in kw['bz'] if p['rand']], 'achse', 'a'),
                             'spanne_a': sp_kw, 'n_u': mm([p['achse']['sp']['a'].get('n_u') for p in kp]),
                             'n_u_perp': mm([p['achse'].get('n_u_perp') for p in kp])},
                   'ls': {'wachsend_raster': zaehle(kw['raster'], 'ls', 'a'), 'wachsend_bz': zaehle(kw['bz'], 'ls', 'a'),
                          'spanne_a': spanne(kw['raster'], 'ls', 'a'), 'n_u': mm([p['ls']['sp']['a'].get('n_u') for p in kp]),
                          'n_u_perp': mm([p['ls'].get('n_u_perp') for p in kp]),
                          'r_UV0': mm([p['ls'].get('r_UV0') for p in kp])}}
    # ---------------- V
    vr = J['vraster']['ergebnis']['raster']
    vb = J['vbz0']['ergebnis']['bz'] + J['vbz1']['ergebnis']['bz']
    alle = vr + vb
    # UV1
    defp = [p for p in alle if not p['ls'].get('undefiniert')]
    dmax = {nm: max(p['ls']['uv1'][nm]['d'] for p in defp) for nm in ('M', 'V', 'C', 'X')}
    undef1 = sum(1 for p in alle if p['ls'].get('undefiniert') or not p['ls']['J_rang_ok'] or p['ls']['rang_B_s'] != [30])
    if max(dmax.values()) > 1e-10:
        u1 = 'nicht eingetroffen'
    elif undef1:
        u1 = 'nicht entscheidbar'
    else:
        u1 = 'eingetroffen'
    dje = {nm: [max(p['ls']['uv1'][nm]['d_je_h'][j] for p in defp) for j in range(len(H7))] for nm in ('M', 'V', 'C', 'X')}
    U['UV1'] = {'plan': u1, 'karte': u1, 'd_max': dmax, 'd_max_je_h': dje, 'k_schema_undefiniert': undef1,
                'e_max': {nm: max(p['ls']['e'][nm] for p in defp) for nm in ('M', 'V', 'C', 'X')}}
    # UV2
    nus = [p['ls']['sp']['a'].get('n_u') for p in alle]
    klar_reg = [p for p in alle if p['ls']['sp']['a'].get('n_u') == 0
                and p['ls']['sp']['a']['M_min_rel'] >= 100 * p['ls']['tol_null']]
    n_unsicher = int(sum(1 for p in alle if (p["ls"].get("tol_null") or 0) > 1e-6))
    if all(x is not None and x >= 1 for x in nus) and n_unsicher == 0:
        u2 = 'eingetroffen'
    elif klar_reg:
        u2 = 'nicht eingetroffen'
    else:
        u2 = 'nicht entscheidbar'
    vert = {}
    for x in nus:
        vert[str(x)] = vert.get(str(x), 0) + 1
    vperp = {}
    for p in alle:
        x = p['ls'].get('n_u_perp')
        vperp[str(x)] = vperp.get(str(x), 0) + 1
    U['UV2'] = {'plan': u2, 'karte': u2, 'k_tol_unsicher': n_unsicher, 'n_u_verteilung': vert, 'n_u_perp_verteilung': vperp,
                'n_u_gleich_n_u_perp': int(sum(1 for p in alle if p['ls']['sp']['a'].get('n_u') == p['ls'].get('n_u_perp'))),
                'k_klar_regulaer': len(klar_reg), 'M_min_rel': mm([p['ls']['sp']['a'].get('M_min_rel') for p in alle]),
                'M_min_nichtnull_rel': mm([p['ls']['sp']['a'].get('M_min_nichtnull_rel') for p in alle]),
                'tol_null': mm([p['ls']['tol_null'] for p in alle]),
                'M_n_neg': mm([p['ls']['sp']['a'].get('M_n_neg') for p in alle]),
                'ls2_n_u': mm([p['ls2']['sp']['a'].get('n_u') for p in vr if 'ls2' in p]),
                'ls2_n_u_perp': mm([p['ls2'].get('n_u_perp') for p in vr if 'ls2' in p])}
    # UV3
    s_a = spanne(vr, 'ls', 'a')
    s_ap = spanne(vr, 'ls', 'a_Q0p')
    if s_a is None or s_ap is None or not s_a['alle_ok_fit'] or s_a['spanne0'] is None or s_ap['spanne0'] is None:
        u3, delta = 'nicht entscheidbar', None
    else:
        delta = abs(s_a['spanne0'] - s_ap['spanne0'])
        if s_a["spanne0"] + delta < 1e-6 and n_unsicher == 0:
            u3 = 'eingetroffen'
        elif s_a['spanne0'] - delta >= 1e-6:
            u3 = 'nicht eingetroffen'
        else:
            u3 = 'nicht entscheidbar'
    U['UV3'] = {'plan': u3, 'karte': u3, 'spanne_a': s_a, 'spanne_a_Q0p': s_ap, 'delta': delta}
    # UV4
    def gruppe(L):
        return {'a': zaehle(L, 'ls', 'a'), 'a_Q0p': zaehle(L, 'ls', 'a_Q0p')}
    w_alle = gruppe(alle)
    beide = sum(1 for p in alle if p['ls']['sp']['a'].get('definiert') and p['ls']['sp']['a_Q0p'].get('definiert')
                and p['ls']['sp']['a'].get('n_wachsend', 0) > 0 and p['ls']['sp']['a_Q0p'].get('n_wachsend', 0) > 0)
    undef = w_alle['a']['k_nicht_definiert'] + w_alle['a_Q0p']['k_nicht_definiert']
    if beide > 0:
        u4 = 'nicht eingetroffen'
    elif undef == 0 and n_unsicher == 0 and w_alle["a"]["k_wachsend"] == 0 and w_alle["a_Q0p"]["k_wachsend"] == 0:
        u4 = 'eingetroffen'
    else:
        u4 = 'nicht entscheidbar'
    U['UV4'] = {'plan': u4, 'karte': u4, 'k_gesamt': len(alle), 'k_wachsend_beide': beide, 'alle': w_alle,
                'raster': gruppe(vr), 'bz_rand': gruppe([p for p in vb if p.get('rand')]),
                'bz_innen': gruppe([p for p in vb if not p.get('rand')]),
                'max_wachsend_je_k': max(p['ls']['sp']['a'].get('n_wachsend', 0) for p in alle)}
    out['urteile'] = U
    # beschreibend
    def kz(key, L=alle, sch='ls'):
        return mm([p[sch].get(key) for p in L])
    out['regeln_V'] = {k: kz(k) for k in ('R_L', 'R_K', 'R_S_rest', 'R_S_bb', 'R_S_hoeher', 'r_V', 'VM_null', 'sin_Cc',
                                          'C_rest_kappa', 'Meff_herm', 'D0_min_rel', 'J_sv_min_rel', 'Dbb_kond',
                                          'Mperp_M_rel', 'uC_rel', 'uc_rel', 'uX_rel', 'uG_rel', 'uM_rel')}
    out['regeln_V']['kappa_Cc_re'] = mm([p['ls']['kappa_Cc'][0] for p in defp])
    out['regeln_V']['kappa_Cc_im'] = mm([p['ls']['kappa_Cc'][1] for p in defp])
    out['regeln_V']['K4_Mdisp'] = mm([p['K4_Mdisp'] for p in alle])
    out['regeln_V_rand'] = {k: kz(k, [p for p in vb if p.get('rand')]) for k in ('R_S_rest', 'R_S_bb', 'R_K', 'uC_rel', 'uX_rel')}
    out['paarungen_V'] = {}
    for var in ('a', 'a_Q0p', 'a_C', 'a_V'):
        out['paarungen_V'][var] = {'spanne': spanne(vr, 'ls', var), 'wachsend': zaehle(alle, 'ls', var),
                                   'dim_red': mm([p['ls']['sp'][var].get('dim_red') for p in alle]),
                                   'pass_rest': mm([p['ls']['sp'][var].get('pass_rest') for p in alle]),
                                   'B_red_nicht_pd': int(sum(1 for p in alle if p['ls']['sp'][var].get('B_red_pd') is False)),
                                   'A_red_n_neg': mm([p['ls']['sp'][var].get('A_red_n_neg') for p in alle])}
    out['paarungen_V']['a_s'] = {'spanne': spanne(vr, 'ls2', 'a'), 'wachsend': zaehle(vr, 'ls2', 'a')}
    out['paarungen_V']['a_lsa'] = {'spanne': spanne(vr, 'lsa', 'a'), 'wachsend': zaehle(vr, 'lsa', 'a')}
    out['uv1_varianten_raster'] = {}
    for sch in ('ls', 'ls2', 'lsa'):
        dp = [p for p in vr if not p[sch].get('undefiniert')]
        out['uv1_varianten_raster'][sch] = {
            'd_max': {nm: max(p[sch]['uv1'][nm]['d'] for p in dp) for nm in ('M', 'V', 'C', 'X')} if dp else None,
            'd_max_je_h': {nm: [max(p[sch]['uv1'][nm]['d_je_h'][j] for p in dp) for j in range(len(H7))]
                           for nm in ('M', 'V', 'C', 'X')} if dp else None,
            'k_undefiniert': len(vr) - len(dp),
            'n_u': mm([p[sch]['sp']['a'].get('n_u') for p in vr]), 'n_u_perp': mm([p[sch].get('n_u_perp') for p in vr])}
    out['tt_anteil'] = [{'richtung': p['richtung'], 'tt': p['ls']['sp']['a'].get('tt_anteil')} for p in vr
                        if p['ls']['sp']['a'].get('tt_anteil') is not None]
    out['kontrollen'] = {nm: J[nm]['ergebnis'].get('kontrollen') for nm in ('kw', 'vraster')}
    return out


# ================================================================================================= main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch1', 'kw', 'vraster', 'vbz', 'hoeher', 'auswertung'])
    ap.add_argument('--netz', default='V', choices=['V', 'KW'])
    ap.add_argument('--teil', type=int, default=0)
    ap.add_argument('--probe', action='store_true', help='Codeprobe mit wenigen k (Werte nicht ansehen)')
    ap.add_argument('--ein', nargs='*', default=[])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'skript_sha256': sha(os.path.abspath(__file__)),
            'module_sha256': {nm: sha(os.path.abspath(sys.modules[nm].__file__))
                              for nm in ('rk', 'pt', 'rk2', 'ew', 'tp', 'tg', 'hm', 'tti', 'dn', 'nachtrag_kinetik')
                              if nm in sys.modules}}
    if a.modus == 'auswertung':
        erg = lauf_auswertung(dict(x.split('=', 1) for x in a.ein))
    elif a.modus == 'rauch1':
        erg = lauf_rauch1(a.netz)
    elif a.modus == 'hoeher':
        erg = lauf_hoeher('V')
    else:
        netz = 'KW' if a.modus == 'kw' else 'V'
        vl, mod, geo, LV, zu, tb = bau(netz)
        info['t_aufbau_s'] = tb
        lm = float(mod['l'].mean())
        erg = {'l_mittel': lm}
        if a.modus == 'kw':
            ras = raster(lm)
            bzp = bz(LV)
            if a.probe:
                ras, bzp = ras[:3], bzp[:3]
            erg['raster'] = lauf_punkte(vl, mod, geo, zu, ras, ('achse', 'ls'), 'achse')
            erg['bz'] = lauf_punkte(vl, mod, geo, zu, bzp, ('achse', 'ls'), 'achse')
            erg['kontrollen'] = kontrollen(vl, mod, LV, zu)
        elif a.modus == 'vraster':
            ras = raster(lm)
            if a.probe:
                ras = ras[:3]
            erg['raster'] = lauf_punkte(vl, mod, geo, zu, ras, ('ls', 'ls2', 'lsa'), 'ls', tt_richt=('100', '110', '111'))
            erg['kontrollen'] = kontrollen(vl, mod, LV, zu)
        else:
            pts = bz(LV, a.teil) + (extra_V() if a.teil == 1 else [])
            if a.probe:
                pts = pts[:2] + (extra_V()[:1] if a.teil == 1 else [])
            erg['bz'] = lauf_punkte(vl, mod, geo, zu, pts, ('ls',), 'ls')
            erg['teil'] = a.teil
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
