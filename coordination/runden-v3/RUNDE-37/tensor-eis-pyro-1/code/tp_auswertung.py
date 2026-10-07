#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TENSOR-EIS-PYRO-1: mechanische Auswertung nach PLAN.md (Urteile TE0 bis TE3, nach Plan und nach Kartenwortlaut)."""
import argparse, json, os, hashlib, time
import numpy as np

AV = np.array([[0., .5, .5], [.5, 0., .5], [.5, .5, 0.]])
LBAR = float(np.linalg.norm(AV[0]))
STRAHLEN = {'kubisch': {'100': ((1, 0, 0), range(4, 17)), '110': ((1, 1, 0), range(3, 12)), '111': ((1, 1, 1), range(3, 10))},
            'pyro': {'100': ((-1, 1, 1), range(3, 12)), '110': ((0, 0, 1), range(4, 17)), '111': ((1, 1, 1), range(2, 7))}}
STRAHLEN_LP = {'100': ((-1, 1, 1), range(2, 6)), '110': ((0, 0, 1), range(2, 9)), '111': ((1, 1, 1), range(1, 4))}


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def lade_statik(lauf, praefix):
    U, n, meta = {}, None, []
    for fn in sorted(os.listdir(lauf)):
        if fn.startswith(praefix) and fn.endswith('.npz'):
            d = np.load(os.path.join(lauf, fn))
            n = d['n']
            for key in d.files:
                if key.startswith('U_L'):
                    U[int(key[3:])] = d[key]
            with open(os.path.join(lauf, fn[:-4] + '.json')) as f:
                meta.append(json.load(f))
    return n, U, meta


def torus(U, Ls):
    A = np.array([[1.0, 1.0 / L, 1.0 / L ** 3] for L in Ls])
    Y = np.stack([U[L] for L in Ls], 0)
    return np.linalg.solve(A, Y)[0]


def radien(modell, n):
    if modell == 'kubisch':
        return np.linalg.norm(n.astype(float), axis=1)
    return np.linalg.norm(n @ AV, axis=1) / LBAR


def steigung(r, U):
    x, y = np.log(r), np.log(np.abs(U))
    return -float(np.polyfit(x, y, 1)[0])


def analyse(modell, n, Uinf, r, rmin, rmax, strahlen):
    idx = {tuple(v): i for i, v in enumerate(n)}
    out = {'strahlen': {}}
    for nm, (d, js) in strahlen.items():
        ii = [idx[tuple(j * np.array(d))] for j in js]
        rr, uu = r[ii], Uinf[ii]
        sel = (rr >= rmin - 1e-9) & (rr <= rmax + 1e-9)
        out['strahlen'][nm] = {'r': rr.tolist(), 'U': uu.tolist(), 'p': steigung(rr[sel], uu[sel]),
                               'steigt_nach_aussen': bool(np.all(np.diff(uu[sel]) > 0)),
                               'faellt_nach_aussen': bool(np.all(np.diff(uu[sel]) < 0))}
    sel = (r >= rmin - 1e-9) & (r <= rmax + 1e-9)
    out['schale'] = {'anzahl': int(sel.sum()), 'p': steigung(r[sel], Uinf[sel])}
    C = -Uinf[sel] * r[sel]
    out['vorfaktor'] = {'mittel': float(C.mean()), 'min': float(C.min()), 'max': float(C.max()),
                        'streuung': float((C.max() - C.min()) / abs(C.mean())),
                        'arg_min': n[sel][np.argmin(C)].tolist(), 'arg_max': n[sel][np.argmax(C)].tolist()}
    out['U_max_im_fenster'] = float(Uinf[sel].max())
    out['alle_negativ'] = bool(np.all(Uinf[sel] < 0))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--fit_kub', default='128,192,256;64,128,256')     # nur fuer Rauchlaeufe aendern
    ap.add_argument('--fit_pyro', default='128,160,192;96,128,192')
    a = ap.parse_args()
    fk = [tuple(int(x) for x in s.split(',')) for s in a.fit_kub.split(';')]
    fp = [tuple(int(x) for x in s.split(',')) for s in a.fit_pyro.split(';')]
    t0 = time.time()
    res = {'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'skript_sha256': sha(os.path.abspath(__file__))}
    eing = {}
    for fn in sorted(os.listdir(a.lauf)):
        if fn.endswith('.json') and fn != os.path.basename(a.out):
            with open(os.path.join(a.lauf, fn)) as f:
                try:
                    eing[fn] = json.load(f).get('info', {}).get('skript_sha256')
                except Exception:
                    eing[fn] = None
    res['eingaben_skript_sha256'] = eing
    urteile = {}
    # ---------------- TE1 (Schritt 1)
    with open(os.path.join(a.lauf, 'zaehlung.json')) as f:
        Z = json.load(f)
    g = Z['gleitkomma']
    ex = Z['exakt']
    b1 = g['zufall']['A']['rang_verteilung'] == {'12': g['zufall']['A']['n']}
    b2 = g['gitter']['A']['rangarm_ohne_ebene'] == 0
    b3 = all(z['rang_A'] == 12 for z in ex['allgemein'])
    haupt = b1 and b2 and b3
    flaeche = all(v['A_rang_verteilung'] == {'11': sum(v['A_rang_verteilung'].values())} for v in g['ebenen'].values()) and \
        all(z['rang_A'] == 11 for z in ex['ebene'])
    klammer = not flaeche
    urteile['TE1'] = {'nach_plan': 'eingetroffen' if haupt else 'nicht eingetroffen',
                      'nach_kartenwortlaut': 'eingetroffen' if (haupt and klammer) else 'nicht eingetroffen',
                      'kennzahlen': {'zufall_rang12_alle': b1, 'rangarm_ohne_ebene': g['gitter']['A']['rangarm_ohne_ebene'],
                                     'exakt_allgemein_rang12': b3, 'ebenen_flaechig_rangarm': flaeche,
                                     'n_s_gleich_n_fam': g['gitter']['A']['n_s_gleich_n_fam_alle'],
                                     'exakt_raenge': {k: sorted(set(z['rang_A'] for z in v)) for k, v in ex.items()},
                                     'det_quotient': g['det_quotient']}}
    res['schritt1'] = {
        'B1': {'rang_k_ungleich_0': g['gitter']['B1']['rang_k_ungleich_0'], 'zufall': g['zufall']['B1']['rang_verteilung'],
               'exakt': {k: sorted(set(z['rang_B1'] for z in v)) for k, v in ex.items()},
               'bloecke': g['B1_bloecke'], 'n_glatt': g['klein_k']['B1']['eps_1e-09']['n_glatt_menge'],
               'n_versetzt': g['klein_k']['B1']['eps_1e-09']['n_versetzt_menge']},
        'B2': {'rang_gitter': g['gitter']['B2']['rang_verteilung'], 'zufall': g['zufall']['B2']['rang_verteilung'],
               'exakt': {k: sorted(set(z['rang_B2'] for z in v)) for k, v in ex.items()},
               'n_glatt_je_richtung': g['klein_k']['B2']['eps_1e-09']['n_glatt'],
               'n_versetzt_je_richtung': g['klein_k']['B2']['eps_1e-09']['n_versetzt']}}
    # ---------------- Statik: TE0 (kubisch) und TE3 (Finns Netz, Kopie 1)
    stat = {}
    res['fitsaetze'] = {'kubisch': fk, 'pyro': fp}
    for modell, praefix, Ls, Ls_alt in (('kubisch', 'statik-kub', fk[0], fk[1]),
                                        ('pyro', 'statik-pyro', fp[0], fp[1])):
        n, U, meta = lade_statik(a.lauf, praefix)
        Uinf = torus(U, Ls)
        Ualt = torus(U, Ls_alt)
        r = radien(modell, n)
        z = {'L': sorted(U.keys()), 'fit': Ls, 'fit_alt': Ls_alt,
             'meta': [{k: l[k] for k in ('L', 't_kern_s', 'stat', 'G0', 'mittel', 'spiegel_max')} for m in meta for l in m['laeufe']]}
        sel = (r >= 2 - 1e-9) & (r <= 16 + 1e-9)
        z['torus_unsicherheit_rel_max'] = float((np.abs(Uinf - Ualt)[sel] / np.abs(Uinf[sel])).max())
        z['roh_gegen_inf_bei_Lmax_r16'] = None
        z['analyse_4_16'] = analyse(modell, n, Uinf, r, 4.0, 16.0, STRAHLEN[modell])
        if modell == 'kubisch':
            s8 = (r >= 8 - 1e-9) & (r <= 16 + 1e-9)
            dev = Uinf[s8] * 8 * np.pi * r[s8] + 1.0
            s4 = (r >= 4 - 1e-9) & (r <= 16 + 1e-9)
            dev4 = Uinf[s4] * 8 * np.pi * r[s4] + 1.0
            z['abw_8pi_r_ab8_max'] = float(np.abs(dev).max())
            z['abw_8pi_r_ab4_max'] = float(np.abs(dev4).max())
            z['zeilen'] = [{'n': list(v), 'r': float(rr), 'U_inf': float(u), 'U_8pir_plus1': float(u * 8 * np.pi * rr + 1)}
                           for v, rr, u in zip(n, r, Uinf) if tuple(v) in {(2, 0, 0), (4, 0, 0), (8, 0, 0), (16, 0, 0), (3, 3, 0), (8, 8, 0), (11, 11, 0), (3, 3, 3), (6, 6, 6), (9, 9, 9)}]
            ok = z['abw_8pi_r_ab8_max'] <= 0.01
            urteile['TE0'] = {'nach_plan': 'eingetroffen' if ok else 'nicht eingetroffen',
                              'nach_kartenwortlaut': 'eingetroffen' if ok else 'nicht eingetroffen',
                              'kennzahlen': {'max_abw_ab_r8': z['abw_8pi_r_ab8_max'], 'max_abw_ab_r4': z['abw_8pi_r_ab4_max'],
                                             'torus_unsicherheit': z['torus_unsicherheit_rel_max']}}
        else:
            an = z['analyse_4_16']
            # Kartenwortlaut: r in Kantenlaengen l_P = LBAR/2, Fenster 4 <= r/l_P <= 16, also 2 <= r/LBAR <= 8
            an_lp = analyse(modell, n, Uinf, r, 2.0, 8.0, STRAHLEN_LP)
            z['analyse_lP_4_16'] = an_lp
            z['G_eff_8pi'] = float(8 * np.pi * an['vorfaktor']['mittel'])

            def te3(x):
                ps = [x['strahlen'][s]['p'] for s in x['strahlen']] + [x['schale']['p']]
                c1 = x['alle_negativ']
                c2 = all(x['strahlen'][s]['steigt_nach_aussen'] for s in x['strahlen'])
                c3 = all(0.98 <= p <= 1.02 for p in ps)
                c4 = x['vorfaktor']['streuung'] <= 0.03
                return (c1 and c2 and c3 and c4), {'negativ': c1, 'anziehend': c2, 'exponenten': ps, 'exponent_ok': c3,
                                                   'streuung': x['vorfaktor']['streuung'], 'streuung_ok': c4}
            ok_p, kz_p = te3(an)
            ok_k, kz_k = te3(an_lp)
            urteile['TE3'] = {'nach_plan': 'eingetroffen' if ok_p else 'nicht eingetroffen',
                              'nach_kartenwortlaut': 'eingetroffen' if ok_k else 'nicht eingetroffen',
                              'kennzahlen': {'plan_r_in_staeben_4_16': kz_p, 'karte_r_in_lP_4_16': kz_k,
                                             'torus_unsicherheit': z['torus_unsicherheit_rel_max'],
                                             'G_eff_8pi': z['G_eff_8pi']},
                              'vermerk': 'Massen in verschiedenen Kopien (Auf- gegen Ab-Mitte) wechselwirken nicht (Entkopplung, PLAN 1.3)'}
        stat[modell] = z
    res['statik'] = stat
    # ---------------- TE2 (Spektrum auf der Zwangsflaeche, ganzes Netz = Kopie 1 + Kopie 2)
    with open(os.path.join(a.lauf, 'spektrum.json')) as f:
        SP = json.load(f)['spektren']
    p1, p2 = SP['pyro1'], SP['pyro2']
    assert p1['phys']['m_je_k'] == p2['phys']['m_je_k']
    summe = np.array(p1['phys']['positiv_je_k']) + np.array(p2['phys']['positiv_je_k'])
    verteilung = {str(int(x)): int((summe == x).sum()) for x in np.unique(summe)}
    ca = bool(np.all(summe == 2))
    tt, lin, w2pos, v2 = [], [], [], {}
    for nm, sp in (('pyro1', p1), ('pyro2', p2)):
        for z in sp['klein_k']:
            e1, e2 = z['eps_0.001'], z['eps_0.002']
            for j, w in enumerate(e1['w2_ueber_k2']):
                if w > 0:
                    tt.append(e1['tt_anteil'][j])
                    lin.append(abs(e2['w2_ueber_k2'][j] / w - 1.0))
                    w2pos.append(w)
            v2.setdefault(nm, {})[z['richtung']] = e1['w2_ueber_k2']
    cb = len(tt) > 0 and min(tt) >= 0.99
    cc = len(lin) > 0 and max(lin) <= 0.01
    ok2 = ca and cb and cc
    iso = {}
    for nm in v2:
        arr = np.array([v2[nm][d] for d in v2[nm]])
        iso[nm] = {'w2_ueber_k2_min_je_zweig': arr.min(0).tolist(), 'w2_ueber_k2_max_je_zweig': arr.max(0).tolist(),
                   '100': v2[nm]['100'], '110': v2[nm]['110'], '111': v2[nm]['111']}
    urteile['TE2'] = {'nach_plan': 'eingetroffen' if ok2 else 'nicht eingetroffen',
                      'nach_kartenwortlaut': 'eingetroffen' if ok2 else 'nicht eingetroffen',
                      'kennzahlen': {'positive_moden_ganzes_netz_verteilung': verteilung, 'genau_zwei_ueberall': ca,
                                     'je_kopie': {'pyro1': p1['phys']['positiv_je_k_verteilung'], 'pyro2': p2['phys']['positiv_je_k_verteilung']},
                                     'tt_anteil_min': min(tt) if tt else None, 'helizitaet2_ok': cb,
                                     'linear_abw_max': max(lin) if lin else None, 'linear_ok': cc,
                                     'tempo_quadrat': iso,
                                     'A_phys_neg_anteil': {nm: SP[nm]['phys']['A_phys_neg_anteil'] for nm in ('pyro1', 'pyro2')},
                                     'B_phys_neg_anteil': {nm: SP[nm]['phys']['B_phys_neg_anteil'] for nm in ('pyro1', 'pyro2')},
                                     'spur_eichdefekt': {nm: SP[nm]['spur_eichdefekt'] for nm in ('pyro1', 'pyro2')},
                                     'frei_ohne_zwang': {nm: SP[nm]['frei'] for nm in ('pyro1', 'pyro2')}}}
    kub = SP['kubisch']
    res['spektrum_kontrolle_kubisch'] = {'positiv_je_k_verteilung': kub['phys']['positiv_je_k_verteilung'],
                                         'w2_ueber_k2_100_110_111': [z['eps_0.001']['w2_ueber_k2'] for z in kub['klein_k'][:3]],
                                         'tt_anteil_min': min(min(z['eps_0.001']['tt_anteil']) for z in kub['klein_k']),
                                         'spur_eichdefekt': kub['spur_eichdefekt'], 'kontr': kub['kontr']}
    res['spektrum_kontr'] = {nm: SP[nm]['kontr'] for nm in SP}
    res['kontinuum_B_eichfrei'] = {nm: [z['B_eichfrei_ueber_k2'] for z in SP[nm]['klein_k'][:3]] for nm in SP}
    with open(os.path.join(a.lauf, 'kontrolle.json')) as f:
        res['kontrolle'] = json.load(f)
    res['urteile'] = urteile
    res['laufzeit_s'] = time.time() - t0
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig auswertung', {k: (v['nach_plan'], v['nach_kartenwortlaut']) for k, v in urteile.items()}, flush=True)


if __name__ == '__main__':
    main()
