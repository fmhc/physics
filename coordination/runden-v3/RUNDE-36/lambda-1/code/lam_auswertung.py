#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LAMBDA-1, Auswertung nach PLAN.md (Urteilsregeln Abschnitt 6), Bilder.

Basis: Kopie von RUNDE-36/tensor-eis-n/code/tn_auswertung.py; die Helfer korrigiert, steigung, schale, strahl sind
unveraendert uebernommen, alles Uebrige ist neu.
Aufruf (auf der .69, im Ordner runde36-lambda):
  lam_auswertung.py --lauf lauf --out lauf/auswertung.json
Liest lauf/statik-64-128-192.json/.npz, lauf/statik-256.json/.npz, lauf/scan.json, lauf/kontrolle.json und, falls
vorhanden, lauf/tensor-eis-n-auswertung.json (nur Vergleich, Kontrolle).
"""
import argparse, json, os, time, hashlib
import numpy as np

DATEIEN, LKORR, LALT, LALLE = None, None, None, None
TAU = 1e-6              # exponentielles Wachstum, relativ (wie TENSOR-EIS-N)
TOL_OFF = 1e-6          # L3: Anteil ausserhalb Z, darueber "neben der Zwangsflaeche"
TOL_KERN = 1e-10        # L4: c-Unabhaengigkeit des statischen Kerns bestaetigt
C_NAMEN = ['0.30', '1/3', '0.40', '0.45', '0.48', '0.49', '0.50', '0.51', '0.52', '0.55', '0.60', '0.70']
C_WERT = dict(zip(C_NAMEN, [0.30, 1.0 / 3.0, 0.40, 0.45, 0.48, 0.49, 0.50, 0.51, 0.52, 0.55, 0.60, 0.70]))
FREI = ('P0', 'P1')
ALLE = ('P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6')
L1_WACHS = ('0.40', '0.45', '0.48', '0.49')
L1_FIT = ('0.45', '0.48', '0.49')
L1_FENSTER = (0.35, 0.65)
L2_PAAR = ('0.45', '0.55')
L2_SCHWELLE = 0.20
L0_TOL = 0.01
L4_TOL = 0.01
L4_SPRUNG = 0.10
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


def geff(Ukorr, lo=8.0, hi=16.0):
    """Ausgleich U = -G/r (g = m = 1) ueber alle Oktantpunkte lo <= r <= hi (kleinste Quadrate)."""
    r, u = schale(Ukorr, lo, hi)
    G = float(-(u / r).sum() / (1.0 / r ** 2).sum())
    rest = float(np.abs(u + G / r).max() / np.abs(u).max())
    return G, rest, int(len(r))


def anziehung(Ukorr):
    _, u_all = schale(Ukorr, 2.0, 16.0)
    kraft = {}
    for nm in STRAHLEN:
        _, uu = strahl(Ukorr, nm, 2.0, 16.0)
        kraft[nm] = bool((np.diff(uu) > 0).all())
    return bool((u_all < 0).all()), kraft, float(u_all.max()), float(u_all.min())


def gitter_K2(L=32):
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    qx, qy, qz = np.meshgrid(q1, q1, q1, indexing='ij')
    K2 = (4 * np.sin(qx / 2) ** 2 + 4 * np.sin(qy / 2) ** 2 + 4 * np.sin(qz / 2) ** 2).reshape(-1)
    return K2[K2 > 0]


def bilder(sc, Ukorr, G, lauf):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fr, zw, di = sc['frei'], sc['zwang'], sc['dirac']
    cs = np.array([C_WERT[cn] for cn in C_NAMEN])
    cc = np.linspace(0.28, 0.72, 441)
    K2 = gitter_K2(sc['L'])
    fminus = float((K2 - 2 * K2 ** 2).max())
    fplus = float((2 * K2 ** 2 - K2).max())
    fig, ax = plt.subplots(2, 2, figsize=(13.5, 10))
    # (a) P0
    a0 = ax[0, 0]
    a0.plot(cc, np.sqrt(12.0 * np.maximum(0.0, 1 - 2 * cc)), 'k--', lw=1,
            label='Horava (IR): omega^2 = -((lam-1)/(3lam-1)) xi k^2,\nxi = gJ, k^2 -> K^2 = 12 (Zonenecke)')
    a0.plot(cs, [fr['P0'][cn]['gamma_max'] for cn in C_NAMEN], 'o', color='#1f77b4', ms=7, label='Gitter frei, P0 (ohne Strafterme)')
    a0.plot(cs, [zw['P0'][cn]['gamma_max'] for cn in C_NAMEN], 's', mfc='none', color='#d62728', ms=10,
            label='Zwangsflaeche (b), Projektion')
    a0.plot(cs, [di['P0'][cn]['gamma_max'] for cn in C_NAMEN], 'x', color='#2ca02c', ms=8, label='Zwangsflaeche, Dirac-Unterraum')
    a0.set_title('P0: Form Gl. 32 mit -c (E^ii)^2, ohne Strafterme')
    # (b) P1
    a1 = ax[0, 1]
    hl1 = np.where(cc < 0.5, np.sqrt(np.maximum(0.0, (1 - 2 * cc) * fminus)), np.sqrt(np.maximum(0.0, (2 * cc - 1) * fplus)))
    a1.plot(cc, hl1, 'k--', lw=1, label='Horava mit z=2-Glied: omega^2 = -((lam-1)/(3lam-1))(xi K^2 - eta K^4),\n'
                                         'eta = 2 U_s J (Gitter-K^2, Maximum ueber die Zone)')
    a1.plot(cc, np.sqrt(12.0 * np.maximum(0.0, 1 - 2 * cc)), ':', color='gray', lw=1, label='Horava (IR) wie links')
    a1.plot(cs, [fr['P1'][cn]['gamma_max'] for cn in C_NAMEN], 'o', color='#ff7f0e', ms=7, label='Gitter frei, P1 (U_v = U_s = 1)')
    a1.plot(cs, [zw['P1'][cn]['gamma_max'] for cn in C_NAMEN], 's', mfc='none', color='#d62728', ms=10,
            label='Zwangsflaeche (b), Projektion')
    a1.plot(cs, [di['P1'][cn]['gamma_max'] for cn in C_NAMEN], 'x', color='#2ca02c', ms=8, label='Zwangsflaeche, Dirac-Unterraum')
    a1.set_yscale('symlog', linthresh=0.01)
    a1.set_title('P1: Gu/Wen-Gittermodell (Strafterme U = 1)')
    for a in (a0, a1):
        a.axvline(0.5, color='gray', lw=0.6)
        a.axvline(1 / 3, color='gray', lw=0.4, ls=':')
        a.set_xlabel('c im Spurglied -c (E^ii)^2   (lambda = c/(3c-1); c = 1/2: lambda = 1)')
        a.set_ylabel('groesste Wachstumsrate gamma (BZ-Gitter L = %d)' % sc['L'])
        a.legend(fontsize=7)
    # (c) kleines k
    a2 = ax[1, 0]
    a2.plot(cc, np.sqrt(np.maximum(0.0, 1 - 2 * cc)), 'k--', lw=1, label='Horava (IR): gamma/k = sqrt(xi (lam-1)/(3lam-1)) = sqrt(1-2c)')
    t = np.array(sc['linien']['t'])
    K0 = 2 * np.sin(t[0] / 2)
    for S, col in (('P0', '#1f77b4'), ('P1', '#ff7f0e')):
        a2.plot(cs, [fr[S][cn]['gamma_q_min'] / fr[S][cn]['K_q_min'] for cn in C_NAMEN], 'o', color=col, ms=6, mfc='none',
                label='%s: kleinstes Gitter-q = 2 pi/%d, gamma/|K|' % (S, sc['L']))
        a2.plot(cs, [sc['linien']['100'][S][cn]['gamma'][0] / K0 for cn in C_NAMEN], '+', color=col, ms=9,
                label='%s: Schnitt [100], |q| = %.0e, gamma/|K|' % (S, t[0]))
    a2.axvline(0.5, color='gray', lw=0.6)
    a2.set_xlabel('c')
    a2.set_ylabel('gamma / |K| bei kleinem k')
    a2.set_title('Vergleich mit der Horava-Formel bei kleinem k')
    a2.legend(fontsize=7)
    # (d) Zusammensetzung
    a3 = ax[1, 1]
    cm = cc[np.abs(1 - 2 * cc) > 1e-3]
    a3.semilogy(cm, 1.0 / (1.0 + 2 * cm ** 2 / (1 - 2 * cm) ** 2), 'k--', lw=1,
                label='Schreibtisch: a_T^2/|a|^2 = 1/(1 + 2c^2/(1-2c)^2)')
    for S, col in (('P0', '#1f77b4'), ('P1', '#ff7f0e')):
        xs, ys, ye = [], [], []
        for cn in C_NAMEN:
            z = fr[S][cn].get('zerlegung')
            if z:
                xs.append(C_WERT[cn])
                ys.append(z['a_seite']['skalar'])
                ye.append(z['E_seite']['eich23'])
        a3.semilogy(xs, ys, 'o', color=col, ms=6, label='%s: a-Seite, Anteil Skalarbedingung (Masse)' % S)
        a3.semilogy(xs, ye, '^', color=col, ms=6, mfc='none', label='%s: E-Seite, Anteil Eichrichtung Gl. 23' % S)
    a3.axvline(0.5, color='gray', lw=0.6)
    a3.set_xlabel('c')
    a3.set_ylabel('Anteil am schnellsten wachsenden Modus')
    a3.set_title('Zusammensetzung des wachsenden Modus (frei)')
    a3.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(lauf, 'bild-wachstum.png'), dpi=120)
    plt.close(fig)
    # G_eff
    fig, ax = plt.subplots(1, 2, figsize=(12.5, 4.6))
    farben = {'100': '#1f77b4', '110': '#d62728', '111': '#2ca02c'}
    for nm in STRAHLEN:
        rs, us = strahl(Ukorr, nm, 2.0, 16.5)
        ax[0].plot(rs, -us * 8 * np.pi * rs, 'o-', color=farben[nm], ms=4, label='[%s], torus-korrigiert' % nm)
    ax[0].axhline(1.0, color='k', lw=0.8)
    ax[0].axhspan(1 - L0_TOL, 1 + L0_TOL, color='gray', alpha=0.2, label='+- 1 %')
    ax[0].axvline(8, color='gray', lw=0.5, ls=':')
    ax[0].set_xlabel('r (Gitterabstaende)')
    ax[0].set_ylabel('-U(r) 8 pi r   (g = m = 1)')
    ax[0].set_title('Statik (c-unabhaengig [M]): U(r) gegen -1/(8 pi r)')
    ax[0].legend(fontsize=8)
    ax[1].plot(cs, [8 * np.pi * G for _ in C_NAMEN], 'o', color='#9467bd', ms=7, label='8 pi G_eff(c), Ausgleich 8 <= r <= 16')
    ax[1].axhline(1.0, color='k', lw=0.8, label='1/(8 pi) (Newton-Wert des N-Typs)')
    ax[1].axhspan(1 - L4_TOL, 1 + L4_TOL, color='gray', alpha=0.2, label='+- 1 %')
    ax[1].axvline(0.5, color='gray', lw=0.6)
    ax[1].set_ylim(0.97, 1.03)
    ax[1].set_xlabel('c (lambda = c/(3c-1))')
    ax[1].set_ylabel('8 pi G_eff')
    ax[1].set_title('Statische Anziehung gleicher Massen gegen c')
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(lauf, 'bild-geff.png'), dpi=120)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--dateien', default='statik-64-128-192,statik-256')
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
    with open(os.path.join(a.lauf, 'scan.json')) as f:
        scj = json.load(f)
    sc = scj['scan']
    with open(os.path.join(a.lauf, 'kontrolle.json')) as f:
        ko = json.load(f)
    erg = {'erzeugt_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           'skript_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
           'quell_sha256': sorted(set(v['info']['skript_sha256'] for v in info.values()) |
                                  {scj['info']['skript_sha256'], ko['info']['skript_sha256']}),
           'urteile': {}, 'tabellen': {}, 'kontrollen': {}}
    Ukorr, _, _ = korrigiert(U, 'N', LKORR)
    Ualt, _, _ = korrigiert(U, 'N', LALT)
    fr, zw, di, ph, sv = sc['frei'], sc['zwang'], sc['dirac'], sc['phys'], sc['statik_voll']
    # ---------------------------------------------------------------- L0
    dyn0 = {S: {'neg_rel_max': fr[S]['0.50']['neg_rel_max'], 'im_rel_max': fr[S]['0.50']['im_rel_max'],
                'wachsend': fr[S]['0.50']['anzahl_q_wachsend'] > 0} for S in ALLE}
    dyn0['phys'] = {'wachsend': ph['0.50']['anzahl_q_wachsend'] > 0}
    kein = not any(v['wachsend'] for v in dyn0.values())
    rest = max(max(dyn0[S]['neg_rel_max'], dyn0[S]['im_rel_max']) for S in ALLE)
    r8, u8 = schale(Ukorr, 8.0, 16.0)
    abw8 = float(np.abs(u8 * 8 * np.pi * r8 + 1).max())
    r4, u4 = schale(Ukorr, 4.0, 16.0)
    abw4 = float(np.abs(u4 * 8 * np.pi * r4 + 1).max())
    _, u8alt = schale(Ualt, 8.0, 16.0)
    w0 = {'dynamik_c0.50': dyn0, 'rest_max': rest, 'kein_exponentielles_wachstum': kein,
          'abw_U_8pi_r_r>=8': abw8, 'abw_U_8pi_r_r>=4': abw4,
          'unsicherheit_torus_rel_max_r>=8': float(np.abs((u8 - u8alt) / u8).max()),
          'exakt_c0.50': {S: {k: ko['exakt_c']['saetze'][S]['0.50'][k] for k in
                              ('alle_gleich_formel', 'punkte_mit_negativer_wurzel', 'punkte_mit_nicht_reeller_wurzel')}
                          for S in FREI}}
    tvgl = os.path.join(a.lauf, 'tensor-eis-n-auswertung.json')
    if os.path.exists(tvgl):
        with open(tvgl) as f:
            tv = json.load(f)
        abw = []
        for row in tv['tabellen']['strahlen']['N']:
            v = tuple(row['v'])
            abw.append(abs(float(Ukorr[v]) - row['U_korr']) / abs(row['U_korr']))
        w0['vergleich_tensor_eis_n_U_korr_rel_max'] = float(max(abw))
        w0['vergleich_tensor_eis_n_n'] = len(abw)
    u0 = 'eingetroffen' if (kein and rest < TAU and abw8 <= L0_TOL) else 'nicht eingetroffen'
    erg['urteile']['L0'] = {'urteil': u0, 'werte': w0}
    # ---------------------------------------------------------------- L1
    l1 = {}
    for S in FREI:
        g = {cn: fr[S][cn]['gamma_max'] for cn in C_NAMEN}
        wachs = {cn: bool(g[cn] > 0) for cn in L1_WACHS}
        if all(g[cn] > 0 for cn in L1_FIT):
            x = np.log([0.5 - C_WERT[cn] for cn in L1_FIT])
            p = float(np.polyfit(x, np.log([g[cn] for cn in L1_FIT]), 1)[0])
        else:
            p = None
        gk = {cn: fr[S][cn]['gamma_q_min'] for cn in L1_FIT}
        pk = float(np.polyfit(np.log([0.5 - C_WERT[cn] for cn in L1_FIT]), np.log([gk[cn] for cn in L1_FIT]), 1)[0]) \
            if all(v > 0 for v in gk.values()) else None
        ok = all(wachs.values()) and (p is not None) and (L1_FENSTER[0] <= p <= L1_FENSTER[1])
        l1[S] = {'erfuellt': bool(ok), 'wachstum_bei': wachs, 'exponent_gamma_max': p, 'gamma_max': g,
                 'exponent_kleinstes_q_beschreibend': pk,
                 'ort_q_stern': {cn: fr[S][cn]['q_stern'] for cn in L1_WACHS},
                 'K2_stern': {cn: fr[S][cn]['K2_stern'] for cn in L1_WACHS}}
    n_ok = sum(l1[S]['erfuellt'] for S in FREI)
    u1 = 'eingetroffen' if n_ok == len(FREI) else 'nicht eingetroffen'
    erg['urteile']['L1'] = {'urteil': u1, 'werte': l1,
                            'vermerk': None if n_ok in (0, len(FREI)) else 'nur in einem Satz erfuellt (Regel: beide noetig)'}
    # ---------------------------------------------------------------- L2
    l2 = {}
    for S in FREI:
        gm, gp = fr[S][L2_PAAR[0]]['gamma_max'], fr[S][L2_PAAR[1]]['gamma_max']
        mx, mn = max(gm, gp), min(gm, gp)
        d_max = abs(gp - gm) / mx if mx > 0 else 0.0
        l2[S] = {'gamma_0.45': gm, 'gamma_0.55': gp, 'delta_rel_zum_groesseren': d_max,
                 'delta_rel_zum_kleineren': (abs(gp - gm) / mn) if mn > 0 else None,
                 'delta_rel_zum_mittel': (abs(gp - gm) / (0.5 * (gp + gm))) if (gp + gm) > 0 else 0.0,
                 'erfuellt': bool(d_max > L2_SCHWELLE)}
    n_ok = sum(l2[S]['erfuellt'] for S in FREI)
    u2 = 'eingetroffen' if n_ok == len(FREI) else 'nicht eingetroffen'
    erg['urteile']['L2'] = {'urteil': u2, 'werte': l2,
                            'vermerk': None if n_ok in (0, len(FREI)) else 'nur in einem Satz erfuellt (Regel: beide noetig)'}
    # ---------------------------------------------------------------- L3
    z_w = {S: {cn: zw[S][cn]['anzahl_q_wachsend'] for cn in C_NAMEN} for S in FREI}
    d_w = {S: {cn: di[S][cn]['anzahl_q_wachsend'] for cn in C_NAMEN} for S in FREI}
    p_w = {cn: ph[cn]['anzahl_q_wachsend'] for cn in C_NAMEN}
    z_any = any(v > 0 for S in FREI for v in z_w[S].values())
    d_any = any(v > 0 for S in FREI for v in d_w[S].values())
    p_any = any(v > 0 for v in p_w.values())
    off = {S: {cn: fr[S][cn]['zerlegung']['gesamt']['f_off'] for cn in C_NAMEN if fr[S][cn]['gamma_max'] > 0}
           for S in FREI}
    hat_w = any(len(off[S]) > 0 for S in FREI)
    neben = all(v > TOL_OFF for S in FREI for v in off[S].values())
    if (z_any != d_any) or (p_any and not z_any):
        u3, v3 = 'nicht auswertbar', 'Projektion, Dirac-Unterraum und TT-Dynamik widersprechen sich.'
    elif (not z_any) and neben:
        u3, v3 = 'eingetroffen', (None if hat_w else 'kein freier Wachstumsmodus: zweiter Teil leer')
    else:
        u3, v3 = 'nicht eingetroffen', None
    w3 = {'projektion_q_wachsend': z_w, 'dirac_q_wachsend': d_w, 'tt_q_wachsend': p_w,
          'projektion_neg_rel_max': {S: max(max(zw[S][cn]['w2_E']['neg_rel_max'], zw[S][cn]['w2_a']['neg_rel_max'])
                                            for cn in C_NAMEN) for S in FREI},
          'projektion_im_rel_max': {S: max(max(zw[S][cn]['w2_E']['im_rel_max'], zw[S][cn]['w2_a']['im_rel_max'])
                                           for cn in C_NAMEN) for S in FREI},
          'D8_re_max_rel': {S: max(zw[S][cn]['D8_re_max_rel'] for cn in C_NAMEN) for S in FREI},
          'dirac_dim': {S: {cn: di[S][cn]['dim'] for cn in C_NAMEN} for S in FREI},
          'dirac_einheitlich': all(di[S][cn]['einheitlich'] for S in FREI for cn in C_NAMEN),
          'invarianz_defekt_rel_max': {cn: zw['P0'][cn]['invarianz_defekt_rel_max'] for cn in C_NAMEN},
          'f_off_wachsender_modus': off, 'f_off_min': min([v for S in FREI for v in off[S].values()] or [None]),
          'energie_auf_Z': {S: {cn: zw[S][cn]['energie_Z'] for cn in C_NAMEN} for S in FREI}}
    erg['urteile']['L3'] = {'urteil': u3, 'werte': w3, 'vermerk': v3}
    # ---------------------------------------------------------------- L4
    G, rest_fit, nfit = geff(Ukorr)
    Galt, _, _ = geff(Ualt)
    neg, kraft, umax, umin = anziehung(Ukorr)
    kern = {cn: sv[cn]['kap_abw_rel_max'] for cn in C_NAMEN}
    Erel = {cn: sv[cn]['E_max'] / sv['kap_skala'] for cn in C_NAMEN}
    kern_ok = (max(kern.values()) <= TOL_KERN) and (max(Erel.values()) <= TOL_KERN)
    Gc = {cn: G for cn in C_NAMEN}
    sprung = max(abs(Gc[C_NAMEN[i + 1]] - Gc[C_NAMEN[i]]) for i in range(len(C_NAMEN) - 1)) / G
    anz = neg and all(kraft.values())
    gleich = abs(8 * np.pi * G - 1) <= L4_TOL
    if not kern_ok:
        u4, v4 = 'nicht auswertbar', 'c-Unabhaengigkeit des statischen Problems numerisch nicht bestaetigt.'
    elif anz and G > 0 and sprung <= L4_SPRUNG and gleich:
        u4, v4 = 'eingetroffen', 'vorab ableitbar [M]: c tritt in der Statik nicht auf (PLAN Abschnitt 3).'
    else:
        u4, v4 = 'nicht eingetroffen', None
    erg['urteile']['L4'] = {'urteil': u4, 'vermerk': v4, 'werte': {
        'G_eff_c': Gc, '8pi_G_eff_halb': 8 * np.pi * G, 'G_eff_alt_anpassung': Galt, 'ausgleich_rest_rel': rest_fit,
        'ausgleich_punkte': nfit, 'sprung_max_rel': sprung, 'U<0_2_16': neg, 'kraft_anziehend_strahlen': kraft,
        'U_max_2_16': umax, 'U_min_2_16': umin, 'kern_abw_rel_max_je_c': kern, 'E_max_rel_je_c': Erel,
        'statik_voll_gitter': {'L': sv['L'], 'nzufall': sv['nzufall'], 'nq': sv['nq']},
        'statik_minimum_auf_Z_beschreibend': {cn: bool(zw['P0'][cn]['energie_Z']['A_neg_anteil'] == 0.0 and
                                                       zw['P0'][cn]['energie_Z']['B_neg_anteil'] == 0.0) for cn in C_NAMEN}}}
    # ---------------------------------------------------------------- Tabellen
    tab = []
    for cn in C_NAMEN:
        row = {'c': cn, 'lambda': sc['lambda_hl'][cn], 'HL_(lam-1)/(3lam-1)': None if sc['lambda_hl'][cn] is None else
               (sc['lambda_hl'][cn] - 1) / (3 * sc['lambda_hl'][cn] - 1), '1-2c': 1 - 2 * C_WERT[cn]}
        for S in ALLE:
            row['gamma_max_' + S] = fr[S][cn]['gamma_max']
        for S in FREI:
            r = fr[S][cn]
            row[S] = {'q_stern': r['q_stern'], 'K2_stern': r['K2_stern'], 'anteil_q_wachsend': r['anteil_q_wachsend'],
                      'formel_abw_rel_max': r['formel_abw_rel_max'], 'gamma_q_min': r['gamma_q_min'],
                      'gamma_q_min_ueber_K': r['gamma_q_min'] / r['K_q_min'],
                      'linie100_gamma_ueber_K_bei_t0': sc['linien']['100'][S][cn]['gamma'][0] / (2 * np.sin(sc['linien']['t'][0] / 2)),
                      'linie_formel_abw_rel_max': max(sc['linien']['100'][S][cn]['formel_abw_rel_max'],
                                                      sc['linien']['111'][S][cn]['formel_abw_rel_max']),
                      'hl_gamma_max_formel_gitter': sc['hl'][S][cn]['gamma_max_formel_gitter'],
                      'hl_ir_koeff': sc['hl'][S][cn]['hl_ir_koeff'],
                      'zerlegung': r.get('zerlegung'),
                      'zwang_gamma_max': zw[S][cn]['gamma_max'], 'dirac_dim': di[S][cn]['dim'],
                      'dirac_gamma_max': di[S][cn]['gamma_max']}
        tab.append(row)
    erg['tabellen']['c_scan'] = tab
    erg['tabellen']['formel_abw_rel_max_alle_saetze'] = {S: {cn: fr[S][cn]['formel_abw_rel_max'] for cn in C_NAMEN} for S in ALLE}
    # ---------------------------------------------------------------- Kontrollen
    kon = {'ortsraum_L6_c0.50': ko['ortsraum'], 'ortsraum_c': ko['ortsraum_c'], 'gw_s19': ko['gw_s19'],
           'exakt_c0.50_alt': {k: {kk: vv for kk, vv in v.items() if kk != 'beispiel_punkt0'} for k, v in ko['exakt']['saetze'].items()},
           'exakt_c': {S: {cn: {k: v for k, v in ko['exakt_c']['saetze'][S][cn].items() if k != 'zeilen'} for cn in C_NAMEN}
                       for S in FREI},
           'exakt_c_beispiel': {S: {cn: ko['exakt_c']['saetze'][S][cn]['zeilen'][0] for cn in ('0.45', '0.50', '0.55')} for S in FREI},
           'exakt_punkte': ko['exakt_c']['punkte'],
           'scan_kontr_Z': sc['kontr_Z'], 'phys_tt': ph, 'statik_voll': sv}
    for name, js in info.items():
        for l in js['laeufe']:
            kon['statik_L%d' % l['L']] = {'stat': l['stat'], 'sym': l['sym'], 't_s': l['t_gesamt_s'], 'kap_q0': l['kap_q0']}
    erg['kontrollen'] = kon
    with open(a.out + '.tmp', 'w') as f:
        json.dump(erg, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    bilder(sc, Ukorr, G, a.lauf)
    print('Urteile:', {k: v['urteil'] for k, v in erg['urteile'].items()})
    print('fertig auswertung %.1f s' % (time.time() - t0), flush=True)


if __name__ == '__main__':
    main()
