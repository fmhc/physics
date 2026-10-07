#!/usr/bin/env python3
"""AFM-KANAL-1, Diagnose NACH Befund (nicht entscheidend, getrennt markiert): K3 verfehlte woertlich (Translationsmode,
groesstes Residuum am ersten ausgewerteten Punkt r = 3 hp). Diese Datei rechnet die Profile mit afm_kanal.py
(unveraendert importiert) neu und gibt das K3-Residuum getrennt nach Bereichen aus: wie vorab (ab Index 3), ab r >= 0,1,
ab r >= 1, sowie die Residuen der ersten 8 Punkte. Die bindende Auswertung bleibt die vorab festgelegte.
Aufruf: k3diag.py --kappa <k> --h <h> --aus <ordner> --name <name>"""
import argparse
import json
import math
import os
import sys

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import afm_kanal as ak  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kappa", type=str, required=True)
    ap.add_argument("--h", type=str, default="0.02,0.01")
    ap.add_argument("--aus", type=str, default="aus")
    ap.add_argument("--name", type=str, default="k3diag")
    a = ap.parse_args()
    kaps = [float(x) for x in a.kappa.split(",")]
    zeilen = [f"k3diag.py ({a.name}) Start {ak.jetzt()}", "Argumente: " + json.dumps(vars(a)),
              "kappa | f | h | K3_transl ab i=3 (wie vorab) | ab r>=0,1 | ab r>=1 | Ort max (ab i=3) | erste 8 Punkte | "
              "K3_phase ab i=3 | ab r>=0,1"]
    erg = {"argumente": vars(a), "zeilen": []}
    for h in [float(x) for x in a.h.split(",")]:
        prot = []
        paare = [(k, f) for k in kaps for f in ak.FS]
        prs = ak.afm_profile([p[0] for p in paare], [p[1] for p in paare], h, prot)
        hp = 0.5 * h
        for p in prs:
            if not p.get("gueltig"):
                zeilen.append(f"{p['kappa']} | {p['f']} | {h} | ungueltig")
                continue
            r = p["_r"]
            th = p["_th"]
            a1 = 1.0 - p["Omega2"]
            dth = ak.d1_fd4(th, hp, gerade=True)
            Vu, Vv = ak.V_uv(th, dth, a1, p["kappa"])
            J = len(r) - 1
            Y = r * np.sin(th)
            Z = r * dth
            Ypp = ak.d2_fd4(Y, hp, gerade=False)
            Zpp = ak.d2_fd4(Z, hp, gerade=True)
            i = np.arange(3, J - 2)
            rv = np.abs((-Ypp[i] + Vv[i] * Y[i]) / r[i]) / np.max(np.abs(np.sin(th)))
            ru = np.abs((-Zpp[i] + (2.0 / r[i] ** 2) * Z[i] + Vu[i] * Z[i]) / r[i]) / np.max(np.abs(dth))
            m01 = r[i] >= 0.1
            m1 = r[i] >= 1.0
            d = {"kappa": p["kappa"], "f": p["f"], "h": h, "K3_transl_ab3": float(ru.max()),
                 "K3_transl_ab_r0.1": float(ru[m01].max()), "K3_transl_ab_r1": float(ru[m1].max()),
                 "ort_max": float(r[i][int(np.argmax(ru))]), "erste8": [float(x) for x in ru[:8]],
                 "K3_phase_ab3": float(rv.max()), "K3_phase_ab_r0.1": float(rv[m01].max()),
                 "K3_transl_vorab": p["K3_transl"]}
            erg["zeilen"].append(d)
            zeilen.append(f"{p['kappa']} | {p['f']} | {h} | {d['K3_transl_ab3']:.2e} | {d['K3_transl_ab_r0.1']:.2e} | "
                          f"{d['K3_transl_ab_r1']:.2e} | {d['ort_max']:.3f} | "
                          + ", ".join(f"{x:.1e}" for x in d["erste8"]) + f" | {d['K3_phase_ab3']:.1e} | "
                          f"{d['K3_phase_ab_r0.1']:.1e}")
    zeilen.append(f"Ende {ak.jetzt()}")
    os.makedirs(a.aus, exist_ok=True)
    with open(os.path.join(a.aus, f"{a.name}.txt"), "w") as fh:
        fh.write("\n".join(zeilen) + "\n")
    with open(os.path.join(a.aus, f"{a.name}.json"), "w") as fh:
        json.dump(ak.jsonfest(erg), fh, indent=1)
    print("\n".join(zeilen))


if __name__ == "__main__":
    main()
