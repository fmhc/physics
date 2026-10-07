#!/usr/bin/env python3
"""TETRA-KETTE (Runde 26): mechanische Auswertung nach PLAN.md (eingefroren vor den echten Laeufen).

Liest aus <ordner>: k0_10.json, k0_16.json (ohne Defekt), d_10.json, d_16.json (Defekt 10 Grad, M = 12),
d_10_m16.json (Randkontrolle, M = 16), g_20.json (Gegenprobe ein Tetraeder) und ref_tetra_stab_d_20.json
(TETRA-STAB, RUNDE-24/tetra-stab/lauf-69/d_20.json). Schreibt <aus.json>.

Aufruf: python auswertung.py <ordner> <aus.json>
"""
import json
import math
import os
import sys

import numpy as np

K_FIT = list(range(2, 9))          # Fitbereich k = 2 .. 8 (Karte)
MIN_FITPUNKTE = 5


def lade(ordner, name):
    with open(os.path.join(ordner, name + ".json")) as fh:
        return json.load(fh)


def schwelle(lauf):
    """Messschwelle s = max(1e-9, 100 x groesster Gleichgewichtsrest (Kraft oder Moment) der freien Verbinder)."""
    rest = max(max(v["F_summe"], v["tau_summe"]) for v in lauf["verbinder"] if not v["fest"])
    return max(1e-9, 100.0 * rest), rest


def fit_loglin(ks, ys):
    k = np.array(ks, float)
    y = np.log(np.array(ys, float))
    A = np.vstack([np.ones_like(k), k]).T
    coef = np.linalg.lstsq(A, y, rcond=None)[0]
    res = y - A @ coef
    sst = float(((y - y.mean()) ** 2).sum())
    r2 = 1.0 - float((res ** 2).sum()) / sst if sst > 0 else float("nan")
    b = float(coef[1])
    return {"k": ks, "steigung_ln": b, "R2": r2, "verhaeltnis": math.exp(-b),
            "abklinglaenge_tetraeder": (-1.0 / b) if b < 0 else None}


def fit_loglog(ks, ys):
    x = np.log(np.array(ks, float))
    y = np.log(np.array(ys, float))
    A = np.vstack([np.ones_like(x), x]).T
    coef = np.linalg.lstsq(A, y, rcond=None)[0]
    res = y - A @ coef
    sst = float(((y - y.mean()) ** 2).sum())
    return {"k": ks, "exponent_p": -float(coef[1]), "R2": 1.0 - float((res ** 2).sum()) / sst if sst > 0 else None}


def monoton_ab_null(T, s):
    """Anzahl Tetraeder ab k = 0 mit T_0 > T_1 > ... (streng), alle ueber der Messschwelle."""
    n = 0
    for k in range(len(T)):
        if T[k] <= s:
            break
        if k > 0 and not T[k] < T[k - 1]:
            break
        n = k + 1
    return n


def vorzeichenwechsel(lauf, s):
    """TKe3: je Familie (i, i+f), Staebe ausserhalb Tetraeder 0 (k_eindeutig >= 1), nach i geordnet, |A| > s."""
    aus = {}
    gesamt = 0
    for f in (1, 2, 3):
        folge = [(st["i"], st["F_i_axial"]) for st in lauf["staebe"] if st["familie"] == f and st["k_eindeutig"] >= 1]
        folge.sort()
        gemessen = [(i, a) for (i, a) in folge if abs(a) > s]
        wechsel = [[gemessen[n][0], gemessen[n + 1][0]] for n in range(len(gemessen) - 1)
                   if gemessen[n][1] * gemessen[n + 1][1] < 0]
        aus[f"familie_{f}"] = {"folge": folge, "anzahl_gemessen": len(gemessen), "wechsel_zwischen_i": wechsel}
        gesamt += len(wechsel)
    return aus, gesamt


def gesamturteil(u10, u16):
    if u10 and u16:
        return "eingetroffen"
    if not u10 and not u16:
        return "nicht eingetroffen"
    return "uneinheitlich (Gitter N = 10 gegen 16)"


def main():
    ordner, pfad = sys.argv[1], sys.argv[2]
    aus = {"regeln": "PLAN.md (eingefroren); Zuordnung eindeutig: Stab (i, j) -> Tetraeder k = max(0, j - 3)"}

    # TKe0
    t0 = {}
    ok0 = True
    for nm in ("k0_10", "k0_16"):
        r = lade(ordner, nm)
        tm = max(max(st["tau_i_betrag"], st["tau_j_betrag"]) for st in r["staebe"])
        fm = max(max(st["F_i_betrag"], st["F_j_betrag"]) for st in r["staebe"])
        t0[nm] = {"tau_max": tm, "F_max": fm, "gradnorm": r["gradnorm"], "unter_1e-8": tm < 1e-8 and fm < 1e-8}
        ok0 = ok0 and t0[nm]["unter_1e-8"]
    aus["TKe0"] = {"laeufe": t0, "urteil": "eingetroffen" if ok0 else "nicht eingetroffen"}

    # TKe1 bis TKe3 an d_10 und d_16
    je_n = {}
    for nm in ("d_10", "d_16"):
        r = lade(ordner, nm)
        s, rest = schwelle(r)
        T = [t["T_eind"] for t in r["tetraeder"]]
        F = [t["F_eind"] for t in r["tetraeder"]]
        Tm = [t["T_mitg"] for t in r["tetraeder"]]
        Te = [e["T_ecke"] for e in r["ecken"]]
        n_mon = monoton_ab_null(T, s)
        pkt = [k for k in K_FIT if T[k] > s]
        fit = fit_loglin(pkt, [T[k] for k in pkt]) if len(pkt) >= MIN_FITPUNKTE else None
        if fit is None:
            u2 = None
        else:
            u2 = bool(fit["R2"] > 0.95 and 2.0 <= fit["verhaeltnis"] <= 30.0)
        vz, n_wechsel = vorzeichenwechsel(r, s)
        pktF = [k for k in K_FIT if F[k] > s]
        pktm = [k for k in K_FIT if Tm[k] > s]
        dom = []
        for t in r["tetraeder"]:
            a = t["axial_eind"]
            j = int(np.argmax(np.abs(a)))
            dom.append({"k": t["k"], "stab": t["staebe_eind"][j], "axial": a[j]})
        je_n[nm] = {
            "schwelle": s, "gleichgewichtsrest_max": rest, "gradnorm": r["gradnorm"],
            "T_eind": T, "F_eind": F, "verhaeltnis_T_k_zu_k1": [T[k] / T[k + 1] for k in range(len(T) - 1)],
            "TKe1": {"monoton_ab_k0_anzahl_tetraeder": n_mon, "erfuellt": n_mon >= 6},
            "TKe2": {"fitpunkte": pkt, "fit": fit, "erfuellt": u2},
            "TKe3": {"familien": vz, "anzahl_wechsel": n_wechsel, "erfuellt": n_wechsel >= 1},
            "nebenbei_nicht_gewertet": {
                "fit_F_eind": fit_loglin(pktF, [F[k] for k in pktF]) if len(pktF) >= MIN_FITPUNKTE else None,
                "T_mitg": Tm, "monoton_T_mitg": monoton_ab_null(Tm, s),
                "fit_T_mitg": fit_loglin(pktm, [Tm[k] for k in pktm]) if len(pktm) >= MIN_FITPUNKTE else None,
                "T_ecke": Te,
                "loglog_T_eind_k2_8": fit_loglog(pkt, [T[k] for k in pkt]) if len(pkt) >= MIN_FITPUNKTE else None,
                "dominante_axialkraft_je_tetraeder": dom,
                "reaktion_fest": [v for v in r["verbinder"] if v["fest"]][0],
                "hesse_kleinste": r.get("hesse_kleinste")}}
    aus["je_N"] = je_n
    aus["TKe1"] = {"urteil": gesamturteil(je_n["d_10"]["TKe1"]["erfuellt"], je_n["d_16"]["TKe1"]["erfuellt"])}
    e10, e16 = je_n["d_10"]["TKe2"]["erfuellt"], je_n["d_16"]["TKe2"]["erfuellt"]
    if e10 is None or e16 is None:
        aus["TKe2"] = {"urteil": "nicht entscheidbar (weniger als 5 Fitpunkte ueber der Messschwelle)"}
    else:
        aus["TKe2"] = {"urteil": gesamturteil(e10, e16)}
    aus["TKe3"] = {"urteil": gesamturteil(je_n["d_10"]["TKe3"]["erfuellt"], je_n["d_16"]["TKe3"]["erfuellt"])}

    # Kontrollen
    d10, d16, m16 = lade(ordner, "d_10"), lade(ordner, "d_16"), lade(ordner, "d_10_m16")
    T10 = [t["T_eind"] for t in d10["tetraeder"]]
    T16 = [t["T_eind"] for t in d16["tetraeder"]]
    Tm16 = [t["T_eind"] for t in m16["tetraeder"]]
    kontrollen = {
        "gitter_N10_gegen_N16_T_eind_rel_max_k0_8": max(abs(T10[k] - T16[k]) / T16[k] for k in range(9)),
        "gitter_rel_je_k": [(T10[k] - T16[k]) / T16[k] for k in range(len(T16))],
        "rand_M12_gegen_M16_T_eind_rel_max_k0_8": max(abs(T10[k] - Tm16[k]) / Tm16[k] for k in range(9)),
        "rand_rel_je_k": [(T10[k] - Tm16[k]) / Tm16[k] for k in range(len(T10))],
        "T_eind_M16": Tm16,
        "gleichgewicht": {}}
    for nm in ("k0_10", "k0_16", "d_10", "d_16", "d_10_m16", "g_20"):
        r = lade(ordner, nm)
        frei = [v for v in r["verbinder"] if not v["fest"]]
        fest = [v for v in r["verbinder"] if v["fest"]][0]
        kontrollen["gleichgewicht"][nm] = {"F_rest_frei_max": max(v["F_summe"] for v in frei),
                                           "tau_rest_frei_max": max(v["tau_summe"] for v in frei),
                                           "reaktion_fest_F": fest["F_summe"], "reaktion_fest_tau": fest["tau_summe"],
                                           "gradnorm": r["gradnorm"], "newton": r["newton_meldung"],
                                           "geometrie": r["geometrie"], "sek": r["sek"]}
    g, ref = lade(ordner, "g_20"), lade(ordner, "ref_tetra_stab_d_20")
    vergleich = []
    dmax = 0.0
    for sg, sr in zip(g["staebe"], ref["staebe"]):
        d = {"stab": sr["stab"], "tau_i": [sg["tau_i_betrag"], sr["tau_j_betrag"]],
             "tau_j": [sg["tau_j_betrag"], sr["tau_k_betrag"]], "axial": [sg["F_i_axial"], sr["F_j_axial"]],
             "a": [sg["a"], sr["a"]]}
        dmax = max(dmax, abs(d["tau_i"][0] - d["tau_i"][1]), abs(d["tau_j"][0] - d["tau_j"][1]),
                   abs(d["axial"][0] - d["axial"][1]), abs(d["a"][0] - d["a"][1]))
        vergleich.append(d)
    kontrollen["gegenprobe_tetra_stab_d20"] = {"staebe": vergleich, "max_abs_abweichung": dmax,
                                               "reproduziert_auf_1e-6": dmax < 1e-6}
    aus["kontrollen"] = kontrollen
    with open(pfad + ".tmp", "w") as fh:
        json.dump(aus, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    print(f"TKe0 {aus['TKe0']['urteil']}; TKe1 {aus['TKe1']['urteil']}; TKe2 {aus['TKe2']['urteil']}; "
          f"TKe3 {aus['TKe3']['urteil']}", flush=True)
    for nm in ("d_10", "d_16"):
        f = je_n[nm]["TKe2"]["fit"]
        print(f"{nm}: n_mon {je_n[nm]['TKe1']['monoton_ab_k0_anzahl_tetraeder']}, fit R2 "
              f"{f['R2'] if f else None}, Verhaeltnis {f['verhaeltnis'] if f else None}, "
              f"Wechsel {je_n[nm]['TKe3']['anzahl_wechsel']}, Schwelle {je_n[nm]['schwelle']:.1e}", flush=True)
    print(f"Gitter {kontrollen['gitter_N10_gegen_N16_T_eind_rel_max_k0_8']:.2e}, Rand "
          f"{kontrollen['rand_M12_gegen_M16_T_eind_rel_max_k0_8']:.2e}, Gegenprobe {dmax:.2e}", flush=True)


if __name__ == "__main__":
    main()
