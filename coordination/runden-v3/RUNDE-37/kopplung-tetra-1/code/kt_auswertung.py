#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KOPPLUNG-TETRA-1: mechanische Urteile KT0 bis KT3 nach PLAN.md Abschnitt 4 (nach Plan und nach Kartenwortlaut)."""
import argparse, json, os, hashlib, time


def lade(p):
    with open(p) as f:
        return json.load(f)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def kt0(ko):
    c1 = ko['einzel']['max_abw'] <= 1e-12
    pa = ko['paar']
    c2 = (pa['n_null'] == 9 and not pa['dreifach_positiv'] and pa['t2_summe_vielfach'] == 6
          and sorted(pa['t2_muster']) == [1, 1, 2, 2])
    u = 'eingetroffen' if (c1 and c2) else 'nicht eingetroffen'
    return {'nach_plan': u, 'nach_kartenwortlaut': u,
            'kennzahlen': {'einzel_max_abw': ko['einzel']['max_abw'], 'paar_n_null': pa['n_null'],
                           'paar_dreifach_positiv': pa['dreifach_positiv'], 'paar_t2_muster': pa['t2_muster'],
                           'paar_t2_summe_vielfach': pa['t2_summe_vielfach'], 'paar_t2_stufen': pa['t2_stufen'],
                           'paar_delta_T2_rel': pa['delta_T2_rel'],
                           'paar_T2_projiziert': pa['T2_projiziert'],
                           'gekoppelt_delta_T2_rel': {k: v['delta_T2_rel'] for k, v in ko['gekoppelt'].items()},
                           'gekoppelt_T2_projiziert_delta': {k: v['T2_projiziert']['delta_rel']
                                                              for k, v in ko['gekoppelt'].items()}},
            'teile': {'einzel': c1, 'paar': c2}}


def saetze(ru):
    s = {'gitter': ru['gitter'], 'zufall': ru['zufall']}
    for k, v in ru['ebenen'].items():
        s['ebene_' + k] = v
    for k, v in ru['linien'].items():
        s['linie_' + k] = v
    return s


def kt1(ru):
    eb0 = sum(v['n_a_verteilung'].get('0', 0) for v in ru['ebenen'].values())
    zuf_ok = ru['zufall']['n_a_verteilung'] == {'0': ru['zufall']['punkte']}
    plan = eb0 == 0 and zuf_ok
    wort = plan and ru['gitter']['n_a_ge1_ausserhalb'] == 0 and ru['zufall']['n_a_ge1_ausserhalb'] == 0
    return {'nach_plan': 'eingetroffen' if plan else 'nicht eingetroffen',
            'nach_kartenwortlaut': 'eingetroffen' if wort else 'nicht eingetroffen',
            'kennzahlen': {'ebenenpunkte_ohne_rum': eb0,
                           'ebenenpunkte': sum(v['punkte'] for v in ru['ebenen'].values()),
                           'zufall_n_a_verteilung': ru['zufall']['n_a_verteilung'],
                           'gitter_rum_ausserhalb_der_scharen': ru['gitter']['n_a_ge1_ausserhalb'],
                           'gitter_n_a_verteilung': ru['gitter']['n_a_verteilung']},
            'vermerk': 'vorab an der Quelle belegt (Wegner 2007, Gl. 44) und vorab ableitbar (PLAN 2.3); Kontrolle'}


def kt2(ru):
    s = saetze(ru)
    ab = {k: v['n_a_ungleich_n_b'] for k, v in s.items()}
    g = ru['gitter']
    ka = ru['kernabbildung']
    plan = (sum(ab.values()) == 0 and g['n_a_ungleich_n_fam'] == 0 and g['k0_n_a'] == 6
            and ka['residuum_max'] <= 1e-9 and ka['dim_ungleich'] == 0)
    mab = {k: v['menge_ungleich_ab'] for k, v in s.items()}
    mfam = {k: v['menge_ungleich_fam'] for k, v in s.items()}
    wort = sum(mab.values()) == 0 and sum(mfam.values()) == 0
    return {'nach_plan': 'eingetroffen' if plan else 'nicht eingetroffen',
            'nach_kartenwortlaut': 'eingetroffen' if wort else 'nicht eingetroffen',
            'kennzahlen': {'n_a_ungleich_n_b': ab, 'gitter_n_a_ungleich_n_fam': g['n_a_ungleich_n_fam'],
                           'k0_n_a': g['k0_n_a'], 'gitter_tabelle_n_fam_n_a': g['tabelle_n_fam_n_a'],
                           'kern_residuum_max': ka['residuum_max'], 'kern_hauptwinkel_max': ka['hauptwinkel_1_minus_cos_max'],
                           'kern_dim_ungleich': ka['dim_ungleich'], 'kern_punkte': ka['punkte'],
                           'menge_ungleich_ab': mab, 'menge_ungleich_fam': mfam},
            'vermerk': 'vorab ableitbar (PLAN 2.3: ker K = ker C_A; Wegner Gl. 41 bis 44; TENSOR-EIS-PYRO-1); Kontrolle'}


def werkzeug_ok(ko):
    w = ko['werkzeug']
    e, m = w['eichform']['H+'], w['massenform']['H+']
    ok = e['U'] <= 1e-12 and e['G'] <= 1e-12 and m['U'] >= 0.5 and m['G'] >= 1 - 1e-12
    return ok, {'eichform_U': e['U'], 'eichform_G': e['G'], 'massenform_U': m['U'], 'massenform_G': m['G']}


def urteil_eich(ei, L, e_ref):
    v = ei['haupt']['L%d' % L]['varianten']['V3']['H+']
    lmax = v['lambda_max']
    if lmax <= 1e-8 * e_ref:
        return 'nicht eingetroffen (entartet)', 'nicht auswertbar (entartet, 0/0)', lmax
    plan = 'eingetroffen' if v['U'] < 0.05 else 'nicht eingetroffen'
    wort = 'eingetroffen' if v['U_K'] < 0.05 else 'nicht eingetroffen'
    return plan, wort, lmax


def kt3(ei, ko):
    wok, wz = werkzeug_ok(ko)
    Ls = sorted(ei['L_liste'])
    e_ref = ei['e_ref']
    Lm = Ls[-1]
    plan, wort, lmax = urteil_eich(ei, Lm, e_ref)
    konv = None
    if len(Ls) >= 2:
        p2, w2, _ = urteil_eich(ei, Ls[-2], e_ref)
        konv = (p2 == plan and w2 == wort)
    if not wok:
        plan = wort = 'nicht auswertbar (Werkzeugprobe W nicht bestanden)'
    tab = {}
    for rn in ('haupt', 'gegen'):
        for L in Ls:
            o = ei[rn]['L%d' % L]
            for vn, vv in o['varianten'].items():
                for h in ('H+', 'H-'):
                    x = vv[h]
                    tab['%s L%d %s %s' % (rn, L, vn, h)] = {
                        'lambda_max_rel': x['lambda_max'] / e_ref, 'U': x['U'], 'U_K': x['U_K'], 'G': x['G']}
            tab['%s L%d dim_W_V3' % (rn, L)] = o['V3_dim_W']
            tab['%s L%d dim_W36_V2' % (rn, L)] = o['V2_dim_W36']
    dicht = {rn: ei[rn].get('dicht_L%d' % ei['dicht_L']) for rn in ('haupt', 'gegen')}
    v3 = ei['haupt']['L%d' % Lm]['varianten']['V3']['H+']
    return {'nach_plan': plan, 'nach_kartenwortlaut': wort,
            'kennzahlen': {'L': Lm, 'e_ref': e_ref, 'lambda_max_V3': lmax, 'lambda_max_V3_rel': lmax / e_ref,
                           'U_V3': v3['U'], 'U_K_V3': v3['U_K'], 'G_V3': v3['G'],
                           'dim_W_V3': ei['haupt']['L%d' % Lm]['V3_dim_W'],
                           'urteil_gleich_beim_zweitgroessten_L': konv, 'werkzeugprobe': wz, 'werkzeug_ok': wok},
            'tabelle_beschreibend': tab,
            'dichte_gegenprobe': {rn: ({vn: {'max_abw': d['max_abw'], 'skala': d['skala']} for vn, d in dd.items()}
                                       if dd else None) for rn, dd in dicht.items()}}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--lauf', required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()
    pk, pr, pe = (os.path.join(a.lauf, x) for x in ('kontrolle.json', 'rum.json', 'eich.json'))
    ko, ru, ei = lade(pk), lade(pr), lade(pe)
    res = {'KT0': kt0(ko), 'KT1': kt1(ru), 'KT2': kt2(ru), 'KT3': kt3(ei, ko),
           'eingaben': {x: {'sha256': sha(x), 'sha256_kt': lade(x)['laufinfo']['sha256_kt']} for x in (pk, pr, pe)},
           'sha256_auswertung': sha(os.path.abspath(__file__)),
           'zeit_utc': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}
    with open(a.out, 'w') as f:
        json.dump(res, f, indent=1)
    for k in ('KT0', 'KT1', 'KT2', 'KT3'):
        print(k, 'Plan:', res[k]['nach_plan'], '| Kartenwortlaut:', res[k]['nach_kartenwortlaut'], flush=True)


if __name__ == '__main__':
    main()
