#!/usr/bin/env python3
# Diagnose (nachtraeglich, nicht gewertet): Hintergrund-Newton unterhalb der untersten Zeile 0,830.
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zweifeld as Z
d = np.load('aus/prof-M2.npz')
for st in (1, 2):
    hp = float(d['hp_st%d' % st]); u = d['U_st%d' % st][0]; v = d['V_st%d' % st][0]
    w2a = 0.830
    for w2n in (0.829, 0.8275, 0.825, 0.82, 0.815, 0.81, 0.805):
        un, vn, it, sch, ok = Z.numerov_newton('M2', w2n, hp, u, v, maxit=40)
        print('st', st, 'w2', w2n, 'ok', ok, 'it', it, 'sch %.3e' % sch, 'umin %.3e' % float(np.min(un[1:-1])),
              'umax %.3e' % float(np.max(un)), flush=True)
        if ok:
            g = Z.profil_groessen('M2', w2n, hp, un, vn)
            print('   Q %.6f E %.6f R_half %.4f chi0 %.3e f_R_rel %.2e' % (g['Q'], g['E'], g['R_half'], g['chi0'], g['f_R_rel']), flush=True)
            u, v = un, vn
        else:
            break
