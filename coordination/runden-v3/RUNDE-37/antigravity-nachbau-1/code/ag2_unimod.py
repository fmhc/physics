#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ANTIGRAVITY-NACHBAU-1, AG2: Unimodulare Bedingung (Volumen fest) an M_eff aus NETZ-NICHTLINEAR-1 (nn.py, Lesart G1).

nn.py, td.py, uf.py usw. werden unveraendert aus /home/fmh/fmhc-physics-remote/netz-nichtlinear-1/code importiert.
Jede gebaute NetzG-Instanz (start, alt_gd, neu_gd, neu_hg) wird zusaetzlich ausgewertet:
  - C (E x nV): Ableitung der Eckvolumen V_v = sum_{t an v} V_t / 4 nach a_e (l = l0 (1 + a), am gedehnten Netz l0 f)
  - global: c = Summe der Spalten (Gesamtvolumen)
  (a) M_eff (E x E) eingeschraenkt auf Kern(C^T) bzw. Kern(c^T): Zahl negativer Eigenwerte (Kartenmass, M_n_neg)
  (b) Dynamik auf der Zwangsflaeche x (a = S x), zusaetzlich C^T S x = 0 (holonom): Kinetik Z^T Ar^-1 Z, Potential
      Z^T Br Z; Zahl negativer Kinetik-Richtungen und wachsender Moden (omega^2 < 0 oder komplex, Schwelle td.TAU_REL)
Abbruch nach dem ersten (bzw. --zugmax+1) ausgefuehrten Zug ueber nn.lauf (zugmax).
"""
import json, os, sys, time, platform
import numpy as np
import scipy
import scipy.linalg as sla

NNCODE = '/home/fmh/fmhc-physics-remote/netz-nichtlinear-1/code'
sys.path.insert(0, NNCODE)
import nn  # noqa: E402
import tg  # noqa: E402
import td  # noqa: E402

TOL = 1e-10
REK = []


def cm_vol(l6):
    """l6 (T,6) in tg.PAARE-Reihenfolge -> Volumen (T,)."""
    T = len(l6)
    M = np.ones((T, 5, 5))
    M[:, 0, 0] = 0
    for i in range(4):
        M[:, i + 1, i + 1] = 0
    for p, (i, j, _, _) in enumerate(tg.PAARE):
        M[:, i + 1, j + 1] = M[:, j + 1, i + 1] = l6[:, p] ** 2
    return np.sqrt(np.clip(np.linalg.det(M) / 288.0, 0, None))


def zwang(N):
    mod = N.mod
    eidx = mod['eidx']
    l0 = mod['l']
    l = l0 * N.f
    l6 = l[eidx]
    T = len(l6)
    V0 = cm_vol(l6)
    dV = np.zeros((T, 6))
    for p in range(6):
        h = 1e-6 * l6[:, p]
        lp, lm = l6.copy(), l6.copy()
        lp[:, p] += h
        lm[:, p] -= h
        dV[:, p] = (cm_vol(lp) - cm_vol(lm)) / (2 * h)
    dVa = dV * l0[eidx]                                # d V_t / d a_e
    nV = N.nV
    C = np.zeros((N.E, nV))
    for c in range(4):
        v = N.G[:, c]
        for p in range(6):
            np.add.at(C, (eidx[:, p], v), 0.25 * dVa[:, p])
    return C, V0


def neg(ev, s=None):
    s = np.abs(ev).max() if s is None else s
    return int((ev < -TOL * s).sum())


def auswerten(N, rolle):
    t0 = time.time()
    C, V0 = zwang(N)
    c = C.sum(1, keepdims=True)
    M = 0.5 * (N.M + N.M.T)
    r = {'rolle': rolle, 'E': int(N.E), 'nV': int(N.nV), 'T': int(len(N.G)), 'vol_summe': float(V0.sum()),
         'M_n_neg_selbst': neg(np.linalg.eigvalsh(M)), 'M_n_neg_code': N.meff.get('M_n_neg'),
         'A_pd': bool(N.A_pd), 'n_wachsend_code': (N.eig or {}).get('n_wachsend')}
    for name, Cm in (('global', c), ('lokal', C)):
        Z = sla.null_space(Cm.T)
        R = Z.T @ M @ Z
        r['M_neg_' + name] = neg(np.linalg.eigvalsh(0.5 * (R + R.T)))
        r['rang_' + name] = int(N.E - Z.shape[1])
        # Dynamik auf der Zwangsflaeche
        Cx = N.S.T @ Cm
        Zx = sla.null_space(Cx.T)
        Ainv = np.linalg.inv(N.Ar)
        Kr = Zx.T @ Ainv @ Zx
        Kr = 0.5 * (Kr + Kr.T)
        Vr = Zx.T @ N.Br @ Zx
        Vr = 0.5 * (Vr + Vr.T)
        r['kin_neg_' + name] = neg(np.linalg.eigvalsh(Kr))
        w = sla.eigvals(Vr, Kr)
        s = float(np.abs(w).max())
        tau = td.TAU_REL * s
        r['wachsend_' + name] = int(((w.real < -tau) | (np.abs(w.imag) > tau)).sum())
        r['dim_x_' + name] = int(Zx.shape[1])
    # ohne Zwang, gleiche Auswertung (Kontrolle gegen td.spektrum)
    Ainv = np.linalg.inv(N.Ar)
    w = sla.eigvals(0.5 * (N.Br + N.Br.T), 0.5 * (Ainv + Ainv.T))
    s = float(np.abs(w).max())
    r['wachsend_ohne'] = int(((w.real < -td.TAU_REL * s) | (np.abs(w.imag) > td.TAU_REL * s)).sum())
    r['kin_neg_ohne'] = neg(np.linalg.eigvalsh(0.5 * (Ainv + Ainv.T)))
    r['t_s'] = time.time() - t0
    REK.append(r)
    print('auswertung', json.dumps(r), flush=True)


_Orig = nn.NetzG


class NetzU(_Orig):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        auswerten(self, k.get('rolle', ''))


nn.NetzG = NetzU


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--netz', default='glas-N128-s2')
    ap.add_argument('--lesart', default='P')
    ap.add_argument('--zugmax', type=int, default=0)
    ap.add_argument('--budget', type=float, default=420.0)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    ns = argparse.Namespace(modus='lauf', netz=a.netz, A=1e-3, arm='b', lesart=a.lesart, h=0.5, perioden=10, proben=50,
                            budget=a.budget, split=1, vergleich=1, hmax=100.0, zugmax=a.zugmax, bgd=1, vorlauf=0.0,
                            out=a.out + '.nn')
    nn.B_GD['an'] = True
    t0 = time.time()
    erg = nn.lauf(ns)
    ev = [{k: e.get(k) for k in ('t', 'typ', 'mu_hg', 'ausgefuehrt', 'dH_rel')} for e in erg['ereignisse']]
    res = {'info': {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
                    'host': platform.node(), 'argv': sys.argv, 'nn_sha256': td.sha(nn.__file__)},
           'netz': a.netz, 'lesart': a.lesart, 'abbruch': erg.get('abbruch'), 'ereignisse': ev, 'auswertung': REK,
           'laufzeit_s': time.time() - t0}
    with open(a.out, 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    for p in (ns.out + '.zustand.npz', ns.out + '.zustand.json'):
        if os.path.exists(p):
            os.remove(p)
    print('fertig %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
