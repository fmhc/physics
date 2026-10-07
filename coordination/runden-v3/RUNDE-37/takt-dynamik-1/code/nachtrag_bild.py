#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TAKT-DYNAMIK-1, Nachtrag nach dem Einfrieren (nur Darstellung): lesbareres Bild aus lauf/td-*.json.
Energie in Prozent (Arm c abgeschnitten, Abbruch markiert), Zuege je Periode, TT-Amplitude (Projektion auf die Mode)."""
import json, glob, os, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ordner, pfad = sys.argv[1], sys.argv[2]
D = {}
for p in sorted(glob.glob(os.path.join(ordner, 'td-*.json'))):
    if p.endswith('zustand.json'):
        continue
    d = json.load(open(p))
    if 'ergebnis' in d:
        e = d['ergebnis']
        D[(e['netz'], e['A'], e['arm'], e['lesart'], e['h'])] = e
farbe = {'a': '#1f77b4', 'b': '#d62728', 'c': '#2ca02c'}
stil = {1: '-', 2: '--', 3: ':', 4: '-.'}
fig, ax = plt.subplots(2, 3, figsize=(19, 10))
for row, A in enumerate((1e-3, 1e-2)):
    for s in (1, 2, 3, 4):
        for arm in ('a', 'b', 'c'):
            e = D.get(('glas-N128-s%d' % s, A, arm, 'R', 0.5))
            if e is None:
                continue
            P = np.array(e['proben'])
            t = P[:, 0] / e['T']
            y = 100 * (P[:, 1] - e['H0']) / e['H0']
            ax[row, 0].plot(t, np.clip(y, -60, 60), stil[s], color=farbe[arm], lw=1.0,
                            label=('Arm %s' % arm) if s == 1 else None)
            if e.get('abbruch'):
                ax[row, 0].axvline(e['abbruch']['t'] / e['T'], color=farbe[arm], ls=stil[s], lw=0.6)
            if arm in ('b', 'c'):
                ev = [x['t'] / e['T'] for x in e['ereignisse'] if x.get('ausgefuehrt')]
                h, _ = np.histogram(ev, bins=np.arange(0, 11))
                ax[row, 1].step(np.arange(0, 10) + 0.5, h, stil[s], where='mid', color=farbe[arm],
                                label=('Arm %s, Saat %d' % (arm, s)))
    for arm in ('a', 'b', 'c'):
        e = D.get(('glas-N128-s2', A, arm, 'R', 0.5))
        if e is None:
            continue
        P = np.array(e['proben'])
        r = np.array(e['mode']['tt_richtung'])
        ax[row, 2].plot(P[:, 0] / e['T'], np.clip((P[:, 4:8] @ r) / A, -2, 2), color=farbe[arm], lw=0.7, label='Arm %s' % arm)
    ax[row, 0].set_title('Energie (H - H0)/H0 in %%, A = %g (Glas N = 128, Saat 1 -, 2 --, 3 :, 4 -.; c bei +-60 %% abgeschnitten, senkrecht = Abbruch)' % A, fontsize=8)
    ax[row, 0].set_ylim(-62, 62)
    ax[row, 1].set_title('Ausgefuehrte Zuege je Periode, A = %g' % A, fontsize=9)
    ax[row, 2].set_title('TT-Lesung (Projektion auf die Mode) / A, Saat 2, A = %g (bei +-2 abgeschnitten)' % A, fontsize=9)
    for c in range(3):
        ax[row, c].set_xlabel('t / T')
        ax[row, c].legend(fontsize=7, ncol=2)
fig.suptitle('TAKT-DYNAMIK-1: Arm a feste Zerlegung, b Delaunay-Zuege, c gleich viele Zufallszuege (synthetische Gitterrechnung, keine Messdaten)')
fig.tight_layout()
fig.savefig(pfad + '.tmp.png', dpi=100)
os.replace(pfad + '.tmp.png', pfad)
print('fertig nachtrag_bild', flush=True)
