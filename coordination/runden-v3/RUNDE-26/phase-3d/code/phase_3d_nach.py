#!/usr/bin/env python3
"""PHASE-3D (Runde 26), Code-Agent (Claude, Anthropic) fuer die Leitung claude-primary, 03.10.2026.
NACHLAUF-FASSUNG (nach dem Einfrieren, offen benannte Abweichung, ERGEBNIS.md): Kopie von phase_3d.py (eingefroren
20261003-050006) mit zwei Aenderungen, beide mit "NACHLAUF" markiert: (1) phase vermerkt rho_n ausserhalb des ebenen
Fensters, statt abzubrechen; (2) auswertung rechnet die Zusatzform ueberall, wo rho_n bekannt ist, die Nebenform nur, wo
die ebene Phase definiert ist. Haupt-Delta, K-Profil und Regeln sind unveraendert.
Karte: coordination/runden-v3/RUNDE-26/phase-3d/KARTE.md, Plan: PLAN.md daneben.

3D-Profil (l = 0) des Modells M1, U = S - S^2 + beta S^3, S = f^2:
    f'' + (2/r) f' = F(f) = (1 - omega^2) f - 2 f^3 + 3 beta f^5,   f'(0) = 0,  f -> 0.
Schiessen in u = t - f wie bic2.profil (RUNDE-13): t = sqrt(S_top), S_top = groessere Wurzel von U'(S) = omega^2,
u'' + (2/r) u' = G(u) = -F(t - u) (Taylor-Polynom, exakt), Startwert u(0) = e^(-s), Bisektion in s:
grosses s -> Ueberschuss (f < 0), kleines s -> Unterschuss (f' > 0).
Halbhoehenradius R (Konvention PHASE-WAND): S(R) = S_c/2, S_c = 1/(2 beta), also u(R) = t - sqrt(S_c/2).
Abweichung je Sprosse: x = [k_in R + phi]/pi - 1/2, Delta = x - ceil(x - 1/2) in (-1/2, 1/2].

Verfahren fuer R ("name:wert"):
  rk4:h       eigenes klassisches RK4 mit festem Schritt h (reines Python), R per kubischer Hermite-Interpolation
  dop853:rtol scipy DOP853 mit Ereignissen, R als Ereignis auf der dichten Ausgabe
  bic2:h      bic2_3d_praez.profil (RUNDE-13, unveraendert, torch auf der CPU) mit Profilschritt h, R per Hermite

Kommandos (Zahlenparameter und Sprossenlagen nur aus Dateien):
  profile    --konfig K --out O   R je Sprosse mit den Verfahren der Konfiguration (dazu dR/d omega^2)
  phase      --konfig K --out O   ebene Wand bei omega_min (phase_wand.py, unveraendert): phi(rho), k_in(rho)
  auswertung --konfig K --out O   Delta (Haupt-, Neben-, Zusatzform), Ausgleich, Kontrollen, mechanische Regeln
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

T_START = time.time()
S_LO_ABSTAND = 1e-3      # Unterschuss-Start der Bisektion: f(0) = 1e-3 (wie bic2: lo0 = -ln(t - 1e-3))
S_HI = 150.0             # Ueberschuss-Start der Bisektion (wie bic2: hi0 = 150)
R_MAX = 400.0
TOL_S = 1e-13            # Bisektion bis (hi - lo) < TOL_S * max(1, hi)
IT_MAX = 120
PROTOKOLL = False        # True: jede Bahn der Bisektion ins Log (nur Rauchlauf)
U_UM = 1e-3              # DOP853: Umschaltpunkt der Toleranz (u = U_UM)
ATOL2 = 1e-15            # DOP853: absolute Toleranz ab u = U_UM


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


def frac_halb(x):
    """x - ceil(x - 1/2): Bruchteil in (-1/2, 1/2], dazu die ganze Zahl."""
    m = math.ceil(x - 0.5)
    return x - m, m


# ----------------------------------------------------------------------------------------------------------------------
# Profil: Parameter, G(u), Start, Hermite
# ----------------------------------------------------------------------------------------------------------------------

class Par:
    def __init__(self, beta, w2):
        self.beta, self.w2 = float(beta), float(w2)
        a0 = 1.0 - self.w2
        disk = 4.0 - 12.0 * self.beta * a0
        if disk <= 0.0:
            raise ValueError("kein Buckel: 4 - 12 beta a0 <= 0")
        s_top = (2.0 + math.sqrt(disk)) / (6.0 * self.beta)
        t = math.sqrt(s_top)
        b = self.beta
        self.c = (a0 - 6.0 * s_top + 15.0 * b * s_top * s_top, -6.0 * t + 30.0 * b * t * s_top,
                  -2.0 + 30.0 * b * s_top, 15.0 * b * t, 3.0 * b)
        self.a0, self.s_top, self.t = a0, s_top, t
        self.Sc = 1.0 / (2.0 * b)
        self.f_w = math.sqrt(0.5 * self.Sc)
        self.u_w = t - self.f_w
        self.omega_min2 = 1.0 - 1.0 / (4.0 * b)
        self.eps = self.w2 - self.omega_min2

    def G(self, u):
        c1, c2, c3, c4, c5 = self.c
        return u * (c1 + u * (-c2 + u * (c3 + u * (-c4 + u * c5))))

    def Gp(self, u):
        c1, c2, c3, c4, c5 = self.c
        return c1 + u * (-2.0 * c2 + u * (3.0 * c3 + u * (-4.0 * c4 + u * 5.0 * c5)))

    def start(self, s, r0):
        """Reihe u = u0 + a r^2 + b r^4 (dim = 3), Werte bei r0."""
        u0 = math.exp(-s)
        a = self.G(u0) / 6.0
        b = self.Gp(u0) * a / 20.0
        return u0, u0 + a * r0 * r0 + b * r0 ** 4, 2.0 * a * r0 + 4.0 * b * r0 ** 3


def hermite_wurzel(r0, y0, p0, r1, y1, p1, ziel):
    """Kubische Hermite-Interpolation auf [r0, r1] (Werte y, Ableitungen p), Wurzel von H(r) = ziel per Bisektion."""
    h = r1 - r0

    def H(tau):
        t2, t3 = tau * tau, tau * tau * tau
        return ((2 * t3 - 3 * t2 + 1) * y0 + (t3 - 2 * t2 + tau) * h * p0 + (-2 * t3 + 3 * t2) * y1
                + (t3 - t2) * h * p1 - ziel)
    lo, hi = 0.0, 1.0
    flo = H(lo)
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        fm = H(mid)
        if (fm < 0.0) == (flo < 0.0):
            lo, flo = mid, fm
        else:
            hi = mid
    return r0 + 0.5 * (lo + hi) * h


# ----------------------------------------------------------------------------------------------------------------------
# Bahnen: RK4 (fester Schritt) und DOP853 (Ereignisse)
# ----------------------------------------------------------------------------------------------------------------------

def bahn_rk4(P, s, h):
    """Rueckgabe (Klasse, R, r_ende, u0); Klasse 'ueber' (u > t), 'unter' (u' < 0) oder 'offen'."""
    G = P.G
    t, uw = P.t, P.u_w
    u0, u, p = P.start(s, h)
    if p < 0.0:
        return "unter", None, h, u0
    r = h
    R = None
    n = int(R_MAX / h)
    h2, h6 = 0.5 * h, h / 6.0
    for _ in range(1, n):
        rm, rn = r + h2, r + h
        k1u, k1p = p, G(u) - 2.0 / r * p
        u2, p2 = u + h2 * k1u, p + h2 * k1p
        k2u, k2p = p2, G(u2) - 2.0 / rm * p2
        u3, p3 = u + h2 * k2u, p + h2 * k2p
        k3u, k3p = p3, G(u3) - 2.0 / rm * p3
        u4, p4 = u + h * k3u, p + h * k3p
        k4u, k4p = p4, G(u4) - 2.0 / rn * p4
        un = u + h6 * (k1u + 2.0 * k2u + 2.0 * k3u + k4u)
        pn = p + h6 * (k1p + 2.0 * k2p + 2.0 * k3p + k4p)
        if R is None and u < uw <= un:
            R = hermite_wurzel(r, u, p, rn, un, pn, uw)
        if un > t:
            return "ueber", R, rn, u0
        if pn < 0.0:
            return "unter", R, rn, u0
        r, u, p = rn, un, pn
    return "offen", R, r, u0


def bahn_dop(P, s, rtol, r0=0.01):
    G = P.G
    t, uw = P.t, P.u_w
    u0, us, ps = P.start(s, r0)
    if ps < 0.0:
        return "unter", None, r0, u0

    def rhs(r, y):
        return [y[1], G(y[0]) - 2.0 / r * y[1]]

    def ev_ueber(r, y):
        return y[0] - t
    ev_ueber.terminal, ev_ueber.direction = True, 1

    def ev_unter(r, y):
        return y[1]
    ev_unter.terminal, ev_unter.direction = True, -1

    def ev_w(r, y):
        return y[0] - uw
    ev_w.terminal, ev_w.direction = False, 1

    def ev_um(r, y):
        return y[0] - U_UM
    ev_um.terminal, ev_um.direction = True, 1
    # Zwei Abschnitte (Rauchlaeufe 2 bis 4): bis u = U_UM atol relativ zu u0 (u waechst von e^(-s) an); danach
    # atol = ATOL2 absolut. Mit atol << 1e-15 im Schwanz (u nahe t) bestimmt das Rundungsrauschen von G(u) die Schrittweite.
    sol1 = solve_ivp(rhs, (r0, R_MAX), [us, ps], method="DOP853", rtol=rtol, atol=1e-2 * rtol * u0,
                     events=[ev_unter, ev_um])
    if sol1.status < 0:
        raise RuntimeError(sol1.message)
    if len(sol1.t_events[0]):
        return "unter", None, float(sol1.t_events[0][0]), u0
    if not len(sol1.t_events[1]):
        return "offen", None, float(sol1.t[-1]), u0
    r1, y1 = float(sol1.t_events[1][0]), sol1.y_events[1][0]
    sol = solve_ivp(rhs, (r1, R_MAX), y1, method="DOP853", rtol=rtol, atol=ATOL2,
                    events=[ev_ueber, ev_unter, ev_w])
    if sol.status < 0:
        raise RuntimeError(sol.message)
    R = float(sol.t_events[2][0]) if len(sol.t_events[2]) else None
    if len(sol.t_events[0]):
        return "ueber", R, float(sol.t_events[0][0]), u0
    if len(sol.t_events[1]):
        return "unter", R, float(sol.t_events[1][0]), u0
    return "offen", R, float(sol.t[-1]), u0


def schiessen(P, bahn, klammer=None):
    """Bisektion in s; Rueckgabe dict mit R (Mittel der Klammerbahnen), Aufloesung, s, S0.
    klammer: optionale enge Startklammer (aus einer anderen Rechnung); ist sie ungueltig, volle Klammer wie bic2."""
    eng = False
    if PROTOKOLL:
        bahn_roh = bahn

        def bahn(s):
            t0 = time.time()
            erg = bahn_roh(s)
            log(f"    Bahn s = {s:.15f}: {erg[0]} r_ende {erg[2]:.2f} R {erg[1]} ({time.time() - t0:.2f} s)")
            return erg
    if klammer is not None:
        lo, hi = klammer
        k_lo, R_lo, _, _ = bahn(lo)
        k_hi, R_hi, _, _ = bahn(hi)
        eng = (k_lo == "unter" and k_hi == "ueber")
    if not eng:
        lo, hi = -math.log(P.t - S_LO_ABSTAND), S_HI
        k_lo, R_lo, _, _ = bahn(lo)
        k_hi, R_hi, _, _ = bahn(hi)
    if k_lo != "unter" or k_hi != "ueber":
        raise RuntimeError(f"Startklammer ungueltig: {k_lo} / {k_hi}")
    it = 0
    for it in range(1, IT_MAX + 1):
        mid = 0.5 * (lo + hi)
        k, R, _, _ = bahn(mid)
        if k == "ueber":
            hi, R_hi = mid, R
        elif k == "unter":
            lo, R_lo = mid, R
        else:
            raise RuntimeError(f"Bahn offen bei s = {mid}")
        if hi - lo < TOL_S * max(1.0, hi):
            break
    if R_lo is None or R_hi is None:
        raise RuntimeError("Halbhoehe auf einer Klammerbahn nicht erreicht")
    s_mid = 0.5 * (lo + hi)
    u0 = math.exp(-s_mid)
    f0 = P.t - u0
    return {"R": 0.5 * (R_lo + R_hi), "R_lo": R_lo, "R_hi": R_hi, "aufloesung": abs(R_hi - R_lo), "s": s_mid,
            "s_klammer": hi - lo, "iterationen": it, "u0": u0, "f0": f0, "S0": f0 * f0, "enge_startklammer": eng}


def R_bic2(P, h_prof):
    import torch
    torch.set_num_threads(1)
    import bic2_3d_praez as b2
    prof = b2.profil(P.w2, 3.0, P.beta, h_prof, torch.device("cpu"))
    f, fp = prof["f"], prof["fp"]
    R = None
    for j in range(len(f) - 1):
        if f[j] > P.f_w >= f[j + 1]:
            # in u = t - f: u steigt; Hermite in f mit Ziel f_w (f faellt), Vorzeichen egal fuer die Bisektion
            R = hermite_wurzel(j * h_prof, f[j], fp[j], (j + 1) * h_prof, f[j + 1], fp[j + 1], P.f_w)
            break
    if R is None:
        raise RuntimeError("bic2-Profil erreicht die Halbhoehe nicht")
    return {"R": R, "f0": prof["f0"], "S0": prof["f0"] ** 2, "s": prof["s"], "klammer_s": prof["klammer"],
            "grund": prof["grund"], "r_cut": prof["r_cut"], "rueckfall": prof["rueckfall"]}


def R_verfahren(P, verf, klammer=None):
    art, wert = verf.split(":")
    w = float(wert)
    if art == "rk4":
        return schiessen(P, lambda s: bahn_rk4(P, s, w), klammer)
    if art == "dop853":
        return schiessen(P, lambda s: bahn_dop(P, s, w), klammer)
    if art == "bic2":
        return R_bic2(P, w)
    raise ValueError(f"unbekanntes Verfahren {verf}")


# ----------------------------------------------------------------------------------------------------------------------
# Kommando profile
# ----------------------------------------------------------------------------------------------------------------------

def cmd_profile(args):
    global PROTOKOLL
    K = lade(args.konfig)
    PROTOKOLL = bool(K.get("protokoll_bahnen", False))
    SP = lade(K["sprossen_datei"])
    beta = float(SP["beta"])
    if abs(float(K["beta"]) - beta) > 0.0:
        raise ValueError("beta der Sprossendatei passt nicht zur Konfiguration")
    auswahl = K.get("ids")
    sprossen = [x for x in SP["sprossen"] if auswahl is None or x["id"] in auswahl]
    out = {"kommando": "profile", "beginn": BEGINN, "konfig": K, "konfig_datei": args.konfig, "beta": beta,
           "sprossen_datei": K["sprossen_datei"], "verfahren": K["verfahren"], "fd": K.get("fd"), "zeilen": [],
           "TOL_S": TOL_S, "S_HI": S_HI, "R_MAX": R_MAX}
    for x in sprossen:
        w2 = float(x["omega2"])
        P = Par(beta, w2)
        z = {"id": x["id"], "omega2": w2, "eps": P.eps, "t": P.t, "S_top": P.s_top, "c1": P.c[0], "u_w": P.u_w,
             "R_tw": 1.0 / (2.0 * math.sqrt(beta) * P.eps), "R": {}}
        s_ref = None
        for verf in K["verfahren"]:
            t0 = time.time()
            kl = None
            if s_ref is not None and not verf.startswith("bic2"):
                ds = float(K["klammer_rel"]) * max(1.0, s_ref)
                kl = (s_ref - ds, s_ref + ds)
            try:
                e = R_verfahren(P, verf, kl)
                e["sek"] = time.time() - t0
                if s_ref is None and "s" in e and verf.startswith("rk4"):
                    s_ref = e["s"]
            except (RuntimeError, ValueError) as err:
                e = {"fehler": str(err), "sek": time.time() - t0}
            z["R"][verf] = e
            log(f"id {x['id']} omega^2 {w2:.10f} eps {P.eps:.6f} {verf}: "
                + (f"R = {e['R']:.10f} (Aufl. {e.get('aufloesung', float('nan')):.1e}, {e['sek']:.1f} s)"
                   if "R" in e else f"Fehler {e['fehler']}"))
            schreibe(args.out, {**out, "zeilen": out["zeilen"] + [z]})
        fd = K.get("fd")
        if fd:
            d = float(fd["delta"])
            t0 = time.time()
            try:
                Rp = R_verfahren(Par(beta, w2 + d), fd["verfahren"])["R"]
                Rm = R_verfahren(Par(beta, w2 - d), fd["verfahren"])["R"]
                z["fd_R_plus_minus"] = [Rp, Rm]
                z["dR_domega2"] = (Rp - Rm) / (2.0 * d)
                z["fd_sek"] = time.time() - t0
                log(f"id {x['id']}: dR/domega^2 = {z['dR_domega2']:.4f} ({fd['verfahren']}, delta {d:g})")
            except (RuntimeError, ValueError) as err:
                z["dR_domega2_fehler"] = str(err)
        out["zeilen"].append(z)
        schreibe(args.out, out)
    out["ende"] = jetzt()
    out["sek"] = time.time() - T_START
    schreibe(args.out, out)
    log("profile fertig")


# ----------------------------------------------------------------------------------------------------------------------
# Kommando phase (ebene Wand bei omega_min, phase_wand.py unveraendert)
# ----------------------------------------------------------------------------------------------------------------------

def cmd_phase(args):
    import phase_wand as pw
    K = lade(args.konfig)
    PW = lade(K["phase_wand_datei"])
    SP = lade(K["sprossen_datei"])
    beta = float(K["beta"])
    if abs(float(PW["beta"]) - beta) > 0.0 or abs(float(SP["beta"]) - beta) > 0.0:
        raise ValueError("beta passt nicht")
    mod = pw.MB(beta)
    sb = math.sqrt(beta)
    tiefen = [float(t) * sb for t in K["tiefen"]]
    d_wert = float(K["tiefe_gewertet"]) * sb
    liste = [{"id": "rho_z", "rho": float(PW["rho_z"])}]
    liste += [{"id": x["id"], "rho": float(x["rho"])} for x in SP["sprossen"] if x.get("rho") is not None]
    out = {"kommando": "phase", "beginn": BEGINN, "konfig": K, "beta": beta, "phase_wand": {
        k: PW[k] for k in ("rho_z", "k_in", "kappa_in", "phi", "R", "c_plus")}, "werte": []}
    for e in liste:
        rho = e["rho"]
        try:   # NACHLAUF: rho_n ausserhalb des ebenen Fensters (aussen beide Kanaele offen) -> vermerken, weiter
            k, e1, kap, e2 = pw.innen_moden(mod, rho)
            satz, _ = pw.phase_satz(mod, rho, tiefen + [d_wert], pw.RTOL_HAUPT, mod.xb)
        except ValueError as err:
            e["fehler"] = str(err)
            out["werte"].append(e)
            log(f"rho {e['id']}: rho = {rho:.10f}: nicht definiert ({err})")
            schreibe(args.out, out)
            continue
        wert = min(satz, key=lambda s: abs(s["d"] - d_wert))
        streu = max(abs(pw.wrap_pi(s["phi"] - wert["phi"])) for s in satz
                    if s["d"] >= (float(K["streuung_ab"]) - 1e-3) * sb)
        e.update({"k_in": k, "kappa_in": kap, "phi": wert["phi"], "R_amp": wert["R"], "c_plus": wert["c_plus"],
                  "c_minus": wert["c_minus"], "wachsend_rel": wert["wachsend_rel"], "phi_streuung": streu,
                  "tiefen": [{"d_in_sqrtbeta": s["d"] / sb, "phi": s["phi"]} for s in sorted(satz, key=lambda s: s["d"])]})
        out["werte"].append(e)
        log(f"rho {e['id']}: rho = {rho:.10f}, k_in = {k:.9f}, phi = {wert['phi']:.9f}, Streuung {streu:.1e}")
        schreibe(args.out, out)
    z = out["werte"][0]
    out["kontrolle_rho_z"] = {"d_phi": pw.wrap_pi(z["phi"] - float(PW["phi"])), "d_k": z["k_in"] - float(PW["k_in"])}
    out["ende"] = jetzt()
    schreibe(args.out, out)
    log(f"phase fertig; Kontrolle bei rho_z: {out['kontrolle_rho_z']}")


# ----------------------------------------------------------------------------------------------------------------------
# Kommando auswertung
# ----------------------------------------------------------------------------------------------------------------------

def k_lokal(beta, w2, rho, S):
    """Innere Wellenzahl bei (omega^2, rho, S): k^2 = omega^2 + rho^2 - D + sqrt(4 omega^2 rho^2 + C^2)."""
    D = 1.0 - 4.0 * S + 9.0 * beta * S * S
    C = -2.0 * S + 6.0 * beta * S * S
    k2 = w2 + rho * rho - D + math.sqrt(4.0 * w2 * rho * rho + C * C)
    return math.sqrt(k2)


def ausgleich(punkte):
    """Linearer Ausgleich Delta = a eps + b (kleinste Quadrate) nach Abwicklung um die Sprosse mit kleinstem eps."""
    pk = sorted(punkte, key=lambda p: p["eps"])
    ref = pk[0]["Delta"]
    abgew = []
    for p in pk:
        m = math.ceil(p["Delta"] - ref - 0.5)       # Delta - m in (ref - 1/2, ref + 1/2]
        abgew.append({**p, "Delta_abgew": p["Delta"] - m, "verschoben": m})
    e = np.array([p["eps"] for p in abgew])
    d = np.array([p["Delta_abgew"] for p in abgew])
    A = np.vstack([e, np.ones_like(e)]).T
    (a, b), *_ = np.linalg.lstsq(A, d, rcond=None)
    res = d - (a * e + b)
    b_w, _ = frac_halb(float(b))
    return {"a": float(a), "b": float(b), "b_gewickelt": b_w, "rest_max": float(np.max(np.abs(res))),
            "rest_rms": float(np.sqrt(np.mean(res * res))), "n": len(abgew),
            "abwicklung": any(p["verschoben"] != 0 for p in abgew),
            "punkte": [{"id": p["id"], "eps": p["eps"], "Delta": p["Delta"], "Delta_abgew": p["Delta_abgew"]}
                       for p in abgew]}


def spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean()
    ry -= ry.mean()
    return float((rx * ry).sum() / math.sqrt((rx * rx).sum() * (ry * ry).sum()))


def cmd_auswertung(args):
    K = lade(args.konfig)
    SP = lade(K["sprossen_datei"])
    PW = lade(K["phase_wand_datei"])
    PH = lade(K["phase_datei"])
    beta = float(K["beta"])
    for q in (SP, PW, PH):
        if abs(float(q["beta"]) - beta) > 0.0:
            raise ValueError("beta passt nicht")
    k_z, phi_z = float(PW["k_in"]), float(PW["phi"])
    om2min = 1.0 - 1.0 / (4.0 * beta)
    # Profile sammeln: je id und Verfahren das erste vorhandene Ergebnis
    Rtab, fd = {}, {}
    for pf in K["profil_dateien"]:
        D = lade(pf)
        if abs(float(D["beta"]) - beta) > 0.0:
            raise ValueError(f"beta passt nicht in {pf}")
        for z in D["zeilen"]:
            for verf, e in z["R"].items():
                Rtab.setdefault(z["id"], {}).setdefault(verf, {**e, "datei": pf, "omega2": z["omega2"]})
            if "dR_domega2" in z:
                fd.setdefault(z["id"], z["dR_domega2"])
    nb = {w["id"]: w for w in PH["werte"]}
    haupt = K["haupt"]
    zeilen = []
    for x in SP["sprossen"]:
        i = x["id"]
        w2 = float(x["omega2"])
        eps = w2 - om2min
        rv = Rtab.get(i, {})
        z = {"id": i, "omega2": w2, "eps": eps, "R_tw": 1.0 / (2.0 * math.sqrt(beta) * eps), "rho": x.get("rho"),
             "quelle": x.get("quelle")}
        e = rv.get(haupt)
        if e is None or "R" not in e:
            z["fehlt"] = True
            zeilen.append(z)
            continue
        if abs(float(e["omega2"]) - w2) > 0.0:
            raise ValueError(f"omega^2 der Profildatei passt nicht bei id {i}")
        R = float(e["R"])
        xh = (k_z * R + phi_z) / math.pi - 0.5
        Dh, nh = frac_halb(xh)
        z.update({"R": R, "R_minus_R_tw": R - z["R_tw"], "S0": e.get("S0"), "S0_minus_Sc_minus_eps":
                  (e["S0"] - 1.0 / (2.0 * beta) - eps) if e.get("S0") is not None else None,
                  "aufloesung_bisektion": e.get("aufloesung"), "x": xh, "Delta": Dh, "n_strich": nh})
        # Kontrollen: Proben gegen die Hauptrechnung
        pr = {}
        for verf in K["proben_regel"] + K["proben_bericht"]:
            q = rv.get(verf)
            pr[verf] = (float(q["R"]) - R) if (q is not None and "R" in q) else None
        z["proben_dR"] = pr
        regel_ok = all(pr[v] is not None and abs(pr[v]) <= float(K["tol_R"]) for v in K["proben_regel"])
        regel_ok = regel_ok and (e.get("aufloesung") is not None and e["aufloesung"] <= float(K["tol_bisektion"]))
        z["K_profil"] = bool(regel_ok)
        if i in fd:
            z["dR_domega2"] = fd[i]
            z["dDelta_domega2"] = k_z * fd[i] / math.pi
        # Nebenform (k_in, phi bei rho_n, ebene Wand bei omega_min) und Zusatzform (k lokal bei omega_n, rho_n, S0)
        if i in nb and "phi" in nb[i]:          # NACHLAUF: nur wo die ebene Phase bei rho_n definiert ist
            w = nb[i]
            xn = (float(w["k_in"]) * R + float(w["phi"])) / math.pi - 0.5
            z["Delta_neben"], z["n_strich_neben"] = frac_halb(xn)
            z["k_in_rho_n"], z["phi_rho_n"] = w["k_in"], w["phi"]
        elif i in nb:
            z["neben_fehler"] = nb[i].get("fehler")
        if x.get("rho") is not None:            # NACHLAUF: Zusatzform braucht nur rho_n und S0, nicht die ebene Phase
            if e.get("S0") is not None:
                kl = k_lokal(beta, w2, float(x["rho"]), float(e["S0"]))
                xz = (kl * R + phi_z) / math.pi - 0.5
                z["Delta_zusatz"], z["n_strich_zusatz"] = frac_halb(xz)
                z["k_lokal"] = kl
                z["k_lokal_kontrolle_rho_z"] = k_lokal(beta, om2min, float(PW["rho_z"]), 1.0 / (2.0 * beta)) - k_z
        zeilen.append(z)
    # Regeln
    nach_id = {z["id"]: z for z in zeilen}
    urteile = {}
    for rg in K["regeln"]:
        ids = rg["sprossen"]
        fehl = [i for i in ids if i not in nach_id or "Delta" not in nach_id[i]]
        kfehl = [i for i in ids if i in nach_id and not nach_id[i].get("K_profil", False)]
        u = {"name": rg["name"], "sprossen": ids, "fehlend": fehl, "K_profil_nicht_bestanden": kfehl}
        if fehl or kfehl:
            u["eingetroffen"] = False
            u["auswertbar"] = False
            u["grund"] = "Sprosse fehlt oder K-Profil nicht bestanden (nicht auswertbar)"
        elif rg["art"] == "betrag":
            werte = {i: nach_id[i]["Delta"] for i in ids}
            u["Delta"] = werte
            u["max_betrag"] = max(abs(v) for v in werte.values())
            u["grenze"] = rg["grenze"]
            u["auswertbar"] = True
            u["eingetroffen"] = bool(all(abs(v) < float(rg["grenze"]) for v in werte.values()))
        elif rg["art"] == "ausgleich":
            fit = ausgleich([{"id": i, "eps": nach_id[i]["eps"], "Delta": nach_id[i]["Delta"]} for i in ids])
            u["ausgleich"] = fit
            u["grenze_b"] = rg["grenze_b"]
            u["auswertbar"] = True
            b_ok = abs(fit["b_gewickelt"]) < float(rg["grenze_b"])
            u["b_ok"] = bool(b_ok)
            ok = b_ok
            if rg.get("monoton"):
                pk = sorted([nach_id[i] for i in ids], key=lambda z: -z["eps"])     # eps fallend
                betr = [abs(z["Delta"]) for z in pk]
                streng = all(betr[j + 1] < betr[j] for j in range(len(betr) - 1))
                rs = spearman(np.array([z["eps"] for z in pk]), np.array(betr))
                u["monoton_streng"] = bool(streng)
                u["spearman_betrag_eps"] = rs
                u["monoton_mild_bericht"] = bool(rs > 0.0)
                ok = ok and streng
            u["eingetroffen"] = bool(ok)
        else:
            raise ValueError(f"unbekannte Regelart {rg['art']}")
        urteile[rg["name"]] = u
        log(f"{rg['name']}: eingetroffen {u['eingetroffen']} (auswertbar {u.get('auswertbar')})")
    # Berichte (ohne Regel): Ausgleich fuer Neben- und Zusatzform, Ausgleich ueber weitere Mengen
    bericht = {}
    for name, feld, ids in K.get("berichtsausgleiche", []):
        pts = [{"id": i, "eps": nach_id[i]["eps"], "Delta": nach_id[i][feld]} for i in ids
               if i in nach_id and feld in nach_id[i]]
        if len(pts) >= 2:
            bericht[name] = {"feld": feld, **ausgleich(pts)}
    out = {"kommando": "auswertung", "beginn": BEGINN, "konfig": K, "beta": beta, "k_in_rho_z": k_z,
           "phi_rho_z": phi_z, "theta_inf_karte": frac_halb(0.5 - phi_z / math.pi)[0] % 1.0, "zeilen": zeilen,
           "urteile": urteile, "berichtsausgleiche": bericht, "ende": jetzt()}
    schreibe(args.out, out)
    for z in zeilen:
        if "Delta" in z:
            log(f"  id {z['id']:>3} eps {z['eps']:.6f} R {z['R']:.6f} (R_tw {z['R_tw']:.4f}) n' {z['n_strich']} "
                f"Delta {z['Delta']:+.5f} K_profil {z['K_profil']}"
                + (f" | neben {z['Delta_neben']:+.5f}" if "Delta_neben" in z else "")
                + (f" | zusatz {z['Delta_zusatz']:+.5f}" if "Delta_zusatz" in z else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="kommando", required=True)
    for name in ("profile", "phase", "auswertung"):
        a = sp.add_parser(name)
        a.add_argument("--konfig", required=True)
        a.add_argument("--out", required=True)
    args = ap.parse_args()
    log(f"phase_3d {args.kommando} Beginn {BEGINN}, argv {sys.argv[1:]}")
    {"profile": cmd_profile, "phase": cmd_phase, "auswertung": cmd_auswertung}[args.kommando](args)


if __name__ == "__main__":
    main()
