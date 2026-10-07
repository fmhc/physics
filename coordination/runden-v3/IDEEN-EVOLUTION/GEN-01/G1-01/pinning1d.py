#!/usr/bin/env python3
"""G1-01 Gitter-Pinning duennwandiger Q-Baelle in 1D. Test-Agent T-2, Generation 1.

Neu geschrieben: Keine Rundenvorlage rechnet stationaere Loesungen auf dem Gitter per Newton in Q (tests1d.py und r5a.py
schiessen im Kontinuum). Nur numpy, float64, CPU; fuer 1 Thread gedacht (OMP/OPENBLAS_NUM_THREADS=1 setzen).

Modell (Atlas): U(S) = S - S^2 + S^3/2, S = f^2. Stationaer auf dem Gitter mit Weite h:
    (f_{j+1} - 2 f_j + f_{j-1}) / h^2 - f_j (1 - 2 f_j^2 + 1,5 f_j^4 - omega^2) = 0
    Q = 2 omega h Sum_j f_j^2,   E = h Sum_j [omega^2 f_j^2 + U(f_j^2)] + h Sum_Bindungen ((f_{j+1} - f_j)/h)^2
Zweige: "platz"   Mitte auf einem Gitterpunkt,      f_{-j} = f_j,     Unbekannte f_0 .. f_M
        "bindung" Mitte zwischen zwei Gitterpunkten, f_{1-j} = f_j,   Unbekannte f_1 .. f_M
Dirichlet f = 0 am Rand |x| = X_RAND. Newton mit Rand: Unbekannte (f, omega), Nebenbedingung Q = Q_ziel.
Fortsetzung in Q mit Sekanten-Vorhersage, Schritt dQ = DQ_FAKTOR * h (grob) bzw. halb so gross (fein).

Kontinuum (geschlossen, Papier in KARTE.md): b = sqrt(2 omega^2 - 1),
    Q_kont = 2 sqrt2 omega arcosh(1/b),  E_kont = omega Q_kont + (sqrt(1 - b^2) - b^2 arcosh(1/b)) / sqrt2,
    Profil f^2 = 4 a u / ((u + 1)^2 - 2 a), a = 1 - omega^2, u = u0 exp(2 sqrt(a) |x|), u0 = (2 a - g0)/g0, g0 = 1 - b.

Aufruf (Messgroessen und Schwellen stehen in KARTE.md, hier nur umgesetzt):
    python pinning1d.py haupt [--h 1,0.75,0.5,0.25] [--stufen grob,fein] [--out ORDNER]
    python pinning1d.py gegen [--h 0.125,0.1] [--stufen grob,fein] [--out ORDNER]
        gegen rechnet zusaetzlich h = 0,25 und 0,125 bis Q = 12,5 fuer die Konvergenzordnung gegen das Kontinuum.
    python pinning1d.py form  (Formprobe: Q 4 bis 14, h = 1 und 0,5, nur grob; Zahlen ungueltig)
Ausgabe: <out>/<modus>_ergebnis.json und <out>/<modus>_bericht.txt.
"""
import argparse
import datetime
import json
import math
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")   # 1 Thread auch unter kleintest.sh (systemd-run reicht die Umgebung nicht durch)
import numpy as np  # noqa: E402

Q_START, Q_ENDE = 4.0, 34.0
FENSTER = (12.0, 30.0)       # Q-Fenster fuer A_E und d_w (Fronten ausgebildet)
X_RAND = 42.0                # Dirichlet-Rand
DQ_FAKTOR = 0.236            # dQ = 0,236 h: etwa 12 Punkte je Pinning-Periode (Periode in Q etwa 2,83 h)
RAUSCHEN_W = 1e-14           # Extrema von omega^2(Q) zaehlen erst ab dieser Umkehr (float64-Rauschen)
AUFL_E = 1e-12               # Energieabstand darunter: "auf dem Raster nicht gesehen"
NEWTON_MAX, NEWTON_TOL = 40, 1e-13
ZEIT_BUDGET = 540.0          # s; danach werden keine neuen Zweige begonnen (kleintest.sh bricht nach 600 s ab)
KONV_Q = (8.0, 12.0)         # Konvergenzordnung gegen das Kontinuum
T0 = time.time()


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


# ---------------- Kontinuum ----------------
def q_kont(w):
    b2 = 2.0 * w * w - 1.0
    if b2 <= 0.0:
        return math.inf
    return 2.0 * math.sqrt(2.0) * w * math.acosh(1.0 / math.sqrt(b2))


def e_kont(w):
    b = math.sqrt(2.0 * w * w - 1.0)
    return w * q_kont(w) + (math.sqrt(1.0 - b * b) - b * b * math.acosh(1.0 / b)) / math.sqrt(2.0)


def w_aus_q_kont(q):
    """omega mit Q_kont(omega) = q (Q_kont faellt monoton in omega auf (1/sqrt2, 1))."""
    lo, hi = math.sqrt(0.5), 1.0 - 1e-15
    for _ in range(200):
        if hi - lo < 4e-16:
            break
        mi = 0.5 * (lo + hi)
        if q_kont(mi) > q:
            lo = mi
        else:
            hi = mi
    return 0.5 * (lo + hi)


def profil_kont(w, x):
    a = 1.0 - w * w
    b = math.sqrt(2.0 * w * w - 1.0)
    g0 = 1.0 - b
    u = (2.0 * a - g0) / g0 * np.exp(2.0 * math.sqrt(a) * np.abs(x))
    g = 4.0 * a * u / ((u + 1.0) ** 2 - 2.0 * a)
    return np.sqrt(np.maximum(g, 0.0))


# ---------------- Gitter ----------------
class Zweig:
    def __init__(self, art, h):
        self.art, self.h = art, h
        m = int(math.floor(X_RAND / h + 1e-9))
        if art == "platz":
            self.x = h * np.arange(0, m + 1, dtype=np.float64)          # f_0 .. f_M
            self.w = np.full(self.x.size, 2.0)
            self.w[0] = 1.0
        else:
            self.x = h * (np.arange(1, m + 1, dtype=np.float64) - 0.5)  # f_1 .. f_M bei (j - 1/2) h
            self.w = np.full(self.x.size, 2.0)
        self.n = self.x.size

    def lap(self, f):
        h2 = self.h * self.h
        r = np.empty_like(f)
        r[1:-1] = f[2:] - 2.0 * f[1:-1] + f[:-2]
        r[-1] = -2.0 * f[-1] + f[-2]                      # f_{M+1} = 0
        if self.art == "platz":
            r[0] = 2.0 * f[1] - 2.0 * f[0]                # f_{-1} = f_1
        else:
            r[0] = f[1] - f[0]                            # f_0 = f_1 (Spiegel), also f_2 - 2 f_1 + f_1
        return r / h2

    def residuum(self, f, w):
        s = f * f
        return self.lap(f) - f * (1.0 - 2.0 * s + 1.5 * s * s - w * w)

    def q(self, f, w):
        return 2.0 * w * self.h * math.fsum(self.w * f * f)

    def energie(self, f, w):
        s = f * f
        teil_platz = self.h * math.fsum(self.w * (w * w * s + s - s * s + 0.5 * s ** 3))
        d = np.diff(np.append(f, 0.0))                    # Bindungen (j, j+1) bis zum Rand
        teil_bind = 2.0 * math.fsum(d * d) / self.h       # jede Bindung zweimal (Spiegel)
        # "platz": Bindungen (0,1),(1,2),...,(M,M+1) und gespiegelt: 2 Sum.  "bindung": Mittelbindung (0,1) hat
        # Differenz 0, sonst (1,2),...,(M,M+1) und gespiegelt: ebenfalls 2 Sum ueber d.
        return teil_platz + teil_bind

    def schritt(self, f, w, q_ziel):
        """Ein Newton-Schritt des geraenderten Systems (f, omega) mit Nebenbedingung Q = q_ziel."""
        h2 = self.h * self.h
        n = self.n
        s = f * f
        F = self.residuum(f, w)
        G = self.q(f, w) - q_ziel
        J = np.zeros((n + 1, n + 1))
        diag = -2.0 / h2 - (1.0 - 2.0 * s + 1.5 * s * s - w * w) - f * (-4.0 * f + 6.0 * s * f)
        idx = np.arange(n)
        J[idx, idx] = diag
        J[idx[:-1], idx[:-1] + 1] = 1.0 / h2
        J[idx[1:], idx[1:] - 1] = 1.0 / h2
        if self.art == "platz":
            J[0, 1] = 2.0 / h2
        else:
            J[0, 0] += 1.0 / h2                           # Zeile 1: (f_2 - f_1)/h^2
        J[:n, n] = 2.0 * w * f
        J[n, :n] = 4.0 * w * self.h * self.w * f
        J[n, n] = 2.0 * self.h * math.fsum(self.w * s)
        return np.linalg.solve(J, -np.append(F, G))

    def newton(self, f, w, q_ziel):
        """Rueckgabe f, omega, Iterationen, konvergiert, Rauschmass |d omega| des Nachschritts nach der Konvergenz."""
        n = self.n
        vorher = math.inf
        for it in range(1, NEWTON_MAX + 1):
            d = self.schritt(f, w, q_ziel)
            f = f + d[:n]
            w = w + d[n]
            gross = max(float(np.max(np.abs(d[:n]))), abs(float(d[n])))
            # konvergiert: Schritt unter der Toleranz, oder Rundungsboden (klein und nicht mehr quadratisch fallend)
            if gross < NEWTON_TOL or (it >= 3 and gross < 1e-9 and gross > 0.5 * vorher):
                d2 = self.schritt(f, w, q_ziel)           # Nachschritt misst den Rundungsboden
                return f + d2[:n], w + d2[n], it + 1, True, abs(float(d2[n]))
            vorher = gross
        return f, w, NEWTON_MAX, False, abs(float(d[n]))


def zweig_rechnen(art, h, dq, q_ende):
    z = Zweig(art, h)
    qs = np.arange(Q_START, q_ende + 0.5 * dq, dq)
    w0 = w_aus_q_kont(Q_START)
    xm = z.x
    f = profil_kont(w0, xm)
    w = w0
    reihe = {"Q": [], "w2": [], "E": [], "fmax2": [], "iter": [], "ok": [], "rausch_w2": []}
    alt = []
    for k, q in enumerate(qs):
        if len(alt) == 2:                                  # Sekanten-Vorhersage
            (f1, w1), (f2, w2_) = alt
            f, w = 2.0 * f2 - f1, 2.0 * w2_ - w1
        f, w, it, ok, dw = z.newton(f, w, q)
        reihe["rausch_w2"].append(2.0 * abs(w) * dw)       # letzter Newton-Schritt in omega^2 (Rauschmass)
        reihe["Q"].append(float(q))
        reihe["w2"].append(float(w * w))
        reihe["E"].append(float(z.energie(f, w)))
        reihe["fmax2"].append(float(np.max(f * f)))
        reihe["iter"].append(it)
        reihe["ok"].append(bool(ok))
        alt = (alt + [(f.copy(), w)])[-2:]
    return reihe


# ---------------- Auswertung ----------------
def extrema(ws, eta):
    """Umkehrpunkte von ws mit Hysterese eta; liefert Indizes der Extrema (ohne Start und Ende)."""
    ext = []
    richtung = 0
    i_ext = 0
    for i in range(1, len(ws)):
        if richtung == 0:
            if ws[i] < ws[i_ext] - eta:
                richtung, i_ext = -1, i
            elif ws[i] > ws[i_ext] + eta:
                richtung, i_ext = 1, i
            elif (richtung == 0) and abs(ws[i] - ws[0]) <= eta:
                continue
        elif richtung < 0:
            if ws[i] < ws[i_ext]:
                i_ext = i
            elif ws[i] > ws[i_ext] + eta:
                ext.append(i_ext)
                richtung, i_ext = 1, i
        else:
            if ws[i] > ws[i_ext]:
                i_ext = i
            elif ws[i] < ws[i_ext] - eta:
                ext.append(i_ext)
                richtung, i_ext = -1, i
    return ext


def loesungen_je_w2(ws, ext):
    """Groesste Zahl von Loesungen eines Zweigs bei einem omega^2 (Skelett aus Extrema)."""
    if not ext:
        return 1
    stuetz = [ws[0]] + [ws[i] for i in ext] + [ws[-1]]
    stuecke = [(min(a, b), max(a, b)) for a, b in zip(stuetz[:-1], stuetz[1:])]
    werte = sorted(set(stuetz))
    beste = 1
    for a, b in zip(werte[:-1], werte[1:]):
        v = 0.5 * (a + b)
        beste = max(beste, sum(1 for lo, hi in stuecke if lo <= v <= hi))
    return beste


def zweige_auswerten(h, rp, rb):
    Q = np.array(rp["Q"])
    wp, wb = np.array(rp["w2"]), np.array(rb["w2"])
    ep, eb = np.array(rp["E"]), np.array(rb["E"])
    n = min(len(Q), len(rb["Q"]))
    Q, wp, wb, ep, eb = Q[:n], wp[:n], wb[:n], ep[:n], eb[:n]
    im = (Q >= FENSTER[0]) & (Q <= FENSTER[1])
    a_e = float(np.max(np.abs(ep[im] - eb[im]))) if im.any() else None
    d_w = float(np.max(np.abs(wp[im] - wb[im]))) if im.any() else None
    zwei = float(np.mean(np.abs(ep[im] - eb[im]) > AUFL_E)) if im.any() else None
    aus = {"h": h, "n_Q": int(n), "Q_max": float(Q[-1]), "A_E": a_e, "d_w": d_w,
           "anteil_Q_mit_2_loesungen": zwei,
           "loesungen_je_Q": (2 if (a_e is not None and a_e > AUFL_E) else 1)}
    for name, ws in (("platz", wp), ("bindung", wb)):
        r_ = rp if name == "platz" else rb
        eta = max(RAUSCHEN_W, 10.0 * max(r_["rausch_w2"][:len(ws)]))   # "ueber dem Rauschen": 10 x Newton-Boden
        ext = extrema(list(ws), eta)
        q_pin = float(Q[ext[0]]) if ext else None
        aus[name] = {"n_extrema": len(ext), "Q_pin": q_pin, "eta_rauschen": eta,
                     "W_pin": (float(ws[ext[0]] - 0.5) if ext else None),
                     "max_loesungen_je_w2": loesungen_je_w2(list(ws), ext),
                     "w2_min": float(np.min(ws)), "w2_ende": float(ws[-1])}
    aus["snaking"] = bool(aus["platz"]["n_extrema"] > 0 or aus["bindung"]["n_extrema"] > 0)
    return aus


def plausibel(h, reihen, d_w):
    fehler = []
    dw = d_w if d_w is not None else 0.0
    rel_max = 0.0
    for art, r in reihen.items():
        Q = np.array(r["Q"])
        w2 = np.array(r["w2"])
        E = np.array(r["E"])
        w = np.sqrt(w2)
        if not all(r["ok"]):
            fehler.append(f"{art}: Newton nicht konvergiert an {r['ok'].count(False)} Stellen")
        if np.any(w2 < 0.5 - dw - 1e-14) or np.any(w2 >= 1.0):
            fehler.append(f"{art}: omega^2 ausserhalb [1/2 - d_w, 1)")
        eq = E / Q
        if np.any(eq <= w) or np.any(eq >= 1.0):
            fehler.append(f"{art}: omega < E/Q < 1 verletzt")
        fm = np.array(r["fmax2"])
        if np.any(fm <= 0.0) or np.any(fm > 1.0 + 1e-9):
            fehler.append(f"{art}: max f^2 ausserhalb (0, 1 + 1e-9]")
        if len(Q) >= 3:
            dq = Q[2:] - Q[:-2]
            dedq = (E[2:] - E[:-2]) / dq
            # omega als Simpson-Mittel der drei Stuetzpunkte: (E_{k+1} - E_{k-1}) = Int omega dQ exakt bis O(dQ^5);
            # der blosse Mittelpunktwert haette den Abbruchfehler dQ^2 omega''/6 (bei h = 1 etwa 4e-4 relativ).
            w_simpson = (w[:-2] + 4.0 * w[1:-1] + w[2:]) / 6.0
            rel = np.abs(dedq - w_simpson) / w_simpson
            rel_max = max(rel_max, float(np.max(rel)))
    if rel_max > 1e-4:
        fehler.append(f"dE/dQ gegen omega: {rel_max:.2e} > 1e-4")
    return {"h": h, "bestanden": not fehler, "fehler": fehler, "dEdQ_rel_max": rel_max}


def fit_c(werte):
    pts = [(1.0 / h, math.log(a)) for h, a in werte if a is not None and a > 1e-13]
    if len(pts) < 2:
        return None, len(pts)
    x = np.array([p[0] for p in pts])
    y = np.array([p[1] for p in pts])
    A = np.vstack([x, np.ones_like(x)]).T
    k, _ = np.linalg.lstsq(A, y, rcond=None)[0]
    return float(-k), len(pts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["haupt", "gegen", "form"])
    ap.add_argument("--h", default=None, help="Gitterweiten, Komma-getrennt")
    ap.add_argument("--stufen", default="grob,fein")
    ap.add_argument("--q-ende", type=float, default=Q_ENDE)
    ap.add_argument("--out", default=".")
    args = ap.parse_args()
    start = jetzt()
    if args.modus == "haupt":
        hs = [1.0, 0.75, 0.5, 0.25]
    elif args.modus == "gegen":
        hs = [0.125, 0.1]
    else:
        hs = [1.0, 0.5]
    if args.h:
        hs = [float(v) for v in args.h.split(",")]
    stufen = [s for s in args.stufen.split(",") if s]
    q_ende = args.q_ende
    if args.modus == "form":
        stufen, q_ende = ["grob"], 14.0
    os.makedirs(args.out, exist_ok=True)
    text = [f"G1-01 Gitter-Pinning 1D, Modus {args.modus}. Start {start}, numpy {np.__version__}, "
            f"Threads OMP={os.environ.get('OMP_NUM_THREADS')} OPENBLAS={os.environ.get('OPENBLAS_NUM_THREADS')}"]
    if args.modus == "form":
        text.append("FORMPROBE: Zahlen ungueltig, nur Durchlauf und Laufzeit.")
    ergebnis = {"karte": "G1-01", "modus": args.modus, "start": start, "stufen": {}, "abgebrochen": []}
    dauer = {}
    for stufe in stufen:
        fak = 1.0 if stufe == "grob" else 0.5
        erg_st = []
        for h in hs:
            if time.time() - T0 > ZEIT_BUDGET:
                ergebnis["abgebrochen"].append({"stufe": stufe, "h": h, "grund": "Zeitbudget"})
                continue
            t1 = time.time()
            dq = DQ_FAKTOR * h * fak
            reihen = {art: zweig_rechnen(art, h, dq, q_ende) for art in ("platz", "bindung")}
            aus = zweige_auswerten(h, reihen["platz"], reihen["bindung"])
            aus["dQ"] = dq
            aus["plausibel"] = plausibel(h, reihen, aus["d_w"])
            aus["dauer_s"] = round(time.time() - t1, 2)
            aus["reihen"] = reihen
            dauer[f"{stufe}_h{h}"] = aus["dauer_s"]
            erg_st.append(aus)
            print(f"  {stufe} h={h}: {aus['dauer_s']} s, A_E={aus['A_E']}, d_w={aus['d_w']}, "
                  f"snaking={aus['snaking']}, plausibel={aus['plausibel']['bestanden']}", flush=True)
        ergebnis["stufen"][stufe] = erg_st
    # Konvergenzordnung gegen das Kontinuum (nur gegen): h = 0,25 und 0,125 bis Q = 12,5
    if args.modus == "gegen" and time.time() - T0 < ZEIT_BUDGET:
        konv = {}
        for h in (0.25, 0.125):
            r = zweig_rechnen("platz", h, DQ_FAKTOR * h, 12.5)
            Q = np.array(r["Q"])
            konv[h] = {}
            for qz in KONV_Q:
                i = int(np.argmin(np.abs(Q - qz)))
                wk = w_aus_q_kont(float(Q[i]))
                konv[h][qz] = {"Q": float(Q[i]), "w2_gitter": r["w2"][i], "w2_kont": wk * wk,
                               "fehler": abs(r["w2"][i] - wk * wk), "E_gitter": r["E"][i], "E_kont": e_kont(wk)}
        verh = {str(qz): konv[0.25][qz]["fehler"] / max(konv[0.125][qz]["fehler"], 1e-300) for qz in KONV_Q}
        ergebnis["kontinuum"] = {"werte": {str(h): {str(q): v for q, v in d.items()} for h, d in konv.items()},
                                 "fehlerverhaeltnis_0.25_zu_0.125": verh,
                                 "ordnung_2_bestanden": all(3.0 <= v <= 5.0 for v in verh.values())}
    # Kennzahlen gegen KARTE.md
    kenn = {}
    for stufe, erg_st in ergebnis["stufen"].items():
        werte = [(a["h"], a["A_E"]) for a in erg_st]
        c, n_pts = fit_c([(h, a) for h, a in werte if h in (1.0, 0.75, 0.5)])
        k = {"A_E": {str(h): a for h, a in werte}, "d_w": {str(a["h"]): a["d_w"] for a in erg_st},
             "snaking": {str(a["h"]): a["snaking"] for a in erg_st},
             "plausibel": {str(a["h"]): a["plausibel"]["bestanden"] for a in erg_st},
             "c_fit": c, "c_fit_punkte": n_pts}
        if args.modus == "haupt":
            a05 = dict(werte).get(0.5)
            k["V1_c_in_10_18"] = (None if c is None else bool(10.0 <= c <= 18.0))
            k["V2_A_E_05_in_1e-14_1e-8"] = (None if a05 is None else bool(1e-14 <= a05 <= 1e-8))
            s1 = k["snaking"].get("1.0")
            s25 = k["snaking"].get("0.25")
            k["V3_snaking_h1"] = s1
            k["V3_kein_snaking_h025"] = (None if s25 is None else (not s25))
            a25 = dict(werte).get(0.25)
            k["V4_A_E_025_unter_1e-12"] = (None if a25 is None else bool(a25 < 1e-12))
        if args.modus == "gegen":
            k["gegenprobe_monoton_und_klein"] = all((not a["snaking"]) and (a["A_E"] is not None and a["A_E"] < 1e-12)
                                                    for a in erg_st)
        kenn[stufe] = k
    if "grob" in ergebnis["stufen"] and "fein" in ergebnis["stufen"]:
        l3 = []
        g = {a["h"]: a for a in ergebnis["stufen"]["grob"]}
        for a in ergebnis["stufen"]["fein"]:
            b = g.get(a["h"])
            if b is None or a["A_E"] is None or b["A_E"] is None:
                continue
            gross = max(a["A_E"], b["A_E"]) > 1e-13
            rel = abs(a["A_E"] - b["A_E"]) / max(a["A_E"], b["A_E"], 1e-300)
            l3.append({"h": a["h"], "A_E_grob": b["A_E"], "A_E_fein": a["A_E"], "rel_aenderung": rel,
                       "messbar": gross, "bestanden": (rel <= 0.05) if gross else (a["snaking"] == b["snaking"])})
        kenn["L3"] = {"laeufe": l3, "bestanden": all(x["bestanden"] for x in l3) if l3 else None}
    ergebnis["kennzahlen"] = kenn
    ergebnis["plausibilitaet_bestanden"] = all(a["plausibel"]["bestanden"]
                                              for st in ergebnis["stufen"].values() for a in st)
    ergebnis["dauer_s"] = dauer
    ergebnis["ende"] = jetzt()
    ergebnis["gesamt_s"] = round(time.time() - T0, 1)
    with open(os.path.join(args.out, f"{args.modus}_ergebnis.json"), "w") as fh:
        json.dump(ergebnis, fh, indent=1)
    text.append(f"Ende {ergebnis['ende']}, gesamt {ergebnis['gesamt_s']} s, Plausibilitaet bestanden: "
                f"{ergebnis['plausibilitaet_bestanden']}")
    for stufe, erg_st in ergebnis["stufen"].items():
        for a in erg_st:
            text.append(f"  {stufe} h={a['h']}: A_E={a['A_E']}, d_w={a['d_w']}, snaking={a['snaking']} "
                        f"(Q_pin platz {a['platz']['Q_pin']}), Loesungen je Q {a['loesungen_je_Q']}, "
                        f"plausibel {a['plausibel']['bestanden']}, {a['dauer_s']} s")
    text.append("Kennzahlen: " + json.dumps(kenn, default=str))
    if "kontinuum" in ergebnis:
        text.append("Kontinuum: " + json.dumps(ergebnis["kontinuum"]["fehlerverhaeltnis_0.25_zu_0.125"])
                    + f", Ordnung 2 bestanden: {ergebnis['kontinuum']['ordnung_2_bestanden']}")
    if ergebnis["abgebrochen"]:
        text.append("Abgebrochen (Zeitbudget): " + json.dumps(ergebnis["abgebrochen"]))
    with open(os.path.join(args.out, f"{args.modus}_bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")
    print("\n".join(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
