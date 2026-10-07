"""KAUSAL-4D-SCHICHT-2 (Runde 39, Code-Agent), Teil A: Kontinuums-Erwartung, Pole und Nullstellenzaehlung.

Wie schicht_kont.py aus KAUSAL-4D-SCHICHT-1 (Rechenweg uebernommen), erweitert um die dritte Schicht und um:
- Kern f(tau) = sum_n a_n mu_n(tau) = a (c0 + c1 u + c2 u^2/2) exp(-u), u = c tau^4, c = pi rho/24.
- k~_gen(Z) = (4 pi/Z) int tau^2 f(tau) K1(Z tau) dtau, Z = sqrt(|k|^2 - omega^2), Re Z > 0;  K_P~ = k~_gen/(1 + m^2 k~_gen).
- Zweites Blatt: k~_II = k~_gen - D, D(Z) = (4 pi^2 i/Z) int tau^2 f I1(Z tau) dtau.
- Fortgesetzte Funktion F(omega) = g_I(omega) fuer Im omega > 0, g_II(omega) fuer Im omega <= 0; stetig ueber den
  zeitartigen Schnitt (Re omega > |k|). Die Schalennullstelle ist die Newton-Nullstelle von F ab omega_0 + 0,001 i
  (Gegenstart omega_0 - 0,02 i); Blatt I bei Im > 0 (Wachstum), Blatt II bei Im < 0 (Zerfall). PLAN Abschnitt 4.
- Region S0 (neu): Re omega in [0,5; 2,0], Im omega in [1e-5; 0,002], Zaehlung per Argumentprinzip auf g_I,
  Lokalisierung per Newton auf F ab x + 0,001 i.
- Momentprobe S_p = int tau^p f dtau gegen die Gamma-Formeln, Sprungprobe D(i y) gegen die Reihe.

Aufruf (nur ueber kleintest.sh):
  schicht2_kont.py pole      <ausgabeordner> <rho1,rho2,...> <varianten, z. B. VJ,V0> <dateiname.json>
  schicht2_kont.py momente   <ausgabeordner> <rho1,rho2,...> <varianten>       (nur Moment-, Sprung-, Windungsprobe)
  schicht2_kont.py erwartung <ausgabeordner> <rho1,rho2,...> <pole1.json,pole2.json> [varianten]
"""
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import iv, j0, j1, kv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal4d as kd  # noqa: E402
import kontinuum4d as kc  # noqa: E402
import schicht2_feld as sf  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
M = kd.MASSE
VAR = {name: (c0, c1, c2) for (name, c0, c1, c2) in sf.VARIANTEN}
# Regionen (PLAN Abschnitt 4); A und S wie KAUSAL-4D-SCHICHT-1, S0 neu
R_A = 10.0
Y_A = 0.05
S_X = (0.5, 2.0)
S_Y = (0.002, 1.0)
S0_Y = (1e-5, 0.002)
NTAU_POL = 128
KS = (0.0, float(kd.PP[1]))
LEIT = {"VJ": 0, "V0": 1, "V00": 2}   # erste nichtverschwindende Ordnung des Sprungs D in Z^2 (PLAN Abschnitt 2)


def kern(tau, rho, cs):
    """f(tau) = a (c0 + c1 u + c2 u^2/2) exp(-u); fuer c2 = 0 derselbe Ausdruck wie schicht_kont.kern."""
    c0, c1, c2 = cs
    u = (np.pi * rho / 24.0) * tau ** 4
    if c2 == 0.0:
        return kd.a_hop(rho) * (c0 + c1 * u) * np.exp(-u)
    return kd.a_hop(rho) * (c0 + c1 * u + c2 * 0.5 * u * u) * np.exp(-u)


def tau_knoten(rho, ntau):
    c = np.pi * rho / 24.0
    return kc.gl(0.0, (40.0 / c) ** 0.25, ntau)


def kt_gen(Z, rho, cs, ntau=NTAU_POL):
    tau, wt = tau_knoten(rho, ntau)
    w = wt * tau ** 2 * kern(tau, rho, cs)
    return (4 * np.pi / Z) * (kv(1, Z[..., None] * tau) * w).sum(axis=-1)


def sprung(Z, rho, cs, ntau=NTAU_POL):
    tau, wt = tau_knoten(rho, ntau)
    w = wt * tau ** 2 * kern(tau, rho, cs)
    return (4j * np.pi ** 2 / Z) * (iv(1, Z[..., None] * tau) * w).sum(axis=-1)


def Z_von(om, k):
    Z = np.sqrt(k * k - np.asarray(om, dtype=np.complex128) ** 2)
    return np.where(Z.real < 0, -Z, Z)


def g1(om, k, rho, cs, ntau=NTAU_POL):
    om = np.atleast_1d(np.asarray(om, dtype=np.complex128))
    return 1.0 + M * M * kt_gen(Z_von(om, k), rho, cs, ntau)


def g2(om, k, rho, cs, ntau=NTAU_POL):
    om = np.atleast_1d(np.asarray(om, dtype=np.complex128))
    Z = Z_von(om, k)
    return 1.0 + M * M * (kt_gen(Z, rho, cs, ntau) - sprung(Z, rho, cs, ntau))


def gF(om, k, rho, cs, ntau=NTAU_POL):
    """Fortgesetzte Funktion: g_I fuer Im omega > 0, g_II fuer Im omega <= 0."""
    om = np.atleast_1d(np.asarray(om, dtype=np.complex128))
    return np.where(om.imag > 0, g1(om, k, rho, cs, ntau), g2(om, k, rho, cs, ntau))


def newton(fun, om0, iters=80):
    om = complex(om0)
    for _ in range(iters):
        f = fun(om)[0]
        h = 1e-6 * max(1.0, abs(om))
        d = (fun(om + h)[0] - fun(om - h)[0]) / (2 * h)
        if d == 0 or not np.isfinite(d):
            return om, np.inf
        st = f / d
        if abs(st) > 2.0:
            st = 2.0 * st / abs(st)
        om -= st
        if abs(st) < 1e-13 * max(1.0, abs(om)):
            break
    return om, float(abs(fun(om)[0]))


# ---------- Argumentprinzip (wie KAUSAL-4D-SCHICHT-1) ----------
def stuecke_A(R=R_A, y0=Y_A):
    xr = np.sqrt(R * R - y0 * y0)
    th0 = np.arcsin(y0 / R)
    return [lambda s: (-xr + 2 * xr * s) + 1j * y0 + 0 * s,
            lambda s: R * np.exp(1j * (th0 + (np.pi - 2 * th0) * s))]


def stuecke_rechteck(x1, x2, y1, y2):
    return [lambda s: (x1 + (x2 - x1) * s) + 1j * y1 + 0 * s,
            lambda s: x2 + 1j * (y1 + (y2 - y1) * s) + 0 * s,
            lambda s: (x2 - (x2 - x1) * s) + 1j * y2 + 0 * s,
            lambda s: x1 + 1j * (y2 - (y2 - y1) * s) + 0 * s]


def windung(fun, stuecke, n0, dmax, runden=16):
    tot = 0.0
    dmx = 0.0
    gmin = np.inf
    nev = 0
    ok = True
    for p in stuecke:
        s = np.linspace(0.0, 1.0, n0 + 1)
        g = fun(p(s))
        nev += s.size
        for _ in range(runden):
            d = np.angle(g[1:] / g[:-1])
            sch = np.nonzero(np.abs(d) > dmax)[0]
            if sch.size == 0:
                break
            sm = 0.5 * (s[sch] + s[sch + 1])
            gm = fun(p(sm))
            nev += sm.size
            s = np.insert(s, sch + 1, sm)
            g = np.insert(g, sch + 1, gm)
        d = np.angle(g[1:] / g[:-1])
        if np.abs(d).max() > dmax:
            ok = False
        tot += d.sum()
        dmx = max(dmx, float(np.abs(d).max()))
        gmin = min(gmin, float(np.abs(g).min()))
    w = tot / (2 * np.pi)
    return {"windung": w, "zahl": int(round(w)), "max_dphase": dmx, "min_abs_g": gmin, "auswertungen": nev,
            "aufgeloest": ok}


def zaehle(fun, stuecke):
    a = windung(fun, stuecke, 2000, 0.25)
    b = windung(fun, stuecke, 4000, 0.12)
    a["fein"] = b
    a["stabil"] = bool(a["zahl"] == b["zahl"] and a["aufgeloest"] and b["aufgeloest"])
    return a


def suche(fun, xs, ys, maske, region):
    """Lokale Minima von |g| auf dem Gitter, dann Newton; Nullstellen in der Region (dedupliziert)."""
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    W = X + 1j * Y
    A = np.full(W.shape, np.inf)
    sel = maske(W)
    A[sel] = np.abs(fun(W[sel]))
    kand = []
    for i in range(1, W.shape[0] - 1):
        for j in range(1, W.shape[1] - 1):
            if not np.isfinite(A[i, j]):
                continue
            nb = A[i - 1:i + 2, j - 1:j + 2]
            if A[i, j] <= nb.min():
                kand.append((A[i, j], W[i, j]))
    kand.sort(key=lambda z: z[0])
    nullst = []
    for _, w0 in kand[:60]:
        om, res = newton(fun, w0)
        if res < 1e-9 and region(om) and all(abs(om - z) > 1e-6 for z in nullst):
            nullst.append(om)
    return nullst


def suche_S0(fF, f1):
    """Nullstellen in S0: Newton auf F ab x + 0,001 i (x = 0,5 ... 2,0, Schritt 0,05); Residuum auf g_I geprueft."""
    out = []
    for x in np.arange(S_X[0], S_X[1] + 1e-9, 0.05):
        om, res = newton(fF, complex(x, 0.001))
        if (res < 1e-9 and S_X[0] <= om.real <= S_X[1] and S0_Y[0] <= om.imag <= S0_Y[1]
                and float(abs(f1(om)[0])) < 1e-9 and all(abs(om - z) > 1e-6 for z in out)):
            out.append(om)
    return out


def pole_variante(name, rho, k):
    cs = VAR[name]
    f1 = lambda om: g1(om, k, rho, cs)  # noqa: E731
    f2 = lambda om: g2(om, k, rho, cs)  # noqa: E731
    fF = lambda om: gF(om, k, rho, cs)  # noqa: E731
    in_A = lambda om: (abs(om) < R_A) and (om.imag > Y_A)  # noqa: E731
    in_S = lambda om: (S_X[0] <= om.real <= S_X[1]) and (S_Y[0] <= om.imag <= S_Y[1])  # noqa: E731
    zA = zaehle(f1, stuecke_A())
    zS = zaehle(f1, stuecke_rechteck(S_X[0], S_X[1], S_Y[0], S_Y[1]))
    zS0 = zaehle(f1, stuecke_rechteck(S_X[0], S_X[1], S0_Y[0], S0_Y[1]))
    nA = suche(f1, np.arange(-10.0, 10.0001, 0.1), np.arange(Y_A, 10.0001, 0.1),
               lambda W: (np.abs(W) < R_A) & (W.imag > Y_A), in_A)
    nS = suche(f1, np.arange(S_X[0], S_X[1] + 1e-9, 0.01), np.arange(S_Y[0], S_Y[1] + 1e-9, 0.01),
               lambda W: np.ones(W.shape, dtype=bool), in_S)
    nS0 = suche_S0(fF, f1)
    w_bare = np.sqrt(k * k + M * M)
    # Regel aus KAUSAL-4D-SCHICHT-1 (Vergleich): Blatt I naechste in S, sonst Newton auf g_II ab omega_0 - 0,05 i
    schale_alt = None
    if zS["zahl"] >= 1 and nS:
        z = min(nS, key=lambda o: abs(o - w_bare))
        schale_alt = {"blatt": "I", "omega_re": z.real, "omega_im": z.imag, "residuum": float(abs(f1(z)[0]))}
    elif zS["zahl"] == 0:
        z, res = newton(f2, w_bare - 0.05j)
        if res < 1e-9 and z.imag < 0 and z.real > k:
            schale_alt = {"blatt": "II", "omega_re": z.real, "omega_im": z.imag, "residuum": res}
    # Regel dieses Plans: Newton auf der fortgesetzten Funktion F, zwei Starts
    zF, rF = newton(fF, w_bare + 0.001j)
    zG, rG = newton(fF, w_bare - 0.02j)
    schale = None
    if rF < 1e-9 and zF.real > k and abs(zF - w_bare) < 0.6:
        bl = "I" if zF.imag > 0 else "II"
        res_blatt = float(abs((f1 if bl == "I" else f2)(zF)[0]))
        konsistent = bool(rG < 1e-9 and abs(zG - zF) < 1e-8)
        if bl == "I" and zF.imag >= S_Y[0]:
            konsistent = konsistent and zS["zahl"] >= 1 and any(abs(zF - z) < 1e-8 for z in nS)
        elif bl == "I" and zF.imag >= S0_Y[0]:
            konsistent = konsistent and zS0["zahl"] >= 1 and any(abs(zF - z) < 1e-8 for z in nS0)
        schale = {"blatt": bl, "omega_re": zF.real, "omega_im": zF.imag, "residuum": rF,
                  "residuum_blattfunktion": res_blatt, "gegenstart": [zG.real, zG.imag, rG],
                  "konsistent": konsistent, "unter_zaehlaufloesung": bool(bl == "I" and zF.imag < S0_Y[0])}
    z2, r2 = newton(f2, w_bare - 0.05j)
    blatt2 = {"omega_re": z2.real, "omega_im": z2.imag, "residuum": r2,
              "gueltig": bool(r2 < 1e-9 and z2.imag < 0 and z2.real > k)}
    schalenpaar_in_A = 2 if (schale is not None and schale["blatt"] == "I" and schale["omega_im"] > Y_A) else 0
    th = np.linspace(0.001, np.pi - 0.001, 2001)
    gross = {str(R): float(np.abs(f1(R * np.exp(1j * th)) - 1.0).max()) for R in (10.0, 20.0)}
    if schale is not None:
        zz = complex(schale["omega_re"], schale["omega_im"])
        zf, rf = newton(lambda om: gF(om, k, rho, cs, 256), zz)
        quad = {"ntau256_omega_re": zf.real, "ntau256_omega_im": zf.imag, "abw": float(abs(zf - zz))}
    else:
        quad = None
    om_t = R_A * np.exp(1j * th[::50])
    quad_bogen = float(np.abs(f1(om_t) - g1(om_t, k, rho, cs, 256)).max())
    return {"variante": name, "rho": rho, "k": k, "zaehlung_A": zA, "zaehlung_S": zS, "zaehlung_S0": zS0,
            "nullstellen_A": [[z.real, z.imag] for z in nA], "nullstellen_S": [[z.real, z.imag] for z in nS],
            "nullstellen_S0": [[z.real, z.imag] for z in nS0],
            "schale": schale, "schale_regel_schicht1": schale_alt, "blatt2": blatt2,
            "schalenpaar_in_A": schalenpaar_in_A, "weitere_in_A": zA["zahl"] - schalenpaar_in_A,
            "lokalisiert_gleich_gezaehlt_A": bool(len(nA) == zA["zahl"]),
            "lokalisiert_gleich_gezaehlt_S": bool(len(nS) == zS["zahl"]),
            "lokalisiert_gleich_gezaehlt_S0": bool(len(nS0) == zS0["zahl"]),
            "max_abs_m2k_bogen": gross, "quadratur_schale": quad, "quadratur_bogen_max_abw_g": quad_bogen}


def probe_windung():
    """Synthetisch: bekannte Nullstellen; dazu eine Nullstelle knapp ueber der Achse (S0) mit Pol-artiger Stelle
    auf der Achse bei 0,52 (wie der Lichtkegelpunkt bei k = p)."""
    z1, z2 = 1.0 + 0.3j, -2.0 + 4.0j
    fun = lambda om: (om - z1) * (om - z2) * (om + np.conj(z1)) / (om + 3j) ** 3  # noqa: E731
    z3 = 1.07 + 4e-4j
    fun2 = lambda om: (om - z3) * (om + np.conj(z3)) / ((om - 0.52) * (om + 0.52))  # noqa: E731
    return {"A_soll": 3, "A": zaehle(fun, stuecke_A())["zahl"], "S_soll": 1,
            "S": zaehle(fun, stuecke_rechteck(S_X[0], S_X[1], S_Y[0], S_Y[1]))["zahl"],
            "S0_soll": 1, "S0": zaehle(fun2, stuecke_rechteck(S_X[0], S_X[1], S0_Y[0], S0_Y[1]))["zahl"],
            "S0_stabil": zaehle(fun2, stuecke_rechteck(S_X[0], S_X[1], S0_Y[0], S0_Y[1]))["stabil"],
            "S_ohne_S0_soll": 0, "S_ohne_S0": zaehle(fun2, stuecke_rechteck(S_X[0], S_X[1], S_Y[0], S_Y[1]))["zahl"]}


def blattprobe(name, rho, k):
    """Stetigkeit: g_II(x - i e) gegen g_I(x + i e) fuer x > k (zeitartig), e = 1e-6 und 1e-8."""
    cs = VAR[name]
    x = np.linspace(np.sqrt(k * k + 0.25), 3.0, 11)
    out = {}
    for e in (1e-6, 1e-8):
        a = g1(x + 1j * e, k, rho, cs)
        b = g2(x - 1j * e, k, rho, cs)
        out[f"{e:g}"] = float(np.abs(a - b).max())
    return out


def momente_analytisch(rho, cs, p):
    """S_p = sum_n a_n Gamma(n + (p+1)/4)/(4 c^((p+1)/4) n!)."""
    c = np.pi * rho / 24.0
    a = kd.a_hop(rho)
    q = (p + 1) / 4.0
    return sum(a * cn * math.gamma(n + q) / (4.0 * c ** q * math.factorial(n)) for n, cn in enumerate(cs))


def momentprobe(name, rho):
    cs = VAR[name]
    tau, wt = tau_knoten(rho, NTAU_POL)
    f = kern(tau, rho, cs)
    out = {}
    for p in (1, 3, 5, 7, 9):
        num = float((wt * tau ** p * f).sum())
        ana = momente_analytisch(rho, cs, p)
        skala = float((wt * tau ** p * np.abs(f)).sum())
        out[f"S{p}"] = {"numerisch": num, "analytisch": ana, "abw_bezogen_auf_betragsintegral": abs(num - ana) / skala}
    out["normierung_4pi_S1"] = 4 * np.pi * out["S1"]["numerisch"]
    return out


def sprungprobe(name, rho):
    """D(i y) gegen die Reihe 4 pi^2 i sum_j (i y)^(2j) S_(2j+3)/(2^(2j+1) j! (j+1)!), erste nichtverschwindende Ordnung."""
    cs = VAR[name]
    tau, wt = tau_knoten(rho, NTAU_POL)
    w = wt * tau ** 2 * kern(tau, rho, cs)
    out = {}
    for y in (0.05, 0.1, 0.2):
        D = (4j * np.pi ** 2 / y) * float((w * j1(y * tau)).sum())        # I1(i y tau) = i J1(y tau)
        terme = [4j * np.pi ** 2 * (1j * y) ** (2 * j) * momente_analytisch(rho, cs, 2 * j + 3)
                 / (2 ** (2 * j + 1) * math.factorial(j) * math.factorial(j + 1)) for j in range(5)]
        erst = terme[LEIT[name]]
        out[f"y{y:g}"] = {"D_numerisch": [D.real, D.imag], "erster_term": [erst.real, erst.imag],
                          "reihe_5_terme": [sum(terme).real, sum(terme).imag],
                          "verhaeltnis_zu_erstem_term": abs(D) / abs(erst) if abs(erst) > 0 else None,
                          "rel_abw_reihe": abs(D - sum(terme)) / abs(sum(terme)) if abs(sum(terme)) > 0 else None}
    return out


def modus_pole(ordner, rhos, varianten, datei):
    t0 = time.time()
    out = {"modus": "pole", "rhos": rhos, "varianten": varianten, "R_A": R_A, "Y_A": Y_A, "S_X": S_X, "S_Y": S_Y,
           "S0_Y": S0_Y, "ks": KS, "probe_windung": probe_windung(),
           "momentprobe": {f"{v}_rho{r:g}": momentprobe(v, r) for v in varianten for r in rhos},
           "sprungprobe": {f"{v}_rho{r:g}": sprungprobe(v, r) for v in varianten for r in rhos},
           "blattprobe": {f"{v}_rho{r:g}_k{k:.4f}": blattprobe(v, r, k) for v in varianten for r in rhos for k in KS},
           "ergebnisse": {}}
    print(json.dumps({"proben_s": round(time.time() - t0, 1), "probe_windung": out["probe_windung"]}), flush=True)
    for v in varianten:
        for r in rhos:
            for k in KS:
                tt = time.time()
                e = pole_variante(v, r, k)
                e["zeit_s"] = round(time.time() - tt, 1)
                out["ergebnisse"][f"{v}_rho{r:g}_k{k:.4f}"] = e
                print(json.dumps({"fertig": f"{v}_rho{r:g}_k{k:.4f}", "zeit_s": e["zeit_s"]}), flush=True)
    out.update({"zeit_gesamt_s": round(time.time() - t0, 1), "skript_sha256": SKRIPT_SHA,
                "schicht2_feld_sha256": sf.SKRIPT_SHA, "kausal4d_sha256": kd.SKRIPT_SHA,
                "kontinuum4d_sha256": kc.SKRIPT_SHA, "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    with open(os.path.join(ordner, datei), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps({"zeit_gesamt_s": out["zeit_gesamt_s"]}), flush=True)


# ---------- Erwartung an Punkten (wie KAUSAL-4D-SCHICHT-1) ----------
def F_gen(om, k, rho, cs, ntau=64):
    Z2 = k[None, :] ** 2 - om[:, None] ** 2
    Z = np.sqrt(Z2)
    Z = np.where(Z.real < 0, -Z, Z)
    out = np.zeros(Z.shape, dtype=np.complex128)
    for i in range(Z.shape[0]):
        km = kt_gen(Z[i], rho, cs, ntau)
        out[i] = km / (1.0 + M * M * km)
    return out


def erwartung_punkte(pp, c, rho, cs, Gam, ntau=64, dom=0.05, dk=0.1):
    """Wie kontinuum4d.johnston_punkte, mit k~_gen statt a mu~; Linie Im omega = Gam ueber allen Nullstellen."""
    kp, wp, kz, wz = kc.k_knoten(c)
    om_r = kd.OM[c] + np.arange(-int(round(9.0 / kd.SIGMA / dom)), int(round(9.0 / kd.SIGMA / dom)) + 1) * dom
    om = om_r + 1j * Gam
    kmax = np.sqrt(kc.KB ** 2 + (abs(kd.PP[c]) + kc.KB) ** 2) + 0.2
    kg = np.arange(0.0, kmax + dk, dk)
    if np.isfinite(rho):
        Fg = F_gen(om, kg, rho, cs, ntau)
    else:
        Fg = 1.0 / (kg[None, :] ** 2 - om[:, None] ** 2 + M * M)
    spl_r = CubicSpline(kg, Fg.real, axis=1)
    spl_i = CubicSpline(kg, Fg.imag, axis=1)
    kn = np.sqrt(kp[None, :] ** 2 + kz[:, None] ** 2).ravel()
    Fn = spl_r(kn) + 1j * spl_i(kn)
    h = kc.h3(kp, kz, c).ravel()
    Jt = kd.SIGMA * np.sqrt(2 * np.pi) * np.exp(-kd.SIGMA ** 2 * (om - kd.OM[c]) ** 2 / 2.0)
    rp = np.sqrt(pp[:, 1] ** 2 + pp[:, 2] ** 2)
    z = pp[:, 3]
    A = np.exp(1j * z[:, None] * kz[None, :]) * wz[None, :]
    B = j0(rp[:, None] * kp[None, :]) * (kp * wp)[None, :]
    P = (A[:, :, None] * B[:, None, :]).reshape(pp.shape[0], -1)
    MK = (Fn * h[None, :]) @ P.T / (2 * np.pi) ** 2
    ph = np.exp(-1j * om[:, None] * pp[None, :, 0]) * (Jt * dom / (2 * np.pi))[:, None]
    return (ph * MK).sum(axis=0)


def achsenpunkte():
    tt = np.round(np.arange(2, 21) * 0.2, 10)
    out = np.zeros((kd.NC, tt.size, 4))
    for c in range(kd.NC):
        out[c, :, 0] = tt
        out[c, :, 3] = kd.VN[c] * tt
    return out


def linkzahl_schichten(rhos, nt=8, nr=24, nchi=60, nmu=24):
    """E[L_n]/E[N] fuer D, n = 0, 1, 2: innen (6/pi) int dOmega dchi sinh^2 chi [1 - sum_(j<=n) U^j/j! e^-U]."""
    kk = kd.R_S / np.sqrt(2.0)
    tc = 0.5 * (kd.T_TOP - np.sqrt(2.0) * kd.R_S)
    kanten = sorted(set([kd.LZ_T0 + kd.LZ_W * i for i in range(kd.LZ_N + 1)] + [-kk, tc]))
    chi_l, wchi_l = [], []
    for a_ in range(7):
        x_, w_ = kc.gl(2.0 * a_, 2.0 * a_ + 2.0, nchi // 6)
        chi_l.append(x_)
        wchi_l.append(w_)
    chi = np.concatenate(chi_l)
    wchi = np.concatenate(wchi_l)
    mu, wmu = kc.gl(-1.0, 1.0, nmu)
    CH = np.cosh(chi)[:, None]
    SH = np.sinh(chi)[:, None]
    WI = (wchi * np.sinh(chi) ** 2)[:, None] * wmu[None, :] * 2 * np.pi
    z = {(r, n): 0.0 for r in rhos for n in range(3)}
    vol = 0.0
    for ia in range(len(kanten) - 1):
        ta, tb = kanten[ia], kanten[ia + 1]
        if tb - ta < 1e-12:
            continue
        tn, wt = kc.gl(ta, tb, nt)
        for tt, w_t in zip(tn, wt):
            rp = np.sqrt(max(kd.R_S ** 2 - tt ** 2, 0.0)) if tt <= -kk else tt + np.sqrt(2.0) * kd.R_S
            rD = min(rp, kd.T_TOP - tt)
            if rD <= 0:
                continue
            rn, wr = kc.gl(0.0, rD, nr)
            for rr, w_r in zip(rn, wr):
                tm = kc.tau_max(tt, rr, CH, SH, mu[None, :])
                wv = w_t * w_r * 4 * np.pi * rr * rr
                vol += wv
                for rho in rhos:
                    U = (np.pi * rho / 24.0) * tm ** 4
                    eU = np.exp(-U)
                    for n, poly in enumerate((1.0, 1.0 + U, 1.0 + U + 0.5 * U * U)):
                        z[(rho, n)] += wv * (6.0 / np.pi) * float((WI * (1.0 - poly * eU)).sum())
    return [{str(r): z[(r, n)] / vol for r in rhos} for n in range(3)], vol


def lade_pole(dateien):
    P = {"ergebnisse": {}, "dateien": [], "sha256": []}
    for d in dateien:
        q = json.load(open(d))
        P["ergebnisse"].update(q["ergebnisse"])
        P["dateien"].append(d)
        P["sha256"].append(hashlib.sha256(open(d, "rb").read()).hexdigest())
    return P


def modus_erwartung(ordner, rhos, pole_dateien, varianten):
    t0 = time.time()
    P = lade_pole(pole_dateien)
    pp = kd.pruefpunkte()
    pa = achsenpunkte()
    allp = np.concatenate([pp, pa], axis=1)          # (NC, 26 + 19, 4)
    npkt = allp.shape[1]
    phi_k = np.zeros((kd.NC, npkt), dtype=np.complex128)
    quad_kappe = np.zeros((kd.NC, 9), dtype=np.complex128)
    norm_c = np.zeros((kd.NC, kd.N_SCHEIBEN))
    for c in range(kd.NC):
        phi_k[c] = kc.kontinuum_punkte(allp[c], c)
        norm_c[c] = kc.kontinuum_norm(c)
        for i in range(9):
            tp, xp, yp, zp = pp[c, i]
            quad_kappe[c, i] = kc.faltung(tp, xp, yp, zp, c, True)
    print(json.dumps({"kontinuum_s": round(time.time() - t0, 1)}), flush=True)
    # Gamma je Variante und rho: ueber allen Nullstellen auf Blatt I (k = 0, dort groesstes Im omega)
    gammas = {}
    for v in varianten:
        for r in rhos:
            e = P["ergebnisse"][f"{v}_rho{r:g}_k0.0000"]
            ims = [z[1] for z in e["nullstellen_A"]] + [z[1] for z in e["nullstellen_S"]] + \
                  [z[1] for z in e["nullstellen_S0"]]
            if e["schale"] is not None and e["schale"]["blatt"] == "I":
                ims.append(e["schale"]["omega_im"])
            g1_ = max(0.8, (max(ims) if ims else 0.0) + 0.5)
            gammas[f"{v}_rho{r:g}"] = (g1_, g1_ + 0.6)
    rho_liste = list(rhos) + [1e6]
    erw = {}
    for v in varianten:
        cs = VAR[v]
        for r in rho_liste:
            G = gammas.get(f"{v}_rho{r:g}", (0.8, 1.4))
            arr = np.zeros((2, kd.NC, npkt), dtype=np.complex128)
            for ig in range(2 if np.isfinite(r) and r < 1e5 else 1):
                for c in range(kd.NC):
                    arr[ig, c] = erwartung_punkte(allp[c], c, r, cs, G[ig])
            erw[f"{v}_rho{r:g}"] = arr
            print(json.dumps({"erwartung": f"{v}_rho{r:g}", "gamma": G, "zeit_s": round(time.time() - t0, 1)}),
                  flush=True)
    quad = {}
    for v in [x for x in varianten if x != "VJ"]:
        r = min(rhos)
        cs = VAR[v]
        G = gammas[f"{v}_rho{r:g}"][0]
        b = np.array([erwartung_punkte(allp[c], c, r, cs, G, ntau=128) for c in range(kd.NC)])
        a = erw[f"{v}_rho{r:g}"][0]
        quad[f"{v}_rho{r:g}"] = float(np.max(np.abs(a - b) / np.abs(a)))
    lz, vol = linkzahl_schichten([r for r in rhos if r >= 8.0])
    kontrollen = {
        "gamma_gegenprobe_rel_max": {key: float(np.max(np.abs(a[0] - a[1]) / np.abs(a[0])))
                                     for key, a in erw.items() if np.abs(a[1]).max() > 0},
        "rho1e6_gegen_k_raum_rel_max": {v: float(np.max(np.abs(erw[f"{v}_rho1e+06"][0] - phi_k) / np.abs(phi_k)))
                                        for v in varianten},
        "quadratur_ntau128_rel_max": quad}
    np.savez_compressed(os.path.join(ordner, "erwartung.npz"), pruefpunkte=pp, achsenpunkte=pa, phi_k=phi_k,
                        quad_kappe=quad_kappe, norm_c=norm_c,
                        **{f"E_{key}": a for key, a in erw.items()})
    kopf = {"modus": "erwartung", "rhos": rhos, "varianten": varianten, "gammas": gammas, "kontrollen": kontrollen,
            "linkzahl_L0_je_N": lz[0], "linkzahl_L1_je_N": lz[1], "linkzahl_L2_je_N": lz[2], "V_D": vol,
            "norm_c": norm_c.tolist(), "zeit_gesamt_s": round(time.time() - t0, 1), "skript_sha256": SKRIPT_SHA,
            "pole_dateien": P["dateien"], "pole_sha256": P["sha256"],
            "kontinuum4d_sha256": kc.SKRIPT_SHA, "kausal4d_sha256": kd.SKRIPT_SHA,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(ordner, "erwartung.json"), "w") as fh:
        json.dump(kopf, fh, indent=1, default=str)
    print(json.dumps({"zeit_gesamt_s": kopf["zeit_gesamt_s"]}), flush=True)


def main():
    modus, ordner = sys.argv[1], sys.argv[2]
    rhos = [float(x) for x in sys.argv[3].split(",")]
    os.makedirs(ordner, exist_ok=True)
    if modus == "pole":
        modus_pole(ordner, rhos, sys.argv[4].split(","), sys.argv[5])
    elif modus == "momente":
        vs = sys.argv[4].split(",")
        out = {"momentprobe": {f"{v}_rho{r:g}": momentprobe(v, r) for v in vs for r in rhos},
               "sprungprobe": {f"{v}_rho{r:g}": sprungprobe(v, r) for v in vs for r in rhos},
               "probe_windung": probe_windung(), "skript_sha256": SKRIPT_SHA}
        with open(os.path.join(ordner, "momente.json"), "w") as fh:
            json.dump(out, fh, indent=1, default=str)
        print(json.dumps(out), flush=True)
    elif modus == "erwartung":
        varianten = sys.argv[5].split(",") if len(sys.argv) > 5 else [v[0] for v in sf.VARIANTEN]
        modus_erwartung(ordner, rhos, sys.argv[4].split(","), varianten)


if __name__ == "__main__":
    main()
