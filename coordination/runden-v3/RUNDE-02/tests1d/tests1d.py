#!/usr/bin/env python3
"""Runde 2 (runden-v3): vier kleine Tests zu Q-Ball-Ideen. Explorativ. Ungetestet abgegeben (Interpreterverbot auf dem
Laptop); Plan, Aufruf, Vorhersagen und Latten stehen in PLAN-1D.md daneben. Nur CUDA, float64 (psi als complex128).

Modell wie QG-1 ohne Feld: L = |psi_t|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2, 1/2 < omega^2 < 1.
Bewegungsgleichung psi_tt = psi_xx - U'(S) psi. Ladungsdichte rho = 2 Im(psi conj(psi_t)), Ladungsfluss
j = -2 Im(psi conj(psi_x)), Energiedichte |psi_t|^2 + |psi_x|^2 + U, Energiefluss -2 Re(psi_t conj(psi_x)).

Aus RUNDE-01/qg1/qg1.py unveraendert uebernommen (dort auf der .69 geprueft: Profil gegen Anker 1,2e-10, K0 bis K4):
rhs, rk4, schiessen, profil_bahn, gitter, profil_gitter, profil_anker, anker_wgv, die Konstanten des Schiessens, der
Velocity-Verlet-Schritt mit dx = 0,1 und dt = 0,05 (fein dx/2, dt/2) und die quadratische Daempfungsschicht (sigma0 = 1,
40 breit). Geaendert: Box [-150, 150] statt [-120, 120], kein Brechungsfeld (A = B = C = 1).
Neu: Profil an beliebigen Orten (lineare Interpolation der Schiessbahn, fuer Lorentz-Boost), Messungen je Test und fuer
Test 4 ein radiales Schiessen mit der Abweichung u = f_top - f als Zustand (duenne Waende bis u0 ~ e^-150).

Tests:
  1  Idee 9/10: Uhren-Synchronisation (Kette aus fuenf Baellen; gross neben klein)
  2  Idee 32:   Absorptionsspektrum (schwache Wellenpakete nu = 1,125 ... 2,5 an einem Ball omega^2 = 0,7)
  3  Idee 33:   Virus (kleiner Ball 0,90 laeuft in grossen 0,55; Phasenabtastung; Modenspektrum vorher und nachher)
  4  Idee 31:   Gedaechtnis (3D radial: Q(omega), E(omega), Q_min, Vorzeichen von dQ/domega)

Aufruf:  python tests1d.py [--tests 1234] [--rauch] [--profil DATEI] [--out ORDNER]
  --rauch   Laufzeiten mal 0,05 und in Test 4 nur eine Schiessrunde: prueft nur, ob alles durchlaeuft.
  --profil  1D-Schiessbahnen aus einem frueheren Lauf laden (profil_1d.pt), spart das Schiessen (P5000: 84 s).
Rechenort seit 30.09. 01:31: Quadro P4000 ueber kleintests/kleintest.sh (Aufruf in PLAN-1D.md), Torch-Speicher
hoechstens SPEICHER_GB; Bericht, JSON und Zeitreihen werden nach jedem Test neu geschrieben.
"""
import argparse
import datetime
import json
import math
import os
import time
import traceback

import torch

DEV = torch.device("cuda")
F64 = torch.float64
PI = math.pi

# ---- aus qg1.py unveraendert ----
SIGMA0 = 1.0             # Daempfung am Rand
DX, DT = 0.1, 0.05       # grobe Aufloesung; die feine halbiert beide
H_ODE = 0.01             # Schrittweite beim Schiessen (teilt DX und DX/2)
X_ODE = 80.0             # Schiesslaenge
N_KAND, RUNDEN = 4096, 4 # Kandidaten je Einschachtelungsrunde, Zahl der Runden
SCHWANZ = 1e-3           # ab f < SCHWANZ * f(0): exponentieller Schwanz statt Schiessbahn
TOL_PROFIL = 1e-6        # K0: max |f_Schuss - f_Anker| auf dem Gitter

# ---- Runde 2, gemeinsam ----
L_BOX = 150.0            # Box [-L, L], Dirichlet-Rand (QG-1: 120)
X_SPONGE = 110.0         # Daempfungsschicht fuer |x| > X_SPONGE, 40 breit wie in QG-1
FEIN = 0.5               # feine Stufe: dx und dt mal FEIN (Latte L3, enthaelt den halben Zeitschritt)
ETA_STOSS = 0.01         # kleiner Stoss: psi und psi_t eines ruhenden Balls mal (1 + ETA_STOSS)
SPEICHER_GB = 2.5        # Obergrenze fuer den Torch-Speicher auf der Karte (P4000, Vorgabe der Leitung 30.09.)

# ---- Test 1: Uhren ----
T1, T1_MESS = 400.0, 0.5
W2_KETTE = [0.695, 0.710, 0.700, 0.690, 0.705]           # omega^2 = 0,70 +- 0,01, feste Reihenfolge
PHASEN_KETTE = {"gleich": [0.0] * 5, "wechselnd": [0.0, PI, 0.0, PI, 0.0],
                "zufall": [(2.39996 * j) % (2.0 * PI) for j in range(5)]}   # goldener Winkel, fest
D_KETTE = [8.0, 11.0, 14.0]   # 8,0 = 1,12 x doppelte Halbwertsbreite von |psi|^2 bei 0,70 (7,12)
D_KONTROLLE = 30.0           # Gegenprobe ohne Kopplung (Auslaeufer dort ~ 1e-7)
W2_PAAR = (0.55, 0.80)        # gross, klein
D_PAAR = 8.6                 # 1,13 x (FWHM(0,55) + FWHM(0,80)) = 1,13 x 7,63
PHASEN_PAAR = [0.0, 0.5 * PI, PI, 1.5 * PI]
R_SYNC = 0.9                 # Schwelle: Kuramoto-r, gemittelt ueber das letzte Viertel

# ---- Test 2: Absorption ----
W2_ZIEL = 0.70
NU_LISTE = [1.125 + 0.125 * j for j in range(12)]       # nu = 1,0 laeuft nicht (Gruppengeschwindigkeit 0)
EPS_PAKET, SIGMA_PAKET, X0_PAKET = 1e-3, 8.0, -65.0
X_EBENE = 30.0               # Flussebenen bei x = -30 und +30
T2, T2_MESS = 500.0, 0.1

# ---- Test 3: Virus ----
W2_GROSS, W2_KLEIN = 0.55, 0.90
X_KLEIN0, V_KLEIN = -24.0, 0.1
T3, T3_MESS = 600.0, 0.5
W_KLUMPEN = 10.0             # Fenster +-10 um das Maximum von |psi|^2
PHASEN_KONTAKT = [0.25 * PI * j for j in range(8)]      # Soll-Phasendifferenz beim freien Kontakt

# ---- Test 4: Gedaechtnis, 3D radial ----
W2_3D = [round(0.51 + 0.01 * i, 2) for i in range(49)]
W2_1D_KONTROLLE = [0.55, 0.70, 0.90]                    # gleiches Verfahren in d = 1 gegen den Anker
H3, X3 = 0.05, 150.0
N_KAND3, RUNDEN3 = 1024, 4
S_MAX3 = 150.0               # Schiessparameter s = -ln(f_top - f(0)) in [s_min, 150]


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    torch.cuda.synchronize()
    return time.perf_counter()


# ---------------------------------------------------------------- aus qg1.py: Profil durch Schiessen

def rhs(f, fp, a0):
    """f'' = (U'(f^2) - omega^2) f = (a0 - 2 f^2 + 1.5 f^4) f,  a0 = 1 - omega^2."""
    s = f * f
    return fp, (a0 - 2.0 * s + 1.5 * s * s) * f


def rk4(f, fp, a0, h):
    k1f, k1p = rhs(f, fp, a0)
    k2f, k2p = rhs(f + 0.5 * h * k1f, fp + 0.5 * h * k1p, a0)
    k3f, k3p = rhs(f + 0.5 * h * k2f, fp + 0.5 * h * k2p, a0)
    k4f, k4p = rhs(f + h * k3f, fp + h * k3p, a0)
    return (f + (h / 6.0) * (k1f + 2.0 * k2f + 2.0 * k3f + k4f),
            fp + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p))


def schiessen(a0):
    """Zentralwert f(0) je omega durch Einschachteln, alle omega und Kandidaten gleichzeitig.

    a0 hat die Form (n_om, 1). Start in Ruhe bei f(0). Ueberschuss: f wird negativ.
    Unterschuss: f' wird positiv, bevor f null erreicht. Rueckgabe: f(0) und Klammerbreite, je (n_om, 1)."""
    n_om = a0.shape[0]
    lo = torch.full((n_om, 1), 1e-3, dtype=F64, device=DEV)   # sicher Unterschuss
    hi = torch.ones((n_om, 1), dtype=F64, device=DEV)         # S = 1: sicher Ueberschuss
    stufen = torch.linspace(0.0, 1.0, N_KAND, dtype=F64, device=DEV)
    n_schritte = int(round(X_ODE / H_ODE))
    for _ in range(RUNDEN):
        f0 = lo + (hi - lo) * stufen                           # (n_om, N_KAND)
        f, fp = f0.clone(), torch.zeros_like(f0)
        zustand = torch.zeros_like(f0)                         # 0 offen, +1 Ueberschuss, -1 Unterschuss
        for _ in range(n_schritte):
            f, fp = rk4(f, fp, a0, H_ODE)
            ueber = (zustand == 0) & (f < 0)
            unter = (zustand == 0) & (f >= 0) & (fp > 0)
            zustand = zustand + ueber.to(F64) - unter.to(F64)
            lebt = (zustand == 0).to(F64)
            f = f * lebt                                       # entschiedene Kandidaten einfrieren
            fp = fp * lebt
        lo = torch.where(zustand < 0, f0, torch.zeros_like(f0)).max(dim=1, keepdim=True).values
        hi = torch.where(zustand > 0, f0, torch.full_like(f0, 2.0)).min(dim=1, keepdim=True).values
    return 0.5 * (lo + hi), hi - lo


def profil_bahn(f0, a0):
    """Schiessbahn f(j h) ab f(0) = f0, bis f unter SCHWANZ * f0 faellt; danach eingefroren.

    Rueckgabe: Bahn (n_om, n+1) und j_cut (n_om, 1), der erste Index unter der Schwelle."""
    n_schritte = int(round(X_ODE / H_ODE))
    f, fp = f0.clone(), torch.zeros_like(f0)
    schwelle = SCHWANZ * f0
    steigt = torch.zeros_like(f0, dtype=torch.bool)
    bahn = [f]
    for _ in range(n_schritte):
        weiter = f >= schwelle
        f_neu, fp_neu = rk4(f, fp, a0, H_ODE)
        steigt = steigt | (weiter & (fp_neu > 0))
        f = torch.where(weiter, f_neu, f)
        fp = torch.where(weiter, fp_neu, fp)
        bahn.append(f)
    if bool(steigt.any()):
        raise RuntimeError("Schiessbahn steigt vor dem Schwanz wieder an: f(0) zu ungenau")
    bahn = torch.cat(bahn, dim=1)
    j_cut = (bahn >= schwelle).sum(dim=1, keepdim=True)
    if bool((j_cut > n_schritte).any()):
        raise RuntimeError("Schwanzschwelle innerhalb X_ODE nicht erreicht")
    return bahn, j_cut


def gitter(dx):
    """Symmetrisches Gitter x_i = (i - i0) dx auf [-L, L]; x = 0 liegt genau auf einem Punkt."""
    i0 = int(round(L_BOX / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx


def profil_gitter(bahn, j_cut, a0, dx):
    """Geschossenes Profil auf dem Gitter: gespiegelt, jenseits der Schwelle f_cut exp(-sqrt(a0)(|x| - x_cut))."""
    m = int(round(dx / H_ODE))
    i0 = int(round(L_BOX / dx))
    k = (torch.arange(2 * i0 + 1, device=DEV) - i0).abs()           # |x| / dx
    j = (k * m).unsqueeze(0).repeat(bahn.shape[0], 1)               # Index in der Schiessbahn
    innen = bahn.gather(1, j.clamp(max=bahn.shape[1] - 1))
    f_cut = bahn.gather(1, j_cut)
    aussen = f_cut * torch.exp(-torch.sqrt(a0) * (j - j_cut).to(F64) * H_ODE)
    f = torch.where(j < j_cut, innen, aussen)
    f[:, 0] = 0.0                                                   # Dirichlet-Rand
    f[:, -1] = 0.0
    return f


def profil_anker(w2, dx):
    """Analytischer 1D-Anker (nur Kontrolle): f^2 = 2 a0 / (1 + b0 cosh(2 sqrt(a0) x))."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    x = gitter(dx)
    return torch.sqrt(2.0 * a0 / (1.0 + b0 * torch.cosh(2.0 * math.sqrt(a0) * x)))


def anker_wgv(w2):
    """Geschlossene 1D-Werte: I = sqrt(2) arcosh(1/b0), W = omega^2 I, G = sqrt(a0)/2 - b0^2 I/4, V = W + G."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    integral = math.sqrt(2.0) * math.acosh(1.0 / b0)
    w = w2 * integral
    g = math.sqrt(a0) / 2.0 - b0 * b0 * integral / 4.0
    return w, g, w + g


# ---------------------------------------------------------------- neu: Anker-Hilfen, Profile, Anfangsfelder

def anker_q_e(w2):
    """Q und E des 1D-Ankers: Q = 2 W / omega, E = W + G + V."""
    w, g, v = anker_wgv(w2)
    return 2.0 * w / math.sqrt(w2), w + g + v


def anker_umkehr(q):
    """omega^2 des 1D-Ankers mit der Ladung q (Q faellt mit omega^2), durch Einschachteln."""
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
    """Volle Halbwertsbreite von |psi|^2 des 1D-Ankers: arcosh((1 + 2 b0) / b0) / sqrt(a0)."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    return math.acosh((1.0 + 2.0 * b0) / b0) / math.sqrt(a0)


def w2_liste_1d():
    """Alle 1D-omega^2 der Tests 1 bis 3; der letzte Eintrag ist der Ersatzball mit Q = Q(0,55) + Q(0,90)."""
    q = anker_q_e(W2_GROSS)[0] + anker_q_e(W2_KLEIN)[0]
    basis = sorted(set([W2_ZIEL, W2_GROSS, W2_KLEIN] + W2_KETTE + list(W2_PAAR)))
    return basis + [round(anker_umkehr(q), 6)]


def profile_1d(w2_liste, laden, speichern):
    """Schiessbahnen aller 1D-omega (Schiessen aus qg1.py) oder aus einer frueheren Ausgabe."""
    if laden:
        alt = torch.load(laden, map_location=DEV, weights_only=False)
        if list(alt["w2"]) == list(w2_liste):
            print(f"1D-Profile geladen aus {laden}", flush=True)
            alt["geladen"] = laden
            return alt
        print("gespeicherte 1D-Profile passen nicht zur omega-Liste: neu schiessen", flush=True)
    a0 = (1.0 - torch.tensor(w2_liste, dtype=F64, device=DEV)).unsqueeze(1)
    f0, klammer = schiessen(a0)
    bahn, j_cut = profil_bahn(f0, a0)
    prof = {"w2": list(w2_liste), "a0": a0, "f0": f0, "klammer": klammer, "bahn": bahn, "j_cut": j_cut}
    torch.save(prof, speichern)
    prof["geladen"] = None
    return prof


def profil_an(prof, iw, xi):
    """f(|xi|) aus der Schiessbahn, linear interpoliert; ab der Schwanzschwelle exponentiell wie profil_gitter."""
    bahn = prof["bahn"][iw]
    jc = int(prof["j_cut"][iw, 0].item())
    k = torch.sqrt(prof["a0"][iw, 0])
    j = xi.abs() / H_ODE
    j0 = j.floor().clamp(max=bahn.shape[0] - 2)
    anteil = j - j0
    j0 = j0.long()
    innen = bahn[j0] * (1.0 - anteil) + bahn[j0 + 1] * anteil
    aussen = bahn[jc] * torch.exp(-k * (j - jc) * H_ODE)
    return torch.where(j < jc, innen, aussen)


def ball(prof, iw, x, xc, v=0.0, phase=0.0):
    """Q-Ball omega^2 = prof['w2'][iw] um xc mit Geschwindigkeit v (Lorentz-Boost) und Phase.

    psi = f(xi) exp(i(omega gamma v (x - xc) + phase)), xi = gamma (x - xc);
    psi_t = (-gamma v f'(xi) - i omega gamma f(xi)) exp(...). Phase am mitbewegten Zentrum: -arg psi = omega t / gamma - phase."""
    w = math.sqrt(prof["w2"][iw])
    gam = 1.0 / math.sqrt(1.0 - v * v)
    xi = gam * (x - xc)
    f = profil_an(prof, iw, xi)
    fp = (profil_an(prof, iw, xi + H_ODE) - profil_an(prof, iw, xi - H_ODE)) / (2.0 * H_ODE)
    ph = torch.exp(1j * (w * gam * v * (x - xc) + phase))
    return f * ph, (-gam * v * fp - 1j * w * gam * f) * ph


def paket(x, nu):
    """Schwaches Wellenpaket von links: eps exp(-(x-x0)^2/(2 sigma^2)) exp(i k (x - x0)), nu^2 = k^2 + 1, nach rechts."""
    k = math.sqrt(nu * nu - 1.0)
    vg = k / nu
    psi = EPS_PAKET * torch.exp(-((x - X0_PAKET) ** 2) / (2.0 * SIGMA_PAKET ** 2)) * torch.exp(1j * k * (x - X0_PAKET))
    return psi, (-1j * nu + vg * (x - X0_PAKET) / SIGMA_PAKET ** 2) * psi


def summe(teile):
    return sum(p for p, _ in teile), sum(v for _, v in teile)


def gestossen(feld):
    return (1.0 + ETA_STOSS) * feld[0], (1.0 + ETA_STOSS) * feld[1]


def stapel(felder):
    """Liste (psi, psi_t) je Lauf -> zwei (B, N)-Stapel mit Dirichlet-Rand."""
    psi = torch.stack([p for p, _ in felder])
    vel = torch.stack([v for _, v in felder])
    for a in (psi, vel):
        a[:, 0] = 0.0
        a[:, -1] = 0.0
    return psi, vel


# ---------------------------------------------------------------- Zeitentwicklung (Schritt aus qg1.py, ohne Feld)

def entwickeln(psi, vel, dx, dt, t_end, t_mess, messen):
    """Velocity-Verlet fuer alle Laeufe als ein Stapel (B x N); messen(psi, vel) -> (B, m) alle t_mess."""
    x = gitter(dx)
    sigma = SIGMA0 * ((x.abs() - X_SPONGE).clamp(min=0.0) / (L_BOX - X_SPONGE)) ** 2

    def kraft(psi):
        fluss = (psi[:, 1:] - psi[:, :-1]) / dx
        lap = torch.zeros_like(psi)
        lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = psi.real ** 2 + psi.imag ** 2
        return lap - (1.0 - 2.0 * s + 1.5 * s * s) * psi

    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(t_mess / dt)))
    reihe = [messen(psi, vel)]
    kr = kraft(psi)
    for n in range(1, n_schritte + 1):
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        psi = psi + dt * vel
        kr = kraft(psi)
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        if n % alle == 0:
            reihe.append(messen(psi, vel))
    daten = torch.stack(reihe)                   # (M, B, m)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
    return t, daten


def stufen_rechnen(name, bauen, t_end, t_mess):
    """Grob (dx, dt) und fein (dx/2, dt/2). bauen(x, dx) -> (psi, vel, messen)."""
    aus = {}
    for stufe, dx, dt in (("grob", DX, DT), ("fein", DX * FEIN, DT * FEIN)):
        x = gitter(dx)
        psi, vel, messen = bauen(x, dx)
        t0 = uhr()
        t, daten = entwickeln(psi, vel, dx, dt, t_end, t_mess, messen)
        sek = uhr() - t0
        print(f"{name} {stufe}: {psi.shape[0]} Laeufe x {psi.shape[1]} Punkte, T = {t_end}, {sek:.1f} s", flush=True)
        aus[stufe] = {"t": t, "daten": daten, "sek": sek}
    return aus


# ---------------------------------------------------------------- Auswerte-Hilfen

def wrap(a):
    """Winkel nach [-pi, pi)."""
    return torch.remainder(a + PI, 2.0 * PI) - PI


def entfalten(th):
    """Phasenreihe (M, ...) stetig machen; Schritte muessen unter pi liegen (omega * t_mess < pi)."""
    return torch.cat([th[:1], th[:1] + torch.cumsum(wrap(th[1:] - th[:-1]), dim=0)], dim=0)


def breite_s(x, s, maske):
    """Standardabweichung von |psi|^2 im Fenster (|psi|^2 statt rho: immer positiv)."""
    m = (s * maske).sum(1).clamp(min=1e-300)
    mitte = (x * s * maske).sum(1) / m
    return torch.sqrt(((x - mitte.unsqueeze(1)) ** 2 * s * maske).sum(1) / m)


def integral(t, y):
    """Trapezregel ueber die Zeit, y (M, B) -> (B,)."""
    return 0.5 * ((y[1:] + y[:-1]) * (t[1:] - t[:-1]).unsqueeze(1)).sum(0)


def spektrum(t, y, t_ab, n_spitzen=3):
    """Groesste Spitzen der FFT von y ab t_ab (linearer Trend entfernt, Hann-Fenster), Kreisfrequenz Omega."""
    wahl = t >= t_ab - 1e-9
    ts, ys = t[wahl], y[wahl]
    n = ys.shape[0]
    if n < 16:
        return []
    tau = ts - ts[0]
    a_mat = torch.stack([torch.ones_like(tau), tau], dim=1)
    koef = torch.linalg.lstsq(a_mat, ys.unsqueeze(1)).solution
    rest = ys - (a_mat @ koef).squeeze(1)
    fen = torch.hann_window(n, periodic=False, dtype=F64, device=DEV)
    amp = torch.fft.rfft(rest * fen).abs()
    d_om = 2.0 * PI / (n * (ts[1] - ts[0]).item())
    lok = (amp[1:-1] > amp[:-2]) & (amp[1:-1] >= amp[2:])
    kand = torch.nonzero(lok).squeeze(1) + 1
    kand = kand[kand >= 2]
    kand = kand[amp[kand].argsort(descending=True)][:n_spitzen]
    aus = []
    for k in kand.tolist():
        a, b, c = amp[k - 1].item(), amp[k].item(), amp[k + 1].item()
        nenner = a - 2.0 * b + c
        delta = 0.5 * (a - c) / nenner if nenner != 0.0 else 0.0
        aus.append({"Omega": (k + delta) * d_om, "amplitude": 2.0 * b / fen.sum().item()})
    return aus


def spitzen_text(sp):
    return ", ".join(f"{s['Omega']:.4f} ({s['amplitude']:.1e})" for s in sp) if sp else "-"


def l3(wert_grob, wert_fein, null):
    """Latte L3: Effekt (Abstand vom Nullwert) mindestens fuenfmal so gross wie die Aenderung grob -> fein."""
    eff, aend = abs(wert_grob - null), abs(wert_fein - wert_grob)
    return {"effekt": eff, "aenderung": aend, "bestanden": bool(eff >= 5.0 * aend)}


def gf(v):
    return float(v.item()) if torch.is_tensor(v) else float(v)


def teilen(a, b):
    return a / b if b != 0.0 else float("nan")


# ---------------------------------------------------------------- Test 1: Uhren-Synchronisation

def test1(prof, faktor):
    iw = {w2: i for i, w2 in enumerate(prof["w2"])}
    laeufe = []
    for d in D_KETTE + [D_KONTROLLE]:
        for name, ph in PHASEN_KETTE.items():
            laeufe.append({"teil": "a", "D": d, "phasen": name,
                           "baelle": [(W2_KETTE[j], (j - 2) * d, ph[j]) for j in range(5)]})
    for d in (D_PAAR, D_KONTROLLE):
        for ph in PHASEN_PAAR:
            laeufe.append({"teil": "b", "D": d, "phasen": round(ph, 6),
                           "baelle": [(W2_PAAR[0], -0.5 * d, 0.0), (W2_PAAR[1], 0.5 * d, ph)]})

    def bauen(x, dx):
        felder = [summe([ball(prof, iw[w2], x, xc, 0.0, ph) for w2, xc, ph in r["baelle"]]) for r in laeufe]
        psi, vel = stapel(felder)
        i0 = int(round(L_BOX / dx))
        start = []
        for r in laeufe:
            s = [i0 + int(round(xc / dx)) for _, xc, _ in r["baelle"]]
            start.append(s + [s[-1]] * (5 - len(s)))          # Paare: Tracker 3 bis 5 doppeln den kleinen Ball
        zentren = torch.tensor(start, device=DEV)
        w = int(round(1.0 / dx))
        off = torch.arange(-w, w + 1, device=DEV)
        n_b, n_x = psi.shape

        def messen(psi, vel):
            s = psi.real ** 2 + psi.imag ** 2
            idx = (zentren.unsqueeze(-1) + off).clamp(0, n_x - 1)                 # (B, 5, 2w+1)
            werte = s.gather(1, idx.reshape(n_b, -1)).reshape(n_b, 5, -1)
            neu = idx.gather(2, werte.argmax(dim=2, keepdim=True)).squeeze(2)     # (B, 5)
            zentren.copy_(neu)
            p = psi.gather(1, neu)
            return torch.cat([x[neu], -torch.angle(p), p.abs() ** 2], dim=1)     # Ort, Phase, |psi|^2
        return psi, vel, messen

    stufen = stufen_rechnen("Test 1", bauen, T1 * faktor, T1_MESS)
    ergebnis = {}
    for stufe, st in stufen.items():
        ergebnis[stufe] = auswertung1(laeufe, st["t"], st["daten"])
    # L3 je gekoppeltem Lauf
    l3_liste = []
    for zg, zf in zip(ergebnis["grob"], ergebnis["fein"]):
        if zg["D"] == D_KONTROLLE:
            continue
        if zg["teil"] == "a":
            l3_liste.append({"lauf": zg["name"], "r": l3(zg["effekt_r"], zf["effekt_r"], 0.0),
                             "sigma": l3(zg["sigma_verh"], zf["sigma_verh"], 1.0)})
        else:
            l3_liste.append({"lauf": zg["name"], "mitnahme": l3(zg["mitnahme"], zf["mitnahme"], 1.0)})
    return {"laeufe": laeufe, "ergebnis": ergebnis, "L3": l3_liste,
            "fwhm": {"0.70": fwhm(0.70), "0.55": fwhm(0.55), "0.80": fwhm(0.80)},
            "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def auswertung1(laeufe, t, daten):
    T = t[-1].item()
    pos, th, amp = daten[:, :, 0:5], daten[:, :, 5:10], daten[:, :, 10:15]
    thu = entfalten(th)
    ia = max(1, int((t <= 0.1 * T + 1e-9).sum().item()) - 1)     # Anfangsfenster [0, T/10]
    ie = min(len(t) - 2, int((t < 0.75 * T - 1e-9).sum().item()))  # Endfenster [3T/4, T]
    zeilen = []
    for b, r in enumerate(laeufe):
        k = len(r["baelle"])

        def fenster(m1, m2):
            dauer = (t[m2] - t[m1]).item()
            om = (thu[m2, b, :k] - thu[m1, b, :k]) / dauer
            v = ((pos[m2, b, :k] - pos[m1, b, :k]) / dauer).clamp(-0.99, 0.99)
            return om / torch.sqrt(1.0 - v * v), v                  # Eigenfrequenz gamma * omega_mess, Geschwindigkeit

        eig_a, _ = fenster(0, ia)
        eig_e, v_e = fenster(ie, len(t) - 1)
        rr = torch.exp(1j * th[:, b, :k]).mean(dim=1).abs()       # Kuramoto-Ordnungsparameter
        nb = wrap(th[:, b, :k - 1] - th[:, b, 1:k]).abs()          # Nachbar-Phasendifferenz
        abstand = (pos[-1, b, 1:k] - pos[-1, b, :k - 1]).abs()
        z = {"name": f"{r['teil']} D={r['D']} {r['phasen']}", "teil": r["teil"], "D": r["D"], "phasen": r["phasen"],
             "r_anfang": gf(rr[:ia + 1].mean()), "r_ende": gf(rr[ie:].mean()),
             "sigma_om_anfang": gf(((eig_a - eig_a.mean()) ** 2).mean().sqrt()),
             "sigma_om_ende": gf(((eig_e - eig_e.mean()) ** 2).mean().sqrt()),
             "dphi_ende": gf(nb[ie:].mean()), "verschmolzen": int((abstand < 1.5).sum().item()),
             "v_max_ende": gf(v_e.abs().max()), "amp_min_rel": gf((amp[-1, b, :k] / amp[0, b, :k]).min()),
             "x_ende": [gf(v) for v in pos[-1, b, :k]], "om_eigen_ende": [gf(v) for v in eig_e],
             "om_eigen_anfang": [gf(v) for v in eig_a]}
        if r["teil"] == "b":
            z["diff_anfang"] = gf(eig_a[1] - eig_a[0])
            z["diff_ende"] = gf(eig_e[1] - eig_e[0])
        zeilen.append(z)
    kontrolle = {(z["teil"], z["phasen"]): z for z in zeilen if z["D"] == D_KONTROLLE}
    for z in zeilen:
        kz = kontrolle[(z["teil"], z["phasen"])]
        z["effekt_r"] = z["r_ende"] - kz["r_ende"]
        z["phasensynchron"] = bool(z["r_ende"] >= R_SYNC and z["verschmolzen"] == 0 and z["effekt_r"] >= 0.3)
        if z["teil"] == "a":
            z["sigma_verh"] = z["sigma_om_ende"] / max(kz["sigma_om_anfang"], 1e-300)
            z["frequenzsynchron"] = bool(z["sigma_verh"] <= 0.2 and z["verschmolzen"] == 0)
            z["gegenphasig"] = bool(z["dphi_ende"] >= 2.5 and z["dphi_ende"] - kz["dphi_ende"] >= 0.5)
        else:
            z["mitnahme"] = z["diff_ende"] / kz["diff_anfang"] if kz["diff_anfang"] != 0.0 else float("nan")
            z["mitgenommen"] = bool(z["mitnahme"] <= 0.5 and z["verschmolzen"] == 0)
    return zeilen


def bericht1(res):
    zz = ["Test 1 (Idee 9/10) Uhren. Fenster: Anfang [0, T/10], Ende [3T/4, T]. Kontrolle D = 30.",
          f"  FWHM |psi|^2: 0,70 {res['fwhm']['0.70']:.3f}, 0,55 {res['fwhm']['0.55']:.3f}, 0,80 {res['fwhm']['0.80']:.3f}",
          "  Lauf | r Anfang | r Ende | Effekt r | sigma_om Anfang, Ende | |dphi| Ende | verschmolzen | v_max | "
          "phasensynchron / frequenzsynchron / gegenphasig  bzw. Mitnahme P"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]:
            zeile = (f"  {z['name']:22s} | {z['r_anfang']:.3f} | {z['r_ende']:.3f} | {z['effekt_r']:+.3f} | "
                     f"{z['sigma_om_anfang']:.2e}, {z['sigma_om_ende']:.2e} | {z['dphi_ende']:.2f} | "
                     f"{z['verschmolzen']} | {z['v_max_ende']:.3f} | ")
            if z["teil"] == "a":
                zeile += f"{z['phasensynchron']} / {z['frequenzsynchron']} / {z['gegenphasig']}"
            else:
                zeile += f"P = {z['mitnahme']:.3f} (Diff. Ende {z['diff_ende']:+.4f}), mitgenommen {z['mitgenommen']}"
            zz.append(zeile)
    n_l3 = sum(1 for e in res["L3"] for k, v in e.items() if k != "lauf" and v["bestanden"])
    n_ges = sum(1 for e in res["L3"] for k in e if k != "lauf")
    zz.append(f"  L3 (Effekt >= 5 x Aenderung grob -> fein): {n_l3} von {n_ges} Kenngroessen bestanden")
    return zz


# ---------------------------------------------------------------- Test 2: Absorptionsspektrum

def test2(prof, faktor):
    i_z = prof["w2"].index(W2_ZIEL)
    n = len(NU_LISTE)
    laeufe = ([{"art": "ball+paket", "nu": nu} for nu in NU_LISTE] + [{"art": "paket", "nu": nu} for nu in NU_LISTE]
              + [{"art": "ball", "nu": None}, {"art": "ball+stoss", "nu": None}])

    def bauen(x, dx):
        b0 = ball(prof, i_z, x, 0.0)
        felder = []
        for r in laeufe:
            if r["art"] == "ball+paket":
                felder.append(summe([b0, paket(x, r["nu"])]))
            elif r["art"] == "paket":
                felder.append(paket(x, r["nu"]))
            elif r["art"] == "ball":
                felder.append(b0)
            else:
                felder.append(gestossen(b0))
        psi, vel = stapel(felder)
        i0, di = int(round(L_BOX / dx)), int(round(X_EBENE / dx))
        ebenen = (i0 - di, i0 + di)
        mitte = (x.abs() < X_EBENE).to(F64)

        def messen(psi, vel):
            werte = []
            for i in ebenen:
                px = (psi[:, i + 1] - psi[:, i - 1]) / (2.0 * dx)
                werte.append(-2.0 * (psi[:, i] * px.conj()).imag)       # Ladungsfluss
                werte.append(-2.0 * (vel[:, i] * px.conj()).real)       # Energiefluss
            s = psi.real ** 2 + psi.imag ** 2
            rho = 2.0 * (psi * vel.conj()).imag
            werte += [(rho * mitte).sum(1) * dx, breite_s(x, s, mitte), s.max(dim=1).values]
            return torch.stack(werte, dim=1)    # jL, SL, jR, SR, Q_mitte, Breite, S_max
        return psi, vel, messen

    stufen = stufen_rechnen("Test 2", bauen, T2 * faktor, T2_MESS)
    ergebnis = {s: auswertung2(st["t"], st["daten"], n) for s, st in stufen.items()}
    l3_liste = []
    for zg, zf in zip(ergebnis["grob"]["zeilen"], ergebnis["fein"]["zeilen"]):
        l3_liste.append({"nu": zg["nu"], "R_Q": l3(zg["R_Q"], zf["R_Q"], 0.0), "dA_Q": l3(zg["dA_Q"], zf["dA_Q"], 0.0)})
    return {"laeufe": laeufe, "ergebnis": ergebnis, "L3": l3_liste, "schwelle_1_minus_omega": 1.0 - math.sqrt(W2_ZIEL),
            "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def auswertung2(t, daten, n):
    T = t[-1].item()
    o, stoss = 2 * n, 2 * n + 1
    phi = {name: integral(t, daten[:, :, c]) for c, name in enumerate(["jL", "SL", "jR", "SR"])}
    qm = daten[:, :, 4]
    zeilen = []
    for j, nu in enumerate(NU_LISTE):
        b, p = j, n + j
        z = {"nu": nu, "k": math.sqrt(nu * nu - 1.0), "v_g": math.sqrt(nu * nu - 1.0) / nu}
        for g, cl, cr in (("Q", "jL", "jR"), ("E", "SL", "SR")):
            fl = gf(phi[cl][b] - phi[cl][o])       # netto nach rechts durch x = -30, ohne Ballbeitrag
            fr = gf(phi[cr][b] - phi[cr][o])       # nach rechts durch x = +30
            fl0, fr0 = gf(phi[cl][p]), gf(phi[cr][p])
            z["ein_" + g] = fl0
            z["T_" + g] = teilen(fr, fl0)
            z["R_" + g] = teilen(fl0 - fl, fl0)
            z["A_" + g] = teilen(fl - fr, fl0)
            z["T0_" + g] = teilen(fr0, fl0)
            z["A0_" + g] = teilen(fl0 - fr0, fl0)
            z["dA_" + g] = z["A_" + g] - z["A0_" + g]
            if g == "Q":
                dq = gf((qm[-1, b] - qm[-1, o]) - (qm[0, b] - qm[0, o]))
                z["bilanzrest_Q"] = teilen(dq - (fl - fr), fl0)
        zeilen.append(z)
    return {"zeilen": zeilen, "spektrum_stoss": spektrum(t, daten[:, stoss, 5], T / 8.0),
            "spektrum_ruhe": spektrum(t, daten[:, o, 5], T / 8.0),
            "atmung_ruhe": gf(daten[:, o, 5].max() - daten[:, o, 5].min()),
            "atmung_stoss": gf(daten[:, stoss, 5].max() - daten[:, stoss, 5].min())}


def bericht2(res):
    zz = [f"Test 2 (Idee 32) Absorption am Ball omega^2 = {W2_ZIEL}; Schwelle 1 - omega = "
          f"{res['schwelle_1_minus_omega']:.4f}. Anteile bezogen auf den Einstrom durch x = -30 ohne Ball.",
          "  nu | v_g | T_Q | R_Q | A_Q | A0_Q (ohne Ball) | dA_Q = A_Q - A0_Q | dA_E | T0_Q | Bilanzrest"]
    for stufe in ("grob", "fein"):
        e = res["ergebnis"][stufe]
        zz.append(f"  [{stufe}]")
        for z in e["zeilen"]:
            zz.append(f"  {z['nu']:.3f} | {z['v_g']:.3f} | {z['T_Q']:.6f} | {z['R_Q']:.2e} | {z['A_Q']:+.2e} | "
                      f"{z['A0_Q']:+.2e} | {z['dA_Q']:+.2e} | {z['dA_E']:+.2e} | {z['T0_Q']:.6f} | "
                      f"{z['bilanzrest_Q']:+.1e}")
        zz.append(f"  Stoss (eta = {ETA_STOSS}): Breite-FFT Spitzen Omega (Amplitude): {spitzen_text(e['spektrum_stoss'])}")
        zz.append(f"  Ruhender Ball (Rauschen): {spitzen_text(e['spektrum_ruhe'])}; Spannweite Breite "
                  f"{e['atmung_ruhe']:.1e} (gestossen {e['atmung_stoss']:.1e})")
    n_l3 = sum(1 for e in res["L3"] if e["R_Q"]["bestanden"])
    zz.append(f"  L3 fuer R_Q: {n_l3} von {len(res['L3'])} nu bestanden; max |dA_Q| grob "
              f"{max(abs(z['dA_Q']) for z in res['ergebnis']['grob']['zeilen']):.2e}, fein "
              f"{max(abs(z['dA_Q']) for z in res['ergebnis']['fein']['zeilen']):.2e}")
    return zz


# ---------------------------------------------------------------- Test 3: Virus

def test3(prof, faktor):
    ig, ik = prof["w2"].index(W2_GROSS), prof["w2"].index(W2_KLEIN)
    iersatz = len(prof["w2"]) - 1
    wg, wk = math.sqrt(W2_GROSS), math.sqrt(W2_KLEIN)
    gam = 1.0 / math.sqrt(1.0 - V_KLEIN ** 2)
    d_kontakt = 1.2 * 0.5 * (fwhm(W2_GROSS) + fwhm(W2_KLEIN))
    t_kontakt = (abs(X_KLEIN0) - d_kontakt) / V_KLEIN            # freier Kontakt ohne Anziehung
    laeufe = [{"art": "stoss", "delta_soll": dc, "phase_klein": (wk / gam - wg) * t_kontakt - dc}
              for dc in PHASEN_KONTAKT]
    laeufe += [{"art": "gross"}, {"art": "gross+stoss"}, {"art": "ersatz+stoss"}, {"art": "klein"}]

    def bauen(x, dx):
        g0 = ball(prof, ig, x, 0.0)
        felder = []
        for r in laeufe:
            if r["art"] == "stoss":
                felder.append(summe([g0, ball(prof, ik, x, X_KLEIN0, V_KLEIN, r["phase_klein"])]))
            elif r["art"] == "gross":
                felder.append(g0)
            elif r["art"] == "gross+stoss":
                felder.append(gestossen(g0))
            elif r["art"] == "ersatz+stoss":
                felder.append(gestossen(ball(prof, iersatz, x, 0.0)))
            else:
                felder.append(ball(prof, ik, x, X_KLEIN0, V_KLEIN, 0.0))
        psi, vel = stapel(felder)

        def messen(psi, vel):
            s = psi.real ** 2 + psi.imag ** 2
            rho = 2.0 * (psi * vel.conj()).imag
            e = vel.abs() ** 2 + (s - s * s + 0.5 * s ** 3)
            e[:, :-1] += ((psi[:, 1:] - psi[:, :-1]).abs() / dx) ** 2
            ib = s.argmax(dim=1, keepdim=True)                               # grosser Ball bzw. Klumpen
            xb = x[ib]
            iS = (s * (x < xb - 3.0).to(F64)).argmax(dim=1, keepdim=True)    # kleiner Ball links davon
            fenster = ((x - xb).abs() < W_KLUMPEN).to(F64)
            pb, ps = psi.gather(1, ib), psi.gather(1, iS)
            spalten = [xb, x[iS], -torch.angle(pb), -torch.angle(ps), ps.abs() ** 2,
                       ((rho * fenster).sum(1) * dx).unsqueeze(1), ((e * fenster).sum(1) * dx).unsqueeze(1),
                       breite_s(x, s, fenster).unsqueeze(1), pb.abs() ** 2,
                       (rho.sum(1) * dx).unsqueeze(1), (e.sum(1) * dx).unsqueeze(1)]
            return torch.cat(spalten, dim=1)
        return psi, vel, messen

    stufen = stufen_rechnen("Test 3", bauen, T3 * faktor, T3_MESS)
    ergebnis = {s: auswertung3(laeufe, st["t"], st["daten"], d_kontakt) for s, st in stufen.items()}
    l3_liste = []
    for zg, zf in zip(ergebnis["grob"]["zeilen"], ergebnis["fein"]["zeilen"]):
        if zg["art"] == "stoss":
            l3_liste.append({"delta_soll": zg["delta_soll"], "M": l3(zg["M"], zf["M"], 0.0)})
    return {"laeufe": laeufe, "ergebnis": ergebnis, "L3": l3_liste, "d_kontakt": d_kontakt, "t_kontakt_frei": t_kontakt,
            "w2_ersatz": prof["w2"][iersatz], "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def auswertung3(laeufe, t, daten, d_kontakt):
    T = t[-1].item()
    xb, xs, thb, ths, ss, qk, ek, bk, sb, qbox, ebox = daten.unbind(dim=2)
    thbu = entfalten(thb)
    ie = min(len(t) - 2, int((t < 0.75 * T - 1e-9).sum().item()))
    zeilen = []
    for b, r in enumerate(laeufe):
        dauer = (t[-1] - t[ie]).item()
        v_e = gf((xb[-1, b] - xb[ie, b]) / dauer)
        om_e = gf((thbu[-1, b] - thbu[ie, b]) / dauer) / math.sqrt(max(1e-12, 1.0 - v_e * v_e))
        q_t, e_t = gf(qk[-1, b]), gf(ek[-1, b])
        w2a = anker_umkehr(q_t)
        e_anker = anker_q_e(w2a)[1] if math.isfinite(w2a) else float("nan")
        z = {"art": r["art"], "Q_box_0": gf(qbox[0, b]), "Q_box_T": gf(qbox[-1, b]), "E_box_0": gf(ebox[0, b]),
             "E_box_T": gf(ebox[-1, b]), "Q_klumpen_0": gf(qk[0, b]), "Q_klumpen_T": q_t, "E_klumpen_0": gf(ek[0, b]),
             "E_klumpen_T": e_t, "omega2_klumpen_ende": om_e * om_e, "omega2_anker_zu_Q": w2a,
             "E_anker_zu_Q": e_anker, "anregung": e_t - e_anker, "v_klumpen_ende": v_e,
             "x_klumpen_ende": gf(xb[-1, b])}
        if r["art"] == "stoss":
            z["delta_soll"] = r["delta_soll"]
            kontakt = ((xb[:, b] - xs[:, b]) < d_kontakt) & (ss[:, b] > 0.3 * ss[0, b])
            if bool(kontakt.any()):
                m = int(torch.nonzero(kontakt)[0, 0].item())
                z["t_kontakt"] = gf(t[m])
                z["delta_kontakt"] = gf(wrap(ths[m, b] - thb[m, b]))
            else:
                z["t_kontakt"], z["delta_kontakt"] = float("nan"), float("nan")
            z["M"] = (z["Q_klumpen_T"] - z["Q_klumpen_0"]) / (z["Q_box_0"] - z["Q_klumpen_0"])
            z["klasse"] = "verschmolzen" if z["M"] >= 0.7 else ("getrennt" if z["M"] <= 0.3 else "teilweise")
            z["spektrum"] = spektrum(t, bk[:, b], 0.5 * T)
        elif r["art"] in ("gross+stoss", "ersatz+stoss", "gross"):
            z["spektrum"] = spektrum(t, bk[:, b], T / 8.0)
        zeilen.append(z)
    return {"zeilen": zeilen}


def bericht3(res):
    zz = [f"Test 3 (Idee 33) Virus: klein {W2_KLEIN} bei x = {X_KLEIN0} mit v = {V_KLEIN} in gross {W2_GROSS} bei 0. "
          f"Kontakt ab Abstand {res['d_kontakt']:.2f}, frei bei t = {res['t_kontakt_frei']:.0f}. "
          f"Ersatzball omega^2 = {res['w2_ersatz']}.",
          "  Lauf | Soll-dphi Kontakt | gemessen | t Kontakt | M | Klasse | Q Klumpen 0 -> T | Q Box 0 -> T | "
          "E Box 0 -> T | omega^2 Ende (Anker zu Q) | Anregung | Breite-FFT Omega (Amplitude)"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]["zeilen"]:
            kopf = f"  {z['art']:12s}"
            if z["art"] == "stoss":
                kopf += (f" | {z['delta_soll']:.3f} | {z['delta_kontakt']:+.3f} | {z['t_kontakt']:.1f} | {z['M']:.3f} | "
                         f"{z['klasse']}")
            zz.append(kopf + f" | {z['Q_klumpen_0']:.4f} -> {z['Q_klumpen_T']:.4f} | {z['Q_box_0']:.4f} -> "
                      f"{z['Q_box_T']:.4f} | {z['E_box_0']:.4f} -> {z['E_box_T']:.4f} | {z['omega2_klumpen_ende']:.4f} "
                      f"({z['omega2_anker_zu_Q']:.4f}) | {z['anregung']:.2e} | {spitzen_text(z.get('spektrum', []))}")
    n_l3 = sum(1 for e in res["L3"] if e["M"]["bestanden"])
    zz.append(f"  L3 fuer M: {n_l3} von {len(res['L3'])} Phasen bestanden")
    return zz


# ---------------------------------------------------------------- Test 4: 3D radial (neu)

def koeffizienten(a0):
    """f_top = sqrt(S+) mit S+ = (2 + sqrt(4 - 6 a0))/3 (Buckel des Teilchenpotentials) und die Taylor-Koeffizienten
    c1..c5 von F(f) = a0 f - 2 f^3 + 1,5 f^5 um f_top: F(f_top + v) = c1 v + ... + c5 v^5 (exakt, F(f_top) = 0)."""
    s_top = (2.0 + torch.sqrt(4.0 - 6.0 * a0)) / 3.0
    t = torch.sqrt(s_top)
    c = (a0 - 6.0 * s_top + 7.5 * s_top * s_top, -6.0 * t + 15.0 * t * s_top, -2.0 + 15.0 * s_top, 7.5 * t,
         torch.full_like(t, 1.5))
    return t, c


def g_u(u, c):
    """G(u) = -F(f_top - u) = c1 u - c2 u^2 + c3 u^3 - c4 u^4 + c5 u^5 (relativ genau auch fuer winziges u)."""
    c1, c2, c3, c4, c5 = c
    return u * (c1 + u * (-c2 + u * (c3 + u * (-c4 + u * c5))))


def g_strich(u, c):
    c1, c2, c3, c4, c5 = c
    return c1 + u * (-2.0 * c2 + u * (3.0 * c3 + u * (-4.0 * c4 + u * 5.0 * c5)))


def rk4_radial(r, u, up, h, c, dm1):
    """RK4 fuer u'' = G(u) - (d-1)/r u' (u = f_top - f; f'' + (d-1)/r f' = F(f))."""
    def ab(rr, uu, pp):
        return pp, g_u(uu, c) - dm1 * pp / rr
    k1u, k1p = ab(r, u, up)
    k2u, k2p = ab(r + 0.5 * h, u + 0.5 * h * k1u, up + 0.5 * h * k1p)
    k3u, k3p = ab(r + 0.5 * h, u + 0.5 * h * k2u, up + 0.5 * h * k2p)
    k4u, k4p = ab(r + h, u + h * k3u, up + h * k3p)
    return (u + (h / 6.0) * (k1u + 2.0 * k2u + 2.0 * k3u + k4u),
            up + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p))


def radial_start(s, c, dm1):
    """Reihe um r = 0: u = u0 + a r^2 + b r^4, a = G(u0)/(2d), b = G'(u0) a/(4d + 8), u0 = exp(-s). Werte bei r = H3."""
    d = dm1 + 1.0
    u0 = torch.exp(-s)
    a = g_u(u0, c) / (2.0 * d)
    b = g_strich(u0, c) * a / (4.0 * d + 8.0)
    return u0, u0 + a * H3 ** 2 + b * H3 ** 4, 2.0 * a * H3 + 4.0 * b * H3 ** 3


def schiessen_radial(a0, dm1, runden):
    """Einschachteln in s = -ln(f_top - f(0)) wie schiessen(): grosses s = Ueberschuss (f < 0), kleines s =
    Unterschuss (f' > 0 vor der Null). Unentschiedene Kandidaten verschieben die Klammer nicht."""
    t, c = koeffizienten(a0)
    lo = -torch.log(t - 1e-3)                                  # f(0) = 1e-3: sicher Unterschuss
    hi = torch.full_like(lo, S_MAX3)                           # f(0) = f_top - e^-150: sicher Ueberschuss
    stufen = torch.linspace(0.0, 1.0, N_KAND3, dtype=F64, device=DEV)
    n_schritte = int(round(X3 / H3)) - 1
    for _ in range(runden):
        s = lo + (hi - lo) * stufen                            # (n, N_KAND3)
        _, u, up = radial_start(s, c, dm1)
        zustand = torch.zeros_like(s)
        for k in range(n_schritte):
            u, up = rk4_radial(H3 * (k + 1), u, up, H3, c, dm1)
            ueber = (zustand == 0) & (u > t)
            unter = (zustand == 0) & (u <= t) & (up < 0)
            zustand = zustand + ueber.to(F64) - unter.to(F64)
            lebt = (zustand == 0).to(F64)
            u = u * lebt
            up = up * lebt
        lo = torch.where(zustand < 0, s, lo.expand_as(s)).max(dim=1, keepdim=True).values
        hi = torch.where(zustand > 0, s, hi.expand_as(s)).min(dim=1, keepdim=True).values
    return 0.5 * (lo + hi), hi - lo, t, c


def radial_bahn(s, t, c, dm1):
    """Profilbahn zum Mittelwert der Klammer. Stopp (Grund): 1 f < SCHWANZ f(0), 2 f' > 0, 3 f < 0; 0 offen."""
    u0, u, up = radial_start(s, c, dm1)
    schwelle = SCHWANZ * (t - u0)
    bu, bp = [u0, u], [torch.zeros_like(u0), up]
    n_schritte = int(round(X3 / H3)) - 1
    aktiv = torch.ones_like(u0, dtype=torch.bool)
    j_cut = torch.full_like(u0, n_schritte + 1, dtype=torch.long)
    grund = torch.zeros_like(u0, dtype=torch.long)
    for k in range(n_schritte):
        u_neu, up_neu = rk4_radial(H3 * (k + 1), u, up, H3, c, dm1)
        f_neu = t - u_neu
        stopp = torch.where(f_neu < schwelle, torch.ones_like(grund), torch.zeros_like(grund))
        stopp = torch.where(up_neu < 0, torch.full_like(grund, 2), stopp)
        stopp = torch.where(f_neu < 0, torch.full_like(grund, 3), stopp)
        neu = aktiv & (stopp > 0)
        j_cut = torch.where(neu, torch.full_like(j_cut, k + 2), j_cut)
        grund = torch.where(neu, stopp, grund)
        u = torch.where(aktiv, u_neu, u)
        up = torch.where(aktiv, up_neu, up)
        aktiv = aktiv & (stopp == 0)
        bu.append(u)
        bp.append(up)
    return torch.cat(bu, dim=1), torch.cat(bp, dim=1), j_cut, grund, t - u0


def radial_integrale(bu, bp, j_cut, t, a0, dm1, w2):
    """Trapez bis r_cut plus Schwanz f_cut (r_cut/r)^((d-1)/2) exp(-k (r - r_cut)); Kugelflaeche 2 (d = 1), 4 pi (d = 3)."""
    n, p = bu.shape
    idx = torch.arange(p, device=DEV).unsqueeze(0)
    r = idx.to(F64) * H3
    gew = H3 * (idx <= j_cut).to(F64) - 0.5 * H3 * ((idx == 0) | (idx == j_cut)).to(F64)
    f, fp = t - bu, -bp
    rp = r ** dm1
    sd = torch.where(dm1 == 0, torch.full_like(dm1, 2.0), torch.full_like(dm1, 4.0 * PI))
    s = f * f
    i_f = sd * (gew * s * rp).sum(1, keepdim=True)
    i_g = sd * (gew * fp * fp * rp).sum(1, keepdim=True)
    i_u = sd * (gew * (s - s * s + 0.5 * s ** 3) * rp).sum(1, keepdim=True)
    k = torch.sqrt(a0)
    f_c = f.gather(1, j_cut)
    schwanz = sd * f_c * f_c * (j_cut.to(F64) * H3) ** dm1 / (2.0 * k)
    i_f = i_f + schwanz
    w = w2 * i_f
    g = i_g + k * k * schwanz
    v = i_u + schwanz
    e = w + g + v
    q = 2.0 * torch.sqrt(w2) * i_f
    vir = ((dm1 - 1.0) * g + (dm1 + 1.0) * (v - w)) / e      # Pohozaev: (d-2) G + d (V - W) = 0
    return q, e, vir, schwanz / i_f


def test4(runden):
    w2_liste = W2_3D + W2_1D_KONTROLLE
    n3 = len(W2_3D)
    dm1 = torch.tensor([2.0] * n3 + [0.0] * len(W2_1D_KONTROLLE), dtype=F64, device=DEV).unsqueeze(1)
    w2t = torch.tensor(w2_liste, dtype=F64, device=DEV).unsqueeze(1)
    a0 = 1.0 - w2t
    t0 = uhr()
    s, klammer, t, c = schiessen_radial(a0, dm1, runden)
    bu, bp, j_cut, grund, f0 = radial_bahn(s, t, c, dm1)
    q, e, vir, schwanzanteil = radial_integrale(bu, bp, j_cut, t, a0, dm1, w2t)
    sek = uhr() - t0
    print(f"Test 4: radiales Schiessen fertig nach {sek:.1f} s", flush=True)
    zeilen = []
    for i, w2 in enumerate(w2_liste):
        zeilen.append({"d": 3 if i < n3 else 1, "omega2": w2, "f0_quadrat": gf(f0[i, 0]) ** 2, "s": gf(s[i, 0]),
                       "klammer_s": gf(klammer[i, 0]), "r_cut": gf(j_cut[i, 0]) * H3, "grund": int(grund[i, 0].item()),
                       "Q": gf(q[i, 0]), "E": gf(e[i, 0]), "E_zu_Q": gf(e[i, 0] / q[i, 0]), "virial": gf(vir[i, 0]),
                       "schwanzanteil": gf(schwanzanteil[i, 0])})
    drei = zeilen[:n3]
    om = [math.sqrt(z["omega2"]) for z in drei]
    qs, es = [z["Q"] for z in drei], [z["E"] for z in drei]
    for i, z in enumerate(drei):                                 # dQ/domega, zentral, am Rand einseitig
        a, b = max(0, i - 1), min(n3 - 1, i + 1)
        z["dQ_domega"] = (qs[b] - qs[a]) / (om[b] - om[a])
        z["VK_stabil"] = bool(z["dQ_domega"] < 0.0)
        z["dE_dQ_durch_omega"] = ((es[b] - es[a]) / (qs[b] - qs[a]) / om[i]) if qs[b] != qs[a] else float("nan")
    vorzeichen = [z["dQ_domega"] > 0.0 for z in drei]
    wechsel = sum(1 for i in range(n3 - 1) if vorzeichen[i] != vorzeichen[i + 1])
    i_min = min(range(n3), key=lambda i: qs[i])
    if 0 < i_min < n3 - 1:                                       # Parabel durch drei Punkte um das Minimum
        x1, x2, x3 = om[i_min - 1], om[i_min], om[i_min + 1]
        y1, y2, y3 = qs[i_min - 1], qs[i_min], qs[i_min + 1]
        nenner = (x1 - x2) * (x1 - x3) * (x2 - x3)
        pa = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / nenner
        pb = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / nenner
        pc = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / nenner
        om_c = -pb / (2.0 * pa) if pa != 0.0 else om[i_min]
        q_min = pc - pb * pb / (4.0 * pa) if pa != 0.0 else qs[i_min]
    else:
        om_c, q_min = om[i_min], qs[i_min]
    q_ober = min(qs[0], qs[-1])
    vergleich = []
    for fak in (1.2, 1.5, 2.0, 3.0, 5.0):                        # E auf beiden Aesten bei gleichem Q
        qq = fak * q_min
        if qq >= q_ober:
            continue
        e_duenn = interp_bei(qs[:i_min + 1], es[:i_min + 1], qq)
        e_dick = interp_bei(qs[i_min:], es[i_min:], qq)
        vergleich.append({"Q": qq, "E_duenne_wand": e_duenn, "E_dicke_wand": e_dick, "E_dick_minus_duenn": e_dick - e_duenn})
    kontrolle_1d = []
    for z in zeilen[n3:]:
        q_a, e_a = anker_q_e(z["omega2"])
        kontrolle_1d.append({"omega2": z["omega2"], "Q": z["Q"], "Q_anker": q_a, "E": z["E"], "E_anker": e_a,
                             "rel_abw_Q": z["Q"] / q_a - 1.0, "rel_abw_E": z["E"] / e_a - 1.0,
                             "f0_quadrat": z["f0_quadrat"], "f0_quadrat_anker": 1.0 - math.sqrt(2.0 * z["omega2"] - 1.0)})
    innen = [z["dE_dQ_durch_omega"] for z in drei[1:-1] if math.isfinite(z["dE_dQ_durch_omega"])]
    innen = sorted(abs(v - 1.0) for v in innen)
    zusammen = {"omega2_Qmin": om_c * om_c, "Q_min": q_min, "i_min_gitter": i_min, "vorzeichenwechsel_dQ": wechsel,
                "zwei_aeste_fuer_Q": [q_min, q_ober], "vergleich_gleiches_Q": vergleich,
                "duenne_wand_alle_VK_stabil": all(z["VK_stabil"] for z in drei[:i_min]),
                "dicke_wand_alle_VK_instabil": all(not z["VK_stabil"] for z in drei[i_min + 1:]),
                "E_kleiner_Q_bereich": [z["omega2"] for z in drei if z["E"] < z["Q"]],
                "max_abs_virial_3d": max(abs(z["virial"]) for z in drei),
                "median_abw_dEdQ_omega": innen[len(innen) // 2] if innen else float("nan"),
                "gruende_nicht_schwanz": [z["omega2"] for z in zeilen if z["grund"] != 1],
                "max_rel_abw_1d_anker": max(max(abs(k["rel_abw_Q"]), abs(k["rel_abw_E"])) for k in kontrolle_1d)}
    return {"zeilen": zeilen, "kontrolle_1d": kontrolle_1d, "zusammen": zusammen, "sek": sek, "runden": runden}


def interp_bei(qs, es, qq):
    for i in range(len(qs) - 1):
        a, b = qs[i], qs[i + 1]
        if (a - qq) * (b - qq) <= 0.0 and a != b:
            return es[i] + (es[i + 1] - es[i]) * (qq - a) / (b - a)
    return float("nan")


def bericht4(res):
    zs = res["zusammen"]
    zz = [f"Test 4 (Idee 31) 3D radial, {res['runden']} Schiessrunden, {res['sek']:.1f} s. Grund: 1 Schwanz, 2 f'>0, "
          "3 f<0, 0 offen.",
          "  omega^2 | f0^2 | s | Klammer | r_cut | Grund | Q | E | E/Q | dQ/domega | VK stabil | Virial | dE/dQ/omega"]
    for z in res["zeilen"]:
        if z["d"] != 3:
            continue
        zz.append(f"  {z['omega2']:.2f} | {z['f0_quadrat']:.6f} | {z['s']:.4f} | {z['klammer_s']:.1e} | "
                  f"{z['r_cut']:.1f} | {z['grund']} | {z['Q']:.5e} | {z['E']:.5e} | {z['E_zu_Q']:.5f} | "
                  f"{z['dQ_domega']:+.4e} | {z['VK_stabil']} | {z['virial']:+.1e} | {z['dE_dQ_durch_omega']:.5f}")
    zz.append(f"  Q_min = {zs['Q_min']:.4f} bei omega^2 = {zs['omega2_Qmin']:.4f} (Gitterindex {zs['i_min_gitter']}); "
              f"Vorzeichenwechsel von dQ/domega: {zs['vorzeichenwechsel_dQ']}")
    zz.append(f"  duenne Wand alle VK-stabil: {zs['duenne_wand_alle_VK_stabil']}; dicke Wand alle VK-instabil: "
              f"{zs['dicke_wand_alle_VK_instabil']}; zwei Aeste fuer Q in [{zs['zwei_aeste_fuer_Q'][0]:.3f}, "
              f"{zs['zwei_aeste_fuer_Q'][1]:.3e}]")
    for v in zs["vergleich_gleiches_Q"]:
        zz.append(f"  gleiches Q = {v['Q']:.3f}: E duenn {v['E_duenne_wand']:.5f}, E dick {v['E_dicke_wand']:.5f}, "
                  f"Differenz {v['E_dick_minus_duenn']:+.5f}")
    zz.append(f"  E < Q (stabil gegen freie Quanten) bei omega^2: {zs['E_kleiner_Q_bereich']}")
    zz.append(f"  Kontrollen: max |Virial| 3D {zs['max_abs_virial_3d']:.1e}; Median |dE/dQ / omega - 1| "
              f"{zs['median_abw_dEdQ_omega']:.1e}; Stopp nicht im Schwanz bei {zs['gruende_nicht_schwanz']}; "
              f"1D-Verfahren gegen Anker max rel. Abw. {zs['max_rel_abw_1d_anker']:.1e}")
    for k in res["kontrolle_1d"]:
        zz.append(f"  1D {k['omega2']:.2f}: Q {k['Q']:.8f} (Anker {k['Q_anker']:.8f}), E {k['E']:.8f} "
                  f"(Anker {k['E_anker']:.8f}), f0^2 {k['f0_quadrat']:.10f} (Anker {k['f0_quadrat_anker']:.10f})")
    return zz


# ---------------------------------------------------------------- Hauptprogramm

def main():
    ap = argparse.ArgumentParser(description="Runde 2: 1D-Tests fuer die Ideen 9/10, 32, 33 und 3D radial fuer 31")
    ap.add_argument("--tests", default="1234", help="Auswahl, z. B. 4 oder 123")
    ap.add_argument("--rauch", action="store_true", help="Laufzeiten x 0,05, Test 4 mit einer Schiessrunde")
    ap.add_argument("--profil", default=None, help="1D-Schiessbahnen (profil_1d.pt) aus einem frueheren Lauf")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ausgabe"))
    args = ap.parse_args()
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    gesamt = torch.cuda.get_device_properties(0).total_memory
    torch.cuda.set_per_process_memory_fraction(min(1.0, SPEICHER_GB * 2 ** 30 / gesamt))
    os.makedirs(args.out, exist_ok=True)
    faktor = 0.05 if args.rauch else 1.0
    start = jetzt()
    t_start = uhr()
    kopf = f"Runde 2 tests1d Start {start} auf {torch.cuda.get_device_name(0)}, torch {torch.__version__}, " \
           f"Tests {args.tests}, Rauchtest {args.rauch}"
    print(kopf, flush=True)
    ausgabe = {"start": start, "geraet": torch.cuda.get_device_name(0), "torch": torch.__version__,
               "tests": args.tests, "rauch": args.rauch, "ergebnisse": {}, "fehler": {}}
    text = [kopf, ""]
    reihen = {}

    if "4" in args.tests:
        try:
            res4 = test4(1 if args.rauch else RUNDEN3)
            ausgabe["ergebnisse"]["4"] = res4
            text += bericht4(res4) + [""]
        except Exception:
            ausgabe["fehler"]["4"] = traceback.format_exc()
            text += ["Test 4 FEHLER:", ausgabe["fehler"]["4"], ""]
            print(ausgabe["fehler"]["4"], flush=True)
        schreiben(args.out, ausgabe, text, reihen)

    auswahl = [n for n in "123" if n in args.tests]
    if auswahl:
        t0 = uhr()
        w2_liste = w2_liste_1d()
        try:
            prof = profile_1d(w2_liste, args.profil, os.path.join(args.out, "profil_1d.pt"))
        except Exception:
            ausgabe["fehler"]["profile_1d"] = traceback.format_exc()
            text += ["1D-Profile FEHLER, Tests 1 bis 3 entfallen:", ausgabe["fehler"]["profile_1d"], ""]
            print(ausgabe["fehler"]["profile_1d"], flush=True)
            auswahl = []
        sek = uhr() - t0
    if auswahl:
        x = gitter(DX)
        anker = []
        for i, w2 in enumerate(w2_liste):
            f_int = profil_an(prof, i, x)
            f_git = profil_gitter(prof["bahn"][i:i + 1], prof["j_cut"][i:i + 1], prof["a0"][i:i + 1], DX)[0]
            anker.append({"omega2": w2, "f0_quadrat": gf(prof["f0"][i, 0]) ** 2,
                          "max_abw_anker": gf((f_int - profil_anker(w2, DX)).abs().max()),
                          "max_abw_interpolation_gitter": gf((f_int[1:-1] - f_git[1:-1]).abs().max())})
        k0 = max(a["max_abw_anker"] for a in anker)
        ausgabe["profile_1d"] = {"omega2": w2_liste, "sek": sek, "geladen": prof["geladen"], "anker": anker,
                                 "K0_bestanden": bool(k0 <= TOL_PROFIL)}
        text.append(f"1D-Profile ({'geladen' if prof['geladen'] else 'geschossen'}, {sek:.1f} s): K0 max |f - f_Anker| = "
                    f"{k0:.1e} ({'bestanden' if k0 <= TOL_PROFIL else 'NICHT bestanden'}), Interpolation gegen "
                    f"profil_gitter max {max(a['max_abw_interpolation_gitter'] for a in anker):.1e}")
        text.append("  omega^2: " + ", ".join(f"{a['omega2']}" for a in anker))
        text.append("")
        for n, funk, ber in (("1", test1, bericht1), ("2", test2, bericht2), ("3", test3, bericht3)):
            if n not in auswahl:
                continue
            try:
                res, stufen = funk(prof, faktor)
                ausgabe["ergebnisse"][n] = res
                reihen[n] = {"laeufe": res["laeufe"],
                             "stufen": {s: {"t": st["t"].cpu(), "daten": st["daten"].cpu()} for s, st in stufen.items()}}
                text += ber(res) + [""]
            except Exception:
                ausgabe["fehler"][n] = traceback.format_exc()
                text += [f"Test {n} FEHLER:", ausgabe["fehler"][n], ""]
                print(ausgabe["fehler"][n], flush=True)
            schreiben(args.out, ausgabe, text, reihen)

    ausgabe["ende"] = jetzt()
    ausgabe["dauer_s"] = uhr() - t_start
    ausgabe["torch_speicher_max_mb"] = torch.cuda.max_memory_allocated() / 2 ** 20
    text.append(f"Ende {ausgabe['ende']}, Dauer {ausgabe['dauer_s']:.1f} s, Torch-Speicher max "
                f"{ausgabe['torch_speicher_max_mb']:.0f} MB, Fehler in: "
                f"{sorted(ausgabe['fehler']) if ausgabe['fehler'] else 'keine'}")
    schreiben(args.out, ausgabe, text, reihen)
    print("\n".join(text), flush=True)
    if ausgabe["fehler"]:
        raise SystemExit(1)


def schreiben(out, ausgabe, text, reihen):
    """Stand nach jedem Test sichern; bricht der Lauf ab (RuntimeMaxSec), bleiben die fertigen Tests erhalten."""
    with open(os.path.join(out, "tests1d_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    torch.save(reihen, os.path.join(out, "tests1d_zeitreihen.pt"))
    with open(os.path.join(out, "tests1d_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)


if __name__ == "__main__":
    main()
