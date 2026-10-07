#!/usr/bin/env python3
# QBALL-PYRO-1: mechanische Urteile nach PLAN.md (Abschnitt 6), Bilder. Aufruf: auswertung.py <laufordner>
import sys, os, json, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1]
H_RING = 1.0
H_BALL = 0.5
E_TAB, Q_TAB = 428.641, 473.413          # RUNDE-02/tests1d Test 4, omega^2 = 0,70
AMP = [0.5, 1.0, 1.5, 2.0, 3.0]
KICKS = [0.02, 0.05, 0.1]


def lade(n):
    p = os.path.join(D, n)
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def reihe(lauf):
    return np.array(lauf["reihe"])


def numerik_ok(r, tol_E=1e-3, tol_Q=1e-10):
    dE = float(np.abs(r[:, 3] / r[0, 3] - 1).max())
    dQ = float(np.abs(r[:, 4] / r[0, 4] - 1).max())
    return dE <= tol_E and dQ <= tol_Q, dE, dQ


def wachstum(r):
    """Ausgleich ln(leck_N) = c + 2 gamma t im Bereich 1e-8 <= leck_N <= 1e-4 (beschreibend)."""
    t, l = r[:, 0], r[:, 1]
    m = (l >= 1e-8) & (l <= 1e-4)
    if m.sum() < 4:
        return None
    A = np.vstack([np.ones(m.sum()), t[m]]).T
    c, s = np.linalg.lstsq(A, np.log(l[m]), rcond=None)[0]
    return float(s / 2.0)


aus = {"urteile": {}, "kontrollen": {}, "beschreibend": {}}
U = aus["urteile"]

# ------------------------------------------------------------ QP0
lin = lade("linear.json")
if lin is None:
    U["QP0"] = {"urteil": "nicht auswertbar", "vermerk": "linear.json fehlt", "werte": {}}
else:
    rp8 = lin["ring_pruef"]["8"]
    gp_ok = all([lin["gitter_pruef"]["nachbarn_min_max"] == [6, 6],
                 lin["gitter_pruef"]["tetraeder_je_knoten_min_max"] == [2, 2],
                 lin["gitter_pruef"]["nachbar_abstand2_min_max_einheiten"] == [8, 8],
                 rp8["gitter_pruef"]["nachbarn_min_max"] == [6, 6]])
    ring_ok = all([rp8["ringknoten_mit_2_ringnachbarn"], rp8["aussen_je_genau_2_ringknoten"],
                   rp8["aussen_summe_null"], rp8["tetraeder_verschieden"], rp8["tetraeder_wechseln_oben_unten"]])
    w = dict(flach_abw_max=lin["flach_abw_max"], k_punkte=lin["k_punkte"],
             hexagon_resid_L8=rp8["resid_Av_plus_2v_inf"],
             hexagon_resid_alle_L={k: v["resid_Av_plus_2v_inf"] for k, v in lin["ring_pruef"].items()},
             band3_min=lin["band3_min"], band4_max=lin["band4_max"],
             realraum_gegen_k_max=lin["realraum_gegen_k_max"],
             realraum_anzahl_bei_minus2=lin["realraum_anzahl_bei_minus2"],
             realraum_anzahl_soll=lin["realraum_anzahl_soll"], gitter_ok=gp_ok, ring_vorpruefung_ok=ring_ok,
             sechserwege=lin["sechserwege_ab_s0"])
    if not gp_ok or not ring_ok:
        U["QP0"] = {"urteil": "nicht auswertbar", "vermerk": "Gitter- oder Ringvorpruefung verfehlt", "werte": w}
    else:
        ok = lin["flach_abw_max"] <= 1e-12 and rp8["resid_Av_plus_2v_inf"] <= 1e-12
        U["QP0"] = {"urteil": "eingetroffen" if ok else "nicht eingetroffen", "werte": w}

# ------------------------------------------------------------ QP1
q1 = lade("ring-qp1.json")
if q1 is None:
    U["QP1"] = {"urteil": "nicht auswertbar", "vermerk": "ring-qp1.json fehlt", "werte": {}}
else:
    w = {}
    ok_all = True
    vollst = True
    for a2 in AMP:
        L = q1["laeufe"].get(str(a2))
        if L is None:
            vollst = False
            continue
        r = reihe(L)
        fertig = L["status"] == "fertig" and r[-1, 0] >= 100.0 - 1e-9
        ok = L["resid_rel"] <= 1e-12 and float(r[:, 1].max()) <= 1e-10 and fertig
        ok_all &= ok
        vollst &= fertig
        w[str(a2)] = dict(omega2=L["omega2"], resid_rel=L["resid_rel"], resid_abs=L["resid_inf"],
                          leck_N_max=float(r[:, 1].max()), max_abs_phi_aussen=float(r[:, 9].max()),
                          t_ende=float(r[-1, 0]), dE=numerik_ok(r)[1], dQ=numerik_ok(r)[2])
    if not vollst:
        U["QP1"] = {"urteil": "nicht auswertbar", "vermerk": "Lauf unvollstaendig", "werte": w}
    else:
        U["QP1"] = {"urteil": "eingetroffen" if ok_all else "nicht eingetroffen", "werte": w,
                    "vermerk": "Zeitteil vorab ableitbar (exakte Ausloeschung in IEEE-Arithmetik, PLAN 3)"}


# ------------------------------------------------------------ QP2
def qp2_urteil(js):
    w = {}
    valid = True
    for a2 in AMP:
        L = js["laeufe"].get(str(a2))
        if L is None:
            valid = False
            continue
        r = reihe(L)
        fertig = L["status"] == "fertig" and r[-1, 0] >= 200.0 - 1e-9
        nok, dE, dQ = numerik_ok(r)
        valid &= fertig and nok
        lmax = float(r[:, 1].max())
        lend = float(r[-1, 1])
        i3 = np.argmax(r[:, 1] > 1e-3) if np.any(r[:, 1] > 1e-3) else None
        w[str(a2)] = dict(leck_N_max=lmax, leck_N_ende=lend, leck_Q_ende=float(r[-1, 2]),
                          kompakt=bool(lmax <= 1e-3), zerlaufen=bool(lend >= 1e-2),
                          t_leck_1e3=None if i3 is None else float(r[i3, 0]), dE=dE, dQ=dQ, fertig=fertig,
                          gamma_fit=wachstum(r))
    if not valid:
        return "nicht auswertbar", w
    A = any(w[str(a)]["kompakt"] for a in [1.5, 2.0, 3.0])
    B = all(w[str(a)]["zerlaufen"] for a in [0.5, 1.0])
    w["teil_A_ueber_band_kompakt"] = A
    w["teil_B_im_band_zerlaufen"] = B
    return ("eingetroffen" if (A and B) else "nicht eingetroffen"), w


q2 = lade("ring-qp2-s1.json")
stabil = []
if q2 is None:
    U["QP2"] = {"urteil": "nicht auswertbar", "vermerk": "ring-qp2-s1.json fehlt", "werte": {}}
else:
    u2, w2 = qp2_urteil(q2)
    proben = {}
    for n in ["ring-qp2-s2.json", "ring-qp2-L10.json", "ring-qp2-dt2.json"]:
        js = lade(n)
        if js is not None:
            proben[n] = qp2_urteil(js)
    robust = all(p[0] == u2 for p in proben.values()) and len(proben) == 3
    U["QP2"] = {"urteil": u2, "werte": w2,
                "vermerk": ("robust gegen Saat 2, L = 10, dt/2" if robust else
                            "nicht robust oder Probe fehlt: " + json.dumps({k: v[0] for k, v in proben.items()}))}
    aus["beschreibend"]["QP2_proben"] = {k: {"urteil": v[0], "werte": v[1]} for k, v in proben.items()}
    if u2 != "nicht auswertbar":
        stabil = [a for a in AMP if w2[str(a)]["kompakt"]]

# ------------------------------------------------------------ Bogoliubov (beschreibend)
bg = {}
for n in ["bogo-L3.json", "bogo-L4.json"]:
    js = lade(n)
    if js is not None:
        bg[n] = {k: dict(re_max=v["re_max"], anzahl_re_gt_1e5=v["anzahl_re_gt_1e5"], top=v["top"][:6])
                 for k, v in js["amplituden"].items()}
aus["beschreibend"]["bogoliubov"] = bg
q4L = lade("ring-qp2-L4.json")
if q4L is not None:
    aus["beschreibend"]["wachstum_zeitentwicklung_L4"] = {k: wachstum(reihe(v)) for k, v in q4L["laeufe"].items()}
if q2 is not None:
    aus["beschreibend"]["wachstum_zeitentwicklung_L8"] = {k: wachstum(reihe(v)) for k, v in q2["laeufe"].items()}


# ------------------------------------------------------------ QP3
def verschiebung(r):
    d = r[:, 5:8] - r[0, 5:8]
    dn = np.sqrt((d ** 2).sum(1))
    return dn, float(dn[-1]), float(dn.max()), float(r[-1, 8] / r[0, 8])


kick = {}
for k in KICKS:
    js = lade(f"ring-kick-{k}.json")
    if js is not None:
        kick[k] = js
w3 = {}
for k, js in kick.items():
    for a2 in AMP:
        L = js["laeufe"].get(str(a2))
        if L is None:
            continue
        r = reihe(L)
        dn, dend, dmax, qr = verschiebung(r)
        nok, dE, dQ = numerik_ok(r)
        w3[f"a2={a2},kick={k}"] = dict(D_ende=dend, D_max=dmax, Q_fenster_ende_rel=qr, leck_N_ende=float(r[-1, 1]),
                                       fertig=L["status"] == "fertig" and r[-1, 0] >= 200 - 1e-9, numerik_ok=nok,
                                       dE=dE, dQ=dQ)
if q2 is None or U["QP2"]["urteil"] == "nicht auswertbar":
    U["QP3"] = {"urteil": "nicht auswertbar", "vermerk": "QP2 nicht auswertbar, Stabilitaet unbekannt", "werte": w3}
elif not stabil:
    U["QP3"] = {"urteil": "nicht auswertbar", "vermerk": "kein stabiler Ring (keine Amplitude kompakt in QP2)",
                "werte": w3}
else:
    faelle = [(a, k) for a in stabil for k in KICKS]
    fehl = [f for f in faelle if f"a2={f[0]},kick={f[1]}" not in w3]
    if fehl:
        U["QP3"] = {"urteil": "nicht auswertbar", "vermerk": f"Laeufe fehlen: {fehl}", "werte": w3}
    else:
        ww = [w3[f"a2={a},kick={k}"] for a, k in faelle]
        gueltig = [x for x in ww if x["Q_fenster_ende_rel"] >= 0.1 and x["fertig"] and x["numerik_ok"]]
        nein = [x for x in gueltig if x["D_ende"] >= 0.5 * H_RING]
        if nein:
            u = "nicht eingetroffen"
        elif len(gueltig) == len(ww):
            u = "eingetroffen"
        else:
            u = "nicht auswertbar"
        U["QP3"] = {"urteil": u, "werte": w3, "vermerk": f"stabile Amplituden: {stabil}"}

# ------------------------------------------------------------ QP4
bk = lade("ball-kick-0.1.json")
if bk is None:
    U["QP4"] = {"urteil": "nicht auswertbar", "vermerk": "ball-kick-0.1.json fehlt", "werte": {}}
else:
    Eg, Qg = bk["newton"]["E"], bk["newton"]["Q"]
    r = reihe(bk["lauf"])
    dn, dend, dmax, qr = verschiebung(r)
    nok, dE, dQ = numerik_ok(r)
    fertig = bk["lauf"]["status"] == "fertig" and r[-1, 0] >= 200 - 1e-9
    newton_ok = bk["newton"]["res"][-1] <= 1e-10
    aE, aQ = Eg / E_TAB - 1, Qg / Q_TAB - 1
    w = dict(E_gitter=Eg, Q_gitter=Qg, E_kont=E_TAB, Q_kont=Q_TAB, abw_E=aE, abw_Q=aQ,
             radial_eigen=bk["radial"], radial_gegen_tabelle=dict(E=bk["radial"]["E"] / E_TAB - 1,
                                                                   Q=bk["radial"]["Q"] / Q_TAB - 1),
             newton_res=bk["newton"]["res"], abgetastet=bk["abgetastet"], D_ende=dend, D_max=dmax,
             D_ende_in_h=dend / H_BALL, Q_fenster_ende_rel=qr, dE=dE, dQ=dQ)
    w["kartenwortlaut_h3"] = dict(abw_E=(Eg / math.sqrt(2.0)) / E_TAB - 1, abw_Q=(Qg / math.sqrt(2.0)) / Q_TAB - 1)
    if not (newton_ok and nok and fertig):
        U["QP4"] = {"urteil": "nicht auswertbar", "vermerk": "Newton, Numerik oder Laufende verfehlt", "werte": w}
    else:
        ok = abs(aE) <= 0.05 and abs(aQ) <= 0.05 and dend > 2.0 * H_BALL and qr >= 0.5
        U["QP4"] = {"urteil": "eingetroffen" if ok else "nicht eingetroffen", "werte": w}
for n in ["ball-ruhe.json", "ball-kick-0.02.json"]:
    js = lade(n)
    if js is not None and "lauf" in js:
        r = reihe(js["lauf"])
        dn, dend, dmax, qr = verschiebung(r)
        aus["beschreibend"][n] = dict(D_ende=dend, D_max=dmax, Q_fenster_ende_rel=qr, dE=numerik_ok(r)[1],
                                      dQ=numerik_ok(r)[2], t_ende=float(r[-1, 0]), E=js["newton"]["E"],
                                      Q=js["newton"]["Q"])

with open(os.path.join(D, "auswertung.json"), "w") as fh:
    json.dump(aus, fh, indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o))
for k, v in U.items():
    print(k, v["urteil"], v.get("vermerk", ""))

# ------------------------------------------------------------ Bilder
if lin is not None:
    pf = lin["pfad"]
    s = np.array(pf["s"])
    ev = np.array(pf["ev"])
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for b in range(4):
        ax.plot(s, ev[:, b], color=["#c0392b", "#c0392b", "#2c3e50", "#2c3e50"][b], lw=[3.0, 1.5, 1.5, 1.5][b])
    for m_ in pf["marken"]:
        ax.axvline(m_, color="0.8", lw=0.8)
    ax.set_xticks(pf["marken"])
    ax.set_xticklabels(["Γ" if n == "G" else n for n in pf["namen"]])
    ax.set_ylabel("Eigenwert von A")
    ax2 = ax.twinx()
    ax2.set_ylim(*[6 - y for y in ax.get_ylim()])
    ax2.set_ylabel("-Δ = 6 - A")
    ax.set_title("Pyrochlor: zwei flache Baender bei A = -2 (rot), Abw. max %.1e" % lin["flach_abw_max"])
    fig.tight_layout()
    fig.savefig(os.path.join(D, "spektrum.png"), dpi=130)
    plt.close(fig)
if q2 is not None:
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    cols = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]
    q2b = lade("ring-qp2-s2.json")
    for c, a2 in zip(cols, AMP):
        L = q2["laeufe"].get(str(a2))
        if L is None:
            continue
        r = reihe(L)
        ax.semilogy(r[:, 0], np.maximum(r[:, 1], 1e-18), color=c, lw=1.6, label=f"a² = {a2} (Saat 1)")
        if q2b is not None and str(a2) in q2b["laeufe"]:
            rb = reihe(q2b["laeufe"][str(a2)])
            ax.semilogy(rb[:, 0], np.maximum(rb[:, 1], 1e-18), color=c, lw=0.8, ls="--")
    ax.axhline(1e-3, color="0.3", lw=0.8, ls=":")
    ax.axhline(1e-2, color="0.3", lw=0.8, ls="-.")
    ax.set_xlabel("t")
    ax.set_ylabel("Leckanteil (Norm ausserhalb der 6 Ringknoten)")
    ax.set_title("Ringe mit Rauschen 1e-6 (h = 1, L = 8); gestrichelt Saat 2")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "leck.png"), dpi=130)
    plt.close(fig)
fig, ax = plt.subplots(figsize=(7.5, 4.5))
cols = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]
if 0.1 in kick:
    for c, a2 in zip(cols, AMP):
        L = kick[0.1]["laeufe"].get(str(a2))
        if L is None:
            continue
        r = reihe(L)
        ax.plot(r[:, 0], verschiebung(r)[0] / H_RING, color=c, lw=1.2, label=f"Ring a² = {a2}, Stoss 0,1 ω")
if bk is not None:
    r = reihe(bk["lauf"])
    ax.plot(r[:, 0], verschiebung(r)[0] / H_BALL, color="k", lw=2.0, label="Ball ω² = 0,7, Stoss 0,1 ω")
js = lade("ball-kick-0.02.json")
if js is not None and "lauf" in js:
    r = reihe(js["lauf"])
    ax.plot(r[:, 0], verschiebung(r)[0] / H_BALL, color="0.4", lw=1.2, ls="--", label="Ball, Stoss 0,02 ω")
ax.axhline(0.5, color="0.3", lw=0.8, ls=":")
ax.axhline(2.0, color="0.3", lw=0.8, ls="-.")
ax.set_yscale("symlog", linthresh=0.1)
ax.set_xlabel("t")
ax.set_ylabel("|X(t) - X(0)| in Gitterabstaenden h")
ax.set_title("Ladungsschwerpunkt (Fenster): Ring (h = 1) gegen Ball (h = 0,5)")
ax.legend(fontsize=7)
fig.tight_layout()
fig.savefig(os.path.join(D, "schwerpunkt.png"), dpi=130)
plt.close(fig)
print("Bilder geschrieben")
