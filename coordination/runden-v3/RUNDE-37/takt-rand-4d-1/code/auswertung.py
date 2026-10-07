#!/usr/bin/env python3
# TAKT-RAND-4D-1: mechanische Urteile TR0 bis TR2 nach PLAN.md Abschnitt 4 (nach Plan und nach Kartenwortlaut).
# Aufruf nur auf der .69 ueber kleintest.sh: auswertung.py --dir LAUFORDNER --out auswertung.json
# Erwartet r2.json und p4_<Modell>.json (P4a, P4b, P4t, P4c, P4cr, P4aL24) im Laufordner.
import argparse
import json
import os
import sys

TOL_GANZ = 0.05
TOL_ISO = 0.10
MODELLE = ["P4a", "P4b", "P4t", "P4c", "P4cr", "P4aL24"]
KW_MODELLE = ["P4a", "P4b", "P4c", "P4cr"]


def lade(p):
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def ganz(x):
    return abs(x - round(x)) < TOL_GANZ


def einseitig(f):
    if f is None:
        return False
    return bool(ganz(f["N_oben"]) and ganz(f["N_unten"]) and abs(f["N_alle"]) < TOL_GANZ and round(f["N_oben"]) != 0
                and round(f["N_unten"]) == -round(f["N_oben"]))


def null(f):
    if f is None:
        return False
    return bool(ganz(f["N_oben"]) and ganz(f["N_unten"]) and abs(f["N_alle"]) < TOL_GANZ and round(f["N_oben"]) == 0
                and round(f["N_unten"]) == 0)


def kchi_ok(R):
    k = (R or {}).get("K_chi") or {}
    soll = {"Gamma": 1, "X1": -1, "X12": 1, "R": -1}
    return bool(all(k.get(n) is not None and k[n]["chi"] == s for n, s in soll.items()))


def tr1_modell(P, kchi):
    """Rueckgabe: (Urteil, Details) fuer ein 4D-Modell nach der TR1-Regel."""
    if P is None:
        return "nicht auswertbar", {"grund": "Datei fehlt"}
    d = {"unitaer_platte": P.get("unitaer_platte"), "unitaer_volumen": P.get("unitaer_volumen"),
         "vollstaendig": P.get("vollstaendig"), "luecken_offen": P.get("luecken_offen"), "zaehlung": P.get("zaehlung"),
         "summenregel": P.get("summenregel"), "volumen": P.get("volumen")}
    vb = bool(P.get("modus_haupt") and P.get("unitaer_platte", 1) <= 1e-10 and P.get("unitaer_volumen", 1) <= 1e-10
              and kchi and P.get("vollstaendig") and P.get("luecken_offen"))
    d["vorbedingungen_ok"] = vb
    if not vb:
        return "nicht auswertbar", d
    treffer = []
    for g in P["luecken_offen"]:
        top, bot = P["zaehlung"][f"oben|{g}"], P["zaehlung"][f"unten|{g}"]
        if top["anzahl"] % 2 == 1 and top["netto"] != 0 and bot["anzahl"] % 2 == 1 and bot["netto"] == -top["netto"]:
            treffer.append(g)
    d["luecken_mit_treffer"] = treffer
    return ("eingetroffen" if treffer else "nicht eingetroffen"), d


def iso_ok(kegel):
    if kegel is None:
        return False
    i = kegel["iso"]["0.05"]
    return bool(i["alle_gefunden"] and i["spann_rel"] <= TOL_ISO)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    J2 = lade(os.path.join(args.dir, "r2.json"))
    P = {}
    for m in MODELLE:
        j = lade(os.path.join(args.dir, f"p4_{m}.json"))
        if j is not None:
            j["p4"]["modus_haupt"] = j.get("modus") == "haupt"
            P[m] = j["p4"]
        else:
            P[m] = None
    res = {"urteile_plan": {}, "urteile_kartenwortlaut": {}, "vermerke": {}, "kennzahlen": {}}
    R = (J2 or {}).get("r2")
    kchi = kchi_ok(R)
    res["kennzahlen"]["K_chi"] = (R or {}).get("K_chi")
    res["kennzahlen"]["K_chi_ok"] = kchi
    # ---------------- TR0
    vb0 = bool(J2 is not None and J2.get("modus") == "haupt" and kchi
               and all(R.get(n, {}).get("unitaer_abw", 1) <= 1e-10 for n in ("R1_sonder", "R2_anomal", "R2r_anomal_umkehr", "R3_chern")))

    def fl(n, g):
        return ((R or {}).get(n, {}).get("fluss") or {}).get(g)

    benoetigt = [("R1_sonder", "pi"), ("R2_anomal", "0"), ("R2_anomal", "pi"), ("R2r_anomal_umkehr", "0"),
                 ("R2r_anomal_umkehr", "pi"), ("R3_chern", "0"), ("R3_chern", "pi")]
    da = all(fl(n, g) is not None for n, g in benoetigt)
    teile = {}
    if vb0 and da:
        teile["R1_pi_einseitig"] = einseitig(fl("R1_sonder", "pi"))
        teile["R2_0_einseitig"] = einseitig(fl("R2_anomal", "0"))
        teile["R2_pi_einseitig"] = einseitig(fl("R2_anomal", "pi"))
        teile["R3_0_null"] = null(fl("R3_chern", "0"))
        teile["R3_pi_einseitig"] = einseitig(fl("R3_chern", "pi"))
        teile["R2r_umgekehrt"] = bool(all(einseitig(fl("R2r_anomal_umkehr", g)) and einseitig(fl("R2_anomal", g))
                                          and round(fl("R2r_anomal_umkehr", g)["N_oben"]) == -round(fl("R2_anomal", g)["N_oben"])
                                          for g in ("0", "pi")))
        res["urteile_plan"]["TR0"] = "eingetroffen" if all(teile.values()) else "nicht eingetroffen"
    else:
        res["urteile_plan"]["TR0"] = "nicht auswertbar"
    res["vermerke"]["TR0"] = {"vorbedingungen_ok": vb0, "alle_luecken_offen": da, "teile": teile,
                              "fluss": {n: (R or {}).get(n, {}).get("fluss") for n in R_NAMEN(R)},
                              "volumen": {n: (R or {}).get(n, {}).get("volumen") for n in R_NAMEN(R)}}
    if vb0 and fl("R2_anomal", "0") is not None or (vb0 and fl("R2_anomal", "pi") is not None):
        kw0 = any(einseitig(fl("R2_anomal", g)) for g in ("0", "pi"))
        res["urteile_kartenwortlaut"]["TR0"] = "eingetroffen" if kw0 else "nicht eingetroffen"
    else:
        res["urteile_kartenwortlaut"]["TR0"] = "nicht auswertbar"
    # ---------------- TR1
    u1 = {}
    for m in MODELLE:
        u1[m] = tr1_modell(P[m], kchi)
    res["urteile_plan"]["TR1"] = u1["P4a"][0]
    kw = [u1[m][0] for m in KW_MODELLE]
    if "eingetroffen" in kw:
        res["urteile_kartenwortlaut"]["TR1"] = "eingetroffen"
    elif all(x == "nicht eingetroffen" for x in kw):
        res["urteile_kartenwortlaut"]["TR1"] = "nicht eingetroffen"
    else:
        res["urteile_kartenwortlaut"]["TR1"] = "nicht auswertbar"
    res["vermerke"]["TR1"] = {m: {"urteil_regel": u1[m][0], **u1[m][1]} for m in MODELLE}
    res["vermerke"]["TR1_kw_modelle_mit_treffer"] = [m for m in KW_MODELLE if u1[m][0] == "eingetroffen"]
    # Takt-Umkehr: Netto je Rand und Luecke bei P4c und P4cr
    if P["P4c"] and P["P4cr"] and P["P4c"].get("zaehlung") and P["P4cr"].get("zaehlung"):
        res["vermerke"]["takt_umkehr"] = {key: [P["P4c"]["zaehlung"][key]["netto"],
                                                P["P4cr"]["zaehlung"].get(key, {}).get("netto")]
                                          for key in P["P4c"]["zaehlung"]}
    # dicke Platte
    if P["P4a"] and P["P4aL24"] and P["P4a"].get("zaehlung") and P["P4aL24"].get("zaehlung"):
        res["vermerke"]["dicke_platte"] = {key: [P["P4a"]["zaehlung"][key]["anzahl"], P["P4a"]["zaehlung"][key]["netto"],
                                                 P["P4aL24"]["zaehlung"].get(key, {}).get("anzahl"),
                                                 P["P4aL24"]["zaehlung"].get(key, {}).get("netto")]
                                           for key in P["P4a"]["zaehlung"]}
    # ---------------- TR2
    if res["urteile_plan"]["TR1"] == "eingetroffen":
        tk = P["P4a"]["tiefster_kegel"]
        ok = iso_ok(tk.get("oben")) and iso_ok(tk.get("unten"))
        res["urteile_plan"]["TR2"] = "eingetroffen" if ok else "nicht eingetroffen"
    else:
        res["urteile_plan"]["TR2"] = "nicht auswertbar"
    kwm = [m for m in KW_MODELLE if u1[m][0] == "eingetroffen"]
    if kwm:
        tk = P[kwm[0]]["tiefster_kegel"]
        kegel = [tk[r] for r in ("oben", "unten") if tk.get(r)]
        mn = min(abs(((k["knoten"]["phase"] + 3.141592653589793) % 6.283185307179586) - 3.141592653589793) for k in kegel)
        tief = [k for k in kegel
                if abs(abs(((k["knoten"]["phase"] + 3.141592653589793) % 6.283185307179586) - 3.141592653589793) - mn) < 1e-6]
        res["urteile_kartenwortlaut"]["TR2"] = "eingetroffen" if all(iso_ok(k) for k in tief) else "nicht eingetroffen"
        res["vermerke"]["TR2_kw_modell"] = kwm[0]
    else:
        res["urteile_kartenwortlaut"]["TR2"] = "nicht auswertbar"
    res["vermerke"]["TR2"] = {m: (P[m] or {}).get("tiefster_kegel") for m in MODELLE}
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("Plan:", res["urteile_plan"], flush=True)
    print("Kartenwortlaut:", res["urteile_kartenwortlaut"], flush=True)


def R_NAMEN(R):
    return [n for n in (R or {}) if n != "K_chi"]


if __name__ == "__main__":
    sys.exit(main())
