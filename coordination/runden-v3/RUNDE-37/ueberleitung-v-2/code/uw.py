#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-V-2 (fmhc-physics, Runde 49), Code-Agent fuer die Leitung claude-primary.

Stetige Grenze der Zeltstangen-Wirkung (Hauptwert h = 2^-10, Kontrollen 2^-8 und 2^-12; Schema ls, Fassung B) auf den
Netzen V (V-A), S (S-A) und B1 (B1-t1); M_eff, negative Richtungen, Regime H mit M_eff und R1, Messziel h*(k).
Plan: PLAN.md. Importiert uv.py (UEBERLEITUNG-V-1, eingefroren) und die Vorlagen unveraendert; erweitert wird nur die
Netzwahl (uv.baue_gitter fuer S und B1) und die Auswertung.

Modi:
  rauch1     technische Kontrollen je Netz (K1 bis K5, K7, K8, Netzgroessen, Laufzeit); keine Spektren, keine Zaehlungen
  punkte     --netz V|S|B1 --menge raster|rasterbz|neu [--teil 0|1|2]: Bloecke bei H3, Konvergenz, M_eff, Paarungen
  hstern     --richtung 100|111|321: n_D(h) auf dem h-Raster 2^(-j/8), Bisektion (PLAN 6)
  auswertung Urteile UW0 bis UW4 nach PLAN 5, Messziel (PLAN 6)
"""
import argparse, json, sys, os, time, platform, resource, itertools
import numpy as np
import scipy

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import uv  # noqa: E402  (UEBERLEITUNG-V-1, eingefroren, unveraendert)
import rk  # noqa: E402
import rk2  # noqa: E402
import tg  # noqa: E402
import hm  # noqa: E402
import tti  # noqa: E402
import tp  # noqa: E402

H3 = [2.0 ** -8, 2.0 ** -10, 2.0 ** -12]
IH = 1                                   # Index des Hauptwerts 2^-10
TOL_NULL = 1e-10
NECK = {'V': 10, 'S': 6, 'B1': 4}         # Ecken je Grundzelle (PLAN 1)
W_X0 = uv.lagrange0(H3)                   # quadratisch durch die drei h, ausgewertet bei h = 0 (beschreibend)
KONV_MAX = 1e-2
UW2_MIN = 0.9
HS_J = 112                                # h_j = 2^(-j/8), j = 0..112
HS_BIS = 10
HS_KL = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, float(np.pi)]
VARS = ('a', 'a12', 'a0', 'aC')

herm, fro = uv.herm, uv.fro
_baue_alt = uv.baue_gitter


def baue_gitter2(netz, h):
    """Netzwahl (PLAN 1): V und KW unveraendert aus uv; S-A wie REGIME-K-2 (Hubfolge A); B1-t1 wie REGIME-K-1."""
    if netz in ('V', 'KW'):
        return _baue_alt(netz, h)
    if netz == 'S':
        xb, tets, arten = rk2.netz_raum('S')
        NV = len(xb)
        rang = {b: b for b in range(NV)}
        hb = [rang[b] / float(NV) for b in range(NV)]
        return rk.Gitter('S-A', xb, hb, tp.AV.T, tets, rk2.ord_rang(rang), h)
    if netz == 'B1':
        return rk.baue('B1', tau=h)
    raise ValueError(netz)


uv.baue_gitter = baue_gitter2            # uv.Vier.__init__ ruft uv.baue_gitter (Name im Modul uv)


def netz3d2(netz):
    if netz == 'V':
        return uv.netz3d('V')
    if netz == 'S':
        LV, pos, G, O, info = hm.netz('S')
        return tg.modell(LV, pos, G, O, {}), None, LV
    if netz == 'B1':
        tets, info = rk.b1_raum()
        G = np.array([[b for (b, n) in T] for T in tets], np.int64)
        O = np.array([[list(n) for (b, n) in T] for T in tets], np.int64)
        LV = np.eye(3)
        return tg.modell(LV, np.array(rk.XB_B1, float), G, O, {}), None, LV
    raise ValueError(netz)


def bau(netz, hs=H3):
    t0 = time.time()
    vl = [uv.Vier(netz, h) for h in hs]
    mod, geo, LV = netz3d2(netz)
    zu = uv.Zuordnung(vl[0], mod, LV)
    return vl, mod, LV, zu, time.time() - t0


# ================================================================================================= 4D-Bloecke
def bloecke2(V, ks, pmax=2):
    """Wie uv.Vier.bloecke (Schema ls), zusaetzlich die Eigenwerte von D_0 (Zahl negativ, kleinster vorzeichenbehaftet)."""
    h = V.h
    C = V.lau.koeff(np.asarray(ks, float))
    lD = V.g.l
    Ca = {m: lD[:, None] * Cm * lD[None, :] for m, Cm in C.items()}
    fak = [1.0, 1.0, 2.0, 6.0, 24.0]
    Hp = [sum(Ca[m] * (1j * m * h) ** p for m in Ca) / fak[p] for p in range(pmax + 1)]
    Jm, nL, rB = V.J_mats(ks, 'ls')
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
    nK = V.nq + 4 * V.NV
    IK = list(range(nK))
    IL = list(range(nK, nK + nL))
    rows_live = [e for e in range(V.NE) if e not in V.tot]
    sv = np.linalg.svd(Jp[0][rows_live], compute_uv=False)
    diag = {'rang_B_s': rB, 'n_L': nL, 'J_sv_min_rel': float(sv[-1] / sv[0]),
            'J_rang_ok': bool(sv[-1] > 1e-10 * sv[0] and Jp[0].shape[1] <= len(rows_live) and rB == 3 * V.NV)}
    if not diag['J_rang_ok']:
        diag['grund'] = 'schema_rang'
        return None, diag
    A = [Pp[np.ix_(IK, IK)] for Pp in P]
    B = [Pp[np.ix_(IK, IL)] for Pp in P]
    Bt = [Pp[np.ix_(IL, IK)] for Pp in P]
    D = [Pp[np.ix_(IL, IL)] for Pp in P]
    evD = np.linalg.eigvalsh(herm(D[0]))
    amax = float(np.abs(evD).max())
    diag.update({'D0_min_rel': float(np.abs(evD).min() / amax), 'D0_n_neg': int((evD < 0).sum()),
                 'D0_eig_min_rel': float(evD.min() / amax), 'D0_absmax': amax})
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


def d0_eig(V, ks):
    """Nur D_0 = P_0[L, L] (PLAN 6): Eigenwerte (hermitesch), oder None bei Rangverlust von B_s."""
    C = V.lau.koeff(np.asarray(ks, float))
    lD = V.g.l
    H0 = sum(lD[:, None] * Cm * lD[None, :] for Cm in C.values())
    Jm, nL, rB = V.J_mats(ks, 'ls')
    if rB != 3 * V.NV:
        return None
    J0 = sum(Jm.values())
    JL = J0[:, V.nq + 4 * V.NV:]
    D0 = -(np.conj(JL.T) @ H0 @ JL) / V.h
    return np.linalg.eigvalsh(herm(D0))


def traegheit(ev):
    s = float(np.abs(ev).max())
    return [int((ev < -TOL_NULL * s).sum()), int((np.abs(ev) <= TOL_NULL * s).sum()), int((ev > TOL_NULL * s).sum())]


def wh_matrix(mod, ks):
    """Spalten = oertliche Dehnungsrichtungen je Ecke (PLAN 5, UW2): wie Wh in tg.ops."""
    E, nV = mod['E'], mod['nV']
    phe = np.exp(1j * (mod['Tedge'] @ ks))
    W = np.zeros((E, nV), complex)
    np.add.at(W, (np.arange(E), mod['es']), 1.0)
    np.add.at(W, (np.arange(E), mod['es2']), phe)
    return W


def projektion(Meff, Dq):
    ev, Uv = np.linalg.eigh(Meff)
    s = float(np.abs(ev).max())
    N = Uv[:, ev < -TOL_NULL * s]
    if N.shape[1] == 0:
        return None, None, 0
    X = np.conj(Dq.T) @ N
    cs = np.linalg.svd(X, compute_uv=False)
    return float(fro(X) ** 2 / N.shape[1]), float(cs.min() ** 2) if N.shape[1] <= Dq.shape[1] else 0.0, int(N.shape[1])


def punkt2(vl, mod, zu, ks, uw2=False):
    """Ein k (PLAN 2, 3, 5): Bloecke bei H3, Konvergenz, Traegheit, Paarungen, UW2-Projektion."""
    t0 = time.time()
    ks = np.asarray(ks, float)
    eps = float(np.linalg.norm(ks))
    Bs, A1s, M, c = tg.ops(mod, ks)
    B = herm(Bs.toarray())
    U = zu.U(ks)
    UH = np.conj(U.T)
    V0 = vl[0]
    nq, NV = V0.nq, V0.NV
    IQ = list(range(nq)); IN = list(range(nq, nq + NV)); IB = list(range(nq + NV, nq + 4 * NV))
    out = {'k': [float(x) for x in ks], 'eps': eps, 'K4_Mdisp': fro(UH @ uv.M_disp_rk(V0, ks) - M) / fro(M)}
    Sh, dg = [], []
    for V in vl:
        S, d = bloecke2(V, ks)
        Sh.append(S)
        dg.append(d)
    out['D0'] = [{x: d.get(x) for x in ('D0_n_neg', 'D0_eig_min_rel', 'D0_min_rel', 'D0_absmax', 'grund')} for d in dg]
    out['rang_B_s'] = sorted(set(d['rang_B_s'] for d in dg))
    out['J_sv_min_rel'] = float(min(d['J_sv_min_rel'] for d in dg))
    if any(S is None for S in Sh):
        g = ','.join(sorted(set(d.get('grund', '') for d in dg if d.get('grund'))))
        out.update({'definiert': False, 'grund': g, 'konvergent': False, 'traegheit_stabil': False,
                    'ls': {'sp': {v: {'definiert': False, 'grund': 'bloecke:' + g} for v in VARS}}})
        out['t_s'] = time.time() - t0
        return out
    out['definiert'] = True
    Q = []
    for S in Sh:
        Q.append({'M': herm(UH @ S[2][np.ix_(IQ, IQ)] @ U), 'V': herm(UH @ S[0][np.ix_(IQ, IQ)] @ U),
                  'C': UH @ S[0][np.ix_(IQ, IN)], 'X': UH @ S[1][np.ix_(IQ, IB)]})
    out['K6_herm'] = float(max(fro(S[2][np.ix_(IQ, IQ)] - np.conj(S[2][np.ix_(IQ, IQ)].T)) / fro(S[2][np.ix_(IQ, IQ)])
                               for S in Sh))
    r8 = {nm: fro(Q[0][nm] - Q[1][nm]) / fro(Q[1][nm]) for nm in Q[1]}
    r12 = {nm: fro(Q[2][nm] - Q[1][nm]) / fro(Q[1][nm]) for nm in Q[1]}
    out['r8'], out['r12'] = r8, r12
    out['p_h'] = {nm: (float(np.log2(r8[nm] / r12[nm]) / 2.0) if r8[nm] > 0 and r12[nm] > 0 else None) for nm in r8}
    evs = [np.linalg.eigvalsh(q['M']) for q in Q]
    tr = [traegheit(ev) for ev in evs]
    out['traegheit'] = tr
    out['Meff_eig'] = [float(x) for x in evs[IH]]
    out['Meff_absmin_rel'] = [float(np.abs(ev).min() / np.abs(ev).max()) for ev in evs]
    out['dM12_2norm_rel'] = float(np.linalg.norm(Q[2]['M'] - Q[1]['M'], 2) / np.abs(evs[IH]).max())
    d0pd = all(d.get('D0_eig_min_rel') is not None and d['D0_eig_min_rel'] > 1e-10 for d in dg)
    out['D0_pd_alle_h'] = bool(d0pd)
    out['konvergent'] = bool(d0pd and r12['M'] <= KONV_MAX and r12['M'] <= max(r8['M'], 1e-10))
    out['traegheit_stabil'] = bool(tr[0] == tr[1] == tr[2])
    Mx0 = herm(sum(W_X0[j] * Q[j]['M'] for j in range(3)))
    out['traegheit_x0'] = traegheit(np.linalg.eigvalsh(Mx0))
    sp = {'a': uv.reduktion(Q[IH]['M'], B, c, M, eps, TOL_NULL),
          'a12': uv.reduktion(Q[2]['M'], B, c, M, eps, TOL_NULL),
          'a0': uv.reduktion(Mx0, B, c, M, eps, TOL_NULL),
          'aC': uv.reduktion(Q[IH]['M'], B, Q[IH]['C'], M, eps, TOL_NULL)}
    for v in sp.values():
        v.pop('_vek', None)
    out['ls'] = {'sp': sp}
    # ADM-Form (beschreibend, PLAN 7)
    S = Sh[IH]
    out['r_V'] = fro(Q[IH]['V'] - B) / fro(B)
    kap = np.vdot(c, Q[IH]['C']) / np.vdot(c, c)
    out['kappa'] = [float(kap.real), float(kap.imag)]
    out['C_rest_kappa'] = fro(Q[IH]['C'] - kap * c) / fro(Q[IH]['C'])
    out['G_rel'] = fro(S[1][np.ix_(IQ, IQ)]) * eps / max(fro(Q[IH]['V']), 1e-300)
    out['nn_rel'] = fro(S[0][np.ix_(IN, IN)]) / max(fro(S[0][np.ix_(IQ, IN)]), 1e-300)
    if uw2:
        Wv = wh_matrix(mod, ks)
        Ud, sd, _ = np.linalg.svd(Wv, full_matrices=False)
        rW = int((sd > 1e-9 * sd[0]).sum())
        Dq = Ud[:, :rW]
        z = {'rang_Wh': rW}
        for tag, j in (('10', IH), ('12', 2), ('8', 0)):
            P, cmin, nn = projektion(Q[j]['M'], Dq)
            z['P' + tag], z['cos2_min' + tag], z['n_neg' + tag] = P, cmin, nn
        P, cmin, nn = projektion(Mx0, Dq)
        z['Px0'], z['cos2_minx0'] = P, cmin
        out['uw2'] = z
    out['t_s'] = time.time() - t0
    return out


# ================================================================================================= k-Mengen
def raster_kl(lm):
    return [p for p in uv.raster(lm) if p['art'] == 'kl']


def bz_netz(netz, LV):
    pts = uv.bz(LV)
    if netz in ('V', 'S'):
        pts = pts + uv.extra_V()
    return pts


def fib_richtungen(n=60):
    ga = np.pi * (3.0 - np.sqrt(5.0))
    out = []
    for i in range(n):
        z = 1.0 - (2 * i + 1) / float(n)
        r = np.sqrt(1.0 - z * z)
        out.append(np.array([r * np.cos(i * ga), r * np.sin(i * ga), z]))
    return out


def ws_rand(d, BVc):
    best = np.inf
    for n in itertools.product(range(-2, 3), repeat=3):
        if not any(n):
            continue
        G = np.array(n, float) @ BVc
        dg = float(d @ G)
        if dg > 1e-12:
            best = min(best, float(G @ G) / (2.0 * dg))
    return best * d


def neu_V(lm, LV):
    """PLAN 4: 1484 neue k fuer UW4 (R, W, G16R, G16I), mit Ausschlusspruefung gegen die 591 Nachtrag-k."""
    BVc = 2 * np.pi * np.linalg.inv(LV).T
    F = fib_richtungen(60)
    d13 = np.array([d for _, d in tti.richtungen13()])
    cmax = float(np.abs(np.array(F) @ d13.T).max())
    assert cmax < 1 - 1e-9, cmax
    pts = []
    for i, d in enumerate(F):
        for kl in uv.KL_RASTER:
            pts.append({'menge': 'R', 'ridx': i, 'richtung': 'fib%02d' % i, 'kl': kl, 'art': 'kl', 'rand': False,
                        'ks': (kl / lm) * d})
    for i, d in enumerate(F):
        pts.append({'menge': 'W', 'ridx': i, 'name': 'W%02d' % i, 'art': 'ws', 'rand': True, 'ks': ws_rand(d, BVc)})
    for m in itertools.product(range(16), repeat=3):
        if any(x == 8 for x in m) and any(x % 2 for x in m):
            pts.append({'menge': 'G16R', 'name': 'G16:%d,%d,%d' % m, 'art': 'g16', 'rand': True,
                        'ks': (np.array(m, float) / 16) @ BVc})
    for m in itertools.product(range(1, 16, 2), repeat=3):
        pts.append({'menge': 'G16I', 'name': 'G16:%d,%d,%d' % m, 'art': 'g16', 'rand': False,
                    'ks': (np.array(m, float) / 16) @ BVc})
    alt = [p['ks'] for p in raster_kl(lm)] + [p['ks'] for p in bz_netz('V', LV)]
    ra = np.array(alt) @ LV.T / (2 * np.pi)
    rn = np.array([p['ks'] for p in pts]) @ LV.T / (2 * np.pi)
    dd = rn[:, None, :] - ra[None, :, :]
    dd = np.abs(dd - np.round(dd)).max(axis=2)
    assert len(alt) == 591 and float(dd.min()) > 1e-9, (len(alt), float(dd.min()))
    return pts, {'n_neu': len(pts), 'cos_max_gegen_13': cmax, 'abstand_min_gegen_591': float(dd.min()),
                 'je_menge': {mg: sum(1 for p in pts if p['menge'] == mg) for mg in ('R', 'W', 'G16R', 'G16I')}}


def teil_von(pts, teil, nteil=3):
    n = len(pts)
    a, b = (n * teil) // nteil, (n * (teil + 1)) // nteil
    return pts[a:b]


# ================================================================================================= Laeufe
def lauf_punkte(netz, menge, teil, probe):
    vl, mod, LV, zu, tb = bau(netz)
    lm = float(mod['l'].mean())
    erg = {'netz': netz, 'menge': menge, 'teil': teil, 'h': H3, 'l_mittel': lm, 't_aufbau_s': tb,
           'struktur': {'NE': vl[0].NE, 'NV': vl[0].NV, 'nq': vl[0].nq, 'n_diag': len(vl[0].diag),
                        'tot': sorted(vl[0].tot), 'n_lebend_diag': int(vl[0].lebend.sum())},
           'pruefung_3d': {x: mod['pruefung'][x] for x in ('T', 'E', 'nV', 'dieder_summe_minus_2pi_max', 'Vbox',
                                                           'selbstkanten')}}
    if menge == 'raster':
        pts = raster_kl(lm)
    elif menge == 'rasterbz':
        pts = raster_kl(lm) + bz_netz(netz, LV)
    elif menge == 'neu':
        alle, info = neu_V(lm, LV)
        erg['neu_info'] = info
        pts = teil_von(alle, teil)
    else:
        raise ValueError(menge)
    if probe:
        pts = pts[:2] + pts[-1:]
    if menge != 'neu' or teil == 0:
        erg['kontrollen'] = uv.kontrollen(vl, mod, LV, zu)
    out = []
    for p in pts:
        uw2 = p.get('art') == 'kl' and p.get('kl', 1.0) <= 0.1 + 1e-12
        r = punkt2(vl, mod, zu, p['ks'], uw2=uw2)
        r.update({x: y for x, y in p.items() if x != 'ks'})
        out.append(r)
    erg['punkte'] = out
    return erg


def lauf_hstern(richtung, probe):
    """PLAN 6: n_D(h) auf h_j = 2^(-j/8), j = 0..112, je k; Bisektion fuer h*_letzt und h*_erst."""
    R = dict(tti.richtungen13())
    mod, geo, LV = netz3d2('V')
    lm = float(mod['l'].mean())
    d = R[richtung]
    kls = HS_KL if not probe else HS_KL[:1]
    J = HS_J if not probe else 16
    ks_l = [(kl / lm) * d for kl in kls]
    js = list(range(J + 1))
    hs = [2.0 ** (-j / 8.0) for j in js]
    nD = np.zeros((len(ks_l), len(js)), int)
    dmin = np.zeros((len(ks_l), len(js)))
    t0 = time.time()
    for jj, h in enumerate(hs):
        V = uv.Vier('V', h)
        for i, ks in enumerate(ks_l):
            ev = d0_eig(V, ks)
            if ev is None:
                nD[i, jj] = -1
                continue
            nD[i, jj] = int((ev < 0).sum())
            dmin[i, jj] = float(ev.min() / np.abs(ev).max())
    t_raster = time.time() - t0

    def zahl(h, ks):
        ev = d0_eig(uv.Vier('V', h), ks)
        return -1 if ev is None else int((ev < 0).sum())

    out = []
    for i, ks in enumerate(ks_l):
        z = {'kl': kls[i], 'k': [float(x) for x in ks], 'eps': float(np.linalg.norm(ks)), 'n_D_raster': nD[i].tolist(),
             'D0_min_rel_raster': dmin[i].tolist()}
        if (nD[i] < 0).any():
            z['schema_undefiniert'] = True
        pos = [j for j in range(len(js)) if nD[i, j] > 0]
        if not pos:
            z['h_letzt'] = None
            z['zensiert_letzt'] = 'kein negativer Eigenwert bei h <= 1'
        elif pos[-1] == len(js) - 1:
            z['h_letzt'] = None
            z['zensiert_letzt'] = 'h* < kleinstes Raster-h'
        else:
            lo, hi = hs[pos[-1] + 1], hs[pos[-1]]
            for _ in range(HS_BIS if not probe else 2):
                m = float(np.sqrt(lo * hi))
                if zahl(m, ks) > 0:
                    hi = m
                else:
                    lo = m
            z['h_letzt'] = float(np.sqrt(lo * hi))
            z['klammer_letzt'] = [lo, hi]
        aend = [j for j in range(1, len(js)) if nD[i, j] != nD[i, j - 1]]
        if not aend:
            z['h_erst'] = None
            z['zensiert_erst'] = 'keine Aenderung im Raster'
        else:
            j1 = aend[0]
            lo, hi = hs[j1], hs[j1 - 1]
            ref = int(nD[i, j1 - 1])
            for _ in range(HS_BIS if not probe else 2):
                m = float(np.sqrt(lo * hi))
                if zahl(m, ks) == ref:
                    hi = m
                else:
                    lo = m
            z['h_erst'] = float(np.sqrt(lo * hi))
            z['klammer_erst'] = [lo, hi]
        out.append(z)
    return {'richtung': richtung, 'l_mittel': lm, 'h_raster': hs, 'punkte': out, 't_raster_s': t_raster}


def lauf_rauch1(netz):
    vl, mod, LV, zu, tb = bau(netz)
    lm = float(mod['l'].mean())
    out = {'netz': netz, 't_aufbau_s': tb, 'l_mittel': lm, 'kontrollen': uv.kontrollen(vl, mod, LV, zu),
           'pruefung_3d': {x: mod['pruefung'][x] for x in ('T', 'E', 'nV', 'dieder_summe_minus_2pi_max', 'Vbox',
                                                           'selbstkanten')},
           'NV': vl[0].NV, 'NE': vl[0].NE, 'nq': vl[0].nq, 'n_diag': len(vl[0].diag), 'tot': sorted(vl[0].tot)}
    pts = raster_kl(lm)[::31][:3] + bz_netz(netz, LV)[::200][:3]
    tech = []
    for p in pts:
        t = time.time()
        z = {'art': p['art']}
        z['K4'] = fro(np.conj(zu.U(p['ks']).T) @ uv.M_disp_rk(vl[0], p['ks']) - tg.ops(mod, p['ks'])[2]) / \
            fro(tg.ops(mod, p['ks'])[2])
        k8 = 0.0
        for V in vl:
            S1, d1 = V.bloecke(p['ks'], 'ls')
            S2, d2 = bloecke2(V, p['ks'])
            if S1 is not None and S2 is not None:
                k8 = max(k8, float(np.abs(S1 - S2).max() / np.abs(S1).max()))
            z.setdefault('rang_B_s', []).append(d2['rang_B_s'])
            z.setdefault('n_L', []).append(d2['n_L'])
            z.setdefault('J_rang_ok', []).append(d2['J_rang_ok'])
            z.setdefault('D0_regulaer', []).append(bool(d2.get('D0_min_rel', 0) >= 1e-10))
        z['K8_bloecke2_gleich_uv'] = k8
        z['t_s'] = time.time() - t
        tech.append(z)
    out['technik'] = tech
    t = time.time()
    r = punkt2(vl, mod, zu, pts[0]['ks'], uw2=True)
    out['t_punkt_s'] = time.time() - t
    out['punkt_schluessel'] = sorted(r.keys())
    return out


# ================================================================================================= Auswertung
def mm(xs):
    xs = [x for x in xs if x is not None]
    return [float(min(xs)), float(max(xs))] if xs else None


def vert(xs):
    o = {}
    for x in xs:
        o[str(x)] = o.get(str(x), 0) + 1
    return o


def nneg(p, j=IH):
    return p['traegheit'][j][0] if p.get('definiert') else None


def wachs(p, v):
    r = p['ls']['sp'][v]
    return bool(r.get('definiert') and r.get('n_wachsend', 0) > 0)


def defi(p, v):
    return bool(p['ls']['sp'][v].get('definiert'))


def netz_urteil(pts_sp, pts, thr=1e-8):
    """PLAN 5, UW3/UW4 je Netz: (plan, karte, Kennzahlen)."""
    sa = uv.spanne(pts_sp, 'ls', 'a')
    s12 = uv.spanne(pts_sp, 'ls', 'a12')
    a_fit = bool(sa is not None and sa['alle_ok_fit'] and sa['spanne0'] is not None)
    delta = abs(sa['spanne0'] - s12['spanne0']) if (a_fit and s12 is not None and s12['spanne0'] is not None) else None
    alle_def = all(defi(p, 'a') and defi(p, 'a12') for p in pts)
    wa_a = sum(1 for p in pts if wachs(p, 'a'))
    wa_12 = sum(1 for p in pts if wachs(p, 'a12'))
    beide = sum(1 for p in pts if wachs(p, 'a') and wachs(p, 'a12'))
    konv = sum(1 for p in pts if p.get('konvergent'))
    if a_fit and delta is not None and sa['spanne0'] + delta < thr and alle_def and wa_a == 0 and wa_12 == 0 \
            and konv == len(pts):
        plan = 'eingetroffen'
    elif (a_fit and delta is not None and sa['spanne0'] - delta >= thr) or beide > 0:
        plan = 'nicht eingetroffen'
    else:
        plan = 'nicht entscheidbar'
    a_def = all(defi(p, 'a') for p in pts)
    if a_fit and sa['spanne0'] < thr and a_def and wa_a == 0:
        karte = 'eingetroffen'
    elif (a_fit and sa['spanne0'] >= thr) or wa_a > 0:
        karte = 'nicht eingetroffen'
    else:
        karte = 'nicht entscheidbar'
    kz = {'spanne0_a': sa['spanne0'] if sa else None, 'alle_ok_fit_a': a_fit,
          'spanne0_a12': s12['spanne0'] if s12 else None, 'alle_ok_fit_a12': bool(s12 and s12['alle_ok_fit']),
          'delta': delta, 'k_gesamt': len(pts), 'k_a_nicht_definiert': sum(1 for p in pts if not defi(p, 'a')),
          'k_a12_nicht_definiert': sum(1 for p in pts if not defi(p, 'a12')), 'k_wachsend_a': wa_a,
          'k_wachsend_a12': wa_12, 'k_wachsend_beide': beide, 'k_konvergent': konv,
          'spanne_a_je_kl': sa['je_kl'] if sa else None, 'w0_a': [sa['w0_min'], sa['w0_max']] if sa else None}
    return plan, karte, kz


def kombi(a, b):
    if a == 'eingetroffen' and b == 'eingetroffen':
        return 'eingetroffen'
    if 'nicht eingetroffen' in (a, b):
        return 'nicht eingetroffen'
    return 'nicht entscheidbar'


def gruppe(pts, vars_=VARS):
    o = {}
    for v in vars_:
        o[v] = uv.zaehle(pts, 'ls', v)
    o['konvergent'] = sum(1 for p in pts if p.get('konvergent'))
    o['traegheit_stabil'] = sum(1 for p in pts if p.get('traegheit_stabil'))
    o['n_neg_10'] = vert([nneg(p) for p in pts])
    o['traegheit_10'] = vert([tuple(p['traegheit'][IH]) if p.get('definiert') else None for p in pts])
    o['n_neg_x0'] = vert([p['traegheit_x0'][0] if p.get('definiert') else None for p in pts])
    o['n_u_a'] = vert([p['ls']['sp']['a'].get('n_u') for p in pts])
    o['dim_red_a'] = vert([p['ls']['sp']['a'].get('dim_red') for p in pts])
    o['B_red_nicht_pd_a'] = sum(1 for p in pts if p['ls']['sp']['a'].get('B_red_pd') is False)
    o['pass_rest_a'] = mm([p['ls']['sp']['a'].get('pass_rest') for p in pts])
    o['n'] = len(pts)
    return o


def beschreibend(pts):
    dp = [p for p in pts if p.get('definiert')]
    o = {'n': len(pts), 'definiert': len(dp)}
    for nm in ('M', 'V', 'C', 'X'):
        o['r12_' + nm] = mm([p['r12'][nm] for p in dp])
        o['r8_' + nm] = mm([p['r8'][nm] for p in dp])
    o['p_h_M'] = mm([p['p_h']['M'] for p in dp])
    o['p_h_M_vert'] = vert([None if p['p_h']['M'] is None else round(p['p_h']['M'] * 2) / 2 for p in dp])
    o['D0_pd_alle_h'] = sum(1 for p in dp if p.get('D0_pd_alle_h'))
    o['D0_n_neg_je_h'] = [vert([p['D0'][j]['D0_n_neg'] for p in pts]) for j in range(3)]
    o['D0_eig_min_rel_je_h'] = [mm([p['D0'][j]['D0_eig_min_rel'] for p in pts]) for j in range(3)]
    o['Meff_absmin_rel_10'] = mm([p['Meff_absmin_rel'][IH] for p in dp])
    o['dM12_2norm_rel'] = mm([p['dM12_2norm_rel'] for p in dp])
    for x in ('r_V', 'C_rest_kappa', 'G_rel', 'nn_rel', 'K4_Mdisp', 'K6_herm', 'J_sv_min_rel'):
        o[x] = mm([p.get(x) for p in dp])
    o['kappa_re'] = mm([p['kappa'][0] for p in dp])
    o['kappa_im'] = mm([p['kappa'][1] for p in dp])
    o['rang_B_s'] = vert([tuple(p['rang_B_s']) for p in pts])
    o['nicht_definiert_gruende'] = vert([p.get('grund') for p in pts if not p.get('definiert')])
    o['nicht_konvergent_orte'] = [p.get('m') or p.get('name') or [p.get('richtung'), p.get('kl')]
                                  for p in pts if not p.get('konvergent')][:30]
    return o


def lade(p):
    with open(p) as fh:
        return json.load(fh)


def lauf_auswertung(pfade):
    J = {nm: lade(p) for nm, p in pfade.items()}
    out = {'eingaben': {nm: {'pfad': p, 'sha256': uv.sha(p), 'skript': J[nm]['info']['skript_sha256']}
                        for nm, p in pfade.items()}}
    U = {}
    v0 = J['v0']['ergebnis']['punkte']
    s = J['s']['ergebnis']['punkte']
    b1 = J['b1']['ergebnis']['punkte']
    vneu = J['vneu0']['ergebnis']['punkte'] + J['vneu1']['ergebnis']['punkte'] + J['vneu2']['ergebnis']['punkte']
    # ---------------- UW0
    sa = uv.spanne(v0, 'ls', 'a')
    i_ok = bool(sa is not None and sa['alle_ok_fit'] and sa['spanne0'] is not None)
    i_in = bool(i_ok and 1.7e-10 <= sa['spanne0'] <= 1.53e-9)
    ii_def = all(defi(p, 'a') for p in v0)
    ii_wa = sum(1 for p in v0 if wachs(p, 'a'))
    ii_beide = sum(1 for p in v0 if wachs(p, 'a') and wachs(p, 'a12'))
    iii_alle = all(p.get('definiert') and p['konvergent'] and p['traegheit_stabil'] and nneg(p) == 10 for p in v0)
    iii_verf = sum(1 for p in v0 if p.get('definiert') and p['konvergent'] and p['traegheit_stabil'] and nneg(p) != 10)
    if i_in and ii_def and ii_wa == 0 and iii_alle:
        u0 = 'eingetroffen'
    elif (i_ok and not i_in) or ii_beide > 0 or iii_verf > 0:
        u0 = 'nicht eingetroffen'
    else:
        u0 = 'nicht entscheidbar'
    k_iii = all(p.get('definiert') and nneg(p) == 10 for p in v0)
    k_verf = (i_ok and not i_in) or ii_wa > 0 or any(p.get('definiert') and nneg(p) != 10 for p in v0)
    if i_in and ii_def and ii_wa == 0 and k_iii:
        u0k = 'eingetroffen'
    elif k_verf:
        u0k = 'nicht eingetroffen'
    else:
        u0k = 'nicht entscheidbar'
    U['UW0'] = {'plan': u0, 'karte': u0k, 'spanne0_a': sa['spanne0'] if sa else None, 'alle_ok_fit': i_ok,
                'fenster': [1.7e-10, 1.53e-9], 'k': len(v0), 'k_a_nicht_definiert': sum(1 for p in v0 if not defi(p, 'a')),
                'k_wachsend_a': ii_wa, 'k_wachsend_beide': ii_beide, 'n_neg_10': vert([nneg(p) for p in v0]),
                'k_konvergent': sum(1 for p in v0 if p.get('konvergent')),
                'k_traegheit_stabil': sum(1 for p in v0 if p.get('traegheit_stabil')), 'k_n_neg_ungleich_10_sicher': iii_verf,
                'spanne_a_je_kl': sa['je_kl'] if sa else None, 'w0': [sa['w0_min'], sa['w0_max']] if sa else None}
    # ---------------- UW1
    z1 = {}
    pl, ka = [], []
    for nm, pts in (('S', s), ('B1', b1)):
        n = NECK[nm]
        ok = all(p.get('definiert') and p['konvergent'] and p['traegheit_stabil'] and nneg(p) == n for p in pts)
        verf = sum(1 for p in pts if p.get('definiert') and p['konvergent'] and p['traegheit_stabil'] and nneg(p) != n)
        kok = all(p.get('definiert') and nneg(p) == n for p in pts)
        kverf = sum(1 for p in pts if p.get('definiert') and nneg(p) != n)
        pl.append('eingetroffen' if ok else ('nicht eingetroffen' if verf else 'nicht entscheidbar'))
        ka.append('eingetroffen' if kok else ('nicht eingetroffen' if kverf else 'nicht entscheidbar'))
        z1[nm] = {'ecken_je_zelle': n, 'k': len(pts), 'plan': pl[-1], 'karte': ka[-1], 'n_neg_10': vert([nneg(p) for p in pts]),
                  'n_neg_8': vert([nneg(p, 0) for p in pts]), 'n_neg_12': vert([nneg(p, 2) for p in pts]),
                  'k_konvergent': sum(1 for p in pts if p.get('konvergent')),
                  'k_traegheit_stabil': sum(1 for p in pts if p.get('traegheit_stabil')),
                  'k_nicht_definiert': sum(1 for p in pts if not p.get('definiert')),
                  'k_ungleich_sicher': verf, 'k_ungleich_woertlich': kverf,
                  'n_null_10': vert([p['traegheit'][IH][1] if p.get('definiert') else None for p in pts]),
                  'raster_n_neg_10': vert([nneg(p) for p in pts if p.get('art') == 'kl']),
                  'bz_n_neg_10': vert([nneg(p) for p in pts if p.get('art') != 'kl'])}
    U['UW1'] = {'plan': kombi(*pl), 'karte': kombi(*ka), 'je_netz': z1}
    # ---------------- UW2
    p65 = [p for p in v0 if p.get('art') == 'kl' and p['kl'] <= 0.1 + 1e-12]
    P10 = [p['uw2']['P10'] if p.get('definiert') and 'uw2' in p else None for p in p65]
    P12 = [p['uw2']['P12'] if p.get('definiert') and 'uw2' in p else None for p in p65]
    ok2 = all(p.get('definiert') and p['konvergent'] and a is not None and b is not None and a >= UW2_MIN and b >= UW2_MIN
              for p, a, b in zip(p65, P10, P12))
    verf2 = sum(1 for p, a, b in zip(p65, P10, P12) if p.get('definiert') and p['konvergent'] and a is not None
                and b is not None and a < UW2_MIN and b < UW2_MIN)
    u2 = 'eingetroffen' if ok2 else ('nicht eingetroffen' if verf2 else 'nicht entscheidbar')
    if any(x is None for x in P10):
        u2k, LA, LB = 'nicht entscheidbar', None, None
    else:
        LA = all(x >= UW2_MIN for x in P10)
        LB = bool(float(np.mean(P10)) >= UW2_MIN)
        u2k = ('eingetroffen' if LA else 'nicht eingetroffen') if LA == LB else 'unklar'
    U['UW2'] = {'plan': u2, 'karte': u2k, 'lesart_A_jedes_k': LA, 'lesart_B_mittel': LB, 'k': len(p65),
                'P10': mm(P10), 'P10_mittel': float(np.mean([x for x in P10 if x is not None])) if any(x is not None for x in P10) else None,
                'P12': mm(P12), 'P8': mm([p['uw2']['P8'] for p in p65 if p.get('definiert') and 'uw2' in p]),
                'Px0': mm([p['uw2']['Px0'] for p in p65 if p.get('definiert') and 'uw2' in p]),
                'cos2_min10': mm([p['uw2']['cos2_min10'] for p in p65 if p.get('definiert') and 'uw2' in p]),
                'rang_Wh': vert([p['uw2']['rang_Wh'] for p in p65 if 'uw2' in p]),
                'k_P10_unter_0_9': sum(1 for x in P10 if x is not None and x < UW2_MIN),
                'k_konvergent': sum(1 for p in p65 if p.get('konvergent')), 'k_verfehlt_sicher': verf2,
                'P10_je_kl': {('%g' % kl): mm([x for p, x in zip(p65, P10) if abs(p['kl'] - kl) < 1e-12])
                              for kl in uv.KL_FIT}}
    U['UW2']['beschreibend_S_B1'] = {}
    for nm, pts in (('S', s), ('B1', b1)):
        q = [p for p in pts if p.get('art') == 'kl' and p['kl'] <= 0.1 + 1e-12 and p.get('definiert') and 'uw2' in p]
        U['UW2']['beschreibend_S_B1'][nm] = {'k': len(q), 'P10': mm([p['uw2']['P10'] for p in q]),
                                             'P12': mm([p['uw2']['P12'] for p in q]),
                                             'cos2_min10': mm([p['uw2']['cos2_min10'] for p in q])}
    # ---------------- UW3
    r3 = {}
    pl, ka = [], []
    for nm, pts in (('S', s), ('B1', b1)):
        a, b, kz = netz_urteil([p for p in pts if p.get('art') == 'kl'], pts)
        pl.append(a); ka.append(b)
        kz.update({'plan': a, 'karte': b})
        r3[nm] = kz
    U['UW3'] = {'plan': kombi(*pl), 'karte': kombi(*ka), 'je_netz': r3}
    # ---------------- UW4
    a, b, kz = netz_urteil([p for p in vneu if p.get('menge') == 'R'], vneu)
    kz['mindestens_1000'] = len(vneu) >= 1000
    if len(vneu) < 1000:
        a = b = 'nicht entscheidbar'
    U['UW4'] = {'plan': a, 'karte': b, **kz}
    out['urteile'] = U
    # ---------------- beschreibend
    out['gruppen'] = {'V_raster': gruppe(v0), 'S_raster': gruppe([p for p in s if p.get('art') == 'kl']),
                      'S_bz_innen': gruppe([p for p in s if p.get('art') != 'kl' and not p.get('rand')]),
                      'S_bz_rand': gruppe([p for p in s if p.get('art') != 'kl' and p.get('rand')]),
                      'B1_raster': gruppe([p for p in b1 if p.get('art') == 'kl']),
                      'B1_bz_innen': gruppe([p for p in b1 if p.get('art') != 'kl' and not p.get('rand')]),
                      'B1_bz_rand': gruppe([p for p in b1 if p.get('art') != 'kl' and p.get('rand')])}
    for mg in ('R', 'W', 'G16R', 'G16I'):
        out['gruppen']['Vneu_' + mg] = gruppe([p for p in vneu if p.get('menge') == mg])
    out['beschreibend'] = {'V_raster': beschreibend(v0), 'S': beschreibend(s), 'B1': beschreibend(b1),
                           'Vneu': beschreibend(vneu)}
    out['spannen_varianten'] = {}
    for nm, pts in (('V_raster', v0), ('S_raster', [p for p in s if p.get('art') == 'kl']),
                    ('B1_raster', [p for p in b1 if p.get('art') == 'kl']), ('Vneu_R', [p for p in vneu if p.get('menge') == 'R'])):
        out['spannen_varianten'][nm] = {v: uv.spanne(pts, 'ls', v) for v in VARS}
    # ---------------- Messziel
    ms = {}
    for r in ('100', '111', '321'):
        key = 'hs' + r
        if key not in J:
            continue
        P = J[key]['ergebnis']['punkte']
        z = {'punkte': [{x: p.get(x) for x in ('kl', 'eps', 'h_letzt', 'klammer_letzt', 'zensiert_letzt', 'h_erst',
                                                'klammer_erst', 'zensiert_erst', 'schema_undefiniert')} for p in P]}
        for nmf, cond in (('exp_kl_le_0_1', lambda p: p['kl'] <= 0.1 + 1e-12), ('exp_alle', lambda p: True)):
            q = [p for p in P if cond(p) and p.get('h_letzt')]
            if len(q) >= 2:
                x = np.log([p['kl'] for p in q]); y = np.log([p['h_letzt'] for p in q])
                A = np.stack([np.ones_like(x), x], 1)
                cf, *_ = np.linalg.lstsq(A, y, rcond=None)
                z[nmf] = {'exponent': float(cf[1]), 'vorfaktor': float(np.exp(cf[0])), 'n': len(q),
                          'rest_max_log': float(np.abs(A @ cf - y).max())}
            else:
                z[nmf] = None
        z['n_D_bei_h1'] = [p['n_D_raster'][0] for p in P]
        ms[r] = z
    out['messziel'] = ms
    out['kontrollen'] = {nm: J[nm]['ergebnis'].get('kontrollen') for nm in ('v0', 's', 'b1', 'vneu0')}
    out['struktur'] = {nm: J[nm]['ergebnis'].get('struktur') for nm in ('v0', 's', 'b1')}
    out['pruefung_3d'] = {nm: J[nm]['ergebnis'].get('pruefung_3d') for nm in ('v0', 's', 'b1')}
    out['neu_info'] = J['vneu0']['ergebnis'].get('neu_info')
    return out


# ================================================================================================= main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch1', 'punkte', 'hstern', 'auswertung'])
    ap.add_argument('--netz', default='V', choices=['V', 'S', 'B1'])
    ap.add_argument('--menge', default='raster', choices=['raster', 'rasterbz', 'neu'])
    ap.add_argument('--teil', type=int, default=0)
    ap.add_argument('--richtung', default='100', choices=['100', '111', '321'])
    ap.add_argument('--probe', action='store_true', help='Codeprobe mit wenigen k (Werte nicht ansehen)')
    ap.add_argument('--ein', nargs='*', default=[])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'skript_sha256': uv.sha(os.path.abspath(__file__)),
            'module_sha256': {nm: uv.sha(os.path.abspath(sys.modules[nm].__file__))
                              for nm in ('uv', 'rk', 'pt', 'rk2', 'ew', 'tp', 'tg', 'hm', 'tti', 'dn', 'nachtrag_kinetik')
                              if nm in sys.modules}}
    if a.modus == 'auswertung':
        erg = lauf_auswertung(dict(x.split('=', 1) for x in a.ein))
    elif a.modus == 'rauch1':
        erg = lauf_rauch1(a.netz)
    elif a.modus == 'hstern':
        erg = lauf_hstern(a.richtung, a.probe)
    else:
        erg = lauf_punkte(a.netz, a.menge, a.teil, a.probe)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, a.netz, a.menge, a.teil, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
