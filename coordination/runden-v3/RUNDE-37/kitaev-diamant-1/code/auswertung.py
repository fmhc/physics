#!/usr/bin/env python3
"""KITAEV-DIAMANT-1: Urteile nach PLAN.md Abschnitt 5, mechanisch.
Aufruf: python auswertung.py <haupt.json> <rc des Hauptlaufs> <auswertung.json>
"""
import sys
import json
import os

NA = "nicht auswertbar"
VERMERK_KD3 = ("Die Quelle (Ryu) nennt keine String-Operatoren. Huepfer = Bindungsterme in Majorana-Form (Eq. 27) [S], "
               "Strings als Produkte der Huepfer nach Levin/Wen Abschnitt IV [S ueber STRINGENDE-1]; Zuordnung [M]. "
               "Nach strengem Kartenwortlaut (Test-Abschnitt: 'sofern die Quelle die String-Operatoren angibt. Sonst nur "
               "Spektrum und Erhaltungsgroessen') waere KD3 'nicht auswertbar'.")


def nur(d, wert):
    return isinstance(d, dict) and set(d.keys()) == {str(wert)}


def urteil(ok):
    return "eingetroffen" if ok else "nicht eingetroffen"


def luecke_ok(fall):
    g = fall["gitter_min"]
    Ns = sorted(int(n) for n in g)
    g1, g2 = g[str(Ns[-2])], g[str(Ns[-1])]
    km = fall["kont_min"]
    return (km >= 1e-3 and g1 >= 1e-3 and g2 >= 1e-3 and abs(g1 - g2) <= 0.02 * max(g1, g2)
            and km <= min(g1, g2) + 1e-9)


def main():
    pfad, rc, aus = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    U = {}
    if rc != 0 or not os.path.exists(pfad):
        for s in ("KD0", "KD1", "KD2", "KD3"):
            U[s] = {"urteil": NA, "vermerk": "Lauf fehlt oder rc=%d" % rc, "werte": {}}
        json.dump({"urteile": U, "quelle": pfad, "rc": rc}, open(aus, "w"), indent=1, ensure_ascii=False)
        return
    E = json.load(open(pfad))

    # ---------------- KD0
    k0 = E["kd0"]
    df = k0["dirac"]["fehler"]
    lese_ok = df["eq24_dirac"] == 0 and df["zeta_gleich_i_alpha_g45"] == 0
    a_ok = all(df[k] == 0 for k in ("alpha_nicht_hermitesch", "alpha_quadrat", "alpha_paar_kommutiert",
                                     "zeta_nicht_hermitesch", "zeta_quadrat", "zeta_paar_kommutiert"))
    gl = k0["gitter"]
    struktur = {}
    for name, r in gl.items():
        L = r["L"]
        if L >= 3:
            struktur[name] = (r["sechsecke"] == 4 * L ** 3 and r["sechsecke_je_knoten"] == [12]
                              and r["typmuster_fehler"] == 0)
    struktur_ok = len(struktur) >= 1 and all(struktur.values())
    b_ok = all(r["H_gegen_W_antikommut"] == 0 and r["W_paar_antikommut"] == 0 and r["W_nicht_hermitesch"] == 0
               and r["W_quadrat_fehler"] == 0 for r in gl.values())
    w0 = {"dirac_fehler": df, "gitter": {n: {k: r[k] for k in ("L", "sechsecke", "sechsecke_je_knoten",
                                                                  "H_gegen_W_paare", "H_gegen_W_antikommut",
                                                                  "W_paare", "W_paar_antikommut",
                                                                  "W_nicht_hermitesch", "W_quadrat_fehler",
                                                                  "W_alpha_ungleich_W_zeta", "W_normierung",
                                                                  "relationen", "relation_produkt_phasen",
                                                                  "relation_nicht_phase")}
                                          for n, r in gl.items()},
          "struktur_ok": struktur, "lesepruefung_ok": lese_ok, "teile_ok": {"a_gamma": a_ok, "b_schleifen": b_ok}}
    if not (lese_ok and struktur_ok):
        U["KD0"] = {"urteil": NA, "vermerk": "Lesepruefung Eq. (24)/(3) oder Gitterstruktur verfehlt", "werte": w0}
    else:
        U["KD0"] = {"urteil": urteil(a_ok and b_ok), "werte": w0}

    # ---------------- KD1
    k1 = E["kd1"]
    kn = k1["knoten"]
    kn_ok = all(v == 0 for v in kn["fehler"].values())
    for s, d in kn["sektoren"].items():
        e25 = d["Eq25_G5_gegen_i_G4_P4"]
        if not (len(set(e25)) == 1 and e25[0] in ("+", "-") and d["Eq24_P4_gegen_G45"] in ("+", "-")):
            kn_ok = False
    mg = k1["gitter_L3"]
    mg_ok = all(v == 0 for v in mg["fehler"].values()) and mg["schleife_nicht_pm_prod_u"] == 0
    se = {k: v for k, v in k1["sechseck_ed"].items() if isinstance(v, dict)}
    se_ok = len(se) >= 1 and all(
        r["abw_plus"] is not None and r["abw_minus"] is not None and r["abw_plus"] < 1e-8 and r["abw_minus"] < 1e-8
        and r["anzahl_plus"] == 2048 and r["anzahl_minus"] == 2048 and r["W_gegen_Hterme_antikommut"] == 0
        for r in se.values())
    cl = k1["cluster112"]
    cl_ok = len(cl) >= 1 and all(
        r["abw_spin_gegen_ext"] is not None and r["abw_spin_gegen_ext"] < 1e-9
        and r["abw_spin_gegen_frei_projiziert"] is not None and r["abw_spin_gegen_frei_projiziert"] < 1e-8
        and r["c_projektion"] in (1, -1) and r["phys_dim"] == 256 and r["ext_terme_aus_phys_raus"] == 0
        for r in cl.values())
    abb_ok = kn_ok and mg_ok and se_ok and cl_ok
    kr = k1["kraum"]
    cp = kr["code_pruefung"]
    fr = k1["fluss_realraum"]
    code_ok = cp["reduziert_gegen_eq31"] < 1e-10 and cp["J1_gegen_4ccc_minus_i_sss"] < 1e-10 and all(
        v["abw_realraum_gegen_kraum"] < 1e-9 for v in fr.values())
    j1 = kr["J1"]
    gm = j1["gitter_min"]
    odd = sorted(int(n) for n in gm if int(n) % 2 == 1)
    ref = 33 if 33 in odd else odd[0]
    schrumpf = gm[str(odd[-1])] < gm[str(ref)] / 3.0
    null_ok = j1["kont_min"] < 1e-8 and schrumpf
    steig = j1["steigung_loglog"]
    form_ok = steig is not None and steig >= 1.5
    w1 = {"abbildung": {"knoten": kn, "gitter_L3": {k: mg[k] for k in ("fehler", "schleife_sigma",
                                                                         "schleife_nicht_pm_prod_u",
                                                                         "normierung_gleich_spin", "anzahl")},
                        "sechseck_ed": k1["sechseck_ed"], "cluster112": cl,
                        "teile_ok": {"knoten": kn_ok, "gitter": mg_ok, "sechseck_ed": se_ok, "cluster112": cl_ok}},
          "spektrum_J1": {"gitter_min": gm, "kont_min": j1["kont_min"], "nullen_gefunden": j1["nullen_gefunden"],
                          "ungerade_N_schrumpft": schrumpf, "volumenanteil": j1["volumenanteil"],
                          "deltas": j1["deltas"], "steigung_loglog": steig,
                          "form": ("Linien" if steig is not None and 1.5 <= steig < 2.5 else
                                   ("Punkte" if steig is not None and steig >= 2.5 else "Flaeche oder unklar")),
                          "nullstellen_lage": j1["nullstellen_lage"]},
          "code_pruefung": cp, "code_ok": code_ok,
          "u1_beschreibend": k1.get("u1_L3"),
          "fluss_realraum_beschreibend": fr}
    if not code_ok:
        U["KD1"] = {"urteil": NA, "vermerk": "Codepruefung Impulsraum (Eq. 31) verfehlt", "werte": w1}
    else:
        U["KD1"] = {"urteil": urteil(abb_ok and null_ok and form_ok), "werte": w1}

    # ---------------- KD2
    k2 = E["kd2"]
    f = k2["faelle"]
    prim = luecke_ok(f["J0_4"])
    alt = luecke_ok(f["J0_2"])
    sym_ok = all(abs(f[n]["kont_min"] - f["J0_4"]["kont_min"]) < 1e-6 for n in ("J3_4", "J1_4"))
    scan_abw = max(abs(s["kont_min"] - s["vorhersage_schreibtisch"]) for s in k2["scan"])
    w2 = {"J0_4_primaer": f["J0_4"], "J0_2_lesart_faktor2": f["J0_2"], "luecke_J0_4": prim, "luecke_J0_2": alt,
          "andere_richtung_gleich": sym_ok, "scan": k2["scan"], "scan_max_abw_von_max(0,J0-3)": scan_abw}
    verm2 = ("Schreibtisch [M]: Luecke genau dann, wenn J_max > Summe der anderen drei (hier J0 > 3), "
             "Luecke = J0 - 3. Lesart 'Faktor 2' (J0 = 2): Luecke %s." % ("ja" if alt else "nein"))
    if not code_ok:
        U["KD2"] = {"urteil": NA, "vermerk": "Codepruefung Impulsraum verfehlt; " + verm2, "werte": w2}
    else:
        U["KD2"] = {"urteil": urteil(prim), "vermerk": verm2, "werte": w2}

    # ---------------- KD3
    k3 = E["kd3"]
    lok = k3["lokal_L4"]
    lang = k3["lang_L8"]
    inkons = sum(lok[s]["inkonsistent"] for s in lok) + sum(lang[s]["inkonsistent"] for s in ("a", "z", "az"))
    durch = {s: {p: v["passt"] for p, v in lang[s]["durchgang"].items() if isinstance(v, dict)}
             for s in ("a", "z", "az")}
    durch_ok = all(all(v.values()) for v in durch.values())
    ktrl_ok = nur(lok["az"]["V1"], 1) and nur(lang["az"]["V1"], 1) and lang["az"]["nicht_lokal"] == 0
    ferm = {}
    for s in ("a", "z"):
        ferm[s] = (nur(lok[s]["V1"], -1) and nur(lang[s]["V1"], -1) and lang[s]["endpunkt_fehler"] == 0
                   and lang[s]["aequivalenz_fehler"] == 0 and lang[s]["fluss_antikommut"] == 0)
    w3 = {"lokal_L4": lok, "lang_L8": {s: {k: lang[s][k] for k in ("V1", "anzahl", "inkonsistent", "endpunkt_fehler",
                                                                   "aequivalenz_fehler", "fluss_antikommut",
                                                                   "fluss_geprueft", "nicht_lokal", "durchgang")}
                                       for s in ("a", "z", "az")},
          "pfadlaengen_bezug": lang.get("pfadlaengen_bezug"), "inkonsistent_V1_V2_V3": inkons,
          "kontrolle_verbund_az_bosonisch": ktrl_ok, "durchgang_ok": durch_ok, "fermion_teile_ok": ferm}
    if inkons != 0 or not ktrl_ok or not durch_ok:
        U["KD3"] = {"urteil": NA, "vermerk": "V1/V2/V3 inkonsistent oder Kontrolle (Verbund, Durchgang) verfehlt. "
                    + VERMERK_KD3, "werte": w3}
    else:
        U["KD3"] = {"urteil": urteil(all(ferm.values())), "vermerk": VERMERK_KD3, "werte": w3}

    out = {"urteile": U, "quelle": pfad, "rc": rc, "laufzeit_s": E.get("laufzeit_s"), "meta": E.get("meta")}
    with open(aus + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    os.replace(aus + ".tmp", aus)
    print({s: U[s]["urteil"] for s in U})


if __name__ == "__main__":
    main()
