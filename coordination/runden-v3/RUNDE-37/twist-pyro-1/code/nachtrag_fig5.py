#!/usr/bin/env python3
"""TWIST-PYRO-1, Nachtrag nach dem Einfrieren (eingefrorener Code unveraendert, nur importiert).
Grund: PLAN.md 0 und 1.4 enthalten drei Schreibtisch-Aussagen, die der Hauptlauf nicht einzeln ausweist:
  (a) Fig. 5: Drehmenge der xz-Plakette = 8 Kanten (oben, links, +y unten links, -y oben rechts, 4 Beine oben links)
  (b) Gl. (11)/Fig. 6: Drehmengen der Huepfer auf x-, y-, z-Kante
  (c) Gegenbeispiel: p (xz, y=0) und r' (yz, x=1, y=-1..0) antivertauschen in Lesart V, vertauschen in Lesart S
Erwartungen stehen unten fest im Skript (aus PLAN.md, vor diesem Lauf). Kubisch L = 4, Projektion P1.
Aufruf: python nachtrag_fig5.py <ausgabe.json>
"""
import sys
import json
import twist_pyro as tp


def kanten(N, paare):
    return sum(1 << N.kante_id(u, w) for (u, w) in paare)


def namen(N, bits):
    out = []
    for l, (ti, hi) in enumerate(N.links):
        if bits >> l & 1:
            out.append([list(N.sites[ti]), list(N.sites[hi])])
    return sorted(out)


def main():
    aus = sys.argv[1]
    N = tp.Netz("kubisch", 4)
    M = tp.PROJ["P1"]
    z = {"ent_schnitt": 0, "unklar": 0, "fern": 0, "nah": 0, "torus_zusammenfall": 0, "unklar_beispiele": []}
    o = (0, 0, 0)
    ex, ey, ez = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    A, B, C, D = o, ex, (1, 0, 1), ez            # p: unten links, unten rechts, oben rechts, oben links
    p = [A, B, C, D]
    soll_p = kanten(N, [(D, C), (A, D), (A, tp.add(A, ey)), (C, tp.sub3(C, ey)), (D, tp.sub3(D, ey)),
                        (D, tp.sub3(D, ex)), (D, tp.add(D, ez)), (D, tp.add(D, ey))])
    pS, pV = tp.drehung(N, M, p, True, tp.DELTA_P, z)
    r = [(1, -1, 0), (1, 0, 0), (1, 0, 1), (1, -1, 1)]
    rS, rV = tp.drehung(N, M, r, True, tp.DELTA_P, z)
    Xp = kanten(N, [(p[i], p[(i + 1) % 4]) for i in range(4)])
    Xr = kanten(N, [(r[i], r[(i + 1) % 4]) for i in range(4)])
    erg = {"fig5": {"soll": namen(N, soll_p), "S": namen(N, pS), "V": namen(N, pV),
                    "S_gleich_soll": pS == soll_p, "V_gleich_soll": pV == soll_p}}
    huepfer = {"x": (o, ex, [(ex, tp.sub3(ex, ez)), (ex, tp.sub3(ex, ey))]),
               "y": (o, ey, [(o, ex), (ey, tp.sub3(ey, ez))]),
               "z": (o, ez, [(o, ex), (o, ey)])}
    erg["gl11"] = {}
    for name, (u, w, soll) in huepfer.items():
        hS, hV = tp.drehung(N, M, [u, w], False, tp.DELTA_H, z)
        s = kanten(N, soll)
        erg["gl11"][name] = {"soll": namen(N, s), "S": namen(N, hS), "V": namen(N, hV), "S_gleich_soll": hS == s,
                             "V_gleich_soll": hV == s}
    erg["gegenbeispiel"] = {"p": [list(v) for v in p], "r_strich": [list(v) for v in r],
                            "s_S": tp.sym(Xp, pS, Xr, rS), "s_V": tp.sym(Xp, pV, Xr, rV),
                            "erwartet": {"s_S": 0, "s_V": 1},
                            "T_S_r": namen(N, rS), "T_V_r": namen(N, rV)}
    erg["zaehler"] = {k: v for k, v in z.items() if k != "unklar_beispiele"}
    with open(aus, "w") as fh:
        json.dump(erg, fh, indent=1)
    print(json.dumps({"fig5_S": erg["fig5"]["S_gleich_soll"], "fig5_V": erg["fig5"]["V_gleich_soll"],
                      "gl11_S": {k: v["S_gleich_soll"] for k, v in erg["gl11"].items()},
                      "gegenbeispiel_s_S": erg["gegenbeispiel"]["s_S"], "gegenbeispiel_s_V": erg["gegenbeispiel"]["s_V"],
                      "zaehler": erg["zaehler"]}))


if __name__ == "__main__":
    main()
