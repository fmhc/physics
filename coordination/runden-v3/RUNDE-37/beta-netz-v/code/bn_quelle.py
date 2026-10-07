#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, lokale Probe (nach Sicht auf die Fits geschrieben; bn.py unveraendert importiert).

Die Fits von mu2 sind vom grossen 1/r-Glied (Massenrenormierung) beherrscht. Der Takt-Operator P = -W^H B W
vernichtet 1/r und Konstanten im Vakuum. ART, isotrop, Vakuum: Lap n2 = (2 beta - 1) |grad n1|^2 und
Lap(n1^2/2) = |grad n1|^2, also je Schale R_t = Summe Q P mu2 / Summe Q P(mu1^2/2) = 2 beta - 1.
Quelle von mu2 ohne k = 0-Abzug: S = Q2G + W^H Q2F + W^H M lam2 (= Q P mu2 fuer k != 0).
Raum: P psi2 = -Q2G - c^H rest2; Psi - 1 = psi - psi^2/2 harmonisch -> R_s = Summe(-Q2G - c^H rest2)/Summe P(psi1^2/2)
= 3 delta - 2. Torus (Kontinuum, gleichfoermiger Hintergrund, x = 4 pi r^3/V): R_t = (2 beta - 1 + 2x)/(1 + x),
R_s = (3 delta - 2)/(1 + x).
"""
import json, sys, os, time, resource
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bn  # noqa: E402

Q = bn.Q


def main():
    L = int(sys.argv[1])
    namen = sys.argv[2].split(',')
    out_pfad = sys.argv[3]
    t0 = time.time()
    net = bn.Netz(L)
    E, nV, Nk = net.E, net.nV, net.Nk
    quellen = [bn.QUELLEN[n] for n in namen]
    nq = len(quellen)
    sig, a1, mu1, lam1, im1 = bn.erste_ordnung(net, quellen)
    h = 1e-2
    Q2F = np.zeros((L, L, L, E, nq))
    Q2G = np.zeros((L, L, L, nV, nq))
    for j in range(nq):
        f1, g1, _, _ = bn.zweite_quelle(net, a1[..., j], mu1[..., j], sig[..., j], h)
        f2, g2, _, _ = bn.zweite_quelle(net, a1[..., j], mu1[..., j], sig[..., j], 2 * h)
        Q2F[..., j] = (4 * f1 - f2) / 3
        Q2G[..., j] = (4 * g1 - g2) / 3
    x2, psi2k, rst2k, mlam2k, _ = net.loese(-net.hin(Q2F), -net.hin(Q2G), zerlege=True)
    mu2k = x2[:, E:E + nV]
    psi1 = -Q * mu1
    T1k = net.hin(0.5 * mu1 ** 2)
    Tpk = net.hin(0.5 * psi1 ** 2)
    Q2Fk, Q2Gk = net.hin(Q2F), net.hin(Q2G)
    felder = {nm: np.zeros((Nk, nV, nq), complex) for nm in ('Pmu2', 'Tm', 'SG', 'SF', 'SM', 'Ppsi2', 'Tp', 'cR')}
    for i0 in range(0, Nk, 64):
        idx = np.arange(i0, min(i0 + 64, Nk))
        K, M, W, B, c = net.K_chunk(net.kgrid[idx])
        WH = bn.cT(W)
        P = -WH @ B @ W
        felder['Pmu2'][idx] = P @ mu2k[idx]
        felder['Tm'][idx] = P @ T1k[idx]
        felder['SG'][idx] = Q2Gk[idx]
        felder['SF'][idx] = WH @ Q2Fk[idx]
        felder['SM'][idx] = WH @ mlam2k[idx]
        felder['Ppsi2'][idx] = P @ psi2k[idx]
        felder['Tp'][idx] = P @ Tpk[idx]
        felder['cR'][idx] = bn.cT(c) @ rst2k[idx]
    reell = {nm: net.zurueck(v)[0] for nm, v in felder.items()}
    out = {'L': L, 'quellen': namen, 'Vtor_lP3': net.Vtor, 'lam1_max': lam1, 'imag1': im1, 'ergebnis': {}}
    for j, nm in enumerate(namen):
        r = net.r_von(quellen[j]).ravel()
        f = {k: v[..., j].ravel() for k, v in reell.items()}
        S = f['SG'] + f['SF'] + f['SM']
        # Pruefung: Q P mu2 = S - Mittel(S) je Untergitter (k = 0 nicht geloest)
        Sm = (f['SG'] + f['SF'] + f['SM']).reshape(L ** 3, nV)
        Sm = (Sm - Sm.mean(0)).ravel()
        pr = float(np.abs(Q * f['Pmu2'] - Sm).max() / np.abs(Sm).max())
        sch = []
        for a0 in np.arange(0.0, 0.5 * L, 1.0):
            s = (r >= a0) & (r < a0 + 1.0)
            if not s.any():
                continue
            rbar = float(r[s].mean())
            x = 4 * np.pi * rbar ** 3 / net.Vtor
            St, Tt = float(S[s].sum()), float(Q * f['Tm'][s].sum())
            Rt = St / Tt
            Rt0 = float((f['SG'][s] + f['SF'][s]).sum()) / Tt
            Ss = float((-f['SG'][s] - f['cR'][s]).sum())
            Ts = float(f['Tp'][s].sum())
            Rs = Ss / Ts
            sch.append({'r0': float(a0), 'r_mittel': rbar, 'n': int(s.sum()), 'x_torus': x,
                        'S_summe': St, 'QT_summe': Tt, 'SG': float(f['SG'][s].sum()), 'SF': float(f['SF'][s].sum()),
                        'SM': float(f['SM'][s].sum()), 'R_t': Rt, 'R_t_ohne_SM': Rt0,
                        'beta_lokal_roh': 0.5 * (Rt + 1), 'beta_lokal_torus': 0.5 * (Rt * (1 + x) - 2 * x + 1),
                        'beta_lokal_ohne_SM_torus': 0.5 * (Rt0 * (1 + x) - 2 * x + 1),
                        'R_s': Rs, 'delta_lokal_roh': (Rs + 2) / 3, 'delta_lokal_torus': (Rs * (1 + x) + 2) / 3,
                        'cR_anteil': float(f['cR'][s].sum()) / Ss if Ss != 0 else None})
        # kumulativ ab r_min (Summen ueber Schalen)
        kum = []
        for rmin in (2.0, 3.0, 4.0):
            for rmax in (0.25 * L, 0.375 * L):
                if rmax <= rmin + 1:
                    continue
                s = (r >= rmin) & (r < rmax)
                Rt = float(S[s].sum() / (Q * f['Tm'][s].sum()))
                Rs = float((-f['SG'][s] - f['cR'][s]).sum() / f['Tp'][s].sum())
                kum.append({'rmin': rmin, 'rmax': rmax, 'R_t': Rt, 'beta_roh': 0.5 * (Rt + 1), 'R_s': Rs, 'delta_roh': (Rs + 2) / 3})
        out['ergebnis'][nm] = {'pruef_QPmu2_gegen_S_rel': pr, 'schalen': sch, 'kumulativ': kum}
    out['zeit_s'] = time.time() - t0
    out['max_rss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    with open(out_pfad, 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({'L': L, 'zeit_s': out['zeit_s'], 'max_rss_MB': out['max_rss_MB']}))


if __name__ == '__main__':
    main()
