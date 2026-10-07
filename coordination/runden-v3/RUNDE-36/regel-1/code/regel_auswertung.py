#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGEL-1 (Runde 36): mechanische Urteile RG0 bis RG3 nach PLAN.md, Tabellen, Kontrollen, Bilder.

Eingaben im Laufordner: radial.json, wellen.json, kontrolle.json, statik-<L...>.json (alle L zusammen), optional
tensor-eis-n-auswertung.json (Punktquellen-Vergleich der Torus-Korrektur).
Aufruf: regel_auswertung.py --lauf lauf --out lauf/auswertung.json
"""
import argparse, glob, hashlib, json, os, time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---- Schwellen (PLAN.md Abschnitt 6, vor dem Einfrieren festgelegt)
TOL_INV = 1e-12          # RG0 (Karte)
TAU = 1e-6               # Wachstumstest (wie TENSOR-EIS-N, LAMBDA-1)
SPREAD_RG1 = 0.01        # RG1 (Karte): v ueber Richtungen innerhalb 1 %
K_LIN_MAX = 1.0          # RG1 [F]: |omega^2/(v0^2 k^2) - 1| / k^2 <= 1 fuer alle k
V0_2_MIN = 0.01          # RG1 [F]: v0^2 > 0,01 (sonst nicht linear)
SPREAD_RG2 = 0.01        # RG2 (Karte)
D_MIN, D_MAX = 4.0, 10.0  # RG2 (Karte), in Ballradien des grossen Balls
D_FALL = 8.0             # RG3 (Karte)
ETA_E_MAX = 1e-3         # RG3 (Karte)
ETA_Q_MIN = 5e-2         # RG3 (Karte)
TORUS_TOL = 1e-3         # Tor fuer RG2 [F]
AUFL_R_MIN = 4.0         # Tor [F]: R_half(klein)/h >= 4
AUFL_TOL = 1e-4          # Tor [F]: |Gittersumme/Radialintegral - 1| <= 1e-4
L_HAUPT = 256          # per --Lhaupt aenderbar (nur fuer Rauchlaeufe)
GG = 1.0                 # g
LINIEN = {'100': (1, 0, 0), '110': (1, 1, 0), '111': (1, 1, 1)}
K_LISTE = (0.025, 0.05, 0.1, 0.2)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def lade(p):
    with open(p) as f:
        return json.load(f)


def u_korr(Ul, W, Sa, Sb, m2a, m2b, L):
    """Ewald-Torus-Korrektur: U_inf = U_L + (g/2) S_a S_b [W(s) + (m2_a + m2_b)/(6 L^3)]."""
    return np.asarray(Ul) + 0.5 * GG * Sa * Sb * (np.asarray(W) + (m2a + m2b) / (6.0 * L ** 3))


def statik_sammeln(lauf):
    baelle, proL, quellen = None, {}, []
    for p in sorted(glob.glob(os.path.join(lauf, 'statik-*.json'))):
        d = lade(p)
        quellen.append(p)
        st = d['statik']
        if baelle is None:
            baelle = st['baelle']
            h = st['h']
        for Ls, r in st['L'].items():
            proL[int(Ls)] = r
    return baelle, h, proL, quellen


def korr_linien(r, L, baelle, paar, kopplung):
    a, b = paar[0], paar[1]
    Sa = baelle[a]['E_gitter'] if kopplung == 'E' else baelle[a]['N_gitter']
    Sb = baelle[b]['E_gitter'] if kopplung == 'E' else baelle[b]['N_gitter']
    m2a = baelle[a]['m2_E_gitter'] if kopplung == 'E' else baelle[a]['m2_N_gitter']
    m2b = baelle[b]['m2_E_gitter'] if kopplung == 'E' else baelle[b]['m2_N_gitter']
    out = {}
    for nm in LINIEN:
        out[nm] = u_korr(r['linien'][paar + kopplung][nm], r['W'][nm], Sa, Sb, m2a, m2b, L)
    return out, Sa, Sb


def newton_tabelle(r, L, baelle, R, paar, kopplung):
    Uk, Sa, Sb = korr_linien(r, L, baelle, paar, kopplung)
    zeilen = []
    for nm, e in LINIEN.items():
        le = float(np.linalg.norm(e))
        for n in range(1, len(Uk[nm])):
            d = n * le
            if D_MIN * R - 1e-9 <= d <= D_MAX * R + 1e-9:
                U = float(Uk[nm][n])
                Ur = float(r['linien'][paar + kopplung][nm][n])
                zeilen.append({'linie': nm, 'n': n, 'd': d, 'd_durch_R': d / R, 'U_korr': U, 'U_roh': Ur,
                               'y': U * d / (Sa * Sb), 'y_8pi': U * d / (Sa * Sb) * 8 * np.pi})
    return zeilen


def fall(r, L, baelle, R, kopplung, n_fest=None):
    """Kraft je Energie auf k und g im Feld von s (zentrale Differenz laengs der Linie); Traegheit = Energie."""
    erg = {}
    for nm, e in LINIEN.items():
        le = float(np.linalg.norm(e))
        n0 = int(round(D_FALL * R / le)) if n_fest is None else n_fest[nm]
        a = {}
        for t in ('k', 'g'):
            Uk, Sa, Sb = korr_linien(r, L, baelle, t + 's', kopplung)
            U = Uk[nm]
            Ur = np.asarray(r['linien'][t + 's' + kopplung][nm])
            F = -(U[n0 + 1] - U[n0 - 1]) / (2 * le)
            Fr = -(Ur[n0 + 1] - Ur[n0 - 1]) / (2 * le)
            Et = baelle[t]['E_gitter']
            a[t] = {'F': float(F), 'a': float(F / Et), 'a_roh': float(Fr / Et), 'quelle_S': Sa}
        ak, ag = a['k']['a'], a['g']['a']
        akr, agr = a['k']['a_roh'], a['g']['a_roh']
        erg[nm] = {'n': n0, 'd': n0 * le, 'd_durch_R': n0 * le / R, 'a_k': ak, 'a_g': ag,
                   'eta': float(2 * abs(ak - ag) / (ak + ag)) if (ak + ag) != 0 else float('nan'),
                   'eta_roh': float(2 * abs(akr - agr) / (akr + agr)) if (akr + agr) != 0 else float('nan')}
    return erg


def eta_profil(r, L, baelle, R, kopplung, nm='100'):
    e = LINIEN[nm]
    le = float(np.linalg.norm(e))
    Uk_k, _, _ = korr_linien(r, L, baelle, 'ks', kopplung)
    Uk_g, _, _ = korr_linien(r, L, baelle, 'gs', kopplung)
    zeilen = []
    for n in range(2, len(Uk_k[nm]) - 1):
        d = n * le
        if not (D_MIN * R - 1e-9 <= d <= D_MAX * R + 1e-9):
            continue
        Fk = -(Uk_k[nm][n + 1] - Uk_k[nm][n - 1]) / (2 * le)
        Fg = -(Uk_g[nm][n + 1] - Uk_g[nm][n - 1]) / (2 * le)
        ak, ag = Fk / baelle['k']['E_gitter'], Fg / baelle['g']['E_gitter']
        zeilen.append({'d_durch_R': d / R, 'a_k': float(ak), 'a_g': float(ag), 'eta': float(2 * abs(ak - ag) / (ak + ag))})
    return zeilen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--Lhaupt', type=int, default=256)
    a = ap.parse_args()
    global L_HAUPT
    L_HAUPT = a.Lhaupt
    lauf = a.lauf
    WE = lade(os.path.join(lauf, 'wellen.json'))
    KO = lade(os.path.join(lauf, 'kontrolle.json'))
    RA = lade(os.path.join(lauf, 'radial.json'))
    baelle, h, proL, quellen = statik_sammeln(lauf)
    quellen += [os.path.join(lauf, x) for x in ('wellen.json', 'kontrolle.json', 'radial.json')]
    aus = {'erzeugt_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           'skript_sha256': sha(os.path.abspath(__file__)),
           'quell_sha256': {os.path.basename(p): sha(p) for p in quellen},
           'eingabe_skript_sha256': {os.path.basename(p): lade(p)['info']['skript_sha256'] for p in quellen},
           'urteile': {}, 'tabellen': {}, 'kontrollen': {}}
    U = aus['urteile']
    w = WE['wellen']
    ko = KO['kontrolle']

    # ------------------------------------------------------------------ RG0
    inv_f = w['invarianz_bz']['lin_max']
    inv_q = w['invarianz_bz']['quad_max']
    inv_r = max(v['inv_lin_max'] for v in w['richtungs_k'].values())
    inv_z = w['zwang_projektion']['invarianz_defekt_rel_max']
    inv_o = ko['invarianz_ort']['defekt_c0.50']
    defekt = max(inv_f, inv_q, inv_r, inv_z, inv_o)
    wach_proj = w['zwang_projektion']['anzahl_q_wachsend']
    wach_dirac = w['zwang_dirac']['anzahl_q_wachsend']
    wach_moden = w['moden_bz']['anzahl_q_wachsend']
    wach_r = sum(sum(1 for x in v['wach'] if x) for v in w['richtungs_k'].values())
    rg0_i = defekt < TOL_INV
    rg0_ii = (wach_proj == 0 and wach_dirac == 0 and wach_moden == 0 and wach_r == 0)
    U['RG0'] = {'urteil': 'eingetroffen' if (rg0_i and rg0_ii) else 'nicht eingetroffen',
                'werte': {'invarianzdefekt_max': defekt, 'energie_lin_bz': inv_f, 'energie_quad_bz': inv_q,
                          'energie_lin_richtungen': inv_r, 'Z_invarianz_bewegung': inv_z, 'ortsraum_L6': inv_o,
                          'tt_identitaet_max': w['invarianz_bz']['tt_identitaet_max'],
                          'kontrast_c045_c055': {k: v['lin_min'] for k, v in w['invarianz_kontrast'].items()},
                          'kontrast_ortsraum': {k: ko['invarianz_ort'][k] for k in ('defekt_c0.45', 'defekt_c0.55')},
                          'wachsend_q_projektion': wach_proj, 'wachsend_q_dirac': wach_dirac,
                          'wachsend_q_moden': wach_moden, 'wachsend_richtungsproben': wach_r,
                          'dirac_dim': w['zwang_dirac']['dim'], 'dirac_einheitlich': w['zwang_dirac']['einheitlich'],
                          'neg_rel_max': w['moden_bz']['neg_rel_max'], 'im_rel_max': w['moden_bz']['im_rel_max'],
                          'D8_re_max_rel': w['zwang_projektion']['D8_re_max_rel']}}

    # ------------------------------------------------------------------ RG1
    D = np.array(w['richtungen'])
    nd = len(D)
    nl_ok = all(all(x == 2 for x in v['n_lauf']) for v in w['richtungs_k'].values())
    a_ok = (w['moden_bz']['anzahl_q_nicht_2'] == 0) and nl_ok
    ks = np.array(K_LISTE)
    Y = np.zeros((nd, 2, len(ks)))
    for j, kk in enumerate(K_LISTE):
        w2 = np.array(w['richtungs_k']['%g' % kk]['w2'])
        Y[:, :, j] = w2[:, :2] / kk ** 2
    Amat = np.stack([np.ones_like(ks), ks ** 2], 1)
    v02 = np.zeros((nd, 2))
    bko = np.zeros((nd, 2))
    lin_abw = np.zeros((nd, 2))
    for i in range(nd):
        for m in range(2):
            coef, *_ = np.linalg.lstsq(Amat, Y[i, m], rcond=None)
            v02[i, m], bko[i, m] = coef
            lin_abw[i, m] = np.max(np.abs(Y[i, m] / coef[0] - 1.0) / ks ** 2) if coef[0] > 0 else np.inf
    b_ok = bool((v02 > V0_2_MIN).all() and (lin_abw <= K_LIN_MAX).all())
    j01 = K_LISTE.index(0.1)
    v01 = np.sqrt(np.maximum(Y[:, :, j01], 0.0))      # omega/|k| bei |k| = 0,1
    spread = float((v01.max() - v01.min()) / v01.mean())
    c_ok = spread <= SPREAD_RG1
    U['RG1'] = {'urteil': 'eingetroffen' if (a_ok and b_ok and c_ok) else 'nicht eingetroffen',
                'werte': {'richtungen': nd, 'genau_2_laufend_bz': w['moden_bz']['anzahl_q_nicht_2'] == 0,
                          'genau_2_laufend_richtungen': nl_ok, 'n_null_werte_bz': w['moden_bz']['n_null_werte'],
                          'null_E_anteil_G23_min': w['moden_bz']['null_E_anteil_G23_min'],
                          'null_a_G15_rest_max': w['moden_bz']['null_a_G15_rest_max'],
                          'w2_lauf_ueber_K2_bz': [w['moden_bz']['w2_lauf_ueber_K2_min'], w['moden_bz']['w2_lauf_ueber_K2_max']],
                          'v0_quadrat_min': float(v02.min()), 'v0_quadrat_max': float(v02.max()),
                          'v0_min': float(np.sqrt(v02.min())), 'v0_max': float(np.sqrt(v02.max())),
                          'k2_koeffizient_min': float((bko / v02).min()), 'k2_koeffizient_max': float((bko / v02).max()),
                          'linear_abw_durch_k2_max': float(lin_abw.max()),
                          'v_k01_min': float(v01.min()), 'v_k01_max': float(v01.max()), 'v_k01_mittel': float(v01.mean()),
                          'v_k01_streuung_rel': spread, 'teil_a': a_ok, 'teil_b': b_ok, 'teil_c': c_ok}}

    # ------------------------------------------------------------------ Tore (Aufloesung, Torus)
    R = baelle['g']['R_half'] / h
    aufl = {nm: {'R_half_durch_h': b['R_half'] / h, 'E_rel': b['E_gitter_rel_abw'], 'N_rel': b['N_gitter_rel_abw']}
            for nm, b in baelle.items()}
    tor_aufl = (baelle['k']['R_half'] / h >= AUFL_R_MIN and
                all(abs(v['E_rel']) <= AUFL_TOL and abs(v['N_rel']) <= AUFL_TOL for v in aufl.values()))
    aus['kontrollen']['aufloesung'] = {'werte': aufl, 'tor_bestanden': tor_aufl}
    Ls = sorted(proL)
    rH = proL[L_HAUPT]
    tabs = {}
    for paar in ('kg', 'gg', 'kk'):
        for kp in ('E', 'N'):
            Rp = (baelle['g']['R_half'] if 'g' in paar else baelle['k']['R_half']) / h
            tabs[paar + kp] = {L: newton_tabelle(proL[L], L, baelle, Rp, paar, kp) for L in Ls}
    # Torus-Tor: y bei L != 256 gegen L = 256, gleiche Punkte, Paar kg, E
    tor_abw = {}
    ref = {(z['linie'], z['n']): z['y'] for z in tabs['kgE'][L_HAUPT]}
    for L in Ls:
        if L == L_HAUPT:
            continue
        m = 0.0
        for z in tabs['kgE'][L]:
            k = (z['linie'], z['n'])
            if k in ref:
                m = max(m, abs(z['y'] / ref[k] - 1.0))
        tor_abw[str(L)] = m
    tor_torus = all(v <= TORUS_TOL for v in tor_abw.values()) and len(tor_abw) >= 1
    # roh (ohne Korrektur) zum Vergleich
    roh = [z['U_roh'] * z['d'] / (baelle['k']['E_gitter'] * baelle['g']['E_gitter']) for z in tabs['kgE'][L_HAUPT]]
    aus['kontrollen']['torus'] = {'max_rel_abw_y_gegen_L256': tor_abw, 'tor_bestanden': tor_torus,
                                  'roh_y_8pi_min_max_L256': [float(min(roh) * 8 * np.pi), float(max(roh) * 8 * np.pi)],
                                  'ewald_alpha_abw_max': {str(L): proL[L]['ewald_alpha_abw_max'] for L in Ls}}
    # Punktquellen gegen TENSOR-EIS-N (Torus-Korrektur 3-Punkt-Anpassung dort)
    pt = os.path.join(lauf, 'tensor-eis-n-auswertung.json')
    if os.path.exists(pt):
        tn = lade(pt)['tabellen']['strahlen']['N']
        pv = {}
        for L in Ls:
            r = proL[L]
            m = 0.0
            for z in tn:
                v = z['v']
                nm = {(1, 0, 0): '100', (1, 1, 0): '110', (1, 1, 1): '111'}.get(tuple(int(np.sign(x)) for x in v))
                if nm is None:
                    continue
                n = int(max(v))
                Uc = r['linien']['punkt'][nm][n] + 0.5 * GG * r['W'][nm][n]
                m = max(m, abs(Uc / z['U_korr'] - 1.0))
            pv[str(L)] = m
        aus['kontrollen']['punkt_gegen_tensor_eis_n_rel_max'] = pv

    # ------------------------------------------------------------------ RG2
    z2 = tabs['kgE'][L_HAUPT]
    ys = np.array([z['y'] for z in z2])
    Uv = np.array([z['U_korr'] for z in z2])
    spread2 = float((ys.max() - ys.min()) / abs(np.median(ys)))
    rg2_ok = bool((Uv < 0).all() and spread2 <= SPREAD_RG2)
    if not (tor_aufl and tor_torus):
        urteil2 = 'nicht auswertbar'
    else:
        urteil2 = 'eingetroffen' if rg2_ok else 'nicht eingetroffen'
    nebenpaare = {}
    for key in ('ggE', 'kkE', 'kgN'):
        zz = tabs[key][L_HAUPT]
        yy = np.array([z['y'] for z in zz])
        nebenpaare[key] = {'y_8pi_min': float(yy.min() * 8 * np.pi), 'y_8pi_max': float(yy.max() * 8 * np.pi),
                           'streuung_rel': float((yy.max() - yy.min()) / abs(np.median(yy))), 'punkte': len(zz)}
    U['RG2'] = {'urteil': urteil2,
                'werte': {'paar': 'Q=%g mit Q=%g' % (baelle['k']['Q'], baelle['g']['Q']), 'L': L_HAUPT,
                          'R_gitter': R, 'd_bereich_gitter': [D_MIN * R, D_MAX * R], 'punkte': len(z2),
                          'alle_U_negativ': bool((Uv < 0).all()), 'y_min': float(ys.min()), 'y_max': float(ys.max()),
                          'y_8pi_min': float(ys.min() * 8 * np.pi), 'y_8pi_max': float(ys.max() * 8 * np.pi),
                          'y_median_8pi': float(np.median(ys) * 8 * np.pi), 'streuung_rel': spread2,
                          'G_eff_soll_8pi': 1.0, 'tor_aufloesung': tor_aufl, 'tor_torus': tor_torus,
                          'nebenpaare_L256': nebenpaare}}
    if urteil2 == 'nicht auswertbar':
        U['RG2']['vermerk'] = 'Tor verfehlt: Aufloesung %s, Torus %s' % (tor_aufl, tor_torus)

    # ------------------------------------------------------------------ RG3
    fE = fall(rH, L_HAUPT, baelle, R, 'E')
    fQ = fall(rH, L_HAUPT, baelle, R, 'N')
    a_pos = all(v['a_k'] > 0 and v['a_g'] > 0 for f in (fE, fQ) for v in f.values())
    etaE = max(v['eta'] for v in fE.values())
    etaQ = min(v['eta'] for v in fQ.values())
    rk = baelle['k']['N_gitter'] / baelle['k']['E_gitter']
    rg = baelle['g']['N_gitter'] / baelle['g']['E_gitter']
    eta_Q_soll = 2 * abs(rk - rg) / (rk + rg)
    rg3_ok = a_pos and etaE < ETA_E_MAX and etaQ > ETA_Q_MIN
    urteil3 = ('eingetroffen' if rg3_ok else 'nicht eingetroffen') if tor_aufl else 'nicht auswertbar'
    andereL = {str(L): {'eta_E_max': max(v['eta'] for v in fall(proL[L], L, baelle, R, 'E').values()),
                        'eta_Q_min': min(v['eta'] for v in fall(proL[L], L, baelle, R, 'N').values())} for L in Ls}
    U['RG3'] = {'urteil': urteil3,
                'werte': {'L': L_HAUPT, 'd_durch_R': {k: v['d_durch_R'] for k, v in fE.items()},
                          'energie': fE, 'ladung': fQ, 'eta_E_max': etaE, 'eta_Q_min': etaQ,
                          'alle_a_positiv': a_pos, 'N_durch_E_k': rk, 'N_durch_E_g': rg, 'eta_Q_aus_N_durch_E': eta_Q_soll,
                          'andere_L': andereL, 'tor_aufloesung': tor_aufl}}
    if urteil3 == 'nicht auswertbar':
        U['RG3']['vermerk'] = 'Aufloesungstor verfehlt'

    # ------------------------------------------------------------------ Tabellen und weitere Kontrollen
    aus['tabellen']['baelle'] = {nm: {k: b[k] for k in ('Q', 'om2', 'omega', 'E', 'N', 'E_durch_Q', 'N_durch_E', 'R_half', 'R_half_gitter',
                                                        'S0', 'virial', 'E_gitter', 'N_gitter', 'E_gitter_rel_abw', 'N_gitter_rel_abw',
                                                        'm2_E', 'm2_E_gitter', 'anteil_jenseits_rcut_E', 'f2_bei_rcut_rel')}
                                 for nm, b in baelle.items()}
    aus['tabellen']['h'] = h
    aus['tabellen']['newton_kgE_L256'] = z2
    aus['tabellen']['eta_profil_100'] = {'E': eta_profil(rH, L_HAUPT, baelle, R, 'E'), 'N': eta_profil(rH, L_HAUPT, baelle, R, 'N')}
    ra = RA['radial']
    aus['kontrollen']['radial'] = {k: {'vergleich_tabelle': v['vergleich_tabelle'], 'Q_min': v['Q_min'], 'om2_Q_min': v['om2_Q_min'],
                                       'virial_max': v['virial_max'], 'res_max': v['res_max'], 'dEdQ_max_rel_abw_familie': v['dEdQ_max_rel_abw'],
                                       'baelle_dEdQ': {nm: b['dEdQ_rel_abw'] for nm, b in v['baelle'].items()},
                                       'aufloesung': {nm: b['aufloesung'] for nm, b in v['baelle'].items()}}
                                   for k, v in ra['ergebnisse'].items()}
    aus['kontrollen']['radial_dr_probe'] = ra['dr_probe']
    aus['kontrollen']['kern'] = {str(L): proL[L]['kern'] for L in Ls}
    aus['kontrollen']['imag_rel_max'] = {str(L): max(proL[L]['imag_rel'].values()) for L in Ls}
    aus['kontrollen']['statik_ortsraum'] = {k: ko['statik_ort'][k] for k in ('asym_max_abw', 'sym_max_abw', 'skala')}
    aus['kontrollen']['voller_kkt'] = ko['voll']
    aus['kontrollen']['invarianz_ort'] = ko['invarianz_ort']
    aus['kontrollen']['zeit'] = {k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if kk != 'zeilen'})
                                 for k, v in ko['zeit'].items()}

    # ------------------------------------------------------------------ Bilder
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    t = np.array(w['linien']['t'])
    for nm, col in zip(LINIEN, ('C0', 'C1', 'C2')):
        w2 = np.array(w['linien'][nm]['w2'])
        K2 = np.array(w['linien'][nm]['K2'])
        ax[0].plot(t, np.sqrt(np.maximum(w2[:, 0], 0)), '-', color=col, label='[%s] laufende Moden' % nm)
        ax[0].plot(t, np.sqrt(np.maximum(w2[:, 1], 0)), ':', color=col)
        ax[0].plot(t, np.sqrt(K2), 'k--', lw=0.6)
    ax[0].plot(t, t, color='0.5', lw=0.8, label='omega = |q| (v = 1)')
    ax[0].set_xlabel('|q| (Gitter)')
    ax[0].set_ylabel('omega')
    ax[0].set_title('Wellen auf der Zwangsflaeche, c = 1/2 (gestrichelt: 2 sin-Formel)')
    ax[0].legend(fontsize=8)
    ax[1].plot(np.arange(nd), v01[:, 0], 'o', ms=3, label='Mode 1')
    ax[1].plot(np.arange(nd), v01[:, 1], 'x', ms=3, label='Mode 2')
    mu = v01.mean()
    ax[1].axhspan(mu * (1 - SPREAD_RG1 / 2), mu * (1 + SPREAD_RG1 / 2), color='0.9', label='Band 1 %')
    ax[1].set_xlabel('Richtung (0..99 Fibonacci, 100..102 = [100], [110], [111])')
    ax[1].set_ylabel('v = omega/|k| bei |k| = 0,1')
    ax[1].set_title('RG1: Streuung %.2e' % spread)
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(lauf, 'bild-dispersion.png'), dpi=120)
    plt.close(fig)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    for key, mk in (('kgE', 'o'), ('ggE', 's'), ('kkE', '^')):
        zz = tabs[key][L_HAUPT]
        for nm, col in zip(LINIEN, ('C0', 'C1', 'C2')):
            sel = [z for z in zz if z['linie'] == nm]
            ax[0].plot([z['d_durch_R'] for z in sel], [-z['y_8pi'] for z in sel], mk, ms=3, color=col,
                       label='%s [%s]' % (key[:2], nm) if key == 'kgE' or nm == '100' else None)
    ax[0].axhspan(0.995, 1.005, color='0.9')
    ax[0].set_xlabel('d / R (R = R_half des groesseren Balls / h)')
    ax[0].set_ylabel('-U d / (E1 E2) * 8 pi')
    ax[0].set_title('RG2: Newton mit Q-Ball-Quellen, L = 256, Ewald-korrigiert')
    ax[0].legend(fontsize=7, ncol=2)
    for L in Ls:
        zz = tabs['kgE'][L]
        sel = [z for z in zz if z['linie'] == '100']
        ax[1].plot([z['d_durch_R'] for z in sel], [-z['y_8pi'] for z in sel], '-', label='L = %d korrigiert' % L)
        ax[1].plot([z['d_durch_R'] for z in sel], [-z['U_roh'] * z['d'] / (baelle['k']['E_gitter'] * baelle['g']['E_gitter']) * 8 * np.pi
                                                   for z in sel], ':', label='L = %d roh' % L)
    ax[1].set_xlabel('d / R')
    ax[1].set_ylabel('-U d / (E1 E2) * 8 pi, [100]')
    ax[1].set_title('Torus: roh gegen korrigiert')
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(lauf, 'bild-newton.png'), dpi=120)
    plt.close(fig)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    for kp, col, lab in (('E', 'C0', 'Energiekopplung'), ('N', 'C3', 'Ladungskopplung')):
        zz = aus['tabellen']['eta_profil_100'][kp]
        ax[0].semilogy([z['d_durch_R'] for z in zz], [max(z['eta'], 1e-18) for z in zz], '-o', ms=3, color=col, label=lab)
    ax[0].axhline(ETA_E_MAX, color='C0', ls='--', lw=0.8)
    ax[0].axhline(ETA_Q_MIN, color='C3', ls='--', lw=0.8)
    ax[0].axvline(D_FALL, color='0.6', lw=0.8)
    ax[0].set_xlabel('d / R ([100])')
    ax[0].set_ylabel('eta = 2 |a1 - a2| / (a1 + a2)')
    ax[0].set_title('RG3: Q = %g gegen Q = %g im Feld von Q = %g' % (baelle['k']['Q'], baelle['g']['Q'], baelle['s']['Q']))
    ax[0].legend(fontsize=8)
    xs = np.arange(3)
    ax[1].bar(xs - 0.2, [max(fE[nm]['eta'], 1e-18) for nm in LINIEN], 0.4, label='Energie', color='C0')
    ax[1].bar(xs + 0.2, [fQ[nm]['eta'] for nm in LINIEN], 0.4, label='Ladung', color='C3')
    ax[1].set_yscale('log')
    ax[1].set_xticks(xs)
    ax[1].set_xticklabels(['[100]', '[110]', '[111]'])
    ax[1].axhline(ETA_E_MAX, color='C0', ls='--', lw=0.8)
    ax[1].axhline(ETA_Q_MIN, color='C3', ls='--', lw=0.8)
    ax[1].set_title('eta bei d = 8 R')
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(lauf, 'bild-eta.png'), dpi=120)
    plt.close(fig)

    with open(a.out + '.tmp', 'w') as f:
        json.dump(aus, f, indent=1, default=float)
    os.replace(a.out + '.tmp', a.out)
    print('Urteile:', {k: v['urteil'] for k, v in U.items()}, flush=True)


if __name__ == '__main__':
    main()
