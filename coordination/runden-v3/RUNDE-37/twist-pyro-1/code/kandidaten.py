#!/usr/bin/env python3
"""TWIST-PYRO-1, Vorlauf vor dem Einfrieren: Generizitaet von Projektionskandidaten fuer P3 (nur Entartungs- und
Unklar-Zaehler, keine Messgroesse). Auswahlregel (PLAN.md 7): der erste Kandidat der Liste, der auf allen drei Netzen
0 Entartungen und 0 unklare Kreuzungen hat.
Aufruf: python kandidaten.py <ausgabe.json>
"""
import sys
import json
import twist_pyro as tp

KAND = [(5, 9, 17), (3, 8, 14), (6, 11, 19), (2, 9, 13), (7, 4, 15)]


def main():
    aus = sys.argv[1]
    erg = []
    netze = [tp.Netz("kubisch", 3), tp.Netz("diamant", 2), tp.Netz("pyro", 1)]
    schl = {N.art: N.schleifen() for N in netze}
    for d in KAND:
        M = ((d[1], -d[0], 0), (d[2], 0, -d[0]))
        r = {"kern": list(d), "M": [list(M[0]), list(M[1])]}
        for N in netze:
            z = {"ent_schnitt": 0, "unklar": 0, "fern": 0, "nah": 0, "torus_zusammenfall": 0, "unklar_beispiele": []}
            ek = tp.knoten_entartung(N, M)
            for s in schl[N.art]:
                tp.drehung(N, M, s["knoten"], True, tp.DELTA_P, z)
            for (ti, hi) in N.links:
                u = N.sites[ti]
                w = [tp.add(u, b) for b in N.bonds(u) if N.idx[N.mod(tp.add(u, b))] == hi][0]
                tp.drehung(N, M, [u, w], False, tp.DELTA_H, z)
                tp.drehung(N, M, [u, w], False, tp.DELTA_P, z)
            r[N.art] = {"ent_knoten": ek, "ent_schnitt": z["ent_schnitt"], "unklar": z["unklar"]}
        r["generisch"] = all(r[N.art]["ent_knoten"] == 0 and r[N.art]["ent_schnitt"] == 0 and r[N.art]["unklar"] == 0
                             for N in netze)
        erg.append(r)
        print(json.dumps(r))
    with open(aus, "w") as fh:
        json.dump(erg, fh, indent=1)


if __name__ == "__main__":
    main()
