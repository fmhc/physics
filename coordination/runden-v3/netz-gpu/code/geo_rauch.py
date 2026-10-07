# -*- coding: utf-8 -*-
"""Rauchtest netzgpu.geometrie: Zeiten je k, k <-> -k, GPU-Reduktion gegen uv.reduktion, Zuordnung zu netz.py
(Eichkern, Regge-Defizit per Differenzenquotient). Synthetisch, linear um flach."""
import json
import sys
import time

import numpy as np
import torch

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu.netz import Netz  # noqa: E402
from netzgpu import geometrie as geo  # noqa: E402

OUT = sys.argv[1]
out = {'torch': torch.__version__, 'gpu': torch.cuda.get_device_name(0), 'start': time.strftime('%Y-%m-%dT%H:%M:%S%z')}
fr, tot = torch.cuda.mem_get_info()
out['gpu_frei_MB'] = fr / 1e6


def log(*a):
    print(*a, flush=True)


t0 = time.time()
P = geo.Projekt(2.0 ** -10)
out['t_projekt_s'] = time.time() - t0
out['lm'] = P.lm
log('Projekt', out['t_projekt_s'], P.lm)
uw, uv, tg = geo._alt()
R13 = dict(uw.tti.richtungen13())
ks = [(0.05 / P.lm) * R13['100'], (0.05 / P.lm) * R13['111'], (0.05 / P.lm) * R13['321'], -(0.05 / P.lm) * R13['321'],
      np.array([1.3, -0.7, 2.1]), np.array([-1.3, 0.7, -2.1])]
ks = np.array(ks)
tz = []
bl = None
t0 = time.time()
bl = P.bloecke_viele(ks)
out['t_bloecke_je_k_s'] = bl['t_s'] / len(ks)
log('bloecke je k', out['t_bloecke_je_k_s'])
out['konj_M'] = float(np.abs(bl['M'][3] - np.conj(bl['M'][2])).max() / np.abs(bl['M'][2]).max())
out['konj_M_bz'] = float(np.abs(bl['M'][5] - np.conj(bl['M'][4])).max() / np.abs(bl['M'][4]).max())
out['konj_B'] = float(np.abs(bl['B'][5] - np.conj(bl['B'][4])).max() / np.abs(bl['B'][4]).max())
torch.cuda.synchronize()
t0 = time.time()
sp = geo.reduktion_gpu(bl, ks)
torch.cuda.synchronize()
out['t_red_gpu_6k_s'] = time.time() - t0
cpu = geo.reduktion_cpu(P, bl, ks, range(len(ks)))
g = sp['w2k2'].cpu().numpy()
out['w2k2_gpu'] = g.tolist()
out['w2k2_cpu'] = [x for x in cpu]
out['gpu_gegen_cpu_rel'] = float(max(np.abs(np.array(c) - gg).max() / np.abs(gg).max() for c, gg in zip(cpu, g) if c is not None))
out['n_neg'] = sp['n_neg'].cpu().tolist()
out['luecke'] = sp['luecke'].cpu().tolist()
out['gueltig'] = sp['gueltig'].cpu().tolist()
out['w2_alle_k0'] = sp['w2'][0].cpu().tolist()
log(json.dumps({k: out[k] for k in ('konj_M', 'konj_M_bz', 'konj_B', 'gpu_gegen_cpu_rel', 't_red_gpu_6k_s')}))
# Buendel-Zeit: 512 Kopien
blv = {x: np.repeat(bl[x][:1], 512, 0) for x in ('M', 'B', 'c', 'Md')}
blv['ok'] = np.ones(512, bool)
torch.cuda.synchronize()
t0 = time.time()
sp2 = geo.reduktion_gpu(blv, np.repeat(ks[:1], 512, 0))
torch.cuda.synchronize()
out['t_red_gpu_je_k_512_s'] = (time.time() - t0) / 512
out['gpu_max_MB'] = torch.cuda.max_memory_allocated() / 1e6
# Zuordnung auf Netz n = 2 und 4
for n in (2, 4):
    N = Netz('V', (n, n, n))
    gi = geo.KGitter(n)
    zo = geo.NetzZuordnung(P, N)
    z = {'K_halb': gi.K, 'K_voll': gi.K_voll, 'n_selbst': gi.n_selbst, 'zuordnung': zo.info()}
    z['eichkern'] = geo.pruefe_eichkern(P, zo, gi, n_k=min(gi.K, 24))
    # Regge: zufaellige F (K,E) -> q, Bq real
    rng = np.random.default_rng(7)
    F = rng.normal(size=(gi.K, P.E)) + 1j * rng.normal(size=(gi.K, P.E))
    F *= np.exp(-0.5 * (gi.ks ** 2).sum(1))[:, None]
    BF = np.zeros_like(F)
    for i in range(gi.K):
        Bs = tg.ops(P.mod, gi.ks[i])[0]
        BF[i] = uv.herm(Bs.toarray()) @ F[i]
    x = zo.synthese(np.stack([F, BF], -1), gi.ks)
    q, Bq = x[:, 0], x[:, 1]
    q = q / q.abs().max()
    Bq = Bq / x[:, 0].abs().max()
    z['regge'] = geo.pruefe_regge(N, q, Bq)
    # Energie-Parseval: sum_j q_j Bq_j gegen 2 N_c sum_k Re(F^H B F)
    z['parseval_rel'] = float(abs(float((x[:, 0] * x[:, 1]).sum()) - 2 * zo.N_c * float(np.real(np.einsum('ke,ke->', np.conj(F), BF))))
                              / abs(float((x[:, 0] * x[:, 1]).sum())))
    out['netz_%d' % n] = z
    log(n, json.dumps(z))
out['ende'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
with open(OUT, 'w') as fh:
    json.dump(out, fh, indent=1)
log('fertig')
