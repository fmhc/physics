#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PRISMA-MAXWELL-1 (Runde 52, ag-physics), Rechen-Agent fuer die Leitung claude-primary.

Frage: Ist die DEC-Maxwell-Form Q(q) = d1(q)^+ W d1(q) auf dem Produktkomplex V x Z (Prismen) ueber die volle 4D-Zone
ausser den Eichmoden positiv?  Kontrolle Z^4, Vergleich (beschreibend) Zeltnetz QUANT-2.

Konventionen:
  - Reduzierte Blochkoordinaten q_i = k . a_i (a_1..a_3 fcc-Vektoren aus tp.AV in Einheiten a, a_4 = tau e_t).
    Ein Koeffizient einer um n (ganzzahlig, 4 Komponenten) verschobenen Zelle bekommt die Phase exp(i q . n).
  - d0, d1 als Termlisten (Zeile, Spalte, Vorzeichen, n). D(q) = sum_n D_n exp(i q . n), D_n reell.
  - Q(q) = sum_Delta C_Delta exp(i q . Delta), C_Delta = sum_{m - n = Delta} D_n^T W D_m (reell).
  - Produktkomplex V x Z: Kanten = (e, Schicht) und (v, Zeitschritt); Flaechen = (f, Schicht) und (e x Zeitschritt).
    d0: (e,0) <- d0s; (v,I) <- exp(i q_t) - 1.
    d1: (f,0) <- d1s auf (e,0); (e x I) <- d0s auf (v,I) und -(exp(i q_t) - 1) auf (e,0).
    Sterne (Produkt-DEC): *2(f x pt) = *2s(f) tau, *2(e x I) = *1s(e) / tau.
  - Nicht-Eich-Eigenwert: lambda_nV(Q) (0-basiert, aufsteigend); fuer q != 0 ist d0(q) injektiv (Eichraum = nV).
    Kreuzkontrolle per Projektion auf das orthogonale Komplement von Bild(d0) (SVD).
  - Schranke (Weyl): |lambda_j(Q(q)) - lambda_j(Q(c))| <= ||Q(q) - Q(c)|| <= sum_i L_i |q_i - c_i|,
    L_i >= sup_q ||dQ/dq_i||; naechste Ecke c komponentenweise, |q_i - c_i| <= h_i / 2.

Aufruf (nur ueber kleintest.sh auf der .69):
  python pm.py rauch <aus.json>
  python pm.py pr0k <aus.json>
  python pm.py scan <netz: VZ|Z4|zelt> <N> <k0> <fein> <aus.json>
"""
import hashlib
import itertools
import json
import math
import os
import platform
import sys
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)

TAU_Q2 = 0.348006576329167          # QUANT-2 (kette-p0.sh), auch fuer V x Z
HAND_X, HAND_Y = -23.0 / 7.0, -32.0 / 7.0
GWP = os.path.join(HIER, '..', 'daten', 'gwp.npz')
T0 = time.time()


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def kopf():
    return {'python': platform.python_version(), 'numpy': np.__version__, 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__))}


# ================================================================================================ Komplexe
def raum_V(x=HAND_X, y=HAND_Y):
    """Raeumliches Netz V (L = 1) mit Potenzgewichten (x, y) in (a/8)^2; Sterne aus rv.sterne (unveraendert)."""
    import rv
    import ew
    net = rv.netz_V(1)
    topo = rv.topologie(net)
    w = rv.w_sym(net, x, y)
    st = rv.sterne(net, topo, w)
    rows, A, G0 = rv.zeilen(net, topo)
    kontr = rv.stern_kontrolle(net, topo, rows, A, G0, w, st)
    home = net['home']
    nV = net['n']
    ekeys = list(topo['kanten'].keys())
    eid = {k: i for i, k in enumerate(ekeys)}
    fkeys = list(topo['flaechen'].keys())

    def n_aus(T8):
        n = np.asarray(T8, float) @ ew.AV8INV
        assert np.allclose(n, np.rint(n), atol=1e-9), T8
        return [int(v) for v in np.rint(n)]

    d0 = []
    for e, key in enumerate(ekeys):
        (g0, x0), (g1, x1) = key
        n0 = n_aus(np.array(x0) - home[g0])
        n1 = n_aus(np.array(x1) - home[g1])
        assert not any(n0)
        d0.append((e, g1, 1.0, n1))
        d0.append((e, g0, -1.0, n0))
    d1 = []
    s2 = np.zeros(len(fkeys))
    flaeche = np.zeros(len(fkeys))
    Pf = []
    for f, key in enumerate(fkeys):
        it = [(g, np.array(p, float)) for g, p in key]
        for a, b in ((0, 1), (1, 2), (2, 0)):
            ek, T = rv.kanon([it[a], it[b]], home, True)
            assert ek in eid, ek
            first = (ek[0][0] == it[a][0]) and np.allclose(np.array(ek[0][1]) + T, it[a][1])
            d1.append((f, eid[ek], 1.0 if first else -1.0, n_aus(T)))
        P = np.array([p for g, p in it]) * net['skala']
        Pf.append(P)
        flaeche[f] = 0.5 * np.linalg.norm(np.cross(P[1] - P[0], P[2] - P[0]))
        s2[f] = st['delta'][key] / flaeche[f]
    vols = np.array([abs(np.linalg.det(X[1:] - X[0])) / 6.0 for g, X in net['tets']]) * net['skala'] ** 3
    # Kanten-Vektoren (fuer die Maxwell-Identitaet)
    evec = np.array([(np.array(k[1][1]) - np.array(k[0][1])) * net['skala'] for k in ekeys])
    return {'name': 'V', 'nV': nV, 'nE': len(ekeys), 'nF': len(fkeys), 'd0': d0, 'd1': d1,
            's0': st['s0'], 's1': st['s1'], 's2': s2, 'tetvol': vols, 'A3': np.array(ew.AV, float),
            'vol3': float(net['vol'] * net['skala'] ** 3), 'Pf': np.array(Pf), 'evec': evec,
            'kontrolle_3d': kontr, 'n_tet': len(net['tets']), 'w': w.tolist()}


def raum_Z3():
    """Kubisches Gitter Z^3 (Kante 1): 1 Ecke, 3 Kanten, 3 Quadrate; alle Sterne 1."""
    E = np.eye(3, dtype=int)
    d0, d1 = [], []
    for e in range(3):
        d0.append((e, 0, 1.0, list(E[e])))
        d0.append((e, 0, -1.0, [0, 0, 0]))
    Pf, fl = [], []
    for f, (i, j) in enumerate(((0, 1), (1, 2), (0, 2))):
        d1 += [(f, i, 1.0, [0, 0, 0]), (f, j, 1.0, list(E[i])), (f, i, -1.0, list(E[j])), (f, j, -1.0, [0, 0, 0])]
    return {'name': 'Z3', 'nV': 1, 'nE': 3, 'nF': 3, 'd0': d0, 'd1': d1, 's0': np.ones(1), 's1': np.ones(3),
            's2': np.ones(3), 'tetvol': np.ones(1), 'A3': np.eye(3), 'vol3': 1.0, 'quadrat': True,
            'evec': np.eye(3), 'Pf': None}


def produkt(R, tau):
    """Produktkomplex R x Z mit Zeitschritt tau (Termlisten mit 4-Komponenten-Verschiebung)."""
    nV, nE, nF = R['nV'], R['nE'], R['nF']
    t1 = [0, 0, 0, 1]
    z = [0, 0, 0, 0]
    d0 = [(e, v, c, list(n) + [0]) for (e, v, c, n) in R['d0']]
    for v in range(nV):
        d0 += [(nE + v, v, 1.0, t1), (nE + v, v, -1.0, z)]
    d1 = [(f, e, c, list(n) + [0]) for (f, e, c, n) in R['d1']]
    for (e, v, c, n) in R['d0']:
        d1.append((nF + e, nE + v, c, list(n) + [0]))
    for e in range(nE):
        d1 += [(nF + e, e, -1.0, t1), (nF + e, e, 1.0, z)]
    W = np.r_[R['s2'] * tau, R['s1'] / tau]
    A4 = np.zeros((4, 4))
    A4[:3, :3] = R['A3']
    A4[3, 3] = tau
    sterne4 = {'*0 (v x pt)': R['s0'] * tau, '*1 (e x pt)': R['s1'] * tau, '*1 (v x I)': R['s0'] / tau,
               '*2 (f x pt)': R['s2'] * tau, '*2 (e x I)': R['s1'] / tau,
               '*3 (t x pt)': tau / R['tetvol'], '*3 (f x I)': R['s2'] / tau, '*4 (t x I)': 1.0 / (R['tetvol'] * tau)}
    return {'name': R['name'] + 'xZ', 'nV': nV, 'nE': nE + nV, 'nF': nF + nE, 'd0': d0, 'd1': d1, 'W': W,
            'A4': A4, 'tau': tau, 'sterne4': sterne4, 'raum': R}


def zelt():
    """Zeltnetz QUANT-2 (gw.Vorlage, unveraendert) mit den Gewichten aus gwp.npz (tau = 0,348)."""
    import gw
    import rk
    dat = np.load(GWP)
    tau = float(dat['tau'])
    V = gw.Vorlage(nq=1, seed=1)
    g = V.g
    eid = {key: i for i, key in enumerate(g.ekeys)}
    d1 = []
    for f, key in enumerate(V.keys):
        vs = list(key)
        for a, b in ((0, 1), (1, 2), (2, 0)):
            ek, Tn = rk.kanon_kante(vs[a], vs[b])
            s_ = 1.0 if (ek[0] == vs[a][0] and tuple(Tn) == tuple(int(x) for x in vs[a][1])) else -1.0
            d1.append((f, eid[ek], s_, list(Tn)))
    d0 = []
    for e, (b1, b2, d) in enumerate(g.ekeys):
        d0 += [(e, b2, 1.0, list(d)), (e, b1, -1.0, [0, 0, 0, 0])]
    w_neu, _, _ = V.sterne(tau, dat['omega'])
    A4 = g.A.copy()
    A4[3, 3] = tau
    # rk.Gitter: pos = ... + A @ n, also a_i = Spalten von A; hier Zeilen = Gittervektoren
    return {'name': 'Zelt', 'nV': g.NV, 'nE': g.NE, 'nF': V.NF, 'd0': d0, 'd1': d1, 'W': np.array(dat['w'], float),
            'A4': A4.T.copy(), 'tau': tau, 'w_nachgerechnet_abw': float(np.abs(w_neu - dat['w']).max()),
            'omega': dat['omega'].tolist()}


# ================================================================================================ Bloch
def koeff(terms, nrow, ncol):
    blk = {}
    for (r, c, s, n) in terms:
        key = tuple(int(v) for v in n)
        if key not in blk:
            blk[key] = np.zeros((nrow, ncol))
        blk[key][r, c] += s
    ns = sorted(blk)
    return np.array(ns, float), np.array([blk[k] for k in ns])


class Bloch:
    def __init__(self, K):
        self.K = K
        self.nV, self.nE, self.nF = K['nV'], K['nE'], K['nF']
        self.n1, self.D1 = koeff(K['d1'], self.nF, self.nE)
        self.n0, self.D0 = koeff(K['d0'], self.nE, self.nV)
        W = K['W']
        Cd = {}
        WD = W[None, :, None] * self.D1
        for a in range(len(self.n1)):
            for b in range(len(self.n1)):
                dl = tuple(int(v) for v in (self.n1[b] - self.n1[a]))
                M = self.D1[a].T @ WD[b]
                if not np.any(M):
                    continue
                Cd[dl] = Cd.get(dl, 0.0) + M
        self.dl = np.array(sorted(Cd), float)
        self.C = np.array([Cd[tuple(int(v) for v in d)] for d in self.dl])
        self.Cflat = self.C.reshape(len(self.dl), -1)
        self.Cnorm = np.array([np.linalg.norm(c, 2) for c in self.C])
        A = self.K['A4']
        self.A4 = A                       # Zeilen: Gittervektoren a_i (physikalisch)

    # --- Matrizen
    def D(self, q, which=1):
        n, Dn = (self.n1, self.D1) if which == 1 else (self.n0, self.D0)
        ph = np.exp(1j * (np.atleast_2d(q) @ n.T))          # (Nq, Nn)
        return np.einsum('qn,nij->qij', ph, Dn)

    def Q(self, q):
        q = np.atleast_2d(q)
        arg = q @ self.dl.T
        out = (np.cos(arg) @ self.Cflat) + 1j * (np.sin(arg) @ self.Cflat)
        N = self.nE
        return out.reshape(len(q), N, N)

    def dQ(self, q, i):
        q = np.atleast_2d(q)
        arg = q @ self.dl.T
        fac = self.dl[:, i]
        out = 1j * ((np.cos(arg) * fac) @ self.Cflat) - ((np.sin(arg) * fac) @ self.Cflat)
        N = self.nE
        return out.reshape(len(q), N, N)

    def ev(self, q, chunk=512):
        res = []
        for s in range(0, len(q), chunk):
            Qm = self.Q(q[s:s + chunk])
            res.append(np.linalg.eigvalsh(0.5 * (Qm + np.conj(np.transpose(Qm, (0, 2, 1))))))
        return np.concatenate(res)

    def ev_proj(self, q, chunk=256):
        """Eigenwerte von Q auf dem orthogonalen Komplement von Bild(d0(q)) (exakt, per SVD)."""
        res, smin = [], []
        for s in range(0, len(q), chunk):
            qq = q[s:s + chunk]
            Qm = self.Q(qq)
            D0 = self.D(qq, 0)
            U, sv, _ = np.linalg.svd(D0, full_matrices=True)
            smin.append(sv[:, -1])
            P = U[:, :, self.nV:]
            H = np.conj(np.transpose(P, (0, 2, 1))) @ Qm @ P
            res.append(np.linalg.eigvalsh(0.5 * (H + np.conj(np.transpose(H, (0, 2, 1))))))
        return np.concatenate(res), np.concatenate(smin)

    def dnorm(self, q, chunk=256):
        """||dQ/dq_i|| an den Punkten q (4 Spalten)."""
        out = np.zeros((len(q), 4))
        for s in range(0, len(q), chunk):
            for i in range(4):
                M = self.dQ(q[s:s + chunk], i)
                out[s:s + chunk, i] = np.abs(np.linalg.eigvalsh(0.5 * (M + np.conj(np.transpose(M, (0, 2, 1)))))).max(1)
        return out

    def k_phys(self, q):
        """q_i = k . a_i  ->  k = A^{-1} q (A Zeilen a_i)."""
        return np.linalg.solve(self.A4, np.atleast_2d(q).T).T

    def q_aus_k(self, k):
        return np.atleast_2d(k) @ self.A4.T

    def lipschitz_grob(self):
        """Zwei globale Schranken je Richtung: (a) sum ||C_Delta|| |Delta_i|; (b) Hessian-Matrix H_ij."""
        a = (self.Cnorm[:, None] * np.abs(self.dl)).sum(0)
        H = np.einsum('d,di,dj->ij', self.Cnorm, np.abs(self.dl), np.abs(self.dl))
        lam_sup = float(self.Cnorm.sum())
        return a, H, lam_sup


def d1d0_max(B, qs):
    return float(max(np.abs(B.D(q, 1)[0] @ B.D(q, 0)[0]).max() for q in qs))


# ================================================================================================ Modi
def info_bloch(B):
    a, H, lam_sup = B.lipschitz_grob()
    return {'nV': B.nV, 'nE': B.nE, 'nF': B.nF, 'n_terme_d1': len(B.n1), 'n_Delta': len(B.dl),
            'L_grob_sumC': a.tolist(), 'H_grob': H.tolist(), 'lam_sup_schranke': lam_sup}


def nullzahl(ev, rel=1e-10):
    sc = np.abs(ev).max(1)
    return (np.abs(ev) <= rel * sc[:, None]).sum(1)


def modus_rauch(aus):
    out = {'kopf': kopf()}
    R = raum_V()
    K = produkt(R, TAU_Q2)
    B = Bloch(K)
    out['VZ'] = info_bloch(B)
    out['VZ']['kontrolle_3d'] = R['kontrolle_3d']
    rng = np.random.default_rng(1)
    qs = rng.uniform(-np.pi, np.pi, (20, 4))
    out['VZ']['d1d0'] = d1d0_max(B, qs)
    ev = B.ev(qs)
    out['VZ']['nullen'] = nullzahl(ev).tolist()
    evp, smin = B.ev_proj(qs)
    out['VZ']['proj_gegen_lamnV'] = float(np.abs(evp[:, 0] - ev[:, B.nV]).max())
    out['VZ']['lam_nV'] = ev[:, B.nV].tolist()
    out['VZ']['lam_max'] = float(ev[:, -1].max())
    # Q aus C gegen D^+ W D direkt
    Dq = B.D(qs[:3], 1)
    Qd = np.conj(np.transpose(Dq, (0, 2, 1))) @ (K['W'][None, :, None] * Dq)
    out['VZ']['Q_C_gegen_direkt'] = float(np.abs(Qd - B.Q(qs[:3])).max())
    # Vorfaktor nahe 0 in ein paar Richtungen (physikalisch)
    vf = []
    for n in np.eye(4):
        for t in (1e-3, 1e-2, 1e-1, 0.5, 1.0, 2.0):
            q = B.q_aus_k(t * n)
            e = B.ev(q)[0]
            vf.append([n.tolist(), t, float(e[B.nV] / t ** 2), float(e[B.nV])])
    out['VZ']['vorfaktor_probe'] = vf
    t1 = time.time()
    qg = rng.uniform(-np.pi, np.pi, (512, 4))
    B.ev(qg)
    out['VZ']['zeit_ev_512'] = time.time() - t1
    t1 = time.time()
    dn = B.dnorm(qg[:256])
    out['VZ']['zeit_dnorm_256'] = time.time() - t1
    out['VZ']['dnorm_max_probe'] = dn.max(0).tolist()
    # Z^4
    BZ = Bloch(produkt(raum_Z3(), 1.0))
    out['Z4'] = info_bloch(BZ)
    out['Z4']['d1d0'] = d1d0_max(BZ, qs)
    evz = BZ.ev(qs)
    soll = 4 * (np.sin(qs / 2) ** 2).sum(1)
    out['Z4']['spektrum_abw'] = float(np.abs(evz - np.c_[np.zeros(len(qs)), soll, soll, soll]).max())
    log('rauch V x Z / Z4 fertig')
    # Zelt
    t1 = time.time()
    KZ = zelt()
    BT = Bloch(KZ)
    out['zelt'] = info_bloch(BT)
    out['zelt']['w_nachgerechnet_abw'] = KZ['w_nachgerechnet_abw']
    out['zelt']['d1d0'] = d1d0_max(BT, qs[:5])
    evt = BT.ev(qs[:5])
    evpt, _ = BT.ev_proj(qs[:5])
    out['zelt']['nullen'] = nullzahl(evt).tolist()
    out['zelt']['proj_min'] = evpt[:, 0].tolist()
    out['zelt']['lam_max'] = float(evt[:, -1].max())
    out['zelt']['zeit_aufbau'] = time.time() - t1
    t1 = time.time()
    BT.ev(qg[:128])
    out['zelt']['zeit_ev_128'] = time.time() - t1
    out['zeit_s'] = time.time() - T0
    with open(aus, 'w') as f:
        json.dump(out, f, indent=1)
    log(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items()
                                                          if kk not in ('H_grob', 'lam_nV', 'vorfaktor_probe')})
                    for k, v in out.items()})[:6000])


def maxwell_identitaet(K):
    """sum_f W_f S_f S_f^T gegen Vol4 I_6 (Produktkomplex, Bivektoren in 4D)."""
    R = K['raum']
    tau = K['tau']
    IU = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    S = []
    if R.get('Pf') is not None:
        for P in R['Pf']:
            a, b = np.r_[P[1] - P[0], 0.0], np.r_[P[2] - P[0], 0.0]
            S.append([0.5 * (a[m] * b[n] - a[n] * b[m]) for (m, n) in IU])
    else:
        for (i, j) in ((0, 1), (1, 2), (0, 2)):
            a, b = np.eye(4)[i], np.eye(4)[j]
            S.append([a[m] * b[n] - a[n] * b[m] for (m, n) in IU])
    for ev in R['evec']:
        a, b = np.r_[ev, 0.0], np.array([0, 0, 0, tau])
        S.append([a[m] * b[n] - a[n] * b[m] for (m, n) in IU])
    S = np.array(S)
    M = np.einsum('f,fa,fb->ab', K['W'], S, S)
    vol4 = R['vol3'] * tau
    return float(np.abs(M - vol4 * np.eye(6)).max() / vol4)


def modus_pr0k(aus):
    out = {'kopf': kopf()}
    rng = np.random.default_rng(20261009)
    qs = rng.uniform(-np.pi, np.pi, (200, 4))
    # ---- PR0: Sterne auf V x Z am Kammermittelpunkt
    R = raum_V()
    K = produkt(R, TAU_Q2)
    st = {k: {'min': float(v.min()), 'max': float(v.max()), 'n': int(len(v)), 'n_nichtpos': int((v <= 0).sum())}
          for k, v in K['sterne4'].items()}
    out['PR0'] = {'tau': TAU_Q2, 'x': HAND_X, 'y': HAND_Y, 'sterne4': st,
                  'alle_positiv': bool(all(s['n_nichtpos'] == 0 for s in st.values())),
                  'kontrolle_3d': R['kontrolle_3d'], 'n_tet': R['n_tet'],
                  'maxwell_identitaet_rel': maxwell_identitaet(K),
                  'W_min': float(K['W'].min()), 'W_max': float(K['W'].max())}
    log('PR0', json.dumps(out['PR0']))
    # ---- PRk
    prk = {}
    netze = [('VZ', K), ('Z4', produkt(raum_Z3(), 1.0)), ('VZ_tau0.2924', produkt(R, 0.2924)),
             ('VZ_tau1', produkt(R, 1.0))]
    for name, KK in netze:
        B = Bloch(KK)
        ev = B.ev(qs)
        nz = nullzahl(ev)
        evp, smin = B.ev_proj(qs)
        e = {'nV': B.nV, 'nE': B.nE, 'nF': B.nF, 'd1d0_max': d1d0_max(B, qs),
             'nullen_min': int(nz.min()), 'nullen_max': int(nz.max()), 'nullen_gleich_nV': bool(np.all(nz == B.nV)),
             'lam_nV_min_rel': float((ev[:, B.nV] / ev[:, -1]).min()),
             'proj_gegen_lamnV_max': float(np.abs(evp[:, 0] - ev[:, B.nV]).max()),
             'sigma_min_d0_min': float(smin.min()),
             'symmetrie_Q(-q)': float(np.abs(B.ev(-qs[:20]) - ev[:20]).max())}
        if name == 'Z4':
            soll = 4 * (np.sin(qs / 2) ** 2).sum(1)
            e['spektrum_abw_max'] = float(np.abs(ev - np.c_[np.zeros(len(qs)), soll, soll, soll]).max())
            e['soll'] = '[0, S, S, S], S = 4 sum_mu sin^2(q_mu/2)'
        # k = 0
        e0 = B.ev(np.zeros((1, 4)))[0]
        e['nullen_bei_q0'] = int(nullzahl(e0[None])[0])
        prk[name] = e
        log('PRk', name, json.dumps(e))
    KZ = zelt()
    BT = Bloch(KZ)
    evt = BT.ev(qs[:40])
    nz = nullzahl(evt)
    evpt, smt = BT.ev_proj(qs[:40])
    prk['zelt_beschreibend'] = {'nV': BT.nV, 'nE': BT.nE, 'nF': BT.nF, 'd1d0_max': d1d0_max(BT, qs[:40]),
                                'nullen_min': int(nz.min()), 'nullen_max': int(nz.max()),
                                'proj_min_rel': float((evpt[:, 0] / evt[:, -1]).min()),
                                'n_q_proj_negativ': int((evpt[:, 0] < 0).sum()),
                                'W_min': float(KZ['W'].min()), 'n_W_neg': int((KZ['W'] < 0).sum()),
                                'w_nachgerechnet_abw': KZ['w_nachgerechnet_abw'], 'tau': KZ['tau']}
    log('PRk zelt', json.dumps(prk['zelt_beschreibend']))
    prk['bestanden'] = bool(all(prk[n]['d1d0_max'] < 1e-12 and prk[n]['nullen_gleich_nV'] for n in ('VZ', 'Z4')))
    out['PRk'] = prk
    out['zeit_s'] = time.time() - T0
    with open(aus, 'w') as f:
        json.dump(out, f, indent=1)
    log('PRk bestanden:', prk['bestanden'])


# ------------------------------------------------------------------------------------------------ Scan
def richtungen26(B):
    """13 Raumachsen (<100> 3, <110> 6, <111> 4, bis aufs Vorzeichen) je mit k_t = 0 und k_t = |k_s|; dazu rein
    zeitlich (27., Zusatz). Physikalische Einheitsvektoren."""
    ax = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1),
          (1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]
    out = []
    for a in ax:
        s = np.array(a, float) / np.linalg.norm(a)
        out.append(np.r_[s, 0.0])
        out.append(np.r_[s, 1.0] / math.sqrt(2.0))
    out.append(np.array([0, 0, 0, 1.0]))
    return np.array(out)


def gitterpunkte(N, stufe=1):
    M = N * stufe
    us = np.arange(-M // 2, M // 2 + 1)
    ut = np.arange(0, M // 2 + 1)
    U = np.array(list(itertools.product(us, us, us, ut)), float)
    return U, 2 * np.pi / M


def modus_scan(netz, N, k0, fein, aus):
    out = {'kopf': kopf(), 'netz': netz, 'N': N, 'k0': k0, 'fein': fein}
    if netz == 'VZ':
        K = produkt(raum_V(), TAU_Q2)
    elif netz == 'Z4':
        K = produkt(raum_Z3(), 1.0)
    else:
        K = zelt()
    B = Bloch(K)
    out['info'] = info_bloch(B)
    nV = B.nV
    a_grob, Hgrob, lam_sup = B.lipschitz_grob()
    # ---- Ecken 12^4 (halbe Zone in q_t)
    U, h = gitterpunkte(N)
    q = U * h
    t1 = time.time()
    ev = B.ev(q)
    lam = ev[:, nV]
    lam_max_gitter = float(ev[:, -1].max())
    gauge_max = float(np.abs(ev[:, :nV]).max())
    out['zeit_ecken'] = time.time() - t1
    kp = np.linalg.norm(B.k_phys(q), axis=1)
    null = np.all(U == 0, axis=1)
    log('Ecken', len(q), 'lam_nV min (ohne q=0)', lam[~null].min())
    # Kreuzkontrolle Projektion (alle Ecken ausser q = 0) und sigma_min(d0)
    t1 = time.time()
    evp, smin = B.ev_proj(q[~null])
    out['proj_min_ohne_q0'] = float(evp[:, 0].min())
    out['proj_n_negativ'] = int((evp[:, 0] < -1e-12 * lam_max_gitter).sum())
    out['proj_gegen_lamnV_max'] = float(np.abs(evp[:, 0] - lam[~null]).max())
    out['sigma_min_d0_min_ohne_q0'] = float(smin.min())
    out['zeit_proj'] = time.time() - t1
    # ---- Lipschitz: sup ||dQ/dq_i|| <= max_Ecken ||dQ/dq_i|| + sum_j H_ij h/2
    t1 = time.time()
    if netz != 'zelt':
        dn = B.dnorm(q)
        L_gitter = dn.max(0) + Hgrob @ (np.full(4, h / 2))
    else:
        dn = np.full((1, 4), np.nan)
        L_gitter = np.full(4, np.inf)
    L = np.minimum(L_gitter, a_grob)
    out['zeit_dnorm'] = time.time() - t1
    out['L'] = {'sumC': a_grob.tolist(), 'gitter_plus_hesse': L_gitter.tolist(), 'max_ecken_dnorm': dn.max(0).tolist(),
                'genommen': L.tolist(), 'lam_sup_schranke': lam_sup, 'lam_max_gitter': lam_max_gitter}
    eps = 1e-10 * lam_sup
    # beschreibend (nicht Kartenwortlaut): Wurzel-Variante, sqrt(lambda_j) ist Lipschitz mit
    # L_M,i = sum_n |n_i| ||W^1/2 D_n|| (Weyl fuer Singulaerwerte von M = W^1/2 D)
    if np.all(K['W'] > 0):
        sw = np.sqrt(K['W'])
        LM = np.array([sum(abs(B.n1[a, i]) * np.linalg.norm(sw[:, None] * B.D1[a], 2) for a in range(len(B.n1)))
                       for i in range(4)])
    else:
        LM = np.full(4, np.inf)
    out['L']['wurzel_LM'] = LM.tolist()

    def schranke(hh):
        return float((L * hh / 2).sum()) + eps

    def schranke_M(hh):
        return float((LM * hh / 2).sum()) + 1e-10
    B12 = schranke(h)
    out['schranke_B'] = {'N': B12, 'wurzel_N': schranke_M(h)}
    # ---- Ecken ausserhalb der Kugel
    aus_k = kp >= k0
    out['ecken'] = {'n': int(len(q)), 'n_ausserhalb_kugel': int(aus_k.sum()),
                    'lam_nV_min_ausserhalb': float(lam[aus_k].min()),
                    'wo_min_ausserhalb_q': q[aus_k][np.argmin(lam[aus_k])].tolist(),
                    'wo_min_ausserhalb_kphys': B.k_phys(q[aus_k][np.argmin(lam[aus_k])])[0].tolist(),
                    'lam_nV_min_ohne_q0': float(lam[~null].min()),
                    'wo_min_ohne_q0': q[~null][np.argmin(lam[~null])].tolist(),
                    'n_lam_nV_nichtpos_ohne_q0': int((lam[~null] <= 0).sum()),
                    'gauge_eigenwerte_max_abs': gauge_max, 'lam_max': lam_max_gitter}
    # ---- Zellen
    ns, nt = N + 1, N // 2 + 1
    lamg = lam.reshape(ns, ns, ns, nt)
    kg = kp.reshape(ns, ns, ns, nt)
    cmin = np.full((N, N, N, N // 2), np.inf)
    kmax = np.zeros((N, N, N, N // 2))
    for o in itertools.product((0, 1), repeat=4):
        sl = tuple(slice(o[d], o[d] + (N if d < 3 else N // 2)) for d in range(4))
        cmin = np.minimum(cmin, lamg[sl])
        kmax = np.maximum(kmax, kg[sl])
    in_kugel = kmax < k0
    ok = (cmin - B12 > 0) & ~in_kugel
    offen = ~ok & ~in_kugel
    out['zellen'] = {'n': int(cmin.size), 'in_kugel': int(in_kugel.sum()), 'zertifiziert': int(ok.sum()),
                     'offen': int(offen.sum()), 'min_lam_ecken_minus_B_ausserhalb': float((cmin - B12)[~in_kugel].min())}
    out["zellen"]["wurzel_zertifiziert_beschreibend"] = int(((np.sqrt(np.maximum(cmin, 0)) - schranke_M(h) > 0) & ~in_kugel).sum())
    log('Stufe N:', json.dumps(out['zellen']), 'B', B12)
    # ---- Verfeinerung 2N (lokal: Teilzellen offener Zellen)
    stufen = []
    offene = [tuple(int(v) for v in idx) for idx in np.argwhere(offen)]
    stufe = 1
    while offene and stufe * 2 <= fein // N and time.time() - T0 < 420:
        stufe *= 2
        hs = h / stufe
        Bs = schranke(hs)
        cache = {}
        neu_offen = []
        n_ok = n_kug = n_okM = 0
        # Punkte sammeln
        pts = set()
        for c in offene:
            base = np.array(c) * 2
            for o in itertools.product((0, 1, 2), repeat=4):
                pts.add(tuple(base + np.array(o)))
        pts = sorted(pts)
        P = np.array(pts, float)
        # Gitterindex auf Stufe 'stufe' relativ zur letzten Stufe: Ecken bei (index - M/2) * hs, Zeit index * hs
        M = N * stufe
        qq = np.c_[(P[:, :3] - M // 2) * hs, P[:, 3] * hs]
        ev2 = B.ev(qq)[:, nV]
        k2 = np.linalg.norm(B.k_phys(qq), axis=1)
        for p, l_, k_ in zip(pts, ev2, k2):
            cache[p] = (l_, k_)
        for c in offene:
            base = np.array(c) * 2
            for o in itertools.product((0, 1), repeat=4):
                sub = base + np.array(o)
                vals = [cache[tuple(sub + np.array(oo))] for oo in itertools.product((0, 1), repeat=4)]
                lm = min(v[0] for v in vals)
                km = max(v[1] for v in vals)
                if km >= k0 and math.sqrt(max(lm, 0.0)) - schranke_M(hs) > 0:
                    n_okM += 1
                if km < k0:
                    n_kug += 1
                elif lm - Bs > 0:
                    n_ok += 1
                else:
                    neu_offen.append(tuple(int(v) for v in sub))
        st = {"gitter": M, "B": Bs, "wurzel_B": schranke_M(hs), "wurzel_zert_unter_offenen_beschreibend": n_okM, "teilzellen": 16 * len(offene), "in_kugel": n_kug, "zertifiziert": n_ok,
              'offen': len(neu_offen), 'punkte': len(pts), 'lam_nV_min_ausserhalb_kugel':
              float(ev2[k2 >= k0].min()) if np.any(k2 >= k0) else None}
        if neu_offen:
            # Beispiel: offene Teilzelle mit kleinster Ecke
            st['beispiel_offen'] = [list(c) for c in neu_offen[:5]]
        stufen.append(st)
        log('Stufe', M, json.dumps({k: v for k, v in st.items() if k != 'beispiel_offen'}))
        offene = neu_offen
        if M >= fein:
            out['ergebnis_bis_fein'] = {'gitter': M, 'offen': len(offene)}
    out['verfeinerung'] = stufen
    out['zertifiziert_bis_fein'] = (len(offene) == 0)
    # ---- Kugel: Vorfaktoren in 26 (+1) Richtungen
    dirs = richtungen26(B)
    kug = []
    ts = k0 * np.r_[1e-3, 1e-2, np.linspace(0.05, 1.0, 20)]
    for n in dirs:
        qq = B.q_aus_k(ts[:, None] * n[None, :])
        e = B.ev(qq)
        l_ = e[:, nV]
        kug.append({'n': n.tolist(), 'vorfaktor_1e-3': float(l_[0] / ts[0] ** 2),
                    'vorfaktor_1e-2': float(l_[1] / ts[1] ** 2),
                    'drei_kleinste_1e-3': (e[0, nV:nV + 3] / ts[0] ** 2).tolist(),
                    'strahl_min': float(l_.min()), 'strahl_alle_pos': bool(np.all(l_ > 0)),
                    'gauge_max_rel_1e-3': float(np.abs(e[0, :nV]).max() / e[0, -1])})
    out['kugel'] = kug
    vf = np.array([d['vorfaktor_1e-3'] for d in kug[:26]])
    out['kugel_zusammen'] = {'vorfaktor_min_26': float(vf.min()), 'vorfaktor_max_26': float(vf.max()),
                             'alle_26_positiv': bool(np.all(vf > 0)),
                             'vorfaktor_konsistenz_max_rel': float(max(abs(d['vorfaktor_1e-3'] / d['vorfaktor_1e-2'] - 1)
                                                                       for d in kug)),
                             'strahlen_alle_pos': bool(all(d['strahl_alle_pos'] for d in kug)),
                             'zeit_vorfaktor_27': kug[26]['vorfaktor_1e-3']}
    # Kugelanteil am Zonenvolumen (physikalisch): Kugel 4D Volumen pi^2/2 k0^4 gegen |det(2 pi A^-1)|
    zone = abs(np.linalg.det(2 * np.pi * np.linalg.inv(B.A4)))
    out['kugel_anteil_zone'] = float(0.5 * math.pi ** 2 * k0 ** 4 / zone)
    # Mindest-k0 fuer N-Stufe (beschreibend): kleinster |k| an Ecken mit lam_nV <= B12
    schlecht = (lam <= B12) & ~null
    out['beschreibend_kmax_ecken_lam_unter_BN'] = float(kp[schlecht].max()) if np.any(schlecht) else 0.0
    # beschreibend: noetiges Gitter N (gleichmaessig), damit B(2 pi / N) < min lambda ausserhalb der Kugel
    lmin_a = float(lam[aus_k].min())
    out['beschreibend_N_noetig'] = {'karte_L': float(np.pi * L.sum() / lmin_a) if lmin_a > 0 else None,
                                    'wurzel_LM': float(np.pi * LM.sum() / math.sqrt(lmin_a)) if lmin_a > 0 else None}
    out['zeit_s'] = time.time() - T0
    with open(aus, 'w') as f:
        json.dump(out, f, indent=1)
    zus = {k: out[k] for k in ('ecken', 'zellen', 'schranke_B', 'zertifiziert_bis_fein', 'kugel_zusammen', 'beschreibend_N_noetig',
                               'kugel_anteil_zone', 'proj_min_ohne_q0', 'proj_n_negativ', 'proj_gegen_lamnV_max',
                               'sigma_min_d0_min_ohne_q0', 'beschreibend_kmax_ecken_lam_unter_BN', 'zeit_s')}
    zus['L'] = out['L']
    zus['verfeinerung'] = [{k: v for k, v in s.items() if k != 'beispiel_offen'} for s in stufen]
    log('ZUSAMMEN', json.dumps(zus))


def main():
    m = sys.argv[1]
    if m == 'rauch':
        modus_rauch(sys.argv[2])
    elif m == 'pr0k':
        modus_pr0k(sys.argv[2])
    elif m == 'scan':
        modus_scan(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6])
    else:
        raise SystemExit('Modus?')


if __name__ == '__main__':
    main()
