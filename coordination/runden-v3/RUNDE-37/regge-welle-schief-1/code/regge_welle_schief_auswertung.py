#!/usr/bin/env python3
"""REGGE-WELLE-SCHIEF-1: mechanische Urteile WS0 bis WS5 nach PLAN.md (Abschnitt 6), Beschreibung und Bilder.

Aufruf: python regge_welle_schief_auswertung.py <s0.json> <s01.json> <s02.json> <referenz_welle1.json>
                                                 <auswertung.json> <bildordner> [probe]
  probe: Probe auf Rauchdaten (|k| = 0,3/0,6; Referenz = rauch2.json aus REGGE-WELLE-1); keine Urteile zur Karte.
"""
import json
import sys

import numpy as np

WS0_TOL = 1e-9          # Karte WS0
WS1_TOL = 1e-3          # Karte WS1
WS2_SPALT = 1e-4        # Karte WS2
WS4_IM = 1e-6           # Karte WS4
WS5_V = 1e-6            # Karte WS5
LK = (0.5, 1.5)         # Lichtkegel-Fenster Re omega/|k| (wie REGGE-WELLE-1 [F5])
RHO_MIN, S_WURZEL, PHYS_MIN, PHASE_MAX, WIND_REST, RES_SPERRE = 0.05, 1e-9, 0.1, 0.5, 0.05, 1e-8   # wie [F7]
G_A, G_B = 1e-12, 1e-10  # Formkontrolle G (wie W0 in REGGE-WELLE-1)
SS = ("0.0", "0.1", "0.2")


def g_ok(d):
    return d["g"]["a_max"] <= G_A and d["g"]["b_zufall_max"] <= G_B


def sperren(p, gok):
    w = p["windung"]
    f = {"windung_unsauber": w["rest"] > WIND_REST or w["max_phasensprung"] >= PHASE_MAX,
         "zahl_ungleich": w["zahl"] != len(p["nullstellen"]),
         "wurzel_unverifiziert": any(x["s"] > S_WURZEL for x in p["nullstellen"]),
         "komplement_oder_unphysikalisch": any(x["rho"] < RHO_MIN or x["physikalisch"] < PHYS_MIN
                                               for x in p["nullstellen"]),
         "rand_rho": w["rho_rand_min"] < RHO_MIN,
         "null_residuum": p["achse"]["null_residuum_max"] > RES_SPERRE,
         "formkontrolle_G": not gok}
    return f, any(f.values())


def lk(p):
    return [x for x in p["nullstellen"] if LK[0] <= x["v_re"] <= LK[1]]


def pol(p):
    """Die zwei Polarisationen: LK-Nullstellen; bei mehr als zwei die zwei mit dem groessten TT-Anteil (PLAN [F5])."""
    z = lk(p)
    if len(z) > 2:
        z = sorted(z, key=lambda x: -x["tt_anteil"])[:2]
    return sorted(z, key=lambda x: x["v_re"])


ZENSUS_PAAR_TOL = 1e-6   # PLAN [F6]: Kopien omega und omega -+ 2 pi i (dieselbe Gitterwelle)


def zensus_wellen(p):
    """Je Gitterwelle ein Eintrag: Kopien omega, omega -+ 2 pi i werden gepaart; Vertreter = Kopie mit dem groessten rho
    (regulaerstes Komplement). Fassung nach den Rauchlaeufen, vor dem Einfrieren (PLAN Abschnitt 9)."""
    Z = list(p.get("zensus", []))
    weg, out = set(), []
    for i, a in enumerate(Z):
        if i in weg:
            continue
        beste = a
        wa = complex(a["re"], a["im"])
        for j in range(i + 1, len(Z)):
            if j in weg:
                continue
            wb = complex(Z[j]["re"], Z[j]["im"])
            if any(abs(wa + sh - wb) <= ZENSUS_PAAR_TOL * (1 + abs(wa)) for sh in (2j * np.pi, -2j * np.pi)):
                weg.add(j)
                if Z[j].get("rho", 0.0) > beste.get("rho", 0.0):
                    beste = Z[j]
        out.append(beste)
    return out


def zensus(p):
    intr, schein, unklar = [], [], []
    for z in zensus_wellen(p):
        if z["s"] > S_WURZEL:
            unklar.append(z)
        elif z["rho"] < RHO_MIN or z["physikalisch"] < PHYS_MIN:
            schein.append(z)
        else:
            intr.append(z)
    return intr, schein, unklar


def kreuzung(p):
    return len(p.get("eukl_linie", {}).get("n_neg_werte", [0])) > 1


def dreiwertig(verletzt_frei, gesperrt):
    if verletzt_frei:
        return "nicht eingetroffen"
    if gesperrt:
        return "nicht auswertbar"
    return "eingetroffen"


def ws0(d0, ref):
    idx = {(p["richtung"], p["betrag"]): p for p in ref["punkte"]}
    tab, ok = [], True
    for p in d0["punkte"]:
        q = idx.get((p["richtung"], p["betrag"]))
        if q is None:
            continue
        a = sorted(p["nullstellen"], key=lambda x: (x["v_re"], x["v_im"]))
        b = sorted(q["nullstellen"], key=lambda x: (x["v_re"], x["v_im"]))
        gleich = len(a) == len(b) and p["windung"]["zahl"] == q["windung"]["zahl"]
        dv = max([abs(x["v_re"] - y["v_re"]) for x, y in zip(a, b)] + [0.0]) if gleich else None
        dc = max([abs(complex(x["v_re"], x["v_im"]) - complex(y["v_re"], y["v_im"])) for x, y in zip(a, b)]
                 + [0.0]) if gleich else None
        ok &= gleich and dv <= WS0_TOL
        tab.append({"richtung": p["richtung"], "betrag": p["betrag"], "zahlen": [len(a), len(b)],
                    "windung": [p["windung"]["zahl"], q["windung"]["zahl"]], "max_dv": dv, "max_dv_komplex": dc})
    if not tab:
        return {"urteil": "nicht auswertbar", "vermerk": "keine gemeinsamen Punkte", "werte": {}}
    dvs = [t["max_dv"] for t in tab if t["max_dv"] is not None]
    dcs = [t["max_dv_komplex"] for t in tab if t["max_dv_komplex"] is not None]
    return {"urteil": "eingetroffen" if ok else "nicht eingetroffen",
            "werte": {"gemeinsame_punkte": len(tab), "max_dv": max(dvs) if dvs else None,
                      "max_dv_komplex": max(dcs) if dcs else None,
                      "zahl_abweichend": sum(1 for t in tab if t["max_dv"] is None), "punkte": tab}}


def urteile(D, betr, aus=frozenset()):
    """WS1 bis WS5. aus: Menge (s, richtung, betrag) ausgeschlossener Punkte (Lesart ohne Kreuzungspunkte)."""
    gk = {s: g_ok(D[s]) for s in SS}

    def punkte(slist, kbs):
        for s in slist:
            for p in D[s]["punkte"]:
                if p["betrag"] in kbs and (s, p["richtung"], p["betrag"]) not in aus:
                    f, g = sperren(p, gk[s])
                    yield s, p, f, g
    out = {}
    # ---------------- WS1
    vf, vfc, ges, tab = False, False, False, []
    for s, p, f, g in punkte(("0.1", "0.2"), betr["ws1"]):
        z = p["nullstellen"]
        abw = [abs(x["v_re"] - 1) for x in z]
        abwc = [abs(complex(x["v_re"], x["v_im"]) - 1) for x in z]
        verl = p["windung"]["zahl"] != 2 or len(z) != 2 or max(abw + [0]) > WS1_TOL
        verlc = p["windung"]["zahl"] != 2 or len(z) != 2 or max(abwc + [0]) > WS1_TOL
        if g:
            ges = True
        else:
            vf |= verl
            vfc |= verlc
        tab.append({"s": s, "richtung": p["richtung"], "windung": p["windung"]["windung"], "zahl_R": len(z),
                    "max_abw_v": max(abw) if abw else None, "max_abw_komplex": max(abwc) if abwc else None,
                    "gesperrt": g, "sperren": [k for k, v in f.items() if v]})
    out["WS1"] = {"urteil": dreiwertig(vf, ges), "lesart_komplex": dreiwertig(vfc, ges),
                  "werte": {"max_abw_v": max([t["max_abw_v"] or 0 for t in tab] + [0]),
                            "max_abw_komplex": max([t["max_abw_komplex"] or 0 for t in tab] + [0]),
                            "windungen": sorted(set(round(t["windung"], 3) for t in tab)),
                            "gesperrt": sum(t["gesperrt"] for t in tab), "punkte": tab}}
    # ---------------- WS2
    treffer, unbek, tab = False, False, []
    for s, p, f, g in punkte(("0.2",), [betr["ws2"]]):
        z = pol(p)
        sp = abs(z[0]["v_re"] - z[1]["v_re"]) if len(z) >= 2 else None
        if g or sp is None:
            unbek = True
        elif sp > WS2_SPALT:
            treffer = True
        tab.append({"richtung": p["richtung"], "lk_zahl": len(lk(p)), "v": [x["v_re"] for x in z],
                    "aufspaltung_v": sp, "gesperrt": g})
    sps = [t["aufspaltung_v"] for t in tab if t["aufspaltung_v"] is not None and not t["gesperrt"]]
    out["WS2"] = {"urteil": "eingetroffen" if treffer else ("nicht auswertbar" if unbek else "nicht eingetroffen"),
                  "werte": {"aufspaltung_max": max(sps) if sps else None, "aufspaltung_min": min(sps) if sps else None,
                            "punkte": tab}}
    # ---------------- WS3 und WS4 (Haupt: Bereich R; Zusatzlesart: Zensus)
    vf3, vf4, ges, vf3z, vf4z, gesz = False, False, False, False, False, False
    tab, maxim, maxim_z, zus = [], 0.0, 0.0, []
    for s, p, f, g in punkte(("0.1", "0.2"), betr["alle"]):
        z = p["nullstellen"]
        im = max([abs(x["im"]) for x in z] + [0.0])
        intr, schein, unklar = zensus(p)
        imz = max([abs(x["im"]) for x in intr] + [0.0])
        if g:
            ges = True
        else:
            vf3 |= p["windung"]["zahl"] != 2
            vf4 |= im > WS4_IM
            maxim = max(maxim, im)
        if unklar or g:
            gesz = True
        else:
            vf3z |= len(intr) != 2
            vf4z |= imz > WS4_IM
            maxim_z = max(maxim_z, imz)
        andere = [x for x in intr if not (x["in_R"] and LK[0] <= x["re"] / p["betrag"] <= LK[1])]
        for x in andere:
            zus.append(dict(x, s=s, richtung=p["richtung"], betrag=p["betrag"]))
        tab.append({"s": s, "richtung": p["richtung"], "betrag": p["betrag"], "windung": p["windung"]["windung"],
                    "zahl_R": len(z), "max_abs_im_R": im, "zensus_intrinsisch": len(intr),
                    "zensus_schein": len(schein), "zensus_unklar": len(unklar), "max_abs_im_zensus": imz,
                    "gesperrt": g, "sperren": [k for k, v in f.items() if v], "kreuzung": kreuzung(p)})
    # Kontrolle der Zensus-Lesart: s = 0 muss genau 2 intrinsische Wurzeln je Punkt haben
    kz = [len(zensus(p)[0]) for p in D["0.0"]["punkte"] if p["betrag"] in betr["alle"]]
    kz_unklar = sum(1 for p in D["0.0"]["punkte"] if p["betrag"] in betr["alle"] and zensus(p)[2])
    z_kontrolle = bool(kz) and all(x == 2 for x in kz) and kz_unklar == 0

    def zus_urteil(vf_, gz):
        if not z_kontrolle:
            return "nicht auswertbar"
        return dreiwertig(vf_, gz)
    out["WS3"] = {"urteil": dreiwertig(vf3, ges), "zensus_lesart": zus_urteil(vf3z, gesz),
                  "werte": {"windungen": sorted(set(round(t["windung"], 3) for t in tab)),
                            "zahlen_R": sorted(set(t["zahl_R"] for t in tab)),
                            "zensus_intrinsisch_zahlen": sorted(set(t["zensus_intrinsisch"] for t in tab)),
                            "zensus_kontrolle_s0": {"erfuellt": z_kontrolle, "zahlen": sorted(set(kz)),
                                                    "unklar": kz_unklar},
                            "gesperrt": sum(t["gesperrt"] for t in tab), "zusatzwurzeln_intrinsisch": zus[:200],
                            "zusatzwurzeln_zahl": len(zus)}}
    out["WS4"] = {"urteil": dreiwertig(vf4, ges), "zensus_lesart": zus_urteil(vf4z, gesz),
                  "werte": {"max_abs_im_R": maxim, "max_abs_im_zensus_intrinsisch": maxim_z, "punkte": tab}}
    # ---------------- WS5
    treffer, trefferp, ges, tab = False, False, False, []
    for s, p, f, g in punkte(("0.2",), betr["ws5"]):
        vmax = max([x["v_re"] for x in p["nullstellen"]] + [-1.0])
        vmaxp = max([x["v_re"] for x in pol(p)] + [-1.0])
        if g:
            ges = True
        else:
            treffer |= vmax > 1 + WS5_V
            trefferp |= vmaxp > 1 + WS5_V
        tab.append({"richtung": p["richtung"], "betrag": p["betrag"], "v_max_R": vmax, "v_max_pol": vmaxp,
                    "gesperrt": g})

    def u5(t):
        return "eingetroffen" if t else ("nicht auswertbar" if ges else "nicht eingetroffen")
    vm = [t["v_max_R"] for t in tab if not t["gesperrt"]]
    vmp = [t["v_max_pol"] for t in tab if not t["gesperrt"]]
    out["WS5"] = {"urteil": u5(treffer), "lesart_polarisationen": u5(trefferp),
                  "werte": {"v_max_R": max(vm) if vm else None, "v_max_pol": max(vmp) if vmp else None,
                            "punkte": tab}}
    return out


def beschreibend(D):
    out = {}
    for s in SS:
        P = D[s]["punkte"]
        idx = {(p["richtung"], p["betrag"]): p for p in P}
        tab = []
        for p in P:
            z = pol(p)
            intr, schein, unklar = zensus(p)
            hk = p["hyperkubisch"]
            v = [x["v_re"] for x in z]
            tab.append({"richtung": p["richtung"], "betrag": p["betrag"], "betrag_gitter": p["betrag_gitter"],
                        "windung": p["windung"]["windung"], "zahl_R": len(p["nullstellen"]), "v_pol": v,
                        "v_im_pol": [x["v_im"] for x in z],
                        "aufspaltung_v": abs(v[1] - v[0]) if len(v) == 2 else None,
                        "max_abs_im_R": max([abs(x["im"]) for x in p["nullstellen"]] + [0.0]),
                        "tt": [x["tt_anteil"] for x in z], "tt2": [x["tt_anteil_2"] for x in z],
                        "zeit": [x["zeit_anteil"] for x in z], "diag": [x["diag_anteil"] for x in z],
                        "c4": [x["c4_anteil"] for x in z], "gitter_rest": [x["gitter_rest"] for x in z],
                        "rho": [x["rho"] for x in p["nullstellen"]], "phys": [x["physikalisch"] for x in p["nullstellen"]],
                        "s_wurzel": [x["s"] for x in p["nullstellen"]],
                        "zensus": {"intrinsisch": [[x["re"], x["im"]] for x in intr],
                                   "schein": [[x["re"], x["im"], x["rho"], x["physikalisch"]] for x in schein],
                                   "unklar": [[x["re"], x["im"], x["s"]] for x in unklar]},
                        "eukl": {k: p["eukl_linie"][k] for k in ("n_neg_werte", "n_null_werte", "wechsel_kappa",
                                                                 "kleinster_nichtnull_rel_min", "kappa_bei_min")},
                        "v_hk_gitter": hk["v_gitter_k"], "v_hk_phys": hk["v_phys_k"],
                        "dv_hk_gitter": (np.mean(v) - hk["v_gitter_k"]) if v else None,
                        "dv_hk_phys": (np.mean(v) - hk["v_phys_k"]) if v else None,
                        "kinetik": p["kinetik"], "geister": p["geister"], "minima_fein": p["achse"]["minima_fein"],
                        "zeitumkehr": p["achse"]["zeitumkehr_max"], "rho_rand": p["windung"]["rho_rand_min"],
                        "null_residuum": p["achse"]["null_residuum_max"], "pep": p["pep"], "aberth": p["aberth"],
                        "etop_residuum_rel_min": p["achse"]["etop_residuum_rel_min"]})
        # Inversion: Nullstellen bei -n = konjugierte bei n (Inversion X -> -X bleibt Symmetrie)
        paare = [("x+", "x-"), ("xy+", "xy-"), ("xyz+", "xyz-"), ("xy-z", "-x-yz"), ("123", "-1-2-3")]
        sym = []
        for a, b in paare:
            for kb in sorted(set(p["betrag"] for p in P)):
                if (a, kb) in idx and (b, kb) in idx:
                    za = sorted([complex(x["re"], -x["im"]) for x in idx[(a, kb)]["nullstellen"]], key=lambda c: (c.real, c.imag))
                    zb = sorted([complex(x["re"], x["im"]) for x in idx[(b, kb)]["nullstellen"]], key=lambda c: (c.real, c.imag))
                    sym.append({"paar": [a, b], "betrag": kb, "zahlen": [len(za), len(zb)],
                                "max_abw_rel": float(max(abs(u - v) for u, v in zip(za, zb)) / kb)
                                if len(za) == len(zb) and za else None})
        gkp = []
        for g in D[s].get("gegenprobe_weg_K", []):
            p = idx.get((g["richtung"], g["betrag"]))
            if p is None:
                continue
            zt = sorted([complex(x["re"], x["im"]) for x in p["nullstellen"]], key=lambda c: (c.real, c.imag))
            zk = sorted([complex(a, b) for a, b in g["nullstellen"]], key=lambda c: (c.real, c.imag))
            gkp.append({"richtung": g["richtung"], "betrag": g["betrag"], "zahlen": [len(zt), len(zk)],
                        "max_abw_rel": float(max(abs(u - v) for u, v in zip(zt, zk)) / g["betrag"])
                        if len(zt) == len(zk) and zt else None})
        out[s] = {"tabelle": tab, "inversion_n_gegen_minus_n": sym, "gegenprobe_weg_K": gkp,
                  "geometrie": D[s]["geometrie"],
                  "g": {k: D[s]["g"][k] for k in ("a_max", "b_zufall_max", "etop_residuum_min", "etop_residuum_max")},
                  "kreuzungspunkte": [[t["richtung"], t["betrag"], t["eukl"]["wechsel_kappa"]] for t in tab
                                      if len(t["eukl"]["n_neg_werte"]) > 1]}
    return out


def bilder(D, ordner, betraege):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    namen = []
    for p in D["0.0"]["punkte"]:
        if p["richtung"] not in namen:
            namen.append(p["richtung"])
    farben = plt.cm.viridis(np.linspace(0, 0.95, len(namen)))
    # 1: v gegen |k| je s und Richtung
    fig, axs = plt.subplots(1, 3, figsize=(19, 6), sharey=True)
    for j, s in enumerate(SS):
        P = D[s]["punkte"]
        for c, r in zip(farben, namen):
            pk = sorted([p for p in P if p["richtung"] == r], key=lambda p: p["betrag"])
            for i in range(2):
                b = [p["betrag"] for p in pk if len(pol(p)) > i]
                v = [pol(p)[i]["v_re"] for p in pk if len(pol(p)) > i]
                axs[j].semilogx(b, v, "-", marker="o" if i == 0 else "s", ms=3, color=c, lw=0.8,
                                label=r if (i == 0 and j == 0) else None)
            ex = [(p["betrag"], x["v_re"]) for p in pk for x in p["nullstellen"] if x not in pol(p)]
            if ex:
                axs[j].semilogx([e[0] for e in ex], [e[1] for e in ex], "x", color="r", ms=7)
        axs[j].axhline(1.0, color="k", lw=0.8)
        axs[j].axhspan(1 - WS1_TOL, 1 + WS1_TOL, color="0.88")
        axs[j].set_title(f"s = {s}: v = Re omega/|k_phys| (Kreis/Quadrat: zwei Polarisationen; x: weitere in R)")
        axs[j].set_xlabel("|k_phys|")
    axs[0].set_ylabel("v")
    axs[0].legend(fontsize=6, ncol=2)
    fig.suptitle("REGGE-WELLE-SCHIEF-1: Geschwindigkeit der laufenden Moden, physikalische Richtungen")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-geschwindigkeit.png", dpi=105)
    plt.close(fig)
    # 2: Aufspaltung und Im omega
    fig, axs = plt.subplots(2, 3, figsize=(19, 10))
    for j, s in enumerate(SS):
        P = D[s]["punkte"]
        for c, r in zip(farben, namen):
            pk = sorted([p for p in P if p["richtung"] == r], key=lambda p: p["betrag"])
            b, sp, im = [], [], []
            for p in pk:
                z = pol(p)
                if len(z) == 2:
                    b.append(p["betrag"])
                    sp.append(max(abs(z[0]["v_re"] - z[1]["v_re"]), 1e-17))
                    im.append(max(max(abs(x["im"]) for x in p["nullstellen"]), 1e-17))
            axs[0, j].loglog(b, sp, "-o", ms=3, color=c, lw=0.8)
            axs[1, j].loglog(b, im, "-o", ms=3, color=c, lw=0.8)
        axs[0, j].axhline(WS2_SPALT, color="r", ls="--", lw=0.8)
        axs[1, j].axhline(WS4_IM, color="r", ls="--", lw=0.8)
        axs[0, j].set_title(f"s = {s}: Aufspaltung |v1 - v2| (rot: WS2-Schwelle 1e-4)")
        axs[1, j].set_title(f"s = {s}: max |Im omega| in R (rot: WS4-Schwelle 1e-6)")
        axs[1, j].set_xlabel("|k_phys|")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-aufspaltung-im.png", dpi=100)
    plt.close(fig)
    # 3: Modenzahl (Windung in R) und intrinsische Zensus-Wurzeln
    fig, axs = plt.subplots(2, 3, figsize=(19, 10))
    for j, s in enumerate(SS):
        P = {(p["richtung"], p["betrag"]): p for p in D[s]["punkte"]}
        W = np.full((len(namen), len(betraege)), np.nan)
        Z = np.full((len(namen), len(betraege)), np.nan)
        for a, r in enumerate(namen):
            for b, kb in enumerate(betraege):
                p = P.get((r, kb))
                if p:
                    W[a, b] = p["windung"]["windung"]
                    Z[a, b] = len(zensus(p)[0])
        for ax, X, tt in ((axs[0, j], W, "Windungszahl in R"), (axs[1, j], Z, "intrinsische Wurzeln im Zensus")):
            im_ = ax.imshow(X, aspect="auto", cmap="coolwarm", vmin=0, vmax=4)
            for a in range(X.shape[0]):
                for b in range(X.shape[1]):
                    if np.isfinite(X[a, b]):
                        ax.text(b, a, f"{X[a, b]:.0f}" if tt.startswith("intr") else f"{X[a, b]:.2f}",
                                ha="center", va="center", fontsize=6)
            ax.set_xticks(range(len(betraege)))
            ax.set_xticklabels([str(x) for x in betraege])
            ax.set_yticks(range(len(namen)))
            ax.set_yticklabels(namen, fontsize=6)
            ax.set_title(f"s = {s}: {tt}")
            fig.colorbar(im_, ax=ax, fraction=0.04)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-modenzahl.png", dpi=100)
    plt.close(fig)
    # 4: Zensus in der komplexen Ebene
    fig, axs = plt.subplots(1, 3, figsize=(19, 6))
    for j, s in enumerate(SS):
        for p in D[s]["punkte"]:
            intr, schein, unklar = zensus(p)
            axs[j].plot([x["re"] for x in schein], [x["im"] for x in schein], ".", color="0.7", ms=3)
            axs[j].plot([x["re"] for x in unklar], [x["im"] for x in unklar], "x", color="orange", ms=4)
            axs[j].plot([x["re"] for x in intr], [x["im"] for x in intr], "o", color="tab:blue", ms=3)
        axs[j].set_title(f"s = {s}: Zensus (blau intrinsisch, grau Schein, orange unklar)")
        axs[j].set_xlabel("Re omega")
        axs[j].set_ylabel("Im omega")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-zensus.png", dpi=100)
    plt.close(fig)
    # 5: Wuerfelgitter-Formel (beschreibend)
    fig, axs = plt.subplots(1, 2, figsize=(15, 5.5))
    for s, c in zip(SS, ("k", "tab:blue", "tab:red")):
        for p in D[s]["punkte"]:
            z = pol(p)
            if z:
                v = np.mean([x["v_re"] for x in z])
                axs[0].semilogx(p["betrag"], abs(v - p["hyperkubisch"]["v_gitter_k"]) + 1e-17, "o", color=c, ms=3,
                                label=f"s = {s}" if p is D[s]["punkte"][0] else None)
                axs[1].semilogx(p["betrag"], abs(v - p["hyperkubisch"]["v_phys_k"]) + 1e-17, "o", color=c, ms=3)
    for ax, t in zip(axs, ("mit Gitter-k", "mit physikalischem k")):
        ax.set_yscale("log")
        ax.set_title(f"|v - v_Wuerfelgitter| {t}")
        ax.set_xlabel("|k_phys|")
    axs[0].legend()
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-wuerfelgitter.png", dpi=100)
    plt.close(fig)


def main():
    D = {}
    for s, fn in zip(SS, sys.argv[1:4]):
        with open(fn) as f:
            D[s] = json.load(f)
    with open(sys.argv[4]) as f:
        ref = json.load(f)
    probe = len(sys.argv) > 7 and sys.argv[7] == "probe"
    if probe:
        betr = {"ws1": [0.3], "ws2": 0.6, "ws5": [0.6], "alle": [0.3, 0.6]}
        betraege = [0.3, 0.6]
    else:
        betr = {"ws1": [0.05], "ws2": 0.8, "ws5": [0.4, 0.8], "alle": [0.05, 0.1, 0.2, 0.4, 0.8]}
        betraege = [0.05, 0.1, 0.2, 0.4, 0.8]
    u = {"WS0": ws0(D["0.0"], ref)}
    u.update(urteile(D, betr))
    kreuz = frozenset((s, p["richtung"], p["betrag"]) for s in ("0.1", "0.2") for p in D[s]["punkte"] if kreuzung(p))
    u_ohne = urteile(D, betr, kreuz) if kreuz else None
    erg = {"hinweis": "PROBE des Auswertungscodes auf Rauchdaten (|k| = 0,3/0,6), keine Urteile zur Karte" if probe
           else "Urteile nach PLAN.md Abschnitt 6", "urteile": u,
           "kreuzungspunkte": sorted([list(x) for x in kreuz]),
           "urteile_ohne_kreuzungspunkte": {k: {kk: vv for kk, vv in v.items() if kk != "werte"}
                                            for k, v in u_ohne.items()} if u_ohne else None,
           "beschreibend": beschreibend(D)}
    with open(sys.argv[5], "w") as f:
        json.dump(erg, f, indent=1)
    for g, v in u.items():
        print(g, v["urteil"], {k: vv for k, vv in v.items() if k not in ("urteil", "werte")})
    print("Kreuzungspunkte:", len(kreuz))
    bilder(D, sys.argv[6], betraege)
    print("Bilder geschrieben")


if __name__ == "__main__":
    main()
