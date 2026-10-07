#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZWEI-KOPIEN-1: mechanische Auswertung nach PLAN.md Abschnitt 3, 4 und 7 (Urteile ZK0 bis ZK2, beschreibende Teile)."""
import argparse, json, os, hashlib, time
import numpy as np

EPS = (1e-3, 2e-3)
KAPPA_HAUPT = (0.01, 0.1, 1.0)
KAPPA_LEITER = (1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0)
DREI = ('1,0,0', '1,1,0', '1,1,1')


def schl(les, kap, eps=None):
    return '%s|%g' % (les, kap) if eps is None else '%s|%g|%g' % (les, kap, eps)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def klassen(z1, z2):
    re1, im1 = np.array(z1['w2_re']), np.array(z1['w2_im'])
    re2, im2 = np.array(z2['w2_re']), np.array(z2['w2_im'])
    tt1, tt2 = np.array(z1['tt']), np.array(z2['tt'])
    w1 = np.array(z1['w1'])
    if len(re1) != len(re2):
        n = len(re1)
        return {'gleiche_dim': False, 'wachs': np.zeros(n, bool), 'massl': np.zeros(n, bool), 'luecke': np.zeros(n, bool),
                'unklar': np.ones(n, bool), 'hel2': np.zeros(n, bool), 're1': re1, 're2': re2[:n] if len(re2) >= n else re1,
                'q': np.full(n, np.nan), 'w1': w1}
    s1 = max(float(np.sqrt(re1 ** 2 + im1 ** 2).max()), 1e-300)
    s2 = max(float(np.sqrt(re2 ** 2 + im2 ** 2).max()), 1e-300)
    wachs = (re1 < -1e-9 * s1) | (np.abs(im1) > 1e-9 * s1) | (re2 < -1e-9 * s2) | (np.abs(im2) > 1e-9 * s2)
    q = re2 / np.where(re1 != 0, re1, 1e-300)
    massl = (~wachs) & (re1 > 1e-9 * s1) & (q >= 3.0) & (q <= 5.0) & (re2 <= 100 * EPS[1] ** 2)
    luecke = (~wachs) & (q >= 0.8) & (q <= 1.25) & (re1 >= 1e-5)
    unklar = ~(wachs | massl | luecke)
    hel2 = (tt1 >= 0.99) & (tt2 >= 0.99)
    return {'gleiche_dim': True, 'wachs': wachs, 'massl': massl, 'luecke': luecke, 'unklar': unklar, 'hel2': hel2,
            're1': re1, 're2': re2, 'q': q, 'w1': w1}


def negnorm(z):
    sa = max(abs(z['eA_min']), abs(z['eA_max']), 1e-300)
    sb = max(abs(z['eB_min']), abs(z['eB_max']), 1e-300)
    return z['eA_min'] < -1e-9 * sa, z['eB_min'] < -1e-9 * sb


def bewerte(res, kap, les, gitter_e):
    """Band und Kennzahlen je Fassung, kappa, Lesart (PLAN Abschnitt 3)."""
    zeilen = []
    massl_vals, w1_vals = [], []
    luecke_hel2, luecke_alle = [], []
    wachs_klein = 0
    aneg_klein = bneg_klein = 0
    for z in res['klein26']:
        z1, z2 = z[schl(les, kap, EPS[0])], z[schl(les, kap, EPS[1])]
        c = klassen(z1, z2)
        for zz in (z1, z2):
            an, bn = negnorm(zz)
            aneg_klein += int(an)
            bneg_klein += int(bn)
        mh = c['massl'] & c['hel2']
        lh = c['luecke'] & c['hel2']
        wachs_klein += int(c['wachs'].sum())
        massl_vals += list(c['re1'][mh] / EPS[0] ** 2)
        w1_vals += list(c['w1'][mh])
        luecke_hel2 += list(c['re1'][lh])
        luecke_alle += list(c['re1'][c['luecke']])
        zeilen.append({'richtung': z['richtung'], 'dim': int(len(c['re1'])), 'gleiche_dim': c['gleiche_dim'],
                       'n0': int(mh.sum()), 'n_luecke_hel2': int(lh.sum()), 'n_luecke': int(c['luecke'].sum()),
                       'n_masselos_andere': int((c['massl'] & ~c['hel2']).sum()), 'n_unklar': int(c['unklar'].sum()),
                       'n_wachsend': int(c['wachs'].sum()),
                       'masselos_hel2_w2k2_eps1': (c['re1'][mh] / EPS[0] ** 2).tolist(),
                       'masselos_hel2_w2k2_eps2': (c['re2'][mh] / EPS[1] ** 2).tolist(),
                       'masselos_andere_w2k2_eps1': (c['re1'][c['massl'] & ~c['hel2']] / EPS[0] ** 2).tolist(),
                       'luecke_w2_eps1': c['re1'][c['luecke']].tolist(),
                       'w1_masselos_hel2': c['w1'][mh].tolist()})
    n0s = [r['n0'] for r in zeilen]
    s = None
    if massl_vals:
        mv = np.array(massl_vals)
        s = float((mv.max() - mv.min()) / mv.mean())
    delta = float(np.sqrt(min(luecke_hel2))) if luecke_hel2 else None
    delta_alle = float(np.sqrt(min(luecke_alle))) if luecke_alle else None
    g_neg = gitter_e['negativ_k'] > 0 or gitter_e['komplex_k'] > 0
    Bd_plan = bool(wachs_klein > 0 or g_neg or gitter_e['A_neg_k'] > 0 or aneg_klein > 0 or gitter_e['B_neg_k'] > 0 or bneg_klein > 0)
    Bd_wort = bool(wachs_klein > 0 or g_neg or gitter_e['A_neg_k'] > 0 or aneg_klein > 0)
    if all(n == 4 for n in n0s):
        nb = 'B-a'
    elif all(n == 2 for n in n0s) and all(r['n_luecke_hel2'] == 2 for r in zeilen) and s is not None and s < 0.05:
        nb = 'B-b'
    elif all(n == 0 for n in n0s):
        nb = 'B-c'
    else:
        nb = 'kein Band'
    komb = bool(w1_vals) and all(0.1 <= w <= 0.9 for w in w1_vals)
    return {'band_plan': 'B-d' if Bd_plan else nb, 'band_wort': 'B-d' if Bd_wort else nb, 'band_ohne_Bd': nb,
            'n0_menge': sorted(set(n0s)), 'n0_je_richtung': {r['richtung']: r['n0'] for r in zeilen},
            'delta': delta, 'delta_alle': delta_alle, 's': s, 'kombination': komb,
            'w1_min': float(min(w1_vals)) if w1_vals else None, 'w1_max': float(max(w1_vals)) if w1_vals else None,
            'wachsend_klein': wachs_klein, 'A_neg_klein': aneg_klein, 'B_neg_klein': bneg_klein,
            'gitter': {k_: gitter_e[k_] for k_ in ('negativ_k', 'komplex_k', 'A_neg_k', 'B_neg_k', 'w2_min_rel', 'positiv_verteilung', 'dim_verteilung', 'gebrochen_verteilung')},
            'konkurrenz': {'masselos_andere_max': max(r['n_masselos_andere'] for r in zeilen),
                           'unklar_max': max(r['n_unklar'] for r in zeilen),
                           'luecke_min_w2': float(min(luecke_alle)) if luecke_alle else None},
            'zeilen': zeilen}


def exponent(werte):
    ks = [k for k, d in werte if d is not None and d > 0]
    if len(ks) < 3:
        return None
    x = np.log([k for k, d in werte])
    y = np.log([d for k, d in werte])
    return float(np.polyfit(x, y, 1)[0])


def zusatz(res, kap, les, fass):
    """PLAN 7: omega^2/k^2 der masselosen TT-Moden in [100], [110], [111], je eps, und Spannen max/min - 1."""
    out = {'richtungen': {}}
    for eps_i, eps in enumerate(EPS):
        pool3, pool26 = [], []
        for z in res['klein26']:
            c = klassen(z[schl(les, kap, EPS[0])], z[schl(les, kap, EPS[1])])
            mh = c['massl'] & c['hel2']
            vals = (c['re1'][mh] / EPS[0] ** 2) if eps_i == 0 else (c['re2'][mh] / EPS[1] ** 2)
            pool26 += list(vals)
            if z['richtung'] in DREI:
                pool3 += list(vals)
                out['richtungen'].setdefault(z['richtung'], {})['eps_%g' % eps] = [float(v) for v in vals]
        out['spanne_drei_eps_%g' % eps] = float(max(pool3) / min(pool3) - 1) if pool3 and min(pool3) > 0 else None
        out['spanne_26_eps_%g' % eps] = float(max(pool26) / min(pool26) - 1) if pool26 and min(pool26) > 0 else None
        out['n_werte_26_eps_%g' % eps] = len(pool26)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    R = {}
    quellen = {}
    for f in ('K2', 'K4', 'K2e'):
        p = os.path.join(a.lauf, 'zk-%s.json' % f)
        with open(p) as fh:
            R[f] = json.load(fh)
        quellen[f] = {'datei': p, 'sha256': sha(p), 'skript_sha256': R[f]['info']['skript_sha256'], 'tp_sha256': R[f]['info']['tp_sha256']}
    out = {'quellen': quellen, 'skript_sha256': sha(os.path.abspath(__file__)), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    # Haupt: Baender je Fassung, kappa, Lesart (Gitter L = 16)
    tab = {}
    for f in ('K2', 'K4', 'K2e'):
        tab[f] = {}
        for kap in (0.0,) + KAPPA_HAUPT:
            for les in (('P',) if kap == 0.0 else ('P', 'R')):
                tab[f][schl(les, kap)] = bewerte(R[f], kap, les, R[f]['gitter'][schl(les, kap)])
        for les in ('P', 'R'):
            tab[f]['p_' + les] = exponent([(kap, tab[f][schl(les, kap)]['delta']) for kap in KAPPA_HAUPT])
    out['tabelle'] = tab
    # Leiter (Gitter L = 8)
    lei = {}
    for f in ('K2', 'K4', 'K2e'):
        lei[f] = {}
        for les in ('P', 'R'):
            reihe = []
            for kap in KAPPA_LEITER:
                b = bewerte(R[f], kap, les, R[f]['leiter_gitter'][schl(les, kap)])
                reihe.append({'kappa': kap, 'band_plan': b['band_plan'], 'band_wort': b['band_wort'], 'n0_menge': b['n0_menge'],
                              'delta': b['delta'], 's': b['s'], 'w2_min_rel_gitter': b['gitter']['w2_min_rel'],
                              'negativ_k': b['gitter']['negativ_k'], 'komplex_k': b['gitter']['komplex_k'],
                              'A_neg_k': b['gitter']['A_neg_k'], 'B_neg_k': b['gitter']['B_neg_k'],
                              'masselos_andere_max': b['konkurrenz']['masselos_andere_max']})
            kc = [r['kappa'] for r in reihe if r['band_plan'] == 'B-d']
            lei[f][les] = {'reihe': reihe, 'kappa_c_plan': min(kc) if kc else None,
                           'kappa_c_wort': min([r['kappa'] for r in reihe if r['band_wort'] == 'B-d'], default=None)}
    out['leiter'] = lei
    # ZK0 (aus dem K2-Lauf; kappa = 0 in allen drei Laeufen gleich?)
    z0 = R['K2']['zk0_ref']
    b0 = tab['K2'][schl('P', 0.0)]
    gleich = all(R[f]['klein26'][i][schl('P', 0.0, e)]['w2_re'] == R['K2']['klein26'][i][schl('P', 0.0, e)]['w2_re']
                 for f in ('K4', 'K2e') for i in range(26) for e in EPS)
    zk0_plan = bool(b0['n0_menge'] == [4] and z0['max_abw_w2_ueber_k2'] <= 1e-8 and z0['gitter_positiv_gleich_alle'])
    zk0_wort = bool(b0['n0_menge'] == [4] and z0['max_abw_v'] <= 1e-8)
    # ZK1, ZK2
    b2 = [tab['K2'][schl('P', k)] for k in KAPPA_HAUPT]
    b4 = [tab['K4'][schl('P', k)] for k in KAPPA_HAUPT]
    zk1_plan = all(b['band_plan'] == 'B-b' for b in b2)
    zk1_wort = all(b['band_wort'] == 'B-b' and b['kombination'] for b in b2)
    zk2_plan = all(b['band_plan'] == 'B-a' for b in b4)
    zk2_wort = all(b['band_wort'] == 'B-a' for b in b4)
    out['urteile'] = {
        'ZK0': {'plan': zk0_plan, 'wort': zk0_wort, 'n0_menge': b0['n0_menge'], 'max_abw_w2k2': z0['max_abw_w2_ueber_k2'],
                'max_abw_v': z0['max_abw_v'], 'gitter_gleich': z0['gitter_positiv_gleich_alle'],
                'gitter_abweichungen': z0['gitter_abweichungen'], 'gitter_alt': z0['gitter_alt_verteilung'],
                'gitter_neu': z0['gitter_neu_verteilung'], 'kappa0_in_allen_laeufen_gleich': gleich,
                's_kappa0': b0['s']},
        'ZK1': {'plan': zk1_plan, 'wort': zk1_wort,
                'baender_plan': {('%g' % k): b['band_plan'] for k, b in zip(KAPPA_HAUPT, b2)},
                'baender_wort': {('%g' % k): b['band_wort'] for k, b in zip(KAPPA_HAUPT, b2)},
                'kombination': {('%g' % k): b['kombination'] for k, b in zip(KAPPA_HAUPT, b2)}},
        'ZK2': {'plan': zk2_plan, 'wort': zk2_wort,
                'baender_plan': {('%g' % k): b['band_plan'] for k, b in zip(KAPPA_HAUPT, b4)},
                'baender_wort': {('%g' % k): b['band_wort'] for k, b in zip(KAPPA_HAUPT, b4)}}}
    # Zusatz Leitung (PLAN 7), beschreibend
    zs = {}
    for f in ('K2', 'K4', 'K2e'):
        zs[f] = {}
        for kap in (0.0,) + KAPPA_HAUPT:
            for les in (('P',) if kap == 0.0 else ('P', 'R')):
                zs[f][schl(les, kap)] = zusatz(R[f], kap, les, f)
    out['zusatz_isotropie'] = zs
    out['kontrollen'] = {f: R[f]['kontrolle'] for f in R}
    out['laufzeiten_s'] = {f: R[f]['laufzeit_s'] for f in R}
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1, default=lambda x: x.item() if hasattr(x, 'item') else str(x))
    os.replace(a.out + '.tmp', a.out)
    print('fertig auswertung %.1f s' % (time.time() - t0), flush=True)


if __name__ == '__main__':
    main()
