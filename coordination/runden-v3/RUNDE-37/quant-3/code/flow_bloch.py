#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S5: Freifeld-Spektrum des naiven Flusses d A_l/dt = -(K A)_l auf dem Zeltnetz (nur numpy, CPU).
K(k) = D(k)^+ diag(w) D(k), D = bloch_d1 aus qu2.py (Dreieck von Kante), w = gwp.npz (Potenz-Dual), A_l = Drehwinkel.
Fuer den Hyperkubus ist die uebertragene Rate lambda = Summe_mu (2 - 2 cos k_mu) = |k|^2 (a = 1).
Ausgabe: kleinste Eigenwerte je k, transversale Rate / |k|^2 je Richtung (Isotropie des Flusszeit-Massstabs), Bereich des Spektrums."""
import json
import sys
import os
import numpy as np
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import qu2


def main():
    tau = 0.348006576329167
    g = qu2.netz_gitter(tau)
    h = qu2.hodge2(g)
    w = np.asarray(np.load(os.path.join(HIER, 'gwp.npz'))['w'], float)
    out = {'NE': int(g.NE), 'nf': int(len(w))}
    dirs = {'x': (1, 0, 0, 0), 'y': (0, 1, 0, 0), 'z': (0, 0, 1, 0), '111': (1, 1, 1, 0), '110': (1, 1, 0, 0), 't': (0, 0, 0, 1),
            'x+t': (1, 0, 0, 1), '111+t': (1, 1, 1, 1), 'xyt': (1, 1, 0, 1)}
    rows = []
    for name, d in dirs.items():
        d = np.array(d, float)
        d /= np.linalg.norm(d)
        for kk in (0.05, 0.1, 0.2, 0.4):
            D = qu2.bloch_d1(g, h['keys'], kk * d)
            K = D.conj().T @ (w[:, None] * D)
            K = 0.5 * (K + K.conj().T)
            ev = np.linalg.eigvalsh(K)
            nz = ev[np.abs(ev) > 1e-8 * max(1.0, kk * kk)]
            rows.append({'richtung': name, 'k': kk, 'ev_kleinste': ev[:16].tolist(), 'n_nullmoden': int((np.abs(ev) <= 1e-8).sum()),
                         'rate_unten_ueber_k2': [float(x / kk ** 2) for x in nz[:6]], 'ev_min': float(ev.min()), 'ev_max': float(ev.max())})
    out['zeilen'] = rows
    # Spektrum ueber zufaellige k in der Brillouin-Zone (Gitter ueber Zelle): max und min
    rng = np.random.default_rng(1)
    mx, mn = [], []
    for _ in range(60):
        n = rng.uniform(-np.pi, np.pi, 4)
        k4 = np.linalg.solve(g.A.T, n)
        D = qu2.bloch_d1(g, h['keys'], k4)
        K = D.conj().T @ (w[:, None] * D)
        ev = np.linalg.eigvalsh(0.5 * (K + K.conj().T))
        mx.append(ev.max())
        mn.append(ev.min())
    out['zufall_k'] = {'ev_max': float(max(mx)), 'ev_min': float(min(mn)), 'eps_max_RK3_2.5_ueber_evmax': 2.5 / float(max(mx))}
    with open(sys.argv[1], 'w') as f:
        json.dump(out, f, indent=1)
    for r in rows:
        print(r['richtung'], r['k'], 'Null', r['n_nullmoden'], 'rate/k2', np.round(r['rate_unten_ueber_k2'], 4), 'ev_min %.3g' % r['ev_min'])
    print(out['zufall_k'])


if __name__ == '__main__':
    main()
