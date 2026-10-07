#!/usr/bin/env python3
"""RAUTE-ATEM-1, Auswertung der VARIANTE [Zusatz Leitung] (C und D mit halber Atemamplitude). Beschreibend; Regeln
wie PLAN.md Abschn. 5 (Plan-Fassung), festgelegt in PLAN-NACHTRAG.md vor dem Variantenlauf. Nutzt die eingefrorenen
Funktionen aus auswertung.py unveraendert.
Aufruf: auswertung_var.py --lauf <ordner> --aus <json>"""
import argparse
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auswertung as A  # noqa: E402

SAATEN = (1, 2, 3, 4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--aus', required=True)
    a = ap.parse_args()
    out = {'fehlend': [], 'laeufe': {}, 'urteile_beschreibend': {}, 'vermerke': {}}

    def lade(name):
        p = os.path.join(a.lauf, name)
        if not os.path.exists(p):
            out['fehlend'].append(name)
            return None
        with open(p) as f:
            return json.load(f)

    h3, k = {}, {}
    for B in A.B_WERTE:
        js = lade(f'haupt_d3_B{B:.2f}.json')
        if js:
            for r in js['laeufe']:
                h3[(B, r['seed'])] = A.lauf_metriken(r)
    js = lade('haupt_d2_B0.05.json')
    h2 = {r['seed']: A.lauf_metriken(r) for r in js['laeufe']} if js else {}
    for dim in (3, 2):
        js = lade(f'kontrolle_d{dim}.json')
        if js:
            for r in js['laeufe']:
                k[(dim, r['seed'])] = A.lauf_metriken(r)
    for kk, v in h3.items():
        out['laeufe'][f'var_haupt_d3_B{kk[0]:.2f}_s{kk[1]}'] = v
    for s, v in h2.items():
        out['laeufe'][f'var_haupt_d2_B0.05_s{s}'] = v
    for kk, v in k.items():
        out['laeufe'][f'var_kontrolle_d{kk[0]}_s{kk[1]}'] = v
    voll = len(h3) == 12 and len(k) == 8 and len(h2) == 4

    def phasen_ok(m):
        dp = m['dphi_ende']
        return all(abs(abs(dp[n]) - 2 * math.pi / 3) < 0.1 for n in A.NAMEN[:5]) and abs(dp['CD']) < 0.1

    alle = list(h3.values()) + list(h2.values()) + list(k.values())
    werk = all(A.werkzeug_ok(m['werkzeugprobe']) for m in alle) and len(alle) > 0
    ph = all(phasen_ok(m) for m in k.values()) and len(k) == 8
    falt = all(k[(3, s)]['max_dtheta_200_grad'] < 5.0 for s in SAATEN if (3, s) in k)
    out['vermerke']['V_RA0_teile'] = {'phasen_2d_3d': ph, 'kein_falten': falt, 'werkzeugprobe': werk}
    zu200 = {kk: (v['t_erstes_schliessen'] is not None and v['t_erstes_schliessen'] <= 200.0 + 1e-9)
             for kk, v in h3.items()}
    ra2p = {B: sum(h3[(B, s)]['RA2_lauf_plan'] for s in SAATEN if (B, s) in h3) for B in A.B_WERTE}
    ra2k = {B: sum(h3[(B, s)]['RA2_lauf_karte'] for s in SAATEN if (B, s) in h3) for B in A.B_WERTE}
    ausw = [v for v in h3.values() if v['fp_lauf'] is not None]
    n_ja = sum(v['fp_lauf'] for v in ausw)
    if not voll:
        out['urteile_beschreibend'] = {'V-RA0': 'nicht auswertbar', 'V-RA1': 'nicht auswertbar',
                                       'V-RA2': 'nicht auswertbar', 'V-FP': 'nicht auswertbar'}
    else:
        out['urteile_beschreibend']['V-RA0'] = 'eingetroffen' if (ph and falt and werk) else 'nicht eingetroffen'
        out['urteile_beschreibend']['V-RA1'] = 'eingetroffen' if all(zu200.values()) else 'nicht eingetroffen'
        out['urteile_beschreibend']['V-RA2 (Plan)'] = ('eingetroffen' if any(n >= 3 for n in ra2p.values())
                                                       else 'nicht eingetroffen')
        out['urteile_beschreibend']['V-RA2 (Karte)'] = ('eingetroffen' if any(n >= 3 for n in ra2k.values())
                                                        else 'nicht eingetroffen')
        out['urteile_beschreibend']['V-FP (Plan)'] = ('nicht auswertbar' if len(ausw) < 8 else
                                                      ('eingetroffen' if n_ja >= 0.75 * len(ausw)
                                                       else 'nicht eingetroffen'))
    out['vermerke']['V_RA1_je_B'] = {f'{B:.2f}': sum(zu200.get((B, s), False) for s in SAATEN) for B in A.B_WERTE}
    out['vermerke']['V_RA2_je_B'] = {f'{B:.2f}': {'plan': ra2p[B], 'karte': ra2k[B]} for B in A.B_WERTE}
    out['vermerke']['V_FP'] = {'auswertbar': len(ausw), 'ja': n_ja}
    if ausw:
        gew = np.array([v['fp_dauer_takte'] for v in ausw])
        M = np.array([[v['stab_mittel'][n] / v['B'] for n in A.NAMEN] for v in ausw])
        Mp = (gew[:, None] * M).sum(axis=0) / gew.sum()
        cdp = float((gew * np.array([v['cd_anteil_gebunden'] for v in ausw])).sum() / gew.sum())
        out['urteile_beschreibend']['V-FP (Karte, gepoolt)'] = ('eingetroffen' if A.fp_regel(Mp, cdp >= 0.5)
                                                                else 'nicht eingetroffen')
        out['vermerke']['V_FP_gepoolt_durch_B'] = {'stab_mittel_durch_B': dict(zip(A.NAMEN, Mp.tolist())),
                                                   'cd_anteil_gebunden': cdp}
    with open(a.aus, 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out['urteile_beschreibend'], indent=1))
    print(json.dumps(out['vermerke'], indent=1))


if __name__ == '__main__':
    main()
