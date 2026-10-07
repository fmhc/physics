#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, Extrapolation (nach Sicht geschrieben, liest nur quelle-L*.json).

Variante A (Lapse-Quelle ohne Eichprojektion): beta_roh(L, r) = (R_A + 1)/2 je Schale [r0, r0 + 1).
Torus: beta_roh = beta(r) + a(r) y, y = (4 pi/3) r^3/V (fuehrende Ordnung ~ 1/V); lineare Ausgleichsgerade in y ueber
alle L, in denen die Schale vollstaendig unter 0,5 L liegt (mindestens zwei L). Dann beta(r) = beta_inf - c/r^3 ueber
die Schalen mit r_mittel >= 4,5 (und, getrennt, freier Exponent ueber drei Stuetzwerte nicht: nur Ausgabe).
"""
import json, sys, math
import numpy as np


def main():
    pfade = sys.argv[1:-1]
    out_pfad = sys.argv[-1]
    daten = {}
    for p in pfade:
        with open(p) as f:
            d = json.load(f)
        L, V = d['L'], d['Vtor_lP3']
        for q, z in d['ergebnis'].items():
            for s in z['schalen']:
                if s['r0'] + 1.0 > 0.5 * L:
                    continue
                RA = (s['SG'] + s['SF']) / s['QT_summe']
                y = (4 * math.pi / 3) * s['r_mittel'] ** 3 / V
                daten.setdefault(q, {}).setdefault(s['r0'], []).append((L, s['r_mittel'], y, 0.5 * (RA + 1)))
    out = {}
    for q, sch in daten.items():
        zeilen = []
        for r0 in sorted(sch):
            pts = sch[r0]
            if len(pts) < 2:
                continue
            ys = np.array([p[2] for p in pts])
            bs = np.array([p[3] for p in pts])
            X = np.stack([np.ones_like(ys), ys], -1)
            (b0, a), *_ = np.linalg.lstsq(X, bs, rcond=None)
            rest = float(np.abs(X @ np.array([b0, a]) - bs).max()) if len(pts) > 2 else None
            zeilen.append({'r0': r0, 'r_mittel': float(np.mean([p[1] for p in pts])), 'L': [p[0] for p in pts],
                           'beta_roh_je_L': [float(p[3]) for p in pts], 'y_je_L': [float(p[2]) for p in pts],
                           'beta_extrapoliert': float(b0), 'steigung_y': float(a), 'rest_max': rest})
        sel = [z for z in zeilen if z['r_mittel'] >= 4.5]
        fit = None
        if len(sel) >= 2:
            r = np.array([z['r_mittel'] for z in sel])
            b = np.array([z['beta_extrapoliert'] for z in sel])
            X = np.stack([np.ones_like(r), -1.0 / r ** 3], -1)
            (binf, c), *_ = np.linalg.lstsq(X, b, rcond=None)
            X2 = np.stack([np.ones_like(r), -1.0 / r ** 2], -1)
            (binf2, c2), *_ = np.linalg.lstsq(X2, b, rcond=None)
            fit = {'shells': [float(x) for x in r], 'beta_inf_1r3': float(binf), 'c_1r3': float(c),
                   'rest_1r3_max': float(np.abs(X @ np.array([binf, c]) - b).max()),
                   'beta_inf_1r2': float(binf2), 'c_1r2': float(c2), 'rest_1r2_max': float(np.abs(X2 @ np.array([binf2, c2]) - b).max())}
        out[q] = {'zeilen': zeilen, 'fit_r': fit}
    with open(out_pfad, 'w') as f:
        json.dump(out, f, indent=1)
    for q, v in out.items():
        print('==', q)
        for z in v['zeilen']:
            print('  r=%5.2f L=%s beta_roh=%s -> beta(L->inf)=%.4f (Steigung %.3f, Rest %s)' % (
                z['r_mittel'], z['L'], ['%.4f' % x for x in z['beta_roh_je_L']], z['beta_extrapoliert'], z['steigung_y'],
                ('%.4f' % z['rest_max']) if z['rest_max'] is not None else '-'))
        print('  fit:', json.dumps(v['fit_r']))


if __name__ == '__main__':
    main()
