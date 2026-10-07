#!/usr/bin/env python3
# DIM-BEUTEL-2 Auswertung (Wertung nach PLAN.md.eingefroren-20261002-110453, Abschnitt 4).
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_k] = "1"
import sys, json, glob
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AUS = sys.argv[1] if len(sys.argv) > 1 else "aus"
ZIEL = sys.argv[2] if len(sys.argv) > 2 else os.path.join(AUS, "auswertung")
os.makedirs(ZIEL, exist_ok=True)

P = {"sierpinski": 3.0 * np.sqrt(5.0), "vicsek": 5.0 * np.sqrt(15.0)}
DS = {"sierpinski": 2 * np.log(3) / np.log(5), "vicsek": 2 * np.log(5) / np.log(15)}
DH = {"sierpinski": np.log(3) / np.log(2), "vicsek": np.log(5) / np.log(3)}
GTOL = 1e-7

LAEUFE = {
    "F1": dict(frak="sierpinski", tag="sie10", haupt="haupt/stufen-sie10.jsonl", info="haupt/info-sie10.json",
               kontr="kontrolle/stufen-sie9v.jsonl", kinfo="kontrolle/info-sie9v.json"),
    "F2": dict(frak="vicsek", tag="vic8", haupt="haupt/stufen-vic8.jsonl", info="haupt/info-vic8.json",
               kontr="kontrolle/stufen-vic7v.jsonl", kinfo="kontrolle/info-vic7v.json"),
}


def lies(pfad):
    p = os.path.join(AUS, pfad)
    if not os.path.exists(p):
        return [], {}
    formen, stufen = [], {}
    with open(p) as fh:
        for z in fh:
            r = json.loads(z)
            if r.get("typ") == "stufe":
                stufen[int(r["k"])] = r
            elif r.get("typ") == "form":
                formen.append(r)
    return formen, stufen


def formen_zu(formen, st):
    return {f["form"]: f for f in formen if f["k"] == st["k"] and f["lauf"] == st["lauf"]}


def konv(f):
    return f["msg"] != "ZEITGRENZE" and f["gskal"] <= 100 * GTOL and f["ident"] <= 1e-6


def gueltig(st, Rself):
    gr = dict(konv=bool(st["beste_konv"]), beutel=st["b_chi_min"] < 0.1,
              rand=(st["b_rand_phi"] <= 1e-6 and st["b_rand_chi"] <= 1e-6),
              bereich=(8.0 <= st["b_Rbag"] <= Rself / 2.0))
    return all(gr.values()), gr


def bereich(ks, ok):
    best, cur = [], []
    for k in ks:
        if ok[k]:
            cur.append(k)
            if len(cur) > len(best):
                best = list(cur)
        else:
            cur = []
    return best


def p_per_liste(Ek, run, frak):
    out = []
    s = set(run)
    for k in run:
        if k + 12 in s:
            out.append((k, float(np.log(Ek[k + 12] / Ek[k]) / np.log(P[frak]))))
    return out


erg = {"plan": "PLAN.md.eingefroren-20261002-110453"}
# d_s Vicsek
dsj = {}
pds = os.path.join(AUS, "ds", "ds-vicsek.json")
if os.path.exists(pds):
    dsj = json.load(open(pds))
ds_info = {}
for g in (5, 7, 8):
    z = dsj.get(f"zaehlung_g{g}")
    if not z:
        continue
    n = z["n"]
    rows = [r for r in z["rows"] if r["N15"] >= 5 and r["N"] <= n / 25]
    v = [2 * r["ds_half"] for r in rows]
    ds_info[f"zaehlung_g{g}"] = dict(n=n, anzahl=len(v), ds_mittel=float(np.mean(v)) if v else None,
                                     ds_min=float(np.min(v)) if v else None, ds_max=float(np.max(v)) if v else None,
                                     kontrolle_dicht=z.get("kontrolle_dicht"))
for g in (6, 7, 8):
    w = dsj.get(f"irrfahrt_g{g}")
    if w:
        ds_info[f"irrfahrt_g{g}"] = dict(ds_fit=-2 * w["fit_slope_225_tmax"],
                                         ds_sekanten=[2 * r["ds_half"] for r in w["rows"]], masse=w["masse"])
ds_V = ds_info.get("zaehlung_g8", {}).get("ds_mittel")
erg["ds_vicsek"] = ds_info
erg["ds_V_gewertet"] = ds_V
if ds_V is not None and abs(ds_V - DS["vicsek"]) > 0.03:
    ps_V = ds_V / (ds_V + 1)
    erg["soll_vicsek_quelle"] = "gemessen (Abweichung > 0,03)"
else:
    ps_V = DS["vicsek"] / (DS["vicsek"] + 1)
    erg["soll_vicsek_quelle"] = "2 ln5/ln15"
SOLL = {"sierpinski": (DS["sierpinski"] / (DS["sierpinski"] + 1), DH["sierpinski"] / (DH["sierpinski"] + 1)),
        "vicsek": (ps_V, DH["vicsek"] / (DH["vicsek"] + 1))}
erg["soll"] = {k: dict(p_s=v[0], p_H=v[1], mitte=(v[0] + v[1]) / 2) for k, v in SOLL.items()}

daten = {}
for lauf, cfg in LAEUFE.items():
    frak = cfg["frak"]
    formen, stufen = lies(cfg["haupt"])
    if not stufen:
        erg[lauf] = "keine Daten"
        continue
    info = json.load(open(os.path.join(AUS, cfg["info"])))
    Rself = info["R_self"]
    ks = sorted(stufen)
    ok, grund = {}, {}
    for k in ks:
        ok[k], grund[k] = gueltig(stufen[k], Rself)
    run = bereich(ks, ok)
    Ek = {k: stufen[k]["b_E"] for k in ks}
    pp = p_per_liste(Ek, run, frak)
    vals = np.array([v for _, v in pp])
    perioden = (run[-1] - run[0]) / 12.0 if run else 0.0
    res = dict(frak=frak, R_self=Rself, stufen=ks, gueltig=[k for k in ks if ok[k]],
               ungueltig={k: [n for n, b in grund[k].items() if not b] for k in ks if not ok[k]},
               bereich=run, perioden=perioden,
               Q_bereich=[stufen[run[0]]["Q"], stufen[run[-1]]["Q"]] if run else None,
               Rbag_bereich=[stufen[run[0]]["b_Rbag"], stufen[run[-1]]["b_Rbag"]] if run else None,
               p_per=pp)
    if len(vals):
        res.update(p_mittel=float(vals.mean()), p_sd=float(vals.std(ddof=1)) if len(vals) > 1 else None,
                   p_min=float(vals.min()), p_max=float(vals.max()),
                   p_nichtueberlappend=[v for k, v in pp if (k - run[0]) % 12 == 0])
        pm = res["p_mittel"]
        res["d_aus_p"] = pm / (1 - pm)
    # Kontrollen
    dq = []
    for k in run:
        st = stufen[k]
        if "p_fd" in st:
            dq.append(dict(k=k, dp=abs(st["p_fd"] - st["b_p_loc"]), dEdQ_rel=st["dEdQ_rel"], pm_konv=st["pm_konv"],
                           V=[st["pm_Vbag"][0], st["b_Vbag"], st["pm_Vbag"][1]]))
    if dq:
        dpa = np.array([d["dp"] for d in dq])
        res["dEdQ"] = dict(median=float(np.median(dpa)), max=float(dpa.max()),
                           alle_pm_konv=all(d["pm_konv"] for d in dq),
                           V_wechsel=[d["k"] for d in dq if len(set(d["V"])) > 1],
                           bestanden=bool(dpa.max() <= 2e-3 and all(d["pm_konv"] for d in dq)), je_stufe=dq)
    # Startformen
    fs = {}
    for k in ks:
        fz = formen_zu(formen, stufen[k])
        fs[k] = fz
    gew = {}
    for k in run:
        b = stufen[k]["beste"]
        gew[b] = gew.get(b, 0) + 1
    diffs = []
    for k in run:
        E = stufen[k]["E"]
        Emin = min(E.values())
        diffs.append({f: (E[f] - Emin) / Emin for f in E})
    res["startformen"] = dict(gewinner=gew, rel_ueber_min=dict(zip([str(k) for k in run], diffs)))
    # p_per nur aus A
    Ak = {}
    for k in run:
        f = fs[k].get("A")
        if f and konv(f) and f["chi_min"] < 0.1 and f["rand_phi"] <= 1e-6 and f["rand_chi"] <= 1e-6:
            Ak[k] = f["E"]
    runA = [k for k in run if k in Ak]
    ppA = [(k, float(np.log(Ak[k + 12] / Ak[k]) / np.log(P[frak]))) for k in runA if k + 12 in Ak]
    if ppA:
        mA = float(np.mean([v for _, v in ppA]))
        res["startformen"].update(p_per_A=ppA, p_mittel_A=mA,
                                  robust=bool(len(vals) and abs(mA - res["p_mittel"]) <= 0.01))
    # Generationen
    kf, kst = lies(cfg["kontr"])
    gen = []
    if kst:
        kinfo = json.load(open(os.path.join(AUS, cfg["kinfo"])))
        for k in sorted(kst):
            st2 = kst[k]
            fA = fs.get(k, {}).get("A")
            if fA is None:
                continue
            gen.append(dict(k=k, E_kontr=st2["b_E"], E_hauptA=fA["E"], rel=st2["b_E"] / fA["E"] - 1,
                            konv_kontr=bool(st2["beste_konv"]), konv_A=konv(fA), Rbag=st2["b_Rbag"],
                            Rbag_durch_Rself_kontr=st2["b_Rbag"] / kinfo["R_self"],
                            rand=[st2["b_rand_phi"], st2["b_rand_chi"]]))
        beide = [x for x in gen if x["konv_kontr"] and x["konv_A"]]
        res["generationen"] = dict(R_self_kontr=kinfo["R_self"], g_kontr=kinfo["g"], je_stufe=gen,
                                   max_rel=float(max(abs(x["rel"]) for x in beide)) if beide else None,
                                   bestanden=bool(beide and max(abs(x["rel"]) for x in beide) <= 1e-6))
    # Beutelradius
    res["radius"] = [dict(k=k, Q=stufen[k]["Q"], Rbag=stufen[k]["b_Rbag"], V=stufen[k]["b_Vbag"],
                          wand=stufen[k]["b_wand"], Rbag_durch_Rself=stufen[k]["b_Rbag"] / Rself,
                          p_loc=stufen[k]["b_p_loc"], beste=stufen[k]["beste"], E=stufen[k]["b_E"],
                          nsub=stufen[k]["b_nsub"], gueltig=ok[k]) for k in ks]
    if run:
        pl = [stufen[k]["b_p_loc"] for k in run]
        res["p_loc_spanne"] = [float(min(pl)), float(max(pl))]
    erg[lauf] = res
    daten[lauf] = dict(stufen=stufen, formen=fs, ok=ok, run=run, pp=pp, frak=frak, kst=kst, tag=cfg["tag"])

# Vorhersagen
def ausgang(bed, offen=False):
    return "offen" if offen else ("eingetroffen" if bed else "nicht eingetroffen")

V = {}
f1 = erg.get("F1", {}) if isinstance(erg.get("F1"), dict) else {}
f2 = erg.get("F2", {}) if isinstance(erg.get("F2"), dict) else {}
p1 = f1.get("p_mittel")
p2 = f2.get("p_mittel")
off1 = (p1 is None) or f1.get("perioden", 0) < 3
off2 = (p2 is None) or f2.get("perioden", 0) < 3
V["E1"] = dict(ausgang=ausgang(p1 is not None and abs(p1 - 0.577) <= 0.015, off1), p=p1)
V["E2"] = dict(ausgang=ausgang(ds_V is not None and abs(ds_V - 1.19) <= 0.03, ds_V is None), ds=ds_V)
V["E3"] = dict(ausgang=ausgang(p2 is not None and p2 < (SOLL["vicsek"][0] + SOLL["vicsek"][1]) / 2, off2), p=p2,
               grenze=(SOLL["vicsek"][0] + SOLL["vicsek"][1]) / 2)
V["E4"] = dict(ausgang=ausgang(p1 is not None and p2 is not None and abs(p1 - SOLL["sierpinski"][0]) <= 0.02
                               and abs(p2 - SOLL["vicsek"][0]) <= 0.02, off1 or off2),
               abw_F1=(p1 - SOLL["sierpinski"][0]) if p1 is not None else None,
               abw_F2=(p2 - SOLL["vicsek"][0]) if p2 is not None else None)
erg["vorhersagen"] = V
with open(os.path.join(ZIEL, "auswertung.json"), "w") as fh:
    json.dump(erg, fh, indent=1, default=float)

# CSV je Lauf
for lauf, d in daten.items():
    with open(os.path.join(ZIEL, f"stufen-{lauf}.csv"), "w") as fh:
        fh.write("k,Q,beste,E,E_A,E_Bm,E_Bp,p_loc,p_fd,Rbag,Vbag,wand,nsub,gueltig\n")
        for k in sorted(d["stufen"]):
            st = d["stufen"][k]
            E = st["E"]
            fh.write(f"{k},{st['Q']:.6g},{st['beste']},{st['b_E']:.12g},{E.get('A', float('nan')):.12g},"
                     f"{E.get('Bm', float('nan')):.12g},{E.get('Bp', float('nan')):.12g},{st['b_p_loc']:.6f},"
                     f"{st.get('p_fd', float('nan')):.6f},{st['b_Rbag']:.0f},{st['b_Vbag']},{st['b_wand']:.0f},"
                     f"{st['b_nsub']},{int(d['ok'][k])}\n")

# Abbildungen
NAMEN = {"F1": "F1 Sierpinski g=10", "F2": "F2 Vicsek g=8"}
fig, axs = plt.subplots(1, 2, figsize=(13, 5))
for ax, lauf in zip(axs, ("F1", "F2")):
    if lauf not in daten:
        continue
    d = daten[lauf]
    frak = d["frak"]
    ks = sorted(d["stufen"])
    Q = np.array([d["stufen"][k]["Q"] for k in ks])
    pl = np.array([d["stufen"][k]["b_p_loc"] for k in ks])
    okm = np.array([d["ok"][k] for k in ks])
    ax.plot(Q[okm], pl[okm], "o", color="tab:blue", ms=4, label="p_loc = omega Q/E (beste Form, gueltig)")
    ax.plot(Q[~okm], pl[~okm], "x", color="tab:gray", ms=5, label="p_loc ungueltig/ausserhalb")
    pfd = [(d["stufen"][k]["Q"], d["stufen"][k]["p_fd"]) for k in ks if "p_fd" in d["stufen"][k]]
    if pfd:
        ax.plot([a for a, _ in pfd], [b for _, b in pfd], "+", color="tab:cyan", ms=7, label="p_fd (+-1 %)")
    if d["pp"]:
        qm = [np.sqrt(d["stufen"][k]["Q"] * d["stufen"][k + 12]["Q"]) for k, _ in d["pp"]]
        ax.plot(qm, [v for _, v in d["pp"]], "s-", color="tab:orange", ms=5, label="p_per (Sekante ueber 1 Periode)")
        pm = erg[lauf]["p_mittel"]
        ax.axhline(pm, color="k", ls="--", lw=1, label=f"Mittel p_per = {pm:.4f}")
    ps, pH = SOLL[frak]
    ax.axhline(ps, color="tab:green", lw=1.5, label=f"p_s = {ps:.4f}")
    ax.axhline(pH, color="tab:red", lw=1.5, label=f"p_H = {pH:.4f}")
    ax.set_xscale("log")
    ax.set_xlabel("Q")
    ax.set_ylabel("p")
    ax.set_ylim(0.3, 0.95)
    ax.set_title(NAMEN[lauf])
    ax.legend(fontsize=7, loc="upper right")
plt.tight_layout()
plt.savefig(os.path.join(ZIEL, "abb1-p.png"), dpi=130)
plt.close()

fig, axs = plt.subplots(2, 2, figsize=(13, 11))
for col, lauf in enumerate(("F1", "F2")):
    if lauf not in daten:
        continue
    d = daten[lauf]
    run = d["run"] if d["run"] else sorted(d["stufen"])
    wahl = run[::6][:4] if len(run) > 6 else run
    ax = axs[0, col]
    for k in wahl:
        st = d["stufen"][k]
        fl = glob.glob(os.path.join(AUS, "haupt", f"profil-{d['tag']}-k{k:03d}-{st['beste']}.npz"))
        if not fl:
            continue
        z = np.load(fl[0])
        ln = ax.plot(z["dist"], z["phi"] / z["phi"].max(), ".", ms=2, label=f"phi/max k={k} (Q={st['Q']:.3g})")
        ax.plot(z["dist"], z["chi"], "_", ms=3, color=ln[0].get_color(), alpha=0.5)
    ax.set_xscale("symlog", linthresh=1)
    ax.set_xlabel("Graphabstand vom Mittelpunkt")
    ax.set_ylabel("phi/max (Punkte), chi (Striche)")
    ax.set_title(NAMEN[lauf] + ": Profile")
    ax.legend(fontsize=7)
    ax = axs[1, col]
    k = wahl[-1] if wahl else None
    if k is not None:
        st = d["stufen"][k]
        fl = glob.glob(os.path.join(AUS, "haupt", f"profil-{d['tag']}-k{k:03d}-{st['beste']}.npz"))
        if fl:
            z = np.load(fl[0])
            xy = z["xy"]
            o = np.argsort(z["phi"])
            sc = ax.scatter(xy[o, 0], xy[o, 1], c=z["phi"][o] / z["phi"].max(), s=1.5, cmap="viridis")
            wb = z["chi"] < 0.5
            ax.scatter(xy[~wb, 0], xy[~wb, 1], c="lightgray", s=0.5)
            ax.set_aspect("equal")
            plt.colorbar(sc, ax=ax, label="phi/max")
            ax.set_title(f"{NAMEN[lauf]}: Beutel bei k={k}, Q={st['Q']:.3g} (grau: chi > 1/2)")
plt.tight_layout()
plt.savefig(os.path.join(ZIEL, "abb2-profile.png"), dpi=120)
plt.close()

if dsj:
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    for g in (5, 7, 8):
        z = dsj.get(f"zaehlung_g{g}")
        if z:
            ax.step(z["lams"], z["N"], where="post", label=f"g={g}, n={z['n']}")
    lam = np.logspace(-8, 1, 50)
    ax.plot(lam, 5 ** 8 * (lam / 8.0) ** (np.log(5) / np.log(15)), "k--", lw=0.8, label="Steigung ln5/ln15 = 0,5943")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("lambda")
    ax.set_ylabel("N(lambda) = #Eigenwerte < lambda")
    ax.set_title("Vicsek: Zaehlfunktion (Traegheitssatz)")
    ax.legend(fontsize=8)
    ax = axs[1]
    for g in (6, 7, 8):
        pf = os.path.join(AUS, "ds", f"rueckkehr-vicsek-g{g}.npy")
        if os.path.exists(pf):
            r = np.load(pf)
            t = np.arange(1, r.size)
            ax.loglog(t, r[1:], label=f"g={g}")
    t = np.logspace(0, np.log10(50625), 20)
    ax.loglog(t, 0.5 * t ** (-np.log(5) / np.log(15)), "k--", lw=0.8, label="t^(-0,5943)")
    ax.set_xlabel("t")
    ax.set_ylabel("P(Rueckkehr)")
    ax.set_title("Vicsek: traege Irrfahrt vom Mittelpunkt")
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(ZIEL, "abb3-ds.png"), dpi=130)
    plt.close()

fig, axs = plt.subplots(1, 2, figsize=(13, 5))
for ax, lauf in zip(axs, ("F1", "F2")):
    if lauf not in daten:
        continue
    d = daten[lauf]
    frak = d["frak"]
    ps = SOLL[frak][0]
    ks = sorted(d["stufen"])
    for f, mk in (("A", "o"), ("Bm", "v"), ("Bp", "^")):
        pts = [(d["stufen"][k]["Q"], d["stufen"][k]["E"][f]) for k in ks if f in d["stufen"][k]["E"]]
        if pts:
            q = np.array([a for a, _ in pts])
            e = np.array([b for _, b in pts])
            ax.plot(q, e / q ** ps, mk, mfc="none", label=f"Form {f}")
    q = np.array([d["stufen"][k]["Q"] for k in ks])
    e = np.array([d["stufen"][k]["b_E"] for k in ks])
    ax.plot(q, e / q ** ps, "k-", lw=1, label="Minimum")
    for k in d["run"][:1] + d["run"][-1:]:
        ax.axvline(d["stufen"][k]["Q"], color="gray", ls=":", lw=1)
    ax.set_xscale("log")
    ax.set_xlabel("Q")
    ax.set_ylabel(f"E / Q^p_s (p_s = {ps:.4f})")
    ax.set_title(NAMEN[lauf] + ": log-periodisch? (Punkte: Beutelbereich zwischen den Linien)")
    ax.legend(fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(ZIEL, "abb4-E.png"), dpi=130)
plt.close()

print(json.dumps({k: erg[k] for k in ("ds_V_gewertet", "soll", "vorhersagen")}, indent=1, default=float))
for lauf in ("F1", "F2"):
    r = erg.get(lauf)
    if isinstance(r, dict):
        print(lauf, "bereich", r["bereich"][:1], r["bereich"][-1:], "perioden", r["perioden"], "p_mittel",
              r.get("p_mittel"), "sd", r.get("p_sd"), "min/max", r.get("p_min"), r.get("p_max"))
        print("  p_per:", [(k, round(v, 4)) for k, v in r["p_per"]])
        print("  dEdQ:", {k: v for k, v in r.get("dEdQ", {}).items() if k != "je_stufe"})
        print("  startformen:", {k: v for k, v in r["startformen"].items() if k not in ("rel_ueber_min", "p_per_A")})
        if "generationen" in r:
            print("  generationen:", {k: v for k, v in r["generationen"].items() if k != "je_stufe"})
        print("  ungueltig:", r["ungueltig"])
