#!/usr/bin/env python3
"""Runde 6 (v3), Agent M2: Medium-Karten in 2D. Zwei komplexe Felder: psi (Q-Ball) und chi (stabiles Medium).

Karten (Auftrag RUNDE-06/AUFTRAG-MEDIUM-UND-2D-B.md, Abschnitt "Agent M2"; Plan, Vorhersagen und Aufrufe in PLAN.md):
    magnus      Wellen 8/9  drehender Ball m = +1/-1 (und m = 0) frei im stroemenden Medium: Querdrift?
    kielwasser  Wellen 4    gehaltener Ball im stroemenden Medium (Ruhesystem des Balls): Machkegel ueber c_s?
    wirbel      Wellen 18   grosser gehaltener Ball in schneller Stroemung: loest er chi-Wirbel ab? Zahl und Takt
    brechung    Wellen 14   Ball laeuft schraeg ueber eine Dichtestufe des Mediums: Winkel gegen Vorhersage
    profile     nur Schiessen der benutzten Profile (Kontrolle)
    alle        nur mit --rauch: alle Karten nacheinander
Linse (Wellen 15) und Kelvin-Helmholtz (Wellen 17): nur Papier (PLAN.md), kein Code.

Modell (psi wie tests2d_r3.py, chi wie die Medium-Rolle in r5d.py; d = 2):
    L = |psi_t|^2 - |(grad - i B(t)) psi|^2 + |chi_t|^2 - |(grad - i A(t)) chi|^2 - V
    V = U(S) + V_h(x) S + C + g4 C^2 + W(x) C + lam S C,   U(S) = S - S^2 + S^3/2,  S = |psi|^2,  C = |chi|^2
    psi_tt = (grad - iB)^2 psi - (U'(S) + lam C + V_h) psi
    chi_tt = (grad - iA)^2 chi - (1 + 2 g4 C + lam S + W) chi
    - A(t) = (-q r(t), 0) und B(t): gleichfoermige aeussere Felder, die nur waehrend der Rampe r: 0 -> 1 wirken
      (gleichfoermige "elektrische" Kraft auf die chi- bzw. psi-Ladung). Danach sind sie konstant und lokal reine Eichung
      (verdrehte periodische Randbedingung). Fuer q = 2 pi n/(2L) ist das exakt das Modell ohne Eichfeld mit
      chi ~ exp(i k_n x) (Stroemung quantisiert); andere q sind dieselbe lokale Physik mit einer Bloch-Phase am Rand.
    - Medium: C0 = 0,1, g4 = 0,5, lam = 0,1 (Startwerte des Auftrags); c_s^2 = g/(2 w0^2 + g), g = 2 g4 C, w0^2 = 1 + g.
    - W(x): aeusseres Potential nur fuer chi (Dichtestufe bei "brechung"); V_h: schwacher harmonischer Halter nur fuer
      psi (Hindernis bei "kielwasser" und "wirbel").
Ablauf je Lauf:
    1. Schiessen des Vakuumprofils (auf der CPU; Regel fuer m != 0 aus RUNDE-05/r5-2d-a/r5_2d_a.py, dort berichtigt).
    2. Relaxieren (Gradientenfluss, halbimplizit spektral): psi bei fester Ladung Q (omega = Q/(2N)), chi bei festem
       w0 (Fernfeld C0). Ball im Medium ist so eine stationaere Loesung, nicht der Vakuumball plus Medium.
    3. Start mit psi_t = -i (sin th/dt) psi, th = arccos(1 - dt^2 omega^2/2): exakte diskrete Kreisbahn des Verlet.
    4. Rampe r(t) = sin^2(pi t/(2 T_R)) fuer Stroemung (A) oder Anschub (B); danach messen.
Numerik: Laplace spektral (FFT, periodische Box [-L, L)^2), Velocity-Verlet, Randschicht fuer psi (psi_t daempfen)
und chi (Abweichung chi_t + i w chi daempfen; gleichfoermige und stationaere Stroemung bleibt unberuehrt).
Messung alle T_MESS: Schwerpunkt (Gewicht S^2), Kraft des Mediums F = -Int lam S grad C, Ladungen, Windung von psi
um den Ball, Zirkulation von chi um den Ball, chi-Wirbel Plakette fuer Plakette (Phasensumme / 2 pi).
Zwei Aufloesungen: grob dx = 0,3, dt = 0,05; fein dx = 0,2, dt = 0,025 (Latte L3).

Aufruf:  python medium2d.py KARTE [--stufe grob|fein|beide] [--rauch [--mini]] [--geraet cuda|cpu] [--out ORDNER]
Rauchtest: --rauch (Laufzeiten x 0,05, Zahlen ungueltig, Hochrechnung). --mini: grobes Gitter, x 0,02 (Formprobe CPU).
Ausgaben je Karte und Stufe: <karte>_<stufe>_roh.pt und _roh.json sofort nach der Rechnung (Rohdaten), dann
<karte>_bericht.txt und <karte>_ergebnis.json nach der Auswertung.
"""
import argparse
import cmath
import datetime
import json
import math
import os
import time
import traceback

import torch

F64 = torch.float64
C128 = torch.complex128
CPU = torch.device("cpu")
DEV = torch.device("cpu")          # in main() nach --geraet gesetzt
PI = math.pi

# ---- Schiessen (aus r5_2d_a.py; auf der CPU, weil die Tensoren klein sind) ----
H_ODE, X_ODE, SCHWANZ = 0.01, 60.0, 1e-3
KAND = {"normal": (256, 7), "mini": (64, 9)}     # Kandidaten je Runde, Runden (256^7 und 64^9 > 1e16)
R_TAB = 90.0

# ---- Medium und Kopplung (Startwerte des Auftrags) ----
C0, G4, LAM = 0.1, 0.5, 0.1

# ---- Numerik ----
L_BOX = 38.4                                       # n = 256 (grob) bzw. 384 (fein)
STUFEN = {"grob": (0.3, 0.05), "fein": (0.2, 0.025)}
STUFEN_MINI = {"grob": (0.6, 0.1), "fein": (0.48, 0.08)}
SPONGE, SIGMA0 = 8.0, 0.5
HALT_R = 12.0                                      # Halter V_h = a R^2 tanh(r^2/R^2): harmonisch innen, beschraenkt aussen
T_MESS = 1.0
DTAU, N_RELAX, RELAX_ZIEL = 0.4, 2500, 1e-8
RAUCH_FAKTOR, MINI_FAKTOR = 0.05, 0.02
N_THETA = 128
SNAP_ZAHL = 6

# ---- magnus (Wellen 8/9): frei beweglicher Ball, Stroemung in MG_RAMPE hochgefahren ----
MG_W2, MG_X0 = 0.60, -8.0
MG_RAMPE, MG_T = 100.0, 400.0
MG_LAEUFE = (
    {"name": "m+1_u0.4", "m": 1, "u_cs": 0.4},
    {"name": "m-1_u0.4", "m": -1, "u_cs": 0.4},
    {"name": "m+1_u0.8", "m": 1, "u_cs": 0.8},
    {"name": "m-1_u0.8", "m": -1, "u_cs": 0.8},
    {"name": "m0_u0.8", "m": 0, "u_cs": 0.8},
    {"name": "m+1_ruhe", "m": 1, "u_cs": 0.0},
    {"name": "m+1_u0.8_lam0", "m": 1, "u_cs": 0.8, "lam": 0.0},
    {"name": "medium_allein_u0.8", "m": None, "u_cs": 0.8},
)
MG_FEIN = ("m+1_u0.8", "m-1_u0.8", "m0_u0.8")

# ---- kielwasser (Wellen 4): gehaltener Ball, Medium stroemt (Ruhesystem des Balls) ----
KW_W2, KW_X0, KW_HALT = 0.60, -12.0, 2e-3
KW_RAMPE, KW_T, KW_MITTEL = 80.0, 280.0, 60.0
KW_RING = (10.0, 24.0)
KW_LAEUFE = (
    {"name": "u0.5", "m": 0, "u_cs": 0.5},
    {"name": "u1.3", "m": 0, "u_cs": 1.3},
    {"name": "u1.8", "m": 0, "u_cs": 1.8},
    {"name": "u2.5", "m": 0, "u_cs": 2.5},
    {"name": "u1.8_lam0", "m": 0, "u_cs": 1.8, "lam": 0.0},
    {"name": "medium_allein_u1.8", "m": None, "u_cs": 1.8},
)
KW_FEIN = ("u1.3", "u1.8", "u2.5")

# ---- wirbel (Wellen 18): grosser gehaltener Ball in schneller Unterschall-Stroemung ----
WB_W2, WB_X0, WB_Y0, WB_HALT = 0.55, -14.0, 0.05, 5e-4
WB_RAMPE, WB_T = 100.0, 700.0
WB_LAEUFE = tuple({"name": f"u{u}", "m": 0, "u_cs": u} for u in (0.4, 0.55, 0.7, 0.85, 1.0)) + (
    {"name": "u0.85_lam0", "m": 0, "u_cs": 0.85, "lam": 0.0},)
WB_FEIN = ("u0.7", "u0.85")

# ---- brechung (Wellen 14): Dichtestufe C0 -> C0 + dC bei x = 0 (periodisch: zweite Stufe bei x = +-L) ----
BR_W2, BR_V1, BR_X0 = 0.70, 0.12, -16.0
BR_BREITE, BR_XFIT = 2.0, 9.0
BR_RAMPE, BR_T = 60.0, 420.0
BR_LAEUFE = (
    {"name": "abst20", "dC": 0.04, "th": 20.0},
    {"name": "abst40", "dC": 0.04, "th": 40.0},
    {"name": "abst50", "dC": 0.06, "th": 50.0},
    {"name": "anz20", "dC": -0.04, "th": 20.0},
    {"name": "anz40", "dC": -0.04, "th": 40.0},
    {"name": "senkrecht", "dC": 0.04, "th": 0.0},
    {"name": "ohne40", "dC": 0.0, "th": 40.0},
    {"name": "lam0_40", "dC": 0.04, "th": 40.0, "lam": 0.0},
)
BR_FEIN = ("abst20", "abst40", "anz40")

SPALTEN = ["X", "Y", "Q_psi", "Q_chi", "F_x", "F_y", "S_max", "C_min_ball", "C_fern", "wind_psi", "zirk_chi",
           "N_plus", "N_minus", "N_plus_oben", "N_minus_oben", "N_plus_unten", "N_minus_unten", "N_alle",
           "C_spanne", "c2", "rampe"]
SP = {n: i for i, n in enumerate(SPALTEN)}
_PROFILE = {}


# ================================================================ Allgemeines

def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def geraet_name():
    return torch.cuda.get_device_name(0) if DEV.type == "cuda" else "CPU (1 Thread)"


def upot(s):
    return s - s * s + 0.5 * s ** 3


def schall(c):
    """Schallgeschwindigkeit des ruhenden Mediums der Dichte c (r5d.py 1.3): c_s^2 = g/(2 w0^2 + g), g = 2 g4 c."""
    g = 2.0 * G4 * c
    return math.sqrt(g / (2.0 * (1.0 + g) + g))


def heilungslaenge(c):
    """xi = 1/(sqrt(2) w0 c_s) (nichtrelativistische Naeherung, nur zur Einordnung)."""
    return 1.0 / (math.sqrt(2.0) * math.sqrt(1.0 + 2.0 * G4 * c) * schall(c))


def stroemung(u_cs):
    """Endzustand des gleichfoermig beschleunigten Mediums fuer u = u_cs * c_s(C_f).
    Ladungsdichte 2 C w bleibt erhalten (C_f w_f = C0 w0); stationaer w_f^2 (1 - u^2) = 1 + 2 g4 C_f; q = u w_f."""
    w0 = math.sqrt(1.0 + 2.0 * G4 * C0)
    cf, u, wf = C0, 0.0, w0
    for _ in range(300):
        u = u_cs * schall(cf)
        wf = math.sqrt((1.0 + 2.0 * G4 * cf) / (1.0 - u * u))
        cf = C0 * w0 / wf
    return {"u": u, "q": u * wf, "w_f": wf, "C_f": cf, "c_s_f": schall(cf), "gamma": 1.0 / math.sqrt(1.0 - u * u),
            "u_cs": u_cs}


def rampe(t, T):
    if T <= 0.0 or t >= T:
        return 1.0
    if t <= 0.0:
        return 0.0
    return math.sin(0.5 * PI * t / T) ** 2


def polyfit(t, y, grad):
    """y = sum c_k tau^k, tau = (t - t0)/Spanne; Rueckgabe (c, Standardfehler, Rest-RMS, Spanne) oder None."""
    if t.shape[0] < grad + 3:
        return None
    spanne = (t[-1] - t[0]).item()
    if spanne <= 0.0:
        return None
    tau = (t - t[0]) / spanne
    a = torch.stack([tau ** k for k in range(grad + 1)], dim=1)
    c = torch.linalg.lstsq(a, y.unsqueeze(1)).solution.squeeze(1)
    rest = y - a @ c
    s2 = (rest ** 2).sum() / max(a.shape[0] - a.shape[1], 1)
    se = torch.sqrt(torch.diagonal(torch.linalg.inv(a.T @ a)) * s2)
    return c, se, torch.sqrt((rest ** 2).mean()).item(), spanne


def geschw(t, y):
    f = polyfit(t, y, 1)
    return float("nan") if f is None else (f[0][1] / f[3]).item()


def beschl(t, y):
    f = polyfit(t, y, 2)
    return float("nan") if f is None else (2.0 * f[0][2] / f[3] ** 2).item()


def periodogramm(t, y, om_lo, om_hi, n=1500):
    """Kleinste Quadrate y = a + b tau + c cos(om t) + d sin(om t); bestes om, Amplitude, R2."""
    if t.shape[0] < 12 or om_hi <= om_lo:
        return None
    tau = (t - t[0]) / max((t[-1] - t[0]).item(), 1e-12)
    var = ((y - y.mean()) ** 2).sum().item()
    if var <= 0.0:
        return None
    oms = torch.linspace(om_lo, om_hi, n, dtype=F64, device=t.device)
    arg = oms.view(-1, 1) * t.view(1, -1)
    a = torch.stack([torch.ones_like(arg), tau.expand_as(arg), torch.cos(arg), torch.sin(arg)], dim=2)
    ata = torch.einsum("nmi,nmj->nij", a, a)
    atb = torch.einsum("nmi,m->ni", a, y).unsqueeze(2)
    koef = torch.linalg.solve(ata + 1e-12 * torch.eye(4, dtype=F64, device=t.device), atb)
    res = (((a @ koef).squeeze(2) - y.view(1, -1)) ** 2).sum(1)
    i = int(torch.argmin(res))
    return {"omega": oms[i].item(), "periode": 2.0 * PI / oms[i].item(),
            "amplitude": torch.sqrt(koef[i, 2, 0] ** 2 + koef[i, 3, 0] ** 2).item(), "R2": 1.0 - res[i].item() / var}


def fz(v, fmt=".4f"):
    return "-" if v is None or (isinstance(v, float) and not math.isfinite(v)) else format(v, fmt)


# ================================================================ Profile durch Schiessen (CPU)

def rhs(r, f, fp, a0, m2):
    s = f * f
    return fp, (a0 - 2.0 * s + 1.5 * s * s) * f - fp / r + m2 * f / (r * r)


def rk4(r, f, fp, a0, m2, h):
    k1f, k1p = rhs(r, f, fp, a0, m2)
    k2f, k2p = rhs(r + 0.5 * h, f + 0.5 * h * k1f, fp + 0.5 * h * k1p, a0, m2)
    k3f, k3p = rhs(r + 0.5 * h, f + 0.5 * h * k2f, fp + 0.5 * h * k2p, a0, m2)
    k4f, k4p = rhs(r + h, f + h * k3f, fp + h * k3p, a0, m2)
    return (f + (h / 6.0) * (k1f + 2.0 * k2f + 2.0 * k3f + k4f),
            fp + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p))


def startwerte(p, a0, mm, h):
    """Wie r5_2d_a.py: m = 0: f = p + g r^2/4; |m| >= 1: f = p r^m (1 + a0 r^2/(4 (m + 1)))."""
    s = p * p
    g = (a0 - 2.0 * s + 1.5 * s * s) * p
    ist_m0 = mm == 0.0
    m1 = mm.clamp(min=1.0)
    k2 = a0 / (4.0 * (m1 + 1.0))
    hm = torch.pow(torch.full_like(m1, h), m1)
    f = torch.where(ist_m0, p + 0.25 * g * h * h, p * hm * (1.0 + k2 * h * h))
    fp = torch.where(ist_m0, 0.5 * g * h, p * (hm / h) * (m1 + (m1 + 2.0) * k2 * h * h))
    return f, fp


def schiessen(w2_liste, m_liste, n_kand, runden):
    """Coleman-Regel fuer alle m (berichtigt in r5_2d_a.py): Ueberschuss f > f_top oder f < 0; Unterschuss f' > 0
    unterhalb der Talsohle, nachdem die Bahn einmal gefallen ist. Fuer |m| >= 1 wird ln p eingeschachtelt."""
    w2 = torch.tensor(w2_liste, dtype=F64).unsqueeze(1)
    mm = torch.tensor([float(abs(m)) for m in m_liste], dtype=F64).unsqueeze(1)
    m2 = mm * mm
    ist_m0 = mm == 0.0
    a0 = 1.0 - w2
    f_top = torch.sqrt((2.0 + torch.sqrt(6.0 * w2 - 2.0)) / 3.0)
    f_tal = torch.sqrt((2.0 - torch.sqrt(6.0 * w2 - 2.0)) / 3.0)
    lo = torch.where(ist_m0, torch.full_like(w2, 1e-3), torch.full_like(w2, math.log(1e-6)))
    hi = torch.where(ist_m0, f_top, torch.full_like(w2, math.log(10.0)))
    stufen = torch.linspace(0.0, 1.0, n_kand, dtype=F64)
    n_schritte = int(round(X_ODE / H_ODE))
    for _ in range(runden):
        par = lo + (hi - lo) * stufen
        p = torch.where(ist_m0, par, torch.exp(par))
        f, fp = startwerte(p, a0, mm, H_ODE)
        zustand = torch.zeros_like(p)
        gefallen = ist_m0.expand_as(p).clone()
        for s in range(n_schritte):
            f, fp = rk4(H_ODE * (s + 1), f, fp, a0, m2, H_ODE)
            offen = zustand == 0.0
            ueber = offen & ((f > f_top) | (f < 0.0))
            unter = offen & ~ueber & gefallen & (fp > 0.0) & (f < f_tal)
            gefallen = gefallen | (fp < 0.0)
            zustand = zustand + ueber.to(F64) - unter.to(F64)
            lebt = (zustand == 0.0).to(F64)
            f = f * lebt
            fp = fp * lebt
            if s % 250 == 249 and not bool((zustand == 0.0).any()):
                break
        lo = torch.where(zustand < 0.0, par, lo.expand_as(par)).max(dim=1, keepdim=True).values
        hi = torch.where(zustand > 0.0, par, hi.expand_as(par)).min(dim=1, keepdim=True).values
    mitte = 0.5 * (lo + hi)
    return {"p": torch.where(ist_m0, mitte, torch.exp(mitte)), "klammer": hi - lo, "w2": w2, "m2": m2, "mm": mm,
            "ist_m0": ist_m0, "a0": a0, "f_top": f_top, "m": list(m_liste), "w2_liste": list(w2_liste)}


def profile_bauen(sch, r_max):
    """Wie r5_2d_a.py: Schiessbahn mit p, Radialtabelle f, f' bis r_max (asymptotischer Schwanz), Radialintegrale."""
    p, a0, m2, mm, ist_m0, f_top = sch["p"], sch["a0"], sch["m2"], sch["mm"], sch["ist_m0"], sch["f_top"]
    n_schritte = int(round(X_ODE / H_ODE))
    f, fp = startwerte(p, a0, mm, H_ODE)
    f0 = torch.where(ist_m0, p, torch.zeros_like(p))
    fp0 = torch.where(mm == 1.0, p, torch.zeros_like(p))
    bahn_f, bahn_fp = [f0, f], [fp0, fp]
    fmax = torch.maximum(f0, f)
    faellt = fp < 0.0
    fertig = torch.zeros_like(faellt)
    fehler = torch.zeros_like(faellt)
    j_cut = torch.zeros(p.shape, dtype=torch.long)
    for s in range(n_schritte):
        f_neu, fp_neu = rk4(H_ODE * (s + 1), f, fp, a0, m2, H_ODE)
        weiter = ~fertig
        fehler = fehler | (weiter & ((f_neu < 0.0) | (f_neu > f_top) | (faellt & (fp_neu > 0.0))))
        faellt = faellt | (weiter & (fp_neu < 0.0))
        fmax = torch.where(weiter, torch.maximum(fmax, f_neu), fmax)
        f = torch.where(weiter, f_neu, f)
        fp = torch.where(weiter, fp_neu, fp)
        neu = weiter & faellt & (f < SCHWANZ * fmax)
        j_cut = torch.where(neu, torch.full_like(j_cut, s + 2), j_cut)
        fertig = fertig | neu
        bahn_f.append(f)
        bahn_fp.append(fp)
        if s % 250 == 249 and bool(fertig.all()):
            break
    gueltig = (~fehler & fertig).squeeze(1)
    bf = torch.cat(bahn_f, dim=1)
    bfp = torch.cat(bahn_fp, dim=1)
    n_z = p.shape[0]
    J = int(math.ceil(r_max / H_ODE)) + 2
    j = torch.arange(J).unsqueeze(0).expand(n_z, J)
    r = j.to(F64) * H_ODE
    innen_f = bf.gather(1, j.clamp(max=bf.shape[1] - 1))
    innen_fp = bfp.gather(1, j.clamp(max=bfp.shape[1] - 1))
    f_cut = bf.gather(1, j_cut)
    r_cut = j_cut.to(F64) * H_ODE
    kappa0 = torch.sqrt(a0)
    c1 = (4.0 * m2 - 1.0) / (8.0 * kappa0)
    rs = r.clamp(min=1.0)
    verh = torch.exp(-kappa0 * (rs - r_cut)) * torch.sqrt(r_cut / rs) * (1.0 + c1 / rs) / (1.0 + c1 / r_cut)
    aussen_f = f_cut * verh
    aussen_fp = aussen_f * (-kappa0 - 0.5 / rs - c1 / (rs * rs + c1 * rs))
    tab_f = torch.where(j < j_cut, innen_f, aussen_f)
    tab_fp = torch.where(j < j_cut, innen_fp, aussen_fp)
    wr = 2.0 * PI * r * H_ODE
    s_tab = tab_f * tab_f
    zentr = torch.where(r > 0.0, m2 * s_tab / (r * r).clamp(min=1e-300), torch.zeros_like(r))
    n_int = (s_tab * wr).sum(1)
    g_int = ((tab_fp * tab_fp + zentr) * wr).sum(1)
    v_int = (upot(s_tab) * wr).sum(1)
    w2 = sch["w2"].squeeze(1)
    s_max, j_max = s_tab.max(dim=1)
    unter_halb = (j > j_max.unsqueeze(1)) & (s_tab < 0.5 * s_max.unsqueeze(1))
    j_h = unter_halb.to(torch.int64).argmax(dim=1)
    s1 = s_tab.gather(1, j_h.unsqueeze(1)).squeeze(1)
    s0 = s_tab.gather(1, (j_h - 1).clamp(min=0).unsqueeze(1)).squeeze(1)
    r_halb = ((j_h - 1).to(F64) + (s0 - 0.5 * s_max) / (s0 - s1)) * H_ODE
    aus = []
    for i in range(n_z):
        aus.append({
            "omega2": sch["w2_liste"][i], "m": sch["m"][i], "p": p[i, 0].item(), "klammer": sch["klammer"][i, 0].item(),
            "f": tab_f[i], "fp": tab_fp[i], "N": n_int[i].item(), "G": g_int[i].item(), "VU": v_int[i].item(),
            "Q": (2.0 * math.sqrt(w2[i].item()) * n_int[i]).item(),
            "E": (w2[i] * n_int[i] + g_int[i] + v_int[i]).item(),
            "virialrest": ((v_int[i] - w2[i] * n_int[i]) / (v_int[i] + w2[i] * n_int[i])).item(),
            "S_max": s_max[i].item(), "R_max": j_max[i].item() * H_ODE, "R_halb": r_halb[i].item(),
            "gueltig": bool(gueltig[i])})
    return aus


def profil_info(pr):
    return {k: v for k, v in pr.items() if k not in ("f", "fp")}


def profile_holen(liste, mini):
    """Profile (omega2, |m|) aus dem Zwischenspeicher, fehlende in einem Schiessdurchgang auf der CPU."""
    fehlt = [k for k in dict.fromkeys(liste) if k not in _PROFILE]
    if fehlt:
        n_kand, runden = KAND["mini" if mini else "normal"]
        t0 = time.perf_counter()
        sch = schiessen([w2 for w2, _ in fehlt], [m for _, m in fehlt], n_kand, runden)
        for k, pr in zip(fehlt, profile_bauen(sch, R_TAB)):
            if not pr["gueltig"]:
                raise RuntimeError(f"Profil {k} ungueltig (Schiessbahn verlaesst den Separatrixweg)")
            pr["f_dev"], pr["fp_dev"] = pr["f"].to(DEV), pr["fp"].to(DEV)
            _PROFILE[k] = pr
        print(f"Schiessen {fehlt}: {time.perf_counter() - t0:.1f} s (CPU)", flush=True)
    return {k: _PROFILE[k] for k in liste}


def hermite(pr, r):
    tf, tfp = pr["f_dev"], pr["fp_dev"]
    u = r / H_ODE
    j = u.floor().clamp(0, tf.shape[0] - 2)
    t = (u - j).clamp(0.0, 1.0)
    j = j.long()
    f0, f1 = tf[j], tf[j + 1]
    d0, d1 = tfp[j] * H_ODE, tfp[j + 1] * H_ODE
    t2 = t * t
    t3 = t2 * t
    return (2 * t3 - 3 * t2 + 1) * f0 + (t3 - 2 * t2 + t) * d0 + (-2 * t3 + 3 * t2) * f1 + (t3 - t2) * d1


def ball_feld(g, pr, m, x0, y0):
    """psi = f(r) e^{i m theta} bei (x0, y0), glatt im Zentrum (f/r^|m| -> p); Form (ny, nx)."""
    X = g.x[0] - x0
    Y = g.y[0] - y0
    r = torch.sqrt(X * X + Y * Y)
    f = hermite(pr, r)
    if m == 0:
        return f.to(C128)
    am, sg = abs(m), (1.0 if m > 0 else -1.0)
    f_r = torch.where(r > 0.0, f / r.clamp(min=1e-300) ** am, torch.full_like(r, pr["p"]))
    return f_r * (X + 1j * sg * Y) ** am


# ================================================================ Gitter, Aufbau, Relaxation, Zeitentwicklung

class Gitter:
    """Periodische Box [-L, L)^2 (spiegelsymmetrisch: y -> -y bildet das Gitter auf sich ab), Randschicht SPONGE."""

    def __init__(self, L, dx):
        n = int(round(2.0 * L / dx))
        self.L, self.dx, self.n = L, dx, n
        x = -L + dx * torch.arange(n, dtype=F64, device=DEV)
        self.x = x.view(1, 1, n)
        self.y = x.view(1, n, 1)
        k = 2.0 * PI * torch.fft.fftfreq(n, d=dx, dtype=F64, device=DEV)
        self.kx = k.view(1, 1, n)
        self.ky = k.view(1, n, 1)
        self.k2 = self.kx ** 2 + self.ky ** 2
        tiefe = torch.maximum((self.x.abs() - (L - SPONGE)).clamp(min=0.0), (self.y.abs() - (L - SPONGE)).clamp(min=0.0))
        self.sigma = SIGMA0 * (tiefe / SPONGE) ** 2
        self.schwamm = self.sigma > 0.0
        self.innen = ~self.schwamm
        self.dA = dx * dx

    def minbild(self, d):
        return torch.remainder(d + self.L, 2.0 * self.L) - self.L


def stufenprofil(g):
    """Glatte, periodische Stufe: 0 fuer x < 0, 1 fuer 0 < x < L; Uebergaenge der Breite BR_BREITE bei x = 0 und
    x = +-L (dort in der Randschicht). (L/pi) sin(pi x/L) ist nahe x = 0 gleich x."""
    return 0.5 * (1.0 + torch.tanh((g.L / PI) * torch.sin(PI * g.x / g.L) / BR_BREITE))


class Aufbau:
    """Ein Stapel von Laeufen. spec je Lauf: name, m (None = ohne Ball), w2, x0, y0, lam, q (Stroemung), push (Bx, By),
    halt (Staerke des Halters), dC (Dichtestufe), W_konst (gleichfoermiges W fuer Massenrelaxation)."""

    def __init__(self, g, specs, prof):
        self.g, self.specs = g, specs
        B, n = len(specs), g.n
        self.B = B
        self.psi = torch.zeros((B, n, n), dtype=C128, device=DEV)
        self.W = torch.zeros((B, n, n), dtype=F64, device=DEV)
        self.Vh = torch.zeros((B, n, n), dtype=F64, device=DEV)
        spalte = lambda werte: torch.tensor(werte, dtype=F64, device=DEV).view(B, 1, 1)
        self.lam = spalte([s.get("lam", LAM) for s in specs])
        self.q = spalte([s.get("q", 0.0) for s in specs])
        self.bx = spalte([s.get("push", (0.0, 0.0))[0] for s in specs])
        self.by = spalte([s.get("push", (0.0, 0.0))[1] for s in specs])
        self.ball = torch.tensor([s["m"] is not None for s in specs], device=DEV)
        self.Qz = torch.tensor([prof[(s["w2"], abs(s["m"]))]["Q"] if s["m"] is not None else 0.0 for s in specs],
                               dtype=F64, device=DEV)
        stufe = stufenprofil(g) if any(s.get("dC") for s in specs) else None
        for b, s in enumerate(specs):
            if s["m"] is not None:
                self.psi[b] = ball_feld(g, prof[(s["w2"], abs(s["m"]))], s["m"], s["x0"], s["y0"])
            if s.get("halt"):
                rh2 = g.minbild(g.x[0] - s["x0"]) ** 2 + g.minbild(g.y[0] - s["y0"]) ** 2
                self.Vh[b] = s["halt"] * HALT_R ** 2 * torch.tanh(rh2 / HALT_R ** 2)
            if s.get("dC"):
                self.W[b] = (-2.0 * G4 * s["dC"]) * stufe[0].expand(n, n)
            if s.get("W_konst"):
                self.W[b] = s["W_konst"]
        self.w2c = 1.0 + 2.0 * G4 * C0                   # chemisches Potential des Mediums (Fernfeld C0 bei W = 0)
        S = self.psi.real ** 2 + self.psi.imag ** 2
        c_tf = (C0 - (self.W + self.lam * S) / (2.0 * G4)).clamp(min=1e-3)
        self.chi = torch.sqrt(c_tf).to(C128)
        self.om2 = torch.zeros(B, dtype=F64, device=DEV)
        self.res = (float("nan"), float("nan"))
        self.n_relax = 0
        x0 = torch.tensor([s.get("x0", 0.0) for s in specs], dtype=F64, device=DEV).view(B, 1, 1)
        y0 = torch.tensor([s.get("y0", 0.0) for s in specs], dtype=F64, device=DEV).view(B, 1, 1)
        self.z0 = g.minbild(g.x - x0) + 1j * g.minbild(g.y - y0)
        self.c2_relax = []

    def c2(self):
        """Quadrupolanteil |Sum S z^2| / Sum S |z|^2 je Ball um den Startort (Teilungsmode l = 2)."""
        S = self.psi.real ** 2 + self.psi.imag ** 2
        return ((S * self.z0 * self.z0).sum((1, 2)).abs() / (S * self.z0.abs() ** 2).sum((1, 2)).clamp(min=1e-300))

    # ---------------------------------------------------------- Relaxation (Gradientenfluss)
    def potentiale(self, S, C):
        pp = 1.0 + S * (1.5 * S - 2.0) + self.lam * C + self.Vh
        pc = 1.0 + 2.0 * G4 * C + self.lam * S + self.W
        return pp, pc

    def residuum(self):
        g = self.g
        S = self.psi.real ** 2 + self.psi.imag ** 2
        C = self.chi.real ** 2 + self.chi.imag ** 2
        pp, pc = self.potentiale(S, C)
        om2 = self.om2.view(-1, 1, 1)
        rp = torch.fft.ifft2(torch.fft.fft2(self.psi) * (-g.k2)) - (pp - om2) * self.psi
        rc = torch.fft.ifft2(torch.fft.fft2(self.chi) * (-g.k2)) - (pc - self.w2c) * self.chi
        norm_p = (om2 * self.psi).abs().pow(2).sum((1, 2)).sqrt().clamp(min=1e-300)
        norm_c = (self.w2c * self.chi).abs().pow(2).sum((1, 2)).sqrt()
        r_p = torch.where(self.ball, rp.abs().pow(2).sum((1, 2)).sqrt() / norm_p, torch.zeros_like(norm_p))
        r_c = rc.abs().pow(2).sum((1, 2)).sqrt() / norm_c
        return r_p.max().item(), r_c.max().item()

    def relaxieren(self, n_max):
        g = self.g
        nenner = 1.0 / (1.0 + DTAU * g.k2)
        for it in range(n_max):
            S = self.psi.real ** 2 + self.psi.imag ** 2
            C = self.chi.real ** 2 + self.chi.imag ** 2
            N = S.sum((1, 2)) * g.dA
            self.om2 = torch.where(self.ball, (self.Qz / (2.0 * N.clamp(min=1e-300))) ** 2, torch.zeros_like(N))
            pp, pc = self.potentiale(S, C)
            self.psi = torch.fft.ifft2(torch.fft.fft2(self.psi - DTAU * (pp - self.om2.view(-1, 1, 1)) * self.psi) * nenner)
            self.chi = torch.fft.ifft2(torch.fft.fft2(self.chi - DTAU * (pc - self.w2c) * self.chi) * nenner)
            self.n_relax = it + 1
            if it % 100 == 99 or it == n_max - 1:
                S = self.psi.real ** 2 + self.psi.imag ** 2
                self.om2 = torch.where(self.ball, (self.Qz / (2.0 * (S.sum((1, 2)) * g.dA).clamp(min=1e-300))) ** 2,
                                       torch.zeros_like(N))
                self.res = self.residuum()
                c2 = self.c2()
                self.c2_relax.append(round(c2.max().item(), 12))
                if bool((c2 > 1e-2).any()):
                    print(f"WARNUNG Relaxation: Quadrupol c2 = {c2.max().item():.2e} > 1e-2 nach {it + 1} Schritten "
                          "(Teilungsmode waechst?); Relaxation hier beendet.", flush=True)
                    break
                if max(self.res) < RELAX_ZIEL:
                    break
        if not bool(torch.isfinite(self.psi).all() and torch.isfinite(self.chi).all()):
            raise RuntimeError("Relaxation divergiert")

    def freie_energie(self):
        """F = E - w Q_chi der stationaeren Felder (Ball bei fester Ladung, Medium bei festem w); fuer M_eff."""
        g = self.g
        S = self.psi.real ** 2 + self.psi.imag ** 2
        C = self.chi.real ** 2 + self.chi.imag ** 2
        grad2 = torch.zeros_like(S)
        for feld in (self.psi, self.chi):
            fh = torch.fft.fft2(feld)
            for k in (g.kx, g.ky):
                d = torch.fft.ifft2(fh * (1j * k))
                grad2 = grad2 + d.real ** 2 + d.imag ** 2
        dichte = (self.om2.view(-1, 1, 1) * S + upot(S) + self.Vh * S + grad2 + (1.0 - self.w2c) * C + G4 * C * C
                  + self.W * C + self.lam * S * C)
        return (dichte.sum((1, 2)) * g.dA).tolist()

    # ---------------------------------------------------------- Zeitentwicklung
    def entwickeln(self, dt, t_end, t_rampe, r_win, r_psi, r_chi, snap_zeiten=(), mittel_ab=None):
        g, B = self.g, self.B
        psi, chi = self.psi.clone(), self.chi.clone()
        th_p = torch.arccos((1.0 - 0.5 * dt * dt * self.om2).clamp(-1.0, 1.0))
        th_c = math.acos(1.0 - 0.5 * dt * dt * self.w2c)
        vpsi = (-1j) * (torch.sin(th_p) / dt).view(-1, 1, 1) * psi
        vchi = (-1j) * (math.sin(th_c) / dt) * chi
        daempf = torch.exp(-g.sigma * dt)
        schw = g.schwamm.to(F64)
        n_schw = schw.sum().clamp(min=1.0)
        stroemt = bool((self.q != 0.0).any())
        schiebt = bool((self.bx != 0.0).any() or (self.by != 0.0).any())
        cache = {}

        def multiplikatoren(r):
            if "fest" in cache and (r >= 1.0 or not (stroemt or schiebt)):
                return cache["fest"]
            mp = -((g.kx - self.bx * r) ** 2 + (g.ky - self.by * r) ** 2) if schiebt else -g.k2
            mc = -((g.kx + self.q * r) ** 2 + g.ky ** 2) if stroemt else -g.k2
            if r >= 1.0 or not (stroemt or schiebt):
                cache["fest"] = (mp, mc)
            return mp, mc

        def kraft(p, c, r):
            mp, mc = multiplikatoren(r)
            S = p.real ** 2 + p.imag ** 2
            C = c.real ** 2 + c.imag ** 2
            pp, pc = self.potentiale(S, C)
            return (torch.fft.ifft2(torch.fft.fft2(p) * mp) - pp * p,
                    torch.fft.ifft2(torch.fft.fft2(c) * mc) - pc * c)

        zx = torch.tensor([s.get("x0", 0.0) for s in self.specs], dtype=F64, device=DEV)
        zy = torch.tensor([s.get("y0", 0.0) for s in self.specs], dtype=F64, device=DEV)
        rw = torch.full((B,), r_win, dtype=F64, device=DEV)

        def messen(p, vp, c, vc, r):
            nonlocal zx, zy
            S = p.real ** 2 + p.imag ** 2
            C = c.real ** 2 + c.imag ** 2
            dxm = g.minbild(g.x - zx.view(-1, 1, 1))
            dym = g.minbild(g.y - zy.view(-1, 1, 1))
            rr2 = dxm ** 2 + dym ** 2
            fen = (rr2 < rw.view(-1, 1, 1) ** 2).to(F64)
            w = S * S * fen
            ws = w.sum((1, 2))
            da = self.ball & (ws > 1e-200)
            X = torch.where(da, zx + (w * dxm).sum((1, 2)) / ws.clamp(min=1e-300), zx)
            Y = torch.where(da, zy + (w * dym).sum((1, 2)) / ws.clamp(min=1e-300), zy)
            zx, zy = X, Y
            dxm = g.minbild(g.x - X.view(-1, 1, 1))
            dym = g.minbild(g.y - Y.view(-1, 1, 1))
            rr2 = dxm ** 2 + dym ** 2
            fen = (rr2 < rw.view(-1, 1, 1) ** 2).to(F64)
            ch = torch.fft.fft2(C.to(C128))
            gcx = torch.fft.ifft2(ch * (1j * g.kx)).real
            gcy = torch.fft.ifft2(ch * (1j * g.ky)).real
            fx = -(self.lam * S * gcx).sum((1, 2)) * g.dA
            fy = -(self.lam * S * gcy).sum((1, 2)) * g.dA
            qp = 2.0 * (p * vp.conj()).imag.sum((1, 2)) * g.dA
            qc = 2.0 * (c * vc.conj()).imag.sum((1, 2)) * g.dA
            aussen = (rr2 > (r_chi + 4.0) ** 2) & g.innen
            c_fern = (C * aussen).sum((1, 2)) / aussen.to(F64).sum((1, 2)).clamp(min=1.0)
            c_min = torch.where(fen > 0.0, C, torch.full_like(C, 1e300)).amin((1, 2))
            s_max = (S * fen).amax((1, 2))
            wp, _ = windung(g, p, X, Y, r_psi)
            wc, _ = windung(g, c, X, Y, r_chi)
            nk = wirbelkarte(c)
            frei = (((dxm + 0.5 * g.dx) ** 2 + (dym + 0.5 * g.dx) ** 2) > r_chi ** 2) & g.innen
            oben = dym + 0.5 * g.dx > 0.0
            n_p = ((nk > 0.5) & frei)
            n_m = ((nk < -0.5) & frei)
            zaehl = lambda m: m.to(F64).sum((1, 2))
            n_alle = zaehl((nk.abs() > 0.5) & g.innen)
            ci = torch.where(g.innen, C, torch.full_like(C, float("nan")))
            spanne = torch.nan_to_num(ci, nan=-1e300).amax((1, 2)) - torch.nan_to_num(ci, nan=1e300).amin((1, 2))
            z = dxm + 1j * dym
            wsf = S * fen
            c2 = (wsf * z * z).sum((1, 2)).abs() / (wsf * (dxm ** 2 + dym ** 2)).sum((1, 2)).clamp(min=1e-300)
            return torch.stack([X, Y, qp, qc, fx, fy, s_max, c_min, c_fern, wp, wc, zaehl(n_p), zaehl(n_m),
                                zaehl(n_p & oben), zaehl(n_m & oben), zaehl(n_p & ~oben), zaehl(n_m & ~oben), n_alle,
                                spanne, c2, torch.full_like(X, r)], dim=1)

        n_schritte = int(round(t_end / dt))
        alle = max(1, int(round(T_MESS / dt)))
        snap_idx = sorted({int(round(ts / dt)) for ts in snap_zeiten if 0 < ts <= t_end})
        snaps, snap_t, snap_wk = [], [], []
        mittel, n_mittel = None, 0
        i_mittel = int(round(mittel_ab / dt)) if mittel_ab is not None else None
        reihe = [messen(psi, vpsi, chi, vchi, 0.0)]
        ap, ac = kraft(psi, chi, 0.0)
        lam_c = torch.full((B, 1, 1), -1j * math.sqrt(self.w2c), dtype=C128, device=DEV)
        for n in range(1, n_schritte + 1):
            t = n * dt
            r = rampe(t, t_rampe)
            vpsi.add_(ap, alpha=0.5 * dt)
            vchi.add_(ac, alpha=0.5 * dt)
            psi.add_(vpsi, alpha=dt)
            chi.add_(vchi, alpha=dt)
            ap, ac = kraft(psi, chi, r)
            vpsi.add_(ap, alpha=0.5 * dt)
            vchi.add_(ac, alpha=0.5 * dt)
            vpsi.mul_(daempf)
            if True:                                     # jede Stufe: Referenz folgt auch dem Atmen (k = 0)
                # komplexe Rate lambda = Mittel von chi_t/chi ueber die Randschicht (Drehung und Dichteaenderung des
                # gleichfoermigen Mediums); gedaempft wird nur die Abweichung chi_t - lambda chi.
                C = (chi.real ** 2 + chi.imag ** 2).clamp(min=1e-30)
                rate = (vchi * chi.conj()) / C
                lam_c = ((rate * schw).sum((1, 2)) / n_schw).view(-1, 1, 1)
            rot = lam_c * chi
            vchi.sub_(rot).mul_(daempf).add_(rot)
            if n % alle == 0:
                reihe.append(messen(psi, vpsi, chi, vchi, r))
            if n in snap_idx:
                snaps.append((chi.real ** 2 + chi.imag ** 2).float().cpu())
                snap_wk.append(wirbelkarte(chi).to(torch.int8).cpu())
                snap_t.append(t)
            if i_mittel is not None and n >= i_mittel and n % alle == 0:
                C = chi.real ** 2 + chi.imag ** 2
                mittel = C.clone() if mittel is None else mittel + C
                n_mittel += 1
        daten = torch.stack(reihe)
        if not bool(torch.isfinite(daten[:, :, :SP["C_spanne"]]).all()):
            raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
        t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
        aus = {"t": t, "daten": daten, "snap_t": snap_t,
               "snaps": torch.stack(snaps) if snaps else None, "wirbelkarten": torch.stack(snap_wk) if snap_wk else None,
               "C_mittel": (mittel / max(n_mittel, 1)) if mittel is not None else None,
               "S_ende": (psi.real ** 2 + psi.imag ** 2).float().cpu(), "C_ende": (chi.real ** 2 + chi.imag ** 2).float().cpu()}
        return aus


def windung(g, feld, xc, yc, rc):
    """Phasenumlauf von feld (B, n, n) auf Kreisen (Radius rc um xc, yc), bilinear, gegen den Uhrzeigersinn.
    Rueckgabe Windungszahl (B,) und kleinstes |feld|^2 auf dem Kreis."""
    B = feld.shape[0]
    th = torch.arange(N_THETA, dtype=F64, device=DEV) * (2.0 * PI / N_THETA)
    fx = (xc.view(-1, 1) + rc * torch.cos(th).view(1, -1) + g.L) / g.dx
    fy = (yc.view(-1, 1) + rc * torch.sin(th).view(1, -1) + g.L) / g.dx
    j0f, i0f = torch.floor(fx), torch.floor(fy)
    tx, ty = fx - j0f, fy - i0f
    j0, i0 = j0f.long() % g.n, i0f.long() % g.n
    j1, i1 = (j0 + 1) % g.n, (i0 + 1) % g.n
    b = torch.arange(B, device=DEV).view(-1, 1)
    w = ((1.0 - tx) * (1.0 - ty) * feld[b, i0, j0] + tx * (1.0 - ty) * feld[b, i0, j1]
         + (1.0 - tx) * ty * feld[b, i1, j0] + tx * ty * feld[b, i1, j1])
    ph = torch.angle(w)
    d = torch.remainder(ph.roll(-1, dims=1) - ph + PI, 2.0 * PI) - PI
    return torch.round(d.sum(1) / (2.0 * PI)), (w.real ** 2 + w.imag ** 2).amin(1)


def wirbelkarte(chi):
    """Windung je Plakette (x, y) -> (x+dx, y) -> (x+dx, y+dx) -> (x, y+dx), gegen den Uhrzeigersinn positiv."""
    ph = torch.angle(chi)
    wr = lambda a: torch.remainder(a + PI, 2.0 * PI) - PI
    p01 = torch.roll(ph, -1, dims=2)
    p11 = torch.roll(p01, -1, dims=1)
    p10 = torch.roll(ph, -1, dims=1)
    return torch.round((wr(p01 - ph) + wr(p11 - p01) + wr(p10 - p11) + wr(ph - p10)) / (2.0 * PI))


# ================================================================ Rahmen je Karte

class Rahmen:
    def __init__(self, karte, args):
        self.karte, self.args = karte, args
        self.rauch, self.mini = args.rauch, args.mini
        self.faktor = (MINI_FAKTOR if self.mini else RAUCH_FAKTOR) if self.rauch else 1.0
        self.stufen = STUFEN_MINI if self.mini else STUFEN
        self.n_relax = max(40, int(N_RELAX * self.faktor)) if self.rauch else N_RELAX
        self.out = args.out
        self.dauer = {}
        self.start = jetzt()
        os.makedirs(self.out, exist_ok=True)
        print(f"{karte} Start {self.start} auf {geraet_name()}, torch {torch.__version__}"
              + (" RAUCHTEST: Zahlen ungueltig" if self.rauch else ""), flush=True)

    def stufen_liste(self):
        return ("grob", "fein") if self.args.stufe == "beide" else (self.args.stufe,)

    def roh_sichern(self, stufe, specs, lauf, extra):
        """Rohdaten sofort nach der Rechnung (vor der Auswertung) sichern."""
        name = os.path.join(self.out, f"{self.karte}_{stufe}_roh")
        torch.save({k: (v.cpu() if torch.is_tensor(v) else v) for k, v in lauf.items()} | {"specs": specs,
                   "spalten": SPALTEN, "extra": extra}, name + ".pt")
        d = lauf["daten"]
        kurz = {"karte": self.karte, "stufe": stufe, "zeit": jetzt(), "rauch": self.rauch, "extra": extra,
                "specs": specs, "spalten": SPALTEN, "erste_zeile": d[0].cpu().tolist(), "letzte_zeile": d[-1].cpu().tolist()}
        with open(name + ".json", "w") as fh:
            json.dump(kurz, fh, indent=1, default=str)

    def laufzeit_zeilen(self):
        zz = ["Dauer [s]: " + ", ".join(f"{k} {v:.1f}" for k, v in self.dauer.items())]
        if self.rauch:
            entw = sum(v for k, v in self.dauer.items() if k.startswith("entw"))
            rest = sum(v for k, v in self.dauer.items() if not k.startswith("entw"))
            fak = 1.0 / self.faktor
            zz.append(f"Hochrechnung Hauptlauf (nur --rauch ohne --mini gilt): {rest + entw * fak:.0f} s = nicht "
                      f"entwickelnde Teile {rest:.0f} s + Entwicklung x {fak:.0f}; Relaxation im Rauchtest gekuerzt. "
                      "Ueber 540 s je Aufruf: Stufen einzeln (--stufe grob / --stufe fein).")
        return zz

    def endung(self):
        return "" if self.args.stufe == "beide" or self.karte == "profile" else f"_{self.args.stufe}"

    def l3(self, ergebnis, groessen):
        """Latte L3: grob gegen fein je Lauf und Groesse; |fein - grob| <= max(0,2 |fein|, Toleranz).
        Fehlt grob in diesem Aufruf, wird <karte>_grob_ergebnis.json aus dem --out-Ordner gelesen."""
        grob = ergebnis.get("grob")
        if grob is None and "fein" in ergebnis:
            pfad = os.path.join(self.out, f"{self.karte}_grob_ergebnis.json")
            if os.path.exists(pfad):
                with open(pfad) as fh:
                    grob = json.load(fh).get("ergebnis", {}).get("grob")
        fein = ergebnis.get("fein")
        if not grob or not fein or "zeilen" not in grob or "zeilen" not in fein:
            return {"bestanden": None, "zeilen": []}, ["L3: grob oder fein fehlt, kein Vergleich"]
        gz = {z["name"]: z for z in grob["zeilen"]}
        aus, text, alle_ok = [], ["L3 (grob gegen fein; bestanden, wenn |fein - grob| <= max(0,2 |fein|, Toleranz)):"], True
        for z in fein["zeilen"]:
            g = gz.get(z["name"])
            if g is None:
                continue
            for k, tol in groessen:
                a, b = g.get(k), z.get(k)
                if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not (math.isfinite(a) and math.isfinite(b)):
                    continue
                ok = abs(b - a) <= max(0.2 * abs(b), tol)
                alle_ok = alle_ok and ok
                aus.append({"lauf": z["name"], "groesse": k, "grob": a, "fein": b, "ok": ok})
                text.append(f"  {z['name']} {k}: grob {a:.5g}, fein {b:.5g} -> {'ok' if ok else 'NICHT ok'}")
        text.append(f"  L3 gesamt: {'bestanden' if alle_ok else 'nicht bestanden'} ({sum(x['ok'] for x in aus)} von {len(aus)})")
        return {"bestanden": alle_ok, "zeilen": aus}, text

    def schreiben(self, ausgabe, text, l3=None):
        ausgabe.update({"karte": self.karte, "start": self.start, "ende": jetzt(), "rauch": self.rauch,
                        "mini": self.mini, "geraet": geraet_name(), "torch": torch.__version__, "dauer_s": self.dauer,
                        "medium": {"C0": C0, "g4": G4, "lam": LAM, "c_s": schall(C0), "xi": heilungslaenge(C0)}})
        if l3 is not None and "ergebnis" in ausgabe:
            l3_daten, l3_text = self.l3(ausgabe["ergebnis"], l3)
            ausgabe["L3"] = l3_daten
            text = text + l3_text
        kopf = [f"{self.karte}: Start {self.start}, Ende {ausgabe['ende']}, {geraet_name()}, torch {torch.__version__}"
                + (" RAUCHTEST: Zahlen ungueltig" if self.rauch else ""),
                f"Medium C0 = {C0}, g4 = {G4}, lam = {LAM}: c_s = {schall(C0):.4f}, Heilungslaenge etwa "
                f"{heilungslaenge(C0):.2f}"] + self.laufzeit_zeilen()
        text = "\n".join(kopf + text)
        with open(os.path.join(self.out, f"{self.karte}{self.endung()}_ergebnis.json"), "w") as fh:
            json.dump(ausgabe, fh, indent=1, default=str)
        with open(os.path.join(self.out, f"{self.karte}{self.endung()}_bericht.txt"), "w") as fh:
            fh.write(text + "\n")
        print(text, flush=True)

    def rechnen(self, stufe, specs, prof, t_end, t_rampe, r_win, r_psi, r_chi, mittel=None, extra=None):
        """Aufbau, Relaxation, Entwicklung einer Stufe; Rohdaten sichern. Rueckgabe (Aufbau, Lauf)."""
        dx, dt = self.stufen[stufe]
        g = Gitter(L_BOX, dx)
        auf = Aufbau(g, specs, prof)
        t0 = uhr()
        auf.relaxieren(self.n_relax)
        self.dauer[f"relax_{stufe}_s"] = uhr() - t0
        print(f"{self.karte} {stufe}: {auf.B} Laeufe, {g.n}^2 Punkte, Relaxation {auf.n_relax} Schritte, Residuen "
              f"psi {auf.res[0]:.1e}, chi {auf.res[1]:.1e}, {self.dauer[f'relax_{stufe}_s']:.1f} s", flush=True)
        T = t_end * self.faktor
        TR = t_rampe * self.faktor
        snaps = [T * (k + 1) / SNAP_ZAHL for k in range(SNAP_ZAHL)]
        t0 = uhr()
        lauf = auf.entwickeln(dt, T, TR, r_win, r_psi, r_chi, snaps, None if mittel is None else T - mittel * self.faktor)
        self.dauer[f"entw_{stufe}_s"] = uhr() - t0
        print(f"{self.karte} {stufe}: Entwicklung T = {T:g} ({int(round(T / dt))} Schritte) in "
              f"{self.dauer[f'entw_{stufe}_s']:.1f} s", flush=True)
        ex = {"dx": dx, "dt": dt, "n": g.n, "T": T, "T_rampe": TR, "relax_schritte": auf.n_relax,
              "residuen": list(auf.res), "omega2_im_medium": auf.om2.tolist(), "faktor": self.faktor,
              "c2_relax": auf.c2_relax} | (extra or {})
        self.roh_sichern(stufe, specs, lauf, ex)
        lauf["extra"] = ex
        lauf["gitter"] = g
        return auf, lauf


def spec_basis(s, w2, x0, y0):
    d = dict(s)
    d.setdefault("lam", LAM)
    d["w2"], d["x0"], d["y0"] = w2, x0, y0
    return d


def reihe(lauf, b, name):
    return lauf["daten"][:, b, SP[name]]


def nach_rampe(lauf, abstand=20.0):
    t = lauf["t"]
    return t >= lauf["extra"]["T_rampe"] + abstand * lauf["extra"]["faktor"]


# ================================================================ Karte magnus (Wellen 8/9)

def karte_magnus(rah):
    prof = profile_holen([(MG_W2, 0), (MG_W2, 1)], rah.mini)
    pr1, pr0 = prof[(MG_W2, 1)], prof[(MG_W2, 0)]
    r_psi = pr1["R_max"]
    r_chi = pr1["R_halb"] + 6.0
    r_win = pr1["R_halb"] + 8.0
    ergebnis = {}
    for stufe in rah.stufen_liste():
        auswahl = MG_LAEUFE if stufe == "grob" else tuple(s for s in MG_LAEUFE if s["name"] in MG_FEIN)
        specs = []
        for s in auswahl:
            d = spec_basis(s, MG_W2, MG_X0, 0.0)
            d.update(stroemung(s["u_cs"]))
            specs.append(d)
        auf, lauf = rah.rechnen(stufe, specs, prof, MG_T, MG_RAMPE, r_win, r_psi, r_chi)
        try:
            ergebnis[stufe] = auswertung_magnus(specs, lauf, prof)
        except Exception:
            ergebnis[stufe] = {"fehler": traceback.format_exc()}
            print(ergebnis[stufe]["fehler"], flush=True)
    text = bericht_magnus(ergebnis, prof)
    rah.schreiben({"profile": {str(k): profil_info(v) for k, v in prof.items()}, "ergebnis": ergebnis}, text,
                 l3=(("v_x", 1e-4), ("dY", 0.01), ("v_y", 1e-5)))


def auswertung_magnus(specs, lauf, prof):
    t = lauf["t"]
    w = nach_rampe(lauf)
    zeilen = []
    for b, s in enumerate(specs):
        z = {"name": s["name"], "m": s["m"], "u": s["u"], "u_cs": s["u_cs"], "lam": s["lam"]}
        if s["m"] is None:
            z["C_spanne_max"] = reihe(lauf, b, "C_spanne").max().item()
            z["Q_chi_halt"] = (reihe(lauf, b, "Q_chi")[-1] / reihe(lauf, b, "Q_chi")[0]).item()
            z["N_wirbel_max"] = reihe(lauf, b, "N_alle").max().item()
            zeilen.append(z)
            continue
        X, Y = reihe(lauf, b, "X"), reihe(lauf, b, "Y")
        i_r = int((t < lauf["extra"]["T_rampe"]).sum().item())
        pr = prof[(s["w2"], abs(s["m"]))]
        z.update({"Q": pr["Q"], "E_vak": pr["E"], "J_mQ": s["m"] * pr["Q"],
                  "dX": (X[-1] - X[0]).item(), "dY": (Y[-1] - Y[0]).item(),
                  "dY_nach_rampe": (Y[-1] - Y[min(i_r, len(Y) - 1)]).item(),
                  "Y_max_abs": Y.abs().max().item(), "v_x": geschw(t[w], X[w]), "v_y": geschw(t[w], Y[w]),
                  "a_x": beschl(t[w], X[w]), "a_y": beschl(t[w], Y[w]),
                  "F_x_mittel": reihe(lauf, b, "F_x")[w].mean().item(), "F_y_mittel": reihe(lauf, b, "F_y")[w].mean().item(),
                  "zirk_chi": sorted(set(reihe(lauf, b, "zirk_chi")[w].tolist())),
                  "wind_psi": sorted(set(reihe(lauf, b, "wind_psi").tolist())),
                  "c2_max": reihe(lauf, b, "c2").max().item(),
                  "N_frei_max": (reihe(lauf, b, "N_plus") + reihe(lauf, b, "N_minus")).max().item(),
                  "Q_psi_verlust": (1.0 - reihe(lauf, b, "Q_psi")[-1] / reihe(lauf, b, "Q_psi")[0]).item(),
                  "C_min_ball": reihe(lauf, b, "C_min_ball")[-1].item()})
        z["mitnahme_vx_zu_u"] = z["v_x"] / s["u"] if s["u"] > 0 else None
        z["dY_moeller"] = s["m"] * pr["Q"] * z["v_x"] / pr["E"] if math.isfinite(z["v_x"]) else float("nan")
        z["ball_heil"] = (z["wind_psi"] == [float(s["m"])]) and z["c2_max"] < 0.3
        # Kutta-Joukowski mit gequantelter Zirkulation n: F_y = -rho u Gamma = -4 pi w_f C_f u n (rho = 2 w^2 C)
        n_z = [n for n in z["zirk_chi"] if n != 0]
        z["F_y_KJ_je_n"] = -4.0 * PI * s["w_f"] * s["C_f"] * s["u"]
        z["zirkulation_null"] = not n_z
        zeilen.append(z)
    namen = {z["name"]: z for z in zeilen}
    kontrollen = {}
    for u in ("0.4", "0.8"):
        a, bb = namen.get(f"m+1_u{u}"), namen.get(f"m-1_u{u}")
        if a and bb:
            ia = [s["name"] for s in specs].index(a["name"])
            ib = [s["name"] for s in specs].index(bb["name"])
            kontrollen[f"K_spiegel_u{u}_max|Y+ + Y-|"] = (reihe(lauf, ia, "Y") + reihe(lauf, ib, "Y")).abs().max().item()
    if "m0_u0.8" in namen:
        kontrollen["K_m0_max|Y|"] = namen["m0_u0.8"]["Y_max_abs"]
    if "m+1_u0.8_lam0" in namen:
        zz = namen["m+1_u0.8_lam0"]
        kontrollen["K_lam0_|dX|,|Y|max"] = [abs(zz["dX"]), zz["Y_max_abs"]]
    if "medium_allein_u0.8" in namen:
        kontrollen["K_medium_allein_C_spanne_max"] = namen["medium_allein_u0.8"]["C_spanne_max"]
    # Urteil nach PLAN.md (vorab festgelegt)
    urteile = []
    for z in zeilen:
        if z["m"] in (1, -1) and z["u"] > 0 and z["lam"] > 0:
            if not z["ball_heil"]:
                urteile.append(f"{z['name']}: Ball nicht heil (Windung {z['wind_psi']}, c2 {z['c2_max']:.2f}); keine Aussage")
            elif z["zirkulation_null"]:
                rest = z["dY"] - z["dY_moeller"]
                if abs(rest) < 0.05 and abs(z["v_y"]) < 1e-4:
                    urteile.append(f"{z['name']}: keine Querdrift ohne Zirkulation (V-M1 getragen); dY {z['dY']:+.3e}, "
                                   f"Moeller m Q v_x/E {z['dY_moeller']:+.3e} (V-M2)")
                elif abs(rest) > 0.15 or abs(z["v_y"]) > 3e-4:
                    urteile.append(f"{z['name']}: Querdrift ohne Zirkulation (Befund-Kandidat gegen V-M1): dY - Moeller "
                                   f"{rest:+.3e}, v_y {z['v_y']:+.1e}")
                else:
                    urteile.append(f"{z['name']}: Zwischenbereich: dY - Moeller {rest:+.3e}, v_y {z['v_y']:+.1e}")
            else:
                vz = "passt" if z["F_y_mittel"] * z["F_y_KJ_je_n"] * sum(z["zirk_chi"]) > 0 else "passt nicht"
                urteile.append(f"{z['name']}: Zirkulation {z['zirk_chi']} gebunden; Vorzeichen F_y gegen KJ {vz}")
    return {"zeilen": zeilen, "kontrollen": kontrollen, "urteile": urteile}


def bericht_magnus(ergebnis, prof):
    pr1, pr0 = prof[(MG_W2, 1)], prof[(MG_W2, 0)]
    zz = [f"Karte magnus (Wellen 8/9). Ball omega^2 = {MG_W2}: m = 1 Q {pr1['Q']:.2f}, E {pr1['E']:.2f}, R_halb "
          f"{pr1['R_halb']:.2f}, R_max {pr1['R_max']:.2f}; m = 0 Q {pr0['Q']:.2f}, E {pr0['E']:.2f}, R_halb {pr0['R_halb']:.2f}.",
          "Lauf | u/c_s | u | dX | dY gesamt | Moeller m Q v_x/E | dY nach Rampe | v_x | v_x/u | v_y | a_y | F_y | "
          "Zirk. chi | Wind. psi | c2 max | N frei"]
    for stufe, e in ergebnis.items():
        zz.append(f"[{stufe}]")
        if "fehler" in e:
            zz.append("  Auswertung fehlgeschlagen:\n" + e["fehler"])
            continue
        for z in e["zeilen"]:
            if z["m"] is None:
                zz.append(f"  {z['name']} | {z['u_cs']} | {z['u']:.4f} | Medium allein: C-Spanne max {z['C_spanne_max']:.1e}, "
                          f"Q_chi Ende/Start {z['Q_chi_halt']:.6f}, Wirbel {z['N_wirbel_max']:.0f}")
                continue
            zz.append(f"  {z['name']} | {z['u_cs']} | {z['u']:.4f} | {z['dX']:+.3f} | {z['dY']:+.3e} | {z['dY_moeller']:+.3e} | "
                      f"{z['dY_nach_rampe']:+.2e} | "
                      f"{z['v_x']:+.2e} | {fz(z['mitnahme_vx_zu_u'], '.3f')} | {z['v_y']:+.1e} | {z['a_y']:+.1e} | "
                      f"{z['F_y_mittel']:+.1e} | {z['zirk_chi']} | {z['wind_psi']} | {z['c2_max']:.3f} | {z['N_frei_max']:.0f}")
        zz.append("  Kontrollen: " + json.dumps(e["kontrollen"]))
        zz += ["  Urteil: " + u for u in e["urteile"]]
    return zz


# ================================================================ Karte kielwasser (Wellen 4)

def mach_winkel(st):
    """Halbwinkel des Machkegels im Ruhesystem des Balls: tan a' = tan(arcsin(c_s/u))/gamma (Lorentz-Stauchung)."""
    if st["u"] <= st["c_s_f"]:
        return None
    a = math.asin(st["c_s_f"] / st["u"])
    return math.degrees(math.atan(math.tan(a) / st["gamma"])), math.degrees(a)


def karte_kielwasser(rah):
    prof = profile_holen([(KW_W2, 0)], rah.mini)
    pr = prof[(KW_W2, 0)]
    r_win, r_psi, r_chi = pr["R_halb"] + 8.0, pr["R_halb"], pr["R_halb"] + 6.0
    ergebnis = {}
    for stufe in rah.stufen_liste():
        auswahl = KW_LAEUFE if stufe == "grob" else tuple(s for s in KW_LAEUFE if s["name"] in KW_FEIN)
        specs = []
        for s in auswahl:
            d = spec_basis(s, KW_W2, KW_X0, 0.0)
            d.update(stroemung(s["u_cs"]))
            d["halt"] = KW_HALT
            specs.append(d)
        auf, lauf = rah.rechnen(stufe, specs, prof, KW_T, KW_RAMPE, r_win, r_psi, r_chi, mittel=KW_MITTEL)
        try:
            ergebnis[stufe] = auswertung_kielwasser(specs, lauf)
        except Exception:
            ergebnis[stufe] = {"fehler": traceback.format_exc()}
            print(ergebnis[stufe]["fehler"], flush=True)
    rah.schreiben({"profil": profil_info(pr), "ergebnis": ergebnis}, bericht_kielwasser(ergebnis, pr),
                 l3=(("winkel_mess", 2.0), ("amplitude", 1e-5), ("F_x_mittel", 1e-4)))


def winkelprofil(g, feld, xc, yc, r1, r2, phis):
    """Mittel von feld (n, n) ueber Strahlen r in [r1, r2] je Winkel phi (Grad), bilinear."""
    rs = torch.linspace(r1, r2, 29, dtype=F64, device=DEV)
    ph = torch.tensor(phis, dtype=F64, device=DEV) * (PI / 180.0)
    fx = (xc + rs.view(1, -1) * torch.cos(ph).view(-1, 1) + g.L) / g.dx
    fy = (yc + rs.view(1, -1) * torch.sin(ph).view(-1, 1) + g.L) / g.dx
    j0f, i0f = torch.floor(fx), torch.floor(fy)
    tx, ty = fx - j0f, fy - i0f
    j0, i0 = j0f.long() % g.n, i0f.long() % g.n
    j1, i1 = (j0 + 1) % g.n, (i0 + 1) % g.n
    w = ((1 - tx) * (1 - ty) * feld[i0, j0] + tx * (1 - ty) * feld[i0, j1] + (1 - tx) * ty * feld[i1, j0]
         + tx * ty * feld[i1, j1])
    return w.mean(1)


def auswertung_kielwasser(specs, lauf):
    g = lauf["gitter"]
    t = lauf["t"]
    T = lauf["extra"]["T"]
    spaet = t >= t[-1] - KW_MITTEL * lauf["extra"]["faktor"] + 1e-9
    zeilen = []
    phis = [float(p) for p in range(-89, 90)]
    for b, s in enumerate(specs):
        z = {"name": s["name"], "u_cs": s["u_cs"], "u": s["u"], "gamma": s["gamma"], "c_s_f": s["c_s_f"], "lam": s["lam"]}
        mw = mach_winkel(s)
        z["mach_vorhersage_ball"], z["mach_medium"] = (mw if mw else (None, None))
        cm = lauf["C_mittel"][b]
        cref = cm[g.innen[0]].median()
        dc = cm - cref
        if s["m"] is None:
            z["dC_max_abs"] = dc[g.innen[0]].abs().max().item()
            z["C_spanne_max"] = reihe(lauf, b, "C_spanne").max().item()
            zeilen.append(z)
            continue
        xb = reihe(lauf, b, "X")[spaet].mean().item()
        yb = reihe(lauf, b, "Y")[spaet].mean().item()
        prof_a = winkelprofil(g, dc, xb, yb, KW_RING[0], KW_RING[1], phis)                    # Mittel laengs Strahl
        prof_q = winkelprofil(g, dc * dc, xb, yb, KW_RING[0], KW_RING[1], phis).clamp(min=0.0).sqrt()   # RMS
        spitze = lambda lo, hi: max((prof_q[i].item(), phis[i]) for i in range(len(phis)) if lo <= phis[i] <= hi)
        ro, po = spitze(8.0, 87.0)                       # Hauptschaetzer (vorab): RMS-Spitze ausserhalb 8 Grad
        ru, pu = spitze(-87.0, -8.0)
        mx = max(ro, ru)

        def kante(vz):
            kand = [abs(phis[i]) for i in range(len(phis)) if 8.0 <= vz * phis[i] <= 87.0 and prof_q[i].item() >= 0.5 * mx]
            return max(kand) if kand else None
        vorlauf = winkelprofil(g, dc * dc, xb, yb, KW_RING[0], KW_RING[1], [float(p) for p in range(115, 246, 5)])
        ko, ku = kante(1.0), kante(-1.0)
        z.update({"X_mittel": xb, "Y_mittel": yb, "winkel_oben": po, "winkel_unten": pu,
                  "winkel_mess": 0.5 * (po - pu), "amplitude": mx,
                  "kante_50": (0.5 * (ko + ku)) if (ko is not None and ku is not None) else None,
                  "rms_achse_0_8": max(prof_q[i].item() for i in range(len(phis)) if abs(phis[i]) < 8.0),
                  "profil_rms": [round(v, 8) for v in prof_q.tolist()],
                  "vorlauf_rms": math.sqrt(max(vorlauf.mean().item(), 0.0)),
                  "F_x_mittel": reihe(lauf, b, "F_x")[spaet].mean().item(),
                  "F_y_mittel": reihe(lauf, b, "F_y")[spaet].mean().item(),
                  "N_wirbel_max": reihe(lauf, b, "N_alle").max().item(),
                  "wind_psi": sorted(set(reihe(lauf, b, "wind_psi").tolist())),
                  "profil": [round(v, 7) for v in prof_a.tolist()]})
        if z["mach_vorhersage_ball"] is not None:
            z["abweichung_grad"] = z["winkel_mess"] - z["mach_vorhersage_ball"]
        zeilen.append(z)
    namen = {z["name"]: z for z in zeilen}
    urteile = []
    for z in zeilen:
        if z.get("abweichung_grad") is not None and z["lam"] > 0:
            ok = abs(z["abweichung_grad"]) <= 6.0
            urteile.append(f"{z['name']}: Winkel {z['winkel_mess']:.1f} gegen Mach (Ballsystem) "
                           f"{z['mach_vorhersage_ball']:.1f} Grad -> {'getragen' if ok else 'verfehlt'} (6 Grad); 50-%-Kante {fz(z.get('kante_50'), '.1f')}")
    if "u0.5" in namen and "u1.3" in namen and namen["u1.3"].get("amplitude"):
        q = namen["u0.5"]["amplitude"] / namen["u1.3"]["amplitude"]
        urteile.append(f"u0.5: Amplitude/Amplitude(u1.3) = {q:.3f} -> {'kein Kielwasser (V-K2)' if q < 0.1 else 'Muster auch unter c_s'}")
        fq = abs(namen["u0.5"]["F_x_mittel"]) / max(abs(namen["u1.3"]["F_x_mittel"]), 1e-300)
        urteile.append(f"u0.5: |F_x|/|F_x(u1.3)| = {fq:.3f} -> {'reibungsfrei (V-K3)' if fq < 0.1 else 'Widerstand unter c_s'}")
    return {"zeilen": zeilen, "urteile": urteile}


def bericht_kielwasser(ergebnis, pr):
    zz = [f"Karte kielwasser (Wellen 4). Ball m = 0, omega^2 = {KW_W2} (Q {pr['Q']:.2f}, R_halb {pr['R_halb']:.2f}) gehalten "
          f"(V_h = {KW_HALT} r^2) bei x = {KW_X0}; Medium stroemt in +x (Ruhesystem des Balls). Dichtebild gemittelt "
          f"ueber die letzten {KW_MITTEL}; Winkelprofil im Ring r = {KW_RING}.",
          "Lauf | u/c_s | u | gamma | Mach Medium | Mach Ballsystem | RMS-Spitze oben/unten | gemessen | Abw. | 50-%-Kante | "
          "RMS-Spitze | RMS Achse <8 Grad | Vorlauf RMS | F_x | Wirbel"]
    for stufe, e in ergebnis.items():
        zz.append(f"[{stufe}]")
        if "fehler" in e:
            zz.append("  Auswertung fehlgeschlagen:\n" + e["fehler"])
            continue
        for z in e["zeilen"]:
            if "winkel_mess" not in z:
                zz.append(f"  {z['name']} | {z['u_cs']} | {z['u']:.4f} | Medium allein: max|dC| {z['dC_max_abs']:.1e}, "
                          f"C-Spanne {z['C_spanne_max']:.1e}")
                continue
            zz.append(f"  {z['name']} | {z['u_cs']} | {z['u']:.4f} | {z['gamma']:.3f} | {fz(z['mach_medium'], '.1f')} | "
                      f"{fz(z['mach_vorhersage_ball'], '.1f')} | {z['winkel_oben']:.0f}/{z['winkel_unten']:.0f} | "
                      f"{z['winkel_mess']:.1f} | {fz(z.get('abweichung_grad'), '+.1f')} | {fz(z.get('kante_50'), '.1f')} | {z['amplitude']:.2e} | {z['rms_achse_0_8']:.2e} | "
                      f"{z['vorlauf_rms']:.1e} | {z['F_x_mittel']:+.2e} | {z['N_wirbel_max']:.0f}")
        zz += ["  Urteil: " + u for u in e["urteile"]]
    return zz


# ================================================================ Karte wirbel (Wellen 18)

def karte_wirbel(rah):
    prof = profile_holen([(WB_W2, 0)], rah.mini)
    pr = prof[(WB_W2, 0)]
    r_win, r_psi, r_chi = pr["R_halb"] + 8.0, pr["R_halb"], pr["R_halb"] + 4.0
    ergebnis = {}
    for stufe in rah.stufen_liste():
        auswahl = WB_LAEUFE if stufe == "grob" else tuple(s for s in WB_LAEUFE if s["name"] in WB_FEIN)
        specs = []
        for s in auswahl:
            d = spec_basis(s, WB_W2, WB_X0, WB_Y0)
            d.update(stroemung(s["u_cs"]))
            d["halt"] = WB_HALT
            specs.append(d)
        auf, lauf = rah.rechnen(stufe, specs, prof, WB_T, WB_RAMPE, r_win, r_psi, r_chi)
        try:
            ergebnis[stufe] = auswertung_wirbel(specs, lauf, pr)
        except Exception:
            ergebnis[stufe] = {"fehler": traceback.format_exc()}
            print(ergebnis[stufe]["fehler"], flush=True)
    rah.schreiben({"profil": profil_info(pr), "ergebnis": ergebnis}, bericht_wirbel(ergebnis, pr),
                 l3=(("N_ereignisse", 1.0), ("erste_zeit", 20.0), ("F_x_mittel", 1e-4)))


def auswertung_wirbel(specs, lauf, pr):
    t = lauf["t"]
    w = t >= lauf["extra"]["T_rampe"]
    D = 2.0 * pr["R_halb"]
    zeilen = []
    for b, s in enumerate(specs):
        npl, nmi = reihe(lauf, b, "N_plus"), reihe(lauf, b, "N_minus")
        seiten = {k: reihe(lauf, b, k) for k in ("N_plus_oben", "N_minus_oben", "N_plus_unten", "N_minus_unten")}
        ereignisse = []
        for i in range(1, t.shape[0]):
            for k, v in seiten.items():
                d = int(round((v[i] - v[i - 1]).item()))
                if d > 0:
                    ereignisse.append((round(t[i].item(), 1), k, d))
        n_ereig = sum(e[2] for e in ereignisse)
        zeiten = sorted({e[0] for e in ereignisse})
        abst = [b2 - a2 for a2, b2 in zip(zeiten[:-1], zeiten[1:]) if b2 - a2 > 2.0]
        z = {"name": s["name"], "u_cs": s["u_cs"], "u": s["u"], "lam": s["lam"], "N_ereignisse": n_ereig,
             "erste_zeit": zeiten[0] if zeiten else None, "N_frei_max": (npl + nmi).max().item(),
             "N_alle_max": reihe(lauf, b, "N_alle").max().item(), "ereignisse_20": ereignisse[:20],
             "mittlerer_abstand": (sum(abst) / len(abst)) if abst else None,
             "F_x_mittel": reihe(lauf, b, "F_x")[w].mean().item(),
             "F_y_rms": reihe(lauf, b, "F_y")[w].std().item() if int(w.sum()) > 2 else None,
             "X_spanne": (reihe(lauf, b, "X")[w].max() - reihe(lauf, b, "X")[w].min()).item(),
             "wind_psi": sorted(set(reihe(lauf, b, "wind_psi").tolist())), "zirk_chi_werte": sorted(set(reihe(lauf, b, "zirk_chi").tolist()))}
        if zeiten:
            ab = t >= zeiten[0]
            per = periodogramm(t[ab], reihe(lauf, b, "F_y")[ab], 2.0 * PI / max((t[-1] - zeiten[0]).item(), 1.0) * 1.5, 0.5)
            z["auftrieb_periodogramm"] = per
            if per:
                z["strouhal_aus_auftrieb"] = (per["omega"] / (2.0 * PI)) * D / s["u"] if s["u"] > 0 else None
        if z["mittlerer_abstand"]:
            z["strouhal_aus_ereignissen"] = D / (z["mittlerer_abstand"] * s["u"]) if s["u"] > 0 else None
        oben = sum(e[2] for e in ereignisse if e[1].endswith("oben"))
        unten = n_ereig - oben
        z["oben_unten"] = [oben, unten]
        zeilen.append(z)
    urteile = []
    nam = {z["name"]: z for z in zeilen}
    if "u0.4" in nam:
        urteile.append(f"u0.4: {nam['u0.4']['N_ereignisse']} Wirbel -> {'unter der Schwelle (V-W1)' if nam['u0.4']['N_ereignisse'] == 0 else 'Abloesung schon bei 0,4 c_s'}")
    ab = [z for z in zeilen if z["lam"] > 0 and z["N_ereignisse"] > 0]
    if ab:
        urteile.append(f"Schwelle zwischen u/c_s = {max([z['u_cs'] for z in zeilen if z['lam'] > 0 and z['N_ereignisse'] == 0] or [0.0])} "
                       f"und {min(z['u_cs'] for z in ab)}")
    if "u0.85_lam0" in nam:
        urteile.append(f"lam0: {nam['u0.85_lam0']['N_alle_max']:.0f} Wirbel (erwartet 0)")
    return {"zeilen": zeilen, "urteile": urteile, "D": D}


def bericht_wirbel(ergebnis, pr):
    zz = [f"Karte wirbel (Wellen 18). Ball m = 0, omega^2 = {WB_W2} (Q {pr['Q']:.1f}, R_halb {pr['R_halb']:.2f}, "
          f"D = 2 R_halb = {2 * pr['R_halb']:.1f}) gehalten (V_h = {WB_HALT} r^2), y0 = {WB_Y0} (kleiner Anstoss).",
          "Lauf | u/c_s | u | Ereignisse | erste Zeit | oben/unten | mittl. Abstand | St (Ereignisse) | "
          "Auftrieb Periode | St (Auftrieb) | F_x | F_y RMS | N frei max"]
    for stufe, e in ergebnis.items():
        zz.append(f"[{stufe}]")
        if "fehler" in e:
            zz.append("  Auswertung fehlgeschlagen:\n" + e["fehler"])
            continue
        for z in e["zeilen"]:
            per = z.get("auftrieb_periodogramm")
            zz.append(f"  {z['name']} | {z['u_cs']} | {z['u']:.4f} | {z['N_ereignisse']} | {fz(z['erste_zeit'], '.0f')} | "
                      f"{z['oben_unten']} | {fz(z['mittlerer_abstand'], '.1f')} | {fz(z.get('strouhal_aus_ereignissen'), '.3f')} | "
                      f"{fz(per['periode'] if per else None, '.1f')} | {fz(z.get('strouhal_aus_auftrieb'), '.3f')} | "
                      f"{z['F_x_mittel']:+.2e} | {fz(z['F_y_rms'], '.1e')} | {z['N_frei_max']:.0f}")
            if z["ereignisse_20"]:
                zz.append(f"      erste Ereignisse (t, Seite und Vorzeichen, Zahl): {z['ereignisse_20'][:10]}")
        zz += ["  Urteil: " + u for u in e["urteile"]]
    return zz


# ================================================================ Karte brechung (Wellen 14)

def massen_im_medium(rah, prof, stufe):
    """M_eff(dC) = F(Ball + Medium) - F(Medium) bei festem Q und festem w (Grand-Potential), gleichfoermige Medien
    C0 + dC fuer alle dC der Laeufe; dazu lam = 0 als Kontrolle (muss die Vakuumenergie des Profils treffen)."""
    dx, _ = rah.stufen[stufe]
    g = Gitter(L_BOX, dx)
    specs = []
    for dc in sorted({0.0} | {s["dC"] for s in BR_LAEUFE}):
        for mit in (True, False):
            specs.append({"name": f"dC{dc}_{'ball' if mit else 'leer'}", "m": 0 if mit else None, "w2": BR_W2,
                          "x0": 0.0, "y0": 0.0, "lam": LAM, "W_konst": -2.0 * G4 * dc})
    specs.append({"name": "lam0_ball", "m": 0, "w2": BR_W2, "x0": 0.0, "y0": 0.0, "lam": 0.0})
    specs.append({"name": "lam0_leer", "m": None, "w2": BR_W2, "x0": 0.0, "y0": 0.0, "lam": 0.0})
    auf = Aufbau(g, specs, prof)
    t0 = uhr()
    auf.relaxieren(rah.n_relax)
    rah.dauer[f"massen_{stufe}_s"] = uhr() - t0
    F = auf.freie_energie()
    m = {}
    for i in range(0, len(specs), 2):
        m[specs[i]["name"].replace("_ball", "")] = F[i] - F[i + 1]
    return {"M_eff": m, "residuen": list(auf.res), "omega2": auf.om2.tolist()[::2]}


def brechung_vorhersage(m1, m2, v1, th1):
    """P1 (wie R3, Teilchen ohne Mitbewegung des Mediums): E = gamma1 M1 und p_y erhalten."""
    gam = 1.0 / math.sqrt(1.0 - v1 * v1)
    e = gam * m1
    p1 = gam * m1 * v1
    py = p1 * math.sin(th1)
    p2q = e * e - m2 * m2
    if p2q <= py * py:
        return {"ausgang": "reflektiert", "theta2_grad": math.degrees(th1), "v2": v1}
    p2 = math.sqrt(p2q)
    return {"ausgang": "durchgelaufen", "theta2_grad": math.degrees(math.asin(py / p2)), "v2": p2 / e, "n_eff": p2 / p1}


def brechung_mitgefuehrt(p1, m_stern1, m_a1, m1, m2, dc2, th1):
    """P2 (Variante): mitgefuehrte Mediumsmasse m_a ~ C; p_y erhalten, K = p^2/(2 M*) nichtrelativistisch."""
    k1 = p1 * p1 / (2.0 * m_stern1)
    k2 = k1 - (m2 - m1)
    ms2 = m_stern1 + m_a1 * (dc2 / C0)
    py = p1 * math.sin(th1)
    if k2 <= py * py / (2.0 * ms2):
        return {"ausgang": "reflektiert", "theta2_grad": math.degrees(th1)}
    p2 = math.sqrt(2.0 * ms2 * k2)
    return {"ausgang": "durchgelaufen", "theta2_grad": math.degrees(math.asin(py / p2)), "v2": p2 / ms2}


def karte_brechung(rah):
    prof = profile_holen([(BR_W2, 0)], rah.mini)
    pr = prof[(BR_W2, 0)]
    r_win, r_psi, r_chi = pr["R_halb"] + 8.0, pr["R_halb"], pr["R_halb"] + 6.0
    ergebnis = {}
    for stufe in rah.stufen_liste():
        massen = massen_im_medium(rah, prof, stufe)
        me = massen["M_eff"]
        m1 = me["dC0.0"]
        print(f"brechung {stufe}: M_eff {json.dumps(me)} (Vakuum-E {pr['E']:.4f})", flush=True)
        gam = 1.0 / math.sqrt(1.0 - BR_V1 ** 2)
        auswahl = BR_LAEUFE if stufe == "grob" else tuple(s for s in BR_LAEUFE if s["name"] in BR_FEIN)
        specs = []
        for s in auswahl:
            th = math.radians(s["th"])
            d = spec_basis(s, BR_W2, BR_X0, BR_X0 * math.tan(th))
            m_ref = pr["E"] if d["lam"] == 0.0 else m1
            p = gam * m_ref * BR_V1
            d["push"] = (-(p / pr["Q"]) * math.cos(th), -(p / pr["Q"]) * math.sin(th))
            d["p_stoss"] = p
            d["m"] = 0
            specs.append(d)
        auf, lauf = rah.rechnen(stufe, specs, prof, BR_T, BR_RAMPE, r_win, r_psi, r_chi, extra={"massen": massen})
        try:
            ergebnis[stufe] = auswertung_brechung(specs, lauf, massen, pr)
        except Exception:
            ergebnis[stufe] = {"fehler": traceback.format_exc(), "massen": massen}
            print(ergebnis[stufe]["fehler"], flush=True)
    rah.schreiben({"profil": profil_info(pr), "ergebnis": ergebnis}, bericht_brechung(ergebnis, pr),
                 l3=(("theta2", 0.3), ("v2", 0.002)))


def auswertung_brechung(specs, lauf, massen, pr):
    t = lauf["t"]
    me = massen["M_eff"]
    m0 = me["dC0.0"]
    grenze = L_BOX - SPONGE - 6.0
    zeilen = []
    for b, s in enumerate(specs):
        X, Y = reihe(lauf, b, "X"), reihe(lauf, b, "Y")
        dc = s.get("dC", 0.0)
        lam0 = s["lam"] == 0.0
        m1 = pr["E"] if lam0 else m0
        m2 = pr["E"] if lam0 else me.get(f"dC{dc}", m0)
        gueltig = (X.abs() <= grenze) & (Y.abs() <= grenze)
        idx = torch.arange(X.shape[0], device=DEV)
        erst = (X >= -BR_XFIT).nonzero()
        i_a = int(erst[0]) if erst.numel() > 0 else X.shape[0]
        vorher = (t >= lauf["extra"]["T_rampe"] + 5.0 * lauf["extra"]["faktor"]) & (idx < i_a) & gueltig
        i_max = int(torch.argmax(X))
        durch = (X >= BR_XFIT) & gueltig
        zurueck = (idx > i_max) & (X <= -BR_XFIT) & gueltig
        z = {"name": s["name"], "dC": dc, "theta1_soll": s["th"], "lam": s["lam"], "M1": m1, "M2": m2,
             "p_stoss": s["p_stoss"], "n_vorher": int(vorher.sum())}
        if int(vorher.sum()) >= 10:
            vx1, vy1 = geschw(t[vorher], X[vorher]), geschw(t[vorher], Y[vorher])
            v1 = math.hypot(vx1, vy1)
            th1 = math.atan2(vy1, vx1)
            z.update({"v1": v1, "theta1": math.degrees(th1), "vy1": vy1,
                      "M_stern": s["p_stoss"] / v1, "vorhersage_P1": brechung_vorhersage(m1, m2, v1, th1)})
            gam1 = 1.0 / math.sqrt(1.0 - v1 * v1)
            z["m_mitgefuehrt"] = z["M_stern"] - gam1 * m1
            z["vorhersage_P2"] = brechung_mitgefuehrt(s["p_stoss"], z["M_stern"], z["m_mitgefuehrt"], m1, m2, dc, th1)
        if int(durch.sum()) >= 10:
            aus, mask = "durchgelaufen", durch
        elif int(zurueck.sum()) >= 10:
            aus, mask = "reflektiert", zurueck
        else:
            aus, mask = "unklar", None
        z["ausgang"] = aus
        if mask is not None:
            vx2, vy2 = geschw(t[mask], X[mask]), geschw(t[mask], Y[mask])
            z.update({"v2": math.hypot(vx2, vy2), "theta2": math.degrees(math.atan2(vy2, abs(vx2))), "vy2": vy2})
        if "vorhersage_P1" in z and "theta2" in z:
            p1v = z["vorhersage_P1"]
            z["d_theta2_P1"] = z["theta2"] - p1v["theta2_grad"]
            z["v2_zu_P1"] = z["v2"] / p1v["v2"]
            z["ausgang_P1"] = p1v["ausgang"] == aus
            p2v = z["vorhersage_P2"]
            z["d_theta2_P2"] = z["theta2"] - p2v["theta2_grad"]
            z["ausgang_P2"] = p2v["ausgang"] == aus
            if abs(z.get("vy1", 0.0)) > 1e-4:
                z["vy2_zu_vy1"] = z["vy2"] / z["vy1"]
        z["Q_psi_verlust"] = (1.0 - reihe(lauf, b, "Q_psi")[-1] / reihe(lauf, b, "Q_psi")[0]).item()
        z["wirbel_max"] = reihe(lauf, b, "N_alle").max().item()
        zeilen.append(z)
    pruef = [z for z in zeilen if z["dC"] != 0.0 and z["lam"] > 0 and "d_theta2_P1" in z]
    urteil = "offen"
    if pruef:
        okw = all(abs(z["d_theta2_P1"]) <= 1.0 for z in pruef)
        okv = all(abs(z["v2_zu_P1"] - 1.0) <= 0.02 for z in pruef)
        oka = all(z["ausgang_P1"] for z in pruef)
        if okw and okv and oka:
            urteil = "P1 getragen (1 Grad, 2 Prozent, Ausgang): Brechung wie ein Teilchen mit M_eff(C)"
        else:
            urteil = "P1 verfehlt: " + ", ".join(n for n, ok in (("Winkel", okw), ("Geschwindigkeit", okv),
                                                                   ("Ausgang", oka)) if not ok)
            okw2 = all(abs(z["d_theta2_P2"]) <= 1.0 for z in pruef)
            urteil += "; P2 (mitgefuehrte Mediumsmasse) " + ("traegt die Winkel" if okw2 else "verfehlt die Winkel ebenfalls")
    return {"zeilen": zeilen, "massen": massen, "urteil": urteil}


def bericht_brechung(ergebnis, pr):
    zz = [f"Karte brechung (Wellen 14). Ball m = 0, omega^2 = {BR_W2} (Q {pr['Q']:.3f}, Vakuum-E {pr['E']:.4f}), Soll "
          f"v1 = {BR_V1}; Stufe C0 -> C0 + dC bei x = 0 (Breite {BR_BREITE}), Fits fuer |X| >= {BR_XFIT}."]
    for stufe, e in ergebnis.items():
        zz.append(f"[{stufe}]")
        if "massen" in e:
            zz.append("  M_eff (F mit Ball - F ohne Ball): " + json.dumps(e["massen"]["M_eff"])
                      + f"; Kontrolle lam0 gegen Vakuum-E: {e['massen']['M_eff'].get('lam0', float('nan')) - pr['E']:+.2e}")
        if "fehler" in e:
            zz.append("  Auswertung fehlgeschlagen:\n" + e["fehler"])
            continue
        zz.append("  Lauf | dC | th1 soll/mess | v1 | M* (Stoss/v1) | m mitgef. | Ausgang | th2 mess | P1 th2 | d P1 | "
                  "v2/P1 | P2 th2 | d P2 | vy2/vy1 | Q-Verlust")
        for z in e["zeilen"]:
            p1v, p2v = z.get("vorhersage_P1") or {}, z.get("vorhersage_P2") or {}
            zz.append(f"  {z['name']} | {z['dC']:+.2f} | {z['theta1_soll']:.0f}/{fz(z.get('theta1'), '.2f')} | "
                      f"{fz(z.get('v1'), '.4f')} | {fz(z.get('M_stern'), '.3f')} | {fz(z.get('m_mitgefuehrt'), '.3f')} | "
                      f"{z['ausgang']} ({p1v.get('ausgang', '-')}) | {fz(z.get('theta2'), '.2f')} | "
                      f"{fz(p1v.get('theta2_grad'), '.2f')} | {fz(z.get('d_theta2_P1'), '+.2f')} | {fz(z.get('v2_zu_P1'), '.4f')} | "
                      f"{fz(p2v.get('theta2_grad'), '.2f')} | {fz(z.get('d_theta2_P2'), '+.2f')} | "
                      f"{fz(z.get('vy2_zu_vy1'), '.4f')} | {z['Q_psi_verlust']:.1e}")
        zz.append("  Urteil nach PLAN.md: " + e["urteil"])
    return zz


# ================================================================ Profile und Hauptprogramm

def karte_profile(rah):
    liste = [(MG_W2, 0), (MG_W2, 1), (WB_W2, 0), (BR_W2, 0)]
    t0 = time.perf_counter()
    prof = profile_holen(liste, rah.mini)
    rah.dauer["schiessen_s"] = time.perf_counter() - t0
    zz = ["omega2 m | p | Klammer | S_max | R_max | R_halb | Q | E | E/Q | Virialrest | gueltig"]
    for k in liste:
        p = prof[k]
        zz.append(f"  {p['omega2']:.2f} {p['m']} | {p['p']:.15f} | {p['klammer']:.1e} | {p['S_max']:.5f} | {p['R_max']:.3f} | "
                  f"{p['R_halb']:.3f} | {p['Q']:.4f} | {p['E']:.4f} | {p['E'] / p['Q']:.5f} | {p['virialrest']:.1e} | "
                  f"{'ja' if p['gueltig'] else 'NEIN'}")
    zz.append("Erwartung: Virialrest < 1e-6; Werte wie RUNDE-05/r5-2d-a/lauf-lokal/profile_bericht.txt (m = 1 bei 0,60: "
              "Q etwa 138,8, R_halb etwa 5,96).")
    rah.schreiben({"profile": [profil_info(prof[k]) for k in liste]}, zz)


KARTEN = {"profile": karte_profile, "magnus": karte_magnus, "kielwasser": karte_kielwasser, "wirbel": karte_wirbel,
          "brechung": karte_brechung}


def main():
    global DEV
    ap = argparse.ArgumentParser(description="Runde 6, Agent M2: Medium-Karten in 2D (psi-Ball im chi-Medium)")
    ap.add_argument("karte", choices=list(KARTEN) + ["alle"])
    ap.add_argument("--stufe", choices=["grob", "fein", "beide"], default="beide")
    ap.add_argument("--rauch", action="store_true", help="Laufzeiten x 0,05; nur Durchlauf und Hochrechnung")
    ap.add_argument("--mini", action="store_true", help="mit --rauch: grobes Gitter, x 0,02 (Formprobe, auch CPU)")
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("Kein CUDA-Geraet sichtbar: Abbruch (kein stiller CPU-Ausweg; --geraet cpu waehlen).")
        DEV = torch.device("cuda")
    else:
        torch.set_num_threads(1)
        DEV = torch.device("cpu")
        if not args.rauch:
            print("WARNUNG: Messlauf auf der CPU (1 Thread) ist etwa 10- bis 30-mal langsamer als die P4000.", flush=True)
    if args.mini and not args.rauch:
        raise SystemExit("--mini nur zusammen mit --rauch")
    if args.karte == "alle" and not args.rauch:
        raise SystemExit("'alle' nur mit --rauch (sonst laenger als 10 min)")
    if args.out is None:
        args.out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rauchtest" if args.rauch else "ausgabe")
    namen = ["profile", "magnus", "kielwasser", "wirbel", "brechung"] if args.karte == "alle" else [args.karte]
    fehler = []
    t_ges = time.perf_counter()
    for name in namen:
        try:
            KARTEN[name](Rahmen(name, args))
        except Exception:
            fehler.append(name)
            print(f"FEHLER in {name}:\n{traceback.format_exc()}", flush=True)
    speicher = torch.cuda.max_memory_allocated() / 2 ** 20 if DEV.type == "cuda" else float("nan")
    print(f"Ende {jetzt()}, gesamt {time.perf_counter() - t_ges:.1f} s, Torch-Speicher max {speicher:.0f} MB, "
          f"Karten mit Fehler: {fehler}", flush=True)
    if fehler:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
