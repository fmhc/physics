#!/usr/bin/env python3
"""DIM-LEITER-QBALL-1, nach dem Einfrieren geschrieben, nur beschreibend [D] (kein Urteil):
- Wachstumsfaktoren Q_min(D)/Q_min(D-1) und Q_s(D)/Q_s(D-1);
- Virial-Identitaet [M]: E = omega Q + (2/D) G (G = Int |grad f|^2), also E/Q - omega = 2G/(D Q); Probe am Gitter;
- Richardson-Werte (4 fein - grob)/3 fuer Q_min und Q_s.
Aufruf ueber kleintest.sh: beschreibung.py <auswertung.json> <d1.json> ... <d12.json>
"""
import json
import sys

with open(sys.argv[1]) as fh:
    A = json.load(fh)
tab = {z['D']: z for z in A['tabelle']}
daten = {}
for p in sys.argv[2:]:
    with open(p) as fh:
        daten.update(json.load(fh)['ergebnisse'])
print('D | Q_min fein | Q_min Richardson | Faktor Q_min | Q_s fein | Q_s Richardson | Faktor Q_s | 1 - omega_s')
pm = ps = None
for D in sorted(tab):
    z = tab[D]
    qm, qmg = z['Q_min'], z['Q_min_grob']
    qmr = (4.0 * qm - qmg) / 3.0
    qs, qsg = z['Q_s'], z['Q_s_grob']
    qsr = (4.0 * qs - qsg) / 3.0 if qs else None
    fm = qm / pm if pm else None
    fs = qs / ps if (qs and ps) else None
    print('%2d | %.6g | %.7g | %s | %s | %s | %s | %s' % (
        D, qm, qmr, '%.3f' % fm if fm else '-', '%.6g' % qs if qs else '-', '%.7g' % qsr if qsr else '-',
        '%.3f' % fs if fs else '-', '%.5f' % (1.0 - z['omega_s']) if z['omega_s'] else '-'))
    pm, ps = qm, qs
print()
print('Virial-Probe am obersten und an drei weiteren Gitterpunkten (fein): E/Q - omega gegen 2G/(D Q)')
for D in sorted(tab):
    P = daten[str(D)]['fein']['punkte']
    teile = []
    for p in (P[0], P[len(P) // 2], P[-9], P[-1]):
        a = p['E'] / p['Q'] - p['omega']
        b = 2.0 * p['G'] / (D * p['Q'])
        teile.append('om2 %.6f: %.6e / %.6e (rel %.1e)' % (p['om2'], a, b, a / b - 1.0))
    print('D = %2d: ' % D + '; '.join(teile))
