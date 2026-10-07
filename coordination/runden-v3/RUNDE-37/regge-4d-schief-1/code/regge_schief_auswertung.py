#!/usr/bin/env python3
"""REGGE-4D-SCHIEF-1: mechanische Urteile SC0 bis SC3 nach PLAN.md Abschnitt 7 und Bilder.

Aufruf: python regge_schief_auswertung.py <teil1.json> <teil2-s0.json> <teil2-s02.json> <auswertung.json> <bildordner>
"""
import json
import sys

import numpy as np

FLACH = 1e-12              # Karte SC0
FLACH_SPERRE = 1e-8        # sonst SC1 bis SC3 nicht auswertbar
HERM = 1e-10               # Karte SC0
EICH_SPERRE = 1e-6         # Eich- bzw. Affinmoden nicht im Nullraum -> nicht auswertbar
SC2_S = 0.2
SC2_BETRAEGE = (0.05, 0.075, 0.1)
SC2_ENTART = 0.01          # fuenf Spin-2-Werte gleich auf 1 % (Karte)
SC2_R = 0.02               # c0s/c2 = -2 +- 0,02 (Karte)
SC2_STREU = 0.01           # Richtungsstreuung <= 1 % (Karte; PLAN [F6]: c2 ueber die Richtungen)
SC3_L = 32
SC3_R = 6.0
SC3_TOL = 0.044            # Karte: abs(gamma(6) - 1) < 0,044
SC3_EICH_EPS = 1e-9        # PLAN [F8]: Eichmoden aendern die Fehlwinkel nicht
KUHN_GAMMA6 = 1.0872270030956324   # REGGE-ZEIT-1, L = 32, x-Achse, r = 6
KONTROLLE_TOL = 0.002      # PLAN [F10]: s = 0 mit demselben Code
KOND_2X2 = 10.0            # PLAN [F11]: zeilennormierte Kondition des 2x2-Systems
KOND_KSS = 1e8             # PLAN [F11]: Versklavungssystem
IMAG_SPERRE = 1e-8
L_VERGLEICH = 48
L_TOL = 0.01               # PLAN [F11]: gamma(6) auf L = 48 gegen L = 32
KUHN_REF = {6: 1.0872270030956324, 7: 1.05642658665781, 8: 1.0396771558969347, 9: 1.0297362895136413,
            10: 1.0233834160633328, 11: 1.0191380266816634, 12: 1.016293129027678, 13: 1.0145300247199738,
            14: 1.013775967857507}


def lauf1(t1, s):
    for r in t1["laeufe"]:
        if r["name"] == f"s={s}":
            return r
    return None


def lauf2(t2, L):
    for x in t2.get("laeufe", []):
        if x["L"] == L:
            return x
    return None


def nicht_auswertbar(grund, werte=None):
    return {"urteil": "nicht auswertbar", "vermerk": grund, "werte": werte or {}}


def sc0(t1):
    flach = {r["name"]: r["geometrie"]["flach_max_abs_eps"] for r in t1["laeufe"]}
    herm = {r["name"]: r["hermitesch_max_rel"] for r in t1["laeufe"]}
    r0 = lauf1(t1, 0.0)
    allg = r0["zufall"] + r0["leiter"]
    nk = sorted(set(p["n_null"] for p in allg))
    teil = {"flach_alle_s": len(flach) == 3 and all(v <= FLACH for v in flach.values()),
            "hermitesch_alle_s": len(herm) == 3 and all(v <= HERM for v in herm.values()),
            "s0_k0_genau_11": r0["k0"]["n_null"] == 11,
            "s0_allgemein_genau_5": nk == [5]}
    return {"urteil": "eingetroffen" if all(teil.values()) else "nicht eingetroffen",
            "werte": {"teilpruefungen": teil, "flach_max_abs_eps": flach, "hermitesch_max_rel": herm,
                      "s0_k0_nullmoden": r0["k0"]["n_null"], "s0_k0_kleinste_abs_rel_mittel":
                          r0["k0"]["kleinste_abs_rel_mittel"][:13],
                      "s0_allgemein_nullmoden": nk, "s0_allgemein_punkte": len(allg),
                      "s0_kleinster_nicht_eich_rel_mittel_min": min(p["kleinster_nicht_eich_rel_mittel"] for p in allg),
                      "s0_bz": r0.get("bz_zaehlung_null_pos_neg")}}


def sc1(t1):
    werte = {}
    teil = {}
    for s in (0.1, 0.2):
        r = lauf1(t1, s)
        if r is None:
            return nicht_auswertbar(f"s = {s} fehlt")
        if r["geometrie"]["flach_max_abs_eps"] > FLACH_SPERRE:
            return nicht_auswertbar(f"Flachheit verfehlt bei s = {s}")
        allg = r["zufall"] + r["leiter"]
        eich = max(p["eich_residuum_rel"] for p in allg)
        if eich > EICH_SPERRE or r["k0"]["affin_residuum_rel"] > EICH_SPERRE:
            return nicht_auswertbar(f"Eich- oder Affinmoden nicht im Nullraum bei s = {s}")
        nk = sorted(set(p["n_null"] for p in allg))
        teil[f"s{s}_k0_genau_10"] = r["k0"]["n_null"] == 10
        teil[f"s{s}_allgemein_genau_4"] = nk == [4]
        werte[f"s={s}"] = {"k0_nullmoden": r["k0"]["n_null"], "k0_kleinste_abs_rel_mittel":
                           r["k0"]["kleinste_abs_rel_mittel"][:13], "k0_elfter_eigenwert": r["k0"]["elfter_eigenwert"],
                           "k0_elfter_top_anteil": r["k0"]["elfter_top_anteil"],
                           "allgemein_nullmoden": nk, "allgemein_punkte": len(allg),
                           "kleinster_nicht_eich_rel_mittel_min": min(p["kleinster_nicht_eich_rel_mittel"] for p in allg),
                           "eich_residuum_max": eich, "affin_residuum_k0": r["k0"]["affin_residuum_rel"],
                           "vorzeichen_allgemein_pos_neg": sorted(set((p["n_pos"], p["n_neg"]) for p in allg)),
                           "bz": r.get("bz_zaehlung_null_pos_neg"),
                           "bz_kleinster_fuenfter_rel_mittel": r.get("bz_kleinster_fuenfter_rel_mittel")}
    return {"urteil": "eingetroffen" if all(teil.values()) else "nicht eingetroffen",
            "werte": dict(teilpruefungen=teil, **werte)}


def form_werte(pts, key):
    """Kennzahlen einer Form (schur, orth, direkt) ueber die Punkte."""
    ent, rr, c2 = [], [], {}
    allv = {}
    for p in pts:
        f = p[key]
        x = np.array(f["spin2_eigenwerte"])
        ent.append(float(np.max(np.abs(x / x.mean() - 1))))
        rr.append(float(f["verhaeltnis_0s_2"]))
        c2.setdefault(p["betrag_nominal"], []).append(f["c2"])
        allv.setdefault(p["betrag_nominal"], []).extend(list(x))
    streu = {str(b): float(np.max(np.abs(np.array(v) / np.mean(v) - 1))) for b, v in c2.items()}
    streu_alle = {str(b): float(np.max(np.abs(np.array(v) / np.mean(v) - 1))) for b, v in allv.items()}
    return {"entartung_max": max(ent), "r_min": min(rr), "r_max": max(rr), "r_abw_max": max(abs(v + 2) for v in rr),
            "c2_richtungsstreuung": streu, "spin2_alle_streuung_G3_art": streu_alle,
            "c2_mittel_durch_viertel": {str(b): float(np.mean(v) / 0.25) for b, v in c2.items()}}


def sc2(t1):
    r = lauf1(t1, SC2_S)
    if r is None:
        return nicht_auswertbar("s = 0,2 fehlt")
    if r["geometrie"]["flach_max_abs_eps"] > FLACH_SPERRE:
        return nicht_auswertbar("Flachheit verfehlt")
    pts = [p for p in r["leiter"] if p["betrag_nominal"] in SC2_BETRAEGE]
    verw = max(p["form_schur"]["Kww_verworfen"] for p in pts)
    if verw > 0:
        return nicht_auswertbar(f"Schur-Komplement: {verw} Eigenwerte verworfen")
    w = form_werte(pts, "form_schur")
    teil = {"fuenf_gleich_1_prozent": w["entartung_max"] <= SC2_ENTART,
            "verhaeltnis_minus2_pm_0_02": w["r_abw_max"] <= SC2_R,
            "richtungsstreuung_c2_1_prozent": all(v <= SC2_STREU for v in w["c2_richtungsstreuung"].values())}
    je = {}
    for p in pts:
        f = p["form_schur"]
        je.setdefault(p["richtung"], {})[str(p["betrag_nominal"])] = {
            "c2_durch_viertel": f["c2"] / 0.25, "r": f["verhaeltnis_0s_2"],
            "spin2_durch_viertel": [x / 0.25 for x in f["spin2_eigenwerte"]],
            "abw_EH_fest": f["abweichung_EH_fest_1_4"], "mischung": f["mischung"], "c1": f["c1"], "c0w": f["c0w"],
            "Kww": f["Kww_eigenwerte"]}
    return {"urteil": "eingetroffen" if all(teil.values()) else "nicht eingetroffen",
            "werte": {"teilpruefungen": teil, "schur": w, "variante_orth": form_werte(pts, "form_orth"),
                      "variante_direkt": form_werte(pts, "form_direkt"), "punkte": len(pts), "je_richtung": je,
                      "s0_zum_vergleich": form_werte([p for p in lauf1(t1, 0.0)["leiter"]
                                                      if p["betrag_nominal"] in SC2_BETRAEGE], "form_schur"),
                      "s0_1_zum_vergleich": form_werte([p for p in lauf1(t1, 0.1)["leiter"]
                                                        if p["betrag_nominal"] in SC2_BETRAEGE], "form_schur")}}


def gamma_bei(pkte, r_ziel, key="gamma"):
    """Lineare Interpolation in 1/r^2 zwischen den Achsenpunkten, die r_ziel einschliessen."""
    lo = [p for p in pkte if p["r"] <= r_ziel]
    hi = [p for p in pkte if p["r"] > r_ziel]
    if not lo or not hi:
        return None, None, None
    a = max(lo, key=lambda p: p["r"])
    b = min(hi, key=lambda p: p["r"])
    ua, ub, u = 1 / a["r"] ** 2, 1 / b["r"] ** 2, 1 / r_ziel ** 2
    g = a[key] + (b[key] - a[key]) * (u - ua) / (ub - ua)
    return float(g), a, b


def sc3(t2_0, t2_2):
    werte = {}
    x0 = lauf2(t2_0, SC3_L)
    if x0 is None:
        return nicht_auswertbar("Kontrolle s = 0 fehlt")
    p6 = [p for p in x0["achse_1"]["punkte"] if p["x0"] == 6][0]
    werte["kontrolle_s0_gamma6"] = p6["gamma"]
    werte["kontrolle_s0_alpha6"] = p6["alpha"]
    werte["kontrolle_s0_abw_von_REGGE_ZEIT_1"] = p6["gamma"] - KUHN_GAMMA6
    werte["kontrolle_s0_halbe_abweichung"] = (p6["gamma"] - 1) / 2
    if abs(p6["gamma"] - KUHN_GAMMA6) > KONTROLLE_TOL:
        return nicht_auswertbar("Kontrolle s = 0 reproduziert REGGE-ZEIT-1 nicht", werte)
    if t2_2["geometrie"]["flach_max_abs_eps"] > FLACH_SPERRE:
        return nicht_auswertbar("Flachheit verfehlt", werte)
    y = lauf2(t2_2, SC3_L)
    if y is None:
        return nicht_auswertbar("L = 32 fehlt", werte)
    k = y["kontrollen"]
    werte["kontrollen_L32"] = k
    werte["Kss_eigen"] = t2_2["kalibrierung"]["Kss_eigen"]
    werte["Kss_kondition"] = t2_2["kalibrierung"]["Kss_kondition"]
    if t2_2["kalibrierung"]["Kss_kondition"] > KOND_KSS:
        return nicht_auswertbar("Versklavungssystem schlecht konditioniert", werte)
    if k["eps_imag_max"] > IMAG_SPERRE or k["nullraum_residuum_rel_max"] > EICH_SPERRE:
        return nicht_auswertbar("Imaginaerteil oder Eichmoden nicht im Nullraum", werte)
    eindeutig = (k["n_null_min"] == 4 and k["n_null_max"] == 4 and k["eps_eichmoden_rel_max"] <= SC3_EICH_EPS)
    pk = y["achse_1"]["punkte"]
    g6, a, b = gamma_bei(pk, SC3_R)
    if g6 is None:
        return nicht_auswertbar("r = 6 nicht eingeschlossen", werte)
    werte.update({"gamma6": g6, "abw": abs(g6 - 1), "stuetzpunkte": [[a["x0"], a["r"], a["gamma"]],
                                                                       [b["x0"], b["r"], b["gamma"]]],
                  "kondition_zeilennorm": [a["kondition_zeilennorm"], b["kondition_zeilennorm"]],
                  "alpha6": gamma_bei(pk, SC3_R, "alpha")[0], "gamma_kin6": gamma_bei(pk, SC3_R, "gamma_kin")[0],
                  "gamma_gitterpunkt_x0_6": [p["gamma"] for p in pk if p["x0"] == 6][0],
                  "eindeutig": eindeutig})
    for L in (24, 32, 48):
        z = lauf2(t2_2, L)
        if z is not None:
            werte[f"L{L}"] = {f"achse{ax}": {"gamma6": gamma_bei(z[f"achse_{ax}"]["punkte"], SC3_R)[0],
                                             "alpha6": gamma_bei(z[f"achse_{ax}"]["punkte"], SC3_R, "alpha")[0],
                                             "laenge": z[f"achse_{ax}"]["laenge_A_e"],
                                             "gamma_je_r": {f"{p['r']:.3f}": p["gamma"]
                                                            for p in z[f"achse_{ax}"]["punkte"]},
                                             "kond_zn_max_6_14": max([p["kondition_zeilennorm"]
                                                                      for p in z[f"achse_{ax}"]["punkte"]
                                                                      if 5 <= p["r"] <= 14] or [0])}
                              for ax in (1, 2, 3)}
    if max(a["kondition_zeilennorm"], b["kondition_zeilennorm"]) > KOND_2X2:
        return nicht_auswertbar("2x2-System schlecht konditioniert", werte)
    z48 = lauf2(t2_2, L_VERGLEICH)
    if z48 is not None:
        g48 = gamma_bei(z48["achse_1"]["punkte"], SC3_R)[0]
        werte["gamma6_L48_minus_L32"] = g48 - g6
        if abs(g48 - g6) > L_TOL:
            return nicht_auswertbar("gamma(6) haengt von L ab (L = 48 gegen 32)", werte)
    if not eindeutig:
        return {"urteil": "nicht eingetroffen", "vermerk": "Fehlwinkel nicht eindeutig", "werte": werte}
    return {"urteil": "eingetroffen" if abs(g6 - 1) < SC3_TOL else "nicht eingetroffen", "werte": werte}


def bilder(t1, t2_0, t2_2, ordner):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    # 1) kleinste Eigenwerte gegen s
    kv = t1.get("kurve", [])
    if kv:
        s = np.array([k["s"] for k in kv])
        fig, axs = plt.subplots(1, 2, figsize=(14, 5))
        e11 = np.array([k["k0_kleinste_abs_rel_mittel"][10] for k in kv])
        e10 = np.array([k["k0_kleinste_abs_rel_mittel"][9] for k in kv])
        e12 = np.array([k["k0_kleinste_abs_rel_mittel"][11] for k in kv])
        axs[0].semilogy(s, np.maximum(e10, 1e-17), "s-", label="10. kleinster (affin)")
        axs[0].semilogy(s, np.maximum(e11, 1e-17), "o-", label="11. kleinster (Hyperdiagonale)")
        axs[0].semilogy(s, e12, "^-", label="12. kleinster (Gittermode)")
        axs[0].axhline(1e-6, color="k", ls="--", lw=0.8, label="Schwelle 1e-6 x Mittel")
        for k in kv:
            axs[0].annotate("+" if k["k0_elfter_signiert"] > 0 else "-", (k["s"], max(k["k0_kleinste_abs_rel_mittel"][10],
                                                                                         1e-17)), fontsize=9)
        axs[0].set_title("k = 0: kleinste |Eigenwerte| von H / Mittel |Eigenwert| (Vorzeichen des 11. markiert)")
        f5 = np.array([k["zufall_fuenfter_rel_mittel_min"] for k in kv])
        f5m = np.array([k["zufall_fuenfter_rel_mittel_median"] for k in kv])
        p5 = np.array([k["punkt_1234_0p1_kleinste_rel_mittel"][4] for k in kv])
        p4 = np.array([k["punkt_1234_0p1_kleinste_rel_mittel"][3] for k in kv])
        axs[1].semilogy(s, np.maximum(p4, 1e-17), "s-", label="(1,2,3,4), |k_phys| = 0,1: 4. kleinster (Eichung)")
        axs[1].semilogy(s, p5, "o-", label="(1,2,3,4), |k_phys| = 0,1: 5. kleinster")
        axs[1].semilogy(s, f5, "^-", label="64 Zufalls-k: 5. kleinster, Minimum")
        axs[1].semilogy(s, f5m, "v-", label="64 Zufalls-k: 5. kleinster, Median")
        axs[1].axhline(1e-6, color="k", ls="--", lw=0.8)
        axs[1].set_title("allgemeines k: kleinster Nicht-Eich-Eigenwert / Mittel")
        for ax in axs:
            ax.set_xlabel("s (A_raum = 1 + s B)")
            ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(f"{ordner}/bild-eigenwerte-s.png", dpi=110)
        plt.close(fig)
    # 2) Spin-2 und konform gegen Richtung
    fig, axs = plt.subplots(1, 2, figsize=(15, 5.5))
    farben = {0.0: "0.5", 0.1: "tab:orange", 0.2: "tab:blue"}
    namen = None
    for si, s in enumerate((0.0, 0.1, 0.2)):
        r = lauf1(t1, s)
        if r is None:
            continue
        for bi, (b, mk) in enumerate(((0.05, "o"), (0.1, "s"))):
            pts = [p for p in r["leiter"] if p["betrag_nominal"] == b]
            namen = [p["richtung"] for p in pts]
            for j, p in enumerate(pts):
                xs = j + (si - 1) * 0.25 + (bi - 0.5) * 0.1
                y = np.array(p["form_schur"]["spin2_eigenwerte"]) / 0.25
                axs[0].plot([xs] * len(y), y, mk, ms=3, color=farben[s],
                            label=f"s = {s}, |k| = {b}" if j == 0 else None)
                axs[1].plot(xs, p["form_schur"]["verhaeltnis_0s_2"], mk, ms=4, color=farben[s],
                            label=f"s = {s}, |k| = {b}" if j == 0 else None)
    axs[0].axhspan(0.99, 1.01, color="0.9", zorder=0)
    axs[0].set_title("Spin-2-Eigenwerte der Schur-Form / (k_phys^2 det A / 4); Band +-1 %")
    axs[1].axhspan(-2.02, -1.98, color="0.9", zorder=0)
    axs[1].set_title("konform zu Spin 2: c0s/c2; Band -2 +- 0,02")
    for ax in axs:
        ax.set_xticks(range(len(namen)))
        ax.set_xticklabels(namen, rotation=60, fontsize=7)
        ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-spin2-richtung.png", dpi=110)
    plt.close(fig)
    # 3) gamma(r)
    fig, axs = plt.subplots(1, 2, figsize=(15, 5.5))
    fl = {24: "tab:green", 32: "tab:blue", 48: "tab:purple"}
    x0 = lauf2(t2_0, 32)
    if x0 is not None:
        pk = x0["achse_1"]["punkte"]
        axs[0].plot([p["r"] for p in pk], [p["gamma"] for p in pk], "o-", ms=3, color="0.4", label="s = 0, L = 32")
        axs[1].plot([p["r"] for p in pk], [p["alpha"] for p in pk], "o-", ms=3, color="0.4", label="s = 0, L = 32")
    axs[0].plot(list(KUHN_REF), list(KUHN_REF.values()), "kx", ms=8, label="REGGE-ZEIT-1 (Kuhn, L = 32)")
    for x in t2_2.get("laeufe", []):
        L = x["L"]
        for ax_i, ls in ((1, "-"), (2, ":"), (3, "--")):
            if ax_i != 1 and L != 32:
                continue
            pk = x[f"achse_{ax_i}"]["punkte"]
            lab = f"s = 0,2, L = {L}, Achse A e_{'xyz'[ax_i - 1]}"
            axs[0].plot([p["r"] for p in pk], [p["gamma"] for p in pk], "o" + ls, ms=3, color=fl.get(L, "k"), label=lab)
            axs[1].plot([p["r"] for p in pk], [p["alpha"] for p in pk], "o" + ls, ms=3, color=fl.get(L, "k"), label=lab)
    axs[0].axvline(SC3_R, color="0.6", lw=0.8)
    axs[0].axhspan(1 - SC3_TOL, 1 + SC3_TOL, color="0.92", zorder=0)
    axs[0].set_title("gamma (2x2, versklavt kalibriert); Band +-0,044 (SC3 bei r = 6)")
    axs[1].set_title("alpha = G_gemessen / G_Wirkung")
    for ax in axs:
        ax.axhline(1.0, color="k", lw=0.8)
        ax.set_xlabel("r (physikalisch, Gitterabstaende)")
        ax.set_xlim(0, 25)
        ax.set_ylim(0.7, 1.3)
        ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-gamma.png", dpi=110)
    plt.close(fig)


def main():
    t1 = json.load(open(sys.argv[1]))
    t2_0 = json.load(open(sys.argv[2]))
    t2_2 = json.load(open(sys.argv[3]))
    u = {"SC0": sc0(t1), "SC1": sc1(t1), "SC2": sc2(t1), "SC3": sc3(t2_0, t2_2)}
    erg = {"hinweis": "Urteile nach PLAN.md Abschnitt 7 (mechanisch)", "urteile": u,
           "quellen_sha256": {"teil1": t1.get("skript_sha256"), "teil2_s0": t2_0.get("skript_sha256"),
                              "teil2_s02": t2_2.get("skript_sha256")}}
    with open(sys.argv[4], "w") as f:
        json.dump(erg, f, indent=1)
    for z, v in u.items():
        print(z, v["urteil"], v.get("vermerk", ""))
    bilder(t1, t2_0, t2_2, sys.argv[5])
    print("Bilder geschrieben")


if __name__ == "__main__":
    main()
