#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S5: Erwartetes Verhaeltnis E_s/E_t im Freifeld fuer isotropes F, aus den Gewichten gwp.npz und den Dreiecksklassen.
E_s = Beitrag der Dreiecke, die qu2.netz als 'Scheibe' (alle Ecken gleiche Zelle-Zeitverschiebung) fuehrt."""
import json
import os
import sys
import numpy as np
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import qu2


def main():
    g = qu2.netz_gitter(0.348006576329167)
    h = qu2.hodge2(g)
    w = np.asarray(np.load(os.path.join(HIER, 'gwp.npz'))['w'], float)
    sl = np.array([len(set(d[3] for (_, d) in key)) == 1 for key in h['keys']])
    Sb = h['S']
    q = (Sb ** 2).sum(1)
    out = {'n_klassen': len(w), 'n_scheibe': int(sl.sum()),
           'Spur_Ms': float((w * q)[sl].sum()), 'Spur_Mt': float((w * q)[~sl].sum()),
           'Es_zu_Et_isotrop': float((w * q)[sl].sum() / (w * q)[~sl].sum()),
           'Ms_diag': np.einsum('f,fi,fi->i', w * sl, Sb, Sb).tolist(), 'Mt_diag': np.einsum('f,fi,fi->i', w * (~sl), Sb, Sb).tolist(),
           'IU': [list(x) for x in qu2.IU],
           'Gewichtsanteil_Scheibe': float(w[sl].sum() / w.sum())}
    print(json.dumps(out, indent=1))
    with open(sys.argv[1], 'w') as f:
        json.dump(out, f, indent=1)


if __name__ == '__main__':
    main()
