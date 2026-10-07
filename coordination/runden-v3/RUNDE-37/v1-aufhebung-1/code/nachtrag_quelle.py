#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IMPULS-NETZ-1, Nachtrag nach Sicht (beschreibend, aendert kein Urteil).

Frage: Haengt der Rest des Lecks mit Impulskopplung (H1: S+J 1,021 / 1,011 / 0,971) an der Gitterfeinstruktur der
phi-Quelle (w = d = 0,8 l_P, also Klumpen von Gitterkantengroesse)? Die kompakte Grenze mit affinem Spannungsmuster
(Z1, kreisbahnen phi_*) gab 0,991 / 1,007 / 1,004. Gerechnet: dieselbe Quelle mit w = d = 1,6 und 2,0 l_P.
inz.py, pn.py, ew.py, mn.py, tp.py, nachtrag_iso.py unveraendert importiert (eingefroren 2026-10-05 07:46:10).
Aufruf: python nachtrag_quelle.py --out nachtrag/quelle.json
"""
import argparse, json, sys, time, platform, os, resource, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inz  # noqa: E402


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'host': platform.node(), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)), 'inz_sha256': sha(os.path.abspath(inz.__file__))}
    out = {'info': info, 'laeufe': {}}
    for w in (1.6, 2.0):
        r = inz.lauf(nt=8, nphi=16, w_lP=w, d_lP=w)
        out['laeufe']['w_%g' % w] = {'G_rad_ueber_G_N_kl001': r['G_rad_ueber_G_N_kl001'], 'quellen': r['quellen'],
                                      'G_N_ueber_G': r['G_N_ueber_G'], 'zeiten_s': r['zeiten_s'],
                                      'kontrollen': {k: r['kontrollen'][k] for k in ('cM_rel_max', 'MB_rel_max', 'KJ_MhPMsig_rel_max', 'chol_ok', 'rang_MC')},
                                      'tabelle_iso': {q: [{k: z[k] for k in ('kl', 'P_V1S_ueber_P_E', 'P_SJ_ueber_P_E', 'P_V1SJ_ueber_P_E', 'A_R')}
                                                          for z in zeilen if z['kl'] <= 0.3] for q, zeilen in r['tabelle']['iso'].items()}}
    out['laufzeit_s'] = time.time() - t0
    out['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(out, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_quelle laufzeit %.1f s' % out['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
