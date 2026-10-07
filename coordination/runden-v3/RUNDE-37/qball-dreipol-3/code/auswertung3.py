#!/usr/bin/env python3
# QBALL-DREIPOL-3: Auswertung nach PLAN.md Abschnitt 6 (Urteile DR0 bis DR2 nach Plan und nach Kartenwortlaut),
# Tabellen und Bilder. Aufruf: auswertung3.py <laufordner>. Liest bisekt3.json, bisekt2.json, stab3.json
# (+ *_bilder.npz). Schreibt auswertung.json und PNG-Bilder.
import sys, os, json, math, hashlib, time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1]
ST6 = ["V1", "V2", "L1", "L2", "P1", "P2"]
EXTRA = ["Z1", "R5", "R20"]
# Bezugswerte der Karte (DR0) und aus QBALL-DREIPOL-2 (DP0)
KARTE_LUECKE_3D, TOL_LUECKE_3D = 3.32, 0.1
KARTE_D_R, KARTE_LUECKE_2D = 1.245, 0.146
SCHRANKE_DR2 = 1.3          # "gleich auf 30 %": max/min <= 1,3
BREITE_MAX = 0.10           # Klammer (Q_hi - Q_lo)/Q_hi hoechstens 10 %


def lade(name):
    p = os.path.join(D, name)
    return json.load(open(p)) if os.path.exists(p) else None


def sha(name):
    p = os.path.join(D, name)
    return hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None


out = {"erstellt_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "ordner": D, "eingaben": {},
       "urteile": {}, "beschreibend": {}, "vermerke": []}
for n in ("bisekt3.json", "bisekt2.json", "stab3.json"):
    out["eingaben"][n] = sha(n)
B = {3: lade("bisekt3.json"), 2: lade("bisekt2.json")}
S3 = lade("stab3.json")


def schritt_bei(b, Q):
    if b is None:
        return None
    for s in b["schritte"]:
        if abs(s["Q1"] - Q) < 1e-9:
            return s
    return None


def zeile(s):
    """Bisektionszeile: E_start, E_Mischball, E_Tropfen (Sektorlauf), E_Ende (beruehrend), Ausgaenge, Radien."""
    v = s["vorab"]
    e = s["beruehrend"]["ende"]
    return dict(Q1=s["Q1"], rolle=s["rolle"], om_ball=s["ball"]["om"], R_halb=s["R_halb"],
                E_start=v["E_start"], E_Misch=v["E_Misch"], E_Misch_radial=v["E_Misch_radial"],
                E_Tropfen=v["E_Tropfen"], E_drei_getrennt=v["E_drei_getrennt"],
                start_minus_misch=v["start_minus_misch"], start_minus_tropfen=v["start_minus_tropfen"],
                tropfen_minus_misch=(v["E_Tropfen"] - v["E_Misch"]) if v["E_Tropfen"] is not None else None,
                erzwungen=v["erzwungen"], erzwungen_gegen_misch=v["erzwungen_gegen_misch"],
                erzwungen_gegen_tropfen=v["erzwungen_gegen_tropfen"],
                sektorstart_minus_misch=v["sektorstart_minus_misch"], sektorlauf_erzwungen=v["sektorlauf_erzwungen"],
                ausgang=s["ausgang"], gestalt=s["beruehrend"]["gestalt"], status=s["beruehrend"]["status"],
                it=s["beruehrend"]["it"], E_ende=e["E"], ende_minus_misch=e["E"] - v["E_Misch"],
                paarabstand_R=e["paarabstand_R"], reinheit=e["reinheit"], res=e["res"],
                sektor_ausgang=s["sektor"]["ausgang"], sektor_gestalt=s["sektor"]["gestalt"],
                sektor_status=s["sektor"]["status"], sektor_it=s["sektor"]["it"],
                sektor_E_ende=s["sektor"]["ende"]["E"], sektor_paarabstand_R=s["sektor"]["ende"]["paarabstand_R"],
                gueltig=s["gueltig"], R_eq_ball=s["ball"]["radien"]["R_eq"], R_eq_ende=s["beruehrend"]["radien"]["R_eq"],
                R_eq_misch=s["misch"]["radien"]["R_eq"], R_vol_ball=s["ball"]["radien"]["R_vol"],
                R_vol_ende=s["beruehrend"]["radien"]["R_vol"], R_rms_ball=s["ball"]["radien"]["R_rms"],
                R_rms_ende=s["beruehrend"]["radien"]["R_rms"], sek=s["sek"])


tab = {}
for dim in (3, 2):
    b = B[dim]
    if b is None:
        tab[dim] = None
        continue
    tab[dim] = dict(zeilen=[zeile(s) for s in b["schritte"]], klammer=b.get("klammer"), N=b["N"], L=b["L"],
                    h=b["h"], g4=b["g4"])
out["beschreibend"]["bisektion"] = {"%dd" % k: v for k, v in tab.items()}
for dim in (3, 2):
    if tab[dim] is None:
        continue
    for z in tab[dim]["zeilen"]:
        if z["erzwungen"]:
            out["vermerke"].append("%dD Q1 = %g: Start schon unter einem Ausgang (erzwungen), zaehlt nur als Kontrolle"
                                   % (dim, z["Q1"]))
        if z["sektorlauf_erzwungen"]:
            out["vermerke"].append("%dD Q1 = %g: Sektorstart unter dem Mischball; E_Tropfen stammt aus einem "
                                   "erzwungenen Hilfslauf (Fixpunkt bleibt Fixpunkt)" % (dim, z["Q1"]))

# ------------------------------------------------------------------ DR0
teile = {}
s = schritt_bei(B[3], 800.0)
if s is None:
    teile["3d_800"] = dict(urteil="nicht auswertbar")
else:
    z = zeile(s)
    luecke = z["E_Misch"] - z["E_ende"]
    if z["ausgang"] == "Tropfen":
        u = "eingetroffen" if abs(luecke - KARTE_LUECKE_3D) <= TOL_LUECKE_3D else "nicht eingetroffen"
    elif z["ausgang"] == "verschmolzen":
        u = "nicht eingetroffen"
    else:
        u = "nicht auswertbar"
    teile["3d_800"] = dict(ausgang=z["ausgang"], luecke=luecke, urteil=u)
s = schritt_bei(B[3], 400.0)
if s is None:
    teile["3d_400"] = dict(urteil="nicht auswertbar")
else:
    z = zeile(s)
    u = {"verschmolzen": "eingetroffen", "Tropfen": "nicht eingetroffen"}.get(z["ausgang"], "nicht auswertbar")
    teile["3d_400"] = dict(ausgang=z["ausgang"], paarabstand_R=z["paarabstand_R"], urteil=u)
s = schritt_bei(B[2], 60.0)
if s is None:
    teile["2d_60"] = dict(urteil="nicht auswertbar")
else:
    z = zeile(s)
    luecke = z["E_Misch"] - z["E_ende"]
    if z["ausgang"] == "Tropfen":
        abw_d = max(abs(x / KARTE_D_R - 1.0) for x in z["paarabstand_R"])
        abw_l = abs(luecke / KARTE_LUECKE_2D - 1.0)
        u = "eingetroffen" if (abw_d <= 0.02 and abw_l <= 0.10) else "nicht eingetroffen"
    elif z["ausgang"] == "verschmolzen":
        abw_d = abw_l = None
        u = "nicht eingetroffen"
    else:
        abw_d = abw_l = None
        u = "nicht auswertbar"
    teile["2d_60"] = dict(ausgang=z["ausgang"], E_ende=z["E_ende"], luecke=luecke, paarabstand_R=z["paarabstand_R"],
                          max_rel_abw_paarabstand=abw_d, rel_abw_luecke=abw_l, urteil=u)
us = [t["urteil"] for t in teile.values()]
u0 = ("eingetroffen" if all(u == "eingetroffen" for u in us) else
      ("nicht eingetroffen" if any(u == "nicht eingetroffen" for u in us) else "nicht auswertbar"))
out["urteile"]["DR0"] = dict(plan=u0, kartenwortlaut=u0, teile=teile,
                             regel="3D Q1 = 800: Tropfen, E_Misch - E_Ende = 3,32 +- 0,1; 3D Q1 = 400: verschmolzen; "
                                   "2D Q1 = 60: Tropfen, Paarabstand/R auf 2 % bei 1,245, Luecke auf 10 % bei 0,146")

# ------------------------------------------------------------------ DR1
dr1 = {}
if S3 is not None and "stoerungen" in S3:
    Eref = S3["referenz"]["E"]
    for name, s in S3["stoerungen"].items():
        if "ende" not in s:
            dr1[name] = dict(status=s.get("status"), plan="offen", kartenwortlaut="nicht zurueck")
            continue
        e, st = s["ende"], s["start"]
        konv = s["status"] == "konvergiert"
        zur = konv and e["d_form_R"] < 0.02 and e["d_rms_R"] < 0.02 and abs(e["dE"]) < 1e-3
        weg = (konv and not zur) or (e["dE"] < -1e-3) or ((not konv) and e["d_rms_R"] > st["d_rms_R"])
        plan = "zurueck" if zur else ("nicht zurueck" if weg else "offen")
        kw = "zurueck" if (e["d_rms_R"] < 0.02 and abs(e["dE"]) / abs(Eref) < 1e-3) else "nicht zurueck"
        dr1[name] = dict(text=s["text"], status=s["status"], it=s["it"], sek=s["sek"], d_rms_start=st["d_rms_R"],
                         d_form_start=st["d_form_R"], dE_start=st["dE"], d_rms_ende=e["d_rms_R"],
                         d_form_ende=e["d_form_R"], dE_ende=e["dE"], res_ende=e["res"],
                         reinheit_start=st["reinheit"], reinheit_ende=e["reinheit"],
                         paarabstand_R_ende=e["paarabstand_R"], plan=plan, kartenwortlaut=kw,
                         start_unter_misch=bool(st["E"] < S3["mischball"]["E"]),
                         beschreibend=name not in ST6)
    sel = [dr1[n] for n in ST6 if n in dr1]
    if len(sel) == 6:
        if all(x["plan"] == "zurueck" for x in sel):
            up = "eingetroffen"
        elif any(x["plan"] == "nicht zurueck" for x in sel):
            up = "nicht eingetroffen"
        else:
            up = "nicht auswertbar"
        uk = "eingetroffen" if all(x["kartenwortlaut"] == "zurueck" for x in sel) else "nicht eingetroffen"
    else:
        up = uk = "nicht auswertbar"
    ref = S3["referenz"]
    out["urteile"]["DR1"] = dict(plan=up, kartenwortlaut=uk, je_stoerung=dr1, E_ref=Eref,
                                 referenz={k: ref[k] for k in ("status", "it", "E", "res", "paarabstand_R",
                                                               "reinheit", "gestalt", "radien")},
                                 E_misch=S3["mischball"]["E"], E_ref_minus_misch=Eref - S3["mischball"]["E"],
                                 R_halb=S3["ball"]["R_halb"],
                                 regel_plan="je Stoerung: Fluss konvergiert (Residuum < tol_st), d_form < 0,02 R, "
                                            "d_rms < 0,02 R, |E_Ende - E_ref| < 1e-3; alle sechs (V1, V2, L1, L2, P1, P2)",
                                 regel_kw="je Stoerung am Flussende: d_rms < 0,02 R und |dE|/E_ref < 1e-3; alle sechs")
    out["vermerke"].append("DR1: P1 und P2 (gleichfoermiger Phasenversatz je Komponente) sind exakte Symmetrien von "
                           "E_Q (U(1)^3); ihre Rueckkehr war vorab ableitbar (PLAN 2). L1 und L2 sind eine "
                           "Symmetrieklasse (D3 x S3).")
    if ref["gestalt"] != "dreieck":
        out["vermerke"].append("DR1: Referenz bei Q1 = %g ist kein Dreieck (%s)" % (S3["Q1"], ref["gestalt"]))
else:
    out["urteile"]["DR1"] = dict(plan="nicht auswertbar", kartenwortlaut="nicht auswertbar")


# ------------------------------------------------------------------ DR2
def schwelle(dim):
    t = tab[dim]
    if t is None or t["klammer"] is None:
        return None
    k = t["klammer"]
    if k["Q_lo"] is None or k["Q_hi"] is None:
        return dict(klammer=k, auswertbar=False, grund="keine Klammer (%s)" % k["stop"])
    s = schritt_bei(B[dim], k["Q_hi"])
    z = zeile(s)
    breite = (k["Q_hi"] - k["Q_lo"]) / k["Q_hi"]
    ok = bool(z["ausgang"] == "Tropfen" and not z["erzwungen"] and breite <= BREITE_MAX)
    return dict(klammer=k, auswertbar=ok, rel_breite=breite, Q_lo=k["Q_lo"], Q_hi=k["Q_hi"],
                om_ball_Q_hi=z["om_ball"], R_halb_ball=z["R_halb"],
                R_stern_abs=z["R_eq_ende"], R_eq_ball=z["R_eq_ball"], R_stern_norm=z["R_eq_ende"] / z["R_eq_ball"],
                R_vol_abs=z["R_vol_ende"], R_vol_norm=z["R_vol_ende"] / z["R_vol_ball"],
                R_rms_abs=z["R_rms_ende"], R_rms_norm=z["R_rms_ende"] / z["R_rms_ball"],
                R_eq_misch=z["R_eq_misch"], tropfen_minus_misch=z["ende_minus_misch"],
                grund=None if ok else "Klammer zu breit, erzwungen oder kein Tropfen am oberen Ende")


def verhaeltnis(a, b):
    return max(a, b) / min(a, b)


sw = {dim: schwelle(dim) for dim in (3, 2)}
if sw[3] and sw[2] and sw[3]["auswertbar"] and sw[2]["auswertbar"]:
    v_abs = verhaeltnis(sw[2]["R_stern_abs"], sw[3]["R_stern_abs"])
    v_norm = verhaeltnis(sw[2]["R_stern_norm"], sw[3]["R_stern_norm"])
    up = "eingetroffen" if v_abs <= SCHRANKE_DR2 else "nicht eingetroffen"
    uk = "eingetroffen" if v_norm <= SCHRANKE_DR2 else "nicht eingetroffen"
    besch = dict(R_vol_abs=verhaeltnis(sw[2]["R_vol_abs"], sw[3]["R_vol_abs"]),
                 R_vol_norm=verhaeltnis(sw[2]["R_vol_norm"], sw[3]["R_vol_norm"]),
                 R_rms_abs=verhaeltnis(sw[2]["R_rms_abs"], sw[3]["R_rms_abs"]),
                 R_rms_norm=verhaeltnis(sw[2]["R_rms_norm"], sw[3]["R_rms_norm"]),
                 R_halb_ball=verhaeltnis(sw[2]["R_halb_ball"], sw[3]["R_halb_ball"]))
else:
    v_abs = v_norm = None
    besch = None
    up = uk = "nicht auswertbar"
out["urteile"]["DR2"] = dict(plan=up, kartenwortlaut=uk, schwelle_3d=sw[3], schwelle_2d=sw[2],
                             verhaeltnis_abs=v_abs, verhaeltnis_norm=v_norm, verhaeltnisse_beschreibend=besch,
                             duennwand_geometrie_norm=math.sqrt(3.0) / 3.0 ** (1.0 / 3.0),
                             regel_plan="R* absolut (R_eq des Tropfens am oberen Klammerende, Laengeneinheit 1/m), "
                                        "max/min(2D, 3D) <= 1,3; beide Klammern (Q_hi - Q_lo)/Q_hi <= 0,1",
                             regel_kw="R* in Einheiten des Einpolradius gleicher Ladung Q1 (R_eq Tropfen / R_eq "
                                      "Einpolball bei Q_hi), max/min(2D, 3D) <= 1,3")
out["vermerke"].append("DR2 Kartenwortlaut: Duennwand-Geometrie gibt R_Tropfen/R_1 = 3^(1/D) (2D 1,732, 3D 1,442, "
                       "Verhaeltnis 1,201 < 1,3); das normierte R* ist weitgehend vorab ableitbar (PLAN 2).")

# ------------------------------------------------------------------ Bilder
FARBE = {"Tropfen": "C2", "verschmolzen": "C3", "offen": "C7"}
try:
    fig, axs = plt.subplots(1, 2, figsize=(15, 5.2))
    for j, dim in enumerate((3, 2)):
        t = tab[dim]
        ax = axs[j]
        if t is None:
            continue
        for z in t["zeilen"]:
            q = z["Q1"]
            ax.plot(q, z["start_minus_misch"], "^", color="k", ms=6)
            ax.plot(q, z["ende_minus_misch"], "o", color=FARBE.get(z["ausgang"], "C7"), ms=8,
                    mfc="none" if z["erzwungen"] else FARBE.get(z["ausgang"], "C7"))
            if z["tropfen_minus_misch"] is not None:
                ax.plot(q, z["tropfen_minus_misch"], "x", color="C0", ms=8)
            ax.plot(q, z["E_drei_getrennt"] - z["E_Misch"], "_", color="C1", ms=12)
        k = t["klammer"]
        if k and k["Q_lo"] is not None and k["Q_hi"] is not None:
            ax.axvspan(k["Q_lo"], k["Q_hi"], color="C2", alpha=0.15)
        ax.axhline(0.0, color="k", lw=0.6)
        ax.set_yscale("symlog", linthresh=0.1)
        ax.set_xlabel("Q1 (Ladung je Pol)")
        ax.set_ylabel("E - E_Mischball")
        ax.set_title("%dD, g4 = %+.1f: Dreieck schwarz, Ende (gruen Tropfen, rot verschmolzen), "
                     "Sektorlauf blau x, 3 E_1 orange" % (dim, t["g4"]), fontsize=8)
        ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "bisektion.png"), dpi=110)
    plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild Bisektion: %r" % ex)


def rgbbild(ax, arr, x, m, norm, titel):
    rgb = np.clip(np.stack([arr[0], arr[1], arr[2]], -1) / norm, 0, 1)[np.ix_(m, m)]
    ax.imshow(np.transpose(rgb, (1, 0, 2)), origin="lower", extent=[x[m][0], x[m][-1]] * 2)
    ax.set_title(titel, fontsize=8)


try:
    fig, axs = plt.subplots(2, 4, figsize=(15, 7.6), squeeze=False)
    for i, dim in enumerate((3, 2)):
        t = tab[dim]
        if t is None:
            continue
        z = np.load(os.path.join(D, "bisekt%d_bilder.npz" % dim))
        x = z["x"]
        m = np.abs(x) <= (14.0 if dim == 3 else 12.0)
        k = t["klammer"]
        zeilen = B[dim]["schritte"]
        wahl = []
        for Q in (k["Q_hi"], k["Q_lo"]):
            if Q is None:
                continue
            for s in zeilen:
                if abs(s["Q1"] - Q) < 1e-9:
                    wahl.append(s)
                    break
        j = 0
        for s in wahl:
            tag = s["tag"]
            norm = float(z["%s_start" % tag].max())
            rgbbild(axs[i, j], z["%s_ende" % tag], x, m, norm,
                    "%dD Q1 = %.4g: Ende vom Dreieck (%s)" % (dim, s["Q1"], s["ausgang"]))
            rgbbild(axs[i, j + 1], z["%s_sektor_ende" % tag], x, m, norm,
                    "%dD Q1 = %.4g: Ende vom Sektorstart (%s)" % (dim, s["Q1"], s["sektor"]["ausgang"]))
            j += 2
    fig.suptitle("Klammerenden der Bisektion (3D: Ebene z = 0): |phi_1|^2 rot, |phi_2|^2 gruen, |phi_3|^2 blau",
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "bisektion_bilder.png"), dpi=100)
    plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild Bisektion Felder: %r" % ex)

FARBE_ST = {"V1": "C0", "V2": "C1", "L1": "C2", "L2": "C3", "P1": "C4", "P2": "C5", "Z1": "C6", "R5": "C7",
            "R20": "C8"}
try:
    if S3 is not None and "stoerungen" in S3:
        fig, axs = plt.subplots(1, 3, figsize=(16, 4.6))
        for name, s in S3["stoerungen"].items():
            if "verlauf" not in s:
                continue
            v = np.array([[r[0], r[1], r[3], r[4]] for r in s["verlauf"]], float)
            ls = "--" if name in EXTRA else "-"
            axs[0].semilogy(v[:, 0], np.maximum(v[:, 3], 1e-12), ls, color=FARBE_ST.get(name), label=name)
            axs[1].semilogy(v[:, 0], np.maximum(v[:, 2], 1e-12), ls, color=FARBE_ST.get(name), label=name)
            axs[2].plot(v[:, 0], v[:, 1], ls, color=FARBE_ST.get(name), label=name)
        for ax in axs[:2]:
            ax.axhline(0.02, color="k", ls=":", lw=0.8)
        axs[2].axhline(0.0, color="k", lw=0.5)
        axs[2].set_yscale("symlog", linthresh=1e-6)
        axs[0].set_ylabel("d_rms / R (nach bester Verschiebung und Drehung)")
        axs[1].set_ylabel("d_form / R (max. Paarabstandsfehler)")
        axs[2].set_ylabel("E - E_Tropfen")
        for ax in axs:
            ax.set_xlabel("Flussschritt")
            ax.grid(alpha=0.3)
            ax.legend(fontsize=7)
        fig.suptitle("Teil B (3D, g4 = -0,1, Q1 = %g): Fluss bei festen Ladungen nach Stoerungen "
                     "(gestrichelt beschreibend)" % S3["Q1"])
        fig.tight_layout()
        fig.savefig(os.path.join(D, "stab3_fluss.png"), dpi=110)
        plt.close(fig)
        z = np.load(os.path.join(D, "stab3_bilder.npz"))
        x = z["x"]
        m = np.abs(x) <= 14.0
        namen = [n for n in ST6 + EXTRA if "%s_start" % n in z.files]
        fig, axs = plt.subplots(4, len(namen) + 1, figsize=(2.3 * (len(namen) + 1), 9.6), squeeze=False)
        norm = float(z["referenz"].max())
        norm_s = float(z["referenz_seite"].max())
        rgbbild(axs[0, 0], z["referenz"], x, m, norm, "Tropfen z = 0")
        rgbbild(axs[2, 0], z["referenz_seite"], x, m, norm_s, "Tropfen Seite (x, z)")
        axs[1, 0].axis("off")
        axs[3, 0].axis("off")
        for i, n in enumerate(namen):
            rgbbild(axs[0, i + 1], z["%s_start" % n], x, m, norm, n + " Start z = 0")
            rgbbild(axs[1, i + 1], z["%s_ende" % n], x, m, norm, n + " Ende z = 0")
            rgbbild(axs[2, i + 1], z["%s_start_seite" % n], x, m, norm_s, n + " Start Seite")
            rgbbild(axs[3, i + 1], z["%s_ende_seite" % n], x, m, norm_s, n + " Ende Seite")
        fig.suptitle("Teil B: |phi_1|^2 rot, |phi_2|^2 gruen, |phi_3|^2 blau; Seite = Projektion ueber y "
                     "(waagrecht x, senkrecht z)", fontsize=10)
        fig.tight_layout()
        fig.savefig(os.path.join(D, "stab3_bilder.png"), dpi=90)
        plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild Teil B: %r" % ex)

with open(os.path.join(D, "auswertung.json.tmp"), "w") as fh:
    json.dump(out, fh, indent=1)
os.replace(os.path.join(D, "auswertung.json.tmp"), os.path.join(D, "auswertung.json"))
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk in ("plan", "kartenwortlaut")}
                  for k, v in out["urteile"].items()}, indent=1))
