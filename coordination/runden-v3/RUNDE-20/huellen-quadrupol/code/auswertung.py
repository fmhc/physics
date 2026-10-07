#!/usr/bin/env python3
"""auswertung.py - Runde 18 HUELLEN-LEITER: Stellen, Abgleich der Stufen, L1-Zuordnung, Stichprobe, Wertung, Bilder.
Regeln: PLAN.md (eingefroren), Abschnitte 4 bis 6."""
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
JMAX = 110   # PLAN-NACHTRAG-4: gewertet nur Paare mit Index <= 109

# Runde 17, STILLE-ZWEIFELD, Tabelle "Gefundene E1-Stellen" (Stufe 1), Umlauf je Stufe gleich
BEKANNT = [
    (1, 0.81864948, 1.05187987, +1), (2, 0.82057924, 1.36200257, -1), (3, 0.82123499, 1.23411245, +1),
    (4, 0.83578650, 1.05931135, -1), (5, 0.83728947, 1.24903866, -1), (6, 0.84015011, 1.40944022, +1),
    (7, 0.84743426, 1.33956049, +1), (8, 0.86038074, 1.27174185, +1), (9, 0.86085981, 1.06976351, +1),
    (10, 0.88121651, 1.39804343, -1), (11, 0.89702906, 1.30955352, -1), (12, 0.90096911, 1.08553960, -1),
    (13, 0.96850582, 1.37891993, +1), (14, 0.97514752, 1.11223140, +1), (15, 1.15865988, 1.17041521, -1)]


def lade(adir, praefix, stufe):
    out = []
    for fn in sorted(os.listdir(adir)):
        if fn.startswith('%s-st%d-' % (praefix, stufe)) and fn.endswith('.json'):
            out.append(json.load(open(os.path.join(adir, fn))))
    return out


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    if rx.std() == 0 or ry.std() == 0:
        return float('nan')
    return float(np.corrcoef(rx, ry)[0, 1])


def rangsprung_plan(za, zb):
    """PLAN 4: Sprung einer Nullstelle gleichen Rangs um mehr als die halbe Luecke zu den Nachbarkurven
    (nur Kurven, nicht die Schwellen; ohne Nachbarkurve kein Merker)."""
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


def punkte_stufe(adir, stufe):
    paare = sorted(lade(adir, 'paar', stufe), key=lambda d: d['i'])
    zs = {z['index']: z for z in lade(adir, 'z', stufe)}
    pk = []
    kstat = dict(rangsprung=0, rangsprung_code=0, weg_unterzeile=0, gerade_fein_ungerade_zeile=0, kurven_paare=0)
    for d in paare:
        rs = rangsprung_plan(zs[d['i']], zs[d['i'] + 1])
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
    return paare, pk, kstat


def punkte_stufe_paare(adir, stufe):
    return lade(adir, 'paar', stufe)


def zeilen_stat(adir, stufe):
    zs = sorted(lade(adir, 'z', stufe), key=lambda d: d['index'])
    out = []
    for z in zs:
        out.append(dict(index=z['index'], w2=z['w2'], Rchi=z.get('Rchi'), chi0=z.get('chi0'), Q=z.get('Q'), E=z.get('E'),
                        n=len(z['null']), unsicher=sum(1 for q in z['null'] if not q['sicher']),
                        rho=[q['rho'] for q in z['null']], s=[q['s'] for q in z['null']],
                        kn=[q['knoten'] for q in z['null']], vz=z['vorzeichen'], n_q=z['n_q'], r_m=z['r_m']))
    return out


def cmd_stellen(adir, aus):
    erg = {}
    P = {}
    for st in (1, 2):
        paare, pk, kstat = punkte_stufe(adir, st)
        zs = zeilen_stat(adir, st)
        abn = [dict(i=a['index'], w2=a['w2'], n_vor=a['n'], n_nach=b['n']) for a, b in zip(zs[:-1], zs[1:]) if b['n'] < a['n']]
        P[st] = pk
        erg['st%d' % st] = dict(n_paare=len(paare), n_zeilen=len(zs), n_punkte=len(pk), kstat=kstat, abnahmen=abn,
                                w2_min_paar=min((d['w2b'] for d in paare), default=None),
                                unsicher_nullstellen=sum(z['unsicher'] for z in zs))
    # Zeilenvergleich der Stufen
    z1 = {z['index']: z for z in zeilen_stat(adir, 1)}
    z2 = {z['index']: z for z in zeilen_stat(adir, 2)}
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
    erg['zeilenvergleich'] = dict(zeilen_beide=len(set(z1) & set(z2)), gleiche_zahl=gleich_n, gleiche_vorzeichen=gleich_vz,
                                  max_drho=diff_rho, abweichungen=ungleich[:40], n_abweichungen=len(ungleich))
    # Abgleich der Stufen je Zeilenpaar und Kurve
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
                            dw2_zeile=q['dw2_zeile'], klammer_w2=q['w2_klammer'], klammer_R=q['R_klammer']))
    for key, lst in by2.items():
        for j, r in enumerate(lst):
            if (key[0], key[1], j) not in benutzt:
                nur2.append(r)
    stellen.sort(key=lambda d: -d['w2'])
    # PLAN-NACHTRAG-2: zusammenhaengender Bereich (alle Paare 0..j-1 auf beiden Stufen) und Insel
    S1 = set(q['i'] for q in P[1]) | set(d['i'] for d in punkte_stufe_paare(adir, 1))
    S2 = set(q['i'] for q in P[2]) | set(d['i'] for d in punkte_stufe_paare(adir, 2))
    j_cont = 0
    while j_cont in S1 and j_cont in S2 and j_cont < JMAX:   # JMAX: PLAN-NACHTRAG-4
        j_cont += 1
    w2_grenze = min((d['w2b'] for d in punkte_stufe_paare(adir, 1) if d['i'] == j_cont - 1), default=None)
    erg['bereich'] = dict(j_cont=j_cont, w2_unten=w2_grenze, paare_st1=len(S1), paare_st2=len(S2),
                          insel_paare=sorted(i for i in (S1 & S2) if i >= j_cont))
    for n, d in enumerate(stellen):
        d['nr'] = n + 1
        d['bereich'] = bool(d['i'] < j_cont)
    erg['insel'] = [dict(nr=d['nr'], k=d['k'], w2=d['w2'], rho=d['rho'], R=d['R'], umlauf=d['umlauf_1'])
                    for d in stellen if d['gezaehlt'] and not d['bereich']]
    gez = [d for d in stellen if d['gezaehlt'] and d['bereich']]
    erg['n_stellen_gepaart'] = len(stellen)
    erg['n_gezaehlt'] = len(gez)
    erg['n_nur_st1'] = len(nur1)
    erg['n_nur_st2'] = len(nur2)
    nb1 = [q for q in nur1 if q['i'] < j_cont]
    nb2 = [r for r in nur2 if r['i'] < j_cont]
    erg['nur_eine_stufe_im_bereich'] = dict(
        n_st1=len(nb1), n_st2=len(nb2),
        st1=[dict(i=q['i'], k=q['k'], w2=q['w2'], rho=q['rho'], umlauf=q['umlauf_zelle'], merker=q['merker']) for q in nb1],
        st2=[dict(i=r['i'], k=r['k'], w2=r['w2'], rho=r['rho'], umlauf=r['umlauf_zelle'], merker=r['merker']) for r in nb2])
    erg['gepaart_nicht_gezaehlt_im_bereich'] = [
        dict(nr=d['nr'], k=d['k'], w2=d['w2'], rho=d['rho'], u1=d['umlauf_1'], u2=d['umlauf_2'], m1=d['merker_1'],
             m2=d['merker_2']) for d in stellen if d['bereich'] and not d['gezaehlt']]
    # L1-Zuordnung
    l1 = []
    for nr, w2k, rk, uk in BEKANNT:
        z = dict(nr=nr, w2=w2k, rho=rk, umlauf=uk)
        for st in (1, 2):
            c = [q for q in P[st] if abs(q['w2'] - w2k) < q['dw2_zeile'] and abs(q['rho'] - rk) < 0.3 * q['gap']]
            c.sort(key=lambda q: abs(q['w2'] - w2k))
            z['st%d' % st] = c[0] if c else None
        l1.append(z)
    erg['l1_zuordnung'] = [dict(nr=z['nr'], st1=bool(z['st1']), st2=bool(z['st2']),
                                k=(z['st1'] or {}).get('k'), w2_st1=(z['st1'] or {}).get('w2'),
                                umlauf_zelle_st1=(z['st1'] or {}).get('umlauf_zelle'),
                                umlauf_zelle_st2=(z['st2'] or {}).get('umlauf_zelle')) for z in l1]
    bek_keys = set()
    for z in l1:
        if z['st1']:
            bek_keys.add((z['st1']['i'], z['st1']['k'], round(z['st1']['w2'], 9)))
    for d in stellen:
        d['bekannt'] = None
        for z in l1:
            if z['st1'] and z['st1']['i'] == d['i'] and z['st1']['k'] == d['k'] and abs(z['st1']['w2'] - d['w2']) < 1e-12:
                d['bekannt'] = z['nr']
    # Umlauf-Punkte: L1 und Stichprobe
    for st in (1, 2):
        pkt = []
        for z in l1:
            q = z['st%d' % st]
            if q:
                pkt.append(dict(name='L1-%d' % z['nr'], w2=q['w2'], rho=q['rho'], gap=q['gap'], dw2_zeile=q['dw2_zeile'],
                                k=q['k'], umlauf_zelle=q['umlauf_zelle']))
        probe = []
        ks = sorted(set(d['k'] for d in gez))
        reihe = [k for k in (0, 1, 2, 3) if k in ks] + [k for k in ks if k >= 4 and k % 4 == 0]
        for k in reihe:
            dk = [d for d in gez if d['k'] == k]
            if not dk:
                continue
            d = min(dk, key=lambda d: d['w2'])
            w2 = d['w2'] if st == 1 else d['w2_2']
            rho = d['rho'] if st == 1 else d['rho_2']
            probe.append(dict(name='P-k%d-nr%d' % (k, d['nr']), w2=w2, rho=rho, gap=d['gap'], dw2_zeile=d['dw2_zeile'],
                              k=k, umlauf_zelle=d['umlauf_%d' % st], nr=d['nr']))
        schreibe(os.path.join(os.path.dirname(aus), 'umlauf-punkte-L1-st%d.json' % st), dict(punkte=pkt))
        schreibe(os.path.join(os.path.dirname(aus), 'umlauf-punkte-P-st%d.json' % st), dict(punkte=probe))
    # Kurven und Wertung L2 bis L5
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
        mid = 0.5 * (w2[:-1] + w2[1:])
        e = dict(k=k, n=len(L), w2=w2.tolist(), R=R.tolist(), rho=[d['rho'] for d in L], umlauf=[d['umlauf_1'] for d in L],
                 dw2=dw.tolist(), dR=dR.tolist(), w2_max=float(w2.max()), w2_min=float(w2.min()))
        if len(dR) >= 1:
            e['dR_mittel'] = float(dR.mean())
        if len(dR) >= 3:
            e['cv_dR'] = float(dR.std(ddof=1) / dR.mean())
        if len(dw) >= 4:
            e['spearman_dw2_w2'] = spearman(dw, mid)
        e['umlauf_wechselt'] = bool(all(L[i]['umlauf_1'] == -L[i + 1]['umlauf_1'] for i in range(len(L) - 1)))
        kst.append(e)
    erg['kurven'] = kst
    l2n = sum(1 for d in gez if d['w2'] < 0.819 and d['bekannt'] is None)
    erg['L2'] = dict(n=l2n, eingetroffen=bool(l2n >= 10))
    l3 = []
    for k in (0, 1, 2, 3):
        e = next((e for e in kst if e['k'] == k), None)
        l3.append(dict(k=k, n_abstaende=(len(e['dw2']) if e else 0), spearman=(e.get('spearman_dw2_w2') if e else None)))
    if any(x['n_abstaende'] < 4 for x in l3):
        l3v = 'offen'
    else:
        l3v = 'eingetroffen' if all(x['spearman'] is not None and x['spearman'] > 0.8 for x in l3) else 'nicht eingetroffen'
    erg['L3'] = dict(kurven=l3, ausgang=l3v)
    l4 = [dict(k=e['k'], n=e['n'], cv=e['cv_dR'], dR_mittel=e['dR_mittel']) for e in kst if e['n'] >= 4]
    erg['L4'] = dict(kurven=l4, n_kurven=len(l4), n_cv_klein=sum(1 for x in l4 if x['cv'] < 0.25),
                     ausgang=('offen' if not l4 else ('eingetroffen' if all(x['cv'] < 0.25 for x in l4)
                                                      else 'nicht eingetroffen')),
                     k0_3=[x for x in l4 if x['k'] <= 3])
    l5 = sorted(set(d['k'] for d in gez if d['k'] >= 4))
    erg['L5'] = dict(kurven_k_ge_4=l5, eingetroffen=bool(l5))
    schreibe(aus, erg)
    schreibe(os.path.join(os.path.dirname(aus), 'stellen.json'), dict(stellen=stellen, nur_st1=nur1, nur_st2=nur2))
    print(json.dumps({k: erg[k] for k in ('st1', 'st2', 'zeilenvergleich', 'n_stellen_gepaart', 'n_gezaehlt', 'n_nur_st1',
                                          'n_nur_st2', 'L2', 'L3', 'L5')}, indent=1))
    print(json.dumps(erg['L4'], indent=1))


def cmd_final(adir, aus):
    erg = json.load(open(os.path.join(adir, 'auswertung.json')))
    bek = {nr: (w, r, u) for nr, w, r, u in BEKANNT}
    l1 = {}
    for st in (1, 2):
        for fn in sorted(os.listdir(adir)):
            if fn.startswith('umlauf-L1-st%d' % st) and fn.endswith('.json'):
                for e in json.load(open(os.path.join(adir, fn)))['punkte']:
                    nr = int(e['name'].split('-')[1])
                    w, r, u = bek[nr]
                    um = e.get('umlauf') or {}
                    l1.setdefault(nr, {})['st%d' % st] = dict(
                        w2=e['w2'], rho=e['rho'], konv=e['konvergiert'], dw2=e['w2'] - w, drho=e['rho'] - r,
                        umlauf=um.get('umlauf'), aufgeloest=um.get('aufgeloest'), sprung=um.get('groesster_sprung'),
                        punkte=um.get('punkte'), versuch=um.get('versuch'), svr=e.get('svr'),
                        umlauf_zelle=e['start'].get('umlauf_zelle'), chi0=e.get('chi0'), Rchi=e.get('Rchi'),
                        ok=bool(e['konvergiert'] and abs(e['w2'] - w) <= 1e-6 and abs(e['rho'] - r) <= 1e-6 and
                                um.get('aufgeloest') and um.get('umlauf') == u))
    n_ok = sum(1 for nr in bek if all(l1.get(nr, {}).get('st%d' % st, {}).get('ok') for st in (1, 2)))
    erg['L1'] = dict(je_stelle=l1, n_wiedergefunden=n_ok, eingetroffen=bool(n_ok == 15))
    pr = {}
    for st in (1, 2):
        for fn in sorted(os.listdir(adir)):
            if fn.startswith('umlauf-P-st%d' % st) and fn.endswith('.json'):
                for e in json.load(open(os.path.join(adir, fn)))['punkte']:
                    um = e.get('umlauf') or {}
                    pr.setdefault(e['name'], {})['st%d' % st] = dict(
                        w2=e['w2'], rho=e['rho'], konv=e['konvergiert'], start_w2=e['start']['w2'],
                        start_rho=e['start']['rho'], umlauf=um.get('umlauf'), aufgeloest=um.get('aufgeloest'),
                        sprung=um.get('groesster_sprung'), punkte=um.get('punkte'), svr=e.get('svr'),
                        umlauf_zelle=e['start'].get('umlauf_zelle'), hmax=e.get('hmax'), Rchi=e.get('Rchi'),
                        chi0=e.get('chi0'))
    erg['stichprobe'] = pr
    schreibe(aus, erg)
    print(json.dumps(erg['L1'], indent=1))
    print(json.dumps(pr, indent=1))


def cmd_bild(adir, aus1, aus2):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    st = json.load(open(os.path.join(adir, 'stellen.json')))['stellen']
    gez = [d for d in st if d['gezaehlt'] and d.get('bereich')]
    zs = [z for z in sorted(lade(adir, 'z', 2), key=lambda d: d['index']) if z['index'] <= JMAX]
    if not zs:
        zs = sorted(lade(adir, 'z', 1), key=lambda d: d['index'])
    cmap = plt.get_cmap('tab10')
    fig, axs = plt.subplots(1, 2, figsize=(16, 7))
    for ax, (x0, x1) in zip(axs, ((0.76, 1.405), (0.76, 0.83))):
        for z in zs:
            if not (x0 <= z['w2'] <= x1):
                continue
            for k, q in enumerate(z['null']):
                ax.plot(z['w2'], q['rho'], '.', ms=1.2, color=cmap(k % 10))
        for d in gez:
            if x0 <= d['w2'] <= x1:
                ax.plot(d['w2'], d['rho'], '^' if d['umlauf_1'] > 0 else 'v', ms=4, mfc='none', mec='k', mew=0.6)
        for nr, w, r, u in BEKANNT:
            if x0 <= w <= x1:
                ax.plot(w, r, '*', ms=11, mfc='gold', mec='k', mew=0.6)
        ax.set_xlim(x0, x1)
        ax.set_xlabel('omega^2')
        ax.set_ylabel('rho')
    axs[0].set_title('Stellen (Dreieck auf: Umlauf +1, ab: -1; Stern: Runde 17) auf den chi-Kurven (Farbe = k mod 10)')
    axs[1].set_title('Ausschnitt Duennwand 0,76 bis 0,83 (gewertet bis 0,7635)')
    fig.tight_layout()
    fig.savefig(aus1, dpi=120)
    fig, axs = plt.subplots(1, 2, figsize=(16, 6.5))
    ks = sorted(set(d['k'] for d in gez))
    for k in ks:
        L = sorted([d for d in gez if d['k'] == k], key=lambda d: -d['w2'])
        if len(L) < 2:
            continue
        R = np.array([d['R'] for d in L])
        w2 = np.array([d['w2'] for d in L])
        col = cmap(k % 10)
        axs[0].plot(0.5 * (R[1:] + R[:-1]), np.diff(R), '.-', ms=3, lw=0.6, color=col, label=('k=%d' % k) if k <= 9 else None)
        axs[1].semilogy(0.5 * (w2[1:] + w2[:-1]), -np.diff(w2), '.-', ms=3, lw=0.6, color=col)
    axs[0].set_xlabel('Huellenradius R (chi = 1/2), Mitte des Paares')
    axs[0].set_ylabel('Abstand Delta R benachbarter Stellen derselben Kurve')
    axs[0].set_title('Abstand gegen R je chi-Kurve (Farbe = k mod 10)')
    axs[0].legend(fontsize=7, ncol=2)
    axs[1].set_xlabel('omega^2 (Mitte des Paares)')
    axs[1].set_ylabel('Delta omega^2')
    axs[1].set_title('Abstand in omega^2 je Kurve (logarithmisch)')
    fig.tight_layout()
    fig.savefig(aus2, dpi=120)


def main():
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == 'stellen':
        cmd_stellen(a[0], a[1])
    elif c == 'final':
        cmd_final(a[0], a[1])
    elif c == 'bild':
        cmd_bild(a[0], a[1], a[2])
    else:
        raise SystemExit('unbekannt: ' + c)


if __name__ == '__main__':
    main()
