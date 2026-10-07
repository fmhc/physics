#!/usr/bin/env python3
# LIFE-DIAMANT-1, Nachtrag nach dem Hauptlauf (nicht eingefroren, nicht geurteilt):
# Durchgangsprobe der Gleiterkette (Pruefpunkt-Zerlegung, Einzellauf, gleiter_aus, registriere, Drehverhalten, JSON)
# mit einem Kunst-Schritt, weil die echte Suche keinen Gleiter geliefert hat und dieser Codepfad dort nie lief.
# Kunst-Schritt: Knoten mit n3 < 50 ruecken um den Primitivvektor e1 vor (d = (1,0,0), Kunst-"Gleiter" p = 1),
# Knoten mit n3 >= 50 bleiben stehen (Stilleben). Der eingefrorene Code wird nicht veraendert, nur ld.schritt ersetzt.
# Aufruf: nachtrag_pipeline.py <aus.json>
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import life_diamant as ld


def schritt_kunst(live, bmask, smask):
    n1, n2, n3, s = ld.dekodiere(live)
    lauf = n3 < 50
    return np.sort(ld.kodiere(np.where(lauf, n1 + 1, n1), n2, n3, s))


ld.schritt = schritt_kunst
alle_saaten = ld.saaten()
start = []
for k in (0, 16, 32):
    rho, i, live0, ber = alle_saaten[k]
    # Fassung 2: der stehende Teil ist eine andere Saat (k + 1), nicht eine Kopie. Fassung 1 benutzte eine Kopie; der
    # Kunst-Schritt haengt von der Lage ab, beide Haufen hatten dieselbe Kennung, und der Zwischenspeicher nach Kennung
    # (bei echten, verschiebungsgleichen Regeln exakt) gab dem laufenden Haufen das Ergebnis des stehenden.
    n1, n2, n3, s = ld.dekodiere(alle_saaten[k + 1][2])
    fern = ld.kodiere(n1, n2, n3 + 100, s)
    start.append((rho, i, np.sort(np.concatenate((live0, fern))), ber))
# zusaetzlich: reines Laufmuster aus einer anderen Saat (ganzes Muster ist der Gleiter)
start.append(alle_saaten[40])
r = ld.suche_regel(204, start=start)
txt = json.dumps(r)
erwartet = dict(p=1, d_prim=[1, 0, 0], d_kart=[0, 2, 2], richtung='<110>')
ok_gl = [g for g in r['gleiter'] if g['p'] == 1 and g['d_prim'] == [1, 0, 0] and g['d_kart'] == [0, 2, 2]
         and g['richtung'] == '<110>' and g['geprueft'] and abs(g['v_c'] - 2 * 2 ** 0.5 / 3 ** 0.5) < 1e-12]
arten = sorted({g['erste_quelle']['art'] for g in r['gleiter']})
out = dict(regel=r['name'], saat_klassen=r['saat_klassen'], n_gleiter=r['n_gleiter'], gleiter_mit_erwartung=len(ok_gl),
           quellen_arten=arten, objekt_laeufe=r['objekt_laeufe'],
           ende_objekte=[e['ende_objekte'] for e in r['saaten']], pruefpunkt=[e.get('pruefpunkt') for e in r['saaten']],
           dreh12=[g['dreh12'] for g in r['gleiter']], json_bytes=len(txt),
           ok=bool(r['n_gleiter'] >= 2 and len(ok_gl) == r['n_gleiter'] and 'objekt' in arten and 'ganz' in arten))
json.dump(out, open(sys.argv[1], 'w'), indent=1)
print(json.dumps(dict(ok=out['ok'], n_gleiter=out['n_gleiter'], mit_erwartung=out['gleiter_mit_erwartung'],
                      arten=arten, saat_klassen=r['saat_klassen'])))
