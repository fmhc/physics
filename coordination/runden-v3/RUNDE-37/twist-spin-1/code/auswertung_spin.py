#!/usr/bin/env python3
"""TWIST-SPIN-1: Urteile nach PLAN.md Abschnitt 4, mechanisch (Plan = Stufe K, Wortlaut = Stufe W, [Z] schwach = Stufe F).
Aufruf: python auswertung_spin.py <haupt.json> <rc des Hauptlaufs> <auswertung.json> [rauch]
(rauch: nur zum Codetest, kleinste Groessen)
"""
import sys
import json
import os

NA, EIN, NEIN, ENTF = "nicht auswertbar", "eingetroffen", "nicht eingetroffen", "entfaellt"
PS = ("P1", "P2", "P3")
GR = {"dia": ["diamant-2-T", "diamant-3-T"], "pyT": ["pyro-1-T", "pyro-2-T"], "pyD3": ["pyro-1-D3", "pyro-2-D3"],
      "kub": ["kubisch-3-O", "kubisch-4-O"]}
GR_RAUCH = {"dia": ["diamant-2-T"], "pyT": ["pyro-1-T"], "pyD3": ["pyro-1-D3"], "kub": ["kubisch-3-O"]}
TSS = ("TS0", "TS1", "TS2", "TS3")

# Schreibtisch-Erwartung PLAN.md 1.3 (K-Untergruppen), nur Abgleich, kein Urteil
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
A = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
A2 = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
C2X = ((1, 0, 0), (0, -1, 0), (0, 0, -1))
C2Y = ((-1, 0, 0), (0, 1, 0), (0, 0, -1))
C2Z = ((-1, 0, 0), (0, -1, 0), (0, 0, 1))
D3_111 = [E, A, A2, ((0, -1, 0), (-1, 0, 0), (0, 0, -1)), ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
          ((0, 0, -1), (0, -1, 0), (-1, 0, 0))]
D3_1MM = [E, ((0, 0, -1), (-1, 0, 0), (0, 1, 0)), ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
          ((0, 1, 0), (1, 0, 0), (0, 0, -1)), ((0, 0, 1), (0, -1, 0), (1, 0, 0)), ((-1, 0, 0), (0, 0, -1), (0, -1, 0))]
ERWARTUNG_K = {
    "dia": {"P1": [E, A, A2], "P2": [E, C2X, C2Y, C2Z], "P3": [E, C2X, C2Y, C2Z]},
    "pyT": {"P1": [E, C2Y], "P2": [E, C2Z], "P3": [E, C2Y]},
    "kub": {"P1": D3_111, "P2": D3_1MM, "P3": D3_1MM},
}


def mset(liste):
    return sorted(json.dumps([list(r) for r in m]) for m in liste)


def generisch(r):
    z = r["generik"]
    return z["ent_schnitt"] == 0 and z["unklar"] == 0 and z["ent_knoten"] == 0 and z["torus_zusammenfall"] == 0


def sauber(R):
    ok = all(e["schleife_fehlt"] == 0 and e["richtung_unklar"] == 0 for e in R["elemente"].values())
    return ok and all(r["matrix_identitaet"] for r in R["relationen"].values())


def alle(R, key):
    return all(e[key] for e in R["elemente"].values())


def frustfrei(r):
    return r["kaefige"]["minus"] == 0 and not r["kaefige"]["anders"]


def ts1(E_, netze, stufe):
    """stufe: 'K', 'W' oder 'F'. Rueckgabe Urteil, tragende Projektionen, Werte."""
    werte = {}
    tragend, auswertbar = [], []
    for P in PS:
        rs = [E_["faelle"][nz]["proj"][P] for nz in netze]
        g = all(generisch(r) and sauber(r) for r in rs)
        w = {"generisch_sauber": g}
        if stufe == "F":
            w["frustfrei"] = all(frustfrei(r) for r in rs)
            w["fluss_konsistent"] = all(r["fluss"]["inkonsistent"] == 0 and r["fluss"]["kein_korand"] == 0
                                        for r in rs)
            g = g and w["frustfrei"] and w["fluss_konsistent"]
        key = {"K": "stufe_K", "W": "stufe_W", "F": "stufe_F"}[stufe]
        w["traegt_je_groesse"] = [alle(r, key) for r in rs]
        w["elemente_tragend"] = [sorted(n for n, e in r["elemente"].items() if e[key]) for r in rs]
        werte[P] = w
        if g:
            auswertbar.append(P)
            if all(w["traegt_je_groesse"]):
                tragend.append(P)
    if not auswertbar:
        return {"urteil": NA, "vermerk": "keine auswertbare Projektion", "werte": werte}, []
    return {"urteil": EIN if tragend else NEIN, "projektionen_tragend": tragend, "auswertbar": auswertbar,
            "werte": werte}, tragend


def ts2(E_, netze, t1, tragend, art):
    if t1["urteil"] != EIN:
        return {"urteil": ENTF, "vermerk": "Bedingung TS1 nicht erfuellt"}
    werte = {}
    treffer = False
    na = False
    for P in tragend:
        rs = [E_["faelle"][nz]["proj"][P] for nz in netze]
        if art == "K":
            vz = [rel["K_paarerzeuger"] for r in rs for rel in r["relationen"].values()]
            werte[P] = vz
            if any(v is None or v == "falsch" for v in vz):
                na = True
            if -1 in vz:
                treffer = True
        elif art == "W":
            vz = []
            for r in rs:
                if r["psg"].get("relationen"):
                    vz += [rel["paarerzeuger"] for rel in r["psg"]["relationen"].values()]
                else:
                    vz += [rel["K_paarerzeuger"] for rel in r["relationen"].values()]
            werte[P] = vz
            if any(v is None or v == "falsch" for v in vz):
                na = True
            if -1 in vz:
                treffer = True
        else:
            inv = [r["psg"].get("invariante") for r in rs]
            werte[P] = {"invariante": inv, "holonomie": [r["psg"].get("holonomie_maske") for r in rs]}
            if any(v is None for v in inv) and not all(r["psg"].get("invariante_name") is None for r in rs):
                na = True
            if all(v == -1 for v in inv):
                treffer = True
    if treffer:
        return {"urteil": EIN, "werte": werte}
    if na:
        return {"urteil": NA, "vermerk": "Pruefvorzeichen nicht berechenbar", "werte": werte}
    return {"urteil": NEIN, "werte": werte}


def ts0(E_, netze_alle, stufe):
    werte = {}
    ok, na = True, False
    for nz in netze_alle:
        U = E_["faelle"][nz]["ungedreht"]
        if not sauber(U):
            na = True
        key = {"K": "stufe_K", "W": "stufe_W"}[stufe]
        a = alle(U, key) and alle(U, "stufe_F")
        rel_id = [r["K_identitaet"] for r in U["relationen"].values()]
        rel_pz = [r["K_paarerzeuger"] for r in U["relationen"].values()]
        psg = U["psg"]
        psg_w = [v for rel in psg.get("relationen", {}).values() for v in rel["werte"]]
        psg_pz = [rel["paarerzeuger"] for rel in psg.get("relationen", {}).values()]
        inv = psg.get("invariante")
        kf = U["kaefige"]
        w = {"stufe": a, "rel_identitaet": rel_id, "rel_paarerzeuger": rel_pz, "psg_werte": sorted(set(psg_w)),
             "psg_paarerzeuger": psg_pz, "invariante": inv, "kaefige": kf}
        werte[nz] = w
        good = (a and all(v is True for v in rel_id) and all(v == 1 for v in rel_pz) and psg.get("relationen")
                and set(psg_w) == {"1"} and all(v == 1 for v in psg_pz) and inv in (1, None)
                and kf["minus"] == 0)
        if stufe == "W":
            good = good and True
        ok = ok and bool(good)
    if na:
        return {"urteil": NA, "vermerk": "ungedreht nicht sauber", "werte": werte}
    return {"urteil": EIN if ok else NEIN, "werte": werte}


def urteile(E_, stufe):
    U = {}
    netze_alle = GR["dia"] + GR["pyT"] + GR["pyD3"] + GR["kub"]
    U["TS0"] = ts0(E_, netze_alle, "W" if stufe == "W" else "K")
    t1d, trd = ts1(E_, GR["dia"], stufe)
    U["TS1"] = t1d
    art2 = {"K": "K", "W": "W", "F": "F"}[stufe]
    U["TS2"] = ts2(E_, GR["dia"], t1d, trd, art2)
    t1p, trp = ts1(E_, GR["pyT"], stufe)
    t2p = ts2(E_, GR["pyT"], t1p, trp, art2)
    if NA in (t1d["urteil"], U["TS2"]["urteil"], t1p["urteil"], t2p["urteil"]):
        u3 = NA
    else:
        u3 = EIN if (t1p["urteil"], t2p["urteil"]) == (t1d["urteil"], U["TS2"]["urteil"]) else NEIN
    U["TS3"] = {"urteil": u3, "pyro_TS1": t1p, "pyro_TS2": t2p}
    return U


def abgleich(E_):
    out = {}
    for teil, netze in (("dia", GR["dia"]), ("pyT", GR["pyT"]), ("kub", GR["kub"])):
        for nz in netze:
            for P in PS:
                R = E_["faelle"][nz]["proj"][P]
                ist = mset([tuple(tuple(r) for r in e["matrix"]) for e in R["elemente"].values() if e["stufe_K_graph"]])
                soll = mset(ERWARTUNG_K[teil][P])
                out["%s/%s" % (nz, P)] = {"K_untergruppe_wie_plan": ist == soll, "ordnung_ist": len(ist),
                                          "ordnung_soll": len(soll),
                                          "stufe_K_voll": sorted(n for n, e in R["elemente"].items() if e["stufe_K"]),
                                          "fluss": {k: R["fluss"].get(k) for k in ("plus", "minus", "inkonsistent", "phase_minus",
                                                                                  "start_in_V", "E_T_ungerade", "auswertungen",
                                                                                  "gegenprobe_kante0")},
                                          "kaefige": R["kaefige"],
                                          "gegenprobe_F_max": max(e["F_gegenprobe_abweichungen"]
                                                                  for e in R["elemente"].values())}
    for nz in GR["kub"]:
        fp = E_["faelle"][nz]["proj"]["P1"].get("fig5_probe")
        out["%s/fig5" % nz] = fp
    return out


def main():
    pfad, rc, aus = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    if len(sys.argv) > 4 and sys.argv[4] == "rauch":
        GR.clear()
        GR.update(GR_RAUCH)
    if rc != 0 or not os.path.exists(pfad):
        U = {k: {t: {"urteil": NA, "vermerk": "Lauf fehlt oder rc=%d" % rc} for t in TSS}
             for k in ("Plan", "Wortlaut", "schwach")}
        out = {"haupturteil": "Plan", "urteile": U, "quelle": pfad, "rc": rc}
    else:
        E_ = json.load(open(pfad))
        U = {"Plan": urteile(E_, "K"), "Wortlaut": urteile(E_, "W"), "schwach [Z]": urteile(E_, "F")}
        kurz = {k: {t: U[k][t]["urteil"] for t in TSS} for k in U}
        out = {"haupturteil": "Plan", "kurz": kurz, "urteile": U, "abgleich": abgleich(E_), "quelle": pfad,
               "rc": rc, "laufzeit_s": E_.get("laufzeit_s"), "meta": E_.get("meta")}
        print(json.dumps(kurz, ensure_ascii=False))
    with open(aus + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    os.replace(aus + ".tmp", aus)


if __name__ == "__main__":
    main()
