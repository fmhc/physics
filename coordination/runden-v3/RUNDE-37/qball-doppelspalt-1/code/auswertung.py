#!/usr/bin/env python3
# QBALL-DOPPELSPALT-1: Auswertung (PLAN.md Abschn. 6 und 7). Liest lauf/*.json, ruhe.json, bilanz.json, profil.json,
# schreibt auswertung.json und die Bilder. Laeuft auf der .69 ueber kleintest.sh (CPU-Arbeit in der Einheit).
import sys, os, json, math, glob, time, argparse
import numpy as np
from scipy.signal import find_peaks

SIG = 2.0                 # KDE-Breite in Grad (Plan)
TG = np.arange(-90.0, 90.0001, 0.5)
BIN5 = np.arange(-90.0, 90.0001, 5.0)   # Kartenwortlaut: Histogramm mit 5-Grad-Bins
BIN2 = np.arange(-90.0, 90.0001, 2.0)   # Ladungsverteilung (qds.py: NBIN = 90)
MIN_DURCH = 3             # Kombinationen mit weniger Durchgaengen (Summe der Einzelspalte) werden nicht gewertet
TOL_KONV = 0.02
VQ1_SCHWELLE = 0.05
VQ3_SCHWELLE = 0.05
VQ4_SCHWELLE = 0.20
PER_MIN_PEAKS = 3
PER_CV = 0.25
PER_PROM = 0.10
VQ2_TOL = 0.20


def jetzt():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def kde(thetas, n):
    P = np.zeros_like(TG)
    for t in thetas:
        P += np.exp(-0.5 * ((TG - t) / SIG) ** 2) / (SIG * math.sqrt(2 * math.pi))
    return P / n


def hist5(thetas, n):
    h, _ = np.histogram(thetas, bins=BIN5)
    return h / n


def integ(f, dx=0.5):
    return float(np.sum(f) * dx)


def spiegel_rec(r):
    """y -> -y: Winkel und Ladungshistogramm spiegeln."""
    s = dict(r)
    s["theta"] = None if r.get("theta") is None else -r["theta"]
    s["hist"] = list(reversed(r["hist"]))
    s["flux"] = list(reversed(r["flux"]))
    s["stuecke"] = [dict(st, y=-st["y"], Py=-st["Py"]) for st in r.get("stuecke", [])]
    return s


def lade(laufdir):
    """Alle Auftraege zusammenfuehren: Schluessel (modell, omega, h, nspalt, dkey, v) -> {konfig: {j81: rec}}."""
    data = {}
    meta = {}
    for p in sorted(glob.glob(os.path.join(laufdir, "*.json"))):
        try:
            z = json.load(open(p))
        except Exception:
            continue
        if z.get("modus") != "lauf":
            continue
        a = z["argumente"]
        dkey = ("w%g:" % a.get("wf", 1.0) if a.get("wf", 1.0) != 1.0 else "") + ("fern" if a["d_art"] == "fern" else "%gR" % a["d"])
        ny = a["ny"]
        for v, blk in z["je_v"].items():
            if not blk.get("laeufe"):
                continue
            key =(a["modell"], a["omega"], a["h"], a["nspalt"], dkey, v)
            meta[key] = dict(R=z["R"], om=z["om"], kappa=z["kappa"], w=z["w"], d=z["d"], mitten=z["mitten"],
                             Ymax=z["Ymax"])
            for c, lst in blk["laeufe"].items():
                for r in lst:
                    j81 = 2 * r["j"] if ny == 41 else r["j"]
                    data.setdefault(key, {}).setdefault(c, {})[j81] = r
    return data, meta


def konfigs_mit_spiegel(dk, nspalt):
    """Ergaenzt gespiegelte Konfigurationen: 2 Spalte: B = S(A); 3 Spalte: C = S(A), BC = S(AB)."""
    out = dict(dk)
    paare = {2: [("B", "A")], 3: [("C", "A"), ("BC", "AB")]}[nspalt]
    for neu, alt in paare:
        if neu in out or alt not in out:
            continue
        out[neu] = {80 - j: spiegel_rec(r) for j, r in out[alt].items()}
    return out


def auswahl(dk, gitter):
    """gitter 41: nur gerade j81; gitter 81: alle 81 (nur wenn vollstaendig)."""
    out = {}
    for c, m in dk.items():
        if gitter == 41:
            js = list(range(0, 81, 2))
        else:
            js = list(range(81))
        if all(j in m for j in js):
            out[c] = [m[j] for j in js]
    return out


def verteilungen(sel, n):
    P, H5, Hq, ndurch = {}, {}, {}, {}
    for c, recs in sel.items():
        th = [r["theta"] for r in recs if r.get("theta") is not None]
        P[c] = kde(th, n)
        H5[c] = hist5(th, n)
        Hq[c] = np.mean([np.array(r["hist"]) for r in recs], axis=0)
        ndurch[c] = len(th)
    return P, H5, Hq, ndurch


def i2_mass(D):
    if not all(k in D for k in ("A", "B", "AB")):
        return None
    I = D["AB"] - D["A"] - D["B"]
    s = float(np.sum(np.abs(D["A"] + D["B"])))
    return dict(I_abs=float(np.sum(np.abs(I))), summe=s, r2=(float(np.sum(np.abs(I))) / s) if s > 0 else None)


def i3_mass(D):
    ks = ("A", "B", "C", "AB", "BC", "AC", "ABC")
    if not all(k in D for k in ks):
        return None
    I3 = D["ABC"] - D["AB"] - D["BC"] - D["AC"] + D["A"] + D["B"] + D["C"]
    IAB = D["AB"] - D["A"] - D["B"]
    IBC = D["BC"] - D["B"] - D["C"]
    IAC = D["AC"] - D["A"] - D["C"]
    delta = np.abs(IAB) + np.abs(IBC) + np.abs(IAC)
    sd = float(np.sum(delta))
    out = dict(I3_abs=float(np.sum(np.abs(I3))), I3_int=float(np.sum(I3)), delta=sd,
               kappa_L1=(float(np.sum(np.abs(I3))) / sd) if sd > 0 else None,
               kappa_int=(float(np.sum(I3)) / sd) if sd > 0 else None)
    return out


def i3_zentral(D, edges):
    """Sinha-artig: kappa = I3/delta im Bin, der 0 Grad enthaelt (Kartenwortlaut-Lesart)."""
    ks = ("A", "B", "C", "AB", "BC", "AC", "ABC")
    if not all(k in D for k in ks):
        return None
    i = int(np.searchsorted(edges, 0.0, side="right") - 1)
    g = {k: float(D[k][i]) for k in ks}
    I3 = g["ABC"] - g["AB"] - g["BC"] - g["AC"] + g["A"] + g["B"] + g["C"]
    de = abs(g["AB"] - g["A"] - g["B"]) + abs(g["BC"] - g["B"] - g["C"]) + abs(g["AC"] - g["A"] - g["C"])
    return dict(I3=I3, delta=de, kappa=(I3 / de) if de > 0 else None)


def periode(P):
    if np.max(P) <= 0:
        return dict(peaks=[], periodisch=False, periode=None)
    pk, _ = find_peaks(P, prominence=PER_PROM * float(np.max(P)))
    pos = TG[pk].tolist()
    if len(pk) >= PER_MIN_PEAKS:
        sp = np.diff(TG[pk])
        cv = float(np.std(sp) / np.mean(sp))
        return dict(peaks=pos, periodisch=bool(cv <= PER_CV), periode=float(np.mean(sp)), cv=cv)
    return dict(peaks=pos, periodisch=False, periode=None)


def klassen_zaehlen(recs):
    z = {}
    for r in recs:
        z[r["klasse"]] = z.get(r["klasse"], 0) + 1
    return z


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--bild", required=True)
    a = ap.parse_args()
    t0 = time.time()
    lauf = os.path.join(a.dir, "lauf")
    data, meta = lade(lauf)
    out = {"start_utc": jetzt(), "festlegungen": dict(SIG=SIG, MIN_DURCH=MIN_DURCH, TOL_KONV=TOL_KONV,
                                                      PER_MIN_PEAKS=PER_MIN_PEAKS, PER_CV=PER_CV, PER_PROM=PER_PROM),
           "kombis": {}}
    for p in ("ruhe", "bilanz", "profil"):
        f = os.path.join(a.dir, "lauf", p + ".json")
        if os.path.exists(f):
            out[p] = json.load(open(f))
    werte = {}
    for key, dk in data.items():
        modell, om, h, nspalt, dkey, v = key
        dk2 = konfigs_mit_spiegel(dk, nspalt)
        for gitter in (41, 81):
            sel = auswahl(dk2, gitter)
            if not sel:
                continue
            n = gitter
            P, H5, Hq, nd = verteilungen(sel, n) if modell == "qball" else ({}, {}, {c: np.mean([np.array(r["hist"]) for r in recs], axis=0) for c, recs in sel.items()}, {})
            e = dict(modell=modell, omega=om, h=h, nspalt=nspalt, d=dkey, v=v, gitter=gitter, konfigs=sorted(sel.keys()),
                     n_durch=nd)
            if modell == "qball":
                e["klassen"] = {c: klassen_zaehlen(recs) for c, recs in sel.items()}
                e["teilreflexion"] = {c: int(sum(1 for r in recs if r.get("teilreflexion"))) for c, recs in sel.items()}
                e["dQ_rel_max"] = float(max(abs(r["Q0"] - 1.0) for recs in sel.values() for r in recs))
                e["E_verlust_rel_max"] = float(max((r["E0"] - r["E1"]) / r["E0"] for recs in sel.values() for r in recs))
            # Flussanteile (Spalte mit >= 10 %)
            if nspalt == 2:
                if modell == "qball":
                    e["I2_kde"] = i2_mass(P)
                    e["I2_bin5"] = i2_mass(H5)
                e["I2_ladung"] = i2_mass(Hq)
                if modell == "qball" and "AB" in P:
                    e["periode_kde"] = periode(P["AB"])
                    e["periode_bin5"] = None
                    # V-Q4 (Plan): durchgelassen = n_durch >= 1; geteilt = n_durch >= 2
                    recs = sel["AB"]
                    nd_ = [r for r in recs if r["n_durch"] >= 1]
                    e["VQ4"] = dict(durchgelassen=len(nd_), geteilt_plan=int(sum(1 for r in nd_ if r["n_durch"] >= 2)),
                                    geteilt_wortlaut=int(sum(1 for r in nd_ if (r["n_durch"] + r["n_zurueck"]) >= 2)),
                                    beide_spalte=int(sum(1 for r in recs if r["n_spalt_10"] >= 2)))
            if nspalt == 3:
                if modell == "qball":
                    e["I3_kde"] = i3_mass(P)
                    e["I3_bin5"] = i3_mass(H5)
                    e["I3_zentral_bin5"] = i3_zentral(H5, BIN5)
                e["I3_ladung"] = i3_mass(Hq)
                e["I3_zentral_ladung"] = i3_zentral(Hq, BIN2)
            # Rohkurven fuer Bilder (nur Gitter 41, h = 0,25)
            if gitter == 41 and abs(h - 0.25) < 1e-9 and modell == "qball":
                e["_kurven"] = {c: P[c].tolist() for c in P}
                e["_theta_y"] = {c: [[r["y"], r.get("theta")] for r in recs] for c, recs in sel.items()}
            if modell == "lin":
                e["_ladung"] = {c: Hq[c].tolist() for c in Hq}
            k = "%s|%s|h%g|%d|%s|v%s|n%d" % (modell, om, h, nspalt, dkey, v, gitter)
            werte[k] = e
    out["kombis"] = {k: {kk: vv for kk, vv in e.items() if not kk.startswith("_")} for k, e in werte.items()}

    def wert(modell, om, h, nspalt, dkey, v, gitter, feld, sub):
        e = werte.get("%s|%s|h%g|%d|%s|v%s|n%d" % (modell, om, h, nspalt, dkey, v, gitter))
        if e is None or e.get(feld) is None:
            return None
        return e[feld].get(sub)

    def nsum(om, nspalt, dkey, v, konf):
        e = werte.get("qball|%s|h0.25|%d|%s|v%s|n41" % (om, nspalt, dkey, v))
        if e is None:
            return 0
        return sum(e["n_durch"].get(c, 0) for c in konf)

    urteile = {}
    # ---------------- V-Q1: fern, Doppelspalt, je (omega, v)
    zeilen = []
    for om in ("0.8", "0.9"):
        for v in ("0.2", "0.3", "0.45"):
            z = dict(omega=om, v=v)
            for les, feld in (("plan", "I2_kde"), ("wortlaut", "I2_bin5")):
                r41 = wert("qball", om, 0.25, 2, "fern", v, 41, feld, "r2")
                r81 = wert("qball", om, 0.25, 2, "fern", v, 81, feld, "r2")
                rh = wert("qball", om, 0.125, 2, "fern", v, 41, feld, "r2")
                z[les] = dict(r2_41=r41, r2_81=r81, r2_h0125=rh,
                              konv_y=(abs(r81 - r41) < TOL_KONV) if (r41 is not None and r81 is not None) else None,
                              konv_h=(abs(rh - r41) < TOL_KONV) if (r41 is not None and rh is not None) else None)
            z["n_durch_A_B"] = nsum(om, 2, "fern", v, ("A", "B"))
            zeilen.append(z)

    def urteil_vq1(les):
        gew = [z for z in zeilen if z["n_durch_A_B"] >= MIN_DURCH and z[les]["r2_41"] is not None]
        if not gew:
            return "unentschieden (keine wertbare Kombination)"
        konv = [z for z in gew if z[les]["konv_y"] and z[les]["konv_h"]]
        if any(z[les]["r2_41"] >= VQ1_SCHWELLE for z in konv):
            return "gescheitert"
        if len(konv) == len(gew) and all(z[les]["r2_41"] < VQ1_SCHWELLE for z in konv):
            return "bestanden"
        return "unentschieden (Konvergenz nicht fuer alle wertbaren Kombinationen geprueft/bestanden)"
    urteile["VQ1"] = dict(zeilen=zeilen, plan=urteil_vq1("plan"), wortlaut=urteil_vq1("wortlaut"))

    # ---------------- V-Q2: d <= 1,5 R, Doppelspalt AB, Periode gegen v
    vq2 = []
    gv = {v: (1.0 / math.sqrt(1 - float(v) ** 2)) * float(v) for v in ("0.2", "0.3", "0.45")}
    for om in ("0.8", "0.9"):
        for dkey in ("1R", "1.5R"):
            pers = {}
            for v in ("0.2", "0.3", "0.45"):
                e = werte.get("qball|%s|h0.25|2|%s|v%s|n41" % (om, dkey, v))
                pers[v] = None if e is None else e.get("periode_kde")
            alle = all(p is not None and p["periodisch"] for p in pers.values())
            z = dict(omega=om, d=dkey, perioden={v: (p["periode"] if p else None) for v, p in pers.items()},
                     peaks={v: (p["peaks"] if p else None) for v, p in pers.items()}, alle_periodisch=alle)
            if alle:
                c = [pers[v]["periode"] * gv[v] for v in pers]
                m = float(np.mean(c))
                z["c"] = c
                z["max_abw"] = float(max(abs(x / m - 1) for x in c))
                z["skaliert"] = bool(z["max_abw"] <= VQ2_TOL)
            vq2.append(z)
    per = [z for z in vq2 if z["alle_periodisch"]]
    if not per:
        u2 = "kein Muster"
    elif all(z["skaliert"] for z in per):
        u2 = "bestanden"
    else:
        u2 = "gescheitert"
    urteile["VQ2"] = dict(zeilen=vq2, plan=u2, wortlaut=u2)

    # ---------------- V-Q3: d <= 1,5 R, Dreifachspalt, kappa - Rand-kappa
    zeilen3 = []
    for om in ("0.8", "0.9"):
        for dkey in ("1R", "1.5R"):
            for v in ("0.2", "0.3", "0.45"):
                z = dict(omega=om, d=dkey, v=v, n_durch_einzel=nsum(om, 3, dkey, v, ("A", "B", "C")))
                for les, feld, sub, linfeld, linsub in (("plan", "I3_kde", "kappa_L1", "I3_ladung", "kappa_L1"),
                                                        ("ladung", "I3_ladung", "kappa_L1", "I3_ladung", "kappa_L1"),
                                                        ("wortlaut", "I3_zentral_bin5", "kappa", "I3_zentral_ladung", "kappa")):
                    vals = {}
                    for tag, hh, g in (("41", 0.25, 41), ("81", 0.25, 81), ("h0125", 0.125, 41)):
                        kq = wert("qball", om, hh, 3, dkey, v, g, feld, sub)
                        kl = wert("lin", om, hh, 3, dkey, v, g, linfeld, linsub)
                        vals[tag] = dict(kq=kq, krand=kl, korr=(kq - kl) if (kq is not None and kl is not None) else None)
                    k41 = vals["41"]["korr"]
                    z[les] = dict(vals=vals,
                                  konv_y=(abs(vals["81"]["korr"] - k41) < TOL_KONV) if (k41 is not None and vals["81"]["korr"] is not None) else None,
                                  konv_h=(abs(vals["h0125"]["korr"] - k41) < TOL_KONV) if (k41 is not None and vals["h0125"]["korr"] is not None) else None)
                zeilen3.append(z)

    def urteil_vq3(les):
        gew = [z for z in zeilen3 if z["n_durch_einzel"] >= MIN_DURCH and z[les]["vals"]["41"]["korr"] is not None]
        if not gew:
            return "unentschieden (keine wertbare Kombination)"
        konv = [z for z in gew if z[les]["konv_y"] and z[les]["konv_h"]]
        if len(konv) < len(gew):
            return "unentschieden (Konvergenz nicht fuer alle wertbaren Kombinationen geprueft/bestanden: %d von %d)" % (len(konv), len(gew))
        gross = [abs(z[les]["vals"]["41"]["korr"]) >= VQ3_SCHWELLE for z in konv]
        if all(gross):
            return "bestanden"
        if not any(gross):
            return "gescheitert"
        return "gemischt (kein Urteil)"
    urteile["VQ3"] = dict(zeilen=zeilen3, plan=urteil_vq3("plan"), ladung=urteil_vq3("ladung"),
                          wortlaut=urteil_vq3("wortlaut"))

    # ---------------- V-Q4: d = R, Doppelspalt AB, gepoolt ueber omega, v
    nd = ng = ngw = 0
    zeilen4 = []
    for om in ("0.8", "0.9"):
        for v in ("0.2", "0.3", "0.45"):
            e = werte.get("qball|%s|h0.25|2|1R|v%s|n41" % (om, v))
            if e is None or "VQ4" not in e:
                continue
            q = e["VQ4"]
            zeilen4.append(dict(omega=om, v=v, **q))
            nd += q["durchgelassen"]
            ng += q["geteilt_plan"]
            ngw += q["geteilt_wortlaut"]

    def u4(n_g):
        if nd < 5:
            return "unentschieden (weniger als 5 durchgelassene Laeufe)"
        return "bestanden" if n_g / nd >= VQ4_SCHWELLE else "gescheitert"
    urteile["VQ4"] = dict(zeilen=zeilen4, durchgelassen=nd, geteilt_plan=ng, geteilt_wortlaut=ngw,
                          anteil_plan=(ng / nd) if nd else None, anteil_wortlaut=(ngw / nd) if nd else None,
                          plan=u4(ng), wortlaut=u4(ngw))
    out["urteile"] = urteile
    out["sek"] = time.time() - t0
    out["ende_utc"] = jetzt()
    with open(a.out + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(a.out + ".tmp", a.out)
    print("urteile", {k: {kk: vv for kk, vv in u.items() if kk in ("plan", "wortlaut", "ladung")} for k, u in urteile.items()}, flush=True)

    # ---------------- Bilder
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    dks = ("1R", "1.5R", "3R", "fern")
    fig, axs = plt.subplots(8, 3, figsize=(13, 20), sharex=True)
    for i, (om, dkey) in enumerate([(o, d) for o in ("0.8", "0.9") for d in dks]):
        for jv, v in enumerate(("0.2", "0.3", "0.45")):
            ax = axs[i, jv]
            e = werte.get("qball|%s|h0.25|2|%s|v%s|n41" % (om, dkey, v))
            if e is None or "_kurven" not in e:
                ax.text(0.5, 0.5, "keine Daten", transform=ax.transAxes, ha="center")
            else:
                K = {c: np.array(x) for c, x in e["_kurven"].items()}
                if "AB" in K:
                    ax.plot(TG, K["AB"], "k-", lw=1.2, label="AB (beide offen)")
                if "A" in K and "B" in K:
                    ax.plot(TG, K["A"] + K["B"], "r--", lw=1.0, label="A + B")
                r2 = (e.get("I2_kde") or {}).get("r2")
                ax.set_title("omega %s, d %s, v %s: |I2|/Summe %s" % (om, dkey, v, "-" if r2 is None else "%.3f" % r2),
                             fontsize=8)
            if i == 7:
                ax.set_xlabel("Ablenkwinkel des groessten Stuecks [Grad]")
            if jv == 0:
                ax.set_ylabel("Dichte [1/Grad]")
            if i == 0 and jv == 0:
                ax.legend(fontsize=7)
    fig.suptitle("QBALL-DOPPELSPALT-1: Doppelspalt, KDE (sigma 2 Grad) der Ablenkwinkel, h = 0,25, 41 Stossparameter",
                 fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.98])
    fig.savefig(a.bild, dpi=90)
    plt.close(fig)
    fig, axs = plt.subplots(4, 3, figsize=(13, 11), sharex=True)
    for i, (om, dkey) in enumerate([(o, d) for o in ("0.8", "0.9") for d in ("1R", "1.5R")]):
        for jv, v in enumerate(("0.2", "0.3", "0.45")):
            ax = axs[i, jv]
            e = werte.get("qball|%s|h0.25|3|%s|v%s|n41" % (om, dkey, v))
            if e is None or "_kurven" not in e:
                ax.text(0.5, 0.5, "keine Daten", transform=ax.transAxes, ha="center")
                continue
            K = {c: np.array(x) for c, x in e["_kurven"].items()}
            if all(k in K for k in ("A", "B", "C", "AB", "BC", "AC", "ABC")):
                I3 = K["ABC"] - K["AB"] - K["BC"] - K["AC"] + K["A"] + K["B"] + K["C"]
                ax.plot(TG, K["ABC"], "k-", lw=1.2, label="ABC")
                ax.plot(TG, I3, "b-", lw=1.0, label="I3")
                kp = (e.get("I3_kde") or {}).get("kappa_L1")
                ax.set_title("omega %s, d %s, v %s: kappa_L1 %s" % (om, dkey, v, "-" if kp is None else "%.3f" % kp),
                             fontsize=8)
            if i == 0 and jv == 0:
                ax.legend(fontsize=7)
            if i == 3:
                ax.set_xlabel("Ablenkwinkel [Grad]")
    fig.suptitle("QBALL-DOPPELSPALT-1: Dreifachspalt, KDE und I3, h = 0,25, 41 Stossparameter", fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(a.bild.replace(".png", "-dreifach.png"), dpi=90)
    plt.close(fig)
    # Ablenkwinkel gegen Stossparameter (Doppelspalt AB)
    fig, axs = plt.subplots(2, 4, figsize=(15, 7), sharey=True)
    for i, om in enumerate(("0.8", "0.9")):
        for jd, dkey in enumerate(dks):
            ax = axs[i, jd]
            for v, col in (("0.2", "tab:blue"), ("0.3", "tab:orange"), ("0.45", "tab:green")):
                e = werte.get("qball|%s|h0.25|2|%s|v%s|n41" % (om, dkey, v))
                if e is None or "_theta_y" not in e or "AB" not in e["_theta_y"]:
                    continue
                pts = [(yy, t) for yy, t in e["_theta_y"]["AB"] if t is not None]
                if pts:
                    ax.plot([p[0] for p in pts], [p[1] for p in pts], "o-", ms=3, lw=0.6, color=col, label="v %s" % v)
            ax.set_title("omega %s, d %s (AB)" % (om, dkey), fontsize=9)
            ax.set_xlabel("Stossparameter y_b")
            if jd == 0:
                ax.set_ylabel("Ablenkwinkel [Grad] (nur durchgelassen)")
            if i == 0 and jd == 0:
                ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(a.bild.replace(".png", "-theta-y.png"), dpi=90)
    plt.close(fig)
    # Zusatzarm W (w = 3R, beschreibend, kein Urteil): Kerndichten und Winkel gegen Stossparameter
    wks = sorted({e["d"] for e in werte.values() if str(e["d"]).startswith("w")})
    if wks:
        fig, axs = plt.subplots(2 * len(wks), 4, figsize=(16, 3.2 * 2 * len(wks)), squeeze=False)
        for i, (om, dkey) in enumerate([(o, d) for o in ("0.8", "0.9") for d in wks]):
            for jv, v in enumerate(("0.2", "0.3", "0.45")):
                ax = axs[i, jv]
                e = werte.get("qball|%s|h0.25|2|%s|v%s|n41" % (om, dkey, v))
                if e is None or "_kurven" not in e:
                    ax.text(0.5, 0.5, "keine Daten", transform=ax.transAxes, ha="center")
                    continue
                K = {c: np.array(x) for c, x in e["_kurven"].items()}
                if "AB" in K:
                    ax.plot(TG, K["AB"], "k-", lw=1.2, label="AB")
                if "A" in K and "B" in K:
                    ax.plot(TG, K["A"] + K["B"], "r--", lw=1.0, label="A + B")
                r2 = (e.get("I2_kde") or {}).get("r2")
                ax.set_title("W: omega %s, %s, v %s: r2 %s" % (om, dkey, v, "-" if r2 is None else "%.3f" % r2), fontsize=8)
                if i == 0 and jv == 0:
                    ax.legend(fontsize=7)
            ax = axs[i, 3]
            for v, col in (("0.2", "tab:blue"), ("0.3", "tab:orange"), ("0.45", "tab:green")):
                e = werte.get("qball|%s|h0.25|2|%s|v%s|n41" % (om, dkey, v))
                if e is None or "_theta_y" not in e or "AB" not in e["_theta_y"]:
                    continue
                pts = [(yy, t) for yy, t in e["_theta_y"]["AB"] if t is not None]
                if pts:
                    ax.plot([p[0] for p in pts], [p[1] for p in pts], "o-", ms=3, lw=0.6, color=col, label="v %s" % v)
            ax.set_title("W: Winkel gegen y_b (AB), omega %s, %s" % (om, dkey), fontsize=8)
            if i == 0:
                ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(a.bild.replace(".png", "-zusatz-w.png"), dpi=80)
        plt.close(fig)
    print("bilder", a.bild, f"{time.time() - t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
