#!/usr/bin/env python3
"""Runde 9 (runden-v3), Karte MESS-1 "Troepfchen-Bruecke". Explorativ, v3.

Kopie und Anpassung von Teilen aus RUNDE-07/bic2/bic2.py (Version 3): Reihenstart der regulaeren Loesungen
(reg_start/direkt_m), abbrechende Hankel-Reihe (hankel), Anschlussdeterminante und 2D-Newton (det/newton), Umlaufzahl
(umlauf), W = L(y_a) + i L(y_b) als symplektisches Produkt mit der abklingenden Loesung bei r_m (direkt_m). Dort torch,
hier numpy (float64/complex128). Die Originale bleiben unveraendert.

Modell (Petrov 2015, PRL 115, 155302, Gl. (10), an der Quelle gelesen): symmetrische binaere Mischung, reduziert
    i phi_t = (-1/2 lap - 3 |phi|^2 + (5/2) |phi|^3 - mu) phi,   N~ = Integral |phi|^2 d^3r,  Energie
    E~ = Integral [ |grad phi|^2/2 - 3 |phi|^4/2 + |phi|^5 ].
Grundzustand phi_0(r) reell bei festem mu in (-1/2, 0): phi'' + (2/r) phi' = 2 (F(phi^2) - mu) phi, F(n) = -3n + 5/2 n^1.5.
BdG fuer Drehimpuls l, delta = u e^{-i eps t} + v* e^{i eps t}, reduziert U = r u, V = r v (dim = 3, nu = l + 1):
    U'' = [2 (D - eps) + l(l+1)/r^2] U + 2 C V
    V'' = 2 C U + [2 (D + eps) + l(l+1)/r^2] V
    D = (n F)'(n0) - mu = -6 n0 + 6,25 n0^1.5 - mu,   C = n0 F'(n0) = -3 n0 + 3,75 n0^1.5,   n0 = phi_0^2.
Aussen: Kanal u offen fuer Re eps > -mu (q = sqrt(2 (eps + mu))), Kanal v geschlossen (kappa = sqrt(2 (eps - mu))).
Pol: regulaer bei 0, auslaufend in u, abklingend in v; eps = eps_r - i Gamma (Gamma = Amplitudenrate, Energiebreite 2 Gamma).
Verfahren: direkte Loesungsvektoren mit fortlaufender Gram-Schmidt-Orthonormierung (positive Diagonale): regulaere
Ebene von r = h nach aussen bis r_m, Jost-Ebene (z2 = abklingend in v zuerst, dann z1 = auslaufend in u) von R nach innen
bis r_m. Orthonormierung aendert die aufgespannten Ebenen nicht, also weder Pole noch Nullstellen; die Umlaufzahl von W
bleibt, weil die Basiswechsel Dreiecksmatrizen mit positiver Diagonale sind.
    D(eps)  = det[b1, b2, j1, j2] (normiert), Nullstellen = Pole (gebunden: reell unter der Schwelle).
    W(eps)  = Omega(b1, j1) + i Omega(b2, j1) bei reellem eps > -mu. W = 0 <=> gebundener Zustand im Kontinuum
              (Satz in bic2/PLAN.md, Abschnitt 1: P lagrangesch). Omega(y, z) = U_y U_z' - U_y' U_z + V_y V_z' - V_y' V_z.

Kommandos: rauch | profile | gebunden | pole | wgitter | umlauf | einheiten
Lokal nur Rauchtest (CPU, 1 Thread). Messlaeufe auf der .69 ueber kleintest.sh. Plan: PLAN.md im selben Ordner.
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

T0 = time.perf_counter()
PI = math.pi


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

# Modellwahl: "egpe" (Parameter mu) oder "qball" (Positivkontrolle, Parameter omega^2, U = S - S^2 + beta S^3, wie bic2)
MODELL = {"art": "egpe", "beta": 0.5}


def G_(phi, mu):
    """phi'' + (2/r) phi' = G(phi) = 2 (F(phi^2) - mu) phi, F(n) = -3 n + 5/2 n^1.5 (|phi|^3 fuer phi < 0).
    Q-Ball (Kontrolle): G = (U'(S) - omega^2) f mit U' = 1 - 2 S + 3 beta S^2, Parameter mu = omega^2."""
    if MODELL["art"] == "qball":
        S = phi * phi
        return (1.0 - 2.0 * S + 3.0 * MODELL["beta"] * S * S - mu) * phi
    a = np.abs(phi)
    return 2.0 * (-3.0 * phi * phi + 2.5 * a * a * a - mu) * phi


def Gs_(phi, mu):
    """dG/dphi fuer phi > 0"""
    if MODELL["art"] == "qball":
        return (1.0 - mu) - 6.0 * phi * phi + 15.0 * MODELL["beta"] * phi ** 4
    return -18.0 * phi * phi + 20.0 * phi ** 3 - 2.0 * mu


def kappa0(mu):
    if MODELL["art"] == "qball":
        return np.sqrt(1.0 - mu)
    return np.sqrt(-2.0 * mu)


def D_(n, mu):
    return -6.0 * n + 6.25 * n * np.sqrt(n) - mu


def C_(n):
    return -3.0 * n + 3.75 * n * np.sqrt(n)


def Dn_(n):
    return -6.0 + 9.375 * np.sqrt(n)


def Cn_(n):
    return -3.0 + 5.625 * np.sqrt(n)


def grenzen(mu):
    """Startintervall (phi_z, phi_m): V(phi) = 3/2 phi^4 - phi^5 + mu phi^2 > 0 und unterhalb des Gipfels phi_m."""
    if MODELL["art"] == "qball":
        b, e = MODELL["beta"], 1.0 - mu
        Xm = (2.0 + math.sqrt(4.0 - 12.0 * b * e)) / (6.0 * b)
        Xz = (1.0 - math.sqrt(1.0 - 4.0 * b * e)) / (2.0 * b)
        return math.sqrt(Xz), math.sqrt(Xm)
    wm = np.roots([5.0, -6.0, 0.0, -2.0 * mu])
    phim = max(w.real for w in wm if abs(w.imag) < 1e-12 and w.real > 0)
    wz = np.roots([-1.0, 1.5, 0.0, mu])
    phiz = max(w.real for w in wz if abs(w.imag) < 1e-12 and 0 < w.real < phim)
    return phiz, phim


# ----------------------------------------------------------------------------------------------------------------------
# Profil: Schiessen, vektorisiert ueber (mu, Kandidaten)
# ----------------------------------------------------------------------------------------------------------------------

def _rk4_prof(r, phi, p, hp, mu):
    def f(rr, x, y):
        return y, G_(x, mu) - 2.0 * y / rr
    k1a, k1b = f(r, phi, p)
    k2a, k2b = f(r + 0.5 * hp, phi + 0.5 * hp * k1a, p + 0.5 * hp * k1b)
    k3a, k3b = f(r + 0.5 * hp, phi + 0.5 * hp * k2a, p + 0.5 * hp * k2b)
    k4a, k4b = f(r + hp, phi + hp * k3a, p + hp * k3b)
    return (phi + hp / 6.0 * (k1a + 2 * k2a + 2 * k3a + k4a), p + hp / 6.0 * (k1b + 2 * k2b + 2 * k3b + k4b))


def _start(c, mu, hp):
    a = G_(c, mu) / 6.0
    b = Gs_(c, mu) * a / 20.0
    return c + a * hp * hp + b * hp ** 4, 2.0 * a * hp + 4.0 * b * hp ** 3


def klassen(mus, lo, hi, K, hp, r_max, f_lin):
    """Kandidaten c (M, K) im offenen Intervall (lo, hi); Klasse -1 = Unterschuss (kehrt um), +1 = Ueberschuss
    (kreuzt 0), im linearen Schwanz (phi < f_lin c) nach dem Vorzeichen des wachsenden Anteils
    B ~ kappa r phi + phi + r phi' (> 0: Unterschuss)."""
    t = np.arange(1, K + 1) / (K + 1.0)
    c = lo[:, None] + (hi - lo)[:, None] * t[None, :]
    mu = mus[:, None] * np.ones_like(c)
    kap = kappa0(mu)
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
        B = kap * r * phi + phi + r * p
        kl[ueber] = 1
        kl[unter] = -1
        kl[lin & (B > 0)] = -1
        kl[lin & (B <= 0)] = 1
        offen &= ~(ueber | unter | lin)
        if not offen.any():
            break
    return c, kl


def profile(mus, hp, K=64, runden=12, r_max=120.0, f_lin=1e-4, f_rand=1e-9, protokoll=None):
    """Grundzustaende fuer eine Liste mu. Rueckgabe: Liste von dicts mit Gitter r_j = j hp."""
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
            if (k == 0).any():
                if protokoll is not None:
                    protokoll.append(f"mu={mus[i]}: {int((k == 0).sum())} Kandidaten unentschieden (Runde {rd})")
            iu = np.where(k == -1)[0]
            io = np.where(k == 1)[0]
            if len(io) == 0 and len(iu) == K:      # Loesung liegt oberhalb aller Kandidaten (duenne Wand)
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
    # Endtrajektorien lo, hi speichern
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
    PH = np.array(PH)   # (J, M, 2)
    PP = np.array(PP)
    aus = []
    for i, mu in enumerate(mus):
        kap = float(kappa0(mu))
        ph = 0.5 * (PH[:, i, 0] + PH[:, i, 1])
        pp = 0.5 * (PP[:, i, 0] + PP[:, i, 1])
        dif = np.abs(PH[:, i, 1] - PH[:, i, 0])
        f0 = ph[0]
        # Anschluss an den Schwanz A exp(-kap r)/r: erster Punkt mit phi < f_lin f0, solange die Klammer eng ist
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
        A = ph[jm] * rm * math.exp(kap * rm)
        R_aus = rm + max(0.0, (math.log(ph[jm] / (f_rand * f0)) / kap)) + 2.0
        J = int(math.ceil(R_aus / hp))
        J += J % 2
        rr = np.arange(J + 1) * hp
        phi_g = np.empty(J + 1)
        p_g = np.empty(J + 1)
        phi_g[:jm + 1] = ph[:jm + 1]
        p_g[:jm + 1] = pp[:jm + 1]
        rt = rr[jm + 1:]
        phi_g[jm + 1:] = A * np.exp(-kap * rt) / rt
        p_g[jm + 1:] = -phi_g[jm + 1:] * (kap + 1.0 / rt)
        w = np.ones(J + 1)
        w[1:-1:2] = 4.0
        w[2:-1:2] = 2.0
        w *= hp / 3.0
        n0 = phi_g ** 2
        N = 4 * PI * float(np.sum(w * n0 * rr ** 2))
        E = 4 * PI * float(np.sum(w * (0.5 * p_g ** 2 - 1.5 * n0 ** 2 + n0 ** 2.5) * rr ** 2))
        jh = int(np.argmax(n0 < 0.5 * n0[0]))
        r_halb = (jh - 1 + (n0[jh - 1] - 0.5 * n0[0]) / (n0[jh - 1] - n0[jh])) * hp if jh > 0 else float("nan")
        r2 = 4 * PI * float(np.sum(w * n0 * rr ** 4)) / N
        aus.append({"mu": float(mu), "hp": hp, "f0": float(f0), "phi_lo": float(lo[i]), "phi_hi": float(hi[i]),
                    "r": rr, "phi": phi_g, "dphi": p_g, "j_anschluss": jm, "r_anschluss": rm, "grund": grund,
                    "f_anschluss": float(ph[jm] / f0), "R_aus": float(rr[-1]), "N": N, "E": E, "E_durch_N": E / N,
                    "R_halb": r_halb, "R_rms": math.sqrt(r2), "kappa0": kap})
    return aus


def prof_kurz(pr):
    return {k: v for k, v in pr.items() if k not in ("r", "phi", "dphi")}


# ----------------------------------------------------------------------------------------------------------------------
# BdG: Koeffizienten, Reihenstart (aus bic2 reg_start/direkt_m), Hankel (aus bic2), Loesungen, D und W
# ----------------------------------------------------------------------------------------------------------------------

def lin_aufbau(pr, h):
    """Gitter r_k = k h; Profil mit Schritt h/2 fuer die RK4-Mittelpunkte. Anschluss r_m bei R_halb.
    dv, sv: Diagonale ohne Spektralterm und Kopplung; dv_inf = Wert von dv bei r -> unendlich."""
    if abs(pr["hp"] - 0.5 * h) > 1e-12:
        raise ValueError("Profil braucht Schritt h/2")
    mu = pr["mu"]
    n0 = pr["phi"] ** 2
    J = len(n0) - 1
    K = J // 2
    Km = max(2, min(K - 2, int(round(pr["R_halb"] / h))))
    rj = np.arange(J + 1) * pr["hp"]
    cf = np.zeros(J + 1)
    cf[1:] = 1.0 / rj[1:] ** 2
    f0 = pr["f0"]
    a = G_(f0, mu) / 6.0
    n2 = 2.0 * f0 * a                     # n(r) = f0^2 + n2 r^2 + ...
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
    return {"h": h, "K": K, "Km": Km, "R_aus": K * h, "r_m": Km * h, "mu": mu, "dv": dv, "sv": sv, "cf": cf,
            "reihe": reihe, "dv_inf": dv_inf}


def hankel(q, R, nu, M=16):
    """aus bic2: w = exp(i q r) P(q r); Rueckgabe P(qR), Q = w'(R)/exp(i q R). Ganzzahliges nu: Reihe bricht ab."""
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


def _abl4(y, m11, m22, s):
    U, V, Up, Vp = y
    return (Up, Vp, m11 * U + s * V, s * U + m22 * V)


def _schritt(y, lin, j0, sg, hs, cnu, s11, s22):
    """RK4-Schritt fuer U'' = (b - s11) U + s V, V'' = s U + (b - s22) V, b = dv + cnu/r^2."""
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
    """Gram-Schmidt ueber die Achse 1 (zwei Vektoren), positive Diagonale; y: Tupel von 4 Arrays (2, B)."""
    A = np.stack(y, 0)                     # (4, 2, B)
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
    """Spektralterme (sub11, sub22): EGPE (2 eps, -2 eps); Q-Ball (omega + rho)^2, (omega - rho)^2 mit rho = eps."""
    eps = np.asarray(eps, dtype=complex)
    if MODELL["art"] == "qball":
        om = math.sqrt(lin["mu"])
        return (om + eps) ** 2, (om - eps) ** 2
    return 2.0 * eps, -2.0 * eps


def loesungen(lin, eps, l=0, n_gs=4):
    """Regulaere Ebene (b1 ~ U-Start, b2) bei r_m und Jost-Ebene (j1 ~ z2 abklingend in v, j2 ~ z1 auslaufend in u),
    beide fortlaufend orthonormiert. eps: komplexes Array (B,) (Q-Ball: rho)."""
    eps = np.asarray(eps, dtype=complex)
    B = eps.shape[0]
    h, K, Km = lin["h"], lin["K"], lin["Km"]
    nu = l + 1.0
    cnu = nu * (nu - 1.0)
    s11, s22 = spektral(lin, eps)
    # Reihenstart (bic2 direkt_m), U = r^nu (a0 + a2 r^2 + a4 r^4), V ebenso
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
    # Jost-Start bei R: offener Kanal q = sqrt(-(dv_inf - s11)), geschlossener kappa = sqrt(dv_inf - s22)
    R = lin["R_aus"]
    m11i = lin["dv_inf"] - s11
    m22i = lin["dv_inf"] - s22
    q = np.sqrt(-m11i)
    unter = (np.real(-m11i) < 0) & (np.imag(eps) == 0)
    q = np.where(unter, 1j * np.sqrt(np.abs(m11i)), q)
    qm = 1j * np.sqrt(m22i)
    Pp, Qp = hankel(q, R, nu)
    Pm, Qm = hankel(qm, R, nu)
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
    M = np.stack([b1, b2, j1, j2], 1)      # (4 zeilen, 4 spalten, B)
    M = np.moveaxis(M, 2, 0)               # (B, 4, 4)
    return np.linalg.det(M)


def W_werte(lin, eps, l=0):
    """W = Omega(b1, j1) + i Omega(b2, j1) bei reellem eps (Realteile; Imaginaerteile als Kontrolle)."""
    b1, b2, j1, j2, q = loesungen(lin, np.asarray(eps, dtype=float) + 0j, l)
    w1 = omega_bil(b1, j1)
    w2 = omega_bil(b2, j1)
    return w1.real + 1j * w2.real, np.maximum(np.abs(w1.imag), np.abs(w2.imag))


def newton(lin, eps0, l=0, iters=40, tol=1e-13, schritt_max=0.02, delta=1e-7):
    """2D-Newton auf (Re D, Im D) mit Vorwaertsdifferenzen (D ist nach der Normierung nicht analytisch)."""
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
        st = np.where(ok, (-(j22 * d0.real - j12 * d0.imag) + 1j * (-(-j21 * d0.real + j11 * d0.imag))) / np.where(ok, dd, 1), 0)
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
# Kommandos
# ----------------------------------------------------------------------------------------------------------------------

def liste(s):
    return [float(x) for x in s.split(",") if x.strip()]


def mu_gitter(a):
    if a.mu:
        return liste(a.mu)
    return list(np.linspace(a.mu_von, a.mu_bis, a.n_mu))


def cmd_profile(a, erg, zeilen):
    mus = mu_gitter(a)
    prot = []
    prs = profile(mus, 0.5 * a.h, protokoll=prot)
    erg["profile"] = [prof_kurz(p) for p in prs]
    erg["protokoll"] = prot
    zeilen.append("mu | phi(0) | N~ | E~/N~ | R_halb | R_rms | Anschluss (f/f0, Grund)")
    for p in prs:
        zeilen.append(f"{p['mu']:.6f} | {p['f0']:.12f} | {p['N']:.6f} | {p['E_durch_N']:.6f} | {p['R_halb']:.4f} | "
                      f"{p['R_rms']:.4f} | {p['f_anschluss']:.1e} {p['grund']}")
    return prs


def gebunden_fuer(lin, l, eps_min, n_scan):
    """Reelle Nullstellen von D auf (eps_min, -mu) (gebundene Moden), Vorzeichenwechsel plus Illinois."""
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
    mus = mu_gitter(a)
    prs = profile(mus, 0.5 * a.h)
    erg["gebunden"] = []
    zeilen.append(f"gebundene Moden l = {a.l} (Nullstellen von D auf ({a.eps_min}, -mu)), h = {a.h}")
    zeilen.append("mu | N~ | -mu | eps (gebunden) | max|Im D|")
    for p in prs:
        lin = lin_aufbau(p, a.h)
        w, imd = gebunden_fuer(lin, a.l, a.eps_min, a.n_scan)
        erg["gebunden"].append({"mu": p["mu"], "N": p["N"], "schwelle": -p["mu"], "eps": w, "imD": imd})
        zeilen.append(f"{p['mu']:.6f} | {p['N']:.4f} | {-p['mu']:.6f} | {', '.join(f'{x:.8f}' for x in w)} | {imd:.1e}")


def cmd_pole(a, erg, zeilen):
    """Resonanzpole: Startgitter im komplexen eps (je mu), Newton aus den Minima von |D|, dann Fortsetzung."""
    mus = mu_gitter(a)
    prs = profile(mus, 0.5 * a.h)
    erg["pole"] = []
    zeilen.append(f"Pole l = {a.l}, h = {a.h}; eps = Re - i Gamma; Gitter Re in (-mu - {a.re_unter}, -mu + {a.re_breite}), "
                  f"Im in (-{a.im_tiefe}, 0)")
    zeilen.append("mu | N~ | -mu | Pole (Re eps, Gamma, |D|, konv)")
    for p in prs:
        lin = lin_aufbau(p, a.h)
        mu = p["mu"]
        rs = -mu + np.linspace(-a.re_unter, a.re_breite, a.n_re)
        ims = -np.linspace(0.0005, a.im_tiefe, a.n_im)
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
        if not start:
            zeilen.append(f"{mu:.6f} | {p['N']:.4f} | {-mu:.6f} | keine lokalen Minima")
            erg["pole"].append({"mu": mu, "N": p["N"], "pole": []})
            continue
        e, konv, absd = newton(lin, start, a.l, iters=a.iters)
        pol = []
        for x, k, d in zip(e, konv, absd):
            if (k or d < 1e-8) and x.real > 0 and x.imag <= 1e-10 and all(abs(x - y["eps"]) > 1e-7 for y in pol):
                pol.append({"eps": complex(x), "Gamma": float(-x.imag), "absD": float(d), "unter_schwelle": bool(x.real < -mu)})
        pol.sort(key=lambda z: z["eps"].real)
        erg["pole"].append({"mu": mu, "N": p["N"], "schwelle": -mu, "pole": pol})
        zeilen.append(f"{mu:.6f} | {p['N']:.4f} | {-mu:.6f} | " + "; ".join(
            f"({z['eps'].real:.8f}, {z['Gamma']:.3e}, {z['absD']:.1e})" for z in pol))


def cmd_wgitter(a, erg, zeilen):
    """W auf einem Gitter (eps, mu): Vorzeichen beider Komponenten, Zellen mit Vorzeichenwechsel in beiden
    Komponenten sind Kandidaten fuer Nullstellen (BIC)."""
    mus = mu_gitter(a)
    prs = profile(mus, 0.5 * a.h)
    es = np.linspace(a.eps_von, a.eps_bis, a.n_eps)
    Wm = np.empty((len(prs), len(es)), dtype=complex)
    imx = 0.0
    for i, p in enumerate(prs):
        lin = lin_aufbau(p, a.h)
        w, im = W_werte(lin, es, a.l)
        Wm[i] = w
        imx = max(imx, float(np.max(im)))
    kand = []
    for i in range(len(prs) - 1):
        for j in range(len(es) - 1):
            ecken = [Wm[i, j], Wm[i, j + 1], Wm[i + 1, j + 1], Wm[i + 1, j]]
            s1 ={np.sign(e.real) for e in ecken}
            s2 = {np.sign(e.imag) for e in ecken}
            if len(s1) > 1 and len(s2) > 1:
                wz, sprung = umlauf(ecken)
                kand.append({"i": i, "j": j, "mu": [prs[i]["mu"], prs[i + 1]["mu"]], "eps": [es[j], es[j + 1]],
                             "N": [prs[i]["N"], prs[i + 1]["N"]], "umlauf_ecken": wz, "sprung": sprung})
    erg["wgitter"] = {"mu": [p["mu"] for p in prs], "N": [p["N"] for p in prs], "eps": es, "W": Wm,
                      "max_imag": imx, "kandidaten": kand}
    zeilen.append(f"W-Gitter l = {a.l}, h = {a.h}: {len(prs)} mu x {len(es)} eps; max |Im-Rest| {imx:.1e}")
    zeilen.append("Kandidaten (Zellen mit Vorzeichenwechsel in beiden Komponenten), Umlauf auf den vier Ecken:")
    for k in kand:
        zeilen.append(f"  mu {k['mu'][0]:.6f}..{k['mu'][1]:.6f} (N~ {k['N'][0]:.2f}..{k['N'][1]:.2f}), "
                      f"eps {k['eps'][0]:.5f}..{k['eps'][1]:.5f}: Umlauf {k['umlauf_ecken']:+.3f}")
    if not kand:
        zeilen.append("  keine")


def cmd_umlauf(a, erg, zeilen):
    """Umlaufzahl von W auf dem Rechteck [eps0 +- de] x [mu0 +- dmu], n Punkte je Kante (mu-Kanten: n_mu Profile)."""
    e0, de, m0, dm = a.eps0, a.deps, a.mu0, a.dmu
    nm = a.n_kante_mu
    mus = list(np.linspace(m0 - dm, m0 + dm, nm))
    prs = profile(mus, 0.5 * a.h)
    lins = [lin_aufbau(p, a.h) for p in prs]
    ne = a.n_kante
    es = np.linspace(e0 - de, e0 + de, ne)
    # unten (mu0 - dm): eps aufsteigend; rechts (eps0 + de): mu aufsteigend; oben: eps absteigend; links: mu absteigend
    unten = W_werte(lins[0], es, a.l)[0]
    oben = W_werte(lins[-1], es, a.l)[0][::-1]
    rechts = np.array([W_werte(L, np.array([e0 + de]), a.l)[0][0] for L in lins])
    links = np.array([W_werte(L, np.array([e0 - de]), a.l)[0][0] for L in lins])[::-1]
    werte = list(unten) + list(rechts[1:]) + list(oben[1:]) + list(links[1:-1])
    wz, sprung = umlauf(werte)
    mn = float(min(abs(w) for w in werte))
    erg["umlauf"] = {"eps0": e0, "deps": de, "mu0": m0, "dmu": dm, "N": [p["N"] for p in prs], "umlauf": wz,
                     "max_sprung": sprung, "min_abs_W": mn, "n_punkte": len(werte)}
    zeilen.append(f"Umlauf l = {a.l}, h = {a.h}: eps {e0:.6f} +- {de:.1e}, mu {m0:.6f} +- {dm:.1e} "
                  f"(N~ {prs[0]['N']:.3f}..{prs[-1]['N']:.3f}): Umlauf {wz:+.4f}, groesster Phasensprung "
                  f"{sprung:.3f} rad, min|W| {mn:.2e}, {len(werte)} Punkte")


def w_raster(prs, es, l, h):
    """W auf dem Gitter (Profile x Spektralwerte); Kandidatenzellen und Umlauf auf dem Gesamtrand."""
    Wm = np.empty((len(prs), len(es)), dtype=complex)
    imx = 0.0
    for i, p in enumerate(prs):
        w, im = W_werte(lin_aufbau(p, h), es, l)
        Wm[i] = w
        imx = max(imx, float(np.max(im)))
    kand = []
    for i in range(len(prs) - 1):
        for j in range(len(es) - 1):
            ecken = [Wm[i, j], Wm[i, j + 1], Wm[i + 1, j + 1], Wm[i + 1, j]]
            if len({np.sign(e.real) for e in ecken}) > 1 and len({np.sign(e.imag) for e in ecken}) > 1:
                kand.append((i, j, umlauf(ecken)[0]))
    rand = list(Wm[0, :]) + list(Wm[1:, -1]) + list(Wm[-1, -2::-1]) + list(Wm[-2:0:-1, 0])
    return Wm, imx, kand, umlauf(rand)


def cmd_qbkontrolle(a, erg, zeilen):
    """Positivkontrolle der portierten W-Maschine am Q-Ball (U = S - S^2 + beta S^3, 3D, l = 0): bekannte Nullstelle
    omega*^2 = 0,79767679, rho* = 1,7446175 (RUNDE-07/THEORIE-ATMUNGS-NULLSTELLEN.md, Tabelle 2.2), Umlauf +-1 erwartet;
    Negativkontrolle um omega^2 = 0,8003 (dort Umlauf 0, bic2 lauf-69/aus-exakt-g5)."""
    MODELL["art"] = "qball"
    MODELL["beta"] = a.beta
    es = np.linspace(a.qb_rho_von, a.qb_rho_bis, a.qb_n_rho)
    for name, xs in (("positiv", liste(a.qb_x)), ("negativ", liste(a.qb_x_neg))):
        prs = profile(xs, 0.5 * a.h)
        Wm, imx, kand, (wz, sprung) = w_raster(prs, es, a.l, a.h)
        erg[f"qb_{name}"] = {"x": xs, "rho": es, "W": Wm, "kandidaten": kand, "umlauf_rand": wz, "sprung": sprung,
                             "f0": [p["f0"] for p in prs], "max_imag": imx}
        zeilen.append(f"Q-Ball {name}: omega^2 {xs[0]:.5f}..{xs[-1]:.5f} ({len(xs)}), rho {es[0]:.4f}..{es[-1]:.4f} "
                      f"({len(es)}), h = {a.h}: Umlauf auf dem Rand {wz:+.4f} (groesster Sprung {sprung:.3f} rad), "
                      f"Kandidatenzellen {len(kand)}, f(0) = {', '.join(f'{p['f0']:.9f}' for p in prs)}")
        for (i, j, w) in kand:
            zeilen.append(f"   Zelle omega^2 {xs[i]:.5f}..{xs[i + 1]:.5f}, rho {es[j]:.5f}..{es[j + 1]:.5f}: Umlauf {w:+.3f}")
    # Pol an der bekannten Stelle (Breite ~ 0 erwartet)
    pr = profile([a.qb_xstern], 0.5 * a.h)[0]
    lin = lin_aufbau(pr, a.h)
    e, k, d = newton(lin, [a.qb_rhostern - 1e-4j], a.l, iters=40)
    erg["qb_pol"] = {"x": a.qb_xstern, "rho": complex(e[0]), "absD": float(d[0]), "f0": pr["f0"]}
    zeilen.append(f"Q-Ball Pol bei omega^2 = {a.qb_xstern}: rho = {e[0].real:.8f} {e[0].imag:+.3e} i (|D| {d[0]:.1e}); "
                  f"f(0) = {pr['f0']:.10f}")
    MODELL["art"] = "egpe"


def cmd_einheiten(a, erg, zeilen):
    """Petrov 2015, Gl. (7) und (9), gleiche Massen: n_i^(0), xi, tau aus a11, a22, a12 (in a0) und der Masse (u)."""
    a0 = 5.29177210903e-11
    hbar = 1.054571817e-34
    u = 1.66053906660e-27
    m = a.masse * u
    a11, a22, a12 = a.a11 * a0, a.a22 * a0, a.a12 * a0
    g11, g22 = 4 * PI * hbar ** 2 * a11 / m, 4 * PI * hbar ** 2 * a22 / m
    dg = 4 * PI * hbar ** 2 * (a12 + math.sqrt(a11 * a22)) / m
    s5 = (math.sqrt(a11) + math.sqrt(a22)) ** 5
    n1 = 25 * PI / 1024 * (a12 + math.sqrt(a11 * a22)) ** 2 / (a11 * a22 * math.sqrt(a11) * s5)
    n2 = 25 * PI / 1024 * (a12 + math.sqrt(a11 * a22)) ** 2 / (a11 * a22 * math.sqrt(a22) * s5)
    if a.n1 > 0:                               # Vorgabe n1 in cm^-3 (Kontrolle gegen Petrovs Beispiel)
        n1 = a.n1 * 1e6
        n2 = n1 * math.sqrt(a11 / a22)
    xi = math.sqrt(1.5 * (math.sqrt(g22) / m + math.sqrt(g11) / m) / (abs(dg) * math.sqrt(g11) * n1)) * hbar
    tau = 1.5 * (math.sqrt(g11) + math.sqrt(g22)) / (abs(dg) * math.sqrt(g11) * n1) * hbar
    zeilen.append(f"Einheiten (Petrov Gl. 7, 9; gleiche Massen {a.masse} u): a11 {a.a11}, a22 {a.a22}, a12 {a.a12} a0,"
                  f" delta a = {a.a12 + math.sqrt(a.a11 * a.a22):.4f} a0")
    zeilen.append(f"  n1(0) = {n1 * 1e-6:.4e} cm^-3, n2(0) = {n2 * 1e-6:.4e} cm^-3, xi = {xi * 1e6:.4f} um, "
                  f"tau = {tau * 1e3:.4f} ms, n0 xi^3 (N1 je N~) = {n1 * xi ** 3:.4e}, N je N~ (beide) = "
                  f"{(n1 + n2) * xi ** 3:.4e}")
    erg["einheiten"] = {"n1": n1, "n2": n2, "xi": xi, "tau": tau, "N1_je_Ntilde": n1 * xi ** 3,
                        "N_je_Ntilde": (n1 + n2) * xi ** 3}


def cmd_rauch(a, erg, zeilen):
    mus = [-0.10, -0.30, -0.45]
    prs = profile(mus, 0.5 * a.h)
    for p in prs:
        zeilen.append(f"Profil mu {p['mu']}: phi0 {p['f0']:.12f}, N~ {p['N']:.6f}, E~/N~ {p['E_durch_N']:.6f}, "
                      f"R_halb {p['R_halb']:.4f}, Anschluss {p['f_anschluss']:.1e} ({p['grund']}), R_aus {p['R_aus']:.1f}")
        lin = lin_aufbau(p, a.h)
        w, imd = gebunden_fuer(lin, 0, 0.005, 60)
        zeilen.append(f"  gebunden l=0: {w} (max|Im D| {imd:.1e}); Schwelle {-p['mu']:.4f}")
        es = np.linspace(-p["mu"] + 0.01, -p["mu"] + 0.8, 9)
        Wv, im = W_werte(lin, es, 0)
        zeilen.append("  W(eps): " + ", ".join(f"{e:.3f}:{w.real:+.3f}{w.imag:+.3f}i" for e, w in zip(es, Wv))
                      + f"  (Im-Rest {np.max(im):.1e})")
    # freie Negativkontrolle: kein Ball -> D ohne Nullstellen; Symplektik-Probe
    erg["rauch"] = [prof_kurz(p) for p in prs]


def argumente():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kommando", choices=["rauch", "profile", "gebunden", "pole", "wgitter", "umlauf", "einheiten",
                                         "qbkontrolle"])
    ap.add_argument("--beta", type=float, default=0.5)
    ap.add_argument("--qb-x", type=str, default="0.7964,0.7968,0.7972,0.7976,0.7980,0.7984,0.7988")
    ap.add_argument("--qb-x-neg", type=str, default="0.7996,0.8000,0.8004,0.8008")
    ap.add_argument("--qb-rho-von", type=float, default=1.735)
    ap.add_argument("--qb-rho-bis", type=float, default=1.755)
    ap.add_argument("--qb-n-rho", type=int, default=21)
    ap.add_argument("--qb-xstern", type=float, default=0.79767679)
    ap.add_argument("--qb-rhostern", type=float, default=1.7446175)
    ap.add_argument("--h", type=float, default=0.02)
    ap.add_argument("--l", type=int, default=0)
    ap.add_argument("--mu", type=str, default="")
    ap.add_argument("--mu-von", type=float, default=-0.30)
    ap.add_argument("--mu-bis", type=float, default=-0.10)
    ap.add_argument("--n-mu", type=int, default=5)
    ap.add_argument("--eps-min", type=float, default=0.002)
    ap.add_argument("--n-scan", type=int, default=200)
    ap.add_argument("--re-breite", type=float, default=0.8)
    ap.add_argument("--re-unter", type=float, default=0.0)
    ap.add_argument("--iters", type=int, default=40)
    ap.add_argument("--im-tiefe", type=float, default=0.2)
    ap.add_argument("--n-re", type=int, default=41)
    ap.add_argument("--n-im", type=int, default=11)
    ap.add_argument("--eps-von", type=float, default=0.3)
    ap.add_argument("--eps-bis", type=float, default=1.2)
    ap.add_argument("--n-eps", type=int, default=91)
    ap.add_argument("--eps0", type=float, default=0.5)
    ap.add_argument("--deps", type=float, default=0.01)
    ap.add_argument("--mu0", type=float, default=-0.3)
    ap.add_argument("--dmu", type=float, default=0.005)
    ap.add_argument("--n-kante", type=int, default=41)
    ap.add_argument("--n-kante-mu", type=int, default=21)
    ap.add_argument("--masse", type=float, default=38.9637)
    ap.add_argument("--a11", type=float, default=84.3)
    ap.add_argument("--a22", type=float, default=33.5)
    ap.add_argument("--a12", type=float, default=-56.16)
    ap.add_argument("--n1", type=float, default=0.0)
    ap.add_argument("--aus", type=str, default="aus")
    ap.add_argument("--name", type=str, default="")
    return ap.parse_args()


def main():
    a = argumente()
    name = a.name or a.kommando
    os.makedirs(a.aus, exist_ok=True)
    zeilen = [f"mess1.py {a.kommando} ({name}), Start {jetzt()}", "Argumente: " + json.dumps(vars(a))]
    erg = {"argumente": vars(a), "start": jetzt()}
    rc = 0
    try:
        {"rauch": cmd_rauch, "profile": cmd_profile, "gebunden": cmd_gebunden, "pole": cmd_pole,
         "wgitter": cmd_wgitter, "umlauf": cmd_umlauf, "einheiten": cmd_einheiten,
         "qbkontrolle": cmd_qbkontrolle}[a.kommando](a, erg, zeilen)
    except Exception as ex:  # Sicherheitsnetz wie bic2 v2
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
