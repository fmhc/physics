# QBALL-GITTER-1 (Runde 35): mechanische Auswertung nach PLAN.md (Urteile G0 bis G4, Kontrollen, Bilder).
# Aufruf (nur ueber kleintest.sh): auswertung.py <laufordner> <ausgabe.json>
import sys, os, json, math
import numpy as np

KINK = {0.5: 1.78, 0.25: 2.61, 0.125: 3.86}   # gamma_max des Kinks aus NETZ-C-1 (Karte)
HS = (0.5, 0.25, 0.125)
TAU = 10.0        # halbe Fensterbreite der Schnelle (Ausgleichsgerade ueber [t - TAU, t + TAU])
TAU2 = 20.0       # Kontrollfenster
T_G1_START = 20.0
G1_TOL = 0.02
G0_DRIFT = 1e-4; G0_Q = 1e-10; G0_E = 1e-7; G0_T = 500.0
SATT_ANTEIL = 0.05   # Saettigung: Steigung von gamma im letzten Viertel <= 0,05 a0
FALL_ANTEIL = 0.05   # oder gamma am Ende <= gamma_max - 0,05 (gamma_max - 1)
G3_QANTEIL = 0.5


def lade(ordner, name):
    pj = os.path.join(ordner, name + ".json"); pz = os.path.join(ordner, name + ".npz")
    if not (os.path.exists(pj) and os.path.exists(pz)):
        return None
    kopf = json.load(open(pj))
    if kopf.get("status") == "unterbrochen":
        return None
    z = np.load(pz)
    d = {k: np.asarray(z[k]) for k in z.files}
    d["kopf"] = kopf
    return d


def schnelle(t, X, tau):
    ds = float(t[1] - t[0])
    m = int(round(tau / ds))
    j = np.arange(-m, m + 1, dtype=float)
    w = j / (ds * np.sum(j * j))
    v = np.full(len(X), np.nan)
    if len(X) > 2 * m:
        v[m:len(X) - m] = np.correlate(X, w, mode="valid")
    return v


def gamma_aus_v(v):
    g = np.full(len(v), np.nan)
    ok = np.isfinite(v)
    sub = np.abs(v[ok]) < 1.0
    gg = np.full(int(ok.sum()), np.inf)
    gg[sub] = 1.0 / np.sqrt(1.0 - v[ok][sub] ** 2)
    g[ok] = gg
    return g


def kenngroessen(d, tau=TAU, xfeld="X"):
    k = d["kopf"]; t = d["t"]; X = d[xfeld]
    v = schnelle(t, X, tau); g = gamma_aus_v(v)
    ok = np.isfinite(g)
    r = dict(name=k["name"], h=k["h"], a0=k["a0"], E=k["E"], M0=k["M0"], Q0=k["Q0"], TB=k["TB"], status=k["status"],
             t_letzt=k["t_letzt"], dt=k["dt"], L_w=k["L_w"], abschnitte=k["abschnitte"])
    if not ok.any():
        r["gueltig"] = False
        return r, v, g
    r["gueltig"] = True
    iv = np.nonzero(ok)[0]
    r["v_ueber_1"] = bool(np.any(np.abs(v[ok]) >= 1.0))
    im = iv[np.argmax(g[iv])]
    r["gamma_max"] = float(g[im]); r["t_max"] = float(t[im]); r["v_max"] = float(v[im])
    r["Qwin_bei_tmax"] = float(d["Qwin"][im] / k["Q0"])
    # gamma_max solange Q_win >= 0,5 Q0 (Nebenwert)
    sel = iv[d["Qwin"][iv] >= 0.5 * k["Q0"]]
    r["gamma_max_Q50"] = float(np.max(g[sel])) if len(sel) else None
    # Saettigung / Abfall
    il = iv[-1]
    r["t_letzt_v"] = float(t[il]); r["gamma_ende"] = float(g[il]); r["v_ende"] = float(v[il])
    viertel = iv[iv >= iv[0] + int(0.75 * (iv[-1] - iv[0]))]
    if len(viertel) >= 3 and np.all(np.isfinite(g[viertel])):
        steig = float(np.polyfit(t[viertel], g[viertel], 1)[0])
    else:
        steig = float("nan")
    r["steigung_letztes_viertel"] = steig
    a0 = k["a0"]
    gefallen = bool(np.isfinite(r["gamma_max"]) and (r["gamma_max"] - r["gamma_ende"]) >= FALL_ANTEIL * (r["gamma_max"] - 1.0))
    gesaettigt = bool(np.isfinite(steig) and steig <= SATT_ANTEIL * a0)
    r["gefallen"] = gefallen; r["gesaettigt"] = gesaettigt
    r["max_erreicht"] = bool(gefallen or gesaettigt or k["status"] == "zerfallen")
    # Umkehr nach t_max
    nach = iv[iv > im]
    neg = nach[v[nach] < 0.0]
    if len(neg):
        i1 = neg[0]; i0 = i1 - 1
        if np.isfinite(v[i0]) and v[i0] > 0:
            tu = float(t[i0] + (t[i1] - t[i0]) * v[i0] / (v[i0] - v[i1]))
        else:
            tu = float(t[i1])
        r["t_umkehr"] = tu; r["Qwin_bei_umkehr"] = float(np.interp(tu, t, d["Qwin"]) / k["Q0"])
    else:
        r["t_umkehr"] = None; r["Qwin_bei_umkehr"] = None
    r["v_min_nach_tmax"] = float(np.min(v[nach])) if len(nach) else None
    # Ladung
    q = d["Qwin"] / k["Q0"]
    r["Qwin_ende"] = float(q[-1]); r["Qwin_min"] = float(np.min(q))
    r["Qwin_bei_TB_halb"] = float(np.interp(k["TB"] / 2, t, q)) if np.isfinite(k["TB"]) and t[-1] >= k["TB"] / 2 else None
    r["Qwin_bei_TB"] = float(np.interp(k["TB"], t, q)) if np.isfinite(k["TB"]) and t[-1] >= k["TB"] else None
    below = np.nonzero(q < 0.5)[0]
    r["t_Q_unter_halb"] = float(t[below[0]]) if len(below) else None
    # Abstrahlung und Bilanzen
    H = d["H"]; M0 = k["M0"]; Q0 = k["Q0"]
    bil = H + d["Eabs"] + d["Edrop"] - H[0] - d["W"]
    qb = d["Qdom"] + d["Qabs"] + d["Qdrop"] - d["Qdom"][0]
    r["bilanz_E_max_rel"] = float(np.max(np.abs(bil)) / M0)
    r["bilanz_Q_max_rel"] = float(np.max(np.abs(qb)) / Q0)
    Etot = H + d["Eabs"] + d["Edrop"]
    r["E_aussen_ende"] = float(Etot[-1] - d["Ewin"][-1])
    r["Q_aussen_ende"] = float(Q0 - d["Qwin"][-1])
    r["W_ende"] = float(d["W"][-1]); r["Ewin_ende"] = float(d["Ewin"][-1])
    r["Eabs_ende"] = float(d["Eabs"][-1]); r["Edrop_ende"] = float(d["Edrop"][-1])
    r["Qabs_ende"] = float(d["Qabs"][-1]); r["Qdrop_ende"] = float(d["Qdrop"][-1])
    r["weg"] = float(X[-1] - X[0])
    return r, v, g


def urteil(u, vermerk=None, werte=None):
    o = {"urteil": u}
    if vermerk:
        o["vermerk"] = vermerk
    o["werte"] = werte or {}
    return o


def g0_pruefen(laeufe):
    werte = {}; alle = True; fehlt = False
    for h in HS:
        d = laeufe.get("g0_h%s" % h)
        if d is None:
            fehlt = True; continue
        k = d["kopf"]; t = d["t"]; sel = t <= G0_T + 1e-9
        drift = float(np.max(np.abs(d["X"][sel] - d["X"][0])))
        dq = float(np.max(np.abs(d["Qdom"][sel] - d["Qdom"][0])) / abs(d["Qdom"][0]))
        dE = float(np.max(np.abs(d["H"][sel] - d["H"][0])) / abs(d["H"][0]))
        amp = d["amax"][sel]
        ok = drift < G0_DRIFT and dq <= G0_Q and dE <= G0_E and t[sel][-1] >= G0_T - 1e-9
        werte["h%s" % h] = dict(drift=drift, ladung_rel=dq, energie_rel=dE, t_bis=float(t[sel][-1]),
                               amax_schwankung_rel=float((amp.max() - amp.min()) / amp[0]), M0=k["M0"], Q0=k["Q0"],
                               newton_rest=k["newton"]["newton_rest"], phi0=k["newton"]["phi0"], erfuellt=bool(ok))
        alle = alle and ok
    if fehlt:
        return urteil("nicht auswertbar", "G0-Lauf fehlt", werte)
    return urteil("eingetroffen" if alle else "nicht eingetroffen", None, werte)


def g1_pruefen(d):
    if d is None:
        return urteil("nicht auswertbar", "Lauf fehlt")
    k = d["kopf"]; t = d["t"]
    v = schnelle(t, d["X"], TAU); g = gamma_aus_v(v)
    ok = np.isfinite(g)
    i15 = np.nonzero(ok & (g >= 1.5))[0]
    w = dict(M0=k["M0"], Q0=k["Q0"], E=k["E"])
    sel_all = ok & (t >= T_G1_START)
    if not len(i15):
        w["gamma_max"] = float(np.nanmax(g)) if ok.any() else None
        return urteil("nicht eingetroffen", "gamma erreicht 1,5 nicht", w)
    t15 = float(t[i15[0]])
    sel = sel_all & (t <= t15)
    soll = k["Q0"] * k["E"] * t[sel]
    dev = g[sel] * k["M0"] * v[sel] / soll - 1.0
    vE = schnelle(t, d["XE"], TAU); gE = gamma_aus_v(vE)
    devE = gE[sel] * k["M0"] * vE[sel] / soll - 1.0
    devP = d["P"][sel] / soll - 1.0
    imax = int(np.argmax(np.abs(dev)))
    w.update(t_gamma_1_5=t15, max_abs_abweichung=float(np.max(np.abs(dev))), bei_t=float(t[sel][imax]),
             abweichung_bei_t15=float(dev[-1]), abweichung_t50=float(np.interp(50.0, t[sel], dev)),
             abweichung_t100=float(np.interp(100.0, t[sel], dev)),
             kontrolle_energieschwerpunkt_max_abs=float(np.nanmax(np.abs(devE))),
             kontrolle_impuls_P_max_abs=float(np.nanmax(np.abs(devP))),
             Qwin_bei_t15=float(np.interp(t15, t, d["Qwin"]) / k["Q0"]),
             kontinuum_t_gamma_1_5=float(math.sqrt(1.25) / k["a0"]))
    eingetr = w["max_abs_abweichung"] <= G1_TOL
    return urteil("eingetroffen" if eingetr else "nicht eingetroffen", None, w)


def g2_pruefen(kg):
    w = {}
    for h in HS:
        r = kg.get(h)
        if r is None or not r.get("gueltig"):
            return urteil("nicht auswertbar", "Hauptlauf h = %s fehlt" % h, w)
        w["h%s" % h] = dict(gamma_max=r["gamma_max"], t_max=r["t_max"], max_erreicht=r["max_erreicht"],
                            gefallen=r["gefallen"], gesaettigt=r["gesaettigt"],
                            steigung_letztes_viertel=r["steigung_letztes_viertel"], gamma_ende=r["gamma_ende"],
                            v_ueber_1=r["v_ueber_1"])
    if any(kg[h]["v_ueber_1"] for h in HS):
        return urteil("nicht auswertbar", "Schnelle >= 1 gemessen", w)
    gm = [kg[h]["gamma_max"] for h in HS]
    alle_max = all(kg[h]["max_erreicht"] for h in HS)
    steigend = gm[0] < gm[1] < gm[2]
    faktor = gm[2] / gm[0]
    w.update(alle_maximum=alle_max, steigend_mit_1_durch_h=steigend, faktor_0125_zu_05=faktor)
    ok = alle_max and steigend and faktor >= 1.5
    return urteil("eingetroffen" if ok else "nicht eingetroffen", None, w)


def g3_einzeln(r):
    if r is None or not r.get("gueltig"):
        return "offen", "Lauf fehlt"
    TB = r["TB"]
    if r["t_umkehr"] is not None:
        if r["t_umkehr"] < TB and r["Qwin_bei_umkehr"] >= G3_QANTEIL:
            return "ja", "Umkehr bei t = %.1f, Q_win = %.3f Q0" % (r["t_umkehr"], r["Qwin_bei_umkehr"])
        return "nein", "Umkehr bei t = %.1f (T_B = %.1f), Q_win = %.3f Q0" % (r["t_umkehr"], TB, r["Qwin_bei_umkehr"])
    if r["status"] == "zerfallen":
        return "nein", "Ball zerfallen vor einer Umkehr (t = %.1f)" % r["t_letzt"]
    if r["t_letzt_v"] >= TB:
        return "nein", "keine Umkehr bis T_B = %.1f" % TB
    return "offen", "Lauf endet vor T_B ohne Umkehr"


def g3_pruefen(kg):
    w = {}; res = []
    for h in HS:
        e, txt = g3_einzeln(kg.get(h))
        r = kg.get(h) or {}
        w["h%s" % h] = dict(ergebnis=e, text=txt, t_umkehr=r.get("t_umkehr"), Qwin_bei_umkehr=r.get("Qwin_bei_umkehr"),
                            TB=r.get("TB"), t_max=r.get("t_max"), v_min_nach_tmax=r.get("v_min_nach_tmax"))
        res.append(e)
    if all(x == "ja" for x in res):
        return urteil("eingetroffen", None, w)
    if any(x == "nein" for x in res):
        return urteil("nicht eingetroffen", None, w)
    return urteil("nicht auswertbar", "mindestens ein Lauf offen", w)


def g4_pruefen(kg):
    w = {}
    for h in HS:
        r = kg.get(h)
        if r is None or not r.get("gueltig"):
            return urteil("nicht auswertbar", "Hauptlauf h = %s fehlt" % h, w)
        w["h%s" % h] = dict(gamma_max_qball=r["gamma_max"], gamma_max_kink=KINK[h], erfuellt=bool(r["gamma_max"] >= KINK[h]))
    if any(kg[h]["v_ueber_1"] for h in HS):
        return urteil("nicht auswertbar", "Schnelle >= 1 gemessen", w)
    ok = all(w["h%s" % h]["erfuellt"] for h in HS)
    return urteil("eingetroffen" if ok else "nicht eingetroffen", None, w)


def bilder(ordner, laeufe, kgv):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:
        return "keine Bilder: %s" % e
    farben = {0.5: "#1f77b4", 0.25: "#d62728", 0.125: "#2ca02c"}
    fig1, ax1 = plt.subplots(2, 1, figsize=(9, 8), sharex=False)
    fig2, ax2 = plt.subplots(2, 1, figsize=(9, 8), sharex=False)
    fig3, ax3 = plt.subplots(2, 1, figsize=(9, 8), sharex=False)
    for j, (pref, a0) in enumerate((("f1", 0.005), ("f2", 0.01))):
        tmax_plot = 0.0
        for h in HS:
            d = laeufe.get("%s_h%s_dt1" % (pref, h))
            if d is None:
                continue
            t = d["t"]; v, g = kgv[(pref, h)]
            TB = d["kopf"]["TB"]; tmax_plot = max(tmax_plot, t[-1])
            ax1[j].plot(t, v, color=farben[h], lw=1, label="h = %s (T_B = %.0f)" % (h, TB))
            ax2[j].plot(t, g, color=farben[h], lw=1, label="h = %s" % h)
            ax3[j].plot(t, d["Qwin"] / d["kopf"]["Q0"], color=farben[h], lw=1, label="h = %s" % h)
            for ax in (ax1[j], ax2[j], ax3[j]):
                ax.axvline(TB, color=farben[h], ls=":", lw=0.8)
                ax.axvline(TB / 2, color=farben[h], ls="--", lw=0.5)
        tt = np.linspace(0, max(tmax_plot, 1.0), 2000)
        ax1[j].plot(tt, a0 * tt / np.sqrt(1 + (a0 * tt) ** 2), color="k", lw=0.8, ls="--", label="Kontinuum")
        ax2[j].plot(tt, np.sqrt(1 + (a0 * tt) ** 2), color="k", lw=0.8, ls="--", label="Kontinuum")
        for h in HS:
            ax2[j].axhline(KINK[h], color=farben[h], lw=0.6, ls="-.")
        ax1[j].set_ylabel("v (Ladungsschwerpunkt, Fenster +-10)"); ax1[j].set_title("Q E/M = %s" % a0)
        ax2[j].set_ylabel("gamma"); ax2[j].set_title("Q E/M = %s (strichpunktiert: Kink NETZ-C-1)" % a0)
        ax2[j].set_ylim(0.9, max(5.0, 1.0))
        ax3[j].set_ylabel("Q_win / Q0 (Fenster X +- 10)"); ax3[j].set_title("Q E/M = %s" % a0)
        for ax in (ax1[j], ax2[j], ax3[j]):
            ax.set_xlabel("t"); ax.grid(alpha=0.3); ax.legend(fontsize=8)
    for f, n in ((fig1, "v_t.png"), (fig2, "gamma_t.png"), (fig3, "ladung_t.png")):
        f.tight_layout(); f.savefig(os.path.join(ordner, n), dpi=110); plt.close(f)
    # Raum-Zeit-Bild der Ladungsdichte (Hauptlaeufe)
    fig, ax = plt.subplots(1, 3, figsize=(14, 6))
    for j, h in enumerate(HS):
        d = laeufe.get("f1_h%s_dt1" % h)
        if d is None or "snaps" not in d:
            continue
        sn = np.asarray(d["snaps"], float); st = d["snap_t"]; n0 = d["snap_n0"].astype(int); N = sn.shape[1]
        nb = 1200
        x_lo = float(n0.min() * h); x_hi = float((n0.max() + N) * h)
        bild = np.zeros((len(st), nb))
        for i in range(len(st)):
            x = (n0[i] + np.arange(N)) * h
            ib = np.clip(((x - x_lo) / (x_hi - x_lo) * nb).astype(int), 0, nb - 1)
            mx = np.zeros(nb); mn = np.zeros(nb)
            np.maximum.at(mx, ib, sn[i]); np.minimum.at(mn, ib, sn[i])
            bild[i] = np.where(mx >= -mn, mx, mn)
        lg = np.sign(bild) * np.log10(np.abs(bild) / 1e-5 + 1.0)
        vm = float(np.max(np.abs(lg))) if lg.size else 1.0
        ax[j].imshow(lg, origin="lower", aspect="auto", cmap="coolwarm", vmin=-vm, vmax=vm,
                     extent=[x_lo, x_hi, float(st[0]), float(st[-1])])
        ax[j].set_title("h = %s: Ladungsdichte, log, Q E/M = 0,005" % h, fontsize=9)
        ax[j].set_xlabel("x"); ax[j].set_ylabel("t")
    fig.tight_layout(); fig.savefig(os.path.join(ordner, "raumzeit_f1.png"), dpi=110); plt.close(fig)
    return "ok"


def main():
    ordner = sys.argv[1]; aus = sys.argv[2]
    namen = ["g0_h%s" % h for h in HS] + ["%s_h%s_dt%d" % (p, h, D) for p in ("f1", "f2") for h in HS for D in (1, 2)]
    namen += ["f1_h0.125_lang"]
    laeufe = {}
    for n in namen:
        d = lade(ordner, n)
        if d is not None:
            laeufe[n] = d
    kg = {}; kgv = {}; alle_kg = {}
    for n, d in laeufe.items():
        if n.startswith("g0"):
            continue
        r, v, g = kenngroessen(d)
        r2, v2, g2 = kenngroessen(d, tau=TAU2)
        rE, vE, gE = kenngroessen(d, xfeld="XE")
        r["kontrolle_tau20"] = dict(gamma_max=r2.get("gamma_max"), t_max=r2.get("t_max"), t_umkehr=r2.get("t_umkehr"))
        r["kontrolle_energieschwerpunkt"] = dict(gamma_max=rE.get("gamma_max"), t_max=rE.get("t_max"),
                                                 t_umkehr=rE.get("t_umkehr"))
        # gamma(t) an festen Zeiten gegen Kontinuum
        t = d["t"]; a0 = d["kopf"]["a0"]
        tab = {}
        for tz in (50, 100, 200, 300, 400, 600, 800, 1000, 1500, 2000, 3000, 5000, 8000, 10000):
            if tz <= t[-1] - TAU:
                tab[str(tz)] = dict(gamma=float(np.interp(tz, t, g)), v=float(np.interp(tz, t, v)),
                                    gamma_kontinuum=float(math.sqrt(1 + (a0 * tz) ** 2)),
                                    Qwin=float(np.interp(tz, t, d["Qwin"]) / d["kopf"]["Q0"]),
                                    breite=float(np.interp(tz, t, d["breite"])))
        r["verlauf"] = tab
        alle_kg[n] = r
        if n.endswith("_dt1"):
            kgv[(n[:2], d["kopf"]["h"])] = (v, g)
    for h in HS:
        n = "f1_h%s_dt1" % h
        if n in alle_kg:
            kg[h] = alle_kg[n]
    urt = {}
    urt["G0"] = g0_pruefen(laeufe)
    urt["G1"] = g1_pruefen(laeufe.get("f1_h0.125_dt1"))
    urt["G2"] = g2_pruefen(kg)
    urt["G3"] = g3_pruefen(kg)
    urt["G4"] = g4_pruefen(kg)
    # Konvergenzproben: dieselben Urteile mit den Probelaeufen an Stelle der Hauptlaeufe
    proben = {}
    for tag, ersatz in (("dt2", {h: "f1_h%s_dt2" % h for h in HS}), ("lang", {0.125: "f1_h0.125_lang"})):
        kgp = dict(kg)
        fehlt = False
        for h, n in ersatz.items():
            if n in alle_kg:
                kgp[h] = alle_kg[n]
            else:
                fehlt = True
        if fehlt and tag == "dt2" and not any(n in alle_kg for n in ersatz.values()):
            continue
        g1n = ersatz.get(0.125)
        proben[tag] = dict(
            G1=g1_pruefen(laeufe.get(g1n)) if g1n in laeufe else None,
            G2=g2_pruefen(kgp), G3=g3_pruefen(kgp), G4=g4_pruefen(kgp),
            ersetzt={str(h): n for h, n in ersatz.items() if n in alle_kg})
    # Vergleich zweites Feld (beschreibend, gleiche Regeln)
    kg2 = {h: alle_kg["f2_h%s_dt1" % h] for h in HS if "f2_h%s_dt1" % h in alle_kg}
    feld2 = dict(G2=g2_pruefen(kg2), G3=g3_pruefen(kg2), G4=g4_pruefen(kg2),
                 G1=g1_pruefen(laeufe.get("f2_h0.125_dt1")))
    try:
        bstatus = bilder(ordner, laeufe, kgv)
    except Exception as e:
        bstatus = "Bildfehler: %s" % e
    out = dict(urteile=urt, konvergenzproben=proben, feld2_vergleich=feld2, laeufe=alle_kg,
               g0_laeufe=sorted(n for n in laeufe if n.startswith("g0")), bilder=bstatus,
               skript_sha256=__import__("hashlib").sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest())

    def fix(o):
        if isinstance(o, dict):
            return {str(k): fix(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [fix(x) for x in o]
        if isinstance(o, (np.floating, float)):
            x = float(o)
            return x if math.isfinite(x) else str(x)
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, np.bool_):
            return bool(o)
        return o
    json.dump(fix(out), open(aus, "w"), indent=1, ensure_ascii=False)
    print(json.dumps({k: v["urteil"] for k, v in urt.items()}))


if __name__ == "__main__":
    main()
