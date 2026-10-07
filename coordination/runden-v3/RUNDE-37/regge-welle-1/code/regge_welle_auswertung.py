#!/usr/bin/env python3
"""REGGE-WELLE-1: mechanische Urteile W0 bis W3 nach PLAN.md (Abschnitt 6) und Bilder.

Aufruf: python regge_welle_auswertung.py <haupt.json> <auswertung.json> <bildordner> [probe]
  probe: Probe des Auswertungscodes auf Rauchdaten (andere Betraege); ergibt keine Urteile zur Karte.
"""
import json
import sys

import numpy as np

W0_A, W0_B = 1e-12, 1e-10        # Karte W0
W1_TOL = 0.005                   # Karte W1
W2_ABW, W2_STREU = 0.01, 0.001   # Karte W2
W3_ENT = 1e-3                    # Karte W3
LK = (0.5, 1.5)                  # Lichtkegel-Fenster Re omega/|k| (PLAN [F5])
RHO_MIN, S_WURZEL, PHYS_MIN, PHASE_MAX, WIND_REST, RES_SPERRE = 0.05, 1e-9, 0.1, 0.5, 0.05, 1e-8
TT_MIN, KIN_LUECKE, KIN_LS = 0.95, 0.1, 0.9      # Tor fuer W3 (PLAN [F9])
ENTARTET_EXAKT = 1e-6


def sperren(p):
    w = p["windung"]
    f = {"windung_unsauber": w["rest"] > WIND_REST or w["max_phasensprung"] >= PHASE_MAX,
         "zahl_ungleich": w["zahl"] != len(p["nullstellen"]),
         "wurzel_unverifiziert": any(x["s"] > S_WURZEL for x in p["nullstellen"]),
         "komplement_oder_unphysikalisch": any(x["rho"] < RHO_MIN or x["physikalisch"] < PHYS_MIN
                                               for x in p["nullstellen"]),
         "rand_rho": w["rho_rand_min"] < RHO_MIN,
         "null_residuum": p["achse"]["null_residuum_max"] > RES_SPERRE}
    return f, any(f.values())


def lk(p):
    return [x for x in p["nullstellen"] if LK[0] <= x["v_re"] <= LK[1]]


def cluster(zs, tol):
    """Single-Linkage-Gruppen komplexer Zahlen mit Abstand <= tol; Rueckgabe: Liste von Indexlisten."""
    n = len(zs)
    eltern = list(range(n))

    def wurzel(i):
        while eltern[i] != i:
            eltern[i] = eltern[eltern[i]]
            i = eltern[i]
        return i
    for i in range(n):
        for j in range(i + 1, n):
            if abs(zs[i] - zs[j]) <= tol:
                eltern[wurzel(i)] = wurzel(j)
    gr = {}
    for i in range(n):
        gr.setdefault(wurzel(i), []).append(i)
    return list(gr.values())


def dreiwertig(verletzt_frei, gesperrt):
    if verletzt_frei:
        return "nicht eingetroffen"
    if gesperrt:
        return "nicht auswertbar"
    return "eingetroffen"


def urteile(d, betr):
    b_w1, b_w2, b_w3 = betr["w1"], betr["w2"], betr["w3"]
    P = d["punkte"]
    sp = {(p["richtung"], p["betrag"]): sperren(p) for p in P}
    out, kw = {}, {}
    # ---------------- W0
    resid = [p["achse"]["null_residuum_max"] for p in P]
    w0w = {"a_max": d["w0"]["a_max"], "a_punkte": d["w0"]["a_punkte"], "b_zufall_max": d["w0"]["b_zufall_max"],
           "b_achse_max": float(max(resid)), "symmetrie_max": float(max(p["achse"]["symmetrie_max"] for p in P))}
    ok0 = d["w0"]["a_max"] <= W0_A and max(d["w0"]["b_zufall_max"], max(resid)) <= W0_B
    out["W0"] = {"urteil": "eingetroffen" if ok0 else "nicht eingetroffen", "werte": w0w}
    # ---------------- W1
    vf, vf_kw, ges = False, False, False
    tab1 = []
    for p in P:
        if p["betrag"] not in b_w1:
            continue
        f, g = sperren(p)
        abw = [abs(complex(x["v_re"], x["v_im"]) - 1) for x in p["nullstellen"]]
        abw_re = [abs(x["v_re"] - 1) for x in p["nullstellen"]]
        verl = len(abw) == 0 or max(abw) > W1_TOL
        verl_kw = len(abw) == 0 or max(abw_re) > W1_TOL
        if g:
            ges = True
        else:
            vf |= verl
            vf_kw |= verl_kw
        tab1.append({"richtung": p["richtung"], "betrag": p["betrag"], "zahl": len(abw),
                     "max_abw_komplex": max(abw) if abw else None, "max_abw_re": max(abw_re) if abw else None,
                     "gesperrt": g, "sperren": f})
    out["W1"] = {"urteil": dreiwertig(vf, ges), "werte": {"punkte": tab1,
                 "max_abw_komplex": max([t["max_abw_komplex"] or 0 for t in tab1]),
                 "max_abw_re": max([t["max_abw_re"] or 0 for t in tab1]),
                 "zahlen": sorted(set(t["zahl"] for t in tab1))}}
    kw["W1"] = dreiwertig(vf_kw, ges)
    # ---------------- W2
    vf, vf_kw, ges = False, False, False
    vmit = {}
    tab2 = []
    for p in P:
        if p["betrag"] != b_w2:
            continue
        f, g = sperren(p)
        z = lk(p)
        abw = [abs(complex(x["v_re"], x["v_im"]) - 1) for x in z]
        abw_re = [abs(x["v_re"] - 1) for x in z]
        verl = len(z) == 0 or min(abw) < W2_ABW
        verl_kw = len(z) == 0 or min(abw_re) < W2_ABW
        if g:
            ges = True
        else:
            vf |= verl
            vf_kw |= verl_kw
            if z:
                vmit[p["richtung"]] = float(np.mean([x["v_re"] for x in z]))
        tab2.append({"richtung": p["richtung"], "lk_zahl": len(z), "v_re": [x["v_re"] for x in z],
                     "v_im": [x["v_im"] for x in z], "min_abw_komplex": min(abw) if abw else None,
                     "min_abw_re": min(abw_re) if abw else None, "gesperrt": g})
    vals = np.array(list(vmit.values()))
    streu = float((vals.max() - vals.min()) / vals.mean()) if len(vals) else 0.0
    b_ok = streu >= W2_STREU

    def urteil_w2(verletzt_a):
        if verletzt_a:
            return "nicht eingetroffen"
        if ges:
            return "nicht auswertbar"
        return "eingetroffen" if b_ok else "nicht eingetroffen"
    abw_k = [t["min_abw_komplex"] for t in tab2 if t["min_abw_komplex"] is not None]
    abw_r = [t["min_abw_re"] for t in tab2 if t["min_abw_re"] is not None]
    out["W2"] = {"urteil": urteil_w2(vf),
                 "werte": {"punkte": tab2, "streuung_ueber_richtungen": streu, "v_mittel_je_richtung": vmit,
                           "teil_b_streuung_erfuellt": b_ok,
                           "min_abw_komplex": min(abw_k) if abw_k else None,
                           "min_abw_re": min(abw_r) if abw_r else None}}
    kw["W2"] = urteil_w2(vf_kw)
    # ---------------- W3: Tor (Polarisationen und Zwangsbedingungen identifiziert)
    tor = {"i_zwei_lk_klein": True, "ii_tt": True, "iii_zwei_lk_w3": True, "iv_kinetik": True, "keine_sperre": True}
    tor_det = []
    for p in P:
        if p["betrag"] in b_w1 or p["betrag"] == b_w3:
            f, g = sperren(p)
            z = lk(p)
            if g:
                tor["keine_sperre"] = False
            if p["betrag"] == b_w3:
                tor["iii_zwei_lk_w3"] &= len(z) == 2
                continue
            tor["i_zwei_lk_klein"] &= len(z) == 2
            tt_ok = all(x["tt_anteil"] >= TT_MIN for x in z)
            if len(z) == 2 and abs(complex(z[0]["re"], z[0]["im"]) - complex(z[1]["re"], z[1]["im"])) <= ENTARTET_EXAKT * p["betrag"]:
                tt_ok &= max(z[0]["tt_anteil_2"], z[1]["tt_anteil_2"]) >= TT_MIN
            tor["ii_tt"] &= tt_ok
            kin = p["kinetik"]
            tor["iv_kinetik"] &= kin["luecke_s4_durch_s3"] <= KIN_LUECKE and kin["lapse_shift_anteil_klein3"] >= KIN_LS
            tor_det.append({"richtung": p["richtung"], "betrag": p["betrag"], "lk_zahl": len(z),
                            "tt": [x["tt_anteil"] for x in z], "tt2": [x["tt_anteil_2"] for x in z],
                            "zeit_anteil": [x["zeit_anteil"] for x in z],
                            "kin_luecke": kin["luecke_s4_durch_s3"], "kin_ls": kin["lapse_shift_anteil_klein3"]})
    tor_ok = all(tor.values())
    tab3 = []
    vf, vf_kw = False, False
    for p in P:
        if p["betrag"] != b_w3:
            continue
        z = lk(p)
        zs = [complex(x["re"], x["im"]) for x in z]
        gr = cluster(zs, W3_ENT * p["betrag"])
        ok = any(len(g) == 2 for g in gr)
        vf |= not ok
        alle = [complex(x["re"], x["im"]) for x in p["nullstellen"]]
        gra = cluster(alle, W3_ENT * p["betrag"])
        ok_kw = len(gra) >= 2 and any(len(g) == 2 for g in gra)
        vf_kw |= not ok_kw
        spl = abs(zs[1] - zs[0]) / p["betrag"] if len(zs) == 2 else None
        tab3.append({"richtung": p["richtung"], "lk_zahl": len(z), "gruppen": [len(g) for g in gr],
                     "aufspaltung_rel": spl, "gruppen_alle": [len(g) for g in gra]})
    if not tor_ok:
        u3 = "nicht auswertbar"
    else:
        u3 = "eingetroffen" if not vf else "nicht eingetroffen"
    out["W3"] = {"urteil": u3, "werte": {"tor": tor, "tor_einzeln": tor_det, "punkte": tab3,
                                         "aufspaltung_max": max([t["aufspaltung_rel"] or 0 for t in tab3] or [0]),
                                         "aufspaltung_min": min([t["aufspaltung_rel"] for t in tab3
                                                                 if t["aufspaltung_rel"] is not None] or [None])}}
    kw["W3"] = ("eingetroffen" if not vf_kw else "nicht eingetroffen") if tor_ok else "nicht auswertbar"
    return out, kw, sp


def beschreibend(d):
    P = d["punkte"]
    idx = {(p["richtung"], p["betrag"]): p for p in P}
    tab = []
    for p in P:
        z = lk(p)
        tab.append({"richtung": p["richtung"], "betrag": p["betrag"], "zahl_R": len(p["nullstellen"]),
                    "windung": p["windung"]["windung"], "lk": [[x["v_re"], x["v_im"]] for x in z],
                    "andere_in_R": [[x["v_re"], x["v_im"]] for x in p["nullstellen"] if x not in z],
                    "geister": p["geister"], "achse_minima": p["achse"]["minima_fein"],
                    "zeitumkehr_max": p["achse"]["zeitumkehr_max"], "rho_achse_min": p["achse"]["rho_min"],
                    "rho_rand_min": p["windung"]["rho_rand_min"], "kinetik": p["kinetik"],
                    "tt": [x["tt_anteil"] for x in z], "gitter_rest": [x["gitter_rest"] for x in z],
                    "physikalisch": [x["physikalisch"] for x in z], "s": [x["s"] for x in z],
                    "pep": p["pep"], "aberth": p["aberth"]})
    # Symmetrie n gegen -n: vorwaerts-Nullstellen bei -n = konjugierte bei n
    paare = [("x+", "x-"), ("xy+", "xy-"), ("xyz+", "xyz-"), ("xy-z", "-x-yz"), ("123", "-1-2-3")]
    sym = []
    for a, b in paare:
        for kb in sorted(set(p["betrag"] for p in P)):
            if (a, kb) in idx and (b, kb) in idx:
                za = sorted([complex(x["re"], -x["im"]) for x in idx[(a, kb)]["nullstellen"]], key=lambda c: (c.real, c.imag))
                zb = sorted([complex(x["re"], x["im"]) for x in idx[(b, kb)]["nullstellen"]], key=lambda c: (c.real, c.imag))
                if len(za) == len(zb) and za:
                    sym.append({"paar": [a, b], "betrag": kb,
                                "max_abw_rel": float(max(abs(u - v) for u, v in zip(za, zb)) / kb)})
                else:
                    sym.append({"paar": [a, b], "betrag": kb, "zahlen": [len(za), len(zb)]})
    s3 = []
    for kb in sorted(set(p["betrag"] for p in P)):
        if ("123", kb) in idx and ("312", kb) in idx:
            za = sorted([complex(x["re"], x["im"]) for x in idx[("123", kb)]["nullstellen"]], key=lambda c: (c.real, c.imag))
            zb = sorted([complex(x["re"], x["im"]) for x in idx[("312", kb)]["nullstellen"]], key=lambda c: (c.real, c.imag))
            if len(za) == len(zb) and za:
                s3.append({"betrag": kb, "max_abw_rel": float(max(abs(u - v) for u, v in zip(za, zb)) / kb)})
    gk = []
    for g in d.get("gegenprobe_weg_K", []):
        p = idx.get((g["richtung"], g["betrag"]))
        if p is None:
            continue
        zt = sorted([complex(x["re"], x["im"]) for x in p["nullstellen"]], key=lambda c: (c.real, c.imag))
        zk = sorted([complex(a, b) for a, b in g["nullstellen"]], key=lambda c: (c.real, c.imag))
        gk.append({"richtung": g["richtung"], "betrag": g["betrag"], "zahlen": [len(zt), len(zk)],
                   "max_abw_rel": float(max(abs(u - v) for u, v in zip(zt, zk)) / g["betrag"]) if len(zt) == len(zk) and zt else None})
    return {"tabelle": tab, "symmetrie_n_gegen_minus_n": sym, "s3_kopie_123_312": s3, "gegenprobe_weg_K": gk,
            "zeitumkehr_max": float(max(p["achse"]["zeitumkehr_max"] for p in P)),
            "geometrie": d["geometrie"]}


def bilder(d, ordner, betraege):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    P = d["punkte"]
    namen = []
    for p in P:
        if p["richtung"] not in namen:
            namen.append(p["richtung"])
    farben = plt.cm.viridis(np.linspace(0, 0.95, len(namen)))
    sym_namen = {"x+", "x-", "xy+", "xy-", "x-y", "xyz+", "xyz-", "xy-z", "-x-yz", "123", "312", "-1-2-3"}
    # 1: Geschwindigkeit
    fig, axs = plt.subplots(1, 3, figsize=(19, 6))
    for c, r in zip(farben, namen):
        pk = sorted([p for p in P if p["richtung"] == r], key=lambda p: p["betrag"])
        for j in range(2):
            b = [p["betrag"] for p in pk if len(lk(p)) > j]
            v = [sorted(lk(p), key=lambda x: x["v_re"])[j]["v_re"] for p in pk if len(lk(p)) > j]
            vi = [sorted(lk(p), key=lambda x: x["v_re"])[j]["v_im"] for p in pk if len(lk(p)) > j]
            ls = "-" if r in sym_namen else ":"
            axs[0].semilogx(b, v, ls, marker="o" if j == 0 else "s", ms=3, color=c, label=r if j == 0 else None)
            axs[1].semilogx(b, vi, ls, marker="o" if j == 0 else "s", ms=3, color=c)
    axs[0].axhline(1.0, color="k", lw=0.8)
    axs[0].axhspan(1 - W1_TOL, 1 + W1_TOL, color="0.88")
    axs[0].set_title("Re omega / |k| der Lichtkegel-Nullstellen (Kreis: kleinere, Quadrat: groessere)")
    axs[1].axhline(0.0, color="k", lw=0.8)
    axs[1].set_yscale("symlog", linthresh=1e-6)
    axs[1].set_title("Im omega / |k| (Anwachsen bzw. Daempfung)")
    for ax in axs[:2]:
        ax.set_xlabel("|k| (Gittereinheiten)")
    axs[0].legend(fontsize=6, ncol=2)
    # dritte Tafel: Re omega/|k| je Richtung beim groessten Betrag
    bmax = max(betraege)
    for i, r in enumerate(namen):
        p = [q for q in P if q["richtung"] == r and q["betrag"] == bmax]
        if p:
            for x in lk(p[0]):
                axs[2].plot(i, x["v_re"], "o", color="tab:blue", ms=4)
    axs[2].axhline(1.0, color="k", lw=0.8)
    axs[2].set_xticks(range(len(namen)))
    axs[2].set_xticklabels(namen, rotation=60, fontsize=7)
    axs[2].set_title(f"Re omega/|k| je Richtung bei |k| = {bmax}")
    fig.suptitle("REGGE-WELLE-1: Nullstellen von det(Q0^T M(i omega, k) Q0), Zeitachse = Gitterachse 0")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-geschwindigkeit.png", dpi=110)
    plt.close(fig)
    # 2: Aufspaltung
    fig, axs = plt.subplots(1, 2, figsize=(15, 5.5))
    for c, r in zip(farben, namen):
        pk = sorted([p for p in P if p["richtung"] == r], key=lambda p: p["betrag"])
        b, sp = [], []
        for p in pk:
            z = lk(p)
            if len(z) == 2:
                b.append(p["betrag"])
                sp.append(max(abs(complex(z[0]["re"], z[0]["im"]) - complex(z[1]["re"], z[1]["im"])) / p["betrag"], 1e-17))
        axs[0].loglog(b, sp, "-o" if r in sym_namen else ":o", ms=3, color=c, label=r)
    axs[0].axhline(W3_ENT, color="r", ls="--", lw=0.8)
    axs[0].set_xlabel("|k|")
    axs[0].set_ylabel("|omega_1 - omega_2| / |k|")
    axs[0].set_title("Aufspaltung des Lichtkegel-Paars (rot: Schwelle W3 1e-3)")
    axs[0].legend(fontsize=6, ncol=2)
    b3 = sorted(set(p["betrag"] for p in P))
    b3 = [x for x in b3 if x >= 0.3][:1] if 0.4 not in b3 else [0.4]
    for i, r in enumerate(namen):
        p = [q for q in P if q["richtung"] == r and q["betrag"] == b3[0]]
        if p:
            z = lk(p[0])
            for x in z:
                axs[1].plot(x["v_re"], x["v_im"], "o", color=farben[i], ms=4)
    axs[1].set_xlabel("Re omega/|k|")
    axs[1].set_ylabel("Im omega/|k|")
    axs[1].set_title(f"Lichtkegel-Nullstellen in der komplexen Ebene, |k| = {b3[0]}")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-aufspaltung.png", dpi=110)
    plt.close(fig)
    # 3: reelle Achse s(omega) und Eigenwerte von M
    zeig = [r for r in ("x+", "xyz+", "x-y", "fib05") if r in namen]
    bb = sorted(set(p["betrag"] for p in P))
    fig, axs = plt.subplots(2, len(bb), figsize=(4.2 * len(bb), 8), squeeze=False)
    for j, kb in enumerate(bb):
        for r in zeig:
            p = [q for q in P if q["richtung"] == r and q["betrag"] == kb][0]
            om = np.array(p["achse"]["omega"]) / kb
            axs[0, j].semilogy(om, p["achse"]["s"], "-", lw=1, label=r)
            if "eigen_M" in p and r in ("x+", "xyz+"):
                e = np.array(p["eigen_M"]["betrag_rel_sortiert"])
                o2 = np.array(p["eigen_M"]["omega"]) / kb
                for q in range(5, 15):
                    axs[1, j].semilogy(o2, e[:, q], "-", lw=0.8, color="tab:blue" if r == "x+" else "tab:orange")
        axs[0, j].axvline(1.0, color="k", lw=0.6)
        axs[1, j].axvline(1.0, color="k", lw=0.6)
        axs[0, j].set_title(f"|k| = {kb}: s = sigma_min/sigma_max")
        axs[1, j].set_title(f"|k| = {kb}: |Eigenwerte| von M (ohne 5 Nullmoden)")
        axs[1, j].set_xlabel("omega/|k| (reell)")
    axs[0, 0].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-achse.png", dpi=100)
    plt.close(fig)


def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    probe = len(sys.argv) > 4 and sys.argv[4] == "probe"
    if probe:
        betr = {"w1": [0.3], "w2": 0.6, "w3": 0.6}
    else:
        betr = {"w1": [0.05, 0.1], "w2": 0.8, "w3": 0.4}
    u, kw, sp = urteile(d, betr)
    erg = {"hinweis": "PROBE des Auswertungscodes auf Rauchdaten (|k| = 0,3/0,6), keine Urteile zur Karte" if probe
           else "Urteile nach PLAN.md Abschnitt 6", "urteile": u, "kartenwortlaut": kw,
           "sperren": {f"{a}|{b}": v[0] for (a, b), v in sp.items() if v[1]},
           "beschreibend": beschreibend(d), "w0_rohdaten": d["w0"]}
    with open(sys.argv[2], "w") as f:
        json.dump(erg, f, indent=1)
    for g, v in u.items():
        print(g, v["urteil"], "| Kartenwortlaut:", kw.get(g, "-"))
    bilder(d, sys.argv[3], [0.3, 0.6] if probe else [0.05, 0.1, 0.2, 0.4, 0.8])
    print("Bilder geschrieben")


if __name__ == "__main__":
    main()
