#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Z2-SCHUTZ-1 (Runde 49, RUNDE-37/z2-schutz-1): Barriere 360 -> 0 Grad auf Finns Diamant-Netz.

Synthetische Modellrechnung, keine Messdaten. Modell, Ablauf und Regeln: PLAN.md.
Netz, Energie, FIRE, Stoss: finn.py aus GUERTEL-FINN-NETZ-1 (unveraendert, sha256 e9f357b6...), Umparametrisierung
g2.reparam_feld (guertel2.py, unveraendert).

Modi:
  start  Startzustand S bei 360 Grad (FIRE ab dem harmonischen Profil, ohne Rauschen) auf (r0, R).
  weg    Wegrechnung: --aufgabe haupt (S -> T), zs0 (420 -> -300, GFN1-Endpunkte), so2 (SO(2)-Gegenprobe);
         --verfahren neb (CI-NEB) oder string (Stringmethode mit Kletterbild).
  hesse  vier kleinste Eigenwerte der Riemannschen Hesse-Matrix fuer S, T und die Kletterbilder.
Aufruf nur ueber kleintest.sh auf der .69.
"""
import argparse
import hashlib
import json
import os
import resource
import sys
import time

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import finn  # noqa: E402  (GUERTEL-FINN-NETZ-1, unveraendert)
import guertel2 as g2  # noqa: E402  (GUERTEL-2, unveraendert)

T_START = time.time()
START_UTC = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
NP_ROH = np.array([0.92, 0.33, 0.21])
N_P = NP_ROH / np.sqrt((NP_ROH * NP_ROH).sum())
E_IMAG = [np.array([0.0, 1.0, 0.0, 0.0]), np.array([0.0, 0.0, 1.0, 0.0]), np.array([0.0, 0.0, 0.0, 1.0])]


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def kopf(args):
    return {"karte": "Z2-SCHUTZ-1 (Runde 49)", "modus": args.modus, "args": vars(args),
            "code_sha256": sha_datei(os.path.abspath(__file__)),
            "finn_sha256": sha_datei(os.path.abspath(finn.__file__)),
            "g2_sha256": sha_datei(os.path.abspath(g2.__file__)),
            "start_utc": START_UTC, "schreibzeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "numpy": np.__version__}


def maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def gtag(r0, R):
    return "r%g-R%g" % (r0, R)


# ---------------------------------------------------------------- Start und Ende

def modus_start(args):
    t0 = time.time()
    netz = finn.Netz("diamant", args.r0, args.R, "so3")
    x = np.zeros((netz.N, 1, 4))
    x[:, 0, 0] = np.cos(np.pi * netz.h)
    x[:, 0, 3] = np.sin(np.pi * netz.h)
    x = netz.setze(x, 2.0 * np.pi)
    E0, _, mon0 = netz.energie(x, grad=False)
    # finn.fire_feld in Bloecken zu 1000 Schritten bis ftol, nmax oder Wandzeit (args.budget)
    it, ml_alle = 0, float(mon0[0])
    grund = "nmax"
    while True:
        x, E, fm, i1, mon, ml = finn.fire_feld(netz, x, min(1000, args.nmax - it), args.ftol, args.dtmax)
        it += int(i1) + (0 if fm[0] <= args.ftol else 1)
        ml_alle = min(ml_alle, float(ml[0]))
        if fm[0] <= args.ftol:
            grund = "konvergiert"
            break
        if it >= args.nmax:
            break
        if time.time() - T_START > args.budget:
            grund = "wandzeit"
            break
    ml = np.array([ml_alle])
    st = finn.struktur(netz, x)
    tag = "start-" + gtag(args.r0, args.R)
    np.savez_compressed(os.path.join(args.aus, tag + ".npz"), q=x[:, 0])
    aus = {"kopf": kopf(args), "netz_info": netz.info(), "E_anfang": float(E0[0]), "sonde_anfang": float(mon0[0]),
           "E_S": float(E[0]), "fmax": float(fm[0]), "schritte": int(it), "grund": grund, "sonde": float(mon[0]),
           "sonde_lauf": float(ml[0]), "struktur": st, "laufzeit_s": time.time() - t0, "maxrss_mb": maxrss_mb()}
    g2.schreibe_json(os.path.join(args.aus, tag + ".json"), aus)
    print("start fertig %s laufzeit %.1f s" % (tag, aus["laufzeit_s"]))


def zustand_T(netz, qS):
    q = qS.copy()
    q[netz.frei] = np.array([1.0, 0.0, 0.0, 0.0])
    return q


# ---------------------------------------------------------------- Keim K (Endpunkt der Wegrechnung) und Weg K -> T

def fire_stopp(netz, x, nmax, ftol, dtmax, stopp, dtstart=0.02, capw=0.05, nmin=0):
    """Kopie von finn.fire_feld fuer B = 1, mit Abbruch sobald stopp(E) wahr ist; laufendes E-Maximum."""
    E, G, mon = netz.energie(x)
    F = -netz.tang(G, x)
    v = np.zeros_like(x)
    dt, alpha, npos = dtstart, 0.1, 0
    fmax = float(np.sqrt((F * F).sum(-1)).max())
    Emax, ml, it, halt = float(E[0]), float(mon[0]), 0, False
    for it in range(nmax):
        if fmax <= ftol:
            break
        if it >= nmin and stopp(float(E[0])):
            halt = True
            break
        Pw = (F * v).sum()
        vn = np.sqrt((v * v).sum())
        fn = np.sqrt((F * F).sum()) + 1.0e-300
        if Pw > 0.0:
            v = (1.0 - alpha) * v + (alpha * vn / fn) * F
            if npos >= 5:
                dt = min(dt * 1.1, dtmax)
                alpha *= 0.99
            npos += 1
        else:
            v = np.zeros_like(v)
            dt = max(dt * 0.5, 1.0e-7)
            alpha = 0.1
            npos = 0
        v = v + F * dt
        dx = v * dt
        dn = np.sqrt((dx * dx).sum(-1)).max()
        if dn > capw:
            dx *= capw / dn
            v *= capw / dn
        x = netz.norm(x + dx)
        v = netz.tang(v, x)
        E, G, mon = netz.energie(x)
        F = -netz.tang(G, x)
        fmax = float(np.sqrt((F * F).sum(-1)).max())
        Emax = max(Emax, float(E[0]))
        ml = min(ml, float(mon[0]))
    return x, float(E[0]), fmax, int(it), float(mon[0]), ml, Emax, halt


def kappe(netz, qS, alpha_rad, d_rad):
    """Ebener Zustand: Kappe um n_P (Winkel <= alpha voll, bis alpha + d linear) entdrillt (psi -> psi (1 - w))."""
    psi = np.arctan2(qS[:, 3], qS[:, 0])
    rn = np.sqrt((netz.pos ** 2).sum(1))
    gam = np.arccos(np.clip((netz.pos @ N_P) / np.maximum(rn, 1e-300), -1.0, 1.0))
    w = np.clip((alpha_rad + d_rad - gam) / d_rad, 0.0, 1.0)
    ps = psi * (1.0 - w)
    q = np.zeros((netz.N, 4))
    q[:, 0] = np.cos(ps)
    q[:, 3] = np.sin(ps)
    q[~netz.frei] = qS[~netz.frei]
    return q


def modus_keim(args):
    """PLAN Abschnitt 2 (nach Rauchtest 3): Keim K und Pruefung K -> T."""
    t0 = time.time()
    netz = finn.Netz("diamant", args.r0, args.R, "so3")
    qS = np.load(args.start)["q"]
    ES, _, _ = netz.energie(qS[:, None, :], grad=False)
    ES = float(ES[0])
    versuche = []
    K = None
    for a in [float(s) for s in args.kappen.split(",")]:
        x0 = kappe(netz, qS, np.deg2rad(a), np.deg2rad(args.d_grad))[:, None, :]
        E0, _, _ = netz.energie(x0, grad=False)
        x, E, fm, it, mon, ml, Emax, halt = fire_stopp(netz, x0, args.nkeim, 1e-7, args.dtmax,
                                                       lambda e: e < ES - args.delta_k, nmin=args.keim_min)
        versuche.append({"kappe_grad": a, "E_K0": float(E0[0]), "schritte": it, "E": E, "fmax": fm,
                         "unter_ES": bool(halt)})
        if halt:
            K = x
            break
    aus = {"kopf": kopf(args), "netz_info": netz.info(), "E_S": ES, "versuche": versuche, "K_gefunden": K is not None}
    if K is not None:
        EK, _, monK = netz.energie(K, grad=False)
        aus["E_K"] = float(EK[0])
        aus["sonde_K"] = float(monK[0])
        np.savez_compressed(os.path.join(args.aus, "keim-%s.npz" % gtag(args.r0, args.R)), q=K[:, 0])
        x, E, fm, it, mon, ml, Emax, halt = fire_stopp(
            netz, K.copy(), args.nmax, 1e-7, args.dtmax,
            lambda e: e < args.e_T or time.time() - T_START > args.budget)
        aus["K_nach_T"] = {"schritte": it, "E_end": E, "fmax_end": fm, "E_max": Emax, "sonde_end": mon,
                           "abbruch_E_oder_zeit": bool(halt), "T_erreicht": bool(E < args.e_T),
                           "E_max_unter_ES": bool(Emax < ES),
                           "abstand_T": float(np.abs(np.abs(x[netz.frei, 0, 0]) - 1.0).max())}
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    g2.schreibe_json(os.path.join(args.aus, "keim-%s.json" % gtag(args.r0, args.R)), aus)
    print("keim fertig %s laufzeit %.1f s" % (gtag(args.r0, args.R), aus["laufzeit_s"]))


def fire_zug(netz, x, ia, ib, cstern, kappa, nmax, ftol, dtmax, dtstart=0.02, capw=0.05):
    """Kopie von finn.fire_feld fuer B = 1 mit Strafterm kappa (c_b - c*)^2 auf der Bindung (ia, ib)."""
    def kraft(x):
        E, G, mon = netz.energie(x)
        c = float((x[ia, 0] * x[ib, 0]).sum())
        G = G.copy()
        G[ia, 0] += 2.0 * kappa * (c - cstern) * x[ib, 0]
        G[ib, 0] += 2.0 * kappa * (c - cstern) * x[ia, 0]
        return float(E[0]), -netz.tang(G, x), float(mon[0]), c

    E, F, mon, c = kraft(x)
    v = np.zeros_like(x)
    dt, alpha, npos = dtstart, 0.1, 0
    fmax = float(np.sqrt((F * F).sum(-1)).max())
    it = 0
    for it in range(nmax):
        if fmax <= ftol:
            break
        Pw = (F * v).sum()
        vn = np.sqrt((v * v).sum())
        fn = np.sqrt((F * F).sum()) + 1.0e-300
        if Pw > 0.0:
            v = (1.0 - alpha) * v + (alpha * vn / fn) * F
            if npos >= 5:
                dt = min(dt * 1.1, dtmax)
                alpha *= 0.99
            npos += 1
        else:
            v = np.zeros_like(v)
            dt = max(dt * 0.5, 1.0e-7)
            alpha = 0.1
            npos = 0
        v = v + F * dt
        dx = v * dt
        dn = np.sqrt((dx * dx).sum(-1)).max()
        if dn > capw:
            dx *= capw / dn
            v *= capw / dn
        x = netz.norm(x + dx)
        v = netz.tang(v, x)
        E, F, mon, c = kraft(x)
        fmax = float(np.sqrt((F * F).sum(-1)).max())
    return x, E, c, fmax, int(it), mon


def modus_zug(args):
    """Verfahren A (nach Rauchtest 5): Zugverfahren an der staerksten Bindung von S, danach Freigabe."""
    t0 = time.time()
    netz = finn.Netz("diamant", args.r0, args.R, "so3")
    qS = np.load(args.start)["q"]
    ES, _, monS = netz.energie(qS[:, None, :], grad=False)
    ES = float(ES[0])
    cS = (qS[netz.a] * qS[netz.b]).sum(-1)
    b = int(np.argmin(cS))
    ia, ib = int(netz.a[b]), int(netz.b[b])
    om0 = 2.0 * np.arccos(np.clip(cS[b], -1.0, 1.0))
    oms = om0 + (2.0 * np.pi - 2.0 * om0) * np.arange(args.nzug) / (args.nzug - 1.0)
    x = qS[:, None, :].copy()
    profil, zust = [], [qS.copy()]
    for j, om in enumerate(oms):
        if j == 0:
            profil.append({"j": 0, "c_ziel": float(cS[b]), "c": float(cS[b]), "E": ES, "fmax": 0.0, "schritte": 0,
                           "sonde": float(monS[0])})
            continue
        cst = float(np.cos(om / 2.0))
        x, E, c, fm, it, mon = fire_zug(netz, x, ia, ib, cst, args.kappa, args.nzugmax, args.ftol_zug, args.dtmax_zug)
        profil.append({"j": j, "c_ziel": cst, "c": c, "E": E, "fmax": fm, "schritte": it, "sonde": mon,
                       "t": time.time() - t0})
        zust.append(x[:, 0].copy())
        if time.time() - T_START > args.budget * 0.6:
            break
    Ez = np.array([p["E"] for p in profil])
    jm = int(np.argmax(Ez))
    mitte = 0.5 * (netz.pos[ia] + netz.pos[ib])
    aus = {"kopf": kopf(args), "netz_info": netz.info(), "E_S": ES, "bindung": b, "knoten": [ia, ib],
           "c_S": float(cS[b]), "r_bindung": float(np.sqrt((mitte ** 2).sum())),
           "kern_beteiligt": bool(netz.kern[ia] or netz.kern[ib]), "profil": profil, "j_max": jm,
           "barriere": float(Ez[jm] - ES), "max_innen": bool(0 < jm < len(Ez) - 1),
           "vollstaendig": bool(len(profil) == args.nzug)}
    aus["lokalisierung"] = lokalisierung(netz, zust[jm], qS)
    # Freigabe: FIRE ohne Strafterm ab dem letzten Zustand
    x, E, fm, it, mon, ml, Emax, halt = fire_stopp(
        netz, x.copy(), args.nmax, 1e-7, args.dtmax, lambda e: e < args.e_T or time.time() - T_START > args.budget)
    aus["freigabe"] = {"schritte": it, "E_end": E, "fmax_end": fm, "E_max": Emax, "T_erreicht": bool(E < args.e_T),
                       "zurueck_zu_S": bool(abs(E - ES) < 1e-3 * ES and fm < 1e-3), "E_max_unter_Zugmax": bool(Emax <= Ez[jm])}
    aus["gueltig"] = bool(aus["max_innen"] and aus["vollstaendig"] and aus["freigabe"]["T_erreicht"]
                          and aus["freigabe"]["E_max_unter_Zugmax"])
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    np.savez_compressed(os.path.join(args.aus, "zug-%s.npz" % gtag(args.r0, args.R)), Z=np.stack(zust))
    g2.schreibe_json(os.path.join(args.aus, "zug-%s.json" % gtag(args.r0, args.R)), aus)
    print("zug fertig %s laufzeit %.1f s" % (gtag(args.r0, args.R), aus["laufzeit_s"]))


def fire_klasse(netz, x, ES, nmax, delta, nskip, dtmax, dtstart=0.02, capw=0.05):
    """Kopie von finn.fire_feld fuer B = 1; Klasse 'T' sobald E < E_S - delta, 'S' sobald keine Bindung mehr c <= 0 hat
    (Rueckkehr in die Hebung von S), sonst 'offen'. Merkt den Zustand kleinster Knotenkraft ab Schritt nskip."""
    def kraft(x):
        E, G, mon = netz.energie(x)
        c = (x[netz.a, 0] * x[netz.b, 0]).sum(-1)
        return float(E[0]), -netz.tang(G, x), int((c <= 0.0).sum())

    E, F, nfl = kraft(x)
    v = np.zeros_like(x)
    dt, alpha, npos = dtstart, 0.1, 0
    fmax = float(np.sqrt((F * F).sum(-1)).max())
    best = (np.inf, None, None, -1)
    klasse, it = "offen", 0
    Ev = []
    for it in range(nmax):
        Ev.append(E)
        if it >= nskip and fmax < best[0]:
            best = (fmax, x[:, 0].copy(), E, it)
        if E < ES - delta:
            klasse = "T"
            break
        if nfl == 0 and it >= nskip:
            klasse = "S"
            break
        Pw = (F * v).sum()
        vn = np.sqrt((v * v).sum())
        fn = np.sqrt((F * F).sum()) + 1.0e-300
        if Pw > 0.0:
            v = (1.0 - alpha) * v + (alpha * vn / fn) * F
            if npos >= 5:
                dt = min(dt * 1.1, dtmax)
                alpha *= 0.99
            npos += 1
        else:
            v = np.zeros_like(v)
            dt = max(dt * 0.5, 1.0e-7)
            alpha = 0.1
            npos = 0
        v = v + F * dt
        dx = v * dt
        dn = np.sqrt((dx * dx).sum(-1)).max()
        if dn > capw:
            dx *= capw / dn
            v *= capw / dn
        x = netz.norm(x + dx)
        v = netz.tang(v, x)
        E, F, nfl = kraft(x)
        fmax = float(np.sqrt((F * F).sum(-1)).max())
    if best[1] is None:
        best = (fmax, x[:, 0].copy(), E, int(it))
    return klasse, x, int(it), best, Ev


def modus_bisekt(args):
    """Verfahren A (nach Rauchtest 6): Bisektion auf der Trennflaeche (edge tracking) in der Familie
    psi -> psi (1 - lambda w), w = Kappe um n_P (alpha 30 Grad, Uebergang 30 Grad); lambda in [0, 1]."""
    t0 = time.time()
    netz = finn.Netz("diamant", args.r0, args.R, "so3")
    qS = np.load(args.start)["q"]
    ES, _, _ = netz.energie(qS[:, None, :], grad=False)
    ES = float(ES[0])
    psi = np.arctan2(qS[:, 3], qS[:, 0])
    rn = np.sqrt((netz.pos ** 2).sum(1))
    gam = np.arccos(np.clip((netz.pos @ N_P) / np.maximum(rn, 1e-300), -1.0, 1.0))
    w = np.clip((np.deg2rad(args.kappe_b) + np.deg2rad(args.d_grad) - gam) / np.deg2rad(args.d_grad), 0.0, 1.0)

    def zustand(lam):
        ps = psi * (1.0 - lam * w)
        q = np.zeros((netz.N, 4))
        q[:, 0] = np.cos(ps)
        q[:, 3] = np.sin(ps)
        q[~netz.frei] = qS[~netz.frei]
        return q[:, None, :]

    lo, hi = 0.0, 1.0
    schritte = []
    kl_hi, x_hi, it_hi, best_hi, Ev_hi = fire_klasse(netz, zustand(hi), ES, args.nbis, args.delta_k, args.nskip,
                                                     args.dtmax)
    schritte.append({"lambda": hi, "klasse": kl_hi, "schritte": it_hi, "fmin": best_hi[0], "E_fmin": best_hi[2]})
    letzte = {"T": (hi, x_hi, best_hi) if kl_hi == "T" else None, "S": None}
    if kl_hi == "T":
        for i in range(args.nbisekt):
            if time.time() - T_START > args.budget * 0.7:
                break
            lam = 0.5 * (lo + hi)
            kl, x, it, best, Ev = fire_klasse(netz, zustand(lam), ES, args.nbis, args.delta_k, args.nskip, args.dtmax)
            schritte.append({"lambda": lam, "klasse": kl, "schritte": it, "fmin": best[0], "E_fmin": best[2],
                             "it_fmin": best[3]})
            if kl == "T":
                hi = lam
                letzte["T"] = (lam, x, best)
            elif kl == "S":
                lo = lam
                letzte["S"] = (lam, x, best)
            else:
                letzte["offen"] = (lam, x, best)
                break
    aus = {"kopf": kopf(args), "netz_info": netz.info(), "E_S": ES, "schritte": schritte, "lambda_lo": lo,
           "lambda_hi": hi}
    gut = letzte.get("T") is not None and letzte.get("S") is not None
    aus["klammer"] = bool(gut)
    if gut:
        bT, bS = letzte["T"][2], letzte["S"][2]
        aus["E_fmin_T"] = bT[2]
        aus["E_fmin_S"] = bS[2]
        aus["fmin_T"] = bT[0]
        aus["fmin_S"] = bS[0]
        aus["barriere"] = float(max(bT[2], bS[2]) - ES)
        aus["lokalisierung"] = lokalisierung(netz, bT[1] if bT[2] >= bS[2] else bS[1], qS)
        np.savez_compressed(os.path.join(args.aus, "bisekt-%s.npz" % gtag(args.r0, args.R)),
                            Z=np.stack([qS, bS[1], bT[1], letzte["T"][1][:, 0]]))
        # Freigabe: T-seitige Bahn weiter bis T
        xT = letzte["T"][1]
        x, E, fm, it, mon, ml, Emax, halt = fire_stopp(
            netz, xT.copy(), args.nmax, 1e-7, args.dtmax, lambda e: e < args.e_T or time.time() - T_START > args.budget)
        aus["freigabe"] = {"schritte": it, "E_end": E, "fmax_end": fm, "E_max": Emax, "T_erreicht": bool(E < args.e_T),
                           "E_max_unter_ES": bool(Emax < ES)}
        aus["gueltig"] = bool(aus["freigabe"]["T_erreicht"] and aus["freigabe"]["E_max_unter_ES"]
                              and len(schritte) - 1 >= args.nbisekt_min)
    else:
        aus["gueltig"] = False
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    g2.schreibe_json(os.path.join(args.aus, "bisekt-%s.json" % gtag(args.r0, args.R)), aus)
    print("bisekt fertig %s laufzeit %.1f s" % (gtag(args.r0, args.R), aus["laufzeit_s"]))


def weg_SK(netz, qS, qK, M, rng, sigma):
    """Anfangsweg S -> K: Halbwinkel je Knoten linear (beide Zustaende eben), innere Bilder mit Rauschen."""
    pS = np.arctan2(qS[:, 3], qS[:, 0])
    pK = np.arctan2(qK[:, 3], qK[:, 0])
    P = M + 2
    X = np.empty((P, netz.N, 4))
    for k in range(P):
        s = k / (M + 1.0)
        ps = (1.0 - s) * pS + s * pK
        q = np.zeros((netz.N, 4))
        q[:, 0] = np.cos(ps)
        q[:, 3] = np.sin(ps)
        q[~netz.frei] = qS[~netz.frei]
        X[k] = q
    X[0] = qS
    X[P - 1] = qK
    innen = np.ascontiguousarray(X[1:P - 1].transpose(1, 0, 2))
    innen = netz.rauschen(innen, rng, sigma)
    X[1:P - 1] = innen.transpose(1, 0, 2)
    return np.ascontiguousarray(X)


# ---------------------------------------------------------------- Anfangswege

def streifweg(netz, qS, M, d, rng, sigma):
    """PLAN Abschnitt 2: Entdrillung beginnt bei n_P und streift ueber die Kugel."""
    psi = np.arctan2(qS[:, 3], qS[:, 0])
    rn = np.sqrt((netz.pos ** 2).sum(1))
    dirs = netz.pos / np.maximum(rn, 1e-300)[:, None]
    gam = np.arccos(np.clip(dirs @ N_P, -1.0, 1.0))
    P = M + 2
    X = np.empty((P, netz.N, 4))
    for k in range(P):
        s = k / (M + 1.0)
        w = np.clip((s * (np.pi + d) - gam) / d, 0.0, 1.0)
        ps = psi * (1.0 - w)
        q = np.zeros((netz.N, 4))
        q[:, 0] = np.cos(ps)
        q[:, 3] = np.sin(ps)
        q[~netz.frei] = qS[~netz.frei]
        X[k] = q
    X[0] = qS
    X[P - 1] = zustand_T(netz, qS)
    innen = np.ascontiguousarray(X[1:P - 1].transpose(1, 0, 2))
    innen = netz.rauschen(innen, rng, sigma)
    X[1:P - 1] = innen.transpose(1, 0, 2)
    return np.ascontiguousarray(X)


def weg_zs0(netz, args):
    """PLAN Abschnitt 4: GFN1-Stoss eps = 0,01 bei 420 Grad mit Bildern alle 4 FIRE-Schritte."""
    q420 = np.load(os.path.join(args.eingaben, "prot-diamant-so3-d10-zust.npz"))["420"]
    qend = np.load(os.path.join(args.eingaben, "stoss-diamant-so3-T420-e0.01-end.npz"))["q"]
    x = q420[:, None, :].copy()
    x, delta = finn.kipp(netz, x, np.deg2rad(420.0), 0.01)
    rahmen = [x[:, 0].copy()]
    z = {"n": 0}

    def rec(xx):
        z["n"] += 1
        if z["n"] % 4 == 0:
            rahmen.append(xx[:, 0].copy())

    netz.dim = 3  # nur fuer g2.fire_feld (laufende Sonde min wie SO(3)); Arithmetik wie finn.fire_feld
    x, E, fm, it, mon, ml = g2.fire_feld(netz, x, args.zs0_nmax, 1.0e-5, 0.1, rec=rec)
    rahmen.append(x[:, 0].copy())
    info = {"stoss_schritte": int(it), "stoss_E_end": float(E[0]), "stoss_sonde_lauf": float(ml[0]),
            "abstand_eigenes_ende_gfn1_ende": float(np.abs(x[:, 0] - qend).max()), "rahmen": len(rahmen)}
    pfad = np.concatenate([q420[None], np.stack(rahmen), qend[None]], 0)
    del rahmen
    X = np.ascontiguousarray(g2.reparam_feld(pfad, args.M + 2, netz.frei, normP_fn(netz)))
    X[0] = q420
    X[-1] = qend
    return X, info


def weg_so2(netz2, args):
    """PLAN Abschnitt 4: SO(2)-Gegenprobe 420 -> -300."""
    p420 = np.load(os.path.join(args.eingaben, "prot-diamant-so2-d10-zust.npz"))["420"]
    qend = np.load(os.path.join(args.eingaben, "stoss-diamant-so3-T420-e0.01-end.npz"))["q"]
    phi = 2.0 * np.arctan2(qend[:, 3], qend[:, 0])
    x = phi[:, None, None].copy()
    x = netz2.setze(x, np.deg2rad(420.0))
    x, E, fm, it, mon, ml = finn.fire_feld(netz2, x, args.nmax_rel, 1.0e-7, 0.1)
    pend = x[:, 0].copy()
    P = args.M + 2
    X = np.empty((P, netz2.N, 1))
    for k in range(P):
        s = k / (P - 1.0)
        X[k] = (1.0 - s) * p420 + s * pend
    X[0] = p420
    X[-1] = pend
    info = {"so2_ende_E": float(E[0]), "so2_ende_fmax": float(fm[0]), "so2_ende_schritte": int(it),
            "so2_ende_sonde": float(mon[0])}
    return X, info


# ---------------------------------------------------------------- Wegverfahren (Bilder zuerst: X hat Form (P, N, k))

def normP_fn(netz):
    if netz.so3:
        return lambda x: x / np.sqrt((x * x).sum(-1, keepdims=True))
    return lambda x: x


def tangP(netz, G, X):
    if netz.so3:
        G = G - (G * X).sum(-1, keepdims=True) * X
    G = G.copy()
    G[:, ~netz.frei] = 0.0
    return G


def proj(netz, t, x):
    if netz.so3:
        t = t - (t * x).sum(-1, keepdims=True) * x
    t = t.copy()
    t[~netz.frei] = 0.0
    return t


def energie_bild(netz, q):
    e, g, m = netz.energie(q[:, None, :])
    return float(e[0]), g[:, 0], float(m[0])


def tangenten(netz, X, E, verfahren):
    P = X.shape[0]
    tau = np.zeros_like(X)
    for k in range(1, P - 1):
        if verfahren == "neb":
            Ep, E0, Em = E[k + 1], E[k], E[k - 1]
            if Ep > E0 > Em:
                t = X[k + 1] - X[k]
            elif Ep < E0 < Em:
                t = X[k] - X[k - 1]
            else:
                dmax = max(abs(Ep - E0), abs(Em - E0))
                dmin = min(abs(Ep - E0), abs(Em - E0))
                dp = X[k + 1] - X[k]
                dm = X[k] - X[k - 1]
                t = dp * dmax + dm * dmin if Ep > Em else dp * dmin + dm * dmax
        else:
            t = X[k + 1] - X[k - 1]
        t = proj(netz, t, X[k])
        n = np.sqrt((t * t).sum())
        tau[k] = t / max(n, 1e-300)
    return tau


def kraefte(netz, X, verfahren, ki, ks, E_end):
    """Innere Bilder neu, Endpunkte fest (E_end = (E_0, E_P-1, Sonde_0, Sonde_P-1))."""
    P = X.shape[0]
    E = np.zeros(P)
    mon = np.zeros(P)
    F = np.zeros_like(X)
    E[0], E[-1], mon[0], mon[-1] = E_end
    for k in range(1, P - 1):
        e, g, m = energie_bild(netz, X[k])
        E[k], mon[k] = e, m
        F[k] = -g
    F = tangP(netz, F, X)
    tau = tangenten(netz, X, E, verfahren)
    Fn = np.zeros_like(X)
    for k in range(1, P - 1):
        f = F[k]
        t = tau[k]
        fp = (f * t).sum()
        if k == ki:
            Fn[k] = f - 2.0 * fp * t
        else:
            Fn[k] = f - fp * t
            if verfahren == "neb":
                lp = np.sqrt(((X[k + 1] - X[k]) ** 2).sum())
                lm = np.sqrt(((X[k] - X[k - 1]) ** 2).sum())
                Fn[k] += ks * (lp - lm) * t
    return E, Fn, mon


def ausrichten(netz, X, v=None):
    """Eichung (PLAN nach Rauchtest 4): Bild k+1 je Knoten auf das Vorzeichen von Bild k (E haengt nur von c^2 ab)."""
    if not netz.so3:
        return X, v
    for k in range(1, X.shape[0]):
        s = np.where((X[k] * X[k - 1]).sum(-1) < 0.0, -1.0, 1.0)
        s[~netz.frei] = 1.0
        X[k] *= s[:, None]
        if v is not None:
            v[k] *= s[:, None]
    return X, v


def umparam(netz, X, ki):
    P = X.shape[0]
    nf = normP_fn(netz)

    def seg(a, b):
        n = b - a + 1
        if n <= 2:
            return X[a:b + 1]
        return g2.reparam_feld(X[a:b + 1], n, netz.frei, nf)

    if 0 < ki < P - 1:
        L = seg(0, ki)
        Rr = seg(ki, P - 1)
        X = np.concatenate([L[:-1], X[ki:ki + 1], Rr[1:]], 0)
    else:
        X = seg(0, P - 1)
    return np.ascontiguousarray(X)


def knotenkraft(Fk):
    return float(np.sqrt((Fk * Fk).sum(-1)).max())


def wegrechnung(netz, X, args, verfahren):
    """FIRE global ueber alle inneren Bilder (Parameter wie finn.fire_feld); Klettern ab args.nvor."""
    t0 = time.time()
    P = X.shape[0]
    nf = normP_fn(netz)
    X, _ = ausrichten(netz, X)
    e0, _, m0 = energie_bild(netz, X[0])
    e1, _, m1 = energie_bild(netz, X[-1])
    E_end = (e0, e1, m0, m1)
    v = np.zeros_like(X)
    dt, alpha, npos = np.full(P, args.dtstart), np.full(P, 0.1), np.zeros(P, int)
    ki = -1
    X, v = ausrichten(netz, X, v)
    E, Fn, mon = kraefte(netz, X, verfahren, ki, args.ks, E_end)
    lauf = float(mon.min()) if netz.so3 else float(mon.max())
    verlauf = []
    E_anf = E.copy()
    konv, grund, it = False, "nmax", 0
    kl_moeglich = False
    for it in range(args.nmax):
        if it >= args.nvor:
            km = int(np.argmax(E[1:-1])) + 1
            kl_moeglich = bool(E[km] > max(E[0], E[-1]))
            ki_neu = km if kl_moeglich else -1
            if ki_neu != ki:
                ki = ki_neu
                E, Fn, mon = kraefte(netz, X, verfahren, ki, args.ks, E_end)
        fb = max([knotenkraft(Fn[k]) for k in range(1, P - 1) if k != ki] + [0.0])
        fki = knotenkraft(Fn[ki]) if ki > 0 else None
        if it % 20 == 0:
            verlauf.append({"it": it, "E_max": float(E[1:-1].max()), "imax": int(np.argmax(E[1:-1])) + 1,
                            "ki": int(ki), "E_ki": float(E[ki]) if ki > 0 else None, "fband": fb, "fki": fki,
                            "dt": float(dt.max()), "sonde_min": float(mon.min()), "t": time.time() - t0})
        if it >= args.nvor:
            if ki > 0 and fki < args.ftol_ci and fb < args.ftol_band:
                konv, grund = True, "konvergiert"
                break
            if ki < 0 and fb < args.ftol_band:
                konv, grund = True, "konvergiert (ohne Klettern)"
                break
        if time.time() - T_START > args.budget:
            grund = "wandzeit"
            break
        # FIRE je Bild (wie finn.fire_feld je Spalte), Schrittdeckel je Bild
        Pw = (Fn * v).sum((1, 2))
        vn = np.sqrt((v * v).sum((1, 2)))
        fn = np.sqrt((Fn * Fn).sum((1, 2))) + 1.0e-300
        pos = Pw > 0.0
        v = np.where(pos[:, None, None], (1.0 - alpha)[:, None, None] * v + (alpha * vn / fn)[:, None, None] * Fn, 0.0)
        hoch = pos & (npos >= 5)
        dt = np.where(hoch, np.minimum(dt * 1.1, args.dtmax), np.where(pos, dt, np.maximum(dt * 0.5, 1.0e-7)))
        alpha = np.where(hoch, alpha * 0.99, np.where(pos, alpha, 0.1))
        npos = np.where(pos, npos + 1, 0)
        v = v + Fn * dt[:, None, None]
        dx = v * dt[:, None, None]
        dn = np.sqrt((dx * dx).sum(-1)).max(1)
        sc = np.where(dn > args.capw, args.capw / np.maximum(dn, 1.0e-300), 1.0)
        dx *= sc[:, None, None]
        v *= sc[:, None, None]
        X = nf(X + dx)
        X, v = ausrichten(netz, X, v)
        if verfahren == "string":
            X = umparam(netz, X, ki)
            X, v = ausrichten(netz, X, v)
        v = tangP(netz, v, X)
        v[0] = 0.0
        v[-1] = 0.0
        E, Fn, mon = kraefte(netz, X, verfahren, ki, args.ks, E_end)
        lauf = min(lauf, float(mon.min())) if netz.so3 else max(lauf, float(mon.max()))
    fb = max([knotenkraft(Fn[k]) for k in range(1, P - 1) if k != ki] + [0.0])
    fki = knotenkraft(Fn[ki]) if ki > 0 else None
    verlauf.append({"it": it, "E_max": float(E[1:-1].max()), "imax": int(np.argmax(E[1:-1])) + 1, "ki": int(ki),
                    "E_ki": float(E[ki]) if ki > 0 else None, "fband": fb, "fki": fki, "dt": float(dt.max()),
                    "sonde_min": float(mon.min()), "t": time.time() - t0})
    fk_bild = [knotenkraft(Fn[k]) for k in range(P)]
    abst = [float(np.sqrt(((X[k + 1] - X[k]) ** 2).sum())) for k in range(P - 1)]
    nachbar = ([float((X[k + 1] * X[k]).sum(-1)[netz.frei].min()) for k in range(P - 1)] if netz.so3 else None)
    erg = {"verfahren": verfahren, "iterationen": int(it), "grund": grund, "konvergiert": bool(konv),
           "ki": int(ki), "klettern_moeglich": bool(kl_moeglich), "E_profil": E, "E_profil_anfang": E_anf,
           "sonde_bilder": mon, "sonde_lauf": lauf, "fband": fb, "fki": fki, "fmax_bild": fk_bild,
           "abstand": abst, "nachbar_min_qq": nachbar, "verlauf": verlauf, "laufzeit_weg_s": time.time() - t0}
    return X, erg


def lokalisierung(netz, qs, qS):
    ca = (qs[netz.a] * qs[netz.b]).sum(-1)
    c0 = (qS[netz.a] * qS[netz.b]).sum(-1)
    D = 4.0 * (1.0 - ca * ca) - 4.0 * (1.0 - c0 * c0)
    B = float(D.sum())
    o = np.argsort(-D)
    cs = np.cumsum(D[o])
    L6 = float(cs[5] / B) if B > 0 else None
    n50 = int(np.argmax(cs >= 0.5 * B) + 1) if B > 0 else None
    b0 = int(o[0])
    mitte = 0.5 * (netz.pos[netz.a] + netz.pos[netz.b])
    rm = np.sqrt((mitte ** 2).sum(1))
    gam = np.degrees(np.arccos(np.clip((mitte @ N_P) / np.maximum(rm, 1e-300), -1.0, 1.0)))
    kernb = netz.kern[netz.a] | netz.kern[netz.b]
    top = [{"bindung": int(i), "Delta": float(D[i]), "c_sattel": float(ca[i]), "c_start": float(c0[i]),
            "r": float(rm[i]), "gamma_grad": float(gam[i]), "kernbindung": bool(kernb[i])} for i in o[:12]]
    return {"B_bindungssumme": B, "L6": L6, "n50": n50, "Delta_max": float(D[b0]), "r_max": float(rm[b0]),
            "gamma_max_grad": float(gam[b0]), "c_sattel_max": float(ca[b0]),
            "bindungen_c_le_0": int((ca <= 0).sum()), "anteil_kernbindungen": float(D[kernb].sum() / B) if B else None,
            "bindungen_Delta_gt_0.5": int((D > 0.5).sum()), "top12": top}


def modus_weg(args):
    t0 = time.time()
    rng = np.random.default_rng([49, 1, int(round(args.R))])
    info = {}
    fort = bool(args.fortsetzung)
    if args.aufgabe == "haupt":
        netz = finn.Netz("diamant", args.r0, args.R, "so3")
        if not fort:
            qS = np.load(args.start)["q"]
            if args.zugpfad:
                # Verfahren B (nach Rauchtest 5): CI-NEB auf dem Zugweg, gleiche Bogenlaenge, Rauschen innen
                Z = np.load(args.zugpfad)["Z"][args.zug_von:]
                X = np.ascontiguousarray(g2.reparam_feld(Z, args.M + 2, netz.frei, normP_fn(netz)))
                X[0] = Z[0]
                X[-1] = Z[-1]
                innen = np.ascontiguousarray(X[1:-1].transpose(1, 0, 2))
                innen = netz.rauschen(innen, rng, args.sigma)
                X[1:-1] = innen.transpose(1, 0, 2)
            else:
                qK = np.load(args.keim)["q"]
                X = weg_SK(netz, qS, qK, args.M, rng, args.sigma)
        tag = "weg-haupt-%s-%s" % (gtag(args.r0, args.R), args.verfahren)
    elif args.aufgabe == "zs0":
        netz = finn.Netz("diamant", 12.0, 24.0, "so3")
        if not fort:
            X, info = weg_zs0(netz, args)
        tag = "weg-zs0-%s" % args.verfahren
    else:
        netz = finn.Netz("diamant", 12.0, 24.0, "so2")
        if not fort:
            X, info = weg_so2(netz, args)
        tag = "weg-so2-%s" % args.verfahren
    if fort:
        # Fortsetzung (PLAN Abschnitt 2): Weg aus dem vorigen Lauf derselben Kette, FIRE neu gestartet
        X = np.ascontiguousarray(np.load(args.fortsetzung)["X"])
        info["fortsetzung_von"] = args.fortsetzung
        tag = tag + "-f%d" % args.fstufe
    info["aufbau_s"] = time.time() - t0
    X, erg = wegrechnung(netz, X, args, args.verfahren)
    E = np.asarray(erg["E_profil"])
    aus = {"kopf": kopf(args), "aufgabe": args.aufgabe, "netz_info": netz.info(), "info": info, "weg": erg,
           "E_0": float(E[0]), "E_ende": float(E[-1])}
    if erg["ki"] > 0:
        aus["E_sattel"] = float(E[erg["ki"]])
        if args.aufgabe == "haupt" and args.start:
            qS0 = np.load(args.start)["q"]
            ES0, _, _ = netz.energie(qS0[:, None, :], grad=False)
            aus["E_S"] = float(ES0[0])
            aus["barriere"] = float(E[erg["ki"]] - ES0[0])
            aus["lokalisierung"] = lokalisierung(netz, X[erg["ki"]], qS0)
        else:
            aus["barriere"] = float(E[erg["ki"]] - E[0])
            if netz.so3:
                aus["lokalisierung"] = lokalisierung(netz, X[erg["ki"]], X[0])
    else:
        aus["E_sattel"] = None
        aus["barriere"] = float(max(0.0, E[1:].max() - E[0]))
    if netz.so3:
        ok = np.nonzero(np.asarray(erg["sonde_bilder"]) <= 0.0)[0]
    else:
        ok = np.nonzero(np.asarray(erg["sonde_bilder"]) >= np.pi)[0]
    aus["erstes_sprungbild"] = int(ok[0]) if len(ok) else None
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    np.savez_compressed(os.path.join(args.aus, tag + ".npz"), X=X)
    g2.schreibe_json(os.path.join(args.aus, tag + ".json"), aus)
    print("weg fertig %s iterationen %d grund %s laufzeit %.1f s" % (tag, erg["iterationen"], erg["grund"],
                                                                      aus["laufzeit_s"]))


# ---------------------------------------------------------------- Hesse

def tangentialbasis(q):
    return np.stack([g2.qmul(e, q) for e in E_IMAG], -1)  # (N, 4, 3): e_i q


def hesse_matrix(netz, q):
    fr = netz.frei
    nf = int(fr.sum())
    idx = -np.ones(netz.N, int)
    idx[fr] = np.arange(nf)
    a, b = netz.a, netz.b
    qa, qb = q[a], q[b]
    c = (qa * qb).sum(-1)
    G = np.zeros_like(q)
    np.add.at(G, a, (-8.0 * c)[:, None] * qb)
    np.add.at(G, b, (-8.0 * c)[:, None] * qa)
    lam = (q * G).sum(-1)
    T = tangentialbasis(q)
    Ta, Tb = T[a], T[b]
    vab = np.einsum("nki,nk->ni", Ta, qb)
    vba = np.einsum("nki,nk->ni", Tb, qa)
    Daa = -8.0 * np.einsum("ni,nj->nij", vab, vab)
    Dbb = -8.0 * np.einsum("ni,nj->nij", vba, vba)
    TT = np.einsum("nki,nkj->nij", Ta, Tb)
    Oab = -8.0 * (c[:, None, None] * TT + np.einsum("ni,nj->nij", vab, vba))
    rows, cols, vals = [], [], []
    ii, jj = np.meshgrid(np.arange(3), np.arange(3), indexing="ij")

    def blk(ia, ib, B):
        rows.append((3 * ia[:, None, None] + ii[None]).ravel())
        cols.append((3 * ib[:, None, None] + jj[None]).ravel())
        vals.append(B.ravel())

    fa, fb = fr[a], fr[b]
    blk(idx[a][fa], idx[a][fa], Daa[fa])
    blk(idx[b][fb], idx[b][fb], Dbb[fb])
    m = fa & fb
    blk(idx[a][m], idx[b][m], Oab[m])
    blk(idx[b][m], idx[a][m], Oab[m].transpose(0, 2, 1))
    fi = np.nonzero(fr)[0]
    blk(idx[fi], idx[fi], -lam[fi][:, None, None] * np.eye(3)[None])
    H = sps.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                       shape=(3 * nf, 3 * nf)).tocsr()
    return H, T, idx


def eigen_klein(H, k, tol, maxiter):
    try:
        w, V = spl.eigsh(H, k=k, which="SA", tol=tol, maxiter=maxiter, ncv=min(H.shape[0] - 1, 48))
        o = np.argsort(w)
        return w[o], V[:, o], None
    except spl.ArpackNoConvergence as e:
        return None, None, "keine Konvergenz: %s" % str(e)[:200]


def symmetriemoden(netz, q, T):
    fr = netz.frei
    out = []
    for e in (E_IMAG[0], E_IMAG[1]):
        u = 0.5 * (g2.qmul(e, q) - g2.qmul(q, e))
        uc = np.einsum("nki,nk->ni", T, u)[fr].ravel()
        n = np.sqrt((uc * uc).sum())
        out.append(uc / max(n, 1e-300))
    return out


def modus_hesse(args):
    t0 = time.time()
    netz = finn.Netz("diamant", args.r0, args.R, "so3")
    qS = np.load(args.start)["q"]
    ziele = [("S", qS), ("T", zustand_T(netz, qS))]
    for eintrag in args.zusatz:
        name, datei, schl = eintrag.split("=")[0], eintrag.split("=")[1].split(":")[0], eintrag.split(":")[-1]
        if not os.path.exists(datei):
            ziele.append((name, None))
            continue
        d = np.load(datei)
        if schl.startswith("X"):
            js = json.load(open(datei.replace(".npz", ".json")))
            ki = js["weg"]["ki"]
            ziele.append((name, d["X"][ki] if ki > 0 else None))
        else:
            ziele.append((name, d[schl]))
    aus = {"kopf": kopf(args), "netz_info": netz.info(), "ergebnisse": {}}
    for name, q in ziele:
        t1 = time.time()
        if q is None:
            aus["ergebnisse"][name] = {"fehlt": True}
            continue
        H, T, idx = hesse_matrix(netz, q)
        w, V, fehler = eigen_klein(H, args.k, args.tol, args.maxiter)
        r = {"eigenwerte": w, "fehler": fehler, "dim": int(H.shape[0]), "nnz": int(H.nnz),
             "zahl_negativ": int((w < -1e-5).sum()) if w is not None else None, "laufzeit_s": time.time() - t1}
        if name == "S" and w is not None:
            sm = symmetriemoden(netz, q, T)
            V2 = V[:, :2]
            r["symmetrie_ueberlapp"] = [float(np.sqrt(((V2.T @ u) ** 2).sum())) for u in sm]
        aus["ergebnisse"][name] = r
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    g2.schreibe_json(os.path.join(args.aus, "hesse-%s.json" % gtag(args.r0, args.R)), aus)
    print("hesse fertig %s laufzeit %.1f s" % (gtag(args.r0, args.R), aus["laufzeit_s"]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("modus", choices=["start", "keim", "zug", "bisekt", "weg", "hesse"])
    p.add_argument("--aus", default=".")
    p.add_argument("--r0", type=float, default=12.0)
    p.add_argument("--R", type=float, default=24.0)
    p.add_argument("--nmax", type=int, default=20000)
    p.add_argument("--ftol", type=float, default=1.0e-7)
    p.add_argument("--dtmax", type=float, default=0.1)
    p.add_argument("--dtstart", type=float, default=0.02)
    p.add_argument("--capw", type=float, default=0.05)
    p.add_argument("--start", default="")
    p.add_argument("--eingaben", default="../eingaben-gfn1")
    p.add_argument("--aufgabe", default="haupt", choices=["haupt", "zs0", "so2"])
    p.add_argument("--verfahren", default="neb", choices=["neb", "string"])
    p.add_argument("--M", type=int, default=12)
    p.add_argument("--d_grad", type=float, default=30.0)
    p.add_argument("--sigma", type=float, default=1.0e-3)
    p.add_argument("--ks", type=float, default=1.0)
    p.add_argument("--nvor", type=int, default=150)
    p.add_argument("--ftol_ci", type=float, default=1.0e-3)
    p.add_argument("--ftol_band", type=float, default=5.0e-3)
    p.add_argument("--budget", type=float, default=480.0)
    p.add_argument("--zs0_nmax", type=int, default=3000)
    p.add_argument("--nmax_rel", type=int, default=20000)
    p.add_argument("--zusatz", nargs="*", default=[])
    p.add_argument("--fortsetzung", default="")
    p.add_argument("--fstufe", type=int, default=1)
    p.add_argument("--keim", default="")
    p.add_argument("--kappen", default="30,60,90")
    p.add_argument("--delta_k", type=float, default=1.0)
    p.add_argument("--nkeim", type=int, default=2000)
    p.add_argument("--e_T", type=float, default=1.0e-3)
    p.add_argument("--keim_min", type=int, default=100)
    p.add_argument("--zugpfad", default="")
    p.add_argument("--nzug", type=int, default=17)
    p.add_argument("--kappa", type=float, default=100.0)
    p.add_argument("--nzugmax", type=int, default=1500)
    p.add_argument("--ftol_zug", type=float, default=1.0e-4)
    p.add_argument("--dtmax_zug", type=float, default=0.05)
    p.add_argument("--kappe_b", type=float, default=30.0)
    p.add_argument("--nbis", type=int, default=800)
    p.add_argument("--nskip", type=int, default=30)
    p.add_argument("--nbisekt", type=int, default=14)
    p.add_argument("--nbisekt_min", type=int, default=10)
    p.add_argument("--zug_von", type=int, default=0)
    p.add_argument("--k", type=int, default=4)
    p.add_argument("--tol", type=float, default=1.0e-9)
    p.add_argument("--maxiter", type=int, default=200000)
    args = p.parse_args()
    os.makedirs(args.aus, exist_ok=True)
    {"start": modus_start, "keim": modus_keim, "zug": modus_zug, "bisekt": modus_bisekt, "weg": modus_weg,
     "hesse": modus_hesse}[args.modus](args)


if __name__ == "__main__":
    main()
