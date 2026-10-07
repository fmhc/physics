#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TENSOR-EIS-0, Nachtrag NACH dem Einfrieren (kein Urteil, offengelegt in ERGEBNIS.md).

Direkter Fourierraum-Vergleich der pinv-Loesung (Gitter, k = 2 sin(q/2)) mit den Schreibtischformeln der Karte
(mit q -> k) und mit Gl. 17 von Yan u. a. (voller 5x5-Projektor). 20000 zufaellige q in der Brillouin-Zone.
"""
import json, sys, time
import numpy as np
from te0 import basis5, basis6, vek_matrix, skal_zeile, kvek

rng = np.random.default_rng(35)
n = 20000
q = rng.uniform(-np.pi, np.pi, size=(n, 3))
k = kvek(q[:, 0], q[:, 1], q[:, 2])
k2 = (k ** 2).sum(1); kh = k / np.sqrt(k2)[:, None]
I3 = np.eye(3)
B5, B6 = basis5(), basis6()
out = {'n_q': n, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}

Bm = vek_matrix(k, B5); Pv = np.linalg.pinv(Bm)
# 1) Energiekern: |E|^2 = rho^H M rho; Karte: F = K sum rho^*(1/q^2)(delta - qq/4) rho mit F = (K/2) sum |E|^2
M_num = np.einsum('naj,nak->njk', Pv, Pv)
M_karte = (2 / k2)[:, None, None] * (I3 - kh[:, :, None] * kh[:, None, :] / 4)
out['kern_rel_abw_max'] = float((np.abs(M_num - M_karte).max(axis=(1, 2)) / np.abs(M_karte).max(axis=(1, 2))).max())
# 2) explizite Laengsloesung der Karte: E = (i/q^2)[-(q rho^T + rho q^T) + (q.rho)/(2q^2) q q^T + (q.rho)/2 Eins]
rho = rng.normal(size=(n, 3)) + 1j * rng.normal(size=(n, 3))
e = -1j * np.einsum('naj,nj->na', Pv, rho)
E_num = np.einsum('na,aij->nij', e, B5)
kr = (k * rho).sum(1)
E_karte = (1j / k2)[:, None, None] * (-(k[:, :, None] * rho[:, None, :] + rho[:, :, None] * k[:, None, :])
                                      + (kr / (2 * k2))[:, None, None] * k[:, :, None] * k[:, None, :]
                                      + (kr / 2)[:, None, None] * I3)
out['E_formel_rel_abw_max'] = float((np.abs(E_num - E_karte).max(axis=(1, 2)) / np.abs(E_karte).max(axis=(1, 2))).max())
out['E_karte_gauss_rest_max'] = float(np.abs(1j * np.einsum('ni,nij->nj', k, E_karte) - rho).max())
out['E_karte_spur_max'] = float(np.abs(np.einsum('nii->n', E_karte)).max())
# 3) |E|^2 = (2/q^2)(rho^2 - (qdach.rho)^2/4)
E2_num = (np.abs(e) ** 2).sum(1)
E2_karte = (2 / k2) * ((np.abs(rho) ** 2).sum(1) - np.abs((kh * rho).sum(1)) ** 2 / 4)
out['E2_formel_rel_abw_max'] = float((np.abs(E2_num - E2_karte) / E2_karte).max())
# 4) Skalar: Kern 1/k^4 (6 Freiheitsgrade) bzw. 3/(2 k^4) (spurfrei)
m6 = (np.linalg.pinv(skal_zeile(k, B6))[:, :, 0] ** 2).sum(1)
m5 = (np.linalg.pinv(skal_zeile(k, B5))[:, :, 0] ** 2).sum(1)
out['skalar6_k4m_minus1_max'] = float(np.abs(m6 * k2 ** 2 - 1).max())
out['skalar5_k4m_minus_1.5_max'] = float(np.abs(m5 * k2 ** 2 - 1.5).max())
# 5) Gl. 17 (Yan u. a.) als voller Projektor in der 5er-Basis gegen 1 - pinv(Bm) Bm
d = I3; Q = kh
T = (0.5 * (np.einsum('ik,jl->ijkl', d, d) + np.einsum('il,jk->ijkl', d, d))[None]
     + np.einsum('ni,nj,nk,nl->nijkl', Q, Q, Q, Q)
     - 0.5 * (np.einsum('ik,nj,nl->nijkl', d, Q, Q) + np.einsum('jk,ni,nl->nijkl', d, Q, Q)
              + np.einsum('il,nj,nk->nijkl', d, Q, Q) + np.einsum('jl,ni,nk->nijkl', d, Q, Q))
     - 0.5 * np.einsum('nij,nkl->nijkl', d[None] - np.einsum('ni,nj->nij', Q, Q), d[None] - np.einsum('nk,nl->nkl', Q, Q)))
P17 = np.einsum('aij,nijkl,bkl->nab', B5, T, B5)
PT = np.eye(5)[None] - np.einsum('naj,njb->nab', Pv, Bm)
out['Gl17_gegen_Projektor_max_abs'] = float(np.abs(P17 - PT).max())
out['Projektor_idempotent_max_abs'] = float(np.abs(np.einsum('nab,nbc->nac', PT, PT) - PT).max())
out['Projektor_spur_min_max'] = [float(np.einsum('naa->n', PT).min()), float(np.einsum('naa->n', PT).max())]
out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
with open(sys.argv[1] + '.tmp', 'w') as f:
    json.dump(out, f, indent=1)
import os; os.replace(sys.argv[1] + '.tmp', sys.argv[1])
print(json.dumps(out, indent=1))
