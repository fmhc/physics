#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, Auswertung der lokalen Probe (nach Sicht geschrieben, liest nur quelle-L*.json).

SM = W^H M lam2 hat auf dem Torus einen gleichmaessigen Anteil (Dilatationsfeld lam2 ~ 1/r^2 mit periodischen Bildern
hat die Divergenz -4 pi c/V): b = mittleres SM je Ecke fuer r >= 0,375 L. SM_lok = SM - n b.
beta je Schale: 2 beta - 1 = R (1 + y) - 4 y, y = (4 pi/3) r^3/V (Kontinuum, gleichfoermiger Hintergrund, fuehrende Ordnung).
Varianten: A ohne SM, B mit SM_lok, C mit vollem SM (roh).
"""
import json, sys, math


def main():
    pfade = sys.argv[1:-1]
    out_pfad = sys.argv[-1]
    out = {}
    for p in pfade:
        with open(p) as f:
            d = json.load(f)
        L, V = d['L'], d['Vtor_lP3']
        for q, z in d['ergebnis'].items():
            sch = z['schalen']
            fern = [s for s in sch if s['r0'] >= 0.375 * L]
            b = sum(s['SM'] for s in fern) / sum(s['n'] for s in fern)
            zeilen = []
            for s in sch:
                y = (4 * math.pi / 3) * s['r_mittel'] ** 3 / V
                QT = s['QT_summe']
                RA = (s['SG'] + s['SF']) / QT
                RB = (s['SG'] + s['SF'] + s['SM'] - s['n'] * b) / QT
                RC = s['S_summe'] / QT
                be = lambda R: 0.5 * (R * (1 + y) - 4 * y + 1)
                zeilen.append({'r_mittel': s['r_mittel'], 'n': s['n'], 'y': y, 'R_A': RA, 'R_B': RB, 'R_C': RC,
                               'beta_A': be(RA), 'beta_B': be(RB), 'beta_C': be(RC), 'beta_A_roh': 0.5 * (RA + 1),
                               'SM_lok_ueber_QT': (s['SM'] - s['n'] * b) / QT})
            out['%s_L%d' % (q, L)] = {'L': L, 'quelle': q, 'b_SM_je_Ecke': b, 'zeilen': zeilen}
    with open(out_pfad, 'w') as f:
        json.dump(out, f, indent=1)
    for k, v in out.items():
        print(k, 'b=%.3e' % v['b_SM_je_Ecke'])
        for z in v['zeilen']:
            print('  r=%5.2f n=%5d  beta_A=%.3f  beta_B=%.3f  beta_C=%.3f  (roh A %.3f, y=%.3f, SMlok/QT=%.3f)' % (
                z['r_mittel'], z['n'], z['beta_A'], z['beta_B'], z['beta_C'], z['beta_A_roh'], z['y'], z['SM_lok_ueber_QT']))


if __name__ == '__main__':
    main()
