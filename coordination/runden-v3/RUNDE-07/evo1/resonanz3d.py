#!/usr/bin/env python3
"""Runde 6 (runden-v3): die langlebige Q-Ball-Resonanz aus 1D in 3D, radial je Drehimpuls l. Explorativ.

Lokal nur Rauchtest und Zeitproben (Freigabe laut Leitung 30.09. 02:42); Messlaeufe ungerechnet. Plan: PLAN.md.

Modell: L = |phi_t|^2 - |grad phi|^2 - U(S), U = S - S^2 + beta S^3, S = |phi|^2, beta = 1/2 (Ciurla-Probe beta = 1/4).
Grundzustand phi = f(r) exp(-i omega t) in dim Raumdimensionen (dim = 3; die Dimensionsbruecke laeuft dim = 1 ... 3).
Stoerung phi = [f + u(r) e^{-i rho t} + v*(r) e^{+i rho* t}] e^{-i omega t} Y_lm. Reduziert U = r^{(dim-1)/2} u usw.:
    U'' = [dp + c_nu/r^2 - (omega + rho)^2] U + sp V
    V'' = sp U + [dp + c_nu/r^2 - (omega - rho)^2] V
    dp = 1 - 4 S + 9 beta S^2,  sp = -2 S + 6 beta S^2,  nu = l + (dim-1)/2,  c_nu = nu (nu - 1)  (dim = 3: l(l+1)).
Pol: regulaer bei r = 0 (U, V ~ r^nu), auslaufend im Kanal omega + rho, abklingend im Kanal omega - rho. Abklingende
Pole haben Im rho < 0 (Konvention wie Codex in resonance-20260930/linear; Ciurla u. a. benutzen die konjugierte).
Verfahren: Verbundmatrix (Pluecker-Koordinaten der zwei 2-Ebenen "regulaer" und "Jost"), damit die im Kern
exponentiell wachsenden Loesungen die lineare Unabhaengigkeit nicht zerstoeren (duennwandige Baelle). Die Invariante
p13 + p24 = 0 (symplektisch, beide Ebenen Lagrange) spart eine Komponente. D(rho) = normierte 4x4-Determinante
= <p, q> (Laplace-Entwicklung); Nullstellen = Pole. Positive Normierungen aendern weder Nullstellen noch Umlaufzahl.

Kommandos: rauch | pole | bruecke | zeit0 | zeitlin   (Einzelheiten: python resonanz3d.py <kommando> -h)
Geraet: --geraet cpu (Vorgabe) oder cuda, alles float64 / complex128.
"""
import argparse
import cmath
import datetime
import json
import math
import os
import time

import torch

F64 = torch.float64
C128 = torch.complex128
PI = math.pi
BETA = 0.5
T_START = time.perf_counter()
SIGMA0 = 1.0          # Daempfungsstaerke der Randschicht (wie tests1d)
CODEX_1D = complex(1.49377696454877, -6.71596847535e-5)    # resonance-20260930/linear/RESULT.txt, R32
CIURLA_1D = complex(1.53878955094988, -1.17883363642e-5)   # dieselbe Datei, Kalibrierung beta = 1/4, omega^2 = 3/4


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    return time.perf_counter() - T_START


class Budget:
    """Zeitwaechter: jede Stufe fragt vorher; RuntimeMaxSec der Unit ist 600 s."""
    def __init__(self, sek):
        self.sek = sek
        self.abgebrochen = []

    def ok(self, was, reserve=0.0):
        if uhr() + reserve < self.sek:
            return True
        self.abgebrochen.append(f"{was} (bei {uhr():.0f} s)")
        print(f"ZEIT: {was} entfaellt ({uhr():.0f} s von {self.sek:.0f} s)", flush=True)
        return False


def zahl(z):
    if isinstance(z, complex):
        return [z.real, z.imag]
    return z


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, complex):
        return [x.real, x.imag]
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return x


def fz(z, n=10):
    """complex -> Text"""
    return f"{z.real:.{n}f} {'-' if z.imag < 0 else '+'} {abs(z.imag):.3e} i"


# ================================================================ Grundzustand (Schiessen in u = f_top - f)

def koeffizienten(a0, beta):
    """f_top = sqrt(S+) (Buckel des Teilchenpotentials) und Taylor-Koeffizienten von F(f) = a0 f - 2 f^3 + 3 beta f^5
    um f_top: F(f_top + v) = c1 v + ... + c5 v^5 (exakt, F(f_top) = 0). Fuer beta = 1/2 wie tests1d.koeffizienten."""
    disk = 4.0 - 12.0 * beta * a0
    if disk <= 0.0:
        raise ValueError("kein Buckel: 4 - 12 beta a0 <= 0")
    s_top = (2.0 + math.sqrt(disk)) / (6.0 * beta)
    t = math.sqrt(s_top)
    c = (a0 - 6.0 * s_top + 15.0 * beta * s_top * s_top, -6.0 * t + 30.0 * beta * t * s_top,
         -2.0 + 30.0 * beta * s_top, 15.0 * beta * t, 3.0 * beta)
    return t, c


def g_u(u, c):
    """G(u) = -F(f_top - u) = c1 u - c2 u^2 + c3 u^3 - c4 u^4 + c5 u^5."""
    c1, c2, c3, c4, c5 = c
    return u * (c1 + u * (-c2 + u * (c3 + u * (-c4 + u * c5))))


def g_strich(u, c):
    c1, c2, c3, c4, c5 = c
    return c1 + u * (-2.0 * c2 + u * (3.0 * c3 + u * (-4.0 * c4 + u * 5.0 * c5)))


def rk4_u(r, u, up, h, c, dm1):
    """RK4 fuer u'' = G(u) - (dim-1)/r u'  (u = f_top - f)."""
    def ab(rr, uu, pp):
        return pp, g_u(uu, c) - (dm1 / rr) * pp
    k1u, k1p = ab(r, u, up)
    k2u, k2p = ab(r + 0.5 * h, u + 0.5 * h * k1u, up + 0.5 * h * k1p)
    k3u, k3p = ab(r + 0.5 * h, u + 0.5 * h * k2u, up + 0.5 * h * k2p)
    k4u, k4p = ab(r + h, u + h * k3u, up + h * k3p)
    return (u + (h / 6.0) * (k1u + 2.0 * k2u + 2.0 * k3u + k4u),
            up + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p))


def start_reihe(s, c, dm1, h):
    """u = u0 + a r^2 + b r^4 um r = 0, a = G(u0)/(2 dim), b = G'(u0) a/(4 dim + 8); Werte bei r = h."""
    d = dm1 + 1.0
    u0 = torch.exp(-s)
    a = g_u(u0, c) / (2.0 * d)
    b = g_strich(u0, c) * a / (4.0 * d + 8.0)
    return u0, u0 + a * h * h + b * h ** 4, 2.0 * a * h + 4.0 * b * h ** 3


def einschachteln(lo, hi, t, c, dm1, h, dev, runden, n_kand, r_max):
    """Klammer in s = -ln(f_top - f(0)): grosses s = Ueberschuss (f < 0), kleines s = Unterschuss (f' > 0).
    Rueckgabe lo, hi und ob in der ersten Runde beide Enden richtig lagen (Klammer gueltig)."""
    n_max = int(round(r_max / h))
    stufen = torch.linspace(0.0, 1.0, n_kand, dtype=F64, device=dev)
    gueltig = True
    for rnd in range(runden):
        s = lo + (hi - lo) * stufen
        _, u, up = start_reihe(s, c, dm1, h)
        zustand = torch.zeros_like(s)
        for k in range(1, n_max):
            u, up = rk4_u(k * h, u, up, h, c, dm1)
            ueber = (zustand == 0) & (u > t)
            unter = (zustand == 0) & (u <= t) & (up < 0)
            zustand = zustand + ueber.to(F64) - unter.to(F64)
            lebt = (zustand == 0).to(F64)
            u = u * lebt
            up = up * lebt
            if k % 100 == 0 and not bool((zustand == 0).any()):
                break
        if rnd == 0:
            gueltig = bool(zustand[0] < 0) and bool(zustand[-1] > 0)
        unter_s = s[zustand < 0]
        ueber_s = s[zustand > 0]
        if unter_s.numel() > 0:
            lo = max(lo, float(unter_s.max()))
        if ueber_s.numel() > 0:
            hi = min(hi, float(ueber_s.min()))
    return lo, hi, gueltig


def profil(w2, dim, beta, h, dev, f_schwanz=1e-5, n_kand=1024):
    """Profil f(r_j), r_j = j h, bis r_cut; danach Schwanz f_c (r_c/r)^((dim-1)/2) exp(-kappa (r - r_c)).
    Grob (h = 0,05, 2 Runden) einschachteln, dann fein (Schritt h, 4 Runden) im Fenster +-0,02 um die grobe Klammer;
    ist die feine Klammer ungueltig, 5 feine Runden im vollen Fenster."""
    a0 = 1.0 - w2
    dm1 = dim - 1.0
    t, c = koeffizienten(a0, beta)
    lo0, hi0 = -math.log(t - 1e-3), 150.0
    lo, hi, _ = einschachteln(lo0, hi0, t, c, dm1, 0.05, dev, 2, n_kand, 130.0)
    lo_f, hi_f = max(lo0, lo - 0.02), min(hi0, hi + 0.02)
    lo2, hi2, gueltig = einschachteln(lo_f, hi_f, t, c, dm1, h, dev, 4, n_kand, 130.0)
    rueckfall = not gueltig
    if rueckfall:
        lo2, hi2, gueltig = einschachteln(lo0, hi0, t, c, dm1, h, dev, 5, n_kand, 130.0)
    s_mid = 0.5 * (lo2 + hi2)
    s3 = torch.tensor([lo2, s_mid, hi2], dtype=F64, device=dev)
    u0, u, up = start_reihe(s3, c, dm1, h)
    f0 = t - float(u0[1])
    f2 = -float(g_u(u0[1:2], c)[0]) / (2.0 * (dm1 + 1.0))
    bu, bp = [(t - u0).cpu(), torch.zeros(3, dtype=F64)], [None, None]
    bu[1] = (t - u).cpu()
    bp[0] = torch.zeros(3, dtype=F64)
    bp[1] = (-up).cpu()
    n_max = int(round(130.0 / h))
    grund, j_cut = 0, None
    k = 1
    while k < n_max and j_cut is None:
        stueck_f, stueck_p = [], []
        for _ in range(50):
            if k >= n_max:
                break
            u, up = rk4_u(k * h, u, up, h, c, dm1)
            stueck_f.append(t - u)
            stueck_p.append(-up)
            k += 1
        if not stueck_f:
            break
        sf = torch.stack(stueck_f).cpu()                  # (n, 3)
        sp = torch.stack(stueck_p).cpu()
        fm = sf[:, 1]
        streu = (sf[:, 2] - sf[:, 0]).abs()
        bed = [(fm < f_schwanz * f0, 1), (sp[:, 1] > 0, 2), (fm < 0, 3), (streu > 1e-2 * fm.abs(), 4)]
        erst = None
        for maske, g in bed:
            idx = torch.nonzero(maske)
            if idx.numel() > 0:
                i = int(idx[0])
                if erst is None or i < erst[0]:
                    erst = (i, g)
        j_anfang = len(bu)
        for i in range(sf.shape[0]):
            bu.append(sf[i])
            bp.append(sp[i])
        if erst is not None:
            j_cut = max(1, j_anfang + erst[0] - 1)
            grund = erst[1]
    if j_cut is None:
        j_cut = len(bu) - 1
    f_liste = [float(bu[j][1]) for j in range(j_cut + 1)]
    fp_liste = [float(bp[j][1]) for j in range(j_cut + 1)]
    streuung = float((bu[j_cut][2] - bu[j_cut][0]).abs())
    return {"w2": w2, "dim": dim, "beta": beta, "h": h, "t": t, "f0": f0, "f2": f2, "s": s_mid, "klammer": hi2 - lo2,
            "rueckfall": rueckfall, "j_cut": j_cut, "r_cut": j_cut * h, "grund": grund, "streuung_cut": streuung,
            "f": f_liste, "fp": fp_liste, "kappa": math.sqrt(a0), "dm1": dm1}


def f_werte(prof, n):
    """f und f' an r_j = j h, j = 0 .. n-1 (Schwanzformel jenseits von r_cut)."""
    jc, h = prof["j_cut"], prof["h"]
    fc, rc, ka, dm1 = prof["f"][jc], jc * h, prof["kappa"], prof["dm1"]
    f, fp = list(prof["f"][:n]), list(prof["fp"][:n])
    for j in range(len(f), n):
        r = j * h
        w = fc * (rc / r) ** (0.5 * dm1) * math.exp(-ka * (r - rc))
        f.append(w)
        fp.append(w * (-ka - 0.5 * dm1 / r))
    return f, fp


def radius_wo(prof, wert):
    """kleinstes r mit f(r) < wert (Schwanzformel, ohne Potenzfaktor: eher zu gross)."""
    jc, h = prof["j_cut"], prof["h"]
    for j in range(jc + 1):
        if prof["f"][j] < wert:
            return j * h
    fc = prof["f"][jc]
    return jc * h + max(0.0, math.log(fc / wert)) / prof["kappa"]


def r_halb(prof):
    """Radius, bei dem S = f^2 auf S(0)/2 faellt (lineare Interpolation)."""
    s0 = prof["f0"] ** 2
    f = prof["f"]
    for j in range(1, len(f)):
        if f[j] ** 2 < 0.5 * s0:
            a, b = f[j - 1] ** 2 - 0.5 * s0, f[j] ** 2 - 0.5 * s0
            return (j - 1 + a / (a - b)) * prof["h"]
    return len(f) * prof["h"]


def kennzahlen_3d(prof):
    """Q, E, Radien, Wandspannung, Enthalpiedichte und Rayleigh-Frequenz (nur dim = 3)."""
    w2, beta, h = prof["w2"], prof["beta"], prof["h"]
    om = math.sqrt(w2)
    n = int(radius_wo(prof, 1e-12 * prof["f0"]) / h) + 2
    f, fp = f_werte(prof, n)
    iq = ie = ig = 0.0
    jmax, fpmax = 0, 0.0
    for j in range(n):
        r = j * h
        gew = 0.5 * h if j in (0, n - 1) else h
        s = f[j] ** 2
        us = s - s * s + beta * s ** 3
        iq += gew * s * r * r
        ig += gew * fp[j] ** 2 * r * r
        ie += gew * (w2 * s + fp[j] ** 2 + us) * r * r
        if abs(fp[j]) > fpmax:
            fpmax, jmax = abs(fp[j]), j
    q = 8.0 * PI * om * iq
    e = 4.0 * PI * ie
    s0 = prof["f0"] ** 2
    u0 = s0 - s0 * s0 + beta * s0 ** 3
    n_in = 2.0 * om * s0
    w_in = 2.0 * w2 * s0                  # Enthalpiedichte eps + p = omega n (Traegheit im Rayleigh-Ansatz)
    eps_in = w2 * s0 + u0
    p_in = w2 * s0 - u0
    r_q = (3.0 * q / (4.0 * PI * n_in)) ** (1.0 / 3.0)
    r_h = r_halb(prof)
    r_g = jmax * h
    sig_grad = 2.0 * ig / (r_q * r_q)     # 2 int |grad f|^2 d^3x / (4 pi R_Q^2)
    sig_lap = 0.5 * p_in * r_q            # Laplace: p_in = 2 sigma / R
    s_stern = 1.0 / (2.0 * beta)
    sig_kink = math.sqrt(beta) * s_stern ** 2 / 2.0     # Wand bei omega_min (beta = 1/2: 1/(2 sqrt 2))
    varianten = {}
    for sn, sv in (("grad", sig_grad), ("laplace", sig_lap), ("kink", sig_kink)):
        for rn, rv in (("R_Q", r_q), ("R_halb", r_h)):
            for wn, wv in (("w", w_in), ("eps", eps_in)):
                varianten[f"{sn}/{rn}/{wn}"] = math.sqrt(8.0 * sv / (wv * rv ** 3))
    werte = list(varianten.values())
    return {"Q": q, "E": e, "S0": s0, "n_in": n_in, "w_in": w_in, "eps_in": eps_in, "p_in": p_in, "R_Q": r_q,
            "R_halb": r_h, "R_gradmax": r_g, "sigma_grad": sig_grad, "sigma_laplace": sig_lap, "sigma_kink": sig_kink,
            "omega_R_haupt": varianten["grad/R_Q/w"], "omega_R_min": min(werte), "omega_R_max": max(werte),
            "omega_R_varianten": varianten}


# ================================================================ lineares Randwertproblem (Verbundmatrix)

def lin_aufbau(prof, h, f_rand, frei=False, r_min=20.0):
    """Gitter r_k = k h (Profil mit Schritt h/2 fuer die RK4-Mittelpunkte), Aussenrand R bei f(R) = f_rand f0,
    Anschluss bei R_halb. frei=True: Negativkontrolle ohne Ball (dp = 1, sp = 0)."""
    if abs(prof["h"] - 0.5 * h) > 1e-12:
        raise ValueError("Profil braucht Schritt h/2")
    w2, beta = prof["w2"], prof["beta"]
    r_aus = max(r_min, radius_wo(prof, f_rand * prof["f0"]))
    K = int(math.ceil(r_aus / h))
    Km = max(1, min(K - 1, int(round(r_halb(prof) / h))))
    f, _ = f_werte(prof, 2 * K + 1)
    dv, sv, cf = [], [], [0.0]
    for j in range(2 * K + 1):
        s = 0.0 if frei else f[j] ** 2
        dv.append(1.0 - 4.0 * s + 9.0 * beta * s * s)
        sv.append(-2.0 * s + 6.0 * beta * s * s)
        if j > 0:
            cf.append(1.0 / (j * 0.5 * h) ** 2)
    if frei:
        reihe = (1.0, 0.0, 0.0, 0.0)
    else:
        s0 = prof["f0"] ** 2
        s2 = 2.0 * prof["f0"] * prof["f2"]
        reihe = (1.0 - 4.0 * s0 + 9.0 * beta * s0 * s0, (-4.0 + 18.0 * beta * s0) * s2,
                 -2.0 * s0 + 6.0 * beta * s0 * s0, (-2.0 + 12.0 * beta * s0) * s2)
    return {"h": h, "K": K, "Km": Km, "R_aus": K * h, "r_m": Km * h, "omega": math.sqrt(w2), "dv": dv, "sv": sv,
            "cf": cf, "reihe": reihe, "frei": frei, "dev": None}


def normieren(P):
    m = torch.stack([p.abs() for p in P]).amax(0)
    return [p / m for p in P]


def norm5(P):
    p12, p13, p14, p23, p34 = P
    return torch.sqrt(p12.abs() ** 2 + 2.0 * p13.abs() ** 2 + p14.abs() ** 2 + p23.abs() ** 2 + p34.abs() ** 2)


def abl(P, m11, m22, s):
    """Verbundsystem fuer (p12, p13, p14, p23, p34), p24 = -p13 (1 = U, 2 = V, 3 = U', 4 = V')."""
    p12, p13, p14, p23, p34 = P
    return [p14 - p23,
            s * p12,
            p34 + m22 * p12,
            -(p34 + m11 * p12),
            m11 * p14 - m22 * p23 - (2.0 * s) * p13]


def rk4_schritt(P, j0, sg, hs, lin, cnu, wp2, wm2):
    dv, sv, cf = lin["dv"], lin["sv"], lin["cf"]
    j1, j2 = j0 + sg, j0 + 2 * sg
    b0 = cnu * cf[j0] + dv[j0]
    b1 = cnu * cf[j1] + dv[j1]
    b2 = cnu * cf[j2] + dv[j2]
    m11a, m22a = b0 - wp2, b0 - wm2
    m11b, m22b = b1 - wp2, b1 - wm2
    m11c, m22c = b2 - wp2, b2 - wm2
    k1 = abl(P, m11a, m22a, sv[j0])
    k2 = abl([torch.add(p, k, alpha=0.5 * hs) for p, k in zip(P, k1)], m11b, m22b, sv[j1])
    k3 = abl([torch.add(p, k, alpha=0.5 * hs) for p, k in zip(P, k2)], m11b, m22b, sv[j1])
    k4 = abl([torch.add(p, k, alpha=hs) for p, k in zip(P, k3)], m11c, m22c, sv[j2])
    return [torch.add(p, torch.add(a + d, b + c, alpha=2.0), alpha=hs / 6.0) for p, a, b, c, d in zip(P, k1, k2, k3, k4)]


def reg_start(lin, nu, wp2, wm2):
    """Zwei regulaere Loesungen bei r = h aus der Reihe U = r^nu (a0 + a2 r^2 + a4 r^4), V ebenso; der gemeinsame
    Faktor r^nu ist weggelassen (positiv). Rekursion n (n + 2 nu - 1) a_n = ... ."""
    r = lin["h"]
    d0, d2, s0, s2 = lin["reihe"]
    A = d0 - wp2
    B = d0 - wm2
    n2 = 2.0 * (2.0 * nu + 1.0)
    n4 = 4.0 * (2.0 * nu + 3.0)
    a2 = A / n2                                  # Loesung a: a0 = 1, b0 = 0
    b2 = s0 / n2
    a4 = (A * a2 + s0 * b2 + d2) / n4
    b4 = (s0 * a2 + B * b2 + s2) / n4
    c2 = s0 / n2                                 # Loesung b: a0 = 0, b0 = 1
    e2 = B / n2
    c4 = (A * c2 + s0 * e2 + s2) / n4
    e4 = (s0 * c2 + B * e2 + d2) / n4
    r2, r3, r4 = r * r, r ** 3, r ** 4
    aU = 1.0 + a2 * r2 + a4 * r4
    aV = b2 * r2 + b4 * r4
    aUp = nu * aU / r + 2.0 * a2 * r + 4.0 * a4 * r3
    aVp = nu * aV / r + 2.0 * b2 * r + 4.0 * b4 * r3
    bU = c2 * r2 + c4 * r4
    bV = 1.0 + e2 * r2 + e4 * r4
    bUp = nu * bU / r + 2.0 * c2 * r + 4.0 * c4 * r3
    bVp = nu * bV / r + 2.0 * e2 * r + 4.0 * e4 * r3
    return [aU * bV - aV * bU, aU * bUp - aUp * bU, aU * bVp - aVp * bU, aV * bUp - aUp * bV, aUp * bVp - aVp * bUp]


def hankel(q, R, nu, M=16):
    """w = exp(i q r) P(q r), P = sum_m i^m a_m(mu) (q r)^-m, mu = nu - 1/2, a_m = prod (4mu^2 - (2j-1)^2)/(m! 8^m).
    Fuer ganzzahliges nu (dim = 1, 3) bricht die Reihe ab (exakt); sonst asymptotisch, abgeschnitten beim kleinsten
    Glied. Rueckgabe P(qR) und Q = w'(R)/exp(i q R). Der gemeinsame Faktor exp(i q R) wird weggelassen."""
    z = q * R
    mu2 = 4.0 * (nu - 0.5) ** 2
    endlich = (nu - torch.round(nu)).abs() < 1e-12
    term = torch.ones_like(z)
    P = torch.ones_like(z)
    dP = torch.zeros_like(z)
    aktiv = torch.ones(z.shape, dtype=torch.bool, device=z.device)
    alt = term.abs()
    for m in range(1, M + 1):
        term = term * (1j * (mu2 - (2 * m - 1) ** 2) / (8.0 * m)) / z
        b = term.abs()
        aktiv = aktiv & (endlich | (b < alt))
        alt = b
        null = torch.zeros_like(term)
        P = P + torch.where(aktiv, term, null)
        dP = dP + torch.where(aktiv, -m * term / z, null)
    return P, q * (1j * P + dP)


def jost_start(lin, rho, nu, wp2, wm2):
    """Kanal omega + rho: auslaufend exp(+i q+ r), q+ = sqrt((omega+rho)^2 - 1) (Hauptzweig, Re q+ > 0); fuer reelles
    rho unter der Kante q+ = i sqrt(1 - (omega+rho)^2) (abklingend). Kanal omega - rho: abklingend, q- = i kappa-,
    kappa- = sqrt(1 - (omega-rho)^2). z1 = (w+, 0, w+', 0), z2 = (0, w-, 0, w-')."""
    R = lin["R_aus"]
    qp = torch.sqrt(wp2 - 1.0)
    unter = (wp2.real < 1.0) & (rho.imag == 0)
    qp = torch.where(unter, 1j * torch.sqrt(1.0 - wp2), qp)
    qm = 1j * torch.sqrt(1.0 - wm2)
    Pp, Qp = hankel(qp, R, nu)
    Pm, Qm = hankel(qm, R, nu)
    return [Pp * Pm, torch.zeros_like(Pp), Pp * Qm, -Qp * Pm, Qp * Qm]


def det(lin, rho, nu):
    """Normierte Anschlussdeterminante D(rho) fuer einen Stapel (rho_i, nu_i)."""
    dev = lin["dev"]
    rho = rho.to(device=dev, dtype=C128)
    nu = nu.to(device=dev, dtype=F64)
    om, h, K, Km = lin["omega"], lin["h"], lin["K"], lin["Km"]
    cnu = nu * (nu - 1.0)
    wp2 = (om + rho) ** 2
    wm2 = (om - rho) ** 2
    P = normieren(reg_start(lin, nu, wp2, wm2))
    for k in range(1, Km):
        P = rk4_schritt(P, 2 * k, 1, h, lin, cnu, wp2, wm2)
        if k % 16 == 0:
            P = normieren(P)
    Q = normieren(jost_start(lin, rho, nu, wp2, wm2))
    for i, k in enumerate(range(K, Km, -1)):
        Q = rk4_schritt(Q, 2 * k, -1, -h, lin, cnu, wp2, wm2)
        if i % 16 == 15:
            Q = normieren(Q)
    P = normieren(P)
    Q = normieren(Q)
    D = P[0] * Q[4] + P[4] * Q[0] + P[2] * Q[3] + P[3] * Q[2] + 2.0 * P[1] * Q[1]
    # Phasenfaktor g/|g|, g = exp(i (q+ + q-) (R - r_m)) analytisch und ohne Nullstellen: aendert weder Nullstellen
    # noch Umlaufzahl, nimmt aber die schnelle Phase exp(-i q R) aus der Jost-Normierung heraus (Kontur aufloesbar).
    qp = torch.sqrt(wp2 - 1.0)
    qp = torch.where((wp2.real < 1.0) & (rho.imag == 0), 1j * torch.sqrt(1.0 - wp2), qp)
    qm = 1j * torch.sqrt(1.0 - wm2)
    phase = torch.exp(1j * ((qp + qm) * (lin["R_aus"] - lin["r_m"])).real)
    return D / (norm5(P) * norm5(Q)) * phase


def det_liste(lin, rhos, nus):
    rho = torch.tensor([complex(z) for z in rhos], dtype=C128)
    nu = torch.tensor([float(v) for v in nus], dtype=F64)
    return [complex(z) for z in det(lin, rho, nu).cpu().tolist()]


def newton(lin, rhos, nus, iters=30, tol=1e-12, schritt_max=0.05, delta=1e-7):
    """2D-Newton auf (Re D, Im D) mit Vorwaertsdifferenzen (D ist wegen der positiven Normierung nicht analytisch,
    die Nullstelle ist trotzdem regulaer). Nur fuer komplexe Resonanzen (fuer reelle gebundene Zustaende: illinois)."""
    rho = [complex(z) for z in rhos]
    nu = list(nus)
    n = len(rho)
    aktiv = list(range(n))
    konv = [False] * n
    it_n = [0] * n
    for it in range(iters):
        if not aktiv:
            break
        batch = [rho[i] for i in aktiv] + [rho[i] + delta for i in aktiv] + [rho[i] + 1j * delta for i in aktiv]
        D = det_liste(lin, batch, [nu[i] for i in aktiv] * 3)
        m = len(aktiv)
        neu = []
        for a, i in enumerate(aktiv):
            d0, dx, dy = D[a], D[m + a], D[2 * m + a]
            j11, j21 = (dx - d0).real / delta, (dx - d0).imag / delta
            j12, j22 = (dy - d0).real / delta, (dy - d0).imag / delta
            dd = j11 * j22 - j12 * j21
            if dd == 0.0 or not math.isfinite(dd):
                continue
            sx = -(j22 * d0.real - j12 * d0.imag) / dd
            sy = -(-j21 * d0.real + j11 * d0.imag) / dd
            st = complex(sx, sy)
            if abs(st) > schritt_max:
                st = st * (schritt_max / abs(st))
            rho[i] = rho[i] + st
            it_n[i] = it + 1
            if abs(st) < tol * max(1.0, abs(rho[i])):
                konv[i] = True
            else:
                neu.append(i)
        aktiv = neu
    Dend = det_liste(lin, rho, nu) if n else []
    return [{"rho": rho[i], "nu": nu[i], "absD": abs(Dend[i]), "konvergiert": konv[i], "iter": it_n[i]}
            for i in range(n)]


def illinois(lin, a, b, fa, fb, nus, iters=40, tol=1e-12):
    """Reelle Nullstellen von Re D in Klammern [a, b] (gebundene Zustaende unter der Kante), Illinois-Verfahren."""
    a, b, fa, fb = list(a), list(b), list(fa), list(fb)
    n = len(a)
    for _ in range(iters):
        offen = [i for i in range(n) if abs(b[i] - a[i]) > tol * max(1.0, abs(b[i]))]
        if not offen:
            break
        c = {}
        for i in offen:
            x = b[i] - fb[i] * (b[i] - a[i]) / (fb[i] - fa[i]) if fb[i] != fa[i] else 0.5 * (a[i] + b[i])
            lo, hi = min(a[i], b[i]), max(a[i], b[i])
            if not (lo < x < hi):
                x = 0.5 * (a[i] + b[i])
            c[i] = x
        D = det_liste(lin, [complex(c[i], 0.0) for i in offen], [nus[i] for i in offen])
        for k, i in enumerate(offen):
            fc = D[k].real
            if fc * fb[i] < 0:
                a[i], fa[i] = b[i], fb[i]
            else:
                fa[i] = 0.5 * fa[i]
            b[i], fb[i] = c[i], fc
            if fc == 0.0:
                a[i] = b[i]
    return [{"rho": b[i], "nu": nus[i], "klammer": abs(b[i] - a[i])} for i in range(n)]


def lokale_minima(werte):
    return [i for i in range(1, len(werte) - 1) if werte[i] < werte[i - 1] and werte[i] <= werte[i + 1]]


def kontur(lin, nus, x0, x1, y0, y1, n_kante, runden, max_punkte):
    """Argumentprinzip: Zahl der Nullstellen von D im Kasten [x0, x1] x [y0, y1], je nu. Adaptive Verfeinerung, bis
    jeder Phasensprung |d arg| < 0,4 ist. D ist bis auf positive Faktoren analytisch, ohne Pole im Kasten."""
    nb, nr, no, nl = n_kante

    def lin_pkt(a, b, n):
        return [a + (b - a) * i / n for i in range(n)]
    grund = ([complex(x, y0) for x in lin_pkt(x0, x1, nb)] + [complex(x1, y) for y in lin_pkt(y0, y1, nr)] +
             [complex(x, y1) for x in lin_pkt(x1, x0, no)] + [complex(x0, y) for y in lin_pkt(y1, y0, nl)])
    pkt = {v: list(grund) for v in nus}
    alle = [z for v in nus for z in pkt[v]]
    D = det_liste(lin, alle, [v for v in nus for _ in pkt[v]])
    wert = {}
    o = 0
    for v in nus:
        wert[v] = D[o:o + len(pkt[v])]
        o += len(pkt[v])
    for _ in range(runden):
        neu_pkt, neu_nu, stellen = [], [], {}
        for v in nus:
            z, d = pkt[v], wert[v]
            st = []
            for i in range(len(z)):
                j = (i + 1) % len(z)
                if d[i] == 0 or d[j] == 0 or abs(cmath.phase(d[j] / d[i])) > 0.4:
                    st.append(i)
            if len(z) + len(st) > max_punkte:
                st = []
            stellen[v] = st
            for i in st:
                j = (i + 1) % len(z)
                neu_pkt.append(0.5 * (z[i] + z[j]))
                neu_nu.append(v)
        if not neu_pkt:
            break
        Dn = det_liste(lin, neu_pkt, neu_nu)
        o = 0
        for v in nus:
            st = stellen[v]
            mitte = Dn[o:o + len(st)]
            mz = neu_pkt[o:o + len(st)]
            o += len(st)
            z, d = pkt[v], wert[v]
            nz, nd = [], []
            k = 0
            for i in range(len(z)):
                nz.append(z[i])
                nd.append(d[i])
                if k < len(st) and st[k] == i:
                    nz.append(mz[k])
                    nd.append(mitte[k])
                    k += 1
            pkt[v], wert[v] = nz, nd
    erg = {}
    for v in nus:
        d = wert[v]
        sprung = [cmath.phase(d[(i + 1) % len(d)] / d[i]) if d[i] != 0 else 0.0 for i in range(len(d))]
        w = sum(sprung) / (2.0 * PI)
        erg[v] = {"umlauf_roh": w, "umlauf": int(round(w)), "punkte": len(d), "max_sprung": max(abs(s) for s in sprung),
                  "aufgeloest": max(abs(s) for s in sprung) <= 0.4, "min_absD_rand": min(abs(x) for x in d)}
    return erg


# ================================================================ Kommando pole

def pole_omega(w2, l_liste, h_liste, bereich, a, dev, budget, zeilen):
    om = math.sqrt(w2)
    kante, oben = 1.0 - om, 1.0 + om
    f_rand = [1e-6, 1e-8, 1e-10][:len(h_liste)] if len(h_liste) <= 3 else [1e-8] * len(h_liste)
    iB = len(h_liste) // 2
    nus = [float(l) + 1.0 for l in l_liste]            # dim = 3: nu = l + 1
    erg = {"omega2": w2, "omega": om, "kante_unten": kante, "kante_oben": oben, "l": l_liste, "stufen": {}}
    zeilen.append(f"=== omega^2 = {w2}: Kanten 1 - omega = {kante:.6f}, 1 + omega = {oben:.6f}")

    def stufe(i):
        t0 = uhr()
        prof = profil(w2, 3.0, BETA, 0.5 * h_liste[i], dev)
        lin = lin_aufbau(prof, h_liste[i], f_rand[i])
        lin["dev"] = dev
        info = {"h": h_liste[i], "f_rand": f_rand[i], "R_aus": lin["R_aus"], "r_m": lin["r_m"], "f0": prof["f0"],
                "S0": prof["f0"] ** 2, "r_cut": prof["r_cut"], "grund": prof["grund"], "klammer_s": prof["klammer"],
                "rueckfall": prof["rueckfall"], "streuung_cut": prof["streuung_cut"], "sek_profil": uhr() - t0}
        return prof, lin, info

    profB, linB, infoB = stufe(iB)
    kz = kennzahlen_3d(profB)
    erg["kennzahlen"] = kz
    erg["stufen"][str(h_liste[iB])] = infoB
    zeilen.append(f"  Profil (h/2 = {0.5 * h_liste[iB]}): S0 = {kz['S0']:.6f}, Q = {kz['Q']:.5e}, E = {kz['E']:.5e}, "
                  f"R_Q = {kz['R_Q']:.4f}, R_halb = {kz['R_halb']:.4f}, Grund {profB['grund']}, r_cut {profB['r_cut']:.2f}")
    zeilen.append(f"  Wand: sigma grad/Laplace/kink = {kz['sigma_grad']:.5f}/{kz['sigma_laplace']:.5f}/"
                  f"{kz['sigma_kink']:.5f}, w = {kz['w_in']:.5f}; Rayleigh omega_2 = {kz['omega_R_haupt']:.6f} "
                  f"(Band {kz['omega_R_min']:.6f} .. {kz['omega_R_max']:.6f})")
    zeilen.append(f"  Rand R = {linB['R_aus']:.2f}, Anschluss r_m = {linB['r_m']:.2f}, K = {linB['K']}")

    # ---- Kontrollen bei rho = 0 (Null-Moden: l = 0 Phase/Ladung, l = 1 Translation/Boost; Jordan-Kette -> D ~ rho^2)
    t0 = uhr()
    eps = a.null_eps
    rh = [complex(0.0, 0.0), complex(eps, 0.0), complex(2 * eps, 0.0)]
    D = det_liste(linB, [z for _ in nus for z in rh], [v for v in nus for _ in rh])
    sek_pass = uhr() - t0
    null = {}
    for i, l in enumerate(l_liste):
        d0, d1, d2 = D[3 * i], D[3 * i + 1], D[3 * i + 2]
        null[l] = {"absD0": abs(d0), "absD_eps": abs(d1), "absD_2eps": abs(d2),
                   "verhaeltnis_2eps_eps": abs(d2) / abs(d1) if abs(d1) > 0 else float("nan"),
                   "D0_durch_Deps": abs(d0) / abs(d1) if abs(d1) > 0 else float("nan")}
        zeilen.append(f"  Nullmoden l = {l}: |D(0)| = {abs(d0):.3e}, |D({eps})| = {abs(d1):.3e}, |D(2 eps)|/|D(eps)| = "
                      f"{null[l]['verhaeltnis_2eps_eps']:.4f} (Nullmode: ~4 und |D(0)|/|D(eps)| << 1)")
    erg["nullmoden"] = null
    erg["sek_je_durchlauf_B"] = sek_pass
    zeilen.append(f"  ein Durchlauf (9 Werte) {sek_pass:.2f} s")

    gebunden, resonanzen, zaehlung = [], [], {}
    # ---- gebundene Zustaende 0 < rho < 1 - omega (reell, Vorzeichenwechsel von Re D)
    if bereich in ("alles", "gebunden") and budget.ok("gebundene Suche", 20 * sek_pass):
        nb = a.n_gebunden
        xs = [0.001 + (kante - 0.0005 - 0.001) * i / (nb - 1) for i in range(nb)]
        D = det_liste(linB, [complex(x, 0.0) for x in xs] * len(nus), [v for v in nus for _ in xs])
        klammern = []
        max_im = 0.0
        for i, v in enumerate(nus):
            re = [z.real for z in D[i * nb:(i + 1) * nb]]
            max_im = max(max_im, max(abs(z.imag) / max(abs(z), 1e-300) for z in D[i * nb:(i + 1) * nb]))
            for k in range(nb - 1):
                if re[k] * re[k + 1] < 0:
                    klammern.append((xs[k], xs[k + 1], re[k], re[k + 1], v))
        erg["gebunden_max_rel_imD"] = max_im
        if klammern:
            wurz = illinois(linB, [k[0] for k in klammern], [k[1] for k in klammern], [k[2] for k in klammern],
                            [k[3] for k in klammern], [k[4] for k in klammern], iters=a.iter_illinois)
            for w in wurz:
                gebunden.append({"l": int(round(w["nu"] - 1.0)), "rho": w["rho"], "klammer": w["klammer"]})
        zeilen.append(f"  gebunden: {len(gebunden)} Nullstellen in (0, 1 - omega), max |Im D|/|D| = {max_im:.1e}")

    # ---- Resonanzen 1 - omega < Re rho < 1 + omega
    if bereich in ("alles", "resonanz") and budget.ok("Resonanzsuche", 40 * sek_pass):
        x0, x1 = kante + 0.002, min(oben - 0.002, a.rho_max)
        nr = a.n_resonanz
        xs = [x0 + (x1 - x0) * i / (nr - 1) for i in range(nr)]
        keime = []
        D = det_liste(linB, [complex(x, 0.0) for x in xs] * len(nus), [v for v in nus for _ in xs])
        for i, v in enumerate(nus):
            ab = [abs(z) for z in D[i * nr:(i + 1) * nr]]
            for k in lokale_minima(ab):
                keime.append((complex(xs[k], -1e-4), v))
        n2 = a.n_flaeche
        xs2 = [x0 + (x1 - x0) * i / (n2 - 1) for i in range(n2)]
        ims = [-0.003, -0.01, -0.03, -0.07]
        pk = [complex(x, y) for y in ims for x in xs2]
        D = det_liste(linB, pk * len(nus), [v for v in nus for _ in pk])
        for i, v in enumerate(nus):
            for r_, y in enumerate(ims):
                ab = [abs(z) for z in D[i * len(pk) + r_ * n2:i * len(pk) + (r_ + 1) * n2]]
                for k in lokale_minima(ab):
                    keime.append((complex(xs2[k], y), v))
        zeilen.append(f"  Resonanzsuche: {len(keime)} Keime (reelle Achse {nr} Punkte, Flaeche {n2} x {len(ims)})")
        if budget.ok("Newton Stufe B", 3 * a.iter_newton * sek_pass):
            nw = newton(linB, [k[0] for k in keime], [k[1] for k in keime], iters=a.iter_newton)
            for w in nw:
                z = w["rho"]
                if not (w["konvergiert"] and w["absD"] < 1e-8):
                    continue
                if not (kante < z.real < oben):
                    continue
                l = int(round(w["nu"] - 1.0))
                if any(r["l"] == l and abs(r["rho"] - z) < 1e-7 for r in resonanzen):
                    continue
                resonanzen.append({"l": l, "rho": z, "absD": w["absD"], "iter": w["iter"]})
        resonanzen.sort(key=lambda r: (r["l"], r["rho"].real))
        if budget.ok("Konturzaehlung", 12 * sek_pass):
            zaehlung = kontur(linB, nus, x0, x1, a.kasten_im, 0.001, (a.n_kante, 20, 2 * a.n_kante, 20),
                              a.kontur_runden, a.kontur_max)
            for v in nus:
                l = int(round(v - 1.0))
                im_kasten = [r for r in resonanzen if r["l"] == l and x0 < r["rho"].real < x1 and
                             a.kasten_im < r["rho"].imag < 0.001]
                zaehlung[v]["gefunden_newton"] = len(im_kasten)
                zeilen.append(f"  Kontur l = {l}: Umlaufzahl {zaehlung[v]['umlauf_roh']:.3f} "
                              f"({zaehlung[v]['punkte']} Punkte, aufgeloest {zaehlung[v]['aufgeloest']}), "
                              f"Newton im Kasten {len(im_kasten)}")

    # ---- weitere Stufen (Nachpolieren) und Negativkontrolle
    stufen_erg = {str(h_liste[iB]): {"gebunden": gebunden, "resonanzen": resonanzen}}
    for i in range(len(h_liste)):
        if i == iB:
            continue
        if not budget.ok(f"Stufe h = {h_liste[i]}", (30 * sek_pass + 2 * infoB["sek_profil"]) * (h_liste[iB] / h_liste[i])):
            continue
        prof_i, lin_i, info_i = stufe(i)
        erg["stufen"][str(h_liste[i])] = info_i
        geb_i = []
        if gebunden:
            dl = 2e-4
            kl = [(g["rho"] - dl, g["rho"] + dl, g["l"] + 1.0) for g in gebunden]
            D = det_liste(lin_i, [complex(k[0], 0.0) for k in kl] + [complex(k[1], 0.0) for k in kl],
                          [k[2] for k in kl] * 2)
            n = len(kl)
            ok = [D[j].real * D[n + j].real < 0 for j in range(n)]
            wz = illinois(lin_i, [kl[j][0] for j in range(n) if ok[j]], [kl[j][1] for j in range(n) if ok[j]],
                          [D[j].real for j in range(n) if ok[j]], [D[n + j].real for j in range(n) if ok[j]],
                          [kl[j][2] for j in range(n) if ok[j]], iters=a.iter_illinois)
            wz_iter = iter(wz)
            for j in range(n):
                geb_i.append({"l": gebunden[j]["l"], "rho": next(wz_iter)["rho"] if ok[j] else None,
                              "klammer_ok": ok[j]})
        res_i = []
        if resonanzen:
            nw = newton(lin_i, [r["rho"] for r in resonanzen], [r["l"] + 1.0 for r in resonanzen], iters=12)
            for r, w in zip(resonanzen, nw):
                res_i.append({"l": r["l"], "rho": w["rho"], "absD": w["absD"], "konvergiert": w["konvergiert"]})
        stufen_erg[str(h_liste[i])] = {"gebunden": geb_i, "resonanzen": res_i}
    erg["ergebnisse"] = stufen_erg
    erg["kontur"] = {str(int(round(v - 1.0))): zaehlung[v] for v in zaehlung}

    # Negativkontrolle ohne Ball auf dem Gitter der Stufe B
    if budget.ok("Negativkontrolle", 8 * sek_pass):
        linF = lin_aufbau(profB, h_liste[iB], f_rand[iB], frei=True)
        linF["dev"] = dev
        neg = {}
        if resonanzen:
            D = det_liste(linF, [r["rho"] for r in resonanzen], [r["l"] + 1.0 for r in resonanzen])
            neg["absD_frei_an_polen"] = [abs(z) for z in D]
        if gebunden:
            D = det_liste(linF, [complex(g["rho"], 0.0) for g in gebunden], [g["l"] + 1.0 for g in gebunden])
            neg["absD_frei_an_gebundenen"] = [abs(z) for z in D]
        xs = [0.001 + (kante - 0.0015) * i / 199 for i in range(200)]
        D = det_liste(linF, [complex(x, 0.0) for x in xs] * len(nus), [v for v in nus for _ in xs])
        neg["vorzeichenwechsel_frei_gebunden"] = sum(1 for i in range(len(nus)) for k in range(199)
                                                     if D[i * 200 + k].real * D[i * 200 + k + 1].real < 0)
        if bereich in ("alles", "resonanz"):
            x0, x1 = kante + 0.002, min(oben - 0.002, a.rho_max)
            kf = kontur(linF, nus, x0, x1, a.kasten_im, 0.001, (60, 10, 60, 10), 3, 4000)
            neg["umlauf_frei"] = {str(int(round(v - 1.0))): kf[v]["umlauf_roh"] for v in kf}
        erg["negativkontrolle"] = neg
        zeilen.append(f"  Negativkontrolle ohne Ball: |D_frei| an den Polen "
                      f"{min(neg.get('absD_frei_an_polen', [float('nan')])):.3e} (Minimum), Vorzeichenwechsel unter der "
                      f"Kante {neg['vorzeichenwechsel_frei_gebunden']}, Umlauf {neg.get('umlauf_frei', '-')}")

    # ---- Tabelle
    hs = [str(h) for h in h_liste]
    zeilen.append("  gebundene Zustaende (reell), je Stufe h = " + ", ".join(hs))
    for j, g in enumerate(gebunden):
        werte = []
        for hk in hs:
            e = stufen_erg.get(hk, {}).get("gebunden", [])
            if hk == str(h_liste[iB]):
                werte.append(f"{g['rho']:.10f}")
            elif j < len(e) and e[j]["rho"] is not None:
                werte.append(f"{e[j]['rho']:.10f}")
            else:
                werte.append("-")
        zeilen.append(f"    l = {g['l']}: " + " | ".join(werte))
    zeilen.append("  Resonanzen (Im rho < 0 = abklingend), je Stufe h = " + ", ".join(hs))
    for j, r in enumerate(resonanzen):
        werte = []
        for hk in hs:
            e = stufen_erg.get(hk, {}).get("resonanzen", [])
            if hk == str(h_liste[iB]):
                werte.append(fz(r["rho"]))
            elif j < len(e):
                werte.append(fz(e[j]["rho"]) + ("" if e[j]["konvergiert"] else " (nicht konv.)"))
            else:
                werte.append("-")
        zeilen.append(f"    l = {r['l']}: " + " | ".join(werte))
    return erg


# ================================================================ Kommando bruecke (Dimensionsfortsetzung 1 -> 3)

def bruecke(w2, dims, start, l, h, beta, dev, budget, zeilen, f_rand=1e-8, iters=25, max_halb=6):
    """Verfolgt einen Pol von dim = 1 (gerader 1D-Sektor fuer l = 0) bis dim = 3: Profil und Stoerung in dim
    Dimensionen, nu = l + (dim-1)/2. Schrittweise Newton vom vorigen Pol (lineare Extrapolation aus zwei Vorgaengern);
    scheitert ein Schritt, wird er einmal halbiert."""
    spur = []
    rho_alt = [start]
    liste = list(dims)
    i = 0
    halbiert = 0
    while i < len(liste):
        dim = liste[i]
        if not budget.ok(f"Bruecke dim = {dim}", 30.0):
            break
        prof = profil(w2, dim, beta, 0.5 * h, dev)
        lin = lin_aufbau(prof, h, f_rand)
        lin["dev"] = dev
        nu = l + 0.5 * (dim - 1.0)
        if len(rho_alt) >= 2 and len(spur) >= 2:
            d_a, d_b = spur[-2]["dim"], spur[-1]["dim"]
            keim = rho_alt[-1] + (rho_alt[-1] - rho_alt[-2]) * (dim - d_b) / (d_b - d_a)
        else:
            keim = rho_alt[-1]
        w = newton(lin, [keim], [nu], iters=iters)[0]
        ok = w["konvergiert"] and w["absD"] < 1e-8 and w["rho"].imag < 1e-9
        if not ok and halbiert < max_halb and spur:
            liste.insert(i, 0.5 * (spur[-1]["dim"] + dim))
            halbiert += 1
            continue
        eintrag = {"dim": dim, "nu": nu, "rho": w["rho"], "absD": w["absD"], "konvergiert": w["konvergiert"],
                   "S0": prof["f0"] ** 2, "R_aus": lin["R_aus"], "r_m": lin["r_m"],
                   "kante_unten": 1.0 - math.sqrt(w2), "kante_oben": 1.0 + math.sqrt(w2)}
        if abs(dim - 1.0) < 1e-12:
            a0 = 1.0 - w2
            fx, _ = f_werte(prof, prof["j_cut"] + 1)
            abw = 0.0
            for j in range(prof["j_cut"] + 1):
                x = j * prof["h"]
                ex = math.sqrt(2.0 * a0 / (1.0 + math.sqrt(1.0 - 4.0 * beta * a0) * math.cosh(2.0 * math.sqrt(a0) * x)))
                abw = max(abw, abs(fx[j] - ex))
            eintrag["K0_max_abw_profil_exakt"] = abw
        spur.append(eintrag)
        zeilen.append(f"  dim = {dim:.4f}: S0 = {eintrag['S0']:.6f}, rho = {fz(w['rho'])}, |D| = {w['absD']:.1e}, "
                      f"konvergiert {w['konvergiert']}" + (f", K0 Profil {eintrag['K0_max_abw_profil_exakt']:.1e}"
                                                            if "K0_max_abw_profil_exakt" in eintrag else ""))
        if not ok:
            zeilen.append("  Spur abgebrochen (Newton ohne Konvergenz auch nach Halbierung)")
            break
        rho_alt.append(w["rho"])
        i += 1
    return spur


# ================================================================ Zeitentwicklung (radial, reduziert Psi = r phi)

def matrix_pencil(y, dt, K=12, max_n=2400):
    """Summe gedaempfter Exponentiale y_n = sum c_k z_k^n, z = exp(-i rho dt) -> rho = i ln z / dt
    (Re rho = Frequenz, Im rho < 0 = abklingend). Unterabtastung auf hoechstens max_n Punkte."""
    y = y.to(C128).cpu()
    schritt = max(1, int(math.ceil(y.numel() / max_n)))
    y = y[::schritt]
    dt = dt * schritt
    N = y.numel()
    L = N // 3
    if N < 12:
        return []
    idx = torch.arange(N - L).unsqueeze(1) + torch.arange(L + 1).unsqueeze(0)
    Y = y[idx]
    _, S, Vh = torch.linalg.svd(Y, full_matrices=False)
    K = max(1, min(K, int((S > S[0] * 1e-11).sum())))
    W = Vh[:K, :].transpose(0, 1)
    T = torch.linalg.pinv(W[:-1, :]) @ W[1:, :]
    z = torch.linalg.eigvals(T)
    n = torch.arange(N, dtype=F64).to(C128)
    V = z.unsqueeze(0) ** n.unsqueeze(1)
    c = torch.linalg.pinv(V) @ y
    rho = 1j * torch.log(z) / dt
    aus = [{"re": float(rho[k].real), "im": float(rho[k].imag), "amp": float(c[k].abs())} for k in range(z.numel())]
    aus.sort(key=lambda e: -e["amp"])
    rest = (y - V @ c).abs().max().item() / max(y.abs().max().item(), 1e-300)
    for e in aus:
        e["rel_rest"] = rest
    return aus


def nulldurchgaenge(t, x):
    """Frequenz aus den Vorzeichenwechseln des reellen Signals x - Mittelwert (lineare Interpolation)."""
    m = sum(x) / max(1, len(x))
    x = [v - m for v in x]
    tt = []
    for i in range(len(x) - 1):
        if x[i] == 0.0 or x[i] * x[i + 1] < 0.0:
            tt.append(t[i] + (t[i + 1] - t[i]) * x[i] / (x[i] - x[i + 1]) if x[i] != x[i + 1] else t[i])
    if len(tt) < 3:
        return float("nan"), len(tt)
    return PI * (len(tt) - 1) / (tt[-1] - tt[0]), len(tt)


def zeitlauf(w2, dr, T, r_max, r_sd, art, reihen, dev, budget, mess=0.2, dt_fak=0.4, r_zusatz=30.0):
    """art = 'nl0': nichtlinear, l = 0, reihen = Liste der Stoesse eta (psi, psi_t mal 1 + eta; eta = 0 ist die
    Ballreferenz fuer die Differenz). art = 'lin': linearisiert, reihen = Liste von l; Anfangsstoerung
    Phi = r f'(r) r^2/(r^2+1) (Wandverschiebung), Phi_t = -i omega Phi. Laborsystem:
        Phi_tt = Phi_rr - (l(l+1)/r^2 + dp) Phi - sp exp(-2 i omega t) conj(Phi).
    Leapfrog mit Daempfungsschicht r > r_sd; Dirichlet bei r = 0 und r_max."""
    prof = profil(w2, 3.0, BETA, dr, dev)
    om = math.sqrt(w2)
    N = int(round(r_max / dr))
    f_l, fp_l = f_werte(prof, N + 1)
    f = torch.tensor(f_l, dtype=F64, device=dev)
    fp = torch.tensor(fp_l, dtype=F64, device=dev)
    r = torch.arange(N + 1, dtype=F64, device=dev) * dr
    inv_r2 = torch.zeros_like(r)
    inv_r2[1:] = 1.0 / r[1:] ** 2
    dt = dt_fak * dr
    n_mess = max(1, int(round(mess / dt)))
    mess = n_mess * dt                      # tatsaechlicher Messabstand (ganzes Vielfaches von dt) fuer die Analyse
    n_schritte = int(round(T / dt))
    gam = torch.where(r > r_sd, SIGMA0 * ((r - r_sd) / (r_max - r_sd)) ** 2, torch.zeros_like(r))
    fak_p = 1.0 / (1.0 + 0.5 * dt * gam)
    fak_m = 1.0 - 0.5 * dt * gam
    rh = r_halb(prof)
    orte = [dr, 0.5 * rh, rh, 1.5 * rh, r_zusatz]
    j_orte = [min(N - 1, max(1, int(round(x / dr)))) for x in orte]
    nr = len(reihen)
    S_p = f * f
    dpot = 1.0 - 4.0 * S_p + 9.0 * BETA * S_p * S_p
    spot = -2.0 * S_p + 6.0 * BETA * S_p * S_p
    if art == "nl0":
        eta = torch.tensor(reihen, dtype=F64, device=dev).unsqueeze(1)
        phi = ((1.0 + eta) * (r * f).unsqueeze(0)).to(C128)
        vel = -1j * om * phi
        g = None
    else:
        cnu = torch.tensor([float(l * (l + 1)) for l in reihen], dtype=F64, device=dev).unsqueeze(1)
        V = cnu * inv_r2.unsqueeze(0) + dpot.unsqueeze(0)
        g = r * fp * r * r / (r * r + 1.0)
        g = g / g.abs().max()
        phi = g.unsqueeze(0).repeat(nr, 1).to(C128)
        vel = -1j * om * phi
    j_in = int(round(r_sd / dr))

    def beschl(p, t):
        a = torch.zeros_like(p)
        a[:, 1:-1] = (p[:, 2:] - 2.0 * p[:, 1:-1] + p[:, :-2]) / (dr * dr)
        if art == "nl0":
            S = (p.real ** 2 + p.imag ** 2) * inv_r2
            a = a - (1.0 - 2.0 * S + 3.0 * BETA * S * S) * p
        else:
            a = a - V * p - (spot * cmath.exp(-2j * om * t)) * p.conj()
        a[:, 0] = 0.0
        a[:, -1] = 0.0
        return a

    phi_alt = phi - dt * vel + 0.5 * dt * dt * beschl(phi, 0.0)
    ts, sig, proj, ladung = [], [], [], []
    t0 = uhr()
    for n in range(n_schritte + 1):
        t = n * dt
        a = beschl(phi, t)
        phi_neu = (2.0 * phi - fak_m * phi_alt + dt * dt * a) * fak_p
        if n % n_mess == 0:
            dreh = cmath.exp(1j * om * t)
            ts.append(t)
            werte = torch.stack([phi[:, j] / (j * dr) for j in j_orte], dim=1) * dreh     # (reihen, orte)
            sig.append(werte.cpu())
            if g is not None:
                proj.append(((phi[:, :j_in] * dreh) * g[:j_in]).sum(1).cpu() * dr / float((g[:j_in] ** 2).sum() * dr))
            v = (phi_neu - phi_alt) / (2.0 * dt)
            ladung.append((-2.0 * (phi[:, :j_in].conj() * v[:, :j_in]).imag.sum(1) * dr * 4.0 * PI).cpu())
            if n == 10 * n_mess and n_schritte > 0:
                schaetz = (uhr() - t0) / n * n_schritte
                print(f"  Zeitlauf dr = {dr}: geschaetzt {schaetz:.0f} s", flush=True)
                if not budget.ok(f"Zeitlauf dr = {dr} (Schaetzung {schaetz:.0f} s)", schaetz):
                    return None
        phi_alt, phi = phi, phi_neu
    sig = torch.stack(sig)                  # (zeiten, reihen, orte)
    ladung = torch.stack(ladung)
    tt = torch.tensor(ts, dtype=F64)
    out = {"dr": dr, "dt": dt, "mess": mess, "T": T, "r_max": r_max, "r_sd": r_sd, "orte": [j * dr for j in j_orte], "sek": uhr() - t0,
           "S0": prof["f0"] ** 2, "R_halb": rh, "profil_grund": prof["grund"], "reihen": reihen}
    q0 = ladung[0]
    out["ladung_rel_drift_bis_T4"] = [float((ladung[:len(ts) // 4, i] - q0[i]).abs().max() / q0[i].abs().clamp_min(1e-300))
                                      for i in range(nr)]
    ab = len(ts) // 2
    ana = []
    f_orte = torch.tensor([f_l[j] for j in j_orte], dtype=F64)
    for i in range(nr):
        e = {"reihe": reihen[i]}
        if art == "nl0":
            if 0.0 in reihen and reihen[i] != 0.0:
                ref = reihen.index(0.0)
                d = sig[:, i, :] - sig[:, ref, :]
                e["differenz_zentrum"] = matrix_pencil(d[ab:, 0], mess)[:8]
                e["differenz_wand"] = matrix_pencil(d[ab:, 2], mess)[:8]
                betr = sig[:, i, 0].abs() - sig[:, ref, 0].abs()
                e["betrag_zentrum"] = matrix_pencil(betr[ab:].to(C128), mess)[:8]
            e["roh_zentrum"] = matrix_pencil((sig[:, i, 0] - f_orte[0])[ab:], mess)[:8]
        else:
            e["wand"] = matrix_pencil(sig[ab:, i, 2], mess)[:8]
            e["halbe_wand"] = matrix_pencil(sig[ab:, i, 1], mess)[:8]
            p = torch.stack(proj)[:, i]
            e["projektion"] = matrix_pencil(p[ab:], mess)[:8]
            fq, nd = nulldurchgaenge(ts[ab:], p[ab:].real.tolist())
            e["nulldurchgang_frequenz"] = fq
            e["nulldurchgaenge"] = nd
        ana.append(e)
    out["analyse"] = ana
    return out


def zeit_bericht(res, art, zeilen, kante):
    zeilen.append(f"  dr = {res['dr']}, dt = {res['dt']}, T = {res['T']}, {res['sek']:.1f} s, S0 = {res['S0']:.6f}, "
                  f"Ladungsdrift bis T/4 {['%.1e' % x for x in res['ladung_rel_drift_bis_T4']]}")
    for e in res["analyse"]:
        for schl in ("differenz_zentrum", "differenz_wand", "betrag_zentrum", "roh_zentrum", "wand", "halbe_wand",
                     "projektion"):
            if schl in e and e[schl]:
                kurz = ", ".join(f"({k['re']:+.6f} {k['im']:+.2e}i |{k['amp']:.1e}|)" for k in e[schl][:5])
                zeilen.append(f"    {'eta' if art == 'nl0' else 'l'} = {e['reihe']} {schl}: {kurz}")
        if "nulldurchgang_frequenz" in e:
            zeilen.append(f"    l = {e['reihe']} Nulldurchgaenge der Projektion: Frequenz "
                          f"{e['nulldurchgang_frequenz']:.6f} ({e['nulldurchgaenge']} Durchgaenge); Kante {kante:.6f}")


# ================================================================ Hauptprogramm

def argumente():
    ap = argparse.ArgumentParser(description="Runde 6: Q-Ball-Resonanz in 3D (radial, l = 0, 1, 2)")
    ap.add_argument("kommando", choices=["rauch", "pole", "bruecke", "zeit0", "zeitlin"])
    ap.add_argument("--geraet", default="cpu", choices=["cpu", "cuda"])
    ap.add_argument("--out", default=None)
    ap.add_argument("--budget", type=float, default=540.0, help="Sekunden, danach entfallen weitere Stufen")
    ap.add_argument("--omega2", default="0.7", help="Liste, z. B. 0.7 oder 0.52,0.55")
    ap.add_argument("--l", default="0,1,2")
    ap.add_argument("--h", default="0.02,0.01,0.005", help="Stufen A,B,C (Schritt der linearen ODE)")
    ap.add_argument("--bereich", default="alles", choices=["alles", "gebunden", "resonanz"])
    ap.add_argument("--n-gebunden", dest="n_gebunden", type=int, default=300)
    ap.add_argument("--n-resonanz", dest="n_resonanz", type=int, default=700)
    ap.add_argument("--n-flaeche", dest="n_flaeche", type=int, default=160)
    ap.add_argument("--n-kante", dest="n_kante", type=int, default=240)
    ap.add_argument("--kasten-im", dest="kasten_im", type=float, default=-0.1)
    ap.add_argument("--kontur-runden", dest="kontur_runden", type=int, default=8)
    ap.add_argument("--kontur-max", dest="kontur_max", type=int, default=6000)
    ap.add_argument("--rho-max", dest="rho_max", type=float, default=9.0)
    ap.add_argument("--iter-newton", dest="iter_newton", type=int, default=25)
    ap.add_argument("--iter-illinois", dest="iter_illinois", type=int, default=30)
    ap.add_argument("--null-eps", dest="null_eps", type=float, default=1e-3)
    ap.add_argument("--dims", default="1,1.25,1.5,1.75,2,2.25,2.5,2.75,3")
    ap.add_argument("--start", default=None, help="Startpol der Bruecke, z. B. 1.4937769645-6.716e-5j")
    ap.add_argument("--ciurla", action="store_true", help="Bruecke: vorher Kalibrierung beta = 1/4, omega^2 = 3/4, dim = 1")
    ap.add_argument("--eta", default="0,0.001,0.01", help="zeit0: Stoesse (0 = Ballreferenz)")
    ap.add_argument("--dr", default="0.05,0.025,0.0125")
    ap.add_argument("--T", type=float, default=800.0)
    ap.add_argument("--rmax", type=float, default=200.0)
    ap.add_argument("--rsd", type=float, default=130.0, help="Beginn der Daempfungsschicht")
    ap.add_argument("--mess", type=float, default=0.2)
    return ap.parse_args()


def main():
    a = argumente()
    if a.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber kein CUDA-Geraet")
        dev = torch.device("cuda")
    else:
        torch.set_num_threads(1)
        dev = torch.device("cpu")
    budget = Budget(a.budget)
    out = a.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), f"ausgabe-{a.kommando}")
    os.makedirs(out, exist_ok=True)
    start = jetzt()
    zeilen = [f"Runde 6 resonanz3d {a.kommando} Start {start}, Geraet {a.geraet}, torch {torch.__version__}"]
    print(zeilen[0], flush=True)
    ergebnis = {"start": start, "kommando": a.kommando, "argumente": vars(a), "ergebnisse": {}}
    w2_liste = [float(x) for x in a.omega2.split(",")]
    l_liste = [int(x) for x in a.l.split(",")]
    h_liste = [float(x) for x in a.h.split(",")]

    def sichern():
        ergebnis["ende"] = jetzt()
        ergebnis["sek"] = uhr()
        ergebnis["entfallen"] = budget.abgebrochen
        with open(os.path.join(out, f"{a.kommando}.json"), "w") as fh:
            json.dump(jsonfest(ergebnis), fh, indent=1)
        with open(os.path.join(out, f"{a.kommando}_bericht.txt"), "w") as fh:
            fh.write("\n".join(zeilen) + "\n")

    if a.kommando == "rauch":
        # alles einmal mit winzigen Groessen: prueft nur, ob der Code durchlaeuft (keine Physik)
        a.n_gebunden, a.n_resonanz, a.n_flaeche, a.n_kante = 12, 16, 8, 16
        a.kontur_runden, a.iter_newton, a.iter_illinois = 1, 3, 4
        ergebnis["ergebnisse"]["pole"] = pole_omega(0.7, [0, 1, 2], [0.08, 0.04], "alles", a, dev, budget, zeilen)
        sichern()
        zeilen.append("Rauch Bruecke:")
        ergebnis["ergebnisse"]["bruecke"] = bruecke(0.7, [1.0, 1.25], CODEX_1D, 0, 0.04, BETA, dev, budget, zeilen, iters=8, max_halb=0)
        sichern()
        for art, reihen in (("nl0", [0.0, 1e-3]), ("lin", [2, 0])):
            res = zeitlauf(0.7, 0.1, 6.0, 40.0, 25.0, art, reihen, dev, budget, mess=0.2)
            ergebnis["ergebnisse"][f"zeit_{art}"] = res
            if res is not None:
                zeit_bericht(res, art, zeilen, 1.0 - math.sqrt(0.7))
        zeilen.append(f"Rauchtest durchgelaufen nach {uhr():.1f} s (Zahlen ohne Bedeutung).")
    elif a.kommando == "pole":
        for w2 in w2_liste:
            if not budget.ok(f"pole omega^2 = {w2}", 30.0):
                continue
            ergebnis["ergebnisse"][str(w2)] = pole_omega(w2, l_liste, h_liste, a.bereich, a, dev, budget, zeilen)
            sichern()
    elif a.kommando == "bruecke":
        dims = [float(x) for x in a.dims.split(",")]
        hB = h_liste[len(h_liste) // 2]
        if a.ciurla:
            zeilen.append("Kalibrierung Ciurla u. a. (beta = 1/4, omega^2 = 3/4, dim = 1, gerade):")
            sp = bruecke(0.75, [1.0], complex(1.538789, -1.18e-5), 0, hB, 0.25, dev, budget, zeilen)
            ergebnis["ergebnisse"]["ciurla"] = sp
            if sp:
                zeilen.append(f"  Soll (Codex-Nachrechnung) {fz(CIURLA_1D)}, Abweichung {abs(sp[0]['rho'] - CIURLA_1D):.2e}")
            sichern()
        for w2 in w2_liste:
            st = complex(a.start.replace(" ", "")) if a.start else CODEX_1D
            for l in l_liste:
                zeilen.append(f"Bruecke omega^2 = {w2}, l = {l}, Start {fz(st)}, h = {hB}:")
                sp = bruecke(w2, dims, st, l, hB, BETA, dev, budget, zeilen)
                ergebnis["ergebnisse"][f"{w2}_l{l}"] = sp
                if sp and abs(sp[0]["dim"] - 1.0) < 1e-12 and l == 0:
                    zeilen.append(f"  dim = 1 gegen Codex {fz(CODEX_1D)}: Abweichung {abs(sp[0]['rho'] - CODEX_1D):.2e}")
                sichern()
    else:
        drs = [float(x) for x in a.dr.split(",")]
        art = "nl0" if a.kommando == "zeit0" else "lin"
        reihen = [float(x) for x in a.eta.split(",")] if art == "nl0" else l_liste
        for w2 in w2_liste:
            kante = 1.0 - math.sqrt(w2)
            zeilen.append(f"=== {a.kommando} omega^2 = {w2}, Kante 1 - omega = {kante:.6f}, Reihen {reihen}")
            if art == "lin":
                p = profil(w2, 3.0, BETA, drs[0], dev)
                kz = kennzahlen_3d(p)
                ergebnis["ergebnisse"][f"{w2}_kennzahlen"] = kz
                zeilen.append(f"  R_Q = {kz['R_Q']:.4f}, sigma_grad = {kz['sigma_grad']:.5f}, w = {kz['w_in']:.5f}, "
                              f"Rayleigh omega_2 = {kz['omega_R_haupt']:.6f} (Band {kz['omega_R_min']:.6f} .. "
                              f"{kz['omega_R_max']:.6f})")
            for dr in drs:
                if not budget.ok(f"{a.kommando} omega^2 = {w2}, dr = {dr}", 20.0):
                    continue
                res = zeitlauf(w2, dr, a.T, a.rmax, a.rsd, art, reihen, dev, budget, mess=a.mess)
                ergebnis["ergebnisse"][f"{w2}_dr{dr}"] = res
                if res is not None:
                    zeit_bericht(res, art, zeilen, kante)
                sichern()
    zeilen.append(f"Ende {jetzt()}, {uhr():.1f} s; entfallen: {budget.abgebrochen or 'nichts'}")
    sichern()
    print("\n".join(zeilen), flush=True)


if __name__ == "__main__":
    main()
