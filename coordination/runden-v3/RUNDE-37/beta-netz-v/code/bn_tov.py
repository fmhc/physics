#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, SCHWARZES-LOCH: Kontinuum-Referenz MIT isotropem Druck (nach Sicht auf die Gitterlaeufe geschrieben).
Gleiche Quelle wie bn_ode.py (Koordinaten-Energiedichte E = sqrt(g) rho fest, gleichfoermig fuer r < R0), dazu Druck p:
  Lap Psi = -E/(8 LP Psi)
  div(Psi^2 grad N) = N E/(4 LP) (1 + 3 q),   q = p/rho
  TOV: dp/dr = -(rho + p) N'/N  ->  q' = 6 q phi'/phi - (1 + q) N'/N   (rho ~ phi^-6 innen)
Zwang + Spur + TOV + Regularitaet ergeben die volle statische Einstein-Gleichung (kugelsymmetrisch) [M].
Skalierung wie bn_ode.py (phi(0) = 1, t = s/A_out^2); je t Bisektion auf q(0), bis q(R0) = 0.
"""
import json, sys, math
import numpy as np

LP = math.sqrt(2.0) / 4.0


def integriere(R0, t, qc, n=3000):
    e0 = 3.0 / (4 * math.pi * R0 ** 3)
    c = t * e0 / (8 * LP)
    dd = t * e0 / (4 * LP)
    r = R0 * 1e-5
    y = np.stack([1 - c * r * r / 6, -c * r / 3, 1 + dd * (1 + 3 * qc) * r * r / 6, dd * (1 + 3 * qc) * r / 3, qc.copy()])

    def rhs(r, y):
        ph, php, N, Np, q = y
        return np.stack([php, -2 * php / r - c / ph, Np,
                         -2 * Np / r - 2 * php * Np / ph + dd * (1 + 3 * q) * N / (ph * ph),
                         6 * q * php / ph - (1 + q) * Np / N])
    h = (R0 - r) / n
    for _ in range(n):
        k1 = rhs(r, y)
        k2 = rhs(r + h / 2, y + h / 2 * k1)
        k3 = rhs(r + h / 2, y + h / 2 * k2)
        k4 = rhs(r + h, y + h * k3)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        r += h
    return y


def rechne(R0, ts, n=3000):
    t = np.asarray(ts, float)
    lo = np.zeros_like(t)
    hi = np.full_like(t, 1e4)
    with np.errstate(all='ignore'):
        for _ in range(70):
            mid = np.sqrt(np.maximum(lo, 1e-12) * hi) if True else 0.5 * (lo + hi)
            y = integriere(R0, t, mid, n)
            qR = y[4]
            gut = np.isfinite(qR)
            zu_viel = (~gut) | (qR > 0)
            hi = np.where(zu_viel, mid, hi)
            lo = np.where(zu_viel, lo, mid)
        qc = 0.5 * (lo + hi)
        y = integriere(R0, t, qc, n)
    ph, php, N, Np, q = y
    A = ph + R0 * php
    B = -R0 * R0 * php
    s = t / A ** 2
    m2 = B / A
    x = m2 / R0
    J = R0 * R0 * ph * ph * Np / A ** 2
    Ninf = N + J / (R0 + m2)
    ok = np.isfinite(Ninf) & (A > 0) & (hi < 1e4 * 0.999) & (np.abs(q) < 1e-6 * np.maximum(qc, 1))
    return {'t': t, 'ok': ok, 's': s, 'q_mitte': qc, 'M_iso': 2 * m2, 'x': x, 'kompakt': 4 * x / (1 + x) ** 2,
            'N_mitte_rel': 1 / Ninf, 'K_ueber_M': (J / Ninf) / (2 * m2), 'q_rand': q}


def main():
    out_pfad = sys.argv[1]
    out = {}
    for R0 in (2.0, 3.0):
        ts = np.logspace(-2, 2, 801)
        d = rechne(R0, ts)
        ok = d['ok']
        last = (int(np.argmin(ok)) - 1) if not ok.all() else len(ok) - 1
        z = {'letzter_gueltiger_t': float(ts[last]), 's_max': float(d['s'][:last + 1].max()),
             's_monoton': bool(np.all(np.diff(d['s'][:last + 1]) > 0))}
        i_max = int(np.argmax(d['s'][:last + 1]))
        z['bei_s_max'] = {k: float(d[k][i_max]) for k in ('s', 'x', 'kompakt', 'N_mitte_rel', 'q_mitte', 'K_ueber_M')}
        tab = []
        for j in range(0, last + 1, 20):
            tab.append({k: float(d[k][j]) for k in ('t', 's', 'x', 'kompakt', 'N_mitte_rel', 'q_mitte', 'K_ueber_M')})
        z['tabelle'] = tab
        z['letzte_zeilen'] = [{k: float(d[k][j]) for k in ('t', 's', 'x', 'kompakt', 'N_mitte_rel', 'q_mitte', 'K_ueber_M')}
                              for j in range(max(0, last - 5), min(last + 3, len(ts)))]
        out['R0_%g' % R0] = z
        print('R0 =', R0, json.dumps({k: v for k, v in z.items() if k not in ('tabelle', 'letzte_zeilen')}))
        for row in tab:
            print('  s=%9.3f x=%.4f C=%.4f Nc=%.4f qc=%.4g K/M=%.4f' % (row['s'], row['x'], row['kompakt'], row['N_mitte_rel'], row['q_mitte'], row['K_ueber_M']))
        print('  letzte:')
        for row in z['letzte_zeilen']:
            print('  t=%.4g s=%9.3f x=%.4f C=%.4f Nc=%.4g qc=%.4g' % (row['t'], row['s'], row['x'], row['kompakt'], row['N_mitte_rel'], row['q_mitte']))
    with open(out_pfad, 'w') as f:
        json.dump(out, f, indent=1)


if __name__ == '__main__':
    main()
