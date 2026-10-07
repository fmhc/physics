#!/usr/bin/env python3
"""NACHTRAG 2 (nach der Auswertung, nicht im eingefrorenen Plan, beschreibend): Amplitudenreihe.

Grund: K und E antworten 11- bzw. 21-mal staerker als vorhergesagt und wachsen mit N. Ist die Antwort quadratisch in der
Amplitude (eine echte zweite Ordnung mit groesserem Koeffizienten) oder nicht (Hinweis auf eine Gitterursache)?
Gerechnet mit derselben Vorschrift (kovarianz.verformtes_netz, unveraendert importiert): K mit eps = -0,05 und -0,025,
E mit lam = e^(-0,25). Vorhersagen aus derselben Kontinuumsquadratur (Verformung.dS).
Aufruf (nur ueber kleintest.sh): python nachtrag_amplitude.py <aus.json> <N-Liste> <saat0> <anzahl>
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kovarianz as kv  # noqa: E402
import kugel as k1      # noqa: E402


def main():
    ziel = sys.argv[1]
    Nlist = [int(x) for x in sys.argv[2].split(",")]
    saat0, anzahl = int(sys.argv[3]), int(sys.argv[4])
    V = {"K050": kv.verf_konform(-0.05), "K025": kv.verf_konform(-0.025), "E025": kv.verf_ellipsoid(math.exp(-0.25))}
    out = {"argv": sys.argv[1:], "vorab": {k: {"par": v.par, "dS_einheit": v.dS,
                                                  "y_pred_Q": kv.BETA_Q[0] * v.dS / kv.S0E} for k, v in V.items()},
           "messungen": []}
    for saat in range(saat0, saat0 + anzahl):
        for N in Nlist:
            kn, rr = kv.rundes_netz(N, saat)
            rec = {"N": N, "saat": saat, "rund_Q": rr["Q"]["gamma"], "rund_gueltig": bool(k1.kugel_gueltig(kn["pruefung"], 4)),
                   "F_rund": int(kn["tri"].shape[0])}
            for name, v in V.items():
                r = kv.verformtes_netz(kn, v, N)
                rec[name] = {"gueltig": r["gueltig"], "QI": r["regeln"]["QI"]["gamma"], "anteil_neu": r["info"]["anteil_neu"],
                             "F": r["info"]["F"]}
            out["messungen"].append(rec)
            k1.speichern(ziel, out)
            print(f"N={N} saat={saat}: ok " + " ".join(f"{k} {rec[k]['gueltig']} neu {rec[k]['anteil_neu']:.3f}" for k in V),
                  flush=True)


if __name__ == "__main__":
    main()
