#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-KH-1, Nachtrag 4 (beschreibend): Zusammenfassungen aus lauf/ und nachtrag/ (statt jq-Aggregation)."""
import argparse, json, sys, os
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import tg  # noqa: E402


def lade(p):
    with open(p) as fh:
        return json.load(fh)['ergebnis']


def mm(xs):
    xs = [x for x in xs if x is not None]
    return [float(min(xs)), float(max(xs))] if xs else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--nachtrag', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    ras = lade(os.path.join(a.lauf, 'raster.json'))['punkte']
    bz = lade(os.path.join(a.lauf, 'bz0.json'))['punkte'] + lade(os.path.join(a.lauf, 'bz1.json'))['punkte']
    nt = lade(os.path.join(a.nachtrag, 'nt2.json'))
    out = {}
    nr, nb = nt['raster'], nt['bz']
    g1 = [p for p in nb if p['n_null'] == 1]
    sp = [p for p in nb if p['n_null'] != 1]
    out['nt2_generisch_bz'] = {'anzahl': len(g1), 'pass_MC': mm([p['pass_ohne_inv_MC'] for p in g1]),
                               'uC': mm([p['uC_rel'] for p in g1]), 'uX': mm([p['uX_rel'] for p in g1]),
                               'X_in_MeffM': mm([p['X_in_MeffM'] for p in g1]),
                               'pass_Kc': mm([p['pass_ohne_inv_Kc'] for p in g1]),
                               'u_111': mm([p['u_111_anteil'] for p in g1]), 'Vuu_rel': mm([p['Vuu_rel'] for p in g1])}
    out['nt2_raster'] = {'anzahl': len(nr), 'n_null': sorted(set(p['n_null'] for p in nr)),
                         'pass_MC': mm([p['pass_ohne_inv_MC'] for p in nr]), 'uC': mm([p['uC_rel'] for p in nr]),
                         'uX': mm([p['uX_rel'] for p in nr]), 'X_in_MeffM': mm([p['X_in_MeffM'] for p in nr]),
                         'pass_Kc': mm([p['pass_ohne_inv_Kc'] for p in nr]),
                         'pass_reduziert': mm([p.get('pass_reduziert') for p in nr]),
                         'pass_Kc_je_richtung_kl0005': {p['richtung']: p['pass_ohne_inv_Kc'] for p in nr if p['kl'] == 0.005}}
    ki_pi = [p for p in sp if any(int(m) == 4 for m in p['m'])]
    out['nt2_sonderpunkte'] = {'anzahl': len(sp), 'davon_mit_k_i_gleich_pi': len(ki_pi),
                               'n_null': sorted(set(p['n_null'] for p in sp)), 'uM': mm([p['uM_rel'] for p in sp]),
                               'Vuu_kond_min': float(min(p.get('Vuu_kond', np.inf) for p in sp))}
    # Paarung b (A2L R1): Lage der wachsenden BZ-Punkte
    wb = [p['m'] for p in bz if p['sp']['b'].get('n_neg', 0) > 0]
    out['b_wachsend_bz'] = {'anzahl': len(wb), 'summe_m_mod8_gleich_4': int(sum(1 for m in wb if sum(m) % 8 == 4)),
                            'summe_m_mod8_verteilung': {str(r): int(sum(1 for m in wb if sum(m) % 8 == r)) for r in range(8)},
                            'alle_mit_summe_mod8_4_im_gitter': int(sum(1 for p in bz if sum(p['m']) % 8 == 4))}
    wc_r = [(p['richtung'], p['kl']) for p in ras if p['sp']['c'].get('n_neg', 0) > 0]
    uc_r = sorted(set(p['richtung'] for p in ras if not p['sp']['c'].get('definiert', True)))
    out['c_raster'] = {'wachsend_k': len(wc_r), 'richtungen_wachsend': sorted(set(r for r, k in wc_r)),
                       'nicht_definiert_richtungen': uc_r}
    out['sonder_adm'] = {'nicht_adm_bz': int(sum(1 for p in bz if not p['adm'])),
                         'nicht_adm_mit_k_i_pi': int(sum(1 for p in bz if not p['adm'] and any(int(round(x / (np.pi / 4))) == 4 for x in p['k']))),
                         'nicht_adm_raster': int(sum(1 for p in ras if not p['adm']))}
    out['R_S_rest_raster'] = mm([p['R_S_rest'] for p in ras])
    out['R_S_bb_raster'] = mm([p['R_S_bb'] for p in ras])
    tg.schreibe(a.out, {'ergebnis': out})
    print('fertig nachtrag_aw', flush=True)


if __name__ == '__main__':
    main()
