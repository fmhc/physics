#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V1-AUFHEBUNG-1, Nachtrag nach Sicht (beschreibend, aendert kein Urteil).

Frage: Folgt der Rest mit V1 auch abseits der Kurve E = T2 (dTT != 0) der TT-Anisotropie, und verschwindet er glatt am
exakten TT-Punkt? Dazu Gewichtspunkte um den exakten Punkt (SKALAR-MISCH-1), verschoben in log10 Sechseck bzw.
log10 Kegel. va.py (eingefroren) wird unveraendert importiert und nur aufgerufen.
Aufruf (nur ueber kleintest.sh auf der .69): python nachtrag_abseits.py --out nachtrag/abseits.json
"""
import argparse, json, os, sys, time, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import va  # noqa: E402  (eingefroren, unveraendert)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    ref = va.lade_ref()
    x0, x1 = ref['smi_F1_exakt']['x']
    punkte = {'exakt': [1.0, 1.0, 10 ** x0, 10 ** x0, 10 ** x1, 10 ** x1]}
    for d in (-0.02, -0.01, -0.005, -0.002, 0.002, 0.005, 0.01, 0.02):
        punkte['S%+.3f' % d] = [1.0, 1.0, 10 ** x0, 10 ** x0, 10 ** (x1 + d), 10 ** (x1 + d)]
    for d in (-0.05, -0.02, 0.02, 0.05):
        punkte['K%+.3f' % d] = [1.0, 1.0, 10 ** (x0 + d), 10 ** (x0 + d), 10 ** x1, 10 ** x1]
    mod, SIG0, vv, kp1 = va.netz()
    ndir, wdir = va.richtungen(10, 20)
    out = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'va_sha256': sha(os.path.abspath(va.__file__))},
           'x_exakt': [x0, x1], 'punkte': punkte, 'kl': {}}
    for kl in (0.005, 0.01):
        gem, per = va.kl_lauf(mod, SIG0, vv, kl, ndir, punkte)
        z = {}
        for nm in punkte:
            if not per[nm]['chol_ok']:
                z[nm] = {'chol_ok': False}
                continue
            r = va.auswerten(ndir, wdir, kl, gem, per[nm])
            st = r['statistik']
            z[nm] = {'chol_ok': True, 'SV1': {k: st['SV1'][k] for k in ('spanne', 'gang', 'fitrest_max', 'min', 'max')},
                     'S_gang': st['S']['gang'], 'TT_gang': st['TT']['gang'], 'TTL_gang': st['TTL']['gang'],
                     'tempo2_spanne': r['tempo2_spanne'], 'c0_quadrat': r['c0_quadrat'], 'lambda_gang_null': r['lambda_gang_null'],
                     'nn_V1_diagnose': r['nn_V1_diagnose']}
        out['kl']['%g' % kl] = z
    out['laufzeit_s'] = time.time() - t0
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_abseits, %.1f s' % out['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
