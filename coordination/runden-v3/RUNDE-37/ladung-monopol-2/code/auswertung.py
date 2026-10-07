#!/usr/bin/env python3
"""LADUNG-MONOPOL-2: mechanische Urteile nach PLAN.md Abschnitt 5, auswertung.json und Bild.

Aufruf (nur .69, ueber kleintest.sh):
  auswertung.py --gitter lauf/gitter-a.json,lauf/gitter-b.json --schwelle lauf/schwelle-46.json,lauf/schwelle-8.json
                --scan lauf/scan.json --aus lauf/auswertung.json --bild lauf/bild-eigenwerte.png
"""
import argparse
import json

import numpy as np

TOL_S = 1e-8
TOL_EICH = 1e-10
TOL_STRING = 1e-10
TOL_FLUSS = 1e-12
TOL_DEFEKT = 1e-10
TOL_SYM = 1e-6
TOL_LP4 = 1e-6
TIEF = 1.0          # [F] tief gebunden: Bindung E_Kante - E >= 1
E_KANTE = -6.0


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


def lade_schwelle(pfade):
    erg = {'ergebnis': {}, 'zweitlauf': []}
    for p in pfade.split(','):
        if p:
            with open(p) as f:
                s = json.load(f)
            erg['ergebnis'].update(s['ergebnis'])
            erg['zweitlauf'] += s.get('zweitlauf', [])
    return erg


def punkt_bei(qd, V0):
    for p in qd['punkte']:
        if abs(p['V0'] - V0) < 1e-12:
            return p
    return None


def gueltigkeit(laengen):
    """Konstruktionspruefungen (PLAN 5, Gueltigkeit): Euler, Zellraender, Inzidenz, lsqr, Schliessung, Defekte."""
    w = {}
    ok = True
    for L, res in sorted(laengen.items()):
        pr = res['geo']['pruef']
        e = {'euler': pr['euler'], 'zellrand_max': pr['zellrand_max'], 'umkugel_ok': pr['zellen_ecken_umkugel_ok'],
             'innen': [pr['innen_flaechen'], pr['innen_flaechen_in_zwei_zellen']], 'grad': pr['grad_min_max'],
             'zusammenhang': pr['zusammenhang'], 'sechseck_eben_max': pr['sechseck_eben_max'],
             'eich_rest': {k: v['rest_max'] for k, v in res['geo']['eich'].items()},
             'schliessung': {k: v['schliessung_max'] for k, v in res['geo']['eich'].items()},
             'defekte_max': max(max(res['q'][q]['defekte'].values()) for q in ('0', '1', '2'))}
        g = (pr['euler'] == 1 and pr['zellrand_max'] == 0.0 and pr['zellen_ecken_umkugel_ok']
             and pr['innen_flaechen'] == pr['innen_flaechen_in_zwei_zellen'] and pr['zusammenhang'] == 1
             and pr['grad_min_max'][1] == 6
             and all(v <= TOL_EICH for v in e['eich_rest'].values())
             and all(v <= TOL_FLUSS for v in e['schliessung'].values())
             and e['defekte_max'] <= TOL_DEFEKT)
        e['ok'] = bool(g)
        ok &= g
        w[L] = e
    return ok, w


def lp0(laengen, gueltig):
    w = {'gebunden_punkte': 0, 'tiefste_m_q0': {}, 'fluss': {}, 'string_max': {}, 'string_max_q0': 0.0,
         'sym_rest_max': 0.0}
    ok_a = ok_b = ok_c = True
    for L, res in sorted(laengen.items()):
        qd = res['q']['0']
        for p in qd['punkte']:
            for s in p['stufen']:
                if s['voll']:
                    w['sym_rest_max'] = max(w['sym_rest_max'], s['sym_rest'])
            t = tiefste_gebundene(p['stufen'])
            if t is not None:
                w['gebunden_punkte'] += 1
                w['tiefste_m_q0'][f'L{L}_V0_{p["V0"]:g}'] = t['m']
                ok_a &= t['m'] == 1
        fl = res['geo']['fluss']
        w['fluss'][L] = fl
        ok_b &= fl['zelle_aussen_max'] <= TOL_FLUSS and abs(fl['monopolzelle_minus_2pi']) <= TOL_FLUSS
        smax = 0.0
        for q in ('0', '1', '2'):
            for st in res['q'][q]['string']:
                smax = max(smax, st['max_diff'])
                if q == '0':
                    w['string_max_q0'] = max(w['string_max_q0'], st['max_diff'])
        w['string_max'][L] = smax
        ok_c &= smax <= TOL_STRING
    w['teile'] = {'a': ok_a, 'b': ok_b, 'c': ok_c}
    w['c_nur_q0_kartenwortlaut'] = bool(w['string_max_q0'] <= TOL_STRING)
    if not gueltig or w['gebunden_punkte'] == 0 or w['sym_rest_max'] > TOL_SYM:
        return 'nicht auswertbar', w
    return ('eingetroffen' if (ok_a and ok_b and ok_c) else 'nicht eingetroffen'), w


def lp1(laengen, gueltig):
    w = {'c_op': {}, 's_max_abw': {}, 'ungerade_stufen': [], 'sym_rest_max': 0.0, 'stufen_geprueft': 0}
    ok = True
    for L, res in sorted(laengen.items()):
        for q, soll in (('1', -1.0), ('2', 1.0)):
            qd = res['q'][q]
            c = qd['operator']['kommutator']
            w['c_op'][f'L{L}_q{q}'] = [c['c_re'], c['c_im'], c['rest']]
            ok &= abs(c['c_re'] - soll) <= TOL_S and abs(c['c_im']) <= TOL_S and c['rest'] <= TOL_S
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
    if not gueltig or w['sym_rest_max'] > TOL_SYM:
        return 'nicht auswertbar', w
    return ('eingetroffen' if ok else 'nicht eingetroffen'), w


def lp23(laengen, schwelle, q, soll_m, gueltig):
    Lg = max(laengen)
    e = schwelle['ergebnis'].get(f'{Lg}_{q}', {}).get('karte', {})
    V0c = e.get('V0c')
    w = {'L': Lg, 'V0c': V0c, 'punkte': [], 'zweitlauf': [], 'oberes_ende': None}
    if V0c is None or not gueltig:
        return 'nicht auswertbar', w
    qd = laengen[Lg]['q'][str(q)]
    pkte = [p for p in qd['punkte'] if p['V0'] > V0c]
    if not pkte:
        return 'nicht auswertbar', w
    ok = True
    g = True
    zweit = {round(z['punkt']['V0'], 9): z['punkt'] for z in schwelle['zweitlauf']
             if z['q'] == q and z['L'] == Lg and not z.get('oberes_ende')}
    for p in pkte:
        t = tiefste_gebundene(p['stufen'])
        if t is None:
            g = False
            w['punkte'].append({'V0': p['V0'], 'gebunden': False})
            continue
        w['punkte'].append({'V0': p['V0'], 'm': t['m'], 'E': t['E'], 'gewicht': t['gewicht'],
                            'etikett': t['etikett'], 'c3_ew_grad': t['c3_ew_grad'], 's': t['s_re'],
                            'sym_rest': t['sym_rest'], 'tiefste_stufe_ueberhaupt': p['stufen'][0]['a'] == t['a']})
        ok &= t['m'] == soll_m
        g &= t['sym_rest'] <= TOL_SYM
        z = zweit.get(round(p['V0'], 9))
        if z is None:
            g = False
        else:
            t2 = tiefste_gebundene(z['stufen'])
            gleich = t2 is not None and t2['m'] == t['m'] and abs(t2['E'] - t['E']) <= 1e-9 * abs(t['E'])
            w['zweitlauf'].append({'V0': p['V0'], 'm': None if t2 is None else t2['m'],
                                   'dE': None if t2 is None else abs(t2['E'] - t['E']), 'gleich': gleich})
            g &= gleich
    for z in schwelle['zweitlauf']:
        if z['q'] == q and z['L'] == Lg and z.get('oberes_ende'):
            t = tiefste_gebundene(z['punkt']['stufen'])
            w['oberes_ende'] = {'V0': z['punkt']['V0'], 'm': None if t is None else t['m'],
                                'E': None if t is None else t['E'],
                                'etikett': None if t is None else t['etikett'],
                                'gewicht': None if t is None else t['gewicht']}
    if not g:
        return 'nicht auswertbar', w
    return ('eingetroffen' if ok else 'nicht eingetroffen'), w


def lp4(laengen, gueltig):
    Ls = sorted(laengen)
    La, Lb = Ls[-2], Ls[-1]
    w = {'L': [La, Lb], 'vergleiche': [], 'max_dE': 0.0, 'm_abweichungen': 0, 'alle_gebundenen': [],
         'alle_gebundenen_max_dE': 0.0}
    ok = True
    n = 0
    for q in ('0', '1', '2'):
        for pb in laengen[Lb]['q'][q]['punkte']:
            pa = punkt_bei(laengen[La]['q'][q], pb['V0'])
            for i, s in enumerate(pb['stufen']):
                if not (s['gebunden'] and s['voll']):
                    continue
                sa = pa['stufen'][i] if i < len(pa['stufen']) else None
                tief = (E_KANTE - s['E']) >= TIEF
                if sa is None or sa['m'] != s['m']:
                    eintrag = {'q': int(q), 'V0': pb['V0'], 'stufe': i, 'm_b': s['m'],
                               'm_a': None if sa is None else sa['m'], 'dE': None, 'tief': tief}
                    w['alle_gebundenen'].append(eintrag)
                    if tief:
                        n += 1
                        ok = False
                        w['m_abweichungen'] += 1
                        w['vergleiche'].append(eintrag)
                    continue
                dE = abs(s['E'] - sa['E'])
                w['alle_gebundenen'].append({'q': int(q), 'V0': pb['V0'], 'stufe': i, 'm': s['m'], 'E': s['E'],
                                             'dE': dE, 'tief': tief})
                w['alle_gebundenen_max_dE'] = max(w['alle_gebundenen_max_dE'], dE)
                if tief:
                    n += 1
                    w['max_dE'] = max(w['max_dE'], dE)
                    ok &= dE <= TOL_LP4
                    w['vergleiche'].append({'q': int(q), 'V0': pb['V0'], 'stufe': i, 'm': s['m'], 'E': s['E'],
                                            'dE': dE})
    w['anzahl'] = n
    w['alle_gebundenen_unter_tol'] = bool(all(x.get('dE') is not None and x['dE'] <= TOL_LP4
                                             for x in w['alle_gebundenen']))
    if n == 0 or not gueltig:
        return 'nicht auswertbar', w
    return ('eingetroffen' if ok else 'nicht eingetroffen'), w


def kontrollen(laengen, schwelle):
    k = {'kato_verletzt': [], 'dicht': [], 'eig_ergaenzt': 0, 'eig_punkte': 0, 'eig_verworfen': 0,
         'eig_res_max': 0.0, 'k4': {}, 'c3_normierung': {}, 'operator': {}, 'tiefste_je_punkt': {},
         'schwellen': {}, 'geo': {}}
    for L, res in sorted(laengen.items()):
        k['geo'][L] = {x: res['geo']['pruef'][x] for x in ('N', 'kanten', 'dreiecke', 'sechsecke', 'tetraeder',
                                                            'stumpftetraeder', 'euler', 'sechseck_eben_max',
                                                            'kante_in_flaechen_min_max')}
        k['geo'][L]['string_flaechen'] = {s: v['string_flaechen'] for s, v in res['geo']['eich'].items()}
        e0 = {q: {p['V0']: p['w'][0] for p in res['q'][q]['punkte']} for q in ('0', '1', '2')}
        for V0, e in e0['0'].items():
            for q in ('1', '2'):
                if e0[q][V0] < e - 1e-12:
                    k['kato_verletzt'].append({'L': L, 'q': q, 'V0': V0})
        for q in ('0', '1', '2'):
            qd = res['q'][q]
            k['k4'][f'L{L}_q{q}'] = [(s['E'], s['m'], s['etikett']) for s in qd['k4']]
            k['c3_normierung'][f'L{L}_q{q}'] = qd['c3_normierung']
            k['operator'][f'L{L}_q{q}'] = qd['operator']
            for d in qd['dicht']:
                k['dicht'].append({'L': L, 'q': int(q), 'V0': d['V0'], 'max_diff': d['max_diff'],
                                   'gleich': d['stufen_dicht'] == d['stufen_eigsh']})
            for p in qd['punkte']:
                k['eig_punkte'] += 1
                if p['eig']['ergaenzt'] != 0:
                    k['eig_ergaenzt'] += 1
                k['eig_verworfen'] += p['eig']['verworfen']
                k['eig_res_max'] = max(k['eig_res_max'], p['eig']['res_max'])
                s0 = p['stufen'][0]
                t = tiefste_gebundene(p['stufen'])
                k['tiefste_je_punkt'][f'L{L}_q{q}_V0_{p["V0"]:g}'] = {
                    'E0': s0['E'], 'm0': s0['m'], 'etikett0': s0['etikett'], 'gewicht0': s0['gewicht'],
                    'geb_m': None if t is None else t['m'], 'geb_E': None if t is None else t['E'],
                    'geb_etikett': None if t is None else t['etikett'],
                    'stufen': [(s['m'], s['etikett'], round(s['E'], 6), s['gebunden']) for s in p['stufen']
                               if s['voll']]}
    for key, e in schwelle['ergebnis'].items():
        k['schwellen'][key] = {kr: {x: e.get(kr, {}).get(x) for x in ('V0c', 'lo', 'hi', 'monoton', 'erweitert')}
                               for kr in ('karte', 'energie')}
    return k


FARBE = {'G4': '#2a78d6', 'G5': '#eb6834', 'G6': '#1baf7a', 'G5+G6': '#eda100',
         'A': '#2a78d6', 'E1': '#eb6834', 'E2': '#1baf7a', 'T': '#9b59b6'}
FARBE_REST = '#e87ba4'
FORM = {1: 'o', 2: 's', 3: '^', 4: 'D'}


def bild(pfad, scan, laengen, schwelle):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    plt.rcParams.update({'font.size': 10, 'axes.edgecolor': '#52514e', 'axes.labelcolor': '#0b0b0b',
                         'xtick.color': '#52514e', 'ytick.color': '#52514e'})
    Lg = max(laengen)
    Ls = sorted(int(k.split('_')[0]) for k in scan['scan']) if scan else []
    Lscan = Ls[0] if Ls else None
    fig, axs = plt.subplots(1, 3, figsize=(15.5, 6.0), sharey=True, facecolor='#fcfcfb')
    for ax, q in zip(axs, (0, 1, 2)):
        ax.set_facecolor('#fcfcfb')
        pts = scan['scan'].get(f'{Lscan}_{q}', []) if scan else []
        for p in pts:
            for s in p['stufen']:
                if s['a'] >= 12 or not s['voll']:
                    continue
                c = FARBE.get(s['etikett'], FARBE_REST)
                ax.plot(p['V0'], s['E'], FORM.get(s['m'], 'P'), ms=4.5, mfc=c if s['gebunden'] else 'none',
                        mec=c, mew=0.9, zorder=2)
        qd = laengen[Lg]['q'][str(q)]
        for p in qd['punkte']:
            s = p['stufen'][0]
            ax.plot(p['V0'], s['E'], FORM.get(s['m'], 'P'), ms=10, mfc='none', mec='#0b0b0b', mew=1.2, zorder=3)
            ax.annotate(f"{s['m']} {s['etikett']}", (p['V0'], s['E']), textcoords='offset points', xytext=(7, -13),
                        fontsize=8, color='#0b0b0b')
        ax.axhline(-6.001, color='#52514e', lw=0.8, ls='--', zorder=1)
        e = schwelle['ergebnis'].get(f'{Lg}_{q}', {}).get('karte', {})
        if e.get('V0c') is not None:
            ax.axvline(e['V0c'], color='#52514e', lw=0.8, ls=':', zorder=1)
            ax.text(e['V0c'] + 0.15, -4.6, f"V0c = {e['V0c']:.3f}", fontsize=9, color='#52514e')
        ax.set_title(f'q = {q}' + ('  (ohne Monopol)' if q == 0 else ''), color='#0b0b0b')
        ax.set_xlabel('Kern-Topf V0')
        ax.grid(True, color='#e6e5e1', lw=0.6)
        ax.set_xlim(-0.3, 12.8)
    axs[0].set_ylabel('Eigenwert E (tiefste 12)')
    griffe = [Line2D([], [], ls='none', marker=FORM[m], mfc='#52514e', mec='#52514e', ms=7, label=f'{m}-fach')
              for m in (1, 2, 3, 4)]
    griffe += [Line2D([], [], ls='none', marker='s', mfc=FARBE[e], mec=FARBE[e], ms=7, label=e)
               for e in ('G4', 'G5', 'G6', 'G5+G6', 'T')]
    griffe.append(Line2D([], [], ls='none', marker='o', mfc='none', mec='#52514e', ms=7, label='hohl: ungebunden'))
    griffe.append(Line2D([], [], ls='none', marker='o', mfc='none', mec='#0b0b0b', ms=10, mew=1.2,
                         label=f'L = {Lg}: tiefste Stufe (m, Darstellung)'))
    fig.legend(handles=griffe, loc='lower center', ncol=6, frameon=False, fontsize=9)
    fig.suptitle(f'LADUNG-MONOPOL-2 (Pyrochlor-Netz): tiefste Eigenwerte gegen V0; Punkte L = {Lscan} (Schritt 0,25), '
                 f'Ringe L = {Lg}; Farbe = Darstellung (q = 0, 2: A blau, E1 orange, E2 gruen, T violett)',
                 color='#0b0b0b', fontsize=10)
    fig.tight_layout(rect=(0, 0.09, 1, 0.95))
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
    schwelle = lade_schwelle(args.schwelle)
    scan = None
    if args.scan:
        with open(args.scan) as f:
            scan = json.load(f)
    gueltig, wg = gueltigkeit(laengen)
    urteile = {}
    for nr, (u, werte) in (('LP0', lp0(laengen, gueltig)), ('LP1', lp1(laengen, gueltig)),
                           ('LP2', lp23(laengen, schwelle, 1, 2, gueltig)),
                           ('LP3', lp23(laengen, schwelle, 2, 3, gueltig)), ('LP4', lp4(laengen, gueltig))):
        urteile[nr] = {'urteil': u, 'werte': werte}
    out = {'urteile': urteile, 'gueltigkeit': {'ok': gueltig, 'je_L': wg}, 'kontrollen': kontrollen(laengen, schwelle)}
    with open(args.aus, 'w') as f:
        json.dump(out, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    if args.bild:
        bild(args.bild, scan, laengen, schwelle)
    for nr, u in urteile.items():
        print(nr, u['urteil'], flush=True)


if __name__ == '__main__':
    main()
