#!/usr/bin/env python3
"""Test der Auswertung an einer handgeschriebenen Schein-Zeitreihe (keine Rechenwerte): nur Laufzeitfehler und Ereignislogik."""
import json
import sys

import numpy as np

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/raute-atem-1/code')
import auswertung as A  # noqa: E402

n = 10001
t = np.arange(n) * 0.05
gap = np.zeros((n, 6))
gap[:, 5] = 0.5 * np.cos(2 * np.pi * t / 100.0)
theta = np.radians(100 + 30 * np.cos(2 * np.pi * t / 100.0))
tb = np.random.default_rng(0).normal(0, 0.01, (n, 6))
tb[:, 0] += 0.05
fm = np.zeros((n, 6))
phi = np.zeros((n, 4))
phi[:, 2] = np.where((t % 100) < 50, 2.0, 0.0)
cd = gap[:, 5] < A.DELTA_F
p = '/home/fmh/fmhc-physics-remote/raute-atem-1/rauch/test/schein.npz'
np.savez(p, t=t, theta=theta, gap=gap, r=np.ones((n, 6)), tb=tb, fm=fm, phi=phi, x=np.zeros((n, 4, 3)), cd=cd)
m = A.lauf_metriken({'npz': p, 'dim': 3, 'B': 0.05, 'seed': 9, 'takte': 500, 'werkzeugprobe': {}})
print(json.dumps({k: m[k] for k in ['schliessen_plan', 'oeffnen_plan', 'oeffnen_karte', 'n_oeffnen_plan',
                                    'n_oeffnen_karte', 'umordnung', 't_umordnung', 'fp_fenster', 'fp_dauer_takte',
                                    'cd_anteil_gebunden', 'fp_lauf', 'zyklus_takte_plan', 'RA2_lauf_plan',
                                    'RA2_lauf_karte']}, indent=0))
