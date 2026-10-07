#!/usr/bin/env python3
"""Runde 5/6 (v3), Paket 2D-B (Kollektiv und Kristall): Q-Ball-Karten mit vielen Baellen in 2D, Ein-Feld-Modell.

Karten (Auftrag RUNDE-06/AUFTRAG-MEDIUM-UND-2D-B.md, Abschnitt "Agent B"; Plan, Vorhersagen, Aufrufe in PLAN.md daneben):
    profile      Wellen 19   Auge des Tornados: m = 1-Profile bei sieben omega^2, Kernradius gegen Q (nur Schiessen).
                             Schiesst zugleich alle Profile der uebrigen Karten und legt sie im Zwischenspeicher ab.
    paare        Grundlage   Paarkraft und Paarbindung in 2D: Ueberlagerungsenergie E(d, dphi) ohne Zeitentwicklung,
                             dazu Paare (gleich-, quer-, gegenphasig) in der Zeit
    gitter       Bio 25/42, Chemie 13   Quadrat- und Dreiecksgitter aus 9 bis 16 Baellen mit Phasenmustern
    ringe        Bio 46, Chemie 19      Ringe aus N = 5 bis 8 Baellen mit Phasenstufe 2 pi k/N, ruhend und drehend
    gluehwurm    Bio 11      Ring aus 8 Baellen mit leicht verschiedenem omega, Zufallsphasen, angeregter Atmung
    haendigkeit  Bio 47      Gitter aus m = +1- und m = -1-Baellen, exakte Spiegelbilder, Zufallsmischungen
    isomere      Chemie 5    drei Baelle als Kette, geknickte Kette, Dreieck: Bindungsenergie, Umwandlung
    kollektiv    Bio 26/40   zwoelf verstreute Baelle, ruhend (Schleimpilz) bzw. mit Zufallsgeschwindigkeit (Schwarm)
    alle         nur mit --rauch: alle Karten nacheinander

Explorativ. Modell (Atlas-Normierung wie tests2d_r3.py, d = 2):
    L = |psi_t|^2 - |grad psi|^2 - U(S),  S = |psi|^2,  U(S) = S - S^2 + S^3/2.
    Ladungsdichte rho = 2 Im(psi conj(psi_t)), Energiedichte |psi_t|^2 + |grad psi|^2 + U(S),
    Impulsdichte p_i = -2 Re(conj(psi_t) d_i psi), Drehimpuls J = Int (x p_y - y p_x); fuer f e^{i m theta - i omega t}
    gilt J = m Q.

Grundlage: RUNDE-05/r5-2d-a/r5_2d_a.py (dort aus RUNDE-03/tests2d-r3/tests2d_r3.py): Schiessen mit der fuer |m| >= 1
berichtigten Unterschussregel (ln p eingeschachtelt), Radialtabelle, Hermite-Interpolation, periodisches Gitter,
spektraler Laplace, Velocity-Verlet, Randschicht, bewegter Ball fuer beliebiges m, Gebietsanalyse (Klumpen) mit
Windungszahl. Unveraendert uebernommen bis auf:
    1. Zwischenspeicher der Profile auf der Platte (--out/profil_cache.pt), damit nicht jeder Aufruf 1 bis 2 min schiesst.
    2. Ball-Verfolger: je Ball ein Fenster (Radius R_halb + 2,5) um den letzten Ort; Ort (Gewicht S^2), Ladung, innere
       Phase arg(Sum psi S), Radius R_rms, S_max, alle T_MEAS.
    3. Klumpen: Schwelle 0,5 x Anfangsmaximum der geglaetteten Dichte (wie 2D-A), Mindestladung 0,25 Q_1 (Einzelball,
       statt 3 % der Boxladung, sonst fielen bei 16 Baellen Einzelbaelle heraus); dazu Klumpenphase.
    4. "Dichte Ladung" Q_dicht: Ladung im Gebiet geglaettetes S > 0,1 x Anfangsmaximum; abgestrahlt = 1 - Q_dicht/Q_Box(0).
    5. Rohdaten jeder Stufe werden sofort nach der Zeitentwicklung gesichert (<karte>_<stufe>_roh.pt).

Aufruf:  python r5_2d_b.py KARTE [--rauch [--mini]] [--stufe grob|fein|beide] [--out ORDNER] [--geraet cuda|cpu]
Rauchtest: --rauch (Laufzeiten x 0,05; Zahlen ungueltig, nur Durchlauf und Hochrechnung).
Formprobe: --rauch --mini (256 Kandidaten, dx 0,6/0,4, Laufzeiten x 0,02); nur damit ist --geraet cpu erlaubt.
"""
import argparse
import cmath
import datetime
import json
import math
import os
import random
import time
import traceback

import torch

DEV = torch.device("cuda")
F64 = torch.float64
C128 = torch.complex128

# ---- Aus r5_2d_a.py / tests2d_r3.py unveraendert ----
H_ODE = 0.01
X_ODE = 60.0
N_KAND, RUNDEN = 2048, 5
SCHWANZ = 1e-3
SPONGE, SIGMA0 = 8.0, 1.0
STUFEN = (("grob", 0.3, 0.05), ("fein", 0.2, 0.025))
RAUCH_FAKTOR = 0.05
R_TAB = 100.0
BLUR = 1.0
SCHWELLE_REL = 0.5
N_THETA = 128
DAUER_K = 3

# ---- Gemeinsam, neu (vor dem Lauf festgelegt, PLAN.md Abschnitt 1) ----
W2_STD = 0.70            # Standardball m = 0: R_halb 1,92, Q 24,0 (R3-Profil)
SPALT = 4.0              # Luecke zwischen den Halbwertsradien benachbarter Baelle: Abstand d = 2 R_halb + SPALT
T_MEAS = 1.0
ANALYSE_DT = 5.0
Q_KLUMPEN = 0.25         # Klumpen zaehlt ab 0,25 Q_1
S_DICHT_REL = 0.1        # dichte Ladung: geglaettetes S > 0,1 x Anfangsmaximum
R_WIN_PLUS = 2.5         # Verfolgerfenster min(R_halb + 2,5; 0,4 d_NN), damit sich Nachbarfenster nicht ueberlappen
RAND_ABSTAND = 2.0       # Auswertefenster endet, wenn ein Klumpen weniger als SPONGE + 2 vom Rand entfernt ist
GOLD = 2.39996           # goldener Winkel (wie tests1d.py): feste "Zufalls"phasen

# Wellen 19 und Profilzwischenspeicher
W19_W2 = (0.52, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80)

# paare
P_L, P_T, P_MESS = 38.4, 400.0, 0.5
P_LAEUFE = (("gleich_s4", 0.0, 4.0), ("gleich_s5", 0.0, 5.0), ("gleich_s7", 0.0, 7.0), ("quer_s4", 0.5 * math.pi, 4.0),
            ("gegen_s4", math.pi, 4.0), ("gegen_s5", math.pi, 5.0), ("einzel", None, 4.0))
P_FEIN = ("gleich_s4", "quer_s4", "gegen_s4")
P_FIT = (1.0, 10.0)      # Fitfenster fuer die Anfangsbeschleunigung des Abstands (vor dem Verschmelzen)
P_FIT_Q = (0.5, 5.0)     # Fitfenster fuer den Anfangsstrom dQ/dt (Josephson)
P_STAT_SPALT = tuple(1.0 + 0.5 * j for j in range(19))      # 1,0 ... 10,0
P_STAT_PHASEN = (0.0, 0.5 * math.pi, math.pi)

# gitter
G_L, G_T = 48.0, 400.0
G_LAEUFE = (("Q3_gleich", "quadrat", 3, "gleich"), ("Q3_wechsel", "quadrat", 3, "wechsel"),
            ("Q4_gleich", "quadrat", 4, "gleich"), ("Q4_wechsel", "quadrat", 4, "wechsel"),
            ("Q4_windung", "quadrat", 4, "windung"), ("Q4_zufall", "quadrat", 4, "zufall"),
            ("D16_gleich", "dreieck", 4, "gleich"), ("D16_streifen", "dreieck", 4, "streifen"),
            ("D16_drei", "dreieck", 4, "drei"), ("D16_windung", "dreieck", 4, "windung"),
            ("Q4_gleich_s7", "quadrat", 4, "gleich", 7.0), ("Q4_wechsel_s7", "quadrat", 4, "wechsel", 7.0))
G_FEIN = ("Q4_gleich", "Q4_wechsel", "Q4_windung", "D16_streifen", "D16_drei")
G_SEED = 20260930

# ringe (Kapsid, Aromatizitaet)
R_L, R_T = 48.0, 500.0
R_LAEUFE = (("N6_k0", 6, 0, 0), ("N6_k1", 6, 1, 0), ("N6_k2", 6, 2, 0), ("N6_k3", 6, 3, 0),
            ("N5_k1", 5, 1, 0), ("N7_k1", 7, 1, 0), ("N8_k1", 8, 1, 0),
            ("N6_k1_dreh+", 6, 1, 1), ("N6_k1_dreh-", 6, 1, -1), ("N6_k0_dreh+", 6, 0, 1), ("N8_k1_dreh+", 8, 1, 1))
R_FEIN = ("N6_k0", "N6_k1", "N6_k3", "N8_k1", "N6_k1_dreh+")

# gluehwurm
GW_L, GW_T, GW_MESS = 57.6, 1000.0, 0.5
GW_DW2 = (-0.005, 0.010, 0.0, -0.010, 0.005, -0.0025, 0.0075, -0.0075)   # omega^2 = 0,70 + d, feste Reihenfolge
GW_EPS = 0.05            # Atmung: r -> r (1 + eps cos beta), psi_t -> -i omega (1 + eps sin beta) psi
GW_LAEUFE = (("nah_zufall_atem", 4.0, "zufall", True), ("nah_zufall", 4.0, "zufall", False),
             ("nah_gleich_atem", 4.0, "gleich", True), ("nah_wechsel_atem", 4.0, "wechsel", True),
             ("mittel_zufall_atem", 6.0, "zufall", True), ("weit_zufall_atem", 22.0, "zufall", True))
GW_FEIN = ("nah_zufall_atem",)
GW_KONTROLLE = "weit_zufall_atem"
R_SYNC = 0.9

# haendigkeit
H_W2, H_L, H_T = 0.55, 57.6, 400.0
H_FEIN = ("plus9", "misch_a")

# isomere
I_L, I_T = 38.4, 400.0
I_LAEUFE = (("kette_gleich", 180.0, (0.0, 0.0, 0.0)), ("kette_wechsel", 180.0, (0.0, math.pi, 0.0)),
            ("knick_gleich", 150.0, (0.0, 0.0, 0.0)), ("knick_wechsel", 150.0, (0.0, math.pi, 0.0)),
            ("dreieck_gleich", 60.0, (0.0, 0.0, 0.0)), ("dreieck_wechsel", 60.0, (0.0, math.pi, 0.0)))
I_FEIN = tuple(l[0] for l in I_LAEUFE)

# kollektiv (Schleimpilz, Schwarm)
K_L, K_T = 48.0, 400.0
K_N, K_RSCHEIBE, K_V, K_SEED = 12, 18.0, 0.05, 26
K_LAEUFE = (("schleim_gleich", "gleich", False), ("schleim_zufall", "zufall", False),
            ("schwarm_zufall", "zufall", True), ("schwarm_gleich", "gleich", True))
K_FEIN = ("schleim_gleich", "schwarm_zufall")

_PROFILE = {}
CACHE = {"pfad": None}


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def geraet_name():
    return torch.cuda.get_device_name(0) if DEV.type == "cuda" else "CPU (nur Formprobe)"


def upot(s):
    return s - s * s + 0.5 * s ** 3


# ---------------------------------------------------------------- Profil durch Schiessen (aus r5_2d_a.py)

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
    s = p * p
    g = (a0 - 2.0 * s + 1.5 * s * s) * p
    ist_m0 = mm == 0.0
    m1 = mm.clamp(min=1.0)
    k2 = a0 / (4.0 * (m1 + 1.0))
    hm = torch.pow(torch.full_like(m1, h), m1)
    f = torch.where(ist_m0, p + 0.25 * g * h * h, p * hm * (1.0 + k2 * h * h))
    fp = torch.where(ist_m0, 0.5 * g * h, p * (hm / h) * (m1 + (m1 + 2.0) * k2 * h * h))
    return f, fp


def schiessen(w2_liste, m_liste):
    """Wie r5_2d_a.py: Ueberschuss f > f_top oder f < 0; Unterschuss f' > 0 unter der Talsohle nach dem ersten Abstieg;
    fuer |m| >= 1 wird ln p eingeschachtelt (1e-6 bis 10)."""
    w2 = torch.tensor(w2_liste, dtype=F64, device=DEV).unsqueeze(1)
    mm = torch.tensor([float(abs(m)) for m in m_liste], dtype=F64, device=DEV).unsqueeze(1)
    m2 = mm * mm
    ist_m0 = mm == 0.0
    a0 = 1.0 - w2
    f_top = torch.sqrt((2.0 + torch.sqrt(6.0 * w2 - 2.0)) / 3.0)
    f_tal = torch.sqrt((2.0 - torch.sqrt(6.0 * w2 - 2.0)) / 3.0)
    lo = torch.where(ist_m0, torch.full_like(w2, 1e-3), torch.full_like(w2, math.log(1e-6)))
    hi = torch.where(ist_m0, f_top, torch.full_like(w2, math.log(10.0)))
    stufen = torch.linspace(0.0, 1.0, N_KAND, dtype=F64, device=DEV)
    n_schritte = int(round(X_ODE / H_ODE))
    for _ in range(RUNDEN):
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


def profile_bauen(sch, r_max, streng=True):
    """Wie r5_2d_a.py (Schiessbahn, Tabellen f, f', Radialintegrale, innerer und aeusserer Halbwertsradius)."""
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
    j_cut = torch.zeros(p.shape, dtype=torch.long, device=DEV)
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
    if streng and bool(fehler.any()):
        raise RuntimeError("Schiessbahn verlaesst den Separatrixweg vor dem Schwanz")
    gueltig = (~fehler & fertig).squeeze(1)
    bf = torch.cat(bahn_f, dim=1)
    bfp = torch.cat(bahn_fp, dim=1)
    n_z = p.shape[0]
    J = int(math.ceil(r_max / H_ODE)) + 2
    j = torch.arange(J, device=DEV).unsqueeze(0).expand(n_z, J)
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
    wr = 2.0 * math.pi * r * H_ODE
    s_tab = tab_f * tab_f
    zentr = torch.where(r > 0.0, m2 * s_tab / (r * r).clamp(min=1e-300), torch.zeros_like(r))
    n_int = (s_tab * wr).sum(1)
    g_int = ((tab_fp * tab_fp + zentr) * wr).sum(1)
    v_int = (upot(s_tab) * wr).sum(1)
    w2 = sch["w2"].squeeze(1)
    w = torch.sqrt(w2)
    s_max, j_max = s_tab.max(dim=1)
    unter_halb = (j > j_max.unsqueeze(1)) & (s_tab < 0.5 * s_max.unsqueeze(1))
    j_h = unter_halb.to(torch.int64).argmax(dim=1)
    s1 = s_tab.gather(1, j_h.unsqueeze(1)).squeeze(1)
    s0 = s_tab.gather(1, (j_h - 1).clamp(min=0).unsqueeze(1)).squeeze(1)
    r_halb = ((j_h - 1).to(F64) + (s0 - 0.5 * s_max) / (s0 - s1)) * H_ODE
    ueber_halb = s_tab >= 0.5 * s_max.unsqueeze(1)
    j_in = ueber_halb.to(torch.int64).argmax(dim=1)
    si1 = s_tab.gather(1, j_in.unsqueeze(1)).squeeze(1)
    si0 = s_tab.gather(1, (j_in - 1).clamp(min=0).unsqueeze(1)).squeeze(1)
    r_kern = torch.where(j_in > 0, ((j_in - 1).to(F64) + (0.5 * s_max - si0) / (si1 - si0).clamp(min=1e-300)) * H_ODE,
                         torch.zeros_like(s_max))
    profile = []
    for i in range(n_z):
        q = 2.0 * w[i] * n_int[i]
        e = w2[i] * n_int[i] + g_int[i] + v_int[i]
        profile.append({
            "omega2": sch["w2_liste"][i], "m": sch["m"][i], "p": p[i, 0].item(), "klammer": sch["klammer"][i, 0].item(),
            "x_schwanz": r_cut[i, 0].item(), "f": tab_f[i], "fp": tab_fp[i],
            "N": n_int[i].item(), "G": g_int[i].item(), "VU": v_int[i].item(), "Q": q.item(), "E": e.item(),
            "virialrest": ((v_int[i] - w2[i] * n_int[i]) / (v_int[i] + w2[i] * n_int[i])).item(),
            "S_zentrum": s_tab[i, 0].item(), "S_max": s_max[i].item(), "R_halb": r_halb[i].item(),
            "R_kern_halb": r_kern[i].item(), "R_max": j_max[i].item() * H_ODE,
            "f_top": f_top[i, 0].item(), "gueltig": bool(gueltig[i]),
        })
    return profile


def profil_info(pr):
    return {k: v for k, v in pr.items() if k not in ("f", "fp")}


def cache_schluessel(w2, m):
    return f"{w2:.6f}|{m}|{H_ODE}|{X_ODE}|{N_KAND}|{RUNDEN}|{R_TAB}"


def profile_holen(liste):
    """Profile (omega2, m): erst Speicher, dann Plattencache (--out/profil_cache.pt), sonst ein Schiessdurchgang fuer alle
    fehlenden Zeilen zugleich; neue Profile werden in den Plattencache geschrieben (atomar ueber os.replace)."""
    liste = [(round(float(w2), 6), int(m)) for w2, m in liste]
    platte = {}
    if CACHE["pfad"] and os.path.exists(CACHE["pfad"]):
        try:
            platte = torch.load(CACHE["pfad"], map_location="cpu")
        except Exception as exc:                     # beschaedigter Cache: neu schiessen
            print(f"Profilcache nicht lesbar ({exc!r}), schiesse neu", flush=True)
            platte = {}
    for k in dict.fromkeys(liste):
        if k not in _PROFILE and cache_schluessel(*k) in platte:
            e = platte[cache_schluessel(*k)]
            _PROFILE[k] = {**e["info"], "f": e["f"].to(DEV), "fp": e["fp"].to(DEV)}
    fehlt = [k for k in dict.fromkeys(liste) if k not in _PROFILE]
    if fehlt:
        sch = schiessen([w2 for w2, _ in fehlt], [m for _, m in fehlt])
        for k, pr in zip(fehlt, profile_bauen(sch, R_TAB, streng=False)):
            _PROFILE[k] = pr
            platte[cache_schluessel(*k)] = {"info": profil_info(pr), "f": pr["f"].cpu(), "fp": pr["fp"].cpu()}
        if CACHE["pfad"]:
            os.makedirs(os.path.dirname(CACHE["pfad"]), exist_ok=True)
            tmp = CACHE["pfad"] + f".tmp{os.getpid()}"
            torch.save(platte, tmp)
            os.replace(tmp, CACHE["pfad"])
    return {k: _PROFILE[k] for k in liste}


def hermite(pr, r):
    tf, tfp = pr["f"], pr["fp"]
    u = r / H_ODE
    j = u.floor().clamp(0, tf.shape[0] - 2)
    t = (u - j).clamp(0.0, 1.0)
    j = j.long()
    f0, f1 = tf[j], tf[j + 1]
    d0, d1 = tfp[j] * H_ODE, tfp[j + 1] * H_ODE
    t2 = t * t
    t3 = t2 * t
    f = (2 * t3 - 3 * t2 + 1) * f0 + (t3 - 2 * t2 + t) * d0 + (-2 * t3 + 3 * t2) * f1 + (t3 - t2) * d1
    fp = ((6 * t2 - 6 * t) * f0 + (3 * t2 - 4 * t + 1) * d0 + (-6 * t2 + 6 * t) * f1 + (3 * t2 - 2 * t) * d1) / H_ODE
    return f, fp


# ---------------------------------------------------------------- Gitter, Felder, Zeitentwicklung

class Gitter:
    """Periodische Box [-L, L)^2 mit Randschicht (wie r5_2d_a.py); x_j = -L + j dx liegt spiegelsymmetrisch."""

    def __init__(self, L, dx):
        n = int(round(2.0 * L / dx))
        self.L, self.dx, self.n = L, dx, n
        x = -L + dx * torch.arange(n, dtype=F64, device=DEV)
        self.x = x.view(1, 1, n)
        self.y = x.view(1, n, 1)
        k = 2.0 * math.pi * torch.fft.fftfreq(n, d=dx, dtype=F64, device=DEV)
        self.kx = k.view(1, 1, n)
        self.ky = k.view(1, n, 1)
        self.minus_k2 = -(self.kx ** 2 + self.ky ** 2)
        tiefe = torch.maximum(self.x.abs(), self.y.abs())
        self.sigma = SIGMA0 * ((tiefe - (L - SPONGE)).clamp(min=0.0) / SPONGE) ** 2
        self.dA = dx * dx
        self.blur = torch.exp(0.5 * BLUR * BLUR * self.minus_k2)
        self.X2 = self.x.expand(1, n, n)[0].contiguous()
        self.Y2 = self.y.expand(1, n, n)[0].contiguous()


def winkelteil(f, r, X, Y, m, c):
    if m == 0:
        return f.to(C128)
    am = abs(m)
    sg = 1.0 if m > 0 else -1.0
    f_r = torch.where(r > 0.0, f / r.clamp(min=1e-300) ** am, torch.full_like(r, c))
    return f_r * (X + 1j * sg * Y) ** am


def ball_feld(g, pr, m=0, x0=0.0, y0=0.0, phase=0.0, eps_r=0.0, eps_w=0.0):
    """Ruhender Ball f(r) e^{i m theta + i phase - i omega t}; Atmung: r -> r (1 + eps_r), psi_t = -i omega (1 + eps_w) psi."""
    w = math.sqrt(pr["omega2"])
    X = g.x - x0
    Y = g.y - y0
    r = torch.sqrt(X * X + Y * Y)
    f, _ = hermite(pr, r * (1.0 + eps_r))
    psi = winkelteil(f, r, X, Y, m, pr["p"] * (1.0 + eps_r) ** abs(m)) * cmath.exp(1j * phase)
    return psi, -1j * w * (1.0 + eps_w) * psi


def ball_bewegt(g, pr, m, x0, y0, v, winkel, phase=0.0):
    """Wie r5_2d_a.py: Lorentz-geboosteter Ball (beliebiges m), d_par F spektral."""
    w = math.sqrt(pr["omega2"])
    gam = 1.0 / math.sqrt(1.0 - v * v)
    ca, sa = math.cos(winkel), math.sin(winkel)
    X = g.x - x0
    Y = g.y - y0
    xpar = X * ca + Y * sa
    Xs = X + (gam - 1.0) * xpar * ca
    Ys = Y + (gam - 1.0) * xpar * sa
    r = torch.sqrt(Xs * Xs + Ys * Ys)
    f, _ = hermite(pr, r)
    F = winkelteil(f, r, Xs, Ys, m, pr["p"])
    dF = torch.fft.ifft2(torch.fft.fft2(F) * (1j * (g.kx * ca + g.ky * sa)))
    welle = torch.exp(1j * (w * gam * v) * xpar) * cmath.exp(1j * phase)
    return F * welle, (-v * dF - 1j * (w * gam) * F) * welle


def summe_baelle(g, baelle):
    """baelle: Liste von dicts {pr, m, x, y, phase, [v, winkel], [eps_r, eps_w]}; Rueckgabe psi, psi_t (1, n, n)."""
    psi = torch.zeros((1, g.n, g.n), dtype=C128, device=DEV)
    vel = torch.zeros_like(psi)
    for b in baelle:
        if b.get("v", 0.0) != 0.0:
            p_, v_ = ball_bewegt(g, b["pr"], b.get("m", 0), b["x"], b["y"], b["v"], b["winkel"], b.get("phase", 0.0))
        else:
            p_, v_ = ball_feld(g, b["pr"], b.get("m", 0), b["x"], b["y"], b.get("phase", 0.0), b.get("eps_r", 0.0),
                               b.get("eps_w", 0.0))
        psi = psi + p_
        vel = vel + v_
    return psi, vel


def entwickeln(g, psi, vel, dt, t_end, t_mess, messen):
    """Velocity-Verlet (wie qg1.py) fuer einen Stapel (B, n, n); Laplace spektral; Randschicht psi_t -> psi_t e^{-sigma dt}.
    messen(psi, vel) gibt ein Tupel von Tensoren; Rueckgabe t und ein Tupel gestapelter Reihen."""
    daempf = torch.exp(-g.sigma * dt)
    mk2 = g.minus_k2

    def kraft(p):
        lap = torch.fft.ifft2(torch.fft.fft2(p) * mk2)
        s = p.real * p.real + p.imag * p.imag
        return lap - (1.0 + s * (1.5 * s - 2.0)) * p

    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(t_mess / dt)))
    reihen = [messen(psi, vel)]
    F = kraft(psi)
    for n in range(1, n_schritte + 1):
        vel.add_(F, alpha=0.5 * dt)
        psi.add_(vel, alpha=dt)
        F = kraft(psi)
        vel.add_(F, alpha=0.5 * dt)
        vel.mul_(daempf)
        if n % alle == 0:
            reihen.append(messen(psi, vel))
    daten = tuple(torch.stack([r[i] for r in reihen]) for i in range(len(reihen[0])))
    for d in daten:
        if not bool(torch.isfinite(d).all()):
            raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten[0].shape[0], dtype=F64, device=DEV) * (alle * dt)
    return t, daten


def dichten(g, psi, vel):
    s = psi.real ** 2 + psi.imag ** 2
    rho = 2.0 * (psi * vel.conj()).imag
    ph = torch.fft.fft2(psi)
    gx = torch.fft.ifft2(ph * (1j * g.kx))
    gy = torch.fft.ifft2(ph * (1j * g.ky))
    e = vel.real ** 2 + vel.imag ** 2 + gx.real ** 2 + gx.imag ** 2 + gy.real ** 2 + gy.imag ** 2 + upot(s)
    px = -2.0 * (vel.conj() * gx).real
    py = -2.0 * (vel.conj() * gy).real
    jz = g.x * py - g.y * px
    return s, rho, e, px, py, jz


def unschaerfe(g, a):
    return torch.fft.ifft2(torch.fft.fft2(a) * g.blur).real


def komponenten(maske):
    """Wie r5_2d_a.py: zusammenhaengende Gebiete, 4er-Nachbarschaft, periodisch; Minimum-Weitergabe plus Zeigersprung."""
    B, n, _ = maske.shape
    nn = n * n
    idx = torch.arange(nn, device=DEV, dtype=torch.int64).view(1, n, n).expand(B, n, n)
    aus = torch.full((B, n, n), nn, device=DEV, dtype=torch.int64)
    rand = torch.full((B, 1), nn, device=DEV, dtype=torch.int64)
    lab = torch.where(maske, idx, aus)
    for it in range(4 * n):
        alt = lab
        nb = torch.minimum(torch.minimum(lab.roll(1, 1), lab.roll(-1, 1)),
                           torch.minimum(lab.roll(1, 2), lab.roll(-1, 2)))
        lab = torch.where(maske, torch.minimum(lab, nb), aus)
        flach = torch.cat([lab.reshape(B, nn), rand], dim=1)
        lab = torch.where(maske, flach.gather(1, lab.reshape(B, nn)).view(B, n, n), aus)
        if it % 4 == 3 and torch.equal(lab, alt):
            break
    return lab


def windung_kreis(g, feld, xc, yc, rc):
    """Wie r5_2d_a.py: Phasenumlauf auf dem Kreis (bilinear), Rueckgabe Windung und kleinstes S auf dem Kreis."""
    th = torch.arange(N_THETA, dtype=F64, device=DEV) * (2.0 * math.pi / N_THETA)
    fx = (xc + rc * torch.cos(th) + g.L) / g.dx
    fy = (yc + rc * torch.sin(th) + g.L) / g.dx
    j0f, i0f = torch.floor(fx), torch.floor(fy)
    tx, ty = fx - j0f, fy - i0f
    j0, i0 = j0f.long() % g.n, i0f.long() % g.n
    j1, i1 = (j0 + 1) % g.n, (i0 + 1) % g.n
    w = ((1.0 - tx) * (1.0 - ty) * feld[i0, j0] + tx * (1.0 - ty) * feld[i0, j1]
         + (1.0 - tx) * ty * feld[i1, j0] + tx * ty * feld[i1, j1])
    ph = torch.angle(w)
    d = torch.remainder(ph.roll(-1) - ph + math.pi, 2.0 * math.pi) - math.pi
    return int(round(d.sum().item() / (2.0 * math.pi))), (w.real ** 2 + w.imag ** 2).min().item()


def klumpen(g, psi, dicht, maske, q_min, windung=False):
    """Gebiete der Maske je Lauf (wie analyse() in r5_2d_a.py) mit Ladung >= q_min[b]; neu: Klumpenphase arg(Sum psi S)."""
    s, rho, e, px, py, jz = dicht
    lab = komponenten(maske)
    alle = []
    for b in range(maske.shape[0]):
        mb = maske[b]
        if not bool(mb.any()):
            alle.append([])
            continue
        u, inv = torch.unique(lab[b][mb], return_inverse=True)
        k = int(u.shape[0])

        def summe(werte):
            return torch.zeros(k, dtype=F64, device=DEV).index_add_(0, inv, werte[mb])

        sw = summe(s[b])
        q = summe(rho[b]) * g.dA
        en = summe(e[b]) * g.dA
        X = summe(s[b] * g.X2) / sw
        Y = summe(s[b] * g.Y2) / sw
        ppx = summe(px[b]) * g.dA
        ppy = summe(py[b]) * g.dA
        jspin = summe(jz[b]) * g.dA - X * ppy + Y * ppx
        ph = torch.atan2(summe(psi[b].imag * s[b]), summe(psi[b].real * s[b]))
        abst = torch.sqrt((g.X2[mb] - X[inv]) ** 2 + (g.Y2[mb] - Y[inv]) ** 2)
        rbar = torch.zeros(k, dtype=F64, device=DEV).index_add_(0, inv, s[b][mb] * abst) / sw
        werte = torch.stack([q, en, X, Y, ppx, ppy, jspin, rbar, ph], dim=1).tolist()
        liste = []
        for qq, ee, xx, yy, pxx, pyy, js, rb, pp in werte:
            if qq < q_min:
                continue
            d = {"Q": qq, "E": ee, "X": xx, "Y": yy, "vx": pxx / ee, "vy": pyy / ee, "Jspin_Q": js / qq,
                 "r_mittel": rb, "phase": pp}
            if windung:
                d["windung"], d["S_min_kreis"] = windung_kreis(g, psi[b], xx, yy, rb)
                d["windung_sicher"] = d["S_min_kreis"] >= 0.05          # PLAN.md 1.3: sonst Windung unsicher
            liste.append(d)
        liste.sort(key=lambda d: -d["Q"])
        alle.append(liste)
    return alle


def verfolger(g, psi, vel, cx, cy, off, r_w):
    """Je Ball ein Fenster (Radius r_w) um den letzten Ort. Neuer Ort = Schwerpunkt mit Gewicht S^2; dazu Ladung, innere
    Phase arg(Sum psi S), R_rms (Gewicht S), S_max. cx, cy: (B, K). Rueckgabe cx, cy, Werte (B, K, 6)."""
    B, K = cx.shape
    n = g.n
    P = off.shape[0]
    i0x = torch.round((cx + g.L) / g.dx).long()
    i0y = torch.round((cy + g.L) / g.dx).long()
    jx = i0x.unsqueeze(-1) + off
    jy = i0y.unsqueeze(-1) + off
    flat = jy.remainder(n).unsqueeze(-1) * n + jx.remainder(n).unsqueeze(-2)          # (B, K, P, P)
    idx = flat.reshape(B, K * P * P, 1).expand(B, K * P * P, 2)
    pp = torch.view_as_complex(torch.view_as_real(psi).reshape(B, n * n, 2).gather(1, idx).contiguous()).view(B, K, P, P)
    vv = torch.view_as_complex(torch.view_as_real(vel).reshape(B, n * n, 2).gather(1, idx).contiguous()).view(B, K, P, P)
    xr = (jx.to(F64) * g.dx - g.L - cx.unsqueeze(-1)).unsqueeze(-2)                     # (B, K, 1, P)
    yr = (jy.to(F64) * g.dx - g.L - cy.unsqueeze(-1)).unsqueeze(-1)                     # (B, K, P, 1)
    r2 = xr * xr + yr * yr
    kreis = (r2 < r_w * r_w).to(F64)
    s = (pp.real ** 2 + pp.imag ** 2) * kreis
    w = s * s
    ws = w.sum((2, 3))
    da = ws > 1e-200
    dxc = torch.where(da, (w * xr).sum((2, 3)) / ws.clamp(min=1e-300), torch.zeros_like(ws))
    dyc = torch.where(da, (w * yr).sum((2, 3)) / ws.clamp(min=1e-300), torch.zeros_like(ws))
    rho = 2.0 * (pp * vv.conj()).imag * kreis
    qb = rho.sum((2, 3)) * g.dA
    zs = (pp * s).sum((2, 3))
    ph = torch.atan2(zs.imag, zs.real)
    ss = s.sum((2, 3)).clamp(min=1e-300)
    rb = torch.sqrt((s * r2).sum((2, 3)) / ss)
    smax = s.amax((2, 3))
    cx = cx + dxc
    cy = cy + dyc
    return cx, cy, torch.stack([cx, cy, qb, ph, rb, smax], dim=2)


def lauf(g, psi, vel, dt, t_end, zentren, r_w, q_min, t_mess=T_MEAS, windung=False):
    """Zeitentwicklung mit Messungen: je t_mess Q_Box, E_Box, J_Box, S_max und Verfolger je Ball; je ANALYSE_DT Klumpen und
    dichte Ladung. zentren: (B, K, 2). Rueckgabe t, glob (M, B, 4), bahn (M, B, K, 6), verlauf je Lauf [(t, Q_dicht, [..])]."""
    B, K, _ = zentren.shape
    cx = zentren[:, :, 0].clone()
    cy = zentren[:, :, 1].clone()
    w = int(math.ceil(r_w / g.dx)) + 1
    off = torch.arange(-w, w + 1, device=DEV)
    s0 = psi.real ** 2 + psi.imag ** 2
    s_ref = unschaerfe(g, s0).amax((1, 2))
    schwelle = (SCHWELLE_REL * s_ref).view(-1, 1, 1)
    schwelle_dicht = (S_DICHT_REL * s_ref).view(-1, 1, 1)
    verlauf = [[] for _ in range(B)]
    zaehler = [0]
    alle = max(1, int(round(ANALYSE_DT / t_mess)))

    def messen(psi, vel):
        nonlocal cx, cy
        dicht = dichten(g, psi, vel)
        s, rho, e, _, _, jz = dicht
        glob = torch.stack([rho.sum((1, 2)) * g.dA, e.sum((1, 2)) * g.dA, jz.sum((1, 2)) * g.dA, s.amax((1, 2))], dim=1)
        cx, cy, bahn = verfolger(g, psi, vel, cx, cy, off, r_w)
        if zaehler[0] % alle == 0:
            glatt = unschaerfe(g, s)
            q_dicht = ((rho * (glatt > schwelle_dicht)).sum((1, 2)) * g.dA).tolist()
            kl = klumpen(g, psi, dicht, glatt > schwelle, q_min, windung)
            for b in range(B):
                verlauf[b].append((zaehler[0] * t_mess, q_dicht[b], kl[b]))
        zaehler[0] += 1
        return glob, bahn

    t, (glob, bahn) = entwickeln(g, psi, vel, dt, t_end, t_mess, messen)
    return t, glob, bahn, verlauf


def stufe_rechnen(karte, stufe, dx, dt, L, t_end, laeufe, bauen, r_w, q_min, out, dauer, t_mess=T_MEAS, windung=False):
    """Baut alle Laeufe der Stufe (bauen(g, lauf) -> Liste von Ball-dicts), entwickelt sie als Stapel und sichert die
    Rohdaten sofort (<karte>_<stufe>_roh.pt). Rueckgabe g, t, glob, bahn, verlauf, Startorte je Lauf."""
    g = Gitter(L, dx)
    psis, vels, orte = [], [], []
    for lauf_ in laeufe:
        baelle = bauen(g, lauf_)
        p_, v_ = summe_baelle(g, baelle)
        psis.append(p_)
        vels.append(v_)
        orte.append([(b["x"], b["y"]) for b in baelle])
    K = max(len(o) for o in orte)
    zentren = torch.tensor([o + [o[0]] * (K - len(o)) for o in orte], dtype=F64, device=DEV)
    psi = torch.cat(psis).contiguous()
    vel = torch.cat(vels).contiguous()
    del psis, vels
    t0 = uhr()
    t, glob, bahn, verlauf = lauf(g, psi, vel, dt, t_end, zentren, r_w, q_min, t_mess, windung)
    dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
    print(f"{karte}: Entwicklung {stufe} ({len(laeufe)} Laeufe, n = {g.n}) fertig nach "
          f"{dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
    os.makedirs(out, exist_ok=True)
    torch.save({"t": t.cpu(), "glob": glob.cpu(), "bahn": bahn.cpu(), "verlauf": verlauf,
                "laeufe": [l[0] for l in laeufe], "orte": orte, "dx": dx, "dt": dt, "L": L,
                "spalten_glob": ["Q_box", "E_box", "J_box", "S_max"],
                "spalten_bahn": ["x", "y", "Q_ball", "phase", "R_rms", "S_max"]},
               os.path.join(out, f"{karte}_{stufe}_roh.pt"))
    return g, t, glob, bahn, verlauf, orte


# ---------------------------------------------------------------- Auswertehilfen

def polyfit(t, y, grad):
    if t.shape[0] < grad + 3:
        return None
    spanne = t[-1] - t[0]
    tau = (t - t[0]) / spanne
    a_mat = torch.stack([tau ** k for k in range(grad + 1)], dim=1)
    c = torch.linalg.lstsq(a_mat, y.unsqueeze(1)).solution.squeeze(1)
    rest = y - a_mat @ c
    s2 = (rest ** 2).sum() / max(a_mat.shape[0] - a_mat.shape[1], 1)
    se = torch.sqrt(torch.diagonal(torch.linalg.inv(a_mat.T @ a_mat)) * s2)
    return c, se, torch.sqrt((rest ** 2).mean()), spanne


def erste_dauerhaft(ts, flags, k=DAUER_K):
    for i in range(len(flags) - k + 1):
        if all(flags[i:i + k]):
            return ts[i]
    return None


def traegheitsradius(kl):
    qs = sum(k["Q"] for k in kl)
    if len(kl) < 2 or qs <= 0.0:
        return None
    xm = sum(k["Q"] * k["X"] for k in kl) / qs
    ym = sum(k["Q"] * k["Y"] for k in kl) / qs
    return math.sqrt(sum(k["Q"] * ((k["X"] - xm) ** 2 + (k["Y"] - ym) ** 2) for k in kl) / qs)


def nn_abstand(kl):
    if len(kl) < 2:
        return None
    return sum(min(math.hypot(a["X"] - b["X"], a["Y"] - b["Y"]) for j, b in enumerate(kl) if j != i)
               for i, a in enumerate(kl)) / len(kl)


def kenngroessen(verlauf_b, q0, L_rand):
    """Zeitreihen je Analyse: Klumpenzahl n, Traegheitsradius, mittlerer Naechster-Nachbar-Abstand, abgestrahlter Anteil
    1 - Q_dicht/Q_Box(0); t_rand = erste Analyse mit einem Klumpen naeher als SPONGE + RAND_ABSTAND am Rand."""
    kg = {"t": [], "n": [], "rg": [], "dnn": [], "frad": [], "t_rand": None}
    for t, q_dicht, kl in verlauf_b:
        if kg["t_rand"] is None and any(abs(k["X"]) > L_rand or abs(k["Y"]) > L_rand for k in kl):
            kg["t_rand"] = t
        kg["t"].append(t)
        kg["n"].append(len(kl))
        kg["rg"].append(traegheitsradius(kl))
        kg["dnn"].append(nn_abstand(kl))
        kg["frad"].append(1.0 - q_dicht / q0)
    return kg


def klasse_bestimmen(kg, T):
    """Ausgang nach PLAN.md 1.4 (vorab). Rangfolge: zerfallen > zerbrochen > verschmolzen > auseinander > halten > offen.
    Ausgewertet nur bis t_rand (danach kann Ladung in die Randschicht laufen)."""
    ts, n = kg["t"], kg["n"]
    idx = [i for i, t in enumerate(ts) if kg["t_rand"] is None or t < kg["t_rand"]]
    aus = {"t_ende_auswertung": ts[idx[-1]] if idx else None, "n_start": n[0] if n else None}
    if not idx:
        aus["klasse"] = "offen (Rand sofort)"
        return aus
    i_e = idx[-1]
    n0 = n[0]
    tw = [ts[i] for i in idx]
    aus["n_ende"] = n[i_e]
    aus["n_min"] = min(n[i] for i in idx)
    aus["n_max"] = max(n[i] for i in idx)
    aus["frad_ende"] = kg["frad"][i_e]
    # Plausibilitaetsschranke (Lehre R5): am Start muss die dichte Ladung fast die ganze Boxladung sein
    aus["frad_start"] = kg["frad"][0]
    aus["plausibel_start"] = -0.05 <= kg["frad"][0] <= 0.25
    aus["t_erste_verschmelzung"] = erste_dauerhaft(tw, [n[i] < n0 for i in idx])
    rg0, d0 = kg["rg"][0], kg["dnn"][0]
    rg_rel = [kg["rg"][i] / rg0 for i in idx if rg0 and kg["rg"][i] is not None and n[i] == n0]
    dnn_rel = [kg["dnn"][i] / d0 for i in idx if d0 and kg["dnn"][i] is not None and n[i] == n0]
    aus["rg_rel_max"] = max(rg_rel) if rg_rel else None
    aus["rg_rel_min"] = min(rg_rel) if rg_rel else None
    aus["dnn_rel_max"] = max(dnn_rel) if dnn_rel else None
    aus["dnn_rel_min"] = min(dnn_rel) if dnn_rel else None
    if n0 <= 1:
        aus["klasse"] = "ruhig" if all(n[i] == 1 for i in idx) and kg["frad"][i_e] < 0.2 else "unruhig"
        return aus
    if kg["frad"][i_e] >= 0.5:
        aus["klasse"] = "zerfallen"
    elif erste_dauerhaft(tw, [n[i] > n0 for i in idx]) is not None:
        aus["klasse"] = "zerbrochen"
    elif all(n[i] < n0 for i in idx[-DAUER_K:]):
        aus["klasse"] = "verschmolzen (ganz)" if n[i_e] == 1 else f"verschmolzen (teilweise, {n[i_e]} von {n0})"
    elif (rg_rel and max(rg_rel) >= 1.3) or (dnn_rel and max(dnn_rel) >= 1.3):
        aus["klasse"] = "auseinander"
    elif (all(n[i] == n0 for i in idx) and rg_rel and dnn_rel and all(0.85 <= x <= 1.15 for x in rg_rel + dnn_rel)
          and ts[i_e] >= 0.8 * T):
        aus["klasse"] = "halten"
    else:
        aus["klasse"] = "offen"
    return aus


def erhaltung(glob, b):
    return {"Q_box_verlust": (1.0 - glob[-1, b, 0] / glob[0, b, 0]).item(),
            "E_box_verlust": (1.0 - glob[-1, b, 1] / glob[0, b, 1]).item(),
            "J_box_start": glob[0, b, 2].item(), "J_box_ende": glob[-1, b, 2].item(),
            "Q_box_start": glob[0, b, 0].item(), "E_box_start": glob[0, b, 1].item()}


def klumpen_kurz(kl, windung=False):
    return [[round(k["Q"], 3), round(k["X"], 2), round(k["Y"], 2), round(k["vx"], 4), round(k["vy"], 4),
             round(k["phase"], 3)] + ([k["windung"], round(k["S_min_kreis"], 4)] if windung else []) for k in kl]


def verlauf_kurz(verlauf_b, windung=False, jede=4):
    """Fuer die JSON-Ausgabe jede 4. Analyse: [t, Q_dicht, [[Q, X, Y, vx, vy, Phase, (Windung, S_min)], ...]]."""
    return [[t, round(qd, 4), klumpen_kurz(kl, windung)] for i, (t, qd, kl) in enumerate(verlauf_b)
            if i % jede == 0 or i == len(verlauf_b) - 1]


def schreiben(out, name, ausgabe, text):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, name + "_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1)
    with open(os.path.join(out, name + "_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


def laufzeit_text(dauer, rauch):
    zeilen = ["Dauer [s]: " + ", ".join(f"{k} {s:.1f}" for k, s in dauer.items())]
    if rauch:
        entw = sum(s for k, s in dauer.items() if k.startswith("entw"))
        rest = sum(s for k, s in dauer.items() if not k.startswith("entw"))
        zeilen.append(f"Hochrechnung Hauptlauf: {rest + entw / RAUCH_FAKTOR:.0f} s (nicht entwickelnde Teile {rest:.0f} s "
                      f"+ Entwicklung x {1 / RAUCH_FAKTOR:.0f}); Schiessen entfaellt bei gefuelltem Profilcache. "
                      "Ueber 480 s: Stufen einzeln mit --stufe grob / --stufe fein starten.")
    return zeilen


def kopf(titel, start, rauch):
    return (f"{titel}. Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}"
            + (" RAUCHTEST: Zahlen ungueltig" if rauch else ""))


def fenster_r(pr, d_nn):
    """Verfolgerfenster: min(R_halb + 2,5; 0,4 d_NN), damit das Fenster nicht den Nachbarn erfasst."""
    return min(pr["R_halb"] + R_WIN_PLUS, 0.4 * d_nn)


def r_halb(pr):
    return pr["R_halb"]


def abstand(pr, spalt):
    return 2.0 * pr["R_halb"] + spalt


def wickeln(x):
    return (x + math.pi) % (2.0 * math.pi) - math.pi


def entfalten(ph):
    """Phasen (M, ...) entlang der Zeitachse entfalten."""
    d = torch.remainder(ph[1:] - ph[:-1] + math.pi, 2.0 * math.pi) - math.pi
    return torch.cat([ph[:1], ph[:1] + torch.cumsum(d, dim=0)], dim=0)


def schwuenge(x, h):
    """Zahl der Richtungswechsel einer Reihe mit Hub >= h (Hysterese; Rauschen unter h zaehlt nicht)."""
    n, r = 0, 0
    hi = lo = x[0]
    for v in x[1:]:
        if r == 0:
            if v >= lo + h:
                r, hi = 1, v
            elif v <= hi - h:
                r, lo = -1, v
            else:
                hi, lo = max(hi, v), min(lo, v)
        elif r == 1:
            if v > hi:
                hi = v
            elif v <= hi - h:
                r, lo, n = -1, v, n + 1
        else:
            if v < lo:
                lo = v
            elif v >= lo + h:
                r, hi, n = 1, v, n + 1
    return n


def fenster_idx(t, a, b):
    return ((t >= a - 1e-9) & (t <= b + 1e-9)).nonzero().flatten()


# ---------------------------------------------------------------- Liste aller Profile

def alle_profile():
    liste = [(w2, 1) for w2 in W19_W2] + [(w2, 0) for w2 in W19_W2]
    liste += [(round(W2_STD + d, 6), 0) for d in GW_DW2] + [(H_W2, 1)]
    return list(dict.fromkeys((round(w, 6), m) for w, m in liste))


# ---------------------------------------------------------------- Wellen 19: Auge des Tornados (nur Schiessen)

def test_profile(out, rauch, stufen, args):
    start = jetzt()
    print(f"Wellen 19 / Profile Start {start} auf {geraet_name()}", flush=True)
    t0 = uhr()
    prof = profile_holen(alle_profile())
    dauer = {"schiessen_oder_cache_s": uhr() - t0}
    zeilen = []
    for w2 in W19_W2:
        p1, p0 = prof[(w2, 1)], prof[(w2, 0)]
        z = {"omega2": w2, "m1": profil_info(p1), "m0_gueltig": p0["gueltig"]}
        if p0["gueltig"]:
            sc = p0["S_zentrum"]
            r_q = math.sqrt(p0["N"] / (math.pi * sc))
            p_c = w2 * sc - upot(sc)
            sig = p0["G"] / (math.pi * r_q)
            z["S_c"], z["p_c"], z["sigma_G"], z["R_Q_m0"] = sc, p_c, sig, r_q
            # Kapillarloch [S]: p a^2 + sigma a = S_c m^2 (m = 1); Heilungslaenge [S]: sqrt(2) xi = 1/sqrt(S_c U''(S_c))
            z["P_loch"] = (-sig + math.sqrt(sig * sig + 4.0 * p_c * sc)) / (2.0 * p_c) if p_c > 0 else sc / sig
            upp = sc * (3.0 * sc - 2.0)                    # S_c < 2/3 (dicke Baelle): keine Heilungslaenge
            z["P_heil"] = 1.0 / math.sqrt(upp) if upp > 0.0 else float("nan")
        zeilen.append(z)
    ok = [z for z in zeilen if z["m1"]["gueltig"] and z["m1"]["R_kern_halb"] > 0.0]

    def steigung(rows, schl):
        if len(rows) < 2:
            return None
        lq = torch.tensor([math.log(r["m1"]["Q"]) for r in rows], dtype=F64)
        lr = torch.tensor([math.log(r["m1"][schl]) for r in rows], dtype=F64)
        a = torch.stack([torch.ones_like(lq), lq], dim=1)
        return torch.linalg.lstsq(a, lr.unsqueeze(1)).solution[1, 0].item()

    gross = sorted(ok, key=lambda r: -r["m1"]["Q"])[:4]
    kenn = {"s_kern_alle": steigung(ok, "R_kern_halb"), "s_kern_4_groesste_Q": steigung(gross, "R_kern_halb"),
            "s_aussen_alle": steigung(ok, "R_halb"), "gueltige_m1_zeilen": len(ok)}
    abw_loch = [abs(r["m1"]["R_kern_halb"] / r["P_loch"] - 1.0) for r in ok if r.get("P_loch", 0.0) > 0.0]
    abw_heil = [abs(r["m1"]["R_kern_halb"] / r["P_heil"] - 1.0) for r in ok if r.get("P_heil", 0.0) > 0.0]
    kenn["abw_nur_beide_definiert"] = "Vergleich nur ueber Zeilen mit S_c > 2/3 (sonst keine Heilungslaenge)"
    abw_loch = [abs(r["m1"]["R_kern_halb"] / r["P_loch"] - 1.0) for r in ok
                if r.get("P_loch", 0.0) > 0.0 and r.get("P_heil", 0.0) > 0.0]
    kenn["mittlere_abw_P_loch"] = sum(abw_loch) / len(abw_loch) if abw_loch else None
    kenn["mittlere_abw_P_heil"] = sum(abw_heil) / len(abw_heil) if abw_heil else None
    s4 = kenn["s_kern_4_groesste_Q"]
    if s4 is None:
        urteil = "offen (zu wenige gueltige m = 1-Profile)"
    elif abs(s4) <= 0.10:
        urteil = "Kern von Q unabhaengig (Saettigung): Regel 'Auge waechst mit Q' scheitert bei grossen Q"
    elif s4 >= 0.35:
        urteil = "Kern waechst wie der Ball (Idee 19 getragen)"
    else:
        urteil = "Kern haengt schwach von Q ab (Zwischenbereich)"
    if kenn["mittlere_abw_P_loch"] is not None and kenn["mittlere_abw_P_heil"] is not None:
        urteil += ("; naeher am Kapillarloch" if kenn["mittlere_abw_P_loch"] < kenn["mittlere_abw_P_heil"]
                   else "; naeher an der Heilungslaenge")
    text = [kopf("Wellen 19 Auge des Tornados, m = 1-Profile (nur Schiessen)", start, False)]
    text += laufzeit_text(dauer, False)
    text.append("omega2 | Q(m=1) | E/Q | R_kern_halb | R_max | R_halb aussen | P_loch [S] | P_heil [S] | Virialrest | "
                "Klammer | gueltig")
    for z in zeilen:
        m1 = z["m1"]
        text.append(f"  {z['omega2']:.2f} | {m1['Q']:.3f} | {(m1['E'] / m1['Q'] if m1['Q'] else float('nan')):.5f} | "
                    f"{m1['R_kern_halb']:.3f} | {m1['R_max']:.3f} | {m1['R_halb']:.3f} | "
                    f"{z.get('P_loch', float('nan')):.3f} | {z.get('P_heil', float('nan')):.3f} | "
                    f"{m1['virialrest']:.1e} | {m1['klammer']:.1e} | {'ja' if m1['gueltig'] else 'NEIN'}")
    text.append("Alle Profile im Cache: omega2 m | Q | E | R_halb | Virialrest | gueltig")
    for k, pr in prof.items():
        text.append(f"  {k[0]:.4f} {k[1]} | {pr['Q']:.4f} | {pr['E']:.4f} | {pr['R_halb']:.3f} | "
                    f"{pr['virialrest']:.1e} | {'ja' if pr['gueltig'] else 'NEIN'}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    text.append("Urteil nach PLAN.md (Abschnitt 9): " + urteil)
    schreiben(out, "profile", {"karte": "Wellen 19", "start": start, "dauer_s": dauer, "zeilen": zeilen,
                               "alle": [profil_info(p) for p in prof.values()], "kennzahlen": kenn, "urteil": urteil},
              "\n".join(text))


# ---------------------------------------------------------------- Grundlage: Paare

def statik(g, pr, konfigs, stapel=16):
    """Ueberlagerungsenergie ohne Zeitentwicklung: je Konfiguration (Liste von Ball-dicts) E und Q des Startfelds.
    E_bind = E - k E_1 - omega (Q - k Q_1) mit Einzelball-Werten auf demselben Gitter (Bindung bei fester Ladung,
    erste Ordnung). Rueckgabe Liste E_bind und die Einzelwerte."""
    w = math.sqrt(pr["omega2"])
    p1, v1 = ball_feld(g, pr)
    s, rho, e, _, _, _ = dichten(g, p1, v1)
    q1, e1 = (rho.sum() * g.dA).item(), (e.sum() * g.dA).item()
    aus = []
    for i in range(0, len(konfigs), stapel):
        teil = konfigs[i:i + stapel]
        felder = [summe_baelle(g, k) for k in teil]
        psi = torch.cat([f[0] for f in felder])
        vel = torch.cat([f[1] for f in felder])
        s, rho, e, _, _, _ = dichten(g, psi, vel)
        qs = (rho.sum((1, 2)) * g.dA).tolist()
        es = (e.sum((1, 2)) * g.dA).tolist()
        for k, qq, ee in zip(teil, qs, es):
            aus.append(ee - len(k) * e1 - w * (qq - len(k) * q1))
    return aus, q1, e1


def test_paare(out, rauch, stufen, args):
    start = jetzt()
    print(f"Paare Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t0 = uhr()
    pr = profile_holen([(W2_STD, 0)])[(W2_STD, 0)]
    dauer["profil_s"] = uhr() - t0
    if not pr["gueltig"]:
        raise SystemExit("Profil 0,70 ungueltig")
    kappa = math.sqrt(1.0 - W2_STD)
    # Statik: E_bind(d, dphi) aus der Ueberlagerung
    t0 = uhr()
    gs = Gitter(P_L, STUFEN[0][1])
    konf = []
    for sp in P_STAT_SPALT:
        d = abstand(pr, sp)
        for dph in P_STAT_PHASEN:
            konf.append([{"pr": pr, "x": -0.5 * d, "y": 0.0, "phase": 0.0}, {"pr": pr, "x": 0.5 * d, "y": 0.0, "phase": dph}])
    eb, q1g, e1g = statik(gs, pr, konf)
    dauer["statik_s"] = uhr() - t0
    stat = []
    for i, sp in enumerate(P_STAT_SPALT):
        stat.append({"spalt": sp, "d": abstand(pr, sp), "E_bind_0": eb[3 * i], "E_bind_quer": eb[3 * i + 1],
                     "E_bind_pi": eb[3 * i + 2]})
    # Abklingkonstante aus ln|E_bind(0) - E_bind(pi)| / 2 gegen d (Spalt >= 3), mit K_0-Vorfaktor sqrt(d)
    sel = [z for z in stat if z["spalt"] >= 3.0 and abs(z["E_bind_0"] - z["E_bind_pi"]) > 0]
    kappa_fit = None
    if len(sel) >= 3:
        dd = torch.tensor([z["d"] for z in sel], dtype=F64)
        yy = torch.tensor([math.log(abs(z["E_bind_0"] - z["E_bind_pi"]) * math.sqrt(z["d"])) for z in sel], dtype=F64)
        a = torch.stack([torch.ones_like(dd), dd], dim=1)
        kappa_fit = -torch.linalg.lstsq(a, yy.unsqueeze(1)).solution[1, 0].item()
    t_end = P_T * (RAUCH_FAKTOR if rauch else 1.0)
    r_w = fenster_r(pr, abstand(pr, 4.0))
    q_min = Q_KLUMPEN * pr["Q"]

    def bauen(g, lauf_):
        name, dph, sp = lauf_
        if dph is None:
            return [{"pr": pr, "x": 0.0, "y": 0.0, "phase": 0.0}]
        d = abstand(pr, sp)
        return [{"pr": pr, "x": -0.5 * d, "y": 0.0, "phase": 0.0}, {"pr": pr, "x": 0.5 * d, "y": 0.0, "phase": dph}]

    ergebnis = {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [l for l in P_LAEUFE if stufe == "grob" or l[0] in P_FEIN]
        g, t, glob, bahn, verlauf, orte = stufe_rechnen("paare", stufe, dx, dt, P_L, t_end, laeufe, bauen, r_w, q_min,
                                                        out, dauer, t_mess=P_MESS)
        L_rand = g.L - SPONGE - RAND_ABSTAND
        for b, (name, dph, sp) in enumerate(laeufe):
            kg = kenngroessen(verlauf[b], glob[0, b, 0].item(), L_rand)
            z = {"lauf": name, "dphi": dph, "spalt": sp, "stufe": stufe, **klasse_bestimmen(kg, t_end), **erhaltung(glob, b)}
            if dph is not None:
                x1, y1, x2, y2 = bahn[:, b, 0, 0], bahn[:, b, 0, 1], bahn[:, b, 1, 0], bahn[:, b, 1, 1]
                d = torch.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                z["d_start"] = d[0].item()
                z["d_min"] = d.min().item()
                z["d_max"] = d.max().item()
                z["d_ende"] = d[-1].item()
                i_f = fenster_idx(t, *P_FIT)
                fit = polyfit(t[i_f], d[i_f], 2) if i_f.numel() > 0 else None
                if fit is not None:
                    c, se, _, sp_ = fit
                    z["d_beschl"] = (2.0 * c[2] / sp_ ** 2).item()
                    z["d_beschl_fehler"] = (2.0 * se[2] / sp_ ** 2).item()
                i_q = fenster_idx(t, *P_FIT_Q)
                fq = polyfit(t[i_q], bahn[i_q, b, 0, 2], 1) if i_q.numel() > 0 else None
                if fq is not None:
                    z["dQ1_dt_start"] = (fq[0][1] / fq[3]).item()
                dq = bahn[:, b, 0, 2] - bahn[:, b, 1, 2]
                z["max_absdQ_rel"] = (dq.abs().max() / bahn[0, b, 0, 2].abs()).item()
                dth = entfalten(bahn[:, b, 1, 3]) - entfalten(bahn[:, b, 0, 3])
                z["dphase_start"] = wickeln(dth[0].item())
                z["dphase_ende"] = wickeln(dth[-1].item())
                z["dphase_spanne"] = (dth.max() - dth.min()).item()
                # gebunden (schwingt): kein Verschmelzen, nicht auseinander, mindestens zwei Richtungswechsel von d(t)
                # mit Hub >= 0,3 (Hysterese), d bleibt in [0,5; 1,3] d_Start, Auswertung ueber mindestens 100 Zeiteinheiten
                z["umkehrpunkte_d"] = schwuenge(d.tolist(), 0.3)
                if (z["klasse"] not in ("auseinander",) and not z["klasse"].startswith("verschmolzen")
                        and z["umkehrpunkte_d"] >= 2 and z["d_max"] < 1.3 * z["d_start"]
                        and z["d_min"] > 0.5 * z["d_start"] and (z["t_ende_auswertung"] or 0.0) >= 100.0):
                    z["klasse"] = "gebunden (schwingt)"
            ergebnis.setdefault(stufe, []).append(z)
    # Kennzahlen (vorab festgelegt, PLAN.md Abschnitt 2)
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn = {"kappa_theorie": kappa, "kappa_fit_statik": kappa_fit}
    # Statik je Spalt: E_bind(dphi) = A + B cos dphi + C cos 2 dphi; B = (E(0) - E(pi))/2 ist die Josephson-Amplitude
    def statik_bei(sp):
        z = [s for s in stat if abs(s["spalt"] - sp) < 1e-9]
        return z[0] if z else None

    def kraft_statik(sp, schl):
        a, b = statik_bei(sp - 0.5), statik_bei(sp + 0.5)
        if a is None or b is None:
            return None
        return -(b[schl] - a[schl]) / (b["d"] - a["d"])       # F = -dE_bind/dd

    for sp in (4.0, 5.0, 7.0):
        s_ = statik_bei(sp)
        if s_ is None:
            continue
        f0, fpi = kraft_statik(sp, "E_bind_0"), kraft_statik(sp, "E_bind_pi")
        kenn[f"statik_s{int(sp)}"] = {"B_josephson": 0.5 * (s_["E_bind_0"] - s_["E_bind_pi"]),
                                      "d_beschl_gleich": 2.0 * f0 / e1g if f0 is not None else None,
                                      "d_beschl_gegen": 2.0 * fpi / e1g if fpi is not None else None}
    # Dynamik gegen Statik (Kriterien PLAN.md 2.3): Beschleunigung d'' und Josephson-Strom
    for name, sp, schl in (("gleich_s4", 4.0, "d_beschl_gleich"), ("gleich_s5", 5.0, "d_beschl_gleich"),
                           ("gleich_s7", 7.0, "d_beschl_gleich"), ("gegen_s4", 4.0, "d_beschl_gegen"),
                           ("gegen_s5", 5.0, "d_beschl_gegen")):
        st = kenn.get(f"statik_s{int(sp)}", {}).get(schl)
        if name in grob and "d_beschl" in grob[name] and st:
            kenn[f"dyn_zu_statik_{name}"] = grob[name]["d_beschl"] / st
    if "quer_s4" in grob and "dQ1_dt_start" in grob["quer_s4"] and "statik_s4" in kenn:
        kenn["J_fluss_quer_s4"] = abs(grob["quer_s4"]["dQ1_dt_start"])
        kenn["J_fluss_zu_B_statik"] = kenn["J_fluss_quer_s4"] / abs(kenn["statik_s4"]["B_josephson"])
    if all(k in grob and "d_beschl" in grob[k] for k in ("gleich_s4", "gegen_s4")) and grob["gegen_s4"]["d_beschl"]:
        kenn["antisymmetrie_gleich_zu_gegen_s4"] = grob["gleich_s4"]["d_beschl"] / grob["gegen_s4"]["d_beschl"]
    if all(k in grob and "d_beschl" in grob[k] for k in ("gleich_s4", "gleich_s5", "gleich_s7")):
        kenn["verh_beschl_s4_s5"] = grob["gleich_s4"]["d_beschl"] / grob["gleich_s5"]["d_beschl"]
        kenn["verh_beschl_s5_s7"] = grob["gleich_s5"]["d_beschl"] / grob["gleich_s7"]["d_beschl"]
        kenn["verh_theorie_exp_kappa_1_und_2"] = [math.exp(kappa * 1.0), math.exp(kappa * 2.0)]
    if "fein" in ergebnis:
        l3 = []
        for zf in ergebnis["fein"]:
            zg = grob.get(zf["lauf"])
            if zg and "d_beschl" in zf and "d_beschl" in zg and zg["d_beschl"]:
                l3.append({"lauf": zf["lauf"], "klasse_gleich": zf["klasse"] == zg["klasse"],
                           "rel_aenderung_beschl": abs(zf["d_beschl"] / zg["d_beschl"] - 1.0)})
        kenn["L3"] = {"laeufe": l3, "bestanden": bool(l3) and all(z["klasse_gleich"] and z["rel_aenderung_beschl"] <= 0.1
                                                                  for z in l3)}
    ausgabe = {"karte": "paare", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer, "geraet": geraet_name(),
               "parameter": {"omega2": W2_STD, "L": P_L, "T": P_T, "fit": P_FIT, "fit_Q": P_FIT_Q, "stufen": STUFEN},
               "profil": profil_info(pr), "statik": stat, "Q1_gitter": q1g, "E1_gitter": e1g, "ergebnis": ergebnis,
               "kennzahlen": kenn}
    text = [kopf("Grundlage Paare (Paarkraft, Paarbindung)", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append(f"Ball omega2 {W2_STD}: Q {pr['Q']:.4f}, E {pr['E']:.4f}, R_halb {pr['R_halb']:.3f}; kappa {kappa:.4f}")
    text.append("Statik (Ueberlagerung, E_bind bei fester Ladung): Spalt | d | dphi=0 | pi/2 | pi")
    for z in stat:
        text.append(f"  {z['spalt']:.1f} | {z['d']:.2f} | {z['E_bind_0']:+.4e} | {z['E_bind_quer']:+.4e} | "
                    f"{z['E_bind_pi']:+.4e}")
    text.append("Dynamik: Stufe Lauf | Klasse | d Start/min/max/Ende | d'' (Fit 10-60) | dQ1/dt Start | max|dQ|/Q | "
                "dphase Start/Ende | Umkehrpunkte | t erste Verschmelzung | Q-Verlust")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            if z["dphi"] is None:
                text.append(f"  {stufe} {z['lauf']} | {z['klasse']} | Q-Verlust {z['Q_box_verlust']:.1e}")
                continue
            text.append(f"  {stufe} {z['lauf']} | {z['klasse']} | {z['d_start']:.2f}/{z['d_min']:.2f}/{z['d_max']:.2f}/"
                        f"{z['d_ende']:.2f} | {z.get('d_beschl', float('nan')):+.3e} | "
                        f"{z.get('dQ1_dt_start', float('nan')):+.3e} | {z['max_absdQ_rel']:.3f} | "
                        f"{z['dphase_start']:+.3f}/{z['dphase_ende']:+.3f} | {z['umkehrpunkte_d']} | "
                        f"{z['t_erste_verschmelzung']} | {z['Q_box_verlust']:.1e}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "paare", ausgabe, "\n".join(text))


# ---------------------------------------------------------------- Bio 25/42, Chemie 13: Gitter

def gitter_orte(form, k, d):
    """Quadrat k x k oder Dreiecksgitter (Basis (d, 0), (d/2, d sqrt3/2), Reihen j = 0..k-1, i = -floor(j/2) .. +k-1),
    zentriert. Rueckgabe Liste (x, y, i, j)."""
    orte = []
    if form == "quadrat":
        for j in range(k):
            for i in range(k):
                orte.append(((i - 0.5 * (k - 1)) * d, (j - 0.5 * (k - 1)) * d, i, j))
    else:
        for j in range(k):
            for i in range(-(j // 2), -(j // 2) + k):
                orte.append((i * d + 0.5 * j * d, j * d * math.sqrt(3.0) / 2.0, i, j))
        xm = sum(o[0] for o in orte) / len(orte)
        ym = sum(o[1] for o in orte) / len(orte)
        orte = [(x - xm, y - ym, i, j) for x, y, i, j in orte]
    return orte


def gitter_phasen(form, muster, orte, seed):
    rng = random.Random(seed)
    ph = []
    for x, y, i, j in orte:
        if muster == "gleich":
            ph.append(0.0)
        elif muster == "wechsel":
            ph.append(math.pi * ((i + j) % 2))
        elif muster == "streifen":
            ph.append(math.pi * (j % 2))
        elif muster == "drei":
            ph.append(2.0 * math.pi / 3.0 * ((i - j) % 3))
        elif muster == "windung":
            ph.append(math.atan2(y, x))
        elif muster == "zufall":
            ph.append(rng.uniform(0.0, 2.0 * math.pi))
        else:
            raise ValueError(muster)
    return ph


def gruppen_text(ergebnis, extra=None):
    zeilen = []
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            zeilen.append(f"  {stufe} {z['lauf']} | {z['klasse']} | n {z.get('n_start')}->{z.get('n_ende')} "
                          f"(min {z.get('n_min')}, max {z.get('n_max')}) | t_verschm {z.get('t_erste_verschmelzung')} | "
                          f"Rg rel {fz(z.get('rg_rel_min'))}..{fz(z.get('rg_rel_max'))} | dNN rel "
                          f"{fz(z.get('dnn_rel_min'))}..{fz(z.get('dnn_rel_max'))} | abgestr. {fz(z.get('frad_ende'))} | "
                          f"Ende Auswertung {z.get('t_ende_auswertung')} | J {z['J_box_start']:+.3f}->{z['J_box_ende']:+.3f} | "
                          f"Q-Verl. {z['Q_box_verlust']:.1e}" + (extra(z) if extra else ""))
    return zeilen


def fz(x, f="{:.3f}"):
    return f.format(x) if isinstance(x, (int, float)) and x is not None else "-"


def l3_klassen(ergebnis, schluessel_t="t_erste_verschmelzung"):
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    l3 = []
    for zf in ergebnis.get("fein", []):
        zg = grob.get(zf["lauf"])
        if not zg:
            continue
        ok = zf["klasse"] == zg["klasse"]
        tg, tf = zg.get(schluessel_t), zf.get(schluessel_t)
        if tg is not None:
            ok = ok and tf is not None and abs(tf - tg) <= max(0.2 * tg, 10.0)
        l3.append({"lauf": zf["lauf"], "grob": zg["klasse"], "fein": zf["klasse"], "t_grob": tg, "t_fein": tf,
                   "bestanden": ok})
    return {"laeufe": l3, "bestanden": (all(z["bestanden"] for z in l3) if l3 else None)}


def test_gitter(out, rauch, stufen, args):
    start = jetzt()
    print(f"Gitter Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t0 = uhr()
    pr = profile_holen([(W2_STD, 0)])[(W2_STD, 0)]
    dauer["profil_s"] = uhr() - t0
    d = abstand(pr, SPALT)
    t_end = G_T * (RAUCH_FAKTOR if rauch else 1.0)
    info = {}

    def bauen(g, lauf_):
        name, form, k, muster = lauf_[:4]
        dd = abstand(pr, lauf_[4]) if len(lauf_) > 4 else d
        orte = gitter_orte(form, k, dd)
        ph = gitter_phasen(form, muster, orte, G_SEED)
        info[name] = {"orte": [(round(x, 3), round(y, 3)) for x, y, _, _ in orte], "phasen": [round(p, 4) for p in ph]}
        return [{"pr": pr, "x": x, "y": y, "phase": p} for (x, y, _, _), p in zip(orte, ph)]

    ergebnis = {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [l for l in G_LAEUFE if stufe == "grob" or l[0] in G_FEIN]
        g, t, glob, bahn, verlauf, orte = stufe_rechnen("gitter", stufe, dx, dt, G_L, t_end, laeufe, bauen,
                                                        fenster_r(pr, d), Q_KLUMPEN * pr["Q"], out, dauer)
        L_rand = g.L - SPONGE - RAND_ABSTAND
        for b, lauf_ in enumerate(laeufe):
            name, form, k, muster = lauf_[:4]
            kg = kenngroessen(verlauf[b], glob[0, b, 0].item(), L_rand)
            z = {"lauf": name, "form": form, "k": k, "muster": muster, "spalt": lauf_[4] if len(lauf_) > 4 else SPALT,
                 "stufe": stufe, "n_baelle": len(orte[b]),
                 **klasse_bestimmen(kg, t_end), **erhaltung(glob, b), "startzerlegung_ok": kg["n"][0] == len(orte[b]),
                 "klumpen_ende": klumpen_kurz(verlauf[b][-1][2]), "verlauf": verlauf_kurz(verlauf[b])}
            ergebnis.setdefault(stufe, []).append(z)
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn = {"klassen": {n: z["klasse"] for n, z in grob.items()},
            "halten_gefunden": [n for n, z in grob.items() if z["klasse"] == "halten"],
            "gemischte_phasen_halten": [n for n, z in grob.items() if z["klasse"] == "halten" and z["muster"] != "gleich"]}
    if "fein" in ergebnis:
        kenn["L3"] = l3_klassen(ergebnis)
    ausgabe = {"karte": "gitter (Bio 25/42, Chemie 13)", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "parameter": {"omega2": W2_STD, "spalt": SPALT, "d": d, "L": G_L, "T": G_T,
                                                      "seed": G_SEED, "stufen": STUFEN},
               "profil": profil_info(pr), "aufbau": info, "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Bio 25/42 und Chemie 13: Gitter und Wabe, Wechselphasen-Kristall", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append(f"Ball omega2 {W2_STD}: Q {pr['Q']:.3f}, R_halb {pr['R_halb']:.3f}; Nachbarabstand d {d:.3f}")
    text.append("Stufe Lauf | Klasse | Klumpen | erste Verschmelzung | Traegheitsradius rel | NN-Abstand rel | abgestrahlt | "
                "Auswertung bis | J Box | Q-Verlust")
    text += gruppen_text(ergebnis)
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "gitter", ausgabe, "\n".join(text))


# ---------------------------------------------------------------- Bio 46, Chemie 19: Ringe

def ring_geschw(pr, R):
    """Tangentialgeschwindigkeit fuer J_Bahn = Q je Ball: gamma E v R = Q  ->  v = x / sqrt(1 + x^2), x = Q/(E R)."""
    x = pr["Q"] / (pr["E"] * R)
    return x / math.sqrt(1.0 + x * x)


def test_ringe(out, rauch, stufen, args):
    start = jetzt()
    print(f"Ringe Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t0 = uhr()
    pr = profile_holen([(W2_STD, 0)])[(W2_STD, 0)]
    dauer["profil_s"] = uhr() - t0
    d = abstand(pr, SPALT)
    t_end = R_T * (RAUCH_FAKTOR if rauch else 1.0)
    info = {}

    def bauen(g, lauf_):
        name, N, k, dreh = lauf_
        R = d / (2.0 * math.sin(math.pi / N))
        v = ring_geschw(pr, R) if dreh else 0.0
        baelle = []
        for j in range(N):
            th = 2.0 * math.pi * j / N
            b = {"pr": pr, "x": R * math.cos(th), "y": R * math.sin(th), "phase": 2.0 * math.pi * k * j / N}
            if dreh:
                b["v"], b["winkel"] = v, th + dreh * 0.5 * math.pi
            baelle.append(b)
        info[name] = {"N": N, "k": k, "dreh": dreh, "R": R, "v": v, "cos_nachbar": math.cos(2.0 * math.pi * k / N)}
        return baelle

    ergebnis = {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [l for l in R_LAEUFE if stufe == "grob" or l[0] in R_FEIN]
        g, t, glob, bahn, verlauf, orte = stufe_rechnen("ringe", stufe, dx, dt, R_L, t_end, laeufe, bauen,
                                                        fenster_r(pr, d), Q_KLUMPEN * pr["Q"], out, dauer,
                                                        windung=True)
        L_rand = g.L - SPONGE - RAND_ABSTAND
        for b, (name, N, k, dreh) in enumerate(laeufe):
            kg = kenngroessen(verlauf[b], glob[0, b, 0].item(), L_rand)
            # Ringradius aus dem Verfolger (Mittel der Abstaende vom Schwerpunkt der Verfolger) und Drehwinkel von Ball 0
            xs, ys = bahn[:, b, :N, 0], bahn[:, b, :N, 1]
            rr = torch.sqrt((xs - xs.mean(1, keepdim=True)) ** 2 + (ys - ys.mean(1, keepdim=True)) ** 2).mean(1)
            winkel = entfalten(torch.atan2(ys[:, 0] - ys.mean(1), xs[:, 0] - xs.mean(1)))
            kl_ende = verlauf[b][-1][2]
            z = {"lauf": name, "N": N, "k": k, "dreh": dreh, "stufe": stufe, **info[name], **klasse_bestimmen(kg, t_end),
                 **erhaltung(glob, b), "startzerlegung_ok": kg["n"][0] == N,
                 "J_zu_Q_start": (glob[0, b, 2] / glob[0, b, 0]).item(),
                 "R_ring_start": rr[0].item(), "R_ring_min": rr.min().item(), "R_ring_max": rr.max().item(),
                 "drehwinkel_ball0": (winkel[-1] - winkel[0]).item(),
                 "windungen_ende": [kk.get("windung") if kk.get("windung_sicher") else None for kk in kl_ende],
                 "klumpen_ende": klumpen_kurz(kl_ende, True), "verlauf": verlauf_kurz(verlauf[b], True)}
            ergebnis.setdefault(stufe, []).append(z)
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn = {"klassen": {n: z["klasse"] for n, z in grob.items()},
            "halten_gefunden": [n for n, z in grob.items() if z["klasse"] == "halten"],
            "windung_1_am_ende": [n for n, z in grob.items() if 1 in z["windungen_ende"] or -1 in z["windungen_ende"]]}
    if "N6_k0" in grob and "N6_k3" in grob:
        kenn["aromatizitaet_N6"] = {"gleich": grob["N6_k0"]["klasse"], "wechsel": grob["N6_k3"]["klasse"]}
    if "fein" in ergebnis:
        kenn["L3"] = l3_klassen(ergebnis)
    ausgabe = {"karte": "ringe (Bio 46 Kapsid, Chemie 19 Aromatizitaet)", "start": start, "ende": jetzt(), "rauch": rauch,
               "dauer_s": dauer, "geraet": geraet_name(),
               "parameter": {"omega2": W2_STD, "spalt": SPALT, "d": d, "L": R_L, "T": R_T, "stufen": STUFEN},
               "profil": profil_info(pr), "aufbau": info, "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Bio 46 Kapsid und Chemie 19 Aromatizitaet: Ringe", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append(f"Ball omega2 {W2_STD}: Q {pr['Q']:.3f}, E {pr['E']:.3f}, R_halb {pr['R_halb']:.3f}; d {d:.3f}")
    text.append("Stufe Lauf | Klasse | Klumpen | ... | Zusatz: J/Q Start | R_Ring Start/min/max | Drehwinkel Ball 0 | "
                "Windungen Ende")
    text += gruppen_text(ergebnis, lambda z: (f" | J/Q {z['J_zu_Q_start']:+.3f} | R {z['R_ring_start']:.2f}/"
                                             f"{z['R_ring_min']:.2f}/{z['R_ring_max']:.2f} | Dreh {z['drehwinkel_ball0']:+.2f}"
                                             f" | W {z['windungen_ende']}"))
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "ringe", ausgabe, "\n".join(text))


# ---------------------------------------------------------------- Bio 11: Gluehwuermchen

def hilbert_phase(x):
    """Analytisches Signal ueber FFT fuer (M, K) entlang der Zeit; Rueckgabe Phase und Betrag."""
    M = x.shape[0]
    X = torch.fft.fft(x, dim=0)
    h = torch.zeros(M, dtype=F64, device=x.device)
    h[0] = 1.0
    if M % 2 == 0:
        h[M // 2] = 1.0
        h[1:M // 2] = 2.0
    else:
        h[1:(M + 1) // 2] = 2.0
    a = torch.fft.ifft(X * h.view(-1, 1), dim=0)
    return torch.atan2(a.imag, a.real), a.abs()


def test_gluehwurm(out, rauch, stufen, args):
    start = jetzt()
    print(f"Gluehwuermchen Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    w2s = [round(W2_STD + dd, 6) for dd in GW_DW2]
    t0 = uhr()
    prof = profile_holen([(w, 0) for w in w2s] + [(W2_STD, 0)])
    dauer["profil_s"] = uhr() - t0
    p70 = prof[(W2_STD, 0)]
    N = len(w2s)
    t_end = GW_T * (RAUCH_FAKTOR if rauch else 1.0)
    info = {}

    def bauen(g, lauf_):
        name, spalt, muster, atem = lauf_
        d = abstand(p70, spalt)
        R = d / (2.0 * math.sin(math.pi / N))
        baelle = []
        for j in range(N):
            th = 2.0 * math.pi * j / N
            ph = {"zufall": (GOLD * j) % (2.0 * math.pi), "gleich": 0.0, "wechsel": math.pi * (j % 2)}[muster]
            beta = (1.0 + GOLD * (j + 3)) % (2.0 * math.pi)
            b = {"pr": prof[(w2s[j], 0)], "x": R * math.cos(th), "y": R * math.sin(th), "phase": ph}
            if atem:
                b["eps_r"], b["eps_w"] = GW_EPS * math.cos(beta), GW_EPS * math.sin(beta)
            baelle.append(b)
        info[name] = {"R": R, "d": d, "omega2": w2s}
        return baelle

    ergebnis = {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [l for l in GW_LAEUFE if stufe == "grob" or l[0] in GW_FEIN]
        g, t, glob, bahn, verlauf, orte = stufe_rechnen("gluehwurm", stufe, dx, dt, GW_L, t_end, laeufe, bauen,
                                                        fenster_r(p70, abstand(p70, 4.0)), Q_KLUMPEN * p70["Q"], out, dauer,
                                                        t_mess=GW_MESS)
        L_rand = g.L - SPONGE - RAND_ABSTAND
        T_ = t[-1].item()
        ia = fenster_idx(t, 0.0, 0.1 * T_)
        ie = fenster_idx(t, 0.75 * T_, T_)
        for b, (name, spalt, muster, atem) in enumerate(laeufe):
            kg = kenngroessen(verlauf[b], glob[0, b, 0].item(), L_rand)
            z = {"lauf": name, "spalt": spalt, "muster": muster, "atem": atem, "stufe": stufe, **info[name],
                 **klasse_bestimmen(kg, t_end), **erhaltung(glob, b)}
            ph = entfalten(bahn[:, b, :N, 3])                              # (M, N), faellt mit omega
            z["verschmolzen"] = z["n_min"] is not None and z["n_min"] < N
            if ia.numel() >= 2 and ie.numel() >= 2:
                def frequenz(ii):
                    return -(ph[ii[-1]] - ph[ii[0]]) / (t[ii[-1]] - t[ii[0]])
                om_a, om_e = frequenz(ia), frequenz(ie)
                z["omega_anfang"] = om_a.tolist()
                z["omega_ende"] = om_e.tolist()
                z["sigma_om_anfang"] = om_a.std(unbiased=False).item()
                z["sigma_om_ende"] = om_e.std(unbiased=False).item()
                r_t = torch.exp(1j * bahn[:, b, :N, 3]).mean(1).abs()
                z["r_anfang"] = r_t[ia].mean().item()
                z["r_ende"] = r_t[ie].mean().item()
                # Atmung: R_rms je Ball, linear entzerrt, analytisches Signal
                x = bahn[:, b, :N, 4]
                tt = t.view(-1, 1)
                a_ = torch.cat([torch.ones_like(tt), tt], dim=1)
                koef = torch.linalg.lstsq(a_, x).solution
                xr = x - a_ @ koef
                beta, amp = hilbert_phase(xr)
                rb = torch.exp(1j * beta).mean(1).abs()
                rand = max(1, int(0.05 * t.shape[0]))                     # Randeffekt der FFT: 5 % abschneiden
                ia2 = ia[(ia >= rand)]
                ie2 = ie[(ie < t.shape[0] - rand)]
                if ia2.numel() > 0 and ie2.numel() > 0:
                    z["r_atem_anfang"] = rb[ia2].mean().item()
                    z["r_atem_ende"] = rb[ie2].mean().item()
                    z["atem_amp_anfang"] = amp[ia2].mean().item()
                    z["atem_amp_ende"] = amp[ie2].mean().item()
                    spek = torch.fft.rfft(xr, dim=0).abs().mean(1)
                    fr = torch.fft.rfftfreq(xr.shape[0], d=(t[1] - t[0]).item()) * 2.0 * math.pi
                    z["atem_Omega_dominant"] = fr[1 + int(spek[1:].argmax())].item() if spek.shape[0] > 1 else None
            ergebnis.setdefault(stufe, []).append(z)
    # Urteile gegen die weite Kontrolle (vorab, PLAN.md Abschnitt 5)
    for stufe, liste in ergebnis.items():
        kz = {z["lauf"]: z for z in liste}.get(GW_KONTROLLE) or {z["lauf"]: z for z in ergebnis.get("grob", [])}.get(
            GW_KONTROLLE)
        for z in liste:
            if kz is None or "r_ende" not in z or "r_ende" not in kz:
                continue
            z["effekt_r"] = z["r_ende"] - kz["r_ende"]
            z["phasensynchron"] = bool(z["r_ende"] >= R_SYNC and not z["verschmolzen"] and z["effekt_r"] >= 0.3)
            z["sigma_verh"] = z["sigma_om_ende"] / max(kz["sigma_om_anfang"], 1e-300)
            z["frequenzsynchron"] = bool(z["sigma_verh"] <= 0.2 and not z["verschmolzen"])
            if "r_atem_ende" in z and "r_atem_ende" in kz:
                z["effekt_r_atem"] = z["r_atem_ende"] - kz["r_atem_ende"]
                z["atem_synchron"] = bool(z["r_atem_ende"] >= R_SYNC and z["effekt_r_atem"] >= 0.3 and not z["verschmolzen"]
                                          and z["atem_amp_ende"] >= 0.2 * z["atem_amp_anfang"])
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn = {"phasensynchron": [n for n, z in grob.items() if z.get("phasensynchron")],
            "frequenzsynchron": [n for n, z in grob.items() if z.get("frequenzsynchron")],
            "atem_synchron": [n for n, z in grob.items() if z.get("atem_synchron")],
            "klassen": {n: z["klasse"] for n, z in grob.items()}}
    if "fein" in ergebnis:
        l3 = []
        for zf in ergebnis["fein"]:
            zg = grob.get(zf["lauf"])
            if zg and "r_ende" in zf and "r_ende" in zg:
                l3.append({"lauf": zf["lauf"], "klasse_gleich": zf["klasse"] == zg["klasse"],
                           "d_r_ende": abs(zf["r_ende"] - zg["r_ende"]),
                           "d_sigma_om_ende_rel": abs(zf["sigma_om_ende"] / max(zg["sigma_om_ende"], 1e-300) - 1.0)})
        kenn["L3"] = {"laeufe": l3, "bestanden": bool(l3) and all(z["klasse_gleich"] and z["d_r_ende"] <= 0.1 for z in l3)}
    ausgabe = {"karte": "gluehwurm (Bio 11)", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "parameter": {"omega2": w2s, "L": GW_L, "T": GW_T, "t_mess": GW_MESS,
                                                      "eps": GW_EPS, "stufen": STUFEN},
               "profile": [profil_info(prof[(w, 0)]) for w in w2s], "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Bio 11 Gluehwuermchen: Ring aus 8 Baellen", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append("omega^2 der Baelle: " + ", ".join(f"{w:.4f}" for w in w2s))
    text.append("Stufe Lauf | Klasse | verschmolzen | r Anfang/Ende | sigma_om Anfang/Ende | r_Atem Anfang/Ende | "
                "Atem-Amplitude Anfang/Ende | Omega_Atem | phasen-/frequenz-/atemsynchron")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            text.append(f"  {stufe} {z['lauf']} | {z['klasse']} | {z['verschmolzen']} | {fz(z.get('r_anfang'))}/"
                        f"{fz(z.get('r_ende'))} | {fz(z.get('sigma_om_anfang'), '{:.2e}')}/"
                        f"{fz(z.get('sigma_om_ende'), '{:.2e}')} | {fz(z.get('r_atem_anfang'))}/{fz(z.get('r_atem_ende'))}"
                        f" | {fz(z.get('atem_amp_anfang'), '{:.2e}')}/{fz(z.get('atem_amp_ende'), '{:.2e}')} | "
                        f"{fz(z.get('atem_Omega_dominant'))} | {z.get('phasensynchron')}/{z.get('frequenzsynchron')}/"
                        f"{z.get('atem_synchron')}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "gluehwurm", ausgabe, "\n".join(text))


# ---------------------------------------------------------------- Bio 47: Haendigkeit

def spiegel(baelle):
    """Spiegelung x -> -x: Ball (x, y, m, phi) -> (-x, y, -m, phi + m pi)."""
    return [{**b, "x": -b["x"], "m": -b["m"], "phase": b["phase"] + b["m"] * math.pi} for b in baelle]


def test_haendigkeit(out, rauch, stufen, args):
    start = jetzt()
    print(f"Haendigkeit Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t0 = uhr()
    pr = profile_holen([(H_W2, 1)])[(H_W2, 1)]
    dauer["profil_s"] = uhr() - t0
    if not pr["gueltig"]:
        raise SystemExit("Profil m = 1 bei 0,55 ungueltig: Karte entfaellt")
    d = 2.0 * pr["R_halb"] + SPALT
    orte = [((i - 1) * d, (j - 1) * d) for j in range(3) for i in range(3)]

    def misch(seed):
        rng = random.Random(seed)
        vorz = [1] * 5 + [-1] * 4
        rng.shuffle(vorz)
        return [{"pr": pr, "x": x, "y": y, "m": s, "phase": rng.uniform(0.0, 2.0 * math.pi)} for (x, y), s in zip(orte, vorz)]

    plus = [{"pr": pr, "x": x, "y": y, "m": 1, "phase": 0.0} for x, y in orte]
    konf = {"plus9": plus, "plus9_spiegel": spiegel(plus), "misch_a": misch(1), "misch_a_spiegel": spiegel(misch(1)),
            "misch_b": misch(2), "einzel_plus": [{"pr": pr, "x": 0.0, "y": 0.0, "m": 1, "phase": 0.0}]}
    namen = list(konf)
    t_end = H_T * (RAUCH_FAKTOR if rauch else 1.0)

    def bauen(g, lauf_):
        return konf[lauf_[0]]

    ergebnis, roh = {}, {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [(n,) for n in namen if stufe == "grob" or n in H_FEIN]
        g, t, glob, bahn, verlauf, _ = stufe_rechnen("haendigkeit", stufe, dx, dt, H_L, t_end, laeufe, bauen,
                                                     fenster_r(pr, d), Q_KLUMPEN * pr["Q"], out, dauer,
                                                     windung=True)
        L_rand = g.L - SPONGE - RAND_ABSTAND
        roh[stufe] = {"glob": glob, "verlauf": verlauf, "namen": [l[0] for l in laeufe]}
        for b, (name,) in enumerate(laeufe):
            kg = kenngroessen(verlauf[b], glob[0, b, 0].item(), L_rand)

            def eta(kl):
                w = [(k["Q"], k["windung"]) for k in kl if k.get("windung") and k.get("windung_sicher")]
                qs = sum(q for q, _ in w)
                return sum(q * (1 if s > 0 else -1) for q, s in w) / qs if qs > 0 else 0.0

            etas = [eta(kl) for _, _, kl in verlauf[b]]
            z = {"lauf": name, "stufe": stufe, **klasse_bestimmen(kg, t_end), **erhaltung(glob, b),
                 "eta_start": etas[0], "eta_ende": etas[-1], "eta_min": min(etas), "eta_max": max(etas),
                 "J_zu_Q_start": (glob[0, b, 2] / glob[0, b, 0]).item(), "J_zu_Q_ende": (glob[-1, b, 2] / glob[-1, b, 0]).item(),
                 "windungen_start": [k.get("windung") for k in verlauf[b][0][2]],
                 "windungen_ende": [k.get("windung") for k in verlauf[b][-1][2]],
                 "klumpen_ende": klumpen_kurz(verlauf[b][-1][2], True), "verlauf": verlauf_kurz(verlauf[b], True)}
            ergebnis.setdefault(stufe, []).append(z)
    # Spiegelprobe (vorab, PLAN.md Abschnitt 6): J(t) + J_spiegel(t) = 0, gleiche Klumpenzahlen, eta + eta_spiegel = 0
    kenn = {}
    if "grob" in roh:
        r_ = roh["grob"]
        ix = {n: i for i, n in enumerate(r_["namen"])}
        for a, b in (("plus9", "plus9_spiegel"), ("misch_a", "misch_a_spiegel")):
            if a in ix and b in ix:
                ja, jb = r_["glob"][:, ix[a], 2], r_["glob"][:, ix[b], 2]
                na = [len(kl) for _, _, kl in r_["verlauf"][ix[a]]]
                nb = [len(kl) for _, _, kl in r_["verlauf"][ix[b]]]
                grob = {z["lauf"]: z for z in ergebnis["grob"]}
                kenn[f"spiegel_{a}"] = {
                    "max_J_summe_rel": ((ja + jb).abs().max() / ja.abs().max().clamp(min=1e-300)).item(),
                    "klumpenzahl_gleich": na == nb, "eta_summe_ende": grob[a]["eta_ende"] + grob[b]["eta_ende"]}
        grob = {z["lauf"]: z for z in ergebnis["grob"]}
        kenn["eta_drift"] = {n: grob[n]["eta_ende"] - grob[n]["eta_start"] for n in ("misch_a", "misch_a_spiegel", "misch_b")
                             if n in grob}
        kenn["einzel_plus_klasse"] = grob.get("einzel_plus", {}).get("klasse")
    if "fein" in ergebnis:
        kenn["L3"] = l3_klassen(ergebnis)
    ausgabe = {"karte": "haendigkeit (Bio 47)", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "parameter": {"omega2": H_W2, "m": 1, "d": d, "L": H_L, "T": H_T, "stufen": STUFEN},
               "profil": profil_info(pr),
               "aufbau": {n: [[round(b["x"], 3), round(b["y"], 3), b["m"], round(b["phase"], 4)] for b in k]
                          for n, k in konf.items()},
               "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Bio 47 Haendigkeit: Gitter aus m = +1 / -1", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append(f"Ball m = 1, omega2 {H_W2}: Q {pr['Q']:.3f}, R_halb {pr['R_halb']:.3f}, Loch {pr['R_kern_halb']:.3f}; "
                f"d {d:.3f}")
    text += gruppen_text(ergebnis, lambda z: (f" | eta {z['eta_start']:+.3f}->{z['eta_ende']:+.3f} | J/Q "
                                             f"{z['J_zu_Q_start']:+.3f}->{z['J_zu_Q_ende']:+.3f} | W {z['windungen_ende']}"))
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "haendigkeit", ausgabe, "\n".join(text))


# ---------------------------------------------------------------- Chemie 5: Isomere

def iso_orte(alpha_grad, d):
    a = math.radians(alpha_grad) / 2.0
    o = [(-d * math.sin(a), -d * math.cos(a)), (0.0, 0.0), (d * math.sin(a), -d * math.cos(a))]
    xm = sum(x for x, _ in o) / 3.0
    ym = sum(y for _, y in o) / 3.0
    return [(x - xm, y - ym) for x, y in o]


def test_isomere(out, rauch, stufen, args):
    start = jetzt()
    print(f"Isomere Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t0 = uhr()
    pr = profile_holen([(W2_STD, 0)])[(W2_STD, 0)]
    dauer["profil_s"] = uhr() - t0
    d = abstand(pr, SPALT)
    t_end = I_T * (RAUCH_FAKTOR if rauch else 1.0)
    konf = {name: [{"pr": pr, "x": x, "y": y, "phase": ph} for (x, y), ph in zip(iso_orte(alpha, d), phs)]
            for name, alpha, phs in I_LAEUFE}
    # Statik: Bindungsenergie jeder Anordnung und paarweise Summe (Additivitaet)
    t0 = uhr()
    gs = Gitter(I_L, STUFEN[0][1])
    namen = [l[0] for l in I_LAEUFE]
    eb, _, _ = statik(gs, pr, [konf[n] for n in namen])
    paare = []
    for n in namen:
        k = konf[n]
        for i in range(3):
            for j in range(i + 1, 3):
                paare.append([{**k[i]}, {**k[j]}])
    ep, _, _ = statik(gs, pr, paare)
    dauer["statik_s"] = uhr() - t0
    stat = {n: {"E_bind": eb[i], "E_paarsumme": sum(ep[3 * i:3 * i + 3])} for i, n in enumerate(namen)}
    for n in namen:
        s = stat[n]
        s["dreikoerper_rel"] = (s["E_bind"] - s["E_paarsumme"]) / abs(s["E_paarsumme"]) if s["E_paarsumme"] else None

    def bauen(g, lauf_):
        return konf[lauf_[0]]

    ergebnis = {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [l for l in I_LAEUFE if stufe == "grob" or l[0] in I_FEIN]
        g, t, glob, bahn, verlauf, orte = stufe_rechnen("isomere", stufe, dx, dt, I_L, t_end, laeufe, bauen,
                                                        fenster_r(pr, d), Q_KLUMPEN * pr["Q"], out, dauer)
        L_rand = g.L - SPONGE - RAND_ABSTAND
        for b, (name, alpha, phs) in enumerate(laeufe):
            kg = kenngroessen(verlauf[b], glob[0, b, 0].item(), L_rand)
            xs, ys = bahn[:, b, :3, 0], bahn[:, b, :3, 1]
            v1 = torch.stack([xs[:, 0] - xs[:, 1], ys[:, 0] - ys[:, 1]], 1)
            v2 = torch.stack([xs[:, 2] - xs[:, 1], ys[:, 2] - ys[:, 1]], 1)
            cosw = (v1 * v2).sum(1) / (v1.norm(dim=1) * v2.norm(dim=1)).clamp(min=1e-300)
            winkel = torch.rad2deg(torch.acos(cosw.clamp(-1.0, 1.0)))
            z = {"lauf": name, "alpha_start": alpha, "stufe": stufe, **stat[name], **klasse_bestimmen(kg, t_end),
                 **erhaltung(glob, b), "winkel_min": winkel.min().item(), "winkel_max": winkel.max().item(),
                 "winkel_ende": winkel[-1].item(), "verlauf": verlauf_kurz(verlauf[b])}
            ergebnis.setdefault(stufe, []).append(z)
    kenn = {"E_dreieck_minus_kette_gleich": stat["dreieck_gleich"]["E_bind"] - stat["kette_gleich"]["E_bind"],
            "E_dreieck_minus_kette_wechsel": stat["dreieck_wechsel"]["E_bind"] - stat["kette_wechsel"]["E_bind"],
            "dreikoerper_rel": {n: stat[n]["dreikoerper_rel"] for n in namen}}
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn["klassen"] = {n: z["klasse"] for n, z in grob.items()}
    kenn["umwandlung_kette_zu_dreieck"] = [n for n, z in grob.items() if n.startswith(("kette", "knick"))
                                           and z["winkel_min"] <= 75.0 and not z["klasse"].startswith("verschmolzen")]
    if "fein" in ergebnis:
        kenn["L3"] = l3_klassen(ergebnis)
    ausgabe = {"karte": "isomere (Chemie 5)", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "parameter": {"omega2": W2_STD, "d": d, "L": I_L, "T": I_T, "stufen": STUFEN},
               "profil": profil_info(pr), "statik": stat, "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Chemie 5 Isomere: Kette, geknickte Kette, Dreieck", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append(f"d {d:.3f}. Statik: Anordnung | E_bind | Paarsumme | Dreikoerperanteil rel")
    for n in namen:
        s = stat[n]
        text.append(f"  {n} | {s['E_bind']:+.4e} | {s['E_paarsumme']:+.4e} | {fz(s['dreikoerper_rel'], '{:+.3f}')}")
    text += gruppen_text(ergebnis, lambda z: f" | Winkel min/max/Ende {z['winkel_min']:.1f}/{z['winkel_max']:.1f}/"
                                             f"{z['winkel_ende']:.1f}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "isomere", ausgabe, "\n".join(text))


# ---------------------------------------------------------------- Bio 26 Schleimpilz, Bio 40 Schwarm

def streuorte(n, rscheibe, dmin, seed):
    rng = random.Random(seed)
    orte = []
    versuche = 0
    while len(orte) < n:
        versuche += 1
        if versuche > 200000:
            raise RuntimeError("Streuorte: keine Anordnung gefunden")
        r = rscheibe * math.sqrt(rng.random())
        th = rng.uniform(0.0, 2.0 * math.pi)
        x, y = r * math.cos(th), r * math.sin(th)
        if all(math.hypot(x - a, y - b) >= dmin for a, b in orte):
            orte.append((x, y))
    return orte


def test_kollektiv(out, rauch, stufen, args):
    start = jetzt()
    print(f"Kollektiv Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t0 = uhr()
    pr = profile_holen([(W2_STD, 0)])[(W2_STD, 0)]
    dauer["profil_s"] = uhr() - t0
    orte = streuorte(K_N, K_RSCHEIBE, 2.0 * pr["R_halb"] + 3.0, K_SEED)
    rng = random.Random(K_SEED + 1)
    phasen = [rng.uniform(0.0, 2.0 * math.pi) for _ in range(K_N)]
    richt = [rng.uniform(0.0, 2.0 * math.pi) for _ in range(K_N)]
    t_end = K_T * (RAUCH_FAKTOR if rauch else 1.0)

    def bauen(g, lauf_):
        name, muster, bewegt = lauf_
        baelle = []
        for j, (x, y) in enumerate(orte):
            b = {"pr": pr, "x": x, "y": y, "phase": phasen[j] if muster == "zufall" else 0.0}
            if bewegt:
                b["v"], b["winkel"] = K_V, richt[j]
            baelle.append(b)
        return baelle

    def polarisation(kl):
        num = [sum(k["Q"] * k["vx"] for k in kl), sum(k["Q"] * k["vy"] for k in kl)]
        den = sum(k["Q"] * math.hypot(k["vx"], k["vy"]) for k in kl)
        return math.hypot(*num) / den if den > 0 else None

    def phasenordnung(kl):
        if not kl:
            return None
        z = sum(cmath.exp(1j * k["phase"]) for k in kl) / len(kl)
        return abs(z)

    ergebnis = {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [l for l in K_LAEUFE if stufe == "grob" or l[0] in K_FEIN]
        g, t, glob, bahn, verlauf, _ = stufe_rechnen("kollektiv", stufe, dx, dt, K_L, t_end, laeufe, bauen,
                                                     fenster_r(pr, 2.0 * pr["R_halb"] + 3.0), Q_KLUMPEN * pr["Q"], out, dauer)
        L_rand = g.L - SPONGE - RAND_ABSTAND
        for b, (name, muster, bewegt) in enumerate(laeufe):
            kg = kenngroessen(verlauf[b], glob[0, b, 0].item(), L_rand)
            kc = klasse_bestimmen(kg, t_end)
            i_e = [i for i, tt in enumerate(kg["t"]) if kg["t_rand"] is None or tt < kg["t_rand"]]
            kl_a, kl_e = verlauf[b][0][2], verlauf[b][i_e[-1] if i_e else -1][2]
            qs_e = sum(k["Q"] for k in kl_e)
            z = {"lauf": name, "muster": muster, "bewegt": bewegt, "stufe": stufe, **kc, **erhaltung(glob, b),
                 "polarisation_start": polarisation(kl_a), "polarisation_ende": polarisation(kl_e),
                 "phasenordnung_start": phasenordnung(kl_a), "phasenordnung_ende": phasenordnung(kl_e),
                 "anteil_groesster_klumpen": (kl_e[0]["Q"] / qs_e) if kl_e and qs_e > 0 else None,
                 "verlauf": verlauf_kurz(verlauf[b])}
            n0, ne = z.get("n_start") or 0, z.get("n_ende") or 0
            if ne and n0 and ne <= n0 / 3 and (z["anteil_groesster_klumpen"] or 0) >= 0.5:
                z["kollektiv"] = "aggregiert (Schleimpilz)"
            elif ne and n0 and ne < n0:
                z["kollektiv"] = "vergroebert"
            else:
                z["kollektiv"] = "Gas (kein Sammeln)"
            if (z["polarisation_ende"] or 0) >= 0.5 and ne >= 3 and (z["polarisation_ende"] or 0) - (
                    z["polarisation_start"] or 0) >= 0.3:
                z["kollektiv"] += "; Schwarm (Ausrichtung)"
            ergebnis.setdefault(stufe, []).append(z)
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn = {"kollektiv": {n: z["kollektiv"] for n, z in grob.items()}, "klassen": {n: z["klasse"] for n, z in grob.items()}}
    if "fein" in ergebnis:
        kenn["L3"] = l3_klassen(ergebnis)
    ausgabe = {"karte": "kollektiv (Bio 26 Schleimpilz, Bio 40 Schwarm)", "start": start, "ende": jetzt(), "rauch": rauch,
               "dauer_s": dauer, "geraet": geraet_name(),
               "parameter": {"omega2": W2_STD, "N": K_N, "R_scheibe": K_RSCHEIBE, "v": K_V, "seed": K_SEED, "L": K_L,
                             "T": K_T, "stufen": STUFEN},
               "aufbau": {"orte": orte, "phasen": phasen, "richtungen": richt}, "profil": profil_info(pr),
               "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Bio 26 Schleimpilz und Bio 40 Schwarm: zwoelf verstreute Baelle", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text += gruppen_text(ergebnis, lambda z: (f" | {z['kollektiv']} | Polarisation {fz(z['polarisation_start'])}->"
                                             f"{fz(z['polarisation_ende'])} | Phasenordnung {fz(z['phasenordnung_start'])}"
                                             f"->{fz(z['phasenordnung_ende'])} | groesster Anteil "
                                             f"{fz(z['anteil_groesster_klumpen'])}"))
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "kollektiv", ausgabe, "\n".join(text))


# ---------------------------------------------------------------- Hauptprogramm

KARTEN = {"profile": test_profile, "paare": test_paare, "gitter": test_gitter, "ringe": test_ringe,
          "gluehwurm": test_gluehwurm, "haendigkeit": test_haendigkeit, "isomere": test_isomere,
          "kollektiv": test_kollektiv}


def main():
    global DEV, N_KAND, STUFEN, RAUCH_FAKTOR
    ap = argparse.ArgumentParser(description="Runde 5/6, Paket 2D-B (Kollektiv und Kristall)")
    ap.add_argument("karte", choices=list(KARTEN) + ["alle"])
    ap.add_argument("--rauch", action="store_true", help="Laufzeiten x 0,05; nur Durchlauf und Hochrechnung")
    ap.add_argument("--mini", action="store_true", help="nur mit --rauch: Formprobe (256 Kandidaten, dx 0,6/0,4, x 0,02)")
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda",
                    help="cpu nur fuer die Formprobe mit --rauch --mini, nie fuer Messlaeufe")
    ap.add_argument("--stufe", choices=["grob", "fein", "beide"], default="beide")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.geraet == "cpu" and not (args.rauch and args.mini):
        raise SystemExit("--geraet cpu nur zusammen mit --rauch --mini (Formprobe); Messlaeufe nur auf CUDA.")
    if args.mini and not args.rauch:
        raise SystemExit("--mini nur zusammen mit --rauch.")
    DEV = torch.device(args.geraet)
    if DEV.type == "cuda" and not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg fuer Messlaeufe).")
    if DEV.type == "cpu":
        torch.set_num_threads(1)
    if args.mini:
        N_KAND = 256
        STUFEN = (("grob", 0.6, 0.1), ("fein", 0.4, 0.05))
        RAUCH_FAKTOR = 0.02
    if args.karte == "alle" and not args.rauch:
        raise SystemExit("'alle' nur mit --rauch (sonst ueber 10 min).")
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), "rauchtest" if args.rauch else "ausgabe")
    CACHE["pfad"] = os.path.join(out, "profil_cache.pt")
    stufen = ("grob", "fein") if args.stufe == "beide" else (args.stufe,)
    namen = list(KARTEN) if args.karte == "alle" else [args.karte]
    fehler = []
    for name in namen:
        if len(namen) == 1:
            KARTEN[name](out, args.rauch, stufen, args)
            continue
        try:
            KARTEN[name](out, args.rauch, stufen, args)
        except (Exception, SystemExit) as exc:
            traceback.print_exc()
            print(f"FEHLER in Karte {name}: {exc!r}", flush=True)
            fehler.append(name)
    if fehler:
        raise SystemExit(f"Karten mit Fehler: {fehler}")


if __name__ == "__main__":
    main()
