#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, Zusatzprobe (nach den ersten Laeufen geschrieben, bn.py unveraendert importiert):
F aus bn.Netz.rest muss an krummen Konfigurationen der Gradient von Phi(l) = sum_v N_v H_v(l) sein (alle Ordnungen),
Phi nur aus Diederwinkeln (ohne J). Richtungsableitung per zentraler Differenz, zwei Schrittweiten.
Dazu Euler: sum_e l_e F_e = sum_v N_v H_v (H_v homogen vom Grad 1).
"""
import json, sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bn  # noqa: E402


def main():
    L = int(sys.argv[1])
    out_pfad = sys.argv[2]
    t0 = time.time()
    net = bn.Netz(L)
    rng = np.random.default_rng(11)
    E, nV = net.E, net.nV
    z = np.zeros((L, L, L, nV))
    res = {'L': L, 'proben': []}
    for amp_a, amp_mu in ((0.02, 0.1), (0.05, 0.3)):
        a = amp_a * rng.normal(size=(L, L, L, E))
        mu = amp_mu * rng.normal(size=(L, L, L, nV))
        RF, RG = net.rest(a, mu, z)
        F = -2.0 * RF / net.l0
        l = net.l0 * (1 + a)
        phi = lambda aa: float(((1 + mu) * net.rest(aa, mu, z)[1]).sum())
        euler = float((l * F).sum())
        nh = float(((1 + mu) * RG).sum())
        d = rng.normal(size=a.shape)
        soll = float((F * net.l0 * d).sum())
        z1 = {'amp_a': amp_a, 'amp_mu': amp_mu, 'euler_lF': euler, 'euler_NH': nh,
              'euler_rel': abs(euler - nh) / max(abs(nh), 1e-300), 'gradient_soll': soll}
        for h in (1e-4, 2e-4):
            ist = (phi(a + h * d) - phi(a - h * d)) / (2 * h)
            z1['gradient_h%g' % h] = ist
            z1['gradient_rel_h%g' % h] = abs(ist - soll) / abs(soll)
        res['proben'].append(z1)
    res['zeit_s'] = time.time() - t0
    with open(out_pfad, 'w') as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res))


if __name__ == '__main__':
    main()
