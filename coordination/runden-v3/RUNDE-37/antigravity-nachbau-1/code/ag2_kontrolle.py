#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ANTIGRAVITY-NACHBAU-1, AG2 Gegenprobe: Ist die globale Volumenbedingung besonders, oder toetet jede Zufallsbedingung
die negative Kinetik-Richtung? Und liegt die TT-Mode im Kern der Bedingungen?
Nutzt ag2_unimod (Hook auf nn.NetzG) und ersetzt dessen Auswertung.
  - Kriterium: Kinetik K = Ar^-1 mit genau einer negativen Richtung ist auf c-perp positiv definit genau dann,
    wenn c^T Ar c < 0 (c in x-Koordinaten).
  - Zufall Z1: c ~ N(0, 1) in x (10000); Z2: Zufallsgewichte w_e >= 0 je Kante in a, c = S^T w (10000);
    Z3: wie die Volumenbedingung, aber Tetraedervolumen-Ableitungen je Kante permutiert (1000).
  - Wachsende Moden fuer 40 Zufallsbedingungen je Art.
"""
import json, sys, time
import numpy as np
import scipy.linalg as sla

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/antigravity-nachbau-1/code')
import ag2_unimod as U  # noqa: E402
import td  # noqa: E402

REK2 = []


def wachsend(N, c):
    Zx = sla.null_space(c[None, :])
    Ainv = np.linalg.inv(N.Ar)
    Kr = Zx.T @ Ainv @ Zx
    Vr = Zx.T @ N.Br @ Zx
    w = sla.eigvals(0.5 * (Vr + Vr.T), 0.5 * (Kr + Kr.T))
    s = float(np.abs(w).max())
    return int(((w.real < -td.TAU_REL * s) | (np.abs(w.imag) > td.TAU_REL * s)).sum())


def auswerten(N, rolle):
    t0 = time.time()
    rng = np.random.default_rng(11)
    C, V0 = U.zwang(N)
    cg = N.S.T @ C.sum(1)
    r = {'rolle': rolle, 'A_pd': bool(N.A_pd)}
    if rolle == 'start':
        k1 = 2 * np.pi * np.linalg.inv(N.LV).T[0]
        mode, xm, w2, Qm = td.tt_mode(N, 1e-3, k1)
        Cx = N.S.T @ C
        r['tt_global_rel'] = float(abs(cg @ xm) / (np.linalg.norm(cg) * np.linalg.norm(xm)))
        r['tt_lokal_rel'] = float(np.linalg.norm(Cx.T @ xm) / (np.linalg.norm(Cx) * np.linalg.norm(xm)))
    if not N.A_pd:
        Ar = N.Ar
        r['krit_global'] = float(cg @ Ar @ cg / (cg @ cg) / np.abs(np.linalg.eigvalsh(Ar)).max())
        Z1 = rng.normal(size=(10000, N.m))
        W = rng.uniform(0, 1, size=(10000, N.E))
        Z2 = W @ N.S
        # Z3: Ableitungen permutiert
        g = C.sum(1)
        Z3 = np.array([N.S.T @ rng.permutation(g) for _ in range(1000)])
        for name, Z in (('Z1', Z1), ('Z2', Z2), ('Z3', Z3)):
            k = np.einsum('ni,ij,nj->n', Z, Ar, Z)
            r['anteil_pd_' + name] = float((k < 0).mean())
            r['wachsend_' + name] = [wachsend(N, Z[i]) for i in range(40)]
        r['wachsend_global'] = wachsend(N, cg)
        # Ueberlapp der negativen Richtung von Ar mit cg
        ev, V = np.linalg.eigh(Ar)
        r['cos_neg_richtung_global'] = float(abs(V[:, 0] @ cg) / np.linalg.norm(cg))
    r['t_s'] = time.time() - t0
    REK2.append(r)
    U.REK.append(r)
    print('kontrolle', json.dumps(r)[:2000], flush=True)


U.auswerten = auswerten

if __name__ == '__main__':
    U.main()
