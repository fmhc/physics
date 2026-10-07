#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-KH-1, Nachtrag 3 nach Sicht (beschreibend): Haengt die Nullrichtung von M_eff (Raumdiagonale ohne
Traegheit) von der Abbildung der zeitartigen Kanten ab? gz = 1 zeitsymmetrisch (Plan), gz = 2 einseitig (obere
Schicht), gz = 0 raeumlicher Anteil ohne Zeitableitung (Fourier-Mittelpunkt). Dazu: Spektrum der reduzierten
Grenzdynamik (wie nachtrag_ukh N4) je gz. Importiert ukh.py und nachtrag_ukh.py unveraendert."""
import argparse, sys, os, time
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import ukh  # noqa: E402
import nachtrag_ukh as nu  # noqa: E402
import tg  # noqa: E402
import hm  # noqa: E402
import tti  # noqa: E402


def herm(X):
    return 0.5 * (X + np.conj(X.T))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    vier, mod, geo, tb = ukh.bau_alles()
    e111 = [e for e in range(mod['E']) if ukh.DS[mod['zu_DS'][e]] == (1, 1, 1)][0]
    lm = float(mod['l'].mean())
    zeilen = []
    for nm, d in tti.richtungen13()[:3] + [tti.richtungen13()[9]]:
        for kl in (0.01, 0.2, 1.0):
            ks = (kl / lm) * d
            U = ukh.U_matrix(mod, ks)
            Bs, A1s, M, c = tg.ops(mod, ks)
            B = herm(Bs.toarray())
            z = {'richtung': nm, 'kl': kl}
            for gz in (0.0, 1.0, 2.0):
                gf = ukh.grenzform(vier, ks, gz=gz)
                T11 = np.eye(11, dtype=complex); T11[:7, :7] = U
                S = np.array([np.conj(T11.T) @ Sp @ T11 for Sp in gf['Q0']])
                Meff = herm(S[2][np.ix_(ukh.IQ, ukh.IQ)])
                Cv = S[0][ukh.IQ, ukh.IN][:, None]
                X = S[1][np.ix_(ukh.IQ, ukh.IB)]
                ev, Uv = np.linalg.eigh(Meff)
                i0 = int(np.argmin(np.abs(ev)))
                r = {'Meff_min_rel': float(np.abs(ev).min() / np.abs(ev).max()),
                     'u_111': float(abs(Uv[e111, i0]) ** 2), 'eig': [float(x) for x in ev],
                     'X_in_MeffM': nu.rest_proj(Meff @ M, X), 'C_in_MeffM': nu.rest_proj(Meff @ M, Cv),
                     'e_M': float(np.linalg.norm(gf['Q0'][2] - gf['Q0p'][2]) / np.linalg.norm(gf['Q0'][2]))}
                null = np.abs(ev) <= 1e-10 * np.abs(ev).max()
                u, W = Uv[:, null], Uv[:, ~null]
                if null.any():
                    Vuu = np.conj(u.T) @ B @ u
                    Vui = np.linalg.inv(Vuu)
                    Vp = herm(np.conj(W.T) @ B @ W - (np.conj(W.T) @ B @ u) @ Vui @ (np.conj(u.T) @ B @ W))
                    Cp = np.conj(W.T) @ Cv - (np.conj(W.T) @ B @ u) @ (Vui @ (np.conj(u.T) @ Cv))
                    Mp, Mdp = herm(np.conj(W.T) @ Meff @ W), np.conj(W.T) @ M
                else:
                    Vp, Cp, Mp, Mdp = B, Cv, Meff, M
                S2 = hm.zerlege(Mdp, Cp)[0]
                Ap = np.linalg.inv(Mp)
                lam = np.sort(np.linalg.eigvals(herm(np.conj(S2.T) @ Ap @ S2) @ herm(np.conj(S2.T) @ Vp @ S2)).real)
                r['w2_red'] = [float(x) for x in lam]
                r['dim_red'] = int(S2.shape[1])
                r['kubisch'] = float(np.sum(4.0 * np.sin(0.5 * ks) ** 2))
                z['gz%g' % gz] = r
            zeilen.append(z)
    res = {'info': {'argv': sys.argv, 'skript_sha256': ukh.sha(os.path.abspath(__file__)),
                    'ukh_sha256': ukh.sha(os.path.abspath(ukh.__file__))},
           'ergebnis': zeilen, 'laufzeit_s': time.time() - t0}
    tg.schreibe(a.out, res)
    print('fertig nachtrag_konv laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
