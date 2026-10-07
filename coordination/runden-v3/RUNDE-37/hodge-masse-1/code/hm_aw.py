#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HODGE-MASSE-1: Auswertung (Urteile HM0 bis HM4 nach PLAN 7, Tabellen, Bild). Liest nur JSON-Dateien.
Aufruf: hm_aw.py --ordner lauf --td1 /home/fmh/fmhc-physics-remote/takt-dynamik-1/lauf --out lauf/auswertung.json
"""
import argparse, json, os, sys, glob, hashlib, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hm  # noqa: E402

NETZE = ['V', 'S', 'A15', 'glas-s1', 'glas-s2', 'glas-s3', 'glas-s4']
TAB_VAR = ['A1R1', 'A1RH', 'A2R1', 'A2RH', 'A2LR2', 'A2LRH', 'A2LRHL', 'A2LR1']
REF = {('V', 'A1R1'): 0.06338809562866454, ('V', 'A2R1'): 0.05924, ('V', 'A2LR2'): 0.03182,
       ('S', 'A1R1'): 0.026847167230505953, ('S', 'A2R1'): 0.06408, ('S', 'A2LR2'): 0.00303,
       ('A15', 'A1R1'): 0.00933868,
       ('glas-s1', 'A1R1'): 0.1093, ('glas-s2', 'A1R1'): 0.1138, ('glas-s3', 'A1R1'): 0.2370, ('glas-s4', 'A1R1'): 0.1246,
       ('glas-s1', 'A2LR2'): 0.0819, ('glas-s2', 'A2LR2'): 0.0718, ('glas-s3', 'A2LR2'): 0.0801, ('glas-s4', 'A2LR2'): 0.0854}


def lade(p):
    with open(p) as fh:
        return json.load(fh)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def netzdaten(ordner, n):
    if n.startswith('glas'):
        teile = [ordner + '/sp-%s-a.json' % n, ordner + '/sp-%s-b.json' % n]
    else:
        teile = [ordner + '/sp-%s.json' % n]
    if not all(os.path.exists(p) for p in teile):
        return None
    ds = [lade(p)['ergebnis'] for p in teile]
    zeilen = sorted([z for d in ds for z in d['zeilen']], key=lambda z: z['ridx'])
    erg = dict(ds[0])
    erg['zeilen'] = zeilen
    erg['spannen'] = hm.spannen(zeilen, ds[0]['eps'])
    erg['dateien'] = {os.path.basename(p): sha(p) for p in teile}
    erg['n_richtungen'] = len(zeilen)
    return erg


def rel_abw(a, b):
    a, b = np.array(a, float), np.array(b, float)
    return float(np.max(np.abs(a - b) / np.abs(b)))


def hm1_auswerten(d):
    out = {}
    ok_all = all(z['eps%d' % i]['A1R1']['ok'] and z['eps%d' % i]['A1RH']['ok'] for z in d['zeilen'] for i in (1, 2))
    for kin in ('A1', 'A2', 'A2L'):
        e = d['eich']
        q = {}
        for nm, (x, y) in {'RH_E_hamilton_gegen_G1_symplektisch': ('E_RH_hamilton', 'G1_RH_symplektisch'),
                           'RH_E_hamilton_gegen_G2_symplektisch': ('E_RH_hamilton', 'G2_RH_symplektisch'),
                           'RH_E_hamilton_gegen_E_lagrange': ('E_RH_hamilton', 'E_RH_lagrange'),
                           'RH_E_hamilton_gegen_G1_lagrange': ('E_RH_hamilton', 'G1_RH_lagrange'),
                           'R1_E_gegen_G1_R1G': ('E_R1', 'G1_R1G'), 'R1_E_gegen_G2_R1G': ('E_R1', 'G2_R1G'),
                           'R1_E_gegen_G1_R1P': ('E_R1', 'G1_R1P'), 'R1_E_gegen_G2_R1P': ('E_R1', 'G2_R1P'),
                           'R2_E_gegen_G1': ('E_R2', 'G1_R2'), 'R2_E_gegen_G2': ('E_R2', 'G2_R2'),
                           'R1_gegen_RH_auf_E': ('E_R1', 'E_RH_hamilton')}.items():
            q[nm] = max(rel_abw(r[kin][x], r[kin][y]) for r in e)
        out[kin] = q
    out['ohne_c_A1_abw_max'] = max(r['ohne_c_A1']['abw_rel_max'] for r in d['eich'])
    out['alle_ok_A1'] = bool(ok_all)
    a = out['A1']
    if not ok_all:
        out['urteil_plan'] = out['urteil_wortlaut'] = 'nicht entscheidbar'
    else:
        i_ = a['RH_E_hamilton_gegen_G1_symplektisch'] <= 1e-10
        out['urteil_plan'] = 'eingetroffen' if (i_ and a['R1_E_gegen_G1_R1G'] > 1e-4) else 'verfehlt'
        out['urteil_wortlaut'] = 'eingetroffen' if (i_ and a['R1_E_gegen_G1_R1P'] > 1e-4) else 'verfehlt'
    return out


def td_lauf(p):
    if not os.path.exists(p):
        return None
    r = lade(p)['ergebnis']
    ev = [e for e in r['ereignisse'] if e.get('ausgefuehrt')]
    z = {'fertig': r['fertig'], 'n_zuege': len(ev), 'n_23': sum(1 for e in ev if e['typ'] == 23),
         'n_32': sum(1 for e in ev if e['typ'] == 32), 'T': r['T'], 'NT': r['NT'], 'omega_max': r['omega_max'],
         'mode_omega': r['mode']['omega'], 'mode_anteil': r['mode']['anteil_TT_welle'], 'H0': r['H0'],
         'abbruch': r['abbruch'], 'wand_s': r.get('wand_s')}
    pr = np.array([q[:4] for q in r['proben']])
    if len(pr):
        z['drift_ende'] = float((pr[-1, 1] - r['H0']) / r['H0'])
        z['drift_max'] = float(np.abs(pr[:, 1] - r['H0']).max() / r['H0'])
    for typ in (23, 32):
        s = [e for e in ev if e['typ'] == typ]
        if s:
            dh = np.array([e['dH_rel'] for e in s])
            dk = np.array([e['dK_rel'] for e in s])
            dv = np.array([e['dV_rel'] for e in s])
            z['dH_%d' % typ] = {'mittel_abs': float(np.abs(dh).mean()), 'max_abs': float(np.abs(dh).max()),
                                'summe': float(dh.sum()), 'mittel_abs_dK': float(np.abs(dk).mean()),
                                'mittel_abs_dV': float(np.abs(dv).mean())}
    alle = [e['dH_rel'] for e in ev]
    if alle:
        z['dH_alle_mittel_abs'] = float(np.abs(alle).mean())
    z['A_nicht_pd_nach_zug'] = int(sum(1 for e in ev if not e['eig_nach']['A_pd']))
    z['wachsend_nach_zug_max'] = int(max([e['eig_nach']['n_wachsend'] for e in ev] + [0]))
    z['omega_max_dt_max'] = float(max([e['stabil_dt'] for e in ev] + [0.0]))
    if 'hm' in r:
        z['hm'] = {k: v for k, v in r['hm'].items() if k not in ('kontr_netze',)}
    if r.get('hm', {}).get('messformen'):
        m0 = r['hm']['mess0']
        mf = {}
        for f in m0:
            for typ in (23, 32):
                s = [e['abbildung']['messformen'][f] for e in ev if e['typ'] == typ and 'messformen' in e['abbildung']]
                if s:
                    d = np.array([b - a for a, b in s]) / abs(m0[f])
                    mf['%s_%d' % (f, typ)] = {'mittel_abs': float(np.abs(d).mean()), 'max_abs': float(np.abs(d).max()),
                                              'summe': float(d.sum()), 'n': int(len(d))}
        mf['K0'] = m0
        # Kontrolle: Messform A1R1 = Bewegungsenergie der Dynamik (dK_rel H0)
        kk = [abs((e['abbildung']['messformen']['A1R1'][1] - e['abbildung']['messformen']['A1R1'][0]) / r['H0'] - e['dK_rel'])
              for e in ev if 'messformen' in e['abbildung']]
        mf['kontr_A1R1_gegen_dK'] = float(max(kk + [0.0]))
        z['messarm'] = mf
    z['proben'] = pr[:, :2].tolist() if len(pr) else []
    return z


def urteile(res):
    u = {}
    # HM0
    for les, key in (('plan', 'fehler_norm_A2L'), ('wortlaut', 'fehler_norm_A2')):
        vals = [res['netze'][n]['hm0'][key] for n in NETZE if res['netze'].get(n) and 'hm0' in res['netze'][n]]
        n_ok = len(vals) == len(NETZE)
        u['HM0_' + les] = ('nicht entscheidbar' if not n_ok else ('eingetroffen' if max(vals) <= 1e-12 else 'verfehlt'))
        u['HM0_' + les + '_max'] = max(vals) if vals else None
    # HM1
    if res['netze'].get('V') and 'hm1' in res:
        u['HM1_plan'] = res['hm1']['urteil_plan']
        u['HM1_wortlaut'] = res['hm1']['urteil_wortlaut']
    # HM2
    sv = res['netze'].get('V', {}).get('spannen', {}) if res['netze'].get('V') else {}
    for les, v in (('plan', 'A2LRH'), ('wortlaut', 'A2RH')):
        s = sv.get(v)
        if not s:
            u['HM2_' + les] = 'nicht entscheidbar'
        elif not s['alle_ok'] or s['spanne_alle'] is None:
            u['HM2_' + les] = 'nicht entscheidbar'
        else:
            u['HM2_' + les] = 'eingetroffen' if s['spanne_alle'] < 1e-3 else 'verfehlt'
        u['HM2_' + les + '_spanne'] = s['spanne_alle'] if s else None
    # HM3
    gl = [res['netze'].get('glas-s%d' % i) for i in range(1, 5)]
    if all(gl):
        a1 = [g['spannen']['A1R1'] for g in gl]
        for les, v in (('plan', 'A2LRH'), ('wortlaut', 'A2RH')):
            ss = [g['spannen'][v] for g in gl]
            if not all(s['alle_ok'] and s['spanne_eps1'] is not None for s in ss):
                u['HM3_' + les] = 'nicht entscheidbar'
            else:
                m = float(np.mean([s['spanne_eps1'] for s in ss]))
                grenze = 0.5 * float(np.mean([s['spanne_eps1'] for s in a1])) if les == 'plan' else 0.0765
                u['HM3_' + les] = 'eingetroffen' if m <= grenze else 'verfehlt'
                u['HM3_' + les + '_mittel'] = m
                u['HM3_' + les + '_grenze'] = grenze
    else:
        u['HM3_plan'] = u['HM3_wortlaut'] = 'nicht entscheidbar'
    # HM4
    t = res['td']
    lw = [t.get('A2R1-s%d-b' % i) for i in range(1, 5)]
    lw = [x for x in lw if x]
    z23 = [x for x in lw if x.get('n_23', 0) > 0]
    if not z23:
        u['HM4_wortlaut'] = 'nicht entscheidbar'
    else:
        mx = max(x['dH_23']['max_abs'] for x in z23)
        u['HM4_wortlaut'] = 'eingetroffen' if mx < 1e-4 else 'verfehlt'
        u['HM4_wortlaut_max'] = mx
        u['HM4_wortlaut_mittel_je_lauf'] = [x['dH_23']['mittel_abs'] for x in z23]
        u['HM4_wortlaut_laeufe'] = len(lw)
    lp = [t.get('A2LR1-s%d-b' % i) for i in range(1, 5)]
    lp = [x for x in lp if x and x.get('n_23', 0) > 0]
    if not lp:
        u['HM4_plan'] = 'nicht entscheidbar'
    else:
        u['HM4_plan'] = 'eingetroffen' if all(x['dH_23']['mittel_abs'] < 1e-4 for x in lp) else 'verfehlt'
    return u


def tabellen(res):
    L = []
    L.append('### TT-Spanne je Netz und Paarung (Kristalle 52 Werte, Glas 26 Werte bei |k| = 1e-2; * = nicht alle Punkte ok)')
    L.append('')
    L.append('| Netz | ' + ' | '.join(TAB_VAR) + ' |')
    L.append('|---|' + '---|' * len(TAB_VAR))
    for n in NETZE:
        d = res['netze'].get(n)
        if not d:
            continue
        cells = []
        for v in TAB_VAR:
            s = d['spannen'][v]
            x = s['spanne_eps1'] if n.startswith('glas') else s['spanne_alle']
            cells.append(('%.3e' % x if x is not None else '-') + ('' if s['alle_ok'] else '*') +
                         (' (neg %d)' % s['n_neg_max'] if s['n_neg_max'] else ''))
        L.append('| %s | %s |' % (n, ' | '.join(cells)))
    L.append('')
    L.append('### Ritz-Spanne (projizierte affine TT-Wellen, beschreibend)')
    L.append('')
    L.append('| Netz | ' + ' | '.join(TAB_VAR) + ' |')
    L.append('|---|' + '---|' * len(TAB_VAR))
    for n in NETZE:
        d = res['netze'].get(n)
        if not d:
            continue
        cells = []
        for v in TAB_VAR:
            s = d['spannen'][v]
            x = s['ritz_spanne_eps1'] if n.startswith('glas') else s['ritz_spanne_alle']
            cells.append('%.3e' % x if x is not None else '-')
        L.append('| %s | %s |' % (n, ' | '.join(cells)))
    L.append('')
    return '\n'.join(L)


def bild(res, pfad):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
    farben = {'A1R1': '#1f77b4', 'A1RH': '#6baed6', 'A2R1': '#d62728', 'A2RH': '#fc9272', 'A2LR2': '#2ca02c',
              'A2LRH': '#74c476', 'A2LRHL': '#bcbddc', 'A2LR1': '#969696'}
    xs = np.arange(len(NETZE))
    for j, v in enumerate(TAB_VAR):
        ys, xv, mk = [], [], []
        for i, n in enumerate(NETZE):
            d = res['netze'].get(n)
            if not d:
                continue
            s = d['spannen'][v]
            y = s['spanne_eps1'] if n.startswith('glas') else s['spanne_alle']
            if y is None or y <= 0:
                continue
            ys.append(y)
            xv.append(i + (j - 3.5) * 0.09)
            mk.append(s['alle_ok'])
        ys, xv, mk = np.array(ys), np.array(xv), np.array(mk, bool)
        if len(ys):
            ax[0].scatter(xv[mk], ys[mk], color=farben[v], label=v, s=28, zorder=3)
            ax[0].scatter(xv[~mk], ys[~mk], facecolors='none', edgecolors=farben[v], s=28, zorder=3)
    ax[0].set_yscale('log')
    ax[0].axhline(1e-3, color='k', lw=0.6, ls=':')
    ax[0].set_xticks(xs)
    ax[0].set_xticklabels(NETZE, rotation=30)
    ax[0].set_ylabel('TT-Spanne max/min - 1 (offen: nicht alle Punkte regulaer)')
    ax[0].set_title('TT-Spanne je Netz und Paarung (J = 1, ohne Abstimmung)')
    ax[0].legend(fontsize=7, ncol=2)
    for nm, sty in (('A1 (TAKT-DYNAMIK-1)', '-'), ('A2R1', '--')):
        for i, c in zip(range(1, 4), ('#1f77b4', '#d62728', '#2ca02c')):
            key = ('td1-s%d-b' % i) if nm.startswith('A1') else ('A2R1-s%d-b' % i)
            z = res['td'].get(key)
            if not z or not z['proben']:
                continue
            p = np.array(z['proben'])
            ax[1].plot(p[:, 0] / z['T'], 100 * (p[:, 1] / z['H0'] - 1), sty, color=c, lw=1,
                       label='%s s%d (%d Zuege)' % (nm, i, z['n_zuege']))
    ax[1].set_xlabel('t / T')
    ax[1].set_ylabel('(H - H0) / H0 in %')
    ax[1].set_title('Umklapp-Aufbau (Glas N = 128, A = 1e-3, Lesart R): Energie ueber t')
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(pfad, dpi=130)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ordner', default='lauf')
    ap.add_argument('--td1', default='/home/fmh/fmhc-physics-remote/takt-dynamik-1/lauf')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'hm_sha256': sha(os.path.abspath(hm.__file__)),
                    'zeit_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, 'netze': {}, 'td': {}}
    for n in NETZE:
        d = netzdaten(a.ordner, n)
        if d is None:
            continue
        if n.startswith('glas'):
            da = lade(a.ordner + '/sp-%s-a.json' % n)['ergebnis']
            d['hm0'] = da.get('hm0')
            d['affin'] = da.get('affin')
        res['netze'][n] = {k: d[k] for k in ('spannen', 'hm0', 'affin', 'geo_kontr', 'E', 'T', 'nV', 'n_richtungen', 'dateien')
                           if k in d}
        # Reproduktion und Detailwerte
        rep = {}
        for (nn, v), ref in REF.items():
            if nn == n:
                s = d['spannen'][v]
                x = s['spanne_eps1'] if n.startswith('glas') else s['spanne_alle']
                rep[v] = {'neu': x, 'ref': ref, 'abw_abs_pp': abs(x - ref) * 100 if x is not None else None}
        res['netze'][n]['reproduktion'] = rep
        vert, tt, kontr = {}, {}, {}
        for z in d['zeilen']:
            p = z['eps1']
            if 'vertikal' in p:
                vert[z['richtung']] = p['vertikal']
            if z['richtung'] in ('100', '110', '111'):
                tt[z['richtung']] = {v: {'tt': p[v].get('tt_anteil'), 'n_neg': p[v]['n_neg'], 'luecke': p[v]['luecke']}
                                     for v in TAB_VAR if v in p}
            if 'kontr' in p:
                kontr[z['richtung']] = p['kontr']
        res['netze'][n]['vertikal'] = vert
        res['netze'][n]['tt3'] = tt
        res['netze'][n]['kontr'] = kontr
        if n == 'V':
            dv = lade(a.ordner + '/sp-V.json')['ergebnis']
            res['hm1'] = hm1_auswerten(dict(dv, zeilen=d['zeilen']))
    for p in sorted(glob.glob(a.ordner + '/td-*.json')):
        if p.endswith('.zustand.json'):
            continue
        key = os.path.basename(p)[3:-5]
        z = td_lauf(p)
        if z:
            res['td'][key] = z
    for i in range(1, 5):
        z = td_lauf(a.td1 + '/td-glas-N128-s%d-A1e-3-b.json' % i)
        if z:
            res['td']['td1-s%d-b' % i] = z
    res['urteile'] = urteile(res)
    tab = tabellen(res)
    with open(os.path.splitext(a.out)[0] + '-tabellen.md', 'w') as fh:
        fh.write(tab)
    try:
        bild(res, os.path.splitext(a.out)[0] + '-bild.png')
        res['bild'] = True
    except Exception as exc:  # Bild darf die Auswertung nicht abbrechen
        res['bild'] = repr(exc)
    for k in list(res['td']):
        res['td'][k].pop('proben', None)
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig auswertung', json.dumps(res['urteile']), flush=True)


if __name__ == '__main__':
    main()
