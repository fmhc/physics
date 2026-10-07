#!/usr/bin/env python3
"""SPIN-ZUFALLSNETZ-1: Urteile nach PLAN.md Abschnitt 7 und Bilder. Liest lauf/*.json, schreibt lauf/auswertung.json
und lauf/bild-*.png. Aufruf (nur ueber kleintest.sh): python auswertung.py <lauf-ordner>"""
import glob
import json
import math
import os
import sys

import numpy as np

EPS_GITTER = [0.20, 0.25, 0.30, 0.35, 0.40]
EPS0 = 0.05
RHO_K = EPS0 ** 2 / (6 * math.pi ** 2)
WAECHTER = 1.0 + 1e-6


def lade(pfad):
    with open(pfad) as f:
        return json.load(f)


def idx_eps(eps_liste, e):
    a = np.asarray(eps_liste)
    i = int(np.argmin(np.abs(a - e)))
    assert abs(a[i] - e) < 1e-9, (e, a[i])
    return i


def netz_pool(dateien):
    """Alle Saaten aus den Dateien: KPM-Proben, Spektral, Pruefungen."""
    saaten = []
    for p in dateien:
        d = lade(p)
        saaten.extend(d["saaten"])
        if not d["saaten"] and "teil" in d:      # Lauf nach dem KPM-Teil abgebrochen
            saaten.append(d["teil"])
    return saaten


def kpm_pool(saaten):
    eps = saaten[0]["kpm"]["eps"]
    proben = np.concatenate([np.asarray(s["kpm"]["n_proben"]) for s in saaten], axis=1)   # (ne, R)
    rho = np.mean([np.asarray(s["kpm"]["rho_mittel"]) for s in saaten], axis=0)
    E = np.asarray(saaten[0]["kpm"]["E"])
    mu = max(s["kpm"]["mu_max_betrag"] for s in saaten)
    return eps, proben, E, rho, mu


def n_s(eps, proben):
    R = proben.shape[1]
    out = []
    for e in EPS_GITTER:
        i = idx_eps(eps, e)
        m = proben[i].mean()
        se = proben[i].std(ddof=1) / math.sqrt(R)
        f = 3 * math.pi ** 2 / e ** 3
        out.append({"eps": e, "n": m, "n_se": se, "n_s": m * f, "n_s_se": se * f})
    return out


def rho0(eps, proben):
    i = idx_eps(eps, EPS0)
    R = proben.shape[1]
    r = proben[i] / (2 * EPS0)
    return float(r.mean()), float(r.std(ddof=1) / math.sqrt(R)), int(R)


def geometrie_ok(saaten):
    fehl = []
    for s in saaten:
        p = s["pruefung"]
        ok = (p["euler"] == 0 and p["dreiecke_genau_zwei"] and p["umkugel_ausserhalb_saum"] == 0
              and p["abschluss_max_rel"] < 1e-10 and p["volumen_summe_rel"] < 1e-10 and p["A_nicht_positiv"] == 0
              and p["kante_bild_konsistenz_s"] == 0 and p["knoten_benutzt"] == p["N"]
              and s["op"]["hermitesch_max"] < 1e-12 and s["op"]["nullmoden_residuum"] < 1e-10)
        if not ok:
            fehl.append(s["saat"])
    return fehl


def fit_rho(E, rho, lo=0.05, hi=0.30):
    E = np.asarray(E)
    sym = 0.5 * (rho + rho[::-1])     # E-Raster symmetrisch um 0
    sel = (E >= lo - 1e-9) & (E <= hi + 1e-9)
    X = np.stack([np.ones(sel.sum()), E[sel] ** 2], axis=1)
    c, *_ = np.linalg.lstsq(X, sym[sel], rcond=None)
    return {"rho0_fit": float(c[0]), "c_fit": float(c[1]), "c_kegel": 1 / (2 * math.pi ** 2), "fenster": [lo, hi]}


def asymmetrie(E, rho, emax=0.5):
    E = np.asarray(E)
    sel = (E > 0) & (E <= emax)
    a = rho[sel]
    b = rho[::-1][sel]
    return float(np.max(np.abs(a - b) / (0.5 * (a + b))))


def main():
    ordner = sys.argv[1]
    erg = {"urteile": {}}
    kon = lade(os.path.join(ordner, "kontrolle.json"))
    g46 = lade(os.path.join(ordner, "gitter46.json"))
    g22 = lade(os.path.join(ordner, "gitter22.json"))
    n4 = netz_pool(sorted(glob.glob(os.path.join(ordner, "netz1e4-*.json"))))
    n5 = netz_pool(sorted(glob.glob(os.path.join(ordner, "netz1e5-*.json"))))
    erg["saaten_1e4"] = [s["saat"] for s in n4]
    erg["saaten_1e5"] = [s["saat"] for s in n5]

    # ---------------- SZ0
    k = g46["kpm"]
    prob = np.asarray(k["n_proben"])
    ns0 = n_s(k["eps"], prob)
    teil_i = all(7.5 <= x["n_s"] <= 8.5 for x in ns0)
    null16 = [x["null_1e-9"] for x in kon["K1_kubisch_dicht"] if x["L"] == 6 and max(map(abs, x["theta"])) == 0][0]
    teil_ii = null16 == 16
    teil_iii = k["kpm_minus_exakt_max"] <= 0.01 and k["mu_max_betrag"] <= WAECHTER
    if not teil_iii:
        u0 = "nicht auswertbar"
    else:
        u0 = "eingetroffen" if (teil_i and teil_ii) else "nicht eingetroffen"
    erg["urteile"]["SZ0"] = {"urteil": u0, "werte": {
        "n_s_L46": ns0, "analytisch_n_s": [n * 3 * math.pi ** 2 / e ** 3 for n, e in
                                          zip(g46["analytisch_n_mittel"], g46["analytisch_mittel_eps"])],
        "nullmoden_L6_theta0": null16, "kpm_minus_exakt_max": k["kpm_minus_exakt_max"],
        "mu_max": k["mu_max_betrag"], "teil_i": teil_i, "teil_ii": teil_ii, "teil_iii": teil_iii}}

    # ---------------- SZ1
    fehl5 = geometrie_ok(n5)
    fehl4 = geometrie_ok(n4)
    eps5, prob5, E5, rho5, mu5 = kpm_pool(n5)
    eps4, prob4, E4, rho4, mu4 = kpm_pool(n4)
    ns5 = n_s(eps5, prob5)
    ns4 = n_s(eps4, prob4)
    ok1 = (not fehl5) and mu5 <= WAECHTER
    if not ok1:
        u1 = "nicht auswertbar"
    else:
        u1 = "eingetroffen" if all(2 / 3 <= x["n_s"] <= 1.5 for x in ns5) else "nicht eingetroffen"
    u1_gegen = "eingetroffen" if all(2 / 3 <= x["n_s"] <= 1.5 for x in ns4) else "nicht eingetroffen"
    erg["urteile"]["SZ1"] = {"urteil": u1, "werte": {
        "n_s_N1e5": ns5, "n_s_N1e4_gegenprobe": ns4, "gegenprobe_urteil": u1_gegen, "proben_1e5": prob5.shape[1],
        "proben_1e4": prob4.shape[1], "geometrie_fehler_saaten": fehl5 + fehl4, "mu_max": max(mu5, mu4)}}
    if u1_gegen != u1:
        erg["urteile"]["SZ1"]["vermerk"] = "Gegenprobe N = 1e4 gibt ein anderes Urteil"

    # ---------------- SZ2
    Wr = sum(float(np.sum(s["spektral"]["W_richtig"])) for s in n4)
    Wf = sum(float(np.sum(s["spektral"]["W_falsch"])) for s in n4)
    nw = sum(s["spektral"]["zahl_wellen"] for s in n4)
    mus = max(s["spektral"]["mu_max_betrag"] for s in n4)
    F = Wr / (Wr + Wf)
    mittel_w = (Wr + Wf) / nw
    if mus > WAECHTER or mittel_w < 0.05 or fehl4:
        u2 = "nicht auswertbar"
    else:
        u2 = "eingetroffen" if F >= 0.9 else "nicht eingetroffen"
    je_saat = [{"saat": s["saat"], "F": s["spektral"]["F_fenster"], "W": s["spektral"]["W_fenster_summe"],
                "G_mittel": float(np.mean(s["spektral"]["G_richtig"])),
                "v_spitze_median": float(np.median(s["spektral"]["v_spitze"]))} for s in n4]
    G_alle = np.concatenate([np.asarray(s["spektral"]["G_richtig"]) for s in n4])
    erg["urteile"]["SZ2"] = {"urteil": u2, "werte": {
        "F_W": F, "W_richtig": Wr, "W_falsch": Wf, "wellen": nw, "mittleres_fenstergewicht": mittel_w,
        "je_saat": je_saat, "G_richtig_min": float(G_alle.min()), "G_richtig_mittel": float(G_alle.mean()),
        "mu_max": mus, "kontrolle_K4": {x: kon["K4_dicht_2000"][x] for x in ("F_eigen", "F_kpm", "F_abw",
                                                                            "gehalt_fenster_summe", "W_kpm_summe")},
        "kubisch_L22_F": g22["spektral"]["F_fenster"]}}

    # ---------------- SZ3
    r5, se5, R5 = rho0(eps5, prob5)
    r4, se4, R4 = rho0(eps4, prob4)
    if not ok1:
        u3 = "nicht auswertbar"
    elif r5 < 3 * RHO_K or (r5 - RHO_K) < 3 * se5:
        u3 = "nicht eingetroffen"
    elif 0.5 <= r4 / r5 <= 2.0:
        u3 = "eingetroffen"
    else:
        u3 = "nicht auswertbar"
    erg["urteile"]["SZ3"] = {"urteil": u3, "werte": {
        "rho0_N1e5": r5, "rho0_se_N1e5": se5, "rho0_N1e4": r4, "rho0_se_N1e4": se4, "rho_K": RHO_K,
        "verhaeltnis_1e4_zu_1e5": r4 / r5, "fit_N1e5": fit_rho(E5, rho5), "fit_N1e4": fit_rho(E4, rho4),
        "proben": [R5, R4]}}

    # ---------------- beschreibend
    besch = {}
    besch["asymmetrie_rho_max_rel_N1e5"] = asymmetrie(E5, rho5)
    besch["asymmetrie_rho_max_rel_L46"] = asymmetrie(np.asarray(k["E"]), np.asarray(k["rho_mittel"]))
    sp5 = [s["spektral"] for s in n5 if "spektral" in s]
    v5 = {}
    for s in sp5:
        for mm, vv, hh in zip(s["m"], s["v_spitze"], s["h"]):
            key = str(tuple(int(x) for x in mm))
            v5.setdefault(key, []).append(vv)
    besch["v_spitze_N1e5_je_m"] = {k_: float(np.mean(v)) for k_, v in v5.items()}
    besch["G_richtig_N1e5"] = float(np.mean(np.concatenate([np.asarray(s["G_richtig"]) for s in sp5]))) if sp5 else None
    besch["F_W_N1e5_auswahl"] = float(sum(np.sum(s["W_richtig"]) for s in sp5) / sum(
        np.sum(s["W_richtig"]) + np.sum(s["W_falsch"]) for s in sp5)) if sp5 else None
    besch["kubisch_L46_v_spitze"] = {str(tuple(int(x) for x in mm)): float(v) for mm, v in
                                     zip(g46["spektral"]["m"], g46["spektral"]["v_spitze"])}
    besch["kubisch_L46_G_mittel"] = float(np.mean(g46["spektral"]["G_richtig"]))
    besch["K4"] = {x: kon["K4_dicht_2000"][x] for x in ("ipr_median_alle", "tiefste", "zahl_fenster", "spektrum")}
    besch["geometrie_1e5"] = [{x: s["pruefung"][x] for x in ("T", "E", "grad_mittel", "M_eigen_streuung_rms",
                                                             "abschluss_max_rel", "volumen_summe_rel",
                                                             "M_durch_V_volumengewichtet", "sek")} for s in n5]
    erg["beschreibend"] = besch
    with open(os.path.join(ordner, "auswertung.json"), "w") as f:
        json.dump(erg, f, indent=1)
    for nr, u in erg["urteile"].items():
        print(nr, u["urteil"], flush=True)

    # ---------------- Bilder
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    Ek = np.asarray(k["E"])
    selp = (Ek > 0.005) & (Ek <= 0.6)
    ax[0].semilogy(Ek[selp], np.asarray(k["rho_mittel"])[selp], color="#1f5fa8", label="kubisch L = 46 (KPM)")
    ax[0].semilogy(E5[selp], rho5[selp], color="#c0392b", label="Zufallsnetz N = 1e5 (KPM, 2 Saaten)")
    ax[0].semilogy(E4[selp], rho4[selp], color="#e08a7f", ls="--", label="Zufallsnetz N = 1e4 (4 Saaten)")
    ee = Ek[selp]
    ax[0].semilogy(ee, ee ** 2 / (2 * math.pi ** 2), color="k", ls=":", label="1 Weyl-Kegel E^2/(2 pi^2)")
    ax[0].semilogy(ee, 8 * ee ** 2 / (2 * math.pi ** 2), color="#1f5fa8", ls=":", label="8 Kegel")
    ax[0].set_xlabel("E")
    ax[0].set_ylabel("rho(E) je Knoten und Energie")
    ax[0].set_title("Zustandsdichte nahe E = 0 (verdrillungsgemittelt)")
    ax[0].legend(fontsize=8)
    for lab, prob_, col in (("kubisch L = 46", prob, "#1f5fa8"), ("Zufallsnetz N = 1e5", prob5, "#c0392b"),
                            ("Zufallsnetz N = 1e4", prob4, "#e08a7f")):
        epsa = np.asarray(k["eps"])
        nsv = prob_.mean(axis=1) * 3 * math.pi ** 2 / epsa ** 3
        ax[1].semilogy(epsa, nsv, color=col, label=lab)
    ax[1].axhline(1, color="k", ls=":", label="1 Kegel")
    ax[1].axhline(8, color="#1f5fa8", ls=":", label="8 Kegel")
    ax[1].axhspan(2 / 3, 1.5, color="0.85", label="SZ1-Band [2/3; 1,5]")
    ax[1].axvspan(0.2, 0.4, color="#fff3c4", alpha=0.6, label="Urteilsfenster")
    ax[1].set_xlabel("eps")
    ax[1].set_ylabel("n_s(eps) = n(|E|<eps) 3 pi^2/eps^3")
    ax[1].set_title("Zahl der Kegel aus der Zaehlung")
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "bild-zustandsdichte.png"), dpi=130)
    plt.close(fig)

    # Helizitaetsanteil gegen Energie aus den Schalen-Spektralfunktionen
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    Esp = np.asarray(kon["K4_dicht_2000"]["bins"][0]["E"]) if False else None
    for lab, liste, col in (("Zufallsnetz N = 1e4 (4 Saaten)", [s["spektral"] for s in n4], "#c0392b"),
                            ("kubisch L = 22", [g22["spektral"]], "#1f5fa8")):
        Eg = np.round(np.arange(-1.5, 1.50001, 0.005), 4)
        rich = np.zeros(Eg.size)
        tot = np.zeros(Eg.size)
        for s in liste:
            for key, val in s["schalen"].items():
                hh = int(key.split("_")[1])
                A = np.asarray(val["A"]) * val["anzahl"]
                tot += A
                rich += np.where((Eg > 0) == (hh < 0), A, 0.0)
        frac = np.where(tot > 1e-3 * tot.max(), rich / np.maximum(tot, 1e-300), np.nan)
        selh = np.abs(Eg) <= 1.0
        ax[0].plot(Eg[selh], frac[selh], color=col, label=lab)
    ax[0].axhline(0.9, color="k", ls=":", label="SZ2-Schwelle 0,9")
    ax[0].axvspan(-0.35, 0.35, color="#fff3c4", alpha=0.6, label="unterstes Fenster |E| <= 0,35")
    ax[0].set_ylim(0, 1.05)
    ax[0].set_xlabel("E")
    ax[0].set_ylabel("Anteil richtige Helizitaet (Ebene Wellen |k| <= 0,5)")
    ax[0].set_title("Helizitaetsanteil gegen Energie")
    ax[0].legend(fontsize=8)
    s0 = n4[0]["spektral"]
    for key, val in s0["schalen"].items():
        hh = int(key.split("_")[1])
        if hh < 0 and val["anzahl"] >= 2:
            ax[1].plot(Eg, val["A"], label=f"|k| = {val['k_mittel']:.3f}, h = -1 (Saat {n4[0]['saat']})")
            ax[1].axvline(val["k_mittel"], color="0.6", ls=":")
    ax[1].set_xlim(-1.0, 1.0)
    ax[1].set_xlabel("E")
    ax[1].set_ylabel("Spektralfunktion A_k,h(E)")
    ax[1].set_title("Ebene Welle: scharfe Spitze bei E = v|k| (Linien: |k|)")
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "bild-helizitaet.png"), dpi=130)
    plt.close(fig)

    # K4: IPR und Ebene-Wellen-Gehalt gegen Energie (dicht, N = 2000)
    b = kon["K4_dicht_2000"]["bins"]
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))
    ax[0].plot([x["E"] for x in b], [x["anzahl"] / (0.1 * 2000) for x in b], "o-", color="#c0392b")
    ax[0].set_xlabel("E")
    ax[0].set_ylabel("Zustaende je Knoten und Energie (dicht, N = 2000)")
    ax[0].set_title("Volles Spektrum, Zufallsnetz N = 2000 (Kontrolle K4)")
    ax2 = ax[1]
    ax2.semilogy([x["E"] for x in b], [x["ipr_median"] for x in b], "o-", color="#555", label="IPR-Median x N")
    ax2.semilogy([x["E"] for x in b], [max(x["gehalt_summe"], 1e-6) for x in b], "s-", color="#1f5fa8",
                 label="Ebene-Wellen-Gehalt (Summe je Bin, |k| <= 0,75)")
    ax2.set_xlabel("E")
    ax2.legend(fontsize=8)
    ax2.set_title("Lokalisierung und langwelliger Gehalt")
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "bild-k4-spektrum.png"), dpi=130)
    plt.close(fig)
    print("Bilder geschrieben", flush=True)


if __name__ == "__main__":
    main()
