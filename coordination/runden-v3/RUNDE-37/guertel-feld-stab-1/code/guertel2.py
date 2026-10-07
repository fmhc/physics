#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUERTEL-2 (Runde 42, RUNDE-37/guertel-2): Staley-Weg am Tetraeder-Knoten (Teil A), Guertel im Feld (Teil B).

Synthetische Modellrechnung, keine Messdaten. Modell, Ablauf und Regeln: PLAN.md.
Teil A nutzt das Fadenmodell von GUERTEL-1 unveraendert (guertel.py, Kopie, sha256 795f474d...).

Modi:
  leiter   Temperaturleiter bei 0 Grad (GZ3); 720 Grad ab dem Zwischenrast-Zustand (beschreibend)
  pfad     Bau der Anfangsstrings S1 (Staley), S2 (Zwischenrast), S0 (trivial); Durchdringungsprobe (GZ0a)
  string   Stringrelaxation eines gebauten Anfangsstrings
  feld     Orientierungsfeld: SO(3) auf Z^3 (dim 3) bzw. SO(2) auf Z^2 (dim 2); Protokoll, Saaten, Feld-String

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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guertel as g1  # noqa: E402  (GUERTEL-1, unveraendert)

ZWEI_PI = 2.0 * np.pi
VIER_PI = 4.0 * np.pi
EX = np.array([1.0, 0.0, 0.0])


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def schreibe_json(pfad, obj):
    tmp = pfad + ".neu"
    with open(tmp, "w") as f:
        json.dump(sauber(obj), f, indent=1)
    os.replace(tmp, pfad)


def sauber(o):
    if isinstance(o, float) and (np.isnan(o) or np.isinf(o)):
        return None
    if isinstance(o, dict):
        return {str(k): sauber(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sauber(v) for v in o]
    if isinstance(o, np.ndarray):
        return sauber(o.tolist())
    if isinstance(o, np.floating):
        return sauber(float(o))
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def kopf(args):
    return {"karte": "GUERTEL-2 (Runde 42)", "modus": args.modus, "args": vars(args),
            "code_sha256": sha_datei(os.path.abspath(__file__)),
            "g1_code_sha256": sha_datei(os.path.abspath(g1.__file__)),
            "start_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "numpy": np.__version__}


def maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


# =====================================================================================
# Teil A: Faeden (GUERTEL-1-Modell)
# =====================================================================================

def t_rad(r):
    """Radiale Koordinate: 0 am Anker (R_ANK), 1 am Ansatz (R_ATT)."""
    return np.clip((g1.R_ANK - r) / (g1.R_ANK - g1.R_ATT), 0.0, 1.0)


def rampen(t):
    fa = np.clip((t - 0.05) / 0.45, 0.0, 1.0)
    fi = np.clip((t - 0.50) / 0.45, 0.0, 1.0)
    return fa, fi


def rot_n(n, th):
    th = np.atleast_1d(np.asarray(th, float))
    return g1.rot(np.repeat(np.asarray(n, float)[None], len(th), 0), th)


def drehe_perlen(netz, X, Rm):
    """X (nb,3); Rm (nb,3,3) je Perle; feste Perlen bleiben exakt."""
    Y = np.einsum("bij,bj->bi", Rm, X)
    Y[~netz.frei] = X[~netz.frei]
    return Y


def staley_bild(netz, X0, s=None, lam=None):
    """Phase 1 (s in [0,1]): g = Rot(x, 2pi fa) Rot(n(s), 2pi fi), n(s) = (cos pi s, sin pi s, 0).
    Phase 2 (lam in [1,0]): g = Rot(x, 2pi lam (fa - fi))."""
    r = np.sqrt((X0 * X0).sum(-1))
    fa, fi = rampen(t_rad(r))
    if s is not None:
        n = np.array([np.cos(np.pi * s), np.sin(np.pi * s), 0.0])
        Rm = np.matmul(rot_n(EX, ZWEI_PI * fa), rot_n(n, ZWEI_PI * fi))
    else:
        Rm = rot_n(EX, ZWEI_PI * lam * (fa - fi))
    return drehe_perlen(netz, X0, Rm)


def staley_pfad(netz, X0, K1, K2):
    bilder = [staley_bild(netz, X0, s=s) for s in np.linspace(0.0, 1.0, K1 + 1)]
    bilder += [staley_bild(netz, X0, lam=l) for l in np.linspace(1.0, 0.0, K2 + 1)[1:]]
    return np.stack(bilder)


def kompensiert(netz, X, theta):
    """Rot(x, (4 pi - theta) k(t)) je Perle, k = (fa + fi)/2: Koerper von Rot(x, theta) nach Rot(x, 4 pi) = I."""
    r = np.sqrt((X * X).sum(-1))
    fa, fi = rampen(t_rad(r))
    Rm = rot_n(EX, (VIER_PI - theta) * 0.5 * (fa + fi))
    Y = np.einsum("bij,bj->bi", Rm, X)
    # Ansatzperlen: auf R_ATT u_i (Koerper bei 4 pi = I), Anker unveraendert
    for i in range(4):
        Y[netz.bead(i, 0)] = g1.R_ATT * g1.U_TET[i]
        Y[netz.bead(i, netz.ns)] = g1.R_ANK * g1.U_TET[i]
    return Y


def trivial_pfad(netz, X0, K):
    r = np.sqrt((X0 * X0).sum(-1))
    t = t_rad(r)
    bilder = []
    for s in np.linspace(0.0, 1.0, K + 1):
        Rm = rot_n(EX, np.pi * np.sin(np.pi * s) * np.sin(np.pi * t))
        bilder.append(drehe_perlen(netz, X0, Rm))
    out = np.stack(bilder)
    out[-1] = X0
    return out


def windungen_um(netz, X, achse):
    """Windung jedes Fadens um eine Achse, vom Anker zum Ansatz (wie g1.windungen); X (nb,B,3) -> (B,4)."""
    nrm = np.asarray(achse, float)
    nrm = nrm / np.linalg.norm(nrm)
    ref = np.array([0.0, 0.0, 1.0]) if abs(nrm[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
    e1 = np.cross(nrm, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(nrm, e1)
    B = X.shape[1]
    W = np.zeros((B, 4))
    for i in range(4):
        idx = [netz.bead(i, k) for k in range(netz.ns, -1, -1)]
        x = X[idx]
        phi = np.arctan2((x * e2).sum(-1), (x * e1).sum(-1))
        dphi = np.diff(phi, axis=0)
        dphi = (dphi + np.pi) % (2.0 * np.pi) - np.pi
        W[:, i] = dphi.sum(0) / (2.0 * np.pi)
    return W


def wxyz(netz, X):
    return {"Wx": windungen_um(netz, X, [1, 0, 0]), "Wy": windungen_um(netz, X, [0, 1, 0]),
            "Wz": windungen_um(netz, X, [0, 0, 1])}


def entwirrt(netz, X, E, E_ref):
    """PLAN A5: gerundete Windungen um x, y, z alle 0 und E <= 1,10 E_ref (Koerper bei 720 Grad = I)."""
    w = wxyz(netz, X)
    nullw = np.ones(X.shape[1], bool)
    for k in ("Wx", "Wy", "Wz"):
        nullw &= (np.abs(np.round(w[k])) < 0.5).all(1)
    return nullw & (E <= 1.10 * E_ref), w


def sonde_bilder(netz, P, chunk=400):
    """Sonde je Bild (K,nb,3) und zwischen Nachbarbildern (GUERTEL-1 string_pfad-Pruefung)."""
    K = P.shape[0]
    de_l, dp_l, rh_l, rr_l, E_l = [], [], [], [], []
    for a in range(0, K, chunk):
        Pa = P[a:a + chunk]
        Bc = Pa.shape[0]
        st = g1.Stapel(netz, [0] * Bc, np.zeros(Bc))
        X = np.ascontiguousarray(Pa.transpose(1, 0, 2)).copy()
        cb = st.setze_fest(X)
        E, _, so = g1.energie(st, X, cb, grad=False)
        de, dp, rh, rr = so
        de_l.append(de)
        dp_l.append(dp)
        rh_l.append(rh)
        rr_l.append(rr)
        E_l.append(E)
    de = np.concatenate(de_l)
    dp = np.concatenate(dp_l)
    rh = np.concatenate(rh_l)
    rr = np.concatenate(rr_l)
    E = np.concatenate(E_l)
    delta = np.sqrt(((P[1:] - P[:-1]) ** 2).sum(-1)).max(1) if K > 1 else np.zeros(0)
    rand_ff = np.minimum(dp[:-1], dp[1:]) - 2.0 * delta if K > 1 else np.zeros(0)
    rand_k = np.minimum(rh[:-1], rh[1:]) - delta - g1.A_KOERPER if K > 1 else np.zeros(0)
    bild_ok = (de >= g1.GRENZE_FF) & (rh >= g1.A_KOERPER) & (rr <= g1.R_AUSSEN)
    return {"E": E, "min_ff": de, "min_rho": rh, "max_r": rr, "bild_ok": bild_ok,
            "max_bildabstand": delta, "rand_ff_zwischen": rand_ff, "rand_k_zwischen": rand_k}


def sonde_zusammen(sb):
    K = len(sb["E"])
    z = {"bilder": K, "bilder_ok": int(sb["bild_ok"].sum()), "alle_bilder_ok": bool(sb["bild_ok"].all()),
         "min_ff": float(sb["min_ff"].min()), "min_rho": float(sb["min_rho"].min()), "max_r": float(sb["max_r"].max())}
    if K > 1:
        z.update({"min_rand_ff_zwischen": float(sb["rand_ff_zwischen"].min()),
                  "min_rand_k_zwischen": float(sb["rand_k_zwischen"].min()),
                  "max_bildabstand": float(sb["max_bildabstand"].max()),
                  "zwischen_ok": bool((sb["rand_ff_zwischen"] > 0).all() and (sb["rand_k_zwischen"] > 0).all())})
    return z


def fire_rec(st, X, nmax, ftol, sonde, dtmax=0.01, dtstart=0.002, cap=0.01, rec=None):
    """Wortgleiche Kopie von g1.fire (gleiche Arithmetik) mit Aufzeichnungs-Haken nach jedem Schritt."""
    B = st.B
    cb = st.setze_fest(X)
    E, G, so = g1.energie(st, X, cb)
    F = -G
    v = np.zeros_like(X)
    dt = np.full(B, dtstart)
    alpha = np.full(B, 0.1)
    npos = np.zeros(B, int)
    fmax = g1.fmax_von(F)
    it = 0
    for it in range(nmax):
        aktiv = fmax > ftol
        if not aktiv.any():
            break
        Pw = (F * v).sum((0, 2))
        vn = np.sqrt((v * v).sum((0, 2)))
        fn = np.sqrt((F * F).sum((0, 2))) + 1.0e-300
        pos = Pw > 0.0
        v = np.where(pos[None, :, None],
                     (1.0 - alpha)[None, :, None] * v + (alpha * vn / fn)[None, :, None] * F, 0.0)
        hoch = pos & (npos >= 5)
        dt = np.where(hoch, np.minimum(dt * 1.1, dtmax), np.where(pos, dt, np.maximum(dt * 0.5, 1.0e-7)))
        alpha = np.where(hoch, alpha * 0.99, np.where(pos, alpha, 0.1))
        npos = np.where(pos, npos + 1, 0)
        v = v + F * dt[None, :, None]
        dx = v * dt[None, :, None]
        dmax = np.sqrt((dx * dx).sum(-1)).max(0)
        sc = np.where(dmax > cap, cap / np.maximum(dmax, 1.0e-300), 1.0) * aktiv
        dx *= sc[None, :, None]
        v *= sc[None, :, None]
        sonde.vor(so, dmax * sc)
        X += dx
        if rec is not None:
            rec(X)
        E, G, so = g1.energie(st, X, cb)
        F = -G
        fmax = g1.fmax_von(F)
    sonde.vor(so, np.zeros(B))
    return X, E, fmax, it, so


class Rekorder:
    """Speichert System 0, sobald sich eine Perle seit dem letzten Eintrag um >= schwelle bewegt hat."""

    def __init__(self, schwelle):
        self.schwelle = schwelle
        self.X = []
        self.theta = []
        self.th = 0.0

    def zwang(self, X0):
        self.X.append(X0.copy())
        self.theta.append(self.th)

    def __call__(self, X):
        X0 = X[:, 0]
        if not self.X:
            self.zwang(X0)
            return
        d = np.sqrt(((X0 - self.X[-1]) ** 2).sum(-1)).max()
        if d >= self.schwelle:
            self.zwang(X0)


def lade_g1(eingaben, lfak, gidx):
    d = np.load(os.path.join(eingaben, "protokoll-L%.1f.npz" % lfak))
    return d["X"][gidx][:, 0, :].copy(), float(d["gitter"][gidx])


def energie_einzel(netz, X):
    st = g1.Stapel(netz, [0], np.zeros(1))
    Xb = X[:, None, :].copy()
    cb = st.setze_fest(Xb)
    E, _, so = g1.energie(st, Xb, cb, grad=False)
    return float(E[0]), [float(s[0]) for s in so]


def modus_leiter(args):
    t0 = time.time()
    netz = g1.Netz(args.lfak)
    B0, _ = lade_g1(args.eingaben, args.lfak, 0)
    E_B0, _ = energie_einzel(netz, B0)
    T0s = [float(x) for x in args.leiter.split(",")]
    sysl, th, X0, T0l, wl = [], [], [], [], []
    for T in T0s:
        for s in range(args.saaten):
            sysl.append(0)
            th.append(0.0)
            X0.append(B0)
            T0l.append(T)
            wl.append(0.0)
    if args.mit720:
        XW, gw = lade_g1(args.eingaben, args.lfak, 24)
        assert abs(gw - 720.0) < 1e-9
        for T in [float(x) for x in args.leiter720.split(",")]:
            for s in range(args.saaten):
                sysl.append(0)
                th.append(0.0)
                X0.append(XW)
                T0l.append(T)
                wl.append(720.0)
    st = g1.Stapel(netz, sysl, np.array(th))
    X = np.ascontiguousarray(np.stack(X0, axis=1))
    cb = st.setze_fest(X)
    E0 = g1.energie(st, X, cb, grad=False)[0]
    rng = np.random.default_rng([42, int(round(args.lfak * 10)), args.saat_basis])
    son = g1.Sonde(st.B)
    T0a = np.array(T0l)
    X, E, _, so = g1.langevin(st, X, args.nL, T0a, rng, son, args.dt0, args.capl)
    X, E, fmax, it, so = g1.fire(st, X, args.nF, args.ftol, son)
    ok = son.ok()
    ent, w = entwirrt(netz, X, E, E_B0)
    aus = {"kopf": kopf(args), "E_B0": E_B0, "winkel": wl, "T0": T0l, "E_start": E0, "E_end": E,
           "fmax_end": fmax, "sonde": son.als_dict(), "sonde_ok": ok, "entwirrt": ent,
           "Wx": w["Wx"], "Wy": w["Wy"], "Wz": w["Wz"], "laufzeit_s": time.time() - t0, "maxrss_mb": maxrss_mb()}
    m0 = (np.array(wl) == 0.0) & ok
    ibest = int(np.argmin(np.where(m0, E, np.inf)))
    np.savez_compressed(os.path.join(args.aus, "leiter-L%.1f.npz" % args.lfak), X_end=X, X_best0=X[:, ibest])
    schreibe_json(os.path.join(args.aus, "leiter-L%.1f.json" % args.lfak), aus)
    print("leiter fertig L=%.1f B=%d laufzeit %.1f s" % (args.lfak, st.B, aus["laufzeit_s"]))


def protokoll_fein(netz, lfak, schwelle, tmax):
    """Wiederholung des GUERTEL-1-Drehprotokolls (drei Systeme, gleiche Saat und Parameter) bis tmax mit
    Aufzeichnung von System 0 (zweizaehlig). Gibt (theta-Liste, Zustaende, Zustand bei tmax) zurueck."""
    st = g1.Stapel(netz, [0, 1, 2], np.zeros(3))
    X = g1.startzustand(st, 4100 + int(round(lfak * 10)))
    son = g1.Sonde(st.B)
    X, E, fmax, it, so = g1.fire(st, X, 5000, 1.0e-3, son)
    X, E, fmax, it, so = fire_rec(st, X, 1500, 1.0e-3, son)  # Gitterwinkel 0
    rec = Rekorder(schwelle)
    rec.th = 0.0
    rec.zwang(X[:, 0])
    gitter = [g for g in g1.GITTER if g <= tmax + 1e-9]
    for j in range(1, int(round(tmax)) + 1):
        st.theta[:] = np.deg2rad(float(j))
        rec.th = np.deg2rad(float(j))
        st.setze_fest(X)
        rec(X)
        X, E, fmax, it, so = fire_rec(st, X, 80, 1.0e-3, son, rec=rec)
        if any(abs(j - g) < 1e-9 for g in gitter):
            X, E, fmax, it, so = fire_rec(st, X, 1500, 1.0e-3, son, rec=rec)
    rec.zwang(X[:, 0])
    return rec.theta, rec.X, X[:, 0].copy(), float(E[0]), son.als_dict(0)


def modus_pfad(args):
    t0 = time.time()
    netz = g1.Netz(args.lfak)
    B0, _ = lade_g1(args.eingaben, args.lfak, 0)
    E_B0, so_B0 = energie_einzel(netz, B0)
    aus = {"kopf": kopf(args), "E_B0": E_B0, "sonde_B0": so_B0}
    pfade = {}
    # --- Staley-Weg (Bau) und GZ0a ---
    ST = staley_pfad(netz, B0, args.K1, args.K2)
    sb = sonde_bilder(netz, ST)
    aus["gz0a_staley"] = sonde_zusammen(sb)
    aus["gz0a_staley_je_bild"] = {k: sb[k] for k in ("min_ff", "min_rho", "max_r")}
    aus["staley_E_anfang"] = sb["E"]
    # --- S1: FIRE-Relaxation der idealen 4-pi-Wicklung (mit Rahmen) + Staley ---
    st1 = g1.Stapel(netz, [0], np.zeros(1))
    X = ST[0][:, None, :].copy()
    rec = Rekorder(args.schwelle)
    rec.zwang(X[:, 0])
    son1 = g1.Sonde(1)
    X, E1, fm1, it1, so1 = fire_rec(st1, X, args.nfire4pi, 1.0e-3, son1, rec=rec)
    rec.zwang(X[:, 0])
    ent1, w1 = entwirrt(netz, X, E1, E_B0)
    aus["start_S1"] = {"E": float(E1[0]), "fmax": float(fm1[0]), "fire_schritte": int(it1),
                       "sonde": son1.als_dict(0), "entwirrt": bool(ent1[0]),
                       "Wx": w1["Wx"][0], "Wy": w1["Wy"][0], "Wz": w1["Wz"][0], "rahmen": len(rec.X)}
    fr = np.stack(rec.X)
    sbf = sonde_bilder(netz, fr)
    aus["s1_fire_rahmen_sonde"] = sonde_zusammen(sbf)
    S1 = np.concatenate([fr[::-1], ST[1:]], axis=0)
    pfade["S1"] = S1
    # --- S0: trivialer Weg 0 -> 0 ---
    S0 = trivial_pfad(netz, B0, args.K1)
    sb0 = sonde_bilder(netz, S0)
    aus["s0_anfang_sonde"] = sonde_zusammen(sb0)
    pfade["S0"] = S0
    # --- S2: Zwischenrast (nur mit --mit_s2) ---
    if args.mit_s2:
        ths, Xs, X720, E720, son_p = protokoll_fein(netz, args.lfak, args.schwelle, 720.0)
        XW, _ = lade_g1(args.eingaben, args.lfak, 24)
        B0p = Xs[0]
        aus["reproduktion"] = {"max_abw_720_gegen_g1": float(np.abs(X720 - XW).max()),
                               "max_abw_0_gegen_g1": float(np.abs(B0p - B0).max()),
                               "E_720_neu": E720, "aufzeichnungen": len(Xs), "sonde_protokoll": son_p}
        ent_w, ww = entwirrt(netz, X720[:, None, :], np.array([E720]), E_B0)
        aus["start_S2"] = {"E": E720, "Wx": ww["Wx"][0], "Wy": ww["Wy"][0], "Wz": ww["Wz"][0],
                           "entwirrt": bool(ent_w[0])}
        Q = np.stack([kompensiert(netz, Xs[j], ths[j]) for j in range(len(Xs))])
        sbq = sonde_bilder(netz, Q)
        aus["s2_kompensiert_sonde"] = sonde_zusammen(sbq)
        STp = staley_pfad(netz, B0p, args.K1, args.K2)
        aus["s2_naht_abw"] = float(np.abs(Q[0] - STp[0]).max())
        S2 = np.concatenate([Q[::-1], STp[1:]], axis=0)
        pfade["S2"] = S2
    # --- Umverteilung auf M Bilder, Sonde der Anfangsstrings ---
    out = {}
    for name, P in pfade.items():
        Pm = g1.reparam(P, args.bilder, netz.frei)
        sbm = sonde_bilder(netz, Pm)
        aus["anfang_%s" % name] = {"fein_bilder": int(P.shape[0]), "sonde_M": sonde_zusammen(sbm),
                                   "E_profil_M": sbm["E"]}
        out[name] = Pm
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    np.savez_compressed(os.path.join(args.aus, "pfad-L%.1f.npz" % args.lfak), **out)
    schreibe_json(os.path.join(args.aus, "pfad-L%.1f.json" % args.lfak), aus)
    print("pfad fertig L=%.1f laufzeit %.1f s" % (args.lfak, aus["laufzeit_s"]))


def string_relax(netz, P0, niter, dts, cap, reparam_alle, log_alle):
    """Vereinfachte Stringmethode (wie GUERTEL-1) mit festen Endpunkten und laufender Durchdringungsprobe."""
    M = P0.shape[0]
    st = g1.Stapel(netz, [0] * M, np.zeros(M))
    Xs = np.ascontiguousarray(P0.transpose(1, 0, 2)).copy()
    cb = st.setze_fest(Xs)
    lauf_ff = np.full(M, np.inf)
    lauf_rho = np.full(M, np.inf)
    lauf_r = np.zeros(M)
    lauf_rand_ff = np.full(M, np.inf)
    lauf_rand_k = np.full(M, np.inf)
    verlauf = []
    for it in range(niter):
        E, G, so = g1.energie(st, Xs, cb)
        de, dp, rh, rr = so
        lauf_ff = np.minimum(lauf_ff, de)
        lauf_rho = np.minimum(lauf_rho, rh)
        lauf_r = np.maximum(lauf_r, rr)
        if it % log_alle == 0:
            verlauf.append({"it": it, "S": float(E.max() - E[0]), "S_wort": float(E.max() - E[-1]),
                            "imax": int(np.argmax(E)), "E_max": float(E.max())})
        F = -G
        F[:, 0] = 0.0
        F[:, -1] = 0.0
        dx = F * dts
        dn = np.sqrt((dx * dx).sum(-1))
        dx *= np.minimum(1.0, cap / np.maximum(dn, 1.0e-300))[..., None]
        dmax = np.sqrt((dx * dx).sum(-1)).max(0)
        Xs += dx
        if it % reparam_alle == reparam_alle - 1:
            alt = Xs.copy()
            Xs = np.ascontiguousarray(g1.reparam(Xs.transpose(1, 0, 2).copy(), M, netz.frei).transpose(1, 0, 2))
            st.setze_fest(Xs)
            dmax = dmax + np.sqrt(((Xs - alt) ** 2).sum(-1)).max(0)
        lauf_rand_ff = np.minimum(lauf_rand_ff, dp - 2.0 * dmax)
        lauf_rand_k = np.minimum(lauf_rand_k, rh - dmax - g1.A_KOERPER)
    E, G, so = g1.energie(st, Xs, cb)
    verlauf.append({"it": niter, "S": float(E.max() - E[0]), "S_wort": float(E.max() - E[-1]),
                    "imax": int(np.argmax(E)), "E_max": float(E.max())})
    F = -G
    F[:, 0] = 0.0
    F[:, -1] = 0.0
    P = Xs.transpose(1, 0, 2).copy()
    sb = sonde_bilder(netz, P)
    lauf = {"min_ff": float(lauf_ff.min()), "min_rho": float(lauf_rho.min()), "max_r": float(lauf_r.max()),
            "min_rand_ff_schritt": float(lauf_rand_ff.min()), "min_rand_k_schritt": float(lauf_rand_k.min())}
    lauf["ok"] = bool(lauf["min_ff"] >= g1.GRENZE_FF and lauf["min_rho"] >= g1.A_KOERPER
                      and lauf["max_r"] <= g1.R_AUSSEN and lauf["min_rand_ff_schritt"] > 0
                      and lauf["min_rand_k_schritt"] > 0)
    return P, E, F, sb, lauf, verlauf


def modus_string(args):
    t0 = time.time()
    netz = g1.Netz(args.lfak)
    B0, _ = lade_g1(args.eingaben, args.lfak, 0)
    E_B0, _ = energie_einzel(netz, B0)
    d = np.load(os.path.join(args.aus_pfad, "pfad-L%.1f.npz" % args.lfak))
    P0 = d[args.welcher]
    if args.bilder_kontrolle and P0.shape[0] != args.bilder_kontrolle:
        raise SystemExit("Bilderzahl passt nicht")
    P, E, F, sb, lauf, verlauf = string_relax(netz, P0, args.niter, args.dts, args.cap, 5, args.log_alle)
    zus = sonde_zusammen(sb)
    gueltig = bool(zus["alle_bilder_ok"] and zus.get("zwischen_ok", True) and lauf["ok"])
    X = np.ascontiguousarray(P.transpose(1, 0, 2))
    ent, w = entwirrt(netz, X, E, E_B0)
    st = g1.Stapel(netz, [0] * P.shape[0], np.zeros(P.shape[0]))
    Wx_alle = g1.windungen(st, X)
    imax = int(np.argmax(E))
    # lokale Minima des Profils (beschreibend)
    lm = [k for k in range(1, len(E) - 1) if E[k] < E[k - 1] and E[k] <= E[k + 1]]
    aus = {"kopf": kopf(args), "welcher": args.welcher, "E_B0": E_B0, "E_profil": E,
           "S_plan": float(E.max() - E[0]), "S_wort": float(E.max() - E[-1]), "H": float(E.max() - E_B0),
           "imax": imax, "E_anfang": float(E[0]), "E_ende": float(E[-1]), "E_max": float(E.max()),
           "pruefung_end": zus, "pruefung_lauf": lauf, "gueltig": gueltig,
           "anfang_entwirrt": bool(ent[0]), "ende_entwirrt": bool(ent[-1]),
           "W_anfang": {k: w[k][0] for k in w}, "W_ende": {k: w[k][-1] for k in w},
           "Wx_je_bild": Wx_alle, "lokale_minima": [{"k": k, "E": float(E[k]), "Wx": Wx_alle[k]} for k in lm],
           "fmax_bilder": g1.fmax_von(F), "verlauf": verlauf, "laufzeit_s": time.time() - t0,
           "maxrss_mb": maxrss_mb()}
    np.savez_compressed(os.path.join(args.aus, "string-%s-L%.1f.npz" % (args.welcher, args.lfak)), P=P)
    schreibe_json(os.path.join(args.aus, "string-%s-L%.1f.json" % (args.welcher, args.lfak)), aus)
    print("string %s fertig L=%.1f laufzeit %.1f s" % (args.welcher, args.lfak, aus["laufzeit_s"]))


# =====================================================================================
# Teil B: Orientierungsfeld
# =====================================================================================

def qmul(a, b):
    w1, x1, y1, z1 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    w2, x2, y2, z2 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], -1)


def qachse(n, alpha):
    """Einheitsquaternion fuer Drehung um n (...,3) um alpha (...)."""
    alpha = np.asarray(alpha, float)
    n = np.broadcast_to(np.asarray(n, float), alpha.shape + (3,))
    return np.concatenate([np.cos(alpha / 2.0)[..., None], n * np.sin(alpha / 2.0)[..., None]], -1)


def qexp(eta):
    """Drehvektor eta (...,3) -> Quaternion."""
    a = np.sqrt((eta * eta).sum(-1))
    n = eta / np.maximum(a, 1.0e-300)[..., None]
    return qachse(n, a)


class Feld:
    def __init__(self, dim, r0, R, chunk=8):
        self.dim, self.r0, self.R, self.chunk = dim, float(r0), float(R), chunk
        n = int(np.ceil(R)) + 1
        ax = np.arange(-n, n + 1)
        grids = np.meshgrid(*([ax] * dim), indexing="ij")
        pts = np.stack([g.ravel() for g in grids], 1)
        r = np.sqrt((pts * pts).sum(1).astype(float))
        keep = r <= R + 1.0 + 1e-9
        pts, r = pts[keep], r[keep]
        self.N = len(pts)
        self.r = r
        lut = -np.ones((2 * n + 1,) * dim, int)
        lut[tuple((pts + n).T)] = np.arange(self.N)
        al, bl = [], []
        for d in range(dim):
            e = np.zeros(dim, int)
            e[d] = 1
            nb = pts + e
            ok = (nb <= n).all(1)
            j = np.full(self.N, -1)
            j[ok] = lut[tuple((nb[ok] + n).T)]
            m = j >= 0
            al.append(np.nonzero(m)[0])
            bl.append(j[m])
        self.a = np.concatenate(al)
        self.b = np.concatenate(bl)
        self.nbond = len(self.a)
        self.kern = r <= self.r0 + 1e-9
        self.rand = r > self.R + 1e-9
        self.frei = ~self.kern & ~self.rand
        rc = np.maximum(r, self.r0)
        if dim == 3:
            h = (1.0 / rc - 1.0 / self.R) / (1.0 / self.r0 - 1.0 / self.R)
        else:
            h = np.log(self.R / rc) / np.log(self.R / self.r0)
        h = np.clip(h, 0.0, 1.0)
        h[self.kern] = 1.0
        h[self.rand] = 0.0
        self.h = h
        ones = np.ones(self.nbond)
        idx = np.arange(self.nbond)
        self.inc_a = sps.csr_matrix((ones, (self.a, idx)), shape=(self.N, self.nbond))
        self.inc_b = sps.csr_matrix((ones, (self.b, idx)), shape=(self.N, self.nbond))
        self.k = 4 if dim == 3 else 1

    # --- Energie, Gradient, Sonde ---
    def energie(self, x, grad=True):
        """x (N,B,k). 3D: E = sum 4(1-(q_a.q_b)^2) = sum (3 - tr R_a^T R_b); Sonde: min q_a.q_b (> 0: kein Gittersprung).
        2D: E = sum 2(1-cos(phi_a-phi_b)) = sum (2 - tr R_a^T R_b); Sonde: max |phi_a - phi_b| (< pi)."""
        B = x.shape[1]
        E = np.zeros(B)
        mon = np.zeros(B)
        G = np.zeros_like(x) if grad else None
        for s in range(0, B, self.chunk):
            xs = x[:, s:s + self.chunk]
            bb = xs.shape[1]
            xa = xs[self.a]
            xb = xs[self.b]
            if self.dim == 3:
                c = (xa * xb).sum(-1)
                E[s:s + bb] = (4.0 * (1.0 - c * c)).sum(0)
                mon[s:s + bb] = c.min(0)
                if grad:
                    f = (-8.0 * c)[..., None]
                    ga = (f * xb).reshape(self.nbond, -1)
                    gb = (f * xa).reshape(self.nbond, -1)
                    G[:, s:s + bb] = (self.inc_a @ ga + self.inc_b @ gb).reshape(self.N, bb, 4)
            else:
                d = (xa - xb)[..., 0]
                E[s:s + bb] = (2.0 * (1.0 - np.cos(d))).sum(0)
                mon[s:s + bb] = np.abs(d).max(0)
                if grad:
                    sn = 2.0 * np.sin(d)
                    G[:, s:s + bb, 0] = self.inc_a @ sn - self.inc_b @ sn
        return E, G, mon

    def gueltig(self, mon):
        return mon > 0.0 if self.dim == 3 else mon < np.pi

    def tang(self, G, x):
        if self.dim == 3:
            G = G - (G * x).sum(-1, keepdims=True) * x
        G = G.copy()
        G[~self.frei] = 0.0
        return G

    def norm(self, x):
        if self.dim == 3:
            return x / np.sqrt((x * x).sum(-1, keepdims=True))
        return x

    def setze(self, x, theta):
        """Kern auf Drehung um z mit Winkel theta (rad, stetig), Rand auf Identitaet."""
        if self.dim == 3:
            x[self.kern] = qachse(np.array([0.0, 0.0, 1.0]), np.array(theta))[None]
            x[self.rand] = np.array([1.0, 0.0, 0.0, 0.0])
        else:
            x[self.kern] = theta
            x[self.rand] = 0.0
        return x

    def null(self, B=1):
        x = np.zeros((self.N, B, self.k))
        if self.dim == 3:
            x[..., 0] = 1.0
        return x

    def praediktor(self, x, dth):
        if self.dim == 3:
            dq = qachse(np.array([0.0, 0.0, 1.0]), dth * self.h)[:, None, :]
            y = qmul(dq, x)
            x = np.where(self.frei[:, None, None], y, x)
        else:
            x = x + (dth * self.h * self.frei)[:, None, None]
        return x

    def rauschen(self, x, rng, sigma):
        if sigma <= 0:
            return x
        if self.dim == 3:
            eta = rng.normal(0.0, sigma / np.sqrt(3.0), x.shape[:-1] + (3,))
            y = qmul(qexp(eta), x)
            x = np.where(self.frei[:, None, None], y, x)
        else:
            x = x + rng.normal(0.0, sigma, x.shape) * self.frei[:, None, None]
        return x


def fire_feld(feld, x, nmax, ftol, dtmax, dtstart=0.02, capw=0.05, rec=None):
    B = x.shape[1]
    E, G, mon = feld.energie(x)
    F = -feld.tang(G, x)
    v = np.zeros_like(x)
    dt = np.full(B, dtstart)
    alpha = np.full(B, 0.1)
    npos = np.zeros(B, int)
    fmax = np.sqrt((F * F).sum(-1)).max(0)
    mon_lauf = mon.copy()
    it = 0
    for it in range(nmax):
        aktiv = fmax > ftol
        if not aktiv.any():
            break
        Pw = (F * v).sum((0, 2))
        vn = np.sqrt((v * v).sum((0, 2)))
        fn = np.sqrt((F * F).sum((0, 2))) + 1.0e-300
        pos = Pw > 0.0
        v = np.where(pos[None, :, None], (1.0 - alpha)[None, :, None] * v + (alpha * vn / fn)[None, :, None] * F, 0.0)
        hoch = pos & (npos >= 5)
        dt = np.where(hoch, np.minimum(dt * 1.1, dtmax), np.where(pos, dt, np.maximum(dt * 0.5, 1.0e-7)))
        alpha = np.where(hoch, alpha * 0.99, np.where(pos, alpha, 0.1))
        npos = np.where(pos, npos + 1, 0)
        v = v + F * dt[None, :, None]
        dx = v * dt[None, :, None]
        dn = np.sqrt((dx * dx).sum(-1)).max(0)
        sc = np.where(dn > capw, capw / np.maximum(dn, 1.0e-300), 1.0) * aktiv
        dx *= sc[None, :, None]
        v *= sc[None, :, None]
        x = feld.norm(x + dx)
        v = feld.tang(v, x)
        if rec is not None:
            rec(x)
        E, G, mon = feld.energie(x)
        mon_lauf = np.minimum(mon_lauf, mon) if feld.dim == 3 else np.maximum(mon_lauf, mon)
        F = -feld.tang(G, x)
        fmax = np.sqrt((F * F).sum(-1)).max(0)
    return x, E, fmax, it, mon, mon_lauf




def feld_protokoll(feld, args, rng):
    t0 = time.time()
    x = feld.setze(feld.null(1), 0.0)
    dth_deg = args.fdtheta
    nst = int(round(args.ftmax / dth_deg))
    E_l, mon_l, th_l = [], [], []
    gitter, Eg, mong, fmg, zust = [], [], [], [], {}
    x, E, fm, it, mon, _ = fire_feld(feld, x, args.fngitter, args.fftol, args.fdtmax)
    for j in range(0, nst + 1):
        th = j * dth_deg
        if j > 0:
            x = feld.praediktor(x, np.deg2rad(dth_deg))
            x = feld.setze(x, np.deg2rad(th))
            x = feld.rauschen(x, rng, args.frausch)
            x, E, fm, it, mon, _ = fire_feld(feld, x, args.fnrelax, args.fftol, args.fdtmax)
        E_l.append(float(E[0]))
        mon_l.append(float(mon[0]))
        th_l.append(th)
        if abs(th / args.fgitter - round(th / args.fgitter)) < 1e-9:
            x, E, fm, it, mon, _ = fire_feld(feld, x, args.fngitter, args.fftol, args.fdtmax)
            gitter.append(th)
            Eg.append(float(E[0]))
            mong.append(float(mon[0]))
            fmg.append(float(fm[0]))
            if abs(th / 180.0 - round(th / 180.0)) < 1e-9:
                zust["%d" % int(round(th))] = x[:, 0].copy()
    return {"theta_schritt": th_l, "E_schritt": E_l, "sonde_schritt": mon_l, "gitter": gitter, "E_gitter": Eg,
            "sonde_gitter": mong, "gueltig_gitter": [bool(feld.gueltig(np.array([m]))[0]) for m in mong],
            "fmax_gitter": fmg, "laufzeit_s": time.time() - t0}, zust


def feld_saaten(feld, args, zust, rng):
    t0 = time.time()
    out = {}
    for w in [int(x) for x in args.fsaatwinkel.split(",")]:
        x0 = zust["%d" % w]
        x = np.repeat(x0[:, None, :], args.fsaaten, axis=1)
        x = feld.rauschen(x, rng, args.fkick)
        x = feld.setze(x, np.deg2rad(float(w)))
        x, E, fm, it, mon, mon_l = fire_feld(feld, x, args.fnF, args.fftol, args.fdtmax)
        out["%d" % w] = {"E": E, "sonde": mon, "sonde_lauf": mon_l, "gueltig": feld.gueltig(mon),
                         "fmax": fm, "schritte": int(it)}
    return out, time.time() - t0


def reparam_feld(pfad, M, frei, norm):
    d = pfad[1:, frei] - pfad[:-1, frei]
    seg = np.sqrt((d * d).sum(tuple(range(1, d.ndim))))
    s = np.concatenate([[0.0], np.cumsum(seg)])
    ziel = np.linspace(0.0, s[-1], M)
    out = np.empty((M,) + pfad.shape[1:])
    j = np.clip(np.searchsorted(s, ziel, side="right") - 1, 0, len(s) - 2)
    for m in range(M):
        jj = j[m]
        w = 0.0 if seg[jj] <= 0 else min(max((ziel[m] - s[jj]) / seg[jj], 0.0), 1.0)
        out[m] = (1.0 - w) * pfad[jj] + w * pfad[jj + 1]
    out[0] = pfad[0]
    out[-1] = pfad[-1]
    return norm(out)


def feld_string(feld, args, rng):
    """Feld-Staley-Weg bei 720 Grad (nur dim 3): Start = FIRE-relaxierte harmonische 4-pi-Verdrillung."""
    t0 = time.time()
    h = feld.h
    fa = np.clip(2.0 * h, 0.0, 1.0)
    fi = np.clip(2.0 * h - 1.0, 0.0, 1.0)
    ez = np.array([0.0, 0.0, 1.0])
    bilder = []
    for s in np.linspace(0.0, 1.0, args.fK + 1):
        n = np.array([np.cos(np.pi * s), np.sin(np.pi * s), 0.0])
        bilder.append(qmul(qachse(ez, ZWEI_PI * fa), qachse(n, ZWEI_PI * fi)))
    for lam in np.linspace(1.0, 0.0, args.fK + 1)[1:]:
        bilder.append(qachse(ez, ZWEI_PI * lam * (fa - fi)))
    ST = np.stack(bilder)  # (K, N, 4)
    ST[:, feld.kern] = np.array([1.0, 0.0, 0.0, 0.0])  # Kern bei 720 Grad: q = +1
    ST[:, feld.rand] = np.array([1.0, 0.0, 0.0, 0.0])
    Es, _, mons = feld.energie(np.ascontiguousarray(ST.transpose(1, 0, 2)), grad=False)
    staley_info = {"E": Es, "sonde": mons, "alle_gueltig": bool((mons > 0).all())}
    # Start relaxieren (Symmetriebruch 1e-3), Rahmen alle 25 Schritte
    x = ST[0][:, None, :].copy()
    x = feld.rauschen(x, rng, args.frausch)
    rahmen = [x[:, 0].copy()]
    zaehler = {"n": 0}

    def rec(xx):
        zaehler["n"] += 1
        if zaehler["n"] % 25 == 0:
            rahmen.append(xx[:, 0].copy())

    x, E0, fm0, it0, mon0, monl0 = fire_feld(feld, x, args.fnfire4pi, args.fftol, args.fdtmax, rec=rec)
    rahmen.append(x[:, 0].copy())
    start = {"E": float(E0[0]), "fmax": float(fm0[0]), "schritte": int(it0), "sonde": float(mon0[0]),
             "sonde_lauf": float(monl0[0])}
    pfad = np.concatenate([np.stack(rahmen)[::-1], ST[1:]], axis=0)
    P = reparam_feld(pfad, args.fM, feld.frei, feld.norm)
    M = args.fM
    xs = np.ascontiguousarray(P.transpose(1, 0, 2))
    lauf_mon = np.full(M, np.inf)
    verlauf = []
    for it in range(args.fniter):
        E, G, mon = feld.energie(xs)
        lauf_mon = np.minimum(lauf_mon, mon)
        if it % 50 == 0:
            verlauf.append({"it": it, "S": float(E.max() - E[0]), "S_wort": float(E.max() - E[-1]),
                            "imax": int(np.argmax(E))})
        F = -feld.tang(G, xs)
        F[:, 0] = 0.0
        F[:, -1] = 0.0
        dx = F * args.fdts
        dn = np.sqrt((dx * dx).sum(-1))
        dx *= np.minimum(1.0, args.fcap / np.maximum(dn, 1.0e-300))[..., None]
        xs = feld.norm(xs + dx)
        if it % 5 == 4:
            xs = np.ascontiguousarray(reparam_feld(xs.transpose(1, 0, 2).copy(), M, feld.frei,
                                                   feld.norm).transpose(1, 0, 2))
    E, G, mon = feld.energie(xs)
    lauf_mon = np.minimum(lauf_mon, mon)
    verlauf.append({"it": args.fniter, "S": float(E.max() - E[0]), "S_wort": float(E.max() - E[-1]),
                    "imax": int(np.argmax(E))})
    nachbar = (xs[:, 1:] * xs[:, :-1]).sum(-1).min(0)  # je Nachbarpaar: min ueber Plaetze q_k . q_k+1
    gueltig = bool((mon > 0).all() and (lauf_mon > 0).all() and (nachbar > 0).all())
    return {"staley_anfang": staley_info, "start": start, "E_profil": E, "sonde_bilder": mon,
            "sonde_lauf": lauf_mon, "nachbar_min": nachbar, "gueltig": gueltig,
            "S_plan": float(E.max() - E[0]), "S_wort": float(E.max() - E[-1]), "imax": int(np.argmax(E)),
            "E_anfang": float(E[0]), "E_ende": float(E[-1]), "verlauf": verlauf, "laufzeit_s": time.time() - t0}


def modus_feld(args):
    t0 = time.time()
    tag = "feld-%dd-r%g-R%g" % (args.dim, args.r0, args.R)
    feld = Feld(args.dim, args.r0, args.R, chunk=args.fchunk)
    rng = np.random.default_rng([42, args.dim, int(round(args.r0 * 10)), int(round(args.R))])
    aus = {"kopf": kopf(args), "gitter_info": {"N": feld.N, "frei": int(feld.frei.sum()), "kern": int(feld.kern.sum()),
                                               "rand": int(feld.rand.sum()), "bindungen": feld.nbond}}
    teile = args.teil.split(",")
    zp = os.path.join(args.aus, tag + "-zust.npz")
    if "prot" in teile:
        pr, zust = feld_protokoll(feld, args, rng)
        aus["protokoll"] = pr
        np.savez_compressed(zp, **zust)
    if "saat" in teile:
        d = np.load(zp if "prot" in teile else os.path.join(args.aus_feld, tag + "-zust.npz"))
        zust = {k: d[k] for k in d.files}
        rng_s = np.random.default_rng([43, args.dim, int(round(args.r0 * 10)), int(round(args.R))])
        sa, ts = feld_saaten(feld, args, zust, rng_s)
        aus["saaten"] = sa
        aus["saaten_laufzeit_s"] = ts
        # Protokollzustand je Saatwinkel (Energie nach Gitter-FIRE) mitnehmen
        aus["saaten_protokollzustand"] = {}
        for w in sa:
            x = zust[w][:, None, :]
            E, _, mon = feld.energie(x, grad=False)
            aus["saaten_protokollzustand"][w] = {"E": float(E[0]), "sonde": float(mon[0]),
                                                 "gueltig": bool(feld.gueltig(mon)[0])}
    if "string" in teile:
        rng_t = np.random.default_rng([44, args.dim, int(round(args.r0 * 10)), int(round(args.R))])
        aus["string"] = feld_string(feld, args, rng_t)
    aus["laufzeit_s"] = time.time() - t0
    aus["maxrss_mb"] = maxrss_mb()
    name = tag + ("-" + args.teil.replace(",", "-"))
    schreibe_json(os.path.join(args.aus, name + ".json"), aus)
    print("feld fertig %s teil=%s laufzeit %.1f s" % (tag, args.teil, aus["laufzeit_s"]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("modus", choices=["leiter", "pfad", "string", "feld"])
    p.add_argument("--aus", default=".")
    p.add_argument("--eingaben", default="../eingaben-g1")
    p.add_argument("--aus_pfad", default=".")
    p.add_argument("--aus_feld", default=".")
    # Teil A
    p.add_argument("--lfak", type=float, default=1.8)
    p.add_argument("--saaten", type=int, default=5)
    p.add_argument("--saat_basis", type=int, default=0)
    p.add_argument("--leiter", default="0.5,1,2,4")
    p.add_argument("--leiter720", default="1,2,4")
    p.add_argument("--mit720", type=int, default=0)
    p.add_argument("--nL", type=int, default=12000)
    p.add_argument("--nF", type=int, default=3000)
    p.add_argument("--dt0", type=float, default=2.0e-4)
    p.add_argument("--capl", type=float, default=0.01)
    p.add_argument("--ftol", type=float, default=1.0e-3)
    p.add_argument("--K1", type=int, default=360)
    p.add_argument("--K2", type=int, default=360)
    p.add_argument("--schwelle", type=float, default=0.02)
    p.add_argument("--nfire4pi", type=int, default=10000)
    p.add_argument("--mit_s2", type=int, default=0)
    p.add_argument("--bilder", type=int, default=201)
    p.add_argument("--bilder_kontrolle", type=int, default=0)
    p.add_argument("--welcher", default="S1")
    p.add_argument("--niter", type=int, default=2000)
    p.add_argument("--dts", type=float, default=1.0e-4)
    p.add_argument("--cap", type=float, default=0.005)
    p.add_argument("--log_alle", type=int, default=100)
    # Teil B
    p.add_argument("--dim", type=int, default=3)
    p.add_argument("--r0", type=float, default=6.0)
    p.add_argument("--R", type=float, default=24.0)
    p.add_argument("--teil", default="prot")
    p.add_argument("--fdtheta", type=float, default=5.0)
    p.add_argument("--ftmax", type=float, default=1440.0)
    p.add_argument("--fgitter", type=float, default=45.0)
    p.add_argument("--fnrelax", type=int, default=40)
    p.add_argument("--fngitter", type=int, default=300)
    p.add_argument("--fftol", type=float, default=1.0e-5)
    p.add_argument("--fdtmax", type=float, default=0.1)
    p.add_argument("--frausch", type=float, default=1.0e-3)
    p.add_argument("--fsaatwinkel", default="0,360,720,1080,1440")
    p.add_argument("--fsaaten", type=int, default=4)
    p.add_argument("--fkick", type=float, default=0.1)
    p.add_argument("--fnF", type=int, default=600)
    p.add_argument("--fK", type=int, default=40)
    p.add_argument("--fnfire4pi", type=int, default=3000)
    p.add_argument("--fM", type=int, default=25)
    p.add_argument("--fniter", type=int, default=400)
    p.add_argument("--fdts", type=float, default=0.02)
    p.add_argument("--fcap", type=float, default=0.05)
    p.add_argument("--fchunk", type=int, default=8)
    args = p.parse_args()
    os.makedirs(args.aus, exist_ok=True)
    {"leiter": modus_leiter, "pfad": modus_pfad, "string": modus_string, "feld": modus_feld}[args.modus](args)


if __name__ == "__main__":
    main()
