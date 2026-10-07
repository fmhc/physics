#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGIME-K-3 Nachtrag nach Sicht (beschreibend, nicht eingefroren, kein Urteil). Liest die Laufdateien und zaehlt
nur an UNGESPERRTEN Punkten: Maxima der Kontrollgroessen, instabile Gitter- und TT-Eigenwerte getrennt, TT-g je Betrag.
Benutzt die Funktionen ev, test, tt_zuordnung aus dem eingefrorenen rk3.py unveraendert."""
import json, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rk3  # noqa: E402

pfade = sys.argv[1:-1]
out_pfad = sys.argv[-1]
arme = {}
for p in pfade:
    d = json.load(open(p))
    arme.setdefault(d['arm'], {'tau': d['tau'], 'pkt': []})['pkt'].extend(
        [dict(q, _satz=d['satz']) for q in d['punkte']])
res = {}
for arm, A in arme.items():
    tau = A['tau']
    frei = [q for q in A['pkt'] if not q['kontrollen']['sperren']]
    kon = {}
    for key in ('p_err', 'err_max', 's_voll_max', 's_sym', 'eich_max', 'sin_C'):
        v = [q['kontrollen'][key] for q in frei if q['kontrollen'].get(key) is not None]
        kon[key] = float(max(v)) if v else None
    je = {}
    for q in frei:
        E = rk3.eigen(q)
        lab = q.get('betrag_label', 'bz')
        if q['kb'] <= 0.25 and q['_satz'] == 'raster':
            kand, ok = rk3.tt_zuordnung(q, E, tau)
        else:
            kand, ok = [], False
        tts = set(kand) if ok else set()
        n_git = sum(1 for j, e in enumerate(E) if j not in tts)
        n_git_inst = sum(1 for j, e in enumerate(E) if j not in tts and rk3.test(e, 1e-6) == 2)
        n_tt_inst = sum(1 for j in tts if rk3.test(E[j], 1e-6) == 2)
        n_git_stabil = sum(1 for j, e in enumerate(E) if j not in tts and rk3.test(e, 1e-6) == 0)
        x = je.setdefault(lab, {'punkte': 0, 'tt_zuordenbar': 0, 'tt_g_max': 0.0, 'gitter_alle_instabil': 0,
                                'gitter_stabil_min': None, 'gitter_stabil_max': 0, 'tt_inst_verteilung': {},
                                'err_max': 0.0})
        x['punkte'] += 1
        x['tt_zuordenbar'] += int(ok)
        if ok:
            x['tt_g_max'] = max(x['tt_g_max'], max(E[j]['g'] for j in kand))
            x['gitter_alle_instabil'] += int(n_git_inst == n_git)
            x['tt_inst_verteilung'][str(n_tt_inst)] = x['tt_inst_verteilung'].get(str(n_tt_inst), 0) + 1
        x['gitter_stabil_max'] = max(x['gitter_stabil_max'], n_git_stabil)
        x['gitter_stabil_min'] = n_git_stabil if x['gitter_stabil_min'] is None else min(x['gitter_stabil_min'], n_git_stabil)
        x['err_max'] = max(x['err_max'], float(max(q['err'])) if q['err'] else 0.0)
    res[arm] = {'punkte': len(A['pkt']), 'ungesperrt': len(frei), 'kontrollen_ungesperrt_max': kon, 'je_betrag': je}
with open(out_pfad, 'w') as f:
    json.dump(res, f, indent=1)
print('fertig nachtrag', flush=True)
