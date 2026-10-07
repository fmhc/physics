#!/usr/bin/env python3
"""Finns Idee F-5 (schwer und leicht, RUNDE-06/FINN-IDEE-F5-SCHWER-LEICHT.md): vier Versuchskarten F5-1 bis F5-4 mit dem
Zwei-Feld-Modell aus r5d.py (liegt daneben und wird importiert, unveraendert). Explorativ; Plan in PLAN-F5.md.

Modell wie r5d.py: psi schwer (Masse 1, U(S) = S - S^2 + S^3/2), chi leicht (Masse m < 1), V_chi = m^2 C + g4 C^2 (+ kc-Term),
Kopplung C (lam S + lam2 S^2) und Mischung eps (conj(psi) chi + c.c.).

Geometrie:
  f51  Q-Atom            3D radial: lineares Eigenwertproblem (l = 0, 1, 2) und radiale Zeitentwicklung (l = 0)
  f52  Huelle            3D radial: Huelle auf der Wand eines stabilen (0,7) und eines VK-instabilen (0,95) Kerns
  f53  Mischung          1D: Pendeln eines Pakets zwischen leicht und schwer; gemischte Baelle
  f54  unsichtbarer Kern 1D: Streuung einer leichten Welle an einem schweren Ball (nur lam)
3D radial: u = r psi, w = r chi; u_tt = u_rr - [...] u mit S = |u|^2/r^2 (l = 0), Dirichlet bei r = 0 und r = 150,
Daempfung ab r = 110 wie in der 1D-Box. Ladung Q = 8 pi Int Im(u conj(u_t)) dr. Das 3D-Profil des Kerns kommt aus dem
radialen Schiessen von RUNDE-02/tests1d.py (Test 4), hier unveraendert kopiert.

Aufruf:  python r5d_f5.py <rauch|f51|f52|f53|f54> [--geraet cuda|cpu] [--out ORDNER] [--masse 0.3|0.6 (nur f54)]
"""
import argparse
import json
import math
import os
import time
import traceback

import torch

import r5d as z

F64 = torch.float64
C128 = torch.complex128
PI = math.pi
DEV = torch.device("cpu")          # in main() gesetzt, zugleich z.DEV

# ---- radiales Schiessen aus tests1d.py (Test 4), unveraendert ----
H3, X3 = 0.05, 150.0
N_KAND3, RUNDEN3 = 1024, 4
S_MAX3 = 150.0
SCHWANZ = 1e-3

# ---- allgemein ----
R_MAX = 150.0                      # radiale Box [0, 150]
X_SPONGE = 110.0
SIGMA0 = 1.0
R_EIGEN = 60.0                     # lineares Eigenwertproblem auf (0, 60], Dirichlet an beiden Enden
DR_EIGEN = 0.05                    # Gitter fuer die Startvektoren (teilt 0,1 und 0,05)
RAUCH_FAKTOR = 0.05

# ---- F5-1 Q-Atom ----
A1_W2 = 0.7                        # 3D-Kern: Q 473,4, E 428,6, f0^2 1,135 (Test 4)
A1_M = [0.3, 0.6]
A1_LAM_SCAN = [-0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.8, -1.0]
A1_L = [0, 1, 2]
A1_G4 = 0.1                        # schwache Abstossung im leichten Feld: V nach unten beschraenkt
A1_LAEUFE = [
    {"name": "m=0,3 lam=-0,25 Q=1", "m": 0.3, "lam": -0.25, "q": 1.0},
    {"name": "m=0,3 lam=-0,35 Q=1", "m": 0.3, "lam": -0.35, "q": 1.0},
    {"name": "m=0,3 lam=-0,35 Q=20", "m": 0.3, "lam": -0.35, "q": 20.0},
    {"name": "m=0,6 lam=-0,3 Q=1", "m": 0.6, "lam": -0.3, "q": 1.0},
    {"name": "m=0,6 lam=-0,6 Q=1", "m": 0.6, "lam": -0.6, "q": 1.0},
    {"name": "m=0,6 lam=-0,6 Q=20", "m": 0.6, "lam": -0.6, "q": 20.0},
    {"name": "Gegenprobe lam=0", "m": 0.6, "lam": 0.0, "lam_start": -0.6, "q": 1.0},
    {"name": "tief m=0,3 lam=-0,8 g4=1", "m": 0.3, "lam": -0.8, "q": 0.01, "g4": 1.0},
]
A1_T, A1_MESS = 300.0, 0.5
A1_FENSTER = 40.0

# ---- F5-2 Huelle ----
B2_W2 = [0.7, 0.95]                # stabiler Kern und VK-instabiler Kern (Q_min bei omega^2 = 0,927)
B2_M, B2_G4 = 0.6, 0.1
B2_STOSS = 0.01                    # Kern mal 1,01: stoesst die VK-Mode an
B2_OM0 = 0.54                      # Startfrequenz der Huelle (0,9 m)
B2_LAEUFE = [
    {"name": "0,7 nackt", "iw": 0, "A": 0.0, "a": 0.0},
    {"name": "0,7 a=0 A=0,2", "iw": 0, "A": 0.2, "a": 0.0},
    {"name": "0,7 a=0,2 A=0,2", "iw": 0, "A": 0.2, "a": 0.2},
    {"name": "0,7 a=0,4 A=0,2", "iw": 0, "A": 0.2, "a": 0.4},
    {"name": "0,7 a=0,4 A=0,05", "iw": 0, "A": 0.05, "a": 0.4},
    {"name": "0,95 nackt", "iw": 1, "A": 0.0, "a": 0.0},
    {"name": "0,95 a=0 A=0,2", "iw": 1, "A": 0.2, "a": 0.0},
    {"name": "0,95 a=0,4 A=0,2", "iw": 1, "A": 0.2, "a": 0.4},
]
B2_T, B2_MESS = 400.0, 0.5
B2_FENSTER, B2_BAND = 40.0, 1.5

# ---- F5-3 Mischung (1D) ----
C3_A, C3_SIGMA = 1e-3, 10.0        # ruhendes Paket im leichten Feld
C3_PAKETE = [(0.6, 0.02), (0.6, 0.05), (0.9, 0.02), (0.9, 0.05), (0.97, 0.02), (0.97, 0.05), (0.9, 0.0)]
C3_W2 = 0.7
C3_BAELLE = [
    {"name": "psi-Ball, chi m=0,6, eps=0,02", "art": "ball_psi", "m": 0.6, "eps": 0.02},
    {"name": "psi-Ball, chi m=0,6, eps=0,05", "art": "ball_psi", "m": 0.6, "eps": 0.05},
    {"name": "psi-Ball, chi m=0,6, eps=0", "art": "ball_psi", "m": 0.6, "eps": 0.0},
    {"name": "psi-Ball, chi m=1,2, eps=0,05", "art": "ball_psi", "m": 1.2, "eps": 0.05},
    {"name": "chi-Ball m=0,6 (Kopie), eps=0,05", "art": "ball_chi", "m": 0.6, "eps": 0.05},
]
C3_T, C3_MESS = 400.0, 0.5
C3_FENSTER = 40.0

# ---- F5-4 unsichtbarer Kern (1D) ----
D4_W2 = 0.7
D4_M = [0.3, 0.6]
D4_LAM = [-0.3, 0.3, 0.0]          # lam = 0 ist die Bezugsmessung (Einstrom)
D4_K = [0.25, 0.4, 0.6, 0.9, 1.3]
D4_A, D4_SIGMA, D4_X0 = 1e-3, 12.0, -70.0
D4_EBENE, D4_FANG = 30.0, 10.0
D4_T, D4_MESS = 400.0, 0.2


# ================================================================ radiales Schiessen (tests1d.py, unveraendert)

def koeffizienten(a0):
    """f_top = sqrt(S+) mit S+ = (2 + sqrt(4 - 6 a0))/3 und Taylor-Koeffizienten c1..c5 von F um f_top."""
    s_top = (2.0 + torch.sqrt(4.0 - 6.0 * a0)) / 3.0
    t = torch.sqrt(s_top)
    c = (a0 - 6.0 * s_top + 7.5 * s_top * s_top, -6.0 * t + 15.0 * t * s_top, -2.0 + 15.0 * s_top, 7.5 * t,
         torch.full_like(t, 1.5))
    return t, c


def g_u(u, c):
    c1, c2, c3, c4, c5 = c
    return u * (c1 + u * (-c2 + u * (c3 + u * (-c4 + u * c5))))


def g_strich(u, c):
    c1, c2, c3, c4, c5 = c
    return c1 + u * (-2.0 * c2 + u * (3.0 * c3 + u * (-4.0 * c4 + u * 5.0 * c5)))


def rk4_radial(r, u, up, h, c, dm1):
    def ab(rr, uu, pp):
        return pp, g_u(uu, c) - dm1 * pp / rr
    k1u, k1p = ab(r, u, up)
    k2u, k2p = ab(r + 0.5 * h, u + 0.5 * h * k1u, up + 0.5 * h * k1p)
    k3u, k3p = ab(r + 0.5 * h, u + 0.5 * h * k2u, up + 0.5 * h * k2p)
    k4u, k4p = ab(r + h, u + h * k3u, up + h * k3p)
    return (u + (h / 6.0) * (k1u + 2.0 * k2u + 2.0 * k3u + k4u),
            up + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p))


def radial_start(s, c, dm1):
    d = dm1 + 1.0
    u0 = torch.exp(-s)
    a = g_u(u0, c) / (2.0 * d)
    b = g_strich(u0, c) * a / (4.0 * d + 8.0)
    return u0, u0 + a * H3 ** 2 + b * H3 ** 4, 2.0 * a * H3 + 4.0 * b * H3 ** 3


def schiessen_radial(a0, dm1, runden):
    t, c = koeffizienten(a0)
    lo = -torch.log(t - 1e-3)
    hi = torch.full_like(lo, S_MAX3)
    stufen = torch.linspace(0.0, 1.0, N_KAND3, dtype=F64, device=DEV)
    n_schritte = int(round(X3 / H3)) - 1
    for _ in range(runden):
        s = lo + (hi - lo) * stufen
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


# ================================================================ 3D-Profil, radiales Gitter, Eigenwerte

def profil_3d(w2_liste, runden):
    """3D-Kerne durch radiales Schiessen; f auf dem H3-Gitter bis j_cut, danach Schwanz wie in tests1d.py."""
    w2t = torch.tensor(w2_liste, dtype=F64, device=DEV).unsqueeze(1)
    dm1 = torch.full_like(w2t, 2.0)
    s, klammer, t, c = schiessen_radial(1.0 - w2t, dm1, runden)
    bu, _, j_cut, grund, f0 = radial_bahn(s, t, c, dm1)
    return {"w2": list(w2_liste), "f": t - bu, "j_cut": j_cut, "grund": grund, "klammer_s": klammer, "f0": f0}


def f_radial(prof, iw, r):
    """Kernprofil f(r): linear interpoliert bis r_cut, danach f_cut (r_cut/r) exp(-sqrt(1 - omega^2)(r - r_cut))."""
    f = prof["f"][iw]
    jc = min(int(prof["j_cut"][iw, 0].item()), f.shape[0] - 1)
    k = math.sqrt(1.0 - prof["w2"][iw])
    j = r / H3
    j0 = j.floor().clamp(0, f.shape[0] - 2)
    anteil = j - j0
    j0 = j0.long()
    innen = f[j0] * (1.0 - anteil) + f[j0 + 1] * anteil
    rc = jc * H3
    aussen = f[jc] * (rc / r.clamp(min=1e-12)) * torch.exp(-k * (r - rc))
    return torch.where(j < jc, innen, aussen)


def kern_kennzahlen(prof, iw):
    """Dichte in der Mitte, Wandradius (S = S(0)/2), Q und E des Kerns aus dem Profil (Trapez auf dem H3-Gitter)."""
    r = torch.arange(0, int(round(R_EIGEN / H3)) + 1, dtype=F64, device=DEV) * H3
    f = f_radial(prof, iw, r)
    s = f * f
    s0 = gf(s[0])
    halb = torch.nonzero(s < 0.5 * s0)
    r_w = gf(r[halb[0, 0]]) if halb.numel() else float("nan")
    w = math.sqrt(prof["w2"][iw])
    fp = torch.zeros_like(f)
    fp[1:-1] = (f[2:] - f[:-2]) / (2.0 * H3)
    dichte_q = 2.0 * w * s * r * r * 4.0 * PI
    dichte_e = (w * w * s + fp * fp + s - s * s + 0.5 * s ** 3) * r * r * 4.0 * PI
    return {"omega2": prof["w2"][iw], "S0": s0, "R_wand": r_w, "Q": gf(dichte_q.sum()) * H3,
            "E": gf(dichte_e.sum()) * H3, "grund": int(prof["grund"][iw, 0].item()),
            "r_cut": int(prof["j_cut"][iw, 0].item()) * H3}


def gitter_r(dr):
    return torch.arange(int(round(R_MAX / dr)) + 1, dtype=F64, device=DEV) * dr


def inv_r2_von(r):
    return torch.where(r > 0.0, 1.0 / (r * r).clamp(min=1e-300), torch.zeros_like(r))


def eigen_radial(potential, dr, l, vektoren=False):
    """-u'' + [potential(r) + l (l + 1)/r^2] u = e u auf r_i = i dr, i = 1 .. N-1 (Dirichlet bei 0 und R_EIGEN).

    Rueckgabe r, e (aufsteigend) und, falls verlangt, die Eigenvektoren als Spalten (Summe der Quadrate 1)."""
    n = int(round(R_EIGEN / dr))
    r = torch.arange(1, n, dtype=F64, device=DEV) * dr
    haupt = 2.0 / (dr * dr) + potential(r) + l * (l + 1) / (r * r)
    neben = torch.full((n - 2,), -1.0 / (dr * dr), dtype=F64, device=DEV)
    mat = torch.diag(haupt) + torch.diag(neben, 1) + torch.diag(neben, -1)
    if vektoren:
        e, vec = torch.linalg.eigh(mat)
        return r, e, vec
    return r, torch.linalg.eigvalsh(mat), None


def auf_gitter(r_e, vec, x):
    """Eigenvektor (Werte bei r_e = i DR_EIGEN) auf das Gitter x bringen; ausserhalb von (0, R_EIGEN) null."""
    idx = torch.round(x / DR_EIGEN).long()
    gut = (idx >= 1) & (idx <= r_e.shape[0])
    werte = vec[(idx - 1).clamp(0, r_e.shape[0] - 1)]
    return torch.where(gut, werte, torch.zeros_like(werte))


# ================================================================ Zeitentwicklung fuer 1D und 3D radial

def kraft_allg(u, w, par, dx, periodisch, inv_r2):
    """Wie r5d.kraft; in 3D radial sind u = r psi, w = r chi und S = |u|^2/r^2 (inv_r2), sonst inv_r2 = None."""
    s = u.real ** 2 + u.imag ** 2
    c = w.real ** 2 + w.imag ** 2
    if inv_r2 is not None:
        s = s * inv_r2
        c = c * inv_r2
    fp = 1.0 - 2.0 * s + 1.5 * s * s
    fc = par.mc2
    if par.mit_selbst:
        fc = fc + 2.0 * par.g4 * c + par.kc * (-2.0 * c + 1.5 * c * c)
    if par.mit_lam:
        fp = fp + c * (par.lam + 2.0 * par.lam2 * s)
        fc = fc + s * (par.lam + par.lam2 * s)
    a_u = z.lap(u, dx, periodisch) - fp * u
    a_w = z.lap(w, dx, periodisch) - fc * w
    if par.mit_eps:
        a_u = a_u - par.eps * w
        a_w = a_w - par.eps * u
    return a_u, a_w


def entwickeln_allg(felder, par, x, dx, dt, t_end, t_mess, messen, inv_r2):
    """Velocity-Verlet wie r5d.entwickeln; Daempfung ab |x| bzw. r = 110, Dirichlet an beiden Enden."""
    u, vu, w, vw = felder
    sig = SIGMA0 * ((x.abs() - X_SPONGE).clamp(min=0.0) / (R_MAX - X_SPONGE)) ** 2
    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(t_mess / dt)))
    h = 0.5 * dt
    reihe = [messen(u, vu, w, vw)]
    au, aw = kraft_allg(u, w, par, dx, False, inv_r2)
    for n in range(1, n_schritte + 1):
        vu = vu + h * (au - sig * vu)
        vw = vw + h * (aw - sig * vw)
        u = u + dt * vu
        w = w + dt * vw
        au, aw = kraft_allg(u, w, par, dx, False, inv_r2)
        vu = vu + h * (au - sig * vu)
        vw = vw + h * (aw - sig * vw)
        if n % alle == 0:
            reihe.append(messen(u, vu, w, vw))
    daten = torch.stack(reihe)
    endlich = torch.isfinite(daten).all(dim=2).all(dim=0)          # je Lauf; Laeufe sind unabhaengig
    if not bool(endlich.any()):
        raise RuntimeError("nicht endliche Messwerte in allen Laeufen: instabil")
    if not bool(endlich.all()):
        print(f"WARNUNG: nicht endliche Messwerte in Lauf {torch.nonzero(~endlich).flatten().tolist()}", flush=True)
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
    return t, daten, (u, vu, w, vw)


def stufen_allg(name, laeufe, bauen, t_end, t_mess, radial):
    """Grob (0,1 / 0,05) und fein (0,05 / 0,025). bauen(x, dx, par, inv_r2) -> (Felder, messen)."""
    par = z.Kopplung(laeufe)
    aus = {}
    for stufe, dx, dt in (("grob", z.DX, z.DT), ("fein", z.DX * z.FEIN, z.DT * z.FEIN)):
        x = gitter_r(dx) if radial else z.gitter(dx)
        inv_r2 = inv_r2_von(x) if radial else None
        felder, messen = bauen(x, dx, par, inv_r2)
        felder = list(felder)
        for a in felder:
            a[:, 0] = 0.0
            a[:, -1] = 0.0
        t0 = z.uhr()
        t, daten, ende = entwickeln_allg(felder, par, x, dx, dt, t_end, t_mess, messen, inv_r2)
        sek = z.uhr() - t0
        print(f"{name} {stufe}: {daten.shape[1]} Laeufe x {x.shape[0]} Punkte, T = {t_end:g}, "
              f"{int(round(t_end / dt))} Schritte, {sek:.1f} s", flush=True)
        aus[stufe] = {"t": t, "daten": daten, "sek": sek, "x": x}
    return aus


def ladungen_r(u, vu, w, vw, inv_r2):
    """3D radial: S, C und Ladungsdichten je dr (Q = Summe * dr)."""
    s = (u.real ** 2 + u.imag ** 2) * inv_r2
    c = (w.real ** 2 + w.imag ** 2) * inv_r2
    return s, c, 8.0 * PI * (u * vu.conj()).imag, 8.0 * PI * (w * vw.conj()).imag


def gf(v):
    return z.gf(v)


def teilen(a, b):
    return z.teilen(a, b)


def omega_aus_phase(t, th, ab):
    """Kreisfrequenz aus der Steigung der entfalteten Phase (M, B) ab Index ab."""
    return z.steigung(t[ab:], z.entfalten(th)[ab:])


def sek_zeile(res):
    return f"  Rechenzeit grob {res['sek']['grob']:.1f} s, fein {res['sek']['fein']:.1f} s"


# ================================================================ F5-1 Q-Atom (3D radial)

def a1_niveaus(prof, faktor):
    """Linear: Eigenwerte e von -u'' + [lam S + l(l+1)/r^2] u; omega^2 = m^2 + e. Grob dr = 0,1, fein dr = 0,05."""
    tabelle = {"grob": [], "fein": []}
    for stufe, dr in (("grob", 0.1), ("fein", 0.05)):
        for lam in A1_LAM_SCAN:
            for l in A1_L:
                r, e, vec = eigen_radial(lambda rr: lam * f_radial(prof, 0, rr) ** 2, dr, l, vektoren=True)
                gebunden = e < 0.0
                n_geb = int(gebunden.sum().item())
                eintraege = []
                for j in range(min(n_geb, 4)):
                    v = vec[:, j]
                    radius = math.sqrt(gf((r * r * v * v).sum() / (v * v).sum()))
                    eintraege.append({"e": gf(e[j]), "radius": radius})
                zeile = {"lam": lam, "l": l, "n_gebunden": n_geb, "niveaus": eintraege}
                for m in A1_M:
                    zeile[f"m={m}"] = {"omega2_grund": m * m + gf(e[0]),
                                       "stabil": bool(m * m + gf(e[0]) > 0.0),
                                       "n_gebunden_stabil": sum(1 for q in eintraege if m * m + q["e"] > 0.0)}
                tabelle[stufe].append(zeile)
    return tabelle


def test_f51(faktor):
    prof = profil_3d([A1_W2], 1 if faktor < 1.0 else RUNDEN3)
    kern = kern_kennzahlen(prof, 0)
    t0 = z.uhr()
    niveaus = a1_niveaus(prof, faktor)
    sek_lin = z.uhr() - t0
    print(f"f51 linear: {sek_lin:.1f} s", flush=True)
    laeufe = []
    start = {}
    for r in A1_LAEUFE:
        lam0 = r.get("lam_start", r["lam"])
        r_e, e, vec = eigen_radial(lambda rr: lam0 * f_radial(prof, 0, rr) ** 2, DR_EIGEN, 0, vektoren=True)
        om2 = r["m"] ** 2 + gf(e[0])
        om = math.sqrt(om2) if om2 > 0.0 else 0.1 * r["m"]
        start[r["name"]] = (r_e, vec[:, 0].clone(), om, math.sqrt(r["q"] / (8.0 * PI * om * DR_EIGEN)))
        laeufe.append(dict(r, mc2=r["m"] ** 2, kc=0.0, g4=r.get("g4", A1_G4), omega2_linear=om2, omega_start=om))
    w_kern = math.sqrt(A1_W2)

    def bauen(x, dx, par, inv_r2):
        f = f_radial(prof, 0, x)
        u = (x * f).to(C128)
        felder = []
        for r in laeufe:
            r_e, v0, om, amp = start[r["name"]]
            wv = (amp * auf_gitter(r_e, v0, x)).to(C128)
            felder.append((u.clone(), -1j * w_kern * u, wv, -1j * om * wv))
        fel = [torch.stack([f[j] for f in felder]) for j in range(4)]
        fen = (x < A1_FENSTER).to(F64)
        i1 = int(round(1.0 / dx))

        def messen(u, vu, w, vw):
            s, c, qu, qw = ladungen_r(u, vu, w, vw, inv_r2)
            nu = (u.real ** 2 + u.imag ** 2) * fen
            nw = (w.real ** 2 + w.imag ** 2) * fen
            return torch.stack([(qu * fen).sum(1) * dx, (qw * fen).sum(1) * dx,
                                torch.sqrt((x * x * nu).sum(1) / nu.sum(1).clamp(min=1e-300)),
                                torch.sqrt((x * x * nw).sum(1) / nw.sum(1).clamp(min=1e-300)),
                                c.max(dim=1).values, s[:, i1], -torch.angle(u[:, i1]), -torch.angle(w[:, i1])], dim=1)
        return fel, messen

    stufen = stufen_allg("f51", laeufe, bauen, A1_T * faktor, A1_MESS, radial=True)
    erg = {s: a1_auswertung(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "Bindung": z.l3(zg["bindung"], zf["bindung"], 0.0),
                 "R_chi": z.l3(zg["R_chi"], zf["R_chi"], 0.0)} for zg, zf in zip(erg["grob"], erg["fein"])]
    l3_lin = []
    for zg, zf in zip(niveaus["grob"], niveaus["fein"]):
        if zg["n_gebunden"] and zf["n_gebunden"]:
            l3_lin.append({"lauf": f"lam={zg['lam']} l={zg['l']}", "e0": z.l3(zg["niveaus"][0]["e"],
                                                                               zf["niveaus"][0]["e"], 0.0)})
    return {"laeufe": laeufe, "kern": kern, "niveaus": niveaus, "sek_linear": sek_lin, "ergebnis": erg,
            "L3": l3_liste, "L3_linear": l3_lin, "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def a1_auswertung(laeufe, t, d):
    ih = z.ab_index(t, 0.5)
    ie = z.ab_index(t, 0.75)
    om_c = omega_aus_phase(t, d[:, :, 7], ih)
    om_p = omega_aus_phase(t, d[:, :, 6], ih)
    zeilen = []
    for b, r in enumerate(laeufe):
        qp_halt = teilen(gf(d[-1, b, 0]), gf(d[0, b, 0]))
        qc_halt = teilen(gf(d[-1, b, 1]), gf(d[0, b, 1]))
        c_wachs = teilen(gf(d[:, b, 4].max()), gf(d[0, b, 4]))
        oc = gf(om_c[b])
        if c_wachs >= 3.0:
            klasse = "Kondensation"
        elif qc_halt < 0.5:
            klasse = "zerlaeuft"
        elif qc_halt >= 0.9 and qp_halt >= 0.98:
            klasse = "Atom stabil"
        else:
            klasse = "unklar"
        zeilen.append({"name": r["name"], "m": r["m"], "lam": r["lam"], "q": r["q"],
                       "omega2_linear": r["omega2_linear"], "omega_chi": oc, "omega_psi": gf(om_p[b]),
                       "bindung": r["m"] - oc, "E_bind_linear": -(r["m"] - oc) * gf(d[0, b, 1]),
                       "Q_psi_halt": qp_halt, "Q_chi_halt": qc_halt, "C_max_wachstum": c_wachs,
                       "R_psi": gf(d[ie:, b, 2].mean()), "R_chi": gf(d[ie:, b, 3].mean()),
                       "R_verhaeltnis": teilen(gf(d[ie:, b, 3].mean()), gf(d[ie:, b, 2].mean())),
                       "S_mitte_rel": teilen(gf(d[-1, b, 5]), gf(d[0, b, 5])), "klasse": klasse})
    return zeilen


def bericht_f51(res):
    k = res["kern"]
    zz = [f"F5-1 Q-Atom (3D radial): Kern omega^2 = {k['omega2']}, S(0) = {k['S0']:.4f}, Wandradius {k['R_wand']:.2f}, "
          f"Q = {k['Q']:.2f}, E = {k['E']:.2f} (Schiessen, Grund {k['grund']}, r_cut {k['r_cut']:.1f}).",
          f"  Linear (Rechenzeit {res['sek_linear']:.1f} s): e = omega^2 - m^2 der gebundenen Niveaus (e < 0); stabil, "
          "wenn m^2 + e0 > 0. Spalten: lam, l, Zahl gebunden, e (Radius) der ersten Niveaus, je m: omega0^2 und stabil"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for q in res["niveaus"][stufe]:
            nv = ", ".join(f"{n['e']:+.4f} ({n['radius']:.2f})" for n in q["niveaus"]) or "-"
            je_m = "; ".join(f"m={m}: {q[f'm={m}']['omega2_grund']:+.4f} {'stabil' if q[f'm={m}']['stabil'] else 'TACHYON'}"
                             for m in A1_M)
            zz.append(f"  lam={q['lam']:+.1f} l={q['l']} | {q['n_gebunden']} | {nv} | {je_m}")
    zz.append("  Dynamik (l = 0, Fenster r < 40): Lauf | omega^2 linear | omega_chi | Bindung m - omega | Q_chi, Q_psi "
              "gehalten | C_max Wachstum | R_chi / R_psi | Klasse")
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for q in res["ergebnis"][stufe]:
            zz.append(f"  {q['name']:22s} | {q['omega2_linear']:+.4f} | {q['omega_chi']:.4f} | {q['bindung']:+.4f} | "
                      f"{q['Q_chi_halt']:.4f}, {q['Q_psi_halt']:.4f} | {q['C_max_wachstum']:.2f} | "
                      f"{q['R_chi']:.2f} / {q['R_psi']:.2f} = {q['R_verhaeltnis']:.2f} | {q['klasse']}")
    zz += [z.l3_zeile(res["L3"]), "  L3 linear (e0):" + z.l3_zeile(res["L3_linear"])[1:], sek_zeile(res)]
    return zz


# ================================================================ F5-2 Huelle auf der Wand (3D radial)

def test_f52(faktor):
    prof = profil_3d(B2_W2, 1 if faktor < 1.0 else RUNDEN3)
    kerne = [kern_kennzahlen(prof, i) for i in range(len(B2_W2))]
    laeufe = []
    for r in B2_LAEUFE:
        s_in = kerne[r["iw"]]["S0"]
        lam, lam2 = -4.0 * r["a"] / s_in, 4.0 * r["a"] / (s_in * s_in)
        laeufe.append(dict(r, lam=lam, lam2=lam2, mc2=B2_M ** 2, kc=0.0, g4=B2_G4))
    niveaus = []                                            # lineares Huellen-Niveau (l = 0) je Lauf mit Kopplung
    for r in laeufe:
        if r["a"] > 0.0:
            iw, lam, lam2 = r["iw"], r["lam"], r["lam2"]
            _, e, _ = eigen_radial(lambda rr: lam * f_radial(prof, iw, rr) ** 2 + lam2 * f_radial(prof, iw, rr) ** 4,
                                   0.05, 0)
            niveaus.append({"lauf": r["name"], "omega2_grund": B2_M ** 2 + gf(e[0]), "gebunden": bool(gf(e[0]) < 0.0),
                            "stabil": bool(B2_M ** 2 + gf(e[0]) > 0.0)})

    def bauen(x, dx, par, inv_r2):
        felder = []
        for r in laeufe:
            iw = r["iw"]
            wk = math.sqrt(B2_W2[iw])
            u = ((1.0 + B2_STOSS) * x * f_radial(prof, iw, x)).to(C128)
            rw = kerne[iw]["R_wand"]
            wv = (r["A"] * x * torch.exp(-0.5 * (x - rw) ** 2)).to(C128)
            felder.append((u, -1j * wk * u, wv, -1j * B2_OM0 * wv))
        fel = [torch.stack([f[j] for f in felder]) for j in range(4)]
        fen = (x < B2_FENSTER).to(F64)
        rw_t = torch.tensor([kerne[r["iw"]]["R_wand"] for r in laeufe], dtype=F64, device=DEV).unsqueeze(1)
        band = ((x - rw_t).abs() < B2_BAND).to(F64) * fen
        i1 = int(round(1.0 / dx))

        def messen(u, vu, w, vw):
            s, c, qu, qw = ladungen_r(u, vu, w, vw, inv_r2)
            nw = (w.real ** 2 + w.imag ** 2)
            nu = (u.real ** 2 + u.imag ** 2) * fen
            return torch.stack([(qu * fen).sum(1) * dx, (qw * fen).sum(1) * dx,
                                (nw * band).sum(1) / (nw * fen).sum(1).clamp(min=1e-300), s[:, i1],
                                torch.sqrt((x * x * nu).sum(1) / nu.sum(1).clamp(min=1e-300)),
                                -torch.angle(u[:, i1]), c.max(dim=1).values], dim=1)
        return fel, messen

    stufen = stufen_allg("f52", laeufe, bauen, B2_T * faktor, B2_MESS, radial=True)
    erg = {s: b2_auswertung(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "Wandanteil": z.l3(zg["wandanteil"], zf["wandanteil"], 0.0),
                 "Q_psi_halt": z.l3(zg["Q_psi_halt"], zf["Q_psi_halt"], 1.0)}
                for zg, zf in zip(erg["grob"], erg["fein"]) if zg["A"] > 0.0]
    return {"laeufe": laeufe, "kerne": kerne, "niveaus": niveaus, "ergebnis": erg, "L3": l3_liste,
            "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def b2_auswertung(laeufe, t, d):
    ih = z.ab_index(t, 0.5)
    om_p = omega_aus_phase(t, d[:, :, 5], ih)
    zeilen = []
    for b, r in enumerate(laeufe):
        qp_halt = teilen(gf(d[-1, b, 0]), gf(d[0, b, 0]))
        s_rel = gf((d[:, b, 3] / d[0, b, 3] - 1.0).abs().max())
        if qp_halt >= 0.98 and s_rel < 0.3:
            kern = "stabil"
        elif qp_halt < 0.9 or s_rel > 0.5:
            kern = "zerfaellt"
        else:
            kern = "unklar"
        wand = gf(d[ih:, b, 2].mean())
        qc_halt = teilen(gf(d[-1, b, 1]), gf(d[0, b, 1]))
        huelle = "-" if r["A"] == 0.0 else ("traegt" if wand >= 0.5 and qc_halt >= 0.5 else "traegt nicht")
        zeilen.append({"name": r["name"], "omega2": B2_W2[r["iw"]], "a": r["a"], "A": r["A"], "Q_psi_halt": qp_halt,
                       "S_mitte_max_rel": s_rel, "omega_psi": gf(om_p[b]), "wandanteil": wand, "Q_chi_halt": qc_halt,
                       "C_max_wachstum": teilen(gf(d[:, b, 6].max()), gf(d[0, b, 6])), "R_psi_ende": gf(d[-1, b, 4]),
                       "kern": kern, "huelle": huelle})
    return zeilen


def bericht_f52(res):
    zz = ["F5-2 Huelle (3D radial): chi Masse 0,6 (g4 = 0,1), Kopplung -a 4 S (S0 - S)/S0^2 C, Kern x 1,01 angestossen."]
    for k in res["kerne"]:
        zz.append(f"  Kern omega^2 = {k['omega2']}: S(0) = {k['S0']:.4f}, Wandradius {k['R_wand']:.2f}, Q = {k['Q']:.2f}, "
                  f"E = {k['E']:.2f}")
    for n in res["niveaus"]:
        zz.append(f"  lineares Huellen-Niveau {n['lauf']}: omega^2 = {n['omega2_grund']:+.4f}, gebunden {n['gebunden']}, "
                  f"stabil {n['stabil']}")
    zz.append("  Lauf | Q_psi gehalten | S(r=1) max rel. Aenderung | omega_psi | Wandanteil chi | Q_chi gehalten | "
              "C_max Wachstum | Kern | Huelle")
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for q in res["ergebnis"][stufe]:
            zz.append(f"  {q['name']:18s} | {q['Q_psi_halt']:.4f} | {q['S_mitte_max_rel']:.3f} | {q['omega_psi']:.5f} | "
                      f"{q['wandanteil']:.3f} | {q['Q_chi_halt']:.3f} | {q['C_max_wachstum']:.2f} | {q['kern']} | "
                      f"{q['huelle']}")
    zz += [z.l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ F5-3 Mischung (1D)

def c3_massen(m, eps):
    """Eigenmassen der Massenmatrix [[1, eps], [eps, m^2]] und Mischungsamplitude sin^2(2 theta)."""
    spur, diff = 1.0 + m * m, 1.0 - m * m
    wurzel = math.sqrt(diff * diff + 4.0 * eps * eps)
    m_plus, m_minus = math.sqrt(0.5 * (spur + wurzel)), math.sqrt(max(0.0, 0.5 * (spur - wurzel)))
    return m_plus, m_minus, (4.0 * eps * eps / (wurzel * wurzel) if wurzel > 0.0 else 0.0)


def c3_ft(w2, k):
    """Int f(x) cos(k x) dx fuer das 1D-Profil (Quadratur h = 0,005)."""
    y = torch.arange(-80.0, 80.0 + 1e-9, 0.005, dtype=F64, device=DEV)
    f, _ = z.profil(y, w2)
    return gf((f * torch.cos(k * y)).sum()) * 0.005


def test_f53(faktor):
    laeufe = []
    for m, eps in C3_PAKETE:
        mp, mm, s2 = c3_massen(m, eps)
        laeufe.append({"name": f"Paket m={m} eps={eps}", "art": "paket", "m": m, "eps": eps, "mc2": m * m, "kc": 0.0,
                       "sin2_2theta": s2, "periode_formel": teilen(2.0 * PI, mp - mm)})
    w_ball = math.sqrt(C3_W2)
    for r in C3_BAELLE:
        mp, mm, _ = c3_massen(r["m"], r["eps"])
        if r["art"] == "ball_psi":
            leicht = min(mp, mm)
            k = math.sqrt(C3_W2 - leicht * leicht) if w_ball > leicht else 0.0
            g_v = r["eps"] ** 2 * c3_ft(C3_W2, k) ** 2 / k if k > 0.0 else 0.0
            laeufe.append(dict(r, mc2=r["m"] ** 2, kc=0.0, gamma_formel=g_v, k_abstrahl=k))
        else:
            laeufe.append(dict(r, mc2=r["m"] ** 2, kc=r["m"] ** 2, gamma_formel=0.0, k_abstrahl=0.0))

    def bauen(x, dx, par, inv_r2):
        felder = []
        for r in laeufe:
            if r["art"] == "paket":
                c = (C3_A * torch.exp(-0.5 * (x / C3_SIGMA) ** 2)).to(C128)
                p, vp = z.leer(x)
                felder.append((p, vp, c, -1j * r["m"] * c))
            elif r["art"] == "ball_psi":
                p, vp = z.ball(x, 0.0, C3_W2)
                s = p.real ** 2 + p.imag ** 2
                if r["mc2"] > C3_W2:                  # chi schwerer als omega: gebundene Bekleidung eps f/(U'(S) - m^2)
                    fak = r["eps"] / (1.0 - 2.0 * s + 1.5 * s * s - r["mc2"])
                else:                                 # chi leichter als omega: keine lokale Bekleidung, chi startet leer
                    fak = torch.zeros_like(s)
                felder.append((p, vp, fak * p, fak * vp))
            else:
                c, vc = z.ball(x, 0.0, C3_W2, m=r["m"])
                cc = c.real ** 2 + c.imag ** 2
                fak = r["eps"] / (r["mc2"] * (1.0 - 2.0 * cc + 1.5 * cc * cc) - 1.0)   # eps h/(m^2 U'(C) - 1)
                felder.append((fak * c, fak * vc, c, vc))
        fel = [torch.stack([f[j] for f in felder]) for j in range(4)]
        fen = (x.abs() < C3_FENSTER).to(F64)
        box = (x.abs() < 100.0).to(F64)

        def messen(u, vu, w, vw):
            qu = 2.0 * (u * vu.conj()).imag
            qw = 2.0 * (w * vw.conj()).imag
            return torch.stack([(qu * box).sum(1) * dx, (qw * box).sum(1) * dx,
                                (qu * fen).sum(1) * dx, (qw * fen).sum(1) * dx], dim=1)
        return fel, messen

    stufen = stufen_allg("f53", laeufe, bauen, C3_T * faktor, C3_MESS, radial=False)
    erg = {s: c3_auswertung(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = []
    for zg, zf in zip(erg["grob"], erg["fein"]):
        if zg["art"] == "paket" and zg["eps"] > 0.0:
            l3_liste.append({"lauf": zg["name"], "P_max": z.l3(zg["P_max"], zf["P_max"], 0.0),
                             "Periode": z.l3(zg["periode"], zf["periode"], 0.0)})
        elif zg["art"] != "paket" and zg["eps"] > 0.0:
            l3_liste.append({"lauf": zg["name"], "Gamma": z.l3(zg["gamma"], zf["gamma"], 0.0),
                             "p": z.l3(zg["p_ende"], zf["p_ende"], 0.0)})
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste,
            "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def c3_auswertung(laeufe, t, d):
    ia = z.ab_index(t, 0.25)
    zeilen = []
    for b, r in enumerate(laeufe):
        qp, qc = d[:, b, 0], d[:, b, 1]
        q0 = gf(qp[0] + qc[0])
        zl = {"name": r["name"], "art": r["art"], "m": r["m"], "eps": r["eps"]}
        if r["art"] == "paket":
            p = qp / q0
            om, _ = z.hauptfrequenz(t, p)
            zl.update({"P_max": gf(p.max()), "sin2_2theta": r["sin2_2theta"], "periode": teilen(2.0 * PI, om),
                       "periode_formel": r["periode_formel"]})
        else:
            qb = d[:, b, 2] + d[:, b, 3]
            gam = -gf(z.steigung(t[ia:], qb[ia:]))
            zl.update({"gamma": gam, "gamma_formel": r["gamma_formel"], "k_abstrahl": r["k_abstrahl"],
                       "Q_ball_0": gf(qb[0]), "Q_ball_T": gf(qb[-1]), "lebensdauer": teilen(gf(qb[ia]), gam),
                       "p_start": teilen(gf(d[0, b, 2]), gf(qb[0])), "p_ende": teilen(gf(d[-1, b, 2]), gf(qb[-1]))})
        zeilen.append(zl)
    return zeilen


def bericht_f53(res):
    zz = ["F5-3 Mischung (1D): Pakete im leichten Feld (A = 1e-3, sigma = 10, ruhend), Anteil P(t) = Q_psi/Q; Baelle "
          "omega^2 = 0,7 mit Bekleidung, Gamma = -dQ_Ball/dt auf [T/4, T], p = Q_psi/Q im Ballfenster |x| < 40."]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for q in res["ergebnis"][stufe]:
            if q["art"] == "paket":
                zz.append(f"  {q['name']:34s} | P_max {q['P_max']:.4e} (Formel sin^2 2theta {q['sin2_2theta']:.4e}) | "
                          f"Periode {q['periode']:.2f} (Formel {q['periode_formel']:.2f})")
            else:
                zz.append(f"  {q['name']:34s} | Gamma {q['gamma']:+.3e} (Formel {q['gamma_formel']:.3e}, k {q['k_abstrahl']:.3f}) "
                          f"| Q_Ball {q['Q_ball_0']:.4f} -> {q['Q_ball_T']:.4f} | Lebensdauer {q['lebensdauer']:.3e} | "
                          f"p {q['p_start']:.5f} -> {q['p_ende']:.5f}")
    zz += [z.l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ F5-4 unsichtbarer Kern (1D)

def d4_st(k2):
    """S~(q) = Int S(x) cos(q x) dx des 1D-Kerns bei q = 2 k (Quadratur h = 0,005)."""
    y = torch.arange(-80.0, 80.0 + 1e-9, 0.005, dtype=F64, device=DEV)
    f, _ = z.profil(y, D4_W2)
    return gf((f * f * torch.cos(k2 * y)).sum()) * 0.005


def test_f54(faktor, nur_masse=None):
    massen = [m for m in D4_M if nur_masse is None or abs(m - nur_masse) < 1e-9]
    laeufe = []
    for m in massen:
        for lam in D4_LAM:
            for k in D4_K:
                nu = math.sqrt(k * k + m * m)
                laeufe.append({"name": f"m={m} lam={lam:+.1f} k={k}", "m": m, "lam": lam, "k": k, "nu": nu,
                               "mc2": m * m, "kc": 0.0,
                               "R_born": lam * lam * d4_st(2.0 * k) ** 2 / (4.0 * k * k)})

    def bauen(x, dx, par, inv_r2):
        p, vp = z.ball(x, 0.0, D4_W2)
        felder = []
        for r in laeufe:
            k, nu = r["k"], r["nu"]
            env = D4_A * torch.exp(-((x - D4_X0) ** 2) / (2.0 * D4_SIGMA ** 2))
            c = env * torch.exp(1j * k * (x - D4_X0))
            vc = (-1j * nu + (k / nu) * (x - D4_X0) / D4_SIGMA ** 2) * c
            felder.append((p.clone(), vp.clone(), c, vc))
        fel = [torch.stack([f[j] for f in felder]) for j in range(4)]
        i0 = z.index_von(x, 0.0)
        di = int(round(D4_EBENE / dx))
        fang = (x.abs() < D4_FANG).to(F64)

        def messen(u, vu, w, vw):
            werte = []
            for i in (i0 - di, i0 + di):
                wx = (w[:, i + 1] - w[:, i - 1]) / (2.0 * dx)
                werte.append(-2.0 * (w[:, i] * wx.conj()).imag)
            qw = 2.0 * (w * vw.conj()).imag
            s = u.real ** 2 + u.imag ** 2
            werte += [(qw * fang).sum(1) * dx, s.max(dim=1).values]
            return torch.stack(werte, dim=1)
        return fel, messen

    stufen = stufen_allg("f54", laeufe, bauen, D4_T * faktor, D4_MESS, radial=False)
    erg = {s: d4_auswertung(laeufe, st["t"], st["daten"]) for s, st in stufen.items()}
    l3_liste = [{"lauf": zg["name"], "R": z.l3(zg["R"], zf["R"], 0.0)}
                for zg, zf in zip(erg["grob"], erg["fein"]) if zg["lam"] != 0.0]
    return {"laeufe": laeufe, "ergebnis": erg, "L3": l3_liste,
            "sek": {s: st["sek"] for s, st in stufen.items()}}, stufen


def d4_auswertung(laeufe, t, d):
    integ = 0.5 * ((d[1:] + d[:-1]) * (t[1:] - t[:-1]).view(-1, 1, 1)).sum(0)      # (B, 4)
    ref = {(r["m"], r["k"]): b for b, r in enumerate(laeufe) if r["lam"] == 0.0}
    zeilen = []
    for b, r in enumerate(laeufe):
        b0 = ref[(r["m"], r["k"])]
        ein = gf(integ[b0, 0])
        fl, fr = gf(integ[b, 0]), gf(integ[b, 1])
        tt, rr = teilen(fr, ein), teilen(ein - fl, ein)
        zeilen.append({"name": r["name"], "m": r["m"], "lam": r["lam"], "k": r["k"], "nu": r["nu"], "T": tt, "R": rr,
                       "A": 1.0 - tt - rr, "R_born": r["R_born"],
                       "fang": teilen(gf(d[-1, b, 2] - d[-1, b0, 2]), ein),
                       "S_max_aenderung": gf((d[:, b, 3] - d[0, b, 3]).abs().max())})
    return zeilen


def bericht_f54(res):
    zz = [f"F5-4 unsichtbarer Kern (1D): leichtes Paket (A = {D4_A}, sigma = {D4_SIGMA}) von x = {D4_X0} auf den Kern "
          f"omega^2 = {D4_W2}, nur Kopplung lam; Fluesse bei x = -+{D4_EBENE:g}; Bezug lam = 0.",
          "  Lauf | nu | T | R (Born) | A = 1 - T - R | Einfang |x| < 10 | max |dS_max|"]
    for stufe in ("grob", "fein"):
        zz.append(f"  [{stufe}]")
        for q in res["ergebnis"][stufe]:
            zz.append(f"  {q['name']:24s} | {q['nu']:.4f} | {q['T']:.6f} | {q['R']:.3e} ({q['R_born']:.3e}) | "
                      f"{q['A']:+.2e} | {q['fang']:+.2e} | {q['S_max_aenderung']:.1e}")
    zz += [z.l3_zeile(res["L3"]), sek_zeile(res)]
    return zz


# ================================================================ Hauptprogramm

TESTS = {"f51": (test_f51, bericht_f51), "f52": (test_f52, bericht_f52), "f53": (test_f53, bericht_f53),
         "f54": (test_f54, bericht_f54)}


def schreiben(out, name, ausgabe, text, reihen):
    basis = os.path.join(out, f"r5d_f5_{name}")
    with open(basis + "_bericht.txt", "w") as fh:
        fh.write("\n".join(text) + "\n")
    torch.save(reihen, basis + "_reihen.pt")
    with open(basis + "_ergebnis.json", "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=str)


def main():
    global DEV
    ap = argparse.ArgumentParser(description="F-5 schwer und leicht: F5-1 bis F5-4")
    ap.add_argument("unterbefehl", choices=["rauch"] + list(TESTS))
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cuda")
    ap.add_argument("--out", default=None)
    ap.add_argument("--masse", type=float, default=None, help="nur f54: nur diese leichte Masse (0.3 oder 0.6)")
    args = ap.parse_args()
    if args.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber keine CUDA-Karte sichtbar: Abbruch (kein stiller CPU-Ausweg).")
        DEV = torch.device("cuda")
        gesamt = torch.cuda.get_device_properties(0).total_memory
        torch.cuda.set_per_process_memory_fraction(min(1.0, z.SPEICHER_GB * 2 ** 30 / gesamt))
        name_geraet = torch.cuda.get_device_name(0)
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(1)
        name_geraet = "CPU, 1 Thread"
    z.DEV = DEV
    out = args.out or os.path.join(os.getcwd(), "ausgabe-f5-" + args.unterbefehl)
    os.makedirs(out, exist_ok=True)
    rauch = args.unterbefehl == "rauch"
    faktor = RAUCH_FAKTOR if rauch else 1.0
    auswahl = list(TESTS) if rauch else [args.unterbefehl]
    start = z.jetzt()
    t_start = time.perf_counter()
    kopf = (f"F-5 r5d_f5.py {args.unterbefehl} Start {start} auf {name_geraet}, torch {torch.__version__}, "
            f"Laufzeitfaktor {faktor}")
    print(kopf, flush=True)
    ausgabe = {"start": start, "geraet": name_geraet, "torch": torch.__version__, "unterbefehl": args.unterbefehl,
               "faktor": faktor, "ergebnisse": {}, "fehler": {}}
    text = [kopf, ""]
    reihen = {}
    for name in auswahl:
        funk, ber = TESTS[name]
        try:
            t0 = time.perf_counter()
            res, stufen = funk(faktor, args.masse) if name == "f54" else funk(faktor)
            res["dauer_s"] = time.perf_counter() - t0
            ausgabe["ergebnisse"][name] = res
            reihen[name] = {s: {k: (v.cpu() if torch.is_tensor(v) else v) for k, v in st.items()}
                            for s, st in stufen.items()}
            text += ber(res) + [f"  Dauer {name}: {res['dauer_s']:.1f} s", ""]
        except Exception:
            ausgabe["fehler"][name] = traceback.format_exc()
            text += [f"{name} FEHLER:", ausgabe["fehler"][name], ""]
            print(ausgabe["fehler"][name], flush=True)
        schreiben(out, args.unterbefehl, ausgabe, text, reihen)
    ausgabe["ende"] = z.jetzt()
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
