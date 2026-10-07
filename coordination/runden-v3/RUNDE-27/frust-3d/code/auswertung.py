#!/usr/bin/env python3
"""FRUST-3D (Runde 27): mechanische Auswertung nach PLAN.md (eingefroren vor den echten Laeufen).

Liest aus <ordner>: k1_G_<N>, k1_E_<N>, k4_G_<N>, k4_E_<N> (Kontrollen), g_<N>, g_ein_<NF>, e_<N>, e_aus_<N>, ek_<N>
(N = 12 und 20, NF = 20). Schreibt <aus.json>.

Aufruf: python auswertung.py <ordner> <aus.json>
"""
import json
import math
import os
import sys

NETZE = (12, 20)
NF = 20
GRENZE_F0 = 1e-8
STICH_GRENZE = 0.01
BIEGE_ANTEIL = 0.80
ARTEN = ("achse", "speiche", "ring")


def lade(ordner, name):
    p = os.path.join(ordner, name + ".json")
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def schwelle(r):
    rest = max(max(k["rest_F"], k["rest_tau"]) for k in r["knoten"])
    return max(1e-9, 100.0 * rest), rest


def mittel(v):
    return sum(v) / len(v)


def je_art(r):
    aus = {}
    for art in ARTEN:
        st = [s for s in r["staebe"] if s["art"] == art]
        if not st:
            continue
        ax = [s["F_i_axial"] for s in st]
        sti = [s["stich"] for s in st]
        e = r["energie_je_art"][art]
        aus[art] = {"anzahl": len(st), "axial": ax, "axial_mittel": mittel(ax), "axial_min": min(ax),
                    "axial_max": max(ax), "stich": sti, "stich_min": min(sti), "stich_max": max(sti),
                    "tau_ende_max": max(max(s["tau_i_betrag"], s["tau_j_betrag"]) for s in st),
                    "tau_i": [s["tau_i_betrag"] for s in st], "tau_j": [s["tau_j_betrag"] for s in st],
                    "M_innen_max": max(s["M_innen_max"] for s in st),
                    "querkraft_max": max(max(s["F_i_quer"], s["F_j_quer"]) for s in st),
                    "sehne": [s["a"] for s in st], "euler_verhaeltnis": [s["euler_verhaeltnis"] for s in st],
                    "einspann_abw_grad_max": max(max(s["einspann_abweichung_grad_i"],
                                                     s["einspann_abweichung_grad_j"]) for s in st),
                    "energie_dehnung": e["dehnung"], "energie_biegung_innen": e["biegung_innen"],
                    "energie_einspannung": e["einspannung"]}
    return aus


def biegeanteil(r):
    b = sum(r["energie_je_art"][a]["biegung_innen"] + r["energie_je_art"][a]["einspannung"] for a in ARTEN)
    return b / r["energie"] if r["energie"] > 0 else None


def zusammenfassung(r):
    s, rest = schwelle(r)
    fest_F = max(k["reaktion_F"] for k in r["knoten"])
    fest_T = max(k["reaktion_tau"] for k in r["knoten"])
    f = r["form"]
    return {"name": r["name"], "energie": r["energie"], "biegeanteil": biegeanteil(r), "schwelle": s,
            "gleichgewichtsrest_frei": rest, "reaktion_lager_F": fest_F, "reaktion_lager_tau": fest_T,
            "gradnorm": r["gradnorm"], "newton": r["newton_meldung"], "schritte": r["newton_schritte"],
            "stoesse": r.get("anzahl_stoesse"), "stabil": r.get("stabil"), "hesse_kleinste": r["hesse_kleinste"][:12],
            "achse": f["achse"], "ringradius": f["ringradius"], "ringhoehe_ab_A": f["ring_hoehe_ab_A"],
            "je_art": je_art(r), "sek": r["sek"]}


def gesamturteil(u12, u20):
    if u12 is None or u20 is None:
        return "nicht entscheidbar (Lauf fehlt oder nicht stabil)"
    if u12 and u20:
        return "eingetroffen"
    if not u12 and not u20:
        return "nicht eingetroffen"
    return "uneinheitlich (Gitter N = 12 gegen 20)"


def rel(a, b):
    return abs(a - b) / abs(b) if b != 0 else None


def main():
    ordner, pfad = sys.argv[1], sys.argv[2]
    aus = {"regeln": "PLAN.md (eingefroren)", "laeufe": {}}

    # F0
    f0 = {}
    ok0 = True
    for t in ("k1", "k4"):
        for lag in ("G", "E"):
            for N in NETZE:
                nm = f"{t}_{lag}_{N}"
                r = lade(ordner, nm)
                if r is None:
                    f0[nm] = None
                    ok0 = None if ok0 is not False else False
                    continue
                tm = max(max(s["tau_i_betrag"], s["tau_j_betrag"]) for s in r["staebe"])
                fm = max(max(s["F_i_betrag"], s["F_j_betrag"]) for s in r["staebe"])
                stm = max(s["stich"] for s in r["staebe"])
                ok = tm < GRENZE_F0 and fm < GRENZE_F0
                f0[nm] = {"tau_max": tm, "F_max": fm, "stich_max": stm, "energie": r["energie"],
                          "gradnorm": r["gradnorm"], "unter_1e-8": ok, "stabil": r.get("stabil"),
                          "hesse_kleinste": r["hesse_kleinste"][:4]}
                if ok0 is not None:
                    ok0 = ok0 and ok
    aus["F0"] = {"laeufe": f0, "urteil": ("nicht entscheidbar (Lauf fehlt)" if ok0 is None else
                                          ("eingetroffen" if ok0 else "nicht eingetroffen"))}

    # F1, F2, F3 je N
    je_n = {}
    for N in NETZE:
        d = {}
        g = lade(ordner, f"g_{N}")
        if g is not None:
            s, rest = schwelle(g)
            a = je_art(g)
            f1 = (all(x > s for x in a["achse"]["axial"]) and all(x < -s for x in a["speiche"]["axial"])
                  and all(x < -s for x in a["ring"]["axial"]))
            f2_arten = {}
            for art in ARTEN:
                gedr = all(x < -s for x in a[art]["axial"])
                f2_arten[art] = {"alle_gedrueckt": gedr, "stich_min": a[art]["stich_min"],
                                 "stich_max": a[art]["stich_max"],
                                 "streng_alle_geknickt": gedr and a[art]["stich_min"] > STICH_GRENZE,
                                 "schwach_ein_stab_geknickt": gedr and a[art]["stich_max"] > STICH_GRENZE}
            f2 = any(v["streng_alle_geknickt"] for v in f2_arten.values())
            f2_schwach = any(v["schwach_ein_stab_geknickt"] for v in f2_arten.values())
            h = g["form"]["achse"]
            ls = mittel(a["speiche"]["sehne"])
            lr = mittel(a["ring"]["sehne"])
            ta = a["achse"]["axial_mittel"]
            d["F1"] = {"erfuellt": f1, "schwelle": s,
                       "eigenspannung_gemessen": {"achse": 1.0, "speiche": a["speiche"]["axial_mittel"] / ta,
                                                  "ring": a["ring"]["axial_mittel"] / ta},
                       "eigenspannung_formel": {"achse": 1.0, "speiche": -2.0 * ls / (5.0 * h),
                                                "ring": 2.0 * lr / (5.0 * h * (1.0 - math.cos(math.radians(72.0))))}}
            d["F2"] = {"erfuellt": f2, "schwach_ein_stab": f2_schwach, "je_art": f2_arten}
            g_kand = [g]
            if N == NF:
                ge = lade(ordner, f"g_ein_{N}")
                if ge is not None:
                    g_kand.append(ge)
            E_G = min(x["energie"] for x in g_kand)
            e_kand = [x for x in (lade(ordner, f"e_{N}"), lade(ordner, f"e_aus_{N}")) if x is not None]
            e_stabil = [x for x in e_kand if x.get("stabil")]
            if e_stabil:
                ew = min(e_stabil, key=lambda x: x["energie"])
                ba = biegeanteil(ew)
                f3 = bool(ew["energie"] > E_G and ba > BIEGE_ANTEIL)
                d["F3"] = {"erfuellt": f3, "E_E": ew["energie"], "E_lauf": ew["name"], "E_G": E_G,
                           "G_laeufe": [x["name"] for x in g_kand], "biegeanteil_E": ba,
                           "verhaeltnis_E_E_zu_E_G": ew["energie"] / E_G,
                           "E_kandidaten": {x["name"]: {"energie": x["energie"], "stabil": x.get("stabil")}
                                            for x in e_kand}}
            else:
                d["F3"] = {"erfuellt": None, "grund": "kein stabiler E-Zustand"}
        je_n[str(N)] = d
    aus["je_N"] = je_n

    def u(key, feld="erfuellt"):
        v = [je_n[str(N)].get(key, {}).get(feld) if je_n[str(N)] else None for N in NETZE]
        return gesamturteil(v[0], v[1])

    aus["F1"] = {"urteil": u("F1")}
    aus["F2"] = {"urteil": u("F2"), "schwache_lesart_nur_berichtet": u("F2", "schwach_ein_stab")}
    aus["F3"] = {"urteil": u("F3")}

    # Laeufe zusammengefasst
    for nm in ([f"{t}_{lag}_{N}" for t in ("k1", "k4") for lag in ("G", "E") for N in NETZE]
               + [f"{p}_{N}" for p in ("g", "e", "e_aus", "ek") for N in NETZE] + [f"g_ein_{NF}"]):
        r = lade(ordner, nm)
        aus["laeufe"][nm] = zusammenfassung(r) if r is not None else None

    # Kontrollen
    k = {"gitter_12_gegen_20": {}}
    for p in ("g", "e", "e_aus", "ek"):
        a, b = lade(ordner, f"{p}_12"), lade(ordner, f"{p}_20")
        if a is None or b is None:
            continue
        ja, jb = je_art(a), je_art(b)
        k["gitter_12_gegen_20"][p] = {
            "energie_rel": rel(a["energie"], b["energie"]), "achse_rel": rel(a["form"]["achse"], b["form"]["achse"]),
            "axial_mittel_rel": {art: rel(ja[art]["axial_mittel"], jb[art]["axial_mittel"]) for art in ARTEN},
            "stich_max_rel": {art: rel(ja[art]["stich_max"], jb[art]["stich_max"]) for art in ARTEN
                              if jb[art]["stich_max"] > 1e-6}}
    g20, ge20 = lade(ordner, f"g_{NF}"), lade(ordner, f"g_ein_{NF}")
    if g20 is not None and ge20 is not None:
        k["knickrichtung_g_ein_gegen_g"] = {
            "energie_diff": ge20["energie"] - g20["energie"],
            "axial_diff_max": max(abs(x["F_i_axial"] - y["F_i_axial"]) for x, y in zip(ge20["staebe"], g20["staebe"]))}
    for N in NETZE:
        a, b = lade(ordner, f"e_{N}"), lade(ordner, f"e_aus_{N}")
        if a is not None and b is not None:
            k[f"ast_e_gegen_e_aus_{N}"] = {
                "energie_diff": b["energie"] - a["energie"],
                "axial_diff_max": max(abs(x["F_i_axial"] - y["F_i_axial"]) for x, y in zip(a["staebe"], b["staebe"]))}
    aus["kontrollen"] = k
    with open(pfad + ".tmp", "w") as fh:
        json.dump(aus, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    print(f"F0 {aus['F0']['urteil']}; F1 {aus['F1']['urteil']}; F2 {aus['F2']['urteil']} (schwach: "
          f"{aus['F2']['schwache_lesart_nur_berichtet']}); F3 {aus['F3']['urteil']}", flush=True)
    for N in NETZE:
        d = je_n[str(N)]
        if not d:
            continue
        print(f"N {N}: F1 {d['F1']['erfuellt']} {d['F1']['eigenspannung_gemessen']} formel "
              f"{d['F1']['eigenspannung_formel']}; F2 {d['F2']['erfuellt']} schwach {d['F2']['schwach_ein_stab']}; "
              f"F3 {d['F3']}", flush=True)


if __name__ == "__main__":
    main()
