# FLUSS-1 (Runde 34): Bild der Ringform (nur Darstellung, nach den Laeufen geschrieben, keine Urteile).
# Aufruf: bild_ringe.py <auswertung.json> <ausgabe.png> <L_haupt> <L_kontrolle>
import sys, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

d = json.load(open(sys.argv[1])); aus = sys.argv[2]; LH = sys.argv[3]; LK = sys.argv[4]
fig, axs = plt.subplots(1, 2, figsize=(9, 3.6))
for L, mk in ((LH, "o"), (LK, "s")):
    k = d["korr_A"].get(L)
    if not k:
        continue
    rg = k["ringe"]["D"]
    r = np.array(rg["r"]); y = np.array([np.nan if v is None else v for v in rg["y"]]); s = np.array(rg["s"])
    axs[0].errorbar(r, y, s, fmt=mk, ms=4, label="A L=%s D (Ringe)" % L)
    a = rg["ausgleich"]
    if "potenz" in a and L == LH:
        xx = np.linspace(min(a["ringe_r"]), max(a["ringe_r"]), 50)
        X = np.log(a["ringe_r"]); Y = np.log(a["ringe_y"])
        c = np.polyfit(X, Y, 1); axs[0].plot(xx, np.exp(np.polyval(c, np.log(xx))), "k-", lw=1,
                                             label="Potenz p=%.2f" % a["potenz"]["p"])
        c2 = np.polyfit(a["ringe_r"], Y, 1); axs[0].plot(xx, np.exp(np.polyval(c2, xx)), "k:", lw=1,
                                                         label="exp xi=%.2f" % a["exponentiell"]["xi"])
    g = k.get("gauss_referenz_D", {}).get("ringform")
    if g and L == LH:
        axs[0].plot(g["r"], g["y"], "x", color="tab:red", ms=6, label="Gauss L=%s" % L)
axs[0].set_xscale("log"); axs[0].set_yscale("log"); axs[0].set_xlabel("r (Zellkanten)")
axs[0].set_ylabel("D(r)"); axs[0].set_title("Netz A: P2-Anteil der Pfeil-Korrelation", fontsize=9)
axs[0].legend(fontsize=6)
for net, L, mk, col in (("korr_B", LH, "o", "tab:blue"), ("korr_B", LK, "s", "tab:orange"),
                        ("korr_A", LH, "^", "tab:green")):
    k = d[net].get(L)
    if not k or "R2_alle" not in k["ringe"]:
        continue
    rg = k["ringe"]["R2_alle"]
    r = np.array(rg["r"]); y = np.array([np.nan if v is None else v for v in rg["y"]]); s = np.array(rg["s"])
    m = np.isfinite(y) & (y > 0)
    axs[1].errorbar(r[m], np.sqrt(y[m]), s[m] / (2 * np.sqrt(y[m])), fmt=mk, ms=4, color=col,
                    label="%s L=%s" % ("B" if net == "korr_B" else "A (Vergleich)", L))
    a = rg["ausgleich"]
    if net == "korr_B" and L == LH and "potenz" in a:
        xx = np.linspace(min(a["ringe_r"]), max(a["ringe_r"]), 50)
        Y = np.log(a["ringe_y"])
        c = np.polyfit(np.log(a["ringe_r"]), Y, 1)
        axs[1].plot(xx, np.sqrt(np.exp(np.polyval(c, np.log(xx)))), "k-", lw=1, label="Potenz p=%.2f" % a["potenz"]["p"])
        c2 = np.polyfit(a["ringe_r"], Y, 1)
        axs[1].plot(xx, np.sqrt(np.exp(np.polyval(c2, xx))), "k:", lw=1, label="exp xi=%.3f" % a["exponentiell"]["xi"])
axs[1].set_yscale("log"); axs[1].set_xlabel("r (Zellkanten)"); axs[1].set_ylabel("sqrt(R2) (Schalen-RMS von C)")
axs[1].set_title("Netz B (srs) gegen Netz A, Ringe", fontsize=9); axs[1].legend(fontsize=6)
fig.tight_layout(); fig.savefig(aus, dpi=85)
print("ok", aus)
