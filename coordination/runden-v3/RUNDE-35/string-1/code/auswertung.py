#!/usr/bin/env python3
"""STRING-1 (Runde 35): mechanische Auswertung nach PLAN.md (eingefroren). Nur auf der .69 ueber kleintest.sh.
Aufruf: auswertung.py <laufordner> <ausgabe.json> <L2_gross> <L2_klein> <L3_gross> <L3_klein> [villain_L2] [villain_L3]
Dateien im Laufordner: w_d{d}_L{L}_K{K}.npz/.json (Wurm), v_d{d}_L{L}_K{K}.npz/.json (Villain),
vf_d3_L{L}_K4.5.npz/.json (Villain mit Feld, S6), kette.json (d = 1), gauss.json (Referenz).
"""
import sys, os, json, hashlib
import numpy as np

FORMEN = {  # Basis je Ausgleichsform; Parameter in dieser Reihenfolge
    "string": (lambda r: np.stack([r, np.log(r), np.ones_like(r)], 1), ["inv_xi", "a", "c"]),
    "log": (lambda r: np.stack([np.log(r), np.ones_like(r)], 1), ["eta", "c"]),
    "coulomb": (lambda r: np.stack([-1.0 / r, np.ones_like(r)], 1), ["C", "c"]),
    "linear": (lambda r: np.stack([r, np.ones_like(r)], 1), ["sigma", "c"]),
}


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def jkf(xjk):
    """Jackknife-Fehler aus Weglass-Stichproben (Achse 0)."""
    B = xjk.shape[0]
    return np.sqrt((B - 1) / B * ((xjk - xjk.mean(axis=0)) ** 2).sum(axis=0))


def fenster(L):
    return np.arange(2, L // 4 + 1)


def wurm_daten(npz):
    axz = npz["axz"].astype(np.float64)
    Sb = axz / (npz["nvec"] * npz["w_ax"])
    S = Sb.sum(axis=0)
    Sjk = S[None, :] - Sb
    with np.errstate(divide="ignore", invalid="ignore"):
        G = S / S[0]
        Gjk = Sjk / Sjk[:, :1]
        F = -np.log(G)
        Fjk = -np.log(Gjk)
        y = -np.log(S)
        yjk = -np.log(Sjk)
    return dict(G=G, sG=jkf(Gjk), F=F, sF=jkf(Fjk), Fjk=Fjk, y=y, sy=jkf(yjk), yjk=yjk, zaehler=axz.sum(axis=0),
                Sjk_min=Sjk.min(axis=0), B=axz.shape[0])


def ausgleich(form, r, y, s, yjk=None):
    X = FORMEN[form][0](r.astype(np.float64))
    Wt = 1.0 / s
    beta = np.linalg.lstsq(X * Wt[:, None], y * Wt, rcond=None)[0]
    chi2 = float((((y - X @ beta) / s) ** 2).sum())
    k = X.shape[1]
    aus = {"param": dict(zip(FORMEN[form][1], beta.tolist())), "chi2": chi2, "aic": chi2 + 2 * k, "k": k, "n": len(r)}
    if yjk is not None:
        bj = np.array([np.linalg.lstsq(X * Wt[:, None], yy * Wt, rcond=None)[0] for yy in yjk])
        aus["fehler"] = dict(zip(FORMEN[form][1], jkf(bj).tolist()))
    return aus


def fall(lauf, d, L, K):
    p = os.path.join(lauf, "w_d%d_L%d_K%s" % (d, L, K))
    if not (os.path.exists(p + ".npz") and os.path.exists(p + ".json")):
        return None
    npz = np.load(p + ".npz")
    js = json.load(open(p + ".json"))
    w = wurm_daten(npz)
    r = fenster(L)
    ok = bool(np.all(np.isfinite(w["y"][r])) and np.all(w["Sjk_min"][r] > 0) and np.all(w["zaehler"][r] >= 1000))
    aus = {"d": d, "L": L, "K": K, "fenster": r.tolist(), "fenster_ok": ok, "B": int(w["B"]),
           "gauss_fehler": int(js["gauss_fehler_start"]) + int(js["gauss_fehler_bloecke"]),
           "versuche": js["versuche"], "anteil_geschlossen": js["anteil_geschlossen"], "bias_b": js["bias_b"],
           "chi": js["chi"], "pruefsummen_lauf": js["pruefsummen"],
           "r": list(range(L // 2 + 1)), "F_T": w["F"].tolist(), "F_T_fehler": w["sF"].tolist(),
           "G": w["G"].tolist(), "G_fehler": w["sG"].tolist(), "zaehler_achse": w["zaehler"].tolist()}
    if ok:
        # Ausgleich an y(r) = F/T(r) + const mit Fehlern ohne Normierungsrauschen; c danach auf F/T umgerechnet
        fits = {}
        for form in FORMEN:
            f = ausgleich(form, r, w["y"][r], w["sy"][r], w["yjk"][:, r])
            f["param"]["c"] -= w["y"][0]  # F/T = y - y(0)
            fits[form] = f
        aus["ausgleiche"] = fits
        aus["sy_fenster"] = w["sy"][r].tolist()
        R = L // 2
        F = w["F"]
        aus["Q_sat"] = float((F[R] - F[L // 4]) / (F[L // 4] - F[1]))
    return aus


def urteil_S(nr, f):
    if f is None or not f.get("fenster_ok"):
        return None, {}
    a = f["ausgleiche"]
    if nr == "S1":
        w = {"aic_string": a["string"]["aic"], "aic_log": a["log"]["aic"], "a": a["string"]["param"]["a"]}
        return (w["aic_string"] < w["aic_log"] and 0.25 <= w["a"] <= 0.75), w
    if nr == "S2":
        w = {"eta": a["log"]["param"]["eta"]}
        return (0.068 <= w["eta"] <= 0.092), w
    if nr == "S3":
        w = {"aic_string": a["string"]["aic"], "aic_coulomb": a["coulomb"]["aic"], "a": a["string"]["param"]["a"]}
        return (w["aic_string"] < w["aic_coulomb"] and 0.6 <= w["a"] <= 1.4), w
    if nr == "S4":
        w = {"Q_sat": f["Q_sat"], "aic_coulomb": a["coulomb"]["aic"], "aic_linear": a["linear"]["aic"],
             "aic_string": a["string"]["aic"], "C": a["coulomb"]["param"]["C"]}
        return (w["Q_sat"] < 0.2 and w["aic_coulomb"] < w["aic_linear"] and w["aic_coulomb"] < w["aic_string"]
                and 0.10 <= w["C"] <= 0.36), w
    raise ValueError(nr)


def vergleich_villain(lauf, d, L, K):
    pv = os.path.join(lauf, "v_d%d_L%d_K%s" % (d, L, K))
    pw = os.path.join(lauf, "w_d%d_L%d_K%s" % (d, L, K))
    if not (os.path.exists(pv + ".npz") and os.path.exists(pw + ".npz")):
        return None
    v = np.load(pv + ".npz")
    jv = json.load(open(pv + ".json"))
    Gb = v["Gb"]
    B = Gb.shape[0]
    Gv = Gb.mean(axis=0)
    sv = Gb.std(axis=0, ddof=1) / np.sqrt(B)
    w = wurm_daten(np.load(pw + ".npz"))
    r = np.arange(1, L // 4 + 1)
    z = (w["G"][r] - Gv[r]) / np.sqrt(w["sG"][r] ** 2 + sv[r] ** 2)
    return {"d": d, "L": L, "K": K, "r": r.tolist(), "G_wurm": w["G"][r].tolist(), "f_wurm": w["sG"][r].tolist(),
            "G_villain": Gv[r].tolist(), "f_villain": sv[r].tolist(), "z": z.tolist(), "max_betrag_z": float(np.abs(z).max()),
            "chi2_diag": float((z ** 2).sum()), "stimmt": bool(np.all(np.abs(z) <= 3.0)), "villain_bloecke": int(B),
            "villain_annahme": jv["annahme"], "villain_abschnitt": [jv["abschnitt_rel_fehler_max"], jv["abschnitt_schranke"]],
            "pruefsummen_villain": jv["pruefsummen"]}


def s5(lauf):
    p = os.path.join(lauf, "kette.json")
    if not os.path.exists(p):
        return None
    k = json.load(open(p))
    r = np.array(k["r"], dtype=float)
    Fm = np.array(k["F_T_mit"])
    Fo = np.array(k["F_T_ohne"])
    sel = (r >= 1) & (r <= 6)
    s1, c1 = np.polyfit(r[sel], Fm[sel], 1)
    P = float(Fm[r == 60][0])
    rc = (P - c1) / s1
    return {"steigung_ast": float(s1), "achsenabschnitt_ast": float(c1), "plateau_F_T_60": P,
            "plateau_aenderung_40_60": float(Fm[r == 60][0] - Fm[r == 40][0]), "r_c": float(rc),
            "r_c_mit_ohne_paare_linie": float(P / (0.5 * k["K"])), "ohne_max_abw": k["ohne_max_abw_von_K2_r"],
            "kontrolle_N600": k["kontrolle_max_abw_N600"], "kontrolle_nmax16": k["kontrolle_max_abw_nmax16"],
            "F_T_mit": Fm.tolist(), "F_T_ohne": Fo.tolist(), "K": k["K"], "muT": k["muT"]}


def s6(lauf, f3klein):
    import glob
    c = sorted(glob.glob(os.path.join(lauf, "wp_d3_L*_K4.5.json")))
    if not c or f3klein is None or not f3klein.get("fenster_ok"):
        return None
    jv = json.load(open(c[0]))
    L = jv["L"]
    if L != f3klein["L"]:
        return {"fehler": "Gittergroesse passt nicht"}
    w = wurm_daten(np.load(c[0][:-5] + ".npz"))
    Fh, sFh = w["F"], w["sF"]
    R = L // 2
    pr = np.arange(R - 3, R + 1)
    P = float(Fh[pr].mean())
    st = f3klein["ausgleiche"]["string"]["param"]
    ixi, a, cc = st["inv_xi"], st["a"], st["c"]
    xi = 1.0 / ixi
    f0 = lambda x: ixi * x + a * np.log(x) + cc
    xs = np.linspace(1.0, 40.0, 39001)
    vals = f0(xs)
    ueber = np.where(vals >= P)[0]
    rc = float(xs[ueber[0]]) if len(ueber) else float("nan")
    muT = jv["muT"]
    rc_pred = 2.0 * muT * xi
    chi1 = f3klein["chi"]
    P_pred = 2.0 * muT - 2.0 * np.log(chi1)
    sat = float(Fh[R] - Fh[R - 3])
    ok = bool(sat < 0.3 * ixi and 0.7 * rc_pred <= rc <= 1.3 * rc_pred and abs(P - P_pred) <= 0.3 * P_pred)
    return {"L": L, "muT": muT, "z": jv["z"], "gauss_fehler": int(jv["gauss_fehler_start"]) + int(jv["gauss_fehler_bloecke"]), "spruenge": jv["spruenge"], "F_T_feld": Fh.tolist(), "F_T_feld_fehler": sFh.tolist(),
            "plateau_P": P, "plateau_r": pr.tolist(), "anstieg_R-3_R": sat, "schwelle_anstieg": 0.3 * ixi,
            "xi": xi, "a": a, "c": cc, "r_c": rc, "r_c_pred": rc_pred, "chi1": chi1, "P_pred": float(P_pred),
            "urteil_ok": ok, "pruefsummen_lauf": jv["pruefsummen"]}


def gauss_ref(lauf):
    p = os.path.join(lauf, "gauss.json")
    if not os.path.exists(p):
        return None
    g = json.load(open(p))
    aus = []
    for c in g["faelle"]:
        L = c["L"]
        F = np.array(c["F_T"])
        r = fenster(L)
        s = np.ones(len(r))
        e = {"d": c["d"], "L": L, "K": c["K"]}
        for form in FORMEN:
            e[form] = ausgleich(form, r, F[r], s)["param"]
        e["Q_sat"] = float((F[L // 2] - F[L // 4]) / (F[L // 4] - F[1]))
        aus.append(e)
    return aus


def bild(erg, pfad):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:
        return str(e)
    fig, ax = plt.subplots(2, 3, figsize=(15, 8.5))
    ax = ax.ravel()
    k = erg.get("S5_daten")
    if k:
        r = np.arange(len(k["F_T_mit"]))
        ax[0].plot(r, k["F_T_ohne"], "k-", lw=1, label="ohne Paare: (K/2) r")
        ax[0].plot(r, k["F_T_mit"], "o", ms=3, label="mit Paaren (exakt)")
        ax[0].axhline(k["plateau_F_T_60"], color="gray", ls=":")
        ax[0].axvline(k["r_c"], color="r", ls="--", label="r_c = %.2f" % k["r_c"])
        ax[0].set_ylim(0, 16)
        ax[0].set_title("d = 1, J = 1, T = 0,5, mu = 3")
        ax[0].legend(fontsize=8)
    for i, (d, K) in enumerate([(2, 0.5), (2, 2.5), (3, 1.5), (3, 4.5)]):
        a = ax[i + 1]
        for key, mk in (("gross", "o"), ("klein", "s")):
            f = erg["faelle"].get("d%d_K%s_%s" % (d, K, key))
            if not f:
                continue
            r = np.array(f["r"][1:], dtype=float)
            F = np.array(f["F_T"][1:])
            sF = np.array(f["F_T_fehler"][1:])
            a.errorbar(r, F, sF, fmt=mk, ms=3, mfc="none" if key == "klein" else None, label="L = %d" % f["L"])
            if key == "gross" and f.get("ausgleiche"):
                rr = np.linspace(2, f["L"] // 4, 200)
                for form, col in (("string", "r"), ("log", "g"), ("coulomb", "b"), ("linear", "m")):
                    p = f["ausgleiche"][form]["param"]
                    X = FORMEN[form][0](rr)
                    a.plot(rr, X @ np.array(list(p.values())), color=col, lw=1,
                           label="%s (AIC %.1f)" % (form, f["ausgleiche"][form]["aic"]))
        a.set_title("d = %d, K = %s" % (d, K))
        a.set_xlabel("r")
        a.set_ylabel("F/T")
        a.legend(fontsize=7)
    s6d = erg.get("S6_daten")
    if s6d and "F_T_feld" in s6d:
        r = np.arange(len(s6d["F_T_feld"]))
        ax[5].errorbar(r[1:], s6d["F_T_feld"][1:], s6d["F_T_feld_fehler"][1:], fmt="o", ms=3, label="mit Paaren (Feld)")
        rr = np.linspace(1, r[-1], 200)
        ax[5].plot(rr, rr / s6d["xi"] + s6d["a"] * np.log(rr) + s6d["c"], "r-", lw=1, label="String (h = 0)")
        ax[5].axhline(s6d["plateau_P"], color="gray", ls=":")
        ax[5].axvline(s6d["r_c"], color="r", ls="--", label="r_c = %.2f" % s6d["r_c"])
        ax[5].set_ylim(0, 1.5 * s6d["plateau_P"])
        ax[5].set_title("d = 3, K = 4,5, mit Paarbildung (S6)")
        ax[5].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(pfad, dpi=110)
    return "ok"


def main():
    lauf, aus = sys.argv[1], sys.argv[2]
    L2g, L2k, L3g, L3k = (int(x) for x in sys.argv[3:7])
    LV2 = int(sys.argv[7]) if len(sys.argv) > 7 else L2k
    LV3 = int(sys.argv[8]) if len(sys.argv) > 8 else L3k
    erg = {"pruefsumme_auswertung": sha(os.path.abspath(__file__)), "faelle": {}, "urteile": {}}
    for d, K, Lg, Lk in [(2, 0.5, L2g, L2k), (2, 2.5, L2g, L2k), (3, 1.5, L3g, L3k), (3, 4.5, L3g, L3k)]:
        erg["faelle"]["d%d_K%s_gross" % (d, K)] = fall(lauf, d, Lg, K)
        erg["faelle"]["d%d_K%s_klein" % (d, K)] = fall(lauf, d, Lk, K)
    # S1 bis S4: Urteil auf dem groesseren L; anderes Urteil auf dem kleineren -> Vermerk "nicht konvergiert"
    for nr, d, K in [("S1", 2, 2.5), ("S2", 2, 0.5), ("S3", 3, 4.5), ("S4", 3, 1.5)]:
        ug, wg = urteil_S(nr, erg["faelle"]["d%d_K%s_gross" % (d, K)])
        uk, wk = urteil_S(nr, erg["faelle"]["d%d_K%s_klein" % (d, K)])
        if ug is None:
            e = {"urteil": "nicht auswertbar", "werte": {}}
        else:
            e = {"urteil": "eingetroffen" if ug else "nicht eingetroffen", "werte": wg}
            if uk is not None and uk != ug:
                e["vermerk"] = "nicht konvergiert (kleineres L: %s)" % ("eingetroffen" if uk else "nicht eingetroffen")
        e["werte_kleines_L"] = wk
        erg["urteile"][nr] = e
    # S0
    gf = [f["gauss_fehler"] for f in erg["faelle"].values() if f]
    k5 = s5(lauf)
    erg["S5_daten"] = k5
    v2 = vergleich_villain(lauf, 2, LV2, 2.5)
    v3 = vergleich_villain(lauf, 3, LV3, 1.5)
    erg["villain_vergleich"] = {"d2_K2.5": v2, "d3_K1.5": v3}
    extra = {}
    for d, L, K in [(2, LV2, 0.5), (3, LV3, 4.5)]:
        extra["d%d_K%s" % (d, K)] = vergleich_villain(lauf, d, L, K)
    erg["villain_vergleich_zusatz"] = extra
    teil_a = len(gf) == 8 and sum(gf) == 0
    teil_b = k5 is not None and k5["ohne_max_abw"] <= 1e-9 and k5["kontrolle_N600"] <= 1e-9 and k5["kontrolle_nmax16"] <= 1e-9
    teil_c = v2 is not None and v3 is not None and v2["stimmt"] and v3["stimmt"]
    if len(gf) < 8 or k5 is None or v2 is None or v3 is None:
        u0 = "nicht auswertbar"
    else:
        u0 = "eingetroffen" if (teil_a and teil_b and teil_c) else "nicht eingetroffen"
    erg["urteile"]["S0"] = {"urteil": u0, "werte": {
        "gauss_fehler_summe": int(sum(gf)), "wurm_laeufe": len(gf),
        "d1_ohne_max_abw": None if k5 is None else k5["ohne_max_abw"],
        "villain_d2_K2.5_max_z": None if v2 is None else v2["max_betrag_z"],
        "villain_d3_K1.5_max_z": None if v3 is None else v3["max_betrag_z"],
        "teil_gauss": teil_a, "teil_d1": teil_b, "teil_villain": teil_c}}
    # S5
    if k5 is None:
        erg["urteile"]["S5"] = {"urteil": "nicht auswertbar", "werte": {}}
    else:
        erg["urteile"]["S5"] = {"urteil": "eingetroffen" if 10 <= k5["r_c"] <= 13 else "nicht eingetroffen",
                                "werte": {"r_c": k5["r_c"], "plateau": k5["plateau_F_T_60"], "steigung": k5["steigung_ast"]}}
    # S6 (wahlweise) auf dem kleineren 3D-Gitter
    s6d = s6(lauf, erg["faelle"]["d3_K4.5_klein"])
    erg["S6_daten"] = s6d
    if s6d is None:
        erg["urteile"]["S6"] = {"urteil": "nicht auswertbar", "vermerk": "nicht gerechnet", "werte": {}}
    elif "fehler" in s6d:
        erg["urteile"]["S6"] = {"urteil": "nicht auswertbar", "vermerk": s6d["fehler"], "werte": {}}
    else:
        erg["urteile"]["S6"] = {"urteil": "eingetroffen" if s6d["urteil_ok"] else "nicht eingetroffen", "werte": {
            k: s6d[k] for k in ("r_c", "r_c_pred", "plateau_P", "P_pred", "anstieg_R-3_R", "schwelle_anstieg", "muT")}}
    erg["gauss_referenz"] = gauss_ref(lauf)
    erg["bild"] = bild(erg, aus[:-5] + "-F.png" if aus.endswith(".json") else aus + "-F.png")
    with open(aus, "w") as f:
        json.dump(erg, f, indent=1)
    print(json.dumps(erg["urteile"], indent=1))


if __name__ == "__main__":
    main()
