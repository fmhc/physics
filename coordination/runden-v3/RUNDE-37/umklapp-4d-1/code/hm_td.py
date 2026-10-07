#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HODGE-MASSE-1, Frage 3: Umklapp-Aufbau von TAKT-DYNAMIK-1 (td.py, unveraendert importiert) mit anderer
Bewegungsenergie und wahlweise horizontaler Reduktion.

Aufruf wie td.py lauf, zusaetzlich --kin {A1, A2, A2L} und --red {R1, RH}:
  A1 : A = sum_t A0_t (TAKT-DYNAMIK-1, J = 1)
  A2 : A = sum_t (Vref / V_t) A0_t (Kartenformel, Hamilton-additiv)
  A2L: K = sum_t (V_t / Vref) Phi_t^-T (1 - TR TR^T) Phi_t^-1, A = K^-1 (Lagrange-additiv)
  Vref = Kastenvolumen / Zahl der Tetraeder der Ausgangszerlegung (fest ueber alle Zuege eines Laufs).
  R1 : A_red = S^T A S (TAKT-DYNAMIK-1; S = Komplement von Bild[M, c, 1_E])
  RH : A_red = S^T (A - A C (C^T A C)^-1 C^T A) S mit C = [c, 1_E] (Eichung horizontal, c und 1_E holonom, Dirac)
Alles andere (Netze, Saaten, Mode, Integrator, Ereignissuche, Abbildung Lesart R) ist td.py.
"""
import argparse, sys, os, time, hashlib
import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import td  # noqa: E402
import tg  # noqa: E402
import tp  # noqa: E402

KIN = 'A1'
RED = 'R1'
VREF = None
KONTR = []
GL = np.eye(6) - np.outer(tp.TR, tp.TR)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def tet_mats(LV, pos, G, O, mod):
    global VREF
    X = pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)
    et = np.stack([X[:, j] - X[:, i] for (i, j, _, _) in tg.PAARE], 1)
    nt = et / np.linalg.norm(et, axis=2)[..., None]
    vol = np.abs(np.linalg.det(X[:, 1:] - X[:, :1])) / 6.0
    if VREF is None:
        VREF = float(mod['Vbox'] / len(G))
    if KIN == 'A2':
        return (VREF / vol)[:, None, None] * mod['A0'], None
    Phi = np.einsum('tpi,sij,tpj->tps', nt, tp.B6, nt)
    Pi = np.linalg.inv(Phi)
    Kt = (vol / VREF)[:, None, None] * np.einsum('tsp,sr,trq->tpq', Pi, GL, Pi)
    return None, Kt


def assemble0(mod, Mt):
    E, eidx = mod['E'], mod['eidx']
    rows = np.repeat(eidx[:, :, None], 6, 2).ravel()
    cols = np.repeat(eidx[:, None, :], 6, 1).ravel()
    return sp.coo_matrix((Mt.ravel(), (rows, cols)), shape=(E, E)).toarray()


class NetzHM(td.Netz):
    def __init__(self, LV, pos, G, O, k1, hp, hx, eigen=True):
        t0 = time.time()
        super().__init__(LV, pos, G, O, k1, hp, hx, eigen=False)
        mod = self.mod
        S = self.S
        kz = {'T': int(len(G))}
        if KIN == 'A1':
            A = self.A.toarray()
        else:
            At, Kt = tet_mats(LV, pos, G, O, mod)
            if KIN == 'A2':
                A = assemble0(mod, At)
            else:
                Km = assemble0(mod, Kt)
                A = np.linalg.inv(Km)
                kz['K_cond'] = float(np.linalg.cond(Km))
        A = 0.5 * (A + A.T)
        self.A = sp.csr_matrix(A)
        if RED == 'R1':
            Ar = S.T @ A @ S
        else:
            B, A1, M, c = tg.ops(mod, np.zeros(3))
            C = np.concatenate([c.real[:, 1:], np.ones((self.E, 1))], 1)
            C = np.linalg.qr(C)[0]
            AS = A @ S
            AC = A @ C
            CAC = 0.5 * (C.T @ AC + (C.T @ AC).T)
            Ar = S.T @ AS - AS.T @ C @ np.linalg.solve(CAC, C.T @ AS)
            if KIN == 'A2L':
                # Gegenprobe Lagrange-Route: K_red = S^T K S - S^T K Q (Q^T K Q)^-1 Q^T K S, Q = Basis Bild M (ohne Translationen)
                Mq = np.linalg.qr(np.ascontiguousarray(M.real[:, 3:]))[0]
                SKQ = S.T @ Km @ Mq
                Kr = S.T @ Km @ S - SKQ @ np.linalg.solve(Mq.T @ Km @ Mq, SKQ.T)
                ev1 = np.sort(np.linalg.eigvalsh(0.5 * (Kr + Kr.T)))
                ev2 = np.sort(1.0 / np.linalg.eigvalsh(0.5 * (Ar + Ar.T)))
                kz['RH_lagrange_gegen_hamilton'] = float(np.abs(ev1 - ev2).max() / np.abs(ev1).max())
        self.Ar = 0.5 * (Ar + Ar.T)
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
        self.eig = None
        if eigen:
            self.spektrum()
        kz['A_pd'] = bool(self.A_pd)
        kz['n_A_neg'] = self.n_A_neg
        if len(KONTR) < 400:
            KONTR.append(kz)
        self.t_bau = self.t_bau + (time.time() - t0)


# ------------------------------------------------------------------------------------------------ Messarm (beschreibend)
# Bei --messformen (nur mit --kin A1 --red R1, also der unveraenderten TAKT-DYNAMIK-1-Bahn): an jedem Zug die reduzierte
# Bewegungsenergie 1/2 xd^T A_red^-1 xd vor und nach dem Zug fuer sechs Formen (A1, A2, A2L) x (R1, RH), dazu am Start.
FORMEN = ('A1R1', 'A1RH', 'A2R1', 'A2RH', 'A2LR1', 'A2LRH')
MESS = False
MESS0 = {}


def formen(N):
    global VREF
    if getattr(N, '_formen', None) is not None:
        return N._formen
    mod = N.mod
    X = N.pos[N.G] + np.einsum('tai,ij->taj', N.O.astype(float), N.LV)
    et = np.stack([X[:, j] - X[:, i] for (i, j, _, _) in tg.PAARE], 1)
    nt = et / np.linalg.norm(et, axis=2)[..., None]
    vol = np.abs(np.linalg.det(X[:, 1:] - X[:, :1])) / 6.0
    if VREF is None:
        VREF = float(mod['Vbox'] / len(N.G))
    Phi = np.einsum('tpi,sij,tpj->tps', nt, tp.B6, nt)
    Pi = np.linalg.inv(Phi)
    Kt = (vol / VREF)[:, None, None] * np.einsum('tsp,sr,trq->tpq', Pi, GL, Pi)
    A1 = assemble0(mod, mod['A0'])
    A2 = assemble0(mod, (VREF / vol)[:, None, None] * mod['A0'])
    A2L = np.linalg.inv(assemble0(mod, Kt))
    B, A1s, M, c = tg.ops(mod, np.zeros(3))
    C = np.linalg.qr(np.concatenate([c.real[:, 1:], np.ones((N.E, 1))], 1))[0]
    S = N.S
    F = {}
    for nm, A in (('A1', A1), ('A2', A2), ('A2L', A2L)):
        A = 0.5 * (A + A.T)
        AS = A @ S
        AC = A @ C
        CAC = 0.5 * (C.T @ AC + (C.T @ AC).T)
        F[nm + 'R1'] = S.T @ AS
        F[nm + 'RH'] = S.T @ AS - AS.T @ C @ np.linalg.solve(CAC, C.T @ AS)
    N._formen = {f: 0.5 * (v + v.T) for f, v in F.items()}
    return N._formen


def kin(N, xd):
    F = formen(N)
    return {f: 0.5 * float(xd @ np.linalg.solve(F[f], xd)) for f in FORMEN}


_tt_mode_orig = td.tt_mode
_abb_orig = td.abbilden


def tt_mode_hm(N, A, k1):
    res = _tt_mode_orig(N, A, k1)
    if MESS:
        MESS0.update(kin(N, res[0]['omega'] * res[1]))
    return res


def abbilden_hm(N, N2, x, y, besch, lesart):
    x2, y2, info = _abb_orig(N, N2, x, y, besch, lesart)
    if MESS:
        kv = kin(N, N.Ar @ y)
        kn = kin(N2, N2.Ar @ y2)
        info['messformen'] = {f: [kv[f], kn[f]] for f in FORMEN}
    return x2, y2, info


_lauf_orig = td.lauf


def lauf_hm(args):
    res = _lauf_orig(args)
    res['hm'] = {'kin': KIN, 'red': RED, 'vref': VREF, 'hm_td_sha256': sha(os.path.abspath(__file__)),
                 'td_sha256': sha(os.path.abspath(td.__file__)), 'kontr_netze': KONTR[:50],
                 'kontr_n': len(KONTR), 'kontr_A_nicht_pd': int(sum(1 for k in KONTR if not k['A_pd'])),
                 'kontr_RH_lagr_max': max([k.get('RH_lagrange_gegen_hamilton', 0.0) for k in KONTR] + [0.0]),
                 'messformen': MESS, 'mess0': MESS0}
    return res


def main():
    global KIN, RED, MESS
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('--kin', default='A1', choices=['A1', 'A2', 'A2L'])
    ap.add_argument('--red', default='R1', choices=['R1', 'RH'])
    ap.add_argument('--messformen', action='store_true')
    a, rest = ap.parse_known_args()
    KIN, RED, MESS = a.kin, a.red, a.messformen
    if MESS and (KIN != 'A1' or RED != 'R1'):
        raise SystemExit('--messformen nur mit --kin A1 --red R1 (unveraenderte Bahn)')
    td.Netz = NetzHM
    td.lauf = lauf_hm
    td.tt_mode = tt_mode_hm
    td.abbilden = abbilden_hm
    sys.argv = [os.path.abspath(td.__file__)] + rest
    td.main()


if __name__ == '__main__':
    main()
