#!/usr/bin/env python3
# PAAR-REGGE-1 (Runde 42), Code-Agent fuer die Leitung claude-primary.
# Klassischer, starr rotierender Nambu-Goto-String mit zwei gleichen Endmassen m gegen die fuehrende
# Gitter-Glueball-Trajektorie (2++, 4++). Einheiten: sigma = 1 (Massen in sqrt(sigma)), c = 1.
#
# Modell [P] coordination/regge-anschluss-20260912.md Z. 146-155 (gleiche Endmassen m, Endgeschwindigkeit v):
#   kappa/omega = m v/(1 - v^2),   kappa = sigma_A/sigma
#   E = 2 m/sqrt(1 - v^2) + (2 kappa/omega) arcsin v
#   J = 2 m v^2/(omega sqrt(1 - v^2)) + (kappa/omega^2) (arcsin v - v sqrt(1 - v^2))
# Variante "D" (nur Diagnose): Kraftgleichgewicht der Dossier-Handrechnung sigma_A = gamma m v^2/R
#   (gluon-paar-l/ARBEITSFELD.md Z. 174, 304), also kappa/omega = gamma m v.
# Intercept a (fest): J = J_cl + a.
# Parametrisierung v = tanh(eta), damit v nahe 1 genau bleibt.
#
# Aufruf nur ueber kleintest.sh auf der .69:
#   paar_regge.py kontrollen <aus.json>
#   paar_regge.py fits <aus.json>
#   paar_regge.py bild <fits.json> <aus.png>
import json
import math
import sys
import time

import numpy as np
import scipy
from scipy.optimize import brentq, minimize_scalar
from scipy.stats import chi2 as chi2vert

KAPPA = {"9/4": 9.0 / 4.0, "2.14": 2.14, "2.36": 2.36}
A_4D = {"0": 0.0, "1/12": 1.0 / 12.0}
A_3D = {"0": 0.0, "1/24": 1.0 / 24.0}
J_PUNKTE = (2.0, 4.0)

DATEN_A = {"quelle": "Athenodorou/Teper 2020, Tab. 17 (gluon-paar-l/quellen/F3 Z. 1985-1993)",
           "M": (4.894, 7.60), "dM": (0.022, 0.12)}
LINIE_B = {"quelle": "Meyer/Teper 2004, Gl. (3) (gluon-paar-l/quellen/F2 Z. 157)",
           "s": 0.281, "ds": 0.022, "a0": 0.93, "da0": 0.24}
LINIE_3D = {"quelle": "Meyer/Teper 2004, Gl. (5) (gluon-paar-l/quellen/F2 Z. 257)",
            "s": 0.384, "ds": 0.016, "a0": -1.144, "da0": 0.071}

V_BAND = (0.70, 0.82)
P_MIN = 0.05
M_MAX = 4.0
N_GITTER = 2001
KARTE_MASSELOS = 5.32
KARTE_V34 = 6.80
TOL_PR0 = 1e-3


# ---------------------------------------------------------------- Modell
def omega_von(m, kappa, eta, variante):
    if variante == "P":   # kappa/omega = m v/(1 - v^2) = m sinh(eta) cosh(eta)
        return kappa / (m * math.sinh(eta) * math.cosh(eta))
    if variante == "D":   # kappa/omega = gamma m v = m sinh(eta)
        return kappa / (m * math.sinh(eta))
    raise ValueError(variante)


def EJ(m, kappa, eta, variante="P"):
    v = math.tanh(eta)
    ch = math.cosh(eta)
    wurzel = 1.0 / ch                 # sqrt(1 - v^2)
    asv = math.atan(math.sinh(eta))   # arcsin(v)
    w = omega_von(m, kappa, eta, variante)
    E = 2.0 * m * ch + (2.0 * kappa / w) * asv
    J = 2.0 * m * v * v * ch / w + (kappa / (w * w)) * (asv - v * wurzel)
    return E, J, w, v


def loese(m, kappa, Jcl, variante="P"):
    """Zustand mit klassischem Drehimpuls Jcl bei Endmasse m (m = 0: masseloser String)."""
    if Jcl <= 0.0:
        raise ValueError("J_cl <= 0")
    if m <= 0.0:
        E = math.sqrt(2.0 * math.pi * kappa * Jcl)
        w = math.pi * kappa / E
        return {"E": E, "v": 1.0, "omega": w, "laenge": 2.0 / w}
    f = lambda eta: EJ(m, kappa, eta, variante)[1] - Jcl
    eta = brentq(f, 1e-9, 60.0, xtol=1e-14, rtol=1e-13, maxiter=1000)
    E, J, w, v = EJ(m, kappa, eta, variante)
    return {"E": E, "v": v, "omega": w, "laenge": 2.0 * v / w}


def sekante(E2, E4):
    """Gerade J = a0 + (s/2pi) M^2 durch (M = E2, J = 2) und (M = E4, J = 4); s = 2 pi sigma alpha'."""
    s = 2.0 * math.pi * (J_PUNKTE[1] - J_PUNKTE[0]) / (E4 * E4 - E2 * E2)
    a0 = J_PUNKTE[0] - s / (2.0 * math.pi) * E2 * E2
    return s, a0


def linien_punkte(linie):
    """Punkte der Geraden bei J = 2, 4 und ihre Kovarianz aus unkorrelierten Fehlern von s und a0 (linear)."""
    s, a0 = linie["s"], linie["a0"]
    M = [math.sqrt(2.0 * math.pi * (J - a0) / s) for J in J_PUNKTE]
    G = [[-Mi / (2.0 * s), -Mi / (2.0 * (J - a0))] for Mi, J in zip(M, J_PUNKTE)]
    D = [linie["ds"] ** 2, linie["da0"] ** 2]
    C = [[sum(G[i][k] * G[j][k] * D[k] for k in range(2)) for j in range(2)] for i in range(2)]
    return M, C


# ---------------------------------------------------------------- chi^2
def chi2_funktion(datensatz, kappa, a, lesart, variante="P"):
    if datensatz == "A":
        M, dM = DATEN_A["M"], DATEN_A["dM"]

        def f(m):
            r = [loese(m, kappa, J - a, variante)["E"] for J in J_PUNKTE]
            return sum(((ri - Mi) / di) ** 2 for ri, Mi, di in zip(r, M, dM))
        return f
    linie = LINIE_B if datensatz == "B" else LINIE_3D
    if lesart == "R3":   # exakt im Parameterraum (s, a0), unkorreliert
        def f(m):
            E2, E4 = (loese(m, kappa, J - a, variante)["E"] for J in J_PUNKTE)
            s, a0 = sekante(E2, E4)
            return ((s - linie["s"]) / linie["ds"]) ** 2 + ((a0 - linie["a0"]) / linie["da0"]) ** 2
        return f
    M, C = linien_punkte(linie)
    if lesart == "R1":   # Massenraum, Bandbreite je Punkt, ohne Korrelation
        d = [math.sqrt(C[0][0]), math.sqrt(C[1][1])]

        def f(m):
            r = [loese(m, kappa, J - a, variante)["E"] for J in J_PUNKTE]
            return sum(((ri - Mi) / di) ** 2 for ri, Mi, di in zip(r, M, d))
        return f
    if lesart == "R2":   # Massenraum, volle Kovarianz (lineare Fortpflanzung)
        Ci = np.linalg.inv(np.array(C))
        Mv = np.array(M)

        def f(m):
            r = np.array([loese(m, kappa, J - a, variante)["E"] for J in J_PUNKTE]) - Mv
            return float(r @ Ci @ r)
        return f
    raise ValueError(lesart)


def fitte(f):
    ms = np.linspace(0.0, M_MAX, N_GITTER)
    c = np.array([f(float(m)) for m in ms])
    i = int(np.argmin(c))
    lo = float(ms[max(i - 1, 0)])
    hi = float(ms[min(i + 1, N_GITTER - 1)])
    res = minimize_scalar(f, bounds=(lo, hi), method="bounded", options={"xatol": 1e-10})
    mb, cb = float(res.x), float(res.fun)
    if c[i] < cb:
        mb, cb = float(ms[i]), float(c[i])
    c0 = f(0.0)
    if c0 <= cb:
        mb, cb = 0.0, c0
    g = lambda m: f(m) - cb - 1.0
    # linker Rand des 1-sigma-Intervalls
    if g(0.0) <= 0.0:
        links = 0.0
    else:
        j = i
        while j > 0 and c[j] - cb <= 1.0:
            j -= 1
        b_ = float(ms[j + 1])
        if g(b_) > 0.0:
            b_ = mb
        links = brentq(g, float(ms[j]), b_, xtol=1e-10)
    # rechter Rand
    j = i
    while j < N_GITTER - 1 and c[j] - cb <= 1.0:
        j += 1
    if c[j] - cb <= 1.0:
        rechts = None
    else:
        a_ = float(ms[j - 1])
        if g(a_) > 0.0:
            a_ = mb
        rechts = brentq(g, a_, float(ms[j]), xtol=1e-10)
    lokmin = int(sum(1 for k in range(1, N_GITTER - 1) if c[k] < c[k - 1] and c[k] < c[k + 1]))
    return {"m": mb, "chi2": cb, "p": float(chi2vert.sf(cb, 1)), "m_1sigma": [links, rechts],
            "chi2_m0": c0, "dchi2_m0": c0 - cb, "lokale_minima_gitter": lokmin,
            "gitter": {"m_max": M_MAX, "n": N_GITTER}}


def details(m, kappa, a, variante):
    r2 = loese(m, kappa, J_PUNKTE[0] - a, variante)
    r4 = loese(m, kappa, J_PUNKTE[1] - a, variante)
    s, a0 = sekante(r2["E"], r4["E"])
    return {"E2": r2["E"], "E4": r4["E"], "v_end2": r2["v"], "v_end4": r4["v"],
            "laenge2": r2["laenge"], "laenge4": r4["laenge"], "s_sekante": s, "a0_sekante": a0}


def ein_fit(datensatz, kappa_name, a_name, a, lesart, variante):
    kappa = KAPPA[kappa_name]
    t0 = time.perf_counter()
    f = chi2_funktion(datensatz, kappa, a, lesart, variante)
    r = fitte(f)
    r.update(details(r["m"], kappa, a, variante))
    lo, hi = r["m_1sigma"]
    r["v_end2_1sigma"] = [loese(x, kappa, J_PUNKTE[0] - a, variante)["v"] if x is not None else None
                          for x in (lo, hi)]
    r.update({"datensatz": datensatz, "kappa": kappa_name, "a": a_name, "lesart": lesart,
              "variante": variante, "sekunden": time.perf_counter() - t0})
    return r


# ---------------------------------------------------------------- Baender (vorab festgelegt, PLAN.md Abschn. 5)
def baender(recs):
    """recs: Fits eines Datensatzes (gleiche kappa, Lesart, Variante) fuer beide a."""
    traegt = any(r["p"] >= P_MIN and V_BAND[0] <= r["v_end2"] <= V_BAND[1] for r in recs)
    masselos = any(r["p"] >= P_MIN and r["dchi2_m0"] <= 1.0 for r in recs)
    nicht = all(r["p"] < P_MIN for r in recs)
    liste = []
    if traegt:
        liste.append("(a) traegt")
    if masselos:
        liste.append("masselos")
    if nicht:
        liste.append("traegt nicht")
    if not liste:
        liste.append("uebrig")
    return liste


def auswerten(fits):
    def wahl(ds, kappa, lesart, variante):
        return [r for r in fits if r["datensatz"] == ds and r["kappa"] == kappa
                and r["lesart"] == lesart and r["variante"] == variante]
    tab = {}
    for ds, les_liste in (("A", ("diag",)), ("B", ("R3", "R1", "R2"))):
        for kappa in KAPPA:
            for les in les_liste:
                tab[f"{ds}|{kappa}|{les}"] = baender(wahl(ds, kappa, les, "P"))
    pr1_plan = "(a) traegt" in tab["B|9/4|R3"]
    pr2_plan = "(a) traegt" in tab["A|9/4|diag"]
    pr1_lesarten = {les: ("(a) traegt" in tab[f"B|9/4|{les}"]) for les in ("R1", "R2", "R3")}
    if all(pr1_lesarten.values()):
        pr1_wort = "eingetroffen"
    elif not any(pr1_lesarten.values()):
        pr1_wort = "nicht eingetroffen"
    else:
        pr1_wort = "uneindeutig (haengt an der Lesart des Bandes)"
    robust = {}
    for ds, les in (("A", "diag"), ("B", "R3")):
        robust[ds] = {k: tab[f"{ds}|{k}|{les}"] for k in KAPPA}
    return {"baender": tab,
            "PR1_plan": "eingetroffen" if pr1_plan else "nicht eingetroffen",
            "PR2_plan": "eingetroffen" if pr2_plan else "nicht eingetroffen",
            "PR1_wortlaut": pr1_wort, "PR1_je_lesart": pr1_lesarten,
            "PR2_wortlaut": "eingetroffen" if pr2_plan else "nicht eingetroffen",
            "kappa_robustheit": robust}


# ---------------------------------------------------------------- Kontrollen
def kontrollen():
    k = KAPPA["9/4"]
    out = {}
    E_geschl = math.sqrt(2.0 * math.pi * k * 2.0)
    out["K1_masselos"] = {"E_geschlossen": E_geschl,
                          "E_grenzwert": {str(m): loese(m, k, 2.0)["E"] for m in (1e-4, 1e-6, 1e-8)},
                          "laenge": loese(0.0, k, 2.0)["laenge"]}

    def konst_v(v, J, variante):
        eta = math.atanh(v)
        E1, J1, w1, _ = EJ(1.0, k, eta, variante)   # E^2/J haengt bei festem v nicht von m ab
        m = math.sqrt(J / J1)                       # J skaliert wie m^2, E wie m
        E = E1 * m
        w = omega_von(m, k, eta, variante)
        return {"E": E, "m": m, "laenge": 2.0 * v / w, "s": 2.0 * math.pi * J1 / (E1 * E1)}

    out["K2_konst_v34"] = {var: konst_v(0.75, 2.0, var) for var in ("P", "D")}
    s_A = sekante(*DATEN_A["M"])[0]
    out["K4_sonderfall_konst_v"] = {"s_A_sekante": s_A, "s_B": LINIE_B["s"]}
    for var in ("P", "D"):
        sv = lambda v: konst_v(v, 2.0, var)["s"]
        out["K4_sonderfall_konst_v"][var] = {
            "v_B": brentq(lambda v: sv(v) - LINIE_B["s"], 0.01, 0.999999, xtol=1e-12),
            "v_A": brentq(lambda v: sv(v) - s_A, 0.01, 0.999999, xtol=1e-12),
            "s_bei_v": {str(v): sv(v) for v in (0.5, 0.7, 0.75, 0.8, 0.9, 0.99, 0.999999)}}

    def hauptsatz(var, m=1.0):
        werte = []
        for eta in np.linspace(0.1, 3.0, 30):
            h = 1e-5
            Ep, Jp, _, _ = EJ(m, k, eta + h, var)
            Em, Jm, _, _ = EJ(m, k, eta - h, var)
            w = EJ(m, k, eta, var)[2]
            werte.append(abs((Ep - Em) / (Jp - Jm) / w - 1.0))
        return {"max_rel_abweichung_dEdJ_omega": max(werte), "min": min(werte)}
    out["K3_erster_hauptsatz"] = {var: hauptsatz(var) for var in ("P", "D")}

    E1 = out["K1_masselos"]["E_geschlossen"]
    E2 = out["K2_konst_v34"]["P"]["E"]
    out["PR0"] = {
        "masselos_rel": abs(E1 / KARTE_MASSELOS - 1.0), "masselos_abs": abs(E1 - KARTE_MASSELOS),
        "v34_rel": abs(E2 / KARTE_V34 - 1.0), "v34_abs": abs(E2 - KARTE_V34),
        "v34_rel_variante_D": abs(out["K2_konst_v34"]["D"]["E"] / KARTE_V34 - 1.0)}
    p = out["PR0"]
    p["plan_relativ"] = "eingetroffen" if (p["masselos_rel"] <= TOL_PR0 and p["v34_rel"] <= TOL_PR0) \
        else "nicht eingetroffen"
    p["wortlaut_absolut"] = "eingetroffen" if (p["masselos_abs"] <= TOL_PR0 and p["v34_abs"] <= TOL_PR0) \
        else "nicht eingetroffen"
    # Budgetmessung ohne Datensicht: 1000 Loesungen bei beliebigen m, J
    t0 = time.perf_counter()
    for i in range(1000):
        loese(0.05 + 0.003 * i, k, 1.0 + 0.002 * i)
    out["budget_s_je_loesung"] = (time.perf_counter() - t0) / 1000.0
    return out


# ---------------------------------------------------------------- Fits
def fits():
    recs = []
    for ds, les_liste in (("A", ("diag",)), ("B", ("R3", "R1", "R2"))):
        for kappa_name in KAPPA:
            for les in les_liste:
                for a_name, a in A_4D.items():
                    recs.append(ein_fit(ds, kappa_name, a_name, a, les, "P"))
    nachtrag = [ein_fit("3D", "9/4", a_name, a, "R3", "P") for a_name, a in A_3D.items()]
    diag_D = []
    for ds, les in (("A", "diag"), ("B", "R3")):
        for a_name, a in A_4D.items():
            diag_D.append(ein_fit(ds, "9/4", a_name, a, les, "D"))
    M_B, C_B = linien_punkte(LINIE_B)
    M_3, C_3 = linien_punkte(LINIE_3D)
    return {"fits": recs, "auswertung": auswerten(recs), "nachtrag_2plus1": nachtrag,
            "diagnose_dossier_kraft": diag_D,
            "daten": {"A": DATEN_A, "B": LINIE_B, "B_punkte": M_B, "B_kovarianz": C_B,
                      "3D": LINIE_3D, "3D_punkte": M_3, "3D_kovarianz": C_3}}


# ---------------------------------------------------------------- Bild
def bild(pfad_fits, pfad_png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    d = json.load(open(pfad_fits))
    k = KAPPA["9/4"]
    farbe = {"0": "#2a78d6", "1/12": "#eb6834"}
    ink, ink2, grau = "#0b0b0b", "#52514e", "#9a9893"
    fig, axs = plt.subplots(1, 2, figsize=(12.5, 5.6), sharey=True)
    fig.patch.set_facecolor("#fcfcfb")
    x_max = 90.0
    for ax, ds, les, titel in ((axs[0], "A", "diag", "(A) Athenodorou/Teper 2020"),
                               (axs[1], "B", "R3", "(B) Meyer/Teper-Gerade 2004")):
        ax.set_facecolor("#fcfcfb")
        xs = np.linspace(0.0, x_max, 200)
        ax.plot(xs, xs / (2.0 * math.pi * k), color=grau, lw=1.5, ls=":",
                label="masselos, a = 0 (Steigung 4/9)")
        if ds == "A":
            M = np.array(DATEN_A["M"]); dM = np.array(DATEN_A["dM"])
            ax.errorbar(M ** 2, J_PUNKTE, xerr=2 * M * dM, fmt="o", ms=8, color=ink, capsize=4,
                        label="Gitter 2++, 4++ (A)", zorder=5)
        else:
            L = LINIE_B
            ax.plot(xs, L["a0"] + L["s"] * xs / (2 * math.pi), color=ink2, lw=1.5,
                    label="MT-Gerade 0,281(22), 0,93(24)")
            Mp, C = linien_punkte(L)
            Mp = np.array(Mp)
            ax.errorbar(Mp ** 2, J_PUNKTE, xerr=2 * Mp * np.sqrt(np.diag(C)), fmt="s", ms=8, color=ink,
                        capsize=4, label="Punkte (B) mit Bandbreite je Punkt", zorder=5)
        for r in d["fits"]:
            if r["datensatz"] != ds or r["kappa"] != "9/4" or r["lesart"] != les or r["variante"] != "P":
                continue
            a = A_4D[r["a"]]
            m = r["m"]
            if m <= 0.0:
                xx = xs
                yy = xs / (2.0 * math.pi * k) + a
            else:
                etas = np.linspace(0.02, 8.0, 600)
                EE, JJ = [], []
                for e in etas:
                    E, J, _, _ = EJ(m, k, float(e), "P")
                    EE.append(E); JJ.append(J)
                xx = np.array(EE) ** 2
                yy = np.array(JJ) + a
                sel = (xx <= x_max) & (yy <= 6.5)
                xx, yy = xx[sel], yy[sel]
            ax.plot(xx, yy, color=farbe[r["a"]], lw=2.0,
                    label=f"Fit a = {r['a']}: m = {m:.2f}, v(2) = {r['v_end2']:.2f}, p = {r['p']:.2g}")
        ax.set_xlim(0, x_max)
        ax.set_ylim(0, 6.5)
        ax.set_xlabel("M² / σ", color=ink)
        ax.set_title(titel, color=ink, fontsize=11)
        ax.grid(True, color="#e4e3df", lw=0.6)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        ax.legend(loc="upper left", fontsize=8.5, frameon=False)
    axs[0].set_ylabel("J", color=ink)
    fig.suptitle("PAAR-REGGE-1: rotierender String mit zwei Endmassen, σ_A = 9/4 σ (3+1D)",
                 color=ink, fontsize=12)
    fig.tight_layout()
    fig.savefig(pfad_png, dpi=130, facecolor=fig.get_facecolor())


def main():
    modus = sys.argv[1]
    t0 = time.perf_counter()
    if modus == "kontrollen":
        out = kontrollen()
    elif modus == "fits":
        out = fits()
    elif modus == "bild":
        bild(sys.argv[2], sys.argv[3])
        print(f"fertig, {time.perf_counter() - t0:.1f} s")
        return
    else:
        raise SystemExit("modus?")
    out["versionen"] = {"python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__}
    out["laufzeit_s"] = time.perf_counter() - t0
    with open(sys.argv[2], "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"fertig, {out['laufzeit_s']:.1f} s")


if __name__ == "__main__":
    main()
