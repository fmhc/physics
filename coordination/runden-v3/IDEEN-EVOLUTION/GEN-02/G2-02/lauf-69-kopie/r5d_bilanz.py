#!/usr/bin/env python3
"""Runde 5 (runden-v3), Paket R5-D: 1D mit zwei komplexen Feldern psi und chi fuer sechs Q-Ball-Ideen.

Explorativ. Ungetestet abgegeben (Interpreterverbot auf dem Laptop); Aufrufe, Laufzeiten, Vorhersagen, Gegenproben und
Latten stehen in PLAN.md daneben. float64 bzw. complex128 auf CUDA oder CPU (--geraet cuda|cpu).

Modell (psi wie in RUNDE-02/tests1d/tests1d.py, chi neu):
  L = |psi_t|^2 + |chi_t|^2 - |psi_x|^2 - |chi_x|^2 - V
  V = U(S) + mc2 C + g4 C^2 + kc (-C^2 + C^3/2) + C (lam S + lam2 S^2) + eps (conj(psi) chi + conj(chi) psi)
  U(S) = S - S^2 + S^3/2,  S = |psi|^2,  C = |chi|^2
Rollen von chi (je Unterbefehl eine):
  - Kanal (kc = mc2 = m^2, g4 = 0): Kopie von psi mit Masse m. Ein chi-Ball ist f(m x) exp(-i m omega t) mit dem
    psi-Profil f bei omega: gleiche Ladung und Hoehe, m-mal schmaler, m-mal mehr Energie.
  - Medium (kc = 0, g4 > 0): defokussierend, U_chi'' = 2 g4 > 0; jede homogene Dichte ist linear stabil (PLAN.md).
  - frei (kc = g4 = 0): nur Masse sqrt(mc2).
Kopplungen:
  - lam, lam2: Dichtekopplung; Q_psi und Q_chi bleiben einzeln erhalten.
  - eps: Austausch (Rabi-Mischung); erhalten bleibt nur Q_psi + Q_chi. Das Vakuum ist nur fuer mc2 >= eps^2 stabil
    (Massenmatrix [[1, eps], [eps, mc2]]); bei mc2 = eps^2 ist eine Eigenmode genau masselos.
Bewegungsgleichungen:
  psi_tt = psi_xx - [U'(S) + C (lam + 2 lam2 S)] psi - eps chi
  chi_tt = chi_xx - [mc2 + 2 g4 C + kc (-2 C + 1,5 C^2) + lam S + lam2 S^2] chi - eps psi
Ladungsdichte je Feld rho = 2 Im(f conj(f_t)); Energiedichte |psi_t|^2 + |chi_t|^2 + |psi_x|^2 + |chi_x|^2 + V.

Aus tests1d.py uebernommen: Gitter (dx = 0,1, Box [-150, 150], x = 0 auf einem Gitterpunkt), Velocity-Verlet mit
dt = 0,05, feine Stufe dx/2 und dt/2 (Latte L3), quadratische Daempfungsschicht (sigma0 = 1, ab |x| = 110), Anker-Formeln
(Q, E, FWHM, Umkehrung Q -> omega), l3, Lorentz-Boost eines Balls. Geaendert: zwei Felder; statt der Schiessbahn das
geschlossene 1D-Profil f^2 = 2 a0/(1 + b0 cosh(2 sqrt(a0) x)) (profil_anker in tests1d.py, dort gegen das Schiessen auf
1,5e-10 geprueft; in 1D ist Schiessen deshalb unnoetig); fuer "kreuzen" eine periodische Box ohne Daempfung.

Aufruf:  python r5d.py <unterbefehl> [--geraet cuda|cpu] [--out ORDNER]
  rauch          alle sechs Unterbefehle mit Laufzeiten x 0,05 (prueft nur, ob alles durchlaeuft)
  zellkern       Bio 8      psi-Ball und chi-Ball (Masse m) am selben Ort, lam = -0,4 / 0 / +0,4
  raeuber        Bio 15     psi- und chi-Ball am selben Ort mit Austausch eps; Bestaende Q_psi(t), Q_chi(t)
  mitochondrium  Bio 35     kleiner schwerer chi-Ball in grossem psi-Ball; gefangen oder entkommen
  altern         Bio 48     psi-Ball mit Austausch in einen masselosen Kanal; Verdampfungsrate gegen Groesse
  tensid         Chemie 17  chi an der Wand eines grossen psi-Balls (Kopplung -a S (1 - S) C); Belegung, Wand, Energie
  kreuzen        Wellen 10  psi-Ball in stroemendem, stabilem chi-Medium (1D-Baustein: Kraft gegen Stroemung)
--geraet cuda ohne sichtbare Karte bricht ab (kein stiller CPU-Ausweg); --geraet cpu rechnet mit einem Thread.
Ausgabe im --out-Ordner: r5d_<unterbefehl>_bericht.txt, _ergebnis.json, _reihen.pt; nach jedem Test neu geschrieben.
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
C128 = torch.complex128
PI = math.pi
DEV = torch.device("cpu")          # in main() nach --geraet gesetzt

# ---- aus tests1d.py (RUNDE-02) unveraendert ----
SIGMA0 = 1.0             # Daempfung am Rand
DX, DT = 0.1, 0.05       # grobe Aufloesung; die feine halbiert beide
L_BOX = 150.0            # Box [-L, L]
X_SPONGE = 110.0         # Daempfungsschicht fuer |x| > X_SPONGE, 40 breit (nur offene Box)
FEIN = 0.5               # feine Stufe: dx und dt mal FEIN (Latte L3, enthaelt den halben Zeitschritt)
# ---- neu ----
SPEICHER_GB = 1.5        # Obergrenze fuer den Torch-Speicher auf der Karte (Vorgabe Runde 5)
RAUCH_FAKTOR = 0.05      # Rauchtest: alle Laufzeiten mal 0,05

# ---- zellkern (Bio 8) ----
ZK_W2 = 0.6                   # omega^2 beider Baelle relativ zur eigenen Masse (chi: omega_chi = m sqrt(0,6))
ZK_M = [1.0, 1.5, 2.5]        # Masse von chi; m = 1 ist die Gegenprobe "gleiche Massen"
ZK_LAM = [-0.4, 0.0, 0.4]     # lam = 0 ist die Gegenprobe "ohne Kopplung"
ZK_D0 = 0.5                   # chi-Ball um 0,5 versetzt: bricht die Spiegelsymmetrie
ZK_T, ZK_MESS = 400.0, 0.5
ZK_FENSTER = 60.0
ZK_SPALTEN = ["x_psi", "x_chi", "w_psi", "w_chi", "Q_psi", "Q_chi", "S_am_chi_rel", "C_am_psi_rel", "S_max", "C_max"]

# ---- raeuber (Bio 15) ----
RB_W2_REF = 0.7               # Gesamtladung je Einheit: 2 Q(0,7) = 4,883
RB_EPS = 0.02                 # Austausch; Vakuum stabil (mc2 = 1 > eps^2)
RB_T, RB_MESS = 500.0, 0.5
RB_FENSTER = 100.0
RB_LAEUFE = [
    {"name": "rein z0=1", "z0": 1.0, "dphi": 0.0, "kontrolle": True},
    {"name": "gleichphasig z0=0,05", "z0": 0.05, "dphi": 0.0},
    {"name": "gleichphasig z0=0,3", "z0": 0.3, "dphi": 0.0},
    {"name": "gleichphasig z0=0,6", "z0": 0.6, "dphi": 0.0},
    {"name": "gegenphasig z0=0,05", "z0": 0.05, "dphi": PI},
    {"name": "gegenphasig z0=0,3", "z0": 0.3, "dphi": PI},
    {"name": "Kontrolle eps=0", "z0": 0.3, "dphi": 0.0, "eps": 0.0, "kontrolle": True},
    {"name": "Kontrolle getrennt 40", "z0": 0.3, "dphi": 0.0, "abstand": 40.0, "kontrolle": True},
    {"name": "Box 3 Einheiten", "z0": 0.3, "dphi": 0.0, "box": [(-60.0, 0.8), (0.0, 1.0), (60.0, 1.2)]},
]
RB_SPALTEN = ["Q_psi", "Q_chi", "dphi_mitte", "S_mitte", "C_mitte"]

# ---- mitochondrium (Bio 35) ----
MT_W2_WIRT = 0.500001         # grosser psi-Ball: FWHM 10,26, Q 14,5, Plateau S ~ 1
MT_M, MT_W2_GAST = 2.0, 0.8   # kleiner schwerer chi-Ball: FWHM 2,08, Q 1,89, E 3,64
MT_LAM = [-0.3, 0.0, 0.3]
MT_V = [0.0, 0.2, 0.4]        # Startgeschwindigkeit des Gastes aus der Mitte
MT_T, MT_MESS = 400.0, 0.5
MT_FENSTER = 60.0
MT_GAST_FENSTER = 6.0
MT_SPALTEN = ["x_gast", "C_gast", "x_wirt", "R_wirt", "Q_gast", "Q_wirt", "S_max"]

# ---- altern (Bio 48) ----
AL_EPS = 0.05                 # Austausch; chi mit mc2 = eps^2: eine Eigenmode genau masselos
AL_W2 = [0.500001, 0.5001, 0.51, 0.55, 0.6, 0.7, 0.8, 0.9]
AL_MC2_SCHWER = 1.44          # Gegenprobe: Kanal mit Masse 1,2 > omega, keine Abstrahlung
AL_T, AL_MESS = 400.0, 1.0
AL_FENSTER = 40.0             # Ball-Fenster |x| < 40
AL_BOX = 100.0
AL_SPALTEN = ["Q_ball", "Q_psi_ball", "Q_box"]

# ---- tensid (Chemie 17) ----
TS_W2 = 0.500001              # grosser psi-Ball mit Plateau; Waende bei +-FWHM/2 = +-5,13
TS_OM0 = 0.95                 # Startfrequenz der chi-Pakete an den Waenden
TS_T, TS_MESS = 400.0, 0.5
TS_FENSTER = 60.0
TS_BAND = 2.0                 # Wandband: ||x| - x_Wand| < 2
TS_LAEUFE = [
    {"name": "nackt (ohne chi)", "A": 0.0},
    {"name": "chi frei, A=0,15", "A": 0.15},
    {"name": "amphiphil a=1, A=0,05", "A": 0.05, "lam": -1.0, "lam2": 1.0},
    {"name": "amphiphil a=1, A=0,15", "A": 0.15, "lam": -1.0, "lam2": 1.0},
    {"name": "amphiphil a=2, A=0,05", "A": 0.05, "lam": -2.0, "lam2": 2.0},
    {"name": "amphiphil a=2, A=0,15", "A": 0.15, "lam": -2.0, "lam2": 2.0},
    {"name": "Dichte lam=-0,5, A=0,15", "A": 0.15, "lam": -0.5, "lam2": 0.0},
    {"name": "anti a=-1, A=0,15", "A": 0.15, "lam": 1.0, "lam2": -1.0},
]
TS_SPALTEN = ["anteil_wand", "anteil_innen", "w_wand", "E", "Q_psi", "Q_chi", "N_chi", "theta_psi", "theta_chi",
              "S_max"]

# ---- kreuzen (Wellen 10) ----
KZ_C0, KZ_G4 = 0.1, 0.5       # duennes chi-Medium, U_chi = C + 0,5 C^2: defokussierend, stabil
KZ_W2 = 0.7
KZ_T, KZ_MESS = 300.0, 0.5
KZ_LAEUFE = [                 # Stroemung chi = sqrt(C0) exp(i (k x - omega t)), k = 2 pi n / 300
    {"name": "n=0 ruhend", "n": 0, "lam": 0.1},
    {"name": "n=+5", "n": 5, "lam": 0.1},
    {"name": "n=-5 Spiegel", "n": -5, "lam": 0.1},
    {"name": "n=+8", "n": 8, "lam": 0.1},
    {"name": "n=+16", "n": 16, "lam": 0.1},
    {"name": "n=+29", "n": 29, "lam": 0.1},
    {"name": "n=+16 lam=0", "n": 16, "lam": 0.0},
    {"name": "n=+16 lam=0,3", "n": 16, "lam": 0.3},
    {"name": "Medium allein n=+16", "n": 16, "lam": 0.1, "ohne_ball": True},
]
KZ_SPALTEN = ["x_ball", "S_ball", "C_am_ball", "Q_psi", "Q_chi", "C_min", "C_max"]


# ================================================================ Allgemeines

def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def gf(v):
    return float(v.item()) if torch.is_tensor(v) else float(v)


def teilen(a, b):
    return a / b if b != 0.0 else float("nan")


# ================================================================ 1D-Anker (aus tests1d.py) und Anfangsfelder

def anker_ab(w2):
    return 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)


def profil(y, w2):
    """Geschlossenes 1D-Profil zur Masse 1 und seine Ableitung: f^2 = 2 a0/(1 + b0 cosh(2 sqrt(a0) y))."""
    a0, b0 = anker_ab(w2)
    k2 = 2.0 * math.sqrt(a0)
    z = (k2 * y).clamp(-700.0, 700.0)                 # cosh(700) ~ 5e303: kein Ueberlauf
    nenner = 1.0 + b0 * torch.cosh(z)
    f = torch.sqrt(2.0 * a0 / nenner)
    return f, -f * (0.5 * k2 * b0) * torch.sinh(z) / nenner


def anker_wgv(w2):
    """Geschlossene 1D-Werte: I = sqrt(2) arcosh(1/b0), W = omega^2 I, G = sqrt(a0)/2 - b0^2 I/4, V = W + G."""
    a0, b0 = anker_ab(w2)
    integral = math.sqrt(2.0) * math.acosh(1.0 / b0)
    w = w2 * integral
    g = math.sqrt(a0) / 2.0 - b0 * b0 * integral / 4.0
    return w, g, w + g


def anker_q_e(w2):
    """Q und E des 1D-Balls (Masse 1): Q = 2 W / omega, E = W + G + V."""
    w, g, v = anker_wgv(w2)
    return 2.0 * w / math.sqrt(w2), w + g + v


def anker_umkehr(q):
    """omega^2 des 1D-Balls mit der Ladung q (Q faellt mit omega^2), durch Einschachteln."""
    if not math.isfinite(q) or q <= 0.0:
        return float("nan")
    lo, hi = 0.5 + 1e-12, 1.0 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if anker_q_e(mid)[0] > q:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def fwhm(w2):
    """Volle Halbwertsbreite von |psi|^2 des 1D-Balls (Masse 1): arcosh((1 + 2 b0)/b0)/sqrt(a0)."""
    a0, b0 = anker_ab(w2)
    return math.acosh((1.0 + 2.0 * b0) / b0) / math.sqrt(a0)


def gitter(dx, periodisch=False):
    """x_i = (i - i0) dx; offen: [-L, L] mit beiden Randpunkten; periodisch: [-L, L) mit 2 L/dx Punkten."""
    i0 = int(round(L_BOX / dx))
    n = 2 * i0 if periodisch else 2 * i0 + 1
    return (torch.arange(n, dtype=F64, device=DEV) - i0) * dx


def index_von(x, xw):
    return int(round((xw - x[0].item()) / (x[1] - x[0]).item()))


def ball(x, xc, w2, m=1.0, v=0.0, phase=0.0):
    """Ball mit omega = m sqrt(w2) in einem Feld der Masse m (Selbstpotential m^2 U), um xc, Geschwindigkeit v.

    f = profil(m gamma (x - xc)); Feld = f exp(i(omega gamma v (x - xc) + phase)),
    Zeitableitung = (-gamma v m f' - i omega gamma f) exp(...)  (Lorentz-Boost wie in tests1d.py)."""
    w = m * math.sqrt(w2)
    gam = 1.0 / math.sqrt(1.0 - v * v)
    f, fp = profil(m * gam * (x - xc), w2)
    ph = torch.exp(1j * (w * gam * v * (x - xc) + phase))
    return f * ph, (-gam * v * m * fp - 1j * w * gam * f) * ph


def leer(x):
    z = torch.zeros(x.shape[0], dtype=C128, device=DEV)
    return z, z.clone()


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def stapel(felder, periodisch):
    """Liste (psi, psi_t, chi, chi_t) je Lauf -> vier (B, N)-Stapel; offene Box mit Dirichlet-Rand."""
    aus = [torch.stack([f[j] for f in felder]) for j in range(4)]
    if not periodisch:
        for a in aus:
            a[:, 0] = 0.0
            a[:, -1] = 0.0
    return aus


class Kopplung:
    """Modellparameter je Lauf als (B, 1)-Spalten; Schalter sparen Rechenschritte, wenn ein Term in keinem Lauf vorkommt."""

    def __init__(self, laeufe):
        def spalte(name, vorgabe):
            return torch.tensor([float(r.get(name, vorgabe)) for r in laeufe], dtype=F64, device=DEV).unsqueeze(1)
        for r in laeufe:
            if float(r.get("mc2", 1.0)) < float(r.get("eps", 0.0)) ** 2 - 1e-15:
                raise ValueError(f"Lauf {r.get('name')}: mc2 < eps^2, das Vakuum waere tachyonisch")
        self.lam, self.lam2, self.eps = spalte("lam", 0.0), spalte("lam2", 0.0), spalte("eps", 0.0)
        self.mc2, self.kc, self.g4 = spalte("mc2", 1.0), spalte("kc", 1.0), spalte("g4", 0.0)
        self.mit_lam = bool((self.lam != 0.0).any() or (self.lam2 != 0.0).any())
        self.mit_eps = bool((self.eps != 0.0).any())
        self.mit_selbst = bool((self.kc != 0.0).any() or (self.g4 != 0.0).any())


# ================================================================ Zeitentwicklung

def lap(f, dx, periodisch):
    """Zweite Ableitung; offen wie tests1d.py (Randpunkte bleiben 0), periodisch ueber torch.roll."""
    if periodisch:
        return (torch.roll(f, -1, dims=1) - 2.0 * f + torch.roll(f, 1, dims=1)) / (dx * dx)
    fluss = (f[:, 1:] - f[:, :-1]) / dx
    aus = torch.zeros_like(f)
    aus[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
    return aus


def kraft(psi, chi, par, dx, periodisch):
    s = psi.real ** 2 + psi.imag ** 2
    c = chi.real ** 2 + chi.imag ** 2
    fp = 1.0 - 2.0 * s + 1.5 * s * s
    fc = par.mc2
    if par.mit_selbst:
        fc = fc + 2.0 * par.g4 * c + par.kc * (-2.0 * c + 1.5 * c * c)
    if par.mit_lam:
        fp = fp + c * (par.lam + 2.0 * par.lam2 * s)
        fc = fc + s * (par.lam + par.lam2 * s)
    a_psi = lap(psi, dx, periodisch) - fp * psi
    a_chi = lap(chi, dx, periodisch) - fc * chi
    if par.mit_eps:
        a_psi = a_psi - par.eps * chi
        a_chi = a_chi - par.eps * psi
    return a_psi, a_chi


def entwickeln(felder, par, dx, dt, t_end, t_mess, messen, periodisch):
    """Velocity-Verlet wie tests1d.py fuer beide Felder, alle Laeufe als ein Stapel; messen(...) -> (B, m)."""
    psi, vpsi, chi, vchi = felder
    x = gitter(dx, periodisch)
    sig = None if periodisch else SIGMA0 * ((x.abs() - X_SPONGE).clamp(min=0.0) / (L_BOX - X_SPONGE)) ** 2
    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(t_mess / dt)))
    h = 0.5 * dt
    reihe = [messen(psi, vpsi, chi, vchi)]
    ap, ac = kraft(psi, chi, par, dx, periodisch)
    for n in range(1, n_schritte + 1):
        if sig is None:
            vpsi = vpsi + h * ap
            vchi = vchi + h * ac
        else:
            vpsi = vpsi + h * (ap - sig * vpsi)
            vchi = vchi + h * (ac - sig * vchi)
        psi = psi + dt * vpsi
        chi = chi + dt * vchi
        ap, ac = kraft(psi, chi, par, dx, periodisch)
        if sig is None:
            vpsi = vpsi + h * ap
            vchi = vchi + h * ac
        else:
            vpsi = vpsi + h * (ap - sig * vpsi)
            vchi = vchi + h * (ac - sig * vchi)
        if n % alle == 0:
            reihe.append(messen(psi, vpsi, chi, vchi))
    daten = torch.stack(reihe)                          # (M, B, m)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
    return t, daten, (psi, vpsi, chi, vchi)


def stufen_rechnen(name, laeufe, bauen, t_end, t_mess, periodisch=False):
    """Grob (dx, dt) und fein (dx/2, dt/2). bauen(x, dx, par) -> (Felder, messen)."""
    par = Kopplung(laeufe)
    aus = {}
    for stufe, dx, dt in (("grob", DX, DT), ("fein", DX * FEIN, DT * FEIN)):
        x = gitter(dx, periodisch)
        felder, messen = bauen(x, dx, par)
        t0 = uhr()
        t, daten, ende = entwickeln(felder, par, dx, dt, t_end, t_mess, messen, periodisch)
        sek = uhr() - t0
        print(f"{name} {stufe}: {daten.shape[1]} Laeufe x {x.shape[0]} Punkte, T = {t_end:g}, "
              f"{int(round(t_end / dt))} Schritte, {sek:.1f} s", flush=True)
        aus[stufe] = {"t": t, "daten": daten, "sek": sek, "x": x,
                      "S_ende": ende[0].real ** 2 + ende[0].imag ** 2, "C_ende": ende[2].real ** 2 + ende[2].imag ** 2}
    return aus


# ================================================================ Mess- und Auswerte-Hilfen

def ladungen(psi, vpsi, chi, vchi):
    s = psi.real ** 2 + psi.imag ** 2
    c = chi.real ** 2 + chi.imag ** 2
    return s, c, 2.0 * (psi * vpsi.conj()).imag, 2.0 * (chi * vchi.conj()).imag


def energiedichte(psi, vpsi, chi, vchi, par, dx, periodisch):
    s = psi.real ** 2 + psi.imag ** 2
    c = chi.real ** 2 + chi.imag ** 2
    e = (vpsi.real ** 2 + vpsi.imag ** 2 + vchi.real ** 2 + vchi.imag ** 2 + s - s * s + 0.5 * s ** 3
         + par.mc2 * c + par.g4 * c * c + par.kc * (-c * c + 0.5 * c ** 3) + c * (par.lam * s + par.lam2 * s * s)
         + 2.0 * par.eps * (psi.conj() * chi).real)
    for f in (psi, chi):
        if periodisch:
            d = torch.roll(f, -1, dims=1) - f
            e = e + (d.real ** 2 + d.imag ** 2) / (dx * dx)
        else:
            d = f[:, 1:] - f[:, :-1]
            e = torch.cat([e[:, :-1] + (d.real ** 2 + d.imag ** 2) / (dx * dx), e[:, -1:]], dim=1)
    return e


def wrap(a):
    """Winkel nach [-pi, pi)."""
    return torch.remainder(a + PI, 2.0 * PI) - PI


def entfalten(th):
    """Phasenreihe (M, ...) stetig machen; Schritte muessen unter pi liegen (omega * t_mess < pi)."""
    return torch.cat([th[:1], th[:1] + torch.cumsum(wrap(th[1:] - th[:-1]), dim=0)], dim=0)


def ab_index(t, anteil):
    """Erster Index mit t >= anteil * T."""
    return int((t < anteil * t[-1].item() - 1e-9).sum().item())


def steigung(t, y):
    """Kleinste-Quadrate-Steigung von y (M, ...) gegen t (M,)."""
    tm = t - t.mean()
    form = [-1] + [1] * (y.dim() - 1)
    return (tm.view(form) * (y - y.mean(dim=0))).sum(dim=0) / (tm * tm).sum()


def beschleunigung(t, y):
    """2 c2 aus y = c0 + c1 t + c2 t^2 (kleinste Quadrate, t zentriert und skaliert); y (M,)."""
    h = 0.5 * (t[-1] - t[0]).item()
    tm = (t - t.mean()) / h
    a = torch.stack([torch.ones_like(tm), tm, tm * tm], dim=1)
    koef = torch.linalg.solve(a.T @ a, a.T @ y)
    return 2.0 * koef[2].item() / (h * h)


def hauptfrequenz(t, y):
    """Kreisfrequenz und Amplitude der groessten FFT-Spitze von y (Mittel und Trend entfernt, Hann-Fenster)."""
    n = y.shape[0]
    if n < 16:
        return float("nan"), 0.0
    rest = y - y.mean() - steigung(t, y) * (t - t.mean())
    fen = torch.hann_window(n, periodic=False, dtype=F64, device=DEV)
    amp = torch.fft.rfft(rest * fen).abs()
    k = int(torch.argmax(amp[1:]).item()) + 1
    delta = 0.0
    if k < amp.shape[0] - 1:
        a, b, c = amp[k - 1].item(), amp[k].item(), amp[k + 1].item()
        nenner = a - 2.0 * b + c
        delta = 0.5 * (a - c) / nenner if nenner != 0.0 else 0.0
    return (k + delta) * 2.0 * PI / (n * (t[1] - t[0]).item()), 2.0 * amp[k].item() / fen.sum().item()


def durchgaenge(y, schwelle):
    """Wechsel zwischen y > schwelle und y < -schwelle (Hysterese: Rauschen um 0 zaehlt nicht); y (M,)."""
    zustand, n = 0, 0
    for v in y.tolist():
        if v > schwelle:
            n += 1 if zustand == -1 else 0
            zustand = 1
        elif v < -schwelle:
            n += 1 if zustand == 1 else 0
            zustand = -1
    return n


def spitze(x, y):
    """Ort und Hoehe des Maximums je Zeile; Ort mit Parabel durch drei Punkte verfeinert; y (B, N)."""
    n = y.shape[1]
    i = y.argmax(dim=1, keepdim=True).clamp(1, n - 2)
    ym, y0, yp = y.gather(1, i - 1), y.gather(1, i), y.gather(1, i + 1)
    nenner = ym - 2.0 * y0 + yp
    gut = nenner.abs() > 1e-300
    d = torch.where(gut, 0.5 * (ym - yp) / torch.where(gut, nenner, torch.ones_like(nenner)),
                    torch.zeros_like(nenner)).clamp(-1.0, 1.0)
    return (x[i] + d * (x[1] - x[0])).squeeze(1), y0.squeeze(1)


def l3(wert_grob, wert_fein, null):
    """Latte L3: Effekt (Abstand vom Nullwert) mindestens fuenfmal so gross wie die Aenderung grob -> fein."""
    eff, aend = abs(wert_grob - null), abs(wert_fein - wert_grob)
    return {"effekt": eff, "aenderung": aend, "bestanden": bool(eff >= 5.0 * aend)}


def l3_zeile(liste):
    n_ok = sum(1 for e in liste for k, v in e.items() if k != "lauf" and v["bestanden"])
    n_ges = sum(1 for e in liste for k in e if k != "lauf")
    return f"  L3 (Effekt >= 5 x Aenderung grob -> fein): {n_ok} von {n_ges} Kenngroessen bestanden"


def sek_zeile(res):
    return f"  Rechenzeit grob {res['sek']['grob']:.1f} s, fein {res['sek']['fein']:.1f} s"


# ================================================================ zellkern (Bio 8)

def test_zellkern(faktor):
    laeufe = [{"name": f"m={m:g} lam={lam:+.1f}", "m": m, "lam": lam, "mc2": m * m, "kc": m * m}
              for m in ZK_M for lam in ZK_LAM]

    def bauen(x, dx, par):
        felder = [ball(x, 0.0, ZK_W2) + ball(x, ZK_D0, ZK_W2, m=r["m"]) for r in laeufe]
        fen = (x.abs() < ZK_FENSTER).to(F64)
        n = x.shape[0]

        def messen(psi, vpsi, chi, vchi):
            s, c, rp, rc = ladungen(psi, vpsi, chi, vchi)
            ms = (s * fen).sum(1).clamp(min=1e-300)
            mc = (c * fen).sum(1).clamp(min=1e-300)
            xs = (x * s * fen).sum(1) / ms
            xc = (x * c * fen).sum(1) / mc
            ws = torch.sqrt(((x - xs.unsqueeze(1)) ** 2 * s * fen).sum(1) / ms)
            wc = torch.sqrt(((x - xc.unsqueeze(1)) ** 2 * c * fen).sum(1) / mc)
            i_c = ((xc - x[0]) / dx).round().long().clamp(0, n - 1).unsqueeze(1)
            i_s = ((xs - x[0]) / dx).round().long().clamp(0, n - 1).unsqueeze(1)
            smax = s.max(dim=1).values.clamp(min=1e-300)
            cmax = c.max(dim=1).values.clamp(min=1e-300)
            return torch.stack([xs, xc, ws, wc, (rp * fen).sum(1) * dx, (rc * fen).sum(1) * dx,
                                s.gather(1, i_c).squeeze(1) / smax, c.gather(1, i_s).squeeze(1) / cmax,
                                smax, cmax], dim=1)
        return stapel(felder, False), messen

    stufen = stufen_rechnen("zellkern", laeufe, bauen, ZK_T * faktor, ZK_MESS)
    erg = {s: auswertung_zellkern(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = []
    for zg, zf in zip(erg["grob"], erg["fein"]):
        if zg["lam"] == 0.0:
            continue
        if zg["klasse"] == "getrennt":                   # Kenngroesse: Zeitpunkt der Trennung (Abstand > 5)
            l3_liste.append({"lauf": zg["name"], "t_trennung": l3(zg["t_trennung"], zf["t_trennung"], 0.0)})
        else:
            l3_liste.append({"lauf": zg["name"], "dAbstand": l3(zg["dAbstand"], zf["dAbstand"], 0.0),
                             "dK": l3(zg["dK"], zf["dK"], 0.0)})
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "fwhm_psi": fwhm(ZK_W2),
            "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def auswertung_zellkern(laeufe, t, d):
    ie = ab_index(t, 0.75)
    m = d[ie:].mean(dim=0)                               # (B, 10), Endfenster [3T/4, T]
    abst_t = (d[:, :, 1] - d[:, :, 0]).abs()             # (M, B)
    zeilen = []
    for b, r in enumerate(laeufe):
        xs, xc, ws, wc, qs, qc, s_c, c_s, smax, cmax = [gf(v) for v in m[b]]
        abst = abs(xc - xs)
        k = teilen(wc, ws)
        kk = max(k, 1.0 / k) if k > 0.0 else float("inf")
        loch_psi, loch_chi = 1.0 - s_c, 1.0 - c_s        # Delle der aeusseren Komponente am Ort der inneren
        weg = torch.nonzero(abst_t[:, b] > 5.0)
        if weg.numel() or abst > 5.0:                    # einmal getrennt reicht: ein Ball kann das Fenster verlassen
            klasse = "getrennt"
        elif abst < 1.0 and ((k < 1.0 and loch_psi > 0.2) or (k > 1.0 and loch_chi > 0.2)):
            klasse = "Huelle mit Loch"
        elif abst < 1.0 and kk > 1.25:
            klasse = "verschachtelt"
        elif abst < 1.0:
            klasse = "gemeinsam"
        else:
            klasse = "unklar"
        zeilen.append({"name": r["name"], "m": r["m"], "lam": r["lam"], "abstand": abst, "K": k,
                       "K_unabhaengig": 1.0 / r["m"], "w_psi": ws, "w_chi": wc, "loch_psi": loch_psi,
                       "loch_chi": loch_chi, "Q_psi_halt": teilen(qs, gf(d[0, b, 4])),
                       "Q_chi_halt": teilen(qc, gf(d[0, b, 5])), "S_max": smax, "C_max": cmax,
                       "abstand_max": gf(abst_t[:, b].max()),
                       "t_trennung": gf(t[weg[0, 0]]) if weg.numel() else float("nan"), "klasse": klasse})
    null = {z["m"]: z for z in zeilen if z["lam"] == 0.0}
    for z in zeilen:
        z["dK"] = z["K"] - null[z["m"]]["K"]
        z["dAbstand"] = z["abstand"] - null[z["m"]]["abstand"]
    return zeilen


def bericht_zellkern(res):
    zz = [f"zellkern (Bio 8): psi-Ball omega^2 = {ZK_W2} (FWHM {res['fwhm_psi']:.3f}) bei 0, chi-Ball mit Masse m und "
          f"omega_chi = m sqrt({ZK_W2}) bei +{ZK_D0}. Endfenster [3T/4, T]. K = w_chi/w_psi (ohne Kopplung 1/m).",
          "  Lauf | Abstand | K (1/m) | dK | Loch psi | Loch chi | Q_psi, Q_chi gehalten | Abstand max | t Trennung | "
          "Klasse"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]:
            zz.append(f"  {z['name']:14s} | {z['abstand']:.3f} | {z['K']:.3f} ({z['K_unabhaengig']:.3f}) | "
                      f"{z['dK']:+.3f} | {z['loch_psi']:+.3f} | {z['loch_chi']:+.3f} | {z['Q_psi_halt']:.4f}, "
                      f"{z['Q_chi_halt']:.4f} | {z['abstand_max']:.2f} | {z['t_trennung']:.1f} | {z['klasse']}")
    zz += [l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ raeuber (Bio 15)

def rb_einheit(x, xa, xb, q_ges, z0, dphi):
    """psi-Ball mit (1 + z0)/2 und chi-Ball mit (1 - z0)/2 der Ladung q_ges; chi-Phase dphi."""
    qa, qb = 0.5 * (1.0 + z0) * q_ges, 0.5 * (1.0 - z0) * q_ges
    pa = ball(x, xa, anker_umkehr(qa))
    pb = ball(x, xb, anker_umkehr(qb), phase=dphi) if qb > 1e-9 else leer(x)
    return pa, pb


def test_raeuber(faktor):
    q_ges = 2.0 * anker_q_e(RB_W2_REF)[0]
    laeufe = [dict(r, eps=r.get("eps", RB_EPS), mc2=1.0, kc=1.0) for r in RB_LAEUFE]

    def bauen(x, dx, par):
        felder = []
        for r in laeufe:
            if "box" in r:
                p, c = leer(x), leer(x)
                for xc, fak in r["box"]:
                    pa, pb = rb_einheit(x, xc, xc, fak * q_ges, r["z0"], r["dphi"])
                    p, c = plus(p, pa), plus(c, pb)
            else:
                h = 0.5 * r.get("abstand", 0.0)
                p, c = rb_einheit(x, -h, h, q_ges, r["z0"], r["dphi"])
            felder.append(p + c)
        fen = (x.abs() < RB_FENSTER).to(F64)
        i0 = index_von(x, 0.0)

        def messen(psi, vpsi, chi, vchi):
            s, c, rp, rc = ladungen(psi, vpsi, chi, vchi)
            return torch.stack([(rp * fen).sum(1) * dx, (rc * fen).sum(1) * dx,
                                wrap(torch.angle(chi[:, i0]) - torch.angle(psi[:, i0])), s[:, i0], c[:, i0]], dim=1)
        return stapel(felder, False), messen

    stufen = stufen_rechnen("raeuber", laeufe, bauen, RB_T * faktor, RB_MESS)
    erg = {s: auswertung_raeuber(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "A": l3(zg["A"], zf["A"], 0.0), "Periode": l3(zg["Periode"], zf["Periode"], 0.0)}
                for zg, zf, r in zip(erg["grob"], erg["fein"], laeufe) if not r.get("kontrolle")]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "q_ges": q_ges,
            "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def auswertung_raeuber(laeufe, t, d):
    qp, qc = d[:, :, 0], d[:, :, 1]
    qs = qp + qc
    z = (qp - qc) / qs.clamp(min=1e-300)
    ia = ab_index(t, 1.0 / 6.0)
    zeilen = []
    for b, r in enumerate(laeufe):
        zz = z[ia:, b]
        zmin, zmax = gf(zz.min()), gf(zz.max())
        amp = 0.5 * (zmax - zmin)
        wechsel = durchgaenge(zz, 0.005)
        om, _ = hauptfrequenz(t[ia:], zz)
        a1, a2 = qp[ia:, b] - qp[ia:, b].mean(), qc[ia:, b] - qc[ia:, b].mean()
        if amp < 0.01:
            klasse = "ruhig"
        elif wechsel >= 2:
            klasse = "pendelt um Gleichstand"
        else:
            klasse = "Selbstfang"
        zeilen.append({"name": r["name"], "z0": r["z0"], "dphi0": r["dphi"], "eps": r["eps"], "z_start": gf(z[0, b]),
                       "z_min": zmin, "z_max": zmax, "z_mittel": gf(zz.mean()), "A": amp, "wechsel": wechsel,
                       "Omega": om, "Periode": teilen(2.0 * PI, om),
                       "cos_dphi_mittel": gf(torch.cos(d[ia:, b, 2]).mean()),
                       "summe_rel_max": teilen(gf((qs[:, b] - qs[0, b]).abs().max()), gf(qs[0, b])),
                       "korrelation": teilen(gf((a1 * a2).sum()), gf(torch.sqrt((a1 * a1).sum() * (a2 * a2).sum()))),
                       "klasse": klasse})
    return zeilen


def bericht_raeuber(res):
    zz = [f"raeuber (Bio 15): psi- und chi-Ball (gleiche Masse, lam = 0) am selben Ort, Austausch eps = {RB_EPS}. "
          f"Ladung je Einheit {res['q_ges']:.4f}; z = (Q_psi - Q_chi)/(Q_psi + Q_chi) in |x| < {RB_FENSTER:g}; "
          "Fenster [T/6, T].",
          "  Lauf | z Start | z min .. max | A | Wechsel | Periode | cos dphi | Summe rel. | Korr. psi/chi | Klasse"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]:
            zz.append(f"  {z['name']:22s} | {z['z_start']:+.4f} | {z['z_min']:+.4f} .. {z['z_max']:+.4f} | "
                      f"{z['A']:.4f} | {z['wechsel']} | {z['Periode']:.1f} | {z['cos_dphi_mittel']:+.3f} | "
                      f"{z['summe_rel_max']:.1e} | {z['korrelation']:+.3f} | {z['klasse']}")
    zz += [l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ mitochondrium (Bio 35)

def test_mitochondrium(faktor):
    laeufe = [{"name": f"lam={lam:+.1f} v={v:.1f}", "lam": lam, "v": v, "mc2": MT_M ** 2, "kc": MT_M ** 2}
              for lam in MT_LAM for v in MT_V]

    def bauen(x, dx, par):
        felder = [ball(x, 0.0, MT_W2_WIRT) + ball(x, 0.0, MT_W2_GAST, m=MT_M, v=r["v"]) for r in laeufe]
        fen = (x.abs() < MT_FENSTER).to(F64)

        def messen(psi, vpsi, chi, vchi):
            s, c, rp, rc = ladungen(psi, vpsi, chi, vchi)
            xg, cg = spitze(x, c)
            xh = (x * s * fen).sum(1) / (s * fen).sum(1).clamp(min=1e-300)
            smax = s.max(dim=1).values
            halb = ((s > 0.5 * smax.unsqueeze(1)).to(F64) * fen).sum(1) * (0.5 * dx)
            gfen = ((x - xg.unsqueeze(1)).abs() < MT_GAST_FENSTER).to(F64)
            return torch.stack([xg, cg, xh, halb, (rc * gfen).sum(1) * dx, (rp * fen).sum(1) * dx, smax], dim=1)
        return stapel(felder, False), messen

    stufen = stufen_rechnen("mitochondrium", laeufe, bauen, MT_T * faktor, MT_MESS)
    erg = {s: auswertung_mitochondrium(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "d_drin": l3(zg["d_drin"], zf["d_drin"], 0.0)}
                for zg, zf in zip(erg["grob"], erg["fein"]) if zg["lam"] != 0.0 and zg["v"] > 0.0]
    q_gast, e_gast = anker_q_e(MT_W2_GAST)
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "fwhm_wirt": fwhm(MT_W2_WIRT),
            "Q_wirt": anker_q_e(MT_W2_WIRT)[0], "Q_gast": q_gast, "E_gast": MT_M * e_gast,
            "fwhm_gast": fwhm(MT_W2_GAST) / MT_M, "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def auswertung_mitochondrium(laeufe, t, d):
    ia = ab_index(t, 0.25)
    zeilen = []
    for b, r in enumerate(laeufe):
        xg, cg, xh, rh, qg, qh = (d[:, b, j] for j in range(6))
        rel = xg - xh
        drin = (rel.abs() < rh).to(F64)
        raus = torch.nonzero(rel.abs() - rh > 3.0)
        i_raus = int(raus[0, 0].item()) if raus.numel() else -1
        anteil = gf(drin[ia:].mean())
        if i_raus >= 0:
            klasse = "entkommen"
        elif anteil >= 0.9 and bool(drin[-1] > 0.5):
            klasse = "gefangen" if r["v"] > 0.0 else "ruht innen"
        else:
            klasse = "unklar"
        ie = i_raus if i_raus >= 0 else len(t) - 1         # Gast-Werte beim Austritt bzw. am Ende
        zeilen.append({"name": r["name"], "lam": r["lam"], "v": r["v"], "drin_anteil": anteil,
                       "t_raus": gf(t[i_raus]) if i_raus >= 0 else float("nan"),
                       "abstand_ende": abs(gf(rel[-1])), "R_wirt_ende": gf(rh[-1]), "abstand_max": gf(rel.abs().max()),
                       "durchgaenge": durchgaenge(rel[ia:], 1.0), "x_wirt_ende": gf(xh[-1]),
                       "Q_gast_halt": teilen(gf(qg[ie]), gf(qg[0])), "C_gast_halt": teilen(gf(cg[ie]), gf(cg[0])),
                       "Q_wirt_halt": teilen(gf(qh[-1]), gf(qh[0])), "klasse": klasse})
    null = {z["v"]: z for z in zeilen if z["lam"] == 0.0}
    for z in zeilen:
        z["d_drin"] = z["drin_anteil"] - null[z["v"]]["drin_anteil"]
    return zeilen


def bericht_mitochondrium(res):
    zz = [f"mitochondrium (Bio 35): Wirt psi omega^2 = {MT_W2_WIRT} (FWHM {res['fwhm_wirt']:.2f}, Q {res['Q_wirt']:.2f}); "
          f"Gast chi Masse {MT_M:g}, omega^2/m^2 = {MT_W2_GAST} (FWHM {res['fwhm_gast']:.2f}, Q {res['Q_gast']:.3f}, "
          f"E {res['E_gast']:.3f}), Start in der Mitte mit v. Fenster [T/4, T].",
          "  Lauf | drin-Anteil | Durchgaenge | t raus | Abstand Ende (R Wirt) | Abstand max | x Wirt Ende | "
          "Q_gast, C_gast gehalten | Q_wirt gehalten | d_drin | Klasse"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]:
            zz.append(f"  {z['name']:14s} | {z['drin_anteil']:.3f} | {z['durchgaenge']} | {z['t_raus']:.1f} | "
                      f"{z['abstand_ende']:.2f} ({z['R_wirt_ende']:.2f}) | {z['abstand_max']:.2f} | "
                      f"{z['x_wirt_ende']:+.2f} | {z['Q_gast_halt']:.4f}, {z['C_gast_halt']:.4f} | "
                      f"{z['Q_wirt_halt']:.4f} | {z['d_drin']:+.3f} | {z['klasse']}")
    zz += [l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ altern (Bio 48)

def al_vorhersage(w2, eps):
    """Rate erster Ordnung in eps: dQ/dt = -eps^2 ft(omega)^2/omega, ft(k) = Int f(x) cos(k x) dx (Quadratur h = 0,005).

    Herleitung (PLAN.md): chi'' + omega^2 chi = eps f im Fernfeld der masselosen Mode, auslaufende Welle mit
    Amplitude eps ft(omega)/(2 omega) auf jeder Seite, Ladungsfluss 2 omega |Amplitude|^2 je Seite."""
    y = torch.arange(-80.0, 80.0 + 1e-9, 0.005, dtype=F64, device=DEV)
    f, _ = profil(y, w2)
    w = math.sqrt(w2)
    ft = gf((f * torch.cos(w * y)).sum()) * 0.005
    return eps * eps * ft * ft / w, ft


def test_altern(faktor):
    laeufe = [{"name": f"masselos w2={w2}", "w2": w2, "eps": AL_EPS, "mc2": AL_EPS ** 2, "kc": 0.0, "art": "masselos"}
              for w2 in AL_W2]
    laeufe += [{"name": "Gegenprobe m_chi=1,2 w2=0.500001", "w2": 0.500001, "eps": AL_EPS, "mc2": AL_MC2_SCHWER,
                "kc": 0.0, "art": "schwer"},
               {"name": "Gegenprobe m_chi=1,2 w2=0.7", "w2": 0.7, "eps": AL_EPS, "mc2": AL_MC2_SCHWER, "kc": 0.0,
                "art": "schwer"},
               {"name": "Gegenprobe eps=0 w2=0.7", "w2": 0.7, "eps": 0.0, "mc2": AL_EPS ** 2, "kc": 0.0, "art": "ohne"}]

    def bauen(x, dx, par):
        felder = []
        for r in laeufe:
            p, vp = ball(x, 0.0, r["w2"])
            s = p.real ** 2 + p.imag ** 2
            fak = r["eps"] / (1.0 - 2.0 * s + 1.5 * s * s - r["mc2"])   # lokale Bekleidung eps f/(U'(S) - mc2)
            felder.append((p, vp, fak * p, fak * vp))
        fen = (x.abs() < AL_FENSTER).to(F64)
        box = (x.abs() < AL_BOX).to(F64)

        def messen(psi, vpsi, chi, vchi):
            s, c, rp, rc = ladungen(psi, vpsi, chi, vchi)
            return torch.stack([((rp + rc) * fen).sum(1) * dx, (rp * fen).sum(1) * dx,
                                ((rp + rc) * box).sum(1) * dx], dim=1)
        return stapel(felder, False), messen

    stufen = stufen_rechnen("altern", laeufe, bauen, AL_T * faktor, AL_MESS)
    erg = {s: auswertung_altern(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "Gamma": l3(zg["Gamma"], zf["Gamma"], 0.0)}
                for zg, zf in zip(erg["grob"], erg["fein"]) if zg["art"] == "masselos"]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste,
            "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def auswertung_altern(laeufe, t, d):
    ia = ab_index(t, 0.25)
    zeilen = []
    for b, r in enumerate(laeufe):
        qb = d[:, b, 0]
        gam = -gf(steigung(t[ia:], qb[ia:]))
        g_v, ft = al_vorhersage(r["w2"], r["eps"]) if r["art"] == "masselos" else (0.0, float("nan"))
        zeilen.append({"name": r["name"], "art": r["art"], "omega2": r["w2"], "Q_anker": anker_q_e(r["w2"])[0],
                       "fwhm": fwhm(r["w2"]), "Q_ball_0": gf(qb[0]), "Q_ball_ab": gf(qb[ia]), "Q_ball_T": gf(qb[-1]),
                       "Anfangsverlust": gf(qb[0] - qb[ia]), "Gamma": gam, "Gamma_vorhersage": g_v, "ft": ft,
                       "verhaeltnis": teilen(gam, g_v), "Lebensdauer": teilen(gf(qb[ia]), gam),
                       "Q_box_rel": teilen(gf(d[-1, b, 2] - d[0, b, 2]), gf(d[0, b, 2]))})
    return zeilen


def bericht_altern(res):
    zz = [f"altern (Bio 48): psi-Ball ruhend; Austausch eps = {AL_EPS} mit chi (mc2 = eps^2, frei): eine Eigenmode "
          f"masselos. Gamma = -dQ_Ball/dt (Fit auf [T/4, T], Q_Ball = Q_psi + Q_chi in |x| < {AL_FENSTER:g}); "
          "Vorhersage eps^2 ft(omega)^2/omega.",
          "  Lauf | Q Anker | Q Ball 0 -> T | Anfangsverlust | Gamma | Vorhersage | Verh. | Lebensdauer Q/Gamma"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]:
            zz.append(f"  {z['name']:32s} | {z['Q_anker']:.4f} | {z['Q_ball_0']:.5f} -> {z['Q_ball_T']:.5f} | "
                      f"{z['Anfangsverlust']:+.2e} | {z['Gamma']:+.3e} | {z['Gamma_vorhersage']:.3e} | "
                      f"{z['verhaeltnis']:.3f} | {z['Lebensdauer']:.3e}")
        masselos = sorted((z for z in res["ergebnis"][stufe] if z["art"] == "masselos"), key=lambda z: z["Q_anker"])
        g = [z["Gamma"] for z in masselos]
        monoton = all(g[i] <= g[i + 1] for i in range(len(g) - 1))
        zz.append(f"  Gamma nach Q aufsteigend monoton wachsend: {monoton}")
    zz += [l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ G2-02 (Ideen-Evolution Gen 2): Bilanz des Alterns
# Kopie von RUNDE-05/r5d/r5d.py; neu nur dieser Abschnitt und zwei Eintraege in TESTS. Karte GEN-02/G2-02/KARTE.md.
# Dynamik und Anfangsfelder wie altern (gleiche 11 Laeufe); neu sind nur Messgroessen (alle 0,5).
# Hauptlauf "bilanz" (8 masselose Laeufe) und Gegenprobe "bilanz_gegen" (3 Laeufe) sind getrennte Aufrufe.

BI_MESS = 0.5
BI_SCHALE = 110.0            # Schale 40 <= |x| < 110, Schwammbereich |x| >= 110 (X_SPONGE)
BI_T_KONTAKT = 90.0          # bis hier hat keine Welle aus |x| < 10 den Schwamm erreicht
BI_SPALTEN = ["Q_win", "Q_psi_win", "Q_chi_win", "Q_neg_win", "Q_schale", "Q_schwamm", "Q_ges",
              "E_win", "E_schale", "E_schwamm", "E_ges", "x_max", "S_max", "x_betrag", "omega_max"]
# R5-D altern, Fensterladung bei T = 400 (lauf-69/altern/r5d_altern_ergebnis.json, Q_ball_T), V4-Anschluss
BI_R5D = {"grob": {"masselos w2=0.500001": 13.272808923029146, "masselos w2=0.5001": 9.949925348464646,
                   "masselos w2=0.51": 2.7553994478452926, "masselos w2=0.55": -0.9319376484334119,
                   "masselos w2=0.6": 2.493945259500739, "masselos w2=0.7": 2.220658539925476,
                   "masselos w2=0.8": 1.8385379676592313, "masselos w2=0.9": 1.293255787803732,
                   "Gegenprobe m_chi=1,2 w2=0.500001": 14.548131602250464,
                   "Gegenprobe m_chi=1,2 w2=0.7": 2.451577115106216, "Gegenprobe eps=0 w2=0.7": 2.4414914913415955},
          "fein": {"masselos w2=0.500001": 13.274816378473796, "masselos w2=0.5001": 9.949331404078288,
                   "masselos w2=0.51": 2.755269528309429, "masselos w2=0.55": -0.9451417598737053,
                   "masselos w2=0.6": 2.4989057251261455, "masselos w2=0.7": 2.2212237413335933,
                   "masselos w2=0.8": 1.8386657303754945, "masselos w2=0.9": 1.293261311701391,
                   "Gegenprobe m_chi=1,2 w2=0.500001": 14.548131621502684,
                   "Gegenprobe m_chi=1,2 w2=0.7": 2.4515774815862885, "Gegenprobe eps=0 w2=0.7": 2.441491654529432}}


def bi_laeufe(teil):
    if teil == "haupt":
        return [{"name": f"masselos w2={w2}", "w2": w2, "eps": AL_EPS, "mc2": AL_EPS ** 2, "kc": 0.0, "art": "masselos"}
                for w2 in AL_W2]
    return [{"name": "Gegenprobe m_chi=1,2 w2=0.500001", "w2": 0.500001, "eps": AL_EPS, "mc2": AL_MC2_SCHWER,
             "kc": 0.0, "art": "schwer"},
            {"name": "Gegenprobe m_chi=1,2 w2=0.7", "w2": 0.7, "eps": AL_EPS, "mc2": AL_MC2_SCHWER, "kc": 0.0,
             "art": "schwer"},
            {"name": "Gegenprobe eps=0 w2=0.7", "w2": 0.7, "eps": 0.0, "mc2": AL_EPS ** 2, "kc": 0.0, "art": "ohne"}]


def bi_rechnen(laeufe, faktor, name):
    def bauen(x, dx, par):
        felder = []
        for r in laeufe:
            p, vp = ball(x, 0.0, r["w2"])
            s = p.real ** 2 + p.imag ** 2
            fak = r["eps"] / (1.0 - 2.0 * s + 1.5 * s * s - r["mc2"])   # wie altern: lokale Bekleidung
            felder.append((p, vp, fak * p, fak * vp))
        ax = x.abs()
        fen = (ax < AL_FENSTER).to(F64)
        sch = ((ax >= AL_FENSTER) & (ax < BI_SCHALE)).to(F64)
        swa = (ax >= BI_SCHALE).to(F64)

        def messen(psi, vpsi, chi, vchi):
            s, c, rp, rc = ladungen(psi, vpsi, chi, vchi)
            rho = rp + rc
            e = energiedichte(psi, vpsi, chi, vchi, par, dx, False)
            i_max = torch.argmax(s, dim=1, keepdim=True)
            s_max = s.gather(1, i_max)
            om = (psi * vpsi.conj()).imag.gather(1, i_max) / s_max.clamp(min=1e-300)
            sw = s * fen
            return torch.stack([(rho * fen).sum(1) * dx, (rp * fen).sum(1) * dx, (rc * fen).sum(1) * dx,
                                (rho.clamp(max=0.0) * fen).sum(1) * dx, (rho * sch).sum(1) * dx,
                                (rho * swa).sum(1) * dx, rho.sum(1) * dx,
                                (e * fen).sum(1) * dx, (e * sch).sum(1) * dx, (e * swa).sum(1) * dx, e.sum(1) * dx,
                                x[i_max.squeeze(1)], s_max.squeeze(1),
                                (sw * ax).sum(1) / sw.sum(1).clamp(min=1e-300), om.squeeze(1)], dim=1)
        return stapel(felder, False), messen

    return stufen_rechnen(name, laeufe, bauen, AL_T * faktor, BI_MESS)


def bi_fenster(t, y, ta, tb):
    m = (t >= ta - 1e-9) & (t <= tb + 1e-9)
    return gf(steigung(t[m], y[m])) if int(m.sum()) > 2 else float("nan")


def bi_zeile(r, t, d, stufe, faktor):
    """Kenngroessen eines Laufs; d: (M, Spalten)."""
    col = {k: d[:, i] for i, k in enumerate(BI_SPALTEN)}
    T = gf(t[-1])
    q0, e0 = gf(col["Q_ges"][0]), gf(col["E_ges"][0])
    kontakt = t <= BI_T_KONTAKT * faktor + 1e-9
    e_ges = col["E_ges"]
    tief = torch.cummin(e_ges, dim=0).values
    om_gilt = col["S_max"] > 0.01
    g_v, _ = al_vorhersage(r["w2"], r["eps"]) if r["art"] == "masselos" else (0.0, float("nan"))

    def rq(ta, tb):
        sq, se = bi_fenster(t, col["Q_win"], ta, tb), bi_fenster(t, col["E_win"], ta, tb)
        m = (t >= ta - 1e-9) & (t <= tb + 1e-9)
        om = gf(col["omega_max"][m].mean()) if int(m.sum()) else float("nan")
        return {"R_EQ": teilen(se, sq), "omega_quer": om, "R_EQ_zu_omega": teilen(teilen(se, sq), om),
                "steigung_Q": sq, "steigung_E": se}

    def ballfest(tb):
        m = t <= tb + 1e-9
        return {"x_max_betrag_max": gf(col["x_max"][m].abs().max()), "Q_neg_min": gf(col["Q_neg_win"][m].min()),
                "bestanden": bool(gf(col["x_max"][m].abs().max()) <= 0.5
                                  and gf(col["Q_neg_win"][m].min()) >= -1e-3 * abs(q0))}

    ereignis = (col["x_max"].abs() > 0.5) | (col["Q_neg_win"] < -1e-3 * abs(q0))
    t_ereignis = gf(t[ereignis][0]) if bool(ereignis.any()) else float("nan")
    z = {"name": r["name"], "art": r["art"], "omega2": r["w2"], "omega": math.sqrt(r["w2"]), "Q0": q0, "E0": e0,
         "Q_win_T": gf(col["Q_win"][-1]), "Q_psi_win_T": gf(col["Q_psi_win"][-1]),
         "Q_chi_win_T": gf(col["Q_chi_win"][-1]), "Q_neg_win_T": gf(col["Q_neg_win"][-1]),
         "Q_schale_T": gf(col["Q_schale"][-1]), "Q_schwamm_T": gf(col["Q_schwamm"][-1]),
         "Q_abs_T": q0 - gf(col["Q_ges"][-1]), "E_abs_T": e0 - gf(e_ges[-1]),
         "dQ_schale_T_rel": teilen(gf(col["Q_schale"][-1] - col["Q_schale"][0]), abs(q0)),
         "x_max_T": gf(col["x_max"][-1]), "S_max_0": gf(col["S_max"][0]), "S_max_T": gf(col["S_max"][-1]),
         "x_betrag_0": gf(col["x_betrag"][0]), "x_betrag_T": gf(col["x_betrag"][-1]),
         "omega_T": gf(col["omega_max"][-1]), "t_ereignis": t_ereignis,
         "Gamma_fit": -bi_fenster(t, col["Q_win"], T / 4.0, T), "Gamma_formel": g_v,
         "spaet": rq(T / 4.0, T), "frueh": rq(T / 4.0, T / 2.0),
         "ball_ganz": ballfest(T), "ball_frueh": ballfest(T / 2.0),
         "plaus": {
             "Q_ges_bis_Kontakt_1e-9": {"max_rel": teilen(gf((col["Q_ges"][kontakt] - q0).abs().max()), abs(q0))},
             "E_ges_bis_Kontakt_1e-4": {"max_rel": teilen(gf((e_ges[kontakt] - e0).abs().max()), abs(e0))},
             "E_ges_steigt_nie_1e-6": {"max_anstieg_rel": teilen(gf((e_ges - tief).max()), abs(e0))},
             "omega_unter_1": {"max": gf(col["omega_max"][om_gilt].max()) if bool(om_gilt.any()) else float("nan")},
             "buchfuehrung_1e-9": {"max_rest_rel": teilen(gf((col["Q_win"] + col["Q_schale"] + col["Q_schwamm"]
                                                              - col["Q_ges"]).abs().max()), abs(q0))}}}
    p = z["plaus"]
    p["Q_ges_bis_Kontakt_1e-9"]["bestanden"] = bool(p["Q_ges_bis_Kontakt_1e-9"]["max_rel"] <= 1e-9)
    p["E_ges_bis_Kontakt_1e-4"]["bestanden"] = bool(p["E_ges_bis_Kontakt_1e-4"]["max_rel"] <= 1e-4)
    p["E_ges_steigt_nie_1e-6"]["bestanden"] = bool(p["E_ges_steigt_nie_1e-6"]["max_anstieg_rel"] <= 1e-6)
    p["omega_unter_1"]["bestanden"] = bool(not (p["omega_unter_1"]["max"] >= 1.0))
    p["buchfuehrung_1e-9"]["bestanden"] = bool(p["buchfuehrung_1e-9"]["max_rest_rel"] <= 1e-9)
    # nur Diagnose, nicht bindend: Anstieg ueber dem gleitenden Mittel (Breite 20 Messpunkte) statt Rohwerten
    k = 20
    if e_ges.numel() > 2 * k:
        gl = torch.nn.functional.avg_pool1d(e_ges.view(1, 1, -1), k, 1).view(-1)
        z["diagnose_E_glatt_anstieg_rel"] = teilen(gf((gl - torch.cummin(gl, 0).values).max()), abs(e0))
    ref = BI_R5D.get(stufe, {}).get(r["name"])
    z["V4_R5D_Q_win_T"] = ref
    z["V4_rel"] = teilen(abs(z["Q_win_T"] - ref), abs(ref)) if ref is not None else float("nan")
    z["V4_bestanden"] = bool(ref is not None and z["V4_rel"] <= 1e-6) if faktor == 1.0 else None
    return z


def bi_pruefen_haupt(zz):
    by = {round(z["omega2"], 6): z for z in zz}
    v1 = {w: abs(by[w]["spaet"]["R_EQ_zu_omega"] - 1.0) <= 0.05 for w in (0.6, 0.7, 0.8)}
    v2 = {w: bool(by[w]["ball_ganz"]["bestanden"] and abs(by[w]["dQ_schale_T_rel"]) <= 0.05)
          for w in (0.6, 0.7, 0.8, 0.9)}
    v3 = {w: bool(abs(by[w]["frueh"]["R_EQ_zu_omega"] - 1.0) <= 0.05 and by[w]["ball_frueh"]["bestanden"])
          for w in (0.51, 0.55)}
    v4 = [z["V4_bestanden"] for z in zz]
    plaus = all(v["bestanden"] for z in zz for v in z["plaus"].values())
    return {"V1": v1, "V2": v2, "V3": v3, "V4": v4, "plausibilitaet_bestanden": plaus,
            "scheitert": (not all(v1.values())) or (not all(v2.values())) or (not all(v3.values())),
            "nicht_entscheidbar": (not plaus) or any(v is False for v in v4)}


def bi_pruefen_gegen(zz):
    aus = {}
    for z in zz:
        if z["art"] == "schwer":
            g_ref, _ = al_vorhersage(z["omega2"], AL_EPS)
            ok = abs(z["Gamma_fit"]) < 1e-2 * g_ref and z["Q_abs_T"] < 1e-3 * abs(z["Q0"])
            aus[z["name"]] = {"Gamma_fit": z["Gamma_fit"], "grenze": 1e-2 * g_ref, "Q_abs_T": z["Q_abs_T"],
                              "bestanden": bool(ok)}
        else:
            ok = (abs(z["Gamma_fit"]) < 1e-7 and abs(z["Q_abs_T"]) < 1e-7 * abs(z["Q0"])
                  and z["ball_ganz"]["Q_neg_min"] >= -1e-9)
            aus[z["name"]] = {"Gamma_fit": z["Gamma_fit"], "Q_abs_T": z["Q_abs_T"],
                              "Q_neg_min": z["ball_ganz"]["Q_neg_min"], "bestanden": bool(ok)}
    plaus = all(v["bestanden"] for z in zz for v in z["plaus"].values())
    return {"gegenproben": aus, "alle_bestanden": all(v["bestanden"] for v in aus.values()),
            "plausibilitaet_bestanden": plaus}


def bi_test(teil, faktor):
    laeufe = bi_laeufe(teil)
    name = "bilanz" if teil == "haupt" else "bilanz_gegen"
    stufen = bi_rechnen(laeufe, faktor, name)
    erg, pruef = {}, {}
    for s, st in stufen.items():
        erg[s] = [bi_zeile(r, st["t"], st["daten"][:, b, :], s, faktor) for b, r in enumerate(laeufe)]
        pruef[s] = bi_pruefen_haupt(erg[s]) if teil == "haupt" else bi_pruefen_gegen(erg[s])
        if faktor != 1.0:
            pruef[s]["hinweis"] = "Zeitfaktor != 1 (Formprobe): Pruefung nur Durchlauf, Zahlen ungueltig"
    l3_liste = []
    for zg, zf in zip(erg["grob"], erg["fein"]):
        if zg["art"] == "masselos":
            l3_liste.append({"lauf": zg["name"], "Gamma": l3(zg["Gamma_fit"], zf["Gamma_fit"], 0.0),
                             "R_EQ": l3(zg["spaet"]["R_EQ"], zf["spaet"]["R_EQ"], 0.0),
                             "R_EQ_auf_1pz": {"bestanden": bool(abs(zf["spaet"]["R_EQ"] - zg["spaet"]["R_EQ"])
                                                                <= 0.01 * abs(zg["spaet"]["R_EQ"]))}})
    return {"laeufe": laeufe, "ergebnis": erg, "pruefung": pruef, "L3": l3_liste,
            "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def bericht_bilanz(res):
    zz = [f"bilanz (G2-02): wie altern (eps = {AL_EPS}, mc2 = eps^2, T = {AL_T:g} x Faktor), Fenster |x| < {AL_FENSTER:g}, "
          f"Schale bis {BI_SCHALE:g}, Schwamm dahinter; geschluckt = Gesamt(0) - Gesamt(t). R_EQ = Steigung E_win / "
          "Steigung Q_win; omega_quer = Mittel omega(t) am Maximum. spaet = [T/4, T], frueh = [T/4, T/2].",
          "  Lauf | Q0 | Q_win T (psi, chi, neg) | Schale T | geschluckt Q, E | x_max T | S_max 0 -> T | "
          "|x| 0 -> T | Gamma fit / Formel | R_EQ/omega spaet, frueh | t_Ereignis | V4 rel"]
    for stufe in ("grob", "fein"):
        if stufe not in res["ergebnis"]:
            continue
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]:
            zz.append(f"  {z['name']:32s} | {z['Q0']:.5f} | {z['Q_win_T']:+.5f} ({z['Q_psi_win_T']:+.4f}, "
                      f"{z['Q_chi_win_T']:+.4f}, {z['Q_neg_win_T']:+.2e}) | {z['Q_schale_T']:+.4f} | "
                      f"{z['Q_abs_T']:+.4f}, {z['E_abs_T']:+.4f} | {z['x_max_T']:+.2f} | {z['S_max_0']:.4f} -> "
                      f"{z['S_max_T']:.4f} | {z['x_betrag_0']:.2f} -> {z['x_betrag_T']:.2f} | "
                      f"{z['Gamma_fit']:+.3e} / {z['Gamma_formel']:.3e} | {z['spaet']['R_EQ_zu_omega']:.4f}, "
                      f"{z['frueh']['R_EQ_zu_omega']:.4f} | {z['t_ereignis']:.1f} | {z['V4_rel']:.1e}")
        for z in res["ergebnis"][stufe]:
            zz.append(f"    Plausibilitaet {z['name']}: " + "; ".join(
                f"{k} {'ok' if v['bestanden'] else 'NICHT'} (" + ", ".join(f"{n} {w:.2e}" for n, w in v.items()
                                                                        if n != "bestanden") + ")"
                for k, v in z["plaus"].items()) + f"; Diagnose E glatt {z.get('diagnose_E_glatt_anstieg_rel', float('nan')):.1e}")
        zz.append(f"  Pruefung [{stufe}]: {json.dumps(res['pruefung'][stufe], default=str)}")
    zz += [l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ tensid (Chemie 17)

def test_tensid(faktor):
    xw = 0.5 * fwhm(TS_W2)
    laeufe = [dict(r, mc2=1.0, kc=0.0) for r in TS_LAEUFE]

    def bauen(x, dx, par):
        felder = []
        for r in laeufe:
            p, vp = ball(x, 0.0, TS_W2)
            c = (r["A"] * (torch.exp(-0.5 * (x - xw) ** 2) + torch.exp(-0.5 * (x + xw) ** 2))).to(C128)
            felder.append((p, vp, c, -1j * TS_OM0 * c))
        fen = (x.abs() < TS_FENSTER).to(F64)
        band = ((x.abs() - xw).abs() < TS_BAND).to(F64)
        innen = (x.abs() < xw - TS_BAND).to(F64)
        rechts = (x > 0.0).to(F64)
        i0, iw = index_von(x, 0.0), index_von(x, xw)

        def messen(psi, vpsi, chi, vchi):
            s, c, rp, rc = ladungen(psi, vpsi, chi, vchi)
            e = energiedichte(psi, vpsi, chi, vchi, par, dx, False)
            n_ges = (c * fen).sum(1)
            nn = n_ges.clamp(min=1e-300)
            smax = s.max(dim=1).values.clamp(min=1e-300)
            p = (s / smax.unsqueeze(1)).clamp(0.0, 1.0)
            return torch.stack([(c * band).sum(1) / nn, (c * innen).sum(1) / nn,
                                (4.0 * p * (1.0 - p) * rechts).sum(1) * dx, (e * fen).sum(1) * dx,
                                (rp * fen).sum(1) * dx, (rc * fen).sum(1) * dx, n_ges * dx,
                                -torch.angle(psi[:, i0]), -torch.angle(chi[:, iw]), smax], dim=1)
        return stapel(felder, False), messen

    stufen = stufen_rechnen("tensid", laeufe, bauen, TS_T * faktor, TS_MESS)
    erg = {s: auswertung_tensid(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "Wandanteil": l3(zg["anteil_wand"], zf["anteil_wand"], erg["grob"][1]["anteil_wand"]),
                 "dw": l3(zg["dw"], zf["dw"], 0.0), "E_ads": l3(zg["E_ads"], zf["E_ads"], 0.0)}
                for zg, zf in zip(erg["grob"], erg["fein"]) if zg["lam"] != 0.0]
    a0, b0 = anker_ab(TS_W2)
    zwei_sigma_anker = math.sqrt(a0) - b0 * b0 * math.sqrt(2.0) * math.acosh(1.0 / b0) / 2.0
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "x_wand": xw, "zwei_sigma_anker": zwei_sigma_anker,
            "w_anker": 2.0 / math.sqrt(a0), "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def auswertung_tensid(laeufe, t, d):
    ih = ab_index(t, 0.5)
    tt = t[ih:]
    m = d[ih:].mean(dim=0)
    om_p = steigung(tt, entfalten(d[:, :, 7])[ih:])       # (B,)
    om_c = steigung(tt, entfalten(d[:, :, 8])[ih:])
    zeilen = []
    for b, r in enumerate(laeufe):
        wand, innen, w, e, qp, qc = [gf(v) for v in m[b, :6]]
        op, oc = gf(om_p[b]), gf(om_c[b])
        mit_chi = r["A"] > 0.0
        zeilen.append({"name": r["name"], "A": r["A"], "lam": r.get("lam", 0.0), "lam2": r.get("lam2", 0.0),
                       "anteil_wand": wand, "anteil_innen": innen, "w_wand": w, "E": e, "Q_psi": qp, "Q_chi": qc,
                       "N_chi_halt": teilen(gf(d[-1, b, 6]), gf(d[0, b, 6])), "omega_psi": op,
                       "omega_chi": oc if mit_chi else float("nan"),
                       "Omega_gross": e - op * qp - (oc * qc if mit_chi else 0.0)})
    nackt = zeilen[0]
    for z in zeilen:
        z["dOmega"] = z["Omega_gross"] - nackt["Omega_gross"]
        z["E_ads"] = z["E"] - nackt["E"] - 1.0 * z["Q_chi"]
        z["E_ads_linear"] = -(1.0 - z["omega_chi"]) * z["Q_chi"] if z["A"] > 0.0 else 0.0
        z["dw"] = z["w_wand"] - nackt["w_wand"]
    return zeilen


def bericht_tensid(res):
    zz = [f"tensid (Chemie 17): psi-Ball omega^2 = {TS_W2}, Waende bei +-{res['x_wand']:.3f}; chi frei (Masse 1) als "
          f"Pakete an beiden Waenden, Kopplung C (lam S + lam2 S^2). Fenster [T/2, T]. Anker: 2 sigma = E - omega Q = "
          f"{res['zwei_sigma_anker']:.5f}, Wandbreite w = Int 4 p (1 - p) dx = {res['w_anker']:.4f}.",
          "  Lauf | Wand- / Innenanteil chi | chi gehalten | w (dw) | omega_psi | omega_chi | Omega = E - Sum omega Q "
          "(dOmega) | E_ads (linear)"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]:
            zz.append(f"  {z['name']:24s} | {z['anteil_wand']:.3f} / {z['anteil_innen']:.3f} | {z['N_chi_halt']:.3f} | "
                      f"{z['w_wand']:.4f} ({z['dw']:+.2e}) | {z['omega_psi']:.6f} | {z['omega_chi']:.5f} | "
                      f"{z['Omega_gross']:.5f} ({z['dOmega']:+.2e}) | {z['E_ads']:+.3e} ({z['E_ads_linear']:+.3e})")
    zz += [l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ kreuzen (Wellen 10)

def kz_medium():
    """omega_0^2 = U_chi'(C0), g = U_chi''(C0) C0 und Schallgeschwindigkeit c_s = sqrt(g/(2 omega_0^2 + g))."""
    om2 = 1.0 + 2.0 * KZ_G4 * KZ_C0
    g = 2.0 * KZ_G4 * KZ_C0
    return om2, g, math.sqrt(g / (2.0 * om2 + g))


def test_kreuzen(faktor):
    om2, g, c_s = kz_medium()
    laeufe = []
    for r in KZ_LAEUFE:
        k = 2.0 * PI * r["n"] / (2.0 * L_BOX)
        laeufe.append(dict(r, mc2=1.0, kc=0.0, g4=KZ_G4, k=k, u=k / math.sqrt(k * k + om2)))

    def bauen(x, dx, par):
        felder = []
        for r in laeufe:
            om = math.sqrt((2.0 - 2.0 * math.cos(r["k"] * dx)) / (dx * dx) + om2)   # exakte Gitter-Loesung
            c = math.sqrt(KZ_C0) * torch.exp(1j * r["k"] * x)
            p = leer(x) if r.get("ohne_ball") else ball(x, 0.0, KZ_W2)
            felder.append(p + (c, -1j * om * c))
        n = x.shape[0]

        def messen(psi, vpsi, chi, vchi):
            s, c, rp, rc = ladungen(psi, vpsi, chi, vchi)
            xb, sb = spitze(x, s)
            ib = ((xb - x[0]) / dx).round().long().clamp(0, n - 1).unsqueeze(1)
            return torch.stack([xb, sb, c.gather(1, ib).squeeze(1), rp.sum(1) * dx, rc.sum(1) * dx,
                                c.min(dim=1).values, c.max(dim=1).values], dim=1)
        return stapel(felder, True), messen

    stufen = stufen_rechnen("kreuzen", laeufe, bauen, KZ_T * faktor, KZ_MESS, periodisch=True)
    erg = {s: auswertung_kreuzen(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "a_spaet": l3(zg["a_spaet"], zf["a_spaet"], 0.0),
                 "v_ende": l3(zg["v_ende"], zf["v_ende"], 0.0)}
                for zg, zf in zip(erg["grob"], erg["fein"]) if not zg["ohne_ball"] and zg["n"] != 0 and zg["lam"] != 0.0]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "omega0_quadrat": om2, "g": g, "c_s": c_s,
            "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def auswertung_kreuzen(laeufe, t, d):
    i3 = ab_index(t, 1.0 / 3.0)
    zeilen = []
    for b, r in enumerate(laeufe):
        xb = d[:, b, 0]
        sprung = torch.remainder(xb[1:] - xb[:-1] + L_BOX, 2.0 * L_BOX) - L_BOX
        xu = torch.cat([xb[:1], xb[:1] + torch.cumsum(sprung, dim=0)])      # Ort ohne periodische Spruenge
        zeilen.append({"name": r["name"], "n": r["n"], "u": r["u"], "lam": r["lam"],
                       "ohne_ball": bool(r.get("ohne_ball", False)), "verschiebung": gf(xu[-1] - xu[0]),
                       "v_ende": gf(steigung(t[i3:], xu[i3:])), "a_spaet": beschleunigung(t[i3:], xu[i3:]),
                       "S_ball_halt": teilen(gf(d[-1, b, 1]), gf(d[0, b, 1])), "C_am_ball_ende": gf(d[-1, b, 2]),
                       "C_min_ende": gf(d[-1, b, 5]), "C_max_ende": gf(d[-1, b, 6]),
                       "Q_psi_halt": teilen(gf(d[-1, b, 3]), gf(d[0, b, 3])),
                       "Q_chi_halt": teilen(gf(d[-1, b, 4]), gf(d[0, b, 4]))})
    return zeilen


def bericht_kreuzen(res):
    zz = [f"kreuzen (Wellen 10, 1D-Baustein): psi-Ball omega^2 = {KZ_W2} ruhend in stroemendem chi-Medium C0 = {KZ_C0}, "
          f"U_chi = C + {KZ_G4} C^2 (omega_0^2 = {res['omega0_quadrat']:.3f}, g = {res['g']:.3f}, Schall c_s = "
          f"{res['c_s']:.4f}); periodische Box. v und a aus Fits auf [T/3, T].",
          "  Lauf | u | u/c_s | lam | Verschiebung | v Ende | a spaet | S_Ball gehalten | C am Ball | C min .. max"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]:
            zz.append(f"  {z['name']:20s} | {z['u']:+.4f} | {z['u'] / res['c_s']:+.2f} | {z['lam']:.1f} | "
                      f"{z['verschiebung']:+.3f} | {z['v_ende']:+.2e} | {z['a_spaet']:+.2e} | {z['S_ball_halt']:.4f} | "
                      f"{z['C_am_ball_ende']:.4f} | {z['C_min_ende']:.6f} .. {z['C_max_ende']:.6f}")
    zz += [l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ Hauptprogramm

TESTS = {
    "zellkern": (test_zellkern, bericht_zellkern, ZK_SPALTEN),
    "raeuber": (test_raeuber, bericht_raeuber, RB_SPALTEN),
    "mitochondrium": (test_mitochondrium, bericht_mitochondrium, MT_SPALTEN),
    "altern": (test_altern, bericht_altern, AL_SPALTEN),
    "tensid": (test_tensid, bericht_tensid, TS_SPALTEN),
    "kreuzen": (test_kreuzen, bericht_kreuzen, KZ_SPALTEN),
    "bilanz": (lambda f: bi_test("haupt", f), bericht_bilanz, BI_SPALTEN),          # G2-02
    "bilanz_gegen": (lambda f: bi_test("gegen", f), bericht_bilanz, BI_SPALTEN),    # G2-02
}


def schreiben(out, name, ausgabe, text, reihen):
    """Stand nach jedem Test sichern; bricht der Lauf ab (RuntimeMaxSec), bleiben die fertigen Tests erhalten."""
    basis = os.path.join(out, f"r5d_{name}")
    with open(basis + "_bericht.txt", "w") as fh:
        fh.write("\n".join(text) + "\n")
    torch.save(reihen, basis + "_reihen.pt")
    with open(basis + "_ergebnis.json", "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)


def main():
    global DEV
    ap = argparse.ArgumentParser(description="Runde 5, R5-D: 1D mit zwei komplexen Feldern psi und chi")
    ap.add_argument("unterbefehl", choices=["rauch"] + list(TESTS))
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None, help="Ausgabeordner (Vorgabe ./ausgabe-<unterbefehl>)")
    ap.add_argument("--faktor", type=float, default=None, help="G2-02: Zeitfaktor (Vorgabe 1, rauch 0,05; Formprobe klein)")
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber keine CUDA-Karte sichtbar: Abbruch (kein stiller CPU-Ausweg).")
        DEV = torch.device("cuda")
        gesamt = torch.cuda.get_device_properties(0).total_memory
        torch.cuda.set_per_process_memory_fraction(min(1.0, SPEICHER_GB * 2 ** 30 / gesamt))
        name_geraet = torch.cuda.get_device_name(0)
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(1)
        name_geraet = "CPU, 1 Thread"
    out = args.out or os.path.join(os.getcwd(), "ausgabe-" + args.unterbefehl)
    os.makedirs(out, exist_ok=True)
    rauch = args.unterbefehl == "rauch"
    faktor = args.faktor if args.faktor is not None else (RAUCH_FAKTOR if rauch else 1.0)
    auswahl = list(TESTS) if rauch else [args.unterbefehl]
    start = jetzt()
    t_start = time.perf_counter()
    kopf = (f"Runde 5 R5-D r5d.py {args.unterbefehl} Start {start} auf {name_geraet}, torch {torch.__version__}, "
            f"Laufzeitfaktor {faktor}")
    print(kopf, flush=True)
    ausgabe = {"start": start, "geraet": name_geraet, "torch": torch.__version__, "unterbefehl": args.unterbefehl,
               "faktor": faktor, "ergebnisse": {}, "fehler": {}}
    text = [kopf, ""]
    reihen = {}
    for name in auswahl:
        funk, ber, spalten = TESTS[name]
        try:
            res, stufen = funk(faktor)
            ausgabe["ergebnisse"][name] = res
            reihen[name] = {"laeufe": res["laeufe"], "spalten": spalten,
                            "stufen": {s: {k: (v.cpu() if torch.is_tensor(v) else v) for k, v in st.items()}
                                       for s, st in stufen.items()}}
            text += ber(res) + [""]
        except Exception:
            ausgabe["fehler"][name] = traceback.format_exc()
            text += [f"{name} FEHLER:", ausgabe["fehler"][name], ""]
            print(ausgabe["fehler"][name], flush=True)
        schreiben(out, args.unterbefehl, ausgabe, text, reihen)
    ausgabe["ende"] = jetzt()
    ausgabe["dauer_s"] = time.perf_counter() - t_start
    speicher = torch.cuda.max_memory_allocated() / 2 ** 20 if DEV.type == "cuda" else float("nan")
    ausgabe["torch_speicher_max_mb"] = speicher
    text.append(f"Ende {ausgabe['ende']}, Dauer {ausgabe['dauer_s']:.1f} s, Torch-Speicher max {speicher:.0f} MB, "
                f"Fehler in: {sorted(ausgabe['fehler']) if ausgabe['fehler'] else 'keine'}")
    schreiben(out, args.unterbefehl, ausgabe, text, reihen)
    print("\n".join(text), flush=True)
    if ausgabe["fehler"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
