#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, Extrapolation fuer Variante A (ohne SM) und B (mit SM_lok, je Untergitter bereinigt), aus quelle2-L*.json.
beta_roh = (R + 1)/2 je Schale; Torus: linear in y = (4 pi/3) r^3/V ueber die L, in denen die Schale unter 0,5 L liegt;
dann beta(r) = beta_inf - c/r^p (p = 2, 3) ueber r_mittel >= 4,5.
"""
import json, sys, math
import numpy as np


def main():
    pfade = sys.argv[1:-1]
    out_pfad = sys.argv[-1]
    out = {}
    for w in ('1.0', '2.0'):
        for var in ('A', 'B'):
            daten = {}
            for p in pfade:
                with open(p) as f:
                    d = json.load(f)
                L, V = d['L'], d['Vtor_lP3']
                for s in d['schalen'][w]:
                    if s['r0'] + float(w) > 0.5 * L:
                        continue
                    S = s['SG'] + s['SF'] + (s['SM_lok'] if var == 'B' else 0.0)
                    R = S / s['QT']
                    y = (4 * math.pi / 3) * s['r_mittel'] ** 3 / V
                    daten.setdefault(s['r0'], []).append((L, s['r_mittel'], y, 0.5 * (R + 1)))
            zeilen = []
            for r0 in sorted(daten):
                pts = daten[r0]
                if len(pts) < 2:
                    continue
                ys = np.array([q[2] for q in pts])
                bs = np.array([q[3] for q in pts])
                X = np.stack([np.ones_like(ys), ys], -1)
                (b0, a), *_ = np.linalg.lstsq(X, bs, rcond=None)
                zeilen.append({'r0': r0, 'r_mittel': float(np.mean([q[1] for q in pts])), 'L': [q[0] for q in pts],
                               'beta_roh_je_L': [float(q[3]) for q in pts], 'beta_extrapoliert': float(b0), 'steigung_y': float(a),
                               'rest_max': float(np.abs(X @ np.array([b0, a]) - bs).max()) if len(pts) > 2 else None})
            sel = [z for z in zeilen if z['r_mittel'] >= 4.5]
            fits = {}
            if len(sel) >= 2:
                r = np.array([z['r_mittel'] for z in sel])
                b = np.array([z['beta_extrapoliert'] for z in sel])
                for pexp in (2, 3):
                    X = np.stack([np.ones_like(r), -1.0 / r ** pexp], -1)
                    (binf, c), *_ = np.linalg.lstsq(X, b, rcond=None)
                    fits['p%d' % pexp] = {'beta_inf': float(binf), 'c': float(c), 'rest_max': float(np.abs(X @ np.array([binf, c]) - b).max())}
                fits['mittel_r_ab_4.5'] = float(b.mean())
                fits['streuung_r_ab_4.5'] = float(b.std())
            out['%s_w%s' % (var, w)] = {'zeilen': zeilen, 'fits': fits}
    with open(out_pfad, 'w') as f:
        json.dump(out, f, indent=1)
    for k, v in out.items():
        print('==', k)
        for z in v['zeilen']:
            print('  r=%5.2f L=%s roh=%s -> %.4f' % (z['r_mittel'], z['L'], ['%.3f' % x for x in z['beta_roh_je_L']], z['beta_extrapoliert']))
        print('  fits:', json.dumps(v['fits']))


if __name__ == '__main__':
    main()
