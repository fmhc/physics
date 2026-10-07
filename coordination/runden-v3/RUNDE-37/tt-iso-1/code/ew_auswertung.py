#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EINE-WELT-LOCH-1: mechanische Auswertung nach PLAN.md Abschnitt 3 (Urteile EW0 bis EW3, nach Plan und Kartenwortlaut)."""
import argparse, json, os, hashlib, time
import numpy as np

EPS = (1e-3, 2e-3)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def klassen(z, eps):
    re = np.array(z['w2_re'])
    im = np.array(z['w2_im'])
    tt = np.array(z['tt_anteil'])
    s = float(np.sqrt(re ** 2 + im ** 2).max())
    betrag = np.sqrt(re ** 2 + im ** 2)
    wachs = (re < -1e-9 * s) | (np.abs(im) > 1e-9 * s)
    massl = (~wachs) & (betrag <= 1e3 * eps ** 2)
    luecke = (~wachs) & (re >= 1e-4 * s) & (re >= 2e3 * eps ** 2)
    unklar = ~(wachs | massl | luecke)
    tt_pos = massl & (re > 1e-9 * s) & (tt >= 0.99)
    return {'s': s, 'wachs': wachs, 'massl': massl, 'luecke': luecke, 'unklar': unklar, 'tt_pos': tt_pos,
            're': re, 'im': im, 'tt': tt, 'neg_re': re < -1e-9 * s, 'fit_rest': np.array(z['fit_rest'])}


def bewerte(klein):
    punkte = []
    for z in klein:
        k1, k2 = klassen(z['eps_0.001'], EPS[0]), klassen(z['eps_0.002'], EPS[1])
        m1 = np.sort(k1['re'][k1['massl']])
        m2 = np.sort(k2['re'][k2['massl']])
        if len(m1) == len(m2) and len(m1) > 0:
            lin = np.abs(m2 / (4 * m1) - 1.0)
            lin_ok_je = lin <= 0.01
        else:
            lin = np.array([np.inf])
            lin_ok_je = np.zeros(len(m1), bool)
        # masselose TT-Mode: positiv, TT >= 0.99, linear (Linearitaet gilt fuer die Menge der masselosen Moden je Richtung)
        lin_alle = bool(len(m1) == len(m2) and np.all(lin_ok_je))
        # Luecke eps-unabhaengig: kleinster Luecke-Wert bei 2e-3 geteilt durch den bei 1e-3 in [0,5; 2]
        if k1['luecke'].any() and k2['luecke'].any():
            lq = float(k2['re'][k2['luecke']].min() / k1['re'][k1['luecke']].min())
        else:
            lq = None
        luecke_konst = lq is not None and 0.5 <= lq <= 2.0
        for eps, kk in ((EPS[0], k1), (EPS[1], k2)):
            n_tt = int(kk['tt_pos'].sum()) if lin_alle else 0
            punkte.append({'richtung': z['richtung'], 'eps': eps, 'dim': int(len(kk['re'])),
                           'n_wachsend': int(kk['wachs'].sum()), 'n_neg_re': int(kk['neg_re'].sum()),
                           'n_masselos': int(kk['massl'].sum()), 'n_masselos_tt': n_tt, 'n_luecke': int(kk['luecke'].sum()),
                           'n_unklar': int(kk['unklar'].sum()),
                           'masselos_w2_ueber_k2': (kk['re'][kk['massl']] / eps ** 2).tolist(),
                           'masselos_tt': kk['tt'][kk['massl']].tolist(),
                           'masselos_fit_rest': kk['fit_rest'][kk['massl']].tolist(),
                           'luecke_min_re': float(kk['re'][kk['luecke']].min()) if kk['luecke'].any() else None,
                           'luecke_min_rel': float(kk['re'][kk['luecke']].min() / kk['s']) if kk['luecke'].any() else None,
                           'kleinstes_re': float(kk['re'].min()), 'max_im_rel': float(np.abs(kk['im']).max() / kk['s']),
                           'unklar_re': kk['re'][kk['unklar']].tolist(), 'wachsend_re': kk['re'][kk['wachs']].tolist(),
                           'wachsend_im': kk['im'][kk['wachs']].tolist(), 's': kk['s'],
                           'linear_abw': [float(x) for x in np.atleast_1d(lin)], 'linear_alle': lin_alle,
                           'luecke_quotient_2e3_1e3': lq, 'luecke_konstant': luecke_konst})
    return punkte


def urteile_netz(punkte):
    ew1 = all(p['n_wachsend'] == 0 and p['n_unklar'] == 0 and p['n_masselos'] == 2 and p['n_masselos_tt'] == 2 and
              p['n_luecke'] == p['dim'] - 2 and p['luecke_konstant'] for p in punkte)
    ew2 = all(p['n_masselos_tt'] == 4 for p in punkte)
    ew3_plan = any(p['n_wachsend'] > 0 for p in punkte)
    ew3_karte = any(p['n_neg_re'] > 0 for p in punkte)
    tempo = [x for p in punkte if p['eps'] == EPS[0] for x in p['masselos_w2_ueber_k2']]
    kz = {'punkte': len(punkte),
          'n_masselos_verteilung': dict(sorted({str(v): sum(1 for p in punkte if p['n_masselos'] == v) for v in set(p['n_masselos'] for p in punkte)}.items())),
          'n_masselos_tt_verteilung': dict(sorted({str(v): sum(1 for p in punkte if p['n_masselos_tt'] == v) for v in set(p['n_masselos_tt'] for p in punkte)}.items())),
          'punkte_mit_wachsend': sum(1 for p in punkte if p['n_wachsend'] > 0),
          'punkte_mit_neg_re': sum(1 for p in punkte if p['n_neg_re'] > 0),
          'punkte_mit_unklar': sum(1 for p in punkte if p['n_unklar'] > 0),
          'max_wachsend_je_punkt': max(p['n_wachsend'] for p in punkte),
          'max_neg_re_je_punkt': max(p['n_neg_re'] for p in punkte),
          'kleinstes_re_min': min(p['kleinstes_re'] for p in punkte),
          'max_im_rel': max(p['max_im_rel'] for p in punkte),
          'tt_min_masselos': min([x for p in punkte for x in p['masselos_tt']], default=None),
          'fit_rest_max_masselos': max([x for p in punkte for x in p['masselos_fit_rest']], default=None),
          'linear_abw_max': max(max(p['linear_abw']) for p in punkte),
          'masselos_w2_ueber_k2_min': min(tempo, default=None), 'masselos_w2_ueber_k2_max': max(tempo, default=None),
          'tempo_spanne_rel': (max(tempo) - min(tempo)) / np.mean(tempo) if tempo else None,
          'luecke_min_re': min([p['luecke_min_re'] for p in punkte if p['luecke_min_re'] is not None], default=None),
          'luecke_min_rel': min([p['luecke_min_rel'] for p in punkte if p['luecke_min_rel'] is not None], default=None),
          'luecke_quotient_min': min([p['luecke_quotient_2e3_1e3'] for p in punkte if p['luecke_quotient_2e3_1e3'] is not None], default=None),
          'luecke_quotient_max': max([p['luecke_quotient_2e3_1e3'] for p in punkte if p['luecke_quotient_2e3_1e3'] is not None], default=None),
          'punkte_luecke_nicht_konstant': sum(1 for p in punkte if not p['luecke_konstant'])}
    return ew1, ew2, ew3_plan, ew3_karte, kz


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    res = {'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'skript_sha256': sha(os.path.abspath(__file__))}
    eing = {}
    for fn in sorted(os.listdir(a.lauf)):
        if fn.endswith('.json') and fn != os.path.basename(a.out):
            with open(os.path.join(a.lauf, fn)) as f:
                try:
                    eing[fn] = json.load(f).get('info', {}).get('skript_sha256')
                except Exception:
                    eing[fn] = None
    res['eingaben_skript_sha256'] = eing
    urteile = {}
    # ---------------- EW0
    with open(os.path.join(a.lauf, 'kontrolle.json')) as f:
        KO = json.load(f)['kontrolle']
    ok0 = bool(KO['modenzahl_gleich_alle']) and KO['tempo_abw_max'] <= 1e-8
    w0 = 'eingetroffen' if ok0 else 'nicht eingetroffen'
    urteile['EW0'] = {'nach_plan': w0, 'nach_kartenwortlaut': w0,
                      'kennzahlen': {'modenzahl_gleich_alle_4095': KO['modenzahl_gleich_alle'],
                                     'modenzahl_abweichungen': KO['modenzahl_abweichungen'],
                                     'modenzahl_verteilung_alt': KO['modenzahl_alt_verteilung'],
                                     'modenzahl_verteilung_neu': KO['modenzahl_neu_verteilung'],
                                     'tempo_abw_max': KO['tempo_abw_max'], 'gegenprobe_tp': KO['gegenprobe_tp']}}
    # ---------------- EW1 bis EW3 (V), S beschreibend
    netze = {}
    for f_ in ('V', 'S'):
        fn = os.path.join(a.lauf, 'spektrum-%s.json' % f_)
        if not os.path.exists(fn):
            continue
        with open(fn) as f:
            SP = json.load(f)['spektrum']
        punkte = bewerte(SP['klein_k'])
        ew1, ew2, ew3p, ew3k, kz = urteile_netz(punkte)
        netze[f_] = {'ew1': ew1, 'ew2': ew2, 'ew3_plan': ew3p, 'ew3_karte': ew3k, 'kennzahlen': kz, 'punkte': punkte,
                     'gitter': {k: v for k, v in SP.get('gitter', {}).items() if k not in ('m_je_k', 'positiv_je_k')}}
    if 'V' in netze:
        n = netze['V']
        w = lambda b: 'eingetroffen' if b else 'nicht eingetroffen'
        urteile['EW1'] = {'nach_plan': w(n['ew1']), 'nach_kartenwortlaut': w(n['ew1']), 'kennzahlen': n['kennzahlen']}
        urteile['EW2'] = {'nach_plan': w(n['ew2']), 'nach_kartenwortlaut': w(n['ew2']),
                          'kennzahlen': {'n_masselos_tt_verteilung': n['kennzahlen']['n_masselos_tt_verteilung']}}
        urteile['EW3'] = {'nach_plan': w(n['ew3_plan']), 'nach_kartenwortlaut': w(n['ew3_karte']),
                          'kennzahlen': {'punkte_mit_wachsend': n['kennzahlen']['punkte_mit_wachsend'],
                                         'punkte_mit_neg_re': n['kennzahlen']['punkte_mit_neg_re'],
                                         'kleinstes_re_min': n['kennzahlen']['kleinstes_re_min'],
                                         'max_im_rel': n['kennzahlen']['max_im_rel']}}
    else:
        for k_ in ('EW1', 'EW2', 'EW3'):
            urteile[k_] = {'nach_plan': 'nicht entscheidbar', 'nach_kartenwortlaut': 'nicht entscheidbar'}
    if 'S' in netze:
        n = netze['S']
        res['variante_S_beschreibend'] = {'wie_EW1': n['ew1'], 'wie_EW2': n['ew2'], 'wie_EW3_plan': n['ew3_plan'],
                                          'wie_EW3_karte': n['ew3_karte'], 'kennzahlen': n['kennzahlen']}
    res['netze'] = netze
    with open(os.path.join(a.lauf, 'zaehlung.json')) as f:
        res['zaehlung'] = json.load(f)['zaehlung']
    res['kontrolle_ohne_fuellung'] = {k: v for k, v in KO.items() if k != 'tempo_zeilen'}
    res['urteile'] = urteile
    res['laufzeit_s'] = time.time() - t0
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig auswertung', {k: (v['nach_plan'], v['nach_kartenwortlaut']) for k, v in urteile.items()}, flush=True)


if __name__ == '__main__':
    main()
