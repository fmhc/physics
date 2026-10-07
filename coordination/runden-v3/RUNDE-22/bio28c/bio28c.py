#!/usr/bin/env python3
"""Runde 22 (v3), Karte bio28c (RUNDE-22/bio28c/KARTE.md): Wohin geht der Drehimpuls des gefuetterten Drehballs?

Rechnet die vier gefuetterten Laeufe aus Bio 28b (RUNDE-22/bio28b/bio28b.py) nach:
  - r5_2d_a.py (RUNDE-05/r5-2d-a) unveraendert importiert: profile_holen, Gitter, ball_feld, ball_bewegt, entwickeln,
    dichten, unschaerfe, analyse, Konstanten.
  - Box wie Bio 28b: halbe Kantenlaenge L = 3 x 38,4 = 115,2 (n 768), Randschicht ab Tiefe 107,2. Nur grob
    (dx 0,3, dt 0,05). T = 90 (vor der Ankunft von Abstrahlung am Rand).
  - Profile in derselben Reihenfolge wie R5/R21/Bio 28b; Anfangsfelder wie Bio 28b.
Messung (PLAN.md Abschnitt 2 und 3):
  - Konvention (r5.dichten, aus L = |psi_t|^2 - |grad psi|^2 - U(S) per Noether):
        rho = 2 Im(psi conj psi_t),  P_i = -2 Re(conj(psi_t) d_i psi),  L_z = Int (x P_y - y P_x).
    Fuer psi = f(r) e^{i m theta - i omega t} gilt punktweise x P_y - y P_x = m rho, also L_z = m Q.
  - je Messpunkt (Takt 0,5): Q_box, E_box, L_box, P_box, Q/E/L in der Randschicht, Ladungsschwerpunkt der Box.
  - an allen Vielfachen von 5: Gebiete wie Bio 28b (Maske geglaettetes S > 0,5 x Anfangsmaximum, q_min 3 %,
    r5.analyse) und Zerlegung
        X0 = Sum Q_k X_k / Sum Q_k (gemeinsamer Ladungsschwerpunkt der Gebiete; X_k Schwerpunkt aus r5.analyse)
        (a) Bahn  = Sum_k (X_k - X0) x P_k,   P_k = Gebietsintegral der Impulsdichte
        (b) Eigen = Sum_k Int_k ((x - X_k) P_y - (y - Y_k) P_x)
        (c) Rest  = L_box - Sum_k Int_k (x P_y - y P_x)   (ausserhalb der gezaehlten Gebiete)
        s         = X0 x Sum_k P_k  (Schliessglied; L_box = a + b + c + s exakt)
    Zusatz (kein Kriterium): dieselbe Zerlegung mit Zonen statt Masken (jeder Punkt gehoert zum naechsten
    Gebietsschwerpunkt, wenn er hoechstens R_ZONE = 12 entfernt ist).
  - Konventionspruefung bei t = 0 auf demselben Gitter (Kontrollfelder, keine Zeitentwicklung):
        m1_w60, m1_w75   exakter Drehball m = 1 allein im Ursprung (K0: L/Q = 1 auf 1 %)
        m0_w60_ruhend    ruhender m = 0-Ball bei (10, -7) (K0: L = 0 auf 1 % von Q)
        paar_w60/_w75    zwei m = 0-Baelle bei (0, +-12), v = 0,2 in +-x (Vorzeichen der Bahn: L < 0, a/L > 0,
                         |b/L| < 0,05)

Aufruf:  python bio28c.py --gruppe grob|rauch [--out ORDNER]
         python bio28c.py --auswerten ROH.json
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

# ---- feste Parameter (PLAN.md, vor dem ersten echten Lauf) ----
L_GROSS = 3.0 * r5.L_STD          # 115,2 wie Bio 28b
T_ENDE = 90.0
MESS_DT = 0.5                     # Messtakt wie Bio 28b
ANALYSE_DT = 5.0                  # Gebietsanalyse und Zerlegung an allen Vielfachen von 5
T_TAB = (0.0, 20.0, 40.0, 60.0, 90.0)   # Zeiten der Karte
T_J = 60.0                        # J1, J2
R_ZONE = 12.0                     # Zusatz-Zerlegung (kein Kriterium)
K0_TOL = 0.01                     # K0: 1 %
J1_ANTEIL, J1_MIN = 0.5, 3        # J1: a/L0 >= 0,5 in mindestens 3 von 4 Laeufen
J2_ANTEIL = 0.10                  # J2: |b|/L0 < 0,10 in allen 4 Laeufen (Festlegung der Bearbeitung, PLAN 4)
PAAR_B_TOL = 0.05                 # Konvention, Paar: |b/L| < 0,05
RAND_E_REL = 1e-4                 # "Rand erreicht": Energie in der Randschicht >= 1e-4 E_box(0)
T_WAECHTER = 20.0
ZEITGRENZE_S = 570.0
RAUCH_T = 6.0
PAAR_Y, PAAR_V = 12.0, 0.2
NAMEN_GEF = ["w60_nachbarn1", "w60_nachbarn2", "w75_nachbarn1", "w75_nachbarn2"]
SPALTEN = ["Q_box", "E_box", "L_box", "Px_box", "Py_box", "Q_rand", "E_rand", "L_rand", "Qx_box", "Qy_box"]


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


# ---------------------------------------------------------------- Zerlegung (PLAN.md Abschnitt 3)

def zerlegen(g, rhob, pxb, pyb, jzb, geb, l_box):
    """Zerlegung von L_box (um den Ursprung) fuer ein Stapelelement; geb = Gebietsliste aus r5.analyse
    (volle Genauigkeit). Rueckgabe a, b, c, s (Maske) und a_Z, b_Z, c_Z, s_Z (Zonen, Zusatz)."""
    if not geb:
        return {"n": 0, "X0": None, "Y0": None, "a": 0.0, "b": 0.0, "c": l_box, "s": 0.0, "a_Z": 0.0, "b_Z": 0.0,
                "c_Z": l_box, "s_Z": 0.0, "gebiete": []}
    Q = [x["Q"] for x in geb]
    X = [x["X"] for x in geb]
    Y = [x["Y"] for x in geb]
    Px = [x["vx"] * x["E"] for x in geb]
    Py = [x["vy"] * x["E"] for x in geb]
    spin = [x["Jspin_Q"] * x["Q"] for x in geb]
    qs = sum(Q)
    X0 = sum(q * x for q, x in zip(Q, X)) / qs
    Y0 = sum(q * y for q, y in zip(Q, Y)) / qs
    K = len(geb)
    a = sum((X[k] - X0) * Py[k] - (Y[k] - Y0) * Px[k] for k in range(K))
    b = sum(spin)
    l_in = sum(spin[k] + X[k] * Py[k] - Y[k] * Px[k] for k in range(K))
    c = l_box - l_in
    s = X0 * sum(Py) - Y0 * sum(Px)
    # Zusatz: Zonen (naechster Gebietsschwerpunkt, hoechstens R_ZONE)
    cx = torch.tensor(X, dtype=r5.F64, device=r5.DEV).view(-1, 1, 1)
    cy = torch.tensor(Y, dtype=r5.F64, device=r5.DEV).view(-1, 1, 1)
    d2 = (g.X2.unsqueeze(0) - cx) ** 2 + (g.Y2.unsqueeze(0) - cy) ** 2
    dmin, kz = d2.min(0)
    inz = dmin <= R_ZONE * R_ZONE
    zone = []
    for k in range(K):
        zk = (inz & (kz == k)).to(r5.F64)
        qz, pxz, pyz, jzz = (torch.stack([(rhob * zk).sum(), (pxb * zk).sum(), (pyb * zk).sum(), (jzb * zk).sum()])
                             * g.dA).tolist()
        zone.append((qz, pxz, pyz, jzz))
    a_Z = sum((X[k] - X0) * zone[k][2] - (Y[k] - Y0) * zone[k][1] for k in range(K))
    b_Z = sum(zone[k][3] - X[k] * zone[k][2] + Y[k] * zone[k][1] for k in range(K))
    c_Z = l_box - sum(z[3] for z in zone)
    s_Z = X0 * sum(z[2] for z in zone) - Y0 * sum(z[1] for z in zone)
    gebiete = []
    for k, x in enumerate(geb):
        gebiete.append({"Q": x["Q"], "E": x["E"], "X": X[k], "Y": Y[k], "Px": Px[k], "Py": Py[k], "spin": spin[k],
                        "Jspin_Q": x["Jspin_Q"], "vx": x["vx"], "vy": x["vy"], "r_mittel": x["r_mittel"],
                        "flaeche": x["flaeche"], "windung": x.get("windung"), "S_min_kreis": x.get("S_min_kreis"),
                        "bahn": (X[k] - X0) * Py[k] - (Y[k] - Y0) * Px[k],
                        "zone": {"Q": zone[k][0], "Px": zone[k][1], "Py": zone[k][2], "Lz_ursprung": zone[k][3],
                                 "spin": zone[k][3] - X[k] * zone[k][2] + Y[k] * zone[k][1]}})
    return {"n": K, "X0": X0, "Y0": Y0, "a": a, "b": b, "c": c, "s": s, "a_Z": a_Z, "b_Z": b_Z, "c_Z": c_Z,
            "s_Z": s_Z, "P_in": [sum(Px), sum(Py)], "gebiete": gebiete}


def dichte_summen(g, d):
    s, rho, e, px, py, jz = d
    rand = 1.0 - g.innen
    dA = g.dA
    return torch.stack([rho.sum((1, 2)) * dA, e.sum((1, 2)) * dA, jz.sum((1, 2)) * dA, px.sum((1, 2)) * dA,
                        py.sum((1, 2)) * dA, (rho * rand).sum((1, 2)) * dA, (e * rand).sum((1, 2)) * dA,
                        (jz * rand).sum((1, 2)) * dA, (rho * g.x).sum((1, 2)) * dA, (rho * g.y).sum((1, 2)) * dA],
                       dim=1)


# ---------------------------------------------------------------- Kontrollfelder bei t = 0

def kontrolle(g, prof):
    felder = []
    for name, w2 in (("m1_w60", 0.60), ("m1_w75", 0.75)):
        p_, v_ = r5.ball_feld(g, prof[(w2, 1)], 1)
        felder.append((name, p_, v_))
    p_, v_ = r5.ball_feld(g, prof[(0.60, 0)], 0, 10.0, -7.0)
    felder.append(("m0_w60_ruhend", p_, v_))
    for name, w2 in (("paar_w60", 0.60), ("paar_w75", 0.75)):
        pa, va = r5.ball_bewegt(g, prof[(w2, 0)], 0, 0.0, PAAR_Y, PAAR_V, 0.0)
        pb, vb = r5.ball_bewegt(g, prof[(w2, 0)], 0, 0.0, -PAAR_Y, PAAR_V, math.pi)
        felder.append((name, pa + pb, va + vb))
    psi = torch.cat([f[1] for f in felder]).contiguous()
    vel = torch.cat([f[2] for f in felder]).contiguous()
    d = r5.dichten(g, psi, vel)
    s, rho, e, px, py, jz = d
    schwelle = r5.SCHWELLE_REL * r5.unschaerfe(g, s).amax((1, 2))
    q_min = (r5.Q_MIN_REL * rho.sum((1, 2)) * g.dA).tolist()
    maske = r5.unschaerfe(g, s) > schwelle.view(-1, 1, 1)
    gebiete = r5.analyse(g, psi, d, maske, q_min, True)
    summen = dichte_summen(g, d).tolist()
    aus = {}
    for b, (name, _, _) in enumerate(felder):
        zl = zerlegen(g, rho[b], px[b], py[b], jz[b], gebiete[b], summen[b][2])
        zl.update({sp: summen[b][i] for i, sp in enumerate(SPALTEN)})
        zl["profil_Q"] = {"m1_w60": prof[(0.60, 1)]["Q"], "m1_w75": prof[(0.75, 1)]["Q"],
                          "m0_w60_ruhend": prof[(0.60, 0)]["Q"]}.get(name)
        aus[name] = zl
    del psi, vel, d
    return aus


# ---------------------------------------------------------------- Lauf

def lauf_messen(g, psi, vel, dt, t_end, zeiten, t_aufruf, waechter):
    B = psi.shape[0]
    s0, rho0, _, _, _, _ = r5.dichten(g, psi, vel)
    schwelle = r5.SCHWELLE_REL * r5.unschaerfe(g, s0).amax((1, 2))
    q_min = (r5.Q_MIN_REL * rho0.sum((1, 2)) * g.dA).tolist()
    zerl = [[] for _ in range(B)]
    zaehler = [0]
    alle = int(round(ANALYSE_DT / MESS_DT))
    z_waechter = int(round(T_WAECHTER / MESS_DT))
    t_lauf = r5.uhr()

    def messen(psi, vel):
        d = r5.dichten(g, psi, vel)
        s, rho, e, px, py, jz = d
        spalten = dichte_summen(g, d)
        z = zaehler[0]
        t = z * MESS_DT
        if z % alle == 0:
            ta = r5.uhr()
            maske = r5.unschaerfe(g, s) > schwelle.view(-1, 1, 1)
            gebiete = r5.analyse(g, psi, d, maske, q_min, True)
            werte = spalten.tolist()
            for b, geb in enumerate(gebiete):
                zl = zerlegen(g, rho[b], px[b], py[b], jz[b], geb, werte[b][2])
                zl.update({"t": t, **{sp: werte[b][i] for i, sp in enumerate(SPALTEN)}})
                zerl[b].append(zl)
            zeiten["analyse_s"] += r5.uhr() - ta
            zeiten["analysen"] += 1
        if waechter and z == z_waechter:
            verg = r5.uhr() - t_lauf
            prognose = (r5.uhr() - t_aufruf) + verg / t * (t_end - t)
            zeiten["prognose_s"] = prognose
            print(f"  Prognose Gesamtdauer des Aufrufs {prognose:.0f} s (bei t {t:g})", flush=True)
            if prognose > ZEITGRENZE_S:
                raise SystemExit(f"Abbruch: Prognose {prognose:.0f} s > {ZEITGRENZE_S:.0f} s")
        zaehler[0] += 1
        return spalten

    alt = r5.T_MEAS
    r5.T_MEAS = MESS_DT
    try:
        t, daten = r5.entwickeln(g, psi, vel, dt, t_end, messen)
    finally:
        r5.T_MEAS = alt
    return t, daten, zerl, schwelle.tolist(), q_min


def rechnen(args, out):
    if not torch.cuda.is_available():
        raise SystemExit("Kein CUDA-Geraet: Abbruch (kein CPU-Ausweg).")
    t_aufruf = r5.uhr()
    rauch = args.gruppe == "rauch"
    start = r5.jetzt()
    pfad = frei(os.path.join(out, "rauch_roh.json" if rauch else "bio28c_roh.json"))
    print(f"bio28c {args.gruppe}: Start {start} auf {r5.geraet_name()}, torch {torch.__version__}", flush=True)
    dauer = {}
    t0 = r5.uhr()
    prof = r5.profile_holen([(w2, m) for _, w2, _ in r5.T5_LAEUFE for m in (0, 1)])
    dauer["schiessen_s"] = r5.uhr() - t0
    print(f"Schiessen fertig nach {dauer['schiessen_s']:.1f} s", flush=True)
    if not all(p["gueltig"] for p in prof.values()):
        raise SystemExit("Profil ungueltig: Abbruch")
    t_end = RAUCH_T if rauch else T_ENDE
    stufe, dx, dt = next(s_ for s_ in r5.STUFEN if s_[0] == "grob")
    g = r5.Gitter(L_GROSS, dx)
    t0 = r5.uhr()
    kon = kontrolle(g, prof)
    dauer["kontrolle_s"] = r5.uhr() - t0
    laeufe = [l for l in r5.T5_LAEUFE if l[0] in NAMEN_GEF]
    psis, vels, info = [], [], []
    for name, w2, k in laeufe:
        p1, p0 = prof[(w2, 1)], prof[(w2, 0)]
        dd = p1["R_halb"] + p0["R_halb"] + r5.T5_LUECKE
        p_, v_ = r5.ball_feld(g, p1, 1)
        for x0, ph in ((dd, 0.0), (-dd, math.pi))[:k]:
            a, b_ = r5.ball_feld(g, p0, 0, x0, 0.0, ph)
            p_, v_ = p_ + a, v_ + b_
        info.append({"lauf": name, "omega2": w2, "nachbarn": k, "abstand": dd, "Q_m1": p1["Q"], "Q_nachbar": p0["Q"]})
        psis.append(p_)
        vels.append(v_)
    psi = torch.cat(psis).contiguous()
    vel = torch.cat(vels).contiguous()
    del psis, vels
    zeiten = {"analyse_s": 0.0, "analysen": 0}
    t0 = r5.uhr()
    t, daten, zerl, schwelle, q_min = lauf_messen(g, psi, vel, dt, t_end, zeiten, t_aufruf, waechter=not rauch)
    dauer["entwicklung_s"] = r5.uhr() - t0
    n_schritte = int(round(t_end / dt))
    zeiten["ms_je_schritt"] = (dauer["entwicklung_s"] - zeiten["analyse_s"]) / n_schritte * 1e3
    zeiten["n"] = g.n
    zeiten["B"] = psi.shape[0]
    print(f"Entwicklung (L {L_GROSS:g}, n {g.n}, B {psi.shape[0]}) fertig nach {dauer['entwicklung_s']:.1f} s; "
          f"Analysen {zeiten['analysen']} in {zeiten['analyse_s']:.1f} s; {zeiten['ms_je_schritt']:.2f} ms je Schritt",
          flush=True)
    erg = []
    dl = daten.tolist()
    for b, inf in enumerate(info):
        reihe = [[round(i * MESS_DT, 3)] + list(dl[i][b]) for i in range(len(dl))]
        inf.update({"stufe": stufe, "L": L_GROSS, "dx": dx, "dt": dt, "n": g.n, "schwelle_S_glatt": schwelle[b],
                    "q_min": q_min[b], "reihe_spalten": ["t"] + SPALTEN, "reihe": reihe, "zerlegung": zerl[b]})
        erg.append(inf)
    roh = {"test": "bio28c", "gruppe": args.gruppe, "start": start, "ende": r5.jetzt(), "rauch": rauch,
           "dauer_s": dauer, "zeiten": zeiten, "geraet": r5.geraet_name(), "torch": torch.__version__,
           "gpu_max_mb": torch.cuda.max_memory_allocated() / 2 ** 20,
           "sha256": {"bio28c.py": sha(os.path.abspath(__file__)), "r5_2d_a.py": sha(r5.__file__)},
           "parameter": {"L_gross": L_GROSS, "sponge": r5.SPONGE, "t_end": t_end, "mess_dt": MESS_DT,
                         "analyse_dt": ANALYSE_DT, "stufe": [stufe, dx, dt], "luecke": r5.T5_LUECKE,
                         "schwelle_rel": r5.SCHWELLE_REL, "blur": r5.BLUR, "q_min_rel": r5.Q_MIN_REL,
                         "r_zone": R_ZONE, "paar_y": PAAR_Y, "paar_v": PAAR_V},
           "profile": [r5.profil_info(p) for p in prof.values()], "kontrolle": kon, "ergebnis": erg}
    roh["dauer_s"]["gesamt_s"] = r5.uhr() - t_aufruf
    schreibe(pfad, roh)
    print(f"Rohdaten geschrieben: {pfad}; Gesamtdauer {roh['dauer_s']['gesamt_s']:.1f} s; GPU max "
          f"{roh['gpu_max_mb']:.0f} MB", flush=True)
    return roh, pfad


# ---------------------------------------------------------------- Auswertung (PLAN.md Abschnitt 4, vorab)

def bei(liste, T):
    return next((p for p in liste if abs(p["t"] - T) < 1e-9), None)


def lauf_auswerten(lauf):
    sp = lauf["reihe_spalten"]
    iL, iE, iER, iQ = sp.index("L_box"), sp.index("E_box"), sp.index("E_rand"), sp.index("Q_box")
    reihe = lauf["reihe"]
    L0, E0, Q0 = reihe[0][iL], reihe[0][iE], reihe[0][iQ]
    t_rand = next((r[0] for r in reihe if r[iER] >= RAND_E_REL * E0), None)
    fenster = [r for r in reihe if r[0] <= T_ENDE + 1e-9 and (t_rand is None or r[0] < t_rand)]
    abw = max(abs(r[iL] / L0 - 1.0) for r in fenster)
    t_abw = max(fenster, key=lambda r: abs(r[iL] / L0 - 1.0))[0]
    t_max = reihe[-1][0]
    k0c = {"L0": L0, "Q_m1": lauf["Q_m1"], "L0_zu_Q_m1": L0 / lauf["Q_m1"], "max_abw": abw, "t_max_abw": t_abw,
           "t_rand": t_rand, "t_ende": t_max, "vollstaendig": t_max >= T_ENDE - 1e-9,
           "ok": (abw <= K0_TOL) if t_max >= T_ENDE - 1e-9 else None,
           "Q_ende_zu_Q0": reihe[-1][iQ] / Q0, "E_ende_zu_E0": reihe[-1][iE] / E0,
           "E_rand_max_rel": max(r[iER] for r in reihe) / E0}
    tab = {}
    for T in T_TAB:
        z = bei(lauf["zerlegung"], T)
        if z is None:
            continue
        tab[f"{T:g}"] = {"n_gebiete": z["n"], "L": z["L_box"] / L0, "a": z["a"] / L0, "b": z["b"] / L0,
                         "c": z["c"] / L0, "s": z["s"] / L0, "a_Z": z["a_Z"] / L0, "b_Z": z["b_Z"] / L0,
                         "c_Z": z["c_Z"] / L0, "s_Z": z["s_Z"] / L0, "X0": z["X0"], "Y0": z["Y0"],
                         "schluss": (z["L_box"] - z["a"] - z["b"] - z["c"] - z["s"]) / L0,
                         "gebiete": [[g_["Q"], g_["X"], g_["Y"], g_["bahn"] / L0, g_["spin"] / L0, g_["Jspin_Q"],
                                      g_["windung"]] for g_ in z["gebiete"]]}
    zj = tab.get(f"{T_J:g}")
    j1 = None if zj is None else zj["a"] >= J1_ANTEIL
    j2 = None if zj is None else abs(zj["b"]) < J2_ANTEIL
    return {"lauf": lauf["lauf"], "K0c": k0c, "tabelle": tab, "J1_lauf": j1, "J2_lauf": j2}


def kontrolle_auswerten(kon):
    aus = {}
    for n in ("m1_w60", "m1_w75"):
        k = kon[n]
        aus[n] = {"L": k["L_box"], "Q": k["Q_box"], "L_zu_Q": k["L_box"] / k["Q_box"], "Q_profil": k["profil_Q"],
                  "ok": abs(k["L_box"] / k["Q_box"] - 1.0) <= K0_TOL, "a_zu_L": k["a"] / k["L_box"],
                  "b_zu_L": k["b"] / k["L_box"], "c_zu_L": k["c"] / k["L_box"], "b_Z_zu_L": k["b_Z"] / k["L_box"],
                  "n_gebiete": k["n"]}
    k = kon["m0_w60_ruhend"]
    aus["m0_w60_ruhend"] = {"L": k["L_box"], "Q": k["Q_box"], "L_zu_Q": k["L_box"] / k["Q_box"],
                            "ok": abs(k["L_box"]) <= K0_TOL * k["Q_box"], "n_gebiete": k["n"]}
    for n in ("paar_w60", "paar_w75"):
        k = kon[n]
        L = k["L_box"]
        aus[n] = {"L": L, "Q": k["Q_box"], "P_box": [k["Px_box"], k["Py_box"]], "a_zu_L": k["a"] / L,
                  "b_zu_L": k["b"] / L, "c_zu_L": k["c"] / L, "s_zu_L": k["s"] / L, "a_Z_zu_L": k["a_Z"] / L,
                  "b_Z_zu_L": k["b_Z"] / L, "c_Z_zu_L": k["c_Z"] / L, "n_gebiete": k["n"],
                  "ok": L < 0.0 and k["a"] / L > 0.0 and abs(k["b"] / L) < PAAR_B_TOL and k["n"] == 2}
    return aus


def auswerten(roh):
    kon = kontrolle_auswerten(roh["kontrolle"])
    laeufe = {lauf["lauf"]: lauf_auswerten(lauf) for lauf in roh["ergebnis"]}
    k0a = kon["m1_w60"]["ok"] and kon["m1_w75"]["ok"]
    k0b = kon["m0_w60_ruhend"]["ok"]
    paare = kon["paar_w60"]["ok"] and kon["paar_w75"]["ok"]
    k0c_liste = [laeufe[n]["K0c"]["ok"] if n in laeufe else None for n in NAMEN_GEF]
    if any(x is None for x in k0c_liste):
        k0 = None
    else:
        k0 = k0a and k0b and all(k0c_liste)
    j0 = "offen (unvollstaendig)" if k0 is None else ("eingetroffen" if k0 else "nicht eingetroffen")
    j1_liste = [laeufe[n]["J1_lauf"] if n in laeufe else None for n in NAMEN_GEF]
    j2_liste = [laeufe[n]["J2_lauf"] if n in laeufe else None for n in NAMEN_GEF]
    if k0 is not True or not paare:
        grund = "offen (K0 oder Vorzeichenprobe nicht bestanden oder unvollstaendig)"
        j1 = j2 = grund
    else:
        ja1 = sum(1 for x in j1_liste if x is True)
        nein1 = sum(1 for x in j1_liste if x is False)
        if ja1 >= J1_MIN:
            j1 = "eingetroffen"
        elif nein1 > len(NAMEN_GEF) - J1_MIN:
            j1 = "nicht eingetroffen"
        else:
            j1 = "offen (unvollstaendig)"
        if any(x is False for x in j2_liste):
            j2 = "nicht eingetroffen"
        elif all(x is True for x in j2_liste):
            j2 = "eingetroffen"
        else:
            j2 = "offen (unvollstaendig)"
    if j1 == "eingetroffen" and j2 == "eingetroffen":
        bed = ("J1 und J2 treffen ein: Der innere Drehimpuls des Drehballs geht beim Zerfall in die Bahnbewegung der "
               "Toechter ueber, wie bei einem sich teilenden rotierenden Tropfen [H, im Modell].")
    elif j1 == "nicht eingetroffen":
        cs = {n: laeufe[n]["tabelle"].get(f"{T_J:g}", {}).get("c") for n in NAMEN_GEF if n in laeufe}
        bed = ("J1 trifft nicht ein: Der Drehimpuls geht ueberwiegend in Abstrahlung (c) (Wortlaut der Karte); (c)/L0 "
               f"bei T = {T_J:g}: " + ", ".join(f"{n} {v:.3f}" for n, v in cs.items() if v is not None))
    else:
        bed = f"Die Karte ordnet keine Bedeutung zu (J1 {j1}, J2 {j2}); Ausgaenge ohne Deutung."
    return {"J": {"J0": j0, "J1": j1, "J2": j2}, "K0": {"K0a": k0a, "K0b": k0b, "K0c": k0c_liste, "gesamt": k0},
            "vorzeichenprobe_paare": paare, "J1_je_lauf": dict(zip(NAMEN_GEF, j1_liste)),
            "J2_je_lauf": dict(zip(NAMEN_GEF, j2_liste)), "bedeutung": bed, "kontrolle": kon, "laeufe": laeufe,
            "datei": {"start": roh["start"], "ende": roh["ende"], "dauer_s": roh["dauer_s"], "zeiten": roh["zeiten"],
                      "gpu_max_mb": roh["gpu_max_mb"], "sha256": roh["sha256"], "geraet": roh["geraet"]}}


def f_(v, fmt=".4f"):
    return "-" if v is None else format(v, fmt)


def text_auswertung(a):
    L = [f"bio28c Auswertung: J {json.dumps(a['J'])}", f"K0 {json.dumps(a['K0'])}; Vorzeichenprobe Paare "
         f"{a['vorzeichenprobe_paare']}", f"J1 je Lauf {json.dumps(a['J1_je_lauf'])}; J2 je Lauf "
         f"{json.dumps(a['J2_je_lauf'])}", "Bedeutung (Karte): " + a["bedeutung"]]
    for n, k in a["kontrolle"].items():
        L.append(f"[Kontrolle {n}] " + json.dumps(k))
    for n in NAMEN_GEF:
        x = a["laeufe"].get(n)
        if x is None:
            L.append(f"[{n}] fehlt")
            continue
        k = x["K0c"]
        L.append(f"[{n}] K0c ok {k['ok']}: L0 {k['L0']:.4f} (Q_m1 {k['Q_m1']:.4f}, L0/Q_m1 {k['L0_zu_Q_m1']:.4f}), "
                 f"max |L/L0 - 1| {k['max_abw']:.2e} bei t {k['t_max_abw']}, t_rand {k['t_rand']}, E_rand max/E0 "
                 f"{k['E_rand_max_rel']:.2e}, Q_ende/Q0 {k['Q_ende_zu_Q0']:.5f} | J1 {x['J1_lauf']} J2 {x['J2_lauf']}")
        for T, z in x["tabelle"].items():
            L.append(f"   T {T}: n {z['n_gebiete']} L/L0 {z['L']:.4f} a {z['a']:+.4f} b {z['b']:+.4f} c {z['c']:+.4f} "
                     f"s {z['s']:+.2e} | Zonen a {z['a_Z']:+.4f} b {z['b_Z']:+.4f} c {z['c_Z']:+.4f} s "
                     f"{z['s_Z']:+.2e} | X0 ({f_(z['X0'], '.3f')}, {f_(z['Y0'], '.3f')}) Schluss {z['schluss']:+.1e}")
            for gg in z["gebiete"]:
                L.append(f"      Gebiet Q {gg[0]:.3f} ({gg[1]:.3f}, {gg[2]:.3f}) Bahn/L0 {gg[3]:+.4f} Spin/L0 "
                         f"{gg[4]:+.4f} Jspin/Q {gg[5]:+.4f} w {gg[6]}")
    d = a["datei"]
    L.append(f"Datei: {d['start']} bis {d['ende']}, Dauer {json.dumps(d['dauer_s'])}, GPU max {d['gpu_max_mb']:.0f} MB, "
             f"{d['geraet']}")
    return "\n".join(L)


def selbsttest():
    """Auswertungspfade mit erfundenen Zahlen (keine Messdaten)."""
    def lauf(name, a60, b60, abw):
        reihe = [[0.5 * i, 100.0, 50.0, 40.0 * (1.0 + (abw if i == 100 else 0.0)), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                 for i in range(181)]
        zerl = []
        for T in range(0, 95, 5):
            a_ = a60 * 40.0 if T >= 20 else 0.0
            b_ = b60 * 40.0 if T >= 20 else 30.0
            zerl.append({"t": float(T), "n": 2, "X0": 0.0, "Y0": 0.0, "a": a_, "b": b_, "c": 40.0 - a_ - b_, "s": 0.0,
                         "a_Z": a_, "b_Z": b_, "c_Z": 40.0 - a_ - b_, "s_Z": 0.0, "L_box": 40.0, "gebiete": []})
        return {"lauf": name, "Q_m1": 40.0, "reihe_spalten": ["t"] + SPALTEN, "reihe": reihe, "zerlegung": zerl}
    kon = {"m1_w60": {"L_box": 70.0, "Q_box": 70.2, "profil_Q": 70.2, "a": 0.0, "b": 60.0, "c": 10.0, "b_Z": 69.0,
                      "n": 1},
           "m1_w75": {"L_box": 30.0, "Q_box": 30.0, "profil_Q": 30.0, "a": 0.0, "b": 25.0, "c": 5.0, "b_Z": 29.0,
                      "n": 1},
           "m0_w60_ruhend": {"L_box": 0.0, "Q_box": 60.0, "n": 1},
           "paar_w60": {"L_box": -20.0, "Q_box": 1.0, "Px_box": 0.0, "Py_box": 0.0, "a": -15.0, "b": 0.0, "c": -5.0,
                        "s": 0.0, "a_Z": -19.0, "b_Z": 0.0, "c_Z": -1.0, "n": 2},
           "paar_w75": {"L_box": -10.0, "Q_box": 1.0, "Px_box": 0.0, "Py_box": 0.0, "a": -7.0, "b": 0.0, "c": -3.0,
                        "s": 0.0, "a_Z": -9.0, "b_Z": 0.0, "c_Z": -1.0, "n": 2}}
    d = {"start": "-", "ende": "-", "dauer_s": {}, "zeiten": {}, "gpu_max_mb": 0.0, "sha256": {}, "geraet": "-"}
    fall1 = auswerten({"kontrolle": kon, **d, "ergebnis": [lauf("w60_nachbarn1", 0.8, 0.02, 0.0),
                                                           lauf("w60_nachbarn2", 0.6, -0.05, 0.005),
                                                           lauf("w75_nachbarn1", 0.4, 0.01, 0.0),
                                                           lauf("w75_nachbarn2", 0.55, 0.12, 0.0)]})
    fall2 = auswerten({"kontrolle": kon, **d, "ergebnis": [lauf("w60_nachbarn1", 0.8, 0.02, 0.02),
                                                           lauf("w60_nachbarn2", 0.6, -0.05, 0.0),
                                                           lauf("w75_nachbarn1", 0.4, 0.01, 0.0),
                                                           lauf("w75_nachbarn2", 0.3, 0.02, 0.0)]})
    fall3 = auswerten({"kontrolle": kon, **d, "ergebnis": [lauf("w60_nachbarn1", 0.4, 0.02, 0.0),
                                                           lauf("w60_nachbarn2", 0.45, -0.05, 0.0),
                                                           lauf("w75_nachbarn1", 0.4, 0.01, 0.0),
                                                           lauf("w75_nachbarn2", 0.9, 0.02, 0.0)]})
    soll = {"fall1": {"J0": "eingetroffen", "J1": "eingetroffen", "J2": "nicht eingetroffen"},
            "fall2_J0": "nicht eingetroffen", "fall2_J1_offen": True,
            "fall3": {"J0": "eingetroffen", "J1": "nicht eingetroffen", "J2": "eingetroffen"}}
    ist = {"fall1": fall1["J"], "fall2_J0": fall2["J"]["J0"], "fall2_J1_offen": fall2["J"]["J1"].startswith("offen"),
           "fall3": fall3["J"]}
    text_auswertung(fall1)
    return {"soll": soll, "ist": ist, "ok": soll == ist}


def main():
    ap = argparse.ArgumentParser(description="Runde 22 bio28c: Drehimpuls des gefuetterten Drehballs")
    ap.add_argument("--gruppe", choices=["grob", "rauch"], default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--auswerten", default=None, help="ROH.json")
    args = ap.parse_args()
    if args.auswerten:
        with open(args.auswerten) as fh:
            roh = json.load(fh)
        a = auswerten(roh)
        ordner = os.path.dirname(os.path.abspath(args.auswerten))
        schreibe(os.path.join(ordner, "bio28c_auswertung.json"), a)
        text = text_auswertung(a)
        schreibe(os.path.join(ordner, "bio28c_auswertung.txt"), text + "\n")
        print(text, flush=True)
        return
    if args.gruppe is None:
        raise SystemExit("--gruppe oder --auswerten angeben")
    out = args.out or os.path.join(HIER, "lauf-69", "rauch" if args.gruppe == "rauch" else "ausgabe")
    os.makedirs(out, exist_ok=True)
    try:
        st = selbsttest()
    except Exception:
        print("FEHLER im Selbsttest:\n" + traceback.format_exc(), flush=True)
        raise SystemExit("Selbsttest mit Fehler")
    print("Selbsttest Auswertung (erfundene Zahlen): " + json.dumps(st), flush=True)
    if not st["ok"]:
        raise SystemExit("Selbsttest nicht bestanden")
    roh, pfad = rechnen(args, out)
    if args.gruppe == "rauch":
        try:
            a = auswerten(roh)
            print("Auswertungsdurchlauf Rauchdaten (ungueltig): J " + json.dumps(a["J"]) + "; K0 " + json.dumps(a["K0"])
                  + "; Vorzeichenprobe " + json.dumps(a["vorzeichenprobe_paare"]) + "; Tabellenzeiten "
                  + json.dumps({n: list(x["tabelle"]) for n, x in a["laeufe"].items()}), flush=True)
            text_auswertung(a)
        except Exception:
            print("FEHLER in der Auswertung der Rauchdaten:\n" + traceback.format_exc(), flush=True)
            raise SystemExit("Auswertung mit Fehler")


if __name__ == "__main__":
    main()
