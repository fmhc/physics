#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HODGE-MASSE-1, Nachtrag nach Sicht (beschreibend, kein Urteil): Haengt der Abstand RH(Sigma_E) gegen
RH(Sigma_G1) der TT-Werte auf V von |k| ab wie eine numerische Grenze (~ eps_mach ||B|| / omega^2_TT ~ 1/k^2) oder
bleibt er (dann waere er eine Flaechenabhaengigkeit)? Ruft hm.eichflaechen (eingefroren, unveraendert) bei
|k| = 1e-3, 1e-2, 1e-1 an den 13 Richtungen auf.
"""
import json, sys, os, time, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hm  # noqa: E402
import tg  # noqa: E402
import tti  # noqa: E402


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    out_pfad = sys.argv[1]
    t0 = time.time()
    LV, pos, G, O, info = hm.netz('V')
    mod = tg.modell(LV, pos, G, O, {})
    geo = hm.tet_geo(LV, pos, G, O, mod)
    gauges = [np.random.default_rng(s).uniform(0.25, 4.0, mod['E']) for s in hm.GSAAT]
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'hm_sha256': sha(os.path.abspath(hm.__file__))}, 'zeilen': []}
    for e in (1e-3, 1e-2, 1e-1):
        q = {'eps': e}
        for kin in ('A1', 'A2'):
            dd = {'RH_E_gegen_G1_sym': 0.0, 'RH_E_gegen_G1_lagr': 0.0, 'RH_G1_sym_gegen_G1_lagr': 0.0,
                  'RH_E_ham_gegen_E_lagr': 0.0, 'R1_E_gegen_G1_R1G': 0.0}
            for nm, d in tti.richtungen13():
                r = hm.eichflaechen(mod, geo, e * d, gauges)[kin]
                f = lambda a, b: float(np.max(np.abs(np.array(a) - np.array(b)) / np.abs(np.array(b))))  # noqa: E731
                dd['RH_E_gegen_G1_sym'] = max(dd['RH_E_gegen_G1_sym'], f(r['G1_RH_symplektisch'], r['E_RH_hamilton']))
                dd['RH_E_gegen_G1_lagr'] = max(dd['RH_E_gegen_G1_lagr'], f(r['G1_RH_lagrange'], r['E_RH_hamilton']))
                dd['RH_G1_sym_gegen_G1_lagr'] = max(dd['RH_G1_sym_gegen_G1_lagr'], f(r['G1_RH_symplektisch'], r['G1_RH_lagrange']))
                dd['RH_E_ham_gegen_E_lagr'] = max(dd['RH_E_ham_gegen_E_lagr'], f(r['E_RH_lagrange'], r['E_RH_hamilton']))
                dd['R1_E_gegen_G1_R1G'] = max(dd['R1_E_gegen_G1_R1G'], f(r['G1_R1G'], r['E_R1']))
            q[kin] = dd
        res['zeilen'].append(q)
    res['laufzeit_s'] = time.time() - t0
    with open(out_pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1)
    os.replace(out_pfad + '.tmp', out_pfad)
    print('fertig nachtrag_hm1', flush=True)


if __name__ == '__main__':
    main()
