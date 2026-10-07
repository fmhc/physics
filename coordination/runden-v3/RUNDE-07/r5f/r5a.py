#!/usr/bin/env python3
"""Runde 5 (runden-v3), Paket R5-A: sechs Q-Ball-Ideen in 3D-Radialsymmetrie. Explorativ. Ungetestet abgegeben
(Interpreterverbot auf dem Laptop); Aufrufe, Laufzeiten, Vorhersagen und Latten stehen in PLAN.md daneben.

Modell: L = |psi_t|^2 - |grad psi|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2, 1/2 < omega^2 < 1.

Grundlage RUNDE-02/tests1d/tests1d.py (Test 4, dort auf der P4000 gelaufen):
  unveraendert: koeffizienten, g_u, g_strich, rk4_radial, Konstanten des Schiessens (h = 0,05, bis r = 150,
                1024 Kandidaten x 4 Runden, s = -ln(f_top - f(0)) in [s_min, 150], Schwanz ab |f| < 1e-3 f(0))
  erweitert:    radial_start, schiessen_radial, radial_bahn, radial_integrale bekommen die Schrittweite h als Argument
                (fuer L3: h/2) und eine Knotenzahl n (fuer Bio 17). Fuer n = 0 entscheiden Schiessen und Bahn genau
                wie in tests1d: Ueberschuss = weiterer Nulldurchgang, Unterschuss = Umkehr vor dem Nulldurchgang.
  neu:          radiale Zeitentwicklung mit chi = r psi: chi_tt = chi_rr - U'(|chi/r|^2) chi, chi(0) = 0. Derselbe
                Velocity-Verlet-Schritt wie tests1d.entwickeln (dr = 0,1, dt = 0,05; fein dr/2, dt/2; quadratische
                Daempfungsschicht sigma0 = 1, 40 breit am Rand r = 150). Dazu ein Bad -gamma (psi_t + i omega_b psi):
                  omega_b = 0: gleichmaessiger Ladungsabfluss, dQ/dt = -gamma Q (Bio 4)
                  omega_b > 0: Reservoir mit festem chemischem Potential omega_b (Chemie 11); fuer einen ruhenden
                               Ball gilt dQ/dt = -gamma (1 - omega_b/omega) Q.

Unterbefehle (einer je Idee, dazu der Rauchtest):
  membran   Bio 1      Spannungstensor p_r, p_t; Wandspannung sigma; Young-Laplace Delta P = 2 sigma / R
  tod       Bio 4      Ladungsabfluss durch Q_min: stirbt der Ball schlagartig oder allmaehlich?
  mutanten  Bio 17     radial angeregte Profile mit 1 und 2 Knoten: Existenz, E(Q) gegen Grundzustand, Lebensdauer
  fitness   Bio 19/34  nur Auswertung der Q(omega)-Tabelle aus Runde 2: E/Q, 1 - omega, Q-Fenster, Fusionsgewinn
  keim      Chemie 11  Ball im Reservoir omega_b: waechst oder schrumpft er; kritischer Radius gegen 2 sigma / Delta P
  magisch   Chemie 18  E/Q(Q) fein fuer n = 0, 1, 2: glatt, Knicke oder Stufen?
  rauch     alle sechs verkleinert (Laufzeiten x 0,05, 2 Schiessrunden, kurze omega-Listen): prueft nur den Durchlauf

Aufruf: python r5a.py <unterbefehl> [--geraet cuda|cpu] [--out ORDNER] [--tabelle JSON] [--kand K] [--runden R]
  float64 bzw. complex128 auf beiden Geraeten. Voreinstellung Schiessen: cuda 1024 Kandidaten x 4 Runden (wie
  tests1d), cpu 256 x 5 (gleiche Klammerbreite 1,4e-10 bei einem Drittel der Arbeit). Torch-Speicher auf der Karte
  hoechstens 1,5 GB. Nach ZEIT_BUDGET = 540 s werden laufende Zeitentwicklungen gekuerzt und die feine Stufe
  entfaellt; Bericht und JSON entstehen trotzdem (kleintest.sh bricht nach 600 s ab).
"""
import argparse
import datetime
import json
import math
import os
import time
import traceback

import torch

F64 = torch.float64
PI = math.pi
NAN = float("nan")
INF = float("inf")
HIER = os.path.dirname(os.path.abspath(__file__))
DEV = torch.device("cpu")          # wird in main() nach --geraet gesetzt

# ---- aus tests1d.py (Test 4) unveraendert ----
SCHWANZ = 1e-3           # Bahnende bei |f| < SCHWANZ * f(0), danach exponentieller Schwanz
H3, X3 = 0.05, 150.0     # RK4-Schrittweite und Schiesslaenge
N_KAND3, RUNDEN3 = 1024, 4
S_MAX3 = 150.0
# ---- aus tests1d.py (Zeitentwicklung), radial uebertragen ----
SIGMA0 = 1.0             # Daempfungsschicht am Rand
DR, DT = 0.1, 0.05       # grob; fein halbiert beide (FEIN)
FEIN = 0.5
R_BOX, R_SPONGE = 150.0, 110.0
# ---- Runde 5, gemeinsam ----
SPEICHER_GB = 1.5
ZEIT_BUDGET = 540.0      # s je Aufruf
R_MESS = 25.0            # "Ball-Gebiet" r < 25 fuer Q_in und den Ladungsradius (Dichteabweichung: r < R_SPONGE)
Q_MIN_R2, W2_QMIN_R2 = 111.8441, 0.9269        # Runde 2, lauf-69 (tests1d_bericht.txt)
SIGMA_INF = math.sqrt(2.0) / 4.0               # flache Wand bei omega^2 = 1/2: f' = -(f/sqrt 2)(1 - f^2), Int 2 f'^2
W_C = math.sqrt(0.5)
C_DW = 1.5 * SIGMA_INF / W_C * (8.0 * PI * W_C / 3.0) ** (1.0 / 3.0)   # E/Q - omega_c ~ C_DW Q^(-1/3), ~1,357

# ---- Bio 1 Membran ----
M_W2 = [0.51, 0.52, 0.53, 0.54, 0.55, 0.57, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.93, 0.95, 0.98]
M_DREI = [0.52, 0.55, 0.60]                    # die drei Q der Karte; dort auch d = 1 als Gegenprobe
# ---- Bio 4 Tod ----
TOD_W2 = 0.80
TOD_LAEUFE = [("abfluss 2e-3", 2e-3, None), ("abfluss 1e-3", 1e-3, None), ("abfluss 5e-4", 5e-4, None),
              ("stopp 1,1 Q_min", 1e-3, 1.1), ("stopp 0,9 Q_min", 1e-3, 0.9), ("ohne Abfluss", 0.0, None)]
TOD_T, TOD_MESS = 1500.0, 1.0
# ---- Bio 17 Mutanten ----
MU_W2_0 = [round(0.51 + 0.01 * i, 2) for i in range(49)]
MU_W2_N = [round(0.60 + 0.02 * i, 2) for i in range(20)]
MU_DYN = [(1, 0.70), (1, 0.80), (1, 0.90), (2, 0.70), (2, 0.80), (2, 0.90), (0, 0.80), (0, 0.95)]
MU_ETA = 1e-3            # Saat: psi und psi_t mal (1 + MU_ETA)
MU_T, MU_MESS = 1000.0, 1.0
# ---- Bio 19/34 Fitness ----
FU_Q = [120.0, 150.0, 200.0, 300.0, 500.0, 1e3, 3e3, 1e4, 1e5, 1e6]
# ---- Chemie 11 Keim ----
KE_WB2 = [0.55, 0.60, 0.70]
KE_OFF = [-0.02, -0.005, 0.0, 0.005, 0.02]     # Startball omega^2 = omega_b^2 + Versatz
KE_KONTROLLE = [-0.02, 0.02]                   # dieselben Baelle ohne Bad
KE_GAMMA = 0.02
KE_T, KE_MESS = 800.0, 1.0
# ---- Chemie 18 magisch ----
MA_W2 = [round(0.51 + 0.005 * i, 3) for i in range(97)]
MA_W2_N = [round(0.60 + 0.02 * i, 2) for i in range(20)]


# ---------------------------------------------------------------- Hilfen

def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


T_START = [0.0]


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def rest_sek():
    return ZEIT_BUDGET - (uhr() - T_START[0])


def gf(v):
    return float(v.item()) if torch.is_tensor(v) else float(v)


def teilen(a, b):
    return a / b if (b != 0.0 and math.isfinite(a) and math.isfinite(b)) else NAN


def pot(s):
    return s - s * s + 0.5 * s ** 3


def s_top_von(w2):
    """Dichte der dichten Phase (Buckel des Teilchenpotentials): U'(S) = omega^2, groessere Wurzel."""
    return (2.0 + math.sqrt(4.0 - 6.0 * (1.0 - w2))) / 3.0


def p_bulk_von(w2):
    """Druck der homogenen dichten Phase bei omega: omega^2 S - U(S), S = S_top."""
    s = s_top_von(w2)
    return w2 * s - pot(s)


def l3(wert_grob, wert_fein, null):
    """Latte L3: Effekt (Abstand vom Nullwert) mindestens fuenfmal so gross wie die Aenderung grob -> fein."""
    eff, aend = abs(wert_grob - null), abs(wert_fein - wert_grob)
    ok = math.isfinite(eff) and math.isfinite(aend) and eff >= 5.0 * aend
    return {"effekt": eff, "aenderung": aend, "bestanden": bool(ok)}


def erste_zeit(t, maske):
    idx = torch.nonzero(maske)
    return gf(t[int(idx[0, 0])]) if idx.numel() > 0 else NAN


def index_ab(t, t0):
    """Erster Index mit t >= t0; sonst der letzte."""
    if not math.isfinite(t0):
        return t.shape[0] - 1
    idx = torch.nonzero(t >= t0 - 1e-9)
    return int(idx[0, 0]) if idx.numel() > 0 else t.shape[0] - 1


def interp(xs, ys, x):
    """Linear auf aufsteigenden xs; ausserhalb nan."""
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1] and xs[i + 1] > xs[i]:
            return ys[i] + (ys[i + 1] - ys[i]) * (x - xs[i]) / (xs[i + 1] - xs[i])
    return NAN


def median(werte):
    w = sorted(v for v in werte if math.isfinite(v))
    return w[len(w) // 2] if w else NAN


def wrap(a):
    return torch.remainder(a + PI, 2.0 * PI) - PI


def entfalten(th):
    """Phasenreihe stetig machen; Schritte muessen unter pi liegen (omega * t_mess < pi)."""
    return torch.cat([th[:1], th[:1] + torch.cumsum(wrap(th[1:] - th[:-1]), dim=0)], dim=0)


def fz(v, fmt=".4g"):
    if isinstance(v, (int, float)) and math.isinf(v):
        return "inf" if v > 0 else "-inf"
    return format(v, fmt) if isinstance(v, (int, float)) and math.isfinite(v) else "nan"


# ---------------------------------------------------------------- Schiessen (aus tests1d, Test 4)

def koeffizienten(a0):
    """f_top = sqrt(S+) mit S+ = (2 + sqrt(4 - 6 a0))/3 und die Taylor-Koeffizienten c1..c5 von
    F(f) = a0 f - 2 f^3 + 1,5 f^5 um f_top (unveraendert aus tests1d)."""
    s_top = (2.0 + torch.sqrt(4.0 - 6.0 * a0)) / 3.0
    t = torch.sqrt(s_top)
    c = (a0 - 6.0 * s_top + 7.5 * s_top * s_top, -6.0 * t + 15.0 * t * s_top, -2.0 + 15.0 * s_top, 7.5 * t,
         torch.full_like(t, 1.5))
    return t, c


def g_u(u, c):
    """G(u) = -F(f_top - u) = c1 u - c2 u^2 + c3 u^3 - c4 u^4 + c5 u^5 (exakt, auch fuer u > f_top, d. h. f < 0)."""
    c1, c2, c3, c4, c5 = c
    return u * (c1 + u * (-c2 + u * (c3 + u * (-c4 + u * c5))))


def g_strich(u, c):
    c1, c2, c3, c4, c5 = c
    return c1 + u * (-2.0 * c2 + u * (3.0 * c3 + u * (-4.0 * c4 + u * 5.0 * c5)))


def rk4_radial(r, u, up, h, c, dm1):
    """RK4 fuer u'' = G(u) - (d-1)/r u' (u = f_top - f), unveraendert aus tests1d."""
    def ab(rr, uu, pp):
        return pp, g_u(uu, c) - dm1 * pp / rr
    k1u, k1p = ab(r, u, up)
    k2u, k2p = ab(r + 0.5 * h, u + 0.5 * h * k1u, up + 0.5 * h * k1p)
    k3u, k3p = ab(r + 0.5 * h, u + 0.5 * h * k2u, up + 0.5 * h * k2p)
    k4u, k4p = ab(r + h, u + h * k3u, up + h * k3p)
    return (u + (h / 6.0) * (k1u + 2.0 * k2u + 2.0 * k3u + k4u),
            up + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p))


def radial_start(s, c, dm1, h):
    """Reihe um r = 0: u = u0 + a r^2 + b r^4, u0 = exp(-s). Werte bei r = h (tests1d: h = H3)."""
    d = dm1 + 1.0
    u0 = torch.exp(-s)
    a = g_u(u0, c) / (2.0 * d)
    b = g_strich(u0, c) * a / (4.0 * d + 8.0)
    return u0, u0 + a * h ** 2 + b * h ** 4, 2.0 * a * h + 4.0 * b * h ** 3


def schiessen_radial(a0, dm1, knoten, runden, h, n_kand):
    """Einschachteln in s wie tests1d. Je Kandidat werden Nulldurchgaenge gezaehlt. Ueberschuss: mehr als n
    Nulldurchgaenge. Unterschuss: die Bahn kehrt um (entfernt sich wieder von f = 0), bevor sie den naechsten
    Nulldurchgang erreicht, und hat hoechstens n. Fuer n = 0 ist das genau die Regel aus tests1d."""
    t, c = koeffizienten(a0)
    lo = -torch.log(t - 1e-3)
    hi = torch.full_like(lo, S_MAX3)
    stufen = torch.linspace(0.0, 1.0, n_kand, dtype=F64, device=DEV)
    n_schritte = int(round(X3 / h)) - 1
    for _ in range(runden):
        s = lo + (hi - lo) * stufen                              # (n, K)
        _, u, up = radial_start(s, c, dm1, h)
        zustand = torch.zeros_like(s)                            # 0 offen, +1 Ueberschuss, -1 Unterschuss
        null = torch.zeros_like(s)                               # Nulldurchgaenge bisher
        vorz = torch.ones_like(s)                                # Vorzeichen von f im aktuellen Abschnitt
        rein = torch.ones(s.shape, dtype=torch.bool, device=DEV)  # Bahn laeuft auf f = 0 zu
        for k in range(n_schritte):
            u, up = rk4_radial(h * (k + 1), u, up, h, c, dm1)
            offen = zustand == 0
            kreuz = offen & ((t - u) * vorz < 0.0)
            null = null + kreuz.to(F64)
            vorz = torch.where(kreuz, -vorz, vorz)
            weg = vorz * up < 0.0                                # f f' > 0: entfernt sich von f = 0
            ueber = offen & (null > knoten)
            unter = offen & ~kreuz & weg & rein & (null <= knoten)
            rein = (rein | ~weg) & ~kreuz
            zustand = zustand + ueber.to(F64) - unter.to(F64)
            lebt = (zustand == 0).to(F64)
            u = u * lebt
            up = up * lebt
        lo = torch.where(zustand < 0, s, lo.expand_as(s)).max(dim=1, keepdim=True).values
        hi = torch.where(zustand > 0, s, hi.expand_as(s)).min(dim=1, keepdim=True).values
    return 0.5 * (lo + hi), hi - lo, t, c


def radial_bahn(s, t, c, dm1, knoten, h):
    """Profilbahn zum Klammermittel. Stopp (Grund): 1 |f| < SCHWANZ f(0) nach genau n Nulldurchgaengen auf dem Weg
    zu f = 0, 2 Umkehr vor dem Nulldurchgang, 3 ein Nulldurchgang zu viel; 0 offen."""
    u0, u, up = radial_start(s, c, dm1, h)
    f0 = t - u0
    schwelle = SCHWANZ * f0
    bu, bp = [u0, u], [torch.zeros_like(u0), up]
    n_schritte = int(round(X3 / h)) - 1
    aktiv = torch.ones_like(u0, dtype=torch.bool)
    j_cut = torch.full_like(u0, n_schritte + 1, dtype=torch.long)
    grund = torch.zeros_like(u0, dtype=torch.long)
    null = torch.zeros_like(u0)
    vorz = torch.ones_like(u0)
    rein = torch.ones_like(u0, dtype=torch.bool)
    eins = torch.ones_like(grund)
    for k in range(n_schritte):
        u_neu, up_neu = rk4_radial(h * (k + 1), u, up, h, c, dm1)
        f_neu = t - u_neu
        kreuz = aktiv & (f_neu * vorz < 0.0)
        null = null + kreuz.to(F64)
        vorz = torch.where(kreuz, -vorz, vorz)
        weg = vorz * up_neu < 0.0
        stopp = torch.where(~kreuz & rein & (null == knoten) & (f_neu.abs() < schwelle), eins, 0 * eins)
        stopp = torch.where(~kreuz & rein & weg, 2 * eins, stopp)
        stopp = torch.where(null > knoten, 3 * eins, stopp)
        rein = (rein | ~weg) & ~kreuz
        neu = aktiv & (stopp > 0)
        j_cut = torch.where(neu, torch.full_like(j_cut, k + 2), j_cut)
        grund = torch.where(neu, stopp, grund)
        u = torch.where(aktiv, u_neu, u)
        up = torch.where(aktiv, up_neu, up)
        aktiv = aktiv & (stopp == 0)
        bu.append(u)
        bp.append(up)
    return torch.cat(bu, dim=1), torch.cat(bp, dim=1), j_cut, grund, f0


def radial_integrale(bu, bp, j_cut, t, a0, dm1, w2, h):
    """Wie tests1d: Trapez bis r_cut plus Schwanz f_cut (r_cut/r)^((d-1)/2) exp(-k (r - r_cut)); h als Argument."""
    n, p = bu.shape
    idx = torch.arange(p, device=DEV).unsqueeze(0)
    r = idx.to(F64) * h
    gew = h * (idx <= j_cut).to(F64) - 0.5 * h * ((idx == 0) | (idx == j_cut)).to(F64)
    f, fp = t - bu, -bp
    rp = r ** dm1
    sd = torch.where(dm1 == 0, torch.full_like(dm1, 2.0), torch.full_like(dm1, 4.0 * PI))
    s = f * f
    i_f = sd * (gew * s * rp).sum(1, keepdim=True)
    i_g = sd * (gew * fp * fp * rp).sum(1, keepdim=True)
    i_u = sd * (gew * (s - s * s + 0.5 * s ** 3) * rp).sum(1, keepdim=True)
    k = torch.sqrt(a0)
    f_c = f.gather(1, j_cut)
    schwanz = sd * f_c * f_c * (j_cut.to(F64) * h) ** dm1 / (2.0 * k)
    i_f = i_f + schwanz
    w = w2 * i_f
    g = i_g + k * k * schwanz
    v = i_u + schwanz
    e = w + g + v
    q = 2.0 * torch.sqrt(w2) * i_f
    vir = ((dm1 - 1.0) * g + (dm1 + 1.0) * (v - w)) / e      # Pohozaev: (d-2) G + d (V - W) = 0
    return q, e, vir, schwanz / i_f


def familie(zeilen, h, opt, name):
    """zeilen: Liste (omega^2, d, Knotenzahl). Schiessen, Bahn, Integrale; Rueckgabe auf der CPU."""
    w2 = torch.tensor([z[0] for z in zeilen], dtype=F64, device=DEV).unsqueeze(1)
    dm1 = torch.tensor([z[1] - 1.0 for z in zeilen], dtype=F64, device=DEV).unsqueeze(1)
    kn = torch.tensor([float(z[2]) for z in zeilen], dtype=F64, device=DEV).unsqueeze(1)
    a0 = 1.0 - w2
    t0 = uhr()
    s, klammer, t, c = schiessen_radial(a0, dm1, kn, opt.runden, h, opt.kand)
    bu, bp, j_cut, grund, f0 = radial_bahn(s, t, c, dm1, kn, h)
    q, e, vir, schwanz = radial_integrale(bu, bp, j_cut, t, a0, dm1, w2, h)
    sek = uhr() - t0
    schritte = (opt.runden + 1) * (int(round(X3 / h)) - 1)
    print(f"{name}: Schiessen {len(zeilen)} Zeilen x {opt.kand} Kandidaten, {opt.runden} Runden, h = {h}, "
          f"{schritte} RK4-Schritte, {sek:.1f} s ({1000.0 * sek / schritte:.2f} ms je Schritt)", flush=True)
    return {"zeilen": list(zeilen), "h": h, "sek": sek, "schritte": schritte, "s": s.cpu(), "klammer": klammer.cpu(),
            "f_top": t.cpu(), "f": (t - bu).cpu(), "fp": (-bp).cpu(), "j_cut": j_cut.cpu(), "grund": grund.cpu(),
            "f0": f0.cpu(), "Q": q.cpu(), "E": e.cpu(), "virial": vir.cpu(), "schwanz": schwanz.cpu()}


def fam_zeile(fam, i):
    w2, d, kn = fam["zeilen"][i]
    q, e, s = gf(fam["Q"][i, 0]), gf(fam["E"][i, 0]), gf(fam["s"][i, 0])
    grund = int(fam["grund"][i, 0])
    return {"omega2": w2, "d": d, "knoten": kn, "s": s, "klammer_s": gf(fam["klammer"][i, 0]),
            "f0_quadrat": gf(fam["f0"][i, 0]) ** 2, "r_cut": int(fam["j_cut"][i, 0]) * fam["h"], "grund": grund,
            "gueltig": bool(grund == 1 and s < S_MAX3 - 0.5), "Q": q, "E": e, "E_zu_Q": teilen(e, q),
            "virial": gf(fam["virial"][i, 0]), "schwanzanteil": gf(fam["schwanz"][i, 0])}


def profil_kenn(fam, i):
    """Spannungstensor und Radien einer Zeile. Stationaer: p_r = f'^2 + omega^2 f^2 - U, p_t = omega^2 f^2 - f'^2 - U,
    dp_r/dr = -(2/r)(p_r - p_t) = -(4/r) f'^2 (d = 3). Wandspannung sigma = Int (p_r - p_t) dr = Int 2 f'^2 dr."""
    z = fam_zeile(fam, i)
    w2, d, kn = fam["zeilen"][i]
    h = fam["h"]
    jc = int(fam["j_cut"][i, 0])
    f = fam["f"][i, :jc + 1]
    fp = fam["fp"][i, :jc + 1]
    r = torch.arange(jc + 1, dtype=F64) * h
    gew = torch.full_like(r, h)
    gew[0] = 0.5 * h
    gew[-1] = 0.5 * h
    k = math.sqrt(1.0 - w2)
    f_c, r_c = gf(f[-1]), jc * h
    s_r = f * f
    fp2 = fp * fp
    s0 = gf(s_r[0])
    s_top = gf(fam["f_top"][i, 0]) ** 2
    z["S0"], z["S_top"] = s0, s_top
    z["P_in"] = w2 * s0 - pot(s0)
    z["P_bulk"] = w2 * s_top - pot(s_top)
    z["sigma"] = 2.0 * gf((gew * fp2).sum()) + k * f_c * f_c
    z["sigma_rel"] = z["sigma"] / SIGMA_INF
    p_r = fp2 + w2 * s_r - pot(s_r)
    p_t = w2 * s_r - fp2 - pot(s_r)
    neg = (p_t < 0.0).to(F64)
    z["membran_breite"] = gf((gew * neg).sum())
    z["membran_int_pt"] = gf((gew * neg * p_t).sum())
    z["p_r_min"] = gf(p_r.min())
    z["R_halb"] = NAN
    if kn == 0:
        unter = torch.nonzero(s_r < 0.5 * s0)
        if unter.numel() > 0:
            m = int(unter[0, 0])
            if m > 0:
                a, b = gf(s_r[m - 1]), gf(s_r[m])
                z["R_halb"] = (m - 1) * h + h * (a - 0.5 * s0) / (a - b)
    if d == 3:
        r_s = r.clone()
        r_s[0] = 1.0
        z["dP_mech"] = 4.0 * gf((gew * fp2 / r_s).sum()) + 2.0 * k * f_c * f_c / max(r_c, h)
        z["ident_rest"] = teilen(z["dP_mech"], z["P_in"]) - 1.0
        z["R_grad"] = teilen(gf((gew * r * fp2).sum()), gf((gew * fp2).sum()))
        z["R_Q"] = (3.0 * z["Q"] / (8.0 * PI * math.sqrt(w2) * s_top)) ** (1.0 / 3.0) if z["Q"] > 0.0 else NAN
    else:
        z["dP_mech"], z["ident_rest"], z["R_grad"], z["R_Q"] = 0.0, NAN, NAN, NAN
    z["R_YL"] = teilen(2.0 * SIGMA_INF, z["P_bulk"])
    z["Y_halb"] = teilen(z["P_in"] * z["R_halb"], 2.0 * z["sigma"])
    z["Y_grad"] = teilen(z["P_in"] * z["R_grad"], 2.0 * z["sigma"])
    z["Y_Q"] = teilen(z["P_in"] * z["R_Q"], 2.0 * z["sigma"])
    z["Y_vorh"] = teilen(z["P_bulk"] * z["R_halb"], 2.0 * SIGMA_INF)
    z["tolman_delta"] = 0.5 * z["R_halb"] * (1.0 - z["Y_halb"])
    return z, (r, f, p_r, p_t)


def aeste(rows):
    """Nach omega^2 sortiert; duenner Ast bis einschliesslich Q-Minimum, dicker Ast ab dort."""
    rows = sorted(rows, key=lambda z: z["omega2"])
    if not rows:
        return [], [], -1
    i_min = min(range(len(rows)), key=lambda i: rows[i]["Q"])
    return rows[:i_min + 1], rows[i_min:], i_min


def e_zu_q_duenn(duenn, q):
    """E/Q des duennen Asts bei der Ladung q, linear in ln Q; ausserhalb nan."""
    if not (q > 0.0) or not duenn:
        return NAN
    pts = sorted((math.log(z["Q"]), z["E_zu_Q"]) for z in duenn if z["Q"] > 0.0)
    return interp([p[0] for p in pts], [p[1] for p in pts], math.log(q))


def omega_duenn(duenn, q):
    if not (q > 0.0) or not duenn:
        return NAN
    pts = sorted((math.log(z["Q"]), math.sqrt(z["omega2"])) for z in duenn if z["Q"] > 0.0)
    return interp([p[0] for p in pts], [p[1] for p in pts], math.log(q))


def q_min_parabel(rows):
    """Q_min und omega^2 dort: Parabel in omega durch das Gitterminimum und seine Nachbarn (wie tests1d)."""
    rows = sorted(rows, key=lambda z: z["omega2"])
    n = len(rows)
    if n == 0:
        return NAN, NAN
    om = [math.sqrt(z["omega2"]) for z in rows]
    qs = [z["Q"] for z in rows]
    i = min(range(n), key=lambda k: qs[k])
    if 0 < i < n - 1:
        x1, x2, x3 = om[i - 1], om[i], om[i + 1]
        y1, y2, y3 = qs[i - 1], qs[i], qs[i + 1]
        nenner = (x1 - x2) * (x1 - x3) * (x2 - x3)
        pa = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / nenner
        pb = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / nenner
        pc = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / nenner
        if pa > 0.0:
            om_c = -pb / (2.0 * pa)
            return pc - pb * pb / (4.0 * pa), om_c * om_c
    return qs[i], rows[i]["omega2"]


def q_abs_duenn(duenn):
    """Ladung und omega^2, bei denen auf dem duennen Ast E/Q = 1 wird (darueber E < Q: stabil gegen freie Quanten)."""
    rows = sorted(duenn, key=lambda z: z["omega2"])
    for a, b in zip(rows[:-1], rows[1:]):
        if a["E_zu_Q"] < 1.0 <= b["E_zu_Q"]:
            x = (1.0 - a["E_zu_Q"]) / (b["E_zu_Q"] - a["E_zu_Q"])
            lq = math.log(a["Q"]) + x * (math.log(b["Q"]) - math.log(a["Q"]))
            return math.exp(lq), a["omega2"] + x * (b["omega2"] - a["omega2"])
    return NAN, NAN


def monotonie_verstoesse(ast):
    """Nachbarpaare eines Asts, in denen E/Q mit Q steigt (d(E/Q)/dQ = (omega - E/Q)/Q < 0 erwartet)."""
    return sum(1 for a, b in zip(ast[:-1], ast[1:]) if (b["E_zu_Q"] - a["E_zu_Q"]) * (b["Q"] - a["Q"]) > 0.0)


# ---------------------------------------------------------------- radiale Zeitentwicklung (neu)

def radial_gitter(dr):
    return torch.arange(int(round(R_BOX / dr)) + 1, dtype=F64, device=DEV) * dr


def profil_radial(fam, i, r):
    """f(r) der Zeile i auf dem Gitter r, linear aus der Bahn; ab r_cut f_cut (r_cut/r) exp(-k (r - r_cut))."""
    h = fam["h"]
    f = fam["f"][i].to(DEV)
    jc = int(fam["j_cut"][i, 0])
    k = math.sqrt(1.0 - fam["zeilen"][i][0])
    j = r / h
    j0 = j.floor().clamp(max=f.shape[0] - 2)
    anteil = j - j0
    j0 = j0.long()
    innen = f[j0] * (1.0 - anteil) + f[j0 + 1] * anteil
    r_c = jc * h
    aussen = f[jc] * (r_c / r.clamp(min=h)) * torch.exp(-k * (r - r_c))
    return torch.where(j < jc, innen, aussen)


def ball_radial(fam, i, r, eta=0.0):
    """chi = r f(r), chi_t = -i omega chi; beide mal (1 + eta). Rueckgabe (N,)-Tensoren."""
    w = math.sqrt(fam["zeilen"][i][0])
    chi = (r * profil_radial(fam, i, r) * (1.0 + eta)).to(torch.complex128)
    return chi, (-1j * w) * chi


def messer(r, dr, s_init):
    """Messspalten: 0 Q_tot, 1 Q_in (r < R_MESS), 2 E_tot, 3 S_c = |psi(dr)|^2, 4 Phase -arg psi(dr), 5 max |psi|^2,
    6 Ladungsradius (rms, r < R_MESS), 7 Dichteabweichung Int (S - S_0)^2 r^2 / Int S_0^2 r^2 (r < R_SPONGE)."""
    r_s = r.clone()
    r_s[0] = 1.0
    innen = (r < R_MESS).to(F64)
    innen_abw = (r < R_SPONGE).to(F64)
    nenner = ((s_init ** 2) * (r ** 2) * innen_abw).sum(1).clamp(min=1e-300)

    def messen(chi, vel):
        a2 = chi.real ** 2 + chi.imag ** 2
        s = a2 / (r_s * r_s)
        w = (chi * vel.conj()).imag                              # rho r^2 / 2
        wi = w * innen
        grad = torch.zeros_like(a2)
        grad[:, :-1] = ((chi[:, 1:] - chi[:, :-1]).abs() / dr) ** 2
        e = vel.real ** 2 + vel.imag ** 2 + grad + a2 * (1.0 - s + 0.5 * s * s)
        spalten = [8.0 * PI * w.sum(1) * dr, 8.0 * PI * wi.sum(1) * dr, 4.0 * PI * e.sum(1) * dr, s[:, 1],
                   -torch.angle(chi[:, 1]), s[:, 1:].max(dim=1).values,
                   torch.sqrt(((r ** 2) * wi).sum(1).abs() / wi.sum(1).abs().clamp(min=1e-300)),
                   (((s - s_init) ** 2) * (r ** 2) * innen_abw).sum(1) / nenner]
        return torch.stack(spalten, dim=1)
    return messen


def entwickeln_radial(chi, vel, dr, dt, t_end, t_mess, messen, gam, omb, t_stop):
    """Velocity-Verlet wie tests1d.entwickeln fuer chi = r psi, Rand chi(0) = chi(R_BOX) = 0, Daempfungsschicht wie
    dort. Bad -gam (psi_t + i omb psi), solange t < t_stop; gam, omb, t_stop haben die Form (B, 1)."""
    r = radial_gitter(dr)
    r_s = r.clone()
    r_s[0] = 1.0
    sigma = SIGMA0 * ((r - R_SPONGE).clamp(min=0.0) / (R_BOX - R_SPONGE)) ** 2
    rand = torch.ones_like(r)
    rand[0] = 0.0
    rand[-1] = 0.0

    def kraft(chi):
        lap = torch.zeros_like(chi)
        lap[:, 1:-1] = (chi[:, 2:] - 2.0 * chi[:, 1:-1] + chi[:, :-2]) / (dr * dr)
        s = (chi.real ** 2 + chi.imag ** 2) / (r_s * r_s)
        return (lap - (1.0 - 2.0 * s + 1.5 * s * s) * chi) * rand

    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(t_mess / dt)))
    reihe = [messen(chi, vel)]
    kr = kraft(chi)
    gekuerzt = False
    for n in range(1, n_schritte + 1):
        g = gam * (t_stop > (n - 1) * dt).to(F64)
        gi = 1j * (g * omb)
        vel = vel + (0.5 * dt) * (kr - (sigma + g) * vel - gi * chi)
        chi = chi + dt * vel
        kr = kraft(chi)
        vel = vel + (0.5 * dt) * (kr - (sigma + g) * vel - gi * chi)
        if n % alle == 0:
            reihe.append(messen(chi, vel))
            if (n // alle) % 100 == 0 and rest_sek() < 0.0:
                gekuerzt = True
                break
    daten = torch.stack(reihe)                                   # (M, B, 8)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
    return t, daten, gekuerzt


def stufen_radial(name, bauen, t_end, t_mess, gam, omb, t_stop):
    """Grob (dr, dt) und fein (dr/2, dt/2). bauen(r) -> (chi, vel) als (B, N). Fein entfaellt, wenn die Restzeit
    unter dem Dreifachen der groben Laufzeit liegt."""
    aus = {}
    for stufe, dr, dt in (("grob", DR, DT), ("fein", DR * FEIN, DT * FEIN)):
        if stufe == "fein" and rest_sek() < 3.0 * aus["grob"]["sek"]:
            print(f"{name} fein: entfaellt (Restzeit {rest_sek():.0f} s)", flush=True)
            aus["fein"] = None
            continue
        r = radial_gitter(dr)
        chi, vel = bauen(r)
        for a in (chi, vel):
            a[:, 0] = 0.0
            a[:, -1] = 0.0
        r_s = r.clone()
        r_s[0] = 1.0
        s_init = (chi.real ** 2 + chi.imag ** 2) / (r_s * r_s)
        t0 = uhr()
        t, daten, gekuerzt = entwickeln_radial(chi, vel, dr, dt, t_end, t_mess, messer(r, dr, s_init), gam, omb,
                                               t_stop)
        sek = uhr() - t0
        schritte = int(round(gf(t[-1]) / dt))
        print(f"{name} {stufe}: {chi.shape[0]} Laeufe x {chi.shape[1]} Punkte, T = {gf(t[-1]):.1f}"
              f"{' (gekuerzt)' if gekuerzt else ''}, {schritte} Schritte, {sek:.1f} s "
              f"({1000.0 * sek / max(1, schritte):.2f} ms je Schritt)", flush=True)
        aus[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "sek": sek, "gekuerzt": gekuerzt}
    return aus


def reihen_von(stufen, laeufe):
    return {"laeufe": laeufe, "stufen": {s: ({"t": st["t"], "daten": st["daten"]} if st else None)
                                         for s, st in stufen.items()},
            "spalten": ["Q_tot", "Q_in", "E_tot", "S_c", "Phase_c", "S_max", "R_q", "Dichteabweichung"]}


# ---------------------------------------------------------------- Bio 1: Membran und Young-Laplace

def lauf_membran(opt):
    w2s = [0.52, 0.55, 0.60, 0.80] if opt.rauch else M_W2
    eins_d = [0.55] if opt.rauch else M_DREI
    zeilen = [(w2, 3, 0) for w2 in w2s] + [(w2, 1, 0) for w2 in eins_d]
    fams = {"grob": familie(zeilen, H3, opt, "membran h")}
    fams["fein"] = fams["grob"] if opt.rauch else familie(zeilen, H3 * FEIN, opt, "membran h/2")
    erg = {s: [profil_kenn(fam, i)[0] for i in range(len(zeilen))] for s, fam in fams.items()}
    l3_liste = []
    for zg, zf in zip(erg["grob"], erg["fein"]):
        if zg["d"] == 3 and zg["gueltig"] and zf["gueltig"]:
            l3_liste.append({"omega2": zg["omega2"], "P_in": l3(zg["P_in"], zf["P_in"], 0.0),
                             "sigma": l3(zg["sigma"], zf["sigma"], 0.0),
                             "Y_halb_minus_1": l3(zg["Y_halb"], zf["Y_halb"], 1.0),
                             "Y_vorh_minus_1": l3(zg["Y_vorh"], zf["Y_vorh"], 1.0)})
    profile = {}
    for i, (w2, d, _) in enumerate(zeilen):
        if d == 3 and w2 in M_DREI:
            _, (r, f, p_r, p_t) = profil_kenn(fams["grob"], i)
            m = max(1, int(round(0.2 / fams["grob"]["h"])))
            profile[str(w2)] = {"r": r[::m].tolist(), "f": f[::m].tolist(), "p_r": p_r[::m].tolist(),
                                "p_t": p_t[::m].tolist()}
    g3 = [z for z in erg["grob"] if z["d"] == 3 and z["gueltig"]]
    g1 = [z for z in erg["grob"] if z["d"] == 1 and z["gueltig"]]
    duenn = [z for z in g3 if z["omega2"] <= 0.60 and math.isfinite(z["Y_halb"]) and z["R_halb"] > 0.0]
    sxy = sum((1.0 / z["R_halb"]) * (z["Y_halb"] - 1.0) for z in duenn)
    sxx = sum((1.0 / z["R_halb"]) ** 2 for z in duenn)
    zus = {"max_ident_rest": max((abs(z["ident_rest"]) for z in g3 if math.isfinite(z["ident_rest"])), default=NAN),
           "max_P_in_d1": max((abs(z["P_in"]) for z in g1), default=NAN),
           "tolman_delta_fit": -0.5 * sxy / sxx if sxx > 0.0 else NAN,
           "sigma_inf": SIGMA_INF, "n_gueltig": len(g3), "n_zeilen_d3": len(w2s)}
    res = {"zeilen": erg, "L3": l3_liste, "profile_drei_Q": profile, "zusammen": zus,
           "sek": {s: fams[s]["sek"] for s in fams}}
    zz = [f"Bio 1 Membran: Spannungstensor, sigma = Int 2 f'^2 dr (flache Wand sigma_inf = {SIGMA_INF:.5f}), "
          "Young-Laplace Y = Delta P R / (2 sigma). Stufe grob (h = 0,05).",
          "  omega^2 | d | gueltig | Q | S0 | P_in | P_bulk | sigma/sigma_inf | ident (dP_mech/P_in - 1) | R_halb | "
          "R_grad | R_Q | R_YL = 2 sigma_inf/P_bulk | Y_halb | Y_grad | Y_Q | Y_vorh | Membranbreite (p_t<0) | "
          "Int p_t dort | Tolman-delta"]
    for z in erg["grob"]:
        zz.append(f"  {z['omega2']:.2f} | {z['d']} | {z['gueltig']} | {fz(z['Q'], '.5e')} | {fz(z['S0'], '.6f')} | "
                  f"{fz(z['P_in'], '.4e')} | {fz(z['P_bulk'], '.4e')} | {fz(z['sigma_rel'], '.5f')} | "
                  f"{fz(z['ident_rest'], '+.1e')} | {fz(z['R_halb'], '.3f')} | {fz(z['R_grad'], '.3f')} | "
                  f"{fz(z['R_Q'], '.3f')} | {fz(z['R_YL'], '.3f')} | {fz(z['Y_halb'], '.4f')} | "
                  f"{fz(z['Y_grad'], '.4f')} | {fz(z['Y_Q'], '.4f')} | {fz(z['Y_vorh'], '.4f')} | "
                  f"{fz(z['membran_breite'], '.2f')} | {fz(z['membran_int_pt'], '.4f')} | {fz(z['tolman_delta'], '+.3f')}")
    zz.append(f"  Pruefzeilen: max |ident| (d = 3) {fz(zus['max_ident_rest'], '.1e')}; max |P_in| (d = 1, Gegenprobe) "
              f"{fz(zus['max_P_in_d1'], '.1e')}; Tolman-delta aus Fit (omega^2 <= 0,60) "
              f"{fz(zus['tolman_delta_fit'], '+.3f')}")
    n_ok = sum(1 for e in l3_liste for k, v in e.items() if k != "omega2" and v["bestanden"])
    n_ges = sum(1 for e in l3_liste for k in e if k != "omega2")
    zz.append(f"  L3 (h gegen h/2): {n_ok} von {n_ges} Kenngroessen bestanden"
              + (" (Rauchtest: fein = grob)" if opt.rauch else ""))
    for e in l3_liste:
        zz.append(f"    {e['omega2']:.2f}: " + ", ".join(f"{k} {fz(v['effekt'], '.2e')}/{fz(v['aenderung'], '.1e')} "
                                                       f"{'ok' if v['bestanden'] else 'NEIN'}"
                                                       for k, v in e.items() if k != "omega2"))
    return res, zz, {}


# ---------------------------------------------------------------- Bio 4: Tod unter Q_min

def lauf_tod(opt):
    fam = familie([(TOD_W2, 3, 0)], H3, opt, "tod h")
    z0 = fam_zeile(fam, 0)
    if not z0["gueltig"] and not opt.rauch:
        raise RuntimeError(f"Startprofil omega^2 = {TOD_W2} ungueltig: {z0}")
    q0 = z0["Q"]
    laeufe = []
    for name, g, fak in TOD_LAEUFE:
        if fak is None:
            ts = INF
        else:
            ts = math.log(q0 / (fak * Q_MIN_R2)) / g if q0 > fak * Q_MIN_R2 else 0.0
        laeufe.append({"name": name, "gamma": g, "stopp_faktor": fak, "t_stop": ts})
    t_end = TOD_T * (0.05 if opt.rauch else 1.0)
    gam = torch.tensor([[l["gamma"]] for l in laeufe], dtype=F64, device=DEV)
    omb = torch.zeros_like(gam)
    tst = torch.tensor([[l["t_stop"]] for l in laeufe], dtype=F64, device=DEV)

    def bauen(r):
        chi, vel = ball_radial(fam, 0, r)
        return torch.stack([chi] * len(laeufe)), torch.stack([vel] * len(laeufe))

    stufen = stufen_radial("tod", bauen, t_end, TOD_MESS, gam, omb, tst)
    erg = {s: (auswertung_tod(laeufe, st) if st is not None else None) for s, st in stufen.items()}
    p_exp = {s: (verzoegerung_exponent(e) if e is not None else NAN) for s, e in erg.items()}
    l3_liste = []
    if erg.get("fein") is not None:
        for zg, zf in zip(erg["grob"], erg["fein"]):
            if zg["klasse"] != "ueberlebt":
                l3_liste.append({"name": zg["name"],
                                 "rate_durch_gamma": l3(zg["rate_max_durch_gamma"], zf["rate_max_durch_gamma"], 1.0),
                                 "q_rel_T": l3(zg["q_rel_T"], zf["q_rel_T"], 1.0),
                                 "Q_tod": l3(zg["Q_in_bei_t90"], zf["Q_in_bei_t90"], 0.0)})
    res = {"start": z0, "laeufe": laeufe, "ergebnis": erg, "exponent_verzoegerung": p_exp, "L3": l3_liste,
           "Q_min_runde2": Q_MIN_R2, "omega2_Qmin_runde2": W2_QMIN_R2,
           "sek": {s: (st["sek"] if st else None) for s, st in stufen.items()}, "sek_schiessen": fam["sek"]}
    zz = [f"Bio 4 Tod unter Q_min: Start omega^2 = {TOD_W2} (Q = {fz(q0, '.3f')}), gleichmaessiger Abfluss "
          f"-gamma psi_t; Q_min (Runde 2) = {Q_MIN_R2} bei omega^2 = {W2_QMIN_R2}; Ball-Gebiet r < {R_MESS}.",
          "  Lauf | gamma | t_stop | t(Q_erw = Q_min) | t90 | t50 | t10 | Q_in bei t90 / Q_min | omega vor Tod | "
          "rate_max/gamma | gamma x Dauer(90->10) | q_rel(T) | S_c 0 -> T | Klasse"]
    for stufe in ("grob", "fein"):
        if erg.get(stufe) is None:
            zz.append(f"  [{stufe}] entfaellt")
            continue
        zz.append(f"  [{stufe}] Exponent p in Verzoegerung ~ gamma^-p: {fz(p_exp[stufe], '.3f')}")
        for z in erg[stufe]:
            zz.append(f"  {z['name']:16s} | {z['gamma']:.1e} | {fz(z['t_stop'], '.1f')} | {fz(z['t_Qmin'], '.1f')} | "
                      f"{fz(z['t90'], '.1f')} | {fz(z['t50'], '.1f')} | {fz(z['t10'], '.1f')} | "
                      f"{fz(z['Q_tod_durch_Qmin'], '.4f')} | {fz(z['omega_vor_tod'], '.4f')} | "
                      f"{fz(z['rate_max_durch_gamma'], '.2f')} | {fz(z['gamma_mal_dauer'], '.3f')} | "
                      f"{fz(z['q_rel_T'], '.4f')} | {fz(z['S_c_0'], '.4f')} -> {fz(z['S_c_T'], '.2e')} | {z['klasse']}")
    n_ok = sum(1 for e in l3_liste for k, v in e.items() if k != "name" and v["bestanden"])
    n_ges = sum(1 for e in l3_liste for k in e if k != "name")
    zz.append(f"  L3 (grob gegen fein, sterbende Laeufe): {n_ok} von {n_ges} bestanden")
    return res, zz, reihen_von(stufen, laeufe)


def auswertung_tod(laeufe, st):
    t, d = st["t"], st["daten"]
    dtm = gf(t[1] - t[0])
    w10 = max(1, int(round(10.0 / dtm)))
    w20 = max(1, int(round(20.0 / dtm)))
    zeilen = []
    for b, lauf in enumerate(laeufe):
        g, ts = lauf["gamma"], lauf["t_stop"]
        q_tot, q_in, s_c, th = d[:, b, 0], d[:, b, 1], d[:, b, 3], d[:, b, 4]
        q0 = gf(q_tot[0])
        q_erw = q0 * torch.exp(-g * t.clamp(max=ts))
        q_rel = q_in / q_erw
        z = {"name": lauf["name"], "gamma": g, "t_stop": ts, "T": gf(t[-1]), "Q_tot_0": q0, "Q_in_0": gf(q_in[0]),
             "S_c_0": gf(s_c[0]), "t90": erste_zeit(t, q_rel < 0.9), "t50": erste_zeit(t, q_rel < 0.5),
             "t10": erste_zeit(t, q_rel < 0.1), "q_rel_T": gf(q_rel[-1]), "Q_in_T": gf(q_in[-1]),
             "S_c_T": gf(s_c[-1]), "E_tot_0": gf(d[0, b, 2]), "E_tot_T": gf(d[-1, b, 2])}
        z["t_Qmin"] = math.log(q0 / Q_MIN_R2) / g if (g > 0.0 and q0 > Q_MIN_R2) else NAN
        z["rate_max"] = NAN
        if q_in.shape[0] > w10:
            lq = torch.log(q_in.clamp(min=1e-300))
            rate = -(lq[w10:] - lq[:-w10]) / (t[w10:] - t[:-w10])
            gut = q_rel[:-w10] > 0.05
            if bool(gut.any()):
                z["rate_max"] = gf(rate[gut].max())
        z["rate_max_durch_gamma"] = teilen(z["rate_max"], g) if g > 0.0 else NAN
        thu = entfalten(th)

        def omega_bei(tt):
            i = index_ab(t, tt)
            i0 = max(0, i - w20)
            return teilen(gf(thu[i] - thu[i0]), gf(t[i] - t[i0]))
        z["omega_vor_tod"] = omega_bei(z["t90"] - 10.0) if math.isfinite(z["t90"]) else omega_bei(gf(t[-1]))
        if math.isfinite(z["t90"]):
            z["Q_in_bei_t90"] = gf(q_in[index_ab(t, z["t90"])])
        else:
            z["Q_in_bei_t90"] = NAN
        z["Q_tod_durch_Qmin"] = z["Q_in_bei_t90"] / Q_MIN_R2
        z["dauer_90_10"] = z["t10"] - z["t90"]
        z["gamma_mal_dauer"] = g * z["dauer_90_10"] if g > 0.0 else NAN
        z["verzoegerung"] = z["t50"] - z["t_Qmin"]
        gd, rg = z["gamma_mal_dauer"], z["rate_max_durch_gamma"]
        if not math.isfinite(z["t50"]):
            z["klasse"] = "ueberlebt"
        elif math.isfinite(gd) and gd < 0.1 and math.isfinite(rg) and rg > 10.0:
            z["klasse"] = "schlagartig"
        elif (math.isfinite(gd) and gd > 0.3) or (math.isfinite(rg) and rg < 3.0):
            z["klasse"] = "allmaehlich"
        else:
            z["klasse"] = "unklar"
        zeilen.append(z)
    return zeilen


def verzoegerung_exponent(zeilen):
    """p in (t50 - t(Q_erw = Q_min)) ~ gamma^-p aus den Laeufen ohne Stopp (Ausgleichsgerade in log-log)."""
    pts = [(math.log(z["gamma"]), math.log(z["verzoegerung"])) for z in zeilen
           if z["gamma"] > 0.0 and not math.isfinite(z["t_stop"]) and math.isfinite(z["verzoegerung"])
           and z["verzoegerung"] > 0.0]
    if len(pts) < 2:
        return NAN
    mx = sum(p[0] for p in pts) / len(pts)
    my = sum(p[1] for p in pts) / len(pts)
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    return -sum((p[0] - mx) * (p[1] - my) for p in pts) / sxx if sxx > 0.0 else NAN


# ---------------------------------------------------------------- Bio 17: Mutanten (radial angeregt)

def lauf_mutanten(opt):
    w2_0 = [0.55, 0.70, 0.80, 0.90, 0.95] if opt.rauch else MU_W2_0
    w2_n = [0.70, 0.80, 0.90] if opt.rauch else MU_W2_N
    zeilen = [(w2, 3, 0) for w2 in w2_0] + [(w2, 3, 1) for w2 in w2_n] + [(w2, 3, 2) for w2 in w2_n]
    fams = {"grob": familie(zeilen, H3, opt, "mutanten h"), "fein": familie(zeilen, H3 * FEIN, opt, "mutanten h/2")}
    tab = {s: [fam_zeile(fam, i) for i in range(len(zeilen))] for s, fam in fams.items()}
    info = {}
    for s in tab:
        duenn0, _, _ = aeste([z for z in tab[s] if z["knoten"] == 0 and z["gueltig"]])
        for z in tab[s]:
            z["E0_gleiches_Q"] = z["Q"] * e_zu_q_duenn(duenn0, z["Q"]) if z["gueltig"] else NAN
            z["dE_zum_Grundzustand"] = z["E"] - z["E0_gleiches_Q"]
            z["dE_je_Q"] = teilen(z["dE_zum_Grundzustand"], z["Q"])
        info[s] = {}
        for kn in (0, 1, 2):
            rows = [z for z in tab[s] if z["knoten"] == kn and z["gueltig"]]
            duenn, dick, _ = aeste(rows)
            q_min, w2_min = q_min_parabel(rows)
            info[s][kn] = {"n_gueltig": len(rows), "n_gesucht": sum(1 for z in tab[s] if z["knoten"] == kn),
                           "Q_min": q_min, "omega2_Qmin": w2_min,
                           "monotonie_verstoesse": monotonie_verstoesse(duenn) + monotonie_verstoesse(dick),
                           "E_groesser_Q_omega2": [z["omega2"] for z in rows if z["E"] > z["Q"]],
                           "max_abs_virial": max((abs(z["virial"]) for z in rows), default=NAN),
                           "min_dE_zum_Grundzustand": min((z["dE_zum_Grundzustand"] for z in rows
                                                           if math.isfinite(z["dE_zum_Grundzustand"])), default=NAN)}
    dyn, ausgelassen = [], []
    for kn, w2 in MU_DYN:
        i = next((j for j, zl in enumerate(zeilen) if zl[2] == kn and abs(zl[0] - w2) < 1e-9), None)
        if i is None:
            ausgelassen.append({"knoten": kn, "omega2": w2, "grund": "nicht in der Liste"})
            continue
        z = tab["grob"][i]
        if not z["gueltig"] and not opt.rauch:
            ausgelassen.append({"knoten": kn, "omega2": w2, "grund": "kein Profil gefunden"})
            continue
        if z["r_cut"] > R_SPONGE - 20.0:
            ausgelassen.append({"knoten": kn, "omega2": w2, "grund": f"r_cut {z['r_cut']:.1f} zu gross"})
            continue
        dyn.append({"knoten": kn, "omega2": w2, "zeile": i, "Q": z["Q"], "E": z["E"], "r_cut": z["r_cut"]})
    stufen, erg_dyn = {}, {}
    if dyn:
        t_end = MU_T * (0.05 if opt.rauch else 1.0)
        gam = torch.zeros((len(dyn), 1), dtype=F64, device=DEV)
        tst = torch.full((len(dyn), 1), INF, dtype=F64, device=DEV)

        def bauen(r):
            felder = [ball_radial(fams["grob"], l["zeile"], r, MU_ETA) for l in dyn]
            return torch.stack([a for a, _ in felder]), torch.stack([b for _, b in felder])

        stufen = stufen_radial("mutanten", bauen, t_end, MU_MESS, gam, gam.clone(), tst)
        erg_dyn = {s: (auswertung_mutant(dyn, st) if st is not None else None) for s, st in stufen.items()}
    l3_liste = []
    for zg, zf in zip(tab["grob"], tab["fein"]):
        if zg["knoten"] > 0 and zg["gueltig"] and zf["gueltig"]:
            l3_liste.append({"was": f"n={zg['knoten']} omega^2={zg['omega2']}",
                             "dE_zum_Grundzustand": l3(zg["dE_zum_Grundzustand"], zf["dE_zum_Grundzustand"], 0.0)})
    if erg_dyn.get("fein") is not None:
        for zg, zf in zip(erg_dyn["grob"], erg_dyn["fein"]):
            l3_liste.append({"was": f"Dynamik n={zg['knoten']} omega^2={zg['omega2']}",
                             "t_zerfall": l3(zg["t_zerfall"], zf["t_zerfall"], 0.0)})
    res = {"tabelle": tab, "familien": info, "dynamik": dyn, "ausgelassen": ausgelassen, "ergebnis_dynamik": erg_dyn,
           "L3": l3_liste, "sek_schiessen": {s: fams[s]["sek"] for s in fams},
           "sek_dynamik": {s: (st["sek"] if st else None) for s, st in stufen.items()}}
    zz = ["Bio 17 Mutanten: radial angeregte Profile (n Knoten), Stufe grob (h = 0,05).",
          "  n | omega^2 | gueltig | s | Klammer | r_cut | Q | E | E/Q | E - E_0(gleiches Q) | Virial"]
    for z in tab["grob"]:
        if z["knoten"] == 0 and z["omega2"] not in (0.55, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99):
            continue
        zz.append(f"  {z['knoten']} | {z['omega2']:.2f} | {z['gueltig']} | {fz(z['s'], '.4f')} | "
                  f"{fz(z['klammer_s'], '.1e')} | {fz(z['r_cut'], '.1f')} | {fz(z['Q'], '.5e')} | {fz(z['E'], '.5e')} | "
                  f"{fz(z['E_zu_Q'], '.5f')} | {fz(z['dE_zum_Grundzustand'], '+.4e')} | {fz(z['virial'], '+.1e')}")
    for kn in (0, 1, 2):
        fi = info["grob"][kn]
        zz.append(f"  Familie n = {kn}: gueltig {fi['n_gueltig']} von {fi['n_gesucht']}; Q_min {fz(fi['Q_min'], '.4g')} "
                  f"bei omega^2 {fz(fi['omega2_Qmin'], '.4f')}; Monotonie-Verstoesse E/Q(Q) {fi['monotonie_verstoesse']}; "
                  f"min (E - E_0) {fz(fi['min_dE_zum_Grundzustand'], '+.3e')}; max |Virial| "
                  f"{fz(fi['max_abs_virial'], '.1e')}")
    zz.append("  Dynamik (Saat psi, psi_t mal 1 + 1e-3): n | omega^2 | t_zerfall (Abw. > 0,1) | Anwachsrate lambda | "
              "Abw. Start | Q_in T/0 | S_c T | omega Ende | Klasse")
    for s in ("grob", "fein"):
        e = erg_dyn.get(s)
        if e is None:
            zz.append(f"  [{s}] entfaellt")
            continue
        zz.append(f"  [{s}]")
        for z in e:
            zz.append(f"  {z['knoten']} | {z['omega2']:.2f} | {fz(z['t_zerfall'], '.1f')} | {fz(z['lambda'], '.4f')} | "
                      f"{fz(z['abw_start'], '.1e')} | {fz(z['Q_in_T_durch_0'], '.4f')} | {fz(z['S_c_T'], '.3e')} | "
                      f"{fz(z['omega_ende'], '.4f')} | {z['klasse']}")
    for a in ausgelassen:
        zz.append(f"  ausgelassen: n = {a['knoten']}, omega^2 = {a['omega2']}: {a['grund']}")
    n_ok = sum(1 for e in l3_liste for k, v in e.items() if k != "was" and v["bestanden"])
    n_ges = sum(1 for e in l3_liste for k in e if k != "was")
    zz.append(f"  L3 (h gegen h/2 bzw. grob gegen fein): {n_ok} von {n_ges} bestanden")
    return res, zz, (reihen_von(stufen, dyn) if stufen else {})


def auswertung_mutant(dyn, st):
    t, d = st["t"], st["daten"]
    dtm = gf(t[1] - t[0])
    w100 = max(1, int(round(100.0 / dtm)))
    zeilen = []
    for b, l in enumerate(dyn):
        abw, q_in, s_c, th = d[:, b, 7], d[:, b, 1], d[:, b, 3], d[:, b, 4]
        t_z = erste_zeit(t, abw > 0.1)
        t_a, t_b = erste_zeit(t, abw > 1e-4), erste_zeit(t, abw > 1e-2)
        lam = math.log(100.0) / (2.0 * (t_b - t_a)) if (math.isfinite(t_a) and math.isfinite(t_b) and t_b > t_a) else NAN
        thu = entfalten(th)
        i0 = max(0, thu.shape[0] - 1 - w100)
        om_e = teilen(gf(thu[-1] - thu[i0]), gf(t[-1] - t[i0]))
        z = {"knoten": l["knoten"], "omega2": l["omega2"], "t_zerfall": t_z, "t_1e-4": t_a, "t_1e-2": t_b,
             "lambda": lam, "abw_start": gf(abw[:index_ab(t, 20.0) + 1].max()), "abw_T": gf(abw[-1]),
             "Q_in_0": gf(q_in[0]), "Q_in_T": gf(q_in[-1]), "Q_in_T_durch_0": teilen(gf(q_in[-1]), gf(q_in[0])),
             "Q_tot_T_durch_0": teilen(gf(d[-1, b, 0]), gf(d[0, b, 0])),
             "S_c_0": gf(s_c[0]), "S_c_T": gf(s_c[-1]), "omega_ende": om_e, "T": gf(t[-1]),
             "klasse": "zerfallen" if math.isfinite(t_z) else "lebt bis T"}
        zeilen.append(z)
    return zeilen


# ---------------------------------------------------------------- Bio 19/34: Fitness und Energiewaehrung

def lauf_fitness(opt):
    with open(opt.tabelle) as fh:
        roh = json.load(fh)
    if "ergebnisse" in roh:
        quelle = [z for z in roh["ergebnisse"]["4"]["zeilen"] if z["d"] == 3]
    else:
        quelle = [z for z in roh["zeilen"] if z.get("d", 3) == 3 and z.get("knoten", 0) == 0]
    rows = []
    for z in sorted(quelle, key=lambda z: z["omega2"]):
        if not (z["Q"] > 0.0 and math.isfinite(z["E"])):
            continue
        om = math.sqrt(z["omega2"])
        eq = z["E"] / z["Q"]
        rows.append({"omega2": z["omega2"], "Q": z["Q"], "E": z["E"], "E_zu_Q": eq, "omega": om,
                     "b_frei_je_Ladung": 1.0 - eq, "grenzgewinn_1_minus_omega": 1.0 - om, "B_bindung": z["Q"] - z["E"],
                     "E_zu_Q_minus_omega": eq - om, "duennwand_konst": (eq - W_C) * z["Q"] ** (1.0 / 3.0) / C_DW})
    duenn, dick, _ = aeste(rows)
    q_min, w2_min = q_min_parabel(rows)
    q_abs, w2_abs = q_abs_duenn(duenn)
    q_max = max((z["Q"] for z in duenn), default=NAN)
    fusion = []
    for i, q1 in enumerate(FU_Q):
        for q2 in FU_Q[i:]:
            if not (q1 + q2 <= q_max):
                continue
            e1, e2 = q1 * e_zu_q_duenn(duenn, q1), q2 * e_zu_q_duenn(duenn, q2)
            e12 = (q1 + q2) * e_zu_q_duenn(duenn, q1 + q2)
            de = e1 + e2 - e12
            fusion.append({"Q1": q1, "Q2": q2, "dE_fusion": de, "dE_je_Q1": teilen(de, q1),
                           "wirkungsgrad": teilen(de, e1 + e2), "omega_Q1": omega_duenn(duenn, q1),
                           "omega_Q2": omega_duenn(duenn, q2)})
    zus = {"Q_min": q_min, "omega2_Qmin": w2_min, "Q_abs_E_gleich_Q": q_abs, "omega2_Qabs": w2_abs,
           "fenster_metastabil": [q_min, q_abs], "Q_max_tabelle_duenn": q_max,
           "monotonie_verstoesse_duenn": monotonie_verstoesse(duenn),
           "monotonie_verstoesse_dick": monotonie_verstoesse(dick),
           "E_zu_Q_minus_omega_min": min((z["E_zu_Q_minus_omega"] for z in rows), default=NAN),
           "dick_E_kleiner_Q": [z["omega2"] for z in dick if z["E"] < z["Q"]],
           "fusion_alle_positiv": all(f["dE_fusion"] > 0.0 for f in fusion if math.isfinite(f["dE_fusion"])),
           "ostwald_richtung_alle": all(f["omega_Q1"] >= f["omega_Q2"] for f in fusion
                                        if math.isfinite(f["omega_Q1"]) and math.isfinite(f["omega_Q2"])),
           "duennwand_konst_C_DW": C_DW, "b_grenze_grosse_Q": 1.0 - W_C, "quelle": opt.tabelle}
    res = {"zeilen": rows, "fusion": fusion, "zusammen": zus}
    zz = [f"Bio 19/34 Fitness und Waehrung (nur Auswertung der Tabelle {os.path.basename(opt.tabelle)}).",
          "  omega^2 | Q | E/Q | b = 1 - E/Q | 1 - omega | E/Q - omega | (E/Q - omega_c) Q^(1/3) / C_DW"]
    for z in rows:
        zz.append(f"  {z['omega2']:.2f} | {z['Q']:.5e} | {z['E_zu_Q']:.5f} | {z['b_frei_je_Ladung']:+.5f} | "
                  f"{z['grenzgewinn_1_minus_omega']:.5f} | {z['E_zu_Q_minus_omega']:.5f} | {z['duennwand_konst']:.4f}")
    zz.append(f"  Q-Fenster: kein Ball unter Q_min = {fz(q_min, '.3f')} (omega^2 {fz(w2_min, '.4f')}); metastabil "
              f"(VK-stabil, E > Q) bis Q_abs = {fz(q_abs, '.2f')} (omega^2 {fz(w2_abs, '.4f')}); darueber E < Q.")
    zz.append(f"  Monotonie E/Q(Q): Verstoesse duenn {zus['monotonie_verstoesse_duenn']}, dick "
              f"{zus['monotonie_verstoesse_dick']}; min (E/Q - omega) {fz(zus['E_zu_Q_minus_omega_min'], '.3e')}; "
              f"dicker Ast mit E < Q bei {zus['dick_E_kleiner_Q']}")
    zz.append("  Fusion auf dem duennen Ast: Q1 | Q2 | dE = E(Q1) + E(Q2) - E(Q1+Q2) | dE/Q1 | dE/(E1+E2) | omega(Q1) | "
              "omega(Q2)")
    for f in fusion:
        zz.append(f"  {f['Q1']:.0f} | {f['Q2']:.0f} | {fz(f['dE_fusion'], '.4e')} | {fz(f['dE_je_Q1'], '.4f')} | "
                  f"{fz(f['wirkungsgrad'], '.3e')} | {fz(f['omega_Q1'], '.4f')} | {fz(f['omega_Q2'], '.4f')}")
    zz.append(f"  Fusion alle positiv: {zus['fusion_alle_positiv']}; Ladung fliesst immer vom kleineren zum groesseren "
              f"Ball (omega(Q1) >= omega(Q2)): {zus['ostwald_richtung_alle']}")
    return res, zz, {}


# ---------------------------------------------------------------- Chemie 11: Keimbildung im Reservoir

def lauf_keim(opt):
    wb2s = [0.60] if opt.rauch else KE_WB2
    laeufe = []
    for wb2 in wb2s:
        for off in KE_OFF:
            laeufe.append({"wb2": wb2, "off": off, "gamma": KE_GAMMA})
        for off in KE_KONTROLLE:
            laeufe.append({"wb2": wb2, "off": off, "gamma": 0.0})
    w2_liste = sorted(set(round(l["wb2"] + l["off"], 4) for l in laeufe))
    fam = familie([(w2, 3, 0) for w2 in w2_liste], H3, opt, "keim h")
    kenn = [profil_kenn(fam, i)[0] for i in range(len(w2_liste))]
    for l in laeufe:
        l["w2"] = round(l["wb2"] + l["off"], 4)
        l["zeile"] = w2_liste.index(l["w2"])
        k = kenn[l["zeile"]]
        l["Q_profil"], l["R_halb"], l["gueltig"] = k["Q"], k["R_halb"], k["gueltig"]
        l["kappa_vorh"] = l["gamma"] * (math.sqrt(l["wb2"]) / math.sqrt(l["w2"]) - 1.0)
    t_end = KE_T * (0.05 if opt.rauch else 1.0)
    gam = torch.tensor([[l["gamma"]] for l in laeufe], dtype=F64, device=DEV)
    omb = torch.tensor([[math.sqrt(l["wb2"])] for l in laeufe], dtype=F64, device=DEV)
    tst = torch.full_like(gam, INF)

    def bauen(r):
        felder = [ball_radial(fam, l["zeile"], r) for l in laeufe]
        return torch.stack([a for a, _ in felder]), torch.stack([b for _, b in felder])

    stufen = stufen_radial("keim", bauen, t_end, KE_MESS, gam, omb, tst)
    erg = {s: (auswertung_keim(laeufe, st) if st is not None else None) for s, st in stufen.items()}
    krit = []
    for wb2 in wb2s:
        i0 = w2_liste.index(round(wb2, 4))
        k0 = kenn[i0]
        eintrag = {"omega_b2": wb2, "R_halb_omega_b": k0["R_halb"], "Q_omega_b": k0["Q"],
                   "R_CNT_sigma_inf": teilen(2.0 * SIGMA_INF, p_bulk_von(wb2)),
                   "R_YL_eigen": teilen(2.0 * k0["sigma"], k0["P_in"])}
        for s in ("grob", "fein"):
            eintrag["R_c_dyn_" + s], eintrag["richtung_" + s] = (kritischer_radius(erg[s], wb2)
                                                                 if erg.get(s) is not None else (NAN, "-"))
        eintrag["R_CNT_durch_R_c_dyn"] = teilen(eintrag["R_CNT_sigma_inf"], eintrag["R_c_dyn_grob"])
        eintrag["R_halb_durch_R_c_dyn"] = teilen(eintrag["R_halb_omega_b"], eintrag["R_c_dyn_grob"])
        krit.append(eintrag)
    l3_liste = []
    if erg.get("fein") is not None:
        for zg, zf in zip(erg["grob"], erg["fein"]):
            if zg["gamma"] > 0.0 and zg["omega2_start"] != zg["omega_b2"]:
                l3_liste.append({"was": f"omega_b^2={zg['omega_b2']} start {zg['omega2_start']}",
                                 "kappa": l3(zg["kappa"], zf["kappa"], 0.0)})
    res = {"laeufe": laeufe, "profile": kenn, "ergebnis": erg, "kritisch": krit, "L3": l3_liste,
           "sek": {s: (st["sek"] if st else None) for s, st in stufen.items()}, "sek_schiessen": fam["sek"]}
    zz = [f"Chemie 11 Keimbildung: Ball im Reservoir -gamma (psi_t + i omega_b psi), gamma = {KE_GAMMA}; "
          "kappa = d ln Q/dt in [T/8, T/2]; Vorhersage fuer einen stationaeren Ball kappa = gamma (omega_b/omega - 1).",
          "  omega_b^2 | Start omega^2 | gamma | R_halb | Q_0 | Q_T/Q_0 | kappa | kappa_vorh | kappa/vorh | Klasse"]
    for s in ("grob", "fein"):
        e = erg.get(s)
        if e is None:
            zz.append(f"  [{s}] entfaellt")
            continue
        zz.append(f"  [{s}]")
        for z in e:
            zz.append(f"  {z['omega_b2']:.2f} | {z['omega2_start']:.3f} | {z['gamma']:.2f} | {fz(z['R_halb_start'], '.3f')} | "
                      f"{fz(z['Q_0'], '.5e')} | {fz(z['Q_T_durch_Q_0'], '.5f')} | {fz(z['kappa'], '+.3e')} | "
                      f"{fz(z['kappa_vorh'], '+.3e')} | {fz(z['kappa_durch_vorh'], '.3f')} | {z['klasse']}")
    zz.append("  Kritischer Radius: omega_b^2 | R_c dynamisch grob (fein) | R_halb(omega_b) | R_CNT = 2 sigma_inf/P_bulk | "
              "R_YL eigen = 2 sigma/P_in | R_CNT/R_c | R_halb/R_c")
    for k in krit:
        zz.append(f"  {k['omega_b2']:.2f} | {fz(k['R_c_dyn_grob'], '.3f')} ({fz(k['R_c_dyn_fein'], '.3f')}, "
                  f"{k['richtung_grob']}) | {fz(k['R_halb_omega_b'], '.3f')} | {fz(k['R_CNT_sigma_inf'], '.3f')} | "
                  f"{fz(k['R_YL_eigen'], '.3f')} | {fz(k['R_CNT_durch_R_c_dyn'], '.4f')} | "
                  f"{fz(k['R_halb_durch_R_c_dyn'], '.4f')}")
    n_ok = sum(1 for e in l3_liste if e["kappa"]["bestanden"])
    zz.append(f"  L3 fuer kappa (grob gegen fein): {n_ok} von {len(l3_liste)} bestanden")
    return res, zz, reihen_von(stufen, laeufe)


def auswertung_keim(laeufe, st):
    t, d = st["t"], st["daten"]
    T = gf(t[-1])
    i1, i2 = index_ab(t, T / 8.0), index_ab(t, T / 2.0)
    zeilen = []
    for b, l in enumerate(laeufe):
        q = d[:, b, 0]
        lq = torch.log(q.clamp(min=1e-300))
        kappa = teilen(gf(lq[i2] - lq[i1]), gf(t[i2] - t[i1]))
        verh = teilen(gf(q[-1]), gf(q[0]))
        klasse = "waechst" if verh > 1.001 else ("schrumpft" if verh < 0.999 else "bleibt")
        zeilen.append({"omega_b2": l["wb2"], "omega2_start": l["w2"], "gamma": l["gamma"], "R_halb_start": l["R_halb"],
                       "Q_0": gf(q[0]), "Q_T": gf(q[-1]), "Q_T_durch_Q_0": verh, "kappa": kappa,
                       "kappa_ende": teilen(gf(lq[-1] - lq[i1]), gf(t[-1] - t[i1])), "kappa_vorh": l["kappa_vorh"],
                       "kappa_durch_vorh": teilen(kappa, l["kappa_vorh"]),
                       "S_c_T_durch_0": teilen(gf(d[-1, b, 3]), gf(d[0, b, 3])), "klasse": klasse})
    return zeilen


def kritischer_radius(zeilen, wb2):
    """Radius, bei dem kappa (mit Bad) das Vorzeichen wechselt; linear zwischen den Startbaellen. Erwartet:
    kleine Baelle schrumpfen (kappa < 0), grosse wachsen ("normal")."""
    pts = sorted((z["R_halb_start"], z["kappa"]) for z in zeilen
                 if z["omega_b2"] == wb2 and z["gamma"] > 0.0 and math.isfinite(z["R_halb_start"])
                 and math.isfinite(z["kappa"]))
    for (ra, ka), (rb, kb) in zip(pts[:-1], pts[1:]):
        if (ka < 0.0 <= kb) or (ka > 0.0 >= kb):
            return ra + (rb - ra) * (0.0 - ka) / (kb - ka), ("normal" if ka < 0.0 else "umgekehrt")
    return NAN, "kein Wechsel"


# ---------------------------------------------------------------- Chemie 18: magische Zahlen

def glatt_analyse(rows, rausch, schritt):
    """Monotonie je Ast, 4. Differenzen von E/Q entlang omega^2 (lueckenlose Fenster), erster Hauptsatz dE/dQ = omega,
    Virialschranke E/Q > omega, Q_min und Q_abs."""
    rows = sorted(rows, key=lambda z: z["omega2"])
    n = len(rows)
    aus = {"n": n}
    if n < 3:
        return aus
    duenn, dick, i_min = aeste(rows)
    aus["Q_min"], aus["omega2_Qmin"] = q_min_parabel(rows)
    aus["Q_abs"], aus["omega2_Qabs"] = q_abs_duenn(duenn)
    aus["monotonie_verstoesse_duenn"] = monotonie_verstoesse(duenn)
    aus["monotonie_verstoesse_dick"] = monotonie_verstoesse(dick)
    d4 = []
    for i in range(2, n - 2):
        w = [rows[i + k]["omega2"] for k in range(-2, 3)]
        if all(abs((w[k + 1] - w[k]) - schritt) < 1e-9 for k in range(4)):
            y = [rows[i + k]["E_zu_Q"] for k in range(-2, 3)]
            d4.append((rows[i]["omega2"], y[0] - 4.0 * y[1] + 6.0 * y[2] - 4.0 * y[3] + y[4]))
    werte = [abs(v) for _, v in d4]
    aus["d4_median"] = median(werte)
    aus["d4_max"] = max(werte, default=NAN)
    aus["d4_groesste"] = [{"omega2": w2, "d4": v} for w2, v in sorted(d4, key=lambda p: -abs(p[1]))[:3]]
    auff = []
    for j, (w2, v) in enumerate(d4):
        ref = median([werte[k] for k in range(max(0, j - 8), min(len(werte), j + 9)) if abs(k - j) > 2])
        if math.isfinite(ref) and abs(v) > 10.0 * ref and abs(v) > 20.0 * rausch:
            auff.append({"omega2": w2, "d4": v, "nachbar_median": ref})
    aus["auffaellig"] = auff
    res = []
    for i in range(1, n - 1):
        if abs(i - i_min) <= 1:
            continue
        dq = rows[i + 1]["Q"] - rows[i - 1]["Q"]
        if dq != 0.0:
            res.append(abs((rows[i + 1]["E"] - rows[i - 1]["E"]) / dq / math.sqrt(rows[i]["omega2"]) - 1.0))
    aus["hauptsatz_median"] = median(res)
    aus["hauptsatz_max"] = max(res, default=NAN)
    aus["E_zu_Q_minus_omega_min"] = min(z["E_zu_Q"] - math.sqrt(z["omega2"]) for z in rows)
    return aus


def lauf_magisch(opt):
    w2_0 = [round(0.51 + 0.04 * i, 2) for i in range(13)] if opt.rauch else MA_W2
    w2_n = [0.70, 0.80, 0.90] if opt.rauch else MA_W2_N
    schritt_0, schritt_n = (0.04, 0.1) if opt.rauch else (0.005, 0.02)
    zeilen = [(w2, 3, 0) for w2 in w2_0] + [(w2, 3, 1) for w2 in w2_n] + [(w2, 3, 2) for w2 in w2_n]
    fam = familie(zeilen, H3, opt, "magisch h")
    fam_f = fam if opt.rauch else familie([(w2, 3, 0) for w2 in w2_0], H3 * FEIN, opt, "magisch h/2")
    tab = [fam_zeile(fam, i) for i in range(len(zeilen))]
    tab_f = [fam_zeile(fam_f, i) for i in range(len(w2_0))]
    paare = [(a, b) for a, b in zip(tab[:len(w2_0)], tab_f) if a["gueltig"] and b["gueltig"]]
    rausch = max((abs(a["E_zu_Q"] - b["E_zu_Q"]) for a, b in paare), default=NAN)
    rausch_q = max((abs(a["Q"] / b["Q"] - 1.0) for a, b in paare), default=NAN)
    fam_ana = {}
    for kn in (0, 1, 2):
        rows = [z for z in tab if z["knoten"] == kn and z["gueltig"]]
        fam_ana[kn] = glatt_analyse(rows, rausch if math.isfinite(rausch) else 0.0, schritt_0 if kn == 0 else schritt_n)
    duenn0, _, _ = aeste([z for z in tab if z["knoten"] == 0 and z["gueltig"]])
    kreuz = []
    for z in tab:
        if z["knoten"] > 0 and z["gueltig"]:
            e0 = z["Q"] * e_zu_q_duenn(duenn0, z["Q"])
            kreuz.append({"knoten": z["knoten"], "omega2": z["omega2"], "Q": z["Q"], "E": z["E"], "E0": e0,
                          "dE": z["E"] - e0})
    zus = {"rausch_E_zu_Q_h_gegen_h2": rausch, "rausch_Q_rel": rausch_q,
           "kreuzungen_E_n_unter_E_0": sum(1 for k in kreuz if math.isfinite(k["dE"]) and k["dE"] < 0.0),
           "vergleiche": sum(1 for k in kreuz if math.isfinite(k["dE"]))}
    res = {"tabelle": tab, "tabelle_h2": tab_f, "familien": fam_ana, "kreuzvergleich": kreuz, "zusammen": zus,
           "sek": {"h": fam["sek"], "h2": fam_f["sek"]}}
    zz = [f"Chemie 18 magische Zahlen: E/Q(Q) fuer n = 0 ({len(w2_0)} omega^2, Schritt {schritt_0}) und n = 1, 2 "
          f"({len(w2_n)} omega^2). Rauschen |E/Q(h) - E/Q(h/2)| max {fz(rausch, '.1e')}, |Q(h)/Q(h/2) - 1| max "
          f"{fz(rausch_q, '.1e')}" + (" (Rauchtest: h/2 = h)" if opt.rauch else "")]
    for kn in (0, 1, 2):
        a = fam_ana[kn]
        if a.get("n", 0) < 3:
            zz.append(f"  n = {kn}: nur {a.get('n', 0)} gueltige Profile, keine Analyse")
            continue
        zz.append(f"  n = {kn}: {a['n']} Profile; Q_min {fz(a['Q_min'], '.4f')} bei omega^2 {fz(a['omega2_Qmin'], '.4f')}; "
                  f"Q_abs (E = Q) {fz(a['Q_abs'], '.3f')}; Monotonie-Verstoesse duenn {a['monotonie_verstoesse_duenn']}, "
                  f"dick {a['monotonie_verstoesse_dick']}; |d4 E/Q| Median {fz(a['d4_median'], '.1e')}, max "
                  f"{fz(a['d4_max'], '.1e')}; auffaellig {len(a['auffaellig'])}; dE/dQ = omega Median "
                  f"{fz(a['hauptsatz_median'], '.1e')}, max {fz(a['hauptsatz_max'], '.1e')}; min (E/Q - omega) "
                  f"{fz(a['E_zu_Q_minus_omega_min'], '.3e')}")
        for p in a["auffaellig"]:
            zz.append(f"    auffaellig bei omega^2 = {p['omega2']}: d4 {p['d4']:+.2e} (Nachbarn {p['nachbar_median']:.1e})")
        zz.append("    groesste |d4|: " + ", ".join(f"{p['omega2']} ({p['d4']:+.1e})" for p in a["d4_groesste"]))
    zz.append(f"  Angeregte unter dem Grundzustand gleicher Ladung (Kreuzung der Familien): "
              f"{zus['kreuzungen_E_n_unter_E_0']} von {zus['vergleiche']} Vergleichen")
    return res, zz, {}


# ---------------------------------------------------------------- Rauchtest und Hauptprogramm

def lauf_rauch(opt):
    teile, fehler, zz = {}, {}, []
    for name in ("fitness", "membran", "magisch", "mutanten", "keim", "tod"):
        t0 = uhr()
        try:
            res, text, _ = LAEUFE[name](opt)
            teile[name] = res
            zz += text
        except Exception:
            fehler[name] = traceback.format_exc()
            zz += [f"{name} FEHLER:", fehler[name]]
            print(fehler[name], flush=True)
        zz += [f"  Rauchtest {name}: {uhr() - t0:.1f} s", ""]
    return {"teile": teile, "fehler_teile": fehler}, zz, {}


LAEUFE = {"membran": lauf_membran, "tod": lauf_tod, "mutanten": lauf_mutanten, "fitness": lauf_fitness,
          "keim": lauf_keim, "magisch": lauf_magisch, "rauch": lauf_rauch}


def schreiben(out, name, ausgabe, text, reihen):
    with open(os.path.join(out, f"r5a_{name}_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    with open(os.path.join(out, f"r5a_{name}_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)
    if reihen:
        torch.save(reihen, os.path.join(out, f"r5a_{name}_zeitreihen.pt"))


def main():
    global DEV
    ap = argparse.ArgumentParser(description="Runde 5, Paket R5-A: sechs Q-Ball-Ideen in 3D radial")
    ap.add_argument("unterbefehl", choices=sorted(LAEUFE))
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None, help="Ausgabeordner (Voreinstellung ausgabe-<unterbefehl> neben dem Skript)")
    ap.add_argument("--tabelle", default=os.path.join(HIER, "eingabe", "tests1d_ergebnis_runde2.json"),
                    help="Q(omega)-Tabelle fuer fitness (tests1d_ergebnis.json aus Runde 2)")
    ap.add_argument("--kand", type=int, default=None, help="Kandidaten je Schiessrunde (cuda 1024, cpu 256)")
    ap.add_argument("--runden", type=int, default=None, help="Schiessrunden (cuda 4, cpu 5)")
    ap.add_argument("--faeden", type=int, default=1, help="Torch-Faeden auf der CPU (kleintest.sh: CPUQuota 100 %%)")
    opt = ap.parse_args()
    if opt.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("Kein CUDA-Geraet sichtbar: auf einer cpu-Spur mit --geraet cpu starten.")
        DEV = torch.device("cuda")
        gesamt = torch.cuda.get_device_properties(0).total_memory
        torch.cuda.set_per_process_memory_fraction(min(1.0, SPEICHER_GB * 2 ** 30 / gesamt))
        geraet = torch.cuda.get_device_name(0)
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(max(1, opt.faeden))
        geraet = f"CPU, {torch.get_num_threads()} Faden"
    opt.rauch = opt.unterbefehl == "rauch"
    if opt.kand is None:
        opt.kand = N_KAND3 if DEV.type == "cuda" else 256
    if opt.runden is None:
        opt.runden = RUNDEN3 if DEV.type == "cuda" else 5
    if opt.rauch:
        opt.runden = min(opt.runden, 2)
    out = opt.out or os.path.join(HIER, "ausgabe-" + opt.unterbefehl)
    os.makedirs(out, exist_ok=True)
    T_START[0] = uhr()
    start = jetzt()
    kopf = (f"Runde 5 R5-A {opt.unterbefehl} Start {start} auf {geraet}, torch {torch.__version__}, Schiessen "
            f"{opt.kand} x {opt.runden}")
    print(kopf, flush=True)
    ausgabe = {"start": start, "geraet": geraet, "torch": torch.__version__, "unterbefehl": opt.unterbefehl,
               "kand": opt.kand, "runden": opt.runden, "ergebnis": None, "fehler": None}
    text = [kopf, ""]
    reihen = {}
    try:
        res, zz, reihen = LAEUFE[opt.unterbefehl](opt)
        ausgabe["ergebnis"] = res
        text += zz
        if opt.rauch and res["fehler_teile"]:
            ausgabe["fehler"] = sorted(res["fehler_teile"])
    except Exception:
        ausgabe["fehler"] = traceback.format_exc()
        text += ["FEHLER:", ausgabe["fehler"]]
        print(ausgabe["fehler"], flush=True)
    ausgabe["ende"] = jetzt()
    ausgabe["dauer_s"] = uhr() - T_START[0]
    speicher = torch.cuda.max_memory_allocated() / 2 ** 20 if DEV.type == "cuda" else NAN
    ausgabe["torch_speicher_max_mb"] = speicher
    text += ["", f"Ende {ausgabe['ende']}, Dauer {ausgabe['dauer_s']:.1f} s, Torch-Speicher max {fz(speicher, '.0f')} MB, "
                 f"Fehler: {'keine' if not ausgabe['fehler'] else 'ja (siehe oben)'}"]
    schreiben(out, opt.unterbefehl, ausgabe, text, reihen)
    print("\n".join(text), flush=True)
    if ausgabe["fehler"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
