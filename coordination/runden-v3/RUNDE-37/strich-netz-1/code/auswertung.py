#!/usr/bin/env python3
"""STRICH-NETZ-1: mechanische Auswertung nach PLAN.md Abschnitt 7 (Urteile SN0 bis SN7, Kontrollen, [Z]-Streuung).

Aufruf (nur ueber kleintest.sh):  python auswertung.py <laufordner>
"""
import glob
import json
import math
import os
import sys

import numpy as np

D = sys.argv[1]
KARTE_LESARTEN = ("alle", "gabriel", "delaunay", "beruehrung")


def lade(p):
    with open(p) as f:
        return json.load(f)


def da(p):
    return os.path.exists(os.path.join(D, p))


def j(p):
    return lade(os.path.join(D, p))


def fit(x, y, grad):
    """Kleinste Quadrate y = sum_k c_k x^p_k (p aus grad), Rueckgabe Koeffizienten und Standardfehler."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    A = np.stack([x ** p for p in grad], 1)
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = y - A @ c
    dof = max(len(y) - len(grad), 1)
    s2 = float(r @ r) / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    return c, np.sqrt(np.diag(cov)), float(np.sqrt(np.mean(r ** 2)))


out = {"ordner": D, "urteile": {}, "werte": {}, "kontrollen": {}, "vermerke": []}
W = out["werte"]

# ------------------------------------------------------------------ Teil A
saaten = []
probe = []
for f in sorted(glob.glob(os.path.join(D, "teilA-b*.json"))):
    z = lade(f)
    saaten += z["saaten"]
    probe += z["proben_3420"]
nA = len(saaten)
W["teilA_saaten"] = nA
if nA:
    tab = {}
    for la in ("alle", "gabriel", "delaunay", "beruehrung", "wachstum"):
        E = np.array([s[la]["E"] for s in saaten])
        I = np.array([s[la]["inseln"] for s in saaten])
        g = np.array([s[la]["grad_mittel"] for s in saaten])
        kr = np.array([s["kreuz"][la]["mittel"] for s in saaten])
        tab[la] = {"E_mittel": float(E.mean()), "E_sd": float(E.std(ddof=1)), "E_min": int(E.min()),
                   "E_max": int(E.max()), "inseln_mittel": float(I.mean()), "inseln_sd": float(I.std(ddof=1)),
                   "grad_mittel": float(g.mean()), "kreuz_mittel": float(kr.mean()),
                   "kreuz_se_saaten": float(kr.std(ddof=1) / math.sqrt(nA)),
                   "anteil_zusammenhaengend": float(np.mean(I == 1))}
        fe = np.array([s["feder"][la]["abw"] for s in saaten])
        Z = np.array([s["feder"][la]["Z"] for s in saaten])
        S = np.array([s["feder"][la]["S"] for s in saaten])
        tab[la]["feder"] = {"abw_max": int(np.abs(fe).max()), "anteil_abw_ueber_1": float(np.mean(np.abs(fe) > 1)),
                            "anteil_abw_ungleich_0": float(np.mean(fe != 0)), "Z_mittel": float(Z.mean()),
                            "S_mittel": float(S.mean()),
                            "calladine_max": int(np.abs([s["feder"][la]["calladine"] for s in saaten]).max()),
                            "sv_min_nichtnull_rel_min": float(min(s["feder"][la]["sv_min_nichtnull_rel"] for s in saaten)),
                            "sv_max_null_rel_max": float(max(s["feder"][la]["sv_max_null_rel"] for s in saaten))}
        b = [s["beruehr"][la] for s in saaten if "beruehr" in s and la in s["beruehr"]]
        if b:
            tab[la]["beruehr_mittel_je_ansicht"] = np.mean([x["mittel"] for x in b], axis=0).tolist()
            tab[la]["beruehr_anteil_ansichten_mit"] = np.mean([x["anteil_ansichten_mit"] for x in b], axis=0).tolist()
    W["teilA"] = tab
    W["teilA_nn_gegenseitig_mittel"] = float(np.mean([s["nn_gegenseitig"] for s in saaten]))
    W["teilA_gabriel_in_delaunay_alle"] = bool(all(s["gabriel_in_delaunay"] for s in saaten))
    W["teilA_fem_flache_tetra_summe"] = int(sum(s["fem_flache_tetra"] for s in saaten))
    W["teilA_fem_volumen_rel_max"] = float(max(abs(s["fem_volumen_rel"]) for s in saaten))
    kp = [s["kontrolle_kreuz_paare_gleich_konvex"] for s in saaten if "kontrolle_kreuz_paare_gleich_konvex" in s]
    out["kontrollen"]["kreuzungen_paare_gleich_konvex"] = bool(all(kp)) if kp else None
    sk = {}
    for key in saaten[0]["skalar"]:
        sk[key] = {"null_mittel": float(np.mean([s["skalar"][key]["null"] for s in saaten])),
                   "pr_tief_mittel": float(np.mean([np.mean(s["skalar"][key]["pr_tief"]) for s in saaten
                                                    if len(s["skalar"][key]["pr_tief"])])),
                   "affin_tief1_mittel": float(np.mean([s["skalar"][key]["affin_tief"][0] for s in saaten
                                                        if len(s["skalar"][key]["affin_tief"])]))}
    W["teilA_skalar"] = sk
    st = [s["stoss"] for s in saaten if "stoss" in s]
    if st:
        W["teilA_stoss"] = {la: {"kor_ankunft_abstand_mittel": float(np.nanmean([x[la]["kor_ankunft_abstand"] if
                                                                                 x[la]["kor_ankunft_abstand"] is not None
                                                                                 else np.nan for x in st])),
                                 "kor_ankunft_hops_mittel": float(np.nanmean([x[la]["kor_ankunft_hops"] if
                                                                             x[la]["kor_ankunft_hops"] is not None
                                                                             else np.nan for x in st]))}
                            for la in st[0]}
        W["teilA_alle_spread_max"] = float(max(x["alle"]["spread_andere_max"] for x in st))
        W["teilA_alle_analytisch_max"] = float(max(x["alle"]["alle_gegen_analytisch_max"] for x in st))
    if probe:
        W["probe_3420"] = {"zahl": len(probe), "abw_max": float(max(p["abw_max"] for p in probe)),
                           "summe_abw_max": float(max(abs(p["summe"] - 2 * math.pi) for p in probe))}

# ------------------------------------------------------------------ Netze N = 50 000
dicht = {int(lade(f)["saat"]): lade(f) for f in sorted(glob.glob(os.path.join(D, "dicht-*.json")))}
if dicht:
    W["sn7"] = {s: d["sn7"] for s, d in dicht.items()}
    W["homogen"] = {s: {k: {x: h[x] for x in ("c_mittel", "c_voigt_mittel", "anisotropie", "c_richt13", "c_eig",
                                              "drift_rel", "cg_residuum")} if k != "weyl" else h
                        for k, h in d["homogen"].items()} for s, d in dicht.items()}
    W["alternativ_takt"] = {s: d["homogen"]["delaunay/ungew"].get("alternativ_takt_mittlere_laenge")
                            for s, d in dicht.items()}
    W["kuerzeste"] = {s: {la: {x: d["kuerzeste"][la][x] for x in ("v_mittel", "v_se", "umweg_fern_mittel",
                                                                  "v_kegel_rel_std", "v_quelle_kegel_rel_std_mittel")}
                          for la in d["kuerzeste"]} for s, d in dicht.items()}
    W["lokal_streuung_Z"] = {s: d["lokal"] for s, d in dicht.items()}
    W["beruehrung_50k"] = {s: d["beruehrung"] for s, d in dicht.items()}
    W["netz_pruefung"] = {s: d["pruefung"] for s, d in dicht.items()}
klein = {}
for f in sorted(glob.glob(os.path.join(D, "klein-*.json"))):
    z = lade(f)
    klein[z["N"]] = z
if klein:
    kz = {}
    for N, z in klein.items():
        kz[N] = {}
        for fe in ("fem", "voronoi", "ungew", "laenge"):
            c = np.array([s["homogen"][fe]["c_mittel"] for s in z["saaten"]])
            a = np.array([s["homogen"][fe]["anisotropie"] for s in z["saaten"]])
            kz[N][fe] = {"c_mittel": float(c.mean()), "c_sd_saaten": float(c.std(ddof=1)) if len(c) > 1 else 0.0,
                         "anisotropie_mittel": float(a.mean()), "saaten": len(c)}
        kz[N]["sn7"] = {x: float(np.mean([s["sn7"][x] for s in z["saaten"]])) for x in z["saaten"][0]["sn7"]}
    W["klein"] = kz

eigen = {}
for f in sorted(glob.glob(os.path.join(D, "eigen-*.json"))):
    z = lade(f)
    for fe, d in z["felder"].items():
        eigen[fe] = d
if eigen:
    W["eigen"] = {fe: {"wellen": [{x: w[x] for x in ("m", "k", "c", "gewicht_schale")} for w in d["wellen"]],
                       "residuum_max": d["residuum_max"], "c2_homogen": d["c2_homogen"],
                       "ebene_welle_anteil_tief_mittel": float(np.mean(np.array(d["ebene_welle_anteil_je_mode"])[1:33]))}
                  for fe, d in eigen.items()}

weyl = []
for f in sorted(glob.glob(os.path.join(D, "weyl-1-*.json"))):
    z = lade(f)
    for lauf in z["laeufe"]:
        for w in lauf["wellen"]:
            weyl.append(dict(w, a=lauf["a"], mu_max=lauf["mu_max"]))
if weyl:
    W["weyl"] = [{x: w[x] for x in ("m", "theta", "k", "v", "v_halbM", "v_max", "gewicht_fenster", "sigma_E",
                                    "erstes_moment", "mu_max")} for w in weyl]

welle = {}
for f in sorted(glob.glob(os.path.join(D, "welle-*.json"))):
    z = lade(f)
    welle[f"{z['lesart']}/{z['feld']}"] = z

kontrolle = j("kontrolle.json") if da("kontrolle.json") else None

# ------------------------------------------------------------------ Kontrollen
K = out["kontrollen"]
if kontrolle:
    K["K1_weyl_gitter_max_abw"] = float(max(abs(x["abw"]) for x in kontrolle["K1_weyl_gitter"]))
    K["K1_ok"] = K["K1_weyl_gitter_max_abw"] <= 1e-3
    K["K2_skalar_gitter_max_abw"] = float(max(abs(x["c_eigen"] - x["c_exakt"])
                                             for x in kontrolle["K2_skalar_gitter"]["wellen"]))
    K["K2_ok"] = K["K2_skalar_gitter_max_abw"] <= 1e-6
    K["K3_homogen_abw"] = kontrolle["K3_homogen_geschichtet"]["abw"]
    K["K3_ok"] = K["K3_homogen_abw"] <= 1e-6
    k4 = kontrolle["K4_netz_1000"]
    K["K4"] = {"kanten_gleich": k4["pruefung"]["kanten_tetra_gleich_spinnetz"],
               "fem_kopie_rel": k4["pruefung"]["fem_kopie_gegen_gradient_rel"],
               "drift_fem": k4["fem"]["drift_rel"], "drift_voronoi": k4["voronoi"]["drift_rel"],
               "voigt_fem": k4["fem"]["voigt"], "voigt_voronoi": k4["voronoi"]["voigt"]}
    K["K4_ok"] = bool(k4["pruefung"]["kanten_tetra_gleich_spinnetz"] and k4["pruefung"]["fem_kopie_gegen_gradient_rel"]
                      <= 1e-8 and k4["fem"]["drift_rel"] <= 1e-10 and k4["voronoi"]["drift_rel"] <= 1e-10)
if dicht:
    K["netze_50k"] = {s: {"kanten_gleich": d["pruefung"]["kanten_tetra_gleich_spinnetz"],
                          "euler": d["pruefung"]["euler"], "abschluss": d["pruefung"]["abschluss_max_rel"],
                          "drift_fem": d["homogen"]["delaunay/fem"]["drift_rel"],
                          "drift_voronoi": d["homogen"]["delaunay/voronoi"]["drift_rel"]} for s, d in dicht.items()}

U = out["urteile"]


def urteil(nr, plan, wortlaut, kennzahlen, bem=""):
    U[nr] = {"plan": plan, "kartenwortlaut": wortlaut, "kennzahlen": kennzahlen, "bemerkung": bem}


# ------------------------------------------------------------------ SN0
if nA and dicht and eigen and welle.get("alle/ungew") is not None:
    a1 = all(s["alle"]["E"] == 190 for s in saaten)
    al = welle["alle/ungew"]
    sp_rel = max(x["spread_andere"] for p in al["proben"] for x in p["reihe"])
    a2 = (W["teilA_alle_spread_max"] <= 1e-12 and W["teilA_alle_analytisch_max"] <= 1e-10 and sp_rel <= 1e-12)
    fe_max = max(abs(s["feder"][la]["abw"]) for s in saaten for la in KARTE_LESARTEN)
    a3 = fe_max <= 1
    hc = [c for s, d in dicht.items() for c in d["homogen"]["delaunay/fem"]["c_richt13"]]
    ec = [w["c"] for w in eigen["fem"]["wellen"][:3]]
    a4 = all(0.98 <= c <= 1.02 for c in hc + ec)
    a5 = bool(probe) and W["probe_3420"]["abw_max"] <= 1e-3 and W["probe_3420"]["summe_abw_max"] <= 1e-3
    teile = {"190": a1, "keine_front": a2, "maxwell": a3, "fem_c": a4, "3420": a5}
    pl = "eingetroffen" if all(teile.values()) else "nicht eingetroffen"
    urteil("SN0", pl, pl, {"teile": teile, "maxwell_abw_max": fe_max,
                           "maxwell_anteil_abw_ueber_1": {la: W["teilA"][la]["feder"]["anteil_abw_ueber_1"]
                                                          for la in KARTE_LESARTEN},
                           "fem_c_homogen_min_max": [min(hc), max(hc)], "fem_c_k0171": ec,
                           "alle_spread_50k": sp_rel, "probe_3420": W.get("probe_3420")})

# ------------------------------------------------------------------ SN1 bis SN3
if nA:
    e1 = W["teilA"]["gabriel"]["E_mittel"]
    urteil("SN1", "eingetroffen" if 75 <= e1 <= 110 else "nicht eingetroffen",
           "eingetroffen" if 75 <= e1 <= 110 else "nicht eingetroffen", {"gabriel_E_mittel": e1})
    e2, i2 = W["teilA"]["beruehrung"]["E_mittel"], W["teilA"]["beruehrung"]["inseln_mittel"]
    ok2 = 12 <= e2 <= 16 and 4 <= i2 <= 8
    urteil("SN2", "eingetroffen" if ok2 else "nicht eingetroffen", "eingetroffen" if ok2 else "nicht eingetroffen",
           {"E_mittel": e2, "inseln_mittel": i2})
    k3 = W["teilA"]["alle"]["kreuz_mittel"]
    ok3 = 2900 <= k3 <= 3500
    urteil("SN3", "eingetroffen" if ok3 else "nicht eingetroffen", "eingetroffen" if ok3 else "nicht eingetroffen",
           {"kreuz_mittel": k3, "P_konvex": k3 / 4845})

# ------------------------------------------------------------------ SN4


def front_pruefung(z, L):
    ell = z["mittlere_kantenlaenge"]
    erg = []
    for p in z["proben"]:
        t = np.array([x["t"] for x in p["reihe"]])
        R = np.array([x["R90"] for x in p["reihe"]])
        Rk = np.array([x["R90_kegel"] for x in p["reihe"]])
        sel = (R >= 2 * ell) & (R <= L / 2 - 4.0)
        if sel.sum() < 6:
            erg.append({"auswertbar": False, "punkte": int(sel.sum())})
            continue
        ts, Rs = t[sel], R[sel]
        span = float(Rs.max() - Rs.min())
        c, _, rms = fit(ts, Rs, (0, 1))
        r2 = 1 - np.sum((Rs - (c[0] + c[1] * ts)) ** 2) / np.sum((Rs - Rs.mean()) ** 2)
        h = len(ts) // 2
        v1 = fit(ts[:h], Rs[:h], (0, 1))[0][1]
        v2 = fit(ts[h:], Rs[h:], (0, 1))[0][1]
        vk = np.array([fit(ts, Rk[sel, k], (0, 1))[0][1] for k in range(Rk.shape[1])
                       if np.all(np.isfinite(Rk[sel, k]))])
        lin = bool(r2 >= 0.99 and abs(v1 - v2) / c[1] <= 0.10 and span >= 5 * ell)
        erg.append({"auswertbar": True, "v": float(c[1]), "r2": float(r2), "v_haelften": [float(v1), float(v2)],
                    "span_durch_ell": span / ell, "linear": lin, "kegel_cv": float(vk.std() / vk.mean()),
                    "punkte": int(sel.sum())})
    return erg


if welle and dicht:
    L = float(50000 ** (1 / 3))
    sn4 = {}
    for key in welle:
        if key.startswith("alle"):
            continue
        e = front_pruefung(welle[key], L)
        aus = all(x["auswertbar"] for x in e)
        ok = aus and all(x["linear"] for x in e) and np.mean([x["kegel_cv"] for x in e]) <= 0.15
        sn4[key] = {"proben": e, "auswertbar": aus, "erfuellt": bool(ok),
                    "v_mittel": float(np.mean([x["v"] for x in e if x["auswertbar"]])) if aus else None,
                    "kegel_cv_mittel": float(np.mean([x["kegel_cv"] for x in e if x["auswertbar"]])) if aus else None}
    W["sn4"] = sn4
    if "gabriel/ungew" in sn4 and "delaunay/ungew" in sn4:
        if not (sn4["gabriel/ungew"]["auswertbar"] and sn4["delaunay/ungew"]["auswertbar"]):
            pl = "nicht auswertbar"
        else:
            pl = "eingetroffen" if sn4["gabriel/ungew"]["erfuellt"] and sn4["delaunay/ungew"]["erfuellt"] \
                else "nicht eingetroffen"
        wl = "eingetroffen" if all(v["erfuellt"] for k, v in sn4.items() if k.split("/")[0] in ("gabriel", "delaunay")) \
            else "nicht eingetroffen"
        urteil("SN4", pl, wl, {k: {x: v[x] for x in ("erfuellt", "v_mittel", "kegel_cv_mittel")} for k, v in sn4.items()},
               "Plan: Feld ungew; Wortlaut: alle gerechneten Felder auf Gabriel und Delaunay")

# ------------------------------------------------------------------ SN5
if weyl and eigen and dicht:
    wk = [w for w in weyl if w["k"] <= 0.35 and w["gewicht_fenster"] >= 0.5]
    cw, sw, rw = fit([w["k"] for w in wk], [w["v"] for w in wk], (0, 1, 2))
    fk = [w for w in eigen["fem"]["wellen"] if w["c"] is not None]
    cf, sf, rf = fit([w["k"] for w in fk], [w["c"] for w in fk], (0, 2))
    d5 = abs(cw[0] - cf[0]) / cf[0]
    se5 = math.sqrt(sw[0] ** 2 + sf[0] ** 2) / cf[0]
    ax_w = [w["v"] for w in weyl if np.allclose(w["theta"], 0) and sum(abs(x) for x in w["m"]) == 1]
    ax_f = [w["c"] for w in eigen["fem"]["wellen"][:3]]
    k1ok = K.get("K1_ok", False)
    if not k1ok or 2 * se5 > 0.005:
        pl = "nicht auswertbar"
    else:
        pl = "eingetroffen" if d5 < 0.01 else "nicht eingetroffen"
    wl = pl
    klein_k = sorted([w for w in weyl if w["k"] < 0.1], key=lambda w: w["k"])
    urteil("SN5", pl, wl, {"v0_weyl": float(cw[0]), "se_v0_weyl": float(sw[0]), "fit_weyl": cw.tolist(),
                           "rms_weyl": rw, "c0_fem": float(cf[0]), "se_c0_fem": float(sf[0]), "fit_fem": cf.tolist(),
                           "rms_fem": rf, "delta5": d5, "se_delta5": se5, "punkte_weyl": len(wk),
                           "k0171_weyl_achsen": ax_w, "k0171_fem_achsen": ax_f,
                           "k0171_abw_rel": abs(np.mean(ax_w) - np.mean(ax_f)) / np.mean(ax_f),
                           "weyl_kleinste_k": [(w["k"], w["v"]) for w in klein_k[:6]],
                           "weyl_grenzwert_erste_ordnung": {s: d["homogen"]["weyl"]["v_mittel"] for s, d in dicht.items()},
                           "fem_grenzwert_homogen": {s: d["homogen"]["delaunay/fem"]["c_mittel"] for s, d in dicht.items()},
                           "K1_ok": k1ok})

# ------------------------------------------------------------------ SN6
if dicht and 1 in dicht:
    h = dicht[1]["homogen"]
    ci, cii = h["delaunay/fem"]["c_mittel"], h["delaunay/ungew"]["c_mittel"]
    d6 = abs(cii - ci) / ci
    a6 = h["delaunay/ungew"]["anisotropie"]
    ok = d6 > 0.05 or a6 > 0.02
    geg = {s: {"delta6": abs(d["homogen"]["delaunay/ungew"]["c_mittel"] - d["homogen"]["delaunay/fem"]["c_mittel"])
                / d["homogen"]["delaunay/fem"]["c_mittel"], "anisotropie": d["homogen"]["delaunay/ungew"]["anisotropie"]}
           for s, d in dicht.items()}
    ken = {"c_fem": ci, "c_ungew": cii, "delta6": d6, "anisotropie_ungew": a6, "gegenprobe_saaten": geg,
           "c_ungew_alternativ_takt": h["delaunay/ungew"].get("alternativ_takt_mittlere_laenge")}
    if eigen.get("ungew"):
        ken["k0171_ungew"] = [w["c"] for w in eigen["ungew"]["wellen"][:3]]
    urteil("SN6", "eingetroffen" if ok else "nicht eingetroffen", "eingetroffen" if ok else "nicht eingetroffen", ken,
           "Plan-Normierung: Mittelwert-Tensor mit Spur 3; Wortlaut ohne Normierung, siehe ERGEBNIS")
    if any((g["delta6"] > 0.05 or g["anisotropie"] > 0.02) != ok for g in geg.values()):
        out["vermerke"].append("SN6: Gegenprobe-Saat gibt ein anderes Urteil")

# ------------------------------------------------------------------ SN7
if dicht:
    g = np.mean([d["sn7"]["grad_gabriel"] for d in dicht.values()])
    dl = np.mean([d["sn7"]["grad_delaunay"] for d in dicht.values()])
    nn = np.mean([d["sn7"]["nn_gegenseitig"] for d in dicht.values()])
    teile = {"gabriel": bool(abs(g - 8.0) <= 0.1), "delaunay": bool(abs(dl - 15.54) <= 0.1),
             "nn": bool(abs(nn - 0.62) <= 0.01)}
    pl = "eingetroffen" if all(teile.values()) else "nicht eingetroffen"
    urteil("SN7", pl, pl, {"grad_gabriel": float(g), "grad_delaunay": float(dl), "nn_gegenseitig": float(nn),
                           "teile": teile, "je_saat": {s: d["sn7"] for s, d in dicht.items()},
                           "nn_soll_3d_16_27": 16 / 27})

with open(os.path.join(D, "auswertung.json.tmp"), "w") as f:
    json.dump(out, f, indent=1, default=lambda x: x.tolist() if hasattr(x, "tolist") else str(x))
os.replace(os.path.join(D, "auswertung.json.tmp"), os.path.join(D, "auswertung.json"))
for k, v in U.items():
    print(k, v["plan"], "|", v["kartenwortlaut"], flush=True)
print("Kontrollen:", {k: v for k, v in K.items() if k.endswith("_ok")}, flush=True)
