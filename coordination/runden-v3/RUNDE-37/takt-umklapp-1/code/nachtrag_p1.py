#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TAKT-UMKLAPP-1, NACHTRAG nach dem Einfrieren (beschreibend, geht in kein Urteil ein).
Anlass: Kontrolle K6 (PLAN 3) zeigte im Lauf A1 auf V kleinstes *1 = 1/720, PUMPE-NETZ-1 meldet fuer die P1-Gewichte
1/60 bis 1/2. Frage: Sind P1-Gewichte (3D-Kotangens, pn.K_aus_laengen aus PUMPE-NETZ-1, unveraendert) und umkreisbasierte
*1 (tu.hodge, eingefroren) je Kante gleich? Ist P = c L_P1 oder nur P = c L_umkreis?
Netze: V, S, V_D, glas-N128-s1 (wie tu.netz_bauen). tu.py, tg.py, pn.py werden unveraendert importiert."""
import argparse, json, os, sys, time, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import tu  # noqa: E402
import pn  # noqa: E402

PAARE2 = [(p[0], p[1]) for p in tg.PAARE]


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def p1_gewichte(mod):
    w = np.zeros(mod['E'])
    lt = mod['l'][mod['eidx']]
    for t in range(mod['T']):
        K = np.real(pn.K_aus_laengen(PAARE2, lt[t].astype(complex)))
        for p, (i, j) in enumerate(PAARE2):
            w[mod['eidx'][t, p]] += -K[i, j]
    return w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--netze', default='V,S,VD,glas-N128-s1')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'tu_sha256': sha(os.path.abspath(tu.__file__)),
                    'pn_sha256': sha(os.path.abspath(pn.__file__)), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())},
           'netze': []}
    for name in a.netze.split(','):
        LV, pos, G, O, pr, info = tu.netz_bauen(name)
        mod = tg.modell(LV, pos, G, O, pr)
        h, s1, s2, Ast = tu.hodge(LV, pos, G, O, mod)
        w = p1_gewichte(mod)
        d = np.abs(w - s1)
        z = {'name': name, 'E': int(mod['E']), 'p1_min': float(w.min()), 'p1_max': float(w.max()), 'p1_n_neg': int((w < -1e-12).sum()),
             'stern1_min': float(s1.min()), 'stern1_max': float(s1.max()), 'abw_max': float(d.max()),
             'abw_rel_max': float(d.max() / np.abs(s1).max()), 'n_kanten_abw': int((d > 1e-12 * np.abs(s1).max()).sum()),
             'summe_l_w_durch_summe_l_s1': float((mod['l'] ** 2 * w).sum() / (mod['l'] ** 2 * s1).sum())}
        if mod['E'] <= 100:
            paare = sorted(set((round(float(x), 9), round(float(y), 9), round(float(l), 9)) for x, y, l in zip(s1, w, mod['l'])))
            z['werte_stern1_p1_laenge'] = paare
        ks = tu.k_satz(LV, 0, 4, 5)
        rest_p1, rest_um, c_p1 = [], [], []
        for nm, k in ks:
            P, L1 = tu.takt_mats(mod, k, s1)
            _, Lp = tu.takt_mats(mod, k, w)
            cp = float(np.vdot(Lp, P).real / np.vdot(Lp, Lp).real)
            c_p1.append(cp)
            rest_p1.append(float(np.abs(P - cp * Lp).max() / np.abs(P).max()))
            rest_um.append(float(np.abs(P - 8.0 * L1).max() / np.abs(P).max()))
        z['P_gegen_c_Lp1'] = {'c_bestfit_min': min(c_p1), 'c_bestfit_max': max(c_p1), 'rest_min': min(rest_p1), 'rest_max': max(rest_p1)}
        z['P_gegen_8_Lumkreis_rest_max'] = max(rest_um)
        res['netze'].append(z)
        print('nachtrag p1', name, 'abw_rel_max %.3g' % z['abw_rel_max'], flush=True)
    res['laufzeit_s'] = time.time() - t0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    tg.schreibe(a.out, res)
    print('fertig nachtrag p1', 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
