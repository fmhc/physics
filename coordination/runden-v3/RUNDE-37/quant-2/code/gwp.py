#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-2: Nachpruefung und Speicherung der gefundenen Potenz-Gewichte (gw.py lief in die 600-s-Grenze, Werte aus
gw.log uebernommen). Aufruf: gwp.py TAU O1,...,O9 AUS  (omega_0 = 0). Dichte Bloch-Probe mit 96 neuen q."""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gw, qu2  # noqa: E402

tau = float(sys.argv[1])
om = np.r_[0.0, [float(x) for x in sys.argv[2].split(',')]]
aus = sys.argv[3]
V = gw.Vorlage(nq=96, seed=99)
e, w = gw.bewerte(V, tau, om)
e0, w0 = gw.bewerte(V, tau, np.zeros(10))
tsl = np.array([len(set(d[3] for (_, d) in key)) == 1 for key in V.keys])
st = {'w_min': float(w.min()), 'w_max': float(w.max()), 'w_mittel': float(w.mean()),
      'w_quantile_1_5_25_50_75_95_99': [float(x) for x in np.percentile(w, [1, 5, 25, 50, 75, 95, 99])],
      'w_scheibe_mittel': float(w[tsl].mean()), 'w_zeitartig_mittel': float(w[~tsl].mean()),
      'n_scheibe': int(tsl.sum()), 'negative_klassen': [[list(map(list, V.keys[i])), float(w[i])] for i in np.where(w < 0)[0]],
      'summe_w_je_zelle': float(w.sum()), 'summe_w0_je_zelle': float(w0.sum())}
out = {'kopf': qu2.kopf(), 'tau': tau, 'omega': om.tolist(), 'gewichtet_nq96': e, 'omega0_nq96': e0, 'statistik': st,
       'd1d0_max': V.d1d0}
np.savez(aus + '.npz', tau=tau, omega=om, w=w)
with open(aus + '.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps({'gewichtet': e, 'omega0': e0}), flush=True)
print(json.dumps(st)[:2000], flush=True)
