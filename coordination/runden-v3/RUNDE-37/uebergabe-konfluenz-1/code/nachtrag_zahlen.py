#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERGABE-KONFLUENZ-1, Nachtrag nach Sicht (nur Zusammenfassung vorhandener Zahlen, kein Urteil).
Liest lauf/auswertung.json und nachtrag/auswertung-nt.json (eingefroren erzeugt) sowie lauf/konfluenz-s*.json und
nachtrag/konfluenz-s*.json; gibt Median und Maximum von Delta_H gesamt je Form, Lesart, Skalar-Amplitude und die
Skalar-Kontrollen (Summe *0 / V, kleinstes *0 relativ, negative *0) aus. Aufruf: nachtrag_zahlen.py <out.json>"""
import json, glob, sys, os
import numpy as np


def dh(aw):
    d = json.load(open(aw))['ergebnis']
    out = {}
    for form in ('A1', 'A2'):
        for les in ('R', 'P'):
            for amp in ('0', '0.001', '0.01'):
                v = [z[form][les]['d_H_gesamt_rel'][amp] for z in d['zeilen'] if les in z.get(form, {})]
                if v:
                    out['%s-%s-%s' % (form, les, amp)] = {'n': len(v), 'median': float(np.median(v)), 'max': float(np.max(v))}
    return out


def sk(muster):
    s0v, s0min, neg = [], [], []
    for p in sorted(glob.glob(muster)):
        for f in json.load(open(p))['ergebnis']['faelle']:
            k = f.get('skalar_kontrolle')
            if k:
                s0v.append(abs(k['s0_durch_V_anfang'] - 1.0))
                s0min.append(k['s0_min_rel_alle'])
                neg.append(k['stern0_n_neg_max'])
    return {'n': len(s0v), 'abw_summe_s0_durch_V_max': float(max(s0v)), 's0_min_rel_min': float(min(s0min)),
            'stern0_neg_max': int(max(neg))}


res = {'haupt': {'d_H_gesamt': dh('lauf/auswertung.json'), 'skalar': sk('lauf/konfluenz-s*.json')},
       'nachtrag_T': {'d_H_gesamt': dh('nachtrag/auswertung-nt.json'), 'skalar': sk('nachtrag/konfluenz-s*.json')}}
with open(sys.argv[1] + '.tmp', 'w') as fh:
    json.dump(res, fh, indent=1)
os.replace(sys.argv[1] + '.tmp', sys.argv[1])
print('fertig nachtrag_zahlen', flush=True)
