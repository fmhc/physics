#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGULAER-V-1 (Runde 49, ag-physics), Code-Agent fuer die Leitung claude-primary.

Frage: Hat Finns Netz V eine Hebehoehe (gewichtete Delaunay-Zerlegung), und wie viel Spielraum hat sie?
  - LP: je innerer Flaeche f = (a, b, c) mit Gegenecken d, e der Sehnenabstand
        g_f(w) = lambda_d h_d + lambda_e h_e - sum mu_i h_i,  h = |p|^2 - w,  lambda_d + lambda_e = 1 = sum mu,
        q = lambda_d d + lambda_e e = sum mu_i p_i  (Schnittpunkt der Geraden d-e mit der Ebene von f);
        maximiere t mit g_f(w) >= t, sum w = 0 (Konstante), Kasten |w| <= 64 (a/8)^2.
  - Kammer: Breite je Koordinate, Wandgruppen (Facetten) und Zugart.
  - Gewichteter Hodge-Stern (Orthozentren) und l = 4-Anisotropie des Skalar-Laplace wie DANZER-NAEHERUNG-2
    (danzer_naeherung.operator_messen, unveraendert importiert).
Unveraendert importiert: ew.py, tp.py (TT-ISO-1), danzer_naeherung.py, licht_netz.py (DANZER-NAEHERUNG-2).
Einheiten: V-Lagen in 1/8 der kubischen Kante a (ganzzahlig), Gewichte und Margen in (a/8)^2; Hodge und Dispersion in a.

Aufruf (nur ueber kleintest.sh auf der .69):
  python rv.py rauch <aus.json>
  python rv.py lp <L> <aus.json>
  python rv.py kontrollen <aus.json>
  python rv.py kammer <L> <aus.json>
  python rv.py auswerten <aus.json> <lp1.json> <lp2.json> <kontrollen.json> <kammer1.json> <kammer2.json>
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
import scipy
from scipy.optimize import linprog
from scipy.spatial import Delaunay

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402  TT-ISO-1 (unveraendert)
import danzer_naeherung as dn  # noqa: E402  DANZER-NAEHERUNG-2 (unveraendert)
import licht_netz as ln  # noqa: E402  LICHT-FINN-NETZ-1 ueber DANZER-NAEHERUNG-2 (unveraendert)

T0 = time.time()
BOX = 64.0                   # (a/8)^2 = a^2
TOL_G = 1e-12
TOL_T = 1e-9
TOL_FACETTE = 1e-6
TOL_MU = 1e-9
KLASSEN = {'PPP|CP': 1, 'CPP|HP': 2, 'CPP|HH': 3, 'HPP|CC': 4, 'CHP|PP': 5}
JE_ZELLE = {1: 8, 2: 24, 3: 12, 4: 24, 5: 48}
HAND = {'t_max': 12.0 / 7.0, 'x': -23.0 / 7.0, 'y': -32.0 / 7.0,
        'g_w0': {1: 4.0, 2: 0.5, 3: -2.0 / 3.0, 4: 3.0, 5: 4.0},
        'g_hand': {1: 344.0 / 63.0, 2: 12.0 / 7.0, 3: 12.0 / 7.0, 4: 12.0 / 7.0, 5: 12.0 / 7.0},
        'ecken_schnitt': [(7.0, 4.0), (-5.0, -8.0), (-11.0, -8.0)]}
S_WERTE = (0.5, 0.9, 0.99)


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def schreiben(path, obj):
    obj = dict(obj)
    obj['_meta'] = {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'scipy': scipy.__version__, 'host': platform.node(), 'laufzeit_s': time.time() - T0,
                    'sha256': {f: sha(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))
                               for f in ('rv.py', 'ew.py', 'tp.py', 'danzer_naeherung.py', 'licht_netz.py')}}
    with open(path, 'w') as f:
        json.dump(ln.js(obj), f, indent=1)
    log('->', path)


# ------------------------------------------------------------------------------------------------ Netze
def netz_V(L):
    pos8, zellen = ew.geometrie('V')
    pos8 = [np.asarray(p, int) for p in pos8]
    nS = len(pos8)
    bahn_s = ['P'] * 4 + ['C'] * 2 + ['H'] * 4
    zellen_idx = list(itertools.product(range(L), repeat=3))
    cidx = {c: i for i, c in enumerate(zellen_idx)}
    n = nS * L ** 3
    home = np.zeros((n, 3))
    bahn = [''] * n
    for s in range(nS):
        for c in zellen_idx:
            g = s * L ** 3 + cidx[c]
            home[g] = pos8[s] + np.array(c) @ ew.AV8
            bahn[g] = bahn_s[s]
    tets, arten = [], []
    for c in zellen_idx:
        sh = np.array(c) @ ew.AV8
        for z in zellen:
            X = np.array([np.asarray(x, int) + sh for x in z['X8']], float)
            g = []
            for x in X:
                s, nn = ew.zerlege(x, pos8)
                g.append(s * L ** 3 + cidx[tuple(int(v) % L for v in nn)])
            tets.append((np.array(g), X))
            arten.append(z['art'])
    return {'name': 'V', 'L': L, 'n': n, 'home': home, 'bahn': bahn, 'tets': tets, 'arten': arten,
            'vol': 128.0 * L ** 3, 'periodisch': True, 'skala': 1.0 / 8.0}


def netz_zufall(saat, N=40):
    rng = np.random.default_rng([4096, 99, saat])
    P = rng.random((N, 3))
    offs = np.array(list(itertools.product((-1, 0, 1), repeat=3)), float)
    Q = (P[None, :, :] + offs[:, None, :]).reshape(-1, 3)
    gid = np.tile(np.arange(N), 27)
    tri = Delaunay(Q)
    tets = []
    for simp in tri.simplices:
        X = Q[simp]
        cen = X.mean(0)
        if np.all(cen >= 0.0) and np.all(cen < 1.0):
            tets.append((gid[simp], X.copy()))
    return {'name': 'zufall-%d' % saat, 'L': 1, 'n': N, 'home': P, 'bahn': ['X'] * N, 'tets': tets,
            'arten': ['d'] * len(tets), 'vol': 1.0, 'periodisch': True, 'skala': 1.0}


def mutter_punkte():
    w = [math.radians(a) for a in (90.0, 210.0, 330.0)]
    P2 = [(2 * math.cos(a), 2 * math.sin(a)) for a in w] + [(math.cos(a), math.sin(a)) for a in w]
    return np.array([[x, y, 0.0] for x, y in P2] + [[x, y, 1.0] for x, y in P2])


MUTTER_DREIECKE = [(3, 4, 5), (0, 1, 4), (0, 4, 3), (1, 2, 5), (1, 5, 4), (2, 0, 3), (2, 3, 5)]


def netz_mutter():
    P = mutter_punkte()
    tets = []
    for tr in MUTTER_DREIECKE:
        a, b, c = sorted(tr)
        for q in ([a, b, c, c + 6], [a, b, b + 6, c + 6], [a, a + 6, b + 6, c + 6]):
            tets.append((np.array(q), P[q].copy()))
    return {'name': 'mutter-prisma', 'L': 1, 'n': 12, 'home': P, 'bahn': ['X'] * 12, 'tets': tets,
            'arten': ['m'] * len(tets), 'vol': None, 'periodisch': False, 'skala': 1.0}


def netz_mutter_delaunay():
    rng = np.random.default_rng([4096, 98])
    P = mutter_punkte() + 1e-2 * rng.standard_normal((12, 3))
    tri = Delaunay(P)
    tets = [(np.array(s), P[s].copy()) for s in tri.simplices]
    return {'name': 'mutter-delaunay-zitter', 'L': 1, 'n': 12, 'home': P, 'bahn': ['X'] * 12, 'tets': tets,
            'arten': ['m'] * len(tets), 'vol': None, 'periodisch': False, 'skala': 1.0}


def mutter_2d_pruefung():
    P = mutter_punkte()[:6, :2]
    ori, fl = [], 0.0
    for a, b, c in MUTTER_DREIECKE:
        d = (P[b, 0] - P[a, 0]) * (P[c, 1] - P[a, 1]) - (P[b, 1] - P[a, 1]) * (P[c, 0] - P[a, 0])
        ori.append(float(np.sign(d)))
        fl += abs(d) / 2
    return {'orientierungen': ori, 'flaechensumme': fl, 'aussen': 3.0 * math.sqrt(3.0)}


# ------------------------------------------------------------------------------------------------ Topologie
def kanon(items, home, per):
    items = sorted(items, key=lambda it: (int(it[0]), tuple(np.round(it[1], 6))))
    g0, x0 = items[0]
    T = np.rint(x0 - home[g0]) if per else np.zeros(3)
    key = tuple((int(g), tuple(float(v) for v in np.round(x - T, 6))) for g, x in items)
    return key, T


def topologie(net):
    home, per = net['home'], net['periodisch']
    flaechen, kanten, tf, tk = {}, {}, [], []
    for t, (g, X) in enumerate(net['tets']):
        if len(set(int(v) for v in g)) < 4:
            raise ValueError('Tetraeder mit doppelter Ecke: %s' % (g,))
        fl = {}
        for j in range(4):
            idx = [i for i in range(4) if i != j]
            key, T = kanon([(g[i], X[i]) for i in idx], home, per)
            flaechen.setdefault(key, []).append((t, j, T))
            fl[j] = key
        ka = {}
        for (i, j) in itertools.combinations(range(4), 2):
            key, T = kanon([(g[i], X[i]), (g[j], X[j])], home, per)
            kanten.setdefault(key, []).append((t, (i, j), T))
            ka[(i, j)] = key
        tf.append(fl)
        tk.append(ka)
    vols = [abs(np.linalg.det(X[1:] - X[0])) / 6.0 for g, X in net['tets']]
    paarung = {}
    for key, lst in flaechen.items():
        paarung[len(lst)] = paarung.get(len(lst), 0) + 1
    out = {'ecken': net['n'], 'kanten': len(kanten), 'flaechen': len(flaechen), 'tetraeder': len(net['tets']),
           'flaechen_je_anzahl_tetraeder': paarung, 'volumen_summe': float(sum(vols)),
           'tet_vol_min': float(min(vols)), 'tet_vol_max': float(max(vols))}
    if per:
        out['euler'] = net['n'] - len(kanten) + len(flaechen) - len(net['tets'])
        out['volumen_soll'] = net['vol']
    return {'flaechen': flaechen, 'kanten': kanten, 'tf': tf, 'tk': tk, 'pruefung': out}


def zeilen(net, topo):
    """LP-Zeilen: g_f(w) = G0 + A w; dazu lambda, mu, Klasse, Apexhoehen."""
    n = net['n']
    rows = []
    for key, lst in topo['flaechen'].items():
        if len(lst) == 1:
            continue
        if len(lst) != 2:
            raise ValueError('Flaeche in %d Tetraedern' % len(lst))
        (t1, j1, T1), (t2, j2, T2) = lst
        ga = [k[0] for k in key]
        Pa = np.array([k[1] for k in key], float)
        g1, X1 = net['tets'][t1]
        g2, X2 = net['tets'][t2]
        gd, pd = int(g1[j1]), X1[j1] - T1
        ge, pe = int(g2[j2]), X2[j2] - T2
        ref = Pa.mean(0)
        Pa_, pd_, pe_ = Pa - ref, pd - ref, pe - ref
        M = np.column_stack([pd_ - pe_, -(Pa_[0] - Pa_[2]), -(Pa_[1] - Pa_[2])])
        sol = np.linalg.solve(M, Pa_[2] - pe_)
        ld = float(sol[0])
        le = 1.0 - ld
        mu = np.array([sol[1], sol[2], 1.0 - sol[1] - sol[2]])
        G0 = ld * pd_ @ pd_ + le * pe_ @ pe_ - sum(mu[i] * Pa_[i] @ Pa_[i] for i in range(3))
        nrm = np.cross(Pa_[1] - Pa_[0], Pa_[2] - Pa_[0])
        nrm /= np.linalg.norm(nrm)
        hd, he = abs((pd_ - Pa_[0]) @ nrm), abs((pe_ - Pa_[0]) @ nrm)
        lab = ''.join(sorted(net['bahn'][g] for g in ga)) + '|' + ''.join(sorted((net['bahn'][gd], net['bahn'][ge])))
        rows.append({'key': key, 'G0': float(G0), 'idx': [gd, ge] + ga, 'coef': [-ld, -le] + [float(v) for v in mu],
                     'ld': ld, 'le': le, 'mu': mu, 'klasse': KLASSEN.get(lab, lab), 'hd': hd, 'he': he})
    A = np.zeros((len(rows), n))
    G0 = np.zeros(len(rows))
    for r, row in enumerate(rows):
        np.add.at(A[r], row['idx'], row['coef'])
        G0[r] = row['G0']
    return rows, A, G0


def zugart(mu):
    if np.any(mu < -TOL_MU):
        return 'nicht konvex'
    nul = int(np.sum(np.abs(mu) <= TOL_MU))
    return {0: '2-3', 1: '4-4 (q auf Kante)', 2: 'Ecke (q in einer Ecke)'}.get(nul, 'entartet')


def bahnmatrix(net):
    B = np.zeros((net['n'], 3))
    for i, b in enumerate(net['bahn']):
        B[i, 'PCH'.index(b)] = 1.0
    return B


# ------------------------------------------------------------------------------------------------ LP
def lp_marge(A, G0, gauge=True, lo=None, hi=None):
    m, n = A.shape
    c = np.zeros(n + 1)
    c[-1] = -1.0
    A_ub = np.hstack([-A, np.ones((m, 1))])
    kw = {}
    if gauge:
        kw = {'A_eq': np.r_[np.ones(n), 0.0][None, :], 'b_eq': np.zeros(1)}
    if lo is None:
        bounds = [(-BOX, BOX)] * n + [(None, None)]
    else:
        bounds = [(float(a), float(b)) for a, b in zip(lo, hi)] + [(None, None)]
    r = linprog(c, A_ub=A_ub, b_ub=G0, bounds=bounds, method='highs', **kw)
    if r.status != 0:
        return {'status': int(r.status), 'meldung': r.message, 't': None, 'w': None}
    w = r.x[:n]
    if lo is None:
        kasten = bool(np.any(np.abs(w) > BOX - 1e-6))
    else:
        kasten = bool(np.any((w < np.asarray(lo) + 1e-9) | (w > np.asarray(hi) - 1e-9)))
    return {'status': 0, 't': float(r.x[-1]), 'w': w, 'kasten_aktiv': kasten}


def lp_extrem(A, G0, c_vec):
    n = A.shape[1]
    r = linprog(c_vec, A_ub=-A, b_ub=G0, A_eq=np.ones((1, n)), b_eq=np.zeros(1),
                bounds=[(-BOX, BOX)] * n, method='highs')
    if r.status != 0:
        return None
    return r.x


def lp_symmetrisch(A, G0, B):
    As = A @ B                                   # Spalten P, C, H; w_P = 0
    Axy = As[:, 1:]
    m = len(G0)
    c = np.array([0.0, 0.0, -1.0])
    r = linprog(c, A_ub=np.hstack([-Axy, np.ones((m, 1))]), b_ub=G0, bounds=[(-BOX, BOX)] * 2 + [(None, None)],
                method='highs')
    out = {'status': int(r.status), 't': float(r.x[2]), 'x': float(r.x[0]), 'y': float(r.x[1])}
    ext = {}
    for nm, cv in (('x_min', [1, 0]), ('x_max', [-1, 0]), ('y_min', [0, 1]), ('y_max', [0, -1])):
        rr = linprog(np.array(cv, float), A_ub=-Axy, b_ub=G0, bounds=[(-BOX, BOX)] * 2, method='highs')
        ext[nm] = [float(rr.x[0]), float(rr.x[1])] if rr.status == 0 else None
    out['extreme'] = ext
    return out


def wandgruppen(A, G0):
    V = np.hstack([A, G0[:, None]])
    V = V / np.linalg.norm(V, axis=1, keepdims=True)
    grp = {}
    for r in range(len(G0)):
        grp.setdefault(tuple(np.round(V[r], 9)), []).append(r)
    return list(grp.values())


def lp_facette(A, G0, r0, andere):
    n = A.shape[1]
    c = np.zeros(n + 1)
    c[-1] = -1.0
    A_ub = np.hstack([-A[andere], np.ones((len(andere), 1))])
    A_eq = np.vstack([np.r_[A[r0], 0.0], np.r_[np.ones(n), 0.0]])
    b_eq = np.array([-G0[r0], 0.0])
    r = linprog(c, A_ub=A_ub, b_ub=G0[andere], A_eq=A_eq, b_eq=b_eq, bounds=[(-BOX, BOX)] * n + [(None, None)],
                method='highs')
    if r.status != 0:
        return None
    return float(r.x[-1])


# ------------------------------------------------------------------------------------------------ Hodge
def sterne(net, topo, w):
    """Gewichtete (orthozentrische) Sterne in Einheiten a. w in Netzeinheiten^2."""
    s = net['skala']
    Ast = {k: 0.0 for k in topo['kanten']}
    dlt = {k: 0.0 for k in topo['flaechen']}
    for t, (g, X0) in enumerate(net['tets']):
        X = X0 * s
        wt = w[g] * s * s
        q = (X * X).sum(1) - wt
        z = np.linalg.solve(2.0 * (X[1:] - X[0]), q[1:] - q[0])
        cf, nu = {}, {}
        for j in range(4):
            i0, i1, i2 = [i for i in range(4) if i != j]
            e1, e2 = X[i1] - X[i0], X[i2] - X[i0]
            G = np.array([[e1 @ e1, e1 @ e2], [e1 @ e2, e2 @ e2]])
            rhs = 0.5 * np.array([e1 @ e1 + wt[i0] - wt[i1], e2 @ e2 + wt[i0] - wt[i2]])
            ab = np.linalg.solve(G, rhs)
            c = X[i0] + ab[0] * e1 + ab[1] * e2
            nv = np.cross(e1, e2)
            nv /= np.linalg.norm(nv)
            if nv @ (X[j] - X[i0]) < 0:
                nv = -nv
            cf[j] = c
            nu[j] = nv
            dlt[topo['tf'][t][j]] += (z - c) @ nv
        for (i, j) in itertools.combinations(range(4), 2):
            k, l = [m for m in range(4) if m not in (i, j)]
            e = X[j] - X[i]
            le = np.linalg.norm(e)
            eh = e / le
            cij = X[i] + (le * le + wt[i] - wt[j]) / (2 * le) * eh
            tot = 0.0
            for (a, b) in ((k, l), (l, k)):
                u = (X[a] - X[i]) - ((X[a] - X[i]) @ eh) * eh
                u /= np.linalg.norm(u)
                h1 = (cf[b] - cij) @ u               # Flaeche (i, j, a) ist die ohne b
                h2 = (z - cf[b]) @ nu[b]
                tot += 0.5 * h1 * h2
            Ast[topo['tk'][t][(i, j)]] += tot
    keys = list(topo['kanten'].keys())
    n = net['n']
    s0 = np.zeros(n)
    s1 = np.zeros(len(keys))
    gt, gh, xt, xh, lv, nv = [], [], [], [], [], []
    T1 = np.zeros((3, 3))
    for m, key in enumerate(keys):
        (ga, pa), (gb, pb) = key
        pa, pb = np.array(pa) * s, np.array(pb) * s
        d = pb - pa
        l = np.linalg.norm(d)
        A_ = Ast[key]
        s1[m] = A_ / l
        wa, wb = w[ga] * s * s, w[gb] * s * s
        s0[ga] += A_ * (l * l + wa - wb) / (2 * l) / 3.0
        s0[gb] += A_ * (l * l + wb - wa) / (2 * l) / 3.0
        T1 += A_ * l * np.outer(d / l, d / l)
        gt.append(ga)
        gh.append(gb)
        xt.append(pa)
        xh.append(pb)
    vol = net['vol'] * s ** 3
    return {'s1': s1, 's0': s0, 'delta': dlt, 'gt': np.array(gt), 'gh': np.array(gh), 'xt': np.array(xt),
            'xh': np.array(xh), 'id_vol': float(abs(s0.sum() - vol) / vol),
            'id_T1': float(np.abs(T1 / vol - np.eye(3)).max())}


def stern_kontrolle(net, topo, rows, A, G0, w, st):
    s = net['skala']
    g = (G0 + A @ w) * s * s
    dl = np.array([st['delta'][row['key']] for row in rows])
    H = np.array([2 * row['hd'] * row['he'] / (row['hd'] + row['he']) for row in rows]) * s
    return {'vorzeichen_gleich': bool(np.all(np.sign(np.round(g, 14)) == np.sign(np.round(dl, 14)))),
            'g_gegen_delta_H_max': float(np.abs(g - dl * H).max()),
            'min_s1': float(st['s1'].min()), 'min_s0': float(st['s0'].min()), 'min_delta': float(dl.min()),
            'n_s1_nichtpos': int(np.sum(st['s1'] <= 0)), 'n_s0_nichtpos': int(np.sum(st['s0'] <= 0)),
            'n_delta_nichtpos': int(np.sum(dl <= 0)), 'id_vol': st['id_vol'], 'id_T1': st['id_T1']}


def fabrik_skalar(net, st):
    n = net['n']
    gt, gh, xt, xh, s1 = st['gt'], st['gh'], st['xt'], st['xh'], st['s1']
    m12 = 1.0 / np.sqrt(st['s0'])

    def fabrik(nvec):
        def op(kv):
            pt = np.exp(1j * (xt @ kv))
            ph = np.exp(1j * (xh @ kv))
            K = np.zeros((n, n), complex)
            np.add.at(K, (gh, gh), s1)
            np.add.at(K, (gt, gt), s1)
            np.add.at(K, (gh, gt), -s1 * np.conj(ph) * pt)
            np.add.at(K, (gt, gh), -s1 * np.conj(pt) * ph)
            lam = np.linalg.eigvalsh(K * m12[:, None] * m12[None, :])[0]
            return np.array([math.sqrt(max(lam, 0.0))])
        return op
    return fabrik


def messen(net, topo, w, ref, nd, fen=None, je_richtung=False):
    st = sterne(net, topo, w)
    if np.any(st['s0'] <= 0):
        return st, None
    fen = dn.FENSTER_HAUPT if fen is None else fen
    out = dn.operator_messen('S', fabrik_skalar(net, st), 1, nd, fen, 1.0, ref)
    sk = out['skalar']
    if not je_richtung:
        sk = {k: v for k, v in sk.items() if k != 'je_richtung'}
    return st, sk


def kurz(sk):
    z = sk['a2_zerlegung']
    return {'beta': z['beta_S4'], 'rms_l4': z['rms_l4'], 'nichtkub4_rms': z['nichtkub4_rms'], 'rms_l2': z['rms_l2'],
            'rms_l6': z['rms_l6'], 'a2_mittel': z['mittel'], 'c_mittel': sk['c_mittel'],
            'c_spanne_rel': sk['c_spanne_rel'], 'fit_rms_rel_max': sk['fit_rms_rel_max'], 'zerlegung_rest': z['rest_rms']}


# ------------------------------------------------------------------------------------------------ Modi
def klassen_zaehlung(rows, L):
    z = {}
    for row in rows:
        z[row['klasse']] = z.get(row['klasse'], 0) + 1
    return {str(k): v for k, v in z.items()}, all(z.get(k, 0) == JE_ZELLE[k] * L ** 3 for k in JE_ZELLE)


def je_klasse(rows, g):
    out = {}
    for k in sorted(JE_ZELLE):
        v = np.array([g[r] for r, row in enumerate(rows) if row['klasse'] == k])
        out[str(k)] = {'min': float(v.min()), 'max': float(v.max()), 'n': int(len(v)), 'n_neg': int(np.sum(v < -TOL_G))}
    return out


def w_sym(net, x, y):
    w = bahnmatrix(net) @ np.array([0.0, x, y])
    return w - w.mean()


def modus_rauch(aus):
    res = {'versionen': {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version()}}
    for L in (1, 2):
        net = netz_V(L)
        topo = topologie(net)
        rows, A, G0 = zeilen(net, topo)
        kz, ok = klassen_zaehlung(rows, L)
        st = sterne(net, topo, np.zeros(net['n']))
        sk = stern_kontrolle(net, topo, rows, A, G0, np.zeros(net['n']), st)
        t1 = time.time()
        r = lp_marge(A, G0)
        res['V%d' % L] = {'pruefung': topo['pruefung'], 'klassen_ok': ok, 'lambda_in_0_1': bool(
            all(0 < row['ld'] < 1 for row in rows)), 'k2_vorzeichen_gleich': sk['vorzeichen_gleich'],
            'k2_g_gegen_delta_H_max': sk['g_gegen_delta_H_max'], 'k3_id_vol': sk['id_vol'], 'k3_id_T1': sk['id_T1'],
            'lp_status': r['status'], 'lp_zeit_s': time.time() - t1}
        log('V L=%d' % L, res['V%d' % L])
    net = netz_zufall(0)
    topo = topologie(net)
    res['zufall0'] = topo['pruefung']
    log('zufall0', topo['pruefung'])
    net = netz_mutter()
    topo = topologie(net)
    res['mutter'] = {'pruefung': topo['pruefung'], '2d': mutter_2d_pruefung()}
    log('mutter', res['mutter'])
    # Zeitprobe einer Messung (ohne Werte): V L=1 bei w = 0
    net = netz_V(1)
    topo = topologie(net)
    t1 = time.time()
    st, sk = messen(net, topo, np.zeros(net['n']), dn.referenzen(), dn.halbkugel(40))
    res['messung_zeit_s_L1'] = time.time() - t1
    res['messung_ok'] = sk is not None
    log('Messung L=1: %.2f s' % res['messung_zeit_s_L1'])
    schreiben(aus, res)


def modus_lp(L, aus):
    net = netz_V(L)
    topo = topologie(net)
    rows, A, G0 = zeilen(net, topo)
    kz, ok = klassen_zaehlung(rows, L)
    res = {'L': L, 'pruefung': topo['pruefung'], 'klassen': kz, 'klassen_ok': ok,
           'lambda_in_0_1': bool(all(0 < row['ld'] < 1 for row in rows))}
    # w = 0
    res['w0'] = je_klasse(rows, G0)
    neg = [r for r in range(len(rows)) if G0[r] < -TOL_G]
    sneg = set(neg)
    res['w0_verletzt'] = {'anzahl': len(neg), 'klassen': sorted(set(rows[r]['klasse'] for r in neg)),
                          'uebrige_min': float(min(G0[r] for r in range(len(rows)) if r not in sneg))}
    # Handpunkt
    wh = w_sym(net, HAND['x'], HAND['y'])
    res['w_hand'] = je_klasse(rows, G0 + A @ wh)
    # LP voll
    r = lp_marge(A, G0)
    w_opt = r['w']
    B = bahnmatrix(net)
    zb = np.linalg.lstsq(B, w_opt, rcond=None)[0]
    w_s = B @ zb
    res['lp'] = {'status': r['status'], 't_max': r['t'], 'kasten_aktiv': r['kasten_aktiv'], 'w_opt': w_opt,
                 'bahnmittel_P_C_H': zb, 'x_sym': float(zb[1] - zb[0]), 'y_sym': float(zb[2] - zb[0]),
                 'marge_bahnmittel': float((G0 + A @ (w_s - w_s.mean())).min()),
                 'w_opt_symmetrisch_abw': float(np.abs(w_opt - w_s).max())}
    log('LP voll: status', r['status'])
    # LP symmetrisch
    res['lp_sym'] = lp_symmetrisch(A, G0, B)
    log('LP sym: status', res['lp_sym']['status'])
    # Kammerbreite je Koordinate
    rng_ = []
    for i in range(net['n']):
        c = np.zeros(net['n'])
        c[i] = 1.0
        lo = lp_extrem(A, G0, c)
        hi = lp_extrem(A, G0, -c)
        rng_.append((float(lo[i]) if lo is not None else None, float(hi[i]) if hi is not None else None))
    res['koordinaten'] = rng_
    zus = {}
    for b in 'PCH':
        lo = [rng_[i][0] for i in range(net['n']) if net['bahn'][i] == b]
        hi = [rng_[i][1] for i in range(net['n']) if net['bahn'][i] == b]
        zus[b] = {'min': min(lo), 'max': max(hi), 'breite_max': max(h - l for l, h in zip(lo, hi)),
                  'breite_min': min(h - l for l, h in zip(lo, hi))}
    res['koordinaten_je_bahn'] = zus
    res['kammer_dimension'] = net['n'] - 1
    log('Koordinaten fertig')
    # Wandgruppen
    gr = wandgruppen(A, G0)
    fac = []
    for G in gr:
        sG = set(G)
        andere = np.array([r_ for r_ in range(len(rows)) if r_ not in sG])
        tau = lp_facette(A, G0, G[0], andere)
        fac.append({'zeilen': len(G), 'klasse': rows[G[0]]['klasse'], 'zugart': zugart(rows[G[0]]['mu']),
                    'tau': tau, 'facette': bool(tau is not None and tau > TOL_FACETTE)})
    zf = {}
    for f in fac:
        k = str(f['klasse'])
        e = zf.setdefault(k, {'gruppen': 0, 'facetten': 0, 'zeilen_je_gruppe': set(), 'zugarten': set(),
                              'tau_max': -1e300})
        e['gruppen'] += 1
        e['facetten'] += int(f['facette'])
        e['zeilen_je_gruppe'].add(f['zeilen'])
        e['zugarten'].add(f['zugart'])
        if f['tau'] is not None:
            e['tau_max'] = max(e['tau_max'], f['tau'])
    for e in zf.values():
        e['zeilen_je_gruppe'] = sorted(e['zeilen_je_gruppe'])
        e['zugarten'] = sorted(e['zugarten'])
    res['wandgruppen'] = zf
    res['wandgruppen_anzahl'] = len(gr)
    log('Wandgruppen fertig:', len(gr))
    # Zugart je Klasse aus mu
    res['zugart_je_klasse'] = {str(k): sorted(set(zugart(row['mu']) for row in rows if row['klasse'] == k))
                               for k in JE_ZELLE}
    schreiben(aus, res)


def modus_kontrollen(aus):
    res = {}
    zuf = []
    for s in range(3):
        net = netz_zufall(s)
        topo = topologie(net)
        rows, A, G0 = zeilen(net, topo)
        r = lp_marge(A, G0)
        zuf.append({'saat': s, 'pruefung': topo['pruefung'], 'g0_min': float(G0.min()), 'n_neg': int(np.sum(G0 < TOL_G)),
                    'zulaessig': bool(np.all(G0 > TOL_G)), 'lp_t_max': r['t'], 'lp_kasten': r.get('kasten_aktiv')})
        log('zufall', s, topo['pruefung']['euler'], topo['pruefung']['flaechen_je_anzahl_tetraeder'])
    res['b_zufall'] = zuf
    for nm, net in (('c_mutter', netz_mutter()), ('c2_mutter_delaunay', netz_mutter_delaunay())):
        topo = topologie(net)
        rows, A, G0 = zeilen(net, topo)
        p2 = (net['home'] ** 2).sum(1)
        r = lp_marge(A, G0, gauge=False, lo=p2 - 1.0, hi=p2 + 1.0)
        res[nm] = {'pruefung': topo['pruefung'], 'innere_flaechen': len(rows), 'lp_status': r['status'],
                   't_max': r['t'], 'kasten_aktiv': r.get('kasten_aktiv'), 'g0_min': float(G0.min())}
        log(nm, r['status'])
    res['c_mutter']['2d'] = mutter_2d_pruefung()
    schreiben(aus, res)


def strahl_wand(A, G0, w_mid, d):
    kap = A @ d
    g = G0 + A @ w_mid
    m = kap < -1e-14
    return float(np.min(g[m] / (-kap[m])))


def modus_kammer(L, aus):
    ref = dn.referenzen()
    nd = dn.halbkugel(40)
    net1 = netz_V(1)
    topo1 = topologie(net1)
    rows1, A1, G01 = zeilen(net1, topo1)
    sy = lp_symmetrisch(A1, G01, bahnmatrix(net1))
    xm, ym = sy['x'], sy['y']
    net = net1 if L == 1 else netz_V(L)
    topo = topo1 if L == 1 else topologie(net)
    rows, A, G0 = (rows1, A1, G01) if L == 1 else zeilen(net, topo)
    w_mid = w_sym(net, xm, ym)
    res = {'L': L, 'x_mid': xm, 'y_mid': ym, 'marge_mid': float((G0 + A @ w_mid).min()), 'ref_kontrolle': ref['kontrolle']}
    proben = []

    def probe(gruppe, w, info):
        st, sk = messen(net, topo, w, ref, nd)
        kk = stern_kontrolle(net, topo, rows, A, G0, w, st)
        rec = {'gruppe': gruppe, 'marge': float((G0 + A @ w).min()), 'sterne': kk}
        rec.update(info)
        if sk is not None:
            rec.update(kurz(sk))
        proben.append(rec)

    # Mitte (mit je_richtung), Probe-Fenster, w = 0 (beschreibend)
    st, sk = messen(net, topo, w_mid, ref, nd, je_richtung=True)
    res['mitte'] = kurz(sk)
    res['mitte_je_richtung'] = sk['je_richtung']
    res['mitte_sterne'] = stern_kontrolle(net, topo, rows, A, G0, w_mid, st)
    st, sk = messen(net, topo, w_mid, ref, nd, fen=dn.FENSTER_PROBE)
    res['mitte_probefenster'] = kurz(sk)
    w0 = np.zeros(net['n'])
    st, sk = messen(net, topo, w0, ref, nd)
    res['w0'] = kurz(sk) if sk is not None else None
    res['w0_sterne'] = stern_kontrolle(net, topo, rows, A, G0, w0, st)
    log('Mitte und w=0 fertig')
    # Zufallsgewichte fuer K2
    rk = np.random.default_rng([4096, L, 3])
    res['k2_zufall'] = []
    for j in range(3):
        wz = w_mid + 0.5 * rk.standard_normal(net['n'])
        stz = sterne(net, topo, wz)
        res['k2_zufall'].append(stern_kontrolle(net, topo, rows, A, G0, wz, stz))
    if L == 1:
        # S1 symmetrisch
        E = HAND['ecken_schnitt']
        ziele = [('ecke', e) for e in E] + [('kantenmitte', ((E[a][0] + E[b][0]) / 2, (E[a][1] + E[b][1]) / 2))
                                             for a, b in ((0, 1), (1, 2), (2, 0))]
        for nm, (xz, yz) in ziele:
            for s in S_WERTE:
                probe('S1', w_sym(net, xm + s * (xz - xm), ym + s * (yz - ym)), {'ziel': nm, 'xy': (xz, yz), 's': s})
        log('S1 fertig')
    # S2 / S4 Zufallsrichtungen
    rng = np.random.default_rng([4096, L, 7])
    nr = 40 if L == 1 else 16
    for j in range(nr):
        d = rng.standard_normal(net['n'])
        d -= d.mean()
        d /= np.linalg.norm(d)
        sw = strahl_wand(A, G0, w_mid, d)
        for s in S_WERTE:
            probe('S2' if L == 1 else 'S4', w_mid + s * sw * d, {'richtung': j, 's': s, 's_wand': sw})
    log('Zufallsrichtungen fertig')
    if L == 1:
        # S3 Kammerecken (LP-Extreme)
        for i in range(net['n']):
            for sinn in (1.0, -1.0):
                c = np.zeros(net['n'])
                c[i] = sinn
                we = lp_extrem(A, G0, c)
                if we is None:
                    continue
                probe('S3', w_mid + 0.99 * (we - w_mid), {'ecke_index': i, 'sinn': 'min' if sinn > 0 else 'max',
                                                          'w_ext_i': float(we[i]), 's': 0.99})
        log('S3 fertig')
    else:
        # K4: Mitte gekachelt (gleich w_mid)
        res['k4_mitte_L2'] = res['mitte']
    res['proben'] = proben
    schreiben(aus, res)


# ------------------------------------------------------------------------------------------------ Auswertung
def urteilen(lp1, lp2, ko, ka1, ka2):
    U = {}
    # RV0
    a = all(lp['w0_verletzt']['anzahl'] == 12 * lp['L'] ** 3 and lp['w0_verletzt']['klassen'] == [3]
            and lp['w0_verletzt']['uebrige_min'] > TOL_G for lp in (lp1, lp2))
    b = all(z['zulaessig'] for z in ko['b_zufall'])
    c = ko['c_mutter']['t_max'] is not None and ko['c_mutter']['t_max'] <= TOL_T
    c2 = ko['c2_mutter_delaunay']['t_max'] is not None and ko['c2_mutter_delaunay']['t_max'] > 1e-6
    U['RV0'] = {'a_V_w0': a, 'b_zufall': b, 'c_mutter': c, 'c2_positivkontrolle': c2,
                'urteil': ('nicht auswertbar' if not c2 else ('eingetroffen' if (a and b and c) else 'nicht eingetroffen'))}
    # RV1
    t1, t2 = lp1['lp']['t_max'], lp2['lp']['t_max']
    if t1 > TOL_T and t2 > TOL_T:
        u1 = 'eingetroffen'
    elif t1 <= TOL_T and t2 <= TOL_T:
        u1 = 'nicht eingetroffen'
    else:
        u1 = 'L-abhaengig'
    U['RV1'] = {'t_max_L1': t1, 't_max_L2': t2, 'urteil': u1, 'L_gleich': abs(t1 - t2) <= 1e-7 * max(1, abs(t1))}
    # RV2
    ts = lp1['lp_sym']['t']
    if u1 == 'eingetroffen':
        U['RV2'] = {'t_sym': ts, 'urteil': 'eingetroffen' if ts > TOL_T else 'nicht eingetroffen',
                    'zusatz_beste_marge_symmetrisch': abs(ts - t1) <= 1e-7}
    else:
        U['RV2'] = {'t_sym': ts, 'urteil': 'entfaellt'}
    # RV3
    bm = ka1['mitte']['beta']
    rm = ka1['mitte']['rms_l4']
    pr = [p for p in ka1['proben'] + ka2['proben']]
    gueltig = [p for p in pr if 'beta' in p and p['sterne']['n_delta_nichtpos'] == 0 and p['sterne']['n_s0_nichtpos'] == 0]
    aus_kammer = len(pr) - len(gueltig)
    if abs(bm) < 1e-12:
        U['RV3'] = {'urteil': 'nicht auswertbar', 'beta_mid': bm}
    else:
        db = [abs(p['beta'] - bm) / abs(bm) for p in gueltig]
        dr = [abs(p['rms_l4'] - rm) / abs(rm) for p in gueltig]
        jb, jr = int(np.argmax(db)), int(np.argmax(dr))
        grp = {}
        for p, v in zip(gueltig, db):
            k = '%s s=%s' % (p['gruppe'], p['s'])
            grp[k] = max(grp.get(k, 0.0), v)
        U['RV3'] = {'beta_mid': bm, 'rms_l4_mid': rm, 'n_proben': len(gueltig), 'n_ausserhalb': aus_kammer,
                    'delta_beta_max': max(db), 'ort_beta_max': {k: v for k, v in gueltig[jb].items() if k != 'sterne'},
                    'delta_rms_l4_max': max(dr), 'ort_rms_l4_max': {k: v for k, v in gueltig[jr].items() if k != 'sterne'},
                    'delta_beta_je_gruppe': grp,
                    'urteil_plan': 'eingetroffen' if max(db) < 0.10 else 'nicht eingetroffen',
                    'urteil_wortlaut_rms_l4': 'eingetroffen' if max(dr) < 0.10 else 'nicht eingetroffen'}
    # Kontrollen K4, K5
    k5 = {'t_L1': abs(t1 - HAND['t_max']) <= 1e-7, 't_L2': abs(t2 - HAND['t_max']) <= 1e-7,
          't_sym': abs(ts - HAND['t_max']) <= 1e-7,
          'x_sym': abs(lp1['lp_sym']['x'] - HAND['x']) <= 1e-6, 'y_sym': abs(lp1['lp_sym']['y'] - HAND['y']) <= 1e-6}
    for nm, soll in (('w0', HAND['g_w0']), ('w_hand', HAND['g_hand'])):
        for k, v in soll.items():
            e = lp1[nm][str(k)]
            k5['%s_klasse%d' % (nm, k)] = abs(e['min'] - v) <= 1e-9 and abs(e['max'] - v) <= 1e-9
    ex = lp1['lp_sym']['extreme']
    k5['schnitt_x'] = abs(ex['x_min'][0] + 11) <= 1e-6 and abs(ex['x_max'][0] - 7) <= 1e-6
    k5['schnitt_y'] = abs(ex['y_min'][1] + 8) <= 1e-6 and abs(ex['y_max'][1] - 4) <= 1e-6
    U['K5_hand'] = k5
    U['K5_alle'] = all(k5.values())
    U['K4'] = {'beta_L1': bm, 'beta_L2_mitte': ka2['k4_mitte_L2']['beta'],
               'rel': abs(ka2['k4_mitte_L2']['beta'] - bm) / max(abs(bm), 1e-300)}
    U['K4']['ok'] = U['K4']['rel'] <= 1e-8
    return U


def modus_auswerten(aus, ein):
    lp1, lp2, ko, ka1, ka2 = [json.load(open(p)) for p in ein]
    U = urteilen(lp1, lp2, ko, ka1, ka2)
    for k, v in U.items():
        log(k, json.dumps(ln.js(v))[:600])
    schreiben(aus, {'urteile': U, 'eingaben': {p: sha(p) for p in ein}})


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return 2
    if a[0] == 'rauch':
        modus_rauch(a[1])
    elif a[0] == 'lp':
        modus_lp(int(a[1]), a[2])
    elif a[0] == 'kontrollen':
        modus_kontrollen(a[1])
    elif a[0] == 'kammer':
        modus_kammer(int(a[1]), a[2])
    elif a[0] == 'auswerten':
        modus_auswerten(a[1], a[2:])
    else:
        print(__doc__)
        return 2
    log('fertig')
    return 0


if __name__ == '__main__':
    sys.exit(main())
