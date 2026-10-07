#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FADEN-PUMPEN-1 (Runde 50), Rechen-Agent fuer die Leitung claude-primary, 05.10.2026.

Kurze Zeitentwicklung des Q-Schlauchs in einer periodischen 3D-Kiste (L x L Zellen quer, Lz Zellen laengs) auf V oder
SC (gitter.netz). Start: stationaerer Gitter-Schlauch aus gitter.stationaer_q (eine Periode), laengs wiederholt,
mal (1 + eps * Rauschen) (Zufallszahlen mit festem Saatwert), phi_t = i om phi.
Leapfrog: *0 phi_tt = -Lap phi - *0 U'(|phi|^2) phi. Ausgabe: Ladung je Laengsscheibe (Zelle) zu Zeitpunkten,
Fourier-Amplituden laengs, Energie- und Ladungserhaltung, Zahl der Perlen (Maxima der Ladung je Scheibe).
Aufruf nur ueber kleintest.sh auf der .69:
  python zeit.py --geo SC --om 0.8 --h 0.5 --L 48 --Lz 302 --tend 400 --out lauf/zeit-SC-o0.8.json
"""
import argparse, json, os, sys, time, math
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rad  # noqa: E402
import gitter  # noqa: E402

T0 = time.time()


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def kiste3d(nz, L, Lz, h):
    pos, B = nz['pos'], nz['B']
    nV = len(pos)
    Binv = np.linalg.inv(B)
    g = np.arange(L)
    gz = np.arange(Lz)
    nn = np.stack(np.meshgrid(g, g, gz, indexing='ij'), -1).reshape(-1, 3)
    N = L * L * Lz * nV

    def idx(c1, c2, c3, s):
        return ((np.mod(c1, L) * L + np.mod(c2, L)) * Lz + np.mod(c3, Lz)) * nV + s
    tl, hd, w1 = [], [], []
    for (s, s2, T, w) in nz['kanten']:
        ci = np.rint(T @ Binv).astype(int)
        tl.append(idx(nn[:, 0], nn[:, 1], nn[:, 2], s))
        hd.append(idx(nn[:, 0] + ci[0], nn[:, 1] + ci[1], nn[:, 2] + ci[2], s2))
        w1.append(np.full(len(nn), w))
    tl, hd, w1 = map(np.concatenate, (tl, hd, w1))
    ne = len(tl)
    rows = np.concatenate([np.arange(ne), np.arange(ne)])
    D = sps.csr_matrix((np.concatenate([np.ones(ne), -np.ones(ne)]), (rows, np.concatenate([hd, tl]))), shape=(ne, N))
    s0 = np.tile(nz['s0'], L * L * Lz) * h ** 3
    s1 = w1 * h
    scheibe = np.repeat(nn[:, 2], nV)            # Laengszelle je Ecke
    quer = np.repeat((nn[:, 0] * L + nn[:, 1]), nV) * nV + np.tile(np.arange(nV), L * L * Lz)   # Index in der Querzelle
    return D, s0, s1, scheibe, quer, N


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--geo', default='SC')
    ap.add_argument('--om', type=float, default=0.8)
    ap.add_argument('--h', type=float, default=0.5)
    ap.add_argument('--L', type=int, default=48)
    ap.add_argument('--Lz', type=int, default=200)
    ap.add_argument('--tend', type=float, default=400.0)
    ap.add_argument('--eps', type=float, default=1e-3)
    ap.add_argument('--seed', type=int, default=20261005)
    ap.add_argument('--dtfak', type=float, default=0.4)
    ap.add_argument('--dtaus', type=float, default=10.0)
    ap.add_argument('--tmax', type=float, default=540.0)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    log('start', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), sys.argv)
    nz = gitter.netz(a.geo)
    h = a.h
    # stationaerer Schlauch auf einer Periode
    sz = gitter.superzelle(nz, a.L, h)
    R = rad.Radial(0.02, 60.0)
    fk, info = rad.profil_q(a.om, R)
    kk = rad.kenn_q(a.om, R, fk)
    f_start = np.interp(sz['r'], R.r, fk, right=0.0)
    f1, st = gitter.stationaer_q(sz, a.om, h, kk['q'], f_start, 20000, 120.0)
    om = st['om_gitter']
    log('stationaer', st)
    D, s0, s1, scheibe, quer, N = kiste3d(nz, a.L, a.Lz, h)
    log('Kiste', a.geo, a.L, a.Lz, 'N', N, 'Kanten', D.shape[0], 'Laenge', a.Lz * sz['periode'])
    rng = np.random.default_rng(a.seed)
    f = f1[quer]
    phi = f * (1 + a.eps * (rng.standard_normal(N) + 1j * rng.standard_normal(N)))
    pi = 1j * om * phi
    DT = D.T.tocsr()

    def lapl(p):
        return DT @ (s1 * (D @ p))

    def beschl(p):
        S = (p * p.conj()).real
        return -lapl(p) / s0 - rad.Up(S) * p

    # Zeitschritt aus der groessten Eigenfrequenz von M^-1 Lap (+ 2 als Sicherheit fuer U')
    mi = sps.diags(1.0 / np.sqrt(s0))
    Hs = (mi @ (D.T @ sps.diags(s1) @ D) @ mi).tocsr()
    lmax = float(spla.eigsh(Hs, k=1, which='LA', tol=1e-3, return_eigenvectors=False)[0])
    wmax = math.sqrt(lmax + 2.0)
    dt = a.dtfak * 2.0 / wmax
    nst = int(math.ceil(a.tend / dt))
    dt = a.tend / nst
    log('lmax', lmax, 'dt', dt, 'Schritte', nst)

    def messen(t, p, q):
        S = (p * p.conj()).real
        dp = D @ p
        E = float(np.sum(s0 * (q * q.conj()).real) + np.sum(s1 * (dp * dp.conj()).real) + np.sum(s0 * rad.U(S)))
        rho = 2 * s0 * (p.conj() * q).imag
        Qs = np.bincount(scheibe, weights=rho, minlength=a.Lz)
        F = np.abs(np.fft.rfft(Qs)) / a.Lz
        return {'t': t, 'E': E, 'Q': float(Qs.sum()), 'Q_scheibe': [float(x) for x in Qs],
                'fourier_1_12': [float(x) for x in F[1:13]], 'Q_scheibe_max_durch_mittel': float(Qs.max() / Qs.mean())}
    aus = []
    aus.append(messen(0.0, phi, pi))
    naus = max(1, int(round(a.dtaus / dt)))
    acc = beschl(phi)
    t_lauf = time.time()
    abbruch = None
    for it in range(1, nst + 1):
        pi = pi + 0.5 * dt * acc
        phi = phi + dt * pi
        acc = beschl(phi)
        pi = pi + 0.5 * dt * acc
        if it % naus == 0 or it == nst:
            m = messen(it * dt, phi, pi)
            aus.append(m)
            log('t %.1f E %.6f Q %.6f max/mittel %.4f F1-8 %s' % (m['t'], m['E'], m['Q'], m['Q_scheibe_max_durch_mittel'],
                                                                 [round(x, 4) for x in m['fourier_1_12'][:8]]))
            if time.time() - T0 > a.tmax:
                abbruch = 'Zeitgrenze bei t = %.1f' % (it * dt)
                break
    # Perlen zaehlen: lokale Maxima der Ladung je Scheibe (periodisch) ueber 1,5 x Mittel
    def perlen(Qs):
        Qs = np.asarray(Qs)
        m = Qs.mean()
        mx = (Qs > np.roll(Qs, 1)) & (Qs >= np.roll(Qs, -1)) & (Qs > 1.5 * m)
        return int(mx.sum()), [int(i) for i in np.nonzero(mx)[0]]
    zaehl = [{'t': m['t'], 'perlen': perlen(m['Q_scheibe'])[0], 'orte': perlen(m['Q_scheibe'])[1]} for m in aus]
    res = {'geo': a.geo, 'om_kont': a.om, 'om_gitter': om, 'h': h, 'L': a.L, 'Lz': a.Lz, 'periode': sz['periode'],
           'laenge': a.Lz * sz['periode'], 'eps': a.eps, 'seed': a.seed, 'dt': dt, 'stationaer': st,
           'kont': kk, 'abbruch': abbruch, 'perlen': zaehl, 'messungen': aus,
           'E_drift_rel': (aus[-1]['E'] - aus[0]['E']) / aus[0]['E'], 'Q_drift_rel': (aus[-1]['Q'] - aus[0]['Q']) / aus[0]['Q'],
           'laufzeit_schleife_s': time.time() - t_lauf}
    gitter.schreibe(a.out, res)


if __name__ == '__main__':
    main()
