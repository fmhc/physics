#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGULAER-V-1, NACHTRAG NACH SICHT (beschreibend, kein Urteil), geschrieben nach den Hauptlaeufen.

Anlass: In S3 (Extreme der Lochmitten-Gewichte) fiel beta auf etwa 2 % des Mittewerts, ohne l = 2-Anteil. Frage: Wechselt
beta in der Kammer das Vorzeichen (l = 4-isotrope Gewichtung in Ordnung k^2)?
  N1: symmetrischer Schnitt (x, y), baryzentrisches Gitter m = 24 im Dreieck, um 0,99 zur Mitte geschrumpft (325 Punkte).
  N2: Td-Schnitt (w_P, w_C1, w_C2, w_H; F-43m-symmetrisch), 200 Zufallsrichtungen aus der Mitte (default_rng([4096, 5, 11])),
      s = 0,25; 0,5; 0,75; 0,9; 0,99 des Wandabstands (1000 Punkte).
rv.py (eingefroren) wird unveraendert importiert.
Aufruf: python nachtrag_beta.py <aus.json>
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv  # noqa: E402
import danzer_naeherung as dn  # noqa: E402


def main(aus):
    ref = dn.referenzen()
    nd = dn.halbkugel(40)
    net = rv.netz_V(1)
    topo = rv.topologie(net)
    rows, A, G0 = rv.zeilen(net, topo)
    sy = rv.lp_symmetrisch(A, G0, rv.bahnmatrix(net))
    xm, ym = sy['x'], sy['y']
    E = np.array(rv.HAND['ecken_schnitt'])
    mid = np.array([xm, ym])
    res = {'x_mid': xm, 'y_mid': ym}
    # N1
    m = 24
    n1 = []
    for i in range(m + 1):
        for j in range(m + 1 - i):
            k = m - i - j
            p = (i * E[0] + j * E[1] + k * E[2]) / m
            p = mid + 0.99 * (p - mid)
            w = rv.w_sym(net, p[0], p[1])
            st, sk = rv.messen(net, topo, w, ref, nd)
            rec = {'x': float(p[0]), 'y': float(p[1]), 'marge': float((G0 + A @ w).min()),
                   'min_s0': float(st['s0'].min()), 'min_s1': float(st['s1'].min())}
            if sk is not None:
                rec.update(rv.kurz(sk))
            n1.append(rec)
    b = np.array([r.get('beta', np.nan) for r in n1])
    j0, j1 = int(np.nanargmin(b)), int(np.nanargmax(b))
    res['N1'] = {'punkte': n1, 'beta_min': float(np.nanmin(b)), 'ort_min': (n1[j0]['x'], n1[j0]['y']),
                 'beta_max': float(np.nanmax(b)), 'ort_max': (n1[j1]['x'], n1[j1]['y']),
                 'n_beta_neg': int(np.sum(b < 0)), 'n': len(n1)}
    rv.log('N1 fertig')
    # N2: Td-Schnitt
    B4 = np.zeros((net['n'], 4))
    for g in range(net['n']):
        s = g  # L = 1: globale Nummer = Untergitter
        col = 0 if s < 4 else (1 if s == 4 else (2 if s == 5 else 3))
        B4[g, col] = 1.0
    wmid = rv.w_sym(net, xm, ym)
    rng = np.random.default_rng([4096, 5, 11])
    n2 = []
    for r_ in range(200):
        z = rng.standard_normal(4)
        d = B4 @ z
        d -= d.mean()
        d /= np.linalg.norm(d)
        sw = rv.strahl_wand(A, G0, wmid, d)
        for s in (0.25, 0.5, 0.75, 0.9, 0.99):
            w = wmid + s * sw * d
            st, sk = rv.messen(net, topo, w, ref, nd)
            zb = np.linalg.lstsq(B4, w, rcond=None)[0]
            rec = {'richtung': r_, 's': s, 's_wand': sw, 'w_P_C1_C2_H': zb - zb[0], 'marge': float((G0 + A @ w).min()),
                   'min_s0': float(st['s0'].min())}
            if sk is not None:
                rec.update(rv.kurz(sk))
            n2.append(rec)
    b = np.array([r.get('beta', np.nan) for r in n2])
    j0, j1 = int(np.nanargmin(b)), int(np.nanargmax(b))
    res['N2'] = {'punkte': n2, 'beta_min': float(np.nanmin(b)), 'ort_min': n2[j0], 'beta_max': float(np.nanmax(b)),
                 'ort_max': n2[j1], 'n_beta_neg': int(np.sum(b < 0)), 'n': len(n2),
                 'rms_l2_max': float(np.nanmax([r.get('rms_l2', np.nan) for r in n2])),
                 'nichtkub4_max': float(np.nanmax([r.get('nichtkub4_rms', np.nan) for r in n2]))}
    rv.log('N2 fertig')
    rv.schreiben(aus, res)


if __name__ == '__main__':
    main(sys.argv[1])
