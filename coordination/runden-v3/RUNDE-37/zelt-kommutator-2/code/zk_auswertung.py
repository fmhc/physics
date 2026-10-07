#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZELT-KOMMUTATOR-2: mechanische Auswertung nach PLAN.md (Urteile ZP0 bis ZP3, UT1 bis UT4, Kontrollen K1 bis K7).
Aufruf: zk_auswertung.py <ordner mit kb.json ki.json dl.json dg.json ut.json ko_pt1.json> --out auswertung.json
"""
import argparse, json, os, sys, hashlib, time
import numpy as np

TAUS = [0.2, 0.1, 0.05, 0.025]
TAU_HAUPT = 0.1
LAS = [4.0, 8.0, 16.0, 32.0]
RUND = 1e-13


def lade(d, nm):
    with open(os.path.join(d, nm)) as f:
        return json.load(f)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def fit(las, ys):
    ys = np.asarray(ys, float)
    if np.any(~np.isfinite(ys)) or np.any(ys < RUND):
        return {'p': None, 'se': None, 'lokal': None, 'unter_rundung': True}
    x = np.log(1.0 / np.asarray(las, float))
    y = np.log(ys)
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = y - A @ coef
    n = len(x)
    se = float(np.sqrt((r @ r) / (n - 2) / ((x - x.mean()) @ (x - x.mean())))) if n > 2 else None
    lok = [float((y[i + 1] - y[i]) / (x[i + 1] - x[i])) for i in range(n - 1)]
    return {'p': float(coef[0]), 'se': se, 'lokal': lok, 'unter_rundung': False}


def tau_eintrag(dx, tau):
    for r in dx['tau']:
        if abs(r['tau'] - tau) < 1e-12:
            return r
    return None


def welle(r, eps, La):
    for w in r['welle']:
        if abs(w['eps'] - eps) < 1e-15 and abs(w['La'] - La) < 1e-12:
            return w
    return None


def robust(urteile):
    """urteile: dict tau -> Urteil (str). Gleich bei allen tau -> dieses, sonst unklar."""
    vals = set(urteile.values())
    return vals.pop() if len(vals) == 1 else 'unklar (haengt an der Regularisierung)'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ordner')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    d = a.ordner
    kb = lade(d, 'kb.json')
    ki = lade(d, 'ki.json')
    D = {'L': lade(d, 'dl.json'), 'G': lade(d, 'dg.json')}
    ut = lade(d, 'ut.json')
    ko = lade(d, 'ko_pt1.json')
    aus = {'eingaben': {nm: sha(os.path.join(d, nm)) for nm in ('kb.json', 'ki.json', 'dl.json', 'dg.json', 'ut.json', 'ko_pt1.json')},
           'skripte': {nm: x['info']['skript_sha256'] for nm, x in (('kb', kb), ('ki', ki), ('dl', D['L']), ('dg', D['G']), ('ut', ut))},
           'auswertung_sha256': sha(os.path.abspath(__file__)),
           'zeit_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    U = {}
    dfk = {v: D[v]['defekte'] for v in ('L', 'G')}
    global TAUS
    TAUS = [r['tau'] for r in dfk['L']['tau']]          # aus den Daten (Hauptlauf: alle vier tau)
    assert TAUS == [r['tau'] for r in dfk['G']['tau']] and TAU_HAUPT in TAUS
    aus['tau_liste'] = TAUS

    # Teil A: Hauptmass linear (Karte: "linearisiert"); d_j = eps ||(Q_j - Q_(j-1)) w||, Verhaeltnisse eps-frei.
    def lin(var, tau, La):
        r = tau_eintrag(dfk[var], tau)
        for li in r['linear']:
            if abs(li['La'] - La) < 1e-12:
                return li

    # ---------------- ZP0
    def zp0(var, tau, epsf):
        r = tau_eintrag(dfk[var], tau)
        lf = r['linear_flach']
        lin_rel = epsf * max(lf['d_lin']) / lf['p0_norm']
        nl_rel = None
        for f in r['flach']:
            if abs(f['eps'] - epsf) < 1e-15 and 'd' in f:
                nl_rel = max(f['d']) / f['p_norm']
        return {'linear': lin_rel, 'nichtlinear': nl_rel}

    def zp0_ok(x):
        return x['linear'] < 1e-13 and (x['nichtlinear'] is None or x['nichtlinear'] < 1e-13)
    k0 = {'%s|%g|%g' % (v, t, e): zp0(v, t, e) for v in ('L', 'G') for t in TAUS for e in (1e-3, 1e-4)}
    plan0 = all(zp0_ok(k0['%s|%g|%g' % (v, TAU_HAUPT, 1e-3)]) for v in ('L', 'G'))
    wl0 = {t: ('eingetroffen' if all(zp0_ok(k0['%s|%g|%g' % (v, t, e)]) for v in ('L', 'G') for e in (1e-3, 1e-4))
               else 'nicht eingetroffen') for t in TAUS}
    U['ZP0'] = {'plan': 'eingetroffen' if plan0 else 'nicht eingetroffen', 'wortlaut': robust(wl0),
                'wortlaut_je_tau': wl0, 'max_d_rel': k0,
                'nichtlinear_fehlt': sorted(k for k, x in k0.items() if x['nichtlinear'] is None)}

    # ---------------- ZP1
    b = kb['kb']['bfs']
    if b['kuerzeste_laenge'] is None:
        z1 = 'nicht auswertbar'
    else:
        z1 = 'eingetroffen' if b['jeder_mit_33'] else 'nicht eingetroffen'
    U['ZP1'] = {'plan': z1, 'wortlaut': z1, 'kuerzeste_laenge': b['kuerzeste_laenge'], 'n_kuerzeste': b['n_kuerzeste'],
                'zusammensetzung': b['zusammensetzung'], 'laengen_mit_treffer': b['laengen_mit_treffer']}

    # ---------------- ZP2 (linear)
    def zp2(var, tau):
        out = []
        for La in LAS:
            li = lin(var, tau, La)
            s = sum(li['d_lin'])
            out.append({'La': La, 'summe_d_lin': s, 'D_lin': li['D_lin'], 'rel': (s - li['D_lin']) / li['D_lin']})
        return out
    k2 = {'%s|%g' % (v, t): zp2(v, t) for v in ('L', 'G') for t in TAUS}
    plan2 = all(abs(x['rel']) <= 0.01 for x in k2['L|%g' % TAU_HAUPT])
    wl2 = {t: ('eingetroffen' if all(abs(x['rel']) <= 0.01 for v in ('L', 'G') for x in k2['%s|%g' % (v, t)])
               else 'nicht eingetroffen') for t in TAUS}
    U['ZP2'] = {'plan': 'eingetroffen' if plan2 else 'nicht eingetroffen', 'wortlaut': robust(wl2),
                'wortlaut_je_tau': wl2, 'werte': k2}

    # ---------------- ZP3 (linear)
    def zp3(var, tau):
        ls = [lin(var, tau, La) for La in LAS]
        D4 = ls[0]['D_lin']
        rel = [j for j in range(len(ls[0]['d_lin'])) if ls[0]['d_lin'][j] > 1e-6 * D4]
        ex = {j: fit(LAS, [li['d_lin'][j] for li in ls]) for j in rel}
        if not rel or any(e['unter_rundung'] for e in ex.values()):
            urt = 'nicht auswertbar'
        else:
            urt = 'eingetroffen' if all(2.0 <= e['p'] <= 2.5 for e in ex.values()) else 'nicht eingetroffen'
        return {'zuege_relevant': rel, 'exponenten': {str(j): e for j, e in ex.items()}, 'urteil': urt,
                'typen': dfk[var]['typen'], 'D_lin_fit': fit(LAS, [li['D_lin'] for li in ls]),
                'summe_fit': fit(LAS, [sum(li['d_lin']) for li in ls])}
    k3 = {'%s|%g' % (v, t): zp3(v, t) for v in ('L', 'G') for t in TAUS}
    plan3 = k3['L|%g' % TAU_HAUPT]['urteil']

    def agg(urts):
        if all(u == 'eingetroffen' for u in urts):
            return 'eingetroffen'
        if any(u == 'nicht auswertbar' for u in urts):
            return 'nicht auswertbar'
        return 'nicht eingetroffen'
    wl3 = {t: agg([k3['%s|%g' % (v, t)]['urteil'] for v in ('L', 'G')]) for t in TAUS}
    U['ZP3'] = {'plan': plan3, 'wortlaut': robust(wl3), 'wortlaut_je_tau': wl3, 'werte': k3}

    # ---------------- UT1 bis UT4
    def ut_werte(var, eps):
        u = ut['uhr'][var]
        out = []
        for La in LAS:
            for w in u['welle']:
                if abs(w['eps'] - eps) < 1e-15 and abs(w['La'] - La) < 1e-12:
                    out.append(w)
        return out
    qs = {}
    for v in ('L', 'G'):
        for e in (1e-3, 1e-4):
            ws = ut_werte(v, e)
            qs['%s|%g' % (v, e)] = {'D_T': [w['D_T'] for w in ws], 'fit': fit(LAS, [w['D_T'] for w in ws]),
                                   'D': [w['D'] for w in ws], 'D_fit': fit(LAS, [w['D'] for w in ws])}

    def klasse(q):
        if q is None:
            return None
        return 'UT1' if q >= 2.75 else ('UT2' if q >= 1.75 else 'UT3')
    haupt = qs['L|%g' % 1e-3]
    if all(x < RUND for x in haupt['D_T']):
        for n in ('UT1', 'UT2', 'UT3'):
            U[n] = {'plan': 'nicht auswertbar (D_T verschwindet)', 'wortlaut': 'nicht auswertbar (D_T verschwindet)'}
    else:
        kp = klasse(haupt['fit']['p'])
        kl_alle = [klasse(qs[k]['fit']['p']) for k in qs]
        for n in ('UT1', 'UT2', 'UT3'):
            if kp is None:
                pl = 'nicht auswertbar'
            else:
                pl = 'eingetroffen' if kp == n else 'nicht eingetroffen'
            treffer = sum(1 for k in kl_alle if k == n)
            if any(k is None for k in kl_alle):
                wl = 'nicht auswertbar'
            elif treffer == len(kl_alle):
                wl = 'eingetroffen'
            elif treffer > 0:
                wl = 'unklar'
            else:
                wl = 'nicht eingetroffen'
            U[n] = {'plan': pl, 'wortlaut': wl}
    U['UT_q'] = qs
    rat = {}
    for v in ('L', 'G'):
        a1 = ut_werte(v, 1e-3)
        a4 = ut_werte(v, 1e-4)
        rat[v] = [x['D_T'] / y['D_T'] if y['D_T'] > 0 else None for x, y in zip(a1, a4)]
    ok = lambda r: r is not None and 9.0 <= r <= 11.0
    U['UT4'] = {'plan': 'eingetroffen' if all(ok(r) for r in rat['L']) else 'nicht eingetroffen',
                'wortlaut': 'eingetroffen' if all(ok(r) for v in ('L', 'G') for r in rat[v]) else 'nicht eingetroffen',
                'verhaeltnis': rat}
    aus['urteile'] = U

    # ---------------- Kontrollen
    K = {}
    k1 = {}
    for v in ('L', 'G'):
        ref = {x['La']: x['D'] for x in ko['ko'][v]['L_scan']}
        for w in ut_werte(v, 1e-3):
            k1['%s|%g' % (v, w['La'])] = {'D': w['D'], 'D_pt': w['D_pt'], 'ref': ref[w['La']],
                                          'rel': abs(w['D'] - ref[w['La']]) / ref[w['La']],
                                          'rel_pt': abs(w['D_pt'] - ref[w['La']]) / ref[w['La']]}
    K['K1'] = {'ok': all(x['rel'] <= 1e-8 and x['rel_pt'] <= 1e-8 for x in k1.values()), 'werte': k1}
    k2 = {}
    for v in ('L', 'G'):
        u = ut['uhr'][v]
        k2[v] = {'null_D_T_max': max(x['D_T'] for x in u['null']),
                 'T_null_rel': max(abs(x['T_AB'] - u['T_analytisch']) / u['T_analytisch'] for x in u['null']),
                 'T_null_BA_rel': max(abs(x['T_BA'] - u['T_analytisch']) / u['T_analytisch'] for x in u['null']),
                 'flach_D_T': [x['D_T'] for x in u['flach']], 'flach_D_rel': [x['D'] / x['p_norm'] for x in u['flach']]}
    K['K2'] = {'ok': all(x['null_D_T_max'] <= 1e-13 and x['T_null_rel'] <= 1e-13 and x['T_null_BA_rel'] <= 1e-13
                         and max(x['flach_D_T']) <= 1e-13 for x in k2.values()), 'werte': k2}
    voll = lambda r: [w for w in r['welle'] + r['flach'] + [r['null']] if 'd' in w]
    tele = max(w['teleskop'] / w['p_norm'] for v in ('L', 'G') for r in dfk[v]['tau'] for w in voll(r))
    p5 = max(w['p_T5_gegen_pt'] / w['p_norm'] for v in ('L', 'G') for w in ut['uhr'][v]['welle'])
    K['K3'] = {'ok': tele <= 1e-12 and p5 <= 1e-12 and kb['kb']['kombinatorik']['BA_gleich_C_plus_R5'],
               'teleskop_max_rel': tele, 'p_T5_gegen_pt_max_rel': p5,
               'BA_gleich_C_plus_R5': kb['kb']['kombinatorik']['BA_gleich_C_plus_R5']}
    z24 = ki['ki']['zug_24']
    z33 = ki['ki']['zug_33']
    K['K4'] = {'ok': all(x['defekt_rel'] <= 1e-10 for x in z24)
               and all((x['defekt_rel'] <= 1e-12) if x['art'] == 'flach' else (x['defekt_rel'] > 1e-8) for x in z33),
               'zug_24': z24, 'zug_33': z33, 'geo_24': ki['ki']['geo_24'], 'geo_33': ki['ki']['geo_33']}
    aw = kb['kb']['auswahl']
    K['K5'] = {'ok': aw is not None and aw['je_variante_erster']['L'] == aw['je_variante_erster']['G'],
               'je_variante_erster': None if aw is None else aw['je_variante_erster']}
    resmax = max(max(rr / w['p_norm'] for rr in w['res']) for v in ('L', 'G') for r in dfk[v]['tau'] for w in voll(r))
    resmax_ut = max(max(rr / w['p_norm'] for rr in w['res']) for v in ('L', 'G') for w in ut['uhr'][v]['welle'])
    fehl = {'%s|%g' % (v, r['tau']): sorted('%s|%g|%g' % (w['art'], w['eps'], w['La'])
                                             for w in r['welle'] + r['flach'] + [r['null']] if 'fehler' in w)
            for v in ('L', 'G') for r in dfk[v]['tau']}
    dtau = {}
    dlin = {}
    for v in ('L', 'G'):
        u0 = {(w['eps'], w['La']): w['D'] for w in ut['uhr'][v]['welle']}
        for r in dfk[v]['tau']:
            dtau['%s|%g' % (v, r['tau'])] = [w['D'] / u0[(w['eps'], w['La'])] - 1.0 for w in r['welle'] if 'D' in w]
            dlin['%s|%g' % (v, r['tau'])] = [w['D'] / (w['eps'] * lin(v, r['tau'], w['La'])['D_lin']) - 1.0
                                             for w in r['welle'] if 'D' in w]
    K['K6'] = {'ok': resmax <= 1e-12 and resmax_ut <= 1e-12, 'newton_rest_max_rel': resmax,
               'newton_rest_max_rel_uhr': resmax_ut, 'nichtlinear_nicht_loesbar': fehl,
               'D_tau_gegen_D0_minus_1': dtau, 'D_tau_gegen_eps_D_lin_minus_1': dlin}
    typen = dfk['L']['typen']
    dks = []
    for v in ('L', 'G'):
        for t in TAUS:
            for La in LAS:
                li = lin(v, t, La)
                for j, ty in enumerate(typen):
                    dks.append((v, t, La, j, ty, li['d_lin'][j] / li['D_lin']))
    K['K7'] = {'ok': all((q <= 1e-10) if ty in ('2-4', '4-2') else (q >= 1e-3) for (_, _, _, _, ty, q) in dks),
               'max_24_42_rel': max([x[5] for x in dks if x[4] in ('2-4', '4-2')] or [None]),
               'min_33_rel': min([x[5] for x in dks if x[4] == '3-3'] or [None])}
    k8 = {}
    for v in ('L', 'G'):
        for r in dfk[v]['tau']:
            for w in r['welle']:
                if 'd' in w:
                    li = lin(v, r['tau'], w['La'])
                    k8['%s|%g|%g|%g' % (v, r['tau'], w['eps'], w['La'])] = [
                        (w['d'][j] / (w['eps'] * li['d_lin'][j]) if li['d_lin'][j] > 1e-6 * li['D_lin'] else None)
                        for j in range(len(typen))]
    K['K8_nichtlinear_gegen_linear_je_zug'] = k8
    aus['kontrollen'] = K

    # ---------------- beschreibend
    B = {}
    for v in ('L', 'G'):
        for r in dfk[v]['tau']:
            for w in r['welle']:
                if 'd' in w:
                    B['%s|%g|%g|%g' % (v, r['tau'], w['eps'], w['La'])] = {
                        'd': w['d'], 'D': w['D'], 'summe_d': w['summe_d'], 'dS': w['dS'], 'dT': w['dT'],
                        'D_T_je_zug': [x / w['T'][0] for x in w['dT']], 'D_T_ende': (w['T'][-1] - w['T'][0]) / w['T'][0]}
            for li in r['linear']:
                B['lin|%s|%g|%g' % (v, r['tau'], li['La'])] = li
            B['linflach|%s|%g' % (v, r['tau'])] = r['linear_flach']
            B['Hii_cond|%s|%g' % (v, r['tau'])] = r['Hii_cond']
    aus['beschreibend'] = B
    aus['alle_geometrischen_wege_haupt'] = {v: dfk[v].get('alle_geometrischen_wege_haupt') for v in ('L', 'G')}
    with open(a.out + '.tmp', 'w') as f:
        json.dump(aus, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('auswertung fertig', flush=True)


if __name__ == '__main__':
    main()
