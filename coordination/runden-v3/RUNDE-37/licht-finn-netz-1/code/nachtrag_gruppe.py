#!/usr/bin/env python3
"""LICHT-FINN-NETZ-1, Nachtrag nach Zusatz der Leitung (22:1x): Phase gegen Gruppe, Schranke in der Konvention der
LHAASO-Arbeit (RUNDE-34/grb-221009a/quellen/lhaaso-2402.06009.txt). Beschreibend, ohne Urteil. Liest die eingefroren
erzeugte Datei lauf/ergebnis.json und aendert sie nicht; der eingefrorene Code bleibt unberuehrt.

Quelle: Gl. (1) E^2 ~ p^2 c^2 [1 - s (E/E_QG,n)^n]  ->  Phasentempo E/p = c [1 - (s/2) (E/E_QG,n)^n]
        Gl. (2) v = dE/dp ~ c [1 - s (n+1)/2 (E/E_QG,n)^n]  (Gruppentempo; n = 2: Faktor 3/2)
Netz:   omega/k   = c (1 + a1 k + a2 k^2 + a3 k^3 + a4 k^4 + ...)          (Phasentempo, k in 1/PU)
        domega/dk = c (1 + 2 a1 k + 3 a2 k^2 + 4 a3 k^3 + 5 a4 k^4 + ...)  (Gruppentempo)
Mit E = hbar omega, p = hbar k, k l = E l/(hbar c) in fuehrender Ordnung:
  Phase:  a2 (E l/hbar c)^2 = -(s/2)(E/E_QG,2)^2          ->  l = hbar c / (E_QG,2 sqrt(2 |a2|))
  Gruppe: 3 a2 (E l/hbar c)^2 = -s (3/2)(E/E_QG,2)^2      ->  l = hbar c sqrt(3/2 / (3 |a2|)) / E_QG,2  (gleich)
Falsch zugeordnet (nur zur Pruefung): a2 als Gruppenkoeffizient gelesen -> l * sqrt3; 3 a2 als Phasenkoeffizient
gelesen -> l / sqrt3.

Aufruf (nur ueber kleintest.sh): python nachtrag_gruppe.py <ergebnis.json> <aus.json>
"""
import json
import math
import sys

HBARC = 1.973269804e-16      # GeV m
L_P = 1.616255e-35           # m
E_QG2 = {"sub": 6.9e11, "sup": 7.0e11}    # LHAASO Z. 469-471 (Tabelle Z. 446)
E_QG1 = {"sub": 1.0e20, "sup": 1.1e20}    # LHAASO Z. 466-468
NULL_A2 = 1e-6               # abs(a2) darunter gilt als null (Grover laengs der Achsen): keine Schranke


def l_phase(a2, E):
    return HBARC / (E * math.sqrt(2.0 * abs(a2)))


def l_gruppe(a2, E):
    return HBARC * math.sqrt(1.5 / (3.0 * abs(a2))) / E


def zusammen(w):
    if not w:
        return None
    m = sum(w) / len(w)
    return {"mittel": m, "min": min(w), "max": max(w)}


def schranke(abs_a2, s):
    E = E_QG2[s]
    lp, lg = l_phase(abs_a2, E), l_gruppe(abs_a2, E)
    return {"abs_a2_phase": abs_a2, "abs_g2_gruppe": 3.0 * abs_a2, "E_QG2_GeV": E, "l_phase_m": lp, "l_gruppe_m": lg,
            "rel_abw_phase_gruppe": abs(lp - lg) / lp, "l_durch_lP": lg / L_P,
            "falsch_a2_als_gruppe_m": lg * math.sqrt(3.0), "falsch_3a2_als_phase_m": lg / math.sqrt(3.0)}


def main(pfad, aus):
    d = json.load(open(pfad))
    out = {"quelle": "lhaaso-2402.06009.txt Gl. (1) Z. ~165-172, Gl. (2) Z. 141-147, Grenzen Z. 466-471, Tabelle Z. 446",
           "operatoren": {}}
    for name in d["finn_operatoren"]:
        erg = d["operatoren"][name]
        if "fehler" in erg:
            continue
        zweige = []
        for zz in erg["fenster"]["W0"]:
            je = [e for e in zz["je_richtung"] if not e.get("flach") and e.get("a2") is not None]
            if not je:
                zweige.append(None)
                continue
            g1 = [2.0 * e["a1"] for e in je]
            g2 = [3.0 * e["a2"] for e in je]
            g4 = [5.0 * e["a4"] for e in je]
            a2 = [e["a2"] for e in je]
            neg = [abs(v) for v in a2 if v < 0 and abs(v) >= NULL_A2]
            z = {"g2_gruppe": zusammen(g2), "g4_gruppe": zusammen(g4), "g1_gruppe_max_abs": max(abs(v) for v in g1),
                 "a2_phase": zusammen(a2), "richtungen": len(je),
                 "richtungen_a2_null": sum(1 for v in a2 if abs(v) < NULL_A2),
                 "richtungen_a2_positiv": sum(1 for v in a2 if v >= NULL_A2)}
            if neg:
                s = "sub"
                z["schranke"] = {"konservativ": schranke(min(neg), s), "mittel": schranke(abs(sum(a2) / len(a2)), s),
                                 "streng": schranke(max(neg), s)}
            g1max = max(abs(v) for v in g1)
            if g1max > 1e-8:
                a1max = g1max / 2.0
                # Gl. (2) mit n = 1: 2 a1 (E l/hbar c) = -s (E/E_QG,1)  ->  l = hbar c / (2 |a1| E_QG,1)
                z["linear"] = {"abs_a1_phase": a1max, "abs_g1_gruppe": g1max,
                               "l_m_sub": HBARC / (2.0 * a1max * E_QG1["sub"]),
                               "l_m_sup": HBARC / (2.0 * a1max * E_QG1["sup"])}
            zweige.append(z)
        out["operatoren"][name] = zweige
    # WEYL-LINEAR-1 / STRICH-NETZ-1: kappa = 0,117 ist Phasenkoeffizient (strichnetz.py Z. 787: v = E_zentrum / k)
    out["weyl_linear_1"] = {"kappa_phase": 0.117, "richtig_m": l_phase(0.117, E_QG2["sub"]),
                            "gruppe_route_m": l_gruppe(0.117, E_QG2["sub"]),
                            "falls_kappa_als_gruppe_gelesen_m": l_gruppe(0.117, E_QG2["sub"]) * math.sqrt(3.0)}
    with open(aus, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"nachtrag -> {aus}", flush=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
