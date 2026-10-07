#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S6: fuehrt die Zeilen mehrerer `ana.py tab`-Ausgaben (gleiches Gitter, gleiche L und Nt) zu einem Lauf zusammen,
damit ana_s4b.py beta (unveraendert) die Suszeptibilitaetsspitze ueber alle beta-Stufen findet.
Aufruf: merge_tab_s6.py NAME AUS.json TAB1.json [TAB2.json ...]"""
import json
import sys

name, aus = sys.argv[1], sys.argv[2]
zeilen, L, Nt, quellen = [], None, None, []
for p in sys.argv[3:]:
    with open(p) as fh:
        t = json.load(fh)
    for d in t['laeufe']:
        if L is None:
            L, Nt = d['L'], d['Nt']
        if (d['L'], d['Nt']) != (L, Nt):
            raise SystemExit('L/Nt passen nicht: %s' % d['datei'])
        for z in d['zeilen']:
            z = dict(z)
            z['quelle'] = d['datei']
            zeilen.append(z)
        quellen.append(d['datei'])
with open(aus, 'w') as fh:
    json.dump({'laeufe': [{'datei': name, 'L': L, 'Nt': Nt, 'zeilen': zeilen, 'quellen': quellen}]}, fh, indent=1)
print('zusammengefuehrt', name, 'L', L, 'Nt', Nt, 'Zeilen', len(zeilen), 'aus', quellen)
