#!/usr/bin/env python3
"""G1-03 (Ideen-Evolution, Generation 1, Test-Agent T-2): Kopie von RUNDE-05/r5-2d-a/r5_2d_a.py (sha256 4b7a00b2...),
nur Unterbefehl "teilung" wird benutzt. Aenderungen gegenueber dem Original (alle mit "G1-03" markiert):
    - Laufliste: m = 2 bei omega^2 = 0,55 / 0,57 / 0,59 / 0,61 / 0,63 / 0,65 / 0,70 (--teil haupt), Gegenprobe m = 0 bei
      0,59 (--teil gegen); fein nur 0,57 / 0,59 / 0,61 / 0,63. T = 1200 statt 600 (--t-end).
    - Kennzahlen V1 bis V3, Gegenprobe, Plausibilitaetsschranke und L3 nach KARTE.md; Ausgabe teilung_<teil>_<stufe>.
    - Getrennte Aufrufe grob und fein: der fein-Aufruf liest fuer L3 und V1 bis V3 teilung_haupt_grob_ergebnis.json.
Rechenweg (Schiessen, Gitter, Velocity-Verlet, Randschicht, Gebietsanalyse, gamma-Fit) unveraendert.

Urspruenglicher Kopf:
Runde 5 (v3), Paket 2D-A (Zelle): sieben Q-Ball-Karten in 2D.

Karten (Auftrag RUNDE-05/AUFTRAG-2D-A.md; Plan, Vorhersagen und Aufrufe in PLAN.md daneben):
    teilung      Bio 5/29  drehender Ball m = 2 mit kleiner Stoerung: Teilung? Windungen der Toechter?
    schale       Bio 7     Ringprofil (Q-Schale) ohne und mit Windung: Zerfall, Zeitskala
    polaritaet   Bio 23    Ball im schwachen Potentialgradienten V(x)|psi|^2: Ladungsdipol, Verformung
    vielzeller   Bio 24    drei bzw. vier Baelle mit Phasenmustern: Verschmelzen, Zusammenhalt, Auseinanderlaufen
    groesse      Bio 28    m = 1-Ball, gefuettert durch ein oder zwei gleichphasige Nachbarn (kein Bad, kein Zufluss)
    replikation  Bio 49    nur nach einer Teilung in "teilung": Toechter wachsen zusammen, Windung 2, neue Teilung?
    phasen       Chemie 12 geschlossene periodische Box, Kondensat plus Rauschen, 3 Dichten x 3 Rauschenergien
    profile      Schiessen aller benutzten Profile (m = 0, 1, 2), ohne Zeitentwicklung
    alle         nur mit --rauch: alle Karten nacheinander (Profile nur einmal geschossen)

Explorativ. Ohne Testlauf abgegeben (auf dem Laptop gilt das Interpreterverbot). Nur CUDA, float64 bzw. complex128;
ohne CUDA bricht das Programm ab.

Modell (wie tests2d_r3.py, Atlas-Normierung, d = 2):
    L = |psi_t|^2 - |grad psi|^2 - U(S) - V(x) S,  S = |psi|^2,  U(S) = S - S^2 + S^3/2.
    Ladungsdichte rho = 2 Im(psi conj(psi_t)), Energiedichte |psi_t|^2 + |grad psi|^2 + U(S) (+ V S),
    Impulsdichte p_i = -2 Re(conj(psi_t) d_i psi), Drehimpuls J = Int (x p_y - y p_x); fuer f e^{i m theta - i omega t}
    gilt J = m Q.

Grundlage: RUNDE-03/tests2d-r3/tests2d_r3.py (Schiessen, Radialtabelle, Hermite-Interpolation, periodisches Gitter,
spektraler Laplace, Velocity-Verlet, Randschicht, Messabstand 1, zwei Aufloesungen, Rauchtest). Abweichungen:
    1. Schiessen auch fuer |m| = 2: Startreihe f = p r^m (1 + a0 r^2/(4 (m + 1))), p = f^(m)(0)/m!.
    2. Unterschussregel fuer |m| >= 1 berichtigt. In tests2d_r3.py heisst Unterschuss "f' < 0", also "kehrt vor der
       Kuppe f_top um". Das tut auch der gesuchte Ball (sein Maximum liegt unter f_top); die Klammer laeuft dort gegen
       die Grenzbahn, die an der Kuppe haengen bleibt, nicht gegen den Q-Ball. Hier wie bei m = 0: Ueberschuss = ueber
       die Kuppe oder durch null; Unterschuss = nach dem ersten Abstieg wieder steigend unterhalb der Talsohle.
    3. Gitter wahlweise ohne Randschicht (nur "phasen": geschlossene Box, Q und E erhalten).
    4. Baelle mit beliebigem m und Phase; bewegter Ball fuer beliebiges m ueber die spektrale Ableitung (nur
       "replikation"; fuer m = 0 gleich dem analytischen Boost aus tests2d_r3.py).
    5. Neue Messungen: Gebiete dichter Materie (geglaettete Dichte, zusammenhaengende Gebiete auf der GPU), je Gebiet
       Ladung, Energie, Schwerpunkt, Geschwindigkeit P/E, Eigendrehimpuls/Q und Windungszahl (Phasenumlauf auf einem
       Kreis); azimutale Moden der Dichte; Drehimpuls der Box.

Aufruf:  python r5_2d_a.py KARTE [--rauch [--mini]] [--stufe grob|fein|beide] [--out ORDNER] [--tochter-m 0|1]
                                 [--omega2 W] [--geraet cuda|cpu]
Rauchtest: --rauch (Laufzeiten x 0,05; Zahlen dann ungueltig, nur Durchlauf und Hochrechnung).
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

# ---- Aus tests2d_r3.py unveraendert ----
H_ODE = 0.01             # Schrittweite beim Schiessen
X_ODE = 60.0             # Schiesslaenge
N_KAND, RUNDEN = 2048, 5 # Kandidaten je Einschachtelungsrunde, Zahl der Runden
SCHWANZ = 1e-3           # ab f < SCHWANZ * f_max (im Abfall): asymptotischer Schwanz
T_MEAS = 1.0             # Messabstand
SPONGE, SIGMA0 = 8.0, 1.0  # Breite und Staerke der Randschicht
STUFEN = (("grob", 0.3, 0.05), ("fein", 0.2, 0.025))
RAUCH_FAKTOR = 0.05

# ---- Gemeinsam, neu (vor dem Lauf festgelegt, PLAN.md Abschnitt 1) ----
L_STD = 38.4             # halbe Boxlaenge: n = 256 (grob) bzw. 384 (fein)
R_TAB = 100.0            # Radialtabelle bis r = 100 (deckt die Boxdiagonale)
BLUR = 1.0               # Gauss-Glaettung (Breite 1) der Dichte vor der Gebietssuche
SCHWELLE_REL = 0.5       # Gebiet: geglaettetes S > 0,5 * Anfangsmaximum des geglaetteten S (je Lauf)
Q_MIN_REL = 0.03         # Gebiete mit weniger als 3 % der Anfangsladung zaehlen nicht (Strahlung)
N_THETA = 128            # Punkte auf dem Kreis fuer die Windungszahl
ANALYSE_DT = 5.0         # Gebietsanalyse alle 5 Zeiteinheiten
DAUER_K = 3              # "dauerhaft" = in 3 aufeinanderfolgenden Analysen

# Karte 1, teilung (Bio 5/29)
T1_T = 1200.0            # G1-03: doppelt so lang wie in Runde 5 (600)
T1_EPS, T1_LMAX, T1_PHI = 0.01, 6, 2.4   # Stoerung je Mode l = 1..6 mit Amplitude 0,01 und Phase 2,4 l
# G1-03: Schwellen-Scan m = 2 und Gegenprobe m = 0
T1_LAEUFE_HAUPT = (("m2_055", 2, 0.55, True), ("m2_057", 2, 0.57, True), ("m2_059", 2, 0.59, True),
                   ("m2_061", 2, 0.61, True), ("m2_063", 2, 0.63, True), ("m2_065", 2, 0.65, True),
                   ("m2_070", 2, 0.70, True))
T1_LAEUFE_GEGEN = (("m0_059", 0, 0.59, True),)
T1_LAEUFE = T1_LAEUFE_HAUPT + T1_LAEUFE_GEGEN
T1_FEIN = ("m2_057", "m2_059", "m2_061", "m2_063")
T1_NACH = 30.0           # Toechter werden 30 Zeiteinheiten nach der Teilung vermessen

# Karte 2, schale (Bio 7): Q-Materie-Ring aus zwei ebenen Duennwandprofilen, S = 1 innen, omega^2 = 1/2
T2_T = 400.0
T2_R1, T2_R2, T2_W2 = 8.0, 14.0, 0.5
T2_LAEUFE = (("m0", 0, False), ("m1", 1, False), ("m3", 3, False), ("m6", 6, False), ("scheibe", 0, True))
T2_DR, T2_NBIN, T2_LMAX, T2_RWIN = 0.25, 128, 8, 30.0

# Karte 3, polaritaet (Bio 23): V(x) = g LG tanh(x/LG), Gradient g im Zentrum
T3_T, T3_LG, T3_AB = 150.0, 60.0, 50.0
T3_LAEUFE = tuple((f"w{int(round(100 * w2))}_g{gname}", w2, gw) for w2 in (0.55, 0.70)
                  for gname, gw in (("0", 0.0), ("+5e-4", 5e-4), ("+1e-3", 1e-3), ("-1e-3", -1e-3)))

# Karte 4, vielzeller (Bio 24): regelmaessiges Vieleck, Seitenlaenge 2 R_halb + Luecke
T4_T, T4_W2, T4_LUECKE = 500.0, 0.70, 4.0
T4_LAEUFE = (("n3_gleich", 3, (0.0, 0.0, 0.0)),
             ("n3_wechsel", 3, (0.0, math.pi, 0.0)),
             ("n3_windung", 3, (0.0, 2.0 * math.pi / 3.0, 4.0 * math.pi / 3.0)),
             ("n4_gleich", 4, (0.0, 0.0, 0.0, 0.0)),
             ("n4_wechsel", 4, (0.0, math.pi, 0.0, math.pi)),
             ("n4_windung", 4, (0.0, 0.5 * math.pi, math.pi, 1.5 * math.pi)),
             ("n1_kontrolle", 1, (0.0,)))
T4_FEIN = ("n3_gleich", "n3_wechsel", "n3_windung", "n4_gleich", "n4_wechsel", "n4_windung")

# Karte 5, groesse (Bio 28): m = 1 im Ursprung, m = 0-Nachbarn bei (+-D, 0), Phase 0 bzw. pi (gleichphasig am Kontakt)
T5_T, T5_LUECKE = 600.0, 3.5
T5_LAEUFE = tuple((f"w{int(round(100 * w2))}_nachbarn{k}", w2, k) for w2 in (0.60, 0.75) for k in (0, 1, 2))
T5_FEIN = tuple(n for n, _, k in T5_LAEUFE if k > 0)

# Karte 6, replikation (Bio 49): zwei Toechter (Windung aus "teilung") laufen tangential zusammen
T6_T, T6_LUECKE = 600.0, 3.5
T6_LAEUFE = (("rueck_J2", 2.0), ("rueck_J1", 1.0), ("einzel", None))   # Ziel J = Faktor * Q_gesamt
T6_FEIN = ("rueck_J2", "rueck_J1")

# Karte 7, phasen (Chemie 12): geschlossene Box ohne Randschicht
T7_T, T7_L, T7_KC = 800.0, 48.0, 1.5
T7_S0 = (0.1, 0.4, 0.9)
T7_EPS = (0.1, 1.0, 3.0)                  # Rauschenergie je Ladung in Einheiten der Bindung 1 - 1/sqrt(2)
T7_BINDUNG = 1.0 - 1.0 / math.sqrt(2.0)
T7_ANALYSE = 10.0
T7_FEIN = ((0.1, 0.1), (0.4, 1.0), (0.9, 3.0))
T7_SEED = 20260930
T7_S_DICHT, T7_OM_LO, T7_OM_HI = 0.3, 0.5, 0.97   # gebunden: S_glatt >= 0,3 und 0,5 < omega_lokal < 0,97
T7_QMIN = 0.01

_PROFILE = {}            # Zwischenspeicher (omega2, m) -> Profil


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def geraet_name():
    return torch.cuda.get_device_name(0) if DEV.type == "cuda" else "CPU (nur Form- und Syntaxprobe)"


def upot(s):
    return s - s * s + 0.5 * s ** 3


# ---------------------------------------------------------------- Profil durch Schiessen (aus tests2d_r3.py)

def rhs(r, f, fp, a0, m2):
    """f'' = (U'(f^2) - omega^2) f - f'/r + m^2 f/r^2,  U' - omega^2 = a0 - 2 f^2 + 1,5 f^4,  a0 = 1 - omega^2."""
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
    """Zustand bei r = h aus der Reihe um r = 0 (mm = |m| als Tensor).
    m = 0: f = p + g r^2/4 mit g = (U'(p^2) - omega^2) p (wie tests2d_r3.py).
    |m| >= 1: f = p r^m (1 + a0 r^2/(4 (m + 1))); fuer |m| = 1 gleich tests2d_r3.py (f = p r + (a0 p/8) r^3)."""
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
    """Schiessparameter p je Zeile (m = 0: f(0); |m| >= 1: f^(m)(0)/m!) durch Einschachteln, alle Zeilen zugleich.

    Ueberschuss: f > f_top (ueber die Kuppe) oder f < 0 (durch null). Unterschuss: f' > 0 unterhalb der Talsohle
    f_tal, nachdem die Bahn schon einmal gefallen ist (m = 0: von Anfang an; |m| >= 1: nach dem ersten Maximum).
    Fuer m = 0 ist das die Regel aus tests2d_r3.py; fuer |m| >= 1 ist sie berichtigt (Kopf der Datei, Punkt 2).
    Fuer |m| >= 1 wird ln p eingeschachtelt (1e-6 bis 10): Beim Ring (m = 2, grosses Loch) ist p etwa 1e-3, eine
    lineare Klammer ergaebe dort nur 6e-14 relative Genauigkeit. "klammer" ist bei |m| >= 1 daher relativ.
    Unentschiedene Kandidaten veraendern die Klammer nicht."""
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
        zustand = torch.zeros_like(p)                     # 0 offen, +1 Ueberschuss, -1 Unterschuss
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
    """Schiessbahn mit dem gefundenen p, dann Tabellen f, f' auf r_j = j h bis r_max und Radialintegrale.
    streng: Abbruch, wenn eine Bahn den Separatrixweg vor dem Schwanz verlaesst; sonst Zeile als ungueltig markieren."""
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
        raise RuntimeError("Schiessbahn verlaesst den Separatrixweg vor dem Schwanz (Zeilen "
                           f"{fehler.squeeze(1).nonzero().flatten().tolist()}): p zu ungenau")
    if streng and not bool(fertig.all()):
        raise RuntimeError("Schwanzschwelle innerhalb X_ODE nicht erreicht")
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
    # neu: innerer Halbwertsradius (Loch bei |m| >= 1; bei m = 0 null) und Lage des Maximums
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


def profile_holen(liste):
    """Profile (omega2, m) aus dem Zwischenspeicher; fehlende in einem Schiessdurchgang, alle Zeilen zugleich."""
    fehlt = [k for k in dict.fromkeys(liste) if k not in _PROFILE]
    if fehlt:
        sch = schiessen([w2 for w2, _ in fehlt], [m for _, m in fehlt])
        for k, pr in zip(fehlt, profile_bauen(sch, R_TAB, streng=False)):
            _PROFILE[k] = pr
    return {k: _PROFILE[k] for k in liste}


def hermite(pr, r):
    """Kubische Hermite-Interpolation von f und f' aus der Radialtabelle (Fehler O(h^4) bzw. O(h^3))."""
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
    """Periodische Box [-L, L)^2; x_j = -L + j dx liegt spiegelsymmetrisch. Neu: schwamm=False ohne Randschicht,
    Glaettungsfilter und volle Koordinatenfelder X2, Y2 (n, n) fuer die Gebietsanalyse."""

    def __init__(self, L, dx, schwamm=True):
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
        if schwamm:
            self.sigma = SIGMA0 * ((tiefe - (L - SPONGE)).clamp(min=0.0) / SPONGE) ** 2
            self.innen = (tiefe < L - SPONGE).to(F64)
        else:
            self.sigma = torch.zeros_like(tiefe)
            self.innen = torch.ones_like(tiefe)
        self.dA = dx * dx
        self.blur = torch.exp(0.5 * BLUR * BLUR * self.minus_k2)
        self.X2 = self.x.expand(1, n, n)[0].contiguous()
        self.Y2 = self.y.expand(1, n, n)[0].contiguous()


def winkelteil(f, r, X, Y, m, c):
    """f(r) e^{i m theta} = f/r^|m| (X +- iY)^|m|, glatt im Zentrum (f/r^|m| -> c = p)."""
    if m == 0:
        return f.to(C128)
    am = abs(m)
    sg = 1.0 if m > 0 else -1.0
    f_r = torch.where(r > 0.0, f / r.clamp(min=1e-300) ** am, torch.full_like(r, c))
    return f_r * (X + 1j * sg * Y) ** am


def ball_feld(g, pr, m=0, x0=0.0, y0=0.0, phase=0.0):
    """Ruhender Q-Ball psi = f(r) e^{i m theta + i phase - i omega t} bei (x0, y0); Rueckgabe psi, psi_t, Form (1, n, n)."""
    w = math.sqrt(pr["omega2"])
    X = g.x - x0
    Y = g.y - y0
    r = torch.sqrt(X * X + Y * Y)
    f, _ = hermite(pr, r)
    psi = winkelteil(f, r, X, Y, m, pr["p"]) * cmath.exp(1j * phase)
    return psi, -1j * w * psi


def ball_bewegt(g, pr, m, x0, y0, v, winkel, phase=0.0):
    """Lorentz-geboosteter Ball mit beliebigem m (Geschwindigkeit v in Richtung winkel), t = 0.
    psi = F(x') e^{i omega gamma v x_par}, psi_t = (-v d_par F - i omega gamma F) e^{...}; d_par F spektral.
    Fuer m = 0 gleich dem analytischen Boost in tests2d_r3.py."""
    w = math.sqrt(pr["omega2"])
    gam = 1.0 / math.sqrt(1.0 - v * v)
    ca, sa = math.cos(winkel), math.sin(winkel)
    X = g.x - x0
    Y = g.y - y0
    xpar = X * ca + Y * sa
    Xs = X + (gam - 1.0) * xpar * ca          # Ruhesystem-Koordinaten (Streckung laengs der Bewegung)
    Ys = Y + (gam - 1.0) * xpar * sa
    r = torch.sqrt(Xs * Xs + Ys * Ys)
    f, _ = hermite(pr, r)
    F = winkelteil(f, r, Xs, Ys, m, pr["p"])
    dF = torch.fft.ifft2(torch.fft.fft2(F) * (1j * (g.kx * ca + g.ky * sa)))
    welle = torch.exp(1j * (w * gam * v) * xpar) * cmath.exp(1j * phase)
    return F * welle, (-v * dF - 1j * (w * gam) * F) * welle


def entwickeln(g, psi, vel, dt, t_end, messen, V=None):
    """Velocity-Verlet (wie qg1.py) fuer einen Stapel (B, n, n); Laplace spektral.
    Randschicht nach jedem Schritt: psi_t -> psi_t exp(-sigma dt)."""
    daempf = torch.exp(-g.sigma * dt)
    mk2 = g.minus_k2

    def kraft(p):
        lap = torch.fft.ifft2(torch.fft.fft2(p) * mk2)
        s = p.real * p.real + p.imag * p.imag
        pot = 1.0 + s * (1.5 * s - 2.0)
        if V is not None:
            pot = pot + V
        return lap - pot * p

    n_schritte = int(round(t_end / dt))
    alle = int(round(T_MEAS / dt))
    reihe = [messen(psi, vel)]
    F = kraft(psi)
    for n in range(1, n_schritte + 1):
        vel.add_(F, alpha=0.5 * dt)
        psi.add_(vel, alpha=dt)
        F = kraft(psi)
        vel.add_(F, alpha=0.5 * dt)
        vel.mul_(daempf)
        if n % alle == 0:
            reihe.append(messen(psi, vel))
    daten = torch.stack(reihe)                            # (M, B, K)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * T_MEAS
    return t, daten


def grundmessung(g, psi, vel, V, zx, zy, r_win):
    """Dichten und Schwerpunkt (Gewicht S^2 im Fenster um den alten Schwerpunkt)."""
    s = psi.real ** 2 + psi.imag ** 2
    rho = 2.0 * (psi * vel.conj()).imag
    ph = torch.fft.fft2(psi)
    gx = torch.fft.ifft2(ph * (1j * g.kx))
    gy = torch.fft.ifft2(ph * (1j * g.ky))
    e = (vel.real ** 2 + vel.imag ** 2 + gx.real ** 2 + gx.imag ** 2 + gy.real ** 2 + gy.imag ** 2 + upot(s))
    if V is not None:
        e = e + V * s
    fenster = (((g.x - zx.view(-1, 1, 1)) ** 2 + (g.y - zy.view(-1, 1, 1)) ** 2) < r_win.view(-1, 1, 1) ** 2).to(F64)
    w = s * s * fenster
    wsum = w.sum((1, 2))
    da = wsum > 1e-200                                    # leeres Fenster: alten Schwerpunkt behalten
    X = torch.where(da, (w * g.x).sum((1, 2)) / wsum.clamp(min=1e-300), zx)
    Y = torch.where(da, (w * g.y).sum((1, 2)) / wsum.clamp(min=1e-300), zy)
    return s, rho, e, fenster, X, Y


# ---------------------------------------------------------------- Messhilfen (neu, alle auf CUDA)

def dichten(g, psi, vel):
    """S, Ladungsdichte, Energiedichte (ohne V), Impulsdichten p_x, p_y, Drehimpulsdichte um den Ursprung."""
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
    """Gauss-Glaettung (Breite BLUR) einer reellen Dichte (B, n, n) ueber FFT."""
    return torch.fft.ifft2(torch.fft.fft2(a) * g.blur).real


def komponenten(maske):
    """Zusammenhaengende Gebiete der Maske (B, n, n), 4er-Nachbarschaft, periodisch.
    Label = kleinster Flachindex im Gebiet, ausserhalb n*n. Minimum-Weitergabe plus Zeigersprung."""
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
    """Phasenumlauf von feld (n, n) auf dem Kreis (Radius rc um xc, yc), bilinear interpoliert, gegen den Uhrzeigersinn.
    Rueckgabe Windungszahl und kleinstes S auf dem Kreis (Guete: nahe null heisst unsicher)."""
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


def analyse(g, psi, dicht, maske, q_min, windung=True):
    """Gebiete der Maske je Stapelelement. Je Gebiet mit Ladung >= q_min[b]: Q, E, Schwerpunkt (Gewicht S),
    Geschwindigkeit P/E, Eigendrehimpuls/Q, mittlerer Abstand vom Schwerpunkt, Flaeche, spannt die Box (in jeder
    Spalte bzw. Zeile vertreten), Windung auf dem Kreis mit dem mittleren Abstand. Nach Q absteigend sortiert."""
    s, rho, e, px, py, jz = dicht
    lab = komponenten(maske)
    n = g.n
    spalte = torch.arange(n, device=DEV).view(1, n).expand(n, n)
    zeile = torch.arange(n, device=DEV).view(n, 1).expand(n, n)
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
        abst = torch.sqrt((g.X2[mb] - X[inv]) ** 2 + (g.Y2[mb] - Y[inv]) ** 2)
        rbar = torch.zeros(k, dtype=F64, device=DEV).index_add_(0, inv, s[b][mb] * abst) / sw
        fl = torch.zeros(k, dtype=F64, device=DEV).index_add_(0, inv, torch.ones_like(abst)) * g.dA
        nsp = torch.unique(inv * n + spalte[mb]).div(n, rounding_mode="floor").bincount(minlength=k)
        nze = torch.unique(inv * n + zeile[mb]).div(n, rounding_mode="floor").bincount(minlength=k)
        werte = torch.stack([q, en, X, Y, ppx, ppy, jspin, rbar, fl, nsp.to(F64), nze.to(F64)], dim=1).tolist()
        liste = []
        for qq, ee, xx, yy, pxx, pyy, js, rb, ff, cs, cz in werte:
            if qq < q_min[b]:
                continue
            d = {"Q": qq, "E": ee, "X": xx, "Y": yy, "vx": pxx / ee, "vy": pyy / ee, "Jspin_Q": js / qq,
                 "r_mittel": rb, "flaeche": ff, "spannt_x": cs >= n, "spannt_y": cz >= n}
            if windung:
                d["windung"], d["S_min_kreis"] = windung_kreis(g, psi[b], xx, yy, rb)
            liste.append(d)
        liste.sort(key=lambda d: -d["Q"])
        alle.append(liste)
    return alle


def azimut(g, s, zx, zy, r_win, l_max):
    """A_l = |Sum S e^{-i l theta}| / Sum S im Fenster r < r_win um (zx, zy), l = 1..l_max; Rueckgabe (B, l_max)."""
    X = g.x - zx.view(-1, 1, 1)
    Y = g.y - zy.view(-1, 1, 1)
    r2 = X * X + Y * Y
    w = s * (r2 < r_win * r_win).to(F64)
    u = (X - 1j * Y) / torch.sqrt(r2).clamp(min=1e-12)
    ws = w.sum((1, 2))
    ul = torch.ones_like(u)
    aus = []
    for _ in range(l_max):
        ul = ul * u
        aus.append((w * ul).sum((1, 2)).abs() / ws)
    return torch.stack(aus, dim=1)


def radialprofil(g, s):
    """Azimutal gemitteltes S(r) um den Ursprung in Ringen der Breite T2_DR; Rueckgabe (B, T2_NBIN)."""
    if not hasattr(g, "rbin"):
        r = torch.sqrt(g.X2 ** 2 + g.Y2 ** 2).reshape(-1)
        g.rbin = torch.floor(r / T2_DR).long().clamp(max=T2_NBIN)
        g.rzahl = torch.bincount(g.rbin, minlength=T2_NBIN + 1).to(F64).clamp(min=1.0)
    B = s.shape[0]
    summe = torch.zeros(B, T2_NBIN + 1, dtype=F64, device=DEV).index_add_(1, g.rbin, s.reshape(B, -1))
    return summe[:, :T2_NBIN] / g.rzahl[:T2_NBIN]


def stoerfaktor(g, x0, y0, r_s, eps):
    """1 + eps Sum_{l=1..T1_LMAX} Re[e^{i phi_l} (z/r_s)^l] exp(-l (r^2/r_s^2 - 1)/2), phi_l = T1_PHI l.
    Jede Mode hat bei r = r_s genau die Amplitude eps; glatt im Zentrum (Polynom mal Gauss)."""
    X = g.x - x0
    Y = g.y - y0
    z = (X + 1j * Y) / r_s
    u2 = (X * X + Y * Y) / (r_s * r_s)
    fak = torch.ones_like(u2)
    zl = torch.ones_like(z)
    for l in range(1, T1_LMAX + 1):
        zl = zl * z
        fak = fak + eps * (zl * cmath.exp(1j * T1_PHI * l)).real * torch.exp(-0.5 * l * (u2 - 1.0))
    return fak


def lauf_standard(g, psi, vel, dt, t_end, r_win=None, l_max=0, radial=False, windung=True):
    """Zeitentwicklung mit Standardmessung je Messpunkt: Q_box, E_box, J_box, S_max; mit r_win zusaetzlich Schwerpunkt
    (Gewicht S^2 im Fenster, wie tests2d_r3.py) und A_1..A_lmax; mit radial S(r=0), R_innen, R_aussen (S-Mittel >= 0,5).
    Alle ANALYSE_DT: Gebietsanalyse. Rueckgabe t, daten (M, B, K), verlauf (je Lauf Liste (t, Gebiete))."""
    B = psi.shape[0]
    s0, rho0, _, _, _, _ = dichten(g, psi, vel)
    schwelle = SCHWELLE_REL * unschaerfe(g, s0).amax((1, 2))
    q_min = (Q_MIN_REL * rho0.sum((1, 2)) * g.dA).tolist()
    zx = torch.zeros(B, dtype=F64, device=DEV)
    zy = torch.zeros(B, dtype=F64, device=DEV)
    verlauf = [[] for _ in range(B)]
    zaehler = [0]
    alle = int(round(ANALYSE_DT / T_MEAS))

    def messen(psi, vel):
        nonlocal zx, zy
        dicht = dichten(g, psi, vel)
        s, rho, e, _, _, jz = dicht
        spalten = [rho.sum((1, 2)) * g.dA, e.sum((1, 2)) * g.dA, jz.sum((1, 2)) * g.dA, s.amax((1, 2))]
        if r_win is not None:
            fen = (((g.x - zx.view(-1, 1, 1)) ** 2 + (g.y - zy.view(-1, 1, 1)) ** 2) < r_win ** 2).to(F64)
            w = s * s * fen
            wsum = w.sum((1, 2))
            da = wsum > 1e-200
            X = torch.where(da, (w * g.x).sum((1, 2)) / wsum.clamp(min=1e-300), zx)
            Y = torch.where(da, (w * g.y).sum((1, 2)) / wsum.clamp(min=1e-300), zy)
            zx, zy = X, Y
            spalten += [X, Y]
            if l_max:
                spalten += list(azimut(g, s, X, Y, r_win, l_max).unbind(1))
        if radial:
            sr = radialprofil(g, s)
            innen = sr >= 0.5
            hat = innen.any(dim=1)
            i_in = innen.to(torch.int64).argmax(dim=1)
            i_out = T2_NBIN - 1 - innen.flip(1).to(torch.int64).argmax(dim=1)
            leer = torch.full_like(sr[:, 0], -1.0)
            spalten += [sr[:, 0], torch.where(hat, i_in.to(F64) * T2_DR, leer),
                        torch.where(hat, (i_out.to(F64) + 1.0) * T2_DR, leer)]
        if zaehler[0] % alle == 0:
            maske = unschaerfe(g, s) > schwelle.view(-1, 1, 1)
            for b, geb in enumerate(analyse(g, psi, dicht, maske, q_min, windung)):
                verlauf[b].append((zaehler[0] * T_MEAS, geb))
        zaehler[0] += 1
        return torch.stack(spalten, dim=1)

    t, daten = entwickeln(g, psi, vel, dt, t_end, messen)
    return t, daten, verlauf


# ---------------------------------------------------------------- Auswertehilfen

def polyfit(t, y, grad):
    """y = sum_k c_k tau^k, tau = (t - t0)/Spanne. Rueckgabe c, Standardfehler (weisses Rauschen), Rest-RMS, Spanne."""
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
    """Erste Zeit, ab der flags in k aufeinanderfolgenden Analysen gilt (sonst None)."""
    for i in range(len(flags) - k + 1):
        if all(flags[i:i + k]):
            return ts[i]
    return None


def naechste(ts, ziel):
    return min(range(len(ts)), key=lambda i: abs(ts[i] - ziel))


def gebiet_kurz(d):
    return {k: d[k] for k in ("Q", "windung", "Jspin_Q", "vx", "vy", "X", "Y", "S_min_kreis") if k in d}


def verlauf_kurz(verlauf):
    """Fuer die JSON-Ausgabe: je Analysezeit [t, Zahl, [[Q, Windung, Jspin/Q, X, Y, vx, vy], ...]]."""
    return [[t, len(gb), [[round(d["Q"], 4), d.get("windung"), round(d["Jspin_Q"], 4), round(d["X"], 3),
                            round(d["Y"], 3), round(d["vx"], 5), round(d["vy"], 5)] for d in gb]] for t, gb in verlauf]


def erhaltung(t, daten, b):
    return {"Q_box_verlust": (1.0 - daten[-1, b, 0] / daten[0, b, 0]).item(),
            "E_box_verlust": (1.0 - daten[-1, b, 1] / daten[0, b, 1]).item(),
            "J_box_aenderung": (daten[-1, b, 2] - daten[0, b, 2]).item(),
            "J_box_start": daten[0, b, 2].item(), "Q_box_start": daten[0, b, 0].item()}


def schreiben(out, name, ausgabe, zeitreihen, text):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, name + "_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1)
    torch.save(zeitreihen, os.path.join(out, name + "_zeitreihen.pt"))
    with open(os.path.join(out, name + "_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


def laufzeit_text(dauer, rauch):
    zeilen = ["Dauer [s]: " + ", ".join(f"{k} {s:.1f}" for k, s in dauer.items())]
    if rauch:
        entw = sum(s for k, s in dauer.items() if k.startswith("entw"))
        rest = sum(s for k, s in dauer.items() if not k.startswith("entw"))
        zeilen.append(f"Hochrechnung Hauptlauf: {rest + entw / RAUCH_FAKTOR:.0f} s "
                      f"(nicht entwickelnde Teile {rest:.0f} s + Entwicklung x {1 / RAUCH_FAKTOR:.0f}); "
                      "ueber 540 s: nicht starten, Leitung entscheidet (Stufen einzeln mit --stufe).")
    return zeilen


def kopf(titel, start, rauch):
    return (f"{titel}. Start {start}, Ende {jetzt()}, {geraet_name()}, torch {torch.__version__}"
            + (" RAUCHTEST: Zahlen ungueltig" if rauch else ""))


def auswahl(laeufe, stufe, fein, prof, schluessel, notizen):
    """Laeufe der Stufe (fein: nur die genannten); Laeufe mit ungueltigem Profil entfallen mit Notiz."""
    aus = []
    for lauf in laeufe:
        if stufe == "fein" and lauf[0] not in fein:
            continue
        ks = schluessel(lauf)
        if any(not prof[k]["gueltig"] for k in ks):
            notizen.append(f"{stufe} {lauf[0]}: Profil ungueltig, Lauf entfaellt")
            continue
        aus.append(lauf)
    return aus


# ---------------------------------------------------------------- Profile (nur Schiessen)

ALLE_PROFILE = ((0.55, 0), (0.55, 1), (0.55, 2), (0.60, 0), (0.60, 1), (0.65, 1), (0.65, 2), (0.70, 0), (0.75, 0),
                (0.75, 1), (0.80, 0), (0.80, 1), (0.80, 2))


def test_profile(out, rauch, stufen, args):
    start = jetzt()
    print(f"Profile Start {start} auf {geraet_name()}", flush=True)
    t0 = uhr()
    prof = profile_holen(list(ALLE_PROFILE))
    dauer = {"schiessen_s": uhr() - t0}
    zeilen = [profil_info(prof[k]) for k in ALLE_PROFILE]
    text = [kopf("Profile m = 0, 1, 2 (nur Schiessen)", start, False)]
    text += laufzeit_text(dauer, False)
    text.append("m omega2 | p | Klammer | S_max | R_kern_halb | R_max | R_halb | Q | E | E/Q | Virialrest | gueltig")
    for z in zeilen:
        text.append(f"  {z['m']} {z['omega2']:.2f} | {z['p']:.15f} | {z['klammer']:.1e} | {z['S_max']:.5f} | "
                    f"{z['R_kern_halb']:.3f} | {z['R_max']:.3f} | {z['R_halb']:.3f} | {z['Q']:.3f} | {z['E']:.3f} | "
                    f"{(z['E'] / z['Q'] if z['Q'] else float('nan')):.5f} | {z['virialrest']:.1e} | "
                    f"{'ja' if z['gueltig'] else 'NEIN'}")
    text.append("Erwartung (PLAN.md 1.2): Virialrest < 1e-5 fuer alle gueltigen Zeilen; m = 1, 2: Loch R_kern_halb > 0; "
                "m = 2 bei 0,55 ringfoermig (R_kern_halb etwa 4 bis 8).")
    tabellen = {"schluessel": list(ALLE_PROFILE), "h": H_ODE,
                "f": torch.stack([prof[k]["f"] for k in ALLE_PROFILE]).cpu()}
    schreiben(out, "profile", {"test": "profile", "start": start, "dauer_s": dauer, "profile": zeilen}, tabellen,
              "\n".join(text))


# ---------------------------------------------------------------- Karte 1: Teilung und Vererbung (Bio 5/29)

def test_teilung(out, rauch, stufen, args):
    start = jetzt()
    print(f"G1-03 Teilung ({args.teil}) Start {start} auf {geraet_name()}, torch {torch.__version__}", flush=True)
    dauer, notizen = {}, []
    t0 = uhr()
    laeufe_teil = T1_LAEUFE_HAUPT if args.teil == "haupt" else T1_LAEUFE_GEGEN     # G1-03
    prof = profile_holen([(w2, m) for _, m, w2, _ in laeufe_teil])
    dauer["schiessen_s"] = uhr() - t0
    t_end = args.t_end * (RAUCH_FAKTOR if rauch else 1.0)                            # G1-03
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = auswahl(laeufe_teil, stufe, T1_FEIN, prof, lambda l: [(l[2], l[1])], notizen)   # G1-03
        if not laeufe:
            continue
        g = Gitter(L_STD, dx)
        psis, vels = [], []
        for name, m, w2, stoer in laeufe:
            pr = prof[(w2, m)]
            p_, v_ = ball_feld(g, pr, m)
            if stoer:
                fak = stoerfaktor(g, 0.0, 0.0, max(pr["R_max"], 0.7 * pr["R_halb"]), T1_EPS)
                p_, v_ = p_ * fak, v_ * fak
            psis.append(p_)
            vels.append(v_)
        psi = torch.cat(psis).contiguous()
        vel = torch.cat(vels).contiguous()
        r_win = max(prof[(w2, m)]["R_halb"] for _, m, w2, _ in laeufe) + 12.0
        t0 = uhr()
        t, daten, verlauf = lauf_standard(g, psi, vel, dt, t_end, r_win=r_win, l_max=T1_LMAX)
        dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
        for b, (name, m, w2, stoer) in enumerate(laeufe):
            pr = prof[(w2, m)]
            ts = [tt for tt, _ in verlauf[b]]
            ns = [len(gb) for _, gb in verlauf[b]]
            t_teil = erste_dauerhaft(ts, [n >= 2 for n in ns])
            zeile = {"lauf": name, "m": m, "omega2": w2, "gestoert": stoer, "stufe": stufe, "dx": dx, "dt": dt,
                     "Q_profil": pr["Q"], "n_max": max(ns), "n_ende": ns[-1], "teilung": t_teil is not None,
                     "t_teilung": t_teil, **erhaltung(t, daten, b)}
            if t_teil is not None:
                i_z = naechste(ts, t_teil + T1_NACH)
                gb = verlauf[b][i_z][1]
                zeile["t_toechter"] = ts[i_z]
                zeile["toechter"] = [gebiet_kurz(d) for d in gb]
                zeile["windungen_toechter"] = [d["windung"] for d in gb]
                zeile["drehimpuls_eigen_anteil"] = (sum(d["Jspin_Q"] * d["Q"] for d in gb)
                                                    / max(abs(daten[i_z * int(round(ANALYSE_DT / T_MEAS)), b, 2].item()),
                                                          1e-300))
            else:
                zeile["windung_ende"] = [d["windung"] for d in verlauf[b][-1][1]]
            # azimutale Moden: dominante Mode und Wachstumsrate (Fit ln A_l ueber 3 A_l(0) <= A_l <= 0,2)
            i_ref = (int(round(t_teil / T_MEAS)) if t_teil is not None else daten.shape[0] - 1)
            am = daten[:, b, 6:6 + T1_LMAX]
            l_dom = int(torch.argmax(am[i_ref])) + 1
            a = am[:, l_dom - 1]
            maske = ((a >= 3.0 * a[0]) & (a > 1e-12) & (a <= 0.2)
                     & (torch.arange(a.shape[0], device=DEV) <= i_ref))
            zeile["l_dominant"] = l_dom
            zeile["A_start_ende"] = [a[0].item(), a[i_ref].item()]
            zeile["gamma"] = None
            if int(maske.sum()) >= 8:
                fit = polyfit(t[maske], torch.log(a[maske]), 1)
                if fit is not None:
                    zeile["gamma"] = (fit[0][1] / fit[3]).item()
                    zeile["gamma_rest_rms"] = fit[2].item()
            # G1-03: Plausibilitaetsschranke (KARTE.md)
            qb = daten[:, b, 0]
            q0 = qb[0].item()
            tl = t.tolist()
            t_ref = 0.5 * t_teil if t_teil is not None else tl[-1]
            i_q = naechste(tl, t_ref)
            pl = {"Q_nie_wachsend": bool(qb.max().item() <= q0 * (1.0 + 1e-4)),
                  "Q_max_rel": qb.max().item() / q0 - 1.0,
                  "Q_erhalten_bis_t": tl[i_q], "Q_rel_aenderung": abs(1.0 - qb[i_q].item() / q0)}
            pl["Q_erhalten"] = pl["Q_rel_aenderung"] <= 2e-3
            pl["J_durch_Q_start"] = daten[0, b, 2].item() / q0
            pl["JQ_gleich_m"] = abs(pl["J_durch_Q_start"] - m) <= 1e-3
            if t_teil is not None:
                gb_t = verlauf[b][naechste(ts, t_teil + T1_NACH)][1]
                pl["summe_toechter_Q"] = sum(d["Q"] for d in gb_t)
                pl["toechter_Q_ok"] = pl["summe_toechter_Q"] <= 1.002 * q0
                pl["v_max_toechter"] = max((math.hypot(d["vx"], d["vy"]) for d in gb_t), default=0.0)
                pl["v_ok"] = pl["v_max_toechter"] < 1.0
            pl["gamma_ok"] = zeile["gamma"] is None or 0.0 <= zeile["gamma"] <= 1.0
            pl["bestanden"] = all(v for k, v in pl.items()
                                  if k.endswith("_ok") or k in ("Q_nie_wachsend", "Q_erhalten", "JQ_gleich_m"))
            zeile["plausibel"] = pl
            zeile["gebiete"] = verlauf_kurz(verlauf[b])
            ergebnis.setdefault(stufe, []).append(zeile)
        zeitreihen[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "laeufe": [l[0] for l in laeufe],
                             "spalten": ["Q_box", "E_box", "J_box", "S_max", "X", "Y"]
                             + [f"A{l}" for l in range(1, T1_LMAX + 1)]}
    # G1-03: Kennzahlen gegen KARTE.md (vor jedem Lauf festgelegt; Vorhersage geschrieben 07:58:24)
    grob_liste, grob_quelle = ergebnis.get("grob"), "dieser Aufruf"
    if grob_liste is None and args.teil == "haupt":
        pfad = os.path.join(out, "teilung_haupt_grob_ergebnis.json")
        if os.path.exists(pfad):
            with open(pfad) as fh:
                grob_liste = json.load(fh)["ergebnis"].get("grob")
            grob_quelle = pfad
    grob = {z["lauf"]: z for z in (grob_liste or [])}
    kenn = {"grob_quelle": grob_quelle if grob else None}
    if args.teil == "haupt" and grob:
        m2 = sorted(((z["omega2"], z) for z in grob.values() if z["m"] == 2), key=lambda p: p[0])
        folge = [(w2, bool(z["teilung"])) for w2, z in m2]
        teilend = [w2 for w2, tt in folge if tt]
        nicht = [w2 for w2, tt in folge if not tt]
        monoton = all((not a[1]) or b_[1] for a, b_ in zip(folge[:-1], folge[1:]))
        w_lo = max(nicht) if nicht else None
        w_hi = min(teilend) if teilend else None
        d055, d065 = dict(folge).get(0.55), dict(folge).get(0.65)
        kenn["V1"] = {"folge": folge, "monoton": monoton, "hoechste_nicht_teilende": w_lo, "tiefste_teilende": w_hi,
                      "teilt_055": d055, "teilt_065": d065,
                      "bestanden": bool(monoton and d055 is False and d065 is True)}
        gam = [(w2, z["gamma"]) for w2, z in m2 if z["teilung"]]
        gam_ok = [(w, g_) for w, g_ in gam if g_ is not None]
        v2 = {"gamma_teilende": gam}
        if len(gam_ok) >= 2 and w_lo is not None:
            mono_g = all(g2 >= g1 for (_, g1), (_, g2) in zip(gam_ok[:-1], gam_ok[1:]))
            (wa, ga), (wb, gbb) = gam_ok[0], gam_ok[1]
            w0 = wa - ga * ga * (wb - wa) / (gbb * gbb - ga * ga) if gbb * gbb > ga * ga else None
            v2.update({"gamma_monoton": mono_g, "nullpunkt_gamma2": w0, "grenze_minus_0_03": w_lo - 0.03,
                       "bestanden": bool(mono_g and w0 is not None and w0 >= w_lo - 0.03)})
        else:
            v2.update({"bestanden": None,
                       "grund": "weniger als zwei teilende Laeufe mit gamma, oder keine nicht teilende Stelle"})
        kenn["V2"] = v2
        wind = [w for _, z in m2 if z["teilung"] for w in z.get("windungen_toechter", [])]
        kenn["V3"] = {"windungen_toechter": wind, "bestanden": (all(w == 0 for w in wind) if wind else None)}
        kenn["scheitert"] = any(kenn[v]["bestanden"] is False for v in ("V1", "V2", "V3"))
    if args.teil == "gegen" and grob:
        z0 = grob.get("m0_059")
        if z0:
            kenn["gegenprobe"] = {"teilung": z0["teilung"], "gamma": z0["gamma"],
                                  "bestanden": bool((not z0["teilung"]) and (z0["gamma"] is None or z0["gamma"] < 0.005))}
    kenn["plausibel"] = {f"{z['stufe']}_{z['lauf']}": z["plausibel"]["bestanden"]
                         for st in ergebnis.values() for z in st}
    kenn["plausibilitaet_bestanden"] = all(kenn["plausibel"].values()) if kenn["plausibel"] else None
    if "fein" in ergebnis and grob:
        l3 = []
        for zf in ergebnis["fein"]:
            zg = grob.get(zf["lauf"])
            if not zg:
                continue
            gleich = (zf["teilung"] == zg["teilung"]
                      and len(zf.get("windungen_toechter", [])) == len(zg.get("windungen_toechter", [])))
            dt_ok = (not zf["teilung"]) or abs(zf["t_teilung"] - zg["t_teilung"]) <= max(0.1 * zg["t_teilung"], 10.0)
            dg = None
            if zf["gamma"] and zg["gamma"]:
                dg = abs(zf["gamma"] / zg["gamma"] - 1.0)
            l3.append({"lauf": zf["lauf"], "ausgang_und_toechterzahl_gleich": gleich, "t_teilung_ok_info": dt_ok,
                       "gamma_rel_aenderung": dg, "bestanden": gleich and (dg is None or dg <= 0.2)})
        kenn["L3"] = {"laeufe": l3, "bestanden": all(z["bestanden"] for z in l3) if l3 else None}
    ausgabe = {"test": "teilung", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "torch": torch.__version__, "notizen": notizen,
               "parameter": {"T": args.t_end, "teil": args.teil, "eps": T1_EPS, "l_max": T1_LMAX, "L": L_STD, "stufen": STUFEN,
                             "schwelle_rel": SCHWELLE_REL, "q_min_rel": Q_MIN_REL, "blur": BLUR},
               "profile": [profil_info(prof[(w2, m)]) for _, m, w2, _ in laeufe_teil],
               "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf(f"G1-03 Teilung m = 2, Schwelle in omega^2 ({args.teil})", start, rauch)]
    text += laufzeit_text(dauer, rauch) + notizen
    text.append("Stufe Lauf | Q | Teilung t | n_max | Toechter (Q, Windung, Jspin/Q, v) | l_dom | gamma | Q/E-Verlust")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            if z["teilung"]:
                toe = "; ".join(f"{d['Q']:.1f} w{d['windung']} s{d['Jspin_Q']:.2f} v({d['vx']:.3f},{d['vy']:.3f})"
                                for d in z["toechter"])
            else:
                toe = f"keine (Windung Ende {z['windung_ende']})"
            gam = f"{z['gamma']:.4f}" if z["gamma"] else "-"
            text.append(f"  {stufe} {z['lauf']} | {z['Q_profil']:.1f} | {z['t_teilung']} | {z['n_max']} | {toe} | "
                        f"{z['l_dominant']} | {gam} | {z['Q_box_verlust']:.1e}/{z['E_box_verlust']:.1e}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, f"teilung_{args.teil}_{'_'.join(stufen)}", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- Karte 2: Q-Schale (Bio 7)

def schalen_feld(g, m, scheibe):
    """Q-Materie aus ebenen Duennwandprofilen S(xi) = 1/(1 + e^{sqrt 2 xi}) (exakt bei omega^2 = 1/2), S = 1 innen.
    Ring R1 < r < R2 bzw. Scheibe gleicher Flaeche; Windung m glatt im Zentrum; psi_t = -i omega psi."""
    X, Y = g.x, g.y
    r = torch.sqrt(X * X + Y * Y)
    k = math.sqrt(2.0)
    if scheibe:
        s = 1.0 / (1.0 + torch.exp(k * (r - math.sqrt(T2_R2 ** 2 - T2_R1 ** 2))))
    else:
        s = 1.0 / ((1.0 + torch.exp(k * (T2_R1 - r))) * (1.0 + torch.exp(k * (r - T2_R2))))
    psi = torch.sqrt(s).to(C128)
    if m != 0:
        psi = psi * (X + 1j * Y) ** m / (r * r + 1.0) ** (0.5 * m)
    w = math.sqrt(T2_W2)
    return psi, -1j * w * psi


def test_schale(out, rauch, stufen, args):
    start = jetzt()
    print(f"Karte 2 Q-Schale Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t_end = T2_T * (RAUCH_FAKTOR if rauch else 1.0)
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        g = Gitter(L_STD, dx)
        felder = [schalen_feld(g, m, sch) for _, m, sch in T2_LAEUFE]
        psi = torch.cat([f[0] for f in felder]).contiguous()
        vel = torch.cat([f[1] for f in felder]).contiguous()
        t0 = uhr()
        t, daten, verlauf = lauf_standard(g, psi, vel, dt, t_end, r_win=T2_RWIN, l_max=T2_LMAX, radial=True)
        dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
        i_s0, i_rin, i_rout = 6 + T2_LMAX, 7 + T2_LMAX, 8 + T2_LMAX
        haelfte = t >= 0.5 * t[-1]
        for b, (name, m, sch) in enumerate(T2_LAEUFE):
            s0r = daten[:, b, i_s0]
            gefuellt = (s0r >= 0.5).nonzero()
            rin = daten[:, b, i_rin]
            rin_h = rin[haelfte & (rin >= 0.0)]
            ts = [tt for tt, _ in verlauf[b]]
            ns = [len(gb) for _, gb in verlauf[b]]
            zeile = {"lauf": name, "m": m, "scheibe": sch, "stufe": stufe,
                     "t_gefuellt": t[int(gefuellt[0])].item() if gefuellt.numel() else None,
                     "R_innen_start": rin[0].item(),
                     "R_innen_2haelfte": ([rin_h.min().item(), rin_h.mean().item(), rin_h.max().item()]
                                          if rin_h.numel() else None),
                     "R_aussen_start_ende": [daten[0, b, i_rout].item(), daten[-1, b, i_rout].item()],
                     "n_max": max(ns), "n_ende": ns[-1],
                     "t_bruch": erste_dauerhaft(ts, [n >= 2 for n in ns]),
                     "gebiete_ende": [gebiet_kurz(d) for d in verlauf[b][-1][1]],
                     "A_max_2haelfte": [daten[haelfte, b, 6 + l].max().item() for l in range(T2_LMAX)],
                     "J_zu_Q_start": (daten[0, b, 2] / daten[0, b, 0]).item(), **erhaltung(t, daten, b),
                     "gebiete": verlauf_kurz(verlauf[b])}
            ergebnis.setdefault(stufe, []).append(zeile)
        zeitreihen[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "laeufe": [l[0] for l in T2_LAEUFE],
                             "spalten": ["Q_box", "E_box", "J_box", "S_max", "X", "Y"]
                             + [f"A{l}" for l in range(1, T2_LMAX + 1)] + ["S_r0", "R_innen", "R_aussen"]}
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn = {}
    if "m0" in grob:
        tf = grob["m0"]["t_gefuellt"]
        kenn["ohne_windung"] = (f"Schale fuellt sich nach t = {tf}" if tf is not None
                                else "Loch bleibt bis T offen (gegen die Vorhersage)")
    for n in ("m1", "m3", "m6"):
        if n in grob:
            z = grob[n]
            ri = z["R_innen_2haelfte"]
            if z["t_bruch"] is not None:
                kenn[n] = f"zerbricht bei t = {z['t_bruch']} in {z['n_max']} Gebiete"
            elif ri is not None and ri[0] >= 4.0:
                kenn[n] = f"Ring haelt bis T (R_innen 2. Haelfte {ri[0]:.1f} bis {ri[2]:.1f})"
            else:
                kenn[n] = f"Loch schrumpft unter 4 (Wirbelkern), t_gefuellt {z['t_gefuellt']}"
    if "scheibe" in grob:
        z = grob["scheibe"]
        kenn["gegenprobe_scheibe_ruhig"] = z["t_bruch"] is None and z["n_max"] == 1
    if "fein" in ergebnis:
        l3 = []
        for zf in ergebnis["fein"]:
            zg = grob.get(zf["lauf"])
            if not zg:
                continue
            ok = (zf["n_max"] == zg["n_max"] and (zf["t_gefuellt"] is None) == (zg["t_gefuellt"] is None)
                  and (zg["t_gefuellt"] is None or abs(zf["t_gefuellt"] - zg["t_gefuellt"])
                       <= max(0.1 * zg["t_gefuellt"], 3.0)))
            l3.append({"lauf": zf["lauf"], "bestanden": ok})
        kenn["L3"] = {"laeufe": l3, "bestanden": all(z["bestanden"] for z in l3) if l3 else None}
    ausgabe = {"test": "schale", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "parameter": {"T": T2_T, "R1": T2_R1, "R2": T2_R2,
               "omega2": T2_W2, "L": L_STD, "stufen": STUFEN}, "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Karte 2 Q-Schale (Bio 7)", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append("Stufe Lauf | J/Q | t_gefuellt | R_innen 2. Haelfte (min, mittel, max) | R_aussen Start/Ende | "
                "n_max | t_bruch | Windungen Ende | Q-Verlust")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            ri = z["R_innen_2haelfte"]
            ri_t = f"{ri[0]:.2f}, {ri[1]:.2f}, {ri[2]:.2f}" if ri else "-"
            text.append(f"  {stufe} {z['lauf']} | {z['J_zu_Q_start']:.3f} | {z['t_gefuellt']} | {ri_t} | "
                        f"{z['R_aussen_start_ende'][0]:.2f}/{z['R_aussen_start_ende'][1]:.2f} | {z['n_max']} | "
                        f"{z['t_bruch']} | {[d.get('windung') for d in z['gebiete_ende']]} | {z['Q_box_verlust']:.1e}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "schale", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- Karte 3: Polaritaet im Gradienten (Bio 23)

def test_polaritaet(out, rauch, stufen, args):
    start = jetzt()
    print(f"Karte 3 Polaritaet Start {start} auf {geraet_name()}", flush=True)
    dauer, notizen = {}, []
    t0 = uhr()
    prof = profile_holen([(w2, 0) for _, w2, _ in T3_LAEUFE])
    dauer["schiessen_s"] = uhr() - t0
    t_end = T3_T * (RAUCH_FAKTOR if rauch else 1.0)
    t_ab = T3_AB * (RAUCH_FAKTOR if rauch else 1.0)
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = auswahl(T3_LAEUFE, stufe, [l[0] for l in T3_LAEUFE], prof, lambda l: [(l[1], 0)], notizen)
        if not laeufe:
            continue
        g = Gitter(L_STD, dx)
        felder = [ball_feld(g, prof[(w2, 0)], 0) for _, w2, _ in laeufe]
        psi = torch.cat([f[0] for f in felder]).contiguous()
        vel = torch.cat([f[1] for f in felder]).contiguous()
        V = torch.cat([gw * T3_LG * torch.tanh(g.x / T3_LG) for _, _, gw in laeufe])      # (B, 1, n)
        B = psi.shape[0]
        zx = torch.zeros(B, dtype=F64, device=DEV)
        zy = torch.zeros(B, dtype=F64, device=DEV)
        r_win = torch.tensor([prof[(w2, 0)]["R_halb"] + 12.0 for _, w2, _ in laeufe], dtype=F64, device=DEV)

        def messen(psi, vel):
            nonlocal zx, zy
            s, rho, e, fen, X, Y = grundmessung(g, psi, vel, None, zx, zy, r_win)   # e ohne V (innere Energie)
            sf, rf, ef = s * fen, rho * fen, e * fen
            ss, rs, es = sf.sum((1, 2)), rf.sum((1, 2)), ef.sum((1, 2))
            xq, xe, xs = (rf * g.x).sum((1, 2)) / rs, (ef * g.x).sum((1, 2)) / es, (sf * g.x).sum((1, 2)) / ss
            yq, ye, ys = (rf * g.y).sum((1, 2)) / rs, (ef * g.y).sum((1, 2)) / es, (sf * g.y).sum((1, 2)) / ss
            dxs = g.x - xs.view(-1, 1, 1)
            dys = g.y - ys.view(-1, 1, 1)
            r2 = dxs * dxs + dys * dys
            m2 = (sf * r2).sum((1, 2)) / ss
            schief = (sf * dxs ** 3).sum((1, 2)) / ss / m2 ** 1.5
            lang = (sf * (dxs * dxs - dys * dys)).sum((1, 2)) / (sf * r2).sum((1, 2))
            zx, zy = X, Y
            return torch.stack([X, Y, xq, xe, xs, yq, ye, schief, lang, rs * g.dA, es * g.dA,
                                rho.sum((1, 2)) * g.dA, (e + V * s).sum((1, 2)) * g.dA], dim=1)

        t0 = uhr()
        t, daten = entwickeln(g, psi, vel, dt, t_end, messen, V=V)
        dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
        spaet = t >= t_ab
        for b, (name, w2, gw) in enumerate(laeufe):
            pr = prof[(w2, 0)]
            d = daten[:, b, :]
            zeile = {"lauf": name, "omega2": w2, "g": gw, "stufe": stufe}
            fit = polyfit(t, d[:, 3], 2)
            zeile["a_mess"] = (2.0 * fit[0][2] / fit[3] ** 2).item() if fit is not None else None
            zeile["a_vorhersage"] = -gw * pr["N"] / pr["E"]
            zeile["a_verhaeltnis"] = (zeile["a_mess"] / zeile["a_vorhersage"]
                                      if gw != 0.0 and zeile["a_mess"] is not None else None)
            for key, reihe in (("d_QE", d[:, 2] - d[:, 3]), ("d_SE", d[:, 4] - d[:, 3]), ("schiefe", d[:, 7]),
                               ("langstreckung", d[:, 8]), ("y_QE_kontrolle", d[:, 5] - d[:, 6])):
                zeile[key] = [reihe[spaet].mean().item(), reihe[spaet].std().item()]
            zeile["X_ende"] = d[-1, 0].item()
            zeile["Q_fenster_verlust"] = (1.0 - d[-1, 9] / d[0, 9]).item()
            zeile["E_gesamt_verlust"] = (1.0 - d[-1, 12] / d[0, 12]).item()
            ergebnis.setdefault(stufe, []).append(zeile)
        zeitreihen[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "laeufe": [l[0] for l in laeufe],
                             "spalten": ["X_S2", "Y_S2", "X_Q", "X_E", "X_S", "Y_Q", "Y_E", "schiefe", "langstreckung",
                                         "Q_fenster", "E_fenster", "Q_box", "E_gesamt"]}
    kenn = {}
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    for w2 in (0.55, 0.70):
        k = f"w{int(round(100 * w2))}"
        z0, z1, z2, zm = (grob.get(f"{k}_g{s}") for s in ("0", "+5e-4", "+1e-3", "-1e-3"))
        if not (z0 and z1 and z2 and zm):
            continue
        d1, d2, dm = z1["d_QE"][0], z2["d_QE"][0], zm["d_QE"][0]
        kenn[k] = {"null_d_QE": z0["d_QE"][0], "null_schiefe": z0["schiefe"][0],
                   "linear_2g_zu_g": d2 / d1 if d1 != 0.0 else None,
                   "antisymmetrie": dm / d2 if d2 != 0.0 else None,
                   "d_QE_bei_1e-3": d2, "d_SE_bei_1e-3": z2["d_SE"][0], "schiefe_bei_1e-3": z2["schiefe"][0],
                   "langstreckung_bei_1e-3": z2["langstreckung"][0], "a_verhaeltnis_1e-3": z2["a_verhaeltnis"]}
    if "fein" in ergebnis:
        l3 = []
        for zf in ergebnis["fein"]:
            zg = grob.get(zf["lauf"])
            if not zg or zg["g"] == 0.0:
                continue
            aend = abs(zf["d_QE"][0] - zg["d_QE"][0])
            l3.append({"lauf": zf["lauf"], "aenderung_d_QE": aend, "bestanden": aend <= 0.2 * abs(zg["d_QE"][0])})
        kenn["L3"] = {"laeufe": l3, "bestanden": all(z["bestanden"] for z in l3) if l3 else None}
    ausgabe = {"test": "polaritaet", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "notizen": notizen,
               "parameter": {"T": T3_T, "LG": T3_LG, "t_ab": T3_AB, "L": L_STD, "stufen": STUFEN},
               "profile": [profil_info(prof[(w2, 0)]) for w2 in (0.55, 0.70)],
               "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Karte 3 Polaritaet im Gradienten (Bio 23)", start, rauch)]
    text += laufzeit_text(dauer, rauch) + notizen
    text.append("Stufe Lauf | a_mess/a_vorh | d_QE (Mittel, Streuung) | d_SE | Schiefe | Langstreckung | y-Kontrolle")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            av = f"{z['a_verhaeltnis']:.4f}" if z["a_verhaeltnis"] is not None else "-"
            text.append(f"  {stufe} {z['lauf']} | {av} | {z['d_QE'][0]:.3e} ({z['d_QE'][1]:.1e}) | "
                        f"{z['d_SE'][0]:.3e} | {z['schiefe'][0]:.3e} | {z['langstreckung'][0]:.3e} | "
                        f"{z['y_QE_kontrolle'][0]:.1e}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "polaritaet", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- Karte 4: Vielzeller (Bio 24)

def vieleck(n_b, d):
    """Ecken eines regelmaessigen n-Ecks mit Seitenlaenge d um den Ursprung (Dreieck Spitze oben, Quadrat achsparallel),
    gegen den Uhrzeigersinn."""
    if n_b == 1:
        return [(0.0, 0.0)]
    rad = d / (2.0 * math.sin(math.pi / n_b))
    anf = 0.5 * math.pi if n_b == 3 else 0.25 * math.pi
    return [(rad * math.cos(anf + 2.0 * math.pi * k / n_b), rad * math.sin(anf + 2.0 * math.pi * k / n_b))
            for k in range(n_b)]


def mittlerer_abstand(gb):
    paare = [math.hypot(a["X"] - b["X"], a["Y"] - b["Y"]) for i, a in enumerate(gb) for b in gb[i + 1:]]
    return sum(paare) / len(paare) if paare else None


def verschmelzung_zeit(ts, ns, qb, q0):
    """Erste Analyse mit weniger Gebieten als zuvor, waehrend Q_box >= 0,9 Q_box(0) (kein Verlust in die Randschicht)."""
    for i in range(1, len(ns)):
        if ns[i] < ns[i - 1] and qb[i] >= 0.9 * q0:
            return ts[i]
    return None


def ganz_verschmolzen(ts, ns, qb, q0):
    """Erste Analyse mit genau einem Gebiet, nachdem es mehrere gab, waehrend Q_box >= 0,9 Q_box(0)."""
    vorher = False
    for i in range(len(ns)):
        if ns[i] >= 2:
            vorher = True
        elif ns[i] == 1 and vorher and qb[i] >= 0.9 * q0:
            return ts[i]
    return None


def test_vielzeller(out, rauch, stufen, args):
    start = jetzt()
    print(f"Karte 4 Vielzeller Start {start} auf {geraet_name()}", flush=True)
    dauer, notizen = {}, []
    t0 = uhr()
    prof = profile_holen([(T4_W2, 0)])
    dauer["schiessen_s"] = uhr() - t0
    pr = prof[(T4_W2, 0)]
    if not pr["gueltig"]:
        raise SystemExit("Profil omega2 0.70 ungueltig: Karte 4 entfaellt")
    d_seite = 2.0 * pr["R_halb"] + T4_LUECKE
    t_end = T4_T * (RAUCH_FAKTOR if rauch else 1.0)
    alle = int(round(ANALYSE_DT / T_MEAS))
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [l for l in T4_LAEUFE if stufe == "grob" or l[0] in T4_FEIN]
        g = Gitter(L_STD, dx)
        psis, vels = [], []
        for name, n_b, phasen in laeufe:
            p_ = torch.zeros((1, g.n, g.n), dtype=C128, device=DEV)
            v_ = torch.zeros_like(p_)
            for (x0, y0), ph in zip(vieleck(n_b, d_seite), phasen):
                a, b_ = ball_feld(g, pr, 0, x0, y0, ph)
                p_, v_ = p_ + a, v_ + b_
            psis.append(p_)
            vels.append(v_)
        psi = torch.cat(psis).contiguous()
        vel = torch.cat(vels).contiguous()
        t0 = uhr()
        t, daten, verlauf = lauf_standard(g, psi, vel, dt, t_end)
        dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
        for b, (name, n_b, phasen) in enumerate(laeufe):
            ts = [tt for tt, _ in verlauf[b]]
            ns = [len(gb) for _, gb in verlauf[b]]
            qb = [daten[i * alle, b, 0].item() for i in range(len(ts))]
            q0 = qb[0]
            abst = [mittlerer_abstand(gb) if len(gb) == n_b else None for _, gb in verlauf[b]]
            d0 = abst[0] if abst[0] is not None else d_seite
            t_v = verschmelzung_zeit(ts, ns, qb, q0)
            if n_b == 1:
                klasse = "kontrolle ruhig" if max(ns) == 1 and min(ns) == 1 else "kontrolle UNRUHIG"
            elif ns[-1] == 1 and t_v is not None:
                klasse = "verschmolzen"
            elif all(n == n_b for n in ns) and all(a is not None and 0.85 * d0 <= a <= 1.15 * d0 for a in abst):
                klasse = "zusammen"
            elif t_v is None and any(a is not None and a >= 1.3 * d0 for a in abst):
                klasse = "auseinander"
            else:
                klasse = "teilweise"
            zeile = {"lauf": name, "n_baelle": n_b, "phasen": list(phasen), "stufe": stufe, "klasse": klasse,
                     "n_start": ns[0], "startzerlegung_ok": ns[0] == n_b,
                     "t_erste_verschmelzung": t_v, "n_ende": ns[-1], "abstand_start": d0,
                     "abstand_max": max((a for a in abst if a is not None), default=None),
                     "gebiete_ende": [gebiet_kurz(d) for d in verlauf[b][-1][1]], **erhaltung(t, daten, b),
                     "gebiete": verlauf_kurz(verlauf[b])}
            ergebnis.setdefault(stufe, []).append(zeile)
        zeitreihen[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "laeufe": [l[0] for l in laeufe],
                             "spalten": ["Q_box", "E_box", "J_box", "S_max"]}
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn = {"klassen": {n: z["klasse"] for n, z in grob.items()},
            "stabiler_verbund_gefunden": any(z["klasse"] == "zusammen" for z in grob.values())}
    if "fein" in ergebnis:
        l3 = []
        for zf in ergebnis["fein"]:
            zg = grob.get(zf["lauf"])
            if not zg:
                continue
            ok = zf["klasse"] == zg["klasse"] and (
                zg["t_erste_verschmelzung"] is None or (zf["t_erste_verschmelzung"] is not None and abs(
                    zf["t_erste_verschmelzung"] - zg["t_erste_verschmelzung"]) <= max(0.2 * zg["t_erste_verschmelzung"],
                                                                                     10.0)))
            l3.append({"lauf": zf["lauf"], "bestanden": ok})
        kenn["L3"] = {"laeufe": l3, "bestanden": all(z["bestanden"] for z in l3) if l3 else None}
    ausgabe = {"test": "vielzeller", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "parameter": {"T": T4_T, "omega2": T4_W2,
               "luecke": T4_LUECKE, "seite": d_seite, "L": L_STD, "stufen": STUFEN},
               "profil": profil_info(pr), "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Karte 4 Vielzeller (Bio 24)", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append(f"Ball omega2 {T4_W2}: Q {pr['Q']:.3f}, R_halb {pr['R_halb']:.3f}; Seitenlaenge {d_seite:.3f}")
    text.append("Stufe Lauf | Klasse | t erste Verschmelzung | n Ende | Abstand Start/max | Windungen Ende | Q-Verlust")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            am = f"{z['abstand_max']:.2f}" if z["abstand_max"] is not None else "-"
            text.append(f"  {stufe} {z['lauf']} | {z['klasse']} | {z['t_erste_verschmelzung']} | {z['n_ende']} | "
                        f"{z['abstand_start']:.2f}/{am} | {[d.get('windung') for d in z['gebiete_ende']]} | "
                        f"{z['Q_box_verlust']:.1e}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "vielzeller", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- Karte 5: Groessengrenze (Bio 28)

def test_groesse(out, rauch, stufen, args):
    start = jetzt()
    print(f"Karte 5 Groessengrenze Start {start} auf {geraet_name()}", flush=True)
    dauer, notizen = {}, []
    t0 = uhr()
    prof = profile_holen([(w2, m) for _, w2, _ in T5_LAEUFE for m in (0, 1)])
    dauer["schiessen_s"] = uhr() - t0
    t_end = T5_T * (RAUCH_FAKTOR if rauch else 1.0)
    alle = int(round(ANALYSE_DT / T_MEAS))
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = auswahl(T5_LAEUFE, stufe, T5_FEIN, prof, lambda l: [(l[1], 0), (l[1], 1)], notizen)
        if not laeufe:
            continue
        g = Gitter(L_STD, dx)
        psis, vels, abst = [], [], []
        for name, w2, k in laeufe:
            p1, p0 = prof[(w2, 1)], prof[(w2, 0)]
            dd = p1["R_halb"] + p0["R_halb"] + T5_LUECKE
            abst.append(dd)
            p_, v_ = ball_feld(g, p1, 1)
            for x0, ph in ((dd, 0.0), (-dd, math.pi))[:k]:
                a, b_ = ball_feld(g, p0, 0, x0, 0.0, ph)
                p_, v_ = p_ + a, v_ + b_
            psis.append(p_)
            vels.append(v_)
        psi = torch.cat(psis).contiguous()
        vel = torch.cat(vels).contiguous()
        t0 = uhr()
        t, daten, verlauf = lauf_standard(g, psi, vel, dt, t_end)
        dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
        for b, (name, w2, k) in enumerate(laeufe):
            ts = [tt for tt, _ in verlauf[b]]
            ns = [len(gb) for _, gb in verlauf[b]]
            qb = [daten[i * alle, b, 0].item() for i in range(len(ts))]
            t_v = ganz_verschmolzen(ts, ns, qb, qb[0]) if k > 0 else None
            i_v = ts.index(t_v) if t_v is not None else 0
            t_neu = erste_dauerhaft(ts[i_v:], [n >= 2 for n in ns[i_v:]]) if (k == 0 or t_v is not None) else None
            wind = [gb[0].get("windung") if gb else None for _, gb in verlauf[b]]
            zeile = {"lauf": name, "omega2": w2, "nachbarn": k, "stufe": stufe, "abstand": abst[b],
                     "Q_m1": prof[(w2, 1)]["Q"], "Q_nachbar": prof[(w2, 0)]["Q"],
                     "t_verschmolzen": t_v, "t_teilung_danach": t_neu, "n_ende": ns[-1],
                     "windung_groesstes_ende": wind[-1],
                     "windung_groesstes_verlauf": sorted(set(w for w in wind if w is not None)),
                     "J_zu_Q_start": (daten[0, b, 2] / daten[0, b, 0]).item(),
                     "gebiete_ende": [gebiet_kurz(d) for d in verlauf[b][-1][1]], **erhaltung(t, daten, b),
                     "gebiete": verlauf_kurz(verlauf[b])}
            ergebnis.setdefault(stufe, []).append(zeile)
        zeitreihen[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "laeufe": [l[0] for l in laeufe],
                             "spalten": ["Q_box", "E_box", "J_box", "S_max"]}
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn = {}
    gefuettert = [z for z in grob.values() if z["nachbarn"] > 0]
    if gefuettert:
        kenn["verschmolzen"] = {z["lauf"]: z["t_verschmolzen"] for z in gefuettert}
        kenn["teilung_nach_wachstum"] = {z["lauf"]: z["t_teilung_danach"] for z in gefuettert}
        kenn["windung_behalten"] = {z["lauf"]: z["windung_groesstes_ende"] == 1 for z in gefuettert}
        kenn["bio28"] = ("Groessengrenze gesehen: gewachsener Ball teilt sich"
                         if any(z["t_teilung_danach"] is not None for z in gefuettert if z["t_verschmolzen"])
                         else "keine Groessengrenze im Fenster: gewachsene Baelle teilen sich nicht")
    kenn["kontrollen_ohne_nachbarn"] = {z["lauf"]: z["t_teilung_danach"] for z in grob.values() if z["nachbarn"] == 0}
    if "fein" in ergebnis:
        l3 = []
        for zf in ergebnis["fein"]:
            zg = grob.get(zf["lauf"])
            if not zg:
                continue
            ok = ((zf["t_verschmolzen"] is None) == (zg["t_verschmolzen"] is None)
                  and (zf["t_teilung_danach"] is None) == (zg["t_teilung_danach"] is None)
                  and zf["windung_groesstes_ende"] == zg["windung_groesstes_ende"])
            l3.append({"lauf": zf["lauf"], "bestanden": ok})
        kenn["L3"] = {"laeufe": l3, "bestanden": all(z["bestanden"] for z in l3) if l3 else None}
    ausgabe = {"test": "groesse", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "notizen": notizen,
               "parameter": {"T": T5_T, "luecke": T5_LUECKE, "L": L_STD, "stufen": STUFEN},
               "profile": [profil_info(prof[(w2, m)]) for w2 in (0.60, 0.75) for m in (0, 1)],
               "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Karte 5 Groessengrenze (Bio 28, Futter = gleichphasige Nachbarn)", start, rauch)]
    text += laufzeit_text(dauer, rauch) + notizen
    text.append("Stufe Lauf | Q_m1 + k Q_0 | J/Q | t verschmolzen | Windung groesstes (Ende; je gesehen) | "
                "t Teilung danach | n Ende | Q-Verlust")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            text.append(f"  {stufe} {z['lauf']} | {z['Q_m1']:.1f} + {z['nachbarn']} x {z['Q_nachbar']:.1f} | "
                        f"{z['J_zu_Q_start']:.3f} | {z['t_verschmolzen']} | {z['windung_groesstes_ende']}; "
                        f"{z['windung_groesstes_verlauf']} | {z['t_teilung_danach']} | {z['n_ende']} | "
                        f"{z['Q_box_verlust']:.1e}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "groesse", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- Karte 6: Selbstreplikation (Bio 49)

def test_replikation(out, rauch, stufen, args):
    """Nur sinnvoll, wenn "teilung" eine Teilung zeigte (PLAN.md). --tochter-m: gemessene Windung der Toechter,
    --omega2: omega^2 des geteilten m = 2-Balls (Naeherung: Toechter mit demselben omega)."""
    start = jetzt()
    w_t, w2 = args.tochter_m, args.omega2
    print(f"Karte 6 Replikation Start {start}: Toechter m = {w_t}, omega2 {w2}", flush=True)
    dauer, notizen = {}, []
    t0 = uhr()
    prof = profile_holen([(w2, w_t)])
    dauer["schiessen_s"] = uhr() - t0
    pr = prof[(w2, w_t)]
    if not pr["gueltig"]:
        raise SystemExit(f"Profil omega2 {w2}, m {w_t} ungueltig: Karte 6 entfaellt")
    dd = 2.0 * pr["R_halb"] + T6_LUECKE
    q_b, e_b = pr["Q"], pr["E"]
    geschw = {}
    for name, faktor in T6_LAEUFE:
        if faktor is None:
            continue
        gv = max(faktor * 2.0 * q_b - 2.0 * w_t * q_b, 0.0) / (dd * e_b)     # J_Bahn = D gamma E v
        geschw[name] = gv / math.sqrt(1.0 + gv * gv)
    t_end = T6_T * (RAUCH_FAKTOR if rauch else 1.0)
    alle = int(round(ANALYSE_DT / T_MEAS))
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        laeufe = [l for l in T6_LAEUFE if stufe == "grob" or l[0] in T6_FEIN]
        g = Gitter(L_STD, dx)
        psis, vels = [], []
        for name, faktor in laeufe:
            if faktor is None:
                p_, v_ = ball_feld(g, pr, w_t)
            else:
                v = geschw[name]
                a1, b1 = ball_bewegt(g, pr, w_t, -0.5 * dd, 0.0, v, -0.5 * math.pi, 0.0)
                a2, b2 = ball_bewegt(g, pr, w_t, 0.5 * dd, 0.0, v, 0.5 * math.pi, math.pi * w_t)
                p_, v_ = a1 + a2, b1 + b2
            psis.append(p_)
            vels.append(v_)
        psi = torch.cat(psis).contiguous()
        vel = torch.cat(vels).contiguous()
        t0 = uhr()
        t, daten, verlauf = lauf_standard(g, psi, vel, dt, t_end)
        dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
        for b, (name, faktor) in enumerate(laeufe):
            ts = [tt for tt, _ in verlauf[b]]
            ns = [len(gb) for _, gb in verlauf[b]]
            qb = [daten[i * alle, b, 0].item() for i in range(len(ts))]
            t_v = ganz_verschmolzen(ts, ns, qb, qb[0]) if faktor is not None else None
            i_v = ts.index(t_v) if t_v is not None else 0
            w_eins = [gb[0].get("windung") for (_, gb), n in zip(verlauf[b][i_v:], ns[i_v:]) if n == 1]
            gross = [[d["Q"] >= 0.2 * qb[0] for d in gb] for _, gb in verlauf[b]]
            t_neu = (erste_dauerhaft(ts[i_v:], [n >= 2 and sum(gr) >= 2 for n, gr in zip(ns[i_v:], gross[i_v:])])
                     if t_v is not None or faktor is None else None)
            zeile = {"lauf": name, "stufe": stufe, "v": geschw.get(name, 0.0), "abstand": dd,
                     "J_zu_Q_start": (daten[0, b, 2] / daten[0, b, 0]).item(), "t_verschmolzen": t_v,
                     "windungen_als_ein_gebiet": sorted(set(w for w in w_eins if w is not None)),
                     "m2_erreicht": 2 in w_eins, "t_neue_teilung": t_neu, "n_ende": ns[-1],
                     "gebiete_ende": [gebiet_kurz(d) for d in verlauf[b][-1][1]], **erhaltung(t, daten, b),
                     "gebiete": verlauf_kurz(verlauf[b])}
            ergebnis.setdefault(stufe, []).append(zeile)
        zeitreihen[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "laeufe": [l[0] for l in laeufe],
                             "spalten": ["Q_box", "E_box", "J_box", "S_max"]}
    grob = {z["lauf"]: z for z in ergebnis.get("grob", [])}
    kenn = {"zyklus": {n: z["m2_erreicht"] and z["t_neue_teilung"] is not None for n, z in grob.items()
                       if n != "einzel"},
            "m2_erreicht": {n: z["m2_erreicht"] for n, z in grob.items() if n != "einzel"}}
    if "einzel" in grob:
        kenn["gegenprobe_einzel_ruhig"] = grob["einzel"]["t_neue_teilung"] is None
    if "fein" in ergebnis:
        l3 = []
        for zf in ergebnis["fein"]:
            zg = grob.get(zf["lauf"])
            if zg:
                ok = (zf["m2_erreicht"] == zg["m2_erreicht"]
                      and (zf["t_neue_teilung"] is None) == (zg["t_neue_teilung"] is None))
                l3.append({"lauf": zf["lauf"], "bestanden": ok})
        kenn["L3"] = {"laeufe": l3, "bestanden": all(z["bestanden"] for z in l3) if l3 else None}
    ausgabe = {"test": "replikation", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(), "notizen": notizen,
               "parameter": {"T": T6_T, "tochter_m": w_t, "omega2": w2, "abstand": dd, "v": geschw, "L": L_STD,
                             "stufen": STUFEN}, "profil": profil_info(pr), "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf(f"Karte 6 Selbstreplikation (Bio 49), Toechter m = {w_t}, omega2 {w2}", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append("Stufe Lauf | v | J/Q | t verschmolzen | Windungen als ein Gebiet | m = 2 erreicht | t neue Teilung | "
                "n Ende")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            text.append(f"  {stufe} {z['lauf']} | {z['v']:.4f} | {z['J_zu_Q_start']:.3f} | {z['t_verschmolzen']} | "
                        f"{z['windungen_als_ein_gebiet']} | {z['m2_erreicht']} | {z['t_neue_teilung']} | {z['n_ende']}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "replikation", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- Karte 7: Endzustand nach Rauschstart (Chemie 12)

def rauschfeld(g, seed):
    """Zufallsfeld und -geschwindigkeit aus den Moden 0 < |k| <= T7_KC der Box, Feldamplitude je Mode ~ 1/sqrt(1 + k^2),
    Geschwindigkeit ~ 1 (Gleichverteilung der Modenenergie). Die Moden haengen nur von L ab, nicht von dx: grob und fein
    beginnen mit demselben Feld."""
    kk_max = int(math.floor(T7_KC * g.L / math.pi))
    gen = torch.Generator(device=DEV)
    gen.manual_seed(seed)
    zahl = 2 * kk_max + 1
    a = torch.randn((4, zahl, zahl), generator=gen, dtype=F64, device=DEV)
    idx = torch.arange(-kk_max, kk_max + 1, device=DEV)
    kk = (math.pi / g.L) * idx.to(F64)
    k2 = kk.view(-1, 1) ** 2 + kk.view(1, -1) ** 2
    maske = ((k2 <= T7_KC * T7_KC) & (k2 > 0.0)).to(F64)
    wk = torch.sqrt(1.0 + k2)
    ii = (idx % g.n).view(-1, 1)
    jj = (idx % g.n).view(1, -1)
    fk = torch.zeros((g.n, g.n), dtype=C128, device=DEV)
    vk = torch.zeros((g.n, g.n), dtype=C128, device=DEV)
    fk[ii, jj] = torch.complex(a[0], a[1]) * maske / wk
    vk[ii, jj] = torch.complex(a[2], a[3]) * maske
    eta = torch.fft.ifft2(fk) * (g.n * g.n)
    eta_t = torch.fft.ifft2(vk) * (g.n * g.n)
    return eta.unsqueeze(0), eta_t.unsqueeze(0)


def freie_energie(g, eta, eta_t):
    """Mittlere freie quadratische Energiedichte |eta_t|^2 + |grad eta|^2 + |eta|^2."""
    ph = torch.fft.fft2(eta)
    gx = torch.fft.ifft2(ph * (1j * g.kx))
    gy = torch.fft.ifft2(ph * (1j * g.ky))
    return (eta_t.abs() ** 2 + gx.abs() ** 2 + gy.abs() ** 2 + eta.abs() ** 2).mean().item()


def phase_klasse(f_geb, phi, geb):
    """Vorab festgelegt (PLAN.md 8.2): G Gas, M gemischt, K Kondensat, N Netz, T Tropfen."""
    if f_geb < 0.2:
        return "G"
    if f_geb < 0.5:
        return "M"
    if geb and any(d["spannt_x"] or d["spannt_y"] for d in geb):
        gr = geb[0]
        return "K" if (gr["spannt_x"] and gr["spannt_y"] and phi >= 0.7) else "N"
    return "T"


def test_phasen(out, rauch, stufen, args):
    start = jetzt()
    print(f"Karte 7 Phasen Start {start} auf {geraet_name()}", flush=True)
    dauer = {}
    t_end = T7_T * (RAUCH_FAKTOR if rauch else 1.0)
    alle = int(round(T7_ANALYSE / T_MEAS))
    zellen = [(s0, ep) for s0 in T7_S0 for ep in T7_EPS]
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN:
        if stufe not in stufen:
            continue
        auswahl7 = zellen if stufe == "grob" else [z for z in zellen if z in T7_FEIN]
        g = Gitter(T7_L, dx, schwamm=False)
        psis, vels, vorab = [], [], []
        for s0, ep in auswahl7:
            mu = math.sqrt(1.0 - 2.0 * s0 + 1.5 * s0 * s0)
            eta, eta_t = rauschfeld(g, T7_SEED + zellen.index((s0, ep)))
            q0 = 2.0 * mu * s0
            amp = math.sqrt(ep * T7_BINDUNG * q0 / freie_energie(g, eta, eta_t))
            p_ = math.sqrt(s0) + amp * eta
            v_ = -1j * mu * math.sqrt(s0) + amp * eta_t
            psis.append(p_)
            vels.append(v_)
            vorab.append({"S0": s0, "eps": ep, "mu": mu, "amplitude": amp})
        psi = torch.cat(psis).contiguous()
        vel = torch.cat(vels).contiguous()
        B = psi.shape[0]
        s_i, rho_i, e_i, _, _, _ = dichten(g, psi, vel)
        q_i = rho_i.sum((1, 2)) * g.dA
        e_ges = e_i.sum((1, 2)) * g.dA
        for b in range(B):
            eq = (e_ges[b] / q_i[b]).item()
            vorab[b]["E_zu_Q"] = eq
            vorab[b]["f_geb_min"] = max(0.0, (1.0 - eq) / T7_BINDUNG)       # Schranke (PLAN.md 8.3)
        q_min = (T7_QMIN * q_i).tolist()
        verlauf = [[] for _ in range(B)]
        schnapp = {}
        zaehler = [0]
        n_mess = int(round(t_end / T_MEAS))

        def messen(psi, vel):
            s = psi.real ** 2 + psi.imag ** 2
            rho = 2.0 * (psi * vel.conj()).imag
            if zaehler[0] % alle == 0:
                dicht = dichten(g, psi, vel)
                sb = unschaerfe(g, s)
                om = unschaerfe(g, rho) / (2.0 * sb.clamp(min=1e-12))
                maske = (sb >= T7_S_DICHT) & (om > T7_OM_LO) & (om < T7_OM_HI)
                qt = rho.sum((1, 2))
                f_geb = ((rho * maske).sum((1, 2)) / qt).tolist()
                phi = maske.to(F64).mean((1, 2)).tolist()
                kontrast = (sb.std((1, 2)) / sb.mean((1, 2))).tolist()
                koh = (psi.sum((1, 2)).abs() ** 2 / (g.n * g.n * s.sum((1, 2)))).tolist()
                gebiete = analyse(g, psi, dicht, maske, q_min, windung=False)
                for b in range(B):
                    verlauf[b].append({"t": zaehler[0] * T_MEAS, "f_geb": f_geb[b], "phi": phi[b],
                                       "kontrast": kontrast[b], "koharenz": koh[b], "n_geb": len(gebiete[b]),
                                       "gebiete": [{k: d[k] for k in ("Q", "flaeche", "spannt_x", "spannt_y")}
                                                   for d in gebiete[b][:8]],
                                       "klasse": phase_klasse(f_geb[b], phi[b], gebiete[b])})
            if zaehler[0] in (n_mess // 2, n_mess):
                schnapp[zaehler[0] * T_MEAS] = s.to(torch.float32).cpu()
            zaehler[0] += 1
            return torch.stack([rho.sum((1, 2)) * g.dA, s.amax((1, 2))], dim=1)

        t0 = uhr()
        t, daten = entwickeln(g, psi, vel, dt, t_end, messen)
        dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
        s_e, rho_e, e_e, _, _, _ = dichten(g, psi, vel)
        e_ende = e_e.sum((1, 2)) * g.dA
        for b in range(B):
            vl = verlauf[b]
            letzte = vl[-5:]
            f_m = sum(v["f_geb"] for v in letzte) / len(letzte)
            phi_m = sum(v["phi"] for v in letzte) / len(letzte)
            kl_ende = vl[-1]["klasse"]
            i_h = min(range(len(vl)), key=lambda i: abs(vl[i]["t"] - 0.5 * vl[-1]["t"]))
            zeile = {**vorab[b], "stufe": stufe, "klasse_ende": kl_ende, "klasse_haelfte": vl[i_h]["klasse"],
                     "stationaer": kl_ende == vl[i_h]["klasse"], "f_geb_ende": f_m, "phi_ende": phi_m,
                     "n_gebiete_ende": vl[-1]["n_geb"], "kontrast_ende": vl[-1]["kontrast"],
                     "koharenz_ende": vl[-1]["koharenz"],
                     "schranke_erfuellt": f_m >= vorab[b]["f_geb_min"] - 0.05,
                     "Q_drift": (1.0 - daten[-1, b, 0] / daten[0, b, 0]).item(),
                     "E_drift": (1.0 - e_ende[b] / e_ges[b]).item(), "verlauf": vl}
            ergebnis.setdefault(stufe, []).append(zeile)
        zeitreihen[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "zellen": auswahl7, "spalten": ["Q_box", "S_max"],
                             "S_schnappschuss": schnapp}
    kenn = {}
    grob = ergebnis.get("grob", [])
    if grob:
        kenn["diagramm"] = {f"S0={z['S0']} eps={z['eps']}": z["klasse_ende"] for z in grob}
        kenn["schranke_alle_erfuellt"] = all(z["schranke_erfuellt"] for z in grob)
        kenn["stationaer_alle"] = all(z["stationaer"] for z in grob)
    if "fein" in ergebnis and grob:
        l3 = []
        for zf in ergebnis["fein"]:
            zg = [z for z in grob if z["S0"] == zf["S0"] and z["eps"] == zf["eps"]]
            if zg:
                l3.append({"zelle": [zf["S0"], zf["eps"]], "bestanden": zf["klasse_ende"] == zg[0]["klasse_ende"],
                           "f_geb_aenderung": abs(zf["f_geb_ende"] - zg[0]["f_geb_ende"])})
        kenn["L3"] = {"zellen": l3, "bestanden": all(z["bestanden"] for z in l3) if l3 else None}
    ausgabe = {"test": "phasen", "start": start, "ende": jetzt(), "rauch": rauch, "dauer_s": dauer,
               "geraet": geraet_name(),
               "parameter": {"T": T7_T, "L": T7_L, "kc": T7_KC, "S0": T7_S0, "eps": T7_EPS, "seed": T7_SEED,
                             "S_dicht": T7_S_DICHT, "omega_fenster": [T7_OM_LO, T7_OM_HI], "stufen": STUFEN},
               "ergebnis": ergebnis, "kennzahlen": kenn}
    text = [kopf("Karte 7 Endzustand nach Rauschstart (Chemie 12), geschlossene Box", start, rauch)]
    text += laufzeit_text(dauer, rauch)
    text.append("Stufe S0 eps | E/Q | f_geb_min | Klasse T/2 -> T | f_geb | phi | n Gebiete | Kontrast | Kohaerenz | "
                "Schranke | Q/E-Drift")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            text.append(f"  {stufe} {z['S0']} {z['eps']} | {z['E_zu_Q']:.4f} | {z['f_geb_min']:.3f} | "
                        f"{z['klasse_haelfte']} -> {z['klasse_ende']} | {z['f_geb_ende']:.3f} | {z['phi_ende']:.3f} | "
                        f"{z['n_gebiete_ende']} | {z['kontrast_ende']:.3f} | {z['koharenz_ende']:.3f} | "
                        f"{'ja' if z['schranke_erfuellt'] else 'NEIN'} | {z['Q_drift']:.1e}/{z['E_drift']:.1e}")
    text.append("Kennzahlen: " + json.dumps(kenn))
    schreiben(out, "phasen", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- Aufruf

KARTEN = {"profile": test_profile, "teilung": test_teilung, "schale": test_schale, "polaritaet": test_polaritaet,
          "vielzeller": test_vielzeller, "groesse": test_groesse, "replikation": test_replikation,
          "phasen": test_phasen}


def main():
    global DEV, N_KAND, STUFEN, RAUCH_FAKTOR
    ap = argparse.ArgumentParser(description="Runde 5, Paket 2D-A (Zelle): sieben Q-Ball-Karten in 2D")
    ap.add_argument("karte", choices=list(KARTEN) + ["alle"])
    ap.add_argument("--rauch", action="store_true", help="Laufzeiten x 0,05; nur Durchlauf und Hochrechnung")
    ap.add_argument("--mini", action="store_true",
                    help="nur mit --rauch: Formprobe in Sekunden (256 Kandidaten, dx 0,6/0,4, Laufzeiten x 0,02)")
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda",
                    help="cpu nur fuer die Formprobe mit --rauch --mini, nie fuer Messlaeufe")
    ap.add_argument("--stufe", choices=["grob", "fein", "beide"], default="beide")
    ap.add_argument("--out", default=None)
    ap.add_argument("--tochter-m", type=int, default=0, choices=[0, 1], help="nur replikation: Windung der Toechter")
    ap.add_argument("--omega2", type=float, default=0.80, help="nur replikation: omega^2 des geteilten Balls")
    ap.add_argument("--teil", choices=["haupt", "gegen"], default="haupt", help="G1-03: Hauptlauf m = 2 oder Gegenprobe m = 0")
    ap.add_argument("--t-end", type=float, default=T1_T, help="G1-03: Laufzeit T (Voreinstellung 1200)")
    args = ap.parse_args()
    if args.geraet == "cpu" and not (args.rauch and args.mini):
        raise SystemExit("--geraet cpu nur zusammen mit --rauch --mini (Formprobe); Messlaeufe nur auf CUDA.")
    if args.mini and not args.rauch:
        raise SystemExit("--mini nur zusammen mit --rauch.")
    DEV = torch.device(args.geraet)
    if DEV.type == "cuda" and not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    if args.mini:
        N_KAND = 256
        STUFEN = (("grob", 0.6, 0.1), ("fein", 0.4, 0.05))
        RAUCH_FAKTOR = 0.02
    if args.karte == "alle" and not args.rauch:
        raise SystemExit("'alle' nur mit --rauch (sonst ueber 10 min).")
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "rauchtest" if args.rauch else "ausgabe")
    stufen = ("grob", "fein") if args.stufe == "beide" else (args.stufe,)
    namen = list(KARTEN) if args.karte == "alle" else [args.karte]
    fehler = []
    for name in namen:
        if len(namen) == 1:
            KARTEN[name](out, args.rauch, stufen, args)
            continue
        try:                                   # "alle": ein Fehler stoppt die uebrigen Karten nicht
            KARTEN[name](out, args.rauch, stufen, args)
        except (Exception, SystemExit) as exc:
            traceback.print_exc()
            print(f"FEHLER in Karte {name}: {exc!r}", flush=True)
            fehler.append(name)
    if fehler:
        raise SystemExit(f"Karten mit Fehler: {fehler}")


if __name__ == "__main__":
    main()
