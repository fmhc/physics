#!/usr/bin/env python3
"""STRINGENDE-1: Urteile nach PLAN.md Abschnitt 5, mechanisch.
Aufruf: python auswertung.py <haupt.json> <rc des Hauptlaufs> <auswertung.json>
"""
import sys
import json
import os

NA = "nicht auswertbar"


def nur(d, wert):
    return isinstance(d, dict) and set(d.keys()) == {str(wert)}


def einzelwert(dicts):
    keys = set()
    for d in dicts:
        keys |= set(d.keys())
    return keys.pop() if len(keys) == 1 else None


def urteil(ok):
    return "eingetroffen" if ok else "nicht eingetroffen"


def main():
    pfad, rc, aus = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    U = {}
    K = {}
    if rc != 0 or not os.path.exists(pfad):
        for s in ("SE0", "SE1", "SE2", "SE3"):
            U[s] = {"urteil": NA, "vermerk": "Lauf fehlt oder rc=%d" % rc, "werte": {}}
        json.dump({"urteile": U, "kontrollen": K, "quelle": pfad, "rc": rc}, open(aus, "w"), indent=1, ensure_ascii=False)
        return
    E = json.load(open(pfad))
    z = E["zweiD"]
    d = E["dreiD"]
    G = ["G1", "G2", "G3", "G4"]

    # ---------------- Gegenproben
    durch2 = {g: {p: v["passt"] for p, v in z["durchgang"][g].items() if isinstance(v, dict)} for g in G}
    durch2_ok = all(all(v.values()) for v in durch2.values())
    durch3 = {p: v["passt"] for p, v in d["lang_L8"]["durchgang"].items() if isinstance(v, dict)}
    durch3_ok = all(durch3.values())
    tc = d["torus3d_kontrolle"]
    tc_ok = nur(tc["V1"], 1) and tc["endpunkt_fehler"] == 0 and tc["inkonsistent"] == 0 and tc["A_gegen_B_antikommut"] == 0
    K["durchgang_2D"] = {"passt": durch2_ok, "einzeln": durch2}
    K["durchgang_3D"] = {"passt": durch3_ok, "einzeln": durch3}
    K["torus3d_bosonisch"] = {"passt": tc_ok, "V1": tc["V1"], "endpunkt_fehler": tc["endpunkt_fehler"],
                              "anzahl": tc["anzahl"]}

    inkons_2d = sum(z["lang"][g][s]["inkonsistent"] for g in G for s in z["lang"][g]) \
        + sum(z["zweilagen"][g][s]["inkonsistent"] for g in G for s in z["zweilagen"][g]) \
        + sum(z["lokal"][s]["inkonsistent"] for s in z["lokal"])

    # ---------------- SE0
    ep = sum(z["lang"][g][s]["endpunkt_fehler"] for g in G for s in z["lang"][g]) \
        + sum(z["zweilagen"][g][s]["endpunkt_fehler"] for g in G for s in z["zweilagen"][g]) \
        + z["gegenseitig"]["paar_endpunkt_fehler"]
    eindeutig = {g + "/" + s: len(z["lang"][g][s]["V1"]) == 1 for g in G for s in z["lang"][g]}
    eindeutig.update({g + "/" + s: len(z["zweilagen"][g][s]["V1"]) == 1 for g in G for s in z["zweilagen"][g]})
    aeq = sum(z["lang"][g][s]["aequivalenz_fehler"] for g in G for s in z["lang"][g]) \
        + sum(z["zweilagen"][g][s]["aequivalenz_fehler"] for g in G for s in z["zweilagen"][g])
    stab = z["stabilisatoren"]["paar_fehler"]
    w0 = {"endpunkt_fehler": ep, "wegunabhaengig_alle": all(eindeutig.values()),
          "nicht_eindeutig": [k for k, v in eindeutig.items() if not v], "aequivalenz_fehler": aeq,
          "stabilisator_paar_fehler": stab,
          "strings_geprueft": sum(3 * z["lang"][g][s]["anzahl"] for g in G for s in z["lang"][g])
          + sum(3 * z["zweilagen"][g][s]["anzahl"] for g in G for s in z["zweilagen"][g]) + 3}
    if not durch2_ok:
        U["SE0"] = {"urteil": NA, "vermerk": "Durchgangsprobe 2D weicht ab", "werte": w0}
    else:
        U["SE0"] = {"urteil": urteil(ep == 0 and all(eindeutig.values()) and aeq == 0 and stab == 0), "werte": w0}

    # ---------------- SE1
    lang = z["lang"]
    w1 = {g: {s: lang[g][s]["V1"] for s in ("e", "m", "eps")} for g in G}
    w1["lokal"] = {s: z["lokal"][s]["V1"] for s in z["lokal"]}
    w1["anzahl_lang"] = sum(lang[g][s]["anzahl"] for g in G for s in ("e", "m", "eps"))
    w1["anzahl_lokal"] = sum(z["lokal"][s]["anzahl"] for s in z["lokal"])
    w1["inkonsistent_V1_V2_V3"] = inkons_2d
    w1["drehung_2pi_beschreibend"] = z["drehung"]
    ok1 = all(nur(lang[g]["e"]["V1"], 1) and nur(lang[g]["m"]["V1"], 1) and nur(lang[g]["eps"]["V1"], -1) for g in G) \
        and nur(z["lokal"]["eps_fig3"]["V1"], -1) and nur(z["lokal"]["e"]["V1"], 1) and nur(z["lokal"]["m"]["V1"], 1)
    if inkons_2d != 0 or not durch2_ok:
        U["SE1"] = {"urteil": NA, "vermerk": "V1/V2/V3 inkonsistent oder Durchgangsprobe 2D weicht ab", "werte": w1}
    else:
        U["SE1"] = {"urteil": urteil(ok1), "werte": w1}

    # ---------------- SE2
    gg = z["gegenseitig"]

    def klassen_ok(r):
        ks = r["klassen"].keys()
        return any(k.endswith(":-1") for k in ks) and any(k.endswith(":1") for k in ks)

    a_ok = gg["e_um_m"]["abweichungen"] == 0 and gg["m_um_e"]["abweichungen"] == 0 \
        and klassen_ok(gg["e_um_m"]) and klassen_ok(gg["m_um_e"]) \
        and gg["e_um_m"]["schleife_nicht_stabilisator"] == 0 and gg["m_um_e"]["schleife_nicht_stabilisator"] == 0
    b_ok = gg["lokal_abschnitt_V"]["fehler"] == 0
    zer = {g: lang[g]["eps"]["zerlegung"] for g in G}
    c_ok = all(nur(zer[g]["z_teil"], 1) and nur(zer[g]["x_teil"], 1) and nur(zer[g]["kreuz"], -1)
               and zer[g]["produkt_gleich_V1_fehler"] == 0 for g in G)
    zl = z["zweilagen"]
    d_ok = all(nur(zl[g]["e0m1"]["V1"], 1) and nur(zl[g]["e1m0"]["V1"], 1) and nur(zl[g]["e0m0"]["V1"], -1)
               and nur(zl[g]["e1m1"]["V1"], -1) for g in G)
    th_e = einzelwert([lang[g]["e"]["V1"] for g in G])
    th_m = einzelwert([lang[g]["m"]["V1"] for g in G])
    th_eps = einzelwert([lang[g]["eps"]["V1"] for g in G])
    M_vals = {k.split(":")[1] for k in gg["e_um_m"]["klassen"] if k.startswith("1_umschlossen")}
    M_em = M_vals.pop() if len(M_vals) == 1 else None
    try:
        e_ok = int(th_eps) == int(th_e) * int(th_m) * int(M_em)
    except (TypeError, ValueError):
        e_ok = False
    w2 = {"a_schleifen": {"e_um_m": gg["e_um_m"], "m_um_e": gg["m_um_e"]},
          "b_lokal_abschnitt_V": gg["lokal_abschnitt_V"], "c_zerlegung": zer,
          "d_zweilagen": {g: {s: zl[g][s]["V1"] for s in zl[g]} for g in G},
          "e_bandrelation": {"theta_e": th_e, "theta_m": th_m, "M_em": M_em, "theta_eps": th_eps, "gilt": e_ok},
          "teile_ok": {"a": a_ok, "b": b_ok, "c": c_ok, "d": d_ok, "e": e_ok},
          "eps_um_eps_beschreibend": gg["eps_um_eps_beschreibend"]}
    if inkons_2d != 0:
        U["SE2"] = {"urteil": NA, "vermerk": "V1/V2/V3 inkonsistent", "werte": w2}
    else:
        U["SE2"] = {"urteil": urteil(a_ok and b_ok and c_ok and d_ok and e_ok), "werte": w2}

    # ---------------- SE3
    alg = d["algebra"]["fehler"]
    L4, L6, l8 = d["L4"], d.get("L6"), d["lang_L8"]
    modell = [L4] + ([L6] if L6 else [])
    m_ok = all(sum(alg.values()) == 0 for _ in [0]) and L6 is not None and all(
        m["F_nicht_hermitesch"] == 0 and m["F_quadrat_fehler"] == 0 and m["F_paar_antikommut"] == 0
        and m["huepfer_fehler"] == 0 for m in modell)
    h10_ok = L4["zehn_huepfer_fehler"] == 0
    lok_ok = nur(L4["lokal"]["V1"], -1)
    lang_ok = nur(l8["V1"], -1) and l8["endpunkt_fehler"] == 0 and l8["aequivalenz_fehler"] == 0 \
        and l8["mittelkante_alle_beine_gleich"]
    wuerfel = {"L4": L4["wuerfelprodukt"], "L6": L6["wuerfelprodukt"] if L6 else None}
    w3 = {"algebra_fehler": alg, "algebra_anzahl": d["algebra"]["anzahl"],
          "modell": {m["L"] if isinstance(m, dict) else "?": {k: m[k] for k in ("plaketten", "F_nicht_hermitesch",
                                                                          "F_quadrat_fehler", "F_paar_antikommut",
                                                                          "huepfer_geprueft", "huepfer_fehler")}
                     for m in modell},
          "zehn_huepfer_fehler": L4["zehn_huepfer_fehler"], "lokal_L4": L4["lokal"],
          "lang_L8": {k: l8[k] for k in ("V1", "anzahl", "endpunkt_fehler", "aequivalenz_fehler", "inkonsistent",
                                         "mittelkante_alle_beine_gleich")},
          "wuerfelprodukt_beschreibend": wuerfel,
          "teile_ok": {"nachbau": m_ok, "zehn_huepfer": h10_ok, "lokal": lok_ok, "lang": lang_ok}}
    inkons_3d = L4["lokal"]["inkonsistent"] + l8["inkonsistent"] + tc["inkonsistent"]
    vermerk = None
    if not all(nur(w, 1) for w in wuerfel.values() if w is not None):
        vermerk = "Wuerfelprodukt weicht von +1 (Quelle) ab; beschreibend, nicht im Urteil (PLAN 5)"
    if not tc_ok or not durch3_ok or inkons_3d != 0:
        U["SE3"] = {"urteil": NA, "vermerk": "Kontrolle 3D (Torus-Code, Durchgang) oder Konsistenz verfehlt", "werte": w3}
    else:
        U["SE3"] = {"urteil": urteil(m_ok and h10_ok and lok_ok and lang_ok), "werte": w3}
        if vermerk:
            U["SE3"]["vermerk"] = vermerk

    out = {"urteile": U, "kontrollen": K, "quelle": pfad, "rc": rc, "laufzeit_s": E.get("laufzeit_s"),
           "meta": E.get("meta")}
    with open(aus + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False, sort_keys=False)
    os.replace(aus + ".tmp", aus)
    print({s: U[s]["urteil"] for s in U})


if __name__ == "__main__":
    main()
