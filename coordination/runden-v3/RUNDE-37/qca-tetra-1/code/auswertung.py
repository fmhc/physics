#!/usr/bin/env python3
# QCA-TETRA-1, Runde 37: mechanische Urteile nach PLAN.md Abschnitt 4.
# Aufruf: auswertung.py OUT.json AB.json AB.log C_a.json C_a.log [C_b.json C_b.log ...]
import json
import re
import sys

FAELLE = ["L3:1+1", "L3:1+1'", "L3:1+1''", "L3:1'+1''", "L3:2", "L3:2'", "L3:2''",
          "L2:Pauli", "L2:1+1", "L2:1+chi_x", "L2:1+chi_y", "L2:1+chi_z"]


def rc_of(logpfad):
    try:
        txt = open(logpfad).read()
    except OSError:
        return None
    m = re.findall(r"rc=(\d+)", txt)
    return int(m[-1]) if m else None


def main():
    out, pab, lab = sys.argv[1:4]
    rest = sys.argv[4:]
    ab = json.load(open(pab))
    rc_ab = rc_of(lab)
    c = {"teil_C": {"C1": {}, "C2": {}}}
    rc_c, chk_c, modi_c = [], [], []
    for i in range(0, len(rest), 2):
        d = json.load(open(rest[i]))
        rc_c.append(rc_of(rest[i + 1]))
        chk_c.append(d["defekt_codepruefung_rel"])
        modi_c.append(d["modus"])
        for f in ("C1", "C2"):
            c["teil_C"][f].update(d["teil_C"][f])
    vollstaendig = all(n in c["teil_C"][f] for f in ("C1", "C2") for n in FAELLE) and all(n in ab["teil_B"] for n in FAELLE)
    urteile = {}
    g = ab["gruppen"]
    vor = {
        "rc_AB": rc_ab, "rc_C": rc_c,
        "T_ordnung": g["T_ordnung"], "T_konsistenzfehler": g["T_konsistenzfehler"],
        "2T_ordnung": g["2T_ordnung"], "2T_kern_ist_pm_I": g["2T_kern_ist_pm_I"],
        "spinor_SO3_abw": g["spinor_SO3_abw"], "wirkung_auf_S_ok": g["wirkung_auf_S_ok"],
        "L2_ordnung": g["L2_ordnung"], "V_C3_hoch3_plus_I": g["V_C3_hoch3_plus_I"],
        "defekt_codepruefung_AB": ab["defekt_codepruefung_rel"], "defekt_codepruefung_C": chk_c,
        "modus_AB": ab["modus"], "modus_C": modi_c, "faelle_vollstaendig": vollstaendig,
    }
    vor_ok = (rc_ab == 0 and len(rc_c) > 0 and all(r == 0 for r in rc_c) and vollstaendig
              and g["T_ordnung"] == 12 and g["T_konsistenzfehler"] == 0
              and g["2T_ordnung"] == 24 and g["2T_kern_ist_pm_I"] and g["spinor_SO3_abw"] <= 1e-12
              and g["wirkung_auf_S_ok"] and g["L2_ordnung"] == 4 and g["V_C3_hoch3_plus_I"] <= 1e-12
              and ab["defekt_codepruefung_rel"] <= 1e-10 and all(x <= 1e-10 for x in chk_c))

    # QT0
    tA = ab["teil_A"]
    w0 = {}
    ok0 = True
    for nm in ("A+", "A-"):
        r = tA[nm]
        im = r["implementierung"]
        a = r["koeff_maxabs"] <= 1e-12 and r["gitter_max_norm"] <= 1e-12
        b = (r["W0_minus_I"] <= 1e-12 and r["M_herm_abw"] <= 1e-12 and r["M_antikomm_abw"] <= 1e-12
             and r["v_1e-7_abw_max"] <= 1e-6)
        cc = (all(im[x]["s_min"] <= 1e-12 and im[x]["s_2"] >= 1e-3 for x in ("C2x", "C2y", "C2z"))
              and r["kommutator_plus_I"] <= 1e-12)
        w0[nm] = {"a_unitaer": a, "b_kegel": b, "c_360": cc,
                  "koeff_maxabs": r["koeff_maxabs"], "gitter_max_norm": r["gitter_max_norm"],
                  "W0_minus_I": r["W0_minus_I"], "M_antikomm_abw": r["M_antikomm_abw"],
                  "v_1e-7_abw_max": r["v_1e-7_abw_max"], "v_1e-7_min": r["v_1e-7_min"], "v_1e-7_max": r["v_1e-7_max"],
                  "kommutator_K_plus_I": r["kommutator_plus_I"],
                  "U_C2_hoch2_plus_I": {x: im[x]["U_hoch2_plus_I"] for x in ("C2x", "C2y", "C2z")},
                  "C3_s_min_kleinster": min(v["s_min"] for k, v in im.items() if k.startswith("C3")),
                  "v_0.05_streuung_std_rel": r["v_0.05_streuung_std_rel"],
                  "v_0.05_spannweite_rel": r["v_0.05_spannweite_rel"]}
        ok0 = ok0 and a and b and cc
    urteile["QT0"] = {"urteil": ("eingetroffen" if ok0 else "nicht eingetroffen") if vor_ok else "nicht auswertbar",
                      "werte": w0}

    # QT1
    B = ab["teil_B"]
    nontriv = {k: v["kegel"] + v["andere"] for k, v in B.items()}
    proj = [k for k, v in B.items() if v["art"] == "projektiv"]
    lin = [k for k, v in B.items() if v["art"] == "linear"]
    kontrolle = B["L2:Pauli"]["kegel"] >= 1
    i_ber = any(nontriv[k] >= 1 for k in proj)
    ii_ber = all(nontriv[k] == 0 for k in lin)
    proj3 = [k for k in proj if k.startswith("L3")]
    lin3 = [k for k in lin if k.startswith("L3")]
    i_k = any(nontriv[k] >= 1 for k in proj3)
    ii_k = all(nontriv[k] == 0 for k in lin3)
    if not vor_ok or not kontrolle:
        u1 = "nicht auswertbar"
    else:
        u1 = "eingetroffen" if (i_ber and ii_ber) else "nicht eingetroffen"
    u1k = ("eingetroffen" if (i_k and ii_k) else "nicht eingetroffen") if vor_ok else "nicht auswertbar"
    urteile["QT1"] = {"urteil": u1,
                      "vermerk": f"Urteil nach Kartenwortlaut (nur L_3 = T): {u1k}. Haupturteil mit der Isotropie-"
                                 f"Definition der Quelle (L_2 oder L_3), PLAN.md Abschnitt 1, Punkt 1.",
                      "werte": {"positivkontrolle_L2_Pauli_kegel": B["L2:Pauli"]["kegel"],
                                "je_fall": {k: {"art": v["art"], "dim_komplex": v["dim_komplex"], "starts": v["starts"],
                                                "treffer": v["treffer"], "kegel": v["kegel"], "trivial": v["trivial"],
                                                "andere": v["andere"], "D_min": v["D_min"], "D_median": v["D_median"]}
                                          for k, v in B.items()},
                                "urteil_kartenwortlaut": u1k}}

    # QT2
    C = c["teil_C"]
    funde = []
    for fass in ("C1", "C2"):
        for k, v in C[fass].items():
            for kl in v["klassen"]:
                if kl.get("kegel_0") and kl["streuung_std_rel"] <= 1e-3:
                    funde.append((fass, k))
    u2 = ("eingetroffen" if funde else "nicht eingetroffen") if vor_ok else "nicht auswertbar"
    urteile["QT2"] = {"urteil": u2,
                      "werte": {"funde": funde,
                                "je_fall": {fass: {k: {"treffer": v["treffer"], "D_min": v["D_min"], "dim_komplex": v["dim_komplex"],
                                                      "klassen": v["klassen"][:5]} for k, v in C[fass].items()}
                                            for fass in ("C1", "C2")}}}

    # QT3
    w3 = {}
    ok3 = True
    for nm in ("A+", "A-"):
        deg = tA[nm]["entartungen"]
        weitere = [d for d in deg if d["kegel"] and not d["gamma_aequivalent"]]
        w3[nm] = {"entartungspunkte": len(deg), "kegelpunkte": sum(1 for d in deg if d["kegel"]),
                  "kegel_ausser_Gamma": len(weitere),
                  "punkte": [{"k": [round(x, 6) for x in d["k"]], "W_wert": d["W_wert"], "kegel": d["kegel"],
                              "gamma": d["gamma_aequivalent"], "v_min": d["v_min"], "v_max": d["v_max"]} for d in deg]}
        ok3 = ok3 and len(weitere) >= 1
    urteile["QT3"] = {"urteil": ("eingetroffen" if ok3 else "nicht eingetroffen") if vor_ok else "nicht auswertbar",
                      "werte": w3}
    json.dump({"urteile": urteile, "vorbedingungen": vor, "vorbedingungen_ok": vor_ok}, open(out, "w"), indent=1)
    for k, v in urteile.items():
        print(k, v["urteil"], flush=True)


if __name__ == "__main__":
    main()
