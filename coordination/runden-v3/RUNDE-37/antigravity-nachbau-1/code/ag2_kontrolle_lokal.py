#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ANTIGRAVITY-NACHBAU-1, AG2 Gegenprobe zur lokalen Lesart: Toeten auch 128 Zufallsbedingungen die wachsende Mode?
  L1: 128 Gauss-Vektoren in x; L2: gleiche Besetzung wie C (Kante an Ecke), Werte zufaellig positiv (|N(0,1)|);
  L3: C mit je Ecke zufaellig permutierten Spalten-Werten (Vorzeichen und Betraege der Volumenableitungen behalten).
  Je Art 12 Versuche; gezaehlt: negative Kinetik-Richtungen, wachsende Moden. Nur Rollen neu_hg und neu_gd.
"""
import json, sys, time
import numpy as np
import scipy.linalg as sla

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/antigravity-nachbau-1/code')
import ag2_unimod as U  # noqa: E402
import td  # noqa: E402


def zaehle(N, Cx):
    Zx = sla.null_space(Cx.T)
    Ainv = np.linalg.inv(N.Ar)
    Kr = Zx.T @ Ainv @ Zx
    Kr = 0.5 * (Kr + Kr.T)
    Vr = Zx.T @ N.Br @ Zx
    Vr = 0.5 * (Vr + Vr.T)
    kn = U.neg(np.linalg.eigvalsh(Kr))
    w = sla.eigvals(Vr, Kr)
    s = float(np.abs(w).max())
    return kn, int(((w.real < -td.TAU_REL * s) | (np.abs(w.imag) > td.TAU_REL * s)).sum())


def auswerten(N, rolle):
    if rolle not in ('neu_hg', 'neu_gd'):
        return
    t0 = time.time()
    rng = np.random.default_rng(5)
    C, _ = U.zwang(N)
    r = {'rolle': rolle, 'volumen_lokal': zaehle(N, N.S.T @ C)}
    for name in ('L1', 'L2', 'L3'):
        out = []
        for _ in range(12):
            if name == 'L1':
                Cx = rng.normal(size=(N.m, C.shape[1]))
            elif name == 'L2':
                Cr = np.where(C != 0, np.abs(rng.normal(size=C.shape)), 0.0)
                Cx = N.S.T @ Cr
            else:
                Cr = np.zeros_like(C)
                for v in range(C.shape[1]):
                    nz = np.nonzero(C[:, v])[0]
                    Cr[nz, v] = rng.permutation(C[nz, v])
                Cx = N.S.T @ Cr
            out.append(zaehle(N, Cx))
        r[name] = out
    r['t_s'] = time.time() - t0
    U.REK.append(r)
    print('lokal', json.dumps(r), flush=True)


U.auswerten = auswerten

if __name__ == '__main__':
    U.main()
