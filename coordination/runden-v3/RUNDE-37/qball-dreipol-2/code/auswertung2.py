#!/usr/bin/env python3
# QBALL-DREIPOL-2: Auswertung nach PLAN.md Abschnitt 6 (Urteile DP0 bis DP3 nach Plan und nach Kartenwortlaut),
# Tabellen und Bilder. Aufruf: auswertung2.py <laufordner>. Liest A.json, B_m01.json, B_p01.json, optional
# B_m01_fein.json, S.json, C_p01.json, C_m01.json (+ *_bilder.npz). Schreibt auswertung.json und PNG-Bilder.
import sys, os, json, math, hashlib, time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1]
# Bezugswerte aus QBALL-DREIPOL-1 (Karte; lauf-69/c_m01.json und a.json)
KARTE_D_R = 1.245
KARTE_LUECKE = 0.146
ST6 = ["V1", "V2", "L1", "L2", "P1", "P2"]


def lade(name):
    p = os.path.join(D, name)
    return json.load(open(p)) if os.path.exists(p) else None


def sha(name):
    p = os.path.join(D, name)
    return hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None


out = {"erstellt_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "ordner": D, "eingaben": {},
       "urteile": {}, "beschreibend": {}, "vermerke": []}
NAMEN = ["A.json", "B_m01.json", "B_p01.json", "B_m01_fein.json", "S.json", "C_p01.json", "C_m01.json"]
for n in NAMEN:
    out["eingaben"][n] = sha(n)
A = lade("A.json")
B = {"m01": lade("B_m01.json"), "p01": lade("B_p01.json")}
BF = lade("B_m01_fein.json")
S = lade("S.json")
C = {"p01": lade("C_p01.json"), "m01": lade("C_m01.json")}

# ------------------------------------------------------------------ DP0
dp0 = {}
teil2d = "nicht auswertbar"
if A is not None and "nachbau" in A and "mischball" in A:
    nb, mx = A["nachbau"], A["mischball"]
    R = A["ball"]["R_halb"]
    dR = nb["paarabstand_R"]
    luecke = mx["E"] - nb["E"]
    abw_d = max(abs(x / KARTE_D_R - 1.0) for x in dR)
    abw_l = abs(luecke / KARTE_LUECKE - 1.0)
    konv = nb["status"] == "konvergiert" and mx["status"] == "konvergiert"
    ok = abw_d <= 0.02 and abw_l <= 0.10
    teil2d = ("eingetroffen" if ok else "nicht eingetroffen") if konv else "nicht auswertbar"
    dp0["2d"] = dict(paarabstand_R=dR, max_rel_abw_paarabstand=abw_d, E_dreieck=nb["E"], E_mischball=mx["E"],
                     luecke=luecke, rel_abw_luecke=abw_l, nachbau_status=nb["status"], nachbau_it=nb["it"],
                     misch_status=mx["status"], urteil=teil2d,
                     E_ball=A["ball"]["E"], ball_abw_gitter_radial=A["ball"]["abw_gitter_radial"],
                     misch_abw_gitter_radial=mx["abw_gitter_radial"])
teil3d = []
for t in ("m01", "p01"):
    b = B[t]
    if b is None or "ball" not in b or "mischball" not in b:
        teil3d.append("nicht auswertbar")
        dp0["3d_" + t] = None
        continue
    ba, mx = b["ball"], b["mischball"]
    konv = (ba["status"] == "konvergiert" and mx["status"] == "konvergiert" and
            ba["radial"]["status"] == "konvergiert" and mx["radial"]["status"] == "konvergiert")
    abw = max(abs(ba["abw_gitter_radial"]), abs(mx["abw_gitter_radial"]))
    u = ("eingetroffen" if abw <= 1e-4 else "nicht eingetroffen") if konv else "nicht auswertbar"
    teil3d.append(u)
    dp0["3d_" + t] = dict(g4=b["g4"], N=b["N"], L=b["L"], h=b["h"], Q1=b["Q1"], E_ball=ba["E"],
                          E_ball_radial=ba["radial"]["E"], abw_ball=ba["abw_gitter_radial"], om_ball=ba["om"],
                          R_halb=ba["R_halb"], E_misch=mx["E"], E_misch_radial=mx["radial"]["E"],
                          abw_misch=mx["abw_gitter_radial"], status=[ba["status"], mx["status"]], urteil=u)
alle = [teil2d] + teil3d
if all(u == "eingetroffen" for u in alle):
    u0 = "eingetroffen"
elif any(u == "nicht eingetroffen" for u in alle):
    u0 = "nicht eingetroffen"
else:
    u0 = "nicht auswertbar"
out["urteile"]["DP0"] = dict(plan=u0, kartenwortlaut=u0, teile=dp0,
                             regel="2D: Paarabstand/R auf 2 % bei 1,245, Luecke zum Mischball auf 10 % bei 0,146; "
                                   "3D: |E_Gitter/E_radial - 1| <= 1e-4 fuer Einpol- und Mischball bei beiden g4")

# ------------------------------------------------------------------ DP1
dp1 = {}
if A is not None and "stoerungen" in A:
    Eref = A["referenz"]["E"]
    for name, s in A["stoerungen"].items():
        e = s["ende"]
        st = s["start"]
        konv = s["status"] == "konvergiert"
        zur = konv and e["d_form_R"] < 0.02 and e["d_rms_R"] < 0.02 and abs(e["dE"]) < 1e-3
        weg = (konv and not zur) or (e["dE"] < -1e-3) or ((not konv) and e["d_rms_R"] > st["d_rms_R"])
        plan = "zurueck" if zur else ("nicht zurueck" if weg else "offen")
        kw = "zurueck" if (e["d_rms_R"] < 0.02 and abs(e["dE"]) / abs(Eref) < 1e-3) else "nicht zurueck"
        dp1[name] = dict(text=s["text"], status=s["status"], it=s["it"], d_rms_start=st["d_rms_R"],
                         d_form_start=st["d_form_R"], dE_start=st["dE"], d_rms_ende=e["d_rms_R"],
                         d_form_ende=e["d_form_R"], dE_ende=e["dE"], reinheit_start=st["reinheit"],
                         reinheit_ende=e["reinheit"], res_ende=e["res"], plan=plan, kartenwortlaut=kw)
    sel = [dp1[n] for n in ST6 if n in dp1]
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
    out["urteile"]["DP1"] = dict(plan=up, kartenwortlaut=uk, je_stoerung=dp1, E_ref=Eref,
                                 referenz=A["referenz"],
                                 regel_plan="je Stoerung: Fluss konvergiert, d_form < 0,02 R, d_rms < 0,02 R, "
                                            "|E_Ende - E_ref| < 1e-3; alle sechs",
                                 regel_kw="je Stoerung am Flussende: d_rms < 0,02 R und |dE|/E_ref < 1e-3; alle sechs")
    out["vermerke"].append("DP1: P1 und P2 (gleichfoermiger Phasenversatz je Komponente) sind exakte Symmetrien von "
                           "E_Q (U(1)^3); ihre Rueckkehr war vorab ableitbar (PLAN 2.2).")
else:
    out["urteile"]["DP1"] = dict(plan="nicht auswertbar", kartenwortlaut="nicht auswertbar")


# ------------------------------------------------------------------ DP2
def gestalt(pa, R):
    if max(pa) < 0.25 * R:
        return "verschmolzen"
    if min(pa) > R:
        return "dreieck"
    return "zwischenform"


dp2 = {}
for t in ("m01", "p01"):
    b = B[t]
    if b is None or "fluss" not in b:
        dp2[t] = None
        continue
    R = b["ball"]["R_halb"]
    f = b["fluss"]
    e = f["ende"]
    g = gestalt(e["paarabstand"], R)
    rein = min(x for x in e["reinheit"])
    Emg = b["mischball"]["E"]
    Emr = b["mischball"]["radial"]["E"]
    dp2[t] = dict(g4=b["g4"], status=f["status"], it=f["it"], sek=f["sek"], res=e["res"], E_ende=e["E"],
                  E_drei_getrennt=b["E_drei_getrennt"], E_start=b["start"]["E"], E_misch_gitter=Emg,
                  E_misch_radial=Emr, E_ende_minus_misch_gitter=e["E"] - Emg, E_ende_minus_misch_radial=e["E"] - Emr,
                  paarabstand_R=e["paarabstand_R"], gestalt=g, reinheit=e["reinheit"], min_reinheit=rein, R_halb=R,
                  om=e["om"])
d = dp2.get("m01")
if d is None:
    up = uk = "nicht auswertbar"
else:
    konv = d["status"] == "konvergiert"
    if konv:
        ja = d["gestalt"] == "dreieck" and d["min_reinheit"] >= 0.5
        up = "eingetroffen" if (ja and d["E_ende"] < d["E_misch_gitter"] * (1 - 1e-6)) else "nicht eingetroffen"
        uk = "eingetroffen" if (ja and d["E_ende"] < d["E_misch_gitter"] and d["E_ende"] < d["E_misch_radial"]) \
            else "nicht eingetroffen"
    elif d["gestalt"] == "verschmolzen":
        up = uk = "nicht eingetroffen"
    else:
        up = uk = "nicht auswertbar"
out["urteile"]["DP2"] = dict(plan=up, kartenwortlaut=uk, je_g4=dp2,
                             regel_plan="g4 = -0,1: Fluss konvergiert, Gestalt Dreieck (min Paarabstand > R), "
                                        "Reinheit je Farbe >= 0,5, E_Ende < E_Misch(Gitter) (1 - 1e-6)",
                             regel_kw="wie Plan, E_Ende unter dem Gitter- und dem radialen 3D-Mischball")
if BF is not None and "fluss" in BF:
    e = BF["fluss"]["ende"]
    R = BF["ball"]["R_halb"]
    out["beschreibend"]["B_m01_fein"] = dict(N=BF["N"], h=BF["h"], status=BF["fluss"]["status"],
                                             it=BF["fluss"]["it"], E_ende=e["E"], paarabstand_R=e["paarabstand_R"],
                                             gestalt=gestalt(e["paarabstand"], R), reinheit=e["reinheit"],
                                             E_misch=BF.get("mischball", {}).get("E"), E_ball=BF["ball"]["E"])


# ------------------------------------------------------------------ DP3
def lauf_c(run, R):
    rec = np.array(run["reihe"])
    t = rec[:, 0]
    Q0 = rec[0, 2:5]
    frac = rec[:, 5:8] / Q0[None, :]
    ra = rec[:, 17:20]
    X, Y = rec[:, 8:11], rec[:, 11:14]
    paar = np.stack([np.hypot(X[:, i] - X[:, j], Y[:, i] - Y[:, j]) for i, j in ((0, 1), (0, 2), (1, 2))], 1)
    pm = paar.mean(1)
    gueltig = bool(run["status"] == "fertig" and t[-1] >= 300.0 - 1e-9 and run["dE_rel"] <= 1e-3 and
                   run["dQ_rel"] <= 1e-8)
    aus = bool(ra.max() > 4.0 * R)
    t_aus = float(t[np.nonzero(ra.max(1) > 4.0 * R)[0][0]]) if aus else None
    plan_ok = (not aus) and frac.min() >= 0.9
    kw_ok = (not aus) and frac[-1].min() >= 0.9
    # Pulsation: lokale Minima des mittleren Paarabstands (Mittendurchgaenge), Fenster +-5 Zeiteinheiten
    dtm = t[1] - t[0]
    w = max(1, int(round(5.0 / dtm)))
    mins = [i for i in range(w, len(pm) - w) if pm[i] == pm[i - w:i + w + 1].min() and pm[i] < pm.mean()]
    tm = [float(t[i]) for i in mins]
    per = float(np.mean(np.diff(tm))) if len(tm) >= 2 else None
    return dict(gueltig=gueltig, t_ende=float(t[-1]), dE_rel=run["dE_rel"], dQ_rel=run["dQ_rel"],
                ausstoss=aus, t_ausstoss=t_aus, max_r_R=float(ra.max() / R),
                min_anteil=float(frac.min()), anteil_t_ende=frac[-1].tolist(), min_anteil_t_ende=float(frac[-1].min()),
                beisammen_plan=bool(plan_ok), beisammen_kw=bool(kw_ok),
                paarabstand_R_t_ende=(paar[-1] / R).tolist(), mittendurchgaenge=tm, pulsationsdauer=per,
                min_mittlerer_paarabstand_R=float(pm.min() / R), max_mittlerer_paarabstand_R=float(pm.max() / R))


def urteil_dp3(laeufe, schluessel):
    n_ja = sum(1 for x in laeufe if x["gueltig"] and x[schluessel])
    n_nein = sum(1 for x in laeufe if x["gueltig"] and not x[schluessel])
    if len(laeufe) != 4:
        return "nicht auswertbar"
    if n_ja >= 3:
        return "eingetroffen"
    if n_nein >= 2:
        return "nicht eingetroffen"
    return "nicht auswertbar"


dp3 = {}
for t in ("p01", "m01"):
    c = C[t]
    if c is None:
        dp3[t] = None
        continue
    R = c["info"]["R"]
    laeufe = {k: lauf_c(v, R) for k, v in c["laeufe"].items()}
    lst = list(laeufe.values())
    e = dict(g4=c["g4"], R=R, R_K=c["info"]["R_K"], laeufe=laeufe, plan=urteil_dp3(lst, "beisammen_plan"),
             kartenwortlaut=urteil_dp3(lst, "beisammen_kw"))
    if S is not None and ("%g" % c["g4"]) in S["je_g4"]:
        s = S["je_g4"]["%g" % c["g4"]]
        e["schwellen"] = dict(E_start=s["E_start"], E_drei_getrennt=s["E_drei_getrennt"],
                              paare={k: dict(schwelle=v["schwelle"], start_minus_schwelle=v["start_minus_schwelle"])
                                     for k, v in s["paare"].items()},
                              ausstoss_energetisch_verboten=s["ausstoss_energetisch_verboten"],
                              zerfall_in_drei_verboten=s["zerfall_in_drei_verboten"])
        if s["ausstoss_energetisch_verboten"]:
            out["vermerke"].append("DP3 bei g4 = %g: Ausstoss (zwei verschmolzen, einer frei) ist energetisch "
                                   "verboten (E_start unter allen Schwellen); 'kein Ausstoss' war vorab ableitbar."
                                   % c["g4"])
    dp3[t] = e
hp = dp3.get("p01")
nb = dp3.get("m01")
up = hp["plan"] if hp else "nicht auswertbar"
if hp and nb:
    ks = [hp["kartenwortlaut"], nb["kartenwortlaut"]]
    uk = "eingetroffen" if all(k == "eingetroffen" for k in ks) else (
        "nicht eingetroffen" if any(k == "nicht eingetroffen" for k in ks) else "nicht auswertbar")
else:
    uk = "nicht auswertbar"
out["urteile"]["DP3"] = dict(plan=up, kartenwortlaut=uk, je_g4=dp3,
                             nebenurteil_plan_g4_m01=(nb["plan"] if nb else None),
                             regel_plan="g4 = +0,1 (Hauptwert): >= 3 von 4 gueltigen Saaten ohne Ausstoss (kein "
                                        "Polschwerpunkt > 4 R von der Mitte bis t = 300) und min_t,a Q_a,in/Q_a >= 0,9",
                             regel_kw="bei beiden g4: >= 3 von 4 Saaten ohne Ausstoss und Q_a,in/Q_a >= 0,9 bei t = 300")

# ------------------------------------------------------------------ Bilder
FARBE = {"V1": "C0", "V2": "C1", "L1": "C2", "L2": "C3", "P1": "C4", "P2": "C5", "L3": "C7"}
try:
    if A is not None and "stoerungen" in A:
        fig, axs = plt.subplots(1, 3, figsize=(16, 4.6))
        for name, s in A["stoerungen"].items():
            v = np.array([[r[0], r[1], r[3], r[4]] for r in s["verlauf"]], float)
            ls = "--" if name == "L3" else "-"
            axs[0].semilogy(v[:, 0], np.maximum(v[:, 3], 1e-12), ls, color=FARBE.get(name), label=name)
            axs[1].semilogy(v[:, 0], np.maximum(v[:, 2], 1e-12), ls, color=FARBE.get(name), label=name)
            axs[2].plot(v[:, 0], v[:, 1], ls, color=FARBE.get(name), label=name)
        for ax in axs[:2]:
            ax.axhline(0.02, color="k", ls=":", lw=0.8)
        axs[2].axhline(0.0, color="k", lw=0.5)
        axs[2].set_yscale("symlog", linthresh=1e-6)
        axs[0].set_ylabel("d_rms / R (nach bester Verschiebung und Drehung)")
        axs[1].set_ylabel("d_form / R (max. Paarabstandsfehler)")
        axs[2].set_ylabel("E - E_Dreieck")
        for ax in axs:
            ax.set_xlabel("Flussschritt")
            ax.grid(alpha=0.3)
            ax.legend(fontsize=7)
        fig.suptitle("Teil A (2D, g4 = -0,1): Fluss bei festen Ladungen nach sechs Stoerungen (L3 beschreibend)")
        fig.tight_layout()
        fig.savefig(os.path.join(D, "teilA_fluss.png"), dpi=110)
        plt.close(fig)
        z = np.load(os.path.join(D, "A_bilder.npz"))
        x = z["x"]
        m = np.abs(x) <= 10.0
        namen = [n for n in ST6 + ["L3"] if "%s_start" % n in z.files]
        fig, axs = plt.subplots(2, len(namen) + 1, figsize=(2.6 * (len(namen) + 1), 5.6), squeeze=False)
        norm = float(z["referenz"].max())
        for i, (lab, arr) in enumerate([("Dreieck", z["referenz"])] + [(n, z["%s_start" % n]) for n in namen]):
            rgb = np.clip(np.stack([arr[0], arr[1], arr[2]], -1) / norm, 0, 1)[np.ix_(m, m)]
            axs[0, i].imshow(np.transpose(rgb, (1, 0, 2)), origin="lower", extent=[x[m][0], x[m][-1]] * 2)
            axs[0, i].set_title(lab + (" Start" if i else ""), fontsize=9)
        axs[1, 0].axis("off")
        for i, n in enumerate(namen):
            arr = z["%s_ende" % n]
            rgb = np.clip(np.stack([arr[0], arr[1], arr[2]], -1) / norm, 0, 1)[np.ix_(m, m)]
            axs[1, i + 1].imshow(np.transpose(rgb, (1, 0, 2)), origin="lower", extent=[x[m][0], x[m][-1]] * 2)
            axs[1, i + 1].set_title(n + " Ende", fontsize=9)
        fig.suptitle("|phi_1|^2 rot, |phi_2|^2 gruen, |phi_3|^2 blau", fontsize=10)
        fig.tight_layout()
        fig.savefig(os.path.join(D, "teilA_bilder.png"), dpi=100)
        plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild Teil A: %r" % ex)

try:
    reihen = [(t, B[t]) for t in ("m01", "p01") if B[t] is not None and "fluss" in B[t]]
    if reihen:
        fig, axs = plt.subplots(len(reihen), 3, figsize=(14, 4.4 * len(reihen)), squeeze=False)
        for i, (t, b) in enumerate(reihen):
            z = np.load(os.path.join(D, "B_%s_bilder.npz" % t))
            x = z["x"]
            m = np.abs(x) <= 0.45 * b["L"]
            norm = float(z["start"].max())
            for j, k in enumerate(("start", "ende")):
                arr = z[k]
                rgb = np.clip(np.stack([arr[0], arr[1], arr[2]], -1) / norm, 0, 1)[np.ix_(m, m)]
                axs[i, j].imshow(np.transpose(rgb, (1, 0, 2)), origin="lower", extent=[x[m][0], x[m][-1]] * 2)
                axs[i, j].set_title("3D, g4 = %+.1f, Ebene z = 0, %s" % (b["g4"], k), fontsize=9)
            v = b["fluss"]["verlauf"]
            it = [r[0] for r in v]
            R = b["ball"]["R_halb"]
            for q in range(3):
                axs[i, 2].plot(it, [r[3][q] / R for r in v], label="Paar %d" % q)
            axs[i, 2].set_xlabel("Flussschritt")
            axs[i, 2].set_ylabel("Paarabstand / R_halb")
            axs[i, 2].grid(alpha=0.3)
            axs[i, 2].legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(os.path.join(D, "teilB_3d.png"), dpi=100)
        plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild Teil B: %r" % ex)

try:
    reihen = [(t, C[t]) for t in ("p01", "m01") if C[t] is not None]
    if reihen:
        fig, axs = plt.subplots(len(reihen), 3, figsize=(16, 4.2 * len(reihen)), squeeze=False)
        for i, (t, c) in enumerate(reihen):
            R = c["info"]["R"]
            for k, run in c["laeufe"].items():
                rec = np.array(run["reihe"])
                tt = rec[:, 0]
                X, Y = rec[:, 8:11], rec[:, 11:14]
                paar = np.stack([np.hypot(X[:, a] - X[:, b], Y[:, a] - Y[:, b]) for a, b in ((0, 1), (0, 2), (1, 2))],
                                1)
                axs[i, 0].plot(tt, rec[:, 17:20].max(1) / R, label=k)
                axs[i, 1].plot(tt, (rec[:, 5:8] / rec[0, 2:5][None, :]).min(1), label=k)
                axs[i, 2].plot(tt, paar.mean(1) / R, label=k)
            axs[i, 0].axhline(4.0, color="k", ls=":", lw=0.8)
            axs[i, 1].axhline(0.9, color="k", ls=":", lw=0.8)
            axs[i, 0].set_ylabel("max_a Abstand Pol - Mitte / R")
            axs[i, 1].set_ylabel("min_a Q_a,in / Q_a(0)")
            axs[i, 2].set_ylabel("mittlerer Paarabstand / R")
            for ax in axs[i]:
                ax.set_xlabel("t")
                ax.set_title("Teil C, g4 = %+.1f" % c["g4"], fontsize=9)
                ax.grid(alpha=0.3)
                ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(os.path.join(D, "teilC_dynamik.png"), dpi=100)
        plt.close(fig)
        fig, axs = plt.subplots(len(reihen), 4, figsize=(13, 3.4 * len(reihen)), squeeze=False)
        for i, (t, c) in enumerate(reihen):
            z = np.load(os.path.join(D, "C_%s_bilder.npz" % t))
            x = z["x"]
            m = np.abs(x) <= 20.0
            norm = float(z["s1_t0"].max())
            for j, ts in enumerate((0, 100, 200, 300)):
                k = "s1_t%g" % ts
                if k not in z.files:
                    continue
                arr = z[k]
                rgb = np.clip(np.stack([arr[0], arr[1], arr[2]], -1) / norm, 0, 1)[np.ix_(m, m)]
                axs[i, j].imshow(np.transpose(rgb, (1, 0, 2)), origin="lower", extent=[x[m][0], x[m][-1]] * 2)
                axs[i, j].set_title("g4 = %+.1f, Saat 1, t = %d" % (c["g4"], ts), fontsize=9)
        fig.tight_layout()
        fig.savefig(os.path.join(D, "teilC_bilder.png"), dpi=100)
        plt.close(fig)
except Exception as ex:
    out["vermerke"].append("Bild Teil C: %r" % ex)

with open(os.path.join(D, "auswertung.json.tmp"), "w") as fh:
    json.dump(out, fh, indent=1)
os.replace(os.path.join(D, "auswertung.json.tmp"), os.path.join(D, "auswertung.json"))
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk in ("plan", "kartenwortlaut")}
                  for k, v in out["urteile"].items()}, indent=1))
