#!/usr/bin/env python3
# QCA-BCC-RUECK-1: mechanische Urteile QR0 bis QR2 aus den Laufdateien (Regeln PLAN.md Abschnitt 5).
# Aufruf (nur ueber kleintest.sh auf der .69): auswertung.py AUSGABE.json L1.json [L2.json ...]
import json
import sys

FAELLE4 = ["T:1+1+1+1", "T:1+1+1+1'", "T:1+1+1+1''", "T:1+1+1'+1'", "T:1+1+1'+1''", "T:1+3", "T:1'+3", "T:2+2",
           "T:2+2'", "T:2+2''"]
FAELLE8 = ["K1", "K2", "K3", "K4", "K5"]
VAR4 = ["frei", "r50", "r20", "r05"]
VAR8 = ["frei", "r50", "r20"]
VAR0 = ["frei", "r50", "r20"]


def vorbedingungen(laeufe):
    fehler = []
    for d in laeufe:
        if d["modus"] != "haupt":
            fehler.append(f"Modus {d['modus']} in Teil {d['teil']}")
        g = d["gruppen"]
        if not (g["T_ordnung"] == 12 and g["T_konsistenzfehler"] == 0 and g["2T_ordnung"] == 24 and g["2T_kern_ist_pm_I"]
                and g["spinor_SO3_abw"] <= 1e-12 and g["U_C2x_quadrat_plus_I"] <= 1e-12
                and g["U_R3_hoch3_plus_I"] <= 1e-12 and g["wirkung_auf_slots_ok"] and g["L2_ordnung"] == 4):
            fehler.append(f"Gruppenpruefung Teil {d['teil']}")
        for nm, r in d["darstellungen"].items():
            soll = "-I" if r["art"] == "projektiv" else "+I"
            if not (r["unitaer_abw"] <= 1e-12 and r["projektiv_abw"] <= 1e-12 and r["kommutator"] == soll):
                fehler.append(f"Darstellung {nm} Teil {d['teil']}")
        for c in d["codepruefung"]:
            if not (c["defekt_rel"] <= 1e-10 and c["J+_rel"] <= 1e-10 and c["jacobi_rel"] <= 1e-4):
                fehler.append(f"Codepruefung {c['fall']}")
        for k, st in d["faelle"].items():
            if st["projektor_abw"] > 1e-10:
                fehler.append(f"Projektor {k}")
    t0 = [d for d in laeufe if d["teil"] == "0"]
    f4 = {k for d in laeufe if d["teil"] == "4" for k in d["faelle"]}
    f8 = {k for d in laeufe if d["teil"] == "8" for k in d["faelle"]}
    if len(t0) != 1:
        fehler.append("Teil 0 fehlt oder doppelt")
    else:
        for v in VAR0:
            if "L2:Pauli|N|" + v not in t0[0]["teil0"]["qr0_suche"]:
                fehler.append("Teil 0 Variante " + v)
    for nm in FAELLE4:
        for fo in "NO":
            for v in VAR4:
                if f"4|{nm}|{fo}|{v}" not in f4:
                    fehler.append(f"fehlt 4|{nm}|{fo}|{v}")
    for nm in FAELLE8:
        for fo in "NO":
            for v in VAR8:
                if f"8|{nm}|{fo}|{v}" not in f8:
                    fehler.append(f"fehlt 8|{nm}|{fo}|{v}")
    return fehler


def nichttrivial(h):
    return not h["klass"]["trivial"]


def kegel(h):
    return bool(h["klass"]["kegel_0"])


def qr2_kandidat(h, block=True, streng=False, nur_rep=False):
    if not (h["gueltig"] and nichttrivial(h) and h["voll_eingeordnet"]):
        return False
    if not (h["rueck"]["rueck_block"] if block else h["rueck"]["rueck_matrix"]):
        return False
    iso = "isotrop_streng" if streng else "isotrop"
    ok_cl = any(c.get(iso, False) and c["spin_rep"] for c in h["klass"]["kegel_cluster"])
    if nur_rep:
        return ok_cl
    return ok_cl and h["klass"].get("am_treffer", {}).get("wirkung") == "projektiv"


def main():
    out_path = sys.argv[1]
    laeufe = [json.load(open(p)) for p in sys.argv[2:]]
    fehler = vorbedingungen(laeufe)
    alle = {}
    for d in laeufe:
        alle.update(d["faelle"])
    t0 = [d for d in laeufe if d["teil"] == "0"]
    t0 = t0[0]["teil0"] if t0 else None
    urteile = {}
    # Die Urteile werden immer gerechnet; bei verletzten Vorbedingungen gelten sie nicht (alle "nicht auswertbar") und
    # stehen nur zur Diagnose unter "diagnose_ohne_vorbedingungen".
    # QR0
    def qr0_treffer(var):
        st = t0["qr0_suche"]["L2:Pauli|N|" + var]
        return [h for h in st["hits"] if h["gueltig"] and nichttrivial(h) and h["rueck"]["rueck_block"] and kegel(h)
                and h["weyl_vergleich"]["best"] <= 1e-8]
    q0 = qr0_treffer("r50")
    q0f = qr0_treffer("frei")
    st50 = t0["qr0_suche"]["L2:Pauli|N|r50"]
    urteile["QR0"] = {"urteil": "eingetroffen" if q0 else "nicht eingetroffen",
                      "vermerk": f"Variante frei: {'eingetroffen' if q0f else 'nicht eingetroffen'} ({len(q0f)} Treffer)",
                      "werte": {"treffer_r50": st50["treffer"], "weyl_treffer_r50": len(q0), "starts": st50["starts"],
                                "weyl_abw_max": max([h["weyl_vergleich"]["best"] for h in q0], default=None),
                                "v_kegel": sorted({round(c["lin_min"], 6) for h in q0 for c in h["klass"]["kegel_cluster"]}),
                                "J+_J-": sorted({(round(h["rueck"]["J+"], 9), round(h["rueck"]["J-"], 9)) for h in q0}),
                                "r20_treffer": t0["qr0_suche"]["L2:Pauli|N|r20"]["treffer"],
                                "r20_D_min": t0["qr0_suche"]["L2:Pauli|N|r20"]["D_min"],
                                "weyl_quelle": {k: {"rueck_block": v["rueck"]["rueck_block"], "weyl": v["weyl_vergleich"]["best"],
                                                    "iso_0.05": [c["iso_0.05"]["std_rel"] for c in v["klass"]["kegel_cluster"]]}
                                                for k, v in t0["weyl_quelle"].items()}}}
    kontrolle = bool(q0)
    # QR1
    f4 = {k: v for k, v in alle.items() if k.startswith("4|")}
    gb = [(k, i) for k, st in f4.items() for i, h in enumerate(st["hits"])
          if h["gueltig"] and nichttrivial(h) and h["rueck"]["rueck_block"] and kegel(h)]
    gm = [(k, i) for k, st in f4.items() for i, h in enumerate(st["hits"])
          if h["gueltig"] and nichttrivial(h) and h["rueck"]["rueck_matrix"] and kegel(h)]
    gN = [(k, i) for (k, i) in gb if k.split("|")[2] == "N"]
    gr = [(k, i) for k, st in f4.items() for i, h in enumerate(st["hits"])
          if h["gueltig"] and nichttrivial(h) and h["rueck"]["rueck_block"]]
    graw = [(k, i) for k, st in f4.items() for i, h in enumerate(st["hits"])
            if nichttrivial(h) and h["rueck"]["rueck_block"] and kegel(h)]
    if not kontrolle:
        urteile["QR1"] = {"urteil": "nicht auswertbar", "vermerk": "Kontrolle QR0 fehlt"}
    else:
        urteile["QR1"] = {"urteil": "eingetroffen" if not gb else "nicht eingetroffen",
                          "vermerk": (f"nur Matrix-Lesart (Kartenwortlaut): {'eingetroffen' if not gm else 'nicht eingetroffen'} "
                                      f"({len(gm)}); nur Form N: {'eingetroffen' if not gN else 'nicht eingetroffen'} ({len(gN)}); "
                                      f"ohne Gueltigkeitsschwelle 1e-20: {'eingetroffen' if not graw else 'nicht eingetroffen'} ({len(graw)})"),
                          "werte": {"gegenbeispiele_block": gb[:20], "n_block": len(gb), "n_matrix": len(gm),
                                    "rueck_block_ohne_kegel_bedingung": len(gr),
                                    "treffer_je_fall": {k: st["treffer"] for k, st in f4.items()},
                                    "kategorien_je_fall": {k: st["kategorien"] for k, st in f4.items()},
                                    "D_min_je_fall": {k: st["D_min"] for k, st in f4.items()}}}
    # QR2
    f8 = {k: v for k, v in alle.items() if k.startswith("8|")}

    def zaehle(**kw):
        return [(k, i) for k, st in f8.items() for i, h in enumerate(st["hits"]) if qr2_kandidat(h, **kw)]
    kb = zaehle()
    km = zaehle(block=False)
    ks = zaehle(streng=True)
    kr = zaehle(nur_rep=True)
    kN = [(k, i) for (k, i) in kb if k.split("|")[2] == "N"]
    kall = [(k, i) for (k, i) in kb if all(c.get("isotrop", False) for c in f8[k]["hits"][i]["klass"]["kegel_cluster"])]
    kons = [k for k, e in (t0["konstruktionen"].items() if t0 else []) if e["kategorie"] == "rueck+Kegel iso proj"]
    if not kontrolle:
        urteile["QR2"] = {"urteil": "nicht auswertbar", "vermerk": "Kontrolle QR0 fehlt"}
    else:
        iso05 = [c["iso_0.05"]["std_rel"] for k, st in f8.items() for h in st["hits"]
                 if h["gueltig"] and nichttrivial(h) and h["rueck"]["rueck_block"] and h["voll_eingeordnet"]
                 for c in h["klass"]["kegel_cluster"] if "iso_0.05" in c]
        vk = [c["iso_0.05"]["v_mittel"] for k, st in f8.items() for h in st["hits"]
              if h["gueltig"] and nichttrivial(h) and h["rueck"]["rueck_block"] and h["voll_eingeordnet"]
              for c in h["klass"]["kegel_cluster"] if "iso_0.05" in c]
        urteile["QR2"] = {"urteil": "eingetroffen" if kb else "nicht eingetroffen",
                          "vermerk": (f"Matrix-Lesart: {'eingetroffen' if km else 'nicht eingetroffen'} ({len(km)}); "
                                      f"Isotropie 1e-3 bei 0,05: {'eingetroffen' if ks else 'nicht eingetroffen'} ({len(ks)}); "
                                      f"nur Form N: {'eingetroffen' if kN else 'nicht eingetroffen'} ({len(kN)}); "
                                      f"360 Grad nur ueber die Darstellung: {'eingetroffen' if kr else 'nicht eingetroffen'} ({len(kr)}); "
                                      f"alle Kegel des Automaten isotrop: {'eingetroffen' if kall else 'nicht eingetroffen'} ({len(kall)}); "
                                      f"Konstruktionen Teil 0: {len(kons)} ({', '.join(kons)})"),
                          "werte": {"kandidaten": kb[:30], "n_kandidaten": len(kb), "n_matrix": len(km), "n_streng": len(ks),
                                    "n_nur_N": len(kN), "n_nur_rep": len(kr), "n_alle_kegel_isotrop": len(kall),
                                    "iso_0.05_rueck_kegel_min": min(iso05, default=None),
                                    "iso_0.05_rueck_kegel_max": max(iso05, default=None),
                                    "v_rueck_kegel_min": min(vk, default=None), "v_rueck_kegel_max": max(vk, default=None),
                                    "treffer_je_fall": {k: st["treffer"] for k, st in f8.items()},
                                    "kategorien_je_fall": {k: st["kategorien"] for k, st in f8.items()},
                                    "D_min_je_fall": {k: st["D_min"] for k, st in f8.items()}}}
    if fehler:
        diag = urteile
        urteile = {q: {"urteil": "nicht auswertbar", "vermerk": "Vorbedingungen: " + "; ".join(fehler[:20])}
                   for q in ("QR0", "QR1", "QR2")}
        ausgabe = {"vorbedingungen_ok": False, "fehler": fehler, "urteile": urteile, "diagnose_ohne_vorbedingungen": diag}
        print("Vorbedingungen verletzt:", fehler[:12], flush=True)
        for q, u in diag.items():
            print("Diagnose", q, u["urteil"], "|", u.get("vermerk", ""), flush=True)
    else:
        ausgabe = {"vorbedingungen_ok": True, "urteile": urteile}
    json.dump(ausgabe, open(out_path, "w"), indent=1, default=lambda o: list(o) if isinstance(o, tuple) else str(o))
    for q, u in urteile.items():
        print(q, u["urteil"], "|", u.get("vermerk", ""), flush=True)


if __name__ == "__main__":
    main()
