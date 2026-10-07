#!/usr/bin/env python3
"""INDUZIERT-WILSON-2D (Runde 40, Code-Agent): Auswertung nach PLAN.md (Urteile W0 bis W3; W4 vom Schreibtisch).

Einheiten wie INDUZIERT-DIRAC-2D: eps = sqrt(A/N); y_eps = y A/N, x = (k eps)^2; Modell y_eps = a + c x + d x^2
gemeinsam ueber E1 und E2 (GLS auf Zellmitteln, freie Kovarianz je Datensatz, Birge; grob_auswertung.py unveraendert).
c_eff = c/P, P = -1/(24 pi) (Fermion-Konvention Gamma_F = -1/2 log det'(D^T D): Dirac +1, Skalar +1).

Aufruf (nur ueber kleintest.sh):
  python wilson_auswertung.py auswerten <lauf_ordner> <aus.json> <vorgaenger_lauf_ordner>
      lauf_ordner: e1-*.json (N = 16 001, A = N), e2-*.json (N = 16 001, A = 64 004)
      vorgaenger_lauf_ordner (nur gelesen): INDUZIERT-DIRAC-2D lauf/ fuer den Bitvergleich W0
"""
import glob
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grob_auswertung as ga    # noqa: E402  (unveraendert, eingefroren 20261004-091915)
import dirac_auswertung as da   # noqa: E402  (unveraendert, eingefroren 20261004-102358)

POLYAKOV = -1.0 / (24.0 * math.pi)
NL_E1, NL_E2 = (1, 2, 4, 6), (2, 4, 8, 12)
OPS = ("B", "W1", "W05")
P_LOF = 0.01
MIN_SAATEN = 16
NSE_NEIN = 2.0
BAND_W1 = (0.7, 1.3)            # Karte W1: c_eff in [0,7; 1,3] mit SE <= 0,3
SE_W1 = 0.3
Q_W2 = 2.0                      # Karte W2: Streuung je Saat (Wilson r = 1) <= 2 x Skalar
SE_Q_W2 = 0.5                   # Plan: Q-Urteil "eingetroffen" nur mit Jackknife-SE(Q) <= 0,5
SE_W3 = 0.3                     # Plan: W3 "eingetroffen" nur mit SE(Differenz) <= 0,3
TOR_NEWTON = 1e-12
RES_MAX = 1e-8                  # Tor W (Grundnetz): Nullvektor-Residuen (relativ)
LUECKE_MAX = 0.5                # Tor W (Bildnetze): sigma_2/sigma_3 <= 0,5 (zwei kleinste getrennt)
KONV_MAX = 1e-10                # Tor W (Bildnetze): letzte Aenderung von log(sigma_1 sigma_2)


# ---------------------------------------------------------------------- Tor
def tor_W(info):
    if not info["endlich"]:
        return False
    if info["art"] == "grund":
        return info["nullvektor_res_rechts"] <= RES_MAX and info["nullvektor_res_links"] <= RES_MAX
    return (info["letzte_aenderung"] is not None and info["letzte_aenderung"] <= KONV_MAX
            and info["luecke_s2_s3"] <= LUECKE_MAX)


def tor(d):
    f = {"netz": [], "W1": [], "W05": []}
    n_netze, luecke, it, wneg, s1, s3 = 0, {"W1": [], "W05": []}, {"W1": [], "W05": []}, [], \
        {"W1": [], "W05": []}, {"W1": [], "W05": []}
    for saat, s in d["saaten"].items():
        g0 = s["gamma0"]
        if not (ga.gueltig(s["pruefung0"]) and s["pruefung0_z2"]["delaunay_verletzt_1e-9"] == 0
                and ga.lu_ok(s["lu0_B"])):
            f["netz"].append(f"s{saat}/basis")
        for op in ("W1", "W05"):
            if not tor_W(g0["info_" + op]):
                f[op].append(f"s{saat}/basis")
        for p in s["punkte"]:
            for e in p["je_S"]:
                for seite in ("plus", "minus"):
                    x = e[seite]
                    n_netze += 1
                    tag = f"s{saat}/{p['richtung']}/n{p['n']}/{seite}"
                    if not da.tor_netz(x):
                        f["netz"].append(tag)
                    for op in ("W1", "W05"):
                        inf = x["info_" + op]
                        if not tor_W(inf):
                            f[op].append(tag)
                        luecke[op].append(inf["luecke_s2_s3"])
                        it[op].append(inf["iterationen"])
                        s1[op].append(inf["sigma_ritz"][1])
                        s3[op].append(inf["sigma_ritz"][2])
                    wneg.append(x["w_negativ"] / x["pruefung"]["E"])
    out = {"netze": n_netze}
    for k, v in f.items():
        out[k] = {"fehler_anzahl": len(v), "fehler": v[:20], "bestanden": len(v) == 0}
    for op in ("W1", "W05"):
        if luecke[op]:
            out["kennzahlen_" + op] = {"luecke_s2_s3_max": float(np.max(luecke[op])),
                                       "luecke_s2_s3_median": float(np.median(luecke[op])),
                                       "iterationen_max": int(np.max(it[op])),
                                       "sigma2_max": float(np.max(s1[op])), "sigma3_min": float(np.min(s3[op]))}
    out["anteil_w_negativ_mittel"] = float(np.mean(wneg)) if wneg else None
    return out


# ---------------------------------------------------------------------- Bitvergleich W0
def lade_vorgaenger(ordner):
    saaten = {}
    for p in sorted(glob.glob(os.path.join(ordner, "e[12]-s*.json"))):
        with open(p) as fh:
            d = json.load(fh)
        for s in d["saaten"]:
            saaten[(int(d["N"]), float(d.get("A", d["N"])), s["saat"])] = s
    return saaten


def bitvergleich(d, ref):
    erg = {}
    for op in ("B", "A"):
        zeilen, gleich, mx, fehlend, saaten = 0, 0, 0.0, 0, 0
        for saat, s in d["saaten"].items():
            if op == "A" and not s.get("mit_A"):
                continue
            key = (int(d["kopf"]["N"]), float(d["kopf"]["A"]), saat)
            if key not in ref:
                fehlend += 1
                continue
            r = ref[key]
            saaten += 1
            werte = [(s["gamma0"][op], r["gamma0"][op])]
            for p in s["punkte"]:
                q = [u for u in r["punkte"] if u["n"] == p["n"] and u["richtung"] == p["richtung"]]
                if not q:
                    fehlend += 1
                    continue
                e, f = p["je_S"][0], q[0]["je_S"][0]
                werte += [(e["plus"][op], f["plus"][op]), (e["minus"][op], f["minus"][op]),
                          (e["D_" + op], f["D_" + op]), (e["y_" + op], f["y_" + op])]
            for a, b in werte:
                zeilen += 1
                gleich += int(a == b)
                mx = max(mx, abs(a - b))
        erg[op] = {"saaten": saaten, "werte": zeilen, "bitgleich": gleich, "max_abs_abw": mx, "fehlend": fehlend,
                   "alle_bitgleich": bool(zeilen > 0 and gleich == zeilen and fehlend == 0)}
    return erg


# ---------------------------------------------------------------------- W2: Streuung je Saat
def streuung_q(tabW, tabB):
    """Q = sqrt(sum_Zellen var_W / sum_Zellen var_B), Varianz von y_eps ueber Saaten je Zelle (ddof 1), E1 + E2."""
    vw = sum(float(np.sum(np.var(tabW[nm], axis=0, ddof=1))) for nm in tabW)
    vb = sum(float(np.sum(np.var(tabB[nm], axis=0, ddof=1))) for nm in tabB)
    return math.sqrt(vw / vb)


def streuung_jackknife(tabW, tabB):
    q = streuung_q(tabW, tabB)
    werte = []
    for nm in tabW:
        M = tabW[nm].shape[0]
        for i in range(M):
            tw = dict(tabW)
            tb = dict(tabB)
            tw[nm] = np.delete(tabW[nm], i, axis=0)
            tb[nm] = np.delete(tabB[nm], i, axis=0)
            werte.append(streuung_q(tw, tb))
    werte = np.array(werte)
    n = werte.size
    se = math.sqrt((n - 1) / n * float(np.sum((werte - werte.mean()) ** 2)))
    return q, se


# ---------------------------------------------------------------------- Hauptauswertung
def auswerten(lauf, ziel, vorg):
    na = "nicht auswertbar"
    e1 = da.lade(lauf, "e1-*.json")
    e2 = da.lade(lauf, "e2-*.json")
    erg = {"polyakov": POLYAKOV, "urteile": {}, "dateien": {"E1": e1["dateien"], "E2": e2["dateien"]}}
    erg["tor"] = {"E1": tor(e1) if e1["saaten"] else None, "E2": tor(e2) if e2["saaten"] else None}
    ref = lade_vorgaenger(vorg)
    erg["bitvergleich_W0"] = {"E1": bitvergleich(e1, ref) if e1["saaten"] else None,
                              "E2": bitvergleich(e2, ref) if e2["saaten"] else None}

    tab, info = {}, {}
    for name, d, nl in (("E1", e1, NL_E1), ("E2", e2, NL_E2)):
        if not d["saaten"]:
            continue
        eps = math.sqrt(d["kopf"]["A"] / d["kopf"]["N"])
        info[name] = {"N": d["kopf"]["N"], "A": d["kopf"]["A"], "eps": eps}
        for op in OPS:
            sa, Y, kb = da.tabelle(d, nl, op)
            tab[(name, op)] = (sa, Y * (d["kopf"]["A"] / d["kopf"]["N"]), (kb * eps) ** 2)
        sa, YW1, x = tab[(name, "W1")]
        _, YW05, _ = tab[(name, "W05")]
        _, YB, _ = tab[(name, "B")]
        tab[(name, "W05_minus_W1")] = (sa, YW05 - YW1, x)
        tab[(name, "W1_minus_B")] = (sa, YW1 - YB, x)
        tab[(name, "W05_minus_B")] = (sa, YW05 - YB, x)
        tab[(name, "W1_plus_4B")] = (sa, YW1 + 4.0 * YB, x)
        tab[(name, "W05_plus_4B")] = (sa, YW05 + 4.0 * YB, x)
        info[name].update({"saaten": int(len(sa)), "saat_min": int(sa.min()) if len(sa) else None,
                           "saat_max": int(sa.max()) if len(sa) else None, "x": x.tolist(),
                           "k_eps": np.sqrt(x).tolist()})
    erg["datensaetze"] = info
    zwei = all(nm in info for nm in ("E1", "E2"))
    alle_ops = OPS + ("W05_minus_W1", "W1_minus_B", "W05_minus_B", "W1_plus_4B", "W05_plus_4B")
    fits = {}
    for op in alle_ops:
        if not zwei or min(info["E1"]["saaten"], info["E2"]["saaten"]) < 5:
            break
        saetze = [(nm, tab[(nm, op)][1], tab[(nm, op)][2]) for nm in ("E1", "E2")]
        h, o = da.fit_op(saetze)
        o["je_datensatz"] = {}
        for nm, Y, x in saetze:
            sig2, tau2 = ga.varianzanteile(Y)
            o["je_datensatz"][nm] = {"y_mittel": Y.mean(axis=0).tolist(),
                                     "y_se": (Y.std(axis=0, ddof=1) / math.sqrt(Y.shape[0])).tolist(),
                                     "y_std": Y.std(axis=0, ddof=1).tolist(), "sigma_rest": math.sqrt(sig2),
                                     "tau_versatz": math.sqrt(tau2),
                                     "c_eff_je_k": ((Y.mean(axis=0) - h["a"]["wert"]) / x / POLYAKOV).tolist(),
                                     "se_c_eff_je_k": (Y.std(axis=0, ddof=1) / math.sqrt(Y.shape[0]) / x
                                                       / abs(POLYAKOV)).tolist()}
        b = {}
        b["nur_E1"] = da.fit_op([saetze[0]])[1] if saetze[0][1].shape[0] > 4 else None
        b["nur_E2"] = da.fit_op([saetze[1]])[1] if saetze[1][1].shape[0] > 4 else None
        b["mit_k6"] = da.fit_op(saetze, "kub")[1]
        b["a_je_datensatz"] = da.fit_op(saetze, "a_je_satz")[1]
        b["fenster_k_eps_0.40"] = da.fit_op(saetze, "quad", 0.40)[1]
        b["nur_k2_fenster_0.40"] = da.fit_op(saetze, "lin", 0.40)[1]
        try:
            b["jackknife_se_c_eff"] = float(ga.jackknife(saetze, "quad")[1] / abs(POLYAKOV))
        except Exception as ex:   # beschreibend
            b["jackknife_se_c_eff"] = repr(ex)
        o["beschreibend"] = b
        fits[op] = o
    erg["fits"] = fits

    # ---- Vorbedingungen
    tor_netz_ok = bool(erg["tor"]["E1"] and erg["tor"]["E2"] and erg["tor"]["E1"]["netz"]["bestanden"]
                       and erg["tor"]["E2"]["netz"]["bestanden"])
    tor_ok = {op: bool(tor_netz_ok and erg["tor"]["E1"][op]["bestanden"] and erg["tor"]["E2"][op]["bestanden"])
              for op in ("W1", "W05")}
    erg["vorbedingungen"] = {"tor_netz": tor_netz_ok, "tor_W1": tor_ok["W1"], "tor_W05": tor_ok["W05"]}

    def vorbed(op):
        if not zwei or op not in fits:
            return False, "Datensatz fehlt"
        if min(info["E1"]["saaten"], info["E2"]["saaten"]) < MIN_SAATEN:
            return False, "weniger als 16 Saaten je Datensatz"
        if fits[op]["p"] < P_LOF:
            return False, f"Modellprobe p = {fits[op]['p']:.4f} < 0,01"
        return True, ""

    # ---- W0
    bv = erg["bitvergleich_W0"]
    teile = [bv[nm][op] for nm in ("E1", "E2") if bv[nm] for op in ("B", "A")]
    if any(t["bitgleich"] < t["werte"] for t in teile):
        u0 = "nicht eingetroffen"
    elif teile and all(t["alle_bitgleich"] for t in teile):
        u0 = "eingetroffen"
    else:
        u0 = na
    erg["urteile"]["W0"] = {"urteil": u0, "kartenwortlaut": u0, "werte": bv}

    # ---- W1
    ok, grund = vorbed("W1")
    if not tor_ok["W1"]:
        ok, grund = False, "Tor"
    w1 = {"c_eff": fits["W1"]["c_eff"], "se": fits["W1"]["se_c_eff"]} if "W1" in fits else {}
    if ok:
        u1, wb = da.band(fits["W1"]["c_eff"], fits["W1"]["se_c_eff"], *BAND_W1)
        w1.update(wb)
        w1.update({"p_modell": fits["W1"]["p"], "birge": fits["W1"]["birge"], "d_eff": fits["W1"].get("d_eff")})
    else:
        u1 = na
    kw1 = ("eingetroffen" if w1 and BAND_W1[0] <= w1["c_eff"] <= BAND_W1[1] and w1["se"] <= SE_W1
           else "nicht eingetroffen")
    erg["urteile"]["W1"] = {"urteil": u1, "vermerk": grund or None, "kartenwortlaut": kw1, "werte": w1}

    # ---- W2
    if zwei and min(info["E1"]["saaten"], info["E2"]["saaten"]) >= 5:
        tW = {nm: tab[(nm, "W1")][1] for nm in ("E1", "E2")}
        tB = {nm: tab[(nm, "B")][1] for nm in ("E1", "E2")}
        q, seq = streuung_jackknife(tW, tB)
        q05, seq05 = streuung_jackknife({nm: tab[(nm, "W05")][1] for nm in ("E1", "E2")}, tB)
        je_zelle = {nm: (np.std(tW[nm], axis=0, ddof=1) / np.std(tB[nm], axis=0, ddof=1)).tolist()
                    for nm in ("E1", "E2")}
        ok2 = tor_ok["W1"] and min(info["E1"]["saaten"], info["E2"]["saaten"]) >= MIN_SAATEN
        if not ok2:
            u2 = na
        elif q <= Q_W2 and seq <= SE_Q_W2:
            u2 = "eingetroffen"
        elif q - Q_W2 > NSE_NEIN * seq:
            u2 = "nicht eingetroffen"
        else:
            u2 = na
        w2 = {"Q_W1": q, "se_Q_W1": seq, "Q_W05": q05, "se_Q_W05": seq05, "je_zelle_W1": je_zelle,
              "se_c_eff_verhaeltnis_W1_B": (fits["W1"]["se_c_eff"] / fits["B"]["se_c_eff"]) if "B" in fits else None,
              "beschreibend_Q_W1_plus_4B": streuung_q({nm: tab[(nm, "W1_plus_4B")][1] for nm in ("E1", "E2")}, tB),
              "beschreibend_Q_W05_minus_W1": streuung_q({nm: tab[(nm, "W05_minus_W1")][1] for nm in ("E1", "E2")},
                                                        tB)}
        kw2 = "eingetroffen" if q <= Q_W2 else "nicht eingetroffen"
    else:
        u2, w2, kw2 = na, {}, na
    erg["urteile"]["W2"] = {"urteil": u2, "kartenwortlaut": kw2, "werte": w2}

    # ---- W3
    okd, gd = vorbed("W05_minus_W1")
    ok1, g1_ = vorbed("W1")
    ok05, g05 = vorbed("W05")
    if not (tor_ok["W1"] and tor_ok["W05"]):
        okd, gd = False, "Tor"
    w3 = {}
    if "W05_minus_W1" in fits:
        dlt = fits["W05"]["c_eff"] - fits["W1"]["c_eff"]
        se_p = fits["W05_minus_W1"]["se_c_eff"]
        se_u = math.hypot(fits["W05"]["se_c_eff"], fits["W1"]["se_c_eff"])
        w3 = {"c_eff_W1": fits["W1"]["c_eff"], "c_eff_W05": fits["W05"]["c_eff"], "differenz": dlt,
              "differenz_gepaart_fit": fits["W05_minus_W1"]["c_eff"], "se_gepaart": se_p, "se_ungepaart": se_u,
              "abstand_in_se_gepaart": abs(dlt) / se_p, "abstand_in_se_ungepaart": abs(dlt) / se_u}
    if not (okd and ok1 and ok05):
        u3 = na
    elif abs(dlt) <= NSE_NEIN * se_p and se_p <= SE_W3:
        u3 = "eingetroffen"
    elif abs(dlt) > NSE_NEIN * se_p:
        u3 = "nicht eingetroffen"
    else:
        u3 = na
    kw3 = ("eingetroffen" if w3 and abs(w3["differenz"]) <= NSE_NEIN * w3["se_ungepaart"] else "nicht eingetroffen")
    erg["urteile"]["W3"] = {"urteil": u3, "vermerk": (gd or g1_ or g05) or None, "kartenwortlaut": kw3, "werte": w3}

    # ---- beschreibend (nach dem Rauchlauf festgelegt, kein Urteil): Kontrollvariable Skalar
    #      c_eff(W) = c_eff(W + 4B) [diese Saaten] - 4 c_eff(B) [alle 96 + 96 Saaten des Vorgaengers]
    pv = os.path.join(vorg, "auswertung.json")
    if os.path.exists(pv):
        with open(pv) as fh:
            bv_all = json.load(fh)["fits"]["B"]
        kv = {"c_eff_B_vorgaenger": bv_all["c_eff"], "se_B_vorgaenger": bv_all["se_c_eff"],
              "hinweis": "SE ohne Korrelation der beiden Teile (Saaten dieses Laufs sind Teilmenge)"}
        for op, comb in (("W1", "W1_plus_4B"), ("W05", "W05_plus_4B")):
            if comb in fits:
                kv[op] = {"c_eff": fits[comb]["c_eff"] - 4.0 * bv_all["c_eff"],
                          "se": math.hypot(fits[comb]["se_c_eff"], 4.0 * bv_all["se_c_eff"]),
                          "c_eff_plus_4B": fits[comb]["c_eff"], "se_plus_4B": fits[comb]["se_c_eff"]}
        erg["beschreibend_kontrollvariable"] = kv

    # ---- W4 (Schreibtisch, PLAN Abschnitt 1)
    erg["urteile"]["W4"] = {"urteil": "eingetroffen", "kartenwortlaut": "eingetroffen",
                            "werte": {"quelle": "PLAN.md Abschnitt 2 (Schreibtisch vor jeder Rechnung)",
                                      "c_KD_kontinuum": -4}}

    with open(ziel, "w") as fh:
        json.dump(erg, fh, indent=1)
    for k, v in erg["urteile"].items():
        print(k, v["urteil"], "| Kartenwortlaut:", v.get("kartenwortlaut"), flush=True)
    try:
        bilder(tab, fits, os.path.dirname(os.path.abspath(ziel)))
    except Exception as ex:   # beschreibend
        print("Bilder fehlgeschlagen:", repr(ex), flush=True)


def bilder(tab, fits, ordner):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    farbe = {"E1": "tab:orange", "E2": "tab:blue"}
    text = {"E1": "Netzabstand 1 (N = 16 001)", "E2": "Netzabstand 2 (N = 16 001, A = 64 004)"}
    titel = {"B": "Skalar (Kotangens-Laplace)", "W1": "Wilson-Fermion r = 1", "W05": "Wilson-Fermion r = 1/2",
             "W05_minus_W1": "Differenz r = 1/2 minus r = 1 (je Saat gepaart)"}
    fig, axs = plt.subplots(2, 2, figsize=(15, 11))
    xx = np.linspace(0, 0.37, 200)
    for ax, op in zip(axs.ravel(), ("B", "W1", "W05", "W05_minus_W1")):
        if op not in fits:
            continue
        o = fits[op]
        a, c, d = o["a"]["wert"], o["c"]["wert"], o["d"]["wert"]
        for nm in ("E1", "E2"):
            sa, Y, x = tab[(nm, op)]
            m = Y.mean(axis=0)
            se = Y.std(axis=0, ddof=1) / math.sqrt(Y.shape[0])
            ax.errorbar(x, (m - a) / x / POLYAKOV, yerr=se / x / abs(POLYAKOV), fmt="o", color=farbe[nm], capsize=3,
                        ms=5, label=f"{text[nm]} ({Y.shape[0]} Saaten)")
        ax.plot(xx, (c + d * xx) / POLYAKOV, "-", color="k", lw=1.2,
                label=f"Ausgleich: c_eff(0) = {o['c_eff']:+.2f} +- {o['se_c_eff']:.2f} (p = {o['p']:.2f})")
        if op != "W05_minus_W1":
            ax.axhspan(BAND_W1[0], BAND_W1[1], color="tab:green", alpha=0.12, label="Band W1 [0,7; 1,3]")
            ax.axhline(1, color="tab:red", lw=1.0, ls=":", label="c = 1")
        ax.axhline(0, color="0.6", lw=0.6)
        ax.set_xlim(0, 0.37)
        ax.set_xlabel("x = (k eps)^2")
        ax.set_ylabel("c_eff(k) = (y - a)/(x P)")
        ax.set_title(titel[op], fontsize=10)
        ax.legend(fontsize=7)
    fig.suptitle("INDUZIERT-WILSON-2D: c_eff(k) gegen (k eps)^2 (Fermion-Konvention, Dirac = +1)", fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "bild-ck-gegen-k2.png"), dpi=105)
    plt.close(fig)


def main():
    if sys.argv[1] == "auswerten":
        auswerten(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        raise SystemExit("unbekannter Modus")


if __name__ == "__main__":
    main()
