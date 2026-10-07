"""WOLFRAM-RUHE-1 Rauchlauf (PLAN.md Abschn. 7): Zeit, Speicher, Programmprobe, WR0 (1500 Intervalle je Kontrolle),
WR1 (E = 2e4), KI (D = 25, 50), Diagnosen. Erzeugt keine R2-Intervalle (keine WR2-Werte).
Aufruf nur ueber kleintest.sh auf der .69: rauch.py <ausgabe.json>"""
import json
import os
import resource
import sys
import time

import numpy as np

import urteile as U
import wr_kern as K


def main():
    aus = sys.argv[1]
    t_anf = time.time()
    zeiten = {}
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 42, 1]))
    t = time.time()
    probe = K.programmprobe(rng, 40)
    zeiten["programmprobe_s"] = round(time.time() - t, 2)
    t = time.time()
    kon = K.kontrollen(rng, 1500)
    zeiten["kontrollen_s"] = round(time.time() - t, 2)
    tabP, maxabw_P = U.bin_tabelle(kon["poisson"], saat=11)
    tabG, maxabw_G = U.bin_tabelle(kon["gitter"], saat=21)
    wr0 = U.urteil_wr0(tabP, tabG, maxabw_G)
    t = time.time()
    e1, s, ch = K.r2_wr1(K.ANFANG_STANDARD, 20000)
    zeiten["wr1_s"] = round(time.time() - t, 2)
    wr1 = U.urteil_wr1(e1)
    t = time.time()
    ki = K.ki_probe([25, 50], list(range(1, 9)))
    zeiten["ki_s"] = round(time.time() - t, 2)
    t = time.time()
    diag = {"anfang_lhs_standard": K.r2_diagnose(K.ANFANG_LHS, 5000),
            "anfang_standard_zufall_saat1": K.r2_diagnose(K.ANFANG_STANDARD, 5000, zufall_saat=1)}
    zeiten["diagnose_s"] = round(time.time() - t, 2)
    zeiten["gesamt_s"] = round(time.time() - t_anf, 2)
    hier = os.path.dirname(os.path.abspath(__file__))
    out = {
        "lauf": "rauch", "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "skripte_sha256": {f: K.datei_sha(os.path.join(hier, f)) for f in ("rauch.py", "wr_kern.py", "urteile.py")},
        "numpy": np.__version__, "zeiten": zeiten,
        "max_rss_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0, 1),
        "programmprobe": {"anzahl": probe["anzahl"], "abweichungen": probe["abweichungen"]},
        "wr0": {"c_gitter": kon["c_gitter"], "c_poisson": kon["c_poisson"], "max_abs_r_minus_x_gitter": maxabw_G,
                "tab_poisson": tabP, "tab_gitter": tabG, "urteil": wr0},
        "wr1": {"werte": e1, "urteil": wr1},
        "ki": ki, "diagnose": diag,
    }
    with open(aus, "w") as fh:
        json.dump(out, fh, indent=1)
    kurz = {"zeiten": zeiten, "max_rss_mb": out["max_rss_mb"], "programmprobe_abw": probe["abweichungen"],
            "wr0": {"plan": wr0["plan"]["urteil"], "karte": wr0["kartenwortlaut"]["urteil"]},
            "wr1": wr1, "D_geo": e1.get("D_geo"), "D_gen": e1["D_gen"], "s_b": e1["s_b"],
            "ev_je_gen_letzt": e1["ereignisse_je_gen_letztes_zehntel"], "marken_hist": e1["marken_hist"],
            "kette": e1["kettenprobe_anteil"], "ki": ki["urteil"]}
    print(json.dumps(kurz))


if __name__ == "__main__":
    main()
