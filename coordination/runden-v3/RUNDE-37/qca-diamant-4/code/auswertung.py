#!/usr/bin/env python3
# QCA-DIAMANT-4, Runde 38: mechanische Urteile nach PLAN.md Abschnitt 5.
# Aufruf (nur ueber kleintest.sh auf der .69): auswertung.py OUT.json L1.json L1.log [L2.json L2.log ...]
# Erwartet: ein Lauf Teil 0, vier Laeufe Teil A (Fassung 1/2 x Variante frei/w0), zwei Laeufe Teil B (frei/w0).
import json
import re
import sys

T_S4 = ["T:1+1+1+1", "T:1+1+1+1'", "T:1+1+1+1''", "T:1+1+1'+1'", "T:1+1+1'+1''", "T:1+3", "T:1'+3", "T:2+2",
        "T:2+2'", "T:2+2''"]
L2_S4 = ["L2:1+1+1+1", "L2:1+1+1+x", "L2:1+1+x+x", "L2:1+1+x+y", "L2:1+1+y+z", "L2:1+1+x+z", "L2:1+x+y+z", "L2:P+P"]
S2 = ["T:1+1", "T:1+1'", "T:1+1''", "T:1'+1''", "T:2", "T:2'", "T:2''", "L2:Pauli", "L2:1+1", "L2:1+chi_x",
      "L2:1+chi_y", "L2:1+chi_z"]


def rc_of(logpfad):
    try:
        txt = open(logpfad).read()
    except OSError:
        return None
    m = re.findall(r"rc=(\d+)", txt)
    return int(m[-1]) if m else None


def main():
    out = sys.argv[1]
    rest = sys.argv[2:]
    laeufe = []
    for i in range(0, len(rest), 2):
        d = json.load(open(rest[i]))
        d["_rc"] = rc_of(rest[i + 1])
        d["_datei"] = rest[i]
        laeufe.append(d)
    teil0 = [d for d in laeufe if d["teil"] == "0"]
    teilA, teilB = {}, {}
    for d in laeufe:
        if d["teil"] == "A":
            teilA.setdefault((d["fassung"], d["variante"]), []).append(d)
        elif d["teil"] == "B":
            teilB.setdefault(d["variante"], []).append(d)

    def zusammen(ds):
        z = dict(ds[0])
        z["faelle"] = {}
        for d in ds:
            z["faelle"].update(d["faelle"])
        return z

    teilA = {k: zusammen(v) for k, v in teilA.items()}
    teilB = {k: zusammen(v) for k, v in teilB.items()}
    # Vorbedingungen
    vor = {"rc": {d["_datei"]: d["_rc"] for d in laeufe}, "modus": sorted(set(d["modus"] for d in laeufe))}
    ok = all(d["_rc"] == 0 for d in laeufe) and vor["modus"] == ["haupt"]
    for d in laeufe:
        g = d["gruppen"]
        ok = ok and (g["T_ordnung"] == 12 and g["T_konsistenzfehler"] == 0 and g["2T_ordnung"] == 24
                     and g["2T_kern_ist_pm_I"] and g["spinor_SO3_abw"] <= 1e-12 and g["wirkung_auf_S_ok"]
                     and g["L2_ordnung"] == 4 and g["V_C3_hoch3_plus_I"] <= 1e-12
                     and d["defekt_codepruefung_rel"] <= 1e-10)
        for nm, r in d["darstellungen"].items():
            ok = ok and (r["projektiv_abw"] <= 1e-12 and r["unitaer_abw"] <= 1e-12
                         and ((r["kommutator_C2x_C2y"] == "-I") == (r["art"] == "projektiv"))
                         and r["kommutator_C2x_C2y"] in ("-I", "+I"))
        for k, st in d["faelle"].items():
            ok = ok and st["projektor_abw"] <= 1e-10
    voll = (len(teil0) == 1 and all(("d1|" + n) in teil0[0]["faelle"] for n in S2)
            and all(("bcc|" + n) in teil0[0]["faelle"] for n in ("L2:Pauli", "L2:1+chi_x", "T:2")))
    for fa in ("1", "2"):
        for va in ("frei", "w0"):
            d = teilA.get((fa, va))
            art = "d1" if fa == "1" else "cayley"
            voll = voll and d is not None and all((art + "|" + n) in d["faelle"] for n in T_S4 + L2_S4)
    for va in ("frei", "w0"):
        d = teilB.get(va)
        voll = voll and d is not None and all(("bcc|" + n) in d["faelle"] for n in T_S4)
    vor["faelle_vollstaendig"] = voll
    ok = ok and voll
    vor["defekt_codepruefung"] = {d["_datei"]: d["defekt_codepruefung_rel"] for d in laeufe}
    urteile = {}

    # QD0
    if teil0:
        f0 = teil0[0]["faelle"]
        pos = f0["bcc|L2:Pauli"].get("kegel_0", 0)
        d1_treffer = {n: f0["d1|" + n]["treffer"] for n in S2 if ("d1|" + n) in f0}
        i0 = pos >= 1
        ii0 = len(d1_treffer) == 12 and all(v == 0 for v in d1_treffer.values())
        u0 = ("eingetroffen" if (i0 and ii0) else "nicht eingetroffen") if ok else "nicht auswertbar"
        urteile["QD0"] = {"urteil": u0, "werte": {
            "BCC_L2_Pauli_treffer": f0["bcc|L2:Pauli"]["treffer"], "BCC_L2_Pauli_kegel_0": pos,
            "BCC_L2_Pauli_D_min": f0["bcc|L2:Pauli"]["D_min"],
            "BCC_L2_1+chi_x_treffer": f0["bcc|L2:1+chi_x"]["treffer"], "BCC_L2_1+chi_x_D_min": f0["bcc|L2:1+chi_x"]["D_min"],
            "BCC_T_2_treffer": f0["bcc|T:2"]["treffer"], "BCC_T_2_D_min": f0["bcc|T:2"]["D_min"],
            "Diamant_s2_treffer": d1_treffer,
            "Diamant_s2_D_min": {n: f0["d1|" + n]["D_min"] for n in S2 if ("d1|" + n) in f0}}}
        kontrolle = i0
    else:
        urteile["QD0"] = {"urteil": "nicht auswertbar", "werte": {}}
        kontrolle = False

    # QD1 und QD2
    qd1 = []
    qd1_alt = []
    tabA = {}
    for (fa, va), d in sorted(teilA.items()):
        for k, st in d["faelle"].items():
            wk = {"projektiv": 0, "linear": 0, "mehrdeutig": 0}
            typen = {}
            for h in st["hits"]:
                if h["klass"].get("kegel_0_alt"):
                    qd1_alt.append({"fassung": fa, "variante": va, "fall": k,
                                    "wirkung": h.get("dreihundertsechzig", {}).get("wirkung", "nicht berechnet (neu trivial)")})
                if h["kegel_0"]:
                    w = h["dreihundertsechzig"]["wirkung"]
                    wk[w] += 1
                    qd1.append({"fassung": fa, "variante": va, "fall": k, "wirkung": w})
                    for c in h["klass"]["cluster0"]:
                        if c["kegel"]:
                            t = f"{c['m']}-fach, flach {c['flache_zweige_min']}..{c['flache_zweige_max']}"
                            typen[t] = typen.get(t, 0) + 1
            tabA[f"F{fa}|{va}|{k}"] = {"dim_je_block": st["dim_komplex_je_block"], "treffer": st["treffer"],
                                       "kegel_0": st.get("kegel_0", 0), "trivial": st.get("trivial", 0),
                                       "D_min": st["D_min"], "D_median": st["D_median"], "wirkung_bei_kegel": wk,
                                       "kegeltypen": typen}
    if not ok or not kontrolle:
        u1 = "nicht auswertbar"
    else:
        u1 = "eingetroffen" if qd1 else "nicht eingetroffen"
    u1_f1 = ("eingetroffen" if any(q["fassung"] == "1" for q in qd1) else "nicht eingetroffen") if u1 != "nicht auswertbar" else u1
    u1_alt = ("eingetroffen" if qd1_alt else "nicht eingetroffen") if u1 != "nicht auswertbar" else u1
    urteile["QD1"] = {"urteil": u1, "vermerk": f"nur Fassung 1 (Kartenwortlaut, = gleichzeitiger Sprung): {u1_f1}; "
                                               f"nach der Kegelregel vor Rauchlauf 1 (ohne Kommutatortest): {u1_alt}",
                      "werte": {"zahl_treffer_mit_kegel_0": len(qd1), "urteil_nur_fassung1": u1_f1,
                                "urteil_alte_regel": u1_alt, "zahl_treffer_alte_regel": len(qd1_alt),
                                              "faelle_mit_kegel_0": sorted(set(f"F{q['fassung']}|{q['variante']}|{q['fall']}" for q in qd1)),
                                              "je_fall": tabA}}
    if u1 != "eingetroffen":
        u2 = "nicht auswertbar"
        u2_frei, u2_f1 = "nicht auswertbar", "nicht auswertbar"
    else:
        u2 = "eingetroffen" if all(q["wirkung"] == "projektiv" for q in qd1) else "nicht eingetroffen"
        frei = [q for q in qd1 if q["variante"] == "frei"]
        f1 = [q for q in qd1 if q["fassung"] == "1"]
        u2_frei = ("eingetroffen" if all(q["wirkung"] == "projektiv" for q in frei) else "nicht eingetroffen") if frei else "keine Treffer"
        u2_f1 = ("eingetroffen" if all(q["wirkung"] == "projektiv" for q in f1) else "nicht eingetroffen") if f1 else "keine Treffer"
    gegen = sorted(set(f"F{q['fassung']}|{q['variante']}|{q['fall']}:{q['wirkung']}" for q in qd1 if q["wirkung"] != "projektiv"))
    if u1_alt != "eingetroffen":
        u2_alt = "nicht auswertbar"
    else:
        u2_alt = "eingetroffen" if all(q["wirkung"] == "projektiv" for q in qd1_alt) else "nicht eingetroffen"
    urteile["QD2"] = {"urteil": u2,
                      "vermerk": f"nur Variante frei: {u2_frei}; nur Fassung 1: {u2_f1}; nach der Kegelregel vor Rauchlauf 1: "
                                 f"{u2_alt}. Haupturteil ueber beide Fassungen und Varianten (PLAN.md Abschnitt 5).",
                      "werte": {"treffer_mit_kegel_0": len(qd1),
                                "projektiv": sum(1 for q in qd1 if q["wirkung"] == "projektiv"),
                                "linear": sum(1 for q in qd1 if q["wirkung"] == "linear"),
                                "mehrdeutig": sum(1 for q in qd1 if q["wirkung"] == "mehrdeutig"),
                                "nicht_projektive_faelle": gegen, "urteil_nur_frei": u2_frei, "urteil_nur_fassung1": u2_f1}}

    # QD3
    qd3 = []
    qd3_alt = []
    tabB = {}
    for va, d in sorted(teilB.items()):
        for k, st in d["faelle"].items():
            n_k0, n_kw = 0, 0
            for h in st["hits"]:
                if not h["klass"].get("trivial_alt") and (h["klass"].get("kegel_0_alt") or
                                                          any(e.get("kegel_alt") for e in h.get("entartungen", []))):
                    qd3_alt.append(f"{va}|{k}")
                if h["klasse"] == "trivial":
                    continue
                kw = any(e["kegel"] for e in h.get("entartungen", []))
                if h["kegel_0"]:
                    n_k0 += 1
                if kw:
                    n_kw += 1
                if h["kegel_0"] or kw:
                    qd3.append(f"{va}|{k}")
            tabB[f"{va}|{k}"] = {"dim": st["dim_komplex_je_block"], "treffer": st["treffer"], "trivial": st.get("trivial", 0),
                                 "kegel_0": n_k0, "kegel_anderswo_in_untersuchten": n_kw, "D_min": st["D_min"],
                                 "D_median": st["D_median"]}
    if not ok or not kontrolle:
        u3 = "nicht auswertbar"
    else:
        u3 = "eingetroffen" if qd3 else "nicht eingetroffen"
    u3_alt = ("eingetroffen" if qd3_alt else "nicht eingetroffen") if u3 != "nicht auswertbar" else u3
    urteile["QD3"] = {"urteil": u3, "vermerk": f"nach der Kegelregel vor Rauchlauf 1 (ohne Kommutatortests): {u3_alt}",
                      "werte": {"faelle_mit_kegel": sorted(set(qd3)), "faelle_alte_regel": sorted(set(qd3_alt)),
                                "urteil_alte_regel": u3_alt, "je_fall": tabB}}
    json.dump({"urteile": urteile, "vorbedingungen": vor, "vorbedingungen_ok": ok}, open(out, "w"), indent=1)
    for k, v in urteile.items():
        print(k, v["urteil"], flush=True)


if __name__ == "__main__":
    main()
