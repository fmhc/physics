#!/usr/bin/env python3
"""KEGEL-XD (Runde 27, runden-v3, explorativ). Code-Agent fuer die Leitung claude-primary.

Modell M1: U(S) = S - S^2 + S^3/2 (beta = 1/2), S = f^2, phi = f exp(-i omega t), f reell, Q = 2 omega Int f^2.
Energie bei festem Q: E[f] = Q^2/(4 Int f^2) + Int |grad f|^2 + Int U(f^2).  g = f'^2 + U(f^2) - omega^2 f^2.

Befehle:
  teil_a      2D: ebenes Radialprofil bei Q = 200; Delta E_1(d) = -delta Int_0^inf r g(d + r) dr (delta = pi/3);
              Vergleich mit den KEGEL-Q-Daten (h = 0,2): O(d), P(d); Urteile KX1 und KX3 (2D-Teil).
  ziel        3D: ebene radiale Familie, omega^2 mit R_halb(S = 1/2) = 5,00, Ladung Q, Zielwerte Delta E_1(d) und
              Schwanzformel fuer delta = 0,1284, exakte Keilabbildung E_flach(sQ)/s - E_flach(Q) (KX0).
  ball3d      3D-Keil um die z-Achse in Zylinderkoordinaten (r, phi, z) mit phi in [0, Theta/2] und z >= 0
              (Spiegelflaechen, Neumann), Dirichlet f = 0 hinter r_max und z_max. Ball bei festem Q und festem
              harmonischem Schwerpunkt <r^s cos(s phi)> = d^s (s = 2 pi/Theta), Augmented Lagrangian + L-BFGS-B in
              vorkonditionierten Variablen (Volumen-Skalierung, DCT-II in phi mit Skalierung der phi-Steifigkeit).
              Bei nphi = 1 ist die Rechnung achsensymmetrisch ((r, z)-Rechnung, d = 0, ohne Nebenbedingung).
  auswertung  Urteile KX0, KX2, KX3 nach PLAN.md (mechanisch), urteile.json.
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
# Ebene radiale Familie in n = 2 oder 3 Dimensionen (FV, wie KEGEL-Q, Gewichte r^(n-1))
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


def loese_Rhalb(rad, fam, Rziel):
    """omega^2 mit R_halb(S = 1/2) = Rziel (R_halb faellt mit omega^2 auf dem duennwandigen Ast)."""
    a = None
    for k in range(len(fam) - 1):
        Ra, Rb = fam[k][0]['R_halb'], fam[k + 1][0]['R_halb']
        if Ra is not None and Rb is not None and (Ra - Rziel) * (Rb - Rziel) <= 0:
            a = k
            break
    if a is None:
        raise RuntimeError('R_halb %.4f nicht in der Familie' % Rziel)
    ref = [fam[a][1]]

    def F(om2):
        f, it, nr = rad.newton(ref[0], om2)
        ref[0] = f
        return rad.groessen(f, om2)['R_halb'] - Rziel

    om2 = brentq(F, fam[a][0]['om2'], fam[a + 1][0]['om2'], xtol=1e-15, rtol=1e-14, maxiter=200)
    f, it, nr = rad.newton(ref[0], om2)
    g = rad.groessen(f, om2)
    g['res'] = nr
    return g, f


# --------------------------------------------------------------------------------------------------------------------
# Erste Ordnung der Karte: Delta E_1(d) aus dem ebenen Profil (diskret konsistent mit der FV-Energie)
# --------------------------------------------------------------------------------------------------------------------
def kern(n, rho, d):
    """2D: (rho - d)_+ ; 3D: 2 rho K(rho, d), K = sqrt(rho^2 - d^2) - d arccos(d/rho) fuer rho > d.
    3D: Int dz Int_0^inf r g(sqrt((d + r)^2 + z^2)) dr = Int_d^inf 2 rho K(rho, d) g(rho) drho (Polarkoordinaten in
    der Halbebene x > d)."""
    rho = np.asarray(rho, dtype=float)
    if n == 2:
        return np.maximum(rho - d, 0.0)
    out = np.zeros_like(rho)
    m = rho > d
    if d == 0.0:
        out[m] = 2 * rho[m] * rho[m]
    else:
        x = rho[m]
        out[m] = 2 * x * (np.sqrt(x * x - d * d) - d * np.arccos(d / x))
    return out


def delta_E1(rad, f, om2, d, delta):
    """Delta E_1(d) = -delta Int ... g, g = f'^2 (an den Flaechen rp) + U(f^2) - om2 f^2 (an den Zellmitten r)."""
    S = f * f
    fp = np.append(f[1:], 0.0)
    gG = (fp - f) ** 2 / rad.dr ** 2
    gV = U(S) - om2 * S
    J = float(np.sum(kern(rad.n, rad.rp, d) * gG)) * rad.dr + float(np.sum(kern(rad.n, rad.r, d) * gV)) * rad.dr
    return -delta * J


def kraft_E1(rad, f, om2, d, delta):
    """d(Delta E_1)/dd. 2D: delta Int_d^inf g; 3D: 2 delta Int_d^inf rho g arccos(d/rho)."""
    S = f * f
    fp = np.append(f[1:], 0.0)
    gG = (fp - f) ** 2 / rad.dr ** 2
    gV = U(S) - om2 * S

    def k(rho):
        if rad.n == 2:
            return (rho > d).astype(float)
        out = np.zeros_like(rho)
        m = rho > d
        out[m] = 2 * rho[m] * np.arccos(np.minimum(d / rho[m], 1.0))
        return out

    return delta * (float(np.sum(k(rad.rp) * gG)) + float(np.sum(k(rad.r) * gV))) * rad.dr


def impulsfluss(rad, f, om2):
    """Probe der Karte: 2D Int_0^inf g drho = 0, 3D Int_0^inf rho g drho = 0 (Impulsfluss durch die Symmetrieebene)."""
    S = f * f
    fp = np.append(f[1:], 0.0)
    gG = (fp - f) ** 2 / rad.dr ** 2
    gV = U(S) - om2 * S
    w_p = rad.rp ** (rad.n - 2)
    w_c = rad.r ** (rad.n - 2)
    a = float(np.sum(w_p * gG) + np.sum(w_c * gV)) * rad.dr
    b = float(np.sum(w_p * np.abs(gG)) + np.sum(w_c * np.abs(gV))) * rad.dr
    return dict(integral=a, betrag=b, rel=a / b)


def schwanz(rad, f, d, delta):
    """2D: -(delta/2) f^2(d); 3D: -(delta/2) Int f^2(sqrt(d^2 + z^2)) dz."""
    S = f * f
    if rad.n == 2:
        return -0.5 * delta * float(np.interp(d, rad.r, S, right=0.0))
    z = np.arange(0.0, 60.0, 0.0025) + 0.00125
    Sz = np.interp(np.sqrt(d * d + z * z), rad.r, S, right=0.0)
    return -0.5 * delta * 2.0 * float(np.sum(Sz)) * 0.0025


def S_bei(rad, f, d):
    return float(np.interp(d, rad.r, f * f, right=0.0))


# --------------------------------------------------------------------------------------------------------------------
# Teil A: 2D-Auswertung der KEGEL-Q-Daten
# --------------------------------------------------------------------------------------------------------------------
def befehl_teil_a(args):
    delta = PI / 3.0
    Q = 200.0
    ordner = args.kq_ordner
    EK = lambda p: p['E_korr_erste_ordnung']
    E5, E7, m5, m7, S5, S7 = {}, {}, {}, {}, {}, {}
    quellen = []
    for n, Ed, md, Sd in ((5, E5, m5, S5), (7, E7, m7, S7)):
        for teil in ('a', 'b'):
            p = os.path.join(ordner, 'kraft-n%d-h0.2-Q200-%s.json' % (n, teil))
            b = lade(p)
            quellen.append(os.path.basename(p))
            assert b['n'] == n and abs(b['h'] - 0.2) < 1e-12 and abs(b['Q'] - 200.0) < 1e-9 and b['R'] == 40.0
            for q in b['punkte']:
                key = round(q['d'], 9)
                Ed[key] = EK(q)
                md[key] = q.get('dEdd_lambda')
                Sd[key] = q['S_spitze']
    bf = lade(os.path.join(ordner, 'bind-n6-h0.2-Q200.json'))
    quellen.append('bind-n6-h0.2-Q200.json')
    E_flach = [EK(q) for q in bf['punkte'] if q['art'] == 'd' and q['d'] == 0.0][0]
    ds = sorted(set(E5) & set(E7))
    aus = dict(befehl='teil_a', start=jetzt(), delta=delta, Q=Q, quellen=quellen, E_flach_gitter=E_flach, profile={})
    for dr in (0.01, 0.005):
        rad, fam = baue_familie(2, dr, 60.0, 0.62)
        g, f = loese_Q(rad, fam, Q)
        zeilen = []
        for d in ds:
            zeilen.append(dict(d=d, dE1=delta_E1(rad, f, g['om2'], d, delta), dE1_kraft=kraft_E1(rad, f, g['om2'], d, delta),
                               schwanz=schwanz(rad, f, d, delta), S_eben=S_bei(rad, f, d)))
        aus['profile']['dr=%g' % dr] = dict(omega=g['omega'], om2=g['om2'], E=g['E'], I=g['I'], G=g['G'], V=g['V'],
                                            S0=g['S0'], R_halb=g['R_halb'], R_half_S0=g['R_half_S0'], kappa=g['kappa'],
                                            res=g['res'], F=g['E'] - g['omega'] * Q,
                                            dE1_0_derrick=-(delta / (2 * PI)) * (g['E'] - g['omega'] * Q),
                                            impulsfluss=impulsfluss(rad, f, g['om2']), zeilen=zeilen)
    P = aus['profile']['dr=0.01']
    P2 = aus['profile']['dr=0.005']
    dE1_0 = P['zeilen'][0]['dE1']
    assert ds[0] == 0.0
    tab = []
    for k, d in enumerate(ds):
        z = P['zeilen'][k]
        O = 0.5 * (E5[d] - E7[d])
        Pd = 0.5 * (E5[d] + E7[d]) - E_flach
        tab.append(dict(d=d, E5_minus_Eflach=E5[d] - E_flach, E7_minus_Eflach=E7[d] - E_flach, O=O, P=Pd,
                        dE1=z['dE1'], dE1_dr0005=P2['zeilen'][k]['dE1'], O_minus_dE1=O - z['dE1'],
                        rel_zu_dE1_0=(O - z['dE1']) / abs(dE1_0), O_durch_dE1=(O / z['dE1'] if z['dE1'] != 0 else None),
                        schwanz=z['schwanz'], O_durch_schwanz=(O / z['schwanz'] if z['schwanz'] != 0 else None),
                        dE1_durch_schwanz=(z['dE1'] / z['schwanz'] if z['schwanz'] != 0 else None),
                        S_eben=z['S_eben'], S_spitze_5=S5[d], S_spitze_7=S7[d],
                        kraft_odd_lambda=(0.5 * (m5[d] - m7[d]) if (m5[d] is not None and m7[d] is not None) else None),
                        dE1_kraft=z['dE1_kraft']))
    aus['tabelle'] = tab
    # KX1
    abw = [abs(t['O_minus_dE1']) for t in tab]
    schranke = 0.03 * abs(dE1_0)
    aus['KX1'] = dict(eingetroffen=bool(all(a <= schranke for a in abw)), schranke=schranke, dE1_0=dE1_0,
                      max_abw=max(abw), d_max_abw=tab[int(np.argmax(abw))]['d'], punkte=len(tab),
                      regel='|O(d) - Delta E_1(d)| <= 0,03 |Delta E_1(0)| fuer alle d der E(d)-Tabelle (h = 0,2)')
    # KX3 (2D-Teil)
    dkx3 = P['R_halb'] + 3.0 / P['kappa']
    pk = [t for t in tab if t['d'] >= dkx3]
    ok = len(pk) >= 2 and all(abs(t['O'] - t['schwanz']) <= 0.25 * abs(t['schwanz']) for t in pk)
    aus['KX3_2D'] = dict(erfuellt=bool(ok), d_schwelle=dkx3, R_halb=P['R_halb'], kappa=P['kappa'],
                         punkte=[[t['d'], t['O'], t['schwanz'], t['O_durch_schwanz']] for t in pk],
                         regel='fuer alle d >= R_halb + 3/kappa (mind. 2 Punkte): |O(d) - T(d)| <= 0,25 |T(d)|, '
                               'T = -(delta/2) f^2(d) (ebenes Profil)')
    aus['ende'] = jetzt()
    schreibe_json(args.aus, aus)
    print('KX1', aus['KX1']['eingetroffen'], 'max_abw %.4e schranke %.4e' % (aus['KX1']['max_abw'], schranke))
    print('KX3_2D', ok, 'd_schwelle %.3f' % dkx3)
    print('geschrieben', args.aus)


# --------------------------------------------------------------------------------------------------------------------
# Ziel (3D): Familie, omega^2 fuer R_halb = 5, Zielwerte
# --------------------------------------------------------------------------------------------------------------------
def befehl_ziel(args):
    delta = args.delta
    aus = dict(befehl='ziel', start=jetzt(), delta=delta, R_ziel=args.R_ziel, dr=args.dr, rmax=args.rmax, ergebnisse={})
    for dr in (args.dr, args.dr / 2):
        rad, fam = baue_familie(3, dr, args.rmax, args.om2_start)
        tab = [g for g, f in fam]
        kmin = int(np.argmin([g['Q'] for g in tab]))
        if dr == args.dr:
            g, f = loese_Rhalb(rad, fam, args.R_ziel)
            Q = g['Q']
        else:
            g, f = loese_Q(rad, fam, Q)
        dk = g['R_halb'] + 3.0 / g['kappa']
        dl = [0.0, 3.0, args.R_ziel, args.R_ziel + 2.0, args.R_ziel + 4.0]
        dkx3 = [math.ceil(dk * 4.0) / 4.0, math.ceil(dk * 4.0) / 4.0 + 1.0]
        zeilen = []
        for d in dl + dkx3:
            zeilen.append(dict(d=d, dE1=delta_E1(rad, f, g['om2'], d, delta), dE1_kraft=kraft_E1(rad, f, g['om2'], d, delta),
                               schwanz=schwanz(rad, f, d, delta), S_eben=S_bei(rad, f, d), kx3=bool(d >= dk)))
        keil = {}
        for name, sgn in (('plus', 1.0), ('minus', -1.0)):
            Theta = 2 * PI - sgn * delta
            s = 2 * PI / Theta
            gs, fs = loese_Q(rad, fam, s * Q)
            keil[name] = dict(Theta=Theta, s=s, E_flach_sQ=gs['E'], E_keil=gs['E'] / s, dE_exakt=gs['E'] / s - g['E'],
                              omega_sQ=gs['omega'])
        aus['ergebnisse']['dr=%g' % dr] = dict(
            om2=g['om2'], omega=g['omega'], Q=Q, E=g['E'], I=g['I'], G=g['G'], V=g['V'], S0=g['S0'],
            R_halb=g['R_halb'], R_half_S0=g['R_half_S0'], kappa=g['kappa'], res=g['res'], F=g['E'] - g['omega'] * Q,
            derrick_G_plus_3V=g['G'] + 3 * (g['V'] - g['om2'] * g['I']),
            dE1_0_derrick=-(delta / (2 * PI)) * (g['E'] - g['omega'] * Q), d_kx3_schwelle=dk, d_liste=dl, d_kx3=dkx3,
            impulsfluss=impulsfluss(rad, f, g['om2']), zeilen=zeilen, keil=keil,
            VK_min=dict(om2=tab[kmin]['om2'], Q=tab[kmin]['Q']),
            familie=[{k: x[k] for k in ('om2', 'Q', 'E', 'R_halb', 'S0', 'res')} for x in tab])
        print('dr %g: om2 %.10f Q %.6f E %.8f R_halb %.5f kappa %.5f F %.6f dE1(0) %.6f' % (
            dr, g['om2'], Q, g['E'], g['R_halb'], g['kappa'], g['E'] - g['omega'] * Q, zeilen[0]['dE1']), flush=True)
    aus['ende'] = jetzt()
    schreibe_json(args.aus, aus)
    print('geschrieben', args.aus)


# --------------------------------------------------------------------------------------------------------------------
# 3D-Keil
# --------------------------------------------------------------------------------------------------------------------
class Zeitende(Exception):
    pass


class Keil:
    """Zellen (j, k, l): r_j = (j + 1/2) h, phi_k = (k + 1/2) dphi, z_l = (l + 1/2) h; Viertelgebiet (phi >= 0, z >= 0),
    Faktor 4 in allen Gewichten. Theta = Winkelumfang (2 pi - delta), dphi = Theta/(2 nphi)."""

    def __init__(self, h, rmax, zmax, nphi, Theta):
        self.h, self.Theta, self.Np = h, Theta, nphi
        self.Nr = int(round(rmax / h))
        self.Nz = int(round(zmax / h))
        self.dphi = 0.5 * Theta / nphi
        self.r = (np.arange(self.Nr) + 0.5) * h
        self.phi = (np.arange(self.Np) + 0.5) * self.dphi
        self.z = (np.arange(self.Nz) + 0.5) * h
        rf = np.arange(1, self.Nr + 1) * h
        self.w = 4.0 * self.r * h * self.dphi * h
        self.cr = 4.0 * rf * self.dphi
        self.cp = 4.0 * h * h / (self.r * self.dphi)
        self.cz = 4.0 * self.r * self.dphi
        self.s = 2 * PI / Theta
        self.u = (self.r[:, None] ** self.s) * np.cos(self.s * self.phi[None, :])   # (Nr, Np)
        mu = 2.0 - 2.0 * np.cos(PI * np.arange(self.Np) / self.Np)
        c0 = 4.0 / (h * h)
        th = mu[None, :] / (self.r[:, None] * self.dphi) ** 2
        self.Dm = (1.0 / np.sqrt(1.0 + th / c0))[:, :, None]                        # (Nr, Np, 1)
        self.Wi = (1.0 / np.sqrt(self.w))[:, None, None]
        self.Ws = np.sqrt(self.w)[:, None, None]
        self.shape = (self.Nr, self.Np, self.Nz)

    def abstand(self, d):
        """Geodaetischer Abstand jeder Zelle vom Punkt (r = d, phi = 0, z = 0)."""
        P = self.phi[None, :]
        R = self.r[:, None]
        rho2 = np.where(P < PI, np.sqrt(np.maximum(R * R + d * d - 2 * R * d * np.cos(P), 0.0)), R + d)
        return np.sqrt(rho2[:, :, None] ** 2 + self.z[None, None, :] ** 2)

    def nach_f(self, y):
        if self.Np > 1:
            return self.Wi * idct(self.Dm * y, type=2, axis=1, norm='ortho')
        return self.Wi * (self.Dm * y)

    def nach_y(self, f):
        if self.Np > 1:
            return dct(self.Ws * f, type=2, axis=1, norm='ortho') / self.Dm
        return self.Ws * f / self.Dm

    def grad_y(self, gf):
        if self.Np > 1:
            return self.Dm * dct(self.Wi * gf, type=2, axis=1, norm='ortho')
        return self.Dm * (self.Wi * gf)

    def teile(self, f):
        S = f * f
        Sj = S.sum(axis=(1, 2))
        I = float(self.w @ Sj)
        V = float(self.w @ U(S).sum(axis=(1, 2)))
        gG = np.zeros_like(f)
        df = f[1:] - f[:-1]
        t = self.cr[:-1, None, None] * df
        G = float(np.sum(t * df))
        gG[:-1] -= 2 * t
        gG[1:] += 2 * t
        G += self.cr[-1] * float(np.sum(f[-1] * f[-1]))
        gG[-1] += 2 * self.cr[-1] * f[-1]
        if self.Np > 1:
            df = f[:, 1:] - f[:, :-1]
            t = self.cp[:, None, None] * df
            G += float(np.sum(t * df))
            gG[:, :-1] -= 2 * t
            gG[:, 1:] += 2 * t
        df = f[:, :, 1:] - f[:, :, :-1]
        t = self.cz[:, None, None] * df
        G += float(np.sum(t * df))
        gG[:, :, :-1] -= 2 * t
        gG[:, :, 1:] += 2 * t
        G += float(self.cz @ np.sum(f[:, :, -1] ** 2, axis=1))
        gG[:, :, -1] += 2 * self.cz[:, None] * f[:, :, -1]
        return S, I, G, V, gG


def loese_keil(K, Q, D, f0, mit_nb, mu, tol_c, max_aussen, maxiter, deadline, maxcor):
    w3 = K.w[:, None, None]
    gu = (K.u - D)[:, :, None]
    N0 = float(K.w @ (f0 * f0).sum(axis=(1, 2)))
    lam = 0.0
    zaehler = dict(nfev=0)
    best = dict(LA=None, y=None)

    def werte(f):
        S, I, G, V, gG = K.teile(f)
        c = float(K.w @ (S * gu).sum(axis=(1, 2))) / N0 if mit_nb else 0.0
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
        gf = gG + 2 * w3 * f * (dU(S) - om2 + (m * gu / N0 if mit_nb else 0.0))
        if best['LA'] is None or LA < best['LA']:
            best['LA'] = LA
            best['y'] = yv.copy()
        return LA, K.grad_y(gf).ravel()

    y = K.nach_y(f0).ravel()
    verlauf = []
    nit = 0
    E_alt = None
    abgebrochen = False
    for aussen in range(max_aussen if mit_nb else 1):
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
        lam_alt = lam
        if mit_nb:
            lam = lam + mu * c
        verlauf.append(dict(aussen=aussen, E=E, c=c, lam=lam, msg=msg, nfev=zaehler['nfev'],
                            t=time.perf_counter() - T_START))
        print('   aussen %d: E %.12f c %.2e lam %.4e nfev %d %s (%.1f s)' % (
            aussen, E, c, lam, zaehler['nfev'], msg, time.perf_counter() - T_START), flush=True)
        if abgebrochen:
            break
        fertig = (not mit_nb) or (abs(c) < tol_c and E_alt is not None and abs(E - E_alt) < 1e-12 * abs(E))
        E_alt = E
        if fertig:
            break
    om2 = Q * Q / (4 * I * I)
    m = lam
    gE = gG + 2 * w3 * f * (dU(S) - om2)
    gL = gE + (2 * w3 * f * m * gu / N0 if mit_nb else 0.0)
    return dict(E=E, I=I, G=G, V=V, omega=math.sqrt(om2), c=c, m=m, N=I, N0=N0,
                res_max=float(np.max(np.abs(gL / (2 * w3)))), res_E_ohne_m=float(np.max(np.abs(gE / (2 * w3)))),
                aussen=len(verlauf), nit=nit, nfev=zaehler['nfev'], abgebrochen=abgebrochen, verlauf=verlauf), f


def befehl_ball3d(args):
    deadline = T_START + args.tmax
    Theta = 2 * PI - args.delta
    K = Keil(args.h, args.rmax, args.zmax, args.nphi, Theta)
    rad, fam = baue_familie(3, args.dr_radial, 60.0, args.om2_start)
    gQ, fQ = loese_Q(rad, fam, args.Q)
    gsQ, fsQ = loese_Q(rad, fam, K.s * args.Q) if args.delta != 0.0 else (gQ, fQ)
    aus = dict(befehl='ball3d', rolle=args.rolle, start=jetzt(), delta=args.delta, Theta=Theta, s=K.s, h=args.h,
               rmax=args.rmax, zmax=args.zmax, nphi=args.nphi, dphi=K.dphi, Nr=K.Nr, Nz=K.Nz, zellen=K.Nr * K.Np * K.Nz,
               Q=args.Q, mu=args.mu, maxcor=args.maxcor, tmax=args.tmax,
               radial=dict(omega_Q=gQ['omega'], E_eben_Q=gQ['E'], R_halb_Q=gQ['R_halb'], kappa_Q=gQ['kappa'],
                           omega_sQ=gsQ['omega'], E_eben_sQ=gsQ['E'], E_keil_exakt=gsQ['E'] / K.s),
               punkte=[])
    print('Keil delta %+.4f Theta %.6f s %.6f h %g Nr %d Np %d Nz %d (%d Zellen), dphi %.8f' % (
        args.delta, Theta, K.s, args.h, K.Nr, K.Np, K.Nz, K.Nr * K.Np * K.Nz, K.dphi), flush=True)
    for d in [float(x) for x in args.d.split(',')]:
        t0 = time.perf_counter()
        if d == 0.0 and K.Np > 1 and not args.nb_bei_null:
            raise RuntimeError('d = 0 nur achsensymmetrisch (nphi = 1) oder mit --nb-bei-null')
        if d > 0 and K.Np == 1:
            raise RuntimeError('d > 0 braucht nphi > 1')
        prof = fsQ if d == 0.0 else fQ
        f0 = np.interp(K.abstand(d), rad.r, prof, right=0.0)
        mit_nb = d > 0 or (K.Np > 1 and args.nb_bei_null)
        D = d ** K.s
        r, f = loese_keil(K, args.Q, D, f0, mit_nb, args.mu, args.tol_c, args.max_aussen, args.maxiter, deadline,
                          args.maxcor)
        S = f * f
        Nn = float(K.w @ S.sum(axis=(1, 2)))
        W = float(K.w @ (S * K.u[:, :, None]).sum(axis=(1, 2))) / Nn
        p = dict(d=d, D=D)
        p.update({k: v for k, v in r.items() if k != 'verlauf'})
        p['W'] = W
        p['d_W'] = abs(W) ** (1.0 / K.s) * (1 if W >= 0 else -1)
        p['E_korr'] = r['E'] + (r['m'] * r['c'] if mit_nb else 0.0)
        p['dEdD_lambda'] = -r['m'] * Nn / r['N0'] if mit_nb else None
        p['dEdd_lambda'] = (p['dEdD_lambda'] * K.s * d ** (K.s - 1.0)) if (mit_nb and d > 0) else None
        p['S_achse_z0'] = float(np.mean(S[0, :, 0]))
        p['f_max'] = float(f.max())
        p['f_min'] = float(f.min())
        p['f_rand_r'] = float(np.max(np.abs(f[-1])))
        p['f_rand_z'] = float(np.max(np.abs(f[:, :, -1])))
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
# Auswertung (3D-Urteile und Gesamturteile)
# --------------------------------------------------------------------------------------------------------------------
def befehl_auswertung(args):
    ordner = args.ordner
    zi = lade(args.ziel)
    Z = zi['ergebnisse']['dr=%g' % zi['dr']]
    ta = lade(os.path.join(ordner, 'teil-a.json'))
    balls = []
    for p in sorted(glob.glob(os.path.join(ordner, 'b3-*.json'))):
        b = lade(p)
        if b.get('befehl') == 'ball3d':
            b['datei'] = os.path.basename(p)
            balls.append(b)
    E = {}
    E_rand = {}
    info = {}
    for b in balls:
        sg = 0 if b['delta'] == 0.0 else (1 if b['delta'] > 0 else -1)
        for q in b['punkte']:
            key = (sg, round(b['h'], 6), round(q['d'], 6))
            if b['rolle'] == 'rand':
                E_rand[key] = dict(E=q['E_korr'], rmax=b['rmax'], zmax=b['zmax'], abgebrochen=q['abgebrochen'])
                continue
            if b['rolle'] not in ('haupt', 'null', 'flach'):
                continue
            E[key] = q['E_korr']
            info[key] = dict(datei=b['datei'], res_max=q['res_max'], c=q['c'], abgebrochen=q['abgebrochen'],
                             nfev=q['nfev'], dauer_s=q['dauer_s'], S_achse_z0=q['S_achse_z0'], d_W=q['d_W'],
                             f_rand_r=q['f_rand_r'], f_rand_z=q['f_rand_z'], dEdd_lambda=q.get('dEdd_lambda'),
                             nphi=b['nphi'], zellen=b['zellen'])
    hf, hc = args.h_fein, args.h_grob
    zeilen = {round(z['d'], 6): z for z in Z['zeilen']}
    dE1_0 = zeilen[0.0]['dE1']
    aus = dict(befehl='auswertung', start=jetzt(), h_fein=hf, h_grob=hc, ziel=os.path.basename(args.ziel),
               dateien=[b['datei'] for b in balls], urteile={}, tabellen={}, beschreibend={})
    tab = []
    for d in sorted(zeilen):
        z = zeilen[d]
        row = dict(d=d, dE1=z['dE1'], schwanz=z['schwanz'], kx3=z['kx3'], S_eben=z['S_eben'])
        for h, name in ((hf, 'fein'), (hc, 'grob')):
            kp, km, k0 = (1, round(h, 6), d), (-1, round(h, 6), d), (0, round(h, 6), d)
            if kp in E and km in E:
                O = 0.5 * (E[kp] - E[km])
                row['O_' + name] = O
                row['O_minus_dE1_' + name] = O - z['dE1']
                row['rel_zu_dE1_0_' + name] = (O - z['dE1']) / abs(dE1_0)
                row['abgebrochen_' + name] = bool(info[kp]['abgebrochen'] or info[km]['abgebrochen'])
                row['res_max_' + name] = max(info[kp]['res_max'], info[km]['res_max'])
                row['c_max_' + name] = max(abs(info[kp]['c']), abs(info[km]['c']))
                if k0 in E:
                    row['P_' + name] = 0.5 * (E[kp] + E[km]) - E[k0]
                    row['E_flach_' + name] = E[k0]
                    row['abgebrochen_flach_' + name] = bool(info[k0]['abgebrochen'])
        if 'O_fein' in row and 'O_grob' in row:
            q2 = (hc / hf) ** 2
            row['O_richardson'] = row['O_fein'] + (row['O_fein'] - row['O_grob']) / (q2 - 1.0)
            row['O_richardson_minus_dE1'] = row['O_richardson'] - z['dE1']
        tab.append(row)
    aus['tabellen']['3D'] = tab
    aus['tabellen']['info'] = {'%+d|%g|%g' % k: v for k, v in sorted(info.items())}
    # Randprobe: groesseres Gebiet (Rolle rand) gegen das Hauptgebiet bei gleichem h und d
    rp = []
    for (sg, h, d), v in sorted(E_rand.items()):
        if sg != 1 or (-1, h, d) not in E_rand:
            continue
        O_gross = 0.5 * (v['E'] - E_rand[(-1, h, d)]['E'])
        if (1, h, d) in E and (-1, h, d) in E:
            O_haupt = 0.5 * (E[(1, h, d)] - E[(-1, h, d)])
            rp.append(dict(h=h, d=d, rmax_gross=v['rmax'], zmax_gross=v['zmax'], O_gross=O_gross, O_haupt=O_haupt,
                           dO=O_gross - O_haupt, dO_rel_zu_dE1_0=(O_gross - O_haupt) / abs(dE1_0),
                           dE_plus=v['E'] - E[(1, h, d)], dE_minus=E_rand[(-1, h, d)]['E'] - E[(-1, h, d)]))
    aus['beschreibend']['randprobe'] = rp
    # KX0
    k_p, k_0 = (1, round(hf, 6), 0.0), (0, round(hf, 6), 0.0)
    ex = Z['keil']['plus']['dE_exakt']
    if k_p in E and k_0 in E:
        dE = E[k_p] - E[k_0]
        aus['urteile']['KX0'] = dict(eingetroffen=bool(abs(dE - ex) <= 0.03 * abs(ex)), dE_gitter=dE, dE_exakt=ex,
                                     rel_abw=(dE - ex) / abs(ex),
                                     regel='3D, d = 0, h_fein: |Delta E(+delta) - (E_flach(sQ)/s - E_flach(Q))| <= 0,03 '
                                           '|E_flach(sQ)/s - E_flach(Q)|')
    else:
        aus['urteile']['KX0'] = dict(eingetroffen=None, grund='Daten fehlen')
    km_, k0m = (-1, round(hf, 6), 0.0), (0, round(hf, 6), 0.0)
    if km_ in E and k0m in E:
        aus['beschreibend']['KX0_minus'] = dict(dE_gitter=E[km_] - E[k0m], dE_exakt=Z['keil']['minus']['dE_exakt'],
                                                rel_abw=(E[km_] - E[k0m] - Z['keil']['minus']['dE_exakt']) /
                                                abs(Z['keil']['minus']['dE_exakt']))
    # KX2
    karte = [round(x, 6) for x in Z['d_liste']]
    kx2 = [r for r in tab if round(r['d'], 6) in karte]
    vorhanden = [r for r in kx2 if 'O_fein' in r]
    schranke = 0.05 * abs(dE1_0)
    if len(vorhanden) == len(karte):
        ok = all(abs(r['O_minus_dE1_fein']) <= schranke for r in vorhanden)
        urteil = bool(ok)
    else:
        urteil = None
    aus['urteile']['KX2'] = dict(eingetroffen=urteil, schranke=schranke, dE1_0=dE1_0,
                                 punkte=[[r['d'], r.get('O_fein'), r['dE1'], r.get('O_minus_dE1_fein')] for r in kx2],
                                 max_abw=max((abs(r['O_minus_dE1_fein']) for r in vorhanden), default=None),
                                 regel='3D, h_fein: |O(d) - Delta E_1(d)| <= 0,05 |Delta E_1(0)| fuer alle fuenf d der Karte')
    # KX3
    k3 = [r for r in tab if r['kx3'] and 'O_fein' in r]
    ok3 = len(k3) >= 2 and all(abs(r['O_fein'] - r['schwanz']) <= 0.25 * abs(r['schwanz']) for r in k3)
    kx3_2d = ta['KX3_2D']
    aus['urteile']['KX3'] = dict(
        eingetroffen=bool(ok3 and kx3_2d['erfuellt']),
        teil_2D=dict(erfuellt=kx3_2d['erfuellt'], d_schwelle=kx3_2d['d_schwelle'], punkte=kx3_2d['punkte']),
        teil_3D=dict(erfuellt=bool(ok3), d_schwelle=Z['d_kx3_schwelle'],
                     punkte=[[r['d'], r['O_fein'], r['schwanz'], r['O_fein'] / r['schwanz']] for r in k3]),
        regel='beide Dimensionen: fuer alle d >= R_halb + 3/kappa (mind. 2 Punkte je Dimension) |O(d) - T(d)| <= 0,25 |T(d)|; '
              'T = -(delta/2) f^2(d) (2D) bzw. -(delta/2) Int f^2(sqrt(d^2 + z^2)) dz (3D), ebenes Profil')
    aus['urteile']['KX1'] = dict(eingetroffen=ta['KX1']['eingetroffen'], max_abw=ta['KX1']['max_abw'],
                                 schranke=ta['KX1']['schranke'], dE1_0=ta['KX1']['dE1_0'], regel=ta['KX1']['regel'])
    aus['ende'] = jetzt()
    schreibe_json(os.path.join(ordner, 'auswertung.json'), aus)
    kurz = {k: v.get('eingetroffen') for k, v in aus['urteile'].items()}
    schreibe_json(os.path.join(ordner, 'urteile.json'), dict(stand=jetzt(), urteile=kurz,
                                                             details={k: v for k, v in aus['urteile'].items()}))
    for k, v in sorted(kurz.items()):
        print(k, v)
    print('geschrieben', os.path.join(ordner, 'auswertung.json'))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='befehl', required=True)
    a = sub.add_parser('teil_a')
    a.add_argument('--kq-ordner', dest='kq_ordner', required=True)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('ziel')
    a.add_argument('--delta', type=float, required=True)
    a.add_argument('--R-ziel', dest='R_ziel', type=float, required=True)
    a.add_argument('--dr', type=float, default=0.01)
    a.add_argument('--rmax', type=float, default=60.0)
    a.add_argument('--om2-start', dest='om2_start', type=float, default=0.64)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('ball3d')
    a.add_argument('--rolle', required=True)
    a.add_argument('--delta', type=float, required=True)
    a.add_argument('--h', type=float, required=True)
    a.add_argument('--rmax', type=float, required=True)
    a.add_argument('--zmax', type=float, required=True)
    a.add_argument('--nphi', type=int, required=True)
    a.add_argument('--Q', type=float, required=True)
    a.add_argument('--d', required=True)
    a.add_argument('--nb-bei-null', dest='nb_bei_null', action='store_true')
    a.add_argument('--mu', type=float, default=5.0)
    a.add_argument('--tol-c', dest='tol_c', type=float, default=1e-9)
    a.add_argument('--max-aussen', dest='max_aussen', type=int, default=8)
    a.add_argument('--maxiter', type=int, default=20000)
    a.add_argument('--maxcor', type=int, default=12)
    a.add_argument('--tmax', type=float, default=560.0)
    a.add_argument('--dr-radial', dest='dr_radial', type=float, default=0.01)
    a.add_argument('--om2-start', dest='om2_start', type=float, default=0.64)
    a.add_argument('--aus', required=True)
    a = sub.add_parser('auswertung')
    a.add_argument('--ordner', required=True)
    a.add_argument('--ziel', required=True)
    a.add_argument('--h-fein', dest='h_fein', type=float, required=True)
    a.add_argument('--h-grob', dest='h_grob', type=float, required=True)
    args = ap.parse_args()
    try:
        {'teil_a': befehl_teil_a, 'ziel': befehl_ziel, 'ball3d': befehl_ball3d, 'auswertung': befehl_auswertung}[
            args.befehl](args)
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
