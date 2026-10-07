#!/usr/bin/env python3
"""R4-W, Runde 4 (runden-v3): fuenf 1D-Wellentests mit Q-Baellen. Explorativ, ungetestet abgegeben.

Karten Wellen 1, 2, 3, 12, 13. Plan, Aufruf, Vorhersagen und Latten stehen in PLAN.md daneben.
Ausgangscode: RUNDE-01/qg1/qg1.py (Schiessen, Anker, Gitter, Zeitschritt, Velocity-Verlet unveraendert uebernommen,
hier ohne Brechungsfeld: A = B = C = 1). Nur CUDA, float64 bzw. complex128; ohne CUDA bricht das Programm ab.

Modell: L = |psi_t|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2.
Bewegungsgleichung psi_tt = psi_xx - U'(S) psi, U'(S) = 1 - 2S + 1,5 S^2.
Ladungsdichte rho = 2 Im(psi conj(psi_t)), Energiedichte |psi_t|^2 + |psi_x|^2 + U(S).

Unterbefehle (je einer pro Test, jeder rechnet grob dx = 0,1, dt = 0,05 und fein dx = 0,05, dt = 0,025):
  profil    Schiessen wie QG-1, Profil in profil_cache.pt ablegen (die Tests laden es, sonst schiessen sie selbst)
  russell   Wellen 1:  Stoss zweier gleicher Baelle (omega^2 = 0,7) bei v = 0,1, 0,3, 0,5
  monster   Wellen 2:  instabiler Hintergrund (S0 = 0,1 und 0,3) mit Rauschen 1e-3 gegen stabilen (S0 = 0,8)
  stokes    Wellen 3:  Ball in freier laufender Welle um das Vakuum, Amplituden 0,01, 0,02, 0,04
  surfen    Wellen 12: grosses laufendes Wellenpaket um das Vakuum trifft einen ruhenden Ball
  brandung  Wellen 13: Ball laeuft auf den stabilen dichten See S = 1 (natuerliche Wand als Rampe)
  rauch     alle fuenf mit kurzer Laufzeit (nur Durchlaufprobe, Zahlen ohne Bedeutung)
Aufruf:  python wellen.py <unterbefehl> [--T ZEIT] [--out ORDNER] [--rauch]
"""
import argparse
import datetime
import json
import math
import os
import time

import torch

DEV = torch.device("cuda")
F64 = torch.float64
HIER = os.path.dirname(os.path.abspath(__file__))

# ---- Feste Parameter (vor dem Lauf in PLAN.md festgehalten) ----
OMEGA2 = [0.55, 0.70, 0.90]   # wie QG-1; gerechnet wird mit 0,70
OM_BALL = 0.70
H_ODE = 0.01                  # Schiessen wie QG-1
X_ODE = 80.0
N_KAND, RUNDEN = 4096, 4
SCHWANZ = 1e-3
TOL_PROFIL = 1e-6             # K0: max |f_Schuss - f_Anker| auf dem Gitter
DX, DT = 0.1, 0.05            # grob; fein halbiert beide
L_BOX = 150.0                 # Dirichlet-Box [-L, L] (Russell, Surfen, Brandung)
X_SPONGE = 110.0              # Daempfungsschicht fuer |x| > X_SPONGE
SIGMA0 = 1.0
R_WIN = 15.0                  # Energie-/Ladungsfenster um einen Ball
T_MESS = 1.0                  # Messabstand
T_RAUCH = 12.0                # Laufzeit im Rauchtest


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    torch.cuda.synchronize()
    return time.perf_counter()


# ---------------------------------------------------------------- Profil durch Schiessen (aus QG-1 unveraendert)

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
    """Zentralwert f(0) je omega durch Einschachteln, alle omega und Kandidaten gleichzeitig (wie QG-1)."""
    n_om = a0.shape[0]
    lo = torch.full((n_om, 1), 1e-3, dtype=F64, device=DEV)
    hi = torch.ones((n_om, 1), dtype=F64, device=DEV)
    stufen = torch.linspace(0.0, 1.0, N_KAND, dtype=F64, device=DEV)
    n_schritte = int(round(X_ODE / H_ODE))
    for _ in range(RUNDEN):
        f0 = lo + (hi - lo) * stufen
        f, fp = f0.clone(), torch.zeros_like(f0)
        zustand = torch.zeros_like(f0)
        for _ in range(n_schritte):
            f, fp = rk4(f, fp, a0, H_ODE)
            ueber = (zustand == 0) & (f < 0)
            unter = (zustand == 0) & (f >= 0) & (fp > 0)
            zustand = zustand + ueber.to(F64) - unter.to(F64)
            lebt = (zustand == 0).to(F64)
            f = f * lebt
            fp = fp * lebt
        lo = torch.where(zustand < 0, f0, torch.zeros_like(f0)).max(dim=1, keepdim=True).values
        hi = torch.where(zustand > 0, f0, torch.full_like(f0, 2.0)).min(dim=1, keepdim=True).values
    return 0.5 * (lo + hi), hi - lo


def profil_bahn(f0, a0):
    """Schiessbahn f(j h) ab f(0) = f0, bis f unter SCHWANZ * f0 faellt; danach eingefroren (wie QG-1)."""
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
    """Symmetrisches Gitter x_i = (i - i0) dx auf [-L, L] (wie QG-1); x = 0 liegt genau auf einem Punkt."""
    i0 = int(round(L_BOX / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx


def gitter_periodisch(dx, laenge):
    """Periodisches Gitter x_i = (i - n/2) dx, n = laenge/dx; x = 0 liegt auf einem Punkt, Spiegelung i -> n - i."""
    n = int(round(laenge / dx))
    return (torch.arange(n, dtype=F64, device=DEV) - n // 2) * dx


def profil_anker(w2, x):
    """Analytischer 1D-Anker (nur Kontrolle): f^2 = 2 a0 / (1 + b0 cosh(2 sqrt(a0) x))."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    return torch.sqrt(2.0 * a0 / (1.0 + b0 * torch.cosh(2.0 * math.sqrt(a0) * x)))


def anker_wgv(w2):
    """Geschlossene 1D-Werte: I = sqrt(2) arcosh(1/b0), W = omega^2 I, G = sqrt(a0)/2 - b0^2 I/4, V = W + G."""
    a0, b0 = 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)
    integral = math.sqrt(2.0) * math.acosh(1.0 / b0)
    w = w2 * integral
    g = math.sqrt(a0) / 2.0 - b0 * b0 * integral / 4.0
    return w, g, w + g


# ---------------------------------------------------------------- neu: Profil-Zwischenspeicher und Auswertung

def profil_holen():
    """Schiessen wie QG-1, einmal; Ergebnis in profil_cache.pt neben dem Skript (spart je Test etwa 1,5 bis 2,5 min)."""
    datei = os.path.join(HIER, "profil_cache.pt")
    a0 = (1.0 - torch.tensor(OMEGA2, dtype=F64, device=DEV)).unsqueeze(1)
    if os.path.exists(datei):
        d = torch.load(datei, map_location=DEV)
        if list(d["omega2"]) == OMEGA2 and float(d["h_ode"]) == H_ODE:
            return {"f0": d["f0"], "bahn": d["bahn"], "j_cut": d["j_cut"], "a0": a0, "klammer": d["klammer"],
                    "herkunft": "profil_cache.pt"}
    f0, klammer = schiessen(a0)
    bahn, j_cut = profil_bahn(f0, a0)
    torch.save({"omega2": OMEGA2, "h_ode": H_ODE, "f0": f0, "bahn": bahn, "j_cut": j_cut, "klammer": klammer}, datei)
    return {"f0": f0, "bahn": bahn, "j_cut": j_cut, "a0": a0, "klammer": klammer, "herkunft": "geschossen"}


def profil_auswerten(prof, iw, y):
    """f(y) und f'(y) des geschossenen Profils (omega-Index iw) an beliebigen Orten y.

    Kubische Hermite-Interpolation der Schiessbahn (Knotenabstand H_ODE); f' aus dem ersten Integral
    f'^2 = f^2 (a0 - f^2 + f^4/2). Jenseits der Schwanzschwelle exponentieller Schwanz wie in QG-1."""
    b = prof["bahn"][iw]
    jc = int(prof["j_cut"][iw, 0].item())
    a = float(prof["a0"][iw, 0].item())

    def steigung(f):                                   # df/dr <= 0 fuer r = |y|
        return -f * torch.sqrt((a - f * f + 0.5 * f ** 4).clamp(min=0.0))

    r = y.abs()
    s = r / H_ODE
    j = s.floor().clamp(max=jc - 1).long()
    t = s - j.to(F64)
    fa, fb = b[j], b[j + 1]
    da, db = steigung(fa), steigung(fb)
    t2, t3 = t * t, t * t * t
    innen = ((2.0 * t3 - 3.0 * t2 + 1.0) * fa + (t3 - 2.0 * t2 + t) * H_ODE * da
             + (-2.0 * t3 + 3.0 * t2) * fb + (t3 - t2) * H_ODE * db)
    aussen = b[jc] * torch.exp(-math.sqrt(a) * (r - jc * H_ODE))
    f = torch.where(s < jc, innen, aussen)
    return f, torch.sign(y) * steigung(f)


def ball(x, prof, iw, x0, v, phase):
    """Geboosteter Q-Ball bei x0 mit Geschwindigkeit v und Phase:
    psi = f(g (x - x0)) exp(i (w g v (x - x0) + phase)),  psi_t = (-g v f' - i w g f) exp(...),  g = 1/sqrt(1 - v^2)."""
    w = math.sqrt(OMEGA2[iw])
    g = 1.0 / math.sqrt(1.0 - v * v)
    f, fs = profil_auswerten(prof, iw, g * (x - x0))
    ph = torch.exp(1j * (w * g * v * (x - x0) + phase))
    return f * ph, (-g * v * fs - 1j * w * g * f) * ph


def profil_kontrolle(prof):
    """K0 wie QG-1: interpoliertes Schussprofil gegen den Anker auf beiden Gittern (max |f - f_Anker|)."""
    abw = 0.0
    for dx in (DX, DX / 2.0):
        x = gitter(dx)
        for iw, w2 in enumerate(OMEGA2):
            f, _ = profil_auswerten(prof, iw, x)
            abw = max(abw, (f - profil_anker(w2, x)).abs().max().item())
    return {"max_abw_f": abw, "bestanden": abw <= TOL_PROFIL, "herkunft": prof["herkunft"],
            "f0_quadrat_schuss": [prof["f0"][i, 0].item() ** 2 for i in range(len(OMEGA2))],
            "f0_quadrat_anker": [1.0 - math.sqrt(2.0 * w2 - 1.0) for w2 in OMEGA2]}


# ---------------------------------------------------------------- Zeitentwicklung (Velocity-Verlet wie QG-1)

def schwamm(x):
    """Quadratische Daempfungsschicht fuer |x| > X_SPONGE (wie QG-1)."""
    return SIGMA0 * ((x.abs() - X_SPONGE).clamp(min=0.0) / (L_BOX - X_SPONGE)) ** 2


def dichten(psi, vel, dx, periodisch):
    """S, Ladungsdichte rho und Energiedichte e (Gradient als Vorwaertsdifferenz wie QG-1)."""
    s = psi.real ** 2 + psi.imag ** 2
    rho = 2.0 * (psi * vel.conj()).imag
    e = vel.abs() ** 2 + s - s * s + 0.5 * s ** 3
    if periodisch:
        e = e + ((torch.roll(psi, -1, 1) - psi).abs() / dx) ** 2
    else:
        e[:, :-1] += ((psi[:, 1:] - psi[:, :-1]).abs() / dx) ** 2
    return s, rho, e


def teilen(a, b):
    """a / b, aber 0 wo |b| <= 1e-12 (leere Bereiche ohne Ladung)."""
    ok = b.abs() > 1e-12
    return torch.where(ok, a / torch.where(ok, b, torch.ones_like(b)), torch.zeros_like(a))


def entwickeln(psi, vel, dx, dt, t_end, periodisch, sigma, messen, t_abstand):
    """Velocity-Verlet wie QG-1 (A = B = C = 1) fuer einen Stapel (B Laeufe x N Punkte).

    periodisch: Laplace mit torch.roll, sonst Dirichlet-Rand mit Flussform wie QG-1. sigma: Daempfung (N,) oder None.
    messen(psi, vel, t) wird bei t = 0 und alle t_abstand aufgerufen. Rueckgabe: psi, vel am Ende, Messliste."""

    def kraft(psi):
        if periodisch:
            lap = (torch.roll(psi, -1, 1) - 2.0 * psi + torch.roll(psi, 1, 1)) / (dx * dx)
        else:
            fluss = (psi[:, 1:] - psi[:, :-1]) / dx
            lap = torch.zeros_like(psi)
            lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = psi.real ** 2 + psi.imag ** 2
        return lap - (1.0 - 2.0 * s + 1.5 * s * s) * psi

    n_schritte = int(round(t_end / dt))
    alle = int(round(t_abstand / dt))
    reihe = [messen(psi, vel, 0.0)]
    kr = kraft(psi)
    for n in range(1, n_schritte + 1):
        if sigma is None:
            vel = vel + (0.5 * dt) * kr
            psi = psi + dt * vel
            kr = kraft(psi)
            vel = vel + (0.5 * dt) * kr
        else:
            vel = vel + (0.5 * dt) * (kr - sigma * vel)
            psi = psi + dt * vel
            kr = kraft(psi)
            vel = vel + (0.5 * dt) * (kr - sigma * vel)
        if n % alle == 0:
            reihe.append(messen(psi, vel, n * dt))
    return psi, vel, reihe


def endlich(daten):
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    return daten


def parabel(t, y, t0, t1):
    """Fit y = k0 + k1 tau + k2 tau^2 auf [t0, t1], tau = (t - Fensteranfang) / Spanne (wie QG-1). y: (M, B)."""
    wahl = (t >= t0 - 1e-9) & (t <= t1 + 1e-9)
    ts, ys = t[wahl], y[wahl]
    spanne = ts[-1] - ts[0]
    tau = (ts - ts[0]) / spanne
    a_mat = torch.stack([torch.ones_like(tau), tau, tau * tau], dim=1)
    koef = torch.linalg.lstsq(a_mat, ys).solution
    return koef, ys - a_mat @ koef, spanne, ys


def gerade(t, y, t0, t1):
    """Steigung einer Ausgleichsgeraden y(t) auf [t0, t1]. y: (M, B). Rueckgabe (B,)."""
    wahl = (t >= t0 - 1e-9) & (t <= t1 + 1e-9)
    ts, ys = t[wahl], y[wahl]
    tm = ts - ts.mean()
    return (tm.unsqueeze(1) * (ys - ys.mean(0))).sum(0) / (tm * tm).sum()


# ==== TESTS ====

# ---------------------------------------------------------------- 1 Russell (Wellen 1)
RUS_V = [0.1, 0.3, 0.5]
RUS_D = 20.0                  # Start bei -D (und +D); Messzeit t_m = (D + RUS_NACH) / v, Baelle dann bei etwa +-30
RUS_NACH = 30.0
RUS_T = 500.0                 # = t_m fuer v = 0,1


def lauf_russell(prof, dx, dt, t_end):
    x = gitter(dx)
    iw = OMEGA2.index(OM_BALL)
    laeufe, psi, vel = [], [], []
    for v in RUS_V:
        for art, vz in (("gleichphasig", 1.0), ("gegenphasig", -1.0), ("einzeln", 0.0)):
            p, q = ball(x, prof, iw, -RUS_D, v, 0.0)
            if vz != 0.0:                          # Spiegelbild bei +D mit -v: psi_R(x) = vz psi_L(-x)
                p2, q2 = ball(x, prof, iw, RUS_D, -v, 0.0)
                p, q = p + vz * p2, q + vz * q2
            laeufe.append({"v": v, "art": art, "t_mess": min((RUS_D + RUS_NACH) / v, t_end)})
            psi.append(p)
            vel.append(q)
    psi, vel = torch.stack(psi), torch.stack(vel)
    psi[:, 0] = 0.0
    psi[:, -1] = 0.0
    vel[:, 0] = 0.0
    vel[:, -1] = 0.0
    paar = torch.tensor([r["art"] != "einzeln" for r in laeufe], device=DEV).unsqueeze(1)
    rechts, links = (x > 0).to(F64), (x < 0).to(F64)

    def messen(psi, vel, t):
        s, rho, e = dichten(psi, vel, dx, False)
        x_r = teilen((x * rho * rechts).sum(1), (rho * rechts).sum(1))
        x_l = teilen((x * rho * links).sum(1), (rho * links).sum(1))
        x_g = teilen((x * rho).sum(1), rho.sum(1))
        f_paar = ((x - x_r.unsqueeze(1)).abs() < R_WIN) | ((x - x_l.unsqueeze(1)).abs() < R_WIN)
        f_einz = (x - x_g.unsqueeze(1)).abs() < R_WIN
        fenster = torch.where(paar, f_paar, f_einz).to(F64)
        return torch.stack([x_r, x_l, x_g, (e * fenster).sum(1) * dx, (rho * fenster).sum(1) * dx,
                            e.sum(1) * dx, rho.sum(1) * dx, s.max(dim=1).values], dim=1)

    _, _, reihe = entwickeln(psi, vel, dx, dt, t_end, False, schwamm(x), messen, T_MESS)
    d = endlich(torch.stack(reihe))              # (M, B, 8)
    zeilen = []
    for b, r in enumerate(laeufe):
        m = min(int(round(r["t_mess"] / T_MESS)), d.shape[0] - 1)
        m0 = max(m - 20, 0)
        spalte = 0 if r["art"] != "einzeln" else 2
        e0, q0 = d[0, b, 5], d[0, b, 6]
        zeilen.append(dict(r, **{
            "E0": e0.item(), "Q0": q0.item(),
            "abgestrahlt_E": (1.0 - d[m, b, 3] / e0).item(),
            "abgestrahlt_Q": (1.0 - d[m, b, 4] / q0).item(),
            "E_box_rest": (d[m, b, 5] / e0).item(),
            "X_mess": d[m, b, spalte].item(),
            "v_nach": ((d[m, b, spalte] - d[m0, b, spalte]) / max((m - m0) * T_MESS, 1e-9)).item(),
            "S_max_mess_zu_start": (d[m, b, 7] / d[0, b, 7]).item(),
            "S_max_gesamt_zu_start": (d[:m + 1, b, 7].max() / d[0, b, 7]).item(),
        }))
    return zeilen, {"spalten": ["X_rechts", "X_links", "X_global", "E_fenster", "Q_fenster", "E_box", "Q_box",
                                "S_max"], "laeufe": laeufe, "daten": d.cpu()}


def bewerten_russell(grob, fein):
    stoss = [z for z in fein if z["art"] != "einzeln"]
    einzel = [z for z in fein if z["art"] == "einzeln"]
    g_idx = {(z["v"], z["art"]): z for z in grob}
    kontrolle = max(abs(z["abgestrahlt_E"]) for z in einzel)
    effekt_min = min(abs(z["abgestrahlt_E"]) for z in stoss)
    aenderung = max(abs(z["abgestrahlt_E"] - g_idx[(z["v"], z["art"])]["abgestrahlt_E"]) for z in stoss)
    k = {
        "L2_gegenprobe_einzelball": {"max_abgestrahlt_E_einzeln": kontrolle, "min_abgestrahlt_E_stoss": effekt_min,
                                     "bestanden": effekt_min >= 5.0 * kontrolle},
        "L3_aufloesung": {"min_effekt": effekt_min, "max_aenderung_fein_grob": aenderung,
                          "bestanden": effekt_min >= 5.0 * aenderung},
    }
    text = ["Stoss: v | Art | abgestrahlt E (grob, fein) | abgestrahlt Q (fein) | X bei t_m | v danach | "
            "S_max(t_m)/S_max(0) | Ausgang"]
    for z in fein:
        gz = g_idx[(z["v"], z["art"])]
        if z["art"] == "einzeln":
            ausgang = "Kontrolle"
        elif abs(z["X_mess"]) < 5.0:
            ausgang = "verschmolzen (ein Klumpen bei x = 0)"
        else:
            ausgang = "getrennt"
        text.append(f"  {z['v']:.1f} | {z['art']:12s} | {gz['abgestrahlt_E']:.3e}, {z['abgestrahlt_E']:.3e} | "
                    f"{z['abgestrahlt_Q']:.3e} | {z['X_mess']:.2f} | {z['v_nach']:.4f} | "
                    f"{z['S_max_mess_zu_start']:.4f} | {ausgang}")
    return k, text


# ---------------------------------------------------------------- 2 Monsterwelle (Wellen 2)
MON_L = 800.0                 # periodische Box
MON_S0 = [0.1, 0.3, 0.8]      # 0,1 und 0,3 instabil (U'' < 0), 0,8 stabil (Gegenprobe)
MON_SEEDS = [1, 2, 3, 4]
MON_RAUSCH = 1e-3             # rms des komplexen Rauschens
MON_KMAX = 2.0                # Rauschen nur in Moden |k| <= 2 (dieselben Moden auf beiden Gittern)
MON_T = 300.0
MON_ALLE = 2.0                # Abstand der Schnappschuesse
MON_FENSTER = [(1.0 / 6.0, 0.5), (0.5, 1.0)]   # Anteile von T: [50, 150] und [150, 300]
MON_KAPPA_M = [2.0, 4.0, 6.0]                   # Schwellen s = kappa M
MON_KAPPA_SD = [2.0, 3.0, 4.0, 5.0]             # Schwellen s = M + kappa sqrt(V)


def rauschen(n_gitter, seed):
    """Komplexes Rauschen aus den Moden 0 < |k| <= MON_KMAX (k = 2 pi n / L), rms MON_RAUSCH."""
    n_c = int(MON_KMAX * MON_L / (2.0 * math.pi))
    gen = torch.Generator(device=DEV)
    gen.manual_seed(seed)
    c = torch.randn(2 * n_c + 1, 2, dtype=F64, device=DEV, generator=gen)
    c = torch.complex(c[:, 0], c[:, 1])
    nn = torch.arange(-n_c, n_c + 1, device=DEV)
    c = torch.where(nn == 0, torch.zeros_like(c), c)
    vorz = 1.0 - 2.0 * torch.remainder(nn, 2).to(F64)       # (-1)^n, weil x_0 = -L/2
    spek = torch.zeros(n_gitter, dtype=torch.complex128, device=DEV)
    spek[torch.remainder(nn, n_gitter)] = c * vorz
    eta = torch.fft.ifft(spek) * n_gitter
    return eta * (MON_RAUSCH / torch.sqrt((eta.abs() ** 2).mean()))


def rice_ueber(nu, sig2, schwellen):
    """P(S > s) fuer S = |m + z|^2, |m| = nu, z komplex gauss mit E|z|^2 = 2 sig2 (Rice; nu = 0: Rayleigh)."""
    sig = math.sqrt(sig2)
    a_max = max(nu + 40.0 * sig, math.sqrt(max(schwellen)) * 1.01)
    a = torch.linspace(0.0, a_max, 400001, dtype=F64, device=DEV)
    dichte = a / sig2 * torch.exp(-(a - nu) ** 2 / (2.0 * sig2)) * torch.special.i0e(a * nu / sig2)
    da = (a[1] - a[0]).item()
    teil = 0.5 * (dichte[1:] + dichte[:-1]) * da
    ueber = torch.flip(torch.cumsum(torch.flip(teil, [0]), 0), [0])      # ueber[i] = Integral a[i] .. a_max
    norm = ueber[0].item()
    aus = []
    for s in schwellen:
        i = int(math.sqrt(max(s, 0.0)) / da)
        aus.append(ueber[i].item() / norm if i < ueber.shape[0] else 0.0)
    return aus, norm


def statistik(probe, s0, fenster):
    """Ueberschreitungen von S in der Probe (Zeiten x Laeufe x Orte) gegen Rice mit gleichem Mittel und Varianz."""
    m_, v_ = probe.mean().item(), probe.var().item()
    n_ges = probe.numel()
    if v_ < m_ * m_:
        sig2 = 0.5 * (m_ - math.sqrt(m_ * m_ - v_))
        nu = math.sqrt(max(m_ - 2.0 * sig2, 0.0))
        art = "Rice (Mittel und Varianz von S angepasst)"
    else:
        sig2, nu = 0.5 * m_, 0.0
        art = "Rayleigh, exponentiell in S (V >= M^2: nur Mittel angepasst)"
    schwellen = [("4 S0", 4.0 * s0)] + [(f"{k:g} M", k * m_) for k in MON_KAPPA_M] \
        + [(f"M + {k:g} sd", m_ + k * math.sqrt(v_)) for k in MON_KAPPA_SD]
    p_rice, norm = rice_ueber(nu, sig2, [s for _, s in schwellen])
    eintraege = []
    for (name, s), pr in zip(schwellen, p_rice):
        n_obs = int((probe > s).sum().item())
        eintraege.append({"schwelle": name, "s": s, "n_beob": n_obs, "n_erw": pr * n_ges, "p_beob": n_obs / n_ges,
                          "p_rice": pr, "verhaeltnis": (n_obs + 0.5) / (pr * n_ges + 0.5)})
    ueber = probe > 4.0 * s0
    erst = int(ueber[:-1].sum().item())
    beide = int((ueber[1:] & ueber[:-1]).sum().item())
    return {"S0": s0, "fenster": fenster, "M": m_, "V": v_, "nu": nu, "sigma2": sig2, "referenz": art,
            "rice_norm": norm, "n": n_ges, "S_max_zu_S0": probe.max().item() / s0,
            "persistenz_4S0": beide / erst if erst > 0 else None, "schwellen": eintraege}


def lauf_monster(prof, dx, dt, t_end):
    x = gitter_periodisch(dx, MON_L)
    n = x.shape[0]
    laeufe, psi = [], []
    for i_s, s0 in enumerate(MON_S0):
        for seed in MON_SEEDS:
            mu2 = 1.0 - 2.0 * s0 + 1.5 * s0 * s0                  # mu^2 = U'(S0)
            laeufe.append({"S0": s0, "seed": 100 * i_s + seed, "mu": math.sqrt(mu2), "beta": 2.0 * s0 * (3.0 * s0 - 2.0)})
            psi.append(math.sqrt(s0) + rauschen(n, 100 * i_s + seed))
    psi = torch.stack(psi)
    mu = torch.tensor([r["mu"] for r in laeufe], dtype=F64, device=DEV).unsqueeze(1)
    vel = -1j * mu * psi                                          # ruhender Hintergrund im mitdrehenden System
    bilder = []

    def messen(psi, vel, t):
        s, rho, e = dichten(psi, vel, dx, True)
        bilder.append(s)
        return torch.stack([e.sum(1) * dx, rho.sum(1) * dx, s.max(dim=1).values, s.mean(1)], dim=1)

    _, _, reihe = entwickeln(psi, vel, dx, dt, t_end, True, None, messen, MON_ALLE)
    d = endlich(torch.stack(reihe))              # (M, B, 4)
    S = torch.stack(bilder)                      # (M, B, N)
    t = torch.arange(S.shape[0], dtype=F64, device=DEV) * MON_ALLE
    zeilen = []
    for s0 in MON_S0:
        wahl = [b for b, r in enumerate(laeufe) if r["S0"] == s0]
        for ta, tb in MON_FENSTER:
            zt = ((t >= ta * t_end - 1e-9) & (t <= tb * t_end + 1e-9)).nonzero().flatten()
            if zt.numel() < 2:
                continue
            eintrag = statistik(S[zt][:, wahl], s0, [ta * t_end, tb * t_end])
            eintrag["drift_E_rel"] = max(abs(d[-1, b, 0].item() / d[0, b, 0].item() - 1.0) for b in wahl)
            eintrag["drift_Q_rel"] = max(abs(d[-1, b, 1].item() / d[0, b, 1].item() - 1.0) for b in wahl)
            zeilen.append(eintrag)
    return zeilen, {"spalten": ["E_box", "Q_box", "S_max", "S_mittel"], "laeufe": laeufe, "daten": d.cpu(),
                    "t_schnappschuss": t.cpu()}


def bewerten_monster(grob, fein):
    def finde(zeilen, s0, name, fenster_nr):
        kand = [z for z in zeilen if z["S0"] == s0]
        if len(kand) <= fenster_nr:
            return None
        return next(e for e in kand[fenster_nr]["schwellen"] if e["schwelle"] == name)

    letzte = len(MON_FENSTER) - 1
    stab = [finde(fein, 0.8, n, letzte) for n in ("M + 2 sd", "M + 3 sd")]
    stab_ok = all(e is not None and 0.5 <= e["verhaeltnis"] <= 2.0 for e in stab)
    l3 = {}
    for s0 in (0.1, 0.3):
        eg, ef = finde(grob, s0, "4 S0", letzte), finde(fein, s0, "4 S0", letzte)
        if eg is None or ef is None:
            continue
        eff = abs(math.log(ef["verhaeltnis"]))
        aend = abs(math.log(ef["verhaeltnis"]) - math.log(eg["verhaeltnis"]))
        l3[f"S0={s0}"] = {"log_verhaeltnis_fein": math.log(ef["verhaeltnis"]), "aenderung_fein_grob": aend,
                          "bestanden": eff >= 5.0 * aend}
    k = {
        "L2_gegenprobe_stabil_S0_0.8": {"verhaeltnis_M+2sd_M+3sd": [e["verhaeltnis"] if e else None for e in stab],
                                        "bestanden": stab_ok},
        "L3_aufloesung_4S0_spaetfenster": l3,
    }
    text = ["S0 | Fenster | Referenz | M | V | S_max/S0 | Persistenz(4 S0) | Schwelle: beobachtet / Rice-erwartet "
            "(Verhaeltnis)"]
    for z in fein:
        teile = "; ".join(f"{e['schwelle']}: {e['n_beob']} / {e['n_erw']:.3g} ({e['verhaeltnis']:.3g})"
                          for e in z["schwellen"])
        pers = "-" if z["persistenz_4S0"] is None else f"{z['persistenz_4S0']:.3f}"
        text.append(f"  {z['S0']:.1f} | {z['fenster'][0]:.0f}-{z['fenster'][1]:.0f} | {z['referenz'][:5]} | "
                    f"{z['M']:.4f} | {z['V']:.3e} | {z['S_max_zu_S0']:.3f} | {pers} | {teile}")
    text.append("  Erhaltung (fein, max ueber Laeufe): " + ", ".join(
        f"S0 {z['S0']}: dE {z['drift_E_rel']:.1e}, dQ {z['drift_Q_rel']:.1e}" for z in fein[::len(MON_FENSTER)]))
    return k, text


# ---------------------------------------------------------------- 3 Stokes-Drift (Wellen 3)
ST_L = 256.0                  # periodische Box, genau 41 Wellenlaengen
ST_NW = 41
ST_K = 2.0 * math.pi * ST_NW / ST_L         # k = 1,0063
ST_W = math.sqrt(1.0 + ST_K ** 2)           # lineare Dispersion um das Vakuum: w^2 = 1 + k^2
ST_T = 400.0
ST_FENSTER = 40.0             # Messfenster um den Ladungsschwerpunkt (wie QG-1)
ST_LAEUFE = [("laufend", 0.01, 1.0), ("laufend", 0.02, 1.0), ("laufend", 0.04, 1.0), ("laufend", 0.04, -1.0),
             ("stehend_bauch", 0.04, 0.0), ("stehend_knoten", 0.04, 0.0), ("ohne", 0.0, 0.0)]


def lauf_stokes(prof, dx, dt, t_end):
    x = gitter_periodisch(dx, ST_L)
    iw = OMEGA2.index(OM_BALL)
    pb, vb = ball(x, prof, iw, 0.0, 0.0, 0.0)
    ph = ST_K * x
    psi, vel = [], []
    for art, a, r in ST_LAEUFE:
        if art == "laufend":                     # a cos(k x - r w t), reelle Welle ohne Ladung
            pw, vw = a * torch.cos(ph), r * a * ST_W * torch.sin(ph)
        elif art == "stehend_bauch":             # a cos(kx - wt) + a cos(kx + wt), Bauch am Ball
            pw, vw = 2.0 * a * torch.cos(ph), torch.zeros_like(x)
        elif art == "stehend_knoten":            # dasselbe um eine Viertelwelle verschoben, Knoten am Ball
            pw, vw = -2.0 * a * torch.sin(ph), torch.zeros_like(x)
        else:
            pw, vw = torch.zeros_like(x), torch.zeros_like(x)
        psi.append(pb + pw)
        vel.append(vb + vw)
    psi, vel = torch.stack(psi), torch.stack(vel)
    zustand = {"x_alt": torch.zeros(len(ST_LAEUFE), 1, dtype=F64, device=DEV)}

    def messen(psi, vel, t):
        s, rho, e = dichten(psi, vel, dx, True)
        fenster = ((x - zustand["x_alt"]).abs() < ST_FENSTER).to(F64)
        q_win = (rho * fenster).sum(1) * dx
        X = teilen((x * rho * fenster).sum(1) * dx, q_win)
        breite = torch.sqrt(teilen(((x - X.unsqueeze(1)) ** 2 * rho * fenster).sum(1) * dx, q_win).clamp(min=0.0))
        zustand["x_alt"] = X.unsqueeze(1)
        return torch.stack([X, q_win, (e * fenster).sum(1) * dx, breite, s.max(dim=1).values], dim=1)

    _, _, reihe = entwickeln(psi, vel, dx, dt, t_end, True, None, messen, T_MESS)
    d = endlich(torch.stack(reihe))              # (M, B, 5)
    t = torch.arange(d.shape[0], dtype=F64, device=DEV) * T_MESS
    koef, rest, spanne, _ = parabel(t, d[:, :, 0], t_end / 8.0, t_end)
    t_welle = 2.0 * math.pi / ST_W
    zeilen = []
    for b, (art, a, r) in enumerate(ST_LAEUFE):
        dX = (koef[1, b] + koef[2, b]).item()
        zeilen.append({"art": art, "a": a, "richtung": r, "dX_fit": dX,
                       "beschl": (2.0 * koef[2, b] / spanne ** 2).item(),
                       "v_anfang": (koef[1, b] / spanne).item(), "v_mittel": dX / spanne.item(),
                       "drift_je_periode": dX / (spanne.item() / t_welle),
                       "zittern": rest[:, b].pow(2).mean().sqrt().item(), "X_ende": d[-1, b, 0].item(),
                       "Q_fenster_aenderung_rel": (d[-1, b, 1] / d[0, b, 1] - 1.0).item(),
                       "breite_aenderung_rel": (d[-1, b, 3] / d[0, b, 3] - 1.0).item()})
    return zeilen, {"spalten": ["X", "Q_fenster", "E_fenster", "breite", "S_max"], "laeufe": ST_LAEUFE,
                    "daten": d.cpu(), "k": ST_K, "w": ST_W}


def verh(a, b):
    return a / b if b != 0.0 else float("inf")


def bewerten_stokes(grob, fein):
    def z(zeilen, art, a, r):
        return next(q for q in zeilen if q["art"] == art and q["a"] == a and q["richtung"] == r)

    d1, d2, d4 = (z(fein, "laufend", a, 1.0)["dX_fit"] for a in (0.01, 0.02, 0.04))
    links = z(fein, "laufend", 0.04, -1.0)["dX_fit"]
    bauch = z(fein, "stehend_bauch", 0.04, 0.0)["dX_fit"]
    knoten = z(fein, "stehend_knoten", 0.04, 0.0)["dX_fit"]
    ohne = z(fein, "ohne", 0.0, 0.0)["dX_fit"]
    d4g = z(grob, "laufend", 0.04, 1.0)["dX_fit"]
    r21, r42 = verh(d2, d1), verh(d4, d2)
    k = {
        "L1_skalierung_a2": {"dX_0.02_zu_0.01": r21, "dX_0.04_zu_0.02": r42, "soll": 4.0,
                             "bestanden": 3.2 <= r21 <= 4.8 and 3.2 <= r42 <= 4.8},
        "L2_gegenprobe": {"dX_stehend_bauch": bauch, "dX_ohne_welle": ohne, "dX_stehend_knoten_diagnose": knoten,
                          "bestanden": abs(d4) >= 5.0 * max(abs(bauch), abs(ohne))},
        "spiegelprobe_links_rechts": {"dX_rechts_plus_links": d4 + links,
                                      "bestanden": abs(d4 + links) <= 1e-6 * abs(d4) + 1e-12},
        "L3_aufloesung": {"dX_fein": d4, "dX_grob": d4g, "bestanden": abs(d4) >= 5.0 * abs(d4 - d4g)},
    }
    text = [f"Welle k = {ST_K:.5f}, w = {ST_W:.5f}, Periode {2.0 * math.pi / ST_W:.4f}; Fit auf [T/8, T]",
            "Lauf | a | Richtung | dX (grob, fein) | Drift je Periode | Beschl. | v_anfang | Zittern | dQ_Fenster"]
    for q in fein:
        g = z(grob, q["art"], q["a"], q["richtung"])
        text.append(f"  {q['art']:14s} | {q['a']:.2f} | {q['richtung']:+.0f} | {g['dX_fit']:.4e}, {q['dX_fit']:.4e} | "
                    f"{q['drift_je_periode']:.3e} | {q['beschl']:.3e} | {q['v_anfang']:.3e} | {q['zittern']:.1e} | "
                    f"{q['Q_fenster_aenderung_rel']:.1e}")
    return k, text


# ---------------------------------------------------------------- 4 Surfen (Wellen 12)
SU_K = 0.3                    # Traegerwellenzahl des Pakets
SU_W = math.sqrt(1.0 + SU_K ** 2)
SU_VG = SU_K / SU_W           # Gruppengeschwindigkeit 0,2873
SU_SIGMA = 15.0               # Huellkurve exp(-(x - x0)^2 / (2 sigma^2))
SU_X0 = -60.0                 # Paketmitte beim Start; Ball ruht bei x = 0
SU_A = [0.025, 0.05, 0.1, 0.2]
SU_T = 450.0


def paket(x, amp):
    """Reelles Wellenpaket nach rechts: A g(x - x0 - v_g t) cos(k (x - x0) - w t), bei t = 0 mit Zeitableitung."""
    g = torch.exp(-(x - SU_X0) ** 2 / (2.0 * SU_SIGMA ** 2))
    gs = -(x - SU_X0) / SU_SIGMA ** 2 * g
    ph = SU_K * (x - SU_X0)
    return amp * g * torch.cos(ph), amp * (SU_W * g * torch.sin(ph) - SU_VG * gs * torch.cos(ph))


def lauf_surfen(prof, dx, dt, t_end):
    x = gitter(dx)
    iw = OMEGA2.index(OM_BALL)
    pb, vb = ball(x, prof, iw, 0.0, 0.0, 0.0)
    laeufe, psi, vel = [], [], []
    for amp in SU_A:
        pw, vw = paket(x, amp)
        laeufe.append({"A": amp, "art": "ball_und_welle"})
        psi.append(pb + pw)
        vel.append(vb + vw)
        laeufe.append({"A": amp, "art": "nur_welle"})
        psi.append(pw.to(torch.complex128))
        vel.append(vw.to(torch.complex128))
    laeufe.append({"A": 0.0, "art": "nur_ball"})
    psi.append(pb)
    vel.append(vb)
    psi, vel = torch.stack(psi), torch.stack(vel)
    psi[:, 0] = 0.0
    psi[:, -1] = 0.0
    vel[:, 0] = 0.0
    vel[:, -1] = 0.0
    zustand = {"x_alt": torch.zeros(len(laeufe), 1, dtype=F64, device=DEV)}

    def messen(psi, vel, t):
        s, rho, e = dichten(psi, vel, dx, False)
        fenster = ((x - zustand["x_alt"]).abs() < 40.0).to(F64)
        q_win = (rho * fenster).sum(1) * dx
        X = teilen((x * rho * fenster).sum(1) * dx, q_win)
        breite = torch.sqrt(teilen(((x - X.unsqueeze(1)) ** 2 * rho * fenster).sum(1) * dx, q_win).clamp(min=0.0))
        zustand["x_alt"] = X.unsqueeze(1)
        return torch.stack([X, q_win, breite, s.max(dim=1).values, e.sum(1) * dx], dim=1)

    psi_e, vel_e, reihe = entwickeln(psi, vel, dx, dt, t_end, False, schwamm(x), messen, T_MESS)
    d = endlich(torch.stack(reihe))              # (M, B, 5)
    t = torch.arange(d.shape[0], dtype=F64, device=DEV) * T_MESS
    v_ende = gerade(t, d[:, :, 0], t_end - min(50.0, 0.5 * t_end), t_end)
    _, _, e_0 = dichten(psi, vel, dx, False)
    _, _, e_T = dichten(psi_e, vel_e, dx, False)
    f_0 = (x.abs() < R_WIN).to(F64)
    b_ball = len(laeufe) - 1
    e_ball0 = ((e_0[b_ball] * f_0).sum() * dx).item()
    zeilen = []
    for b, r in enumerate(laeufe):
        if r["art"] == "nur_welle":
            zeilen.append(dict(r, **{"S_max_welle_max": d[:, b, 3].max().item(),
                                     "E_welle_rest": (d[-1, b, 4] / d[0, b, 4]).item()}))
            continue
        f_T = ((x - d[-1, b, 0]).abs() < R_WIN).to(F64)
        e_T_ball = (e_T[b] * f_T).sum() * dx
        e_0_ball = (e_0[b] * f_0).sum() * dx
        if r["art"] == "ball_und_welle":         # Energie des Pakets allein im selben Fenster abziehen
            e_T_ball = e_T_ball - (e_T[b + 1] * f_T).sum() * dx
            e_0_ball = e_0_ball - (e_0[b + 1] * f_0).sum() * dx
        zeilen.append(dict(r, **{
            "v_ende": v_ende[b].item(), "mitgenommen": bool(v_ende[b].item() > 0.5 * SU_VG),
            "X_ende": d[-1, b, 0].item(), "X_min": d[:, b, 0].min().item(), "X_max": d[:, b, 0].max().item(),
            "E_ball_start": e_0_ball.item(), "E_gewinn_rel": (e_T_ball / e_0_ball - 1.0).item(),
            "E_ball_start_zu_nur_ball": (e_0_ball / e_ball0).item(),
            "Q_fenster_aenderung_rel": (d[-1, b, 1] / d[0, b, 1] - 1.0).item(),
            "S_max_min_rel": (d[:, b, 3].min() / d[0, b, 3]).item(),
            "S_max_max_rel": (d[:, b, 3].max() / d[0, b, 3]).item(),
            "breite_max_rel": (d[:, b, 2].max() / d[0, b, 2]).item()}))
    return zeilen, {"spalten": ["X", "Q_fenster", "breite", "S_max", "E_box"], "laeufe": laeufe, "daten": d.cpu(),
                    "v_g": SU_VG}


def bewerten_surfen(grob, fein):
    def z(zeilen, art, amp):
        return next(q for q in zeilen if q["art"] == art and q["A"] == amp)

    kontrolle = z(fein, "nur_ball", 0.0)
    v = {amp: z(fein, "ball_und_welle", amp)["v_ende"] for amp in SU_A}
    vg = {amp: z(grob, "ball_und_welle", amp)["v_ende"] for amp in SU_A}
    k = {
        "L2_gegenprobe_ohne_welle": {"v_ende_nur_ball": kontrolle["v_ende"],
                                     "E_gewinn_nur_ball": kontrolle["E_gewinn_rel"],
                                     "v_ende_A0.1": v[0.1],
                                     "bestanden": abs(v[0.1]) >= 5.0 * abs(kontrolle["v_ende"])},
        "skalierung_v_mit_A2": {"v_0.05_zu_0.025": verh(v[0.05], v[0.025]), "v_0.1_zu_0.05": verh(v[0.1], v[0.05]),
                                "soll_zweite_ordnung": 4.0},
        "L3_aufloesung": {f"A={amp}": {"v_fein": v[amp], "v_grob": vg[amp],
                                       "bestanden": abs(v[amp]) >= 5.0 * abs(v[amp] - vg[amp])}
                          for amp in (0.1, 0.2)},
        "mitgenommen": {f"A={amp}": z(fein, "ball_und_welle", amp)["mitgenommen"] for amp in SU_A},
    }
    text = [f"Paket k = {SU_K}, v_g = {SU_VG:.4f}, sigma = {SU_SIGMA}, Start x = {SU_X0}; Ball ruht bei x = 0",
            "A | v_ende (grob, fein) | mitgenommen | X_min, X_max | E-Gewinn rel | dQ rel | S_max min, max rel | "
            "S_max Welle allein"]
    for amp in SU_A + [0.0]:
        art = "nur_ball" if amp == 0.0 else "ball_und_welle"
        q, g = z(fein, art, amp), z(grob, art, amp)
        sw = "-" if amp == 0.0 else f"{z(fein, 'nur_welle', amp)['S_max_welle_max']:.3e}"
        text.append(f"  {amp:.3f} | {g['v_ende']:.3e}, {q['v_ende']:.3e} | {q['mitgenommen']} | "
                    f"{q['X_min']:.3f}, {q['X_max']:.3f} | {q['E_gewinn_rel']:.2e} | {q['Q_fenster_aenderung_rel']:.1e} | "
                    f"{q['S_max_min_rel']:.4f}, {q['S_max_max_rel']:.4f} | {sw}")
    return k, text


# ---------------------------------------------------------------- 5 Brandung (Wellen 13)
BR_XA, BR_XB = 20.0, 100.0    # See (stabiles Kondensat S = 1) zwischen zwei natuerlichen Waenden
BR_MU = math.sqrt(0.5)        # Frequenz des Sees: U'(1) = 1/2
BR_X0 = -5.0                  # Startort des Balls
BR_V = [0.1, 0.3, 0.5]
BR_PHASEN = [0.0, 0.5 * math.pi, math.pi, 1.5 * math.pi]
BR_T = 450.0


def see(x):
    """F^2 = 1 / (1 + exp(-sqrt2 (x - XA))) / (1 + exp(sqrt2 (x - XB))): zwei exakte Wandloesungen bei omega^2 = 1/2
    (f' = f (1 - f^2) / sqrt2), innen S = 1. Die Waende wechselwirken nur mit exp(-sqrt2 80)."""
    r2 = math.sqrt(2.0)
    s = 1.0 / (1.0 + torch.exp(-r2 * (x - BR_XA))) / (1.0 + torch.exp(r2 * (x - BR_XB)))
    return torch.sqrt(s)


def lauf_brandung(prof, dx, dt, t_end):
    x = gitter(dx)
    iw = OMEGA2.index(OM_BALL)
    F = see(x)
    ps, vs = F.to(torch.complex128), -1j * BR_MU * F
    laeufe, psi, vel = [], [], []
    for v in BR_V:
        for phase in BR_PHASEN:
            pb, vb = ball(x, prof, iw, BR_X0, v, phase)
            laeufe.append({"art": "see_und_ball", "v": v, "phase": phase})
            psi.append(ps + pb)
            vel.append(vs + vb)
    for v in BR_V:
        pb, vb = ball(x, prof, iw, BR_X0, v, 0.0)
        laeufe.append({"art": "nur_ball", "v": v, "phase": 0.0})
        psi.append(pb)
        vel.append(vb)
    laeufe.append({"art": "nur_see", "v": 0.0, "phase": 0.0})
    psi.append(ps)
    vel.append(vs)
    psi, vel = torch.stack(psi), torch.stack(vel)
    psi[:, 0] = 0.0
    psi[:, -1] = 0.0
    vel[:, 0] = 0.0
    vel[:, -1] = 0.0
    vor = (x < BR_XA - 4.0).to(F64)
    see_b = ((x >= BR_XA - 4.0) & (x <= BR_XB + 4.0)).to(F64)
    hinter = (x > BR_XB + 4.0).to(F64)
    wandzone = (x >= BR_XA - 4.0) & (x <= BR_XA + 12.0)

    def messen(psi, vel, t):
        s, rho, e = dichten(psi, vel, dx, False)
        q_vor = (rho * vor).sum(1) * dx
        X = teilen((x * rho * vor).sum(1) * dx, q_vor)
        breite = torch.sqrt(teilen(((x - X.unsqueeze(1)) ** 2 * rho * vor).sum(1) * dx, q_vor).clamp(min=0.0))
        x_wand = BR_XA - 4.0 + dx * ((s < 0.5) & wandzone).sum(1).to(F64)
        return torch.stack([q_vor, X, breite, (s * vor).max(dim=1).values, (rho * see_b).sum(1) * dx,
                            (rho * hinter).sum(1) * dx, x_wand, e.sum(1) * dx, rho.sum(1) * dx], dim=1)

    _, _, reihe = entwickeln(psi, vel, dx, dt, t_end, False, schwamm(x), messen, T_MESS)
    d = endlich(torch.stack(reihe))              # (M, B, 9)
    t = torch.arange(d.shape[0], dtype=F64, device=DEV) * T_MESS
    v_vor = gerade(t, d[:, :, 1], t_end - min(50.0, 0.5 * t_end), t_end)
    zeilen = []
    for b, r in enumerate(laeufe):
        if r["art"] == "nur_see":
            zeilen.append(dict(r, **{"ausgang": "Kontrolle See",
                                     "Q_see_aenderung_rel": (d[-1, b, 4] / d[0, b, 4] - 1.0).item(),
                                     "x_wand_start": d[0, b, 6].item(),
                                     "x_wand_max_abw": (d[:, b, 6] - d[0, b, 6]).abs().max().item(),
                                     "E_box_rest": (d[-1, b, 7] / d[0, b, 7]).item()}))
            continue
        q_ball = d[0, b, 0].item()
        vor_kontakt = (d[:, b, 1] < BR_XA - 10.0) & (d[:, b, 0] > 0.5 * q_ball)
        s_rel = (d[:, b, 3] / d[0, b, 3] - 1.0).abs()
        b_rel = (d[:, b, 2] / d[0, b, 2] - 1.0).abs()
        anteil_vor = d[-1, b, 0].item() / q_ball
        anteil_see = (d[-1, b, 4] - d[0, b, 4]).item() / q_ball
        anteil_hinter = d[-1, b, 5].item() / q_ball
        if r["art"] == "nur_ball":
            ausgang = "Kontrolle Ball"
        elif anteil_hinter >= 0.5:
            ausgang = "durchgereicht (Ladung tritt hinter dem See aus)"
        elif anteil_vor >= 0.8 and v_vor[b].item() < 0.0:
            ausgang = "zurueckgeworfen, Ball erhalten"
        elif anteil_see >= 0.8:
            ausgang = "aufgenommen (Ball loest sich im See auf)"
        else:
            ausgang = "zerbrochen oder teilweise aufgenommen"
        zeilen.append(dict(r, **{
            "ausgang": ausgang, "Q_ball": q_ball, "anteil_vor": anteil_vor, "anteil_see": anteil_see,
            "anteil_hinter": anteil_hinter, "v_vor_ende": v_vor[b].item(),
            "verformung_S_vor_kontakt": s_rel[vor_kontakt].max().item() if bool(vor_kontakt.any()) else None,
            "verformung_breite_vor_kontakt": b_rel[vor_kontakt].max().item() if bool(vor_kontakt.any()) else None,
            "S_max_vor_ende_rel": (d[-1, b, 3] / d[0, b, 3]).item(),
            "breite_vor_ende_rel": (d[-1, b, 2] / d[0, b, 2]).item(),
            "x_wand_verschiebung": (d[-1, b, 6] - d[0, b, 6]).item(),
            "E_box_rest": (d[-1, b, 7] / d[0, b, 7]).item(), "Q_box_rest": (d[-1, b, 8] / d[0, b, 8]).item()}))
    return zeilen, {"spalten": ["Q_vor", "X_vor", "breite_vor", "S_max_vor", "Q_see", "Q_hinter", "x_wand", "E_box",
                                "Q_box"], "laeufe": laeufe, "daten": d.cpu()}


def bewerten_brandung(grob, fein):
    def schluessel(q):
        return (q["art"], q["v"], q["phase"])

    g_idx = {schluessel(q): q for q in grob}
    see_k = next(q for q in fein if q["art"] == "nur_see")
    ball_k = [q for q in fein if q["art"] == "nur_ball"]
    stoss = [q for q in fein if q["art"] == "see_und_ball"]
    verf = max((q["verformung_S_vor_kontakt"] or 0.0) for q in ball_k)
    gleich = all(q["ausgang"] == g_idx[schluessel(q)]["ausgang"] for q in stoss)
    aend = max(max(abs(q["anteil_see"] - g_idx[schluessel(q)]["anteil_see"]),
                   abs(q["anteil_vor"] - g_idx[schluessel(q)]["anteil_vor"])) for q in stoss)
    k = {
        "gegenprobe_see_allein_stabil": {"x_wand_max_abw": see_k["x_wand_max_abw"],
                                         "Q_see_aenderung_rel": see_k["Q_see_aenderung_rel"],
                                         "bestanden": see_k["x_wand_max_abw"] <= 0.5
                                         and abs(see_k["Q_see_aenderung_rel"]) <= 1e-3},
        "gegenprobe_ball_allein": {"max_verformung_S_vor_kontakt": verf, "bestanden": verf <= 1e-3},
        "L3_aufloesung": {"ausgang_gleich_grob_fein": gleich, "max_aenderung_anteile": aend,
                          "bestanden": gleich and aend <= 0.2},
    }
    text = [f"See S = 1 auf [{BR_XA}, {BR_XB}], mu = {BR_MU:.4f}; Ball omega^2 = {OM_BALL} startet bei x = {BR_X0}",
            "v | Phase/pi | Ausgang | Anteil vor, See, hinter | v_vor Ende | Verformung S, Breite vor Kontakt | "
            "S_max, Breite am Ende rel | Wandverschiebung"]
    for q in fein:
        if q["art"] == "nur_see":
            text.append(f"  See allein: Wand wandert max {q['x_wand_max_abw']:.3f}, Q_See rel {q['Q_see_aenderung_rel']:.1e}")
            continue
        vs = "-" if q["verformung_S_vor_kontakt"] is None else f"{q['verformung_S_vor_kontakt']:.1e}"
        vb = "-" if q["verformung_breite_vor_kontakt"] is None else f"{q['verformung_breite_vor_kontakt']:.1e}"
        text.append(f"  {q['v']:.1f} | {q['phase'] / math.pi:.1f} | {q['ausgang']} | {q['anteil_vor']:.3f}, "
                    f"{q['anteil_see']:.3f}, {q['anteil_hinter']:.3f} | {q['v_vor_ende']:.3f} | {vs}, {vb} | "
                    f"{q['S_max_vor_ende_rel']:.3f}, {q['breite_vor_ende_rel']:.3f} | {q['x_wand_verschiebung']:.2f}")
    return k, text


# ---------------------------------------------------------------- Hauptprogramm
TESTS = {
    "russell": (lauf_russell, bewerten_russell, RUS_T),
    "monster": (lauf_monster, bewerten_monster, MON_T),
    "stokes": (lauf_stokes, bewerten_stokes, ST_T),
    "surfen": (lauf_surfen, bewerten_surfen, SU_T),
    "brandung": (lauf_brandung, bewerten_brandung, BR_T),
}


def test_ausfuehren(name, t_end, ordner):
    lauf, bewerten, _ = TESTS[name]
    os.makedirs(ordner, exist_ok=True)
    start = jetzt()
    print(f"R4-W {name} Start {start} auf {torch.cuda.get_device_name(0)}, torch {torch.__version__}, T = {t_end}",
          flush=True)
    dauer = {}
    t0 = uhr()
    prof = profil_holen()
    dauer["profil_s"] = uhr() - t0
    k0 = profil_kontrolle(prof)
    print(f"Profil ({prof['herkunft']}) nach {dauer['profil_s']:.1f} s, K0 max|f - Anker| = {k0['max_abw_f']:.1e}",
          flush=True)
    ergebnis, reihen = {}, {}
    for stufe, dx, dt in (("grob", DX, DT), ("fein", DX / 2.0, DT / 2.0)):
        t0 = uhr()
        zeilen, r = lauf(prof, dx, dt, t_end)
        dauer[stufe + "_s"] = uhr() - t0
        ergebnis[stufe], reihen[stufe] = zeilen, r
        print(f"{name} {stufe} fertig nach {dauer[stufe + '_s']:.1f} s", flush=True)
        torch.cuda.empty_cache()
    kontrollen, text = bewerten(ergebnis["grob"], ergebnis["fein"])
    kontrollen["K0_profil_gegen_anker"] = k0
    ende = jetzt()
    ausgabe = {"test": name, "start": start, "ende": ende, "dauer_s": dauer, "geraet": torch.cuda.get_device_name(0),
               "torch": torch.__version__, "T": t_end, "dx_dt_grob": [DX, DT], "dx_dt_fein": [DX / 2.0, DT / 2.0],
               "omega2_ball": OM_BALL, "ergebnis": ergebnis, "kontrollen": kontrollen}
    with open(os.path.join(ordner, name + "_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)
    torch.save(reihen, os.path.join(ordner, name + "_reihen.pt"))
    kopf = [f"R4-W {name}. Start {start}, Ende {ende}, Geraet {ausgabe['geraet']}, torch {torch.__version__}, T = {t_end}",
            "Dauer [s]: " + ", ".join(f"{k} {s:.1f}" for k, s in dauer.items()), ""]
    fuss = ["", "Kontrollen und Latten:"] + [f"  {kn}: {json.dumps(kv, default=str)}" for kn, kv in kontrollen.items()]
    bericht = "\n".join(kopf + text + fuss)
    with open(os.path.join(ordner, name + "_bericht.txt"), "w") as fh:
        fh.write(bericht + "\n")
    print(bericht, flush=True)


def main():
    ap = argparse.ArgumentParser(description="R4-W: fuenf 1D-Wellentests mit Q-Baellen (Runde 4)")
    ap.add_argument("befehl", choices=["profil", "rauch"] + list(TESTS))
    ap.add_argument("--T", type=float, default=None, help="Laufzeit in Modellzeit (Vorgabe je Test)")
    ap.add_argument("--out", default=os.path.join(HIER, "ausgabe"))
    ap.add_argument("--rauch", action="store_true", help=f"kurze Laufzeit T = {T_RAUCH} (nur Durchlaufprobe)")
    args = ap.parse_args()
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    if args.befehl == "profil":
        t0 = uhr()
        prof = profil_holen()
        k0 = profil_kontrolle(prof)
        print(f"Profil ({prof['herkunft']}) nach {uhr() - t0:.1f} s: {json.dumps(k0)}", flush=True)
        return
    namen = list(TESTS) if args.befehl == "rauch" else [args.befehl]
    for name in namen:
        if args.befehl == "rauch" or args.rauch:
            t_end = T_RAUCH
        else:
            t_end = args.T if args.T is not None else TESTS[name][2]
        test_ausfuehren(name, t_end, args.out)


if __name__ == "__main__":
    main()
