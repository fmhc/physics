#!/usr/bin/env python3
"""Abbildungen V1 bis V5 (Runde 16, ausprobieren). Aufruf: python plot.py <ausgabeordner>"""
import json, os, sys, traceback
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1] if len(sys.argv) > 1 else "aus"
C1, C2, C3, C4 = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7"
GRAU, TXT, TXT2, BG = "#8a8985", "#0b0b0b", "#52514e", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
                     "axes.edgecolor": TXT2, "axes.labelcolor": TXT, "xtick.color": TXT2, "ytick.color": TXT2,
                     "axes.grid": True, "grid.color": "#e4e3df", "grid.linewidth": 0.6, "font.size": 9,
                     "axes.spines.top": False, "axes.spines.right": False, "lines.linewidth": 2,
                     "legend.frameon": False})


def lade(name):
    with open(os.path.join(D, name)) as f:
        return json.load(f)


def v1():
    r = lade("v1_tetra.json")
    fig, ax = plt.subplots(1, 3, figsize=(12, 3.6))
    ax[0].plot(range(12), r["soll"], "x", color=C2, ms=9, mew=2, label="Vorhersage (k/m)")
    ax[0].plot(range(12), r["eig_analytisch"], "o", color=C1, ms=6, label="Hesse analytisch")
    ax[0].set_xlabel("Index n")
    ax[0].set_ylabel("Eigenwert mu_n = omega_n^2")
    ax[0].set_title("Spektrum Federtetraeder", color=TXT)
    ax[0].legend()
    f = np.load(os.path.join(D, "v1_fft.npz"))
    sel = f["om"] < 3
    ax[1].semilogy(f["om"][sel], f["P"][sel] / f["P"].max(), color=C1, lw=1.5)
    for w in (1, np.sqrt(2), 2):
        ax[1].axvline(w, color=GRAU, ls="--", lw=1)
    ax[1].set_xlabel("omega")
    ax[1].set_ylabel("Leistung (normiert)")
    ax[1].set_title("Zeitreihe Kantenlaengen: Spitzen bei 1, sqrt2, 2", color=TXT)
    z = r["zeitentwicklung"]
    dts = np.array([q["dt"] for q in z])
    ef = np.array([q["rel_energiefehler_max"] for q in z])
    ax[2].loglog(dts, ef, "o-", color=C1, ms=7, label="Velocity-Verlet")
    ax[2].loglog(dts, ef[0] * (dts / dts[0]) ** 2, "--", color=GRAU, lw=1, label="Steigung 2")
    ax[2].axhline(1e-6, color=C2, lw=1, ls=":", label="Kartenschwelle 1e-6")
    ax[2].set_xlabel("dt")
    ax[2].set_ylabel("max |E - E0| / E0")
    ax[2].set_title("Energiefehler", color=TXT)
    ax[2].legend()
    fig.tight_layout()
    fig.savefig(os.path.join(D, "v1_tetra.png"), dpi=130)


def v2():
    t1, t2, tz = lade("v2b_teil1.json"), lade("v2b_teil2.json"), lade("v2b_zeit.json")
    r = {"eps_raster": t1["eps_raster"], "scan": t1["scan"] + t2["scan"], "zeitentwicklung": tz["zeitentwicklung"]}
    grid = np.array(r["eps_raster"])
    sc = [e for e in r["scan"] if e["N"] <= 40]
    Ns = np.array([e["N"] for e in sc])
    M = np.array([e["maxRe"] for e in sc])
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.9))
    Z = np.log10(np.maximum(M, 1e-9))
    im = ax[0].pcolormesh(np.log10(grid), Ns, Z, cmap="Blues", shading="nearest", vmin=-9, vmax=-1)
    ec = [(e["N"], e["eps_c"]) for e in sc if "eps_c" in e]
    ax[0].plot(np.log10([q[1] for q in ec]), [q[0] for q in ec], color=C2, lw=2, label="Grenze eps_c(N)")
    nn = np.arange(7, 41)
    ax[0].plot(np.log10(2.298 / nn ** 3), nn, "--", color=TXT2, lw=1, label="Maxwell 2,298/N^3 [L?]")
    ax[0].axhline(6.5, color=TXT2, lw=0.8, ls=":")
    ax[0].set_xlabel("log10(m/M)")
    ax[0].set_ylabel("N")
    ax[0].set_title("max Re s (log10), hell = stabil", color=TXT)
    ax[0].legend(loc="lower left", fontsize=8)
    fig.colorbar(im, ax=ax[0], fraction=0.046)
    ec_all = [(e["N"], e["eps_c_N3"]) for e in r["scan"] if "eps_c_N3" in e]
    ax[1].plot([q[0] for q in ec_all], [q[1] for q in ec_all], "o", color=C1, ms=6, label="eps_c * N^3 (berechnet)")
    ax[1].axhline(1 / 0.4352, color=GRAU, ls="--", lw=1, label="1/0,4352 = 2,298 (Maxwell, [L?])")
    ax[1].set_xscale("log")
    ax[1].set_xlabel("N")
    ax[1].set_ylabel("eps_c * N^3")
    ax[1].set_title("Skalierung der Stabilitaetsgrenze", color=TXT)
    ax[1].legend(fontsize=8)
    for N, col in ((6, C2), (8, C1)):
        f = np.load(os.path.join(D, f"v2b_zeit_N{N}_rtol1e-12.npz"))
        ax[2].semilogy(f["t"], f["D"], color=col, lw=1.5, label=f"N = {N}, m/M = 1e-4")
    z6 = [q for q in r["zeitentwicklung"] if q["N"] == 6 and q["rtol"] == 1e-12][0]
    t = np.linspace(0, 1500, 50)
    ax[2].semilogy(t, z6["D0"] * np.exp(z6["maxRe_linear"] * t), "--", color=TXT2, lw=1,
                   label="exp(max Re s * t) aus Linearisierung")
    ax[2].set_ylim(1e-8, 1)
    ax[2].set_xlabel("t (Einheiten 1/Omega)")
    ax[2].set_ylabel("Formabweichung D(t)")
    ax[2].set_title("Nichtlineare Zeitentwicklung", color=TXT)
    ax[2].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "v2_maxwell.png"), dpi=130)


def v3():
    r = {"F0": lade("v3b_F0.json")["F0"], "F1": lade("v3b_F1.json")["F1"]}
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.9))
    for k, var in enumerate(("F1",)):
        tab = r[var]
        Ns = np.array([e["N"] for e in tab])
        rel = np.array(tab[0]["omega_raster"]) / tab[0]["sqrtK"]
        M = np.array([e["omega_raster_maxRe"] for e in tab])
        im = ax[0].pcolormesh(rel, Ns, np.log10(np.maximum(M, 1e-9)), cmap="Blues", shading="nearest",
                              vmin=-9, vmax=0)
        ax[0].set_xlabel("Omega / sqrt(K_N)")
        ax[0].set_ylabel("N")
        ax[0].set_title("F1 (L_s = L_r = 1): max Re s (log10), 2D", color=TXT)
        fig.colorbar(im, ax=ax[0], fraction=0.046)
    for var, col in (("F0", C1), ("F1", C2)):
        tab = r[var]
        ax[1].plot([e["N"] for e in tab], [e["Om0.6"]["omega_soft"] for e in tab], "o-", color=col, ms=4,
                   lw=1.5, label=f"{var}")
    for N in (11, 19):
        ax[1].axvline(N, color=GRAU, lw=0.8, ls=":")
        ax[2].axvline(N, color=GRAU, lw=0.8, ls=":")
    ax[1].set_xlabel("N")
    ax[1].set_ylabel("weichste Frequenz |Im s|")
    ax[1].set_title("omega_soft bei Omega = 0,6 (2D)", color=TXT)
    ax[1].legend()
    tab = r["F1"]
    xs = [e["N"] for e in tab if e.get("Omega_stab") is not None]
    ys = [e["Omega_stab"] for e in tab if e.get("Omega_stab") is not None]
    ax[2].plot(xs, ys, "o-", color=C2, ms=4, lw=1.5, label="F1: Omega_stab (2D)")
    x3 = [e["N"] for e in tab]
    ax[2].plot(x3, [e["sqrtK"] for e in tab], "--", color=GRAU, lw=1, label="sqrt(K_N): dort R -> unendlich")
    ax[2].set_xlabel("N")
    ax[2].set_ylabel("Omega")
    ax[2].set_title("F1: Rotation stabilisiert ab Omega_stab", color=TXT)
    ax[2].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "v3_federring.png"), dpi=130)


def v4():
    r = lade("v4_ticks.json")
    L = r["laeufe_T200"]
    dts = [q["dt"] for q in L]
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
    ax[0].semilogx(dts, [q["naiv_soll_3EF_4KK"] for q in L], "--", color=GRAU, lw=1,
                   label="Soll naiv = 3 N_EF + 4 N_KK")
    ax[0].semilogx(dts, [q["naiv_summe"] for q in L], "o-", color=C2, ms=6, label="naiv: Summe |B_k Delta B_k+1|")
    ax[0].semilogx(dts, [q["N_ticks"] for q in L], "o-", color=C1, ms=6, label="ereignisgenau: Ticks")
    ax[0].semilogx(dts, [q["naiv_schritte_mit_wechsel"] for q in L], "s-", color=C3, ms=5,
                   label="naiv: Schritte mit Wechsel")
    ax[0].set_xlabel("dt")
    ax[0].set_ylabel("Anzahl in T = 200")
    ax[0].set_title("Zaehlung gegen Schrittweite", color=TXT)
    ax[0].legend(fontsize=8)
    f = np.load(os.path.join(D, "v4_ref_ereignisse.npz"))
    t = np.sort(f["t"])
    ax[1].plot(t, np.arange(1, t.size + 1), color=C1, lw=1.5, label="Referenz dt = 0,001")
    ax[1].plot(t, r["referenz"]["nu"] * t, "--", color=GRAU, lw=1, label=f"nu = {r['referenz']['nu']:.3f}")
    ax[1].set_xlabel("t")
    ax[1].set_ylabel("kumulierte Ticks")
    ax[1].set_title("Tick-Uhr (Ecke-Flaeche + Kante-Kante)", color=TXT)
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "v4_ticks.png"), dpi=130)


def v5():
    r = lade("v5_feld.json")
    fig, ax = plt.subplots(1, 4, figsize=(16, 3.9))
    try:
        rb = lade("v5b_feld.json")
        for J, col in ((0.05, C1), (0.1, C2), (0.2, C3)):
            sel = [e for e in rb["fest"] if e["J"] == J and e.get("ok")]
            ax[3].plot([e["N"] for e in sel], [e["Q"] for e in sel], "o-", color=col, ms=4, lw=1.5,
                       label=f"J = {J}, omega^2 = {sel[0]['w2'] if sel else ''}")
        for N in (11, 19):
            ax[3].axvline(N, color=GRAU, lw=0.8, ls=":")
        ax[3].set_xlabel("N")
        ax[3].set_ylabel("Q bei festem omega^2")
        ax[3].set_title("Ringmode: Ladung gegen N", color=TXT)
        ax[3].legend(fontsize=7)
    except Exception:
        traceback.print_exc()
    for br, col in (("klein", C1), ("gross", C2)):
        rows = [q for q in r["details"]["N11_J0.1_ring_" + br] if q]
        w2 = np.array([q["w2"] for q in rows])
        Q = np.array([q["Q"] for q in rows])
        st = np.array([q["maxRe"] <= 1e-6 for q in rows])
        ax[0].plot(w2[st], Q[st], "o", color=col, ms=4, label=f"Zweig {br}, stabil")
        ax[0].plot(w2[~st], Q[~st], "o", mfc="none", color=col, ms=6, label=f"Zweig {br}, instabil")
    ax[0].set_xlabel("omega^2")
    ax[0].set_ylabel("Q = 2 omega sum phi^2")
    ax[0].set_title("N = 11, J = 0,1, Mode auf Ringknoten", color=TXT)
    ax[0].legend(fontsize=8)
    tab = r["tabelle"]
    for J, col in ((0.05, C1), (0.1, C2), (0.2, C3)):
        sel = [t for t in tab if t["J"] == J and t["mode"] == "ring" and t["zweig"] == "klein" and t["existiert"]]
        Ns = [t["N"] for t in sel]
        ax[1].plot(Ns, [t["w2_min"] for t in sel], "o-", color=col, ms=4, lw=1.5, label=f"J = {J}: Fenster")
        ax[1].plot(Ns, [t["w2_max"] for t in sel], "o-", color=col, ms=4, lw=1.5)
        ax[1].plot(Ns, [t["w2_stabil_max"] if t["w2_stabil_max"] is not None else np.nan for t in sel], "x",
                   color=col, ms=6, label=f"J = {J}: stabil bis")
        selz = [t for t in tab if t["J"] == J and t["mode"] == "zentrum" and t["zweig"] == "klein"]
        ax[2].plot([t["N"] for t in selz], [t["w2_max"] if t["existiert"] else np.nan for t in selz], "o-",
                   color=col, ms=4, lw=1.5, label=f"J = {J}: obere Grenze")
        ax[2].plot([t["N"] for t in selz], [t["w2_min"] if t["existiert"] else np.nan for t in selz], "s--",
                   color=col, ms=4, lw=1, label=f"J = {J}: untere Grenze")
    for a in ax[1:3]:
        for N in (11, 19):
            a.axvline(N, color=GRAU, lw=0.8, ls=":")
        a.axhspan(0.5, 1.0, color="#e4e3df", alpha=0.4, lw=0)
        a.set_xlabel("N")
        a.set_ylabel("omega^2")
        a.legend(fontsize=7)
    ax[1].set_title("Ringmode (kleiner Zweig): Existenzfenster", color=TXT)
    ax[2].set_title("Zentrumsmode (kleiner Zweig): Existenzfenster", color=TXT)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "v5_feld.png"), dpi=130)


for fn in (v1, v2, v3, v4, v5):
    try:
        fn()
        print("ok", fn.__name__)
    except Exception:
        print("FEHLER", fn.__name__)
        traceback.print_exc()
