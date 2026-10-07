#!/usr/bin/env python3
"""EINFANG-2 (Runde 34, runden-v3, explorativ). Code-Agent fuer die Leitung claude-primary.

Bremsen viele Fuenfer-Ecken einen Q-Ball bis zum Einfang? Q-Ball (M1, beta = 1/2) auf der Oberflaeche eines
Ikosaeders (Kante a, jede Flaeche in nu^2 gleichseitige Dreiecke der Kante h = a/nu; 12 Fuenfer-Spitzen). Kontrolle:
flacher periodischer Dreiecksnetz-Torus gleicher Flaeche und gleichen h.

Zeitentwicklung wie EINFANG-1 (einfang.py), ohne Schwamm (geschlossene Flaeche):
    A_i phi_i'' = -(L phi)_i - A_i U'(|phi_i|^2) phi_i,   U(S) = S - S^2 + S^3/2
  L = Kotangens-Laplace, A = baryzentrische Eckflaechen.
  Energie E = Sum A |phi'|^2 + phi^H L phi + Sum A U(|phi|^2);  Ladung Q = 2 Sum A Im(conj(phi') phi).
  Stoermer-Verlet (Kick-Drift-Kick), float64.
Statischer Ball: kegel_q.loese_ball auf einem ebenen Sechser-Flicken (n = 6, Radius 30, Dirichlet) bei Q_lat = Q/gamma,
uebertragen auf das Zielnetz ueber Gitterkoordinaten um den Startknoten (dasselbe Dreiecksgitter), ausserhalb des
Radius R_trans = min(19, a/2 - 1) null. Boost wie EINFANG-1: phi = f exp(i omega gamma v e.xi),
phi' = [-v e.grad f - i omega gamma f] exp(...), grad f aus dem radialen Kontinuumsprofil.
Ort auf dem Ikosaeder: harmonischer Schwerpunkt je Spitzenkarte k. Karte k = Abwicklung der 5 Sternflaechen und der
5 Flaechen des zweiten Rings um Spitze k, Kegelkoordinaten (r, theta), theta in (-5 pi/6, 5 pi/6], Periode 5 pi/3.
  W_k = Sum rho w_k / Sum rho, w_k = r^s exp(i s theta), s = 6/5, rho = Ladungsdichte auf Ecken mit |phi|^2 > S_thr.
  Gueltig, wenn die ganze gewichtete Ladung in Karte k liegt (Abdeckung 1). Abstand d_k = |W_k|^(1/s),
  Richtung theta_k = arg(W_k)/s; exakt fuer runde Baelle, die die Spitze nicht ueberdecken.
Ort auf dem Torus: ladungsgewichteter Schwerpunkt (gleiche Gewichte) im Mindestbild um den Knoten mit groesstem |phi|^2.
Befehle: lauf, auswertung, bild.
"""
import argparse
import glob
import json
import math
import os
import sys
import time

for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_v, '1')

import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PI = math.pi
SQ3 = math.sqrt(3.0)
S5 = 6.0 / 5.0
THETA5 = 5.0 * PI / 3.0
T_START = time.perf_counter()
R_HALB = 6.2551            # R_half(Q = 200), KEGEL-Q radial (dr = 0,01)
R_EINFANG = R_HALB + 6.0   # Karte: R_halb + 6 = 12,3
R_FREI = 12.0              # freier Flug: alle Spitzen mindestens 12 entfernt (EINFANG-1: Fenster |x| >= 12)
D_NAH = 3.0                # naher Durchgang: Mindestabstand < 3 (Karte)
DELTA_EXT = 2.0            # Hysterese fuer Wenden und Durchgaenge
COV_TOL = 1e-6             # Abdeckung einer Karte: |Sum_Karte rho / Sum rho - 1| <= COV_TOL
SEHNE = 5                  # Sehnen ueber 5 Diagnosepunkte (10 Zeiteinheiten) fuer die Geschwindigkeit
MIN_PUNKTE = 10            # freie Strecke: mindestens 10 Diagnosepunkte
T_MIN = 20.0               # Startstrecke erst ab t = 20 (wie EINFANG-1)


def jetzt():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def sauber(o):
    """Nicht endliche Zahlen -> None (jq-lesbares JSON)."""
    if isinstance(o, dict):
        return {k: sauber(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sauber(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return float(o) if math.isfinite(o) else None
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def schreibe_json(pfad, obj, kompakt=True):
    obj = sauber(obj)
    tmp = pfad + '.tmp'
    with open(tmp, 'w') as fh:
        if kompakt:
            json.dump(obj, fh, separators=(',', ':'))
        else:
            json.dump(obj, fh, indent=1)
    os.replace(tmp, pfad)


def lade(p):
    with open(p) as fh:
        return json.load(fh)


def kegelabstand(r1, t1, r2, t2):
    """Geodaetischer Abstand zweier Punkte (r, theta) auf dem Fuenfer-Kegel (Periode 5 pi/3)."""
    D = np.remainder(np.abs(t1 - t2), THETA5)
    D = np.minimum(D, THETA5 - D)
    return np.where(D < PI, np.sqrt(np.maximum(r1 * r1 + r2 * r2 - 2.0 * r1 * r2 * np.cos(D), 0.0)), r1 + r2)


# --------------------------------------------------------------------------------------------------------------------
# Netze
# --------------------------------------------------------------------------------------------------------------------
def ikosaeder_ecken(a):
    p = (1.0 + math.sqrt(5.0)) / 2.0
    V = []
    for s1 in (-1.0, 1.0):
        for s2 in (-1.0, 1.0):
            V.append((0.0, s1, s2 * p))
            V.append((s1, s2 * p, 0.0))
            V.append((s2 * p, 0.0, s1))
    V = np.array(V) * (a / 2.0)
    n = len(V)
    D = np.linalg.norm(V[:, None, :] - V[None, :, :], axis=2)
    adj = np.abs(D - a) < 1e-9 * a
    F = []
    for i in range(n):
        for j in range(i + 1, n):
            if not adj[i, j]:
                continue
            for k in range(j + 1, n):
                if adj[i, k] and adj[j, k]:
                    f = [i, j, k]
                    if np.dot(np.cross(V[j] - V[i], V[k] - V[i]), V[i] + V[j] + V[k]) < 0:
                        f = [i, k, j]
                    F.append(f)
    F = np.array(F, dtype=np.int64)
    assert len(F) == 20 and int(adj.sum()) == 60
    return V, F, adj


def karte_flaechen(V, F, adj, k):
    """Abwicklung um Spitze k: 5 Sternflaechen (Winkel m*60 bis (m+1)*60 Grad) und 5 Flaechen des zweiten Rings.
    Bezugsrichtung B_0 = kleinster Nachbar von k; B_m gegen den Uhrzeigersinn (von aussen gesehen).
    Rueckgabe: Liste (Flaechenindex, {Ecke: komplexe Lage in der Abwicklung}), Nachbarn in Reihenfolge."""
    a = float(np.linalg.norm(V[F[0][1]] - V[F[0][0]]))
    nb = [int(j) for j in np.where(adj[k])[0]]
    order = [min(nb)]
    while len(order) < 5:
        cur = order[-1]
        cand = [j for j in nb if adj[cur, j] and j not in order]
        ccw = [j for j in cand if np.dot(np.cross(V[cur] - V[k], V[j] - V[k]), V[k]) > 0]
        assert len(ccw) == 1, (k, cur, cand)
        order.append(ccw[0])
    fset = {frozenset(int(x) for x in f): fi for fi, f in enumerate(F)}
    flaechen = []
    for m in range(5):
        Bm, Bn = order[m], order[(m + 1) % 5]
        flaechen.append((fset[frozenset((k, Bm, Bn))],
                         {k: 0j, Bm: a * np.exp(1j * m * PI / 3.0), Bn: a * np.exp(1j * (m + 1) * PI / 3.0)}))
    for m in range(5):
        Bm, Bn = order[m], order[(m + 1) % 5]
        zm, zn = a * np.exp(1j * m * PI / 3.0), a * np.exp(1j * (m + 1) * PI / 3.0)
        X = [j for j in range(len(V)) if adj[Bm, j] and adj[Bn, j] and j != k]
        assert len(X) == 1
        flaechen.append((fset[frozenset((Bm, Bn, X[0]))], {Bm: zm, Bn: zn, X[0]: zm + zn}))
    return flaechen, order


def winkel_kegel(z):
    """Abwicklungswinkel in [0, 5 pi/3] -> symmetrisch (-5 pi/6, 5 pi/6]."""
    th = np.angle(z)
    th = np.where(th < -1e-9, th + 2.0 * PI, th)
    th = np.where(th < 0.0, 0.0, th)
    return np.where(th > THETA5 / 2.0, th - THETA5, th)


def kotangens_netz(N, tris, kanten_vek):
    """Kotangens-Gewichte, Eckflaechen, Winkelsummen. kanten_vek(tris) -> e01, e02, e12 (je M x 3)."""
    e01, e02, e12 = kanten_vek(tris)
    cr = np.cross(e01, e02)
    twoA = np.linalg.norm(cr, axis=1)
    d0 = (e01 * e02).sum(1)
    d1 = (-e01 * e12).sum(1)
    d2 = (e02 * e12).sum(1)
    cot = np.stack([d0, d1, d2], 1) / twoA[:, None]
    ang = np.arctan2(twoA[:, None], np.stack([d0, d1, d2], 1))
    A = np.bincount(tris.ravel(), weights=np.repeat(twoA / 6.0, 3), minlength=N)
    winkel = np.bincount(tris.ravel(), weights=ang.ravel(), minlength=N)
    ei = np.concatenate([tris[:, 1], tris[:, 0], tris[:, 0]])
    ej = np.concatenate([tris[:, 2], tris[:, 2], tris[:, 1]])
    ww = np.concatenate([cot[:, 0], cot[:, 1], cot[:, 2]]) / 2.0
    lo, hi = np.minimum(ei, ej), np.maximum(ei, ej)
    uk, inv, cnt = np.unique(lo * N + hi, return_inverse=True, return_counts=True)
    w = np.bincount(inv, weights=ww)
    ki, kj = (uk // N).astype(np.int64), (uk % N).astype(np.int64)
    L = sp.coo_matrix((np.concatenate([w, w, -w, -w]),
                       (np.concatenate([ki, kj, ki, kj]), np.concatenate([ki, kj, kj, ki]))), shape=(N, N)).tocsr()
    grad = np.bincount(np.concatenate([ki, kj]), minlength=N)
    return dict(A=A, winkel=winkel, w=w, ki=ki, kj=kj, kanten_anz=cnt, L=L, grad=grad, n_dreiecke=len(tris))


class Ikosaeder:
    geo = 'ikosaeder'

    def __init__(self, nu, a):
        assert nu % 2 == 0, 'nu gerade (Kantenmitte = Knoten)'
        self.nu, self.a, self.h = nu, a, a / nu
        V, F, adj = ikosaeder_ecken(a)
        self.V, self.F, self.adj = V, F, adj
        kanten = sorted({(min(int(f[x]), int(f[y])), max(int(f[x]), int(f[y])))
                         for f in F for x, y in ((0, 1), (1, 2), (0, 2))})
        assert len(kanten) == 30
        kid = {e: n for n, e in enumerate(kanten)}
        I, J = [], []
        for i in range(nu + 1):
            for j in range(nu + 1 - i):
                I.append(i)
                J.append(j)
        I, J = np.array(I, dtype=np.int64), np.array(J, dtype=np.int64)
        K = nu - I - J
        self.I_f, self.J_f = I, J
        ninnen = (nu - 1) * (nu - 2) // 2
        base_e, base_f = 12, 12 + 30 * (nu - 1)
        inner = (I >= 1) & (J >= 1) & (K >= 1)
        assert int(inner.sum()) == ninnen
        loc = -np.ones(len(I), dtype=np.int64)
        loc[inner] = np.arange(ninnen)

        def kante(u, v, schritte):
            e = kid[(min(u, v), max(u, v))]
            kk = schritte if u < v else nu - schritte
            return base_e + e * (nu - 1) + (kk - 1)

        gid = np.empty((20, len(I)), dtype=np.int64)
        for fi, (c0, c1, c2) in enumerate(F):
            c0, c1, c2 = int(c0), int(c1), int(c2)
            g = np.full(len(I), -1, dtype=np.int64)
            g[(I == 0) & (J == 0)] = c0
            g[I == nu] = c1
            g[J == nu] = c2
            m = (J == 0) & (I > 0) & (I < nu)
            g[m] = kante(c0, c1, I[m])
            m = (I == 0) & (J > 0) & (J < nu)
            g[m] = kante(c0, c2, J[m])
            m = (K == 0) & (I > 0) & (I < nu)
            g[m] = kante(c1, c2, J[m])
            g[inner] = base_f + fi * ninnen + loc[inner]
            assert (g >= 0).all()
            gid[fi] = g
        N = 10 * nu * nu + 2
        assert np.array_equal(np.unique(gid), np.arange(N))
        self.gid, self.N = gid, N
        pos = np.zeros((N, 3))
        for fi, (c0, c1, c2) in enumerate(F):
            pos[gid[fi]] = V[c0][None] + (I / nu)[:, None] * (V[c1] - V[c0])[None] + (J / nu)[:, None] * (V[c2] - V[c0])[None]
        pos[:12] = V
        self.pos = pos

        def lidx(i, j):
            return i * (nu + 1) - (i * (i - 1)) // 2 + j
        tl = []
        for i in range(nu):
            for j in range(nu - i):
                tl.append((lidx(i, j), lidx(i + 1, j), lidx(i, j + 1)))
                if i + j <= nu - 2:
                    tl.append((lidx(i + 1, j), lidx(i + 1, j + 1), lidx(i, j + 1)))
        tl = np.array(tl, dtype=np.int64)
        tris = np.concatenate([gid[fi][tl] for fi in range(20)])

        def kv(t):
            p0, p1, p2 = pos[t[:, 0]], pos[t[:, 1]], pos[t[:, 2]]
            return p1 - p0, p2 - p0, p2 - p1
        self.k = kotangens_netz(N, tris, kv)
        self.A = self.k['A']
        self.L = self.k['L']
        self.flaeche_soll = 5.0 * SQ3 * a * a

    def pruefung(self):
        k = self.k
        g = k['grad']
        defekt = 2.0 * PI - k['winkel']
        spitzen = np.where(np.abs(defekt) > 1e-9)[0]
        V, E, F = self.N, len(k['w']), k['n_dreiecke']
        return dict(geo='ikosaeder', nu=self.nu, a=self.a, h=self.h, ecken=V, ecken_soll=10 * self.nu ** 2 + 2,
                    kanten=E, dreiecke=F, euler=V - E + F,
                    grade={int(a): int(b) for a, b in zip(*np.unique(g, return_counts=True))},
                    grad5_knoten=[int(i) for i in np.where(g == 5)[0]],
                    ecken_mit_defekt=[int(i) for i in spitzen[:20]], anzahl_defekte=int(len(spitzen)),
                    defekt_spitzen=[float(defekt[i]) for i in range(12)], defekt_soll=PI / 3.0,
                    defekt_rest_max=float(np.max(np.abs(defekt[12:]))),
                    kanten_alle_doppelt=bool(np.all(k['kanten_anz'] == 2)),
                    w_min=float(k['w'].min()), w_max=float(k['w'].max()), w_soll=1.0 / SQ3,
                    A_regulaer=float(np.median(self.A)), A_regulaer_soll=SQ3 / 2.0 * self.h ** 2,
                    A_spitze=float(self.A[0]), A_spitze_soll=5.0 / 6.0 * SQ3 / 2.0 * self.h ** 2,
                    flaeche=float(self.A.sum()), flaeche_soll=self.flaeche_soll)

    def karten(self):
        """Je Spitze k: globale Knoten, r, theta (symmetrisch), w = r^s exp(i s theta)."""
        out = []
        for kk in range(12):
            fl, order = karte_flaechen(self.V, self.F, self.adj, kk)
            gs, zs = [], []
            for fi, dz in fl:
                c0, c1, c2 = (int(x) for x in self.F[fi])
                d0, d1, d2 = dz[c0], dz[c1], dz[c2]
                zs.append(d0 + (self.I_f / self.nu) * (d1 - d0) + (self.J_f / self.nu) * (d2 - d0))
                gs.append(self.gid[fi])
            g = np.concatenate(gs)
            z = np.concatenate(zs)
            ug, first = np.unique(g, return_index=True)
            z = z[first]
            r = np.abs(z)
            th = winkel_kegel(z)
            w = r ** S5 * np.exp(1j * S5 * th)
            out.append(dict(idx=ug, r=r, th=th, w=w, order=order))
        return out


class Torus:
    geo = 'torus'

    def __init__(self, N1, N2, h):
        assert N2 % 2 == 0
        self.N1, self.N2, self.h = N1, N2, h
        self.Wx, self.Wy = N1 * h, N2 * h * SQ3 / 2.0
        i, j = np.meshgrid(np.arange(N1), np.arange(N2), indexing='ij')
        i, j = i.ravel(), j.ravel()
        N = N1 * N2
        self.N = N

        def g(a, b):
            return (a % N1) * N2 + (b % N2)
        self.x = h * (i + 0.5 * (j % 2))
        self.y = h * SQ3 / 2.0 * j
        ev = (j % 2) == 0
        T1 = np.where(ev[:, None], np.stack([g(i, j), g(i + 1, j), g(i, j + 1)], 1),
                      np.stack([g(i, j), g(i + 1, j), g(i + 1, j + 1)], 1))
        T2 = np.where(ev[:, None], np.stack([g(i, j), g(i, j + 1), g(i - 1, j + 1)], 1),
                      np.stack([g(i, j), g(i + 1, j + 1), g(i, j + 1)], 1))
        tris = np.concatenate([T1, T2])
        x, y = self.x, self.y

        def mi(dx, dy):
            return dx - self.Wx * np.round(dx / self.Wx), dy - self.Wy * np.round(dy / self.Wy)

        def kv(t):
            out = []
            for a_, b_ in ((0, 1), (0, 2), (1, 2)):
                dx, dy = mi(x[t[:, b_]] - x[t[:, a_]], y[t[:, b_]] - y[t[:, a_]])
                out.append(np.stack([dx, dy, np.zeros_like(dx)], 1))
            return out
        self.k = kotangens_netz(N, tris, kv)
        self.A = self.k['A']
        self.L = self.k['L']
        self.mi = mi

    def pruefung(self):
        k = self.k
        V, E, F = self.N, len(k['w']), k['n_dreiecke']
        defekt = 2.0 * PI - k['winkel']
        return dict(geo='torus', N1=self.N1, N2=self.N2, h=self.h, Wx=self.Wx, Wy=self.Wy, ecken=V, kanten=E,
                    dreiecke=F, euler=V - E + F,
                    grade={int(a): int(b) for a, b in zip(*np.unique(k['grad'], return_counts=True))},
                    defekt_max=float(np.max(np.abs(defekt))), kanten_alle_doppelt=bool(np.all(k['kanten_anz'] == 2)),
                    w_min=float(k['w'].min()), w_max=float(k['w'].max()), w_soll=1.0 / SQ3,
                    flaeche=float(self.A.sum()))


# --------------------------------------------------------------------------------------------------------------------
# Startzustand
# --------------------------------------------------------------------------------------------------------------------
def gitter_mn(dx, dy, h):
    n = dy / (h * SQ3 / 2.0)
    m = dx / h - n / 2.0
    mr, nr = np.round(m), np.round(n)
    fehler = float(max(np.max(np.abs(m - mr), initial=0.0), np.max(np.abs(n - nr), initial=0.0)))
    return mr.astype(np.int64), nr.astype(np.int64), fehler


def startzustand(geo, args):
    """Statischer Ball (Flicken n = 6) mit Q_lat = Q/gamma, uebertragen, geboostet."""
    from kegel_q import Netz, baue_familie, loese_Q, loese_ball
    v = args.v
    gam = 1.0 / math.sqrt(1.0 - v * v)
    h = geo.h
    rad, fam = baue_familie(0.01, 60.0)
    g200, _ = loese_Q(rad, fam, args.Q)
    Q_lat = args.Q / gam
    gQ, fQ = loese_Q(rad, fam, Q_lat)
    patch = Netz(6, h, args.R_flicken)
    patch.setze_richtung(0.0)
    f0 = np.interp(patch.r, rad.r, fQ, right=0.0)
    f0[patch.rand] = 0.0
    tb = time.perf_counter()
    rb, fp = loese_ball(patch, Q_lat, 0.0, 0.0, f0, 5.0, 1e-9, 12, 40000, 1e-10)
    tb = time.perf_counter() - tb
    om = rb['omega']
    mp, np_, fehl_p = gitter_mn(patch.X, patch.Y, h)
    tab = {(int(a), int(b)): i for i, (a, b) in enumerate(zip(mp, np_))}
    info = dict(Q_lat=Q_lat, E_lat=rb['E'], omega_lat=om, c1=rb['c1'], c2=rb['c2'], res_max=rb['res_max'],
                aussen=rb['aussen'], dauer_s=tb, f_max=float(fp.max()), flicken_ecken=int(patch.N),
                flicken_R=args.R_flicken, gitterfehler_flicken=fehl_p,
                radial_Q=dict(omega=g200['omega'], R_half=g200['R_half'], kappa=g200['kappa'], E=g200['E']))
    if geo.geo == 'ikosaeder':
        R_trans = min(19.0, geo.a / 2.0 - 1.0)
        kart = geo.karten()[0]       # Spitze 0; Bezugsrichtung B_0 = kleinster Nachbar, Startkante (0, B_0)
        B0 = kart['order'][0]
        d_m = geo.a / 2.0
        dist = kegelabstand(kart['r'], kart['th'], d_m, 0.0)
        sel = dist < R_trans
        knoten = kart['idx'][sel]
        dx = kart['r'][sel] * np.cos(kart['th'][sel]) - d_m
        dy = kart['r'][sel] * np.sin(kart['th'][sel])
        alpha = math.asin(args.b / d_m) if args.b else 0.0
        e = np.array([-math.cos(alpha), math.sin(alpha)])   # Richtung zur Spitze 0, um alpha gedreht
        info.update(start_spitze=0, start_kante=[0, int(B0)], R_trans=R_trans, b=args.b, alpha_grad=math.degrees(alpha))
    else:
        R_trans = 19.0
        i0 = (geo.N1 // 2) * geo.N2 + geo.N2 // 2
        dx, dy = geo.mi(geo.x - geo.x[i0], geo.y - geo.y[i0])
        sel = np.hypot(dx, dy) < R_trans
        knoten = np.where(sel)[0]
        dx, dy = dx[sel], dy[sel]
        e = np.array([1.0, 0.0])
        info.update(start_knoten=int(i0), start_xy=[float(geo.x[i0]), float(geo.y[i0])], R_trans=R_trans)
    mt, nt, fehl_t = gitter_mn(dx, dy, h)
    fehlend = [(int(a), int(b)) for a, b in zip(mt, nt) if (int(a), int(b)) not in tab]
    assert not fehlend, 'Gitterpunkte fehlen im Flicken: %d' % len(fehlend)
    f = np.array([fp[tab[(int(a), int(b))]] for a, b in zip(mt, nt)])
    info['gitterfehler_ziel'] = fehl_t
    rho = np.hypot(dx, dy)
    dfr = np.gradient(fQ, rad.r)
    dfd = np.interp(rho, rad.r, dfr, right=0.0)
    edf = np.where(rho > 1e-12, dfd * (e[0] * dx + e[1] * dy) / np.maximum(rho, 1e-12), 0.0)
    phase = np.exp(1j * om * gam * v * (e[0] * dx + e[1] * dy))
    phi_c = f * phase
    p_c = (-v * edf - 1j * om * gam * f) * phase
    phi = np.zeros((geo.N, 2))
    p = np.zeros((geo.N, 2))
    phi[knoten, 0], phi[knoten, 1] = phi_c.real, phi_c.imag
    p[knoten, 0], p[knoten, 1] = p_c.real, p_c.imag
    E_rest = rb['E'] + om * (args.Q - Q_lat)
    info.update(gamma=gam, E_rest=E_rest, K_nominal=(gam - 1.0) * E_rest, richtung=list(e),
                knoten_mit_feld=int(len(knoten)))
    return phi, p, info


# --------------------------------------------------------------------------------------------------------------------
# Lauf
# --------------------------------------------------------------------------------------------------------------------
def befehl_lauf(args):
    import torch
    if args.geraet == 'cuda':
        if not torch.cuda.is_available():
            raise RuntimeError('CUDA verlangt, aber nicht verfuegbar (kein CPU-Ausweichen)')
        dev = torch.device('cuda')
        geraet_name = torch.cuda.get_device_name(0)
    else:
        torch.set_num_threads(1)
        dev = torch.device('cpu')
        geraet_name = 'cpu'
    print('torch %s, Geraet %s (%s)' % (torch.__version__, dev, geraet_name), flush=True)
    if args.geo == 'ikosaeder':
        geo = Ikosaeder(args.nu, args.a)
    else:
        geo = Torus(args.N1, args.N2, args.h)
    pr = geo.pruefung()
    print('Netz %s: %s (Bauzeit bis jetzt %.1f s)' % (args.geo, json.dumps(pr if args.geo == 'torus' else {
        k_: pr[k_] for k_ in ('nu', 'a', 'h', 'ecken', 'ecken_soll', 'euler', 'grade', 'anzahl_defekte',
                              'defekt_rest_max', 'w_min', 'w_max', 'flaeche', 'flaeche_soll')}),
        time.perf_counter() - T_START), flush=True)
    dt = args.dt
    if args.fortsetzen:
        z = np.load(args.fortsetzen)
        meta = json.loads(str(z['meta']))
        rec = json.loads(str(z['rec']))
        phi_np, p_np = z['phi'], z['p']
        t_now = float(z['t'])
        meta['fortsetzungen'] = meta.get('fortsetzungen', []) + [dict(datei=args.fortsetzen, t=t_now, start=jetzt(),
                                                                      T_neu=args.T)]
        meta['T'] = args.T
        meta['name'] = args.name
        print('fortgesetzt bei t = %.3f aus %s' % (t_now, args.fortsetzen), flush=True)
    else:
        phi_np, p_np, info = startzustand(geo, args)
        print('statischer Ball und Start: %s' % json.dumps({k_: info[k_] for k_ in (
            'Q_lat', 'E_lat', 'omega_lat', 'res_max', 'dauer_s', 'gitterfehler_flicken', 'gitterfehler_ziel',
            'R_trans', 'knoten_mit_feld', 'E_rest', 'K_nominal')}), flush=True)
        t_now = 0.0
        meta = dict(befehl='lauf', name=args.name, start=jetzt(), geo=args.geo, Q=args.Q, v=args.v, b=args.b,
                    dt=dt, T=args.T, diag=args.diag, S_thr=args.S_thr, R_ball=args.R_ball, geraet=geraet_name,
                    netz=pr, ball=info, E_rest=info['E_rest'], K_nominal=info['K_nominal'],
                    R_einfang=R_EINFANG, R_frei=R_FREI, D_nah=D_NAH)
        if args.geo == 'ikosaeder':
            meta.update(nu=args.nu, a=args.a, h=geo.h)
            rec = {k_: [] for k_ in ('t', 'Wre', 'Wim', 'cov', 'k', 'd', 'th', 'E_tot', 'Q_tot', 'Q_thr', 'E_ball',
                                     'Q_ball', 'S_max', 'S_spitze', 'i_max')}
        else:
            meta.update(N1=args.N1, N2=args.N2, h=args.h)
            rec = {k_: [] for k_ in ('t', 'cx', 'cy', 'E_tot', 'Q_tot', 'Q_thr', 'E_ball', 'Q_ball', 'S_max', 'i_max')}

    f64 = torch.float64
    A = torch.tensor(geo.A, dtype=f64, device=dev)
    invA = 1.0 / A
    Lc = geo.L.tocsr()
    Lt = torch.sparse_csr_tensor(torch.tensor(Lc.indptr, dtype=torch.int64), torch.tensor(Lc.indices, dtype=torch.int64),
                                 torch.tensor(Lc.data, dtype=f64), size=Lc.shape).to(dev)
    phi = torch.tensor(phi_np, dtype=f64, device=dev)
    p = torch.tensor(p_np, dtype=f64, device=dev)

    if args.geo == 'ikosaeder':
        kart = geo.karten()
        K_idx = [torch.tensor(c['idx'], dtype=torch.int64, device=dev) for c in kart]
        K_r = [torch.tensor(c['r'], dtype=f64, device=dev) for c in kart]
        K_th = [torch.tensor(c['th'], dtype=f64, device=dev) for c in kart]
        g_all = torch.cat(K_idx)
        seg = np.concatenate([np.full(len(c['idx']), kk, dtype=np.int64) for kk, c in enumerate(kart)])
        bins = torch.tensor(np.concatenate([seg, seg + 12, seg + 24]), dtype=torch.int64, device=dev)
        wcat = torch.tensor(np.concatenate([np.concatenate([c['w'].real for c in kart]),
                                            np.concatenate([c['w'].imag for c in kart]),
                                            np.ones(len(seg))]), dtype=f64, device=dev)
        meta['karten_knoten'] = [int(len(c['idx'])) for c in kart]
        print('Karten: %s Knoten je Spitze (%.1f s)' % (meta['karten_knoten'], time.perf_counter() - T_START), flush=True)
    else:
        X = torch.tensor(geo.x, dtype=f64, device=dev)
        Y = torch.tensor(geo.y, dtype=f64, device=dev)

    def kraft(ph):
        S = (ph * ph).sum(1)
        dU = 1.0 - 2.0 * S + 1.5 * S * S
        return -(Lt @ ph) * invA[:, None] - dU[:, None] * ph

    def dichten(ph, pp):
        S = (ph * ph).sum(1)
        q = 2.0 * A * (pp[:, 0] * ph[:, 1] - pp[:, 1] * ph[:, 0])
        e = A * (pp * pp).sum(1) + (ph * (Lt @ ph)).sum(1) + A * (S - S * S + 0.5 * S ** 3)
        return S, q, e

    def diagnose_ik(ph, pp, t):
        S, q, e = dichten(ph, pp)
        rho = torch.where(S > args.S_thr, q, torch.zeros_like(q))
        sums = torch.zeros(36, dtype=f64, device=dev).index_add_(0, bins, rho[g_all].repeat(3) * wcat)
        imax = torch.argmax(S)
        v1 = torch.cat([sums, torch.stack([e.sum(), q.sum(), rho.sum(), S.max(), imax.to(f64)]), S[:12]]).cpu().numpy()
        nre, nim, den = v1[0:12], v1[12:24], v1[24:36]
        Et, Qt, Qthr, Smax, im = (float(x) for x in v1[36:41])
        S12 = v1[41:53]
        cov = den / Qthr if Qthr != 0 else np.zeros(12)
        ok = np.abs(cov - 1.0) <= COV_TOL
        W = np.where(ok, (nre + 1j * nim) / np.where(den != 0, den, 1.0), np.nan)
        d = np.where(ok, np.abs(W) ** (1.0 / S5), np.inf)
        kk = int(np.argmin(d))
        dk = float(d[kk])
        thk = float(np.angle(W[kk]) / S5) if ok[kk] else float('nan')
        if math.isfinite(dk):
            D = torch.remainder((K_th[kk] - thk).abs(), THETA5)
            D = torch.minimum(D, THETA5 - D)
            rr = K_r[kk]
            dist = torch.where(D < PI, torch.sqrt(torch.clamp(rr * rr + dk * dk - 2.0 * rr * dk * torch.cos(D), min=0.0)),
                               rr + dk)
            mb = dist < args.R_ball
            ii = K_idx[kk][mb]
            bv = torch.stack([e[ii].sum(), q[ii].sum()]).cpu().numpy()
            Eb, Qb = float(bv[0]), float(bv[1])
        else:
            Eb = Qb = 0.0
        for k_, val in (('t', t), ('Wre', [float(x) for x in np.nan_to_num(nre / np.where(den != 0, den, 1.0))]),
                        ('Wim', [float(x) for x in np.nan_to_num(nim / np.where(den != 0, den, 1.0))]),
                        ('cov', [float(x) for x in cov]), ('k', kk), ('d', dk if math.isfinite(dk) else -1.0),
                        ('th', thk if math.isfinite(thk) else 0.0), ('E_tot', Et), ('Q_tot', Qt), ('Q_thr', Qthr),
                        ('E_ball', Eb), ('Q_ball', Qb), ('S_max', Smax), ('S_spitze', float(S12[kk])),
                        ('i_max', int(im))):
            rec[k_].append(val)
        return dk, Et

    def diagnose_torus(ph, pp, t):
        S, q, e = dichten(ph, pp)
        rho = torch.where(S > args.S_thr, q, torch.zeros_like(q))
        imax = torch.argmax(S)
        dx = X - X[imax]
        dy = Y - Y[imax]
        dx = dx - geo.Wx * torch.round(dx / geo.Wx)
        dy = dy - geo.Wy * torch.round(dy / geo.Wy)
        sr = rho.sum()
        cxr = X[imax] + (rho * dx).sum() / sr
        cyr = Y[imax] + (rho * dy).sum() / sr
        ddx = X - cxr
        ddy = Y - cyr
        ddx = ddx - geo.Wx * torch.round(ddx / geo.Wx)
        ddy = ddy - geo.Wy * torch.round(ddy / geo.Wy)
        mb = torch.sqrt(ddx * ddx + ddy * ddy) < args.R_ball
        v1 = torch.stack([e.sum(), q.sum(), sr, S.max(), imax.to(f64), cxr, cyr, e[mb].sum(), q[mb].sum()]).cpu().numpy()
        Et, Qt, Qthr, Smax, im, cx, cy, Eb, Qb = (float(x) for x in v1)
        if rec['cx']:
            cx += geo.Wx * round((rec['cx'][-1] - cx) / geo.Wx)
            cy += geo.Wy * round((rec['cy'][-1] - cy) / geo.Wy)
        for k_, val in (('t', t), ('cx', cx), ('cy', cy), ('E_tot', Et), ('Q_tot', Qt), ('Q_thr', Qthr),
                        ('E_ball', Eb), ('Q_ball', Qb), ('S_max', Smax), ('i_max', int(im))):
            rec[k_].append(val)
        return cx, Et

    diagnose = diagnose_ik if args.geo == 'ikosaeder' else diagnose_torus
    nd = int(round(args.diag / dt))
    step0 = int(round(t_now / dt))
    n_steps = int(round(args.T / dt)) - step0
    if not args.fortsetzen:
        x0, _ = diagnose(phi, p, 0.0)
        meta['E0'] = rec['E_tot'][0]
        meta['Q0'] = rec['Q_tot'][0]
        meta['K_eff'] = rec['E_tot'][0] - meta['E_rest']
        print('Start: E %.8f Q %.8f E_rest %.8f K_eff %.6f K_nominal %.6f Lage %.4f Q_ball %.6f' % (
            meta['E0'], meta['Q0'], meta['E_rest'], meta['K_eff'], meta['K_nominal'], x0, rec['Q_ball'][0]), flush=True)
    F = kraft(phi)
    tl = time.perf_counter()
    grund = 'T erreicht'
    fertig = True
    k = 0
    for k in range(1, n_steps + 1):
        p.add_(F, alpha=0.5 * dt)
        phi.add_(p, alpha=dt)
        F = kraft(phi)
        p.add_(F, alpha=0.5 * dt)
        if (step0 + k) % nd == 0:
            t = (step0 + k) * dt
            x, Et = diagnose(phi, p, t)
            if not math.isfinite(Et):
                grund = 'nicht endlich'
                break
            if (step0 + k) % (nd * 100) == 0:
                el = time.perf_counter() - tl
                if args.geo == 'ikosaeder':
                    print('t %.1f Spitze %d d %.4f th %.4f E %.8f Q %.8f E_ball %.6f Q_ball %.6f S_max %.4f '
                          '(%.2f ms/Schritt)' % (t, rec['k'][-1], rec['d'][-1], rec['th'][-1], Et, rec['Q_tot'][-1],
                                                 rec['E_ball'][-1], rec['Q_ball'][-1], rec['S_max'][-1], 1e3 * el / k),
                          flush=True)
                else:
                    print('t %.1f cx %.4f cy %.4f E %.8f Q %.8f E_ball %.6f Q_ball %.6f S_max %.4f (%.2f ms/Schritt)' % (
                        t, rec['cx'][-1], rec['cy'][-1], Et, rec['Q_tot'][-1], rec['E_ball'][-1], rec['Q_ball'][-1],
                        rec['S_max'][-1], 1e3 * el / k), flush=True)
            if time.perf_counter() - T_START > args.wand and k < n_steps:
                grund = 'Wandzeit'
                fertig = False
                break
    el = time.perf_counter() - tl
    meta['ms_je_schritt_letzter_abschnitt'] = 1e3 * el / max(k, 1)
    meta.setdefault('abschnitte', []).append(dict(t_von=step0 * dt, t_bis=rec['t'][-1], schritte=k,
                                                  ms_je_schritt=1e3 * el / max(k, 1), ende=jetzt(),
                                                  dauer_s=time.perf_counter() - T_START, grund=grund))
    meta['grund_ende'] = grund
    meta['vollstaendig'] = fertig
    meta['ende'] = jetzt()
    zpfad = args.zustand
    tmp = zpfad + '.tmp.npz'
    np.savez(tmp, phi=phi.cpu().numpy(), p=p.cpu().numpy(), t=rec['t'][-1], meta=json.dumps(meta), rec=json.dumps(rec))
    os.replace(tmp, zpfad)
    meta['zustand'] = zpfad
    schreibe_json(args.aus, dict(meta=meta, rec=rec))
    print('Ende: %s, t %.1f, %.2f ms/Schritt, Dauer %.1f s, Zustand %s, geschrieben %s' % (
        grund, rec['t'][-1], meta['ms_je_schritt_letzter_abschnitt'], time.perf_counter() - T_START, zpfad, args.aus),
        flush=True)


# --------------------------------------------------------------------------------------------------------------------
# Auswertung (Regeln nach PLAN.md)
# --------------------------------------------------------------------------------------------------------------------
def laeufe_bool(mask):
    runs, i, n = [], 0, len(mask)
    while i < n:
        if mask[i]:
            j = i
            while j + 1 < n and mask[j + 1]:
                j += 1
            runs.append((i, j))
            i = j + 1
        else:
            i += 1
    return runs


def extrema(y, delta):
    """Extrema mit Hysterese delta: 'max' (Wende) bzw. 'min', jeweils erst bestaetigt, wenn y danach um delta
    zurueckgeht. Anfangsrichtung zaehlt nicht."""
    ev, mode, imax, imin = [], 0, 0, 0
    for i in range(len(y)):
        if y[i] > y[imax]:
            imax = i
        if y[i] < y[imin]:
            imin = i
        if mode >= 0 and y[imax] - y[i] >= delta:
            if mode == 1:
                ev.append((imax, 'max'))
            mode, imin = -1, i
        elif mode <= 0 and y[i] - y[imin] >= delta:
            if mode == -1:
                ev.append((imin, 'min'))
            mode, imax = 1, i
    return ev


def steigung(t, y):
    if len(t) < 3:
        return None
    return float(np.polyfit(t, y, 1)[0])


def reihen_ik(L):
    r = L['rec']
    t = np.array(r['t'])
    W = np.array(r['Wre']) + 1j * np.array(r['Wim'])
    cov = np.array(r['cov'])
    ok = np.abs(cov - 1.0) <= COV_TOL
    with np.errstate(divide='ignore', invalid='ignore'):
        d = np.where(ok, np.abs(W) ** (1.0 / S5), np.inf)
    th = np.angle(W) / S5
    k = np.argmin(d, 1)
    dn = d[np.arange(len(t)), k]
    return t, d, th, k, dn, ok


def K_von(v, Q, m):
    return (1.0 / math.sqrt(1.0 - v * v) - 1.0) * (m['E_rest'] + m['ball']['omega_lat'] * (Q - m['Q']))


def strecke_ik(i0, i1, t, d, th, k, ok, rec, m):
    ii = [i for i in range(i0, i1 + 1) if t[i] >= T_MIN]
    if len(ii) < MIN_PUNKTE:
        return None
    sel = ii[::SEHNE]
    if sel[-1] != ii[-1]:
        sel.append(ii[-1])
    s = [0.0]
    for a_, b_ in zip(sel[:-1], sel[1:]):
        c = k[a_]
        if not ok[b_, c]:
            c = k[b_]
            if not ok[a_, c]:
                return None
        s.append(s[-1] + float(kegelabstand(d[a_, c], th[a_, c], d[b_, c], th[b_, c])))
    v = steigung(t[sel], np.array(s))
    Qb = np.array(rec['Q_ball'])[ii]
    Eb = np.array(rec['E_ball'])[ii]
    Sm = np.array(rec['S_max'])[ii]
    out = dict(t_von=float(t[ii[0]]), t_bis=float(t[ii[-1]]), punkte=len(ii), sehnen=len(sel) - 1, v=v,
               Q_ball=float(Qb.mean()), E_ball=float(Eb.mean()),
               atmung_rel=float((Sm.max() - Sm.min()) / 2.0 / Sm.mean()), S_max_mittel=float(Sm.mean()))
    if v is not None and 0 <= v < 1:
        out['K'] = K_von(v, out['Q_ball'], m)
        out['E_innen'] = out['E_ball'] - (m['E_rest'] + m['ball']['omega_lat'] * (out['Q_ball'] - m['Q'])) - out['K']
    return out


def analyse_ik(L):
    m, rec = L['meta'], L['rec']
    t, d, th, k, dn, ok = reihen_ik(L)
    n = len(t)
    a = dict(name=m['name'], geo='ikosaeder', v0=m['v'], b=m.get('b', 0.0), nu=m['nu'], h=m['h'], dt=m['dt'],
             T_ende=float(t[-1]), vollstaendig=m.get('vollstaendig'), K_nominal=m['K_nominal'], K_eff=m['K_eff'],
             E_rest=m['E_rest'], punkte=n)
    Et, Qt = np.array(rec['E_tot']), np.array(rec['Q_tot'])
    a['E_tot_abw_max'] = float(np.max(np.abs(Et - Et[0])))
    a['Q_tot_abw_max'] = float(np.max(np.abs(Qt - Qt[0])))
    a['ohne_karte'] = int(np.sum(~np.isfinite(dn)))
    frei = np.isfinite(dn) & (dn >= R_FREI)
    seg_frei = laeufe_bool(frei)
    seg_beg = laeufe_bool(np.isfinite(dn) & (dn < R_FREI))
    strecken = []
    for (i0, i1) in seg_frei:
        s = strecke_ik(i0, i1, t, d, th, k, ok, rec, m)
        strecken.append(dict(i0=i0, i1=i1, t_von=float(t[i0]), t_bis=float(t[i1]), werte=s))
    beg = []
    for (i0, i1) in seg_beg:
        ap = int(k[i0])
        wechsel = bool(np.any(k[i0:i1 + 1] != ap))
        dA = d[i0:i1 + 1, ap]
        j = int(np.argmin(dA))
        ev = extrema(dA, DELTA_EXT)
        mins_nah = [e_ for e_ in ev if e_[1] == 'min' and dA[e_[0]] < D_NAH]
        wenden = [e_ for e_ in ev if e_[1] == 'max']
        vor = [s for s in strecken if s['i1'] == i0 - 1]
        nach = [s for s in strecken if s['i0'] == i1 + 1]
        sv = vor[0]['werte'] if vor else None
        sn = nach[0]['werte'] if nach else None
        b_ = dict(spitze=ap, t_ein=float(t[i0]), t_aus=float(t[i1]), offen_am_ende=bool(i1 == n - 1),
                  spitzenwechsel=wechsel, d_min=float(dA[j]), t_min=float(t[j + i0]),
                  durchgaenge=max(len(mins_nah), 1 if dA[j] < D_NAH else 0),
                  t_minima_nah=[float(t[i0 + e_[0]]) for e_ in mins_nah],
                  wenden=len(wenden), d_wenden=[float(dA[e_[0]]) for e_ in wenden],
                  v_vor=sv['v'] if sv else None, K_vor=sv.get('K') if sv else None,
                  v_nach=sn['v'] if sn else None, K_nach=sn.get('K') if sn else None)
        b_['nah'] = bool(b_['d_min'] < D_NAH)
        if b_['K_vor'] and b_['K_nach'] is not None:
            b_['K_verhaeltnis'] = b_['K_nach'] / b_['K_vor']
            b_['K_abfall_rel'] = 1.0 - b_['K_verhaeltnis']
        beg.append(b_)
    a['strecken'] = [{**dict(seg_von=s['t_von'], seg_bis=s['t_bis'], v=None), **(s['werte'] or {})} for s in strecken]
    a['begegnungen'] = beg
    a['nahe_durchgaenge'] = [b_ for b_ in beg if b_['nah']]
    # Einfang am Ende
    A_end = int(k[-1])
    ein = dict(eingefangen=False, spitze_ende=A_end, d_ende=float(dn[-1]))
    if np.isfinite(dn[-1]) and d[-1, A_end] <= R_EINFANG:
        i = n - 1
        while i - 1 >= 0 and ok[i - 1, A_end] and d[i - 1, A_end] <= R_EINFANG:
            i -= 1
        ev = extrema(d[i:, A_end], DELTA_EXT)
        w = [e_ for e_ in ev if e_[1] == 'max']
        ein.update(t_c=float(t[i]), wenden=len(w), d_wenden=[float(d[i + e_[0], A_end]) for e_ in w],
                   eingefangen=bool(len(w) >= 2))
    a['einfang'] = ein
    # Lage in 3D und Spiegelebene (Startkante)
    V, F, adj = ikosaeder_ecken(m['a'])
    fl = [karte_flaechen(V, F, adj, kk)[0] for kk in range(12)]
    P = np.array([lage3d(V, fl[int(k[i])], d[i, int(k[i])], th[i, int(k[i])]) if np.isfinite(dn[i]) else
                  [np.nan] * 3 for i in range(n)])
    B0 = karte_flaechen(V, F, adj, 0)[1][0]
    nrm = np.cross(V[0], V[B0])
    nrm /= np.linalg.norm(nrm)
    auf = np.abs(V @ nrm) < 1e-9 * m['a']
    mask_auf = np.array([bool(np.isfinite(dn[i]) and auf[int(k[i])]) for i in range(n)])
    a['spitzen_auf_spiegelebene'] = [int(i) for i in np.where(auf)[0]]
    a['spiegel_abstand_max'] = float(np.nanmax(np.abs(P[mask_auf] @ nrm))) if mask_auf.any() else None
    a['spiegel_abstand_max_alle_karten'] = float(np.nanmax(np.abs(P @ nrm)))
    a['_P'] = P
    a['_reihen'] = (t, d, th, k, dn, ok)
    return a


def lage3d(V, flaechen, dd, tt):
    if not np.isfinite(dd):
        return [np.nan] * 3
    t2 = tt if tt >= 0 else tt + THETA5
    z = dd * np.exp(1j * t2)
    best = None
    for fi, dz in flaechen:
        ks = list(dz.keys())
        Z = [dz[x] for x in ks]
        M = np.array([[Z[1].real - Z[0].real, Z[2].real - Z[0].real], [Z[1].imag - Z[0].imag, Z[2].imag - Z[0].imag]])
        l12 = np.linalg.solve(M, [z.real - Z[0].real, z.imag - Z[0].imag])
        lam = np.array([1.0 - l12.sum(), l12[0], l12[1]])
        if best is None or lam.min() > best[0]:
            best = (lam.min(), lam, ks)
    _, lam, ks = best
    return list(lam[0] * V[ks[0]] + lam[1] * V[ks[1]] + lam[2] * V[ks[2]])


def analyse_torus(L):
    m, rec = L['meta'], L['rec']
    t = np.array(rec['t'])
    cx, cy = np.array(rec['cx']), np.array(rec['cy'])
    Qb = np.array(rec['Q_ball'])
    Et, Qt = np.array(rec['E_tot']), np.array(rec['Q_tot'])

    def v_sehne(a_, b_):
        ii = np.where((t >= a_) & (t <= b_))[0]
        if len(ii) < MIN_PUNKTE:
            return None
        sel = list(ii[::SEHNE])
        if sel[-1] != ii[-1]:
            sel.append(ii[-1])
        s = np.concatenate([[0.0], np.cumsum(np.hypot(np.diff(cx[sel]), np.diff(cy[sel])))])
        return steigung(t[sel], s)

    def v_gerade(a_, b_):
        ii = np.where((t >= a_) & (t <= b_))[0]
        return steigung(t[ii], cx[ii]) if len(ii) >= 3 else None
    out = dict(name=m['name'], geo='torus', v0=m['v'], dt=m['dt'], T_ende=float(t[-1]),
               vollstaendig=m.get('vollstaendig'), K_nominal=m['K_nominal'], K_eff=m['K_eff'],
               E_tot_abw_max=float(np.max(np.abs(Et - Et[0]))), Q_tot_abw_max=float(np.max(np.abs(Qt - Qt[0]))),
               v_20_220=v_sehne(20, 220), v_3800_4000=v_sehne(3800, 4000),
               vx_gerade_20_220=v_gerade(20, 220), vx_gerade_3800_4000=v_gerade(3800, 4000),
               quer_drift_max=float(np.max(np.abs(cy - cy[0]))))
    k4 = int(np.argmin(np.abs(t - 4000.0)))
    out['t_4000'] = float(t[k4])
    out['Q_ball_0'] = float(Qb[0])
    out['Q_ball_4000'] = float(Qb[k4])
    out['Q_ball_rel_4000'] = float(Qb[k4] / Qb[0] - 1.0)
    out['S_max_spanne'] = [float(min(rec['S_max'])), float(max(rec['S_max']))]
    return out


def befehl_auswertung(args):
    dateien = sorted(glob.glob(os.path.join(args.ordner, 'ef2-*.json')))
    laeufe = {}
    for p in dateien:
        L = lade(p)
        if L.get('meta', {}).get('befehl') == 'lauf':
            laeufe[L['meta']['name']] = L
    an = {}
    for name, L in sorted(laeufe.items()):
        an[name] = analyse_ik(L) if L['meta']['geo'] == 'ikosaeder' else analyse_torus(L)
    aus = dict(befehl='auswertung', start=jetzt(), regeln=dict(R_einfang=R_EINFANG, R_frei=R_FREI, D_nah=D_NAH,
                                                               delta_ext=DELTA_EXT, sehne=SEHNE, min_punkte=MIN_PUNKTE),
               laeufe={}, urteile={})
    for name, a in an.items():
        aus['laeufe'][name] = {k_: v_ for k_, v_ in a.items() if not k_.startswith('_')}
    U = aus['urteile']
    haupt, schnell = args.haupt, args.schnell
    # E2-0
    a0 = an.get(args.torus)
    if a0 and a0['T_ende'] >= 4000.0 - 1e-9 and a0['v_20_220'] and a0['v_3800_4000']:
        rv = a0['v_3800_4000'] / a0['v_20_220'] - 1.0
        U['E2-0'] = dict(eingetroffen=bool(abs(rv) < 0.05 and abs(a0['Q_ball_rel_4000']) < 0.01),
                         v_20_220=a0['v_20_220'], v_3800_4000=a0['v_3800_4000'], v_verhaeltnis_minus_1=rv,
                         Q_ball_rel_4000=a0['Q_ball_rel_4000'],
                         regel='|v(3800..4000)/v(20..220) - 1| < 0,05 und |Q_ball(4000)/Q_ball(0) - 1| < 0,01 '
                               '(v ueber Sehnen, PLAN.md)')
    else:
        U['E2-0'] = dict(eingetroffen=None, urteil='nicht entscheidbar (Lauf fehlt oder zu kurz)')

    def e21(nm):
        a1 = an.get(nm)
        if not a1:
            return dict(eingetroffen=None, urteil='nicht entscheidbar (Lauf fehlt)')
        bg = a1['begegnungen']
        if not bg:
            return dict(eingetroffen=None, urteil='nicht entscheidbar (keine Begegnung)')
        b1 = bg[0]
        r = dict(spitze=b1['spitze'], d_min=b1['d_min'], t_min=b1['t_min'], v_vor=b1['v_vor'], v_nach=b1['v_nach'],
                 K_vor=b1['K_vor'], K_nach=b1['K_nach'])
        if not b1['nah']:
            r.update(eingetroffen=False, grund='erste Begegnung ist kein naher Durchgang')
        elif b1['v_nach'] is None:
            if b1['offen_am_ende'] and a1['T_ende'] < 8000.0 - 1e-9:
                r.update(eingetroffen=None, grund='Lauf endet vor dem Austritt')
            else:
                r.update(eingetroffen=False, grund='kein Austritt nach dem ersten Durchgang')
        else:
            q = b1['v_nach'] / a1['v0']
            r.update(eingetroffen=bool(0.60 <= q <= 0.80), v_nach_durch_v0=q,
                     v_nach_durch_v_vor=(b1['v_nach'] / b1['v_vor']) if b1['v_vor'] else None)
        return r

    def e22(nm):
        a1 = an.get(nm)
        if not a1:
            return dict(eingetroffen=None, urteil='nicht entscheidbar (Lauf fehlt)')
        if a1['T_ende'] < 8000.0 - 1e-9:
            return dict(eingetroffen=None, urteil='nicht entscheidbar (T_ende %.1f < 8000)' % a1['T_ende'],
                        einfang=a1['einfang'])
        return dict(eingetroffen=bool(a1['einfang']['eingefangen']), einfang=a1['einfang'])

    def e23(namen):
        dd = []
        for nm in namen:
            a1 = an.get(nm)
            if not a1:
                continue
            for b_ in a1['nahe_durchgaenge']:
                if b_['t_min'] <= 8000.0 and b_.get('K_verhaeltnis') is not None:
                    dd.append(dict(lauf=nm, spitze=b_['spitze'], t_min=b_['t_min'], K_vor=b_['K_vor'],
                                   K_nach=b_['K_nach'], K_verhaeltnis=b_['K_verhaeltnis'],
                                   K_abfall_rel=b_['K_abfall_rel']))
        nicht = [dict(lauf=nm, spitze=b_['spitze'], t_min=b_['t_min'], K_vor=b_['K_vor'], K_nach=b_['K_nach'])
                 for nm in namen if an.get(nm) for b_ in an[nm]['nahe_durchgaenge'] if b_.get('K_verhaeltnis') is None]
        if len(dd) < 2:
            return dict(eingetroffen=None, urteil='nicht entscheidbar (weniger als 2 auswertbare Durchgaenge)',
                        auswertbar=dd, nicht_auswertbar=nicht)
        mittel = float(np.mean([x['K_abfall_rel'] for x in dd]))
        mx = float(max(x['K_verhaeltnis'] for x in dd))
        geo_m = float(1.0 - np.exp(np.mean(np.log([max(x['K_verhaeltnis'], 1e-12) for x in dd]))))
        return dict(eingetroffen=bool(mittel >= 0.30 and mx <= 1.10), mittlerer_abfall=mittel,
                    groesstes_verhaeltnis=mx, geometrischer_abfall=geo_m, anzahl=len(dd), auswertbar=dd,
                    nicht_auswertbar=nicht)
    U['E2-1'] = e21(haupt)
    U['E2-1']['regel'] = ('erste Begegnung des Hauptlaufs ist ein naher Durchgang (d_min < 3) und '
                          '0,60 <= v_nach/0,05 <= 0,80 (v_nach = Sehnen-Geschwindigkeit der folgenden freien Strecke)')
    U['E2-2'] = e22(haupt)
    U['E2-2']['regel'] = ('Hauptlauf bis T = 8000: Ball am Ende innerhalb R_halb + 6 = 12,26 einer Spitze, '
                          'durchgehend seit t_c, und in [t_c, 8000] mindestens zwei Wenden (Maxima von d mit Hysterese 2)')
    U['E2-3'] = e23([haupt, schnell])
    U['E2-3']['regel'] = ('alle nahen Durchgaenge (d_min < 3, t_min <= 8000) der Laeufe %s und %s mit K davor und danach: '
                          'Mittel von 1 - K_nach/K_vor >= 0,30 und jedes K_nach/K_vor <= 1,10; mindestens 2' % (haupt,
                                                                                                                schnell))
    # Proben (Konvergenz)
    for probe in args.proben.split(','):
        if probe not in an:
            continue
        p21, p22, p23 = e21(probe), e22(probe), e23([probe, schnell])
        for nr, pu in (('E2-1', p21), ('E2-2', p22), ('E2-3', p23)):
            U[nr].setdefault('proben', {})[probe] = {k_: v_ for k_, v_ in pu.items() if k_ not in ('auswertbar',
                                                                                                  'nicht_auswertbar')}
            if pu.get('eingetroffen') is not None and pu.get('eingetroffen') != U[nr].get('eingetroffen'):
                U[nr]['vermerk'] = 'nicht konvergiert: Probe %s hat ein anderes Urteil' % probe
        nh = len([b_ for b_ in an[haupt]['nahe_durchgaenge'] if b_['t_min'] <= min(an[probe]['T_ende'], 8000.0)]) \
            if haupt in an else None
        npb = len([b_ for b_ in an[probe]['nahe_durchgaenge'] if b_['t_min'] <= min(an[probe]['T_ende'], 8000.0)])
        U['E2-2'].setdefault('durchgaenge_vergleich', {})[probe] = dict(haupt=nh, probe=npb,
                                                                        bis_t=min(an[probe]['T_ende'], 8000.0))
    aus['ende'] = jetzt()
    schreibe_json(os.path.join(args.ordner, 'auswertung.json'), aus, kompakt=False)
    for k_, v_ in U.items():
        print(k_, v_.get('eingetroffen'), json.dumps({kk: vv for kk, vv in v_.items() if kk not in ('regel',)})[:1500],
              flush=True)
    for nm, a in aus['laeufe'].items():
        kurz = {k_: v_ for k_, v_ in a.items() if k_ not in ('strecken', 'begegnungen', 'nahe_durchgaenge')}
        print(nm, json.dumps(kurz)[:900], flush=True)
        for b_ in a.get('begegnungen', []):
            print('   Begegnung', json.dumps({k_: (round(v_, 5) if isinstance(v_, float) else v_) for k_, v_ in b_.items()}),
                  flush=True)
        for s in a.get('strecken', []):
            print('   Strecke', json.dumps({k_: (round(v_, 6) if isinstance(v_, float) else v_) for k_, v_ in s.items()}),
                  flush=True)


# --------------------------------------------------------------------------------------------------------------------
# Bild
# --------------------------------------------------------------------------------------------------------------------
def K_lokal(a, L):
    """Lokale Geschwindigkeit ueber +-10 Diagnosepunkte (Sehne in der Karte der naechsten Spitze), K daraus."""
    t, d, th, k, dn, ok = a['_reihen']
    m, rec = L['meta'], L['rec']
    Qb = np.array(rec['Q_ball'])
    n = len(t)
    tt, KK = [], []
    for i in range(10, n - 10):
        c = k[i]
        if not (np.isfinite(dn[i]) and ok[i - 10, c] and ok[i + 10, c]):
            continue
        s = float(kegelabstand(d[i - 10, c], th[i - 10, c], d[i + 10, c], th[i + 10, c]))
        v = s / (t[i + 10] - t[i - 10])
        if v < 1:
            tt.append(t[i])
            KK.append(K_von(v, Qb[i], m))
    return np.array(tt), np.array(KK)


def befehl_bild(args):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    dateien = sorted(glob.glob(os.path.join(args.ordner, 'ef2-*.json')))
    laeufe = {}
    for p in dateien:
        L = lade(p)
        if L.get('meta', {}).get('befehl') == 'lauf' and L['meta']['geo'] == 'ikosaeder':
            laeufe[L['meta']['name']] = L
    namen = [x for x in args.namen.split(',') if x in laeufe]
    V, F, adj = ikosaeder_ecken(40.0)
    for nm in namen:
        L = laeufe[nm]
        a = analyse_ik(L)
        V, F, adj = ikosaeder_ecken(L['meta']['a'])
        t, d, th, k, dn, ok = a['_reihen']
        P = a['_P']
        fig = plt.figure(figsize=(16, 5.2))
        ax = fig.add_subplot(1, 3, 1, projection='3d')
        for i in range(12):
            for j in range(i + 1, 12):
                if adj[i, j]:
                    ax.plot(*zip(V[i], V[j]), color='#bbbbbb', lw=0.7)
        ax.scatter(V[:, 0], V[:, 1], V[:, 2], color='k', s=10)
        for i in range(12):
            ax.text(*(V[i] * 1.08), str(i), fontsize=7)
        sc = ax.scatter(P[:, 0], P[:, 1], P[:, 2], c=t, cmap='viridis', s=2)
        fig.colorbar(sc, ax=ax, shrink=0.6, label='t')
        ax.set_title('%s: Bahn (Ladungsschwerpunkt)' % nm, fontsize=9)
        ax.set_box_aspect((1, 1, 1))
        ax2 = fig.add_subplot(1, 3, 2)
        ax2.plot(t, dn, lw=0.8, color='#1f4e79')
        ax2.axhline(D_NAH, color='#c0392b', lw=0.6, ls=':')
        ax2.axhline(R_FREI, color='k', lw=0.5, ls=':')
        ax2.axhline(R_EINFANG, color='#7d3c98', lw=0.5, ls='--')
        for b_ in a['nahe_durchgaenge']:
            ax2.annotate('S%d' % b_['spitze'], (b_['t_min'], b_['d_min']), fontsize=7, color='#c0392b',
                         xytext=(0, -10), textcoords='offset points', ha='center')
        ax2.set_xlabel('t')
        ax2.set_ylabel('Abstand zur naechsten Spitze (harmonisch)')
        ax2.set_title('d(t); rot: < 3 (naher Durchgang), violett: 12,26 (Einfanggrenze)', fontsize=9)
        ax3 = fig.add_subplot(1, 3, 3)
        tk, Kk = K_lokal(a, L)
        ax3.plot(tk, Kk, lw=0.6, color='#999999', label='K lokal (Sehne ueber 40 Zeiteinheiten)')
        for s in a['strecken']:
            if s.get('K') is not None:
                ax3.plot([s['t_von'], s['t_bis']], [s['K'], s['K']], color='#1f4e79', lw=2.0)
        for b_ in a['nahe_durchgaenge']:
            ax3.axvline(b_['t_min'], color='#c0392b', lw=0.5, ls=':')
        ax3.set_yscale('log')
        ax3.set_xlabel('t')
        ax3.set_ylabel('K = (gamma - 1) E_rest(Q_ball)')
        ax3.set_title('Bewegungsenergie; blau: freie Strecken (Sehnen-Fit)', fontsize=9)
        ax3.legend(fontsize=7)
        fig.tight_layout()
        pfad = os.path.join(args.ordner, 'bahn-%s.png' % nm)
        fig.savefig(pfad, dpi=120)
        plt.close(fig)
        print('geschrieben', pfad, flush=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    for nm in namen:
        L = laeufe[nm]
        a = analyse_ik(L)
        tk, Kk = K_lokal(a, L)
        ax.plot(tk, Kk, lw=0.7, label=nm)
    ax.set_yscale('log')
    ax.set_xlabel('t')
    ax.set_ylabel('K lokal')
    ax.set_title('EINFANG-2: Bewegungsenergie K(t), alle Ikosaeder-Laeufe')
    ax.legend(fontsize=8)
    fig.tight_layout()
    pfad = os.path.join(args.ordner, 'kt-alle.png')
    fig.savefig(pfad, dpi=120)
    print('geschrieben', pfad, flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='befehl', required=True)
    a = sub.add_parser('lauf')
    a.add_argument('--name', required=True)
    a.add_argument('--geo', choices=['ikosaeder', 'torus'], required=True)
    a.add_argument('--nu', type=int, default=134)
    a.add_argument('--a', type=float, default=40.0)
    a.add_argument('--N1', type=int, default=335)
    a.add_argument('--N2', type=int, default=536)
    a.add_argument('--h', type=float, default=40.0 / 134.0)
    a.add_argument('--Q', type=float, default=200.0)
    a.add_argument('--v', type=float, required=True)
    a.add_argument('--b', type=float, default=0.0)
    a.add_argument('--dt', type=float, required=True)
    a.add_argument('--T', type=float, required=True)
    a.add_argument('--diag', type=float, default=2.0)
    a.add_argument('--S-thr', dest='S_thr', type=float, default=0.01)
    a.add_argument('--R-ball', dest='R_ball', type=float, default=15.0)
    a.add_argument('--R-flicken', dest='R_flicken', type=float, default=30.0)
    a.add_argument('--geraet', choices=['cuda', 'cpu'], required=True)
    a.add_argument('--wand', type=float, default=500.0)
    a.add_argument('--zustand', default=None)
    a.add_argument('--fortsetzen', default=None)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('auswertung')
    a.add_argument('--ordner', required=True)
    a.add_argument('--haupt', default='ik-v0.05')
    a.add_argument('--schnell', default='ik-v0.1')
    a.add_argument('--torus', default='torus-v0.05')
    a.add_argument('--proben', default='ik-v0.05-dt0.05,ik-v0.05-h0.2')
    a = sub.add_parser('bild')
    a.add_argument('--ordner', required=True)
    a.add_argument('--namen', required=True)
    args = ap.parse_args()
    if args.befehl == 'lauf' and args.zustand is None:
        args.zustand = args.aus.replace('.json', '') + '-zustand.npz'
    try:
        {'lauf': befehl_lauf, 'auswertung': befehl_auswertung, 'bild': befehl_bild}[args.befehl](args)
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
