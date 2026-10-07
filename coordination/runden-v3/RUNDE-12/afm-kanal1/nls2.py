#!/usr/bin/env python3
"""Runde 10 (runden-v3), Karte NLS-LEITER, Zusatzmodell: quintisch-septisches NLS (--modell qs, Vorgabe) neben dem
kubisch-quintischen (--modell cq). Kopie von nls1.py mit Modellschalter; nls1.py bleibt unveraendert.
Explorativ, v3.

Kopie und Anpassung von RUNDE-09/mess1/mess1.py (dort EGPE nach Petrov; Positivkontrolle Q-Ball). Das Original bleibt
unveraendert. Aenderungen:
  - Modell "cqnls" (Vorgabe): Pego/Warchall Gl. (1.1), (1.2): -i u_t - Lap u = |u|^2 u - |u|^4 u, u = e^{i Omega t} w(r),
    Lap w = Omega w - w^3 + w^5, Omega_* = 3/16, a_* = sqrt(3)/2.
    Intern in der MESS-1-Form: Zeit t' = 2 t, i psi_t' = -1/2 Lap psi + F(|psi|^2) psi, F(n) = (-n + n^2)/2,
    mu' = -Omega/2, BdG-Energie eps' = nu/2 (nu = Frequenz in PW-Einheiten; Kanal u offen fuer nu > Omega).
      D = (nF)' - mu' = -n + 1,5 n^2 - mu',   C = n F' = -0,5 n + n^2.
  - Raumdimension d = 2 oder 3 (Profil: Reibung (d-1)/r, Reihenstart, Schwanz r^{-(d-1)/2} e^{-kappa r}; BdG:
    nu_l = l + (d-1)/2, Fliehkraft nu_l(nu_l - 1)/r^2 wie bic2). Randfunktionen fuer d = 2 exakt aus scipy (hankel1e,
    kve), fuer d = 3 die abbrechende Hankel-Reihe aus bic2.
  - Ein- und Ausgabe in PW-Einheiten (Omega, nu, Gamma = -Im nu).
  - Modell "qball" bleibt fuer die Positivkontrolle der Zaehlmaschine (3D, wie MESS-1).
Verfahren wie MESS-1: fortlaufend orthonormierte regulaere Ebene (b1, b2) und Jost-Ebene (j1 abklingend in v,
j2 auslaufend in u) bei r_m; D = det[b1, b2, j1, j2]; W = Omega(b1, j1) + i Omega(b2, j1) bei reellem nu; W = 0 <=>
gebundener Zustand im Kontinuum (bic2/PLAN.md, Satz). Plan: PLAN.md im selben Ordner.
Kommandos: profile | gebunden | pole | wgitter | umlauf | qbkontrolle
"""
import argparse
import cmath
import datetime
import json
import math
import os
import sys
import time

import numpy as np

try:
    import scipy.special as sps
except Exception:          # nur fuer d = 2 noetig
    sps = None

T0 = time.perf_counter()
PI = math.pi
A_STERN = math.sqrt(3.0) / 2.0
OMEGA_STERN = 3.0 / 16.0
MODELL = {"art": "cqnls", "beta": 0.5, "d": 3}


def jetzt():
    return datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def uhr():
    return time.perf_counter() - T0


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, (complex, np.complexfloating)):
        return [float(x.real), float(x.imag)]
    if isinstance(x, np.ndarray):
        return jsonfest(x.tolist())
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return x


# ----------------------------------------------------------------------------------------------------------------------
# Modell
# ----------------------------------------------------------------------------------------------------------------------

def G_(phi, mu):
    """phi'' + ((d-1)/r) phi' = G(phi). cqnls: G = (Omega - phi^2 + phi^4) phi; qsnls: G = (Omega - phi^4 + phi^6) phi
    (Omega = -2 mu'); qball: G = (U'(S) - omega^2) f, U' = 1 - 2 S + 3 beta S^2, Parameter mu = omega^2."""
    S = phi * phi
    if MODELL["art"] == "qball":
        return (1.0 - 2.0 * S + 3.0 * MODELL["beta"] * S * S - mu) * phi
    if MODELL["art"] == "qsnls":
        return (-S * S + S * S * S - 2.0 * mu) * phi
    return (-S + S * S - 2.0 * mu) * phi


def Gs_(phi, mu):
    if MODELL["art"] == "qball":
        return (1.0 - mu) - 6.0 * phi * phi + 15.0 * MODELL["beta"] * phi ** 4
    if MODELL["art"] == "qsnls":
        return -5.0 * phi ** 4 + 7.0 * phi ** 6 - 2.0 * mu
    return -3.0 * phi * phi + 5.0 * phi ** 4 - 2.0 * mu


def kappa0(mu):
    if MODELL["art"] == "qball":
        return np.sqrt(1.0 - mu)
    return np.sqrt(-2.0 * mu)


# qsnls (quintisch-septisch, -i u_t - Lap u = |u|^4 u - |u|^6 u): F(n) = (-n^2 + n^3)/2
def D_(n, mu):
    if MODELL["art"] == "qsnls":
        return -1.5 * n * n + 2.0 * n ** 3 - mu
    return -n + 1.5 * n * n - mu


def C_(n):
    if MODELL["art"] == "qsnls":
        return -n * n + 1.5 * n ** 3
    return -0.5 * n + n * n


def Dn_(n):
    if MODELL["art"] == "qsnls":
        return -3.0 * n + 6.0 * n * n
    return -1.0 + 3.0 * n


def Cn_(n):
    if MODELL["art"] == "qsnls":
        return -2.0 * n + 4.5 * n * n
    return -0.5 + 2.0 * n


def grenzen(mu):
    """Startintervall: V(phi) > 0 und unterhalb des Gipfels phi_m."""
    if MODELL["art"] == "qball":
        b, e = MODELL["beta"], 1.0 - mu
        Xm = (2.0 + math.sqrt(4.0 - 12.0 * b * e)) / (6.0 * b)
        Xz = (1.0 - math.sqrt(1.0 - 4.0 * b * e)) / (2.0 * b)
        return math.sqrt(Xz), math.sqrt(Xm)
    Om = -2.0 * mu
    if MODELL["art"] == "qsnls":
        wm = np.roots([1.0, -1.0, 0.0, Om])              # G = 0: X^3 - X^2 + Omega = 0, Gipfel = groesste Wurzel
        Xm = max(w.real for w in wm if abs(w.imag) < 1e-12 and w.real > 0)
        wz = np.roots([-1.0 / 8.0, 1.0 / 6.0, 0.0, -Om / 2.0])   # V/phi^2 = -Omega/2 + X^2/6 - X^3/8
        pos = sorted(w.real for w in wz if abs(w.imag) < 1e-9 and 0 < w.real <= Xm * (1 + 1e-9))
        Xz = pos[0] if pos else 0.5 * Xm
        return math.sqrt(Xz), math.sqrt(Xm)
    Xm = (1.0 + math.sqrt(1.0 - 4.0 * Om)) / 2.0
    Xz = 0.75 - 3.0 * math.sqrt(max(1.0 / 16.0 - Om / 3.0, 0.0))
    return math.sqrt(Xz), math.sqrt(Xm)


# ----------------------------------------------------------------------------------------------------------------------
# Profil: Schiessen, vektorisiert ueber (Parameter, Kandidaten), Dimension d
# ----------------------------------------------------------------------------------------------------------------------

def _rk4_prof(r, phi, p, hp, mu):
    dm1 = MODELL["d"] - 1.0

    def f(rr, x, y):
        return y, G_(x, mu) - dm1 * y / rr
    k1a, k1b = f(r, phi, p)
    k2a, k2b = f(r + 0.5 * hp, phi + 0.5 * hp * k1a, p + 0.5 * hp * k1b)
    k3a, k3b = f(r + 0.5 * hp, phi + 0.5 * hp * k2a, p + 0.5 * hp * k2b)
    k4a, k4b = f(r + hp, phi + hp * k3a, p + hp * k3b)
    return (phi + hp / 6.0 * (k1a + 2 * k2a + 2 * k3a + k4a), p + hp / 6.0 * (k1b + 2 * k2b + 2 * k3b + k4b))


def _start(c, mu, hp):
    d = MODELL["d"]
    a = G_(c, mu) / (2.0 * d)
    b = Gs_(c, mu) * a / (8.0 + 4.0 * d)
    return c + a * hp * hp + b * hp ** 4, 2.0 * a * hp + 4.0 * b * hp ** 3


def klassen(mus, lo, hi, K, hp, r_max, f_lin):
    """Kandidaten c (M, K); Klasse -1 = Unterschuss, +1 = Ueberschuss; im linearen Schwanz nach dem Vorzeichen des
    wachsenden Anteils B ~ phi' + phi (kappa + (d-1)/(2 r))."""
    t = np.arange(1, K + 1) / (K + 1.0)
    c = lo[:, None] + (hi - lo)[:, None] * t[None, :]
    mu = mus[:, None] * np.ones_like(c)
    kap = kappa0(mu)
    h2 = 0.5 * (MODELL["d"] - 1.0)
    phi, p = _start(c, mu, hp)
    r = hp
    kl = np.zeros(c.shape, dtype=np.int8)
    offen = np.ones(c.shape, dtype=bool)
    n = int(r_max / hp)
    for _ in range(1, n):
        phi, p = _rk4_prof(r, phi, p, hp, mu)
        r += hp
        ueber = offen & (phi < 0)
        unter = offen & (p > 0) & (phi > 0)
        lin = offen & ~ueber & ~unter & (phi < f_lin * c)
        B = p + phi * (kap + h2 / r)
        kl[ueber] = 1
        kl[unter] = -1
        kl[lin & (B > 0)] = -1
        kl[lin & (B <= 0)] = 1
        offen &= ~(ueber | unter | lin)
        if not offen.any():
            break
    return c, kl


def profile(mus, hp, K=64, runden=12, r_max=160.0, f_lin=1e-4, f_rand=1e-9, protokoll=None):
    """Grundzustaende fuer eine Liste interner Parameter mu (cqnls: mu' = -Omega/2). Gitter r_j = j hp."""
    d = MODELL["d"]
    h2 = 0.5 * (d - 1.0)
    SD = 4 * PI if d == 3 else 2 * PI
    mus = np.asarray(mus, dtype=float)
    M = len(mus)
    lo = np.empty(M)
    hi = np.empty(M)
    for i, mu in enumerate(mus):
        a, b = grenzen(mu)
        lo[i], hi[i] = a * (1 + 1e-13), b * (1 - 1e-15)
    for rd in range(runden):
        c, kl = klassen(mus, lo, hi, K, hp, r_max, f_lin)
        for i in range(M):
            k = kl[i]
            if (k == 0).any() and protokoll is not None:
                protokoll.append(f"mu={mus[i]}: {int((k == 0).sum())} Kandidaten unentschieden (Runde {rd})")
            iu = np.where(k == -1)[0]
            io = np.where(k == 1)[0]
            if len(io) == 0 and len(iu) == K:
                lo[i] = c[i, -1]
                continue
            if len(iu) == 0 and len(io) == K:
                hi[i] = c[i, 0]
                continue
            if len(iu) == 0 or len(io) == 0:
                raise RuntimeError(f"mu={mus[i]}: keine Klammer (unter {len(iu)}, ueber {len(io)})")
            j = io[0]
            ju = iu[iu < j]
            nlo = c[i, ju[-1]] if len(ju) else lo[i]
            lo[i], hi[i] = nlo, c[i, j]
        if np.all((hi - lo) <= 4e-16 * hi):
            break
    cc = np.stack([lo, hi], 1)
    mu2 = mus[:, None] * np.ones_like(cc)
    phi, p = _start(cc, mu2, hp)
    r = hp
    n = int(r_max / hp)
    PH = [np.stack([lo, hi], 1) * 1.0, phi.copy()]
    PP = [np.zeros_like(cc), p.copy()]
    aktiv = np.ones(M, dtype=bool)
    for k in range(1, n):
        phi, p = _rk4_prof(r, phi, p, hp, mu2)
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
    for i, mu in enumerate(mus):
        kap = float(kappa0(mu))
        ph = 0.5 * (PH[:, i, 0] + PH[:, i, 1])
        pp = 0.5 * (PP[:, i, 0] + PP[:, i, 1])
        dif = np.abs(PH[:, i, 1] - PH[:, i, 0])
        f0 = ph[0]
        jm = None
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
            grund = "Ende"
        rm = jm * hp
        A = ph[jm] * rm ** h2 * math.exp(kap * rm)
        R_aus = rm + max(0.0, (math.log(ph[jm] / (f_rand * f0)) / kap)) + 2.0
        J = int(math.ceil(R_aus / hp))
        J += J % 2
        rr = np.arange(J + 1) * hp
        phi_g = np.empty(J + 1)
        p_g = np.empty(J + 1)
        phi_g[:jm + 1] = ph[:jm + 1]
        p_g[:jm + 1] = pp[:jm + 1]
        rt = rr[jm + 1:]
        phi_g[jm + 1:] = A * np.exp(-kap * rt) / rt ** h2
        p_g[jm + 1:] = -phi_g[jm + 1:] * (kap + h2 / rt)
        w = np.ones(J + 1)
        w[1:-1:2] = 4.0
        w[2:-1:2] = 2.0
        w *= hp / 3.0
        n0 = phi_g ** 2
        rd1 = rr ** (d - 1)
        N = SD * float(np.sum(w * n0 * rd1))
        E = SD * float(np.sum(w * (p_g ** 2 - 0.5 * n0 ** 2 + n0 ** 3 / 3.0) * rd1))
        jh = int(np.argmax(n0 < 0.5 * n0[0]))
        r_halb = (jh - 1 + (n0[jh - 1] - 0.5 * n0[0]) / (n0[jh - 1] - n0[jh])) * hp if jh > 0 else float("nan")
        jk = int(np.argmax(phi_g < 0.5 * A_STERN))
        r_kink = ((jk - 1 + (phi_g[jk - 1] - 0.5 * A_STERN) / (phi_g[jk - 1] - phi_g[jk])) * hp
                  if (jk > 0 and f0 > 0.5 * A_STERN) else float("nan"))
        r2 = SD * float(np.sum(w * n0 * rr ** (d + 1))) / N
        aus.append({"mu": float(mu), "Omega": float(-2.0 * mu), "d": d, "hp": hp, "f0": float(f0),
                    "phi_lo": float(lo[i]), "phi_hi": float(hi[i]), "r": rr, "phi": phi_g, "dphi": p_g,
                    "j_anschluss": jm, "r_anschluss": rm, "grund": grund, "f_anschluss": float(ph[jm] / f0),
                    "R_aus": float(rr[-1]), "N": N, "E": E, "R_halb": r_halb, "R_kink": r_kink,
                    "R_rms": math.sqrt(r2), "kappa0": kap})
    return aus


def prof_kurz(pr):
    return {k: v for k, v in pr.items() if k not in ("r", "phi", "dphi")}


# ----------------------------------------------------------------------------------------------------------------------
# BdG
# ----------------------------------------------------------------------------------------------------------------------

def lin_aufbau(pr, h):
    if abs(pr["hp"] - 0.5 * h) > 1e-12:
        raise ValueError("Profil braucht Schritt h/2")
    mu = pr["mu"]
    d = pr["d"]
    n0 = pr["phi"] ** 2
    J = len(n0) - 1
    K = J // 2
    Km = max(2, min(K - 2, int(round(pr["R_halb"] / h))))
    rj = np.arange(J + 1) * pr["hp"]
    cf = np.zeros(J + 1)
    cf[1:] = 1.0 / rj[1:] ** 2
    f0 = pr["f0"]
    a = G_(f0, mu) / (2.0 * d)
    n2 = 2.0 * f0 * a
    s0 = f0 * f0
    if MODELL["art"] == "qball":
        b = MODELL["beta"]
        dv = 1.0 - 4.0 * n0 + 9.0 * b * n0 * n0
        sv = -2.0 * n0 + 6.0 * b * n0 * n0
        reihe = (1.0 - 4.0 * s0 + 9.0 * b * s0 * s0, (-4.0 + 18.0 * b * s0) * n2, -2.0 * s0 + 6.0 * b * s0 * s0,
                 (-2.0 + 12.0 * b * s0) * n2)
        dv_inf = 1.0
    else:
        dv = 2.0 * D_(n0, mu)
        sv = 2.0 * C_(n0)
        reihe = (2.0 * D_(s0, mu), 2.0 * Dn_(s0) * n2, 2.0 * C_(s0), 2.0 * Cn_(s0) * n2)
        dv_inf = -2.0 * mu
    return {"h": h, "K": K, "Km": Km, "R_aus": K * h, "r_m": Km * h, "mu": mu, "d": d, "dv": dv, "sv": sv, "cf": cf,
            "reihe": reihe, "dv_inf": dv_inf}


def hankel(q, R, nu, M=16):
    """aus bic2 (d = 3, ganzzahliges nu: Reihe bricht ab): w = exp(i q r) P(q r); P(qR), Q = w'(R)/exp(i q R)."""
    z = q * R
    mu2 = 4.0 * (nu - 0.5) ** 2
    term = np.ones_like(z)
    P = np.ones_like(z)
    dP = np.zeros_like(z)
    for m in range(1, M + 1):
        term = term * (1j * (mu2 - (2 * m - 1) ** 2) / (8.0 * m)) / z
        P = P + term
        dP = dP + (-m * term / z)
    return P, q * (1j * P + dP)


def _k_rand(kap, R, l):
    """w = sqrt(r) K_l(kap r) (d = 2), exponentiell skaliert mit e^{kap R}: (w(R), w'(R))."""
    K0 = sps.kve(l, kap * R)
    Kp = -0.5 * (sps.kve(abs(l - 1), kap * R) + sps.kve(l + 1, kap * R))
    sR = math.sqrt(R)
    return sR * K0, K0 / (2.0 * sR) + sR * kap * Kp


def _h_rand(q, R, l):
    """w = sqrt(r) H^(1)_l(q r) (d = 2, auslaufend), skaliert mit e^{-i q R}: (w(R), w'(R))."""
    H0 = sps.hankel1e(l, q * R)
    if l == 0:
        Hp = -sps.hankel1e(1, q * R)
    else:
        Hp = 0.5 * (sps.hankel1e(l - 1, q * R) - sps.hankel1e(l + 1, q * R))
    sR = math.sqrt(R)
    return sR * H0, H0 / (2.0 * sR) + sR * q * Hp


def _abl4(y, m11, m22, s):
    U, V, Up, Vp = y
    return (Up, Vp, m11 * U + s * V, s * U + m22 * V)


def _schritt(y, lin, j0, sg, hs, cnu, s11, s22):
    dv, sv, cf = lin["dv"], lin["sv"], lin["cf"]
    j1, j2 = j0 + sg, j0 + 2 * sg
    b0 = dv[j0] + cnu * cf[j0]
    b1 = dv[j1] + cnu * cf[j1]
    b2 = dv[j2] + cnu * cf[j2]
    k1 = _abl4(y, b0 - s11, b0 - s22, sv[j0])
    k2 = _abl4(tuple(u + (0.5 * hs) * v for u, v in zip(y, k1)), b1 - s11, b1 - s22, sv[j1])
    k3 = _abl4(tuple(u + (0.5 * hs) * v for u, v in zip(y, k2)), b1 - s11, b1 - s22, sv[j1])
    k4 = _abl4(tuple(u + hs * v for u, v in zip(y, k3)), b2 - s11, b2 - s22, sv[j2])
    return tuple(u + (hs / 6.0) * (a1 + 2.0 * a2 + 2.0 * a3 + a4) for u, a1, a2, a3, a4 in zip(y, k1, k2, k3, k4))


def _gs(y):
    A = np.stack(y, 0)
    a = A[:, 0, :]
    n1 = np.sqrt(np.sum(np.abs(a) ** 2, 0))
    a = a / n1
    b = A[:, 1, :]
    c = np.sum(np.conj(a) * b, 0)
    b = b - c * a
    n2 = np.sqrt(np.sum(np.abs(b) ** 2, 0))
    b = b / n2
    A = np.stack([a, b], 1)
    return tuple(A[i] for i in range(4))


def spektral(lin, eps):
    eps = np.asarray(eps, dtype=complex)
    if MODELL["art"] == "qball":
        om = math.sqrt(lin["mu"])
        return (om + eps) ** 2, (om - eps) ** 2
    return 2.0 * eps, -2.0 * eps


def loesungen(lin, eps, l=0, n_gs=4):
    """Regulaere Ebene (b1 ~ U-Start, b2) und Jost-Ebene (j1 ~ abklingend in v, j2 ~ auslaufend in u) bei r_m,
    fortlaufend orthonormiert. eps: interner Spektralparameter (cqnls: eps' = nu/2; qball: rho)."""
    eps = np.asarray(eps, dtype=complex)
    B = eps.shape[0]
    h, K, Km, d = lin["h"], lin["K"], lin["Km"], lin["d"]
    nu = l + 0.5 * (d - 1.0)
    cnu = nu * (nu - 1.0)
    s11, s22 = spektral(lin, eps)
    r = h
    d0, d2, s0, s2 = lin["reihe"]
    A_ = d0 - s11
    B_ = d0 - s22
    n2 = 2.0 * (2.0 * nu + 1.0)
    n4 = 4.0 * (2.0 * nu + 3.0)
    a2, b2 = A_ / n2, s0 / n2 * np.ones(B)
    a4, b4 = (A_ * a2 + s0 * b2 + d2) / n4, (s0 * a2 + B_ * b2 + s2) / n4
    c2, e2_ = s0 / n2 * np.ones(B), B_ / n2
    c4, e4 = (A_ * c2 + s0 * e2_ + s2) / n4, (s0 * c2 + B_ * e2_ + d2) / n4
    fak = r ** nu
    pU = np.stack([1.0 + a2 * r * r + a4 * r ** 4, c2 * r * r + c4 * r ** 4])
    pV = np.stack([b2 * r * r + b4 * r ** 4, 1.0 + e2_ * r * r + e4 * r ** 4])
    dU = np.stack([2.0 * a2 * r + 4.0 * a4 * r ** 3, 2.0 * c2 * r + 4.0 * c4 * r ** 3])
    dV = np.stack([2.0 * b2 * r + 4.0 * b4 * r ** 3, 2.0 * e2_ * r + 4.0 * e4 * r ** 3])
    y = (fak * pU + 0j, fak * pV + 0j, fak * (nu * pU / r + dU) + 0j, fak * (nu * pV / r + dV) + 0j)
    S11 = np.stack([s11, s11])
    S22 = np.stack([s22, s22])
    for k in range(1, Km):
        y = _schritt(y, lin, 2 * k, 1, h, cnu, S11, S22)
        if k % n_gs == 0:
            y = _gs(y)
    y = _gs(y)
    R = lin["R_aus"]
    m11i = lin["dv_inf"] - s11
    m22i = lin["dv_inf"] - s22
    unter = (np.real(-m11i) < 0) & (np.imag(eps) == 0)
    q = np.sqrt(-m11i)
    q = np.where(unter, 1j * np.sqrt(np.abs(m11i)), q)
    if d == 3:
        qm = 1j * np.sqrt(m22i)
        Pp, Qp = hankel(q, R, nu)
        Pm, Qm = hankel(qm, R, nu)
    else:
        if sps is None:
            raise RuntimeError("d = 2 braucht scipy")
        kv = np.sqrt(m22i)
        Pm, Qm = _k_rand(kv, R, l)
        ku = np.sqrt(np.abs(m11i)) + 0j
        Pk, Qk = _k_rand(ku, R, l)
        Ph, Qh = _h_rand(q, R, l)
        Pp = np.where(unter, Pk, Ph)
        Qp = np.where(unter, Qk, Qh)
    null = np.zeros(B, dtype=complex)
    z = (np.stack([null, Pp]), np.stack([Pm, null]), np.stack([null, Qp]), np.stack([Qm, null]))
    z = _gs(z)
    for i, k in enumerate(range(K, Km, -1)):
        z = _schritt(z, lin, 2 * k, -1, -h, cnu, S11, S22)
        if i % n_gs == n_gs - 1:
            z = _gs(z)
    z = _gs(z)
    b1 = np.stack([v[0] for v in y])
    b2 = np.stack([v[1] for v in y])
    j1 = np.stack([v[0] for v in z])
    j2 = np.stack([v[1] for v in z])
    return b1, b2, j1, j2, q


def omega_bil(p, q):
    return p[0] * q[2] - p[2] * q[0] + p[1] * q[3] - p[3] * q[1]


def det_D(lin, eps, l=0):
    b1, b2, j1, j2, q = loesungen(lin, eps, l)
    M = np.moveaxis(np.stack([b1, b2, j1, j2], 1), 2, 0)
    return np.linalg.det(M)


def W_werte(lin, eps, l=0):
    b1, b2, j1, j2, q = loesungen(lin, np.asarray(eps, dtype=float) + 0j, l)
    w1 = omega_bil(b1, j1)
    w2 = omega_bil(b2, j1)
    return w1.real + 1j * w2.real, np.maximum(np.abs(w1.imag), np.abs(w2.imag))


def newton(lin, eps0, l=0, iters=40, tol=1e-13, schritt_max=0.02, delta=1e-7):
    eps = np.array(eps0, dtype=complex)
    n = len(eps)
    konv = np.zeros(n, dtype=bool)
    for it in range(iters):
        akt = np.where(~konv)[0]
        if len(akt) == 0:
            break
        e = eps[akt]
        Dd = det_D(lin, np.concatenate([e, e + delta, e + 1j * delta]), l)
        m = len(akt)
        d0, dx, dy = Dd[:m], Dd[m:2 * m], Dd[2 * m:]
        j11, j21 = (dx - d0).real / delta, (dx - d0).imag / delta
        j12, j22 = (dy - d0).real / delta, (dy - d0).imag / delta
        dd = j11 * j22 - j12 * j21
        ok = (dd != 0) & np.isfinite(dd)
        st = np.where(ok, (-(j22 * d0.real - j12 * d0.imag) + 1j * (-(-j21 * d0.real + j11 * d0.imag)))
                      / np.where(ok, dd, 1), 0)
        gross = np.abs(st) > schritt_max
        st = np.where(gross, st * schritt_max / np.maximum(np.abs(st), 1e-300), st)
        eps[akt] = e + st
        konv[akt] = np.abs(st) < tol * np.maximum(1.0, np.abs(e))
    Dend = det_D(lin, eps, l)
    return eps, konv, np.abs(Dend)


def umlauf(werte):
    sp = [cmath.phase(werte[(i + 1) % len(werte)] * np.conj(werte[i])) for i in range(len(werte))]
    return sum(sp) / (2.0 * PI), max(abs(s) for s in sp)


# ----------------------------------------------------------------------------------------------------------------------
# Kommandos (Ein- und Ausgabe in PW-Einheiten: Omega, nu = 2 eps', Gamma = -Im nu)
# ----------------------------------------------------------------------------------------------------------------------

def liste(s):
    return [float(x) for x in s.split(",") if x.strip()]


def omegas(a):
    if a.omega:
        return liste(a.omega)
    return list(np.linspace(a.omega_von, a.omega_bis, a.n_omega))


def prs_fuer(a, oms):
    return profile([-0.5 * o for o in oms], 0.5 * a.h)


def cmd_profile(a, erg, zeilen):
    oms = omegas(a)
    prot = []
    prs = profile([-0.5 * o for o in oms], 0.5 * a.h, protokoll=prot)
    d = MODELL["d"]
    zeilen.append(f"CQ-NLS-Profile d = {d}, h = {a.h} (Profilschritt {0.5 * a.h}); PW-Kinkradius m = 0: "
                  f"sqrt(3)/(8 (3/16 - Omega)) (2D), in 3D das Doppelte")
    zeilen.append("Omega | w(0) | a_* - w(0) | N (Norm) | R_kink (w = a_*/2) | PW-Formel | R_halb | Anschluss")
    for p in prs:
        Rpw = (math.sqrt(3.0) / (8.0 * (OMEGA_STERN - p["Omega"])) * (2.0 if d == 3 else 1.0)
               if MODELL["art"] == "cqnls" else float("nan"))
        p["R_PW"] = Rpw
        zeilen.append(f"{p['Omega']:.5f} | {p['f0']:.10f} | {A_STERN - p['f0']:.3e} | {p['N']:.6f} | "
                      f"{p['R_kink']:.4f} | {Rpw:.4f} | {p['R_halb']:.4f} | {p['f_anschluss']:.1e} {p['grund']}")
    erg["profile"] = [prof_kurz(p) for p in prs]
    erg["protokoll"] = prot


def gebunden_fuer(lin, l, eps_min, n_scan):
    mu = lin["mu"]
    es = np.linspace(eps_min, -mu * (1 - 1e-6), n_scan)
    Dv = det_D(lin, es + 0j, l)
    re = Dv.real
    wurzeln = []
    for i in range(len(es) - 1):
        if np.sign(re[i]) != np.sign(re[i + 1]) and np.isfinite(re[i]) and np.isfinite(re[i + 1]):
            x0, x1, f0, f1 = es[i], es[i + 1], re[i], re[i + 1]
            seite = 0
            for _ in range(60):
                x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
                f2 = det_D(lin, np.array([x2 + 0j]), l)[0].real
                if np.sign(f2) == np.sign(f1):
                    x1, f1 = x2, f2
                    if seite == -1:
                        f0 *= 0.5
                    seite = -1
                else:
                    x0, f0 = x1, f1
                    x1, f1 = x2, f2
                    if seite == 1:
                        f0 *= 0.5
                    seite = 1
                if abs(x1 - x0) < 1e-13:
                    break
            wurzeln.append(float(x1))
    return wurzeln, float(np.max(np.abs(Dv.imag)))


def cmd_gebunden(a, erg, zeilen):
    oms = omegas(a)
    prs = prs_fuer(a, oms)
    erg["gebunden"] = []
    zeilen.append(f"gebundene Moden d = {MODELL['d']}, l = {a.l} (reelle Nullstellen von D, nu in ({a.nu_min}, Omega)), "
                  f"h = {a.h}")
    zeilen.append("Omega | N | R_kink | nu gebunden (PW-Einheiten)")
    for p in prs:
        lin = lin_aufbau(p, a.h)
        w, imd = gebunden_fuer(lin, a.l, 0.5 * a.nu_min, a.n_scan)
        nus = [2.0 * x for x in w]
        erg["gebunden"].append({"Omega": p["Omega"], "N": p["N"], "R_kink": p["R_kink"], "nu": nus, "imD": imd})
        zeilen.append(f"{p['Omega']:.5f} | {p['N']:.5f} | {p['R_kink']:.3f} | {', '.join(f'{x:.8f}' for x in nus)}")


def cmd_pole(a, erg, zeilen):
    oms = omegas(a)
    prs = prs_fuer(a, oms)
    erg["pole"] = []
    zeilen.append(f"Pole d = {MODELL['d']}, l = {a.l}, h = {a.h}; nu = Re - i Gamma (PW-Einheiten); Gitter Re nu in "
                  f"(Omega - {a.re_unter}, Omega + {a.re_breite}), Im nu in (-{a.im_tiefe}, 0)")
    zeilen.append("Omega | N | R_kink | Pole (Re nu, Gamma, Gamma/Re nu, |D|)")
    for p in prs:
        lin = lin_aufbau(p, a.h)
        mu = p["mu"]
        Om = p["Omega"]
        rs = 0.5 * (Om + np.linspace(-a.re_unter, a.re_breite, a.n_re))
        ims = -0.5 * np.linspace(0.0005, a.im_tiefe, a.n_im)
        EE = (rs[None, :] + 1j * ims[:, None]).ravel()
        Dv = np.abs(det_D(lin, EE, a.l)).reshape(len(ims), len(rs))
        start = []
        for i in range(len(ims)):
            for j in range(len(rs)):
                v = Dv[i, j]
                nb = [Dv[ii, jj] for ii in (i - 1, i, i + 1) for jj in (j - 1, j, j + 1)
                      if 0 <= ii < len(ims) and 0 <= jj < len(rs) and (ii, jj) != (i, j)]
                if all(v < x for x in nb):
                    start.append(rs[j] + 1j * ims[i])
        pol = []
        if start:
            e, konv, absd = newton(lin, start, a.l, iters=a.iters)
            for x, k, dd in zip(e, konv, absd):
                if (k or dd < 1e-8) and x.real > 0 and x.imag <= 1e-10 and all(abs(2 * x - y["nu"]) > 2e-7 for y in pol):
                    pol.append({"nu": complex(2 * x), "Gamma": float(-2 * x.imag), "absD": float(dd),
                                "unter_schwelle": bool(2 * x.real < Om)})
        pol.sort(key=lambda z: z["nu"].real)
        erg["pole"].append({"Omega": Om, "N": p["N"], "R_kink": p["R_kink"], "pole": pol})
        zeilen.append(f"{Om:.5f} | {p['N']:.4f} | {p['R_kink']:.3f} | " + ("; ".join(
            f"({z['nu'].real:.8f}, {z['Gamma']:.3e}, {z['Gamma'] / z['nu'].real:.3f}, {z['absD']:.1e})" for z in pol)
            if pol else "keine"))


def w_raster(prs, nus, l, h):
    """W auf dem Gitter (Profile x nu); Kandidatenzellen (beide Komponenten wechseln das Vorzeichen, nu > Omega)."""
    es = 0.5 * np.asarray(nus)
    Wm = np.empty((len(prs), len(es)), dtype=complex)
    imx = 0.0
    for i, p in enumerate(prs):
        w, im = W_werte(lin_aufbau(p, h), es, l)
        Wm[i] = w
        imx = max(imx, float(np.nanmax(im)))
    kand = []
    for i in range(len(prs) - 1):
        for j in range(len(es) - 1):
            if nus[j] <= max(prs[i]["Omega"], prs[i + 1]["Omega"]):
                continue
            ecken = [Wm[i, j], Wm[i, j + 1], Wm[i + 1, j + 1], Wm[i + 1, j]]
            if len({np.sign(e.real) for e in ecken}) > 1 and len({np.sign(e.imag) for e in ecken}) > 1:
                kand.append((i, j, umlauf(ecken)[0]))
    return Wm, imx, kand


def konturen(prs, nus, Wm):
    """Zahl der Vorzeichenwechsel je Komponente und Zeile (nur nu > Omega)."""
    aus = []
    for i, p in enumerate(prs):
        z1 = z2 = 0
        for j in range(len(nus) - 1):
            if nus[j] <= p["Omega"]:
                continue
            z1 += int(Wm[i, j].real * Wm[i, j + 1].real < 0)
            z2 += int(Wm[i, j].imag * Wm[i, j + 1].imag < 0)
        aus.append((p["Omega"], z1, z2))
    return aus


def cmd_wgitter(a, erg, zeilen):
    oms = omegas(a)
    prs = prs_fuer(a, oms)
    nus = np.linspace(a.nu_von, a.nu_bis, a.n_nu)
    Wm, imx, kand = w_raster(prs, nus, a.l, a.h)
    kont = konturen(prs, nus, Wm)
    erg["wgitter"] = {"d": MODELL["d"], "Omega": [p["Omega"] for p in prs], "N": [p["N"] for p in prs],
                      "R_kink": [p["R_kink"] for p in prs], "f_anschluss": [p["f_anschluss"] for p in prs],
                      "nu": nus, "W": Wm, "max_imag": imx, "kandidaten": kand, "konturen": kont}
    zeilen.append(f"W-Gitter d = {MODELL['d']}, l = {a.l}, h = {a.h}: {len(prs)} Omega ({oms[0]:.4f}..{oms[-1]:.4f}) x "
                  f"{len(nus)} nu ({nus[0]:.3f}..{nus[-1]:.3f}); max |Im-Rest| {imx:.1e}")
    zeilen.append("Kandidatenzellen (nu > Omega, beide Komponenten wechseln das Vorzeichen), Umlauf auf den Ecken:")
    for (i, j, w) in kand:
        zeilen.append(f"  Omega {oms[i]:.5f}..{oms[i + 1]:.5f}, nu {nus[j]:.4f}..{nus[j + 1]:.4f}: Umlauf {w:+.3f}")
    if not kand:
        zeilen.append("  keine")
    zeilen.append("Vorzeichenwechsel je Zeile (Omega: Re W, Im W): " + "; ".join(f"{o:.4f}: {z1},{z2}" for o, z1, z2 in kont))
    zeilen.append("Profilanschluss f/f0 (Guete der Profile): " + ", ".join(f"{p['f_anschluss']:.0e}" for p in prs))


def cmd_umlauf(a, erg, zeilen):
    """Umlaufzahl von W auf dem Rechteck [nu0 +- dnu] x [Omega0 +- dOmega]."""
    oms = list(np.linspace(a.omega0 - a.domega, a.omega0 + a.domega, a.n_kante_om))
    prs = prs_fuer(a, oms)
    lins = [lin_aufbau(p, a.h) for p in prs]
    es = 0.5 * np.linspace(a.nu0 - a.dnu, a.nu0 + a.dnu, a.n_kante)
    unten = W_werte(lins[0], es, a.l)[0]
    oben = W_werte(lins[-1], es, a.l)[0][::-1]
    rechts = np.array([W_werte(L, np.array([es[-1]]), a.l)[0][0] for L in lins])
    links = np.array([W_werte(L, np.array([es[0]]), a.l)[0][0] for L in lins])[::-1]
    werte = list(unten) + list(rechts[1:]) + list(oben[1:]) + list(links[1:-1])
    wz, sprung = umlauf(werte)
    mn = float(min(abs(w) for w in werte))
    erg["umlauf"] = {"nu0": a.nu0, "dnu": a.dnu, "Omega0": a.omega0, "dOmega": a.domega, "umlauf": wz,
                     "max_sprung": sprung, "min_abs_W": mn}
    zeilen.append(f"Umlauf d = {MODELL['d']}, l = {a.l}, h = {a.h}: nu {a.nu0} +- {a.dnu}, Omega {a.omega0} +- "
                  f"{a.domega}: Umlauf {wz:+.4f}, groesster Sprung {sprung:.3f} rad, min|W| {mn:.2e}")


def nackte_zustaende(pr, l, anzahl=4):
    """Nackter geschlossener Kanal (Kopplung C = 0): tiefste Eigenwerte von -1/2 U'' + (D + cnu/r^2) U (NLS) bzw.
    -U'' + (dp + cnu/r^2) U (Q-Ball) auf dem Profilgitter, Dirichlet bei 0 und R_aus (Differenzen 2. Ordnung)."""
    from scipy.linalg import eigh_tridiagonal
    d = pr["d"]
    nu = l + 0.5 * (d - 1.0)
    cnu = nu * (nu - 1.0)
    hp = pr["hp"]
    rr = pr["r"][1:-1]
    n0 = pr["phi"][1:-1] ** 2
    if MODELL["art"] == "qball":
        b = MODELL["beta"]
        pot = 1.0 - 4.0 * n0 + 9.0 * b * n0 * n0 + cnu / rr ** 2
        diag = 2.0 / hp ** 2 + pot
        off = -np.ones(len(rr) - 1) / hp ** 2
    else:
        pot = D_(n0, pr["mu"]) + 0.5 * cnu / rr ** 2
        diag = 1.0 / hp ** 2 + pot
        off = -0.5 * np.ones(len(rr) - 1) / hp ** 2
    return eigh_tridiagonal(diag, off, select="i", select_range=(0, anzahl - 1), eigvals_only=True)


def cmd_kanal(a, erg, zeilen):
    """Gibt es einen nackten, an die Wand gebundenen Zustand des geschlossenen Kanals im Kontinuum des offenen?
    NLS: Eigenwert E von -1/2 Lap + D; eingebettet, wenn E < -Omega/2 (dann nu_c = -2 E > Omega). Q-Ball (Kontrolle,
    --qb): E = (omega - rho)^2 < 1 gebunden; Wandzustand bei omega^2 = 0,7977 erwartet bei E ~ 0,706 (Codex Arm A)."""
    if a.qb:
        alt = dict(MODELL)
        MODELL.update({"art": "qball", "beta": a.beta, "d": 3})
        xs = liste(a.omega) if a.omega else [0.60, 0.70, 0.7977, 0.85, 0.90]
        prs = profile(xs, 0.5 * a.h)
        zeilen.append(f"Q-Ball beta = {a.beta}, nackter geschlossener Kanal: omega^2 | tiefste Eigenwerte E von -U'' + dp U "
                      "(Kontinuum ab 1)")
        erg["kanal"] = []
        for p in prs:
            ev = nackte_zustaende(p, a.l)
            erg["kanal"].append({"omega2": p["mu"], "E": ev})
            zeilen.append(f"{p['mu']:.4f} | " + ", ".join(f"{e:.6f}" for e in ev))
        MODELL.clear()
        MODELL.update(alt)
        return
    oms = omegas(a)
    prs = prs_fuer(a, oms)
    zeilen.append(f"Modell {MODELL['art']}, d = {MODELL['d']}, l = {a.l}: nackter geschlossener Kanal, tiefste Eigenwerte "
                  f"E von -1/2 Lap + D (NLS-intern), eingebettet wenn E < -Omega/2; nu_c = -2 E")
    zeilen.append("Omega | R_kink | min D | E_0, E_1, ... | eingebettet? (nu_c)")
    erg["kanal"] = []
    for p in prs:
        ev = nackte_zustaende(p, a.l)
        n0 = p["phi"] ** 2
        dmin = float(np.min(D_(n0, p["mu"])))
        eing = [float(-2.0 * e) for e in ev if e < -0.5 * p["Omega"]]
        erg["kanal"].append({"Omega": p["Omega"], "E": ev, "D_min": dmin, "nu_c": eing})
        zeilen.append(f"{p['Omega']:.5f} | {p['R_kink']:.3f} | {dmin:+.5f} | " + ", ".join(f"{e:+.6f}" for e in ev)
                      + " | " + (("ja, nu_c = " + ", ".join(f"{x:.5f}" for x in eing)) if eing else "nein"))


def cmd_qbkontrolle(a, erg, zeilen):
    """Positivkontrolle der Zaehlmaschine am Q-Ball (3D, U = S - S^2 + S^3/2, wie MESS-1): bekannte Stelle
    omega*^2 = 0,79767679, rho* = 1,7446175 (Umlauf +-1 erwartet); Nachbarkasten um 0,8003 (Umlauf 0 erwartet)."""
    alt = dict(MODELL)
    MODELL.update({"art": "qball", "beta": 0.5, "d": 3})
    es = np.linspace(1.735, 1.755, 21)
    for name, xs in (("positiv", [0.7964, 0.7968, 0.7972, 0.7976, 0.7980, 0.7984, 0.7988]),
                     ("negativ", [0.7996, 0.8000, 0.8004, 0.8008])):
        prs = profile(xs, 0.5 * a.h)
        Wm = np.empty((len(prs), len(es)), dtype=complex)
        for i, p in enumerate(prs):
            Wm[i] = W_werte(lin_aufbau(p, a.h), es, 0)[0]
        kand = []
        for i in range(len(prs) - 1):
            for j in range(len(es) - 1):
                ecken = [Wm[i, j], Wm[i, j + 1], Wm[i + 1, j + 1], Wm[i + 1, j]]
                if len({np.sign(e.real) for e in ecken}) > 1 and len({np.sign(e.imag) for e in ecken}) > 1:
                    kand.append((i, j, umlauf(ecken)[0]))
        rand = list(Wm[0, :]) + list(Wm[1:, -1]) + list(Wm[-1, -2::-1]) + list(Wm[-2:0:-1, 0])
        wz, sprung = umlauf(rand)
        erg[f"qb_{name}"] = {"x": xs, "umlauf_rand": wz, "kandidaten": kand}
        zeilen.append(f"Q-Ball {name}: Umlauf auf dem Rand {wz:+.4f} (groesster Sprung {sprung:.3f} rad), Zellen mit "
                      f"Umlauf != 0: " + (", ".join(f"omega^2 {xs[i]:.4f}..{xs[i + 1]:.4f}, rho {es[j]:.3f}..{es[j + 1]:.3f}: "
                                                    f"{w:+.3f}" for (i, j, w) in kand if abs(w) > 0.5) or "keine"))
    MODELL.clear()
    MODELL.update(alt)


def argumente():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kommando", choices=["profile", "gebunden", "pole", "wgitter", "umlauf", "qbkontrolle", "kanal"])
    ap.add_argument("--qb", action="store_true")
    ap.add_argument("--beta", type=float, default=0.5)
    ap.add_argument("--dim", type=int, default=3, choices=[2, 3])
    ap.add_argument("--modell", type=str, default="qs", choices=["cq", "qs"])
    ap.add_argument("--h", type=float, default=0.02)
    ap.add_argument("--l", type=int, default=0)
    ap.add_argument("--omega", type=str, default="")
    ap.add_argument("--omega-von", type=float, default=0.05)
    ap.add_argument("--omega-bis", type=float, default=0.175)
    ap.add_argument("--n-omega", type=int, default=6)
    ap.add_argument("--nu-min", type=float, default=0.002)
    ap.add_argument("--n-scan", type=int, default=240)
    ap.add_argument("--re-unter", type=float, default=0.0)
    ap.add_argument("--re-breite", type=float, default=0.8)
    ap.add_argument("--im-tiefe", type=float, default=0.4)
    ap.add_argument("--n-re", type=int, default=41)
    ap.add_argument("--n-im", type=int, default=11)
    ap.add_argument("--iters", type=int, default=25)
    ap.add_argument("--nu-von", type=float, default=0.02)
    ap.add_argument("--nu-bis", type=float, default=1.0)
    ap.add_argument("--n-nu", type=int, default=121)
    ap.add_argument("--nu0", type=float, default=0.3)
    ap.add_argument("--dnu", type=float, default=0.01)
    ap.add_argument("--omega0", type=float, default=0.15)
    ap.add_argument("--domega", type=float, default=0.002)
    ap.add_argument("--n-kante", type=int, default=41)
    ap.add_argument("--n-kante-om", type=int, default=15)
    ap.add_argument("--aus", type=str, default="aus")
    ap.add_argument("--name", type=str, default="")
    return ap.parse_args()


def main():
    a = argumente()
    MODELL["d"] = a.dim
    global A_STERN, OMEGA_STERN
    if a.modell == "qs":
        MODELL["art"] = "qsnls"
        A_STERN = math.sqrt(8.0 / 9.0)
        OMEGA_STERN = 64.0 / 729.0
    name = a.name or a.kommando
    os.makedirs(a.aus, exist_ok=True)
    zeilen = [f"nls2.py {a.kommando} ({name}), Modell {MODELL['art']}, Start {jetzt()}", "Argumente: " + json.dumps(vars(a))]
    erg = {"argumente": vars(a), "start": jetzt()}
    rc = 0
    try:
        {"profile": cmd_profile, "gebunden": cmd_gebunden, "pole": cmd_pole, "wgitter": cmd_wgitter,
         "umlauf": cmd_umlauf, "qbkontrolle": cmd_qbkontrolle, "kanal": cmd_kanal}[a.kommando](a, erg, zeilen)
    except Exception as ex:
        import traceback
        zeilen.append("FEHLER: " + repr(ex))
        zeilen.append(traceback.format_exc())
        erg["fehler"] = traceback.format_exc()
        rc = 1
    zeilen.append(f"Ende {jetzt()}, Laufzeit {uhr():.1f} s")
    erg["ende"] = jetzt()
    with open(os.path.join(a.aus, f"{name}.txt"), "w") as f:
        f.write("\n".join(zeilen) + "\n")
    with open(os.path.join(a.aus, f"{name}.json"), "w") as f:
        json.dump(jsonfest(erg), f, indent=1)
    print("\n".join(zeilen))
    return rc


if __name__ == "__main__":
    sys.exit(main())
