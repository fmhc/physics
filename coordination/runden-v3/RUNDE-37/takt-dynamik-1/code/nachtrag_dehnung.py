#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TAKT-DYNAMIK-1, Nachtrag nach dem Einfrieren (beschreibend): Kantendehnungen der normierten Mode (TT-Lesung = A)
und kleinste Randabstaende mu0 der Ausgangsnetze. Benutzt td.py (eingefroren) unveraendert."""
import json, os, sys
import numpy as np
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import td  # noqa: E402
import uk  # noqa: E402

out = []
for name in ['glas-N128-s1', 'glas-N128-s2', 'glas-N128-s3', 'glas-N128-s4', 'VD2']:
    LV, pos, G, O, ninfo = td.netz_bauen(name)
    k1 = (2 * np.pi * np.linalg.inv(LV).T)[0]
    hp, hx = td.polarisation(k1)
    N = td.Netz(LV, pos, G, O, k1, hp, hx)
    N.hp = hp
    mode, xm, w2, Qm = td.tt_mode(N, 1.0, k1)
    a = N.S @ xm                       # Kantendehnung bei TT-Lesung 1 (also je Einheit A)
    mu0 = uk.raender(LV, pos, G, O, N.fl)
    s = np.sort(mu0)
    out.append({'netz': name, 'E': N.E, 'F': int(N.fl['F']), 'max_abs_a_je_A': float(np.abs(a).max()),
                'rms_a_je_A': float(np.sqrt(np.mean(a ** 2))), 'median_abs_a_je_A': float(np.median(np.abs(a))),
                'mu0_kleinste_5': [float(x) for x in s[:5]], 'mu0_unter_1e-3': int((mu0 < 1e-3).sum()),
                'mu0_unter_1e-2': int((mu0 < 1e-2).sum()), 'mode_anteil': mode['anteil_TT_welle'], 'omega': mode['omega']})
    print(name, 'fertig', flush=True)
with open(sys.argv[1] + '.tmp', 'w') as fh:
    json.dump(out, fh, indent=1)
os.replace(sys.argv[1] + '.tmp', sys.argv[1])
