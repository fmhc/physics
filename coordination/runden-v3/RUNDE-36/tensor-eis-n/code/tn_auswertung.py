#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TENSOR-EIS-N, Auswertung nach PLAN.md (Urteilsregeln Abschnitt 6), Bilder.

Aufruf (auf der .69, im Ordner runde36-tensorn):
  tn_auswertung.py --lauf lauf --out lauf/auswertung.json
Liest lauf/statik-64.json/.npz, lauf/statik-128-192.json/.npz, lauf/statik-256.json/.npz, lauf/spektrum.json,
lauf/kontrolle.json.
"""
import argparse, json, os, sys, time, hashlib
import numpy as np

DATEIEN, LKORR, LALT, LALLE = None, None, None, None
TOL_NULL = 1e-12        # |U| darunter: keine Wechselwirkung (Einheiten g m^2)
TOL_REL = 1e-9          # Definitheit relativ
TAU = 1e-6              # exponentielles Wachstum, relativ zu |A| |B|
FENSTER = (4.0, 16.0)
STRAHLEN = {'100': [(n, 0, 0) for n in range(1, 17)],
            '110': [(n, n, 0) for n in range(1, 12)],
            '111': [(n, n, n) for n in range(1, 10)]}


def lade(lauf):
    U = {}
    info = {}
    for name in DATEIEN:
        with open(os.path.join(lauf, name + '.json')) as f:
            js = json.load(f)
        info[name] = js
        z = np.load(os.path.join(lauf, name + '.npz'))
        for k in z.files:
            typ, L = k.split('_L')
            U[(typ, int(L))] = z[k]
    return U, info


def korrigiert(U, typ, Ls):
    """Exakte Loesung von U_L = a + b/L + c/L^3 an drei Groessen, je Gitterpunkt des Oktanten."""
    M = np.array([[1.0, 1.0 / L, 1.0 / L ** 3] for L in Ls])
    Y = np.stack([U[(typ, L)] for L in Ls], 0)
    sh = Y.shape[1:]
    coef = np.linalg.solve(M, Y.reshape(3, -1))
    return coef[0].reshape(sh), coef[1].reshape(sh), coef[2].reshape(sh)


def steigung(rs, us):
    rs, us = np.asarray(rs), np.asarray(us)
    p = np.polyfit(np.log(rs), np.log(np.abs(us)), 1)
    return float(-p[0])


def schale(W, lo, hi):
    n = W.shape[0]
    x, y, z = np.meshgrid(np.arange(n), np.arange(n), np.arange(n), indexing='ij')
    r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    m = (r >= lo) & (r <= hi)
    return r[m], W[m]


def strahl(W, nm, lo=None, hi=None):
    rs, us = [], []
    for v in STRAHLEN[nm]:
        r = float(np.linalg.norm(v))
        if (lo is not None and r < lo - 1e-9) or (hi is not None and r > hi + 1e-9):
            continue
        rs.append(r)
        us.append(float(W[v]))
    return np.array(rs), np.array(us)


def urteil_statik(Ukorr, typ):
    """N0 (L-Typ, Abstossung, Kraftexponent 4 +- 0,4) bzw. N1 (N-Typ, Anziehung, Exponent 1 +- 0,1)."""
    r_all, u_all = schale(Ukorr, 2.0, 16.0)
    w = {'max_abs_U_2_16': float(np.abs(u_all).max()), 'min_U_2_16': float(u_all.min()), 'max_U_2_16': float(u_all.max())}
    if w['max_abs_U_2_16'] < TOL_NULL:
        w['befund'] = 'keine Wechselwirkung (|U| < %g fuer alle 2 <= r <= 16)' % TOL_NULL
        return 'nicht eingetroffen', w
    exps = {}
    kraft = {}
    for nm in STRAHLEN:
        rs, us = strahl(Ukorr, nm, *FENSTER)
        exps[nm] = steigung(rs, us)
        rr, uu = strahl(Ukorr, nm, 2.0, 16.0)
        dU = np.diff(uu)
        kraft[nm] = {'alle_dU_pos': bool((dU > 0).all()), 'alle_dU_neg': bool((dU < 0).all())}
    rs, us = schale(Ukorr, *FENSTER)
    exps['schale'] = steigung(rs, us)
    w['exponent_U'] = exps
    w['kraft'] = kraft
    if typ == 'N':
        anz = bool((u_all < 0).all())
        anz_k = all(kraft[nm]['alle_dU_pos'] for nm in STRAHLEN)
        ex_ok = all(0.9 <= exps[k] <= 1.1 for k in exps)
        w['regel'] = {'U<0 alle': anz, 'Kraft anziehend Strahlen': anz_k, 'Exponent in [0,9; 1,1]': ex_ok}
        return ('eingetroffen' if (anz and anz_k and ex_ok) else 'nicht eingetroffen'), w
    abst = bool((u_all > 0).all())
    abst_k = all(kraft[nm]['alle_dU_neg'] for nm in STRAHLEN)
    pf = {k: v + 1.0 for k, v in exps.items()}
    w['exponent_Kraft'] = pf
    ex_ok = all(3.6 <= pf[k] <= 4.4 for k in pf)
    w['regel'] = {'U>0 alle': abst, 'Kraft abstossend Strahlen': abst_k, 'Kraftexponent in [3,6; 4,4]': ex_ok}
    return ('eingetroffen' if (abst and abst_k and ex_ok) else 'nicht eingetroffen'), w


def bilder(Ukorr, U, sp, lauf):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    farben = {'100': '#1f77b4', '110': '#d62728', '111': '#2ca02c'}
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    for nm in STRAHLEN:
        rs, us = strahl(Ukorr['N'], nm, 1.0, 16.5)
        ax[0].loglog(rs, -us, 'o', color=farben[nm], ms=4, label='N-Typ, [%s], torus-korrigiert' % nm)
    rr = np.linspace(1, 17, 100)
    ax[0].loglog(rr, 1 / (8 * np.pi * rr), 'k--', lw=1, label='1/(8 pi r) (Kontinuum, Schreibtisch)')
    ax[0].set_xlabel('r (Gitterabstaende)')
    ax[0].set_ylabel('-U(r)  (g = m = 1)')
    ax[0].set_title('N-Typ: Anziehung gleicher Massen')
    ax[0].legend(fontsize=7)
    for nm in STRAHLEN:
        rs, us = strahl(Ukorr['L'], nm, 1.0, 16.5)
        ax[1].plot(rs, us * 1e15, 'o-', color=farben[nm], ms=4, label='L-Typ, [%s], korrigiert (x 1e15)' % nm)
    for L, mk in zip((LALLE[0], LALLE[1], LALLE[-1]), ('x', '+', '^')):
        rs, us = strahl(U[('L', L)], '100', 1.0, 16.5)
        ax[1].plot(rs, us * 1e15, mk, color='gray', ms=5, label='L-Typ roh L = %d, [100] (x 1e15)' % L)
    ax[1].set_yscale('symlog', linthresh=1.0)
    ax[1].set_xlabel('r (Gitterabstaende)')
    ax[1].set_ylabel('U(r) x 1e15')
    ax[1].set_title('L-Typ: keine Wechselwirkung (roh: Torus-Konstante -1/(2 L^3))')
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(lauf, 'bild-wechselwirkung.png'), dpi=130)
    plt.close(fig)
    # Spektrum
    lin = sp['linien']
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.6))
    for i, nm in enumerate(('100', '111')):
        z = lin[nm]
        t = np.array(z['t'])
        eA = np.array(z['P0']['eigA'])
        eB = np.array(z['P0']['eigB'])
        eA1 = np.array(z['P1']['eigA'])
        eB1 = np.array(z['P1']['eigB'])
        for k in range(6):
            ax[i].semilogx(t, eA[:, k], '-', color='#1f77b4', lw=1, label='E-Teil A (ohne Strafe)' if k == 0 else None)
            ax[i].semilogx(t, eB[:, k], '-', color='#d62728', lw=1, label='a-Teil B (ohne Strafe)' if k == 0 else None)
            ax[i].semilogx(t, eA1[:, k], ':', color='#1f77b4', lw=1, label='A mit Strafe U = 1' if k == 0 else None)
            ax[i].semilogx(t, eB1[:, k], ':', color='#d62728', lw=1, label='B mit Strafe U = 1' if k == 0 else None)
        pa = np.array(z['phys_A'])
        pb = np.array(z['phys_B'])
        ax[i].semilogx(t, pa[:, 0], 'k--', lw=1.5, label='A auf eichfreier Zwangsflaeche')
        ax[i].semilogx(t, pb[:, 0], 'k-.', lw=1.5, label='B auf eichfreier Zwangsflaeche')
        ax[i].axhline(0, color='gray', lw=0.5)
        ax[i].set_ylim(-1.5, 2.5)
        ax[i].set_xlabel('|q| laengs [%s]' % nm)
        ax[i].set_ylabel('Eigenwert der Hesse-Matrix (J = g = 1)')
        ax[i].set_title('N-Typ: quadratische Form, Schnitt [%s]' % nm)
        ax[i].legend(fontsize=6)
    lam = sp['spektrum']['lam_scan']
    for U_, mk in ((1.0, 'o-'), (0.0, 's--')):
        ls = sorted(v['lam'] for v in lam.values() if v['U'] == U_)
        g = [lam['%.2f_U%g' % (l, U_)]['gamma_max'] for l in ls]
        ax[2].plot(ls, g, mk, label='Strafe U = %g' % U_)
    ax[2].axvline(0.5, color='gray', lw=0.5)
    ax[2].set_xlabel('lambda in -lambda (E^ii)^2 (Gu/Wen: 1/2)')
    ax[2].set_ylabel('groesste Wachstumsrate |Im omega| (L = 32)')
    ax[2].set_title('Lineare Dynamik: Wachstum nur fuer lambda != 1/2')
    ax[2].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(lauf, 'bild-spektrum.png'), dpi=130)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--dateien', default='statik-64,statik-128-192,statik-256')
    ap.add_argument('--Lkorr', default='128,192,256')
    ap.add_argument('--Lalt', default='64,128,256')
    a = ap.parse_args()
    global DATEIEN, LKORR, LALT, LALLE
    DATEIEN = a.dateien.split(',')
    LKORR = tuple(int(x) for x in a.Lkorr.split(','))
    LALT = tuple(int(x) for x in a.Lalt.split(','))
    LALLE = sorted(set(LKORR) | set(LALT))
    t0 = time.time()
    U, info = lade(a.lauf)
    with open(os.path.join(a.lauf, 'spektrum.json')) as f:
        sp = json.load(f)
    with open(os.path.join(a.lauf, 'kontrolle.json')) as f:
        ko = json.load(f)
    erg = {'erzeugt_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           'skript_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
           'quell_sha256': sorted(set(v['info']['skript_sha256'] for v in info.values()) | {sp['info']['skript_sha256'], ko['info']['skript_sha256']}),
           'urteile': {}, 'tabellen': {}, 'kontrollen': {}}
    Ukorr, Ualt, koef = {}, {}, {}
    for typ in ('N', 'L'):
        a0, b0, c0 = korrigiert(U, typ, LKORR)
        a1, _, _ = korrigiert(U, typ, LALT)
        Ukorr[typ], Ualt[typ] = a0, a1
        koef[typ] = (b0, c0)
    # ---- N0, N1
    u0, w0 = urteil_statik(Ukorr['L'], 'L')
    u1, w1 = urteil_statik(Ukorr['N'], 'N')
    r_all, u_n = schale(Ukorr['N'], 4.0, 16.0)
    _, u_n_alt = schale(Ualt['N'], 4.0, 16.0)
    w1['unsicherheit_korrektur_rel_max'] = float(np.abs((u_n - u_n_alt) / u_n).max())
    w1['abw_von_minus_1_durch_8pi_r'] = {
        'r>=4': float(np.abs(u_n * 8 * np.pi * r_all + 1).max()),
        'r>=8': float(np.abs((u_n * 8 * np.pi * r_all + 1)[r_all >= 8]).max())}
    st64 = info[DATEIEN[0]]['laeufe'][0]['stat']
    w1['minimum_auf_zwangsflaeche'] = {'tan_neg_anzahl_L64': st64['N']['tan_neg_anzahl'], 'tan_min_rel_L64': st64['N']['tan_min_rel']}
    w0['minimum_auf_zwangsflaeche'] = {'tan_neg_anzahl_L64': st64['L']['tan_neg_anzahl'], 'tan_min_rel_L64': st64['L']['tan_min_rel']}
    w0['roh_U_100_r8'] = {str(L): float(U[('L', L)][8, 0, 0]) for L in LALLE}
    w0['erwartet_roh_minus_1_durch_2L3'] = {str(L): -0.5 / L ** 3 for L in LALLE}
    w0['koef_c_bereich'] = [float(koef['L'][1].min()), float(koef['L'][1].max())]
    erg['urteile']['N0'] = {'urteil': u0, 'werte': w0,
                            'vermerk': 'Gepruefte Fassung: statischer stationaerer Wert von H_L (Gl. 27) unter exakten Bedingungen (13) und (31); Gu/Wen geben fuer r^-4 keine Herleitung.'}
    erg['urteile']['N1'] = {'urteil': u1, 'werte': w1}
    # ---- N2
    nd = sp['spektrum']['N_definitheit']
    indef = (nd['A_neg_q_anteil'] > 0) or (nd['B_neg_q_anteil'] > 0)
    aussen = (nd['A_zwang_min_rel'] >= -TOL_REL) and (nd['B_zwang_min_rel'] >= -TOL_REL) and \
             (nd['A_phys_min_rel'] >= -TOL_REL) and (nd['B_phys_min_rel'] >= -TOL_REL)
    erg['urteile']['N2'] = {'urteil': 'eingetroffen' if (indef and aussen) else 'nicht eingetroffen',
                            'werte': {'indefinit': indef, 'negative_richtungen_ausserhalb': aussen, 'definitheit': nd,
                                      'q0_homogen': sp['spektrum']['q0']},
                            'vermerk': 'q = 0 (homogene Torusmoden) nach PLAN gesondert; siehe q0_homogen.'}
    # ---- N3
    dyn = sp['spektrum']['dynamik']
    ex = ko['exakt']['saetze']
    wachs = {}
    for name in ('P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6'):
        d = dyn[name]
        wachs[name] = bool(d['neg_rel_max'] > TAU or d['im_rel_max'] > TAU)
    pd = nd['phys_dyn']
    wachs['phys'] = bool(pd['neg_rel_max'] > TAU or pd['im_rel_max'] > TAU)
    exakt_wachs = {k: (not v['alle_w2_reell_nichtneg_alle_punkte']) for k, v in ex.items()}
    gleit = any(wachs.values())
    exakt_N = any(exakt_wachs[k] for k in ('P0', 'P1', 'P3', 'P5'))
    if gleit == exakt_N:
        u3 = 'eingetroffen' if gleit else 'nicht eingetroffen'
        verm = 'Polynomiales (saekulares) Wachstum aus Jordanbloecken bei omega = 0 zaehlt nach PLAN nicht; siehe jordan.'
    else:
        u3 = 'nicht auswertbar'
        verm = 'Gleitkomma- und exakte Pruefung widersprechen sich.'
    erg['urteile']['N3'] = {'urteil': u3, 'vermerk': verm,
                            'werte': {'exponentiell_gleitkomma': wachs, 'exponentiell_exakt': exakt_wachs,
                                      'dynamik': dyn, 'phys_dyn': pd,
                                      'jordan_max_D_bei_0': {k: v['jordan_max_D_bei_0'] for k, v in ex.items()},
                                      'lam_scan': sp['spektrum']['lam_scan']}}
    erg['urteile']['N4'] = {'urteil': 'nicht auswertbar', 'vermerk': 'nicht gerechnet (PLAN Abschnitt 6, N4)', 'werte': {}}
    # ---- Tabellen
    tab = {}
    for typ in ('N', 'L'):
        rows = []
        for nm in STRAHLEN:
            for v in STRAHLEN[nm]:
                r = float(np.linalg.norm(v))
                if r < 2 - 1e-9 or r > 16.5:
                    continue
                rows.append({'v': list(v), 'r': r, 'U_korr': float(Ukorr[typ][v]), 'U_korr_alt': float(Ualt[typ][v]),
                             **{'U_L%d' % L: float(U[(typ, L)][v]) for L in LALLE}})
        tab[typ] = rows
    erg['tabellen']['strahlen'] = tab
    # ---- Kontrollen
    kon = {'operatoren_L32': sp['spektrum']['kontr'], 'ortsraum_L6': ko['ortsraum'], 'gw_s19': ko['gw_s19'],
           'exakt': {k: {kk: vv for kk, vv in v.items() if kk != 'beispiel_punkt0'} for k, v in ex.items()},
           'exakt_beispiel_P1': ex['P1']['beispiel_punkt0'], 'exakt_beispiel_L0': ex['L0']['beispiel_punkt0'],
           'exakt_punkte': ko['exakt']['punkte'], 'drift': ko['drift']}
    for name, js in info.items():
        for l in js['laeufe']:
            kon['statik_L%d' % l['L']] = {'stat': l['stat'], 'sym': l['sym'], 't_s': l['t_gesamt_s'], 'kap_q0': l['kap_q0']}
    erg['kontrollen'] = kon
    with open(a.out + '.tmp', 'w') as f:
        json.dump(erg, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    bilder(Ukorr, U, sp, a.lauf)
    print('Urteile:', {k: v['urteil'] for k, v in erg['urteile'].items()})
    print('fertig auswertung %.1f s' % (time.time() - t0), flush=True)


if __name__ == '__main__':
    main()
