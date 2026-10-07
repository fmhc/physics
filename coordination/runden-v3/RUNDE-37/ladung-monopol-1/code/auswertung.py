#!/usr/bin/env python3
"""LADUNG-MONOPOL-1: mechanische Urteile nach PLAN.md Abschnitt 4, auswertung.json und Bild.

Aufruf (nur .69, ueber kleintest.sh):
  auswertung.py --gitter lauf/gitter-a.json,lauf/gitter-b.json --schwelle lauf/schwelle.json
                --scan lauf/scan.json --aus lauf/auswertung.json --bild lauf/bild-eigenwerte.png
"""
import argparse
import json

import numpy as np

TOL_S = 1e-8
TOL_EICH = 1e-10
TOL_STRING = 1e-10
TOL_DEFEKT = 1e-10
TOL_SYM = 1e-6
TOL_L5 = 1e-6
EPS_WUERFEL = {0: -3.0, 1: -np.sqrt(6.0), 2: -2.0}


def tiefste_gebundene(stf):
    for s in stf:
        if s['gebunden'] and s['voll']:
            return s
    return None


def lade_gitter(pfade):
    laengen = {}
    for p in pfade.split(','):
        if p:
            with open(p) as f:
                g = json.load(f)
            for Ls, res in g['laengen'].items():
                laengen[int(Ls)] = res
    return laengen


def punkt_bei(qd, V0):
    for p in qd['punkte']:
        if abs(p['V0'] - V0) < 1e-12:
            return p
    return None


def lm0(laengen):
    w = {'c_op': {}, 's_max_abw': {}, 'gebunden_punkte': 0, 'tiefste_m': {}, 'eich_rest': {}, 'string_max': {},
         'string_max_q0': 0.0, 'defekte_max': 0.0, 'sym_rest_max': 0.0}
    ok_a = ok_b = ok_c = ok_d = True
    gueltig = True
    for L, res in sorted(laengen.items()):
        qd = res['q']['0']
        c = qd['operator']
        w['c_op'][L] = c['c_re']
        ok_a &= abs(c['c_re'] - 1) <= TOL_S and abs(c['c_im']) <= TOL_S
        w['defekte_max'] = max(w['defekte_max'], max(qd['defekte'].values()))
        smax = 0.0
        for p in qd['punkte']:
            for s in p['stufen']:
                if s['voll']:
                    smax = max(smax, abs(s['s_re'] - 1), abs(s['s_im']))
                    w['sym_rest_max'] = max(w['sym_rest_max'], s['sym_rest'])
            t = tiefste_gebundene(p['stufen'])
            if t is not None:
                w['gebunden_punkte'] += 1
                w['tiefste_m'][f'L{L}_V0_{p["V0"]:g}'] = t['m']
                ok_b &= t['m'] == 1
        w['s_max_abw'][L] = smax
        ok_a &= smax <= TOL_S
        w['eich_rest'][L] = {r: e['rest_max'] for r, e in res['geo']['eich'].items()}
        ok_c &= all(e['rest_max'] <= TOL_EICH for e in res['geo']['eich'].values())
        smax_str = 0.0
        for q in ('0', '1', '2'):
            for st in res['q'][q]['string']:
                smax_str = max(smax_str, st['max_diff'])
                if q == '0':
                    w['string_max_q0'] = max(w['string_max_q0'], st['max_diff'])
        w['string_max'][L] = smax_str
        ok_d &= smax_str <= TOL_STRING
    if w['gebunden_punkte'] == 0 or w['defekte_max'] > TOL_DEFEKT or w['sym_rest_max'] > TOL_SYM:
        gueltig = False
    w['teile'] = {'a': ok_a, 'b': ok_b, 'c': ok_c, 'd': ok_d}
    if not gueltig:
        return 'nicht auswertbar', w
    return ('eingetroffen' if (ok_a and ok_b and ok_c and ok_d) else 'nicht eingetroffen'), w


def lm1(laengen):
    w = {'c_op': {}, 's_max_abw': {}, 'ungerade_stufen': [], 'defekte_max': 0.0, 'sym_rest_max': 0.0,
         'stufen_geprueft': 0}
    ok = True
    for L, res in sorted(laengen.items()):
        for q, soll in (('1', -1.0), ('2', 1.0)):
            qd = res['q'][q]
            c = qd['operator']
            w['c_op'][f'L{L}_q{q}'] = c['c_re']
            ok &= abs(c['c_re'] - soll) <= TOL_S and abs(c['c_im']) <= TOL_S
            w['defekte_max'] = max(w['defekte_max'], max(qd['defekte'].values()))
            smax = 0.0
            for p in qd['punkte']:
                for s in p['stufen']:
                    if not s['voll']:
                        continue
                    w['stufen_geprueft'] += 1
                    smax = max(smax, abs(s['s_re'] - soll), abs(s['s_im']))
                    w['sym_rest_max'] = max(w['sym_rest_max'], s['sym_rest'])
                    if q == '1' and s['m'] % 2 != 0:
                        w['ungerade_stufen'].append({'L': L, 'V0': p['V0'], 'E': s['E'], 'm': s['m']})
            w['s_max_abw'][f'L{L}_q{q}'] = smax
            ok &= smax <= TOL_S
    ok &= len(w['ungerade_stufen']) == 0
    if w['defekte_max'] > TOL_DEFEKT or w['sym_rest_max'] > TOL_SYM:
        return 'nicht auswertbar', w
    return ('eingetroffen' if ok else 'nicht eingetroffen'), w


def lm23(laengen, schwelle, q, soll_m):
    e = schwelle['ergebnis'].get(f'24_{q}', {}).get('karte', {})
    V0c = e.get('V0c')
    w = {'V0c_L24': V0c, 'punkte': [], 'zweitlauf': [], 'oberes_ende': None}
    if V0c is None:
        return 'nicht auswertbar', w
    qd = laengen[24]['q'][str(q)]
    pkte = [p for p in qd['punkte'] if p['V0'] > V0c]
    if not pkte:
        return 'nicht auswertbar', w
    ok = True
    gueltig = True
    zweit = {round(z['punkt']['V0'], 9): z['punkt'] for z in schwelle['zweitlauf']
             if z['q'] == q and not z.get('oberes_ende')}
    for p in pkte:
        t = tiefste_gebundene(p['stufen'])
        if t is None:
            gueltig = False
            w['punkte'].append({'V0': p['V0'], 'gebunden': False})
            continue
        ist_tiefste = p['stufen'][0] is t
        w['punkte'].append({'V0': p['V0'], 'm': t['m'], 'E': t['E'], 'gewicht': t['gewicht'],
                            'sym_rest': t['sym_rest'], 'chi_abs': t['chi_abs'], 's': t['s_re'],
                            'tiefste_stufe_ueberhaupt': ist_tiefste})
        ok &= t['m'] == soll_m
        gueltig &= t['sym_rest'] <= TOL_SYM
        z = zweit.get(round(p['V0'], 9))
        if z is None:
            gueltig = False
        else:
            t2 = tiefste_gebundene(z['stufen'])
            gleich = t2 is not None and t2['m'] == t['m'] and abs(t2['E'] - t['E']) <= 1e-9 * abs(t['E'])
            w['zweitlauf'].append({'V0': p['V0'], 'm': None if t2 is None else t2['m'],
                                   'dE': None if t2 is None else abs(t2['E'] - t['E']), 'gleich': gleich})
            gueltig &= gleich
    for z in schwelle['zweitlauf']:
        if z['q'] == q and z.get('oberes_ende'):
            t = tiefste_gebundene(z['punkt']['stufen'])
            w['oberes_ende'] = {'V0': z['punkt']['V0'], 'm': None if t is None else t['m'],
                                'E': None if t is None else t['E'],
                                'gewicht': None if t is None else t['gewicht'],
                                's': None if t is None else t['s_re']}
    if not gueltig:
        return 'nicht auswertbar', w
    return ('eingetroffen' if ok else 'nicht eingetroffen'), w


def lm4(schwelle):
    w = {}
    for q in (0, 1, 2):
        for L in (12, 16, 24):
            e = schwelle['ergebnis'].get(f'{L}_{q}', {})
            w[f'V0c_karte_L{L}_q{q}'] = e.get('karte', {}).get('V0c')
            w[f'V0c_energie_L{L}_q{q}'] = e.get('energie', {}).get('V0c')
    k0 = schwelle['ergebnis'].get('24_0', {}).get('karte', {})
    k1 = schwelle['ergebnis'].get('24_1', {}).get('karte', {})
    if k0.get('V0c') is None or k1.get('V0c') is None:
        return 'nicht auswertbar', w
    r = k1['V0c'] / k0['V0c']
    rmin = k1['lo'] / k0['hi']
    rmax = k1['hi'] / k0['lo']
    w.update({'quotient': r, 'quotient_min': rmin, 'quotient_max': rmax,
              'band_grenze_in_unsicherheit': bool((rmin < 1.3 < rmax) or (rmin < 3.0 < rmax))})
    ok = (k1['V0c'] > k0['V0c']) and (1.3 <= r <= 3.0)
    return ('eingetroffen' if ok else 'nicht eingetroffen'), w


def lm5(laengen):
    w = {'vergleiche': [], 'max_dE': 0.0, 'm_abweichungen': 0}
    ok = True
    n = 0
    for q in ('0', '1', '2'):
        for p24 in laengen[24]['q'][q]['punkte']:
            if tiefste_gebundene(p24['stufen']) is None:
                continue
            p16 = punkt_bei(laengen[16]['q'][q], p24['V0'])
            for i, s in enumerate(p24['stufen']):
                if not (s['gebunden'] and s['voll']):
                    continue
                s16 = p16['stufen'][i] if i < len(p16['stufen']) else None
                n += 1
                if s16 is None or s16['m'] != s['m']:
                    ok = False
                    w['m_abweichungen'] += 1
                    w['vergleiche'].append({'q': int(q), 'V0': p24['V0'], 'stufe': i, 'm24': s['m'],
                                            'm16': None if s16 is None else s16['m'], 'dE': None})
                    continue
                dE = abs(s['E'] - s16['E'])
                w['max_dE'] = max(w['max_dE'], dE)
                ok &= dE <= TOL_L5
                w['vergleiche'].append({'q': int(q), 'V0': p24['V0'], 'stufe': i, 'm': s['m'], 'E24': s['E'],
                                        'dE': dE})
    w['anzahl'] = n
    if n == 0:
        return 'nicht auswertbar', w
    return ('eingetroffen' if ok else 'nicht eingetroffen'), w


def kontrollen(laengen):
    k = {'kato_verletzt': [], 'wuerfel': {}, 'dicht': [], 'eig_ergaenzt': [], 'eig_res_max': 0.0, 'A1': {}}
    for L, res in sorted(laengen.items()):
        k['wuerfel'][L] = {x: res['geo'][x] for x in ('wuerfel_aussen_max', 'wuerfel_zentral_minus_2pi',
                                                       'phi_max_minus_pi_drittel')}
        e0 = {q: {p['V0']: p['w'][0] for p in res['q'][q]['punkte']} for q in ('0', '1', '2')}
        for V0, e in e0['0'].items():
            for q in ('1', '2'):
                if e0[q][V0] < e - 1e-12:
                    k['kato_verletzt'].append({'L': L, 'q': q, 'V0': V0})
        for q in ('0', '1', '2'):
            for d in res['q'][q]['dicht']:
                k['dicht'].append({'L': L, 'q': int(q), 'V0': d['V0'], 'max_diff': d['max_diff'],
                                   'gleich': d['stufen_dicht'] == d['stufen_eigsh']})
            for p in res['q'][q]['punkte']:
                if p['eig']['ergaenzt'] != 0 or p['eig']['verworfen'] != 0:
                    k['eig_ergaenzt'].append({'L': L, 'q': int(q), 'V0': p['V0'], 'ergaenzt': p['eig']['ergaenzt'],
                                              'verworfen': p['eig']['verworfen']})
                k['eig_res_max'] = max(k['eig_res_max'], p['eig']['res_max'])
    if 24 in laengen:
        for q in (0, 1, 2):
            p = punkt_bei(laengen[24]['q'][str(q)], 12.0)
            if p is not None:
                d = p['w'][0] + 12.0 - EPS_WUERFEL[q]
                k['A1'][q] = {'E0': p['w'][0], 'E0_plus_V0_minus_eps': d, 'im_band': bool(-0.30 <= d <= -0.15)}
    return k


FARBE = {1: '#2a78d6', 2: '#eb6834', 3: '#1baf7a', 4: '#eda100'}
FARBE_REST = '#e87ba4'
FORM = {1: 'o', 2: 's', 3: '^', 4: 'D'}


def bild(pfad, scan, laengen, schwelle):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    plt.rcParams.update({'font.size': 10, 'axes.edgecolor': '#52514e', 'axes.labelcolor': '#0b0b0b',
                         'xtick.color': '#52514e', 'ytick.color': '#52514e'})
    fig, axs = plt.subplots(1, 3, figsize=(15, 5.6), sharey=True, facecolor='#fcfcfb')
    for ax, q in zip(axs, (0, 1, 2)):
        ax.set_facecolor('#fcfcfb')
        pts = scan['scan'].get(f'16_{q}', []) if scan else []
        for p in pts:
            for s in p['stufen']:
                if s['a'] >= 12 or not s['voll']:
                    continue
                m = s['m']
                c = FARBE.get(m, FARBE_REST)
                ax.plot(p['V0'], s['E'], FORM.get(m, 'P'), ms=4.5, mfc=c if s['gebunden'] else 'none',
                        mec=c, mew=0.9, zorder=2)
        # L = 24 Raster: tiefste Stufe mit Zahl der Entartung
        qd = laengen[24]['q'][str(q)]
        for p in qd['punkte']:
            s = p['stufen'][0]
            c = FARBE.get(s['m'], FARBE_REST)
            ax.plot(p['V0'], s['E'], FORM.get(s['m'], 'P'), ms=10, mfc='none', mec='#0b0b0b', mew=1.2, zorder=3)
            ax.annotate(f"{s['m']}", (p['V0'], s['E']), textcoords='offset points', xytext=(7, -12),
                        fontsize=9, color='#0b0b0b')
        ax.axhline(-6.001, color='#52514e', lw=0.8, ls='--', zorder=1)
        e = schwelle['ergebnis'].get(f'24_{q}', {}).get('karte', {})
        if e.get('V0c') is not None:
            ax.axvline(e['V0c'], color='#52514e', lw=0.8, ls=':', zorder=1)
            ax.text(e['V0c'] + 0.15, -15.6, f"V0c = {e['V0c']:.3f}", fontsize=9, color='#52514e')
        ax.set_title(f'q = {q}' + ('  (ohne Monopol)' if q == 0 else ''), color='#0b0b0b')
        ax.set_xlabel('Kern-Topf V0')
        ax.grid(True, color='#e6e5e1', lw=0.6)
        ax.set_xlim(-0.3, 12.5)
    axs[0].set_ylabel('Eigenwert E (tiefste 12)')
    axs[0].set_ylim(-16.0, -4.9)
    griffe = [Line2D([], [], ls='none', marker=FORM[m], mfc=FARBE[m], mec=FARBE[m], ms=7, label=f'{m}-fach')
              for m in (1, 2, 3, 4)]
    griffe.append(Line2D([], [], ls='none', marker='o', mfc='none', mec='#52514e', ms=7,
                         label='hohl: nicht gebunden'))
    griffe.append(Line2D([], [], ls='none', marker='o', mfc='none', mec='#0b0b0b', ms=10, mew=1.2,
                         label='L = 24, tiefste Stufe (Zahl = Entartung)'))
    griffe.append(Line2D([], [], color='#52514e', ls='--', lw=0.8, label='E = -6 - 1e-3'))
    griffe.append(Line2D([], [], color='#52514e', ls=':', lw=0.8, label='Schwelle V0c (L = 24)'))
    fig.legend(handles=griffe, loc='lower center', ncol=8, frameon=False, fontsize=9)
    fig.suptitle('LADUNG-MONOPOL-1: tiefste Eigenwerte gegen V0 (Punkte: L = 16, Schritt 0,25; Ringe: L = 24)',
                 color='#0b0b0b')
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    fig.savefig(pfad, dpi=130, facecolor='#fcfcfb')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--gitter', required=True)
    ap.add_argument('--schwelle', required=True)
    ap.add_argument('--scan', default='')
    ap.add_argument('--aus', required=True)
    ap.add_argument('--bild', default='')
    args = ap.parse_args()
    laengen = lade_gitter(args.gitter)
    with open(args.schwelle) as f:
        schwelle = json.load(f)
    scan = None
    if args.scan:
        with open(args.scan) as f:
            scan = json.load(f)
    urteile = {}
    for nr, (u, werte) in (('LM0', lm0(laengen)), ('LM1', lm1(laengen)), ('LM2', lm23(laengen, schwelle, 1, 2)),
                           ('LM3', lm23(laengen, schwelle, 2, 3)), ('LM4', lm4(schwelle)), ('LM5', lm5(laengen))):
        urteile[nr] = {'urteil': u, 'werte': werte}
    out = {'urteile': urteile, 'kontrollen': kontrollen(laengen)}
    with open(args.aus, 'w') as f:
        json.dump(out, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    if args.bild:
        bild(args.bild, scan, laengen, schwelle)
    for nr, u in urteile.items():
        print(nr, u['urteil'], flush=True)


if __name__ == '__main__':
    main()
