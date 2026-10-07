#!/usr/bin/env python3
"""Runde 6 (runden-v3), Karten R-1 bis R-5 zu Finns Frage: Kann Reflexion Q-Baelle oder ihre Resonanzen stabilisieren?
Explorativ. Plan, Aufrufe, Vorhersagen, Gegenproben und Latten stehen in PLAN.md daneben.

Modell wie RUNDE-02/tests1d/tests1d.py: L = |psi_t|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2, 1D.
Standardball omega^2 = 0,7. Exaktes Profil f^2 = 2 a0 / (1 + b0 cosh(2 sqrt(a0) x)), a0 = 1 - omega^2,
b0 = sqrt(2 omega^2 - 1) (in RUNDE-02 stimmte das Schiessen damit auf 1,5e-10 ueberein).

Zwei Werkzeuge.

LINEAR (R-1, R-2, R-3, R-5 und die Spiegelprobe von R-4). Stoerung psi = e^{-i omega t}(f + a e^{-i rho t}
  + conj(b) e^{i conj(rho) t}), physikalische Frequenz nu = omega + rho. Gekoppelte Zweikanal-ODE wie Codex
  (resonance-20260930/linear/run.py):
      a'' = (D - nu^2) a + s b,   b'' = s a + (D - (2 omega - nu)^2) b,   D = 1 - 4S + 4,5 S^2,   s = -2S + 3S^2.
  Offener Kanal a (k = sqrt(nu^2 - 1)), geschlossener Kanal b (kappa = sqrt(1 - (2 omega - nu)^2)).
  Je Ball und Paritaet p: einlaufende Amplitude D_p und Streuanteil T_p, tau_p = T_p / D_p = (S_p - 1)/2, aus dem
  Anschluss bei x = 4 (zwei Regulaerloesungen ab 0, drei Jost-Loesungen ab R, Cramer-Minoren; alles analytisch in nu).
  Mehrere Baelle: exakte Vielfachstreuung im offenen Kanal (Foldy-Lax). Unbekannte je Ball: gerade und ungerade
  Streuamplitude E_j, O_j. D_e,j E_j = T_e,j (alpha_j + beta_j), D_o,j O_j = T_o,j (alpha_j - beta_j), alpha/beta =
  von links/rechts einlaufende Amplitude aus den anderen Baellen (und einer Pumpe). Vernachlaessigt werden nur die
  Kopplung ueber den geschlossenen Kanal (~ e^{-0,75 d}) und die Ueberlappung der Auslaeufer (~ e^{-0,55 d}); fuer
  d >= 30 beide unter 1e-7, also weit unter Gamma0 = 6,7e-5.
  Pole = Nullstellen von det K(nu), Newton mit Jacobi-Formel d ln det K = tr(K^-1 K'). Abklingrate = -Im nu.
  Einzelball-Funktionen werden auf einem Kreis um nu_c = omega + 1,49378 tabelliert (Taylor per FFT, 32 Punkte).
  Anker: Einzelpol gegen Codex rho = 1,49377696454877 - 6,71596847535e-5 i.
  Markov-Modell (CMT) als Saat und fuer das Ueberleben einer Anregung des Mittelballs:
      H = diag(nu_j) - i sqrt(g_j g_l) e^{i k |x_j - x_l|}  (j != l, nur resonante Baelle).

ZEIT (R-2 in der vollen nichtlinearen Dynamik, R-4). Velocity-Verlet mit dx = 0,1 und dt = 0,05 (fein halbiert),
  quadratische Daempfungsschicht (sigma0 = 1, 40 breit), Box [-150, 150]: aus tests1d.py unveraendert. Neu nur:
  Rand ohne Schwamm (Spiegel = fester Rand), periodischer Ring (Laplace mit roll), groessere Box [-300, 300];
  ladungserhaltende Anregung durch Streckung psi = sqrt(lam) f(lam (x - x_j)), lam = 1 +- 1e-3; Messung |psi|^2 in
  der Ballmitte, Demodulation bei der gemessenen Atemfrequenz (Hann-Fenster 100), Huellenfit ab t = 200.

Unterbefehle: rauch, r1, r2, r2zeit, r3, r4, r5 (siehe PLAN.md).
Aufruf:  python reflexion.py <unterbefehl> [--geraet cuda|cpu] [--out ORDNER] [--faeden N]
"""
import argparse
import datetime
import json
import math
import os
import time
import traceback

import torch

DEV = torch.device("cpu")          # wird in main() nach --geraet gesetzt
F64, C128 = torch.float64, torch.complex128
PI = math.pi
SPEICHER_GB = 1.5
MAX_SEK = 540.0                    # kleintest.sh bricht bei 600 s ab: danach keine neue Stufe, Zeitlaeufe gekuerzt
T_START = time.perf_counter()
HINWEISE = []
STUFEN = ("grob", "fein")         # --stufen grob: nur die grobe Stufe (lokale Probe)
T_UEBER = None                     # --T: Laufzeit der Zeitteile ueberschreiben (lokale Probe)

# ---- Modell und Anker ----
W2 = 0.70
RHO_CODEX = complex(1.49377696454877, -6.71596847535e-5)     # resonance-20260930/ERGEBNIS.txt
NU_C = math.sqrt(W2) + RHO_CODEX.real                         # Tabellenmitte (physikalische Frequenz, reell)
GAMMA0 = -RHO_CODEX.imag                                      # Einheit aller Abklingraten (Amplitude)
TOL_ANKER = 1e-7                                              # |rho - rho_Codex|, Stufe grob

# ---- linear ----
X_M = 4.0                                                     # Anschlusspunkt wie Codex
NUMERIK = {"grob": (0.01, 24.0), "fein": (0.005, 32.0)}      # (RK4-Schritt h, Jost-Radius R); L3 = grob gegen fein
M_KREIS, R_KREIS = 32, 0.03
R_GUELTIG = 0.4 * R_KREIS                                     # Taylorfehler dort ~ 0,4^32 = 2e-13
T_UEBERLEBEN = (1.0, 5.0, 20.0)                               # in Einheiten 1/Gamma0
D_ZIEL = 36.0                                                 # Abstaende um 36: Auslaeuferkraft ~ 6e-9
R1_M = (1, 2, 5, 10, 20)                                      # Kettenbaelle je Seite
R1_W2_NR = 0.60                                               # nichtresonanter Kettenball (Gegenprobe echte Bragg-Luecke)
R2_W2_GEGEN = 0.69                                            # verstimmter Partner (Gegenprobe R-2)
R3_D = (30.0, 33.0, 0.05)
R3_NU_OFF = (2.25, 2.10)
R5_N = (2, 5, 10, 20)                                         # Gasbaelle je Seite
R5_SEEDS = (1, 2, 3, 4, 5)
R5_ABST = (30.0, 45.0)
R5_W2_GEMISCHT = (0.65, 0.66, 0.67, 0.68, 0.69, 0.71, 0.72, 0.73, 0.74, 0.75)
R5_PERIODE = 37.5

# ---- Zeit (aus tests1d.py) ----
L_BOX, SIGMA0, SCHWAMM_BREITE = 150.0, 1.0, 40.0
DX, DT, FEIN = 0.1, 0.05, 0.5
T_MESS = 0.5
EPS_DIL = 1e-3
BAND_OM = (1.3, 1.7)
NORMAL = {"T": 1500.0, "tw": 100.0, "schritt": 50.0, "t_fit0": 200.0, "t_om": 100.0}
KLEIN = {"T": 75.0, "tw": 20.0, "schritt": 10.0, "t_fit0": 10.0, "t_om": 10.0}


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def uhr():
    if DEV.type == "cuda":
        torch.cuda.synchronize()
    return time.perf_counter()


def rest_sek():
    return MAX_SEK - (time.perf_counter() - T_START)


def l3(grob, fein, null):
    """Latte L3: Effekt (Abstand vom Nullwert) mindestens fuenfmal so gross wie die Aenderung grob -> fein."""
    if not (math.isfinite(grob) and math.isfinite(fein)):
        return {"grob": grob, "fein": fein, "bestanden": False}
    eff, aend = abs(grob - null), abs(fein - grob)
    return {"grob": grob, "fein": fein, "effekt": eff, "aenderung": aend, "bestanden": bool(eff >= 5.0 * aend)}


def fz(v, fmt=".3e"):
    try:
        return format(v, fmt) if v is not None and math.isfinite(v) else str(v)
    except (TypeError, ValueError):
        return str(v)


def median(werte):
    w = sorted(v for v in werte if v is not None and math.isfinite(v))
    if not w:
        return float("nan")
    n = len(w)
    return w[n // 2] if n % 2 else 0.5 * (w[n // 2 - 1] + w[n // 2])


def ball_par(w2):
    a0 = 1.0 - w2
    return a0, math.sqrt(2.0 * w2 - 1.0), math.sqrt(w2)


def f_mitte(w2):
    a0, b0, _ = ball_par(w2)
    return math.sqrt(2.0 * a0 / (1.0 + b0))


def auslaeuferkraft(d, w2=W2):
    """Kraft zwischen zwei gleichphasigen Baellen aus dem Impulsfluss in der Mitte (Papier, fuer grosses d):
    T_xx = -4 kappa^2 A^2 e^{-kappa d}, A = 2 sqrt(a0/b0), kappa = sqrt(a0); anziehend."""
    a0, b0, _ = ball_par(w2)
    return 16.0 * a0 * a0 / b0 * math.exp(-math.sqrt(a0) * d)


# ================================================================ LINEAR: Einzelball

def _rhs(x, y, a0, b0, nu2, mu2):
    S = 2.0 * a0 / (1.0 + b0 * torch.cosh(2.0 * torch.sqrt(a0) * x))     # [B]
    D = 1.0 - 4.0 * S + 4.5 * S * S
    s = (-2.0 * S + 3.0 * S * S).unsqueeze(1)
    va = (D - nu2).unsqueeze(1)
    vb = (D - mu2).unsqueeze(1)
    a, b = y[..., 0], y[..., 1]
    return torch.stack([y[..., 2], y[..., 3], va * a + s * b, s * a + vb * b], dim=-1)


def _rk4(y, x0, x1, n, par):
    h = (x1 - x0) / n
    for i in range(n):
        x = x0 + i * h
        k1 = _rhs(x, y, *par)
        k2 = _rhs(x + 0.5 * h, y + (0.5 * h) * k1, *par)
        k3 = _rhs(x + 0.5 * h, y + (0.5 * h) * k2, *par)
        k4 = _rhs(x + h, y + h * k3, *par)
        y = y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    return y


def ball_funktionen(w2, nu, par, h, R):
    """Je Eintrag b: Ball omega^2 = w2[b] bei physikalischer Frequenz nu[b], Paritaet par[b] (0 gerade, 1 ungerade).

    Spalten (a, b, a', b') bei x_m: r1, r2 regulaer ab 0; J_in = e^{-ik(x-R)}, J_out = e^{ik(x-R)}, J_b = e^{-kappa(x-x_m)}
    (b-Kanal) ab R. Nullvektor der 4x5-Matrix [r1, r2, -J_in, -J_out, -J_b] ueber Minoren v_i:
    v1 r1 + v2 r2 = v3 J_in + v4 J_out + v5 J_b. Einlaufend a_in = v3 e^{ikR}, auslaufend a_out = v4 e^{-ikR}.
    S_gerade = a_out / a_in, S_ungerade = -a_out / a_in. Rueckgabe D = a_in, T = (S a_in - a_in)/2, G = Kernamplitude
    (|a(0)| + |b(0)|) je einlaufender Amplitude (nur gerade sinnvoll), S."""
    w2 = w2.to(device=DEV, dtype=F64)
    nu = nu.to(device=DEV, dtype=C128)
    par = par.to(device=DEV)
    a0 = 1.0 - w2
    b0 = torch.sqrt(2.0 * w2 - 1.0)
    om = torch.sqrt(w2)
    mu = 2.0 * om - nu
    nu2, mu2 = nu * nu, mu * mu
    k = torch.sqrt(nu2 - 1.0)
    kap = torch.sqrt(1.0 - mu2)
    bn = nu.shape[0]
    gerade = par == 0
    reg = torch.zeros(bn, 2, 4, dtype=C128, device=DEV)
    reg[:, 0, 0] = gerade.to(C128)
    reg[:, 0, 2] = (~gerade).to(C128)
    reg[:, 1, 1] = gerade.to(C128)
    reg[:, 1, 3] = (~gerade).to(C128)
    pr = (a0, b0, nu2, mu2)
    reg = _rk4(reg, 0.0, X_M, int(round(X_M / h)), pr)
    jo = torch.zeros(bn, 3, 4, dtype=C128, device=DEV)
    eb = torch.exp(-kap * (R - X_M))
    jo[:, 0, 0] = 1.0
    jo[:, 0, 2] = -1j * k
    jo[:, 1, 0] = 1.0
    jo[:, 1, 2] = 1j * k
    jo[:, 2, 1] = eb
    jo[:, 2, 3] = -kap * eb
    jo = _rk4(jo, R, X_M, int(round((R - X_M) / h)), pr)
    r1, r2 = reg[:, 0], reg[:, 1]
    ji, jout, jb = jo[:, 0], jo[:, 1], jo[:, 2]

    def det(c1, c2, c3, c4):
        return torch.linalg.det(torch.stack([c1, c2, c3, c4], dim=-1))
    v1 = det(r2, ji, jout, jb)
    v2 = -det(r1, ji, jout, jb)
    v3 = -det(r1, r2, jout, jb)
    v4 = det(r1, r2, ji, jb)
    a_in = v3 * torch.exp(1j * k * R)
    a_out = v4 * torch.exp(-1j * k * R)
    sig = torch.where(gerade, torch.ones_like(a_in), -torch.ones_like(a_in))
    return {"D": a_in, "T": 0.5 * (sig * a_out - a_in), "G": (v1.abs() + v2.abs()) / a_in.abs(),
            "S": sig * a_out / a_in, "k": k}


class Tabelle:
    """Einzelball-Funktionen D, T (gerade, ungerade) je Balltyp als Taylorreihe um NU_C (FFT auf dem Kreis)."""

    def __init__(self, w2_typen, h, R, m=M_KREIS, r=R_KREIS):
        self.w2, self.h, self.R, self.m, self.r = list(w2_typen), h, R, m, r
        nt = len(self.w2)
        t0 = uhr()
        j = torch.arange(m, device=DEV).to(F64)
        nus = NU_C + r * torch.exp(2j * PI * j / m)
        w2b = torch.tensor(self.w2, dtype=F64, device=DEV).repeat_interleave(2 * m)      # (typ, par, j)
        parb = torch.arange(2, device=DEV).repeat_interleave(m).repeat(nt)
        f = ball_funktionen(w2b, nus.repeat(2 * nt), parb, h, R)
        werte = torch.stack([f["D"], f["T"]], dim=0).reshape(2, nt, 2, m).permute(1, 2, 0, 3)   # [typ, par, fn, j]
        self.n = torch.arange(m, device=DEV).to(F64)
        self.koef = torch.fft.fft(werte, dim=-1) / m / (r ** self.n).to(C128)
        self.sek = uhr() - t0
        self.ode_schritte = int(round(X_M / h)) + int(round((R - X_M) / h))
        self.pole = [self.einzelpol(i) for i in range(nt)]

    def werte(self, nu):
        """F und F' bei komplexem nu: je [typ, par, fn] mit fn 0 = D, 1 = T."""
        z = torch.as_tensor(nu, dtype=C128, device=DEV).reshape(1) - NU_C
        pw = torch.cumprod(torch.cat([torch.ones(1, dtype=C128, device=DEV), z.expand(self.m - 1)]), dim=0)
        F = (self.koef * pw).sum(-1)
        dF = (self.koef[..., 1:] * self.n[1:] * pw[:-1]).sum(-1)
        return F, dF

    def einzelpol(self, i):
        nu = torch.tensor(complex(NU_C, -GAMMA0), dtype=C128, device=DEV)
        d = torch.tensor(1.0, dtype=C128, device=DEV)
        for it in range(60):
            F, dF = self.werte(nu)
            d = -F[i, 0, 0] / dF[i, 0, 0]
            if d.abs().item() > 2e-3:
                d = d * (2e-3 / d.abs().item())
            nu = nu + d
            if (nu - NU_C).abs().item() > 0.5 * self.r or d.abs().item() < 1e-14:
                break
        z = complex(nu.item())
        ok = d.abs().item() < 1e-10 and abs(z - NU_C) <= R_GUELTIG
        return {"w2": self.w2[i], "nu": z, "rho": z - math.sqrt(self.w2[i]), "gamma_rel": -z.imag / GAMMA0,
                "resonant": bool(ok), "iter": it}


def tabelle_fuer(w2s, stufe, klein):
    if klein:
        return Tabelle(w2s, 0.02, 20.0, m=16)
    h, R = NUMERIK[stufe]
    return Tabelle(w2s, h, R)


def anker(tab):
    """Einzelpol omega^2 = 0,7 gegen Codex; direkter Rest |D/D'| der ODE am Tabellenpol."""
    p = tab.pole[0]
    nu = torch.tensor(p["nu"], dtype=C128, device=DEV)
    f = ball_funktionen(torch.tensor([W2, W2], dtype=F64), torch.stack([nu, nu + 1e-7]), torch.tensor([0, 0]),
                        tab.h, tab.R)
    d0, d1 = f["D"][0], f["D"][1]
    rest = (d0 / ((d1 - d0) / 1e-7)).abs().item()
    abw = abs(p["rho"] - RHO_CODEX)
    return {"rho": p["rho"], "abw_codex": abw, "abw_im_rel": abs(p["rho"].imag - RHO_CODEX.imag) / GAMMA0,
            "direkt_rest": rest, "bestanden": bool(abw <= TOL_ANKER and rest <= 1e-9), "h": tab.h, "R": tab.R,
            "m": tab.m, "tabelle_sek": tab.sek, "ode_schritte": tab.ode_schritte}


def anker_text(a):
    return (f"  Anker (h = {a['h']}, R = {a['R']}, m = {a['m']}): rho = {a['rho'].real:.11f} {a['rho'].imag:+.6e} i, "
            f"|rho - Codex| = {a['abw_codex']:.1e}, |dIm|/Gamma0 = {a['abw_im_rel']:.1e}, direkter ODE-Rest "
            f"{a['direkt_rest']:.1e} -> {'bestanden' if a['bestanden'] else 'NICHT bestanden'} "
            f"(Tabelle {a['tabelle_sek']:.1f} s, {a['ode_schritte']} RK4-Schritte)")


# ================================================================ LINEAR: Vielfachstreuung (Foldy-Lax)

def ball_werte(tab, typen, nu):
    """(D_e, T_e, D_o, T_o) und Ableitungen je Streuer bei nu; Typ -1 = fester Spiegel (r = -1, t = 0)."""
    F, dF = tab.werte(nu)
    ti = torch.tensor([max(t, 0) for t in typen], device=DEV)
    wand = torch.tensor([t < 0 for t in typen], device=DEV)
    W, dW = F[ti], dF[ti]
    eins = torch.ones(len(typen), dtype=C128, device=DEV)
    null = torch.zeros_like(eins)
    w = (torch.where(wand, eins, W[:, 0, 0]), torch.where(wand, -eins, W[:, 0, 1]),
         torch.where(wand, eins, W[:, 1, 0]), torch.where(wand, null, W[:, 1, 1]))
    dw = tuple(torch.where(wand, null, dW[:, p, q]) for p, q in ((0, 0), (0, 1), (1, 0), (1, 1)))
    return w, dw


def fl_matrix(nu, x, w, dw=None):
    """Foldy-Lax-Matrix K (2N x 2N, Zeilen/Spalten 2j = gerade, 2j+1 = ungerade) und dK/dnu."""
    de, te, do_, to = w
    n = x.shape[0]
    k = torch.sqrt(nu * nu - 1.0)
    xi, xj = x.unsqueeze(0), x.unsqueeze(1)                    # [j, i] = Zeile Ball j, Spalte Ball i
    dist = (xi - xj).abs().to(C128)
    lm = (xi < xj).to(C128)
    um = (xi > xj).to(C128)
    P = torch.exp(1j * k * dist)
    spl, smi = (lm + um) * P, (lm - um) * P
    K = torch.zeros(2 * n, 2 * n, dtype=C128, device=DEV)
    K[0::2, 0::2] = torch.diag(de) - te[:, None] * spl
    K[0::2, 1::2] = -te[:, None] * smi
    K[1::2, 0::2] = -to[:, None] * smi
    K[1::2, 1::2] = torch.diag(do_) - to[:, None] * spl
    if dw is None:
        return K, None
    dde, dte, ddo, dto = dw
    dP = 1j * (nu / k) * dist * P
    dspl, dsmi = (lm + um) * dP, (lm - um) * dP
    Kp = torch.zeros_like(K)
    Kp[0::2, 0::2] = torch.diag(dde) - dte[:, None] * spl - te[:, None] * dspl
    Kp[0::2, 1::2] = -dte[:, None] * smi - te[:, None] * dsmi
    Kp[1::2, 0::2] = -dto[:, None] * smi - to[:, None] * dsmi
    Kp[1::2, 1::2] = torch.diag(ddo) - dto[:, None] * spl - to[:, None] * dspl
    return K, Kp


def newton_pol(nu0, x, tab, typen, max_it=60):
    nu = torch.tensor(complex(nu0), dtype=C128, device=DEV)
    d = torch.tensor(1.0, dtype=C128, device=DEV)
    for _ in range(max_it):
        w, dw = ball_werte(tab, typen, nu)
        K, Kp = fl_matrix(nu, x, w, dw)
        try:
            spur = torch.diagonal(torch.linalg.solve(K, Kp)).sum()
        except RuntimeError:                                   # exakt singulaer: Pol getroffen
            return complex(nu.item()), True
        d = -1.0 / spur
        if d.abs().item() > 1e-3:
            d = d * (1e-3 / d.abs().item())
        nu = nu + d
        if (nu - NU_C).abs().item() > 0.5 * R_KREIS:
            return complex(nu.item()), False
        if d.abs().item() < 1e-13:
            break
    return complex(nu.item()), bool(d.abs().item() < 1e-9)


def pol_details(nu, x, tab, typen, zentral):
    """Nullvektoren (SVD), Gewicht der geraden Amplituden je Ball, Residuum von [K^-1] am Mittelball."""
    nut = torch.tensor(nu, dtype=C128, device=DEV)
    w, dw = ball_werte(tab, typen, nut)
    K, Kp = fl_matrix(nut, x, w, dw)
    U, S, Vh = torch.linalg.svd(K)
    v = Vh[-1].conj()
    u = U[:, -1].conj()
    E, O = v[0::2], v[1::2]
    gew = (E.abs() ** 2) / (E.abs() ** 2).sum().clamp(min=1e-300)
    res = v[2 * zentral] * u[2 * zentral] / (u @ (Kp @ v))
    return {"E": E, "O": O, "gewicht": gew, "residuum": complex(res.item()), "smin_rel": (S[-1] / S[0]).item()}


def hintergrund(tab):
    """Bei nu_r = Re(Einzelpol 0,7): S_e, S_o je Typ; Hintergrundphase e^{2 i delta_e} = -S_e(nu_r) (resonante Typen,
    weil S_e = e^{2 i delta_e} (nu - conj nu1)/(nu - nu1) bei nu_r gleich -e^{2 i delta_e} ist)."""
    nu_r = torch.tensor(complex(tab.pole[0]["nu"].real, 0.0), dtype=C128, device=DEV)
    F, _ = tab.werte(nu_r)
    s_e = 1.0 + 2.0 * F[:, 0, 1] / F[:, 0, 0]
    s_o = 1.0 + 2.0 * F[:, 1, 1] / F[:, 1, 0]
    return s_e, s_o


def cmt_matrix(x, tab, typen):
    """Markov-Modell der resonanten Baelle (Einzelpol in der Tabelle), in geraden Streuamplituden E_j:
    H_jj = nu1_j, H_ji = -i g_j e^{2 i delta_e,j} e^{i k |x_i - x_j|} prod(t_bg der Baelle dazwischen).
    t_bg = (e^{2 i delta_e} + S_o)/2 fuer resonante, (S_e + S_o)/2 fuer nichtresonante Baelle, 0 fuer Spiegel.
    Positionen muessen aufsteigend sortiert sein."""
    res = [j for j, t in enumerate(typen) if t >= 0 and tab.pole[t]["resonant"]]
    if not res:
        return None, []
    xl = x.tolist()
    if any(xl[i + 1] <= xl[i] for i in range(len(xl) - 1)):
        raise ValueError("Positionen nicht aufsteigend sortiert")
    s_e, s_o = hintergrund(tab)
    tb = []
    for t in typen:
        if t < 0:
            tb.append(0j)
        elif tab.pole[t]["resonant"]:
            tb.append(complex((0.5 * (-s_e[t] + s_o[t])).item()))
        else:
            tb.append(complex((0.5 * (s_e[t] + s_o[t])).item()))
    kr = math.sqrt(tab.pole[0]["nu"].real ** 2 - 1.0)
    n = len(res)
    H = torch.zeros(n, n, dtype=C128, device=DEV)
    for a, j in enumerate(res):
        pj = tab.pole[typen[j]]
        H[a, a] = pj["nu"]
        phase_j = complex((-s_e[typen[j]]).item())
        for b, i in enumerate(res):
            if i == j:
                continue
            prod = 1.0 + 0j
            for m in range(min(i, j) + 1, max(i, j)):
                prod *= tb[m]
            H[a, b] = -1j * (-pj["nu"].imag) * phase_j * complex(math.cos(kr * abs(xl[i] - xl[j])),
                                                                 math.sin(kr * abs(xl[i] - xl[j]))) * prod
    return H, res


def ueberleben_cmt(H, res, zentral):
    ic = res.index(zentral)
    n = len(res)
    nr = H[ic, ic].real
    e0 = torch.zeros(n, dtype=C128, device=DEV)
    e0[ic] = 1.0
    eye = torch.eye(n, dtype=C128, device=DEV)
    aus = []
    for tt in T_UEBERLEBEN:
        c = torch.linalg.matrix_exp(-1j * (H - nr * eye) * (tt / GAMMA0)) @ e0
        aus.append({"t_mal_gamma0": tt, "zentral": (c[ic].abs() ** 2).item(), "gesamt": (c.abs() ** 2).sum().item()})
    return aus


def alle_pole(x, tab, typen, zentral):
    """Saaten aus dem Markov-Modell und aus der um nu_ref linearisierten Foldy-Lax-Matrix, dann Newton."""
    saat = []
    H, res = cmt_matrix(x, tab, typen)
    if H is not None:
        saat += [complex(z) for z in torch.linalg.eigvals(H).tolist()]
    nu_ref = torch.tensor(complex(tab.pole[max(typen[zentral], 0)]["nu"].real, 0.0), dtype=C128, device=DEV)
    try:
        w, dw = ball_werte(tab, typen, nu_ref)
        K0, K1 = fl_matrix(nu_ref, x, w, dw)
        lam = torch.linalg.eigvals(-torch.linalg.solve(K1, K0))
        saat += [complex(z) for z in (nu_ref + lam).tolist() if abs(z - NU_C) <= R_GUELTIG and z.imag < 1e-7]
    except RuntimeError:
        HINWEISE.append("linearisierte Saat entfallen (K' singulaer)")
    pole, fehl = [], 0
    for i, s in enumerate(saat):
        z, ok = newton_pol(s + 1e-8 * ((i % 5) - 2) * (1.0 - 0.5j), x, tab, typen)
        if not ok or abs(z - NU_C) > R_GUELTIG:
            fehl += 1
            continue
        if all(abs(z - p) > 1e-9 for p in pole):
            pole.append(z)
    return sorted(pole, key=lambda p: -p.imag), fehl, H, res


def auswerten_konfig(xl, typen, zentral, tab, ueberleben=True):
    """Alle Pole einer Anordnung; Abklingraten in Einheiten Gamma0; Ueberleben einer Anregung des Mittelballs (CMT)."""
    if rest_sek() < 25.0:
        HINWEISE.append(f"Anordnung mit {len(xl)} Baellen uebersprungen (Restzeit {rest_sek():.0f} s)")
        return {"n_baelle": len(xl), "n_resonant": 0, "n_pole": 0, "newton_fehl": 0, "uebersprungen": True,
                "gamma_min": float("nan"), "gamma_max": float("nan"), "gamma_c": float("nan"), "w_c": float("nan"),
                "n_dunkel": 0}
    x = torch.tensor(xl, dtype=F64, device=DEV)
    pole, fehl, H, res = alle_pole(x, tab, typen, zentral)
    zeile = {"n_baelle": len(xl), "n_resonant": len(res), "n_pole": len(pole), "newton_fehl": fehl}
    if not pole:
        zeile.update({"gamma_min": float("nan"), "gamma_max": float("nan"), "gamma_c": float("nan"), "w_c": float("nan"),
                      "n_dunkel": 0})
        return zeile
    det = [pol_details(p, x, tab, typen, zentral) for p in pole]
    gam = [-p.imag / GAMMA0 for p in pole]
    wc = [d["gewicht"][zentral].item() for d in det]
    ib = max(range(len(pole)), key=lambda i: wc[i])
    zeile.update({"gamma_min": min(gam), "gamma_max": max(gam), "gamma_c": gam[ib], "w_c": wc[ib],
                  "nu_c_pol": pole[ib], "n_dunkel": sum(1 for g in gam if g < 0.01),
                  "gammas": sorted(gam), "pole": pole})
    # exakte Polsumme des Mittelball-Ansprechens (nur verlaesslich ohne Beinahe-Entartung): Summenregel pruefen
    F, dF = tab.werte(torch.tensor(tab.pole[0]["nu"], dtype=C128, device=DEV))
    r_einzel = 1.0 / complex(dF[0, 0, 0].item())
    nr = tab.pole[0]["nu"].real
    summe = sum(d["residuum"] for d in det)
    zeile["summenregel"] = abs(summe / r_einzel)
    zeile["ueberleben_polsumme"] = [abs(sum(d["residuum"] * complex(math.cos(-(p.real - nr) * tt / GAMMA0),
                                                                    math.sin(-(p.real - nr) * tt / GAMMA0))
                                            * math.exp(p.imag * tt / GAMMA0) for d, p in zip(det, pole)) / r_einzel) ** 2
                                    for tt in T_UEBERLEBEN]
    if H is not None and ueberleben and zentral in res:
        zeile["ueberleben_cmt"] = ueberleben_cmt(H, res, zentral)
        ev = torch.linalg.eigvals(H).tolist()
        zeile["cmt_gegen_exakt"] = max(min(abs(e - p) for p in pole) for e in ev) / GAMMA0
    return zeile


def zwei_ball(tab, d, typen=(0, 0)):
    """Zwei Baelle bei -d/2, +d/2: Pole, Modus (sym/anti aus den geraden Amplituden), Nullvektor."""
    x = torch.tensor([-0.5 * d, 0.5 * d], dtype=F64, device=DEV)
    H, _ = cmt_matrix(x, tab, list(typen))
    saat = [complex(z) for z in torch.linalg.eigvals(H).tolist()] if H is not None else [complex(NU_C, -GAMMA0)]
    aus = []
    for s in saat:
        z, ok = newton_pol(s, x, tab, list(typen))
        if not ok:
            aus.append({"nu": z, "ok": False, "modus": "?"})
            continue
        det = pol_details(z, x, tab, list(typen), 0)
        e0, e1 = det["E"][0], det["E"][1]
        modus = "sym" if (e0 - e1).abs().item() < (e0 + e1).abs().item() else "anti"
        aus.append({"nu": z, "ok": True, "modus": modus, "gewicht": [g.item() for g in det["gewicht"]],
                    "E": [complex(v) for v in det["E"].tolist()], "O": [complex(v) for v in det["O"].tolist()]})
    return aus


def gam_modus(tab, d, modus):
    for p in zwei_ball(tab, d):
        if p["ok"] and p["modus"] == modus:
            return -p["nu"].imag / GAMMA0
    return 1e9


def golden(f, a, b, n):
    g = (math.sqrt(5.0) - 1.0) / 2.0
    c, d = b - g * (b - a), a + g * (b - a)
    fc, fd = f(c), f(d)
    for _ in range(n):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - g * (b - a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + g * (b - a)
            fd = f(d)
    return 0.5 * (a + b)


def dunkler_abstand(tab, ziel, modus, n_gold):
    """Abstand nahe ziel, an dem der Modus (anti: k d = 2 pi n, sym: k d = (2n+1) pi im Markov-Bild) am
    langsamsten abklingt; Goldener Schnitt in [d0 - lambda/4, d0 + lambda/4]."""
    kr = math.sqrt(tab.pole[0]["nu"].real ** 2 - 1.0)
    per = 2.0 * PI / kr
    d0 = round(ziel / per) * per if modus == "anti" else (math.floor(ziel / per) + 0.5) * per
    s_e, _ = hintergrund(tab)
    dm = d0 - math.atan2((-s_e[0]).imag.item(), (-s_e[0]).real.item()) / kr     # Markov mit Hintergrundphase
    d_opt = golden(lambda d: gam_modus(tab, d, modus), dm - 0.25 * per, dm + 0.25 * per, n_gold)
    return d_opt, gam_modus(tab, d_opt, modus), d0


def streu_loesung(nu, x, w, inc_r, inc_l):
    """Stationaere Streuung bei reellem nu mit Pumpe inc_r e^{ikx} (von links) + inc_l e^{-ikx} (von rechts)."""
    K, _ = fl_matrix(nu, x, w)
    _, te, _, to = w
    k = torch.sqrt(nu * nu - 1.0)
    ai = inc_r * torch.exp(1j * k * x)
    bi = inc_l * torch.exp(-1j * k * x)
    rhs = torch.zeros(2 * x.shape[0], dtype=C128, device=DEV)
    rhs[0::2] = te * (ai + bi)
    rhs[1::2] = to * (ai - bi)
    v = torch.linalg.solve(K, rhs)
    return v[0::2], v[1::2], ai, bi


def kraefte(nu, x, E, O, inc_r, inc_l, ai=None, bi=None):
    """Zeitgemittelte Kraft je Ball aus dem Impulsfluss T_xx = 2 k^2 (|A|^2 + |B|^2) links minus rechts (je Pumpe^2);
    dazu die gesamte gerade einlaufende Amplitude alpha + beta je Ball."""
    k = torch.sqrt(nu * nu - 1.0)
    er = (E + O) * torch.exp(-1j * k * x)          # Anteil an e^{ikx} rechts von Ball i
    el = (E - O) * torch.exp(1j * k * x)           # Anteil an e^{-ikx} links von Ball i
    xi, xj = x.unsqueeze(0), x.unsqueeze(1)
    lt, le, gt, ge = [m.to(C128) for m in ((xi < xj), (xi <= xj), (xi > xj), (xi >= xj))]
    a_l = inc_r + (lt * er).sum(1)
    b_l = inc_l + (ge * el).sum(1)
    a_r = inc_r + (le * er).sum(1)
    b_r = inc_l + (gt * el).sum(1)
    k2 = 2.0 * (k * k).real
    F = k2 * (a_l.abs() ** 2 + b_l.abs() ** 2 - a_r.abs() ** 2 - b_r.abs() ** 2)
    ab = None
    if ai is not None:
        P = torch.exp(1j * k * (xi - xj).abs())
        ab = ai + (lt * P * (E + O)).sum(1) + bi + (gt * P * (E - O)).sum(1)
    return F, ab


# ================================================================ ZEIT (Schritt aus tests1d.py)

def gitter(dx, L=L_BOX, ring=False):
    if ring:
        return torch.arange(int(round(2.0 * L / dx)), dtype=F64, device=DEV) * dx - L
    i0 = int(round(L / dx))
    return (torch.arange(2 * i0 + 1, dtype=F64, device=DEV) - i0) * dx


def schwamm(x, L, an=True):
    if not an:
        return torch.zeros_like(x)
    return SIGMA0 * ((x.abs() - (L - SCHWAMM_BREITE)).clamp(min=0.0) / SCHWAMM_BREITE) ** 2


def ball_zeit(x, w2, xc, lam=1.0, theta=0.0):
    """Ruhender Ball, ladungserhaltend gestreckt: psi = sqrt(lam) f(lam (x - xc)) e^{i theta}, psi_t = -i omega psi."""
    a0, b0, w = ball_par(w2)
    y = lam * (x - xc)
    f = math.sqrt(lam) * torch.sqrt(2.0 * a0 / (1.0 + b0 * torch.cosh(2.0 * math.sqrt(a0) * y)))
    psi = f.to(C128) * complex(math.cos(theta), math.sin(theta))
    return psi, -1j * w * psi


def stapel(felder, ring):
    psi = torch.stack([p for p, _ in felder])
    vel = torch.stack([v for _, v in felder])
    if not ring:
        for a in (psi, vel):
            a[:, 0] = 0.0
            a[:, -1] = 0.0
    return psi, vel


def messer(x, dx, zentren):
    """|psi|^2 an zwei Ballmitten (naechster Gitterpunkt) und Ladung in |x| < 30."""
    idx = torch.tensor([[int(round((c - x[0].item()) / dx)) for c in z] for z in zentren], device=DEV)
    kern = (x.abs() < 30.0).to(F64)

    def messen(psi, vel):
        s = psi.real ** 2 + psi.imag ** 2
        q = (2.0 * (psi * vel.conj()).imag * kern).sum(1, keepdim=True) * dx
        return torch.cat([s.gather(1, idx), q], dim=1)
    return messen


def entwickeln(psi, vel, dx, dt, t_end, t_mess, messen, sigma, ring=False):
    """Velocity-Verlet aus tests1d.py; neu: periodischer Laplace (ring) und Daempfung je Lauf (sigma [B, N])."""
    def kraft(psi):
        if ring:
            lap = (torch.roll(psi, -1, 1) - 2.0 * psi + torch.roll(psi, 1, 1)) / (dx * dx)
        else:
            fluss = (psi[:, 1:] - psi[:, :-1]) / dx
            lap = torch.zeros_like(psi)
            lap[:, 1:-1] = (fluss[:, 1:] - fluss[:, :-1]) / dx
        s = psi.real ** 2 + psi.imag ** 2
        return lap - (1.0 - 2.0 * s + 1.5 * s * s) * psi

    n_schritte = int(round(t_end / dt))
    alle = max(1, int(round(t_mess / dt)))
    reihe = [messen(psi, vel)]
    kr = kraft(psi)
    gekuerzt = False
    for n in range(1, n_schritte + 1):
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        psi = psi + dt * vel
        kr = kraft(psi)
        vel = vel + (0.5 * dt) * (kr - sigma * vel)
        if n % alle == 0:
            reihe.append(messen(psi, vel))
            if n % (alle * 400) == 0 and rest_sek() < 5.0:
                gekuerzt = True
                break
    daten = torch.stack(reihe)
    if not bool(torch.isfinite(daten).all()):
        raise RuntimeError("nicht endliche Messwerte: Lauf instabil")
    t = torch.arange(daten.shape[0], dtype=F64, device=DEV) * (alle * dt)
    return t, daten, gekuerzt, n


def zeit_rechnen(name, bauen_liste, T):
    """Alle Teillaeufe erst grob, dann fein (dx/2, dt/2). bauen(dx) -> (x, felder, zentren, sigma, ring)."""
    aus = {}
    for stufe, dx, dt in (("grob", DX, DT), ("fein", DX * FEIN, DT * FEIN)):
        if stufe not in STUFEN:
            continue
        for teil, bauen in bauen_liste:
            if stufe == "fein":
                grob = aus.get((teil, "grob"))
                if grob is not None and rest_sek() < 2.3 * grob["sek"] + 10.0:
                    HINWEISE.append(f"{name}/{teil}: fein entfaellt (Restzeit {rest_sek():.0f} s)")
                    continue
            x, felder, zentren, sigma, ring = bauen(dx)
            psi, vel = stapel(felder, ring)
            t0 = uhr()
            t, daten, gek, n = entwickeln(psi, vel, dx, dt, T, T_MESS, messer(x, dx, zentren), sigma, ring)
            sek = uhr() - t0
            print(f"{name}/{teil} {stufe}: {psi.shape[0]} Laeufe x {psi.shape[1]} Punkte, T = {t[-1].item():.1f}, "
                  f"{sek:.1f} s, {1000.0 * sek / max(n, 1):.2f} ms je Schritt{' GEKUERZT' if gek else ''}", flush=True)
            if gek:
                HINWEISE.append(f"{name}/{teil} {stufe}: gekuerzt bei t = {t[-1].item():.0f}")
            aus[(teil, stufe)] = {"t": t, "daten": daten, "sek": sek, "ms_je_schritt": 1000.0 * sek / max(n, 1),
                                  "gekuerzt": gek}
    return aus


def spitze(t, y, t_ab, lo, hi, pad=8):
    """Groesste FFT-Spitze (Hann, Nullen aufgefuellt, Parabel) von y ab t_ab im Band [lo, hi]; Kreisfrequenz."""
    wahl = t >= t_ab - 1e-9
    ts, ys = t[wahl], y[wahl]
    n = ys.shape[0]
    if n < 32:
        return float("nan")
    ys = ys - ys.mean()
    fen = torch.hann_window(n, periodic=False, dtype=F64, device=DEV)
    nf = pad * n
    amp = torch.fft.rfft(ys * fen, n=nf).abs()
    d_om = 2.0 * PI / (nf * (ts[1] - ts[0]).item())
    om = torch.arange(amp.shape[0], device=DEV).to(F64) * d_om
    band = (om >= lo) & (om <= hi)
    if not bool(band.any()):
        return float("nan")
    i = int(torch.argmax(torch.where(band, amp, torch.zeros_like(amp))).item())
    delta = 0.0
    if 0 < i < amp.shape[0] - 1:
        a, b, c = amp[i - 1].item(), amp[i].item(), amp[i + 1].item()
        nen = a - 2.0 * b + c
        delta = 0.5 * (a - c) / nen if nen != 0.0 else 0.0
    return (i + delta) * d_om


def demod(t, y, om, tw, schritt):
    """Komplexe Amplitude bei om in Fenstern der Laenge tw (Hann), Fenstermittel abgezogen. y [M, K] -> [n, K]."""
    T = t[-1].item()
    mitten, amps = [], []
    a = 0.0
    while a + tw <= T + 1e-9:
        wahl = (t >= a - 1e-9) & (t <= a + tw + 1e-9)
        ts, ys = t[wahl], y[wahl]
        fen = torch.hann_window(ts.shape[0], periodic=False, dtype=F64, device=DEV)[:, None]
        sw = fen.sum()
        ym = (fen * ys).sum(0) / sw
        ph = torch.exp(1j * om * ts)[:, None]
        amps.append(2.0 * (fen * (ys - ym) * ph).sum(0) / sw)
        mitten.append(a + 0.5 * tw)
        a += schritt
    if not amps:
        return torch.zeros(0, dtype=F64, device=DEV), torch.zeros(0, y.shape[1], dtype=C128, device=DEV)
    return torch.tensor(mitten, dtype=F64, device=DEV), torch.stack(amps)


def huellenfit(tc, amp, t0, t1=None):
    """Gerade durch ln|A| ueber die Fenstermitten in [t0, t1]; Abklingrate in Einheiten Gamma0."""
    wahl = tc >= t0 - 1e-9
    if t1 is not None:
        wahl = wahl & (tc <= t1 + 1e-9)
    tt, a = tc[wahl], amp[wahl].abs()
    if tt.shape[0] < 3 or bool((a <= 0).any()):
        return {"gamma_rel": float("nan"), "rms_log": float("nan"), "n": int(tt.shape[0])}
    la = torch.log(a)
    tm, lm = tt.mean(), la.mean()
    steig = ((tt - tm) * (la - lm)).sum() / ((tt - tm) ** 2).sum()
    rest = la - (lm + steig * (tt - tm))
    return {"gamma_rel": -steig.item() / GAMMA0, "rms_log": rest.pow(2).mean().sqrt().item(), "n": int(tt.shape[0]),
            "amp_erst": a[0].item(), "amp_letzt": a[-1].item()}


# ================================================================ R-1 Bandlueckenschutz

def r1(klein):
    stufen = ("grob",) if klein else STUFEN
    ms = (1, 2) if klein else R1_M
    erg, text = {}, ["R-1 Bandlueckenschutz: Mittelball omega^2 = 0,7 bei x = 0, je M Kettenbaelle links und rechts."]
    for st in stufen:
        tab = tabelle_fuer([W2, R1_W2_NR], st, klein)
        an = anker(tab)
        kr = math.sqrt(tab.pole[0]["nu"].real ** 2 - 1.0)
        per = 2.0 * PI / kr
        d_b, g_b, d_b0 = dunkler_abstand(tab, D_ZIEL, "anti", 12 if klein else 40)
        arme = {"luecke_bragg": (d_b, 0), "verstimmt_lambda8": (d_b + per / 8.0, 0),
                "ohne_luecke_antibragg": (d_b + per / 4.0, 0), "nichtresonant_bragg": (d_b, 1)}
        F, _ = tab.werte(torch.tensor(complex(tab.pole[0]["nu"].real, 0.0), dtype=C128, device=DEV))
        s_e = 1.0 + 2.0 * F[1, 0, 1] / F[1, 0, 0]
        s_o = 1.0 + 2.0 * F[1, 1, 1] / F[1, 1, 0]
        r_nr = (0.5 * (s_e - s_o)).abs().item()
        zeilen = [{"arm": "allein", "M": 0, "d": 0.0, **auswerten_konfig([0.0], [0], 0, tab)}]
        for arm, (d, t) in arme.items():
            for m in ms:
                typen = [t] * (2 * m + 1)
                typen[m] = 0
                zeilen.append({"arm": arm, "M": m, "d": d,
                               **auswerten_konfig([j * d for j in range(-m, m + 1)], typen, m, tab)})
        erg[st] = {"anker": an, "k_r": kr, "lambda": per, "d_bragg": d_b, "d_bragg_markov": d_b0,
                   "gamma_zwei_ball_dunkel": g_b, "r_nichtresonant_bei_nu0": r_nr,
                   "pol_nichtresonant": tab.pole[1], "zeilen": zeilen}
        text.append(f" [{st}]")
        text.append(anker_text(an))
        text.append(f"  k(nu0) = {kr:.6f}, lambda = {per:.5f}; Bragg-Abstand exakt {d_b:.5f} (Markov {d_b0:.5f}); "
                    f"Kettenball {R1_W2_NR}: |r(nu0)| = {r_nr:.3e}, eigener Pol {tab.pole[1]['nu']:.6f} "
                    f"(resonant {tab.pole[1]['resonant']})")
        text.append("  Arm | M | d | Pole gefunden/resonant | Gamma_min | Gamma_c (Pol mit groesstem Mittelgewicht) | w_c "
                    "| dunkel (<0,01) | Ueberleben Mitte exakt (Polsumme) bei 1/5/20 x 1/Gamma0 | Summenregel | "
                    "Markov: Mitte | Markov: alle Baelle | Markov-exakt (Gamma0)")
        for z in zeilen:
            ub = z.get("ueberleben_cmt")
            ubt = "/".join(fz(u["zentral"], ".2e") for u in ub) if ub else "-"
            ubg = "/".join(fz(u["gesamt"], ".2e") for u in ub) if ub else "-"
            ups = "/".join(fz(u, ".2e") for u in z.get("ueberleben_polsumme", [])) or "-"
            text.append(f"  {z['arm']:22s} | {z['M']:2d} | {z['d']:.4f} | {z['n_pole']}/{z['n_resonant']} | "
                        f"{fz(z['gamma_min'])} | {fz(z['gamma_c'])} | {fz(z.get('w_c'), '.3f')} | {z['n_dunkel']} | "
                        f"{ups} | {fz(z.get('summenregel'), '.3f')} | {ubt} | {ubg} | {fz(z.get('cmt_gegen_exakt'), '.1e')}")
    if len(erg) == 2:
        l3l = []
        for zg, zf in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"]):
            l3l.append({"arm": zg["arm"], "M": zg["M"], "gamma_c": l3(zg["gamma_c"], zf["gamma_c"], 1.0),
                        "gamma_min": l3(zg["gamma_min"], zf["gamma_min"], 1.0)})
        erg["L3"] = l3l
        text.append(f"  L3 (Gamma gegen 1, grob -> fein): Gamma_c {sum(e['gamma_c']['bestanden'] for e in l3l)} von "
                    f"{len(l3l)}, Gamma_min {sum(e['gamma_min']['bestanden'] for e in l3l)} von {len(l3l)}; "
                    f"Einzelball ist die Nullzeile (dort nicht anwendbar)")
    return erg, text


# ================================================================ R-2 dunkler Zustand (linear)

def r2(klein):
    stufen = ("grob",) if klein else STUFEN
    erg, text = {}, ["R-2 Dunkler Zustand: zwei Baelle omega^2 = 0,7 bei -d/2, +d/2; Abklingraten in Gamma0."]
    for st in stufen:
        tab = tabelle_fuer([W2, R2_W2_GEGEN], st, klein)
        an = anker(tab)
        kr = math.sqrt(tab.pole[0]["nu"].real ** 2 - 1.0)
        per = 2.0 * PI / kr
        ng = 12 if klein else 40
        d_a, g_a, d_a0 = dunkler_abstand(tab, D_ZIEL, "anti", ng)
        d_s, g_s, d_s0 = dunkler_abstand(tab, D_ZIEL, "sym", ng)
        scan_a = [34.5 + j * per / 10.0 for j in range(3 if klein else 11)]
        scan_b = [24.0, 36.0] if klein else [20.0 + 4.0 * j for j in range(11)]
        s_e, _ = hintergrund(tab)
        phi = math.atan2((-s_e[0]).imag.item(), (-s_e[0]).real.item())     # 2 delta_e

        def zeilen_fuer(ds):
            zz = []
            for d in ds:
                pz = zwei_ball(tab, d)
                z = {"d": d, "markov_sym": 1.0 + math.cos(kr * d + phi), "markov_anti": 1.0 - math.cos(kr * d + phi),
                     "markov_ohne_phase_sym": 1.0 + math.cos(kr * d)}
                for p in pz:
                    if p["ok"]:
                        z["gamma_" + p["modus"]] = -p["nu"].imag / GAMMA0
                        z["dnu_" + p["modus"]] = (p["nu"].real - tab.pole[0]["nu"].real) / GAMMA0
                zz.append(z)
            return zz
        za, zb = zeilen_fuer(scan_a), zeilen_fuer(scan_b)
        gegen = []
        g_einzel = [p["gamma_rel"] for p in tab.pole]
        for d in scan_a:
            pz = zwei_ball(tab, d, (0, 1))
            z = {"d": d}
            for p in pz:
                if p["ok"]:
                    j = 0 if p["gewicht"][0] >= p["gewicht"][1] else 1
                    z[f"gamma_ball{j}_rel_einzel"] = (-p["nu"].imag / GAMMA0) / g_einzel[j]
            gegen.append(z)
        erg[st] = {"anker": an, "k_r": kr, "lambda": per, "d_anti": d_a, "gamma_anti_min": g_a, "d_anti_markov": d_a0,
                   "d_sym": d_s, "gamma_sym_min": g_s, "d_sym_markov": d_s0, "scan_eine_periode": za, "scan_weit": zb,
                   "gegenprobe_verstimmt": gegen, "pole_einzel": tab.pole, "phase_2delta_e": phi,
                   "d_anti_markov_mit_phase": d_a0 - phi / kr}
        text.append(f" [{st}]")
        text.append(anker_text(an))
        text.append(f"  lambda = {per:.5f}; Hintergrundphase 2 delta_e = arg(-S_e(nu_r)) = {phi:.5f} "
                    f"(verschiebt den dunklen Abstand um -{phi / kr:.4f})")
        text.append(f"  dunkel anti bei d = {d_a:.5f} (Markov ohne Phase {d_a0:.5f}, mit Phase {d_a0 - phi / kr:.5f}): "
                    f"Gamma = {fz(g_a)}; dunkel sym bei d = {d_s:.5f} (Markov ohne Phase {d_s0:.5f}): Gamma = {fz(g_s)}")
        text.append(f"  Partner {R2_W2_GEGEN}: Einzelpol {tab.pole[1]['nu']:.7f} (resonant {tab.pole[1]['resonant']}), "
                    f"Gamma {fz(tab.pole[1]['gamma_rel'], '.4f')}")
        for titel, zz in (("eine Periode", za), ("weit", zb)):
            text.append(f"  Abtastung {titel}: d | Gamma_sym (Markov mit Phase) | Gamma_anti (Markov mit Phase) | "
                        f"dnu_sym, dnu_anti (Gamma0)")
            for z in zz:
                text.append(f"  {z['d']:.4f} | {fz(z.get('gamma_sym'), '.5f')} ({z['markov_sym']:.5f}) | "
                            f"{fz(z.get('gamma_anti'), '.5f')} ({z['markov_anti']:.5f}) | "
                            f"{fz(z.get('dnu_sym'), '+.4f')}, {fz(z.get('dnu_anti'), '+.4f')}")
        text.append("  Gegenprobe 0,70 + 0,69: d | Gamma/Gamma_einzel je Ball: "
                    + "; ".join(f"{z['d']:.3f}: {fz(z.get('gamma_ball0_rel_einzel'), '.4f')}, "
                                f"{fz(z.get('gamma_ball1_rel_einzel'), '.4f')}" for z in gegen))
    if len(erg) == 2:
        erg["L3"] = {"gamma_anti_min": l3(erg["grob"]["gamma_anti_min"], erg["fein"]["gamma_anti_min"], 1.0),
                     "gamma_sym_min": l3(erg["grob"]["gamma_sym_min"], erg["fein"]["gamma_sym_min"], 1.0),
                     "d_anti": {"grob": erg["grob"]["d_anti"], "fein": erg["fein"]["d_anti"]}}
        text.append(f"  L3: Gamma_anti_min {erg['L3']['gamma_anti_min']['bestanden']}, Gamma_sym_min "
                    f"{erg['L3']['gamma_sym_min']['bestanden']}; d_anti grob {erg['grob']['d_anti']:.6f}, fein "
                    f"{erg['fein']['d_anti']:.6f}")
    return erg, text


# ================================================================ R-2 in der Zeitentwicklung

def r2zeit(klein):
    P = KLEIN if klein else NORMAL
    tab = tabelle_fuer([W2], "grob", klein)
    ng = 12 if klein else 40
    d_a, g_a, _ = dunkler_abstand(tab, D_ZIEL, "anti", ng)
    d_s, g_s, _ = dunkler_abstand(tab, D_ZIEL, "sym", ng)
    d_m = 0.5 * (d_a + d_s)
    abst = {"dS": d_s, "dA": d_a, "dM": d_m}
    lin = {}
    for name, d in abst.items():
        z = {}
        for p in zwei_ball(tab, d):
            if p["ok"]:
                z[p["modus"]] = -p["nu"].imag / GAMMA0
        lin[name] = z
    laeufe = [("einzel", None, "anr"), ("einzel", None, "ref")]
    for name, d in abst.items():
        laeufe += [(name, d, "sym"), (name, d, "anti"), (name, d, "ref")]

    def bauen(dx):
        x = gitter(dx)
        felder, zentren = [], []
        for _, d, art in laeufe:
            if d is None:
                felder.append(ball_zeit(x, W2, 0.0, 1.0 + EPS_DIL if art == "anr" else 1.0))
                zentren.append([0.0, 0.0])
                continue
            l1 = 1.0 if art == "ref" else 1.0 + EPS_DIL
            l2 = {"sym": 1.0 + EPS_DIL, "anti": 1.0 - EPS_DIL}.get(art, 1.0)
            p1, v1 = ball_zeit(x, W2, -0.5 * d, l1)
            p2, v2 = ball_zeit(x, W2, 0.5 * d, l2)
            felder.append((p1 + p2, v1 + v2))
            zentren.append([-0.5 * d, 0.5 * d])
        return x, felder, zentren, schwamm(x, L_BOX), False
    aus = zeit_rechnen("r2zeit", [("paare", bauen)], T_UEBER or P["T"])
    erg = {"abstaende": abst, "linear": lin, "gamma_min_linear": {"anti": g_a, "sym": g_s}, "stufen": {}}
    text = [f"R-2 in der Zeitentwicklung: Abstaende dS = {d_s:.5f}, dA = {d_a:.5f}, dM = {d_m:.5f}; "
            f"Streckung +-{EPS_DIL}; Fit ab t = {P['t_fit0']}, Fenster {P['tw']}."]
    for name in abst:
        text.append(f"  linear (Kontinuum) {name}: Gamma_sym {fz(lin[name].get('sym'), '.4f')}, Gamma_anti "
                    f"{fz(lin[name].get('anti'), '.4f')}")
    ref_von = {}
    for i, (name, d, art) in enumerate(laeufe):
        if art == "ref":
            ref_von[name] = i
    for (teil, stufe), st in aus.items():
        t, dat = st["t"], st["daten"]
        S = dat[:, :, 0:2]
        om = spitze(t, S[:, 0, 0] - S[:, 1, 0], P["t_om"], *BAND_OM)
        tc, A = demod(t, S.reshape(S.shape[0], -1), om, P["tw"], P["schritt"])
        A = A.reshape(A.shape[0], -1, 2)
        zeilen = []
        for b, (name, d, art) in enumerate(laeufe):
            if art == "ref":
                continue
            dA = A[:, b] - A[:, ref_von[name]]
            if d is None:
                haupt, neben = dA[:, 0], torch.zeros_like(dA[:, 0])
            elif art == "sym":
                haupt, neben = 0.5 * (dA[:, 0] + dA[:, 1]), 0.5 * (dA[:, 0] - dA[:, 1])
            else:
                haupt, neben = 0.5 * (dA[:, 0] - dA[:, 1]), 0.5 * (dA[:, 0] + dA[:, 1])
            fit = huellenfit(tc, haupt, P["t_fit0"])
            rein = (neben.abs().max() / haupt.abs().max().clamp(min=1e-300)).item() if haupt.numel() else float("nan")
            zeilen.append({"abstand": name, "d": d, "anregung": art, **fit, "fremdanteil": rein,
                           "linear": lin.get(name, {}).get(art, 1.0) if d is not None else 1.0,
                           "huelle": haupt.abs().tolist()})
        erg["stufen"][stufe] = {"omega_atem": om, "fenstermitten": tc.tolist(), "zeilen": zeilen, "sek": st["sek"],
                                "ms_je_schritt": st["ms_je_schritt"], "gekuerzt": st["gekuerzt"]}
        text.append(f" [{stufe}] Atemfrequenz {om:.5f} (Kontinuum {RHO_CODEX.real:.5f}); {st['sek']:.1f} s")
        text.append("  Abstand | d | Anregung | Gamma_fit | linear | rms ln | Fremdmodus max/Haupt")
        for z in zeilen:
            text.append(f"  {z['abstand']:6s} | {fz(z['d'], '.4f')} | {z['anregung']:4s} | {fz(z['gamma_rel'], '.4f')} | "
                        f"{fz(z['linear'], '.4f')} | {fz(z['rms_log'], '.1e')} | {fz(z['fremdanteil'], '.2e')}")
    if "grob" in erg["stufen"] and "fein" in erg["stufen"]:
        erg["L3"] = [{"abstand": g["abstand"], "anregung": g["anregung"],
                      "gamma": l3(g["gamma_rel"], f["gamma_rel"], 1.0)}
                     for g, f in zip(erg["stufen"]["grob"]["zeilen"], erg["stufen"]["fein"]["zeilen"])]
        text.append("  L3 (Gamma gegen 1): " + ", ".join(f"{e['abstand']}/{e['anregung']} {e['gamma']['bestanden']}"
                                                          for e in erg["L3"]))
    return erg, text


# ================================================================ R-3 Bindung durch Strahlung

def r3(klein):
    stufen = ("grob",) if klein else STUFEN
    erg, text = {}, ["R-3 Bindung durch Strahlung: zwei Baelle 0,7 bei -d/2, +d/2, Pumpe e^{ikx} (links) oder "
                     "e^{ikx} + e^{-ikx} (beide); Kraefte je Pumpe^2; F_rel = F_rechts - F_links (> 0 treibt auseinander)."]
    lo, hi, sch = R3_D
    ds = [lo, 0.5 * (lo + hi), hi] if klein else [lo + sch * j for j in range(int(round((hi - lo) / sch)) + 1)]
    a0, b0, _ = ball_par(W2)
    for st in stufen:
        tab = tabelle_fuer([W2], st, klein)
        an = anker(tab)
        nu1 = tab.pole[0]["nu"]
        g1 = -nu1.imag
        nus = [nu1.real + j * g1 for j in ((-1, 0, 1) if klein else (-3, -1, 0, 1, 3))] + list(R3_NU_OFF)
        nt = len(nus)
        h, R = (0.02, 20.0) if klein else NUMERIK[st]
        f = ball_funktionen(torch.tensor([W2] * (2 * nt), dtype=F64),
                            torch.tensor(nus + nus, dtype=C128), torch.tensor([0] * nt + [1] * nt), h, R)
        zeilen = []
        for i, nu in enumerate(nus):
            nut = torch.tensor(complex(nu, 0.0), dtype=C128, device=DEV)
            w = (f["D"][i:i + 1].repeat(2), f["T"][i:i + 1].repeat(2), f["D"][nt + i:nt + i + 1].repeat(2),
                 f["T"][nt + i:nt + i + 1].repeat(2))
            s_e, s_o = f["S"][i], f["S"][nt + i]
            r_betrag = (0.5 * (s_e - s_o)).abs().item()
            k = math.sqrt(nu * nu - 1.0)
            ge = f["G"][i].item()
            for pumpe, (ir, il) in (("links", (1.0, 0.0)), ("beide", (1.0, 1.0))):
                frel, gmax, f1s, f2s = [], 0.0, [], []
                for d in ds:
                    x = torch.tensor([-0.5 * d, 0.5 * d], dtype=F64, device=DEV)
                    E, O, ai, bi = streu_loesung(nut, x, w, ir, il)
                    F, ab = kraefte(nut, x, E, O, ir, il, ai, bi)
                    f1s.append(F[0].item())
                    f2s.append(F[1].item())
                    frel.append(F[1].item() - F[0].item())
                    gmax = max(gmax, (ge * ab.abs() / 2.0).max().item())
                gleich = [0.5 * (ds[j] + ds[j + 1]) for j in range(len(ds) - 1) if frel[j] > 0.0 >= frel[j + 1]]
                # Anpassung F_rel = c0 + a1 cos kd + b1 sin kd + a2 cos 2kd + b2 sin 2kd (kleinste Quadrate)
                dt_ = torch.tensor(ds, dtype=F64)
                A = torch.stack([torch.ones_like(dt_), torch.cos(k * dt_), torch.sin(k * dt_), torch.cos(2 * k * dt_),
                                 torch.sin(2 * k * dt_)], dim=1)
                amp_k = amp_2k = float("nan")
                if len(ds) >= 6:
                    c = torch.linalg.lstsq(A, torch.tensor(frel, dtype=F64).unsqueeze(1)).solution.squeeze(1)
                    amp_k, amp_2k = math.hypot(c[1].item(), c[2].item()), math.hypot(c[3].item(), c[4].item())
                fmax = max(abs(v) for v in frel)
                eps_lin = 0.01 * f_mitte(W2) / gmax if gmax > 0 else float("nan")
                f_lin = fmax * eps_lin ** 2
                d_x = (math.log(2.0 * 16.0 * a0 * a0 / b0) - math.log(f_lin)) / math.sqrt(a0) if f_lin > 0 else float("nan")
                zeilen.append({"nu": nu, "dnu_gamma": (nu - nu1.real) / g1, "pumpe": pumpe, "k": k,
                               "r_einzel": r_betrag, "druck_einzel": 4.0 * k * k * r_betrag ** 2,
                               "F_rel": frel, "F_links": f1s, "F_rechts": f2s, "F_rel_max": fmax,
                               "gleichgewichte": gleich,
                               "abstand_gleichgewichte": [gleich[j + 1] - gleich[j] for j in range(len(gleich) - 1)],
                               "halbe_wellenlaenge": PI / k, "amp_k": amp_k, "amp_2k": amp_2k,
                               "G_innen_max": gmax, "eps_linear": eps_lin, "F_rel_bei_eps_linear": f_lin,
                               "d_strahlung_gleich_auslaeufer": d_x})
        # Eigenfeld der beiden Moden am dunklen Abstand (anti) und in der Mitte (Resonanz speist sich selbst)
        d_a, _, _ = dunkler_abstand(tab, D_ZIEL, "anti", 12 if klein else 40)
        eigen = []
        for name, d in (("dA", d_a), ("dM", d_a + 0.25 * 2.0 * PI / math.sqrt(nu1.real ** 2 - 1.0))):
            x = torch.tensor([-0.5 * d, 0.5 * d], dtype=F64, device=DEV)
            for p in zwei_ball(tab, d):
                if not p["ok"]:
                    continue
                E = torch.tensor(p["E"], dtype=C128, device=DEV)
                O = torch.tensor(p["O"], dtype=C128, device=DEV)
                nur = torch.tensor(complex(p["nu"].real, 0.0), dtype=C128, device=DEV)
                F, _ = kraefte(nur, x, E, O, 0.0, 0.0)
                norm = (E.abs() ** 2).sum().item()
                eigen.append({"abstand": name, "d": d, "modus": p["modus"], "gamma_rel": -p["nu"].imag / GAMMA0,
                              "F_rel_je_E2": (F[1] - F[0]).item() / norm})
        schwanz = {str(d): 2.0 * auslaeuferkraft(d) for d in (30.0, 35.0, 40.0, 45.0)}
        erg[st] = {"anker": an, "d": ds, "zeilen": zeilen, "eigenfeld": eigen, "auslaeufer_F_rel_betrag": schwanz}
        text.append(f" [{st}]")
        text.append(anker_text(an))
        text.append("  Gegenprobe ohne Pumpe (Auslaeufer, gleichphasig, |F_rel| = 2 F): "
                    + ", ".join(f"d = {k_}: {v:.2e}" for k_, v in schwanz.items()))
        text.append("  nu | (nu-Re nu1)/Gamma | Pumpe | |r| einzel | max|F_rel| | Gleichgewichte (Abstand; lambda/2) | "
                    "Amp k, 2k | G innen | eps_lin | F bei eps_lin | d ab dem Strahlung > Auslaeufer")
        for z in zeilen:
            text.append(f"  {z['nu']:.7f} | {z['dnu_gamma']:+8.2f} | {z['pumpe']:5s} | {z['r_einzel']:.3e} | "
                        f"{z['F_rel_max']:.3e} | {len(z['gleichgewichte'])} "
                        f"({', '.join(f'{v:.3f}' for v in z['abstand_gleichgewichte'])}; {z['halbe_wellenlaenge']:.4f}) | "
                        f"{fz(z['amp_k'], '.2e')}, {fz(z['amp_2k'], '.2e')} | {z['G_innen_max']:.2e} | "
                        f"{fz(z['eps_linear'], '.2e')} | {fz(z['F_rel_bei_eps_linear'], '.2e')} | "
                        f"{fz(z['d_strahlung_gleich_auslaeufer'], '.1f')}")
        text.append("  Eigenfeld (ohne Pumpe, Mode speist sich selbst): "
                    + "; ".join(f"{e['abstand']} {e['modus']} Gamma {e['gamma_rel']:.4f}: F_rel/|E|^2 {e['F_rel_je_E2']:+.3e}"
                                for e in eigen))
    if len(erg) == 2:
        l3l = []
        for zg, zf in zip(erg["grob"]["zeilen"], erg["fein"]["zeilen"]):
            l3l.append({"nu": zg["nu"], "pumpe": zg["pumpe"], "F_rel_max": l3(zg["F_rel_max"], zf["F_rel_max"], 0.0)})
        erg["L3"] = l3l
        text.append(f"  L3 (max|F_rel| gegen 0): {sum(e['F_rel_max']['bestanden'] for e in l3l)} von {len(l3l)}")
    return erg, text


# ================================================================ R-4 Randreflexion

def r4(klein):
    P = KLEIN if klein else NORMAL
    tab = tabelle_fuer([W2], "grob", klein)
    spiegel = auswerten_konfig([-L_BOX, 0.0, L_BOX], [-1, 0, -1], 1, tab, ueberleben=False)
    lin = {"pole": spiegel.get("pole", []), "max_abs_im": max((abs(p.imag) for p in spiegel.get("pole", [])),
                                                                default=float("nan"))}

    def box(dx):
        x = gitter(dx)
        s = schwamm(x, L_BOX)
        felder = [ball_zeit(x, W2, 0.0, 1.0 + EPS_DIL), ball_zeit(x, W2, 0.0), ball_zeit(x, W2, 0.0, 1.0 + EPS_DIL),
                  ball_zeit(x, W2, 0.0)]
        sigma = torch.stack([s, s, torch.zeros_like(s), torch.zeros_like(s)])
        return x, felder, [[0.0, 0.0]] * 4, sigma, False

    def ring(dx):
        x = gitter(dx, L_BOX, ring=True)
        return x, [ball_zeit(x, W2, 0.0, 1.0 + EPS_DIL), ball_zeit(x, W2, 0.0)], [[0.0, 0.0]] * 2, torch.zeros_like(x), True

    def gross(dx):
        x = gitter(dx, 2.0 * L_BOX)
        return (x, [ball_zeit(x, W2, 0.0, 1.0 + EPS_DIL), ball_zeit(x, W2, 0.0)], [[0.0, 0.0]] * 2,
                schwamm(x, 2.0 * L_BOX), False)
    aus = zeit_rechnen("r4", [("box", box), ("ring", ring), ("gross", gross)], T_UEBER or P["T"])
    paare = {"box": [("schwamm", 0, 1), ("spiegel", 2, 3)], "ring": [("ring", 0, 1)], "gross": [("gross", 0, 1)]}
    erg = {"linear_spiegel": lin, "stufen": {}}
    t_r = 2.0 * L_BOX / (math.sqrt(NU_C ** 2 - 1.0) / NU_C)
    text = [f"R-4 Randreflexion: Einzelball 0,7, Streckung {EPS_DIL}; Rueckkehrzeit der Abstrahlung 2L/v_g = {t_r:.1f}.",
            f"  linear: Ball zwischen festen Spiegeln bei +-{L_BOX}: {len(lin['pole'])} Pole nahe nu0, "
            f"max |Im nu| = {fz(lin['max_abs_im'], '.2e')} (Gamma0 = {GAMMA0:.3e})"]
    for stufe in ("grob", "fein"):
        if ("box", stufe) not in aus:
            continue
        st = aus[("box", stufe)]
        om = spitze(st["t"], st["daten"][:, 0, 0] - st["daten"][:, 1, 0], P["t_om"], *BAND_OM)
        zeilen = []
        for teil, liste in paare.items():
            if (teil, stufe) not in aus:
                continue
            s = aus[(teil, stufe)]
            tc, A = demod(s["t"], s["daten"][:, :, 0], om, P["tw"], P["schritt"])
            for name, i_e, i_r in liste:
                dA = A[:, i_e] - A[:, i_r]
                fit = huellenfit(tc, dA, P["t_fit0"])
                frueh = huellenfit(tc, dA, P["t_fit0"], t_r)
                spaet = huellenfit(tc, dA, t_r + 0.5 * P["tw"])
                zeilen.append({"rand": name, **fit, "gamma_vor_rueckkehr": frueh["gamma_rel"],
                               "gamma_nach_rueckkehr": spaet["gamma_rel"], "huelle": dA.abs().tolist(),
                               "sek": s["sek"], "ms_je_schritt": s["ms_je_schritt"]})
        erg["stufen"][stufe] = {"omega_atem": om, "zeilen": zeilen}
        text.append(f" [{stufe}] Atemfrequenz {om:.5f}")
        text.append("  Rand | Gamma_fit ab t0 | vor Rueckkehr | nach Rueckkehr | rms ln | |A| erst -> letzt | s")
        for z in zeilen:
            text.append(f"  {z['rand']:8s} | {fz(z['gamma_rel'], '.4f')} | {fz(z['gamma_vor_rueckkehr'], '.4f')} | "
                        f"{fz(z['gamma_nach_rueckkehr'], '.4f')} | {fz(z['rms_log'], '.1e')} | "
                        f"{fz(z.get('amp_erst'), '.3e')} -> {fz(z.get('amp_letzt'), '.3e')} | {z['sek']:.1f}")
    if "grob" in erg["stufen"] and "fein" in erg["stufen"]:
        fein = {z["rand"]: z for z in erg["stufen"]["fein"]["zeilen"]}
        erg["L3"] = [{"rand": g["rand"], "gamma": l3(g["gamma_rel"], fein[g["rand"]]["gamma_rel"], 1.0)}
                     for g in erg["stufen"]["grob"]["zeilen"] if g["rand"] in fein]
        text.append("  L3 (Gamma gegen 1): " + ", ".join(f"{e['rand']} {e['gamma']['bestanden']}" for e in erg["L3"]))
    return erg, text


# ================================================================ R-5 Lokalisierung im Q-Ball-Gas

def gas(n, seed, art):
    g = torch.Generator().manual_seed(1000 * seed + 10 * n + (1 if art == "gemischt" else 0))
    lo, hi = R5_ABST
    rechts = torch.cumsum(lo + (hi - lo) * torch.rand(n, generator=g, dtype=F64), 0).tolist()
    links = (-torch.cumsum(lo + (hi - lo) * torch.rand(n, generator=g, dtype=F64), 0)).tolist()
    x = sorted(links) + [0.0] + rechts
    if art == "gleich":
        typen = [0] * (2 * n + 1)
    else:
        typen = [1 + int(v) for v in torch.randint(0, len(R5_W2_GEMISCHT), (2 * n + 1,), generator=g).tolist()]
        typen[n] = 0
    return x, typen


def r5(klein):
    stufen = ("grob",) if klein else STUFEN
    ns = (2,) if klein else R5_N
    seeds = (1,) if klein else R5_SEEDS
    erg, text = {}, [f"R-5 Lokalisierung: Mittelball 0,7 bei 0, je N Gasbaelle links und rechts, Abstaende gleichverteilt "
                     f"in {R5_ABST}; 'gleich' = alle 0,7, 'gemischt' = omega^2 aus {R5_W2_GEMISCHT}; Seeds {seeds}."]
    for st in stufen:
        tab = tabelle_fuer([W2] + list(R5_W2_GEMISCHT), st, klein)
        an = anker(tab)
        zeilen = [{"art": "leer", "N": 0, "seed": 0, **auswerten_konfig([0.0], [0], 0, tab)}]
        for art in ("gleich", "gemischt"):
            for n in ns:
                for s in seeds:
                    x, typen = gas(n, s, art)
                    zeilen.append({"art": art, "N": n, "seed": s, **auswerten_konfig(x, typen, n, tab)})
        for n in ns:
            zeilen.append({"art": "periodisch", "N": n, "seed": 0,
                           **auswerten_konfig([R5_PERIODE * j for j in range(-n, n + 1)], [0] * (2 * n + 1), n, tab)})
        zus = []
        for art in ("gleich", "gemischt", "periodisch"):
            for n in ns:
                zz = [z for z in zeilen if z["art"] == art and z["N"] == n]
                ub = [z["ueberleben_cmt"][1]["zentral"] for z in zz if z.get("ueberleben_cmt")]
                zus.append({"art": art, "N": n, "median_gamma_c": median([z["gamma_c"] for z in zz]),
                            "median_gamma_min": median([z["gamma_min"] for z in zz]),
                            "median_ueberleben_cmt_5": median(ub) if ub else float("nan"),
                            "median_polsumme_5": median([z["ueberleben_polsumme"][1] for z in zz
                                                         if "ueberleben_polsumme" in z]),
                            "median_n_dunkel": median([z["n_dunkel"] for z in zz])})
        resonant = [p["w2"] for p in tab.pole if p["resonant"]]
        erg[st] = {"anker": an, "zeilen": zeilen, "zusammen": zus, "resonante_typen": resonant, "pole": tab.pole}
        text.append(f" [{st}]")
        text.append(anker_text(an))
        text.append(f"  resonante Typen (Einzelpol in |nu - nu0| <= {R_GUELTIG}): {resonant}")
        text.append(f"  Einzelball: Ueberleben bei 5/Gamma0 = e^-10 = {math.exp(-10.0):.2e}")
        text.append("  Art | N je Seite | Median Gamma_c | Median Gamma_min | Median Ueberleben CMT (5/Gamma0) | "
                    "Median Polsumme (5/Gamma0) | Median dunkle Pole")
        for z in zus:
            text.append(f"  {z['art']:10s} | {z['N']:2d} | {fz(z['median_gamma_c'], '.4f')} | "
                        f"{fz(z['median_gamma_min'], '.2e')} | {fz(z['median_ueberleben_cmt_5'], '.2e')} | "
                        f"{fz(z['median_polsumme_5'], '.2e')} | {fz(z['median_n_dunkel'], '.1f')}")
    if len(erg) == 2:
        l3l = [{"art": g["art"], "N": g["N"], "median_gamma_c": l3(g["median_gamma_c"], f["median_gamma_c"], 1.0)}
               for g, f in zip(erg["grob"]["zusammen"], erg["fein"]["zusammen"])]
        erg["L3"] = l3l
        text.append(f"  L3 (Median Gamma_c gegen 1): {sum(e['median_gamma_c']['bestanden'] for e in l3l)} von {len(l3l)}")
    return erg, text


# ================================================================ Hauptprogramm

TEILE = {"r1": r1, "r2": r2, "r2zeit": r2zeit, "r3": r3, "r4": r4, "r5": r5}


def js_default(o):
    if isinstance(o, complex):
        return [o.real, o.imag]
    if torch.is_tensor(o):
        o = o.detach().cpu()
        return torch.view_as_real(o).tolist() if o.is_complex() else o.tolist()
    return str(o)


def schreiben(out, name, ausgabe, text):
    with open(os.path.join(out, f"reflexion_{name}_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    with open(os.path.join(out, f"reflexion_{name}_ergebnis.json"), "w") as fh:
        json.dump(ausgabe, fh, indent=1, default=js_default)


def main():
    global DEV, T_START, STUFEN, T_UEBER
    ap = argparse.ArgumentParser(description="Runde 6: Reflexion und Stabilitaet (Karten R-1 bis R-5)")
    ap.add_argument("unterbefehl", choices=["rauch"] + list(TEILE))
    ap.add_argument("--geraet", choices=["cuda", "cpu"], default="cpu")
    ap.add_argument("--out", default=None)
    ap.add_argument("--faeden", type=int, default=1)
    ap.add_argument("--stufen", choices=["grob", "fein", "grob,fein"], default="grob,fein")
    ap.add_argument("--T", type=float, default=None, help="Laufzeit der Zeitteile (nur fuer lokale Proben)")
    opt = ap.parse_args()
    T_START = time.perf_counter()
    STUFEN = tuple(opt.stufen.split(","))
    T_UEBER = opt.T
    if opt.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("Kein CUDA-Geraet sichtbar: auf einer cpu-Spur mit --geraet cpu starten.")
        DEV = torch.device("cuda")
        gesamt = torch.cuda.get_device_properties(0).total_memory
        torch.cuda.set_per_process_memory_fraction(min(1.0, SPEICHER_GB * 2 ** 30 / gesamt))
        geraet = torch.cuda.get_device_name(0)
    else:
        DEV = torch.device("cpu")
        torch.set_num_threads(max(1, opt.faeden))
        geraet = f"CPU, {torch.get_num_threads()} Faden"
    out = opt.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), "ausgabe-" + opt.unterbefehl)
    os.makedirs(out, exist_ok=True)
    start = jetzt()
    kopf = f"Runde 6 Reflexion {opt.unterbefehl} Start {start} auf {geraet}, torch {torch.__version__}"
    print(kopf, flush=True)
    ausgabe = {"start": start, "geraet": geraet, "torch": torch.__version__, "unterbefehl": opt.unterbefehl,
               "ergebnisse": {}, "fehler": {}, "sek": {}}
    text = [kopf, ""]
    teile = list(TEILE) if opt.unterbefehl == "rauch" else [opt.unterbefehl]
    for name in teile:
        t0 = uhr()
        try:
            erg, tx = TEILE[name](opt.unterbefehl == "rauch")
            ausgabe["ergebnisse"][name] = erg
            text += tx + [""]
        except Exception:
            ausgabe["fehler"][name] = traceback.format_exc()
            text += [f"{name} FEHLER:", ausgabe["fehler"][name], ""]
            print(ausgabe["fehler"][name], flush=True)
        ausgabe["sek"][name] = uhr() - t0
        text.append(f"({name}: {ausgabe['sek'][name]:.1f} s)")
        print(f"{name} fertig nach {ausgabe['sek'][name]:.1f} s", flush=True)
        schreiben(out, opt.unterbefehl, ausgabe, text)
    ausgabe["ende"] = jetzt()
    ausgabe["dauer_s"] = time.perf_counter() - T_START
    ausgabe["hinweise"] = HINWEISE
    if DEV.type == "cuda":
        ausgabe["torch_speicher_max_mb"] = torch.cuda.max_memory_allocated() / 2 ** 20
    text.append(f"Hinweise: {HINWEISE if HINWEISE else 'keine'}")
    text.append(f"Ende {ausgabe['ende']}, Dauer {ausgabe['dauer_s']:.1f} s, Fehler in: "
                f"{sorted(ausgabe['fehler']) if ausgabe['fehler'] else 'keine'}")
    schreiben(out, opt.unterbefehl, ausgabe, text)
    print("\n".join(text), flush=True)
    if ausgabe["fehler"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
