#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUERTEL-FELD-STAB-2 (Runde 43, RUNDE-37/guertel-feld-stab-2): Guertel-Trick im Feld auf (8, 16), (12, 24) und
(16, 32); Sprunggrenze theta_max des ungestossenen Vorwaertsasts; SO(2)-Kontrolle.

Synthetische Modellrechnung, keine Messdaten. Modell, Ablauf und Regeln: PLAN.md.
Feldmodell (SO(3) auf Z^3 bzw. SO(2) auf Z^2), FIRE und Drehprotokoll aus GUERTEL-2 (guertel2.py, Kopie, unveraendert,
sha256 c9374a98...; importiert guertel.py, sha256 795f474d...). Protokoll, Stoss und FIRE-Aufzeichnung aus
GUERTEL-FELD-STAB-1 (stab.py) kopiert und erweitert:
  - Protokoll mit Fortsetzungspunkt (Feld und Zufallszustand) und zusaetzlicher Aufzeichnung je Winkel;
  - Stoss fuer dim 2 (SO(2)): phi + eps sin(pi f_i), weil es dort keine Kipprichtung gibt.

Modi:
  prot   Drehprotokoll von --tmin bis --tmax (bei --tmin > 0 Fortsetzung ab --von); speichert die Zustaende bei
         --speicher und einen Fortsetzungspunkt bei tmax.
  stoss  Zustand bei --theta laden, stossen (eps = 0: ohne Stoss), dann FIRE bis --nmax Schritte mit Aufzeichnung.

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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guertel2 as g2  # noqa: E402  (GUERTEL-2, unveraendert)

EZ = np.array([0.0, 0.0, 1.0])
EY = np.array([0.0, 1.0, 0.0])
KONJ = np.array([1.0, -1.0, -1.0, -1.0])


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def kopf(args):
    return {"karte": "GUERTEL-FELD-STAB-2 (Runde 43)", "modus": args.modus, "args": vars(args),
            "code_sha256": sha_datei(os.path.abspath(__file__)),
            "g2_code_sha256": sha_datei(os.path.abspath(g2.__file__)),
            "g1_code_sha256": sha_datei(os.path.abspath(g2.g1.__file__)),
            "schreibzeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "numpy": np.__version__}


def maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def gitterpunkte(dim, R):
    """Dieselbe Platzliste wie g2.Feld.__init__ (gleiche Reihenfolge)."""
    n = int(np.ceil(R)) + 1
    ax = np.arange(-n, n + 1)
    grids = np.meshgrid(*([ax] * dim), indexing="ij")
    pts = np.stack([g.ravel() for g in grids], 1)
    r = np.sqrt((pts * pts).sum(1).astype(float))
    return pts[r <= R + 1.0 + 1e-9]


def linien(feld, pts):
    """Indizes der Plaetze auf der +x- und der +z-Achse (nur dim 3), radial nach aussen sortiert."""
    out = {}
    for name, d in (("x", 0), ("z", 2)):
        andere = [k for k in range(3) if k != d]
        m = (pts[:, andere[0]] == 0) & (pts[:, andere[1]] == 0) & (pts[:, d] >= 0)
        idx = np.nonzero(m)[0]
        out[name] = idx[np.argsort(pts[idx, d])]
    return out


def kipp_amplitude(feld, x):
    """P = Wurzel aus der Summe von q1^2 + q2^2 ueber freie Plaetze (nur dim 3)."""
    if feld.dim != 3:
        return None
    q = x[feld.frei, 0]
    return float(np.sqrt((q[:, 1] ** 2 + q[:, 2] ** 2).sum()))


def qz_aussen(feld, x):
    """Mittleres q_z der aeusseren Haelfte (h < 1/2) (nur dim 3): vorwaerts > 0, umgekehrt < 0."""
    if feld.dim != 3:
        return None
    m = feld.frei & (feld.h < 0.5)
    return float(x[m, 0, 3].mean())


def struktur(feld, x, lin):
    q = x[:, 0]
    fr = feld.frei
    aussen = fr & (feld.h < 0.5)
    innen = fr & (feld.h >= 0.5)
    if feld.dim != 3:
        return {"phi_mittel_aussen": float(q[aussen, 0].mean()), "phi_mittel_innen": float(q[innen, 0].mean())}
    return {"qz_mittel_aussen": float(q[aussen, 3].mean()), "qz_mittel_innen": float(q[innen, 3].mean()),
            "q0_min_frei": float(q[fr, 0].min()), "kipp_amplitude": kipp_amplitude(feld, x),
            "linie_x": q[lin["x"]], "linie_z": q[lin["z"]]}


def schlechter(feld, a, b):
    """Strengere der beiden Sonden: dim 3 Minimum von min q_a.q_b, dim 2 Maximum von max |phi_a - phi_b|."""
    return min(a, b) if feld.dim == 3 else max(a, b)


def protokoll(feld, args, rng, speicher, x=None, j0=0):
    """Arithmetik wortgleich wie g2.feld_protokoll und GFS-1 protokoll() (gleiche Zufallsfolge). Zusaetzlich:
    Fortsetzung ab Winkelindex j0 mit gegebenem x; je Winkel Sonde im Lauf (Minimum bzw. Maximum ueber alle
    FIRE-Schritte des Winkels, einschliesslich ihres Startzustands), q_z aussen und Kipp-Amplitude nach allen
    Relaxationen des Winkels; Zustaende bei den Winkeln in speicher."""
    t0 = time.time()
    dth_deg = args.fdtheta
    nst = int(round(args.tmax / dth_deg))
    E_l, mon_l, th_l = [], [], []
    gitter, Eg, mong, fmg, zust = [], [], [], [], {}
    lauf_s, lauf_g, qz_l, P_l = [], [], [], []
    if x is None:
        x = feld.setze(feld.null(1), 0.0)
        x, E, fm, it, mon, ml0 = g2.fire_feld(feld, x, args.fngitter, args.fftol, args.fdtmax)
        j0 = 0
    for j in range(j0, nst + 1):
        th = j * dth_deg
        if j > 0:
            x = feld.praediktor(x, np.deg2rad(dth_deg))
            x = feld.setze(x, np.deg2rad(th))
            x = feld.rauschen(x, rng, args.frausch)
            x, E, fm, it, mon, ml = g2.fire_feld(feld, x, args.fnrelax, args.fftol, args.fdtmax)
            sl = float(ml[0])
        else:
            sl = float(ml0[0])
        E_l.append(float(E[0]))
        mon_l.append(float(mon[0]))
        th_l.append(th)
        lauf_s.append(sl)
        if abs(th / args.fgitter - round(th / args.fgitter)) < 1e-9:
            x, E, fm, it, mon, mlg = g2.fire_feld(feld, x, args.fngitter, args.fftol, args.fdtmax)
            gitter.append(th)
            Eg.append(float(E[0]))
            mong.append(float(mon[0]))
            fmg.append(float(fm[0]))
            lauf_g.append(float(mlg[0]))
        qz_l.append(qz_aussen(feld, x))
        P_l.append(kipp_amplitude(feld, x))
        if any(abs(th - s) < 1e-9 for s in speicher):
            zust["%d" % int(round(th))] = x[:, 0].copy()
    return {"theta_schritt": th_l, "E_schritt": E_l, "sonde_schritt": mon_l, "sonde_lauf_schritt": lauf_s,
            "gitter": gitter, "E_gitter": Eg, "sonde_gitter": mong, "sonde_lauf_gitter": lauf_g,
            "fmax_gitter": fmg, "qz_aussen": qz_l, "kipp": P_l, "laufzeit_s": time.time() - t0}, zust, x, nst


def kipp(feld, x, theta_rad, eps):
    """Kopie aus GFS-1 (stab.py): Stoss in Staley-Richtung, Drillachse der inneren Haelfte (h >= 1/2) kippen.
    delta = eps sin(pi f_i), f_i = clip(2h - 1, 0, 1); q -> q_s q_y(delta) q_s^-1 q q_y(-delta), q_s = q_z(theta/2).
    Kern, Rand, aeussere Haelfte bleiben unveraendert."""
    fi = np.clip(2.0 * feld.h - 1.0, 0.0, 1.0)
    delta = eps * np.sin(np.pi * fi)
    delta[~feld.frei] = 0.0
    qs = g2.qachse(EZ, np.array(theta_rad / 2.0))
    qy = g2.qachse(EY, delta)
    qsb = np.broadcast_to(qs, qy.shape)
    A = g2.qmul(g2.qmul(qsb, qy), qsb * KONJ)
    y = g2.qmul(g2.qmul(A[:, None, :], x), (qy * KONJ)[:, None, :])
    y = feld.norm(y)
    x = np.where(feld.frei[:, None, None], y, x)
    return feld.setze(x, theta_rad), delta


def schub2d(feld, x, theta_rad, eps):
    """SO(2)-Stoss (dim 2): keine Kipprichtung vorhanden; dasselbe Sinusprofil in der einzigen Richtung,
    phi -> phi + eps sin(pi f_i) auf der inneren Haelfte. Kern und Rand bleiben."""
    fi = np.clip(2.0 * feld.h - 1.0, 0.0, 1.0)
    delta = eps * np.sin(np.pi * fi)
    delta[~feld.frei] = 0.0
    x = x + delta[:, None, None]
    return feld.setze(x, theta_rad), delta


def fire_log(feld, x, nmax, ftol, dtmax, dtstart=0.02, capw=0.05):
    """Wortgleiche Kopie von g2.fire_feld (gleiche Arithmetik) mit Aufzeichnung je Schritt wie GFS-1 fire_log:
    E, Sonde, fmax, Kipp-Amplitude (dim 3). Sonde im Lauf wie g2.fire_feld: dim 3 Minimum, dim 2 Maximum.
    Index 0 = Startzustand."""
    B = x.shape[1]
    E, G, mon = feld.energie(x)
    F = -feld.tang(G, x)
    v = np.zeros_like(x)
    dt = np.full(B, dtstart)
    alpha = np.full(B, 0.1)
    npos = np.zeros(B, int)
    fmax = np.sqrt((F * F).sum(-1)).max(0)
    mon_lauf = mon.copy()
    hE, hS, hF, hP = [float(E[0])], [float(mon[0])], [float(fmax[0])], [kipp_amplitude(feld, x)]
    schritte = 0
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
        E, G, mon = feld.energie(x)
        mon_lauf = np.minimum(mon_lauf, mon) if feld.dim == 3 else np.maximum(mon_lauf, mon)
        F = -feld.tang(G, x)
        fmax = np.sqrt((F * F).sum(-1)).max(0)
        schritte += 1
        hE.append(float(E[0]))
        hS.append(float(mon[0]))
        hF.append(float(fmax[0]))
        hP.append(kipp_amplitude(feld, x))
    return x, E, fmax, schritte, mon, mon_lauf, {"E": hE, "sonde": hS, "fmax": hF, "kipp": hP}


def modus_prot(args):
    t0 = time.time()
    feld = g2.Feld(args.dim, args.r0, args.R, chunk=args.fchunk)
    speicher = [float(s) for s in args.speicher.split(",")] if args.speicher else []
    von = None
    if args.tmin > 0:
        d = np.load(args.von)
        jv = int(d["j"])
        if abs(jv * args.fdtheta - args.tmin) > 1e-9:
            raise SystemExit("Fortsetzungspunkt passt nicht zu --tmin")
        x = d["x"].copy()
        rng = np.random.default_rng()
        rng.bit_generator.state = json.loads(str(d["rng"]))
        j0 = jv + 1
        von = {"datei": args.von, "sha256": sha_datei(args.von), "j": jv}
    else:
        x, j0 = None, 0
        rng = np.random.default_rng([42, args.dim, int(round(args.r0 * 10)), int(round(args.R))])  # wie g2.modus_feld
    pr, zust, x, nst = protokoll(feld, args, rng, speicher, x, j0)
    st = {}
    if zust:
        lin = linien(feld, gitterpunkte(3, args.R)) if args.dim == 3 else None
        for k, q in zust.items():
            E, _, mon = feld.energie(q[:, None, :], grad=False)
            s = struktur(feld, q[:, None, :], lin)
            s.update({"E": float(E[0]), "sonde": float(mon[0])})
            st[k] = s
    aus = {"kopf": kopf(args), "gitter_info": {"dim": feld.dim, "N": feld.N, "frei": int(feld.frei.sum()),
                                               "kern": int(feld.kern.sum()), "rand": int(feld.rand.sum()),
                                               "bindungen": feld.nbond},
           "fortsetzung_von": von, "protokoll": pr, "zustaende": st, "laufzeit_s": time.time() - t0,
           "maxrss_mb": maxrss_mb()}
    np.savez_compressed(os.path.join(args.aus, "prot-%s-zust.npz" % args.tag), **zust)
    np.savez_compressed(os.path.join(args.aus, "prot-%s-ck.npz" % args.tag), x=x, j=np.array(nst),
                        rng=np.array(json.dumps(rng.bit_generator.state)))
    g2.schreibe_json(os.path.join(args.aus, "prot-%s.json" % args.tag), aus)
    print("prot fertig tag=%s tmin=%g tmax=%g laufzeit %.1f s" % (args.tag, args.tmin, args.tmax, aus["laufzeit_s"]))


def modus_stoss(args):
    t0 = time.time()
    feld = g2.Feld(args.dim, args.r0, args.R, chunk=args.fchunk)
    d = np.load(args.zust)
    q0 = d["%d" % int(round(args.theta))]
    th = np.deg2rad(float(args.theta))
    lin = linien(feld, gitterpunkte(3, args.R)) if args.dim == 3 else None
    x = q0[:, None, :].copy()
    E_vor, _, mon_vor = feld.energie(x, grad=False)
    s_vor = struktur(feld, x, lin)
    if args.eps > 0.0:
        x, delta = (kipp if args.dim == 3 else schub2d)(feld, x, th, args.eps)
    else:
        x = feld.setze(x, th)
        delta = np.zeros(feld.N)
    E_nach, _, mon_nach = feld.energie(x, grad=False)
    s_nach = struktur(feld, x, lin)
    x, E, fm, schritte, mon, mon_l, hist = fire_log(feld, x, args.nmax, args.fftol, args.fdtmax)
    s_end = struktur(feld, x, lin)
    aus = {"kopf": kopf(args), "dim": feld.dim, "r0": feld.r0, "R": feld.R, "theta": float(args.theta),
           "eps": float(args.eps), "kipp_delta_max": float(delta.max()), "kipp_plaetze": int((delta > 0).sum()),
           "E_vor": float(E_vor[0]), "sonde_vor": float(mon_vor[0]), "struktur_vor": s_vor,
           "E_nach_stoss": float(E_nach[0]), "sonde_nach_stoss": float(mon_nach[0]), "struktur_nach_stoss": s_nach,
           "E_end": float(E[0]), "sonde_end": float(mon[0]), "sonde_lauf": float(mon_l[0]),
           "sonde_lauf_mit_start": schlechter(feld, float(mon_vor[0]), float(mon_l[0])),
           "fmax_end": float(fm[0]), "schritte": int(schritte), "struktur_end": s_end, "verlauf": hist,
           "laufzeit_s": time.time() - t0, "maxrss_mb": maxrss_mb()}
    name = "stoss-%s-T%d-e%g" % (args.tag, int(round(args.theta)), args.eps)
    np.savez_compressed(os.path.join(args.aus, name + "-end.npz"), q=x[:, 0])
    g2.schreibe_json(os.path.join(args.aus, name + ".json"), aus)
    print("stoss fertig %s schritte %d laufzeit %.1f s" % (name, schritte, aus["laufzeit_s"]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("modus", choices=["prot", "stoss"])
    p.add_argument("--aus", default=".")
    p.add_argument("--tag", required=True)
    p.add_argument("--dim", type=int, default=3)
    p.add_argument("--r0", type=float, default=12.0)
    p.add_argument("--R", type=float, default=24.0)
    p.add_argument("--tmin", type=float, default=0.0)
    p.add_argument("--tmax", type=float, default=720.0)
    p.add_argument("--von", default="")
    p.add_argument("--speicher", default="270,300,420,450")
    p.add_argument("--fdtheta", type=float, default=10.0)
    p.add_argument("--fgitter", type=float, default=90.0)
    p.add_argument("--fnrelax", type=int, default=30)
    p.add_argument("--fngitter", type=int, default=150)
    p.add_argument("--fftol", type=float, default=1.0e-5)
    p.add_argument("--fdtmax", type=float, default=0.1)
    p.add_argument("--frausch", type=float, default=1.0e-3)
    p.add_argument("--fchunk", type=int, default=8)
    p.add_argument("--zust", default="")
    p.add_argument("--theta", type=float, default=450.0)
    p.add_argument("--eps", type=float, default=0.0)
    p.add_argument("--nmax", type=int, default=3000)
    args = p.parse_args()
    os.makedirs(args.aus, exist_ok=True)
    {"prot": modus_prot, "stoss": modus_stoss}[args.modus](args)


if __name__ == "__main__":
    main()
