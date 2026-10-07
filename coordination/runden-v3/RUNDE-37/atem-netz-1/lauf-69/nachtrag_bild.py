#!/usr/bin/env python3
"""ATEM-NETZ-1, Nachtrag 1: Bild der feinen Einfrier-Abtastung (N1_fein.json) [Zusatz Leitung, beschreibend].
Aufruf (.69, kleintest.sh): nachtrag_bild.py <lauf-ordner>
"""
import json
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = sys.argv[1]
with open(os.path.join(D, 'N1_fein.json')) as fh:
    n1 = json.load(fh)
fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
for name, lab, col in (('pyro', 'Pyrochlor (z = 6, frustriert)', 'C0'), ('kubisch', 'einfach-kubisch (z = 6, zweifaerbbar)', 'C2'),
                       ('diamant', 'Diamant (z = 4, zweifaerbbar)', 'C1')):
    r = n1[name]['res']
    k = [x['kappa'] for x in r]
    ax[0].plot(k, [x['gefroren'] for x in r], 'o-', color=col, ms=3, label=lab)
    ax[1].plot(k, [x['v_mittel'] for x in r], 'o-', color=col, ms=3, label=lab)
for kk, col in ((0.0335, 'C0'), (0.0347, 'C2'), (0.0521, 'C1'), (0.0283, 'grey'), (0.0424, 'grey')):
    ax[0].axvline(kk, color=col, lw=0.7, ls=':')
ax[0].axhline(0.5, color='grey', lw=0.5)
ax[0].set_xlabel('kappa = mu k eps^2 / (8 omega)')
ax[0].set_ylabel('Anteil eingefrorener Takte (letzte 50 von 200 Takten)')
ax[0].set_title('Takt-Stillstand, feines Raster (Punkte: [M]-Schwellen, grau: Stillstand existiert ab)')
ax[0].legend(fontsize=7)
ax[1].set_xlabel('kappa')
ax[1].set_ylabel('mittlere Taktrate / omega')
ax[1].set_title('Taktrate vor dem Stillstand')
fig.tight_layout()
fig.savefig(os.path.join(D, 'bild_N1_stillstand.png'), dpi=110)
print('ok')
