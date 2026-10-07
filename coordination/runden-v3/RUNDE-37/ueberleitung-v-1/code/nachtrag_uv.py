#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-V-1, Nachtrag nach Sicht (beschreibend, nicht geurteilt, nicht eingefroren).

Anlass: Auf V haengen die Bloecke stark und unregelmaessig von h ab (UV1 d bis 8,7e3), der Extrapolationsfehler von
M_eff ist O(1) bis O(100), damit ist die Grenzform nach Plan nicht bestimmbar. Hier wird beschreibend untersucht:
  N1 V, 3 k, h = 1 ... 1/256 (Schema ls): Eigenwerte von D_0 (L-Block; Pole?), Spektrum von M_eff(h) (welche Werte wachsen
     wie 1/h?), Normen S0_nn, S1_qq (Kreisel), Abstand V_eff(h) - B, Lapse-Kopplung gegen Code-c.
  N2 V, dieselben k: schemafreie q-Form (Schur ueber alle zeitartigen Groessen n, beta, L): Q_0(h) gegen B, Spektrum Q_2(h).
  N3 Kuhn, Schema ls: Reduktion am BZ-Rand (k_i = pi): dim_red, omega^2 / Summe 4 sin^2(k_i/2), wachsend.
Importiert uv.py (eingefroren) unveraendert.
"""
import argparse, json, sys, os, time, platform
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import uv  # noqa: E402
import tg  # noqa: E402
import tti  # noqa: E402

H_N = [2.0 ** -j for j in range(9)]


def herm(X):
    return 0.5 * (X + np.conj(X.T))


def n1_n2(vl, mod, zu, ks):
    V0 = vl[0]
    nq, NV = V0.nq, V0.NV
    IQ = list(range(nq)); IN = list(range(nq, nq + NV)); IB = list(range(nq + NV, nq + 4 * NV))
    Bs, A1s, M, c = tg.ops(mod, ks)
    B = herm(Bs.toarray())
    U = zu.U(ks)
    UH = np.conj(U.T)
    zeilen = []
    for V in vl:
        # D_0 des L-Blocks
        S, d = V.bloecke(ks, 'ls', pmax=2)
        z = {'h': V.h, 'D0_min_rel': d.get('D0_min_rel'), 'grund': d.get('grund')}
        if S is None:
            zeilen.append(z)
            continue
        Meff = herm(UH @ S[2][np.ix_(IQ, IQ)] @ U)
        ev = np.linalg.eigvalsh(Meff)
        z['Meff_eig'] = [float(x) for x in ev]
        Veff = herm(UH @ S[0][np.ix_(IQ, IQ)] @ U)
        z['r_V'] = float(np.linalg.norm(Veff - B) / np.linalg.norm(B))
        z['S0_nn'] = float(np.linalg.norm(S[0][np.ix_(IN, IN)]))
        z['S0_qq'] = float(np.linalg.norm(S[0][np.ix_(IQ, IQ)]))
        z['S1_qq'] = float(np.linalg.norm(S[1][np.ix_(IQ, IQ)]))
        z['S1_qq_herm_rel'] = float(np.linalg.norm(S[1][np.ix_(IQ, IQ)] - np.conj(S[1][np.ix_(IQ, IQ)].T))
                                    / max(np.linalg.norm(S[1][np.ix_(IQ, IQ)]), 1e-300))
        Cv = UH @ S[0][np.ix_(IQ, IN)]
        kap = np.vdot(c, Cv) / np.vdot(c, c)
        z['C_rest_kappa'] = float(np.linalg.norm(Cv - kap * c) / np.linalg.norm(Cv))
        z['kappa'] = [float(kap.real), float(kap.imag)]
        # L-Block selbst (Eigenwerte von D_0) ueber eine zweite Zerlegung
        Jm, nL, rB = V.J_mats(ks, 'ls')
        h = V.h
        C = V.lau.koeff(np.asarray(ks, float))
        lD = V.g.l
        H0 = sum(lD[:, None] * Cm * lD[None, :] for Cm in C.values())
        J0 = sum(Jm.values())
        P0 = -(np.conj(J0.T) @ H0 @ J0) / h
        nK = nq + 4 * NV
        evD = np.linalg.eigvalsh(herm(P0[nK:, nK:]))
        z['D0_eig_klein'] = [float(x) for x in sorted(evD, key=abs)[:4]]
        z['D0_n_neg'] = int((evD < 0).sum())
        z['D0_absmax'] = float(np.abs(evD).max())
        # N2: schemafreie q-Form (Schur ueber n, beta)
        Q, kond = uv.schur_reihe(S, IQ, IN + IB)
        z['nb_kond'] = kond
        if Q is not None:
            Q0 = herm(UH @ Q[0] @ U)
            Q2 = herm(UH @ Q[2] @ U)
            z['Q0_gegen_B'] = float(np.linalg.norm(Q0 - B) / np.linalg.norm(B))
            z['Q0_norm'] = float(np.linalg.norm(Q0))
            e2 = np.linalg.eigvalsh(Q2)
            z['Q2_eig_betrag_gross'] = [float(x) for x in sorted(e2, key=abs)[-6:]]
            z['Q2_norm'] = float(np.linalg.norm(Q2))
            Q1 = UH @ Q[1] @ U
            z['Q1_norm'] = float(np.linalg.norm(Q1))
        zeilen.append(z)
    # Wachstum der M_eff-Eigenwerte: Verhaeltnis |ev(h_j)| / |ev(h_j-1)| sortiert
    return zeilen


def n3(vl, mod, geo, zu, LV):
    out = []
    for p in uv.bz(LV):
        if not p['rand']:
            continue
        r = uv.punkt(vl, mod, geo, zu, p['ks'], ('ls',), 'ls')
        a = r['ls']['sp']['a']
        kub = float(np.sum(4.0 * np.sin(0.5 * p['ks']) ** 2))
        z = {'m': p['m'], 'definiert': a.get('definiert'), 'grund': a.get('grund'), 'n_u': a.get('n_u'),
             'dim_red': a.get('dim_red'), 'n_wachsend': a.get('n_wachsend'), 'B_red_pd': a.get('B_red_pd')}
        if a.get('w2_klein') is not None:
            eps = float(np.linalg.norm(p['ks']))
            z['w2_durch_kubisch'] = [float(x) * eps ** 2 / kub for x in a['w2_klein']]
        out.append(z)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('teil', choices=['v', 'kuhn'])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    erg = {}
    if a.teil == 'v':
        vl = [uv.Vier('V', h) for h in H_N]
        mod, geo, LV = uv.netz3d('V')
        zu = uv.Zuordnung(vl[0], mod, LV)
        lm = float(mod['l'].mean())
        R = dict(tti.richtungen13())
        kliste = [('100_kl0.05', (0.05 / lm) * R['100']), ('321_kl0.01', (0.01 / lm) * R['321']),
                  ('bz_m_2_3_5', (np.array([2, 3, 5], float) / 8) @ (2 * np.pi * np.linalg.inv(LV).T))]
        erg['n1_n2'] = []
        for nm, ks in kliste:
            erg['n1_n2'].append({'k_name': nm, 'k': [float(x) for x in ks], 'zeilen': n1_n2(vl, mod, zu, ks)})
        erg['h'] = H_N
    else:
        vl = [uv.Vier('KW', h) for h in uv.H7]
        mod, geo, LV = uv.netz3d('KW')
        zu = uv.Zuordnung(vl[0], mod, LV)
        erg['n3'] = n3(vl, mod, geo, zu, LV)
    res = {'info': {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'skript_sha256': uv.sha(os.path.abspath(__file__)), 'uv_sha256': uv.sha(os.path.abspath(uv.__file__)),
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0))},
           'ergebnis': erg, 'laufzeit_s': time.time() - t0}
    tg.schreibe(a.out, res)
    print('fertig nachtrag', a.teil, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
