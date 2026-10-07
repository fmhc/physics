#!/usr/bin/env python3
# QBALL-DREIPOL-1: Auswertung nach PLAN.md Abschnitt 6 (Urteile QD0 bis QD3 nach Plan und nach Kartenwortlaut),
# Tabellen und Bilder. Aufruf: auswertung.py <laufordner>. Liest a.json, b_<tag>.json, c_<tag>.json (+ _bilder.npz),
# optional c1s2_<tag>.json. Schreibt auswertung.json, wechselwirkung.png, dreier.png, abstaende.png, energie_Q.png.
import sys, os, json, math, hashlib, time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1]
TAGS = [("m01", -0.1), ("0", 0.0), ("p01", 0.1)]
TAG = {g: t for t, g in TAGS}


def lade(name):
    p = os.path.join(D, name)
    return json.load(open(p)) if os.path.exists(p) else None


def sha(name):
    p = os.path.join(D, name)
    return hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None


def fl(x):
    return None if x is None else float(x)


out = {"erstellt_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "ordner": D, "eingaben": {},
       "urteile": {}, "tabellen": {}, "beschreibend": {}, "vermerke": []}
ZUSATZ = ("c1s2", "c1dt")   # c1 mit Saat 2 bzw. mit dt/2 (Proben, ohne Urteil)
namen = ["a.json"] + ["b_%s.json" % t for t, _ in TAGS] + ["c_%s.json" % t for t, _ in TAGS] + \
        ["%s_%s.json" % (z, t) for z in ZUSATZ for t, _ in TAGS]
for n in namen:
    out["eingaben"][n] = sha(n)

A = lade("a.json")
B = {t: lade("b_%s.json" % t) for t, _ in TAGS}
C = {t: lade("c_%s.json" % t) for t, _ in TAGS}
S2 = {(z, t): lade("%s_%s.json" % (z, t)) for z in ZUSATZ for t, _ in TAGS}

# ------------------------------------------------------------------ QD0 und Gewinner
zs = A["zustaende"]
conv2d = all(z["status"] == "konvergiert" for z in zs)
convrad = all(z["rad_status"] == "konvergiert" for z in zs)
maxabw = max(abs(z["abw"]) for z in zs)
if conv2d and convrad:
    u0 = "eingetroffen" if maxabw < 0.01 else "nicht eingetroffen"
else:
    u0 = "nicht auswertbar"
out["urteile"]["QD0"] = dict(plan=u0, kartenwortlaut=u0, max_abs_abw=maxabw, zustaende=len(zs),
                             alle_2d_konvergiert=conv2d, alle_radial_konvergiert=convrad,
                             max_res_2d=max(z["res"] for z in zs), regel="max |E_2D/E_rad(g_eff) - 1| < 0,01")
gewinner = {}
tabA = []
for z in zs:
    tabA.append({k: z[k] for k in ("Q", "g4", "richtung", "g_eff", "E", "E_rad", "abw", "om", "it", "res", "R_halb")})
for Q in sorted(set(z["Q"] for z in zs)):
    for g4 in sorted(set(z["g4"] for z in zs)):
        sel = [z for z in zs if z["Q"] == Q and z["g4"] == g4]
        best = min(sel, key=lambda z: z["E"])
        gewinner["Q=%g,g4=%g" % (Q, g4)] = dict(gewinner=best["richtung"],
                                                E={z["richtung"]: z["E"] for z in sel})
out["tabellen"]["a"] = tabA
out["beschreibend"]["gewinner"] = gewinner
if A.get("extern"):
    out["beschreibend"]["extern_qbbs2d"] = A["extern"]
mix_g4 = []
for g4 in (-0.1, 0.1):
    ok = all(gewinner.get("Q=%g,g4=%g" % (Q, g4), {}).get("gewinner") == "gleich_gemischt" for Q in (60.0, 180.0))
    if ok:
        mix_g4.append(g4)
g4_mix = mix_g4[0] if len(mix_g4) == 1 else None
out["beschreibend"]["mischungs_g4"] = g4_mix

# ------------------------------------------------------------------ QD1
qd1 = {}
r_plan, r_kw = [], []
for t, g in TAGS:
    b = B[t]
    if b is None:
        qd1[t] = None
        continue
    R = b["ball"]["R_halb"]
    row = [r for r in b["eingespannt"] if abs(r["d_R"] - 2.0) < 1e-9]
    rel = [r for r in b["relaxiert"] if abs(r["d_R"] - 2.0) < 1e-9]
    if not row:
        qd1[t] = None
        continue
    row = row[0]
    Ag = abs(row["gleich_phase"])
    Av = abs(row["verschieden"])
    e = dict(g4=g, R_halb=R, R_rms=b["ball"]["R_rms"], E1=b["ball"]["E"], om1=b["ball"]["om"],
             E_gleich_phase=row["gleich_phase"], E_gleich_gegen=row["gleich_gegen"],
             E_verschieden_eingespannt=row["verschieden"], E_dreieck_eingespannt=row["dreieck_verschieden"],
             verhaeltnis_plan=Av / Ag if Ag > 0 else None)
    r_plan.append(e["verhaeltnis_plan"])
    if rel:
        e["E_verschieden_relaxiert"] = rel[0]["verschieden"]
        e["relax_status"] = rel[0]["status"]
        e["verhaeltnis_kw"] = abs(rel[0]["verschieden"]) / Ag if Ag > 0 else None
        r_kw.append(e["verhaeltnis_kw"])
    else:
        r_kw.append(None)
    qd1[t] = e


def urteil_qd1(rs):
    if len(rs) != 3 or any(r is None for r in rs):
        return "nicht auswertbar"
    return "eingetroffen" if all(r <= 1.0 / 3.0 for r in rs) else "nicht eingetroffen"


out["urteile"]["QD1"] = dict(plan=urteil_qd1(r_plan), kartenwortlaut=urteil_qd1(r_kw), je_g4=qd1,
                             regel_plan="|E_versch(2R)| <= |E_gleich,Phase(2R)|/3 bei allen g4, eingespannt",
                             regel_kw="wie Plan, E_versch aus der relaxierten (Stift-)Rechnung")
tabB = {}
for t, g in TAGS:
    if B[t] is not None:
        tabB[t] = dict(g4=g, ball=B[t]["ball"], eingespannt=B[t]["eingespannt"],
                       relaxiert=[{k: r[k] for k in ("d_R", "d", "verschieden", "status", "it", "schwerpunkte")}
                                  for r in B[t]["relaxiert"]])
out["tabellen"]["b"] = tabB


# ------------------------------------------------------------------ QD2 und QD3
def gestalt(paar, R):
    if max(paar) < 0.25 * R:
        return "verschmolzen"
    if min(paar) > R:
        return "dreieck"
    return "zwischenform"


def lauf_auswerten(run, R, Q0ref=None):
    rec = np.array(run["reihe"])
    t = rec[:, 0]
    Q0 = rec[0, 2:5]
    Qin = rec[:, 5:8]
    frac = Qin / Q0[None, :]
    share = Qin[-1] / Qin[-1].sum()
    X = rec[:, 8:11]
    Y = rec[:, 11:14]
    paar = np.stack([np.hypot(X[:, i] - X[:, j], Y[:, i] - Y[:, j]) for i, j in ((0, 1), (0, 2), (1, 2))], 1)
    pmax = paar.max(1)
    k_v = np.nonzero(pmax < 0.25 * R)[0]
    gueltig = (run["status"] == "fertig" and t[-1] >= 200.0 - 1e-9 and run["dE_rel"] <= 1e-3 and
               run["dQ_rel"] <= 1e-8)
    i_ok = bool(frac.min() >= 0.9)
    ii_ok = bool(share.max() <= 0.6)
    return dict(gueltig=bool(gueltig), t_ende=float(t[-1]), dE_rel=run["dE_rel"], dQ_rel=run["dQ_rel"],
                min_anteil_im_klumpen=float(frac.min()), anteil_t_ende=frac[-1].tolist(),
                hoechstanteil_t_ende=float(share.max()), kriterium_i=i_ok, kriterium_ii=ii_ok,
                paarabstand_R_t0=(paar[0] / R).tolist(), paarabstand_R_t_ende=(paar[-1] / R).tolist(),
                paarabstand_R_max=float(paar.max() / R), paarabstand_R_min=float(paar.min() / R),
                t_verschmolzen=(float(t[k_v[0]]) if len(k_v) else None),
                urteil=("eingetroffen" if (i_ok and ii_ok) else "nicht eingetroffen") if gueltig else
                "nicht auswertbar")


besch_c = {}
for t, g in TAGS:
    c = C[t]
    if c is None:
        continue
    R = c["ball"]["R_halb"]
    e = dict(g4=g, R_halb=R, d0=c["d0"], R_K=c["R_K"], E1=c["ball"]["E"], E_drei_getrennt=c["E_drei_getrennt"],
             E_eingespannt=c["E_eingespannt"])
    if "fluss" in c:
        f = c["fluss"]
        e.update(E_fluss_ende=f["E_ende"], B=f["B"], B_rel=f["B"] / c["E_drei_getrennt"], fluss_status=f["status"],
                 fluss_it=f["it"], fluss_res=f["res"], paarabstand_R=[p / R for p in f["paarabstand"]],
                 gestalt=gestalt(f["paarabstand"], R), lokal_anteil=f["lokal_anteil"])
        zm = [z for z in zs if z["Q"] == 3.0 * c["Q1"] and z["g4"] == g and z["richtung"] == "gleich_gemischt"]
        if zm:
            e["E_mix_a"] = zm[0]["E"]
            e["E_fluss_minus_E_mix_a"] = f["E_ende"] - zm[0]["E"]
    for name, run in c.get("laeufe", {}).items():
        e[name] = lauf_auswerten(run, R)
    for z in ZUSATZ:
        if S2.get((z, t)) is not None:
            for name, run in S2[(z, t)].get("laeufe", {}).items():
                e["%s_%s_saat%d_dt%g" % (name, z, run["saat"], run["dt"])] = lauf_auswerten(run, R)
    besch_c[t] = e
out["beschreibend"]["c"] = besch_c

if g4_mix is None or TAG[g4_mix] not in besch_c or "E_fluss_ende" not in besch_c[TAG[g4_mix]]:
    out["urteile"]["QD2"] = dict(plan="nicht auswertbar", kartenwortlaut="nicht auswertbar", g4_mix=g4_mix)
    qd2_plan = False
else:
    e = besch_c[TAG[g4_mix]]
    thr = 1e-3 * e["E_drei_getrennt"]
    loc = min(e["lokal_anteil"])
    qd2_plan = bool(e["B"] >= thr and loc >= 0.98)
    qd2_kw = bool(e["E_fluss_ende"] < e["E_drei_getrennt"] * (1.0 - 1e-6))
    out["urteile"]["QD2"] = dict(plan="eingetroffen" if qd2_plan else "nicht eingetroffen",
                                 kartenwortlaut="eingetroffen" if qd2_kw else "nicht eingetroffen", g4_mix=g4_mix,
                                 B=e["B"], schwelle=thr, B_rel=e["B_rel"], min_lokal_anteil=loc,
                                 gestalt=e["gestalt"], fluss_status=e["fluss_status"],
                                 E_fluss_minus_E_mix_a=e.get("E_fluss_minus_E_mix_a"),
                                 regel_plan="B >= 1e-3 * 3 E_1 und Anteil je Komponente im Klumpengebiet >= 0,98",
                                 regel_kw="E_ende < 3 E_1 (1 - 1e-6)")
    if e["gestalt"] == "verschmolzen":
        out["vermerke"].append("QD2: Flussendzustand verschmolzen; der Energievergleich war nach PLAN Abschnitt 2.4 "
                               "vorab ableitbar (E/Q faellt mit Q, g_eff = g4/3 < g4).")

if g4_mix is None or not qd2_plan:
    out["urteile"]["QD3"] = dict(plan="entfaellt (QD2 Plan nicht eingetroffen)", kartenwortlaut="entfaellt")
else:
    e = besch_c[TAG[g4_mix]]
    up = e.get("c1", {}).get("urteil", "nicht auswertbar")
    uk = e.get("c2", {}).get("urteil", "nicht auswertbar")
    out["urteile"]["QD3"] = dict(plan=up, kartenwortlaut=uk, g4_mix=g4_mix, c1=e.get("c1"), c2=e.get("c2"),
                                 regel="(i) Q_a,in(t)/Q_a(0) >= 0,9 fuer alle a, t <= 200; (ii) max Anteil bei t = 200"
                                       " <= 0,6; gueltig bei T = 200, dE <= 1e-3, dQ <= 1e-8")

# ------------------------------------------------------------------ Bilder
try:
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.6), sharey=True)
    for ax, (t, g) in zip(axs, TAGS):
        b = B[t]
        if b is None:
            continue
        x = [r["d_R"] for r in b["eingespannt"]]
        ax.plot(x, [r["gleich_phase"] for r in b["eingespannt"]], "o-", label="gleicher Pol, in Phase")
        ax.plot(x, [r["gleich_gegen"] for r in b["eingespannt"]], "s-", label="gleicher Pol, gegenphasig")
        ax.plot(x, [r["verschieden"] for r in b["eingespannt"]], "^-", label="verschiedene Pole (eingespannt)")
        ax.plot([r["d_R"] for r in b["relaxiert"]], [r["verschieden"] for r in b["relaxiert"]], "v", ms=9,
                mfc="none", label="verschiedene Pole (relaxiert, Stifte)")
        ax.plot(x, [r["dreieck_verschieden"] / 3.0 for r in b["eingespannt"]], "d--",
                label="Dreieck drei Pole, je Paar (eingespannt)")
        ax.axvline(2.0, color="k", lw=0.8, ls=":")
        ax.axhline(0.0, color="k", lw=0.5)
        ax.set_yscale("symlog", linthresh=1e-3)
        ax.set_xlabel("Abstand d / R_halb")
        ax.set_title("g4 = %+.1f (R_halb = %.3f)" % (g, b["ball"]["R_halb"]))
        ax.grid(alpha=0.3)
    axs[0].set_ylabel("Wechselwirkungsenergie E_int (feste Ladungen)")
    axs[0].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "wechselwirkung.png"), dpi=110)
    plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild wechselwirkung: %r" % ex)

try:
    rows = []
    for t, g in TAGS:
        p = os.path.join(D, "c_%s_bilder.npz" % t)
        if os.path.exists(p):
            z = np.load(p)
            for name in ("c1", "c2"):
                ks = ["%s_t%g" % (name, ts) for ts in (0.0, 100.0, 200.0)]
                if all(k in z.files for k in ks):
                    rows.append(("%s, g4 = %+.1f" % (name, g), [z[k] for k in ks], z["x"]))
    if rows:
        fig, axs = plt.subplots(len(rows), 3, figsize=(10.5, 3.5 * len(rows)), squeeze=False)
        for i, (lab, arrs, x) in enumerate(rows):
            norm = max(float(arrs[0].max()), 1e-12)
            m = np.abs(x) <= 16.0
            for j, (arr, ts) in enumerate(zip(arrs, (0, 100, 200))):
                rgb = np.clip(np.stack([arr[0], arr[1], arr[2]], -1) / norm, 0.0, 1.0)
                rgb = rgb[np.ix_(m, m)]
                axs[i, j].imshow(np.transpose(rgb, (1, 0, 2)), origin="lower",
                                 extent=[x[m][0], x[m][-1], x[m][0], x[m][-1]])
                axs[i, j].set_title("%s, t = %d" % (lab, ts), fontsize=9)
                axs[i, j].set_xticks([-16, 0, 16])
                axs[i, j].set_yticks([-16, 0, 16])
        fig.suptitle("|phi_1|^2 rot, |phi_2|^2 gruen, |phi_3|^2 blau (normiert auf das Startmaximum)", fontsize=10)
        fig.tight_layout()
        fig.savefig(os.path.join(D, "dreier.png"), dpi=100)
        plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild dreier: %r" % ex)

try:
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.2))
    for t, g in TAGS:
        c = C[t]
        if c is None:
            continue
        R = c["ball"]["R_halb"]
        for name, run in c.get("laeufe", {}).items():
            rec = np.array(run["reihe"])
            X, Y = rec[:, 8:11], rec[:, 11:14]
            paar = np.stack([np.hypot(X[:, i] - X[:, j], Y[:, i] - Y[:, j]) for i, j in ((0, 1), (0, 2), (1, 2))],
                            1)
            axs[0].plot(rec[:, 0], paar.max(1) / R, label="%s g4=%+.1f" % (name, g))
            axs[1].plot(rec[:, 0], (rec[:, 5:8] / rec[0, 2:5][None, :]).min(1), label="%s g4=%+.1f" % (name, g))
    axs[0].set_xlabel("t")
    axs[0].set_ylabel("groesster Paarabstand der Polschwerpunkte / R_halb")
    axs[1].set_xlabel("t")
    axs[1].set_ylabel("min_a Q_a,in / Q_a(0)")
    axs[1].axhline(0.9, color="k", ls=":", lw=0.8)
    for ax in axs:
        ax.grid(alpha=0.3)
        ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "abstaende.png"), dpi=110)
    plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild abstaende: %r" % ex)

try:
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.2), sharey=True)
    for ax, (t, g) in zip(axs, TAGS):
        for name in ("ein_pol", "zwei_pole", "gleich_gemischt"):
            sel = sorted([z for z in zs if z["g4"] == g and z["richtung"] == name], key=lambda z: z["Q"])
            ax.plot([z["Q"] for z in sel], [z["E"] / z["Q"] for z in sel], "o-", label=name)
        ax.set_title("g4 = %+.1f" % g)
        ax.set_xlabel("Q")
        ax.grid(alpha=0.3)
    axs[0].set_ylabel("E / Q")
    axs[0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "energie_Q.png"), dpi=110)
    plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild energie_Q: %r" % ex)

with open(os.path.join(D, "auswertung.json.tmp"), "w") as fh:
    json.dump(out, fh, indent=1)
os.replace(os.path.join(D, "auswertung.json.tmp"), os.path.join(D, "auswertung.json"))
print(json.dumps(out["urteile"], indent=1, default=str)[:4000])
