#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HOEHE-ISOTROP-1 (Runde 49, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage: Kann die Hebehoehe (Gewichte w der Potenz-Zerlegung von Finns Netz V) das kubische Kurzwellen-Muster des Lichts
auf V aufheben?
  - Licht = Maxwell auf V (DEC): K(k) = d1(k)^H *2 d1(k), Masse *1. Gewichtete Sterne aus rv.sterne (Potenzdiagramm,
    unveraendert), *2_f = delta_f / A_f. Photonen = die zwei kleinsten Eigenwerte nach den n_V Eichnullen.
  - Messung wie DANZER-NAEHERUNG-2 / REGULAER-V-1: dn.operator_messen, 40 Richtungen, Fenster [0,03; 0,12] pi/a,
    Zerlegung von a2(n); Zweige maxwell_lo, maxwell_hi, maxwell_mittel.
  - beta-Nullpunkt des Skalars im F-43m-Schnitt (w_P, w_C1, w_C2, w_H): Strahlen + brentq, SLSQP (groesste Marge).
  - LHAASO-Umrechnung woertlich wie LICHT-FINN-NETZ-1: ln.operator_auswerten (26 Richtungen, Fenster W0/Wk/Wg) und
    ln.schranken, Laengeneinheit Tetraederkante l_P = a / (2 sqrt2).
Unveraendert importiert: rv.py (REGULAER-V-1), ew.py, tp.py, danzer_naeherung.py, licht_netz.py.
Einheiten: V-Lagen in a/8, Gewichte und Margen in (a/8)^2, Operator und a2 in a (L_ref = 1 = kubische Kante).

Aufruf (nur ueber kleintest.sh auf der .69):
  python hi.py rauch <aus.json>
  python hi.py mitte <aus.json> <kammer1_alt.json> <nachtrag_alt.json>
  python hi.py proben <aus.json> <kammer1_alt.json> [--rauch]
  python hi.py strahlen <teil 0|1> <aus.json> [--rauch]
  python hi.py null <aus.json> [--rauch]
  python hi.py gitter <aus.json> [--rauch]
  python hi.py l2 <aus.json> [anzahl]
  python hi.py auswerten <aus.json> <mitte> <proben> <f43-0> <f43-1> <null> <gitter> [<l2>]
"""
import hashlib
import json
import math
import os
import platform
import sys
import time

import numpy as np
import scipy
import scipy.linalg as sla
import scipy.sparse as sps
from scipy.optimize import brentq, minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv  # noqa: E402  REGULAER-V-1 (unveraendert)
import danzer_naeherung as dn  # noqa: E402  DANZER-NAEHERUNG-2 (unveraendert)
import licht_netz as ln  # noqa: E402  LICHT-FINN-NETZ-1 (unveraendert)

T0 = time.time()
AL = 2.0 * math.sqrt(2.0)          # a / l_P, l_P = Pyrochlorkante = Kante der Finn-Tetraeder
TOL_BETA0 = 1e-9                   # a^2: |beta| darunter gilt als Nullpunkt
TOL_MARGE = 1e-9                   # (a/8)^2
S_STRAHL = (0.25, 0.5, 0.75, 0.9, 0.99)
N_STRAHL = 128
NULL_REL_MAX = 1e-8
LUECKE_MIN = 1.5
FIT_MAX = 1e-6
H_GRAD = 1e-3
EPS_MIN = 0.01
ZEIT_STUFE2 = 400.0                # s: danach keine neuen SLSQP-Starts
ZEIT_NULLMESS = 540.0              # s: danach keine weiteren Licht-Messungen an Nullpunkten (w0* immer)
ZWEIGE = ('maxwell_lo', 'maxwell_hi', 'maxwell_mittel')
CODE = ('hi.py', 'rv.py', 'ew.py', 'tp.py', 'danzer_naeherung.py', 'licht_netz.py')
RAUCH = '--rauch' in sys.argv


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def schreiben(path, obj):
    obj = dict(obj)
    d = os.path.dirname(os.path.abspath(__file__))
    obj['_meta'] = {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'scipy': scipy.__version__, 'host': platform.node(), 'laufzeit_s': time.time() - T0,
                    'rauch': RAUCH, 'sha256': {f: sha(os.path.join(d, f)) for f in CODE}}
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(ln.js(obj), f, indent=1)
    os.replace(tmp, path)
    log('->', path)


# ------------------------------------------------------------------------------------------------ Maxwell auf V
def maxwell_bau(net, topo):
    """d0 (Kanten x Ecken) und d1 (Flaechen x Kanten) mit Lagen relativ (wirkliche Lagen, Einheit a)."""
    s = net['skala']
    home, per = net['home'], net['periodisch']
    ke = list(topo['kanten'].keys())
    ie = {k: m for m, k in enumerate(ke)}
    kf = list(topo['flaechen'].keys())
    nV, E, F = net['n'], len(ke), len(kf)
    xe = np.zeros((E, 3))
    r0, c0, v0, q0 = [], [], [], []
    for m, key in enumerate(ke):
        (ga, pa), (gb, pb) = key
        pa, pb = np.array(pa, float), np.array(pb, float)
        xm = 0.5 * (pa + pb)
        xe[m] = xm
        r0 += [m, m]
        c0 += [int(ga), int(gb)]
        v0 += [-1.0, 1.0]
        q0 += [(pa - xm) * s, (pb - xm) * s]
    r1, c1, v1, q1 = [], [], [], []
    A_f = np.zeros(F)
    n_f = np.zeros((F, 3))
    for f, key in enumerate(kf):
        g = [int(k[0]) for k in key]
        P = [np.array(k[1], float) for k in key]
        xf = (P[0] + P[1] + P[2]) / 3.0
        for (u, v) in ((0, 1), (1, 2), (2, 0)):
            ek, T = rv.kanon([(g[u], P[u]), (g[v], P[v])], home, per)
            m = ie[ek]
            (ga, pa), (gb, pb) = ek
            pa = np.array(pa, float) + T
            pb = np.array(pb, float) + T
            if ga == g[u] and gb == g[v] and np.allclose(pa, P[u]) and np.allclose(pb, P[v]):
                sg = 1.0
            elif ga == g[v] and gb == g[u] and np.allclose(pa, P[v]) and np.allclose(pb, P[u]):
                sg = -1.0
            else:
                raise ValueError('Kante passt nicht zur Flaeche %s' % (key,))
            r1.append(f)
            c1.append(m)
            v1.append(sg)
            q1.append((xe[m] + T - xf) * s)
        nv = np.cross(P[1] - P[0], P[2] - P[0]) * s * s
        A_f[f] = 0.5 * np.linalg.norm(nv)
        n_f[f] = nv / np.linalg.norm(nv)
    return {'nV': nV, 'E': E, 'F': F, 'ke': ke, 'kf': kf, 'A_f': A_f, 'n_f': n_f,
            'd0': (np.array(r0), np.array(c0), np.array(v0), np.array(q0)),
            'd1': (np.array(r1), np.array(c1), np.array(v1), np.array(q1)),
            'vol': net['vol'] * s ** 3}


def bloch(st, k, form):
    r, c, v, q = st
    return sps.csr_matrix((v * np.exp(1j * (q @ np.asarray(k, float))), (r, c)), shape=form)


def sterne_licht(net, topo, mb, w):
    st = rv.sterne(net, topo, w)
    delta = np.array([st['delta'][k] for k in mb['kf']])
    st['S2'] = delta / mb['A_f']
    T2 = np.einsum('f,fi,fj->ij', delta * mb['A_f'], mb['n_f'], mb['n_f']) / mb['vol']
    st['id_T2'] = float(np.abs(T2 - np.eye(3)).max())
    return st


def licht_op(mb, S1, S2, diag):
    nV, E, F = mb['nV'], mb['E'], mb['F']
    m12 = 1.0 / np.sqrt(S1)
    D2 = sps.diags(S2)

    def op(kv):
        D1 = bloch(mb['d1'], kv, (F, E))
        K = (D1.conj().T @ (D2 @ D1)).toarray()
        K = K * m12[:, None] * m12[None, :]
        lam = sla.eigh(K, eigvals_only=True, subset_by_index=[0, nV + 2], driver='evr')
        lo, hi, opt = float(lam[nV]), float(lam[nV + 1]), float(lam[nV + 2])
        diag['n'] += 1
        if lo > 0:
            diag['null_rel'] = max(diag['null_rel'], float(np.max(np.abs(lam[:nV]))) / lo)
            diag['luecke'] = min(diag['luecke'], opt / hi)
        else:
            diag['null_rel'] = float('inf')
        lo, hi = max(lo, 0.0), max(hi, 0.0)
        return [math.sqrt(lo), math.sqrt(hi), math.sqrt(0.5 * (lo + hi))]
    return op


def neue_diag():
    return {'null_rel': 0.0, 'luecke': float('inf'), 'n': 0}


def sterne_positiv(st):
    return not (np.any(st['s0'] <= 0) or np.any(st['s1'] <= 0) or np.any(st['S2'] <= 0))


def licht_messen(ctx, w, fen=None, st=None):
    if st is None:
        st = sterne_licht(ctx['net'], ctx['topo'], ctx['mb'], w)
    if not sterne_positiv(st):
        return st, None, None, None
    diag = neue_diag()
    op = licht_op(ctx['mb'], st['s1'], st['S2'], diag)
    out = dn.operator_messen('M', lambda n: op, 3, ctx['nd'], dn.FENSTER_HAUPT if fen is None else fen, 1.0,
                             ctx['ref'])
    return st, out, diag, op


def kurz_licht(out, je_richtung=False):
    r = {}
    for zw in ZWEIGE:
        o = out[zw]
        z = o['a2_zerlegung']
        r[zw] = {'a2_mittel': z['mittel'], 'beta': z['beta_S4'], 'rms_l4': z['rms_l4'], 'rms_l2': z['rms_l2'],
                 'nichtkub4_rms': z['nichtkub4_rms'], 'rms_l6': z['rms_l6'], 'rest_rms': z['rest_rms'],
                 'c_mittel': o['c_mittel'], 'c_spanne_rel': o['c_spanne_rel'], 'fit_rms_rel_max': o['fit_rms_rel_max'],
                 'a1_voll_max_abs': o['a1_voll_max_abs'], 'a2_min': o['a2_min'], 'a2_max': o['a2_max'],
                 'a4_mittel': o['a4_zerlegung']['mittel'], 'a4_beta': o['a4_zerlegung']['beta_S4']}
        if je_richtung:
            r[zw]['je_richtung'] = o['je_richtung']
    lo = np.array([e['a2'] for e in out['maxwell_lo']['je_richtung']])
    hi = np.array([e['a2'] for e in out['maxwell_hi']['je_richtung']])
    r['doppelbrechung_a2_max'] = float(np.max(np.abs(hi - lo)))
    return r


def lhaaso(op_a):
    """LICHT-FINN-NETZ-1 woertlich: 26 Richtungen, Fenster W0/Wk/Wg, Einheit Tetraederkante l_P."""
    def op_lP(k):
        return [x / AL for x in op_a(AL * np.asarray(k, float))]
    erg = ln.operator_auswerten('M-V', op_lP, 3, ln.richtungen26())
    return {'fenster': erg['fenster'], 'schranken': ln.schranken(erg), 'laufzeit_s': erg['laufzeit_s']}


# ------------------------------------------------------------------------------------------------ Kontext, Proben
def kontext(L=1):
    net1 = rv.netz_V(1)
    topo1 = rv.topologie(net1)
    rows1, A1, G01 = rv.zeilen(net1, topo1)
    sy = rv.lp_symmetrisch(A1, G01, rv.bahnmatrix(net1))
    if L == 1:
        net, topo, rows, A, G0 = net1, topo1, rows1, A1, G01
    else:
        net = rv.netz_V(L)
        topo = rv.topologie(net)
        rows, A, G0 = rv.zeilen(net, topo)
    mb = maxwell_bau(net, topo)
    ctx = {'net': net, 'topo': topo, 'rows': rows, 'A': A, 'G0': G0, 'mb': mb, 'ref': dn.referenzen(),
           'nd': dn.halbkugel(40), 'xm': sy['x'], 'ym': sy['y'], 'w_mid': rv.w_sym(net, sy['x'], sy['y']), 'L': L}
    if L == 1:
        B4 = np.zeros((net['n'], 4))
        for g in range(net['n']):          # L = 1: globale Nummer = Untergitter (wie nachtrag_beta.py)
            B4[g, 0 if g < 4 else (1 if g == 4 else (2 if g == 5 else 3))] = 1.0
        ctx['B4'] = B4
        ctx['AZ'] = A @ B4[:, 1:]
        ctx['z_mid'] = np.array([sy['x'], sy['x'], sy['y']])
    return ctx


def wz(ctx, z):
    w = ctx['B4'] @ np.r_[0.0, np.asarray(z, float)]
    return w - w.mean()


def gueltig(rec):
    if rec['licht'] is None or rec['diagnose'] is None:
        return False
    return bool(rec['marge'] > 0 and rec['sterne']['n_nichtpos'] == 0
                and rec['diagnose']['null_rel'] <= NULL_REL_MAX and rec['diagnose']['luecke'] >= LUECKE_MIN
                and rec['licht']['maxwell_mittel']['fit_rms_rel_max'] <= FIT_MAX)


def probe(ctx, w, info, je_richtung=False, fen_probe=False, mit_lhaaso=False):
    net, topo = ctx['net'], ctx['topo']
    rec = dict(info)
    rec['marge'] = float((ctx['G0'] + ctx['A'] @ w).min())
    st = sterne_licht(net, topo, ctx['mb'], w)
    kk = rv.stern_kontrolle(net, topo, ctx['rows'], ctx['A'], ctx['G0'], w, st)
    rec['sterne'] = {'min_s0': float(st['s0'].min()), 'min_s1': float(st['s1'].min()), 'min_s2': float(st['S2'].min()),
                     'n_nichtpos': int(np.sum(st['s0'] <= 0) + np.sum(st['s1'] <= 0) + np.sum(st['S2'] <= 0)),
                     'id_vol': st['id_vol'], 'id_T1': st['id_T1'], 'id_T2': st['id_T2'],
                     'vorzeichen_g_gleich': kk['vorzeichen_gleich'], 'g_gegen_delta_H_max': kk['g_gegen_delta_H_max']}
    _, sk = rv.messen(net, topo, w, ctx['ref'], ctx['nd'])
    rec['skalar'] = rv.kurz(sk) if sk is not None else None
    _, out, diag, op = licht_messen(ctx, w, st=st)
    rec['licht'] = kurz_licht(out, je_richtung) if out is not None else None
    rec['diagnose'] = diag
    rec['gueltig'] = gueltig(rec)
    if out is not None and fen_probe:
        _, outp, diagp, _ = licht_messen(ctx, w, fen=dn.FENSTER_PROBE, st=st)
        rec['licht_probefenster'] = kurz_licht(outp)
        rec['diagnose_probefenster'] = diagp
    if out is not None and mit_lhaaso:
        rec['lhaaso'] = lhaaso(op)
        a2k = 8.0 * rec['licht']['maxwell_mittel']['a2_mittel']
        rec['lhaaso']['kugelmittel'] = {'a2_lP': a2k, 'l_m': ln.l_aus_a2(a2k)}
    return rec


# ------------------------------------------------------------------------------------------------ Kontrollen
def kontrollen_k(ctx, w_liste):
    net, topo, mb = ctx['net'], ctx['topo'], ctx['mb']
    rng = np.random.default_rng([4096, 76])
    out = {'bau': topo['pruefung'], 'E': mb['E'], 'F': mb['F'], 'nV': mb['nV']}
    dd = []
    for _ in range(3):
        k = rng.normal(size=3) * 2.0
        D0 = bloch(mb['d0'], k, (mb['E'], mb['nV']))
        D1 = bloch(mb['d1'], k, (mb['F'], mb['E']))
        P = (D1 @ D0).toarray()
        dd.append(float(np.abs(P).max()))
    out['k1_d1d0_max'] = max(dd)
    st = sterne_licht(net, topo, mb, ctx['w_mid'])

    def alle_eig(k):
        D1 = bloch(mb['d1'], k, (mb['F'], mb['E']))
        K = (D1.conj().T @ (sps.diags(st['S2']) @ D1)).toarray()
        m12 = 1.0 / np.sqrt(st['s1'])
        return np.linalg.eigvalsh(K * m12[:, None] * m12[None, :])
    lam0 = alle_eig(np.zeros(3))
    out['k1_nullen_k0'] = int(np.sum(np.abs(lam0) <= 1e-11 * lam0.max()))
    nz = []
    for _ in range(3):
        k = rng.normal(size=3)
        k = 0.05 * k / np.linalg.norm(k)
        lam = alle_eig(k)
        nz.append(int(np.sum(np.abs(lam) <= 1e-11 * lam.max())))
    out['k1_nullen_k_klein'] = nz
    out['k1_nullen_soll'] = {'k0': mb['nV'] + 2, 'k_klein': mb['nV']}
    out['k1_ok'] = bool(out['k1_d1d0_max'] <= 1e-12 and out['k1_nullen_k0'] == mb['nV'] + 2
                        and all(v == mb['nV'] for v in nz))
    fab = rv.fabrik_skalar(net, st)
    ab = []
    for _ in range(3):
        k = rng.normal(size=3) * 0.7
        ref_ = float(fab(None)(k)[0])
        D0 = bloch(mb['d0'], k, (mb['E'], mb['nV']))
        KS = (D0.conj().T @ (sps.diags(st['s1']) @ D0)).toarray()
        m = 1.0 / np.sqrt(st['s0'])
        mein = math.sqrt(max(float(np.linalg.eigvalsh(KS * m[:, None] * m[None, :])[0]), 0.0))
        ab.append(abs(mein - ref_) / ref_)
    out['k3_skalar_rel_max'] = max(ab)
    out['k3_ok'] = bool(max(ab) <= 1e-12)
    out['k2'] = []
    for nm, w in w_liste:
        s2 = sterne_licht(net, topo, mb, w)
        kk = rv.stern_kontrolle(net, topo, ctx['rows'], ctx['A'], ctx['G0'], w, s2)
        out['k2'].append({'name': nm, 'id_vol': s2['id_vol'], 'id_T1': s2['id_T1'], 'id_T2': s2['id_T2'],
                          'vorzeichen_g_gleich': kk['vorzeichen_gleich'], 'g_gegen_delta_H_max': kk['g_gegen_delta_H_max'],
                          'n_nichtpos': int(np.sum(s2['s0'] <= 0) + np.sum(s2['s1'] <= 0) + np.sum(s2['S2'] <= 0))})
    out['k2_ok'] = bool(all(e['id_vol'] <= 1e-12 and e['id_T1'] <= 1e-12 and e['id_T2'] <= 1e-12 for e in out['k2']))
    return out


def zufall_w(ctx):
    rk = np.random.default_rng([4096, 77])
    return [('zufall%d' % j, ctx['w_mid'] + 0.5 * rk.standard_normal(ctx['net']['n'])) for j in range(3)]


# ------------------------------------------------------------------------------------------------ Modi
def modus_rauch(aus):
    ctx = kontext(1)
    k = kontrollen_k(ctx, [('mitte', ctx['w_mid'])] + zufall_w(ctx))
    log('Bau L=1:', k['bau']['ecken'], k['bau']['kanten'], k['bau']['flaechen'], k['bau']['tetraeder'],
        'euler', k['bau']['euler'], '| E F nV', k['E'], k['F'], k['nV'])
    log('K1 d1d0 %.1e, Nullen k=0 %d (soll %d), klein %s (soll %d), ok %s' % (
        k['k1_d1d0_max'], k['k1_nullen_k0'], k['k1_nullen_soll']['k0'], k['k1_nullen_k_klein'],
        k['k1_nullen_soll']['k_klein'], k['k1_ok']))
    log('K3 Skalar rel %.1e ok %s' % (k['k3_skalar_rel_max'], k['k3_ok']))
    for e in k['k2']:
        log('K2 %s: I1 %.1e I2 %.1e I3 %.1e Vorzeichen %s nichtpos %d' % (
            e['name'], e['id_vol'], e['id_T1'], e['id_T2'], e['vorzeichen_g_gleich'], e['n_nichtpos']))
    zeiten = {}
    t = time.time()
    st, out, diag, op = licht_messen(ctx, ctx['w_mid'])
    zeiten['licht_messung_L1_s'] = time.time() - t
    log('Licht-Messung L=1: %.2f s, Aufrufe %d, Diagnose null_rel %.1e luecke %.2f' % (
        zeiten['licht_messung_L1_s'], diag['n'], diag['null_rel'], diag['luecke']))
    t = time.time()
    rv.messen(ctx['net'], ctx['topo'], ctx['w_mid'], ctx['ref'], ctx['nd'])
    zeiten['skalar_messung_L1_s'] = time.time() - t
    log('Skalar-Messung L=1: %.2f s' % zeiten['skalar_messung_L1_s'])
    t = time.time()
    for j in range(50):
        op(np.array([0.3, 0.2, 0.1]) * (1 + 0.01 * j))
    zeiten['licht_op_L1_s'] = (time.time() - t) / 50
    log('Licht op L=1: %.2e s je k; LHAASO (5200 k) ~ %.1f s' % (zeiten['licht_op_L1_s'], 5200 * zeiten['licht_op_L1_s']))
    t = time.time()
    c2 = kontext(2)
    zeiten['kontext_L2_s'] = time.time() - t
    t = time.time()
    st2 = sterne_licht(c2['net'], c2['topo'], c2['mb'], c2['w_mid'])
    zeiten['sterne_L2_s'] = time.time() - t
    d2 = neue_diag()
    op2 = licht_op(c2['mb'], st2['s1'], st2['S2'], d2)
    t = time.time()
    for j in range(5):
        op2(np.array([0.3, 0.2, 0.1]) * (1 + 0.01 * j))
    zeiten['licht_op_L2_s'] = (time.time() - t) / 5
    log('L=2: Kontext %.1f s, Sterne %.2f s, op %.3f s je k -> Messung ~ %.0f s; Diagnose null_rel %.1e luecke %.2f, '
        'I3 %.1e, E F nV %d %d %d' % (zeiten['kontext_L2_s'], zeiten['sterne_L2_s'], zeiten['licht_op_L2_s'],
                                       320 * zeiten['licht_op_L2_s'], d2['null_rel'], d2['luecke'], st2['id_T2'],
                                       c2['mb']['E'], c2['mb']['F'], c2['mb']['nV']))
    schreiben(aus, {'kontrollen': k, 'zeiten': zeiten, 'diagnose_mitte': diag})


def modus_mitte(aus, alt_k_pfad, alt_n_pfad):
    ctx = kontext(1)
    net, topo = ctx['net'], ctx['topo']
    alt_k = json.load(open(alt_k_pfad))
    alt_n = json.load(open(alt_n_pfad))
    rep = []
    om = alt_n['N2']['ort_min']
    w3 = ctx['B4'] @ np.array(om['w_P_C1_C2_H'], float)
    w3 = w3 - w3.mean()
    for nm, w, alt in (('kammermitte', ctx['w_mid'], alt_k['mitte']['beta']),
                       ('w0', np.zeros(net['n']), alt_k['w0']['beta']),
                       ('f43_ort_min', w3, om['beta'])):
        _, sk = rv.messen(net, topo, w, ctx['ref'], ctx['nd'])
        b = rv.kurz(sk)['beta']
        rep.append({'name': nm, 'beta_neu': b, 'beta_alt': alt, 'abw_abs': abs(b - alt), 'abw_rel': abs(b - alt) / abs(alt)})
    log('Reproduktion fertig')
    k = kontrollen_k(ctx, [('mitte', ctx['w_mid'])] + zufall_w(ctx))
    log('Kontrollen fertig')
    pm = probe(ctx, ctx['w_mid'], {'gruppe': 'M'}, je_richtung=True, fen_probe=True, mit_lhaaso=True)
    log('Mitte fertig')
    schreiben(aus, {'reproduktion': rep, 'kontrollen': k, 'probe_mitte': pm, 'x_mid': ctx['xm'], 'y_mid': ctx['ym'],
                    'w_mid': ctx['w_mid']})


def modus_proben(aus, alt_pfad):
    ctx = kontext(1)
    net, A, G0, w_mid, xm, ym = ctx['net'], ctx['A'], ctx['G0'], ctx['w_mid'], ctx['xm'], ctx['ym']
    proben = []
    E = rv.HAND['ecken_schnitt']
    ziele = [('ecke', e) for e in E] + [('kantenmitte', ((E[a][0] + E[b][0]) / 2, (E[a][1] + E[b][1]) / 2))
                                         for a, b in ((0, 1), (1, 2), (2, 0))]
    n1 = 0
    for nm, (xz, yz) in ziele:
        for s in rv.S_WERTE:
            if RAUCH and n1 >= 2:
                break
            proben.append(probe(ctx, rv.w_sym(net, xm + s * (xz - xm), ym + s * (yz - ym)),
                                {'gruppe': 'S1', 'ziel': nm, 'xy': (xz, yz), 's': s}))
            n1 += 1
    log('S1 fertig')
    rng = np.random.default_rng([4096, 1, 7])
    for j in range(1 if RAUCH else 40):
        d = rng.standard_normal(net['n'])
        d -= d.mean()
        d /= np.linalg.norm(d)
        sw = rv.strahl_wand(A, G0, w_mid, d)
        for s in rv.S_WERTE:
            proben.append(probe(ctx, w_mid + s * sw * d, {'gruppe': 'S2', 'richtung': j, 's': s, 's_wand': sw}))
    log('S2 fertig')
    n3 = 0
    for i in range(net['n']):
        for sinn in (1.0, -1.0):
            if RAUCH and n3 >= 1:
                break
            c = np.zeros(net['n'])
            c[i] = sinn
            we = rv.lp_extrem(A, G0, c)
            if we is None:
                continue
            proben.append(probe(ctx, w_mid + 0.99 * (we - w_mid), {'gruppe': 'S3', 'ecke_index': i,
                                                                    'sinn': 'min' if sinn > 0 else 'max', 's': 0.99}))
            n3 += 1
    log('S3 fertig')
    alt = json.load(open(alt_pfad))['proben']
    vergl = None
    if not RAUCH:
        abw = []
        for p, q in zip(proben, alt):
            same = (p['gruppe'] == q['gruppe'] and abs(p['s'] - q['s']) < 1e-12)
            if p['skalar'] is not None and same:
                abw.append(abs(p['skalar']['beta'] - q['beta']) / abs(q['beta']))
            else:
                abw.append(None)
        gut = [a for a in abw if a is not None]
        vergl = {'n_alt': len(alt), 'n_neu': len(proben), 'n_verglichen': len(gut),
                 'beta_rel_max': max(gut) if gut else None}
    schreiben(aus, {'proben': proben, 'vergleich_regulaer_v1': vergl})


def strahl(ctx, j):
    d = ln.fib(N_STRAHL)[j]
    dw = ctx['B4'] @ np.r_[0.0, d]
    dw = dw - dw.mean()
    sw = rv.strahl_wand(ctx['A'], ctx['G0'], ctx['w_mid'], dw)
    return d, dw, sw


def modus_strahlen(teil, aus):
    ctx = kontext(1)
    proben = []
    idx = range(64 * teil, 64 * (teil + 1))
    if RAUCH:
        idx = list(idx)[:2]
    for j in idx:
        d, dw, sw = strahl(ctx, j)
        for s in S_STRAHL:
            proben.append(probe(ctx, ctx['w_mid'] + s * sw * dw, {'gruppe': 'F43', 'richtung': j, 's': s, 's_wand': sw,
                                                                   'z': ctx['z_mid'] + s * sw * d}))
    log('Strahlen fertig')
    schreiben(aus, {'teil': teil, 'proben': proben})


def modus_null(aus):
    ctx = kontext(1)
    net, topo, G0, AZ, z_mid = ctx['net'], ctx['topo'], ctx['G0'], ctx['AZ'], ctx['z_mid']
    cache = {}
    zaehl = {'beta': 0}

    def beta_z(z):
        key = tuple(np.round(np.asarray(z, float), 13))
        if key in cache:
            return cache[key]
        _, sk = rv.messen(net, topo, wz(ctx, z), ctx['ref'], ctx['nd'])
        b = rv.kurz(sk)['beta'] if sk is not None else float('nan')
        cache[key] = b
        zaehl['beta'] += 1
        return b

    def grad(z):
        g = np.zeros(3)
        for i in range(3):
            e = np.zeros(3)
            e[i] = H_GRAD
            g[i] = (beta_z(z + e) - beta_z(z - e)) / (2 * H_GRAD)
        return g

    def marge_z(z):
        return float((G0 + AZ @ np.asarray(z, float)).min())

    b_mid = beta_z(z_mid)
    # Stufe 1: Strahlen
    n_str = 6 if RAUCH else N_STRAHL
    strahlen, nullen = [], []
    for j in range(n_str):
        d, dw, sw = strahl(ctx, j)
        bs = [beta_z(z_mid + s * sw * d) for s in S_STRAHL]
        strahlen.append({'richtung': j, 's_wand': sw, 'beta': bs})
        ps, pb = 0.0, b_mid
        for s, b in zip(S_STRAHL, bs):
            if b == 0.0:
                nullen.append({'quelle': 'strahl', 'richtung': j, 's': s, 'z': z_mid + s * sw * d})
                break
            if b < 0 < pb:
                t0 = brentq(lambda t: beta_z(z_mid + t * sw * d), ps, s, xtol=1e-13, maxiter=100)
                nullen.append({'quelle': 'strahl', 'richtung': j, 's': t0, 'z': z_mid + t0 * sw * d})
                break
            ps, pb = s, b
    log('Stufe 1 fertig')
    # Stufe 1b
    stufe1b = []
    if len(nullen) < 3:
        pts = sorted([(b, j, i) for j, e in enumerate(strahlen) for i, b in enumerate(e['beta'])])[:4]
        for b, j, i in pts:
            d, dw, sw = strahl(ctx, j)
            z0 = z_mid + S_STRAHL[i] * sw * d
            res = minimize(lambda z: beta_z(z) / abs(b_mid), z0, jac=lambda z: grad(z) / abs(b_mid), method='SLSQP',
                           constraints=[{'type': 'ineq', 'fun': lambda z: G0 + AZ @ z - EPS_MIN, 'jac': lambda z: AZ}],
                           options={'maxiter': 2 if RAUCH else 60, 'ftol': 1e-14})
            zmin = res.x
            bmin = beta_z(zmin)
            rec = {'start': z0, 'z_min': zmin, 'beta_min': bmin, 'status': int(res.status), 'nit': int(res.nit)}
            if np.isfinite(bmin) and bmin < -TOL_BETA0:
                t0 = brentq(lambda t: beta_z(z_mid + t * (zmin - z_mid)), 0.0, 1.0, xtol=1e-13, maxiter=100)
                nullen.append({'quelle': 'stufe1b', 's': t0, 'z': z_mid + t0 * (zmin - z_mid)})
                rec['nullpunkt'] = True
            stufe1b.append(rec)
        log('Stufe 1b fertig')
    for n in nullen:
        n['beta'] = beta_z(n['z'])
        n['marge'] = marge_z(n['z'])

    # Stufe 2: groesste Marge auf beta = 0
    def polieren(z):
        g = grad(z)
        gn = g / np.linalg.norm(g)
        tau = 0.05
        for _ in range(6):
            fa, fb = beta_z(z - tau * gn), beta_z(z + tau * gn)
            if np.isfinite(fa) and np.isfinite(fb) and fa * fb < 0:
                t = brentq(lambda x: beta_z(z + x * gn), -tau, tau, xtol=1e-13, maxiter=100)
                return z + t * gn
            tau *= 2
        return None

    kand = []
    start = sorted(nullen, key=lambda n: -n['marge'])[:(1 if RAUCH else 3)]
    jac_lin = np.hstack([AZ, -np.ones((len(G0), 1))])
    for n in start:
        if time.time() - T0 > ZEIT_STUFE2:
            kand.append({'quelle': 'slsqp', 'uebersprungen': 'Zeitwaechter'})
            continue
        cons = [{'type': 'ineq', 'fun': lambda x: G0 + AZ @ x[:3] - x[3], 'jac': lambda x: jac_lin},
                {'type': 'eq', 'fun': lambda x: np.array([beta_z(x[:3]) / abs(b_mid)]),
                 'jac': lambda x: (np.r_[grad(x[:3]), 0.0] / abs(b_mid))[None, :]}]
        try:
            res = minimize(lambda x: -x[3], np.r_[n['z'], n['marge']], jac=lambda x: np.array([0.0, 0.0, 0.0, -1.0]),
                           method='SLSQP', constraints=cons, options={'maxiter': 3 if RAUCH else 60, 'ftol': 1e-12})
            z1 = res.x[:3]
            zp = polieren(z1) if np.all(np.isfinite(z1)) else None
            kand.append({'quelle': 'slsqp', 'start_richtung': n.get('richtung'), 'status': int(res.status),
                         'nit': int(res.nit), 'meldung': str(res.message), 'z_slsqp': z1, 'z': zp})
        except Exception as ex:          # noqa: BLE001  (Fehler wird ausgewiesen, kein Abbruch)
            kand.append({'quelle': 'slsqp', 'fehler': repr(ex)})
    log('Stufe 2 fertig')
    alle = []
    for c in nullen + kand:
        z = c.get('z')
        if z is None:
            c['gueltig_null'] = False
            continue
        c['beta'] = beta_z(z)
        c['marge'] = marge_z(z)
        st = sterne_licht(net, topo, ctx['mb'], wz(ctx, z))
        c['sterne_positiv'] = sterne_positiv(st)
        c['gueltig_null'] = bool(np.isfinite(c['beta']) and abs(c['beta']) <= TOL_BETA0 and c['marge'] > TOL_MARGE
                                 and c['sterne_positiv'])
        if c['gueltig_null']:
            alle.append(c)
    w0 = None
    if alle:
        best = max(c['marge'] for c in alle)
        gl = [c for c in alle if c['marge'] >= best - 1e-9]
        w0 = max(gl, key=lambda c: c['z'][0] - c['z'][1])
    out = {'b_mid': b_mid, 'strahlen': strahlen, 'stufe1b': stufe1b, 'nullen': nullen, 'kandidaten': kand,
           'n_beta_auswertungen': zaehl['beta']}
    if w0 is not None:
        out['w0_stern'] = {k: v for k, v in w0.items()}
        out['w0_stern']['w'] = wz(ctx, w0['z'])
        out['w0_probe'] = probe(ctx, wz(ctx, w0['z']), {'gruppe': 'N', 'quelle': w0['quelle'], 'z': w0['z'], 'w0_stern': True},
                                je_richtung=True, fen_probe=True, mit_lhaaso=True)
        log('w0* gemessen')
        rest = sorted([c for c in alle if c is not w0], key=lambda c: -c['marge'])
        if RAUCH:
            rest = rest[:2]
        npr = [out['w0_probe']]
        n_aus = 0
        for c in rest:
            if time.time() - T0 > ZEIT_NULLMESS:
                n_aus += 1
                continue
            npr.append(probe(ctx, wz(ctx, c['z']), {'gruppe': 'N', 'quelle': c['quelle'], 'z': c['z'], 'w0_stern': False}))
        out['null_proben'] = npr
        out['null_proben_ausgelassen_zeit'] = n_aus
    else:
        out['w0_stern'] = None
        out['null_proben'] = []
    log('Nullpunkte gemessen')
    schreiben(aus, out)


def modus_gitter(aus):
    ctx = kontext(1)
    net = ctx['net']
    E = np.array(rv.HAND['ecken_schnitt'])
    mid = np.array([ctx['xm'], ctx['ym']])
    m = 2 if RAUCH else 24
    proben = []
    for i in range(m + 1):
        for j in range(m + 1 - i):
            k = m - i - j
            p = (i * E[0] + j * E[1] + k * E[2]) / m
            p = mid + 0.99 * (p - mid)
            proben.append(probe(ctx, rv.w_sym(net, p[0], p[1]), {'gruppe': 'G', 'x': float(p[0]), 'y': float(p[1])}))
    log('Gitter fertig')
    schreiben(aus, {'proben': proben})


def modus_l2(aus, anzahl):
    ctx = kontext(2)
    net, A, G0, w_mid = ctx['net'], ctx['A'], ctx['G0'], ctx['w_mid']
    proben = [probe(ctx, w_mid, {'gruppe': 'L2', 'art': 'mitte_gekachelt'})]
    log('L2 Mitte fertig')
    rng = np.random.default_rng([4096, 2, 7])
    for j in range(anzahl):
        d = rng.standard_normal(net['n'])
        d -= d.mean()
        d /= np.linalg.norm(d)
        sw = rv.strahl_wand(A, G0, w_mid, d)
        proben.append(probe(ctx, w_mid + 0.9 * sw * d, {'gruppe': 'L2', 'richtung': j, 's': 0.9, 's_wand': sw}))
        log('L2 Richtung %d fertig' % j)
    schreiben(aus, {'proben': proben})


# ------------------------------------------------------------------------------------------------ Auswertung
def ein(flag):
    return 'eingetroffen' if flag else 'nicht eingetroffen'


def faktor(a, b):
    if a is None or b is None or a <= 0 or b <= 0:
        return float('inf')
    return max(a / b, b / a)


def schranke_l(sch, zweig, art):
    r = sch[zweig]
    if r is None or art not in r:
        return None
    return r[art]['l_m']


def urteilen(mitte, proben, f0, f1, null, gitter, l2):
    U = {}
    pm = mitte['probe_mitte']
    w0p = null.get('w0_probe')
    # HI0
    rep = mitte['reproduktion']
    a_rel = all(r['abw_rel'] <= 1e-6 for r in rep)
    a_abs = all(r['abw_abs'] <= 1e-6 for r in rep)
    b = null.get('w0_stern') is not None and bool(null['w0_stern'].get('gueltig_null'))
    U['HI0'] = {'a_rel_1e-6': a_rel, 'a_abs_1e-6': a_abs, 'b_nullpunkt': b, 'reproduktion': rep,
                'urteil_plan': ein(a_rel and b), 'urteil_wortlaut': ein((a_rel or a_abs) and b)}
    if b:
        U['HI0']['w0_stern'] = {k: null['w0_stern'][k] for k in ('quelle', 'z', 'beta', 'marge')}
    # HI1
    bm = pm['licht']['maxwell_mittel']['beta']
    if not b or w0p is None or w0p['licht'] is None:
        U['HI1'] = {'urteil_plan': 'nicht auswertbar', 'urteil_wortlaut': 'nicht auswertbar', 'grund': 'kein w0*'}
    elif abs(bm) < 1e-9:
        U['HI1'] = {'urteil_plan': 'nicht auswertbar', 'urteil_wortlaut': 'nicht auswertbar', 'grund': 'beta_L(mitte) ~ 0',
                    'beta_L_mitte': bm}
    else:
        b0 = w0p['licht']['maxwell_mittel']['beta']
        R = abs(b0) / abs(bm)
        wl = {}
        for zw in ('maxwell_lo', 'maxwell_hi'):
            r0, rm = w0p['licht'][zw]['rms_l4'], pm['licht'][zw]['rms_l4']
            wl[zw] = {'rms_l4_w0': r0, 'rms_l4_mitte': rm, 'verh': r0 / rm if rm > 0 else None}
        flags = [v['verh'] is not None and v['verh'] < 1e-3 for v in wl.values()]
        Rs = []
        for p in null.get('null_proben', []):
            if p.get('licht') is not None and p['gueltig']:
                Rs.append(abs(p['licht']['maxwell_mittel']['beta']) / abs(bm))
        U['HI1'] = {'beta_L_mitte': bm, 'beta_L_w0': b0, 'R': R, 'urteil_plan': ein(R < 1e-3),
                    'wortlaut_rms_l4': wl, 'urteil_wortlaut': ln.urteil_menge(flags),
                    'R_alle_nullpunkte': {'n': len(Rs), 'min': min(Rs) if Rs else None, 'max': max(Rs) if Rs else None}}
    # HI2
    plan = [pm] + proben['proben'] + f0['proben'] + f1['proben'] + null.get('null_proben', []) + gitter['proben']
    gp = [p for p in plan if p['gueltig']]
    ungueltig = [{k: p.get(k) for k in ('gruppe', 'richtung', 's', 'ziel', 'ecke_index', 'x', 'y', 'marge')}
                 for p in plan if not p['gueltig']]
    a_mid = pm['licht']['maxwell_mittel']['a2_mittel']
    a = np.array([p['licht']['maxwell_mittel']['a2_mittel'] for p in gp])
    alle_neg = bool(np.all(a < 0)) and a_mid < 0
    fak = float(max(max(x / a_mid, a_mid / x) for x in a)) if alle_neg else float('inf')
    j_lo, j_hi = int(np.argmin(np.abs(a))), int(np.argmax(np.abs(a)))
    ort = lambda p: {k: p.get(k) for k in ('gruppe', 'richtung', 's', 'ziel', 'ecke_index', 'x', 'y', 'z', 'marge')}
    U['HI2'] = {'n_plan': len(plan), 'n_gueltig': len(gp), 'ungueltig': ungueltig, 'a2_mitte': a_mid,
                'a2_min_betrag': float(a[j_lo]), 'ort_min_betrag': ort(gp[j_lo]), 'a2_max_betrag': float(a[j_hi]),
                'ort_max_betrag': ort(gp[j_hi]), 'alle_negativ': alle_neg, 'faktor_zur_mitte_max': fak,
                'urteil_plan': ein(alle_neg and fak <= 2.0)}
    wl = gp + ([p for p in l2['proben'] if p['gueltig']] if l2 is not None else [])
    aw = np.array([p['licht']['maxwell_mittel']['a2_mittel'] for p in wl])
    neg3 = all(p['licht'][zw]['a2_mittel'] < 0 for p in wl for zw in ZWEIGE)
    spanne = float(np.max(np.abs(aw)) / np.min(np.abs(aw))) if neg3 else float('inf')
    U['HI2'].update({'wortlaut_n': len(wl), 'wortlaut_l2_n': (len(wl) - len(gp)), 'wortlaut_alle_zweige_negativ': neg3,
                     'wortlaut_spanne': spanne, 'urteil_wortlaut': ein(neg3 and spanne <= 2.0),
                     'l2_ungueltig': ([p.get('richtung', p.get('art')) for p in l2['proben'] if not p['gueltig']]
                                      if l2 is not None else None)})
    # HI3
    if w0p is None or 'lhaaso' not in w0p:
        U['HI3'] = {'urteil_plan': 'nicht auswertbar', 'urteil_wortlaut': 'nicht auswertbar'}
    else:
        sm, s0 = pm['lhaaso']['schranken'], w0p['lhaaso']['schranken']
        lm, l0 = schranke_l(sm, 2, 'mittel_abs_a2'), schranke_l(s0, 2, 'mittel_abs_a2')
        F = faktor(lm, l0)
        wfl, wtab = [], {}
        for zi, zw in ((0, 'maxwell_lo'), (1, 'maxwell_hi')):
            for art in ('konservativ_min_abs_a2', 'streng_max_abs_a2'):
                a_, b_ = schranke_l(sm, zi, art), schranke_l(s0, zi, art)
                f_ = faktor(a_, b_)
                wtab['%s/%s' % (zw, art)] = {'l_mitte_m': a_, 'l_w0_m': b_, 'faktor': f_}
                wfl.append(f_ < 3.0)
        U['HI3'] = {'l_mittel_mitte_m': lm, 'l_mittel_w0_m': l0, 'faktor': F, 'urteil_plan': ein(F < 3.0),
                    'wortlaut': wtab, 'urteil_wortlaut': ln.urteil_menge(wfl),
                    'kugelmittel': {'mitte': pm['lhaaso']['kugelmittel'], 'w0': w0p['lhaaso']['kugelmittel']}}
    # Beschreibend
    bes = {}
    alle_p = [p for p in plan if p['gueltig']]
    bl = np.array([p['licht']['maxwell_mittel']['beta'] for p in alle_p])
    jm = int(np.argmin(np.abs(bl)))
    bes['beta_L'] = {'min': float(bl.min()), 'max': float(bl.max()), 'n_negativ': int(np.sum(bl < 0)),
                     'min_betrag': float(bl[jm]), 'ort_min_betrag': ort(alle_p[jm]),
                     'min_betrag_rel_mitte': float(abs(bl[jm]) / abs(bm)) if bm != 0 else None}
    for nm, grp in (('F43', f0['proben'] + f1['proben']), ('G', gitter['proben'])):
        gg = [p for p in grp if p['gueltig']]
        if gg:
            b_ = np.array([p['licht']['maxwell_mittel']['beta'] for p in gg])
            bs_ = np.array([p['skalar']['beta'] for p in gg])
            bes['beta_L_' + nm] = {'min': float(b_.min()), 'max': float(b_.max()), 'n_negativ': int(np.sum(b_ < 0)),
                                   'n': len(gg), 'skalar_min': float(bs_.min()), 'skalar_n_negativ': int(np.sum(bs_ < 0))}
    ray = {}
    for p in f0['proben'] + f1['proben']:
        if p['gueltig']:
            ray.setdefault(p['richtung'], []).append(p['licht']['maxwell_mittel']['beta'])
    bes['F43_strahlen_mit_vorzeichenwechsel_beta_L'] = int(sum(1 for v in ray.values() if (min(v) < 0 < bm) or
                                                               (max(v) > 0 > bm)))
    db = [p['licht']['doppelbrechung_a2_max'] for p in alle_p]
    bes['doppelbrechung_a2_max'] = float(max(db))
    bes['doppelbrechung_mitte'] = pm['licht']['doppelbrechung_a2_max']
    bes['doppelbrechung_w0'] = w0p['licht']['doppelbrechung_a2_max'] if w0p is not None else None
    cm = [abs(p['licht'][zw]['c_mittel'] - 1.0) for p in alle_p for zw in ZWEIGE]
    cs = [p['licht'][zw]['c_spanne_rel'] for p in alle_p for zw in ZWEIGE]
    bes['c_abw_max'] = float(max(cm))
    bes['c_spanne_max'] = float(max(cs))
    bes['id_T2_max'] = float(max(p['sterne']['id_T2'] for p in alle_p))
    bes['symmetrie_mitte'] = {k: pm['licht']['maxwell_mittel'][k] for k in ('rms_l2', 'nichtkub4_rms', 'rms_l6')}
    if w0p is not None:
        bes['symmetrie_w0'] = {k: w0p['licht']['maxwell_mittel'][k] for k in ('rms_l2', 'nichtkub4_rms', 'rms_l6')}
    bes['skalar_vergleich_regulaer_v1'] = proben.get('vergleich_regulaer_v1')
    U['beschreibend'] = bes
    return U


def modus_auswerten(aus, pfade):
    d = [json.load(open(p)) for p in pfade]
    mitte, proben, f0, f1, null, gitter = d[:6]
    l2 = d[6] if len(d) > 6 else None
    U = urteilen(mitte, proben, f0, f1, null, gitter, l2)
    for k, v in U.items():
        log(k, json.dumps(ln.js(v))[:700])
    schreiben(aus, {'urteile': U, 'eingaben': {p: sha(p) for p in pfade}})


def main():
    a = [x for x in sys.argv[1:] if x != '--rauch']
    if not a:
        print(__doc__)
        return 2
    if a[0] == 'rauch':
        modus_rauch(a[1])
    elif a[0] == 'mitte':
        modus_mitte(a[1], a[2], a[3])
    elif a[0] == 'proben':
        modus_proben(a[1], a[2])
    elif a[0] == 'strahlen':
        modus_strahlen(int(a[1]), a[2])
    elif a[0] == 'null':
        modus_null(a[1])
    elif a[0] == 'gitter':
        modus_gitter(a[1])
    elif a[0] == 'l2':
        modus_l2(a[1], int(a[2]) if len(a) > 2 else 4)
    elif a[0] == 'auswerten':
        modus_auswerten(a[1], a[2:])
    else:
        print(__doc__)
        return 2
    log('fertig')
    return 0


if __name__ == '__main__':
    sys.exit(main())
