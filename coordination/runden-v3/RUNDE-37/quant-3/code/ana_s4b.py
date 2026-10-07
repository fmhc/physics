#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S4B (L = 6): Auswertung streng nach VORAB-S4B.md und VORAB-S4B-AUSWERTUNG.md (claude, 06.10.2026).

Neue Datei. ana.py bleibt unveraendert und wird als Modul benutzt (jk, lade, cosh_meff, sigma_ng, M_FAM, kopf).
Nur ueber kleintest.sh auf der .69 (CPU, numpy).

  ana_s4b.py beta  --tab T1.json [T2.json ...] [--haupt m5-n6t4] [--nt6 b2-n6t6] --out AUS.json
      beta_c aus den chi_L-Zeilen von `ana.py tab` (Regeln A.1 bis A.5): je Lauf und Teilmenge heiss / kalt / beide,
      Parabel durch Maximum und zwei Nachbarn; Querproben: drei hoechste Punkte, fuenf Punkte.
  ana_s4b.py sigma --ein LAUF1 LAUF2 LAUF3 --beta 3.30 [--betac-json AUS.json] [--korr-json ana-korr.json] --out AUS2.json
      sigma_NG aus den Multihit-Korrelatoren (Familie 111, Fenster D = 1..L/2, relative Abweichungen wie in ana.py korr),
      Fehler aus dem Jackknife von E (Fortpflanzung) und direkter Jackknife von sigma; gewichtetes Mittel ueber Nt;
      Q = T_c/Wurzel(sigma), T_c = 1/(4 tau); Fehlerquelle beta-Abweichung (Regeln B und C).
"""
import argparse
import itertools
import json
import os
import sys
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import ana  # noqa: E402  (unveraendert, als Modul)

T0 = time.time()


def fl(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return x if np.isfinite(x) else None


def kopf():
    k = ana.kopf()
    k['ana_s4b_sha256'] = ana.sha(os.path.abspath(__file__))
    k['ana_sha256'] = ana.sha(os.path.join(HIER, 'ana.py'))
    return k


# ================================================================================================ beta_c
def parabel(x, y, ye, gew=False, nz=4000):
    """Parabel durch die Punkte; Scheitel am Punkt und aus nz Gauss-Ziehungen mit den Fehlern ye (Seed 1)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    ye = np.asarray(ye, float)
    rng = np.random.default_rng(1)

    def fit(yy):
        return np.polyfit(x, yy, 2, w=(1.0 / ye) if gew else None)
    A0 = fit(y)
    v0 = -A0[1] / (2.0 * A0[0]) if A0[0] < 0 else np.nan
    Z = y[None, :] + ye[None, :] * rng.standard_normal((nz, len(x)))
    As = np.array([fit(z) for z in Z])
    neg = As[:, 0] < 0
    verts = np.full(nz, np.nan)
    verts[neg] = -As[neg, 1] / (2.0 * As[neg, 0])
    ok = np.isfinite(verts)
    im = bool(np.isfinite(v0) and x.min() <= v0 <= x.max())
    frac = float(neg.mean())
    viel = ok.sum() > 10
    return {'beta': x.tolist(), 'chi': y.tolist(), 'chi_err': ye.tolist(), 'scheitel': fl(v0),
            'anteil_konkav': frac, 'scheitel_std': fl(verts[ok].std()) if viel else None,
            'scheitel_16_84': [fl(np.percentile(verts[ok], 16)), fl(np.percentile(verts[ok], 84))] if viel else None,
            'im_intervall': im, 'signifikant': bool(frac >= 0.95 and im)}


def teilmengen(zeilen):
    rows = [z for z in zeilen if (not z.get('zu_wenig')) and z.get('chiL') is not None and z.get('chiL_err')]
    out = {}
    for name in ('heiss', 'kalt', 'beide'):
        R = [z for z in rows if name == 'beide' or z['start'] == name]
        if len(R) < 3:
            continue
        bs = np.array([z['beta'] for z in R])
        cs = np.array([z['chiL'] for z in R])
        ce = np.array([z['chiL_err'] for z in R])
        ub = np.unique(bs)
        cm = np.array([np.average(cs[bs == b], weights=1.0 / np.maximum(ce[bs == b], 1e-12) ** 2) for b in ub])
        cme = np.array([1.0 / np.sqrt((1.0 / np.maximum(ce[bs == b], 1e-12) ** 2).sum()) for b in ub])
        out[name] = (ub, cm, cme)
    return out


def spitze(ub, cm, cme):
    n = len(ub)
    i = int(np.argmax(cm))
    r = {'n_punkte': n, 'gitterpunkt_max_beta': float(ub[i]), 'gitterpunkt_max_chi': float(cm[i]),
         'beta': ub.tolist(), 'chi': cm.tolist(), 'chi_err': cme.tolist(), 'drei_nachbarn': None,
         'drei_hoechste': None, 'fuenf_punkte': None}
    if 0 < i < n - 1:
        s = slice(i - 1, i + 2)
        r['drei_nachbarn'] = parabel(ub[s], cm[s], cme[s])
        r['fuenf_punkte'] = parabel(ub[max(0, i - 2):min(n, i + 3)], cm[max(0, i - 2):min(n, i + 3)],
                                    cme[max(0, i - 2):min(n, i + 3)], gew=True) if n >= 5 else None
    else:
        r['hinweis'] = 'Maximum am Rand des beta-Bereichs'
    if n >= 3:
        top = np.sort(np.argsort(cm)[-3:])
        r['drei_hoechste'] = parabel(ub[top], cm[top], cme[top])
        r['drei_hoechste_sind_nachbarn'] = bool(0 < i < n - 1 and set(top.tolist()) == {i - 1, i, i + 1})
    return r


def hauptwert(erg):
    """Regeln A.2 bis A.4: Teilmenge beide, drei Nachbarn; Fehler quadratisch mit (heiss - kalt)/2."""
    b = (erg.get('beide') or {}).get('drei_nachbarn')
    if b is None or not b['signifikant']:
        return {'signifikant': False,
                'hinweis': 'Parabel-Regel A.3 nicht erfuellt oder Maximum am Rand; kein beta_c aus chi_L',
                'gitterpunkt_max_beta': (erg.get('beide') or {}).get('gitterpunkt_max_beta')}
    stat = b['scheitel_std']
    h = (erg.get('heiss') or {}).get('drei_nachbarn')
    k = (erg.get('kalt') or {}).get('drei_nachbarn')
    syst = abs(h['scheitel'] - k['scheitel']) / 2.0 if (h and k and h['signifikant'] and k['signifikant']) else None
    err = float(np.sqrt(stat ** 2 + (syst or 0.0) ** 2))
    return {'signifikant': True, 'beta_c': b['scheitel'], 'err_stat': stat, 'err_heiss_kalt': syst, 'err': err,
            'heiss_signifikant': bool(h and h['signifikant']), 'kalt_signifikant': bool(k and k['signifikant']),
            'beta_c_heiss': h['scheitel'] if h else None, 'beta_c_kalt': k['scheitel'] if k else None}


def drucke_zeilen(name, zeilen):
    print('--- %s: Zeilen je beta und Start ---' % name)
    print('%-7s %-6s %9s %8s %8s %7s %6s %9s %7s' % ('beta', 'start', 'chi_L', 'chi_err', '|L|', 'U4', 'tauL', 'P', 'nmess'))
    for z in sorted(zeilen, key=lambda z: (z['beta'], z['start'])):
        if z.get('zu_wenig'):
            print('%-7.4f %-6s zu wenig Messungen' % (z['beta'], z['start']))
            continue
        n = float('nan')
        print('%-7.4f %-6s %9.3f %8.3f %8.4f %7.3f %6.1f %9.5f %7d' % (
            z['beta'], z['start'], z['chiL'], z['chiL_err'], z['absL'],
            n if z['binder'] is None else z['binder'], n if z['tau_int_absL'] is None else z['tau_int_absL'],
            z['pw'], z['nmess']))


def zeige(name, k, v):
    if v is None:
        print('  %-22s -' % k)
        return
    print('  %-22s Scheitel %s  anteil_konkav %.3f  std %s  16-84 %s  im_Intervall %s  SIGNIFIKANT %s  Punkte %s' % (
        k, ('%.4f' % v['scheitel']) if v['scheitel'] is not None else 'keiner', v['anteil_konkav'],
        ('%.4f' % v['scheitel_std']) if v['scheitel_std'] is not None else '-',
        v['scheitel_16_84'], v['im_intervall'], v['signifikant'], v['beta']))


def modus_beta(a):
    out = {'kopf': kopf(), 'laeufe': {}}
    info = {}
    for tp in a.tab:
        with open(tp) as fh:
            tj = json.load(fh)
        for d in tj['laeufe']:
            name = d['datei']
            drucke_zeilen(name, d['zeilen'])
            tm = teilmengen(d['zeilen'])
            erg = {}
            print('=== %s (L %d, Nt %d): beta_c aus chi_L ===' % (name, d['L'], d['Nt']))
            for sub, (ub, cm, cme) in tm.items():
                erg[sub] = spitze(ub, cm, cme)
                print(' Teilmenge %s: chi(beta) = %s' % (sub, ', '.join('%.3f:%.1f+-%.1f' % t for t in zip(ub, cm, cme))))
                print('  Gitterpunkt-Maximum bei beta %.4f (chi %.2f)' % (erg[sub]['gitterpunkt_max_beta'], erg[sub]['gitterpunkt_max_chi']))
                zeige(name, 'drei Nachbarn', erg[sub]['drei_nachbarn'])
                zeige(name, 'drei hoechste', erg[sub]['drei_hoechste'])
                if erg[sub]['drei_hoechste'] is not None:
                    print('  (drei hoechste = drei Nachbarn: %s)' % erg[sub].get('drei_hoechste_sind_nachbarn'))
                zeige(name, 'fuenf Punkte (gew.)', erg[sub]['fuenf_punkte'])
            hw = hauptwert(erg)
            print(' HAUPTWERT %s:' % name, json.dumps(hw))
            out['laeufe'][name] = {'L': d['L'], 'Nt': d['Nt'], 'teilmengen': erg, 'hauptwert': hw}
            info[name] = (d['Nt'], hw)
    out['haupt_lauf'] = a.haupt
    out['beta_c_haupt'] = info.get(a.haupt, (None, None))[1]
    emp = {'hinweis': 'nicht bestimmbar'}
    if a.nt6 and a.nt6 in info and a.haupt in info:
        (nt1, h1), (nt2, h2) = info[a.haupt], info[a.nt6]
        if h1 and h2 and h1.get('signifikant') and h2.get('signifikant'):
            s = 2.0 * np.log(nt1 / nt2) / (h2['beta_c'] - h1['beta_c'])
            emp = {'s_emp': float(s), 'Nt1': nt1, 'beta_c1': h1['beta_c'], 'Nt2': nt2, 'beta_c2': h2['beta_c'],
                   'hinweis': 'a ~ 1/Nt am Uebergang, feste Anisotropie tau angenommen; grob'}
    out['steigung_empirisch'] = emp
    print('STEIGUNG empirisch:', json.dumps(emp))
    out['zeit_s'] = time.time() - T0
    with open(a.out, 'w') as fh:
        json.dump(out, fh, indent=1)


# ================================================================================================ sigma
def fitm(v, L, Dmin):
    """Wie in ana.py korr: A cosh(m (D - L/2)), D = Dmin..L/2, relative Abweichungen, Gittersuche in m, A linear."""
    D = np.arange(Dmin, L // 2 + 1)
    y = v[D]
    if (y <= 0).any():
        return np.nan
    best = (np.inf, np.nan)
    for mm in np.linspace(0.01, 12.0, 2400):
        c = np.cosh(mm * (D - L / 2.0))
        A = (y * c).sum() / (c * c).sum()
        ch = (((y - A * c) / y) ** 2).sum()
        if ch < best[0]:
            best = (ch, mm)
    return best[1]


def jk_robust(bins, fun):
    n = len(bins)
    full = fun(bins.mean(0))
    js = np.array([fun(np.delete(bins, i, 0).mean(0)) for i in range(n)], float)
    ok = np.isfinite(js)
    nv = int(ok.sum())
    if nv < 3 or not np.isfinite(full):
        return full, np.nan, nv, js
    jv = js[ok]
    return full, float(np.sqrt((nv - 1) / nv * ((jv - jv.mean()) ** 2).sum())), nv, js


def dsig_dE(E, Lt):
    return 2.0 * E / np.sqrt((2 * np.pi / 3) ** 2 + 4 * Lt ** 2 * E ** 2)


def lag1(x):
    x = np.asarray(x, float)
    x = x - x.mean()
    d = (x * x).sum()
    return float((x[:-1] * x[1:]).sum() / d) if d > 0 else None


def sigma_lauf(p, dmin):
    res, z = ana.lade(p)
    L, Nt, tau, NV = res['L'], res['Nt'], res['tau'], res['NV']
    Lt = Nt * tau
    box = np.array(res['box'])
    AV = box / L
    Bv = np.linalg.inv(AV).T
    dn = np.array(list(itertools.product(range(L), range(L), range(L))))
    K = z['kor_0']
    nb, R = K.shape[0], K.shape[1]
    if R != 1:
        raise RuntimeError('erwartet R = 1')
    Csum = K[:, 0].reshape((nb, NV, NV, L ** 3)).sum(axis=(1, 2))
    st = res['stufen'][0]
    out = {'datei': os.path.basename(p), 'L': L, 'Nt': Nt, 'tau': tau, 'L_t': Lt, 'beta': st['betas'][0],
           'nmess': st['nmess'], 'bins': nb, 'familien': {}}
    for fam in ('111', '100'):
        Sm = []
        dm = []
        for m in ana.M_FAM[fam]:
            idx = (dn @ np.array(m)) % L
            Sm.append(np.stack([np.bincount(idx, Csum[i], minlength=L) for i in range(nb)]))
            dm.append(1.0 / np.linalg.norm(np.array(m) @ Bv))
        Sm = np.mean(Sm, axis=0)                         # (nb, L)
        dfam = float(np.mean(dm))
        mS, eS, _ = ana.jk(Sm, lambda v: v)
        mf, mfe, nvm, _ = jk_robust(Sm, lambda v: fitm(v, L, dmin))
        E = mf / dfam if np.isfinite(mf) else np.nan
        Ee = mfe / dfam if np.isfinite(mfe) else np.nan
        sg = float(ana.sigma_ng(E, Lt)) if np.isfinite(E) else np.nan
        sg_prop = float(abs(dsig_dE(E, Lt)) * Ee) if np.isfinite(E) and np.isfinite(Ee) else np.nan
        sgd, sgde, nvs, _ = jk_robust(Sm, lambda v: float(ana.sigma_ng(fitm(v, L, dmin) / dfam, Lt)))
        # Anpassungsgute in Fehlereinheiten (1 Freiheitsgrad bei L = 6, D = 1..3)
        pulls = None
        A = None
        if np.isfinite(mf):
            D = np.arange(dmin, L // 2 + 1)
            c = np.cosh(mf * (D - L / 2.0))
            A = float((mS[D] * c).sum() / (c * c).sum())   # Amplitude wie im Fit von ana.py (linear, ohne Gewicht)
            pulls = ((mS[D] - A * c) / eS[D]).tolist()
        meff = []
        for D in range(1, L // 2):
            m0, me, nv, _ = jk_robust(Sm, lambda v, D=D: ana.cosh_meff(v[D] / v[D + 1], L, D))
            E0 = m0 / dfam if np.isfinite(m0) else np.nan
            Ee0 = me / dfam if np.isfinite(me) else np.nan
            s0 = float(ana.sigma_ng(E0, Lt)) if np.isfinite(E0) else np.nan
            se0 = float(abs(dsig_dE(E0, Lt)) * Ee0) if np.isfinite(E0) and np.isfinite(Ee0) else np.nan
            meff.append({'Delta': D, 'E': fl(E0), 'E_err': fl(Ee0), 'sigma_NG': fl(s0), 'sigma_NG_err': fl(se0),
                         'gueltige_jackknife_proben': nv})
        rand = bool(np.isfinite(mf) and (mf >= 11.99 or mf <= 0.0101))
        out['familien'][fam] = {
            'd': dfam, 'S': mS.tolist(), 'S_err': eS.tolist(), 'S_rel_err': (eS / np.abs(mS)).tolist(),
            'fit_Dmin': dmin, 'fit_m': fl(mf), 'fit_m_err': fl(mfe), 'fit_E': fl(E), 'fit_E_err': fl(Ee),
            'jackknife_proben_E': nvm, 'sigma_NG': fl(sg), 'sigma_NG_err_fortpflanzung': fl(sg_prop),
            'sigma_NG_jackknife_direkt': fl(sgd), 'sigma_NG_err_jackknife_direkt': fl(sgde),
            'jackknife_proben_sigma': nvs, 'fit_am_rand_des_gitters': rand, 'A': A, 'pulls_D': pulls,
            'meff': meff, 'lag1_binmittel': {str(D): lag1(Sm[:, D]) for D in range(0, L // 2 + 1)}}
        out.setdefault('_Sm', {})[fam] = Sm
    pw = z['pw_0'][:, 0]
    out['pw_zeitreihe'] = pw
    return out


def gmittel(sig, err):
    sig = np.asarray(sig, float)
    err = np.asarray(err, float)
    w = 1.0 / err ** 2
    m = float((w * sig).sum() / w.sum())
    e = float(1.0 / np.sqrt(w.sum()))
    chi2 = float((w * (sig - m) ** 2).sum())
    dof = len(sig) - 1
    skal = max(1.0, float(np.sqrt(chi2 / dof))) if dof > 0 else 1.0
    return {'mittel': m, 'err_roh': e, 'chi2': chi2, 'dof': dof, 'skalierung': skal, 'err': e * skal}


def beta_quelle(Q, beta_run, bc_json, s_emp_json, extra_err=0.01):
    """Regel C.2 und Nachtrag Punkt 3: relative Aenderung von Q durch beta_c - beta_run; s = d ln(sigma a^2)/d beta.
    Zwei Fehler von beta_c: der Regelfehler und die Streuung der Teilergebnisse (extra_err, Vorab-Nachtrag)."""
    b0 = 11.0 * 2 / (48 * np.pi ** 2)
    b1 = (34.0 / 3.0) * (2 / (16 * np.pi ** 2)) ** 2
    s_as = 2.0 * ((b1 / (2 * b0 ** 2)) / beta_run - 1.0 / (8 * b0))
    s_emp = (s_emp_json or {}).get('s_emp')
    r = {'s_AS_zwei_schleifen': float(s_as), 's_emp': s_emp,
         'Q_aenderung_je_0.01_beta_AS_prozent': float(100 * (np.exp(-0.5 * s_as * 0.01) - 1)),
         'Q_aenderung_je_0.01_beta_emp_prozent': float(100 * (np.exp(-0.5 * s_emp * 0.01) - 1)) if s_emp else None}
    if not bc_json or not bc_json.get('signifikant'):
        r['hinweis'] = 'kein beta_c aus chi_L belegt; nur Empfindlichkeit je 0,01 in beta angebbar'
        return r
    dbeta = bc_json['beta_c'] - beta_run
    smax = max(abs(s_as), abs(s_emp) if s_emp else 0.0)
    smin = min(abs(s_as), abs(s_emp)) if s_emp else abs(s_as)
    r.update({'beta_c': bc_json['beta_c'], 'beta_c_err_regel': bc_json['err'], 'beta_c_err_streuung': extra_err,
              'dbeta': float(dbeta), 's_verwendet_betrag': float(smax)})
    for tag, e in (('regel', bc_json['err']), ('streuung', extra_err)):
        deff = float(np.sqrt(dbeta ** 2 + e ** 2))
        r['dbeta_eff_' + tag] = deff
        r['rel_quelle_gross_' + tag] = float(0.5 * smax * deff)
        r['rel_quelle_klein_' + tag] = float(0.5 * smin * deff)
    r['richtung'] = 'Q(beta_c) = Q(3,30) mal exp(-s/2 (beta_c - 3,30)); bei beta_c < 3,30 und s < 0 also kleiner'
    r['Q_faktor_bei_beta_c_AS'] = float(np.exp(-0.5 * s_as * dbeta))
    if Q is not None:
        r['Q_bei_beta_c_AS'] = float(Q * np.exp(-0.5 * s_as * dbeta))
        r['Q_bei_beta_c_emp'] = float(Q * np.exp(-0.5 * s_emp * dbeta)) if s_emp else None
    return r


# ================================================================================================ Zusatz Z1
GRID = np.arange(0.30, 6.0 + 1e-9, 0.005)


def chi2_gem(sig, daten):
    """Zusatz Z1 (nach Sicht): chi^2 eines gemeinsamen Nambu-Goto-Fits, Amplitude je Lauf analytisch."""
    tot = 0.0
    for (Lt, d, L, D, y, e) in daten:
        E2 = sig ** 2 * Lt ** 2 - (2 * np.pi / 3) * sig
        if E2 < 0:
            return np.inf
        c = np.cosh(np.sqrt(E2) * d * (D - L / 2.0))
        w = 1.0 / e ** 2
        A = (w * y * c).sum() / (w * c * c).sum()
        tot += (w * (y - A * c) ** 2).sum()
    return float(tot)


def profil(daten):
    return np.array([chi2_gem(s, daten) for s in GRID])


def bester(chi):
    i = int(np.argmin(chi))
    ok = np.isfinite(chi)
    band = GRID[ok & (chi <= chi[i] + 1.0)]
    return {'sigma': float(GRID[i]), 'chi2': float(chi[i]), 'am_gitterrand': bool(i in (0, len(GRID) - 1)),
            'band_delta_chi2_1': [float(band.min()), float(band.max())],
            'band_beruehrt_gitterrand': bool(band.max() >= GRID[-1] - 1e-9 or band.min() <= GRID[0] + 1e-9)}


def z1_fit(laeufe, Sms, fam, auswahl, Tc):
    """gemeinsamer Fit ueber die Laeufe in `auswahl` (Dateinamen); Jackknife ueber die Bins (Gewichte fest)."""
    D_des = {}
    daten = []
    sm_list = []
    for l in laeufe:
        if l['datei'] not in auswahl:
            continue
        f = l['familien'][fam]
        L = l['L']
        D = np.arange(1, L // 2 + 1)
        S = np.array(f['S'])
        Se = np.array(f['S_err'])
        daten.append((l['L_t'], f['d'], L, D, S[D], Se[D]))
        sm_list.append((Sms[l['datei']][fam], l['L_t'], f['d'], L, D, Se[D]))
    chi = profil(daten)
    r = bester(chi)
    npar = len(daten) + 1
    npts = sum(len(t[3]) for t in daten)
    r['dof'] = npts - npar
    nb = sm_list[0][0].shape[0]
    js = []
    for i in range(nb):
        dd = []
        for (Sm, Lt, d, L, D, Se) in sm_list:
            dd.append((Lt, d, L, D, np.delete(Sm, i, 0).mean(0)[D], Se))
        js.append(GRID[int(np.argmin(profil(dd)))])
    js = np.array(js)
    r['sigma_jackknife_err'] = float(np.sqrt((nb - 1) / nb * ((js - js.mean()) ** 2).sum()))
    r['sigma_jackknife_min_max'] = [float(js.min()), float(js.max())]
    r['Q'] = float(Tc / np.sqrt(r['sigma']))
    lo, hi = r['band_delta_chi2_1']
    r['Q_band_delta_chi2_1'] = [float(Tc / np.sqrt(hi)), float(Tc / np.sqrt(lo))]
    r['Q_jackknife_err'] = float(r['Q'] * 0.5 * r['sigma_jackknife_err'] / r['sigma'])
    r['laeufe'] = sorted(auswahl)
    return r


def modus_sigma(a):
    out = {'kopf': kopf(), 'beta_lauf': a.beta, 'dmin': a.dmin, 'laeufe': []}
    laeufe = [sigma_lauf(p, a.dmin) for p in a.ein]
    korr_ref = None
    if a.korr_json:
        with open(a.korr_json) as fh:
            korr_ref = json.load(fh)
    pws = []
    Sms = {}
    for l in laeufe:
        pws.append(np.asarray(l.pop('pw_zeitreihe'), float))
        Sms[l['datei']] = l.pop('_Sm')
        f = l['familien']['111']
        if korr_ref is not None:
            for d in korr_ref['laeufe']:
                if d['datei'] == l['datei']:
                    ref = d['stufen'][0]['familien']['111']
                    l['abgleich_ana_korr_111'] = {'fit_m_ana': ref['fit_m'], 'fit_m_hier': f['fit_m'],
                                                  'fit_m_err_ana': ref['fit_m_err'], 'fit_m_err_hier': f['fit_m_err'],
                                                  'fit_sigma_NG_ana': ref['fit_sigma_NG'], 'sigma_NG_hier': f['sigma_NG']}
        print('=== %s: L %d Nt %d beta %.3f L_t %.4f, %d Bins, %d Messungen ===' % (
            l['datei'], l['L'], l['Nt'], l['beta'], l['L_t'], l['bins'], l['nmess']))
        for fam, ff in l['familien'].items():
            print(' Familie %s (d = %.4f): S(D) = %s' % (fam, ff['d'], ' '.join(
                'D%d %.4e(%.1e,%.0f%%)' % (D, ff['S'][D], ff['S_err'][D], 100 * ff['S_rel_err'][D])
                for D in range(0, len(ff['S']) // 2 + 1))))
            print('   Fit D=%d..%d: m %s +- %s  E %s +- %s (Proben %d)  sigma_NG %s  err_fortpfl %s  jk_direkt %s +- %s (Proben %d)  Rand %s' % (
                ff['fit_Dmin'], l['L'] // 2, ff['fit_m'], ff['fit_m_err'], ff['fit_E'], ff['fit_E_err'], ff['jackknife_proben_E'],
                ff['sigma_NG'], ff['sigma_NG_err_fortpflanzung'], ff['sigma_NG_jackknife_direkt'],
                ff['sigma_NG_err_jackknife_direkt'], ff['jackknife_proben_sigma'], ff['fit_am_rand_des_gitters']))
            print('   Anpassung (S - Fit)/S_err fuer D=%d..%d: %s' % (ff['fit_Dmin'], l['L'] // 2, ff['pulls_D']))
            print('   effektive Massen: %s' % ff['meff'])
            print('   lag1 der Bin-Mittel: %s' % ff['lag1_binmittel'])
        if 'abgleich_ana_korr_111' in l:
            print(' Abgleich mit ana.py korr (111):', l['abgleich_ana_korr_111'])
    out['laeufe'] = laeufe
    # Unabhaengigkeit der Laeufe
    if len(pws) > 1 and all(len(p) == len(pws[0]) for p in pws):
        cm = np.corrcoef(np.array(pws))
        out['pearson_plakette_zeitreihen'] = {'dateien': [l['datei'] for l in laeufe], 'matrix': cm.tolist()}
        print('Pearson (Plaketten-Zeitreihen der Laeufe):\n', np.round(cm, 4))
    tau = laeufe[0]['tau']
    Tc = 1.0 / (4.0 * tau)
    out['T_c_in_1_pro_a'] = Tc
    gut = [l for l in laeufe if l['familien']['111']['sigma_NG'] is not None
           and l['familien']['111']['sigma_NG_err_fortpflanzung'] is not None]
    gut_namen = set(l['datei'] for l in gut)
    schlecht = [l['datei'] for l in laeufe if l['datei'] not in gut_namen]
    zus = {'verwendet': sorted(gut_namen), 'nicht_bestimmbar': schlecht, 'T_c': Tc}
    print('T_c = 1/(4 tau) = %.6f /a (tau = %.12f)' % (Tc, tau))
    print('VORAB-ERGEBNIS: bestimmbar (Familie 111, Fenster D=%d..L/2): %s; nicht bestimmbar: %s' % (
        a.dmin, sorted(gut_namen) or '-', schlecht or '-'))
    Q = None
    for l in gut:
        f = l['familien']['111']
        f['Q'] = Tc / np.sqrt(f['sigma_NG'])
        f['Q_err'] = f['Q'] * 0.5 * f['sigma_NG_err_fortpflanzung'] / f['sigma_NG']
        print(' Nt %2d: sigma_NG %.4f +- %.4f -> Q %.4f +- %.4f' % (l['Nt'], f['sigma_NG'], f['sigma_NG_err_fortpflanzung'], f['Q'], f['Q_err']))
    if len(gut) >= 1:
        g = gmittel([l['familien']['111']['sigma_NG'] for l in gut],
                    [l['familien']['111']['sigma_NG_err_fortpflanzung'] for l in gut])
        gd = gmittel([l['familien']['111']['sigma_NG_jackknife_direkt'] for l in gut],
                     [l['familien']['111']['sigma_NG_err_jackknife_direkt'] for l in gut]) \
            if all(l['familien']['111']['sigma_NG_err_jackknife_direkt'] is not None for l in gut) else None
        Q = Tc / np.sqrt(g['mittel'])
        dQ = Q * 0.5 * g['err'] / g['mittel']
        zus.update({'sigma_gemittelt': g, 'sigma_gemittelt_gegenprobe_direkter_jackknife': gd, 'Q': float(Q), 'Q_err': float(dQ),
                    'Q_rel_err': float(dQ / Q), 'Q_im_fenster_0.567_0.851': bool(0.567 <= Q <= 0.851),
                    'Q_band_im_fenster_ueberlappt': bool(Q + dQ >= 0.567 and Q - dQ <= 0.851),
                    'Q_abweichung_von_0.709_prozent': float(100 * (Q / 0.709 - 1))})
        print('GEMITTELT (gewichtet, Fortpflanzung): sigma a^2 = %.4f +- %.4f (roh %.4f, chi2 %.2f / %d, Skal. %.2f)' % (
            g['mittel'], g['err'], g['err_roh'], g['chi2'], g['dof'], g['skalierung']))
        print('  Q = T_c/Wurzel(sigma) = %.4f +- %.4f (%.1f %%)' % (Q, dQ, 100 * dQ / Q))
    else:
        print('KEIN sigma und KEIN Q nach der Vorab-Festlegung (Regel B.3).')
    # beta-Quelle (immer; Q nur, wenn vorhanden)
    bc = emp = None
    if a.betac_json:
        with open(a.betac_json) as fh:
            bj = json.load(fh)
        bc = bj.get('beta_c_haupt')
        emp = bj.get('steigung_empirisch')
    bq = beta_quelle(Q, a.beta, bc, emp)
    zus['beta_quelle'] = bq
    print('BETA-QUELLE:', json.dumps(bq))
    # Zusatz Z2: Signal zu Rausch
    z2 = []
    print('ZUSATZ Z2 (Signal zu Rausch |S|/S_err; D = 1, 2, 3):')
    for l in laeufe:
        for fam in ('111', '100'):
            ff = l['familien'][fam]
            sn = [abs(ff['S'][D]) / ff['S_err'][D] for D in (1, 2, 3)]
            z2.append({'datei': l['datei'], 'familie': fam, 'S': [ff['S'][D] for D in (1, 2, 3)],
                       'S_err': [ff['S_err'][D] for D in (1, 2, 3)], 'S_zu_Rausch': sn,
                       'alle_positiv': bool(all(ff['S'][D] > 0 for D in (1, 2, 3)))})
            print('  %-10s %s  S = %s  S/err = %s  alle positiv: %s' % (
                l['datei'], fam, ['%.3e' % ff['S'][D] for D in (1, 2, 3)], ['%.1f' % x for x in sn], z2[-1]['alle_positiv']))
    zus['zusatz_z2'] = z2
    # Zusatz Z1: gemeinsamer Fit (nach Sicht)
    z1 = {}
    alle = [l['datei'] for l in laeufe]
    for fam in ('111', '100'):
        z1[fam] = {'gemeinsam': z1_fit(laeufe, Sms, fam, alle, Tc)}
        for n in alle:
            z1[fam][n] = z1_fit(laeufe, Sms, fam, [n], Tc)
        for k, r in z1[fam].items():
            print('ZUSATZ Z1 (nach Sicht, kein S4-Ergebnis) Familie %s, %s: sigma %.3f, Delta-chi2-1-Band [%.3f, %.3f]%s, Jackknife +- %.3f '
                  '(Min/Max %s), chi2 %.2f bei dof %d; Q %.3f, Band [%.3f, %.3f], Jackknife +- %.3f' % (
                      fam, k, r['sigma'], r['band_delta_chi2_1'][0], r['band_delta_chi2_1'][1],
                      ' (BERUEHRT GITTERRAND)' if r['band_beruehrt_gitterrand'] else '', r['sigma_jackknife_err'],
                      np.round(r['sigma_jackknife_min_max'], 3).tolist(), r['chi2'], r['dof'], r['Q'],
                      r['Q_band_delta_chi2_1'][0], r['Q_band_delta_chi2_1'][1], r['Q_jackknife_err']))
    zus['zusatz_z1_nach_sicht'] = z1
    out['zusammenfassung_111'] = zus
    out['zeit_s'] = time.time() - T0
    with open(a.out, 'w') as fh:
        json.dump(out, fh, indent=1)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='modus', required=True)
    p = sub.add_parser('beta')
    p.add_argument('--tab', nargs='+', required=True)
    p.add_argument('--haupt', default='m5-n6t4')
    p.add_argument('--nt6', default='')
    p.add_argument('--out', required=True)
    p = sub.add_parser('sigma')
    p.add_argument('--ein', nargs='+', required=True)
    p.add_argument('--beta', type=float, required=True)
    p.add_argument('--dmin', type=int, default=1)
    p.add_argument('--betac-json', dest='betac_json', default='')
    p.add_argument('--korr-json', dest='korr_json', default='')
    p.add_argument('--out', required=True)
    a = ap.parse_args()
    if a.modus == 'beta':
        modus_beta(a)
    else:
        modus_sigma(a)


if __name__ == '__main__':
    main()
