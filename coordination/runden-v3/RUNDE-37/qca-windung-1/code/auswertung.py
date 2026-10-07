#!/usr/bin/env python3
# QCA-WINDUNG-1 (Runde 41): mechanische Urteile WI0 bis WI2 nach PLAN.md Abschnitt 6, Reproduktionsprobe Stufe B.
# Start nur auf der .69 ueber kleintest.sh. Aufruf:
#   auswertung.py --dir LAUFORDNER --out auswertung.json [--modus haupt|rauch]
# Erwartet im Laufordner: kontrollen.json, stufeA_rueck*.json, stufeA_dirac*.json (Zusatz), stufeB*.json (Teillaeufe
# werden zusammengefuehrt), wiederholung_{N,Oa,Ob}.json und ref/haupt_{8Na,8Oa,8Ob}.json (gespeicherte RUECK-1-Laeufe).
import argparse
import glob
import json
import os
import sys

import numpy as np

TOL_W = 0.05
REL_D = 1e-10


def lade(p):
    if "*" in p:
        teile = [lade(q) for q in sorted(glob.glob(p))]
        if not teile:
            return None
        return {"modus": "haupt" if all(t.get("modus") == "haupt" for t in teile) else "gemischt",
                "dateien": sorted(glob.glob(p)), "automaten": [a for t in teile for a in t["automaten"]]}
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def rel(a, b):
    if a is None and b is None:
        return 0.0
    if a is None or b is None:
        return float("inf")
    if a == b:
        return 0.0
    return abs(a - b) / max(abs(b), 1e-300)


def repro(neu, alt, nur_gross=False):
    # vergleicht alle D-Werte eines wiederholten Laufs mit dem gespeicherten (strikt; Vermerk: nur Werte >= 1e-20)
    out = {"faelle": {}, "ok": True}
    for k, st in neu["faelle"].items():
        so = alt["faelle"].get(k)
        e = {"vorhanden": so is not None}
        if so is None:
            out["ok"] = False
            out["faelle"][k] = e
            continue
        dev = 0.0
        werte = []
        for key in ("D_min", "D_median", "D_max"):
            werte.append((st.get(key), so.get(key)))
        e["treffer_neu_alt"] = [st.get("treffer"), so.get("treffer")]
        e["n_hits_neu_alt"] = [len(st.get("hits", [])), len(so.get("hits", []))]
        gleich_n = st.get("treffer") == so.get("treffer") and e["n_hits_neu_alt"][0] == e["n_hits_neu_alt"][1]
        for hn, ho in zip(st.get("hits", []), so.get("hits", [])):
            for key in ("D", "D_poliert", "D_voll"):
                werte.append((hn.get(key), ho.get(key)))
        for a, b in werte:
            if nur_gross and (b is None or abs(b) < 1e-20) and (a is None or abs(a) < 1e-20):
                continue
            dev = max(dev, rel(a, b))
        e["log10D_gleich"] = st.get("log10D_alle") == so.get("log10D_alle")
        e["D_rel_max"] = dev
        e["anzahl_werte"] = len(werte)
        rn, ro = st.get("repr"), so.get("repr")
        if rn is not None and ro is not None:
            An = np.array(rn["A"]["re"]) + 1j * np.array(rn["A"]["im"])
            Ao = np.array(ro["A"]["re"]) + 1j * np.array(ro["A"]["im"])
            e["repr_A_abw"] = float(np.abs(An - Ao).max()) if An.shape == Ao.shape else float("inf")
        e["ok"] = bool(gleich_n and dev <= REL_D and e["log10D_gleich"])
        out["ok"] = out["ok"] and e["ok"]
        out["faelle"][k] = e
    return out


def zeile(a, quelle):
    w = a.get("w3", {})
    wy = a.get("weyl", {})
    lz = wy.get("luecken") or {}
    return {"name": a["name"], "quelle": quelle, "s": a["s"], "kategorie": a.get("kategorie"),
            "inversion": a["inversion"]["inversion"], "trivial": a["trivial"],
            "W3_je_gitter": {N: v["W3"] for N, v in w.get("gitter", {}).items()},
            "W3_fein": w.get("W3_fein"), "W3_rund": w.get("W3_rund"), "konvergiert": w.get("konvergiert"),
            "weyl_anzahl": wy.get("anzahl"), "weyl_vollstaendig": wy.get("vollstaendig"),
            "weyl_global": wy.get("global"), "netto_je_luecke": lz.get("netto_je_luecke"),
            "pfad_unabhaengig": lz.get("pfad_unabhaengig"), "summe_chi": wy.get("summe_chi"),
            "s_mal_W3": wy.get("s_mal_W3"), "takt_tabelle": wy.get("takt_tabelle"),
            "unitaer_abw": a["unitaer_abw"], "nachbau_ok": a["nachbau_gamma"].get("ok"),
            "wuerfel_probe": (w.get("wuerfel_probe") or {}).get("W3_wuerfel_durch_faktor")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--modus", default="haupt")
    args = ap.parse_args()
    d = args.dir
    K = lade(os.path.join(d, "kontrollen.json"))
    AR = lade(os.path.join(d, "stufeA_rueck*.json"))
    AD = lade(os.path.join(d, "stufeA_dirac*.json"))
    BB = lade(os.path.join(d, "stufeB*.json"))
    res = {"modus": args.modus, "vorbedingungen": {}, "urteile": {}, "vermerke": {}, "tabellen": {}}
    vb = res["vorbedingungen"]
    vb["dateien"] = {"kontrollen": K is not None, "stufeA_rueck": AR is not None, "stufeA_dirac": AD is not None,
                     "stufeB": BB is not None}
    vb["alle_haupt"] = all(x is not None and x.get("modus") == "haupt" for x in (K, AR, BB))
    # Reproduktionsprobe Stufe B
    rp = {}
    rp_ok, rp_ok_gross = True, True
    for nm, ref in (("N", "haupt_8Na.json"), ("Oa", "haupt_8Oa.json"), ("Ob", "haupt_8Ob.json")):
        neu = lade(os.path.join(d, f"wiederholung_{nm}.json"))
        alt = lade(os.path.join(d, "ref", ref))
        if neu is None or alt is None:
            rp[nm] = {"fehlt": True}
            rp_ok = rp_ok_gross = False
            continue
        r = repro(neu, alt)
        rg = repro(neu, alt, nur_gross=True)
        rp[nm] = {"strikt": r, "nur_D_ab_1e-20_ok": rg["ok"], "modus_neu": neu.get("modus"), "numpy_neu": neu.get("numpy"),
                  "numpy_alt": alt.get("numpy")}
        rp_ok = rp_ok and r["ok"]
        rp_ok_gross = rp_ok_gross and rg["ok"]
    res["reproduktion"] = {"je_lauf": rp, "ok_strikt": rp_ok, "ok_nur_ab_1e-20": rp_ok_gross}
    alle = []
    for J, q in ((K, "kontrolle"), (AR, "rueck_repr"), (AD, "dirac_repr"), (BB, "rueck_treffer")):
        if J is None:
            continue
        for a in J["automaten"]:
            alle.append((q, a))
    alle = [(q, a) for q, a in alle if "w3" in a]  # Rauchlauf: Projekt-Automaten ohne W3 fallen heraus
    tab = [zeile(a, q) for q, a in alle]
    res["tabellen"]["automaten"] = tab
    # Vorbedingungen der Numerik
    vb["unitaer_max"] = max((t["unitaer_abw"] for t in tab), default=None)
    vb["unitaer_ok"] = bool(vb["unitaer_max"] is not None and vb["unitaer_max"] <= 1e-8)
    jac = [abs(t["wuerfel_probe"] - t["W3_je_gitter"]["16"]) for t in tab if t["wuerfel_probe"] is not None and t["W3_je_gitter"].get("16") is not None]
    vb["jacobi_probe_max"] = max(jac) if jac else None
    vb["jacobi_ok"] = bool(jac and max(jac) <= 1e-6)
    nach = [t["nachbau_ok"] for q, t in zip([q for q, _ in alle], tab) if q in ("rueck_repr", "rueck_treffer") and t["nachbau_ok"] is not None]
    vb["nachbau_anzahl"] = len(nach)
    vb["nachbau_ok"] = bool(nach and all(nach))
    dp = {a["name"]: a.get("qt3") for q, a in alle if q == "kontrolle" and a["name"].startswith("DP")}
    soll = {"DP A+": {"Gamma": "plus_I", "P": "minus_I", "H": "minus_I", "P'": "plus_I"},
            "DP A-": {"Gamma": "plus_I", "P": "plus_I", "H": "minus_I", "P'": "minus_I"}}
    dp_ok = bool(len(dp) == 2 and all(dp[n][p][soll[n][p]] <= 1e-12 for n in soll for p in soll[n]))
    vb["dp_qt3_ok"] = dp_ok
    numerik_ok = bool(vb["alle_haupt"] and vb["unitaer_ok"] and vb["jacobi_ok"] and vb["nachbau_ok"] and dp_ok)
    vb["numerik_ok"] = numerik_ok
    # WI0
    byname = {t["name"]: t for t in tab}
    s1 = byname.get("K-S1 Grad-1 (m=2)")
    dpw = [byname.get("DP A+"), byname.get("DP A-")]
    inv = [t for t in tab if t["inversion"]]
    inv_rueck = [t for t, (q, _) in zip(tab, alle) if t["inversion"] and q in ("rueck_repr", "rueck_treffer")]
    if not numerik_ok or s1 is None or None in dpw:
        wi0 = "nicht auswertbar"
    else:
        ok = abs(abs(s1["W3_fein"]) - 1) < TOL_W and all(abs(t["W3_fein"]) < TOL_W for t in dpw) and \
            all(abs(t["W3_fein"]) < TOL_W for t in inv)
        wi0 = "eingetroffen" if ok else "nicht eingetroffen"
    res["urteile"]["WI0"] = wi0
    res["vermerke"]["WI0"] = {"S1_W3": None if s1 is None else s1["W3_fein"],
                              "DP_W3": [None if t is None else t["W3_fein"] for t in dpw],
                              "inversion_anzahl": len(inv), "inversion_davon_rueck": len(inv_rueck),
                              "inversion_W3_max_abs": max((abs(t["W3_fein"]) for t in inv), default=None),
                              "inversion_namen": [t["name"] for t in inv]}
    # WI1
    def menge(quellen):
        return [t for t, (q, _) in zip(tab, alle) if q in quellen and not t["inversion"]]
    def wi1_von(M):
        if any(t["konvergiert"] and abs(t["W3_rund"]) >= 1 for t in M):
            return "eingetroffen"
        if M and all(t["konvergiert"] and t["W3_rund"] == 0 for t in M):
            return "nicht eingetroffen"
        return "nicht auswertbar"
    M_haupt = menge(("rueck_repr", "rueck_treffer")) if rp_ok else menge(("rueck_repr",))
    res["urteile"]["WI1"] = "nicht auswertbar" if wi0 != "eingetroffen" else wi1_von(M_haupt)
    res["vermerke"]["WI1"] = {
        "menge_haupt": len(M_haupt), "stufeB_mitgezaehlt": rp_ok,
        "nur_repr": wi1_von(menge(("rueck_repr",))), "nur_treffer": wi1_von(menge(("rueck_treffer",))),
        "mit_dirac_zusatz": wi1_von(M_haupt + menge(("dirac_repr",))),
        "W3_rund_haeufigkeit": {str(v): sum(1 for t in M_haupt if t["W3_rund"] == v) for v in sorted({t["W3_rund"] for t in M_haupt if t["W3_rund"] is not None})},
        "nicht_konvergiert": [t["name"] for t in M_haupt if not t["konvergiert"]]}
    # Zahl der Treffer ohne Inversion in Stufe B (Pruefung der Zahl 17 aus CHIRAL-L)
    kat = {}
    for t, (q, _) in zip(tab, alle):
        if q == "rueck_treffer":
            key = f"{t['kategorie']}|inv={t['inversion']}"
            kat[key] = kat.get(key, 0) + 1
    res["vermerke"]["stufeB_kategorien"] = kat
    # WI2
    def auswertbar(t):
        return bool((not t["trivial"]) and t["weyl_vollstaendig"] and t["weyl_global"] and t["pfad_unabhaengig"]
                    and t["konvergiert"] and t["netto_je_luecke"] is not None)
    E = [t for t in tab if auswertbar(t)]
    def wi2_von(M):
        if not M:
            return "nicht auswertbar"
        return "eingetroffen" if all(all(x == t["W3_rund"] for x in t["netto_je_luecke"]) for t in M) else "nicht eingetroffen"
    res["urteile"]["WI2"] = "nicht auswertbar" if not numerik_ok else wi2_von(E)
    res["vermerke"]["WI2"] = {
        "auswertbar": len(E), "gesamt": len(tab),
        "nur_projekt_rueck": wi2_von([t for t, (q, _) in zip(tab, alle) if q in ("rueck_repr", "rueck_treffer") and auswertbar(t)]),
        "abweichend": [t["name"] for t in E if not all(x == t["W3_rund"] for x in t["netto_je_luecke"])],
        "ausgeschlossen": {t["name"]: {"trivial": t["trivial"], "vollstaendig": t["weyl_vollstaendig"], "global": t["weyl_global"],
                                       "pfad": t["pfad_unabhaengig"], "konvergiert": t["konvergiert"]}
                           for t in tab if not auswertbar(t)},
        "summenregel_s_mal_W3": {t["name"]: [t["summe_chi"], t["s_mal_W3"]] for t in tab
                                 if t["weyl_vollstaendig"] and not t["trivial"]}}
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print("Urteile:", res["urteile"], "Reproduktion strikt:", rp_ok, flush=True)


if __name__ == "__main__":
    sys.exit(main())
