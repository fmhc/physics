#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S4B Zusatz Z4 (claude, 06.10.2026): Verschmierung der Scheiben-Korrelatoren in ana.py korr.

ana.py korr ordnet jedem der NV Punkte einer Zelle den Ebenenindex m . n (n = Zellindex) zu und ignoriert die Lage
des Punktes in der Zelle. Hier: Ebenenkoordinate u_b = m . f_b (f_b = Bruchkoordinaten des Punktes b in der Zelle,
in Einheiten des Ebenenabstands d_m; ganzzahlig = auf einer Gitterebene). Die Abweichung zwischen zugeordnetem und
wahrem Ebenenabstand eines Paares (b, b') ist u_b' - u_b.
Aufruf nur ueber kleintest.sh auf der .69 (CPU, numpy):  ana_s4b_scheiben.py LAUF_OHNE_ENDUNG
"""
import json
import sys

import numpy as np

M_FAM = {'111': [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)], '100': [(1, 1, 0), (1, 0, 1), (0, 1, 1)]}

with open(sys.argv[1] + '.json') as fh:
    res = json.load(fh)
L, NV = res['L'], res['NV']
box = np.array(res['box'])
AV = box / L
Binv = np.linalg.inv(AV)
Bv = Binv.T
xb = np.array(res['rpos'])[:NV]
f = xb @ Binv
print('L', L, 'NV', NV, 'Bruchkoordinaten der Punkte (Zelle):')
print(np.round(f, 4))
for fam, ms in M_FAM.items():
    for m in ms:
        u = np.round(f @ np.array(m), 6)
        d = 1.0 / np.linalg.norm(np.array(m) @ Bv)
        um = np.round(u % 1.0, 4)
        vals, cnt = np.unique(um, return_counts=True)
        du = (u[None, :] - u[:, None]).ravel()
        print('Familie %s m=%s d=%.4f  u_b mod 1: %s  (Werte:Anzahl %s)  Paar-Abweichung u_b\'-u_b: rms %.3f, max |.| %.3f Ebenen'
              % (fam, m, d, um.tolist(), dict(zip(vals.tolist(), cnt.tolist())), float(np.sqrt((du ** 2).mean())), float(np.abs(du).max())))
