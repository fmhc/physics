#!/usr/bin/env python3
"""Q-STERN-2b (Runde 15): qstern2.py mit Fenster, K1-Ziel und K1-Umlauf als Aufrufparameter (--fenster, --k1-ziel,
--k1-umlauf); Physik unveraendert (Diff qstern2b.diff).
Q-STERN-2 (Runde 14 nach v3, explorativ): Kopie von RUNDE-13/q-stern/qstern.py, erweitert um delta Phi =
psi(r) cos(rho t) (volle Rechnung erster Ordnung, HERLEITUNG.md). Neu (Diff qstern2.diff):
   --psi voll: u = r psi, u'' = 2 alpha [(Pa - Pb rho) y1 + (Pa + Pb rho) y2 + f' (y1' + y2')],
               y1'' += (Ea - Eb rho) u, y2'' += (Ea + Eb rho) u,
               Pa = (omega^2 + U') f - f'/r, Pb = omega f, Ea = f (2 omega^2 - U'), Eb = 2 omega f.
               W aus der exakten Abhaengigkeitsbedingung (3 regulaere, 2 stille Loesungen, u eliminiert,
               W = Omega(Ya^, Z_perp) + i Omega(Yb^, Z_perp)); bei alpha = 0 gleich dem alten W.
   --psi null: Cowling, unveraenderter Q-STERN-Pfad (W_reell_cowling, W_multi_cowling).
   cmd_familie: Lokalisierung und kleines Rechteck direkt nach den Zeilen (vor Zwischenreihen und Streifen);
   Kandidaten im Fenster zuerst. K5 an jeder lokalisierten Stelle (nur --psi voll). --n-rampe.
Alter Kopf (qstern.py):
Q-STERN (Runde 13 nach v3, explorativ): Kopie von RUNDE-13/bball-leiter/bball2.py, erweitert um ein statisches
Newton-Potential Phi (selbstkonsistent, Poisson-Integral) und die Linearisierung in Cowling-Naeherung (delta Phi = 0).
Sextik-Modell U(S) = S - S^2 + S^3/2. Neu (Diff qstern.diff):
   Hintergrund: f'' + (2/r) f' = (1 - 2 Phi) U'(f^2) f - (1 - 4 Phi) omega^2 f,
                Phi'' + (2/r) Phi' = alpha rho_E, rho_E = omega^2 f^2 + f'^2 + U(f^2), Phi(inf) = 0.
   Linear:      A = (1 - 2 Phi) dp - (1 - 4 Phi) omega^2, B = 2 omega (1 - 4 Phi), C = (1 - 2 Phi) sp, D = 1 - 4 Phi,
                y1'' = (A + B rho - D rho^2) y1 + C y2,  y2'' = C y1 + (A - B rho - D rho^2) y2.
   z (geschlossen abklingend, offen exakt null bei R) startet mit z1'/z1 = -kappa_c + eta_c/R (Coulomb-Korrektur).
   Der offene Kanal von z ist bei R exakt null; das langreichweitige Phi koppelt die Kanaele nicht. Die Coulomb-Phase
   des offenen Kanals geht darum nicht in W ein (HERLEITUNG.md).
   --alpha, --r-fak (K3: Aussenrand R -> r_fak R), --quelle (rho | rho3p; Regel nur rho).
Alter Kopf (bball2.py):
B-BALL-LEITER (Runde 13 nach v3, explorativ): stille Stellen (W = 0 bei reellem rho) im Q-Ball mit flachem
Log-Potential U(S) = ln(1 + S) und, im selben Codepfad, im Sextik-Modell U(S) = S - S^2 + S^3/2 (Kontrolle K1).

Aufbau nach RUNDE-12/afm-kanal2/afm_bic.py (Verfahren unveraendert uebernommen: W_reell, W_multi, wurzeln, rechteck,
paaren, lokalisieren, D_komplex, pole). Neu: allgemeiner Profilloeser fuer beide Potentiale (Schiessen wie
RUNDE-10/nls-leiter/nls2.py profile, verallgemeinert; beim Log-Potential gibt es keinen Gipfel, die obere
Schiessgrenze wird darum verdoppelt, bis ein Ueberschuss auftritt), Schritt 0 (nackter geschlossener Kanal), K2.

Modell: L = |d phi|^2 - U(|phi|^2), S = |phi|^2, U'(0) = 1. Profil phi = f(r) e^{-i omega t}:
   f'' + (2/r) f' = (U'(S) - omega^2) f.
Lineares Problem (bic2, afm_bic KG-Zweig), l = 0, y = r w, Zeitfaktor e^{-i rho t}:
   y1'' = (A + B rho - rho^2) y1 + C y2      Kanal 1 geschlossen (omega - rho), Schwelle 1 + omega
   y2'' = C y1 + (A - B rho - rho^2) y2      Kanal 2 offen (omega + rho), Schwelle 1 - omega
   A = dp - omega^2, B = 2 omega, C = sp, dp = U' + S U'' = d(S U')/dS, sp = S U''.
   Sextik: dp = 1 - 4 S + 4,5 S^2, sp = -2 S + 3 S^2 (wie afm_bic/bic2).
   Log:    dp = 1/(1 + S)^2,         sp = -S/(1 + S)^2.
W = L(y_a) + i L(y_b), L(y) = Wronski-Summe mit z2 (abklingend im geschlossenen Kanal). W = 0 <=> stille Stelle.
Kommandos: familie | schritt0 | k2 | auswertung
"""
import argparse
import datetime
import glob
import json
import math
import os
import sys
import time

import numpy as np

T0 = time.perf_counter()
PI = math.pi
SPRUNG = 0.4          # aufgeloest: jeder Phasensprung auf dem Rand < 0,4 rad (wie bic2, afm_bic)
RAND = 0.002          # Abstand der rho-Abtastung von den Schwellen 1 - omega und 1 + omega (wie afm_bic)
THETA_RAND = 1e-6     # Aussenrand R: Profilamplitude < 1e-6 * Amplitude(0), mindestens r = 20 (wie afm_bic)
KG_X = [0.785, 0.79, 0.795, 0.80, 0.805, 0.81, 0.815]
KG_ZIEL = (0.797677, 1.744618)


def jetzt():
    return datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def uhr():
    return time.perf_counter() - T0


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, np.ndarray):
        return jsonfest(x.tolist())
    if isinstance(x, (complex, np.complexfloating)):
        return [jsonfest(float(x.real)), jsonfest(float(x.imag))]
    if isinstance(x, np.floating):
        x = float(x)
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, np.bool_):
        return bool(x)
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return x


class Budget:
    def __init__(self, sek):
        self.sek = sek
        self.entfallen = []

    def ok(self, was, reserve=0.0):
        if uhr() + reserve < self.sek:
            return True
        self.entfallen.append(f"{was} (bei {uhr():.0f} s)")
        return False


# ----------------------------------------------------------------------------------------------------------------------
# Potentiale
# ----------------------------------------------------------------------------------------------------------------------

T_MIX = 0.0          # B-BALL-2: Parameter t des Mischpotentials (Modell "mix"), gesetzt in main aus --t
ALPHA = 0.0          # Q-STERN: Kopplung alpha der Poisson-Gleichung, gesetzt in main aus --alpha
R_FAK = 1.0          # Q-STERN: Aussenrand-Faktor (K3: 1,5), gesetzt in main aus --r-fak
QUELLE = "rho"       # Q-STERN: Quelle der Poisson-Gleichung: "rho" (Karte) oder "rho3p" (rho + 3 p, nur Nebenlauf)
PHI_TOL = 1e-9       # Q-STERN: Konvergenz der Phi-Iteration (max |Phi_neu - Phi_alt|, absolut)
PHI_ITER = 80        # Q-STERN: hoechstens so viele Phi-Iterationen
PHI_MISCH = 1.0      # Q-STERN: Mischung Phi <- Phi_alt + misch (Phi_neu - Phi_alt)
N_RAMPE = 6          # Q-STERN: ohne Warmstart alpha in N_RAMPE Iterationen linear hochfahren (Kontinuitaet in alpha)
BG_CACHE = {}        # Q-STERN: konvergierte Hintergruende je (hp, alpha, r_fak, quelle): Liste (x, f0, PhiF, Phi2)
PSI = "voll"         # Q-STERN-2: "voll" (mit delta Phi = psi cos(rho t)) oder "null" (Cowling, Q-STERN-Pfad)


def U_(m, S):
    if m == "mix":
        return (1.0 - T_MIX) * (S - S * S + 0.5 * S ** 3) + T_MIX * np.log1p(S)
    if m == "log":
        return np.log1p(S)
    return S - S * S + 0.5 * S ** 3


def Up_(m, S):
    if m == "mix":
        return (1.0 - T_MIX) * (1.0 - 2.0 * S + 1.5 * S * S) + T_MIX / (1.0 + S)
    if m == "log":
        return 1.0 / (1.0 + S)
    return 1.0 - 2.0 * S + 1.5 * S * S


def Upp_(m, S):
    if m == "mix":
        return (1.0 - T_MIX) * (-2.0 + 3.0 * S) - T_MIX / (1.0 + S) ** 2
    if m == "log":
        return -1.0 / (1.0 + S) ** 2
    return -2.0 + 3.0 * S


def dp_(m, S):
    """U' + S U''."""
    if m == "mix":
        return (1.0 - T_MIX) * (1.0 - 4.0 * S + 4.5 * S * S) + T_MIX / (1.0 + S) ** 2
    if m == "log":
        return 1.0 / (1.0 + S) ** 2
    return 1.0 - 4.0 * S + 4.5 * S * S


def sp_(m, S):
    """S U''."""
    if m == "mix":
        return (1.0 - T_MIX) * (-2.0 * S + 3.0 * S * S) - T_MIX * S / (1.0 + S) ** 2
    if m == "log":
        return -S / (1.0 + S) ** 2
    return -2.0 * S + 3.0 * S * S


def G_(m, f, x, F=0.0):
    """f'' + (2/r) f' = G(f) = ((1 - 2 Phi) U'(f^2) - (1 - 4 Phi) omega^2) f, x = omega^2, F = Phi(r)."""
    return ((1.0 - 2.0 * F) * Up_(m, f * f) - (1.0 - 4.0 * F) * x) * f


def Gs_(m, f, x, F=0.0):
    """dG/df = (1 - 2 Phi)(U' + 2 S U'') - (1 - 4 Phi) omega^2."""
    S = f * f
    return (1.0 - 2.0 * F) * (Up_(m, S) + 2.0 * S * Upp_(m, S)) - (1.0 - 4.0 * F) * x


def rho_quelle(m, x, S, p2):
    """Quelle der Poisson-Gleichung (ohne alpha). Karte: rho_E = omega^2 f^2 + f'^2 + U. Nebenlauf: rho + 3 p."""
    if QUELLE == "rho3p":
        return 4.0 * x * S - 2.0 * U_(m, S)
    return x * S + p2 + U_(m, S)


def cum_int(g, h):
    """Kumulatives Integral int_0^r g auf dem Gitter j h: Trapez plus Euler-Maclaurin-Endkorrektur (Fehler O(h^4))."""
    T = np.concatenate([[0.0], np.cumsum(0.5 * (g[1:] + g[:-1]) * h)])
    dg = np.gradient(g, h, edge_order=2)
    return T - h * h / 12.0 * (dg - dg[0])


def phi_aus_profil(m, x, rr, f, p, al=None):
    """Phi(r) = -alpha [m(r)/r + int_r^inf rho r' dr'], m(r) = int_0^r rho r'^2 dr'; c = alpha m(inf) (Phi ~ -c/r)."""
    hp = float(rr[1] - rr[0])
    rho = rho_quelle(m, x, f * f, p * p)
    I1 = cum_int(rho * rr * rr, hp)
    I2 = cum_int(rho * rr, hp)
    Ph = np.empty_like(rr)
    al = ALPHA if al is None else al
    Ph[1:] = -al * (I1[1:] / rr[1:] + I2[-1] - I2[1:])
    Ph[0] = -al * I2[-1]
    return Ph, al * float(I1[-1]), float(I1[-1])


def phi_fein(rr, Ph, c, nf, hp):
    """Phi auf dem Feingitter j hp/2 (j = 0 .. nf - 1): kubischer Spline im Profilbereich, -c/r ausserhalb."""
    from scipy.interpolate import CubicSpline
    rf = np.arange(nf) * (0.5 * hp)
    out = np.empty(nf)
    innen = rf <= rr[-1]
    out[innen] = CubicSpline(rr, Ph)(rf[innen])
    out[~innen] = -c / rf[~innen]
    return out


def grenzen(m, x):
    """Schiess-Startintervall [sqrt(X_z), obere Grenze]; X_z: omega^2 X = U(X) (Nullstelle des mechanischen Potentials).
    Sextik: obere Grenze = Gipfel (G = 0, groessere Wurzel), wie nls2. Log: kein Gipfel; Start 2 sqrt(X_z + 1), wird
    im Schiessen verdoppelt, solange kein Ueberschuss auftritt (Rueckgabe erweiterbar = True)."""
    if m == "kg":
        b, e = 0.5, 1.0 - x
        Xm = (2.0 + math.sqrt(4.0 - 12.0 * b * e)) / (6.0 * b)
        Xz = (1.0 - math.sqrt(1.0 - 4.0 * b * e)) / (2.0 * b)
        return math.sqrt(Xz), math.sqrt(Xm), False
    if m == "mix":
        # U_t: X_z = erste Nullstelle von U_t(X) - x X (Abtastung, dann Halbierung); Gipfel X_m = erste Stelle X > X_z
        # mit U_t'(X) = x (nur fuer t < 1 vorhanden). Ohne Gipfel wie beim Log-Potential (obere Grenze verdoppeln).
        Xs = np.geomspace(1e-8, 1e4, 4001)
        gv = U_(m, Xs) - x * Xs
        k = int(np.argmax(gv <= 0.0))
        if gv[k] > 0.0:
            raise ValueError(f"mix t = {T_MIX}, x = {x}: kein X_z (kein Q-Ball)")
        a_, b_ = float(Xs[k - 1]), float(Xs[k])
        for _ in range(200):
            c_ = 0.5 * (a_ + b_)
            if float(U_(m, c_)) - x * c_ > 0:
                a_ = c_
            else:
                b_ = c_
        Xz = 0.5 * (a_ + b_)
        Gv = Up_(m, Xs) - x
        j = np.nonzero((Xs > Xz) & (Gv > 0.0))[0]
        if len(j) == 0:
            return math.sqrt(Xz), 2.0 * math.sqrt(Xz + 1.0), True
        a_, b_ = float(Xs[j[0] - 1]), float(Xs[j[0]])
        for _ in range(200):
            c_ = 0.5 * (a_ + b_)
            if float(Up_(m, c_)) - x < 0:
                a_ = c_
            else:
                b_ = c_
        return math.sqrt(Xz), math.sqrt(0.5 * (a_ + b_)), False
    g = lambda X: math.log1p(X) - x * X       # noqa: E731
    a_, b_ = 1e-9, 1.0
    while g(b_) > 0:
        b_ *= 2.0
    for _ in range(200):
        c_ = 0.5 * (a_ + b_)
        if g(c_) > 0:
            a_ = c_
        else:
            b_ = c_
    Xz = 0.5 * (a_ + b_)
    return math.sqrt(Xz), 2.0 * math.sqrt(Xz + 1.0), True


# ----------------------------------------------------------------------------------------------------------------------
# Profil: Schiessen (wie nls2.profile, 3D, verallgemeinert)
# ----------------------------------------------------------------------------------------------------------------------

def _rk4_prof(m, r, phi, p, hp, x, F0=0.0, Fm=0.0, F1=0.0):
    def f(rr, a, b, F):
        return b, G_(m, a, x, F) - 2.0 * b / rr
    k1a, k1b = f(r, phi, p, F0)
    k2a, k2b = f(r + 0.5 * hp, phi + 0.5 * hp * k1a, p + 0.5 * hp * k1b, Fm)
    k3a, k3b = f(r + 0.5 * hp, phi + 0.5 * hp * k2a, p + 0.5 * hp * k2b, Fm)
    k4a, k4b = f(r + hp, phi + hp * k3a, p + hp * k3b, F1)
    return (phi + hp / 6.0 * (k1a + 2 * k2a + 2 * k3a + k4a), p + hp / 6.0 * (k1b + 2 * k2b + 2 * k3b + k4b))


def _start(m, c, x, hp, F0=0.0, Phi2=0.0):
    """f = c + a r^2 + b r^4, Phi = Phi(0) + Phi2 r^2: 6 a = G(c, Phi(0)), 20 b = Gs a + G_Phi Phi2."""
    a = G_(m, c, x, F0) / 6.0
    GF = (-2.0 * Up_(m, c * c) + 4.0 * x) * c
    b = (Gs_(m, c, x, F0) * a + GF * Phi2) / 20.0
    return c + a * hp * hp + b * hp ** 4, 2.0 * a * hp + 4.0 * b * hp ** 3


def _klassen(m, xs, lo, hi, K, hp, r_max, f_lin, PhiF=None, Phi2=None):
    t = np.arange(1, K + 1) / (K + 1.0)
    c = lo[:, None] + (hi - lo)[:, None] * t[None, :]
    x = xs[:, None] * np.ones_like(c)
    kap = np.sqrt(1.0 - x)
    if PhiF is None:
        def Fz(j):
            return 0.0
        P2 = 0.0
    else:
        def Fz(j):
            return PhiF[j][:, None]
        P2 = Phi2[:, None]
    phi, p = _start(m, c, x, hp, Fz(0), P2)
    r = hp
    kl = np.zeros(c.shape, dtype=np.int8)
    offen = np.ones(c.shape, dtype=bool)
    n = int(r_max / hp)
    for k in range(1, n):
        phi, p = _rk4_prof(m, r, phi, p, hp, x, Fz(2 * k), Fz(2 * k + 1), Fz(2 * k + 2))
        r += hp
        ueber = offen & (phi < 0)
        unter = offen & (p > 0) & (phi > 0)
        lin = offen & ~ueber & ~unter & (phi < f_lin * c)
        if PhiF is None:
            B = p + phi * (kap + 1.0 / r)
        else:
            # Coulomb-Yukawa-Schwanz f ~ e^{-kappa r} r^(eta - 1), eta = -r Phi (4 omega^2 - 2) / (2 kappa)
            eta = -r * Fz(2 * k + 2) * (4.0 * x - 2.0) / (2.0 * kap)
            B = p + phi * (kap + (1.0 - eta) / r)
        kl[ueber] = 1
        kl[unter] = -1
        kl[lin & (B > 0)] = -1
        kl[lin & (B <= 0)] = 1
        offen &= ~(ueber | unter | lin)
        if not offen.any():
            break
    return c, kl


def schnitt(r, f, wert):
    """Erster Radius mit f <= wert (lineare Interpolation), wie afm_kanal.schnitt."""
    j = int(np.argmax(f <= wert))
    if j == 0 or f[j] > wert:
        return float("nan")
    return float(r[j - 1] + (f[j - 1] - wert) / (f[j - 1] - f[j]) * (r[j] - r[j - 1]))


def _schiessen(m, xs, hp, lo, hi, erw, frei, K, runden, r_max, f_lin, PhiF, Phi2):
    """Klammer-Schiessen wie bball2.profile; 'frei' = Startklammer ohne Garantie (Q-STERN, Phi != 0): Ausweiten nach
    oben bzw. unten, bis beide Enden durch eine klassifizierte Probe bestaetigt sind."""
    M = len(xs)
    lo, hi = lo.copy(), hi.copy()
    bestaetigt = ~erw
    lo_ok = ~frei
    hi_ok = ~frei
    fehler = [None] * M
    for rd in range(runden):
        c, kl = _klassen(m, xs, lo, hi, K, hp, r_max, f_lin, PhiF, Phi2)
        for i in range(M):
            k = kl[i]
            iu = np.where(k == -1)[0]
            io = np.where(k == 1)[0]
            w = hi[i] - lo[i]
            if len(io) == 0 and len(iu) == K:
                lo[i] = c[i, -1]
                lo_ok[i] = True
                if frei[i] and not hi_ok[i]:
                    hi[i] = hi[i] + 4.0 * w
                elif not bestaetigt[i]:
                    hi[i] = 2.0 * hi[i]
                continue
            if len(iu) == 0 and len(io) == K:
                hi[i] = c[i, 0]
                hi_ok[i] = True
                bestaetigt[i] = True
                if frei[i] and not lo_ok[i]:
                    lo[i] = max(lo[i] - 4.0 * w, 0.5 * lo[i])
                continue
            if len(iu) == 0 or len(io) == 0:
                fehler[i] = f"keine Klammer (unter {len(iu)}, ueber {len(io)}, Runde {rd})"
                continue
            j = io[0]
            ju = iu[iu < j]
            if len(ju):
                lo[i] = c[i, ju[-1]]
                lo_ok[i] = True
            hi[i] = c[i, j]
            hi_ok[i] = True
            bestaetigt[i] = True
        if np.all((hi - lo) <= 4e-16 * hi) and bestaetigt.all() and lo_ok.all() and hi_ok.all():
            break
    ok = np.array([fehler[i] is None and bool(bestaetigt[i]) and bool(lo_ok[i]) and bool(hi_ok[i])
                   and (hi[i] - lo[i] <= 1e-12 * hi[i]) for i in range(M)])
    return lo, hi, ok, fehler, bestaetigt


def _aufbau(m, xs, hp, lo, hi, ok, fehler, bestaetigt, PhiF, Phi2, cs, r_max, f_lin, f_rand, prot):
    """Profil aus der Klammer (wie bball2.profile), mit Phi im RK4 und Coulomb-Yukawa-Schwanz (eta aus c = alpha m)."""
    M = len(xs)
    cc = np.stack([lo, hi], 1)
    x2 = xs[:, None] * np.ones_like(cc)
    if PhiF is None:
        def Fz(j):
            return 0.0
        P2 = 0.0
    else:
        def Fz(j):
            return PhiF[j][:, None]
        P2 = Phi2[:, None]
    phi, p = _start(m, cc, x2, hp, Fz(0), P2)
    r = hp
    n = int(r_max / hp)
    PH = [cc * 1.0, phi.copy()]
    PP = [np.zeros_like(cc), p.copy()]
    aktiv = np.ones(M, dtype=bool)
    for k in range(1, n):
        phi, p = _rk4_prof(m, r, phi, p, hp, x2, Fz(2 * k), Fz(2 * k + 1), Fz(2 * k + 2))
        r += hp
        PH.append(phi.copy())
        PP.append(p.copy())
        mitte = 0.5 * (phi[:, 0] + phi[:, 1])
        aktiv &= ~((mitte < 1e-2 * f_lin * lo) | (np.abs(phi[:, 1] - phi[:, 0]) > 1e-3 * np.abs(mitte)))
        if not aktiv.any():
            break
    PH = np.array(PH)
    PP = np.array(PP)
    aus = []
    for i, x in enumerate(xs):
        if not ok[i]:
            if prot is not None:
                prot.append(f"Profil x = {x}: ungueltig ({fehler[i]}, bestaetigt {bool(bestaetigt[i])}, "
                            f"Klammer {hi[i] - lo[i]:.1e})")
            aus.append(None)
            continue
        kap = math.sqrt(1.0 - x)
        eta = (0.0 if PhiF is None else float(cs[i])) * (4.0 * x - 2.0) / (2.0 * kap)
        ph = 0.5 * (PH[:, i, 0] + PH[:, i, 1])
        pp = 0.5 * (PP[:, i, 0] + PP[:, i, 1])
        dif = np.abs(PH[:, i, 1] - PH[:, i, 0])
        f0 = ph[0]
        jm = None
        grund = "Ende"
        for j in range(1, len(ph)):
            if dif[j] > 1e-6 * abs(ph[j]):
                jm = j - 1
                grund = "Divergenz"
                break
            if ph[j] < f_lin * f0:
                jm = j
                grund = "Schwanz"
                break
        if jm is None:
            jm = len(ph) - 1
        rm = jm * hp
        Atl = ph[jm] * rm ** (1.0 - eta) * math.exp(kap * rm)
        R_aus = rm + max(0.0, (math.log(ph[jm] / (f_rand * f0)) / kap)) + 2.0
        if R_FAK > 1.0:
            R_aus = R_FAK * R_aus + 2.0
        J = int(math.ceil(R_aus / hp))
        J += J % 2
        if PhiF is not None:
            J = min(J, (PhiF.shape[0] - 1) // 2 - 2)
            J -= J % 2
        rr = np.arange(J + 1) * hp
        phi_g = np.empty(J + 1)
        p_g = np.empty(J + 1)
        phi_g[:jm + 1] = ph[:jm + 1]
        p_g[:jm + 1] = pp[:jm + 1]
        rt = rr[jm + 1:]
        phi_g[jm + 1:] = Atl * np.exp(-kap * rt) * rt ** (eta - 1.0)
        p_g[jm + 1:] = phi_g[jm + 1:] * (-kap + (eta - 1.0) / rt)
        w = np.ones(J + 1)
        w[1:-1:2] = 4.0
        w[2:-1:2] = 2.0
        w *= hp / 3.0
        S = phi_g ** 2
        r2 = rr ** 2
        om = math.sqrt(x)
        Fr = np.zeros(J + 1) if PhiF is None else PhiF[0:2 * J + 1:2, i]
        Q = 8.0 * PI * om * float(np.sum(w * (1.0 - 4.0 * Fr) * S * r2))
        T = 4.0 * PI * float(np.sum(w * p_g ** 2 * r2))
        E = 4.0 * PI * float(np.sum(w * (x * S + p_g ** 2 + U_(m, S)) * r2))
        Rw = schnitt(rr, phi_g, 0.5 * f0)
        aus.append({"x": float(x), "Omega": om, "hp": hp, "f0": float(f0), "r": rr, "phi": phi_g, "dphi": p_g,
                    "j_anschluss": int(jm), "r_anschluss": rm, "grund": grund, "f_anschluss": float(ph[jm] / f0),
                    "R_aus": float(rr[-1]), "R_w": Rw, "Q": Q, "E": E, "T": T,
                    "virial_rel": (E - om * Q - 2.0 * T / 3.0) / E, "kappa0": kap, "eta_schwanz": eta})
    return aus


def _warm(cache, x):
    """Startwerte aus konvergierten Hintergruenden: lineare Interpolation zwischen Nachbarn (Abstand <= 0,03),
    sonst naechster Nachbar. Rueckgabe (PhiF, Phi2, c, f0) oder None."""
    if not cache:
        return None
    unten = [e for e in cache if e[0] <= x]
    oben = [e for e in cache if e[0] >= x]
    if unten and oben:
        a = max(unten, key=lambda e: e[0])
        b = min(oben, key=lambda e: e[0])
        if b[0] - a[0] <= 0.03:
            if b[0] == a[0]:
                return a[2].copy(), a[3], a[4], a[1]
            t = (x - a[0]) / (b[0] - a[0])
            return ((1 - t) * a[2] + t * b[2], (1 - t) * a[3] + t * b[3], (1 - t) * a[4] + t * b[4],
                    (1 - t) * a[1] + t * b[1])
    e = min(cache, key=lambda q: abs(q[0] - x))
    return e[2].copy(), e[3], e[4], e[1]


def profile(m, xs, hp, K=64, runden=40, r_max=120.0, f_lin=1e-4, f_rand=1e-9, prot=None):
    """Grundzustaende (knotenfrei) fuer x = omega^2, mit selbstkonsistentem Phi (alpha > 0). Gitter r_j = j hp.
    alpha = 0: ein Durchgang wie bball2 (Phi = 0). Rueckgabe je x ein dict oder None."""
    xs = np.asarray(xs, dtype=float)
    M = len(xs)
    lo = np.empty(M)
    hi = np.empty(M)
    erw = np.zeros(M, dtype=bool)
    for i, x in enumerate(xs):
        a, b, e = grenzen(m, x)
        lo[i], hi[i], erw[i] = a * (1 + 1e-13), b * (1 - 1e-15), e
    if ALPHA == 0.0:
        lo, hi, ok, fehler, best = _schiessen(m, xs, hp, lo, hi, erw, np.zeros(M, dtype=bool), K, runden, r_max,
                                              f_lin, None, None)
        aus = _aufbau(m, xs, hp, lo, hi, ok, fehler, best, None, None, None, r_max, f_lin, f_rand, prot)
        for p in aus:
            if p is not None:
                p.update({"Phi": np.zeros(len(p["r"])), "Phi0": 0.0, "Phi_Rw": 0.0, "kompaktheit": 0.0,
                          "c_asym": 0.0, "m_quelle": float("nan"), "phi_iter": 0, "phi_dmax": 0.0})
        return aus
    n = int(r_max / hp)
    nf = 2 * n + 3
    cache = BG_CACHE.setdefault((hp, ALPHA, R_FAK, QUELLE), [])
    PhiF = np.zeros((nf, M))
    Phi2 = np.zeros(M)
    cs = np.zeros(M)
    frei = np.zeros(M, dtype=bool)
    letzte = np.full(M, np.nan)
    rampe = np.full(M, N_RAMPE)
    hist = [None] * M
    for i, x in enumerate(xs):
        wv = _warm(cache, x)
        if wv is not None:
            PhiF[:, i], Phi2[i], cs[i], f0w = wv
            lo[i], hi[i] = f0w * 0.97, f0w * 1.03
            frei[i] = True
            rampe[i] = 0
    akt = np.ones(M, dtype=bool)
    erg = [None] * M
    iters = np.zeros(M, dtype=int)
    dmax = np.full(M, np.inf)
    for it in range(PHI_ITER):
        idx = np.nonzero(akt)[0]
        if len(idx) == 0:
            break
        sub = xs[idx]
        Fs = np.ascontiguousarray(PhiF[:, idx])
        lo_s, hi_s, ok_s, feh_s, best_s = _schiessen(m, sub, hp, lo[idx], hi[idx], erw[idx], frei[idx], K, runden,
                                                     r_max, f_lin, Fs, Phi2[idx])
        aus_s = _aufbau(m, sub, hp, lo_s, hi_s, ok_s, feh_s, best_s, Fs, Phi2[idx], cs[idx], r_max, f_lin, f_rand,
                        prot)
        for q, i in enumerate(idx):
            p = aus_s[q]
            iters[i] = it + 1
            if p is None:
                akt[i] = False
                erg[i] = None
                continue
            al_k = ALPHA if rampe[i] == 0 else ALPHA * min(1.0, (it + 1.0) / rampe[i])
            Ph, c_neu, mq = phi_aus_profil(m, xs[i], p["r"], p["phi"], p["dphi"], al_k)
            Fn = phi_fein(p["r"], Ph, c_neu, nf, hp)
            d = float(np.max(np.abs(Fn - PhiF[:, i])))
            dmax[i] = d
            f0n = p["f0"]
            jw = int(np.argmin(np.abs(p["r"] - p["R_w"]))) if math.isfinite(p["R_w"]) else 0
            p.update({"Phi": Ph, "Phi0": float(Ph[0]), "Phi_Rw": float(Ph[jw]), "kompaktheit": float(2.0 * abs(Ph[0])),
                      "c_asym": c_neu, "m_quelle": mq, "phi_iter": int(it + 1), "phi_dmax": d})
            erg[i] = p
            if d < PHI_TOL and al_k == ALPHA:
                akt[i] = False
                cache.append((float(xs[i]), f0n, Fn.copy(), float((Fn[2] - Fn[0]) / hp ** 2), c_neu))
                continue
            # Anderson(1)-Mischung (Q-STERN): x_neu = x + b r - g (dx + b dr), g = <dr, r>/<dr, dr>; waehrend der
            # alpha-Rampe einfache Mischung
            r_k = Fn - PhiF[:, i]
            x_k = PhiF[:, i].copy()
            if al_k == ALPHA and hist[i] is not None:
                dx = x_k - hist[i][0]
                dr = r_k - hist[i][1]
                nn = float(np.dot(dr, dr))
                g = float(np.dot(dr, r_k)) / nn if nn > 0 else 0.0
                PhiF[:, i] = x_k + PHI_MISCH * r_k - g * (dx + PHI_MISCH * dr)
            else:
                PhiF[:, i] = x_k + PHI_MISCH * r_k
            hist[i] = (x_k, r_k) if al_k == ALPHA else None
            Phi2[i] = (PhiF[2, i] - PhiF[0, i]) / hp ** 2
            cs[i] = -PhiF[-1, i] * (PhiF.shape[0] - 1) * 0.5 * hp
            dl = abs(f0n - letzte[i]) if math.isfinite(letzte[i]) else 0.03 * f0n
            rel = min(0.03, max(10.0 * dl / f0n, 1e-9))
            lo[i], hi[i] = f0n * (1.0 - rel), f0n * (1.0 + rel)
            frei[i] = True
            letzte[i] = f0n
    for i in range(M):
        if erg[i] is not None and dmax[i] >= PHI_TOL:
            if prot is not None:
                prot.append(f"Profil x = {xs[i]}: Phi-Iteration nicht konvergiert ({iters[i]} It., d {dmax[i]:.1e})")
            erg[i] = None
    if prot is not None:
        prot.append(f"Phi-Iterationen (alpha {ALPHA}, hp {hp}): " + ", ".join(f"{x:.6f}:{n_}" for x, n_ in zip(xs, iters)))
    return erg


def prof_kurz(p):
    return {k: v for k, v in p.items() if k not in ("r", "phi", "dphi", "Phi")}


# ----------------------------------------------------------------------------------------------------------------------
# Profile -> Koeffizienten A, B, C, D (wie afm_bic.lin_aufbau; Q-STERN: mit Phi und D = 1 - 4 Phi)
# ----------------------------------------------------------------------------------------------------------------------

def lin_aufbau(x, Om, r, amp, A, B, C, D, Rw, h, info, Ph, c_asym):
    hp = float(r[1] - r[0])
    if abs(hp - 0.5 * h) > 1e-12:
        raise ValueError("Profil braucht Schritt h/2")
    J = len(r) - 1
    klein = np.nonzero(np.abs(amp) < THETA_RAND * abs(amp[0]))[0]
    j_r = int(klein[0]) if len(klein) else J
    j_r = min(max(j_r, int(math.ceil(20.0 / hp))), J)
    K = j_r // 2
    if R_FAK != 1.0:
        K = min(int(round(R_FAK * K)), J // 2)
    Km = max(2, min(K - 2, int(round(Rw / h))))
    j = 2 * K
    Af = (1.0 - 2.0 * Ph[j]) - (1.0 - 4.0 * Ph[j]) * Om * Om
    abw = max(abs(A[j] - Af), abs(B[j] - 2.0 * Om * (1.0 - 4.0 * Ph[j])), abs(C[j]))
    return {"x": float(x), "Omega": float(Om), "h": h, "K": K, "Km": Km, "R": K * h, "r_m": Km * h, "R_w": float(Rw),
            "Al": [float(v) for v in A[:j + 1]], "Bl": [float(v) for v in B[:j + 1]], "Cl": [float(v) for v in C[:j + 1]],
            "Dl": [float(v) for v in D[:j + 1]], "c_asym": float(c_asym), "Phi_R": float(Ph[j]),
            "rand_abw": float(abw), "info": info}


def profile_lin(modell, kap, xs, h, prot):
    """Profile fuer die Liste xs = omega^2; None = ungueltig. (kap ohne Bedeutung, Signatur wie afm_bic.)"""
    hp = 0.5 * h
    t0 = uhr()
    aus = []
    if not xs:
        return aus
    prs = profile(modell, list(xs), hp, prot=prot)
    for x, p in zip(xs, prs):
        if p is None:
            aus.append(None)
            continue
        f = p["phi"]
        S = f * f
        om = math.sqrt(x)
        Ph = p["Phi"]
        info = {"f0": p["f0"], "R_w": p["R_w"], "R_aus": p["R_aus"], "grund": p["grund"],
                "f_anschluss": p["f_anschluss"], "Q": p["Q"], "E": p["E"], "virial_rel": p["virial_rel"],
                "Phi0": p["Phi0"], "Phi_Rw": p["Phi_Rw"], "kompaktheit": p["kompaktheit"], "c_asym": p["c_asym"],
                "phi_iter": p["phi_iter"], "phi_dmax": p["phi_dmax"], "eta_schwanz": p["eta_schwanz"]}
        A = (1.0 - 2.0 * Ph) * dp_(modell, S) - (1.0 - 4.0 * Ph) * x
        B = 2.0 * om * (1.0 - 4.0 * Ph)
        C = (1.0 - 2.0 * Ph) * sp_(modell, S)
        D = 1.0 - 4.0 * Ph
        L = lin_aufbau(x, om, p["r"], f, A, B, C, D, p["R_w"], h, info, Ph, p["c_asym"])
        # Q-STERN-2: Kopplungen der psi-Rechnung (HERLEITUNG.md Abschnitte 3, 4)
        r = p["r"]
        fp = p["dphi"]
        Upv = Up_(modell, S)
        fpr = np.empty_like(f)
        fpr[1:] = fp[1:] / r[1:]
        fpr[0] = float(G_(modell, f[0], x, Ph[0])) / 3.0
        j = 2 * L["K"]
        L["Eal"] = [float(v) for v in (f * (2.0 * x - Upv))[:j + 1]]
        L["Ebl"] = [float(v) for v in (2.0 * om * f)[:j + 1]]
        L["Pal"] = [float(v) for v in ((x + Upv) * f - fpr)[:j + 1]]
        L["Pbl"] = [float(v) for v in (om * f)[:j + 1]]
        L["Fl"] = [float(v) for v in fp[:j + 1]]
        aus.append(L)
    prot.append(f"Profile ({modell}, {len(xs)} Stueck, h = {h}, alpha = {ALPHA}): {uhr() - t0:.1f} s")
    return aus


# ----------------------------------------------------------------------------------------------------------------------
# Lineare Loesungen (unveraendert aus afm_bic.py)
# ----------------------------------------------------------------------------------------------------------------------

def _rk4(y, A, B, C, rr, q2, j0, n, sg, hs, fak=None, D=None):
    """n RK4-Schritte fuer y'' = M y, M = [[A + B rho - D rho^2, C], [C, A - B rho - D rho^2]] (Q-STERN: D = 1 - 4 Phi;
    D = None heisst D = 1); Koeffizienten auf dem
    Gitter h/2 (Index j0, j0 + sg, ...). y = (y1, y2, y1', y2'), vektorisiert ueber rho."""
    y1, y2, p1, p2 = y
    h2 = 0.5 * hs
    h6 = hs / 6.0
    j = j0
    a_ = A[j] - (q2 if D is None else D[j] * q2)
    b_ = B[j] * rr
    m11a = a_ + b_
    m22a = a_ - b_
    ca = C[j]
    for _ in range(n):
        jm = j + sg
        je = jm + sg
        a_ = A[jm] - (q2 if D is None else D[jm] * q2)
        b_ = B[jm] * rr
        m11b = a_ + b_
        m22b = a_ - b_
        cb = C[jm]
        a_ = A[je] - (q2 if D is None else D[je] * q2)
        b_ = B[je] * rr
        m11c = a_ + b_
        m22c = a_ - b_
        cc = C[je]
        k1p1 = m11a * y1 + ca * y2
        k1p2 = ca * y1 + m22a * y2
        t1 = y1 + h2 * p1
        t2 = y2 + h2 * p2
        k2y1 = p1 + h2 * k1p1
        k2y2 = p2 + h2 * k1p2
        k2p1 = m11b * t1 + cb * t2
        k2p2 = cb * t1 + m22b * t2
        t1 = y1 + h2 * k2y1
        t2 = y2 + h2 * k2y2
        k3y1 = p1 + h2 * k2p1
        k3y2 = p2 + h2 * k2p2
        k3p1 = m11b * t1 + cb * t2
        k3p2 = cb * t1 + m22b * t2
        t1 = y1 + hs * k3y1
        t2 = y2 + hs * k3y2
        k4y1 = p1 + hs * k3p1
        k4y2 = p2 + hs * k3p2
        k4p1 = m11c * t1 + cc * t2
        k4p2 = cc * t1 + m22c * t2
        y1 = y1 + h6 * (p1 + 2.0 * (k2y1 + k3y1) + k4y1)
        y2 = y2 + h6 * (p2 + 2.0 * (k2y2 + k3y2) + k4y2)
        p1 = p1 + h6 * (k1p1 + 2.0 * (k2p1 + k3p1) + k4p1)
        p2 = p2 + h6 * (k1p2 + 2.0 * (k2p2 + k3p2) + k4p2)
        if fak is not None:
            y1 = y1 * fak
            y2 = y2 * fak
            p1 = p1 * fak
            p2 = p2 * fak
        m11a, m22a, ca = m11c, m22c, cc
        j = je
    return y1, y2, p1, p2


def _rk4_voll(Y, L, rr, j0, n, sg, hs, fak=None):
    """Q-STERN-2: n RK4-Schritte fuer das System mit psi (HERLEITUNG.md Abschnitte 3, 4), u = r psi:
    y1'' = (A + B rho - D rho^2) y1 + C y2 + (Ea - Eb rho) u
    y2'' = C y1 + (A - B rho - D rho^2) y2 + (Ea + Eb rho) u
    u''  = 2 alpha [(Pa - Pb rho) y1 + (Pa + Pb rho) y2 + F (y1' + y2')]
    Y = (y1, y2, u, y1', y2', u'), vektorisiert ueber rho (rr). Koeffizienten auf dem Gitter h/2 wie _rk4."""
    A, B, C, D = L["Al"], L["Bl"], L["Cl"], L["Dl"]
    Ea, Eb, Pa, Pb, F = L["Eal"], L["Ebl"], L["Pal"], L["Pbl"], L["Fl"]
    y1, y2, u, p1, p2, pu = Y
    q2 = rr * rr
    h2 = 0.5 * hs
    h6 = hs / 6.0
    al2 = 2.0 * ALPHA

    def koef(j):
        a_ = A[j] - D[j] * q2
        b_ = B[j] * rr
        return (a_ + b_, a_ - b_, C[j], Ea[j] - Eb[j] * rr, Ea[j] + Eb[j] * rr, al2 * (Pa[j] - Pb[j] * rr),
                al2 * (Pa[j] + Pb[j] * rr), al2 * F[j])

    def abl(k, y1, y2, u, p1, p2):
        m11, m22, c, e1, e2, s1, s2, sf = k
        return m11 * y1 + c * y2 + e1 * u, c * y1 + m22 * y2 + e2 * u, s1 * y1 + s2 * y2 + sf * (p1 + p2)
    j = j0
    ka = koef(j)
    for _ in range(n):
        jm = j + sg
        je = jm + sg
        kb = koef(jm)
        kc = koef(je)
        a1, a2, a3 = abl(ka, y1, y2, u, p1, p2)
        t1, t2, t3 = y1 + h2 * p1, y2 + h2 * p2, u + h2 * pu
        s1, s2, s3 = p1 + h2 * a1, p2 + h2 * a2, pu + h2 * a3
        b1, b2, b3 = abl(kb, t1, t2, t3, s1, s2)
        t1, t2, t3 = y1 + h2 * s1, y2 + h2 * s2, u + h2 * s3
        r1, r2, r3 = p1 + h2 * b1, p2 + h2 * b2, pu + h2 * b3
        c1, c2, c3 = abl(kb, t1, t2, t3, r1, r2)
        t1, t2, t3 = y1 + hs * r1, y2 + hs * r2, u + hs * r3
        w1, w2, w3 = p1 + hs * c1, p2 + hs * c2, pu + hs * c3
        d1, d2, d3 = abl(kc, t1, t2, t3, w1, w2)
        y1 = y1 + h6 * (p1 + 2.0 * (s1 + r1) + w1)
        y2 = y2 + h6 * (p2 + 2.0 * (s2 + r2) + w2)
        u = u + h6 * (pu + 2.0 * (s3 + r3) + w3)
        p1 = p1 + h6 * (a1 + 2.0 * (b1 + c1) + d1)
        p2 = p2 + h6 * (a2 + 2.0 * (b2 + c2) + d2)
        pu = pu + h6 * (a3 + 2.0 * (b3 + c3) + d3)
        if fak is not None:
            y1, y2, u, p1, p2, pu = y1 * fak, y2 * fak, u * fak, p1 * fak, p2 * fak, pu * fak
        ka = kc
        j = je
    return y1, y2, u, p1, p2, pu


def _start_aussen(L, rho):
    """Start von Z1 bei R: y1 = 1, y1' = -kappa_c + eta_c/R (wie qstern.W_reell)."""
    kc = np.sqrt(1.0 - (rho - L["Omega"]) ** 2)
    eta_c = L["c_asym"] * (4.0 * (rho - L["Omega"]) ** 2 - 2.0) / (2.0 * kc)
    return kc, -kc + eta_c / L["R"]


def _u_elim(X, Yu, Z2):
    """X^ = X + p Yu + q Z2 mit u = u' = 0 bei r_m; Rueckgabe der y-Komponenten (y1, y2, y1', y2')."""
    det = Yu[2] * Z2[5] - Z2[2] * Yu[5]
    p = (-X[2] * Z2[5] + Z2[2] * X[5]) / det
    q = (-Yu[2] * X[5] + Yu[5] * X[2]) / det
    return tuple(X[k] + p * Yu[k] + q * Z2[k] for k in (0, 1, 3, 4))


def W_reell_voll(L, rhos, chunk=3000):
    """Q-STERN-2: W = Omega(Ya^, Z_perp) + i Omega(Yb^, Z_perp) (HERLEITUNG.md Abschnitt 6). Rueckgabe wie W_reell."""
    rho_all = np.atleast_1d(np.asarray(rhos, dtype=float))
    n_all = rho_all.size
    La = np.empty(n_all)
    Lb = np.empty(n_all)
    wa = np.empty(n_all)
    for s0 in range(0, n_all, chunk):
        rho = rho_all[s0:s0 + chunk]
        N = rho.size
        rr = np.concatenate([rho, rho, rho])
        z3 = np.zeros(3 * N)
        p1 = z3.copy()
        p1[N:2 * N] = 1.0
        p2 = z3.copy()
        p2[:N] = 1.0
        pu = z3.copy()
        pu[2 * N:] = 1.0
        Yi = _rk4_voll((z3.copy(), z3.copy(), z3.copy(), p1, p2, pu), L, rr, 0, L["Km"], 1, L["h"])
        kc, lam = _start_aussen(L, rho)
        r2 = np.concatenate([rho, rho])
        z2 = np.zeros(2 * N)
        y1 = z2.copy()
        y1[:N] = 1.0
        q1 = z2.copy()
        q1[:N] = lam
        uu = z2.copy()
        uu[N:] = 1.0
        fak = np.concatenate([np.exp(-kc * L["h"]), np.ones(N)])
        Za = _rk4_voll((y1, z2.copy(), uu, q1, z2.copy(), z2.copy()), L, r2, 2 * L["K"], L["K"] - L["Km"], -1, -L["h"],
                       fak=fak)
        Ya = [v[:N] for v in Yi]
        Yb = [v[N:2 * N] for v in Yi]
        Yu = [v[2 * N:] for v in Yi]
        Z1 = [v[:N] for v in Za]
        Z2 = [v[N:] for v in Za]
        # Vertreter von Z2 ohne den nach innen wachsenden geschlossenen Anteil (Z1-artig): Z2 - gamma Z1, gamma aus
        # (y1, y1') bei r_m (kleinste Quadrate). Spaltenoperation im stillen Raum: die Lage bleibt exakt; sie verhindert
        # Pole von W, wo der u-Block von (Yu, Z2) singulaer wuerde (Rauchtest rauch-a2-voll, 23:49).
        gam = (Z2[0] * Z1[0] + Z2[3] * Z1[3]) / (Z1[0] ** 2 + Z1[3] ** 2)
        Z2 = [Z2[k] - gam * Z1[k] for k in range(6)]
        a = np.array(_u_elim(Ya, Yu, Z2))
        b = np.array(_u_elim(Yb, Yu, Z2))
        z = np.array(_u_elim(Z1, Yu, Z2))
        e1 = a / np.sqrt(np.sum(a * a, 0))
        bb = b - np.sum(e1 * b, 0) * e1
        e2 = bb / np.sqrt(np.sum(bb * bb, 0))
        zp = z - np.sum(e1 * z, 0) * e1 - np.sum(e2 * z, 0) * e2
        La[s0:s0 + N] = a[0] * zp[2] - a[2] * zp[0] + a[1] * zp[3] - a[3] * zp[1]
        Lb[s0:s0 + N] = b[0] * zp[2] - b[2] * zp[0] + b[1] * zp[3] - b[3] * zp[1]
        g = np.maximum.reduce([np.abs(v) for v in Yi])
        wa[s0:s0 + N] = np.maximum.reduce([g[:N], g[N:2 * N], g[2 * N:]])
    return La, Lb, wa


def k5_voll(L, rho):
    """Q-STERN-2 K5: Loesung an der Stelle zusammensetzen, u gegen die Integralform der Poisson-Gleichung pruefen."""
    h, K, Km = L["h"], L["K"], L["Km"]
    r3 = np.full(3, float(rho))
    st = (np.zeros(3), np.zeros(3), np.zeros(3), np.array([0.0, 1.0, 0.0]), np.array([1.0, 0.0, 0.0]),
          np.array([0.0, 0.0, 1.0]))
    tin = [st]
    for k in range(Km):
        st = _rk4_voll(st, L, r3, 2 * k, 1, 1, h)
        tin.append(st)
    r2 = np.full(2, float(rho))
    kc, lam = _start_aussen(L, np.array([float(rho)]))
    st = (np.array([1.0, 0.0]), np.zeros(2), np.array([0.0, 1.0]), np.array([float(lam[0]), 0.0]), np.zeros(2),
          np.zeros(2))
    taus = {K: st}
    for k in range(K, Km, -1):
        st = _rk4_voll(st, L, r2, 2 * k, 1, -1, -h)
        taus[k - 1] = st
    Mi = np.array([[float(tin[Km][c][i]) for i in range(3)] for c in range(6)])
    Ma = np.array([[float(taus[Km][c][i]) for i in range(2)] for c in range(6)])
    M = np.concatenate([Mi, -Ma], 1)
    nrm = np.sqrt(np.sum(M * M, 0))
    _, sv, Vt = np.linalg.svd(M / nrm[None, :])
    v = Vt[-1] / nrm
    ci, da = v[:3], v[3:]
    sol = np.empty((6, K + 1))
    for k in range(K + 1):
        if k <= Km:
            sol[:, k] = [float(np.dot(tin[k][c], ci)) for c in range(6)]
        else:
            sol[:, k] = [float(np.dot(taus[k][c], da)) for c in range(6)]
    y1, y2, u, p1, p2 = sol[0], sol[1], sol[2], sol[3], sol[4]
    idx = 2 * np.arange(K + 1)
    Pa = np.asarray(L["Pal"])[idx]
    Pb = np.asarray(L["Pbl"])[idx]
    F = np.asarray(L["Fl"])[idx]
    g = 2.0 * ALPHA * ((Pa - Pb * rho) * y1 + (Pa + Pb * rho) * y2 + F * (p1 + p2))
    I = cum_int(g, h)
    upG = I - I[-1]
    uG = cum_int(upG, h)
    um = float(np.max(np.abs(u)))
    return {"rho": float(rho), "x": L["x"], "rest_rel": float(np.max(np.abs(u - uG)) / um) if um > 0 else float("nan"),
            "sv_verh": float(sv[-1] / sv[0]), "u_max": um, "y_max": float(max(np.max(np.abs(y1)), np.max(np.abs(y2)))),
            "u_R": float(u[-1]), "up_R": float(sol[5][-1]), "y2_R": float(y2[-1]), "K": K, "Km": Km}


def W_reell(L, rhos, chunk=6000):
    """Q-STERN-2: Verteiler (voll: W_reell_voll; null: Q-STERN-Pfad)."""
    if PSI == "voll":
        return W_reell_voll(L, rhos)
    return W_reell_cowling(L, rhos, chunk)


def W_multi(Ls, rho_listen):
    """Q-STERN-2: Verteiler. voll: je Profil W_reell_voll mit eigenem R und r_m."""
    if PSI == "voll":
        return [W_reell_voll(L, r_)[:2] for L, r_ in zip(Ls, rho_listen)]
    return W_multi_cowling(Ls, rho_listen)


def W_reell_cowling(L, rhos, chunk=6000):
    rho_all = np.atleast_1d(np.asarray(rhos, dtype=float))
    n_all = rho_all.size
    La = np.empty(n_all)
    Lb = np.empty(n_all)
    wa = np.empty(n_all)
    for s0 in range(0, n_all, chunk):
        rho = rho_all[s0:s0 + chunk]
        N = rho.size
        rr = np.concatenate([rho, rho])
        q2 = rr * rr
        p1 = np.zeros(2 * N)
        p1[N:] = 1.0
        p2 = np.zeros(2 * N)
        p2[:N] = 1.0
        y1, y2, p1, p2 = _rk4((np.zeros(2 * N), np.zeros(2 * N), p1, p2), L["Al"], L["Bl"], L["Cl"], rr, q2, 0,
                              L["Km"], 1, L["h"], D=L["Dl"])
        kc = np.sqrt(1.0 - (rho - L["Omega"]) ** 2)
        eta_c = L["c_asym"] * (4.0 * (rho - L["Omega"]) ** 2 - 2.0) / (2.0 * kc)
        z1, z2, zp1, zp2 = _rk4((np.ones(N), np.zeros(N), -kc + eta_c / L["R"], np.zeros(N)), L["Al"], L["Bl"], L["Cl"],
                                rho, rho * rho,
                                2 * L["K"], L["K"] - L["Km"], -1, -L["h"], fak=np.exp(-kc * L["h"]), D=L["Dl"])
        La[s0:s0 + N] = y1[:N] * zp1 - p1[:N] * z1 + y2[:N] * zp2 - p2[:N] * z2
        Lb[s0:s0 + N] = y1[N:] * zp1 - p1[N:] * z1 + y2[N:] * zp2 - p2[N:] * z2
        g = np.maximum.reduce([np.abs(y1), np.abs(y2), np.abs(p1), np.abs(p2)])
        wa[s0:s0 + N] = np.maximum(g[:N], g[N:])
    return La, Lb, wa


def W_multi_cowling(Ls, rho_listen):
    h = Ls[0]["h"]
    Kx = max(L["K"] for L in Ls)
    Kmc = max(2, min(min(L["K"] for L in Ls) - 2, int(round(float(np.median([L["R_w"] for L in Ls])) / h))))
    n = 2 * Kx + 1
    Am = np.empty((len(Ls), n))
    Bm = np.empty((len(Ls), n))
    Cm = np.zeros((len(Ls), n))
    Dm = np.empty((len(Ls), n))
    rgit = np.arange(n) * (0.5 * h)
    for p, L in enumerate(Ls):
        m = 2 * L["K"] + 1
        Am[p, :m], Bm[p, :m], Cm[p, :m], Dm[p, :m] = L["Al"][:m], L["Bl"][:m], L["Cl"][:m], L["Dl"][:m]
        # Q-STERN: Fortsetzung mit Phi = -c/r (statt Phi = 0) jenseits des eigenen Randes
        Pa = -L["c_asym"] / rgit[m:] if m < n else np.zeros(0)
        Am[p, m:] = (1.0 - 2.0 * Pa) - (1.0 - 4.0 * Pa) * L["Omega"] ** 2
        Bm[p, m:] = 2.0 * L["Omega"] * (1.0 - 4.0 * Pa)
        Dm[p, m:] = 1.0 - 4.0 * Pa
    pidx = np.concatenate([np.full(len(r_), p, dtype=int) for p, r_ in enumerate(rho_listen)])
    rho = np.concatenate([np.asarray(r_, dtype=float) for r_ in rho_listen])
    Om = np.array([Ls[p]["Omega"] for p in pidx])
    cA = np.array([Ls[p]["c_asym"] for p in pidx])
    AT, BT, CT, DT = Am[pidx].T.copy(), Bm[pidx].T.copy(), Cm[pidx].T.copy(), Dm[pidx].T.copy()
    N = rho.size
    rr = np.concatenate([rho, rho])
    A2, B2, C2 = np.concatenate([AT, AT], 1), np.concatenate([BT, BT], 1), np.concatenate([CT, CT], 1)
    D2 = np.concatenate([DT, DT], 1)
    p1 = np.zeros(2 * N)
    p1[N:] = 1.0
    p2 = np.zeros(2 * N)
    p2[:N] = 1.0
    y1, y2, p1, p2 = _rk4((np.zeros(2 * N), np.zeros(2 * N), p1, p2), A2, B2, C2, rr, rr * rr, 0, Kmc, 1, h, D=D2)
    kc = np.sqrt(1.0 - (rho - Om) ** 2)
    eta_c = cA * (4.0 * (rho - Om) ** 2 - 2.0) / (2.0 * kc)
    z1, z2, zp1, zp2 = _rk4((np.ones(N), np.zeros(N), -kc + eta_c / (Kx * h), np.zeros(N)), AT, BT, CT, rho,
                            rho * rho, 2 * Kx, Kx - Kmc, -1, -h, fak=np.exp(-kc * h), D=DT)
    La = y1[:N] * zp1 - p1[:N] * z1 + y2[:N] * zp2 - p2[:N] * z2
    Lb = y1[N:] * zp1 - p1[N:] * z1 + y2[N:] * zp2 - p2[N:] * z2
    aus, o = [], 0
    for r_ in rho_listen:
        aus.append((La[o:o + len(r_)], Lb[o:o + len(r_)]))
        o += len(r_)
    return aus


def _gs2(Z, N):
    a = np.stack([v[:N] for v in Z], 0)
    b = np.stack([v[N:] for v in Z], 0)
    a = a / np.sqrt(np.sum(np.abs(a) ** 2, 0))
    b = b - np.sum(np.conj(a) * b, 0) * a
    b = b / np.sqrt(np.sum(np.abs(b) ** 2, 0))
    return tuple(np.concatenate([a[k], b[k]]) for k in range(4))


def D_komplex(L, rhos, n_gs=4):
    rho = np.atleast_1d(np.asarray(rhos, dtype=complex))
    N = rho.size
    rr = np.concatenate([rho, rho])
    q2 = rr * rr
    z0 = np.zeros(2 * N, dtype=complex)
    p1 = z0.copy()
    p1[N:] = 1.0
    p2 = z0.copy()
    p2[:N] = 1.0
    y = _rk4((z0.copy(), z0.copy(), p1, p2), L["Al"], L["Bl"], L["Cl"], rr, q2, 0, L["Km"], 1, L["h"], D=L["Dl"])
    kc = np.sqrt(1.0 - (rho - L["Omega"]) ** 2)
    q = np.sqrt((rho + L["Omega"]) ** 2 - 1.0 + L["c_asym"] * (4.0 * (rho + L["Omega"]) ** 2 - 2.0) / L["R"])
    kc = kc - L["c_asym"] * (4.0 * (rho - L["Omega"]) ** 2 - 2.0) / (2.0 * kc * L["R"])
    one, nul = np.ones(N, dtype=complex), np.zeros(N, dtype=complex)
    Z = (np.concatenate([one, nul]), np.concatenate([nul, one]), np.concatenate([-kc, nul]),
         np.concatenate([nul, 1j * q]))
    k = L["K"]
    rest = L["K"] - L["Km"]
    while rest > 0:
        n = min(n_gs, rest)
        Z = _rk4(Z, L["Al"], L["Bl"], L["Cl"], rr, q2, 2 * k, n, -1, -L["h"], D=L["Dl"])
        k -= n
        rest -= n
        Z = _gs2(Z, N)
    M = np.empty((N, 4, 4), dtype=complex)
    for c, (v, sl) in enumerate(((y, slice(0, N)), (y, slice(N, 2 * N)), (Z, slice(0, N)), (Z, slice(N, 2 * N)))):
        col = np.stack([w[sl] for w in v], 1)
        if c < 2:
            col = col / np.sqrt(np.sum(np.abs(col) ** 2, 1))[:, None]
        M[:, :, c] = col
    return np.linalg.det(M)


def pole(L, starts, iters=25, tol=1e-11, delta=1e-7, schritt_max=0.01):
    rho = np.array(starts, dtype=complex)
    n = len(rho)
    konv = np.zeros(n, dtype=bool)
    it_n = np.zeros(n, dtype=int)
    for it in range(iters):
        akt = np.nonzero(~konv)[0]
        if len(akt) == 0:
            break
        e = rho[akt]
        D = D_komplex(L, np.concatenate([e, e + delta, e + 1j * delta]))
        m = len(akt)
        d0, dx, dy = D[:m], D[m:2 * m], D[2 * m:]
        j11, j21 = (dx - d0).real / delta, (dx - d0).imag / delta
        j12, j22 = (dy - d0).real / delta, (dy - d0).imag / delta
        dd = j11 * j22 - j12 * j21
        ok = np.isfinite(dd) & (dd != 0)
        dd = np.where(ok, dd, 1.0)
        st = np.where(ok, (-(j22 * d0.real - j12 * d0.imag) + 1j * (-(-j21 * d0.real + j11 * d0.imag))) / dd, 0.0)
        gross = np.abs(st) > schritt_max
        st = np.where(gross, st * schritt_max / np.maximum(np.abs(st), 1e-300), st)
        rho[akt] = e + st
        it_n[akt] = it + 1
        konv[akt] = ok & (np.abs(st) < tol)
    Dend = np.abs(D_komplex(L, rho)) if n else np.zeros(0)
    return rho, konv, Dend, it_n


# ----------------------------------------------------------------------------------------------------------------------
# Nullstellen von L(y_b), s, Umlauf (unveraendert aus afm_bic.py)
# ----------------------------------------------------------------------------------------------------------------------

def wurzeln(L, rho, La, Lb, n_fein=100, stufen=1):
    sg = np.sign(Lb)
    idx = np.nonzero(sg[:-1] * sg[1:] < 0)[0]
    kl = [(float(rho[i]), float(rho[i + 1]), float(Lb[i]), float(Lb[i + 1])) for i in idx]
    for _ in range(stufen):
        if not kl:
            break
        pts = np.concatenate([np.linspace(a, b, n_fein + 1)[1:-1] for a, b, _, _ in kl])
        _, lbs, _ = W_reell(L, pts)
        m = n_fein - 1
        neu = []
        for q, (a, b, fa, fb) in enumerate(kl):
            xs_ = np.concatenate([[a], pts[q * m:(q + 1) * m], [b]])
            fs_ = np.concatenate([[fa], lbs[q * m:(q + 1) * m], [fb]])
            for t in np.nonzero(np.sign(fs_[:-1]) * np.sign(fs_[1:]) < 0)[0]:
                neu.append((float(xs_[t]), float(xs_[t + 1]), float(fs_[t]), float(fs_[t + 1])))
        kl = neu
    if not kl:
        return []
    rts = [a - fa * (b - a) / (fb - fa) for a, b, fa, fb in kl]
    la, lb, _ = W_reell(L, rts)
    aus = []
    for (a, b, fa, fb), r_, sa, sb in zip(kl, rts, la, lb):
        aus.append({"rho": float(r_), "s": float(sa), "lb_rest": float(sb), "breite": float(b - a),
                    "richtung": 1 if fb > fa else -1, "steigung_lb": float((fb - fa) / (b - a))})
    return aus


def umlauf(W):
    W = np.asarray(W, dtype=complex)
    sp = np.angle(np.roll(W, -1) * np.conj(W))
    return float(sp.sum() / (2.0 * PI)), float(np.abs(sp).max()), int(np.argmax(np.abs(sp)))


def _spruenge(w):
    w = np.asarray(w, dtype=complex)
    return np.abs(np.angle(w[1:] * np.conj(w[:-1])))


def rechteck(modell, kap, h, xl, xr, rlo, rhi, Ll, Lr, prot, budget, links=None, rechts=None, mitte=None,
             n_rho=41, runden_x=8, runden_r=40, max_prof=60):
    t0 = uhr()

    def seite(L, vorgabe):
        if vorgabe is not None:
            return [float(v) for v in vorgabe[0]], [complex(v) for v in vorgabe[1]]
        r_ = np.linspace(rlo, rhi, n_rho)
        la, lb, _ = W_reell(L, r_)
        return [float(v) for v in r_], [complex(a_, b_) for a_, b_ in zip(la, lb)]
    rl, wl = seite(Ll, links)
    rr_, wr = seite(Lr, rechts)
    xs = [xl, xr]
    wu = [wl[0], wr[0]]
    wo = [wl[-1], wr[-1]]
    luecken = []

    def einfuegen(neu):
        offen = [(x, L) for x, L, ecken in neu if L is not None and ecken is None]
        berechnet = {}
        if offen:
            for (x, L), (la, lb) in zip(offen, W_multi([L for _, L in offen], [[rlo, rhi]] * len(offen))):
                berechnet[x] = (complex(la[0], lb[0]), complex(la[1], lb[1]))
        for x, L, ecken in neu:
            if L is None:
                luecken.append(x)
                continue
            if ecken is None:
                ecken = berechnet[x]
            k = int(np.searchsorted(xs, x))
            xs.insert(k, x)
            wu.insert(k, ecken[0])
            wo.insert(k, ecken[1])
    if mitte:
        einfuegen([m for m in mitte if xl < m[0] < xr])
    n_prof = 0
    for _ in range(runden_x):
        sp = np.maximum(_spruenge(wu), _spruenge(wo))
        neu_x = [xs[i] + (xs[i + 1] - xs[i]) * q / 4.0 for i in np.nonzero(sp > SPRUNG)[0]
                 if not any(xs[i] < g < xs[i + 1] for g in luecken) for q in (1, 2, 3)]
        if not neu_x or n_prof + len(neu_x) > max_prof or not budget.ok("Rechteck: neue Profile", 30.0):
            break
        Ls = profile_lin(modell, kap, neu_x, h, prot)
        n_prof += len(neu_x)
        einfuegen([(x, L, None) for x, L in zip(neu_x, Ls)])
    for L, r_, w_ in ((Ll, rl, wl), (Lr, rr_, wr)):
        for _ in range(runden_r):
            sp = _spruenge(w_)
            idx = np.nonzero(sp > SPRUNG)[0]
            if len(idx) == 0 or not budget.ok("Rechteck: rho-Seite", 10.0):
                break
            mids = [0.5 * (r_[i] + r_[i + 1]) for i in idx]
            la, lb, _ = W_reell(L, mids)
            for i, m_, a_, b_ in sorted(zip(idx, mids, la, lb), reverse=True):
                r_.insert(i + 1, m_)
                w_.insert(i + 1, complex(a_, b_))
    pfad = wu + wr[1:] + wo[::-1][1:] + wl[::-1][1:-1]
    u, sprung, ks = umlauf(pfad)
    aufl = bool(sprung < SPRUNG and not luecken)
    P = np.asarray(pfad + pfad[:1])
    kr = 0.0
    for k in np.nonzero(np.sign(P[:-1].imag) * np.sign(P[1:].imag) < 0)[0]:
        t = P[k].imag / (P[k].imag - P[k + 1].imag)
        la = P[k].real + t * (P[k + 1].real - P[k].real)
        kr += 0.5 * np.sign(la) * np.sign(P[k + 1].imag - P[k].imag)
    seiten = {"unten": float(_spruenge(wu).max()), "oben": float(_spruenge(wo).max()),
              "rechts": float(_spruenge(wr).max()), "links": float(_spruenge(wl).max())}
    return {"x_lo": xl, "x_hi": xr, "rho_lo": rlo, "rho_hi": rhi, "umlauf_roh": u, "umlauf": int(round(u)),
            "umlauf_kreuzung": float(kr), "max_sprung_seiten": seiten,
            "max_sprung": sprung, "aufgeloest": aufl, "punkte": len(pfad), "x_punkte": len(xs),
            "rho_punkte_links": len(rl), "rho_punkte_rechts": len(rr_), "neue_profile": n_prof,
            "luecken_ungueltig": luecken, "min_absW": float(min(abs(w) for w in pfad)),
            "median_absW": float(np.median(np.abs(pfad))), "zeit": uhr() - t0}


# ----------------------------------------------------------------------------------------------------------------------
# Reihen, Aeste, Lokalisierung (unveraendert aus afm_bic.py)
# ----------------------------------------------------------------------------------------------------------------------

def fenster(x):
    om = math.sqrt(x)
    return 1.0 - om + RAND, 1.0 + om - RAND


def reihe(L, n1, n2, dicht, extra):
    lo, hi = fenster(L["x"])
    teile = [np.linspace(lo, hi, n1)]
    dlo, dhi = max(lo, dicht[0]), min(hi, dicht[1])
    if n2 > 0 and dhi > dlo:
        teile.append(np.linspace(dlo, dhi, n2))
    teile.append(np.array([e for e in extra if lo <= e <= hi]))
    rho = np.unique(np.concatenate(teile))
    t0 = uhr()
    La, Lb, wa = W_reell(L, rho)
    t1 = uhr()
    wz = wurzeln(L, rho, La, Lb)
    absW = np.hypot(La, Lb)
    med = float(np.median(absW))
    for w in wz:
        w["s_rel"] = w["s"] / med
    return {"x": L["x"], "Omega": L["Omega"], "fenster": [lo, hi], "R": L["R"], "r_m": L["r_m"], "K": L["K"],
            "R_w": L["R_w"], "rand_abw": L["rand_abw"], "info": L["info"], "n_rho": int(rho.size),
            "drho_max": float(np.max(np.diff(rho))), "wachstum_max": float(np.max(wa)), "median_absW": med,
            "min_absW": float(np.min(absW)), "wurzeln": wz, "zeit_abtastung": t1 - t0, "zeit_wurzeln": uhr() - t1,
            "_rho": rho, "_La": La, "_Lb": Lb}


def paaren(w1, w2, tol):
    paare = []
    for i, a in enumerate(w1):
        k2 = [(abs(b["rho"] - a["rho"]), j) for j, b in enumerate(w2) if b["richtung"] == a["richtung"]]
        if not k2:
            continue
        d, j = min(k2)
        if d > tol:
            continue
        k1 = [(abs(c["rho"] - w2[j]["rho"]), k) for k, c in enumerate(w1) if c["richtung"] == w2[j]["richtung"]]
        if min(k1)[1] != i:
            continue
        paare.append((i, j))
    return paare


def lokalisieren(modell, kap, h, xa, ra, sa, xb, rb, sb, richtung, prot, budget, iters=10, tol_x=1e-7):
    schritte = []
    xa0, xb0 = xa, xb
    for it in range(iters):
        if not budget.ok(f"Lokalisierung Schritt {it}", 40.0):
            break
        xn = xb - sb * (xb - xa) / (sb - sa) if sb != sa else 0.5 * (xa + xb)
        lo_, hi_ = min(xa, xb), max(xa, xb)
        if not (lo_ < xn < hi_):
            xn = 0.5 * (xa + xb)
        rp = ra + (rb - ra) * (xn - xa) / (xb - xa)
        L = profile_lin(modell, kap, [xn], h, prot)[0]
        if L is None:
            schritte.append({"x": xn, "fehler": "Profil ungueltig"})
            break
        flo, fhi = fenster(xn)
        w = max(4.0 * abs(rb - ra), 2e-3)
        grid = np.linspace(max(flo, rp - w), min(fhi, rp + w), 401)
        La, Lb, _ = W_reell(L, grid)
        wz = [v for v in wurzeln(L, grid, La, Lb) if v["richtung"] == richtung]
        if not wz:
            schritte.append({"x": xn, "rho_pred": rp, "fehler": "Ast verloren"})
            break
        v = min(wz, key=lambda q: abs(q["rho"] - rp))
        sn, rn = v["s"], v["rho"]
        schritte.append({"x": xn, "rho": rn, "s": sn, "rho_pred": rp, "lb_rest": v["lb_rest"]})
        if sn * sb < 0:
            xa, sa, ra = xb, sb, rb
        else:
            sa = 0.5 * sa
        xb, sb, rb = xn, sn, rn
        if abs(xb - xa) < tol_x or sn == 0.0:
            break
    if sb == sa:
        xs_, rs_ = xb, rb
    else:
        t = sb / (sb - sa)
        xs_ = xb + t * (xa - xb)
        rs_ = rb + t * (ra - rb)
    steig = (rb - ra) / (xb - xa) if xb != xa else 0.0
    return {"x_stern": float(xs_), "rho_stern": float(rs_), "klammer_x": [float(min(xa, xb)), float(max(xa, xb))],
            "klammer_breite": float(abs(xb - xa)), "steigung_rho_x": float(steig), "schritte": schritte,
            "start": [xa0, xb0]}


def ohne_arrays(rw):
    return {k: v for k, v in rw.items() if not k.startswith("_")}


def ecken_aus(rw, lo, hi):
    if rw is None:
        return None
    r = rw["_rho"]
    i1 = int(np.argmin(np.abs(r - lo)))
    i2 = int(np.argmin(np.abs(r - hi)))
    if abs(r[i1] - lo) > 1e-14 or abs(r[i2] - hi) > 1e-14:
        return None
    return (complex(rw["_La"][i1], rw["_Lb"][i1]), complex(rw["_La"][i2], rw["_Lb"][i2]))


# ----------------------------------------------------------------------------------------------------------------------
# Kommando familie (wie afm_bic.cmd_familie; Mitglieder = Zeilen omega^2 aus --x)
# ----------------------------------------------------------------------------------------------------------------------

def _wechsel(alle, tol):
    """Q-STERN-2: s-Wechsel zwischen benachbarten Reihen (gepaarte Nullstellen gleicher Richtung), wie qstern.py."""
    wechsel = []
    ungepaart = []
    for r1, r2 in zip(alle, alle[1:]):
        pa = paaren(r1["wurzeln"], r2["wurzeln"], tol)
        gi = {i for i, _ in pa}
        gj = {j for _, j in pa}
        ungepaart.append({"x1": r1["x"], "x2": r2["x"], "n1": len(r1["wurzeln"]), "n2": len(r2["wurzeln"]),
                          "gepaart": len(pa), "rho_ungepaart_1": [w["rho"] for k, w in enumerate(r1["wurzeln"]) if k not in gi],
                          "rho_ungepaart_2": [w["rho"] for k, w in enumerate(r2["wurzeln"]) if k not in gj]})
        for i, j in pa:
            w1, w2 = r1["wurzeln"][i], r2["wurzeln"][j]
            if w1["s"] * w2["s"] < 0:
                wechsel.append({"x1": r1["x"], "rho1": w1["rho"], "s1": w1["s"], "x2": r2["x"], "rho2": w2["rho"],
                                "s2": w2["s"], "richtung": w1["richtung"]})
    return wechsel, ungepaart


def _wechsel_im_fenster(w):
    return (FENSTER_X[0] <= 0.5 * (w["x1"] + w["x2"]) <= FENSTER_X[1]
            and FENSTER_R[0] <= 0.5 * (w["rho1"] + w["rho2"]) <= FENSTER_R[1])


def cmd_familie(a, erg, zeilen, sichern, npz):
    budget = Budget(a.budget)
    modell = a.modell
    kap = None
    h = a.h
    if a.x:
        xs = sorted(float(v) for v in a.x.split(","))
    elif modell == "kg":
        xs = KG_X
    else:
        raise ValueError("--x fehlt")
    erg.update({"modell": modell, "band": a.band, "h": h, "x_mitglieder": xs, "alpha": ALPHA, "r_fak": R_FAK,
                "quelle": QUELLE, "psi": PSI})
    prot = []
    Ls = profile_lin(modell, kap, xs, h, prot)
    zeilen += prot
    prot.clear()
    sichern()
    fen = [fenster(x) for x in xs]
    reihen = []
    erg["mitglieder"] = reihen
    for i, (x, L) in enumerate(zip(xs, Ls)):
        if L is None:
            reihen.append({"x": x, "gueltig": False})
            sichern()
            continue
        extra = list(fen[i - 1]) if i > 0 else []
        rw = reihe(L, a.n1, a.n2, (a.dicht_lo, a.dicht_hi), extra)
        rw["gueltig"] = True
        rw["mitglied"] = True
        reihen.append(rw)
        npz[f"m{i}_rho"], npz[f"m{i}_La"], npz[f"m{i}_Lb"] = rw["_rho"], rw["_La"], rw["_Lb"]
        zeilen.append(f"Mitglied x = omega^2 = {x:.6f} (omega {L['Omega']:.6f}, f0 {L['info']['f0']:.6f}, "
                      f"2|Phi(0)| {L['info']['kompaktheit']:.5f}, Phi(R_w) {L['info']['Phi_Rw']:.5f}, "
                      f"c {L['info']['c_asym']:.5f}, Phi-It. {L['info']['phi_iter']}): "
                      f"R = {L['R']:.2f}, r_m = {L['r_m']:.2f}, R_w = {L['R_w']:.3f}, "
                      f"Rand-Abw. {L['rand_abw']:.1e}, {rw['n_rho']} rho-Punkte (max Abstand {rw['drho_max']:.1e}), "
                      f"Wachstum {rw['wachstum_max']:.1e}, {len(rw['wurzeln'])} Nullstellen von L(y_b): "
                      + "; ".join(f"rho {w['rho']:.7f} s {w['s']:+.3e} (rel {w['s_rel']:+.1e}, {w['richtung']:+d})"
                                  for w in rw["wurzeln"]) + f"; {rw['zeit_abtastung']:.1f} + {rw['zeit_wurzeln']:.1f} s")
        sichern()
    # Q-STERN-2: Vorzeichenwechsel aus den Zeilen, danach sofort Lokalisierung und kleines Rechteck (Karte:
    # Lokalisierung zuerst); Kandidaten im Fenster zuerst
    wechsel, ungepaart = _wechsel([rw for rw in reihen if rw.get("gueltig")], a.ast_tol)
    erg["paarung"] = ungepaart
    erg["vorzeichenwechsel"] = wechsel
    zeilen.append(f"Vorzeichenwechsel von s aus den Zeilen (Ast-Toleranz {a.ast_tol}): {len(wechsel)}")
    for w in wechsel:
        zeilen.append(f"  zwischen omega^2 {w['x1']:.7f} (rho {w['rho1']:.6f}, s {w['s1']:+.3e}) und {w['x2']:.7f} "
                      f"(rho {w['rho2']:.6f}, s {w['s2']:+.3e}), Richtung {w['richtung']:+d}")
    n_ung = sum(len(u["rho_ungepaart_1"]) + len(u["rho_ungepaart_2"]) for u in ungepaart)
    zeilen.append(f"Ungepaarte Nullstellen (alle Zeilenpaare zusammen): {n_ung}")
    sichern()
    kand = []
    erg["kandidaten"] = kand
    for w in sorted(wechsel, key=lambda q: 0 if _wechsel_im_fenster(q) else 1)[:a.max_kand]:
        if not budget.ok("Lokalisierung", 90.0):
            kand.append({"wechsel": w, "fehler": "Zeit"})
            break
        lok = lokalisieren(modell, kap, h, w["x1"], w["rho1"], w["s1"], w["x2"], w["rho2"], w["s2"], w["richtung"],
                           prot, budget)
        zeilen += prot
        prot.clear()
        e = {"wechsel": w, "lokal": lok}
        kand.append(e)
        zeilen.append(f"Lokalisiert: omega*^2 = {lok['x_stern']:.8f}, rho* = {lok['rho_stern']:.8f} (Klammer "
                      f"{lok['klammer_breite']:.1e}, {len(lok['schritte'])} Schritte, {uhr():.0f} s)")
        sichern()
        if not budget.ok("Rechteck", 60.0):
            e["rechteck"] = {"fehler": "Zeit"}
            continue
        dx = a.rdx
        drho = min(max(a.rdrho, 3.0 * abs(lok["steigung_rho_x"]) * dx), 0.02)
        xc, rc = lok["x_stern"], lok["rho_stern"]
        rlo, rhi = max(rc - drho, fenster(xc - dx)[0]), min(rc + drho, fenster(xc - dx)[1])
        Lr = profile_lin(modell, kap, [xc - dx, xc + dx] + [xc + dx * (2.0 * k / (a.r_nx - 1) - 1.0)
                                                           for k in range(1, a.r_nx - 1)], h, prot)
        zeilen += prot
        prot.clear()
        if Lr[0] is None or Lr[1] is None:
            e["rechteck"] = {"fehler": "Profil ungueltig"}
            continue
        mitte = [(xc + dx * (2.0 * k / (a.r_nx - 1) - 1.0), L, None) for k, L in zip(range(1, a.r_nx - 1), Lr[2:])]
        ru = rechteck(modell, kap, h, xc - dx, xc + dx, rlo, rhi, Lr[0], Lr[1], prot, budget, mitte=mitte)
        zeilen += prot
        prot.clear()
        e["rechteck"] = ru
        zeilen.append(f"  Rechteck omega^2 {xc - dx:.7f} .. {xc + dx:.7f}, rho {rlo:.6f} .. {rhi:.6f}: Umlauf "
                      f"{ru['umlauf_roh']:+.4f} (Kreuzungszaehlung {ru['umlauf_kreuzung']:+.1f}), groesster Sprung "
                      f"{ru['max_sprung']:.3f} rad, aufgeloest {ru['aufgeloest']}, "
                      f"{ru['punkte']} Punkte, min|W|/median {ru['min_absW'] / ru['median_absW']:.1e}, {uhr():.0f} s")
        mi = Lr[1 + (a.r_nx - 1) // 2]
        e["kompaktheit_ort"] = None if mi is None else {"x": mi["x"], "kompaktheit": mi["info"]["kompaktheit"],
                                                        "Phi0": mi["info"]["Phi0"], "Phi_Rw": mi["info"]["Phi_Rw"],
                                                        "c_asym": mi["info"]["c_asym"]}
        if PSI == "voll" and ALPHA > 0.0 and mi is not None:
            try:
                e["K5"] = k5_voll(mi, rc)
                zeilen.append(f"  K5 an {mi['x']:.8f} / {rc:.8f}: Rest relativ {e['K5']['rest_rel']:.2e}, "
                              f"sigma_min/sigma_max {e['K5']['sv_verh']:.2e}, max|u| {e['K5']['u_max']:.3e}, "
                              f"max|y| {e['K5']['y_max']:.3e}")
            except Exception as ex:          # K5 darf den Lauf nicht beenden
                e["K5"] = {"fehler": repr(ex)}
        sichern()
    zw = []
    for i in range(len(xs) - 1):
        if Ls[i] is None or Ls[i + 1] is None:
            continue
        for k in range(1, a.n_mid + 1):
            zw.append((i, xs[i] + (xs[i + 1] - xs[i]) * k / (a.n_mid + 1)))
    zw_reihen = {}
    if zw and budget.ok("Zwischenreihen", 60.0):
        Lz = profile_lin(modell, kap, [x for _, x in zw], h, prot)
        zeilen += prot
        prot.clear()
        for (i, x), L in zip(zw, Lz):
            if L is None:
                zw_reihen.setdefault(i, []).append((x, None, None))
                continue
            if not budget.ok("Zwischenreihe", 30.0):
                zw_reihen.setdefault(i, []).append((x, L, None))
                continue
            rw = reihe(L, a.n_zw, 0, (a.dicht_lo, a.dicht_hi), list(fen[i]))
            rw["gueltig"] = True
            rw["mitglied"] = False
            rw["streifen"] = i
            zw_reihen.setdefault(i, []).append((x, L, rw))
        erg["zwischenreihen"] = [ohne_arrays(rw) for i in sorted(zw_reihen) for (_, _, rw) in zw_reihen[i]
                                 if rw is not None]
        zeilen.append(f"Zwischenreihen: {len(zw)} Profile, {len(erg['zwischenreihen'])} abgetastet ({a.n_zw} rho-Punkte)")
        sichern()
    streifen = []
    erg["streifen"] = streifen
    for i in range(len(xs) - 1):
        if Ls[i] is None or Ls[i + 1] is None:
            streifen.append({"i": i, "fehler": "Profil ungueltig"})
            continue
        if not budget.ok(f"Streifen {i}", 30.0):
            streifen.append({"i": i, "fehler": "Zeit"})
            sichern()
            continue
        lo, hi = fen[i]
        r1, La1, Lb1 = reihen[i]["_rho"], reihen[i]["_La"], reihen[i]["_Lb"]
        r2, La2, Lb2 = reihen[i + 1]["_rho"], reihen[i + 1]["_La"], reihen[i + 1]["_Lb"]
        m2 = (r2 >= lo - 1e-15) & (r2 <= hi + 1e-15)
        mitte = [(x, L, ecken_aus(rw, lo, hi)) for (x, L, rw) in zw_reihen.get(i, [])]
        e = rechteck(modell, kap, h, xs[i], xs[i + 1], lo, hi, Ls[i], Ls[i + 1], prot, budget,
                     links=(r1, La1 + 1j * Lb1), rechts=(r2[m2], La2[m2] + 1j * Lb2[m2]), mitte=mitte)
        zeilen += prot
        prot.clear()
        e["i"] = i
        streifen.append(e)
        zeilen.append(f"Streifen {i}: omega^2 {xs[i]:.6f} .. {xs[i + 1]:.6f}, rho {lo:.4f} .. {hi:.4f}: Umlauf "
                      f"{e['umlauf_roh']:+.4f} (Kreuzungszaehlung {e['umlauf_kreuzung']:+.1f}), groesster Sprung "
                      f"{e['max_sprung']:.3f} rad {json.dumps({k: round(v, 3) for k, v in e['max_sprung_seiten'].items()})}, "
                      f"aufgeloest {e['aufgeloest']}, {e['punkte']} Punkte ({e['x_punkte']} in omega^2, "
                      f"{e['neue_profile']} neue Profile), min|W|/median {e['min_absW'] / e['median_absW']:.1e}, "
                      f"{e['zeit']:.1f} s")
        sichern()
    # Q-STERN-2: s-Wechsel ueber Zeilen und Zwischenreihen nur noch zur Dokumentation (Lokalisierung lief vorher)
    alle = [rw for rw in reihen if rw.get("gueltig")]
    for i in zw_reihen:
        alle += [rw for (_, _, rw) in zw_reihen[i] if rw is not None]
    alle.sort(key=lambda q: q["x"])
    wechsel2, _ = _wechsel(alle, a.ast_tol)
    erg["vorzeichenwechsel_alle"] = wechsel2
    zeilen.append(f"Vorzeichenwechsel von s mit Zwischenreihen ({len(alle)} Reihen): {len(wechsel2)}")
    for w in wechsel2:
        zeilen.append(f"  zwischen omega^2 {w['x1']:.7f} (rho {w['rho1']:.6f}, s {w['s1']:+.3e}) und {w['x2']:.7f} "
                      f"(rho {w['rho2']:.6f}, s {w['s2']:+.3e})")
    sichern()
    if a.pole == "ja":
        for i, (rw, L) in enumerate(zip(reihen, Ls)):
            if not rw.get("gueltig") or not rw["wurzeln"]:
                continue
            if not budget.ok(f"Pole Mitglied {i}", 60.0):
                rw["pole_fehler"] = "Zeit"
                continue
            t0 = uhr()
            ws = [w for w in rw["wurzeln"] if w["rho"] > 1.0 - rw["Omega"] + 0.02]
            if not ws:
                continue
            st = [complex(w["rho"], -1e-6) for w in ws]
            rho_p, konv, absd, itn = pole(L, st, iters=15)
            for w, p_, k_, d_, n_ in zip(ws, rho_p, konv, absd, itn):
                w["pol"] = complex(p_)
                w["Gamma"] = float(-p_.imag)
                w["pol_konvergiert"] = bool(k_)
                w["pol_absD"] = float(d_)
                w["pol_iter"] = int(n_)
            rw["zeit_pole"] = uhr() - t0
            zeilen.append(f"Pole x = {rw['x']:.6f} ({rw['zeit_pole']:.1f} s): " + "; ".join(
                f"{w['pol'].real:.7f} {w['pol'].imag:+.2e}i ({'k' if w['pol_konvergiert'] else 'n'})" for w in ws))
            sichern()
    erg["budget_entfallen"] = budget.entfallen


# ----------------------------------------------------------------------------------------------------------------------
# Schritt 0: nackter geschlossener Kanal (C = 0): -y'' + dp(r) y = E y, E = (rho - omega)^2, Dirichlet 0 und R_max
# ----------------------------------------------------------------------------------------------------------------------

def verlaengern(p, R_max):
    r, phi = p["r"], p["phi"]
    hp = p["hp"]
    J = int(math.ceil(R_max / hp))
    if J + 1 <= len(r):
        return r[:J + 1], phi[:J + 1]
    rr = np.arange(J + 1) * hp
    ph = np.empty(J + 1)
    ph[:len(r)] = phi
    kap = p["kappa0"]
    Atl = phi[-1] * r[-1] * math.exp(kap * r[-1])
    ph[len(r):] = Atl * np.exp(-kap * rr[len(r):]) / rr[len(r):]
    return rr, ph


def nackt(m, p, R_max):
    from scipy.linalg import eigh_tridiagonal
    hp = p["hp"]
    r, f = verlaengern(p, R_max)
    S = f * f
    d = 2.0 / hp ** 2 + dp_(m, S[1:-1])
    off = -np.ones(len(d) - 1) / hp ** 2
    E, V = eigh_tridiagonal(d, off, select="v", select_range=(-1e9, 1.0))
    ri = r[1:-1]
    aus = []
    for k in range(len(E)):
        y2 = V[:, k] ** 2
        s = float(np.sum(y2))
        aus.append({"k": k, "E": float(E[k]), "r_spitze": float(ri[int(np.argmax(y2))]),
                    "r_mittel": float(np.sum(ri * y2) / s), "P_laenge": float(s * s / np.sum(y2 * y2) * hp),
                    "anteil_r_lt_Rw": float(np.sum(y2[ri < p["R_w"]]) / s)})
    return aus


def cmd_schritt0(a, erg, zeilen, sichern, npz):
    xs = [float(v) for v in a.x.split(",")]
    hp = 0.5 * a.h
    prot = []
    prs = profile(a.modell, xs, hp, prot=prot)
    zeilen += prot
    erg.update({"modell": a.modell, "h": a.h, "hp": hp, "x": xs, "zeilen": []})
    for x, p in zip(xs, prs):
        if p is None:
            erg["zeilen"].append({"x": x, "gueltig": False})
            continue
        om = math.sqrt(x)
        R1 = max(3.0 * p["R_w"], p["R_w"] + a.r_extra)
        z1 = nackt(a.modell, p, R1)
        z2 = nackt(a.modell, p, R1 + 20.0)
        dE = [abs(u["E"] - v["E"]) for u, v in zip(z1, z2)]
        zust = []
        for z in z1:
            E = z["E"]
            sq = math.sqrt(E) if E >= 0 else float("nan")
            rp, rm_ = om + sq, om - sq
            z.update({"rho_plus": rp, "rho_minus": rm_,
                      "eingebettet_plus": bool(1.0 - om < rp < 1.0 + om),
                      "eingebettet_minus": bool(1.0 - om < rm_ < 1.0 + om)})
            zust.append(z)
        e = {"x": x, "omega": om, "gueltig": True, "f0": p["f0"], "R_w": p["R_w"], "R_max": R1, "Q": p["Q"],
             "E_ball": p["E"], "n_gebunden": len(z1), "n_gebunden_R_plus_20": len(z2),
             "max_dE_R_plus_20": max(dE) if dE else 0.0, "zustaende": zust,
             "n_eingebettet": sum(1 for z in zust if z["eingebettet_plus"] or z["eingebettet_minus"]),
             "min_dp": float(dp_(a.modell, p["phi"][0] ** 2))}
        erg["zeilen"].append(e)
        zeilen.append(f"x = omega^2 = {x:.4f} (omega {om:.5f}): f0 = {p['f0']:.5f}, R_w = {p['R_w']:.3f}, "
                      f"dp(0) = {e['min_dp']:.4f}, Fenster ({1 - om:.4f}, {1 + om:.4f}), gebundene Zustaende E < 1: "
                      f"{len(z1)} (R_max + 20: {len(z2)}, max |dE| {e['max_dE_R_plus_20']:.1e}); "
                      + "; ".join(f"k={z['k']} E={z['E']:.6f} rho+={z['rho_plus']:.6f}"
                                  f"{' (eingebettet)' if z['eingebettet_plus'] else ''} rho-={z['rho_minus']:.6f}"
                                  f"{' (eingebettet)' if z['eingebettet_minus'] else ''} r_spitze={z['r_spitze']:.2f} "
                                  f"P={z['P_laenge']:.2f}" for z in zust))
        sichern()


# ----------------------------------------------------------------------------------------------------------------------
# K2: Q(omega), E(omega) des Balls auf zwei Gittern (h/2 und h/4 als Profilschritt)
# ----------------------------------------------------------------------------------------------------------------------

def cmd_k2(a, erg, zeilen, sichern, npz):
    """Q-STERN K2: Hintergrund auf zwei Gittern (Profilschritt h/2 und h/4). omega ist Vorgabe (gleich), verglichen
    werden Q, E (Masse der Quelle) und Phi(0) auf 1e-6 relativ."""
    xs = [float(v) for v in a.x.split(",")]
    prot = []
    p1 = profile(a.modell, xs, 0.5 * a.h, prot=prot)
    zeilen += prot
    prot.clear()
    sichern()
    p2 = profile(a.modell, xs, 0.25 * a.h, prot=prot)
    zeilen += prot
    tab = []
    ok = True
    for x, u, v in zip(xs, p1, p2):
        if u is None or v is None:
            tab.append({"x": x, "gueltig": False})
            ok = False
            continue
        dQ = abs(u["Q"] - v["Q"]) / abs(v["Q"])
        dE = abs(u["E"] - v["E"]) / abs(v["E"])
        dP = abs(u["Phi0"] - v["Phi0"]) / abs(v["Phi0"]) if v["Phi0"] != 0.0 else abs(u["Phi0"])
        b = bool(dQ < 1e-6 and dE < 1e-6 and dP < 1e-6)
        ok &= b
        tab.append({"x": x, "Q_h": u["Q"], "Q_h2": v["Q"], "dQ_rel": dQ, "E_h": u["E"], "E_h2": v["E"], "dE_rel": dE,
                    "Phi0_h": u["Phi0"], "Phi0_h2": v["Phi0"], "dPhi0_rel": dP, "f0_h": u["f0"], "f0_h2": v["f0"],
                    "R_w": v["R_w"], "Phi_Rw": v["Phi_Rw"], "kompaktheit": v["kompaktheit"], "c_asym": v["c_asym"],
                    "phi_iter": [u["phi_iter"], v["phi_iter"]], "eta_schwanz": v["eta_schwanz"], "bestanden": b})
        zeilen.append(f"K2 x = {x:.4f}: Q = {u['Q']:.10e} / {v['Q']:.10e} (rel {dQ:.1e}), E = {u['E']:.10e} / "
                      f"{v['E']:.10e} (rel {dE:.1e}), Phi(0) = {u['Phi0']:.10e} / {v['Phi0']:.10e} (rel {dP:.1e}), "
                      f"f0 = {u['f0']:.8f} / {v['f0']:.8f}, R_w = {v['R_w']:.3f}, Phi(R_w) = {v['Phi_Rw']:.5f}, "
                      f"2|Phi(0)| = {v['kompaktheit']:.5f}, c = {v['c_asym']:.5f}, It. {u['phi_iter']}/{v['phi_iter']}"
                      f" -> {'ok' if b else 'VERFEHLT'}")
    erg.update({"modell": a.modell, "alpha": ALPHA, "quelle": QUELLE, "h": a.h, "profilschritte": [0.5 * a.h, 0.25 * a.h],
                "tabelle": tab, "K2_bestanden": bool(ok)})
    zeilen.append(f"K2 ({a.modell}, alpha {ALPHA}, Profilschritte {0.5 * a.h} und {0.25 * a.h}): "
                  f"{'bestanden' if ok else 'VERFEHLT'}")
    sichern()


# ----------------------------------------------------------------------------------------------------------------------
# Kommando auswertung (bindende Regel aus q-stern/KARTE.md, Umsetzung PLAN.md Abschnitt Auswertung)
# ----------------------------------------------------------------------------------------------------------------------

FENSTER_X = (0.74, 0.80)     # Q-STERN-2 (Karte)
FENSTER_R = (1.65, 1.80)
K1_UMLAUF = -1                # Q-STERN-2b: Umlauf der K1-Stelle bei alpha = 0 (n = 1: -1), aus --k1-umlauf


def _im_fenster(x, r):
    return FENSTER_X[0] <= x <= FENSTER_X[1] and FENSTER_R[0] <= r <= FENSTER_R[1]


def cmd_auswertung(a, erg, zeilen, sichern, npz):
    laeufe = []
    for p in sorted(glob.glob(os.path.join(a.aus, "*.json"))):
        if os.path.basename(p).startswith("auswertung"):
            continue
        d = json.load(open(p))
        if "mitglieder" in d:
            d["_datei"] = os.path.basename(p)
            laeufe.append(d)
    zeilen.append(f"Auswertung: {len(laeufe)} Laeufe: " + ", ".join(d["_datei"] for d in laeufe))

    def gruppe(al, h, rf, ps="voll"):
        return [d for d in laeufe if abs(d["alpha"] - al) < 1e-15 and abs(d["h"] - h) < 1e-15
                and abs(d["r_fak"] - rf) < 1e-15 and d.get("quelle", "rho") == "rho" and d.get("psi", "voll") == ps]

    def treffer(ds):
        aus = []
        for d in ds:
            for k in d.get("kandidaten", []):
                r = k.get("rechteck", {})
                if "lokal" in k and "umlauf" in r:
                    aus.append({"x": k["lokal"]["x_stern"], "rho": k["lokal"]["rho_stern"], "umlauf": r["umlauf"],
                                "umlauf_roh": r["umlauf_roh"], "aufgeloest": r["aufgeloest"],
                                "max_sprung": r["max_sprung"], "datei": d["_datei"]})
        return aus
    # K1 (alpha = 0)
    k1 = {}
    for h in (0.02, 0.01):
        t = [q for q in treffer(gruppe(0.0, h, 1.0)) if abs(q["x"] - KG_ZIEL[0]) < 1e-4
             and abs(q["rho"] - KG_ZIEL[1]) < 1e-4 and q["aufgeloest"] and q["umlauf"] == K1_UMLAUF]
        k1[h] = t
        zeilen.append(f"K1 h = {h}: {'bestanden' if t else 'VERFEHLT'}; {t}")
    k1_ok = bool(k1[0.02]) and bool(k1[0.01])
    erg["K1"] = {"treffer": k1, "bestanden": k1_ok}
    # K2 je alpha
    k2 = {}
    for p in sorted(glob.glob(os.path.join(a.aus, "k2*.json"))):
        d = json.load(open(p))
        if "alpha" in d and d.get("quelle", "rho") == "rho":
            k2.setdefault(d["alpha"], []).append(bool(d.get("K2_bestanden")))
    erg["K2"] = {str(k): v for k, v in k2.items()}
    zeilen.append(f"K2: {k2}")
    ergebnisse = []
    for al, ps in [(float(v), q) for v in a.alphas.split(",") if v for q in ("voll", "null")]:
        s1, s2, s3 = gruppe(al, 0.02, 1.0, ps), gruppe(al, 0.01, 1.0, ps), gruppe(al, 0.02, 1.5, ps)
        e = {"alpha": al, "psi": ps, "dateien": [[d["_datei"] for d in s] for s in (s1, s2, s3)]}
        k2_ok = bool(k2.get(al)) and all(k2[al])
        t1, t2, t3 = treffer(s1), treffer(s2), treffer(s3)
        e.update({"treffer_h0.02": t1, "treffer_h0.01": t2, "treffer_K3": t3, "K2_bestanden": k2_ok})
        gesehen, k3_verfehlt = [], []
        for u in t1:
            for v in t2:
                if not (u["aufgeloest"] and v["aufgeloest"] and abs(u["umlauf"]) == 1 and abs(v["umlauf"]) == 1
                        and _im_fenster(u["x"], u["rho"]) and _im_fenster(v["x"], v["rho"])
                        and abs(u["x"] - v["x"]) < 1e-4 and abs(u["rho"] - v["rho"]) < 1e-4):
                    continue
                w3 = [q for q in t3 if abs(q["x"] - u["x"]) < 1e-4 and abs(q["rho"] - u["rho"]) < 1e-4]
                if w3:
                    gesehen.append({"h0.02": u, "h0.01": v, "K3": w3[0]})
                elif s3:
                    k3_verfehlt.append({"h0.02": u, "h0.01": v})
                else:
                    k3_verfehlt.append({"h0.02": u, "h0.01": v, "K3": "nicht gerechnet"})
        # Nicht gesehen: beide Stufen, Fenster in omega^2 ganz abgedeckt, kein s-Wechsel im Fenster, alle Streifen
        # aufgeloest mit Umlauf 0
        ng = True
        info = []
        for nm, s in (("h0.02", s1), ("h0.01", s2)):
            xs_ = sorted({round(m["x"], 12) for d in s for m in d.get("mitglieder", []) if m.get("gueltig")})
            ung = [m["x"] for d in s for m in d.get("mitglieder", []) if not m.get("gueltig")]
            st = [q for d in s for q in d.get("streifen", [])]
            st_ok = all("umlauf" in q and q["aufgeloest"] and q["umlauf"] == 0 for q in st)
            vw = [w for d in s for w in d.get("vorzeichenwechsel", [])
                  if FENSTER_X[0] <= 0.5 * (w["x1"] + w["x2"]) <= FENSTER_X[1]
                  and FENSTER_R[0] <= 0.5 * (w["rho1"] + w["rho2"]) <= FENSTER_R[1]]
            deckt = bool(xs_) and xs_[0] <= FENSTER_X[0] + 1e-12 and xs_[-1] >= FENSTER_X[1] - 1e-12
            ok_s = deckt and st_ok and not vw and not ung and len(st) >= len(xs_) - 1
            info.append({"stufe": nm, "zeilen": len(xs_), "x_min": xs_[0] if xs_ else None,
                         "x_max": xs_[-1] if xs_ else None, "ungueltig": ung, "streifen": len(st),
                         "streifen_umlauf_ungleich_0": sum(1 for q in st if q.get("umlauf", 0) != 0),
                         "streifen_nicht_aufgeloest": sum(1 for q in st if not q.get("aufgeloest", False)),
                         "s_wechsel_im_fenster": len(vw), "deckt_fenster": deckt, "nicht_gesehen_ok": ok_s})
            ng &= ok_s
        e.update({"gesehen": gesehen, "k3_verfehlt": k3_verfehlt, "stufen": info})
        if not k1_ok:
            aus_ = "nicht auswertbar (K1 verfehlt)"
        elif not k2_ok:
            aus_ = "nicht auswertbar (K2 verfehlt oder fehlt)"
        elif gesehen:
            aus_ = "Gesehen"
        elif any(isinstance(q, dict) and "K3" not in q for q in k3_verfehlt):
            aus_ = "nicht auswertbar (K3 verfehlt)"
        elif ng and s1 and s2:
            aus_ = "Nicht gesehen"
        else:
            aus_ = "Unentschieden"
        if not (s1 and s2):
            aus_ = "nicht gerechnet" if not (s1 or s2) else aus_
        e["ausgang"] = aus_
        # Kompaktheit und Phi am Ballrand: Zeile naechst der Stelle (sonst Fenstermitte), h = 0,02
        ziel = gesehen[0]["h0.02"]["x"] if gesehen else (t1[0]["x"] if t1 else 0.80)
        ms = [m for d in s1 for m in d.get("mitglieder", []) if m.get("gueltig")]
        if ms:
            m = min(ms, key=lambda q: abs(q["x"] - ziel))
            e["kompaktheit_zeile"] = {"x": m["x"], "kompaktheit": m["info"]["kompaktheit"], "Phi0": m["info"]["Phi0"],
                                      "Phi_Rw": m["info"]["Phi_Rw"], "R_w": m["R_w"], "c_asym": m["info"]["c_asym"]}
        ergebnisse.append(e)
        zeilen.append(f"alpha {al} psi {ps}: Ausgang {aus_}; gesehen {len(gesehen)}; Stufen {json.dumps(jsonfest(info))}")
        for g in gesehen:
            zeilen.append(f"  Stelle h0.02 {g['h0.02']['x']:.8f} / {g['h0.02']['rho']:.8f}, h0.01 {g['h0.01']['x']:.8f} / "
                          f"{g['h0.01']['rho']:.8f}, K3 {g['K3']['x']:.8f} / {g['K3']['rho']:.8f}, Umlauf "
                          f"{g['h0.02']['umlauf']} / {g['h0.01']['umlauf']}, Sprung {g['h0.02']['max_sprung']:.3f} / "
                          f"{g['h0.01']['max_sprung']:.3f}")
        sichern()
    erg["alpha_ergebnisse"] = ergebnisse
    sichern()


def argumente():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kommando", choices=["familie", "schritt0", "k2", "auswertung"])
    ap.add_argument("--modell", choices=["log", "kg", "mix"], default="kg")
    ap.add_argument("--alpha", type=float, default=0.0)
    ap.add_argument("--r-fak", type=float, default=1.0)
    ap.add_argument("--quelle", choices=["rho", "rho3p"], default="rho")
    ap.add_argument("--phi-misch", type=float, default=1.0)
    ap.add_argument("--psi", choices=["voll", "null"], default="voll")
    ap.add_argument("--n-rampe", type=int, default=6)
    ap.add_argument("--alphas", type=str, default="")
    ap.add_argument("--fenster", type=str, default="")         # Q-STERN-2b: "x_lo,x_hi,rho_lo,rho_hi"
    ap.add_argument("--k1-ziel", type=str, default="")         # Q-STERN-2b: "x,rho" der K1-Stelle
    ap.add_argument("--k1-umlauf", type=int, default=-1)       # Q-STERN-2b: Umlauf der K1-Stelle
    ap.add_argument("--t", type=float, default=0.0)
    ap.add_argument("--band", type=str, default="")
    ap.add_argument("--x", type=str, default="")
    ap.add_argument("--h", type=float, default=0.02)
    ap.add_argument("--n1", type=int, default=4000)
    ap.add_argument("--n2", type=int, default=2000)
    ap.add_argument("--dicht-lo", type=float, default=1.5)
    ap.add_argument("--dicht-hi", type=float, default=1.95)
    ap.add_argument("--n-mid", type=int, default=2)
    ap.add_argument("--n-zw", type=int, default=1500)
    ap.add_argument("--ast-tol", type=float, default=0.3)
    ap.add_argument("--max-kand", type=int, default=4)
    ap.add_argument("--rdx", type=float, default=4e-4)
    ap.add_argument("--rdrho", type=float, default=2e-3)
    ap.add_argument("--r-nx", type=int, default=5)
    ap.add_argument("--r-extra", type=float, default=40.0)
    ap.add_argument("--pole", choices=["ja", "nein"], default="nein")
    ap.add_argument("--budget", type=float, default=520.0)
    ap.add_argument("--aus", type=str, default="aus")
    ap.add_argument("--name", type=str, default="")
    return ap.parse_args()


def main():
    global T_MIX, ALPHA, R_FAK, QUELLE, PHI_MISCH, PSI, N_RAMPE, FENSTER_X, FENSTER_R, KG_ZIEL, K1_UMLAUF
    a = argumente()
    PSI = a.psi
    if a.fenster:
        fw = [float(v) for v in a.fenster.split(",")]
        FENSTER_X, FENSTER_R = (fw[0], fw[1]), (fw[2], fw[3])
    if a.k1_ziel:
        KG_ZIEL = tuple(float(v) for v in a.k1_ziel.split(","))
    K1_UMLAUF = int(a.k1_umlauf)
    N_RAMPE = int(a.n_rampe)
    T_MIX = float(a.t)
    ALPHA = float(a.alpha)
    R_FAK = float(a.r_fak)
    QUELLE = a.quelle
    PHI_MISCH = float(a.phi_misch)
    name = a.name or a.kommando
    os.makedirs(a.aus, exist_ok=True)
    zeilen = [f"qstern2b.py {a.kommando} ({name}), Start {jetzt()}", "Argumente: " + json.dumps(vars(a))]
    erg = {"argumente": vars(a), "start": jetzt()}
    npz = {}

    def sichern():
        e = dict(erg)
        e["mitglieder"] = [ohne_arrays(m) for m in erg.get("mitglieder", [])]
        if "mitglieder" not in erg:
            e.pop("mitglieder")
        e["stand"] = jetzt()
        e["laufzeit_bisher"] = uhr()
        tmp = os.path.join(a.aus, f".{name}.json.tmp")
        with open(tmp, "w") as fh:
            json.dump(jsonfest(e), fh, indent=1)
        os.replace(tmp, os.path.join(a.aus, f"{name}.json"))
        with open(os.path.join(a.aus, f"{name}.txt"), "w") as fh:
            fh.write("\n".join(zeilen) + "\n")
    rc = 0
    try:
        {"familie": cmd_familie, "schritt0": cmd_schritt0, "k2": cmd_k2,
         "auswertung": cmd_auswertung}[a.kommando](a, erg, zeilen, sichern, npz)
    except Exception:
        import traceback
        zeilen.append("FEHLER: " + traceback.format_exc())
        erg["fehler"] = traceback.format_exc()
        rc = 1
    zeilen.append(f"Ende {jetzt()}, Laufzeit {uhr():.1f} s")
    erg["ende"] = jetzt()
    erg["laufzeit"] = uhr()
    sichern()
    if npz:
        np.savez_compressed(os.path.join(a.aus, f"{name}-abtastung.npz"), **npz)
    print("\n".join(zeilen))
    return rc


if __name__ == "__main__":
    sys.exit(main())
