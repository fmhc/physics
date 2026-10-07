#!/usr/bin/env python3
"""REGGE-ZEIT-1: mechanische Urteile Z0 bis Z3 nach PLAN.md Abschnitt 7 und Bilder.

Aufruf: python regge_zeit_auswertung.py <haupt.json> <auswertung.json> <bildordner>
"""
import json
import sys

import numpy as np

L_KARTE = (16, 24, 32)     # Karte; geurteilt wird das groesste davon (PLAN [F7])
L_URTEIL = 32
R_MIN = 6.0                # Karte: 6 <= r <= L/2 - 2
NULL_TOL = 1e-12           # Karte Z0
D3_AUSSEN = 1e-12          # Karte Z0
D3_WL = 1e-10              # Karte Z0
Z1_TOL = 0.02
Z2_TOL = 0.02
Z3_TOL = 0.03
FLACH = 1e-8               # sonst nicht auswertbar
KOND = 1e3                 # 2x2-System schlecht konditioniert -> nicht auswertbar


def lauf(d, L):
    for x in d["laeufe"]:
        if x["L"] == L:
            return x
    return None


def urteile(d):
    u = {}
    g = d["geometrie"]
    k3 = d["kontrolle_3d"]
    # ---------------- Z0
    proj = {str(x["L"]): x["kontrollen"]["quelle_auf_nullraum_rel_max"] for x in d["laeufe"] if x["L"] in L_KARTE}
    teil = {"quelle_4d": all(v <= NULL_TOL for v in proj.values()) and len(proj) > 0,
            "d3_ausserhalb": k3["ausserhalb_max_rel"] <= D3_AUSSEN,
            "d3_weltlinie": k3["weltlinie_rel_abw"] <= D3_WL}
    u["Z0"] = {"urteil": "eingetroffen" if all(teil.values()) else "nicht eingetroffen",
               "werte": {"teilpruefungen": teil, "quelle_auf_nullraum_rel_max_je_L": proj,
                         "d3_ausserhalb_max_rel": k3["ausserhalb_max_rel"],
                         "d3_weltlinie_rel_abw": k3["weltlinie_rel_abw"], "d3_eps_weltlinie": k3["eps_weltlinie"],
                         "d3_soll": k3["soll_8piGM"],
                         "d3_quelle_auf_nullraum": k3["kontrollen_loesung"]["quelle_auf_nullraum_rel_max"]}}
    x = lauf(d, L_URTEIL)
    gesperrt = None
    if g["flach_max_abs_eps"] > FLACH:
        gesperrt = "Flachheit verfehlt"
    elif x is None:
        gesperrt = f"L = {L_URTEIL} fehlt"
    if gesperrt:
        for z in ("Z1", "Z2", "Z3"):
            u[z] = {"urteil": "nicht auswertbar", "vermerk": gesperrt, "werte": {}}
        return u
    rmax = L_URTEIL / 2 - 2
    # ---------------- Z1
    pk = [a for a in x["achse"] if R_MIN <= a["r"] <= rmax]
    kond = max(a["kondition"] for a in pk)
    gam = {str(a["r"]): a["gamma"] for a in pk}
    dev = max(abs(v - 1) for v in gam.values())
    if kond > KOND:
        u["Z1"] = {"urteil": "nicht auswertbar", "vermerk": f"Kondition {kond:.3g}", "werte": {"gamma": gam}}
    else:
        u["Z1"] = {"urteil": "eingetroffen" if dev <= Z1_TOL else "nicht eingetroffen",
                   "werte": {"gamma_je_r": gam, "max_abw": dev, "kondition_max": kond, "punkte": len(pk),
                             "kartenlesart_1_durch_naiv": {str(a["r"]): 1.0 / a["verhaeltnis_naiv"] for a in pk},
                             "naiv": {str(a["r"]): a["verhaeltnis_naiv"] for a in pk},
                             "gamma_kinematisch_kalibriert": {str(a["r"]): a["gamma_kin"] for a in pk},
                             "ortskorrigiert": {str(a["r"]): a["verhaeltnis_ort"] for a in pk}}}
    # ---------------- Z2
    q = x["tx_quadrate"]
    r = np.array(q["r"])
    korr = np.array(q["roh"]) + np.array(q["hintergrund"]) - np.array(q["bild"])
    pgr = np.array(q["PN"]) + np.array(q["PS"])
    m = (r >= R_MIN) & (r <= rmax)
    Q = r[m] ** 3 * korr[m]
    konst = float(np.max(np.abs(Q / Q.mean() - 1)))
    Gk = float(np.mean(korr[m] / pgr[m]))
    alpha = float(np.mean([a["alpha"] for a in pk]))
    u["Z2"] = {"urteil": "eingetroffen" if (konst <= Z2_TOL and abs(Gk - 1) <= Z2_TOL) else "nicht eingetroffen",
               "werte": {"teilpruefungen": {"r3_konstant": konst <= Z2_TOL, "G_karte": abs(Gk - 1) <= Z2_TOL},
                         "r": r[m].tolist(), "r3_eps_korr": Q.tolist(), "r3_max_abw_vom_mittel": konst,
                         "G_karte": Gk, "G_karte_je_r": (korr[m] / pgr[m]).tolist(),
                         "alpha_2x2_mittel": alpha, "alpha_2x2_je_r": {str(a["r"]): a["alpha"] for a in pk},
                         "r3_eps_roh": (r[m] ** 3 * np.array(q["roh"])[m]).tolist()}}
    # ---------------- Z3
    pdg = [a for a in x["diagonale"] if R_MIN <= a["r"] <= rmax]
    if not pdg:
        u["Z3"] = {"urteil": "nicht auswertbar", "vermerk": "keine Diagonalpunkte im Bereich", "werte": {}}
    else:
        kd = max(a["kondition"] for a in pdg)
        gd = {f"{a['r']:.4f}": a["gamma"] for a in pdg}
        dd = max(abs(v - 1) for v in gd.values())
        if kd > KOND:
            u["Z3"] = {"urteil": "nicht auswertbar", "vermerk": f"Kondition {kd:.3g}", "werte": {"gamma": gd}}
        else:
            u["Z3"] = {"urteil": "eingetroffen" if dd <= Z3_TOL else "nicht eingetroffen",
                       "werte": {"gamma_je_r": gd, "max_abw": dd, "kondition_max": kd, "punkte": len(pdg),
                                 "alpha_je_r": {f"{a['r']:.4f}": a["alpha"] for a in pdg}}}
    return u


def bilder(d, ordner):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    farben = {16: "tab:green", 24: "tab:orange", 32: "tab:blue", 64: "tab:purple"}
    # gamma(r)
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    for x in d["laeufe"]:
        L = x["L"]
        r = [a["r"] for a in x["achse"]]
        axs[0].plot(r, [a["gamma"] for a in x["achse"]], "o-", ms=3, color=farben.get(L, "k"), label=f"Achse L = {L}")
        axs[0].plot(r, [a["alpha"] for a in x["achse"]], "x:", ms=3, color=farben.get(L, "k"), alpha=0.6,
                    label=f"G/G_Wirkung (alpha) L = {L}")
        rd = [a["r"] for a in x["diagonale"]]
        axs[1].plot(rd, [a["gamma"] for a in x["diagonale"]], "s-", ms=3, color=farben.get(L, "k"),
                    label=f"Diagonale L = {L}")
    axs[0].axhspan(0.98, 1.02, color="0.9", zorder=0)
    axs[1].axhspan(0.97, 1.03, color="0.9", zorder=0)
    for ax in axs:
        ax.axvspan(R_MIN, L_URTEIL / 2 - 2, color="tab:blue", alpha=0.06, zorder=0)
        ax.axhline(1.0, color="k", lw=0.8)
        ax.set_xlabel("r (Gitterabstaende)")
        ax.set_ylim(0.8, 1.2)
        ax.legend(fontsize=7)
    axs[0].set_title("x-Achse: gamma (2x2, kalibriert) und alpha = G/G_Wirkung; Band +-2 %")
    axs[1].set_title("Diagonale (1,1,0): gamma aus (tau,z)- gegen (x,y)-Quadrate; Band +-3 %")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-gamma.png", dpi=110)
    plt.close(fig)
    # r^3 delta eps
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    for x in d["laeufe"]:
        L = x["L"]
        q = x["tx_quadrate"]
        r = np.array(q["r"])
        korr = np.array(q["roh"]) + np.array(q["hintergrund"]) - np.array(q["bild"])
        axs[0].plot(r, r ** 3 * korr, "o-", ms=3, color=farben.get(L, "k"), label=f"korrigiert L = {L}")
        axs[0].plot(r, r ** 3 * np.array(q["roh"]), "--", lw=0.8, color=farben.get(L, "k"), label=f"roh L = {L}")
        if L == L_URTEIL:
            axs[0].plot(r, r ** 3 * (np.array(q["PN"]) + np.array(q["PS"])), "k-", lw=1.2,
                        label="Erwartung Einstein (kalibriert)")
        ra = np.array([a["r"] for a in x["achse"]])
        yz = np.array([a["yz"]["korr"] for a in x["achse"]])
        yzr = np.array([a["yz"]["roh"] for a in x["achse"]])
        axs[1].plot(ra, ra ** 3 * yz, "o-", ms=3, color=farben.get(L, "k"), label=f"korrigiert L = {L}")
        axs[1].plot(ra, ra ** 3 * yzr, "--", lw=0.8, color=farben.get(L, "k"), label=f"roh L = {L}")
        if L == L_URTEIL:
            axs[1].plot(ra, ra ** 3 * np.array([a["yz"]["PN"] + a["yz"]["PS"] for a in x["achse"]]), "k-", lw=1.2,
                        label="Erwartung Einstein (kalibriert)")
    for ax in axs:
        ax.axvspan(R_MIN, L_URTEIL / 2 - 2, color="tab:blue", alpha=0.06, zorder=0)
        ax.set_xlabel("r (Gitterabstaende)")
        ax.legend(fontsize=7)
    axs[0].set_title("(tau,x)-Quadrate auf der x-Achse: r^3 delta eps (G M = 1)")
    axs[1].set_title("(y,z)-Quadrate um die x-Achse: r^3 delta eps (Mittel von 4)")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-r3-eps.png", dpi=110)
    plt.close(fig)
    # 3D-Kontrolle
    k3 = d["kontrolle_3d"]
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    for ax, key, tit in ((axs[0], "bild_zeit", "Zeitkanten"), (axs[1], "bild_raum_max", "Raumkanten (max)")):
        A = np.array(k3[key]) / k3["soll_8piGM"]
        A = np.fft.fftshift(A)
        im = ax.imshow(np.log10(np.maximum(A, 1e-18)), origin="lower", cmap="viridis", vmin=-18, vmax=0)
        ax.set_title(f"3D-Kontrolle: log10 |eps|/(8 pi G M), {tit}")
        fig.colorbar(im, ax=ax, fraction=0.046)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-3d.png", dpi=110)
    plt.close(fig)


def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    u = urteile(d)
    erg = {"hinweis": "Urteile nach PLAN.md Abschnitt 7 (mechanisch)", "urteile": u,
           "geometrie": d["geometrie"], "kalibrierung_kontrollen": d["kalibrierung"]["kontrollen"],
           "antwort_achse_einheit": d["kalibrierung"]["antwort_achse_einheit"],
           "fixierung_kontrollen": d["fixierung_kontrollen"], "hintergrund_kappa_diff": d["hintergrund"]["kappa_diff_max"],
           "kontrollen_je_L": {str(x["L"]): x["kontrollen"] for x in d["laeufe"]},
           "kontrolle_3d": {k: v for k, v in d["kontrolle_3d"].items() if not k.startswith("bild_")}}
    with open(sys.argv[2], "w") as f:
        json.dump(erg, f, indent=1)
    for z, v in u.items():
        print(z, v["urteil"])
    bilder(d, sys.argv[3])
    print("Bilder geschrieben")


if __name__ == "__main__":
    main()
