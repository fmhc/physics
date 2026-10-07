#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-V-2, Nachtrag-Auswertung (beschreibend, statt jq-Aggregation): Zusammenfassungen je kl und je Gruppe
aus lauf/*.json und nachtrag/nt1-*.json. Importiert uw.py (eingefroren) unveraendert."""
import argparse, json, sys, os
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import uw  # noqa: E402
import tg  # noqa: E402

mm, vert = uw.mm, uw.vert


def lade(p):
    with open(p) as fh:
        return json.load(fh)['ergebnis']


def je_kl(pts):
    o = {}
    for kl in uw.uv.KL_RASTER:
        q = [p for p in pts if p.get('art') == 'kl' and abs(p['kl'] - kl) < 1e-12 and p.get('definiert')]
        o['%g' % kl] = {'n': len(q), 'konvergent': sum(1 for p in q if p['konvergent']),
                        'r12_M': mm([p['r12']['M'] for p in q]), 'r8_M': mm([p['r8']['M'] for p in q]),
                        'p_h_M': mm([p['p_h']['M'] for p in q]),
                        'D0_eig_min_rel_8_10_12': [mm([p['D0'][j]['D0_eig_min_rel'] for p in q]) for j in range(3)],
                        'Meff_absmin_rel_10': mm([p['Meff_absmin_rel'][1] for p in q]),
                        'Meff_eig_min_10': mm([min(p['Meff_eig']) for p in q]),
                        'Meff_eig_max_10': mm([max(p['Meff_eig']) for p in q]),
                        'r_V': mm([p['r_V'] for p in q]), 'C_rest_kappa': mm([p['C_rest_kappa'] for p in q]),
                        'G_rel': mm([p['G_rel'] for p in q]), 'nn_rel': mm([p['nn_rel'] for p in q])}
    return o


def nicht_konv_grund(pts):
    o = {'D0_nicht_pd': 0, 'r12_gross': 0, 'nicht_monoton': 0}
    for p in pts:
        if not p.get('definiert') or p['konvergent']:
            continue
        if not p['D0_pd_alle_h']:
            o['D0_nicht_pd'] += 1
        if p['r12']['M'] > uw.KONV_MAX:
            o['r12_gross'] += 1
        if p['r12']['M'] > max(p['r8']['M'], 1e-10):
            o['nicht_monoton'] += 1
    return o


def b1_info(pts):
    o = {}
    o['schema_undefiniert'] = [{'m': p.get('m'), 'k': p['k'], 'rang_B_s': p['rang_B_s'], 'grund': p.get('grund')}
                               for p in pts if not p.get('definiert')]
    for nm, cond in (('raster', lambda p: p.get('art') == 'kl'), ('bz_innen', lambda p: p.get('art') != 'kl' and not p.get('rand')),
                     ('bz_rand', lambda p: p.get('art') != 'kl' and p.get('rand'))):
        q = [p for p in pts if cond(p) and p.get('definiert')]
        o[nm] = {'n': len(q), 'D0_n_neg_12': vert([p['D0'][2]['D0_n_neg'] for p in q]),
                 'traegheit_10': vert([tuple(p['traegheit'][1]) for p in q]),
                 'traegheit_x0': vert([tuple(p['traegheit_x0']) for p in q]),
                 'a_grund': vert([p['ls']['sp']['a'].get('grund') for p in q if not p['ls']['sp']['a'].get('definiert')]),
                 'a_n_wachsend': vert([p['ls']['sp']['a'].get('n_wachsend') for p in q if p['ls']['sp']['a'].get('definiert')]),
                 'a_w2_min_rel': mm([p['ls']['sp']['a'].get('w2_min_rel') for p in q if p['ls']['sp']['a'].get('definiert')]),
                 'a_w2_im_max_rel': mm([p['ls']['sp']['a'].get('w2_im_max_rel') for p in q if p['ls']['sp']['a'].get('definiert')]),
                 'a_A_red_n_neg': vert([p['ls']['sp']['a'].get('A_red_n_neg') for p in q if p['ls']['sp']['a'].get('definiert')]),
                 'r12_M': mm([p['r12']['M'] for p in q]), 'konvergent': sum(1 for p in q if p['konvergent'])}
    return o


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--l', required=True)
    ap.add_argument('--n', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    v0 = lade(os.path.join(a.l, 'v0.json'))['punkte']
    s = lade(os.path.join(a.l, 's.json'))['punkte']
    b1 = lade(os.path.join(a.l, 'b1.json'))['punkte']
    vn = sum((lade(os.path.join(a.l, 'vneu%d.json' % t))['punkte'] for t in range(3)), [])
    out = {'V_raster_je_kl': je_kl(v0), 'Vneu_R_je_kl': je_kl([p for p in vn if p.get('menge') == 'R']),
           'S_raster_je_kl': je_kl(s), 'B1_raster_je_kl': je_kl(b1),
           'nicht_konvergent_gruende': {'V_raster': nicht_konv_grund(v0), 'Vneu': nicht_konv_grund(vn), 'S': nicht_konv_grund(s),
                                        'B1': nicht_konv_grund(b1)},
           'B1': b1_info(b1),
           'V_alle_Meff_absmin_rel_10': mm([p['Meff_absmin_rel'][1] for p in v0 + vn if p.get('definiert')]),
           'S_bz_Meff_absmin_rel_10': mm([p['Meff_absmin_rel'][1] for p in s if p.get('definiert') and p.get('art') != 'kl']),
           'uw2_V_je_kl_P12': {('%g' % kl): mm([p['uw2']['P12'] for p in v0 if p.get('art') == 'kl' and abs(p['kl'] - kl) < 1e-12
                                                and 'uw2' in p]) for kl in uw.uv.KL_FIT},
           'uw2_V_n_neg10': vert([p['uw2']['n_neg10'] for p in v0 if 'uw2' in p])}
    hs = {}
    for r in ('100', '111', '321'):
        f = os.path.join(a.n, 'nt1-%s.json' % r)
        if os.path.exists(f):
            P = lade(f)['punkte']
            hs[r] = [{x: p.get(x) for x in ('kl', 'eps', 'h_letzt', 'klammer_letzt', 'zensiert_letzt', 'h_erst')} for p in P]
    out['nt1_hstern_klein'] = hs
    tg.schreibe(a.out, {'ergebnis': out})
    print('fertig nachtrag_aw', flush=True)


if __name__ == '__main__':
    main()
