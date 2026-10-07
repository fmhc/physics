#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GLAS-STRAHLUNG-1, Nachtrag nach Sicht (beschreibend, aendert kein Urteil).

Anlass (Sicht 09:5x CEST): Auf V (J_iso) heben sich fuer Kreisbahnen nn-Leck und V1 fast auf, und das L-Leck ist null;
auf dem Glas (J = 1) nicht. Frage: Liegt der Unterschied an den Bewegungsgewichten (J_iso gegen J = 1) oder an der
Unordnung? Dazu V mit J = 1 je Tetraeder, sonst wie Lauf GV (10 x 20, kl = 0,01). gs.py (eingefroren) wird
unveraendert importiert; nur in diesem Prozess wird gs.J_ISO durch J = 1 fuer alle Arten ersetzt.
Aufruf: python nachtrag_v_j1.py --out nachtrag/v-j1.json
"""
import argparse, json, os, sys, time, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gs  # noqa: E402  (eingefroren, unveraendert)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    gs.J_ISO = {k: 1.0 for k in gs.J_ISO}
    arg = argparse.Namespace(kabs=0.01, nt=10, nphi=20, rauch=False, rauch_k=2, frist=540.0)
    dev = gs.dz.geraet()
    r = gs.netz_lauf(0, 1, arg, dev, t0)
    aw = gs.netz_auswerten(r)
    G = {nm: {k: b[k] for k in ('summe_m4', 'P_P1_TT_J', 'P_P1_TTL_J', 'P_P1_S_J', 'P_P1_SV1_J', 'K_P1_SV1_J', 'P_P1_SV1_ohneJ')}
         for nm, b in aw['bahnen'].items()}
    out = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'gs_sha256': sha(os.path.abspath(gs.__file__))},
           'J': 'eins (alle Tetraeder-Arten 1)', 'c0_quadrat': aw['c0_quadrat'], 'tempo2_spanne': aw['tempo2_spanne'],
           'G_N_ueber_G': aw['G_N_ueber_G'], 'kontrollen': aw['kontrollen'], 'phi': aw['phi'], 'bahnen': G}
    for k in ('P_P1_TT_J', 'P_P1_TTL_J', 'P_P1_S_J', 'P_P1_SV1_J', 'K_P1_SV1_J'):
        v = np.array([b[k] for b in G.values()])
        out['lagen_' + k] = {'mittel': float(v.mean()), 'sd': float(v.std(ddof=1)), 'min': float(v.min()), 'max': float(v.max())}
    out['laufzeit_s'] = time.time() - t0
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_v_j1 laufzeit %.1f s' % out['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
