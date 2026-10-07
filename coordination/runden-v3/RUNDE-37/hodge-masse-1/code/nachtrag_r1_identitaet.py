#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HODGE-MASSE-1, Nachtrag nach Sicht (Zusatz der Leitung 10:1x, Punkt 3; beschreibend, kein Urteil):
HM1 als Identitaetsprobe fuer R1. R1 = Dirac-Reduktion des Paars (c^H a, c^H p) plus Quotient nach Eckverschiebungen.
Gleiche Regel (Impulse in Bild S = Komplement Bild[M, c]) auf einer anderen Eichflaeche W = S - M (M^H G M)^-1 M^H G S,
kanonisch gepaart (Gm = W^H S). Erwartet [M]: dieselben omega^2 bis auf Rundung. Daneben R2 (K auf der Flaeche) auf
beiden Flaechen, wie in TT-GLAS-2 (c) (A2L = A3 mit J = 1). Benutzt hm.py (eingefroren, unveraendert).
"""
import json, sys, os, time, hashlib
import numpy as np
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hm  # noqa: E402
import tg  # noqa: E402
import tti  # noqa: E402


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def punkt(mod, geo, k, G):
    eps = float(np.linalg.norm(k))
    Bs, A1s, M, c = tg.ops(mod, k)
    B = Bs.toarray()
    S, Q, C, weg, sv = hm.zerlege(M, c)
    Sh = np.conj(S.T)
    Li = sla.solve_triangular(np.linalg.cholesky(hm.herm(Sh @ B @ S)), np.eye(S.shape[1]), lower=True)
    GM = G[:, None] * M
    W = S - M @ np.linalg.solve(hm.herm(np.conj(M.T) @ GM), np.conj(GM.T) @ S)
    Wh = np.conj(W.T)
    LWi = sla.solve_triangular(np.linalg.cholesky(hm.herm(Wh @ B @ W)), np.eye(W.shape[1]), lower=True)
    Gm = Wh @ S
    out = {}
    Kd = hm.assemble(mod, geo['Kt'], k)
    for kin, A in (('A1', hm.assemble(mod, geo['A1t'], k)), ('A2', hm.assemble(mod, geo['A2t'], k)), ('A2L', np.linalg.inv(Kd))):
        Ar = hm.herm(Sh @ A @ S)
        wE = hm.z_auswerten(Li @ np.linalg.solve(Ar, np.conj(Li.T)), eps)
        KG = Gm @ np.linalg.solve(Ar, np.conj(Gm.T))
        wG = hm.z_auswerten(LWi @ hm.herm(KG) @ np.conj(LWi.T), eps)
        d = {'R1_E': wE['w2k2'], 'R1_G_gleiches_Paar': wG['w2k2'], 'ok_E': wE['ok'], 'ok_G': wG['ok']}
        if kin == 'A2L':
            r2E = hm.z_auswerten(Li @ hm.herm(Sh @ Kd @ S) @ np.conj(Li.T), eps)
            r2G = hm.z_auswerten(LWi @ hm.herm(Wh @ Kd @ W) @ np.conj(LWi.T), eps)
            d['R2_E'] = r2E['w2k2']
            d['R2_G'] = r2G['w2k2']
        out[kin] = d
    return out


def rel(a, b):
    return float(np.max(np.abs(np.array(a) - np.array(b)) / np.abs(np.array(b))))


def main():
    out_pfad = sys.argv[1]
    t0 = time.time()
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'hm_sha256': sha(os.path.abspath(hm.__file__))}}
    for name, epsl, richt in (('V', (1e-3, 1e-2, 1e-1), tti.richtungen13()),
                              ('glas-s1', (1e-2,), [r for r in tg.richtungen13w() if r[0] in ('100', '110', '111')])):
        LV, pos, Gt, O, info = hm.netz(name)
        mod = tg.modell(LV, pos, Gt, O, {})
        geo = hm.tet_geo(LV, pos, Gt, O, mod)
        G1 = np.random.default_rng(hm.GSAAT[0]).uniform(0.25, 4.0, mod['E'])
        zz = []
        for e in epsl:
            q = {'eps': e}
            for kin in ('A1', 'A2', 'A2L'):
                q[kin + '_R1_E_gegen_G1'] = 0.0
                q[kin + '_ok'] = True
            q['A2L_R2_E_gegen_G1'] = 0.0
            for nm, d in richt:
                r = punkt(mod, geo, e * d, G1)
                for kin in ('A1', 'A2', 'A2L'):
                    q[kin + '_R1_E_gegen_G1'] = max(q[kin + '_R1_E_gegen_G1'], rel(r[kin]['R1_G_gleiches_Paar'], r[kin]['R1_E']))
                    q[kin + '_ok'] &= bool(r[kin]['ok_E'] and r[kin]['ok_G'])
                q['A2L_R2_E_gegen_G1'] = max(q['A2L_R2_E_gegen_G1'], rel(r['A2L']['R2_G'], r['A2L']['R2_E']))
            zz.append(q)
        res[name] = zz
    res['laufzeit_s'] = time.time() - t0
    with open(out_pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1)
    os.replace(out_pfad + '.tmp', out_pfad)
    print('fertig nachtrag_r1_identitaet', flush=True)


if __name__ == '__main__':
    main()
