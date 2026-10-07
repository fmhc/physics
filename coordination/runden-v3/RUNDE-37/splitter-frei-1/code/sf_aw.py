#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SPLITTER-FREI-1: mechanische Auswertung nach PLAN 7 (Urteile SF0 bis SF4, Tabellen). Liest nur JSON-Dateien.
Aufruf ueber sf.py: sf.py aw --lauf lauf --hmref <hodge-masse-1/lauf> --lrref <lund-regge-masse-1/lauf> --out lauf/auswertung.json
"""
import json, os, sys, glob, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hm  # noqa: E402

SAATEN = (1, 2, 3, 4)
KL_LR = (0.005, 0.2)
HM_TAB = {1: (10, 6), 2: (9, 5), 3: (10, 7), 4: (9, 6)}            # HODGE-MASSE-1 Tab. 4.2: neg A1RH, A2RH je Saat
LR_TAB = {1: (27, 28), 2: (30, 31), 3: (31, 33), 4: (28, 28)}      # LUND-REGGE-MASSE-1 4.1: wachsend je Spannenpunkt
VAR = ('A1R1', 'A1RH', 'A2R1', 'A2RH', 'A2LR2', 'A2LRH', 'A2LRHL', 'A2LR1')


def lade(p):
    with open(p) as fh:
        return json.load(fh)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def erg(p):
    return lade(p)['ergebnis'] if os.path.exists(p) else None


def punkte(d):
    """(ridx, eps-Schluessel, Punkt) aller Punkte eines hm-Laufs."""
    for z in d['zeilen']:
        for e in ('eps1', 'eps2'):
            if e in z:
                yield z['ridx'], e, z[e]


def hm_zusammen(lauf, a, s, D):
    """Teillaeufe hm-<a>-s<s>-a/-b (Richtungen 0-6, 7-12) zusammenfuehren, Spannen mit hm.spannen."""
    teile = []
    for h in ('a', 'b'):
        p = os.path.join(lauf, 'hm-%s-s%d-%s.json' % (a, s, h))
        if os.path.exists(p):
            teile.append(lade(p)['ergebnis'])
            D['dateien'][os.path.basename(p)] = sha(p)
    if not teile:
        return None
    d = dict(teile[0])
    d['zeilen'] = sorted([z for t in teile for z in t['zeilen']], key=lambda z: z['ridx'])
    d['spannen'] = hm.spannen(d['zeilen'], d['eps'])
    d['vollstaendig'] = len(d['zeilen']) == 13
    d['richtung'] = {z['ridx']: z['richtung'] for z in d['zeilen']}
    return d


def hm_ref(hmref, s):
    zs = []
    dat = {}
    for h in ('a', 'b'):
        p = os.path.join(hmref, 'sp-glas-s%d-%s.json' % (s, h))
        if not os.path.exists(p):
            return None, None
        zs += lade(p)['ergebnis']['zeilen']
        dat[os.path.basename(p)] = sha(p)
    return sorted(zs, key=lambda z: z['ridx']), dat


def auswerten(lauf, hmref, lrref, out):
    D = {'dateien': {}}
    bau = {}
    for p in sorted(glob.glob(os.path.join(lauf, 'bau-*.json'))):
        e = lade(p)['ergebnis']
        D['dateien'][os.path.basename(p)] = sha(p)
        for s, v in e['saaten'].items():
            bau[int(s)] = v
    H = {(a, s): hm_zusammen(lauf, a, s, D) for a in ('orig', 'sf') for s in SAATEN}
    R = {(a, s): erg(os.path.join(lauf, 'lr-%s-s%d.json' % (a, s))) for a in ('orig', 'sf') for s in SAATEN}
    for a in ('orig', 'sf'):
        for s in SAATEN:
            p = os.path.join(lauf, 'lr-%s-s%d.json' % (a, s))
            if os.path.exists(p):
                D['dateien'][os.path.basename(p)] = sha(p)
    D['vollstaendig'] = {'%s-s%d' % k: (v is not None and v['vollstaendig']) for k, v in H.items()}
    D['vollstaendig'].update({'lr-%s-s%d' % k: (v is not None and len(v['zeilen']) == 13) for k, v in R.items()})
    # gueltige splitterarme Glaeser: Schranke erreicht (voller Saum), Zerlegung gueltig, nicht kristallin
    gueltig = {}
    for s in SAATEN:
        b = bau.get(s)
        ok = bool(b and b['bau']['erreicht'] and not b['sf']['kristall']['kristallin']
                  and b['sf']['pruefung']['dieder_summe_minus_2pi_max'] < 1e-9
                  and b['sf']['pruefung']['volumen_summe_rel_abw'] < 1e-12 and b['sf']['pruefung']['selbstkanten'] == 0)
        gueltig[s] = ok
    D['sf_gueltig'] = gueltig
    U = {}

    # ---------------- SF0
    mism, vergl, fehlt = [], 0, False
    wort = {}
    for s in SAATEN:
        d = H[('orig', s)]
        ref, rd = hm_ref(hmref, s)
        if d is None or ref is None:
            fehlt = True
        else:
            fehlt = fehlt or not d['vollstaendig']
            D['dateien'].update(rd)
            rz = {z['ridx']: z for z in ref}
            for ridx, e, p in punkte(d):
                for v in ('A1RH', 'A2RH'):
                    if e in rz[ridx]:
                        vergl += 1
                        if p.get(v, {}).get('n_neg') != rz[ridx][e][v]['n_neg']:
                            mism.append(('hm', s, ridx, e, v, p.get(v, {}).get('n_neg'), rz[ridx][e][v]['n_neg']))
        dl = R[('orig', s)]
        pl = os.path.join(lrref, 'sp-glas-s%d.json' % s)
        if dl is None or not os.path.exists(pl):
            fehlt = True
        else:
            D['dateien'][os.path.basename(pl) + '(lrref)'] = sha(pl)
            rz = {z['richtung']: z for z in lade(pl)['ergebnis']['zeilen']}
            for z in dl['zeilen']:
                for kl in KL_LR:
                    vergl += 1
                    mine = z['kl%g' % kl].get('n_wachsend')
                    soll = rz[z['richtung']]['kl%g' % kl].get('n_wachsend')
                    if mine != soll:
                        mism.append(('lr', s, z['richtung'], kl, 'LR', mine, soll))
        # Wortlaut: je Saat die berichteten Zahlen
        w = {}
        if d is not None:
            w['A1RH_max'] = max(p['A1RH']['n_neg'] for _, _, p in punkte(d) if 'A1RH' in p)
            w['A2RH_max'] = max(p['A2RH']['n_neg'] for _, _, p in punkte(d) if 'A2RH' in p)
        if dl is not None:
            nw = [z['kl%g' % kl]['n_wachsend'] for z in dl['zeilen'] for kl in KL_LR if 'n_wachsend' in z['kl%g' % kl]]
            w['LR_bereich'] = [min(nw), max(nw)]
        w['gleich'] = bool(d is not None and dl is not None and (w['A1RH_max'], w['A2RH_max']) == HM_TAB[s]
                           and tuple(w['LR_bereich']) == LR_TAB[s])
        wort[s] = w
    U['SF0'] = {'plan': ('verfehlt' if mism else ('nicht entscheidbar' if fehlt else 'eingetroffen')),
                'wortlaut': ('eingetroffen' if all(wort[s]['gleich'] for s in SAATEN) else
                             ('nicht entscheidbar' if fehlt and not any(not wort[s]['gleich'] and 'LR_bereich' in wort[s]
                                                                        and 'A1RH_max' in wort[s] for s in SAATEN)
                              else 'verfehlt')),
                'n_vergleiche': vergl, 'abweichungen': mism, 'je_saat': wort}

    # ---------------- SF1 (Originalglas, alle Punkte, alle wachsenden Moden von A1RH und A2RH)
    fs, n_inkons, fehlt = [], [], False
    lok = {}
    for s in SAATEN:
        d = H[('orig', s)]
        if d is None:
            fehlt = True
            continue
        fehlt = fehlt or not d['vollstaendig']
        for v in ('A1RH', 'A2RH', 'A2LR1', 'A2LRH'):
            ff = {'q5': [], 'q1': [], 'q10': [], 'v5': [], 'pr': []}
            for ridx, e, p in punkte(d):
                lo = p.get('lokal', {})
                if not lo.get('B_red_pd'):
                    continue
                if v in p and lo[v]['n_neg_eigh'] != p[v]['n_neg']:
                    n_inkons.append((s, ridx, e, v, lo[v]['n_neg_eigh'], p[v]['n_neg']))
                for mo in lo[v]['moden']:
                    for nm in ('q5', 'q1', 'q10', 'v5'):
                        ff[nm].append(mo['f_' + nm])
                    ff['pr'].append(mo['pr'])
                    if v in ('A1RH', 'A2RH'):
                        fs.append((s, v, ridx, e, mo['f_q5']))
            lok[(s, v)] = ff
    if fehlt or not fs:
        u1p = u1w = 'nicht entscheidbar'
    else:
        f = np.array([x[4] for x in fs])
        u1p = 'eingetroffen' if (f >= 0.5).all() else 'verfehlt'
        u1w = 'eingetroffen' if (f >= 0.25).all() else 'verfehlt'
    fa = np.array([x[4] for x in fs]) if fs else np.array([np.nan])
    U['SF1'] = {'plan': u1p, 'wortlaut': u1w, 'n_moden': len(fs), 'f_min': float(np.nanmin(fa)),
                'f_median': float(np.nanmedian(fa)), 'f_max': float(np.nanmax(fa)),
                'n_ab_0.5': int((fa >= 0.5).sum()), 'n_ab_0.25': int((fa >= 0.25).sum()),
                'inkonsistent_eigh_gegen_hm': n_inkons}

    # ---------------- SF2 (splitterarmes Glas: A1RH, A2RH an allen HM-Punkten ohne wachsende Mode)
    neg, ne, gs = [], False, []
    for s in SAATEN:
        d = H[('sf', s)]
        if d is None or not gueltig[s]:
            ne = True
            continue
        ne = ne or not d['vollstaendig']
        gs.append(s)
        for ridx, e, p in punkte(d):
            if not p.get('B_red_pd'):
                ne = True
                continue
            for v in ('A1RH', 'A2RH'):
                if p[v]['n_neg'] > 0:
                    neg.append((s, ridx, e, v, p[v]['n_neg']))
    u2 = 'verfehlt' if neg else ('nicht entscheidbar' if (ne or not gs) else 'eingetroffen')
    U['SF2'] = {'plan': u2, 'wortlaut': u2, 'saaten_gewertet': gs, 'punkte_mit_wachsend': len(neg),
                'max_n_neg': {v: max([x[4] for x in neg if x[3] == v], default=0) for v in ('A1RH', 'A2RH')},
                'liste': neg[:80]}

    # ---------------- SF3 (splitterarmes Glas: LR mit R1 an jedem gerechneten k mindestens 10 wachsende Moden)
    klein, sing, gs3, nw_all = [], [], [], []
    klein_w = []
    for s in SAATEN:
        dl = R[('sf', s)]
        if dl is None or not gueltig[s]:
            continue
        gs3.append(s)
        for z in dl['zeilen']:
            for kl in KL_LR:
                p = z['kl%g' % kl]
                if not p.get('legendre_regulaer'):
                    sing.append((s, z['richtung'], kl))
                    continue
                nw_all.append(p['n_wachsend'])
                if p['n_wachsend'] < 10:
                    klein.append((s, z['richtung'], kl, p['n_wachsend']))
        d = H[('sf', s)]
        if d is not None:
            for ridx, e, p in punkte(d):
                if 'A2LR1' in p and p['A2LR1']['n_neg'] < 10:
                    klein_w.append((s, ridx, e, p['A2LR1']['n_neg']))
    if klein:
        u3p = 'verfehlt'
    elif sing or len(gs3) < 1 or len(gs3) < sum(1 for s in SAATEN if gueltig[s]):
        u3p = 'nicht entscheidbar'
    else:
        u3p = 'eingetroffen' if len(gs3) == 4 else 'eingetroffen (nur Saaten %s)' % gs3
    u3w = 'verfehlt' if (klein or klein_w) else u3p
    U['SF3'] = {'plan': u3p, 'wortlaut': u3w, 'saaten_gewertet': gs3,
                'n_wachsend_bereich': [min(nw_all), max(nw_all)] if nw_all else None,
                'unter_10_LR_satz': klein, 'unter_10_HM_satz_A2LR1': klein_w, 'legendre_singulaer': sing}

    # ---------------- SF4 (TT-Spanne A1R1: splitterarm gegen Original)
    sp = {}
    for a in ('orig', 'sf'):
        for s in SAATEN:
            d = H[(a, s)]
            if d is None or not d['vollstaendig']:
                continue
            x = d['spannen']['A1R1']
            sp[(a, s)] = (x['spanne_eps1'], x['alle_ok'])
    paare = [s for s in SAATEN if ('orig', s) in sp and ('sf', s) in sp and gueltig[s]]
    alle_ok = all(sp[(a, s)][1] and sp[(a, s)][0] is not None for s in paare for a in ('orig', 'sf'))
    if len(paare) < 4 or not alle_ok:
        u4p = u4w = 'nicht entscheidbar'
        m_o = m_s = None
    else:
        m_o = float(np.mean([sp[('orig', s)][0] for s in paare]))
        m_s = float(np.mean([sp[('sf', s)][0] for s in paare]))
        u4p = 'eingetroffen' if m_s <= 0.5 * m_o else 'verfehlt'
        u4w = 'eingetroffen' if all(sp[('sf', s)][0] <= 0.5 * sp[('orig', s)][0] for s in paare) else 'verfehlt'
    U['SF4'] = {'plan': u4p, 'wortlaut': u4w, 'mittel_orig': m_o, 'mittel_sf': m_s,
                'je_saat': {s: {'orig': sp.get(('orig', s)), 'sf': sp.get(('sf', s))} for s in SAATEN}}

    # ---------------- Kontrolle: A1R1-Spannen und Werte des Originalglases gegen HODGE-MASSE-1
    kontr = {}
    for s in SAATEN:
        d = H[('orig', s)]
        ref, _ = hm_ref(hmref, s)
        if d is None or ref is None:
            continue
        rsp = hm.spannen(ref, d['eps'])
        kontr[s] = {v: {'hier': d['spannen'][v]['spanne_eps1'], 'hm': rsp[v]['spanne_eps1']} for v in VAR}
        rz = {z['ridx']: z for z in ref}
        dmax = 0.0
        for ridx, e, p in punkte(d):
            if e in rz[ridx]:
                for v in VAR:
                    if v not in p or v not in rz[ridx][e]:
                        continue
                    a1, b1 = np.array(p[v]['w2k2']), np.array(rz[ridx][e][v]['w2k2'])
                    dmax = max(dmax, float(np.max(np.abs(a1 - b1) / np.abs(b1))))
        kontr[s]['w2k2_rel_abw_max'] = dmax
    D['kontrolle_hm'] = kontr
    D['urteile'] = U

    # ---------------- Tabellen
    T = []
    T.append('## Formstatistik und Kristallprobe (Bau, voller Saum)\n')
    T.append('| Saat | Glas | T | q_min | q 1 % | q 5 % | q Median | n(q<0,1) | n(q<0,2) | vol_min/Mittel | Q6 (r<1,35) | Q6 Delaunay | max S(q) | kristallin | l_mittel |')
    T.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for s in SAATEN:
        b = bau.get(s)
        if not b:
            continue
        for a in ('orig', 'sf'):
            f, k = b[a]['form'], b[a]['kristall']
            T.append('| s%d | %s | %d | %.4f | %.4f | %.4f | %.4f | %d | %d | %.4f | %.4f | %.4f | %.2f | %s | %.4f |' % (
                s, a, f['T'], f['q_min'], f['q_1proz'], f['q_5proz'], f['q_median'], f['n_q_unter']['0.1'],
                f['n_q_unter']['0.2'], f['vol_min_rel_mittel'], k['Q6_rc'], k['Q6_delaunay'], k['S_max'],
                'ja' if k['kristallin'] else 'nein', b[a]['l_mittel']))
    T.append('\n| Saat | Schranke erreicht | Versuche / angenommen | Bauzeit s | bewegte Punkte | mittl. Verschiebung (alle) | max. Verschiebung | mittl. NN-Abstand Original | Triang = tg |')
    T.append('|---|---|---|---|---|---|---|---|---|')
    for s in SAATEN:
        b = bau.get(s)
        if not b:
            continue
        bb = b['bau']
        vv = bb['verschiebung']
        T.append('| s%d | %s | %d / %d | %.0f | %d | %.4f | %.4f | %.4f | %s |' % (
            s, 'ja' if bb['erreicht'] else 'nein', bb['versuche'], bb['angenommen'], bb['t_s'], vv['n_bewegt'],
            vv['mittel_alle'], vv['max'], vv['mittlerer_nn_abstand_original'], b['kontr_triang_gleich_tg']))
    T.append('\n## Wachsende Moden je Paarung und Saat (HM-Satz: 13 Richtungen bei |k| = 1e-2, [100], [110], [111] auch bei 2e-2; Bereich ueber die 16 Punkte)\n')
    T.append('| Saat | Glas | ' + ' | '.join(VAR) + ' |')
    T.append('|---|---|' + '---|' * len(VAR))
    for s in SAATEN:
        for a in ('orig', 'sf'):
            d = H[(a, s)]
            if d is None:
                continue
            cells = []
            for v in VAR:
                nn = [p[v]['n_neg'] for _, _, p in punkte(d) if v in p]
                cells.append('%d-%d' % (min(nn), max(nn)) if nn else '-')
            T.append('| s%d | %s | %s |' % (s, a, ' | '.join(cells)))
    T.append('\n## Wachsende Moden je k (A1RH / A2RH / A2LR1 / A2LRH; HM-Zaehlregel) \n')
    for a in ('orig', 'sf'):
        for s in SAATEN:
            d = H[(a, s)]
            if d is None:
                continue
            row = []
            for ridx, e, p in punkte(d):
                row.append('%s%s:%s/%s/%s/%s' % (d['richtung'][ridx], '' if e == 'eps1' else "'",
                                                 p.get('A1RH', {}).get('n_neg'), p.get('A2RH', {}).get('n_neg'),
                                                 p.get('A2LR1', {}).get('n_neg'), p.get('A2LRH', {}).get('n_neg')))
            T.append('- %s s%d: ' % (a, s) + ', '.join(row))
    T.append("\n(' = |k| = 2e-2)\n")
    T.append('## Lund-Regge mit R1 (LR-Satz, Zaehlregel LUND-REGGE-MASSE-1): wachsende Moden, Bereich ueber 13 Richtungen\n')
    T.append('| Saat | Glas | kl = 0,005 | kl = 0,2 | Legendre singulaer | A1R1 wachsend (max) |')
    T.append('|---|---|---|---|---|---|')
    for s in SAATEN:
        for a in ('orig', 'sf'):
            dl = R[(a, s)]
            if dl is None:
                continue
            c = []
            for kl in KL_LR:
                nw = [z['kl%g' % kl]['n_wachsend'] for z in dl['zeilen'] if 'n_wachsend' in z['kl%g' % kl]]
                c.append('%d-%d' % (min(nw), max(nw)) if nw else '-')
            nsing = sum(1 for z in dl['zeilen'] for kl in KL_LR if not z['kl%g' % kl].get('legendre_regulaer'))
            a1 = max(z['kl%g' % kl]['A1R1']['n_wachsend'] for z in dl['zeilen'] for kl in KL_LR)
            T.append('| s%d | %s | %s | %s | %d | %d |' % (s, a, c[0], c[1], nsing, a1))
    T.append('\n## Lokalisierung der wachsenden Moden auf dem Originalglas (Anteil von sum |a_e|^2 auf Kanten der schlechtesten Tetraeder)\n')
    T.append('| Saat | Paarung | Moden | f_q5 min / Median / max | n(f_q5 >= 0,5) | n(f_q5 >= 0,25) | Kantenanteil q5 (Zufall) | f_q1 Median | f_q10 Median | f_v5 Median | PR Median |')
    T.append('|---|---|---|---|---|---|---|---|---|---|---|')
    for s in SAATEN:
        d = H[('orig', s)]
        if d is None:
            continue
        for v in ('A1RH', 'A2RH', 'A2LR1', 'A2LRH'):
            ff = lok.get((s, v))
            if not ff or not ff['q5']:
                T.append('| s%d | %s | 0 | - | - | - | %.3f | - | - | - | - |' % (s, v, d['masken']['q5']['kantenanteil']))
                continue
            q5 = np.array(ff['q5'])
            T.append('| s%d | %s | %d | %.3f / %.3f / %.3f | %d | %d | %.3f | %.3f | %.3f | %.3f | %.4f |' % (
                s, v, len(q5), q5.min(), np.median(q5), q5.max(), (q5 >= 0.5).sum(), (q5 >= 0.25).sum(),
                d['masken']['q5']['kantenanteil'], np.median(ff['q1']), np.median(ff['q10']), np.median(ff['v5']),
                np.median(ff['pr'])))
    T.append('\n## Lokalisierung auf dem splitterarmen Glas (beschreibend; Masken aus dessen eigenen schlechtesten Tetraedern)\n')
    T.append('| Saat | Paarung | Moden | f_q5 min / Median / max | Kantenanteil q5 |')
    T.append('|---|---|---|---|---|')
    for s in SAATEN:
        d = H[('sf', s)]
        if d is None:
            continue
        for v in ('A1RH', 'A2RH', 'A2LR1', 'A2LRH'):
            q5 = [mo['f_q5'] for _, _, p in punkte(d) if p.get('lokal', {}).get('B_red_pd') for mo in p['lokal'][v]['moden']]
            if q5:
                q5 = np.array(q5)
                T.append('| s%d | %s | %d | %.3f / %.3f / %.3f | %.3f |' % (s, v, len(q5), q5.min(), np.median(q5), q5.max(),
                                                                     d['masken']['q5']['kantenanteil']))
            else:
                T.append('| s%d | %s | 0 | - | %.3f |' % (s, v, d['masken']['q5']['kantenanteil']))
    T.append('\n## TT-Spanne (26 Werte bei |k| = 1e-2; * = nicht alle 16 Punkte ok)\n')
    T.append('| Saat | Glas | ' + ' | '.join(VAR) + ' |')
    T.append('|---|---|' + '---|' * len(VAR))
    for s in SAATEN:
        for a in ('orig', 'sf'):
            d = H[(a, s)]
            if d is None:
                continue
            cells = []
            for v in VAR:
                x = d['spannen'][v]
                cells.append(('%.4g %%' % (100 * x['spanne_eps1']) if x['spanne_eps1'] is not None else '-') +
                             ('' if x['alle_ok'] else '*'))
            T.append('| s%d | %s | %s |' % (s, a, ' | '.join(cells)))
    T.append('\n## Urteile\n')
    for nr in ('SF0', 'SF1', 'SF2', 'SF3', 'SF4'):
        T.append('- %s: nach Plan **%s**, nach Kartenwortlaut **%s**' % (nr, U[nr]['plan'], U[nr]['wortlaut']))
    md = '\n'.join(T) + '\n'
    with open(out.replace('.json', '-tabellen.md'), 'w') as fh:
        fh.write(md)
    D['tabellen_md'] = os.path.basename(out.replace('.json', '-tabellen.md'))
    return D
