"""KAUSAL-WELLE-4D, Rauchwerkzeug (nur Kontinuum): Johnston-Erwartung gegen Kontinuum an den Pruefpunkten.

Aufruf (nur ueber kleintest.sh): kont_blick.py <kontinuumordner>
"""
import json
import os
import sys

import numpy as np

K = np.load(os.path.join(sys.argv[1], "kontinuum.npz"))
pp = K["pruefpunkte"]
phi_k = K["phi_k"]
ref = K["quad_kappe"]
jo = K["johnston"]
rh = [float(x) for x in K["johnston_rhos"]]
out = {}
for ir, r in enumerate(rh):
    rows = []
    for c in range(pp.shape[0]):
        for i in range(9):
            q = jo[ir, 0, c, i] / ref[c, i]
            rows.append([c, float(pp[c, i, 0]), float(pp[c, i, 1]), float(pp[c, i, 3]), round(float(abs(q)), 4),
                         round(float(np.angle(q)), 4), round(float(abs(jo[ir, 0, c, i] - ref[c, i]) / abs(ref[c, i])), 4)])
    out[str(r)] = rows
out["abs_bezug"] = [[round(float(abs(ref[c, i])), 5) for i in range(9)] for c in range(pp.shape[0])]
print(json.dumps(out))
