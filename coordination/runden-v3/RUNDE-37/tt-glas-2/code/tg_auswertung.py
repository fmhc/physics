#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GLAS-1: mechanische Auswertung (Urteile TG-G0 bis TG-G3 nach PLAN.md). Liest lauf/kontrolle.json,
lauf/netz-*.json (Teile je Netz werden ueber ridx zusammengefuehrt), lauf/affin-*.json; schreibt auswertung.json."""
import argparse, glob, json, os, sys, hashlib, time
import numpy as np

REF_TTISO = 0.06338809562866454      # TT-ISO-1, lauf-69/gitter-V-A1R1.json, ergebnis.spanne_J1 (V, A1R1, J = 1)
REF_KARTE = 0.0634                   # Kartenwortlaut "6,34 %"
TOL_G0 = 1e-3
P_BEREICH = (-0.65, -0.35)
N_ZIEL_G3 = 8000
SCHWELLE_G3 = 0.01
TT_MIN = 0.99
LIN_MAX = 0.01
NBOOT = 2000


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def punkte_ok(zeile):
    """Regulaer an einer Richtung: an allen Punkten genau 2 masselose, positiv, nichts wachsend oder unklar;
    an TT-Richtungen TT-Anteil >= 0,99 und linear (omega^2(2e-3)/(4 omega^2(1e-3)) - 1 <= 0,01)."""
    gruende = []
    for key in ('eps1', 'eps2'):
        if key not in zeile:
            continue
        z = zeile[key]
        if z['n_masselos'] != 2:
            gruende.append('%s: %d masselos' % (key, z['n_masselos']))
        if len(z['w2k2_masselos']) != 2:
            gruende.append('%s: %d positive masselose' % (key, len(z['w2k2_masselos'])))
        if z['n_wachsend'] > 0:
            gruende.append('%s: %d wachsend' % (key, z['n_wachsend']))
        if z['n_unklar'] > 0:
            gruende.append('%s: %d unklar' % (key, z['n_unklar']))
    if 'tt_anteil' in zeile['eps1']:
        if len(zeile['eps1']['tt_anteil']) < 2 or min(zeile['eps1']['tt_anteil']) < TT_MIN:
            gruende.append('TT-Anteil %s' % zeile['eps1']['tt_anteil'])
    if 'eps2' in zeile and len(zeile['eps2']['w2k2_masselos']) == 2 and len(zeile['eps1']['w2k2_masselos']) == 2:
        lin = max(abs(a / b - 1) for a, b in zip(zeile['eps2']['w2k2_masselos'], zeile['eps1']['w2k2_masselos']))
        if lin > LIN_MAX:
            gruende.append('nicht linear %.3g' % lin)
    return gruende


def netz_kennzahlen(spek):
    """spek: Liste der Zeilen (13 Richtungen). Rueckgabe Kennzahlen je Netz."""
    spek = sorted(spek, key=lambda z: z['ridx'])
    w = []
    gruende = []
    for z in spek:
        g = punkte_ok(z)
        gruende += ['%s %s' % (z['richtung'], x) for x in g]
        wm = z['eps1']['w2k2_masselos']
        w.append(wm if len(wm) == 2 else [np.nan, np.nan])
    w = np.array(w, float)
    out = {'richtungen': [z['richtung'] for z in spek], 'w2k2': w.tolist(), 'regulaer': len(gruende) == 0,
           'gruende': gruende[:20], 'n_gruende': len(gruende)}
    if np.isfinite(w).all():
        out['spanne'] = float(w.max() / w.min() - 1)
        wbar = w.mean(1)
        out['delta_richtung'] = (wbar / wbar.mean() - 1).tolist()
        out['w_mittel'] = float(w.mean())
        out['aufspaltung_max'] = float(np.max(w[:, 1] / w[:, 0] - 1))
        out['richtungsspanne_mittel_zweige'] = float(wbar.max() / wbar.min() - 1)
    ks = [z[k] for z in spek for k in ('eps1', 'eps2') if k in z]
    out['n_masselos'] = sorted(set(int(z['n_masselos']) for z in ks))
    out['n_wachsend_max'] = int(max(z['n_wachsend'] for z in ks))
    out['n_unklar_max'] = int(max(z['n_unklar'] for z in ks))
    out['luecke_min'] = min([z['luecke_min'] for z in ks if z['luecke_min'] is not None] or [None])
    out['luecke_min_rel_skala'] = min([z['luecke_min'] / z['skala'] for z in ks if z['luecke_min'] is not None] or [None])
    out['w2_min_re'] = float(min(z['w2_min_re'] for z in ks))
    out['A_red_pd_alle'] = bool(all(z['A_red_pd'] for z in ks))
    out['B_red_neg_max'] = int(max(z['B_red_neg'] for z in ks))
    out['dim'] = sorted(set(int(z['dim']) for z in ks))
    out['rang_voll'] = bool(all(z['rang_Mc'] == z['nX'] for z in ks))
    tt = [x for z in spek if 'tt_anteil' in z['eps1'] for x in z['eps1']['tt_anteil']]
    out['tt_min'] = float(min(tt)) if tt else None
    fr = [x for z in spek if 'fit_rest' in z['eps1'] for x in z['eps1']['fit_rest']]
    out['fit_rest_max'] = float(max(fr)) if fr else None
    lin = [abs(a / b - 1) for z in spek if 'eps2' in z and len(z['eps2']['w2k2_masselos']) == 2 and len(z['eps1']['w2k2_masselos']) == 2
           for a, b in zip(z['eps2']['w2k2_masselos'], z['eps1']['w2k2_masselos'])]
    out['lin_max'] = float(max(lin)) if lin else None
    ko = [z['eps1']['kontr_ops'] for z in spek if 'kontr_ops' in z['eps1']]
    out['kontr_ops'] = ko[0] if ko else None
    out['t_punkt_max_s'] = float(max(z['t_s'] for z in ks))
    return out


def ols(x, y):
    A = np.vstack([np.ones_like(x), x]).T
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(c[0]), float(c[1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())},
           'eingaben': {}}
    # ---------------- Kontrolle TG-G0
    pk = os.path.join(a.lauf, 'kontrolle.json')
    if os.path.exists(pk):
        ko = json.load(open(pk))
        res['eingaben']['kontrolle.json'] = {'sha256': sha(pk), 'tg_sha256': ko['info']['skript_sha256']}
        kz = netz_kennzahlen(ko['ergebnis']['spektrum'])
        sV = kz.get('spanne')
        res['kontrolle'] = {'kennzahlen': kz, 'pruefung': ko['ergebnis']['pruefung'], 'affin': ko['ergebnis'].get('affin')}
        if sV is None:
            res['TG-G0'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar'}
        else:
            ap_ = abs(sV / REF_TTISO - 1)
            aw_ = abs(sV / REF_KARTE - 1)
            res['TG-G0'] = {'spanne_V': sV, 'abw_rel_ttiso': ap_, 'abw_rel_karte': aw_,
                            'plan': 'eingetroffen' if ap_ <= TOL_G0 else 'verfehlt',
                            'wortlaut': 'eingetroffen' if aw_ <= TOL_G0 else 'verfehlt'}
    else:
        res['TG-G0'] = {'plan': 'nicht entscheidbar (kein Lauf)', 'wortlaut': 'nicht entscheidbar (kein Lauf)'}
    # ---------------- Netze
    teile = {}
    for p in sorted(glob.glob(os.path.join(a.lauf, 'netz-*.json'))):
        d = json.load(open(p))
        e = d['ergebnis']
        key = (int(e['N']), int(e['saat']))
        res['eingaben'][os.path.basename(p)] = {'sha256': sha(p), 'tg_sha256': d['info']['skript_sha256'], 'laufzeit_s': d['laufzeit_s']}
        t = teile.setdefault(key, {'spektrum': {}, 'pruefung': e['pruefung']})
        for z in e['spektrum']:
            t['spektrum'][z['ridx']] = z
    netze = []
    for (N, saat), t in sorted(teile.items()):
        if sorted(t['spektrum']) != list(range(13)):
            netze.append({'N': N, 'saat': saat, 'vollstaendig': False, 'ridx': sorted(t['spektrum'])})
            continue
        kz = netz_kennzahlen(list(t['spektrum'].values()))
        kz.update({'N': N, 'saat': saat, 'vollstaendig': True, 'pruefung': t['pruefung']})
        netze.append(kz)
    res['netze'] = netze
    voll = [n for n in netze if n['vollstaendig']]
    reg = [n for n in voll if n['regulaer']]
    res['zaehlung'] = {'netze_vollstaendig': len(voll), 'netze_regulaer': len(reg),
                       'nicht_regulaer': [{'N': n['N'], 'saat': n['saat'], 'n_gruende': n['n_gruende'], 'gruende': n['gruende'][:5]}
                                          for n in voll if not n['regulaer']]}
    Ns = sorted(set(n['N'] for n in reg))
    jeN = {}
    for N in Ns:
        sp_ = np.array([n['spanne'] for n in reg if n['N'] == N])
        wm = np.array([n['w_mittel'] for n in reg if n['N'] == N])
        dl = np.array([n['delta_richtung'] for n in reg if n['N'] == N])
        z = {'n': int(len(sp_)), 'spanne_mittel': float(sp_.mean()), 'spanne_sd': float(sp_.std(ddof=1)) if len(sp_) > 1 else None,
             'spanne_min': float(sp_.min()), 'spanne_max': float(sp_.max()), 'w_mittel': float(wm.mean()),
             'w_sd': float(wm.std(ddof=1)) if len(wm) > 1 else None}
        if len(dl) >= 3:
            m = dl.mean(0)
            se = dl.std(0, ddof=1) / np.sqrt(len(dl))
            zz = m / se
            z.update({'delta_mittel': m.tolist(), 'delta_se': se.tolist(), 'z': zz.tolist(), 'z_absmax': float(np.abs(zz).max()),
                      'n_z_ueber_2': int((np.abs(zz) > 2).sum())})
        jeN[str(N)] = z
    res['je_N'] = jeN
    # ---------------- TG-G1 (Exponent) und TG-G3 (Extrapolation)
    nutzbar = [N for N in Ns if jeN[str(N)]['n'] >= 2]
    if len(nutzbar) >= 3:
        x = np.log([n['N'] for n in reg if n['N'] in nutzbar])
        y = np.log([n['spanne'] for n in reg if n['N'] in nutzbar])
        a0, p_plan = ols(x, y)
        xm = np.log(nutzbar)
        ym = np.log([jeN[str(N)]['spanne_mittel'] for N in nutzbar])
        b0, p_wort = ols(xm, ym)
        rng = np.random.default_rng(17)
        boot = []
        grup = {N: np.array([n['spanne'] for n in reg if n['N'] == N]) for N in nutzbar}
        for _ in range(NBOOT):
            xb, yb = [], []
            for N in nutzbar:
                g = grup[N][rng.integers(0, len(grup[N]), len(grup[N]))]
                xb += [np.log(N)] * len(g)
                yb += list(np.log(g))
            boot.append(ols(np.array(xb), np.array(yb))[1])
        boot = np.array(boot)
        in_b = lambda p: P_BEREICH[0] <= p <= P_BEREICH[1]  # noqa: E731
        res['TG-G1'] = {'N': nutzbar, 'p_plan': p_plan, 'p_wortlaut': p_wort,
                        'p_boot_68': [float(np.percentile(boot, 16)), float(np.percentile(boot, 84))],
                        'p_boot_95': [float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))],
                        'plan': 'eingetroffen' if in_b(p_plan) else 'verfehlt',
                        'wortlaut': 'eingetroffen' if in_b(p_wort) else 'verfehlt'}
        s8000_plan = float(np.exp(a0 + p_plan * np.log(N_ZIEL_G3)))
        s8000_wort = float(np.exp(b0 + p_wort * np.log(N_ZIEL_G3)))
        res['TG-G3'] = {'spanne_8000_extrapoliert_plan': s8000_plan, 'spanne_8000_extrapoliert_mittel': s8000_wort,
                        'N_max_gerechnet': int(max(nutzbar)),
                        'plan': ('eingetroffen (extrapoliert)' if s8000_plan < SCHWELLE_G3 else 'verfehlt (extrapoliert)'),
                        'wortlaut': 'nicht entscheidbar (N ~ 8000 nicht gerechnet)'}
    else:
        res['TG-G1'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar', 'N': nutzbar}
        res['TG-G3'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar (N ~ 8000 nicht gerechnet)'}
    # ---------------- TG-G2 (Mittel ueber Saaten richtungsunabhaengig)
    mitz = [N for N in Ns if 'z' in jeN[str(N)]]
    if mitz:
        plan_ok = all(jeN[str(N)]['n_z_ueber_2'] <= 2 and jeN[str(N)]['z_absmax'] <= 3.5 for N in mitz)
        wort_ok = all(jeN[str(N)]['n_z_ueber_2'] == 0 for N in mitz)
        res['TG-G2'] = {'N': mitz, 'n_z_ueber_2': {str(N): jeN[str(N)]['n_z_ueber_2'] for N in mitz},
                        'z_absmax': {str(N): jeN[str(N)]['z_absmax'] for N in mitz},
                        'plan': 'eingetroffen' if plan_ok else 'verfehlt', 'wortlaut': 'eingetroffen' if wort_ok else 'verfehlt'}
    else:
        res['TG-G2'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar'}
    # ---------------- Zusatz: affine Steifigkeit (beschreibend)
    af = []
    for p in sorted(glob.glob(os.path.join(a.lauf, 'affin-*.json'))):
        d = json.load(open(p))
        e = d['ergebnis']
        res['eingaben'][os.path.basename(p)] = {'sha256': sha(p), 'tg_sha256': d['info']['skript_sha256']}
        af.append({'N': e['N'], 'saat': e['saat'], 'min': e['affin']['min'], 'max': e['affin']['max'],
                   'spanne': e['affin']['spanne_max_min'], 'pruefung': e['pruefung']})
    res['affin'] = af
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig auswertung', len(netze), 'netze', flush=True)


if __name__ == '__main__':
    main()
