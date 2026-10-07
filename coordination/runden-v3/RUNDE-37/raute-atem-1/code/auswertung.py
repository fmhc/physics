#!/usr/bin/env python3
"""RAUTE-ATEM-1, Auswertung (Urteilsregeln PLAN.md Abschn. 5, mechanisch). Laeuft auf der .69 ueber kleintest.sh.
Aufruf: auswertung.py --lauf <ordner> --aus <auswertung.json>
Erwartet im Ordner: haupt_d3_B*.json, haupt_d2_B*.json, kontrolle_d3.json, kontrolle_d2.json, statik.json
(je Lauf eine npz-Datei mit den Zeitreihen, Pfad im JSON)."""
import argparse
import glob
import json
import math
import os

import numpy as np

OMEGA = 2.0 * math.pi
DELTA_F = 0.02
G_AUF = 0.20
NAMEN = ['AB', 'AC', 'BC', 'AD', 'BD', 'CD']
AUSSEN = [1, 2, 3, 4]
I = [0, 0, 1, 0, 1, 2]
J = [1, 2, 2, 3, 3, 3]
B_WERTE = (0.03, 0.05, 0.08)
SAATEN = (1, 2, 3, 4)
TOL_WERKZEUG = 1.0e-6
FP_MIN_TAKTE = 10.0
THETA_GEFALTET = math.radians(125.0)


def wrap(a):
    return (a + np.pi) % (2.0 * np.pi) - np.pi


def kreismittel(z):
    return float(np.angle(np.mean(np.exp(1j * z))))


def ereignisse(t, gap_cd, dt_s):
    """Plan: zu bei Luecke < delta_f, auf bei Luecke >= G_AUF. Karte: auf, wenn die Bindung >= 1 Takt am Stueck geloest ist."""
    zu = False
    zu_plan = np.zeros(len(t), dtype=bool)
    sch_p, auf_p = [], []
    for n in range(len(t)):
        g = gap_cd[n]
        if not zu and g < DELTA_F:
            zu = True
            sch_p.append(float(t[n]))
        elif zu and g >= G_AUF:
            zu = False
            auf_p.append(float(t[n]))
        zu_plan[n] = zu
    zu = False
    los = None
    sch_k, auf_k = [], []
    for n in range(len(t)):
        g = gap_cd[n]
        if not zu:
            if g < DELTA_F:
                zu = True
                sch_k.append(float(t[n]))
                los = None
        else:
            if g >= DELTA_F:
                if los is None:
                    los = float(t[n])
                if t[n] - los >= 1.0 - 1e-9:
                    zu = False
                    auf_k.append(los)
                    los = None
            else:
                los = None
    return zu_plan, sch_p, auf_p, sch_k, auf_k


def lauf_metriken(r):
    d = np.load(r['npz'])
    t = d['t']
    th = d['theta']
    gap = d['gap']
    tb = d['tb']
    fm = d['fm']
    phi = d['phi']
    cd = d['cd']
    dt_s = float(t[1] - t[0])
    dl = np.stack([wrap(phi[:, I[b]] - phi[:, J[b]]) for b in range(6)], axis=1)
    m = {'dim': r['dim'], 'B': r['B'], 'seed': r['seed'], 'takte': r['takte'], 'werkzeugprobe': r['werkzeugprobe'],
         'theta0_grad': math.degrees(th[0])}
    w200 = t <= 200.0 + 1e-9
    m['max_dtheta_200_grad'] = float(np.degrees(np.abs(th[w200] - th[0]).max()))
    m['max_dtheta_alle_grad'] = float(np.degrees(np.abs(th - th[0]).max()))
    m['theta_min_grad'] = float(np.degrees(th.min()))
    m['theta_ende_grad'] = float(np.degrees(th[-1]))
    letzte = t >= t[-1] - 10.0 - 1e-9
    m['dphi_ende'] = {NAMEN[b]: kreismittel(dl[letzte, b]) for b in range(6)}
    zu_plan, sch_p, auf_p, sch_k, auf_k = ereignisse(t, gap[:, 5], dt_s)
    m['schliessen_plan'] = sch_p
    m['oeffnen_plan'] = auf_p
    m['schliessen_karte'] = sch_k
    m['oeffnen_karte'] = auf_k
    m['t_erstes_schliessen'] = sch_p[0] if sch_p else None
    m['n_oeffnen_plan'] = len([x for x in auf_p if x <= 500.0 + 1e-9])
    m['n_oeffnen_karte'] = len([x for x in auf_k if x <= 500.0 + 1e-9])
    m['zyklus_takte_plan'] = float(np.mean(np.diff(sch_p))) if len(sch_p) >= 2 else None
    m['anteil_zu_plan'] = float(zu_plan.mean())
    # Umordnung: |Delta_CD| > pi/2 in einem Zu-Abschnitt (Plan) nach dem ersten Schliessen
    if zu_plan.any():
        dcd = np.abs(dl[zu_plan, 5])
        m['max_abs_dphi_CD_zu'] = float(dcd.max())
        um = np.nonzero(zu_plan & (np.abs(dl[:, 5]) > math.pi / 2))[0]
        m['umordnung'] = bool(len(um) > 0)
        m['t_umordnung'] = float(t[um[0]]) if len(um) else None
    else:
        m['max_abs_dphi_CD_zu'] = None
        m['umordnung'] = False
        m['t_umordnung'] = None
    m['RA2_lauf_plan'] = bool(m['umordnung'] and m['n_oeffnen_plan'] >= 2)
    m['RA2_lauf_karte'] = bool(m['umordnung'] and m['n_oeffnen_karte'] >= 2)
    # FP-Fenster: Zu-Zustand (Plan); sonst gefaltet (theta <= 125 Grad); sonst nicht auswertbar
    fenster = None
    if zu_plan.sum() * dt_s >= FP_MIN_TAKTE:
        w, fenster = zu_plan, 'zu'
    elif (th <= THETA_GEFALTET).sum() * dt_s >= FP_MIN_TAKTE:
        w, fenster = th <= THETA_GEFALTET, 'gefaltet'
    m['fp_fenster'] = fenster
    if fenster is not None:
        mt = tb[w].mean(axis=0)
        m['fp_dauer_takte'] = float(w.sum() * dt_s)
        m['stab_mittel'] = dict(zip(NAMEN, mt.tolist()))
        m['stab_betrag_mittel'] = dict(zip(NAMEN, np.abs(tb[w]).mean(axis=0).tolist()))
        m['stab_wechsel_amp'] = dict(zip(NAMEN, (math.sqrt(2.0) * tb[w].std(axis=0)).tolist()))
        m['medium_mittel'] = dict(zip(NAMEN, fm[w].mean(axis=0).tolist()))
        m['cd_anteil_gebunden'] = float(cd[w].mean())
        m['dphi_fenster'] = {NAMEN[b]: kreismittel(dl[w, b]) for b in range(6)}
        m['fp_lauf'] = fp_regel(mt, m['cd_anteil_gebunden'] >= 0.5)
    else:
        m['fp_lauf'] = None
    # 2D und allgemein: zweite Haelfte (t >= 250) fuer Stabkraefte und C-D-Abstand
    h2 = t >= t[-1] / 2.0
    m['zweite_haelfte'] = {'stab_mittel': dict(zip(NAMEN, tb[h2].mean(axis=0).tolist())),
                           'stab_wechsel_amp': dict(zip(NAMEN, (math.sqrt(2.0) * tb[h2].std(axis=0)).tolist())),
                           'r_CD_mittel': float(d['r'][h2, 5].mean()),
                           'theta_mittel_grad': float(np.degrees(th[h2].mean())),
                           'dphi': {NAMEN[b]: kreismittel(dl[h2, b]) for b in range(6)}}
    return m


def fp_regel(mt, cd_da):
    a = np.abs(mt)
    da = [0, 1, 2, 3, 4] + ([5] if cd_da else [])
    ab_groesste = all(a[0] > a[e] for e in da if e != 0)
    aussen_kleinste = (max(a[e] for e in AUSSEN) < a[5]) if cd_da else True
    return bool(ab_groesste and aussen_kleinste)


def werkzeug_ok(pr):
    return (pr['max_int_vs_schleife'] < TOL_WERKZEUG and pr['max_schleife_vs_fd'] < TOL_WERKZEUG
            and pr['max_impuls_summe'] < TOL_WERKZEUG and pr['n'] > 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--aus', required=True)
    a = ap.parse_args()
    out = {'fehlend': [], 'laeufe': {}, 'urteile': {}, 'vermerke': {}}

    def lade(name):
        p = os.path.join(a.lauf, name)
        if not os.path.exists(p):
            out['fehlend'].append(name)
            return None
        with open(p) as f:
            return json.load(f)

    haupt = {}
    for dim in (3, 2):
        for B in B_WERTE:
            js = lade(f'haupt_d{dim}_B{B:.2f}.json')
            if js is None:
                continue
            for r in js['laeufe']:
                haupt[(dim, B, r['seed'])] = lauf_metriken(r)
    kontr = {}
    for dim in (3, 2):
        js = lade(f'kontrolle_d{dim}.json')
        if js is None:
            continue
        for r in js['laeufe']:
            kontr[(dim, r['seed'])] = lauf_metriken(r)
    st = lade('statik.json')
    for k, v in haupt.items():
        out['laeufe'][f'haupt_d{k[0]}_B{k[1]:.2f}_s{k[2]}'] = v
    for k, v in kontr.items():
        out['laeufe'][f'kontrolle_d{k[0]}_s{k[1]}'] = v
    if st is not None:
        out['statik'] = st['laeufe']
    vollst = (len(haupt) == 24 and len(kontr) == 8 and st is not None)
    out['vollstaendig'] = vollst

    # ---------------- RA0
    def phasen_ok(m):
        dp = m['dphi_ende']
        return all(abs(abs(dp[n]) - 2 * math.pi / 3) < 0.1 for n in NAMEN[:5]) and abs(dp['CD']) < 0.1

    alle_pr = [m['werkzeugprobe'] for m in list(haupt.values()) + list(kontr.values())]
    if st is not None:
        alle_pr += [r['werkzeugprobe'] for r in st['laeufe']]
    werk = all(werkzeug_ok(p) for p in alle_pr) if alle_pr else False
    out['vermerke']['werkzeugprobe_max'] = {
        'int_vs_schleife': max(p['max_int_vs_schleife'] for p in alle_pr),
        'schleife_vs_fd': max(p['max_schleife_vs_fd'] for p in alle_pr),
        'impuls_summe': max(p['max_impuls_summe'] for p in alle_pr),
        'proben': sum(p['n'] for p in alle_pr), 'ausgelassen_fangkante': sum(p['n_ausgelassen'] for p in alle_pr)}
    statik_ok = False
    if st is not None:
        s3 = [r for r in st['laeufe'] if r['dim'] == 3 and r['eps'] == 0.0]
        s2 = [r for r in st['laeufe'] if r['dim'] == 2 and r['eps'] == 0.0]
        statik_ok = (all(r['max_abw_stab_gleich_minus_paar'] < TOL_WERKZEUG and r['max_restkraft_ende'] < TOL_WERKZEUG
                         for r in s3)
                     and all(r['max_abw_stab_gegen_gleichgewicht'] < TOL_WERKZEUG and
                             r['max_restkraft_ende'] < TOL_WERKZEUG for r in s2) and len(s3) == 3 and len(s2) == 3)
    k3 = [kontr[(3, s)] for s in SAATEN if (3, s) in kontr]
    k2 = [kontr[(2, s)] for s in SAATEN if (2, s) in kontr]
    ph3 = all(phasen_ok(m) for m in k3) and len(k3) == 4
    ph2 = all(phasen_ok(m) for m in k2) and len(k2) == 4
    falt = all(m['max_dtheta_200_grad'] < 5.0 for m in k3) and len(k3) == 4
    out['vermerke']['RA0_teile'] = {'phasen_3d': ph3, 'phasen_2d': ph2, 'kein_falten_3d_200': falt,
                                    'werkzeugprobe': werk, 'statik': statik_ok}
    if not vollst:
        out['urteile']['RA0'] = {'plan': 'nicht auswertbar', 'karte': 'nicht auswertbar'}
    else:
        out['urteile']['RA0'] = {
            'plan': 'eingetroffen' if (ph3 and ph2 and falt and werk and statik_ok) else 'nicht eingetroffen',
            'karte': 'eingetroffen' if (ph3 and falt and werk) else 'nicht eingetroffen'}

    # ---------------- RA1
    h3 = {k: v for k, v in haupt.items() if k[0] == 3}
    zu200 = {k: (v['t_erstes_schliessen'] is not None and v['t_erstes_schliessen'] <= 200.0 + 1e-9)
             for k, v in h3.items()}
    je_B = {B: sum(zu200.get((3, B, s), False) for s in SAATEN) for B in B_WERTE}
    out['vermerke']['RA1_je_B_geschlossen_200'] = {f'{B:.2f}': n for B, n in je_B.items()}
    if len(h3) != 12:
        out['urteile']['RA1'] = {'plan': 'nicht auswertbar', 'karte': 'nicht auswertbar'}
    else:
        out['urteile']['RA1'] = {'plan': 'eingetroffen' if all(zu200.values()) else 'nicht eingetroffen',
                                 'karte': 'eingetroffen' if all(n >= 3 for n in je_B.values()) else 'nicht eingetroffen'}

    # ---------------- RA2
    ra2p = {B: sum(h3[(3, B, s)]['RA2_lauf_plan'] for s in SAATEN if (3, B, s) in h3) for B in B_WERTE}
    ra2k = {B: sum(h3[(3, B, s)]['RA2_lauf_karte'] for s in SAATEN if (3, B, s) in h3) for B in B_WERTE}
    out['vermerke']['RA2_je_B'] = {f'{B:.2f}': {'plan': ra2p[B], 'karte': ra2k[B]} for B in B_WERTE}
    if len(h3) != 12:
        out['urteile']['RA2'] = {'plan': 'nicht auswertbar', 'karte': 'nicht auswertbar'}
    else:
        out['urteile']['RA2'] = {'plan': 'eingetroffen' if any(n >= 3 for n in ra2p.values()) else 'nicht eingetroffen',
                                 'karte': 'eingetroffen' if any(n >= 3 for n in ra2k.values()) else 'nicht eingetroffen'}

    # ---------------- FP
    ausw = [v for v in h3.values() if v['fp_lauf'] is not None]
    n_ja = sum(v['fp_lauf'] for v in ausw)
    out['vermerke']['FP_laeufe'] = {'auswertbar': len(ausw), 'ja': n_ja,
                                    'fenster': {f"B{v['B']:.2f}_s{v['seed']}": v['fp_fenster'] for v in h3.values()}}
    if len(ausw) < 8:
        fp_plan = 'nicht auswertbar'
    else:
        fp_plan = 'eingetroffen' if n_ja >= 0.75 * len(ausw) else 'nicht eingetroffen'
    if ausw:
        gew = np.array([v['fp_dauer_takte'] for v in ausw])
        M = np.array([[v['stab_mittel'][n] / v['B'] for n in NAMEN] for v in ausw])
        Mp = (gew[:, None] * M).sum(axis=0) / gew.sum()
        cdp = float((gew * np.array([v['cd_anteil_gebunden'] for v in ausw])).sum() / gew.sum())
        fp_karte = 'eingetroffen' if fp_regel(Mp, cdp >= 0.5) else 'nicht eingetroffen'
        out['vermerke']['FP_gepoolt_durch_B'] = {'stab_mittel_durch_B': dict(zip(NAMEN, Mp.tolist())),
                                                 'cd_anteil_gebunden': cdp}
    else:
        fp_karte = 'nicht auswertbar'
    out['urteile']['FP'] = {'plan': fp_plan, 'karte': fp_karte}

    # ---------------- Vermerke 2D und Stabkraefte je B
    for dim in (3, 2):
        for B in B_WERTE:
            ls = [haupt[(dim, B, s)] for s in SAATEN if (dim, B, s) in haupt]
            if not ls:
                continue
            zh = {n: float(np.mean([m['zweite_haelfte']['stab_mittel'][n] for m in ls])) for n in NAMEN}
            za = {n: float(np.mean([m['zweite_haelfte']['stab_wechsel_amp'][n] for m in ls])) for n in NAMEN}
            out['vermerke'][f'd{dim}_B{B:.2f}_zweite_haelfte'] = {
                'stab_mittel_saatenmittel': zh, 'stab_wechsel_amp_saatenmittel': za,
                'r_CD_mittel': [m['zweite_haelfte']['r_CD_mittel'] for m in ls],
                'theta_mittel_grad': [m['zweite_haelfte']['theta_mittel_grad'] for m in ls],
                'dphi_CD': [m['zweite_haelfte']['dphi']['CD'] for m in ls]}
    with open(a.aus, 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out['urteile'], indent=1))
    print(json.dumps({k: v for k, v in out['vermerke'].items() if k.startswith('RA') or k.startswith('FP') or
                      k.startswith('werk')}, indent=1))


if __name__ == '__main__':
    main()
