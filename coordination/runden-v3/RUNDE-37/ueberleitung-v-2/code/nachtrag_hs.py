#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-V-2, Nachtrag nach Sicht (beschreibend, nicht geurteilt, nicht eingefroren).

Anlass: h*_letzt (PLAN 6) liegt bei kl = 0,005 fuer alle drei Richtungen bei 0,0041 bis 0,0042 und faellt darunter
kaum noch. Hier dasselbe Verfahren (uw.lauf_hstern unveraendert) bei kleineren kl = 0,0005; 0,001; 0,002, um zu sehen,
ob h* fuer kl -> 0 gegen einen festen Wert geht. Importiert uw.py (eingefroren) unveraendert; setzt nur die kl-Liste.
"""
import argparse, sys, os, time, platform
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import uw  # noqa: E402
import tg  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--richtung', required=True, choices=['100', '111', '321'])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    uw.HS_KL = [0.0005, 0.001, 0.002]
    erg = uw.lauf_hstern(a.richtung, False)
    res = {'info': {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'skript_sha256': uw.uv.sha(os.path.abspath(__file__)), 'uw_sha256': uw.uv.sha(os.path.abspath(uw.__file__)),
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0))},
           'ergebnis': erg, 'laufzeit_s': time.time() - t0}
    tg.schreibe(a.out, res)
    print('fertig nachtrag_hs', a.richtung, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
