# AETHER-UHR-1 (Runde 36): Bilder aus auswertung.json (nur Darstellung, keine Urteile).
# Aufruf (nur ueber kleintest.sh): bilder.py <auswertung.json> <ausgabe-ordner>
import sys, os, json, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FARBE = {"100": "#2a78d6", "115": "#eb6834", "170": "#1baf7a"}   # feste Reihenfolge (dataviz-Referenzpalette 1-3)
CBW = {"100": 1.0, "115": 1.15, "170": 1.7}
VERS = {"100": -0.008, "115": 0.0, "170": 0.008}                # seitlicher Versatz nur zur Lesbarkeit
MARKE = {"H": ("o", "Hauptlauf"), "A": ("s", "Adiabatik-Probe"), "G": ("^", "Gitterprobe")}
INK = "#222222"; INK2 = "#666666"; GRID = "#dddddd"


def stil(ax):
    ax.grid(True, color=GRID, lw=0.6)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK2)
    ax.tick_params(colors=INK2, labelcolor=INK)


def punkte(ax, d, kenn, y_von, versatz=False, nur_plateaus=False):
    werte = []
    for satz in ("H", "A", "G"):
        e = d["saetze"][satz].get(kenn)
        if not e or "plateaus" not in e or "R0" not in e:
            continue
        pl = e["plateaus"][1:] if nur_plateaus else e["plateaus"]
        dv = VERS[kenn] if versatz else 0.0
        dv += {"H": 0.0, "A": -0.003, "G": 0.003}[satz]
        y = [y_von(p) for p in pl]
        werte += y
        mk, nm = MARKE[satz]
        ax.plot([p["v"] + dv for p in pl], y, mk, ms=8 if satz == "H" else 6,
                mfc=FARBE[kenn] if satz == "H" else "white", mec=FARBE[kenn], mew=1.5, ls="none",
                label="%s, c_B = %.2f" % (nm, CBW[kenn]) if versatz else nm)
    return werte


def main():
    d = json.load(open(sys.argv[1])); aus = sys.argv[2]
    os.makedirs(aus, exist_ok=True)
    # Bild 1: R(v)/R(0) - 1 gegen v, drei Felder (je c_B), Sollkurven
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.6), constrained_layout=True)
    for ax, kenn in zip(axs, ("100", "115", "170")):
        stil(ax)
        col = FARBE[kenn]; cB = CBW[kenn]
        k = d["kurven"].get(kenn)
        if k:
            v = np.array(k["v"]); kar = np.array(k["karte"])
            if cB != 1.0:
                ax.fill_between(v, 0.8 * kar, 1.2 * kar, color=col, alpha=0.13, lw=0, label="Karte +-20 %")
            else:
                ax.axhspan(-1e-3, 1e-3, color=col, alpha=0.13, lw=0, label="U0-Band +-1e-3")
            ax.plot(v, kar, "--", color=INK2, lw=1.4, label="Karte: v^2 (1 - 1/c_B^2)")
            ax.plot(v, k["hart"], ":", color=INK, lw=1.4, label="harter Hohlraum: gA^2/gB^2 - 1")
            ax.plot(v, k["kin"], "-", color=col, lw=2.0, label="Kinematik mit Ruhemode K(v) [M]")
        w = punkte(ax, d, kenn, lambda p: p["R_rel"])
        ax.set_title("c_B = %.2f" % cB, color=INK, fontsize=12)
        ax.set_xlabel("Endgeschwindigkeit v (gemessen, c_A = 1)", color=INK)
        ax.set_xlim(-0.02, 0.66)
        if cB == 1.0:
            lim = max(2e-3, 1.3 * max([abs(x) for x in w] + [0.0]))
            ax.set_ylim(-lim, lim)
            ax.legend(loc="lower left", fontsize=8, frameon=False)
    axs[0].set_ylabel("R(v)/R(0) - 1,   R = Omega_B/omega_A", color=INK)
    axs[2].legend(loc="upper left", fontsize=8, frameon=False)
    fig.suptitle("AETHER-UHR-1: Uhrenvergleich im bewegten Beutel (synthetisch, 1+1D; Proben seitlich versetzt)",
                 color=INK, fontsize=12)
    fig.savefig(os.path.join(aus, "R_gegen_v.png"), dpi=130)
    plt.close(fig)
    # Bild 2: Rest gegen die exakte Kinematik K(v)
    fig, ax = plt.subplots(1, 1, figsize=(7.5, 4.4), constrained_layout=True)
    stil(ax)
    for kenn in ("100", "115", "170"):
        punkte(ax, d, kenn, lambda p: 1e3 * (p["R_rel"] - p["soll_kin"]), versatz=True, nur_plateaus=True)
    ax.axhline(0, color=INK2, lw=0.8)
    ax.set_xlabel("v (gemessen; seitlich versetzt)", color=INK)
    ax.set_ylabel("(R/R0 - 1) - K(v)  in 1e-3", color=INK)
    ax.set_title("Abweichung von der Kinematik mit Ruhemode", color=INK, fontsize=12)
    ax.legend(fontsize=7.5, frameon=False, ncol=3, loc="best")
    fig.savefig(os.path.join(aus, "R_rest_gegen_K.png"), dpi=130)
    plt.close(fig)
    # Bild 3: Beutellaenge L(v)/L(0) gegen v und Rest gegen 1/gamma_A
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.6), constrained_layout=True)
    vg = np.linspace(0, 0.65, 131)
    ax = axs[0]; stil(ax)
    ax.plot(vg, np.sqrt(1 - vg ** 2), "-", color=INK, lw=1.6, label="1/gamma_A (c_A = 1)")
    for kenn in ("115", "170"):
        cB = CBW[kenn]
        ax.plot(vg, np.sqrt(1 - vg ** 2 / cB ** 2), ":", color=FARBE[kenn], lw=1.6, label="1/gamma_B, c_B = %.2f" % cB)
    for kenn in ("100", "115", "170"):
        e = d["saetze"]["H"].get(kenn)
        if not e or "R0" not in e:
            continue
        L0 = e["plateaus"][0]["LR"]
        ax.plot([p["v"] + VERS[kenn] for p in e["plateaus"]], [p["LR"] / L0 for p in e["plateaus"]], "o", ms=8,
                mfc=FARBE[kenn], mec="white", mew=1.0, ls="none", label="Beutel, c_B = %.2f" % CBW[kenn])
    ax.set_xlabel("v (gemessen; Punkte seitlich versetzt)", color=INK)
    ax.set_ylabel("L(v)/L(0)  (Halbwertsbreite der Ladungsdichte)", color=INK)
    ax.legend(fontsize=8.5, frameon=False, loc="lower left")
    ax = axs[1]; stil(ax)
    w = []
    for kenn in ("100", "115", "170"):
        w += punkte(ax, d, kenn, lambda p: 1e2 * p["L_rel"], versatz=True, nur_plateaus=True)
    lim = min(1.2, max(0.05, 1.5 * max([abs(x) for x in w] + [0.0])))
    ax.axhspan(-1, 1, color="#999999", alpha=0.10, lw=0, label="U3-Band +-1 %")
    ax.axhline(0, color=INK2, lw=0.8)
    ax.set_ylim(-lim, lim)
    ax.set_xlabel("v (gemessen; seitlich versetzt)", color=INK); ax.set_ylabel("L(v) gamma_A/L(0) - 1  in %", color=INK)
    ax.set_xlim(0.15, 0.65)
    ax.legend(fontsize=7, frameon=False, ncol=3, loc="upper left")
    fig.savefig(os.path.join(aus, "laenge_gegen_v.png"), dpi=130)
    plt.close(fig)
    print("ok", flush=True)


if __name__ == "__main__":
    main()
