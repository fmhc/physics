#!/usr/bin/env python3
# PAAR-REGGE-2 (Runde 46), Code-Agent fuer die Leitung claude-primary.
# Grundlage: Kopie von paar-regge-1/code/paar_regge.py (sha256 6beafb5388e74534128d2c2b6794eff535eda5d4d58dabd241a37726b7dfb393,
# hier als paar_regge_kopie_paar-regge-1.py). Modellfunktionen EJ und loese unveraendert, erweitert um
#   - J_cl = 0 (ruhendes Paar, E = 2m), noetig fuer a = 2 bei J = 2;
#   - Intercept-Variante (I') nach H5 (Sonnenschein/Weissman 2020) Gl. (7.9), erste Ordnung;
#   - zehn Kandidaten (kappa = 9/4 und 2, a = 0, 1/12, 1/6, 1, 2) und Datensatz (C).
# Einheiten: sigma = 1 (Massen in sqrt(sigma)), c = 1.
#
# Modell [P] (PAAR-REGGE-1; klassisch gleich H5 Abschn. 5.2.1 mit kappa = 2T fuer den gefalteten geschlossenen String):
#   kappa/omega = m v/(1 - v^2),   kappa = Spannung/sigma
#   E = 2 m/sqrt(1 - v^2) + (2 kappa/omega) arcsin v
#   J_cl = 2 m v^2/(omega sqrt(1 - v^2)) + (kappa/omega^2) (arcsin v - v sqrt(1 - v^2))
# Intercept: J = J_cl + a (H5 Gl. 1.6/1.7: J = alpha' M^2 + a).
# Variante (I'): a = 2 + (3D - 55)/(24 pi) (eps1 + eps2), D = 4, eps1 = eps2 = 1/gamma = sqrt(1 - v^2) (H5 Z. 2619, 1743).
# Parametrisierung v = tanh(eta).
#
# Aufruf nur ueber kleintest.sh auf der .69:
#   paar_regge2.py rauch <aus.json>
#   paar_regge2.py kontrollen <aus.json>
#   paar_regge2.py fits <aus.json>
#   paar_regge2.py bild <fits.json> <aus.png>
import json
import math
import sys
import time

import numpy as np
import scipy
from scipy.optimize import brentq, minimize_scalar
from scipy.stats import chi2 as chi2vert

KAPPA = {"9/4": 9.0 / 4.0, "2": 2.0}                 # Steigung 1/kappa: 4/9 (offen adjungiert), 1/2 (geschlossen gefaltet)
STEIGUNG = {"9/4": "4/9", "2": "1/2"}
A_LISTE = {"0": 0.0, "1/12": 1.0 / 12.0, "1/6": 1.0 / 6.0, "1": 1.0, "2": 2.0}
VARIANTE = "2-1,1406eps"                             # (I'): a = 2 + C1 (eps1 + eps2)
D_DIM = 4
C1 = (3.0 * D_DIM - 55.0) / (24.0 * math.pi)         # -43/(24 pi)
MODELL = {"(I)": ("2", "2"), "(II)": ("9/4", "1"), "(I')": ("2", VARIANTE)}
J_PUNKTE = (2.0, 4.0)

DATEN = {
    "A": {"quelle": "Athenodorou/Teper 2020, Tab. 17: 2++ gs, 4++ gs* (gluon-paar-l/quellen/F3 Z. 1986, 1993)",
          "M": (4.894, 7.60), "dM": (0.022, 0.12)},
    "C": {"quelle": "Athenodorou/Teper 2020, Tab. 17: 2++ ex1, 4++ gs* (gluon-paar-l/quellen/F3 Z. 1988, 1993)",
          "M": (6.788, 7.60), "dM": (0.040, 0.12)},
}
LINIE_B = {"quelle": "Meyer/Teper 2004, Gl. (3) (gluon-paar-l/quellen/F2 Z. 157)",
           "s": 0.281, "ds": 0.022, "a0": 0.93, "da0": 0.24}

V_BAND = (0.70, 0.82)
P_MIN = 0.05
M_MAX = 6.0
N_GITTER = 3001                                      # Schritt 0,002 wie PAAR-REGGE-1
KARTE_PQ0 = {"(I)": (0.0, 5.013), "(II)": (3.760, 6.512)}
TOL_PQ0_LOESER = 1e-6
TOL_PQ0_RUNDUNG = 5e-4
TOL_PQ0_WORTLAUT = 1e-6
SOLL_PR1 = {"A|0": (0.0, 370.77), "A|1/12": (0.0, 202.11), "B|0": (0.258, 70.08), "B|1/12": (0.413, 67.03)}


# ---------------------------------------------------------------- Modell (EJ, loese aus PAAR-REGGE-1)
def omega_von(m, kappa, eta, variante="P"):
    if variante == "P":   # kappa/omega = m v/(1 - v^2) = m sinh(eta) cosh(eta)
        return kappa / (m * math.sinh(eta) * math.cosh(eta))
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
    """Zustand mit klassischem Drehimpuls Jcl bei Endmasse m (m = 0: masseloser String; Jcl = 0: ruhendes Paar)."""
    if abs(Jcl) < 1e-15:
        Jcl = 0.0
    if Jcl < 0.0:
        raise ValueError("J_cl < 0")
    if Jcl == 0.0:            # [F] ruhendes Paar: E = 2m, v = 0 (Grenzwert J_cl -> 0+, Kontrolle K3)
        return {"E": 2.0 * m, "v": 0.0, "omega": None, "laenge": 0.0, "J_cl": 0.0}
    if m <= 0.0:
        E = math.sqrt(2.0 * math.pi * kappa * Jcl)
        w = math.pi * kappa / E
        return {"E": E, "v": 1.0, "omega": w, "laenge": 2.0 / w, "J_cl": Jcl}
    f = lambda eta: EJ(m, kappa, eta, variante)[1] - Jcl
    eta = brentq(f, 1e-9, 60.0, xtol=1e-14, rtol=1e-13, maxiter=1000)
    E, J, w, v = EJ(m, kappa, eta, variante)
    return {"E": E, "v": v, "omega": w, "laenge": 2.0 * v / w, "J_cl": J}


def a_variante(eps):
    """H5 Gl. (7.9), erste Ordnung, gleiche Massen: a = 2 + C1 (eps1 + eps2), eps1 = eps2 = eps."""
    return 2.0 + C1 * 2.0 * eps


def hoehere_ordnung(eps):
    """Terme 2. und 3. Ordnung von H5 Gl. (7.9) bei eps1 = eps2 = eps (nur beschreibend)."""
    s = 2.0 * eps
    t2 = (D_DIM - 3.0) / (24.0 * math.pi ** 2) * s ** 2
    t3 = (D_DIM - 3.0) / (24.0 * math.pi ** 3) * s ** 3 + (8.0 * D_DIM - 495.0) / (1440.0 * math.pi) * 2.0 * eps ** 3
    return t2, t3


def zustand(m, kappa, J, a):
    """Zustand mit Gesamtdrehimpuls J. a: Zahl (fester Intercept) oder VARIANTE (I')."""
    if a != VARIANTE:
        r = dict(loese(m, kappa, J - a))
        r["a"] = a
        r["eps"] = math.sqrt(max(0.0, 1.0 - r["v"] ** 2))
        return r
    if m <= 0.0:              # eps = 0, a = 2
        r = dict(loese(0.0, kappa, J - 2.0))
        r["a"] = 2.0
        r["eps"] = 0.0
        return r
    # J_cl(eta) und a(eta) steigen beide mit eta: eindeutige Nullstelle
    f = lambda eta: EJ(m, kappa, eta)[1] + a_variante(1.0 / math.cosh(eta)) - J
    eta = brentq(f, 1e-9, 60.0, xtol=1e-14, rtol=1e-13, maxiter=1000)
    E, Jc, w, v = EJ(m, kappa, eta)
    eps = 1.0 / math.cosh(eta)
    return {"E": E, "v": v, "omega": w, "laenge": 2.0 * v / w, "J_cl": Jc, "a": a_variante(eps), "eps": eps}


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
def chi2_funktion(datensatz, kappa, a, lesart):
    if datensatz in DATEN:   # A, C (und S: synthetisch, nur Rauchtest)
        M, dM = DATEN[datensatz]["M"], DATEN[datensatz]["dM"]

        def f(m):
            r = [zustand(m, kappa, J, a)["E"] for J in J_PUNKTE]
            return sum(((ri - Mi) / di) ** 2 for ri, Mi, di in zip(r, M, dM))
        return f
    linie = LINIE_B
    if lesart == "R3":   # exakt im Parameterraum (s, a0), unkorreliert
        def f(m):
            E2, E4 = (zustand(m, kappa, J, a)["E"] for J in J_PUNKTE)
            s, a0 = sekante(E2, E4)
            return ((s - linie["s"]) / linie["ds"]) ** 2 + ((a0 - linie["a0"]) / linie["da0"]) ** 2
        return f
    M, C = linien_punkte(linie)
    if lesart == "R1":   # Massenraum, Bandbreite je Punkt, ohne Korrelation
        d = [math.sqrt(C[0][0]), math.sqrt(C[1][1])]

        def f(m):
            r = [zustand(m, kappa, J, a)["E"] for J in J_PUNKTE]
            return sum(((ri - Mi) / di) ** 2 for ri, Mi, di in zip(r, M, d))
        return f
    if lesart == "R2":   # Massenraum, volle Kovarianz (lineare Fortpflanzung)
        Ci = np.linalg.inv(np.array(C))
        Mv = np.array(M)

        def f(m):
            r = np.array([zustand(m, kappa, J, a)["E"] for J in J_PUNKTE]) - Mv
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
            "m_am_rand": bool(mb >= M_MAX - 1e-9),
            "gitter": {"m_max": M_MAX, "n": N_GITTER}}


def details(m, kappa, a):
    r2 = zustand(m, kappa, J_PUNKTE[0], a)
    r4 = zustand(m, kappa, J_PUNKTE[1], a)
    s, a0 = sekante(r2["E"], r4["E"])
    out = {"E2": r2["E"], "E4": r4["E"], "v_end2": r2["v"], "v_end4": r4["v"],
           "laenge2": r2["laenge"], "laenge4": r4["laenge"], "s_sekante": s, "a0_sekante": a0,
           "a2": r2["a"], "a4": r4["a"], "eps2": r2["eps"], "eps4": r4["eps"],
           "J_cl2": r2["J_cl"], "J_cl4": r4["J_cl"]}
    if a == VARIANTE:
        out["hoehere_ordnung_2"] = hoehere_ordnung(r2["eps"])
        out["hoehere_ordnung_4"] = hoehere_ordnung(r4["eps"])
    return out


def band(r):
    liste = []
    if r["p"] >= P_MIN and V_BAND[0] <= r["v_end2"] <= V_BAND[1]:
        liste.append("(a) traegt")
    if r["p"] >= P_MIN and r["dchi2_m0"] <= 1.0:
        liste.append("masselos")
    if r["p"] < P_MIN:
        liste.append("traegt nicht")
    if not liste:
        liste.append("uebrig")
    return liste


def ein_fit(datensatz, kappa_name, a_name, lesart):
    kappa = KAPPA[kappa_name]
    a = A_LISTE[a_name] if a_name in A_LISTE else a_name
    t0 = time.perf_counter()
    f = chi2_funktion(datensatz, kappa, a, lesart)
    r = fitte(f)
    r.update(details(r["m"], kappa, a))
    lo, hi = r["m_1sigma"]
    r["v_end2_1sigma"] = [zustand(x, kappa, J_PUNKTE[0], a)["v"] if x is not None else None for x in (lo, hi)]
    r.update({"datensatz": datensatz, "kappa": kappa_name, "steigung": STEIGUNG[kappa_name], "a": a_name,
              "lesart": lesart, "sekunden": time.perf_counter() - t0})
    r["band"] = band(r)
    modell = [k for k, v in MODELL.items() if v == (kappa_name, a_name)]
    r["modell"] = modell[0] if modell else None
    return r


# ---------------------------------------------------------------- Kontrollen
def k1_pq0():
    out = {}
    for name, (kn, an) in (("(I)", MODELL["(I)"]), ("(II)", MODELL["(II)"])):
        k, a = KAPPA[kn], A_LISTE[an]
        geschl = [0.0 if J - a == 0.0 else math.sqrt(2.0 * math.pi * k * (J - a)) for J in J_PUNKTE]
        loeser = {str(m): [zustand(m, k, J, a)["E"] for J in J_PUNKTE] for m in (1e-4, 1e-6, 1e-8)}
        abw_loeser = []
        for x, y in zip(loeser["1e-08"], geschl):
            abw_loeser.append(abs(x - y) if y == 0.0 else abs(x / y - 1.0))
        karte = KARTE_PQ0[name]
        abw_karte = [abs(x - y) for x, y in zip(geschl, karte)]
        out[name] = {"geschlossen": geschl, "loeser": loeser, "abw_loeser_m1e-8": abw_loeser,
                     "karte": karte, "abw_karte_absolut": abw_karte}
    plan = all(max(out[n]["abw_loeser_m1e-8"]) <= TOL_PQ0_LOESER and max(out[n]["abw_karte_absolut"]) <= TOL_PQ0_RUNDUNG
               for n in out)
    wort = all(max(out[n]["abw_karte_absolut"]) <= TOL_PQ0_WORTLAUT for n in out)
    out["PQ0_plan"] = "eingetroffen" if plan else "nicht eingetroffen"
    out["PQ0_wortlaut"] = "eingetroffen" if wort else "nicht eingetroffen"
    return out


def k2_hauptsatz():
    out = {}
    for kn, k in KAPPA.items():
        werte = []
        for eta in np.linspace(0.1, 3.0, 30):
            h = 1e-5
            Ep, Jp, _, _ = EJ(1.0, k, float(eta) + h)
            Em, Jm, _, _ = EJ(1.0, k, float(eta) - h)
            w = EJ(1.0, k, float(eta))[2]
            werte.append(abs((Ep - Em) / (Jp - Jm) / w - 1.0))
        out[kn] = {"max_rel_abweichung_dEdJ_omega": max(werte), "min": min(werte)}
    return out


def k3_jcl_null():
    out = {}
    for m in (0.5, 1.0, 2.5):
        out[str(m)] = {str(j): loese(m, 2.0, j)["E"] - 2.0 * m for j in (1e-6, 1e-10)}
    out["max_abs"] = max(abs(v) for d in out.values() for v in d.values())
    return out


def k4_paar_regge_1():
    out = {}
    for ds, les in (("A", "diag"), ("B", "R3")):
        for an in ("0", "1/12"):
            r = ein_fit(ds, "9/4", an, les)
            soll_m, soll_c = SOLL_PR1[f"{ds}|{an}"]
            out[f"{ds}|{an}"] = {"m": r["m"], "chi2": r["chi2"], "soll_m": soll_m, "soll_chi2": soll_c,
                                 "ok": bool(abs(r["m"] - soll_m) <= 2e-3 and abs(r["chi2"] / soll_c - 1.0) <= 1e-2)}
    out["alle_ok"] = all(v["ok"] for v in out.values() if isinstance(v, dict))
    return out


def k5_schranke():
    ms = np.linspace(0.0, M_MAX, 601)
    out = {}
    for kn, k in KAPPA.items():
        for an in list(A_LISTE) + ([VARIANTE] if kn == "2" else []):
            a = A_LISTE.get(an, an)
            q = []
            for m in ms:
                E2 = zustand(float(m), k, 2.0, a)["E"]
                E4 = zustand(float(m), k, 4.0, a)["E"]
                q.append((E4 * E4 - E2 * E2) / (4.0 * math.pi * k))
            i = int(np.argmin(q))
            out[f"{kn}|{an}"] = {"min_verhaeltnis": float(q[i]), "bei_m": float(ms[i]),
                                 "schranke_haelt": bool(q[i] >= 1.0 - 1e-9)}
    out["C_daten_dM2"] = DATEN["C"]["M"][1] ** 2 - DATEN["C"]["M"][0] ** 2
    out["alle_festen_a_halten"] = all(v["schranke_haelt"] for kk, v in out.items()
                                     if isinstance(v, dict) and not kk.endswith(VARIANTE))
    return out


def k6_variante():
    k = KAPPA["2"]
    out = {"m1e-8": {str(J): zustand(1e-8, k, J, VARIANTE) for J in J_PUNKTE},
           "masselos_I": [0.0, math.sqrt(2.0 * math.pi * k * 2.0)]}
    mono = {}
    for m in (0.5, 1.0, 2.5):
        Jt = [EJ(m, k, float(e))[1] + a_variante(1.0 / math.cosh(float(e))) for e in np.linspace(1e-3, 10.0, 2000)]
        mono[str(m)] = bool(all(Jt[i + 1] > Jt[i] for i in range(len(Jt) - 1)))
    out["J_von_eta_monoton"] = mono
    out["a_bei_eta_0"] = a_variante(1.0)
    out["C1"] = C1
    return out


def budget():
    k = KAPPA["2"]
    t0 = time.perf_counter()
    for i in range(1000):
        zustand(0.05 + 0.005 * i, k, 2.0 + 0.002 * i, 1.0)
    t1 = time.perf_counter()
    for i in range(1000):
        zustand(0.05 + 0.005 * i, k, 2.0 + 0.002 * i, VARIANTE)
    t2 = time.perf_counter()
    return {"s_je_loesung_fest": (t1 - t0) / 1000.0, "s_je_loesung_variante": (t2 - t1) / 1000.0}


def k7_synthetik():
    """Rueckgewinnung ohne Datensicht: Pseudodaten aus dem Modell selbst (m = 1,3), Fehler wie (A)."""
    out, recs = {}, []
    for mo, (kn, an) in MODELL.items():
        k = KAPPA[kn]
        a = A_LISTE.get(an, an)
        m_wahr = 1.3
        E = [zustand(m_wahr, k, J, a)["E"] for J in J_PUNKTE]
        DATEN["S"] = {"quelle": "synthetisch", "M": tuple(E), "dM": (0.022, 0.12)}
        r = ein_fit("S", kn, an, "diag")
        X, Y = kurve(r["m"], k, a)
        out[mo] = {"m_wahr": m_wahr, "m_fit": r["m"], "chi2": r["chi2"], "band": r["band"],
                   "kurve_punkte": int(len(X)), "kurve_J_min": float(Y.min()), "kurve_M2_min": float(X.min())}
        recs.append(r)
    DATEN.pop("S", None)
    return out, recs


def rauch():
    syn, recs = k7_synthetik()
    return {"K1_PQ0": k1_pq0(), "K2_hauptsatz": k2_hauptsatz(), "K3_jcl_null": k3_jcl_null(),
            "K6_variante": k6_variante(), "K7_synthetik": syn, "budget": budget(),
            "fits": [dict(r, datensatz=ds, lesart=les) for ds, les in (("A", "diag"), ("B", "R3"), ("C", "diag"))
                     for r in recs]}


def kontrollen():
    out = rauch()
    out.pop("fits", None)
    out["K4_paar_regge_1"] = k4_paar_regge_1()
    out["K5_schranke"] = k5_schranke()
    return out


# ---------------------------------------------------------------- Fits und Urteile
LESARTEN = (("A", "diag"), ("B", "R3"), ("B", "R1"), ("B", "R2"), ("C", "diag"))


def fits():
    recs = []
    for ds, les in LESARTEN:
        for kn in KAPPA:
            for an in A_LISTE:
                recs.append(ein_fit(ds, kn, an, les))
        recs.append(ein_fit(ds, "2", VARIANTE, les))

    def hole(ds, les, modell):
        kn, an = MODELL[modell]
        return [r for r in recs if r["datensatz"] == ds and r["lesart"] == les and r["kappa"] == kn and r["a"] == an][0]

    pq1 = hole("A", "diag", "(I)")["p"] >= P_MIN
    pq2 = hole("A", "diag", "(II)")["p"] >= P_MIN
    pq3_plan = any(hole("C", "diag", mo)["p"] >= P_MIN for mo in ("(I)", "(II)"))
    pq3_wort = any(hole("C", "diag", mo)["p"] >= P_MIN for mo in ("(I)", "(II)", "(I')"))
    le = {}
    for ds, les in LESARTEN:
        zehn = [r for r in recs if r["datensatz"] == ds and r["lesart"] == les and r["a"] in A_LISTE]
        treffer = [f"{r['kappa']}|{r['a']}" for r in zehn if r["p"] >= P_MIN]
        le[f"{ds}|{les}"] = {"kandidaten": len(zehn), "p_ge_0.05": len(treffer), "treffer": treffer}
    urteile = {"PQ1": "eingetroffen" if pq1 else "nicht eingetroffen",
               "PQ2": "eingetroffen" if pq2 else "nicht eingetroffen",
               "PQ3_plan": "eingetroffen" if pq3_plan else "nicht eingetroffen",
               "PQ3_wortlaut": "eingetroffen" if pq3_wort else "nicht eingetroffen",
               "look_elsewhere": le}
    M_B, C_B = linien_punkte(LINIE_B)
    return {"fits": recs, "urteile": urteile,
            "daten": {"A": DATEN["A"], "C": DATEN["C"], "B": LINIE_B, "B_punkte": M_B, "B_kovarianz": C_B}}


# ---------------------------------------------------------------- Bild
def kurve(m, kappa, a, j_max=6.5):
    """(M^2, J) entlang der Trajektorie mit fester Masse m, ueber ein J-Gitter (robust auch fuer m -> 0)."""
    if a == VARIANTE:
        j_min = 2.0 if m <= 0.0 else a_variante(1.0) + 1e-6
    else:
        j_min = a
    xs, ys = [], []
    if a == VARIANTE and m > 0.0:
        xs.append((2.0 * m) ** 2)
        ys.append(a_variante(1.0))
    for J in np.linspace(j_min, j_max, 260):
        E = zustand(m, kappa, float(J), a)["E"]
        xs.append(E * E)
        ys.append(float(J))
    return np.array(xs), np.array(ys)


def bild(pfad_fits, pfad_png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    d = json.load(open(pfad_fits))
    farbe = {"(I)": "#2a78d6", "(II)": "#eb6834", "(I')": "#1baf7a"}   # dataviz-Standardpalette, Plaetze 1-3
    stil = {"(I)": "-", "(II)": "-", "(I')": "--"}
    ink, ink2, grau, flaeche = "#0b0b0b", "#52514e", "#9a9893", "#fcfcfb"
    fig, axs = plt.subplots(1, 3, figsize=(16.5, 5.9), sharey=True)
    fig.patch.set_facecolor(flaeche)
    x_max = 100.0
    xs = np.linspace(0.0, x_max, 200)
    for ax, ds, les, titel in ((axs[0], "A", "diag", "(A) A&T 2020: 2++ gs, 4++ gs*"),
                               (axs[1], "B", "R3", "(B) MT-Gerade 2004 (Fit in Lesart R3)"),
                               (axs[2], "C", "diag", "(C) A&T 2020: 2++ ex1, 4++ gs*")):
        ax.set_facecolor(flaeche)
        ax.plot(xs, xs / (2.0 * math.pi * 2.0) + 2.0, color=grau, lw=1.4, ls=":", label="(I) masselos: J = M²/(4π) + 2")
        ax.plot(xs, xs / (2.0 * math.pi * 2.25) + 1.0, color=grau, lw=1.4, ls="-.",
                label="(II) masselos: J = M²/(4,5π) + 1")
        if ds in ("A", "C"):
            M = np.array(DATEN[ds]["M"]); dM = np.array(DATEN[ds]["dM"])
            ax.errorbar(M ** 2, J_PUNKTE, xerr=2 * M * dM, fmt="o", ms=8, color=ink, capsize=4,
                        label="Gitter (Fehler in M² = 2 M dM)", zorder=6)
        else:
            L = LINIE_B
            ax.plot(xs, L["a0"] + L["s"] * xs / (2 * math.pi), color=ink2, lw=1.5, label="MT-Gerade 0,281(22), 0,93(24)")
            Mp, C = linien_punkte(L)
            Mp = np.array(Mp)
            ax.errorbar(Mp ** 2, J_PUNKTE, xerr=2 * Mp * np.sqrt(np.diag(C)), fmt="s", ms=8, color=ink, capsize=4,
                        label="Geradenpunkte mit Bandbreite (R1)", zorder=6)
        for r in d["fits"]:
            if r["datensatz"] != ds or r["lesart"] != les or r["modell"] is None:
                continue
            mo = r["modell"]
            a = A_LISTE.get(r["a"], r["a"])
            X, Y = kurve(r["m"], KAPPA[r["kappa"]], a)
            sel = (X <= x_max) & (Y <= 6.5)
            ax.plot(X[sel], Y[sel], color=farbe[mo], lw=2.0, ls=stil[mo],
                    label=f"{mo} bester Fit: m = {r['m']:.3f}, χ² = {r['chi2']:.3g}, p = {r['p']:.2g}")
            ax.plot([r["E2"] ** 2, r["E4"] ** 2], J_PUNKTE, "D", ms=6, color=farbe[mo], zorder=5,
                    markeredgecolor=flaeche, markeredgewidth=1.0)
        ax.set_xlim(0, x_max)
        ax.set_ylim(0, 6.5)
        ax.set_xlabel("M² / σ", color=ink)
        ax.set_title(titel, color=ink, fontsize=11)
        ax.grid(True, color="#e4e3df", lw=0.6)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        ax.legend(loc="upper left", fontsize=7.8, frameon=False)
    axs[0].set_ylabel("J", color=ink)
    fig.suptitle("PAAR-REGGE-2: rotierendes Paar mit Literatur-Intercept, eine freie Endmasse "
                 "(Rauten = Modellwerte bei J = 2, 4)", color=ink, fontsize=12)
    fig.tight_layout()
    fig.savefig(pfad_png, dpi=130, facecolor=fig.get_facecolor())


def main():
    modus = sys.argv[1]
    t0 = time.perf_counter()
    if modus == "rauch":
        out = rauch()
    elif modus == "kontrollen":
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
