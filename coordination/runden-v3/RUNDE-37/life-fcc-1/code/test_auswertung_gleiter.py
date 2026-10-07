#!/usr/bin/env python3
# LIFE-FCC-1: Test des Gleiterpfads von auswertung.py VOR deren Einfrieren (nur Rauchdaten, keine Hauptergebnisse).
# Ersetzt in einer Kopie der Rauchdatei die Regeln 0 und 355 durch Kunst-Laeufe (Kunst-Schritt aus life_fcc, p = 1 und
# p = 3), damit auswertung.py Gleiterliste, Uebersicht, Geschwindigkeitsbild und 3D-Bildfolge einmal durchlaeuft.
# Aufruf: test_auswertung_gleiter.py <rauch.jsonl> <aus.jsonl>
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import life_fcc as lf

s1 = lf.saaten(1)
dicht = [s for s in s1 if s[0] == lf.PARAM['dichten'][-1]]
ersatz = {}
for idx, R, tv in [(0, np.eye(3, dtype=np.int64), (1, 1, 0)), (355, np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]), (1, 1, 0))]:
    r = lf.suche_regel(idx, dicht[:2], lf.PARAM['W1'], lf.PARAM['W1_obj'], sf=lf.kunst_schritt(R, tv), name='Kunst-%d' % idx)
    r['stufe'] = 1
    ersatz[idx] = r
with open(sys.argv[2], 'w') as fh:
    for z in open(sys.argv[1]):
        if z.strip():
            r = json.loads(z)
            fh.write(json.dumps(ersatz.get(r['index'], r)) + '\n')
print(json.dumps({k: [v['n_gleiter'], v['n_bahnen']] for k, v in ersatz.items()}))
