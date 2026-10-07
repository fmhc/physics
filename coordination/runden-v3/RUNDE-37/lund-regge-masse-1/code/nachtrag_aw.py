#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LUND-REGGE-MASSE-1: Auswertungs-Nachtrag (nach dem Einfrieren geschrieben, liest nur die Laufdateien).

Mechanisch nach PLAN 7 (LR0 bis LR4) und beschreibende Zusammenfassungen (keine neue Physikrechnung):
  - LR3: Mittel der Glas-Spannen bei kl = 0,05 (LR gegen A1R1), Regel wie PLAN 7.
  - Kristalle: Lage der instabilen k (kleinstes |k| l im ersten Brillouin-Bereich), Staerke, Spurdiagnose.
  - kl = 0,2 beschreibend (Werte auch ohne Lueckenregel).
Aufruf nur ueber kleintest.sh: python nachtrag_aw.py --lauf lauf --out lauf/auswertung.json
"""
import argparse, json, os, sys, itertools, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402
import hm  # noqa: E402


def lade(p):
    with open(p) as fh:
        return json.load(fh)['ergebnis']


def kmin_norm(k, BVc):
    best = np.linalg.norm(k)
    for n in itertools.product((-1, 0, 1), repeat=3):
        best = min(best, float(np.linalg.norm(k - np.array(n, float) @ BVc)))
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', default='lauf')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    L = a.lauf
    out = {'sha256_skript': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()}
    lr0 = lade(os.path.join(L, 'lr0.json'))
    out['LR0'] = {'fehler_max_je_netz': {n: d['LR0_fehler_max'] for n, d in lr0.items()},
                  'fehler_max': max(d['LR0_fehler_max'] for d in lr0.values()),
                  'K1_max': max(d['K1_karte_gleich_4vref_Kt'] for d in lr0.values())}
    out['LR0']['eingetroffen'] = bool(out['LR0']['fehler_max'] <= 1e-12)
    sp = {}
    for n in ('V', 'S', 'A15', 'glas-s1', 'glas-s2', 'glas-s3', 'glas-s4'):
        p = os.path.join(L, 'sp-%s.json' % n)
        if os.path.exists(p):
            sp[n] = lade(p)
    out['LR1'] = {n: {'spanne0': sp[n]['LR']['extrapolation']['spanne0'], 'alle_ok': sp[n]['LR']['extrapolation']['alle_ok'],
                      's2': sp[n]['LR'].get('spanne_kl2_fit', {}).get('s2')} for n in ('V', 'S', 'A15') if n in sp}
    out['LR1']['eingetroffen'] = bool(all(out['LR1'][n]['alle_ok'] and out['LR1'][n]['spanne0'] < 1e-6 for n in ('V', 'S', 'A15')))
    g = lade(os.path.join(L, 'gang.json'))
    out['LR2'] = {'gang': g['LR']['gang']['gang'] if 'LR' in g else None, 'A_red_nicht_pd': g['A_red_nicht_pd']}
    out['LR2']['eingetroffen'] = bool(g['A_red_nicht_pd'] == 0 and abs(out['LR2']['gang']) < 1e-3)
    # LR3
    z3 = {}
    for s in (1, 2, 3, 4):
        n = 'glas-s%d' % s
        if n not in sp:
            continue
        d = sp[n]
        z3[n] = {'LR_spanne': d['LR']['je_kl']['0.05']['spanne'], 'LR_alle_ok': d['LR']['je_kl']['0.05']['alle_ok'],
                 'LR_n_ok': d['LR']['je_kl']['0.05']['n_ok'], 'LR_n_neg_max': d['LR']['je_kl']['0.05']['n_neg_max'],
                 'A1_spanne': d['A1R1']['je_kl']['0.05']['spanne'], 'A1_alle_ok': d['A1R1']['je_kl']['0.05']['alle_ok']}
    # beschreibend (nicht Plan): Spanne aus allen Punkten mit zwei positiven betragsgroessten 1/omega^2, ohne Lueckenregel
    for n in list(z3.keys()):
        for schl, tag in (('LR', 'LR'), ('A1R1', 'A1')):
            for kl in ('0.01', '0.05'):
                ww, lu, npos = [], [], 0
                for z in sp[n]['zeilen']:
                    r = z['kl' + kl].get(schl)
                    if r is not None and r.get('pos2') and len(r.get('w2k2', [])) == 2:
                        ww += r['w2k2']
                        lu.append(r['luecke'])
                        npos += 1
                z3[n]['%s_beschr_kl%s' % (tag, kl)] = {'spanne': float(max(ww) / min(ww) - 1) if ww else None, 'n_pos2': npos,
                                                       'luecke_bereich': [float(min(lu)), float(max(lu))] if lu else None}
    ok_alle = len(z3) == 4 and all(v['LR_alle_ok'] for v in z3.values())
    mLR = float(np.mean([v['LR_spanne'] for v in z3.values() if v['LR_spanne'] is not None])) if z3 else None
    mA1 = float(np.mean([v['A1_spanne'] for v in z3.values() if v['A1_spanne'] is not None])) if z3 else None
    out['LR3'] = {'je_saat': z3, 'mittel_LR_ok_punkte': mLR, 'mittel_A1R1': mA1,
                  'verhaeltnis': (mLR / mA1) if (mLR is not None and mA1) else None, 'alle_saaten_alle_ok': bool(ok_alle)}
    out['LR3']['eingetroffen'] = bool(ok_alle and mLR is not None and mLR <= 0.5 * mA1)
    bL = [v['LR_beschr_kl0.05']['spanne'] for v in z3.values() if v['LR_beschr_kl0.05']['spanne'] is not None]
    bA = [v['A1_beschr_kl0.05']['spanne'] for v in z3.values() if v['A1_beschr_kl0.05']['spanne'] is not None]
    out['LR3']['beschreibend_mittel_LR_kl005'] = float(np.mean(bL)) if bL else None
    out['LR3']['beschreibend_mittel_A1_kl005'] = float(np.mean(bA)) if bA else None
    # LR4 und Stabilitaet
    st = {}
    for n in ('V', 'S', 'A15', 'glas-s1', 'glas-s2', 'glas-s3', 'glas-s4'):
        p = os.path.join(L, 'st-%s.json' % n)
        if os.path.exists(p):
            st[n] = lade(p)
    out['stabil'] = {n: d['zusammen'] for n, d in st.items()}
    out['LR4'] = {n: {'k_singulaer': st[n]['zusammen']['k_K_singulaer'], 'k_wachsend': st[n]['zusammen']['k_wachsend']}
                  for n in ('V', 'S') if n in st}
    out['LR4']['eingetroffen'] = bool(all(out['LR4'][n]['k_singulaer'] == 0 and out['LR4'][n]['k_wachsend'] == 0 for n in ('V', 'S')))
    # Lage und Staerke der Instabilitaet (Kristalle und Glas)
    lage = {}
    for n, d in st.items():
        net = hm.netz(n)
        LV = np.asarray(net[0], float)
        BVc = 2 * np.pi * np.linalg.inv(LV).T
        ng = d['gitter_n']
        l = sp[n]['l_mittel'] if n in sp else None
        kl_inst, kl_stab, wrel, a_rel, spur, weyl, kform = [], [], [], [], [], [], []
        for p in d['zeilen']:
            if not any(p['m']) or not p.get('legendre_regulaer'):
                continue
            k = (np.array(p['m'], float) / ng) @ BVc
            kn = kmin_norm(k, BVc) * (l if l else 1.0)
            if p['n_wachsend'] > 0:
                kl_inst.append(kn)
                wrel.append(p['w2_min_rel'])
                a_rel.append(p['A_red']['min_rel'])
                spur.append(p['diag']['spur_neg_mittel'])
                weyl.append(p['diag']['weyl_neg_mittel'])
                kform.append(p['diag']['Kform_neg_max'])
            else:
                kl_stab.append(kn)
        lage[n] = {'n_instabil': len(kl_inst), 'kl_min_instabil': float(min(kl_inst)) if kl_inst else None,
                   'kl_max_stabil': float(max(kl_stab)) if kl_stab else None,
                   'kl_min_gitter': float(min(kl_inst + kl_stab)) if (kl_inst or kl_stab) else None,
                   'w2_min_rel_median': float(np.median(wrel)) if wrel else None,
                   'A_red_min_rel_median': float(np.median(a_rel)) if a_rel else None,
                   'spur_neg_bereich': [float(min(spur)), float(max(spur))] if spur else None,
                   'weyl_neg_bereich': [float(min(weyl)), float(max(weyl))] if weyl else None,
                   'Kform_neg_naechst_null_median': float(np.median(kform)) if kform else None}
    out['lage_instabil'] = lage
    gam = {}
    for n, d in st.items():
        rows = [p for p in d['zeilen'] if not any(p['m'])]
        p = rows[0] if rows else d.get('gamma')
        if p:
            gam[n] = {'K_n_neg': p['K']['n_neg'], 'A_red_n_neg': p.get('A_red', {}).get('n_neg'),
                      'n_wachsend': p.get('n_wachsend'), 'diag': p.get('diag')}
    out['gamma'] = gam
    # benannte Richtungen bei kl = 0,01 und kl = 0,2 beschreibend
    ben = {}
    for n in ('V', 'S', 'A15'):
        if n not in sp:
            continue
        zz = {}
        for z in sp[n]['zeilen']:
            if z['richtung'] in ('100', '110', '111'):
                p1, p2 = z['kl0.01'], z['kl0.2']
                zz[z['richtung']] = {'LR_kl001': p1['LR']['w2k2'], 'affin_unproj_kl001': p1['affin_unproj'],
                                     'LR_rel_affin': [x / float(np.mean(p1['affin_unproj'])) for x in p1['LR']['w2k2']],
                                     'LR_kl02': p2.get('LR', {}).get('w2k2'), 'LR_kl02_ok': p2.get('LR', {}).get('ok'),
                                     'LR_kl02_luecke': p2.get('LR', {}).get('luecke'),
                                     'A1_kl02': p2.get('A1R1', {}).get('w2k2'), 'A1_kl02_luecke': p2.get('A1R1', {}).get('luecke')}
        ben[n] = zz
    out['benannt'] = ben
    # Glas: Spannen je kl, Extrapolation, Regularitaet
    gl = {}
    for s in (1, 2, 3, 4):
        n = 'glas-s%d' % s
        if n in sp:
            d = sp[n]
            gl[n] = {'LR_je_kl': {k: [v['spanne'], v['n_ok'], v['n_neg_max']] for k, v in d['LR']['je_kl'].items()},
                     'A1_je_kl': {k: [v['spanne'], v['n_ok']] for k, v in d['A1R1']['je_kl'].items()},
                     'LR_ex': d['LR']['extrapolation'], 'A1_ex': d['A1R1']['extrapolation'], 'l': d['l_mittel']}
    out['glas_spannen'] = gl
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig auswertung', flush=True)


if __name__ == '__main__':
    main()
