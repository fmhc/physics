#!/usr/bin/env python3
"""Runde 22 (v3), Karte bio28b (RUNDE-22/bio28b/KARTE.md): Ueberleben die Toechter eines verschmolzenen Drehballs
ohne Randverlust?

Rechnet Karte 5 (groesse, Bio 28) aus RUNDE-05/r5-2d-a/r5_2d_a.py wie RUNDE-21/bio28-weiter/bio28_weiter.py nach:
unveraenderter Code (r5_2d_a.py nur importiert), unveraenderte Parameter (Profile, Abstand D, Phasen, dx, dt, Schwelle,
Glaettung, q_min, Windung), aber
  - Box mit dreifacher Kantenlaenge: halbe Laenge L = 3 x 38,4 = 115,2 (n 768 grob, 1152 fein); Randschicht
    unveraendert 8 breit, also ab Tiefe max(|x|, |y|) = 107,2 (PLAN.md Abschnitt 2: doppelte Kantenlaenge reicht nach
    den R21-Bahnen nicht). Gitter(L, dx) nimmt L als Argument; r5_2d_a.py bleibt unveraendert.
  - T = 300 statt 600 (Karte).
  - Gebietsanalyse wie R21: Messtakt 0,5; Analyse an allen Vielfachen von 5 und an jedem Messpunkt bis t = 30;
    dazu je Analyse die groesste Tiefe max(|x|, |y|) der Gebietsmaske (Box-Pruefung).
  - Klassifikator aus RUNDE-06/kf5/kf5_geburt.py (unveraendert importiert, familie_2d_m0.json daneben), aufgerufen wie
    in KF-EICH (RUNDE-21/kf-eich/kf_eich.py): Fenster [T - 40, T] fuer T = 100, 200, 300; am Fensterbeginn
    kg.analyse_arm (S0 = 0,3 Haupt, 0,1 Zusatz), dann kg.fenster_probe alle 1 (erste Probe am Fensterbeginn), am Ende
    kg.fenster_auswerten. Felder s, rho, e aus kg.dichten (nl = 1) auf kg.Gitter(2 L, dx); dieses hat dieselben
    Gitterpunkte und dieselbe [y, x]-Anordnung wie r5.Gitter(L, dx) (wird im Lauf geprueft).

Gruppen (je Aufruf hoechstens 10 min):
  grob       die vier gefuetterten Laeufe, grob (B = 4)
  fein-w60   w60_nachbarn1 und w60_nachbarn2, fein (B = 2)
  fein-w75   w75_nachbarn1 und w75_nachbarn2, fein (B = 2)
  kontrolle  einzelne m = 0-Baelle aus R5-Profilen (omega^2 0,60 und 0,70) in der R5-Box (L 38,4), grob und fein:
             Gegenprobe des Klassifikators auf dem R5-Gitter (PLAN.md 4.5)
  rauch      wie grob, volle Box, T = 6, ein Fenster [2, 6]; Zahlen ungueltig; dazu Selbsttest der Auswertung

Aufruf:  python bio28b.py --gruppe GRUPPE [--out ORDNER]
         python bio28b.py --auswerten ORDNER
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import sys  # noqa: E402

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import traceback  # noqa: E402

import torch  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import r5_2d_a as r5  # noqa: E402
import kf5_geburt as kg  # noqa: E402

# ---- feste Parameter (PLAN.md, vor dem ersten echten Lauf) ----
L_GROSS = 3.0 * r5.L_STD          # 115,2; Randschicht ab L_GROSS - r5.SPONGE = 107,2
T_ENDE = 300.0
DICHT_DT = 0.5                    # Messtakt und dichte Reihe wie R21
DICHT_BIS = 30.0
T_URTEIL = (100.0, 200.0, 300.0)  # Klassifikator-Urteile, Fenster [T - 40, T]
FENSTER = kg.FENSTER              # 40
S0_LISTE = (0.3, 0.1)             # 0,3 Haupt (entscheidet D2), 0,1 Zusatz (nur berichtet), wie KF-EICH
S0_HAUPT = 0.3
BALL_SUCH = 5.0                   # Fenstertropfen gehoert zum Stueck, wenn er hoechstens 5 vom Schwerpunkt startet
D_SPUR = 5.0                      # Verfolgung: naechstes Gebiet hoechstens 5 vom letzten Schwerpunkt
K0_TOL = 1.0
D1_ANTEIL = 0.5
GLEICH_Q = 0.01                   # Rangfolge der Stuecke: Q absteigend, Gleichstand (1 %) nach Y absteigend
VERSCHMOLZEN_Q = 0.9              # wie r5.ganz_verschmolzen
R21_ZEITEN = {"w60_nachbarn1": (2.0, 14.0), "w60_nachbarn2": (2.0, 9.0), "w75_nachbarn1": (1.5, 12.5),
              "w75_nachbarn2": (1.5, 7.0)}   # (Verschmelzen, Teilung) aus der dichten Reihe R21, grob und fein gleich
KONTROLLE_W2 = (0.60, 0.70)
RAUCH_T, RAUCH_URTEIL, RAUCH_FENSTER = 6.0, (6.0,), 4.0
ZEITGRENZE_S = 570.0
NAMEN_GEF = ["w60_nachbarn1", "w60_nachbarn2", "w75_nachbarn1", "w75_nachbarn2"]
GRUPPEN = {"grob": ("grob", NAMEN_GEF),
           "fein-w60": ("fein", ["w60_nachbarn1", "w60_nachbarn2"]),
           "fein-w75": ("fein", ["w75_nachbarn1", "w75_nachbarn2"]),
           "rauch": ("grob", NAMEN_GEF)}


def sha(pfad):
    try:
        with open(pfad, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()
    except OSError:
        return None


def frei(pfad):
    if os.path.exists(pfad) or os.path.exists(pfad + ".tmp"):
        raise SystemExit(f"{pfad} existiert schon: nichts ueberschreiben")
    return pfad


def schreibe(pfad, obj):
    frei(pfad)
    with open(pfad + ".tmp", "w") as fh:
        if isinstance(obj, str):
            fh.write(obj)
        else:
            json.dump(obj, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)


def gebiet_aus(d):
    return {"Q": round(d["Q"], 4), "E": round(d["E"], 4), "X": round(d["X"], 3), "Y": round(d["Y"], 3),
            "vx": round(d["vx"], 5), "vy": round(d["vy"], 5), "Jspin_Q": round(d["Jspin_Q"], 4),
            "r_mittel": round(d["r_mittel"], 3), "flaeche": round(d["flaeche"], 2), "windung": d.get("windung"),
            "S_min_kreis": round(d.get("S_min_kreis", -1.0), 6), "spannt": bool(d["spannt_x"] or d["spannt_y"])}


# ---------------------------------------------------------------- Lauf mit Analyse und Klassifikator-Fenstern

def lauf_messen(g, gk, psi, vel, dt, t_end, t_urteil, fenster, zeiten, t_aufruf, waechter):
    """Wie bio28_weiter.lauf_dicht (Messtakt 0,5; Gebietsanalyse an allen Vielfachen von 5 und an jedem Messpunkt bis
    DICHT_BIS), dazu je Analyse die groesste Masken-Tiefe und die Klassifikator-Fenster wie KF-EICH."""
    B = psi.shape[0]
    s0, rho0, _, _, _, _ = r5.dichten(g, psi, vel)
    schwelle = r5.SCHWELLE_REL * r5.unschaerfe(g, s0).amax((1, 2))
    q_min = (r5.Q_MIN_REL * rho0.sum((1, 2)) * g.dA).tolist()
    tiefe = torch.maximum(g.X2.abs(), g.Y2.abs())
    null = torch.zeros_like(tiefe)
    fam = kg.Familie()
    nl = torch.ones((B, 1, 1), dtype=r5.F64, device=r5.DEV)
    reihe = [[] for _ in range(B)]
    zaehler = [0]
    alle5 = int(round(r5.ANALYSE_DT / DICHT_DT))
    n_dicht = int(round(DICHT_BIS / DICHT_DT))
    je_fen = int(round(kg.DT_FENSTER / DICHT_DT))
    fen_start = {int(round((T - fenster) / DICHT_DT)): T for T in t_urteil}
    fen_ende = {int(round(T / DICHT_DT)): T for T in t_urteil}
    z_waechter = int(round(40.0 / DICHT_DT))
    aktiv, fen_erg = {}, [{} for _ in range(B)]
    t_lauf = r5.uhr()

    def messen(psi, vel):
        d = r5.dichten(g, psi, vel)
        s, rho, e, _, _, jz = d
        spalten = [rho.sum((1, 2)) * g.dA, e.sum((1, 2)) * g.dA, jz.sum((1, 2)) * g.dA, s.amax((1, 2))]
        z = zaehler[0]
        t = z * DICHT_DT
        if z % alle5 == 0 or z <= n_dicht:
            ta = r5.uhr()
            maske = r5.unschaerfe(g, s) > schwelle.view(-1, 1, 1)
            gebiete = r5.analyse(g, psi, d, maske, q_min, True)
            tmax = torch.where(maske, tiefe, null).amax((1, 2)).tolist()
            qbox = spalten[0].tolist()
            for b, geb in enumerate(gebiete):
                reihe[b].append({"t": t, "Q_box": round(qbox[b], 6), "tiefe_max": round(tmax[b], 3),
                                 "gebiete": [gebiet_aus(x) for x in geb]})
            zeiten["analyse_s"] += r5.uhr() - ta
            zeiten["analysen"] += 1
        neu = z in fen_start
        if neu or any((z - a["start"]) % je_fen == 0 for a in aktiv.values()):
            tf = r5.uhr()
            ks, krho, ke = kg.dichten(gk, psi, vel, nl)
            if neu:
                a = {"start": z, "fzs": {}, "zeilen": {}}
                for b in range(B):
                    for S0 in S0_LISTE:
                        zeile, _, tropfen = kg.analyse_arm(gk, ks[b], krho[b], ke[b], psi[b], S0, fam, None)
                        a["fzs"][(b, S0)] = kg.fenster_start(tropfen)
                        a["zeilen"][(b, S0)] = zeile
                aktiv[fen_start[z]] = a
            for a in aktiv.values():
                if (z - a["start"]) % je_fen == 0:
                    for (b, S0), fz in a["fzs"].items():
                        if fz is not None:
                            kg.fenster_probe(gk, fz, ks[b], krho[b], ke[b], psi[b])
            if z in fen_ende:
                T = fen_ende[z]
                a = aktiv.pop(T)
                for (b, S0), fz in a["fzs"].items():
                    fen = kg.fenster_auswerten(fz, T - fenster, kg.DT_FENSTER, fam, gk.box)
                    fen_erg[b].setdefault(f"{T:g}", {})[f"{S0:g}"] = {"zeile": a["zeilen"][(b, S0)], "fenster": fen}
            zeiten["fenster_s"] += r5.uhr() - tf
            zeiten["fensterproben"] += 1
        if waechter and z == z_waechter:
            verg = r5.uhr() - t_lauf
            entw = verg - zeiten["analyse_s"] - zeiten["fenster_s"]
            je_analyse = zeiten["analyse_s"] / max(zeiten["analysen"], 1)
            rest = (entw / t * (t_end - t) + je_analyse * (t_end - t) / r5.ANALYSE_DT
                    + 1.5 * je_analyse * len(t_urteil) * (fenster / kg.DT_FENSTER + 1))
            prognose = (r5.uhr() - t_aufruf) + rest
            zeiten["prognose_s"] = prognose
            print(f"  Prognose Gesamtdauer des Aufrufs {prognose:.0f} s (bei t {t:g})", flush=True)
            if prognose > ZEITGRENZE_S:
                raise SystemExit(f"Abbruch: Prognose {prognose:.0f} s > {ZEITGRENZE_S:.0f} s; Aufruf teilen (PLAN 5)")
        zaehler[0] += 1
        return torch.stack(spalten, dim=1)

    alt = r5.T_MEAS
    r5.T_MEAS = DICHT_DT
    try:
        t, daten = r5.entwickeln(g, psi, vel, dt, t_end, messen)
    finally:
        r5.T_MEAS = alt
    if aktiv:
        raise RuntimeError(f"Fenster nicht abgeschlossen: {list(aktiv)}")
    return t, daten, reihe, fen_erg, schwelle.tolist(), q_min


def rechnen(args, out):
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    kg.DEV = torch.device("cuda")
    t_aufruf = r5.uhr()
    gruppe = args.gruppe
    rauch = gruppe == "rauch"
    start = r5.jetzt()
    pfad = frei(os.path.join(out, f"{gruppe}_roh.json"))
    print(f"bio28b {gruppe}: Start {start} auf {r5.geraet_name()}, torch {torch.__version__}", flush=True)
    dauer = {}
    t0 = r5.uhr()
    if gruppe == "kontrolle":
        prof = r5.profile_holen([(w2, 0) for w2 in KONTROLLE_W2])
    else:
        prof = r5.profile_holen([(w2, m) for _, w2, _ in r5.T5_LAEUFE for m in (0, 1)])
    dauer["schiessen_s"] = r5.uhr() - t0
    print(f"Schiessen fertig nach {dauer['schiessen_s']:.1f} s", flush=True)
    if not all(p["gueltig"] for p in prof.values()):
        raise SystemExit("Profil ungueltig: Abbruch")
    t_end = RAUCH_T if rauch else T_ENDE
    t_urteil = RAUCH_URTEIL if rauch else T_URTEIL
    fenster = RAUCH_FENSTER if rauch else FENSTER
    if gruppe == "kontrolle":
        aufgaben = [(stufe, dx, dt, r5.L_STD, [(f"einzel_w{int(round(100 * w2))}", w2, None) for w2 in KONTROLLE_W2])
                    for stufe, dx, dt in r5.STUFEN]
    else:
        stufe_g, namen = GRUPPEN[gruppe]
        laeufe = [l for l in r5.T5_LAEUFE if l[0] in namen]
        aufgaben = [(stufe, dx, dt, L_GROSS, laeufe) for stufe, dx, dt in r5.STUFEN if stufe == stufe_g]
    erg, zeiten_alle = {}, {}
    for stufe, dx, dt, L, laeufe in aufgaben:
        g = r5.Gitter(L, dx)
        gk = kg.Gitter(2.0 * L, dx)
        if gk.n != g.n or not torch.equal(gk.x1, g.x.reshape(-1)):
            raise SystemExit("kg.Gitter und r5.Gitter haben verschiedene Gitterpunkte: Abbruch")
        psis, vels, info = [], [], []
        for name, w2, k in laeufe:
            if k is None:
                p_, v_ = r5.ball_feld(g, prof[(w2, 0)], 0)
                info.append({"lauf": name, "omega2": w2, "nachbarn": None, "Q_profil": prof[(w2, 0)]["Q"]})
            else:
                p1, p0 = prof[(w2, 1)], prof[(w2, 0)]
                dd = p1["R_halb"] + p0["R_halb"] + r5.T5_LUECKE
                p_, v_ = r5.ball_feld(g, p1, 1)
                for x0, ph in ((dd, 0.0), (-dd, math.pi))[:k]:
                    a, b_ = r5.ball_feld(g, p0, 0, x0, 0.0, ph)
                    p_, v_ = p_ + a, v_ + b_
                info.append({"lauf": name, "omega2": w2, "nachbarn": k, "abstand": dd, "Q_m1": p1["Q"],
                             "Q_nachbar": p0["Q"]})
            psis.append(p_)
            vels.append(v_)
        psi = torch.cat(psis).contiguous()
        vel = torch.cat(vels).contiguous()
        del psis, vels
        zeiten = {"analyse_s": 0.0, "analysen": 0, "fenster_s": 0.0, "fensterproben": 0}
        t0 = r5.uhr()
        t, daten, reihe, fen_erg, schwelle, q_min = lauf_messen(
            g, gk, psi, vel, dt, t_end, t_urteil, fenster, zeiten, t_aufruf,
            waechter=(gruppe not in ("kontrolle", "rauch")))
        dauer[f"entwicklung_{stufe}_s"] = r5.uhr() - t0
        n_schritte = int(round(t_end / dt))
        zeiten["ms_je_schritt"] = ((dauer[f"entwicklung_{stufe}_s"] - zeiten["analyse_s"] - zeiten["fenster_s"])
                                   / n_schritte * 1e3)
        zeiten["n"] = g.n
        zeiten["B"] = psi.shape[0]
        zeiten_alle[stufe] = zeiten
        print(f"Entwicklung {stufe} (L {L:g}, n {g.n}, B {psi.shape[0]}) fertig nach "
              f"{dauer[f'entwicklung_{stufe}_s']:.1f} s; Analysen {zeiten['analysen']} in {zeiten['analyse_s']:.1f} s; "
              f"Fensterproben {zeiten['fensterproben']} in {zeiten['fenster_s']:.1f} s; "
              f"{zeiten['ms_je_schritt']:.2f} ms je Schritt", flush=True)
        alle5 = int(round(r5.ANALYSE_DT / DICHT_DT))
        for b, inf in enumerate(info):
            qb = [[round(i * DICHT_DT, 3), round(daten[i, b, 0].item(), 6)] for i in range(0, daten.shape[0], alle5)]
            inf.update({"stufe": stufe, "L": L, "dx": dx, "dt": dt, "n": g.n, "schwelle_S_glatt": schwelle[b],
                        "q_min": q_min[b], "Q_box_start": daten[0, b, 0].item(), "Q_box_ende": daten[-1, b, 0].item(),
                        "E_box_start": daten[0, b, 1].item(), "E_box_ende": daten[-1, b, 1].item(),
                        "J_box_start": daten[0, b, 2].item(), "J_box_ende": daten[-1, b, 2].item(),
                        "Q_box_5er": qb, "reihe": reihe[b], "fenster": fen_erg[b]})
            erg.setdefault(stufe, []).append(inf)
        del psi, vel, daten
    roh = {"test": "bio28b", "gruppe": gruppe, "start": start, "ende": r5.jetzt(), "rauch": rauch, "dauer_s": dauer,
           "zeiten": zeiten_alle, "geraet": r5.geraet_name(), "torch": torch.__version__,
           "gpu_max_mb": torch.cuda.max_memory_allocated() / 2 ** 20,
           "sha256": {"bio28b.py": sha(os.path.abspath(__file__)), "r5_2d_a.py": sha(r5.__file__),
                      "kf5_geburt.py": sha(kg.__file__), "familie_2d_m0.json": sha(kg.FAMILIE_DATEI)},
           "parameter": {"L_gross": L_GROSS, "L_kontrolle": r5.L_STD, "sponge": r5.SPONGE, "t_end": t_end,
                         "t_urteil": list(t_urteil), "fenster": fenster, "dicht_dt": DICHT_DT, "dicht_bis": DICHT_BIS,
                         "stufen": r5.STUFEN, "luecke": r5.T5_LUECKE, "schwelle_rel": r5.SCHWELLE_REL,
                         "blur": r5.BLUR, "q_min_rel": r5.Q_MIN_REL, "n_theta": r5.N_THETA,
                         "analyse_dt": r5.ANALYSE_DT, "S0_liste": list(S0_LISTE), "kf_FAM_TOL": kg.FAM_TOL,
                         "kf_KOMPAKT_FAMILIE": kg.KOMPAKT_FAMILIE, "kf_A_MIN": kg.A_MIN, "kf_R_PLUS": kg.R_PLUS,
                         "kf_Q_SCHWANK": kg.Q_SCHWANK, "kf_DT_FENSTER": kg.DT_FENSTER},
           "profile": [r5.profil_info(p) for p in prof.values()], "ergebnis": erg}
    roh["dauer_s"]["gesamt_s"] = r5.uhr() - t_aufruf
    schreibe(pfad, roh)
    print(f"Rohdaten geschrieben: {pfad}; Gesamtdauer {roh['dauer_s']['gesamt_s']:.1f} s; GPU max "
          f"{roh['gpu_max_mb']:.0f} MB", flush=True)
    return roh


# ---------------------------------------------------------------- Auswertung (PLAN.md Abschnitt 4, vorab)

def zeiten_k0(reihe):
    """Verschmelzen = erste Probe der dichten Reihe mit genau einem Gebiet nach einer mit mindestens zwei, bei
    Q_box >= 0,9 Q_box(0); Teilung = erste Probe danach mit mindestens zwei Gebieten (Wortlaut R21)."""
    q0 = reihe[0]["Q_box"]
    dicht = [p for p in reihe if p["t"] <= DICHT_BIS + 1e-9]
    vorher, t_v = False, None
    for p in dicht:
        n = len(p["gebiete"])
        if n >= 2:
            vorher = True
        elif n == 1 and vorher and p["Q_box"] >= VERSCHMOLZEN_Q * q0:
            t_v = p["t"]
            break
    t_teil = None
    if t_v is not None:
        t_teil = next((p["t"] for p in dicht if p["t"] > t_v and len(p["gebiete"]) >= 2), None)
    return t_v, t_teil


def rangfolge(geb):
    idx = sorted(range(len(geb)), key=lambda i: -geb[i]["Q"])
    for _ in range(len(idx)):
        for a in range(len(idx) - 1):
            i, j = idx[a], idx[a + 1]
            if (abs(geb[i]["Q"] - geb[j]["Q"]) <= GLEICH_Q * max(geb[i]["Q"], geb[j]["Q"])
                    and geb[j]["Y"] > geb[i]["Y"]):
                idx[a], idx[a + 1] = j, i
    return idx


def verfolgen(reihe, t_teil):
    """Stuecke = Gebiete zur Teilungszeit (Rangfolge); je spaetere Analyse das naechste Gebiet (Schwerpunkt) hoechstens
    D_SPUR vom letzten bekannten Schwerpunkt des Stuecks, sonst 'nicht gefunden' (letzte Lage bleibt)."""
    p0 = next(p for p in reihe if abs(p["t"] - t_teil) < 1e-9)
    stuecke = [p0["gebiete"][i] for i in rangfolge(p0["gebiete"])]
    lage = [(s["X"], s["Y"]) for s in stuecke]
    spur = []
    for p in reihe:
        if p["t"] <= t_teil + 1e-9:
            continue
        zu = []
        for i, (x, y) in enumerate(lage):
            best, dbest = None, None
            for j, gg in enumerate(p["gebiete"]):
                dd = math.hypot(gg["X"] - x, gg["Y"] - y)
                if dd <= D_SPUR and (dbest is None or dd < dbest):
                    best, dbest = j, dd
            zu.append(best)
            if best is not None:
                lage[i] = (p["gebiete"][best]["X"], p["gebiete"][best]["Y"])
        spur.append({"t": p["t"], "zuordnung": zu, "lage": [list(xy) for xy in lage]})
    return stuecke, spur


def bei(liste, T):
    return next((p for p in liste if abs(p["t"] - T) < 1e-9), None)


def klassifikator(lauf, T, S0, x, y):
    """Fenstertropfen des Klassifikators (Fenster [T - 40, T]), der am naechsten an (x, y) startet, hoechstens
    BALL_SUCH entfernt (wie KF-EICH)."""
    eintrag = lauf.get("fenster", {}).get(f"{T:g}", {}).get(f"{S0:g}")
    if eintrag is None:
        return {"klasse": "kein Fenster"}
    beste, dbest = None, None
    for tr in eintrag["fenster"].get("tropfen", []):
        if tr.get("x0") is None or tr.get("y0") is None:
            continue
        dd = math.hypot(tr["x0"] - x, tr["y0"] - y)
        if dd <= BALL_SUCH and (dbest is None or dd < dbest):
            beste, dbest = tr, dd
    if beste is None:
        return {"klasse": "kein Tropfen", "N_tropfen": len(eintrag["fenster"].get("tropfen", []))}
    ztr = eintrag["zeile"].get("tropfen", {})
    k = beste["k"]
    aus = {x_: beste.get(x_) for x_ in ("klasse", "rund", "Q_net", "E_zu_Q", "E_zu_Q_familie", "omega_ruhe", "u_omega",
                                       "omega_familie_bei_Q", "v", "Q_schwankung", "verloren", "stoss", "dQ",
                                       "dQ_band", "S_max_mittel")}
    aus["rmax_zu_ra"] = (ztr.get("rmax_zu_ra") or [None] * (k + 1))[k]
    aus["abstand"] = round(dbest, 3)
    return aus


def lauf_auswerten(lauf):
    name, stufe, L = lauf["lauf"], lauf["stufe"], lauf["L"]
    reihe = lauf["reihe"]
    t_v, t_teil = zeiten_k0(reihe)
    ref = R21_ZEITEN.get(name)
    k0 = {"t_verschmolzen": t_v, "t_teilung": t_teil, "r21": ref,
          "ok": (ref is not None and t_v is not None and t_teil is not None and abs(t_v - ref[0]) <= K0_TOL
                 and abs(t_teil - ref[1]) <= K0_TOL)}
    grenze = L - r5.SPONGE
    t_max = max(p["t"] for p in reihe)
    tiefe = max(p["tiefe_max"] for p in reihe)
    box = {"tiefe_max": tiefe, "grenze": grenze, "ok": tiefe < grenze, "t_ende": t_max,
           "Q_box_start": lauf["Q_box_start"], "Q_box_ende": lauf["Q_box_ende"],
           "Q_box_ende_anteil": lauf["Q_box_ende"] / lauf["Q_box_start"]}
    aus = {"lauf": name, "stufe": stufe, "K0": k0, "box": box}
    if t_teil is None:
        aus.update({"stuecke": [], "D1_lauf": False, "D1_grund": "keine Teilung bis t = 30", "je_T": {}})
        return aus
    stuecke, spur = verfolgen(reihe, t_teil)
    aus["stuecke"] = [{"rang": i, "Q_teil": s["Q"], "X": s["X"], "Y": s["Y"], "windung": s["windung"]}
                      for i, s in enumerate(stuecke)]
    je_T = {}
    for T in T_URTEIL:
        p, sp = bei(reihe, T), bei(spur, T)
        if p is None or sp is None:
            continue
        sp40 = bei(spur, T - FENSTER)
        gruppen = {}
        for i, j in enumerate(sp["zuordnung"]):
            if j is not None:
                gruppen.setdefault(j, []).append(i)
        zeilen = []
        for i, st in enumerate(stuecke):
            j = sp["zuordnung"][i]
            z = {"rang": i, "da": j is not None}
            if j is not None:
                gg = p["gebiete"][j]
                mit = gruppen[j]
                q_teil = sum(stuecke[k]["Q"] for k in mit)
                z.update({"gebiet": j, "mit": [k for k in mit if k != i], "Q": gg["Q"], "anteil": gg["Q"] / q_teil,
                          "X": gg["X"], "Y": gg["Y"], "v": math.hypot(gg["vx"], gg["vy"]), "windung": gg["windung"],
                          "S_min_kreis": gg["S_min_kreis"], "r_mittel": gg["r_mittel"], "flaeche": gg["flaeche"],
                          "Jspin_Q": gg["Jspin_Q"], "tiefe": max(abs(gg["X"]), abs(gg["Y"]))})
            xy = sp40["lage"][i] if sp40 is not None else None
            z["klassifikator"] = ({f"{S0:g}": klassifikator(lauf, T, S0, xy[0], xy[1]) for S0 in S0_LISTE}
                                  if xy is not None else {})
            zeilen.append(z)
        ueberlebt = [j for j, mit in gruppen.items()
                     if p["gebiete"][j]["Q"] / sum(stuecke[k]["Q"] for k in mit) >= D1_ANTEIL]
        je_T[f"{T:g}"] = {"n_gebiete": len(p["gebiete"]), "Q_box": p["Q_box"], "stuecke": zeilen,
                          "ueberlebende_gebiete": len(ueberlebt),
                          "alle_gebiete": [[g_["Q"], g_["X"], g_["Y"], g_["windung"]] for g_ in p["gebiete"]]}
    aus["je_T"] = je_T
    z300 = je_T.get(f"{T_URTEIL[-1]:g}")
    aus["D1_lauf"] = (z300["ueberlebende_gebiete"] >= 2) if z300 is not None else None
    d2 = []
    if z300 is not None:
        for z in z300["stuecke"]:
            kl = z.get("klassifikator", {}).get(f"{S0_HAUPT:g}", {})
            d2.append(bool(z["da"] and z["anteil"] >= D1_ANTEIL and kl.get("klasse") == "auf"
                           and kl.get("rund") is True))
    aus["D2_stuecke"] = d2
    return aus


def kontrolle_auswerten(lauf):
    zeilen = []
    for T in T_URTEIL:
        for S0 in S0_LISTE:
            kl = klassifikator(lauf, T, S0, 0.0, 0.0)
            zeilen.append({"T": T, "S0": S0, **kl,
                           "auf_rund": kl.get("klasse") == "auf" and kl.get("rund") is True})
    return {"lauf": lauf["lauf"], "stufe": lauf["stufe"], "zeilen": zeilen,
            "ok": all(z["auf_rund"] for z in zeilen if abs(z["S0"] - S0_HAUPT) < 1e-12)}


def gesamt(g, f):
    if g is None or f is None:
        return "offen (unvollstaendig)"
    if g == f:
        return "eingetroffen" if g else "nicht eingetroffen"
    return "offen (grob und fein verschieden)"


def auswerten(ordner):
    roh = {}
    for gr in ("grob", "fein-w60", "fein-w75", "kontrolle"):
        p = os.path.join(ordner, f"{gr}_roh.json")
        if os.path.exists(p):
            with open(p) as fh:
                roh[gr] = json.load(fh)
    laeufe = {"grob": {}, "fein": {}}
    kontrolle = []
    for gr, r in roh.items():
        for stufe, liste in r["ergebnis"].items():
            for lauf in liste:
                if gr == "kontrolle":
                    kontrolle.append(kontrolle_auswerten(lauf))
                else:
                    laeufe[stufe][lauf["lauf"]] = lauf_auswerten(lauf)
    k0_zeilen = [(st, n, laeufe[st][n]["K0"]) for st in ("grob", "fein") for n in NAMEN_GEF if n in laeufe[st]]
    if len(k0_zeilen) < 8:
        d0 = "offen (unvollstaendig)"
    else:
        d0 = "eingetroffen" if all(k["ok"] for _, _, k in k0_zeilen) else "nicht eingetroffen"
    box_ok = all(laeufe[st][n]["box"]["ok"] for st in laeufe for n in laeufe[st])
    d1_stufe = {}
    for st in ("grob", "fein"):
        if all(n in laeufe[st] for n in NAMEN_GEF):
            werte = [laeufe[st][n]["D1_lauf"] for n in NAMEN_GEF]
            d1_stufe[st] = None if any(w is None for w in werte) else (sum(1 for w in werte if w) >= 3)
        else:
            d1_stufe[st] = None
    d1 = gesamt(d1_stufe["grob"], d1_stufe["fein"])
    kontrolle_ok = bool(kontrolle) and len(kontrolle) == 2 * len(KONTROLLE_W2) and all(k["ok"] for k in kontrolle)
    treffer = []
    for n in NAMEN_GEF:
        if n in laeufe["grob"] and n in laeufe["fein"]:
            dg, df = laeufe["grob"][n].get("D2_stuecke", []), laeufe["fein"][n].get("D2_stuecke", [])
            for i in range(min(len(dg), len(df))):
                if dg[i] and df[i]:
                    treffer.append(f"{n} Stueck {i}")
    voll = all(n in laeufe[st] for st in ("grob", "fein") for n in NAMEN_GEF)
    if not kontrolle_ok:
        d2 = "offen (Klassifikator-Kontrolle nicht bestanden oder fehlt)"
    elif treffer:
        d2 = "eingetroffen"
    elif voll:
        d2 = "nicht eingetroffen"
    else:
        d2 = "offen (unvollstaendig)"
    if d1 == "eingetroffen" and d2 == "eingetroffen":
        bed = ("D1 und D2 treffen ein: Der gefuetterte Drehball zerfaellt in Q-Ball-Toechter ohne Windung. Das ist eine "
               "Teilung, aber keine Groessengrenze im Sinn von Bio 28 [H].")
    elif d1 == "nicht eingetroffen":
        bed = "D1 trifft nicht ein: Die Toechter zerfliessen auch ohne Rand."
    else:
        bed = f"Bedeutung nach Karte nicht zugeordnet (D1 {d1}, D2 {d2})."
    return {"D": {"D0": d0, "D1": d1, "D2": d2}, "D1_je_stufe": d1_stufe, "D2_treffer": treffer,
            "box_ok_alle": box_ok, "kontrolle_ok": kontrolle_ok, "bedeutung": bed, "laeufe": laeufe,
            "kontrolle": kontrolle,
            "dateien": {gr: {"start": r["start"], "ende": r["ende"], "dauer_s": r["dauer_s"], "zeiten": r["zeiten"],
                             "gpu_max_mb": r["gpu_max_mb"], "sha256": r["sha256"], "geraet": r["geraet"]}
                        for gr, r in roh.items()}}


def f_(v, fmt=".3f"):
    return "-" if v is None else format(v, fmt)


def text_auswertung(a):
    L = [f"bio28b Auswertung: D {json.dumps(a['D'])}", f"D1 je Stufe {json.dumps(a['D1_je_stufe'])}; D2-Treffer "
         f"{a['D2_treffer']}; Box alle ok {a['box_ok_alle']}; Kontrolle ok {a['kontrolle_ok']}",
         "Bedeutung (Karte): " + a["bedeutung"]]
    for st in ("grob", "fein"):
        for n in NAMEN_GEF:
            x = a["laeufe"][st].get(n)
            if x is None:
                L.append(f"[{st} {n}] fehlt")
                continue
            k0, bx = x["K0"], x["box"]
            L.append(f"[{st} {n}] K0 ok {k0['ok']}: t_V {k0['t_verschmolzen']} t_T {k0['t_teilung']} (R21 {k0['r21']})"
                     f" | Box ok {bx['ok']}: Tiefe max {bx['tiefe_max']} < {bx['grenze']:g}; Q_box Ende/Start "
                     f"{bx['Q_box_ende_anteil']:.4f} | D1 Lauf {x['D1_lauf']} | D2 Stuecke {x.get('D2_stuecke')}")
            for s in x["stuecke"]:
                L.append(f"   Stueck {s['rang']}: Q_teil {s['Q_teil']:.2f} bei ({s['X']:.2f}, {s['Y']:.2f}) w {s['windung']}")
            for T, zt in x["je_T"].items():
                L.append(f"   T {T}: n {zt['n_gebiete']}, ueberlebende Gebiete {zt['ueberlebende_gebiete']}, "
                         f"Q_box {zt['Q_box']:.2f}, alle {zt['alle_gebiete']}")
                for z in zt["stuecke"]:
                    k3 = z.get("klassifikator", {}).get("0.3", {})
                    k1 = z.get("klassifikator", {}).get("0.1", {})
                    if z["da"]:
                        L.append(f"     Stueck {z['rang']}: Q {z['Q']:.2f} Anteil {z['anteil']:.3f} mit {z['mit']} "
                                 f"({z['X']:.2f}, {z['Y']:.2f}) v {z['v']:.4f} w {z['windung']} Smin "
                                 f"{z['S_min_kreis']:.3f} | S0 0,3: {k3.get('klasse')} rund {k3.get('rund')} "
                                 f"rmax/ra {f_(k3.get('rmax_zu_ra'))} Q_net {f_(k3.get('Q_net'), '.2f')} omega "
                                 f"{f_(k3.get('omega_ruhe'), '.5f')} +- {f_(k3.get('u_omega'), '.1e')} dQ "
                                 f"{f_(k3.get('dQ'), '+.4f')} v {f_(k3.get('v'), '.4f')} | S0 0,1: {k1.get('klasse')}")
                    else:
                        L.append(f"     Stueck {z['rang']}: nicht gefunden | S0 0,3: {k3.get('klasse')}")
    for k in a["kontrolle"]:
        L.append(f"[Kontrolle {k['stufe']} {k['lauf']}] ok {k['ok']}: " + "; ".join(
            f"T {z['T']:g} S0 {z['S0']:g} {z.get('klasse')} rund {z.get('rund')} dQ {f_(z.get('dQ'), '+.4f')} "
            f"omega {f_(z.get('omega_ruhe'), '.5f')}" for z in k["zeilen"]))
    for gr, d in a["dateien"].items():
        L.append(f"Datei {gr}: {d['start']} bis {d['ende']}, Dauer {json.dumps(d['dauer_s'])}, GPU max "
                 f"{d['gpu_max_mb']:.0f} MB, {d['geraet']}")
    return "\n".join(L)


def selbsttest():
    """Nur im Rauchlauf: Auswertungspfade mit erfundener Reihe (keine Messdaten)."""
    reihe = []
    ts = [0.5 * i for i in range(61)] + [35.0 + 5.0 * i for i in range(54)]
    for t in ts:
        if t < 2.0:
            geb = [(100.0, -10.0, 0.0), (50.0, 10.0, 0.0)]
        elif t < 10.0:
            geb = [(150.0, 0.0, 0.0)]
        else:
            geb = [(90.0, 0.0, 1.0 + 0.2 * (t - 10.0)), (55.0, 0.0, -1.0 - 0.2 * (t - 10.0))]
        reihe.append({"t": t, "Q_box": 200.0, "tiefe_max": 10.0 + 0.2 * t, "gebiete": [
            {"Q": q, "E": q, "X": x, "Y": y, "vx": 0.0, "vy": 0.2, "Jspin_Q": 0.0, "r_mittel": 2.0, "flaeche": 10.0,
             "windung": 0, "S_min_kreis": 0.5, "spannt": False} for q, x, y in geb]})
    fen = {"300": {"0.3": {"zeile": {"tropfen": {"rmax_zu_ra": [1.0, 1.1]}}, "fenster": {"tropfen": [
        {"k": 0, "x0": 0.0, "y0": 1.0 + 0.2 * 250.0, "klasse": "auf", "rund": True},
        {"k": 1, "x0": 0.0, "y0": -1.0 - 0.2 * 250.0, "klasse": "neben", "rund": True}]}}}}
    lauf = {"lauf": "w60_nachbarn1", "stufe": "grob", "L": L_GROSS, "reihe": reihe, "fenster": fen,
            "Q_box_start": 200.0, "Q_box_ende": 200.0}
    a = lauf_auswerten(lauf)
    soll = {"t_v": 2.0, "t_teil": 10.0, "K0": False, "D1_lauf": True, "D2_stuecke": [True, False], "box": True,
            "anteile": [1.0, 1.0]}
    ist = {"t_v": a["K0"]["t_verschmolzen"], "t_teil": a["K0"]["t_teilung"], "K0": a["K0"]["ok"],
           "D1_lauf": a["D1_lauf"], "D2_stuecke": a["D2_stuecke"], "box": a["box"]["ok"],
           "anteile": [round(z["anteil"], 6) for z in a["je_T"]["300"]["stuecke"]]}
    return {"soll": soll, "ist": ist, "ok": soll == ist}


def main():
    ap = argparse.ArgumentParser(description="Runde 22 bio28b: Toechter ohne Randverlust")
    ap.add_argument("--gruppe", choices=list(GRUPPEN) + ["kontrolle"], default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--auswerten", default=None, help="Ordner mit *_roh.json")
    args = ap.parse_args()
    if args.auswerten:
        a = auswerten(args.auswerten)
        schreibe(os.path.join(args.auswerten, "bio28b_auswertung.json"), a)
        text = text_auswertung(a)
        schreibe(os.path.join(args.auswerten, "bio28b_auswertung.txt"), text + "\n")
        print(text, flush=True)
        return
    if args.gruppe is None:
        raise SystemExit("--gruppe oder --auswerten angeben")
    out = args.out or os.path.join(HIER, "lauf-69", "rauch" if args.gruppe == "rauch" else "ausgabe")
    os.makedirs(out, exist_ok=True)
    roh = rechnen(args, out)
    if args.gruppe == "rauch":
        try:
            st = selbsttest()
            print("Selbsttest Auswertung (erfundene Reihe): " + json.dumps(st), flush=True)
            a = lauf_auswerten(roh["ergebnis"]["grob"][0])
            print("Auswertungsdurchlauf Rauchdaten (ungueltig): K0 " + json.dumps(a["K0"]) + " Box "
                  + json.dumps(a["box"]), flush=True)
            for lauf in roh["ergebnis"]["grob"]:
                fe = lauf["fenster"].get("6", {}).get("0.3", {})
                print(f"  Rauch {lauf['lauf']}: Fenstertropfen {len(fe.get('fenster', {}).get('tropfen', []))}, "
                      f"Klassen {[x.get('klasse') for x in fe.get('fenster', {}).get('tropfen', [])]}", flush=True)
            if not st["ok"]:
                raise SystemExit("Selbsttest nicht bestanden")
        except SystemExit:
            raise
        except Exception:
            print("FEHLER im Selbsttest:\n" + traceback.format_exc(), flush=True)
            raise SystemExit("Selbsttest mit Fehler")


if __name__ == "__main__":
    main()
