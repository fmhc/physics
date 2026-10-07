#!/usr/bin/env python3
"""PHASE-WAND (Runde 26), Code-Agent (Claude, Anthropic) fuer die Leitung claude-primary, 03.10.2026.
Karte: coordination/runden-v3/RUNDE-26/phase-wand/KARTE.md, Plan: PLAN.md daneben.

Ebene Wand des Modells M1 (U = S - S^2 + beta S^3) bei omega_min(beta)^2 = 1 - 1/(4 beta):
    S(x) = S_c/(1 + exp(x/sqrt(beta))), S_c = 1/(2 beta); Wandlage x_w = 0 (S = S_c/2); Plateau bei x -> -inf.
Linearisierung (A geschlossen, B offen) wie RUNDE-24/wand-beta/code/wand_beta.py (Klasse MB, Verfahren c_in):
    A'' = [W - (f - omega)^2] A + C B,  B'' = C A + [W - (f + omega)^2] B,  W = 1 - 4S + 9 beta S^2, C = -2S + 6 beta S^2.
Phase (PLAN.md Abschnitt 3): Loesung z_p bei f = rho_z (aussen A = e^(-q x), B = 0; innen ohne wachsende e2-Mode).
Im Plateau, Tiefe d = x_w - x:  e1.z_p = R cos(k_in d + phi),  e2.z_p = c+ e^(-kappa d) + c- e^(+kappa d)  (c- = c_in).
phi wird mod pi angegeben, in [0, pi).
1D-Lagebedingung: Phi(eps) = k_in x_w(eps) + phi = m pi/2;  m gerade -> gerade Mode, m ungerade -> ungerade Mode.
x_w(eps) aus dem exakten 1D-Profil S(x) = 2 m2/(1 + 2 sqrt(beta eps) cosh(b x)), m2 = 1/(4 beta) - eps, b = 2 sqrt(m2):
    S(x_w) = S_c/2  <=>  cosh(b x_w) = (1 - 8 beta eps)/(2 sqrt(beta eps)).

Kommandos (Zahlenparameter nur aus der Konfigurationsdatei):
  phase      --konfig K --out O                 rho_z, phi, e2-Anteile, Gegenproben (rtol, Gebiet, RK4 auf zwei Stufen)
  formel     --konfig K --phase P --out O       vorhergesagte 1D-Lagen eps_n mit Paritaet
  vergleich  --konfig K --formel F --sprossen S --out O   mechanische Regel (PW1 bzw. PW3)
Alles float64, CPU, ein Faden.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import argparse  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.integrate import solve_ivp  # noqa: E402
from scipy.optimize import brentq  # noqa: E402
from scipy.special import expit  # noqa: E402

ATOL = 1e-30
RTOL_HAUPT = 1e-12
M_ABL = np.array([[5.0, 4.0], [4.0, 5.0]])   # dP/dS bei S = S_c (dW/dS = -4 + 18 beta S_c = 5, dC/dS = -2 + 12 beta S_c = 4)
T_START = time.time()


def jetzt():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


BEGINN = jetzt()


def log(*a):
    print(f"[{time.time() - T_START:8.1f} s]", *a, flush=True)


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, np.ndarray):
        return [jsonfest(v) for v in x.tolist()]
    if isinstance(x, (np.floating, float)):
        v = float(x)
        return v if math.isfinite(v) else str(v)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    return x


def schreibe(pfad, obj):
    with open(pfad + ".tmp", "w") as fh:
        json.dump(jsonfest(obj), fh, indent=1)
    os.replace(pfad + ".tmp", pfad)


def lade(pfad):
    with open(pfad) as fh:
        return json.load(fh)


def wrap_pi(a):
    """Differenz mod pi nach [-pi/2, pi/2)."""
    return (a + 0.5 * math.pi) % math.pi - 0.5 * math.pi


# ----------------------------------------------------------------------------------------------------------------------
# Ebene Wand (Klasse MB, innen_moden, aussen_raten, c_in wie RUNDE-24/wand-beta/code/wand_beta.py)
# ----------------------------------------------------------------------------------------------------------------------

class MB:
    def __init__(self, beta):
        self.beta = float(beta)
        self.OM = math.sqrt(1.0 - 1.0 / (4.0 * self.beta))
        self.Sc = 1.0 / (2.0 * self.beta)
        sb = math.sqrt(self.beta)
        self.rate = 1.0 / sb
        self.xa, self.xb = -36.0 * sb, 43.0 * sb
        self.W_in = 1.0 + 1.0 / (4.0 * self.beta)
        self.C_in = 1.0 / (2.0 * self.beta)

    def S(self, x):
        return self.Sc * expit(-self.rate * x)

    def koeff(self, x):
        S = self.S(x)
        b = self.beta
        return 1.0 - 4.0 * S + 9.0 * b * S * S, -2.0 * S + 6.0 * b * S * S

    def P(self, x, f):
        W, C = self.koeff(x)
        return np.array([[W - (f - self.OM) ** 2, C], [C, W - (f + self.OM) ** 2]])

    def P_innen(self, f):
        return np.array([[self.W_in - (f - self.OM) ** 2, self.C_in], [self.C_in, self.W_in - (f + self.OM) ** 2]])

    def k2_formel(self, f):
        return self.OM ** 2 + f * f - self.W_in + math.sqrt(4.0 * self.OM ** 2 * f * f + self.C_in ** 2)

    def rest(self, x):
        S = self.S(x)
        fx = math.sqrt(S)
        sb = math.sqrt(self.beta)
        f1 = -sb * fx * (self.Sc - S)
        f2 = -sb * f1 * (self.Sc - 3.0 * S)
        return f2 - (1.0 - 2.0 * S + 3.0 * self.beta * S * S - self.OM ** 2) * fx


def innen_moden(mod, f):
    lam, vec = np.linalg.eigh(mod.P_innen(f))
    e1, e2 = vec[:, 0].copy(), vec[:, 1].copy()
    if e1[0] < 0:
        e1 = -e1
    if e2[0] < 0:
        e2 = -e2
    if not (lam[0] < 0.0 < lam[1]):
        raise ValueError(f"Innenmatrix nicht ein laufend / ein abklingend bei f = {f}: {lam}")
    return math.sqrt(-lam[0]), e1, math.sqrt(lam[1]), e2


def aussen_raten(mod, f):
    p11 = 1.0 - (f - mod.OM) ** 2
    p22 = 1.0 - (f + mod.OM) ** 2
    if not (p11 > 0.0 and p22 < 0.0):
        raise ValueError(f"aussen nicht geschlossen/offen bei f = {f}")
    return math.sqrt(p11), math.sqrt(-p22)


def _rhs_fun(mod, f):
    def rhs(x, z):
        P = mod.P(x, f)
        return np.concatenate([z[2:], P @ z[:2]])
    return rhs


def c_in(mod, f, rtol=RTOL_HAUPT, xa=None, xb=None):
    """Koeffizient c- der nach innen wachsenden e2-Mode (Normierung A = e^(-q x) aussen), wie wand_beta.c_in."""
    xa = mod.xa if xa is None else xa
    xb = mod.xb if xb is None else xb
    q, _ = aussen_raten(mod, f)
    sol = solve_ivp(_rhs_fun(mod, f), (xb, xa), np.array([1.0, 0.0, -q, 0.0]), method="DOP853", rtol=rtol, atol=ATOL)
    if not sol.success:
        raise RuntimeError(sol.message)
    z = sol.y[:, -1]
    k, e1, kap, e2 = innen_moden(mod, f)
    ye, ye1 = e2 @ z[:2], e2 @ z[2:]
    return (kap * ye - ye1) / (2.0 * kap) * math.exp(kap * xa - q * xb), sol.nfev


def loesung(mod, f, xs, rtol=RTOL_HAUPT, xb=None):
    """z = (A, B, A', B') an den Stellen xs (alle < xb), Normierung A = e^(-q x) aussen. Rueckgabe x absteigend."""
    xb = mod.xb if xb is None else xb
    q, _ = aussen_raten(mod, f)
    xs = sorted(set(float(x) for x in xs), reverse=True)
    sol = solve_ivp(_rhs_fun(mod, f), (xb, xs[-1]), np.array([1.0, 0.0, -q, 0.0]), method="DOP853", rtol=rtol,
                    atol=ATOL, t_eval=xs)
    if not sol.success:
        raise RuntimeError(sol.message)
    return np.array(sol.t), sol.y * math.exp(-q * xb), sol.nfev


def zerlege(mod, f, x, z, x_w=0.0):
    """Plateau-Zerlegung bei x (Tiefe d = x_w - x): e1.z = R cos(k d + phi), e2.z = c+ e^(-kap d) + c- e^(kap d)."""
    k, e1, kap, e2 = innen_moden(mod, f)
    d = x_w - x
    y1, y1p = float(e1 @ z[:2]), float(e1 @ z[2:])
    # d/dx R cos(k (x_w - x) + phi) = R k sin(k d + phi): y1 = R cos(theta), y1'/k = R sin(theta), theta = k d + phi
    th = math.atan2(y1p / k, y1)
    R = math.hypot(y1, y1p / k)
    phi = (th - k * d) % math.pi
    y2, y2p = float(e2 @ z[:2]), float(e2 @ z[2:])
    # e2.z = c+ e^(-kap d) + c- e^(kap d); d/dx = -d/dd, also e2.z'/kap = c+ e^(-kap d) - c- e^(kap d)
    cp = 0.5 * (y2 + y2p / kap) * math.exp(kap * d)
    cm = 0.5 * (y2 - y2p / kap) * math.exp(-kap * d)
    return {"x": x, "d": d, "phi": phi, "R": R, "c_plus": cp, "c_minus": cm,
            "wachsend_rel": abs(cm) * math.exp(kap * d) / R, "abklingend_rel": abs(cp) * math.exp(-kap * d) / R}


def rho_z_suchen(mod, K, fn):
    """Nullstelle von fn (c_in) in K['rho_klammer']; optional vorher Abtastung K['rho_abtastung'] = [lo, hi, n]."""
    if "rho_abtastung" in K:
        lo, hi, n = K["rho_abtastung"]
        fs = np.linspace(lo, hi, int(n))
        vals = [fn(float(f)) for f in fs]
        kl = [(float(fs[i]), float(fs[i + 1])) for i in range(len(fs) - 1) if vals[i] * vals[i + 1] < 0.0]
        if not kl:
            raise RuntimeError("kein Vorzeichenwechsel von c_in in der Abtastung")
        lo, hi = kl[0]
    else:
        lo, hi = K["rho_klammer"]
    a, b = fn(lo), fn(hi)
    if a * b > 0.0:
        raise RuntimeError(f"kein Vorzeichenwechsel von c_in in [{lo}, {hi}]")
    return brentq(fn, lo, hi, xtol=1e-14, rtol=1e-15, maxiter=200), [lo, hi]


# ----------------------------------------------------------------------------------------------------------------------
# Gegenprobe: klassisches RK4 mit festem Schritt (reines Python, ein rho) auf x_j = j h
# ----------------------------------------------------------------------------------------------------------------------

def rk4_eben(mod, f, h, j_rec=()):
    om = mod.OM
    dm2, dp2 = (f - om) ** 2, (f + om) ** 2
    q = math.sqrt(1.0 - dm2)
    Sc, rate, c9, c6 = mod.Sc, mod.rate, 9.0 * mod.beta, 6.0 * mod.beta
    jb, ja = int(math.ceil(mod.xb / h)), int(math.floor(mod.xa / h))

    def koeff(x):
        S = Sc / (1.0 + math.exp(rate * x))
        W = 1.0 - 4.0 * S + c9 * S * S
        c = -2.0 * S + c6 * S * S
        return W - dm2, c, W - dp2

    y0, y1, y2, y3 = 1.0, 0.0, -q, 0.0
    logn = 0.0
    rec = {}
    j_rec = set(int(j) for j in j_rec)
    hs = -h
    p_hi = koeff(jb * h)
    for j in range(jb, ja, -1):
        p_m = koeff((j - 0.5) * h)
        p_lo = koeff((j - 1) * h)
        a11, ac, a22 = p_hi
        k1 = (y2, y3, a11 * y0 + ac * y1, ac * y0 + a22 * y1)
        m11, mc, m22 = p_m
        t0, t1, t2, t3 = y0 + 0.5 * hs * k1[0], y1 + 0.5 * hs * k1[1], y2 + 0.5 * hs * k1[2], y3 + 0.5 * hs * k1[3]
        k2 = (t2, t3, m11 * t0 + mc * t1, mc * t0 + m22 * t1)
        t0, t1, t2, t3 = y0 + 0.5 * hs * k2[0], y1 + 0.5 * hs * k2[1], y2 + 0.5 * hs * k2[2], y3 + 0.5 * hs * k2[3]
        k3 = (t2, t3, m11 * t0 + mc * t1, mc * t0 + m22 * t1)
        l11, lc, l22 = p_lo
        t0, t1, t2, t3 = y0 + hs * k3[0], y1 + hs * k3[1], y2 + hs * k3[2], y3 + hs * k3[3]
        k4 = (t2, t3, l11 * t0 + lc * t1, lc * t0 + l22 * t1)
        y0 += hs / 6.0 * (k1[0] + 2.0 * k2[0] + 2.0 * k3[0] + k4[0])
        y1 += hs / 6.0 * (k1[1] + 2.0 * k2[1] + 2.0 * k3[1] + k4[1])
        y2 += hs / 6.0 * (k1[2] + 2.0 * k2[2] + 2.0 * k3[2] + k4[2])
        y3 += hs / 6.0 * (k1[3] + 2.0 * k2[3] + 2.0 * k3[3] + k4[3])
        p_hi = p_lo
        if j % 128 == 0:
            m = max(abs(y0), abs(y1), abs(y2), abs(y3))
            y0, y1, y2, y3 = y0 / m, y1 / m, y2 / m, y3 / m
            logn += math.log(m)
        if (j - 1) in j_rec:
            rec[j - 1] = (np.array([y0, y1, y2, y3]), logn)
    k, e1, kap, e2 = innen_moden(mod, f)
    xa, xb = ja * h, jb * h
    ye, ye1 = e2[0] * y0 + e2[1] * y1, e2[0] * y2 + e2[1] * y3
    cin = (kap * ye - ye1) / (2.0 * kap) * math.exp(logn + kap * xa - q * xb)
    return cin, rec, q * xb


# ----------------------------------------------------------------------------------------------------------------------
# Kommando phase
# ----------------------------------------------------------------------------------------------------------------------

def phase_satz(mod, fz, tiefen_x, rtol, xb):
    t, Z, nfev = loesung(mod, fz, [-d for d in tiefen_x], rtol, xb)
    return [zerlege(mod, fz, float(t[i]), Z[:, i]) for i in range(len(t))], nfev


def cmd_phase(args):
    K = lade(args.konfig)
    beta = float(K["beta"])
    mod = MB(beta)
    sb = math.sqrt(beta)
    tiefen = [float(t) * sb for t in K["tiefen"]]
    d_wert = float(K["tiefe_gewertet"]) * sb
    out = {"kommando": "phase", "beginn": BEGINN, "konfig": K, "beta": beta, "omega_min": mod.OM, "S_c": mod.Sc,
           "xa": mod.xa, "xb": mod.xb, "rtol": RTOL_HAUPT}
    xs = np.linspace(mod.xa, mod.xb, 4001)
    out["k0_rest_max"] = float(max(abs(mod.rest(float(x))) for x in xs))
    # (1) rho_z, DOP853 rtol 1e-12 (Hauptweg)
    fz, kl = rho_z_suchen(mod, K, lambda f: c_in(mod, f)[0])
    k, e1, kap, e2 = innen_moden(mod, fz)
    out.update({"rho_z": fz, "klammer": kl, "k_in": k, "kappa_in": kap, "e1": e1, "e2": e2,
                "k0_dispersion_abw": abs(k * k - mod.k2_formel(fz)), "c_in_bei_rho_z": c_in(mod, fz)[0]})
    log(f"beta {beta}: rho_z = {fz:.12f}, k_in = {k:.9f}, kappa_in = {kap:.9f}")
    # (2) Phase an allen Tiefen (Hauptweg), gewertete Tiefe d_wert
    satz, nfev = phase_satz(mod, fz, tiefen + [d_wert], RTOL_HAUPT, mod.xb)
    wert = min(satz, key=lambda s: abs(s["d"] - d_wert))
    phi = wert["phi"]
    for s in satz:
        s["d_in_sqrtbeta"] = s["d"] / sb
        s["phi_minus_gewertet"] = wrap_pi(s["phi"] - phi)
    out["tiefen"] = sorted(satz, key=lambda s: s["d"])
    out["phi"] = phi
    out["R"] = wert["R"]
    out["c_plus"] = wert["c_plus"]
    out["e2_wachsend_rel"] = wert["wachsend_rel"]
    out["phi_streuung_tiefen"] = max(abs(s["phi_minus_gewertet"]) for s in satz)
    log(f"phi = {phi:.10f} (Tiefe {d_wert:.3f}), Streuung ueber Tiefen {out['phi_streuung_tiefen']:.2e}, "
        f"e2 wachsend/R = {wert['wachsend_rel']:.2e}, abklingend/R = {wert['abklingend_rel']:.2e}")
    schreibe(args.out, out)
    # (3) Gegenproben DOP853: rtol 1e-10 und Gebiet xb + 10 sqrt(beta), je mit eigenem rho_z
    geg = {}
    for name, rtol, xb in (("rtol_1e-10", 1e-10, mod.xb), ("gebiet_plus_10", RTOL_HAUPT, mod.xb + 10.0 * sb)):
        fz2, _ = rho_z_suchen(mod, {"rho_klammer": kl}, lambda f: c_in(mod, f, rtol, None, xb)[0])
        s2, _ = phase_satz(mod, fz2, [d_wert], rtol, xb)
        geg[name] = {"rho_z": fz2, "d_rho_z": fz2 - fz, "phi": s2[0]["phi"], "d_phi": wrap_pi(s2[0]["phi"] - phi)}
        log(f"Gegenprobe {name}: d rho_z = {fz2 - fz:.2e}, d phi = {geg[name]['d_phi']:.2e}")
    # (4) Gegenprobe RK4 (festes h, eigenes rho_z), Phase an der Gitterstelle naechst d_wert
    for h in K["rk4_h"]:
        def fn(f, h=h):
            return rk4_eben(mod, f, h)[0]
        fzh, _ = rho_z_suchen(mod, {"rho_klammer": kl}, fn)
        jd = int(round(-d_wert / h))
        _, rec, _ = rk4_eben(mod, fzh, h, [jd])
        z, _ = rec[jd]
        s = zerlege(mod, fzh, jd * h, z)
        geg[f"rk4_h{h}"] = {"rho_z": fzh, "d_rho_z": fzh - fz, "phi": s["phi"], "d_phi": wrap_pi(s["phi"] - phi),
                            "x": jd * h}
        log(f"Gegenprobe RK4 h = {h}: rho_z = {fzh:.12f} (d {fzh - fz:.2e}), d phi = {wrap_pi(s['phi'] - phi):.2e}")
    out["gegenproben"] = geg
    schreibe(args.out, out)
    # (5) Ableitungen bei rho_z (fuer die Fehlerabschaetzung der Formel, nicht angepasst)
    abl = []
    for dr in K["delta_rho"]:
        cp_, cm_ = c_in(mod, fz + dr)[0], c_in(mod, fz - dr)[0]
        sp_, _ = phase_satz(mod, fz + dr, [d_wert], RTOL_HAUPT, mod.xb)
        sm_, _ = phase_satz(mod, fz - dr, [d_wert], RTOL_HAUPT, mod.xb)
        kp_, km_ = innen_moden(mod, fz + dr)[0], innen_moden(mod, fz - dr)[0]
        abl.append({"delta_rho": dr, "dc_in_drho": (cp_ - cm_) / (2.0 * dr),
                    "dphi_drho": wrap_pi(sp_[0]["phi"] - sm_[0]["phi"]) / (2.0 * dr), "dk_drho": (kp_ - km_) / (2.0 * dr)})
        log(f"Ableitungen delta {dr:g}: dc_in/drho = {abl[-1]['dc_in_drho']:.6e}, dphi/drho = "
            f"{abl[-1]['dphi_drho']:.6e}, dk/drho = {abl[-1]['dk_drho']:.6f}")
    out["ableitungen"] = abl
    out["e1_M_e1"] = float(e1 @ M_ABL @ e1)
    out["ende"] = jetzt()
    out["sek"] = time.time() - T_START
    schreibe(args.out, out)
    log("phase fertig")


# ----------------------------------------------------------------------------------------------------------------------
# Kommando formel
# ----------------------------------------------------------------------------------------------------------------------

def x_w_1d(eps, beta):
    ar = (1.0 - 8.0 * beta * eps) / (2.0 * math.sqrt(beta * eps))
    return math.acosh(ar) / math.sqrt(1.0 / beta - 4.0 * eps)


def cmd_formel(args):
    K = lade(args.konfig)
    P = lade(args.phase)
    beta = float(K["beta"])
    if abs(float(P["beta"]) - beta) > 0.0:
        raise ValueError("beta der Phase passt nicht")
    k, phi = float(P["k_in"]), float(P["phi"])
    kap, Sc = float(P["kappa_in"]), float(P["S_c"])
    eps_lo, eps_hi = K["eps_bereich"]
    l_lo, l_hi = -math.log(eps_hi), -math.log(eps_lo)

    def Phi(ell):
        return k * x_w_1d(math.exp(-ell), beta) + phi

    gitter = np.linspace(l_lo, l_hi, 20001)
    werte = np.array([Phi(float(x)) for x in gitter])
    monoton = bool(np.all(np.diff(werte) > 0.0))
    m_lo = int(math.ceil(Phi(l_lo) / (0.5 * math.pi)))
    m_hi = int(math.floor(Phi(l_hi) / (0.5 * math.pi)))
    abl = P["ableitungen"][0]
    cpl, dcin = float(P["c_plus"]), float(abl["dc_in_drho"])
    dphi, dk = float(abl["dphi_drho"]), float(abl["dk_drho"])
    e1Me1 = float(P["e1_M_e1"])
    liste = []
    for m in range(m_lo, m_hi + 1):
        ell = brentq(lambda x: Phi(x) - 0.5 * math.pi * m, l_lo, l_hi, xtol=1e-14, rtol=1e-15, maxiter=200)
        eps = math.exp(-ell)
        xw = x_w_1d(eps, beta)
        dPhi = (Phi(ell + 1e-6) - Phi(ell - 1e-6)) / 2e-6
        b = math.sqrt(1.0 / beta - 4.0 * eps)
        e_bxw = math.exp(-b * xw)
        # Abschaetzungen (nur berichtet, nicht angepasst; PLAN.md Abschnitt 3.4)
        dphi_a = e1Me1 / (2.0 * k) * Sc * e_bxw / b
        s = 1.0 if m % 2 == 0 else -1.0
        drho_b = s * cpl / dcin * math.exp(-2.0 * kap * xw)
        dphi_b = (dk * xw + dphi) * drho_b
        liste.append({"m": m, "par": "gerade" if m % 2 == 0 else "ungerade", "ell": ell, "eps": eps,
                      "omega2": 1.0 - 1.0 / (4.0 * beta) + eps, "x_w": xw, "Phi": Phi(ell), "dPhi_dell": dPhi,
                      "abschaetzung_plateau_dell": -dphi_a / dPhi, "abschaetzung_e2_drho": drho_b,
                      "abschaetzung_e2_dell": -dphi_b / dPhi})
    liste.sort(key=lambda x: x["eps"])
    for i in range(len(liste) - 1):
        liste[i]["schritt_zur_naechsten"] = liste[i]["ell"] - liste[i + 1]["ell"]
    # Gueltigkeit der Phase (PLAN.md Abschnitt 6, K-Phase)
    gk = {"e2_wachsend_rel": P["e2_wachsend_rel"], "e2_ok": P["e2_wachsend_rel"] <= 1e-4,
          "tiefen_streuung_ab_16": max(abs(s["phi_minus_gewertet"]) for s in P["tiefen"] if s["d_in_sqrtbeta"] >= 15.999),
          "gegenproben_max_dphi": max(abs(g["d_phi"]) for g in P["gegenproben"].values()),
          "rho_z_abw_R24": P["rho_z"] - float(K["rho_z_r24"])}
    gk["tiefen_ok"] = gk["tiefen_streuung_ab_16"] <= 1e-5
    gk["gegenproben_ok"] = gk["gegenproben_max_dphi"] <= 1e-5
    gk["rho_z_ok"] = abs(gk["rho_z_abw_R24"]) <= 1e-8
    gk["gueltig"] = gk["e2_ok"] and gk["tiefen_ok"] and gk["gegenproben_ok"] and gk["rho_z_ok"] and monoton
    out = {"kommando": "formel", "beginn": BEGINN, "konfig": K, "phase_datei": args.phase, "beta": beta,
           "k_in": k, "phi": phi, "rho_z": P["rho_z"], "lambda_pi_durch_k": math.pi / (math.sqrt(beta) * k),
           "eps_bereich": [eps_lo, eps_hi], "Phi_monoton": monoton, "m_bereich": [m_lo, m_hi], "K_phase": gk,
           "phase_gueltig": gk["gueltig"], "sprossen": liste, "ende": jetzt()}
    schreibe(args.out, out)
    log(f"formel beta {beta}: {len(liste)} Lagen in [{eps_lo:g}, {eps_hi:g}], Phi monoton {monoton}, K-Phase {gk}")
    for x in liste:
        log(f"  m = {x['m']:3d} {x['par']:8s} ln(1/eps) = {x['ell']:.6f} eps = {x['eps']:.4e}")


# ----------------------------------------------------------------------------------------------------------------------
# Kommando vergleich (mechanische Regel)
# ----------------------------------------------------------------------------------------------------------------------

def cmd_vergleich(args):
    K = lade(args.konfig)
    F = lade(args.formel)
    S = lade(args.sprossen)
    vor = F["sprossen"]
    gem = sorted([{"par": x["par"], "ell": float(x["ell"]), "eps": float(x["eps"]), "rho": x.get("rho")}
                  for x in S[K["sprossen_feld"]]], key=lambda x: x["eps"])
    tol = float(K["toleranz_rel"])
    e_lo, e_hi = K["eps_wertung"]
    zeilen = []
    for g in gem:
        v = min(vor, key=lambda v: abs(v["ell"] - g["ell"]))
        dl = v["ell"] - g["ell"]
        z = {**g, "vorhersage_m": v["m"], "vorhersage_par": v["par"], "vorhersage_ell": v["ell"],
             "vorhersage_eps": v["eps"], "d_ell": dl, "d_ell_rel": dl / g["ell"],
             "paritaet_ok": v["par"] == g["par"], "lage_ok": abs(dl) <= tol * g["ell"],
             "gewertet": bool(e_lo <= g["eps"] < e_hi)}
        z["getroffen"] = z["paritaet_ok"] and z["lage_ok"]
        zeilen.append(z)
    gew = [z for z in zeilen if z["gewertet"]]
    m_benutzt = [z["vorhersage_m"] for z in gew]
    eindeutig = len(set(m_benutzt)) == len(m_benutzt)
    ohne = []
    for v in vor:
        if not (e_lo <= v["eps"] < e_hi):
            continue
        if not any(g["par"] == v["par"] and abs(v["ell"] - g["ell"]) <= tol * g["ell"] for g in gem):
            ohne.append({"m": v["m"], "par": v["par"], "ell": v["ell"], "eps": v["eps"]})
    k0_ok = bool(S.get("K0", {}).get("bestanden", False))
    phase_ok = bool(F.get("phase_gueltig", False))
    ein = (len(gew) >= int(K["min_anzahl"]) and all(z["getroffen"] for z in gew) and eindeutig and k0_ok and
           phase_ok)
    out = {"kommando": "vergleich", "beginn": BEGINN, "konfig": K, "formel_datei": args.formel,
           "sprossen_datei": args.sprossen, "name": K["name"], "zeilen": zeilen, "anzahl_gewertet": len(gew),
           "zuordnung_eindeutig": eindeutig, "vorhersagen_ohne_partner_im_wertungsbereich": ohne,
           "K0_sprossen_bestanden": k0_ok, "phase_gueltig": phase_ok, "eingetroffen": ein, "ende": jetzt()}
    if len(gew) < int(K["min_anzahl"]):
        out["grund"] = f"weniger als {K['min_anzahl']} gewertete Sprossen (nicht auswertbar)"
    if not (k0_ok and phase_ok):
        out["grund_k"] = "K0 der Sprossen-Datei oder K-Phase nicht bestanden (nicht auswertbar)"
    schreibe(args.out, out)
    log(f"{K['name']}: eingetroffen {ein} ({len(gew)} gewertet, eindeutig {eindeutig}, ohne Partner {len(ohne)})")
    for z in zeilen:
        log(f"  {z['par']:8s} ln(1/eps) {z['ell']:.6f} <-> m {z['vorhersage_m']} {z['vorhersage_par']:8s} "
            f"{z['vorhersage_ell']:.6f}: d = {z['d_ell']:+.5f} ({100 * z['d_ell_rel']:+.3f} %), gewertet {z['gewertet']}, "
            f"getroffen {z['getroffen']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="kommando", required=True)
    a = sp.add_parser("phase")
    a.add_argument("--konfig", required=True)
    a.add_argument("--out", required=True)
    a = sp.add_parser("formel")
    a.add_argument("--konfig", required=True)
    a.add_argument("--phase", required=True)
    a.add_argument("--out", required=True)
    a = sp.add_parser("vergleich")
    a.add_argument("--konfig", required=True)
    a.add_argument("--formel", required=True)
    a.add_argument("--sprossen", required=True)
    a.add_argument("--out", required=True)
    args = ap.parse_args()
    log(f"phase_wand {args.kommando} Beginn {BEGINN}, argv {sys.argv[1:]}")
    {"phase": cmd_phase, "formel": cmd_formel, "vergleich": cmd_vergleich}[args.kommando](args)


if __name__ == "__main__":
    main()
