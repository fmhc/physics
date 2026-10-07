"""WOLFRAM-RUHE-1 Hauptlauf R2 (PLAN.md Abschn. 3, 4, 5, 7): WR1 mit E = 5e4, KI mit D = 25, 50, 100 (8 Zufallsreihen-
folgen), Diagnosen (zweiter Anfang, Zufallsreihenfolge), R2-Intervalle (6000, nur Daten; Urteil in auswertung.py).
Aufruf nur ueber kleintest.sh auf der .69: haupt_r2.py <ausgabe.json>"""
import json
import os
import resource
import sys
import time

import numpy as np

import wr_kern as K


def main():
    aus = sys.argv[1]
    t0 = time.time()
    zeiten = {}
    t = time.time()
    e1, s, ch = K.r2_wr1(K.ANFANG_STANDARD, 50000)
    zeiten["wr1_s"] = round(time.time() - t, 2)
    t = time.time()
    ki = K.ki_probe([25, 50, 100], list(range(1, 9)))
    zeiten["ki_s"] = round(time.time() - t, 2)
    t = time.time()
    diag = {"anfang_lhs_standard": K.r2_diagnose(K.ANFANG_LHS, 20000),
            "anfang_standard_zufall_saat1": K.r2_diagnose(K.ANFANG_STANDARD, 20000, zufall_saat=1),
            "anfang_standard_zufall_saat2": K.r2_diagnose(K.ANFANG_STANDARD, 20000, zufall_saat=2)}
    zeiten["diagnose_s"] = round(time.time() - t, 2)
    t = time.time()
    iv = K.r2_intervalle(s, ch, 6000)
    zeiten["intervalle_s"] = round(time.time() - t, 2)
    hier = os.path.dirname(os.path.abspath(__file__))
    out = {
        "lauf": "haupt_r2", "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "skripte_sha256": {f: K.datei_sha(os.path.join(hier, f)) for f in ("haupt_r2.py", "wr_kern.py")},
        "numpy": np.__version__, "zeiten": zeiten, "laufzeit_s": round(time.time() - t0, 2),
        "max_rss_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0, 1),
        "wr1": {"werte": e1}, "ki": ki, "diagnose": diag, "r2_intervalle": iv,
    }
    with open(aus, "w") as fh:
        json.dump(out, fh)
    print(json.dumps({"zeiten": zeiten, "max_rss_mb": out["max_rss_mb"], "E": e1["E"], "G": e1["G"],
                      "D_geo": e1.get("D_geo"), "D_gen": e1["D_gen"], "s_b": e1["s_b"], "ki": ki["urteil"],
                      "intervalle": len(iv["N"])}))


if __name__ == "__main__":
    main()
