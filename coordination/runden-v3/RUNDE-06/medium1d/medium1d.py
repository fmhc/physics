#!/usr/bin/env python3
"""Runde 6 (runden-v3), Agent M1: Medium-Karten in 1D (Wellen 3, 5, 6, 7, 11; Bio 2, 21; Chemie 9). Explorativ.

Plan, Vorhersagen, Gegenproben, Latten und Aufrufe: PLAN.md daneben. float64/complex128, --geraet cuda|cpu.
Baut auf RUNDE-05/r5d/r5d.py auf (Medium-Rolle kc = 0, g4 > 0). Periodische Box [-300, 300), keine Daempfung.

Modell:
  L = |psi_t|^2 + |chi_t|^2 - |psi_x|^2 - |D chi|^2 - V,  D = d_x - i A(t)   (A: gleichfoermiges Eichfeld, nur zum
      langsamen Hochfahren der Stroemung; Endzustand = Medium mit Impuls K = -A, bei festem Gesamtladungsinhalt)
  V = U(S) + mc2 C + g4 C^2 + lam S C + eps (conj(psi) chi + c.c.) + Phi(x, t) S + W(x, t) C
  U(S) = S - S^2 + S^3/2,  S = |psi|^2,  C = |chi|^2
  Phi = kappa R^2/2 prod_i tanh^2(gamma d_i / R): Falle, haelt den Ball fest oder zieht ihn (Kontraktion gamma)
  W   = aeusseres Potential des Mediums (nur Nische): Dichtegefaelle
Bewegungsgleichungen:
  psi_tt = psi_xx - [U'(S) + lam C + Phi] psi - eps chi
  chi_tt = D^2 chi - [mc2 + 2 g4 C + lam S + W] chi - eps psi,   Gitter: D^2 chi_j = (e^{-iA dx} chi_{j+1} - 2 chi_j
           + e^{iA dx} chi_{j-1})/dx^2
Einschwingen (Kern dieser Runde): lam, eps und die Falle werden glatt eingeschaltet (C2-Rampe), dann die Stroemung
bzw. die Fallengeschwindigkeit glatt hochgefahren; gemessen wird erst nach einer Abklingzeit. Kraft des Mediums auf
Ball i: F_med = -lam Int_{Fenster i} S dC/dx dx; Kraft der Falle F_fal = -Int S dPhi/dx dx.

Aufruf:  python medium1d.py <unterbefehl> [--geraet cuda|cpu] [--out ORDNER] [--faktor F] [--stufen beide|grob]
  rauch          alle Unterbefehle mit Zeiten x 0,05 (prueft nur den Durchlauf; Zahlen gelten nicht)
  landau         Wellen 5   stationaere Kraft gegen u, zwei Mediendichten (Schwelle gegen c_s)
  gleiten        Wellen 6   Kraft bis u = 0,9 (Maximum ueber der Schwelle?)
  einschwingen   (kreuzen)  freier Ball: ploetzlich wie r5d kreuzen gegen adiabatisch
  windschatten   Wellen 7   zwei Baelle hintereinander, Abstand d
  fahrtwind      Wellen 11  ruhender Ball im stroemenden Medium gegen bewegter Ball im ruhenden Medium (Lorentz)
  stokes         Wellen 3   Ball in einer von weit her einlaufenden Schallwelle, drei Amplituden
  osmose         Bio 2      Ladungsfluss Ball <-> Medium ueber eps gegen die Mediendichte
  massenwirkung  Chemie 9   drei Baelle im Medium mit eps
  nische         Bio 21     freier Ball in sanftem Dichtegefaelle
Ausgabe im --out-Ordner: medium1d_<test>_<stufe>_roh.pt (Rohdaten nach jeder Stufe), medium1d_<unterbefehl>_bericht.txt
und _ergebnis.json (nach jedem Test neu geschrieben).
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
DEV = torch.device("cpu")          # in main() gesetzt
OUT = "."                          # in main() gesetzt
STUFEN = ("grob", "fein")          # --stufen grob: nur grob (lokaler Rauchtest)

DX, DT, FEIN = 0.1, 0.05, 0.5      # wie r5d.py; fein halbiert dx und dt (Latte L3)
L_BOX = 300.0                      # periodische Box [-L, L), Laenge 600
T_MESS = 0.5
W2 = 0.7                           # psi-Ball omega^2: Q 2,441, E 2,298, N = Int S = 1,459, FWHM 3,56
G4, MC2, LAM = 0.5, 1.0, 0.1       # Medium U_chi = mc2 C + g4 C^2; Dichtekopplung lam
KAPPA, R_FALLE = 0.02, 8.0         # Falle: Steifigkeit, Reichweite (Fallenperiode ~56, Hoechstkraft ~0,09)
FENSTER = 12.0                     # Halbbreite des Ballfensters
T_LAM = (0.0, 100.0)               # lam, eps, Falle glatt einschalten
T_STROM = (120.0, 320.0)           # Stroemung glatt hochfahren
RUHE = 50.0                        # Abklingzeit nach dem Hochfahren
F_MIN = 2e-6                       # vorab: |F| darunter gilt als "keine Kraft"
SPEICHER_GB = 1.5
RAUCH_FAKTOR = 0.05


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


def wrap(d):
    """Abstand in der periodischen Box nach [-L, L)."""
    return torch.remainder(d + L_BOX, 2.0 * L_BOX) - L_BOX


def gitter(dx):
    n = int(round(2.0 * L_BOX / dx))
    return (torch.arange(n, dtype=F64, device=DEV) - n // 2) * dx


def glatt(t, t0, t1):
    """C2-Rampe 0 -> 1 zwischen t0 und t1 (smootherstep)."""
    s = ((t - t0) / (t1 - t0)).clamp(0.0, 1.0)
    return s * s * s * (10.0 + s * (-15.0 + 6.0 * s))


def glatt_integral(t, t0, t1):
    s = ((t - t0) / (t1 - t0)).clamp(0.0, 1.0)
    return (t1 - t0) * s ** 4 * (2.5 + s * (-3.0 + s)) + (t - t1).clamp(min=0.0)


# ================================================================ 1D-Anker (aus r5d.py) und Medium-Formeln

def anker_ab(w2):
    return 1.0 - w2, math.sqrt(2.0 * w2 - 1.0)


def profil(y, w2):
    a0, b0 = anker_ab(w2)
    z = (2.0 * math.sqrt(a0) * y).clamp(-700.0, 700.0)
    return torch.sqrt(2.0 * a0 / (1.0 + b0 * torch.cosh(z)))


def anker_q_e(w2):
    a0, b0 = anker_ab(w2)
    integral = math.sqrt(2.0) * math.acosh(1.0 / b0)
    w = w2 * integral
    g = math.sqrt(a0) / 2.0 - b0 * b0 * integral / 4.0
    return 2.0 * w / math.sqrt(w2), w + g + w + g


def k_eff2(k, dx):
    return (2.0 - 2.0 * math.cos(k * dx)) / (dx * dx)


def om0(c, mc2=MC2, g4=G4):
    return math.sqrt(mc2 + 2.0 * g4 * c)


def schall(c, mc2=MC2, g4=G4):
    g = 2.0 * g4 * c
    return math.sqrt(g / (2.0 * (mc2 + g) + g)) if c > 0.0 else 0.0


def k_stroemung(u, c0, art="lorentz", mc2=MC2, g4=G4):
    """Impuls des Mediums mit Ruhdichte c0 und Stroemung u: Lorentz K = gamma omega0 u; 'galilei' K = omega0 u."""
    w = om0(c0, mc2, g4)
    return w * u / math.sqrt(1.0 - u * u) if art == "lorentz" else w * u


def c_start(c0, k, dx, mc2=MC2, g4=G4):
    """Ruhdichte am Anfang, die nach dem Hochfahren auf Impuls k bei gleicher Ladungsdichte C = c0 ergibt."""
    rho = 2.0 * math.sqrt(k_eff2(k, dx) + mc2 + 2.0 * g4 * c0) * c0
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if 2.0 * math.sqrt(mc2 + 2.0 * g4 * mid) * mid > rho:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def u_gitter(k, c0, dx, mc2=MC2, g4=G4):
    """Stroemungsgeschwindigkeit (Gruppengeschwindigkeit) des Mediums mit Impuls k auf dem Gitter."""
    return math.sin(k * dx) / dx / math.sqrt(k_eff2(k, dx) + mc2 + 2.0 * g4 * c0)


def bogoliubov(k, c0, mc2=MC2, g4=G4):
    """Schallast Om(k) aus (k^2 - Om^2)(k^2 - Om^2 + 2g) = 4 omega0^2 Om^2."""
    g, w2 = 2.0 * g4 * c0, mc2 + 2.0 * g4 * c0
    b = 2.0 * g + 4.0 * w2
    a = 0.5 * (-b + math.sqrt(b * b + 16.0 * w2 * k * k))
    return math.sqrt(max(k * k - a, 0.0))


def kielwelle(u, c0, mc2=MC2, g4=G4):
    """Wellenzahl der stehenden Bugwelle im Ballsystem (Om(k) = u k im Mediumsystem, dann k/gamma); nan unter c_s."""
    g, w2 = 2.0 * g4 * c0, mc2 + 2.0 * g4 * c0
    q = (4.0 * w2 * u * u / (1.0 - u * u) - 2.0 * g) / (1.0 - u * u)
    return math.sqrt(q) * math.sqrt(1.0 - u * u) if q > 0.0 else float("nan")


def ft_profil(k, w2):
    y = torch.arange(-80.0, 80.0 + 1e-9, 0.005, dtype=F64, device=DEV)
    return gf((profil(y, w2) * torch.cos(k * y)).sum()) * 0.005


# ================================================================ Laeufe, Zeitplaene, Anfangsfelder

def lauf(name, **kw):
    """Lauf mit Vorgaben; Zeiten sind Tupel (t0, t1) der glatten Rampen."""
    r = dict(name=name, C0=0.1, g4=G4, mc2=MC2, lam=LAM, eps=0.0, baelle=[(0.0, W2)], falle=True, K=0.0, u=0.0,
             t_lam=T_LAM, t_strom=T_STROM, v_falle=0.0, t_zug=(120.0, 370.0), kontraktion=True, t_frei=None,
             W_dC=0.0, W_lam=60.0, t_w=(0.0, 150.0), n_wind=None, paket=None, t_mess=None, kontrolle=False)
    r.update(kw)
    return r


def stroemung(r, u, art="lorentz"):
    """Stroemung u ueber das Eichfeld (adiabatisch, Ladung so gewaehlt, dass am Ende C = C0 ist)."""
    r["u"], r["K"], r["u_art"] = u, math.copysign(k_stroemung(abs(u), r["C0"], art, r["mc2"], r["g4"]), u), art
    return r


def skalieren(laeufe, f):
    for r in laeufe:
        for key in ("t_lam", "t_strom", "t_zug", "t_frei", "t_w", "t_mess"):
            if r.get(key) is not None:
                r[key] = (r[key][0] * f, r[key][1] * f)
        if r.get("paket"):
            r["paket"] = dict(r["paket"], t=r["paket"]["t"] * f)
    return laeufe


def spalte(werte):
    return torch.tensor(werte, dtype=F64, device=DEV).view(1, -1)


def plaene(laeufe, x, dx, dt, n_s):
    """Zeitplaene (Schritte+1, B, 1) als Tensoren; je Schritt nur eine Sicht, kein Rechnen auf dem Host."""
    nb = max(1, max(len(r["baelle"]) for r in laeufe))
    t = (torch.arange(n_s + 1, dtype=F64, device=DEV) * dt).view(-1, 1)
    sp = lambda key, i: spalte([r[key][i] for r in laeufe])
    fern = spalte([1e9 if r["t_frei"] is None else r["t_frei"][0] for r in laeufe])
    fern1 = spalte([1e9 + 1 if r["t_frei"] is None else r["t_frei"][1] for r in laeufe])
    an = glatt(t, sp("t_lam", 0), sp("t_lam", 1))
    kap = spalte([KAPPA if r["falle"] else 0.0 for r in laeufe]) * an * (1.0 - glatt(t, fern, fern1))
    a_t = -spalte([r["K"] for r in laeufe]) * glatt(t, sp("t_strom", 0), sp("t_strom", 1))
    v = spalte([r["v_falle"] for r in laeufe])
    v_t = v * glatt(t, sp("t_zug", 0), sp("t_zug", 1))
    gam = torch.where(spalte([1.0 if r["kontraktion"] else 0.0 for r in laeufe]) > 0.5,
                      1.0 / torch.sqrt(1.0 - v_t * v_t), torch.ones_like(v_t))
    x0 = torch.full((len(laeufe), nb), 0.0, dtype=F64, device=DEV)
    echt = torch.zeros((len(laeufe), nb), dtype=F64, device=DEV)
    for b, r in enumerate(laeufe):
        for i, (xb, _) in enumerate(r["baelle"]):
            x0[b, i], echt[b, i] = xb, 1.0
    wprof = torch.stack([-2.0 * r["g4"] * r["W_dC"] * torch.sin(2.0 * PI * x / r["W_lam"]) for r in laeufe])
    pl = {"lam": (spalte([r["lam"] for r in laeufe]) * an).unsqueeze(-1),
          "eps": (spalte([r["eps"] for r in laeufe]) * an).unsqueeze(-1),
          "kap": kap.unsqueeze(-1), "phase": torch.exp(-1j * a_t * dx).unsqueeze(-1),
          "zug": (v * glatt_integral(t, sp("t_zug", 0), sp("t_zug", 1))).unsqueeze(-1), "gam": gam.unsqueeze(-1),
          "w": glatt(t, sp("t_w", 0), sp("t_w", 1)).unsqueeze(-1), "wprof": wprof,
          "mc2": spalte([r["mc2"] for r in laeufe]).view(-1, 1), "g4": spalte([r["g4"] for r in laeufe]).view(-1, 1),
          "x0": x0, "echt": echt, "falle_echt": echt * spalte([1.0 if r["falle"] else 0.0 for r in laeufe]).view(-1, 1),
          "nb": nb, "t": t.view(-1),
          "mit_falle": any(r["falle"] for r in laeufe), "mit_eps": any(r["eps"] != 0.0 for r in laeufe),
          "mit_A": any(r["K"] != 0.0 for r in laeufe), "mit_w": any(r["W_dC"] != 0.0 for r in laeufe)}
    return pl


def fallen_pot(x, pl, n):
    """Phi (B, N) zum Schritt n: kappa R^2/2 prod_i tanh^2(gamma wrap(x - X_i)/R) ueber die echten Fallen."""
    xi = pl["x0"] + pl["zug"][n]                                        # (B, nb)
    d = wrap(x.view(1, 1, -1) - xi.unsqueeze(-1))
    th = torch.tanh(pl["gam"][n].unsqueeze(-1) * d / R_FALLE) ** 2
    m = pl["falle_echt"].unsqueeze(-1)
    return 0.5 * pl["kap"][n] * R_FALLE ** 2 * (m * th + (1.0 - m)).prod(dim=1)


def anfangsfelder(x, dx, laeufe):
    """psi: Baelle in Ruhe (geschlossenes Profil); chi: ruhendes Medium mit Anfangsdichte (fuer Eichrampe erhoeht),
    oder Stroemung mit Windung n_wind (exakte Gitterloesung, 'ploetzlich' wie r5d kreuzen)."""
    aus = [[], [], [], []]
    for r in laeufe:
        psi = torch.zeros_like(x, dtype=C128)
        vpsi = torch.zeros_like(x, dtype=C128)
        for xb, w2 in r["baelle"]:
            f = profil(wrap(x - xb), w2).to(C128)
            psi, vpsi = psi + f, vpsi - 1j * math.sqrt(w2) * f
        if r["C0"] <= 0.0:
            chi = torch.zeros_like(x, dtype=C128)
            vchi = chi.clone()
        elif r["n_wind"] is not None:
            k = 2.0 * PI * r["n_wind"] / (2.0 * L_BOX)
            om = math.sqrt(k_eff2(k, dx) + r["mc2"] + 2.0 * r["g4"] * r["C0"])
            chi = math.sqrt(r["C0"]) * torch.exp(1j * k * x)
            vchi = -1j * om * chi
        else:
            ci = c_start(r["C0"], r["K"], dx, r["mc2"], r["g4"]) if r["K"] != 0.0 else r["C0"]
            chi = torch.full_like(x, math.sqrt(ci), dtype=C128)
            vchi = -1j * om0(ci, r["mc2"], r["g4"]) * chi
        for j, f in enumerate((psi, vpsi, chi, vchi)):
            aus[j].append(f)
    return [torch.stack(a) for a in aus]


# ================================================================ Zeitentwicklung und Messung

def kraft(psi, chi, pl, n, x, dx):
    s = psi.real ** 2 + psi.imag ** 2
    c = chi.real ** 2 + chi.imag ** 2
    lam = pl["lam"][n]
    fp = 1.0 - 2.0 * s + 1.5 * s * s + lam * c
    fc = pl["mc2"] + 2.0 * pl["g4"] * c + lam * s
    if pl["mit_falle"]:
        fp = fp + fallen_pot(x, pl, n)
    if pl["mit_w"]:
        fc = fc + pl["w"][n] * pl["wprof"]
    ap = (torch.roll(psi, -1, 1) - 2.0 * psi + torch.roll(psi, 1, 1)) / (dx * dx) - fp * psi
    if pl["mit_A"]:
        e = pl["phase"][n]
        lc = (e * torch.roll(chi, -1, 1) - 2.0 * chi + e.conj() * torch.roll(chi, 1, 1)) / (dx * dx)
    else:
        lc = (torch.roll(chi, -1, 1) - 2.0 * chi + torch.roll(chi, 1, 1)) / (dx * dx)
    ac = lc - fc * chi
    if pl["mit_eps"]:
        ep = pl["eps"][n]
        ap, ac = ap - ep * chi, ac - ep * psi
    return ap, ac


SPALTEN_BALL = ["X", "F_med", "F_fal", "N", "Q_psi", "Q_tot", "arg_psi"]
SPALTEN_LAUF = ["C_fern", "rho_fern", "arg_chi_fern", "S_max", "Q_psi_alle", "Q_chi_alle", "C_min", "C_max"]


def messer(x, dx, pl):
    """Messfunktion mit mitgefuehrten Ballorten (Fenster je Ball, bei zwei Baellen nach dem naeheren Ball geteilt)."""
    xtr = pl["x0"].clone()
    echt = pl["echt"]
    fern = (wrap(x.view(1, -1) - (pl["x0"][:, :1] + L_BOX)).abs() < 5.0).to(F64)       # Gegenpunkt des ersten Balls
    n_fern = fern.sum(1).clamp(min=1.0)
    i_fern = torch.argmin(wrap(x.view(1, -1) - (pl["x0"][:, :1] + L_BOX)).abs(), dim=1, keepdim=True)

    def messen(n, psi, vpsi, chi, vchi):
        s = psi.real ** 2 + psi.imag ** 2
        c = chi.real ** 2 + chi.imag ** 2
        rp = 2.0 * (psi * vpsi.conj()).imag
        rc = 2.0 * (chi * vchi.conj()).imag
        d = wrap(x.view(1, 1, -1) - xtr.unsqueeze(-1))                                  # (B, nb, N)
        ab = torch.where(echt.unsqueeze(-1) > 0.5, d.abs(), torch.full_like(d, 1e9))
        naechst = ab <= ab.min(dim=1, keepdim=True).values
        w = ((d.abs() < FENSTER) & naechst).to(F64)
        sw = s.unsqueeze(1) * w
        nn = sw.sum(-1) * dx
        neu = xtr + torch.where(nn > 1e-12, (d * sw).sum(-1) * dx / nn.clamp(min=1e-300), torch.zeros_like(nn))
        xtr.copy_(wrap(neu))
        dc = (torch.roll(c, -1, 1) - torch.roll(c, 1, 1)) / (2.0 * dx)
        f_med = -pl["lam"][n] * (sw * dc.unsqueeze(1)).sum(-1) * dx
        if pl["mit_falle"]:
            phi = fallen_pot(x, pl, n)
            dphi = (torch.roll(phi, -1, 1) - torch.roll(phi, 1, 1)) / (2.0 * dx)
            f_fal = -(sw * dphi.unsqueeze(1)).sum(-1) * dx
        else:
            f_fal = torch.zeros_like(nn)
        q_psi = (rp.unsqueeze(1) * w).sum(-1) * dx
        q_tot = ((rp + rc).unsqueeze(1) * w).sum(-1) * dx
        i_b = torch.remainder(((xtr - x[0]) / dx).round().long(), x.shape[0])
        arg_psi = torch.angle(psi.gather(1, i_b))
        ball = torch.stack([xtr.clone(), f_med, f_fal, nn, q_psi, q_tot, arg_psi], dim=-1).flatten(1)   # (B, nb*7)
        lauf = torch.stack([(c * fern).sum(1) / n_fern, ((rp + rc) * fern).sum(1) / n_fern,
                            torch.angle(chi.gather(1, i_fern)).squeeze(1), s.max(1).values, rp.sum(1) * dx,
                            rc.sum(1) * dx, c.min(1).values, c.max(1).values], dim=1)
        return torch.cat([ball, lauf], dim=1)
    return messen


def entwickeln(felder, pl, x, dx, dt, n_s, alle, messen, hook=None):
    """Velocity-Verlet wie r5d.py (alle Laeufe als Stapel); hook = (Schritt, Funktion) aendert die Felder einmal."""
    psi, vpsi, chi, vchi = felder
    reihe = [messen(0, psi, vpsi, chi, vchi)]
    ap, ac = kraft(psi, chi, pl, 0, x, dx)
    h = 0.5 * dt
    for n in range(1, n_s + 1):
        vpsi = vpsi + h * ap
        vchi = vchi + h * ac
        psi = psi + dt * vpsi
        chi = chi + dt * vchi
        ap, ac = kraft(psi, chi, pl, n, x, dx)
        vpsi = vpsi + h * ap
        vchi = vchi + h * ac
        if hook is not None and n == hook[0]:
            psi, vpsi, chi, vchi = hook[1](psi, vpsi, chi, vchi)
            ap, ac = kraft(psi, chi, pl, n, x, dx)
        if n % alle == 0:
            reihe.append(messen(n, psi, vpsi, chi, vchi))
    daten = torch.stack(reihe)                                                          # (M, B, Spalten)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
    return t, daten, (psi, chi)


def stufen_rechnen(name, laeufe, t_end, hook_bauen=None):
    """Grob und fein; Rohdaten nach jeder Stufe sichern (eine abgestuerzte Auswertung kostet die Rechnung nicht)."""
    aus = {}
    for stufe, dx, dt in (("grob", DX, DT), ("fein", DX * FEIN, DT * FEIN)):
        if stufe not in STUFEN:
            continue
        x = gitter(dx)
        n_s = int(round(t_end / dt))
        alle = max(1, int(round(T_MESS / dt)))
        pl = plaene(laeufe, x, dx, dt, n_s)
        felder = anfangsfelder(x, dx, laeufe)
        hook = hook_bauen(x, dx, dt, laeufe) if hook_bauen else None
        t0 = uhr()
        t, daten, ende = entwickeln(felder, pl, x, dx, dt, n_s, alle, messer(x, dx, pl), hook)
        sek = uhr() - t0
        print(f"{name} {stufe}: {daten.shape[1]} Laeufe x {x.shape[0]} Punkte, T = {t_end:g}, {n_s} Schritte, "
              f"{sek:.1f} s", flush=True)
        st = {"t": t.cpu(), "daten": daten.cpu(), "sek": sek, "nb": pl["nb"], "dx": dx,
              "S_ende": (ende[0].abs() ** 2).cpu(), "C_ende": (ende[1].abs() ** 2).cpu(), "x": x.cpu()}
        torch.save(dict(st, laeufe=laeufe, spalten_ball=SPALTEN_BALL, spalten_lauf=SPALTEN_LAUF),
                   os.path.join(OUT, f"medium1d_{name}_{stufe}_roh.pt"))
        aus[stufe] = st
    return aus


def reihe(st, b, spalte_name, ball=0):
    """Zeitreihe einer Spalte fuer Lauf b (und Ball) aus den Rohdaten."""
    if spalte_name in SPALTEN_BALL:
        j = ball * len(SPALTEN_BALL) + SPALTEN_BALL.index(spalte_name)
    else:
        j = st["nb"] * len(SPALTEN_BALL) + SPALTEN_LAUF.index(spalte_name)
    return st["daten"][:, b, j]


# ================================================================ Auswerte-Hilfen

def entfalten_ort(xr):
    return torch.cat([xr[:1], xr[:1] + torch.cumsum(wrap(xr[1:] - xr[:-1]), 0)])


def steigung(t, y):
    tm = t - t.mean()
    return float((tm * (y - y.mean())).sum() / (tm * tm).sum()) if t.numel() > 2 else float("nan")


def beschl(t, y):
    if t.numel() < 4:
        return float("nan")
    h = 0.5 * float(t[-1] - t[0])
    tm = (t - t.mean()) / h
    a = torch.stack([torch.ones_like(tm), tm, tm * tm], 1)
    return 2.0 * float(torch.linalg.solve(a.T @ a, a.T @ y)[2]) / (h * h)


def maske(t, ta, tb):
    return (t >= ta - 1e-9) & (t <= tb + 1e-9)


def hann_mittel(y):
    """Mittel mit Hann-Gewicht: Restschwingungen (Falle, Atmen) mit >= 2 Perioden im Fenster fallen fast ganz heraus."""
    if y.numel() < 4:
        return float(y.mean()) if y.numel() else float("nan")
    w = torch.hann_window(y.numel(), periodic=False, dtype=F64)
    return float((w * y).sum() / w.sum())


def kraft_stat(st, r, b, ball=0, fenster=None):
    """Stationaere Kenngroessen im Messfenster: mittlere Kraft (Hann; auch je Haelfte), Ballbewegung, Einschwingspitze."""
    t = st["t"]
    ta, tb = fenster or r["t_mess"]
    m = maske(t, ta, tb)
    f = reihe(st, b, "F_med", ball)[m]
    h = f.numel() // 2
    xr = entfalten_ort(reihe(st, b, "X", ball))
    vor = maske(t, r["t_lam"][1], ta) & ~m
    smax = reihe(st, b, "S_max")
    i_an = int(maske(t, 0.0, r["t_lam"][1]).sum()) - 1
    return {"F": hann_mittel(f), "F_h1": hann_mittel(f[:h]), "F_h2": hann_mittel(f[h:]), "F_std": float(f.std()),
            "F_fal": hann_mittel(reihe(st, b, "F_fal", ball)[m]),
            "F_einschwing_max": float(reihe(st, b, "F_med", ball)[vor].abs().max()) if bool(vor.any()) else 0.0,
            "v": steigung(t[m], xr[m]), "a": beschl(t[m], xr[m]), "x_ende": float(xr[-1] - xr[0]),
            "S_halt": teilen(float(smax[-1]), float(smax[max(i_an, 0)])), "C_fern": float(reihe(st, b, "C_fern")[m].mean()),
            "C_spanne_ende": float(reihe(st, b, "C_max")[-1] - reihe(st, b, "C_min")[-1])}


def paare(erg):
    """(grob, fein)-Paare fuer L3; leer, wenn nur eine Stufe gerechnet wurde (--stufen grob oder fein)."""
    return list(zip(erg["grob"], erg["fein"])) if "grob" in erg and "fein" in erg else []


def l3(g, f, null=0.0):
    eff, aend = abs(g - null), abs(f - g)
    return {"effekt": eff, "aenderung": aend, "bestanden": bool(eff >= 5.0 * aend)}


def l3_zeile(liste):
    n_ok = sum(1 for e in liste for k, v in e.items() if k != "lauf" and v["bestanden"])
    n_ges = sum(1 for e in liste for k in e if k != "lauf")
    return f"  L3 (Effekt >= 5 x Aenderung grob -> fein): {n_ok} von {n_ges} Kenngroessen bestanden"


def zeit_zeile(stufen):
    return "  Rechenzeit " + ", ".join(f"{s} {st['sek']:.1f} s" for s, st in stufen.items())


def fmt(v, form=".2e"):
    return format(v, form) if isinstance(v, float) and math.isfinite(v) else str(v)


# ================================================================ Wellen 5/6: landau, gleiten

def schwelle(zeilen, c0):
    """u_c zwischen dem groessten u ohne Kraft (|F| < F_MIN) und dem kleinsten u mit Kraft (Hauptlaeufe, u > 0)."""
    hz = sorted((z for z in zeilen if z["C0"] == c0 and z["u"] > 0.0 and not z["kontrolle"] and z["lam"] == LAM
                 and "langsam" not in z["name"]), key=lambda z: z["u"])
    mit = [z["u"] for z in hz if abs(z["F"]) >= F_MIN]
    if not mit:
        return float("nan"), "keine Kraft bis u = %.2f" % (hz[-1]["u"] if hz else 0.0)
    ohne = [z["u"] for z in hz if z["u"] < mit[0]]
    if not ohne:
        return float("nan"), "Kraft schon beim kleinsten u = %.2f" % mit[0]
    uc = 0.5 * (ohne[-1] + mit[0])
    return uc, f"u_c = {uc:.3f} (zwischen {ohne[-1]:.2f} und {mit[0]:.2f}), u_c/c_s = {uc / schall(c0):.2f}"


def auswertung_kraft(laeufe, stufen):
    erg = {}
    for s, st in stufen.items():
        zz = []
        for b, r in enumerate(laeufe):
            z = dict(kraft_stat(st, r, b), name=r["name"], u=r["u"], C0=r["C0"], lam=r["lam"],
                     kontrolle=r["kontrolle"], c_s=schall(r["C0"]),
                     u_gitter=u_gitter(r["K"], r["C0"], st["dx"]) if r["K"] != 0.0 else r["u"])
            zz.append(z)
        erg[s] = zz
    return erg


def bericht_kraft(titel, laeufe, erg, stufen, extra):
    zz = [titel, "  Lauf | u (Gitter) | u/c_s | F_med Fenster (1./2. Haelfte) | F_std | F_Falle | Einschwing-Spitze | "
                 "v, a Ball | S gehalten | C fern"]
    for s in erg:
        zz.append(f"  [{s}]")
        for z in erg[s]:
            zz.append(f"  {z['name']:28s} | {z['u_gitter']:+.4f} | {teilen(z['u'], z['c_s']) if z['c_s'] else 0.0:+.2f} | "
                      f"{fmt(z['F'])} ({fmt(z['F_h1'])}, {fmt(z['F_h2'])}) | {fmt(z['F_std'])} | {fmt(z['F_fal'])} | "
                      f"{fmt(z['F_einschwing_max'])} | {fmt(z['v'])}, {fmt(z['a'])} | {z['S_halt']:.4f} | "
                      f"{z['C_fern']:.6f}")
        zz += extra(erg[s])
    return zz


def test_landau(f):
    laeufe = []
    for c0, us in ((0.1, [0.0, 0.05, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.21, 0.25, 0.30, 0.40]),
                   (0.3, [0.10, 0.15, 0.19, 0.23, 0.27, 0.31, 0.36, 0.45])):
        laeufe += [stroemung(lauf(f"C0={c0} u={u:.2f}", C0=c0), u) for u in us]
    laeufe += [stroemung(lauf("Spiegel C0=0.1 u=-0.25", kontrolle=True), -0.25),
               stroemung(lauf("lam=0 C0=0.1 u=0.25", lam=0.0, kontrolle=True), 0.25),
               stroemung(lauf("Medium allein u=0.25", baelle=[], falle=False, kontrolle=True), 0.25),
               stroemung(lauf("langsam C0=0.1 u=0.10", t_strom=(120.0, 420.0)), 0.10)]
    for r in laeufe:
        r["t_mess"] = (r["t_strom"][1] + RUHE, 570.0)
    skalieren(laeufe, f)
    stufen = stufen_rechnen("landau", laeufe, 570.0 * f)
    erg = auswertung_kraft(laeufe, stufen)
    extra = lambda zz: [f"  Schwelle C0 = {c0}: {schwelle(zz, c0)[1]} (c_s = {schall(c0):.4f})" for c0 in (0.1, 0.3)]
    l3_liste = [{"lauf": g["name"], "F": l3(g["F"], fz["F"])} for g, fz in paare(erg)
                if g["u"] != 0.0 and not g["kontrolle"]]
    for c0 in (0.1, 0.3) if "grob" in erg and "fein" in erg else ():
        ug, uf = schwelle(erg["grob"], c0)[0], schwelle(erg["fein"], c0)[0]
        if math.isfinite(ug) and math.isfinite(uf):
            l3_liste.append({"lauf": f"Schwelle C0={c0}", "u_c": l3(ug, uf)})
    text = bericht_kraft("landau (Wellen 5): Ball in Falle, Medium adiabatisch auf u (Lorentz, Ruhdichte C0). F_med = "
                         "Kraft des Mediums, gemittelt ab Rampenende + 50. F_MIN = %.0e." % F_MIN,
                         laeufe, erg, stufen, extra)
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste}, text + [l3_zeile(l3_liste), zeit_zeile(stufen)]


def test_gleiten(f):
    laeufe = [stroemung(lauf(f"lam=0.1 u={u:.2f}"), u) for u in (0.25, 0.30, 0.35, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90)]
    laeufe += [stroemung(lauf(f"lam=0.3 u={u:.2f}", lam=0.3), u) for u in (0.30, 0.50, 0.70, 0.90)]
    laeufe += [stroemung(lauf("Spiegel lam=0.1 u=-0.50", kontrolle=True), -0.50)]
    for r in laeufe:
        r["t_mess"] = (r["t_strom"][1] + RUHE, 570.0)
    skalieren(laeufe, f)
    stufen = stufen_rechnen("gleiten", laeufe, 570.0 * f)
    erg = auswertung_kraft(laeufe, stufen)

    def extra(zz):
        aus = []
        for lam in (0.1, 0.3):
            hz = [z for z in zz if z["lam"] == lam and not z["kontrolle"]]
            zm = max(hz, key=lambda z: abs(z["F"]))
            z9 = [z for z in hz if abs(z["u"] - 0.9) < 1e-9][0]
            aus.append(f"  lam = {lam}: groesste Kraft {fmt(zm['F'])} bei u = {zm['u']:.2f}; F(0,9)/F_max = "
                       f"{teilen(abs(z9['F']), abs(zm['F'])):.3f}; Kielwelle k' bei u_max = {kielwelle(zm['u'], 0.1):.3f}")
        return aus
    l3_liste = [{"lauf": g["name"], "F": l3(g["F"], fz["F"])} for g, fz in paare(erg)
                if not g["kontrolle"]]
    text = bericht_kraft("gleiten (Wellen 6): wie landau bis u = 0,9, C0 = 0,1, lam = 0,1 und 0,3.", laeufe, erg, stufen,
                         extra)
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste}, text + [l3_zeile(l3_liste), zeit_zeile(stufen)]


# ================================================================ Klaerung r5d kreuzen: einschwingen

def test_einschwingen(f):
    laeufe = []
    for n in (10, 16, 32):
        k = 2.0 * PI * n / (2.0 * L_BOX)
        u = k / math.sqrt(k * k + om0(0.1) ** 2)
        laeufe.append(lauf(f"ploetzlich frei n={n}", n_wind=n, u=u, falle=False, t_lam=(-1.0, -0.5)))
        laeufe.append(lauf(f"adiabatisch frei u={u:.4f}", K=k, u=u, falle=False))
    k32 = 2.0 * PI * 32 / (2.0 * L_BOX)
    u32 = k32 / math.sqrt(k32 * k32 + om0(0.1) ** 2)
    k10 = 2.0 * PI * 10 / (2.0 * L_BOX)
    laeufe += [lauf("ploetzlich lam=0 n=32", n_wind=32, u=u32, lam=0.0, falle=False, t_lam=(-1.0, -0.5), kontrolle=True),
               lauf("Medium allein n=32", n_wind=32, u=u32, baelle=[], falle=False, t_lam=(-1.0, -0.5), kontrolle=True),
               lauf("ploetzlich gehalten n=10", n_wind=10, u=k10 / math.sqrt(k10 * k10 + 1.1), t_lam=(-1.0, -0.5))]
    for r in laeufe:
        r["t_mess"] = (370.0, 570.0)
    skalieren(laeufe, f)
    stufen = stufen_rechnen("einschwingen", laeufe, 570.0 * f)
    erg = {}
    for s, st in stufen.items():
        t = st["t"]
        zz = []
        for b, r in enumerate(laeufe):
            z = dict(kraft_stat(st, r, b), name=r["name"], u=r["u"], kontrolle=r["kontrolle"])
            xr = entfalten_ort(reihe(st, b, "X"))
            m = maske(t, 100.0 * f, 300.0 * f)
            i3 = int(maske(t, 0.0, 300.0 * f).sum()) - 1
            z.update({"x_300": float(xr[i3] - xr[0]), "v_100_300": steigung(t[m], xr[m]), "a_100_300": beschl(t[m], xr[m]),
                      "C_spanne_max": float((reihe(st, b, "C_max") - reihe(st, b, "C_min")).max()),
                      "C_fern_drift": float((reihe(st, b, "C_fern") - reihe(st, b, "C_fern")[0]).abs().max())})
            zz.append(z)
        erg[s] = zz
    zz = ["einschwingen (Klaerung r5d kreuzen): C0 = 0,1, lam = 0,1, u = 0,48 / 0,76 / 1,46 c_s. 'ploetzlich' = r5d-Start "
          "(Ball ungekleidet, Stroemung und lam ab t = 0); 'adiabatisch' = lam [0, 100], Stroemung [120, 320]. r5d kreuzen "
          "n=5: x(300) = +1,273, v = 5,22e-3, a = 4,04e-6.",
          "  Lauf | x(300) | v, a auf [100, 300] | v, a auf [370, 570] | F_med spaet | F_Falle | C-Spanne max (Medium allein)"]
    for s in erg:
        zz.append(f"  [{s}]")
        for z in erg[s]:
            zz.append(f"  {z['name']:26s} | {z['x_300']:+.4f} | {fmt(z['v_100_300'])}, {fmt(z['a_100_300'])} | "
                      f"{fmt(z['v'])}, {fmt(z['a'])} | {fmt(z['F'])} | {fmt(z['F_fal'])} | {fmt(z['C_spanne_max'])}")
    l3_liste = [{"lauf": g["name"], "v_spaet": l3(g["v"], fz["v"]), "a_spaet": l3(g["a"], fz["a"])}
                for g, fz in paare(erg) if not g["kontrolle"]]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste}, zz + [l3_zeile(l3_liste), zeit_zeile(stufen)]


# ================================================================ Wellen 11: fahrtwind (Lorentz-Codeprobe)

def test_fahrtwind(f):
    laeufe = []
    for u in (0.05, 0.35, 0.60):
        laeufe += [stroemung(lauf(f"A ruhend, Stroemung u={u:.2f}"), u),
                   lauf(f"B bewegt v={-u:.2f}, Medium ruht", v_falle=-u),
                   stroemung(lauf(f"C Galilei K=w0 u, u={u:.2f}"), u, "galilei")]
    laeufe.append(stroemung(lauf("Spiegel A u=-0.35", kontrolle=True), -0.35))
    for r in laeufe:
        r["t_mess"] = (420.0, 620.0)
    skalieren(laeufe, f)
    stufen = stufen_rechnen("fahrtwind", laeufe, 620.0 * f)
    erg = {}
    for s, st in stufen.items():
        zz = []
        for b, r in enumerate(laeufe):
            z = dict(kraft_stat(st, r, b), name=r["name"], u=r["u"], kontrolle=r["kontrolle"])
            z["u_strom"] = u_gitter(r["K"], r["C0"], st["dx"]) if r["K"] != 0.0 else 0.0
            zz.append(z)
        for j in range(3):
            a_, b_, c_ = zz[3 * j], zz[3 * j + 1], zz[3 * j + 2]
            a_["B_minus_A"] = b_["F"] - a_["F"]
            a_["C_minus_A"] = c_["F"] - a_["F"]
        erg[s] = zz
    zz = ["fahrtwind (Wellen 11): A Ball ruht in Falle, Medium adiabatisch auf u (Lorentz: K = gamma w0 u, C = C0); "
          "B Medium ruht, Falle zieht den Ball glatt auf -u (Falle kontrahiert); C wie A, aber Galilei-Impuls K = w0 u "
          "(Stroemung dann u/sqrt(1 + u^2)). Erwartung F_A = F_B (Lorentz-Invarianz der Laengskraft).",
          "  Lauf | Stroemung im Ballsystem | F_med (1./2. Haelfte) | F_Falle | v Ball | F_B - F_A | F_C - F_A"]
    for s in erg:
        zz.append(f"  [{s}]")
        for z in erg[s]:
            zz.append(f"  {z['name']:30s} | {z['u_strom']:+.4f} | {fmt(z['F'])} ({fmt(z['F_h1'])}, {fmt(z['F_h2'])}) | "
                      f"{fmt(z['F_fal'])} | {fmt(z['v'])} | {fmt(z.get('B_minus_A', float('nan')))} | "
                      f"{fmt(z.get('C_minus_A', float('nan')))}")
    l3_liste = []
    for g, fz in paare(erg):
        if "B_minus_A" in g:
            l3_liste.append({"lauf": g["name"], "F_A": l3(g["F"], fz["F"])})
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste}, zz + [l3_zeile(l3_liste), zeit_zeile(stufen)]


# ================================================================ Wellen 7: windschatten

WS_D = (6.0, 10.0, 16.0, 24.0)
WS_U = (0.0, 0.05, 0.35)


def test_windschatten(f):
    laeufe = []
    for u in WS_U:
        for d in WS_D:
            laeufe.append(stroemung(lauf(f"d={d:g} u={u:.2f}", baelle=[(-0.5 * d, W2), (0.5 * d, W2)]), u))
            laeufe[-1]["d"] = d
        laeufe.append(stroemung(lauf(f"allein u={u:.2f}"), u))
        laeufe[-1]["d"] = 0.0
    for r in laeufe:
        r["t_mess"] = (r["t_strom"][1] + RUHE, 570.0)
    skalieren(laeufe, f)
    stufen = stufen_rechnen("windschatten", laeufe, 570.0 * f)
    erg = {}
    for s, st in stufen.items():
        zz = []
        for b, r in enumerate(laeufe):
            z = {"name": r["name"], "u": r["u"], "d": r["d"]}
            z["F_vorn"] = kraft_stat(st, r, b, 0)["F"]
            z["F_hinten"] = kraft_stat(st, r, b, 1)["F"] if r["d"] > 0.0 else float("nan")
            z["F_fal_vorn"] = kraft_stat(st, r, b, 0)["F_fal"]
            zz.append(z)
        null = {z["d"]: z for z in zz if z["u"] == 0.0}
        allein = {z["u"]: z["F_vorn"] - null[0.0]["F_vorn"] for z in zz if z["d"] == 0.0}
        for z in zz:
            z["dF_vorn"] = z["F_vorn"] - null[z["d"]]["F_vorn"]
            z["dF_hinten"] = z["F_hinten"] - null[z["d"]]["F_hinten"] if z["d"] > 0.0 else float("nan")
            z["hinten_durch_allein"] = teilen(z["dF_hinten"], allein[z["u"]]) if z["d"] > 0.0 else float("nan")
            z["vorn_durch_allein"] = teilen(z["dF_vorn"], allein[z["u"]])
            kw = kielwelle(z["u"], 0.1) if z["u"] > 0.0 else float("nan")
            z["cos_kw_d"] = math.cos(kw * z["d"]) if math.isfinite(kw) else float("nan")
        erg[s] = zz
    zz = ["windschatten (Wellen 7): zwei Baelle in Fallen bei -d/2 (vorn, stromauf) und +d/2 (hinten), Stroemung +x. "
          "dF = F(u) - F(u = 0, gleiches d) (statische Anziehung abgezogen); Verhaeltnis zu dF des einzelnen Balls. "
          "cos(k_w d) mit der Bugwelle k_w des Ballsystems.",
          "  Lauf | F vorn, hinten | dF vorn, hinten | vorn/allein | hinten/allein | cos(k_w d)"]
    for s in erg:
        zz.append(f"  [{s}]")
        for z in erg[s]:
            zz.append(f"  {z['name']:16s} | {fmt(z['F_vorn'])}, {fmt(z['F_hinten'])} | {fmt(z['dF_vorn'])}, "
                      f"{fmt(z['dF_hinten'])} | {fmt(z['vorn_durch_allein'], '.3f')} | "
                      f"{fmt(z['hinten_durch_allein'], '.3f')} | {fmt(z['cos_kw_d'], '+.2f')}")
    l3_liste = [{"lauf": g["name"], "dF_vorn": l3(g["dF_vorn"], fz["dF_vorn"]), "dF_hinten": l3(g["dF_hinten"], fz["dF_hinten"])}
                for g, fz in paare(erg) if g["u"] == 0.35 and g["d"] > 0.0]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste}, zz + [l3_zeile(l3_liste), zeit_zeile(stufen)]


# ================================================================ Wellen 3: stokes

ST_K, ST_SIGMA, ST_T_EIN, ST_T = 0.42, 25.0, 150.0, 900.0


def paket_hook(x, dx, dt, laeufe):
    """Linearisierte Bogoliubov-Welle (Schallast, Wellenzahl k, Richtung +-x) mit Gauss-Huelle, relativ zum lokalen
    Medium eingesetzt: chi -> chi (1 + eta), chi_t -> chi_t (1 + eta) + chi eta_t; a = relative Dichteamplitude."""
    etas, etats = [], []
    for r in laeufe:
        p = r.get("paket")
        if not p:
            etas.append(torch.zeros_like(x, dtype=C128))
            etats.append(torch.zeros_like(x, dtype=C128))
            continue
        c0, k = r["C0"], p["k"]
        h0, g, w0 = math.sqrt(c0), 2.0 * r["g4"] * c0, om0(c0, r["mc2"], r["g4"])
        om = bogoliubov(k, c0, r["mc2"], r["g4"])
        rr = -(k * k + g - om * om - 2.0 * w0 * om) / g
        uu = p["a"] * h0 / (2.0 * (1.0 + rr))
        vv = rr * uu
        th = p["richtung"] * k * x
        huelle = torch.exp(-0.5 * (wrap(x - p["x"]) / p["sigma"]) ** 2)
        e1, e2 = torch.exp(1j * th), torch.exp(-1j * th)
        etas.append((uu * e1 + vv * e2) * huelle / h0)
        etats.append((-1j * om * uu * e1 + 1j * om * vv * e2) * huelle / h0)
    eta, etat = torch.stack(etas), torch.stack(etats)
    n_ein = int(round(laeufe[0]["paket_t"] / dt))

    def hook(psi, vpsi, chi, vchi):
        return psi, vpsi, chi * (1.0 + eta), vchi * (1.0 + eta) + chi * etat
    return (n_ein, hook)


def test_stokes(f):
    def pk(a, xp=-130.0, richtung=1.0):
        return {"a": a, "k": ST_K, "x": xp, "sigma": ST_SIGMA, "richtung": richtung, "t": ST_T_EIN}
    laeufe = [lauf(f"a={a}", falle=False, paket=pk(a)) for a in (0.05, 0.1, 0.2)]
    laeufe += [lauf("ohne Welle", falle=False, kontrolle=True),
               lauf("Spiegel a=0.2 von rechts", falle=False, paket=pk(0.2, 130.0, -1.0), kontrolle=True),
               lauf("lam=0 a=0.2", falle=False, lam=0.0, paket=pk(0.2), kontrolle=True),
               lauf("Medium allein a=0.2", falle=False, baelle=[], paket=pk(0.2), kontrolle=True),
               lauf("Welle auf dem Ball a=0.1", falle=False, paket=pk(0.1, 0.0)),
               lauf("Welle auf dem Ball a=0.2", falle=False, paket=pk(0.2, 0.0))]
    for r in laeufe:
        r["paket_t"] = ST_T_EIN
    skalieren(laeufe, f)
    for r in laeufe:
        r["paket_t"] = ST_T_EIN * f
    om = bogoliubov(ST_K, 0.1)
    vg = (bogoliubov(ST_K + 1e-4, 0.1) - bogoliubov(ST_K - 1e-4, 0.1)) / 2e-4
    stufen = stufen_rechnen("stokes", laeufe, ST_T * f, hook_bauen=paket_hook)
    erg = {}
    for s, st in stufen.items():
        t = st["t"]
        zz = []
        t_durch = (ST_T_EIN + (130.0 + 3.0 * ST_SIGMA) / vg) * f
        for b, r in enumerate(laeufe):
            xr = entfalten_ort(reihe(st, b, "X"))
            m_end = maske(t, t[-1] - 150.0 * f, t[-1])
            i_ein = int(maske(t, 0.0, ST_T_EIN * f).sum()) - 1
            i_d = min(int(maske(t, 0.0, t_durch).sum()) - 1, len(t) - 1)
            zz.append({"name": r["name"], "a": (r["paket"] or {}).get("a", 0.0), "kontrolle": r["kontrolle"],
                       "x_ende": float(xr[-1] - xr[i_ein]), "x_durchgang": float(xr[i_d] - xr[i_ein]),
                       "v_ende": steigung(t[m_end], xr[m_end]),
                       "x_schwing": float((xr[i_ein:] - xr[i_ein]).abs().max()),
                       "C_max_ende": float(reihe(st, b, "C_max")[-1]), "C_min_ende": float(reihe(st, b, "C_min")[-1])})
        haupt = [z for z in zz if z["name"].startswith("a=")]
        for key in ("v_ende", "x_durchgang"):
            w = [abs(z[key]) for z in haupt]
            expo = math.log(teilen(w[2], w[0])) / math.log(4.0) if w[0] > 0.0 and w[2] > 0.0 else float("nan")
            for z in zz:
                z["exponent_" + key] = expo
        erg[s] = zz
    zz = [f"stokes (Wellen 3): freier Ball (gekleidet, lam = 0,1, C0 = 0,1); Schallpaket k = {ST_K}, Om = {om:.4f} "
          f"(Periode {2 * PI / om:.1f}), v_g = {vg:.3f}, sigma = {ST_SIGMA}, eingesetzt bei t = {ST_T_EIN} in x = -130 "
          "(130 vom Ball). Exponent: log(Groesse(a=0,2)/Groesse(a=0,05))/log 4.",
          "  Lauf | x nach Durchgang | x Ende | v Ende | groesste Auslenkung | Exponent v, x | C min .. max Ende"]
    for s in erg:
        zz.append(f"  [{s}]")
        for z in erg[s]:
            zz.append(f"  {z['name']:26s} | {z['x_durchgang']:+.3e} | {z['x_ende']:+.3e} | {fmt(z['v_ende'])} | "
                      f"{z['x_schwing']:.3e} | {fmt(z['exponent_v_ende'], '.2f')}, {fmt(z['exponent_x_durchgang'], '.2f')} | "
                      f"{z['C_min_ende']:.5f} .. {z['C_max_ende']:.5f}")
    l3_liste = [{"lauf": g["name"], "v_ende": l3(g["v_ende"], fz["v_ende"]), "x_durchgang": l3(g["x_durchgang"], fz["x_durchgang"])}
                for g, fz in paare(erg) if not g["kontrolle"]]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste}, zz + [l3_zeile(l3_liste), zeit_zeile(stufen)]


# ================================================================ Bio 2 osmose und Chemie 9 massenwirkung (Austausch eps)

OS_MC2, OS_EPS, OS_T, OS_FENSTER = 0.5, 0.01, 800.0, (300.0, 800.0)   # mu_Medium^2 = 0,5 + C bleibt < 0,9


def winkel_wrap(a):
    return torch.remainder(a + PI, 2.0 * PI) - PI


def frequenz(t, arg):
    """omega aus der Phasenreihe (Feld ~ exp(-i omega t)): minus Steigung der entfalteten Phase."""
    th = torch.cat([arg[:1], arg[:1] + torch.cumsum(winkel_wrap(arg[1:] - arg[:-1]), 0)])
    return -steigung(t, th)


def austausch_stat(st, r, b, ball, f):
    """Netto-Ladungsrate in das Ballfenster (Hintergrund des Mediums abgezogen), Ball- und Mediumfrequenz."""
    t = st["t"]
    m = maske(t, OS_FENSTER[0] * f, OS_FENSTER[1] * f)
    dq = reihe(st, b, "Q_tot", ball) - (reihe(st, b, "rho_fern") * 2.0 * FENSTER if r["C0"] > 0.0 else 0.0)
    w_b = frequenz(t[m], reihe(st, b, "arg_psi", ball)[m])
    w_0 = frequenz(t[m], reihe(st, b, "arg_chi_fern")[m]) if r["C0"] > 0.0 else float("nan")
    return {"rate": steigung(t[m], dq[m]), "rate_psi": steigung(t[m], reihe(st, b, "Q_psi", ball)[m]),
            "dQ_gesamt": float(dq[m][-1] - dq[0]), "omega_ball": w_b, "omega_medium": w_0,
            "Q_summe_rel": teilen(float((reihe(st, b, "Q_psi_alle") + reihe(st, b, "Q_chi_alle"))[-1]
                                        - (reihe(st, b, "Q_psi_alle") + reihe(st, b, "Q_chi_alle"))[0]),
                                  float((reihe(st, b, "Q_psi_alle") + reihe(st, b, "Q_chi_alle"))[0]))}


def test_osmose(f):
    kw = dict(mc2=OS_MC2, lam=0.0, falle=False)
    laeufe = [lauf(f"C={c:.2f} eps={OS_EPS}", C0=c, eps=OS_EPS, **kw) for c in (0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35)]
    laeufe += [lauf(f"C={c:.2f} eps=0.02", C0=c, eps=0.02, **kw) for c in (0.10, 0.30)]
    laeufe += [lauf("C=0.30 eps=0", C0=0.3, eps=0.0, kontrolle=True, **kw),
               lauf("Medium allein C=0.30", C0=0.3, eps=OS_EPS, baelle=[], kontrolle=True, **kw)]
    skalieren(laeufe, f)
    stufen = stufen_rechnen("osmose", laeufe, OS_T * f)
    k_vak = math.sqrt(W2 - OS_MC2)
    gamma_vak = OS_EPS ** 2 * ft_profil(k_vak, W2) ** 2 / k_vak
    erg = {}
    for s, st in stufen.items():
        zz = []
        for b, r in enumerate(laeufe):
            z = dict(austausch_stat(st, r, b, 0, f), name=r["name"], C0=r["C0"], eps=r["eps"], kontrolle=r["kontrolle"])
            z["C_iso_naiv"] = W2 - OS_MC2
            zz.append(z)
        haupt = sorted((z for z in zz if z["eps"] == OS_EPS and z["C0"] > 0.0 and not z["kontrolle"]), key=lambda z: z["C0"])
        iso = float("nan")
        for z1, z2 in zip(haupt[:-1], haupt[1:]):
            if z1["rate"] * z2["rate"] < 0.0:
                iso = z1["C0"] + (z2["C0"] - z1["C0"]) * z1["rate"] / (z1["rate"] - z2["rate"])
                break
        for z in zz:
            z["C_iso_gemessen"] = iso
        erg[s] = zz
    zz = [f"osmose (Bio 2): Medium mc2 = {OS_MC2} (mu = sqrt(0,5 + C)), Ball omega^2 = {W2}, lam = 0, Austausch eps. Rate = "
          f"d(Ladung im Ballfenster - Hintergrund)/dt auf {OS_FENSTER}. Isoton naiv C = {W2 - OS_MC2:.2f}. Vakuum-Formel "
          f"(C = 0): Rate = -eps^2 ft(k)^2/k = {-gamma_vak:.3e} (k = {k_vak:.3f}).",
          "  Lauf | Rate (nur psi) | dQ gesamt | omega Ball | omega Medium | mu-Differenz | Q_psi+Q_chi rel."]
    for s in erg:
        zz.append(f"  [{s}]")
        for z in erg[s]:
            zz.append(f"  {z['name']:22s} | {fmt(z['rate'])} ({fmt(z['rate_psi'])}) | {z['dQ_gesamt']:+.3e} | "
                      f"{z['omega_ball']:.5f} | {fmt(z['omega_medium'], '.5f')} | "
                      f"{fmt(z['omega_medium'] - z['omega_ball'], '+.4f')} | {fmt(z['Q_summe_rel'])}")
        zz.append(f"  Vorzeichenwechsel der Rate (isoton) bei C = {fmt(erg[s][0]['C_iso_gemessen'], '.3f')}")
    l3_liste = [{"lauf": g["name"], "rate": l3(g["rate"], fz["rate"])}
                for g, fz in paare(erg) if not g["kontrolle"]]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste, "gamma_vakuum": gamma_vak}, \
        zz + [l3_zeile(l3_liste), zeit_zeile(stufen)]


MW_BAELLE = [(-100.0, 0.6), (0.0, 0.7), (100.0, 0.8)]


def test_massenwirkung(f):
    kw = dict(mc2=OS_MC2, lam=0.0, falle=False, baelle=MW_BAELLE)
    laeufe = [lauf(f"C={c:.1f}", C0=c, eps=OS_EPS, **kw) for c in (0.1, 0.2, 0.3)]
    laeufe += [lauf("C=0.2 eps=0", C0=0.2, eps=0.0, kontrolle=True, **kw),
               lauf("C=0 Vakuum", C0=0.0, eps=OS_EPS, kontrolle=True, **kw)]
    skalieren(laeufe, f)
    stufen = stufen_rechnen("massenwirkung", laeufe, OS_T * f)
    erg = {}
    for s, st in stufen.items():
        zz = []
        for b, r in enumerate(laeufe):
            for i, (_, w2) in enumerate(r["baelle"]):
                z = dict(austausch_stat(st, r, b, i, f), name=f"{r['name']} Ball omega^2={w2}", C0=r["C0"],
                         kontrolle=r["kontrolle"], w2=w2)
                dmu = z["omega_medium"] - z["omega_ball"]
                z["vorzeichen_passt"] = (bool(dmu * z["rate"] > 0.0) if math.isfinite(dmu) and abs(dmu) > 0.01
                                         else None)
                zz.append(z)
        erg[s] = zz
    zz = [f"massenwirkung (Chemie 9): drei Baelle omega^2 = 0,6 / 0,7 / 0,8 bei -100 / 0 / 100 im Medium mc2 = {OS_MC2}, "
          f"eps = {OS_EPS}, lam = 0; mu_Medium^2 = 0,5 + C. Vorhersage: Vorzeichen der Rate = Vorzeichen von mu - omega.",
          "  Ball | Rate | dQ gesamt | omega Ball | mu Medium | mu - omega | Vorzeichen passt"]
    for s in erg:
        zz.append(f"  [{s}]")
        for z in erg[s]:
            zz.append(f"  {z['name']:34s} | {fmt(z['rate'])} | {z['dQ_gesamt']:+.3e} | {z['omega_ball']:.5f} | "
                      f"{fmt(z['omega_medium'], '.5f')} | {fmt(z['omega_medium'] - z['omega_ball'], '+.4f')} | "
                      f"{z['vorzeichen_passt']}")
        treffer = [z["vorzeichen_passt"] for z in erg[s] if z["vorzeichen_passt"] is not None and not z["kontrolle"]]
        zz.append(f"  Vorzeichen passt: {sum(treffer)} von {len(treffer)} (|mu - omega| > 0,01)")
    l3_liste = [{"lauf": g["name"], "rate": l3(g["rate"], fz["rate"])}
                for g, fz in paare(erg) if not g["kontrolle"]]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste}, zz + [l3_zeile(l3_liste), zeit_zeile(stufen)]


# ================================================================ Bio 21: nische

NI_T, NI_FREI = 1300.0, (200.0, 250.0)


def extrema(t, xr, glatt_n=10):
    """Umkehrpunkte: Vorzeichenwechsel der geglaetteten Geschwindigkeit."""
    v = (xr[2 * glatt_n:] - xr[:-2 * glatt_n])
    tv = t[glatt_n:-glatt_n]
    i = torch.nonzero(v[1:] * v[:-1] < 0.0).flatten()
    return [(float(tv[j]), float(xr[j + glatt_n])) for j in i.tolist()]


def test_nische(f):
    kw = dict(C0=0.15, t_frei=NI_FREI)
    laeufe = [lauf("lam=+0.1 sanft (dC 0,02, 30)", lam=0.1, W_dC=0.02, W_lam=30.0, **kw),
              lauf("lam=-0.1 sanft", lam=-0.1, W_dC=0.02, W_lam=30.0, **kw),
              lauf("lam=+0.2 steil (dC 0,05, 60)", lam=0.2, W_dC=0.05, W_lam=60.0, **kw),
              lauf("lam=0", lam=0.0, W_dC=0.02, W_lam=30.0, kontrolle=True, **kw),
              lauf("Spiegel lam=+0.1", lam=0.1, W_dC=-0.02, W_lam=30.0, kontrolle=True, **kw),
              lauf("Medium allein", lam=0.1, W_dC=0.02, W_lam=30.0, baelle=[], falle=False, kontrolle=True, **kw)]
    skalieren(laeufe, f)
    stufen = stufen_rechnen("nische", laeufe, NI_T * f)
    q, e = anker_q_e(W2)
    n_ball = q / (2.0 * math.sqrt(W2))
    erg = {}
    for s, st in stufen.items():
        t = st["t"]
        zz = []
        for b, r in enumerate(laeufe):
            xr = entfalten_ort(reihe(st, b, "X"))
            m = maske(t, NI_FREI[1] * f, t[-1])
            tt, xx = t[m], xr[m]
            ext = extrema(tt, xx) if xx.numel() > 30 else []
            kn = 2.0 * PI / r["W_lam"]
            om2 = abs(r["lam"]) * n_ball * abs(r["W_dC"]) * kn * kn / e
            z = {"name": r["name"], "lam": r["lam"], "kontrolle": r["kontrolle"], "x_frei": float(xx[0]) if xx.numel() else 0.0,
                 "x_min": float(xx.min()), "x_max": float(xx.max()), "x_ende": float(xx[-1]),
                 "umkehr": ext[:4], "T_harmonisch": 2.0 * PI / math.sqrt(om2) if om2 > 0.0 else float("nan"),
                 "C_spanne": float(reihe(st, b, "C_max")[-1] - reihe(st, b, "C_min")[-1])}
            z["halbperiode"] = ext[1][0] - ext[0][0] if len(ext) >= 2 else float("nan")
            z["amplitude_verhaeltnis"] = (teilen(abs(ext[1][1] - ext[0][1]), abs(ext[0][1] - z["x_frei"]))
                                          if len(ext) >= 2 else float("nan"))
            zz.append(z)
        erg[s] = zz
    zz = ["nische (Bio 21): Medium C = 0,15 + dC sin(2 pi x/lambda) (aeusseres W, glatt eingeschaltet), Ball in Falle bei "
          f"x = 0 (Nulldurchgang), Falle geloest auf {NI_FREI}. Delle bei -lambda/4, Buckel bei +lambda/4. T_harmonisch = "
          "2 pi/sqrt(|lam| N dC k^2/E); Pendel mit 90 Grad Ausschlag: x 1,18.",
          "  Lauf | x frei | x min .. max | x Ende | Umkehrpunkte (t, x) | Halbperiode | Amplitudenverh. | T_harm."]
    for s in erg:
        zz.append(f"  [{s}]")
        for z in erg[s]:
            uk = ", ".join(f"({a:.0f}, {b:+.2f})" for a, b in z["umkehr"])
            zz.append(f"  {z['name']:28s} | {z['x_frei']:+.3f} | {z['x_min']:+.3f} .. {z['x_max']:+.3f} | {z['x_ende']:+.3f} | "
                      f"{uk} | {fmt(z['halbperiode'], '.1f')} | {fmt(z['amplitude_verhaeltnis'], '.3f')} | "
                      f"{fmt(z['T_harmonisch'], '.0f')}")
    l3_liste = [{"lauf": g["name"], "x_min": l3(g["x_min"], fz["x_min"]), "x_max": l3(g["x_max"], fz["x_max"])}
                for g, fz in paare(erg) if not g["kontrolle"]]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste}, zz + [l3_zeile(l3_liste), zeit_zeile(stufen)]


# ================================================================ Hauptprogramm

TESTS = {"landau": test_landau, "gleiten": test_gleiten, "einschwingen": test_einschwingen,
         "windschatten": test_windschatten, "fahrtwind": test_fahrtwind, "stokes": test_stokes,
         "osmose": test_osmose, "massenwirkung": test_massenwirkung, "nische": test_nische}


def schreiben(name, ausgabe, text):
    basis = os.path.join(OUT, f"medium1d_{name}")
    with open(basis + "_bericht.txt", "w") as fh:
        fh.write("\n".join(text) + "\n")
    with open(basis + "_ergebnis.json", "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)


def main():
    global DEV, OUT, STUFEN
    ap = argparse.ArgumentParser(description="Runde 6, M1: Medium-Karten in 1D")
    ap.add_argument("unterbefehl", choices=["rauch"] + list(TESTS))
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None)
    ap.add_argument("--faktor", type=float, default=None, help="Zeitfaktor (Vorgabe 1, rauch 0,05)")
    ap.add_argument("--stufen", choices=["beide", "grob", "fein"], default="beide",
                    help="einzelne Stufe (Rauchtest oder Aufteilen eines langen Aufrufs); L3 dann ueber zwei Berichte")
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber keine CUDA-Karte sichtbar: Abbruch (kein stiller CPU-Ausweg).")
        DEV = torch.device("cuda")
        torch.cuda.set_per_process_memory_fraction(
            min(1.0, SPEICHER_GB * 2 ** 30 / torch.cuda.get_device_properties(0).total_memory))
        name_geraet = torch.cuda.get_device_name(0)
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(1)
        name_geraet = "CPU, 1 Thread"
    STUFEN = {"grob": ("grob",), "fein": ("fein",)}.get(args.stufen, ("grob", "fein"))
    OUT = args.out or os.path.join(os.getcwd(), "ausgabe-" + args.unterbefehl)
    os.makedirs(OUT, exist_ok=True)
    rauch = args.unterbefehl == "rauch"
    faktor = args.faktor if args.faktor is not None else (RAUCH_FAKTOR if rauch else 1.0)
    auswahl = list(TESTS) if rauch else [args.unterbefehl]
    t_start = time.perf_counter()
    kopf = (f"Runde 6 M1 medium1d.py {args.unterbefehl} Start {jetzt()} auf {name_geraet}, torch {torch.__version__}, "
            f"Zeitfaktor {faktor}, Stufen {'/'.join(STUFEN)}")
    print(kopf, flush=True)
    ausgabe = {"start": jetzt(), "geraet": name_geraet, "faktor": faktor, "ergebnisse": {}, "fehler": {}}
    text = [kopf, ""]
    for name in auswahl:
        try:
            res, zeilen = TESTS[name](faktor)
            ausgabe["ergebnisse"][name] = res
            text += zeilen + [""]
        except Exception:
            ausgabe["fehler"][name] = traceback.format_exc()
            text += [f"{name} FEHLER:", ausgabe["fehler"][name], ""]
            print(ausgabe["fehler"][name], flush=True)
        schreiben(args.unterbefehl, ausgabe, text)
    ausgabe["ende"] = jetzt()
    ausgabe["dauer_s"] = time.perf_counter() - t_start
    speicher = torch.cuda.max_memory_allocated() / 2 ** 20 if DEV.type == "cuda" else float("nan")
    text.append(f"Ende {ausgabe['ende']}, Dauer {ausgabe['dauer_s']:.1f} s, Torch-Speicher max {speicher:.0f} MB, "
                f"Fehler in: {sorted(ausgabe['fehler']) if ausgabe['fehler'] else 'keine'}")
    schreiben(args.unterbefehl, ausgabe, text)
    print("\n".join(text), flush=True)
    if ausgabe["fehler"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
