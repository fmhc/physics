#!/usr/bin/env python3
"""B-BALL-LEITER (Runde 13 nach v3, explorativ): stille Stellen (W = 0 bei reellem rho) im Q-Ball mit flachem
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


def G_(m, f, x):
    """f'' + (2/r) f' = G(f) = (U'(f^2) - omega^2) f, x = omega^2."""
    return (Up_(m, f * f) - x) * f


def Gs_(m, f, x):
    """dG/df = U' + 2 S U'' - omega^2."""
    S = f * f
    return Up_(m, S) + 2.0 * S * Upp_(m, S) - x


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

def _rk4_prof(m, r, phi, p, hp, x):
    def f(rr, a, b):
        return b, G_(m, a, x) - 2.0 * b / rr
    k1a, k1b = f(r, phi, p)
    k2a, k2b = f(r + 0.5 * hp, phi + 0.5 * hp * k1a, p + 0.5 * hp * k1b)
    k3a, k3b = f(r + 0.5 * hp, phi + 0.5 * hp * k2a, p + 0.5 * hp * k2b)
    k4a, k4b = f(r + hp, phi + hp * k3a, p + hp * k3b)
    return (phi + hp / 6.0 * (k1a + 2 * k2a + 2 * k3a + k4a), p + hp / 6.0 * (k1b + 2 * k2b + 2 * k3b + k4b))


def _start(m, c, x, hp):
    a = G_(m, c, x) / 6.0
    b = Gs_(m, c, x) * a / 20.0
    return c + a * hp * hp + b * hp ** 4, 2.0 * a * hp + 4.0 * b * hp ** 3


def _klassen(m, xs, lo, hi, K, hp, r_max, f_lin):
    t = np.arange(1, K + 1) / (K + 1.0)
    c = lo[:, None] + (hi - lo)[:, None] * t[None, :]
    x = xs[:, None] * np.ones_like(c)
    kap = np.sqrt(1.0 - x)
    phi, p = _start(m, c, x, hp)
    r = hp
    kl = np.zeros(c.shape, dtype=np.int8)
    offen = np.ones(c.shape, dtype=bool)
    n = int(r_max / hp)
    for _ in range(1, n):
        phi, p = _rk4_prof(m, r, phi, p, hp, x)
        r += hp
        ueber = offen & (phi < 0)
        unter = offen & (p > 0) & (phi > 0)
        lin = offen & ~ueber & ~unter & (phi < f_lin * c)
        B = p + phi * (kap + 1.0 / r)
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


def profile(m, xs, hp, K=64, runden=40, r_max=200.0, f_lin=1e-4, f_rand=1e-9, prot=None):
    """Grundzustaende (knotenfrei) fuer x = omega^2. Gitter r_j = j hp. Rueckgabe je x ein dict oder None."""
    xs = np.asarray(xs, dtype=float)
    M = len(xs)
    lo = np.empty(M)
    hi = np.empty(M)
    erw = np.zeros(M, dtype=bool)
    for i, x in enumerate(xs):
        a, b, e = grenzen(m, x)
        lo[i], hi[i], erw[i] = a * (1 + 1e-13), b * (1 - 1e-15), e
    bestaetigt = ~erw
    fehler = [None] * M
    for rd in range(runden):
        c, kl = _klassen(m, xs, lo, hi, K, hp, r_max, f_lin)
        for i in range(M):
            k = kl[i]
            iu = np.where(k == -1)[0]
            io = np.where(k == 1)[0]
            if len(io) == 0 and len(iu) == K:
                lo[i] = c[i, -1]
                if not bestaetigt[i]:
                    hi[i] = 2.0 * hi[i]
                continue
            if len(iu) == 0 and len(io) == K:
                hi[i] = c[i, 0]
                bestaetigt[i] = True
                continue
            if len(iu) == 0 or len(io) == 0:
                fehler[i] = f"keine Klammer (unter {len(iu)}, ueber {len(io)}, Runde {rd})"
                continue
            j = io[0]
            ju = iu[iu < j]
            nlo = c[i, ju[-1]] if len(ju) else lo[i]
            lo[i], hi[i] = nlo, c[i, j]
            bestaetigt[i] = True
        if np.all((hi - lo) <= 4e-16 * hi) and bestaetigt.all():
            break
    cc = np.stack([lo, hi], 1)
    x2 = xs[:, None] * np.ones_like(cc)
    phi, p = _start(m, cc, x2, hp)
    r = hp
    n = int(r_max / hp)
    PH = [cc * 1.0, phi.copy()]
    PP = [np.zeros_like(cc), p.copy()]
    aktiv = np.ones(M, dtype=bool)
    for k in range(1, n):
        phi, p = _rk4_prof(m, r, phi, p, hp, x2)
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
        if fehler[i] is not None or not bestaetigt[i] or not (hi[i] - lo[i] <= 1e-12 * hi[i]):
            if prot is not None:
                prot.append(f"Profil x = {x}: ungueltig ({fehler[i]}, bestaetigt {bool(bestaetigt[i])}, "
                            f"Klammer {hi[i] - lo[i]:.1e})")
            aus.append(None)
            continue
        kap = math.sqrt(1.0 - x)
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
        Atl = ph[jm] * rm * math.exp(kap * rm)
        R_aus = rm + max(0.0, (math.log(ph[jm] / (f_rand * f0)) / kap)) + 2.0
        J = int(math.ceil(R_aus / hp))
        J += J % 2
        rr = np.arange(J + 1) * hp
        phi_g = np.empty(J + 1)
        p_g = np.empty(J + 1)
        phi_g[:jm + 1] = ph[:jm + 1]
        p_g[:jm + 1] = pp[:jm + 1]
        rt = rr[jm + 1:]
        phi_g[jm + 1:] = Atl * np.exp(-kap * rt) / rt
        p_g[jm + 1:] = -phi_g[jm + 1:] * (kap + 1.0 / rt)
        w = np.ones(J + 1)
        w[1:-1:2] = 4.0
        w[2:-1:2] = 2.0
        w *= hp / 3.0
        S = phi_g ** 2
        r2 = rr ** 2
        om = math.sqrt(x)
        Q = 8.0 * PI * om * float(np.sum(w * S * r2))
        T = 4.0 * PI * float(np.sum(w * p_g ** 2 * r2))
        E = 4.0 * PI * float(np.sum(w * (x * S + p_g ** 2 + U_(m, S)) * r2))
        Rw = schnitt(rr, phi_g, 0.5 * f0)
        aus.append({"x": float(x), "Omega": om, "hp": hp, "f0": float(f0), "r": rr, "phi": phi_g, "dphi": p_g,
                    "j_anschluss": int(jm), "r_anschluss": rm, "grund": grund, "f_anschluss": float(ph[jm] / f0),
                    "R_aus": float(rr[-1]), "R_w": Rw, "Q": Q, "E": E, "T": T,
                    "virial_rel": (E - om * Q - 2.0 * T / 3.0) / E, "kappa0": kap})
    return aus


def prof_kurz(p):
    return {k: v for k, v in p.items() if k not in ("r", "phi", "dphi")}


# ----------------------------------------------------------------------------------------------------------------------
# Profile -> Koeffizienten A, B, C (wie afm_bic.lin_aufbau)
# ----------------------------------------------------------------------------------------------------------------------

def lin_aufbau(x, Om, r, amp, A, B, C, Rw, h, info):
    hp = float(r[1] - r[0])
    if abs(hp - 0.5 * h) > 1e-12:
        raise ValueError("Profil braucht Schritt h/2")
    J = len(r) - 1
    klein = np.nonzero(np.abs(amp) < THETA_RAND * abs(amp[0]))[0]
    j_r = int(klein[0]) if len(klein) else J
    j_r = min(max(j_r, int(math.ceil(20.0 / hp))), J)
    K = j_r // 2
    Km = max(2, min(K - 2, int(round(Rw / h))))
    j = 2 * K
    abw = max(abs(A[j] - (1.0 - Om * Om)), abs(B[j] - 2.0 * Om), abs(C[j]))
    return {"x": float(x), "Omega": float(Om), "h": h, "K": K, "Km": Km, "R": K * h, "r_m": Km * h, "R_w": float(Rw),
            "Al": [float(v) for v in A[:j + 1]], "Bl": [float(v) for v in B[:j + 1]], "Cl": [float(v) for v in C[:j + 1]],
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
        info = {"f0": p["f0"], "R_w": p["R_w"], "R_aus": p["R_aus"], "grund": p["grund"],
                "f_anschluss": p["f_anschluss"], "Q": p["Q"], "E": p["E"], "virial_rel": p["virial_rel"]}
        aus.append(lin_aufbau(x, om, p["r"], f, dp_(modell, S) - x, np.full(len(f), 2.0 * om), sp_(modell, S),
                              p["R_w"], h, info))
    prot.append(f"Profile ({modell}, {len(xs)} Stueck, h = {h}): {uhr() - t0:.1f} s")
    return aus


# ----------------------------------------------------------------------------------------------------------------------
# Lineare Loesungen (unveraendert aus afm_bic.py)
# ----------------------------------------------------------------------------------------------------------------------

def _rk4(y, A, B, C, rr, q2, j0, n, sg, hs, fak=None):
    """n RK4-Schritte fuer y'' = M y, M = [[A + B rho - rho^2, C], [C, A - B rho - rho^2]]; Koeffizienten auf dem
    Gitter h/2 (Index j0, j0 + sg, ...). y = (y1, y2, y1', y2'), vektorisiert ueber rho."""
    y1, y2, p1, p2 = y
    h2 = 0.5 * hs
    h6 = hs / 6.0
    j = j0
    a_ = A[j] - q2
    b_ = B[j] * rr
    m11a = a_ + b_
    m22a = a_ - b_
    ca = C[j]
    for _ in range(n):
        jm = j + sg
        je = jm + sg
        a_ = A[jm] - q2
        b_ = B[jm] * rr
        m11b = a_ + b_
        m22b = a_ - b_
        cb = C[jm]
        a_ = A[je] - q2
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


def W_reell(L, rhos, chunk=6000):
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
                              L["Km"], 1, L["h"])
        kc = np.sqrt(1.0 - (rho - L["Omega"]) ** 2)
        z1, z2, zp1, zp2 = _rk4((np.ones(N), np.zeros(N), -kc, np.zeros(N)), L["Al"], L["Bl"], L["Cl"], rho, rho * rho,
                                2 * L["K"], L["K"] - L["Km"], -1, -L["h"], fak=np.exp(-kc * L["h"]))
        La[s0:s0 + N] = y1[:N] * zp1 - p1[:N] * z1 + y2[:N] * zp2 - p2[:N] * z2
        Lb[s0:s0 + N] = y1[N:] * zp1 - p1[N:] * z1 + y2[N:] * zp2 - p2[N:] * z2
        g = np.maximum.reduce([np.abs(y1), np.abs(y2), np.abs(p1), np.abs(p2)])
        wa[s0:s0 + N] = np.maximum(g[:N], g[N:])
    return La, Lb, wa


def W_multi(Ls, rho_listen):
    h = Ls[0]["h"]
    Kx = max(L["K"] for L in Ls)
    Kmc = max(2, min(min(L["K"] for L in Ls) - 2, int(round(float(np.median([L["R_w"] for L in Ls])) / h))))
    n = 2 * Kx + 1
    Am = np.empty((len(Ls), n))
    Bm = np.empty((len(Ls), n))
    Cm = np.zeros((len(Ls), n))
    for p, L in enumerate(Ls):
        m = 2 * L["K"] + 1
        Am[p, :m], Bm[p, :m], Cm[p, :m] = L["Al"][:m], L["Bl"][:m], L["Cl"][:m]
        Am[p, m:] = 1.0 - L["Omega"] ** 2
        Bm[p, m:] = 2.0 * L["Omega"]
    pidx = np.concatenate([np.full(len(r_), p, dtype=int) for p, r_ in enumerate(rho_listen)])
    rho = np.concatenate([np.asarray(r_, dtype=float) for r_ in rho_listen])
    Om = np.array([Ls[p]["Omega"] for p in pidx])
    AT, BT, CT = Am[pidx].T.copy(), Bm[pidx].T.copy(), Cm[pidx].T.copy()
    N = rho.size
    rr = np.concatenate([rho, rho])
    A2, B2, C2 = np.concatenate([AT, AT], 1), np.concatenate([BT, BT], 1), np.concatenate([CT, CT], 1)
    p1 = np.zeros(2 * N)
    p1[N:] = 1.0
    p2 = np.zeros(2 * N)
    p2[:N] = 1.0
    y1, y2, p1, p2 = _rk4((np.zeros(2 * N), np.zeros(2 * N), p1, p2), A2, B2, C2, rr, rr * rr, 0, Kmc, 1, h)
    kc = np.sqrt(1.0 - (rho - Om) ** 2)
    z1, z2, zp1, zp2 = _rk4((np.ones(N), np.zeros(N), -kc, np.zeros(N)), AT, BT, CT, rho, rho * rho, 2 * Kx,
                            Kx - Kmc, -1, -h, fak=np.exp(-kc * h))
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
    y = _rk4((z0.copy(), z0.copy(), p1, p2), L["Al"], L["Bl"], L["Cl"], rr, q2, 0, L["Km"], 1, L["h"])
    kc = np.sqrt(1.0 - (rho - L["Omega"]) ** 2)
    q = np.sqrt((rho + L["Omega"]) ** 2 - 1.0)
    one, nul = np.ones(N, dtype=complex), np.zeros(N, dtype=complex)
    Z = (np.concatenate([one, nul]), np.concatenate([nul, one]), np.concatenate([-kc, nul]),
         np.concatenate([nul, 1j * q]))
    k = L["K"]
    rest = L["K"] - L["Km"]
    while rest > 0:
        n = min(n_gs, rest)
        Z = _rk4(Z, L["Al"], L["Bl"], L["Cl"], rr, q2, 2 * k, n, -1, -L["h"])
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
    erg.update({"modell": modell, "band": a.band, "h": h, "x_mitglieder": xs})
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
        zeilen.append(f"Mitglied x = omega^2 = {x:.6f} (omega {L['Omega']:.6f}, f0 {L['info']['f0']:.6f}): "
                      f"R = {L['R']:.2f}, r_m = {L['r_m']:.2f}, R_w = {L['R_w']:.3f}, "
                      f"Rand-Abw. {L['rand_abw']:.1e}, {rw['n_rho']} rho-Punkte (max Abstand {rw['drho_max']:.1e}), "
                      f"Wachstum {rw['wachstum_max']:.1e}, {len(rw['wurzeln'])} Nullstellen von L(y_b): "
                      + "; ".join(f"rho {w['rho']:.7f} s {w['s']:+.3e} (rel {w['s_rel']:+.1e}, {w['richtung']:+d})"
                                  for w in rw["wurzeln"]) + f"; {rw['zeit_abtastung']:.1f} + {rw['zeit_wurzeln']:.1f} s")
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
    alle = [rw for rw in reihen if rw.get("gueltig")]
    for i in zw_reihen:
        alle += [rw for (_, _, rw) in zw_reihen[i] if rw is not None]
    alle.sort(key=lambda q: q["x"])
    wechsel = []
    ungepaart = []
    for r1, r2 in zip(alle, alle[1:]):
        pa = paaren(r1["wurzeln"], r2["wurzeln"], a.ast_tol)
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
    erg["paarung"] = ungepaart
    erg["vorzeichenwechsel"] = wechsel
    zeilen.append(f"Vorzeichenwechsel von s ({len(alle)} Reihen, Ast-Toleranz {a.ast_tol}): {len(wechsel)}")
    for w in wechsel:
        zeilen.append(f"  zwischen omega^2 {w['x1']:.7f} (rho {w['rho1']:.6f}, s {w['s1']:+.3e}) und {w['x2']:.7f} "
                      f"(rho {w['rho2']:.6f}, s {w['s2']:+.3e})")
    n_ung = sum(len(u["rho_ungepaart_1"]) + len(u["rho_ungepaart_2"]) for u in ungepaart)
    zeilen.append(f"Ungepaarte Nullstellen (alle Reihenpaare zusammen): {n_ung}")
    sichern()
    kand = []
    erg["kandidaten"] = kand
    for w in wechsel[:a.max_kand]:
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
                      f"{lok['klammer_breite']:.1e}, {len(lok['schritte'])} Schritte)")
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
                      f"{ru['punkte']} Punkte, min|W|/median {ru['min_absW'] / ru['median_absW']:.1e}")
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
    xs = [float(v) for v in a.x.split(",")]
    prot = []
    p1 = profile(a.modell, xs, 0.5 * a.h, prot=prot)
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
        b = bool(dQ < 1e-4 and dE < 1e-4)
        ok &= b
        tab.append({"x": x, "Q_h": u["Q"], "Q_h2": v["Q"], "dQ_rel": dQ, "E_h": u["E"], "E_h2": v["E"], "dE_rel": dE,
                    "f0_h": u["f0"], "f0_h2": v["f0"], "R_w": v["R_w"], "virial_h": u["virial_rel"],
                    "virial_h2": v["virial_rel"], "E_durch_omegaQ": v["E"] / (math.sqrt(x) * v["Q"]), "bestanden": b})
        zeilen.append(f"K2 x = {x:.4f}: Q = {u['Q']:.8e} / {v['Q']:.8e} (rel {dQ:.1e}), E = {u['E']:.8e} / "
                      f"{v['E']:.8e} (rel {dE:.1e}), f0 = {u['f0']:.8f} / {v['f0']:.8f}, R_w = {v['R_w']:.3f}, "
                      f"Virial {u['virial_rel']:.1e} / {v['virial_rel']:.1e} -> {'ok' if b else 'VERFEHLT'}")
    erg.update({"modell": a.modell, "h": a.h, "profilschritte": [0.5 * a.h, 0.25 * a.h], "tabelle": tab,
                "K2_bestanden": bool(ok)})
    zeilen.append(f"K2 ({a.modell}, Profilschritte {0.5 * a.h} und {0.25 * a.h}): {'bestanden' if ok else 'VERFEHLT'}")
    sichern()


# ----------------------------------------------------------------------------------------------------------------------
# Kommando auswertung (bindende Regel aus KARTE.md, Umsetzung PLAN.md Abschnitt Auswertung)
# ----------------------------------------------------------------------------------------------------------------------

def cmd_auswertung(a, erg, zeilen, sichern, npz):
    laeufe = []
    for p in sorted(glob.glob(os.path.join(a.aus, "*.json"))):
        if os.path.basename(p).startswith("auswertung"):
            continue
        d = json.load(open(p))
        if "modell" in d and "mitglieder" in d:
            d["_datei"] = os.path.basename(p)
            laeufe.append(d)
    zeilen.append(f"Auswertung: {len(laeufe)} Laeufe: " + ", ".join(d["_datei"] for d in laeufe))

    def treffer(d):
        aus = []
        for k in d.get("kandidaten", []):
            r = k.get("rechteck", {})
            if "lokal" in k and "umlauf" in r:
                aus.append({"x": k["lokal"]["x_stern"], "rho": k["lokal"]["rho_stern"], "umlauf": r["umlauf"],
                            "umlauf_roh": r["umlauf_roh"], "aufgeloest": r["aufgeloest"], "datei": d["_datei"]})
        return aus
    # K1
    kg = {d["h"]: d for d in laeufe if d["modell"] == "kg"}
    pk = {}
    for h, d in sorted(kg.items()):
        ok = [t for t in treffer(d) if abs(t["x"] - KG_ZIEL[0]) < 1e-4 and abs(t["rho"] - KG_ZIEL[1]) < 1e-4
              and t["aufgeloest"] and abs(t["umlauf"]) == 1]
        pk[h] = {"treffer": treffer(d), "bestanden": bool(ok)}
        zeilen.append(f"K1 h = {h}: {'bestanden' if ok else 'VERFEHLT'}; Treffer: {treffer(d)}")
    k1_ok = len(pk) >= 2 and all(v["bestanden"] for v in pk.values())
    erg["K1"] = {"stufen": pk, "bestanden": k1_ok}
    # K2 (Lesart PLAN: verfehlt -> hoechstens unentschieden)
    k2 = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(a.aus, "k2*.json")))]
    k2_ok = bool(k2) and all(d.get("K2_bestanden") for d in k2)
    erg["K2_bestanden"] = k2_ok
    zeilen.append(f"K2: {len(k2)} Laeufe, bestanden {k2_ok}")
    # Log-Baender
    lg = [d for d in laeufe if d["modell"] == "log"]
    baender = sorted({d["band"] for d in lg})
    hs = sorted({d["h"] for d in lg})
    gesehen = []
    irgendwas = []
    tab = []
    for band in baender:
        ds = {}
        for d in lg:
            if d["band"] == band:
                ds.setdefault(d["h"], []).append(d)
        for h, dl in sorted(ds.items()):
            st = [s for d in dl for s in d.get("streifen", []) if "umlauf" in s]
            st_n0 = [s for s in st if s["umlauf"] != 0]
            st_unaufl = [s for s in st if not s["aufgeloest"]]
            st_fehl = [s for d in dl for s in d.get("streifen", []) if "umlauf" not in s]
            vw = [w for d in dl for w in d.get("vorzeichenwechsel", [])]
            rk = [t for d in dl for t in treffer(d)]
            mx = {round(m["x"], 12) for d in dl for m in d.get("mitglieder", []) if m.get("gueltig")}
            ung = [m["x"] for d in dl for m in d.get("mitglieder", []) if not m.get("gueltig")]
            tab.append({"band": band, "h": h, "dateien": [d["_datei"] for d in dl], "zeilen_gueltig": len(mx),
                        "streifen": len(st), "streifen_umlauf_ungleich_0": len(st_n0),
                        "streifen_nicht_aufgeloest": len(st_unaufl), "streifen_fehlend": len(st_fehl),
                        "vorzeichenwechsel": len(vw), "rechtecke": rk})
            if st_n0 or vw or any(t["umlauf"] != 0 for t in rk):
                irgendwas.append((band, h, "Umlauf != 0 oder s-Wechsel"))
            if st_unaufl or st_fehl or len(mx) < 11 or len(st) < 10 or ung:
                irgendwas.append((band, h, "Raster unvollstaendig oder nicht aufgeloest"))
        if len(ds) >= 2:
            h1, h2 = sorted(ds)[:2]
            for t1 in [t for d in ds[h1] for t in treffer(d)]:
                for t2 in [t for d in ds[h2] for t in treffer(d)]:
                    if (t1["aufgeloest"] and t2["aufgeloest"] and abs(t1["umlauf"]) == 1 and abs(t2["umlauf"]) == 1
                            and abs(t1["x"] - t2["x"]) < 1e-3 and abs(t1["rho"] - t2["rho"]) < 1e-3):
                        gesehen.append({"band": band, "h": [h1, h2], "t1": t1, "t2": t2})
    erg["tabelle"] = tab
    erg["gesehen"] = gesehen
    if not k1_ok:
        ausgang = "nicht auswertbar (K1 verfehlt)"
    elif gesehen:
        ausgang = "Gesehen"
    elif not irgendwas and len(baender) == 3 and len(hs) == 2 and k2_ok:
        ausgang = "Nicht gesehen"
    else:
        ausgang = "Unentschieden"
    erg["ausgang"] = ausgang
    erg["hinweise"] = [list(v) for v in irgendwas]
    for t in tab:
        zeilen.append("  " + json.dumps(jsonfest(t)))
    zeilen.append(f"Ausgang nach der bindenden Regel: {ausgang}; Hinweise: {irgendwas}")
    sichern()


def argumente():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kommando", choices=["familie", "schritt0", "k2", "auswertung"])
    ap.add_argument("--modell", choices=["log", "kg", "mix"], default="log")
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
    global T_MIX
    a = argumente()
    T_MIX = float(a.t)
    name = a.name or a.kommando
    os.makedirs(a.aus, exist_ok=True)
    zeilen = [f"bball.py {a.kommando} ({name}), Start {jetzt()}", "Argumente: " + json.dumps(vars(a))]
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
