#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-FOLGE-1: Auswertung und Bild (beschreibend, keine Urteile). Liest lauf/uf-*.json (td.lauf-Ergebnisse mit
M_eff-Traegheit), schreibt auswertung.json, auswertung.md und bild-umklapp-folge.png."""
import argparse, glob, json, os
import numpy as np


def g3(x):
    if x is None:
        return '-'
    if isinstance(x, (bool, str)):
        return str(x)
    if x == 0:
        return '0'
    return '%.3g' % x


def lauf_lesen(p):
    d = json.load(open(p))
    e = d['ergebnis']
    P = np.array(e['proben'], float)
    H0 = float(e['H0'])
    T = float(e['T'])
    ev = [x for x in e['ereignisse']]
    aus = [x for x in ev if x.get('ausgefuehrt')]
    r = {'datei': os.path.basename(p), 'name': os.path.basename(p)[:-5], 'netz': e['netz'], 'arm': e['arm'],
         'lesart': e['lesart'], 'h': e['h'], 'fertig': bool(e['fertig']), 'abschnitt': e['abschnitt'], 'n': e['n'],
         'nges': e['nges'], 'NT': e['NT'], 'dt': e['dt'], 'T': T, 'omega_max': e['omega_max'],
         'omega': e['mode']['omega'], 'anteil_TT': e['mode']['anteil_TT_welle'], 'H0': H0, 'abbruch': e['abbruch'],
         't_ende_T': float(P[-1, 0] / T), 'skript': d['info']['skript_sha256']}
    rel = (P[:, 1] - H0) / H0
    r['drift_ende'] = float(rel[-1])
    r['drift_max'] = float(np.abs(rel).max())
    per = []
    for k in range(1, 11):
        i = int(np.argmin(np.abs(P[:, 0] - k * T)))
        if abs(P[i, 0] - k * T) <= 0.01 * T:
            per.append(float(rel[i]))
    r['drift_perioden'] = per
    r['n_zuege'] = len(aus)
    r['n_23'] = sum(1 for x in aus if x.get('typ') == 23)
    r['n_32'] = sum(1 for x in aus if x.get('typ') == 32)
    r['n_nicht'] = sum(1 for x in ev if not x.get('ausgefuehrt'))
    dH = np.array([x['dH_rel'] for x in aus], float)
    dK = np.array([x['dK_rel'] for x in aus], float)
    dV = np.array([x['dV_rel'] for x in aus], float)
    typ = np.array([x.get('typ') for x in aus])
    muhg = np.array([x.get('mu_hg', np.nan) for x in aus], float)
    mure = np.array([x.get('mu_rechts', np.nan) for x in aus], float)
    r['t_zuege_T'] = [float(x['t'] / T) for x in aus]
    r['dH_rel'] = dH.tolist()
    r['typ'] = typ.tolist()
    r['mu_hg'] = muhg.tolist()
    # Indefinite Netze: nach dem Zug eine wachsende Mode (A_red nicht positiv definit)
    indef = np.array([bool((x.get('eig_nach') or {}).get('n_wachsend', 0)) for x in aus], dtype=bool)
    vor_indef = np.concatenate([[False], indef[:-1]]).astype(bool) if len(aus) else indef
    regulaer = (~indef) & (~vor_indef)
    r['indef_nach'] = indef.tolist()
    r['n_zuege_indef_nach'] = int(indef.sum())
    r['n_zuege_regulaer'] = int(regulaer.sum())
    # Energiebilanz: Spruenge an Zuegen + Drift zwischen den Zuegen (Verlet), getrennt nach Netzart
    if len(aus):
        Hv = np.array([x['H_vor'] for x in aus], float)
        Hn = np.array([x['H_nach'] for x in aus], float)
        Hend = float(P[-1, 1])
        zw = np.concatenate([[Hv[0] - H0], Hv[1:] - Hn[:-1], [Hend - Hn[-1]]]) / H0
        zw_indef = np.concatenate([[False], indef])
        r['zwischen_summe_pd'] = float(zw[~zw_indef].sum())
        r['zwischen_summe_indef'] = float(zw[zw_indef].sum())
        r['spruenge_summe_regulaer'] = float(dH[regulaer].sum()) if regulaer.any() else 0.0
        r['spruenge_summe_indef'] = float(dH[~regulaer].sum()) if (~regulaer).any() else 0.0
        r['bilanz_rest'] = float((Hend - H0) / H0 - zw.sum() - dH.sum())
        if regulaer.any():
            dr = dH[regulaer]
            r['regulaer_n_pos'] = int((dr > 0).sum())
            r['regulaer_n_neg'] = int((dr < 0).sum())
            r['regulaer_mittel_abs'] = float(np.abs(dr).mean())
            r['regulaer_max_abs'] = float(np.abs(dr).max())
            ok = regulaer & np.isfinite(muhg) & (np.abs(muhg) > 0) & (np.abs(dH) > 0)
            if ok.sum() >= 3 and len(set(np.round(np.log10(np.abs(muhg[ok])), 3))) >= 2:
                sl, ic = np.polyfit(np.log10(np.abs(muhg[ok])), np.log10(np.abs(dH[ok])), 1)
                r['regulaer_steigung_dH_mu_hg'] = float(sl)
            r['regulaer_dH_durch_mu_hg_median'] = float(np.median(np.abs(dH[ok]) / np.abs(muhg[ok]))) if ok.any() else None
        r['_regulaer'] = regulaer
    if len(aus):
        r['summe_dH'] = float(dH.sum())
        r['summe_dK'] = float(dK.sum())
        r['summe_dV'] = float(dV.sum())
        r['max_abs_dV'] = float(np.abs(dV).max())
        r['mittel_abs_dH'] = float(np.abs(dH).mean())
        r['max_abs_dH'] = float(np.abs(dH).max())
        r['n_pos'] = int((dH > 0).sum())
        r['n_neg'] = int((dH < 0).sum())
        for t in (23, 32):
            m = typ == t
            if m.any():
                r['summe_dH_%d' % t] = float(dH[m].sum())
                r['n_pos_%d' % t] = int((dH[m] > 0).sum())
                r['n_neg_%d' % t] = int((dH[m] < 0).sum())
                r['median_abs_dH_%d' % t] = float(np.median(np.abs(dH[m])))
        ok = np.isfinite(muhg) & (np.abs(muhg) > 0) & (np.abs(dH) > 0)
        if ok.sum() >= 3:
            sl, ic = np.polyfit(np.log10(np.abs(muhg[ok])), np.log10(np.abs(dH[ok])), 1)
            r['steigung_dH_mu_hg'] = float(sl)
            r['dH_durch_mu_hg_median'] = float(np.median(np.abs(dH[ok]) / np.abs(muhg[ok])))
        r['mu_hg_median'] = float(np.nanmedian(np.abs(muhg)))
        r['mu_hg_bereich'] = [float(np.nanmin(muhg)), float(np.nanmax(muhg))]
        r['mu_rechts_max_abs'] = float(np.nanmax(np.abs(mure)))
        r['stabil_dt_max'] = float(max(x.get('stabil_dt', 0.0) for x in aus))
        r['nach_zug_verletzt_max'] = int(max(x.get('nach_zug_verletzt', 0) for x in aus))
    mz = e.get('meff_netze', [])
    if mz:
        r['meff'] = {'n_netze_abschnitt': len(mz), 'M_n_neg': sorted(set(x.get('M_n_neg') for x in mz)),
                     'M_n_null': sorted(set(x.get('M_n_null') for x in mz)),
                     'D0_n_neg': sorted(set(x.get('D0_n_neg') for x in mz)),
                     'D0_min_rel_min': float(min(x.get('D0_min_rel') for x in mz)),
                     'A_pd_alle': bool(all(x.get('A_pd') for x in mz)),
                     'n_wachsend_max': max((x.get('n_wachsend') or 0) for x in mz),
                     'r_V_max': float(max(x.get('r_V_gegen_B') for x in mz)),
                     'w2_max_max': float(max((x.get('w2_max') or 0.0) for x in mz)),
                     't_bau_median_s': float(np.median([x.get('t_bau_s') for x in mz]))}
    r['_P'] = P
    return r


def auswerten(ordner):
    R = [lauf_lesen(p) for p in sorted(glob.glob(os.path.join(ordner, 'uf-*.json'))) if '.zustand' not in p]
    ref = {(r['netz'], r['h']): r for r in R if r['arm'] == 'a'}
    for r in R:
        if r['arm'] != 'b':
            continue
        a = ref.get((r['netz'], r['h']))
        r['referenz'] = None
        if a is None:
            a = ref.get((r['netz'], 0.5))
        if a is None:
            continue
        r['referenz'] = a['name']
        Pa, Pb = a['_P'], r['_P']
        ta = Pa[:, 0]
        d = []
        for row in Pb:
            i = int(np.argmin(np.abs(ta - row[0])))
            if abs(ta[i] - row[0]) <= 1e-9 * max(r['T'], 1.0) or a['h'] != r['h']:
                d.append((row[0], (row[1] - Pa[i, 1]) / r['H0']))
        if d:
            d = np.array(d)
            r['b_minus_a_ende'] = float(d[-1, 1])
            r['b_minus_a_max'] = float(np.abs(d[:, 1]).max())
            r['_D'] = d
        pa, pb = a['drift_perioden'], r['drift_perioden']
        n = min(len(pa), len(pb))
        r['b_minus_a_perioden'] = [pb[k] - pa[k] for k in range(n)]
    return R


def bild(R, pfad):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))
    farbe = {'glas-N128-s1': 'C0', 'glas-N128-s2': 'C1', 'glas-N128-s3': 'C2', 'glas-N128-s4': 'C3'}
    # (0,0): Energie gegen Zeit, s1 bis s4, Arme a, b-P, b-R (h = 0,5)
    for r in R:
        if r['h'] != 0.5:
            continue
        P = r['_P']
        ls = {'a': ':', 'P': '-', 'R': '--'}[r['arm'] if r['arm'] == 'a' else r['lesart']]
        lab = '%s %s' % (r['netz'][-2:], 'a' if r['arm'] == 'a' else 'b-' + r['lesart'])
        ax[0, 0].plot(P[:, 0] / r['T'], (P[:, 1] - r['H0']) / r['H0'], ls, color=farbe.get(r['netz'], 'k'), lw=1, label=lab)
    ax[0, 0].set_xlabel('t / T')
    ax[0, 0].set_ylabel('(H - H0) / H0')
    ax[0, 0].set_yscale('symlog', linthresh=1e-6)
    ax[0, 0].set_title('Energie gegen Zeit, M_eff, h = 0,5 (a punktiert, b-P durchgezogen, b-R gestrichelt)', fontsize=9)
    ax[0, 0].legend(fontsize=7, ncol=3)
    # (0,1): b minus a gegen Zeit
    for r in R:
        if r['arm'] != 'b' or '_D' not in r:
            continue
        D = r['_D']
        ls = '-' if r['lesart'] == 'P' else '--'
        lw = 1.0 if r['h'] == 0.5 else 2.0
        ax[0, 1].plot(D[:, 0] / r['T'], D[:, 1], ls, color=farbe.get(r['netz'], 'k'), lw=lw,
                      label='%s b-%s h=%g' % (r['netz'][-2:], r['lesart'], r['h']))
    ax[0, 1].set_xlabel('t / T')
    ax[0, 1].set_ylabel('(H_b - H_a) / H0')
    ax[0, 1].set_yscale('symlog', linthresh=1e-8)
    ax[0, 1].set_title('Abweichung von der Referenz ohne Umklappen (dick: h = 0,25)', fontsize=9)
    ax[0, 1].legend(fontsize=7, ncol=2)
    # (1,0): kumulative Summe der Einzelspruenge gegen Zugzahl, nur regulaere Zuege (A_red vor und nach pd)
    for r in R:
        if r['arm'] != 'b' or not r['n_zuege'] or '_regulaer' not in r:
            continue
        dr = np.array(r['dH_rel'])[r['_regulaer']]
        if not len(dr):
            continue
        c = np.cumsum(dr)
        ls = '-' if r['lesart'] == 'P' else '--'
        lw = 1.0 if r['h'] == 0.5 else 2.0
        ax[1, 0].plot(np.arange(1, len(c) + 1), c, ls, color=farbe.get(r['netz'], 'k'), lw=lw,
                      label='%s b-%s h=%g' % (r['netz'][-2:], r['lesart'], r['h']))
    ax[1, 0].set_xlabel('Zahl der regulaeren Zuege')
    ax[1, 0].set_ylabel('Summe dH / H0')
    ax[1, 0].set_yscale('symlog', linthresh=1e-8)
    ax[1, 0].set_title('Kumulativer Sprung, nur Zuege zwischen Netzen mit positiv definitem A_red', fontsize=9)
    ax[1, 0].legend(fontsize=7, ncol=2)
    # (1,1): |dH| je Zug gegen |mu_hg|
    for r in R:
        if r['arm'] != 'b' or not r['n_zuege']:
            continue
        dH = np.abs(np.array(r['dH_rel']))
        mu = np.abs(np.array(r['mu_hg']))
        t = np.array(r['typ'])
        mk = 'o' if r['lesart'] == 'P' else 'x'
        for tt, fc in ((23, None), (32, 'none')):
            m = (t == tt) & (dH > 0) & (mu > 0)
            if m.any():
                ax[1, 1].scatter(mu[m], dH[m], s=10, marker=mk, color=farbe.get(r['netz'], 'k'),
                                 facecolors=fc if mk == 'o' else None, lw=0.6)
    ax[1, 1].set_xscale('log')
    ax[1, 1].set_yscale('log')
    ax[1, 1].set_xlabel('|mu| der Flaeche am Hintergrund')
    ax[1, 1].set_ylabel('|dH| / H0 je Zug')
    ax[1, 1].set_title('Sprung je Zug gegen Randabstand (o = P, x = R; gefuellt 2-3, leer 3-2)', fontsize=9)
    fig.tight_layout()
    fig.savefig(pfad + '.tmp.png', dpi=110)
    os.replace(pfad + '.tmp.png', pfad)


def markdown(R, pfad):
    L = ['# UMKLAPP-FOLGE-1: Auswertung (synthetisch, keine Messdaten)', '',
         '| Lauf | fertig (t/T) | Zuege 2-3/3-2 (nicht ausgef.) | davon nach Zug indefinit / regulaer | Drift Ende | Drift max | '
         'b - a Ende | b - a max | Summe dH (alle) | Summe dH regulaer | regulaer dH > 0 / < 0 | regulaer mittel / max abs dH | '
         'Zwischendrift pd / indefinit | Steigung lg dH / lg mu_hg (regulaer) | omega_max dt max |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in R:
        L.append('| %s | %s (%.2f) | %s (%s) | %s / %s | %s | %s | %s | %s | %s | %s | %s / %s | %s / %s | %s / %s | %s | %s |' % (
            r['name'], r['fertig'], r['t_ende_T'], '%d/%d' % (r['n_23'], r['n_32']), r['n_nicht'],
            r.get('n_zuege_indef_nach', '-'), r.get('n_zuege_regulaer', '-'), g3(r['drift_ende']),
            g3(r['drift_max']), g3(r.get('b_minus_a_ende')), g3(r.get('b_minus_a_max')), g3(r.get('summe_dH')),
            g3(r.get('spruenge_summe_regulaer')), r.get('regulaer_n_pos', '-'), r.get('regulaer_n_neg', '-'),
            g3(r.get('regulaer_mittel_abs')), g3(r.get('regulaer_max_abs')), g3(r.get('zwischen_summe_pd')),
            g3(r.get('zwischen_summe_indef')), g3(r.get('regulaer_steigung_dH_mu_hg')), g3(r.get('stabil_dt_max'))))
    L += ['', '## Je Lauf (JSON ohne Rohreihen)', '', '```']
    for r in R:
        L.append(json.dumps({k: v for k, v in r.items() if not k.startswith('_') and k not in ('dH_rel', 'typ', 'mu_hg',
                                                                                                't_zuege_T', 'indef_nach')}))
    L.append('```')
    with open(pfad + '.tmp', 'w') as fh:
        fh.write('\n'.join(L) + '\n')
    os.replace(pfad + '.tmp', pfad)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ordner', default='lauf')
    ap.add_argument('--out', required=True)
    ap.add_argument('--md', required=True)
    ap.add_argument('--bild', required=True)
    a = ap.parse_args()
    R = auswerten(a.ordner)
    def sauber(o):
        if isinstance(o, float):
            return o if np.isfinite(o) else None
        if isinstance(o, dict):
            return {k: sauber(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [sauber(v) for v in o]
        if isinstance(o, (np.floating,)):
            return sauber(float(o))
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, np.bool_):
            return bool(o)
        return o
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(sauber([{k: v for k, v in r.items() if not k.startswith('_')} for r in R]), fh, indent=1, default=str)
    os.replace(a.out + '.tmp', a.out)
    markdown(R, a.md)
    bild(R, a.bild)
    print('fertig auswertung', len(R), 'Laeufe', flush=True)


if __name__ == '__main__':
    main()
