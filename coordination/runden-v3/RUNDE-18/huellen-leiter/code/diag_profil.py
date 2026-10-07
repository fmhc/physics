#!/usr/bin/env python3
"""Diagnose (nicht gewertet): Dauer und Newton-Verlauf der Profil-Fortsetzung bei grossem R."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stille3 as S3
import huellen_leiter as HL
pdir, listejson, i = sys.argv[1], sys.argv[2], int(sys.argv[3])
liste = json.load(open(listejson))['w2']
mod = S3.modell_von('M2')
p = S3.lade_profil(HL.ppfad(pdir, liste[i]))
print('profil', liste[i], p['N'], p['rhalf'], 'newton', p['newton'], 'res', p['res'], flush=True)
for frac in (0.125, 0.5):
    w2 = liste[i] + frac * (liste[i - 1] - liste[i])
    t = time.time()
    F, H, ok, hist, res = S3.newton_profil(mod, w2, p['hp'], p['N'], p['F'], p['H'])
    print('newton direkt frac', frac, 'ok', ok, 'it', len(hist), 'hist', ['%.1e' % x for x in hist[:12]], hist[-3:], 'res %.2e' % res, '%.2fs' % (time.time() - t), flush=True)
    t = time.time()
    q = S3.fortsetzung(mod, p, w2, p['hp'], N=p['N'])
    print('fortsetzung frac', frac, q is not None, len(q['newton']) if q else None, '%.2fs' % (time.time() - t), flush=True)
