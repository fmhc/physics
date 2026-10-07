#!/usr/bin/env python3
"""NACHTRAG (nach der Auswertung, nicht im eingefrorenen Plan, beschreibend): Nullproben MIT Neuvernetzung.

Grund: Die Kontrollen des Plans decken nur Faelle ohne Neuvernetzung ab (sigma = 0, Moebius exakt). K und E werden zu
53 bis 62 % neu vernetzt und zeigen eine mit N wachsende Antwort. Diese Proben trennen "Neuvernetzung/Paarung" von
"nicht-Moebius-sigma".
  D-B: sigma = 0. Punkte vorher mit einer massstreuen, nicht isometrischen Faserdrehung R verschoben (Drehung der
       S^3-Faser in der (w1, w2)-Ebene um kappa * theta): wieder gleichverteilt, aber neu vernetzt. Erwartung
       E[Delta Gamma] = 0 exakt (beide Punktmengen gleichverteilt, gleiche Vorschrift).
  D-A: Moebius-sigma wie M, Punkte erst mit R, dann mit dem Moebius-Transport. Erwartung wie M (Delta S = 0).
kovarianz.py, kugel.py und kugel2.py werden unveraendert importiert.
Aufruf (nur ueber kleintest.sh): python nachtrag_drehung.py <aus.json> <N-Liste> <saat0> <anzahl> <kappa>
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kovarianz as kv  # noqa: E402
import kugel as k1      # noqa: E402


def drehe(P, kappa):
    th, w = kv.theta_w(P)
    al = kappa * th
    c, s = np.cos(al), np.sin(al)
    w2 = w.copy()
    w2[:, 0] = c * w[:, 0] - s * w[:, 1]
    w2[:, 1] = s * w[:, 0] + c * w[:, 1]
    a = float(np.linalg.norm(P[0]))
    return a * np.concatenate([np.sin(th)[:, None] * w2, np.cos(th)[:, None]], axis=1)


def main():
    ziel = sys.argv[1]
    Nlist = [int(x) for x in sys.argv[2].split(",")]
    saat0, anzahl, kappa = int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    th = kv.gitter()
    v0 = kv.Verformung("0", th, np.zeros_like(th), np.zeros_like(th), {})
    vM = kv.verf_moebius(kv.T_M)
    out = {"kappa": kappa, "argv": sys.argv[1:], "messungen": []}
    for saat in range(saat0, saat0 + anzahl):
        for N in Nlist:
            kn, rr = kv.rundes_netz(N, saat)
            kn2 = dict(kn)
            kn2["P"] = drehe(kn["P"], kappa)
            rec = {"N": N, "saat": saat, "rund_Q": rr["Q"]["gamma"], "rund_C_korr": rr["C"]["gamma"] + rr["C"]["korr"],
                   "rund_gueltig": bool(k1.kugel_gueltig(kn["pruefung"], 4))}
            for name, v in (("B", v0), ("A", vM)):
                r = kv.verformtes_netz(kn2, v, N)
                rec[name] = {"gueltig": r["gueltig"], "QI": r["regeln"]["QI"]["gamma"],
                             "CI_korr": r["regeln"]["CI"]["gamma"] + r["regeln"]["CI"]["korr"],
                             "anteil_neu": r["info"]["anteil_neu"], "F": r["info"]["F"]}
            rec["F_rund"] = int(kn["tri"].shape[0])
            out["messungen"].append(rec)
            k1.speichern(ziel, out)
            print(f"N={N} saat={saat}: ok {rec['B']['gueltig']} {rec['A']['gueltig']} neu B {rec['B']['anteil_neu']:.3f} "
                  f"A {rec['A']['anteil_neu']:.3f}", flush=True)


if __name__ == "__main__":
    main()
