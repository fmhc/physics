#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGIME-K-3 Nachtrag 2 nach dem Gegenlesen (GL-3; beschreibend, nicht eingefroren, kein Urteil).
Vergleicht an UNGESPERRTEN Rasterpunkten die unverfeinerten Transfermatrix-Eigenwerte zT mit den nachgeschaerften z:
max relativer Abstand (TT und alle), und delta aus zT gegen delta aus z fuer die TT-Eigenwerte, je Betrag.
Dazu K6 mit zT statt z (Abstand der REGIME-K-2-Nullstellen zum naechsten zT)."""
import json, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rk3  # noqa: E402

args = sys.argv[1:-1]
out_pfad = sys.argv[-1]
lauf = [a for a in args if not a.startswith('ref=')]
refs = [a[4:] for a in args if a.startswith('ref=')]
arme = {}
for p in lauf:
    d = json.load(open(p))
    if d['satz'] != 'raster':
        continue
    arme.setdefault(d['arm'], {'tau': d['tau'], 'pkt': []})['pkt'].extend(d['punkte'])
res = {}
for arm, A in arme.items():
    tau = A['tau']
    je = {}
    for q in A['pkt']:
        if q['kontrollen']['sperren']:
            continue
        z = np.array(q['z_re']) + 1j * np.array(q['z_im'])
        zT = np.array(q['zT_re']) + 1j * np.array(q['zT_im'])
        E = rk3.eigen(q)
        kand, ok = rk3.tt_zuordnung(q, E, tau)
        rel = np.abs(z - zT) / np.abs(z)
        x = je.setdefault(q['betrag_label'], {'punkte': 0, 'rel_alle_max': 0.0, 'rel_tt_max': 0.0,
                                               'delta_tt_max_z': 0.0, 'delta_tt_max_zT': 0.0,
                                               'abs_ddelta_tt_max': 0.0})
        x['punkte'] += 1
        x['rel_alle_max'] = max(x['rel_alle_max'], float(rel.max()))
        if ok:
            for j in kand:
                dz, dT = abs(np.angle(z[j])), abs(np.angle(zT[j]))
                x['rel_tt_max'] = max(x['rel_tt_max'], float(rel[j]))
                x['delta_tt_max_z'] = max(x['delta_tt_max_z'], float(dz))
                x['delta_tt_max_zT'] = max(x['delta_tt_max_zT'], float(dT))
                x['abs_ddelta_tt_max'] = max(x['abs_ddelta_tt_max'], float(abs(dz - dT)))
    res[arm] = je
k6 = {}
for r in refs:
    R = json.load(open(r))
    arm = R['gitter']
    mine = {q['richtung']: q for q in arme.get(arm, {}).get('pkt', [])
            if q['art'] == 'koord' and abs(q['eingabe'] - 0.05) < 1e-12}
    m, n, gesp = 0.0, 0, 0
    for q in R['punkte']:
        p = mine.get(q['richtung'])
        if p is None:
            continue
        if p['kontrollen']['sperren']:
            gesp += 1
        zT = np.array(p['zT_re']) + 1j * np.array(p['zT_im'])
        for w in q['nullstellen']:
            zr = np.exp(-complex(w['re'], w['im']) * R['tau'])
            m = max(m, float(np.min(np.abs(zT - zr)) / abs(zr)))
            n += 1
    k = k6.setdefault(arm, {'max_rel_zT': 0.0, 'nullstellen': 0, 'gesperrte_punkte': 0})
    k['max_rel_zT'] = max(k['max_rel_zT'], m); k['nullstellen'] += n; k['gesperrte_punkte'] += gesp
with open(out_pfad, 'w') as f:
    json.dump({'je_arm_betrag': res, 'K6_mit_zT': k6}, f, indent=1)
print('fertig nachtrag2', flush=True)
