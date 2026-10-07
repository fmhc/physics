#!/usr/bin/env python3
# Diagnose 2 (nachtraeglich, nicht gewertet): Newton-Verlauf ab gespeicherter Zeile.
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zweifeld as Z
d = np.load('aus/prof-M2.npz')
print('zeilen', d['zeilen'][:3], d['U_st1'].dtype, d['U_st1'].shape, d['V_st1'].shape, float(d['R_lin']))
hp = float(d['hp_st1'])
for j, w2n in ((0, 0.830), (0, 0.8299), (1, 0.832), (1, 0.831), (5, 0.840), (5, 0.839), (40, 0.910), (40, 0.909), (40, 0.911)):
    u = d['U_st1'][j]; v = d['V_st1'][j]
    hist = []
    for mi in (1, 2, 3, 4, 6, 10):
        un, vn, it, sch, ok = Z.numerov_newton('M2', w2n, hp, u, v, maxit=mi)
        hist.append('%d:%.1e' % (it, sch))
    print('row', float(d['zeilen'][j]), '->', w2n, ' '.join(hist), 'ok', ok, flush=True)
