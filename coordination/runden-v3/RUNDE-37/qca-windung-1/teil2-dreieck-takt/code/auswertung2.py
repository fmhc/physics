#!/usr/bin/env python3
# DREIECK-TAKT-1 / QCA-WINDUNG-2: mechanische Urteile DT0 bis DT3 nach PLAN.md Abschnitt 3 und 4.
# Aufruf nur auf der .69 ueber kleintest.sh: auswertung2.py --dir LAUFORDNER --out auswertung2.json
# Erwartet p3.json, lm_2.json, lm_3.json, h2.json im Laufordner.
import argparse
import json
import os
import sys

import numpy as np


def lade(p):
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def w3n(w, N):
    return w["gitter"][str(N)]["W3"]


def einseitig(fl):
    return bool(fl["N_oben"] != 0 and fl["N_unten"] == -fl["N_oben"] and fl["N_bulk"] == 0)


def rand_pruefung(H, name):
    v, u = H.get(f"{name}|vorwaerts"), H.get(f"{name}|umkehr")
    if v is None or u is None or "rand" not in v or "rand" not in u or "gerechnet" in v["rand"] or "gerechnet" in u["rand"]:
        return {"vorhanden": False, "ok": False}
    out = {"vorhanden": True, "luecken": []}
    ok = True
    for key, fv in v["rand"].items():
        cands = list(u["rand"].values())
        fu = min(cands, key=lambda f: abs(np.angle(np.exp(1j * (f["phi0"] - fv["phi0"])))))
        e = {"phi0_v": fv["phi0"], "phi0_u": fu["phi0"], "v": [fv["N_oben"], fv["N_unten"], fv["N_bulk"]],
             "u": [fu["N_oben"], fu["N_unten"], fu["N_bulk"]], "einseitig_v": einseitig(fv), "einseitig_u": einseitig(fu),
             "umkehr_dreht": bool(fu["N_oben"] == -fv["N_oben"] and fv["N_oben"] != 0)}
        e["ok"] = bool(e["einseitig_v"] and e["einseitig_u"] and e["umkehr_dreht"])
        ok = ok and e["ok"]
        out["luecken"].append(e)
    out["ok"] = bool(ok and len(out["luecken"]) == 2)
    out["einseitig_irgendwo_v"] = any(e["einseitig_v"] for e in out["luecken"])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    J3 = lade(os.path.join(args.dir, "p3.json"))
    JL2, JL3 = lade(os.path.join(args.dir, "lm_2.json")), lade(os.path.join(args.dir, "lm_3.json"))
    JL = None if (JL2 is None or JL3 is None) else {"modus": "haupt" if JL2.get("modus") == JL3.get("modus") == "haupt" else "gemischt",
                                                  "lm": {**JL2["lm"], **JL3["lm"]}}
    JH = lade(os.path.join(args.dir, "h2.json"))
    res = {"vorbedingungen": {}, "urteile": {}, "vermerke": {}, "kennzahlen": {}}
    vb = res["vorbedingungen"]
    vb["dateien"] = [J3 is not None, JL is not None, JH is not None]
    vb["alle_haupt"] = bool(all(x is not None and x.get("modus") == "haupt" for x in (J3, JL, JH)))
    P, L, H = (J3 or {}).get("p3", {}), (JL or {}).get("lm", {}), (JH or {}).get("h2", {})
    unit = [e["unitaer_abw"] for e in P.get("produkte", []) + P.get("takt", [])]
    if P.get("higashikawa"):
        unit.append(P["higashikawa"]["unitaer_abw"])
    for k, lst in L.items():
        unit += [e["unitaer_abw"] for e in lst if e.get("treffer")]
    vb["unitaer_max"] = max(unit) if unit else None
    vb["unitaer_ok"] = bool(unit and max(unit) <= 1e-8)
    try:
        lam1_min = H["lam1|vorwaerts"]["bulk"]["min_abstand_null"]
        lam3_min = min(H["lam3|vorwaerts"]["bulk"]["min_abstand_null"], H["lam3|vorwaerts"]["bulk"]["min_abstand_pi"])
    except KeyError:
        lam1_min = lam3_min = None
    vb["lam1_min_abstand_null"] = lam1_min
    vb["lam3_min_abstand_null_pi"] = lam3_min
    vb["nachbau_kitagawa_ok"] = bool(lam1_min is not None and lam1_min < 1e-6 and lam3_min > 1e-3)
    ok_vb = bool(vb["alle_haupt"] and vb["unitaer_ok"] and vb["nachbau_kitagawa_ok"])
    vb["alle_ok"] = ok_vb
    # Kennzahlen 3D
    prod = [abs(w3n(e["w3"], e["n_exakt"])) for e in P.get("produkte", [])]
    takt = [abs(w3n(e["w3"], e["n_exakt"])) for e in P.get("takt", [])]
    lmw = [w3n(e["w3"], e["n_exakt"]) for k, lst in L.items() for e in lst if e.get("treffer") and "w3" in e]
    hz = P.get("higashikawa", {})
    hig_ganz = w3n(hz["w3_ganzer_feiner_torus"], hz["n_exakt"]) if hz else None
    res["kennzahlen"] = {"produkte_anzahl": len(prod), "produkte_max_abs_W3": max(prod) if prod else None,
                         "takt_anzahl": len(takt), "takt_max_abs_W3": max(takt) if takt else None,
                         "lm_treffer": len(lmw), "lm_starts": sum(len(v) for v in L.values()),
                         "lm_max_abs_W3": max(abs(x) for x in lmw) if lmw else None,
                         "higashikawa_ganzer_torus": hig_ganz}
    # DT0
    a = bool(prod and takt and max(prod) <= 1e-8 and max(takt) <= 1e-8)
    try:
        ch = H["lam3|vorwaerts"]["bulk"]["chern"]
        b1 = all(c["eindeutig"] and abs(c["C_rund"]) >= 1 and abs(c["C"] - c["C_rund"]) < 0.05 for c in ch)
    except KeyError:
        ch, b1 = None, False
    r3 = rand_pruefung(H, "lam3")
    b2 = bool(r3.get("einseitig_irgendwo_v", False))
    res["urteile"]["DT0"] = "nicht auswertbar" if not ok_vb else ("eingetroffen" if (a and b1 and b2) else "nicht eingetroffen")
    add = [(e["art"], w3n(e["w3"], 48)) for e in P.get("additiv", [])]
    res["vermerke"]["DT0"] = {"teil_a_produkte_takte": a, "teil_b_chern": ch, "teil_b_chern_ok": b1, "teil_b_rand_lam3": r3,
                              "additivitaet": add,
                              "additivitaet_ok": bool(add and all(abs(w + (1 if s != "R" else 0)) < 0.05 for s, w in add))}
    # DT1
    werte = prod + takt + [abs(x) for x in lmw] + ([abs(hig_ganz)] if hig_ganz is not None else [])
    if not ok_vb or not werte:
        dt1 = "nicht auswertbar"
    elif any(abs(x) >= 0.5 and abs(x - round(x)) < 0.05 for x in werte):
        dt1 = "eingetroffen"
    elif all(x < 0.05 for x in werte):
        dt1 = "nicht eingetroffen"
    else:
        dt1 = "nicht auswertbar"
    res["urteile"]["DT1"] = dt1
    res["vermerke"]["DT1"] = {"anzahl_automaten": len(werte), "max_abs_W3": max(werte) if werte else None,
                              "higashikawa_halbbox": hz.get("w3_halbbox"), "higashikawa_andere_halbbox": hz.get("w3_andere_halbbox"),
                              "higashikawa_rand_abw": [hz.get("rand_abw_halbbox_minus_sigma0"), hz.get("rand_abw_andere_halbbox_minus_sigma0")]}
    # DT2
    res["urteile"]["DT2"] = "nicht auswertbar" if dt1 != "eingetroffen" else "nicht auswertbar (Weyl-Analyse eines DT1-Treffers nicht vorgesehen)"
    verm2 = {"kegel_k0": hz.get("kegel_k0"), "U_bei_k0": hz.get("U_bei_k0"), "U_bei_k3_2pi": hz.get("U_bei_k3_2pi")}
    wy = hz.get("weyl_feiner_torus")
    if wy:
        pts = wy.get("punkte", [])
        halb = [p for p in pts if (np.mod(p["t"][2] + 0.25, 1.0) < 0.5)]
        verm2["weyl_ganz"] = {"anzahl": wy.get("anzahl"), "vollstaendig": wy.get("vollstaendig"),
                              "netto_je_luecke": (wy.get("luecken") or {}).get("netto_je_luecke")}
        verm2["weyl_halbzone"] = [{"k": p["k"], "phase": p["phase"], "chi": p["chi"]} for p in halb]
        verm2["weyl_rest"] = [{"k": p["k"], "phase": p["phase"], "chi": p["chi"]} for p in pts if p not in halb]
    res["vermerke"]["DT2"] = verm2
    # DT3
    rv = rand_pruefung(H, "voll")
    res["urteile"]["DT3"] = "nicht auswertbar" if not ok_vb or not rv["vorhanden"] else ("eingetroffen" if rv["ok"] else "nicht eingetroffen")
    res["vermerke"]["DT3"] = {"voll": rv, "lam3": r3, "lam4": rand_pruefung(H, "lam4"),
                              "chern": {k: v["bulk"]["chern"] for k, v in H.items()},
                              "luecken": {k: v["bulk"]["luecken"] for k, v in H.items()}}
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print("Urteile:", res["urteile"], flush=True)


if __name__ == "__main__":
    sys.exit(main())
