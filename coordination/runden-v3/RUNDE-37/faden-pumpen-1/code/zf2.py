#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FADEN-PUMPEN-1: Zusammenfassung aller Laeufe (nur Lesen der JSON in lauf/, Schreiben von lauf/zusammenfassung.json).
Aufruf nur ueber kleintest.sh auf der .69:  python zf.py lauf lauf/zusammenfassung.json
"""
import json, os, sys, math, glob, time
import numpy as np


def lade(p):
    try:
        with open(p) as fh:
            return json.load(fh)
    except Exception:
        return None


def fit_c2(ks, w2):
    """Omega^2 = a + c2 k^2, kleinste Quadrate."""
    ks, w2 = np.asarray(ks), np.asarray(w2)
    A = np.stack([np.ones_like(ks), ks ** 2], -1)
    (a, c2), *_ = np.linalg.lstsq(A, w2, rcond=None)
    return float(a), float(c2)


def q_lauf(d):
    om = d['stationaer']['om_gitter']
    sp = d['spektren']
    out = {'geo': d['geo'], 'h': d['h'], 'durchmesser_kanten': d['durchmesser_kanten'],
           'durchmesser_kanten_gitter': 2 * d['stationaer']['r_halb'] / d['h'], 'om_gitter': om,
           'schwelle_rot': 1 - om, 'periode': d['periode'], 'k_bz_rand': d['k_bz_rand'], 'k_c': d.get('k_c'),
           'rest_rel': d['stationaer']['rest_rel'], 'E_durch_q': d['stationaer']['E_je_Laenge'] / d['stationaer']['q_je_Laenge']}
    g = [(s['k'], s['gamma']) for s in sp]
    gm = max(g, key=lambda x: x[1]) if g else (None, 0.0)
    out['gamma_max'], out['k_max'] = gm[1], gm[0]
    out['instabil_bis_bz_rand'] = bool(sp and sp[-1]['gamma'] > 1e-6)
    # Ladungsform: Mode mit kleinstem |lambda| bei kleinstem k > 0
    kl = [s for s in sp if 0 < s['k'] <= 0.0101]
    if kl:
        s = kl[0]
        m = min(s['moden'], key=lambda x: abs(complex(x['re'], x['im'])))
        out['ladung_k'] = s['k']
        out['ladung_re_durch_k'] = m['re'] / s['k']
        out['ladung_im_durch_k'] = m['im'] / s['k']
        out['ladung_betrag_anteil'] = m['betrag_anteil']
    # Biegen: kleinste Frequenz mit n_dominant == 1 (rein oszillierend)

    def biege(s):
        c = [x for x in s['moden'] if x['n_dominant'] == 1 and abs(x['re']) < 1e-6 and x['im'] > 1e-7]
        return min(c, key=lambda x: x['im']) if c else None
    b0 = [biege(s) for s in sp]
    ks = [s['k'] for s, b in zip(sp, b0) if b is not None and s['k'] <= 0.1001]
    w2 = [b['im'] ** 2 for s, b in zip(sp, b0) if b is not None and s['k'] <= 0.1001]
    if len(ks) >= 3:
        a, c2 = fit_c2(ks, w2)
        out['biege_luecke'] = math.sqrt(max(a, 0.0))
        out['biege_luecke2'] = a
        out['biege_c2_fit'] = c2
        out['biege_omega_k'] = [[k, math.sqrt(w)] for k, w in zip(ks, w2)]
    # Oval (n = 2) bei k = 0
    s0 = [s for s in sp if s['k'] == 0.0]
    if s0:
        c = [x for x in s0[0]['moden'] if x['n_dominant'] == 2 and x['im'] > 1e-7]
        if c:
            m = min(c, key=lambda x: x['im'])
            out['oval_omega_k0'] = m['im']
            out['oval_r_schwer'] = m['r_schwer']
            out['oval_unter_schwelle'] = bool(m['im'] < 1 - om)
        c = [x for x in s0[0]['moden'] if x['n_dominant'] == 0 and x['im'] > 1e-4]
        if c:
            m = min(c, key=lambda x: x['im'])
            out['pump_intern_omega_k0'] = m['im']
            out['pump_intern_unter_schwelle'] = bool(m['im'] < 1 - om)
    return out


def w_lauf(d, ref):
    sp = d['spektren']
    out = {'geo': d['geo'], 'h': d['h'], 'durchmesser_kanten': d['durchmesser_kanten'], 'R_D': d['R_D'],
           'periode': d['periode'], 'k_bz_rand': d['k_bz_rand'], 'rest_rel': d['stationaer']['rest_rel']}

    def wahl(s, art):
        if art == 'biege':
            c = [x for x in s['moden'] if x['n_dominant'] == 1]
        elif art == 'pump':
            c = [x for x in s['moden'] if x['n_dominant'] == 0 and x['betrag_anteil'] > 0.5]
        else:
            c = [x for x in s['moden'] if x['n_dominant'] == 2 and x['betrag_anteil'] > 0.3]
        return min(c, key=lambda x: x['omega2']) if c else None
    for art in ('biege', 'pump', 'oval'):
        ws = [(s['k'], wahl(s, art)) for s in sp]
        ws = [(k, m) for k, m in ws if m is not None]
        if not ws:
            continue
        k0 = [m for k, m in ws if k == 0.0]
        if k0:
            out[art + '_omega2_k0'] = k0[0]['omega2']
            out[art + '_betrag_anteil_k0'] = k0[0]['betrag_anteil']
        kl = [(k, m['omega2']) for k, m in ws if k <= 0.1001]
        if len(kl) >= 3:
            a, c2 = fit_c2([x[0] for x in kl], [x[1] for x in kl])
            out[art + '_c2_fit_k_bis_0.1'] = c2
            out[art + '_a_fit'] = a
        kg = [(k, m['omega2']) for k, m in ws if 0.2 <= k <= 0.5001]
        if k0 and kg:
            out[art + '_c2_bei_k'] = [[k, (w - k0[0]['omega2']) / k ** 2] for k, w in kg]
    return out


def zeit_lauf(d, radq):
    out = {'geo': d['geo'], 'om_kont': d['om_kont'], 'om_gitter': d['om_gitter'], 'h': d['h'], 'laenge': d['laenge'],
           'eps': d['eps'], 'E_drift_rel': d['E_drift_rel'], 'Q_drift_rel': d['Q_drift_rel'], 'abbruch': d['abbruch']}
    ms = d['messungen']
    t = np.array([m['t'] for m in ms])
    F = np.array([m['fourier_1_12'] for m in ms])
    L = d['laenge']
    # Linearer Abschnitt: Mode mit groesstem Endwert vor der Saettigung (max/mittel < 1.5)
    lin = np.array([m['Q_scheibe_max_durch_mittel'] for m in ms]) < 1.2
    jdom = int(np.argmax(F[lin][-1])) if lin.any() else int(np.argmax(F[-1]))
    out['dominante_mode_j'] = jdom + 1
    out['k_dominant'] = 2 * math.pi * (jdom + 1) / L
    sel = lin & (F[:, jdom] > 3 * F[0, jdom])
    if sel.sum() >= 3:
        p = np.polyfit(t[sel], np.log(F[sel, jdom]), 1)
        out['wachstum_fit'] = float(p[0])
        out['wachstum_fit_fenster'] = [float(t[sel][0]), float(t[sel][-1])]
    out['perlen_verlauf'] = [[p['t'], p['perlen']] for p in d['perlen']]
    out['perlen_ende'] = d['perlen'][-1]['perlen']
    out['perlen_je_laenge_ende'] = d['perlen'][-1]['perlen'] / L
    out['max_durch_mittel_ende'] = ms[-1]['Q_scheibe_max_durch_mittel']
    out['t_ende'] = float(t[-1])
    # Kontinuums-Erwartung (rad-q.json): gamma(k) am naechsten om
    if radq:
        fam = min(radq['familie'], key=lambda e: abs(e['kenn']['om'] - d['om_kont']))
        z0 = fam['n']['0']
        kk = np.array([z['k'] for z in z0])
        gg = np.array([z['gamma'] for z in z0])
        out['kont_k_max'] = fam['auswertung']['k_max']
        out['kont_gamma_max'] = fam['auswertung']['gamma_max']
        out['kont_L_durch_lambda_max'] = L * fam['auswertung']['k_max'] / (2 * math.pi)
        out['kont_gamma_bei_k_dominant'] = float(np.interp(out['k_dominant'], kk, gg))
    return out


def main():
    d0, aus = sys.argv[1], sys.argv[2]
    radq = lade(os.path.join(d0, 'rad-q.json'))
    res = {'erzeugt_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'q': [], 'w': [], 'zeit': []}
    for p in sorted(glob.glob(os.path.join(d0, 'q-*.json'))):
        d = lade(p)
        if d and d.get('spektren'):
            e = q_lauf(d)
            e['datei'] = os.path.basename(p)
            res['q'].append(e)
    ref = lade(os.path.join(d0, 'rad-w12.json'))
    if ref:
        res['w_kontinuum_rmax'] = [{'rmax': l['rmax'], 'biege_omega2': l['n']['1']['block'][0]['omega2'],
                                    'pump_omega2': l['n']['0']['betrag'][0]['omega2'],
                                    'oval_omega2_niedrigste': l['n']['2']['block'][0]['omega2']} for l in ref['laeufe']]
    for p in sorted(glob.glob(os.path.join(d0, 'w-*.json'))):
        d = lade(p)
        if d and d.get('spektren'):
            e = w_lauf(d, ref)
            e['datei'] = os.path.basename(p)
            res['w'].append(e)
    for p in sorted(glob.glob(os.path.join(d0, 'zeit-*.json'))):
        d = lade(p)
        if d:
            e = zeit_lauf(d, radq)
            e['datei'] = os.path.basename(p)
            res['zeit'].append(e)
    with open(aus + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1)
    os.replace(aus + '.tmp', aus)
    print(json.dumps(res, indent=1)[:20000])


if __name__ == "__main__" and len(sys.argv) <= 3:
    main()


def rad_tabelle(radq):
    """Kontinuum: c_b aus Omega^2(k) - Omega^2(0) bei k = 0,01 und 0,02 (Gitterluecke des Radialgitters abgezogen)."""
    out = []
    for e in radq['familie']:
        kk, a = e['kenn'], e['auswertung']
        z1 = {z['k']: (z['omega_rot'][0] if z['omega_rot'] else None) for z in e['n']['1']}
        w0 = z1.get(0.0) or 0.0
        cb = {}
        for k in (0.01, 0.02, 0.05):
            if z1.get(k):
                cb[str(k)] = math.sqrt(max(z1[k] ** 2 - w0 ** 2, 0.0)) / k
        out.append({'om': kk['om'], 'q': kk['q'], 'E_durch_q': kk['mu_E_je_Laenge'] / kk['q'], 'r_halb': kk['r_halb'],
                    'r_wand': kk['r_wand'], 'gamma_durch_k_0.005': a['gamma_durch_k_klein'][0],
                    'cs_erwartet': a['cs_betrag_erwartet'], 'k_c': a['k_c'], 'kc_r_wand': a['kc_r_wand'],
                    'kc_r_halb': a['kc_r_halb'], 'gamma_max': a['gamma_max'], 'k_max': a['k_max'],
                    'kmax_r_wand': a['k_max'] * kk['r_wand'], 'cb_fit': cb, 'cb_erwartet': a['cb_erwartet'],
                    'biege_luecke_radialgitter': w0, 'schwelle': a['schwelle_kontinuum_rot']})
    return out


if __name__ == '__main__' and len(sys.argv) > 3:
    r = lade(sys.argv[3])
    t = rad_tabelle(r)
    with open(sys.argv[4] + '.tmp', 'w') as fh:
        json.dump(t, fh, indent=1)
    os.replace(sys.argv[4] + '.tmp', sys.argv[4])
    print(json.dumps(t, indent=1))
