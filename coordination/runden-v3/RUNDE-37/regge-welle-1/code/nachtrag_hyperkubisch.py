#!/usr/bin/env python3
"""REGGE-WELLE-1, Nachtrag (nach dem Hauptlauf, beschreibend, nicht geurteilt; ERGEBNIS Abschnitt 4).

1. Vergleich der gerechneten Lichtkegel-Nullstellen mit der Dispersion des einfachen hyperkubischen Wellengitters
   sum_mu 4 sin^2(k_mu/2) = 0, fortgesetzt: sinh^2(omega/2) = sum_i sin^2(k_i/2)  [H, nach Sichtung der Zahlen].
   Dazu die Kontinuumsentwicklung v = 1 - (1 + sum n_i^4) k^2/24.
2. Kartenwortlaut-Bild (A9): Wie viele der 10 nicht trivialen Eigenwerte der unreduzierten M (s = l^2) fallen am
   Lichtkegel auf nahe null?

Aufruf: python nachtrag_hyperkubisch.py <haupt.json> <nachtrag.json> <bildordner>
"""
import json
import sys

import numpy as np


def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    zeilen = []
    for p in d["punkte"]:
        n = np.array(p["n"])
        kb = p["betrag"]
        k = kb * n
        x = np.sqrt(np.sum(np.sin(k / 2) ** 2))
        om_hk = 2 * np.arcsinh(x)
        v_hk = om_hk / kb
        v_k2 = 1 - (1 + np.sum(n ** 4)) * kb ** 2 / 24
        vs = [z["v_re"] for z in p["nullstellen"]]
        zeilen.append({"richtung": p["richtung"], "betrag": kb, "v": vs, "v_hyperkubisch": float(v_hk),
                       "v_k2_naeherung": float(v_k2),
                       "abw_hk_max": float(max(abs(v - v_hk) for v in vs)),
                       "abw_hk_rel_zu_1mv": float(max(abs(v - v_hk) for v in vs) / max(abs(1 - v_hk), 1e-300)),
                       "abw_k2_max": float(max(abs(v - v_k2) for v in vs))})
    je_betrag = {}
    for kb in sorted(set(z["betrag"] for z in zeilen)):
        zz = [z for z in zeilen if z["betrag"] == kb]
        je_betrag[str(kb)] = {"abw_hk_max": max(z["abw_hk_max"] for z in zz),
                              "abw_hk_rel_zu_1mv_max": max(z["abw_hk_rel_zu_1mv"] for z in zz),
                              "abw_k2_max": max(z["abw_k2_max"] for z in zz),
                              "1_minus_v_min": min(1 - min(z["v"]) for z in zz),
                              "1_minus_v_max": max(1 - min(z["v"]) for z in zz)}
    # A9: Eigenwerte der unreduzierten M auf der reellen Achse
    a9 = []
    for p in d["punkte"]:
        if "eigen_M" not in p:
            continue
        om = np.array(p["eigen_M"]["omega"]) / p["betrag"]
        e = np.array(p["eigen_M"]["betrag_rel_sortiert"])
        fern = np.abs(om - 1) > 0.3
        nah = np.abs(om - 1) <= 0.05
        tief = []
        for q in range(5, 15):
            ref = np.median(e[fern, q])
            tief.append(float(np.min(e[nah, q]) / ref))
        a9.append({"richtung": p["richtung"], "betrag": p["betrag"],
                   "null5_max": float(np.max(e[:, :5])), "einbruch_min_durch_median": tief,
                   "zahl_einbrueche_unter_1e-2": int(sum(t < 1e-2 for t in tief))})
    out = {"hinweis": "Nachtrag nach dem Hauptlauf, beschreibend, nicht geurteilt", "zeilen": zeilen,
           "je_betrag": je_betrag, "a9_eigenwerte_M": a9}
    with open(sys.argv[2], "w") as f:
        json.dump(out, f, indent=1)
    for kb, v in je_betrag.items():
        print(kb, json.dumps(v))
    print("A9 Einbrueche:", sorted(set(z["zahl_einbrueche_unter_1e-2"] for z in a9)))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))
    namen = []
    for z in zeilen:
        if z["richtung"] not in namen:
            namen.append(z["richtung"])
    for r in namen:
        zz = sorted([z for z in zeilen if z["richtung"] == r], key=lambda z: z["betrag"])
        b = [z["betrag"] for z in zz]
        axs[0].loglog(b, [1 - min(z["v"]) for z in zz], "-o", ms=3, lw=0.8)
        axs[1].loglog(b, [max(z["abw_hk_max"], 1e-17) for z in zz], "-o", ms=3, lw=0.8)
    axs[0].set_title("1 - v (v = Re omega/|k|), alle 24 Richtungen")
    axs[0].set_xlabel("|k|")
    axs[1].set_title("|v - v_hyperkubisch|, v_hk aus sinh^2(omega/2) = sum sin^2(k_i/2)")
    axs[1].set_xlabel("|k|")
    fig.tight_layout()
    fig.savefig(f"{sys.argv[3]}/bild-dispersion-hyperkubisch.png", dpi=110)
    print("Bild geschrieben")


if __name__ == "__main__":
    main()
