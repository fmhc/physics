#!/usr/bin/env python3
# QBALL-DREIPOL-3, Auswertung der Nachtraege nach Sicht (beschreibend, ohne Urteil, nicht eingefroren):
# Ordnungsparameter (Luecke zum Mischball, Paarabstand) gegen Q1, Abklingrate des Residuums im Fluss
# (weiche Mode), grobe Landau-Schaetzungen der Schwelle, Radien an der Schwelle. Aufruf: nachtrag_aw3.py <laufordner>
import sys, os, json, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1]


def lade(p):
    p = os.path.join(D, p)
    return json.load(open(p)) if os.path.exists(p) else None


def rate(verlauf):
    # Abklingrate von ln(Residuum) je Flussschritt, Fit ueber die zweite Haelfte des Verlaufs
    v = np.array([[r[0], r[2]] for r in verlauf if r[2] > 0], float)
    if len(v) < 6:
        return None
    m = v[:, 0] >= 0.5 * v[-1, 0]
    if m.sum() < 3:
        return None
    s = np.polyfit(v[m, 0], np.log(v[m, 1]), 1)[0]
    return float(-s)


out = {"je_dim": {}}
fig, axs = plt.subplots(2, 2, figsize=(13, 8.5))
for j, dim in enumerate((3, 2)):
    zeilen = []
    for name in ("bisekt%d.json" % dim, "nachtrag/N1_%dd.json" % dim):
        b = lade(name)
        if b is None:
            continue
        for s in b["schritte"]:
            if "beruehrend" not in s:
                continue
            x = s["beruehrend"]
            e = x["ende"]
            R = s["R_halb"]
            konv = x["status"] == "konvergiert"
            pa = max(e["paarabstand"]) / R
            gap = s["vorab"]["E_Misch"] - e["E"]
            art = "verschmolzen" if (konv and pa < 0.01) else ("entmischt" if (konv and gap > 0) else "offen")
            zeilen.append(dict(Q1=s["Q1"], quelle=name, art=art, it=x["it"], status=x["status"], gap=gap,
                               paar_R=pa, paar_min_R=min(e["paarabstand"]) / R, reinheit_min=min(e["reinheit"]),
                               rate=rate(x["verlauf"]), sektor_it=s["sektor"]["it"],
                               sektor_gleich=bool(abs(s["sektor"]["ende"]["E"] - e["E"]) < 1e-6 * abs(e["E"])),
                               om=s["ball"]["om"], R_halb=R, R_eq_ball=s["ball"]["radien"]["R_eq"],
                               R_eq_misch=s["misch"]["radien"]["R_eq"], R_eq_ende=x["radien"]["R_eq"],
                               R_vol_ball=s["ball"]["radien"]["R_vol"], R_vol_misch=s["misch"]["radien"]["R_vol"]))
    zeilen.sort(key=lambda z: z["Q1"])
    me = [z for z in zeilen if z["art"] == "verschmolzen"]
    en = [z for z in zeilen if z["art"] == "entmischt"]
    sch = {}
    if len(en) >= 2:
        a, b = en[0], en[1]
        sq = math.sqrt(a["gap"] / b["gap"])
        sch["Qc_luecke_landau"] = (a["Q1"] - sq * b["Q1"]) / (1.0 - sq)
        p2 = (a["paar_R"] / b["paar_R"]) ** 2
        sch["Qc_paar_landau"] = (a["Q1"] - p2 * b["Q1"]) / (1.0 - p2)
        sch["paare_landau"] = [a["Q1"], b["Q1"]]
    if len(me) >= 2 and me[-1]["rate"] and me[-2]["rate"]:
        a, b = me[-2], me[-1]
        sch["Qs_rate_linear"] = b["Q1"] + b["rate"] * (b["Q1"] - a["Q1"]) / (a["rate"] - b["rate"])
        sch["rate_punkte"] = [a["Q1"], b["Q1"]]
    if me and en:
        sch["klammer_entmischung"] = [me[-1]["Q1"], en[0]["Q1"]]
        lo, hi = me[-1], en[0]
        sch["R_eq_misch_klammer"] = [lo["R_eq_misch"], hi["R_eq_misch"]]
        sch["R_eq_ball_klammer"] = [lo["R_eq_ball"], hi["R_eq_ball"]]
        sch["R_norm_misch_klammer"] = [lo["R_eq_misch"] / lo["R_eq_ball"], hi["R_eq_misch"] / hi["R_eq_ball"]]
        sch["R_eq_tropfen_unterster"] = hi["R_eq_ende"]
        sch["R_norm_tropfen_unterster"] = hi["R_eq_ende"] / hi["R_eq_ball"]
        sch["om_klammer"] = [lo["om"], hi["om"]]
    out["je_dim"]["%dd" % dim] = dict(zeilen=zeilen, schaetzungen=sch)
    ax = axs[0, j]
    q = [z["Q1"] for z in zeilen]
    ax.plot(q, [max(z["gap"], 1e-12) for z in zeilen], "o-", label="E_Misch - E_Ende")
    ax.plot(q, [z["paar_R"] for z in zeilen], "s-", label="groesster Paarabstand / R")
    ax.set_yscale("log")
    ax.set_xlabel("Q1")
    ax.set_title("%dD, g4 = -0,1: Ordnungsparameter (Fluss vom beruehrenden Dreieck)" % dim, fontsize=9)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    ax = axs[1, j]
    ax.plot([z["Q1"] for z in zeilen if z["rate"]], [z["rate"] for z in zeilen if z["rate"]], "o-")
    for z in zeilen:
        if z["rate"]:
            ax.annotate(z["art"][:4], (z["Q1"], z["rate"]), fontsize=7)
    ax.set_yscale("log")
    ax.set_xlabel("Q1")
    ax.set_ylabel("Abklingrate ln(Residuum) je Schritt")
    ax.set_title("%dD: weiche Mode (kleine Rate = langsamer Fluss)" % dim, fontsize=9)
    ax.grid(alpha=0.3)
fig.suptitle("Nachtrag (beschreibend, nach Sicht): Uebergang Mischball -> Dreifarben-Tropfen", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(D, "nachtrag", "uebergang.png"), dpi=100)
with open(os.path.join(D, "nachtrag", "nachtrag_aw.json"), "w") as fh:
    json.dump(out, fh, indent=1)
for k, v in out["je_dim"].items():
    print(k, json.dumps(v["schaetzungen"]))
    for z in v["zeilen"]:
        print(k, {kk: (round(vv, 6) if isinstance(vv, float) else vv) for kk, vv in z.items()
                  if kk in ("Q1", "art", "it", "gap", "paar_R", "rate", "sektor_gleich", "om", "R_eq_ende",
                            "R_eq_misch", "R_eq_ball")})
