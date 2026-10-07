#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, SCHWARZES-LOCH: Gitter (bn_sl.py-Ausgaben) gegen Kontinuum (bn_ode.rechne) bei gleicher Staerke s und
gleichem R0. Aufruf: bn_vergleich.py aus.json L12-R2-a.json [L12-R2-b.json ...] (mehrere Laeufe je Kombination erlaubt).
"""
import json, sys, os, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bn_ode  # noqa: E402
import bn_tov  # noqa: E402


def ode_bei(R0, s_werte):
    ts = np.logspace(-3, 3, 6001)
    d = bn_ode.rechne(R0, ts, n=3000)
    ok = d['ok']
    last = (int(np.argmin(ok)) - 1) if not ok.all() else len(ok) - 1
    ls = np.log(d['s'][:last + 1])
    out = []
    for s in s_werte:
        z = {'s': s}
        for k in ('M_iso', 'x', 'kompakt', 'Psi2_mitte', 'N_mitte_rel', 'N_rand_rel', 'K_ueber_M'):
            z[k] = float(np.interp(math.log(s), ls, d[k][:last + 1]))
        out.append(z)
    return out


def tov_bei(R0, s_werte):
    ts = np.linspace(0.05, 20.0 if R0 < 2.5 else 30.0, 500)
    d = bn_tov.rechne(R0, ts, n=2000)
    ok = d["ok"]
    last = (int(np.argmin(ok)) - 1) if not ok.all() else len(ok) - 1
    ls = np.log(d["s"][:last + 1])
    out = []
    for s in s_werte:
        z = {"s": s, "jenseits": bool(math.log(s) > ls[-1])}
        for k in ("x", "kompakt", "N_mitte_rel", "q_mitte"):
            z[k] = float(np.interp(math.log(s), ls, d[k][:last + 1])) if not z["jenseits"] else None
        out.append(z)
    return out, float(d["s"][last]), float(d["kompakt"][last]), float(d["x"][last])


def main():
    aus = sys.argv[1]
    laeufe = {}
    for p in sys.argv[2:]:
        with open(p) as f:
            d = json.load(f)['ergebnis']
        key = (d['L'], d['R0'])
        for z in d['staerken']:
            laeufe.setdefault(key, {})[z['s']] = z
    erg = {}
    for (L, R0), zs in sorted(laeufe.items()):
        sv = sorted(zs)
        ode = ode_bei(R0, sv)
        tov, s_stern, C_stern, x_stern = tov_bei(R0, sv)
        zeilen = []
        for s, o, tv in zip(sv, ode, tov):
            z = zs[s]
            zeilen.append({'s': s, 'konvergiert': z['konvergiert'], 'schritte': z['schritte'], 'verworfen': z['verworfen'],
                           'zeit_abgelaufen': z.get('zeit_abgelaufen', False),
                           'gitter': {k: z.get(k) for k in ('M_iso_lP', 'x', 'kompakt', 'N_mitte_rel', 'N_min_rel', 'r_N_min', 'K_ueber_M',
                                                            'Psi2_mitte_rel', 'a_max', 'lam_max', 'N_negativ', 'fit_rest_Psi', 'fit_rest_N',
                                                            'flaechenradius_monoton', 'flaechenradius_min_bei_r', 'N_min_roh', 'c0', 'd0')},
                           'sin_min': z['diag']['sin_min'], 'eps_max': z['diag']['eps_max'], 'RF_k': z['diag']['RF_k'], 'RG_k': z['diag']['RG_k'],
                           'kontinuum': o, 'tov': tv})
        zeilen.append({'tov_ende': {'s_stern': s_stern, 'kompakt_stern': C_stern, 'x_stern': x_stern}})
        erg['L%d_R%g' % (L, R0)] = zeilen
    with open(aus, 'w') as f:
        json.dump(erg, f, indent=1)
    f = lambda v, fmt='%.3f': (fmt % v) if isinstance(v, (int, float)) and v is not None and math.isfinite(v) else str(v)
    for k, zeilen in erg.items():
        print('==', k)
        print('  s | konv schritte | x G/ohneDruck/TOV | 2M/R G/oD/TOV | N_mitte G/oD/TOV | N_min G (r) | K/M G/oD | sin_min | lam_max')
        for z in zeilen:
            if 'tov_ende' in z:
                print('  TOV-Ende:', json.dumps(z['tov_ende']))
                continue
            g, o, tv = z['gitter'], z['kontinuum'], z['tov']
            print('  %g | %s %d | %s/%s/%s | %s/%s/%s | %s/%s/%s | %s (%s) | %s/%s | %s | %s' % (
                z['s'], 'ja' if z['konvergiert'] else ('ZEIT' if z['zeit_abgelaufen'] else 'NEIN'), z['schritte'], f(g['x']), f(o['x']), f(tv['x']),
                f(g['kompakt']), f(o['kompakt']), f(tv['kompakt']), f(g['N_mitte_rel'], '%.4f'), f(o['N_mitte_rel'], '%.4f'),
                f(tv['N_mitte_rel'], '%.4f'), f(g['N_min_rel'], '%.4f'), f(g['r_N_min'], '%.2f'), f(g['K_ueber_M']), f(o['K_ueber_M']),
                f(z['sin_min']), f(g['lam_max'], '%.2e')))


if __name__ == '__main__':
    main()
