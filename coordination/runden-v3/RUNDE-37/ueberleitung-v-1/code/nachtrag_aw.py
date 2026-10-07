#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-V-1, Nachtrag-Auswertung (beschreibend): Zusammenfassungen aus nachtrag/nt2.json und nt3*.json
(statt jq-Aggregation). Importiert uv.py (eingefroren) unveraendert."""
import argparse, json, sys, os
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import uv  # noqa: E402
import tg  # noqa: E402


def lade(p):
    with open(p) as fh:
        return json.load(fh)['ergebnis']


def mm(xs):
    xs = [x for x in xs if x is not None]
    return [float(min(xs)), float(max(xs))] if xs else None


def vert(xs):
    out = {}
    for x in xs:
        out[str(x)] = out.get(str(x), 0) + 1
    return out


def konvergiert(p):
    return bool(p.get('definiert') and all(x == 0 for x in p['D0_n_neg_je_h'][-3:]) and p['aend_letzte']['M'] < 1e-2)


def zus_v(pts):
    kv = [p for p in pts if konvergiert(p)]
    a = [p['a'] for p in kv]
    out = {'anzahl': len(pts), 'konvergiert': len(kv),
           'nicht_konvergiert_orte': [p.get('m') or p.get('name') or [p.get('richtung'), p.get('kl')]
                                      for p in pts if not konvergiert(p)][:20],
           'e_M': mm([p.get('e_M') for p in kv]), 'aend_M': mm([p['aend_letzte']['M'] for p in kv]),
           'r_V': mm([p.get('r_V') for p in kv]), 'C_rest_kappa': mm([p.get('C_rest_kappa') for p in kv]),
           'kappa_re': mm([p['kappa'][0] for p in kv]), 'kappa_im': mm([p['kappa'][1] for p in kv]),
           'nn_rel': mm([p.get('nn_rel') for p in kv]), 'G_rel': mm([p.get('G_rel') for p in kv]),
           'R_S_rest': mm([p.get('R_S_rest') for p in kv]), 'Meff_min_rel': mm([p.get('Meff_min_rel') for p in kv]),
           'Meff_n_neg': vert([p.get('Meff_n_neg') for p in kv]), 'tol_null': mm([p.get('tol_null') for p in kv]),
           'n_u': vert([x.get('n_u') for x in a]), 'n_u_tol1e-10': vert([p['a_tol1e-10'].get('n_u') for p in kv]),
           'a_definiert': int(sum(1 for x in a if x.get('definiert'))),
           'a_gruende': vert([x.get('grund') for x in a if not x.get('definiert')]),
           'a_dim_red': vert([x.get('dim_red') for x in a]),
           'a_k_wachsend': int(sum(1 for x in a if x.get('definiert') and x.get('n_wachsend', 0) > 0)),
           'a_n_wachsend_max': int(max([x.get('n_wachsend', 0) for x in a], default=0)),
           'a_B_red_nicht_pd': int(sum(1 for x in a if x.get('B_red_pd') is False)),
           'a_A_red_n_neg': vert([x.get('A_red_n_neg') for x in a]),
           'a_pass_rest': mm([x.get('pass_rest') for x in a]),
           'a_w2_min_rel': mm([x.get('w2_min_rel') for x in a]),
           'aC_k_wachsend': int(sum(1 for p in kv if p['a_C'].get('definiert') and p['a_C'].get('n_wachsend', 0) > 0)),
           'aC_definiert': int(sum(1 for p in kv if p['a_C'].get('definiert'))),
           'atol_k_wachsend': int(sum(1 for p in kv if p['a_tol1e-10'].get('definiert')
                                      and p['a_tol1e-10'].get('n_wachsend', 0) > 0)),
           'atol_definiert': int(sum(1 for p in kv if p['a_tol1e-10'].get('definiert')))}
    return out


def spanne_v(pts, var='a'):
    W = {}
    for p in pts:
        r = p.get(var) if p.get('definiert') else None
        ok = bool(r is not None and konvergiert(p) and r.get('definiert') and r.get('ok') and r.get('w2k2') is not None)
        W[(p['ridx'], p['kl'])] = (ok, r['w2k2'] if ok else [np.nan, np.nan])
    je = {}
    for kl in uv.KL_RASTER:
        ww = np.array([W.get((i, kl), (False, [np.nan, np.nan]))[1] for i in range(13)], float)
        je['%g' % kl] = {'spanne': float(np.nanmax(ww) / np.nanmin(ww) - 1) if np.isfinite(ww).any() else None,
                         'n_ok': int(sum(W.get((i, kl), (False, None))[0] for i in range(13))),
                         'w_min': float(np.nanmin(ww)) if np.isfinite(ww).any() else None,
                         'w_max': float(np.nanmax(ww)) if np.isfinite(ww).any() else None}
    w0, alle_ok = [], True
    for i in range(13):
        for b in range(2):
            ws = [W.get((i, kl), (False, [np.nan, np.nan]))[1][b] for kl in uv.KL_FIT]
            alle_ok &= all(W.get((i, kl), (False, None))[0] for kl in uv.KL_FIT)
            if np.all(np.isfinite(ws)):
                w0.append(uv.fit_kl(uv.KL_FIT, ws)[0])
    w0 = np.array(w0)
    return {'spanne0': float(w0.max() / w0.min() - 1) if len(w0) and w0.min() > 0 else None, 'n_w0': int(len(w0)),
            'alle_ok_fit': bool(alle_ok), 'w0': mm(list(w0)), 'je_kl': je}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    out = {}
    n2 = lade(os.path.join(a.n, 'nt2.json'))['n3']
    d = [p for p in n2 if p.get('definiert')]
    out['kuhn_ls_rand'] = {'anzahl': len(n2), 'definiert': len(d), 'gruende': vert([p.get('grund') for p in n2 if not p.get('definiert')]),
                           'n_u': vert([p.get('n_u') for p in d]), 'dim_red': vert([p.get('dim_red') for p in d]),
                           'k_wachsend': int(sum(1 for p in d if p.get('n_wachsend', 0) > 0)),
                           'B_red_nicht_pd': int(sum(1 for p in d if p.get('B_red_pd') is False)),
                           'w2_durch_kubisch_zwei_kleinste': mm([x for p in d for x in (p.get('w2_durch_kubisch') or [])[:2]])}
    r = lade(os.path.join(a.n, 'nt3r.json'))['punkte']
    b = lade(os.path.join(a.n, 'nt3b0.json'))['punkte'] + lade(os.path.join(a.n, 'nt3b1.json'))['punkte']
    out['v_raster'] = zus_v(r)
    out['v_bz'] = zus_v(b)
    out['v_bz_rand'] = zus_v([p for p in b if p.get('rand')])
    out['v_spanne_a'] = spanne_v(r, 'a')
    out['v_spanne_aC'] = spanne_v(r, 'a_C')
    out['v_spanne_atol'] = spanne_v(r, 'a_tol1e-10')
    # Nulldurchgaenge des L-Blocks: kleinstes h mit negativem D_0-Eigenwert je kl (Raster)
    H = lade(os.path.join(a.n, 'nt3r.json'))['h']
    kreuz = {}
    for p in r:
        if not p.get('definiert'):
            continue
        neg = [H[j] for j, x in enumerate(p['D0_n_neg_je_h']) if x > 0]
        kreuz.setdefault('%g' % p['kl'], []).append(min(neg) if neg else 0.0)
    out['v_raster_kleinstes_h_mit_D0_neg_je_kl'] = {k: mm(v) for k, v in kreuz.items()}
    out['v_raster_D0_neg_je_h_beispiel'] = {('%s_%g' % (p['richtung'], p['kl'])): p['D0_n_neg_je_h'] for p in r
                                             if p.get('definiert') and p['richtung'] in ('100', '111')}
    out['herm_S2qq_max_letzte'] = mm([p['herm_S2qq_je_h'][-1] for p in r + b if p.get('definiert')])
    tg.schreibe(a.out, {'ergebnis': out})
    print('fertig nachtrag_aw', flush=True)


if __name__ == '__main__':
    main()
