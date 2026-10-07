#!/usr/bin/env python3
"""SCHWEBUNGSUHR-2 (Runde 23): Hilfsauswertung der Code-Agentin (Auftrag der Leitung claude-primary, 02.10.2026).
Vor dem ersten echten Lauf geschrieben und im eingefrorenen PLAN.md per sha256 gebunden.

Liest die Ausgaben von schwebung1d.py (Code der Vorkarte RUNDE-23/schwebungsuhr/code/, unveraendert; dessen
Funktionen idx, steigung und gleitend werden importiert, damit die Fits genau wie in der Vorkarte laufen) und bildet
die Kartengroessen, den Dichtebild-Pruefpunkt V2 und die Urteile T0 bis T3 nach PLAN.md.

Aufruf (Arbeitsordner = Ordner mit schwebung1d.py):
  python hilfs/auswertung2.py <aus.json> <lauf1.json> [<lauf2.json> ...]
Jeder Lauf braucht <lauf.json> und <lauf.json>.roh.npz.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402

import numpy as np  # noqa: E402

sys.path.insert(0, os.getcwd())
import schwebung1d as sw  # noqa: E402

GEWERTET = (8.0, 10.0, 12.0, 18.0, 22.0)
DX_HAUPT, DX_ZWEIT, D_ZWEIT = 0.1, 0.05, 12.0
# Freie Ladungen: Einzelballlaeufe K1 bis K4 der Vorkarte (gleiche Messformel, Q_innen); Delta omega_frei = delta_omega_diskret
Q_FREI = {0.1: (3.161949367447931, 2.758189341327949), 0.05: (3.1626225071815677, 2.7588548126336563)}
SCHWELLE_BILD = 0.1      # V2: lokales Dichtemaximum zaehlt als Ball, wenn |psi|^2 > 0,1
SCHWELLE_KLEIN = 0.01    # nur berichtet (Splitter)
D_MERGE = 1.5            # wie V1 der Vorkarte
TOL_VERFOLGUNG = 1.0     # p1(T), p2(T) muessen je hoechstens 1,0 von einem Bildmaximum > 0,1 liegen
T1_BEREICH = (-1.22, -0.61)
T2_GRENZE = -0.10


def gleich(a, b):
    return abs(a - b) < 1e-9


def dom_re(e):
    return abs(e["dominant"]["re"]) if e and e.get("dominant") else None


def bildmaxima(S, bx):
    h = float(bx[1] - bx[0])
    ii = np.nonzero((S[1:-1] > S[:-2]) & (S[1:-1] >= S[2:]) & (S[1:-1] > SCHWELLE_KLEIN))[0] + 1
    out = []
    for j in ii:
        lo = j
        while lo > 0 and S[lo - 1] < S[lo] and S[lo - 1] > 0.02 * S[j]:
            lo -= 1
        hi = j
        while hi < S.size - 1 and S[hi + 1] < S[hi] and S[hi + 1] > 0.02 * S[j]:
            hi += 1
        out.append({"x": float(bx[j]), "S": float(S[j]), "int_psi2": float(h * S[lo:hi + 1].sum())})
    out.sort(key=lambda m: -m["S"])
    return out


def lauf(pfad):
    with open(pfad) as fh:
        meta = json.load(fh)
    z = np.load(pfad + ".roh.npz", allow_pickle=False)
    roh = {k: z[k] for k in z.files if k != "meta_json"}
    a = meta["analyse"]
    t = roh["t"]
    T, dx, D = meta["T"], meta["dx"], meta["D"]
    dfrei = meta["delta_omega_diskret"]
    fa, fe = a["fenster_anfang"], a["fenster_ende"]
    w = a["frequenzen"]
    r = {"name": os.path.basename(pfad).replace(".json", ""), "D": D, "dx": dx, "T": T,
         "parameter_wie_karte": bool(gleich(meta["w2a"], 0.60) and gleich(meta["w2b"], 0.65)
                                     and gleich(meta["theta_durch_pi"], 0.0) and gleich(T, 3000.0)
                                     and gleich(meta["L"], 900.0)),
         "delta_frei": dfrei, "delta_nominal": meta["delta_omega_nominal"],
         "fenster_anfang": fa, "fenster_ende": fe}
    # Frequenzen (Fits der Vorkarte) und Delta omega(t) gleitend (Fenster 50, Schritt 5, wie in der Vorkarte)
    r["omega1_A"], r["omega2_A"] = w["anfang"]["omega1"], w["anfang"]["omega2"]
    r["omega1_E"], r["omega2_E"] = w["ende"]["omega1"], w["ende"]["omega2"]
    r["delta_A"], r["delta_E"] = w["anfang"]["delta"], w["ende"]["delta"]
    r["delta_drittel"] = [e["delta"] for e in w["drittel"]]
    r["r"] = (r["delta_E"] - dfrei) / dfrei
    r["r_A"] = (r["delta_A"] - dfrei) / dfrei
    ph1, ph2 = np.unwrap(roh["ph1"]), np.unwrap(roh["ph2"])
    tcs, o1g = sw.gleitend(t, ph1)
    _, o2g = sw.gleitend(t, ph2)
    dg = o2g - o1g
    r["gleit_tc_letzt"] = float(tcs[-1])
    r["delta_gleit_letzt"] = float(dg[-1])
    r["r_gleit"] = (float(dg[-1]) - dfrei) / dfrei
    r["r_gleit_min"], r["r_gleit_max"] = float((dg.min() - dfrei) / dfrei), float((dg.max() - dfrei) / dfrei)
    sch = 20  # alle 100 Zeiteinheiten (Schritt 5)
    r["gleit_reihe"] = {"tc": tcs[::sch].tolist(), "r": ((dg[::sch] - dfrei) / dfrei).tolist()}
    # Ladungen: Q(0) = erste Messung, Ende = Mittel ueber das Ende-Fenster (wie Vorkarte), frei = K-Laeufe
    q1, q2 = roh["Q1"], roh["Q2"]
    i0, i1 = sw.idx(fe[0], fe[1], t.size)
    r["Q1_0"], r["Q2_0"] = float(q1[0]), float(q2[0])
    r["Q1_A"], r["Q2_A"] = a["ladungen"]["anfang"]["Q1"], a["ladungen"]["anfang"]["Q2"]
    r["Q1_E"], r["Q2_E"] = a["ladungen"]["ende"]["Q1"], a["ladungen"]["ende"]["Q2"]
    r["dQ1"], r["dQ2"] = r["Q1_E"] - r["Q1_0"], r["Q2_E"] - r["Q2_0"]
    qf = Q_FREI.get(round(dx, 6))
    r["Q1_frei"], r["Q2_frei"] = (qf if qf else (None, None))
    r["Q1_E_minus_frei"] = r["Q1_E"] - qf[0] if qf else None
    r["Q2_E_minus_frei"] = r["Q2_E"] - qf[1] if qf else None
    r["Q1_halbe_spanne_ende"] = float(0.5 * (q1[i0:i1].max() - q1[i0:i1].min()))
    r["Q_innen_0"], r["Q_innen_T"] = float(roh["Q_innen"][0]), float(roh["Q_innen"][-1])
    # Abstaende und Geschwindigkeiten am Ende
    ab = a["abstaende"]
    r["d_0"] = float(roh["p2"][0] - roh["p1"][0])
    r["d_A"], r["d_E"] = ab["maxima_anfang"], ab["maxima_ende"]
    r["dX_A"], r["dX_E"] = ab["schwerpunkt_anfang"], ab["schwerpunkt_ende"]
    r["d_min"], r["d_max"] = ab["maxima_min"], ab["maxima_max"]
    v1 = sw.steigung(t, roh["p1"], fe[0], fe[1])
    v2 = sw.steigung(t, roh["p2"], fe[0], fe[1])
    r["v1_E"], r["v2_E"] = v1, v2
    # Zeitdehnung omega/gamma in den gemessenen Frequenzen (berichtet, nicht korrigiert)
    r["zeitdehnung_delta_rel"] = (-(r["omega2_E"] * 0.5 * v2 * v2) + r["omega1_E"] * 0.5 * v1 * v1) / dfrei
    r["p1_T"], r["p2_T"] = float(roh["p1"][-1]), float(roh["p2"][-1])
    r["rand_erreicht_t"] = ab["rand_erreicht_t"]
    # Schwebung am Mittelpunkt (Pencil der Vorkarte)
    r["schwebung_drittel"] = [dom_re(e) for e in a["schwebung_mitte"]]
    r["schwebung_gesamt"] = dom_re(a["schwebung_mitte_gesamt"])
    # V1 (Vorkarte): Median d ueber [T - 100, T] < 1,5
    r["V1_median_d_letzte100"] = ab["maxima_median_letzte100"]
    r["V1_verschmolzen"] = bool(ab["verschmolzen_bei_T"])
    r["V1_erstmals_t"] = ab["erstmals_verschmolzen_t"]
    # V2 (Dichtebild): Maxima > 0,1 im Bild; verschmolzen, wenn hoechstens eines oder die zwei groessten < 1,5 auseinander
    B, bt, bx = roh["bilder"], roh["bild_t"], roh["bild_x"]
    bilder = []
    for k in range(B.shape[0]):
        m = bildmaxima(B[k].astype(np.float64), bx)
        gross = [e for e in m if e["S"] > SCHWELLE_BILD]
        n = len(gross)
        abst = abs(gross[0]["x"] - gross[1]["x"]) if n >= 2 else None
        bilder.append({"t": float(bt[k]), "n_ueber_0_1": n, "n_ueber_0_01": len(m), "abstand_zwei_groesste": abst,
                       "verschmolzen": bool(n <= 1 or abst < D_MERGE), "maxima": m[:8]})
    letzt = bilder[-1]
    r["V2_bild_t"] = letzt["t"]
    r["V2_n_ueber_0_1"] = letzt["n_ueber_0_1"]
    r["V2_n_ueber_0_01"] = letzt["n_ueber_0_01"]
    r["V2_abstand"] = letzt["abstand_zwei_groesste"]
    r["V2_verschmolzen"] = letzt["verschmolzen"]
    erst = [b["t"] for b in bilder if b["verschmolzen"]]
    r["V2_erstes_bild_verschmolzen_t"] = erst[0] if erst else None
    r["verschmolzen"] = bool(r["V1_verschmolzen"] or r["V2_verschmolzen"])
    gx = [e["x"] for e in letzt["maxima"] if e["S"] > SCHWELLE_BILD]
    r["verfolgung_ok"] = bool(len(gx) >= 2 and min(abs(r["p1_T"] - x) for x in gx) <= TOL_VERFOLGUNG
                              and min(abs(r["p2_T"] - x) for x in gx) <= TOL_VERFOLGUNG)
    r["bilder"] = bilder
    return r


def kat(s):
    return s.split(" (")[0]


def urteile(haupt, rkey):
    u = {}
    ohne = [D for D in GEWERTET if D in haupt and not haupt[D]["verschmolzen"]]
    gest = [D for D in ohne if not haupt[D]["verfolgung_ok"]]
    if 8.0 in haupt:
        u["T3"] = "eingetroffen" if haupt[8.0]["verschmolzen"] else "nicht eingetroffen"
    else:
        u["T3"] = "offen (Lauf D = 8 fehlt)"
    anw = [D for D in ohne if D >= 10.0]
    if not anw:
        u["T0"] = "offen (kein D >= 10 ohne Verschmelzen)"
    elif any(D in gest for D in anw):
        u["T0"] = "offen (Verfolgung gestoert bei D = %s)" % [D for D in anw if D in gest]
    else:
        neg = [D for D in anw if not haupt[D]["dQ1"] > 0.0]
        u["T0"] = "eingetroffen" if not neg else "nicht eingetroffen (Q1 steigt nicht bei D = %s)" % neg
    if not ohne:
        u["T2"] = "offen (kein D ohne Verschmelzen)"
    elif gest:
        u["T2"] = "offen (Verfolgung gestoert bei D = %s)" % gest
    else:
        zus = [D for D in ohne if not haupt[D][rkey] > T2_GRENZE]
        u["T2"] = "eingetroffen" if not zus else "nicht eingetroffen (r <= -0,10 bei D = %s)" % zus
    pts = [(D, haupt[D][rkey]) for D in ohne]
    pos = [(D, v) for D, v in pts if v > 0.0]
    fit = None
    if len(pos) >= 2:
        Ds = np.array([p[0] for p in pos])
        lr = np.log(np.array([p[1] for p in pos]))
        b, c = np.polyfit(Ds, lr, 1)
        fit = {"punkte_D": Ds.tolist(), "punkte_r": [p[1] for p in pos], "steigung": float(b),
               "achsenabschnitt": float(c), "residuen_ln_r": (lr - (b * Ds + c)).tolist(),
               "nur_positive_punkte": len(pos) < len(pts)}
    if len(pts) < 2:
        u["T1"] = "offen (weniger als zwei D ohne Verschmelzen)"
    elif gest:
        u["T1"] = "offen (Verfolgung gestoert bei D = %s)" % gest
    elif len(pos) < len(pts):
        u["T1"] = "nicht eingetroffen (r <= 0 bei D = %s)" % [D for D, v in pts if not v > 0.0]
    else:
        mono = all(pts[i + 1][1] < pts[i][1] for i in range(len(pts) - 1))
        inb = T1_BEREICH[0] <= fit["steigung"] <= T1_BEREICH[1]
        if mono and inb:
            u["T1"] = "eingetroffen"
        else:
            u["T1"] = "nicht eingetroffen (%s%s)" % ("" if mono else "nicht monoton fallend; ",
                                                     "Steigung %.4f" % fit["steigung"])
    return u, fit


def main():
    aus = sys.argv[1]
    laeufe = [lauf(p) for p in sys.argv[2:]]
    haupt = {L["D"]: L for L in laeufe if gleich(L["dx"], DX_HAUPT) and any(gleich(L["D"], D) for D in GEWERTET)}
    haupt = {min(GEWERTET, key=lambda D: abs(D - k)): v for k, v in haupt.items()}
    zweit = [L for L in laeufe if gleich(L["dx"], DX_ZWEIT) and gleich(L["D"], D_ZWEIT)]
    erg = {"version": "auswertung2", "laeufe": laeufe,
           "alle_parameter_wie_karte": all(L["parameter_wie_karte"] for L in laeufe)}
    for rkey, nm in (("r", "haupt"), ("r_gleit", "zweitlesart_letztes_gleitfenster")):
        u, fit = urteile(haupt, rkey)
        block = {"urteile_dx_0_1": u, "fit_T1": fit}
        if zweit and D_ZWEIT in haupt:
            h2 = dict(haupt)
            h2[D_ZWEIT] = zweit[0]
            u2, fit2 = urteile(h2, rkey)
            block["urteile_mit_D12_dx_0_05"] = u2
            block["fit_T1_mit_D12_dx_0_05"] = fit2
            block["urteile"] = {k: (u[k] if kat(u[k]) == kat(u2[k]) else
                                    "offen (Gitter uneinig bei D = 12: dx 0,1 %s, dx 0,05 %s)" % (kat(u[k]), kat(u2[k])))
                                for k in u}
        else:
            block["urteile"] = u
            block["hinweis"] = "Zweitgitterlauf D = 12, dx 0,05 fehlt"
        erg[nm] = block
    sw.schreiben(erg, aus)
    for L in laeufe:
        print("%-6s D=%5.1f dx=%.2f V1=%d(med %.2f) V2=%d(n %d, abst %s) verfolgung=%d | Q1 %.5f->%.5f (dQ1 %+.2e) "
              "Q2 %.5f->%.5f (dQ2 %+.2e) | dA %.6f dE %.6f r %+.4e r_gleit %+.4e | schw %s | d %.2f/%.2f/%.2f dX %.2f/%.2f"
              % (L["name"], L["D"], L["dx"], L["V1_verschmolzen"], L["V1_median_d_letzte100"], L["V2_verschmolzen"],
                 L["V2_n_ueber_0_1"], L["V2_abstand"], L["verfolgung_ok"], L["Q1_0"], L["Q1_E"], L["dQ1"], L["Q2_0"],
                 L["Q2_E"], L["dQ2"], L["delta_A"], L["delta_E"], L["r"], L["r_gleit"], L["schwebung_gesamt"],
                 L["d_0"], L["d_A"], L["d_E"], L["dX_A"], L["dX_E"]), flush=True)
    for nm in ("haupt", "zweitlesart_letztes_gleitfenster"):
        print(nm, json.dumps(erg[nm]["urteile"], ensure_ascii=True), flush=True)
        f = erg[nm]["fit_T1"]
        if f:
            print("  fit T1: steigung %.4f, punkte %s" % (f["steigung"], list(zip(f["punkte_D"], f["punkte_r"]))))


if __name__ == "__main__":
    main()
