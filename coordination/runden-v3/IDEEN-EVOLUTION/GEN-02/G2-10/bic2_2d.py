#!/usr/bin/env python3
"""G2-10 (Ideen-Evolution, Generation 2, Test-Agent T-2): Kopie von RUNDE-07/bic2/bic2_v2.py (sha256 1f8affbd68b2c312...).
Aenderungen (alle mit "G2-10" markiert):
  - --dim: Raumdimension fuer die Profile in profile_stapel und fuer nu = (dim - 1)/2 (l = 0) im Befehl kurve
    (Vorgabe 3 = bisheriges Verhalten; die uebrigen Befehle unveraendert mit dim = 3 bzw. eigener dims-Liste).
  - barriere: nur Profile, x_B = groesstes omega^2 der Liste mit dp(S0) > c(eps)^2, c = 0,826 + 0,24 eps; dazu Q und
    Virialrest in dim Dimensionen. Eigener Aufruf vor jeder Polsuche (kein Pol geht ein).
  - leiter: Auswertung nach KARTE.md aus kurve.json/barriere.json (V1 bis V4, Gegenproben dim 1 und 3, L3,
    Plausibilitaet). Rechnet nichts neu.

Urspruenglicher Kopf:
Runde 7 (runden-v3), Karte BIC-2: Exaktheit und Robustheit der Nullstelle der l = 0-Breite. Explorativ.

Erweiterte Kopie von RUNDE-06/resonanz3d/resonanz3d.py (dort unveraendert: rauch, pole, bruecke, zeit0, zeitlin).
Neu (Abschnitt "Runde 7 BIC-2" unten):
  exakt  (a) Pol-Amplitude A_out(omega^2) mit Phasenbezug, Fluss-Breite, Krein-Norm; Nullstellenabbildung
             W(rho, omega^2) = (L(y_a), L(y_b)) bei reellem rho und ihre Umlaufzahl in der Ebene (rho, omega^2)
  kurve  (b) Breite und Nullstellen fuer U = S - S^2 + beta S^3 (beliebiges beta) und U = ln(1 + S) (Log-Potential)
  nlfit  (c) Abklingraten aus zeit0-Ausgaben gegen eta (Potenzgesetz, Fenster)
  zeit0 speichert jetzt zusaetzlich das Differenzsignal im Zentrum (unterabgetastet) und Fensterraten.
Lokal nur Rauchtest (Freigabe laut Leitung 30.09. 02:42). Plan: PLAN.md im selben Ordner.

Version 2 (begonnen 2026-09-30 05:08:50 CEST, gemessen; Anlass: Absturz exakt beta 0,55 um 0,67343 auf der .69,
torch.linalg.solve "singular" in lin_fit_nullstelle). Aenderungen gegen Version 1 (SHA-256 ad47922c...):
  - lin_fit_nullstelle: skalierte Spalten, lstsq statt solve, Konditionsgrenze; bei zu wenigen verschiedenen Punkten,
    singulaerer oder schlecht konditionierter Matrix Rueckgabe None mit Grund ("Fit nicht moeglich") statt Abbruch.
  - Fit-Punkte: bis zu 5 Profile um die Mitte (mindestens 2 verschiedene omega^2), nicht mehr festes Fenster 1e-4.
  - ohne Fit: Umlaufzahl trotzdem, Rechtecke um x0 und Re rho des Pols dort (rho0 als Rueckfall), drho aus
    --u-drho-ohne-fit.
  - liegt der Fit-Mittelpunkt ausserhalb eines Rechtecks (oder im aeusseren Fuenftel): zusaetzlich ein Rechteck um den
    Fit-Mittelpunkt mit --neu-profile neuen Profilen, Vermerk "neu_gelegt" im Bericht (abschaltbar: --neu-legen nein).
  - Sicherheitsnetz in main: unerwarteter Fehler -> Traceback in Bericht und JSON, dann rc = 1.
  - Phasenspruenge ohne Division (kein ZeroDivisionError bei W = 0), phasentest gegen A' = 0 geschuetzt.

--- urspruenglicher Kopf (Runde 6) ---

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
            "f": f_liste, "fp": fp_liste, "kappa": math.sqrt(a0), "dm1": dm1, "pot": {"art": "poly", "beta": beta}}


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
    pot = prof.get("pot", {"art": "poly", "beta": beta})
    dv, sv, cf = [], [], [0.0]
    for j in range(2 * K + 1):
        s = 0.0 if frei else f[j] ** 2
        d_, s_, _, _ = pot_werte(pot, s)
        dv.append(d_)
        sv.append(s_)
        if j > 0:
            cf.append(1.0 / (j * 0.5 * h) ** 2)
    if frei:
        reihe = (1.0, 0.0, 0.0, 0.0)
    else:
        s0 = prof["f0"] ** 2
        s2 = 2.0 * prof["f0"] * prof["f2"]
        d0_, s0_, d1_, s1_ = pot_werte(pot, s0)
        reihe = (d0_, d1_ * s2, s0_, s1_ * s2)
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
           "S0": prof["f0"] ** 2, "R_halb": rh, "profil_grund": prof["grund"], "reihen": reihen, "w2": w2}
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
                # Runde 7 (c): Fensterraten (Drittel von [0, T], erstes Zehntel ausgelassen) und Rohsignal
                n_t = d.shape[0]
                i0 = n_t // 10
                gr = [i0 + (n_t - i0) * k // 3 for k in range(4)]
                e["fenster"] = [{"t0": ts[gr[k]], "t1": ts[gr[k + 1] - 1],
                                 "pencil": matrix_pencil(d[gr[k]:gr[k + 1], 0], mess)[:6]} for k in range(3)]
                sch = max(1, n_t // 4000)
                e["roh_zentrum_t"] = ts[::sch]
                e["roh_zentrum_re"] = d[::sch, 0].real.tolist()
                e["roh_zentrum_im"] = d[::sch, 0].imag.tolist()
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


# ================================================================ Runde 7 BIC-2: Potentiale

def pot_poly(beta):
    return {"art": "poly", "beta": float(beta)}


POT_LOG = {"art": "log"}


def pot_werte(pot, S):
    """dp = U' + S U'', sp = S U'' und dp'(S), sp'(S); S float oder Tensor.
    poly: U = S - S^2 + beta S^3.  log: U = ln(1 + S) (flache Richtung, Affleck-Dine-artig; Wahl in PLAN.md)."""
    if pot["art"] == "poly":
        b = pot["beta"]
        return (1.0 - 4.0 * S + 9.0 * b * S * S, -2.0 * S + 6.0 * b * S * S, -4.0 + 18.0 * b * S, -2.0 + 12.0 * b * S)
    if pot["art"] == "log":
        e = 1.0 / (1.0 + S)
        return (e * e, -S * e * e, -2.0 * e ** 3, (S - 1.0) * e ** 3)
    raise ValueError(f"unbekanntes Potential {pot}")


def pot_u(pot, S):
    if pot["art"] == "poly":
        return S - S * S + pot["beta"] * S ** 3
    return math.log1p(S) if isinstance(S, float) else torch.log1p(S)


def pot_u1(pot, S):
    """U'(S)"""
    if pot["art"] == "poly":
        return 1.0 - 2.0 * S + 3.0 * pot["beta"] * S * S
    return 1.0 / (1.0 + S)


def pot_text(pot):
    return f"U = S - S^2 + {pot['beta']} S^3" if pot["art"] == "poly" else "U = ln(1 + S)"


def omega2_min(pot):
    """untere Existenzgrenze omega^2 > min_S U(S)/S (Duennwand-Grenze); obere Grenze ist 1 (Masse 1)."""
    if pot["art"] == "poly":
        return 1.0 - 1.0 / (4.0 * pot["beta"])
    return 0.0


def profil_pot(w2, dim, pot, h, dev):
    if pot["art"] == "poly":
        return profil(w2, dim, pot["beta"], h, dev)
    return profil_allg(w2, dim, pot, h, dev)


def profil_allg(w2, dim, pot, h, dev, f_schwanz=1e-5, n_kand=1024, runden_fein=5, r_max=130.0):
    """Profil fuer Potentiale ohne Buckel (U = ln(1+S)): Klammer in f0 oberhalb von f_1 (Energie null:
    omega^2 S = U(S)). Ueberschuss (f < 0) = f0 zu gross, Unterschuss (f' > 0 bei f >= 0) = f0 zu klein.
    Tote Kandidaten werden auf f_top (F = 0) gesetzt. Rueckgabe mit denselben Schluesseln wie profil()."""
    dm1 = dim - 1.0
    d = float(dim)

    def e_null(S):
        return w2 * S - pot_u(pot, S)
    lo_s, hi_s = 1e-10, 1.0
    while e_null(hi_s) <= 0.0:
        hi_s *= 2.0
        if hi_s > 1e12:
            raise ValueError("kein f_1 (omega^2 zu gross?)")
    for _ in range(200):
        m = 0.5 * (lo_s + hi_s)
        if e_null(m) > 0.0:
            hi_s = m
        else:
            lo_s = m
    f_1 = math.sqrt(hi_s)
    lo_t, hi_t = 0.0, hi_s                         # f_top: U'(S) = omega^2
    for _ in range(200):
        m = 0.5 * (lo_t + hi_t)
        if pot_u1(pot, m) > w2:
            lo_t = m
        else:
            hi_t = m
    f_top = math.sqrt(0.5 * (lo_t + hi_t))

    def F(f):
        return (pot_u1(pot, f * f) - w2) * f

    def Fp(f):
        dp, sp, _, _ = pot_werte(pot, f * f)
        return dp + sp - w2

    def start(f0, hh):
        a_ = F(f0) / (2.0 * d)
        b_ = Fp(f0) * a_ / (4.0 * d + 8.0)
        return f0 + a_ * hh * hh + b_ * hh ** 4, 2.0 * a_ * hh + 4.0 * b_ * hh ** 3

    def rk4(r, f, p, hh):
        def ab(rr, ff, pp):
            return pp, F(ff) - (dm1 / rr) * pp
        k1f, k1p = ab(r, f, p)
        k2f, k2p = ab(r + 0.5 * hh, f + 0.5 * hh * k1f, p + 0.5 * hh * k1p)
        k3f, k3p = ab(r + 0.5 * hh, f + 0.5 * hh * k2f, p + 0.5 * hh * k2p)
        k4f, k4p = ab(r + hh, f + hh * k3f, p + hh * k3p)
        return f + (hh / 6.0) * (k1f + 2.0 * k2f + 2.0 * k3f + k4f), p + (hh / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p)

    def klassen(lo, hi, hh, runden):
        stufen = torch.linspace(0.0, 1.0, n_kand, dtype=F64, device=dev)
        gueltig = True
        n_max = int(round(r_max / hh))
        for rnd in range(runden):
            f0s = lo + (hi - lo) * stufen
            f, p = start(f0s, hh)
            z = torch.zeros_like(f0s)
            for k in range(1, n_max):
                f, p = rk4(k * hh, f, p, hh)
                ueber = (z == 0) & (f < 0)
                unter = (z == 0) & (f >= 0) & (p > 0)
                z = z + ueber.to(F64) - unter.to(F64)
                lebt = z == 0
                f = torch.where(lebt, f, torch.full_like(f, f_top))
                p = torch.where(lebt, p, torch.zeros_like(p))
                if k % 100 == 0 and not bool(lebt.any()):
                    break
            if rnd == 0:
                gueltig = bool(z[0] < 0) and bool(z[-1] > 0)
            u_ = f0s[z < 0]
            o_ = f0s[z > 0]
            if u_.numel() > 0:
                lo = max(lo, float(u_.max()))
            if o_.numel() > 0:
                hi = min(hi, float(o_.min()))
        return lo, hi, gueltig

    lo0, hi0 = f_1 * (1.0 + 1e-12), 3.0 * f_1 + 1.0
    for _ in range(8):                              # obere Grenze muss ueberschiessen
        _, _, g = klassen(lo0, hi0, 0.05, 1)
        if g:
            break
        hi0 = 2.0 * hi0
    lo, hi, _ = klassen(lo0, hi0, 0.05, 2)
    breite = max(1e-6 * f_1, 10.0 * (hi - lo))
    lo_f, hi_f = max(lo0, lo - breite), min(hi0, hi + breite)
    lo2, hi2, gueltig = klassen(lo_f, hi_f, h, runden_fein)
    rueckfall = not gueltig
    if rueckfall:
        lo2, hi2, gueltig = klassen(lo0, hi0, h, runden_fein + 2)
    f_mid = 0.5 * (lo2 + hi2)
    f3 = torch.tensor([lo2, f_mid, hi2], dtype=F64, device=dev)
    f, p = start(f3, h)
    bu, bp = [f3.cpu(), f.cpu()], [torch.zeros(3, dtype=F64), p.cpu()]
    n_max = int(round(r_max / h))
    grund, j_cut = 0, None
    k = 1
    while k < n_max and j_cut is None:
        sf_l, sp_l = [], []
        for _ in range(50):
            if k >= n_max:
                break
            f, p = rk4(k * h, f, p, h)
            sf_l.append(f)
            sp_l.append(p)
            k += 1
        if not sf_l:
            break
        sf = torch.stack(sf_l).cpu()
        sp = torch.stack(sp_l).cpu()
        fm = sf[:, 1]
        streu = (sf[:, 2] - sf[:, 0]).abs()
        bed = [(fm < f_schwanz * f_mid, 1), (sp[:, 1] > 0, 2), (fm < 0, 3), (streu > 1e-2 * fm.abs(), 4)]
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
    return {"w2": w2, "dim": dim, "beta": None, "h": h, "t": f_top, "f0": f_mid, "f2": float(F(f_mid)) / (2.0 * d),
            "s": None, "f_1": f_1, "klammer": hi2 - lo2, "rueckfall": rueckfall, "j_cut": j_cut, "r_cut": j_cut * h,
            "grund": grund, "streuung_cut": float((bu[j_cut][2] - bu[j_cut][0]).abs()), "f": f_liste, "fp": fp_liste,
            "kappa": math.sqrt(1.0 - w2), "dm1": dm1, "pot": pot}


def ladung_3d(prof):
    """Q = 8 pi omega int f^2 r^2 dr (Trapez, dim = 3), fuer jedes Potential."""
    h = prof["h"]
    n = int(radius_wo(prof, 1e-12 * prof["f0"]) / h) + 2
    f, _ = f_werte(prof, n)
    iq = sum((0.5 if j in (0, n - 1) else 1.0) * h * f[j] ** 2 * (j * h) ** 2 for j in range(n))
    return 8.0 * PI * math.sqrt(prof["w2"]) * iq


# ================================================================ Runde 7 BIC-2: mehrere Profile in einem Stapel

def lin_multi(profs, h, f_rand, dev, r_min=20.0):
    """Gemeinsames Gitter fuer mehrere Profile (verschiedene omega^2 oder Potentiale): Aussenrand R = groesster
    Einzelrand, Anschluss r_m = Median der R_halb; K und Km gerade (Simpson). Koeffizienten als Tensoren je Zeile."""
    for p in profs:
        if abs(p["h"] - 0.5 * h) > 1e-12:
            raise ValueError("Profil braucht Schritt h/2")
    R = max([r_min] + [radius_wo(p, f_rand * p["f0"]) for p in profs])
    K = int(math.ceil(R / h))
    K += K % 2
    rh = sorted(r_halb(p) for p in profs)[len(profs) // 2]
    Km = max(2, min(K - 2, int(round(rh / h))))
    Km -= Km % 2
    dv, sv, reihe, om = [], [], [], []
    for p in profs:
        f, _ = f_werte(p, 2 * K + 1)
        S = torch.tensor(f, dtype=F64) ** 2
        d_, s_, _, _ = pot_werte(p["pot"], S)
        dv.append(d_)
        sv.append(s_)
        s0 = p["f0"] ** 2
        S2 = 2.0 * p["f0"] * p["f2"]
        a0, b0, a1, b1 = pot_werte(p["pot"], s0)
        reihe.append([a0, a1 * S2, b0, b1 * S2])
        om.append(math.sqrt(p["w2"]))
    cf = [0.0] + [1.0 / (j * 0.5 * h) ** 2 for j in range(1, 2 * K + 1)]
    return {"h": h, "K": K, "Km": Km, "R_aus": K * h, "r_m": Km * h, "dvX": torch.stack(dv).to(dev),
            "svX": torch.stack(sv).to(dev), "reiheX": torch.tensor(reihe, dtype=F64, device=dev),
            "omX": torch.tensor(om, dtype=F64, device=dev), "cf": cf, "dev": dev, "n": len(profs)}


def lin_fuer(L, ix):
    """lin-Struktur fuer einen Stapel mit Profilzeilen ix (kompatibel mit det(), rk4_schritt(), reg_start())."""
    ix = torch.as_tensor(ix, dtype=torch.long, device=L["dev"])
    return {"h": L["h"], "K": L["K"], "Km": L["Km"], "R_aus": L["R_aus"], "r_m": L["r_m"], "omega": L["omX"][ix],
            "dv": L["dvX"][ix].T.contiguous(), "sv": L["svX"][ix].T.contiguous(), "cf": L["cf"],
            "reihe": tuple(L["reiheX"][ix, k] for k in range(4)), "dev": L["dev"]}


def det_liste_m(L, rhos, ixs, nus):
    lin = lin_fuer(L, ixs)
    rho = torch.tensor([complex(z) for z in rhos], dtype=C128)
    nu = torch.tensor([float(v) for v in nus], dtype=F64)
    return [complex(z) for z in det(lin, rho, nu).cpu().tolist()]


def newton_m(L, rhos, ixs, nus, iters=30, tol=1e-13, schritt_max=0.02, delta=1e-7):
    """wie newton(), aber jeder Pol mit eigener Profilzeile ix (alle omega^2 in einem Stapel)."""
    rho = [complex(z) for z in rhos]
    n = len(rho)
    aktiv = list(range(n))
    konv = [False] * n
    it_n = [0] * n
    for it in range(iters):
        if not aktiv:
            break
        batch = [rho[i] for i in aktiv] + [rho[i] + delta for i in aktiv] + [rho[i] + 1j * delta for i in aktiv]
        D = det_liste_m(L, batch, [ixs[i] for i in aktiv] * 3, [nus[i] for i in aktiv] * 3)
        m = len(aktiv)
        neu = []
        for a_, i in enumerate(aktiv):
            d0, dx, dy = D[a_], D[m + a_], D[2 * m + a_]
            j11, j21 = (dx - d0).real / delta, (dx - d0).imag / delta
            j12, j22 = (dy - d0).real / delta, (dy - d0).imag / delta
            dd = j11 * j22 - j12 * j21
            if dd == 0.0 or not math.isfinite(dd):
                continue
            st = complex(-(j22 * d0.real - j12 * d0.imag) / dd, -(-j21 * d0.real + j11 * d0.imag) / dd)
            if abs(st) > schritt_max:
                st = st * (schritt_max / abs(st))
            rho[i] = rho[i] + st
            it_n[i] = it + 1
            if abs(st) < tol * max(1.0, abs(rho[i])):
                konv[i] = True
            else:
                neu.append(i)
        aktiv = neu
    Dend = det_liste_m(L, rho, ixs, nus) if n else []
    return [{"rho": rho[i], "absD": abs(Dend[i]), "konvergiert": konv[i], "iter": it_n[i]} for i in range(n)]


def direkt_m(L, rhos, ixs, nus, gram=True):
    """Loesungsvektoren direkt (nicht Pluecker): y_a, y_b regulaer (Ursprung: U ~ r^nu bzw. V ~ r^nu, Faktor 1) von
    r = h bis r_m; z1 = (w+, 0, w+', 0), z2 = (0, w-, 0, w-') von R bis r_m (Normierung wie jost_start, Faktor
    exp(i q R) bzw. exp(-kappa R) weggelassen). Simpson-Gram-Matrizen mit Krein-Gewichten (omega + Re rho) fuer |U|^2
    und -(omega - Re rho) fuer |V|^2. Nur fuer Baelle ohne grosses Kernwachstum (Wachstum wird gemeldet)."""
    B = len(rhos)
    dev = L["dev"]
    ix = torch.as_tensor(list(ixs) + list(ixs), dtype=torch.long, device=dev)
    lin = lin_fuer(L, ix)
    rho1 = torch.tensor([complex(z) for z in rhos], dtype=C128, device=dev)
    nu1 = torch.tensor([float(v) for v in nus], dtype=F64, device=dev)
    rho = torch.cat([rho1, rho1])
    nu = torch.cat([nu1, nu1])
    om, h, K, Km = lin["omega"], lin["h"], lin["K"], lin["Km"]
    dv, sv, cf = lin["dv"], lin["sv"], lin["cf"]
    cnu = nu * (nu - 1.0)
    wp2, wm2 = (om + rho) ** 2, (om - rho) ** 2
    wU = (om + rho.real).to(C128)
    wV = (-(om - rho.real)).to(C128)

    def abl4(y, j):
        U, V, Up, Vp = y
        b = cnu * cf[j] + dv[j]
        return [Up, Vp, (b - wp2) * U + sv[j] * V, sv[j] * U + (b - wm2) * V]

    def schritt(y, j0, sg, hs):
        j1, j2 = j0 + sg, j0 + 2 * sg
        k1 = abl4(y, j0)
        k2 = abl4([u + (0.5 * hs) * v for u, v in zip(y, k1)], j1)
        k3 = abl4([u + (0.5 * hs) * v for u, v in zip(y, k2)], j1)
        k4 = abl4([u + hs * v for u, v in zip(y, k3)], j2)
        return [u + (hs / 6.0) * (a1 + 2.0 * a2 + 2.0 * a3 + a4) for u, a1, a2, a3, a4 in zip(y, k1, k2, k3, k4)]

    def dichte(y):
        return (wU * y[0].conj() * y[0] + wV * y[1].conj() * y[1])

    def kreuz(y):
        """Gram-Nebeneintrag zwischen Haelfte 1 und 2 des Doppelstapels"""
        return (wU[:B] * y[0][:B].conj() * y[0][B:] + wV[:B] * y[1][:B].conj() * y[1][B:])

    # regulaere Startwerte bei r = h (Reihe wie reg_start, mit Faktor h^nu); Haelfte 1 = a (U), Haelfte 2 = b (V)
    r = h
    d0, d2, s0, s2 = lin["reihe"]
    A = d0 - wp2
    Bq = d0 - wm2
    n2 = 2.0 * (2.0 * nu + 1.0)
    n4 = 4.0 * (2.0 * nu + 3.0)
    a2, b2 = A / n2, s0 / n2
    a4, b4 = (A * a2 + s0 * b2 + d2) / n4, (s0 * a2 + Bq * b2 + s2) / n4
    c2, e2 = s0 / n2, Bq / n2
    c4, e4 = (A * c2 + s0 * e2 + s2) / n4, (s0 * c2 + Bq * e2 + d2) / n4
    fak = (r ** nu).to(C128)
    ist_a = torch.cat([torch.ones(B, dtype=torch.bool, device=dev), torch.zeros(B, dtype=torch.bool, device=dev)])
    pU = torch.where(ist_a, 1.0 + a2 * r * r + a4 * r ** 4, c2 * r * r + c4 * r ** 4)
    pV = torch.where(ist_a, b2 * r * r + b4 * r ** 4, 1.0 + e2 * r * r + e4 * r ** 4)
    dU = torch.where(ist_a, 2.0 * a2 * r + 4.0 * a4 * r ** 3, 2.0 * c2 * r + 4.0 * c4 * r ** 3)
    dV = torch.where(ist_a, 2.0 * b2 * r + 4.0 * b4 * r ** 3, 2.0 * e2 * r + 4.0 * e4 * r ** 3)
    y = [fak * pU, fak * pV, fak * (nu * pU / r + dU), fak * (nu * pV / r + dV)]
    betrag_start = torch.stack([v.abs() for v in y]).amax(0)
    g_in = torch.zeros(2 * B, dtype=C128, device=dev)
    g_in_x = torch.zeros(B, dtype=C128, device=dev)
    for k in range(1, Km):
        if gram:
            wk = (4.0 if k % 2 else 2.0) * h / 3.0
            g_in = g_in + wk * dichte(y)
            g_in_x = g_in_x + wk * kreuz(y)
        y = schritt(y, 2 * k, 1, h)
    if gram:
        g_in = g_in + (h / 3.0) * dichte(y)
        g_in_x = g_in_x + (h / 3.0) * kreuz(y)
    wachstum = torch.stack([v.abs() for v in y]).amax(0) / betrag_start
    # Jost-Startwerte bei R; Haelfte 1 = z1 (auslaufend, Kanal omega + rho), Haelfte 2 = z2 (abklingend)
    R = lin["R_aus"]
    qp = torch.sqrt(wp2 - 1.0)
    unter = (wp2.real < 1.0) & (rho.imag == 0)
    qp = torch.where(unter, 1j * torch.sqrt(1.0 - wp2), qp)
    qm = 1j * torch.sqrt(1.0 - wm2)
    Pp, Qp = hankel(qp, R, nu)
    Pm, Qm = hankel(qm, R, nu)
    null = torch.zeros_like(Pp)
    z = [torch.where(ist_a, Pp, null), torch.where(ist_a, null, Pm), torch.where(ist_a, Qp, null),
         torch.where(ist_a, null, Qm)]
    g_out = torch.zeros(2 * B, dtype=C128, device=dev)
    g_out_x = torch.zeros(B, dtype=C128, device=dev)
    for i, k in enumerate(range(K, Km, -1)):
        if gram:
            wk = (h / 3.0) * (1.0 if i == 0 else (4.0 if i % 2 else 2.0))
            g_out = g_out + wk * dichte(z)
            g_out_x = g_out_x + wk * kreuz(z)
        z = schritt(z, 2 * k, -1, -h)
    if gram:
        g_out = g_out + (h / 3.0) * dichte(z)
        g_out_x = g_out_x + (h / 3.0) * kreuz(z)

    def teil(v, s):
        return v[:B] if s == 0 else v[B:]
    ya = [teil(v, 0) for v in y]
    yb = [teil(v, 1) for v in y]
    z1 = [teil(v, 0) for v in z]
    z2 = [teil(v, 1) for v in z]

    def omega_bil(p, q):
        return p[0] * q[2] - p[2] * q[0] + p[1] * q[3] - p[3] * q[1]
    M = torch.stack([torch.stack(ya, 1), torch.stack(yb, 1), torch.stack(z1, 1), torch.stack(z2, 1)], 2)   # (B, 4, 4)
    # L(y) = Omega(y, z2) mit z2 auf exp(-kappa r) normiert (Faktor exp(i q- R) > 0 bei reellem rho): unabhaengig von R
    nz = torch.exp(1j * qm[:B] * R)
    return {"M": M, "la": omega_bil(ya, z2) * nz, "lb": omega_bil(yb, z2) * nz, "G_in": (g_in[:B], g_in_x, g_in[B:]),
            "G_out": (g_out[:B], g_out_x, g_out[B:]), "J1": (Pp[:B].conj() * Qp[:B]).imag,
            "J2": (Pm[B:].conj() * Qm[B:]).imag, "qp": qp[:B], "R": R, "omega": om[:B], "rho": rho1,
            "wachstum": torch.maximum(wachstum[:B], wachstum[B:])}


def det_direkt(L, rhos, ixs, nus):
    """det der spaltennormierten 4x4-Matrix [y_a, y_b, z1, z2] bei r_m (direkte Vektoren, gleiche Diskretisierung wie
    Eigenvektor und W). Nullstellen = Pole des direkten Problems."""
    M = direkt_m(L, rhos, ixs, nus, gram=False)["M"]
    cn = M.abs().pow(2).sum(1).sqrt()
    return [complex(v) for v in torch.linalg.det(M / cn.unsqueeze(1)).tolist()]


def newton_direkt(L, rhos, ixs, nus, iters=10, tol=1e-14, delta=1e-8):
    """Nachpolieren der Pole auf det_direkt (die Pluecker-Pole weichen um O(h^4) ab; Rauchtest h = 0,08:
    sig_min/sig_2 = 3e-4 am Pluecker-Pol)."""
    rho = [complex(z) for z in rhos]
    n = len(rho)
    konv = [False] * n
    aktiv = list(range(n))
    for it in range(iters):
        if not aktiv:
            break
        batch = [rho[i] for i in aktiv] + [rho[i] + delta for i in aktiv] + [rho[i] + 1j * delta for i in aktiv]
        D = det_direkt(L, batch, [ixs[i] for i in aktiv] * 3, [nus[i] for i in aktiv] * 3)
        m = len(aktiv)
        neu = []
        for a_, i in enumerate(aktiv):
            d0, dx, dy = D[a_], D[m + a_], D[2 * m + a_]
            j11, j21 = (dx - d0).real / delta, (dx - d0).imag / delta
            j12, j22 = (dy - d0).real / delta, (dy - d0).imag / delta
            dd = j11 * j22 - j12 * j21
            if dd == 0.0 or not math.isfinite(dd):
                continue
            st = complex(-(j22 * d0.real - j12 * d0.imag) / dd, -(-j21 * d0.real + j11 * d0.imag) / dd)
            if abs(st) > 1e-3:
                st = st * (1e-3 / abs(st))
            rho[i] = rho[i] + st
            if abs(st) < tol * max(1.0, abs(rho[i])):
                konv[i] = True
            else:
                neu.append(i)
        aktiv = neu
    Dend = det_direkt(L, rho, ixs, nus) if n else []
    return [{"rho": rho[i], "absD": abs(Dend[i]), "konvergiert": konv[i]} for i in range(n)]


def eigen(Dd, i):
    """Eigenvektor am Pol (Element i von direkt_m): Nullvektor n von [y_a, y_b, z1, z2] (Spalten normiert, SVD),
    Phasenbezug n_b = 1 (Ursprungskoeffizient des geschlossenen Kanals V ~ r^nu reell positiv, Betrag 1).
    A_out = Koeffizient von w+ = exp(i q r) P(q r) im Kanal omega + rho; N_K = Krein-Norm ueber [0, R];
    Gamma_fluss = J(R) / (2 N_K) (Flussbilanz, Herleitung in PLAN.md)."""
    M = Dd["M"][i]
    cn = M.abs().pow(2).sum(0).sqrt()
    _, S_, Vh = torch.linalg.svd(M / cn)
    n = Vh[-1].conj() / cn
    n = n / n[1]
    na, nb, n1, n2 = [complex(v) for v in n.tolist()]
    Gaa, Gab, Gbb = [complex(g[i]) for g in Dd["G_in"]]
    G11, G12, G22 = [complex(g[i]) for g in Dd["G_out"]]
    N_in = (abs(na) ** 2 * Gaa + 2.0 * (na.conjugate() * nb * Gab).real + abs(nb) ** 2 * Gbb)
    N_out = (abs(n1) ** 2 * G11 + 2.0 * (n1.conjugate() * n2 * G12).real + abs(n2) ** 2 * G22)
    NK = N_in + N_out
    J = abs(n1) ** 2 * float(Dd["J1"][i]) + abs(n2) ** 2 * float(Dd["J2"][i])
    qp = complex(Dd["qp"][i])
    A_out = -n1 * cmath.exp(-1j * qp * Dd["R"])
    A_norm = A_out / math.sqrt(abs(NK.real)) if NK.real != 0 else complex("nan")
    sv = S_.tolist()
    rest = float((M @ n).abs().max() / max(float((M.abs() * n.abs()).max()), 1e-300))
    return {"n_a": na, "n_b": nb, "n_1": n1, "n_2": n2, "A_out": A_out, "A_norm": A_norm, "N_K": NK.real,
            "N_K_imag": NK.imag, "N_in": N_in.real, "Gamma_fluss": J / (2.0 * NK.real) if NK.real != 0 else float("nan"),
            "J_R": J, "sig_min_durch_sig2": sv[-1] / sv[-2], "rest_anschluss": rest, "q": qp,
            "wachstum_kern": float(Dd["wachstum"][i])}


def umlauf(werte):
    """Umlaufzahl einer geschlossenen Folge komplexer Werte und groesster Phasensprung (ohne Division)."""
    sp = [cmath.phase(werte[(i + 1) % len(werte)] * werte[i].conjugate()) for i in range(len(werte))]
    return sum(sp) / (2.0 * PI), max(abs(s) for s in sp)


def lin_fit_nullstelle(pkt, cond_max=1e10):
    """W ~ W0 + J (drho, dx), J reell 2x2, aus Punkten (drho, dx, W) (kleinste Quadrate, je Komponente; Spalten
    skaliert). Rueckgabe ((drho*, dx*, J, Rest, cond J), None) oder (None, Grund), nie ein Abbruch."""
    try:
        n_x = len({round(p[1], 14) for p in pkt})
        n_r = len({round(p[0], 14) for p in pkt})
        if len(pkt) < 4 or n_x < 2 or n_r < 2:
            return None, f"zu wenige verschiedene Punkte ({len(pkt)} Punkte, {n_x} omega^2-Werte, {n_r} rho-Werte)"
        sr = max(abs(p[0]) for p in pkt) or 1.0
        sx = max(abs(p[1]) for p in pkt) or 1.0
        X = torch.tensor([[1.0, p[0] / sr, p[1] / sx] for p in pkt], dtype=F64)
        Y = torch.tensor([[p[2].real, p[2].imag] for p in pkt], dtype=F64)
        c = torch.linalg.lstsq(X, Y).solution                  # (3, 2)
        res = float((X @ c - Y).abs().max())
        W0 = c[0]
        J = (c[1:] / torch.tensor([[sr], [sx]], dtype=F64)).T  # J[komp, variable], Variablen (drho, dx)
        sv = torch.linalg.svdvals(J)
        cond = float(sv[0] / sv[1]) if float(sv[1]) > 0.0 else float("inf")
        if not all(math.isfinite(float(v)) for v in J.flatten().tolist()):
            return None, "J nicht endlich"
        if not math.isfinite(cond) or cond > cond_max:
            return None, f"J singulaer oder schlecht konditioniert (cond {cond:.1e})"
        z = -torch.linalg.lstsq(J, W0.unsqueeze(1)).solution.squeeze(1)
        if not all(math.isfinite(float(v)) for v in z.tolist()):
            return None, "Loesung nicht endlich"
        return (float(z[0]), float(z[1]), J.tolist(), res, cond), None
    except (RuntimeError, ValueError, ZeroDivisionError) as err:
        return None, f"{type(err).__name__}: {err}"


FRAND = {0.02: 1e-6, 0.01: 1e-8, 0.005: 1e-10}


def profile_stapel(xs, pot, h, dev, budget, zeilen, reserve=30.0):
    """Profile fuer eine Liste omega^2 (Reihenfolge = Vorrang); bricht ab, wenn die Zeit knapp wird."""
    profs, xs_ok, t_prof = [], [], None
    for x in xs:
        if t_prof is not None and not budget.ok(f"Profil omega^2 = {x}", t_prof + reserve):
            break
        t0 = uhr()
        try:
            p = profil_pot(x, G210_DIM["d"], pot, 0.5 * h, dev)   # G2-10: dim als Parameter (Vorgabe 3)
        except (ValueError, RuntimeError) as err:
            zeilen.append(f"  Profil omega^2 = {x}: Fehler {err}")
            continue
        t_prof = uhr() - t0 if t_prof is None else max(t_prof, uhr() - t0)
        profs.append(p)
        xs_ok.append(x)
    return profs, xs_ok, t_prof


# ================================================================ Kommando exakt (Teil a)

def exakt(a, dev, budget, zeilen, erg, sichern):
    pot = pot_poly(a.beta)
    x0, rho0 = a.x0, a.rho0
    offs = sorted([float(v) for v in a.offsets.split(",")], key=abs)
    for h in [float(v) for v in a.h.split(",")]:
        if not budget.ok(f"exakt h = {h}", 60.0):
            continue
        f_rand = FRAND.get(h, 1e-8)
        st = {"h": h, "f_rand": f_rand, "potential": pot_text(pot)}
        erg[f"h{h}"] = st
        zeilen.append(f"=== exakt {pot_text(pot)}, h = {h}, f_rand = {f_rand}, x0 = {x0}, rho0 = {rho0}")
        profs, xs, t_prof = profile_stapel([x0 + o for o in offs], pot, h, dev, budget, zeilen,
                                           reserve=a.reserve)
        if len(profs) < 3:
            zeilen.append("  zu wenige Profile")
            continue
        ordn = sorted(range(len(xs)), key=lambda i: xs[i])
        profs = [profs[i] for i in ordn]
        xs = [xs[i] for i in ordn]
        L = lin_multi(profs, h, f_rand, dev)
        st.update({"x": xs, "S0": [p["f0"] ** 2 for p in profs], "Q": [ladung_3d(p) for p in profs],
                   "R_aus": L["R_aus"], "r_m": L["r_m"], "K": L["K"], "sek_profil_max": t_prof})
        zeilen.append(f"  {len(xs)} Profile (je bis {t_prof:.1f} s), R = {L['R_aus']:.2f}, r_m = {L['r_m']:.3f}")
        sichern()
        # 1. Pole (alle omega^2 in einem Stapel)
        keime = [complex(rho0 + a.drho * (x - x0), -max(1e-10, a.cgam * (x - x0) ** 2)) for x in xs]
        t0 = uhr()
        pol = newton_m(L, keime, list(range(len(xs))), [1.0] * len(xs), iters=a.iter_newton)
        st["pole_pluecker"] = pol
        st["sek_newton"] = uhr() - t0
        zeilen.append(f"  Newton (Pluecker) {uhr() - t0:.1f} s, konvergiert {sum(p['konvergiert'] for p in pol)}/{len(pol)}")
        sichern()
        if not budget.ok("Newton direkt", 20.0):
            continue
        t0 = uhr()
        pold = newton_direkt(L, [p["rho"] for p in pol], list(range(len(xs))), [1.0] * len(xs))
        for p_, q_ in zip(pold, pol):
            p_["rho_pluecker"] = q_["rho"]
        pol = pold
        st["pole"] = pol
        zeilen.append(f"  Newton (direkt) {uhr() - t0:.1f} s, konvergiert {sum(p['konvergiert'] for p in pol)}/{len(pol)}, "
                      f"max |rho_direkt - rho_pluecker| = {max(abs(p['rho'] - p['rho_pluecker']) for p in pol):.2e}")
        sichern()
        # 2. Eigenvektoren, A_out, Flussbreite
        if not budget.ok("Eigenvektoren", 20.0):
            continue
        Dd = direkt_m(L, [p["rho"] for p in pol], list(range(len(xs))), [1.0] * len(xs), gram=True)
        tab = []
        zeilen.append("  omega^2 | Re rho | Gamma Newton | Gamma Fluss | N_K | A_norm | arg A | sig_min/sig_2 | Wachstum")
        for i, x in enumerate(xs):
            e = eigen(Dd, i)
            e.update({"x": x, "rho": pol[i]["rho"], "Gamma_newton": -pol[i]["rho"].imag,
                      "Gamma_pluecker": -pol[i]["rho_pluecker"].imag,
                      "konvergiert": pol[i]["konvergiert"]})
            tab.append(e)
            zeilen.append(f"    {x:.7f} | {pol[i]['rho'].real:.10f} | {-pol[i]['rho'].imag:.4e} | {e['Gamma_fluss']:.4e} | "
                          f"{e['N_K']:.5e} | {e['A_norm'].real:+.6e} {e['A_norm'].imag:+.6e}i | "
                          f"{cmath.phase(e['A_norm']):+.6f} | {e['sig_min_durch_sig2']:.1e} | {e['wachstum_kern']:.1e}")
        st["tabelle"] = tab
        sichern()
        # Phasentest und naechster Abstand zum Ursprung (lokales komplexes Polynom in x)
        st["phasentest"] = phasentest(xs, [t["A_norm"] for t in tab], zeilen)
        sichern()
        # 3. Nullstellenabbildung W = L(y_a) + i L(y_b) bei reellem rho
        if not budget.ok("W-Gitter", 30.0):
            continue
        ic = min(range(len(xs)), key=lambda i: abs(tab[i]["A_norm"]))
        rc = pol[ic]["rho"].real
        if a.rc is not None:          # feste Mitte: gleiche W-Punkte auf allen Stufen (Stufenvergleich, Regel 3.2)
            ic = min(range(len(xs)), key=lambda i: abs(xs[i] - x0))
            rc = a.rc
        st["mitte"] = {"x": xs[ic], "rho": rc}
        drs = [float(v) for v in a.w_drho.split(",")]
        innen = [i for i in range(len(xs)) if abs(xs[i] - xs[ic]) <= a.w_dx + 1e-15]
        if len(innen) < 3:            # Version 2: Mitte am Gitterrand -> die 3 naechsten Profile (Fit extrapoliert)
            innen = sorted(range(len(xs)), key=lambda i: abs(xs[i] - xs[ic]))[:3]
            zeilen.append(f"  W-Gitter: weniger als 3 Profile im Fenster +-{a.w_dx:.0e}, genommen die 3 naechsten um "
                          f"omega^2 = {xs[ic]:.7f}")
        pkt_r, pkt_i = [], []
        for i in innen:
            for dr_ in drs:
                pkt_r.append(complex(rc + dr_, 0.0))
                pkt_i.append(i)
        Dw = direkt_m(L, pkt_r, pkt_i, [1.0] * len(pkt_r), gram=False)
        W = [complex(float(Dw["la"][k].real), float(Dw["lb"][k].real)) for k in range(len(pkt_r))]
        im_rest = max(float(Dw["la"][k].imag.abs() + Dw["lb"][k].imag.abs()) / max(abs(W[k]), 1e-300)
                      for k in range(len(pkt_r)))
        gitter = [{"x": xs[pkt_i[k]], "rho": pkt_r[k].real, "W": W[k]} for k in range(len(W))]
        st["W_gitter"] = gitter
        st["W_im_rest_rel"] = im_rest
        # s(x): l_a an der Stelle l_b = 0 (lineare Interpolation in rho)
        sx = []
        for i in innen:
            ws = [(g["rho"], g["W"]) for g in gitter if g["x"] == xs[i]]
            for (r1, w1), (r2, w2_) in zip(ws, ws[1:]):
                if w1.imag * w2_.imag <= 0 and w1.imag != w2_.imag:
                    t_ = w1.imag / (w1.imag - w2_.imag)
                    sx.append({"x": xs[i], "rho_b": r1 + t_ * (r2 - r1), "s": w1.real + t_ * (w2_.real - w1.real)})
                    break
        st["s_von_x"] = sx
        zeilen.append("  s(x) = L(y_a) an L(y_b) = 0: " + ", ".join(f"{v['x']:.7f}: {v['s']:+.4e} (rho {v['rho_b']:.9f})"
                                                                 for v in sx))
        # Fit-Punkte: bis zu 5 Profile um die Mitte (mindestens 2 verschiedene omega^2), rho innerhalb 1e-4 um rc
        x_nahe = {xs[i] for i in sorted(innen, key=lambda i: abs(xs[i] - xs[ic]))[:5]}
        nahe = [g for g in gitter if g["x"] in x_nahe and abs(g["rho"] - rc) <= 1.01e-4]
        fit, grund = lin_fit_nullstelle([(g["rho"] - rc, g["x"] - xs[ic], g["W"]) for g in nahe])
        wn = None
        if fit is not None:
            dr0, dx0, J, res, cond = fit
            wn = {"rho": rc + dr0, "x": xs[ic] + dx0, "J": J, "fit_rest": res, "condJ": cond,
                  "detJ": J[0][0] * J[1][1] - J[0][1] * J[1][0], "n_punkte": len(nahe)}
            st["W_null"] = wn
            zeilen.append(f"  Nullstelle von W (linearer Fit, {len(nahe)} Punkte): rho* = {wn['rho']:.10f}, "
                          f"omega*^2 = {wn['x']:.9f}, det J = {wn['detJ']:.3e}, cond J = {cond:.1e}, Fitrest {res:.1e}, "
                          f"|Im|/|W| max {im_rest:.1e}")
        else:
            st["W_null_fehler"] = grund
            zeilen.append(f"  Nullstelle von W: Fit nicht moeglich ({grund}); Umlaufzahl trotzdem (Rechteck um x0)")
        sichern()
        # 4. Umlaufzahl von W auf Rechtecken
        if wn is None:
            # Rueckfall (Leitung 30.09.): Rechtecke um x0 und Re rho des Pols dort; rho0, falls der Pol nicht konvergierte
            ic_u = min(range(len(xs)), key=lambda i: abs(xs[i] - x0))
            rc_u = pol[ic_u]["rho"].real if pol[ic_u]["konvergiert"] else rho0
            if a.rc is not None:
                rc_u = a.rc
            zeilen.append(f"  Rechtecke ohne Fit um omega^2 = {xs[ic_u]:.7f}, rho = {rc_u:.10f}, drho mindestens "
                          f"{a.u_drho_ohne_fit:.1e}")
        else:
            ic_u, rc_u = ic, rc
        st["umlauf"] = []
        for dx_r in [float(v) for v in a.u_dx.split(",")]:
            if not budget.ok(f"Umlauf dx = {dx_r}", 20.0):
                break
            try:
                e_u = umlauf_rechteck(L, xs, ic_u, rc_u, dx_r, wn, a, zeilen)
            except (RuntimeError, ValueError, ZeroDivisionError) as err:
                e_u = {"dx": dx_r, "fehler": f"{type(err).__name__}: {err}"}
                zeilen.append(f"  Umlauf dx = {dx_r:.1e}: Fehler {e_u['fehler']}")
            st["umlauf"].append(e_u)
            sichern()
            # Fit-Mittelpunkt ausserhalb des Rechtecks (oder im aeusseren Fuenftel): zusaetzlich neu legen
            if wn is None or a.neu_legen != "ja":
                continue
            drho_r = rechteck_drho(dx_r, wn, a)
            if abs(wn["x"] - xs[ic_u]) <= 0.8 * dx_r and abs(wn["rho"] - rc_u) <= 0.8 * drho_r:
                continue
            if not budget.ok(f"Rechteck neu legen dx = {dx_r}", a.neu_profile * (t_prof or 20.0) + 30.0):
                st["umlauf"].append({"dx": dx_r, "neu_gelegt": True, "fehler": "neu legen entfallen (Zeit)"})
                zeilen.append(f"  Rechteck dx = {dx_r:.1e} neu legen: entfaellt (Zeit)")
                sichern()
                continue
            try:
                e_n = umlauf_neu_gelegt(a, pot, h, f_rand, dev, budget, zeilen, wn, dx_r)
            except (RuntimeError, ValueError, ZeroDivisionError) as err:
                e_n = {"dx": dx_r, "neu_gelegt": True, "fehler": f"{type(err).__name__}: {err}"}
                zeilen.append(f"  Rechteck dx = {dx_r:.1e} neu legen: Fehler {e_n['fehler']}")
            st["umlauf"].append(e_n)
            sichern()


def umlauf_neu_gelegt(a, pot, h, f_rand, dev, budget, zeilen, wn, dx_r):
    """Rechteck um den Fit-Mittelpunkt (wn["x"], wn["rho"]) mit neuen Profilen bei x* + dx_r * (-1 ... 1); vorher ein
    zweiter linearer Fit auf dem neuen Gitter (Mitte in rho nachgefuehrt, falls er gelingt)."""
    n = max(3, a.neu_profile)
    xs_n = [wn["x"] + dx_r * (2.0 * k / (n - 1) - 1.0) for k in range(n)]
    profs, xs_ok, _ = profile_stapel(xs_n, pot, h, dev, budget, zeilen, reserve=10.0)
    if len(profs) < 3:
        zeilen.append(f"  Rechteck dx = {dx_r:.1e} neu legen: nur {len(profs)} Profile")
        return {"dx": dx_r, "neu_gelegt": True, "fehler": f"nur {len(profs)} Profile"}
    ordn = sorted(range(len(xs_ok)), key=lambda i: xs_ok[i])
    profs = [profs[i] for i in ordn]
    xs_ok = [xs_ok[i] for i in ordn]
    L1 = lin_multi(profs, h, f_rand, dev)
    ic_n = min(range(len(xs_ok)), key=lambda i: abs(xs_ok[i] - wn["x"]))
    rc_n = wn["rho"]
    # zweiter Fit auf dem neuen Gitter (5 rho-Werte je Profil, +-1e-4 um rho*)
    drs = [-1e-4, -3e-5, 0.0, 3e-5, 1e-4]
    pr = [complex(rc_n + d, 0.0) for _ in xs_ok for d in drs]
    pi_ = [i for i in range(len(xs_ok)) for _ in drs]
    Dw = direkt_m(L1, pr, pi_, [1.0] * len(pr), gram=False)
    W = [complex(float(Dw["la"][k].real), float(Dw["lb"][k].real)) for k in range(len(pr))]
    fit2, grund2 = lin_fit_nullstelle([(pr[k].real - rc_n, xs_ok[pi_[k]] - xs_ok[ic_n], W[k]) for k in range(len(pr))])
    wn2 = wn
    if fit2 is not None:
        dr2, dx2, J2, res2, cond2 = fit2
        wn2 = {"rho": rc_n + dr2, "x": xs_ok[ic_n] + dx2, "J": J2, "fit_rest": res2, "condJ": cond2,
               "detJ": J2[0][0] * J2[1][1] - J2[0][1] * J2[1][0]}
        rc_n = wn2["rho"]
    zeilen.append(f"  Rechteck dx = {dx_r:.1e} NEU GELEGT um den Fit-Mittelpunkt omega^2 = {wn['x']:.9f} "
                  f"({len(xs_ok)} neue Profile); zweiter Fit: "
                  + (f"omega*^2 = {wn2['x']:.9f}, rho* = {wn2['rho']:.10f}, cond J = {wn2['condJ']:.1e}"
                     if fit2 is not None else f"nicht moeglich ({grund2})"))
    e = umlauf_rechteck(L1, xs_ok, ic_n, rc_n, dx_r, wn2, a, zeilen)
    e.update({"neu_gelegt": True, "x_neu": xs_ok, "fit_neu": wn2 if fit2 is not None else None,
              "fit_neu_fehler": grund2})
    return e


def phasentest(xs, A, zeilen):
    """Phase von A_norm links und rechts der Nullstelle; naechster Abstand der komplexen Kurve zum Ursprung aus einem
    komplexen Polynom (Grad 2) durch die 5 innersten Punkte."""
    out = {}
    i0 = min(range(len(xs)), key=lambda i: abs(A[i]))
    ph = [cmath.phase(v) for v in A]
    out["phase"] = ph
    # Phase relativ zur Phase am aeussersten linken Punkt, modulo pi (0 = gleiche Gerade)
    ref = ph[0]
    abw = [((p - ref + PI / 2.0) % PI) - PI / 2.0 for p in ph]
    out["phase_mod_pi_relativ"] = abw
    links = [i for i in range(len(xs)) if xs[i] < xs[i0]]
    rechts = [i for i in range(len(xs)) if xs[i] > xs[i0]]
    if links and rechts:
        il, ir = max(links), min(rechts)
        sprung = ((ph[ir] - ph[il]) % (2.0 * PI))
        out["sprung_nachbarn"] = sprung
        out["sprung_minus_pi"] = sprung - PI
    # komplexes Polynom
    innen = sorted(range(len(xs)), key=lambda i: abs(xs[i] - xs[i0]))[:5]
    try:
        _polynom_abstand(xs, A, innen, i0, abw, out, zeilen)
    except (RuntimeError, ValueError, ZeroDivisionError) as err:
        out["polynom_fehler"] = f"{type(err).__name__}: {err}"
        zeilen.append(f"  Naechster Abstand zum Ursprung: nicht bestimmbar ({out['polynom_fehler']})")
    return out


def _polynom_abstand(xs, A, innen, i0, abw, out, zeilen):
    if len(innen) >= 4:
        xc = xs[i0]
        X = torch.tensor([[1.0, xs[i] - xc, (xs[i] - xc) ** 2] for i in innen], dtype=C128)
        Y = torch.tensor([A[i] for i in innen], dtype=C128)
        c = torch.linalg.lstsq(X, Y.unsqueeze(1)).solution.squeeze(1)
        c0, c1, c2 = [complex(v) for v in c.tolist()]
        rest = float((X @ c - Y).abs().max())
        # Minimum von |c0 + c1 t + c2 t^2| ueber reelles t (Newton auf d|A|^2/dt ab t = -Re(c0 c1*)/|c1|^2)
        t = -(c0 * c1.conjugate()).real / abs(c1) ** 2
        for _ in range(50):
            Av = c0 + c1 * t + c2 * t * t
            Ap = c1 + 2.0 * c2 * t
            g1 = 2.0 * (Av.conjugate() * Ap).real
            g2 = 2.0 * (abs(Ap) ** 2 + (Av.conjugate() * 2.0 * c2).real)
            if g2 <= 0:
                break
            t -= g1 / g2
        dmin = abs(c0 + c1 * t + c2 * t * t)
        out.update({"x_min": xc + t, "d_min": dmin, "abl": abs(c1 + 2.0 * c2 * t), "dx_senkrecht": dmin / abs(c1),
                    "fitrest": rest, "c": [c0, c1, c2]})
        zeilen.append(f"  Phasentest: Sprung zwischen Nachbarn - pi = {out.get('sprung_minus_pi', float('nan')):+.3e}; "
                      f"Phase mod pi (rel. links aussen): {', '.join(f'{v:+.2e}' for v in abw)}")
        zeilen.append(f"  Naechster Abstand zum Ursprung: d_min = {dmin:.3e} bei omega^2 = {xc + t:.10f}, |A'| = "
                      f"{abs(c1):.4e}, d_min/|A'| = {dmin / abs(c1):.3e} (Einheit omega^2), Fitrest {rest:.1e}")
    return out


def rechteck_drho(dx_r, wnull, a):
    """halbe rho-Hoehe: mit Fit aus J (x-Seiten ueberstreichen < 2 atan(1/3); l_b-Nullinie bleibt innen), ohne Fit
    --u-drho-ohne-fit; hoechstens 5e-3."""
    if wnull is None:
        return min(max(a.u_drho, a.u_drho_ohne_fit), 5e-3)
    J = wnull["J"]
    jr = math.hypot(J[0][0], J[1][0])
    jx = math.hypot(J[0][1], J[1][1])
    drho = max(a.u_drho, 3.0 * jx * dx_r / max(jr, 1e-300))
    wand = abs(J[1][1] / J[1][0]) * dx_r if J[1][0] != 0 else 0.0     # l_b = 0: drho = -(dlb/dx)/(dlb/drho) dx
    return min(max(drho, 1.5 * wand), 5e-3)


def umlauf_rechteck(L, xs, ic, rc, dx_r, wnull, a, zeilen):
    """Rechteck: x von xs[ic] - dx_r bis + dx_r (nur vorhandene Profile), rho von rc - drho bis rc + drho. drho aus der
    Jacobimatrix (Rechteck im W-Raum etwa quadratisch), mindestens das 1,5-fache der Wanderung der l_b-Nullinie."""
    xl = [i for i in range(len(xs)) if abs(xs[i] - xs[ic]) <= dx_r * (1 + 1e-9)]
    xl.sort(key=lambda i: xs[i])
    if len(xl) < 3:
        zeilen.append(f"  Umlauf W auf Rechteck dx = {dx_r:.1e}: zu wenige Profile ({len(xl)}) um omega^2 = {xs[ic]:.7f}")
        return {"dx": dx_r, "rho_c": rc, "x_c": xs[ic], "fehler": f"zu wenige Profile ({len(xl)})"}
    x_lo, x_hi = xl[0], xl[-1]
    drho = rechteck_drho(dx_r, wnull, a)
    ns = a.u_n
    r_lo, r_hi = rc - drho, rc + drho
    pfad = []                                       # (rho, ix)
    for i in xl:                                    # unten: rho = r_lo, x steigt
        pfad.append((r_lo, i))
    for k in range(1, ns):                          # rechts: x = x_hi, rho steigt
        pfad.append((r_lo + 2.0 * drho * k / ns, x_hi))
    for i in reversed(xl):                          # oben: rho = r_hi, x faellt
        pfad.append((r_hi, i))
    for k in range(1, ns):                          # links: x = x_lo, rho faellt
        pfad.append((r_hi - 2.0 * drho * k / ns, x_lo))
    Dw = direkt_m(L, [complex(p[0], 0.0) for p in pfad], [p[1] for p in pfad], [1.0] * len(pfad), gram=False)
    W = [complex(float(Dw["la"][k].real), float(Dw["lb"][k].real)) for k in range(len(pfad))]
    # rho-Seiten (gleiches Profil) adaptiv verfeinern, bis jeder Phasensprung dort < 0,3 rad ist (billig)
    for _ in range(8):
        neu = []
        for k in range(len(pfad)):
            k2 = (k + 1) % len(pfad)
            if pfad[k][1] == pfad[k2][1] and abs(cmath.phase(W[k2] * W[k].conjugate())) > 0.3:
                neu.append(k)
        if not neu:
            break
        mitte = [(0.5 * (pfad[k][0] + pfad[(k + 1) % len(pfad)][0]), pfad[k][1]) for k in neu]
        Dn = direkt_m(L, [complex(p[0], 0.0) for p in mitte], [p[1] for p in mitte], [1.0] * len(mitte), gram=False)
        Wn = [complex(float(Dn["la"][k].real), float(Dn["lb"][k].real)) for k in range(len(mitte))]
        p2, w2l = [], []
        j = 0
        for k in range(len(pfad)):
            p2.append(pfad[k])
            w2l.append(W[k])
            if j < len(neu) and neu[j] == k:
                p2.append(mitte[j])
                w2l.append(Wn[j])
                j += 1
        pfad, W = p2, w2l
    u, sprung = umlauf(W)
    wmin = min(abs(w) for w in W)
    zeilen.append(f"  Umlauf W auf Rechteck dx = {dx_r:.1e}, drho = {drho:.3e} ({len(pfad)} Punkte): {u:+.4f}, "
                  f"groesster Phasensprung {sprung:.3f} rad (aufgeloest: {sprung < 0.4}), min |W| = {wmin:.3e}")
    return {"dx": dx_r, "drho": drho, "rho_c": rc, "x_c": xs[ic], "umlauf": u, "max_sprung": sprung,
            "aufgeloest": sprung < 0.4, "min_absW": wmin, "pfad": [{"rho": p[0], "x": xs[p[1]], "W": w}
                                                                  for p, w in zip(pfad, W)]}


# ================================================================ Kommando kurve (Teil b)

def kurve(a, dev, budget, zeilen, erg, sichern):
    pot = POT_LOG if a.pot == "log" else pot_poly(a.beta)
    h = float(a.h.split(",")[0])
    f_rand = FRAND.get(h, 1e-8)
    if a.omega2_liste:
        xs = [float(v) for v in a.omega2_liste.split(",")]
    else:
        lo = max(omega2_min(pot) + a.abstand, a.xmin)
        n = int(math.floor((a.xmax - lo) / a.dx + 1e-9)) + 1
        xs = [round(lo + k * a.dx, 6) for k in range(n)]
    zeilen.append(f"=== kurve {pot_text(pot)}, h = {h}, omega^2 = {xs[0]} .. {xs[-1]} ({len(xs)} Werte), "
                  f"Existenz omega^2 > {omega2_min(pot):.4f}")
    st = {"potential": pot_text(pot), "pot": pot, "h": h, "f_rand": f_rand, "x_geplant": xs,
          "dim": G210_DIM["d"], "nu": g210_nu()}                                               # G2-10
    erg["kurve"] = st
    # Vorrang: jeder zweite Wert zuerst (grobes Raster bleibt bei Zeitnot vollstaendig ueber den Bereich)
    reihenf = xs[::2] + xs[1::2]
    profs, xs_ok, t_prof = profile_stapel(reihenf, pot, h, dev, budget, zeilen, reserve=a.reserve)
    ordn = sorted(range(len(xs_ok)), key=lambda i: xs_ok[i])
    profs = [profs[i] for i in ordn]
    xs = [xs_ok[i] for i in ordn]
    if not profs:
        return
    L = lin_multi(profs, h, f_rand, dev)
    st.update({"x": xs, "S0": [p["f0"] ** 2 for p in profs], "Q": [ladung_3d(p) for p in profs],
               "R_halb": [r_halb(p) for p in profs], "R_aus": L["R_aus"], "r_m": L["r_m"], "sek_profil_max": t_prof})
    zeilen.append(f"  {len(xs)} Profile, R = {L['R_aus']:.2f}, r_m = {L['r_m']:.3f}; S0 = "
                  + ", ".join(f"{p['f0'] ** 2:.4f}" for p in profs))
    sichern()
    # W-Abtastung bei reellem rho im Fenster (1 - omega, 1 + omega)
    pkt_r, pkt_i = [], []
    for i, x in enumerate(xs):
        om = math.sqrt(x)
        r0, r1 = 1.0 - om + 0.002, 1.0 + om - 0.002
        for k in range(a.n_rho):
            pkt_r.append(complex(r0 + (r1 - r0) * k / (a.n_rho - 1), 0.0))
            pkt_i.append(i)
    W = []
    wachs = []
    for s0_ in range(0, len(pkt_r), a.stapel):
        Dw = direkt_m(L, pkt_r[s0_:s0_ + a.stapel], pkt_i[s0_:s0_ + a.stapel], [g210_nu()] * len(pkt_r[s0_:s0_ + a.stapel]),
                      gram=False)
        W += [complex(float(Dw["la"][k].real), float(Dw["lb"][k].real)) for k in range(len(Dw["la"]))]
        wachs += [float(v) for v in Dw["wachstum"].tolist()]
    kand = []
    for i, x in enumerate(xs):
        idx = [k for k in range(len(pkt_r)) if pkt_i[k] == i]
        ki = []
        for k1, k2 in zip(idx, idx[1:]):
            w1, w2_ = W[k1], W[k2]
            if w1.imag * w2_.imag < 0:
                t_ = w1.imag / (w1.imag - w2_.imag)
                r1_, r2_ = pkt_r[k1].real, pkt_r[k2].real
                steig = (w2_.imag - w1.imag) / (r2_ - r1_)
                s = w1.real + t_ * (w2_.real - w1.real)
                ki.append({"x": x, "ix": i, "rho_b": r1_ + t_ * (r2_ - r1_), "s": s, "s_durch_steigung": s / abs(steig)})
        kand += ki[:a.max_kand]
    st["kandidaten"] = kand
    st["wachstum_max"] = max(wachs) if wachs else None
    zeilen.append(f"  W-Abtastung {a.n_rho} Punkte je omega^2: {len(kand)} Kandidaten (Nullstellen von L(y_b)); "
                  f"Kernwachstum max {st['wachstum_max']:.1e}")
    sichern()
    # komplexe Pole zu den Kandidaten (Pluecker-Newton, alle in einem Stapel)
    if kand and budget.ok("Newton kurve", 30.0):
        pol = newton_m(L, [complex(k_["rho_b"], -1e-5) for k_ in kand], [k_["ix"] for k_ in kand],
                       [g210_nu()] * len(kand), iters=a.iter_newton)
        for k_, p_ in zip(kand, pol):
            k_["pol"] = p_["rho"]
            k_["pol_konvergiert"] = p_["konvergiert"]
            k_["Gamma"] = -p_["rho"].imag
        zeilen.append("  omega^2 | rho_b (L(y_b) = 0) | s = L(y_a) | Pol | Gamma")
        for k_ in kand:
            zeilen.append(f"    {k_['x']:.4f} | {k_['rho_b']:.6f} | {k_['s']:+.3e} | {fz(k_['pol'], 7)} | "
                          f"{k_['Gamma']:.3e}{'' if k_['pol_konvergiert'] else ' (nicht konv.)'}")
        sichern()
    # Aeste verfolgen (naechster rho_b) und Vorzeichenwechsel von s
    aeste = []
    for i, x in enumerate(xs):
        for k_ in [k for k in kand if k["ix"] == i]:
            best = None
            for ast in aeste:
                if ast[-1]["ix"] == i - 1:
                    d_ = abs(ast[-1]["rho_b"] - k_["rho_b"])
                    if d_ < a.ast_tol and (best is None or d_ < best[0]):
                        best = (d_, ast)
            if best is not None:
                best[1].append(k_)
            else:
                aeste.append([k_])
    wechsel = []
    for n_ast, ast in enumerate(aeste):
        for k1, k2 in zip(ast, ast[1:]):
            if k1["s"] * k2["s"] < 0:
                t_ = k1["s"] / (k1["s"] - k2["s"])
                wechsel.append({"ast": n_ast, "x_lo": k1["x"], "x_hi": k2["x"],
                                "x_stern_linear": k1["x"] + t_ * (k2["x"] - k1["x"]),
                                "rho_stern_linear": k1["rho_b"] + t_ * (k2["rho_b"] - k1["rho_b"]),
                                "Gamma_lo": k1.get("Gamma"), "Gamma_hi": k2.get("Gamma")})
    st["aeste"] = [[{"x": k["x"], "rho_b": k["rho_b"], "s": k["s"], "Gamma": k.get("Gamma")} for k in ast]
                   for ast in aeste]
    st["vorzeichenwechsel"] = wechsel
    for w in wechsel:
        zeilen.append(f"  Vorzeichenwechsel von s auf Ast {w['ast']}: omega*^2 ~ {w['x_stern_linear']:.5f} "
                      f"(zwischen {w['x_lo']} und {w['x_hi']}), rho* ~ {w['rho_stern_linear']:.5f}")
    if not wechsel:
        zeilen.append("  kein Vorzeichenwechsel von s gefunden")
    sichern()
    # Verfeinerung: Sekante in omega^2 je Wechsel (neue Profile), rho-Fenster eng
    st["fein"] = []
    for w in wechsel[:a.n_wechsel_fein]:
        fein = {"start": w, "schritte": []}
        st["fein"].append(fein)
        xa, xb = w["x_lo"], w["x_hi"]
        sa = sb = None
        rho_ref = w["rho_stern_linear"]
        for it in range(a.n_fein):
            xn = w["x_stern_linear"] if it == 0 else (xb - sb * (xb - xa) / (sb - sa) if sb != sa else 0.5 * (xa + xb))
            if not budget.ok(f"Verfeinerung {it}", (t_prof or 20.0) + 20.0):
                break
            ps, xo, _ = profile_stapel([xn], pot, h, dev, budget, zeilen, reserve=0.0)
            if not ps:
                break
            L1 = lin_multi(ps, h, f_rand, dev)
            rr = [complex(rho_ref + a.fein_fenster * (2.0 * k / (a.n_fein_rho - 1) - 1.0), 0.0) for k in range(a.n_fein_rho)]
            Dw = direkt_m(L1, rr, [0] * len(rr), [g210_nu()] * len(rr), gram=False)
            Wf = [complex(float(Dw["la"][k].real), float(Dw["lb"][k].real)) for k in range(len(rr))]
            sn, rn = None, None
            for k in range(len(rr) - 1):
                if Wf[k].imag * Wf[k + 1].imag < 0:
                    t_ = Wf[k].imag / (Wf[k].imag - Wf[k + 1].imag)
                    rk = rr[k].real + t_ * (rr[k + 1].real - rr[k].real)
                    if rn is None or abs(rk - rho_ref) < abs(rn - rho_ref):
                        rn, sn = rk, Wf[k].real + t_ * (Wf[k + 1].real - Wf[k].real)
            pn = newton_m(L1, [complex(rn if rn is not None else rho_ref, -1e-7)], [0], [g210_nu()], iters=a.iter_newton)[0]
            fein["schritte"].append({"x": xn, "rho_b": rn, "s": sn, "pol": pn["rho"], "Gamma": -pn["rho"].imag,
                                     "konvergiert": pn["konvergiert"]})
            zeilen.append(f"    fein {it}: omega^2 = {xn:.8f}, rho_b = {rn}, s = {sn}, Pol {fz(pn['rho'], 8)}")
            sichern()
            if sn is None:
                break
            rho_ref = rn
            if sa is None:
                xa, sa = xn, sn
                # zweiter Punkt: der Rasterwert auf der anderen Seite (s bekannt aus der Abtastung)
                s_hi = next((k["s"] for k in kand if k["x"] == w["x_hi"] and abs(k["rho_b"] - w["rho_stern_linear"]) < a.ast_tol), None)
                s_lo = next((k["s"] for k in kand if k["x"] == w["x_lo"] and abs(k["rho_b"] - w["rho_stern_linear"]) < a.ast_tol), None)
                if s_hi is not None and s_hi * sn < 0:
                    xb, sb = w["x_hi"], s_hi
                elif s_lo is not None:
                    xb, sb = w["x_lo"], s_lo
                else:
                    break
            else:
                xa, sa, xb, sb = xb, sb, xn, sn
            if abs(xb - xa) < 1e-9:
                break


# ================================================================ G2-10: dim als Parameter, Barriere, Leiter-Auswertung

G210_DIM = {"d": 3.0}
G210_TAB = {1: (0.671, 0.02), 2: (0.5971, 0.003), 3: (0.5674, 0.0015), 4: (0.5515, 0.001), 5: (0.5417, 0.001)}
G210_OMEGA_D = {1.0: 2.0, 2.0: 2.0 * PI, 3.0: 4.0 * PI}


def g210_nu():
    """nu = l + (dim - 1)/2 fuer l = 0 (dim = 3: 1 wie bisher; dim = 2: 1/2; dim = 1: 0, gerade)."""
    return 0.5 * (G210_DIM["d"] - 1.0)


def g210_c(eps):
    return 0.826 + 0.24 * eps          # KARTE.md: c(eps) = Re rho* - omega* aus der 3D-Leiter


def g210_profilwerte(p, dim, beta):
    """Q = 2 omega Omega_d int f^2 r^(d-1) dr und Virialrest d(omega^2 N - V) - (d - 2) G (relativ), Trapez."""
    h = p["h"]
    n = int(radius_wo(p, 1e-12 * p["f0"]) / h) + 2
    f, fp = f_werte(p, n)
    w2 = p["w2"]
    N = G = V = 0.0
    for j in range(n):
        g_ = (0.5 if j in (0, n - 1) else 1.0) * h * (j * h) ** (dim - 1.0)
        s = f[j] * f[j]
        N += g_ * s
        G += g_ * fp[j] * fp[j]
        V += g_ * (s - s * s + beta * s ** 3)
    om_d = G210_OMEGA_D.get(float(dim), 2.0 * PI)
    rest = (dim * (w2 * N - V) - (dim - 2.0) * G) / (dim * (w2 * N + V))
    return {"Q": 2.0 * math.sqrt(w2) * om_d * N, "virialrest": rest}


def g210_liste(a):
    if a.omega2_liste:
        return [float(v) for v in a.omega2_liste.split(",")]
    n = int(math.floor((a.xmax - a.xmin) / a.dx + 1e-9)) + 1
    return [round(a.xmin + k * a.dx, 6) for k in range(n)]


def barriere(a, dev, budget, zeilen, erg, sichern):
    """x_B aus den Profilen allein (vor jeder Polsuche): groesstes omega^2 der Liste mit dp(S0) > c(eps)^2."""
    beta, h = a.beta, float(a.h.split(",")[0])
    xs = g210_liste(a)
    zeilen.append(f"=== barriere dim = {a.dim}, beta = {beta}, h = {h}, omega^2 = {xs[0]} .. {xs[-1]} ({len(xs)} Werte)")
    zeilen.append("  omega^2 | S0 | dp(S0) | c(eps)^2 | B | Q | Virialrest")
    zeilen_b = []
    erg["barriere"] = {"dim": a.dim, "beta": beta, "h": h, "x_geplant": xs, "werte": zeilen_b}
    for x in xs:
        if zeilen_b and not budget.ok(f"barriere omega^2 = {x}", 40.0):
            break
        try:
            p = profil_pot(x, a.dim, pot_poly(beta), 0.5 * h, dev)
        except (ValueError, RuntimeError) as err:
            zeilen.append(f"  {x}: Profilfehler {err}")
            continue
        s0 = p["f0"] ** 2
        eps = x - 0.5
        dp = 1.0 - 4.0 * s0 + 9.0 * beta * s0 * s0
        c2 = g210_c(eps) ** 2
        pw = g210_profilwerte(p, a.dim, beta)
        zeilen_b.append({"x": x, "S0": s0, "dp": dp, "c2": c2, "B": dp - c2, "Q": pw["Q"], "virialrest": pw["virialrest"]})
        zeilen.append(f"  {x:.4f} | {s0:.6f} | {dp:.6f} | {c2:.6f} | {dp - c2:+.6f} | {pw['Q']:.4f} | {pw['virialrest']:+.2e}")
        sichern()
    mit = [z["x"] for z in zeilen_b if z["B"] > 0.0]
    erg["barriere"]["x_B"] = max(mit) if mit else None
    zus = None
    for z in sorted(zeilen_b, key=lambda z: z["x"]):
        if z["B"] > 0.0:
            zus = z["x"]
        else:
            break
    erg["barriere"]["x_B_zusammenhaengend_von_unten"] = zus
    erg["barriere"]["regel"] = "x_B = groesstes omega^2 der Liste mit dp(S0) > c(eps)^2 (KARTE.md); kein Pol geht ein"
    zeilen.append(f"  x_B = {erg['barriere']['x_B']} (zusammenhaengend von unten: {zus})")
    sichern()


def g210_lesen(pfade, schluessel):
    aus = []
    for p in [q for q in pfade.split(",") if q]:
        with open(p) as fh:
            aus.append((p, json.load(fh)["ergebnisse"].get(schluessel)))
    return aus


def g210_stellen(st):
    """Nulldurchgaenge der signierten Wurzel s aus einem kurve-Ergebnis; Lage verfeinert (Schritt mit kleinstem |s|)."""
    stellen = []
    for w in st.get("vorzeichenwechsel", []):
        x, rho, gam, quelle = w["x_stern_linear"], w["rho_stern_linear"], None, "linear"
        for fe in st.get("fein", []):
            s_ = fe["start"]
            if s_["x_lo"] == w["x_lo"] and s_["x_hi"] == w["x_hi"] and s_["ast"] == w["ast"]:
                ok = [sc for sc in fe["schritte"] if sc.get("s") is not None]
                if ok:
                    b = min(ok, key=lambda sc: abs(sc["s"]))
                    x, quelle = b["x"], "verfeinert"
                    pol = b.get("pol")
                    if isinstance(pol, list):
                        rho, gam = pol[0], -pol[1]
        stellen.append({"x": x, "x_lo": w["x_lo"], "x_hi": w["x_hi"], "rho": rho, "Gamma": gam, "quelle": quelle,
                        "ast": w["ast"]})
    return stellen


def leiter(a, zeilen, erg):
    """Auswertung nach KARTE.md: V1 bis V4, Gegenproben d = 1 und d = 3, L3, Plausibilitaetsschranke."""
    aus = {}
    erg["leiter"] = aus
    haupt = g210_lesen(a.d2, "kurve")
    stellen, kand, xs_alle = [], [], []
    for pfad, st in haupt:
        if not st:
            continue
        stellen += g210_stellen(st)
        kand += st.get("kandidaten", [])
        xs_alle += st.get("x", [])
    stellen.sort(key=lambda z: z["x"])
    xB = None
    barr = []
    for pfad, b in g210_lesen(a.barr, "barriere"):
        if b:
            barr += b.get("werte", [])
    if barr:
        mit = [z["x"] for z in barr if z["B"] > 0.0]
        xB = max(mit) if mit else None
    aus["x_B_2D"] = xB
    aus["stellen"] = stellen
    # Zuordnung zur Tabelle (naechster Tabellenwert)
    zu = {}
    for s in stellen:
        n = min(G210_TAB, key=lambda k: abs(G210_TAB[k][0] - s["x"]))
        s["n"] = n
        s["in_spanne"] = abs(s["x"] - G210_TAB[n][0]) <= G210_TAB[n][1]
        if n not in zu or abs(s["x"] - G210_TAB[n][0]) < abs(zu[n]["x"] - G210_TAB[n][0]):
            zu[n] = s
    in_sp = {n: (n in zu and zu[n]["in_spanne"]) for n in (2, 3, 4, 5)}
    aus["V1"] = {"in_spanne_n2_bis_n5": in_sp, "zahl_stellen": len(stellen),
                 "bestanden": bool(stellen) and sum(in_sp.values()) >= 3}
    schritte = []
    for n1, n2 in ((3, 4), (4, 5)):
        if n1 in zu and n2 in zu:
            schritte.append({"von": n1, "nach": n2, "schritt_1_durch_eps": 1.0 / (zu[n2]["x"] - 0.5) - 1.0 / (zu[n1]["x"] - 0.5)})
    aus["V2"] = {"schritte": schritte, "band": [3.9, 5.2],
                 "bestanden": (all(3.9 <= z["schritt_1_durch_eps"] <= 5.2 for z in schritte) if schritte else None)}
    th = {}
    for n in (3, 4, 5):
        if n in zu:
            x, rho = zu[n]["x"], zu[n]["rho"]
            om, eps = math.sqrt(x), x - 0.5
            kc = math.sqrt(x + rho * rho - 1.5 + math.sqrt(4.0 * x * rho * rho + 1.0))
            R2 = (G210_DIM["d"] - 1.0) / (4.0 * math.sqrt(a.beta) * eps)
            th[str(n)] = kc * R2 / PI - n + 0.25
    aus["V3"] = {"theta_2D": th, "ziel": [0.63, 0.73], "rho_quelle": "Re rho des Pols am verfeinerten Schritt, sonst rho* linear",
                 "bestanden": (all(0.63 <= v <= 0.73 for v in th.values()) if th else None), "im_scheiterkatalog": False}
    ueber = [s["x"] for s in stellen if xB is not None and s["x"] > xB]
    aus["V4"] = {"x_B_2D": xB, "stellen_ueber_x_B": ueber, "n1_fehlt_erwartet": (xB is not None and xB < 0.67),
                 "bestanden": (not ueber) if xB is not None else None}
    aus["umlaufzahl"] = "vom Code nicht ausgegeben"
    sch = [not stellen, sum(1 for v in in_sp.values() if not v) >= 2,
           aus["V2"]["bestanden"] is False, aus["V4"]["bestanden"] is False]
    aus["scheitert"] = any(sch)
    # Plausibilitaet
    pl = {}
    pole = [k_ for k_ in kand if isinstance(k_.get("pol"), list) and k_.get("pol_konvergiert")]
    pl["im_rho_nicht_positiv"] = all(k_["pol"][1] <= 1e-12 for k_ in pole)
    pl["re_rho_im_fenster"] = all(1.0 - math.sqrt(k_["x"]) < k_["pol"][0] < 1.0 + math.sqrt(k_["x"]) for k_ in pole)
    pl["zahl_pole"] = len(pole)
    if barr:
        bs = sorted(barr, key=lambda z: z["x"])
        pl["virial_max"] = max(abs(z["virialrest"]) for z in bs)
        pl["virial_ok"] = pl["virial_max"] <= 1e-6
        dq = [b2["Q"] - b1["Q"] for b1, b2 in zip(bs, bs[1:])]
        pl["Q_monoton"] = all(d_ < 0 for d_ in dq) or all(d_ > 0 for d_ in dq)
    pl["bestanden"] = all(v for k, v in pl.items() if k in ("im_rho_nicht_positiv", "re_rho_im_fenster", "virial_ok",
                                                            "Q_monoton"))
    aus["plausibilitaet"] = pl
    # Gegenproben
    g1 = [s for _, st in g210_lesen(a.d1, "kurve") if st for s in g210_stellen(st)]
    aus["gegen_d1"] = {"stellen": g1, "bestanden": (not g1) if a.d1 else None}
    g3 = [s for _, st in g210_lesen(a.d3, "kurve") if st for s in g210_stellen(st)]
    ref3 = {2: 0.685129, 3: 0.631449}
    tr = {str(n): min((abs(s["x"] - r) for s in g3), default=None) for n, r in ref3.items()}
    aus["gegen_d3"] = {"abweichung": tr, "grenze": 2e-4,
                       "bestanden": (all(v is not None and v <= 2e-4 for v in tr.values()) if a.d3 else None)}
    # L3: gleiche Stellen mit halbem Schritt und groesserem Aussenrand (h = 0,01)
    l3 = [s for _, st in g210_lesen(a.l3, "kurve") if st for s in g210_stellen(st)]
    vgl = []
    for s in l3:
        nah = min(stellen, key=lambda z: abs(z["x"] - s["x"]), default=None)
        if nah is not None:
            vgl.append({"x_h002": nah["x"], "x_h001": s["x"], "diff": abs(nah["x"] - s["x"])})
    aus["L3"] = {"vergleich": vgl, "grenze": 1e-4,
                 "bestanden": (all(v["diff"] <= 1e-4 for v in vgl) if vgl else None)}
    aus["l3_vorschlag_omega2_liste"] = ",".join(f"{s['x_lo']},{s['x_hi']}" for s in stellen)
    zeilen.append("=== leiter (G2-10)")
    zeilen.append(json.dumps(jsonfest(aus), indent=1))


# ================================================================ Kommando nlfit (Teil c)

def nlfit(a, zeilen, erg):
    """liest zeit0.json-Dateien, nimmt je eta die Atmungslinie (|Re| > 1) aus differenz_zentrum und den Fenstern und
    passt log(Rate) gegen log(eta) an. Zusaetzlich: tatsaechliche Ballfrequenz nach dem Stoss aus der Linie nahe 0
    und die daraus folgende lineare Breite 1,07 (x_eff - x*)^2 (Modell 'Stoss verschiebt omega', PLAN.md)."""
    zeilen_tab = []
    for fn in a.dateien.split(","):
        with open(fn) as fh:
            dat = json.load(fh)
        for key, res in dat.get("ergebnisse", {}).items():
            if not isinstance(res, dict) or "analyse" not in res:
                continue
            w2 = float(res["w2"]) if "w2" in res else float(key.split("_dr")[0])
            om = math.sqrt(w2)
            for e in res["analyse"]:
                eta = e["reihe"]
                if eta == 0.0 or "differenz_zentrum" not in e:
                    continue
                linien = [p for p in e["differenz_zentrum"] if abs(p["re"]) > 1.0]
                linien.sort(key=lambda p: -p["amp"])
                zentrum = [p for p in e["differenz_zentrum"] if abs(p["re"]) < 0.05]
                zentrum.sort(key=lambda p: -p["amp"])
                if not linien:
                    continue
                rate = -0.5 * sum(p["im"] for p in linien[:2]) / min(2, len(linien))
                d_om = zentrum[0]["re"] if zentrum else 0.0
                x_eff = (om + d_om) ** 2
                fr = []
                for f_ in e.get("fenster", []):
                    ll = sorted([p for p in f_["pencil"] if abs(p["re"]) > 1.0], key=lambda p: -p["amp"])
                    fr.append(-0.5 * sum(p["im"] for p in ll[:2]) / min(2, len(ll)) if ll else float("nan"))
                zeilen_tab.append({"datei": fn, "omega2": w2, "dr": res["dr"], "T": res["T"], "eta": eta,
                                   "rate_spaet": rate, "fensterraten": fr, "d_omega": d_om, "x_eff": x_eff,
                                   "x_stern_falls_linear": [x_eff - math.sqrt(max(rate, 0.0) / a.cgam),
                                                            x_eff + math.sqrt(max(rate, 0.0) / a.cgam)]})
    erg["zeilen"] = zeilen_tab
    zeilen.append("  Datei | omega^2 | dr | T | eta | Rate (spaet) | Fensterraten | x_eff | x* falls rein linear")
    for z in zeilen_tab:
        zeilen.append(f"    {os.path.basename(os.path.dirname(z['datei']))} | {z['omega2']} | {z['dr']} | {z['T']} | "
                      f"{z['eta']} | {z['rate_spaet']:.3e} | {', '.join(f'{v:.2e}' for v in z['fensterraten'])} | "
                      f"{z['x_eff']:.6f} | {z['x_stern_falls_linear'][0]:.6f} / {z['x_stern_falls_linear'][1]:.6f}")
    # Potenzgesetz je (omega^2, dr, T)
    gruppen = {}
    for z in zeilen_tab:
        gruppen.setdefault((z["omega2"], z["dr"], z["T"]), []).append(z)
    erg["potenz"] = []
    for (w2, dr, T), zz in sorted(gruppen.items()):
        pts = [(math.log(z["eta"]), math.log(z["rate_spaet"])) for z in zz if z["rate_spaet"] > 0]
        if len(pts) >= 2:
            mx = sum(p[0] for p in pts) / len(pts)
            my = sum(p[1] for p in pts) / len(pts)
            sxx = sum((p[0] - mx) ** 2 for p in pts)
            p_ = sum((p[0] - mx) * (p[1] - my) for p in pts) / sxx if sxx > 0 else float("nan")
            erg["potenz"].append({"omega2": w2, "dr": dr, "T": T, "p": p_, "n": len(pts)})
            zeilen.append(f"  Potenz Rate ~ eta^p fuer omega^2 = {w2}, dr = {dr}, T = {T}: p = {p_:.3f} ({len(pts)} Punkte)")


# ================================================================ Hauptprogramm

def argumente():
    ap = argparse.ArgumentParser(description="Runde 7 BIC-2 (Erweiterung von Runde 6 resonanz3d)")
    ap.add_argument("kommando", choices=["rauch", "pole", "bruecke", "zeit0", "zeitlin", "exakt", "kurve", "nlfit",
                                         "barriere", "leiter"])   # G2-10: barriere, leiter
    ap.add_argument("--dim", type=float, default=3.0, help="G2-10: Raumdimension fuer kurve und barriere (l = 0)")
    ap.add_argument("--d2", default="", help="G2-10 leiter: kurve.json der Hauptlaeufe (dim 2), Komma")
    ap.add_argument("--d3", default="", help="G2-10 leiter: kurve.json der Gegenprobe dim 3, Komma")
    ap.add_argument("--d1", default="", help="G2-10 leiter: kurve.json der Gegenprobe dim 1, Komma")
    ap.add_argument("--l3", default="", help="G2-10 leiter: kurve.json der L3-Laeufe (h 0,01), Komma")
    ap.add_argument("--barr", default="", help="G2-10 leiter: barriere.json, Komma")
    # Runde 7: exakt
    ap.add_argument("--beta", type=float, default=0.5, help="exakt/kurve: U = S - S^2 + beta S^3")
    ap.add_argument("--x0", type=float, default=0.79768, help="exakt: Mitte des omega^2-Gitters")
    ap.add_argument("--rho0", type=float, default=1.744625, help="exakt: Re rho des Pols bei x0 (Keim)")
    ap.add_argument("--drho", type=float, default=0.4049, help="exakt: d Re rho / d omega^2 (Keim)")
    ap.add_argument("--cgam", type=float, default=1.07, help="exakt/nlfit: Gamma ~ cgam (omega^2 - omega*^2)^2")
    ap.add_argument("--offsets", default="0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4,2e-3,-2e-3,8e-3,-8e-3")
    ap.add_argument("--w-drho", dest="w_drho", default="-3e-4,-1e-4,-3e-5,0,3e-5,1e-4,3e-4")
    ap.add_argument("--w-dx", dest="w_dx", type=float, default=5e-4)
    ap.add_argument("--u-dx", dest="u_dx", default="5e-4,1e-4", help="exakt: halbe Rechteckbreiten in omega^2")
    ap.add_argument("--u-drho", dest="u_drho", type=float, default=2e-5, help="exakt: kleinste halbe Rechteckhoehe")
    ap.add_argument("--u-n", dest="u_n", type=int, default=60, help="exakt: Punkte je rho-Seite")
    ap.add_argument("--reserve", type=float, default=90.0, help="Sekunden Reserve nach den Profilen")
    ap.add_argument("--rc", type=float, default=None, help="exakt: feste rho-Mitte fuer W-Gitter und Rechtecke")
    ap.add_argument("--neu-legen", dest="neu_legen", default="ja", choices=["ja", "nein"],
                    help="exakt: Rechteck zusaetzlich um den Fit-Mittelpunkt legen, wenn dieser ausserhalb liegt")
    ap.add_argument("--neu-profile", dest="neu_profile", type=int, default=3,
                    help="exakt: Zahl neuer Profile fuer ein neu gelegtes Rechteck (mindestens 3)")
    ap.add_argument("--u-drho-ohne-fit", dest="u_drho_ohne_fit", type=float, default=5e-4,
                    help="exakt: halbe rho-Hoehe der Rechtecke, wenn der Fit nicht moeglich ist")
    # Runde 7: kurve
    ap.add_argument("--pot", default="poly", choices=["poly", "log"])
    ap.add_argument("--omega2-liste", dest="omega2_liste", default=None)
    ap.add_argument("--xmin", type=float, default=0.62)
    ap.add_argument("--xmax", type=float, default=0.905)
    ap.add_argument("--dx", type=float, default=0.02)
    ap.add_argument("--abstand", type=float, default=0.12, help="kurve: Abstand zur Duennwand-Grenze omega_min^2")
    ap.add_argument("--n-rho", dest="n_rho", type=int, default=400)
    ap.add_argument("--stapel", type=int, default=3000)
    ap.add_argument("--max-kand", dest="max_kand", type=int, default=8)
    ap.add_argument("--ast-tol", dest="ast_tol", type=float, default=0.03)
    ap.add_argument("--n-wechsel-fein", dest="n_wechsel_fein", type=int, default=2)
    ap.add_argument("--n-fein", dest="n_fein", type=int, default=4)
    ap.add_argument("--fein-fenster", dest="fein_fenster", type=float, default=0.01)
    ap.add_argument("--n-fein-rho", dest="n_fein_rho", type=int, default=81)
    # Runde 7: nlfit
    ap.add_argument("--dateien", default="", help="nlfit: zeit0.json-Dateien, durch Komma getrennt")
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
    G210_DIM["d"] = float(a.dim)                                                              # G2-10
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
    zeilen = [f"Runde 7 bic2 {a.kommando} Start {start}, Geraet {a.geraet}, torch {torch.__version__}"]
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

    _ZUSTAND.update({"zeilen": zeilen, "ergebnis": ergebnis, "sichern": sichern})
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
        sichern()
        # Runde 7: alle neuen Wege einmal mit winzigen Groessen (keine Physik)
        zeilen.append("Rauch exakt (h = 0.08, 5 Profile):")
        a.h, a.offsets, a.u_dx, a.u_n, a.iter_newton, a.reserve = "0.08", "0,2e-5,-2e-5,1e-4,-1e-4", "1e-4", 8, 8, 5.0
        a.w_dx, a.rc = 1e-4, 1.7446165
        ergebnis["ergebnisse"]["exakt"] = {}
        exakt(a, dev, budget, zeilen, ergebnis["ergebnisse"]["exakt"], sichern)
        sichern()
        zeilen.append("Rauch exakt, Gegenprobe G5 (Rechteck ohne Nullstelle, x0 = 0.8003; Version 2: dazu neu gelegt):")
        a.x0, a.rho0, a.rc = 0.8003, 1.744625 + 0.4049 * (0.8003 - 0.79768), None
        ergebnis["ergebnisse"]["exakt_G5"] = {}
        exakt(a, dev, budget, zeilen, ergebnis["ergebnisse"]["exakt_G5"], sichern)
        sichern()
        zeilen.append("Rauch exakt, Version 2: Fit nicht moeglich (nur ein rho-Wert), Umlauf trotzdem um x0:")
        a.x0, a.rho0, a.offsets, a.w_drho, a.w_dx = 0.79768, 1.744625, "0,2e-5,-2e-5", "0", 1e-6
        ergebnis["ergebnisse"]["exakt_ohne_fit"] = {}
        exakt(a, dev, budget, zeilen, ergebnis["ergebnisse"]["exakt_ohne_fit"], sichern)
        a.w_drho = "-3e-4,-1e-4,-3e-5,0,3e-5,1e-4,3e-4"
        sichern()
        for pot_art, beta, liste in (("poly", 0.45, "0.78,0.8"), ("log", 0.5, "0.7,0.8")):
            zeilen.append(f"Rauch kurve {pot_art}:")
            a.pot, a.beta, a.omega2_liste, a.n_rho, a.max_kand, a.n_fein, a.n_fein_rho = pot_art, beta, liste, 40, 3, 1, 11
            a.h = "0.08"
            ergebnis["ergebnisse"][f"kurve_{pot_art}"] = {}
            kurve(a, dev, budget, zeilen, ergebnis["ergebnisse"][f"kurve_{pot_art}"], sichern)
            sichern()
        zeilen.append("Rauch nlfit (auf der eigenen Rauch-Ausgabe):")
        a.dateien = os.path.join(out, "rauch.json")
        ergebnis["ergebnisse"]["nlfit"] = {}
        try:
            nlfit(a, zeilen, ergebnis["ergebnisse"]["nlfit"])
        except (KeyError, ValueError, ZeroDivisionError) as err:
            zeilen.append(f"  nlfit Rauch: {type(err).__name__} {err}")
        zeilen.append(f"Rauchtest durchgelaufen nach {uhr():.1f} s (Zahlen ohne Bedeutung).")
    elif a.kommando == "exakt":
        exakt(a, dev, budget, zeilen, ergebnis["ergebnisse"], sichern)
    elif a.kommando == "kurve":
        kurve(a, dev, budget, zeilen, ergebnis["ergebnisse"], sichern)
    elif a.kommando == "barriere":                                                            # G2-10
        barriere(a, dev, budget, zeilen, ergebnis["ergebnisse"], sichern)
    elif a.kommando == "leiter":                                                              # G2-10
        leiter(a, zeilen, ergebnis["ergebnisse"])
    elif a.kommando == "nlfit":
        nlfit(a, zeilen, ergebnis["ergebnisse"])
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


_ZUSTAND = {}


if __name__ == "__main__":
    try:
        main()
    except Exception:            # Sicherheitsnetz (Version 2): Bericht und JSON mit Traceback schreiben, dann rc = 1
        import traceback
        tb = traceback.format_exc()
        if _ZUSTAND:
            _ZUSTAND["zeilen"].append(f"ABBRUCH durch unerwarteten Fehler nach {uhr():.1f} s (Sicherheitsnetz):")
            _ZUSTAND["zeilen"].extend("  " + z for z in tb.rstrip().splitlines())
            _ZUSTAND["ergebnis"]["fehler"] = tb
            try:
                _ZUSTAND["sichern"]()
            except Exception:
                pass
        print(tb, flush=True)
        raise SystemExit(1)
