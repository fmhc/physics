#!/usr/bin/env python3
"""TWIST-PYRO-1: Urteile nach PLAN.md Abschnitt 6, mechanisch (nach Plan und nach Kartenwortlaut, Lesart S und V).
Aufruf: python auswertung.py <haupt.json> <rc des Hauptlaufs> <auswertung.json> [rauch]
(rauch: nur zum Codetest, kleinste Groessen statt der Plan-Groessen)
"""
import sys
import json
import os

NA = "nicht auswertbar"
EIN = "eingetroffen"
NEIN = "nicht eingetroffen"
ENTF = "entfaellt"
PS = ("P1", "P2", "P3")
TPS = ("TP0", "TP1", "TP2", "TP3")
GR = {"kub": ["kubisch-3", "kubisch-4"], "dia": ["diamant-2", "diamant-3"], "pyr": ["pyro-1", "pyro-2"], "g1": "kubisch-4"}
GR_RAUCH = {"kub": ["kubisch-3"], "dia": ["diamant-2"], "pyr": ["pyro-1"], "g1": "kubisch-3"}


def nur(d, wert):
    return isinstance(d, dict) and set(d.keys()) == {str(wert)}


def baustein(E, netz, P, L):
    N = E["netze"][netz]
    r = N["proj"][P]
    R = r[L]
    return {
        "generisch": r["ent_knoten"] == 0 and r["ent_schnitt"] == 0 and r["unklar"] == 0,
        "T1": N["T1a_fehler"] == 0 and N["nicht_einfach"] == 0 and N["mehrfach_fehler"] == 0
        and R["T1b"]["antikommut"] == 0,
        "T1b_antikommut": R["T1b"]["antikommut"],
        "T2": nur(R["T2"]["V1"], -1) and R["T2"]["inkonsistent"] == 0,
        "T2_V1": R["T2"]["V1"],
        "Z3": R["Z3"]["antikommut"] == 0,
        "Z3_antikommut": R["Z3"]["antikommut"],
        "inkons": R["T2"]["inkonsistent"],
    }


def t3_ok(E):
    return all(nur(N["T3"]["V1"], 1) and N["T3"]["inkonsistent"] == 0 for N in E["netze"].values())


def t3_inkons(E):
    return sum(N["T3"]["inkonsistent"] for N in E["netze"].values())


def urteile(E, L, plan):
    U = {}
    kub = [baustein(E, nz, "P1", L) for nz in GR["kub"]]
    g1 = E["netze"][GR["g1"]]["proj"]["P1"]["S"]["G1_gleichsinnig"]["antikommut"]
    # ---- TP0
    if not all(b["generisch"] for b in kub) or any(b["inkons"] for b in kub) or t3_inkons(E):
        U["TP0"] = {"urteil": NA, "vermerk": "kubisch-P1 nicht generisch oder V1/V3 inkonsistent"}
    elif plan and g1 == 0:
        U["TP0"] = {"urteil": NA, "vermerk": "Gegenprobe G1 ohne antivertauschendes Paar (Z3 unempfindlich)"}
    else:
        ok = t3_ok(E) and all(b["T2"] and b["T1"] and (b["Z3"] if plan else True) for b in kub)
        U["TP0"] = {"urteil": EIN if ok else NEIN}
    U["TP0"]["werte"] = {"T3_alle_plus1": t3_ok(E), "kubisch_P1": kub, "G1_kubisch4_P1_S": g1}

    # ---- TP1 (Diamant) und TP2 (Pyrochlor)
    def existiert(netze, felder, tp):
        werte = {P: [baustein(E, nz, P, L) for nz in netze] for P in PS}
        if plan and U["TP0"]["urteil"] != EIN:
            return {"urteil": NA, "vermerk": "Kontrolle TP0 nicht eingetroffen", "werte": werte}
        if any(b["inkons"] for P in PS for b in werte[P]):
            return {"urteil": NA, "vermerk": "V1/V3 inkonsistent", "werte": werte}
        gen = [P for P in PS if all(b["generisch"] for b in werte[P])]
        if not gen:
            return {"urteil": NA, "vermerk": "keine generische Projektion", "werte": werte}
        treffer = [P for P in gen if all(all(b[f] for f in felder) for b in werte[P])]
        return {"urteil": EIN if treffer else NEIN, "projektionen_erfuellt": treffer, "generisch": gen,
                "werte": werte}

    f1 = ("T1", "T2", "Z3") if plan else ("T1", "T2")
    U["TP1"] = existiert(GR["dia"], f1, "TP1")
    U["TP2"] = existiert(GR["pyr"], ("T1",), "TP2")
    # ---- TP3
    werte = {P: [baustein(E, nz, P, L) for nz in GR["pyr"]] for P in PS}
    if U["TP2"]["urteil"] != EIN:
        U["TP3"] = {"urteil": ENTF, "vermerk": "Bedingung TP2 nicht erfuellt", "werte": werte}
    elif not all(b["generisch"] for P in PS for b in werte[P]) or any(b["inkons"] for P in PS for b in werte[P]):
        U["TP3"] = {"urteil": NA, "vermerk": "nicht generisch oder inkonsistent", "werte": werte}
    else:
        f3 = ("T2", "Z3") if plan else ("T2",)
        ok = all(all(b[f] for f in f3) for P in PS for b in werte[P])
        U["TP3"] = {"urteil": EIN if ok else NEIN, "werte": werte}
    return U


def main():
    pfad, rc, aus = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    if len(sys.argv) > 4 and sys.argv[4] == "rauch":
        GR.clear()
        GR.update(GR_RAUCH)
    if rc != 0 or not os.path.exists(pfad):
        U = {k: {tp: {"urteil": NA, "vermerk": "Lauf fehlt oder rc=%d" % rc} for tp in TPS}
             for k in ("Plan-S", "Plan-V", "Wortlaut-S", "Wortlaut-V")}
        out = {"haupturteil": "Plan-S", "urteile": U, "quelle": pfad, "rc": rc}
    else:
        E = json.load(open(pfad))
        U = {"Plan-S": urteile(E, "S", True), "Plan-V": urteile(E, "V", True),
             "Wortlaut-S": urteile(E, "S", False), "Wortlaut-V": urteile(E, "V", False)}
        kurz = {k: {tp: U[k][tp]["urteil"] for tp in TPS} for k in U}
        kenn = {}
        for nz, N in E["netze"].items():
            kenn[nz] = {"knoten": N["knoten"], "kanten": N["kanten"], "grad": N["grad"], "schleifen": N["schleifen"],
                        "schleifen_erwartet": N["schleifen_erwartet"], "T1a_fehler": N["T1a_fehler"],
                        "nicht_einfach": N["nicht_einfach"], "mehrfach_fehler": N["mehrfach_fehler"],
                        "T3_V1": N["T3"]["V1"], "proj": {}}
            for P in PS:
                r = N["proj"][P]
                kenn[nz]["proj"][P] = {
                    "ent_knoten": r["ent_knoten"], "ent_schnitt": r["ent_schnitt"], "unklar": r["unklar"],
                    "nah": r["nah"], "fern": r["fern"], "torus_zusammenfall": r["torus_zusammenfall"],
                    "schleifen_mit_fernanteil": r["schleifen_mit_fernanteil"],
                    "huepfer_mit_fernanteil": r["huepfer_mit_fernanteil"]}
                for L in ("S", "V"):
                    R = r[L]
                    kenn[nz]["proj"][P][L] = {
                        "T1b_paare": R["T1b"]["paare"], "T1b_antikommut": R["T1b"]["antikommut"],
                        "T1b_nach_typ": R["T1b"]["nach_typ"], "T2_V1": R["T2"]["V1"],
                        "T2_inkonsistent": R["T2"]["inkonsistent"], "T2_anzahl": R["T2"]["anzahl"],
                        "Z3_paare": R["Z3"]["paare"], "Z3_antikommut": R["Z3"]["antikommut"],
                        "G1_antikommut": R["G1_gleichsinnig"]["antikommut"]}
        out = {"haupturteil": "Plan-S", "kurz": kurz, "urteile": U, "kennzahlen": kenn, "quelle": pfad, "rc": rc,
               "laufzeit_s": E.get("laufzeit_s"), "meta": E.get("meta")}
        print(json.dumps(kurz, ensure_ascii=False))
    with open(aus + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    os.replace(aus + ".tmp", aus)


if __name__ == "__main__":
    main()
