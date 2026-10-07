#!/usr/bin/env python3
# LIFE-DIAMANT-1, Nachtrag nach dem Hauptlauf (nicht eingefroren, nicht geurteilt):
# Die wegen der Zeitkappe (6 s je Regel) in Stufe 2 uebersprungenen Saaten werden ohne Kappe nachgerechnet,
# Regeln nach Zahl der uebersprungenen Saaten absteigend. Eingefrorener Code unveraendert (nur importiert).
# Aufruf: nachtrag_kappe.py <stufe2.jsonl[,stufe2.jsonl]> <aus.jsonl> <zeitgrenze_s>
import sys, json, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import life_diamant as ld

t0 = time.time()
fertig = set()
if os.path.exists(sys.argv[2]):
    for z in open(sys.argv[2]):
        if z.strip():
            fertig.add(json.loads(z)['index'])
regeln = []
for p in sys.argv[1].split(','):
    for z in open(p):
        if z.strip():
            r = json.loads(z)
            if r['uebersprungen'] > 0 and r['index'] not in fertig:
                regeln.append((r['uebersprungen'], r['index'], r['n_saaten']))
regeln.sort(reverse=True)
st = ld.saaten(stufe=2)
grenze = float(sys.argv[3])
with open(sys.argv[2], 'a') as fh:
    for ueb, idx, n in regeln:
        if time.time() - t0 > grenze:
            print('zeitgrenze erreicht vor regel', idx, flush=True)
            break
        r = ld.suche_regel(idx, start=st[n:], zeitkappe=None, kompakt=True)
        r['nachtrag_kappe'] = dict(ab_saat=n, soll=ueb)
        fh.write(json.dumps(r) + '\n'); fh.flush()
        print(idx, r['name'], 'saaten', r['n_saaten'], 'von', ueb, 'gleiter', r['n_gleiter'], r['saat_klassen'],
              'zeit', r['zeit_s'], flush=True)
print('block fertig', round(time.time() - t0, 1), 's', flush=True)
