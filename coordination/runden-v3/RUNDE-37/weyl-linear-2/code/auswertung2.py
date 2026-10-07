#!/usr/bin/env python3
"""WEYL-LINEAR-2 (Runde 42, Code-Agent fuer claude-primary): Auswertung nach PLAN.md, vor jeder Sicht auf neue
lambda1-Werte eingefroren.

Daten:
  <alt>        Kopien der WL1-Laufdateien zweig-*.json (N = 2000, 8000, 32 000; je Netz die Richtungen x, y, z,
               k = 0,06; 0,12; 0,18; 0,24) und WL1-auswertung.json (nur fuer den Vergleich in WM0).
  <lauf>       neue WL2-Dateien zweig-*.json (je Netz eine Richtung; N = 32 000 mit k bis 0,36, N = 128 000 mit
               k bis 0,24, ein Netz kann auf zwei Dateien verteilt sein).
  <kontrolle>  repro-32000-s1-x-k006.json (altes Netz neu gerechnet).
Zeilen je (N, Saat, Richtung, k). Zeilen mit a_fest_ok != True fallen heraus (gezaehlt). Doppelte Zeilen: die erste
gelesene gilt (alt vor lauf), gezaehlt.

Fits je Einheit und Ast (plus: E > 0; minus: |E| des Asts E < 0), Achsenabschnitt 1, ungewichtet:
  A: v - 1 = l1 k + l2 k^2
  B: v - 1 = l1 k + l2 k^2 + l3 k^3 + l4 k^4
Fenster: W0 k <= 0,24 (Haupt), Wk k <= 0,18 (kleiner; nur A), Wg k <= 0,36 (groesser).
Eine Einheit geht in ein Fenster nur ein, wenn jede ihrer Richtungen alle Soll-k des Fensters hat.
Einheiten: "netz" = alle Richtungen eines Netzes in einem Fit (wie WL1); "richtung" = Netz x Richtung.
Gleichteil lambda_S = (l1+ + l1-)/2, Gegenteil lambda_A = (l1+ - l1-)/2.
Statistik je N, Fenster, Ansatz, Einheit: Mittel, SD, SE = SD/sqrt(n); Bootstrap ueber Netze (B = 4000; die
Einheiten eines Netzes bleiben zusammen).
Urteile WM0 bis WM2 nach Plan [F] und nach Kartenwortlaut (alle Lesarten: eingetroffen nur, wenn alle eintreffen;
nicht eingetroffen, wenn keine; sonst uneindeutig). Agenten-Vorhersagen G1, G2.
Aufruf (nur ueber kleintest.sh):  python auswertung2.py <alt> <lauf> <kontrolle> <aus.json> [bild.png] [nmax=<N>]
"""
import glob
import json
import math
import os
import sys

import numpy as np

FENSTER = {"W0": 0.24, "Wk": 0.18, "Wg": 0.36}
SOLL_K = {"W0": [0.06, 0.12, 0.18, 0.24], "Wk": [0.06, 0.12, 0.18], "Wg": [0.06, 0.12, 0.18, 0.24, 0.30, 0.36]}
ANSATZ = {"A": 2, "B": 4}
B_BOOT = 4000
B_EXPO = 2000
WM0_SOLL, WM0_TOL = 0.0010, 1e-4
WM2_MITTE, WM2_BREITE = -0.5, 0.15
EPS = 1e-9


def js(x):
    if isinstance(x, dict):
        return {str(k): js(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [js(v) for v in x]
    if isinstance(x, np.ndarray):
        return js(x.tolist())
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, np.floating):
        return js(float(x))
    if isinstance(x, np.bool_):
        return bool(x)
    if isinstance(x, float) and not math.isfinite(x):
        return None
    return x


def kschl(k):
    return round(float(k), 6)


# ------------------------------------------------------------------------------------------------ Daten
def lese(ordner, quelle, rows, zaehl):
    gesehen = {(r["N"], r["saat"], r["richtung"], r["kk"]) for r in rows}
    for f in sorted(glob.glob(os.path.join(ordner, "zweig-*.json"))):
        d = json.load(open(f))
        for s in d["saaten"]:
            for w in s["wellen"]:
                p, m = w["aeste"]["plus"], w["aeste"]["minus"]
                r = {"datei": os.path.basename(f), "quelle": quelle, "N": int(d["N"]), "saat": int(s["saat"]),
                     "richtung": w["richtung"], "k": float(w["k"]), "kk": kschl(w["k"]), "v_plus": p["v"],
                     "v_minus": m["v"], "g_plus": p["gewicht_fenster"], "g_minus": m["gewicht_fenster"],
                     "a_fest_ok": w.get("a_fest_ok"), "mu_max": w["mu_max"],
                     "euler": s["pruefung"].get("euler") if isinstance(s.get("pruefung"), dict) else None}
                key = (r["N"], r["saat"], r["richtung"], r["kk"])
                if r["a_fest_ok"] is not True:
                    zaehl["a_fest_nicht_ok"] += 1
                    continue
                if key in gesehen:
                    zaehl["doppelt"] += 1
                    continue
                gesehen.add(key)
                rows.append(r)


def fit(k, v, grad):
    k = np.asarray(k, float)
    y = np.asarray(v, float) - 1.0
    if np.unique(np.round(k, 6)).size < grad:
        return None
    X = np.stack([k ** p for p in range(1, grad + 1)], 1)
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ c
    return {"c": c.tolist(), "rms": float(math.sqrt(np.mean(r * r)))}


def einheiten(rows):
    """netz-Einheiten: (N, saat) -> Zeilen; richtung-Einheiten: (N, saat, richtung) -> Zeilen."""
    netz, richt = {}, {}
    for r in rows:
        netz.setdefault((r["N"], r["saat"]), []).append(r)
        richt.setdefault((r["N"], r["saat"], r["richtung"]), []).append(r)
    return {"netz": netz, "richtung": richt}


def fenster_ok(rs, fn):
    soll = {kschl(x) for x in SOLL_K[fn]}
    je_r = {}
    for r in rs:
        je_r.setdefault(r["richtung"], set()).add(r["kk"])
    return bool(je_r) and all(soll <= ks for ks in je_r.values())


def einheit_fit(rs, fn, an):
    sel = [r for r in rs if r["k"] <= FENSTER[fn] + EPS]
    if not fenster_ok(rs, fn):
        return None
    k = [r["k"] for r in sel]
    fp = fit(k, [r["v_plus"] for r in sel], ANSATZ[an])
    fm = fit(k, [r["v_minus"] for r in sel], ANSATZ[an])
    if fp is None or fm is None:
        return None
    cp, cm = fp["c"], fm["c"]
    out = {"punkte": len(sel), "richtungen": sorted({r["richtung"] for r in sel}),
           "l1_plus": cp[0], "l1_minus": cm[0], "lambda_S": 0.5 * (cp[0] + cm[0]), "lambda_A": 0.5 * (cp[0] - cm[0]),
           "l2_plus": cp[1], "l2_minus": cm[1], "l2_S": 0.5 * (cp[1] + cm[1]), "rms_plus": fp["rms"],
           "rms_minus": fm["rms"]}
    if an == "B":
        out.update({"l3_plus": cp[2], "l3_minus": cm[2], "l3_S": 0.5 * (cp[2] + cm[2]), "l4_plus": cp[3],
                    "l4_minus": cm[3], "l4_S": 0.5 * (cp[3] + cm[3])})
    return out


GROESSEN = ("l1_plus", "l1_minus", "lambda_S", "lambda_A", "l2_S", "l3_S", "l4_S")


def statistik(eintraege, rng):
    """eintraege: Liste (netz_schluessel, wertedict). Bootstrap ueber Netze; Einheiten eines Netzes bleiben zusammen."""
    out = {}
    netze = sorted({e[0] for e in eintraege})
    idx = {n: [i for i, e in enumerate(eintraege) if e[0] == n] for n in netze}
    draws = [rng.choice(len(netze), size=len(netze), replace=True) for _ in range(B_BOOT)] if len(netze) >= 2 else []
    for q in GROESSEN:
        if q not in eintraege[0][1]:
            continue
        x = np.array([e[1][q] for e in eintraege], float)
        st = {"n": int(x.size), "netze": len(netze), "mittel": float(x.mean()),
              "sd": float(x.std(ddof=1)) if x.size > 1 else None,
              "se": float(x.std(ddof=1) / math.sqrt(x.size)) if x.size > 1 else None}
        if draws:
            bm = np.array([x[np.concatenate([idx[netze[j]] for j in dr])].mean() for dr in draws])
            st["se_boot"] = float(bm.std(ddof=1))
            st["q2_5"], st["q97_5"] = float(np.percentile(bm, 2.5)), float(np.percentile(bm, 97.5))
        out[q] = st
    return out


def auswertung_N(rows):
    E = einheiten(rows)
    Ns = sorted({r["N"] for r in rows})
    res = {}
    for N in Ns:
        rN = {}
        for fi, fn in enumerate(FENSTER):
            for ai, an in enumerate(ANSATZ):
                if fn == "Wk" and an == "B":
                    continue
                for ui, ut in enumerate(("netz", "richtung")):
                    eintr = []
                    for key, rs in sorted(E[ut].items()):
                        if key[0] != N:
                            continue
                        f = einheit_fit(rs, fn, an)
                        if f is None:
                            continue
                        f["saat"] = key[1]
                        f["quelle"] = rs[0]["quelle"]
                        if ut == "richtung":
                            f["richtung"] = key[2]
                        eintr.append(((N, key[1]), f))
                    if not eintr:
                        continue
                    rng = np.random.default_rng([42, 5, N, fi, ai, ui])
                    rN[f"{fn}_{an}_{ut}"] = {"einheiten": [e[1] for e in eintr], "statistik": statistik(eintr, rng)}
        res[str(N)] = rN
    return res


def exponent(Ns, sds):
    x, y = np.log(np.asarray(Ns, float)), np.log(np.asarray(sds, float))
    sl, ic = np.polyfit(x, y, 1)
    return float(sl), float(math.exp(ic))


def wm2_exponenten(res, an, ut, q, rng):
    Ns = sorted(int(N) for N in res if f"W0_{an}_{ut}" in res[N]
                and res[N][f"W0_{an}_{ut}"]["statistik"][q]["netze"] >= 3)
    if len(Ns) < 2:
        return None
    sds = [res[str(N)][f"W0_{an}_{ut}"]["statistik"][q]["sd"] for N in Ns]
    p, C = exponent(Ns, sds)
    # Bootstrap: Netze je N mit Zuruecklegen (beschreibend)
    boot = []
    werte = {}
    for N in Ns:
        ein = res[str(N)][f"W0_{an}_{ut}"]["einheiten"]
        netze = sorted({e["saat"] for e in ein})
        werte[N] = (netze, {s: [e[q] for e in ein if e["saat"] == s] for s in netze})
    for _ in range(B_EXPO):
        bs = []
        for N in Ns:
            netze, w = werte[N]
            dr = rng.choice(len(netze), size=len(netze), replace=True)
            x = np.concatenate([w[netze[j]] for j in dr])
            bs.append(x.std(ddof=1) if x.size > 1 and x.std() > 0 else np.nan)
        if np.all(np.isfinite(bs)):
            boot.append(exponent(Ns, bs)[0])
    boot = np.array(boot)
    return {"N": Ns, "sd": sds, "p": p, "C": C, "im_bereich": bool(abs(p - WM2_MITTE) <= WM2_BREITE),
            "boot_q2_5": float(np.percentile(boot, 2.5)) if boot.size else None,
            "boot_q97_5": float(np.percentile(boot, 97.5)) if boot.size else None, "boot_n": int(boot.size)}


def lesarten_urteil(liste):
    if not liste:
        return "nicht auswertbar"
    if all(liste):
        return "eingetroffen"
    if not any(liste):
        return "nicht eingetroffen"
    return f"uneindeutig ({sum(liste)} von {len(liste)} Lesarten eingetroffen)"


def leck_koeffizienten():
    """Leck eines k^4- bzw. k^3-Glieds in l1 von Ansatz A und Rauschverstaerkung B gegen A (gleiche Punkte, je Richtung
    ein Punkt je k, gleiches Rauschen), aus den Designmatrizen."""
    out = {}
    for fn, ks in SOLL_K.items():
        k = np.asarray(ks, float)
        XA = np.stack([k, k * k], 1)
        cA4 = np.linalg.lstsq(XA, k ** 4, rcond=None)[0][0]
        cA3 = np.linalg.lstsq(XA, k ** 3, rcond=None)[0][0]
        vA = float(math.sqrt(np.linalg.inv(XA.T @ XA)[0, 0]))
        e = {"k": ks, "leck_l1_A_je_l4": float(cA4), "leck_l1_A_je_l3": float(cA3), "sd_l1_A_je_sigma_v": vA}
        if len(ks) >= 4:
            XB = np.stack([k ** p for p in range(1, 5)], 1)
            vB = float(math.sqrt(np.linalg.inv(XB.T @ XB)[0, 0]))
            e.update({"sd_l1_B_je_sigma_v": vB, "verstaerkung_B_zu_A": vB / vA})
        out[fn] = e
    return out


def kontrolle(alt, kontr):
    f = os.path.join(kontr, "repro-32000-s1-x-k006.json")
    g = os.path.join(alt, "zweig-32000-1.json")
    if not (os.path.exists(f) and os.path.exists(g)):
        return None
    neu = json.load(open(f))["saaten"][0]["wellen"][0]
    altw = [w for w in json.load(open(g))["saaten"][0]["wellen"] if w["richtung"] == "x" and kschl(w["k"]) == 0.06][0]
    d = {a: abs(neu["aeste"][a]["v"] - altw["aeste"][a]["v"]) for a in ("plus", "minus")}
    return {"abw_v_plus": d["plus"], "abw_v_minus": d["minus"], "bestanden": bool(max(d.values()) <= 1e-12)}


def main():
    alt, lauf, kontr, ziel = sys.argv[1:5]
    pos = [a for a in sys.argv[5:] if "=" not in a]
    opts = {a.split("=")[0]: a.split("=")[1] for a in sys.argv[5:] if "=" in a}
    zaehl = {"a_fest_nicht_ok": 0, "doppelt": 0}
    rows = []
    lese(alt, "alt", rows, zaehl)
    lese(lauf, "neu", rows, zaehl)
    res = auswertung_N(rows)
    Nneu = sorted({r["N"] for r in rows if r["quelle"] == "neu"})
    nmax = int(opts["nmax"]) if "nmax" in opts else (Nneu[-1] if Nneu else None)
    out = {"zeilen": len(rows), "zaehl": zaehl, "N": sorted(int(N) for N in res), "nmax": nmax,
           "gueltigkeit": {"g_min": float(min(min(r["g_plus"], r["g_minus"]) for r in rows)) if rows else None,
                           "mu_max": float(max(r["mu_max"] for r in rows)) if rows else None,
                           "euler_alle_0": bool(all(r["euler"] in (0, None) for r in rows))},
           "netze_je_N": {N: {"alt": sorted({r["saat"] for r in rows if r["N"] == int(N) and r["quelle"] == "alt"}),
                              "neu": sorted({r["saat"] for r in rows if r["N"] == int(N) and r["quelle"] == "neu"})}
                          for N in res},
           "leck": leck_koeffizienten(), "kontrolle_repro": kontrolle(alt, kontr), "je_N": res}
    urteile = {}
    # ---------------- WM0: alte Netze N = 32 000 (Saaten 1 bis 4, quelle alt), A, W0, netz-Einheiten
    wm0 = None
    if "32000" in res and "W0_A_netz" in res["32000"]:
        ein = [e for e in res["32000"]["W0_A_netz"]["einheiten"] if e["quelle"] == "alt"]
        if len(ein) >= 3:
            rng = np.random.default_rng([42, 6, 0])
            st = statistik([((32000, e["saat"]), e) for e in ein], rng)
            mS, mA = st["lambda_S"]["mittel"], st["lambda_A"]["mittel"]
            plan = bool(abs(mS - WM0_SOLL) <= WM0_TOL and abs(mA) < 2 * st["lambda_A"]["se_boot"])
            lesarten = [bool(abs(mS - WM0_SOLL) <= WM0_TOL and abs(mA) < 2 * s) for s in
                        (st["lambda_A"]["se_boot"], st["lambda_A"]["se"])]
            wl1 = None
            fw = os.path.join(alt, "auswertung.json")
            if os.path.exists(fw):
                w1 = json.load(open(fw))["N_neue_laeufe"]["je_N"]["32000"]["statistik"]
                wl1 = {"lambda_S_WL1": w1["lambda_S"]["mittel"], "lambda_A_WL1": w1["lambda_A"]["mittel"],
                       "abw_S": abs(mS - w1["lambda_S"]["mittel"]), "abw_A": abs(mA - w1["lambda_A"]["mittel"])}
            wm0 = {"saaten": [e["saat"] for e in ein], "lambda_S": st["lambda_S"], "lambda_A": st["lambda_A"],
                   "urteil_plan": "eingetroffen" if plan else "nicht eingetroffen",
                   "urteil_kartenwortlaut": lesarten_urteil(lesarten), "vergleich_WL1": wl1}
    urteile["WM0"] = wm0 or {"urteil_plan": "nicht auswertbar", "urteil_kartenwortlaut": "nicht auswertbar"}
    # ---------------- WM1: groesste N, B, W0, netz-Einheiten; |Mittel lambda_S| < 2 se_boot
    wm1 = {"urteil_plan": "nicht auswertbar", "urteil_kartenwortlaut": "nicht auswertbar", "N": nmax}
    if nmax is not None and str(nmax) in res and "W0_B_netz" in res[str(nmax)]:
        st = res[str(nmax)]["W0_B_netz"]["statistik"]["lambda_S"]
        if st["netze"] >= 3:
            plan = bool(abs(st["mittel"]) < 2 * st["se_boot"])
            les = []
            for ut in ("netz", "richtung"):
                s2 = res[str(nmax)].get(f"W0_B_{ut}", {}).get("statistik", {}).get("lambda_S")
                if s2:
                    les += [bool(abs(s2["mittel"]) < 2 * s2["se_boot"]), bool(abs(s2["mittel"]) < 2 * s2["se"])]
            stA = res[str(nmax)].get("W0_A_netz", {}).get("statistik", {}).get("lambda_S")
            wm1.update({"lambda_S_B": st, "verhaeltnis_B": abs(st["mittel"]) / st["se_boot"],
                        "lambda_S_A_beschreibend": stA,
                        "urteil_plan": "eingetroffen" if plan else "nicht eingetroffen",
                        "urteil_kartenwortlaut": lesarten_urteil(les)})
    urteile["WM1"] = wm1
    # ---------------- WM2: Exponent der Streuung je Einheit, W0
    rng = np.random.default_rng([42, 7])
    ex = {}
    for an in ANSATZ:
        for ut in ("netz", "richtung"):
            for q in ("l1_plus", "l1_minus", "lambda_S", "lambda_A"):
                e = wm2_exponenten(res, an, ut, q, rng)
                if e:
                    ex[f"{an}_{ut}_{q}"] = e
    out["exponenten"] = ex
    plan_keys = ["A_richtung_l1_plus", "A_richtung_l1_minus"]
    ok_plan = [ex[k]["im_bereich"] for k in plan_keys if k in ex]
    alle_N = all(ex[k]["N"] == [2000, 8000, 32000, 128000] for k in plan_keys if k in ex)
    les_keys = [f"{an}_{ut}_{q}" for an in ANSATZ for ut in ("netz", "richtung") for q in ("l1_plus", "l1_minus")]
    urteile["WM2"] = {"plan_schluessel": plan_keys, "alle_vier_N": alle_N,
                      "urteil_plan": ("eingetroffen" if all(ok_plan) else "nicht eingetroffen")
                      if (len(ok_plan) == 2 and alle_N) else "nicht auswertbar",
                      "kartenwortlaut_schluessel": les_keys,
                      "urteil_kartenwortlaut": lesarten_urteil([ex[k]["im_bereich"] for k in les_keys if k in ex])}
    # ---------------- Agenten-Vorhersagen
    g1 = {"urteil": "nicht auswertbar"}
    if "32000" in res and "Wg_A_netz" in res["32000"] and "W0_A_netz" in res["32000"]:
        wg = {e["saat"]: e["lambda_S"] for e in res["32000"]["Wg_A_netz"]["einheiten"]}
        w0 = {e["saat"]: e["lambda_S"] for e in res["32000"]["W0_A_netz"]["einheiten"]}
        gem = sorted(set(wg) & set(w0))
        if len(gem) >= 3:
            d = [{"lambda_S": wg[s] - w0[s]} for s in gem]
            st = statistik([((32000, s), x) for s, x in zip(gem, d)], np.random.default_rng([42, 8]))["lambda_S"]
            g1 = {"saaten": gem, "differenz_Wg_minus_W0": st,
                  "urteil": "eingetroffen" if st["mittel"] > 2 * st["se_boot"] else "nicht eingetroffen"}
    urteile["G1"] = g1
    g2 = {"urteil": "nicht auswertbar"}
    pool = {}
    for an in ANSATZ:
        m, w = [], []
        for N in res:
            s = res[N].get(f"W0_{an}_netz", {}).get("statistik", {}).get("lambda_S")
            if s and s.get("se_boot"):
                m.append(s["mittel"])
                w.append(1.0 / s["se_boot"] ** 2)
        if m:
            m, w = np.array(m), np.array(w)
            pool[an] = {"mittel": float((m * w).sum() / w.sum()), "se": float(1.0 / math.sqrt(w.sum())), "N_anzahl": len(m)}
    out["gepoolt_lambda_S_W0"] = pool
    if "A" in pool:
        g2 = {"gepoolt_A": pool["A"], "urteil": "eingetroffen" if pool["A"]["mittel"] > 2 * pool["A"]["se"]
              else "nicht eingetroffen"}
    urteile["G2"] = g2
    out["urteile"] = urteile
    tmp = ziel + ".tmp"
    with open(tmp, "w") as f:
        json.dump(js(out), f, indent=1)
    os.replace(tmp, ziel)
    if pos:
        bild(pos[0], out)
    print("geschrieben", ziel, flush=True)


def bild(pfad, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    res, ex = out["je_N"], out["exponenten"]
    fig, ax = plt.subplots(1, 3, figsize=(16, 5.2))
    # (a) Streuung gegen N
    a = ax[0]
    for key, col, mk, lab in (("A_richtung_l1_plus", "tab:red", "o", "A, Ast E > 0"),
                              ("A_richtung_l1_minus", "tab:blue", "s", "A, Ast E < 0"),
                              ("B_richtung_l1_plus", "tab:red", "^", "B, Ast E > 0"),
                              ("B_richtung_l1_minus", "tab:blue", "v", "B, Ast E < 0")):
        if key not in ex:
            continue
        e = ex[key]
        fill = "full" if key.startswith("A") else "none"
        a.plot(e["N"], e["sd"], mk, color=col, fillstyle=fill, ms=7, label=f"{lab}: p = {e['p']:.2f}")
        NN = np.array([min(e["N"]), max(e["N"])], float)
        a.plot(NN, e["C"] * NN ** e["p"], "-", color=col, lw=0.8, alpha=0.6)
    if "A_richtung_l1_plus" in ex:
        e = ex["A_richtung_l1_plus"]
        NN = np.array([min(e["N"]), max(e["N"])], float)
        a.plot(NN, e["sd"][0] * (NN / NN[0]) ** -0.5, ":", color="0.4", label="Steigung N^(-1/2)")
    a.set_xscale("log")
    a.set_yscale("log")
    a.set_xlabel("N (Punkte im Netz)")
    a.set_ylabel("Streuung von lambda1 (SD ueber Netz x Richtung)")
    a.set_title("(a) Streuung gegen N, Fenster k <= 0,24")
    a.legend(fontsize=7)
    # (b) Gleichteil je Netz gegen N, A und B
    b = ax[1]
    Ns = sorted(int(N) for N in res)
    for an, col, dx in (("A", "tab:green", 0.94), ("B", "tab:purple", 1.06)):
        for N in Ns:
            r = res[str(N)].get(f"W0_{an}_netz")
            if not r:
                continue
            ys = [e["lambda_S"] for e in r["einheiten"]]
            b.plot([N * dx] * len(ys), ys, ".", color=col, alpha=0.5, ms=5)
            st = r["statistik"]["lambda_S"]
            if st.get("se_boot"):
                b.errorbar([N * dx], [st["mittel"]], yerr=[2 * st["se_boot"]], fmt="o" if an == "A" else "s",
                           color=col, ms=6, capsize=3)
        b.plot([], [], "o" if an == "A" else "s", color=col, label=f"Ansatz {an}: Mittel +- 2 SE (Bootstrap)")
    b.axhline(0, color="0.3", lw=0.6)
    b.set_xscale("log")
    b.set_xlabel("N")
    b.set_ylabel("Gleichteil lambda_S je Netz")
    b.set_title("(b) Gleichteil je Netz, Fenster k <= 0,24")
    b.legend(fontsize=7)
    # (c) Fensterabhaengigkeit bei N = 32 000 (neue Netze mit k bis 0,36)
    c = ax[2]
    if "32000" in res:
        for an, col, mk in (("A", "tab:green", "o"), ("B", "tab:purple", "s")):
            xs, ys, es = [], [], []
            for fn in ("Wk", "W0", "Wg"):
                r = res["32000"].get(f"{fn}_{an}_netz")
                if not r:
                    continue
                ein = [e for e in r["einheiten"] if e["quelle"] == "neu"]
                if len(ein) < 2:
                    continue
                x = np.array([e["lambda_S"] for e in ein])
                xs.append(FENSTER[fn])
                ys.append(x.mean())
                es.append(2 * x.std(ddof=1) / math.sqrt(x.size))
            if xs:
                c.errorbar(xs, ys, yerr=es, fmt=mk + "-", color=col, capsize=3, label=f"Ansatz {an} (neue Netze, +- 2 SE)")
    c.axhline(0, color="0.3", lw=0.6)
    c.set_xlabel("obere Fenstergrenze k_max")
    c.set_ylabel("Mittel lambda_S")
    c.set_title("(c) N = 32 000: Gleichteil gegen Fenster")
    c.legend(fontsize=7)
    fig.suptitle("WEYL-LINEAR-2: Gleichteil und Streuung von lambda1 im Zufallsnetz (synthetische Rechnung)")
    fig.tight_layout()
    fig.savefig(pfad, dpi=110)


if __name__ == "__main__":
    main()
