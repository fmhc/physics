#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-V-1, Nachtrag 2 nach Sicht (beschreibend, nicht geurteilt, nicht eingefroren).

Anlass (nt1): Auf V hat der L-Block D_0 bei mittleren h negative Eigenwerte, die mit kleinerem h verschwinden; die
Nulldurchgaenge liegen bei kleinerem h, je kleiner |k| ist. Erst jenseits davon naehern sich die Bloecke der ADM-Form
(V_eff -> B, C -> kappa c, Lapse-Block und Kreisel -> 0). Hier: Bloecke bei h = 2^-8 ... 2^-14 (Schema ls), Grenzwert
durch quadratische Interpolation in h durch die drei kleinsten h, Fehler gegen die lineare durch die zwei kleinsten;
dann dieselbe Paarung (a) wie im Plan (statische Richtungen per Schur im Potential, R1 mit Code-c) mit diesem Grenzwert.
Punkte: Raster 13 Richtungen x kl = 0,005 ... 0,2 (Teil r) bzw. BZ 511 + K, U (Teile b0, b1).
Importiert uv.py (eingefroren) unveraendert.
"""
import argparse, sys, os, time, platform
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import uv  # noqa: E402
import tg  # noqa: E402

H_F = [2.0 ** -j for j in range(8, 15)]
W_Q = uv.lagrange0(H_F[-3:])
W_L = uv.lagrange0(H_F[-2:])


def herm(X):
    return 0.5 * (X + np.conj(X.T))


def punkt(vl, mod, zu, ks):
    eps = float(np.linalg.norm(ks))
    V0 = vl[0]
    nq, NV = V0.nq, V0.NV
    IQ = list(range(nq)); IN = list(range(nq, nq + NV)); IB = list(range(nq + NV, nq + 4 * NV))
    Bs, A1s, M, c = tg.ops(mod, ks)
    B = herm(Bs.toarray())
    U = zu.U(ks)
    UH = np.conj(U.T)
    Sh, d0neg, herm2 = [], [], []
    for V in vl:
        S, d = V.bloecke(ks, 'ls', pmax=2)
        if S is None:
            return {'definiert': False, 'grund': d.get('grund')}
        Sh.append(S)
        Jm, nL, rB = V.J_mats(ks, 'ls')
        C = V.lau.koeff(np.asarray(ks, float))
        lD = V.g.l
        H0 = sum(lD[:, None] * Cm * lD[None, :] for Cm in C.values())
        J0 = sum(Jm.values())
        P0 = -(np.conj(J0.T) @ H0 @ J0) / V.h
        nK = nq + 4 * NV
        evD = np.linalg.eigvalsh(herm(P0[nK:, nK:]))
        d0neg.append(int((evD < 0).sum()))
        X2 = S[2][np.ix_(IQ, IQ)]
        herm2.append(float(np.linalg.norm(X2 - np.conj(X2.T)) / np.linalg.norm(X2)))
    Sh = np.array(Sh)
    Q = np.einsum('j,jpab->pab', W_Q, Sh[-3:])
    Ql = np.einsum('j,jpab->pab', W_L, Sh[-2:])
    out = {'eps': eps, 'D0_n_neg_je_h': d0neg, 'herm_S2qq_je_h': herm2}
    bl = {'M': (2, IQ, IQ), 'V': (0, IQ, IQ), 'C': (0, IQ, IN), 'X': (1, IQ, IB), 'nn': (0, IN, IN), 'G': (1, IQ, IQ)}
    out['aend_letzte'] = {nm: float(np.linalg.norm(Sh[-1][p][np.ix_(I, J)] - Sh[-2][p][np.ix_(I, J)])
                                    / max(np.linalg.norm(Sh[-1][p][np.ix_(I, J)]), 1e-300)) for nm, (p, I, J) in bl.items()}
    out['norm_letzte'] = {nm: float(np.linalg.norm(Sh[-1][p][np.ix_(I, J)])) for nm, (p, I, J) in bl.items()}
    eM = float(np.linalg.norm(Q[2][np.ix_(IQ, IQ)] - Ql[2][np.ix_(IQ, IQ)]) / np.linalg.norm(Q[2][np.ix_(IQ, IQ)]))
    out['e_M'] = eM
    Meff = herm(UH @ Q[2][np.ix_(IQ, IQ)] @ U)
    Veff = herm(UH @ Q[0][np.ix_(IQ, IQ)] @ U)
    Cv = UH @ Q[0][np.ix_(IQ, IN)]
    X = UH @ Q[1][np.ix_(IQ, IB)]
    G = UH @ Q[1][np.ix_(IQ, IQ)] @ U
    out['r_V'] = float(np.linalg.norm(Veff - B) / np.linalg.norm(B))
    kap = np.vdot(c, Cv) / np.vdot(c, c)
    out['kappa'] = [float(kap.real), float(kap.imag)]
    out['C_rest_kappa'] = float(np.linalg.norm(Cv - kap * c) / np.linalg.norm(Cv))
    out['nn_rel'] = float(np.linalg.norm(Q[0][np.ix_(IN, IN)]) / max(np.linalg.norm(Q[0][np.ix_(IQ, IN)]), 1e-300))
    out['G_rel'] = float(np.linalg.norm(G) * eps / max(np.linalg.norm(Veff), 1e-300))
    MM = Meff @ M
    Y, *_ = np.linalg.lstsq(MM, X, rcond=None)
    out['R_S_rest'] = float(np.linalg.norm(X - MM @ Y) / max(np.linalg.norm(X), 1e-300))
    ev = np.linalg.eigvalsh(Meff)
    out['Meff_eig'] = [float(x) for x in ev]
    out['Meff_min_rel'] = float(np.abs(ev).min() / np.abs(ev).max())
    out['Meff_n_neg'] = int((ev < 0).sum())
    tol = max(1e-10, 100.0 * eM)
    out['tol_null'] = tol
    out['a'] = uv.reduktion(Meff, B, c, M, eps, tol)
    out['a_tol1e-10'] = uv.reduktion(Meff, B, c, M, eps, 1e-10)
    out['a_C'] = uv.reduktion(Meff, B, Cv, M, eps, tol)
    for v in ('a', 'a_tol1e-10', 'a_C'):
        out[v].pop('_vek', None)
    kub = None
    out['definiert'] = True
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('teil', choices=['r', 'b0', 'b1'])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    vl = [uv.Vier('V', h) for h in H_F]
    mod, geo, LV = uv.netz3d('V')
    zu = uv.Zuordnung(vl[0], mod, LV)
    lm = float(mod['l'].mean())
    erg = {'h': H_F, 'l_mittel': lm}
    pts = []
    if a.teil == 'r':
        for p in uv.raster(lm):
            if p['art'] != 'kl':
                continue
            r = punkt(vl, mod, zu, p['ks'])
            r.update({x: y for x, y in p.items() if x != 'ks'})
            pts.append(r)
    else:
        ps = uv.bz(LV, 0 if a.teil == 'b0' else 1) + (uv.extra_V() if a.teil == 'b1' else [])
        for p in ps:
            r = punkt(vl, mod, zu, p['ks'])
            r.update({x: y for x, y in p.items() if x != 'ks'})
            pts.append(r)
    erg['punkte'] = pts
    res = {'info': {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'skript_sha256': uv.sha(os.path.abspath(__file__)), 'uv_sha256': uv.sha(os.path.abspath(uv.__file__)),
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0))},
           'ergebnis': erg, 'laufzeit_s': time.time() - t0}
    tg.schreibe(a.out, res)
    print('fertig nachtrag2', a.teil, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
