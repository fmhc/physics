#!/usr/bin/env python3
"""auswertung_dipol.py - Runde 19 HUELLEN-DIPOL: Stellen, Abgleich der Stufen, Kurven, D0 bis D4, Stichprobe.
Regeln: PLAN.md (eingefroren), Abschnitte 2 und 4 bis 9. Hilfsfunktionen aus auswertung.py (Runde 18, unveraendert)."""
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
K1_REF = (0.75449601378264, 1.82634203018107)


def l0_vergleich(l0, k, Rmin, Rmax):
    R = l0.get(str(k))
    if not R or len(R) < 2:
        return None
    mid = [0.5 * (R[i] + R[i + 1]) for i in range(len(R) - 1)]
    dR = [R[i + 1] - R[i] for i in range(len(R) - 1)]
    sel = [d for m, d in zip(mid, dR) if Rmin <= m <= Rmax]
    if sel:
        return dict(mittel=float(np.mean(sel)), n=len(sel), art='Paarmitten im Bereich')
    ab = [max(Rmin - m, 0.0, m - Rmax) for m in mid]
    j = int(np.argmin(ab))
    return dict(mittel=float(dR[j]), n=1, art='naechste Paarmitte', mitte=float(mid[j]))


def cmd_stellen(adir, zeilenjson, l0json, aus):
    liste = json.load(open(zeilenjson))['w2']
    l0 = json.load(open(l0json))
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
                                illinois_zeilen=0)
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
    erg['knoten_letzte_zeile_st1'] = (zl[-1]['kn'] if zl else None)
    erg['letzte_zeile_st1'] = (dict(index=zl[-1]['index'], w2=zl[-1]['w2'], R=zl[-1]['Rchi'], rho=zl[-1]['rho'])
                               if zl else None)
    # Abgleich der Stufen je Zeilenpaar und Kurve (wie Runde 18)
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
                            dw2_zeile=q['dw2_zeile'], klammer_w2=q['w2_klammer'], klammer_R=q['R_klammer']))
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
    # Kurven
    kurven = {}
    for d in gez:
        kurven.setdefault(d['k'], []).append(d)
    kst = []
    for k in sorted(kurven):
        L = sorted(kurven[k], key=lambda d: -d['w2'])
        w2 = np.array([d['w2'] for d in L])
        R = np.array([d['R'] for d in L])
        dw = -np.diff(w2)
        dR = np.diff(R)
        e = dict(k=k, n=len(L), w2=w2.tolist(), R=R.tolist(), rho=[d['rho'] for d in L], umlauf=[d['umlauf_1'] for d in L],
                 nr=[d['nr'] for d in L], kn=[d['kn_1'] for d in L], dw2=dw.tolist(), dR=dR.tolist(),
                 w2_max=float(w2.max()), w2_min=float(w2.min()))
        if len(dR) >= 1:
            e['dR_mittel'] = float(dR.mean())
            e['dR_min'] = float(dR.min())
            e['dR_max'] = float(dR.max())
        if len(dR) >= 2:
            e['dR_std'] = float(dR.std(ddof=1))
            e['cv_dR'] = float(dR.std(ddof=1) / dR.mean())
        if len(dw) >= 4:
            e['spearman_dw2_w2'] = A18.spearman(dw, 0.5 * (w2[:-1] + w2[1:]))
        e['umlauf_wechselt'] = bool(all(L[i]['umlauf_1'] == -L[i + 1]['umlauf_1'] for i in range(len(L) - 1)))
        kst.append(e)
    erg['kurven'] = kst
    # D1
    nf = sum(1 for d in gez if 0.80 - 1e-12 <= d['w2'] <= 1.40 + 1e-12)
    if nf >= 5:
        d1 = 'eingetroffen'
    elif erg['bereich']['bis_080']:
        d1 = 'nicht eingetroffen'
    else:
        d1 = 'offen'
    erg['D1'] = dict(n=nf, ausgang=d1)
    # D2
    d2k = [dict(k=e['k'], n=e['n'], cv=e['cv_dR'], dR_mittel=e['dR_mittel']) for e in kst if e['n'] >= 4]
    if not d2k:
        d2 = 'offen'
    else:
        d2 = 'eingetroffen' if all(x['cv'] < 0.15 for x in d2k) else 'nicht eingetroffen'
    erg['D2'] = dict(kurven=d2k, ausgang=d2)
    # D3
    d3k = []
    for e in kst:
        if e['n'] >= 3:
            Rmin, Rmax = min(e['R']), max(e['R'])
            ref = l0_vergleich(l0, e['k'], Rmin, Rmax)
            if ref is None:
                d3k.append(dict(k=e['k'], n=e['n'], dR1=e['dR_mittel'], ref=None, q=None, ok=None))
                continue
            qk = e['dR_mittel'] / ref['mittel']
            d3k.append(dict(k=e['k'], n=e['n'], R_bereich=[Rmin, Rmax], dR1=e['dR_mittel'], ref=ref, q=qk,
                            ok=bool(abs(qk - 1.0) <= 0.15)))
    wert = [x for x in d3k if x['q'] is not None]
    if not wert:
        d3 = 'offen'
    else:
        d3 = 'eingetroffen' if all(x['ok'] for x in wert) else 'nicht eingetroffen'
    erg['D3'] = dict(kurven=d3k, ausgang=d3)
    # Stichprobe (PLAN 7) und Restliste
    for st in (1, 2):
        probe, rest = [], []
        ks = sorted(set(d['k'] for d in gez))
        reihe = [k for k in (0, 1, 2, 3) if k in ks] + [k for k in ks if k >= 4 and k % 4 == 0]
        gew = set()
        for k in reihe:
            dk = [d for d in gez if d['k'] == k]
            d = min(dk, key=lambda d: d['w2'])
            gew.add(d['nr'])
            probe.append(dict(name='P-k%d-nr%d' % (k, d['nr']), w2=(d['w2'] if st == 1 else d['w2_2']),
                              rho=(d['rho'] if st == 1 else d['rho_2']), gap=d['gap'], dw2_zeile=d['dw2_zeile'], k=k,
                              umlauf_zelle=d['umlauf_%d' % st], nr=d['nr']))
        for d in sorted(gez, key=lambda d: (d['k'], d['w2'])):
            if d['nr'] in gew:
                continue
            rest.append(dict(name='A-k%d-nr%d' % (d['k'], d['nr']), w2=(d['w2'] if st == 1 else d['w2_2']),
                             rho=(d['rho'] if st == 1 else d['rho_2']), gap=d['gap'], dw2_zeile=d['dw2_zeile'],
                             k=d['k'], umlauf_zelle=d['umlauf_%d' % st], nr=d['nr']))
        schreibe(os.path.join(os.path.dirname(aus), 'umlauf-punkte-P-st%d.json' % st), dict(punkte=probe))
        schreibe(os.path.join(os.path.dirname(aus), 'umlauf-punkte-A-st%d.json' % st), dict(punkte=rest))
    schreibe(aus, erg)
    schreibe(os.path.join(os.path.dirname(aus), 'stellen.json'), dict(stellen=stellen, nur_st1=nur1, nur_st2=nur2))
    print(json.dumps({k: erg[k] for k in ('st1', 'st2', 'zeilenvergleich', 'bereich', 'n_stellen_gepaart',
                                          'n_gezaehlt', 'nur_eine_stufe_im_bereich', 'lage_beider_stufen',
                                          'geburt', 'D1', 'D2', 'D3')}, indent=1))
    for e in kst:
        print('k=%d n=%d R=%s dR=%s cv=%s kn=%s umlauf=%s' % (e['k'], e['n'], [round(x, 2) for x in e['R']],
                                                          [round(x, 3) for x in e['dR']], e.get('cv_dR'), e['kn'],
                                                          e['umlauf']))


def umlauf_lesen(adir, praefix):
    out = {}
    for st in (1, 2):
        for fn in sorted(os.listdir(adir)):
            if fn.startswith('%s-st%d' % (praefix, st)) and fn.endswith('.json'):
                for e in json.load(open(os.path.join(adir, fn)))['punkte']:
                    um = e.get('umlauf') or {}
                    out.setdefault(e['name'], {})['st%d' % st] = dict(
                        w2=e['w2'], rho=e['rho'], konv=e['konvergiert'], start_w2=e['start']['w2'],
                        start_rho=e['start']['rho'], d_w2=e['w2'] - e['start']['w2'], d_rho=e['rho'] - e['start']['rho'],
                        umlauf=um.get('umlauf'), aufgeloest=um.get('aufgeloest'), sprung=um.get('groesster_sprung'),
                        punkte=um.get('punkte'), versuch=um.get('versuch'), svr=e.get('svr'),
                        umlauf_zelle=e['start'].get('umlauf_zelle'), hmax=e.get('hmax'), Rchi=e.get('Rchi'),
                        gleich=bool(um.get('aufgeloest') and um.get('umlauf') == e['start'].get('umlauf_zelle')))
    return out


def cmd_final(adir, aus):
    erg = json.load(open(os.path.join(adir, 'auswertung.json')))
    # K1 / D0
    k1 = {}
    for st in (1, 2):
        pf = os.path.join(adir, 'k1-st%d.json' % st)
        if not os.path.exists(pf):
            continue
        d = json.load(open(pf))
        ks = []
        for e in d.get('kandidaten', []):
            um = e.get('umlauf') or {}
            ks.append(dict(w2=e['w2'], rho=e['rho'], konv=e['konvergiert'], svr=e.get('svr'),
                           d_ref=e['abstand_referenz'], d_karte=e['abstand_karte'], umlauf=um.get('umlauf'),
                           aufgeloest=um.get('aufgeloest'), sprung=um.get('groesster_sprung'), punkte=um.get('punkte'),
                           zelle=e.get('zelle')))
        k1['st%d' % st] = dict(kandidaten=ks, selbsttest=d.get('selbsttest_l0'),
                               zeilen=[dict(w2=z['w2'], vz=z['vorzeichen'], rho=[q['rho'] for q in z['null']],
                                            s=[q['s'] for q in z['null']]) for z in d.get('zeilen', [])])
    ok = []
    for st in (1, 2):
        ks = k1.get('st%d' % st, {}).get('kandidaten', [])
        tr = [x for x in ks if x['konv'] and abs(x['d_ref'][0]) <= 1e-6 and abs(x['d_ref'][1]) <= 1e-6
              and x['aufgeloest'] and abs(x['umlauf'] or 0) == 1]
        ok.append(tr[0]['umlauf'] if tr else None)
    d0 = 'eingetroffen' if (ok[0] is not None and ok[0] == ok[1]) else 'nicht eingetroffen'
    erg['K1'] = k1
    erg['D0'] = dict(umlauf_st1=ok[0], umlauf_st2=ok[1], ausgang=d0)
    erg['stichprobe'] = umlauf_lesen(adir, 'umlauf-P')
    erg['weitere_rechtecke'] = umlauf_lesen(adir, 'umlauf-A')
    # D4
    pf = os.path.join(adir, 'd4-st1.json')
    if os.path.exists(pf):
        d4 = json.load(open(pf))
        sch = d4.get('schritte', [])
        last = sch[-1] if sch else None
        if last is None or last['lam'] < 1.0 - 1e-9:
            a4 = 'offen'
        else:
            a4 = 'nicht eingetroffen' if (last.get('art') == 'E1' and last.get('lebt')) else 'eingetroffen'
        erg['D4'] = dict(ausgang=a4, n_schritte=len(sch), abbruch=d4.get('abbruch'),
                         schritte=[{k: s.get(k) for k in ('lam', 'art', 'bereich_start', 'bereich_ende', 'w2', 'rho', 'T',
                                                          'svr', 'lebt', 'Rchi', 'rhalf', 'chi0', 'e1_versuch',
                                                          'sekunden')} for s in sch])
    else:
        erg['D4'] = dict(ausgang='offen', grund='nicht gerechnet')
    schreibe(aus, erg)
    print(json.dumps({k: erg[k] for k in ('D0', 'D1', 'D2', 'D3', 'D4')}, indent=1))
    print(json.dumps(erg['stichprobe'], indent=1))
    print(json.dumps(erg['K1'], indent=1))


def cmd_bild(adir, aus1, aus2):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    st = json.load(open(os.path.join(adir, 'stellen.json')))['stellen']
    gez = [d for d in st if d['gezaehlt'] and d.get('bereich')]
    zs = sorted(A18.lade(adir, 'z', 2), key=lambda d: d['index'])
    cmap = plt.get_cmap('tab10')
    fig, ax = plt.subplots(1, 1, figsize=(11, 7))
    for z in zs:
        for k, q in enumerate(z['null']):
            ax.plot(z['w2'], q['rho'], '.', ms=1.5, color=cmap(k % 10))
    for d in gez:
        ax.plot(d['w2'], d['rho'], '^' if d['umlauf_1'] > 0 else 'v', ms=6, mfc='none', mec='k', mew=0.8)
    ax.set_xlabel('omega^2')
    ax.set_ylabel('rho')
    ax.set_title('l = 1: Nullstellen von m_bc (Farbe = Kurve k), Stellen (Dreieck auf: Umlauf +1, ab: -1)')
    fig.tight_layout()
    fig.savefig(aus1, dpi=120)
    l0 = json.load(open(os.path.join(adir, 'l0-kurven.json')))
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    for k in sorted(set(d['k'] for d in gez)):
        L = sorted([d for d in gez if d['k'] == k], key=lambda d: -d['w2'])
        if len(L) < 2:
            continue
        R = np.array([d['R'] for d in L])
        ax.plot(0.5 * (R[1:] + R[:-1]), np.diff(R), 'o-', ms=4, color=cmap(k % 10), label='l=1, k=%d' % k)
    for k in range(4):
        R = np.array(l0[str(k)])
        R = R[R <= 22]
        ax.plot(0.5 * (R[1:] + R[:-1]), np.diff(R), 'x--', ms=4, lw=0.7, color=cmap(k % 10), label='l=0, k=%d' % k)
    ax.set_xlabel('Huellenradius R (chi = 1/2), Mitte des Paares')
    ax.set_ylabel('Abstand Delta R benachbarter Stellen derselben Kurve')
    ax.set_title('Abstand gegen R: l = 1 (Kreise) und l = 0 aus Runde 18 (Kreuze)')
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    fig.savefig(aus2, dpi=120)


def main():
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == 'stellen':
        cmd_stellen(a[0], a[1], a[2], a[3])
    elif c == 'final':
        cmd_final(a[0], a[1])
    elif c == 'bild':
        cmd_bild(a[0], a[1], a[2])
    else:
        raise SystemExit('unbekannt: ' + c)


if __name__ == '__main__':
    main()
