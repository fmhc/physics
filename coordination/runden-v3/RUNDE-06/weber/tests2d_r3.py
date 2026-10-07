#!/usr/bin/env python3
"""Runde 3 (v3), 2D-Tests: Tropfenschwingung (Wellen 16) und Brechung (Wellen 14), dazu eine Profilkontrolle m = 0, 1.
Magnus/Flettner (Wellen 8/9) ist im Ein-Feld-Modell nicht umsetzbar (kein stabiler duenner Hintergrund, PLAN.md).

Explorativ. Ohne Testlauf abgegeben (auf dem Laptop gilt das Interpreterverbot). Plan, Aufrufe und Vorhersagen stehen
in PLAN.md daneben. Nur CUDA, float64 bzw. complex128; ohne CUDA bricht das Programm ab.

Modell (Atlas-Normierung wie RUNDE-01/qg1/qg1.py, hier d = 2):
    L = |psi_t|^2 - |grad psi|^2 - U(S) - V(x) S,   S = |psi|^2,   U(S) = S - S^2 + S^3/2.
    Bewegungsgleichung: psi_tt = Lap psi - (U'(S) + V) psi,  U'(S) = 1 - 2 S + 1,5 S^2.
    V = 0 ausser in Test 3 (Stufe im Potential, ortsabhaengiger Koeffizient; kein Hintergrund).
    Ladungsdichte rho = 2 Im(psi conj(psi_t)),
    Energiedichte |psi_t|^2 + |grad psi|^2 + U(S) + V S.
Q-Ball: psi = f(r) exp(i m theta - i omega t), m = 0 oder +-1, radial geschossen:
    f'' + f'/r - m^2 f / r^2 = (U'(f^2) - omega^2) f.
Numerik:
    - Schiessen: RK4 mit h = 0,01 wie qg1.py; Einschachteln mit 2048 Kandidaten in 5 Runden, alle Profile zugleich.
      Start bei r = h aus der Reihe um r = 0; Schwanz ab f < 1e-3 f_max asymptotisch K_m(kappa0 r).
    - Zeitentwicklung: Velocity-Verlet wie qg1.py. Laplace spektral (FFT, periodische Box) statt finiter Differenzen:
      exakt isotrop (keine Gitteranisotropie, die die Formmoden l = 2, 3 verfaelscht) und spektral genau.
      Randschicht: nach jedem Schritt psi_t -> psi_t exp(-sigma dt) (Vakuum aussen).
    - Zwei Aufloesungen: grob dx = 0,3, dt = 0,05; fein dx = 0,2, dt = 0,025 (Latte L3).

Aufruf:  python tests2d_r3.py {profile|tropfen|brechung|alle} [--rauch] [--nur-grob] [--omega2 W] [--out ORDNER]
         --omega2 W: Test 1 nur fuer omega^2 = W (0.52 oder 0.55), falls die Hochrechnung ueber 9 min liegt.
Rauchtest: --rauch (Laufzeiten x 0,05; Zahlen dann ungueltig, nur Durchlauf und Hochrechnung).
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
C128 = torch.complex128

# ---- Feste Parameter (vor dem Lauf in PLAN.md festgehalten) ----
H_ODE = 0.01             # Schrittweite beim Schiessen, wie qg1.py
X_ODE = 60.0             # Schiesslaenge
N_KAND, RUNDEN = 2048, 5 # Kandidaten je Einschachtelungsrunde, Zahl der Runden (2048^5 > 1e16)
SCHWANZ = 1e-3           # ab f < SCHWANZ * f_max (im Abfall): asymptotischer Schwanz
T_MEAS = 1.0             # Messabstand
SPONGE, SIGMA0 = 8.0, 1.0  # Breite und Staerke der Randschicht
STUFEN = (("grob", 0.3, 0.05), ("fein", 0.2, 0.025))
RAUCH_FAKTOR = 0.05

# Test 1 (Wellen 16): Tropfenschwingung
T1_OMEGA2 = (0.52, 0.55)
T1_L = {0.52: 48.0, 0.55: 36.0}        # halbe Boxlaenge
T1_T = {0.52: 1000.0, 0.55: 400.0}     # Laufzeit (etwa 3 bzw. 5 Perioden l = 2 nach Vorhersage)
T1_DR, T1_DR_GROSS = 0.25, 0.5         # Randauslenkung delta R (Hauptwert, Linearitaetsprobe)
T1_LAEUFE = {"grob": (("l2", 2, T1_DR), ("l3", 3, T1_DR), ("l2gross", 2, T1_DR_GROSS), ("ruhe", 0, 0.0)),
             "fein": (("l2", 2, T1_DR), ("l3", 3, T1_DR))}

# Test 2 (Wellen 8/9, Magnus/Flettner) entfaellt: im Ein-Feld-Modell nicht umsetzbar (PLAN.md Abschnitt 3).
# Statt dessen Profilkontrolle m = 0 und m = 1 (nur Schiessen, keine Zeitentwicklung):
PR_OMEGA2 = (0.52, 0.55, 0.60, 0.70, 0.80)

# Test 3 (Wellen 14): Brechung an einer Mittelfeldstufe V(x) = V2 (1 + tanh(x/B))/2
T3_OMEGA2 = 0.70
T3_L, T3_T = 42.0, 280.0
T3_V, T3_X0, T3_BREITE = 0.2, -16.0, 1.0   # Einfallsgeschwindigkeit, Startabstand, Stufenbreite
T3_XFIT = 8.0                               # Bahnfit nur mit |X| >= 8 (Ball ganz in einem Medium)
T3_FAMILIE = tuple(round(0.64 + 0.002 * j, 6) for j in range(61))   # 0,64 ... 0,76; enthaelt 0,70
T3_LAEUFE = {"grob": (("anz20", -0.02, 20.0), ("anz40", -0.02, 40.0), ("anz60", -0.02, 60.0),
                      ("anz0", -0.02, 0.0), ("abst20", 0.02, 20.0), ("abst45", 0.02, 45.0), ("ohne40", 0.0, 40.0)),
             "fein": (("anz20", -0.02, 20.0), ("anz40", -0.02, 40.0), ("anz60", -0.02, 60.0))}


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    torch.cuda.synchronize()
    return time.perf_counter()


def upot(s):
    return s - s * s + 0.5 * s ** 3


# ---------------------------------------------------------------- Profil durch Schiessen

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


def startwerte(p, a0, ist_m0, h):
    """Zustand bei r = h aus der Reihe um r = 0.
    m = 0: f = p + g r^2/4 mit g = (U'(p^2) - omega^2) p.  |m| = 1: f = p r + (a0 p/8) r^3 (p = f'(0))."""
    s = p * p
    g = (a0 - 2.0 * s + 1.5 * s * s) * p
    d = a0 * p / 8.0
    f = torch.where(ist_m0, p + 0.25 * g * h * h, p * h + d * h ** 3)
    fp = torch.where(ist_m0, 0.5 * g * h, p + 3.0 * d * h * h)
    return f, fp


def schiessen(w2_liste, m_liste):
    """Schiessparameter p je Zeile (m = 0: f(0); |m| = 1: f'(0)) durch Einschachteln, alle Zeilen zugleich.

    Obergrenze f_top = sqrt(S_oben) ist die Kuppe, bei der das Profil verweilt; f_tal = sqrt(S_unten) ist die Talsohle.
    m = 0: Ueberschuss = f < 0 (oder f > f_top); Unterschuss = f' > 0 jenseits der Talsohle (f < f_tal), also Umkehr
    vor null. (Ohne die Talbedingung koennte ein Kandidat genau auf der Kuppe durch Rundung als Unterschuss zaehlen.)
    |m| = 1: Ueberschuss = f > f_top (laeuft ueber die Kuppe); Unterschuss = f' < 0 (faellt vor der Kuppe zurueck).
    Unentschiedene Kandidaten veraendern die Klammer nicht."""
    w2 = torch.tensor(w2_liste, dtype=F64, device=DEV).unsqueeze(1)
    m2 = torch.tensor([float(m * m) for m in m_liste], dtype=F64, device=DEV).unsqueeze(1)
    ist_m0 = m2 == 0.0
    a0 = 1.0 - w2
    f_top = torch.sqrt((2.0 + torch.sqrt(6.0 * w2 - 2.0)) / 3.0)
    f_tal = torch.sqrt((2.0 - torch.sqrt(6.0 * w2 - 2.0)) / 3.0)
    lo = torch.where(ist_m0, torch.full_like(w2, 1e-3), torch.full_like(w2, 1e-4))
    hi = torch.where(ist_m0, f_top, torch.full_like(w2, 10.0))
    stufen = torch.linspace(0.0, 1.0, N_KAND, dtype=F64, device=DEV)
    n_schritte = int(round(X_ODE / H_ODE))
    for _ in range(RUNDEN):
        p = lo + (hi - lo) * stufen
        f, fp = startwerte(p, a0, ist_m0, H_ODE)
        zustand = torch.zeros_like(p)                     # 0 offen, +1 Ueberschuss, -1 Unterschuss
        for s in range(n_schritte):
            f, fp = rk4(H_ODE * (s + 1), f, fp, a0, m2, H_ODE)
            offen = zustand == 0.0
            ueber = offen & ((f > f_top) | (f < 0.0))
            unter = offen & ~ueber & torch.where(ist_m0, (fp > 0.0) & (f < f_tal), fp < 0.0)
            zustand = zustand + ueber.to(F64) - unter.to(F64)
            lebt = (zustand == 0.0).to(F64)
            f = f * lebt
            fp = fp * lebt
            if s % 250 == 249 and not bool((zustand == 0.0).any()):
                break
        lo = torch.where(zustand < 0.0, p, lo.expand_as(p)).max(dim=1, keepdim=True).values
        hi = torch.where(zustand > 0.0, p, hi.expand_as(p)).min(dim=1, keepdim=True).values
    return {"p": 0.5 * (lo + hi), "klammer": hi - lo, "w2": w2, "m2": m2, "ist_m0": ist_m0, "a0": a0,
            "f_top": f_top, "m": list(m_liste), "w2_liste": list(w2_liste)}


def profile_bauen(sch, r_max, streng=True):
    """Schiessbahn mit dem gefundenen p, dann Tabellen f, f' auf r_j = j h bis r_max und Radialintegrale.
    streng: Abbruch, wenn eine Bahn den Separatrixweg vor dem Schwanz verlaesst; sonst Zeile als ungueltig markieren."""
    p, a0, m2, ist_m0, f_top = sch["p"], sch["a0"], sch["m2"], sch["ist_m0"], sch["f_top"]
    n_schritte = int(round(X_ODE / H_ODE))
    f, fp = startwerte(p, a0, ist_m0, H_ODE)
    f0 = torch.where(ist_m0, p, torch.zeros_like(p))
    fp0 = torch.where(ist_m0, torch.zeros_like(p), p)
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
    # Radialintegrale (Trapez = Summe, weil der Integrand an beiden Enden verschwindet)
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
            "f_top": f_top[i, 0].item(), "gueltig": bool(gueltig[i]),
        })
    return profile


def profil_info(pr):
    return {k: v for k, v in pr.items() if k not in ("f", "fp")}


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
    """Periodische Box [-L, L)^2; x_j = -L + j dx liegt spiegelsymmetrisch (x -> -x bildet das Gitter auf sich ab)."""

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
        self.innen = (tiefe < L - SPONGE).to(F64)
        self.dA = dx * dx


def ball_feld(g, pr, m=0, x0=0.0, y0=0.0, eps=0.0, l=0, v=0.0, winkel=0.0):
    """psi und psi_t eines Q-Balls psi = f(r) exp(i m theta - i omega t) bei (x0, y0), Form (1, n, n).

    eps, l: Formstoerung r -> r (1 - eps cos(l theta)), also Rand R (1 + eps cos(l theta)); nur ruhend, m = 0.
    v, winkel: Lorentz-Boost mit Geschwindigkeit v in Richtung winkel (nur m = 0)."""
    w = math.sqrt(pr["omega2"])
    X = g.x - x0
    Y = g.y - y0
    if v != 0.0:
        gam = 1.0 / math.sqrt(1.0 - v * v)
        ca, sa = math.cos(winkel), math.sin(winkel)
        xpar = X * ca + Y * sa
        xperp = -X * sa + Y * ca
        xs = gam * xpar                                   # Ruhesystem-Koordinate des Balls bei t = 0
        r = torch.sqrt(xs * xs + xperp * xperp)
        f, fp = hermite(pr, r)
        phase = torch.exp(1j * (w * gam * v) * xpar)
        radial = torch.where(r > 0.0, xs / r.clamp(min=1e-300), torch.zeros_like(r))
        return f * phase, (-gam * v * radial * fp - 1j * (w * gam) * f) * phase
    r = torch.sqrt(X * X + Y * Y)
    if eps != 0.0:
        theta = torch.atan2(Y.expand_as(r), X.expand_as(r))
        r = r * (1.0 - eps * torch.cos(l * theta))
    f, _ = hermite(pr, r)
    if m == 0:
        psi = f.to(C128)
    else:
        c = pr["fp"][0]                                   # f'(0) fuer |m| = 1
        f_r = torch.where(r > 0.0, f / r.clamp(min=1e-300), c)
        psi = f_r * (X + 1j * m * Y)
    return psi, -1j * w * psi


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


# ---------------------------------------------------------------- Auswertehilfen (auf CUDA)

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


def periodogramm(t, y, om_lo, om_hi, n=3000):
    """Kleinste Quadrate y = a + b tau + c cos(om t) + d sin(om t), om auf einem Raster in [om_lo, om_hi].
    Rueckgabe: bestes om (verfeinert), Amplitude, erklaerter Varianzanteil R2, drei tiefste Nebenminima."""
    tau = (t - t[0]) / (t[-1] - t[0])
    var = ((y - y.mean()) ** 2).sum()

    def rest(oms):
        """Normalgleichungen je Frequenz (4 Spalten, float64), gestapelt geloest."""
        arg = oms.view(-1, 1) * t.view(1, -1)
        a_mat = torch.stack([torch.ones_like(arg), tau.expand_as(arg), torch.cos(arg), torch.sin(arg)], dim=2)
        ata = torch.einsum("nmi,nmj->nij", a_mat, a_mat)
        atb = torch.einsum("nmi,m->ni", a_mat, y).unsqueeze(2)
        koef = torch.linalg.solve(ata, atb)
        return (((a_mat @ koef).squeeze(2) - y.view(1, -1)) ** 2).sum(1), koef

    oms = torch.linspace(om_lo, om_hi, n, dtype=F64, device=DEV)
    res, _ = rest(oms)
    i = int(torch.argmin(res))
    lok = ((res[1:-1] < res[:-2]) & (res[1:-1] < res[2:])).nonzero().flatten() + 1
    lok = lok[torch.argsort(res[lok])][:3]
    spitzen = [{"omega": oms[k].item(), "R2": (1.0 - res[k] / var).item()} for k in lok.tolist()]
    fein = torch.linspace(oms[max(i - 2, 0)].item(), oms[min(i + 2, n - 1)].item(), 801, dtype=F64, device=DEV)
    res_f, koef_f = rest(fein)
    k = int(torch.argmin(res_f))
    amp = torch.sqrt(koef_f[k, 2, 0] ** 2 + koef_f[k, 3, 0] ** 2)
    return {"omega": fein[k].item(), "amplitude": amp.item(), "R2": (1.0 - res_f[k] / var).item(),
            "spitzen": spitzen}


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
                      "ueber 540 s: nicht starten, Leitung entscheidet.")
    return zeilen


# ---------------------------------------------------------------- Test 1: Tropfenschwingung (Wellen 16)

def tropfen_vorhersage(pr):
    """2D-Rayleigh Omega_l^2 = (l^3 - l) sigma / (rho R^3) aus dem Profil, ohne freie Parameter.

    P1 (festgelegt): sigma = G/(pi R_Q) (2D-Virial: E - omega Q = G = pi sigma R), rho = w = 2 omega^2 S_c
       (Enthalpiedichte = Traegheit der Stroemung), R = R_Q = sqrt(N/(pi S_c)) (Aequimolarradius der Ladung).
    Vergleichswerte: P2 sigma = p_c R_Q (Laplace), P3 sigma = sqrt(2)/4 (ebene Wand), P4 rho = n_c = 2 omega S_c
    (Ladungsdichte), P5 rho = eps_c = omega^2 S_c + U(S_c) (Energiedichte), P6 = P1 mit Kompressibilitaet und
    Wandtraegheit."""
    w2 = pr["omega2"]
    w = math.sqrt(w2)
    sc = pr["S_zentrum"]
    r_q = math.sqrt(pr["N"] / (math.pi * sc))
    p_c = w2 * sc - (sc - sc * sc + 0.5 * sc ** 3)
    w_c = 2.0 * w2 * sc
    n_c = 2.0 * w * sc
    e_c = w2 * sc + (sc - sc * sc + 0.5 * sc ** 3)
    sig_g = pr["G"] / (math.pi * r_q)
    sig_l = p_c * r_q
    sig_0 = math.sqrt(2.0) / 4.0
    upp = 3.0 * sc - 2.0
    cs2 = sc * upp / (sc * upp + 2.0 * w2)
    aus = {"R_Q": r_q, "S_c": sc, "p_c": p_c, "w_c": w_c, "n_c": n_c, "eps_c": e_c, "sigma_G": sig_g,
           "sigma_L": sig_l, "sigma_0": sig_0, "c_s": math.sqrt(max(cs2, 0.0)), "l": {}}
    for l in (2, 3):
        fak = l ** 3 - l
        om = lambda sig, rho: math.sqrt(fak * sig / (rho * r_q ** 3))
        p1 = om(sig_g, w_c)
        q2 = (p1 * r_q) ** 2 / max(cs2, 1e-12)
        p6 = p1 * math.sqrt(max(1.0 - q2 / (2.0 * l * (l + 1)), 0.0) / (1.0 + sig_g * l / (w_c * r_q)))
        aus["l"][l] = {"P1": p1, "P2": om(sig_l, w_c), "P3": om(sig_0, w_c), "P4": om(sig_g, n_c),
                       "P5": om(sig_g, e_c), "P6": p6, "T_P1": 2.0 * math.pi / p1}
    return aus


def test_tropfen(out, rauch, nur_grob, nur_w2=None):
    omegas = T1_OMEGA2 if nur_w2 is None else tuple(w for w in T1_OMEGA2 if abs(w - nur_w2) < 1e-9)
    if not omegas:
        raise SystemExit(f"--omega2 {nur_w2}: nicht in {T1_OMEGA2}")
    start = jetzt()
    print(f"Test 1 Tropfen Start {start} auf {torch.cuda.get_device_name(0)}, torch {torch.__version__}", flush=True)
    dauer = {}
    t0 = uhr()
    sch = schiessen(list(omegas), [0] * len(omegas))
    profile = profile_bauen(sch, 1.5 * max(T1_L.values()) + 5.0)
    dauer["schiessen_s"] = uhr() - t0
    vorh = {w2: tropfen_vorhersage(pr) for w2, pr in zip(omegas, profile)}
    for w2 in omegas:
        v = vorh[w2]
        print(f"Vorhersage omega2 {w2}: R_Q {v['R_Q']:.3f}, S_c {v['S_c']:.5f}, sigma_G {v['sigma_G']:.4f}, "
              f"rho=w {v['w_c']:.4f}; P1 Omega_2 {v['l'][2]['P1']:.5f}, Omega_3 {v['l'][3]['P1']:.5f}", flush=True)
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN:
        if nur_grob and stufe == "fein":
            continue
        for w2, pr in zip(omegas, profile):
            g = Gitter(T1_L[w2], dx)
            laeufe = T1_LAEUFE[stufe]
            r_q = vorh[w2]["R_Q"]
            felder = [ball_feld(g, pr, eps=(dr / r_q), l=l) for _, l, dr in laeufe]
            psi = torch.cat([f[0] for f in felder]).contiguous()
            vel = torch.cat([f[1] for f in felder]).contiguous()
            B = psi.shape[0]
            zx = torch.zeros(B, dtype=F64, device=DEV)
            zy = torch.zeros(B, dtype=F64, device=DEV)
            r_win = torch.full((B,), r_q + 12.0, dtype=F64, device=DEV)

            def messen(psi, vel):
                nonlocal zx, zy
                s, rho, e, fen, X, Y = grundmessung(g, psi, vel, None, zx, zy, r_win)
                z = (g.x - X.view(-1, 1, 1)) + 1j * (g.y - Y.view(-1, 1, 1))
                ws = s * fen
                z2 = z * z
                z3 = z2 * z
                a2 = (ws * z2.abs()).sum((1, 2))
                a3 = (ws * z3.abs()).sum((1, 2))
                zeile = torch.stack([
                    X, Y, (rho * fen).sum((1, 2)) * g.dA, (e * fen).sum((1, 2)) * g.dA, rho.sum((1, 2)) * g.dA,
                    e.sum((1, 2)) * g.dA, s.amax((1, 2)),
                    torch.sqrt((ws * z.abs() ** 2).sum((1, 2)) / ws.sum((1, 2))),
                    (ws * z2.real).sum((1, 2)) / a2, (ws * z2.imag).sum((1, 2)) / a2,
                    (ws * z3.real).sum((1, 2)) / a3, (ws * z3.imag).sum((1, 2)) / a3], dim=1)
                zx, zy = X, Y
                return zeile

            t_end = T1_T[w2] * (RAUCH_FAKTOR if rauch else 1.0)
            t0 = uhr()
            t, daten = entwickeln(g, psi, vel, dt, t_end, messen)
            dauer[f"entwicklung_{stufe}_{w2}_s"] = uhr() - t0
            print(f"Entwicklung {stufe} omega2 {w2} fertig nach {dauer[f'entwicklung_{stufe}_{w2}_s']:.1f} s", flush=True)
            spalten = {"l2": 8, "l3": 10}
            om_lo = 2.0 * math.pi * 1.5 / t_end
            for b, (name, l, dr) in enumerate(laeufe):
                zeile = {"lauf": name, "l": l, "dR": dr, "stufe": stufe, "omega2": w2, "dx": dx, "dt": dt}
                reihe = daten[:, b, :]
                zeile["Q_box_verlust"] = (1.0 - reihe[-1, 4] / reihe[0, 4]).item()
                zeile["E_box_verlust"] = (1.0 - reihe[-1, 5] / reihe[0, 5]).item()
                zeile["R_rms_spanne"] = (reihe[:, 7].max() - reihe[:, 7].min()).item()
                zeile["max_abs_c2_c3"] = [reihe[:, 8].abs().max().item(), reihe[:, 10].abs().max().item()]
                zeile["max_abs_s2_s3"] = [reihe[:, 9].abs().max().item(), reihe[:, 11].abs().max().item()]
                zeile["schwerpunkt_weg"] = torch.sqrt(reihe[:, 0] ** 2 + reihe[:, 1] ** 2).max().item()
                if l in (2, 3):
                    per = periodogramm(t, reihe[:, spalten[f"l{l}"]], om_lo, 0.6)
                    zeile["periodogramm"] = per
                    zeile["verhaeltnis_P"] = {k: per["omega"] / wert for k, wert in vorh[w2]["l"][l].items()
                                              if k.startswith("P")}
                ergebnis.setdefault(stufe, []).append(zeile)
            zeitreihen[f"{stufe}_{w2}"] = {"t": t.cpu(), "daten": daten.cpu(), "laeufe": list(laeufe),
                                           "spalten": ["X", "Y", "Q_fenster", "E_fenster", "Q_box", "E_box", "S_max",
                                                       "R_rms", "c2", "s2", "c3", "s3"]}
    # Kennzahlen und Kriterien (fest vor dem Lauf, PLAN.md Abschnitt 2)
    def om(stufe, w2, lauf):
        for z in ergebnis.get(stufe, []):
            if z["omega2"] == w2 and z["lauf"] == lauf and "periodogramm" in z:
                return z["periodogramm"]["omega"]
        return None
    kenn = {}
    for w2 in omegas:
        k = {}
        for stufe in ("grob", "fein"):
            o2, o3 = om(stufe, w2, "l2"), om(stufe, w2, "l3")
            if o2 and o3:
                k[stufe] = {"Omega2": o2, "Omega3": o3, "Omega3_zu_Omega2": o3 / o2,
                            "zu_P1_l2": o2 / vorh[w2]["l"][2]["P1"], "zu_P1_l3": o3 / vorh[w2]["l"][3]["P1"]}
        o2g = om("grob", w2, "l2gross")
        if o2g and "grob" in k:
            k["linearitaet_dR_0.5_gegen_0.25"] = o2g / k["grob"]["Omega2"] - 1.0
        if "grob" in k and "fein" in k:
            aend = max(abs(k["fein"]["Omega2"] / k["grob"]["Omega2"] - 1.0),
                       abs(k["fein"]["Omega3"] / k["grob"]["Omega3"] - 1.0))
            abw = max(abs(k["fein"]["zu_P1_l2"] - 1.0), abs(k["fein"]["zu_P1_l3"] - 1.0))
            k["L3"] = {"max_aenderung_fein_grob": aend, "max_abw_von_P1_fein": abw,
                       "bestanden": aend <= max(0.2 * abw, 0.005)}
        kenn[w2] = k
    urteil = "offen"
    k52 = kenn.get(0.52, {}).get("fein") or kenn.get(0.52, {}).get("grob")
    if k52 and not rauch:
        r2, r3, q = k52["zu_P1_l2"], k52["zu_P1_l3"], k52["Omega3_zu_Omega2"]
        if 0.90 <= r2 <= 1.05 and 0.90 <= r3 <= 1.05 and 1.85 <= q <= 2.05:
            urteil = "Tropfenbild quantitativ getragen (Kriterium A)"
        elif r2 < 0.85 or r2 > 1.10 or r3 < 0.85 or r3 > 1.10 or q < 1.80 or q > 2.10:
            urteil = "Befund gegen das reine Tropfenbild (Kriterium B)"
        else:
            urteil = "Zwischenbereich: Trend 0,55 -> 0,52 entscheidet (Kriterium C)"
    ende = jetzt()
    ausgabe = {"test": "tropfen", "start": start, "ende": ende, "rauch": rauch, "dauer_s": dauer,
               "geraet": torch.cuda.get_device_name(0), "torch": torch.__version__,
               "parameter": {"omega2": omegas, "L": T1_L, "T": T1_T, "dR": [T1_DR, T1_DR_GROSS], "stufen": STUFEN,
                             "sponge": SPONGE, "sigma0": SIGMA0, "h_ode": H_ODE, "x_ode": X_ODE,
                             "n_kand_runden": [N_KAND, RUNDEN], "schwanz": SCHWANZ},
               "profile": [profil_info(pr) for pr in profile],
               "vorhersage": {str(w2): v for w2, v in vorh.items()}, "ergebnis": ergebnis,
               "kennzahlen": {str(w2): k for w2, k in kenn.items()}, "urteil": urteil}
    text = [f"Test 1 Tropfenschwingung (Wellen 16). Start {start}, Ende {ende}, {ausgabe['geraet']}, "
            f"torch {torch.__version__}" + (" RAUCHTEST: Zahlen ungueltig" if rauch else "")]
    text += laufzeit_text(dauer, rauch)
    text.append("Profile: omega2 | p = f(0) | Klammer | S_c | R_halb | Q | E | Virialrest | x_Schwanz")
    for pr in profile:
        text.append(f"  {pr['omega2']:.2f} | {pr['p']:.15f} | {pr['klammer']:.1e} | {pr['S_zentrum']:.6f} | "
                    f"{pr['R_halb']:.3f} | {pr['Q']:.3f} | {pr['E']:.3f} | {pr['virialrest']:.1e} | {pr['x_schwanz']:.2f}")
    text.append("Vorhersage (aus dem Profil, vor der Entwicklung): omega2 l | P1 | P2 sigma_L | P3 sigma_0 | "
                "P4 rho=n | P5 rho=eps | P6 korr. | Periode P1")
    for w2 in omegas:
        for l in (2, 3):
            v = vorh[w2]["l"][l]
            text.append(f"  {w2:.2f} {l} | {v['P1']:.5f} | {v['P2']:.5f} | {v['P3']:.5f} | {v['P4']:.5f} | "
                        f"{v['P5']:.5f} | {v['P6']:.5f} | {v['T_P1']:.1f}")
    text.append("Messung: Stufe omega2 Lauf | Omega_mess | R2 | Omega/P1 | Omega/P6 | Nebenminima | "
                "E-Verlust Box | Atmung R_rms")
    for stufe in ergebnis:
        for z in ergebnis[stufe]:
            if "periodogramm" in z:
                per = z["periodogramm"]
                neben = ", ".join(f"{sp['omega']:.4f}({sp['R2']:.2f})" for sp in per["spitzen"])
                text.append(f"  {stufe} {z['omega2']:.2f} {z['lauf']} | {per['omega']:.5f} | {per['R2']:.3f} | "
                            f"{z['verhaeltnis_P']['P1']:.4f} | {z['verhaeltnis_P']['P6']:.4f} | {neben} | "
                            f"{z['E_box_verlust']:.1e} | {z['R_rms_spanne']:.2e}")
            else:
                text.append(f"  {stufe} {z['omega2']:.2f} {z['lauf']} | Kontrolle: max|c2|,|c3| = "
                            f"{z['max_abs_c2_c3'][0]:.1e}, {z['max_abs_c2_c3'][1]:.1e}; Atmung R_rms "
                            f"{z['R_rms_spanne']:.2e}; Schwerpunkt {z['schwerpunkt_weg']:.1e}")
    for w2, k in kenn.items():
        text.append(f"Kennzahlen omega2 {w2}: " + json.dumps(k))
    text.append("Urteil nach PLAN.md: " + urteil)
    schreiben(out, "tropfen" if nur_w2 is None else f"tropfen_{omegas[0]}", ausgabe, zeitreihen, "\n".join(text))


# ---------------------------------------------------------------- Profilkontrolle m = 0 und m = 1 (nur Schiessen)

def test_profile(out, rauch, nur_grob):
    """Radiales Schiessen fuer m = 0 und m = 1 bei PR_OMEGA2, ohne Zeitentwicklung.
    Kontrollen: 2D-Virial V_U = omega^2 N; dE/dQ = omega (Differenzenquotient zwischen Nachbarpunkten);
    m = 1: Kernloch S(0) = 0, innerer Halbwertsradius ("Auge", Idee 19 als Nebenprodukt)."""
    start = jetzt()
    print(f"Profilkontrolle Start {start} auf {torch.cuda.get_device_name(0)}, torch {torch.__version__}", flush=True)
    t0 = uhr()
    sch = schiessen(list(PR_OMEGA2) * 2, [0] * len(PR_OMEGA2) + [1] * len(PR_OMEGA2))
    profile = profile_bauen(sch, 80.0, streng=False)
    dauer = {"schiessen_s": uhr() - t0}
    zeilen = []
    for pr in profile:
        info = profil_info(pr)
        if pr["m"] != 0 and pr["gueltig"]:
            s = pr["f"] ** 2
            j = int((s >= 0.5 * pr["S_max"]).to(torch.int64).argmax())
            s0, s1 = s[j - 1].item(), s[j].item()
            info["R_kern_halb"] = ((j - 1) + (0.5 * pr["S_max"] - s0) / (s1 - s0)) * H_ODE
        zeilen.append(info)
    for m in (0, 1):
        z = [zz for zz in zeilen if zz["m"] == m]
        for a, b in zip(z[:-1], z[1:]):
            if not (a["gueltig"] and b["gueltig"]) or b["Q"] == a["Q"]:
                continue
            w_mitte = 0.5 * (math.sqrt(a["omega2"]) + math.sqrt(b["omega2"]))
            b["dEdQ_zu_omega_mitte"] = (b["E"] - a["E"]) / (b["Q"] - a["Q"]) / w_mitte
    ende = jetzt()
    ausgabe = {"test": "profile", "start": start, "ende": ende, "dauer_s": dauer, "geraet": torch.cuda.get_device_name(0),
               "torch": torch.__version__, "h_ode": H_ODE, "x_ode": X_ODE, "n_kand_runden": [N_KAND, RUNDEN],
               "profile": zeilen}
    text = [f"Profilkontrolle m = 0, 1. Start {start}, Ende {ende}, {ausgabe['geraet']}"]
    text += laufzeit_text(dauer, False)
    text.append("m omega2 | p | Klammer | S_max | R_halb | R_kern_halb | Q | E | E/Q | Virialrest | dE/dQ / omega | gueltig")
    for zz in zeilen:
        text.append(f"  {zz['m']} {zz['omega2']:.2f} | {zz['p']:.15f} | {zz['klammer']:.1e} | {zz['S_max']:.6f} | "
                    f"{zz['R_halb']:.3f} | {zz.get('R_kern_halb', float('nan')):.3f} | {zz['Q']:.4f} | {zz['E']:.4f} | "
                    f"{(zz['E'] / zz['Q'] if zz['Q'] else float('nan')):.5f} | {zz['virialrest']:.1e} | {zz.get('dEdQ_zu_omega_mitte', float('nan')):.4f} | "
                    f"{'ja' if zz['gueltig'] else 'NEIN (Bahn ungenau, Zeile nicht verwenden)'}")
    tabellen = {"omega2": [p["omega2"] for p in profile], "m": [p["m"] for p in profile], "h": H_ODE,
                "f": torch.stack([p["f"] for p in profile]).cpu(), "fp": torch.stack([p["fp"] for p in profile]).cpu()}
    schreiben(out, "profile", ausgabe, tabellen, "\n".join(text))


# ---------------------------------------------------------------- Test 3: Brechung (Wellen 14)

def masse_bei_ladung(fam, q1, v2):
    """Ruheenergie im Medium V2 bei fester Ladung Q1. Im Medium ist f das Profil der Familie bei
    Omega^2 = omega2^2 - V2; Q2 = 2 omega2 N(Omega^2), E2 = omega2 Q2 + G(Omega^2) (2D-Virial)."""
    werte = []
    for pr in fam:
        om2 = pr["omega2"] + v2
        if om2 <= 0.0:
            continue
        w = math.sqrt(om2)
        werte.append((pr["omega2"], 2.0 * w * pr["N"] - q1, pr["G"]))
    for (a1, h1, g1), (a2, h2, g2) in zip(werte[:-1], werte[1:]):
        if h1 == 0.0 or h1 * h2 < 0.0:
            phi = h1 / (h1 - h2)
            om_gross2 = a1 + phi * (a2 - a1)
            w2 = math.sqrt(om_gross2 + v2)
            return {"M2": w2 * q1 + g1 + phi * (g2 - g1), "Omega2_familie": om_gross2, "omega_im_medium": w2}
    return None


def brechung_vorhersage(m1, q1, fam, v2, v1, th1):
    """Tangentialimpuls und Energie erhalten, Ball adiabatisch im Grundzustand bei fester Ladung."""
    mb = {"M2": m1, "Omega2_familie": None, "omega_im_medium": None} if v2 == 0.0 else masse_bei_ladung(fam, q1, v2)
    if mb is None:
        return None
    gam = 1.0 / math.sqrt(1.0 - v1 * v1)
    e_tot = gam * m1
    p1 = gam * m1 * v1
    py = p1 * math.sin(th1)
    p2q = e_tot ** 2 - mb["M2"] ** 2
    aus = {**mb, "E_tot": e_tot, "p1": p1, "vy": py / e_tot}
    if p2q <= py * py:
        aus.update({"ausgang": "reflektiert", "theta2_grad": math.degrees(th1), "v2": v1, "n_eff": None})
    else:
        p2 = math.sqrt(p2q)
        aus.update({"ausgang": "durchgelaufen", "theta2_grad": math.degrees(math.asin(py / p2)), "v2": p2 / e_tot,
                    "n_eff": p2 / p1})
    return aus


def test_brechung(out, rauch, nur_grob):
    start = jetzt()
    print(f"Test 3 Brechung Start {start} auf {torch.cuda.get_device_name(0)}, torch {torch.__version__}", flush=True)
    dauer = {}
    t0 = uhr()
    sch = schiessen(list(T3_FAMILIE), [0] * len(T3_FAMILIE))
    fam = profile_bauen(sch, 1.5 * T3_L + 5.0)
    dauer["schiessen_s"] = uhr() - t0
    pr = [p for p in fam if p["omega2"] == T3_OMEGA2][0]
    m1, q1 = pr["E"], pr["Q"]
    kontrolle_interp = masse_bei_ladung(fam, q1, 0.0)
    vorh = {}
    for name, v2, th in T3_LAEUFE["grob"]:
        vorh[name] = brechung_vorhersage(m1, q1, fam, v2, T3_V, math.radians(th))
        print(f"Vorhersage {name}: {json.dumps(vorh[name])}", flush=True)
    t_end = T3_T * (RAUCH_FAKTOR if rauch else 1.0)
    grenze = T3_L - SPONGE - 6.0
    ergebnis, zeitreihen = {}, {}
    for stufe, dx, dt in STUFEN:
        if nur_grob and stufe == "fein":
            continue
        g = Gitter(T3_L, dx)
        laeufe = T3_LAEUFE[stufe]
        psis, vels, vs, x0s, y0s = [], [], [], [], []
        for name, v2, th in laeufe:
            thr = math.radians(th)
            y0 = -0.5 * T3_V * math.sin(thr) * T3_T
            p_, v_ = ball_feld(g, pr, x0=T3_X0, y0=y0, v=T3_V, winkel=thr)
            psis.append(p_)
            vels.append(v_)
            vs.append(v2 * 0.5 * (1.0 + torch.tanh(g.x / T3_BREITE)))
            x0s.append(T3_X0)
            y0s.append(y0)
        psi = torch.cat(psis).contiguous()
        vel = torch.cat(vels).contiguous()
        V = torch.cat(vs)                                  # (B, 1, n)
        zx = torch.tensor(x0s, dtype=F64, device=DEV)
        zy = torch.tensor(y0s, dtype=F64, device=DEV)
        r_win = torch.full((psi.shape[0],), pr["R_halb"] + 8.0, dtype=F64, device=DEV)

        def messen(psi, vel):
            nonlocal zx, zy
            s, rho, e, fen, X, Y = grundmessung(g, psi, vel, V, zx, zy, r_win)
            zeile = torch.stack([X, Y, (rho * fen).sum((1, 2)) * g.dA, (e * fen).sum((1, 2)) * g.dA,
                                 s.amax((1, 2)), rho.sum((1, 2)) * g.dA, e.sum((1, 2)) * g.dA], dim=1)
            zx, zy = X, Y
            return zeile

        t0 = uhr()
        t, daten = entwickeln(g, psi, vel, dt, t_end, messen, V=V)
        dauer[f"entwicklung_{stufe}_s"] = uhr() - t0
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entwicklung_{stufe}_s']:.1f} s", flush=True)
        for b, (name, v2, th) in enumerate(laeufe):
            X, Y = daten[:, b, 0], daten[:, b, 1]
            zeile = {"lauf": name, "V2": v2, "theta1_soll_grad": th, "stufe": stufe, "vorhersage": vorh[name]}
            gueltig = (X.abs() <= grenze) & (Y.abs() <= grenze)
            erst = (X >= -T3_XFIT).nonzero()
            i_a = int(erst[0]) if erst.numel() > 0 else X.shape[0]
            idx = torch.arange(X.shape[0], device=DEV)
            vorher = (t >= 10.0) & (idx < i_a) & gueltig
            i_max = int(torch.argmax(X))
            durch = (X >= T3_XFIT) & gueltig
            zurueck = (idx > i_max) & (X <= -T3_XFIT) & gueltig
            def gerade(maske):
                fx = polyfit(t[maske], X[maske], 1)
                fy = polyfit(t[maske], Y[maske], 1)
                if fx is None or fy is None or int(maske.sum()) < 15:
                    return None
                return ((fx[0][1] / fx[3]).item(), (fy[0][1] / fy[3]).item(),
                        (fx[1][1] / fx[3]).item(), (fy[1][1] / fy[3]).item(), int(maske.sum()))
            g1 = gerade(vorher)
            if int(durch.sum()) >= 15:
                ausgang, g2 = "durchgelaufen", gerade(durch)
            elif int(zurueck.sum()) >= 15:
                ausgang, g2 = "reflektiert", gerade(zurueck)
            else:
                ausgang, g2 = "unklar", None
            zeile["ausgang"] = ausgang
            if g1 is not None:
                vx1, vy1 = g1[0], g1[1]
                zeile["v1_mess"] = math.hypot(vx1, vy1)
                zeile["theta1_mess_grad"] = math.degrees(math.atan2(vy1, vx1))
                zeile["vy1"], zeile["n_vorher"] = vy1, g1[4]
                zeile["vorhersage_aus_messung"] = brechung_vorhersage(m1, q1, fam, v2, zeile["v1_mess"],
                                                                      math.atan2(vy1, vx1))
            if g2 is not None:
                vx2, vy2 = g2[0], g2[1]
                zeile["v2_mess"] = math.hypot(vx2, vy2)
                zeile["theta2_mess_grad"] = math.degrees(math.atan2(vy2, abs(vx2)))
                zeile["vy2"], zeile["n_nachher"] = vy2, g2[4]
            if g1 is not None and g2 is not None and zeile["vorhersage_aus_messung"] is not None:
                va = zeile["vorhersage_aus_messung"]
                zeile["d_theta2_grad"] = zeile["theta2_mess_grad"] - va["theta2_grad"]
                zeile["v2_verhaeltnis"] = zeile["v2_mess"] / va["v2"]
                zeile["vy_verhaeltnis"] = zeile["vy2"] / zeile["vy1"] if abs(zeile["vy1"]) > 1e-4 else None
                zeile["ausgang_wie_vorhergesagt"] = va["ausgang"] == ausgang
            # Verluste am letzten gueltigen Messpunkt (danach kann der Ball in die Randschicht laufen)
            i_last = int(gueltig.nonzero().max()) if bool(gueltig.any()) else 0
            zeile["t_letzter_gueltiger"] = t[i_last].item()
            zeile["Q_fenster_verlust"] = (1.0 - daten[i_last, b, 2] / daten[0, b, 2]).item()
            zeile["E_fenster_verlust"] = (1.0 - daten[i_last, b, 3] / daten[0, b, 3]).item()
            ergebnis.setdefault(stufe, []).append(zeile)
        zeitreihen[stufe] = {"t": t.cpu(), "daten": daten.cpu(), "laeufe": list(laeufe),
                             "spalten": ["X", "Y", "Q_fenster", "E_fenster", "S_max", "Q_box", "E_box"]}
    kontrollen, urteil = {}, "offen"
    haupt = ergebnis.get("grob", [])            # alle sieben Laeufe; die feine Stufe dient der Aufloesungsprobe
    grob = {zz["lauf"]: zz for zz in haupt}
    kontrollen["K_interpolation_M_bei_V0"] = (kontrolle_interp["M2"] / m1 - 1.0) if kontrolle_interp else None
    oh = grob.get("ohne40")
    if oh and "theta2_mess_grad" in oh and "theta1_mess_grad" in oh:
        kontrollen["K_ohne_stufe_knick_grad"] = oh["theta2_mess_grad"] - oh["theta1_mess_grad"]
        kontrollen["K_ohne_stufe_v2_zu_v1"] = oh["v2_mess"] / oh["v1_mess"]
    if "fein" in ergebnis:
        aend = []
        for zz in ergebnis["fein"]:
            zg = grob.get(zz["lauf"])
            if zg and "theta2_mess_grad" in zz and "theta2_mess_grad" in zg:
                aend.append((abs(zz["theta2_mess_grad"] - zg["theta2_mess_grad"]),
                             abs(zz["theta2_mess_grad"] - zz["theta1_mess_grad"])))
        if aend:
            kontrollen["L3"] = {"max_aenderung_theta2_grad": max(a for a, _ in aend),
                                "min_knick_grad": min(k for _, k in aend),
                                "bestanden": all(a <= max(0.2 * k, 0.2) for a, k in aend)}
    if not rauch and haupt:
        pruef = [zz for zz in haupt if "d_theta2_grad" in zz and zz["V2"] != 0.0]
        if pruef:
            ok_winkel = all(abs(zz["d_theta2_grad"]) <= 1.0 for zz in pruef)
            ok_v = all(abs(zz["v2_verhaeltnis"] - 1.0) <= 0.02 for zz in pruef)
            ok_ausgang = all(zz["ausgang_wie_vorhergesagt"] for zz in pruef)
            if ok_winkel and ok_v and ok_ausgang:
                urteil = "Brechungsgesetz aus Energie- und Tangentialimpulserhaltung getragen (1 Grad, 2 %)"
            else:
                urteil = ("Brechungsgesetz verfehlt: " + ", ".join(
                    n for n, ok in (("Winkel", ok_winkel), ("Geschwindigkeit", ok_v), ("Ausgang", ok_ausgang))
                    if not ok) + " (Befund-Kandidat; zuerst Energieverlust ins Innere pruefen)")
    ende = jetzt()
    ausgabe = {"test": "brechung", "start": start, "ende": ende, "rauch": rauch, "dauer_s": dauer,
               "geraet": torch.cuda.get_device_name(0), "torch": torch.__version__,
               "parameter": {"omega2": T3_OMEGA2, "L": T3_L, "T": T3_T, "v1": T3_V, "x0": T3_X0,
                             "stufenbreite": T3_BREITE, "x_fit": T3_XFIT, "stufen": STUFEN},
               "ball": profil_info(pr), "familie": [profil_info(p) for p in fam], "vorhersage": vorh,
               "ergebnis": ergebnis, "kontrollen": kontrollen, "urteil": urteil}
    text = [f"Test 3 Brechung (Wellen 14). Start {start}, Ende {ende}, {ausgabe['geraet']}"
            + (" RAUCHTEST: Zahlen ungueltig" if rauch else "")]
    text += laufzeit_text(dauer, rauch)
    text.append(f"Ball omega2 {T3_OMEGA2}: p {pr['p']:.15f}, Q {q1:.4f}, M {m1:.4f}, R_halb {pr['R_halb']:.3f}, "
                f"Virialrest {pr['virialrest']:.1e}; Familie {len(fam)} Profile, Virialrest max "
                f"{max(abs(p['virialrest']) for p in fam):.1e}")
    text.append("Vorhersage (vor der Entwicklung): Lauf | V2 | theta1 | M2 | Ausgang | theta2 | v2 | n_eff")
    for name, v2, th in T3_LAEUFE["grob"]:
        vv = vorh[name]
        if vv is None:
            text.append(f"  {name} | {v2} | {th} | keine Loesung in der Familie")
            continue
        n_eff = f"{vv['n_eff']:.4f}" if vv["n_eff"] else "-"
        text.append(f"  {name} | {v2:+.2f} | {th:.0f} | {vv['M2']:.4f} | {vv['ausgang']} | "
                    f"{vv['theta2_grad']:.2f} | {vv['v2']:.4f} | {n_eff}")
    text.append("Messung: Stufe Lauf | Ausgang | theta1 mess | theta2 mess | d_theta2 zur Vorhersage | "
                "v2 mess/vorh | vy2/vy1 | Q-Verlust Fenster")
    for stufe in ergebnis:
        for zz in ergebnis[stufe]:
            text.append(f"  {stufe} {zz['lauf']} | {zz['ausgang']} | {zz.get('theta1_mess_grad', float('nan')):.2f} | "
                        f"{zz.get('theta2_mess_grad', float('nan')):.2f} | {zz.get('d_theta2_grad', float('nan')):.2f} | "
                        f"{zz.get('v2_verhaeltnis', float('nan')):.4f} | "
                        f"{(zz.get('vy_verhaeltnis') or float('nan')):.4f} | {zz['Q_fenster_verlust']:.1e}")
    text.append("Kontrollen: " + json.dumps(kontrollen))
    text.append("Urteil nach PLAN.md: " + urteil)
    schreiben(out, "brechung", ausgabe, zeitreihen, "\n".join(text))


def main():
    ap = argparse.ArgumentParser(description="Runde 3, 2D-Tests: Profile m = 0/1, Tropfen, Brechung")
    ap.add_argument("test", choices=["profile", "tropfen", "brechung", "alle"])
    ap.add_argument("--rauch", action="store_true", help="Laufzeiten x 0,05; nur Durchlauf und Hochrechnung")
    ap.add_argument("--nur-grob", action="store_true", help="feine Stufe auslassen (nur falls die Zeit nicht reicht)")
    ap.add_argument("--omega2", type=float, default=None, help="Test 1 nur fuer dieses omega^2 (0.52 oder 0.55)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "rauchtest" if args.rauch else "ausgabe")
    for name in (("profile", "tropfen", "brechung") if args.test == "alle" else (args.test,)):
        if name == "profile":
            test_profile(out, args.rauch, args.nur_grob)
        elif name == "tropfen":
            test_tropfen(out, args.rauch, args.nur_grob, args.omega2)
        else:
            test_brechung(out, args.rauch, args.nur_grob)


if __name__ == "__main__":
    main()
