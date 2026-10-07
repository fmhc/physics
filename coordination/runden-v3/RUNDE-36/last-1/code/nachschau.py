#!/usr/bin/env python3
# LAST-1 Nachschau (nach dem Einfrieren, nur beschreibend, aendert keine Urteile):
# Werte von Pi_korr laengs einzelner Richtungen fuer alle r, L = 64 und 128, mit lokalen Steigungen.
import sys, json, math
import numpy as np

S2 = math.sqrt(2.0)
z = np.load(sys.argv[1]); z64 = np.load(sys.argv[2]); k = np.load(sys.argv[3])
nv = z['aniso_L128_n']
lut = {tuple(int(x) for x in v): i for i, v in enumerate(nv)}
out = {}
for netz, qn, hkl in (('iso', 'b', (1, 1, 0)), ('iso', 'b', (1, 0, 0)), ('iso', 'b', (1, 1, 1)), ('iso', 'b', (3, 2, 0)),
                      ('aniso', 'b', (3, 2, 0)), ('aniso', 'b', (2, 1, 1)), ('aniso', 'b', (1, 1, 0)), ('aniso', 'b', (1, 1, 1)),
                      ('aniso', 'c', (1, 1, 0)), ('iso', 'c', (1, 1, 0))):
    h = np.array(hkl); t = 1 if h.sum() % 2 == 0 else 2
    rows = []
    s = 1
    while True:
        v = h * t * s
        r = float(np.linalg.norm(v) / S2)
        if r > 16 + 1e-9:
            break
        if r >= 2 - 1e-9:
            i = lut[tuple(int(x) for x in v)]
            rows.append(dict(r=round(r, 3), korr128=float(z['%s_L128_Pi_korr_%s' % (netz, qn)][i]),
                             korr64=float(z64['%s_L64_Pi_korr_%s' % (netz, qn)][i]),
                             kont=float(k['%s_Pi_kont_%s' % (netz, qn)][i])))
        s += 1
    for a, b in zip(rows[:-1], rows[1:]):
        if a['korr128'] * b['korr128'] > 0:
            b['lokale_steigung'] = round(-math.log(abs(b['korr128'] / a['korr128'])) / math.log(b['r'] / a['r']), 3)
    out['%s_%s_%s' % (netz, qn, ''.join(map(str, hkl)))] = rows
json.dump(out, open(sys.argv[4], 'w'), indent=1)
print('nachschau fertig')
