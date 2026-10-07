#!/usr/bin/env python3
"""EVO-1 (Runde 7, runden-v3): Evolutions-Pilot. Breite der l = 0-Atmung eines Q-Balls ueber eine Modellfamilie. Explorativ.

Plan: ../GAUNTLET-NEUSTART-PLAN.md. Schwellen, Abweichungen und Befehle: PLAN.md (dieser Ordner).
Familie P: U = S - S^2 + beta S^3 + gamma S^4 (Anker beta = 1/2, gamma = 0). Familie L: U = ln(1 + S) wie in
RUNDE-07/bic2/bic2.py (ohne freien Parameter; eigenes Schiessen in f0, weil das Teilchenpotential keinen Buckel hat).
Rechenkern: resonanz3d.py ist eine unveraenderte Kopie aus RUNDE-06/resonanz3d (sha256 99c54b9c...). Modellabhaengig
und deshalb hier ersetzt: koeffizienten, g_u, g_strich (fuer gamma = 0 rufen sie die Originale, also bitgleich),
lin_aufbau (dp = U' + S U'', sp = S U''), Ladung und Energie in dim Dimensionen.
Unterbefehle: modell | generation | zusammenfassen | rauch. float64, ein CPU-Thread. Nach jedem Punkt wird zustand.json
gesichert; ein Punkt beginnt nur, wenn seine geschaetzte Dauer ins Budget passt, sonst endet der Aufruf mit "offen" und
derselbe Befehl setzt fort. Kein Punkt wird abgebrochen.
Version 1: 2026-09-30 04:53. Version 2: 2026-09-30 05:11:22, nach dem Absturz der 1D-Kontrolle auf der .69 und vor
jeder Bewertung. x_schaetz faengt den Nenner null ab (x_est = xs[k], Vermerk "Nullnenner" in zustand.json und
modell.json); dazu kommt Rauchtest-Teil 0. Schwellen und Entscheidungsregeln sind unveraendert, bei Nenner ungleich null
rechnet x_schaetz wie Version 1.
"""
import argparse
import glob
import json
import math
import os
import random
import sys

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import resonanz3d as r3  # noqa: E402

STUFEN = {"A": (0.02, 1e-6), "B": (0.01, 1e-8), "C": (0.005, 1e-10)}   # h der linearen ODE, f_rand (wie R6)
N_SCAN, W2_OBEN, W2_ABST = 12, 0.93, 0.02
FEIN = (-0.02, -0.002, -0.0005, 0.0005, 0.002, 0.02)
KASTEN_IM, NEWTON_ABSD, MAX_MIN = -0.1, 1e-8, 3
SUCHE = {"n_res": 700, "n_fl": 160, "n_kante": 240, "runden": 8, "max": 6000}
SCHAETZ = {"start": 150.0, "A": 40.0, "B": 90.0, "C": 200.0, "umlauf": 90.0}   # Sekunden, bis gemessen
# Schwellen, vor dem ersten Modell festgelegt (PLAN.md, Abschnitt 3)
F0_W2MIN, F0_PROFILE, F1_WMIN = 0.02, 10, 3
F2_R2, F2_G0_REL, F2_BC_REL, F2_BC_ABS = 0.99, 1e-3, 0.05, 1e-9
BOX = {"beta": (0.15, 1.2), "gamma": (0.0, 0.3)}
RASTER1 = ([0.2, 0.35, 0.5, 0.75, 1.0], [0.0, 0.1, 0.2])
VERSCHIEDEN = (0.05, 0.02)


# ================================================================ Potentiale

def pot_von(fam, beta=0.0, gamma=0.0):
    return {"fam": "P", "beta": float(beta), "gamma": float(gamma)} if fam == "P" else {"fam": "L"}


POT_L = {"fam": "L"}


def U(pot, S):
    if pot["fam"] == "P":
        return S - S * S + pot["beta"] * S ** 3 + pot["gamma"] * S ** 4
    return math.log1p(S)


def dpsp(pot, s):
    """dp = U' + S U'', sp = S U'' und d/dS davon; fuer gamma = 0 dieselben Ausdruecke wie resonanz3d.lin_aufbau."""
    if pot["fam"] == "P":
        b, g = pot["beta"], pot["gamma"]
        return (1.0 - 4.0 * s + 9.0 * b * s * s + 16.0 * g * s ** 3, -2.0 * s + 6.0 * b * s * s + 12.0 * g * s ** 3,
                -4.0 + 18.0 * b * s + 48.0 * g * s * s, -2.0 + 12.0 * b * s + 36.0 * g * s * s)
    e = 1.0 / (1.0 + s)
    return e * e, -s * e * e, -2.0 * e ** 3, (s - 1.0) * e ** 3


def w2_min(pot):
    """min_S U(S)/S (untere Existenzgrenze); L: Infimum 0, nur asymptotisch (S -> unendlich)."""
    if pot["fam"] == "L":
        return 0.0
    b, g = pot["beta"], pot["gamma"]
    if g == 0.0 and b <= 0.0:
        return -math.inf
    sm = 2.0 / (2.0 * b + math.sqrt(4.0 * b * b + 12.0 * g))
    return 1.0 - sm + b * sm * sm + g * sm ** 3


_KOEFF, _G_U, _G_STRICH = r3.koeffizienten, r3.g_u, r3.g_strich


def koeffizienten(a0, pot):
    """Buckel f_top = sqrt(S+) von F(f) = a0 f - 2 f^3 + 3 beta f^5 + 4 gamma f^7 und Taylor-Koeffizienten c1..c7."""
    if pot["gamma"] == 0.0:
        return _KOEFF(a0, pot["beta"])
    b, g = pot["beta"], pot["gamma"]

    def q(S):
        return a0 - 2.0 * S + 3.0 * b * S * S + 4.0 * g * S ** 3
    sc = 4.0 / (6.0 * b + math.sqrt(36.0 * b * b + 96.0 * g))     # Minimum von q fuer S > 0
    if q(sc) >= 0.0:
        raise ValueError("kein Buckel")
    lo, hi = sc, 2.0 * sc + 1.0
    while q(hi) <= 0.0:
        hi *= 2.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        lo, hi = (m, hi) if q(m) < 0.0 else (lo, m)
    t = math.sqrt(0.5 * (lo + hi))
    a = [0.0, a0, 0.0, -2.0, 0.0, 3.0 * b, 0.0, 4.0 * g]
    return t, tuple(sum(a[j] * math.comb(j, k) * t ** (j - k) for j in range(k, 8)) for k in range(1, 8))


def g_u(u, c):
    if len(c) == 5:
        return _G_U(u, c)
    acc = c[-1] if len(c) % 2 else -c[-1]
    for k in range(len(c) - 1, 0, -1):
        acc = (c[k - 1] if k % 2 else -c[k - 1]) + u * acc
    return u * acc


def g_strich(u, c):
    if len(c) == 5:
        return _G_STRICH(u, c)
    n = len(c)
    acc = n * c[-1] * (1.0 if n % 2 else -1.0)
    for k in range(n - 1, 0, -1):
        acc = k * c[k - 1] * (1.0 if k % 2 else -1.0) + u * acc
    return acc


r3.koeffizienten, r3.g_u, r3.g_strich = koeffizienten, g_u, g_strich


def profil_log(w2, dim, h, dev, f_schwanz=1e-5, n_kand=1024, r_max=130.0, runden=6):
    """U = ln(1 + S): Schiessen in f0 > f_1 (omega^2 S_1 = ln(1 + S_1)). Ueberschuss f < 0 (f0 zu gross), Unterschuss
    f' > 0 (f0 zu klein). Schluessel wie resonanz3d.profil."""
    a0, dm1, d = 1.0 - w2, dim - 1.0, float(dim)

    def F(f):
        return f * (a0 - w2 * f * f) / (1.0 + f * f)
    lo, hi = 1e-12, 1.0
    while w2 * hi - math.log1p(hi) <= 0.0:
        hi *= 2.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        lo, hi = (lo, m) if w2 * m - math.log1p(m) > 0.0 else (m, hi)
    f_lo, f_hi = math.sqrt(hi), 4.0 * math.sqrt(hi) + 4.0
    n_max = int(round(r_max / h))

    def schritt(r, f, p):
        def ab(rr, ff, pp):
            return pp, F(ff) - (dm1 / rr) * pp
        k1 = ab(r, f, p)
        k2 = ab(r + 0.5 * h, f + 0.5 * h * k1[0], p + 0.5 * h * k1[1])
        k3 = ab(r + 0.5 * h, f + 0.5 * h * k2[0], p + 0.5 * h * k2[1])
        k4 = ab(r + h, f + h * k3[0], p + h * k3[1])
        return (f + h / 6.0 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), p + h / 6.0 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))

    def start(f0):
        a = F(f0) / (2.0 * d)
        return f0 + a * h * h, 2.0 * a * h
    for _ in range(runden):
        f0 = torch.linspace(f_lo, f_hi, n_kand, dtype=torch.float64, device=dev)
        f, p = start(f0)
        zu = torch.zeros_like(f0)
        for k in range(1, n_max):
            f, p = schritt(k * h, f, p)
            zu = zu + ((zu == 0) & (f < 0)).double() - ((zu == 0) & (f >= 0) & (p > 0)).double()
            lebt = (zu == 0).double()
            f, p = f * lebt + (1 - lebt) * 0.0, p * lebt
            if k % 100 == 0 and not bool((zu == 0).any()):
                break
        if bool((zu < 0).any()):
            f_lo = max(f_lo, float(f0[zu < 0].max()))
        if bool((zu > 0).any()):
            f_hi = min(f_hi, float(f0[zu > 0].min()))
    f0 = torch.tensor([f_lo, 0.5 * (f_lo + f_hi), f_hi], dtype=torch.float64, device=dev)
    f, p = start(f0)
    fl, pl = [float(f0[1]), float(f[1])], [0.0, float(p[1])]
    grund, j = 0, 1
    while j < n_max:
        f, p = schritt(j * h, f, p)
        j += 1
        fm = float(f[1])
        if fm < f_schwanz * float(f0[1]) or float(p[1]) > 0 or fm < 0 or abs(float(f[2] - f[0])) > 1e-2 * abs(fm):
            grund = 1 if fm < f_schwanz * float(f0[1]) else (2 if float(p[1]) > 0 else (3 if fm < 0 else 4))
            break
        fl.append(fm)
        pl.append(float(p[1]))
    jc = len(fl) - 1
    return {"w2": w2, "dim": dim, "beta": {"fam": "L"}, "h": h, "t": None, "f0": fl[0], "f2": F(fl[0]) / (2.0 * d),
            "s": None, "klammer": f_hi - f_lo, "rueckfall": False, "j_cut": jc, "r_cut": jc * h, "grund": grund,
            "streuung_cut": 0.0, "f": fl, "fp": pl, "kappa": math.sqrt(a0), "dm1": dm1}


def profil(w2, dim, pot, h, dev):
    return r3.profil(w2, dim, pot, h, dev) if pot["fam"] == "P" else profil_log(w2, dim, h, dev)


def lin_aufbau(prof, h, f_rand, pot, r_min=20.0):
    """wie resonanz3d.lin_aufbau, dp und sp aus dpsp(pot, S)."""
    if abs(prof["h"] - 0.5 * h) > 1e-12:
        raise ValueError("Profil braucht Schritt h/2")
    r_aus = max(r_min, r3.radius_wo(prof, f_rand * prof["f0"]))
    K = int(math.ceil(r_aus / h))
    Km = max(1, min(K - 1, int(round(r3.r_halb(prof) / h))))
    f, _ = r3.f_werte(prof, 2 * K + 1)
    dv, sv, cf = [], [], [0.0]
    for j in range(2 * K + 1):
        d, s, _, _ = dpsp(pot, f[j] ** 2)
        dv.append(d)
        sv.append(s)
        if j > 0:
            cf.append(1.0 / (j * 0.5 * h) ** 2)
    s0, s2 = prof["f0"] ** 2, 2.0 * prof["f0"] * prof["f2"]
    d0, sp0, d1, sp1 = dpsp(pot, s0)
    return {"h": h, "K": K, "Km": Km, "R_aus": K * h, "r_m": Km * h, "omega": math.sqrt(prof["w2"]), "dv": dv, "sv": sv,
            "cf": cf, "reihe": (d0, d1 * s2, sp0, sp1 * s2), "frei": False, "dev": None}


def ladung_energie(prof, pot, dim):
    w2, h = prof["w2"], prof["h"]
    n = int(r3.radius_wo(prof, 1e-12 * prof["f0"]) / h) + 2
    f, fp = r3.f_werte(prof, n)
    fl = 2.0 * math.pi ** (0.5 * dim) / math.gamma(0.5 * dim)
    iq = ie = 0.0
    for j in range(n):
        g = (0.5 * h if j in (0, n - 1) else h) * (j * h) ** (dim - 1)
        s = f[j] ** 2
        iq += g * s
        ie += g * (w2 * s + fp[j] ** 2 + U(pot, s))
    q = 2.0 * math.sqrt(w2) * fl * iq
    return {"Q": q, "E": fl * ie, "EQ": fl * ie / q}


# ================================================================ Punkte, Pole, Kontur

def cz(z):
    return [z.real, z.imag]


def zc(x):
    return complex(x[0], x[1])


def kasten(w2):
    om = math.sqrt(w2)
    return 1.0 - om + 0.002, min(1.0 + om - 0.002, 9.0)


def punkt(w2, stufe, pot, dim, dev, keim=None):
    h, fr = STUFEN[stufe]
    t0 = r3.uhr()
    e = {"w2": w2, "stufe": stufe}
    try:
        prof = profil(w2, dim, pot, 0.5 * h, dev)
        lin = lin_aufbau(prof, h, fr, pot)
        lin["dev"] = dev
    except Exception as ex:                                      # Profil nicht gefunden
        e.update(profil_ok=False, fehler=repr(ex), sek=r3.uhr() - t0)
        return e, None
    ok = prof["f"][prof["j_cut"]] < 1e-3 * prof["f0"]
    e.update(profil_ok=ok, S0=prof["f0"] ** 2, grund=prof["grund"], r_cut=prof["r_cut"], R_aus=lin["R_aus"])
    e.update(ladung_energie(prof, pot, dim))
    if keim is not None and ok:
        e.update(newton_pol(lin, w2, keim, 0.5 * (dim - 1.0)))
    e["sek"] = r3.uhr() - t0
    return e, lin


def newton_pol(lin, w2, keim, nu):
    w = r3.newton(lin, [keim], [nu], iters=25)[0]
    x0, x1 = kasten(w2)
    z = w["rho"]
    return {"rho": cz(z), "Gamma": -z.imag, "absD": w["absD"], "iter": w["iter"],
            "pol_ok": bool(w["konvergiert"] and w["absD"] < NEWTON_ABSD and x0 < z.real < x1 and z.imag < 0.001)}


def pole_suche(lin, w2, nu):
    x0, x1 = kasten(w2)
    nr, n2 = SUCHE["n_res"], SUCHE["n_fl"]
    xs = [x0 + (x1 - x0) * i / (nr - 1) for i in range(nr)]
    D = r3.det_liste(lin, [complex(x, 0.0) for x in xs], [nu] * nr)
    keime = [complex(xs[k], -1e-4) for k in r3.lokale_minima([abs(z) for z in D])]
    xs2 = [x0 + (x1 - x0) * i / (n2 - 1) for i in range(n2)]
    ims = [-0.003, -0.01, -0.03, -0.07]
    D = r3.det_liste(lin, [complex(x, y) for y in ims for x in xs2], [nu] * (n2 * len(ims)))
    for i, y in enumerate(ims):
        keime += [complex(xs2[k], y) for k in r3.lokale_minima([abs(z) for z in D[i * n2:(i + 1) * n2]])]
    pole = []
    for w in r3.newton(lin, keime, [nu] * len(keime), iters=25):
        z = w["rho"]
        if (w["konvergiert"] and w["absD"] < NEWTON_ABSD and x0 < z.real < x1 and KASTEN_IM < z.imag < 0.001
                and not any(abs(p - z) < 1e-7 for p in pole)):
            pole.append(z)
    return sorted(pole, key=lambda z: -z.imag)                   # schmalster zuerst


def umlauf(lin, w2, nu):
    x0, x1 = kasten(w2)
    nk = SUCHE["n_kante"]
    k = r3.kontur(lin, [nu], x0, x1, KASTEN_IM, 0.001, (nk, 20, 2 * nk, 20), SUCHE["runden"], SUCHE["max"])[nu]
    return {"umlauf": k["umlauf"], "umlauf_roh": k["umlauf_roh"], "aufgeloest": k["aufgeloest"], "punkte": k["punkte"]}


# ================================================================ Kommando modell

def scan_punkte(pot):
    lo = max(w2_min(pot), 0.0) + W2_ABST
    return [lo + (W2_OBEN - lo) * i / (N_SCAN - 1) for i in range(N_SCAN)]


def schluessel(pot, dim):
    return f"P_b{pot['beta']:.4f}_g{pot['gamma']:.4f}_d{dim}" if pot["fam"] == "P" else f"L_d{dim}"


class Lauf:
    def __init__(self, a, pot, dim, dev):
        self.a, self.pot, self.dim, self.dev, self.nu = a, pot, dim, dev, 0.5 * (dim - 1.0)
        self.pfad = os.path.join(a.out, "zustand.json")
        if os.path.exists(self.pfad):
            with open(self.pfad) as fh:
                self.z = json.load(fh)
        else:
            self.z = {"key": schluessel(pot, dim), "pot": pot, "dim": dim, "w2min": w2_min(pot), "grob": {},
                      "fein": {}, "zusatz": {}, "zeiten": {}, "aufrufe": []}
        self.offen = None

    def sichern(self):
        tmp = self.pfad + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(r3.jsonfest(self.z), fh, indent=1)
        os.replace(tmp, self.pfad)

    def darf(self, art, faktor=1.0):
        s = max(self.z["zeiten"].get(art, 0.0) * 1.3, SCHAETZ[art] if art not in self.z["zeiten"] else 0.0) * faktor
        if r3.uhr() + s < self.a.budget:
            return True
        self.offen = f"{art} (Schaetzung {s:.0f} s, Uhr {r3.uhr():.0f} s)"
        return False

    def zeit(self, art, sek):
        self.z["zeiten"][art] = max(self.z["zeiten"].get(art, 0.0), sek)

    def grob(self):
        xs = scan_punkte(self.pot)
        self.z["scan"] = xs
        k0 = N_SCAN // 2
        self.z["k0"] = k0
        g = self.z["grob"]
        if str(k0) not in g:
            if not self.darf("start"):
                return False
            t0 = r3.uhr()
            e, lin = punkt(xs[k0], "A", self.pot, self.dim, self.dev)
            if lin is not None and e["profil_ok"]:
                pole = pole_suche(lin, xs[k0], self.nu)
                e["start_pole"] = [cz(p) for p in pole]
                e["start_umlauf"] = umlauf(lin, xs[k0], self.nu)
                if pole:
                    e.update(newton_pol(lin, xs[k0], pole[0], self.nu))
            e["sek"] = r3.uhr() - t0
            g[str(k0)] = e
            self.zeit("start", e["sek"])
            self.sichern()
        for richtung in (1, -1):
            k = k0 + richtung
            while 0 <= k < N_SCAN:
                if str(k) not in g:
                    if not self.darf("A"):
                        return False
                    v1, v2 = g.get(str(k - richtung), {}), g.get(str(k - 2 * richtung), {})
                    keim = None
                    if v1.get("pol_ok"):
                        keim = zc(v1["rho"])
                        if v2.get("pol_ok"):
                            keim += (keim - zc(v2["rho"])) * (xs[k] - xs[k - richtung]) / (xs[k - richtung] - xs[k - 2 * richtung])
                    e, _ = punkt(xs[k], "A", self.pot, self.dim, self.dev, keim=keim)
                    g[str(k)] = e
                    self.zeit("A", e["sek"])
                    self.sichern()
                k += richtung
        return True

    def spur(self):
        """zusammenhaengende Polspur um k0 (Stufe A): Liste der k."""
        g, k0 = self.z["grob"], self.z["k0"]
        if not g.get(str(k0), {}).get("pol_ok"):
            return []
        ks = [k0]
        for richtung in (1, -1):
            k = k0 + richtung
            while 0 <= k < N_SCAN and g.get(str(k), {}).get("pol_ok"):
                ks.append(k)
                k += richtung
        return sorted(ks)

    def grob_minima(self):
        """innere lokale Minima der groben Breite auf der Polspur, tiefstes zuerst, hoechstens MAX_MIN."""
        g, ks = self.z["grob"], self.spur()
        G = [g[str(k)]["Gamma"] for k in ks]
        return sorted([ks[i] for i in r3.lokale_minima(G)], key=lambda k: g[str(k)]["Gamma"])[:MAX_MIN]

    def x_schaetz(self, k):
        """(x_est, hinweis). Version 2: Nenner null (Breiten unter der Aufloesung, nach max(Gamma, 0) alle 0) ->
        x_est = xs[k], hinweis "Nullnenner"; sonst dieselbe Rechnung wie Version 1."""
        xs, g = self.z["scan"], self.z["grob"]
        gl, gm, gr = (max(g[str(j)]["Gamma"], 0.0) ** 0.5 for j in (k - 1, k, k + 1))
        if gl < gr:                                              # Nullstelle zwischen k-1 und k
            if gl + gm > 0.0:
                return xs[k - 1] + (xs[k] - xs[k - 1]) * gl / (gl + gm), None
        elif gm + gr > 0.0:
            return xs[k] + (xs[k + 1] - xs[k]) * gm / (gm + gr), None
        return xs[k], "Nullnenner"

    def keim_grob(self, x):
        xs, g, ks = self.z["scan"], self.z["grob"], self.spur()
        best = min(ks, key=lambda k: abs(xs[k] - x))
        nb = [k for k in (best - 1, best + 1) if k in ks]
        z0 = zc(g[str(best)]["rho"])
        if not nb:
            return z0
        k2 = nb[0] if len(nb) == 1 else (nb[1] if x > xs[best] else nb[0])
        return z0 + (zc(g[str(k2)]["rho"]) - z0) * (x - xs[best]) / (xs[k2] - xs[best])

    def fein(self, k):
        fz = self.z["fein"].setdefault(str(k), {"A": {}, "B": {}, "C": {}})
        if "x_est" not in fz:
            fz["x_est"], hinweis = self.x_schaetz(k)
            if hinweis:
                fz["hinweis"] = hinweis
        xs = [fz["x_est"] + d for d in FEIN]
        fz["x"] = xs
        for st in ("A", "B"):
            for i, x in enumerate(xs):
                if str(i) in fz[st]:
                    continue
                if not self.darf(st):
                    return False
                vor = fz["A"].get(str(i), {}) if st == "B" else {}
                keim = zc(vor["rho"]) if vor.get("pol_ok") else self.keim_grob(x)
                e, _ = punkt(x, st, self.pot, self.dim, self.dev, keim=keim)
                fz[st][str(i)] = e
                self.zeit(st, e["sek"])
                self.sichern()
        B = [fz["B"][str(i)] for i in range(6)]
        if not all(b.get("pol_ok") for b in B):
            return True                                          # Stufe B unvollstaendig: nicht entscheidbar
        tief = sorted(range(6), key=lambda i: B[i]["Gamma"])[:2]
        for i in tief:
            if str(i) not in fz["C"]:
                if not self.darf("C"):
                    return False
                e, _ = punkt(xs[i], "C", self.pot, self.dim, self.dev, keim=zc(B[i]["rho"]))
                fz["C"][str(i)] = e
                self.zeit("C", e["sek"])
                self.sichern()
        if "umlauf" not in fz:
            if not self.darf("umlauf"):
                return False
            t0 = r3.uhr()
            e, lin = punkt(xs[tief[0]], "B", self.pot, self.dim, self.dev)
            fz["umlauf"] = umlauf(lin, xs[tief[0]], self.nu) if lin is not None else {"umlauf": None}
            fz["umlauf"]["i"] = tief[0]
            self.zeit("umlauf", r3.uhr() - t0)
            self.sichern()
        return True

    def zusatz(self):
        zs = self.z.setdefault("zusatz", {})
        for x in self.a.zusatz:
            if str(x) in zs:
                continue
            if not self.darf("C", 1.6):
                return False
            kand = [(abs(xx - x), zc(fz["B"][str(i)]["rho"])) for fz in self.z["fein"].values()
                    for i, xx in enumerate(fz.get("x", [])) if fz["B"].get(str(i), {}).get("pol_ok")]
            keim = min(kand, key=lambda t: t[0])[1] if kand else self.keim_grob(x)
            eb, _ = punkt(x, "B", self.pot, self.dim, self.dev, keim=keim)
            ec = punkt(x, "C", self.pot, self.dim, self.dev, keim=zc(eb["rho"]))[0] if eb.get("pol_ok") else None
            zs[str(x)] = {"B": eb, "C": ec}
            self.sichern()
        return True

    def rechne(self):
        t0 = r3.jetzt()
        v = bewerte(self.z)
        if v.get("naechstes") == "grob" and self.grob():
            v = bewerte(self.z)
        if v.get("naechstes") == "fein":
            if all(self.fein(k) for k in v["zu_verfeinern"]):
                self.zusatz()
            v = bewerte(self.z)
        if v["status"] != "fertig" and self.offen is None:
            self.offen = v.get("naechstes", "?")
        self.z["aufrufe"].append({"start": t0, "ende": r3.jetzt(), "sek": r3.uhr(), "offen": self.offen})
        self.sichern()
        with open(os.path.join(self.a.out, "modell.json"), "w") as fh:
            json.dump(r3.jsonfest(v), fh, indent=1)
        return v


# ================================================================ Bewertung F0 bis F3

def fit_linear(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    p1 = sxy / sxx
    p0 = my - p1 * mx
    sst = sum((b - my) ** 2 for b in y)
    ssr = sum((b - p0 - p1 * a) ** 2 for a, b in zip(x, y))
    return p0, p1, (1.0 - ssr / sst) if sst > 0 else 0.0


def fit_parabel(x, G):
    """Gamma = c (x - x*)^2 + g0, kleinste Quadrate relativ (Gewicht 1/max(Gamma, 1e-9)); Rueckgabe c, x*, g0."""
    xm = sum(x) / len(x)
    zeilen = [[(a - xm) ** 2 / max(g, F2_BC_ABS), (a - xm) / max(g, F2_BC_ABS), 1.0 / max(g, F2_BC_ABS)] for a, g in zip(x, G)]
    rs = [g / max(g, F2_BC_ABS) for g in G]
    A = torch.tensor(zeilen, dtype=torch.float64)
    b = torch.tensor(rs, dtype=torch.float64).unsqueeze(1)
    c, bb, cc = torch.linalg.lstsq(A, b).solution.squeeze(1).tolist()
    if c <= 0:
        return c, float("nan"), float("nan")
    return c, xm - bb / (2.0 * c), cc - bb * bb / (4.0 * c)


def f2_auswertung(x, GB):
    """Kriterien e bis h (PLAN.md, Abschnitt 3) an den 6 Feinpunkten, Stufe B."""
    im = min(range(6), key=lambda i: GB[i])
    best = None
    for grenze in (im, im + 1):                                  # Vorzeichenwechsel links oder rechts vom Tiefpunkt
        if 1 <= grenze <= 5:
            a = [(1.0 if i < grenze else -1.0) * max(GB[i], 0.0) ** 0.5 for i in range(6)]
            p0, p1, r2 = fit_linear(x[1:5], a[1:5])              # Gerade durch die vier inneren Punkte
            if best is None or r2 > best[2]:
                best = (p0, p1, r2, grenze)
    c, xq, g0 = fit_parabel(x, GB)
    g_ref = min(GB[0], GB[5])
    xl = -best[0] / best[1] if best[1] else float("nan")
    teile = {"e Tiefpunkt innen": 1 <= im <= 4, "f R2 innen >= 0,99": best[2] >= F2_R2,
             "g x* im Feinbereich": bool(x[0] <= xl <= x[5] and x[0] <= xq <= x[5]),
             "h g0 <= 1e-3 Gamma_ref": bool(g0 <= F2_G0_REL * g_ref)}
    return {"i_tief": im, "R2_lin": best[2], "vz_grenze": best[3], "x_stern_lin": xl, "c": c, "x_stern": xq, "g0": g0,
            "Gamma_ref": g_ref, "g0_rel": g0 / g_ref if g_ref > 0 else float("inf"), "F2_teile": teile,
            "F2_ok": all(teile.values())}


def bewerte_min(z, k, W, xs):
    """ein verfeinertes grobes Minimum: Messmittel-Pruefungen a bis d, dann F2 (e bis h) und F3."""
    fz = z["fein"].get(str(k))
    r = {"k": k, "x_grob": xs[k], "status": "offen"}
    if not fz:
        return r
    if fz.get("hinweis"):
        r["hinweis"] = fz["hinweis"]
    B = [fz["B"].get(str(i), {}) for i in range(6)]
    if len(fz["B"]) == 6 and not all(b.get("pol_ok") for b in B):
        r.update(status="fertig", F2="nicht entscheidbar", grund="a) Stufe B ohne Pol")
        return r
    if "umlauf" not in fz:
        return r
    x = fz["x"]
    GA = [fz["A"].get(str(i), {}).get("Gamma") for i in range(6)]
    GB = [b["Gamma"] for b in B]
    im = min(range(6), key=lambda i: GB[i])
    C = fz["C"].get(str(im)) or {}
    reihenfolge = None not in GA and sorted(range(6), key=lambda i: GA[i]) == sorted(range(6), key=lambda i: GB[i])
    bc = abs(GB[im] - C["Gamma"]) if C.get("pol_ok") else float("inf")
    bc_ok = bc < F2_BC_REL * abs(C.get("Gamma", 0.0)) + F2_BC_ABS
    um = fz["umlauf"]
    um_ok = um.get("umlauf") == 1 and bool(um.get("aufgeloest"))
    r.update(status="fertig", x_est=fz["x_est"], x_fein=x, Gamma_A=GA, Gamma_B=GB,
             Gamma_C={i: fz["C"][i].get("Gamma") for i in fz["C"]}, reihenfolge_AB=reihenfolge, BC_abw=bc, BC_ok=bc_ok,
             umlauf_tief=um, rho_tief=B[im]["rho"], Q_tief=B[im]["Q"])
    r.update(f2_auswertung(x, GB))
    if not (reihenfolge and bc_ok and um_ok):
        r.update(F2="nicht entscheidbar", grund=f"b) Reihenfolge A/B {reihenfolge}, c) B-C {bc_ok}, d) Umlauf "
                                                f"{um.get('umlauf')} aufgeloest {um.get('aufgeloest')}")
        return r
    r["F2"] = "ja" if r["F2_ok"] else "nein"
    if r["F2"] == "ja":
        xq, xw = r["x_stern"], [xs[j] for j in W]
        br = [j for j in range(N_SCAN - 1) if xs[j] <= xq < xs[j + 1]]
        r["F3"] = "ja" if br and br[0] in W and br[0] + 1 in W else "nein"
        if xw:
            r["abstand_W"] = [xq - min(xw), max(xw) - xq]
    return r


def bewerte(z):
    pot, dim = z["pot"], z["dim"]
    v = {"key": z["key"], "pot": pot, "dim": dim, "w2min": z["w2min"], "F0": None, "F1": None, "F2": None, "F3": None,
         "qualifiziert": False, "status": "offen"}
    if pot["fam"] == "P" and not float(z["w2min"]) >= F0_W2MIN:
        v.update(F0="nein", status="fertig", urteil="nicht lebensfaehig", grund=f"min U/S = {float(z['w2min']):.4f} < {F0_W2MIN}")
        return v
    g = z["grob"]
    if len(g) < N_SCAN:
        v["naechstes"] = "grob"
        return v
    xs = z["scan"]
    pk = [k for k in range(N_SCAN) if g[str(k)].get("profil_ok")]
    v["profile"] = len(pk)
    if len(pk) < F0_PROFILE:
        v.update(F0="nein (Profile)", status="fertig", urteil="nicht entscheidbar", grund=f"Profile an {len(pk)} von 12")
        return v
    v["F0"] = "ja"
    W = []
    for i, k in enumerate(pk):
        a, b = pk[max(0, i - 1)], pk[min(len(pk) - 1, i + 1)]
        dq = (g[str(b)]["Q"] - g[str(a)]["Q"]) / (xs[b] - xs[a])
        g[str(k)]["dQdw2"] = dq
        if dq < 0 and g[str(k)]["EQ"] < 1.0:
            W.append(k)
    v["W"] = [xs[k] for k in W]
    v["F1"] = "ja" if len(W) >= F1_WMIN else "nein"
    k0 = z["k0"]
    s0 = g[str(k0)]
    v["start_pole"] = s0.get("start_pole")
    v["start_umlauf"] = s0.get("start_umlauf")
    lauf = Lauf.__new__(Lauf)
    lauf.z = z
    ks = lauf.spur()
    v["spur"] = [xs[k] for k in ks]
    v["grob_Gamma"] = {f"{xs[k]:.5f}": g[str(k)]["Gamma"] for k in ks}
    if not ks:
        um = s0.get("start_umlauf") or {}
        if um.get("umlauf") == 0 and um.get("aufgeloest"):
            v.update(F2="nein", status="fertig", urteil="nicht qualifiziert", grund="kein l = 0-Pol im Kasten")
        else:
            v.update(F2="nicht entscheidbar", status="fertig", urteil="nicht entscheidbar", grund="Startpol nicht gefunden")
        return v
    if len(ks) < 3:
        v.update(F2="nicht entscheidbar", status="fertig", urteil="nicht entscheidbar", grund="Polspur kuerzer als 3")
        return v
    mins = lauf.grob_minima()
    v["grob_minima"] = [xs[j] for j in mins]
    if not mins:
        v.update(F2="nein", status="fertig", urteil="nicht qualifiziert", grund="kein lokales Minimum der Breite")
        return v
    if v["F1"] != "ja":
        v.update(F2="grob Minimum, nicht verfeinert", status="fertig", urteil="nicht qualifiziert", grund="F1 (Filter)")
        return v
    v["zu_verfeinern"] = mins
    rs = [bewerte_min(z, k, W, xs) for k in mins]
    v["minima"] = rs
    if any(r.get("hinweis") for r in rs):
        v["hinweise"] = [f"{r['x_grob']:.5f}: {r['hinweis']}" for r in rs if r.get("hinweis")]
    if any(r["status"] != "fertig" for r in rs) or not all(str(x) in z.get("zusatz", {}) for x in z.get("zusatz_soll", [])):
        v["naechstes"] = "fein"
        return v
    v["status"] = "fertig"
    v["zusatz"] = {k2: {s: (e or {}).get("Gamma") for s, e in val.items()} for k2, val in z.get("zusatz", {}).items()}
    ja = [r for r in rs if r.get("F2") == "ja"]
    if not ja and any(r.get("F2") == "nicht entscheidbar" for r in rs):
        v.update(F2="nicht entscheidbar", urteil="nicht entscheidbar",
                 grund="; ".join(r["grund"] for r in rs if r.get("F2") == "nicht entscheidbar"))
        return v
    q = [r for r in ja if r.get("F3") == "ja"]
    kand = q or ja or [r for r in rs if isinstance(r.get("g0_rel"), float)]
    if kand:
        best = min(kand, key=lambda r: r["g0_rel"] if r["g0_rel"] == r["g0_rel"] else math.inf)
        v.update(x_stern=best["x_stern"], x_stern_lin=best["x_stern_lin"], g0_rel=best["g0_rel"], R2_lin=best["R2_lin"])
    v["F2"] = "ja" if ja else "nein"
    v["F3"] = ("ja" if q else "nein") if ja else None
    v["qualifiziert"] = v["F0"] == v["F1"] == v["F2"] == v["F3"] == "ja"
    v["urteil"] = "qualifiziert" if v["qualifiziert"] else "nicht qualifiziert"
    return v


def kommando_modell(a):
    dev = torch.device("cpu")
    torch.set_num_threads(1)
    pot = pot_von(a.familie, a.beta, a.gamma)
    os.makedirs(a.out, exist_ok=True)
    lauf = Lauf(a, pot, a.dim, dev)
    lauf.z["zusatz_soll"] = a.zusatz
    print(f"EVO-1 modell {lauf.z['key']} Start {r3.jetzt()}, Budget {a.budget:.0f} s, torch {torch.__version__}", flush=True)
    v = lauf.rechne()
    kurz = {k: v.get(k) for k in ("key", "status", "urteil", "grund", "F0", "F1", "F2", "F3", "x_stern", "g0_rel",
                                  "R2_lin", "W", "grob_minima", "zusatz", "hinweise")}
    print(json.dumps(r3.jsonfest(kurz), indent=1), flush=True)
    print(f"Ende {r3.jetzt()}, {r3.uhr():.1f} s, offen: {lauf.offen}", flush=True)


# ================================================================ Kommando generation

def eintrag(pot, dim, arm, grund, eltern=None, erg_aus=None):
    key = schluessel(pot, dim)
    arg = (f"--familie P --beta {pot['beta']:.4f} --gamma {pot['gamma']:.4f}" if pot["fam"] == "P" else "--familie L")
    e = {"key": key, "pot": pot, "dim": dim, "arm": arm, "eltern": eltern or [], "grund": grund,
         "befehl": f"evo1.py modell {arg} --dim {dim} --out ergebnisse/{key}"}
    if erg_aus:
        e["ergebnis_aus"] = erg_aus
    return e


def lade(gen_dateien, erg):
    """alle Modelle frueherer Generationen mit Arm und Bewertung (modell.json)."""
    alle = []
    for d in sorted(gen_dateien):
        with open(d) as fh:
            gen = json.load(fh)
        for m in gen["modelle"]:
            p = os.path.join(erg, m["key"], "modell.json")
            v = json.load(open(p)) if os.path.exists(p) else None
            alle.append(dict(m, nr=gen["nr"], v=v))
    return alle


def fitness(m):
    v = m["v"] or {}
    stufe = sum(1 for f in ("F0", "F1", "F2", "F3") if v.get(f) == "ja")
    g0r = v.get("g0_rel")
    return (0 if v.get("qualifiziert") else 1, -stufe, g0r if isinstance(g0r, (int, float)) else math.inf)


def kappen(b, g):
    return (round(min(max(b, BOX["beta"][0]), BOX["beta"][1]), 4), round(min(max(g, BOX["gamma"][0]), BOX["gamma"][1]), 4))


def kommando_generation(a):
    nr, seed = a.nr, a.seed if a.seed is not None else 1000 + a.nr
    mod = []
    if nr == 0:
        mod.append(eintrag(pot_von("P", 0.5, 0.0), 3, "anker", "A1: Anker aus Runde 6"))
        mod[-1]["befehl"] += " --zusatz 0.798"
        mod.append(eintrag(pot_von("P", 0.5, 0.0), 1, "kontrolle", "A1: Negativkontrolle dim = 1, muss an F2 scheitern"))
    elif nr == 1:
        for b in RASTER1[0]:
            for g in RASTER1[1]:
                erg = "Generation 0 (Anker)" if (b, g) == (0.5, 0.0) else None
                mod.append(eintrag(pot_von("P", b, g), 3, "raster1", "gemeinsames Raster (Plan, Abschnitt 7)", erg_aus=erg))
        mod.append(eintrag(POT_L, 3, "log", "Log-Potential wie BIC-2 (b); einziges Modell der Familie"))
        rz = random.Random(seed)
        for _ in range(2):
            b, g = kappen(rz.uniform(*BOX["beta"]), rz.uniform(*BOX["gamma"]))
            mod.append(eintrag(pot_von("P", b, g), 3, "Z", f"Zufall, seed {seed}"))
    else:
        dateien = [d for d in glob.glob(os.path.join(a.gen_ordner, "gen-*.json")) if json.load(open(d))["nr"] < nr]
        alle = [m for m in lade(dateien, a.vorige) if m["pot"]["fam"] == "P" and m["dim"] == 3 and m["nr"] >= 1]
        bekannt = {(m["pot"]["beta"], m["pot"]["gamma"]) for m in alle}
        # Arm E: Eltern aus Generation 1 (gemeinsam) und frueheren E-Modellen
        pool = sorted([m for m in alle if m["nr"] == 1 or m["arm"] == "E"], key=fitness)
        eltern = pool[:4]
        if not eltern:
            raise SystemExit("keine bewerteten Modelle aus Generation 1: --vorige pruefen")
        quali = [m for m in eltern if (m["v"] or {}).get("qualifiziert")]
        rng = random.Random(seed)
        n_kreuz = 4 if len(quali) >= 2 else 0
        for i in range(8 - n_kreuz):
            p = eltern[i % len(eltern)]
            b, g = kappen(p["pot"]["beta"] + rng.gauss(0.0, 0.08), p["pot"]["gamma"] + rng.gauss(0.0, 0.03))
            mod.append(eintrag(pot_von("P", b, g), 3, "E", "Mutation", eltern=[p["key"]]))
        for _ in range(n_kreuz):
            p, q = rng.sample(quali, 2)
            w = rng.choice([0.25, 0.5, 0.75])
            b, g = kappen(w * p["pot"]["beta"] + (1 - w) * q["pot"]["beta"], w * p["pot"]["gamma"] + (1 - w) * q["pot"]["gamma"])
            mod.append(eintrag(pot_von("P", b, g), 3, "E", f"Kreuzung w = {w}", eltern=[p["key"], q["key"]]))
        # Arm R: Zellmitten mit Umschlag von F2 oder F3 auf dem Raster der Stufe nr - 2, dann Halbschritt-Raster
        pool_r = [m for m in alle if m["nr"] == 1 or m["arm"] == "R"]
        erg = {(m["pot"]["beta"], m["pot"]["gamma"]): ((m["v"] or {}).get("F2"), (m["v"] or {}).get("F3")) for m in pool_r}
        B, G = list(RASTER1[0]), list(RASTER1[1])
        for _ in range(nr - 2):
            B = sorted(set(B) | {round(0.5 * (B[i] + B[i + 1]), 4) for i in range(len(B) - 1)})
            G = sorted(set(G) | {round(0.5 * (G[i] + G[i + 1]), 4) for i in range(len(G) - 1)})
        kand = []
        for i in range(len(B) - 1):
            for j in range(len(G) - 1):
                ecken = [erg[(b, g)] for b in (B[i], B[i + 1]) for g in (G[j], G[j + 1]) if (b, g) in erg]
                if len(set(ecken)) > 1:
                    kand.append(kappen(0.5 * (B[i] + B[i + 1]), 0.5 * (G[j] + G[j + 1])))
        B2 = sorted(set(B) | {round(0.5 * (B[i] + B[i + 1]), 4) for i in range(len(B) - 1)})
        G2 = sorted(set(G) | {round(0.5 * (G[i] + G[i + 1]), 4) for i in range(len(G) - 1)})
        kand += [(b, g) for b in B2 for g in G2]
        gewaehlt = []
        for bg in kand:
            if bg not in bekannt and bg not in gewaehlt:
                gewaehlt.append(bg)
            if len(gewaehlt) == 8:
                break
        for b, g in gewaehlt:
            mod.append(eintrag(pot_von("P", b, g), 3, "R", "Rasterregel (Umschlagzelle oder Halbschritt)"))
        rz = random.Random(seed + 1)
        for _ in range(2):
            b, g = kappen(rz.uniform(*BOX["beta"]), rz.uniform(*BOX["gamma"]))
            mod.append(eintrag(pot_von("P", b, g), 3, "Z", f"Zufall, seed {seed + 1}"))
        mod.insert(0, {"eltern_liste": [m["key"] for m in eltern], "hinweis": "Leitung darf Eltern im Arm E mit Grund tauschen"})
    aus = {"nr": nr, "seed": seed, "erzeugt": r3.jetzt(), "modelle": [m for m in mod if "key" in m],
           "info": [m for m in mod if "key" not in m]}
    with open(a.out, "w") as fh:
        json.dump(aus, fh, indent=1)
    for m in aus["modelle"]:
        print(f"{m['arm']:9s} {m['key']:28s} {m['befehl']}")


# ================================================================ Kommando zusammenfassen

def verschieden(p, q):
    if p["fam"] != q["fam"]:
        return True
    if p["fam"] == "L":
        return False
    return abs(p["beta"] - q["beta"]) >= VERSCHIEDEN[0] or abs(p["gamma"] - q["gamma"]) >= VERSCHIEDEN[1]


def kommando_zusammenfassen(a):
    dateien = sorted(d for d in glob.glob(os.path.join(a.gen_ordner, "gen-*.json")) if json.load(open(d))["nr"] <= a.gen)
    alle = lade(dateien, a.ergebnisse)
    diese = [m for m in alle if m["nr"] == a.gen]
    zeilen = ["| Modell | Arm | Status | F0 | F1 | F2 | F3 | omega*^2 | g0/Gamma_ref | R2 | Urteil, Grund |", "|---|" * 1 + "---|" * 10]
    with open(os.path.join(a.gen_ordner, f"bew-{a.gen:03d}.jsonl"), "w") as fh:
        for m in diese:
            v = m["v"] or {"status": "nicht bewertet"}
            fh.write(json.dumps(r3.jsonfest({"key": m["key"], "arm": m["arm"], "nr": m["nr"], "eltern": m["eltern"], "v": v})) + "\n")
            def zf(x, f):
                return format(x, f) if isinstance(x, float) else ("" if x is None else str(x))
            zeilen.append(f"| {m['key']} | {m['arm']} | {v.get('status')} | {v.get('F0')} | {v.get('F1')} | {v.get('F2')} | "
                          f"{v.get('F3')} | {zf(v.get('x_stern'), '.5f')} | {zf(v.get('g0_rel'), '.1e')} | "
                          f"{zf(v.get('R2_lin'), '.4f')} | {v.get('urteil')}; {v.get('grund', '')} |")
    print("\n".join(zeilen))
    fertig = [m for m in diese if (m["v"] or {}).get("status") == "fertig"]
    lebens = [m for m in fertig if m["v"].get("F0") == "ja"]
    quali = [m for m in fertig if m["v"].get("qualifiziert")]
    unent = [m for m in fertig if m["v"].get("urteil") == "nicht entscheidbar"]
    print(f"\nGeneration {a.gen}: {len(diese)} Modelle, fertig {len(fertig)}, lebensfaehig {len(lebens)}, "
          f"qualifiziert {len(quali)}, nicht entscheidbar {len(unent)}")
    if diese:
        print(f"A3 (nicht entscheidbar > 20 %): {len(unent) / len(diese):.0%} -> {'Abbruch' if len(unent) > 0.2 * len(diese) else 'weiter'}")
    if a.gen == 0:
        an = next((m["v"] for m in diese if m["arm"] == "anker"), None) or {}
        ko = next((m["v"] for m in diese if m["arm"] == "kontrolle"), None) or {}
        g798 = (an.get("zusatz") or {}).get("0.798", {})
        gw = g798.get("C") or g798.get("B")
        lagen = [r.get("x_stern") for r in an.get("minima", []) if r.get("F2") == "ja"]
        a1 = (any(isinstance(x, float) and 0.797 <= x <= 0.799 for x in lagen) and isinstance(gw, float)
              and 0.5 * 1.12e-7 <= gw <= 2 * 1.12e-7 and ko.get("F2") == "nein")
        print(f"A1: Anker omega*^2 (F2 ja) = {lagen}, Gamma(0,798) = {gw}, F2 Anker {an.get('F2')}; "
              f"Kontrolle dim 1 F2 = {ko.get('F2')} -> {'bestanden' if a1 else 'NICHT bestanden'}")
    if a.gen == 1 and lebens:
        anteil = len(quali) / len(lebens)
        print(f"A2 Trennschaerfe: {len(quali)}/{len(lebens)} = {anteil:.0%} -> {'trennt' if 0.05 <= anteil <= 0.9 else 'trennt NICHT'}")
    fruehe = [m for m in alle if m["nr"] <= 1 and (m["v"] or {}).get("qualifiziert")]
    neu = {}
    for arm in ("E", "R", "Z"):
        gez = []
        for m in [m for m in alle if m["nr"] >= 2 and m["arm"] == arm and (m["v"] or {}).get("qualifiziert")]:
            if all(verschieden(m["pot"], q["pot"]) for q in fruehe + gez):
                gez.append(m)
        neu[arm] = gez
        n_arm = len([m for m in alle if m["nr"] >= 2 and m["arm"] == arm])
        print(f"Arm {arm}: {n_arm} Modelle in Generation 2+, neue verschiedene qualifizierte {len(gez)}")
    if a.gen >= 2:
        ne, nr_ = len(neu["E"]), len(neu["R"])
        print(f"Vorsprung (nur nach Generation 3 bindend): N_E = {ne}, N_R = {nr_}; N_E >= 1,5 N_R und N_E >= N_R + 3: "
              f"{ne >= 1.5 * nr_ and ne >= nr_ + 3}")


# ================================================================ Kommando rauch

def kommando_rauch(a):
    """Code laeuft durch (Zahlen der Kleinstufen ohne Bedeutung) plus drei Pruefungen mit Soll."""
    torch.set_num_threads(1)
    dev = torch.device("cpu")
    out = a.out or "rauch"
    os.makedirs(out, exist_ok=True)
    z = []

    class Z(list):
        def append(self, x):
            print(x, flush=True)
            super().append(x)
    z = Z(["EVO-1 rauch " + r3.jetzt()])
    if a.nur_ablauf:
        return rauch_ablauf(a, z, out, dev)
    # 0. x_schaetz bei Breiten unter der Aufloesung (Version 1: ZeroDivisionError); Version 1 hier wortgleich zum Vergleich
    def x_alt(xs, G, k):
        gl, gm, gr = (max(G[j], 0.0) ** 0.5 for j in (k - 1, k, k + 1))
        if gl < gr:
            return xs[k - 1] + (xs[k] - xs[k - 1]) * gl / (gl + gm)
        return xs[k] + (xs[k + 1] - xs[k]) * gm / (gm + gr)
    xs0 = scan_punkte(pot_von("P", 0.5, 0.0))
    faelle = {   # 1D-Kontrolle: Stufe-A-Werte der .69 (Generation 0), monoton fallend, am Ende unter der Aufloesung
        "1D .69": [4.431e-3, 4.501e-3, 1.903e-3, 6.618e-4, 2.012e-4, 5.281e-5, 1.143e-5, 1.886e-6, 2.061e-7, 1.0392e-8,
                   -9.859e-10, -8.506e-10],
        "alle null": [1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 0.0, 0.0, 0.0, 0.0, 0.0],
        "links null": [1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, -1e-10, -3e-10, 1e-9, 2e-9, 3e-9],
        "normal, ausgedacht": [2.2e-2, 1.0e-3, 3.0e-4, 1.4e-3, 1.8e-3, 1.9e-3, 1.8e-3, 3.63e-4, 3.25e-4, 1.0e-3, 8.0e-4, 4.0e-4]}
    for name, G in faelle.items():
        lz = Lauf.__new__(Lauf)
        lz.z = {"scan": xs0, "grob": {str(j): {"Gamma": G[j]} for j in range(len(G))}}
        for k in [i for i in r3.lokale_minima(G)]:
            try:
                alt = f"{x_alt(xs0, G, k):.6f}"
            except ZeroDivisionError:
                alt = "ZeroDivisionError"
            neu = lz.x_schaetz(k)
            gleich = "" if alt == "ZeroDivisionError" else f", gleich Version 1: {x_alt(xs0, G, k) == neu[0]}"
            z.append(f"0 x_schaetz {name}, Minimum bei {xs0[k]:.5f}: Version 1 {alt}; Version 2 {neu[0]:.6f} {neu[1]}{gleich}")
    # 1. Taylor-Koeffizienten: allgemeine Formel gegen Original (gamma = 0), und gamma > 0 exakt (F(f_top) = 0)
    t0, c0 = _KOEFF(0.3, 0.5)
    pg = {"fam": "P", "beta": 0.5, "gamma": 1e-300}
    t1, c1 = koeffizienten(0.3, pg)
    z.append(f"1 Koeffizienten gamma -> 0: |dt| = {abs(t1 - t0):.1e}, max|dc| = {max(abs(x - y) for x, y in zip(c0, c1[:5])):.1e}, "
             f"c6, c7 = {c1[5]:.1e}, {c1[6]:.1e} (Soll: alle ~1e-15)")
    tg, cg = koeffizienten(0.3, {"fam": "P", "beta": 0.5, "gamma": 0.1})
    Fg = 0.3 * tg - 2 * tg ** 3 + 1.5 * tg ** 5 + 0.4 * tg ** 7
    z.append(f"  gamma = 0,1: F(f_top) = {Fg:.1e}; G(u) aus Taylor gegen direkt bei u = 0,3: "
             f"{abs(float(g_u(torch.tensor(0.3, dtype=torch.float64), cg)) - (-(0.3 * (tg - 0.3) - 2 * (tg - 0.3) ** 3 + 1.5 * (tg - 0.3) ** 5 + 0.4 * (tg - 0.3) ** 7))):.1e}")
    # 2. Auswertung an synthetischen Kurven (muss bestehen UND scheitern koennen)
    for name, gfun, soll in (("anker-artig", lambda u: (-1.04 * u + 6.8 * u * u) ** 2, "ja"),
                             ("Boden 1e-6", lambda u: (-1.04 * u + 6.8 * u * u) ** 2 + 1e-6, "nein"),
                             ("monoton 1D-artig", lambda u: 1e-8 * math.exp(-77.0 * u), "nein")):
        xe = 0.79768 + 0.0024
        x = [xe + d for d in FEIN]
        G = [gfun(xx - 0.79768) for xx in x]
        f = f2_auswertung(x, G)
        z.append(f"2 {name}: Tiefpunkt {f['i_tief']}, R2 innen {f['R2_lin']:.5f}, x*lin {f['x_stern_lin']:.5f}, x* {f['x_stern']:.5f}, "
                 f"g0 {f['g0']:.2e}, g0/Gref {f['g0_rel']:.1e}, Teile {list(f['F2_teile'].values())} -> "
                 f"F2 {'ja' if f['F2_ok'] else 'nein'} (Soll {soll})")
    # 3. echter Punkt Stufe A bei 0,7 (R6-Anker, Stufe A: 1,7018102190 - 1,468e-3 i) und Zeit je Punkt
    e, lin = punkt(0.7, "A", pot_von("P", 0.5, 0.0), 3, dev, keim=complex(1.7018, -1.5e-3))
    z.append(f"3 Anker 0,7 Stufe A: rho = {e.get('rho')}, Q = {e['Q']:.3f}, E/Q = {e['EQ']:.4f}, {e['sek']:.1f} s "
             f"(Soll R6: 1,7018102 - 1,468e-3 i; Q(0,7) aus R6-Profil nicht gedruckt)")
    e, lin = punkt(0.8, "A", pot_von("P", 0.5, 0.1), 3, dev, keim=complex(1.74, -1e-3))
    z.append(f"  gamma = 0,1 bei 0,8 Stufe A: rho = {e.get('rho')}, pol_ok {e.get('pol_ok')}, Q = {e['Q']:.3f}, {e['sek']:.1f} s")
    if r3.uhr() < 60:
        e, _ = punkt(0.5, "A", POT_L, 3, dev)
        z.append(f"  Log bei 0,5 Stufe A: Profil ok {e['profil_ok']}, S0 = {e.get('S0')}, Q = {e.get('Q')}, Grund {e.get('grund')}, {e['sek']:.1f} s")
    z.append(f"Ende Teil 1 bis 3 {r3.jetzt()}, {r3.uhr():.1f} s")
    with open(os.path.join(out, "rauch_bericht.txt"), "w") as fh:
        fh.write("\n".join(z) + "\n")


def rauch_ablauf(a, z, out, dev):
    """4. Ablauf modell in Kleinstufen (Zahlen ohne Bedeutung), 6 statt 12 Scanpunkte; fortsetzbar."""
    global N_SCAN, F0_PROFILE
    N_SCAN, F0_PROFILE = 6, 5
    STUFEN.update({"A": (0.08, 1e-5), "B": (0.04, 1e-6), "C": (0.02, 1e-6)})
    SUCHE.update({"n_res": 80, "n_fl": 30, "n_kante": 40, "runden": 2, "max": 600})
    SCHAETZ.update({"start": 5.0, "A": 1.0, "B": 2.0, "C": 3.0, "umlauf": 3.0})
    ns = argparse.Namespace(out=os.path.join(out, "anker-klein"), budget=a.budget - 5.0, zusatz=[0.798])
    os.makedirs(ns.out, exist_ok=True)
    lauf = Lauf(ns, pot_von("P", 0.5, 0.0), 3, dev)
    lauf.z["zusatz_soll"] = ns.zusatz
    v = lauf.rechne()
    z.append(f"4 Ablauf Kleinstufen: Status {v['status']}, offen {lauf.offen}, F0..F3 {v.get('F0')}/{v.get('F1')}/{v.get('F2')}/"
             f"{v.get('F3')}, Minima {v.get('grob_minima')}, x* {v.get('x_stern')}, Zeiten {lauf.z['zeiten']}")
    z.append(f"Minima: {json.dumps(r3.jsonfest([{k: m.get(k) for k in ('x_grob', 'status', 'F2', 'F3', 'x_stern', 'R2_lin', 'g0_rel', 'grund')} for m in v.get('minima', [])]))}")
    z.append(f"Zusatz: {v.get('zusatz')}; Urteil {v.get('urteil')}")
    z.append(f"Ende {r3.jetzt()}, {r3.uhr():.1f} s")
    with open(os.path.join(out, "rauch_ablauf.txt"), "a") as fh:
        fh.write("\n".join(z) + "\n")
    print("\n".join(z), flush=True)


def main():
    ap = argparse.ArgumentParser(description="EVO-1: Evolutions-Pilot (Breite der l = 0-Atmung)")
    sub = ap.add_subparsers(dest="kommando", required=True)
    m = sub.add_parser("modell")
    m.add_argument("--familie", default="P", choices=["P", "L"])
    m.add_argument("--beta", type=float, default=0.5)
    m.add_argument("--gamma", type=float, default=0.0)
    m.add_argument("--dim", type=int, default=3, choices=[1, 3])
    m.add_argument("--out", required=True)
    m.add_argument("--budget", type=float, default=540.0)
    m.add_argument("--zusatz", type=lambda s: [float(x) for x in s.split(",")], default=[])
    g = sub.add_parser("generation")
    g.add_argument("--nr", type=int, required=True)
    g.add_argument("--vorige", default="ergebnisse", help="Ergebnisordner (enthaelt <key>/modell.json)")
    g.add_argument("--gen-ordner", dest="gen_ordner", default=".")
    g.add_argument("--seed", type=int, default=None)
    g.add_argument("--out", required=True)
    s = sub.add_parser("zusammenfassen")
    s.add_argument("--gen", type=int, required=True)
    s.add_argument("--ergebnisse", default="ergebnisse")
    s.add_argument("--gen-ordner", dest="gen_ordner", default=".")
    r = sub.add_parser("rauch")
    r.add_argument("--out", default=None)
    r.add_argument("--budget", type=float, default=110.0)
    r.add_argument("--nur-ablauf", dest="nur_ablauf", action="store_true", help="nur Teil 4 (fortsetzbar)")
    a = ap.parse_args()
    {"modell": kommando_modell, "generation": kommando_generation, "zusammenfassen": kommando_zusammenfassen,
     "rauch": kommando_rauch}[a.kommando](a)


if __name__ == "__main__":
    main()
