#!/usr/bin/env python3
"""auswertung_quadrupol.py - Runde 20 HUELLEN-QUADRUPOL: Stellen, Abgleich der Stufen, Kurven, Abstaende, Versatz,
Q0 bis Q3. Regeln: PLAN.md (eingefroren), Abschnitte 2 und 4 bis 8. Abgeleitet aus auswertung_dipol.py (Runde 19);
Hilfsfunktionen aus auswertung.py (Runde 18, unveraendert)."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import math
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import auswertung as A18     # Runde 18, unveraendert (lade, punkte_stufe, zeilen_stat, ...)

schreibe = A18.schreibe


def kurven_aus_stellen(pf):
    """Gezaehlte Stellen im gewerteten Bereich eines Vorlaeufers: {k: [R aufsteigend]} (R Stufe 1)."""
    d = json.load(open(pf))
    out = {}
    for s in d['stellen']:
        if s['gezaehlt'] and s.get('bereich'):
            out.setdefault(int(s['k']), []).append(float(s['R']))
    return {k: sorted(v) for k, v in out.items()}


def versatz(R, R0):
    """PLAN 6: v = (R - R0_unten) / (R0_oben - R0_unten), modulo 1; R0_unten = groesste l = 0-Lage <= R derselben
    Kurve, R0_oben die naechste. Unter der ersten (ueber der letzten) l = 0-Lage: erster (letzter) Abstand."""
    if R0 is None or len(R0) < 2:
        return None
    j0 = max([j for j in range(len(R0)) if R0[j] <= R], default=-1)
    j = min(max(j0, 0), len(R0) - 2)
    vr = (R - R0[j]) / (R0[j + 1] - R0[j])
    return dict(v=float(vr - math.floor(vr)), v_roh=float(vr), R0_unten=R0[j], R0_oben=R0[j + 1],
                abstand=R0[j + 1] - R0[j], j0=j0, rand=bool(j0 != j))


def kreismittel(vs):
    if not vs:
        return None
    z = np.mean(np.exp(2j * np.pi * np.array(vs)))
    m = float(np.angle(z) / (2 * np.pi))
    return dict(mittel=m - math.floor(m), laenge=float(abs(z)), arith=float(np.mean(vs)), n=len(vs),
                v_min=float(min(vs)), v_max=float(max(vs)))


def l0_vergleich(R0, Rmin, Rmax):
    """Wie HUELLEN-DIPOL (D3): l = 0-Abstaende mit Paarmitte in [Rmin, Rmax], sonst naechste Paarmitte."""
    if R0 is None or len(R0) < 2:
        return None
    mid = [0.5 * (R0[i] + R0[i + 1]) for i in range(len(R0) - 1)]
    dR = [R0[i + 1] - R0[i] for i in range(len(R0) - 1)]
    sel = [d for m, d in zip(mid, dR) if Rmin <= m <= Rmax]
    if sel:
        return dict(mittel=float(np.mean(sel)), n=len(sel), art='Paarmitten im Bereich', werte=sel)
    ab = [max(Rmin - m, 0.0, m - Rmax) for m in mid]
    j = int(np.argmin(ab))
    return dict(mittel=float(dR[j]), n=1, art='naechste Paarmitte', mitte=float(mid[j]), werte=[dR[j]])


def kurven_tabelle(K, K0):
    """Je Kurve: Lagen, Abstaende, Mittel, CV, q gegen l = 0 (gleicher Rang), Versatz je Stelle."""
    out = []
    for k in sorted(K):
        R = sorted(K[k])
        dR = np.diff(R)
        e = dict(k=k, n=len(R), R=R, dR=dR.tolist())
        if len(dR) >= 1:
            e['dR_mittel'] = float(dR.mean())
        if len(dR) >= 2:
            e['cv_dR'] = float(dR.std(ddof=1) / dR.mean())
        if len(R) >= 2 and K0 is not None:
            ref = l0_vergleich(K0.get(k), min(R), max(R))
            if ref is not None:
                e['l0_ref'] = ref
                e['q'] = e['dR_mittel'] / ref['mittel']
        if K0 is not None:
            e['versatz'] = [versatz(x, K0.get(k)) for x in R]
        out.append(e)
    return out


def cmd_stellen(adir, zeilenjson, l0json, l1json, aus):
    liste = json.load(open(zeilenjson))['w2']
    K0 = kurven_aus_stellen(l0json)
    K1 = kurven_aus_stellen(l1json)
    erg = dict(n_zeilen_liste=len(liste))
    P = {}
    for st in (1, 2):
        paare, pk, kstat = A18.punkte_stufe(adir, st)
        zs = A18.zeilen_stat(adir, st)
        abn = [dict(i=a['index'], w2=a['w2'], n_vor=a['n'], n_nach=b['n']) for a, b in zip(zs[:-1], zs[1:])
               if b['n'] < a['n']]
        P[st] = pk
        erg['st%d' % st] = dict(n_paare=len(paare), n_zeilen=len(zs), n_punkte=len(pk), kstat=kstat, abnahmen=abn,
                                w2_min_paar=min((d['w2b'] for d in paare), default=None),
                                unsicher_nullstellen=sum(z['unsicher'] for z in zs),
                                illinois_nullstellen=sum(1 for z in A18.lade(adir, 'z', st) for q in z['null']
                                                         if q.get('illinois', 0) > 0))
    # Zeilenvergleich der Stufen
    z1 = {z['index']: z for z in A18.zeilen_stat(adir, 1)}
    z2 = {z['index']: z for z in A18.zeilen_stat(adir, 2)}
    gleich_n, gleich_vz, diff_rho = 0, 0, 0.0
    ungleich = []
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
    erg['zeilenvergleich'] = dict(zeilen_beide=len(set(z1) & set(z2)), gleiche_zahl=gleich_n,
                                  gleiche_vorzeichen=gleich_vz, max_drho=diff_rho, abweichungen=ungleich[:40],
                                  n_abweichungen=len(ungleich))
    # Geburt der Kurven (Stufe 1): erste Zeile mit k + 1 Nullstellen
    geb = []
    zl = [z1[i] for i in sorted(z1)]
    kmax = max((z['n'] for z in zl), default=0)
    for k in range(kmax):
        z = next((z for z in zl if z['n'] >= k + 1), None)
        if z:
            geb.append(dict(k=k, index=z['index'], w2=z['w2'], R=z['Rchi'], rho=z['rho'][k]))
    erg['geburt'] = geb
    erg['zeilen_ohne_nullstelle_st1'] = [dict(i=z['index'], w2=z['w2'], R=z['Rchi']) for z in zl if z['n'] == 0]
    erg['knoten_letzte_zeile_st1'] = (zl[-1]['kn'] if zl else None)
    erg['letzte_zeile_st1'] = (dict(index=zl[-1]['index'], w2=zl[-1]['w2'], R=zl[-1]['Rchi'], rho=zl[-1]['rho'])
                               if zl else None)
    # Abgleich der Stufen je Zeilenpaar und Kurve (wie Runde 18 / 19)
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
        ok = ((not q['merker']) and (not r['merker']) and q['umlauf_zelle'] == r['umlauf_zelle']
              and abs(q['umlauf_zelle']) == 1)
        stellen.append(dict(k=q['k'], i=q['i'], w2=q['w2'], rho=q['rho'], R=q['R'], w2_2=r['w2'], rho_2=r['rho'],
                            R_2=r['R'], dw2=r['w2'] - q['w2'], drho=r['rho'] - q['rho'], dR=r['R'] - q['R'],
                            umlauf_1=q['umlauf_zelle'], umlauf_2=r['umlauf_zelle'], kn_1=q['kn'], kn_2=r['kn'],
                            merker_1=q['merker'], merker_2=r['merker'], gezaehlt=bool(ok), gap=q['gap'],
                            gap_2=r['gap'], dw2_zeile=q['dw2_zeile'], klammer_w2=q['w2_klammer'],
                            klammer_R=q['R_klammer']))
    for key, lst in by2.items():
        for j, r in enumerate(lst):
            if (key[0], key[1], j) not in benutzt:
                nur2.append(r)
    stellen.sort(key=lambda d: -d['w2'])
    # Bereich (PLAN 5): zusammenhaengend ab 1,40 auf beiden Stufen
    S1 = set(d['i'] for d in A18.punkte_stufe_paare(adir, 1))
    S2 = set(d['i'] for d in A18.punkte_stufe_paare(adir, 2))
    j_cont = 0
    while j_cont in S1 and j_cont in S2:
        j_cont += 1
    n_paare_ges = len(liste) - 1
    erg['bereich'] = dict(j_cont=j_cont, n_paare_gesamt=n_paare_ges, w2_unten=(liste[j_cont] if j_cont > 0 else None),
                          bis_080=bool(j_cont >= n_paare_ges), paare_st1=len(S1), paare_st2=len(S2))
    for n, d in enumerate(stellen):
        d['nr'] = n + 1
        d['bereich'] = bool(d['i'] < j_cont)
    gez = [d for d in stellen if d['gezaehlt'] and d['bereich']]
    erg['n_stellen_gepaart'] = len(stellen)
    erg['n_gezaehlt'] = len(gez)
    nb1 = [q for q in nur1 if q['i'] < j_cont]
    nb2 = [r for r in nur2 if r['i'] < j_cont]
    erg['nur_eine_stufe_im_bereich'] = dict(
        n_st1=len(nb1), n_st2=len(nb2),
        st1=[dict(i=q['i'], k=q['k'], w2=q['w2'], rho=q['rho'], umlauf=q['umlauf_zelle'], merker=q['merker']) for q in nb1],
        st2=[dict(i=r['i'], k=r['k'], w2=r['w2'], rho=r['rho'], umlauf=r['umlauf_zelle'], merker=r['merker']) for r in nb2])
    erg['gepaart_nicht_gezaehlt_im_bereich'] = [
        dict(nr=d['nr'], k=d['k'], w2=d['w2'], rho=d['rho'], u1=d['umlauf_1'], u2=d['umlauf_2'], m1=d['merker_1'],
             m2=d['merker_2']) for d in stellen if d['bereich'] and not d['gezaehlt']]
    erg['lage_beider_stufen'] = dict(
        max_dw2=float(max((abs(d['dw2']) for d in gez), default=0.0)),
        max_drho=float(max((abs(d['drho']) for d in gez), default=0.0)),
        max_dR=float(max((abs(d['dR']) for d in gez), default=0.0)))
    # Kurven l = 2 (gezaehlte Stellen), mit Umlauf und Nummern
    K2 = {}
    for d in gez:
        K2.setdefault(int(d['k']), []).append(float(d['R']))
    t2 = kurven_tabelle(K2, K0)
    for e in t2:
        L = sorted([d for d in gez if d['k'] == e['k']], key=lambda d: d['R'])
        e['nr'] = [d['nr'] for d in L]
        e['w2'] = [d['w2'] for d in L]
        e['rho'] = [d['rho'] for d in L]
        e['umlauf'] = [d['umlauf_1'] for d in L]
        e['umlauf_wechselt'] = bool(all(L[i]['umlauf_1'] == -L[i + 1]['umlauf_1'] for i in range(len(L) - 1)))
    erg['kurven_l2'] = t2
    erg['kurven_l1'] = kurven_tabelle(K1, K0)
    erg['kurven_l0'] = kurven_tabelle(K0, K0)
    # Q1
    nf = sum(1 for d in gez if 0.80 - 1e-12 <= d['w2'] <= 1.40 + 1e-12)
    if nf >= 5:
        q1 = 'eingetroffen'
    elif erg['bereich']['bis_080']:
        q1 = 'nicht eingetroffen'
    else:
        q1 = 'offen'
    erg['Q1'] = dict(n=nf, ausgang=q1)
    # Q2: Kurven mit >= 4 Stellen: CV < 0,10 und |q - 1| <= 0,05
    q2k = []
    for e in t2:
        if e['n'] >= 4:
            ok_cv = bool(e['cv_dR'] < 0.10)
            ok_q = bool(e.get('q') is not None and abs(e['q'] - 1.0) <= 0.05)
            q2k.append(dict(k=e['k'], n=e['n'], dR_mittel=e['dR_mittel'], cv=e['cv_dR'], q=e.get('q'),
                            l0_mittel=(e.get('l0_ref') or {}).get('mittel'), ok_cv=ok_cv, ok_q=ok_q))
    if not q2k:
        q2 = 'offen'
    else:
        q2 = 'eingetroffen' if all(x['ok_cv'] and x['ok_q'] for x in q2k) else 'nicht eingetroffen'
    erg['Q2'] = dict(kurven=q2k, ausgang=q2)
    # Q3: Kreismittel des Versatzes ueber alle gezaehlten l = 2-Stellen mit Versatz
    vs = [v['v'] for e in t2 for v in e['versatz'] if v is not None]
    km = kreismittel(vs)
    if km is None:
        q3 = 'offen'
    else:
        q3 = 'eingetroffen' if (0.6 <= km['mittel'] < 1.0 or km['mittel'] == 0.0) else 'nicht eingetroffen'
    erg['Q3'] = dict(kreismittel=km, ausgang=q3,
                     je_kurve=[dict(k=e['k'], km=kreismittel([v['v'] for v in e['versatz'] if v is not None]))
                               for e in t2])
    v1 = [v['v'] for e in erg['kurven_l1'] for v in e['versatz'] if v is not None]
    erg['versatz_l1'] = dict(kreismittel=kreismittel(v1),
                             je_kurve=[dict(k=e['k'], km=kreismittel([v['v'] for v in e['versatz'] if v is not None]))
                                       for e in erg['kurven_l1']])
    # Rechteck-Umlauf an allen Funden (Karte): je Stufe alle Punkte im Bereich
    for st in (1, 2):
        pk = []
        for d in stellen:
            if not d['bereich']:
                continue
            pk.append(dict(name='S-nr%d-k%d' % (d['nr'], d['k']), w2=(d['w2'] if st == 1 else d['w2_2']),
                           rho=(d['rho'] if st == 1 else d['rho_2']), gap=(d['gap'] if st == 1 else d['gap_2']),
                           dw2_zeile=d['dw2_zeile'], k=d['k'], umlauf_zelle=d['umlauf_%d' % st], nr=d['nr']))
        for q in (nb1 if st == 1 else nb2):
            pk.append(dict(name='U%d-i%d-k%d-%.8f' % (st, q['i'], q['k'], q['w2']), w2=q['w2'], rho=q['rho'],
                           gap=q['gap'], dw2_zeile=q['dw2_zeile'], k=q['k'], umlauf_zelle=q['umlauf_zelle'], nr=None))
        schreibe(os.path.join(os.path.dirname(aus), 'umlauf-punkte-alle-st%d.json' % st), dict(punkte=pk))
    schreibe(aus, erg)
    schreibe(os.path.join(os.path.dirname(aus), 'stellen.json'), dict(stellen=stellen, nur_st1=nur1, nur_st2=nur2))
    print(json.dumps({k: erg[k] for k in ('st1', 'st2', 'zeilenvergleich', 'bereich', 'n_stellen_gepaart',
                                          'n_gezaehlt', 'nur_eine_stufe_im_bereich', 'lage_beider_stufen',
                                          'geburt', 'Q1', 'Q2', 'Q3', 'versatz_l1')}, indent=1))
    for e in t2:
        print('l=2 k=%d n=%d R=%s dR=%s cv=%s q=%s v=%s umlauf=%s' % (
            e['k'], e['n'], [round(x, 3) for x in e['R']], [round(x, 3) for x in e['dR']], e.get('cv_dR'), e.get('q'),
            [None if v is None else round(v['v'], 4) for v in e['versatz']], e['umlauf']))


def umlauf_lesen(adir, praefix):
    out = {}
    for st in (1, 2):
        pf = os.path.join(adir, '%s-st%d.json' % (praefix, st))
        if not os.path.exists(pf):
            continue
        for e in json.load(open(pf))['punkte']:
            um = e.get('umlauf') or {}
            out.setdefault(e['name'], {})['st%d' % st] = dict(
                w2=e['w2'], rho=e['rho'], konv=e['konvergiert'], bereich=e.get('bereich'), start_w2=e['start']['w2'],
                start_rho=e['start']['rho'], d_w2=e['w2'] - e['start']['w2'], d_rho=e['rho'] - e['start']['rho'],
                umlauf=um.get('umlauf'), aufgeloest=um.get('aufgeloest'), sprung=um.get('groesster_sprung'),
                punkte=um.get('punkte'), versuch=um.get('versuch'), svr=e.get('svr'),
                umlauf_zelle=e['start'].get('umlauf_zelle'), hmax=e.get('hmax'), Rchi=e.get('Rchi'),
                gleich=bool(um.get('aufgeloest') and um.get('umlauf') == e['start'].get('umlauf_zelle')))
    return out


def cmd_final(adir, aus):
    erg = json.load(open(os.path.join(adir, 'auswertung.json')))
    k1 = {}
    for ell in (0, 1):
        for st in (1, 2):
            pf = os.path.join(adir, 'k1-l%d-st%d.json' % (ell, st))
            k1['l%d-st%d' % (ell, st)] = json.load(open(pf)) if os.path.exists(pf) else None
    vorh = [v for v in k1.values() if v is not None]
    q0 = 'eingetroffen' if (len(vorh) == 4 and all(v.get('bestanden') for v in vorh)) else 'nicht eingetroffen'
    erg['K1'] = k1
    erg['Q0'] = dict(ausgang=q0, je_lauf={k: (v.get('bestanden') if v else None) for k, v in k1.items()})
    pf = os.path.join(adir, 'probe-l2-st1.json')
    erg['probe_l2'] = json.load(open(pf)) if os.path.exists(pf) else None
    erg['rechteck_alle'] = umlauf_lesen(adir, 'umlauf-alle')
    ra = erg['rechteck_alle']
    erg['rechteck_zusammen'] = dict(
        n_namen=len(ra),
        n_beide_stufen=sum(1 for v in ra.values() if 'st1' in v and 'st2' in v),
        n_gleich_beide=sum(1 for v in ra.values() if v.get('st1', {}).get('gleich') and v.get('st2', {}).get('gleich')),
        ungleich=[n for n, v in ra.items() if not all(v.get(s, {}).get('gleich') for s in ('st1', 'st2'))])
    schreibe(aus, erg)
    print(json.dumps({k: erg[k] for k in ('Q0', 'Q1', 'Q2', 'Q3', 'rechteck_zusammen')}, indent=1))


def main():
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == 'stellen':
        cmd_stellen(a[0], a[1], a[2], a[3], a[4])
    elif c == 'final':
        cmd_final(a[0], a[1])
    else:
        raise SystemExit('unbekannt: ' + c)


if __name__ == '__main__':
    main()
