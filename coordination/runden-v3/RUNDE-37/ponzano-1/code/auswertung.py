"""PONZANO-1 (Runde 37): mechanische Urteile nach PLAN.md Abschnitt 5 und Bilder.

Aufruf auf der .69 (kleintest.sh, Spur cpu): python code/auswertung.py lauf
Liest lauf/*.json und lauf/*.log, schreibt lauf/auswertung.json und lauf/bild-*.png.
Geschrieben nach dem Einfrieren von Plan und ponzano.py, vor dem Ansehen der Hauptlauf-Ergebnisse.
"""
import json
import math
import os
import re
import sys

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

D = sys.argv[1] if len(sys.argv) > 1 else "lauf"
SCHWELLE_MP = 1e-30
LAMBDA_PO1 = (5, 10, 20, 50, 100, 200)
PO3_FAELLE = [(k, lam) for lam in (50, 100, 200) for k in ("K1", "K2")]

# Darstellung (dataviz-Referenzpalette, helle Flaeche)
FARBE = {"s1": "#2a78d6", "s2": "#eb6834", "s3": "#1baf7a", "text": "#0b0b0b", "text2": "#52514e",
         "gitter": "#e4e3df", "flaeche": "#fcfcfb", "grau": "#9b9a95"}
plt.rcParams.update({
    "figure.facecolor": FARBE["flaeche"], "axes.facecolor": FARBE["flaeche"], "savefig.facecolor": FARBE["flaeche"],
    "axes.edgecolor": FARBE["grau"], "axes.labelcolor": FARBE["text"], "xtick.color": FARBE["text2"],
    "ytick.color": FARBE["text2"], "text.color": FARBE["text"], "axes.grid": True, "grid.color": FARBE["gitter"],
    "grid.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
    "legend.frameon": False, "lines.linewidth": 1.6,
})


def lade(name):
    pfad = os.path.join(D, name + ".json")
    if not os.path.exists(pfad):
        return None
    with open(pfad) as fh:
        return json.load(fh)


def rc(name):
    pfad = os.path.join(D, name + ".log")
    if not os.path.exists(pfad):
        return None
    m = re.findall(r"rc=(\d+)", open(pfad).read())
    return int(m[-1]) if m else None


def ols(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    A = np.vstack([x, np.ones_like(x)]).T
    (m, c), *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - (m * x + c)
    r2 = 1 - (res @ res) / ((y - y.mean()) @ (y - y.mean()))
    return float(m), float(c), float(r2)


urteile = {}
beschreibend = {}

# ------------------------------------------------------------------ PO0
po0 = lade("po0")
if po0 is None or rc("po0") != 0:
    urteile["PO0"] = {"urteil": "nicht auswertbar", "vermerk": "Lauf fehlt oder rc != 0", "werte": {}}
else:
    o = po0["orthogonalitaet"]
    o2 = po0["orthogonalitaet_mp_formA_lam10"]
    be = po0["biedenharn_elliott"]
    sy = po0["sympy"]
    teile = {
        "a_orthogonalitaet_exakt": o["fehler"] == 0 and o["paare"] > 0,
        "a2_orthogonalitaet_mp": o2["max_abw"] <= SCHWELLE_MP,
        "b_be_exakt": be["fehler_exakt"] == 0 and len(be["saetze"]) == 20,
        "b_be_mp": be["max_rel_abw_mp"] <= SCHWELLE_MP,
        "c_symmetrien": po0["symmetrien"]["fehler"] == 0,
        "d_sympy": sy["fehler"] == 0,
        "e_sonderwert": po0["sonderwert"]["fehler"] == 0,
        "f_mp_gegen_exakt": po0["mp_gegen_exakt_max_rel"] <= SCHWELLE_MP,
    }
    werte = {"teile_bestanden": teile, "ortho_paare": o["paare"], "ortho_fehler": o["fehler"],
             "ortho_mp_max_abw": o2["max_abw"], "be_saetze": len(be["saetze"]), "be_fehler_exakt": be["fehler_exakt"],
             "be_rechts_null": sum(1 for s in be["saetze"] if s["rechts_null"]),
             "be_max_rel_abw_mp": be["max_rel_abw_mp"], "symmetrie_fehler": po0["symmetrien"]["fehler"],
             "sympy_vergleiche": sy["alle_2j_bis_4"] + sy["zufall_bis_j12"] + sy["formen"],
             "sympy_nicht_null_klein": sy["nicht_null_verglichen"], "sympy_fehler": sy["fehler"],
             "sonderwert_fehler": po0["sonderwert"]["fehler"], "mp_gegen_exakt_max_rel": po0["mp_gegen_exakt_max_rel"]}
    urteile["PO0"] = {"urteil": "eingetroffen" if all(teile.values()) else "nicht eingetroffen", "werte": werte}

# ------------------------------------------------------------------ PO1
po1 = lade("po1")
if po1 is None or rc("po1") != 0:
    urteile["PO1"] = {"urteil": "nicht auswertbar", "vermerk": "Lauf fehlt oder rc != 0", "werte": {}}
else:
    werte = {}
    ok = True
    for name in ("A", "B"):
        fr = po1["formen"][name]
        es = [fr["lam"][str(l)]["e"] for l in LAMBDA_PO1]
        m, c, r2 = ols(np.log(LAMBDA_PO1), np.log(es))
        e100 = fr["lam"]["100"]["e"]
        werte[name] = {"e": dict(zip([str(l) for l in LAMBDA_PO1], es)), "steigung": m, "r2_loglog": r2,
                       "e100": e100, "steigung_im_band": -1.3 <= m <= -0.7, "e100_unter_0_02": e100 < 0.02}
        ok = ok and (-1.3 <= m <= -0.7) and e100 < 0.02
    werte["schlaefli_max_abw"] = po1["schlaefli_max_abw"]
    werte["volumen_cm_gegen_einbettung_max_rel"] = po1["volumen_cm_gegen_einbettung_max_rel"]
    urteile["PO1"] = {"urteil": "eingetroffen" if ok else "nicht eingetroffen", "werte": werte}
    # beschreibend: Nullstellen in der Spinfolge
    folge = po1["spinfolge_A_lam50_j6"]
    geo = [r for r in folge if r["V2"] > 0]
    xlo, xhi = geo[0]["j6"], geo[-1]["j6"]
    breite = xhi - xlo
    ilo, ihi = xlo + 0.1 * breite, xhi - 0.1 * breite
    innen = [r for r in geo if ilo <= r["j6"] <= ihi]

    def nullstellen(key):
        out = []
        for r0, r1 in zip(innen, innen[1:]):
            if r1["j6"] != r0["j6"] + 1:
                continue
            y0, y1 = r0[key], r1[key]
            if y0 == 0:
                out.append(float(r0["j6"]))
            elif y0 * y1 < 0:
                out.append(r0["j6"] + y0 / (y0 - y1))
        return out

    n6 = nullstellen("sechsj")
    npr = nullstellen("pr")
    treffer = [(a, b) for a in n6 for b in npr if math.floor(a) == math.floor(b)]
    beschreibend["PO1_nullstellen_formA_lam50"] = {
        "geometrischer_bereich_j6": [xlo, xhi], "innerer_bereich": [ilo, ihi],
        "nullstellen_6j": len(n6), "nullstellen_pr": len(npr), "im_selben_intervall": len(treffer),
        "max_lageabstand": max((abs(a - b) for a, b in treffer), default=None),
        "mittlerer_lageabstand": (sum(abs(a - b) for a, b in treffer) / len(treffer)) if treffer else None,
        "max_e_innen": max(abs(r["sechsj"] - r["pr"]) / r["amp"] for r in innen)}

# ------------------------------------------------------------------ PO2
po2 = lade("po2")
if po2 is None or rc("po2") != 0:
    urteile["PO2"] = {"urteil": "nicht auswertbar", "vermerk": "Lauf fehlt oder rc != 0", "werte": {}}
else:
    werte = {}
    for name in ("N", "N_rand"):
        rows = [r for r in po2[name]["werte"] if 20 <= r["lam"] <= 200]
        if any(r["ln_abs"] is None for r in rows):
            werte[name] = {"exakte_nullen": True}
            continue
        m, c, r2 = ols([r["lam"] for r in rows], [r["ln_abs"] for r in rows])
        werte[name] = {"steigung": m, "achsenabschnitt": c, "r2": r2, "punkte": len(rows),
                       "ln_abs_lam20": rows[0]["ln_abs"], "ln_abs_lam200": rows[-1]["ln_abs"],
                       "vorzeichen_folge_lam20_30": [r["vorzeichen"] for r in rows[:11]],
                       "V2_alle_negativ": all(r["V2"] < 0 for r in po2[name]["werte"])}
    wN = werte["N"]
    if wN.get("exakte_nullen"):
        urteil = "nicht auswertbar"
    else:
        urteil = "eingetroffen" if (wN["r2"] > 0.99 and wN["steigung"] < 0) else "nicht eingetroffen"
    urteile["PO2"] = {"urteil": urteil, "werte": werte, "vermerk": "geurteilt nur Form N; N_rand beschreibend"}

# ------------------------------------------------------------------ PO3
faelle = {}
fehlend = []
for k, lam in PO3_FAELLE:
    name = "po3-%s-%d" % (k, lam)
    d = lade(name)
    if d is None or rc(name) != 0:
        fehlend.append(name)
        continue
    faelle[name] = d
werte = {}
verfehlt = False
unauswertbar = list(fehlend)
for name, d in faelle.items():
    kontrolle = d["be_rel_abw"] <= SCHWELLE_MP
    innen = d["rel_abstand_schwerpunkt"] <= 0.10
    werte[name] = {"x_stern": d["x_stern"], "x_schwerpunkt": d["x_schwerpunkt"],
                   "rel_abstand": d["rel_abstand_schwerpunkt"], "innerhalb_10_prozent": innen,
                   "be_rel_abw": d["be_rel_abw"], "be_kontrolle_bestanden": kontrolle, "x_fold": d["x_fold"],
                   "zeilen": d["zeilen"], "rechenzeit_s": d["rechenzeit_s"]}
    if not kontrolle:
        unauswertbar.append(name)
    elif not innen:
        verfehlt = True
if verfehlt:
    urteil = "nicht eingetroffen"
elif unauswertbar:
    urteil = "nicht auswertbar"
else:
    urteil = "eingetroffen"
urteile["PO3"] = {"urteil": urteil, "werte": werte}
if unauswertbar:
    urteile["PO3"]["vermerk"] = "nicht auswertbar oder fehlend: " + ", ".join(unauswertbar)
besch3 = {}
for name, d in faelle.items():
    besch3[name] = {
        "x_stern": d["x_stern"], "x_fold": d["x_fold"], "x_schwerpunkt": d["x_schwerpunkt"],
        "profil_max_x": d["profil_max_x"], "summe": d["summe"], "rechts": d["rechts"],
        "betragssumme_durch_rechts": d["betragssumme_durch_rechts"],
        "pr_rechts": d["pr_rechts"], "pr_konvex": d["pr_konvex"], "pr_gefaltet": d["pr_gefaltet"],
        "fenster_halbbreite": d["fenster_halbbreite"], "fenster_x_stern": d["fenster_x_stern"],
        "fenster_x_fold": d["fenster_x_fold"],
        "fenster_x_stern_durch_pr_konvex": d["fenster_x_stern"] / d["pr_konvex"] if d["pr_konvex"] else None,
        "fenster_x_fold_durch_pr_gefaltet": d["fenster_x_fold"] / d["pr_gefaltet"] if d["pr_gefaltet"] else None,
        "fenster_summe_durch_rechts": (d["fenster_x_stern"] + d["fenster_x_fold"]) / d["rechts"],
        "pr_rechts_durch_rechts": d["pr_rechts"] / d["rechts"]}
beschreibend["PO3"] = besch3

with open(os.path.join(D, "auswertung.json"), "w") as fh:
    json.dump({"urteile": urteile, "beschreibend": beschreibend}, fh, indent=1)
print(json.dumps({k: v["urteil"] for k, v in urteile.items()}))

# ------------------------------------------------------------------ Bilder
if po1 is not None:
    folge = po1["spinfolge_A_lam50_j6"]
    fig, axs = plt.subplots(2, 1, figsize=(10, 7.2))
    for ax, (lo, hi) in zip(axs, [(None, None), (380, 430)]):
        sel = [r for r in folge if (lo is None or lo <= r["j6"] <= hi)]
        x = [r["j6"] for r in sel]
        ax.plot(x, [r["sechsj"] for r in sel], "o", ms=3.2 if lo is None else 5, color=FARBE["s1"],
                label="6j exakt", zorder=3)
        g = [r for r in sel if "pr" in r]
        xs_pr = [r["j6"] for r in g]
        ax.plot(xs_pr, [r["pr"] for r in g], "-", color=FARBE["s2"], lw=1.4 if lo is not None else 0.8,
                label="Ponzano-Regge (an ganzen j6, verbunden)")
        ax.plot(xs_pr, [r["amp"] for r in g], "-", color=FARBE["grau"], lw=1.0, label="+-1/sqrt(12 pi V)")
        ax.plot(xs_pr, [-r["amp"] for r in g], "-", color=FARBE["grau"], lw=1.0)
        verb = [r["j6"] for r in sel if r["V2"] <= 0]
        links = [v for v in verb if v < xs_pr[0]]
        rechts = [v for v in verb if v > xs_pr[-1]]
        for teil_v in (links, rechts):
            if teil_v:
                ax.axvspan(min(teil_v) - 0.5, max(teil_v) + 0.5, color=FARBE["gitter"], alpha=0.7, lw=0)
        ax.set_xlabel("j6 = Spin der Kante CD")
        ax.set_ylabel("Wert des 6j-Symbols")
        if lo is None:
            ax.set_title("Form A, lambda = 50: 6j gegen Ponzano-Regge ueber j6 (grau hinterlegt: kein echtes Tetraeder)",
                         fontsize=10, loc="left")
            ax.legend(loc="upper right", fontsize=9)
        else:
            ax.set_title("Ausschnitt j6 = %d bis %d" % (lo, hi), fontsize=10, loc="left")
    fig.tight_layout()
    fig.savefig(os.path.join(D, "bild-spinfolge.png"), dpi=130)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5.2))
    for name, farbe in (("A", FARBE["s1"]), ("B", FARBE["s2"])):
        fr = po1["formen"][name]
        lam = [r["lam"] for r in fr["dicht"]]
        ax.plot(lam, [r["e"] for r in fr["dicht"]], "-", color=farbe, lw=1.0, alpha=0.55)
        m = urteile["PO1"]["werte"][name]["steigung"]
        ax.plot(LAMBDA_PO1, [fr["lam"][str(l)]["e"] for l in LAMBDA_PO1], "o", ms=7, color=farbe,
                label="Form %s (Steigung %.2f)" % (name, m), zorder=3)
    lref = np.array([3, 200.0])
    e0 = po1["formen"]["A"]["lam"]["5"]["e"]
    ax.plot(lref, e0 * 5 / lref, "--", color=FARBE["text2"], lw=1.2, label="Steigung -1")
    ax.axhline(0.02, color=FARBE["grau"], lw=1.0, ls=":")
    ax.text(1.1, 0.021, "Schwelle 0,02 (bei lambda = 100)", color=FARBE["text2"], fontsize=9, va="bottom")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("lambda (Spins j = lambda b)")
    ax.set_ylabel("e = abs(6j - PR) / (1/sqrt(12 pi V))")
    ax.set_title("Abweichung von Ponzano-Regge; Linien: alle lambda 1..200, Punkte: die sechs geurteilten",
                 fontsize=10, loc="left")
    ax.legend(loc="lower left", fontsize=9)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "bild-fehler-loglog.png"), dpi=130)
    plt.close(fig)

if po2 is not None:
    fig, ax = plt.subplots(figsize=(8, 5.2))
    for name, farbe in (("N", FARBE["s1"]), ("N_rand", FARBE["s2"])):
        rows = [r for r in po2[name]["werte"] if r["ln_abs"] is not None]
        ax.plot([r["lam"] for r in rows], [r["ln_abs"] for r in rows], "o", ms=2.6, color=farbe,
                label="Form %s %s" % (name, tuple(po2[name]["b"])))
        w = urteile["PO2"]["werte"].get(name, {})
        if "steigung" in w:
            xx = np.array([20, 200.0])
            ax.plot(xx, w["steigung"] * xx + w["achsenabschnitt"], "-", color=FARBE["text2"], lw=1.0)
            ax.text(202, w["steigung"] * 200 + w["achsenabschnitt"], "R^2 = %.5f" % w["r2"], fontsize=9,
                    color=FARBE["text2"], va="center")
    ax.axvline(20, color=FARBE["grau"], lw=1.0, ls=":")
    ax.set_xlabel("lambda (Spins j = lambda b)")
    ax.set_ylabel("ln abs(6j)")
    ax.set_title("Nicht geometrische Spins: exponentieller Abfall (Gerade: Ausgleich ueber lambda = 20..200)",
                 fontsize=10, loc="left")
    ax.legend(loc="lower left", fontsize=9)
    ax.set_xlim(0, 235)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "bild-abfall.png"), dpi=130)
    plt.close(fig)

for k in ("K1", "K2"):
    d = faelle.get("po3-%s-100" % k)
    if d is None:
        continue
    rows = d["zeilen_daten"]
    x = np.array([r["x"] for r in rows], float)
    s = np.array([r["s"] for r in rows], float)
    fig, axs = plt.subplots(3, 1, figsize=(10, 8.6), sharex=True,
                            gridspec_kw={"height_ratios": [2.2, 1.2, 1.2]})
    ax = axs[0]
    ax.vlines(x, 0, s, color=FARBE["s1"], lw=0.6)
    hx = [r["x"] for r in rows if "huelle" in r]
    hy = [r["huelle"] for r in rows if "huelle" in r]
    ax.plot(hx, hy, "-", color=FARBE["grau"], lw=1.0, label="PR-Huelle (2x+1)/prod sqrt(12 pi V_i)")
    ax.plot(hx, [-v for v in hy], "-", color=FARBE["grau"], lw=1.0)
    for ax_ in axs:
        ax_.axvline(d["x_stern"], color=FARBE["s2"], lw=1.8)
        ax_.axvline(d["x_fold"], color=FARBE["s3"], lw=1.8, ls="--")
        ax_.axvline(d["x_schwerpunkt"], color=FARBE["text"], lw=1.2, ls=":")
    ax.plot([], [], color=FARBE["s2"], lw=1.8, label="x* (flacher Schluss) = %.1f" % d["x_stern"])
    ax.plot([], [], color=FARBE["s3"], lw=1.8, ls="--", label="x_fold (gefaltet) = %.1f" % d["x_fold"])
    ax.plot([], [], color=FARBE["text"], lw=1.2, ls=":", label="Schwerpunkt nach Betrag = %.1f" % d["x_schwerpunkt"])
    ax.set_ylabel("Summand s(x)")
    ax.set_title("%s, lambda = 100: Summand des 2-3-Zugs ueber die innere Kante x" % k, fontsize=10, loc="left")
    ax.legend(loc="upper right", fontsize=8.5)
    teil = np.cumsum(s) / d["rechts"]
    axs[1].plot(x, teil, "-", color=FARBE["s1"], lw=1.2)
    axs[1].axhline(1.0, color=FARBE["grau"], lw=1.0, ls=":")
    axs[1].set_ylabel("Teilsumme / Produkt")
    prof = np.array(d["profil"], float)
    axs[2].plot(x, prof / prof.max(), "-", color=FARBE["s1"], lw=1.4)
    axs[2].set_ylabel("geglaettet, normiert")
    axs[2].set_xlabel("x = Spin der inneren Kante DE")
    fig.tight_layout()
    fig.savefig(os.path.join(D, "bild-pachner-%s.png" % k), dpi=130)
    plt.close(fig)
print("bilder fertig")
