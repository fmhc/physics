#!/usr/bin/env python3
# ST-1 Raster (Runde 8): gemeinsame Schranke fuer das Stelle-Paar
#   V(r) = -G m1 m2 / r * (1 + A0 exp(-r/lambda0) + A2 exp(-r/lambda2)),  A2 = -4/3 (Spin-2-Geist), A0 = +1/3 (Skalar)
# aus J. G. Lee, Dissertation UW 2020, Tab. 11.4 (S. 134-137): je lambda alpha* +- sigma, +alpha95, -alpha95, |alpha95|, chi2.
# Modell: lineares Gauss-Modell je Template; zwei Templates mit Korrelation rho (mehrere Modelle).
# Ausschluss wie in der Dissertation: chi2 >= chi2_min,global + 6.17 = 277.88, also Delta = chi2 - chi2_Newton >= 2.89.
# Explorativ, keine formale Bestaetigung. Autor: Papier-Agent (Anthropic), 30.09.2026. Lokal ungetestet (keine Interpreter).
# Aufruf: python st1raster.py --out DIR
import argparse
import json
import math
import sys
import time

import numpy as np

# Spalten: lambda[mm] alpha* sigma +alpha95 -alpha95 |alpha95| chi2   (Abschrift aus pdftotext der Dissertation)
TAB = """
0.0050 4.09e6 2.58e6 1.18e7 -1.63e6 8.45e6 271.89
0.0056 8.6e5 5.29e5 2.4e6 -3.35e5 1.75e6 271.78
0.0063 1.93e5 1.17e5 5.31e5 -6.18e4 3.9e5 271.72
0.0071 4.76e4 2.86e4 1.29e5 -1.53e4 9.58e4 271.71
0.0079 1.5e4 8.96e3 3.99e4 -4.88e3 3.01e4 271.73
0.0089 4.52e3 2.71e3 1.19e4 -1.5e3 9.1e3 271.79
0.0100 1.53e3 923 3.99e3 -520 3.09e3 271.86
0.0110 668 406 1.73e3 -232 1.35e3 271.92
0.0130 176 108 465 -63.5 359 272.04
0.0140 102 63 268 -37.3 208 272.09
0.0160 40.3 25.3 106 -15.2 83 272.19
0.0180 18.9 12 49.4 -7.36 39.2 272.27
0.0200 10.1 6.47 26.3 -4.02 21 272.34
0.0220 5.91 3.83 15.4 -2.41 12.4 272.41
0.0250 3.03 2 7.9 -1.27 6.4 272.50
0.0280 1.75 1.17 4.51 -0.886 3.73 272.59
0.0320 0.963 0.661 2.56 -0.507 2.08 272.71
0.0350 0.663 0.464 1.77 -0.36 1.45 272.81
0.0400 0.394 0.286 1.06 -0.226 0.877 272.97
0.0450 0.257 0.194 0.699 -0.157 0.585 273.13
0.0500 0.179 0.142 0.494 -0.117 0.419 273.30
0.0560 0.124 0.104 0.35 -0.0884 0.3 273.49
0.0630 0.0862 0.078 0.251 -0.0685 0.218 273.71
0.0710 0.0601 0.06 0.183 -0.055 0.162 273.94
0.0790 0.0437 0.0485 0.14 -0.0469 0.126 274.14
0.0890 0.0304 0.0393 0.106 -0.0407 0.097 274.36
0.1000 0.021 0.0326 0.0813 -0.0365 0.0766 274.56
0.1100 0.0151 0.0285 0.0666 -0.034 0.0641 274.70
0.1300 0.0076 0.0231 0.048 -0.0312 0.0487 274.88
0.1400 0.00511 0.0213 0.042 -0.0304 0.0439 274.93
0.1600 0.00157 0.0187 0.0336 -0.0293 0.0376 274.98
0.1800 -0.000748 0.0169 0.0282 -0.0287 0.0339 274.99
0.2000 -0.00235 0.0157 0.0245 -0.0284 0.0317 274.97
0.2200 -0.00351 0.0147 0.0219 -0.0281 0.0303 274.94
0.2500 -0.00471 0.0137 0.0192 -0.0279 0.029 274.88
0.2800 -0.00552 0.013 0.0174 -0.0278 0.0282 274.81
0.3200 -0.00624 0.0123 0.0157 -0.0276 0.0275 274.74
0.3500 -0.00661 0.0119 0.0148 -0.0275 0.0271 274.69
0.4000 -0.00701 0.0114 0.0137 -0.0273 0.0265 274.62
0.4500 -0.00723 0.011 0.0129 -0.0269 0.026 274.57
0.5000 -0.00731 0.0107 0.0123 -0.0265 0.0254 274.53
0.5600 -0.00728 0.0103 0.0117 -0.0259 0.0247 274.49
0.6300 -0.00713 0.00982 0.0111 -0.025 0.0238 274.47
0.7100 -0.00685 0.00936 0.0105 -0.0239 0.0227 274.46
0.7900 -0.00653 0.00893 0.01 -0.0228 0.0217 274.46
0.8900 -0.00612 0.00845 0.00953 -0.0215 0.0205 274.47
1.0000 -0.00569 0.00796 0.00903 -0.0201 0.0192 274.49
1.1000 -0.00534 0.00763 0.00872 -0.0192 0.0183 274.50
1.3000 -0.00478 0.00706 0.00816 -0.0175 0.0168 274.53
1.4000 -0.00456 0.00683 0.00795 -0.0169 0.0162 274.55
1.6000 -0.00421 0.00648 0.0076 -0.0158 0.0152 274.57
1.8000 -0.00395 0.00621 0.00734 -0.015 0.0145 274.59
2.0000 -0.00375 0.00599 0.00712 -0.0144 0.014 274.60
2.2000 -0.0036 0.00585 0.00699 -0.014 0.0136 274.61
2.5000 -0.00344 0.00567 0.00682 -0.0135 0.0131 274.63
2.8000 -0.00332 0.00555 0.00669 -0.0132 0.0128 274.64
3.2000 -0.0032 0.00543 0.00657 -0.0128 0.0125 274.64
3.5000 -0.00314 0.00536 0.00651 -0.0126 0.0123 274.65
4.0000 -0.00307 0.00526 0.0064 -0.0124 0.0121 274.65
4.5000 -0.00303 0.00523 0.00637 -0.0123 0.012 274.66
5.0000 -0.00299 0.00517 0.0063 -0.0121 0.0118 274.66
5.6000 -0.00295 0.00515 0.0063 -0.012 0.0118 274.66
6.3000 -0.00293 0.00512 0.00627 -0.012 0.0117 274.67
7.1000 -0.0029 0.0051 0.00625 -0.0119 0.0116 274.67
7.9000 -0.00289 0.00508 0.00623 -0.0119 0.0116 274.67
8.9000 -0.00288 0.00507 0.00621 -0.0118 0.0116 274.67
"""

CHI2_NEWTON = 274.99        # Dissertation S. 133: Newton-Fit chi2 = 274.99, nu = 285
CHI2_GLOBAL_MIN = 271.71    # Tab. 11.4, Minimum bei lambda = 7.1 um
DCHI2 = 6.17                # Dissertation: "based on the Delta chi^2 = 6.17 surface"
THR = CHI2_GLOBAL_MIN + DCHI2 - CHI2_NEWTON   # 2.89
A2 = -4.0 / 3.0
A0 = 1.0 / 3.0
S_MIN_LEE = 52.0            # um, kleinster Abstand Lee 2020
T_DET, T_ATT = 54.0, 99.0   # um, Dicken der Pt-Testkoerper (Lee 2020, Generation 2)


def lade_tabelle():
    zeilen = [z.split() for z in TAB.strip().splitlines()]
    a = np.array([[float(x) for x in z] for z in zeilen])
    return {
        "lam": a[:, 0] * 1000.0,
        "astar": a[:, 1],
        "sig": a[:, 2],
        "ap": a[:, 3],
        "am": a[:, 4],
        "aabs": a[:, 5],
        "chi2": a[:, 6],
    }


class Likelihood:
    """Je lambda: alpha_star(lambda), sigma(lambda) als Gauss-Linearmodell.
    art = 'V2': aus +-alpha95 so, dass die Tabellengrenzen unter THR exakt herauskommen.
    art = 'V1': alpha* und sigma direkt aus der Tabelle.
    art = 'V0': wie V2, aber alpha* := 0 (vorzeichenneutral, 'konservativ' ohne Ueberschuss)."""

    def __init__(self, tab, art):
        self.art = art
        self.loglam = np.log(tab["lam"])
        if art in ("V2", "V0"):
            self.log_ap = np.log(tab["ap"])
            self.log_am = np.log(-tab["am"])
        elif art == "V1":
            self.logsig = np.log(tab["sig"])
            self.z = tab["astar"] / tab["sig"]
        else:
            raise ValueError(art)

    def werte(self, lam):
        x = np.log(np.asarray(lam, dtype=float))
        if self.art in ("V2", "V0"):
            ap = np.exp(np.interp(x, self.loglam, self.log_ap))
            am = -np.exp(np.interp(x, self.loglam, self.log_am))
            astar = 0.5 * (ap + am)
            sig = np.sqrt(-ap * am / THR)
            if self.art == "V0":
                astar = np.zeros_like(astar)
            return astar, sig
        sig = np.exp(np.interp(x, self.loglam, self.logsig))
        z = np.interp(x, self.loglam, self.z)
        return z * sig, sig


def delta_einzel(lik, lam, alpha):
    astar, sig = lik.werte(lam)
    return (alpha * alpha - 2.0 * alpha * astar) / sig ** 2


def delta_paar(lik, l2, l0, rho):
    """l2 (Zeilen), l0 (Spalten) als 1D-Arrays; rho als 2D-Array (len(l2) x len(l0))."""
    a2s, s2 = lik.werte(l2)
    a0s, s0 = lik.werte(l0)
    p2 = 1.0 / s2 ** 2
    p0 = 1.0 / s0 ** 2
    t2 = (p2 * (A2 * A2 - 2.0 * A2 * a2s))[:, None]
    t0 = (p0 * (A0 * A0 - 2.0 * A0 * a0s))[None, :]
    kreuz = 2.0 * A2 * A0 * rho * np.sqrt(np.outer(p2, p0))
    return t2 + t0 + kreuz


def rho_exp(l2, l0):
    L2, L0 = np.meshgrid(l2, l0, indexing="ij")
    return 2.0 * np.sqrt(L2 * L0) / (L2 + L0)


def rho_fenster(l2, l0, s1, s2):
    def integ(k):
        return (np.exp(-k * s1) - np.exp(-k * s2)) / k
    x2 = (1.0 / l2)[:, None]
    x0 = (1.0 / l0)[None, :]
    num = integ(x2 + x0)
    return num / np.sqrt(integ(2.0 * x2) * integ(2.0 * x0))


def g_platte(lam):
    lam = np.asarray(lam, dtype=float)
    return lam ** 3 * (1.0 - np.exp(-T_DET / lam)) * (1.0 - np.exp(-T_ATT / lam))


def gewichte_anpassen(lik, s_gitter, lam_min=10.0, lam_max=150.0):
    """Gewichte w_s >= 0 so, dass 1/(sigma^2 g^2) = sum_s w_s exp(-2 s/lambda) (relativ) fuer Tabellen-lambda."""
    try:
        from scipy.optimize import nnls
    except Exception as exc:  # pragma: no cover
        return None, {"fehler": "scipy nicht verfuegbar: %r" % (exc,)}
    lam_tab = np.exp(lik.loglam)
    sel = (lam_tab >= lam_min) & (lam_tab <= lam_max)
    L = lam_tab[sel]
    _, sig = lik.werte(L)
    ziel = 1.0 / (sig ** 2 * g_platte(L) ** 2)
    M = np.exp(-2.0 * np.outer(1.0 / L, s_gitter))
    Mr = M / ziel[:, None]
    b = np.ones_like(ziel)
    w, rnorm = nnls(Mr, b, maxiter=100000)
    rel = (M @ w) / ziel - 1.0
    info = {
        "lam_tab_um": [float(v) for v in L],
        "rel_abweichung_sigma2g2": [float(v) for v in rel],
        "max_abs_rel": float(np.max(np.abs(rel))),
        "s_gitter_um": [float(v) for v in s_gitter],
        "w": [float(v) for v in w],
        "anteil_w_je_s": [float(v) for v in (w / w.sum() if w.sum() > 0 else w)],
        "rnorm": float(rnorm),
    }
    return w, info


def rho_aus_gewichten(l2, l0, s, w):
    E2 = np.exp(-np.outer(1.0 / l2, s))
    E0 = np.exp(-np.outer(1.0 / l0, s))
    num = (E2 * w[None, :]) @ E0.T
    n2 = (E2 ** 2 * w[None, :]).sum(axis=1)
    n0 = (E0 ** 2 * w[None, :]).sum(axis=1)
    return num / np.sqrt(np.outer(n2, n0))


def einzelgrenzen(lik, alpha, lam_gitter):
    d = delta_einzel(lik, lam_gitter, alpha)
    aus = d >= THR
    wechsel = []
    for i in range(1, len(lam_gitter)):
        if aus[i] != aus[i - 1]:
            # lineare Interpolation der Schwelle
            x0, x1 = lam_gitter[i - 1], lam_gitter[i]
            y0, y1 = d[i - 1] - THR, d[i] - THR
            xs = x0 + (x1 - x0) * (-y0) / (y1 - y0) if y1 != y0 else x1
            wechsel.append({"lam_um": float(xs), "ab_hier": "ausgeschlossen" if aus[i] else "erlaubt"})
    return wechsel


def intervalle(maske, achse):
    out = []
    start = None
    for i, m in enumerate(maske):
        if m and start is None:
            start = achse[i]
        if (not m) and start is not None:
            out.append([float(start), float(achse[i - 1])])
            start = None
    if start is not None:
        out.append([float(start), float(achse[-1])])
    return out


def auswerten(name, erlaubt, l2, l0, l2_wahl, l0_wahl):
    res = {"name": name}
    # Spitze: groesstes lambda2 mit irgendeinem erlaubten lambda0
    zeilen_mit = np.where(erlaubt.any(axis=1))[0]
    if len(zeilen_mit) > 0:
        i_max = zeilen_mit.max()
        res["spitze_lambda2_um"] = float(l2[i_max])
        res["spitze_lambda0_intervalle_um"] = intervalle(erlaubt[i_max], l0)
    else:
        res["spitze_lambda2_um"] = None
    # je lambda2 die erlaubten lambda0
    res["je_lambda2"] = {}
    for v in l2_wahl:
        i = int(np.argmin(np.abs(l2 - v)))
        res["je_lambda2"]["%.2f" % l2[i]] = intervalle(erlaubt[i], l0)
    res["je_lambda0"] = {}
    for v in l0_wahl:
        j = int(np.argmin(np.abs(l0 - v)))
        res["je_lambda0"]["%.2f" % l0[j]] = intervalle(erlaubt[:, j], l2)
    # Zunge: erlaubte Punkte mit lambda2 > 27.5 um (oberhalb der Einzelgrenzen fuer m0 = m2)
    zunge = erlaubt & (l2[:, None] > 27.5)
    if zunge.any():
        ii, jj = np.where(zunge)
        verh = l0[jj] / l2[ii]
        res["zunge_verhaeltnis_l0_l2_min_max"] = [float(verh.min()), float(verh.max())]
        res["zunge_punkte"] = int(zunge.sum())
    else:
        res["zunge_verhaeltnis_l0_l2_min_max"] = None
        res["zunge_punkte"] = 0
    return res


def ascii_karte(erlaubt, l2, l0, l2_zeilen, l0_spalten):
    zeilen = []
    kopf = "l2\\l0 " + "".join("%-5d" % int(v) if k % 5 == 0 else "" for k, v in enumerate(l0_spalten))
    zeilen.append("lambda0 [um] von %.0f bis %.0f in Schritten von %.0f (Spalten); '.' erlaubt, '#' ausgeschlossen"
                  % (l0_spalten[0], l0_spalten[-1], l0_spalten[1] - l0_spalten[0]))
    for v in l2_zeilen:
        i = int(np.argmin(np.abs(l2 - v)))
        s = ""
        for w in l0_spalten:
            j = int(np.argmin(np.abs(l0 - w)))
            s += "." if erlaubt[i, j] else "#"
        zeilen.append("%5.1f  %s" % (l2[i], s))
    return zeilen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--schritt", type=float, default=0.25)
    args = ap.parse_args()
    t_start = time.time()
    import os
    os.makedirs(args.out, exist_ok=True)

    tab = lade_tabelle()
    lik = {k: Likelihood(tab, k) for k in ("V2", "V1", "V0")}

    l2 = np.arange(10.0, 60.0 + 1e-9, args.schritt)
    l0 = np.arange(10.0, 300.0 + 1e-9, args.schritt)
    feinlam = np.arange(5.0, 300.0 + 1e-9, 0.01)

    bericht = []
    erg = {
        "zeit_start_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t_start)),
        "annahmen": {
            "THR": THR, "CHI2_NEWTON": CHI2_NEWTON, "CHI2_GLOBAL_MIN": CHI2_GLOBAL_MIN, "DCHI2": DCHI2,
            "A2": A2, "A0": A0, "S_MIN_LEE_um": S_MIN_LEE, "Dicken_um": [T_DET, T_ATT],
            "gitter_l2_um": [float(l2[0]), float(l2[-1]), args.schritt],
            "gitter_l0_um": [float(l0[0]), float(l0[-1]), args.schritt],
        },
    }
    bericht.append("ST-1 Raster, Start %s UTC, numpy %s" % (erg["zeit_start_utc"], np.__version__))
    bericht.append("Schwelle Delta >= %.4f (chi2 >= %.2f)" % (THR, CHI2_GLOBAL_MIN + DCHI2))

    # --- Gegenproben: Einzelterme gegen Tabelle ---
    proben = {}
    for art in ("V2", "V1", "V0"):
        proben[art] = {}
        for alpha in (-4.0 / 3.0, -1.0, 1.0 / 3.0, 1.0):
            proben[art]["%+.4f" % alpha] = einzelgrenzen(lik[art], alpha, feinlam)
    erg["einzelproben"] = proben
    # Tabellen-Sollwerte (log-Interpolation der Spalten +-alpha95)
    soll = {}
    lamt = tab["lam"]
    for alpha in (-4.0 / 3.0, -1.0):
        y = np.log(-tab["am"])
        x = np.log(lamt)
        # -alpha95 faellt mit lambda; gesucht lambda mit -am = |alpha|
        f = np.log(abs(alpha))
        idx = np.where((y[:-1] >= f) & (y[1:] < f))[0]
        soll["%+.4f" % alpha] = [float(np.exp(x[i] + (x[i + 1] - x[i]) * (f - y[i]) / (y[i + 1] - y[i]))) for i in idx]
    for alpha in (1.0 / 3.0, 1.0):
        y = np.log(tab["ap"])
        x = np.log(lamt)
        f = np.log(alpha)
        idx = np.where((y[:-1] >= f) & (y[1:] < f))[0]
        soll["%+.4f" % alpha] = [float(np.exp(x[i] + (x[i + 1] - x[i]) * (f - y[i]) / (y[i + 1] - y[i]))) for i in idx]
    erg["tabellen_sollwerte_um"] = soll
    bericht.append("")
    bericht.append("Gegenprobe Einzelterme (lambda, ab dem ausgeschlossen; Tabelle log-interpoliert):")
    for key in soll:
        z = "  alpha %s: Tabelle %s" % (key, ", ".join("%.2f" % v for v in soll[key]))
        for art in ("V2", "V1", "V0"):
            w = [e["lam_um"] for e in proben[art][key] if e["ab_hier"] == "ausgeschlossen"]
            z += " | %s %s" % (art, ", ".join("%.2f" % v for v in w) if w else "-")
        bericht.append(z)

    # --- Nullprobe und Grenzfallprobe ---
    r_eq = rho_exp(np.array([30.0]), np.array([30.0]))[0, 0]
    d_paar_eq = delta_paar(lik["V2"], np.array([30.0]), np.array([30.0]), np.array([[r_eq]]))[0, 0]
    d_einz_m1 = delta_einzel(lik["V2"], np.array([30.0]), -1.0)[0]
    d_null = delta_paar(lik["V2"], np.array([5.0]), np.array([5.0]), np.array([[1.0]]))[0, 0]
    erg["proben"] = {"rho_exp_gleich": float(r_eq), "paar_30_30": float(d_paar_eq), "einzel_minus1_30": float(d_einz_m1),
                     "paar_5_5": float(d_null)}
    bericht.append("")
    bericht.append("Grenzfallprobe lambda0 = lambda2 = 30 um: Paar %.6f gegen Einzel alpha=-1 %.6f (rho %.6f)"
                   % (d_paar_eq, d_einz_m1, r_eq))
    bericht.append("Nullprobe lambda0 = lambda2 = 5 um: Delta %.3e (muss << %.2f sein)" % (d_null, THR))

    # --- Korrelationsmodelle ---
    rhos = {}
    rhos["exp"] = rho_exp(l2, l0)
    rhos["fenster52_150"] = rho_fenster(l2, l0, S_MIN_LEE, 150.0)
    rhos["fenster52_300"] = rho_fenster(l2, l0, S_MIN_LEE, 300.0)
    s_gitter = np.exp(np.linspace(np.log(S_MIN_LEE), np.log(1000.0), 40))
    w, winfo = gewichte_anpassen(lik["V2"], s_gitter)
    erg["gewichtsanpassung"] = winfo
    if w is not None and np.sum(w) > 0:
        rhos["angepasst"] = rho_aus_gewichten(l2, l0, s_gitter, w)
        bericht.append("")
        bericht.append("Gewichtsanpassung: max |rel. Abweichung| %.3f ueber %d Tabellen-lambda (10..150 um); "
                       "Gewichtsanteile > 1%% bei s = %s um"
                       % (winfo["max_abs_rel"], len(winfo["lam_tab_um"]),
                          ", ".join("%.0f" % s for s, a in zip(winfo["s_gitter_um"], winfo["anteil_w_je_s"]) if a > 0.01)))
    for c in (0.90, 0.95, 0.98, 1.00):
        rhos["konst%.2f" % c] = np.full((len(l2), len(l0)), c)

    # rho-Vergleich an einigen Punkten
    punkte = [(30.0, 45.0), (35.0, 56.0), (38.5, 63.0), (40.0, 67.0)]
    bericht.append("")
    bericht.append("rho an Stichpunkten (lambda2, lambda0): " + "; ".join(
        "(%g, %g): " % p + ", ".join("%s %.4f" % (k, rhos[k][int(np.argmin(np.abs(l2 - p[0]))), int(np.argmin(np.abs(l0 - p[1])))])
                                   for k in rhos if not k.startswith("konst")) for p in punkte))

    # --- HUST-Was-waere-wenn [H] ---
    # HUST als unabhaengiges Experiment mit Mittelwert 0, kleinstem Abstand s_H, Template-Empfindlichkeit
    # sigma_H(lambda) = r * sigma_V2(lambda) * exp((s_H - 52)/lambda), r so, dass HUST allein |alpha| = 1 bei 48 um ausschliesst.
    def hust_delta(s_h, l2v, l0v, rho):
        _, sig48 = lik["V2"].werte(np.array([48.0]))
        r = 1.0 / (math.sqrt(THR) * sig48[0] * math.exp((s_h - S_MIN_LEE) / 48.0))
        _, s2 = lik["V2"].werte(l2v)
        _, s0 = lik["V2"].werte(l0v)
        sh2 = r * s2 * np.exp((s_h - S_MIN_LEE) / l2v)
        sh0 = r * s0 * np.exp((s_h - S_MIN_LEE) / l0v)
        p2 = 1.0 / sh2 ** 2
        p0 = 1.0 / sh0 ** 2
        return (p2 * A2 * A2)[:, None] + (p0 * A0 * A0)[None, :] + 2.0 * A2 * A0 * rho * np.sqrt(np.outer(p2, p0)), r

    # --- Modelle rechnen ---
    modelle = []
    for art in ("V2", "V1", "V0"):
        for rk in rhos:
            if art != "V2" and rk not in ("exp", "konst1.00"):
                continue
            modelle.append((art, rk, None))
    for s_h in (200.0, 300.0):
        modelle.append(("V2", "exp", s_h))

    l2_wahl = [20, 24, 25, 26, 27, 28, 30, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 48, 50]
    l0_wahl = [30, 40, 45, 50, 55, 57, 58, 60, 65, 70, 75, 80, 90, 100, 150]
    erg["modelle"] = {}
    karten = {}
    for art, rk, s_h in modelle:
        name = "%s_%s" % (art, rk) + ("" if s_h is None else "_HUST%d" % int(s_h))
        d = delta_paar(lik[art], l2, l0, rhos[rk])
        info_h = None
        if s_h is not None:
            dh, r = hust_delta(s_h, l2, l0, rhos[rk])
            d = d + dh
            info_h = {"s_H_um": s_h, "r": r}
        erlaubt = d < THR
        res = auswerten(name, erlaubt, l2, l0, l2_wahl, l0_wahl)
        res["min_delta_bei_l2_gt_27p5"] = float(np.min(np.where(l2[:, None] > 27.5, d, np.inf)))
        if info_h:
            res["hust"] = info_h
        erg["modelle"][name] = res
        if name in ("V2_exp", "V2_konst1.00", "V2_konst0.90", "V2_exp_HUST200", "V0_exp", "V2_angepasst"):
            karten[name] = ascii_karte(erlaubt, l2, l0, np.arange(16.0, 50.0 + 1e-9, 1.0), np.arange(16.0, 120.0 + 1e-9, 2.0))

    # --- Bericht ---
    bericht.append("")
    bericht.append("Spitze der Zunge je Modell (groesstes lambda2 mit erlaubtem lambda0; erlaubte lambda0 dort):")
    for name, res in erg["modelle"].items():
        sp = res["spitze_lambda2_um"]
        bericht.append("  %-24s Spitze lambda2 = %s um, lambda0 = %s; Verhaeltnis l0/l2 in der Zunge (l2 > 27,5): %s; min Delta (l2 > 27,5) = %.3f"
                       % (name, "%.2f" % sp if sp is not None else "-",
                          res.get("spitze_lambda0_intervalle_um"), res["zunge_verhaeltnis_l0_l2_min_max"],
                          res["min_delta_bei_l2_gt_27p5"]))
    bericht.append("")
    bericht.append("Hauptmodell V2_exp: erlaubte lambda0 je lambda2 [um]:")
    for k, v in erg["modelle"]["V2_exp"]["je_lambda2"].items():
        bericht.append("  lambda2 %s: %s" % (k, v))
    bericht.append("")
    bericht.append("Hauptmodell V2_exp: erlaubte lambda2 je lambda0 [um]:")
    for k, v in erg["modelle"]["V2_exp"]["je_lambda0"].items():
        bericht.append("  lambda0 %s: %s" % (k, v))
    for name, zeilen in karten.items():
        bericht.append("")
        bericht.append("Karte %s (Zeilen lambda2 [um])" % name)
        bericht.extend(zeilen)

    erg["laufzeit_s"] = time.time() - t_start
    bericht.append("")
    bericht.append("Laufzeit %.2f s" % erg["laufzeit_s"])
    with open(os.path.join(args.out, "st1raster_ergebnis.json"), "w") as fh:
        json.dump(erg, fh, indent=1)
    with open(os.path.join(args.out, "st1raster_bericht.txt"), "w") as fh:
        fh.write("\n".join(bericht) + "\n")
    print("\n".join(bericht))
    return 0


if __name__ == "__main__":
    sys.exit(main())
