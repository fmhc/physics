#!/usr/bin/env python3
"""Runde 9 (runden-v3), Karte KOLL-1: kollektive Atmungswellen zweier (dreier) Q-Baelle an der stillen Stelle.
Explorativ. Plan, Gleichungen, Vorab-Erwartungen: PLAN.md im selben Ordner.

Modell: L = |phi_t|^2 - |grad phi|^2 - U(S), U = S - S^2 + S^3/2, S = |phi|^2, 3D.
Ball phi = f(r) e^{i omega t}; Stoerung phi = e^{i omega t}[F + chi], chi = a u e^{i rho t} + conj(a) v e^{-i rho t}:
    (-lap + dp - (omega + rho)^2) u + sp v = 0,   (-lap + dp - (omega - rho)^2) v + sp u = 0,
    dp = 1 - 4S + 4,5 S^2,  sp = -2S + 3S^2   (bic2-System, dort e^{-i omega t}).

Unterbefehle:
  cmt    Frage (a): Profil (Schiessen), Mode bei reellem rho, Krein-Norm N, Schwanz C_v, Kopplung J(d) asymptotisch
         und als 2D-Ueberlappintegral, gemeinsame Verschiebung Delta(d), Abstossung E_int(d) aus der Mittelebenen-
         Spannung, freie Bewegung d(t) und daraus die Weitergabe bei freien Baellen.
  lin    Frage (b), gehaltene Baelle (Zusatz der Bearbeitung): lineare Zeitentwicklung um den eingefrorenen
         Hintergrund, Stapel: Einzelball, Paare, Dreierkette.
  voll   Frage (b), freie Baelle (wie im Auftrag): volle nichtlineare Rechnung, Stapel Paar/Einzel mit eps = 0, +, -.
  auswerten  Auswertung gespeicherter Reihen (laeuft am Ende von lin/voll automatisch).
Gitter: achsensymmetrisch (rho_z, z), rho_j = (j + 1/2) h, gerade Spiegelung an der Achse, 4. Ordnung im Raum,
Leapfrog mit Crank-Nicolson-Daempfung -sigma (phi_t - i omega phi) in der Randschicht (greift den ruhenden Ball
nicht an). Zeitgrenze je Aufruf --budget Sekunden; danach Zustand sichern, Fortsetzung mit --weiter.
Aufruf: python koll1.py <unterbefehl> [--geraet cuda|cpu] [--w2 ...] [--out ORDNER] ...
"""
import argparse
import datetime
import json
import math
import os
import sys
import time
import traceback

import numpy as np
import torch

F64 = torch.float64
PI = math.pi
T_START = time.perf_counter()
VEXT = None                 # Haltepotential (Option --halten), sonst None

W2_STILL = 0.7976768        # oberste stille Stelle (RUNDE-07, zweihaeusig)
RHO_STILL = 1.7446175
RHO_076 = 1.7281470         # kurve-050 (bic2, lauf-lokal): Pol 1.7281470 - 1.988e-3 i
GAMMA_076 = 1.988e-3


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    return time.perf_counter() - T_START


def U(S):
    return S - S * S + 0.5 * S ** 3


def U1(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def dpf(S):
    return 1.0 - 4.0 * S + 4.5 * S * S


def spf(S):
    return -2.0 * S + 3.0 * S * S


class Log:
    def __init__(self, pfad):
        self.pfad = pfad
        self.zeilen = []

    def __call__(self, *a):
        s = " ".join(str(x) for x in a)
        print(s, flush=True)
        self.zeilen.append(s)
        with open(self.pfad, "a") as fh:
            fh.write(s + "\n")


# ------------------------------------------------------------------------------------------------------------
# 1D: Profil und Mode
# ------------------------------------------------------------------------------------------------------------

def _rk4_profil(f0, w2, h, rmax, aufzeichnen=False):
    """Schiessen f'' = -2 f'/r + (U'(f^2) - w2) f fuer ein Feld von Startwerten f0.
    Rueckgabe: Schicksal (+1 schiesst ueber Null, -1 kehrt um, 0 unentschieden) und ggf. Verlauf."""
    f0 = np.atleast_1d(np.asarray(f0, float))
    c = (U1(f0 * f0) - w2) * f0 / 6.0
    r = h
    f = f0 + c * h * h
    g = 2.0 * c * h
    los = np.zeros(f0.size)
    aktiv = np.ones(f0.size, bool)
    FF = [f0.copy(), f.copy()] if aufzeichnen else None
    GG = [np.zeros_like(f0), g.copy()] if aufzeichnen else None
    n = int(round(rmax / h))

    def rhs(rr, ff, gg):
        return gg, -2.0 * gg / rr + (U1(ff * ff) - w2) * ff

    for i in range(1, n):
        k1f, k1g = rhs(r, f, g)
        k2f, k2g = rhs(r + 0.5 * h, f + 0.5 * h * k1f, g + 0.5 * h * k1g)
        k3f, k3g = rhs(r + 0.5 * h, f + 0.5 * h * k2f, g + 0.5 * h * k2g)
        k4f, k4g = rhs(r + h, f + h * k3f, g + h * k3g)
        f = f + h / 6.0 * (k1f + 2 * k2f + 2 * k3f + k4f)
        g = g + h / 6.0 * (k1g + 2 * k2g + 2 * k3g + k4g)
        r = (i + 1) * h
        if aufzeichnen:
            FF.append(f.copy())
            GG.append(g.copy())
        ueber = aktiv & (f < 0)
        unter = aktiv & (g > 0) & (f > 0)
        los[ueber] = 1
        los[unter] = -1
        aktiv &= ~(ueber | unter)
        if not aufzeichnen and not aktiv.any():
            break
    if aufzeichnen:
        return los, np.array(FF), np.array(GG)
    return los


PROFIL_H = 0.002
PROFIL_RMAX = 36.0


def profil(w2, h=None, rmax=None, n_kand=150, runden=9, log=print):
    """Grundzustand f(r) durch Einschachteln von f0; Schwanz A e^{-k0 r}/r ab r_c angesetzt."""
    h = PROFIL_H if h is None else h
    rmax = PROFIL_RMAX if rmax is None else rmax
    k0 = math.sqrt(1.0 - w2)
    s1d = 1.0 - math.sqrt(2.0 * w2 - 1.0)
    stop = (2.0 + math.sqrt(4.0 - 6.0 * (1.0 - w2))) / 3.0
    lo, hi = math.sqrt(s1d) + 1e-6, math.sqrt(stop) - 1e-6
    for rd in range(runden):
        kand = np.linspace(lo, hi, n_kand + 2)[1:-1]
        los = _rk4_profil(kand, w2, h, rmax)
        u = kand[los == -1]
        o = kand[los == 1]
        if u.size:
            lo = max(lo, u.max())
        if o.size:
            hi = min(hi, o.min())
        if (los == 0).all() or hi - lo < 1e-15:
            break
    los, FF, GG = _rk4_profil(np.array([lo, hi]), w2, h, rmax, aufzeichnen=True)
    r = np.arange(FF.shape[0]) * h
    fa, fb = FF[:, 0], FF[:, 1]
    fm = 0.5 * (fa + fb)
    gm = 0.5 * (GG[:, 0] + GG[:, 1])
    rel = np.abs(fa - fb) / np.maximum(np.abs(fm), 1e-300)
    schlecht = np.nonzero((rel > 1e-5) | (fm <= 0))[0]
    i_c = int(schlecht[0]) if schlecht.size else len(r) - 1
    r_c = r[i_c] - 2.0
    i_c = int(r_c / h)
    fenster = (r > r_c - 4.0) & (r <= r_c) & (r > 1.0)
    Aloc = fm[fenster] * r[fenster] * np.exp(k0 * r[fenster])
    A = float(np.median(Aloc))
    A_streu = float((Aloc.max() - Aloc.min()) / A)
    # auf festes Gitter bis 64 fortsetzen
    R = np.arange(0, 64.0 + h / 2, h)
    f = np.empty_like(R)
    g = np.empty_like(R)
    n1 = i_c + 1
    f[:n1] = fm[:n1]
    g[:n1] = gm[:n1]
    rt = R[n1:]
    f[n1:] = A * np.exp(-k0 * rt) / rt
    g[n1:] = -f[n1:] * (k0 + 1.0 / rt)
    w = math.sqrt(w2)
    S = f * f
    Q = 8 * PI * w * np.trapezoid(S * R * R, R)
    E = 4 * PI * np.trapezoid((w2 * S + g * g + U(S)) * R * R, R)
    log(f"  Profil omega^2 = {w2}: f0 = {0.5 * (lo + hi):.15f} (Klammer {hi - lo:.1e}), S0 = {fm[0] ** 2:.6f}, "
        f"r_c = {r_c:.2f}, A = {A:.6f} (Streuung {A_streu:.1e} auf [r_c-4, r_c]), Q = {Q:.4f}, E = {E:.4f}")
    return dict(w2=w2, w=w, k0=k0, h=h, r=R, f=f, g=g, A=A, A_streu=A_streu, r_c=float(r_c), Q=float(Q),
                E=float(E), f0=float(0.5 * (lo + hi)), S0=float(fm[0] ** 2))


def _mode_rk4(prof, rhos, r_m, aufzeichnen=False):
    """Zwei regulaere Loesungen (U, U', V, V') der reduzierten Kanalgleichungen fuer jedes reelle rho.
    Schritt H = 2 h (Profilwerte an Mittelpunkten vorhanden). Rueckgabe Zustand bei r_m [n_rho, 2, 4]."""
    h = prof["h"]
    H = 2 * h
    w = prof["w"]
    S = prof["f"] ** 2
    DP = dpf(S)
    SP = spf(S)
    rhos = np.atleast_1d(np.asarray(rhos, float))
    wp2 = ((w + rhos) ** 2)[:, None]
    wm2 = ((w - rhos) ** 2)[:, None]
    # Start bei r = H mit Reihe
    dp0, sp0 = DP[0], SP[0]
    Y = np.zeros((rhos.size, 2, 4))
    r = H
    for s, (al, be) in enumerate(((1.0, 0.0), (0.0, 1.0))):
        cu = ((dp0 - wp2[:, 0]) * al + sp0 * be) / 6.0
        cv = (sp0 * al + (dp0 - wm2[:, 0]) * be) / 6.0
        Y[:, s, 0] = al * r + cu * r ** 3
        Y[:, s, 1] = al + 3 * cu * r * r
        Y[:, s, 2] = be * r + cv * r ** 3
        Y[:, s, 3] = be + 3 * cv * r * r

    def rhs(i, Y):
        d, c = DP[i], SP[i]
        out = np.empty_like(Y)
        out[..., 0] = Y[..., 1]
        out[..., 1] = (d - wp2) * Y[..., 0] + c * Y[..., 2]
        out[..., 2] = Y[..., 3]
        out[..., 3] = c * Y[..., 0] + (d - wm2) * Y[..., 2]
        return out

    n = int(round(r_m / H))
    spur = [np.zeros_like(Y), Y.copy()] if aufzeichnen else None
    for k in range(1, n):
        i = 2 * k           # Index von r im Profilgitter
        k1 = rhs(i, Y)
        k2 = rhs(i + 1, Y + 0.5 * H * k1)
        k3 = rhs(i + 1, Y + 0.5 * H * k2)
        k4 = rhs(i + 2, Y + H * k3)
        Y = Y + H / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        if aufzeichnen:
            spur.append(Y.copy())
    r_end = n * H
    return Y, r_end, (np.array(spur) if aufzeichnen else None)


def _zerlegen(Y, r, w, rho):
    """Asymptotik: V = a e^{kr} + b e^{-kr}, U = c sin(qr) + d cos(qr). Y [..., 4]."""
    k = math.sqrt(1.0 - (w - rho) ** 2)
    q = math.sqrt((w + rho) ** 2 - 1.0)
    Uu, Up, Vv, Vp = Y[..., 0], Y[..., 1], Y[..., 2], Y[..., 3]
    a = (Vp + k * Vv) / (2 * k) * math.exp(-k * r)
    b = (k * Vv - Vp) / (2 * k) * math.exp(k * r)
    c = Uu * math.sin(q * r) + Up * math.cos(q * r) / q
    d = Uu * math.cos(q * r) - Up * math.sin(q * r) / q
    return a, b, c, d, k, q


def mode(prof, rho, r_m=16.0, r_n=12.0, still=False, log=print):
    """Mode bei reellem rho. Resonanz: Kombination der regulaeren Loesungen ohne wachsenden geschlossenen Anteil.
    Stille Stelle: dort verschwinden die Wachstumskoeffizienten beider regulaerer Loesungen (W = 0 in bic2), die
    Kombination a = 0 ist schlecht gestellt; stattdessen kleinster rechter Singulaervektor der Matrix
    [wachsender Anteil bei r_m, sin-, cos-Amplitude] (alle als Feldwerte bei r_m skaliert).
    Normierung max |u + v| = 1 (nicht reduziert). Rueckgabe Tabellen auf Gitter H = 2h bis 64."""
    w = prof["w"]
    Y, r_end, spur = _mode_rk4(prof, [rho], r_m, aufzeichnen=True)
    a, b, c, d, k, q = _zerlegen(Y[0], r_end, w, rho)
    if still:
        M3 = np.array([a * math.exp(k * r_end), c, d])
        _, sv, Vt = np.linalg.svd(M3)
        al, be = Vt[-1]
        log(f"  stille Stelle: Singulaerwerte {sv[0]:.3e}, {sv[1]:.3e} (Verhaeltnis {sv[1] / sv[0]:.2e}); "
            f"a-Zeile {a[0] * math.exp(k * r_end):+.3e}, {a[1] * math.exp(k * r_end):+.3e}")
    else:
        al, be = a[1], -a[0]          # al * y_a + be * y_b hat a = 0
    a_rest = (al * a[0] + be * a[1]) * math.exp(k * r_end)
    Ys = al * spur[:, 0, 0, :] + be * spur[:, 0, 1, :]
    H = 2 * prof["h"]
    rr = np.arange(Ys.shape[0]) * H
    Uu, Vv = Ys[:, 0], Ys[:, 2]
    bb = al * b[0] + be * b[1]
    cc = al * c[0] + be * c[1]
    dd = al * d[0] + be * d[1]
    # Innennorm und Aussenamplitude vor Normierung
    m = rr <= r_n
    Nroh = 8 * PI * np.trapezoid(((w + rho) * Uu ** 2 + (rho - w) * Vv ** 2)[m], rr[m])
    Bs = math.hypot(cc, dd)
    # auf Gitter bis 64 fortsetzen
    R = np.arange(0, 64.0 + H / 2, H)
    Ut = np.empty_like(R)
    Vt = np.empty_like(R)
    n1 = len(rr)
    Ut[:n1] = Uu
    Vt[:n1] = Vv
    rt = R[n1:]
    Ut[n1:] = cc * np.sin(q * rt) + dd * np.cos(q * rt)
    Vt[n1:] = bb * np.exp(-k * rt)
    u = np.empty_like(R)
    v = np.empty_like(R)
    u[1:] = Ut[1:] / R[1:]
    v[1:] = Vt[1:] / R[1:]
    u[0], v[0] = al, be
    skal = 1.0 / np.max(np.abs(u + v)[R <= 10])
    u *= skal
    v *= skal
    Ut *= skal
    Vt *= skal
    N = Nroh * skal ** 2
    Cv = bb * skal
    Bs_n = Bs * skal
    log(f"  Mode rho = {rho:.9f}: kappa_c = {k:.6f}, q = {q:.6f}, N (r <= {r_n}) = {N:.6e}, C_v = {Cv:+.6e}, "
        f"offene Aussenamplitude {Bs_n:.3e} (reduziert), wachsender Rest bei r_m {a_rest * skal:+.2e}, "
        f"V(r_m) {Vv[-1] * skal:+.3e}, u(0) = {u[0]:+.4f}, v(0) = {v[0]:+.4f}")
    return dict(rho=rho, kappa=k, q=q, N=float(N), Cv=float(Cv), Bs=float(Bs_n), H=H, r=R, u=u, v=v, U=Ut, V=Vt,
                u0=float(u[0]), v0=float(v[0]), a_rest=float(a_rest * skal))


def resonanz_scan(prof, rho0, breite=0.012, n=97, r_m=16.0, r_n=8.0, log=print):
    """Reelles rho abtasten: Innennorm / Aussenamplitude^2 hat bei der Resonanz ein Maximum der Breite Gamma."""
    w = prof["w"]
    rhos = rho0 + np.linspace(-breite, breite, n)
    Y, r_end, spur = _mode_rk4(prof, rhos, r_m, aufzeichnen=True)
    rr = np.arange(spur.shape[0]) * 2 * prof["h"]
    m = rr <= r_n
    inv = []
    for i, rho in enumerate(rhos):
        a, b, c, d, k, q = _zerlegen(Y[i], r_end, w, rho)
        al, be = a[1], -a[0]
        cc = al * c[0] + be * c[1]
        dd = al * d[0] + be * d[1]
        Ys = al * spur[:, i, 0, :] + be * spur[:, i, 1, :]
        Nin = np.trapezoid(((w + rho) * Ys[m, 0] ** 2 + (rho - w) * Ys[m, 2] ** 2), rr[m])
        inv.append((cc * cc + dd * dd) / Nin)
    inv = np.array(inv)
    j = int(np.argmin(inv))
    sel = inv < 4.0 * inv[j]
    x = rhos[sel]
    p = np.polyfit(x - rhos[j], inv[sel], 2)
    a2, a1, a0 = p
    x0 = -a1 / (2 * a2)
    mn = a0 - a1 * a1 / (4 * a2)
    gam = math.sqrt(max(mn, 0.0) / a2)
    rho_r = rhos[j] + x0
    log(f"  Resonanzabtastung um {rho0}: Maximum bei rho_r = {rho_r:.7f}, Breite aus Parabel Gamma = {gam:.4e} "
        f"({int(sel.sum())} Punkte)")
    return rho_r, gam


def tabelle_2d(tab_r, tab, R):
    """Lineare Interpolation einer radialen Tabelle (gleichabstaendig ab 0) an Radien R (torch)."""
    dr = float(tab_r[1] - tab_r[0])
    t = torch.as_tensor(tab, dtype=F64, device=R.device)
    x = (R / dr).clamp(max=len(tab) - 1.000001)
    i = x.floor().long()
    fr = x - i
    return t[i] * (1 - fr) + t[i + 1] * fr


def fenster(R, r1, r2):
    s = ((R - r1) / (r2 - r1)).clamp(0, 1)
    return torch.cos(0.5 * PI * s) ** 2


# ------------------------------------------------------------------------------------------------------------
# cmt: Frage (a)
# ------------------------------------------------------------------------------------------------------------

def cmt_punkt(w2, rho_start, dev, log, erg, name):
    prof = profil(w2, log=log)
    if name == "still":
        rho = rho_start
        gam = 0.0
    else:
        rho, gam = resonanz_scan(prof, rho_start, log=log)
    md = mode(prof, rho, still=(name == "still"), log=log)
    k, q, N, Cv = md["kappa"], md["q"], md["N"], md["Cv"]
    K = 4 * PI * Cv * Cv / N
    log(f"  K = 4 pi C_v^2 / N = {K:.4f}")
    # 2D-Quadratur um Ball A (Ursprung), B bei z = d
    hq = 0.02
    rq = (torch.arange(int(12 / hq), dtype=F64, device=dev) + 0.5) * hq
    zq = (torch.arange(int(24 / hq) + 1, dtype=F64, device=dev) - int(12 / hq)) * hq
    Rr, Zz = torch.meshgrid(rq, zq, indexing="ij")
    vol = 2 * PI * hq * hq * Rr
    rA = torch.sqrt(Rr * Rr + Zz * Zz)
    fA = tabelle_2d(prof["r"], prof["f"], rA)
    SA = fA * fA
    uA = tabelle_2d(md["r"], md["u"], rA)
    vA = tabelle_2d(md["r"], md["v"], rA)
    VAu = (dpf(SA) - 1) * uA + spf(SA) * vA
    VAv = spf(SA) * uA + (dpf(SA) - 1) * vA
    N2 = float((vol * 2 * ((prof["w"] + rho) * uA * uA + (rho - prof["w"]) * vA * vA)).sum())
    zeilen = []
    for d in (8.0, 10.0, 12.0, 14.0, 16.0):
        rB = torch.sqrt(Rr * Rr + (Zz - d) ** 2)
        uB = tabelle_2d(md["r"], md["u"], rB)
        vB = tabelle_2d(md["r"], md["v"], rB)
        fB = tabelle_2d(prof["r"], prof["f"], rB)
        tv = float((vol * vB * VAv).sum())
        tu = float((vol * uB * VAu).sum())
        Jas = -K * math.exp(-k * d) / d
        Jv = tv / N
        Ju = tu / N
        dl = {}
        for sg in (-1, 1):
            S0 = (fA + sg * fB) ** 2
            ddp = dpf(S0) - dpf(SA)
            dsp = spf(S0) - spf(SA)
            Dl = float((vol * (ddp * (uA * uA + vA * vA) + 2 * dsp * uA * vA)).sum())
            dl[sg] = Dl / N
        Jrad = gam / (q * d) if gam > 0 else 0.0
        z = dict(d=d, J_asym=Jas, J_2D_v=Jv, J_2D_u=Ju, J_2D=Jv + Ju, Delta_gegen=dl[-1], Delta_gleich=dl[1],
                 J_rad_betrag=Jrad, t_tr=PI / (2 * abs(Jv)) if Jv != 0 else None)
        zeilen.append(z)
        log(f"  d = {d:5.1f}: J asympt {Jas:+.4e} | J 2D v-Kanal {Jv:+.4e}, u-Kanal {Ju:+.3e} | "
            f"t_tr = pi/(2|J|) = {z['t_tr']:.0f} | Delta/N gegenphasig {dl[-1]:+.3e}, gleichphasig {dl[1]:+.3e} | "
            f"|J_rad| = Gamma/(qd) = {Jrad:.2e}")
    # Abstossung: Mittelebenen-Spannung der Ueberlagerung minus Einzelbaelle
    w = prof["w"]
    hp = 0.01
    rp = (torch.arange(int(25 / hp), dtype=F64, device=dev) + 0.5) * hp
    ds = np.arange(6.0, 40.01, 0.25)
    Fz = []
    for d in ds:
        rr = torch.sqrt(rp * rp + (d / 2) ** 2)
        f = tabelle_2d(prof["r"], prof["f"], rr)
        g = tabelle_2d(prof["r"], prof["g"], rr)
        dz = g * (d / 2) / rr
        dperp = g * rp / rr

        def tzz(Fv, Dz, Dp):
            return Dz * Dz - Dp * Dp + w * w * Fv * Fv - U(Fv * Fv)
        einzel = tzz(f, dz, dperp) + tzz(f, -dz, dperp)
        wert = []
        for sg in (-1, 1):
            Phi = f + sg * f
            Dz = dz - sg * dz
            Dp = dperp + sg * dperp
            wert.append(float((2 * PI * hp * rp * (tzz(Phi, Dz, Dp) - einzel)).sum()))
        Fz.append(wert)
    Fz = np.array(Fz)           # Spalte 0 gegenphasig, 1 gleichphasig; Kraft auf B in +z
    Eint = np.zeros_like(Fz)
    for j in range(2):
        tail = Fz[-1, j] / prof["k0"]
        cum = np.concatenate([np.cumsum(((Fz[1:, j] + Fz[:-1, j]) / 2 * np.diff(ds))[::-1])[::-1], [0.0]])
        Eint[:, j] = cum + tail
    M = prof["E"]
    mu = M / 2
    A = prof["A"]
    for d in (8.0, 10.0, 12.0, 14.0):
        i = int(np.argmin(np.abs(ds - d)))
        form = 8 * PI * A * A * math.exp(-prof["k0"] * d) / d
        log(f"  d = {d:5.1f}: Kraft gegenphasig {Fz[i, 0]:+.4e} (Abstossung > 0), gleichphasig {Fz[i, 1]:+.4e}; "
            f"E_int gegen {Eint[i, 0]:+.4e}, gleich {Eint[i, 1]:+.4e}; Formel 8 pi A^2 e^(-k0 d)/d = {form:.4e}")
    # freie Bewegung: mu d'' = F(d), aus der Ruhe
    frei = []
    for d0 in (10.0, 12.0, 14.0):
        dd, vv, tt = d0, 0.0, 0.0
        dt = 0.05
        theta = 0.0
        marken = {25: None, 50: None, 100: None, 200: None, 400: None, 1000: None}
        Jd = lambda x: K * math.exp(-k * x) / x
        while tt < 1000.0 + 1e-9:
            Fd = float(np.interp(dd, ds, Fz[:, 0])) if dd <= ds[-1] else Fz[-1, 0] * math.exp(-prof["k0"] * (dd - ds[-1]))
            vv += dt * Fd / mu
            dd += dt * vv
            theta += dt * Jd(dd)
            tt += dt
            for m_ in marken:
                if marken[m_] is None and tt >= m_ - 1e-9:
                    marken[m_] = (dd, vv, theta)
        frei.append(dict(d0=d0, marken={str(k_): v_ for k_, v_ in marken.items()}, theta_1000=theta,
                         b_max_frei=math.sin(min(theta, PI / 2))))
        log(f"  frei ab d0 = {d0}: d(50) = {marken[50][0]:.2f}, d(100) = {marken[100][0]:.2f}, "
            f"d(200) = {marken[200][0]:.2f}, d(400) = {marken[400][0]:.2f}; v(400) = {marken[400][1]:.4f}; "
            f"Integral |J| dt bis 1000 = {theta:.4f} -> b_max frei ~ {math.sin(min(theta, PI / 2)):.4f} "
            f"(gehalten: pi/2 nach t_tr)")
    erg[name] = dict(w2=w2, rho=rho, Gamma_scan=gam, kappa_c=k, q=q, N=N, N_2D=N2, Cv=Cv, K=K, Bs=md["Bs"],
                     A=prof["A"], A_streu=prof["A_streu"], Q=prof["Q"], E=prof["E"], S0=prof["S0"], k0=prof["k0"],
                     zeilen=zeilen, d_kraft=ds.tolist(), F_gegen=Fz[:, 0].tolist(), F_gleich=Fz[:, 1].tolist(),
                     E_int_gegen=Eint[:, 0].tolist(), E_int_gleich=Eint[:, 1].tolist(), frei=frei)
    log(f"  Kontrolle N: 1D {N:.6e}, 2D-Quadratur {N2:.6e}")
    return prof, md


def cmd_cmt(a, dev, log):
    erg = {}
    log("=== Frage (a): Kopplungsmodentheorie ===")
    log("--- stille Stelle ---")
    cmt_punkt(W2_STILL, RHO_STILL, dev, log, erg, "still")
    log("--- Vergleich omega^2 = 0,76 ---")
    cmt_punkt(0.76, RHO_076, dev, log, erg, "w076")
    s, v = erg["still"], erg["w076"]
    log("--- Zusammenfassung ---")
    for zs, zv in zip(s["zeilen"], v["zeilen"]):
        log(f"  d = {zs['d']:5.1f}: J still {zs['J_2D']:+.3e} (t_tr {zs['t_tr']:.0f}) | J 0,76 v-Kanal {zv['J_2D_v']:+.3e}"
            f" (t_tr {zv['t_tr']:.0f}), |J_rad| {zv['J_rad_betrag']:.2e}, Gamma 0,76 {v['Gamma_scan']:.3e} -> "
            f"Gamma/|J| = {v['Gamma_scan'] / abs(zv['J_2D_v']):.2f}")
    return erg


# ------------------------------------------------------------------------------------------------------------
# 2D-Zeitentwicklung
# ------------------------------------------------------------------------------------------------------------

class Gitter:
    def __init__(self, h, rmax, zmax, schicht, sig0, B, dev):
        self.h, self.dev, self.B = h, dev, B
        self.nr = int(round(rmax / h))
        self.nz = 2 * int(round(zmax / h)) + 1
        r = (torch.arange(self.nr, dtype=F64, device=dev) + 0.5) * h
        z = (torch.arange(self.nz, dtype=F64, device=dev) - (self.nz - 1) // 2) * h
        self.r, self.z = r, z
        self.R, self.Z = torch.meshgrid(r, z, indexing="ij")
        self.vol = 2 * PI * h * h * self.R
        sr = ((self.R - (rmax - schicht)) / schicht).clamp(min=0)
        sz = ((self.Z.abs() - (zmax - schicht)) / schicht).clamp(min=0)
        self.sig = (sig0 * torch.maximum(sr, sz) ** 2)[..., None]
        c = 1.0 / (12 * h * h)
        d1 = 1.0 / (12 * h)
        inv = (1.0 / r)[:, None, None]
        self.cr = [(-c + d1 * inv), (16 * c - 8 * d1 * inv), (16 * c + 8 * d1 * inv), (-c - d1 * inv)]
        self.c0 = -60.0 * c
        self.cz1, self.cz2 = 16.0 * c, -c
        self.P = torch.zeros(B, self.nr + 4, self.nz + 4, 2, dtype=F64, device=dev)
        self.phi = self.P[:, 2:-2, 2:-2]

    def lap(self):
        P = self.P
        P[:, 1, 2:-2] = P[:, 2, 2:-2]
        P[:, 0, 2:-2] = P[:, 3, 2:-2]
        C = P[:, 2:-2, 2:-2]
        out = self.c0 * C
        out.addcmul_(self.cr[0], P[:, 0:-4, 2:-2])
        out.addcmul_(self.cr[1], P[:, 1:-3, 2:-2])
        out.addcmul_(self.cr[2], P[:, 3:-1, 2:-2])
        out.addcmul_(self.cr[3], P[:, 4:, 2:-2])
        out.add_(P[:, 2:-2, 1:-3] + P[:, 2:-2, 3:-1], alpha=self.cz1)
        out.add_(P[:, 2:-2, 0:-4] + P[:, 2:-2, 4:], alpha=self.cz2)
        return out


def i_mal(x):
    return torch.stack((-x[..., 1], x[..., 0]), -1)


def ablt_r(x, j, h):
    return (-x[:, j + 2] + 8 * x[:, j + 1] - 8 * x[:, j - 1] + x[:, j - 2]) / (12 * h)


def ablt_z(x, k, h):
    return (-x[:, :, k + 2] + 8 * x[:, :, k + 1] - 8 * x[:, :, k - 1] + x[:, :, k - 2]) / (12 * h)


def fluss(G, dphi, pi_, jf, kf):
    """Energiefluss -2 Re(conj(pi) d_n dphi) durch Zylinder rho = r_jf, |z| <= z_kf (Stapel [B, nr, nz, 2])."""
    h = G.h
    k0 = (G.nz - 1) // 2
    ks = slice(k0 - kf, k0 + kf + 1)
    dr = ablt_r(dphi, jf, h)[:, ks]
    seite = -2 * (pi_[:, jf, ks] * dr).sum(-1)
    F = (seite * 2 * PI * G.r[jf] * h).sum(-1)
    for sgn, kk in ((1, k0 + kf), (-1, k0 - kf)):
        dz = ablt_z(dphi[:, :jf + 1], kk, h)
        kap = -2 * sgn * (pi_[:, :jf + 1, kk] * dz).sum(-1)
        F = F + (kap * 2 * PI * G.r[:jf + 1] * h).sum(-1)
    return F


def baelle_aufbauen(G, prof, md, glieder, win_anr=(6.0, 8.5), win_mess=(5.0, 6.5)):
    """Hintergrund F (reell, Vorzeichen je Ball), Anregungsfelder m, n am ersten Ball jedes Glieds, Messgewichte."""
    B = len(glieder)
    Fbg = torch.zeros(B, G.nr, G.nz, dtype=F64, device=G.dev)
    m = torch.zeros_like(Fbg)
    n = torch.zeros_like(Fbg)
    gew = []
    w, rho = prof["w"], md["rho"]
    um = md["u"] + md["v"]
    un = (w + rho) * md["u"] + (w - rho) * md["v"]
    tabs = []
    for b, (name, baelle) in enumerate(glieder):
        gw = []
        tb = []
        for j, (zc, sg) in enumerate(baelle):
            RR = torch.sqrt(G.R ** 2 + (G.Z - zc) ** 2)
            Fbg[b] += sg * tabelle_2d(prof["r"], prof["f"], RR)
            umR = tabelle_2d(md["r"], um, RR)
            tb.append(umR)
            wm = tabelle_2d(prof["r"], prof["f"], RR) * umR * fenster(RR, *win_mess)
            gw.append(wm * G.vol)
            if j == 0:
                fw = fenster(RR, *win_anr)
                m[b] = sg * umR * fw
                n[b] = sg * tabelle_2d(md["r"], un, RR) * fw
        gew.append(gw)
        tabs.append(tb)
    # Ueberlappmatrix: M[X][Y] = sum w_X 2 F (u + v)(r_Y); E_X = sum_Y M[X][Y] a_Y (a_Y: LCAO-Amplitude im chi-Bild)
    Ms = []
    for b in range(B):
        nb = len(gew[b])
        Ms.append([[float((gew[b][X] * 2 * Fbg[b] * tabs[b][Y]).sum()) for Y in range(nb)] for X in range(nb)])
    return Fbg, m, n, gew, Ms


def gewichte_bewegt(G, prof, md, zs, sgs, win_mess=(5.0, 6.5)):
    """Gewichte und Ueberlappmatrix fuer Baelle an den gemessenen Orten zs (Vorzeichen sgs)."""
    um = md["u"] + md["v"]
    Fb = torch.zeros(G.nr, G.nz, dtype=F64, device=G.dev)
    ws, tb = [], []
    for zc, sg in zip(zs, sgs):
        RR = torch.sqrt(G.R ** 2 + (G.Z - zc) ** 2)
        f = tabelle_2d(prof["r"], prof["f"], RR)
        umR = tabelle_2d(md["r"], um, RR)
        Fb += sg * f
        ws.append(f * umR * fenster(RR, *win_mess) * G.vol)
        tb.append(umR)
    M = [[float((ws[X] * 2 * Fb * tb[Y]).sum()) for Y in range(len(zs))] for X in range(len(zs))]
    return ws, M


def lauf_zeit(a, dev, log, art):
    os.makedirs(a.out, exist_ok=True)
    w2 = a.w2
    still = abs(w2 - W2_STILL) < 1e-6
    cache = f"cache-profil-mode-w2_{w2:.7f}-h_{PROFIL_H:g}-r_{PROFIL_RMAX:g}.npz"
    if os.path.exists(cache):
        C = np.load(cache)
        prof = {k_[2:]: (C[k_] if C[k_].ndim else float(C[k_])) for k_ in C.files if k_.startswith("p_")}
        md = {k_[2:]: (C[k_] if C[k_].ndim else float(C[k_])) for k_ in C.files if k_.startswith("m_")}
        rho = md["rho"]
        log(f"  Profil und Mode aus {cache}: A = {prof['A']:.6f}, Q = {prof['Q']:.4f}, rho = {rho:.9f}, N = {md['N']:.6e}, "
            f"C_v = {md['Cv']:+.6e}")
    else:
        prof = profil(w2, log=log)
        if still:
            rho = RHO_STILL
        else:
            rho, gam = resonanz_scan(prof, RHO_076 if abs(w2 - 0.76) < 1e-9 else a.rho0, log=log)
        md = mode(prof, rho, still=still, log=log)
        np.savez(cache + ".tmp.npz", **{"p_" + k_: np.asarray(v_) for k_, v_ in prof.items()},
                 **{"m_" + k_: np.asarray(v_) for k_, v_ in md.items()})
        os.replace(cache + ".tmp.npz", cache)
    w = prof["w"]
    h = a.h
    dt = a.cfl * h
    if art == "lin":
        glieder = [("einzel", [(-5.0, 1)])]
        for d in a.abstaende:
            glieder.append((f"paar{d:g}", [(-d / 2, 1), (d / 2, a.vorzeichen)]))
        if a.kette > 0:
            d = a.kette
            glieder.append((f"kette{d:g}", [(-d, 1), (0.0, a.vorzeichen), (d, 1)]))
        zmax = a.zmax
    else:
        d = a.d
        glieder = [("paar0", [(-d / 2, 1), (d / 2, -1)]), ("paar+", [(-d / 2, 1), (d / 2, -1)]),
                   ("paar-", [(-d / 2, 1), (d / 2, -1)]), ("einzel0", [(-d / 2, 1)]), ("einzel+", [(-d / 2, 1)]),
                   ("einzel-", [(-d / 2, 1)])]
        zmax = a.zmax
    B = len(glieder)
    G = Gitter(h, a.rmax, zmax, a.schicht, a.sig0, B, dev)
    log(f"  Gitter h = {h}, dt = {dt:.4f}, nr = {G.nr}, nz = {G.nz}, Glieder {B}: {[g_[0] for g_ in glieder]}, "
        f"Punkte je Glied {G.nr * G.nz}")
    Fbg, m, n, gew, Ms = baelle_aufbauen(G, prof, md, glieder)
    log("  Ueberlappmatrizen M (Zeile = Messball, Spalte = Mode): "
        + "; ".join(f"{g_[0]}: " + str([[round(x / Ms[0][0][0], 4) for x in zl] for zl in Ms[b]])
                    for b, g_ in enumerate(glieder)))
    cA = (1 - G.sig * dt / 2) / (1 + G.sig * dt / 2)
    cB = dt / (1 + G.sig * dt / 2)
    jf = int(round(a.rfluss / h - 0.5))
    kf = int(round(a.zfluss / h))
    eps = a.eps
    zustand = os.path.join(a.out, "zustand.pt")
    reihen_pfad = os.path.join(a.out, "reihen.npz")
    global VEXT
    VEXT = None
    if a.halten:
        # Haltepotential: V = R/F mit dem diskreten Rest R = lap F - U'(F^2) F + omega^2 F des Hintergrunds.
        # Damit ist der Hintergrund (Paar wie Einzelball) auf dem Gitter exakt stationaer ("gehaltene Baelle").
        G.phi[..., 0] = Fbg
        G.phi[..., 1] = 0
        L0 = G.lap()[..., 0]
        Rres = L0 - U1(Fbg * Fbg) * Fbg + w * w * Fbg
        gut = (Fbg.abs() > 1e-8) & (G.sig[..., 0] == 0)
        VEXT = torch.where(gut, Rres / torch.where(gut, Fbg, torch.ones_like(Fbg)), torch.zeros_like(Fbg))
        VEXT = VEXT.clamp(-1.0, 1.0)
        for b, (name, baelle) in enumerate(glieder):
            werte = []
            for zc, sg in baelle:
                j0 = int(round((zc - float(G.z[0])) / h))
                werte.append(float(VEXT[b, 0, j0]))
            innen = (Fbg[b].abs() > 0.3)
            log(f"  Haltepotential {name}: V in den Ballmitten {['%+.3e' % x for x in werte]}, "
                f"max |V| wo |F| > 0,3: {float(VEXT[b][innen].abs().max()):.3e}, max |V| gesamt {float(VEXT[b].abs().max()):.3e}")
        G.phi.zero_()
    if art == "lin":
        S0 = (Fbg * Fbg)[..., None]
        DP = dpf(S0) + (VEXT[..., None] if VEXT is not None else 0.0)
        SPv = spf(S0)
        Fb = Fbg[..., None]
    if a.weiter and os.path.exists(zustand):
        st = torch.load(zustand, map_location=dev)
        G.phi.copy_(st["phi"])
        pi_ = st["pi"].to(dev)
        t = st["t"]
        schritt = st["schritt"]
        alt = np.load(reihen_pfad)
        rec = {k_: list(alt[k_]) for k_ in alt.files}
        log(f"  fortgesetzt bei t = {t:.2f}, Schritt {schritt}")
    else:
        if art == "lin":
            G.phi[..., 0] = m
            G.phi[..., 1] = 0
            pi0 = torch.zeros_like(G.phi)
            pi0[..., 1] = n            # delta phi_t(0) = i n
            if a.paritaet != 0:
                # Paritaetsprojektion in z fuer alle Glieder ausser dem Einzelball (Glied 0): p = -1 ungerade, +1 gerade
                G.phi[1:] = 0.5 * (G.phi[1:] + a.paritaet * torch.flip(G.phi[1:], dims=[2]))
                pi0[1:] = 0.5 * (pi0[1:] + a.paritaet * torch.flip(pi0[1:], dims=[2]))
        else:
            e = torch.tensor([0.0, eps, -eps, 0.0, eps, -eps], dtype=F64, device=dev)[:, None, None]
            G.phi[..., 0] = Fbg + e * m
            G.phi[..., 1] = 0
            pi0 = torch.zeros_like(G.phi)
            pi0[..., 1] = w * Fbg + e * n
        t = 0.0
        schritt = 0
        rec = {}
        Fk = kraft(G, art, t, w, DP if art == "lin" else None, SPv if art == "lin" else None)
        pi_ = pi0 + 0.5 * dt * Fk
    budget = a.budget
    n_mess = max(1, int(round(a.dtmess / dt)))
    t_ende = a.T
    log(f"  Start Zeitschleife {jetzt()}, t = {t:.2f} bis {t_ende}, Messung alle {n_mess} Schritte, Budget {budget} s")
    t_schleife = uhr()
    while t < t_ende - 1e-9:
        # Drift: phi_{n+1} = phi_n + dt pi_{n+1/2}
        G.phi.add_(pi_, alpha=dt)
        t += dt
        schritt += 1
        Fk = kraft(G, art, t, w, DP if art == "lin" else None, SPv if art == "lin" else None)
        # pi_{n+3/2}
        Fk.add_(G.sig * w * i_mal(G.phi))
        pi_neu = cA * pi_ + cB * Fk
        if schritt % n_mess == 0:
            pim = 0.5 * (pi_ + pi_neu)
            messen(G, art, t, w, eps, gew, Fb if art == "lin" else None, pim, jf, kf, rec, prof, md, Fbg)
        pi_ = pi_neu
        if art == "lin" and a.paritaet != 0 and schritt % 10 == 0:
            G.phi[1:] = 0.5 * (G.phi[1:] + a.paritaet * torch.flip(G.phi[1:], dims=[2]))
            pi_[1:] = 0.5 * (pi_[1:] + a.paritaet * torch.flip(pi_[1:], dims=[2]))
        if schritt % 2000 == 0:
            if not torch.isfinite(G.phi).all():
                log(f"  ABBRUCH: nicht endlich bei t = {t:.2f}")
                break
            if uhr() > budget:
                log(f"  Budget erreicht bei t = {t:.2f} ({uhr():.0f} s)")
                break
    lz = uhr() - t_schleife
    log(f"  Ende Zeitschleife {jetzt()}, t = {t:.2f}, Schritte {schritt}, {lz:.1f} s "
        f"({1000 * lz / max(1, schritt):.2f} ms je Schritt in diesem Aufruf)")
    torch.save(dict(phi=G.phi.clone(), pi=pi_, t=t, schritt=schritt), zustand)
    np.savez(reihen_pfad, **{k_: np.array(v_) for k_, v_ in rec.items()})
    meta = dict(art=art, w2=w2, rho=rho, h=h, dt=dt, eps=eps, glieder=[g_[0] for g_ in glieder],
                baelle=[g_[1] for g_ in glieder], t=t, T=t_ende, rmax=a.rmax, zmax=zmax, schicht=a.schicht,
                sig0=a.sig0, rfluss=a.rfluss, zfluss=a.zfluss, A=prof["A"], Q=prof["Q"], E=prof["E"], N=md["N"],
                Cv=md["Cv"], kappa=md["kappa"], q=md["q"], fertig=bool(t >= t_ende - 1e-9), M=Ms)
    with open(os.path.join(a.out, "meta.json"), "w") as fh:
        json.dump(meta, fh, indent=1)
    auswerten(a.out, log)


def kraft(G, art, t, w, DP, SPv):
    L = G.lap()
    phi = G.phi
    if art == "voll":
        S = (phi * phi).sum(-1, keepdim=True)
        L.sub_(U1(S) * phi)
        if VEXT is not None:
            L.sub_(VEXT[..., None] * phi)
        return L
    c, s = math.cos(2 * w * t), math.sin(2 * w * t)
    a_, b_ = phi[..., 0], phi[..., 1]
    E = torch.stack((c * a_ + s * b_, s * a_ - c * b_), -1)
    L.sub_(DP * phi)
    L.sub_(SPv * E)
    return L


def messen(G, art, t, w, eps, gew, Fb, pim, jf, kf, rec, prof, md, Fbg=None):
    def add(k_, v_):
        rec.setdefault(k_, []).append(v_)
    add("t", t)
    phi = G.phi
    if art == "lin":
        c, s = math.cos(w * t), math.sin(w * t)
        dS = 2 * Fb[..., 0] * (c * phi[..., 0] + s * phi[..., 1])
        P = []
        for b, gw in enumerate(gew):
            P.append([float((g_ * dS[b]).sum()) for g_ in gw] + [0.0] * (3 - len(gw)))
        add("P", P)
        add("F", fluss(G, phi, pim, jf, kf).tolist())
        return
    # voll: Glieder 0..2 Paar (0, +, -), 3..5 Einzel (0, +, -). Zuerst Orte und Ladung aus eps = 0.
    S = (phi * phi).sum(-1)
    q = 2 * (phi[..., 0] * pim[..., 1] - phi[..., 1] * pim[..., 0])
    maske = (S > 1e-2).to(F64) * G.vol
    links = (G.Z < 0).to(F64)
    mA = maske[0] * links
    mB = maske[0] * (1 - links)
    zA = float((mA * S[0] * G.Z).sum() / (mA * S[0]).sum())
    zB = float((mB * S[0] * G.Z).sum() / (mB * S[0]).sum())
    zE = float((maske[3] * S[3] * G.Z).sum() / (maske[3] * S[3]).sum())
    add("z_A", zA)
    add("z_B", zB)
    add("z_E", zE)
    add("z_A+", float((maske[1] * links * S[1] * G.Z).sum() / (maske[1] * links * S[1]).sum()))
    add("z_B+", float((maske[1] * (1 - links) * S[1] * G.Z).sum() / (maske[1] * (1 - links) * S[1]).sum()))
    add("Q_A", float((q[0] * G.vol * links).sum()))
    add("Q_B", float((q[0] * G.vol * (1 - links)).sum()))
    add("Q_A+", float((q[1] * G.vol * links).sum()))
    add("Q_B+", float((q[1] * G.vol * (1 - links)).sum()))
    add("Q_E", float((q[3] * G.vol).sum()))
    wp, Mp = gewichte_bewegt(G, prof, md, [zA, zB], [1, -1])
    we, Me = gewichte_bewegt(G, prof, md, [zE], [1])
    add("M_paar", Mp)
    add("M_einzel", Me[0][0])
    # Hintergrundatmung ohne Anregung (eps = 0): delta S gegen den Anfangshintergrund, mit denselben Gewichten
    add("P_hint", [float((wp[0] * (S[0] - Fbg[0] ** 2)).sum()), float((we[0] * (S[3] - Fbg[3] ** 2)).sum())])
    for (i0, ip, im_, key, gw) in ((0, 1, 2, "paar", wp), (3, 4, 5, "einzel", we)):
        d1 = (phi[ip] - phi[im_]) / (2 * eps)
        d2 = (phi[ip] + phi[im_] - 2 * phi[i0]) / (2 * eps * eps)
        p1 = (pim[ip] - pim[im_]) / (2 * eps)
        p2 = (pim[ip] + pim[im_] - 2 * pim[i0]) / (2 * eps * eps)
        dS = 2 * (phi[i0] * d1).sum(-1)
        add("P_" + key, [float((g_ * dS).sum()) for g_ in gw] + [0.0] * (2 - len(gw)))
        Fl = fluss(G, torch.stack((d1, d2)), torch.stack((p1, p2)), jf, kf)
        add("F_" + key, Fl.tolist())


# ------------------------------------------------------------------------------------------------------------
# Auswertung
# ------------------------------------------------------------------------------------------------------------

def demod(t, P, rho, perioden=20):
    dt = t[1] - t[0]
    nw = int(round(perioden * 2 * PI / rho / dt))
    nw += (nw + 1) % 2
    z = P * np.exp(-1j * rho * t)
    cs = np.concatenate([[0], np.cumsum(z)])
    n = len(P)
    k = nw // 2
    E = np.full(n, np.nan + 0j)
    if n > nw:
        E[k:n - k] = (cs[nw:n + 1] - cs[0:n - nw + 1]) * 2.0 / nw
    return E


def steigung(x, y):
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 3:
        return float("nan")
    return float(np.polyfit(x[ok], y[ok], 1)[0])


def auswerten(out, log):
    meta = json.load(open(os.path.join(out, "meta.json")))
    R = np.load(os.path.join(out, "reihen.npz"))
    t = R["t"]
    rho = meta["rho"]
    ergebnis = dict(meta=meta)
    log(f"=== Auswertung {out} ({meta['art']}, omega^2 = {meta['w2']}, h = {meta['h']}, t bis {t[-1]:.1f}) ===")
    if len(t) < 50:
        log("  zu wenige Messpunkte")
        return
    if meta["art"] == "lin":
        P = R["P"]                    # [n, B, 3]
        F = R["F"]                    # [n, B]
        # Frequenz aus der Phase des Einzelballs nachfuehren
        E0 = demod(t, P[:, 0, 0], rho)
        ok = np.isfinite(E0)
        ph = np.unwrap(np.angle(E0[ok]))
        drho = steigung(t[ok], ph)
        rho_d = rho + drho
        Eraw = np.stack([np.stack([demod(t, P[:, b, j], rho_d) for j in range(3)], -1) for b in range(P.shape[1])], 1)
        # LCAO-Amplituden im chi-Bild: E_X = sum_Y M[X][Y] a_Y
        E = np.full_like(Eraw, np.nan + 0j)
        for b in range(P.shape[1]):
            nb = len(meta["baelle"][b])
            Mb = np.array(meta["M"][b])
            E[:, b, :nb] = Eraw[:, b, :nb] @ np.linalg.inv(Mb).T
            if nb > 1:
                log(f"  {meta['glieder'][b]}: Uebersprechen M_BA/M_BB = {Mb[1, 0] / Mb[1, 1]:+.4f}, "
                    f"M_AB/M_AA = {Mb[0, 1] / Mb[0, 0]:+.4f}")
        i1 = int(np.nonzero(np.isfinite(E[:, 0, 0]))[0][0])
        ref = abs(E[i1, 0, 0])
        amp = np.abs(E) / ref
        ergebnis["rho_d"] = rho_d
        log(f"  Demodulation bei rho_d = {rho_d:.7f} (Nachfuehrung {drho:+.2e}); Bezug |a_A| Einzelball bei "
            f"t = {t[i1]:.1f}; Amplituden nach Inversion der Ueberlappmatrix (chi-Bild, CMT: arg(b/a) = -pi/2 fuer "
            f"t_AB < 0)")
        okE = np.isfinite(amp[:, 0, 0])
        lnA = np.log(amp[okE, 0, 0])
        gam_e = -steigung(t[okE], lnA)
        ergebnis["Gamma_einzel"] = gam_e
        # Flusskalibrierung: F / sum a^2
        fl_e = F[okE, 0] / (amp[okE, 0, 0] ** 2)
        log(f"  Einzelball: Gamma (Abklingen a_A) = {gam_e:+.3e}; a_A(Ende) = {amp[okE, 0, 0][-1]:.5f}; "
            f"Fluss/a^2 Mittel = {np.mean(fl_e):.4e}")
        ergebnis["glieder"] = {}
        for b, name in enumerate(meta["glieder"]):
            nb = len(meta["baelle"][b])
            a_ = amp[:, b, :nb]
            okb = np.isfinite(a_[:, 0])
            tt = t[okb]
            aa = a_[okb]
            summe = (aa ** 2).sum(-1)
            z = dict(n_baelle=nb)
            if nb >= 2:
                th = np.arctan2(aa[:, 1] if nb == 2 else np.sqrt(aa[:, 1] ** 2 + aa[:, 2] ** 2), aa[:, 0])
                ib = int(np.argmax(aa[:, 1]))
                z.update(b_max=float(aa[ib, 1]), t_b_max=float(tt[ib]))
                sel = th < 1.0
                sel &= tt < (tt[np.argmax(th >= 1.0)] if (th >= 1.0).any() else np.inf)
                J_th = steigung(tt[sel], th[sel]) if sel.sum() > 5 else float("nan")
                z["J_aus_theta"] = J_th
                # Phase b gegen a frueh
                Eb = E[okb, b, 1]
                Ea = E[okb, b, 0]
                fr = (tt < min(tt[0] + 300, tt[-1])) & (np.abs(Eb) > 1e-6 * ref)
                if fr.any():
                    z["phase_b_zu_a"] = float(np.angle(np.mean(Eb[fr] / Ea[fr])))
                if nb == 3:
                    ic = int(np.argmax(aa[:, 2]))
                    z.update(c_max=float(aa[ic, 2]), t_c_max=float(tt[ic]))
            z["drho_A"] = steigung(tt, np.unwrap(np.angle(E[okb, b, 0])))
            z["Gamma_A"] = -steigung(tt, np.log(aa[:, 0]))
            z["summe_a2_ende"] = float(summe[-1] / summe[0])
            gs = -0.5 * steigung(tt, np.log(summe))
            z["Gamma_summe"] = gs
            fl = F[okb, b] / summe
            z["fluss_rel"] = float(np.mean(fl[len(fl) // 2:]) / np.mean(fl_e)) if np.mean(fl_e) != 0 else None
            for tm in (250, 500, 1000, 1500, 2000, 3000, 4000, 6000):
                j = np.searchsorted(tt, tm)
                if j < len(tt):
                    z[f"a_bei_{tm}"] = [float(x) for x in aa[j]]
            ergebnis["glieder"][name] = z
            txt = f"  {name:8s}: Summe a^2 Ende/Anfang {z['summe_a2_ende']:.5f}, Gamma_Summe {gs:+.3e}, Gamma_A {z['Gamma_A']:+.3e}, Frequenzversatz A gegen Einzelball {z['drho_A']:+.3e}"
            if nb >= 2:
                txt += (f"; b_max {z['b_max']:.4f} bei t = {z['t_b_max']:.0f}; J aus atan2(b, a) {z['J_aus_theta']:+.3e}"
                        f" -> pi/(2J) = {PI / (2 * abs(z['J_aus_theta'])):.0f}" if np.isfinite(z['J_aus_theta']) else "")
                if "phase_b_zu_a" in z:
                    txt += f"; arg(b/a) frueh {z['phase_b_zu_a']:+.3f}"
            if nb == 3:
                txt += f"; c_max {z['c_max']:.4f} bei t = {z['t_c_max']:.0f}"
            log(txt)
            stuetz = [f"t={tm}: " + "/".join(f"{x:.3f}" for x in z[f"a_bei_{tm}"]) for tm in (500, 1000, 2000, 3000, 4000)
                      if f"a_bei_{tm}" in z]
            log("            a(t): " + "; ".join(stuetz))
    else:
        Pp = R["P_paar"]
        Pe = R["P_einzel"]
        Fp = R["F_paar"]
        Fe = R["F_einzel"]
        E0 = demod(t, Pe[:, 0], rho)
        ok = np.isfinite(E0)
        drho = steigung(t[ok], np.unwrap(np.angle(E0[ok])))
        rho_d = rho + drho
        Mp = R["M_paar"]
        Me = R["M_einzel"]
        Ee = demod(t, Pe[:, 0], rho_d) / Me
        EAr = demod(t, Pp[:, 0], rho_d)
        EBr = demod(t, Pp[:, 1], rho_d)
        det = Mp[:, 0, 0] * Mp[:, 1, 1] - Mp[:, 0, 1] * Mp[:, 1, 0]
        EA = (Mp[:, 1, 1] * EAr - Mp[:, 0, 1] * EBr) / det
        EB = (-Mp[:, 1, 0] * EAr + Mp[:, 0, 0] * EBr) / det
        log(f"  Uebersprechen am Anfang M_BA/M_BB = {Mp[0, 1, 0] / Mp[0, 1, 1]:+.4f}, am Ende {Mp[-1, 1, 0] / Mp[-1, 1, 1]:+.2e}")
        i1 = int(np.nonzero(np.isfinite(Ee))[0][0])
        ref = abs(Ee[i1])
        okE = np.isfinite(Ee)
        ae, aA, aB = np.abs(Ee[okE]) / ref, np.abs(EA[okE]) / ref, np.abs(EB[okE]) / ref
        tt = t[okE]
        gam_e = -steigung(tt, np.log(ae))
        dd = R["z_B"] - R["z_A"]
        log(f"  Demodulation bei rho_d = {rho_d:.7f} ({drho:+.2e}); Einzelball Gamma = {gam_e:+.3e}, a(Ende) {ae[-1]:.5f}")
        ib = int(np.argmax(aB))
        log(f"  Paar: b_max = {aB[ib]:.4f} bei t = {tt[ib]:.0f}; a_A(Ende) {aA[-1]:.4f}; Summe a^2 Ende {aA[-1] ** 2 + aB[-1] ** 2:.4f}")
        for tm in (25, 50, 100, 200, 400, 800, 1600):
            j = np.searchsorted(t, tm)
            if j < len(t):
                jj = np.searchsorted(tt, tm)
                s_ = f"  t = {t[j]:7.1f}: d = {dd[j]:.3f}, z_E = {R['z_E'][j]:+.4f}, Q_A {R['Q_A'][j]:.3f}, Q_B {R['Q_B'][j]:.3f}"
                if jj < len(tt):
                    s_ += f", a_A {aA[jj]:.4f}, a_B {aB[jj]:.4f}, a_einzel {ae[jj]:.4f}"
                log(s_)
        n2 = len(Fp) // 2
        log(f"  Fluss (lineare Antwort, 2. Haelfte) Paar {np.mean(Fp[n2:, 0]):+.3e}, Einzel {np.mean(Fe[n2:, 0]):+.3e}; "
            f"zweite Ordnung Paar {np.mean(Fp[n2:, 1]):+.3e}, Einzel {np.mean(Fe[n2:, 1]):+.3e}")
        if "Q_A+" in R.files:
            dQ = (R["Q_A+"] - R["Q_B+"]) - (R["Q_A"] - R["Q_B"])
            dzA = R["z_A+"] - R["z_A"] if "z_A+" in R.files else None
            for tm in (25, 50, 100, 200, 400):
                j = np.searchsorted(t, tm)
                if j < len(t):
                    log(f"  t = {t[j]:7.1f}: Ladungsasymmetrie durch Anregung (Q_A - Q_B)(+eps) - (Q_A - Q_B)(0) = "
                        f"{dQ[j]:+.3e}" + (f", Verschiebung z_A(+eps) - z_A(0) = {dzA[j]:+.3e}" if dzA is not None else ""))
            ergebnis["dQ_ende"] = float(dQ[-1])
        if "P_hint" in R.files:
            Ph = R["P_hint"]
            Eh_e = np.abs(demod(t, Ph[:, 1], rho_d))[okE] / np.abs(demod(t, Pe[:, 0], rho_d))[okE]
            Eh_p = np.abs(demod(t, Ph[:, 0], rho_d))[okE] / np.abs(demod(t, Pp[:, 0], rho_d))[okE]
            log(f"  Hintergrundatmung ohne Anregung als aequivalentes eps: Einzel max {np.max(Eh_e):.2e}, "
                f"Paar-A max {np.max(Eh_p):.2e} (Anregung eps = {meta['eps']})")
            ergebnis["hint_eps_einzel"] = float(np.max(Eh_e))
            ergebnis["hint_eps_paar"] = float(np.max(Eh_p))
        ergebnis.update(rho_d=rho_d, Gamma_einzel=gam_e, b_max=float(aB[ib]), t_b_max=float(tt[ib]),
                        d_anfang=float(dd[0]), d_ende=float(dd[-1]), t_ende=float(t[-1]),
                        d_verlauf=[[float(t[j]), float(dd[j])] for j in range(0, len(t), max(1, len(t) // 40))],
                        a_verlauf=[[float(tt[j]), float(aA[j]), float(aB[j]), float(ae[j])]
                                   for j in range(0, len(tt), max(1, len(tt) // 40))],
                        z_E_ende=float(R["z_E"][-1]), Q_A=[float(R["Q_A"][0]), float(R["Q_A"][-1])],
                        Q_E=[float(R["Q_E"][0]), float(R["Q_E"][-1])],
                        fluss_lin=[float(np.mean(Fp[n2:, 0])), float(np.mean(Fe[n2:, 0]))],
                        fluss_2=[float(np.mean(Fp[n2:, 1])), float(np.mean(Fe[n2:, 1]))])
    with open(os.path.join(out, "auswertung.json"), "w") as fh:
        json.dump(ergebnis, fh, indent=1, default=float)


# ------------------------------------------------------------------------------------------------------------

def argumente():
    p = argparse.ArgumentParser()
    p.add_argument("kommando", choices=["cmt", "lin", "voll", "auswerten"])
    p.add_argument("--geraet", default="cuda")
    p.add_argument("--out", default="aus")
    p.add_argument("--w2", type=float, default=W2_STILL)
    p.add_argument("--rho0", type=float, default=RHO_076)
    p.add_argument("--h", type=float, default=0.1)
    p.add_argument("--cfl", type=float, default=0.4)
    p.add_argument("--rmax", type=float, default=22.0)
    p.add_argument("--zmax", type=float, default=32.0)
    p.add_argument("--schicht", type=float, default=8.0)
    p.add_argument("--sig0", type=float, default=2.0)
    p.add_argument("--rfluss", type=float, default=13.0)
    p.add_argument("--zfluss", type=float, default=23.0)
    p.add_argument("--abstaende", type=lambda s: [float(x) for x in s.split(",") if x], default=[10.0, 12.0, 14.0])
    p.add_argument("--kette", type=float, default=10.0)
    p.add_argument("--vorzeichen", type=int, default=-1, help="Vorzeichen von Ball B (und Mittelball der Kette) im lin-Lauf")
    p.add_argument("--halten", action="store_true", help="Haltepotential V = R/F: Hintergrund exakt stationaer")
    p.add_argument("--paritaet", type=int, default=0, help="lin: Projektion der Paar-/Kettenglieder auf z-Paritaet -1 oder +1")
    p.add_argument("--d", type=float, default=10.0)
    p.add_argument("--eps", type=float, default=0.005)
    p.add_argument("--T", type=float, default=3000.0)
    p.add_argument("--dtmess", type=float, default=0.2)
    p.add_argument("--budget", type=float, default=500.0)
    p.add_argument("--weiter", action="store_true")
    p.add_argument("--faeden", type=int, default=1)
    p.add_argument("--profil-h", type=float, default=0.002)
    p.add_argument("--profil-rmax", type=float, default=36.0)
    return p.parse_args()


def main():
    global PROFIL_H, PROFIL_RMAX
    a = argumente()
    PROFIL_H, PROFIL_RMAX = a.profil_h, a.profil_rmax
    torch.set_num_threads(a.faeden)
    dev = torch.device("cuda" if a.geraet == "cuda" and torch.cuda.is_available() else "cpu")
    os.makedirs(a.out, exist_ok=True)
    log = Log(os.path.join(a.out, "bericht.txt"))
    log(f"KOLL-1 {a.kommando} Start {jetzt()}, Geraet {dev}"
        + (f" ({torch.cuda.get_device_name(dev)})" if dev.type == "cuda" else "") + f", torch {torch.__version__}")
    log("  Argumente: " + json.dumps(vars(a)))
    rc = 0
    try:
        if a.kommando == "cmt":
            erg = cmd_cmt(a, dev, log)
            with open(os.path.join(a.out, "cmt.json"), "w") as fh:
                json.dump(erg, fh, indent=1, default=float)
        elif a.kommando in ("lin", "voll"):
            lauf_zeit(a, dev, log, a.kommando)
        else:
            auswerten(a.out, log)
    except Exception:
        log("FEHLER:\n" + traceback.format_exc())
        rc = 1
    log(f"Ende {jetzt()}, {uhr():.1f} s")
    sys.exit(rc)


if __name__ == "__main__":
    main()
