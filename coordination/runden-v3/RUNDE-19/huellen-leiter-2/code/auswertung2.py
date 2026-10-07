#!/usr/bin/env python3
"""auswertung2.py - Runde 19 HUELLEN-LEITER-2: K0, Stellen im Suchbereich, P0 bis P4, Geburten, Hintergrund,
Abbildung R <-> omega^2, Stichprobenliste und Abgleich Rechteck- gegen Zellen-Umlauf.
Grundlage: auswertung.py der Runde 18 (782058b1...), Stellenregel (PLAN 4 der Runde 18) unveraendert.
Regeln: PLAN.md (eingefroren), Abschnitte 3 bis 6."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import math
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import stille3 as S3

schreibe = S3.schreibe
K0_PAARE = (0, 109)          # 88 bekannte Stellen (Runde 18, gewertet bis Paar 109)
NEU_PAARE = (110, 123)       # Suchbereich R 38,95 bis 45,98
TOL_K0 = 1e-8
# Karte: letzte bekannte Stelle je Kurve und vorhergesagte naechste Sprossen (R)
VORHERSAGE = {0: (37.18, [39.59, 42.00, 44.41]), 1: (38.40, [40.51, 42.62, 44.72]),
              2: (38.11, [40.24, 42.36, 44.49]), 3: (37.61, [39.77, 41.93, 44.09])}
P1_TOL = 0.10
P3_FENSTER = (40.5, 42.5)


def lade(adir, praefix, stufe):
    out = []
    for fn in sorted(os.listdir(adir)):
        if fn.startswith('%s-st%d-' % (praefix, stufe)) and fn.endswith('.json'):
            out.append(json.load(open(os.path.join(adir, fn))))
    return out


def rangsprung_plan(za, zb):
    ra = [q['rho'] for q in za['null']]
    rb = [q['rho'] for q in zb['null']]
    out = {}
    for k in range(min(len(ra), len(rb))):
        g = []
        for r in (ra, rb):
            if k > 0:
                g.append(r[k] - r[k - 1])
            if k + 1 < len(r):
                g.append(r[k + 1] - r[k])
        out[k] = bool(g and abs(ra[k] - rb[k]) > 0.5 * min(g))
    return out


def gemeinsam(kurven):
    """P4: je Unterzeilen-Intervall (j/8, (j+1)/8) die Zahl der Kurven mit Vorzeichenwechsel von s."""
    zaehl = [0] * 8
    for c in kurven:
        t, s = c['t'], c['s']
        for a in range(len(t) - 1):
            if np.sign(s[a]) != np.sign(s[a + 1]):
                j0 = int(math.floor(t[a] * 8 + 1e-9))
                j1 = int(math.ceil(t[a + 1] * 8 - 1e-9))
                for j in range(j0, j1):
                    zaehl[min(j, 7)] += 1
    return zaehl


def punkte_stufe(adir, stufe, jlo, jhi):
    paare = sorted([d for d in lade(adir, 'paar', stufe) if jlo <= d['i'] <= jhi], key=lambda d: d['i'])
    zs = {z['index']: z for z in lade(adir, 'z', stufe)}
    pk = []
    p4 = []
    kstat = dict(rangsprung=0, rangsprung_code=0, weg_unterzeile=0, gerade_fein_ungerade_zeile=0, kurven_paare=0)
    for d in paare:
        rs = rangsprung_plan(zs[d['i']], zs[d['i'] + 1])
        fein = sum(c['n_wechsel'] for c in d['kurven'])
        zeile = sum(c['n_wechsel_zeile'] for c in d['kurven'])
        zg = gemeinsam(d['kurven'])
        nk = len(d['kurven'])
        p4.append(dict(i=d['i'], n_kurven=nk, fein=fein, zeile=zeile,
                       kurven_ungleich=[c['k'] for c in d['kurven'] if c['n_wechsel'] != c['n_wechsel_zeile']],
                       max_gemeinsam=max(zg) if zg else 0,
                       alle_zugleich=bool(nk >= 2 and max(zg) >= nk)))
        for c in d['kurven']:
            kstat['kurven_paare'] += 1
            kstat['rangsprung'] += int(rs.get(c['k'], False))
            kstat['rangsprung_code'] += int(c['rangsprung'])
            kstat['weg_unterzeile'] += len(c['weg'])
            if (c['n_wechsel'] % 2) != c['n_wechsel_zeile']:
                kstat['gerade_fein_ungerade_zeile'] += 1
        for q in d['punkte']:
            q = dict(q)
            q['i'] = d['i']
            q['dw2_zeile'] = d['w2a'] - d['w2b']
            fl = []
            if q['weg']:
                fl.append('weg')
            if q['steig'] == 0:
                fl.append('steig')
            if rs.get(q['k']):
                fl.append('rangsprung')
            if abs(q['umlauf_zelle']) != 1:
                fl.append('umlauf0')
            q['merker'] = fl
            pk.append(q)
    return paare, pk, kstat, p4


def zeilen_stat(adir, stufe, ilo, ihi):
    zs = sorted([z for z in lade(adir, 'z', stufe) if ilo <= z['index'] <= ihi], key=lambda d: d['index'])
    out = []
    for z in zs:
        out.append(dict(index=z['index'], w2=z['w2'], Rchi=z.get('Rchi'), chi0=z.get('chi0'), Q=z.get('Q'), E=z.get('E'),
                        n=len(z['null']), unsicher=sum(1 for q in z['null'] if not q['sicher']),
                        rho=[q['rho'] for q in z['null']], s=[q['s'] for q in z['null']],
                        vz=z['vorzeichen'], maske=z.get('maske'), kopplung=z.get('kopplung')))
    return out


def stellen_bereich(adir, jlo, jhi):
    """Stellen in den Paaren jlo..jhi, Abgleich der Stufen wie Runde 18 (PLAN 4 dort)."""
    erg = {}
    P = {}
    for st in (1, 2):
        paare, pk, kstat, p4 = punkte_stufe(adir, st, jlo, jhi)
        P[st] = pk
        erg['st%d' % st] = dict(paare=sorted(d['i'] for d in paare), n_punkte=len(pk), kstat=kstat, p4=p4)
    z1 = {z['index']: z for z in zeilen_stat(adir, 1, jlo, jhi + 1)}
    z2 = {z['index']: z for z in zeilen_stat(adir, 2, jlo, jhi + 1)}
    gleich_n, gleich_vz, diff_rho, ungleich = 0, 0, 0.0, []
    for i in sorted(set(z1) & set(z2)):
        if z1[i]['n'] == z2[i]['n']:
            gleich_n += 1
            if z1[i]['vz'] == z2[i]['vz']:
                gleich_vz += 1
            else:
                ungleich.append(dict(i=i, w2=z1[i]['w2'], vz1=z1[i]['vz'], vz2=z2[i]['vz']))
            if z1[i]['n']:
                diff_rho = max(diff_rho, float(np.max(np.abs(np.array(z1[i]['rho']) - np.array(z2[i]['rho'])))))
        else:
            ungleich.append(dict(i=i, w2=z1[i]['w2'], n1=z1[i]['n'], n2=z2[i]['n']))
    erg['zeilenvergleich'] = dict(zeilen_beide=len(set(z1) & set(z2)), gleiche_zahl=gleich_n, gleiche_vorzeichen=gleich_vz,
                                  max_drho=diff_rho, abweichungen=ungleich[:40], n_abweichungen=len(ungleich),
                                  unsicher_st1=sum(z['unsicher'] for z in z1.values()),
                                  unsicher_st2=sum(z['unsicher'] for z in z2.values()))
    stellen, nur1, nur2 = [], [], []
    by2 = {}
    for q in P[2]:
        by2.setdefault((q['i'], q['k']), []).append(q)
    benutzt = set()
    for q in P[1]:
        cand = [(abs(r['w2'] - q['w2']), j, r) for j, r in enumerate(by2.get((q['i'], q['k']), []))
                if (q['i'], q['k'], j) not in benutzt]
        cand = [c for c in cand if c[0] <= q['dw2_zeile'] / 16.0]
        if not cand:
            nur1.append(q)
            continue
        cand.sort(key=lambda c: c[0])
        _, j, r = cand[0]
        benutzt.add((q['i'], q['k'], j))
        ok = (not q['merker']) and (not r['merker']) and q['umlauf_zelle'] == r['umlauf_zelle'] and abs(q['umlauf_zelle']) == 1
        stellen.append(dict(k=q['k'], i=q['i'], w2=q['w2'], rho=q['rho'], R=q['R'], w2_2=r['w2'], rho_2=r['rho'], R_2=r['R'],
                            dw2=r['w2'] - q['w2'], drho=r['rho'] - q['rho'], dR=r['R'] - q['R'],
                            umlauf_1=q['umlauf_zelle'], umlauf_2=r['umlauf_zelle'], kn_1=q['kn'], kn_2=r['kn'],
                            merker_1=q['merker'], merker_2=r['merker'], gezaehlt=bool(ok), gap=q['gap'],
                            dw2_zeile=q['dw2_zeile'], klammer_w2=q['w2_klammer'], klammer_R=q['R_klammer'],
                            sa=q['sa'], sb=q['sb']))
    for key, lst in by2.items():
        for j, r in enumerate(lst):
            if (key[0], key[1], j) not in benutzt:
                nur2.append(r)
    stellen.sort(key=lambda d: -d['w2'])
    for n, d in enumerate(stellen):
        d['nr_bereich'] = n + 1
    erg['stellen'] = stellen
    erg['nur_st1'] = [dict(i=q['i'], k=q['k'], w2=q['w2'], rho=q['rho'], R=q['R'], umlauf=q['umlauf_zelle'],
                           merker=q['merker']) for q in nur1]
    erg['nur_st2'] = [dict(i=r['i'], k=r['k'], w2=r['w2'], rho=r['rho'], R=r['R'], umlauf=r['umlauf_zelle'],
                           merker=r['merker']) for r in nur2]
    erg['n_gepaart'] = len(stellen)
    erg['n_gezaehlt'] = sum(1 for d in stellen if d['gezaehlt'])
    return erg


def cmd_k0(adir, refjson, newtondir, aus):
    ref = [d for d in json.load(open(refjson))['stellen'] if d['gezaehlt'] and d['bereich']]
    e = stellen_bereich(adir, *K0_PAARE)
    gez = [d for d in e['stellen'] if d['gezaehlt']]
    erw = set(range(K0_PAARE[0], K0_PAARE[1] + 1))
    fehl = dict(st1=sorted(erw - set(e['st1']['paare'])), st2=sorted(erw - set(e['st2']['paare'])))
    zu, frei = [], list(gez)
    for d in ref:
        c = [x for x in frei if x['i'] == d['i'] and x['k'] == d['k']]
        c.sort(key=lambda x: abs(x['w2'] - d['w2']))
        if not c:
            zu.append(dict(nr=d['nr'], gefunden=False))
            continue
        x = c[0]
        frei.remove(x)
        zu.append(dict(nr=d['nr'], k=d['k'], i=d['i'], R=d['R'], gefunden=True,
                       umlauf_alt=[d['umlauf_1'], d['umlauf_2']], umlauf_neu=[x['umlauf_1'], x['umlauf_2']],
                       umlauf_gleich=bool(d['umlauf_1'] == x['umlauf_1'] and d['umlauf_2'] == x['umlauf_2']),
                       dw2_st1=x['w2'] - d['w2'], drho_st1=x['rho'] - d['rho'],
                       dw2_st2=x['w2_2'] - d['w2_2'], drho_st2=x['rho_2'] - d['rho_2'], dR_st1=x['R'] - d['R']))
    gef = [z for z in zu if z['gefunden']]
    kette = dict(n_ref=len(ref), n_gezaehlt_neu=len(gez), n_zugeordnet=len(gef), zusaetzlich=[
        dict(i=x['i'], k=x['k'], w2=x['w2'], rho=x['rho'], R=x['R'], u=[x['umlauf_1'], x['umlauf_2']]) for x in frei],
        nicht_gezaehlt=[dict(i=x['i'], k=x['k'], w2=x['w2'], R=x['R'], m1=x['merker_1'], m2=x['merker_2'],
                             u=[x['umlauf_1'], x['umlauf_2']]) for x in e['stellen'] if not x['gezaehlt']],
        nur_st1=e['nur_st1'], nur_st2=e['nur_st2'], fehlende_paare=fehl,
        umlauf_gleich=sum(1 for z in gef if z['umlauf_gleich']),
        max_abs=dict(dw2_st1=max([abs(z['dw2_st1']) for z in gef] or [0]), drho_st1=max([abs(z['drho_st1']) for z in gef] or [0]),
                     dw2_st2=max([abs(z['dw2_st2']) for z in gef] or [0]), drho_st2=max([abs(z['drho_st2']) for z in gef] or [0]),
                     dR_st1=max([abs(z['dR_st1']) for z in gef] or [0])),
        n_lage_le_tol=sum(1 for z in gef if max(abs(z['dw2_st1']), abs(z['drho_st1']), abs(z['dw2_st2']),
                                                 abs(z['drho_st2'])) <= TOL_K0),
        n_lage_exakt=sum(1 for z in gef if z['dw2_st1'] == 0 and z['drho_st1'] == 0 and z['dw2_st2'] == 0 and
                         z['drho_st2'] == 0),
        je_stelle=zu, zeilenvergleich=e['zeilenvergleich'],
        p4_diag=dict(st1=[p for p in e['st1']['p4'] if p['kurven_ungleich'] or p['alle_zugleich']],
                     st2=[p for p in e['st2']['p4'] if p['kurven_ungleich'] or p['alle_zugleich']]))
    kette_ok = bool(len(gef) == len(ref) == 88 and len(gez) == 88 and not frei and
                    kette['umlauf_gleich'] == 88 and not fehl['st1'] and not fehl['st2'])
    # Newton-Lage alt gegen neu
    nw = {1: {}, 2: {}}
    for st in (1, 2):
        for fn in sorted(os.listdir(newtondir)):
            if fn.startswith('k0newton-st%d-' % st) and fn.endswith('.json'):
                for p in json.load(open(os.path.join(newtondir, fn)))['punkte']:
                    nw[st][p['nr']] = p
    nt = []
    for d in ref:
        z = dict(nr=d['nr'], k=d['k'], R=d['R'])
        ok = True
        for st in (1, 2):
            p = nw[st].get(d['nr'])
            if p is None:
                z['st%d' % st] = None
                ok = False
                continue
            z['st%d' % st] = dict(alt_ok=p['alt']['ok'], neu_ok=p['neu']['ok'], dw2=p['dw2'], drho=p['drho'],
                                  it=[p['alt']['it'], p['neu']['it']], svr=[p['alt']['svr'], p['neu']['svr']],
                                  maske_anker=p['maske_anker']['n_maske'],
                                  w2_neu=p['neu']['w2'], rho_neu=p['neu']['rho'],
                                  ab_start=[p['neu']['w2'] - p['start'][0], p['neu']['rho'] - p['start'][1]])
            if not (p['alt']['ok'] and p['neu']['ok'] and abs(p['dw2']) <= TOL_K0 and abs(p['drho']) <= TOL_K0):
                ok = False
        z['ok'] = ok
        nt.append(z)
    def mx(key, st):
        v = [abs(z['st%d' % st][key]) for z in nt if z.get('st%d' % st)]
        return max(v) if v else None
    newton = dict(n_ok=sum(1 for z in nt if z['ok']), n=len(nt),
                  max_abs=dict(dw2_st1=mx('dw2', 1), drho_st1=mx('drho', 1), dw2_st2=mx('dw2', 2), drho_st2=mx('drho', 2)),
                  nicht_ok=[z for z in nt if not z['ok']], je_stelle=nt,
                  max_ab_start=dict(st1=max([abs(z['st1']['ab_start'][0]) for z in nt if z.get('st1')] or [0]),
                                    st2=max([abs(z['st2']['ab_start'][0]) for z in nt if z.get('st2')] or [0])))
    newton_ok = bool(newton['n_ok'] == 88)
    erg = dict(kette=kette, kette_ok=kette_ok, newton=newton, newton_ok=newton_ok, K0_bestanden=bool(kette_ok and newton_ok))
    schreibe(aus, erg)
    print(json.dumps(dict(K0_bestanden=erg['K0_bestanden'], kette_ok=kette_ok, newton_ok=newton_ok,
                          n_gezaehlt_neu=len(gez), n_zugeordnet=len(gef), umlauf_gleich=kette['umlauf_gleich'],
                          zusaetzlich=len(frei), fehlende_paare=fehl, kette_max=kette['max_abs'],
                          kette_n_le_tol=kette['n_lage_le_tol'], kette_n_exakt=kette['n_lage_exakt'],
                          newton_n_ok=newton['n_ok'], newton_max=newton['max_abs'],
                          zeilenvergleich={k: kette['zeilenvergleich'][k] for k in ('zeilen_beide', 'gleiche_zahl',
                                                                                    'gleiche_vorzeichen', 'max_drho',
                                                                                    'n_abweichungen')}), indent=1))


def geburten(adir, stufe, ilo, ihi):
    zs = zeilen_stat(adir, stufe, ilo, ihi)
    geb = {}
    for z in zs:
        for k in range(z['n']):
            if k not in geb:
                geb[k] = dict(index=z['index'], w2=z['w2'], R=z['Rchi'], rho=z['rho'][k])
    return geb, zs


def cmd_neu(adir, refjson, profdir1, profdir2, refprof1, refprof2, aus):
    ref = [d for d in json.load(open(refjson))['stellen'] if d['gezaehlt'] and d['bereich']]
    e = stellen_bereich(adir, *NEU_PAARE)
    gez = [d for d in e['stellen'] if d['gezaehlt']]
    erw = set(range(NEU_PAARE[0], NEU_PAARE[1] + 1))
    fehl = dict(st1=sorted(erw - set(e['st1']['paare'])), st2=sorted(erw - set(e['st2']['paare'])))
    erg = dict(bereich=dict(paare=NEU_PAARE, fehlende_paare=fehl), zeilenvergleich=e['zeilenvergleich'],
               kstat=dict(st1=e['st1']['kstat'], st2=e['st2']['kstat']), n_gepaart=e['n_gepaart'], n_gezaehlt=len(gez),
               nur_st1=e['nur_st1'], nur_st2=e['nur_st2'],
               nicht_gezaehlt=[dict(i=x['i'], k=x['k'], w2=x['w2'], rho=x['rho'], R=x['R'], m1=x['merker_1'],
                                    m2=x['merker_2'], u=[x['umlauf_1'], x['umlauf_2']]) for x in e['stellen']
                               if not x['gezaehlt']],
               stellen=[dict(nr=n + 1, k=d['k'], i=d['i'], w2=d['w2'], rho=d['rho'], R=d['R'], w2_2=d['w2_2'],
                             rho_2=d['rho_2'], R_2=d['R_2'], dw2=d['dw2'], drho=d['drho'], umlauf_1=d['umlauf_1'],
                             umlauf_2=d['umlauf_2'], gap=d['gap'], dw2_zeile=d['dw2_zeile'], klammer_R=d['klammer_R'])
                        for n, d in enumerate(gez)])
    # P1 und Sprossentabelle
    p1 = []
    tab = []
    for k, (rl, vor) in sorted(VORHERSAGE.items()):
        neu = sorted([d for d in gez if d['k'] == k], key=lambda d: d['R'])
        for j, rv in enumerate(vor):
            d = neu[j] if j < len(neu) else None
            z = dict(k=k, sprosse=j + 1, R_vorhergesagt=rv, R_gefunden=(d['R'] if d else None),
                     abweichung=(d['R'] - rv if d else None), w2=(d['w2'] if d else None), rho=(d['rho'] if d else None),
                     umlauf=(d['umlauf_1'] if d else None))
            tab.append(z)
            if j < 2:
                p1.append(dict(z, treffer=bool(d is not None and abs(d['R'] - rv) <= P1_TOL)))
        tab.append(dict(k=k, weitere=[dict(R=d['R'], w2=d['w2']) for d in neu[3:]]))
    p1_aus = 'eingetroffen' if all(z['treffer'] for z in p1) else 'nicht eingetroffen'
    erg['P1'] = dict(je_sprosse=p1, ausgang=p1_aus, n_treffer=sum(1 for z in p1 if z['treffer']),
                     max_abs_abweichung=max([abs(z['abweichung']) for z in p1 if z['abweichung'] is not None] or [-1.0]))
    erg['sprossen_tabelle'] = tab
    # P2: Umlauf wechselt weiter (letzte bekannte Stelle je Kurve plus neue Stellen)
    p2 = []
    for k in sorted(set(d['k'] for d in gez)):
        alt = sorted([d for d in ref if d['k'] == k], key=lambda d: d['R'])
        folge = ([dict(R=alt[-1]['R'], u=alt[-1]['umlauf_1'], quelle='Runde 18 (K0)')] if alt else []) + \
                [dict(R=d['R'], u=d['umlauf_1'], quelle='neu') for d in sorted([d for d in gez if d['k'] == k],
                                                                                 key=lambda d: d['R'])]
        wechsel = [folge[a]['u'] == -folge[a + 1]['u'] for a in range(len(folge) - 1)]
        p2.append(dict(k=k, folge=folge, wechselt=bool(all(wechsel)), n_paare=len(wechsel),
                       n_nicht=sum(1 for w in wechsel if not w)))
    if not gez:
        p2_aus = 'offen'
    else:
        p2_aus = 'eingetroffen' if all(z['wechselt'] for z in p2) else 'nicht eingetroffen'
    erg['P2'] = dict(je_kurve=p2, ausgang=p2_aus, n_folgepaare=sum(z['n_paare'] for z in p2),
                     n_nicht=sum(z['n_nicht'] for z in p2))
    # Geburten und P3
    g1, zs1 = geburten(adir, 1, 0, NEU_PAARE[1] + 1)
    g2, zs2 = geburten(adir, 2, 0, NEU_PAARE[1] + 1)
    erg['geburten'] = dict(st1={str(k): v for k, v in g1.items()}, st2={str(k): v for k, v in g2.items()})
    k10 = sorted([d for d in gez if d['k'] == 10], key=lambda d: d['R'])
    erg['P3'] = dict(erste_stelle_k10=(dict(R=k10[0]['R'], w2=k10[0]['w2'], rho=k10[0]['rho'], umlauf=k10[0]['umlauf_1'])
                                       if k10 else None),
                     fenster=P3_FENSTER, geburt_k10_st1=g1.get(10), geburt_k10_st2=g2.get(10),
                     ausgang=('eingetroffen' if k10 and P3_FENSTER[0] <= k10[0]['R'] <= P3_FENSTER[1]
                              else 'nicht eingetroffen'))
    # P4: kein gemeinsamer Vorzeichenwechsel aller Kurven, Unterzeilen- = Zeilenwechsel je Kurve (beide Stufen)
    p4 = {}
    ok4 = True
    for st in (1, 2):
        L = e['st%d' % st]['p4']
        schlecht = [p for p in L if p['kurven_ungleich'] or p['alle_zugleich']]
        p4['st%d' % st] = dict(paare=len(L), schlecht=schlecht, fein=sum(p['fein'] for p in L),
                               zeile=sum(p['zeile'] for p in L), max_gemeinsam=max([p['max_gemeinsam'] for p in L] or [0]),
                               je_paar=L)
        if schlecht or len(L) != len(erw):
            ok4 = False
    erg['P4'] = dict(p4, ausgang=('eingetroffen' if ok4 else 'nicht eingetroffen'),
                     stufen_gleich=bool(not e['nur_st1'] and not e['nur_st2'] and len(gez) == e['n_gepaart']))
    # Kurvenstatistik im neuen Bereich (Abstaende in R, mit letzter bekannter Stelle)
    kst = []
    for k in sorted(set(d['k'] for d in gez) | set(d['k'] for d in ref)):
        alt = sorted([d['R'] for d in ref if d['k'] == k])
        nn = sorted([d['R'] for d in gez if d['k'] == k])
        R = alt[-1:] + nn
        kst.append(dict(k=k, n_alt=len(alt), n_neu=len(nn), R_neu=nn, dR=np.diff(R).tolist() if len(R) > 1 else [],
                        min_dR_alt=(float(np.min(np.diff(alt))) if len(alt) > 1 else None)))
    erg['kurven'] = kst
    # Hintergrund: Q, E auf zwei Gittern, Vergleich mit Runde 18
    prof = {}
    for st, pd, rp in ((1, profdir1, refprof1), (2, profdir2, refprof2)):
        prof[st] = {round(d['w2'], 10): d for d in json.load(open(os.path.join(pd, 'profile-info.json')))}
        prof['r18_%d' % st] = {round(d['w2'], 10): d for d in json.load(open(rp))}
    liste = sorted(prof[1].keys(), reverse=True)
    hg = []
    for w in liste:
        a, b = prof[1].get(w), prof[2].get(w)
        if a is None or b is None:
            continue
        r1, r2 = prof['r18_1'].get(w), prof['r18_2'].get(w)
        hg.append(dict(w2=w, R1=a['Rchi'], R2=b['Rchi'], dQ=abs(a['Q'] / b['Q'] - 1), dE=abs(a['E'] / b['E'] - 1),
                       dR12=a['Rchi'] - b['Rchi'], it1=a['newton_it'], it2=b['newton_it'], N1=a['N'], N2=b['N'],
                       chi0=a['chi0'], f_rand=max(a['f_rand'], b['f_rand']),
                       gleich_r18_st1=bool(r1 is not None and r1['Q'] == a['Q'] and r1['E'] == a['E']),
                       gleich_r18_st2=bool(r2 is not None and r2['Q'] == b['Q'] and r2['E'] == b['E']),
                       R_formel=1.3736 / (w - 0.7281) + 0.55))
    neu_hg = [h for h in hg if h['R1'] >= 38.9]
    erg['hintergrund'] = dict(n=len(hg), max_dQ=max(h['dQ'] for h in hg), max_dE=max(h['dE'] for h in hg),
                              max_dQ_neu=max([h['dQ'] for h in neu_hg] or [None]),
                              max_dE_neu=max([h['dE'] for h in neu_hg] or [None]),
                              sauber=bool(all(h['dQ'] <= 1e-6 and h['dE'] <= 1e-6 for h in hg)),
                              n_gleich_r18=sum(1 for h in hg if h['gleich_r18_st1'] and h['gleich_r18_st2']),
                              max_f_rand=max(h['f_rand'] for h in hg), zeilen_neu=neu_hg)
    # Abbildung R <-> omega^2 (Stufe 1), vorhergesagte R auf omega^2 (linear in der Zeilentabelle)
    Rt = np.array([h['R1'] for h in hg])
    Wt = np.array([h['w2'] for h in hg])
    o = np.argsort(Rt)
    abb = []
    for k, (rl, vor) in sorted(VORHERSAGE.items()):
        for rv in vor:
            abb.append(dict(k=k, R=rv, w2=float(np.interp(rv, Rt[o], Wt[o]))))
    erg['abbildung'] = dict(vorhersage_w2=abb, regel='R = Radius der chi = 1/2-Kreuzung (r_chi, Runde 18)')
    # Stichprobe Rechteck-Umlauf (PLAN 5): die acht P1-Stellen, dann erste Stelle je Kurve k >= 10,
    # dann groesstes R je Kurve k = 4..9
    probe = []
    namen = set()
    def dazu(d, name):
        if d is None or name in namen:
            return
        namen.add(name)
        probe.append((name, d))
    for k in range(4):
        nn = sorted([d for d in gez if d['k'] == k], key=lambda d: d['R'])
        for j in range(min(2, len(nn))):
            dazu(nn[j], 'P-k%d-s%d' % (k, j + 1))
    for k in sorted(set(d['k'] for d in gez if d['k'] >= 10)):
        nn = sorted([d for d in gez if d['k'] == k], key=lambda d: d['R'])
        dazu(nn[0], 'P-k%d-s1' % k)
    for k in range(4, 10):
        nn = sorted([d for d in gez if d['k'] == k], key=lambda d: d['R'])
        if nn:
            dazu(nn[-1], 'P-k%d-max' % k)
    for st in (1, 2):
        pkt = []
        for name, d in probe:
            pkt.append(dict(name=name, w2=d['w2'] if st == 1 else d['w2_2'], rho=d['rho'] if st == 1 else d['rho_2'],
                            gap=d['gap'], dw2_zeile=d['dw2_zeile'], k=d['k'], R=d['R'], umlauf_zelle=d['umlauf_%d' % st]))
        schreibe(os.path.join(os.path.dirname(aus), 'umlauf-punkte-st%d.json' % st), dict(punkte=pkt))
    erg['stichprobe_liste'] = [n for n, d in probe]
    schreibe(aus, erg)
    print(json.dumps({k: erg[k] for k in ('bereich', 'n_gepaart', 'n_gezaehlt', 'P1', 'P2', 'P3')}, indent=1)[:6000])
    print(json.dumps(dict(P4=erg['P4']['ausgang'], stufen_gleich=erg['P4']['stufen_gleich'],
                          schlecht1=erg['P4']['st1']['schlecht'], schlecht2=erg['P4']['st2']['schlecht']), indent=1))
    print(json.dumps({k: v for k, v in erg['hintergrund'].items() if k != 'zeilen_neu'}, indent=1))


def cmd_umlaufabgleich(adir, aus):
    pr = {}
    for st in (1, 2):
        for fn in sorted(os.listdir(adir)):
            if fn.startswith('umlauf-st%d-' % st) and fn.endswith('.json'):
                for e in json.load(open(os.path.join(adir, fn)))['punkte']:
                    um = e.get('umlauf') or {}
                    pr.setdefault(e['start']['name'], {})['st%d' % st] = dict(
                        w2=e['w2'], rho=e['rho'], konv=e['konvergiert'], start_w2=e['start']['w2'],
                        start_rho=e['start']['rho'], dw2_start=e['w2'] - e['start']['w2'],
                        drho_start=e['rho'] - e['start']['rho'], umlauf=um.get('umlauf'), aufgeloest=um.get('aufgeloest'),
                        sprung=um.get('groesster_sprung'), punkte=um.get('punkte'), svr=e.get('svr'),
                        umlauf_zelle=e['start'].get('umlauf_zelle'), hmax=e.get('hmax'), Rchi=e.get('Rchi'),
                        k=e['start'].get('k'), R=e['start'].get('R'), kopplung=e.get('kopplung'),
                        gleich=bool(um.get('aufgeloest') and um.get('umlauf') == e['start'].get('umlauf_zelle')))
    n = sum(1 for v in pr.values() for st in v.values() if st['gleich'])
    m = sum(1 for v in pr.values() for st in v.values())
    erg = dict(je_stelle=pr, n_gleich=n, n_proben=m, n_stellen=len(pr),
               n_stellen_beide_gleich=sum(1 for v in pr.values() if all(st['gleich'] for st in v.values()) and len(v) == 2))
    schreibe(aus, erg)
    print(json.dumps(erg, indent=1))


def main():
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == 'k0':
        cmd_k0(a[0], a[1], a[2], a[3])
    elif c == 'neu':
        cmd_neu(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
    elif c == 'umlaufabgleich':
        cmd_umlaufabgleich(a[0], a[1])
    else:
        raise SystemExit('unbekannt: ' + c)


if __name__ == '__main__':
    main()
