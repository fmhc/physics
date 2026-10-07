# -*- coding: utf-8 -*-
"""Nachweis: Isotropie der TT-Wellen in der stetigen Grenze (netzgpu.geometrie). Synthetisch, linear um flach.

Je h in (2^-10, 2^-12): Richtungen 'raster13' (tti.richtungen13, wie UEBERLEITUNG-V-2 'V Raster') und 'fib60'
(uw.fib_richtungen(60), wie 'V neu R'), kl in uv.KL_RASTER. Bloecke mit dem Projektcode (CPU), Reduktion und
Eigenzerlegung gebuendelt auf der GPU; CPU-Gegenprobe mit uv.reduktion an allen Punkten.
Spanne wie uv.spanne: je kl max/min - 1 ueber Richtungen und beide TT-Zweige; Spanne0 = Spanne der auf kl -> 0
quadratisch in kl^2 extrapolierten Werte (uv.fit_kl ueber uv.KL_FIT).
"""
import json
import sys
import time

import numpy as np
import torch

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu import geometrie as geo  # noqa: E402

OUT = sys.argv[1]
uw, uv, tg = geo._alt()
HS = [2.0 ** -10, 2.0 ** -12]
KL = list(uv.KL_RASTER)
KLF = list(uv.KL_FIT)


def log(*a):
    print(time.strftime('%H:%M:%S'), *a, flush=True)


def spanne(W, OK):
    """W (nd, nkl, 2), OK (nd, nkl) -> wie uv.spanne (Variante a)."""
    je = {}
    for j, kl in enumerate(KL):
        ww = np.where(OK[:, j, None], W[:, j, :], np.nan)
        je['%g' % kl] = {'spanne': float(np.nanmax(ww) / np.nanmin(ww) - 1), 'n_ok': int(OK[:, j].sum())}
    jf = [KL.index(x) for x in KLF]
    w0, alle_ok = [], True
    for i in range(W.shape[0]):
        alle_ok &= bool(OK[i, jf].all())
        for b in range(2):
            w0.append(uv.fit_kl(KLF, W[i, jf, b])[0])
    w0 = np.array(w0)
    return {'spanne0': float(w0.max() / w0.min() - 1), 'alle_ok_fit': bool(alle_ok), 'w0_min': float(w0.min()),
            'w0_max': float(w0.max()), 'je_kl': je, '_w0': w0}


out = {'torch': torch.__version__, 'gpu': torch.cuda.get_device_name(0), 'start': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
       'h': HS, 'kl': KL, 'kl_fit': KLF, 'je_h': {}}
mengen = {'raster13': [d for _, d in uw.tti.richtungen13()], 'fib60': list(uw.fib_richtungen(60))}
for h in HS:
    t0 = time.time()
    P = geo.Projekt(h)
    z = {'t_projekt_s': time.time() - t0, 'lm': P.lm}
    ks, tags = [], []
    for nm, ds in mengen.items():
        for i, d in enumerate(ds):
            for j, kl in enumerate(KL):
                ks.append((kl / P.lm) * np.asarray(d, float))
                tags.append((nm, i, j))
    ks = np.array(ks)
    bl = P.bloecke_viele(ks, log=log, alle=100)
    z['t_bloecke_s'] = bl['t_s']
    z['t_bloecke_je_k_s'] = bl['t_s'] / len(ks)
    z['bloecke_gruende'] = bl['gruende']
    torch.cuda.synchronize()
    t1 = time.time()
    sp = geo.reduktion_gpu(bl, ks)
    torch.cuda.synchronize()
    z['t_red_gpu_s'] = time.time() - t1
    z['t_red_gpu_je_k_s'] = z['t_red_gpu_s'] / len(ks)
    t1 = time.time()
    cpu = geo.reduktion_cpu(P, bl, ks, range(len(ks)))
    z['t_red_cpu_je_k_s'] = (time.time() - t1) / len(ks)
    g = sp['w2k2'].cpu().numpy()
    okg = sp['tt_ok'].cpu().numpy()
    dif = [float(np.abs(np.array(c) - gg).max()) for c, gg in zip(cpu, g) if c is not None]
    z['gpu_gegen_cpu_abs_max'] = float(max(dif))
    z['cpu_none'] = int(sum(1 for c in cpu if c is None))
    z['n_wachsend_max'] = int(sp['n_wachsend'].max())
    z['n_neg_Meff'] = sorted(set(sp['n_neg'].cpu().tolist()))
    z['n_null_Meff_max'] = int(sp['n_null'].max())
    z['luecke_max'] = float(sp['luecke'].max())
    z['gueltig'] = int(sp['gueltig'].sum())
    z['k'] = len(ks)
    for nm, ds in mengen.items():
        nd = len(ds)
        W = np.zeros((nd, len(KL), 2))
        Wc = np.zeros((nd, len(KL), 2))
        OK = np.zeros((nd, len(KL)), bool)
        for r, (m_, i, j) in enumerate(tags):
            if m_ != nm:
                continue
            W[i, j] = g[r]
            OK[i, j] = okg[r]
            Wc[i, j] = cpu[r] if cpu[r] is not None else np.nan
        s = spanne(W, OK)
        sc = spanne(Wc, OK)
        w0 = s.pop('_w0')
        sc.pop('_w0')
        s['spanne0_cpu'] = sc['spanne0']
        s['eins_minus_w0_durch_h2'] = [float((1 - w0.max()) / h ** 2), float((1 - w0.min()) / h ** 2)]
        for kl in (0.05, 0.1):
            j = KL.index(kl)
            s['tempo_kl_%g' % kl] = [float(W[:, j, :].min()), float(W[:, j, :].max())]
            s['doppelbrechung_kl_%g_max' % kl] = float(np.max(W[:, j, 1] / W[:, j, 0] - 1))
        z[nm] = s
        log(h, nm, 'spanne0 %.4e (cpu %.4e)' % (s['spanne0'], sc['spanne0']), 'kl0.05 %.3e' % s['je_kl']['0.05']['spanne'],
            'kl0.1 %.3e' % s['je_kl']['0.1']['spanne'])
    out['je_h']['%g' % h] = z
    with open(OUT, 'w') as fh:
        json.dump(out, fh, indent=1)
a, b = out['je_h']['%g' % HS[0]], out['je_h']['%g' % HS[1]]
out['vergleich'] = {}
proj = {'raster13': (1.25e-6, 7.8e-8), 'fib60': (1.98e-6, 1.2e-7)}
for nm in mengen:
    out['vergleich'][nm] = {'spanne0_h10': a[nm]['spanne0'], 'spanne0_h12': b[nm]['spanne0'],
                            'faktor': a[nm]['spanne0'] / b[nm]['spanne0'],
                            'projekt_h10_h12': list(proj[nm]),
                            'rel_abw_h10': a[nm]['spanne0'] / proj[nm][0] - 1, 'rel_abw_h12': b[nm]['spanne0'] / proj[nm][1] - 1,
                            'h2_rest_extrapoliert': (16 * b[nm]['spanne0'] - a[nm]['spanne0']) / 15,
                            'faktor_kl_0.05': a[nm]['je_kl']['0.05']['spanne'] / b[nm]['je_kl']['0.05']['spanne'],
                            'faktor_kl_0.1': a[nm]['je_kl']['0.1']['spanne'] / b[nm]['je_kl']['0.1']['spanne']}
out['gpu_max_MB'] = torch.cuda.max_memory_allocated() / 1e6
out['ende'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
with open(OUT, 'w') as fh:
    json.dump(out, fh, indent=1)
log(json.dumps(out['vergleich'], indent=1))
