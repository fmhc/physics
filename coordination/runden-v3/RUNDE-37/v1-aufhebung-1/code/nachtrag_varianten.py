#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V1-AUFHEBUNG-1, Nachtrag nach Sicht (beschreibend, aendert kein Urteil).

Frage: Haengt die Aufhebung am exakten TT-Punkt an zwei Festlegungen der Quelle?
  (a) Verteilung der V1-Energie auf die Ecken: baryzentrisch (Hauptlauf) gegen gleich je Ecke (V/nV);
  (b) Bezugspunkt der Bloch-Phase der Spannung: Kantenmitte (Hauptlauf) gegen Anfangsecke der Kante.
va.py (eingefroren) wird unveraendert importiert; die Varianten entstehen nur durch andere Eingaben an va.kl_lauf
(vv bzw. mod['mitte'] in einer Kopie des Modells).
Aufruf (nur ueber kleintest.sh auf der .69): python nachtrag_varianten.py --out nachtrag/varianten.json
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
    punkte = {'J_iso': [va.pn.J_ISO[x] for x in va.ARTEN], 'F1_exakt': list(ref['smi_F1_exakt']['w'])}
    mod, SIG0, vv, kp1 = va.netz()
    vv_gleich = np.full_like(vv, vv.sum() / len(vv))
    mod_anf = dict(mod)
    mod_anf['mitte'] = np.array([np.asarray(mod['pos'][s], float) for (s, s2, n2) in mod['kliste']])
    ndir, wdir = va.richtungen(10, 20)
    varianten = {'haupt': (mod, vv), 'V1_gleich_je_Ecke': (mod, vv_gleich), 'Phase_Anfangsecke': (mod_anf, vv)}
    out = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'va_sha256': sha(os.path.abspath(va.__file__))},
           'vv_baryzentrisch': vv.tolist(), 'vv_gleich': vv_gleich.tolist(), 'kl': {}}
    for kl in (0.005, 0.01):
        z = {}
        for vn, (m_, vv_) in varianten.items():
            gem, per = va.kl_lauf(m_, SIG0, vv_, kl, ndir, punkte)
            z[vn] = {}
            for nm in punkte:
                r = va.auswerten(ndir, wdir, kl, gem, per[nm])
                st = r['statistik']
                z[vn][nm] = {'SV1': {k: st['SV1'][k] for k in ('spanne', 'gang', 'fitrest_max', 'mittel')},
                             'S_gang': st['S']['gang'], 'TT_mittel': st['TT']['mittel'], 'lambda_gang_null': r['lambda_gang_null'],
                             'nn_V1_rest': r['nn_V1_diagnose']['rest_anteil_leistung'], 'lambda_opt': r['nn_V1_diagnose']['lambda_opt']}
        out['kl']['%g' % kl] = z
    out['laufzeit_s'] = time.time() - t0
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_varianten, %.1f s' % out['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
