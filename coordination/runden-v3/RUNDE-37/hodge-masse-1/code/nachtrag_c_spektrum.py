#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HODGE-MASSE-1, Diagnose-Nachtrag (Zusatz der Leitung 10:1x, CODEX-REVIEW-R48 HM-A1; beschreibend, kein Urteil):
Spektrum des vertikalen Eichblocks C = Q^H K Q (Q orthonormale Basis von Bild M, K = Lagrange-Form der
Bewegungsenergie: A1^-1, A2^-1, A2L) je Netz und |k| an den drei Richtungen [100], [110], [111].
Ausgegeben: Zahl negativer Eigenwerte, Zahl fast null (|ev| <= 1e-12 max), die vier kleinsten |ev| relativ zum groessten
und ihr Verhaeltnis zu k^2 und k^4 (Skalierung der laengs gerichteten Eichrichtung, lambda = 1).
Benutzt hm.py (eingefroren, unveraendert).
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
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'hm_sha256': sha(os.path.abspath(hm.__file__))}}
    for name, epsl in (('V', (1e-3, 1e-2, 1e-1)), ('S', (1e-3, 1e-2, 1e-1)), ('A15', (1e-3, 1e-2, 1e-1)),
                       ('glas-s1', (1e-2, 3e-2, 1e-1))):
        LV, pos, G, O, info = hm.netz(name)
        mod = tg.modell(LV, pos, G, O, {})
        geo = hm.tet_geo(LV, pos, G, O, mod)
        richt = [r for r in (tg.richtungen13w() if name.startswith('glas') else tti.richtungen13()) if r[0] in ('100', '110', '111')]
        zz = []
        for e in epsl:
            for nm, d in richt:
                k = e * d
                Bs, A1s, M, c = tg.ops(mod, k)
                S, Q, C, weg, sv = hm.zerlege(M, c)
                Kd = hm.assemble(mod, geo['Kt'], k)
                z = {'eps': e, 'richtung': nm, 'dim_Q': int(Q.shape[1])}
                for kin, K in (('A1', np.linalg.inv(hm.assemble(mod, geo['A1t'], k))),
                               ('A2', np.linalg.inv(hm.assemble(mod, geo['A2t'], k))), ('A2L', Kd)):
                    ev = np.linalg.eigvalsh(hm.herm(np.conj(Q.T) @ K @ Q))
                    s = float(np.abs(ev).max())
                    a = np.sort(np.abs(ev))
                    z[kin] = {'n_neg': int((ev < -1e-12 * s).sum()), 'n_null': int((np.abs(ev) <= 1e-12 * s).sum()),
                              'kleinste4_rel': [float(x / s) for x in a[:4]],
                              'kleinste_ueber_k2': float(a[0] / e ** 2), 'kleinste_ueber_k4': float(a[0] / e ** 4),
                              'min_rel': float(ev.min() / s)}
                zz.append(z)
        res[name] = zz
    res['laufzeit_s'] = time.time() - t0
    with open(out_pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1)
    os.replace(out_pfad + '.tmp', out_pfad)
    print('fertig nachtrag_c_spektrum', flush=True)


if __name__ == '__main__':
    main()
