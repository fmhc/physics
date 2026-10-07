#!/usr/bin/env python3
"""DIM-LEITER-QBALL-1 (Runde 42), Code-Agent fuer die Leitung claude-primary.

Papier-I-Q-Ball in D Raumdimensionen (D = 1 bis 12), Masse m = 1:
  U(S) = S - S^2 + S^3/2, S = f^2;  phi = f(r) exp(i omega t);
  f'' + (D-1)/r f' + omega^2 f - U'(f^2) f = 0;
  Q = 2 omega Int f^2 d^Dx;  E = Int (omega^2 f^2 + |grad f|^2 + U(f^2)) d^Dx.
  Konvention wie Papier I (main.tex Gl. 1 und 2, Q-Definition) und KEGEL-Q / QB-BS-2D (D = 2).

Verfahren (PLAN.md Abschn. 4):
  Variationelle Finite-Volumen-Diskretisierung: Zellmitten r_j, Raender r_{j+1/2}; gleichfoermig (Schritt h) bis r_u,
  danach exponentiell gestreckt (Laenge L_STRECK) bis R_MAX; Dirichlet f = 0 hinter dem letzten Rand.
  Diskret: E = omega^2 Sum V f^2 + Sum A (f_{j+1} - f_j)^2 + Sum V U(f^2), Q = 2 omega Sum V f^2.
  Feldgleichung = Euler-Lagrange-Gleichung dieser Energie, daher gilt dE/dQ = omega auch im Diskreten.
  Newton bei festem omega^2 (tridiagonal), Fortsetzung in omega^2 mit Schrittteilung.
  dQ/domega exakt aus der linearisierten Gleichung J df/domega = 2 omega f.
  Kontrolle: Schiessverfahren (DOP853, Bisektion in f(0)) an zwei omega^2 je D.

Aufruf nur ueber kleintest.sh auf der .69:
  dim_leiter.py rauch <aus.json>
  dim_leiter.py rechne <D-Liste, z. B. 1,2,3> <aus.json>
  dim_leiter.py auswertung <aus.json> <ein1.json> [<ein2.json> ...]
  dim_leiter.py bild <auswertung.json> <ein1.json> [<ein2.json> ...] -- <praefix>
"""
import json
import math
import os
import sys
import time

for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_v, '1')

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.linalg import solve_banded
from scipy.optimize import brentq

T0 = time.perf_counter()

# ------------------------------------------------------------------------------------------------- Festlegungen (Plan)
OM2_C = 0.5                         # omega_min^2 = min U(S)/S
OM_MIN = math.sqrt(OM2_C)
SIG_TW = math.sqrt(2.0) / 4.0       # Wandspannung bei omega_min (KEGEL-Q)
H_GROB = 0.025
H_FEIN = 0.0125
L_STRECK = 5.0
R_MAX = 3000.0
TOL = 1e-10                         # Newton-Ziel (max. skaliertes Residuum)
TOL_ANNAHME = 1e-8                  # Annahmegrenze
START_OM2 = 0.75
G1 = [round(0.5 + 0.005 * k, 10) for k in range(6, 100)]                 # 0,530 ... 0,995 (Nachtrag 2)
G2 = [round(1.0 - 10.0 ** (-4.0 + 0.25 * k), 12) for k in range(0, 8)]    # 1 - om2 = 1e-4 ... 5,6e-3
OM2_GITTER = sorted(set(G1) | set(G2))
EXP_OM2 = [round(1.0 - 10.0 ** (-4.0 + 0.25 * k), 12) for k in range(0, 5)]  # Fit 1 - om2 in [1e-4, 1e-3]
EXIST_OM2 = [0.53, 0.535, 0.54, 0.545, 0.55]                           # Nachtrag 2: quadratischer Fit
SCHUSS_OM2 = [0.70, 0.95]
D_ALLE = list(range(1, 13))

# Projektwerte [P] (PLAN.md Abschn. 3)
REF_D3 = {0.55: (1.97733e4, 1.50306e4), 0.70: (4.73413e2, 4.28641e2), 0.80: (1.86110e2, 1.81912e2),
          0.90: (1.15642e2, 1.17398e2)}                       # RUNDE-02/tests1d, Test 4 (3D radial)
REF_D3_QMIN = 111.8441                                        # ebenda, bei omega^2 = 0,9269
REF_D3_QMIN_WEITERE = {'beutel-1': 111.86, 'FM-4': 111.87733}
REF_D2_QBBS = {13.0: 12.969231428, 21.0: 20.097535160, 100.0: 82.139707571}     # QB-BS-2D S0, M = 1200
REF_D2_KQ = {50.0: 43.56581450, 100.0: 82.13970391, 200.0: 157.30106459, 400.0: 304.95495546}  # KEGEL-Q, dr = 0,005
REF_D1 = {0.55: (3.81440547, 3.37107562), 0.70: (2.44149167, 2.29860697), 0.90: (1.29122682, 1.26897857)}

# Schwellen (Plan Abschn. 7)
TOL_REF = 1e-3
TOL_EXIST_OM = 0.002
TOL_F0_1D = 1e-4
TOL_EXPO = 0.10
TOL_DQ2 = 0.15


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


def flaeche(D):
    return 2.0 * math.pi ** (D / 2.0) / math.gamma(D / 2.0)


def exakt_1d(om2):
    """D = 1 per Quadratur [M]: f'^2 = U(f^2) - omega^2 f^2; Q = 2 sqrt2 omega ln((1 + sqrt2 eps)/a),
    a = sqrt(2 omega^2 - 1); E = omega Q + 2 Int_0^S0 sqrt(P) dS, P = (S0 - S)(S1 - S)/2."""
    om = math.sqrt(om2)
    a = math.sqrt(2.0 * om2 - 1.0)
    eps = math.sqrt(1.0 - om2)
    S0, S1 = 1.0 - a, 1.0 + a
    Q = 2.0 * math.sqrt(2.0) * om * math.log((1.0 + math.sqrt(2.0) * eps) / a)
    J = quad(lambda S: math.sqrt(max((S0 - S) * (S1 - S) / 2.0, 0.0)), 0.0, S0, epsabs=1e-15, epsrel=1e-13,
             limit=400)[0]
    return dict(Q=Q, E=om * Q + 2.0 * J, S0=S0)


# ------------------------------------------------------------------------------------------------- Gitter und Loeser
class Gitter:
    def __init__(self, D, h, r_u=None):
        self.D, self.h = D, h
        self.r_u = r_u if r_u is not None else max(60.0, (D - 1) * SIG_TW / 0.03 + 40.0)
        L = L_STRECK
        X = self.r_u + L * math.log1p((R_MAX - self.r_u) / L)
        M = int(math.ceil(X / h))
        x_f = np.arange(M + 1) * h
        x_c = (np.arange(M) + 0.5) * h

        def abb(x):
            return np.where(x <= self.r_u, x, self.r_u + L * np.expm1(np.maximum(x - self.r_u, 0.0) / L))

        r_f = abb(x_f)
        r_c = abb(x_c)
        r_g = 2.0 * r_f[-1] - r_c[-1]
        rc_ext = np.append(r_c, r_g)
        Sd = flaeche(D)
        V = np.empty(M)
        V[0] = Sd / D * r_f[1] ** D
        rl = r_f[1:-1]
        V[1:] = Sd / D * rl ** D * np.expm1(D * np.log1p((r_f[2:] - rl) / rl))
        self.A = Sd * r_f[1:] ** (D - 1) / (rc_ext[1:] - rc_ext[:-1])
        self.Am = np.concatenate(([0.0], self.A[:-1]))
        self.M, self.r, self.rf, self.V, self.Sd = M, r_c, r_f, V, Sd
        self.offo = -self.A[:-1] / self.V[:-1]
        self.offu = -self.A[:-1] / self.V[1:]
        self.diag0 = (self.A + self.Am) / self.V

    def F(self, f, om2):
        fp = np.append(f[1:], 0.0)
        fm = np.concatenate(([0.0], f[:-1]))
        S = f * f
        return (self.A * (f - fp) + self.Am * (f - fm)) / self.V + (dU(S) - om2) * f

    def jac(self, f, om2):
        S = f * f
        ab = np.empty((3, self.M))
        ab[0, 0] = 0.0
        ab[0, 1:] = self.offo
        ab[1, :] = self.diag0 + dU(S) + 2.0 * S * d2U(S) - om2
        ab[2, :-1] = self.offu
        ab[2, -1] = 0.0
        return ab

    def newton(self, f0, om2, tol=TOL, maxit=60):
        f = f0.copy()
        R = self.F(f, om2)
        nr = relres(R, f)
        it = 0
        while nr > tol and it < maxit:
            it += 1
            try:
                df = solve_banded((1, 1), self.jac(f, om2), -R)
            except (np.linalg.LinAlgError, ValueError):
                break
            if not np.all(np.isfinite(df)):
                break
            t = 1.0
            while True:
                fn = f + t * df
                Rn = self.F(fn, om2)
                nn = relres(Rn, fn)
                if nn < nr or t < 1e-3:
                    break
                t *= 0.5
            if not nn < nr:
                break
            f, R, nr = fn, Rn, nn
        return f, it, nr

    def groessen(self, f, om2):
        om = math.sqrt(om2)
        S = f * f
        I = float(np.sum(self.V * S))
        fp = np.append(f[1:], 0.0)
        G = float(np.sum(self.A * (fp - f) ** 2))
        Vp = float(np.sum(self.V * U(S)))
        r0, r1 = self.r[0], self.r[1]
        f0 = float((r1 * r1 * f[0] - r0 * r0 * f[1]) / (r1 * r1 - r0 * r0))
        S0 = f0 * f0
        idx = np.nonzero(S < 0.5 * S0)[0]
        if len(idx) and idx[0] > 0:
            k = int(idx[0])
            R_half = float(self.r[k - 1] + (0.5 * S0 - S[k - 1]) * (self.r[k] - self.r[k - 1]) / (S[k] - S[k - 1]))
        else:
            R_half = float('nan')
        D = self.D
        wirk = G + Vp - om2 * I
        vir = ((2 - D) * G - D * (Vp - om2 * I)) / (D * (G + abs(Vp) + om2 * I))
        I_aussen = float(np.sum((self.V * S)[self.r > 0.5 * R_MAX])) / I if I > 0 else float('nan')
        return dict(om2=om2, omega=om, Q=2.0 * om * I, E=om2 * I + G + Vp, I=I, G=G, Vp=Vp, f0=f0, R_half=R_half,
                    wirkung=wirk, virial=vir, I_aussen=I_aussen)

    def ableitungen(self, f, om2):
        om = math.sqrt(om2)
        g = solve_banded((1, 1), self.jac(f, om2), 2.0 * om * f)
        S = f * f
        I = float(np.sum(self.V * S))
        dI = 2.0 * float(np.sum(self.V * f * g))
        dQ = 2.0 * I + 2.0 * om * dI
        fp = np.append(f[1:], 0.0)
        gp = np.append(g[1:], 0.0)
        dG = 2.0 * float(np.sum(self.A * (fp - f) * (gp - g)))
        dV = 2.0 * float(np.sum(self.V * dU(S) * f * g))
        dE = 2.0 * om * I + om2 * dI + dG + dV
        return dQ, dE


def relres(R, f):
    """Relatives Residuum max|F|/max|f| (Nachtrag 1: absolut liess fast-triviale Profile durch)."""
    m = float(np.max(np.abs(f)))
    return float(np.max(np.abs(R))) / m if m > 0 and np.all(np.isfinite(R)) else float('inf')


def schuss_start(g, om2):
    """Startprofil per Schiessen (Nachtrag 1): Bisektion in f(0) zwischen U(S)/S = omega^2 und dem Huegel
    U'(S) = omega^2, Profil bis zum Umkehrpunkt, danach abklingender Schwanz."""
    D = g.D
    S_null = 1.0 - math.sqrt(2.0 * om2 - 1.0)
    S_top = (2.0 + math.sqrt(4.0 - 6.0 * (1.0 - om2))) / 3.0
    eps = math.sqrt(1.0 - om2)
    r_end = 40.0 / eps + (D - 1) * SIG_TW / (om2 - OM2_C) + 20.0

    def rhs(r, y):
        return [y[1], -(D - 1) / r * y[1] - om2 * y[0] + dU(y[0] * y[0]) * y[0]]

    def ev_null(r, y):
        return y[0]
    ev_null.terminal = True
    ev_null.direction = -1

    def ev_umkehr(r, y):
        return y[1]
    ev_umkehr.terminal = True
    ev_umkehr.direction = 1

    def lauf(a0, dense=False):
        b = (dU(a0 * a0) - om2) * a0 / (2.0 * D)
        if b >= 0:
            return 'gross', None
        r0 = 1e-4
        sol = solve_ivp(rhs, (r0, r_end), [a0 + b * r0 * r0, 2.0 * b * r0], method='DOP853', rtol=1e-11,
                        atol=1e-14, events=(ev_null, ev_umkehr), dense_output=dense)
        k = 'gross' if sol.t_events[0].size else 'klein' if sol.t_events[1].size else 'offen'
        return k, sol

    lo, hi = math.sqrt(S_null) * (1.0 + 1e-9), math.sqrt(S_top) * (1.0 - 1e-12)
    if not (lauf(lo)[0] == 'klein' and lauf(hi)[0] == 'gross'):
        return None
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        k = lauf(mid)[0]
        if k == 'gross':
            hi = mid
        elif k == 'klein':
            lo = mid
        else:
            lo = hi = mid
            break
        if hi - lo < 1e-14 * hi:
            break
    k, sol = lauf(lo, dense=True)
    r_stop = float(sol.t[-1])
    rg = g.r
    f = np.empty_like(rg)
    inn = rg <= r_stop
    f[inn] = np.where(rg[inn] < 1e-4, lo, sol.sol(np.maximum(rg[inn], 1e-4))[0])
    f_s = float(sol.sol(r_stop)[0])
    aus = ~inn
    f[aus] = f_s * np.exp(-eps * (rg[aus] - r_stop)) * (r_stop / rg[aus]) ** ((D - 1) / 2.0)
    return np.maximum(f, 0.0)


def knotenfrei(f):
    m = float(np.max(np.abs(f)))
    if not m > 0:
        return False
    s = f[np.abs(f) > 1e-12 * m]
    return bool(s[0] > 0 and np.all(s[1:] * s[:-1] > 0))


def akzeptiert(f, nr):
    return bool(np.all(np.isfinite(f)) and nr <= TOL_ANNAHME and f[0] > 1e-5 and knotenfrei(f))


def start_ueber_D(g, om2):
    """Nachtrag 1: Startprofil fuer D > 4 durch Fortsetzung in der (stetigen) Dimension von D = 4 aus, auf demselben
    Gitter (gleiches h und r_u, also gleiche Zellen). Praediktor: Wand um R_half ((D'-1)/(D-1) - 1) verschieben."""
    Dz = g.D
    D = 4.0
    gk = Gitter(D, g.h, r_u=g.r_u)
    f = None
    for R0 in (2.0, 5.0, 0.0, 10.0):
        for A in (1.0, 0.6, 0.3):
            S = A / (1.0 + np.exp(np.clip((gk.r - R0) / math.sqrt(0.5), -700.0, 700.0)))
            ff, it, nr = gk.newton(np.sqrt(S), om2, maxit=200)
            if akzeptiert(ff, nr):
                f = ff
                break
        if f is not None:
            break
    if f is None:
        raise RuntimeError('D-Fortsetzung: Start bei D = 4 gescheitert')
    schritt = 0.25
    while D < Dz - 1e-12:
        Dn = min(D + schritt, float(Dz))
        gn = Gitter(Dn, g.h, r_u=g.r_u) if Dn < Dz - 1e-12 else g
        q = gk.groessen(f, om2)
        kand = []
        if q['R_half'] > 3.0:
            dR = q['R_half'] * ((Dn - 1.0) / (D - 1.0) - 1.0)
            rr = gn.r - dR
            kand.append(np.where(rr <= gn.r[0], f[0], np.interp(rr, gk.r, f)))
        kand.append(f)
        fn = None
        for guess in kand:
            ff, it, nr = gn.newton(guess, om2, maxit=100)
            if akzeptiert(ff, nr):
                fn = ff
                break
        if fn is None:
            schritt *= 0.5
            if schritt < 1.0 / 256:
                raise RuntimeError('D-Fortsetzung gescheitert bei D = %.4f' % Dn)
            continue
        f, gk, D = fn, gn, Dn
        print("  D-Fortsetzung: D = %.4f, %.1f s" % (D, time.perf_counter() - T0), file=sys.stderr, flush=True)
        schritt = min(0.25, schritt * 1.5)
    return f


def startloesung(g, om2):
    eps = om2 - OM2_C
    Rtw = (g.D - 1) * SIG_TW / eps
    kand = []
    for R0 in sorted(set(round(x, 6) for x in (Rtw, 0.5 * Rtw, 2.0 * Rtw, 0.0, 2.0, 5.0))):
        for A in (1.0, 0.6, 0.3):
            S = A / (1.0 + np.exp(np.clip((g.r - R0) / math.sqrt(0.5), -700.0, 700.0)))
            f, it, nr = g.newton(np.sqrt(S), om2, maxit=200)
            if akzeptiert(f, nr):
                q = g.groessen(f, om2)
                kand.append((q['wirkung'], f, q['f0'], R0, A))
    fs = schuss_start(g, om2)
    if fs is not None:
        f, it, nr = g.newton(fs, om2, maxit=200)
        if akzeptiert(f, nr):
            q = g.groessen(f, om2)
            kand.append((q['wirkung'], f, q['f0'], 'schuss', 'schuss'))
    if not kand and g.D > 4:
        f = start_ueber_D(g, om2)
        q = g.groessen(f, om2)
        kand.append((q['wirkung'], f, q['f0'], 'D-Fortsetzung', 'D-Fortsetzung'))
    if not kand:
        raise RuntimeError('Startloesung D = %d gescheitert' % g.D)
    kand.sort(key=lambda t: t[0])
    verschieden = sorted(set(round(t[2], 6) for t in kand))
    return kand[0][1], dict(n_kandidaten=len(kand), f0_verschieden=verschieden, wirkung=[t[0] for t in kand],
                            gewaehlt=dict(R0=kand[0][3], A=kand[0][4]))


ZAEHLER = {'teilungen': 0, 'newton_aufrufe': 0}


def loese_schritt(g, f_prev, om2_prev, om2_neu, f_pp=None, om2_pp=None, tiefe=0):
    kand = []
    q_prev = g.groessen(f_prev, om2_prev)
    if q_prev['R_half'] > 8.0 and om2_neu < om2_prev:
        dR = q_prev['R_half'] * ((om2_prev - OM2_C) / (om2_neu - OM2_C) - 1.0)
        rr = g.r - dR
        kand.append(np.where(rr <= g.r[0], f_prev[0], np.interp(rr, g.r, f_prev)))
    if f_pp is not None and om2_pp is not None and om2_pp != om2_prev:
        kand.append(f_prev + (om2_neu - om2_prev) / (om2_prev - om2_pp) * (f_prev - f_pp))
    kand.append(f_prev)
    for guess in kand:
        ZAEHLER['newton_aufrufe'] += 1
        f, it, nr = g.newton(guess, om2_neu)
        if akzeptiert(f, nr):
            return f, it, nr
    if tiefe >= 12:
        raise RuntimeError('Fortsetzung gescheitert D = %d bei om2 = %.12f' % (g.D, om2_neu))
    ZAEHLER['teilungen'] += 1
    mid = 0.5 * (om2_prev + om2_neu)
    fm, _, _ = loese_schritt(g, f_prev, om2_prev, mid, f_pp, om2_pp, tiefe + 1)
    return loese_schritt(g, fm, mid, om2_neu, f_prev, om2_prev, tiefe + 1)


def familie(g, om2_liste):
    f_s, info = startloesung(g, START_OM2)
    fam = {START_OM2: f_s}
    ab = sorted([w for w in om2_liste if w < START_OM2], reverse=True)
    auf = sorted([w for w in om2_liste if w > START_OM2])
    for folge in (ab, auf):
        f_prev, o_prev, f_pp, o_pp = f_s, START_OM2, None, None
        for w in folge:
            f, it, nr = loese_schritt(g, f_prev, o_prev, w, f_pp, o_pp)
            fam[w] = f
            print("  Fortschritt D = %s h = %g: om2 %.6f, %.1f s, Teilungen %d" % (g.D, g.h, w, time.perf_counter() - T0, ZAEHLER["teilungen"]), file=sys.stderr, flush=True)
            f_pp, o_pp, f_prev, o_prev = f_prev, o_prev, f, w
    return fam, info


# ------------------------------------------------------------------------------------------------- Auswertung je Gitter
def analysiere(g, fam):
    keys = sorted(fam)
    punkte = []
    for w in keys:
        f = fam[w]
        q = g.groessen(f, w)
        dQ, dE = g.ableitungen(f, w)
        q.update(dQdom=dQ, dEdom=dE, dEdQ_rel=(dE / (math.sqrt(w) * dQ) - 1.0) if dQ != 0 else float('nan'),
                 EQ=q['E'] / q['Q'], res=relres(g.F(f, w), f))
        punkte.append(q)

    def loese_bei(w):
        k = min(keys, key=lambda x: abs(x - w))
        f, it, nr = g.newton(fam[k], w)
        if not akzeptiert(f, nr):
            f, it, nr = loese_schritt(g, fam[k], k, w)
        return f

    wurzeln_vk = []
    for a, b in zip(punkte[:-1], punkte[1:]):
        if a['dQdom'] * b['dQdom'] < 0:
            wc = brentq(lambda w: g.ableitungen(loese_bei(w), w)[0], a['om2'], b['om2'], xtol=1e-13, rtol=1e-12,
                        maxiter=100)
            qc = g.groessen(loese_bei(wc), wc)
            wurzeln_vk.append(dict(om2=wc, omega=math.sqrt(wc), Q=qc['Q'], E=qc['E'],
                                   art='min' if a['dQdom'] < 0 else 'max'))
    wurzeln_eq = []
    for a, b in zip(punkte[:-1], punkte[1:]):
        if (a['E'] - a['Q']) * (b['E'] - b['Q']) < 0:
            def fun(w):
                q = g.groessen(loese_bei(w), w)
                return q['E'] - q['Q']
            ws = brentq(fun, a['om2'], b['om2'], xtol=1e-13, rtol=1e-12, maxiter=100)
            qs = g.groessen(loese_bei(ws), ws)
            wurzeln_eq.append(dict(om2=ws, omega=math.sqrt(ws), Q=qs['Q'], E=qs['E'],
                                   art='E<Q unterhalb' if a['E'] < a['Q'] else 'E<Q oberhalb'))
    W = mass_W(punkte, wurzeln_vk, wurzeln_eq)
    expo = exponent(punkte)
    exist = existenz(punkte) if g.D >= 2 else None
    erg = dict(punkte=punkte, wurzeln_vk=wurzeln_vk, wurzeln_eq=wurzeln_eq, W=W, exponent=expo, existenz=exist,
               gitter=dict(h=g.h, M=g.M, r_u=g.r_u, R_MAX=R_MAX, L=L_STRECK))
    if g.D == 2:
        erg['ref_d2'] = [Q_ziel(g, punkte, loese_bei, Qt) for Qt in sorted(set(REF_D2_QBBS) | set(REF_D2_KQ))]
    if g.D == 1:
        abw = []
        for p in punkte:
            ex = exakt_1d(p['om2'])
            abw.append(dict(om2=p['om2'], dS0=p['f0'] ** 2 - ex['S0'], dQ_rel=p['Q'] / ex['Q'] - 1.0,
                            dE_rel=p['E'] / ex['E'] - 1.0))
        erg['exakt_1d'] = abw
    return erg, loese_bei


def Q_ziel(g, punkte, loese_bei, Qt):
    for a, b in zip(punkte[:-1], punkte[1:]):
        if (a['Q'] - Qt) * (b['Q'] - Qt) <= 0 and a['dQdom'] < 0 and b['dQdom'] < 0:
            w = brentq(lambda w: g.groessen(loese_bei(w), w)['Q'] - Qt, a['om2'], b['om2'], xtol=1e-15, rtol=1e-14,
                       maxiter=200)
            q = g.groessen(loese_bei(w), w)
            return dict(Q=Qt, om2=w, omega=math.sqrt(w), E=q['E'], Q_ist=q['Q'])
    return dict(Q=Qt, om2=None, E=None)


def mass_W(punkte, wurzeln_vk, wurzeln_eq):
    lo = punkte[0]
    s_vk0 = lo['dQdom'] < 0
    s_eq0 = lo['E'] < lo['Q']
    rv = sorted(w['omega'] for w in wurzeln_vk)
    re_ = sorted(w['omega'] for w in wurzeln_eq)
    br = sorted(set([OM_MIN, 1.0] + rv + re_))
    m_om = m_om2 = 0.0
    intervalle = []
    for x, y in zip(br[:-1], br[1:]):
        mid = 0.5 * (x + y)
        vk = s_vk0 ^ (sum(1 for t in rv if t < mid) % 2 == 1)
        eq = s_eq0 ^ (sum(1 for t in re_ if t < mid) % 2 == 1)
        if vk and eq:
            m_om += y - x
            m_om2 += y * y - x * x
            intervalle.append([x, y])
    return dict(W_om=m_om / (1.0 - OM_MIN), W_om2=m_om2 / (1.0 - OM2_C), intervalle_omega=intervalle,
                vk_am_unteren_rand=s_vk0, EQ_am_unteren_rand=s_eq0,
                vk_am_oberen_rand=punkte[-1]['dQdom'] < 0, EQ_am_oberen_rand=punkte[-1]['E'] < punkte[-1]['Q'])


def exponent(punkte):
    sel = [p for p in punkte if any(abs(p['om2'] - w) < 1e-13 for w in EXP_OM2)]
    x = np.log([math.sqrt(1.0 - p['om2']) for p in sel])
    y = np.log([p['Q'] for p in sel])
    p1 = float(np.polyfit(x, y, 1)[0])
    hoch = [p for p in punkte if p['om2'] > 0.99]
    xs = np.log([math.sqrt(1.0 - p['om2']) for p in hoch])
    ys = np.log([p['Q'] for p in hoch])
    lokal = [dict(eps_mitte=float(math.exp(0.5 * (xs[i] + xs[i + 1]))),
                  p=float((ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]))) for i in range(len(xs) - 1)]
    return dict(p=p1, n=len(sel), lokal=lokal)


def existenz(punkte):
    sel = [p for p in punkte if any(abs(p['om2'] - w) < 1e-13 for w in EXIST_OM2)]
    x = np.array([p['om2'] for p in sel])
    y = np.array([1.0 / p['R_half'] for p in sel])
    cf = np.polyfit(x, y, 2)
    wu = [float(z.real) for z in np.roots(cf) if abs(z.imag) < 1e-12 and z.real < x.min()]
    om2s = max(wu) if wu else float("nan")
    return dict(om2_stern=om2s, om_stern=math.sqrt(om2s) if om2s > 0 else float('nan'),
                R_half=[p['R_half'] for p in sel])


# ------------------------------------------------------------------------------------------------- Schiessverfahren
def schuss(D, om2, a_ref, r_end):
    def rhs(r, y):
        return [y[1], -(D - 1) / r * y[1] - om2 * y[0] + dU(y[0] * y[0]) * y[0]]

    def ev_null(r, y):
        return y[0]
    ev_null.terminal = True
    ev_null.direction = -1

    def ev_umkehr(r, y):
        return y[1]
    ev_umkehr.terminal = True
    ev_umkehr.direction = 1

    def klasse(a0):
        b = (dU(a0 * a0) - om2) * a0 / (2.0 * D)
        if b >= 0:
            return 'gross'
        r0 = 1e-4
        sol = solve_ivp(rhs, (r0, r_end), [a0 + b * r0 * r0, 2.0 * b * r0], method='DOP853', rtol=1e-12,
                        atol=1e-15, events=(ev_null, ev_umkehr))
        if sol.t_events[0].size:
            return 'gross'
        if sol.t_events[1].size:
            return 'klein'
        return 'offen'

    t0 = time.perf_counter()
    delta = 1e-4
    lo = hi = None
    while delta <= 0.1:
        a, b = a_ref * (1.0 - delta), a_ref * (1.0 + delta)
        ka, kb = klasse(a), klasse(b)
        if ka == 'klein' and kb == 'gross':
            lo, hi = a, b
            break
        delta *= 10.0
    if lo is None:
        return dict(om2=om2, ok=False, grund='keine Klammer', dauer_s=time.perf_counter() - t0)
    n = 0
    while hi - lo > 1e-12 * a_ref and n < 80:
        n += 1
        mid = 0.5 * (lo + hi)
        k = klasse(mid)
        if k == 'gross':
            hi = mid
        elif k == 'klein':
            lo = mid
        else:
            lo = hi = mid
            break
    return dict(om2=om2, ok=True, f0_schuss=0.5 * (lo + hi), breite=hi - lo, n=n, dauer_s=time.perf_counter() - t0)


# ------------------------------------------------------------------------------------------------- Befehle
def befehl_rauch(aus, Ds=(1, 4, 12), voll=False):
    """Rauchtest: nur Laufzeit, Konvergenz und D = 1 gegen die Quadratur; keine Q- oder E-Werte im Protokoll."""
    liste = OM2_GITTER if voll else [0.505, 0.6, 0.75, 0.9, 0.99, 0.9999]
    erg = dict(befehl='rauch', start=jetzt(), D={})
    for D in Ds:
        t = time.perf_counter()
        g = Gitter(D, H_GROB)
        fam, info = familie(g, liste)
        ana, loese_bei = analysiere(g, fam)
        z = dict(M=g.M, dauer_s=time.perf_counter() - t, max_res=max(p['res'] for p in ana['punkte']),
                 max_dEdQ_rel=max(abs(p['dEdQ_rel']) for p in ana['punkte']),
                 max_I_aussen=max(p['I_aussen'] for p in ana['punkte']), n_start=info['n_kandidaten'],
                 teilungen=ZAEHLER['teilungen'])
        if D == 1:
            z['max_dQ_rel_exakt'] = max(abs(a['dQ_rel']) for a in ana['exakt_1d'])
            z['max_dS0_exakt'] = max(abs(a['dS0']) for a in ana['exakt_1d'])
        if D == 12:
            ts = time.perf_counter()
            p = [q for q in ana['punkte'] if abs(q['om2'] - 0.75) < 1e-12][0]
            s = schuss(D, 0.75, p['f0'], p['R_half'] + 30.0 / math.sqrt(0.25))
            z['schuss_dauer_s'] = time.perf_counter() - ts
            z['schuss_rel_abw'] = (s['f0_schuss'] / p['f0'] - 1.0) if s['ok'] else None
        erg['D'][str(D)] = z
        print('rauch D = %d: M %d, %.1f s, max res %.1e, max |dE/dQ/om - 1| %.1e, I_aussen %.1e, Starts %d, '
              'Teilungen %d%s' % (D, g.M, z['dauer_s'], z['max_res'], z['max_dEdQ_rel'], z['max_I_aussen'],
                                  z['n_start'], z['teilungen'],
                                  (', 1D gegen Quadratur: dQ_rel %.1e, dS0 %.1e' % (z['max_dQ_rel_exakt'],
                                                                                   z['max_dS0_exakt'])) if D == 1
                                  else (', Schuss %.1f s, rel %.1e' % (z['schuss_dauer_s'], z['schuss_rel_abw'] or
                                                                         float('nan'))) if D == 12 else ''),
              flush=True)
    erg['ende'] = jetzt()
    erg['dauer_s'] = time.perf_counter() - T0
    schreibe_json(aus, erg)


def befehl_rechne(D_liste, aus):
    erg = dict(befehl='rechne', start=jetzt(), D_liste=D_liste,
               festlegungen=dict(H_GROB=H_GROB, H_FEIN=H_FEIN, L_STRECK=L_STRECK, R_MAX=R_MAX, TOL=TOL,
                                 TOL_ANNAHME=TOL_ANNAHME, START_OM2=START_OM2, OM2_GITTER=OM2_GITTER,
                                 EXP_OM2=EXP_OM2, EXIST_OM2=EXIST_OM2, SCHUSS_OM2=SCHUSS_OM2),
               ergebnisse={})
    for D in D_liste:
        tD = time.perf_counter()
        res = {}
        fein = None
        for name, h in (('grob', H_GROB), ('fein', H_FEIN)):
            t = time.perf_counter()
            ZAEHLER['teilungen'] = 0
            g = Gitter(D, h)
            fam, info = familie(g, OM2_GITTER)
            ana, loese_bei = analysiere(g, fam)
            ana['start'] = info
            ana['teilungen'] = ZAEHLER['teilungen']
            ana['dauer_s'] = time.perf_counter() - t
            res[name] = ana
            if name == 'fein':
                fein = ana
            del fam
        sch = []
        for w in SCHUSS_OM2:
            pf = [p for p in fein['punkte'] if abs(p['om2'] - w) < 1e-12][0]
            pg = [p for p in res['grob']['punkte'] if abs(p['om2'] - w) < 1e-12][0]
            s = schuss(D, w, pf['f0'], pf['R_half'] + 30.0 / math.sqrt(1.0 - w))
            if s['ok']:
                f0R = (4.0 * pf['f0'] - pg['f0']) / 3.0
                s.update(f0_fein=pf['f0'], f0_grob=pg['f0'], f0_richardson=f0R,
                         rel_fein=pf['f0'] / s['f0_schuss'] - 1.0, rel_grob=pg['f0'] / s['f0_schuss'] - 1.0,
                         rel_richardson=f0R / s['f0_schuss'] - 1.0)
            sch.append(s)
        res['schuss'] = sch
        res['dauer_s'] = time.perf_counter() - tD
        erg['ergebnisse'][str(D)] = res
        erg['stand'] = jetzt()
        schreibe_json(aus, erg)
        fe = res['fein']
        mins = [w for w in fe['wurzeln_vk'] if w['art'] == 'min']
        print('D = %2d: %.1f s (grob %.1f, fein %.1f), Punkte %d, max res %.1e, max |dE/dQ/om - 1| %.1e, '
              'VK-Wurzeln %d (min %d), E=Q-Wurzeln %d, W_om %.4f, p %.3f, Schuss %s' % (
                  D, res['dauer_s'], res['grob']['dauer_s'], fe['dauer_s'], len(fe['punkte']),
                  max(p['res'] for p in fe['punkte']), max(abs(p['dEdQ_rel']) for p in fe['punkte']),
                  len(fe['wurzeln_vk']), len(mins), len(fe['wurzeln_eq']), fe['W']['W_om'], fe['exponent']['p'],
                  ', '.join('%.1e' % s['rel_fein'] if s['ok'] else 'ohne' for s in sch)), flush=True)
    erg['ende'] = jetzt()
    erg['dauer_s'] = time.perf_counter() - T0
    schreibe_json(aus, erg)
    print('geschrieben', aus, 'Dauer %.1f s' % erg['dauer_s'], flush=True)


def lade(ein_liste):
    daten = {}
    for p in ein_liste:
        with open(p) as fh:
            daten.update(json.load(fh)['ergebnisse'])
    return daten


def kenngroessen(fe):
    mins = [w for w in fe['wurzeln_vk'] if w['art'] == 'min']
    if mins:
        m = min(mins, key=lambda w: w['Q'])
        qmin = dict(Q=m['Q'], omega=m['omega'], om2=m['om2'], innen=True)
    else:
        p = min(fe['punkte'], key=lambda p: p['Q'])
        qmin = dict(Q=p['Q'], omega=p['omega'], om2=p['om2'], innen=False)
    ws = fe['wurzeln_eq']
    s0 = min(ws, key=lambda w: w['omega']) if ws else None
    return qmin, s0


def befehl_auswertung(aus, ein_liste):
    daten = lade(ein_liste)
    Ds = sorted(int(k) for k in daten)
    tab = []
    for D in Ds:
        fe, gr = daten[str(D)]['fein'], daten[str(D)]['grob']
        qmin, s0 = kenngroessen(fe)
        qmin_g, s0_g = kenngroessen(gr)
        pf = {round(p['om2'], 12): p for p in fe['punkte']}
        pg = {round(p['om2'], 12): p for p in gr['punkte']}
        dq = max(abs(pf[k]['Q'] / pg[k]['Q'] - 1.0) for k in pf)
        de = max(abs(pf[k]['E'] / pg[k]['E'] - 1.0) for k in pf)
        z = dict(D=D, n_punkte=len(fe['punkte']), n_punkte_grob=len(gr['punkte']),
                 omega_c=qmin['omega'] if qmin['innen'] else None, Q_min=qmin['Q'], Q_min_innen=qmin['innen'],
                 Q_min_omega=qmin['omega'],
                 Q_min_grob=qmin_g['Q'], omega_c_grob=qmin_g['omega'] if qmin_g['innen'] else None,
                 omega_s=s0['omega'] if s0 else None, Q_s=s0['Q'] if s0 else None,
                 omega_s_grob=s0_g['omega'] if s0_g else None, Q_s_grob=s0_g['Q'] if s0_g else None,
                 n_wurzeln_eq=len(fe['wurzeln_eq']), n_wurzeln_vk=len(fe['wurzeln_vk']),
                 W_om=fe['W']['W_om'], W_om2=fe['W']['W_om2'], W_om_grob=gr['W']['W_om'],
                 W_intervalle=fe['W']['intervalle_omega'], W_raender=dict(
                     (k, fe['W'][k]) for k in ('vk_am_unteren_rand', 'EQ_am_unteren_rand', 'vk_am_oberen_rand',
                                               'EQ_am_oberen_rand')),
                 p=fe['exponent']['p'], p_grob=gr['exponent']['p'], p_lokal=fe['exponent']['lokal'],
                 Q_rand_unten=fe['punkte'][0]['Q'], Q_rand_oben=fe['punkte'][-1]['Q'],
                 EQ_rand_oben=fe['punkte'][-1]['EQ'],
                 om_stern=fe['existenz']['om_stern'] if fe['existenz'] else None,
                 max_dQ_grob_fein=dq, max_dE_grob_fein=de,
                 max_res=max(p['res'] for p in fe['punkte']),
                 max_dEdQ_rel=max(abs(p['dEdQ_rel']) for p in fe['punkte']),
                 max_virial=max(abs(p['virial']) for p in fe['punkte']),
                 max_I_aussen=max(p['I_aussen'] for p in fe['punkte']),
                 schuss=[dict((k, s.get(k)) for k in ('om2', 'ok', 'rel_fein', 'rel_grob', 'rel_richardson'))
                         for s in daten[str(D)]['schuss']],
                 start=fe['start'], teilungen=fe['teilungen'])
        tab.append(z)
    T = {z['D']: z for z in tab}
    alle = (Ds == D_ALLE)
    urteil = {}
    # ---- DQ0
    a1 = alle and all(z['n_punkte'] == len(OM2_GITTER) and z['n_punkte_grob'] == len(OM2_GITTER) for z in tab)
    a2_det = {D: (T[D]['om_stern'], abs(T[D]['om_stern'] - OM_MIN) <= TOL_EXIST_OM) for D in Ds if D >= 2}
    a2 = all(v[1] for v in a2_det.values())
    a3_wert = max(abs(a['dS0']) for a in daten['1']['fein']['exakt_1d']) if '1' in daten else None
    a3 = a3_wert is not None and a3_wert <= TOL_F0_1D
    b_det = {D: (T[D]['p'], 2 - D, abs(T[D]['p'] - (2 - D)) <= TOL_EXPO * abs(2 - D)) for D in (1, 3, 4) if D in T}
    b = len(b_det) == 3 and all(v[2] for v in b_det.values())
    c3 = []
    if '3' in daten:
        pf = {round(p['om2'], 12): p for p in daten['3']['fein']['punkte']}
        for w, (Qr, Er) in REF_D3.items():
            p = pf[round(w, 12)]
            c3.append(dict(quelle='RUNDE-02 tests1d', om2=w, Q=p['Q'], Q_ref=Qr, dQ=p['Q'] / Qr - 1.0, E=p['E'],
                           E_ref=Er, dE=p['E'] / Er - 1.0))
        c3.append(dict(quelle='RUNDE-02 tests1d Q_min', Q=T[3]['Q_min'], Q_ref=REF_D3_QMIN,
                       dQ=T[3]['Q_min'] / REF_D3_QMIN - 1.0,
                       weitere=dict((k, T[3]['Q_min'] / v - 1.0) for k, v in REF_D3_QMIN_WEITERE.items())))
    c2 = []
    if '2' in daten:
        refd = {round(r['Q'], 6): r for r in daten['2']['fein']['ref_d2']}
        for quelle, tabl in (('QB-BS-2D', REF_D2_QBBS), ('KEGEL-Q', REF_D2_KQ)):
            for Qt, Er in tabl.items():
                r = refd[round(Qt, 6)]
                c2.append(dict(quelle=quelle, Q=Qt, E=r['E'], E_ref=Er, omega=r.get('omega'),
                               dE=(r['E'] / Er - 1.0) if r['E'] is not None else None))
    c1 = []
    if '1' in daten:
        pf = {round(p['om2'], 12): p for p in daten['1']['fein']['punkte']}
        for w, (Qr, Er) in REF_D1.items():
            p = pf[round(w, 12)]
            c1.append(dict(quelle='RUNDE-02 tests1d Anker 1D', om2=w, dQ=p['Q'] / Qr - 1.0, dE=p['E'] / Er - 1.0))

    def ok3(lst):
        return bool(lst) and all(abs(x['dQ']) <= TOL_REF and (('dE' not in x) or abs(x['dE']) <= TOL_REF)
                                 for x in lst)
    c3_ok = ok3(c3)
    c2_ok = bool(c2) and all(x['dE'] is not None and abs(x['dE']) <= TOL_REF for x in c2)
    urteil['DQ0'] = dict(
        teile=dict(a1_alle_punkte=a1, a2_existenzgrenze=a2, a2_detail=a2_det, a3_1d_exakt=a3, a3_wert=a3_wert,
                   b_exponent=b, b_detail=b_det, c_D3=c3_ok, c_D2=c2_ok),
        plan=bool(a1 and a2 and a3 and b and c3_ok and c2_ok),
        wortlaut=bool(a1 and a2 and a3 and b and c3_ok),
        vergleich_D3=c3, vergleich_D2=c2, vergleich_D1=c1)
    # ---- DQ1
    D3 = [D for D in range(3, 13) if D in T]
    innen = {D: T[D]['Q_min_innen'] for D in D3}
    i_ok = len(D3) == 10 and all(innen.values())
    qm = [T[D]['Q_min'] for D in D3]
    mono = len(D3) == 10 and all(qm[i + 1] > qm[i] for i in range(len(qm) - 1))
    urteil['DQ1'] = dict(wendepunkt_alle=i_ok, wendepunkt_je_D=innen, monoton=mono,
                         plan=bool(i_ok and mono), wortlaut=bool(i_ok and mono))
    # ---- DQ2
    if len(D3) == 10:
        x = np.array(D3, dtype=float)
        y = np.log(np.array(qm))
        bb, aa = np.polyfit(x, y, 1)
        fit = aa + bb * x
        rel_plan = np.abs(np.exp(y - fit) - 1.0)
        rel_wort = np.abs(y - fit) / np.abs(y)
        urteil['DQ2'] = dict(a=float(aa), b=float(bb), faktor_je_D=float(math.exp(bb)),
                             rel_plan=dict(zip(D3, rel_plan.tolist())), rel_wortlaut=dict(zip(D3, rel_wort.tolist())),
                             max_rel_plan=float(rel_plan.max()), max_rel_wortlaut=float(rel_wort.max()),
                             Q_min_rand=[D for D in D3 if not T[D]['Q_min_innen']],
                             plan=bool(rel_plan.max() <= TOL_DQ2), wortlaut=bool(rel_wort.max() <= TOL_DQ2))
    # ---- DQ3
    def argmax(key):
        werte = {D: T[D][key] for D in Ds}
        m = max(werte.values())
        return sorted(D for D, v in werte.items() if v >= m - 1e-9), m
    am_om, m_om = argmax('W_om')
    am_om2, m_om2 = argmax('W_om2')
    p3 = alle and set(am_om) <= {3, 4}
    w3_2 = alle and set(am_om2) <= {3, 4}
    urteil['DQ3'] = dict(argmax_W_om=am_om, max_W_om=m_om, argmax_W_om2=am_om2, max_W_om2=m_om2,
                         plan=bool(p3),
                         wortlaut=('eingetroffen' if (p3 and w3_2) else 'nicht eingetroffen' if (not p3 and not w3_2)
                                   else 'uneindeutig'))
    erg = dict(befehl='auswertung', zeit=jetzt(), quellen=ein_liste, tabelle=tab, urteile=urteil)
    schreibe_json(aus, erg)
    for z in tab:
        print('D = %2d: omega_c %s, Q_min %.6g (%s), omega_s %s, Q_s %s, W_om %.4f, W_om2 %.4f, p %.3f' % (
            z['D'], '%.6f' % z['omega_c'] if z['omega_c'] else '-', z['Q_min'], 'innen' if z['Q_min_innen'] else
            'Rand', '%.6f' % z['omega_s'] if z['omega_s'] else '-', '%.6g' % z['Q_s'] if z['Q_s'] else '-',
            z['W_om'], z['W_om2'], z['p']), flush=True)
    for k, v in urteil.items():
        print(k, 'plan:', v.get('plan'), 'wortlaut:', v.get('wortlaut'), flush=True)


def befehl_bild(aus_json, ein_liste, praefix):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with open(aus_json) as fh:
        A = json.load(fh)
    daten = lade(ein_liste)
    tab = {z['D']: z for z in A['tabelle']}
    Ds = sorted(tab)
    cmap = plt.get_cmap('viridis')
    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    for i, D in enumerate(Ds):
        P = daten[str(D)]['fein']['punkte']
        om = [p['omega'] for p in P]
        Q = [p['Q'] for p in P]
        c = cmap(i / max(1, len(Ds) - 1))
        ax.plot(om, Q, '-', color=c, lw=1.4, label='D = %d' % D)
        z = tab[D]
        if z['omega_c']:
            ax.plot([z['omega_c']], [z['Q_min']], 'o', color=c, ms=5)
        if z['omega_s']:
            ax.plot([z['omega_s']], [z['Q_s']], 'x', color=c, ms=6, mew=1.5)
    ax.axvline(OM_MIN, color='0.5', lw=0.8, ls=':')
    ax.set_yscale('log')
    ax.set_xlim(0.70, 1.0)
    ax.set_xlabel('omega')
    ax.set_ylabel('Ladung Q')
    ax.set_title('Papier-I-Q-Ball: Q(omega) je Raumdimension D (Punkt: Q_min bei omega_c, Kreuz: E = Q bei omega_s)',
                 fontsize=9)
    ax.legend(fontsize=7, ncol=2, loc='upper center')
    ax.grid(alpha=0.3, which='both', lw=0.4)
    fig.tight_layout()
    fig.savefig(praefix + '-Q-omega.png', dpi=150)
    plt.close(fig)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
    xi = [D for D in Ds if tab[D]['Q_min_innen']]
    xr = [D for D in Ds if not tab[D]['Q_min_innen']]
    ax1.plot(xi, [tab[D]['Q_min'] for D in xi], 'o', color='#1f4e8c', label='Q_min (inneres Minimum)')
    ax1.plot(xr, [tab[D]['Q_min'] for D in xr], 'o', mfc='none', color='#1f4e8c', label='kleinstes Q im Fenster (Rand)')
    xs = [D for D in Ds if tab[D]['Q_s']]
    ax1.plot(xs, [tab[D]['Q_s'] for D in xs], 's', color='#c0392b', ms=5, label='Q_s (E = Q)')
    u2 = A['urteile'].get('DQ2')
    if u2:
        xx = np.linspace(3, 12, 50)
        ax1.plot(xx, np.exp(u2['a'] + u2['b'] * xx), '--', color='0.4', lw=1, label='Fit ln Q_min = a + b D (D 3-12)')
    ax1.set_yscale('log')
    ax1.set_xlabel('Raumdimension D')
    ax1.set_ylabel('Ladung')
    ax1.set_xticks(Ds)
    ax1.grid(alpha=0.3, which='both', lw=0.4)
    ax1.legend(fontsize=7)
    ax1.set_title('Mindestladung je D (logarithmisch)', fontsize=9)
    ax2.plot(Ds, [tab[D]['W_om'] for D in Ds], 'o-', color='#1f4e8c', label='W in omega')
    ax2.plot(Ds, [tab[D]['W_om2'] for D in Ds], 's--', color='#7f8c8d', ms=4, label='W in omega^2')
    ax2.set_xlabel('Raumdimension D')
    ax2.set_ylabel('W(D)')
    ax2.set_xticks(Ds)
    ax2.set_ylim(0, 1.05)
    ax2.grid(alpha=0.3, lw=0.4)
    ax2.legend(fontsize=7)
    ax2.set_title('Stabilitaetsmass W(D): VK-stabil und E < Q', fontsize=9)
    fig.tight_layout()
    fig.savefig(praefix + '-Qmin-W.png', dpi=150)
    plt.close(fig)
    print('Bilder', praefix + '-Q-omega.png', praefix + '-Qmin-W.png', flush=True)


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'rauch':
        befehl_rauch(sys.argv[2], tuple(int(x) for x in sys.argv[3].split(",")) if len(sys.argv) > 3 else (1, 4, 12), len(sys.argv) > 4 and sys.argv[4] == "voll")
    elif cmd == 'rechne':
        befehl_rechne([int(x) for x in sys.argv[2].split(',')], sys.argv[3])
    elif cmd == 'auswertung':
        befehl_auswertung(sys.argv[2], sys.argv[3:])
    elif cmd == 'bild':
        i = sys.argv.index('--')
        befehl_bild(sys.argv[2], sys.argv[3:i], sys.argv[i + 1])
    else:
        raise SystemExit('unbekannter Befehl')
