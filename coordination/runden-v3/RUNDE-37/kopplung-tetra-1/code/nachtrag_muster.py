#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KOPPLUNG-TETRA-1, Nachtrag nach dem Einfrieren (beschreibend, kein Urteil).
Liest lauf/eich.json (eingefrorenes kt.py, unveraendert importiert fuer die Ringgeometrie) und beschreibt die
Muster, die nach voller Relaxation (V3) Energie kosten: Eigenvektoren von S_V3, Zerlegung je Tetraeder in
Normal-, Radial- und Tangentialanteil, Inversionsparitaet, Holonomie-Blindheit, Extrapolation in 1/L."""
import argparse, json, os, sys, time, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kt  # noqa: E402  (eingefroren, unveraendert)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--eich', required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()
    ei = json.load(open(a.eich))
    res = {'eingabe_sha256': sha(a.eich), 'sha256_kt': sha(kt.__file__), 'ringe': {}}
    Hp, _ = kt.holonomie_matrix(False)
    Hm, _ = kt.holonomie_matrix(True)
    for rn, abc in (('haupt', (1, 2, 3)), ('gegen', (0, 1, 2))):
        geo = kt.ring_geometrie(abc)
        T, _ = kt.ring(abc)
        n = np.array(geo['normale'])
        c = np.array(geo['mitte'])
        mit = np.array([kt.mitte(nn, t) for nn, t in T])
        rad = mit - c
        rad = rad - np.outer(rad @ n, n)
        rad /= np.linalg.norm(rad, axis=1)[:, None]
        tan = np.cross(n[None, :], rad)
        out = {}
        Ls = sorted(ei['L_liste'])
        lam_L = []
        for L in Ls:
            S = np.array(ei[rn]['L%d' % L]['S_matrizen']['V3'])
            w, v = np.linalg.eigh(S)
            lam_L.append(w[-3:].tolist())
            e = {'eigenwerte_oben': w[-3:].tolist(), 'rang_1e-10': int((w > 1e-10 * w.max()).sum()),
                 'S_Hplus_T_rel': float(np.abs(S @ Hp.T).max() / w.max()),
                 'S_Hminus_T_rel': float(np.abs(S @ Hm.T).max() / w.max())}
            if L == Ls[-1]:
                muster = []
                for q in range(1, 4):
                    x = v[:, -q].reshape(6, 3)
                    x = x / np.abs(x).max()
                    comp = [{'normal': float(x[i] @ n), 'radial': float(x[i] @ rad[i]),
                             'tangential': float(x[i] @ tan[i])} for i in range(6)]
                    par = float(sum(x[i] @ x[(i + 3) % 6] for i in range(6)) / sum(x[i] @ x[i] for i in range(6)))
                    muster.append({'eigenwert': float(w[-q]), 'je_tetraeder': comp, 'inversionsparitaet': par,
                                   'typen': geo['typen']})
                e['muster'] = muster
            out['L%d' % L] = e
        lam_L = np.array(lam_L)
        sel = [i for i, L in enumerate(Ls) if L >= 16]
        X = np.vstack([np.ones(len(sel)), 1.0 / np.array(Ls)[sel]]).T
        coef, *_ = np.linalg.lstsq(X, lam_L[sel], rcond=None)
        out['extrapolation_a_plus_b_durch_L'] = {'L': [Ls[i] for i in sel], 'a': coef[0].tolist(), 'b': coef[1].tolist(),
                                                 'rest_max': float(np.abs(X @ coef - lam_L[sel]).max())}
        out['e_ref'] = ei['e_ref']
        res['ringe'][rn] = out
    res['zeit_utc'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    with open(a.out, 'w') as f:
        json.dump(res, f, indent=1)
    print('fertig nachtrag', flush=True)


if __name__ == '__main__':
    main()
