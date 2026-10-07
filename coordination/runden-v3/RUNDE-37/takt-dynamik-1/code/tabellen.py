#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TAKT-DYNAMIK-1: formatiert lauf/auswertung.json (td.py auswertung, eingefroren) als Markdown-Tabellen.
Nach dem Einfrieren geschrieben (beschreibend, keine Urteile). Aufruf: tabellen.py <auswertung.json> <ausgabe.md>"""
import json, sys, os
import numpy as np


def g(x, n=3):
    if x is None:
        return '-'
    if isinstance(x, bool):
        return 'ja' if x else 'nein'
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float):
        if x != x:
            return 'nan'
        if x == 0:
            return '0'
        return ('%.' + str(n) + 'g') % x
    return str(x)


def main():
    d = json.load(open(sys.argv[1]))['ergebnis']
    Z = d['zeilen']
    key = {}
    for z in Z:
        key[(z['netz'], z['A'], z['arm'], z['lesart'], z['h'])] = z
    netze = sorted(set(z['netz'] for z in Z))
    L = []
    L.append('## Urteile (mechanisch)\n')
    L.append('| Nr | Wortlaut | Plan | Zahlen |')
    L.append('|---|---|---|---|')
    for k in ('TD0', 'TD1', 'TD2', 'TD3', 'TD4'):
        u = d['urteile'][k]
        rest = {kk: v for kk, v in u.items() if kk not in ('wortlaut', 'plan')}
        L.append('| %s | %s | %s | %s |' % (k, u.get('wortlaut'), u.get('plan'), json.dumps(rest)[:600]))
    L.append('\n## T1 Energiedrift (relativ zu H0), Lesart R, h = 0,5\n')
    L.append('| Netz | A | Ende a | Ende b | Ende c | Max a | Max b | Max c | Max b / Max a | Max c / Max a |')
    L.append('|---|---|---|---|---|---|---|---|---|---|')
    for n in netze:
        for A in (1e-3, 1e-2):
            a, b, c = [key.get((n, A, arm, 'R', 0.5)) for arm in ('a', 'b', 'c')]
            if not (a or b or c):
                continue
            def v(z, f):
                return g(z.get(f)) if z else '-'
            rb = g(b['drift_max'] / a['drift_max']) if (a and b) else '-'
            rc = g(c['drift_max'] / a['drift_max']) if (a and c) else '-'
            L.append('| %s | %g | %s | %s | %s | %s | %s | %s | %s | %s |' % (n, A, v(a, 'drift_ende'), v(b, 'drift_ende'), v(c, 'drift_ende'),
                     v(a, 'drift_max'), v(b, 'drift_max'), v(c, 'drift_max'), rb, rc))
    L.append('\n## T1b Nebenarme: Lesart P und dt halb (h = 0,25)\n')
    L.append('| Netz | A | Lauf | fertig | Ende | Max | Zuege | 2-3 / 3-2 | Summe Delta H | Amp / Amp(a) - 1 | Phase - Phase(a) |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|')
    for z in sorted(Z, key=lambda z: (z['netz'], z['A'], z['arm'], z['lesart'], z['h'])):
        if z['lesart'] == 'R' and z['h'] == 0.5:
            continue
        a = key.get((z['netz'], z['A'], 'a', 'R', z['h'])) or key.get((z['netz'], z['A'], 'a', 'R', 0.5))
        ra = g(z['amp'] / a['amp'] - 1) if (a and z.get('amp') and a.get('amp')) else '-'
        ph = g(z['phase'] - a['phase']) if (a and z.get('phase') is not None and a.get('phase') is not None) else '-'
        L.append('| %s | %g | %s %s h=%g | %s | %s | %s | %s | %s / %s | %s | %s | %s |' % (
            z['netz'], z['A'], z['arm'], z['lesart'], z['h'], g(z['fertig']), g(z.get('drift_ende')), g(z.get('drift_max')),
            g(z.get('n_zuege')), g(z.get('n_23')), g(z.get('n_32')), g(z.get('dH_summe')), ra, ph))
    L.append('\n## T2 Zuege je Periode und Spruenge je Zug (Lesart R, h = 0,5)\n')
    L.append('| Netz | A | Arm | Zuege | 2-3 / 3-2 | nicht ausgef. | je Periode | Summe Delta H | mittel \\|Delta H\\| | max \\|Delta H\\| | 2-3: max \\|Delta V\\| / mittel Delta K | 3-2: mittel Delta V / mittel Delta K | omega_max dt (max) | nach Zug sofort verletzt (max) |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for n in netze:
        for A in (1e-3, 1e-2):
            for arm in ('b', 'c'):
                z = key.get((n, A, arm, 'R', 0.5))
                if not z:
                    continue
                L.append('| %s | %g | %s | %s | %s / %s | %s | %s | %s | %s | %s | %s / %s | %s / %s | %s | %s |' % (
                    n, A, arm, g(z.get('n_zuege')), g(z.get('n_23')), g(z.get('n_32')), g(z.get('n_nicht_ausgefuehrt')),
                    g(z.get('zuege_je_periode')), g(z.get('dH_summe')), g(z.get('dH_betrag_mittel')), g(z.get('dH_betrag_max')),
                    g(z.get('dV_23_betrag_max')), g(z.get('dK_23_mittel')), g(z.get('dV_32_mittel')), g(z.get('dK_32_mittel')),
                    g(z.get('stabil_dt_max')), g(z.get('nach_zug_verletzt_max'))))
    L.append('\n## T3 Sprung von P und dualem Mass am Zug (relativ; gd = gedehntes Netz, hg = Hintergrund)\n')
    L.append('| Netz | A | Arm | Typ | n | gd: *1 Kante | gd: *2 Flaeche | gd: max \\|Delta *1\\| | gd: max \\|Delta P\\| | hg: *1 Kante | hg: max \\|Delta P\\| | hg: Median \\|Delta P\\| |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for n in netze:
        for A in (1e-3, 1e-2):
            for arm in ('b', 'c'):
                z = key.get((n, A, arm, 'R', 0.5))
                if not z:
                    continue
                for typ in (23, 32):
                    q, h = z.get('td0_gd_%d' % typ), z.get('td0_hg_%d' % typ)
                    if not q:
                        continue
                    L.append('| %s | %g | %s | %d-%d | %d | %s | %s | %s | %s | %s | %s | %s |' % (
                        n, A, arm, typ // 10, typ % 10, q['n'], g(q['stern1_rel_max']), g(q['stern2_rel_max']), g(q['dstern1_rel_max']),
                        g(q['dP_rel_max']), g(h['stern1_rel_max']) if h else '-', g(h['dP_rel_max']) if h else '-',
                        g(h['dP_rel_median']) if h else '-'))
    L.append('\n## T4 Amplitude, Phase, Streuung (letzte Periode; Mode)\n')
    L.append('| Netz | A | Mode: omega / Anteil der TT-Welle | Amp a / A | Amp b / Amp a - 1 | Phase b - a | Amp c / Amp a - 1 | Phase c - a | b: modal TT / Null / Rest (Periode) | Flaechen wie Anfang b (min / Ende) | gleiche Zerlegung b (Perioden) |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|')
    for n in netze:
        for A in (1e-3, 1e-2):
            a, b, c = [key.get((n, A, arm, 'R', 0.5)) for arm in ('a', 'b', 'c')]
            if not a:
                continue
            def rel(z):
                return (g(z['amp'] / a['amp'] - 1), g(z['phase'] - a['phase'])) if (z and z.get('amp') and a.get('amp')) else ('-', '-')
            rb, rc = rel(b), rel(c)
            mo = '-'
            if b and b.get('modal_letzte'):
                m = b['modal_letzte']
                mo = '%s / %s / %s (%d)' % (g(m['anteil_TT'], 6), g(m['anteil_null']), g(m['anteil_rest']), b['modal_letzte_periode'])
            fw = '%s / %s' % (g(b.get('flaechen_wie_anfang_min'), 6), g(b.get('flaechen_wie_anfang_ende'), 6)) if b else '-'
            gz = '%s von %s' % (b.get('gleiche_zerlegung_n'), b.get('perioden')) if b else '-'
            L.append('| %s | %g | %s / %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
                n, A, g(a['mode']['omega'], 4), g(a['mode']['anteil_TT_welle']), g(a.get('amp', 0) / A if a.get('amp') else None, 6),
                rb[0], rb[1], rc[0], rc[1], mo, fw, gz))
    L.append('\n## T5 Wachsende Moden und Abbruch\n')
    L.append('| Netz | A | Arm | Lesart | h | wachsend (max nach Zug) | wachsend (Ende) | A_red nicht pd (Zuege) | Abbruch | n_mu<0 (max) |')
    L.append('|---|---|---|---|---|---|---|---|---|---|')
    for z in sorted(Z, key=lambda z: (z['netz'], z['A'], z['arm'], z['lesart'], z['h'])):
        L.append('| %s | %g | %s | %s | %g | %s | %s | %s | %s | %s |' % (
            z['netz'], z['A'], z['arm'], z['lesart'], z['h'], g(z.get('wachsend_max')), g(z.get('wachsend_ende')),
            g(z.get('A_nicht_pd')), (('t = %.4g' % z['abbruch']['t']) if z.get('abbruch') else '-'), g(z.get('n_mu_neg_max'))))
    L.append('\n## T6 Kontrollen der Abbildung (max ueber Zuege)\n')
    L.append('| Netz | A | Arm | Lesart | Projektionsrest a | \\|delta\\| nichtflach (3-2) | neue Kante linear / flach - 1 | dt | N_T | omega_max |')
    L.append('|---|---|---|---|---|---|---|---|---|---|')
    for z in sorted(Z, key=lambda z: (z['netz'], z['A'], z['arm'], z['lesart'], z['h'])):
        if z['arm'] == 'a':
            continue
        L.append('| %s | %g | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            z['netz'], z['A'], z['arm'], z['lesart'], g(z.get('proj_rest_a_max')), g(z.get('delta_nichtflach_betrag_max')),
            g(z.get('l_neu_linear_gegen_flach_max')), g(z.get('dt')), g(z.get('NT')), g(z.get('omega_max'))))
    with open(sys.argv[2] + '.tmp', 'w') as fh:
        fh.write('\n'.join(L) + '\n')
    os.replace(sys.argv[2] + '.tmp', sys.argv[2])
    print('fertig tabellen', flush=True)


if __name__ == '__main__':
    main()
