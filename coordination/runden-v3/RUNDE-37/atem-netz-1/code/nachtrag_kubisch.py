#!/usr/bin/env python3
"""ATEM-NETZ-1, Nachtrag 1 [Zusatz Leitung, beschreibend, nach dem Einfrieren]:
Takt-Stillstand auf dem einfach-kubischen Gitter (z = 6, zweifaerbbar) gegen Pyrochlor (z = 6, frustriert).
Gleiche Einstellungen wie teilB2 in atem.py (eingefrorene Fassung, wird importiert): 26 kappa-Werte, Saaten 1 und 2,
200 Takte, W = 50, T = T_ABS, Zufallsphasen mit denselben Saaten-Regeln.
Aufruf (.69, kleintest.sh): nachtrag_kubisch.py <lauf-ordner> <ausgabe.json>
"""
import json
import math
import os
import sys
import time

import numpy as np

import atem


def kubisch(L):
    def idx(x, y, z):
        return (x % L) + L * ((y % L) + L * (z % L))
    b = []
    for z in range(L):
        for y in range(L):
            for x in range(L):
                i = idx(x, y, z)
                b.append((i, idx(x + 1, y, z)))
                b.append((i, idx(x, y + 1, z)))
                b.append((i, idx(x, y, z + 1)))
    sub = np.array([(-1) ** (x + y + z) for z in range(L) for y in range(L) for x in range(L)])
    return L ** 3, np.array(b), {'sub': sub}


def kappa50(res, seeds=None):
    # dieselbe Regel wie auswertung.py (eingefroren)
    ks = sorted(set(r['kappa'] for r in res))
    f = []
    for k in ks:
        v = [r['gefroren'] for r in res if r['kappa'] == k and (seeds is None or r['seed'] in seeds)]
        f.append(float(np.mean(v)))
    for i, (k, fv) in enumerate(zip(ks, f)):
        if fv >= 0.5:
            if i == 0:
                return None, 'unterhalb des Bereichs', ks, f
            k0, f0 = ks[i - 1], f[i - 1]
            t = (0.5 - f0) / (fv - f0)
            return float(math.exp(math.log(k0) + t * (math.log(k) - math.log(k0)))), 'ok', ks, f
    return None, 'nicht bestimmbar', ks, f


def main():
    D, ziel = sys.argv[1], sys.argv[2]
    L = 10
    N, bonds, ex = kubisch(L)
    seeds = [1, 2]
    takte, W = 200, 50
    res = []
    t0 = time.time()
    for kappa in atem.kappa_gitter(False):
        netz = atem.FestNetz(N, bonds, kappa)
        for s in seeds:
            rng0 = np.random.default_rng(5000 + s)
            phi0 = rng0.uniform(0, 2 * np.pi, N)
            rng = np.random.default_rng(6000 + s)
            st = {}

            def cb(n, th, phi):
                if n == takte - W - 1:
                    st['v'] = phi.copy()
                if n == takte - 1:
                    st['phi'] = phi.copy()
                    st['th'] = th.copy()
            atem.lauf_fest(netz.f_voll, phi0, takte, 0.01, atem.T_ABS, rng, True, 5, cb)
            fr, v = atem.gefroren(st['phi'], st['v'], W)
            z = {'kappa': float(kappa), 'seed': s, 'gefroren': float(fr.mean()),
                 'gefroren_A': float(fr[ex['sub'] > 0].mean()), 'gefroren_B': float(fr[ex['sub'] < 0].mean())}
            sinphi = np.sin(st['phi'])
            z['sin_gefroren_mittel'] = float(sinphi[fr].mean()) if fr.any() else None
            lauf = ~fr
            ml = lauf[bonds[:, 0]] & lauf[bonds[:, 1]]
            if ml.any():
                d = st['th'][bonds[ml, 0]] - st['th'][bonds[ml, 1]]
                z['cos_laufende_bindungen'] = float(np.cos(d).mean())
            res.append(z)
    out = {'teil': 'Nachtrag1-kubisch', 'L': L, 'N': N, 'takte': takte, 'W': W, 'res': res,
           'sek': time.time() - t0}
    kk, sk, ksk, fk = kappa50(res)
    out.update({'kappa50_kubisch': kk, 'status_kubisch': sk, 'kurve_kubisch': list(zip(ksk, fk))})
    for name, fn in (('pyro', 'B2_pyro.json'), ('dia', 'B2_dia.json')):
        p = os.path.join(D, fn)
        if os.path.exists(p):
            with open(p) as fh:
                b = json.load(fh)
            kx, sx, _, _ = kappa50(b['res'])
            out['kappa50_' + name] = kx
            out['status_' + name] = sx
    if out.get('kappa50_pyro') and kk:
        R = kk / out['kappa50_pyro']
        out['R_kub_pyro'] = R
        out['lesart_vorab'] = ('Frustration senkt die Schwelle um >= 10 %' if R >= 1.10 else
                               ('kein Frustrationseffekt ueber 10 %' if R > 0.91 else 'Frustration hebt die Schwelle'))
    if out.get('kappa50_dia') and kk:
        out['R_dia_kub'] = out['kappa50_dia'] / kk
    with open(ziel, 'w') as fh:
        json.dump(out, fh)
    print(json.dumps({k: out.get(k) for k in ('kappa50_kubisch', 'kappa50_pyro', 'kappa50_dia', 'R_kub_pyro',
                                              'R_dia_kub', 'lesart_vorab', 'sek')}), flush=True)


if __name__ == '__main__':
    main()
