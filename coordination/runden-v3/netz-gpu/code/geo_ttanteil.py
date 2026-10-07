# -*- coding: utf-8 -*-
"""Kontrolle zum Datensatz schwerewelle-v: Sind die zwei kleinsten Moden an den k der Superzelle (kl 0,19 bis ~2,5)
TT-artig? Je k: Tensor-Anpassung der Moden (tg.tensor_fit, Eichanteil frei) und TT-Anteil (tp.tt_anteil), Luecke
omega_2^2 / omega_3^2; gewichtet mit der Modenenergie |c_j|^2 des Datensatz-Anfangs (sigma = 1, H zirkular um z).
Synthetisch, linear um flach."""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu import geometrie as geo  # noqa: E402

OUT = sys.argv[1]
N12, SIGMA, X0 = 12, 1.0, np.array([6.0, 6.0, 6.0])
uw, uv, tg = geo._alt()
tp = uw.tp
t0 = time.time()
P = geo.Projekt(2.0 ** -10)
teile = [np.load('/home/fmh/fmhc-physics-remote/netz-gpu/lauf/geo/spek-n12-h10-t%d.npz' % t) for t in (0, 1)]
ks = np.concatenate([z['ks'] for z in teile])
u = np.concatenate([z['u'] for z in teile])
Pv = np.concatenate([z['P'] for z in teile])
w2 = np.concatenate([z['w2'] for z in teile])
mod = P.mod
nHn = np.einsum('ei,ij,ej->e', mod['n'], geo.tensor_H('zirkular_z'), mod['n']) / 2.0
g = np.exp(-0.5 * (ks ** 2).sum(1) * SIGMA ** 2)
qref = g[:, None] * np.exp(1j * ((mod['mitte'] - X0[None, :]) @ ks.T)).T * nHn[None, :]
c = np.einsum('kej,ke->kj', np.conj(Pv), qref)
wgt = np.abs(c) ** 2                                      # Modenenergie je k und Zweig (bis auf Faktor)
wgt = wgt / wgt.sum()
kl = np.linalg.norm(ks, axis=1) * P.lm
tt = np.zeros((len(ks), 2))
rest = np.zeros((len(ks), 2))
for i in range(len(ks)):
    Md = tg.ops(mod, ks[i])[2]
    for j in range(2):
        H, r = tg.tensor_fit(mod, u[i, :, j], ks[i], Md)
        tt[i, j] = tp.tt_anteil(H, ks[i])[0]
        rest[i, j] = r
lu = w2[:, 1] / w2[:, 2]
o = np.argsort(-wgt.sum(1))
cum = np.cumsum(wgt.sum(1)[o])
k99 = o[:int(np.searchsorted(cum, 0.99)) + 1]
out = {'k': len(ks), 'lm': P.lm, 'kl_min_max': [float(kl.min()), float(kl.max())],
       'kl_energiegewichtet': float((wgt.sum(1) * kl).sum()),
       'tt_anteil_energiegewichtet': float((wgt * tt).sum()), 'tensorfit_rest_energiegewichtet': float((wgt * rest).sum()),
       'luecke_energiegewichtet': float((wgt.sum(1) * lu).sum()),
       'k_fuer_99proz_energie': int(len(k99)), 'kl_max_99': float(kl[k99].max()),
       'tt_anteil_min_99': float(tt[k99].min()), 'tensorfit_rest_max_99': float(rest[k99].max()),
       'luecke_max_99': float(lu[k99].max()),
       'w2_positiv_alle': bool((w2[:, :2] > 0).all()), 'w2_3_durch_w2_2_min': float((w2[:, 2] / w2[:, 1]).min())}
bins = [0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]
je = []
for a, b in zip(bins[:-1], bins[1:]):
    m = (kl >= a) & (kl < b)
    if m.any():
        je.append({'kl': [a, b], 'n_k': int(m.sum()), 'energieanteil': float(wgt[m].sum()),
                   'tt_anteil_min': float(tt[m].min()), 'tt_anteil_mittel': float(tt[m].mean()),
                   'tensorfit_rest_max': float(rest[m].max()), 'luecke_max': float(lu[m].max())})
out['je_kl'] = je
out['t_s'] = time.time() - t0
with open(OUT, 'w') as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1), flush=True)
