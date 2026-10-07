#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SCHWERE-MASSE-V: Zusammenfassung (liest lauf/*.json, rechnet abgeleitete Groessen, schreibt lauf/zusammenfassung.json).
Aufruf nur ueber kleintest.sh auf der .69: python code/zf.py lauf lauf/zusammenfassung.json
"""
import json, glob, math, os, sys, hashlib

D, AUS = sys.argv[1], sys.argv[2]


def lade(p):
    with open(p) as f:
        return json.load(f)


zeilen = []
for p in sorted(glob.glob(os.path.join(D, 'qb-o*.json')) + glob.glob(os.path.join(D, 'qbz*.json'))):
    d = lade(p)
    l, k = d['loesung'], d['kontinuum']
    nm = os.path.basename(p)
    zentrum = 'C1'
    if nm.startswith('qbz0'):
        zentrum = 'P0'
    elif nm.startswith('qbz6'):
        zentrum = 'H0'
    h = d['h']
    z = {'datei': nm, 'zentrum': zentrum, 'om': d['om_kont'], 'h': h, 'L': d['L'], 'N': d['N'],
         'R_halb_lP': k['r_halb'] / h, 'a_durch_R': h / k['r_halb'], 'bind_gitter': l['bind'], 'bind_kont': k['bind'],
         'E': l['E'], 'E_kont': k['E'], 'Q': l['Q'], 'om_gitter': l['om'], 'S': l['S'], 'S_rel': l['S_rel'],
         'S_start_rel': d['start']['S_rel'], 'brutto_rel': l['brutto_s_rel'], 'brutto_pos_rel': l['brutto_s_pos_rel'],
         'dE_rel': (l['E'] - k['E']) / k['E'], 'minus2dE_durch_S': -2.0 * (l['E'] - k['E']) / l['S'] if l['S'] != 0 else None,
         'resid_rel': l['resid_rel'], 'rand_anteil': l['rand_anteil'], 'c_h2': l['S_rel'] / h ** 2,
         'c_R2': l['S_rel'] / (h / k['r_halb']) ** 2, 'nit': d['minimierer']['nit'], 'status': d['minimierer']['status'],
         'zeitstopp': d['minimierer']['zeitstopp']}
    zeilen.append(z)
# lokale Exponenten im h-Gang (nur Zentrum C1)
exponenten = {}
for om in sorted(set(z['om'] for z in zeilen)):
    zz = sorted([z for z in zeilen if z['om'] == om and z['zentrum'] == 'C1'], key=lambda z: -z['h'])
    ex = []
    for a, b in zip(zz[:-1], zz[1:]):
        if a['S_rel'] > 0 and b['S_rel'] > 0:
            ex.append({'h_von': a['h'], 'h_bis': b['h'], 'p': math.log(a['S_rel'] / b['S_rel']) / math.log(a['h'] / b['h'])})
        else:
            ex.append({'h_von': a['h'], 'h_bis': b['h'], 'p': None})
    fein = [z for z in zz if z['h'] <= 0.8 + 1e-9 and z['S_rel'] > 0]
    fit = None
    if len(fein) >= 2:
        xs = [math.log(z['h']) for z in fein]
        ys = [math.log(z['S_rel']) for z in fein]
        n = len(xs)
        mx, my = sum(xs) / n, sum(ys) / n
        sxx = sum((x - mx) ** 2 for x in xs)
        p = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
        c = math.exp(my - p * mx)
        rest = max(abs(y - (math.log(c) + p * x)) for x, y in zip(xs, ys))
        fit = {'h_bereich': [min(z['h'] for z in fein), max(z['h'] for z in fein)], 'n': n, 'p': p, 'c': c,
               'max_log_rest': rest}
    exponenten[str(om)] = {'lokal': ex, 'fit_h_le_0.8': fit}
# Takt
takt = {}
for p in sorted(glob.glob(os.path.join(D, 'takt-*.json'))):
    d = lade(p)
    bmain = 'band_%g_%g' % tuple(d['band_lP'])
    t = {'LT': d['LT'], 'band': d['band_lP'], 'P_lmin_rel_min': d['P_lmin_rel_min'], 'imag_rel': d['imag_rel'], 'quellen': {}}
    for nm, q in d['quellen'].items():
        info = q['info']
        e = {'summe': info['summe'], 'M_schwer': q[bmain]['M_schwer'], 'M_durch_summe': q[bmain]['M_durch_summe'],
             'rms_rel': q[bmain]['rms_rel'],
             'M_durch_summe_alle_baender': [q[b]['M_durch_summe'] for b in q if b.startswith('band_')]}
        if 'E' in info:
            e['M_durch_E'] = q[bmain]['M_schwer'] / info['E']
            e['S_durch_E'] = info['S'] / info['E']
            e['bind'] = (info['Q'] - info['E']) / info['E']
        t['quellen'][nm] = e
    takt[os.path.basename(p)] = t
out = {'zeilen': zeilen, 'exponenten': exponenten, 'takt': takt}
with open(AUS + '.tmp', 'w') as f:
    json.dump(out, f, indent=1)
os.replace(AUS + '.tmp', AUS)
print('%-22s %-3s %5s %5s %4s %7s %7s %8s %10s %10s %10s %8s %8s %9s' % ('datei', 'z', 'om', 'h', 'L', 'R_lP', 'a/R', 'bind',
                                                                         'E', 'S/E', 'S0/E', '-2dE/S', 'brutto', 'resid'))
for z in sorted(zeilen, key=lambda z: (z['zentrum'], z['om'], -z['h'])):
    print('%-22s %-3s %5.2f %5.2f %4d %7.3f %7.4f %8.5f %10.4f %10.3e %10.3e %8.4f %8.4f %9.2e' % (
        z['datei'][:22], z['zentrum'], z['om'], z['h'], z['L'], z['R_halb_lP'], z['a_durch_R'], z['bind_gitter'], z['E'],
        z['S_rel'], z['S_start_rel'], z['minus2dE_durch_S'] if z['minus2dE_durch_S'] is not None else float('nan'),
        z['brutto_rel'], z['resid_rel']))
print(json.dumps(exponenten, indent=1))
for tn, t in takt.items():
    print(tn, 'LT', t['LT'], 'band', t['band'], 'P_lmin', t['P_lmin_rel_min'], 'imag', t['imag_rel'])
    for nm, e in t['quellen'].items():
        print('  %-24s summe %12.6f  M %12.6f  M/summe %.7f  M/E %s  S/E %s  bind %s  rms %.1e  alle %s' % (
            nm, e['summe'], e['M_schwer'], e['M_durch_summe'], ('%.6f' % e['M_durch_E']) if 'M_durch_E' in e else '-',
            ('%.6f' % e['S_durch_E']) if 'S_durch_E' in e else '-', ('%.4f' % e['bind']) if 'bind' in e else '-',
            e['rms_rel'], ' '.join('%.6f' % x for x in e['M_durch_summe_alle_baender'])))
print('zf.py sha256', hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest())
