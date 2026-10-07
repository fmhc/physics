#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ANTIGRAVITY-NACHBAU-1: die acht Antigravity-Skripte unveraendert ausfuehren und Ausgabe festhalten (CPU)."""
import json, os, subprocess, sys, time, hashlib

HIER = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(os.path.dirname(HIER), 'ag-original')
SKRIPTE = ['unimodular_pachner.py', 'ribbon_frustration.py', 'quantum_rotor_witness.py', 'generationen_dimensionen.py',
           'higgs_masse_hierarchie.py', 'gravity_nearfield_collapse.py', 'kollaps_szenarien.py', 'dirac_gitter_gpu.py']
out = {}
for s in SKRIPTE:
    p = os.path.join(ORIG, s)
    t0 = time.time()
    args = [sys.executable, p] + (['--L', '2', '--out', os.path.join(ORIG, 'dirac_spektrum.json')] if s.startswith('dirac') else [])
    try:
        r = subprocess.run(args, cwd=ORIG, capture_output=True, text=True, timeout=120)
        out[s] = {'rc': r.returncode, 'stdout': r.stdout[-6000:], 'stderr': r.stderr[-3000:]}
    except subprocess.TimeoutExpired:
        out[s] = {'rc': None, 'timeout': True}
    out[s]['sha256'] = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    out[s]['t_s'] = time.time() - t0
with open(sys.argv[1], 'w') as fh:
    json.dump(out, fh, indent=1)
print('fertig', flush=True)
