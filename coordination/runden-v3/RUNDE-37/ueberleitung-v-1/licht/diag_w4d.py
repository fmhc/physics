#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diagnose W4D (beschreibend): Eichrest der 3+1-Form je endlichem h ohne Extrapolation, Blocknormen je h, und
direkte Probe des 4D-Eichvektors in den Variablen (a, phi, L) bei endlichem h und reellem w."""
import argparse, sys, os, time, platform
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import licht as LI  # noqa: E402
import uv  # noqa: E402
import tg  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    lm = 0.3589683417646019
    R = dict(__import__('tti').richtungen13())
    ks = (0.05 / lm) * R['100']
    erg = []
    rng = np.random.default_rng(5)
    for j in (0, 2, 4, 6, 8, 10, 12, 14):
        h = 2.0 ** -j
        L = LI.Licht4(h)
        V = L.V
        nq, NV = V.nq, V.NV
        IA = list(range(nq)); IP = list(range(nq, nq + NV))
        S, kd = L.bloecke(ks)
        D = LI.d0_raum(V, ks)
        z = {'h': h, 'L_kond': kd}
        if S is None:
            erg.append(z)
            continue
        z['norm'] = {nm: [float(np.linalg.norm(S[p][np.ix_(I, J)])) for p in range(3)]
                     for nm, (I, J) in (('aa', (IA, IA)), ('ap', (IA, IP)), ('pp', (IP, IP)))}
        Sa, kp = uv.schur_reihe(S, IA, IP)
        if Sa is not None:
            z['eich_rest'] = [float(np.linalg.norm(Sa[p] @ D) / (np.linalg.norm(Sa[p]) * np.linalg.norm(D))) for p in range(3)]
        # Bedingungen fuer den Grenz-Nullvektor (d0 chi, i w chi): Ordnung w^0, w^1, w^2
        chi = rng.normal(size=NV) + 1j * rng.normal(size=NV)
        u = D @ chi
        r0a = S[0][np.ix_(IA, IA)] @ u
        r1a = S[1][np.ix_(IA, IA)] @ u + S[0][np.ix_(IA, IP)] @ (1j * chi)
        r1p = S[1][np.ix_(IP, IA)] @ u + S[0][np.ix_(IP, IP)] @ (1j * chi)
        r2a = S[2][np.ix_(IA, IA)] @ u + S[1][np.ix_(IA, IP)] @ (1j * chi)
        sc = np.linalg.norm(u) * max(np.linalg.norm(S[p]) for p in range(3))
        z['null_ordnung'] = {'w0_a': float(np.linalg.norm(r0a) / sc), 'w1_a': float(np.linalg.norm(r1a) / sc),
                             'w1_phi': float(np.linalg.norm(r1p) / sc), 'w2_a': float(np.linalg.norm(r2a) / sc)}
        erg.append(z)
    tg.schreibe(a.out, {'info': {'argv': sys.argv, 'python': platform.python_version()}, 'ergebnis': erg,
                        'laufzeit_s': time.time() - t0})
    print('fertig diag', flush=True)


if __name__ == '__main__':
    main()
