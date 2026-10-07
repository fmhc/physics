#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GLAS-STRAHLUNG-1, Nachtrag nach dem Gegenlesen (B2; beschreibend, aendert kein Urteil).

Frage: Ist der Rest der Kreisbahnen auf V mit V1 (J_iso, kl = 0,01: G = 0,999985 bis 1,000003) k-konvergiert?
Dazu V wie Lauf GV (10 x 20, J_iso), aber kl = 0,005; 0,01; 0,02; 0,04. gs.py (eingefroren) wird unveraendert
importiert; nur in diesem Prozess wird gs.LP durch LP/f ersetzt (kabs = 0,01/LP -> f 0,01/LP). Das aendert auch die
Breite der phi-Klumpen; die phi-Werte dieses Nachtrags sind deshalb nicht vergleichbar und werden nicht ausgegeben.
Kreisbahnen haengen nur ueber kabs von LP ab.
Aufruf: python nachtrag_v_kl.py --out nachtrag/v-kl.json
"""
import argparse, json, os, sys, time, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs  # noqa: E402  (eingefroren, unveraendert)

LP0 = gs.LP


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    dev = gs.dz.geraet()
    out = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'gs_sha256': sha(os.path.abspath(gs.__file__))}, 'kl': {}}
    for f in (0.5, 1.0, 2.0, 4.0):
        gs.LP = LP0 / f
        arg = argparse.Namespace(kabs=0.01, nt=10, nphi=20, rauch=False, rauch_k=2, frist=540.0)
        r = gs.netz_lauf(0, 1, arg, dev, t0)
        aw = gs.netz_auswerten(r)
        z = {'kl': 0.01 * f, 'kabs': r['kabs'], 'G_N_ueber_G': aw['G_N_ueber_G'], 'tempo2_spanne': aw['tempo2_spanne']}
        for k in ('P_P1_SV1_J', 'P_P1_S_J', 'P_P1_TT_J'):
            v = np.array([b[k] for b in aw['bahnen'].values()])
            z[k] = {'min': float(v.min()), 'max': float(v.max()), 'sd': float(v.std(ddof=1)), 'mittel': float(v.mean()),
                    'b001': aw['bahnen']['001'][k], 'b111': aw['bahnen']['111'][k]}
        out['kl']['%g' % (0.01 * f)] = z
    gs.LP = LP0
    out['laufzeit_s'] = time.time() - t0
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_v_kl laufzeit %.1f s' % out['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
