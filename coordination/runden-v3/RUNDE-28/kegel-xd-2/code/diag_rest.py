#!/usr/bin/env python3
"""KEGEL-XD-2, nachtraegliche Kontrolle (nicht im eingefrorenen Plan): Wo sitzt der Restgradient des L-BFGS-Loesers,
und wie viel Energie steckt noch darin?

Rechnet einzelne Punkte genau wie ball2d (eingefrorener Code kegel_xd2.py, unveraendert importiert) und danach:
  - Ort des groessten Rests |gL/(2w)| (r, phi), Rest nach r-Bereichen
  - Energieschaetzung eines Diagonal-Newton-Schritts: dE_est = -1/2 Sum gL_i^2 / H_ii
  - 400 rot-schwarze nichtlineare Gauss-Seidel-Halbschritte (je Zelle Newton in f_i bei festem m; omega^2 aus I neu)
    und die Aenderung von E_korr = E + m c.
"""
import json
import math
import os
import sys
import time

for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import kegel_xd2 as kx


def diag_H(K, f, om2, m, gu, N0):
    S = f * f
    Kd = np.zeros(K.shape)
    Kd[:-1] += K.cr[:-1, None]
    Kd[1:] += K.cr[:-1, None]
    Kd[-1] += K.cr[-1]
    nb = np.full(K.Np, 2.0)
    nb[0] -= 1.0
    nb[-1] -= 1.0
    Kd += K.cp[:, None] * nb[None, :]
    w2 = K.w[:, None]
    return 2 * Kd + 2 * w2 * (kx.dU(S) + 2 * S * kx.d2U(S) - om2 + m * gu / N0)


def zustand(K, Q, f, m, gu, N0):
    S, I, G, V, gG = K.teile(f)
    E = Q * Q / (4 * I) + G + V
    om2 = Q * Q / (4 * I * I)
    c = float(K.w @ (S * gu).sum(axis=1)) / N0
    w2 = K.w[:, None]
    gL = gG + 2 * w2 * f * (kx.dU(S) - om2 + m * gu / N0)
    return E, om2, c, gL


def main():
    k, dr, m_g, rmax, Q = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
    ds = [float(x) for x in sys.argv[6].split(',')]
    aus = sys.argv[7]
    K = kx.Kegel2D(dr, rmax, m_g, k)
    rad, fam = kx.baue_familie(2, 0.01, 60.0, 0.62)
    gQ, fQ = kx.loese_Q(rad, fam, Q)
    gsQ, fsQ = kx.loese_Q(rad, fam, K.s * Q) if k != 0 else (gQ, fQ)
    erg = dict(k=k, dr=dr, m=m_g, rmax=rmax, Q=Q, punkte=[])
    for d in ds:
        t0 = time.perf_counter()
        prof = fsQ if d == 0.0 else fQ
        f0 = np.interp(K.abstand(d), rad.r, prof, right=0.0)
        D = d ** K.s
        r, f = kx.loese_kegel(K, Q, D, f0, 5.0, 1e-9, 8, 20000, time.perf_counter() + 400.0, 12)
        gu = K.u - D
        N0 = r['N0']
        mm = r['m']
        E, om2, c, gL = zustand(K, Q, f, mm, gu, N0)
        Ek0 = E + mm * c
        w2 = K.w[:, None]
        res = np.abs(gL / (2 * w2))
        j, l = np.unravel_index(int(np.argmax(res)), res.shape)
        H = diag_H(K, f, om2, mm, gu, N0)
        pos = H > 0
        dE_est = -0.5 * float(np.sum(gL[pos] ** 2 / H[pos]))
        bins = [0, 0.5, 2, 5, 10, 20, 30, 41]
        rb = []
        for a, b in zip(bins[:-1], bins[1:]):
            sel = (K.r >= a) & (K.r < b)
            if sel.any():
                rb.append(dict(r_von=a, r_bis=b, res_max=float(res[sel].max()),
                               dE_est=-0.5 * float(np.sum((gL[sel] ** 2 / np.where(H[sel] > 0, H[sel], np.inf))))))
        # rot-schwarzes nichtlineares Gauss-Seidel bei festem m
        jj, ll = np.meshgrid(np.arange(K.Nr), np.arange(K.Np), indexing='ij')
        farbe = (jj + ll) % 2
        verlauf = []
        for it in range(400):
            for col in (0, 1):
                E, om2, c, gL = zustand(K, Q, f, mm, gu, N0)
                H = diag_H(K, f, om2, mm, gu, N0)
                sel = (farbe == col) & (H > 0)
                f = f - np.where(sel, gL / np.where(H > 0, H, 1.0), 0.0)
            if it % 100 == 99:
                E, om2, c, gL = zustand(K, Q, f, mm, gu, N0)
                verlauf.append(dict(it=it + 1, E=E, c=c, E_korr=E + mm * c,
                                    res_max=float(np.max(np.abs(gL / (2 * w2))))))
        E, om2, c, gL = zustand(K, Q, f, mm, gu, N0)
        p = dict(d=d, E=r['E'], c=r['c'], m=mm, E_korr=Ek0, res_max=float(res.max()), ort_j=int(j), ort_l=int(l),
                 ort_r=float(K.r[j]), ort_phi=float(K.phi[l]), ort_f=float(f[j, l]), dE_est=dE_est, bereiche=rb,
                 gs_verlauf=verlauf, E_korr_nach_gs=E + mm * c, dE_korr_gs=E + mm * c - Ek0,
                 res_max_nach_gs=float(np.max(np.abs(gL / (2 * w2)))), dauer_s=time.perf_counter() - t0)
        erg['punkte'].append(p)
        print('d %.2f: E_korr %.12f res %.2e bei r %.3f phi %.4f; dE_est %.2e; nach GS: E_korr %.12f (dE %.2e) res %.2e'
              % (d, Ek0, p['res_max'], p['ort_r'], p['ort_phi'], dE_est, p['E_korr_nach_gs'], p['dE_korr_gs'],
                 p['res_max_nach_gs']), flush=True)
        for b in rb:
            print('   r %4.1f-%4.1f: res_max %.2e dE_est %.2e' % (b['r_von'], b['r_bis'], b['res_max'], b['dE_est']),
                  flush=True)
        with open(aus, 'w') as fh:
            json.dump(erg, fh, indent=1)


if __name__ == '__main__':
    main()
