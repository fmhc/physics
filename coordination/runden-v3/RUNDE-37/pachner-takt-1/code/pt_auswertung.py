#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PACHNER-TAKT-1: Urteile PT0 bis PT3 mechanisch nach PLAN.md Abschnitt 2.2."""
import argparse, json, os, glob, hashlib, time
import numpy as np


def steigung(x, y):
    x = np.log(np.asarray(x, float)); y = np.log(np.asarray(y, float))
    A = np.vstack([x, np.ones_like(x)]).T
    return float(np.linalg.lstsq(A, y, rcond=None)[0][0])


def lade(p):
    with open(p) as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    faelle = []
    quellen = {}
    for p in sorted(glob.glob(os.path.join(a.lauf, 'takt-*.json'))):
        d = lade(p)
        quellen[os.path.basename(p)] = d['info']['skript_sha256']
        faelle += d['faelle']
    kc = lade(os.path.join(a.lauf, 'kc.json'))
    quellen['kc.json'] = kc['info']['skript_sha256']
    kc = kc['kc']
    ko = lade(os.path.join(a.lauf, 'ko.json'))
    quellen['ko.json'] = ko['info']['skript_sha256']
    ko = ko['ko']

    def fall(var, n, m):
        for f in faelle:
            if f['variante'] == var and f['n'] == n and f['m'] == m:
                return f
        return None
    tab = [{k: f[k] for k in ('variante', 'n', 'm', 'V', 'E0', 'ET', 'G0', 'GT', 'r', 'r_luecke', 'pre', 'post',
                              'pre_nicht_eich', 'post_nicht_eich', 'n_innen', 'bulk_null', 'eich_innen_rang', 'n_x',
                              'n_x_kopplung_rel', 'vol_rel_min', 'innen_fehlwinkel_max', 'Omega_Y_T_rel',
                              'Omega_Y_0_rel', 'H_Y_innen_rel', 'schlaefli', 'M_sym', 't_gesamt_s')}
           for f in faelle]
    for z in tab:
        z['r_je_V'] = z['r'] / z['V']
        z['E_minus_G'] = z['E0'] - z['G0']
    paare = sorted(set((f['n'], f['m']) for f in faelle))
    out = {'quellen_sha256': quellen, 'tabelle': tab, 'urteile': {}}

    # PT0
    a_ok, a_det = True, []
    for (n, m) in paare:
        b, tt = fall('B', n, m), fall('TT', n, m)
        if b is None or tt is None:
            continue
        ok = (b['r'] == tt['r']) and (b['n_x'] == tt['n_x'])
        a_det.append({'n': n, 'm': m, 'r_B': b['r'], 'r_TT': tt['r'], 'n_x_B': b['n_x'], 'n_x_TT': tt['n_x'], 'ok': ok})
        a_ok = a_ok and ok
    a_ok = a_ok and len(a_det) > 0
    b_det = {v: ko[v]['flach']['D_rel'] for v in ('L', 'G')}
    b_ok = all(x <= 1e-10 for x in b_det.values())
    es = ko['L']['eps_scan']
    c_st = steigung([z['eps'] for z in es], [z['D'] for z in es])
    c_ok = 1.8 <= c_st <= 2.2
    pt0 = a_ok and b_ok and c_ok
    out['urteile']['PT0'] = {'nach_plan': 'eingetroffen' if pt0 else 'nicht eingetroffen',
                             'nach_kartenwortlaut': 'eingetroffen' if pt0 else 'nicht eingetroffen',
                             'a_B_gleich_TT': a_ok, 'a_detail': a_det, 'b_flach_D_rel': b_det, 'b_ok': b_ok,
                             'c_steigung_eps': c_st, 'c_ok': c_ok,
                             'c_D_werte': [[z['eps'], z['D']] for z in es]}
    # PT1
    p1_det, p1_ok = [], True
    for n in (2, 3):
        fs = [f for f in faelle if f['variante'] == 'C2' and f['n'] == n]
        if not fs:
            p1_ok = False
            continue
        real = all(f['vol_rel_min'] > 1e-8 and f['innen_fehlwinkel_max'] <= 1e-10 for f in fs)
        loes = all(f['n_x'] == 0 or f['n_x_kopplung_rel'] <= 1e-8 for f in fs)
        rs = [f['r'] for f in sorted(fs, key=lambda f: f['m'])]
        gleich = len(set(rs)) == 1
        p1_det.append({'n': n, 'm': [f['m'] for f in sorted(fs, key=lambda f: f['m'])], 'r': rs,
                       'realisierbar': real, 'loesbar': loes, 'rang_gleich': gleich})
        p1_ok = p1_ok and real and loes and gleich
    kc_ok = kc['summenregel_max_abs'] <= 1e-12 and kc['rueckwechsel_noetig_gt_pi']
    out['urteile']['PT1'] = {'nach_plan': 'eingetroffen' if p1_ok else 'nicht eingetroffen',
                             'nach_kartenwortlaut': 'nicht eingetroffen [M]' if kc_ok else 'unklar',
                             'detail': p1_det, 'kc': kc}
    # PT2
    ms2 = set(f['m'] for f in faelle if f['variante'] == 'C2' and f['n'] == 2)
    ms3 = set(f['m'] for f in faelle if f['variante'] == 'C2' and f['n'] == 3)
    gem = sorted(ms2 & ms3)
    p2 = {'m_stern': None}
    p2_ok = False
    if gem:
        ms = gem[-1]
        f2, f3 = fall('C2', 2, ms), fall('C2', 3, ms)
        rate = (f3['r'] - f2['r']) / (f3['V'] - f2['V'])
        eich = max(f2['Omega_Y_T_rel'], f2['Omega_Y_0_rel'], f3['Omega_Y_T_rel'], f3['Omega_Y_0_rel'])
        p2_ok = f2['r'] / f2['V'] >= 1 and f3['r'] / f3['V'] >= 1 and rate >= 1 and eich <= 1e-9
        p2 = {'m_stern': ms, 'r_je_V_n2': f2['r'] / f2['V'], 'r_je_V_n3': f3['r'] / f3['V'], 'zellrate': rate,
              'eichprobe_max': eich}
    out['urteile']['PT2'] = dict(p2, nach_plan='eingetroffen' if p2_ok else 'nicht eingetroffen',
                                 nach_kartenwortlaut='eingetroffen' if p2_ok else 'nicht eingetroffen')
    # PT3
    ls = ko['L']['L_scan']
    p = -steigung([z['La'] for z in ls], [z['D'] for z in ls])
    D4 = [z['D'] for z in ls if z['La'] == 4.0]
    unter = (not D4) or D4[0] <= 1e-13
    p3_ok = (3 <= p <= 5) and not unter
    out['urteile']['PT3'] = {'nach_plan': 'eingetroffen' if p3_ok else 'nicht eingetroffen',
                             'nach_kartenwortlaut': 'eingetroffen' if p3_ok else 'nicht eingetroffen',
                             'p': p, 'unter_rundung': unter, 'D_werte': [[z['La'], z['D']] for z in ls]}
    # beschreibend
    besch = {}
    for v in ('L', 'G'):
        besch[v] = {'steigung_eps': steigung([z['eps'] for z in ko[v]['eps_scan']], [z['D'] for z in ko[v]['eps_scan']]),
                    'p_L': -steigung([z['La'] for z in ko[v]['L_scan']], [z['D'] for z in ko[v]['L_scan']]),
                    'p_L_linear_D1': -steigung([z['La'] for z in ko[v]['linear']], [z['D1'] for z in ko[v]['linear']]),
                    'D1': [[z['La'], z['D1']] for z in ko[v]['linear']], 'dQ_flach_rel': ko[v]['dQ_flach_rel'],
                    'dQ_max_rel': ko[v]['dQ_max_rel'], 'null_D_rel': ko[v]['null']['D_rel'],
                    'newton_rest_max': max(z['newton_rest'] for z in ko[v]['eps_scan'] + ko[v]['L_scan']),
                    'DS_eps': [[z['eps'], z['DS']] for z in ko[v]['eps_scan']]}
    out['beschreibend_kommutator'] = besch
    out['erzeugt_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(out, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('auswertung fertig')


if __name__ == '__main__':
    main()
