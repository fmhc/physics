#!/usr/bin/env python3
"""KEGEL-XD-2 (Runde 28, runden-v3, explorativ). Code-Agent fuer die Leitung claude-primary.

Frage der Karte: Ist die 2D-Abweichung der ersten Ordnung (KEGEL-XD, delta = pi/3) hoehere Ordnung (r ~ delta^2) oder
ein Fehler der Herleitung? Dazu ein 2D-Kontinuumskegel in Polarkoordinaten bei delta = +-pi/3, +-pi/6 und +-pi/12.

Modell M1: U(S) = S - S^2 + S^3/2 (beta = 1/2), S = f^2, phi = f exp(-i omega t), f reell, Q = 2 omega Int f^2.
Energie bei festem Q: E[f] = Q^2/(4 Int f^2) + Int |grad f|^2 + Int U(f^2).  g = f'^2 + U(f^2) - omega^2 f^2.
Erste Ordnung (Karte KEGEL-XD): Delta E_1(d) = -delta Int_0^inf r g(d + r) dr = -delta Int_d^inf (rho - d) g drho.

Befehle:
  ziel        Ebenes Radialprofil (Q = 200, dr = 0,01 und 0,005); Delta E_1(d) je delta (pi/3, pi/6, pi/12) an den
              17 Abstaenden 0 bis 19,2, Kraft d(Delta E_1)/dd, Schwanzformel, exakte Kegelabbildung bei d = 0
              (E_eben(sQ)/s - E_eben(Q)) fuer alle sechs Defizite.
  ball2d      2D-Kegel in Polarkoordinaten (r, phi), phi in [0, Theta/2] (Spiegel bei phi = 0 und phi = Theta/2,
              Neumann), Theta = 2 pi - delta mit delta = k pi/12. Winkelweite dphi = pi/(24 m) fuer jedes k (Zellzahl
              (24 - k) m), also gleiche Winkelweite fuer +delta, -delta und den flachen Fall. Dirichlet f = 0 hinter
              r_max (Geisterzelle). FV-Gewichte: Volumen 2 r dr dphi (Faktor 2 fuer den Spiegel).
              Ball bei festem Q und festem harmonischem Schwerpunkt <r^s cos(s phi)>_{f^2 dA} = d^s (s = 2 pi/Theta,
              wie KEGEL-Q/KEGEL-XD), Augmented Lagrangian + L-BFGS-B in vorkonditionierten Variablen
              (Volumen-Skalierung, DCT-II in phi mit Skalierung der phi-Steifigkeit), wie KEGEL-XD.
  auswertung  O, r, P je delta und Gitter; Urteile K2-0 bis K2-2 nach PLAN.md (mechanisch); urteile.json.
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
from scipy.fft import dct, idct
from scipy.linalg import solve_banded
from scipy.optimize import brentq, minimize

PI = math.pi
T_START = time.perf_counter()
OMC2 = 0.5
SIGMA_TW = math.sqrt(2.0) / 4.0
D_LISTE = [round(1.2 * j, 10) for j in range(17)]      # 0; 1,2; ...; 19,2 (KEGEL-Q-Tabelle)
K_BETRAG = (4, 2, 1)                                     # delta = k pi/12: pi/3, pi/6, pi/12


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


def lade(pfad):
    with open(pfad) as fh:
        return json.load(fh)


# --------------------------------------------------------------------------------------------------------------------
# Ebene radiale Familie (FV wie KEGEL-Q/KEGEL-XD, Gewichte r^(n-1))
# --------------------------------------------------------------------------------------------------------------------
class Radial:
    def __init__(self, dr, rmax, n):
        self.dr, self.n = dr, n
        self.M = int(round(rmax / dr))
        j = np.arange(self.M, dtype=float)
        self.r = (j + 0.5) * dr
        self.rp = (j + 1.0) * dr
        self.rm = j * dr
        self.Om = 2 * PI if n == 2 else 4 * PI
        self.wv = self.r ** (n - 1)
        self.wp = self.rp ** (n - 1)
        self.wm = self.rm ** (n - 1)

    def teile(self, f):
        dr = self.dr
        S = f * f
        fp = np.append(f[1:], 0.0)
        I = self.Om * dr * float(np.sum(self.wv * S))
        G = self.Om * float(np.sum(self.wp * (fp - f) ** 2)) / dr
        V = self.Om * dr * float(np.sum(self.wv * U(S)))
        return I, G, V

    def residuum(self, f, om2):
        fm = np.concatenate(([0.0], f[:-1]))
        fp = np.append(f[1:], 0.0)
        S = f * f
        return 2 * (self.wm * (f - fm) - self.wp * (fp - f)) / self.dr + 2 * self.dr * self.wv * (dU(S) - om2) * f

    def rnorm(self, R):
        return float(np.max(np.abs(R / (self.dr * self.wv))))

    def newton(self, f0, om2, tol=1e-11, maxit=80):
        f = f0.copy()
        R = self.residuum(f, om2)
        nr = self.rnorm(R)
        it = 0
        off = -2 * self.wp[:-1] / self.dr
        while nr > tol and it < maxit:
            it += 1
            S = f * f
            ab = np.zeros((3, self.M))
            ab[0, 1:] = off
            ab[1, :] = 2 * (self.wm + self.wp) / self.dr + 2 * self.dr * self.wv * (dU(S) + 2 * S * d2U(S) - om2)
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

        def radius(level):
            if S0 <= level:
                return None
            k = int(np.argmax(S < level))
            return float(self.r[k - 1] + (level - S[k - 1]) * (self.r[k] - self.r[k - 1]) / (S[k] - S[k - 1]))

        return dict(om2=om2, omega=om, Q=2 * om * I, E=om2 * I + G + V, I=I, G=G, V=V, S0=S0,
                    R_half_S0=radius(0.5 * S0), R_halb=radius(0.5), kappa=math.sqrt(1.0 - om2))


def baue_familie(n, dr, rmax, om2_start):
    rad = Radial(dr, rmax, n)
    R0 = (n - 1) * SIGMA_TW / (om2_start - OMC2)
    S = 1.0 / (1.0 + np.exp(np.clip(math.sqrt(2.0) * (rad.r - R0), -700.0, 700.0)))
    f0, it0, nr0 = rad.newton(np.sqrt(S), om2_start)
    if np.max(f0) < 0.05 or nr0 > 1e-8:
        raise RuntimeError('Start der radialen Familie gescheitert: res %.3e max f %.3e' % (nr0, np.max(f0)))
    ab = [round(om2_start - 0.002 * k, 6) for k in range(1, 200) if om2_start - 0.002 * k >= 0.5299]
    auf = [round(om2_start + 0.005 * k, 6) for k in range(1, 200) if om2_start + 0.005 * k <= 0.9001]
    erg = {om2_start: (f0, it0, nr0)}
    for folge in (ab, auf):
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
    return rad, fam


def loese_Q(rad, fam, Qt):
    """Profil mit Ladung Qt auf dem VK-stabilen Ast (erste Klammer von kleinem omega^2 her, Q faellt)."""
    a = None
    for k in range(len(fam) - 1):
        Qa, Qb = fam[k][0]['Q'], fam[k + 1][0]['Q']
        if (Qa - Qt) * (Qb - Qt) <= 0 and Qb < Qa:
            a = k
            break
    if a is None:
        raise RuntimeError('Ladung %.6f nicht im stabilen Ast' % Qt)
    ref = [fam[a][1]]

    def F(om2):
        f, it, nr = rad.newton(ref[0], om2)
        ref[0] = f
        return rad.groessen(f, om2)['Q'] - Qt

    om2 = brentq(F, fam[a][0]['om2'], fam[a + 1][0]['om2'], xtol=1e-16, rtol=1e-15, maxiter=200)
    f, it, nr = rad.newton(ref[0], om2)
    g = rad.groessen(f, om2)
    g['res'] = nr
    return g, f


# --------------------------------------------------------------------------------------------------------------------
# Erste Ordnung der Karte aus dem ebenen 2D-Profil (wie KEGEL-XD Teil A, diskret konsistent mit der FV-Energie)
# --------------------------------------------------------------------------------------------------------------------
def J_pro_delta(rad, f, om2, d):
    """Delta E_1(d)/delta = -Int_d^inf (rho - d) g drho; g = f'^2 (Flaechen rp) + U - om2 f^2 (Zellmitten r)."""
    S = f * f
    fp = np.append(f[1:], 0.0)
    gG = (fp - f) ** 2 / rad.dr ** 2
    gV = U(S) - om2 * S
    return -(float(np.sum(np.maximum(rad.rp - d, 0.0) * gG)) + float(np.sum(np.maximum(rad.r - d, 0.0) * gV))) * rad.dr


def kraft_pro_delta(rad, f, om2, d):
    """d(Delta E_1)/dd / delta = Int_d^inf g drho."""
    S = f * f
    fp = np.append(f[1:], 0.0)
    gG = (fp - f) ** 2 / rad.dr ** 2
    gV = U(S) - om2 * S
    return (float(np.sum((rad.rp > d) * gG)) + float(np.sum((rad.r > d) * gV))) * rad.dr


def impulsfluss(rad, f, om2):
    """Probe der Karte (2D): Int_0^inf g drho = 0."""
    S = f * f
    fp = np.append(f[1:], 0.0)
    gG = (fp - f) ** 2 / rad.dr ** 2
    gV = U(S) - om2 * S
    a = float(np.sum(gG) + np.sum(gV)) * rad.dr
    b = float(np.sum(np.abs(gG)) + np.sum(np.abs(gV))) * rad.dr
    return dict(integral=a, betrag=b, rel=a / b)


def befehl_ziel(args):
    Q = args.Q
    aus = dict(befehl='ziel', start=jetzt(), Q=Q, d_liste=D_LISTE, profile={},
               hinweis='Delta E_1(d; delta) = delta * J(d), J = -Int_d^inf (rho - d) g drho; fuer -delta das '
                       'Negative. Zielwerte der Karte KEGEL-XD-2; versiegelt vor den echten Laeufen.')
    for dr in (args.dr, args.dr / 2):
        rad, fam = baue_familie(2, dr, args.rmax, 0.62)
        g, f = loese_Q(rad, fam, Q)
        J = [J_pro_delta(rad, f, g['om2'], d) for d in D_LISTE]
        Kr = [kraft_pro_delta(rad, f, g['om2'], d) for d in D_LISTE]
        Sd = [float(np.interp(d, rad.r, f * f, right=0.0)) for d in D_LISTE]
        deltas = {}
        for k in K_BETRAG:
            delta = k * PI / 12.0
            deltas['k=%d' % k] = dict(
                k=k, delta=delta,
                zeilen=[dict(d=d, dE1=delta * J[i], dE1_kraft=delta * Kr[i], schwanz=-0.5 * delta * Sd[i])
                        for i, d in enumerate(D_LISTE)])
        keil = {}
        for k in (4, -4, 2, -2, 1, -1):
            Theta = 2 * PI - k * PI / 12.0
            s = 2 * PI / Theta
            gs, fs = loese_Q(rad, fam, s * Q)
            keil['k=%d' % k] = dict(k=k, Theta=Theta, s=s, E_eben_sQ=gs['E'], E_kegel=gs['E'] / s,
                                    dE_exakt=gs['E'] / s - g['E'], omega_sQ=gs['omega'])
        for k in K_BETRAG:
            O0 = 0.5 * (keil['k=%d' % k]['dE_exakt'] - keil['k=%d' % (-k)]['dE_exakt'])
            dE10 = deltas['k=%d' % k]['zeilen'][0]['dE1']
            keil['O0_k=%d' % k] = dict(O_exakt_d0=O0, dE1_0=dE10, r_exakt_d0=(O0 - dE10) / abs(dE10))
        aus['profile']['dr=%g' % dr] = dict(
            om2=g['om2'], omega=g['omega'], E=g['E'], I=g['I'], G=g['G'], V=g['V'], S0=g['S0'], R_halb=g['R_halb'],
            R_half_S0=g['R_half_S0'], kappa=g['kappa'], res=g['res'], F=g['E'] - g['omega'] * Q,
            J=J, J_kraft=Kr, S_eben=Sd, deltas=deltas, keil=keil, impulsfluss=impulsfluss(rad, f, g['om2']))
        print('dr %g: om2 %.10f E %.8f R_halb %.4f kappa %.5f F %.6f' % (
            dr, g['om2'], g['E'], g['R_halb'], g['kappa'], g['E'] - g['omega'] * Q), flush=True)
    aus['ende'] = jetzt()
    schreibe_json(args.aus, aus)
    print('geschrieben', args.aus)


# --------------------------------------------------------------------------------------------------------------------
# 2D-Kegel in Polarkoordinaten
# --------------------------------------------------------------------------------------------------------------------
class Zeitende(Exception):
    pass


class Kegel2D:
    """Zellen (j, l): r_j = (j + 1/2) dr, phi_l = (l + 1/2) dphi, dphi = pi/(24 m), Np = (24 - k) m Zellen in
    phi in [0, Theta/2], Theta = 2 Np dphi = 2 pi - k pi/12. Spiegel bei phi = 0 und Theta/2 (Neumann), Faktor 2 in
    allen Gewichten. Dirichlet f = 0 in der Geisterzelle hinter r_max."""

    def __init__(self, dr, rmax, m, k):
        if not (-23 <= k <= 23):
            raise RuntimeError('k ausserhalb')
        self.dr, self.m, self.k = dr, m, k
        self.Np = (24 - k) * m
        self.dphi = PI / (24.0 * m)
        self.Theta = 2.0 * self.Np * self.dphi
        self.delta = 2 * PI - self.Theta
        self.Nr = int(round(rmax / dr))
        self.rmax = self.Nr * dr
        self.r = (np.arange(self.Nr) + 0.5) * dr
        self.phi = (np.arange(self.Np) + 0.5) * self.dphi
        rf = np.arange(1, self.Nr + 1) * dr
        self.w = 2.0 * self.r * dr * self.dphi
        self.cr = 2.0 * rf * self.dphi / dr
        self.cp = 2.0 * dr / (self.r * self.dphi)
        self.s = 2 * PI / self.Theta
        self.u = (self.r[:, None] ** self.s) * np.cos(self.s * self.phi[None, :])   # (Nr, Np)
        mu = 2.0 - 2.0 * np.cos(PI * np.arange(self.Np) / self.Np)
        c0 = 4.0 / (dr * dr)
        th = mu[None, :] / (self.r[:, None] * self.dphi) ** 2
        self.Dm = 1.0 / np.sqrt(1.0 + th / c0)                                      # (Nr, Np)
        self.Wi = (1.0 / np.sqrt(self.w))[:, None]
        self.Ws = np.sqrt(self.w)[:, None]
        self.shape = (self.Nr, self.Np)

    def abstand(self, d):
        """Geodaetischer Abstand jeder Zelle vom Punkt (r = d, phi = 0)."""
        P = self.phi[None, :]
        R = self.r[:, None]
        return np.where(P < PI, np.sqrt(np.maximum(R * R + d * d - 2 * R * d * np.cos(P), 0.0)), R + d)

    def nach_f(self, y):
        return self.Wi * idct(self.Dm * y, type=2, axis=1, norm='ortho')

    def nach_y(self, f):
        return dct(self.Ws * f, type=2, axis=1, norm='ortho') / self.Dm

    def grad_y(self, gf):
        return self.Dm * dct(self.Wi * gf, type=2, axis=1, norm='ortho')

    def teile(self, f):
        S = f * f
        I = float(self.w @ S.sum(axis=1))
        V = float(self.w @ U(S).sum(axis=1))
        gG = np.zeros_like(f)
        df = f[1:] - f[:-1]
        t = self.cr[:-1, None] * df
        G = float(np.sum(t * df))
        gG[:-1] -= 2 * t
        gG[1:] += 2 * t
        G += self.cr[-1] * float(np.sum(f[-1] * f[-1]))
        gG[-1] += 2 * self.cr[-1] * f[-1]
        if self.Np > 1:
            df = f[:, 1:] - f[:, :-1]
            t = self.cp[:, None] * df
            G += float(np.sum(t * df))
            gG[:, :-1] -= 2 * t
            gG[:, 1:] += 2 * t
        return S, I, G, V, gG


def loese_kegel(K, Q, D, f0, mu, tol_c, max_aussen, maxiter, deadline, maxcor):
    w2 = K.w[:, None]
    gu = K.u - D
    N0 = float(K.w @ (f0 * f0).sum(axis=1))
    lam = 0.0
    zaehler = dict(nfev=0)
    best = dict(LA=None, y=None)

    def werte(f):
        S, I, G, V, gG = K.teile(f)
        c = float(K.w @ (S * gu).sum(axis=1)) / N0
        return S, I, G, V, gG, c

    def fun(yv):
        if time.perf_counter() > deadline:
            raise Zeitende()
        zaehler['nfev'] += 1
        y = yv.reshape(K.shape)
        f = K.nach_f(y)
        S, I, G, V, gG, c = werte(f)
        E = Q * Q / (4 * I) + G + V
        om2 = Q * Q / (4 * I * I)
        m = lam + mu * c
        LA = E + lam * c + 0.5 * mu * c * c
        gf = gG + 2 * w2 * f * (dU(S) - om2 + m * gu / N0)
        if best['LA'] is None or LA < best['LA']:
            best['LA'] = LA
            best['y'] = yv.copy()
        return LA, K.grad_y(gf).ravel()

    y = K.nach_y(f0).ravel()
    verlauf = []
    nit = 0
    E_alt = None
    abgebrochen = False
    for aussen in range(max_aussen):
        best['LA'] = None
        try:
            res = minimize(fun, y, jac=True, method='L-BFGS-B',
                           options=dict(maxiter=maxiter, maxcor=maxcor, ftol=1e-16, gtol=1e-12, maxls=60))
            y = res.x
            nit += int(res.nit)
            msg = str(res.message)[:60]
        except Zeitende:
            y = best['y'] if best['y'] is not None else y
            abgebrochen = True
            msg = 'Zeitende'
        f = K.nach_f(y.reshape(K.shape))
        S, I, G, V, gG, c = werte(f)
        E = Q * Q / (4 * I) + G + V
        lam = lam + mu * c
        verlauf.append(dict(aussen=aussen, E=E, c=c, lam=lam, msg=msg, nfev=zaehler['nfev'],
                            t=time.perf_counter() - T_START))
        print('   aussen %d: E %.12f c %.2e lam %.4e nfev %d %s (%.1f s)' % (
            aussen, E, c, lam, zaehler['nfev'], msg, time.perf_counter() - T_START), flush=True)
        if abgebrochen:
            break
        fertig = abs(c) < tol_c and E_alt is not None and abs(E - E_alt) < 1e-12 * abs(E)
        E_alt = E
        if fertig:
            break
    om2 = Q * Q / (4 * I * I)
    m = lam
    gE = gG + 2 * w2 * f * (dU(S) - om2)
    gL = gE + 2 * w2 * f * m * gu / N0
    return dict(E=E, I=I, G=G, V=V, omega=math.sqrt(om2), c=c, m=m, N=I, N0=N0,
                res_max=float(np.max(np.abs(gL / (2 * w2)))), res_E_ohne_m=float(np.max(np.abs(gE / (2 * w2)))),
                aussen=len(verlauf), nit=nit, nfev=zaehler['nfev'], abgebrochen=abgebrochen, verlauf=verlauf), f


def befehl_ball2d(args):
    deadline = T_START + args.tmax
    K = Kegel2D(args.dr, args.rmax, args.m, args.k)
    rad, fam = baue_familie(2, args.dr_radial, 60.0, 0.62)
    gQ, fQ = loese_Q(rad, fam, args.Q)
    gsQ, fsQ = loese_Q(rad, fam, K.s * args.Q) if args.k != 0 else (gQ, fQ)
    aus = dict(befehl='ball2d', rolle=args.rolle, start=jetzt(), k=args.k, delta=K.delta, Theta=K.Theta, s=K.s,
               dr=args.dr, m=args.m, rmax=K.rmax, Nr=K.Nr, Np=K.Np, dphi=K.dphi, zellen=K.Nr * K.Np, Q=args.Q,
               mu=args.mu, maxcor=args.maxcor, tmax=args.tmax,
               radial=dict(omega_Q=gQ['omega'], E_eben_Q=gQ['E'], R_halb_Q=gQ['R_halb'], kappa_Q=gQ['kappa'],
                           omega_sQ=gsQ['omega'], E_eben_sQ=gsQ['E'], E_kegel_exakt=gsQ['E'] / K.s),
               punkte=[])
    print('Kegel k %+d delta %+.6f Theta %.6f s %.6f dr %g m %d Nr %d Np %d (%d Zellen), dphi %.8f' % (
        args.k, K.delta, K.Theta, K.s, args.dr, args.m, K.Nr, K.Np, K.Nr * K.Np, K.dphi), flush=True)
    for d in [float(x) for x in args.d.split(',')]:
        t0 = time.perf_counter()
        prof = fsQ if d == 0.0 else fQ
        f0 = np.interp(K.abstand(d), rad.r, prof, right=0.0)
        D = d ** K.s
        r, f = loese_kegel(K, args.Q, D, f0, args.mu, args.tol_c, args.max_aussen, args.maxiter, deadline,
                           args.maxcor)
        S = f * f
        Nn = float(K.w @ S.sum(axis=1))
        W = float(K.w @ (S * K.u).sum(axis=1)) / Nn
        p = dict(d=d, D=D)
        p.update({kk: v for kk, v in r.items() if kk != 'verlauf'})
        p['W'] = W
        p['d_W'] = abs(W) ** (1.0 / K.s) * (1 if W >= 0 else -1)
        p['E_korr'] = r['E'] + r['m'] * r['c']
        p['dEdD_lambda'] = -r['m'] * Nn / r['N0']
        p['dEdd_lambda'] = (p['dEdD_lambda'] * K.s * d ** (K.s - 1.0)) if d > 0 else 0.0
        p['S_spitze'] = float(np.mean(S[0, :]))
        p['f_max'] = float(f.max())
        p['f_min'] = float(f.min())
        p['f_rand_r'] = float(np.max(np.abs(f[-1])))
        p['verlauf'] = r['verlauf']
        p['dauer_s'] = time.perf_counter() - t0
        aus['punkte'].append(p)
        aus['zwischenstand'] = jetzt()
        schreibe_json(args.aus, aus)
        print('d %.4f: E %.12f E_korr %.12f c %.1e m %.3e res %.1e d_W %.6f nfev %d abgebr %s (%.1f s)' % (
            d, r['E'], p['E_korr'], r['c'], r['m'], r['res_max'], p['d_W'], r['nfev'], r['abgebrochen'], p['dauer_s']),
            flush=True)
        if r['abgebrochen']:
            break
    aus['ende'] = jetzt()
    aus['dauer_s'] = time.perf_counter() - T_START
    schreibe_json(args.aus, aus)
    print('geschrieben', args.aus, 'Dauer %.1f s' % aus['dauer_s'])


# --------------------------------------------------------------------------------------------------------------------
# Auswertung (mechanisch nach PLAN.md)
# --------------------------------------------------------------------------------------------------------------------
def befehl_auswertung(args):
    ordner = args.ordner
    zi = lade(args.ziel)
    Z = zi['profile']['dr=%g' % args.dr_ziel]
    Z2 = zi['profile']['dr=%g' % (args.dr_ziel / 2)]
    dE1 = {}
    for kk in K_BETRAG:
        for z in Z['deltas']['k=%d' % kk]['zeilen']:
            dE1[(kk, round(z['d'], 6))] = z
    dE1_0 = {kk: dE1[(kk, 0.0)]['dE1'] for kk in K_BETRAG}
    # KEGEL-Q (h = 0,2): ungerader Teil
    EK5, EK7, quellen = {}, {}, []
    for n, Ed in ((5, EK5), (7, EK7)):
        for teil in ('a', 'b'):
            p = os.path.join(args.kq_ordner, 'kraft-n%d-h0.2-Q200-%s.json' % (n, teil))
            b = lade(p)
            quellen.append(os.path.basename(p))
            assert b['n'] == n and abs(b['h'] - 0.2) < 1e-12 and abs(b['Q'] - 200.0) < 1e-9 and b['R'] == 40.0
            for q in b['punkte']:
                Ed[round(q['d'], 6)] = q['E_korr_erste_ordnung']
    O_KQ = {d: 0.5 * (EK5[d] - EK7[d]) for d in sorted(set(EK5) & set(EK7))}
    # Kegel-Laeufe
    gitter = {'fein': (args.dr_fein, args.m_fein), 'grob': (args.dr_grob, args.m_grob)}

    def gname(b):
        for name, (dr, m) in gitter.items():
            if abs(b['dr'] - dr) < 1e-12 and b['m'] == m:
                return name
        return None

    E, info, E_rand, doppelt = {}, {}, {}, []
    dateien = []
    for p in sorted(glob.glob(os.path.join(ordner, 'b2-*.json'))):
        b = lade(p)
        if b.get('befehl') != 'ball2d':
            continue
        dateien.append(os.path.basename(p))
        g = gname(b)
        if g is None:
            continue
        for q in b['punkte']:
            d = round(q['d'], 6)
            if abs(b['rmax'] - args.rmax) > 1e-9:
                E_rand[(b['k'], g, d, b['rmax'])] = q['E_korr']
                continue
            key = (b['k'], g, d)
            if key in E:
                doppelt.append([b['k'], g, d, os.path.basename(p)])
                continue
            E[key] = q['E_korr']
            info[key] = dict(datei=os.path.basename(p), res_max=q['res_max'], c=q['c'], abgebrochen=q['abgebrochen'],
                             nfev=q['nfev'], dauer_s=q['dauer_s'], d_W=q['d_W'], S_spitze=q['S_spitze'],
                             f_rand_r=q['f_rand_r'], dEdd_lambda=q['dEdd_lambda'], zellen=b['zellen'])
    aus = dict(befehl='auswertung', start=jetzt(), ziel=os.path.basename(args.ziel), dr_ziel=args.dr_ziel,
               gitter=gitter, rmax=args.rmax, kq_quellen=quellen, dateien=dateien, doppelt=doppelt,
               urteile={}, tabellen={}, beschreibend={}, kontrollen={})
    q2 = (args.dr_grob / args.dr_fein) ** 2
    tab = {}
    for kk in K_BETRAG:
        zeilen = []
        for d in [round(x, 6) for x in D_LISTE]:
            z = dE1[(kk, d)]
            row = dict(d=d, dE1=z['dE1'], dE1_dr_halb=[y for y in Z2['deltas']['k=%d' % kk]['zeilen']
                                                         if abs(y['d'] - d) < 1e-9][0]['dE1'],
                       dE1_kraft=z['dE1_kraft'], schwanz=z['schwanz'])
            for g in ('fein', 'grob'):
                kp, km, k0 = (kk, g, d), (-kk, g, d), (0, g, d)
                if kp in E and km in E:
                    O = 0.5 * (E[kp] - E[km])
                    row['O_' + g] = O
                    row['r_' + g] = (O - z['dE1']) / abs(dE1_0[kk])
                    row['O_durch_dE1_' + g] = O / z['dE1'] if z['dE1'] != 0 else None
                    row['abgebrochen_' + g] = bool(info[kp]['abgebrochen'] or info[km]['abgebrochen'])
                    if info[kp]['dEdd_lambda'] is not None and info[km]['dEdd_lambda'] is not None:
                        row['kraft_odd_' + g] = 0.5 * (info[kp]['dEdd_lambda'] - info[km]['dEdd_lambda'])
                    if k0 in E:
                        row['P_' + g] = 0.5 * (E[kp] + E[km]) - E[k0]
                        row['E_flach_' + g] = E[k0]
            if 'O_fein' in row and 'O_grob' in row:
                row['O_rich'] = row['O_fein'] + (row['O_fein'] - row['O_grob']) / (q2 - 1.0)
                row['r_rich'] = (row['O_rich'] - z['dE1']) / abs(dE1_0[kk])
            if kk == 4 and d in O_KQ:
                row['O_KQ'] = O_KQ[d]
                row['r_KQ'] = (O_KQ[d] - z['dE1']) / abs(dE1_0[kk])
                if 'O_fein' in row:
                    row['O_fein_minus_O_KQ'] = row['O_fein'] - O_KQ[d]
            zeilen.append(row)
        tab['k=%d' % kk] = zeilen
    aus['tabellen'] = tab

    def rmax_von(kk, key):
        rows = tab['k=%d' % kk]
        if any(key not in r for r in rows):
            return None, None, None
        werte = [abs(r[key]) for r in rows]
        i = int(np.argmax(werte))
        return max(werte), rows[i]['d'], rows[i][key]

    # K2-0
    rows4 = tab['k=4']
    schranke0 = 0.003 * abs(dE1_0[4])
    if all('O_fein' in r and 'O_KQ' in r for r in rows4):
        abw = [abs(r['O_fein_minus_O_KQ']) for r in rows4]
        aus['urteile']['K2-0'] = dict(
            eingetroffen=bool(all(a <= schranke0 for a in abw)), schranke=schranke0, dE1_0=dE1_0[4],
            max_abw=max(abw), d_max_abw=rows4[int(np.argmax(abw))]['d'], punkte=len(abw),
            abgebrochene_punkte=[r['d'] for r in rows4 if r.get('abgebrochen_fein')],
            regel='delta = pi/3, feines Gitter: |O_kont(d) - O_KQ(d)| <= 0,003 |Delta E_1(0)| an allen 17 d '
                  '(O_KQ aus KEGEL-Q h = 0,2, E_korr_erste_ordnung)')
    else:
        aus['urteile']['K2-0'] = dict(eingetroffen=None, grund='Punkte fehlen')
    # K2-1, K2-2
    m6, d6, r6 = rmax_von(2, 'r_fein')
    m12, d12, r12 = rmax_von(1, 'r_fein')
    m3, d3, r3 = rmax_von(4, 'r_fein')
    if m6 is not None:
        aus['urteile']['K2-1'] = dict(eingetroffen=bool(0.006 <= m6 <= 0.016), max_r=m6, d_max=d6, r_dort=r6,
                                      abgebrochene_punkte=[r['d'] for r in tab['k=2'] if r.get('abgebrochen_fein')],
                                      regel='delta = pi/6, feines Gitter: 0,006 <= max_d |r| <= 0,016 (17 d)')
    else:
        aus['urteile']['K2-1'] = dict(eingetroffen=None, grund='Punkte fehlen')
    if m12 is not None and m6 is not None:
        verh = m6 / m12 if m12 > 0 else None
        ok = bool(0.0015 <= m12 <= 0.0045 and verh is not None and 3.0 <= verh <= 5.5)
        aus['urteile']['K2-2'] = dict(eingetroffen=ok, max_r=m12, d_max=d12, r_dort=r12, verhaeltnis_6_12=verh,
                                      teil_bereich=bool(0.0015 <= m12 <= 0.0045),
                                      teil_verhaeltnis=bool(verh is not None and 3.0 <= verh <= 5.5),
                                      abgebrochene_punkte=[r['d'] for r in tab['k=1'] if r.get('abgebrochen_fein')],
                                      regel='delta = pi/12, feines Gitter: 0,0015 <= max_d |r| <= 0,0045 und '
                                            '3 <= max|r(pi/6)|/max|r(pi/12)| <= 5,5')
    else:
        aus['urteile']['K2-2'] = dict(eingetroffen=None, grund='Punkte fehlen')
    # Fall der Karte (mechanisch)
    k21 = aus['urteile']['K2-1'].get('eingetroffen')
    k22 = aus['urteile']['K2-2'].get('eingetroffen')
    if k21 and k22:
        fall = 'A: K2-1 und K2-2 eingetroffen'
    elif m12 is not None and m12 > 0.02:
        fall = 'B: max|r(pi/12)| > 2 %'
    elif k21 is None or k22 is None:
        fall = 'nicht entscheidbar'
    else:
        fall = 'dazwischen: beschreiben'
    aus['urteile']['fall_der_karte'] = fall
    # Beschreibend: Skalierung
    sk = []
    for i, d in enumerate([round(x, 6) for x in D_LISTE]):
        e = dict(d=d)
        for key in ('r_fein', 'r_rich', 'r_grob'):
            v = [tab['k=%d' % kk][i].get(key) for kk in K_BETRAG]
            e[key] = v
            if None not in v:
                e[key + '_durch_delta2'] = [v[j] / (K_BETRAG[j] / 4.0) ** 2 for j in range(3)]
                e[key + '_verh_3_6'] = v[0] / v[1] if v[1] != 0 else None
                e[key + '_verh_6_12'] = v[1] / v[2] if v[2] != 0 else None
        sk.append(e)
    aus['beschreibend']['skalierung'] = sk
    aus['beschreibend']['max_r'] = {
        'k=%d' % kk: dict(zip(('fein', 'rich', 'grob', 'KQ'),
                              [rmax_von(kk, key) for key in ('r_fein', 'r_rich', 'r_grob', 'r_KQ')]))
        for kk in K_BETRAG}
    # Kontrollen: d = 0 gegen exakte Kegelabbildung
    k0c = []
    for k in (4, -4, 2, -2, 1, -1):
        ex = Z['keil']['k=%d' % k]['dE_exakt']
        for g in ('fein', 'grob'):
            if (k, g, 0.0) in E and (0, g, 0.0) in E:
                dEg = E[(k, g, 0.0)] - E[(0, g, 0.0)]
                k0c.append(dict(k=k, gitter=g, dE_gitter=dEg, dE_exakt=ex, rel_abw=(dEg - ex) / abs(ex)))
    aus['kontrollen']['d0_kegelabbildung'] = k0c
    aus['kontrollen']['r_exakt_d0'] = {('k=%d' % kk): Z['keil']['O0_k=%d' % kk] for kk in K_BETRAG}
    # Flache Laeufe: Ortsabhaengigkeit (Scheinkraft des Polargitters)
    fl = {}
    for g in ('fein', 'grob'):
        Es = [(d, E[(0, g, round(d, 6))]) for d in D_LISTE if (0, g, round(d, 6)) in E]
        if Es:
            vals = [e for _, e in Es]
            fl[g] = dict(E=Es, spanne=max(vals) - min(vals), E_radial_Q=None)
    aus['kontrollen']['flach'] = fl
    # Randprobe
    rp = []
    for (k, g, d, rm), v in sorted(E_rand.items()):
        if k <= 0 or (-k, g, d, rm) not in E_rand:
            continue
        Og = 0.5 * (v - E_rand[(-k, g, d, rm)])
        if (k, g, d) in E and (-k, g, d) in E:
            Oh = 0.5 * (E[(k, g, d)] - E[(-k, g, d)])
            rp.append(dict(k=k, gitter=g, d=d, rmax_gross=rm, O_gross=Og, O_haupt=Oh, dO=Og - Oh,
                           dO_rel_zu_dE1_0=(Og - Oh) / abs(dE1_0[abs(k)]),
                           dE_plus=v - E[(k, g, d)], dE_minus=E_rand[(-k, g, d, rm)] - E[(-k, g, d)]))
    aus['kontrollen']['randprobe'] = rp
    # Konvergenz
    if info:
        aus['kontrollen']['konvergenz'] = dict(
            punkte=len(info), res_max=max(v['res_max'] for v in info.values()),
            c_max=max(abs(v['c']) for v in info.values()),
            d_W_abw_max=max(abs(v['d_W'] - key[2]) for key, v in info.items()),
            abgebrochen=[list(key) for key, v in info.items() if v['abgebrochen']],
            nfev_max=max(v['nfev'] for v in info.values()), dauer_max_s=max(v['dauer_s'] for v in info.values()),
            f_rand_max=max(v['f_rand_r'] for v in info.values()))
    aus['kontrollen']['ziel_profil'] = dict(
        dr=args.dr_ziel, R_halb=Z['R_halb'], kappa=Z['kappa'], omega=Z['omega'], E=Z['E'], F=Z['F'],
        impulsfluss=Z['impulsfluss'],
        dE1_dr_probe_max=max(abs(r['dE1'] - r['dE1_dr_halb']) for kk in K_BETRAG for r in tab['k=%d' % kk]))
    aus['ende'] = jetzt()
    schreibe_json(os.path.join(ordner, 'auswertung.json'), aus)
    kurz = {k: (v.get('eingetroffen') if isinstance(v, dict) else v) for k, v in aus['urteile'].items()}
    schreibe_json(os.path.join(ordner, 'urteile.json'), dict(stand=jetzt(), urteile=kurz, details=aus['urteile']))
    for k, v in sorted(kurz.items()):
        print(k, v)
    print('geschrieben', os.path.join(ordner, 'auswertung.json'))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='befehl', required=True)
    a = sub.add_parser('ziel')
    a.add_argument('--Q', type=float, default=200.0)
    a.add_argument('--dr', type=float, default=0.01)
    a.add_argument('--rmax', type=float, default=60.0)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('ball2d')
    a.add_argument('--rolle', required=True)
    a.add_argument('--k', type=int, required=True, help='delta = k pi/12')
    a.add_argument('--dr', type=float, required=True)
    a.add_argument('--m', type=int, required=True, help='dphi = pi/(24 m)')
    a.add_argument('--rmax', type=float, required=True)
    a.add_argument('--Q', type=float, required=True)
    a.add_argument('--d', required=True)
    a.add_argument('--mu', type=float, default=5.0)
    a.add_argument('--tol-c', dest='tol_c', type=float, default=1e-9)
    a.add_argument('--max-aussen', dest='max_aussen', type=int, default=8)
    a.add_argument('--maxiter', type=int, default=20000)
    a.add_argument('--maxcor', type=int, default=12)
    a.add_argument('--tmax', type=float, default=560.0)
    a.add_argument('--dr-radial', dest='dr_radial', type=float, default=0.01)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('auswertung')
    a.add_argument('--ordner', required=True)
    a.add_argument('--ziel', required=True)
    a.add_argument('--kq-ordner', dest='kq_ordner', required=True)
    a.add_argument('--dr-ziel', dest='dr_ziel', type=float, default=0.01)
    a.add_argument('--dr-fein', dest='dr_fein', type=float, required=True)
    a.add_argument('--m-fein', dest='m_fein', type=int, required=True)
    a.add_argument('--dr-grob', dest='dr_grob', type=float, required=True)
    a.add_argument('--m-grob', dest='m_grob', type=int, required=True)
    a.add_argument('--rmax', type=float, required=True)
    args = ap.parse_args()
    try:
        {'ziel': befehl_ziel, 'ball2d': befehl_ball2d, 'auswertung': befehl_auswertung}[args.befehl](args)
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
