#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-4D-1: Auswertung aller Laufdateien (beschreibend, ohne Urteile; keine Karte).

Liest lauf/u4-s*-f*-mu*.json (Hauptlaeufe, Hubfolge index, h = 2^-10) und lauf/u4x-*.json (Kontrollen: Hubfolge
umgekehrt, h = 2^-12). Schreibt Zusammenfassung (JSON) und Tabellen (Markdown).
"""
import argparse, glob, json, os
import numpy as np

LES = ['R', 'P']
MUS = [-1e-3, -1e-4, -1e-5]


def lade(p):
    return json.load(open(p))['ergebnis']


def g3(x):
    if x is None:
        return '-'
    if isinstance(x, (bool, str)):
        return str(x)
    if x == 0:
        return '0'
    return '%.3g' % x


def mmm(v):
    v = [x for x in v if x is not None]
    if not v:
        return None
    return {'n': len(v), 'median': float(np.median(v)), 'min': float(np.min(v)), 'max': float(np.max(v))}


def mm(d):
    return '-' if not d else '%s [%s, %s] (n=%d)' % (g3(d['median']), g3(d['min']), g3(d['max']), d['n'])


def zuege(muster, ordner):
    Z = []
    for p in sorted(glob.glob(os.path.join(ordner, muster))):
        e = lade(p)
        if not e.get('zuege'):
            Z.append({'datei': os.path.basename(p), 'saat': e['saat'], 'nr': e['nr'], 'art': e['art'], 'zug': '-',
                      'mu': e['mu'], 'h': e.get('h'), 'hubfolge': e.get('hubfolge'), 'gueltig': False,
                      'grund': 'lagen: %s' % json.dumps(e.get('lagen'))})
            continue
        for zn, z in e.get('zuege', {}).items():
            r = {'datei': os.path.basename(p), 'saat': e['saat'], 'nr': e['nr'], 'art': e['art'], 'zug': zn,
                 'mu': e['mu'], 'h': e.get('h'), 'hubfolge': e.get('hubfolge'), 'gueltig': bool(z.get('gueltig'))}
            if not r['gueltig']:
                r['grund'] = z.get('grund')
                Z.append(r)
                continue
            r['mu_zug'] = e['lagen']['mu_' + zn]
            r['lagen_gueltig'] = e['lagen']['gueltig']
            for tag in ('A2', 'M'):
                g = z.get(tag, {})
                r[tag] = g
                for L in LES:
                    if g.get('H0') and g.get('dH_' + L) is not None:
                        r[tag + '_rel_' + L] = abs(g['dH_' + L]) / g['H0']
                        r[tag + '_relV_' + L] = abs(g['dV_' + L]) / g['H0']
            gesp = z.get('A2_gespeichert', {})
            r['A2_gesp'] = gesp
            r['A2_wiedergabe'] = (max(abs(z['A2']['dH_' + L] - gesp[L]) / abs(gesp[L]) for L in LES)
                                  if gesp and all(gesp.get(L) for L in LES) else None)
            r['meff_vor'] = e.get('meff_vor', {})
            r['meff_nach'] = z.get('meff_nach', {})
            Z.append(r)
    return Z


def auswerten(ordner):
    Z = zuege('u4-s*-f*-mu*.json', ordner)
    X = zuege('u4x-*.json', ordner)
    ok = [r for r in Z if r['gueltig']]
    out = {'n_zuege': len(Z), 'n_gueltig': len(ok), 'ungueltig': [{k: r.get(k) for k in ('datei', 'zug', 'grund')}
                                                                  for r in Z if not r['gueltig']]}
    # je mu: relative Spruenge
    jemu = {}
    for mu in MUS:
        S = [r for r in ok if r['mu'] == mu]
        if not S:
            continue
        B = {'n': len(S)}
        for tag in ('A2', 'M'):
            for L in LES:
                B[tag + '_rel_' + L] = mmm([r.get(tag + '_rel_' + L) for r in S])
                B[tag + '_dH_signed_' + L] = mmm([r[tag].get('dH_' + L) / r[tag]['H0'] for r in S
                                                   if r[tag].get('H0')])
                B[tag + '_relV_' + L] = mmm([r.get(tag + '_relV_' + L) for r in S])
        for L in LES:
            B['faktor_A2_durch_M_' + L] = mmm([r['A2_rel_' + L] / r['M_rel_' + L] for r in S
                                               if r.get('M_rel_' + L)])
            B['n_M_kleiner_' + L] = int(sum(1 for r in S if r.get('M_rel_' + L) is not None
                                            and r['M_rel_' + L] < r['A2_rel_' + L]))
            B['n_M_negativ_' + L] = int(sum(1 for r in S if r['M'].get('dH_' + L, 0) < 0))
        jemu['%g' % mu] = B
    out['je_mu'] = jemu
    # gepaarte Verhaeltnisse
    by = {}
    for r in ok:
        by.setdefault((r['saat'], r['nr'], r['zug']), {})[r['mu']] = r
    paare = {}
    for a, b in ((-1e-3, -1e-4), (-1e-4, -1e-5)):
        V = []
        for key, v in sorted(by.items()):
            if a in v and b in v:
                q = {'saat': key[0], 'nr': key[1], 'zug': key[2], 'art': v[a]['art']}
                for tag in ('A2', 'M'):
                    for L in LES:
                        x, y = v[a][tag].get('dH_' + L), v[b][tag].get('dH_' + L)
                        q[tag + '_' + L] = abs(x) / abs(y) if (x is not None and y) else None
                        q[tag + '_' + L + '_p'] = float(np.log10(q[tag + '_' + L])) if q[tag + '_' + L] else None
                V.append(q)
        S = {'n': len(V), 'liste': V}
        for tag in ('A2', 'M'):
            for L in LES:
                S[tag + '_' + L] = mmm([q[tag + '_' + L] for q in V])
                S[tag + '_' + L + '_p'] = mmm([q[tag + '_' + L + '_p'] for q in V])
        paare['%g/%g' % (a, b)] = S
    out['verhaeltnisse'] = paare
    # Kontrollen
    K = {}
    K['A2_wiedergabe_max'] = max([r['A2_wiedergabe'] for r in ok if r['A2_wiedergabe'] is not None] or [None])
    K['A2_n_wiedergabe'] = int(sum(1 for r in ok if r['A2_wiedergabe'] is not None))
    for w in ('vor', 'nach'):
        M = [r['meff_' + w] for r in ok]
        K[w] = {'M_n_neg': sorted(set(m.get('M_n_neg') for m in M)), 'M_n_null': sorted(set(m.get('M_n_null') for m in M)),
                'NV': sorted(set(m.get('NV') for m in M)),
                'M_absmin_rel': mmm([m.get('M_absmin_rel') for m in M]),
                'D0_n_neg': sorted(set(m.get('D0_n_neg') for m in M)), 'D0_min_rel': mmm([m.get('D0_min_rel') for m in M]),
                'J_sv_min_rel': mmm([m.get('J_sv_min_rel') for m in M]),
                'J_rang_ok': sorted(set(m.get('J_rang_ok') for m in M)),
                'P_sym_max': max(max(m.get('P_sym', [0])) for m in M), 'S2_asym_max': max(m.get('S2_asym', 0) for m in M),
                't_gesamt_s': mmm([m.get('t_gesamt_s') for m in M])}
    K['r_V_gegen_B'] = mmm([r['meff_vor'].get('r_V_gegen_B') for r in ok])
    K['kappa'] = mmm([r['meff_vor'].get('kappa') for r in ok])
    K['C_rest_kappa'] = mmm([r['meff_vor'].get('C_rest_kappa') for r in ok])
    for tag in ('A2', 'M'):
        K[tag + '_A_pd_alle'] = bool(all(r[tag].get('A_pd_vor') and r[tag].get('A_pd_nach') for r in ok))
        K[tag + '_n_A_neg_max'] = max(max(r[tag].get('n_A_neg_vor', 0), r[tag].get('n_A_neg_nach', 0)) for r in ok)
        K[tag + '_omega_durch_k1'] = mmm([r[tag].get('omega_durch_k1') for r in ok])
        K[tag + '_anteil_TT_welle'] = mmm([r[tag].get('anteil_TT_welle') for r in ok])
        K[tag + '_K0_anteil'] = mmm([r[tag]['K0'] / r[tag]['H0'] for r in ok if r[tag].get('H0')])
        K[tag + '_proj_rest_a'] = mmm([r[tag].get('proj_rest_a_R') for r in ok])
        K[tag + '_dA_alt_rel'] = mmm([r[tag].get('dA_alt_rel') for r in ok])
        K[tag + '_dB_pull_rel_max'] = max(r[tag].get('dB_pull_rel', 0) for r in ok)
        K[tag + '_relV_max'] = max(max(r.get(tag + '_relV_' + L, 0) for L in LES) for r in ok)
    K['M_dM_pull_rel'] = mmm([r['M'].get('dM_pull_rel') for r in ok])
    K['M_dV_eff_pull_rel'] = mmm([r['M'].get('dV_eff_pull_rel') for r in ok])
    out['kontrollen'] = K
    # Kontrolllaeufe (Hubfolge, h)
    xs = []
    for r in X:
        if not r['gueltig']:
            xs.append({k: r.get(k) for k in ('datei', 'zug', 'grund')})
            continue
        ref = by.get((r['saat'], r['nr'], r['zug']), {}).get(r['mu'])
        q = {'datei': r['datei'], 'zug': r['zug'], 'mu': r['mu'], 'h': r['h'], 'hubfolge': r['hubfolge'],
             'M_n_neg_vor': r['meff_vor'].get('M_n_neg'), 'D0_n_neg_vor': r['meff_vor'].get('D0_n_neg'),
             'D0_min_rel_vor': r['meff_vor'].get('D0_min_rel'), 'M_omega_durch_k1': r['M'].get('omega_durch_k1')}
        for L in LES:
            q['M_dH_' + L] = r['M'].get('dH_' + L)
            q['M_rel_' + L] = r.get('M_rel_' + L)
            if ref is not None:
                q['ref_M_dH_' + L] = ref['M'].get('dH_' + L)
                q['ref_M_rel_' + L] = ref.get('M_rel_' + L)
        xs.append(q)
    out['kontrolllaeufe'] = xs
    out['zeilen'] = [{k: r.get(k) for k in ('saat', 'nr', 'art', 'zug', 'mu', 'mu_zug', 'A2_rel_R', 'A2_rel_P', 'M_rel_R',
                                             'M_rel_P', 'A2_wiedergabe')} | {
        'A2_dH_R': r['A2'].get('dH_R'), 'A2_dH_P': r['A2'].get('dH_P'), 'M_dH_R': r['M'].get('dH_R'),
        'M_dH_P': r['M'].get('dH_P'), 'A2_H0': r['A2'].get('H0'), 'M_H0': r['M'].get('H0')} for r in ok]
    return out


def markdown(o, pfad):
    L = ['# UMKLAPP-4D-1: Auswertung (synthetisch, keine Messdaten)', '',
         '## Je Zug und mu: relativer Sprung |dH| / H0 (Vorzeichen in Klammern)', '',
         '| Saat | Fall | Art | Zug | mu | A2 R | A2 P | M_eff R | M_eff P | A2/M R | A2/M P |',
         '|---|---|---|---|---|---|---|---|---|---|---|']
    for r in sorted(o['zeilen'], key=lambda r: (r['saat'], r['nr'], r['zug'], -r['mu'])):
        def sg(x):
            return '+' if x is not None and x > 0 else '-'
        fR = r['A2_rel_R'] / r['M_rel_R'] if r.get('M_rel_R') else None
        fP = r['A2_rel_P'] / r['M_rel_P'] if r.get('M_rel_P') else None
        L.append('| %d | %d | %s | %s | %g | %s (%s) | %s (%s) | %s (%s) | %s (%s) | %s | %s |' % (
            r['saat'], r['nr'], r['art'], r['zug'], r['mu'], g3(r['A2_rel_R']), sg(r['A2_dH_R']), g3(r['A2_rel_P']),
            sg(r['A2_dH_P']), g3(r['M_rel_R']), sg(r['M_dH_R']), g3(r['M_rel_P']), sg(r['M_dH_P']), g3(fR), g3(fP)))
    L += ['', '## Je mu (Median [Min, Max])', '']
    for mu, B in o['je_mu'].items():
        L.append('- mu = %s (n = %d): A2 R %s; A2 P %s; M R %s; M P %s; Faktor A2/M R %s, P %s; M kleiner R %d, P %d; '
                 'M negativ R %d, P %d' % (mu, B['n'], mm(B['A2_rel_R']), mm(B['A2_rel_P']), mm(B['M_rel_R']),
                                           mm(B['M_rel_P']), mm(B['faktor_A2_durch_M_R']), mm(B['faktor_A2_durch_M_P']),
                                           B['n_M_kleiner_R'], B['n_M_kleiner_P'], B['n_M_negativ_R'], B['n_M_negativ_P']))
    L += ['', '## Gepaarte Verhaeltnisse |dH(mu_a)| / |dH(mu_b)| und Exponent p = log10', '']
    for k, S in o['verhaeltnisse'].items():
        L.append('- %s (n = %d): A2 R %s, P %s; M R %s (p %s), M P %s (p %s)' % (
            k, S['n'], mm(S['A2_R']), mm(S['A2_P']), mm(S['M_R']), mm(S['M_R_p']), mm(S['M_P']), mm(S['M_P_p'])))
        for q in S['liste']:
            L.append('  - s%d f%d %s %s: A2 R %s P %s; M R %s P %s' % (q['saat'], q['nr'], q['art'], q['zug'], g3(q['A2_R']),
                                                                     g3(q['A2_P']), g3(q['M_R']), g3(q['M_P'])))
    L += ['', '## Kontrollen', '', '```', json.dumps(o['kontrollen'], indent=1), '```', '',
          '## Kontrolllaeufe (Hubfolge umgekehrt, h = 2^-12; Referenz = Hauptlauf)', '', '```',
          json.dumps(o['kontrolllaeufe'], indent=1), '```', '', '## Ungueltig', '', json.dumps(o['ungueltig'])]
    with open(pfad + '.tmp', 'w') as fh:
        fh.write('\n'.join(L) + '\n')
    os.replace(pfad + '.tmp', pfad)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ordner', default='lauf')
    ap.add_argument('--out', required=True)
    ap.add_argument('--md', required=True)
    a = ap.parse_args()
    o = auswerten(a.ordner)
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(o, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    markdown(o, a.md)
    print('fertig auswertung', o['n_gueltig'], 'Zuege', flush=True)


if __name__ == '__main__':
    main()
