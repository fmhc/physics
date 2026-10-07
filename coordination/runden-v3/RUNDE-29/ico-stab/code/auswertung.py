#!/usr/bin/env python3
"""ICO-STAB (Runde 29): mechanische Auswertung nach PLAN.md (eingefroren vor den echten Laeufen).

Liest aus <ordner>: ctrl_<N> (Kontrolle IS0, Speichen-Ruhelaenge R_c), sym_<N> (Zentrum festgehalten,
Konkurrenzzustand), frei_<start>_<N> (Zentrum frei; start: null, ecke, kante, flaeche, zufall1, zufall2, zufall3),
N = 12 und 20; e_sym_12, e_frei_flaeche_12 (Einspannung, nur berichtet). Schreibt <aus.json>.

Aufruf: python auswertung.py <ordner> <aus.json>
"""
import json
import math
import os
import sys

NETZE = (12, 20)
STARTS = ("null", "ecke", "kante", "flaeche", "zufall1", "zufall2", "zufall3")
GRENZE_IS0 = 1e-8
GERADE = 0.01          # Stich < 1 % L: gerade
GEKNICKT = 0.05        # Stich > 5 % L: geknickt
IS2_ABSTAND = 0.005    # freies Minimum mindestens 0,5 % unter dem symmetrischen Zustand
IS2_U = (0.035, 0.075)
IS4_E = (5.2, 6.2)
P_E = math.pi ** 2
E_LAEUFE = ("e_sym_12", "e_frei_flaeche_12")


def lade(ordner, name):
    p = os.path.join(ordner, name + ".json")
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def schwelle(r):
    rest = max(max(k["rest_F"], k["rest_tau"]) for k in r["knoten"])
    return max(1e-9, 100.0 * rest), rest


def biegeanteil(r):
    b = sum(r["energie_je_art"][a]["biegung_innen"] + r["energie_je_art"][a]["einspannung"]
            for a in ("speiche", "kante"))
    return b / r["energie"] if r["energie"] > 0 else None


def zustand(r):
    s, rest = schwelle(r)
    sp = [x for x in r["staebe"] if x["art"] == "speiche"]
    ka = [x for x in r["staebe"] if x["art"] == "kante"]
    zl = r["zentrumslage"]
    cos_t = zl.get("cos_theta_speiche", [None] * 12)
    speichen = [{"ecke": x["j"], "axial": x["F_i_axial"], "axial_j": x["F_j_axial"], "stich": x["stich"],
                 "sehne": x["a"], "verkuerzung": x["verkuerzung"], "cos_theta": cos_t[n],
                 "euler_verhaeltnis": x["euler_verhaeltnis"], "M_innen_max": x["M_innen_max"],
                 "querkraft": max(x["F_i_quer"], x["F_j_quer"])} for n, x in enumerate(sp)]
    ka_ax = [x["F_i_axial"] for x in ka]
    h = r.get("hesse", {})
    z = {"name": r["name"], "N": r["N"], "lagerung": r["lagerung"], "zentrum_lagerung": r["zentrum_lagerung"],
         "start": r["start"], "energie": r["energie"], "biegeanteil": biegeanteil(r),
         "energie_je_art": r["energie_je_art"], "u": zl["u"],
         "winkel_naechste_ecke": zl.get("winkel_naechste_ecke"),
         "winkel_naechste_kantenmitte": zl.get("winkel_naechste_kantenmitte"),
         "winkel_naechste_flaechenmitte": zl.get("winkel_naechste_flaechenmitte"),
         "naechste_flaeche": zl.get("naechste_flaeche"), "winkel_zur_startrichtung": zl.get("winkel_zur_startrichtung"),
         "eckradius_min": min(zl["eckradius"]), "eckradius_max": max(zl["eckradius"]),
         "stabil": r.get("stabil"), "newton": r["newton_meldung"], "schritte": r["newton_schritte"],
         "stoesse": r.get("anzahl_stoesse"), "gradnorm": r["gradnorm"], "schwelle": s,
         "gleichgewichtsrest_frei": rest,
         "reaktion_lager_F_max": max(k["reaktion_F"] for k in r["knoten"] if k["q"] != 0),
         "reaktion_lager_tau_max": max(k["reaktion_tau"] for k in r["knoten"]),
         "haltekraft_zentrum": (r["knoten"][0]["reaktion_F"] if r["zentrum_lagerung"] == "fest" else None),
         "speichen": speichen,
         "n_gerade": sum(1 for x in speichen if x["stich"] < GERADE),
         "n_geknickt": sum(1 for x in speichen if x["stich"] > GEKNICKT),
         "speichen_alle_druck": all(x["axial"] < -s and x["axial_j"] < -s for x in speichen),
         "kanten_alle_zug": all(x["F_i_axial"] > s and x["F_j_axial"] > s for x in ka),
         "kanten_axial_min": min(ka_ax), "kanten_axial_max": max(ka_ax), "kanten_axial_mittel": sum(ka_ax) / len(ka_ax),
         "kanten_sehne_min": min(x["a"] for x in ka), "kanten_sehne_max": max(x["a"] for x in ka),
         "kanten_stich_max": max(x["stich"] for x in ka),
         "querkraft_enden_max": max(max(x["F_i_quer"], x["F_j_quer"]) for x in r["staebe"]),
         "hesse_voll_kleinste": h.get("hesse_kleinste", r.get("hesse_kleinste", []))[:16],
         "hesse_nahe_null_voll": h.get("nahe_null_voll"), "drehmoden_anzahl": h.get("drehmoden_anzahl"),
         "drehmoden_HQ_max": h.get("drehmoden_HQ_max"),
         "hesse_ohne_drehmoden_kleinste": h.get("ohne_drehmoden_kleinste", [])[:16],
         "hesse_ohne_drehmoden_negativ": h.get("ohne_drehmoden_anzahl_negativ"),
         "sek": r["sek"]}
    if "sattelprobe" in r:
        sp_ = r["sattelprobe"]
        z["sattelprobe"] = {"gradnorm_frei": sp_["gradnorm_frei"],
                            "ohne_drehmoden_kleinste": sp_["ohne_drehmoden_kleinste"][:10],
                            "anzahl_negativ": sp_["ohne_drehmoden_anzahl_negativ"],
                            "drehmoden_anzahl": sp_["drehmoden_anzahl"],
                            "zentrumsanteil_tiefste": sp_.get("tiefste_vektoren_zentrumsanteil")}
    return z


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

    # IS0
    is0 = {}
    ok0 = True
    for N in NETZE:
        r = lade(ordner, f"ctrl_{N}")
        if r is None:
            is0[f"ctrl_{N}"] = None
            ok0 = None if ok0 is not False else False
            continue
        tm = max(max(x["tau_i_betrag"], x["tau_j_betrag"]) for x in r["staebe"])
        fm = max(max(x["F_i_betrag"], x["F_j_betrag"]) for x in r["staebe"])
        ok = tm < GRENZE_IS0 and fm < GRENZE_IS0
        is0[f"ctrl_{N}"] = {"F_max": fm, "tau_max": tm, "stich_max": max(x["stich"] for x in r["staebe"]),
                            "energie": r["energie"], "u": r["zentrumslage"]["u"], "gradnorm": r["gradnorm"],
                            "unter_1e-8": ok, "stabil": r.get("stabil"), "newton": r["newton_meldung"]}
        if ok0 is not None:
            ok0 = ok0 and ok
    aus["IS0"] = {"laeufe": is0, "urteil": ("nicht entscheidbar (Lauf fehlt)" if ok0 is None else
                                            ("eingetroffen" if ok0 else "nicht eingetroffen"))}

    je_n = {}
    for N in NETZE:
        d = {}
        sym = lade(ordner, f"sym_{N}")
        frei = {st: lade(ordner, f"frei_{st}_{N}") for st in STARTS}
        endz = {st: zustand(r) for st, r in frei.items() if r is not None}
        kand = [z for z in endz.values() if z["stabil"]]
        zs = zustand(sym) if sym is not None else None
        d["symmetrisch"] = zs
        d["endzustaende"] = {st: {k: z[k] for k in ("energie", "u", "winkel_naechste_ecke",
                                                    "winkel_naechste_kantenmitte", "winkel_naechste_flaechenmitte",
                                                    "naechste_flaeche", "n_gerade", "n_geknickt", "stabil", "stoesse",
                                                    "newton", "schritte", "sek", "hesse_ohne_drehmoden_negativ")}
                             for st, z in endz.items()}
        if kand:
            zf = min(kand, key=lambda z: z["energie"])
            d["freies_minimum"] = zf
            d["freies_minimum_lauf"] = zf["name"]
            for st, z in endz.items():
                d["endzustaende"][st]["abstand_zum_minimum_rel"] = (z["energie"] - zf["energie"]) / zf["energie"]
        else:
            zf = None
            d["freies_minimum"] = None
        # IS1
        if zs is not None and zf is not None:
            d["IS1"] = {"erfuellt": bool(zs["speichen_alle_druck"] and zs["kanten_alle_zug"]
                                         and zf["speichen_alle_druck"] and zf["kanten_alle_zug"]),
                        "sym": {"speichen_alle_druck": zs["speichen_alle_druck"], "kanten_alle_zug": zs["kanten_alle_zug"]},
                        "frei": {"speichen_alle_druck": zf["speichen_alle_druck"],
                                 "kanten_alle_zug": zf["kanten_alle_zug"]}}
        else:
            d["IS1"] = {"erfuellt": None}
        # IS2, IS3, IS4
        if zs is not None and zf is not None:
            abst = (zs["energie"] - zf["energie"]) / zs["energie"]
            d["IS2"] = {"erfuellt": bool(abst >= IS2_ABSTAND and IS2_U[0] <= zf["u"] <= IS2_U[1]),
                        "E_sym": zs["energie"], "E_frei": zf["energie"], "abstand_rel": abst, "u": zf["u"]}
        else:
            d["IS2"] = {"erfuellt": None}
        if zf is not None:
            d["IS3"] = {"erfuellt": bool(zf["n_gerade"] >= 1 and zf["n_geknickt"] >= 6), "n_gerade": zf["n_gerade"],
                        "n_geknickt": zf["n_geknickt"]}
            d["IS4"] = {"erfuellt": bool(IS4_E[0] <= zf["energie"] <= IS4_E[1]), "E_frei": zf["energie"]}
        else:
            d["IS3"] = {"erfuellt": None}
            d["IS4"] = {"erfuellt": None}
        je_n[str(N)] = d
    aus["je_N"] = je_n

    def u(key):
        v = [je_n[str(N)][key]["erfuellt"] for N in NETZE]
        return gesamturteil(v[0], v[1])

    for key in ("IS1", "IS2", "IS3", "IS4"):
        aus[key] = {"urteil": u(key)}
    is2, is3 = aus["IS2"]["urteil"], aus["IS3"]["urteil"]
    if is2 == "eingetroffen" and is3 == "eingetroffen":
        aus["bedeutung_ausgeloest"] = "IS2 und IS3 eingetroffen: Konvexitaetsmechanismus allgemein [H]"
    elif is2 == "nicht eingetroffen":
        aus["bedeutung_ausgeloest"] = "IS2 nicht eingetroffen: beschreiben"
    else:
        aus["bedeutung_ausgeloest"] = "keine (IS2 " + is2 + ", IS3 " + is3 + ")"

    # Kontrollen
    k = {"gitter_12_gegen_20": {}}
    a, b = je_n["12"], je_n["20"]
    if a.get("freies_minimum") and b.get("freies_minimum"):
        k["gitter_12_gegen_20"]["E_frei_rel"] = rel(a["freies_minimum"]["energie"], b["freies_minimum"]["energie"])
        k["gitter_12_gegen_20"]["u_rel"] = rel(a["freies_minimum"]["u"], b["freies_minimum"]["u"])
    if a.get("symmetrisch") and b.get("symmetrisch"):
        k["gitter_12_gegen_20"]["E_sym_rel"] = rel(a["symmetrisch"]["energie"], b["symmetrisch"]["energie"])
        k["gitter_12_gegen_20"]["speiche_axial_sym_rel"] = rel(
            sum(x["axial"] for x in a["symmetrisch"]["speichen"]), sum(x["axial"] for x in b["symmetrisch"]["speichen"]))
    for N in NETZE:
        zs = je_n[str(N)].get("symmetrisch")
        if zs is not None:
            ax = [x["axial"] for x in zs["speichen"]]
            k[f"sym_{N}_speichen_gleich"] = {"axial_min": min(ax), "axial_max": max(ax),
                                             "stich_min": min(x["stich"] for x in zs["speichen"]),
                                             "stich_max": max(x["stich"] for x in zs["speichen"]),
                                             "haltekraft": zs["haltekraft_zentrum"]}
    aus["kontrollen"] = k

    for nm in ([f"ctrl_{N}" for N in NETZE] + [f"sym_{N}" for N in NETZE]
               + [f"frei_{st}_{N}" for N in NETZE for st in STARTS] + list(E_LAEUFE)):
        r = lade(ordner, nm)
        aus["laeufe"][nm] = zustand(r) if r is not None else None
    aus["einspannung_nur_berichtet"] = {nm: aus["laeufe"][nm] for nm in E_LAEUFE}

    with open(pfad + ".tmp", "w") as fh:
        json.dump(aus, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    print(f"IS0 {aus['IS0']['urteil']}; IS1 {aus['IS1']['urteil']}; IS2 {aus['IS2']['urteil']}; "
          f"IS3 {aus['IS3']['urteil']}; IS4 {aus['IS4']['urteil']}; Bedeutung: {aus['bedeutung_ausgeloest']}", flush=True)
    for N in NETZE:
        d = je_n[str(N)]
        print(f"N {N}: freies Minimum {d.get('freies_minimum_lauf')}; IS1 {d['IS1']}; IS2 {d['IS2']}; "
              f"IS3 {d['IS3']}; IS4 {d['IS4']}", flush=True)
        for st, z in d["endzustaende"].items():
            print(f"  {st}: E {z['energie']:.8f}, u {z['u']:.5f}, Winkel Ecke/Kante/Flaeche "
                  f"{z['winkel_naechste_ecke']}/{z['winkel_naechste_kantenmitte']}/{z['winkel_naechste_flaechenmitte']}, "
                  f"gerade {z['n_gerade']}, geknickt {z['n_geknickt']}, stabil {z['stabil']}, Stoesse {z['stoesse']}",
                  flush=True)


if __name__ == "__main__":
    main()
