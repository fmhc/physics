#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, Variante B sauberer (nach Sicht geschrieben; bn.py unveraendert importiert).

Wie bn_quelle.py (nur Lapse), aber der gleichmaessige Torus-Anteil von SM = W^H M lam2 wird je Untergitter abgezogen:
b_s = Mittel von SM ueber die Ecken des Untergitters s mit r >= 0,375 L. Ausgabe je Schale [r0, r0 + w), w = 1 und 2:
SG, SF, SM, SM_lok, QT (alles Summen), damit bn_extra2.py A und B extrapoliert.
"""
import json, sys, os, time, resource
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bn  # noqa: E402

Q = bn.Q


def main():
    L = int(sys.argv[1])
    name = sys.argv[2]
    out_pfad = sys.argv[3]
    t0 = time.time()
    net = bn.Netz(L)
    E, nV, Nk = net.E, net.nV, net.Nk
    v0 = bn.QUELLEN[name]
    sig, a1, mu1, lam1, im1 = bn.erste_ordnung(net, [v0])
    h = 1e-2
    f1, g1, _, _ = bn.zweite_quelle(net, a1[..., 0], mu1[..., 0], sig[..., 0], h)
    f2, g2, _, _ = bn.zweite_quelle(net, a1[..., 0], mu1[..., 0], sig[..., 0], 2 * h)
    Q2F = ((4 * f1 - f2) / 3)[..., None]
    Q2G = ((4 * g1 - g2) / 3)[..., None]
    x2, _, _, mlam2k, _ = net.loese(-net.hin(Q2F), -net.hin(Q2G))
    T1k = net.hin(0.5 * mu1 ** 2)
    Q2Fk, Q2Gk = net.hin(Q2F), net.hin(Q2G)
    fk = {nm: np.zeros((Nk, nV, 1), complex) for nm in ('Tm', 'SG', 'SF', 'SM')}
    for i0 in range(0, Nk, 64):
        idx = np.arange(i0, min(i0 + 64, Nk))
        K, M, W, B, c = net.K_chunk(net.kgrid[idx])
        WH = bn.cT(W)
        P = -WH @ B @ W
        fk['Tm'][idx] = P @ T1k[idx]
        fk['SG'][idx] = Q2Gk[idx]
        fk['SF'][idx] = WH @ Q2Fk[idx]
        fk['SM'][idx] = WH @ mlam2k[idx]
    f = {nm: net.zurueck(v)[0][..., 0] for nm, v in fk.items()}
    r = net.r_von(v0)
    sub = np.broadcast_to(np.arange(nV), r.shape)
    fern = r >= 0.375 * L
    b_s = np.array([f['SM'][fern & (sub == s)].mean() for s in range(nV)])
    SMlok = f['SM'] - b_s[sub]
    out = {'L': L, 'quelle': name, 'Vtor_lP3': net.Vtor, 'b_s': b_s.tolist(), 'schalen': {}}
    for w in (1.0, 2.0):
        sch = []
        for a0 in np.arange(0.0, 0.5 * L, w):
            s = (r >= a0) & (r < a0 + w)
            if not s.any():
                continue
            sch.append({'r0': float(a0), 'w': w, 'r_mittel': float(r[s].mean()), 'n': int(s.sum()),
                        'SG': float(f['SG'][s].sum()), 'SF': float(f['SF'][s].sum()), 'SM': float(f['SM'][s].sum()),
                        'SM_lok': float(SMlok[s].sum()), 'QT': float(Q * f['Tm'][s].sum())})
        out['schalen'][str(w)] = sch
    out['zeit_s'] = time.time() - t0
    out['max_rss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    with open(out_pfad, 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({'L': L, 'zeit_s': out['zeit_s'], 'b_s': out['b_s']}))


if __name__ == '__main__':
    main()
