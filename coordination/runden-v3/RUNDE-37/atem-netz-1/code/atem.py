#!/usr/bin/env python3
"""ATEM-NETZ-1 (Runde 42, Code-Agent fuer Leitung claude-primary).

Modell (KARTE.md): Punkt i hat den Durchmesser d_i = 1 + eps sin(phi_i) PU.
U = (k/2) sum_{i<j} max(0, (d_i + d_j)/2 - r_ij)^2, k = 1.
Phasen: phi_i' = omega - mu dU/dphi_i + sqrt(2T) xi_i.
Lagen: fest (Teile A, B) oder x_i' = -mu grad_i U (Teil C), mu_x = mu_phi = mu.
Kopplungsmass kappa = mu k eps^2 / (8 omega) = K / omega (K = Kopplung der gemittelten XY-Dynamik).
Einheiten: Laenge PU (Ruhedurchmesser 1), Zeit Takte (omega = 2 pi je Takt).

Nur auf der .69 ueber kleintest.sh (1 Thread). Aufrufe siehe PLAN.md Abschn. 7.
"""
import argparse
import json
import resource
import sys
import time

import numpy as np
import scipy.sparse as sp
from scipy.spatial import cKDTree

OMEGA = 2.0 * np.pi
EPS = 0.10          # Atemamplitude im Durchmesser (PU)
DELTA = 0.12        # Vorpressung fester Gitter: Abstand 1 - DELTA (DELTA > EPS)
KAPPA_W = 0.005     # schwache Kopplung
KAPPA_S = 0.05      # starke Kopplung (Teil C)
T_REL = 1.0e-3      # kleines Rauschen: T / K bei schwacher Kopplung
T_ABS = T_REL * KAPPA_W * OMEGA   # dasselbe absolute T in allen Teilen B und C


def g_aus_kappa(kappa, eps=EPS):
    # kappa = mu k eps^2 / (8 omega), k = 1  ->  g = mu k = 8 omega kappa / eps^2
    return 8.0 * OMEGA * kappa / eps ** 2


def wrap(a):
    return (a + np.pi) % (2.0 * np.pi) - np.pi


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


# ----------------------------------------------------------------------------- Gitter (feste Lagen)
def baue(name, L):
    """liefert N, bonds (M,2), extra (sub: Untergitter +-1, tri: Dreiecke gegen den Uhrzeigersinn, tet: Tetraeder)"""
    if name == 'paar':
        return 2, np.array([[0, 1]]), {'sub': np.array([1, -1])}
    if name == 'kette':        # offen
        b = np.array([[i, i + 1] for i in range(L - 1)])
        return L, b, {'sub': np.array([(-1) ** i for i in range(L)])}
    if name == 'quadrat':      # periodisch, L gerade
        def idx(x, y):
            return (x % L) + L * (y % L)
        b = []
        for y in range(L):
            for x in range(L):
                b.append((idx(x, y), idx(x + 1, y)))
                b.append((idx(x, y), idx(x, y + 1)))
        sub = np.array([(-1) ** (x + y) for y in range(L) for x in range(L)])
        return L * L, np.array(b), {'sub': sub}
    if name == 'dreieck':      # periodisch, L Vielfaches von 3; a1 = (1,0), a2 = (1/2, sqrt3/2)
        def idx(x, y):
            return (x % L) + L * (y % L)
        b, tri = [], []
        for y in range(L):
            for x in range(L):
                b.append((idx(x, y), idx(x + 1, y)))
                b.append((idx(x, y), idx(x, y + 1)))
                b.append((idx(x, y), idx(x - 1, y + 1)))
                tri.append((idx(x, y), idx(x + 1, y), idx(x, y + 1)))              # oben, ccw
                tri.append((idx(x + 1, y), idx(x + 1, y + 1), idx(x, y + 1)))      # unten, ccw
        return L * L, np.array(b), {'tri': np.array(tri)}
    if name in ('diamant', 'pyro'):
        M = 8 * L                                   # ganzzahlige Koordinaten in Einheiten a/8
        fcc = [(0, 0, 0), (0, 4, 4), (4, 0, 4), (4, 4, 0)]
        A = []
        for cx in range(L):
            for cy in range(L):
                for cz in range(L):
                    for f in fcc:
                        A.append(((8 * cx + f[0]) % M, (8 * cy + f[1]) % M, (8 * cz + f[2]) % M))
        nA = len(A)
        B = [((a[0] + 2) % M, (a[1] + 2) % M, (a[2] + 2) % M) for a in A]
        dia = A + B
        dia_idx = {s: i for i, s in enumerate(dia)}
        vs = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
        dia_bonds, tet, mid = [], [], {}
        for i, a in enumerate(A):
            t4 = []
            for v in vs:
                bb = ((a[0] + 2 * v[0]) % M, (a[1] + 2 * v[1]) % M, (a[2] + 2 * v[2]) % M)
                dia_bonds.append((i, dia_idx[bb]))
                m = ((a[0] + v[0]) % M, (a[1] + v[1]) % M, (a[2] + v[2]) % M)
                if m not in mid:
                    mid[m] = len(mid)
                t4.append(mid[m])
            tet.append(t4)
        for jb in range(nA, 2 * nA):
            bb = dia[jb]
            t4 = []
            for v in vs:
                m = ((bb[0] - v[0]) % M, (bb[1] - v[1]) % M, (bb[2] - v[2]) % M)
                t4.append(mid[m])
            tet.append(t4)
        if name == 'diamant':
            sub = np.array([1] * nA + [-1] * nA)
            return 2 * nA, np.array(dia_bonds), {'sub': sub}
        tet = np.array(tet)
        pb = set()
        for t4 in tet:
            for p in range(4):
                for q in range(p + 1, 4):
                    i, j = int(t4[p]), int(t4[q])
                    pb.add((min(i, j), max(i, j)))
        return len(mid), np.array(sorted(pb)), {'tet': tet}
    raise ValueError(name)


class FestNetz:
    """feste Lagen, alle Beruehrungen im Abstand 1 - DELTA; wegen DELTA > EPS dauerhaft (h >= DELTA - EPS > 0)"""

    def __init__(self, N, bonds, kappa, eps=EPS, delta=DELTA):
        i, j = bonds[:, 0], bonds[:, 1]
        A = sp.coo_matrix((np.ones(len(i)), (i, j)), shape=(N, N))
        self.A = (A + A.T).tocsr()
        self.z = np.asarray(self.A.sum(1)).ravel()
        self.N = N
        self.bonds = bonds
        self.kappa = kappa
        self.g = g_aus_kappa(kappa, eps)
        self.K = kappa * OMEGA
        self.eps, self.delta = eps, delta

    def f_voll(self, phi):
        s = np.sin(phi)
        c = np.cos(phi)
        last = self.z * self.delta + 0.5 * self.eps * (self.z * s + self.A @ s)   # sum_j h_ij
        return OMEGA - self.g * 0.5 * self.eps * c * last

    def f_mittel(self, th):
        s = np.sin(th)
        c = np.cos(th)
        return self.K * (s * (self.A @ c) - c * (self.A @ s))   # K sum_j sin(th_i - th_j)


def heun(x, f, dt, sig, rng):
    xi = sig * rng.standard_normal(x.shape) if sig > 0 else 0.0
    k1 = f(x)
    xp = x + dt * k1 + xi
    k2 = f(xp)
    return x + 0.5 * dt * (k1 + k2) + xi


def lauf_fest(f, phi0, takte, dt, T, rng, rotierend, mstep, cb, takt0=0):
    """Takt fuer Takt; cb(n, thbar, phi) mit Takt-gemittelten Phasen relativ zu omega t (rotierend) bzw. direkt"""
    nst = int(round(1.0 / dt))
    sig = np.sqrt(2.0 * T * dt) if T > 0 else 0.0
    phi = phi0.copy()
    for n in range(takt0, takt0 + takte):
        Z = np.zeros(len(phi), complex)
        for k in range(nst):
            phi = heun(phi, f, dt, sig, rng)
            if (k + 1) % mstep == 0:
                t = n + (k + 1) * dt
                Z += np.exp(1j * (phi - (OMEGA * t if rotierend else 0.0)))
        if cb is not None:
            cb(n, np.angle(Z), phi)
    return phi


# ----------------------------------------------------------------------------- Messgroessen (feste Gitter)
def bindung(th, bonds):
    d = th[bonds[:, 0]] - th[bonds[:, 1]]
    return float(np.cos(d).mean()), float(np.cos(2 * d).mean())


def chiral(th, tri):
    a, b, c = th[tri[:, 0]], th[tri[:, 1]], th[tri[:, 2]]
    return (2.0 / (3.0 * np.sqrt(3.0))) * (np.sin(b - a) + np.sin(c - b) + np.sin(a - c))


def tetra(th, tet):
    z1 = np.exp(1j * th)[tet].sum(1)
    z2 = np.exp(2j * th)[tet].sum(1)
    summe = np.abs(z1) / 4.0
    achse = np.angle(z2) / 2.0
    npos = (np.cos(th[tet] - achse[:, None]) > 0).sum(1)
    return {
        'anteil_summe_klein': float((summe < 0.1).mean()),
        'summe_mittel': float(summe.mean()),
        'koll_tetra_mittel': float((np.abs(z2) / 4.0).mean()),
        'anteil_22': float((npos == 2).mean()),
        'anteil_31': float(((npos == 1) | (npos == 3)).mean()),
        'anteil_40': float(((npos == 0) | (npos == 4)).mean()),
    }


def nematisch(th):
    return float(np.abs(np.exp(2j * th).mean()))


def gefroren(phi_jetzt, phi_vorher, W):
    v = (phi_jetzt - phi_vorher) / (OMEGA * W)
    return v < 0.1, v


# ----------------------------------------------------------------------------- Teil A
def teilA(args):
    rauch = args.rauch
    out = {'teil': 'A', 'rauch': rauch, 'kappa': KAPPA_W, 'eps': EPS, 'delta': DELTA, 'T': 0.0}
    K = KAPPA_W * OMEGA
    out['K'] = K
    netze = args.netze.split(',')
    for name in netze:
        t0 = time.time()
        if name == 'paar':
            N, bonds, ex = baue('paar', 0)
            seeds = list(range(1, 9)) if not rauch else [1, 2]
            if args.seedsA:
                seeds = [int(x) for x in args.seedsA.split(",")]
            takte = 400 if not rauch else 200
        else:
            L = {'kette': 32, 'quadrat': 16, 'dreieck': 18, 'diamant': 5}[name]
            N, bonds, ex = baue(name, L)
            seeds = list(range(1, 7)) if not rauch else [1]
            if args.seedsA:
                seeds = [int(x) for x in args.seedsA.split(",")]
            takte = 3000 if not rauch else 300
        netz = FestNetz(N, bonds, KAPPA_W)
        res = []
        for s in seeds:
            rng0 = np.random.default_rng(1000 + s)
            phi0 = rng0.uniform(0, 2 * np.pi, N)
            kurven = {}
            for art in ('voll', 'mittel'):
                rng = np.random.default_rng(2000 + s)
                e_t, d_t = [], []
                endfeld = {}

                def cb(n, th, phi):
                    if name == 'paar':
                        d_t.append(float(np.pi - abs(wrap(th[0] - th[1]))))
                    e_t.append(bindung(th, bonds)[0])
                    if n == takte - 1:
                        endfeld['th'] = th.copy()
                if art == 'voll':
                    lauf_fest(netz.f_voll, phi0, takte, 0.01, 0.0, rng, True, 5, cb)
                else:
                    lauf_fest(netz.f_mittel, phi0, takte, 0.1, 0.0, rng, False, 1, cb)
                th = endfeld['th']
                r = {'e': e_t[::10] if name != 'paar' else e_t, 'e_end': e_t[-1]}
                e0, e1 = e_t[0], e_t[-1]
                halb = 0.5 * (e0 + e1)
                th_ = next((n for n, e in enumerate(e_t) if e <= halb), None)
                if th_ is not None and th_ > 0 and e_t[th_ - 1] != e_t[th_]:
                    # linear zwischen den Takten interpoliert (Takt n = Mittel ueber [n, n+1])
                    th_ = (th_ - 1) + (e_t[th_ - 1] - halb) / (e_t[th_ - 1] - e_t[th_])
                r['t_halb'] = th_
                r['gegentakt_end'] = -e_t[-1]
                if name == 'paar':
                    d = np.array(d_t)
                    r['abstand_pi_end'] = float(d[-1])
                    r['abstand_pi_t'] = [float(x) for x in d[::5]]
                    m = (d > 0.003) & (d < 0.3)
                    tt = np.arange(len(d))[m]
                    if m.sum() >= 5:
                        r['rate'] = float(-np.polyfit(tt, np.log(d[m]), 1)[0])
                    else:
                        r['rate'] = None
                if 'tri' in ex:
                    ch = chiral(th, ex['tri'])
                    r['chi_betrag_mittel'] = float(np.abs(ch).mean())
                    r['chi_betrag_min'] = float(np.abs(ch).min())
                    r['anteil_chi_09'] = float((np.abs(ch) >= 0.9).mean())
                    r['chi_vorzeichen_oben_unten'] = [float(np.sign(ch[0::2]).mean()), float(np.sign(ch[1::2]).mean())]
                if 'sub' in ex and name != 'paar':
                    r['stagg'] = float(np.abs((ex['sub'] * np.exp(1j * th)).mean()))
                kurven[art] = r
            res.append({'seed': s, **kurven})
        out[name] = {'N': int(N), 'M': int(len(bonds)), 'takte': takte, 'seeds': res, 'sek': time.time() - t0}
        print(name, 'fertig', round(time.time() - t0, 1), 's', flush=True)
    out['max_rss_mb'] = rss_mb()
    return out


# ----------------------------------------------------------------------------- Teil B
def teilB1(args):
    """Finns Netz (Pyrochlor) bzw. Diamant, schwache Kopplung, kleines Rauschen, volle Dynamik"""
    name = args.gitter
    L = 4 if name == 'pyro' else 5
    N, bonds, ex = baue(name, L)
    netz = FestNetz(N, bonds, KAPPA_W)
    T = args.T_rel * netz.K
    rng0 = np.random.default_rng(3000 + args.seed)
    phi0 = rng0.uniform(0, 2 * np.pi, N)
    rng = np.random.default_rng(4000 + args.seed)
    takte = args.takte
    jede = args.jede
    reihe = []
    phi_hist = {}

    def cb(n, th, phi):
        if (n + 1) % jede == jede - 10:
            phi_hist['v'] = phi.copy()
        if (n + 1) % jede == 0 or n == 0:
            e, p1 = bindung(th, bonds)
            z = {'takt': n + 1, 'e': e, 'P1': p1, 'S': nematisch(th)}
            if name == 'pyro':
                z.update(tetra(th, ex['tet']))
            else:
                z['stagg'] = float(np.abs((ex['sub'] * np.exp(1j * th)).mean()))
            if 'v' in phi_hist:
                fr, v = gefroren(phi, phi_hist['v'], 10)
                z['gefroren'] = float(fr.mean())
                z['v_mittel'] = float(v.mean())
            reihe.append(z)
            if n + 1 == takte:
                phi_hist['th_end'] = th.copy()
    t0 = time.time()
    lauf_fest(netz.f_voll, phi0, takte, 0.01, T, rng, True, 5, cb)
    out = {'teil': 'B1', 'gitter': name, 'L': L, 'N': int(N), 'M': int(len(bonds)), 'seed': args.seed,
           'kappa': KAPPA_W, 'T_rel': args.T_rel, 'T': T, 'takte': takte, 'reihe': reihe,
           'sek': time.time() - t0, 'max_rss_mb': rss_mb()}
    if 'th_end' in phi_hist:
        out['th_end'] = [round(float(x), 5) for x in phi_hist['th_end']]
    return out


def kappa_gitter(rauch):
    if rauch:
        return list(np.geomspace(0.01, 0.3, 6))
    return list(np.geomspace(0.01, 0.3, 26))


def teilB2(args):
    """starke Kopplung: Anteil eingefrorener Takte gegen kappa (volle Dynamik, Zufallsphasen)"""
    name = args.gitter
    L = 4 if name == 'pyro' else 5
    N, bonds, ex = baue(name, L)
    seeds = [int(s) for s in args.seeds.split(',')]
    takte = 200 if not args.rauch else 100
    W = 50 if not args.rauch else 20
    res = []
    t0 = time.time()
    for kappa in kappa_gitter(args.rauch):
        netz = FestNetz(N, bonds, kappa)
        for s in seeds:
            rng0 = np.random.default_rng(5000 + s)
            phi0 = rng0.uniform(0, 2 * np.pi, N)
            rng = np.random.default_rng(6000 + s)
            st = {}

            def cb(n, th, phi):
                if n == takte - W - 1:
                    st['v'] = phi.copy()
                if n == takte - 1:
                    st['phi'] = phi.copy()
                    st['th'] = th.copy()
            lauf_fest(netz.f_voll, phi0, takte, 0.01, T_ABS, rng, True, 5, cb)
            fr, v = gefroren(st['phi'], st['v'], W)
            z = {'kappa': float(kappa), 'seed': s, 'gefroren': float(fr.mean())}
            # Muster der eingefrorenen Takte
            sinphi = np.sin(st['phi'])
            z['sin_gefroren_mittel'] = float(sinphi[fr].mean()) if fr.any() else None
            if name == 'diamant':
                z['gefroren_A'] = float(fr[ex['sub'] > 0].mean())
                z['gefroren_B'] = float(fr[ex['sub'] < 0].mean())
            else:
                k = fr[ex['tet']].sum(1)
                z['tetra_gefroren_hist'] = [float((k == m).mean()) for m in range(5)]
            lauf = ~fr
            b = bonds
            mlauf = lauf[b[:, 0]] & lauf[b[:, 1]]
            if mlauf.any():
                d = st['th'][b[mlauf, 0]] - st['th'][b[mlauf, 1]]
                z['cos_laufende_bindungen'] = float(np.cos(d).mean())
            res.append(z)
    return {'teil': 'B2', 'gitter': name, 'L': L, 'N': int(N), 'takte': takte, 'W': W, 'T': T_ABS,
            'res': res, 'sek': time.time() - t0, 'max_rss_mb': rss_mb()}


def teilB3(args):
    """Diagnose: gemittelte XY-Dynamik auf Pyrochlor, lange Zeiten (Einheit 1/K)"""
    N, bonds, ex = baue('pyro', 4)
    netz = FestNetz(N, bonds, KAPPA_W)
    K = netz.K
    tmax = 5e4 if not args.rauch else 2e3          # in Einheiten 1/K
    dtK = 0.1
    dt = dtK / K
    nsteps = int(round(tmax / dtK))
    marken = sorted(set(int(round(x)) for x in np.geomspace(1, nsteps, 40)))
    out = {'teil': 'B3', 'N': int(N), 'tmax_K': tmax, 'dt_K': dtK, 'laeufe': []}
    t0 = time.time()
    for trel in (0.0, 1e-3):
        rng0 = np.random.default_rng(7001)
        th = rng0.uniform(0, 2 * np.pi, N)
        rng = np.random.default_rng(7002)
        sig = np.sqrt(2 * trel * K * dt) if trel > 0 else 0.0
        reihe = []
        mi = 0
        for k in range(1, nsteps + 1):
            th = heun(th, netz.f_mittel, dt, sig, rng)
            if mi < len(marken) and k == marken[mi]:
                e, p1 = bindung(th, bonds)
                z = {'t_K': k * dtK, 'e': e, 'P1': p1, 'S': nematisch(th)}
                z.update(tetra(th, ex['tet']))
                reihe.append(z)
                mi += 1
        out['laeufe'].append({'T_rel': trel, 'reihe': reihe})
    out['sek'] = time.time() - t0
    out['max_rss_mb'] = rss_mb()
    return out


# ----------------------------------------------------------------------------- Teil C (freie Punkte)
class Frei:
    def __init__(self, N, dim, packung, rng):
        self.N, self.dim = N, dim
        if dim == 2:
            self.L = np.sqrt(N * (np.pi / 4.0) / packung)
        else:
            self.L = (N * (np.pi / 6.0) / packung) ** (1.0 / 3.0)
        self.skin = 0.3
        self.rc = 1.0 + EPS + self.skin
        self.x = rng.uniform(0, self.L, (N, dim))
        self.baue_liste(self.x)

    def baue_liste(self, x):
        tree = cKDTree(np.mod(x, self.L), boxsize=self.L)
        p = tree.query_pairs(self.rc, output_type='ndarray')
        self.pi, self.pj = p[:, 0], p[:, 1]
        self.x_ref = x.copy()
        self.n_listen = getattr(self, 'n_listen', 0) + 1

    def pruefe_liste(self, x):
        if np.max(np.sum((x - self.x_ref) ** 2, 1)) > (0.5 * self.skin) ** 2:
            self.baue_liste(x)

    def paar(self, x, phi, eps):
        d = x[self.pi] - x[self.pj]
        d -= self.L * np.round(d / self.L)
        r = np.sqrt((d * d).sum(1))
        if eps > 0:
            s = np.sin(phi)
            dsum = 1.0 + 0.5 * eps * (s[self.pi] + s[self.pj])
        else:
            dsum = 1.0
        h = dsum - r
        return d, r, h

    def f(self, x, phi, g, eps):
        d, r, h = self.paar(x, phi, eps)
        hm = np.where(h > 0, h, 0.0)
        fv = (hm / np.maximum(r, 1e-12))[:, None] * d
        N = self.N
        Fx = np.empty_like(x)
        for k in range(self.dim):
            Fx[:, k] = np.bincount(self.pi, fv[:, k], N) - np.bincount(self.pj, fv[:, k], N)
        if eps > 0:
            hs = np.bincount(self.pi, hm, N) + np.bincount(self.pj, hm, N)
            dphi = OMEGA - g * 0.5 * eps * np.cos(phi) * hs
        else:
            dphi = np.full(N, OMEGA)
        return g * Fx, dphi

    def schritt(self, x, phi, g, eps, dt, sig, rng):
        self.pruefe_liste(x)
        xi = sig * rng.standard_normal(self.N) if sig > 0 else 0.0
        a1, b1 = self.f(x, phi, g, eps)
        xp = x + dt * a1
        pp = phi + dt * b1 + xi
        a2, b2 = self.f(xp, pp, g, eps)
        return x + 0.5 * dt * (a1 + a2), phi + 0.5 * dt * (b1 + b2) + xi


def min_bild(v, L):
    return v - L * np.round(v / L)


def kontaktdreiecke(xbar, L, rc, N):
    tree = cKDTree(np.mod(xbar, L), boxsize=L)
    p = tree.query_pairs(rc, output_type='ndarray')
    nb = [set() for _ in range(N)]
    for i, j in p:
        nb[i].add(j)
        nb[j].add(i)
    tri = []
    for i, j in p:
        a, b = (i, j) if i < j else (j, i)
        for k in nb[a] & nb[b]:
            if k > b:
                tri.append((a, b, k))
    return p, np.array(tri, dtype=int).reshape(-1, 3)


def dreieck_mass(tri, x0, x1, th, L, dim):
    """Drehsinn chi (Reihenfolge ccw in 2D bzw. a,b,c mit Normale in 3D), Windung, Drehung je Takt dpsi"""
    a, b, c = tri[:, 0].copy(), tri[:, 1].copy(), tri[:, 2].copy()
    u = min_bild(x0[b] - x0[a], L)
    v = min_bild(x0[c] - x0[a], L)
    if dim == 2:
        cr = u[:, 0] * v[:, 1] - u[:, 1] * v[:, 0]
        sw = cr < 0
        b[sw], c[sw] = c[sw].copy(), b[sw].copy()
        u = min_bild(x0[b] - x0[a], L)
        v = min_bild(x0[c] - x0[a], L)
    chi = (2.0 / (3.0 * np.sqrt(3.0))) * (np.sin(th[b] - th[a]) + np.sin(th[c] - th[b]) + np.sin(th[a] - th[c]))
    w = np.round((wrap(th[b] - th[a]) + wrap(th[c] - th[b]) + wrap(th[a] - th[c])) / (2 * np.pi)).astype(int)
    if x1 is None:
        return chi, w, None
    P = np.stack([np.zeros_like(u), u, v], 1)                       # (T,3,dim) relativ zu a
    u1 = min_bild(x1[b] - x1[a], L)
    v1 = min_bild(x1[c] - x1[a], L)
    Q = np.stack([np.zeros_like(u1), u1, v1], 1)
    P = P - P.mean(1, keepdims=True)
    Q = Q - Q.mean(1, keepdims=True)
    if dim == 2:
        Pc = P[:, :, 0] + 1j * P[:, :, 1]
        Qc = Q[:, :, 0] + 1j * Q[:, :, 1]
    else:
        n = np.cross(u, v)
        n /= np.linalg.norm(n, axis=1, keepdims=True)
        e1 = u / np.linalg.norm(u, axis=1, keepdims=True)
        e2 = np.cross(n, e1)
        Pc = (P * e1[:, None, :]).sum(2) + 1j * (P * e2[:, None, :]).sum(2)
        Qc = (Q * e1[:, None, :]).sum(2) + 1j * (Q * e2[:, None, :]).sum(2)
    dpsi = np.angle((np.conj(Pc) * Qc).sum(1))
    return chi, w, dpsi


def gebiete(tri, chi, schwelle=0.5):
    """Drehsinn-Gebiete: Dreiecke mit |chi| >= schwelle, verbunden ueber gemeinsame Kanten bei gleichem Vorzeichen"""
    m = np.abs(chi) >= schwelle
    idx = np.where(m)[0]
    eltern = {int(i): int(i) for i in idx}

    def finde(i):
        while eltern[i] != i:
            eltern[i] = eltern[eltern[i]]
            i = eltern[i]
        return i
    kanten = {}
    for t in idx:
        a, b, c = sorted(tri[t])
        for e in ((a, b), (a, c), (b, c)):
            kanten.setdefault(e, []).append(int(t))
    for e, ts in kanten.items():
        for p in range(len(ts)):
            for q in range(p + 1, len(ts)):
                if np.sign(chi[ts[p]]) == np.sign(chi[ts[q]]):
                    ra, rb = finde(ts[p]), finde(ts[q])
                    if ra != rb:
                        eltern[ra] = rb
    groessen = {}
    for t in idx:
        r = finde(int(t))
        groessen[r] = groessen.get(r, 0) + 1
    gr = sorted(groessen.values(), reverse=True)
    return {'n_gebiete': len(gr), 'groesstes': gr[0] if gr else 0, 'mittel': float(np.mean(gr)) if gr else 0.0,
            'n_dreiecke_chi': int(m.sum())}


def teilC(args):
    dim = args.dim
    packung = args.phi
    N = 500 if dim == 2 else 1000
    rauch = args.rauch
    seed = args.seed
    rng = np.random.default_rng(8000 + seed)
    sys_ = Frei(N, dim, packung, rng)
    g_w = g_aus_kappa(KAPPA_W)
    # Entspannung ohne Atmen (eps = 0)
    t0 = time.time()
    x = sys_.x.copy()
    phi_dummy = np.zeros(N)
    t_ent = 50 if not rauch else 10
    dt_w = 0.004
    for k in range(int(round(t_ent / dt_w))):
        x, _ = sys_.schritt(x, phi_dummy, g_w, 0.0, dt_w, 0.0, rng)
    _, _, h = sys_.paar(x, phi_dummy, 0.0)
    out = {'teil': 'C', 'dim': dim, 'phi': packung, 'N': N, 'L': sys_.L, 'seed': seed, 'rauch': rauch,
           'entspannung': {'takte': t_ent, 'sek': time.time() - t0, 'ueberlapp_max': float(max(h.max(), 0.0)),
                           'n_ueberlapp': int((h > 0).sum())}}
    x_start = x.copy()
    lang = (300 if dim == 2 else 200) if not rauch else 30
    bed = [('schwach', KAPPA_W, EPS, lang, dt_w),
           ('stark', KAPPA_S, EPS, (50 if dim == 2 else 15) if not rauch else 10, 0.0004),
           ('kontrolle', KAPPA_W, 0.0, lang, dt_w)]
    if args.nur:
        bed = [b for b in bed if b[0] in args.nur.split(',')]
    for (art, kappa, eps, takte, dt) in bed:
        t1 = time.time()
        g = g_aus_kappa(kappa)
        rngp = np.random.default_rng(9000 + seed)
        phi = rngp.uniform(0, 2 * np.pi, N)
        rngr = np.random.default_rng(9500 + seed)
        sig = np.sqrt(2 * T_ABS * dt)
        x = x_start.copy()
        nst = int(round(1.0 / dt))
        mstep = max(1, nst // 20)
        fenster0 = 50 if takte >= 150 else max(1, takte // 3)
        W = 50 if takte >= 150 else max(1, takte // 3)
        xbar_alt = None
        th_alt = None
        xbar_marke = {}
        summen = np.zeros(6)       # n, sx, sy, sxx, syy, sxy  (x = chi, y = dpsi)
        probe = []
        rngprobe = np.random.default_rng(42)
        kont_cos, kont_n = 0.0, 0
        phi_v = None
        for n in range(takte):
            X = np.zeros_like(x)
            Z = np.zeros(N, complex)
            cnt = 0
            for k in range(nst):
                x, phi = sys_.schritt(x, phi, g, eps, dt, sig, rngr)
                if (k + 1) % mstep == 0:
                    X += x
                    t = n + (k + 1) * dt
                    Z += np.exp(1j * (phi - OMEGA * t))
                    cnt += 1
                    if n >= takte - 50 and eps > 0 and (k + 1) % (5 * mstep) == 0:
                        d, r, h = sys_.paar(x, phi, eps)
                        mk = h > 0
                        if mk.any():
                            kont_cos += float(np.cos(phi[sys_.pi[mk]] - phi[sys_.pj[mk]]).sum())
                            kont_n += int(mk.sum())
            xbar = X / cnt
            th = np.angle(Z)
            if n in (0, 100, 200, takte - 1):
                xbar_marke[n] = xbar.copy()
            if n == takte - W - 1:
                phi_v = phi.copy()
            if xbar_alt is not None and (n - 1) >= fenster0 and eps > 0:
                p, tri = kontaktdreiecke(xbar_alt, sys_.L, 1.0 + EPS, N)
                if len(tri):
                    chi, w, dpsi = dreieck_mass(tri, xbar_alt, xbar, th_alt, sys_.L, dim)
                    summen += [len(chi), chi.sum(), dpsi.sum(), (chi * chi).sum(), (dpsi * dpsi).sum(),
                               (chi * dpsi).sum()]
                    if len(probe) < 4000:
                        sel = rngprobe.choice(len(chi), min(len(chi), 20), replace=False)
                        probe.extend([[round(float(chi[i]), 4), round(float(dpsi[i]), 6)] for i in sel])
            xbar_alt, th_alt = xbar, th
        r = {'kappa': kappa, 'eps': eps, 'takte': takte, 'dt': dt, 'g': g}
        # Verschiebung (Takt-gemittelte, entfaltete Lagen)
        for (a_, b_) in ((0, 100), (100, 200 if takte > 200 else takte - 1), (200, takte - 1), (0, takte - 1)):
            if a_ in xbar_marke and b_ in xbar_marke and b_ > a_:
                r['msd_%d_%d' % (a_, b_)] = float(((xbar_marke[b_] - xbar_marke[a_]) ** 2).sum(1).mean())
        fr, v = gefroren(phi, phi_v, W)
        r['gefroren'] = float(fr.mean())
        r['v_mittel'] = float(v.mean())
        if eps > 0:
            r['kontakt_cos'] = kont_cos / kont_n if kont_n else None
            r['kontakt_n_proben'] = kont_n
            nn = summen[0]
            if nn > 2:
                mx, my = summen[1] / nn, summen[2] / nn
                vx, vy = summen[3] / nn - mx * mx, summen[4] / nn - my * my
                cxy = summen[5] / nn - mx * my
                r['pump_r'] = float(cxy / np.sqrt(vx * vy)) if vx > 0 and vy > 0 else None
                r['pump_steigung'] = float(cxy / vx) if vx > 0 else None
                r['pump_n'] = int(nn)
                r['pump_dpsi_mittel'] = float(my)
                r['pump_chi_mittel'] = float(mx)
            r['pump_probe'] = probe
            # Zaehlung am Ende (letzter Takt, Takt-gemittelte Lagen und Phasen)
            p, tri = kontaktdreiecke(xbar, sys_.L, 1.0 + EPS, N)
            dd = th[p[:, 0]] - th[p[:, 1]]
            cz = np.cos(dd)
            lauf = ~fr
            ml = lauf[p[:, 0]] & lauf[p[:, 1]]
            zr = {'n_kontakte_geo': int(len(p)), 'z_mittel': float(2 * len(p) / N),
                  'cos_mittel_geo': float(cz.mean()) if len(cz) else None,
                  'cos_mittel_geo_laufend': float(cz[ml].mean()) if ml.any() else None,
                  'anteil_gegentakt_09': float((cz < -0.9).mean()) if len(cz) else None,
                  'anteil_gleichtakt_09': float((cz > 0.9).mean()) if len(cz) else None,
                  'anteil_gleichtakt_09_laufend': float((cz[ml] > 0.9).mean()) if ml.any() else None,
                  'n_dreiecke': int(len(tri))}
            if len(tri):
                chi, w, _ = dreieck_mass(tri, xbar, None, th, sys_.L, dim)
                zr['anteil_chi_05'] = float((np.abs(chi) >= 0.5).mean())
                zr['anteil_chi_09'] = float((np.abs(chi) >= 0.9).mean())
                zr['anteil_windung'] = float((w != 0).mean())
                zr['chi_betrag_mittel'] = float(np.abs(chi).mean())
                if dim == 2:
                    zr['gebiete'] = gebiete(tri, chi)
            r['zaehlung'] = zr
            if dim == 2:
                r['bild'] = {'x': [[round(float(a), 3) for a in row] for row in np.mod(xbar, sys_.L)],
                             'th': [round(float(a), 3) for a in th], 'gefroren': [bool(b) for b in fr]}
        r['sek'] = time.time() - t1
        r['n_listen'] = sys_.n_listen
        out[art] = r
        print(art, 'fertig', round(r['sek'], 1), 's', flush=True)
    out['max_rss_mb'] = rss_mb()
    return out


def teilC0(args):
    """Pumpkontrolle: ein Dreieck aus drei Punkten mit Federn (Laenge (d_i + d_j)/2), Phasen vorgegeben"""
    res = []
    for chi in (1, -1, 0):
        for gfak in (1, 4):
            g = g_aus_kappa(KAPPA_W) * gfak
            x = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(3) / 2]])
            dt = 0.002 / gfak
            nst = int(round(1.0 / dt))
            pairs = [(0, 1), (1, 2), (0, 2)]
            snaps = [x.copy()]
            for n in range(40):
                for k in range(nst):
                    def f(xx, tt):
                        d_ = 1.0 + EPS * np.sin(OMEGA * tt + chi * 2 * np.pi * np.arange(3) / 3)
                        F = np.zeros_like(xx)
                        for i, j in pairs:
                            dv = xx[i] - xx[j]
                            r = np.linalg.norm(dv)
                            ell = 0.5 * (d_[i] + d_[j])
                            fij = -(r - ell) * dv / r
                            F[i] += fij
                            F[j] -= fij
                        return g * F
                    t = n + k * dt
                    k1 = f(x, t)
                    k2 = f(x + dt * k1, t + dt)
                    x = x + 0.5 * dt * (k1 + k2)
                snaps.append(x.copy())
            dpsi = []
            for n in range(10, 40):
                P = snaps[n] - snaps[n].mean(0)
                Q = snaps[n + 1] - snaps[n + 1].mean(0)
                Pc = P[:, 0] + 1j * P[:, 1]
                Qc = Q[:, 0] + 1j * Q[:, 1]
                dpsi.append(float(np.angle((np.conj(Pc) * Qc).sum())))
            res.append({'chi': chi, 'g_faktor': gfak, 'dpsi_je_takt': float(np.mean(dpsi)),
                        'dpsi_streuung': float(np.std(dpsi)), 'vorhersage_betrag': float(np.pi / 2 * EPS ** 2)})
    return {'teil': 'C0', 'res': res, 'max_rss_mb': rss_mb()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('teil')
    ap.add_argument('--out', required=True)
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--netze', default='paar,kette,quadrat,dreieck,diamant')
    ap.add_argument('--gitter', default='pyro')
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--seeds', default='1,2')
    ap.add_argument('--T_rel', type=float, default=T_REL)
    ap.add_argument('--takte', type=int, default=10000)
    ap.add_argument('--seedsA', default='')
    ap.add_argument('--jede', type=int, default=100)
    ap.add_argument('--dim', type=int, default=2)
    ap.add_argument('--phi', type=float, default=0.84)
    ap.add_argument('--nur', default='')
    args = ap.parse_args()
    t0 = time.time()
    fn = {'teilA': teilA, 'teilB1': teilB1, 'teilB2': teilB2, 'teilB3': teilB3, 'teilC': teilC,
          'teilC0': teilC0}[args.teil]
    out = fn(args)
    out['argv'] = sys.argv[1:]
    out['sek_gesamt'] = time.time() - t0
    out['konstanten'] = {'OMEGA': OMEGA, 'EPS': EPS, 'DELTA': DELTA, 'KAPPA_W': KAPPA_W, 'KAPPA_S': KAPPA_S,
                         'T_REL': T_REL, 'T_ABS': T_ABS}
    with open(args.out, 'w') as fh:
        json.dump(out, fh)
    print(json.dumps({'teil': args.teil, 'sek': round(out['sek_gesamt'], 1), 'max_rss_mb': round(rss_mb(), 1)}),
          flush=True)


if __name__ == '__main__':
    main()
