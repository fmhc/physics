#!/usr/bin/env python3
"""Runde 21 (v3), Karte bio28-weiter (RUNDE-21/bio28-weiter/KARTE.md): Gebiets-Zeitreihe fuer Bio 28.

Rechnet Karte 5 (groesse) aus RUNDE-05/r5-2d-a/r5_2d_a.py mit unveraendertem Code nach und gibt zusaetzlich von
t = 0 bis 30 alle 0,5 die Gebiete aus (Zahl; je Gebiet Q, Schwerpunkt, Windung; Schwerpunktabstaende).

Aus r5_2d_a.py unveraendert benutzt: profile_holen (Schiessen), Gitter, ball_feld, entwickeln (Velocity-Verlet mit
Randschicht), dichten, unschaerfe, analyse (Gebiete, Schwerpunkt, Windung auf dem Kreis), ganz_verschmolzen,
erste_dauerhaft, erhaltung, verlauf_kurz, gebiet_kurz, auswahl und alle Konstanten (T5_*, STUFEN, L_STD,
SCHWELLE_REL, BLUR, Q_MIN_REL, N_THETA, ANALYSE_DT, DAUER_K).

Abweichungen (PLAN.md Abschnitt 2, vor dem Lauf festgelegt):
  1. Messtakt 0,5 statt 1: r5.T_MEAS ist waehrend r5.entwickeln 0,5. Zeitschritt, Schrittzahl und Daempfung bleiben;
     die Messung liest psi und psi_t nur.
  2. Eigene Messfunktion = r5.lauf_standard.messen ohne die hier unbenutzten Zweige (r_win, radial). Gebietsanalyse
     an allen Vielfachen von 5 (Runde-5-Raster, fuer K0) und zusaetzlich an jedem Messpunkt bis t = 30.
  3. Zusammenfassung je Lauf wie r5.test_groesse (dieselben Hilfsfunktionen), Index 10 je 5 Zeiteinheiten.
  4. Eigene Ausgabe (JSON und Text), keine .pt-Datei.

Aufruf:  python bio28_weiter.py [--rauch] [--stufe grob|fein|beide] [--out ORDNER] [--ref R5.json]
         python bio28_weiter.py --auswerten ROH.json [--ref R5.json] [--out ORDNER]
--rauch: nur grob, t_end = 1 (vor jedem Verschmelzen), dazu Selbsttest der Auswertung mit erfundener Reihe.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import traceback  # noqa: E402

import torch  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import r5_2d_a as r5  # noqa: E402

DICHT_DT = 0.5           # Takt der Zusatzreihe (Karte: alle 0,5)
DICHT_BIS = 30.0         # Zusatzreihe von t = 0 bis 30
RAUCH_T = 1.0            # Rauchlauf: t_end = 1, nur grob
K0_TOL = 0.10            # K0: Zeiten und Ladungsverlust auf 10 % (relativ), n_ende gleich
VERSCHMOLZEN_Q = 0.9     # wie r5.ganz_verschmolzen: Q_box >= 0,9 Q_box(0)


def sha(pfad):
    try:
        with open(pfad, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()
    except OSError:
        return None


# ---------------------------------------------------------------- Lauf mit dichter Analyse

def lauf_dicht(g, psi, vel, dt, t_end, dicht_bis, zeiten):
    """Wie r5.lauf_standard ohne r_win, l_max, radial; Messtakt DICHT_DT. Gebietsanalyse an allen Vielfachen von
    r5.ANALYSE_DT (Runde-5-Raster) und zusaetzlich an jedem Messpunkt bis dicht_bis.
    Rueckgabe t, daten (M, B, 4), verlauf (Runde-5-Raster), dicht (je Lauf Liste (t, Q_box, Gebiete)), Schwelle, q_min."""
    B = psi.shape[0]
    s0, rho0, _, _, _, _ = r5.dichten(g, psi, vel)
    schwelle = r5.SCHWELLE_REL * r5.unschaerfe(g, s0).amax((1, 2))
    q_min = (r5.Q_MIN_REL * rho0.sum((1, 2)) * g.dA).tolist()
    verlauf = [[] for _ in range(B)]
    dicht = [[] for _ in range(B)]
    zaehler = [0]
    alle5 = int(round(r5.ANALYSE_DT / DICHT_DT))
    n_dicht = int(round(dicht_bis / DICHT_DT))

    def messen(psi, vel):
        d = r5.dichten(g, psi, vel)
        s, rho, e, _, _, jz = d
        spalten = [rho.sum((1, 2)) * g.dA, e.sum((1, 2)) * g.dA, jz.sum((1, 2)) * g.dA, s.amax((1, 2))]
        z = zaehler[0]
        im5, imd = z % alle5 == 0, z <= n_dicht
        if im5 or imd:
            ta = r5.uhr()
            maske = r5.unschaerfe(g, s) > schwelle.view(-1, 1, 1)
            gebiete = r5.analyse(g, psi, d, maske, q_min, True)
            t = z * DICHT_DT
            qbox = spalten[0].tolist()
            for b, geb in enumerate(gebiete):
                if im5:
                    verlauf[b].append((t, geb))
                if imd:
                    dicht[b].append((t, qbox[b], geb))
            zeiten["analyse_s"] += r5.uhr() - ta
            zeiten["analysen"] += 1
        zaehler[0] += 1
        return torch.stack(spalten, dim=1)

    alt = r5.T_MEAS
    r5.T_MEAS = DICHT_DT
    try:
        t, daten = r5.entwickeln(g, psi, vel, dt, t_end, messen)
    finally:
        r5.T_MEAS = alt
    return t, daten, verlauf, dicht, schwelle.tolist(), q_min


def zusammenfassung(name, w2, k, stufe, dd, prof, t, daten, b, verlauf_b):
    """Zeile wie in r5.test_groesse (Zeilen 1311-1327), Index alle5 je Runde-5-Analyse."""
    alle5 = int(round(r5.ANALYSE_DT / DICHT_DT))
    ts = [tt for tt, _ in verlauf_b]
    ns = [len(gb) for _, gb in verlauf_b]
    qb = [daten[i * alle5, b, 0].item() for i in range(len(ts))]
    t_v = r5.ganz_verschmolzen(ts, ns, qb, qb[0]) if k > 0 else None
    i_v = ts.index(t_v) if t_v is not None else 0
    t_neu = r5.erste_dauerhaft(ts[i_v:], [n >= 2 for n in ns[i_v:]]) if (k == 0 or t_v is not None) else None
    wind = [gb[0].get("windung") if gb else None for _, gb in verlauf_b]
    return {"lauf": name, "omega2": w2, "nachbarn": k, "stufe": stufe, "abstand": dd,
            "Q_m1": prof[(w2, 1)]["Q"], "Q_nachbar": prof[(w2, 0)]["Q"],
            "t_verschmolzen": t_v, "t_teilung_danach": t_neu, "n_ende": ns[-1],
            "windung_groesstes_ende": wind[-1],
            "windung_groesstes_verlauf": sorted(set(w for w in wind if w is not None)),
            "J_zu_Q_start": (daten[0, b, 2] / daten[0, b, 0]).item(),
            "gebiete_ende": [r5.gebiet_kurz(d) for d in verlauf_b[-1][1]], **r5.erhaltung(t, daten, b),
            "gebiete": r5.verlauf_kurz(verlauf_b)}


def gebiet_dicht(d):
    return {"Q": round(d["Q"], 4), "windung": d.get("windung"), "S_min_kreis": round(d.get("S_min_kreis", -1.0), 6),
            "X": round(d["X"], 3), "Y": round(d["Y"], 3), "Jspin_Q": round(d["Jspin_Q"], 4),
            "r_mittel": round(d["r_mittel"], 3), "flaeche": round(d["flaeche"], 2), "E": round(d["E"], 4)}


def probe_dicht(t, qbox, gb):
    """Eine Probe der Zusatzreihe; Abstaende ohne periodisches Bild (wie r5.mittlerer_abstand), d12 = zwei groesste."""
    geb = [gebiet_dicht(d) for d in gb]
    paare = [[i, j, round(math.hypot(a["X"] - c["X"], a["Y"] - c["Y"]), 3)]
             for i, a in enumerate(gb) for j, c in enumerate(gb) if j > i]
    return {"t": t, "Q_box": round(qbox, 4), "n": len(gb), "gebiete": geb, "abstaende": paare,
            "d12": paare[0][2] if paare else None}


# ---------------------------------------------------------------- Auswertung (PLAN.md Abschnitt 4, vorab)

def gleich_rel(a, b, tol):
    if a is None or b is None:
        return a is None and b is None
    if b == 0:
        return a == 0
    return abs(a - b) <= tol * abs(b)


def k0_vergleich(ergebnis, ref):
    zeilen = []
    for stufe, liste in ergebnis.items():
        refl = {z["lauf"]: z for z in ref["ergebnis"].get(stufe, [])}
        for z in liste:
            r = refl.get(z["lauf"])
            if r is None:
                zeilen.append({"stufe": stufe, "lauf": z["lauf"], "bestanden": False, "grund": "kein Runde-5-Wert"})
                continue
            pr = {f: {"r5": r[f], "r21": z[f], "ok": gleich_rel(z[f], r[f], K0_TOL)}
                  for f in ("t_verschmolzen", "t_teilung_danach", "Q_box_verlust")}
            pr["n_ende"] = {"r5": r["n_ende"], "r21": z["n_ende"], "ok": z["n_ende"] == r["n_ende"]}
            zeilen.append({"stufe": stufe, "lauf": z["lauf"], "pruef": pr,
                           "bestanden": all(v["ok"] for v in pr.values()),
                           "gebiete_5er_identisch": z.get("gebiete") == r.get("gebiete")})
    erwartet = sum(len(v) for v in ref["ergebnis"].values())
    return {"zeilen": zeilen, "zeilen_erwartet": erwartet, "vollstaendig": len(zeilen) == erwartet,
            "bestanden": bool(zeilen) and len(zeilen) == erwartet and all(x["bestanden"] for x in zeilen)}


def y_lauf(z, reihe):
    """Y1, Y3 je gefuettertem Lauf aus der Zusatzreihe, Y2 aus n_ende (PLAN.md 4.2 bis 4.4); dazu Beschreibendes (4.6)."""
    if z["nachbarn"] == 0:
        return None
    t_T = z["t_teilung_danach"]
    aus = {"lauf": z["lauf"], "stufe": z["stufe"], "t_T": t_T, "Y2": z["n_ende"] == 0, "n_ende": z["n_ende"]}
    if t_T is None or not reihe:
        aus.update({"Y1": None, "Y3": None, "grund": "keine Teilung im Nachrechnen oder keine Zusatzreihe: offen"})
        return aus
    q0 = reihe[0]["Q_box"]
    vorher, ein = False, []
    for i, p in enumerate(reihe):
        if p["t"] >= t_T:
            break
        if p["n"] >= 2:
            vorher = True
        elif p["n"] == 1 and vorher and p["Q_box"] >= VERSCHMOLZEN_Q * q0:
            ein.append(i)
    aus["Y1"] = bool(ein)
    aus["ein_gebiet_t"] = [reihe[i]["t"] for i in ein]
    aus["d12_start"] = reihe[0]["d12"]
    if not ein:
        aus["Y3"] = None
        aus["grund"] = "kein Ein-Gebiet-Zustand vor der Teilung: Y3 offen"
        return aus
    il = ein[-1]
    letzte = reihe[il]["gebiete"][0]
    aus["t_1_erst"], aus["t_1_letzt"] = reihe[ein[0]]["t"], reihe[il]["t"]
    aus["Y3"] = letzte["windung"] == 0
    aus["windung_letzt"], aus["S_min_kreis_letzt"] = letzte["windung"], letzte["S_min_kreis"]
    # beschreibend (kein Kriterium)
    aus["ein_gebiet_proben"] = len(ein)
    best, cur = 1, 1
    for a, c in zip(ein, ein[1:]):
        cur = cur + 1 if c == a + 1 else 1
        best = max(best, cur)
    aus["ein_gebiet_laengste_folge_proben"] = best
    aus["ein_gebiet_laengste_folge_spanne"] = DICHT_DT * (best - 1)
    aus["ein_gebiet_windungen"] = [[reihe[i]["t"], reihe[i]["gebiete"][0]["windung"],
                                    reihe[i]["gebiete"][0]["S_min_kreis"]] for i in ein]
    aus["ein_gebiet_Q_anteil"] = [round(reihe[i]["gebiete"][0]["Q"] / reihe[i]["Q_box"], 4) for i in ein]
    aus["ein_gebiet_erste_windung0"] = next((reihe[i]["t"] for i in ein if reihe[i]["gebiete"][0]["windung"] == 0),
                                            None)
    vor = [p["d12"] for p in reihe[:ein[0]] if p["d12"] is not None]
    aus["d12_min_vor_ein"] = min(vor) if vor else None
    if il + 1 < len(reihe):
        p = reihe[il + 1]
        aus["nach_letztem"] = {"t": p["t"], "n": p["n"], "Q_box": p["Q_box"], "d12": p["d12"],
                               "gebiete": [[gg["Q"], gg["windung"], gg["X"], gg["Y"]] for gg in p["gebiete"]]}
    nach = next((p for p in reihe[il + 1:] if p["n"] >= 2), None)
    if nach is not None:
        aus["bruchstuecke"] = {"t": nach["t"], "n": nach["n"], "d12": nach["d12"],
                               "gebiete": [[gg["Q"], gg["windung"], gg["X"], gg["Y"], gg["S_min_kreis"]]
                                           for gg in nach["gebiete"]],
                               "Q_durch_Q_m1": [round(gg["Q"] / z["Q_m1"], 4) for gg in nach["gebiete"]],
                               "Q_durch_Q_nachbar": [round(gg["Q"] / z["Q_nachbar"], 4) for gg in nach["gebiete"]]}
    return aus


def stufe_urteil(ys, schluessel):
    werte = [y.get(schluessel) for y in ys]
    if not werte or any(w is None for w in werte):
        return None
    return all(werte)


def gesamt(g, f, f_da):
    if g is None:
        return "offen"
    if not f_da:
        return ("eingetroffen" if g else "nicht eingetroffen") + " (nur grob, fein fehlt)"
    if f is None:
        return "offen (fein offen)"
    if g == f:
        return "eingetroffen" if g else "nicht eingetroffen"
    return "offen (grob und fein verschieden)"


def bedeutung(y1, y2):
    if y1 == "eingetroffen" and y2 == "eingetroffen":
        return ("Y1 und Y2 treffen ein: keine Groessengrenze mit Teilung, sondern Instabilitaet nach dem Verschmelzen "
                "(der Ball zerstreut sich). Bio 28 wird verworfen; Befund 'gemischter Ball zerfaellt' notieren [H].")
    if y1 == "eingetroffen" and y2 == "nicht eingetroffen":
        return "Y1 trifft ein, Y2 nicht (stabile Toechter): Groessengrenze mit Teilung gesehen, weiter."
    if y1 == "nicht eingetroffen":
        return "Y1 trifft nicht ein: die 'Teilung' waren unverschmolzene Nachbarn; Bio 28 wird verworfen."
    return "offen: Bedeutung nach Karte nicht zuordenbar"


def auswerten(roh, ref):
    ys = {}
    for stufe, liste in roh["ergebnis"].items():
        ys[stufe] = [y for y in (y_lauf(z, roh["dicht"][stufe].get(z["lauf"], [])) for z in liste) if y is not None]
    je = {stufe: {k: stufe_urteil(yl, k) for k in ("Y1", "Y2", "Y3")} for stufe, yl in ys.items()}
    k0 = k0_vergleich(roh["ergebnis"], ref) if ref else None
    f_da = "fein" in je
    g_, f_ = je.get("grob", {}), je.get("fein", {})
    y = {"Y0": ("eingetroffen" if (k0 and k0["bestanden"]) else ("nicht eingetroffen" if k0 else "offen (keine Referenz)"))}
    for k in ("Y1", "Y2", "Y3"):
        y[k] = gesamt(g_.get(k), f_.get(k), f_da)
    return {"y_je_lauf": ys, "y_je_stufe": je, "Y": y, "K0": k0, "bedeutung": bedeutung(y["Y1"], y["Y2"])}


def selbsttest():
    """Nur im Rauchlauf: Auswertungspfade mit einer erfundenen Reihe (keine Messdaten)."""
    reihe = []
    for i, n in enumerate([2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2]):
        geb = [{"Q": 10.0 - j, "windung": (1 if i < 5 else 0), "S_min_kreis": 0.1, "X": float(j), "Y": 0.0,
                "Jspin_Q": 0.5, "r_mittel": 2.0, "flaeche": 3.0, "E": 9.0} for j in range(n)]
        paare = [[a, c, float(c - a)] for a in range(n) for c in range(a + 1, n)]
        reihe.append({"t": i * DICHT_DT, "Q_box": 20.0, "n": n, "gebiete": geb, "abstaende": paare,
                      "d12": paare[0][2] if paare else None})
    z = {"lauf": "synthetisch", "stufe": "grob", "nachbarn": 1, "t_teilung_danach": 4.0, "n_ende": 0,
         "Q_m1": 10.0, "Q_nachbar": 5.0}
    y = y_lauf(z, reihe)
    soll = {"Y1": True, "Y3": True, "ein_gebiet_t": [1.5, 2.0, 2.5, 3.5], "ein_gebiet_erste_windung0": 2.5,
            "ein_gebiet_laengste_folge_proben": 3}
    return {"ergebnis": y, "soll": soll, "ok": all(y.get(k) == v for k, v in soll.items())}


# ---------------------------------------------------------------- Text

def f_t(x):
    return "None" if x is None else f"{x:g}"


def text_bericht(roh, aus):
    zeilen = [f"Runde 21 bio28-weiter: Bio 28 nachgerechnet mit Zusatzreihe. Start {roh['start']}, Ende {roh['ende']}, "
              f"{roh['geraet']}, torch {roh['torch']}" + (" RAUCHLAUF: Zahlen ungueltig" if roh["rauch"] else "")]
    zeilen.append("Dauer [s]: " + ", ".join(f"{k} {v:.1f}" for k, v in roh["dauer_s"].items()))
    zeilen.append("Analysen: " + ", ".join(f"{k} {v}" for k, v in roh["analysen"].items()))
    zeilen.append(f"sha256: {json.dumps(roh['sha256'])}")
    zeilen += roh["notizen"]
    zeilen.append("Stufe Lauf | Q_m1 + k Q_0 | J/Q | t verschmolzen | Windung groesstes (Ende; je gesehen) | "
                  "t Teilung danach | n Ende | Q-Verlust")
    for stufe, liste in roh["ergebnis"].items():
        for z in liste:
            zeilen.append(f"  {stufe} {z['lauf']} | {z['Q_m1']:.1f} + {z['nachbarn']} x {z['Q_nachbar']:.1f} | "
                          f"{z['J_zu_Q_start']:.3f} | {z['t_verschmolzen']} | {z['windung_groesstes_ende']}; "
                          f"{z['windung_groesstes_verlauf']} | {z['t_teilung_danach']} | {z['n_ende']} | "
                          f"{z['Q_box_verlust']:.1e}")
    if aus is not None:
        k0 = aus.get("K0")
        if k0:
            zeilen.append(f"K0 (Toleranz {K0_TOL:g} relativ, n_ende gleich): bestanden={k0['bestanden']} "
                          f"(Zeilen {len(k0['zeilen'])} von {k0['zeilen_erwartet']})")
            for x in k0["zeilen"]:
                if "pruef" not in x:
                    zeilen.append(f"  {x['stufe']} {x['lauf']}: {x.get('grund')}")
                    continue
                teile = [f"{f} r5 {f_t(v['r5'])} r21 {f_t(v['r21'])} {'ok' if v['ok'] else 'NEIN'}"
                         for f, v in x["pruef"].items()]
                zeilen.append(f"  {x['stufe']} {x['lauf']}: " + "; ".join(teile)
                              + f" | 5er-Gebiete identisch {x['gebiete_5er_identisch']}")
        for stufe, yl in aus["y_je_lauf"].items():
            for y in yl:
                zeilen.append(f"Y {stufe} {y['lauf']}: t_T {f_t(y['t_T'])}, Y1 {y['Y1']}, Y2 {y['Y2']} "
                              f"(n_ende {y['n_ende']}), Y3 {y['Y3']}; Ein-Gebiet t {y.get('ein_gebiet_t')}; "
                              f"Windungen {y.get('ein_gebiet_windungen')}; Q-Anteil {y.get('ein_gebiet_Q_anteil')}; "
                              f"d12 Start {y.get('d12_start')}, min vor Ein {y.get('d12_min_vor_ein')}; "
                              f"Bruchstuecke {json.dumps(y.get('bruchstuecke'))}")
        zeilen.append("Y je Stufe: " + json.dumps(aus["y_je_stufe"]))
        zeilen.append("Y gesamt: " + json.dumps(aus["Y"]))
        zeilen.append("Bedeutung (Karte): " + aus["bedeutung"])
    zeilen.append(f"Zusatzreihe (t, n, Q_box | je Gebiet Q, Windung, Schwerpunkt, S_min_kreis | d12):")
    for stufe, laeufe in roh["dicht"].items():
        for name, reihe in laeufe.items():
            zeilen.append(f"  [{stufe} {name}]")
            for p in reihe:
                geb = "; ".join(f"Q {gg['Q']:7.2f} w {gg['windung']} ({gg['X']:6.2f},{gg['Y']:6.2f}) "
                                f"Smin {gg['S_min_kreis']:.3f}" for gg in p["gebiete"])
                zeilen.append(f"  {p['t']:5.1f} n {p['n']} Qb {p['Q_box']:7.2f} | {geb} | d12 {p['d12']}")
    return "\n".join(zeilen)


# ---------------------------------------------------------------- Ablauf

def rechnen(args, out):
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    stufen = ("grob",) if args.rauch else (("grob", "fein") if args.stufe == "beide" else (args.stufe,))
    t_end = RAUCH_T if args.rauch else r5.T5_T
    dicht_bis = min(DICHT_BIS, t_end)
    start = r5.jetzt()
    print(f"bio28-weiter Start {start} auf {r5.geraet_name()}, torch {torch.__version__}, Stufen {stufen}, "
          f"t_end {t_end}, Zusatzreihe bis {dicht_bis} alle {DICHT_DT}" + (" RAUCHLAUF" if args.rauch else ""),
          flush=True)
    dauer, analysen, notizen = {}, {}, []
    t0 = r5.uhr()
    prof = r5.profile_holen([(w2, m) for _, w2, _ in r5.T5_LAEUFE for m in (0, 1)])
    dauer["schiessen_s"] = r5.uhr() - t0
    print(f"Schiessen fertig nach {dauer['schiessen_s']:.1f} s", flush=True)
    ergebnis, dicht_alle, schw = {}, {}, {}
    for stufe, dx, dt in r5.STUFEN:
        if stufe not in stufen:
            continue
        laeufe = r5.auswahl(r5.T5_LAEUFE, stufe, r5.T5_FEIN, prof, lambda l: [(l[1], 0), (l[1], 1)], notizen)
        if not laeufe:
            continue
        g = r5.Gitter(r5.L_STD, dx)
        psis, vels, abst = [], [], []
        for name, w2, k in laeufe:
            p1, p0 = prof[(w2, 1)], prof[(w2, 0)]
            dd = p1["R_halb"] + p0["R_halb"] + r5.T5_LUECKE
            abst.append(dd)
            p_, v_ = r5.ball_feld(g, p1, 1)
            for x0, ph in ((dd, 0.0), (-dd, math.pi))[:k]:
                a, b_ = r5.ball_feld(g, p0, 0, x0, 0.0, ph)
                p_, v_ = p_ + a, v_ + b_
            psis.append(p_)
            vels.append(v_)
        psi = torch.cat(psis).contiguous()
        vel = torch.cat(vels).contiguous()
        zeiten = {"analyse_s": 0.0, "analysen": 0}
        t0 = r5.uhr()
        t, daten, verlauf, dicht, schwelle, q_min = lauf_dicht(g, psi, vel, dt, t_end, dicht_bis, zeiten)
        dauer[f"entwicklung_{stufe}_s"] = r5.uhr() - t0
        dauer[f"analyse_{stufe}_s"] = zeiten["analyse_s"]
        analysen[stufe] = zeiten["analysen"]
        print(f"Entwicklung {stufe} fertig nach {dauer[f'entwicklung_{stufe}_s']:.1f} s "
              f"(davon Analysen {zeiten['analyse_s']:.1f} s, {zeiten['analysen']} Aufrufe)", flush=True)
        dicht_alle[stufe] = {}
        schw[stufe] = {}
        for b, (name, w2, k) in enumerate(laeufe):
            ergebnis.setdefault(stufe, []).append(zusammenfassung(name, w2, k, stufe, abst[b], prof, t, daten, b,
                                                                  verlauf[b]))
            dicht_alle[stufe][name] = [probe_dicht(tt, qq, gb) for tt, qq, gb in dicht[b]]
            schw[stufe][name] = {"schwelle_S_glatt": schwelle[b], "q_min": q_min[b]}
    pfad_skript = os.path.abspath(__file__)
    roh = {"test": "bio28-weiter", "start": start, "ende": r5.jetzt(), "rauch": args.rauch, "dauer_s": dauer,
           "analysen": analysen, "geraet": r5.geraet_name(), "torch": torch.__version__, "notizen": notizen,
           "sha256": {"bio28_weiter.py": sha(pfad_skript), "r5_2d_a.py": sha(r5.__file__), "ref": sha(args.ref)},
           "parameter": {"T": r5.T5_T, "t_end": t_end, "luecke": r5.T5_LUECKE, "L": r5.L_STD, "stufen": r5.STUFEN,
                         "dicht_dt": DICHT_DT, "dicht_bis": dicht_bis, "schwelle_rel": r5.SCHWELLE_REL,
                         "blur": r5.BLUR, "q_min_rel": r5.Q_MIN_REL, "n_theta": r5.N_THETA,
                         "analyse_dt": r5.ANALYSE_DT, "dauer_k": r5.DAUER_K, "T_MEAS_original": r5.T_MEAS},
           "profile": [r5.profil_info(prof[(w2, m)]) for w2 in (0.60, 0.75) for m in (0, 1)],
           "schwellen": schw, "ergebnis": ergebnis, "dicht": dicht_alle}
    with open(os.path.join(out, "bio28_weiter_roh.json"), "w") as fh:
        json.dump(roh, fh, indent=1)
    print("Rohdaten geschrieben", flush=True)
    return roh


def main():
    ap = argparse.ArgumentParser(description="Runde 21 bio28-weiter: Bio 28 mit Gebiets-Zeitreihe 0 bis 30")
    ap.add_argument("--rauch", action="store_true", help="nur grob, t_end = 1, plus Selbsttest der Auswertung")
    ap.add_argument("--stufe", choices=["grob", "fein", "beide"], default="beide")
    ap.add_argument("--out", default=None)
    ap.add_argument("--ref", default=os.path.join(HIER, "r5_groesse_ergebnis.json"))
    ap.add_argument("--auswerten", default=None, help="nur Auswertung einer vorhandenen Rohdatei")
    args = ap.parse_args()
    out = args.out or os.path.join(HIER, "rauch" if args.rauch else "ausgabe")
    os.makedirs(out, exist_ok=True)
    if args.auswerten:
        with open(args.auswerten) as fh:
            roh = json.load(fh)
    else:
        roh = rechnen(args, out)
    aus, fehler = None, None
    try:
        ref = None
        if not roh["rauch"] and os.path.exists(args.ref):
            with open(args.ref) as fh:
                ref = json.load(fh)
        aus = auswerten(roh, ref)
        if roh["rauch"]:
            aus["selbsttest"] = selbsttest()
            print("Selbsttest Auswertung (erfundene Reihe): " + json.dumps(aus["selbsttest"]), flush=True)
    except Exception:  # Rohdaten sind schon geschrieben; Auswertung dann mit --auswerten wiederholen
        fehler = traceback.format_exc()
        print("FEHLER in der Auswertung:\n" + fehler, flush=True)
    with open(os.path.join(out, "bio28_weiter_ergebnis.json"), "w") as fh:
        json.dump({"auswertung": aus, "fehler_auswertung": fehler, "start": roh["start"], "ende": roh["ende"],
                   "rauch": roh["rauch"], "sha256": roh["sha256"]}, fh, indent=1)
    text = text_bericht(roh, aus)
    with open(os.path.join(out, "bio28_weiter_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    kurz = text.split("Zusatzreihe (t, n")[0]
    print(kurz, flush=True)
    if fehler:
        raise SystemExit("Auswertung mit Fehler (Rohdaten vorhanden)")


if __name__ == "__main__":
    main()
