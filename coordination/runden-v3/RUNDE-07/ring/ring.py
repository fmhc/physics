#!/usr/bin/env python3
"""Runde 7 (v3), Karte RING: Wirbelball aus einem Ring und Vierer-Ring. 2D, Ein-Feld-Modell, explorativ.

Unterbefehle (Plan, Vorhersagen, Aufrufe und Latten in PLAN.md daneben):
    profile  Schiessen aller benutzten Profile: m = 1 bei omega^2 0,540 ... 0,660 (Schritt 0,005), m = 0 bei
             0,54 ... 0,66 (Schritt 0,01) und 0,70. Q(omega), Formdaten; fuellt den Profilcache.
    wirbel   Frage (a): mitdrehende Ringe N6/N8 mit Phasenstufe 2 pi/N wie "ringe" in r5_2d_b.py (N6_k1_dreh+,
             N8_k1_dreh+), lang (T 3000 grob, 1000 fein), ohne Stoerung und mit Saat 1e-2 (N6, N8), 1e-3, 1e-4 (N6). Windung auf acht Kreisen um den
             Schwerpunkt, Wirbelzaehlung, J/Q, Frequenz, Radialprofil gegen den stationaeren m = 1-Ball (Gegenprobe m = 0)
             derselben Ladung, Teilung nach dem Verschmelzen.
    teilung  Frage (a), Anschluss Teilung: ruhender m = 1-Ball mit 1-%-Stoerung wie "teilung" in r5_2d_a.py bei
             omega^2 0,55 / 0,575 / 0,59 / 0,60 / 0,625 / 0,65, T 3000 grob, 1500 fein.
    vierer   Frage (b): Vierer-Ring mit Windung 2 pi/4 wie "vielzeller" n4_windung in r5_2d_a.py, T 2000 grob, 1000 fein,
             mit Gegenproben (ohne Windung, gegenlaeufig, groesserer Abstand), C4-Sektor und gesetzter Asymmetrie.
    alle     nur mit --rauch: alle Unterbefehle nacheinander.
Kontrollen (c) in jedem Unterbefehl: Bilanz von Ladung, Drehimpuls und Energie gegen das, was die Randschicht schluckt;
L3 (fein gegen grob, sobald beide Stufen im Ausgabeordner liegen); Plausibilitaetsschranken je Lauf.

Modell (wie r5_2d_a.py, r5_2d_b.py): L = |psi_t|^2 - |grad psi|^2 - U(S), S = |psi|^2, U(S) = S - S^2 + S^3/2.
    Ladungsdichte rho = 2 Im(psi conj(psi_t)), Energiedichte |psi_t|^2 + |grad psi|^2 + U(S),
    Impulsdichte p_i = -2 Re(conj(psi_t) d_i psi), Drehimpuls J = Int (x p_y - y p_x); fuer f e^{i m theta - i omega t}
    gilt J = m Q und Q = 2 omega Int S.

Grundlage und Aenderungen:
    Aus r5_2d_b.py unveraendert: Schiessen mit der fuer |m| >= 1 berichtigten Unterschussregel, Profilcache, Hermite,
    Gitter mit Randschicht, ruhende und Lorentz-geboostete Baelle, Velocity-Verlet, Dichten, Glaettung, Gebiete, Windung auf
    dem Kreis, Klumpen, Ball-Verfolger, Ringaufbau (ring_geschw, Aufbau aus test_ringe), Hilfsfunktionen.
    Aus r5_2d_a.py unveraendert: Stoerfaktor (Moden l = 1..6, Amplitude 0,01, Phase 2,4 l), azimutale Moden A_l, Vieleck.
    Neu bzw. geaendert:
      1. Messabstand 0,5 (statt 1); je Messung die Verlustraten der Randschicht fuer Q, J und E (Bilanz, Trapezregel).
      2. Klumpenfenster (Radius r_win) um den verfolgten Schwerpunkt (Gewicht S^2): Q, E, J um den Schwerpunkt, N = Int S,
         omega_eff = Q/(2 N), S-gewichtete Frequenz, Impuls, A_l; je Analyse Windung auf acht Kreisen, Radialprofil und
         Wirbelzaehlung (Plaketten) um den Fensterschwerpunkt.
      3. Wahlweise Projektion auf den C4-Sektor mit Windung w, psi(R^-1 x) = e^{-i w pi/2} psi(x), alle 0,5 Zeiteinheiten
         (psi, psi_t und Kraft); das Gitter ist unter 90-Grad-Drehung exakt symmetrisch.
      4. Ballamplitude "amp" (Saat einer Asymmetrie); klumpen() nimmt eine Mindestladung je Lauf.
      5. Profilcache neben dem Skript (Schluessel enthaelt alle Schiessparameter), von --out unabhaengig.
      6. Ergebnisse je Stufe (<karte>_<stufe>_...); L3 entsteht, sobald beide Stufen im Ausgabeordner liegen.

Aufruf:  python ring.py KARTE [--rauch [--mini]] [--stufe grob|fein|beide] [--laeufe A,B] [--out ORDNER] [--geraet cuda|cpu]
Rauchtest: --rauch (Laufzeiten x 0,05; Zahlen ungueltig, nur Durchlauf und Hochrechnung).
Formprobe: --rauch --mini (256 Kandidaten, dx 0,6/0,4, Laufzeiten x 0,02); nur damit ist --geraet cpu erlaubt.
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

DEV = torch.device("cuda")
F64 = torch.float64
C128 = torch.complex128

# ---- Aus r5_2d_b.py / r5_2d_a.py unveraendert ----
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
ANALYSE_DT = 5.0
W2_STD = 0.70            # Ringball m = 0: R_halb 1,92, Q 24,0
SPALT = 4.0              # Abstand d = 2 R_halb + SPALT (ringe und vielzeller)
Q_KLUMPEN = 0.25         # ringe: Klumpen zaehlt ab 0,25 Q_1
Q_MIN_REL = 0.03         # teilung: Gebiete unter 3 % der Anfangsladung zaehlen nicht
S_DICHT_REL = 0.1
R_WIN_PLUS = 2.5
RAND_ABSTAND = 2.0
STOER_EPS, STOER_LMAX, STOER_PHI = 0.01, 6, 2.4     # r5_2d_a.py: T1_EPS, T1_LMAX, T1_PHI

# ---- Neu (vor dem Lauf festgelegt, PLAN.md Abschnitt 1) ----
T_MEAS = 0.5
M1_GITTER = tuple(round(0.540 + 0.005 * i, 3) for i in range(25))         # 0,540 ... 0,660
M0_GITTER = tuple(round(0.54 + 0.01 * i, 2) for i in range(13))           # 0,54 ... 0,66
KREISE = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0)
RAD_DR, RAD_NBIN = 0.25, 64
TOL = {"Q": 1e-3, "J": 3e-3, "E": 1e-3}   # Bilanz: groesster Rest relativ zu Q_Box(0) (Q, J) bzw. E_Box(0)
S_MIN_SICHER = 0.05                       # Windung auf einem Kreis gilt nur mit S_min >= 0,05 (wie r5_2d_b.py)

# wirbel (a)
W_L, W_RWIN = 48.0, 15.0
W_T = {"grob": 3000.0, "fein": 1000.0}
W_LAEUFE = (("N6_dreh+", 6, 0.0), ("N8_dreh+", 8, 0.0), ("N6_dreh+_s1e-2", 6, 1e-2), ("N8_dreh+_s1e-2", 8, 1e-2),
            ("N6_dreh+_s1e-3", 6, 1e-3), ("N6_dreh+_s1e-4", 6, 1e-4), ("N8_ruhend", 8, 0.0))
# Saat: Stoerfaktor l = 1..6 am Ringradius; "ruhend" = N8_k1 aus ringe (Phasenstufe, ohne Drehung), sonst mitdrehend
W_FEIN = ("N6_dreh+", "N8_dreh+", "N6_dreh+_s1e-2")

# teilung (a)
T_L = 38.4
T_T = {"grob": 3000.0, "fein": 1500.0}
T_W2 = (0.55, 0.575, 0.59, 0.60, 0.625, 0.65)
T_FEIN = (0.59, 0.625)
T_NACH = 30.0            # Toechter 30 Zeiteinheiten nach der Teilung vermessen (wie r5_2d_a.py)

# vierer (b): (Name, Luecke, Windung w, C4-Projektion, Saat auf Ball 0)
V_L = 38.4
V_T = {"grob": 2000.0, "fein": 1000.0}
V_LAEUFE = (("n4_windung", 4.0, 1, False, 0.0), ("n4_windung_sym", 4.0, 1, True, 0.0),
            ("n4_windung_s1e-3", 4.0, 1, False, 1e-3), ("n4_windung_s1e-6", 4.0, 1, False, 1e-6),
            ("n4_gegen", 4.0, -1, False, 0.0), ("n4_gleich", 4.0, 0, False, 0.0),
            ("n4_windung_l6", 6.0, 1, False, 0.0), ("n4_windung_l6_sym", 6.0, 1, True, 0.0),
            ("n4_windung_l8_sym", 8.0, 1, True, 0.0))
V_FEIN = ("n4_windung_sym", "n4_windung_s1e-6")
V_SPREAD_BRUCH, V_SPREAD_TAUSCH = 0.1, 0.3   # Ladungsspreizung (max - min)/Mittel der vier Verfolger

_PROFILE = {}
CACHE = {"pfad": None}
AUSWAHL = {"laeufe": None}


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


# ---------------------------------------------------------------- Profil durch Schiessen (aus r5_2d_b.py)

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
    """Wie r5_2d_b.py: erst Speicher, dann Plattencache, sonst ein Schiessdurchgang fuer alle fehlenden Zeilen zugleich;
    neue Profile werden atomar (os.replace) in den Plattencache geschrieben."""
    liste = [(round(float(w2), 6), int(m)) for w2, m in liste]
    platte = {}
    if CACHE["pfad"] and os.path.exists(CACHE["pfad"]):
        try:
            platte = torch.load(CACHE["pfad"], map_location="cpu", weights_only=False)
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
            os.makedirs(os.path.dirname(CACHE["pfad"]) or ".", exist_ok=True)
            tmp = CACHE["pfad"] + f".tmp{os.getpid()}"
            torch.save(platte, tmp)
            os.replace(tmp, CACHE["pfad"])
    return {k: _PROFILE[k] for k in liste}


def alle_profile():
    return [(w2, 1) for w2 in M1_GITTER] + [(w2, 0) for w2 in M0_GITTER] + [(W2_STD, 0)]


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
    """Periodische Box [-L, L)^2 mit Randschicht (wie r5_2d_b.py); x_j = -L + j dx liegt spiegelsymmetrisch und geht bei
    90-Grad-Drehung in sich ueber (Index j -> (n - j) mod n)."""

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
    """baelle: Liste von dicts {pr, m, x, y, phase, [v, winkel], [eps_r, eps_w], [amp]}; Rueckgabe psi, psi_t (1, n, n).
    Neu: amp (Amplitudenfaktor eines Balls, Saat einer Asymmetrie)."""
    psi = torch.zeros((1, g.n, g.n), dtype=C128, device=DEV)
    vel = torch.zeros_like(psi)
    for b in baelle:
        if b.get("v", 0.0) != 0.0:
            p_, v_ = ball_bewegt(g, b["pr"], b.get("m", 0), b["x"], b["y"], b["v"], b["winkel"], b.get("phase", 0.0))
        else:
            p_, v_ = ball_feld(g, b["pr"], b.get("m", 0), b["x"], b["y"], b.get("phase", 0.0), b.get("eps_r", 0.0),
                               b.get("eps_w", 0.0))
        a = b.get("amp", 1.0)
        psi = psi + a * p_
        vel = vel + a * v_
    return psi, vel


def stoerfaktor(g, x0, y0, r_s, eps, lmax=STOER_LMAX, phi=STOER_PHI):
    """Aus r5_2d_a.py: 1 + eps Sum_{l=1..lmax} Re[e^{i phi l} (z/r_s)^l] exp(-l (r^2/r_s^2 - 1)/2).
    Jede Mode hat bei r = r_s genau die Amplitude eps; glatt im Zentrum (Polynom mal Gauss)."""
    X = g.x - x0
    Y = g.y - y0
    z = (X + 1j * Y) / r_s
    u2 = (X * X + Y * Y) / (r_s * r_s)
    fak = torch.ones_like(u2)
    zl = torch.ones_like(z)
    for l in range(1, lmax + 1):
        zl = zl * z
        fak = fak + eps * (zl * cmath.exp(1j * phi * l)).real * torch.exp(-0.5 * l * (u2 - 1.0))
    return fak


def vieleck(n_b, d):
    """Aus r5_2d_a.py: Ecken eines regelmaessigen n-Ecks mit Seitenlaenge d um den Ursprung (Quadrat achsparallel),
    gegen den Uhrzeigersinn."""
    if n_b == 1:
        return [(0.0, 0.0)]
    rad = d / (2.0 * math.sin(math.pi / n_b))
    anf = 0.5 * math.pi if n_b == 3 else 0.25 * math.pi
    return [(rad * math.cos(anf + 2.0 * math.pi * k / n_b), rad * math.sin(anf + 2.0 * math.pi * k / n_b))
            for k in range(n_b)]


def drehe(A):
    """(R A)(x) = A(R^-1 x), R = Drehung um +90 Grad um den Ursprung; A (B, n, n) mit Zeile = y, Spalte = x.
    (R A)[i, j] = A[(n - j) mod n, i]."""
    n = A.shape[-1]
    idx = torch.remainder(-torch.arange(n, device=A.device), n)
    return A[:, idx, :].transpose(1, 2)


def projektion_c4(A, w):
    """Projektion auf den Sektor R A = lam A mit lam = e^{-i w pi/2} (Windung w einer Viererkette gegen den Uhrzeigersinn):
    P = (1/4) Sum_k conj(lam)^k R^k."""
    lam = cmath.exp(-1j * w * math.pi / 2.0)
    aus = A.clone()
    B = A
    for k in range(1, 4):
        B = drehe(B)
        aus = aus + (lam.conjugate() ** k) * B
    return aus / 4.0


def entwickeln(g, psi, vel, dt, t_end, t_mess, messen, proj=None):
    """Velocity-Verlet (wie r5_2d_b.py) fuer einen Stapel (B, n, n); Laplace spektral; Randschicht psi_t -> psi_t e^{-sigma dt}.
    Neu: proj(psi, vel, F) wird vor jeder Messung aufgerufen (C4-Projektion, in place)."""
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
            if proj is not None:
                proj(psi, vel, F)
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
    """Wie r5_2d_b.py; neu: q_min darf eine Liste je Lauf sein."""
    s, rho, e, px, py, jz = dicht
    lab = komponenten(maske)
    alle = []
    for b in range(maske.shape[0]):
        qm = q_min[b] if isinstance(q_min, (list, tuple)) else q_min
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
            if qq < qm:
                continue
            d = {"Q": qq, "E": ee, "X": xx, "Y": yy, "vx": pxx / ee, "vy": pyy / ee, "Jspin_Q": js / qq,
                 "r_mittel": rb, "phase": pp}
            if windung:
                d["windung"], d["S_min_kreis"] = windung_kreis(g, psi[b], xx, yy, rb)
                d["windung_sicher"] = d["S_min_kreis"] >= S_MIN_SICHER
            liste.append(d)
        liste.sort(key=lambda d: -d["Q"])
        alle.append(liste)
    return alle


def verfolger(g, psi, vel, cx, cy, off, r_w):
    """Aus r5_2d_b.py: je Ball ein Fenster (Radius r_w) um den letzten Ort. Neuer Ort = Schwerpunkt mit Gewicht S^2; dazu
    Ladung, innere Phase arg(Sum psi S), R_rms (Gewicht S), S_max. cx, cy: (B, K). Rueckgabe cx, cy, Werte (B, K, 6)."""
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


def azimut(g, s, zx, zy, r_win, l_max):
    """Aus r5_2d_a.py: A_l = |Sum S e^{-i l theta}| / Sum S im Fenster r < r_win um (zx, zy), l = 1..l_max (B, l_max);
    neu: r_win als Tensor (B,)."""
    X = g.x - zx.view(-1, 1, 1)
    Y = g.y - zy.view(-1, 1, 1)
    r2 = X * X + Y * Y
    w = s * (r2 < (r_win * r_win).view(-1, 1, 1)).to(F64)
    u = (X - 1j * Y) / torch.sqrt(r2).clamp(min=1e-12)
    ws = w.sum((1, 2))
    ul = torch.ones_like(u)
    aus = []
    for _ in range(l_max):
        ul = ul * u
        aus.append((w * ul).sum((1, 2)).abs() / ws)
    return torch.stack(aus, dim=1)


FENSTER_SPALTEN = ["x", "y", "Q_w", "E_w", "J_w", "N_w", "Px_w", "Py_w", "S_max_w", "SR_w", "S2_w"]


def fenster_messung(g, dicht, zx, zy, r_win, l_max):
    """Neu: Klumpenfenster r < r_win um den alten Schwerpunkt. Neuer Schwerpunkt mit Gewicht S^2 (wie r5_2d_a.py);
    Q, E, J um den neuen Schwerpunkt, N = Int S, Impuls, S_max, Int S rho und Int S^2 (S-gewichtete Frequenz), A_l."""
    s, rho, e, px, py, jz = dicht
    X = g.x - zx.view(-1, 1, 1)
    Y = g.y - zy.view(-1, 1, 1)
    fen = ((X * X + Y * Y) < (r_win * r_win).view(-1, 1, 1)).to(F64)
    w = s * s * fen
    wsum = w.sum((1, 2))
    da = wsum > 1e-200
    xc = torch.where(da, zx + (w * X).sum((1, 2)) / wsum.clamp(min=1e-300), zx)
    yc = torch.where(da, zy + (w * Y).sum((1, 2)) / wsum.clamp(min=1e-300), zy)
    Xc = g.x - xc.view(-1, 1, 1)
    Yc = g.y - yc.view(-1, 1, 1)
    dA = g.dA
    spalten = [xc, yc, (rho * fen).sum((1, 2)) * dA, (e * fen).sum((1, 2)) * dA,
               ((Xc * py - Yc * px) * fen).sum((1, 2)) * dA, (s * fen).sum((1, 2)) * dA,
               (px * fen).sum((1, 2)) * dA, (py * fen).sum((1, 2)) * dA, (s * fen).amax((1, 2)),
               (s * rho * fen).sum((1, 2)) * dA, (s * s * fen).sum((1, 2)) * dA]
    if l_max:
        spalten += list(azimut(g, s, xc, yc, r_win, l_max).unbind(1))
    return xc, yc, torch.stack(spalten, dim=1)


def radialprofil_um(g, s, xc, yc):
    """Neu: azimutal gemitteltes S(r) um (xc, yc) je Lauf, Ringe der Breite RAD_DR; Rueckgabe (B, RAD_NBIN)."""
    B = s.shape[0]
    r = torch.sqrt((g.x - xc.view(-1, 1, 1)) ** 2 + (g.y - yc.view(-1, 1, 1)) ** 2)
    kk = torch.floor(r / RAD_DR).long().clamp(max=RAD_NBIN) + (RAD_NBIN + 1) * torch.arange(B, device=DEV).view(-1, 1, 1)
    kk = kk.reshape(-1)
    summe = torch.zeros(B * (RAD_NBIN + 1), dtype=F64, device=DEV).index_add_(0, kk, s.reshape(-1))
    zahl = torch.zeros(B * (RAD_NBIN + 1), dtype=F64, device=DEV).index_add_(0, kk, torch.ones_like(s).reshape(-1))
    return (summe / zahl.clamp(min=1.0)).view(B, RAD_NBIN + 1)[:, :RAD_NBIN]


def wirbel_zaehlen(g, psi, xc, yc):
    """Neu: Phasenumlauf je Gitterplakette (gegen den Uhrzeigersinn). Rueckgabe je Lauf: Zahl der +1- und -1-Wirbel mit
    Plakettenmitte in r < 4 und r < 8 um (xc, yc), Abstand des naechsten Wirbels (beliebiges Vorzeichen)."""
    ph = torch.angle(psi)

    def wr(d):
        return torch.remainder(d + math.pi, 2.0 * math.pi) - math.pi

    p01 = ph.roll(-1, 2)
    p11 = p01.roll(-1, 1)
    p10 = ph.roll(-1, 1)
    w = torch.round((wr(p01 - ph) + wr(p11 - p01) + wr(p10 - p11) + wr(ph - p10)) / (2.0 * math.pi))
    X = g.x + 0.5 * g.dx - xc.view(-1, 1, 1)
    Y = g.y + 0.5 * g.dx - yc.view(-1, 1, 1)
    r2 = X * X + Y * Y
    aus = []
    for R in (4.0, 8.0):
        m = r2 < R * R
        aus += [((w > 0.5) & m).sum((1, 2)), ((w < -0.5) & m).sum((1, 2))]
    d = torch.where(w.abs() > 0.5, r2, torch.full_like(r2, 999.0 ** 2)).amin((1, 2)).sqrt()   # 999: kein Wirbel
    return [a.tolist() for a in aus] + [d.tolist()]


def lauf(g, psi, vel, dt, t_end, q_min, zentren=None, r_w=None, fenster=None, l_max=0, sym=(), windung=True):
    """Zeitentwicklung mit Messungen je T_MEAS:
       glob (M, B, 7): Q_Box, E_Box, J_Box, S_max und die Verlustraten der Randschicht L_Q = Int sigma rho,
       L_J = Int sigma j_z, L_E = Int 2 sigma |psi_t|^2;
       mit zentren (B, K, 2) und r_w: Verfolger je Ball (r5_2d_b.py) -> bahn (M, B, K, 6);
       mit fenster (Radien je Lauf): Klumpenfenster -> fen (M, B, 11 + l_max).
       Je ANALYSE_DT: Klumpen (mit Windung) und dichte Ladung (r5_2d_b.py); mit fenster zusaetzlich Windung auf den
       Kreisen KREISE, Radialprofil und Wirbelzaehlung um den Fensterschwerpunkt.
       sym: Liste (b, w): diese Laeufe werden vor jeder Messung auf den C4-Sektor mit Windung w projiziert."""
    B = psi.shape[0]
    s0 = psi.real ** 2 + psi.imag ** 2
    s_ref = unschaerfe(g, s0).amax((1, 2))
    schwelle = (SCHWELLE_REL * s_ref).view(-1, 1, 1)
    schwelle_dicht = (S_DICHT_REL * s_ref).view(-1, 1, 1)
    verlauf = [[] for _ in range(B)]
    extra = [[] for _ in range(B)]
    radial = []
    zaehler = [0]
    alle = max(1, int(round(ANALYSE_DT / T_MEAS)))
    zust = {}
    off = None
    if zentren is not None:
        zust["cx"] = zentren[:, :, 0].clone()
        zust["cy"] = zentren[:, :, 1].clone()
        ww = int(math.ceil(r_w / g.dx)) + 1
        off = torch.arange(-ww, ww + 1, device=DEV)
    if fenster is not None:
        zust["zx"] = torch.zeros(B, dtype=F64, device=DEV)
        zust["zy"] = torch.zeros(B, dtype=F64, device=DEV)
        r_win = torch.as_tensor(fenster, dtype=F64, device=DEV).view(-1)
    sig = g.sigma

    def messen(psi, vel):
        dicht = dichten(g, psi, vel)
        s, rho, e, px, py, jz = dicht
        v2 = vel.real ** 2 + vel.imag ** 2
        aus = [torch.stack([rho.sum((1, 2)) * g.dA, e.sum((1, 2)) * g.dA, jz.sum((1, 2)) * g.dA, s.amax((1, 2)),
                            (sig * rho).sum((1, 2)) * g.dA, (sig * jz).sum((1, 2)) * g.dA,
                            (2.0 * sig * v2).sum((1, 2)) * g.dA], dim=1)]
        if zentren is not None:
            zust["cx"], zust["cy"], bahn = verfolger(g, psi, vel, zust["cx"], zust["cy"], off, r_w)
            aus.append(bahn)
        if fenster is not None:
            zust["zx"], zust["zy"], fw = fenster_messung(g, dicht, zust["zx"], zust["zy"], r_win, l_max)
            aus.append(fw)
        if zaehler[0] % alle == 0:
            t_jetzt = zaehler[0] * T_MEAS
            glatt = unschaerfe(g, s)
            q_dicht = ((rho * (glatt > schwelle_dicht)).sum((1, 2)) * g.dA).tolist()
            kl = klumpen(g, psi, dicht, glatt > schwelle, q_min, windung)
            for b in range(B):
                verlauf[b].append((t_jetzt, q_dicht[b], kl[b]))
            if fenster is not None:
                radial.append(radialprofil_um(g, s, zust["zx"], zust["zy"]))
                wz = wirbel_zaehlen(g, psi, zust["zx"], zust["zy"])
                zx, zy = zust["zx"].tolist(), zust["zy"].tolist()
                for b in range(B):
                    extra[b].append({"t": t_jetzt, "kreise": [windung_kreis(g, psi[b], zx[b], zy[b], rc) for rc in KREISE],
                                     "wirbel": [x[b] for x in wz]})
        zaehler[0] += 1
        return tuple(aus)

    proj = None
    if sym:
        gruppen = {}
        for b, w in sym:
            gruppen.setdefault(w, []).append(b)
        idx = {w: torch.tensor(bs, device=DEV) for w, bs in gruppen.items()}

        def proj(psi, vel, F):
            for w, ib in idx.items():
                for A in (psi, vel, F):
                    A[ib] = projektion_c4(A[ib], w)

    t, daten = entwickeln(g, psi, vel, dt, t_end, T_MEAS, messen, proj)
    aus = {"glob": daten[0]}
    i = 1
    if zentren is not None:
        aus["bahn"] = daten[i]
        i += 1
    if fenster is not None:
        aus["fen"] = daten[i]
        aus["radial"] = torch.stack(radial)
    return t, aus, verlauf, extra


def stufe_rechnen(karte, stufe, dx, dt, L, t_end, laeufe, bauen, q_min, out, dauer, r_w=None, fenster=None, l_max=0,
                  sym=None, nachbau=None, vorher=None):
    """Baut alle Laeufe der Stufe (bauen(g, lauf) -> Ball-dicts; nachbau(g, lauf, psi, vel) -> psi, vel), entwickelt sie als
    Stapel und sichert die Rohdaten sofort (<karte>_<stufe>_roh.pt). vorher(g, psi, vel) liefert Zusatzwerte vor dem Lauf
    (z. B. Sektorabweichung). Rueckgabe g, t, daten, verlauf, extra, orte, vorab."""
    g = Gitter(L, dx)
    psis, vels, orte = [], [], []
    for lauf_ in laeufe:
        baelle = bauen(g, lauf_)
        p_, v_ = summe_baelle(g, baelle)
        if nachbau is not None:
            p_, v_ = nachbau(g, lauf_, p_, v_)
        psis.append(p_)
        vels.append(v_)
        orte.append([(b["x"], b["y"]) for b in baelle])
    psi = torch.cat(psis).contiguous()
    vel = torch.cat(vels).contiguous()
    del psis, vels
    vorab = vorher(g, psi, vel) if vorher is not None else {}
    zentren = None
    if r_w is not None:
        K = max(len(o) for o in orte)
        zentren = torch.tensor([o + [o[0]] * (K - len(o)) for o in orte], dtype=F64, device=DEV)
    t0 = uhr()
    t, daten, verlauf, extra = lauf(g, psi, vel, dt, t_end, q_min, zentren, r_w, fenster, l_max, sym or ())
    dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
    print(f"{karte}: Entwicklung {stufe} ({len(laeufe)} Laeufe, n = {g.n}, T = {t_end:g}) fertig nach "
          f"{dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
    os.makedirs(out, exist_ok=True)
    torch.save({"t": t.cpu(), **{k: v.cpu() for k, v in daten.items()}, "verlauf": verlauf, "extra": extra,
                "laeufe": [l[0] for l in laeufe], "orte": orte, "dx": dx, "dt": dt, "L": L, "T": t_end, "vorab": vorab,
                "spalten_glob": ["Q_box", "E_box", "J_box", "S_max", "L_Q", "L_J", "L_E"],
                "spalten_bahn": ["x", "y", "Q_ball", "phase", "R_rms", "S_max"],
                "spalten_fen": FENSTER_SPALTEN + [f"A{l}" for l in range(1, l_max + 1)],
                "kreise": KREISE, "rad_dr": RAD_DR}, os.path.join(out, f"{karte}_{stufe}_roh.pt"))
    return g, t, daten, verlauf, extra, orte, vorab


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


def entfalten(ph):
    d = torch.remainder(ph[1:] - ph[:-1] + math.pi, 2.0 * math.pi) - math.pi
    return torch.cat([ph[:1], ph[:1] + torch.cumsum(d, dim=0)], dim=0)


def schwuenge(x, h):
    """Aus r5_2d_b.py: Zahl der Richtungswechsel einer Reihe mit Hub >= h (Hysterese)."""
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


def fz(x, f="{:.3f}"):
    return f.format(x) if isinstance(x, (int, float)) and x is not None and not isinstance(x, bool) else "-"


def bilanz(t, glob, b):
    """Neu: kumulierte Verluste in der Randschicht (Trapezregel ueber die Raten je Messung) und Rest der Bilanz
    X_Box(t) + X_geschluckt(t) - X_Box(0). Q und J relativ zu Q_Box(0), E relativ zu E_Box(0). Q ist im Verfahren exakt
    erhalten (Rest = Quadraturfehler der Verlustrate); J nur bis auf die Gitteranisotropie."""
    aus = {}
    q0, e0 = abs(glob[0, b, 0].item()), abs(glob[0, b, 1].item())
    dtm = t[1:] - t[:-1]
    for name, i_box, i_rate, skala in (("Q", 0, 4, q0), ("J", 2, 5, q0), ("E", 1, 6, e0)):
        rate = glob[:, b, i_rate]
        kum = torch.cat([torch.zeros(1, dtype=F64, device=rate.device),
                         torch.cumsum(0.5 * (rate[1:] + rate[:-1]) * dtm, 0)])
        rest = glob[:, b, i_box] + kum - glob[0, b, i_box]
        rmax = (rest.abs().max() / max(skala, 1e-300)).item()
        aus[name] = {"start": glob[0, b, i_box].item(), "ende": glob[-1, b, i_box].item(), "geschluckt": kum[-1].item(),
                     "rest_max_rel": rmax, "rest_ende_rel": (rest[-1] / max(skala, 1e-300)).item(),
                     "ok": rmax <= TOL[name]}
    return aus


def bilanz_text(bz):
    return " ".join(f"{k}: {v['start']:+.3f}->{v['ende']:+.3f} geschluckt {v['geschluckt']:+.3f} Rest {v['rest_max_rel']:.1e}"
                    f"{'' if v['ok'] else ' (UEBER TOLERANZ)'}" for k, v in bz.items())


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
                      f"+ Entwicklung x {1 / RAUCH_FAKTOR:.0f}); Profile aus dem Cache. Ueber 480 s: Stufen einzeln "
                      "(--stufe grob / --stufe fein) oder Laeufe teilen (--laeufe).")
    return zeilen


def kopf(titel, start, rauch):
    return (f"{titel}. Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}"
            + (" RAUCHTEST: Zahlen ungueltig" if rauch else ""))


def waehlen(laeufe, stufe, fein, name=lambda l: l[0]):
    """Laeufe der Stufe (fein: nur die genannten), eingeschraenkt durch --laeufe."""
    aus = [l for l in laeufe if stufe == "grob" or name(l) in fein]
    if AUSWAHL["laeufe"]:
        aus = [l for l in aus if l[0] in AUSWAHL["laeufe"]]
    return aus


def l3_datei(out, karte, vergleich):
    """L3, sobald grob und fein im Ausgabeordner liegen: vergleich(grob_json, fein_json) -> dict; schreibt <karte>_L3."""
    pf = {st: os.path.join(out, f"{karte}_{st}_ergebnis.json") for st in ("grob", "fein")}
    if not all(os.path.exists(p) for p in pf.values()):
        return None
    with open(pf["grob"]) as fh:
        zg = json.load(fh)
    with open(pf["fein"]) as fh:
        zf = json.load(fh)
    if zg.get("rauch") != zf.get("rauch"):
        return None
    l3 = vergleich(zg, zf)
    text = [f"L3 {karte}: fein gegen grob (Stand {jetzt()})"] + [f"  {z}" for z in l3.get("zeilen", [])]
    text.append(f"L3 bestanden: {l3.get('bestanden')}")
    schreiben(out, f"{karte}_L3", l3, "\n".join(text))
    return l3


# ---------------------------------------------------------------- Profile: Interpolation bei gegebener Ladung

def profil_bei_q(q, m):
    """Neu: Profil im Gitter (m = 1: M1_GITTER, m = 0: M0_GITTER) mit Ladung q, linear in ln Q zwischen den zwei
    Nachbarzeilen; keine Extrapolation (dann None). Rueckgabe omega2, Gewicht a, beide Profile, E/Q."""
    if not (isinstance(q, float) and q > 0.0 and math.isfinite(q)):
        return None
    gitter = M1_GITTER if m == 1 else M0_GITTER
    prof = profile_holen([(w2, m) for w2 in gitter])
    zeilen = [(w2, prof[(round(w2, 6), m)]) for w2 in gitter if prof[(round(w2, 6), m)]["gueltig"]]
    for (wa, pa), (wb, pb) in zip(zeilen[:-1], zeilen[1:]):
        if min(pa["Q"], pb["Q"]) <= q <= max(pa["Q"], pb["Q"]):
            a = (math.log(pa["Q"]) - math.log(q)) / (math.log(pa["Q"]) - math.log(pb["Q"]))
            return {"omega2": wa + a * (wb - wa), "a": a, "pa": pa, "pb": pb,
                    "E_Q": (1.0 - a) * pa["E"] / pa["Q"] + a * pb["E"] / pb["Q"], "zwischen": [wa, wb]}
    return None


def profil_s(ip, rc):
    fa, _ = hermite(ip["pa"], rc)
    fb, _ = hermite(ip["pb"], rc)
    return (1.0 - ip["a"]) * fa * fa + ip["a"] * fb * fb


def form(rc, s):
    """S_max, Ort des Maximums, innerer und aeusserer Halbwertsradius eines Radialprofils (Listen)."""
    i_m = max(range(len(s)), key=lambda i: s[i])
    sm = s[i_m]
    innen = 0.0
    if s[0] < 0.5 * sm:
        for i in range(1, i_m + 1):
            if s[i] >= 0.5 * sm:
                innen = rc[i - 1] + (0.5 * sm - s[i - 1]) / max(s[i] - s[i - 1], 1e-300) * (rc[i] - rc[i - 1])
                break
    aussen = None
    for i in range(i_m + 1, len(s)):
        if s[i] < 0.5 * sm:
            aussen = rc[i - 1] + (s[i - 1] - 0.5 * sm) / max(s[i - 1] - s[i], 1e-300) * (rc[i] - rc[i - 1])
            break
    return {"S_max": sm, "R_max": rc[i_m], "R_kern_halb": innen, "R_halb": aussen}


def profil_abweichung(s_mess, s_prof, rc):
    return math.sqrt(float((((s_mess - s_prof) ** 2) * rc).sum() / ((s_prof ** 2) * rc).sum().clamp(min=1e-300)))


# ---------------------------------------------------------------- profile

def test_profile(out, rauch, stufen, args):
    start = jetzt()
    print(f"Profile Start {start} auf {geraet_name()}", flush=True)
    t0 = uhr()
    prof = profile_holen(alle_profile())
    dauer = {"schiessen_oder_cache_s": uhr() - t0}
    zeilen = [profil_info(p) for p in prof.values()]
    m1 = [p for p in zeilen if p["m"] == 1]
    q1 = [p["Q"] for p in m1 if p["gueltig"]]
    kenn = {"m1_gueltig": sum(p["gueltig"] for p in m1), "m1_zeilen": len(m1),
            "m1_Q_monoton_fallend": all(a > b for a, b in zip(q1[:-1], q1[1:])),
            "m0_gueltig": sum(p["gueltig"] for p in zeilen if p["m"] == 0),
            "virialrest_max": max(abs(p["virialrest"]) for p in zeilen if p["gueltig"])}
    for q in (160.0, 208.0):
        ip1, ip0 = profil_bei_q(q, 1), profil_bei_q(q, 0)
        kenn[f"omega2_bei_Q{q:.0f}"] = {"m1": ip1["omega2"] if ip1 else None, "m0": ip0["omega2"] if ip0 else None}
    text = [kopf("RING profile: m = 1 und m = 0 (nur Schiessen)", start, rauch)]
    text += laufzeit_text(dauer, False)
    text.append("omega2 m | Q | E | E/Q | S_max | R_kern_halb | R_max | R_halb | Virialrest | Klammer | gueltig")
    for p in zeilen:
        text.append(f"  {p['omega2']:.3f} {p['m']} | {p['Q']:.3f} | {p['E']:.3f} | {p['E'] / p['Q']:.5f} | "
                    f"{p['S_max']:.4f} | {p['R_kern_halb']:.3f} | {p['R_max']:.3f} | {p['R_halb']:.3f} | "
                    f"{p['virialrest']:.1e} | {p['klammer']:.1e} | {'ja' if p['gueltig'] else 'NEIN'}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    text.append("Schranke: Q(omega) fuer m = 1 streng fallend (Voraussetzung der Interpolation bei gleicher Ladung): "
                + ("ja" if kenn["m1_Q_monoton_fallend"] else "NEIN"))
    schreiben(out, "profile", {"karte": "RING profile", "start": start, "ende": jetzt(), "dauer_s": dauer,
                               "zeilen": zeilen, "kennzahlen": kenn}, "\n".join(text))


# ---------------------------------------------------------------- (a) wirbel: mitdrehender Ring -> drehender Ball?

def ring_geschw(pr, R):
    """Aus r5_2d_b.py: Tangentialgeschwindigkeit fuer J_Bahn = Q je Ball: gamma E v R = Q -> v = x/sqrt(1 + x^2), x = Q/(E R)."""
    x = pr["Q"] / (pr["E"] * R)
    return x / math.sqrt(1.0 + x * x)


def spaet(t, y, t_von):
    m = t >= t_von - 1e-9
    v = y[m]
    return {"mittel": v.mean().item(), "std": v.std().item() if v.numel() > 1 else 0.0,
            "min": v.min().item(), "max": v.max().item()}


def einzelklumpen_auswerten(t, daten, verlauf_b, extra_b, radial_b, b, T, t_ref_null=False):
    """Gemeinsame Auswertung eines Einzelklumpens im Fenster (wirbel, teilung): Zeitreihen und spaete Mittel ab T/2,
    Windungen auf den Kreisen, Wirbelzaehlung, Profilvergleich mit m = 1 und m = 0 gleicher Ladung."""
    fen = daten["fen"][:, b, :]
    q, en, jj, nn = fen[:, 2], fen[:, 3], fen[:, 4], fen[:, 5]
    om_eff = q / (2.0 * nn.clamp(min=1e-300))
    om_loc = fen[:, 9] / (2.0 * fen[:, 10].clamp(min=1e-300))
    t_s = 0.5 * T
    z = {"Q_w": spaet(t, q, t_s), "J_zu_Q": spaet(t, jj / q, t_s), "omega_eff": spaet(t, om_eff, t_s),
         "omega_loc": spaet(t, om_loc, t_s), "E_zu_Q": spaet(t, en / q, t_s), "S_max_w": spaet(t, fen[:, 8], t_s),
         "v_w": spaet(t, torch.sqrt(fen[:, 6] ** 2 + fen[:, 7] ** 2) / en, t_s),
         "ort_ende": [fen[-1, 0].item(), fen[-1, 1].item()]}
    if fen.shape[1] > 11:
        z["A_l_spaet"] = [spaet(t, fen[:, 11 + l], t_s)["mittel"] for l in range(fen.shape[1] - 11)]
    # Zeitpunkte fuer den Bericht
    z["reihe"] = []
    for tt in (0.0, 50.0, 100.0, 250.0, 500.0, 1000.0, 1500.0, 2000.0, 3000.0):
        if tt <= T + 1e-9:
            i = int(round(tt / T_MEAS))
            z["reihe"].append({"t": tt, "Q_w": q[i].item(), "J_zu_Q": (jj[i] / q[i]).item(), "omega_eff": om_eff[i].item(),
                               "E_zu_Q": (en[i] / q[i]).item(), "S_max_w": fen[i, 8].item()})
    # Windungen auf den Kreisen
    ts = [e["t"] for e in extra_b]
    z["windung_ende"] = [[rc, w, round(sm, 4)] for rc, (w, sm) in zip(KREISE, extra_b[-1]["kreise"])]
    z["wirbel_ende"] = {"plus_r4": extra_b[-1]["wirbel"][0], "minus_r4": extra_b[-1]["wirbel"][1],
                        "plus_r8": extra_b[-1]["wirbel"][2], "minus_r8": extra_b[-1]["wirbel"][3],
                        "naechster": extra_b[-1]["wirbel"][4]}
    spaete = [e for e in extra_b if e["t"] >= t_s - 1e-9]
    ok_w1, sicher = 0, 0
    for e in spaete:
        ws = [w for rc, (w, sm) in zip(KREISE, e["kreise"]) if 2.0 <= rc <= 8.0 and sm >= S_MIN_SICHER]
        if ws:
            sicher += 1
            ok_w1 += all(w == 1 for w in ws)
    z["anteil_W1_spaet"] = ok_w1 / sicher if sicher else None
    z["analysen_spaet_sicher"] = sicher
    z["wirbel_spaet_netto_r8"] = (sum(e["wirbel"][2] - e["wirbel"][3] for e in spaete) / len(spaete)) if spaete else None
    z["naechster_wirbel_spaet"] = (sum(min(e["wirbel"][4], 99.0) for e in spaete) / len(spaete)) if spaete else None
    # Klumpenzahl, Verschmelzen, Teilung danach
    ns = [len(kl) for _, _, kl in verlauf_b]
    tv = [tt for tt, _, _ in verlauf_b]
    z["n_start"], z["n_ende"], z["n_max"] = ns[0], ns[-1], max(ns)
    t_eins = erste_dauerhaft(tv, [n == 1 for n in ns])
    z["t_ein_klumpen"] = t_eins
    t_teil = None
    if t_eins is not None:
        i0 = tv.index(t_eins)
        t_teil = erste_dauerhaft(tv[i0:], [n >= 2 for n in ns[i0:]])
    z["t_teilung_danach"] = t_teil
    z["klumpen_ende"] = [[round(k["Q"], 3), round(k["X"], 2), round(k["Y"], 2), k.get("windung"),
                          round(k.get("S_min_kreis", 0.0), 4), round(k["Jspin_Q"], 4)] for k in verlauf_b[-1][2]]
    z["frad_ende"] = 1.0 - verlauf_b[-1][1] / daten["glob"][0, b, 0].item()
    # schwellenfreie Teilungsprobe: Fensterladung faellt unter die Haelfte des Werts bei t_ref (Stuecke verlassen das
    # Fenster); t_ref = min(100, T/2) nach dem Verschmelzen bzw. 0 fuer den ruhenden Ball (t_ref_null)
    t_ref = 0.0 if t_ref_null else min(100.0, 0.5 * T)
    i_ref = int(round(t_ref / T_MEAS))
    halb = ((q < 0.5 * q[i_ref]) & (t >= t_ref - 1e-9)).nonzero()
    z["t_fenster_halb"] = t[halb[0, 0]].item() if halb.numel() else None
    if fen.shape[1] > 11:
        z["A_l_max_ab_tref"] = [fen[i_ref:, 11 + l].max().item() for l in range(fen.shape[1] - 11)]
    # Profilvergleich mit m = 1 und m = 0 gleicher Ladung (spaetes Mittel des Radialprofils)
    rc = (torch.arange(RAD_NBIN, dtype=F64, device=DEV) + 0.5) * RAD_DR
    m_sp = torch.tensor([e["t"] >= t_s - 1e-9 for e in extra_b], device=DEV)
    s_mess = radial_b[m_sp].mean(0) if bool(m_sp.any()) else radial_b[-1]
    q_sp = z["Q_w"]["mittel"]
    rcl = rc.tolist()
    z["form_mess"] = form(rcl, s_mess.tolist())
    for m in (1, 0):
        ip = profil_bei_q(q_sp, m)
        if ip is None:
            z[f"vergleich_m{m}"] = {"eingeschachtelt": False}
            continue
        s_p = profil_s(ip, rc)
        z[f"vergleich_m{m}"] = {"eingeschachtelt": True, "omega2": ip["omega2"], "omega": math.sqrt(ip["omega2"]),
                                "E_zu_Q": ip["E_Q"], "abweichung_L2": profil_abweichung(s_mess, s_p, rc),
                                "form": form(rcl, s_p.tolist()), "zwischen": ip["zwischen"]}
    # Profilabweichung ueber die Zeit (gegen m = 1 bei der jeweiligen Fensterladung)
    z["abweichung_m1_reihe"] = []
    for k, e in enumerate(extra_b):
        if e["t"] in (5.0, 50.0, 100.0, 250.0, 500.0, 1000.0, 2000.0, 3000.0) or k == len(extra_b) - 1:
            i = int(round(e["t"] / T_MEAS))
            ip = profil_bei_q(q[i].item(), 1)
            z["abweichung_m1_reihe"].append([e["t"], profil_abweichung(radial_b[k], profil_s(ip, rc), rc) if ip else None])
    z["radial_spaet"] = [round(x, 6) for x in s_mess.tolist()]
    return z


def test_wirbel(out, rauch, stufen, args):
    start = jetzt()
    print(f"RING wirbel Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t0 = uhr()
    pr = profile_holen([(W2_STD, 0)])[(W2_STD, 0)]
    profile_holen([(w2, 1) for w2 in M1_GITTER] + [(w2, 0) for w2 in M0_GITTER])
    dauer["profile_s"] = uhr() - t0
    d = 2.0 * pr["R_halb"] + SPALT
    info = {}

    def bauen(g, lauf_):
        name, N, eps = lauf_
        dreh = 0 if name.endswith("ruhend") else 1
        R = d / (2.0 * math.sin(math.pi / N))
        v = ring_geschw(pr, R) if dreh else 0.0
        baelle = []
        for j in range(N):
            th = 2.0 * math.pi * j / N
            b = {"pr": pr, "x": R * math.cos(th), "y": R * math.sin(th), "phase": 2.0 * math.pi * j / N}
            if dreh:
                b["v"], b["winkel"] = v, th + 0.5 * math.pi
            baelle.append(b)
        info[name] = {"N": N, "k": 1, "dreh": dreh, "R": R, "v": v, "stoer_eps": eps}
        return baelle

    def nachbau(g, lauf_, p_, v_):
        name, N, eps = lauf_
        if eps == 0.0:
            return p_, v_
        fak = stoerfaktor(g, 0.0, 0.0, info[name]["R"], eps)
        return p_ * fak, v_ * fak

    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = waehlen(W_LAEUFE, stufe, W_FEIN)
        if not laeufe:
            continue
        T = W_T[stufe] * (RAUCH_FAKTOR if rauch else 1.0)
        g, t, daten, verlauf, extra, orte, _ = stufe_rechnen(
            "wirbel", stufe, dx, dt, W_L, T, laeufe, bauen, Q_KLUMPEN * pr["Q"], out, dauer,
            fenster=[W_RWIN] * len(laeufe), l_max=STOER_LMAX, nachbau=nachbau)
        ergebnis = []
        for b, lauf_ in enumerate(laeufe):
            z = {"lauf": lauf_[0], "stufe": stufe, **info[lauf_[0]], "T": T,
                 **einzelklumpen_auswerten(t, daten, verlauf[b], extra[b], daten["radial"][:, b, :], b, T),
                 "bilanz": bilanz(t, daten["glob"], b),
                 "J_zu_Q_box_start": (daten["glob"][0, b, 2] / daten["glob"][0, b, 0]).item()}
            z["schranken"] = {
                "bilanz_Q": z["bilanz"]["Q"]["ok"], "bilanz_J": z["bilanz"]["J"]["ok"], "bilanz_E": z["bilanz"]["E"]["ok"],
                "startzerlegung": z["n_start"] == info[lauf_[0]]["N"],
                "omega_eff_unter_1": 0.0 < z["omega_eff"]["mittel"] < 1.0,
                "Q_w_hoechstens_Q_box0": z["Q_w"]["max"] <= 1.01 * daten["glob"][0, b, 0].item(),
                "profil_eingeschachtelt": z.get("vergleich_m1", {}).get("eingeschachtelt", False)}
            ergebnis.append(z)
        kenn = {}
        for z in ergebnis:
            v1, v0 = z.get("vergleich_m1", {}), z.get("vergleich_m0", {})
            kenn[z["lauf"]] = {
                "windung_1_spaet_anteil": z["anteil_W1_spaet"], "J_zu_Q_spaet": z["J_zu_Q"]["mittel"],
                "omega_eff_zu_omega_m1": (z["omega_eff"]["mittel"] / v1["omega"]) if v1.get("eingeschachtelt") else None,
                "omega_eff_zu_omega_m0": (z["omega_eff"]["mittel"] / v0["omega"]) if v0.get("eingeschachtelt") else None,
                "profil_L2_m1": v1.get("abweichung_L2"), "profil_L2_m0": v0.get("abweichung_L2"),
                "E_zu_Q_ueber_m1": (z["E_zu_Q"]["mittel"] / v1["E_zu_Q"] - 1.0) if v1.get("eingeschachtelt") else None,
                "ein_klumpen_ab": z["t_ein_klumpen"], "teilung_danach": z["t_teilung_danach"],
                "fenster_halb_ab": z["t_fenster_halb"], "A2_max_ab_tref": (z.get("A_l_max_ab_tref") or [None, None])[1],
                "schranken_ok": all(z["schranken"].values())}
        ausgabe = {"karte": "RING wirbel (a)", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
                   "geraet": geraet_name(), "stufe": stufe,
                   "parameter": {"omega2_ball": W2_STD, "spalt": SPALT, "d": d, "L": W_L, "T": T, "dx": dx, "dt": dt,
                                 "r_win": W_RWIN, "kreise": KREISE, "t_meas": T_MEAS},
                   "profil_ball": profil_info(pr), "ergebnis": ergebnis, "kennzahlen": kenn}
        text = [kopf(f"RING wirbel (a): mitdrehende Ringe, Stufe {stufe}", start, rauch)]
        text += laufzeit_text(dauer, rauch)
        text.append(f"Ringball omega2 {W2_STD}: Q {pr['Q']:.3f}, E {pr['E']:.3f}, R_halb {pr['R_halb']:.3f}; d {d:.3f}; "
                    f"T {T:g}, dx {dx}, dt {dt}")
        for z in ergebnis:
            v1, v0 = z.get("vergleich_m1", {}), z.get("vergleich_m0", {})
            text.append(f"  {z['lauf']}: R {z['R']:.2f}, v {z['v']:.4f}, J/Q Box Start {z['J_zu_Q_box_start']:+.4f}; "
                        f"ein Klumpen ab {z['t_ein_klumpen']}, Teilung danach {z['t_teilung_danach']}, n Ende {z['n_ende']}, "
                        f"Fensterladung unter 1/2 ab {z['t_fenster_halb']}, A_l max ab t_ref "
                        f"{[round(x, 3) for x in z.get('A_l_max_ab_tref', [])]}")
            text.append(f"    Windung Ende (r, W, S_min): {z['windung_ende']}; Anteil W = 1 (r 2..8, spaet) "
                        f"{fz(z['anteil_W1_spaet'])}; Wirbel r<4 +{z['wirbel_ende']['plus_r4']}/-{z['wirbel_ende']['minus_r4']}, "
                        f"r<8 +{z['wirbel_ende']['plus_r8']}/-{z['wirbel_ende']['minus_r8']}, naechster {z['wirbel_ende']['naechster']:.2f}")
            text.append(f"    spaet (t >= T/2): Q_w {z['Q_w']['mittel']:.3f} (std {z['Q_w']['std']:.3f}), J/Q "
                        f"{z['J_zu_Q']['mittel']:.4f} (std {z['J_zu_Q']['std']:.4f}), omega_eff {z['omega_eff']['mittel']:.5f}, "
                        f"omega_loc {z['omega_loc']['mittel']:.5f}, E/Q {z['E_zu_Q']['mittel']:.5f}, S_max {z['S_max_w']['mittel']:.4f}, "
                        f"v {z['v_w']['mittel']:.2e}")
            if v1.get("eingeschachtelt"):
                text.append(f"    m = 1 gleicher Ladung: omega2 {v1['omega2']:.4f} (omega {v1['omega']:.5f}), E/Q "
                            f"{v1['E_zu_Q']:.5f}, Profil-L2 {v1['abweichung_L2']:.4f}; Form Messung {json.dumps(z['form_mess'])} "
                            f"gegen Profil {json.dumps(v1['form'])}")
            else:
                text.append("    m = 1 gleicher Ladung: ausserhalb des Profilgitters (keine Extrapolation)")
            if v0.get("eingeschachtelt"):
                text.append(f"    Gegenprobe m = 0 gleicher Ladung: omega {v0['omega']:.5f}, Profil-L2 {v0['abweichung_L2']:.4f}")
            text.append(f"    Reihe (t, Q_w, J/Q, omega_eff, E/Q, S_max): " + "; ".join(
                f"{r['t']:g} {r['Q_w']:.2f} {r['J_zu_Q']:.4f} {r['omega_eff']:.4f} {r['E_zu_Q']:.4f} {r['S_max_w']:.3f}"
                for r in z["reihe"]))
            text.append(f"    Profil-L2 gegen m = 1 ueber die Zeit: " + "; ".join(
                f"{a:g} {fz(b_, '{:.4f}')}" for a, b_ in z["abweichung_m1_reihe"]))
            text.append(f"    Bilanz: {bilanz_text(z['bilanz'])}")
            text.append(f"    Schranken: {json.dumps(z['schranken'])}")
        text.append("Kennzahlen: " + json.dumps(kenn))
        schreiben(out, f"wirbel_{stufe}", ausgabe, "\n".join(text))

    def vergleich(zg, zf):
        g_ = {z["lauf"]: z for z in zg["ergebnis"]}
        zeilen, ok_alle = [], True
        for z in zf["ergebnis"]:
            a = g_.get(z["lauf"])
            if not a:
                continue
            # Bruch = Teilung nach dem Verschmelzen oder Fensterladung unter 1/2 (frueheres von beiden)
            def bruch(x):
                ts_ = [v for v in (x["t_teilung_danach"], x["t_fenster_halb"]) if v is not None and v <= z["T"]]
                return min(ts_) if ts_ else None
            bg, bf = bruch(a), bruch(z)
            ok = (a["t_ein_klumpen"] == z["t_ein_klumpen"] or (a["t_ein_klumpen"] is not None and z["t_ein_klumpen"]
                                                               is not None and abs(a["t_ein_klumpen"] - z["t_ein_klumpen"]) <= 10.0))
            # Bruchzeit nur mit Saat pruefen (ohne Saat waechst die Stoerung aus Rundung, die Zeit ist nicht vergleichbar)
            if z.get("stoer_eps", 0.0) > 0.0:
                ok = ok and (bg is None) == (bf is None) and (bg is None or abs(bf - bg) <= max(0.1 * bg, 10.0))
            t_bis = min([x for x in (bg, bf) if x is not None] + [z["T"] + 50.0]) - 50.0
            rg = {r["t"]: r for r in a["reihe"]}
            dj = [abs(r["J_zu_Q"] - rg[r["t"]]["J_zu_Q"]) for r in z["reihe"] if r["t"] in rg and 100.0 <= r["t"] <= t_bis]
            do = [abs(r["omega_eff"] / rg[r["t"]]["omega_eff"] - 1.0) for r in z["reihe"]
                  if r["t"] in rg and 100.0 <= r["t"] <= t_bis]
            ok = ok and (not dj or max(dj) <= 0.01) and (not do or max(do) <= 0.005)
            ok_alle = ok_alle and ok
            zeilen.append(f"{z['lauf']}: ein Klumpen ab {a['t_ein_klumpen']}/{z['t_ein_klumpen']}, Bruch "
                          f"{bg}/{bf} (Saat {z.get('stoer_eps')}), max|dJ/Q| (t 100 .. Bruch - 50) "
                          f"{fz(max(dj) if dj else None, '{:.2e}')}, max|domega/omega| {fz(max(do) if do else None, '{:.2e}')}"
                          f" -> {'bestanden' if ok else 'NICHT bestanden'}")
        return {"zeilen": zeilen, "bestanden": ok_alle if zeilen else None,
                "kriterium": "ein Klumpen ab gleicher Zeit (+-10); mit Saat Bruch ja/nein gleich und Bruchzeit innerhalb "
                             "max(10 %, 10); |dJ/Q| <= 0,01 und |domega/omega| <= 0,005 an den Reihenzeiten von 100 bis "
                             "50 vor dem frueheren Bruch (hoechstens T_fein)"}

    l3_datei(out, "wirbel", vergleich)


# ---------------------------------------------------------------- (a) teilung: stationaerer m = 1-Ball mit Stoerung

def test_teilung(out, rauch, stufen, args):
    start = jetzt()
    print(f"RING teilung Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t0 = uhr()
    prof = profile_holen([(w2, 1) for w2 in T_W2] + [(w2, 1) for w2 in M1_GITTER] + [(w2, 0) for w2 in M0_GITTER])
    dauer["profile_s"] = uhr() - t0
    laeufe_alle = tuple((f"m1_{int(round(1000 * w2)):04d}", w2) for w2 in T_W2)

    def bauen(g, lauf_):
        return [{"pr": prof[(round(lauf_[1], 6), 1)], "m": 1, "x": 0.0, "y": 0.0}]

    def nachbau(g, lauf_, p_, v_):
        pr = prof[(round(lauf_[1], 6), 1)]
        fak = stoerfaktor(g, 0.0, 0.0, max(pr["R_max"], 0.7 * pr["R_halb"]), STOER_EPS)
        return p_ * fak, v_ * fak

    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [l for l in waehlen(laeufe_alle, stufe, T_FEIN, name=lambda l: l[1])
                  if prof[(round(l[1], 6), 1)]["gueltig"]]
        if not laeufe:
            continue
        T = T_T[stufe] * (RAUCH_FAKTOR if rauch else 1.0)
        r_win = [prof[(round(w2, 6), 1)]["R_halb"] + 12.0 for _, w2 in laeufe]
        q_min = [Q_MIN_REL * prof[(round(w2, 6), 1)]["Q"] for _, w2 in laeufe]
        g, t, daten, verlauf, extra, orte, _ = stufe_rechnen(
            "teilung", stufe, dx, dt, T_L, T, laeufe, bauen, q_min, out, dauer, fenster=r_win, l_max=STOER_LMAX,
            nachbau=nachbau)
        ergebnis = []
        alle = int(round(ANALYSE_DT / T_MEAS))
        for b, (name, w2) in enumerate(laeufe):
            pr = prof[(round(w2, 6), 1)]
            tv = [tt for tt, _, _ in verlauf[b]]
            ns = [len(kl) for _, _, kl in verlauf[b]]
            t_teil = erste_dauerhaft(tv, [n >= 2 for n in ns])
            z = {"lauf": name, "omega2": w2, "stufe": stufe, "T": T, "Q_profil": pr["Q"], "E_zu_Q_profil": pr["E"] / pr["Q"],
                 "n_max": max(ns), "n_ende": ns[-1], "teilung": t_teil is not None, "t_teilung": t_teil,
                 "bilanz": bilanz(t, daten["glob"], b)}
            if t_teil is not None:
                i_z = min(range(len(tv)), key=lambda i: abs(tv[i] - (t_teil + T_NACH)))
                z["t_toechter"] = tv[i_z]
                z["toechter"] = [[round(k["Q"], 3), k.get("windung"), round(k["Jspin_Q"], 4), round(k["vx"], 4),
                                  round(k["vy"], 4)] for k in verlauf[b][i_z][2]]
            fen = daten["fen"][:, b, :]
            i_ref = int(round(t_teil / T_MEAS)) if t_teil is not None else fen.shape[0] - 1
            am = fen[:, 11:11 + STOER_LMAX]
            l_dom = int(torch.argmax(am[i_ref])) + 1
            a = am[:, l_dom - 1]
            maske = (a >= 3.0 * a[0]) & (a > 1e-12) & (a <= 0.2) & (torch.arange(a.shape[0], device=DEV) <= i_ref)
            z["l_dominant"], z["A_start_ende"], z["gamma"] = l_dom, [a[0].item(), a[i_ref].item()], None
            if int(maske.sum()) >= 8:
                fit = polyfit(t[maske], torch.log(a[maske]), 1)
                if fit is not None:
                    z["gamma"] = (fit[0][1] / fit[3]).item()
                    z["gamma_rest_rms"] = fit[2].item()
            z["A_max_ueber_T"] = [am[:, l].max().item() for l in range(STOER_LMAX)]
            ek = einzelklumpen_auswerten(t, daten, verlauf[b], extra[b], daten["radial"][:, b, :], b, T, t_ref_null=True)
            z["t_fenster_halb"] = ek["t_fenster_halb"]
            if t_teil is None:
                z["spaet"] = {k: v for k, v in ek.items()
                              if k in ("J_zu_Q", "omega_eff", "E_zu_Q", "anteil_W1_spaet", "windung_ende", "Q_w",
                                       "vergleich_m1")}
            z["schranken"] = {"bilanz_Q": z["bilanz"]["Q"]["ok"], "bilanz_J": z["bilanz"]["J"]["ok"],
                              "bilanz_E": z["bilanz"]["E"]["ok"], "startzerlegung": ns[0] == 1,
                              "profil_selbst_L2_unter_0p05": (z["spaet"]["vergleich_m1"].get("abweichung_L2", 1.0) < 0.05
                                                             if z.get("spaet") else None)}
            ergebnis.append(z)
        stabil = [z["omega2"] for z in ergebnis if not z["teilung"]]
        geteilt = [z["omega2"] for z in ergebnis if z["teilung"]]
        kenn = {"stabil_bis_T": stabil, "geteilt": geteilt,
                "schwelle_eingeschachtelt": (bool(stabil) and bool(geteilt) and max(stabil) < min(geteilt)),
                "schwelle_zwischen": [max(stabil), min(geteilt)] if stabil and geteilt and max(stabil) < min(geteilt) else None,
                "Q_zwischen": None}
        if kenn["schwelle_zwischen"]:
            kenn["Q_zwischen"] = [prof[(round(w, 6), 1)]["Q"] for w in kenn["schwelle_zwischen"]]
        ausgabe = {"karte": "RING teilung (a, Anschluss Teilung)", "start": start, "ende": jetzt(), "rauch": rauch,
                   "dauer_s": dauer, "geraet": geraet_name(), "stufe": stufe,
                   "parameter": {"T": T, "L": T_L, "dx": dx, "dt": dt, "eps": STOER_EPS, "l_max": STOER_LMAX,
                                 "phi": STOER_PHI, "t_meas": T_MEAS},
                   "ergebnis": ergebnis, "kennzahlen": kenn}
        text = [kopf(f"RING teilung (a): m = 1-Ball mit 1-%-Stoerung, Stufe {stufe}", start, rauch)]
        text += laufzeit_text(dauer, rauch)
        text.append("Lauf | omega2 | Q | Teilung t | n_max | Toechter (Q, W, Jspin/Q, vx, vy) | l_dom | gamma | "
                    "A_max l=1..6 | spaet J/Q, omega_eff, Anteil W1")
        for z in ergebnis:
            toe = "; ".join(str(x) for x in z.get("toechter", [])) or "-"
            sp = z.get("spaet")
            sp_t = (f"{sp['J_zu_Q']['mittel']:.4f}, {sp['omega_eff']['mittel']:.5f}, {fz(sp['anteil_W1_spaet'])}"
                    if sp else "-")
            text.append(f"  {z['lauf']} | {z['omega2']:.3f} | {z['Q_profil']:.2f} | {z['t_teilung']} (Fenster {z['t_fenster_halb']}) | {z['n_max']} | {toe} | "
                        f"{z['l_dominant']} | {fz(z['gamma'], '{:.4f}')} | "
                        f"{' '.join(f'{x:.1e}' for x in z['A_max_ueber_T'])} | {sp_t}")
            text.append(f"    Bilanz: {bilanz_text(z['bilanz'])}; Schranken {json.dumps(z['schranken'])}")
        text.append("Kennzahlen: " + json.dumps(kenn))
        schreiben(out, f"teilung_{stufe}", ausgabe, "\n".join(text))

    def vergleich(zg, zf):
        g_ = {z["lauf"]: z for z in zg["ergebnis"]}
        zeilen, ok_alle = [], True
        for z in zf["ergebnis"]:
            a = g_.get(z["lauf"])
            if not a:
                continue
            tg = a["t_teilung"] if a["t_teilung"] is not None and a["t_teilung"] <= z["T"] else None
            ok = (tg is None) == (z["t_teilung"] is None)
            if ok and tg is not None:
                ok = abs(z["t_teilung"] - tg) <= max(0.1 * tg, 10.0)
            dg = abs(z["gamma"] / a["gamma"] - 1.0) if z.get("gamma") and a.get("gamma") else None
            ok = ok and (dg is None or dg <= 0.2)
            ok_alle = ok_alle and ok
            zeilen.append(f"{z['lauf']}: Teilung grob {a['t_teilung']} / fein {z['t_teilung']} (T_fein {z['T']:g}), "
                          f"gamma {fz(a.get('gamma'), '{:.4f}')} / {fz(z.get('gamma'), '{:.4f}')} -> "
                          f"{'bestanden' if ok else 'NICHT bestanden'}")
        return {"zeilen": zeilen, "bestanden": ok_alle if zeilen else None,
                "kriterium": "Teilung ja/nein bis T_fein gleich, t_teilung innerhalb max(10 %, 10), gamma innerhalb 20 %"}

    l3_datei(out, "teilung", vergleich)


# ---------------------------------------------------------------- (b) vierer: Vierer-Ring mit Windung 2 pi/4

def vierer_auswerten(t, daten, verlauf_b, b, T, L_rand):
    """Neu: Ringradius (Mittel der Abstaende der vier Verfolger vom gemeinsamen Mittelpunkt), mittlerer Paarabstand (wie
    r5_2d_a.py), Ladungsspreizung, Drehwinkel, Bruchzeit, Wachstumsrate der Spreizung, Schwingung und Drift des Radius."""
    bahn = daten["bahn"][:, b, :4, :]
    xs, ys, qs = bahn[:, :, 0], bahn[:, :, 1], bahn[:, :, 2]
    xm, ym = xs.mean(1, keepdim=True), ys.mean(1, keepdim=True)
    r = torch.sqrt((xs - xm) ** 2 + (ys - ym) ** 2).mean(1)
    paare = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    dpaar = torch.stack([torch.sqrt((xs[:, i] - xs[:, j]) ** 2 + (ys[:, i] - ys[:, j]) ** 2) for i, j in paare], 1).mean(1)
    spread = (qs.max(1).values - qs.min(1).values) / qs.mean(1).abs().clamp(min=1e-300)
    winkel = entfalten(torch.atan2(ys[:, 0] - ym[:, 0], xs[:, 0] - xm[:, 0]))
    tv = [tt for tt, _, _ in verlauf_b]
    ns = [len(kl) for _, _, kl in verlauf_b]
    t_rand = next((tt for tt, _, kl in verlauf_b if any(abs(k["X"]) > L_rand or abs(k["Y"]) > L_rand for k in kl)), None)
    t_verschm = erste_dauerhaft(tv, [n < 4 for n in ns])
    idx_b = (spread >= V_SPREAD_BRUCH).nonzero()
    t_bruch = t[idx_b[0, 0]].item() if idx_b.numel() else None
    idx_t = (spread >= V_SPREAD_TAUSCH).nonzero()
    t_tausch = t[idx_t[0, 0]].item() if idx_t.numel() else None
    r0 = r[0].item()
    idx_w = (r >= 1.3 * r0).nonzero()
    t_weit = t[idx_w[0, 0]].item() if idx_w.numel() else None
    ende = min(x for x in (t_verschm, t_bruch, t_rand, t_weit, T) if x is not None)
    m = t <= ende + 1e-9
    z = {"r_start": r0, "d_paar_start": dpaar[0].item(), "t_verschmolzen": t_verschm, "t_bruch_spread_0p1": t_bruch,
         "t_tausch_spread_0p3": t_tausch, "t_rand": t_rand, "t_weit_1p3": t_weit, "t_gueltig_bis": ende,
         "n_start": ns[0], "n_ende": ns[-1], "spread_start": spread[0].item(), "spread_max": spread.max().item()}
    rv, tvv = r[m], t[m]
    z["r_mittel"], z["r_min"], z["r_max"] = rv.mean().item(), rv.min().item(), rv.max().item()
    z["d_paar_max_gueltig"] = dpaar[m].max().item()
    n_ende = rv.shape[0]
    zweite = rv[n_ende // 2:]
    z["r_mittel_zweite_haelfte"] = zweite.mean().item() if zweite.numel() else None
    fit = polyfit(tvv, rv, 1)
    if fit is not None:
        z["drift_pro_zeit"] = (fit[0][1] / fit[3]).item()
        z["drift_fehler"] = (fit[1][1] / fit[3]).item()
        z["drift_mal_fenster_rel"] = (fit[0][1] / r0).item()
        detr = (rv - (fit[0][0] + fit[0][1] * (tvv - tvv[0]) / fit[3])).tolist()
        n_w = schwuenge(detr, 0.02 * r0)
        z["umkehrpunkte"] = n_w
        z["periode"] = (2.0 * (tvv[-1] - tvv[0]).item() / n_w) if n_w >= 2 else None
        h2 = detr[len(detr) // 2:]
        z["amplitude_zweite_haelfte"] = 0.5 * (max(h2) - min(h2)) if h2 else None
        h1 = detr[:len(detr) // 2]
        z["amplitude_erste_haelfte"] = 0.5 * (max(h1) - min(h1)) if h1 else None
    om = polyfit(tvv, winkel[m], 1)
    z["drehrate"] = (om[0][1] / om[3]).item() if om is not None else None
    # Wachstumsrate der Ladungsspreizung: Fenster von max(10 x Startspreizung, 1e-10) bis 3e-2, vor dem Bruch,
    # mindestens 8 Punkte und ein Faktor 20 in der Spreizung (sonst keine Rate; Anfangsschwingung der Saat ausgelassen)
    unten = max(10.0 * spread[0].item(), 1e-10)
    mg = (spread > unten) & (spread < 3e-2) & m
    z["gamma_spreizung"] = None
    if int(mg.sum()) >= 8 and (spread[mg].max() / spread[mg].min()).item() >= 20.0:
        fg = polyfit(t[mg], torch.log(spread[mg]), 1)
        if fg is not None:
            z["gamma_spreizung"] = (fg[0][1] / fg[3]).item()
            z["gamma_fenster"] = [t[mg][0].item(), t[mg][-1].item()]
            z["gamma_rest_rms"] = fg[2].item()
    # Klasse (vorab, PLAN.md 4.3)
    ereignisse = [(x, n) for x, n in ((t_verschm, "verschmolzen"), (t_tausch, "Ladungstausch"), (t_weit, "auseinander"))
                  if x is not None]
    if ereignisse:
        z["klasse"] = min(ereignisse)[1]
    elif t_rand is not None and t_rand < 0.8 * T:
        z["klasse"] = "offen (Rand)"
    elif z.get("drift_mal_fenster_rel") is not None and abs(z["drift_mal_fenster_rel"]) >= 0.1:
        z["klasse"] = "driftend"
    elif (t_bruch is None and all(n == 4 for n in ns) and 0.8 * r0 <= z["r_min"] and z["r_max"] <= 1.25 * r0
          and ende >= 0.8 * T):
        z["klasse"] = "gebunden"
    else:
        z["klasse"] = "offen"
    z["reihe"] = []
    for tt in (0.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 800.0, 1000.0, 1500.0, 2000.0):
        if tt <= T + 1e-9:
            i = int(round(tt / T_MEAS))
            z["reihe"].append([tt, round(r[i].item(), 4), round(dpaar[i].item(), 4), float(f"{spread[i].item():.3e}"),
                               round(winkel[i].item(), 4), round(daten["glob"][i, b, 2].item(), 4)])
    return z, r, winkel


def test_vierer(out, rauch, stufen, args):
    start = jetzt()
    print(f"RING vierer Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t0 = uhr()
    pr = profile_holen([(W2_STD, 0)])[(W2_STD, 0)]
    dauer["profile_s"] = uhr() - t0
    info = {}

    def bauen(g, lauf_):
        name, luecke, w, sym, saat = lauf_
        d = 2.0 * pr["R_halb"] + luecke
        orte = vieleck(4, d)
        baelle = [{"pr": pr, "x": x, "y": y, "phase": 0.5 * math.pi * w * k, "amp": (1.0 + saat) if k == 0 else 1.0}
                  for k, (x, y) in enumerate(orte)]
        info[name] = {"luecke": luecke, "seite": d, "windung": w, "sym": sym, "saat": saat,
                      "phasen": [0.5 * math.pi * w * k for k in range(4)], "orte": orte}
        return baelle

    def vorher(g, psi, vel):
        """Abweichung des Startfelds vom C4-Sektor seiner Windung, ||P psi - psi||/||psi|| (Symmetrie- und Aufbauprobe)."""
        aus = []
        for b, name in enumerate(namen_stufe):
            w = info[name]["windung"]
            p = psi[b:b + 1]
            aus.append((torch.linalg.vector_norm(projektion_c4(p, w) - p) / torch.linalg.vector_norm(p)).item())
        return {"sektor_abweichung_start": aus}

    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = waehlen(V_LAEUFE, stufe, V_FEIN)
        if not laeufe:
            continue
        namen_stufe = [l[0] for l in laeufe]
        T = V_T[stufe] * (RAUCH_FAKTOR if rauch else 1.0)
        d_std = 2.0 * pr["R_halb"] + SPALT
        r_w = min(pr["R_halb"] + R_WIN_PLUS, 0.4 * d_std)
        sym = [(b, l[2]) for b, l in enumerate(laeufe) if l[3]]
        g, t, daten, verlauf, extra, orte, vorab = stufe_rechnen(
            "vierer", stufe, dx, dt, V_L, T, laeufe, bauen, Q_KLUMPEN * pr["Q"], out, dauer, r_w=r_w, sym=sym,
            vorher=vorher)
        L_rand = g.L - SPONGE - RAND_ABSTAND
        ergebnis, reihen = [], {}
        for b, lauf_ in enumerate(laeufe):
            name = lauf_[0]
            z, r, winkel = vierer_auswerten(t, daten, verlauf[b], b, T, L_rand)
            reihen[name] = (r, winkel, daten["glob"][:, b, 2])
            z = {"lauf": name, "stufe": stufe, "T": T, **{k: v for k, v in info[name].items() if k != "orte"},
                 "sektor_abweichung_start": vorab["sektor_abweichung_start"][b], **z,
                 "Q_box_verlust": (1.0 - daten["glob"][-1, b, 0] / daten["glob"][0, b, 0]).item(),
                 "bilanz": bilanz(t, daten["glob"], b),
                 "windungen_klumpen_ende": [k.get("windung") if k.get("windung_sicher") else None for k in verlauf[b][-1][2]]}
            z["schranken"] = {"bilanz_Q": z["bilanz"]["Q"]["ok"], "bilanz_J": z["bilanz"]["J"]["ok"],
                              "bilanz_E": z["bilanz"]["E"]["ok"], "startzerlegung": z["n_start"] == 4,
                              # ohne Saat: nur der Randartefakt der periodischen Box (Feldschwanz am Rand, ~1e-8);
                              # mit Saat eps auf Ball 0: erwartet 0,433 eps (||(1 - P) eps psi_0|| / ||psi||)
                              "sektor_start": (z["sektor_abweichung_start"] <= 1e-7) if z["saat"] == 0.0 else
                              (abs(z["sektor_abweichung_start"] / (0.433 * z["saat"]) - 1.0) <= 0.05)}
            ergebnis.append(z)
        kenn = {"klassen": {z["lauf"]: z["klasse"] for z in ergebnis}}
        # Spiegelprobe: n4_gegen ist das Spiegelbild von n4_windung (mal globaler Phase)
        if "n4_windung" in reihen and "n4_gegen" in reihen:
            rw, ww, jw = reihen["n4_windung"]
            rg, wg, jg = reihen["n4_gegen"]
            m = t <= 300.0 * (RAUCH_FAKTOR if rauch else 1.0) + 1e-9
            kenn["spiegel"] = {"max_dr_rel_bis_300": ((rw[m] - rg[m]).abs().max() / rw[0]).item(),
                               "max_J_summe_rel_bis_300": ((jw[m] + jg[m]).abs().max() / jw[0].abs().clamp(min=1e-300)).item(),
                               "drehrate_windung": next(z["drehrate"] for z in ergebnis if z["lauf"] == "n4_windung"),
                               "drehrate_gegen": next(z["drehrate"] for z in ergebnis if z["lauf"] == "n4_gegen")}
        # ln-eps-Probe: Bruchzeit gegen Saat
        tb = {z["lauf"]: z["t_bruch_spread_0p1"] for z in ergebnis}
        gam = next((z["gamma_spreizung"] for z in ergebnis if z["lauf"] == "n4_windung_s1e-6"), None)
        if tb.get("n4_windung_s1e-3") is not None and tb.get("n4_windung_s1e-6") is not None and gam:
            dtb = tb["n4_windung_s1e-6"] - tb["n4_windung_s1e-3"]
            kenn["saat_probe"] = {"dt_bruch_1e-6_minus_1e-3": dtb, "gamma_s1e-6": gam,
                                  "verhaeltnis_dt_gamma_zu_ln1000": dtb * gam / math.log(1000.0)}
        ausgabe = {"karte": "RING vierer (b)", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
                   "geraet": geraet_name(), "stufe": stufe,
                   "parameter": {"omega2": W2_STD, "L": V_L, "T": T, "dx": dx, "dt": dt, "r_verfolger": r_w,
                                 "spread_bruch": V_SPREAD_BRUCH, "spread_tausch": V_SPREAD_TAUSCH, "t_meas": T_MEAS},
                   "profil": profil_info(pr), "ergebnis": ergebnis, "kennzahlen": kenn}
        text = [kopf(f"RING vierer (b): Vierer-Ring mit Windung 2 pi/4, Stufe {stufe}", start, rauch)]
        text += laufzeit_text(dauer, rauch)
        text.append(f"Ball omega2 {W2_STD}: Q {pr['Q']:.3f}, R_halb {pr['R_halb']:.3f}; T {T:g}, dx {dx}, dt {dt}")
        text.append("Lauf | Klasse | gueltig bis | r Start/Mittel/min/max | d_Paar Start/max | Drift (x Fenster/r0) | "
                    "Periode | Amplitude 1./2. Haelfte | Drehrate | Spreizung Start/max | gamma | t_Bruch 0,1 | "
                    "t_verschm | Q-Verlust | Sektor Start")
        for z in ergebnis:
            text.append(f"  {z['lauf']} | {z['klasse']} | {z['t_gueltig_bis']:g} | {z['r_start']:.3f}/{z['r_mittel']:.3f}/"
                        f"{z['r_min']:.3f}/{z['r_max']:.3f} | {z['d_paar_start']:.3f}/{z['d_paar_max_gueltig']:.3f} | "
                        f"{fz(z.get('drift_pro_zeit'), '{:.2e}')} ({fz(z.get('drift_mal_fenster_rel'), '{:+.3f}')}) | "
                        f"{fz(z.get('periode'), '{:.1f}')} | {fz(z.get('amplitude_erste_haelfte'), '{:.3f}')}/"
                        f"{fz(z.get('amplitude_zweite_haelfte'), '{:.3f}')} | {fz(z.get('drehrate'), '{:+.2e}')} | "
                        f"{z['spread_start']:.1e}/{z['spread_max']:.2f} | {fz(z.get('gamma_spreizung'), '{:.4f}')} | "
                        f"{z['t_bruch_spread_0p1']} | {z['t_verschmolzen']} | {z['Q_box_verlust']:.1e} | "
                        f"{z['sektor_abweichung_start']:.1e}")
            text.append(f"    Reihe (t, r, d_Paar, Spreizung, Winkel, J_Box): {z['reihe']}")
            text.append(f"    Bilanz: {bilanz_text(z['bilanz'])}; Schranken {json.dumps(z['schranken'])}; "
                        f"Windungen Klumpen Ende {z['windungen_klumpen_ende']}")
        text.append("Kennzahlen: " + json.dumps(kenn))
        schreiben(out, f"vierer_{stufe}", ausgabe, "\n".join(text))

    def vergleich(zg, zf):
        g_ = {z["lauf"]: z for z in zg["ergebnis"]}
        zeilen, ok_alle = [], True
        for z in zf["ergebnis"]:
            a = g_.get(z["lauf"])
            if not a:
                continue
            rg = {r_[0]: r_ for r_ in a["reihe"]}
            dr = [abs(r_[1] / rg[r_[0]][1] - 1.0) for r_ in z["reihe"] if r_[0] in rg and r_[0] <= min(z["t_gueltig_bis"],
                                                                                                    a["t_gueltig_bis"])]
            ok = not dr or max(dr) <= 0.01
            tb_g, tb_f = a["t_bruch_spread_0p1"], z["t_bruch_spread_0p1"]
            if tb_g is not None and tb_g <= z["T"]:
                ok = ok and tb_f is not None and abs(tb_f - tb_g) <= max(0.1 * tb_g, 10.0)
            if a.get("gamma_spreizung") and z.get("gamma_spreizung") and z["saat"] > 0.0:
                ok = ok and abs(z["gamma_spreizung"] / a["gamma_spreizung"] - 1.0) <= 0.1
            ok_alle = ok_alle and ok
            zeilen.append(f"{z['lauf']}: max|dr/r| {fz(max(dr) if dr else None, '{:.2e}')}, t_Bruch {tb_g}/{tb_f}, gamma "
                          f"{fz(a.get('gamma_spreizung'), '{:.4f}')}/{fz(z.get('gamma_spreizung'), '{:.4f}')}, Klasse "
                          f"{a['klasse']}/{z['klasse']} -> {'bestanden' if ok else 'NICHT bestanden'}")
        return {"zeilen": zeilen, "bestanden": ok_alle if zeilen else None,
                "kriterium": "Radius an den Reihenzeiten innerhalb 1 %; t_Bruch innerhalb max(10 %, 10); gamma (nur "
                             "mit Saat) innerhalb 10 %"}

    l3_datei(out, "vierer", vergleich)


# ---------------------------------------------------------------- Hauptprogramm

KARTEN = {"profile": test_profile, "wirbel": test_wirbel, "teilung": test_teilung, "vierer": test_vierer}


def main():
    global DEV, N_KAND, STUFEN, RAUCH_FAKTOR
    ap = argparse.ArgumentParser(description="Runde 7, Karte RING (Wirbelball aus einem Ring, Vierer-Ring)")
    ap.add_argument("karte", choices=list(KARTEN) + ["alle"])
    ap.add_argument("--rauch", action="store_true", help="Laufzeiten x 0,05; nur Durchlauf und Hochrechnung")
    ap.add_argument("--mini", action="store_true", help="nur mit --rauch: Formprobe (256 Kandidaten, dx 0,6/0,4, x 0,02)")
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda",
                    help="cpu nur fuer die Formprobe mit --rauch --mini, nie fuer Messlaeufe")
    ap.add_argument("--stufe", choices=["grob", "fein", "beide"], default="beide")
    ap.add_argument("--laeufe", default=None, help="nur diese Laeufe (Namen mit Komma), z. B. zum Aufteilen")
    ap.add_argument("--out", default=None)
    ap.add_argument("--cache", default=None, help="Profilcache (Vorgabe: profil_cache.pt neben dem Skript)")
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
    hier = os.path.dirname(os.path.abspath(__file__))
    out = args.out or os.path.join(hier, "rauchtest" if args.rauch else "ausgabe")
    CACHE["pfad"] = args.cache or os.path.join(hier, "profil_cache.pt")
    AUSWAHL["laeufe"] = set(args.laeufe.split(",")) if args.laeufe else None
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
