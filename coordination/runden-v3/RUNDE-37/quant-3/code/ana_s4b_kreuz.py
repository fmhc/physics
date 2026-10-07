#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S4B Zusatz Z5 (claude, 06.10.2026): Kreuzprobe der Bin-Werte S(D) zwischen den s4b-Laeufen.

Importiert ana_s4b (sigma_lauf) und ana. Nur ueber kleintest.sh auf der .69 (CPU, numpy):
  ana_s4b_kreuz.py LAUF1 LAUF2 LAUF3   (Pfade ohne Endung, gleiche beta, gleiche Bin-Zahl)
Ausgabe: Pearson-Koeffizient der 20 Bin-Werte S(D) je Paar von Laeufen (Familien 111 und 100, D = 0..3) und
Mittel und Streuung von ln(S_bin(Lauf i)/S_bin(Lauf j)) fuer D = 0 und 1 (nur Bins mit beiden S > 0).
"""
import itertools
import os
import sys

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import ana_s4b  # noqa: E402

runs = [ana_s4b.sigma_lauf(p, 1) for p in sys.argv[1:]]
namen = [r['datei'] for r in runs]
for fam in ('111', '100'):
    print('=== Familie %s ===' % fam)
    for (i, a), (j, b) in itertools.combinations(list(enumerate(runs)), 2):
        Sa, Sb = a['_Sm'][fam], b['_Sm'][fam]
        pe = [float(np.corrcoef(Sa[:, D], Sb[:, D])[0, 1]) for D in range(0, 4)]
        print('Pearson %s gegen %s, D = 0..3: %s' % (namen[i], namen[j], np.round(pe, 3).tolist()))
        for D in (0, 1):
            ok = (Sa[:, D] > 0) & (Sb[:, D] > 0)
            lr = np.log(Sa[ok, D] / Sb[ok, D])
            print('   ln(S_bin(%s)/S_bin(%s)) bei D = %d: Bins %d, Mittel %.4f, Streuung der Bins %.4f, Mittel des Verhaeltnisses der Mittel %.4f'
                  % (namen[i], namen[j], D, int(ok.sum()), float(lr.mean()), float(lr.std(ddof=1)),
                     float(np.log(Sa[:, D].mean() / Sb[:, D].mean()))))
print('Bin-Werte S(0), Familie 111 (20 Bins) je Lauf:')
for r in runs:
    print(' ', r['datei'], np.round(r['_Sm']['111'][:, 0], 4).tolist())
