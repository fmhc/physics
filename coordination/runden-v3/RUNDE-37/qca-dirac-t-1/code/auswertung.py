#!/usr/bin/env python3
# QCA-DIRAC-T-1, Runde 38: mechanische Urteile nach PLAN.md Abschnitt 5.
# Aufruf (nur ueber kleintest.sh auf der .69): auswertung.py OUT.json L1.json L1.log [L2.json L2.log ...]
# Erwartet: ein Lauf Teil 0, ein Lauf Teil A, ein oder mehrere Laeufe Teil B (Formen N, O, P).
import json
import re
import sys

import numpy as np

KL = ["K1", "K2", "K3", "K4", "K5"]


def rc_of(logpfad):
    try:
        txt = open(logpfad).read()
    except OSError:
        return None
    m = re.findall(r"rc=(\d+)", txt)
    return int(m[-1]) if m else None


def gueltig(h):
    return h["D_voll"] < 1e-10 and h["kovarianz_abw"] <= 1e-10


def main():
    out = sys.argv[1]
    rest = sys.argv[2:]
    laeufe = []
    for i in range(0, len(rest), 2):
        d = json.load(open(rest[i]))
        d["_rc"] = rc_of(rest[i + 1])
        d["_datei"] = rest[i]
        laeufe.append(d)
    t0 = [d for d in laeufe if d["teil"] == "0"]
    tA = [d for d in laeufe if d["teil"] == "A"]
    faelleB = {}
    for d in laeufe:
        if d["teil"] == "B":
            faelleB.update(d["faelle"])
    faelleA = {}
    for d in tA:
        faelleA.update(d["faelle"])
    vor = {"rc": {d["_datei"]: d["_rc"] for d in laeufe}, "modus": sorted(set(d["modus"] for d in laeufe))}
    ok = all(d["_rc"] == 0 for d in laeufe) and vor["modus"] == ["haupt"]
    for d in laeufe:
        g = d["gruppen"]
        ok = ok and (g["T_ordnung"] == 12 and g["T_konsistenzfehler"] == 0 and g["2T_ordnung"] == 24
                     and g["2T_kern_ist_pm_I"] and g["spinor_SO3_abw"] <= 1e-12 and g["wirkung_auf_slots_ok"]
                     and g["U_C2x_quadrat_plus_I"] <= 1e-12 and g["U_R3_hoch3_plus_I"] <= 1e-12)
        for r in d["darstellungen"].values():
            ok = ok and (r["projektiv_abw"] <= 1e-12 and r["unitaer_abw"] <= 1e-12 and r["K_plus_I"] <= 1e-12
                         and r["Vx2_plus_I"] <= 1e-12 and r["V3hoch3_plus_I"] <= 1e-12)
        for c in d["codepruefung"]:
            ok = ok and c["defekt_rel"] <= 1e-10 and c["jacobi_rel"] <= 1e-4
        for st in d["faelle"].values():
            ok = ok and st["projektor_abw"] <= 1e-10
    soll_B = [f"B|{f}|{k}" for f in "NO" for k in KL] + ["B|P|K4", "B|P|K5"]
    soll_A = ["A|N|T:2+2", "A|N-w0|T:2+2", "A|O|T:2+2"]
    voll = len(t0) == 1 and all(k in faelleB for k in soll_B) and all(k in faelleA for k in soll_A)
    vor["faelle_vollstaendig"] = voll
    vor["fehlend"] = [k for k in soll_B + soll_A if k not in faelleB and k not in faelleA]
    ok = ok and voll
    urteile = {}

    # QM-D0: Quell-Dirac-Automat (Eq. 36), E+ und E-, m = 0,1; 0,3; 0,6
    q0 = t0[0]["teil0"]["quelle_dirac"] if t0 else {}
    werte0 = {}
    alle0 = bool(q0)
    for lab, e in q0.items():
        kl = e["klass"]
        cl = kl["gamma"]["cluster"]
        m = float(lab.split("m=")[1])
        phs = sorted(c["phase"] for c in cl)
        a = float(np.arcsin(m))
        luecke_ok = (len(cl) == 2 and all(c["m"] == 2 for c in cl) and abs(phs[0] + a) <= 1e-12 and abs(phs[1] - a) <= 1e-12)
        quad = all(c["typ"] == "quadratisch" for c in cl)
        streu = max((b["std_rel"] for c in cl for b in c.get("kruemmung", [])), default=None)
        iso = streu is not None and streu <= 1e-3
        kr = e["kruemmung_abw_rel_max"]
        unit = e["unitaer_koeff_max"] <= 1e-12 and e["unitaer_gitter_max"] <= 1e-12
        passt = unit and luecke_ok and quad and iso and kr is not None and kr <= 1e-3
        alle0 = alle0 and passt
        werte0[lab] = {"unitaer_koeff_max": e["unitaer_koeff_max"], "unitaer_gitter_max": e["unitaer_gitter_max"],
                       "phasen_gamma": phs, "arcsin_m": a, "luecke_2arcsin_m": 2 * a, "luecke_2m": 2 * m,
                       "quadratisch": quad, "kruemmung_streuung_max": streu, "kruemmung_soll": e["kruemmung_soll_n_durch_3m"],
                       "kruemmung_abw_rel": kr, "kovarianz_L2": e["kovarianz_L2_abw"],
                       "spin_halb": kl["spin_halb_alle_cluster"], "lesepruefung_eq37": e["lesepruefung_eq37"],
                       "verdoppler": {p: [(c["m"], c["typ"]) for c in v["cluster"]] for p, v in kl.get("spezialpunkte", {}).items()},
                       "erfuellt": passt}
    u0 = ("eingetroffen" if alle0 else "nicht eingetroffen") if ok else "nicht auswertbar"
    urteile["QM-D0"] = {"urteil": u0, "vermerk": "Luecke nach Quelle 2 arccos(n) = 2 arcsin(m); woertlich 2m nur in erster Ordnung",
                        "werte": werte0}

    # Suchkontrolle T:2+2' (s = 4)
    sk = t0[0]["teil0"]["suchkontrolle_T:2+2'"] if t0 else None
    sk_ok = sk is not None and any(gueltig(h) and h["klasse"] == "Kegel bei 0" for h in sk["hits"])
    vk = []
    if sk:
        for h in sk["hits"]:
            if gueltig(h) and h["klasse"] == "Kegel bei 0":
                vk += [c["lin_min"] for c in h["klass"]["gamma"]["cluster"] if c["typ"] == "linear"]
    sk_werte = {"treffer": sk["treffer"] if sk else None, "klassen": sk.get("klassen") if sk else None,
                "D_min": sk["D_min"] if sk else None, "v_kegel_min": min(vk) if vk else None, "v_kegel_max": max(vk) if vk else None}

    # QM-D1: Teil A
    tabA = {}
    nontriv = {}
    for k in soll_A:
        st = faelleA.get(k)
        if st is None:
            continue
        nt = [h for h in st["hits"] if gueltig(h) and h["klasse"] != "trivial"]
        nontriv[k] = len(nt)
        tabA[k] = {"dim": st["dim_komplex"], "starts": st["starts"], "treffer": st["treffer"], "klassen": st.get("klassen"),
                   "D_min": st["D_min"], "D_median": st["D_median"], "nichttrivial_gueltig": len(nt)}
    if not ok or not sk_ok:
        u1 = "nicht auswertbar"
    else:
        starts_ok = all(faelleA[k]["starts"] >= 200 for k in soll_A[:2])
        u1 = "eingetroffen" if (starts_ok and nontriv.get(soll_A[0], 1) == 0 and nontriv.get(soll_A[1], 1) == 0) else "nicht eingetroffen"
    u1_o = ("eingetroffen" if nontriv.get("A|O|T:2+2", 1) == 0 else "nicht eingetroffen") if u1 != "nicht auswertbar" else u1
    urteile["QM-D1"] = {"urteil": u1, "vermerk": f"mit Vor-Ort-Term (Form O, erweitert): {u1_o}; Beweis S2 vorab (PLAN.md Abschnitt 3)",
                        "werte": {"je_form": tabA, "suchkontrolle_T:2+2'": sk_werte, "suchkontrolle_ok": sk_ok}}

    # QM-D2, QM-D3: Teil B (Suche) und Konstruktionen
    kand, tabB = [], {}
    for k in soll_B:
        st = faelleB.get(k)
        if st is None:
            continue
        z = {"massiv": 0, "massiv_spin": 0, "massiv_isotrop": 0, "Kegel bei 0": 0, "sonst": 0, "trivial": 0,
             "teilweise_massiv": 0, "inversionssymmetrisch": 0, "ungueltig": 0}
        streu = []
        for h in st["hits"]:
            if not gueltig(h):
                z["ungueltig"] += 1
                continue
            kl = h["klass"]
            z[h["klasse"]] += 1
            if not kl["trivial"] and any(c["typ"] == "quadratisch" and c["m"] == 2 and c["halbabstand"] > 1e-3
                                         for c in kl["gamma"]["cluster"]):
                z["teilweise_massiv"] += 1
            if kl.get("am_treffer", {}).get("inversion", {}).get("symmetrisch"):
                z["inversionssymmetrisch"] += 1
            if kl["massiv"] and kl["spin_halb_alle_cluster"]:
                z["massiv_spin"] += 1
                kand.append({"quelle": "suche", "fall": k, "isotrop": kl["isotrop"], "streuung": kl["kruemmung_streuung_max"],
                             "luecke": kl["luecke"]})
                streu.append(kl["kruemmung_streuung_max"])
                if kl["isotrop"]:
                    z["massiv_isotrop"] += 1
        z.update({"dim": st["dim_komplex"], "starts": st["starts"], "treffer": st["treffer"], "D_min": st["D_min"],
                  "D_median": st["D_median"], "streuung_min": min(streu) if streu else None,
                  "streuung_max": max(streu) if streu else None})
        tabB[k] = z
    kons = t0[0]["teil0"]["konstruktionen"] if t0 else {}
    tabK = {}
    for lab, e in kons.items():
        kl = e["klass"]
        g = e["unitaer_koeff_max"] <= 1e-12 and e["kovarianz_T_abw"] <= 1e-12
        cl = kl["gamma"]["cluster"]
        tabK[lab] = {"gueltig": g, "unitaer": e["unitaer_koeff_max"], "kovarianz": e["kovarianz_T_abw"],
                     "klasse": kl["klasse"], "massiv": kl["massiv"], "spin_halb": kl["spin_halb_alle_cluster"],
                     "luecke": kl["luecke"], "isotrop": kl.get("isotrop"), "streuung": kl.get("kruemmung_streuung_max"),
                     "phasen_gamma": [c["phase"] for c in cl], "typen_gamma": [c["typ"] for c in cl],
                     "lin_max_gamma": [c["lin_max"] for c in cl],
                     "kruemmung_mittel": [b["mittel"] for c in cl for b in c.get("kruemmung", [])],
                     "kruemmung_soll": e.get("kruemmung_soll_n_durch_9m"),
                     "inversion": kl.get("am_treffer", {}).get("inversion", {}).get("symmetrisch"),
                     "verdoppler": {p: [(c["m"], c["typ"], round(c["phase"], 6)) for c in v["cluster"]]
                                    for p, v in kl.get("spezialpunkte", {}).items()}}
        if g and kl["massiv"] and kl["spin_halb_alle_cluster"]:
            kand.append({"quelle": "konstruktion", "fall": lab, "isotrop": kl["isotrop"],
                         "streuung": kl["kruemmung_streuung_max"], "luecke": kl["luecke"]})
    if not ok:
        u2 = u2_s = u2_sno = "nicht auswertbar"
    else:
        u2 = "eingetroffen" if kand else "nicht eingetroffen"
        such = [c for c in kand if c["quelle"] == "suche"]
        u2_s = ("eingetroffen" if such else "nicht eingetroffen") if sk_ok else "nicht auswertbar (Suchkontrolle)"
        u2_sno = ("eingetroffen" if any(c["fall"].split("|")[1] in "NO" for c in such) else "nicht eingetroffen") if sk_ok else u2_s
    urteile["QM-D2"] = {"urteil": u2, "vermerk": f"nur Suche: {u2_s}; nur Suche ohne Inversionsbedingung (Formen N, O): {u2_sno}",
                        "werte": {"kandidaten": len(kand), "kandidaten_suche": sum(1 for c in kand if c["quelle"] == "suche"),
                                  "kandidaten_konstruktion": [c["fall"] for c in kand if c["quelle"] == "konstruktion"],
                                  "je_fall": tabB, "konstruktionen": tabK}}
    if u2 != "eingetroffen":
        u3 = "nicht auswertbar"
        u3_s = "nicht auswertbar"
    else:
        u3 = "eingetroffen" if any(c["isotrop"] for c in kand) else "nicht eingetroffen"
        such = [c for c in kand if c["quelle"] == "suche"]
        u3_s = ("eingetroffen" if any(c["isotrop"] for c in such) else "nicht eingetroffen") if such else "keine Suchtreffer"
    urteile["QM-D3"] = {"urteil": u3, "vermerk": f"nur Suchtreffer: {u3_s}",
                        "werte": {"isotrope_kandidaten": [c["fall"] for c in kand if c["isotrop"]],
                                  "streuung_je_kandidat": {c["fall"] + ("" if c["quelle"] == "konstruktion" else "#" + str(i)): c["streuung"]
                                                           for i, c in enumerate(kand)}}}
    json.dump({"urteile": urteile, "vorbedingungen": vor, "vorbedingungen_ok": ok}, open(out, "w"), indent=1)
    for k, v in urteile.items():
        print(k, v["urteil"], "|", v.get("vermerk", ""), flush=True)


if __name__ == "__main__":
    main()
