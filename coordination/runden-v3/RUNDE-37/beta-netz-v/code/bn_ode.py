#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, Folgeauftrag SCHWARZES-LOCH: Kontinuum-Referenz (kugelsymmetrisch, isotrope Koordinaten g = Psi^4 delta).
Dieselbe Kopplung wie bn.py (H_v = Integral sqrt(g) R = sigma, Takt aus der Spur der statischen Gleichung, ohne Druck),
Laengen in l_P, LP = Finn-Kante in kubischen Einheiten:
  Zwang:  Lap Psi = -E/(8 LP Psi)                  (E = Koordinaten-Energiedichte je l_P^3, fest)
  Takt:   div(Psi^2 grad N) = N E/(4 LP)            (Spur von N G_ij = D_i D_j N - g_ij D^2 N)
Linear: Psi = 1 + A s/(2r), N = 1 - A s/r mit A = 1/(16 pi LP) = 0,05627 je Einheit s (wie auf dem Netz).
Der spurfreie Teil der statischen Gleichung ist fuer ruhenden Staub nicht erfuellbar (ART: Staub braucht Druck) und
fehlt hier; auf dem Netz nimmt M lam diesen Rest auf.
Kugel: E = s 3/(4 pi R0^3) fuer r < R0. Parametrisierung: Psi = phi/A_out mit phi(0) = 1 und t = s/A_out^2
(gleiche Gleichung fuer phi); s(t) = t/A_out(t)^2. Ein Maximum von s(t) waere ein Umkehrpunkt (groesste Masse).
Referenz ART mit Druck (Schwarzschild-Innenloesung, konstante Dichte): N_c/N_inf = (3 sqrt(1 - C) - 1)/2, C = 2M/R [L].
"""
import json, sys, math
import numpy as np

LP = math.sqrt(2.0) / 4.0


def rechne(R0, ts, n=6000):
    e0 = 3.0 / (4 * math.pi * R0 ** 3)
    t = np.asarray(ts, float)
    c = t * e0 / (8 * LP)
    dd = t * e0 / (4 * LP)
    r = R0 * 1e-4
    y = np.stack([1 - c * r * r / 6, -c * r / 3, 1 + dd * r * r / 6, dd * r / 3])
    phmin = y[0].copy()

    def rhs(r, y):
        ph, php, N, Np = y
        return np.stack([php, -2 * php / r - c / ph, Np, -2 * Np / r - 2 * php * Np / ph + dd * N / (ph * ph)])
    h = (R0 - r) / n
    for _ in range(n):
        k1 = rhs(r, y)
        k2 = rhs(r + h / 2, y + h / 2 * k1)
        k3 = rhs(r + h / 2, y + h / 2 * k2)
        k4 = rhs(r + h, y + h * k3)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        with np.errstate(invalid="ignore"):
            phmin = np.fmin(phmin, np.where(np.isfinite(y[0]), y[0], -1.0))
        r += h
    ph, php, N, Np = y
    A = ph + R0 * php
    B = -R0 * R0 * php
    ok = (A > 0) & (phmin > 0) & np.isfinite(A) & np.isfinite(N) & np.isfinite(Np)
    s = t / A ** 2
    m2 = B / A
    x = m2 / R0
    J = R0 * R0 * ph * ph * Np / A ** 2
    Ninf = N + J / (R0 + m2)
    return {'t': t, 'ok': ok, 's': s, 'M_iso': 2 * m2, 'x': x, 'kompakt': 4 * x / (1 + x) ** 2, 'Psi2_mitte': 1 / A ** 2,
            'N_mitte_rel': 1 / Ninf, 'N_rand_rel': N / Ninf, 'K_ueber_M': (J / Ninf) / (2 * m2), 'Psi2_rand': (ph / A) ** 2}


def main():
    out_pfad = sys.argv[1]
    out = {'LP': LP, 'A_je_s': 1 / (16 * math.pi * LP)}
    for R0 in (2.0, 3.0):
        ts = np.logspace(-2, 5, 1401)
        d = rechne(R0, ts)
        ok = d['ok']
        last = (int(np.argmin(ok)) - 1) if not ok.all() else len(ok) - 1
        sv = d['s'][:last + 1]
        mono = bool(np.all(np.diff(sv) > 0))
        # Konvergenz in n: Vergleich mit halber Schrittzahl an ausgewaehlten t
        d2 = rechne(R0, ts[:last + 1:50], n=3000)
        dev = float(np.max(np.abs(d2['N_mitte_rel'] - d['N_mitte_rel'][:last + 1:50])))
        tab = []
        for s_ziel in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096):
            if s_ziel > sv.max():
                continue
            j = int(np.searchsorted(sv, s_ziel))
            j = min(max(j, 1), last)
            f = (math.log(s_ziel) - math.log(sv[j - 1])) / (math.log(sv[j]) - math.log(sv[j - 1]))
            z = {'s': s_ziel}
            for k in ('M_iso', 'x', 'kompakt', 'Psi2_mitte', 'N_mitte_rel', 'N_rand_rel', 'K_ueber_M'):
                z[k] = float(d[k][j - 1] + f * (d[k][j] - d[k][j - 1]))
            C = z['kompakt']
            z['N_mitte_ART_mit_Druck'] = float((3 * math.sqrt(1 - C) - 1) / 2) if C < 1 else None
            tab.append(z)
        i_k = int(np.argmax(d['kompakt'][:last + 1]))
        out['R0_%g' % R0] = {'s_monoton': mono, 's_max_im_Raster': float(sv.max()), 't_letzt': float(ts[last]),
                             'n_halbiert_abw_N_mitte': dev, 'tabelle': tab,
                             'kompakt_max': float(d['kompakt'][i_k]), 's_bei_kompakt_max': float(d['s'][i_k]),
                             'N_mitte_bei_kompakt_max': float(d['N_mitte_rel'][i_k]),
                             'N_mitte_min_im_Raster': float(d['N_mitte_rel'][:last + 1].min())}
    with open(out_pfad, 'w') as f:
        json.dump(out, f, indent=1)
    for k, v in out.items():
        if not k.startswith('R0'):
            continue
        print(k, json.dumps({kk: vv for kk, vv in v.items() if kk != 'tabelle'}))
        for z in v['tabelle']:
            print('  s=%6g M=%.4f x=%.4f C=%.4f Psi2c=%.3f Nc=%.4f NR=%.4f K/M=%.4f  ART-mit-Druck Nc=%s' % (
                z['s'], z['M_iso'], z['x'], z['kompakt'], z['Psi2_mitte'], z['N_mitte_rel'], z['N_rand_rel'], z['K_ueber_M'],
                ('%.4f' % z['N_mitte_ART_mit_Druck']) if z['N_mitte_ART_mit_Druck'] is not None else '-'))


if __name__ == '__main__':
    main()
