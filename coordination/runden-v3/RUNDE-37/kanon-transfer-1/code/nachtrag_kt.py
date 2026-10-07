#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KANON-TRANSFER-1, Nachtrag [N] nach Sicht (beschreibend, kein Urteil; nach dem eingefrorenen Lauf geschrieben).

Frage: Woher kommt der endliche Rueckstoss von K (|dp_a| bei -1e-3 und -1e-4 gleich gross)?
Je Zug (X, Y) und mu (-1e-3, -1e-4): Anteil der neuen Kante d-e an d ln D_v / d a im Kantenraum der neuen Zerlegung
(Plan-Konvention), und derselbe Kovektor in der Variante "alter Kantenraum, neue Kante flach fortgesetzt"
(a_de = j . a_9, td.jrow_flach): g_flach_e = d ln D_v / d a_e + (d ln D_v / d a_de) j_e. Zustand Z1 wie kanon.zug.
kanon.py (eingefroren), konfluenz.py, td.py, tu.py, tg.py unveraendert importiert.
Aufruf: nachtrag_kt.py lauf <saat> <eingabe> <out>  |  nachtrag_kt.py zusammen <out> <dateien ...>
"""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import tu  # noqa: E402
import td  # noqa: E402
import konfluenz as kf  # noqa: E402
import kanon as kn  # noqa: E402


def lauf(saat, eingabe, out):
    d = json.load(open(eingabe))['ergebnis']
    LV, pos, G0, O0, pr = tg.zufallsnetz(128, saat)
    k1 = 2 * np.pi * np.linalg.inv(LV).T[0]
    hp, hx = td.polarisation(k1)
    Nu = kf.netz('A1', LV, pos, G0, O0, k1, hp, hx)
    lbar, fl = float(Nu.l0.mean()), Nu.fl
    res = []
    for i, f in enumerate(d['faelle']):
        X, Y = int(f['X']), int(f['Y'])
        ecken = f['verschiebung']['ecken']
        for mz in kn.MU_LISTE:
            pos2 = pos.copy()
            if mz == 1e-3:
                vs = [(int(v), np.array(dl, float)) for v, dl in ecken]
            else:
                kf.MU_ZIEL = mz
                try:
                    if len(ecken) == 1:
                        vs = [(int(ecken[0][0]), kf.newton(LV, pos, G0, O0, fl, int(ecken[0][0]), [X, Y], lbar))]
                    else:
                        vs = [(int(ecken[0][0]), kf.newton(LV, pos, G0, O0, fl, int(ecken[0][0]), [X], lbar)),
                              (int(ecken[1][0]), kf.newton(LV, pos, G0, O0, fl, int(ecken[1][0]), [Y], lbar))]
                finally:
                    kf.MU_ZIEL = 1e-3
            for v, dl in vs:
                pos2[v] = pos2[v] + dl
            N0 = kf.netz('A1', LV, pos2, G0, O0, k1, hp, hx)
            sk0 = kf.skalar_ops(N0)
            _, geo = tu.flaechen_geo(LV, pos2, G0, O0)
            for name, j in (('X', X), ('Y', Y)):
                typ, r, (Gn, On, b) = kf.zug_waehlen(N0, j, td.VMIN_B * N0.vbar, geo)
                N1 = kf.netz('A1', LV, pos2, Gn, On, k1, hp, hx)
                alt = b['alt']
                V5e = [alt[0][0], alt[0][1], alt[0][2], alt[0][3], alt[1][3]]
                V5 = [int(v) for v, _ in V5e]
                rc = np.array([pos2[v] + np.asarray(o, float) @ LV for v, o in V5e]).mean(0)
                dl2 = kn.dlnD(N0, N1, V5, lbar)[0]
                inew = int(N1.idx_von_keys(np.array([b['kante_neu']]))[0][0])
                idx01 = N1.idx_von_keys(N0.keys)[0]
                i9 = N0.idx_von_keys(b['k9'])[0]
                jr, _ = td.jrow_flach(N0.l0[i9])
                g_fl = dl2[:, idx01].copy()
                g_fl[:, i9] += dl2[:, [inew]] * jr[None, :]
                s0 = sk0['s0']
                th = pos2 @ k1 + (kn.P0_Z1 - float(rc @ k1))
                phi = kn.A_PHI * np.cos(th)
                pi = s0 * kn.A_PHI * float(np.linalg.norm(k1)) * np.sin(th)
                c = pi[V5] * phi[V5]
                dp_neu, dp_fl = 0.5 * c @ dl2, 0.5 * c @ g_fl
                res.append({'saat': saat, 'nr': i, 'art': f['art'], 'mu': '%g' % mz, 'zug': name,
                            'anteil_neue_kante': [float(abs(dl2[k, inew]) / np.linalg.norm(dl2[k])) for k in range(5)],
                            'norm_dlnD_neu': [float(np.linalg.norm(dl2[k])) for k in range(5)],
                            'norm_dlnD_flach': [float(np.linalg.norm(g_fl[k])) for k in range(5)],
                            'dp_neu_S': float(np.linalg.norm(N1.S.T @ dp_neu)),
                            'dp_flach_S': float(np.linalg.norm(N0.S.T @ dp_fl)),
                            'dp_neu': float(np.linalg.norm(dp_neu)), 'dp_flach': float(np.linalg.norm(dp_fl))})
        print('fall', i, 'fertig', flush=True)
    kf.schreibe(out, {'ergebnis': res})


def mmm(v):
    v = [x for x in v if x is not None]
    return {'n': len(v), 'median': float(np.median(v)), 'min': float(np.min(v)), 'max': float(np.max(v))} if v else None


def zusammen(out, dateien):
    R = [r for p in dateien for r in json.load(open(p))['ergebnis']]
    Z = {'eingaben_sha256': {os.path.basename(p): kf.sha(p) for p in dateien}, 'n': len(R)}
    for mk in ('0.001', '0.0001'):
        S = [r for r in R if r['mu'] == mk]
        Z[mk] = {'n': len(S),
                 'anteil_neue_kante': mmm([x for r in S for x in r['anteil_neue_kante']]),
                 'norm_dlnD_neu': mmm([x for r in S for x in r['norm_dlnD_neu']]),
                 'norm_dlnD_flach': mmm([x for r in S for x in r['norm_dlnD_flach']]),
                 'dp_neu_S': mmm([r['dp_neu_S'] for r in S]), 'dp_flach_S': mmm([r['dp_flach_S'] for r in S]),
                 'dp_flach_S_durch_dp_neu_S': mmm([r['dp_flach_S'] / r['dp_neu_S'] for r in S if r['dp_neu_S'] > 0])}
    by = {}
    for r in R:
        by.setdefault((r['saat'], r['nr'], r['zug']), {})[r['mu']] = r
    P = [v for v in by.values() if '0.001' in v and '0.0001' in v]
    Z['verhaeltnis_mu3_durch_mu4'] = {
        'n': len(P),
        'dp_neu_S': mmm([v['0.001']['dp_neu_S'] / v['0.0001']['dp_neu_S'] for v in P if v['0.0001']['dp_neu_S'] > 0]),
        'dp_flach_S': mmm([v['0.001']['dp_flach_S'] / v['0.0001']['dp_flach_S'] for v in P if v['0.0001']['dp_flach_S'] > 0]),
        'norm_dlnD_flach': mmm([np.linalg.norm(v['0.001']['norm_dlnD_flach']) / np.linalg.norm(v['0.0001']['norm_dlnD_flach'])
                                for v in P])}
    kf.schreibe(out, {'ergebnis': Z})
    print(json.dumps(Z, indent=1))


if __name__ == '__main__':
    if sys.argv[1] == 'lauf':
        lauf(int(sys.argv[2]), sys.argv[3], sys.argv[4])
    else:
        zusammen(sys.argv[2], sys.argv[3:])
