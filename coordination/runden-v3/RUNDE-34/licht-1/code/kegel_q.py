#!/usr/bin/env python3
"""KEGEL-Q (Runde 26, runden-v3, explorativ). Code-Agent fuer die Leitung claude-primary.

Modell M1: U(S) = S - S^2 + S^3/2, S = f^2, phi = f exp(-i omega t), f reell.
Ladung Q = 2 omega Int f^2 dA, Energie bei fester Ladung E[f] = Q^2/(4 Int f^2) + Int (|grad f|^2 + U(f^2)).

Befehle:
  radial      ebene radiale 2D-Familie (FV-Gitter, Newton bei festem omega^2), Zielladungen und exakte Bindung
              B(Q) = E_eben(Q) - E_eben(sQ)/s fuer s = 6/5 (Fuenfer-Ecke) und s = 6/7 (Siebener-Ecke), dE/dQ-Probe.
  netz        Netzpruefung: Grade, Winkeldefekt, Euler-Charakteristik, Flaechen, Kotangens-Gewichte.
  ball        Baelle bei festem Q und festgehaltenem harmonischem Schwerpunkt (Augmented Lagrangian + L-BFGS).
  auswertung  Urteile KQ0 bis KQ3 nach PLAN.md aus den JSON-Dateien eines Laufordners.

Netz: gleichseitiges Dreiecksnetz aus n Sektoren zu je 60 Grad um die Ecke 0 (n = 5 Fuenfer-Ecke, n = 6 flacher
Flicken, n = 7 Siebener-Ecke), abgeschnitten bei geodaetischem Radius R, Dirichlet f = 0 auf den Randecken.
Laplace: Kotangens-Gewichte w_ij = (cot a + cot b)/2, baryzentrische Eckflaechen A_i.
Diskrete Energie: E = Q^2/(4 Sum A_i f_i^2) + Sum_Kanten w_ij (f_i - f_j)^2 + Sum A_i U(f_i^2).

Ort eines Balls (im Plan begruendet): harmonischer Schwerpunkt W = Sum A f^2 w / Sum A f^2 mit w = r^s exp(i s phi),
s = 2 pi/Theta = 6/n, phi = Abwicklungswinkel gegen die Laufrichtung theta0 = 0 (eine Gitterrichtung).
W = 0 fuer den auf der Spitze zentrierten Ball (Symmetrie); W = d^s exakt fuer einen rotationssymmetrischen Ball im
geodaetischen Abstand d, der die Spitze nicht ueberdeckt (Mittelwerteigenschaft der holomorphen Funktion z^s).
Abstand d_W = |W|^(1/s). Nebenbedingungen c1 = Sum A f^2 (u - D1)/N0 = 0, c2 = Sum A f^2 (v - D2)/N0 = 0 (linear
in f^2), exakt erzwungen per Augmented Lagrangian; die gemeldete Energie E enthaelt keinen Straf- oder
Multiplikatorterm. Aus dem Multiplikator m1 folgt dE/dD1 = -m1 N/N0 (N = Sum A f^2).
"""
import argparse
import glob
import json
import math
import os
import sys
import time

# Ein Thread je Lauf (kleintest.sh setzt CPUQuota = 100 %; mehrfaedige BLAS-Aufrufe wuerden dort gedrosselt).
for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_v, '1')

import numpy as np
import scipy.sparse as sp
from scipy.linalg import solve_banded
from scipy.optimize import brentq, minimize

PI = math.pi
T_START = time.perf_counter()
OMC2 = 0.5                      # omega_c^2 von M1: min U(S)/S = 1/2 bei S = 1
SIGMA_TW = math.sqrt(2.0) / 4.0  # Wandspannung bei omega_c: Int 2 f'^2 dx = sqrt(2)/4
S5 = 6.0 / 5.0
S7 = 6.0 / 7.0


def U(S):
    return S - S * S + 0.5 * S ** 3


def dU(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def d2U(S):
    return -2.0 + 3.0 * S


def jetzt():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def schreibe_json(pfad, obj):
    tmp = pfad + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump(obj, fh, indent=1)
    os.replace(tmp, pfad)


# --------------------------------------------------------------------------------------------------------------------
# Radiale ebene Familie
# --------------------------------------------------------------------------------------------------------------------
class Radial:
    """FV-Gitter r_j = (j + 1/2) dr, Dirichlet f = 0 bei r = (M + 1/2) dr. Die diskrete Energie hat exakt die
    diskreten Feldgleichungen als Euler-Lagrange-Gleichungen, daher gilt dE/dQ = omega auch im Diskreten."""

    def __init__(self, dr, rmax):
        self.dr = dr
        self.M = int(round(rmax / dr))
        j = np.arange(self.M, dtype=float)
        self.r = (j + 0.5) * dr
        self.rp = (j + 1.0) * dr
        self.rm = j * dr

    def teile(self, f):
        dr = self.dr
        S = f * f
        I = 2 * PI * dr * float(np.sum(self.r * S))
        fp = np.append(f[1:], 0.0)
        G = 2 * PI * float(np.sum(self.rp * (fp - f) ** 2)) / dr
        V = 2 * PI * dr * float(np.sum(self.r * U(S)))
        return I, G, V

    def residuum(self, f, om2):
        fm = np.concatenate(([0.0], f[:-1]))
        fp = np.append(f[1:], 0.0)
        S = f * f
        return 2 * (self.rm * (f - fm) - self.rp * (fp - f)) / self.dr + 2 * self.dr * self.r * (dU(S) - om2) * f

    def rnorm(self, R):
        return float(np.max(np.abs(R / (self.dr * self.r))))

    def newton(self, f0, om2, tol=1e-11, maxit=80):
        f = f0.copy()
        R = self.residuum(f, om2)
        nr = self.rnorm(R)
        it = 0
        off = -2 * self.rp[:-1] / self.dr
        while nr > tol and it < maxit:
            it += 1
            S = f * f
            ab = np.zeros((3, self.M))
            ab[0, 1:] = off
            ab[1, :] = 2 * (self.rm + self.rp) / self.dr + 2 * self.dr * self.r * (dU(S) + 2 * S * d2U(S) - om2)
            ab[2, :-1] = off
            df = solve_banded((1, 1), ab, -R)
            t = 1.0
            while True:
                fn = f + t * df
                Rn = self.residuum(fn, om2)
                nn = self.rnorm(Rn)
                if nn < nr or t < 1e-4:
                    break
                t *= 0.5
            f, R, nr = fn, Rn, nn
        return f, it, nr

    def groessen(self, f, om2):
        I, G, V = self.teile(f)
        om = math.sqrt(om2)
        S = f * f
        S0 = float(S[0])
        k = int(np.argmax(S < 0.5 * S0))
        r_half = float(self.r[k - 1] + (0.5 * S0 - S[k - 1]) * (self.r[k] - self.r[k - 1]) / (S[k] - S[k - 1]))
        return dict(om2=om2, omega=om, Q=2 * om * I, E=om2 * I + G + V, I=I, G=G, V=V, S0=S0, R_half=r_half,
                    kappa=math.sqrt(1.0 - om2))


def radial_familie(rad, om2_start, om2_ab, om2_auf):
    """Fortsetzung von om2_start abwaerts (om2_ab, fallend) und aufwaerts (om2_auf, steigend)."""
    R0 = SIGMA_TW / (om2_start - OMC2)
    S = 1.0 / (1.0 + np.exp(np.clip(math.sqrt(2.0) * (rad.r - R0), -700.0, 700.0)))
    f0, it0, nr0 = rad.newton(np.sqrt(S), om2_start)
    if np.max(f0) < 0.05 or nr0 > 1e-8:
        raise RuntimeError('Start der radialen Familie gescheitert: res %.3e max f %.3e' % (nr0, np.max(f0)))
    erg = {om2_start: (f0, it0, nr0)}
    for folge in (om2_ab, om2_auf):
        f_prev, o_prev, f_pp, o_pp = f0, om2_start, None, None
        for om2 in folge:
            guess = f_prev if f_pp is None else f_prev + (om2 - o_prev) / (o_prev - o_pp) * (f_prev - f_pp)
            f, it, nr = rad.newton(guess, om2)
            if nr > 1e-9 or np.max(f) < 0.05:
                f2, it2, nr2 = rad.newton(f_prev, om2)
                if nr2 < nr and np.max(f2) >= 0.05:
                    f, it, nr = f2, it2, nr2
            erg[om2] = (f, it, nr)
            f_pp, o_pp, f_prev, o_prev = f_prev, o_prev, f, om2
    fam = []
    for om2 in sorted(erg):
        f, it, nr = erg[om2]
        g = rad.groessen(f, om2)
        g['newton_it'] = it
        g['res'] = nr
        fam.append((g, f))
    return fam


def loese_Q(rad, fam, Qt):
    """Profil der ebenen Familie mit Ladung Qt auf dem VK-stabilen Ast (erste Klammer von kleinem omega^2 her)."""
    a = None
    for k in range(len(fam) - 1):
        Qa, Qb = fam[k][0]['Q'], fam[k + 1][0]['Q']
        if (Qa - Qt) * (Qb - Qt) <= 0 and Qb < Qa:
            a = k
            break
    if a is None:
        raise RuntimeError('Ladung %.6f nicht im stabilen Ast der Familie' % Qt)
    ref = [fam[a][1]]

    def F(om2):
        f, it, nr = rad.newton(ref[0], om2)
        ref[0] = f
        return rad.groessen(f, om2)['Q'] - Qt

    om2 = brentq(F, fam[a][0]['om2'], fam[a + 1][0]['om2'], xtol=1e-16, rtol=1e-15, maxiter=200)
    f, it, nr = rad.newton(ref[0], om2)
    g = rad.groessen(f, om2)
    g['res'] = nr
    g['dQdom2_fam'] = (fam[a + 1][0]['Q'] - fam[a][0]['Q']) / (fam[a + 1][0]['om2'] - fam[a][0]['om2'])
    return g, f


def baue_familie(dr, rmax):
    rad = Radial(dr, rmax)
    ab = [round(0.62 - 0.002 * k, 6) for k in range(1, 46)]      # 0.618 ... 0.530
    auf = [round(0.62 + 0.005 * k, 6) for k in range(1, 57)]     # 0.625 ... 0.900
    fam = radial_familie(rad, 0.62, ab, auf)
    return rad, fam


def befehl_radial(args):
    Qs = [float(x) for x in args.Q.split(',')]
    aus = dict(befehl='radial', start=jetzt(), dr=args.dr, rmax=args.rmax, Q_liste=Qs)
    ergebnisse = {}
    for dr in (args.dr, args.dr / 2):
        rad, fam = baue_familie(dr, args.rmax)
        tab = [g for g, f in fam]
        # dE/dQ = omega entlang der Familie (zentrale Differenzen)
        dev = []
        for k in range(1, len(tab) - 1):
            dEdQ = (tab[k + 1]['E'] - tab[k - 1]['E']) / (tab[k + 1]['Q'] - tab[k - 1]['Q'])
            dev.append(abs(dEdQ / tab[k]['omega'] - 1.0))
        # VK-Minimum der Ladung
        kmin = int(np.argmin([g['Q'] for g in tab]))
        ziel = []
        for Qt in Qs:
            g, f = loese_Q(rad, fam, Qt)
            dq = 1e-3 * Qt
            gp, _ = loese_Q(rad, fam, Qt + dq)
            gm, _ = loese_Q(rad, fam, Qt - dq)
            z = dict(Q=Qt, omega=g['omega'], om2=g['om2'], E=g['E'], I=g['I'], R_half=g['R_half'], S0=g['S0'],
                     kappa=g['kappa'], res=g['res'], dQdom2=g['dQdom2_fam'],
                     dEdQ_num=(gp['E'] - gm['E']) / (2 * dq), E_durch_Q=g['E'] / Qt)
            z['dEdQ_rel_abw'] = z['dEdQ_num'] / g['omega'] - 1.0
            for name, s in (('n5', S5), ('n7', S7)):
                gs, fs = loese_Q(rad, fam, s * Qt)
                B = g['E'] - gs['E'] / s
                z[name] = dict(s=s, Q_eben=s * Qt, omega_eben=gs['omega'], E_eben_sQ=gs['E'], E_kegel=gs['E'] / s,
                               B=B, R_half_kegel=gs['R_half'], dQdom2=gs['dQdom2_fam'],
                               B_durch_duennwand=B / (SIGMA_TW * 2 * PI * g['R_half']),
                               duennwand_soll=1.0 - 1.0 / math.sqrt(s))
            ziel.append(z)
        ergebnisse['dr=%g' % dr] = dict(
            familie=[{k: g[k] for k in ('om2', 'omega', 'Q', 'E', 'R_half', 'S0', 'kappa', 'res', 'newton_it')}
                     for g in tab],
            dEdQ_max_rel_abw=float(max(dev)), VK_min=dict(om2=tab[kmin]['om2'], Q=tab[kmin]['Q']),
            ziele=ziel)
        print('dr = %g: Familie %d Punkte, max res %.2e, dE/dQ max rel Abw %.2e, Q_min %.4f bei om2 %.3f' % (
            dr, len(tab), max(g['res'] for g in tab), max(dev), tab[kmin]['Q'], tab[kmin]['om2']), flush=True)
        for z in ziel:
            print('  Q %.4f om %.6f R_half %.3f kappa %.4f E %.8f  B5 %.6f (%.4f duennw)  B7 %.6f (%.4f)  dEdQ %.1e'
                  % (z['Q'], z['omega'], z['R_half'], z['kappa'], z['E'], z['n5']['B'], z['n5']['B_durch_duennwand'],
                     z['n7']['B'], z['n7']['B_durch_duennwand'], z['dEdQ_rel_abw']), flush=True)
    aus['ergebnisse'] = ergebnisse
    a, b = ergebnisse['dr=%g' % args.dr]['ziele'], ergebnisse['dr=%g' % (args.dr / 2)]['ziele']
    aus['dr_probe'] = [dict(Q=x['Q'], dE=y['E'] - x['E'], dB5=y['n5']['B'] - x['n5']['B'],
                            dB7=y['n7']['B'] - x['n7']['B']) for x, y in zip(a, b)]
    aus['ende'] = jetzt()
    aus['dauer_s'] = time.perf_counter() - T_START
    schreibe_json(args.aus, aus)
    print('geschrieben', args.aus, 'Dauer %.1f s' % aus['dauer_s'])


# --------------------------------------------------------------------------------------------------------------------
# Netz
# --------------------------------------------------------------------------------------------------------------------
class Netz:
    def __init__(self, n, h, R):
        self.n, self.h, self.R = n, h, R
        self.Theta = n * PI / 3.0
        self.s = 6.0 / n
        sq3 = math.sqrt(3.0)
        K = int(math.ceil(R / h)) + 2
        key = {(0, 0, 0): 0}
        rr = [0.0]
        th = [0.0]
        for k in range(n):
            for i in range(1, K + 1):
                for j in range(0, K + 1):
                    r = h * math.sqrt(i * i + i * j + j * j)
                    if r > R + 1e-9:
                        continue
                    key[(k, i, j)] = len(rr)
                    rr.append(r)
                    th.append(k * PI / 3.0 + math.atan2(j * sq3 / 2.0, i + j / 2.0))

        def canon(k, i, j):
            if i == 0 and j == 0:
                return (0, 0, 0)
            if i == 0:
                return ((k + 1) % n, j, 0)
            return (k, i, j)

        tris, loc = [], []
        for k in range(n):
            for i in range(K):
                for j in range(K):
                    for t in (((i, j), (i + 1, j), (i, j + 1)), ((i + 1, j), (i + 1, j + 1), (i, j + 1))):
                        ids = [key.get(canon(k, a, b)) for a, b in t]
                        if None in ids:
                            continue
                        tris.append(ids)
                        loc.append([[h * (a + b / 2.0), h * b * sq3 / 2.0] for a, b in t])
        tris = np.array(tris, dtype=np.int64)
        loc = np.array(loc, dtype=float)
        used = np.unique(tris)
        remap = -np.ones(len(rr), dtype=np.int64)
        remap[used] = np.arange(len(used))
        tris = remap[tris]
        self.r = np.array(rr)[used]
        self.theta = np.array(th)[used]
        self.apex = int(remap[0])
        N = len(used)
        self.N = N
        # Geometrie je Dreieck (lokale Abwicklung)
        e01 = loc[:, 1] - loc[:, 0]
        e02 = loc[:, 2] - loc[:, 0]
        e12 = loc[:, 2] - loc[:, 1]

        def cr(a, b):
            return a[:, 0] * b[:, 1] - a[:, 1] * b[:, 0]

        def dt(a, b):
            return a[:, 0] * b[:, 0] + a[:, 1] * b[:, 1]

        twoA = np.abs(cr(e01, e02))
        cot0 = dt(e01, e02) / twoA
        cot1 = dt(-e01, e12) / twoA
        cot2 = dt(-e02, -e12) / twoA
        ang0 = np.arctan2(twoA, dt(e01, e02))
        ang1 = np.arctan2(twoA, dt(-e01, e12))
        ang2 = np.arctan2(twoA, dt(-e02, -e12))
        self.A = np.bincount(tris.ravel(), weights=np.repeat(twoA / 6.0, 3), minlength=N)
        self.winkelsumme = np.bincount(tris.ravel(), weights=np.stack([ang0, ang1, ang2], 1).ravel(), minlength=N)
        # Kanten: (1,2) gegenueber 0, (0,2) gegenueber 1, (0,1) gegenueber 2
        ei = np.concatenate([tris[:, 1], tris[:, 0], tris[:, 0]])
        ej = np.concatenate([tris[:, 2], tris[:, 2], tris[:, 1]])
        ww = np.concatenate([cot0, cot1, cot2]) / 2.0
        lo, hi = np.minimum(ei, ej), np.maximum(ei, ej)
        kid = lo * N + hi
        uk, inv, cnt = np.unique(kid, return_inverse=True, return_counts=True)
        w = np.bincount(inv, weights=ww)
        self.kanten_i = (uk // N).astype(np.int64)
        self.kanten_j = (uk % N).astype(np.int64)
        self.w = w
        self.anz_kanten = len(uk)
        self.anz_dreiecke = len(tris)
        rand_k = cnt == 1
        rand = np.zeros(N, dtype=bool)
        rand[self.kanten_i[rand_k]] = True
        rand[self.kanten_j[rand_k]] = True
        self.rand = rand
        self.frei = np.where(~rand)[0]
        self.grad = np.bincount(np.concatenate([self.kanten_i, self.kanten_j]), minlength=N)
        I_, J_ = self.kanten_i, self.kanten_j
        L = sp.coo_matrix((np.concatenate([w, w, -w, -w]),
                           (np.concatenate([I_, J_, I_, J_]), np.concatenate([I_, J_, J_, I_]))), shape=(N, N)).tocsr()
        self.L = L
        self.Lff = L[self.frei][:, self.frei].tocsr()
        self.setze_richtung(0.0)

    def setze_richtung(self, theta0):
        self.theta0 = theta0
        T = self.Theta
        self.phi = np.mod(self.theta - theta0 + T / 2.0, T) - T / 2.0
        rs = self.r ** self.s
        self.u = rs * np.cos(self.s * self.phi)
        self.v = rs * np.sin(self.s * self.phi)
        self.X = self.r * np.cos(self.phi)
        self.Y = self.r * np.sin(self.phi)

    def abstand(self, d=None, xy=None):
        """Geodaetischer Abstand jeder Ecke vom Punkt (d, phi = 0) bzw. (bei n = 6) vom Punkt xy."""
        if xy is not None:
            return np.hypot(self.X - xy[0], self.Y - xy[1])
        D = np.abs(self.phi)
        dist = np.sqrt(np.maximum(self.r ** 2 + d * d - 2 * self.r * d * np.cos(D), 0.0))
        return np.where(D < PI, dist, self.r + d)

    def pruefung(self):
        frei = ~self.rand
        g = self.grad
        innen_grade = {int(k): int(v) for k, v in zip(*np.unique(g[frei], return_counts=True))}
        defekt = 2 * PI - self.winkelsumme
        nichtnull = np.where(frei & (np.abs(defekt) > 1e-9))[0]
        V, E, F = self.N, self.anz_kanten, self.anz_dreiecke
        w_innen = self.w[~(self.rand[self.kanten_i] & self.rand[self.kanten_j])]
        return dict(n=self.n, h=self.h, R=self.R, ecken=V, kanten=E, dreiecke=F, euler=V - E + F,
                    freie_ecken=int(frei.sum()), innen_grade=innen_grade,
                    grad_spitze=int(g[self.apex]), spitze_innen=bool(frei[self.apex]),
                    defekt_spitze=float(defekt[self.apex]), defekt_soll=float(2 * PI - self.n * PI / 3),
                    ecken_mit_defekt=[int(i) for i in nichtnull[:10]], anzahl_ecken_mit_defekt=int(len(nichtnull)),
                    defekt_rest_max=float(np.max(np.abs(np.delete(defekt[frei], np.where(np.where(frei)[0] == self.apex)[0])))),
                    flaeche=float(self.A.sum()), flaeche_kegel_soll=float(self.Theta / 2 * self.R ** 2),
                    A_spitze=float(self.A[self.apex]), A_regulaer=float(math.sqrt(3) / 2 * self.h ** 2),
                    w_min=float(w_innen.min()), w_max=float(w_innen.max()), w_soll=float(1 / math.sqrt(3)))


def befehl_netz(args):
    aus = dict(befehl='netz', start=jetzt(), netze=[])
    for n in (5, 6, 7):
        t = time.perf_counter()
        net = Netz(n, args.h, args.R)
        p = net.pruefung()
        p['bauzeit_s'] = time.perf_counter() - t
        aus['netze'].append(p)
        print(json.dumps(p), flush=True)
    aus['ende'] = jetzt()
    if args.aus:
        schreibe_json(args.aus, aus)


# --------------------------------------------------------------------------------------------------------------------
# Ball bei festem Q und festem Ort
# --------------------------------------------------------------------------------------------------------------------
def loese_ball(net, Q, D1, D2, f0, mu, tol_c, max_aussen, maxiter, gtol):
    fr = net.frei
    A = net.A[fr]
    Lff = net.Lff
    g1 = net.u[fr] - D1
    g2 = net.v[fr] - D2
    x = f0[fr].copy()
    N0 = float(A @ (x * x))
    lam = np.zeros(2)
    zaehler = dict(nfev=0)

    def teile(x):
        S = x * x
        I = float(A @ S)
        Lx = Lff @ x
        G = float(x @ Lx)
        V = float(A @ U(S))
        AS = A * S
        c1 = float(AS @ g1) / N0
        c2 = float(AS @ g2) / N0
        return S, I, Lx, G, V, c1, c2

    def fun(x):
        zaehler['nfev'] += 1
        S, I, Lx, G, V, c1, c2 = teile(x)
        E = Q * Q / (4 * I) + G + V
        m1 = lam[0] + mu * c1
        m2 = lam[1] + mu * c2
        LA = E + lam[0] * c1 + lam[1] * c2 + 0.5 * mu * (c1 * c1 + c2 * c2)
        om2 = Q * Q / (4 * I * I)
        g = 2 * Lx + 2 * A * x * (dU(S) - om2 + (m1 * g1 + m2 * g2) / N0)
        return LA, g

    verlauf = []
    nit = 0
    E_alt = None
    for aussen in range(max_aussen):
        res = minimize(fun, x, jac=True, method='L-BFGS-B',
                       options=dict(maxiter=maxiter, maxcor=20, ftol=1e-16, gtol=gtol, maxls=60))
        x = res.x
        nit += int(res.nit)
        S, I, Lx, G, V, c1, c2 = teile(x)
        E = Q * Q / (4 * I) + G + V
        lam_benutzt = lam.copy()
        lam = lam + mu * np.array([c1, c2])
        verlauf.append(dict(aussen=aussen, E=E, c1=c1, c2=c2, lam1=float(lam[0]), lam2=float(lam[1]),
                            nit=int(res.nit), msg=str(res.message)[:60]))
        fertig = max(abs(c1), abs(c2)) < tol_c and (E_alt is not None and abs(E - E_alt) < 1e-11 * abs(E))
        E_alt = E
        if fertig:
            break
    # Restgradient (Funktionalableitung) der Lagrange-Funktion mit dem wirksamen Multiplikator m = lam_benutzt + mu c
    om2 = Q * Q / (4 * I * I)
    m1, m2 = float(lam[0]), float(lam[1])
    gE = 2 * Lx + 2 * A * x * (dU(S) - om2)
    gL = gE + 2 * A * x * (m1 * g1 + m2 * g2) / N0
    f = np.zeros(net.N)
    f[fr] = x
    return dict(E=E, I=I, G=G, V=V, omega=math.sqrt(om2), c1=c1, c2=c2, m1=m1, m2=m2, N=I, N0=N0,
                res_max=float(np.max(np.abs(gL / (2 * A)))), res_E_ohne_m=float(np.max(np.abs(gE / (2 * A)))),
                aussen=len(verlauf), nit=nit, nfev=zaehler['nfev'], verlauf=verlauf), f


def befehl_ball(args):
    net = Netz(args.n, args.h, args.R)
    rad, fam = baue_familie(args.dr_radial, 60.0)
    Qs = [float(x) for x in args.Q.split(',')]
    if len(Qs) > 1 and '{Q}' not in args.aus:
        raise RuntimeError('mehrere Q brauchen {Q} im Ausgabenamen')
    for Q in Qs:
        a = argparse.Namespace(**vars(args))
        a.Q = Q
        a.aus = args.aus.replace('{Q}', '%g' % Q)
        ball_ein_Q(a, net, rad, fam)


def ball_ein_Q(args, net, rad, fam):
    pr = net.pruefung()
    s = net.s
    gQ, fQ = loese_Q(rad, fam, args.Q)
    gsQ, fsQ = loese_Q(rad, fam, s * args.Q) if args.n != 6 else (gQ, fQ)
    aus = dict(befehl='ball', rolle=args.rolle, start=jetzt(), n=args.n, h=args.h, R=args.R, Q=args.Q, s=s,
               mu=args.mu, netz=pr,
               radial=dict(omega_Q=gQ['omega'], R_half_Q=gQ['R_half'], kappa_Q=gQ['kappa'], E_eben_Q=gQ['E'],
                           omega_sQ=gsQ['omega'], E_eben_sQ=gsQ['E'], E_kegel_exakt=gsQ['E'] / s),
               punkte=[])
    orte = []
    if args.d:
        for d in [float(x) for x in args.d.split(',')]:
            orte.append(('d', d))
    if args.xy:
        for p in args.xy.split(';'):
            a, b = p.split(',')
            orte.append(('xy', (float(a), float(b))))
    print('Netz n=%d h=%g R=%g: %d Ecken, %d frei, Euler %d, Grad Spitze %d, Defekt %.6f (Soll %.6f)' % (
        args.n, args.h, args.R, pr['ecken'], pr['freie_ecken'], pr['euler'], pr['grad_spitze'],
        pr['defekt_spitze'], pr['defekt_soll']), flush=True)
    for art, wert in orte:
        t = time.perf_counter()
        if art == 'd':
            d = wert
            D1, D2 = d ** s, 0.0
            dist = net.abstand(d=d)
            prof = fsQ if (d == 0.0 and args.n != 6) else fQ
        else:
            d = None
            D1, D2 = wert
            dist = net.abstand(xy=wert)
            prof = fQ
        f0 = np.interp(dist, rad.r, prof, right=0.0)
        f0[net.rand] = 0.0
        r, f = loese_ball(net, args.Q, D1, D2, f0, args.mu, args.tol_c, args.max_aussen, args.maxiter, args.gtol)
        S = f * f
        Nn = float(net.A @ S)
        W = complex(float(net.A @ (S * net.u)) / Nn, float(net.A @ (S * net.v)) / Nn)
        punkt = dict(art=art, d=d, xy=(list(wert) if art == 'xy' else None), D1=D1, D2=D2)
        punkt.update({k: v for k, v in r.items() if k != 'verlauf'})
        punkt['W_re'] = W.real
        punkt['W_im'] = W.imag
        punkt['d_W'] = abs(W) ** (1.0 / s)
        punkt['X_karte'] = float(net.A @ (S * net.X)) / Nn
        punkt['Y_karte'] = float(net.A @ (S * net.Y)) / Nn
        punkt['f_max'] = float(f.max())
        punkt['S_spitze'] = float(S[net.apex])
        punkt['f_rand_max'] = float(np.max(f[np.abs(net.r - net.R) < 2 * net.h + 1e-9])) if True else None
        # dE/dD1 aus dem Multiplikator und daraus dE/dd (nur bei Laufrichtung, d > 0)
        punkt['dEdD1_lambda'] = -r['m1'] * Nn / r['N0']
        if art == 'd' and d > 0:
            punkt['dEdd_lambda'] = punkt['dEdD1_lambda'] * s * d ** (s - 1.0)
        punkt['E_korr_erste_ordnung'] = r['E'] + r['m1'] * r['c1'] + r['m2'] * r['c2']
        punkt['verlauf'] = r['verlauf']
        punkt['dauer_s'] = time.perf_counter() - t
        aus['punkte'].append(punkt)
        aus['zwischenstand'] = jetzt()
        schreibe_json(args.aus, aus)
        print('%s %s: E %.10f omega %.6f c %.1e %.1e m1 %.3e res %.1e aussen %d nit %d d_W %s  (%.1f s)' % (
            art, wert, r['E'], r['omega'], r['c1'], r['c2'], r['m1'], r['res_max'], r['aussen'], r['nit'],
            ('%.6f' % punkt['d_W']), punkt['dauer_s']), flush=True)
    aus['ende'] = jetzt()
    aus['dauer_s'] = time.perf_counter() - T_START
    schreibe_json(args.aus, aus)
    print('geschrieben', args.aus, 'Dauer %.1f s' % aus['dauer_s'])


# --------------------------------------------------------------------------------------------------------------------
# Auswertung nach PLAN.md
# --------------------------------------------------------------------------------------------------------------------
def lade(pfad):
    with open(pfad) as fh:
        return json.load(fh)


def befehl_auswertung(args):
    """Mechanische Urteile nach PLAN.md. Energie je Punkt: E_korr = E + m1 c1 + m2 c2 (Energie am exakten Ort,
    erste Ordnung im Rest der Nebenbedingung)."""
    ordner = args.ordner
    rad = lade(os.path.join(ordner, 'radial.json'))
    ziele = {round(z['Q'], 6): z for z in rad['ergebnisse']['dr=%g' % rad['dr']]['ziele']}
    dateien = sorted(glob.glob(os.path.join(ordner, '*.json')))
    balls = []
    for p in dateien:
        if os.path.basename(p) in ('radial.json', 'auswertung.json'):
            continue
        b = lade(p)
        if b.get('befehl') == 'ball':
            b['datei'] = os.path.basename(p)
            balls.append(b)
    h_fein = args.h_fein
    Q_kraft = args.Q_kraft
    aus = dict(befehl='auswertung', start=jetzt(), h_fein=h_fein, Q_kraft=Q_kraft, dateien=[b['datei'] for b in balls],
               urteile={}, tabellen={}, beschreibend={})

    def EK(p):
        return p['E_korr_erste_ordnung']

    def ein(b, wert=0.0):
        for p in b['punkte']:
            if p['art'] == 'd' and abs(p['d'] - wert) < 1e-9:
                return p
        return None

    # Bezugsenergien (Rolle bindung): flacher Flicken zentriert (n = 6, d = 0), Spitze (n = 5/7, d = 0), fern (d > 0)
    E_flach, E_kegel0, E_fern = {}, {}, {}
    for b in balls:
        if b['rolle'] != 'bindung':
            continue
        key = (b['h'], round(b['Q'], 6), b['R'])
        p0 = ein(b, 0.0)
        if p0 is not None and b['n'] == 6:
            E_flach[key] = EK(p0)
        elif p0 is not None:
            E_kegel0[(b['n'],) + key] = EK(p0)
        for p in b['punkte']:
            if p['art'] == 'd' and p['d'] > 0 and b['n'] != 6:
                E_fern[(b['n'],) + key] = (p['d'], EK(p))
    # KQ0
    kq0 = []
    for b in balls:
        if b['rolle'] != 'kq0':
            continue
        Es = [EK(p) for p in b['punkte']]
        m = float(np.mean(Es))
        kq0.append(dict(h=b['h'], Q=b['Q'], R=b['R'], orte=len(Es), E_mittel=m,
                        schwankung_rel=(max(Es) - min(Es)) / m, E=Es,
                        res_max=max(p['res_max'] for p in b['punkte'])))
    aus['tabellen']['KQ0'] = kq0
    aus['urteile']['KQ0'] = dict(
        eingetroffen=bool(len(kq0) > 0 and all(k['schwankung_rel'] < 1e-4 for k in kq0)),
        regel='(max E - min E)/mittel E < 1e-4 in jeder kq0-Datei (alle h, alle Q)',
        dateien=len(kq0), groesste_schwankung=max((k['schwankung_rel'] for k in kq0), default=None))
    # KQ1 (Fuenfer-Ecke; Siebener-Ecke beschreibend)
    tabB = []
    for (n, h, Q, R), Ek in sorted(E_kegel0.items()):
        if (h, Q, R) not in E_flach or Q not in ziele:
            continue
        z = ziele[Q]
        Ef = E_flach[(h, Q, R)]
        Bl = Ef - Ek
        Bx = z['n%d' % n]['B']
        zeile = dict(n=n, h=h, Q=Q, R=R, E_flach=Ef, E_spitze=Ek, B_gitter=Bl, B_exakt=Bx, rel_abw=(Bl - Bx) / abs(Bx),
                     E_flach_gegen_radial_rel=Ef / z['E'] - 1.0,
                     E_spitze_gegen_exakt_rel=Ek / z['n%d' % n]['E_kegel'] - 1.0)
        if (n, h, Q, R) in E_fern:
            dF, EF = E_fern[(n, h, Q, R)]
            zeile.update(d_fern=dF, E_fern=EF, B_gitter_fern=EF - Ek, E_fern_minus_E_flach=EF - Ef,
                         rel_abw_fern=(EF - Ek - Bx) / abs(Bx))
        tabB.append(zeile)
    aus['tabellen']['B'] = tabB
    k1 = [z for z in tabB if z['n'] == 5 and abs(z['h'] - h_fein) < 1e-12]
    treffer = [z for z in k1 if abs(z['rel_abw']) < 0.05]
    aus['urteile']['KQ1'] = dict(
        eingetroffen=bool(len(treffer) >= 3),
        regel='Fuenfer-Ecke, h_fein: |B_gitter - B_exakt|/|B_exakt| < 0,05 bei mindestens 3 Q '
              '(B_gitter = E_flach(Q) - E_Spitze(Q), beide zentriert auf einer Ecke)',
        treffer=len(treffer), von=len(k1), abw=[[z['Q'], z['rel_abw']] for z in k1])
    # Richardson (beschreibend): je (n, Q) aus den zwei feinsten h, Ansatz h^2
    rich = []
    for n in (5, 7):
        for Q in sorted(set(z['Q'] for z in tabB)):
            zs = sorted([z for z in tabB if z['n'] == n and z['Q'] == Q], key=lambda z: z['h'])
            if len(zs) >= 2:
                h1, h2 = zs[0]['h'], zs[1]['h']
                B1, B2 = zs[0]['B_gitter'], zs[1]['B_gitter']
                B0 = B1 + (B1 - B2) * h1 * h1 / (h2 * h2 - h1 * h1)
                rich.append(dict(n=n, Q=Q, h=[z['h'] for z in zs], B=[z['B_gitter'] for z in zs], B_h0=B0,
                                 B_exakt=zs[0]['B_exakt'], rel_abw_h0=(B0 - zs[0]['B_exakt']) / abs(zs[0]['B_exakt'])))
    aus['beschreibend']['richardson_B'] = rich
    # Kraftgesetz: Punkte aller kraft-Dateien je (n, h, Q, R) zusammenfuehren
    kraft = {}
    for b in balls:
        if b['rolle'] != 'kraft':
            continue
        key = (b['n'], b['h'], round(b['Q'], 6), b['R'])
        kraft.setdefault(key, {})
        for p in b['punkte']:
            if p['art'] == 'd' and round(p['d'], 9) not in kraft[key]:
                kraft[key][round(p['d'], 9)] = p
    tabK, urteil2, urteil3, schwanz, lamprobe = [], {}, {}, [], []
    for (n, h, Q, R), pdict in sorted(kraft.items()):
        pts = [pdict[d] for d in sorted(pdict)]
        z = ziele.get(Q)
        Bx = z['n%d' % n]['B'] if z else None
        Ef = E_flach.get((h, Q, R))
        E0 = EK(pts[0]) if pts and pts[0]['d'] == 0.0 else None
        Bl = (Ef - E0) if (Ef is not None and E0 is not None) else None
        dkq3 = z['R_half'] + 4.0 / z['kappa'] if z else None
        zeilen = []
        for k, p in enumerate(pts):
            zz = dict(d=p['d'], E=EK(p), E_minus_E0=(EK(p) - E0) if E0 is not None else None,
                      E_minus_Eflach=(EK(p) - Ef) if Ef is not None else None,
                      dEdd_lambda=p.get('dEdd_lambda'), d_W=p['d_W'], res_max=p['res_max'], c1=p['c1'],
                      S_spitze=p['S_spitze'])
            if 0 < k < len(pts) - 1:
                zz['dEdd_diff'] = (EK(pts[k + 1]) - EK(pts[k - 1])) / (pts[k + 1]['d'] - pts[k - 1]['d'])
            # Gegenprobe Multiplikator: Trapez der lambda-Kraefte gegen die Energiestufe zum Vorgaenger (d > 0)
            if k >= 2 and p.get('dEdd_lambda') is not None and pts[k - 1].get('dEdd_lambda') is not None:
                stufe = EK(p) - EK(pts[k - 1])
                trapez = 0.5 * (p['dEdd_lambda'] + pts[k - 1]['dEdd_lambda']) * (p['d'] - pts[k - 1]['d'])
                if Bx and abs(stufe) > 1e-3 * abs(Bx):
                    lamprobe.append(dict(n=n, h=h, Q=Q, d_von=pts[k - 1]['d'], d_bis=p['d'], stufe=stufe,
                                         trapez=trapez, rel=(trapez - stufe) / abs(stufe)))
            zeilen.append(zz)
        tabK.append(dict(n=n, h=h, Q=Q, R=R, E_flach=Ef, B_gitter=Bl, B_exakt=Bx, d_KQ3=dkq3, punkte=zeilen))
        # Schwanz (beschreibend): ln|E(d) - E_flach| gegen d fuer d >= R_half + 2/kappa, |dE| > 1e-9
        if Ef is not None and z:
            sp_ = [(p['d'], EK(p) - Ef) for p in pts if p['d'] >= z['R_half'] + 2.0 / z['kappa']
                   and abs(EK(p) - Ef) > 1e-9]
            if len(sp_) >= 3:
                dd = np.array([a for a, _ in sp_])
                ll = np.log(np.abs([b_ for _, b_ in sp_]))
                steig, achse = np.polyfit(dd, ll, 1)
                schwanz.append(dict(n=n, h=h, Q=Q, punkte=len(sp_), d_von=float(dd.min()), d_bis=float(dd.max()),
                                    rate=float(-steig), zwei_kappa=2 * z['kappa'], verhaeltnis=float(-steig / (2 * z['kappa'])),
                                    vorzeichen=[int(np.sign(b_)) for _, b_ in sp_]))
        if abs(Q - Q_kraft) < 1e-9 and abs(h - h_fein) < 1e-12 and E0 is not None and Bx is not None:
            tol = 1e-4 * abs(Bx)
            Es = [EK(p) for p in pts]
            dif = np.diff(Es)
            if n == 5:
                ok = all(e - E0 > 0 for e in Es[1:]) and all(x >= -tol for x in dif)
            else:
                ok = all(e - E0 < 0 for e in Es[1:]) and all(x <= tol for x in dif)
            urteil2[n] = dict(erfuellt=bool(ok), tol=tol, min_stufe=float(dif.min()), max_stufe=float(dif.max()),
                              punkte=len(pts), E_d_minus_E0=[[p['d'], EK(p) - E0] for p in pts[1:]])
            if Ef is not None and Bl is not None:
                weit = [[p['d'], EK(p) - Ef] for p in pts if p['d'] > dkq3]
                ok3 = len(weit) >= 2 and all(abs(x) < 0.01 * abs(Bl) for _, x in weit)
                urteil3[n] = dict(erfuellt=bool(ok3), d_KQ3=dkq3, schranke=0.01 * abs(Bl), punkte=weit,
                                  max_abs=max((abs(x) for _, x in weit), default=None))
    aus['tabellen']['kraft'] = tabK
    aus['beschreibend']['schwanz'] = schwanz
    aus['beschreibend']['lambda_gegen_differenz'] = dict(
        anzahl=len(lamprobe), max_rel=max((abs(x['rel']) for x in lamprobe), default=None), punkte=lamprobe)
    aus['urteile']['KQ2'] = dict(
        eingetroffen=bool(urteil2.get(5, {}).get('erfuellt') and urteil2.get(7, {}).get('erfuellt')),
        regel='h_fein, Q_kraft: n=5 E(d)-E(0) > 0 fuer alle d > 0 und Stufen >= -tol; '
              'n=7 E(d)-E(0) < 0 fuer alle d > 0 und Stufen <= +tol; tol = 1e-4 |B_exakt|',
        je_netz=urteil2)
    aus['urteile']['KQ3'] = dict(
        eingetroffen=bool(urteil3.get(5, {}).get('erfuellt') and urteil3.get(7, {}).get('erfuellt')),
        regel='h_fein, Q_kraft: fuer alle d > R_half + 4/kappa (mind. 2 Punkte) |E(d) - E_flach| < 0,01 |B_gitter|, '
              'je Netz 5 und 7',
        je_netz=urteil3)
    # Gegenproben bei den anderen h (gleiche Regeln, beschreibend)
    gegen = []
    for (n, h, Q, R), pdict in sorted(kraft.items()):
        if abs(Q - Q_kraft) > 1e-9 or abs(h - h_fein) < 1e-12:
            continue
        pts = [pdict[d] for d in sorted(pdict)]
        z = ziele.get(Q)
        Ef = E_flach.get((h, Q, R))
        if not pts or pts[0]['d'] != 0.0 or z is None or Ef is None:
            continue
        E0 = EK(pts[0])
        Es = [EK(p) for p in pts]
        dif = np.diff(Es)
        tol = 1e-4 * abs(z['n%d' % n]['B'])
        ok2 = (all(e - E0 > 0 for e in Es[1:]) and all(x >= -tol for x in dif)) if n == 5 else \
            (all(e - E0 < 0 for e in Es[1:]) and all(x <= tol for x in dif))
        dkq3 = z['R_half'] + 4.0 / z['kappa']
        weit = [EK(p) - Ef for p in pts if p['d'] > dkq3]
        ok3 = len(weit) >= 2 and all(abs(x) < 0.01 * abs(Ef - E0) for x in weit)
        gegen.append(dict(n=n, h=h, Q=Q, KQ2_regel=bool(ok2), KQ3_regel=bool(ok3)))
    aus['beschreibend']['gegenproben_andere_h'] = gegen
    # Randabstand
    rand = []
    for b in balls:
        if b['rolle'] != 'rand':
            continue
        for b2 in balls:
            if b2['rolle'] == 'bindung' and b2['n'] == b['n'] and b2['h'] == b['h'] and \
                    abs(b2['Q'] - b['Q']) < 1e-9 and b2['R'] != b['R']:
                for p in b['punkte']:
                    q = ein(b2, p['d'])
                    if q is not None:
                        rand.append(dict(n=b['n'], h=b['h'], Q=b['Q'], d=p['d'], R_gross=b['R'], R_klein=b2['R'],
                                         dE=EK(p) - EK(q)))
    aus['tabellen']['rand'] = rand
    # dE/dQ auf dem Gitter: Paare der Rolle dEdQ je (n, h)
    dq = {}
    for b in balls:
        if b['rolle'] != 'dEdQ':
            continue
        p = ein(b, 0.0)
        dq.setdefault((b['n'], b['h']), []).append((b['Q'], EK(p), p['omega']))
    dqt = []
    for (n, h), lst in sorted(dq.items()):
        lst.sort()
        if len(lst) == 2:
            (Qa, Ea, oa), (Qb, Eb, ob) = lst
            dEdQ = (Eb - Ea) / (Qb - Qa)
            dqt.append(dict(n=n, h=h, Q_a=Qa, Q_b=Qb, dEdQ=dEdQ, omega_mittel=(oa + ob) / 2,
                            rel_abw=dEdQ / ((oa + ob) / 2) - 1.0))
    aus['tabellen']['dEdQ_gitter'] = dqt
    aus['ende'] = jetzt()
    schreibe_json(os.path.join(ordner, 'auswertung.json'), aus)
    for k, v in aus['urteile'].items():
        print(k, 'eingetroffen' if v['eingetroffen'] else 'NICHT eingetroffen', flush=True)
    print('geschrieben', os.path.join(ordner, 'auswertung.json'))



def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='befehl', required=True)
    a = sub.add_parser('radial')
    a.add_argument('--Q', required=True, help='Zielladungen, Komma-getrennt')
    a.add_argument('--dr', type=float, default=0.01)
    a.add_argument('--rmax', type=float, default=60.0)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('netz')
    a.add_argument('--h', type=float, required=True)
    a.add_argument('--R', type=float, required=True)
    a.add_argument('--aus', default=None)
    a = sub.add_parser('ball')
    a.add_argument('--rolle', required=True, choices=['kq0', 'bindung', 'kraft', 'rand', 'dEdQ', 'rauch'])
    a.add_argument('--n', type=int, required=True, choices=[5, 6, 7])
    a.add_argument('--h', type=float, required=True)
    a.add_argument('--R', type=float, required=True)
    a.add_argument('--Q', required=True, help='Ladung(en), Komma-getrennt; bei mehreren {Q} im Ausgabenamen')
    a.add_argument('--d', default=None, help='Abstaende entlang theta0 = 0, Komma-getrennt')
    a.add_argument('--xy', default=None, help='nur n = 6: Orte "x,y;x,y;..."')
    a.add_argument('--mu', type=float, default=5.0)
    a.add_argument('--tol-c', dest='tol_c', type=float, default=1e-9)
    a.add_argument('--max-aussen', dest='max_aussen', type=int, default=12)
    a.add_argument('--maxiter', type=int, default=40000)
    a.add_argument('--gtol', type=float, default=1e-10)
    a.add_argument('--dr-radial', dest='dr_radial', type=float, default=0.01)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('auswertung')
    a.add_argument('--ordner', required=True)
    a.add_argument('--h-fein', dest='h_fein', type=float, required=True)
    a.add_argument('--Q-kraft', dest='Q_kraft', type=float, required=True)
    args = ap.parse_args()
    try:
        {'radial': befehl_radial, 'netz': befehl_netz, 'ball': befehl_ball, 'auswertung': befehl_auswertung}[
            args.befehl](args)
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
