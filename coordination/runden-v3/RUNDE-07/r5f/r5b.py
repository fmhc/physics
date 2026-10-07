#!/usr/bin/env python3
"""Runde 5 (runden-v3), Paket R5-B: 1D-Einzelball-Tests zu sechs Q-Ball-Ideen. Explorativ. Ungetestet abgegeben
(Interpreterverbot auf dem Laptop); Plan, Aufrufe, Vorhersagen und Latten stehen in PLAN.md daneben.

Modell wie Runde 2: L = |psi_t|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2, 1/2 < omega^2 < 1.
Bewegungsgleichung psi_tt = psi_xx - U'(S) psi, dazu nur wo angegeben ein Antrieb F(x, t) und eine Daempfung -gamma psi_t.
rho = 2 Im(psi conj psi_t), e = |psi_t|^2 + |psi_x|^2 + U(S), Ladungsfluss j = -2 Im(psi conj psi_x).

Aus RUNDE-02/tests1d/tests1d.py uebernommen (dort auf der P4000 gelaufen): Gitter [-150, 150] mit dx = 0,1, dt = 0,05
(fein dx/2 und dt/2), quadratische Daempfungsschicht (sigma0 = 1, ab |x| = 110), Velocity-Verlet-Schritt und Kraft
(Laplace ueber Flussdifferenzen), die Anker-Formeln (profil_anker, anker_wgv, anker_q_e, anker_umkehr, fwhm) und die
Auswerte-Hilfen (wrap, entfalten, breite_s, spektrum, l3).
Geaendert oder neu:
- Ballprofil direkt aus dem analytischen 1D-Anker statt aus dem Schiessen. Runde 2 hat beide verglichen (K0: max
  |f_Schuss - f_Anker| = 1,5e-10); ohne Brechungsfeld ist der Anker exakt, das Schiessen entfaellt.
- --geraet cuda oder cpu, float64 bzw. complex128 in beiden Faellen; auf der CPU genau ein Thread (CPUQuota 100 %).
- Verlet-Schritt wahlweise mit gleichmaessiger Daempfung gamma je Lauf, Antrieb F(x, t) je Lauf und periodischem Rand
  ohne Daempfungsschicht (nur mi).
Unterbefehle, einer je Idee, dazu ein Rauchtest:
  fuettern      Bio 3             Wellenpakete auf einen Ball: eingefangener Anteil, Ladungs-/Energiebilanz, omega
  photo         Bio 36            Dauerwelle aus einer Quelle: Wachstumsrate gegen Frequenz
  winterschlaf  Bio 38            fester Stoss gegen omega^2 = 0,55 ... 0,90: Antwort, Frequenz, Abklingen, Rest
  rauschen      Bio 20/37         Rauschpuls verschiedener Staerke: Ueberleben und Schmelzschwelle gegen Q
  pumpe         Bio 45            Antrieb plus Daempfung: dissipative Struktur, Schwelle h_min, Attraktor
  mi            Bio 22, Chemie 10 Modulationsinstabilitaet des Kondensats: Wellenlaenge, Wachstum, Verklumpung
  rauch         alle sechs mit Laufzeit x 0,05; druckt die Hochrechnung fuer die volle Laenge
Aufruf: python r5b.py <befehl> [--geraet cuda|cpu] [--out ORDNER] [--faktor F]
Ausgabe je Befehl im --out-Ordner: <befehl>_bericht.txt, <befehl>_ergebnis.json, <befehl>_zeitreihen.pt.
"""
import argparse
import datetime
import json
import math
import os
import time
import traceback

import torch

DEV = torch.device("cpu")      # wird in main() gesetzt
F64 = torch.float64
C128 = torch.complex128
PI = math.pi
NAN = float("nan")
ROH = {}                       # Rohdaten je Befehl (fuer den Fall, dass die Auswertung scheitert)

# ---- aus tests1d.py (Runde 2) unveraendert ----
SIGMA0 = 1.0             # Daempfung am Rand
DX, DT = 0.1, 0.05       # grobe Aufloesung; die feine halbiert beide
L_BOX = 150.0            # Box [-L, L], Dirichlet-Rand
X_SPONGE = 110.0         # Daempfungsschicht fuer |x| > X_SPONGE
FEIN = 0.5               # feine Stufe: dx und dt mal FEIN (Latte L3)

# ---- Runde 5, gemeinsam ----
SPEICHER_GB = 1.5        # Obergrenze Torch-Speicher auf der Karte (Vorgabe der Leitung)
W_FENSTER = 20.0         # Messfenster |x| < 20 um den ruhenden Ball

# ---- fuettern (Bio 3) ----
F_W2 = [0.55, 0.70, 0.90]
F_NU = [1.6, 2.2, 2.6, 2.8, 3.0]
F_EPS = [0.01, 0.05]                                   # 0,05: Flaeche eps sigma sqrt(2 pi) = 1,0 < pi/2 (kein Soliton)
F_ANTI = [(0.55, 2.2), (0.55, 3.0), (0.70, 2.2), (0.70, 3.0)]   # Antiteilchen-Pakete, eps = 0,01
F_SIGMA, F_X0 = 8.0, -55.0
F_T, F_MESS = 250.0, 0.5

# ---- photo (Bio 36) ----
P_EPS = 0.05
P_NU = {0.55: [2.0, 2.3, 2.45, 2.52, 2.6, 2.8, 3.1], 0.70: [2.0, 2.3, 2.6, 2.64, 2.71, 2.8, 3.1], 0.90: [3.1]}
P_ZUSATZ = [(0.55, 2.3, 0.025, 1), (0.55, 2.8, 0.025, 1), (0.55, 2.3, 0.05, -1)]   # (w2, nu, eps, Vorzeichen)
P_XS, P_WS, P_RAMPE = -60.0, 0.3, 30.0                 # Quellort, Quellbreite, Anlaufzeit
P_XJ = -20.0                                           # Flussebene fuer den Einstrom
P_T, P_MESS = 360.0, 0.5

# ---- winterschlaf (Bio 38) ----
W_W2 = [0.55, 0.62, 0.70, 0.78, 0.85, 0.90]
W_A = [0.01, 0.03]                                     # fester Stoss psi -> psi + A exp(-x^2/2)
W_BREITE = 1.0
W_ETA = 0.01                                           # relativer Stoss wie Runde 2 (nur 0,70, Vergleich 0,1702)
W_T, W_MESS = 600.0, 0.5

# ---- rauschen (Bio 20/37) ----
R_W2 = [0.55, 0.70, 0.90]
R_EPS = [0.025, 0.05, 0.1, 0.2, 0.3, 0.4]              # RMS von |psi_Rauschen| in |x| < 90
R_SAAT = [11, 12]
R_KMIN, R_KMAX, R_LMODI = 0.5, 2.5, 300.0              # Band und Modenabstand 2 pi / 300
R_XIN, R_XAUS = 90.0, 100.0                            # Rauschen in |x| < 90, weicher Rand bis 100
R_WT, R_WB = 4.0, 8.0                                  # Mean-shift-Fenster, Ladungsfenster um die Ballmitte
R_T, R_MESS = 220.0, 0.5

# ---- pumpe (Bio 45) ----
PU_W2D, PU_GAMMA = 0.70, 0.01                          # Treiberfrequenz Omega_d^2, Daempfung
PU_H_REL = [0.0, 0.5, 0.8, 1.25, 2.0, 4.0]             # h / h_min, Ball 0,70
PU_SAAT_W2 = [0.55, 0.60, 0.80, 0.90]                  # Startbaelle bei h = 2 h_min
PU_UNTER_W2 = [0.60, 0.80]                             # Startbaelle bei h = 0,5 h_min
PU_TREIBER_H = [0.5, 0.8, 1.25, 2.0, 4.0]              # Treiber ohne Ball (Abzug und Gegenprobe)
PU_XIN, PU_XAUS = 90.0, 100.0
PU_T, PU_MESS = 600.0, 0.5

# ---- mi (Bio 22, Chemie 10) ----
M_L = 200.0                                            # periodische Box
M_S0 = [0.15, 0.35, 0.55, 0.63, 0.72, 0.85]            # instabil fuer S0 < 2/3
M_SAAT = [21, 22]
M_DELTA = 1e-6                                         # RMS des relativen Anfangsrauschens
M_ZUSATZ = [(0.35, 1e-3), (0.63, 1e-3)]                # staerkeres Rauschen, Saat 21
M_LOCH = [(0.72, 2.0), (0.72, 8.0), (0.85, 2.0), (0.85, 8.0)]   # volle Delle, Breite w (metastabil, Hypothese)
M_KMAX = 1.5
M_JMAX = 48                                            # gespeicherte Moden j = 0 .. 48 (k bis 1,51)
M_T, M_MESS = 400.0, 1.0
M_SNAP = 10                                            # Schnappschuss von S jede 10. Messung


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


# ---------------------------------------------------------------- Gitter, Anker (aus tests1d.py)

def gitter(dx):
    """Symmetrisches Gitter x_i = (i - i0) dx auf [-L, L]; x = 0 liegt genau auf einem Punkt."""
    i0 = int(round(L_BOX / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx


def gitter_periodisch(dx):
    """Periodisches Gitter der Laenge M_L, x = 0 auf einem Punkt (nur mi)."""
    n = int(round(M_L / dx))
    return (torch.arange(n, dtype=F64, device=DEV) - n // 2) * dx


def profil_anker_x(w2, x):
    """Analytischer 1D-Anker f^2 = 2 a0 / (1 + b0 cosh(2 sqrt(a0) x)) an beliebigen Orten x (auch CPU-Tensoren)."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    return torch.sqrt(2.0 * a0 / (1.0 + b0 * torch.cosh(2.0 * math.sqrt(a0) * x)))


def anker_wgv(w2):
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    integral = math.sqrt(2.0) * math.acosh(1.0 / b0)
    w = w2 * integral
    g = math.sqrt(a0) / 2.0 - b0 * b0 * integral / 4.0
    return w, g, w + g


def anker_q_e(w2):
    """Q und E des 1D-Ankers."""
    w, g, v = anker_wgv(w2)
    return 2.0 * w / math.sqrt(w2), w + g + v


def anker_umkehr(q):
    """omega^2 des 1D-Ankers mit der Ladung q (Q faellt mit omega^2), durch Einschachteln."""
    if not math.isfinite(q) or q <= 0.0:
        return NAN
    lo, hi = 0.5 + 1e-12, 1.0 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if anker_q_e(mid)[0] > q:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def fwhm(w2):
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    return math.acosh((1.0 + 2.0 * b0) / b0) / math.sqrt(a0)


def domega_dq(w2, h=1e-5):
    """d omega / dQ des 1D-Ankers (zentral, in omega^2 um w2)."""
    qa, qb = anker_q_e(w2 - h)[0], anker_q_e(w2 + h)[0]
    return (math.sqrt(w2 + h) - math.sqrt(w2 - h)) / (qb - qa)


def e_anker_zu_q(q):
    w2 = anker_umkehr(q)
    return anker_q_e(w2)[1] if math.isfinite(w2) else NAN


# ---------------------------------------------------------------- Felder

def null(x):
    z = torch.zeros(x.shape[0], dtype=C128, device=DEV)
    return z, z.clone()


def ball(x, w2, phase=0.0):
    """Ruhender Q-Ball psi = f(x) exp(i phase), psi_t = -i omega psi."""
    psi = profil_anker_x(w2, x) * complex(math.cos(phase), math.sin(phase))
    return psi, (-1j * math.sqrt(w2)) * psi


def summe(teile):
    return sum(p for p, _ in teile), sum(v for _, v in teile)


def stapel(felder, rand_null=True):
    """Liste (psi, psi_t) je Lauf -> zwei (B, N)-Stapel; Dirichlet-Rand ausser im periodischen Fall."""
    psi = torch.stack([p for p, _ in felder])
    vel = torch.stack([v for _, v in felder])
    if rand_null:
        for a in (psi, vel):
            a[:, 0] = 0.0
            a[:, -1] = 0.0
    return psi, vel


def rand_fenster(x, innen, aussen):
    """1 fuer |x| <= innen, cos^2-Uebergang, 0 ab |x| >= aussen."""
    u = ((x.abs() - innen) / (aussen - innen)).clamp(0.0, 1.0)
    return torch.cos(0.5 * PI * u) ** 2


def rausch_basis(x, saat, kmin, kmax, l_modi):
    """Bandbegrenztes Zufallsfeld als Summe ebener Wellen k_j = 2 pi j / l_modi, kmin <= |k_j| <= kmax, Gewicht
    1/sqrt(nu_k); Zufallszahlen auf der CPU mit fester Saat, daher auf jedem Gitter und Geraet dieselbe Funktion.
    psi und psi_t haben unabhaengige Koeffizienten (Teilchen und Antiteilchen, beide Richtungen); Normierung auf
    RMS |psi| = 1 ueber Parseval (nur aus den Koeffizienten, also gitterunabhaengig)."""
    gen = torch.Generator().manual_seed(saat)
    j0 = math.ceil(kmin * l_modi / (2.0 * PI))
    j1 = math.floor(kmax * l_modi / (2.0 * PI))
    kj = torch.arange(j0, j1 + 1, dtype=F64) * (2.0 * PI / l_modi)
    kk = torch.cat([kj, -kj])
    nu = torch.sqrt(1.0 + kk * kk)
    m = kk.shape[0]
    c1 = torch.complex(torch.randn(m, generator=gen, dtype=F64), torch.randn(m, generator=gen, dtype=F64))
    c2 = torch.complex(torch.randn(m, generator=gen, dtype=F64), torch.randn(m, generator=gen, dtype=F64))
    gew = 1.0 / torch.sqrt(nu)
    c1, c2 = c1 * gew, c2 * gew
    norm = math.sqrt(float((c1.abs() ** 2).sum()))
    kk, nu, c1, c2 = kk.to(DEV), nu.to(DEV), c1.to(DEV), c2.to(DEV)
    welle = torch.exp(1j * kk.unsqueeze(1) * x.unsqueeze(0))                  # (m, N)
    psi = (c1.unsqueeze(1) * welle).sum(0) / norm
    vel = ((-1j * nu * c2).unsqueeze(1) * welle).sum(0) / norm
    return psi, vel


# ---------------------------------------------------------------- Messhilfen

def dichte(psi):
    return psi.real ** 2 + psi.imag ** 2


def ladung(psi, vel):
    return 2.0 * (psi * vel.conj()).imag


def energie_dichte(psi, vel, dx, periodisch=False):
    s = dichte(psi)
    e = vel.real ** 2 + vel.imag ** 2 + s - s * s + 0.5 * s ** 3
    if periodisch:
        g = (torch.roll(psi, -1, dims=1) - psi) / dx
        e = e + g.real ** 2 + g.imag ** 2
    else:
        g = (psi[:, 1:] - psi[:, :-1]) / dx
        e[:, :-1] += g.real ** 2 + g.imag ** 2
    return e


def max_im_fenster(psi, s, maske):
    """Index (B, 1) des Maximums von |psi|^2 im Fenster und psi dort (B, 1)."""
    i = (s * maske).argmax(dim=1, keepdim=True)
    return i, psi.gather(1, i)


def breite_s(x, s, maske):
    """Standardabweichung von |psi|^2 im Fenster (aus tests1d.py)."""
    m = (s * maske).sum(1).clamp(min=1e-300)
    mitte = (x * s * maske).sum(1) / m
    return torch.sqrt(((x - mitte.unsqueeze(1)) ** 2 * s * maske).sum(1) / m)


# ---------------------------------------------------------------- Zeitentwicklung (Schritt aus tests1d.py)

def entwickeln(psi, vel, dx, dt, t_end, t_mess, messen, gamma=None, antrieb=None, periodisch=False):
    """Velocity-Verlet fuer alle Laeufe als ein Stapel (B x N). messen(psi, vel, t) -> (B, m) alle t_mess.
    gamma: (B,) zusaetzliche gleichmaessige Daempfung; antrieb(t) -> (B, N) Kraftterm; periodisch: Rand ohne Schicht."""
    n = psi.shape[1]
    if periodisch:
        sig = torch.zeros(1, n, dtype=F64, device=DEV)
    else:
        x = gitter(dx)
        sig = (SIGMA0 * ((x.abs() - X_SPONGE).clamp(min=0.0) / (L_BOX - X_SPONGE)) ** 2).unsqueeze(0)
    if gamma is not None:
        sig = sig + gamma.unsqueeze(1)

    def kraft(psi, t):
        if periodisch:
            lap = (torch.roll(psi, 1, dims=1) - 2.0 * psi + torch.roll(psi, -1, dims=1)) / (dx * dx)
        else:
            fluss = (psi[:, 1:] - psi[:, :-1]) / dx
            lap = torch.zeros_like(psi)
            lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = psi.real ** 2 + psi.imag ** 2
        k = lap - (1.0 - 2.0 * s + 1.5 * s * s) * psi
        if antrieb is not None:
            k = k + antrieb(t)
        return k

    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(t_mess / dt)))
    reihe = [messen(psi, vel, 0.0)]
    kr = kraft(psi, 0.0)
    for j in range(1, n_schritte + 1):
        vel = vel + (0.5 * dt) * (kr - sig * vel)
        psi = psi + dt * vel
        kr = kraft(psi, j * dt)
        vel = vel + (0.5 * dt) * (kr - sig * vel)
        if j % alle == 0:
            reihe.append(messen(psi, vel, j * dt))
    daten = torch.stack(reihe)                   # (M, B, m)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
    return t, daten


def stufen_rechnen(name, bauen, t_end, t_mess, periodisch=False):
    """Grob (dx, dt) und fein (dx/2, dt/2). bauen(x, dx) -> dict psi, vel, messen [, gamma, antrieb, extra]."""
    aus = {}
    for stufe, dx, dt in (("grob", DX, DT), ("fein", DX * FEIN, DT * FEIN)):
        x = gitter_periodisch(dx) if periodisch else gitter(dx)
        b = bauen(x, dx)
        t0 = uhr()
        t, daten = entwickeln(b["psi"], b["vel"], dx, dt, t_end, t_mess, b["messen"], b.get("gamma"),
                              b.get("antrieb"), periodisch)
        sek = uhr() - t0
        print(f"{name} {stufe}: {b['psi'].shape[0]} Laeufe x {b['psi'].shape[1]} Punkte, T = {t_end}, {sek:.1f} s",
              flush=True)
        aus[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "sek": sek, "extra": b.get("extra", {})}
        ROH[name] = aus                      # Rohdaten bleiben erhalten, auch wenn die Auswertung scheitert
    return aus


# ---------------------------------------------------------------- Auswerte-Hilfen

def wrap(a):
    return torch.remainder(a + PI, 2.0 * PI) - PI


def entfalten(th):
    """Phasenreihe stetig machen; Schritte muessen unter pi liegen (omega * t_mess < pi)."""
    return torch.cat([th[:1], th[:1] + torch.cumsum(wrap(th[1:] - th[:-1]), dim=0)], dim=0)


def ende(y):
    """Mittel ueber die letzten 10 % der Proben (mindestens eine)."""
    n = max(1, y.shape[0] // 10)
    return float(y[-n:].mean())


def fenster_idx(t, t_a, t_b):
    return torch.nonzero((t >= t_a - 1e-9) & (t <= t_b + 1e-9)).squeeze(1)


def om_fenster(t, th, t_a, t_b):
    """Mittlere Phasendrehrate (omega) im Zeitfenster aus der entfalteten Phase."""
    idx = fenster_idx(t, t_a, t_b)
    if idx.numel() < 2:
        return NAN
    thu = entfalten(th)
    i0, i1 = int(idx[0]), int(idx[-1])
    return float((thu[i1] - thu[i0]) / (t[i1] - t[i0]))


def steigung(t, y, t_a, t_b):
    idx = fenster_idx(t, t_a, t_b)
    if idx.numel() < 3:
        return NAN
    tt, yy = t[idx], y[idx]
    tm, ym = tt.mean(), yy.mean()
    return float(((tt - tm) * (yy - ym)).sum() / ((tt - tm) ** 2).sum())


def mittel(t, y, t_a, t_b):
    idx = fenster_idx(t, t_a, t_b)
    return float(y[idx].mean()) if idx.numel() > 0 else NAN


def rms_trendfrei(t, y, t_a, t_b):
    idx = fenster_idx(t, t_a, t_b)
    if idx.numel() < 3:
        return NAN
    tt, yy = t[idx], y[idx]
    tm, ym = tt.mean(), yy.mean()
    b = ((tt - tm) * (yy - ym)).sum() / ((tt - tm) ** 2).sum()
    rest = yy - ym - b * (tt - tm)
    return float(rest.pow(2).mean().sqrt())


def spektrum(t, y, t_ab, n_spitzen=3):
    """Groesste Spitzen der FFT von y ab t_ab (Trend entfernt, Hann-Fenster), Kreisfrequenz Omega (aus tests1d.py,
    Trendabzug hier ohne lstsq)."""
    wahl = t >= t_ab - 1e-9
    ts, ys = t[wahl], y[wahl]
    n = ys.shape[0]
    if n < 16:
        return []
    tm, ym = ts.mean(), ys.mean()
    b = ((ts - tm) * (ys - ym)).sum() / ((ts - tm) ** 2).sum()
    rest = ys - ym - b * (ts - tm)
    fen = torch.hann_window(n, periodic=False, dtype=F64, device=ys.device)
    amp = torch.fft.rfft(rest * fen).abs()
    d_om = 2.0 * PI / (n * float(ts[1] - ts[0]))
    lok = (amp[1:-1] > amp[:-2]) & (amp[1:-1] >= amp[2:])
    kand = torch.nonzero(lok).squeeze(1) + 1
    kand = kand[kand >= 2]
    kand = kand[amp[kand].argsort(descending=True)][:n_spitzen]
    aus = []
    for k in kand.tolist():
        a, bb, c = float(amp[k - 1]), float(amp[k]), float(amp[k + 1])
        nenner = a - 2.0 * bb + c
        delta = 0.5 * (a - c) / nenner if nenner != 0.0 else 0.0
        aus.append({"Omega": (k + delta) * d_om, "amplitude": 2.0 * bb / float(fen.sum())})
    return aus


def spitzen_text(sp):
    return ", ".join(f"{s['Omega']:.4f} ({s['amplitude']:.1e})" for s in sp) if sp else "-"


def l3(wert_grob, wert_fein, null_wert):
    """Latte L3: Effekt (Abstand vom Nullwert) mindestens fuenfmal so gross wie die Aenderung grob -> fein."""
    if not (math.isfinite(wert_grob) and math.isfinite(wert_fein)):
        return {"effekt": NAN, "aenderung": NAN, "bestanden": False}
    eff, aend = abs(wert_grob - null_wert), abs(wert_fein - wert_grob)
    return {"effekt": eff, "aenderung": aend, "bestanden": bool(eff >= 5.0 * aend)}


def teilen(a, b):
    return a / b if (b != 0.0 and math.isfinite(b)) else NAN


def l3_text(liste, schluessel):
    n = sum(1 for e in liste if e[schluessel]["bestanden"])
    return f"{n} von {len(liste)}"


# ---------------------------------------------------------------- fuettern (Bio 3)

def paket(x, nu, eps, vz):
    """Wellenpaket von links (aus tests1d.py), Amplitude eps; vz = -1: Antiteilchen (komplex konjugiert)."""
    k = math.sqrt(nu * nu - 1.0)
    vg = k / nu
    psi = eps * torch.exp(-((x - F_X0) ** 2) / (2.0 * F_SIGMA ** 2)) * torch.exp(1j * k * (x - F_X0))
    vel = (-1j * nu + vg * (x - F_X0) / F_SIGMA ** 2) * psi
    if vz < 0:
        return torch.conj_physical(psi), torch.conj_physical(vel)
    return psi, vel


def born_aq(w2, nu, vz):
    """Born-Naeherung fuer den linearen Umwandlungskanal: Teilchen nu -> Antiteilchen nu - 2 omega (offen fuer
    nu > 2 omega + 1; Ball gewinnt 2 je Umwandlung) bzw. Antiteilchen nu -> Teilchen nu + 2 omega (immer offen; Ball
    verliert 2). Kopplung V2 = U''(S) S = -2 S + 3 S^2. Rueckgabe: Ladungsgewinn des Balls / |einfallende Ladung|."""
    om = math.sqrt(w2)
    k_ein = math.sqrt(nu * nu - 1.0)
    nu_aus = nu - 2.0 * om if vz > 0 else nu + 2.0 * om
    if abs(nu_aus) <= 1.0:
        return 0.0
    k_aus = math.sqrt(nu_aus * nu_aus - 1.0)
    xs = torch.arange(-6000, 6001, dtype=F64) * 0.01
    s = profil_anker_x(w2, xs) ** 2
    v2 = -2.0 * s + 3.0 * s * s

    def ft(q):
        return float((v2 * torch.cos(q * xs)).sum()) * 0.01

    p = (ft(k_ein - k_aus) ** 2 + ft(k_ein + k_aus) ** 2) / (4.0 * k_ein * k_aus)
    return 2.0 * p if vz > 0 else -2.0 * p


def fuettern_laeufe():
    laeufe = []
    for w2 in F_W2:
        for nu in F_NU:
            for eps in F_EPS:
                laeufe.append({"art": "ball+paket", "w2": w2, "nu": nu, "eps": eps, "vz": 1})
    for w2, nu in F_ANTI:
        laeufe.append({"art": "ball+paket", "w2": w2, "nu": nu, "eps": 0.01, "vz": -1})
    pakete = []
    for r in laeufe:
        schl = (r["nu"], r["eps"], r["vz"])
        if schl not in pakete:
            pakete.append(schl)
    for nu, eps, vz in pakete:
        laeufe.append({"art": "paket", "w2": None, "nu": nu, "eps": eps, "vz": vz})
    for w2 in F_W2:
        laeufe.append({"art": "ball", "w2": w2, "nu": None, "eps": 0.0, "vz": 0})
    return laeufe


def fuettern(faktor):
    laeufe = fuettern_laeufe()

    def bauen(x, dx):
        felder = []
        for r in laeufe:
            teile = []
            if r["art"] in ("ball+paket", "ball"):
                teile.append(ball(x, r["w2"]))
            if r["art"] in ("ball+paket", "paket"):
                teile.append(paket(x, r["nu"], r["eps"], r["vz"]))
            felder.append(summe(teile))
        psi, vel = stapel(felder)
        maske = (x.abs() < W_FENSTER).to(F64)

        def messen(psi, vel, t):
            s = dichte(psi)
            rho = ladung(psi, vel)
            e = energie_dichte(psi, vel, dx)
            i, p = max_im_fenster(psi, s, maske)
            return torch.stack([(rho * maske).sum(1) * dx, (e * maske).sum(1) * dx, -torch.angle(p[:, 0]),
                                s.gather(1, i)[:, 0], x[i[:, 0]], rho.sum(1) * dx, e.sum(1) * dx], dim=1)
        return {"psi": psi, "vel": vel, "messen": messen}

    stufen = stufen_rechnen("fuettern", bauen, F_T * faktor, F_MESS)
    erg = {s: auswertung_fuettern(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "C_Q": l3(zg["C_Q"], zf["C_Q"], 0.0)}
                for zg, zf in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"])]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def auswertung_fuettern(laeufe, t, d):
    qw, ew, th, smax, xm, qb, eb = d.unbind(dim=2)
    T = float(t[-1])
    i_ball = {r["w2"]: b for b, r in enumerate(laeufe) if r["art"] == "ball"}
    i_pak = {(r["nu"], r["eps"], r["vz"]): b for b, r in enumerate(laeufe) if r["art"] == "paket"}
    zeilen = []
    for b, r in enumerate(laeufe):
        if r["art"] != "ball+paket":
            continue
        ib, ip = i_ball[r["w2"]], i_pak[(r["nu"], r["eps"], r["vz"])]
        dq = ende(qw[:, b]) - ende(qw[:, ib]) - ende(qw[:, ip])
        de = ende(ew[:, b]) - ende(ew[:, ib]) - ende(ew[:, ip])
        qp, ep = float(qb[0, ip]), float(eb[0, ip])
        om = math.sqrt(r["w2"])
        om_r = om_fenster(t, th[:, b], 0.75 * T, T)
        om_b = om_fenster(t, th[:, ib], 0.75 * T, T)
        schwelle = 2.0 * om + 1.0
        zeilen.append({"name": f"w2={r['w2']} nu={r['nu']} eps={r['eps']} vz={r['vz']:+d}", "w2": r["w2"],
                       "nu": r["nu"], "eps": r["eps"], "vz": r["vz"], "Q_paket": qp, "E_paket": ep,
                       "dQ_ball": dq, "dE_ball": de, "C_Q": teilen(dq, abs(qp)), "C_E": teilen(de, ep),
                       "dE_durch_dQ": teilen(de, dq), "omega": om, "nu_schwelle": schwelle,
                       "ueber_schwelle": bool(r["nu"] > schwelle), "born_C_Q": born_aq(r["w2"], r["nu"], r["vz"]),
                       "d_omega": om_r - om_b, "d_omega_soll": domega_dq(r["w2"]) * dq,
                       "x_ball_ende": ende(xm[:, b])})
    # Sprung an der Schwelle (eps = 0,01, Teilchen) und Amplitudenverhaeltnis
    sprung = []
    for w2 in F_W2:
        reihe = [z for z in zeilen if z["w2"] == w2 and z["eps"] == 0.01 and z["vz"] == 1]
        unter = [abs(z["C_Q"]) for z in reihe if not z["ueber_schwelle"] and math.isfinite(z["C_Q"])]
        ueber = [z["C_Q"] for z in reihe if z["ueber_schwelle"]]
        if unter and ueber:
            sprung.append({"w2": w2, "max_unter": max(unter), "erster_ueber": ueber[0],
                           "faktor": teilen(ueber[0], max(max(unter), 1e-15))})
    verh = []
    for w2 in F_W2:
        for nu in F_NU:
            a = [z for z in zeilen if z["w2"] == w2 and z["nu"] == nu and z["vz"] == 1]
            c = {z["eps"]: z["C_Q"] for z in a}
            if 0.01 in c and 0.05 in c:
                verh.append({"w2": w2, "nu": nu, "ueber_schwelle": bool(nu > 2.0 * math.sqrt(w2) + 1.0),
                             "C_Q_005_durch_001": teilen(c[0.05], c[0.01])})
    return {"zeilen": zeilen, "sprung": sprung, "amplitudenverhaeltnis": verh}


def bericht_fuettern(res):
    zz = [f"fuettern (Bio 3): Pakete sigma = {F_SIGMA}, x0 = {F_X0}, Fenster |x| < {W_FENSTER}, T = Laufzeit.",
          "  C_Q = Ladungsgewinn des Balls / |Paketladung| (Ball+Paket - Ball - Paket, Mittel letzte 10 %); "
          "Schwelle nu > 2 omega + 1; born = lineare Born-Schaetzung",
          "  Lauf | ueber | C_Q | born | C_E | dE/dQ (omega) | d omega (Soll aus dQ) | x Ball Ende"]
    for stufe in ("grob", "fein"):
        e = res["ergebnis"][stufe]
        zz.append(f"  [{stufe}]")
        for z in e["zeilen"]:
            zz.append(f"  {z['name']:30s} | {str(z['ueber_schwelle']):5s} | {z['C_Q']:+.3e} | {z['born_C_Q']:+.2e} | "
                      f"{z['C_E']:+.3e} | {z['dE_durch_dQ']:.4f} ({z['omega']:.4f}) | {z['d_omega']:+.2e} "
                      f"({z['d_omega_soll']:+.2e}) | {z['x_ball_ende']:+.3f}")
        for s in e["sprung"]:
            zz.append(f"  Sprung w2 = {s['w2']}: max |C_Q| unter der Schwelle {s['max_unter']:.2e}, erster Wert "
                      f"darueber {s['erster_ueber']:+.2e}, Faktor {s['faktor']:.1f}")
        for v in e["amplitudenverhaeltnis"]:
            zz.append(f"  C_Q(0,05)/C_Q(0,01) w2 = {v['w2']}, nu = {v['nu']} (ueber {v['ueber_schwelle']}): "
                      f"{v['C_Q_005_durch_001']:.2f}")
    zz.append(f"  L3 fuer C_Q: {l3_text(res['L3'], 'C_Q')} Laeufe bestanden")
    return zz


# ---------------------------------------------------------------- photo (Bio 36)

def photo_laeufe():
    laeufe = []
    for w2, nus in P_NU.items():
        for nu in nus:
            laeufe.append({"art": "ball+welle", "w2": w2, "nu": nu, "eps": P_EPS, "vz": 1})
    for w2, nu, eps, vz in P_ZUSATZ:
        laeufe.append({"art": "ball+welle", "w2": w2, "nu": nu, "eps": eps, "vz": vz})
    wellen = []
    for r in laeufe:
        schl = (r["nu"], r["eps"], r["vz"])
        if schl not in wellen:
            wellen.append(schl)
    for nu, eps, vz in wellen:
        laeufe.append({"art": "welle", "w2": None, "nu": nu, "eps": eps, "vz": vz})
    for w2 in P_NU:
        laeufe.append({"art": "ball", "w2": w2, "nu": None, "eps": 0.0, "vz": 0})
    return laeufe


def photo(faktor):
    laeufe = photo_laeufe()

    def bauen(x, dx):
        felder, f0, nuv = [], [], []
        for r in laeufe:
            felder.append(ball(x, r["w2"]) if r["w2"] is not None else null(x))
            if r["nu"] is not None:
                k = math.sqrt(r["nu"] ** 2 - 1.0)
                # Quelle F0 g(x) exp(-i nu t) strahlt nach beiden Seiten |a| = F0 w sqrt(2 pi) exp(-k^2 w^2/2) / (2 k)
                f0.append(2.0 * k * r["eps"] * math.exp(0.5 * (k * P_WS) ** 2) / (P_WS * math.sqrt(2.0 * PI)))
                nuv.append(r["vz"] * r["nu"])
            else:
                f0.append(0.0)
                nuv.append(0.0)
        psi, vel = stapel(felder)
        f0t = torch.tensor(f0, dtype=F64, device=DEV)
        nut = torch.tensor(nuv, dtype=F64, device=DEV)
        g = torch.exp(-((x - P_XS) ** 2) / (2.0 * P_WS ** 2))

        def antrieb(t):
            r = math.sin(0.5 * PI * t / P_RAMPE) ** 2 if t < P_RAMPE else 1.0
            amp = (f0t * r) * torch.exp(-1j * nut * t)
            return amp.unsqueeze(1) * g.unsqueeze(0)

        maske = (x.abs() < W_FENSTER).to(F64)
        ij = int(round((P_XJ + L_BOX) / dx))

        def messen(psi, vel, t):
            s = dichte(psi)
            rho = ladung(psi, vel)
            e = energie_dichte(psi, vel, dx)
            i, p = max_im_fenster(psi, s, maske)
            px = (psi[:, ij + 1] - psi[:, ij - 1]) / (2.0 * dx)
            jl = -2.0 * (psi[:, ij] * px.conj()).imag
            return torch.stack([(rho * maske).sum(1) * dx, (e * maske).sum(1) * dx, -torch.angle(p[:, 0]),
                                s.gather(1, i)[:, 0], x[i[:, 0]], jl, rho.sum(1) * dx, e.sum(1) * dx], dim=1)
        return {"psi": psi, "vel": vel, "messen": messen, "antrieb": antrieb}

    stufen = stufen_rechnen("photo", bauen, P_T * faktor, P_MESS)
    erg = {s: auswertung_photo(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "Gamma": l3(zg["Gamma"], zf["Gamma"], 0.0)}
                for zg, zf in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"])]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def auswertung_photo(laeufe, t, d):
    qw, ew, th, smax, xm, jl, qb, eb = d.unbind(dim=2)
    T = float(t[-1])
    i_ball = {r["w2"]: b for b, r in enumerate(laeufe) if r["art"] == "ball"}
    i_wel = {(r["nu"], r["eps"], r["vz"]): b for b, r in enumerate(laeufe) if r["art"] == "welle"}
    zeilen = []
    for b, r in enumerate(laeufe):
        if r["art"] != "ball+welle":
            continue
        ib, iw = i_ball[r["w2"]], i_wel[(r["nu"], r["eps"], r["vz"])]
        dq = qw[:, b] - qw[:, ib] - qw[:, iw]
        de = ew[:, b] - ew[:, ib] - ew[:, iw]
        g_q = steigung(t, dq, 0.5 * T, T)
        g_e = steigung(t, de, 0.5 * T, T)
        j_ein = mittel(t, jl[:, iw], 0.5 * T, T)
        k = math.sqrt(r["nu"] ** 2 - 1.0)
        om = math.sqrt(r["w2"])
        om1 = om_fenster(t, th[:, b], 0.5 * T, 0.75 * T) - om_fenster(t, th[:, ib], 0.5 * T, 0.75 * T)
        om2 = om_fenster(t, th[:, b], 0.75 * T, T) - om_fenster(t, th[:, ib], 0.75 * T, T)
        zeilen.append({"name": f"w2={r['w2']} nu={r['nu']} eps={r['eps']} vz={r['vz']:+d}", "w2": r["w2"],
                       "nu": r["nu"], "eps": r["eps"], "vz": r["vz"], "omega": om, "nu_schwelle": 2.0 * om + 1.0,
                       "ueber_schwelle": bool(r["nu"] > 2.0 * om + 1.0), "G_Q": g_q, "G_E": g_e, "J_ein": j_ein,
                       "J_ein_soll": r["vz"] * 2.0 * k * r["eps"] ** 2, "Gamma": teilen(g_q, abs(j_ein)),
                       "born_Gamma": born_aq(r["w2"], r["nu"], r["vz"]), "G_E_durch_G_Q": teilen(g_e, g_q),
                       "dQ_Ende": ende(dq), "domega_dt": (om2 - om1) / (0.25 * T) if T > 0 else NAN,
                       "domega_dt_soll": domega_dq(r["w2"]) * g_q})
    return {"zeilen": zeilen}


def bericht_photo(res):
    zz = [f"photo (Bio 36): Quelle bei x = {P_XS} (Breite {P_WS}, Anlauf {P_RAMPE}), Fenster |x| < {W_FENSTER}; "
          "Wachstum G = Steigung von Q(Ball+Welle) - Q(Ball) - Q(Welle) in [T/2, T]; Gamma = G / |Einstrom|",
          "  Lauf | ueber | Gamma | born | G_Q | J_ein (Soll) | G_E/G_Q (omega) | dQ Ende | d omega/dt (Soll)"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]["zeilen"]:
            zz.append(f"  {z['name']:30s} | {str(z['ueber_schwelle']):5s} | {z['Gamma']:+.3e} | {z['born_Gamma']:+.2e} | "
                      f"{z['G_Q']:+.2e} | {z['J_ein']:+.3e} ({z['J_ein_soll']:+.3e}) | {z['G_E_durch_G_Q']:.4f} "
                      f"({z['omega']:.4f}) | {z['dQ_Ende']:+.2e} | {z['domega_dt']:+.1e} ({z['domega_dt_soll']:+.1e})")
    zz.append(f"  L3 fuer Gamma: {l3_text(res['L3'], 'Gamma')} Laeufe bestanden")
    return zz


# ---------------------------------------------------------------- winterschlaf (Bio 38)

def winterschlaf_laeufe():
    laeufe = []
    for w2 in W_W2:
        laeufe.append({"art": "ball", "w2": w2, "A": 0.0})
        for a in W_A:
            laeufe.append({"art": "druck", "w2": w2, "A": a})
    laeufe.append({"art": "relativ", "w2": 0.70, "A": W_ETA})
    return laeufe


def winterschlaf(faktor):
    laeufe = winterschlaf_laeufe()

    def bauen(x, dx):
        felder = []
        stoss = torch.exp(-x ** 2 / (2.0 * W_BREITE ** 2))
        for r in laeufe:
            p, v = ball(x, r["w2"])
            if r["art"] == "druck":
                p = p + r["A"] * stoss
            elif r["art"] == "relativ":
                p, v = (1.0 + r["A"]) * p, (1.0 + r["A"]) * v
            felder.append((p, v))
        psi, vel = stapel(felder)
        maske = (x.abs() < W_FENSTER).to(F64)

        def messen(psi, vel, t):
            s = dichte(psi)
            rho = ladung(psi, vel)
            e = energie_dichte(psi, vel, dx)
            i, p = max_im_fenster(psi, s, maske)
            return torch.stack([(rho * maske).sum(1) * dx, (e * maske).sum(1) * dx, breite_s(x, s, maske),
                                s.gather(1, i)[:, 0], -torch.angle(p[:, 0]), x[i[:, 0]]], dim=1)
        return {"psi": psi, "vel": vel, "messen": messen}

    stufen = stufen_rechnen("winterschlaf", bauen, W_T * faktor, W_MESS)
    erg = {s: auswertung_winterschlaf(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = []
    for zg, zf in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"]):
        l3_liste.append({"lauf": zg["name"], "Omega": l3(zg["Omega_haupt"], zf["Omega_haupt"], 0.0),
                         "antwort": l3(zg["antwort"], zf["antwort"], 0.0), "rest": l3(zg["rest"], zf["rest"], 0.0)})
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def auswertung_winterschlaf(laeufe, t, d):
    qw, ew, br, sm, th, xm = d.unbind(dim=2)
    T = float(t[-1])
    i_ball = {r["w2"]: b for b, r in enumerate(laeufe) if r["art"] == "ball"}
    zeilen = []
    for b, r in enumerate(laeufe):
        if r["art"] == "ball":
            continue
        ib = i_ball[r["w2"]]
        om = math.sqrt(r["w2"])
        de0 = float(ew[0, b] - ew[0, ib])
        dq0 = float(qw[0, b] - qw[0, ib])
        db = br[:, b] - br[:, ib]
        ds = sm[:, b] - sm[:, ib]
        idx = fenster_idx(t, 0.25 * T, T)
        if idx.numel() > 1:
            antwort = float(db[idx].max() - db[idx].min()) / float(br[0, ib]) / r["A"]
            antwort_s = float(ds[idx].pow(2).mean().sqrt()) / float(sm[0, ib]) / r["A"]
        else:
            antwort, antwort_s = NAN, NAN
        sp = spektrum(t, db, T / 8.0)
        om_h = sp[0]["Omega"] if sp else NAN
        frueh = rms_trendfrei(t, db, 0.25 * T, 0.5 * T)
        spaet = rms_trendfrei(t, db, 0.75 * T, T)
        q_r, e_r, q_b, e_b = ende(qw[:, b]), ende(ew[:, b]), ende(qw[:, ib]), ende(ew[:, ib])
        anregung = (e_r - e_anker_zu_q(q_r)) - (e_b - e_anker_zu_q(q_b))
        zeilen.append({"name": f"{r['art']} w2={r['w2']} A={r['A']}", "art": r["art"], "w2": r["w2"], "A": r["A"],
                       "omega": om, "kante": 1.0 - om, "dE_stoss": de0, "dQ_stoss": dq0, "antwort": antwort,
                       "antwort_S": antwort_s, "spektrum": sp, "Omega_haupt": om_h,
                       "Omega_durch_kante": om_h / (1.0 - om), "abkling": teilen(spaet, frueh),
                       "anregung_ende": anregung, "rest": teilen(anregung, de0),
                       "dQ_ende": q_r - q_b, "d_omega_ende": om_fenster(t, th[:, b], 0.75 * T, T)
                       - om_fenster(t, th[:, ib], 0.75 * T, T), "d_omega_soll": domega_dq(r["w2"]) * (q_r - q_b)})
    trend = []
    for a in W_A:
        reihe = [z for z in zeilen if z["art"] == "druck" and z["A"] == a]
        for schl in ("antwort", "rest", "abkling"):
            werte = [z[schl] for z in reihe]
            steigend = sum(1 for i in range(len(werte) - 1) if werte[i + 1] > werte[i])
            trend.append({"A": a, "groesse": schl, "steigend_mit_w2": steigend, "paare": len(werte) - 1,
                          "verh_090_zu_055": teilen(werte[-1], werte[0]) if werte else NAN})
    return {"zeilen": zeilen, "trend": trend}


def bericht_winterschlaf(res):
    zz = [f"winterschlaf (Bio 38): Stoss psi -> psi + A exp(-x^2/2) (druck) bzw. x (1 + {W_ETA}) (relativ); "
          "Differenz zum ungestossenen Ball; Kante = 1 - omega",
          "  Lauf | dE Stoss | Omega Haupt (Kante, Verh.) | Antwort Breite/A | Antwort S/A | Abkling spaet/frueh | "
          "Rest Anregung/dE | Spektrum"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]["zeilen"]:
            zz.append(f"  {z['name']:24s} | {z['dE_stoss']:.3e} | {z['Omega_haupt']:.4f} ({z['kante']:.4f}, "
                      f"{z['Omega_durch_kante']:.3f}) | {z['antwort']:.3e} | {z['antwort_S']:.3e} | {z['abkling']:.3f} | "
                      f"{z['rest']:+.3f} | {spitzen_text(z['spektrum'])}")
        for tr in res["ergebnis"][stufe]["trend"]:
            zz.append(f"  Trend A = {tr['A']}, {tr['groesse']}: steigend in {tr['steigend_mit_w2']} von {tr['paare']} "
                      f"Schritten; Verhaeltnis 0,90 / 0,55 = {tr['verh_090_zu_055']:.3f}")
    n = sum(1 for e in res["L3"] for k in ("Omega", "antwort", "rest") if e[k]["bestanden"])
    zz.append(f"  L3 (Omega, Antwort, Rest): {n} von {3 * len(res['L3'])} bestanden")
    return zz


# ---------------------------------------------------------------- rauschen (Bio 20/37)

def rauschen_laeufe():
    laeufe = [{"art": "ball", "w2": w2, "eps": 0.0, "saat": None} for w2 in R_W2]
    for w2 in R_W2:
        for eps in R_EPS:
            for saat in R_SAAT:
                laeufe.append({"art": "ball+rauschen", "w2": w2, "eps": eps, "saat": saat})
    for eps in R_EPS:
        for saat in R_SAAT:
            laeufe.append({"art": "rauschen", "w2": None, "eps": eps, "saat": saat})
    return laeufe


def rauschen(faktor):
    laeufe = rauschen_laeufe()

    def bauen(x, dx):
        rand = rand_fenster(x, R_XIN, R_XAUS)
        basis = {}
        for saat in R_SAAT:
            p, v = rausch_basis(x, saat, R_KMIN, R_KMAX, R_LMODI)
            basis[saat] = (p * rand, v * rand)
        felder = []
        for r in laeufe:
            teile = [ball(x, r["w2"])] if r["w2"] is not None else [null(x)]
            if r["saat"] is not None:
                p, v = basis[r["saat"]]
                teile.append((r["eps"] * p, r["eps"] * v))
            felder.append(summe(teile))
        psi, vel = stapel(felder)
        zentrum = torch.zeros(psi.shape[0], dtype=F64, device=DEV)
        mz = (x.abs() < W_FENSTER).to(F64)

        def messen(psi, vel, t):
            s = dichte(psi)
            rho = ladung(psi, vel)
            for _ in range(2):                       # Mean-shift: Schwerpunkt von |psi|^2 in +-R_WT
                m = ((x.unsqueeze(0) - zentrum.unsqueeze(1)).abs() < R_WT).to(F64)
                masse = (s * m).sum(1)
                neu = (s * m * x.unsqueeze(0)).sum(1) / masse.clamp(min=1e-300)
                zentrum.copy_(torch.where(masse > 0, neu, zentrum))
            abst = (x.unsqueeze(0) - zentrum.unsqueeze(1)).abs()
            qball = (rho * (abst < R_WB).to(F64)).sum(1) * dx
            speak = (s * (abst < 2.0).to(F64)).max(dim=1).values
            e = energie_dichte(psi, vel, dx)
            return torch.stack([zentrum.clone(), qball, speak, (rho * mz).sum(1) * dx, rho.sum(1) * dx,
                                e.sum(1) * dx], dim=1)
        return {"psi": psi, "vel": vel, "messen": messen}

    stufen = stufen_rechnen("rauschen", bauen, R_T * faktor, R_MESS)
    erg = {s: auswertung_rauschen(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "R_Q": l3(zg["R_Q"], zf["R_Q"], 1.0)}
                for zg, zf in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"])]
    l3_schwelle = [{"w2": sg["w2"], "eps_c": l3(sg["eps_c"], sf["eps_c"], 0.0)}
                   for sg, sf in zip(erg["grob"]["schwellen"], erg["fein"]["schwellen"])]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "L3_schwelle": l3_schwelle,
            "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def auswertung_rauschen(laeufe, t, d):
    zent, qball, speak, qz, qbox, ebox = d.unbind(dim=2)
    i_ball = {r["w2"]: b for b, r in enumerate(laeufe) if r["art"] == "ball"}
    i_rau = {(r["eps"], r["saat"]): b for b, r in enumerate(laeufe) if r["art"] == "rauschen"}
    zeilen = []
    for b, r in enumerate(laeufe):
        if r["art"] != "ball+rauschen":
            continue
        ib, ir = i_ball[r["w2"]], i_rau[(r["eps"], r["saat"])]
        q0, s0 = float(qball[0, ib]), float(speak[0, ib])
        rq, rs = ende(qball[:, b]) / q0, ende(speak[:, b]) / s0
        zeilen.append({"name": f"w2={r['w2']} eps={r['eps']} saat={r['saat']}", "w2": r["w2"], "eps": r["eps"],
                       "saat": r["saat"], "R_Q": rq, "R_S": rs, "lebt": bool(rq >= 0.5 and rs >= 0.5),
                       "schein_Q": ende(qball[:, ir]) / q0, "schein_S": ende(speak[:, ir]) / s0,
                       "dQ_rel": (ende(qball[:, b]) - ende(qball[:, ib])) / q0, "x_ende": ende(zent[:, b]),
                       "Q_rauschen": float(qbox[0, ir]), "E_rauschen": float(ebox[0, ir])})
    schwellen = []
    for w2 in R_W2:
        mittelwerte = []
        for eps in R_EPS:
            werte = [z["R_Q"] for z in zeilen if z["w2"] == w2 and z["eps"] == eps]
            mittelwerte.append(sum(werte) / len(werte))
        eps_c = NAN
        for i in range(len(R_EPS)):
            if mittelwerte[i] < 0.5:
                if i == 0:
                    eps_c = R_EPS[0]
                else:
                    r1, r2 = mittelwerte[i - 1], mittelwerte[i]
                    la, lb = math.log(R_EPS[i - 1]), math.log(R_EPS[i])
                    eps_c = math.exp(la + (lb - la) * (r1 - 0.5) / (r1 - r2))
                break
        q_a, e_a = anker_q_e(w2)
        schwellen.append({"w2": w2, "Q": q_a, "f0": math.sqrt(1.0 - math.sqrt(2.0 * w2 - 1.0)),
                          "bindung_Q_minus_E": q_a - e_a, "mittel_R_Q": mittelwerte, "eps_c": eps_c})
    return {"zeilen": zeilen, "schwellen": schwellen}


def bericht_rauschen(res):
    zz = [f"rauschen (Bio 20/37): Band {R_KMIN} <= |k| <= {R_KMAX}, Gewicht 1/sqrt(nu), |x| < {R_XIN}; R_Q = Ladung in "
          f"+-{R_WB} um die Ballmitte am Ende / Anfang; lebt: R_Q >= 0,5 und Spitze >= 0,5",
          "  Lauf | R_Q | R_S | lebt | Schein (nur Rauschen) Q, S | dQ/Q gegen Ball allein | x Ende | Q Rauschen"]
    for stufe in ("grob", "fein"):
        e = res["ergebnis"][stufe]
        zz.append(f"  [{stufe}]")
        for z in e["zeilen"]:
            zz.append(f"  {z['name']:24s} | {z['R_Q']:.4f} | {z['R_S']:.4f} | {str(z['lebt']):5s} | "
                      f"{z['schein_Q']:+.3f}, {z['schein_S']:.3f} | {z['dQ_rel']:+.2e} | {z['x_ende']:+.2f} | "
                      f"{z['Q_rauschen']:+.3f}")
        for s in e["schwellen"]:
            zz.append(f"  Schwelle w2 = {s['w2']} (Q {s['Q']:.3f}, f0 {s['f0']:.3f}, Q - E {s['bindung_Q_minus_E']:.4f}): "
                      f"eps_c = {s['eps_c']:.3f}; mittleres R_Q je eps: "
                      + ", ".join(f"{v:.3f}" for v in s["mittel_R_Q"]))
    zz.append(f"  L3 fuer R_Q: {l3_text(res['L3'], 'R_Q')}; fuer eps_c: {l3_text(res['L3_schwelle'], 'eps_c')}")
    return zz


# ---------------------------------------------------------------- pumpe (Bio 45)

def pumpe_hmin():
    """Schwelle aus der Ladungsbilanz dQ/dt = -gamma Q - 2 h F sin(theta), F = Int f dx: h_min = gamma Q* / (2 F)."""
    xs = torch.arange(-15000, 15001, dtype=F64) * 0.01
    f_int = float(profil_anker_x(PU_W2D, xs).sum()) * 0.01
    q_stern = anker_q_e(PU_W2D)[0]
    return PU_GAMMA * q_stern / (2.0 * f_int), f_int, q_stern


def pumpe_laeufe():
    laeufe = [{"art": "ball", "w2": 0.70, "h_rel": h, "gamma": PU_GAMMA} for h in PU_H_REL]
    laeufe += [{"art": "ball", "w2": w2, "h_rel": 2.0, "gamma": PU_GAMMA} for w2 in PU_SAAT_W2]
    laeufe += [{"art": "ball", "w2": w2, "h_rel": 0.5, "gamma": PU_GAMMA} for w2 in PU_UNTER_W2]
    laeufe += [{"art": "treiber", "w2": None, "h_rel": h, "gamma": PU_GAMMA} for h in PU_TREIBER_H]
    laeufe += [{"art": "ball", "w2": 0.70, "h_rel": 2.0, "gamma": 0.0},
               {"art": "treiber", "w2": None, "h_rel": 2.0, "gamma": 0.0},
               {"art": "ball", "w2": 0.70, "h_rel": 0.0, "gamma": 0.0}]
    return laeufe


def pumpe(faktor):
    laeufe = pumpe_laeufe()
    hmin, f_int, q_stern = pumpe_hmin()
    om_d = math.sqrt(PU_W2D)

    def bauen(x, dx):
        gd = rand_fenster(x, PU_XIN, PU_XAUS)
        felder, hs, gs = [], [], []
        for r in laeufe:
            h = r["h_rel"] * hmin
            teile = [ball(x, r["w2"])] if r["w2"] is not None else []
            if h > 0.0:
                c = h / complex(1.0 - PU_W2D, -r["gamma"] * om_d)      # stationaerer Hintergrund h / (1 - Om^2 - i g Om)
                p_bg = c * gd
                teile.append((p_bg, (-1j * om_d) * p_bg))
            if not teile:
                teile.append(null(x))
            felder.append(summe(teile))
            hs.append(h)
            gs.append(r["gamma"])
        psi, vel = stapel(felder)
        ht = torch.tensor(hs, dtype=F64, device=DEV)
        gam = torch.tensor(gs, dtype=F64, device=DEV)

        def antrieb(t):
            return (ht * complex(math.cos(om_d * t), -math.sin(om_d * t))).unsqueeze(1) * gd.unsqueeze(0)

        maske = (x.abs() < W_FENSTER).to(F64)

        def messen(psi, vel, t):
            s = dichte(psi)
            rho = ladung(psi, vel)
            e = energie_dichte(psi, vel, dx)
            i, p = max_im_fenster(psi, s, maske)
            return torch.stack([(rho * maske).sum(1) * dx, (e * maske).sum(1) * dx, -torch.angle(p[:, 0]),
                                s.gather(1, i)[:, 0], x[i[:, 0]], rho.sum(1) * dx], dim=1)
        return {"psi": psi, "vel": vel, "messen": messen, "gamma": gam, "antrieb": antrieb}

    stufen = stufen_rechnen("pumpe", bauen, PU_T * faktor, PU_MESS)
    erg = {s: auswertung_pumpe(laeufe, st["t"], st["daten"], hmin, q_stern) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "Q_ende_rel": l3(zg["Q_ende_rel"], zf["Q_ende_rel"], 0.0)}
                for zg, zf in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"])]
    return {"laeufe": laeufe, "h_min": hmin, "F_int": f_int, "Q_stern": q_stern, "ergebnis": erg, "L3": l3_liste,
            "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def auswertung_pumpe(laeufe, t, d, hmin, q_stern):
    qw, ew, th, sm, xm, qb = d.unbind(dim=2)
    T = float(t[-1])
    om_d = math.sqrt(PU_W2D)
    i_tr = {(r["h_rel"], r["gamma"]): b for b, r in enumerate(laeufe) if r["art"] == "treiber"}
    zeilen, treiber = [], []
    for b, r in enumerate(laeufe):
        h = r["h_rel"] * hmin
        if r["art"] == "treiber":
            s_bg = abs(h / complex(1.0 - PU_W2D, -r["gamma"] * om_d)) ** 2
            treiber.append({"h_rel": r["h_rel"], "gamma": r["gamma"], "S_max_ende": ende(sm[:, b]), "S_bg_soll": s_bg,
                            "struktur": bool(ende(sm[:, b]) > 10.0 * s_bg)})
            continue
        schl = (r["h_rel"], r["gamma"])
        qball = qw[:, b] - qw[:, i_tr[schl]] if (r["h_rel"] > 0.0 and schl in i_tr) else qw[:, b]
        q_end = ende(qball)
        om_end = om_fenster(t, th[:, b], 0.75 * T, T)
        sl = steigung(t, qball, 0.75 * T, T)
        stabil = bool(r["gamma"] > 0.0 and q_end >= 0.5 * q_stern and abs(om_end - om_d) <= 0.005
                      and abs(sl) <= 0.01 * PU_GAMMA * q_end)          # gamma = 0: konservative Referenz, nie "dissipativ"
        rate = steigung(t, torch.log(qball.clamp(min=1e-300)), 0.1 * T, 0.4 * T)
        zeilen.append({"name": f"w2={r['w2']} h/hmin={r['h_rel']} gamma={r['gamma']}", "w2": r["w2"],
                       "h_rel": r["h_rel"], "gamma": r["gamma"], "Q_start": float(qball[0]), "Q_ende": q_end,
                       "Q_ende_rel": q_end / q_stern, "omega_ende": om_end, "omega_d": om_d, "dQdt_ende": sl,
                       "stabil_dissipativ": stabil, "rate_ln_Q_frueh": rate, "x_ende": ende(xm[:, b])})
    return {"zeilen": zeilen, "treiber": treiber}


def bericht_pumpe(res):
    zz = [f"pumpe (Bio 45): Treiber h exp(-i Omega_d t), Omega_d^2 = {PU_W2D}, gamma = {PU_GAMMA}; h_min = gamma Q* / (2 F) "
          f"= {res['h_min']:.4e} (F = Int f dx = {res['F_int']:.4f}, Q* = {res['Q_stern']:.4f})",
          "  stabil_dissipativ: Q_Ende >= 0,5 Q*, |omega_Ende - Omega_d| <= 0,005, |dQ/dt| <= 0,01 gamma Q im letzten Viertel",
          "  Lauf | Q Start -> Ende (/Q*) | omega Ende (Omega_d) | dQ/dt Ende | stabil | Rate d ln Q/dt [0,1T, 0,4T] | x Ende"]
    for stufe in ("grob", "fein"):
        e = res["ergebnis"][stufe]
        zz.append(f"  [{stufe}]")
        for z in e["zeilen"]:
            zz.append(f"  {z['name']:34s} | {z['Q_start']:.4f} -> {z['Q_ende']:.4f} ({z['Q_ende_rel']:.4f}) | "
                      f"{z['omega_ende']:.5f} ({z['omega_d']:.5f}) | {z['dQdt_ende']:+.2e} | {str(z['stabil_dissipativ']):5s} | "
                      f"{z['rate_ln_Q_frueh']:+.5f} | {z['x_ende']:+.2f}")
        for tr in e["treiber"]:
            zz.append(f"  Treiber allein h/hmin = {tr['h_rel']}, gamma = {tr['gamma']}: S_max Ende {tr['S_max_ende']:.3e} "
                      f"(Soll Hintergrund {tr['S_bg_soll']:.3e}), Struktur {tr['struktur']}")
    zz.append(f"  L3 fuer Q_Ende/Q*: {l3_text(res['L3'], 'Q_ende_rel')} Laeufe bestanden")
    return zz


# ---------------------------------------------------------------- mi (Bio 22, Chemie 10)

def mi_g(k, s0):
    """Lineare Wachstumsrate der Modulation k um psi = sqrt(s0) exp(-i omega t):
    (k^2 + M^2 - Om^2)(k^2 - Om^2) = 4 omega^2 Om^2, M^2 = 2 U''(s0) s0; Rate = sqrt(-Om^2_minus)."""
    om2 = 1.0 - 2.0 * s0 + 1.5 * s0 * s0
    m2 = 2.0 * s0 * (3.0 * s0 - 2.0)
    a = 2.0 * k * k + m2 + 4.0 * om2
    b = k * k * (k * k + m2)
    x_minus = 0.5 * (a - torch.sqrt(a * a - 4.0 * b))
    return torch.sqrt((-x_minus).clamp(min=0.0))


def mi_theorie(s0):
    m2 = 2.0 * s0 * (3.0 * s0 - 2.0)
    if m2 >= 0.0:
        return {"instabil": False, "k_c": 0.0, "k_max": NAN, "g_max": 0.0, "lambda_max": NAN}
    kc = math.sqrt(-m2)
    k = torch.linspace(0.0, kc, 4001, dtype=F64)[1:-1]
    g = mi_g(k, s0)
    i = int(g.argmax())
    return {"instabil": True, "k_c": kc, "k_max": float(k[i]), "g_max": float(g[i]), "lambda_max": 2.0 * PI / float(k[i])}


def mi_laeufe():
    laeufe = [{"art": "rauschen", "S0": s0, "delta": M_DELTA, "saat": saat, "w": 0.0} for s0 in M_S0 for saat in M_SAAT]
    laeufe += [{"art": "rauschen", "S0": s0, "delta": dl, "saat": 21, "w": 0.0} for s0, dl in M_ZUSATZ]
    laeufe += [{"art": "loch", "S0": s0, "delta": M_DELTA, "saat": 21, "w": w} for s0, w in M_LOCH]
    return laeufe


def mi(faktor):
    laeufe = mi_laeufe()

    def bauen(x, dx):
        n = x.shape[0]
        basis = {saat: rausch_basis(x, saat, 0.5 * 2.0 * PI / M_L, M_KMAX, M_L)[0] for saat in M_SAAT}
        felder = []
        for r in laeufe:
            a = math.sqrt(r["S0"])
            om = math.sqrt(1.0 - 2.0 * r["S0"] + 1.5 * r["S0"] ** 2)
            p = a * (1.0 + r["delta"] * basis[r["saat"]])
            if r["art"] == "loch":
                p = p * (1.0 - torch.exp(-x ** 2 / (2.0 * r["w"] ** 2)))
            felder.append((p, (-1j * om) * p))
        psi, vel = stapel(felder, rand_null=False)
        s0t = torch.tensor([r["S0"] for r in laeufe], dtype=F64, device=DEV)
        schnapp = []
        zaehler = [0]

        def messen(psi, vel, t):
            s = dichte(psi)
            ds = s - s0t.unsqueeze(1)
            rms = ds.pow(2).mean(1).sqrt()
            rho = ladung(psi, vel)
            e = energie_dichte(psi, vel, dx, periodisch=True)
            f = torch.fft.rfft(ds, dim=1) / n
            pw = (f.real ** 2 + f.imag ** 2)[:, :M_JMAX + 1]
            if zaehler[0] % M_SNAP == 0:
                schnapp.append(s.to(torch.float32).cpu())
            zaehler[0] += 1
            return torch.cat([torch.stack([rms, s.max(1).values, s.min(1).values, rho.sum(1) * dx, e.sum(1) * dx],
                                          dim=1), pw], dim=1)
        return {"psi": psi, "vel": vel, "messen": messen, "extra": {"schnapp": schnapp, "x": x.cpu()}}

    stufen = stufen_rechnen("mi", bauen, M_T * faktor, M_MESS, periodisch=True)
    erg = {}
    for s, st in stufen.items():
        snaps = torch.stack(st["extra"]["schnapp"]) if st["extra"]["schnapp"] else None
        st["extra"]["schnapp"] = snaps
        erg[s] = auswertung_mi(laeufe, st["t"], st["daten"], snaps, st["extra"]["x"])
    l3_liste = []
    for zg, zf in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"]):
        l3_liste.append({"lauf": zg["name"], "k_dom": l3(zg["k_dom"], zf["k_dom"], 0.0),
                         "g_mess": l3(zg["g_mess"], zf["g_mess"], 0.0),
                         "t_klumpen": l3(zg["t_klumpen"], zf["t_klumpen"], 0.0)})
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "sek": {s: stufen[s]["sek"] for s in stufen}}, stufen


def klumpen_zahl(s, s0):
    """Lokale Maxima (periodisch) oberhalb der halben Hoehe zwischen Hintergrund und globalem Maximum."""
    smax = float(s.max())
    if smax - s0 < 0.2 * s0:
        return 0
    lok = (s > torch.roll(s, 1)) & (s >= torch.roll(s, -1)) & (s > s0 + 0.5 * (smax - s0))
    return int(lok.sum())


def auswertung_mi(laeufe, t, d, snaps, x):
    rms, smax, smin, qbox, ebox = d[:, :, 0], d[:, :, 1], d[:, :, 2], d[:, :, 3], d[:, :, 4]
    pw = d[:, :, 5:]
    dx = float(x[1] - x[0])
    zeilen = []
    for b, r in enumerate(laeufe):
        s0 = r["S0"]
        th = mi_theorie(s0)
        r0 = float(rms[0, b])
        i_lin = torch.nonzero(rms[:, b] >= 1e-2 * s0).squeeze(1)
        i_1 = torch.nonzero(rms[:, b] >= min(30.0 * r0, 1e-3 * s0)).squeeze(1)
        t_lin, g_mess, k_dom, abw_g = NAN, NAN, NAN, NAN
        if i_lin.numel() > 0:
            il = int(i_lin[0])
            t_lin = float(t[il])
            p = pw[il, b]
            j = int(p[1:].argmax()) + 1
            delta = 0.0
            if 1 < j < M_JMAX:
                a_, b_, c_ = float(p[j - 1]), float(p[j]), float(p[j + 1])
                nenner = a_ - 2.0 * b_ + c_
                delta = 0.5 * (a_ - c_) / nenner if nenner != 0.0 else 0.0
            k_dom = (j + delta) * 2.0 * PI / M_L
            if i_1.numel() > 0 and float(t[il] - t[int(i_1[0])]) >= 5.0:
                i1 = int(i_1[0])
                dauer = float(t[il] - t[i1])
                g_mess = math.log(float(rms[il, b]) / float(rms[i1, b])) / dauer
                if th["instabil"]:
                    kj = torch.arange(1, M_JMAX + 1, dtype=F64) * (2.0 * PI / M_L)
                    gj_soll = mi_g(kj, s0)
                    p1, p2 = pw[i1, b, 1:], pw[il, b, 1:]
                    gut = (gj_soll >= 0.5 * th["g_max"]) & (p1 > 0.0) & (p2 > 0.0)
                    if bool(gut.any()):
                        gj = 0.5 * torch.log(p2[gut] / p1[gut]) / dauer
                        abw_g = float((gj - gj_soll[gut]).abs().max())
        kontrast = (smax[:, b] - smin[:, b]) / s0
        i_k = torch.nonzero(kontrast >= 1.0).squeeze(1)
        t_kl = float(t[int(i_k[0])]) if (i_k.numel() > 0 and r["art"] != "loch") else NAN   # Delle: Kontrast ab t = 0
        n_kl_ende, leer = 0, []
        if snaps is not None:
            n_kl_ende = klumpen_zahl(snaps[-1, b].to(F64), s0)
            for m in (0, snaps.shape[0] // 2, snaps.shape[0] - 1):
                leer.append(float((snaps[m, b] < 0.5 * s0).sum()) * dx)
        zeilen.append({"name": f"{r['art']} S0={s0} delta={r['delta']} saat={r['saat']} w={r['w']}", "art": r["art"],
                       "S0": s0, "delta": r["delta"], "saat": r["saat"], "w": r["w"], "theorie": th,
                       "t_lin": t_lin, "k_dom": k_dom, "g_mess": g_mess, "max_abw_g_moden": abw_g,
                       "t_klumpen": t_kl, "verklumpt": bool(math.isfinite(t_kl)), "klumpen_ende": n_kl_ende,
                       "leerlaenge_0_mitte_ende": leer, "kontrast_ende": float(kontrast[-1]),
                       "Q_drift_rel": float((qbox[-1, b] - qbox[0, b]) / qbox[0, b]),
                       "E_drift_rel": float((ebox[-1, b] - ebox[0, b]) / ebox[0, b])})
    return {"zeilen": zeilen}


def bericht_mi(res):
    zz = [f"mi (Bio 22, Chemie 10): periodische Box L = {M_L}, S0 = |psi|^2 des Kondensats, instabil fuer S0 < 2/3; "
          "t_lin: rms(dS) >= 0,01 S0; verklumpt: (S_max - S_min)/S0 >= 1",
          "  Lauf | instabil | k_max Theorie (lambda) | k_dom | g_max Theorie | g gemessen | max |g_k - Theorie| | "
          "t_lin | t_klumpen | Klumpen Ende | Leerlaenge 0/Mitte/Ende | Q-Drift | E-Drift"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for z in res["ergebnis"][stufe]["zeilen"]:
            th = z["theorie"]
            zz.append(f"  {z['name']:42s} | {str(th['instabil']):5s} | {th['k_max']:.4f} ({th['lambda_max']:.2f}) | "
                      f"{z['k_dom']:.4f} | {th['g_max']:.4f} | {z['g_mess']:.4f} | {z['max_abw_g_moden']:.4f} | "
                      f"{z['t_lin']:.1f} | {z['t_klumpen']:.1f} | {z['klumpen_ende']} | "
                      + "/".join(f"{v:.1f}" for v in z["leerlaenge_0_mitte_ende"])
                      + f" | {z['Q_drift_rel']:+.1e} | {z['E_drift_rel']:+.1e}")
    n = sum(1 for e in res["L3"] for k in ("k_dom", "g_mess", "t_klumpen") if e[k]["bestanden"])
    zz.append(f"  L3 (k_dom, g, t_klumpen; nicht definierte zaehlen als nicht bestanden): {n} von {3 * len(res['L3'])}")
    return zz


# ---------------------------------------------------------------- Hauptprogramm

BEFEHLE = {"fuettern": (fuettern, bericht_fuettern), "photo": (photo, bericht_photo),
           "winterschlaf": (winterschlaf, bericht_winterschlaf), "rauschen": (rauschen, bericht_rauschen),
           "pumpe": (pumpe, bericht_pumpe), "mi": (mi, bericht_mi)}


def schreiben(out, name, ausgabe, text, reihen):
    """Stand sichern: Bericht, JSON und Zeitreihen des Befehls."""
    with open(os.path.join(out, f"{name}_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    with open(os.path.join(out, f"{name}_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)
    if reihen is not None:
        torch.save(reihen, os.path.join(out, f"{name}_zeitreihen.pt"))


def main():
    global DEV
    ap = argparse.ArgumentParser(description="Runde 5, R5-B: 1D-Einzelball-Tests (Bio 3, 36, 38, 20/37, 45, 22/Chemie 10)")
    ap.add_argument("befehl", choices=list(BEFEHLE) + ["rauch"])
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ausgabe"))
    ap.add_argument("--faktor", type=float, default=1.0, help="Laufzeiten mal faktor (rauch: fest 0,05)")
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber kein CUDA-Geraet sichtbar: Abbruch.")
        DEV = torch.device("cuda")
        gesamt = torch.cuda.get_device_properties(0).total_memory
        torch.cuda.set_per_process_memory_fraction(min(1.0, SPEICHER_GB * 2 ** 30 / gesamt))
        name_geraet = torch.cuda.get_device_name(0)
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(1)
        name_geraet = "CPU, 1 Thread"
    os.makedirs(args.out, exist_ok=True)
    liste = list(BEFEHLE) if args.befehl == "rauch" else [args.befehl]
    faktor = 0.05 if args.befehl == "rauch" else args.faktor
    kopf = (f"Runde 5 R5-B {args.befehl} Start {jetzt()} auf {name_geraet}, torch {torch.__version__}, "
            f"Faktor {faktor}")
    print(kopf, flush=True)
    t_start = uhr()
    zeiten, fehler = [], []
    for name in liste:
        funk, ber = BEFEHLE[name]
        ausgabe = {"start": jetzt(), "geraet": name_geraet, "torch": torch.__version__, "befehl": name,
                   "faktor": faktor}
        text = [kopf, ""]
        reihen = None
        t0 = uhr()
        try:
            res, stufen = funk(faktor)
            ausgabe["ergebnis"] = res
            reihen = {"laeufe": res["laeufe"],
                      "stufen": {s: {"t": st["t"], "daten": st["daten"], "extra": st["extra"]}
                                 for s, st in stufen.items()}}
            text += ber(res)
            rechnen = sum(res["sek"].values())
        except Exception:
            ausgabe["fehler"] = traceback.format_exc()
            text += [f"{name} FEHLER:", ausgabe["fehler"]]
            print(ausgabe["fehler"], flush=True)
            fehler.append(name)
            rechnen = NAN
            if reihen is None and name in ROH:
                reihen = {"roh_ohne_auswertung": True,
                          "stufen": {s: {"t": st["t"], "daten": st["daten"], "extra": st["extra"]}
                                     for s, st in ROH[name].items()}}
        sek = uhr() - t0
        hoch = (sek - rechnen) + rechnen / faktor if math.isfinite(rechnen) else NAN
        zeiten.append({"befehl": name, "sek": sek, "rechnen_sek": rechnen, "hochrechnung_volle_laenge_sek": hoch})
        ausgabe["dauer_s"] = sek
        ausgabe["ende"] = jetzt()
        if DEV.type == "cuda":
            ausgabe["torch_speicher_max_mb"] = torch.cuda.max_memory_allocated() / 2 ** 20
        text.append(f"{name}: Dauer {sek:.1f} s (davon Zeitentwicklung {rechnen:.1f} s); Hochrechnung fuer Faktor 1: "
                    f"{hoch:.0f} s")
        schreiben(args.out, name, ausgabe, text, reihen)
        print("\n".join(text), flush=True)
    zeilen = [kopf, "Befehl | Dauer s | Zeitentwicklung s | Hochrechnung Faktor 1 (s, min)"]
    for z in zeiten:
        zeilen.append(f"{z['befehl']:13s} | {z['sek']:.1f} | {z['rechnen_sek']:.1f} | "
                      f"{z['hochrechnung_volle_laenge_sek']:.0f} ({z['hochrechnung_volle_laenge_sek'] / 60.0:.1f})")
    zeilen.append(f"Ende {jetzt()}, gesamt {uhr() - t_start:.1f} s, Fehler in: {fehler if fehler else 'keine'}")
    if DEV.type == "cuda":
        zeilen.append(f"Torch-Speicher max {torch.cuda.max_memory_allocated() / 2 ** 20:.0f} MB")
    with open(os.path.join(args.out, f"{args.befehl}_zeiten.txt"), "w") as fh:
        fh.write("\n".join(zeilen) + "\n")
    print("\n".join(zeilen), flush=True)
    if fehler:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
