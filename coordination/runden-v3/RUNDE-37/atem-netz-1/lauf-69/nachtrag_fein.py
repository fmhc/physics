#!/usr/bin/env python3
"""ATEM-NETZ-1, Nachtrag 1 (fein) [Zusatz Leitung, beschreibend, nach dem Einfrieren]:
Takt-Stillstand mit feinem kappa-Raster (Schritt ~2 %) auf Pyrochlor (z = 6, frustriert), einfach-kubisch (z = 6,
zweifaerbbar) und Diamant (z = 4, zweifaerbbar). Ersetzt nachtrag_kubisch.py vor dessen Start (Grund in NACHTRAG-1.md:
das B2-Raster hat 14,6 % Schrittweite, der erwartete Frustrationseffekt ist ~3,5 %).
Gleiche Einstellungen wie teilB2 (eingefrorene atem.py): 200 Takte, W = 50, T = T_ABS, Zufallsphasen Saat 1
(Saaten-Regel wie B2), dt = 0,01.
Aufruf (.69, kleintest.sh): nachtrag_fein.py <ausgabe.json>
"""
import json
import math
import sys
import time

import numpy as np

import atem
from nachtrag_kubisch import kubisch


def scan(N, bonds, kappas, takte=200, W=50, seed=1):
    res = []
    for kappa in kappas:
        netz = atem.FestNetz(N, bonds, kappa)
        rng0 = np.random.default_rng(5000 + seed)
        phi0 = rng0.uniform(0, 2 * np.pi, N)
        rng = np.random.default_rng(6000 + seed)
        st = {}

        def cb(n, th, phi):
            if n == takte - W - 1:
                st['v'] = phi.copy()
            if n == takte - 1:
                st['phi'] = phi.copy()
        atem.lauf_fest(netz.f_voll, phi0, takte, 0.01, atem.T_ABS, rng, True, 5, cb)
        fr, v = atem.gefroren(st['phi'], st['v'], W)
        res.append({'kappa': float(kappa), 'gefroren': float(fr.mean()), 'v_mittel': float(v.mean())})
    return res


def schwelle(res):
    ks = [r['kappa'] for r in res]
    f = [r['gefroren'] for r in res]
    for i in range(len(ks)):
        if f[i] >= 0.5:
            if i == 0:
                return {'status': 'unterhalb des Bereichs', 'unten': None, 'oben': ks[0], 'kappa50': None}
            t = (0.5 - f[i - 1]) / (f[i] - f[i - 1])
            k50 = math.exp(math.log(ks[i - 1]) + t * (math.log(ks[i]) - math.log(ks[i - 1])))
            return {'status': 'ok', 'unten': ks[i - 1], 'oben': ks[i], 'kappa50': k50}
    return {'status': 'nicht bestimmbar', 'unten': ks[-1], 'oben': None, 'kappa50': None}


def main():
    ziel = sys.argv[1]
    t0 = time.time()
    fein_z6 = list(np.geomspace(0.0280, 0.0400, 19))
    fein_z4 = list(np.geomspace(0.0400, 0.0620, 22))
    out = {'teil': 'Nachtrag1-fein', 'takte': 200, 'W': 50, 'seed': 1}
    for name, L, ks in (('pyro', 4, fein_z6), ('kubisch', 10, fein_z6), ('diamant', 5, fein_z4)):
        if name == 'kubisch':
            N, bonds, ex = kubisch(L)
        else:
            N, bonds, ex = atem.baue(name, L)
        t1 = time.time()
        res = scan(N, bonds, ks)
        out[name] = {'L': L, 'N': int(N), 'res': res, 'schwelle': schwelle(res), 'sek': time.time() - t1}
        print(name, json.dumps(out[name]['schwelle']), round(time.time() - t1, 1), 's', flush=True)
    kp, kk, kd = (out[n]['schwelle']['kappa50'] for n in ('pyro', 'kubisch', 'diamant'))
    if kp and kk:
        R = kk / kp
        out['R_kub_pyro'] = R
        out['lesart_vorab'] = ('Frustration senkt die Schwelle um >= 10 %' if R >= 1.10 else
                               ('kleiner Frustrationseffekt (2-10 %)' if R > 1.02 else
                                ('kein messbarer Effekt (+-2 %)' if R >= 0.98 else 'Frustration hebt die Schwelle')))
    if kd and kp:
        out['R_dia_pyro'] = kd / kp
    if kd and kk:
        out['R_dia_kub'] = kd / kk
    out['vorhersage_M'] = {'gleichfoermig_z6': 0.0347, 'geordnet_pyro': 0.0335, 'geordnet_kubisch': 0.0347,
                           'diamant': 0.0521, 'stillstand_gleichphasig_z6': 0.0283, 'stillstand_gleichphasig_z4': 0.0424}
    out['sek'] = time.time() - t0
    with open(ziel, 'w') as fh:
        json.dump(out, fh)
    print(json.dumps({k: out.get(k) for k in ('R_kub_pyro', 'R_dia_pyro', 'R_dia_kub', 'lesart_vorab', 'sek')}),
          flush=True)


if __name__ == '__main__':
    main()
