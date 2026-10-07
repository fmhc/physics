# ZUFALLS-REIBUNG-1 (Runde 36): mechanische Auswertung nach PLAN.md (Urteile Z0 bis Z3, Proben, Bilder).
# Aufruf (nur ueber kleintest.sh): auswertung.py <laufordner> <ausgabe.json> [bilder: 1|0]
import sys, os, json, math, hashlib
import numpy as np
from scipy.interpolate import CubicSpline

VS = (0.1, 0.2, 0.3, 0.5)
SIGS = (0.01, 0.02, 0.04)
SAATEN_HAUPT = ("A", "B")
TAU = 10.0            # halbe Breite der Schnelle-Ausgleichsgerade (wie QBALL-GITTER-1)
BLOCK = 100.0         # Blocklaenge fuer den blockrobusten Standardfehler der Steigung (10 Bloecke je Fenster)
Z0_V = 1e-4
Z0_Q = 1e-8
Z1_V = 0.3
Z1_P = 2.0
Z1_TOL = 0.3
Z2_SIG = 0.04
Z2_FAKTOR = 10.0
Z3_FAKTOR = 3.0


def lade(ordner, name):
    pj = os.path.join(ordner, name + ".json"); pz = os.path.join(ordner, name + ".npz")
    if not (os.path.exists(pj) and os.path.exists(pz)):
        return None
    k = json.load(open(pj))
    if k.get("status") != "fertig":
        return None
    z = np.load(pz)
    d = {kk: np.asarray(z[kk]) for kk in z.files}
    d["kopf"] = k
    return d


def schnelle(t, X, tau=TAU):
    ds = float(t[1] - t[0]); m = int(round(tau / ds))
    j = np.arange(-m, m + 1, dtype=float); w = j / (ds * np.sum(j * j))
    v = np.full(len(X), np.nan)
    if len(X) > 2 * m:
        v[m:len(X) - m] = np.correlate(X, w, mode="valid")
    return v


def glatt_wie_v(t, V, tau=TAU):
    """Glaettung mit dem Kern, den die Schnelle-Ausgleichsgerade auf die Geschwindigkeit legt (Mittelpunkte,
    Gewichte (m(m+1) - i(i+1)), i = -m..m-1); so passen V und gamma(v) zeitlich zusammen."""
    ds = float(t[1] - t[0]); m = int(round(tau / ds))
    i = np.arange(-m, m, dtype=float)
    b = m * (m + 1) - i * (i + 1); b = b / b.sum()
    Vm = 0.5 * (V[1:] + V[:-1])            # Wert am Mittelpunkt l + 1/2
    out = np.full(len(V), np.nan)
    if len(V) > 2 * m:
        # out[k] = sum_i b_i Vm[k + i], i = -m..m-1
        c = np.correlate(Vm, b, mode="valid")   # c[q] = sum_j b_j Vm[q + j], j = 0..2m-1 -> k = q + m
        out[m:m + len(c)] = c
    return out


def steigung(t, y, block=BLOCK):
    """OLS-Steigung und blockrobuster Standardfehler (Bloecke der Laenge BLOCK als Cluster)."""
    tm = t.mean(); dtt = t - tm
    sxx = float(np.sum(dtt * dtt))
    b = float(np.sum(dtt * (y - y.mean())) / sxx)
    e = y - y.mean() - b * dtt
    nb = max(1, int(round((t[-1] - t[0]) / block)))
    grenzen = np.linspace(t[0], t[-1] + 1e-9, nb + 1)
    idx = np.searchsorted(grenzen, t, side="right") - 1
    s = np.zeros(nb)
    np.add.at(s, np.clip(idx, 0, nb - 1), dtt * e)
    se = float(math.sqrt(np.sum(s * s)) / sxx)
    return b, se


def mq_funktion(kopf):
    fam = sorted(kopf["familie"], key=lambda f: f["Q"])
    Q = np.array([f["Q"] for f in fam]); M = np.array([f["M"] for f in fam])
    return CubicSpline(Q, M), (float(Q[0]), float(Q[-1]))


def kenngroessen(d):
    k = d["kopf"]; t = d["t"]
    TA = k["T_A"]; TB = k["t_end"] - TAU
    v = schnelle(t, d["X"])
    sel = (t >= TA - 1e-9) & (t <= TB + 1e-9) & np.isfinite(v)
    r = dict(name=k["name"], v0=k["v"], sigma=k["sigma"], saat=k["saat"], dt=k["dt"], T_A=TA, T_B=float(t[sel][-1]),
             min_1_plus_sigma_eta=k["min_1_plus_sigma_eta"], wandzeit_s=k["wandzeit_s"])
    tt = t[sel]; vv = v[sel]
    Q0 = k["Q_ruhe"]; M0 = k["M_ruhe"]
    Mq, qb = mq_funktion(k)
    Qw = d["Qwin"][sel]; Ew = d["Ewin"][sel]; Pw = d["Pwin"][sel]
    Vs = glatt_wie_v(t, d["Vwin"])[sel]
    r["Q_bereich_familie"] = list(qb)
    r["Qwin_ausserhalb_familie"] = bool(np.any(Qw < qb[0]) or np.any(Qw > qb[1]))
    MQ = Mq(Qw)
    # Schnelle und Z0-Groessen
    va = float(vv[0])
    r["v_TA"] = va; r["v_mittel"] = float(np.mean(vv)); r["v_min"] = float(np.min(vv)); r["v_max"] = float(np.max(vv))
    r["v_ende"] = float(vv[-1])
    r["umkehr"] = bool(np.min(vv) <= 0.0)
    r["max_rel_dv"] = float(np.max(np.abs(vv - va)) / abs(va)) if va != 0 else float("inf")
    r["Q_TA"] = float(Qw[0]); r["Q_ende"] = float(Qw[-1])
    r["Q_verlust_max_rel"] = float((Qw[0] - np.min(Qw)) / Q0)
    r["Q_abw_max_rel"] = float(np.max(np.abs(Qw - Qw[0])) / Q0)
    # (A) direkt aus der Schnelle
    gv = 1.0 / np.sqrt(np.clip(1.0 - vv * vv, 1e-300, None))
    if not r["umkehr"]:
        yA = np.log(gv * vv)
        bA, seA = steigung(tt, yA)
        r["rA"] = -bA; r["seA"] = seA
    else:
        r["rA"] = None; r["seA"] = None
    # (B) Hauptmass: gamma aus der Schnelle plus Landschaftsenergie / M(Q)
    gc = gv + Vs / MQ
    r["gc_min"] = float(np.min(gc))
    if np.all(np.isfinite(gc)) and np.min(gc) > 1.0:
        yB = 0.5 * np.log(gc * gc - 1.0)
        bB, seB = steigung(tt, yB)
        r["rB"] = -bB; r["seB"] = seB
        Pc = MQ * np.sqrt(gc * gc - 1.0)
        bP, seP = steigung(tt, Pc)
        r["rP"] = -bP; r["seP"] = seP
        r["Pc_TA"] = float(Pc[0]); r["Pc_ende"] = float(Pc[-1])
        r["vc_TA"] = float(math.sqrt(1.0 - 1.0 / gc[0] ** 2)); r["vc_ende"] = float(math.sqrt(1.0 - 1.0 / gc[-1] ** 2))
    else:
        r["rB"] = r["seB"] = r["rP"] = r["seP"] = None
    # (C) Energie: gamma_E = E_win/M(Q_win)
    gE = Ew / MQ
    r["gE_min"] = float(np.min(gE))
    if np.min(gE) > 1.0:
        bC, seC = steigung(tt, 0.5 * np.log(gE * gE - 1.0))
        r["rC"] = -bC; r["seC"] = seC
    else:
        r["rC"] = r["seC"] = None
    # Ladung und Feldimpuls
    bQ, seQ = steigung(tt, Qw)
    r["rQ"] = -bQ; r["seQ"] = seQ; r["rQ_rel"] = -bQ / Q0
    bW, seW = steigung(tt, Pw)
    r["rPw"] = -bW; r["sePw"] = seW
    T = float(tt[-1] - tt[0]); r["T_mess"] = T
    r["dQ_rel_fenster"] = float(-bQ * T / Q0)
    # Bilanzen (ganzer Lauf)
    Hs = d["H"]; bil = Hs + d["Eabs"] + d["Edrop"] - Hs[0] - d["W"]
    qbil = d["Qdom"] + d["Qabs"] + d["Qdrop"] - d["Qdom"][0]
    r["bilanz_E_max_rel"] = float(np.max(np.abs(bil)) / M0); r["bilanz_Q_max_rel"] = float(np.max(np.abs(qbil)) / Q0)
    r["Start_E_rel_gM"] = float(k["E_start"] / k["Kontinuum_EP"][0] - 1.0)
    return r, dict(t=t, v=v, gc_t=None)


def name_von(v, s, saat=None, zus=""):
    if s == 0:
        return "v%g_s0%s" % (v, zus)
    return "v%g_s%g_%s%s" % (v, s, saat, zus)


def zellen_auswerten(K, ersatz=None):
    """K: name -> Kenngroessen. ersatz: dict name_haupt -> name_probe (Probenvariante)."""
    ersatz = ersatz or {}

    def hol(n):
        return K.get(ersatz.get(n, n))

    Z = {}
    for v in VS:
        k0 = hol(name_von(v, 0))
        g0 = {}
        for m, sm in (("rB", "seB"), ("rA", "seA"), ("rQ", "seQ"), ("rP", "seP"), ("rC", "seC")):
            if k0 is not None and k0.get(m) is not None:
                g0[m] = abs(k0[m]) + 2.0 * k0[sm]
            else:
                g0[m] = None
        Z[("%g" % v, "0")] = dict(G0=g0, lauf=None if k0 is None else k0["name"])
        for s in SIGS:
            ks = [hol(name_von(v, s, sa)) for sa in SAATEN_HAUPT]
            zelle = dict(laeufe=[None if kk is None else kk["name"] for kk in ks])
            for m, sm in (("rB", "seB"), ("rA", "seA"), ("rQ", "seQ"), ("rP", "seP"), ("rC", "seC")):
                werte = [kk.get(m) if kk is not None else None for kk in ks]
                ses = [kk.get(sm) if kk is not None else None for kk in ks]
                if any(kk is not None and kk["umkehr"] for kk in ks):
                    # Ball kehrt im Messfenster um (v <= 0): ln(gamma v) nicht definiert -> nicht messbar
                    zelle[m] = dict(status="gefangen", einzel=werte, se_einzel=ses)
                    continue
                if any(w is None for w in werte) or g0[m] is None:
                    zelle[m] = dict(status="fehlt", einzel=werte)
                    continue
                mw = float(np.mean(werte)); se = float(math.sqrt(sum(x * x for x in ses)) / len(ses))
                G = max(g0[m], 2.0 * se)
                gemessen = bool(mw > G)
                zelle[m] = dict(mittel=mw, se=se, grenze=G, G0=g0[m], gemessen=gemessen,
                                obergrenze=None if gemessen else max(mw, 0.0) + G, einzel=werte, se_einzel=ses)
            zelle["umkehr"] = [None if kk is None else kk["umkehr"] for kk in ks]
            zelle["v_mittel"] = [None if kk is None else kk["v_mittel"] for kk in ks]
            zelle["dQ_rel_fenster"] = [None if kk is None else kk["dQ_rel_fenster"] for kk in ks]
            Z[("%g" % v, "%g" % s)] = zelle
    return Z


def urteile(K, Z, ersatz=None, mass="rB"):
    ersatz = ersatz or {}
    U = {}
    # Z0
    w = {}; ok_all = True; fehlt = False
    for v in VS:
        k0 = K.get(ersatz.get(name_von(v, 0), name_von(v, 0)))
        if k0 is None:
            fehlt = True; continue
        w["v%g" % v] = dict(max_rel_dv=k0["max_rel_dv"], Q_verlust_max_rel=k0["Q_verlust_max_rel"],
                            Q_abw_max_rel=k0["Q_abw_max_rel"], v_TA=k0["v_TA"])
        if not (k0["max_rel_dv"] < Z0_V and k0["Q_verlust_max_rel"] < Z0_Q):
            ok_all = False
    if fehlt:
        U["Z0"] = dict(urteil="nicht auswertbar", vermerk="Kontrolllauf fehlt", werte=w)
    else:
        U["Z0"] = dict(urteil="eingetroffen" if ok_all else "nicht eingetroffen", werte=w)
    # Z1
    zs = [Z[("%g" % Z1_V, "%g" % s)][mass] for s in SIGS]
    w = {"sigma": list(SIGS), "r": [z.get("mittel") for z in zs], "se": [z.get("se") for z in zs],
         "grenze": [z.get("grenze") for z in zs], "gemessen": [z.get("gemessen") for z in zs]}
    if any(z.get("status") in ("fehlt", "gefangen") for z in zs):
        U["Z1"] = dict(urteil="nicht auswertbar", vermerk="Lauf fehlt oder Ball kehrt um (gefangen): " + ", ".join(str(z.get("status", "ok")) for z in zs), werte=w)
    elif all(z["gemessen"] for z in zs):
        ls = np.log(np.array(SIGS)); lr = np.log(np.array([z["mittel"] for z in zs]))
        p = float(np.polyfit(ls, lr, 1)[0])
        # Unsicherheit von p aus den se (lineare Fehlerfortpflanzung, nur beschreibend)
        A = np.vstack([ls, np.ones(3)]).T
        cov = np.linalg.inv(A.T @ A)
        sig_lr = np.array([z["se"] / z["mittel"] for z in zs])
        Jp = (cov @ A.T)[0]
        w["p"] = p; w["p_se"] = float(math.sqrt(np.sum((Jp * sig_lr) ** 2)))
        w["p_paare"] = [float(math.log(zs[1]["mittel"] / zs[0]["mittel"]) / math.log(2.0)),
                        float(math.log(zs[2]["mittel"] / zs[1]["mittel"]) / math.log(2.0))]
        U["Z1"] = dict(urteil="eingetroffen" if abs(p - Z1_P) <= Z1_TOL else "nicht eingetroffen", werte=w)
    else:
        verm = "nicht alle drei sigma ueber der Messgrenze"
        if zs[1]["gemessen"] and zs[2]["gemessen"]:
            w["p_zwei_punkte_002_004"] = float(math.log(zs[2]["mittel"] / zs[1]["mittel"]) / math.log(2.0))
        U["Z1"] = dict(urteil="nicht auswertbar", vermerk=verm, werte=w)
    # Z2
    z5 = Z[("0.5", "%g" % Z2_SIG)][mass]; z1 = Z[("0.1", "%g" % Z2_SIG)][mass]
    w = dict(r_v05=z5.get("mittel"), se_v05=z5.get("se"), grenze_v05=z5.get("grenze"), gemessen_v05=z5.get("gemessen"),
             obergrenze_v05=z5.get("obergrenze"), r_v01=z1.get("mittel"), se_v01=z1.get("se"),
             grenze_v01=z1.get("grenze"), gemessen_v01=z1.get("gemessen"), obergrenze_v01=z1.get("obergrenze"),
             umkehr_v01=Z[("0.1", "%g" % Z2_SIG)]["umkehr"])
    if z5.get("status") in ("fehlt", "gefangen") or z1.get("status") in ("fehlt", "gefangen"):
        U["Z2"] = dict(urteil="nicht auswertbar", vermerk="Lauf fehlt oder Ball kehrt im Messfenster um (gefangen): " + "v = 0,5: %s, v = 0,1: %s" % (z5.get("status", "ok"), z1.get("status", "ok")), werte=w)
    elif z5["gemessen"] and z1["gemessen"]:
        q = z5["mittel"] / z1["mittel"]; w["verhaeltnis"] = q
        U["Z2"] = dict(urteil="eingetroffen" if q >= Z2_FAKTOR else "nicht eingetroffen", werte=w)
    elif z5["gemessen"] and not z1["gemessen"]:
        q = z5["mittel"] / z1["obergrenze"]; w["verhaeltnis_mindestens"] = q
        if q >= Z2_FAKTOR:
            U["Z2"] = dict(urteil="eingetroffen", vermerk="v = 0,1 unter der Messgrenze; Verhaeltnis >= r(0,5)/Obergrenze(0,1)",
                           werte=w)
        else:
            U["Z2"] = dict(urteil="nicht auswertbar", vermerk="v = 0,1 unter der Messgrenze, Obergrenze zu hoch", werte=w)
    elif (not z5["gemessen"]) and z1["gemessen"]:
        q = z5["obergrenze"] / z1["mittel"]; w["verhaeltnis_hoechstens"] = q
        if q < Z2_FAKTOR:
            U["Z2"] = dict(urteil="nicht eingetroffen", vermerk="v = 0,5 unter der Messgrenze", werte=w)
        else:
            U["Z2"] = dict(urteil="nicht auswertbar", vermerk="v = 0,5 unter der Messgrenze", werte=w)
    else:
        U["Z2"] = dict(urteil="nicht auswertbar", vermerk="beide unter der Messgrenze", werte=w)
    # Z3
    zel = []; ausgeschl = []
    for v in VS:
        for s in SIGS:
            zz = Z[("%g" % v, "%g" % s)]
            zq = zz["rQ"]; zp = zz["rP" if mass == "rB" else "rP"]
            if zq.get("status") in ("fehlt", "gefangen") or zp.get("status") in ("fehlt", "gefangen"):
                ausgeschl.append(dict(v=v, sigma=s, grund="fehlt")); continue
            if zq["gemessen"] and zp["gemessen"]:
                zel.append(dict(v=v, sigma=s, dQ_durch_dP=zq["mittel"] / zp["mittel"], rQ=zq["mittel"], rP=zp["mittel"]))
            else:
                ausgeschl.append(dict(v=v, sigma=s, grund="unter Messgrenze", rQ_gemessen=zq["gemessen"],
                                      rP_gemessen=zp["gemessen"], rQ=zq["mittel"], rP=zp["mittel"]))
    w = dict(zellen=zel, ausgeschlossen=ausgeschl)
    vs_ok = sorted(set(z["v"] for z in zel)); ss_ok = sorted(set(z["sigma"] for z in zel))
    if len(vs_ok) >= 2 and len(ss_ok) >= 2:
        rr = [z["dQ_durch_dP"] for z in zel]
        f = max(rr) / min(rr); w["max_durch_min"] = f
        U["Z3"] = dict(urteil="eingetroffen" if f <= Z3_FAKTOR else "nicht eingetroffen", werte=w)
    else:
        U["Z3"] = dict(urteil="nicht auswertbar", vermerk="zu wenige Zellen mit gemessenem Ladungs- und Impulsverlust",
                       werte=w)
    return U


def bilder(ordner, K, D, Z):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    farben = {0: "k", 0.01: "tab:blue", 0.02: "tab:orange", 0.04: "tab:red"}
    for feld, datei, ylab in (("v", "v_t.png", "Schnelle v(t) (Ladungsschwerpunkt)"),
                              ("vc", "vc_t.png", "v_c(t) aus gamma_c = gamma_v + V/M(Q)"),
                              ("q", "ladung_t.png", "Q_win(t)/Q_win(T_A)")):
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        for ax, v in zip(axs.flat, VS):
            for s in (0,) + SIGS:
                for sa, ls in (("A", "-"), ("B", "--")):
                    n = name_von(v, s, sa)
                    if s == 0 and sa == "B":
                        continue
                    if n not in D:
                        continue
                    dd = D[n]
                    y = dd[feld]
                    ax.plot(dd["t"], y, ls, color=farben[s], lw=0.8,
                            label=("sigma=%g" % s) + ("" if s == 0 else " Saat " + sa))
            ax.set_title("v0 = %g" % v); ax.set_xlabel("t"); ax.set_ylabel(ylab, fontsize=8)
            ax.axvline(250.0, color="0.6", lw=0.5)
            ax.legend(fontsize=6)
        fig.tight_layout(); fig.savefig(os.path.join(ordner, datei), dpi=110); plt.close(fig)
    # Reibungsrate gegen sigma
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    ax = axs[0]
    for v, fb in zip(VS, ("tab:blue", "tab:green", "tab:orange", "tab:red")):
        xs = []; ys = []
        for s in SIGS:
            z = Z[("%g" % v, "%g" % s)]["rB"]
            if z.get("status") in ("fehlt", "gefangen"):
                continue
            if z["gemessen"]:
                ax.errorbar([s], [z["mittel"]], yerr=[z["se"]], fmt="o", color=fb)
                xs.append(s); ys.append(z["mittel"])
            else:
                ax.plot([s], [z["obergrenze"]], "v", color=fb, mfc="none")
        if xs:
            ax.plot(xs, ys, "-", color=fb, label="v0 = %g" % v)
    ss = np.array([0.008, 0.05])
    ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlabel("sigma"); ax.set_ylabel("Reibungsrate r_B = -d ln(gamma v)/dt")
    ax.set_title("Reibung gegen Unordnung (offen: Obergrenze)"); ax.legend(fontsize=8)
    yl = ax.get_ylim()
    for c in (1e-3, 1e-2, 1e-1, 1.0):
        ax.plot(ss, c * ss ** 2, ":", color="0.7", lw=0.6)
    ax.set_ylim(yl)
    ax = axs[1]
    for s in SIGS:
        xs = []; ys = []
        for v in VS:
            z = Z[("%g" % v, "%g" % s)]["rB"]
            if z.get("status") in ("fehlt", "gefangen"):
                continue
            if z["gemessen"]:
                ax.errorbar([v], [z["mittel"]], yerr=[z["se"]], fmt="o", color=farben[s])
                xs.append(v); ys.append(z["mittel"])
            else:
                ax.plot([v], [z["obergrenze"]], "v", color=farben[s], mfc="none")
        if xs:
            ax.plot(xs, ys, "-", color=farben[s], label="sigma = %g" % s)
    ax.set_yscale("log"); ax.set_xlabel("Startschnelle v0"); ax.set_ylabel("Reibungsrate r_B")
    ax.set_title("Reibung gegen Schnelle (offen: Obergrenze)"); ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(ordner, "reibung_sigma_v.png"), dpi=110); plt.close(fig)


def main():
    ordner = sys.argv[1]; aus = sys.argv[2]
    mit_bildern = (len(sys.argv) <= 3) or sys.argv[3] == "1"
    namen = sorted(f[:-5] for f in os.listdir(ordner) if f.endswith(".json") and f[:1] == "v" and
                   os.path.exists(os.path.join(ordner, f[:-5] + ".npz")))
    K = {}; D = {}; nicht_fertig = []
    for n in namen:
        d = lade(ordner, n)
        if d is None:
            nicht_fertig.append(n); continue
        r, _ = kenngroessen(d)
        K[n] = r
        t = d["t"]; v = schnelle(t, d["X"])
        k = d["kopf"]; Mq, _ = mq_funktion(k)
        Vs = glatt_wie_v(t, d["Vwin"])
        gv = 1.0 / np.sqrt(np.clip(1.0 - v * v, 1e-300, None))
        gc = gv + Vs / Mq(d["Qwin"])
        vc = np.sqrt(np.clip(1.0 - 1.0 / gc ** 2, 0, None))
        D[n] = dict(t=t, v=v, vc=vc, q=d["Qwin"] / d["Qwin"][int(round(k["T_A"] / k["ds_mess"]))])
    Z = zellen_auswerten(K)
    U = urteile(K, Z)
    # Gegenprobe (A): direkte Schnelle (ohne Landschaftsenergie), nur beschreibend
    ZA = zellen_auswerten(K)
    UA = {}
    try:
        UA = urteile(K, ZA, mass="rA")
    except Exception as ex:
        UA = dict(fehler=str(ex))
    UC = {}
    try:
        UC = urteile(K, ZA, mass="rC")
    except Exception as ex:
        UC = dict(fehler=str(ex))
    # Proben
    proben = {}
    e_dt = {}
    for n in K:
        if n.endswith("_dt2"):
            e_dt[n[:-4]] = n
    if e_dt:
        Zd = zellen_auswerten(K, e_dt)
        Ud = urteile(K, Zd, e_dt)
        proben["dt_halb"] = dict(ersatz=e_dt, urteile={kk: vv["urteil"] for kk, vv in Ud.items()},
                                 werte={kk: vv.get("werte") for kk, vv in Ud.items()},
                                 vergleich={n: {m: (K[e_dt[n]].get(m), K[n].get(m) if n in K else None)
                                                for m in ("rB", "rA", "rQ", "rP", "max_rel_dv", "Q_verlust_max_rel")}
                                            for n in e_dt})
    e_c = {}
    for n in K:
        if n.endswith("_C"):
            e_c[n[:-2] + "_B"] = n
    if e_c:
        Zc = zellen_auswerten(K, e_c)
        Uc = urteile(K, Zc, e_c)
        proben["saat_C_statt_B"] = dict(ersatz=e_c, urteile={kk: vv["urteil"] for kk, vv in Uc.items()},
                                        werte={kk: vv.get("werte") for kk, vv in Uc.items()},
                                        einzel={n: {m: K[n].get(m) for m in ("rB", "seB", "rQ_rel", "rP", "umkehr",
                                                                             "v_mittel")} for n in e_c.values()})
    robust = {}
    for zz in U:
        abw = [pn for pn, pr in proben.items() if pr["urteile"].get(zz) != U[zz]["urteil"]]
        robust[zz] = "robust" if not abw else "nicht robust (" + ", ".join(abw) + ")"
        if abw:
            U[zz]["vermerk"] = (U[zz].get("vermerk", "") + "; " if U[zz].get("vermerk") else "") + \
                "nicht robust: Probe(n) " + ", ".join(abw) + " geben ein anderes Urteil"
    zellen_json = {"v%s_s%s" % kk: vv for kk, vv in Z.items()}
    erg = dict(urteile=U, robustheit=robust, gegenprobe_A_direkt=UA, gegenprobe_C_energie=UC, proben=proben,
               zellen=zellen_json, laeufe=K, nicht_fertig=nicht_fertig,
               skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest())
    json.dump(erg, open(aus, "w"), indent=1, default=lambda o: o if not isinstance(o, np.generic) else o.item())
    if mit_bildern:
        try:
            bilder(ordner, K, D, Z)
        except Exception as ex:
            print("Bilder-Fehler:", ex)
    print(json.dumps({kk: (vv["urteil"], vv.get("vermerk", "")) for kk, vv in U.items()}, ensure_ascii=False))
    print("robust:", json.dumps(robust, ensure_ascii=False))
    print("nicht fertig:", nicht_fertig)


if __name__ == "__main__":
    main()
