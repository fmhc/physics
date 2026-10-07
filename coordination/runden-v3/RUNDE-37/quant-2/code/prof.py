#!/usr/bin/env python3
# QUANT-2: Zeitprofil eines Sweeps (Rauchtest, nur Zeitmessung).
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qu2

for name, K in (('kub6', qu2.kubisch(6, 6)), ('netz3', qu2.netz(3, 8, 0.2924, 'dec'))):
    t = time.time(); qu2.vorbereiten(K); tv = time.time() - t
    rng = np.random.default_rng(1)
    th = rng.uniform(-np.pi, np.pi, K.nE)
    print(name, 'nE', K.nE, 'nF', len(K.Pe), 'farben', K.farbe.max() + 1, 'vorbereiten_s', round(tv, 2), flush=True)
    for art in ('hb', 'or'):
        t = time.time()
        for _ in range(5):
            qu2.sweep(K, th, 1.0, rng, art)
        print(' sweep', art, round((time.time() - t) / 5 * 1000, 1), 'ms', flush=True)
    t = time.time()
    for _ in range(5):
        qu2.messen(K, th)
    print(' messen', round((time.time() - t) / 5 * 1000, 1), 'ms', flush=True)
    # Einzelteile eines hb-Sweeps
    tg = tc = tb = tv = 0.0
    for (Pf, Sf, e, s, wf, loc, ed) in K.kl:
        t = time.time(); tf = (Sf * th[Pf]).sum(1); ph = s * tf - th[e]; tg += time.time() - t
        t = time.time(); c = np.cos(ph); sn = np.sin(ph); tc += time.time() - t
        t = time.time(); re = np.bincount(loc, wf * c, minlength=len(ed)); im = np.bincount(loc, wf * sn, minlength=len(ed)); tb += time.time() - t
        t = time.time(); mu = -np.arctan2(im, re); x = rng.vonmises(mu, np.hypot(re, im)); tv += time.time() - t
    print(' teile ms: gather', round(tg * 1000, 1), 'trig', round(tc * 1000, 1), 'bincount', round(tb * 1000, 1), 'vonmises', round(tv * 1000, 1), flush=True)
    sizes = [len(x[2]) for x in K.kl]
    print(' inzidenzen je farbe min/max', min(sizes), max(sizes), flush=True)
