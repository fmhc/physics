#!/usr/bin/env python3
"""REGGE-4D-1: mechanische Urteile G0 bis G3 nach PLAN.md (Abschnitt 7) und Bilder.

Aufruf: python regge4d_auswertung.py <haupt.json> <auswertung.json> <bildordner> [probe3d]
  probe3d: nur Probe des Auswertungscodes auf den 3D-Daten (Rauchlauf); ergibt keine Urteile zur Karte.
"""
import json
import sys

import numpy as np

FLACH = 1e-12          # Karte G0
HERM = 1e-8            # PLAN [F10]
NULL_REL = 1e-6        # Karte G1
G1_SKAL = 0.10         # PLAN [F11]: k^2-Skalierung der Kontinuumsmoden
G1_GITTER = (0.5, 2.0)  # PLAN [F11]: Gittermoden O(1)
G2_TOL = 0.10          # Karte G2
G3_TOL = 0.05          # Karte G3
KLEIN = [0.05, 0.1, 0.2]
# Erwartungen der Karte (n = 4); n = 3 nur fuer die Probe des Codes (Kontinuum d = 3)
ERW = {"n4": {"k0_null": 10, "null_ok": (4, 5), "kont_pos": 5, "kont_neg": 1, "ratio": -2.0},
       "n3": {"k0_null": 6, "null_ok": (3, 4), "kont_pos": 2, "kont_neg": 1, "ratio": -1.0}}


def urteile(d, key):
    nd = d[key]
    e = ERW[key]
    out = {}
    if "abbruch" in nd:
        for g in ("G0", "G1", "G2", "G3"):
            out[g] = {"urteil": "nicht auswertbar", "vermerk": nd["abbruch"], "werte": {}}
        return out, {}
    pk = nd["punkte"]
    p0 = [p for p in pk if p["betrag_nominal"] == 0.0][0]
    rest = [p for p in pk if p["betrag_nominal"] > 0.0]
    # ---------------- G0
    herm = max(nd["hermitesch_zufall_max_rel"], nd["hermitesch_leiter_max_rel"])
    g0w = {
        "max_abs_eps": nd["flach_max_abs_eps"],
        "hermitesch_max_rel": herm,
        "k0_nullmoden": p0["n_null"],
        "k0_affin_residuum_rel": nd["k0_affin_residuum_rel"],
        "k0_top_residuum_rel": nd["k0_top_residuum_rel"],
        "k0_nullraum_ausserhalb_affin_singulaerwerte": nd["k0_nullraum_ausserhalb_affin_singulaerwerte"],
        "k0_eigenwerte": p0["eigenwerte"],
    }
    teil = {
        "flach": nd["flach_max_abs_eps"] < FLACH,
        "hermitesch": herm < HERM,
        "k0_genau_affin": p0["n_null"] == e["k0_null"] and nd["k0_affin_residuum_rel"] < NULL_REL,
    }
    g0w["teilpruefungen"] = teil
    out["G0"] = {"urteil": "eingetroffen" if all(teil.values()) else "nicht eingetroffen", "werte": g0w}
    # ---------------- G1
    zaehl_ok = all(p["n_null"] in e["null_ok"] for p in rest)
    eich_ok = all(p["eich_residuum_rel"] < NULL_REL for p in rest)
    kont_ok = all(p["n_kont_pos"] == e["kont_pos"] and p["n_kont_neg"] == e["kont_neg"] for p in rest)
    skal, gitt = {}, {}
    skal_ok = True
    gitt_ok = True
    for r in sorted(set(p["richtung"] for p in rest)):
        q = {p["betrag_nominal"]: p for p in rest if p["richtung"] == r}
        ref = q[0.05]
        x0 = np.array(ref["kont_werte"]) / 0.05 ** 2
        g0 = np.array(ref["gitter_werte"])
        sk, gk = [], []
        for b in (0.1, 0.2):
            x = np.array(q[b]["kont_werte"]) / b ** 2
            if len(x) != len(x0) or len(x) == 0:
                skal_ok = False
                sk.append(None)
            else:
                dev = float(np.max(np.abs(x / x0 - 1)))
                sk.append(dev)
                skal_ok &= dev <= G1_SKAL
            g = np.array(q[b]["gitter_werte"])
            if len(g) != len(g0) or len(g) == 0:
                gitt_ok = False
                gk.append(None)
            else:
                rat = g / g0
                gk.append([float(rat.min()), float(rat.max())])
                gitt_ok &= bool(np.all((rat >= G1_GITTER[0]) & (rat <= G1_GITTER[1])))
        skal[r] = sk
        gitt[r] = gk
    tab = [{"richtung": p["richtung"], "betrag": p["betrag_nominal"], "null": p["n_null"], "kont+": p["n_kont_pos"],
            "kont-": p["n_kont_neg"], "gitter+": p["n_gitter_pos"], "gitter-": p["n_gitter_neg"],
            "eich_res": p["eich_residuum_rel"], "top_res": p["top_residuum_rel"],
            "null_ausserhalb_eich_top": p.get("nullraum_ausserhalb_eich_top"),
            "kont_werte": p["kont_werte"], "gitter_werte": p["gitter_werte"]} for p in rest]
    teil1 = {"null_zahl": zaehl_ok, "eichmoden_null": eich_ok, "kont_vorzeichen": kont_ok,
             "k2_skalierung": skal_ok, "gitter_O1": gitt_ok}
    out["G1"] = {"urteil": "eingetroffen" if all(teil1.values()) else "nicht eingetroffen",
                 "werte": {"teilpruefungen": teil1, "skalierung_max_rel_0p1_0p2": skal,
                           "gitter_verhaeltnis_0p1_0p2_min_max": gitt,
                           "nullmoden_je_punkt": sorted(set(p["n_null"] for p in rest)), "zaehlung": tab}}
    # ---------------- G2
    rr = {}
    ok2 = True
    for p in rest:
        if p["betrag_nominal"] in KLEIN:
            r = p["form_schur"]["verhaeltnis_0s_2"]
            rr.setdefault(p["richtung"], {})[str(p["betrag_nominal"])] = r
            ok2 &= (r is not None) and abs(r / e["ratio"] - 1) <= G2_TOL
    devs = [abs(v / e["ratio"] - 1) for x in rr.values() for v in x.values() if v is not None]
    out["G2"] = {"urteil": "eingetroffen" if ok2 else "nicht eingetroffen",
                 "werte": {"verhaeltnis_c0s_c2": rr, "ziel": e["ratio"], "max_rel_abw_vom_ziel": float(max(devs))}}
    # ---------------- G3
    ok3 = True
    g3w = {}
    for b in KLEIN:
        X = np.array([v for p in rest if p["betrag_nominal"] == b for v in p["form_schur"]["spin2_eigenwerte"]])
        xm = float(X.mean())
        dev = float(np.max(np.abs(X / xm - 1)))
        je = {}
        for p in rest:
            if p["betrag_nominal"] == b:
                s = np.array(p["form_schur"]["spin2_eigenwerte"])
                je[p["richtung"]] = [float(s.min()), float(s.max()), float(s.mean())]
        g3w[str(b)] = {"mittel": xm, "max_abw": dev, "min": float(X.min()), "max": float(X.max()),
                       "je_richtung_min_max_mittel": je}
        ok3 &= dev <= G3_TOL
    out["G3"] = {"urteil": "eingetroffen" if ok3 else "nicht eingetroffen", "werte": g3w}
    # ---------------- beschreibend
    besch = {}
    for p in rest:
        f = p["form_schur"]
        fd = p["form_direkt"]
        besch.setdefault(p["richtung"], {})[str(p["betrag_nominal"])] = {
            "c2": f["c2"], "c1": f["c1"], "c0s": f["c0s"], "c0w": f["c0w"], "c0sw": f["c0sw"],
            "r": f["verhaeltnis_0s_2"], "spin2": f["spin2_eigenwerte"], "spin1": f["spin1_eigenwerte"],
            "mischung": f["mischung"], "abw_EH_fest": f["abweichung_EH_fest_1_4"],
            "abw_EH_normiert": f["abweichung_EH_normiert"], "eich_kont": f["kontinuums_eich_residuum_rel"],
            "eigenwerte_K_durch_k2": f["eigenwerte_durch_k2"],
            "direkt_c2": fd["c2"], "direkt_r": fd["verhaeltnis_0s_2"], "schur_minus_direkt": p["schur_minus_direkt_rel"],
            "Kww": p["Kww_eigenwerte"], "Kww_verworfen": p["Kww_verworfen"]}
    return out, besch


def bilder(d, key, ordner):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    nd = d[key]
    e = ERW[key]
    kurven = nd["kurven"]
    namen = list(kurven)
    fig, axs = plt.subplots(2, 4, figsize=(17, 8.5), sharex=True, sharey=True)
    for ax, r in zip(axs.ravel(), namen):
        c = kurven[r]
        b = np.array(c["betrag"])
        ev = np.array(c["eigenwerte"])
        kl = np.array(c["klasse"])
        bb = np.repeat(b[:, None], ev.shape[1], axis=1)
        for kla, vz, farbe, lab in (("k", 1, "tab:blue", "Kontinuum +"), ("k", -1, "tab:red", "Kontinuum -"),
                                    ("g", 1, "0.45", "Gitter +"), ("g", -1, "tab:purple", "Gitter -")):
            m = (kl == kla) & (np.sign(ev) == vz)
            ax.loglog(bb[m], np.abs(ev[m]), ".", color=farbe, ms=3.5, label=lab)
        ax.loglog(b, 0.05 * b ** 2, "k--", lw=0.8, label="~ k^2")
        ax.axvspan(0.05, 0.4, color="0.92", zorder=0)
        ax.set_title(r)
        ax.set_xlabel("|k|")
    axs[0, 0].set_ylabel("|Eigenwert| von H(k), Variablen s = l^2")
    axs[1, 0].set_ylabel("|Eigenwert| von H(k), Variablen s = l^2")
    axs[0, 0].legend(fontsize=8)
    fig.suptitle(f"REGGE-4D-1 ({key}): Spektrum von H(k) = -M(k); Nullmoden nicht gezeigt; grau hinterlegt 0,05 bis 0,4")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-eigenwerte-{key}.png", dpi=110)
    plt.close(fig)
    fig, axs = plt.subplots(1, 3, figsize=(17, 5))
    for r in namen:
        c = kurven[r]
        axs[0].semilogx(c["betrag"], c["c2"], "-", label=r)
        axs[1].semilogx(c["betrag"], c["r"], "-", label=r)
    axs[0].axhline(0.25, color="k", ls="--", lw=0.8)
    axs[0].set_title("Spin-2-Koeffizient c2 (Schur-Form), Erwartung 1/4")
    axs[1].axhline(e["ratio"], color="k", ls="--", lw=0.8)
    axs[1].axhspan(e["ratio"] * 1.1, e["ratio"] * 0.9, color="0.9")
    axs[1].set_title(f"Verhaeltnis c0s/c2, Erwartung {e['ratio']} (Band +-10 %)")
    for ax in axs[:2]:
        ax.axvline(0.2, color="0.6", lw=0.8)
        ax.set_xlabel("|k|")
    axs[0].legend(fontsize=7)
    pk = [p for p in nd["punkte"] if p["betrag_nominal"] > 0]
    for i, b in enumerate([0.05, 0.1, 0.2, 0.4]):
        X = [(j, v) for j, r in enumerate(namen) for p in pk if p["richtung"] == r and p["betrag_nominal"] == b
             for v in p["form_schur"]["spin2_eigenwerte"]]
        xs = np.array([x[0] for x in X]) + (i - 1.5) * 0.15
        axs[2].plot(xs, [x[1] for x in X], "o", ms=3.5, label=f"|k| = {b}")
    axs[2].axhline(0.25, color="k", ls="--", lw=0.8)
    axs[2].axhspan(0.25 * 0.95, 0.25 * 1.05, color="0.9")
    axs[2].set_xticks(range(len(namen)))
    axs[2].set_xticklabels(namen, rotation=40, fontsize=7)
    axs[2].set_title("Spin-2-Block: Eigenwerte / k^2 je Richtung (Band +-5 % um 1/4)")
    axs[2].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-koeffizienten-{key}.png", dpi=110)
    plt.close(fig)


def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    probe = len(sys.argv) > 4 and sys.argv[4] == "probe3d"
    key = "n3" if probe else "n4"
    u, besch = urteile(d, key)
    erg = {"hinweis": "PROBE des Auswertungscodes auf 3D-Daten, keine Urteile zur Karte" if probe else
           "Urteile nach PLAN.md Abschnitt 7", "urteile": u, "beschreibend": besch}
    if not probe:
        u3, b3 = urteile(d, "n3")
        erg["kontrolle_3d_regeln_d3"] = u3
        erg["kontrolle_3d_beschreibend"] = b3
        erg["kontrollen_4d"] = {k: v for k, v in d["n4"].items() if k not in ("kurven", "punkte")}
        erg["kontrollen_3d"] = {k: v for k, v in d["n3"].items() if k not in ("kurven", "punkte")}
        erg["kontrolle_L3"] = d.get("n4_L3")
    with open(sys.argv[2], "w") as f:
        json.dump(erg, f, indent=1)
    for g, v in u.items():
        print(g, v["urteil"])
    bilder(d, key, sys.argv[3])
    if not probe:
        bilder(d, "n3", sys.argv[3])
    print("Bilder geschrieben")


if __name__ == "__main__":
    main()
