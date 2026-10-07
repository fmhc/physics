"""WOLFRAM-RUHE-1 Auswertung (PLAN.md Abschn. 6): Urteile WR0 bis WR2 je Plan und Kartenwortlaut, KI, Bild r(eta).
Aufruf nur ueber kleintest.sh auf der .69:
    auswertung.py <haupt_kontrollen.json> <haupt_r2.json> <auswertung.json> <bild.png>"""
import json
import math
import os
import sys
import time

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import urteile as U  # noqa: E402
import wr_kern as K  # noqa: E402


def main():
    kj, rj, aus, bild = sys.argv[1:5]
    with open(kj) as fh:
        KJ = json.load(fh)
    with open(rj) as fh:
        RJ = json.load(fh)
    kon = KJ["kontrollen"]
    tabP, maxabw_P = U.bin_tabelle(kon["poisson"], saat=11)
    tabG, maxabw_G = U.bin_tabelle(kon["gitter"], saat=21)
    wr0 = U.urteil_wr0(tabP, tabG, maxabw_G)
    e1 = RJ["wr1"]["werte"]
    wr1 = U.urteil_wr1(e1)
    c_R2 = e1["c_R2"]
    iv = RJ["r2_intervalle"]
    c_def = c_R2 is not None and c_R2 == c_R2 and c_R2 > 0
    if c_def and iv["N"]:
        iv_x = dict(iv)
        iv_x["x"] = [K.x_wert(c_R2, dT, N) for dT, N in zip(iv["dT"], iv["N"])]
        tabR, _ = U.bin_tabelle(iv_x, saat=31)
    else:
        tabR = None
    wr2_plan = U.urteil_wr2(tabR, tabG, c_R2 if c_def else None, wr1["plan"] == "eingetroffen")
    wr2_karte = U.urteil_wr2(tabR, tabG, c_R2 if c_def else None, wr1["kartenwortlaut"] == "eingetroffen")
    # Kettenprobe an den R2-Intervallen (Diagnose, kein WR2-Urteil)
    N = np.asarray(iv["N"], float)
    L = np.asarray(iv["L"], float)
    ketten = {"anzahl": int(len(N)), "anteil_L_gleich_N": float(np.mean(L == N)) if len(N) else None,
              "je_N_bin": []}
    for lo, hi in U.N_BINS:
        m = (N >= lo) & (N < hi)
        if m.any():
            r = L[m] / (2.0 * np.sqrt(N[m]))
            ketten["je_N_bin"].append({"bin": [lo, hi - 1 if hi == 2001 else hi], "anzahl": int(m.sum()),
                                       "median_r": float(np.median(r)),
                                       "median_sqrtN_halbe": float(np.median(np.sqrt(N[m]) / 2.0))})
    out = {
        "lauf": "auswertung", "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "eingaben": {"kontrollen": os.path.basename(kj), "r2": os.path.basename(rj),
                     "kontrollen_sha256": K.datei_sha(kj), "r2_sha256": K.datei_sha(rj)},
        "skripte_sha256": {f: K.datei_sha(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))
                           for f in ("auswertung.py", "urteile.py", "wr_kern.py")},
        "WR0": {"urteil": wr0, "c_gitter": kon["c_gitter"], "c_poisson": kon["c_poisson"],
                "max_abs_r_minus_x_gitter": maxabw_G, "programmprobe_abweichungen": KJ["programmprobe"]["abweichungen"],
                "tab_poisson": tabP, "tab_gitter": tabG},
        "WR1": {"urteil": wr1, "kennzahlen": {k: e1[k] for k in (
            "E", "G", "anzahl_starts", "t_g", "D_geo", "D_geo_fenster", "D_geo_lokal", "D_gen", "s_b",
            "ereignisse_je_gen_letztes_zehntel", "ereignisse_je_gen_max", "ereignisse_je_gen_hist", "marken_hist",
            "marken_letzt", "halt", "kettenprobe_anteil", "ausgrad_max", "eingrad_max", "c_R2", "c_R2_koeff")}},
        "WR2": {"plan": wr2_plan, "kartenwortlaut": wr2_karte, "tab_r2": tabR},
        "KI": RJ["ki"], "diagnose": RJ["diagnose"], "r2_intervalle_kettenprobe": ketten,
        "laufzeiten": {"kontrollen_s": KJ["laufzeit_s"], "r2_s": RJ["laufzeit_s"]},
        "max_rss_mb": {"kontrollen": KJ["max_rss_mb"], "r2": RJ["max_rss_mb"]},
    }
    with open(aus, "w") as fh:
        json.dump(out, fh, indent=1)
    # Bild
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.8))
    mitten = [0.5 * (a + b) for a, b in zip(U.ETA_BINS[:-1], U.ETA_BINS[1:])]
    eta_f = np.linspace(0, 2, 100)
    ax[0].plot(eta_f, np.cosh(eta_f), "k-", lw=1, label="cosh(eta)")
    ax[0].axhline(1.0, color="0.6", lw=0.8)
    stile = {"poisson": ("tab:blue", tabP), "gitter": ("tab:orange", tabG)}
    for name, (farbe, tab) in stile.items():
        for k, mk in ((-2, "s"), (-1, "o")):
            z = tab[k]
            xs = [m for m, e in zip(mitten, z["eta_bins"]) if e["median_r"] is not None]
            ys = [e["median_r"] for e in z["eta_bins"] if e["median_r"] is not None]
            lo = [e["median_r"] - e["q16_r"] for e in z["eta_bins"] if e["median_r"] is not None]
            hi = [e["q84_r"] - e["median_r"] for e in z["eta_bins"] if e["median_r"] is not None]
            ax[0].errorbar(xs, ys, yerr=[lo, hi], fmt=mk + "-", color=farbe, ms=4, lw=1, capsize=2,
                           label="%s N %d-%d" % (name, z["bin"][0], z["bin"][1]))
    if tabR is not None:
        for k, mk in ((-2, "s"), (-1, "o")):
            z = tabR[k]
            xs = [m for m, e in zip(mitten, z["eta_bins"]) if e["median_r"] is not None]
            ys = [e["median_r"] for e in z["eta_bins"] if e["median_r"] is not None]
            ax[0].plot(xs, ys, mk + "-", color="tab:red", ms=4, label="R2 N %d-%d" % (z["bin"][0], z["bin"][1]))
    else:
        ax[0].text(0.05, 3.3, "R2: eta nicht definiert (c^2 <= 0, Kette)", color="tab:red", fontsize=9)
    ax[0].set_xlabel("Schraegstellung eta (Programm-eta, Bin-Mitte)")
    ax[0].set_ylabel("r = L / (2 sqrt N), Median (16-84 %)")
    ax[0].set_ylim(0.8, 3.8)
    ax[0].legend(fontsize=7, loc="upper left", bbox_to_anchor=(0.0, 0.92))
    ax[0].set_title("r(eta): Kontrollen (WR0)")
    # rechts: r gegen N
    nm = [math.sqrt(lo * min(hi, 2000)) for lo, hi in U.N_BINS]
    for name, (farbe, tab) in stile.items():
        ax[1].plot(nm, [z["median_r"][0] for z in tab], "o-", color=farbe, label=name + " (alle eta)")
    if ketten["je_N_bin"]:
        ax[1].plot([math.sqrt(z["bin"][0] * z["bin"][1]) for z in ketten["je_N_bin"]],
                   [z["median_r"] for z in ketten["je_N_bin"]], "^-", color="tab:red", label="R2 (Standard)")
    nf = np.geomspace(50, 2000, 100)
    ax[1].plot(nf, np.sqrt(nf) / 2.0, "k--", lw=1, label="Kette: sqrt(N)/2")
    ax[1].set_xscale("log")
    ax[1].set_yscale("log")
    ax[1].set_xlabel("N (Elemente im Intervall, mit Endpunkten)")
    ax[1].set_ylabel("Median r")
    ax[1].legend(fontsize=8)
    ax[1].set_title("r gegen N: R2 ist eine Kette")
    fig.suptitle("WOLFRAM-RUHE-1: R2 = {{x,y,y},{x,z,u}} -> {{u,v,v},{v,z,y},{x,y,v}} (TI S. 283-284)", fontsize=10)
    fig.tight_layout()
    fig.savefig(bild, dpi=120)
    print(json.dumps({"WR0": [wr0["plan"]["urteil"], wr0["kartenwortlaut"]["urteil"]],
                      "WR1": [wr1["plan"], wr1["kartenwortlaut"]],
                      "WR2": [wr2_plan["urteil"], wr2_karte["urteil"]], "KI": RJ["ki"]["urteil"]}))


if __name__ == "__main__":
    main()
