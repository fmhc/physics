#!/usr/bin/env python3
"""ZELLE600-1, Zusatz: Form jeder Winkelschale um den Pol (fuer die Legende der Ansicht).

Liest lauf-69/ecken.json und lauf-69/schalen.json, nimmt je Schale den 3D-Anteil (b, c, d) der Ecken
(der Pol ist der Realteil a = 1), normiert ihn und zaehlt den Nachbarschaftsgraphen der kuerzesten Abstaende:
Ikosaeder 12 Ecken / Grad 5 / 30 Kanten, Dodekaeder 20 / 3 / 30, Ikosidodekaeder 30 / 4 / 60.
Aufruf: python schalenform.py <lauf-69-ordner>
"""
import json
import math
import os
import sys
import time
from datetime import datetime, timezone

import numpy as np

T0 = time.time()
D = sys.argv[1] if len(sys.argv) > 1 else 'lauf-69'
V = np.array(json.load(open(os.path.join(D, 'ecken.json')))['koordinaten'])
S = json.load(open(os.path.join(D, 'schalen.json')))
FORM = {(12, 5, 30): 'Ikosaeder', (20, 3, 30): 'Dodekaeder', (30, 4, 60): 'Ikosidodekaeder'}
out = []
for sch in S['nach_winkel']:
    idx = sch['ecken']
    P = V[idx][:, 1:]
    n = len(idx)
    if n < 4:
        out.append({'schale': sch['schale'], 'winkel_grad': sch['winkel_grad'], 'anzahl': n, 'form': 'Punkt',
                    'realteil': [float(x) for x in V[idx][:, 0]]})
        continue
    r = np.linalg.norm(P, axis=1)
    U = P / r[:, None]
    d = np.linalg.norm(U[:, None, :] - U[None, :, :], axis=2)
    np.fill_diagonal(d, np.inf)
    dmin = d.min()
    nbm = np.abs(d - dmin) < 1e-9
    grad = nbm.sum(1)
    kanten = int(nbm.sum() // 2)
    key = (n, int(grad.min()), kanten)
    out.append({'schale': sch['schale'], 'winkel_grad': sch['winkel_grad'], 'anzahl': n,
                'radius_3d_min_max': [float(r.min()), float(r.max())],
                'realteil_min_max': [float(V[idx][:, 0].min()), float(V[idx][:, 0].max())],
                'grad_min_max': [int(grad.min()), int(grad.max())], 'kanten_kuerzester_abstand': kanten,
                'kuerzester_winkel_grad': float(math.degrees(2 * math.asin(dmin / 2))),
                'form': FORM.get(key, 'andere') if grad.min() == grad.max() else 'unregelmaessig'})
res = {'start_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'laufzeit_s': round(time.time() - T0, 3),
       'quelle': 'lauf-69/ecken.json, lauf-69/schalen.json', 'schalen': out}
tmp = os.path.join(D, 'schalenform.json.tmp')
with open(tmp, 'w') as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write('\n')
os.replace(tmp, os.path.join(D, 'schalenform.json'))
print(json.dumps([[o['schale'], o['winkel_grad'], o['anzahl'], o['form']] for o in out], ensure_ascii=False))
