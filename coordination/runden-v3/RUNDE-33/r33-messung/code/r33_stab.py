#!/usr/bin/env python3
"""RUNDE-33 r33-messung (Code-Agent, 03.10.2026): Messseite des Blindtests R33, beta = 1, Fortsetzungen k = -3 .. -25.

Physik unveraendert aus bic2_3d_suche_v2.py (RUNDE-31, sha256 6beabc3f...), importiert, nicht kopiert:
  - Grundzustand f(r): Schiessen in s = -ln(f_top - f(0)) mit derselben Einteilung (Ueberschuss u > t, Unterschuss
    u <= t und u' < 0), demselben RK4-Schritt (rk4_u), derselben Startreihe (start_reihe), denselben Schnittregeln
    und demselben Schwanz (f_werte) wie profil(). Neu nur die Suche: skalare Bisektion in s statt 1024 Kandidaten je
    Runde (Laufzeit auf einem Kern); Gegenprobe gegen bic2.profil im Rauchlauf (Kommando profilvergleich).
  - Gitter und Koeffizienten aus lin_multi (Profil mit Schritt h/2, Aussenrand f(R) = f_rand f0, Anschluss r_m fest
    je Lauf), RK4-Schema, Startreihe der regulaeren Loesungen und abklingende Jost-Loesung z2 wie direkt_m,
    L(y) = Omega(y, z2) exp(-kappa R) wie dort.
Neu (stabilisiert, Godunov/Conte-Orthonormalisierung):
  - y_a (U ~ r) und y_b (V ~ r) werden alle n_orth RK4-Schritte und am Anschluss per Gram-Schmidt orthonormiert:
    q1 = y_b/|y_b|, q2 = (y_a - <q1, y_a> q1)/|...|. Damit y_b = T11 q1, y_a = T12 q1 + T22 q2, T11 > 0, T22 > 0.
  - L1 = L(q1) = L(y_b)/T11: dieselben Nullstellen in rho wie L(y_b) in RUNDE-31.
  - s = L(q2) an der Nullstelle von L1 = s_R31/T22: dasselbe Vorzeichen und dieselben Nullstellen in omega^2 wie s in
    RUNDE-31, ohne die Ausloeschung zwischen y_a und y_b (Kernwachstum).
  - W = L(q2) + i L(q1) entsteht aus W_R31 = L(y_a) + i L(y_b) durch die orientierungstreue Abbildung
    [[T22, T12], [0, T11]]: dieselben Nullstellen und Umlaufzahlen.
  - Alles reell (reelles rho, l = 0, nu = 1: Hankel-Faktor P = 1, Q = -kappa exakt).
Kommandos: zeilen (Abtastung in z = 1/eps), wurzel (Nullstellensuche in omega^2 und Umlauf-Rechteck), kette
(Fensterlogik nach PLAN.md), profilvergleich (Rauchlauf).
"""
import argparse
import datetime
import glob
import hashlib
import json
import math
import os
import sys
import time

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bic2_3d_suche_v2 as B  # noqa: E402

F64 = torch.float64
DEV = torch.device("cpu")
T0 = time.perf_counter()
BETA = 1.0
OM2MIN = 1.0 - 1.0 / (4.0 * BETA)
B_INF = 2.6186


def uhr():
    return time.perf_counter() - T0


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def sha(pfad):
    with open(pfad, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def jf(x):
    if isinstance(x, dict):
        return {str(k): jf(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jf(v) for v in x]
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return x


def speichern(pfad, obj):
    tmp = pfad + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(jf(obj), fh, indent=1)
    os.replace(tmp, pfad)


# ================================================================ Profil (skalar, gleiche Regeln wie bic2.profil)

def profil_skalar(w2, beta, hp, f_schwanz=1e-5, r_max=130.0, it_max=400):
    a0 = 1.0 - w2
    dm1 = 2.0
    t, c = B.koeffizienten(a0, beta)
    c1, c2, c3, c4, c5 = c
    n_max = int(round(r_max / hp))

    def G(u):
        return u * (c1 + u * (-c2 + u * (c3 + u * (-c4 + u * c5))))

    def Gs(u):
        return c1 + u * (-2.0 * c2 + u * (3.0 * c3 + u * (-4.0 * c4 + u * 5.0 * c5)))

    def start(s):
        d = dm1 + 1.0
        u0 = math.exp(-s)
        a = G(u0) / (2.0 * d)
        b = Gs(u0) * a / (4.0 * d + 8.0)
        return u0, u0 + a * hp * hp + b * hp ** 4, 2.0 * a * hp + 4.0 * b * hp ** 3

    def schritt(r, u, up):
        h = hp
        k1u, k1p = up, G(u) - (dm1 / r) * up
        rm = r + 0.5 * h
        u2, p2 = u + 0.5 * h * k1u, up + 0.5 * h * k1p
        k2u, k2p = p2, G(u2) - (dm1 / rm) * p2
        u3, p3 = u + 0.5 * h * k2u, up + 0.5 * h * k2p
        k3u, k3p = p3, G(u3) - (dm1 / rm) * p3
        re = r + h
        u4, p4 = u + h * k3u, up + h * k3p
        k4u, k4p = p4, G(u4) - (dm1 / re) * p4
        return (u + (h / 6.0) * (k1u + 2.0 * k2u + 2.0 * k3u + k4u),
                up + (h / 6.0) * (k1p + 2.0 * k2p + 2.0 * k3p + k4p))

    def schuss(s):
        """+1 Ueberschuss (u > t), -1 Unterschuss (u <= t, u' < 0); bis r_max unentschieden = +1 (s zu gross)."""
        _, u, up = start(s)
        for k in range(1, n_max):
            u, up = schritt(k * hp, u, up)
            if u > t:
                return 1
            if up < 0.0:
                return -1
        return 1

    lo, hi = -math.log(t - 1e-3), 150.0
    gueltig = schuss(lo) < 0
    n_it = 0
    while n_it < it_max:
        mid = 0.5 * (lo + hi)
        if not (lo < mid < hi):
            break
        if schuss(mid) > 0:
            hi = mid
        else:
            lo = mid
        n_it += 1
    s_mid = 0.5 * (lo + hi)
    st = [start(s) for s in (lo, s_mid, hi)]
    u0m = st[1][0]
    f0 = t - u0m
    f2 = -G(u0m) / (2.0 * (dm1 + 1.0))
    f_l = [t - u0m, t - st[1][1]]
    fp_l = [0.0, -st[1][2]]
    us = [v[1] for v in st]
    ups = [v[2] for v in st]
    j_cut, grund, streu = None, 0, 0.0
    k = 1
    while k < n_max:
        for i in range(3):
            us[i], ups[i] = schritt(k * hp, us[i], ups[i])
        k += 1
        fm, fpm = t - us[1], -ups[1]
        streu = abs((t - us[2]) - (t - us[0]))
        j = len(f_l)
        f_l.append(fm)
        fp_l.append(fpm)
        g = 0
        if fm < f_schwanz * f0:
            g = 1
        elif fpm > 0:
            g = 2
        elif fm < 0:
            g = 3
        elif streu > 1e-2 * abs(fm):
            g = 4
        if g:
            j_cut, grund = max(1, j - 1), g
            break
    if j_cut is None:
        j_cut = len(f_l) - 1
    return {"w2": w2, "dim": 3.0, "beta": beta, "h": hp, "t": t, "f0": f0, "f2": f2, "s": s_mid, "klammer": hi - lo,
            "rueckfall": not gueltig, "j_cut": j_cut, "r_cut": j_cut * hp, "grund": grund, "streuung_cut": streu,
            "f": f_l[:j_cut + 1], "fp": fp_l[:j_cut + 1], "kappa": math.sqrt(a0), "dm1": dm1,
            "pot": {"art": "poly", "beta": beta}, "schuesse": n_it}


# ================================================================ stabilisierte Anschlussgroessen

def _stab_W(L, rhos, n_orth):
    h, K, Km = L["h"], L["K"], L["Km"]
    dv = L["dvX"][0].tolist()
    sv = L["svX"][0].tolist()
    om = float(L["omX"][0])
    d0, d2, s0, s2 = [float(v) for v in L["reiheX"][0].tolist()]
    n = len(rhos)
    rho = torch.tensor([float(v) for v in rhos], dtype=F64)
    wp2 = (om + rho) ** 2
    wm2 = (om - rho) ** 2
    # regulaere Startwerte bei r = h (Reihe wie direkt_m, nu = 1, Faktor h^nu = h)
    r = h
    A = d0 - wp2
    Bq = d0 - wm2
    n2, n4 = 6.0, 20.0
    a2 = A / n2
    b2 = s0 / n2
    a4 = (A * a2 + s0 * b2 + d2) / n4
    b4 = (s0 * a2 + Bq * b2 + s2) / n4
    c2 = s0 / n2
    e2 = Bq / n2
    c4 = (A * c2 + s0 * e2 + s2) / n4
    e4 = (s0 * c2 + Bq * e2 + d2) / n4
    r2, r3, r4 = r * r, r ** 3, r ** 4
    pUa = 1.0 + a2 * r2 + a4 * r4
    pVa = b2 * r2 + b4 * r4
    dUa = 2.0 * a2 * r + 4.0 * a4 * r3
    dVa = 2.0 * b2 * r + 4.0 * b4 * r3
    pUb = c2 * r2 + c4 * r4
    pVb = 1.0 + e2 * r2 + e4 * r4
    dUb = 2.0 * c2 * r + 4.0 * c4 * r3
    dVb = 2.0 * e2 * r + 4.0 * e4 * r3
    ya = torch.stack([r * pUa, r * pVa, r * (pUa / r + dUa), r * (pVa / r + dVa)])
    yb = torch.stack([r * pUb, r * pVb, r * (pUb / r + dUb), r * (pVb / r + dVb)])
    start_b = yb.norm(dim=0)
    y = torch.cat([ya, yb], dim=1)
    wp2c = torch.cat([wp2, wp2])
    wm2c = torch.cat([wm2, wm2])

    def ab(v, j, wp, wm):
        d, s = dv[j], sv[j]
        return torch.stack([v[2], v[3], (d - wp) * v[0] + s * v[1], s * v[0] + (d - wm) * v[1]])

    def schritt(v, j0, sg, hs, wp, wm):
        j1, j2 = j0 + sg, j0 + 2 * sg
        k1 = ab(v, j0, wp, wm)
        k2 = ab(v + (0.5 * hs) * k1, j1, wp, wm)
        k3 = ab(v + (0.5 * hs) * k2, j1, wp, wm)
        k4 = ab(v + hs * k3, j2, wp, wm)
        return v + (hs / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

    def orth(v):
        va, vb = v[:, :n], v[:, n:]
        n1 = vb.norm(dim=0)
        q1 = vb / n1
        w = va - (q1 * va).sum(0) * q1
        w = w - (q1 * w).sum(0) * q1          # zweiter Durchgang (Gram-Schmidt zweimal)
        n2_ = w.norm(dim=0)
        return torch.cat([w / n2_, q1], dim=1), n1, n2_

    log1 = torch.zeros(n, dtype=F64)
    log2 = torch.zeros(n, dtype=F64)
    for k in range(1, Km):
        y = schritt(y, 2 * k, 1, h, wp2c, wm2c)
        if n_orth > 0 and k % n_orth == 0:
            y, n1, n2_ = orth(y)
            log1 = log1 + torch.log(n1)
            log2 = log2 + torch.log(n2_)
    y, n1, n2_ = orth(y)
    log1 = log1 + torch.log(n1)
    log2 = log2 + torch.log(n2_)
    # abklingende Jost-Loesung z2 = (0, 1, 0, -kappa) bei R (Faktor exp(-kappa R) weggelassen), nach innen bis r_m
    R = L["R_aus"]
    kap = torch.sqrt(1.0 - wm2)
    null = torch.zeros(n, dtype=F64)
    z = torch.stack([null, torch.ones(n, dtype=F64), null, -kap])
    for k in range(K, Km, -1):
        z = schritt(z, 2 * k, -1, -h, wp2, wm2)
    nz = torch.exp(-kap * R)
    q2, q1 = y[:, :n], y[:, n:]

    def Om(p, q):
        return p[0] * q[2] - p[2] * q[0] + p[1] * q[3] - p[3] * q[1]
    L2 = Om(q2, z) * nz
    L1 = Om(q1, z) * nz
    t2 = torch.stack([(q2[0] * z[2]).abs(), (q2[2] * z[0]).abs(), (q2[1] * z[3]).abs(),
                      (q2[3] * z[1]).abs()]).amax(0) * nz
    wach = (log1 - torch.log(start_b)) / math.log(10.0)
    return L2.tolist(), L1.tolist(), t2.tolist(), wach.tolist()


def stab_W(L, rhos, n_orth, stapel=2500):
    a, b, c, d = [], [], [], []
    for i0 in range(0, len(rhos), stapel):
        r_ = _stab_W(L, rhos[i0:i0 + stapel], n_orth)
        a += r_[0]
        b += r_[1]
        c += r_[2]
        d += r_[3]
    return a, b, c, d


# ================================================================ eine Zeile omega^2 = x

def rho_ref_von(x, a):
    return a.rho0 + a.rho_steig * ((x - OM2MIN) - a.eps0)


def nullstellen(L, rs, L2, L1, n_orth, n_zoom, runden):
    """alle Vorzeichenwechsel von L1 auf dem Gitter rs, je Klammer `runden` Zoomrunden (n_zoom Punkte, ein Stapel je
    Runde fuer alle Klammern), dann lineare Interpolation von L1 und L2 auf der Endklammer."""
    kl = []
    for k in range(len(rs) - 1):
        if L1[k] == 0.0:
            kl.append([rs[k], rs[k], L1[k], L1[k], L2[k], L2[k]])
        elif L1[k] * L1[k + 1] < 0:
            kl.append([rs[k], rs[k + 1], L1[k], L1[k + 1], L2[k], L2[k + 1]])
    t2_end = [0.0] * len(kl)
    wa_end = [0.0] * len(kl)
    for _ in range(runden):
        pts, wer = [], []
        for q, k_ in enumerate(kl):
            if k_[1] - k_[0] <= 0.0:
                continue
            for m in range(1, n_zoom - 1):
                pts.append(k_[0] + (k_[1] - k_[0]) * m / (n_zoom - 1))
                wer.append(q)
        if not pts:
            break
        Z2, Z1, Zt, Zw = stab_W(L, pts, n_orth)
        for q in range(len(kl)):
            idx = [i for i in range(len(pts)) if wer[i] == q]
            if not idx:
                continue
            ka, kb, fa, fb, ga, gb = kl[q]
            folge = [(ka, fa, ga, None, None)] + [(pts[i], Z1[i], Z2[i], Zt[i], Zw[i]) for i in idx] + \
                [(kb, fb, gb, None, None)]
            for (r1, f1, g1, t1, w1), (r2, f2, g2, t2_, w2_) in zip(folge, folge[1:]):
                if f1 == 0.0:
                    kl[q] = [r1, r1, f1, f1, g1, g1]
                    break
                if f1 * f2 < 0:
                    kl[q] = [r1, r2, f1, f2, g1, g2]
                    t2_end[q] = max(v for v in (t1, t2_, t2_end[q]) if v is not None)
                    wa_end[q] = max(v for v in (w1, w2_, wa_end[q]) if v is not None)
                    break
    aus = []
    for q, (ka, kb, fa, fb, ga, gb) in enumerate(kl):
        if kb == ka:
            tt, rho, s = 0.0, ka, ga
            dl1 = dl2 = None
        else:
            tt = fa / (fa - fb)
            rho = ka + tt * (kb - ka)
            s = ga + tt * (gb - ga)
            dl1 = (fb - fa) / (kb - ka)
            dl2 = (gb - ga) / (kb - ka)
        aus.append({"rho": rho, "s": s, "richtung": 1 if fb > fa else -1, "klammer_rho": kb - ka,
                    "dL1_drho": dl1, "dL2_drho": dl2, "terme2": t2_end[q], "wachstum_log10": wa_end[q]})
    return aus


def zeile(x, p, R_fest, rm_fest, rho_ref, h, f_rand, n_orth, n_rho, n_dicht, dicht_halb, n_zoom, runden,
          vergleich=None, r31=False):
    t0 = uhr()
    L = B.lin_multi([p], h, f_rand, DEV, r_min=R_fest, rm_fest=rm_fest)
    om = math.sqrt(x)
    r0, r1 = 1.0 - om + 0.002, 1.0 + om - 0.002
    g = [r0 + (r1 - r0) * k / (n_rho - 1) for k in range(n_rho)] if n_rho > 1 else []
    d = [rho_ref + dicht_halb * (2.0 * k / (n_dicht - 1) - 1.0) for k in range(n_dicht)]
    rs = sorted(set(g + [v for v in d if r0 < v < r1]))
    L2, L1, T2, WA = stab_W(L, rs, n_orth)
    nst = nullstellen(L, rs, L2, L1, n_orth, n_zoom, runden)
    kand = [z for z in nst if abs(z["rho"] - rho_ref) <= dicht_halb]
    ziel = min(kand, key=lambda z: abs(z["rho"] - rho_ref)) if kand else None
    eps = x - OM2MIN
    rec = {"x": x, "eps": eps, "z": 1.0 / eps, "rho_ref": rho_ref, "R_aus": L["R_aus"], "r_m": L["r_m"],
           "R_rand_einzel": B.radius_wo(p, f_rand * p["f0"]), "R_wand": B.r_wand(p, BETA), "R_halb_S0": B.r_halb(p),
           "S0": p["f0"] ** 2, "profil_s": p["s"], "profil_klammer": p["klammer"], "profil_rueckfall": p["rueckfall"],
           "j_cut": p["j_cut"], "grund": p["grund"], "n_rho": len(rs), "rho_fenster": [r0, r1],
           "n_L1_nullstellen": len(nst), "nullstellen": nst, "ziel": ziel,
           "s": ziel["s"] if ziel else None, "rho": ziel["rho"] if ziel else None,
           "richtung": ziel["richtung"] if ziel else None, "wachstum_log10_max_fenster": max(WA) if WA else None}
    if ziel is not None and (vergleich or r31):
        dr = 1e-8
        pr = [ziel["rho"] - dr, ziel["rho"] + dr]
        v = {}
        for no in (vergleich or []):
            a2, a1, _, _ = stab_W(L, pr, no)
            if a1[0] * a1[1] < 0:
                tt = a1[0] / (a1[0] - a1[1])
                v[f"n_orth_{no}"] = {"s": a2[0] + tt * (a2[1] - a2[0]), "rho": pr[0] + tt * (pr[1] - pr[0])}
            else:
                v[f"n_orth_{no}"] = {"s": None, "L1": a1, "L2": a2}
        if r31:
            W, wa, te = B.praez_W(L, pr, [0, 0], 1.0)
            la = [w.real for w in W]
            lb = [w.imag for w in W]
            if lb[0] * lb[1] < 0:
                tt = lb[0] / (lb[0] - lb[1])
                v["r31_direkt"] = {"s": la[0] + tt * (la[1] - la[0]), "rho": pr[0] + tt * (pr[1] - pr[0]),
                                   "wachstum": max(wa), "terme_a": max(te)}
            else:
                v["r31_direkt"] = {"s": None, "La": la, "Lb": lb, "wachstum": max(wa)}
        rec["vergleich"] = v
    rec["sek"] = uhr() - t0
    return rec, L


def profil_zeit(x, hp):
    t0 = uhr()
    p = profil_skalar(x, BETA, hp)
    return p, uhr() - t0


# ================================================================ Kommando zeilen

def cmd_zeilen(a):
    h = a.h
    f_rand = B.FRAND.get(h, 1e-8)
    if a.z_liste:
        zs = [float(v) for v in a.z_liste.split(",")]
    else:
        zs = [a.z0 + a.dz * j for j in range(a.j_von, a.j_bis + 1)]
    xs = [OM2MIN + 1.0 / z for z in zs]
    vergleich = [int(v) for v in a.vergleich.split(",")] if a.vergleich else None
    out = {"kommando": "zeilen", "start": jetzt(), "argumente": vars(a), "code_sha256": sha(__file__),
           "bic2_sha256": sha(B.__file__), "beta": BETA, "h": h, "f_rand": f_rand, "zeilen": [], "abbruch": None}
    pfad = os.path.join(a.out, "zeilen.json")
    os.makedirs(a.out, exist_ok=True)
    profs = []
    for x in xs:
        if uhr() > a.budget:
            out["abbruch"] = f"Zeit bei den Profilen ({uhr():.0f} s)"
            break
        p, tp = profil_zeit(x, 0.5 * h)
        p["sek"] = tp
        profs.append(p)
        print(f"Profil x = {x:.10f}: {tp:.1f} s, Schuesse {p['schuesse']}, r_cut {p['r_cut']:.2f}, nach {uhr():.0f} s",
              flush=True)
    if not profs:
        speichern(pfad, out)
        return
    R_fest = max(B.radius_wo(p, f_rand * p["f0"]) for p in profs) + a.r_zusatz
    rm_fest = sorted(B.r_halb(p) for p in profs)[len(profs) // 2]
    out.update({"R_fest": R_fest, "rm_fest": rm_fest})
    for x, z, p in zip(xs, zs, profs):
        if uhr() > a.budget:
            out["abbruch"] = f"Zeit bei den Zeilen ({uhr():.0f} s)"
            break
        rec, _ = zeile(x, p, R_fest, rm_fest, rho_ref_von(x, a), h, f_rand, a.n_orth, a.n_rho, a.n_dicht,
                       a.dicht_halb, a.n_zoom, a.zoom_runden, vergleich, a.r31 == "ja")
        rec["z_soll"] = z
        rec["sek_profil"] = p["sek"]
        rec["profil_schuesse"] = p["schuesse"]
        out["zeilen"].append(rec)
        speichern(pfad, out)
        print(f"Zeile z {z:.5f}: {rec['n_L1_nullstellen']} Nullstellen L1, Zielast "
              f"{'-' if rec['ziel'] is None else 'ja'}, R_aus {rec['R_aus']:.2f}, r_m {rec['r_m']:.2f}, "
              f"{rec['sek']:.1f} s, nach {uhr():.0f} s", flush=True)
    out["ende"] = jetzt()
    out["sek"] = uhr()
    speichern(pfad, out)


# ================================================================ Kommando wurzel

def lade_zeilen(muster):
    """alle Zeilen aus zeilen.json-Dateien (Muster), nach z sortiert; Duplikate (gleiches z auf 1e-9) bleiben als
    Liste je z erhalten."""
    dateien = sorted(set(sum([glob.glob(m) for m in muster.split(",")], [])))
    rows = []
    for f in dateien:
        with open(f) as fh:
            d = json.load(fh)
        for r in d["zeilen"]:
            r["_datei"] = f
            rows.append(r)
    rows.sort(key=lambda r: r["z_soll"])
    gruppen = []
    for r in rows:
        if gruppen and abs(gruppen[-1][0]["z_soll"] - r["z_soll"]) < 1e-9:
            gruppen[-1].append(r)
        else:
            gruppen.append([r])
    return dateien, gruppen


def wechsel_aus_gruppen(gruppen):
    """Vorzeichenwechsel von s zwischen benachbarten z (erste Zeile je z massgeblich, Duplikate nur Pruefung)."""
    w = []
    for i in range(len(gruppen) - 1):
        A, Bz = gruppen[i][0], gruppen[i + 1][0]
        if A["s"] is None or Bz["s"] is None:
            continue
        if A["s"] * Bz["s"] < 0:
            w.append({"i": i, "z": [A["z_soll"], Bz["z_soll"]], "x": [A["x"], Bz["x"]], "rho": [A["rho"], Bz["rho"]],
                      "s": [A["s"], Bz["s"]]})
    return w


def rechteck(La, Lb, xa, xb, ra, rb, rc, drho, ns, runden, n_orth):
    """Umlauf von W = L(q2) + i L(q1) auf [xa, xb] x [rc - drho, rc + drho], gegen den Uhrzeigersinn in der Ebene
    (omega^2, rho) wie praez_rechteck: unten rho = r_lo (xa -> xb), rechts x = xb (rho steigt), oben rho = r_hi
    (xb -> xa), links x = xa (rho faellt). Je rho-Seite ns gleichabstaendige Punkte plus geometrische Haeufung um die
    Nullstelle von L1 der Zeile (ra, rb), dann Halbierung jedes Abschnitts mit Phasensprung > 0,3 rad (hoechstens
    `runden` Runden). Kreuzungszaehlung wie praez_rechteck."""
    t0 = uhr()
    r_lo, r_hi = rc - drho, rc + drho

    def seite(r0_):
        pts = [r_lo + (r_hi - r_lo) * k / ns for k in range(ns + 1)]
        if r0_ is not None and r_lo < r0_ < r_hi:
            for m in range(-14, 3):
                for sg in (-1.0, 1.0):
                    v = r0_ + sg * 10.0 ** m
                    if r_lo < v < r_hi:
                        pts.append(v)
        return sorted(set(pts))
    sa, sb = seite(ra), seite(rb)
    Wa = list(zip(*stab_W(La, sa, n_orth)[:2]))
    Wb = list(zip(*stab_W(Lb, sb, n_orth)[:2]))
    benutzt = 0
    for rnd in range(runden):
        neu_a = [k for k in range(len(sa) - 1) if abs(math.atan2(*_dphase(Wa[k], Wa[k + 1]))) > 0.3]
        neu_b = [k for k in range(len(sb) - 1) if abs(math.atan2(*_dphase(Wb[k], Wb[k + 1]))) > 0.3]
        if not neu_a and not neu_b:
            break
        benutzt = rnd + 1
        if neu_a:
            m_ = [0.5 * (sa[k] + sa[k + 1]) for k in neu_a]
            Wm = list(zip(*stab_W(La, m_, n_orth)[:2]))
            sa, Wa = _einfuegen(sa, Wa, neu_a, m_, Wm)
        if neu_b:
            m_ = [0.5 * (sb[k] + sb[k + 1]) for k in neu_b]
            Wm = list(zip(*stab_W(Lb, m_, n_orth)[:2]))
            sb, Wb = _einfuegen(sb, Wb, neu_b, m_, Wm)
    # Pfad: rechts (x = xb, rho steigt), oben (Sprung xb -> xa bei r_hi), links (x = xa, rho faellt), unten (Sprung)
    pfad = [(r, "b") for r in sb] + [(r, "a") for r in reversed(sa)]
    W = [Wb[k] for k in range(len(sb))] + [Wa[k] for k in reversed(range(len(sa)))]
    spr, summe = [], 0.0
    for k in range(len(W)):
        w1, w2 = W[k], W[(k + 1) % len(W)]
        dp = math.atan2(*_dphase(w1, w2))
        summe += dp
        spr.append(abs(dp))
    kr = 0.0
    for k in range(len(W)):
        (re1, im1), (re2, im2) = W[k], W[(k + 1) % len(W)]
        if im1 * im2 < 0:
            tt = im1 / (im1 - im2)
            la = re1 + tt * (re2 - re1)
            kr += 0.5 * (1.0 if la > 0 else -1.0) * (1.0 if im2 > im1 else -1.0)
    seiten = {"rechts": max(spr[:len(sb) - 1]) if len(sb) > 1 else None, "oben": spr[len(sb) - 1],
              "links": max(spr[len(sb):len(W) - 1]) if len(sa) > 1 else None, "unten": spr[-1]}
    return {"x_lo": xa, "x_hi": xb, "rho_lo": r_lo, "rho_hi": r_hi, "rho_c": rc, "drho": drho,
            "umlauf_phase": summe / (2.0 * math.pi), "umlauf_kreuzung": kr, "max_sprung": max(spr),
            "aufgeloest": max(spr) < 0.4, "max_sprung_seiten": seiten, "punkte": len(W), "runden_benutzt": benutzt,
            "runden_max": runden, "sek": uhr() - t0}


def _dphase(w1, w2):
    """(sin, cos)-Paar des Phasenschritts von w1 nach w2 (w = (Re, Im)), fuer atan2(y, x)."""
    re1, im1 = w1
    re2, im2 = w2
    # w2 * conj(w1)
    return (im2 * re1 - re2 * im1, re2 * re1 + im2 * im1)


def _einfuegen(pts, W, idx, neu_p, neu_W):
    p2, w2 = [], []
    j = 0
    for k in range(len(pts)):
        p2.append(pts[k])
        w2.append(W[k])
        if j < len(idx) and idx[j] == k:
            p2.append(neu_p[j])
            w2.append(neu_W[j])
            j += 1
    return p2, w2


def wurzel_eine(a, kl, h, f_rand, budget_rest):
    """Illinois in omega^2 auf der Klammer kl = {"x": [xa, xb], "rho": [ra, rb]}; neues Profil je Schritt; festes R
    und r_m aus den zwei Startzeilen; danach Rechteck auf den Startzeilen."""
    w = {"klammer_start": kl["x"], "rho_start_ref": kl["rho"], "z_start": [1.0 / (v - OM2MIN) for v in kl["x"]],
         "quelle": kl.get("quelle"), "verlauf": [], "fehler": None}
    t_anf = uhr()
    pa, ta = profil_zeit(kl["x"][0], 0.5 * h)
    pb, tb = profil_zeit(kl["x"][1], 0.5 * h)
    R_fest = max(B.radius_wo(p, f_rand * p["f0"]) for p in (pa, pb)) + a.r_zusatz
    rm_fest = sorted(B.r_halb(p) for p in (pa, pb))[1]
    w.update({"R_fest": R_fest, "rm_fest": rm_fest})
    A, La = zeile(kl["x"][0], pa, R_fest, rm_fest, kl["rho"][0], h, f_rand, a.n_orth, a.n_rho, a.n_dicht,
                  a.dicht_halb, a.n_zoom, a.zoom_runden)
    Bz, Lb = zeile(kl["x"][1], pb, R_fest, rm_fest, kl["rho"][1], h, f_rand, a.n_orth, a.n_rho, a.n_dicht,
                   a.dicht_halb, a.n_zoom, a.zoom_runden)
    w["zeilen_start"] = [A, Bz]
    if A["ziel"] is None or Bz["ziel"] is None:
        w["fehler"] = "kein Zielast an einer Startzeile"
        return w
    w["wechsel_bestaetigt"] = A["s"] * Bz["s"] < 0
    w["ast_konsistent"] = A["richtung"] == Bz["richtung"] and abs(A["rho"] - Bz["rho"]) <= a.ast_tol
    if not w["wechsel_bestaetigt"]:
        w["fehler"] = "kein Vorzeichenwechsel von s zwischen den Startzeilen"
        return w
    t_schritt = (uhr() - t_anf) / 2.0
    ra, rb = A, Bz
    fa, fb = A["s"], Bz["s"]
    for it in range(a.iter_x):
        if abs(rb["x"] - ra["x"]) <= a.tol_x:
            break
        if uhr() + t_schritt + a.reserve > budget_rest:
            w["fehler"] = "Zeit"
            break
        xa_, xb_ = ra["x"], rb["x"]
        xn = xb_ - fb * (xb_ - xa_) / (fb - fa) if fb != fa else 0.5 * (xa_ + xb_)
        if not (min(xa_, xb_) < xn < max(xa_, xb_)):
            xn = 0.5 * (xa_ + xb_)
        tt = (xn - xa_) / (xb_ - xa_)
        rr = ra["rho"] + tt * (rb["rho"] - ra["rho"])
        t0 = uhr()
        p, tp = profil_zeit(xn, 0.5 * h)
        rec, _ = zeile(xn, p, R_fest, rm_fest, rr, h, f_rand, a.n_orth, a.n_rho_schritt, a.n_dicht_schritt,
                       a.dicht_halb_schritt, a.n_zoom, a.zoom_runden)
        t_schritt = max(t_schritt, uhr() - t0)
        kurz = {k: rec[k] for k in ("x", "eps", "z", "rho_ref", "rho", "s", "richtung", "R_wand", "R_halb_S0",
                                    "n_L1_nullstellen", "sek")}
        if rec["ziel"] is not None:
            kurz["terme2"] = rec["ziel"]["terme2"]
            kurz["wachstum_log10"] = rec["ziel"]["wachstum_log10"]
        w["verlauf"].append(kurz)
        if rec["ziel"] is None:
            w["fehler"] = "kein Zielast im Schritt"
            break
        fx = rec["s"]
        if fx == 0.0:
            ra, rb, fa, fb = rec, rec, 0.0, 0.0
            break
        if fx * fb < 0:
            ra, fa = rb, fb
        else:
            fa = 0.5 * fa
        rb, fb = rec, fx
    sa_, sb_ = ra["s"], rb["s"]
    xa_, xb_ = ra["x"], rb["x"]
    tt = 0.0 if sb_ == sa_ else (0.0 - sa_) / (sb_ - sa_)
    xs_ = xa_ + tt * (xb_ - xa_)

    def li(k):
        va, vb = ra.get(k), rb.get(k)
        return None if va is None or vb is None else va + tt * (vb - va)
    st_start = (Bz["s"] - A["s"]) / (Bz["x"] - A["x"])
    terme = [r_["ziel"]["terme2"] if r_.get("ziel") else r_.get("terme2") for r_ in (ra, rb)]
    terme = [v for v in terme if v is not None]
    rausch = 1e-15 * max(terme) / abs(st_start) if terme and st_start else None
    w.update({"x_stern": xs_, "eps_stern": xs_ - OM2MIN, "z_stern": 1.0 / (xs_ - OM2MIN), "rho_stern": li("rho"),
              "R_wand_stern": li("R_wand"), "R_halb_S0_stern": li("R_halb_S0"), "klammer_end": [xa_, xb_],
              "s_end": [sa_, sb_], "breite_end": abs(xb_ - xa_), "konvergiert": abs(xb_ - xa_) <= a.tol_x,
              "schritte": len(w["verlauf"]), "steigung_s_x_start": st_start, "rauschmass_x": rausch,
              "terme2_max": max(terme) if terme else None,
              "wachstum_log10_kandidat": max(r_["ziel"]["wachstum_log10"] if r_.get("ziel") else
                                             r_.get("wachstum_log10", float("-inf")) for r_ in (ra, rb))})
    if a.rechteck == "ja":
        if uhr() + a.reserve > budget_rest:
            w["rechteck"] = {"fehler": "Zeit"}
        else:
            sl = (Bz["rho"] - A["rho"]) / (Bz["x"] - A["x"])
            halb_x = max(abs(Bz["x"] - xs_), abs(xs_ - A["x"]))
            drho = min(a.pr_drho_max, max(a.pr_drho, 2.0 * abs(sl) * halb_x))
            if A["x"] < Bz["x"]:          # x_lo < x_hi wie praez_rechteck (Umlaufsinn gegen den Uhrzeigersinn)
                e = rechteck(La, Lb, A["x"], Bz["x"], A["rho"], Bz["rho"], w["rho_stern"], drho, a.u_n, a.u_runden,
                             a.n_orth)
            else:
                e = rechteck(Lb, La, Bz["x"], A["x"], Bz["rho"], A["rho"], w["rho_stern"], drho, a.u_n, a.u_runden,
                             a.n_orth)
            e["steigung_ast"] = sl
            w["rechteck"] = e
    w["sek"] = uhr() - t_anf
    return w


def cmd_wurzel(a):
    h = a.h
    f_rand = B.FRAND.get(h, 1e-8)
    os.makedirs(a.out, exist_ok=True)
    pfad = os.path.join(a.out, "wurzel.json")
    out = {"kommando": "wurzel", "start": jetzt(), "argumente": vars(a), "code_sha256": sha(__file__),
           "bic2_sha256": sha(B.__file__), "beta": BETA, "h": h, "f_rand": f_rand, "wurzeln": []}
    if a.fortsetzen and os.path.exists(pfad):
        with open(pfad) as fh:
            alt = json.load(fh)
        out["wurzeln"] = [w for w in alt.get("wurzeln", []) if w.get("fehler") != "Zeit" and "x_stern" in w
                          or (w.get("fehler") and w.get("fehler") != "Zeit")]
        out["fortgesetzt_von"] = alt.get("start")
    klammern = []
    if a.klammer_x:
        x0, x1 = [float(v) for v in a.klammer_x.split(",")]
        klammern.append({"x": [x0, x1], "rho": [rho_ref_von(x0, a), rho_ref_von(x1, a)], "quelle": "klammer_x"})
    elif a.aus_zeilen:
        dateien, gruppen = lade_zeilen(a.aus_zeilen)
        out["zeilen_dateien"] = {f: sha(f) for f in dateien}
        for i, wv in enumerate(wechsel_aus_gruppen(gruppen)):
            if i % a.teile == a.teil:
                klammern.append({"x": wv["x"], "rho": wv["rho"], "quelle": {"wechsel": i, "z": wv["z"]}})
    elif a.aus_wurzeln:
        dateien = sorted(set(sum([glob.glob(m) for m in a.aus_wurzeln.split(",")], [])))
        out["wurzel_dateien"] = {f: sha(f) for f in dateien}
        alle = []
        for f in dateien:
            with open(f) as fh:
                for w in json.load(fh)["wurzeln"]:
                    if w.get("x_stern") is not None and w.get("konvergiert"):
                        alle.append(w)
        alle.sort(key=lambda w: w["x_stern"], reverse=True)          # nach z aufsteigend
        if a.nur_letzte > 0:
            alle = alle[-a.nur_letzte:]
        for i, w in enumerate(alle):
            if i % a.teile != a.teil:
                continue
            xs_, rs_ = w["x_stern"], w["rho_stern"]
            sl = w.get("rechteck", {}).get("steigung_ast")
            if sl is None:
                zs = w["zeilen_start"]
                sl = (zs[1]["rho"] - zs[0]["rho"]) / (zs[1]["x"] - zs[0]["x"])
            klammern.append({"x": [xs_ - a.klammer_halb, xs_ + a.klammer_halb],
                             "rho": [rs_ - sl * a.klammer_halb, rs_ + sl * a.klammer_halb],
                             "quelle": {"x_stern_h004": xs_, "z_stern_h004": w["z_stern"]}})
    erledigt = {round(w["klammer_start"][0], 12) for w in out["wurzeln"]}
    out["n_klammern"] = len(klammern)
    speichern(pfad, out)
    for kl in klammern:
        if round(kl["x"][0], 12) in erledigt:
            continue
        if uhr() + a.reserve + 30.0 > a.budget:
            out["abbruch"] = f"Zeit vor Klammer {kl['quelle']} ({uhr():.0f} s)"
            break
        w = wurzel_eine(a, kl, h, f_rand, a.budget)
        out["wurzeln"].append(w)
        speichern(pfad, out)
        print(f"Wurzel aus {kl['quelle']}: konvergiert {w.get('konvergiert')}, Schritte {w.get('schritte')}, "
              f"Fehler {w.get('fehler')}, Rechteck Kreuzung "
              f"{w.get('rechteck', {}).get('umlauf_kreuzung')}, Phase {w.get('rechteck', {}).get('umlauf_phase')}, "
              f"nach {uhr():.0f} s", flush=True)
    out["ende"] = jetzt()
    out["sek"] = uhr()
    speichern(pfad, out)


# ================================================================ Kommando profilvergleich (Rauchlauf)

def cmd_profilvergleich(a):
    zs = [float(v) for v in a.z_liste.split(",")]
    out = {"kommando": "profilvergleich", "start": jetzt(), "vergleiche": []}
    os.makedirs(a.out, exist_ok=True)
    for z in zs:
        x = OM2MIN + 1.0 / z
        t0 = uhr()
        ps = profil_skalar(x, BETA, 0.5 * a.h)
        t1 = uhr()
        pv = B.profil(x, 3.0, BETA, 0.5 * a.h, DEV)
        t2 = uhr()
        n = min(len(ps["f"]), len(pv["f"]))
        df = max(abs(ps["f"][j] - pv["f"][j]) for j in range(n))
        n2 = int(B.radius_wo(pv, 1e-8 * pv["f0"]) / ps["h"]) + 10
        fs, _ = B.f_werte(ps, n2)
        fv, _ = B.f_werte(pv, n2)
        dfa = max(abs(u - v) for u, v in zip(fs, fv))
        out["vergleiche"].append({"z": z, "x": x, "sek_skalar": t1 - t0, "sek_bic2": t2 - t1,
                                  "s_skalar": ps["s"], "s_bic2": pv["s"], "klammer_skalar": ps["klammer"],
                                  "klammer_bic2": pv["klammer"], "j_cut": [ps["j_cut"], pv["j_cut"]],
                                  "grund": [ps["grund"], pv["grund"]], "f0": [ps["f0"], pv["f0"]],
                                  "max_df_bis_cut": df, "max_df_mit_schwanz": dfa,
                                  "r_halb": [B.r_halb(ps), B.r_halb(pv)], "R_wand": [B.r_wand(ps, BETA),
                                                                                     B.r_wand(pv, BETA)]})
        speichern(os.path.join(a.out, "profilvergleich.json"), out)
        print(json.dumps(jf(out["vergleiche"][-1])), flush=True)
    out["ende"] = jetzt()
    speichern(os.path.join(a.out, "profilvergleich.json"), out)


# ================================================================ Kommando kette (Fensterlogik, PLAN.md)

def cmd_kette(a):
    """Fenster k = -3 .. -25 der Reihe nach: [z_prev + b/2, z_prev + 3b/2], b = B_INF; Kriterien nach PLAN.md."""
    dateien, gruppen = lade_zeilen(a.aus_zeilen)
    w004 = _lade_wurzeln(a.aus_wurzeln)
    w002 = _lade_wurzeln(a.aus_h002)
    wrand = _lade_wurzeln(a.aus_rand) if a.aus_rand else []
    z_alle = [g[0]["z_soll"] for g in gruppen]
    dz = a.dz
    # Duplikat-Pruefung (doppelt gerechnete Randzeilen)
    dup = []
    for g in gruppen:
        if len(g) > 1:
            ss = [r["s"] for r in g]
            dup.append({"z": g[0]["z_soll"], "s_gleiches_vorzeichen": all(v is not None and v * ss[0] > 0 for v in ss),
                        "rel_abw_s": (max(ss) - min(ss)) / max(abs(v) for v in ss) if all(v is not None for v in ss)
                        else None})
    widerspruch_z = [d_["z"] for d_ in dup if not d_["s_gleiches_vorzeichen"]]
    wechsel = wechsel_aus_gruppen(gruppen)
    for wv in wechsel:
        wv["w004"] = _passend(w004, wv["x"])
    z_prev, u_prev = a.z_start, a.umlauf_start
    k_liste = list(range(-3, -26, -1))
    erg, offen_ab = [], None
    for k in k_liste:
        e = {"k": k, "status": None}
        if offen_ab is not None:
            e["status"] = "UNRESOLVED"
            e["grund"] = f"Vorgaenger k = {offen_ab} nicht eindeutig"
            erg.append(e)
            continue
        lo, hi = z_prev + 0.5 * B_INF, z_prev + 1.5 * B_INF
        e["fenster_z"] = [lo, hi]
        krit = {}
        gr = []
        if not z_alle or hi + dz > z_alle[-1] + 1e-9 or lo - dz < z_alle[0] - 1e-9:
            krit["abtastung_deckt_fenster"] = False
        else:
            krit["abtastung_deckt_fenster"] = True
        im = [g for g in gruppen if lo - dz - 1e-9 <= g[0]["z_soll"] <= hi + dz + 1e-9]
        krit["n_zeilen_erweitert"] = len(im)
        luecke = max([im[i + 1][0]["z_soll"] - im[i][0]["z_soll"] for i in range(len(im) - 1)] or [float("inf")])
        krit["groesste_luecke_z"] = luecke
        krit["abtastung_fein"] = luecke <= dz * 1.0001
        krit["ein_L1_ast_je_zeile"] = all(r["n_L1_nullstellen"] == 1 for g in im for r in g)
        krit["n_L1_nullstellen_max"] = max([r["n_L1_nullstellen"] for g in im for r in g] or [0])
        krit["zielast_alle_zeilen"] = all(r["ziel"] is not None for g in im for r in g)
        ri = [g[0]["richtung"] for g in im]
        rh = [g[0]["rho"] for g in im]
        krit["ast_richtung_gleich"] = len(set(ri)) == 1
        krit["ast_drho_max"] = max([abs(rh[i + 1] - rh[i]) for i in range(len(rh) - 1)] or [0.0])
        krit["ast_stetig"] = krit["ast_drho_max"] <= a.ast_tol
        krit["randzeilen_widerspruchsfrei"] = not any(lo - dz <= zw <= hi + dz for zw in widerspruch_z)
        # Rauschreserve des Vorzeichens: |s| > 1e-12 * groesster Einzelterm (1000-fach ueber der Rundung 1e-15)
        unsicher = [g[0]["z_soll"] for g in im if g[0]["s"] is not None and g[0]["ziel"] is not None
                    and abs(g[0]["s"]) <= 1e-12 * g[0]["ziel"]["terme2"]]
        krit["vorzeichen_unsicher_z"] = unsicher
        krit["vorzeichen_sicher"] = not unsicher
        ws = [wv for wv in wechsel if lo - dz - 1e-9 <= wv["z"][0] and wv["z"][1] <= hi + dz + 1e-9]
        krit["n_wechsel_erweitert"] = len(ws)
        fehlende = [wv for wv in ws if wv["w004"] is None]
        krit["alle_wechsel_verfeinert"] = not fehlende
        drin = [wv for wv in ws if wv["w004"] is not None and lo <= wv["w004"]["z_stern"] <= hi]
        krit["n_wurzeln_im_fenster"] = len(drin)
        # Beinahe-Nullstellen: |s| an Zeilen ohne benachbarten Wechsel gegen das Maximum derselben Datei
        bn = []
        wechsel_z = {round(z_, 9) for wv in ws for z_ in wv["z"]}
        for g in im:
            r = g[0]
            if r["s"] is None or round(r["z_soll"], 9) in wechsel_z:
                continue
            smax = _smax_datei(r["_datei"])
            if smax and abs(r["s"]) < a.beinahe * smax:
                bn.append({"z": r["z_soll"], "rel": abs(r["s"]) / smax})
        krit["beinahe_nullstellen"] = bn
        krit["keine_beinahe_nullstelle"] = not bn
        if not krit["abtastung_deckt_fenster"]:
            gr.append("Abtastung deckt das erweiterte Fenster nicht")
        if len(drin) != 1:
            e["status"] = "UNRESOLVED"
            gr.append(f"{len(drin)} Wurzeln im Fenster")
        else:
            w = drin[0]["w004"]
            w2 = _passend_eng(w002, w)
            wr = _passend_eng(wrand, w)
            re = w.get("rechteck", {})
            e.update({"omega2_h004": w["x_stern"], "z_h004": w["z_stern"], "rho": w["rho_stern"],
                      "R_wand": w.get("R_wand_stern"), "R_halb_S0": w.get("R_halb_S0_stern"),
                      "umlauf": re.get("umlauf_kreuzung"), "umlauf_phase": re.get("umlauf_phase"),
                      "rechteck_aufgeloest": re.get("aufgeloest"), "rechteck_max_sprung": re.get("max_sprung"),
                      "endklammer_h004": w.get("breite_end"), "schritte_h004": w.get("schritte"),
                      "rauschmass_omega2_h004": w.get("rauschmass_x"),
                      "wachstum_log10_kandidat": w.get("wachstum_log10_kandidat")})
            krit["wurzel_h004_konvergiert"] = bool(w.get("konvergiert"))
            krit["wechsel_in_wurzellauf_bestaetigt"] = bool(w.get("wechsel_bestaetigt"))
            krit["ast_konsistent_wurzellauf"] = bool(w.get("ast_konsistent"))
            krit["umlauf_pm1"] = re.get("umlauf_kreuzung") in (1.0, -1.0)
            krit["umlauf_wechselt"] = re.get("umlauf_kreuzung") == -u_prev
            krit["phase_aufgeloest_und_gleich"] = bool(re.get("aufgeloest")) and \
                re.get("umlauf_phase") is not None and abs(re.get("umlauf_phase") - (re.get("umlauf_kreuzung") or 0)) < 0.01
            if w2 is not None:
                e.update({"omega2_h002": w2["x_stern"], "z_h002": w2["z_stern"], "endklammer_h002": w2.get("breite_end"),
                          "rauschmass_omega2_h002": w2.get("rauschmass_x")})
                krit["h002_konvergiert"] = bool(w2.get("konvergiert")) and bool(w2.get("wechsel_bestaetigt"))
                d_ = w2["x_stern"] - w["x_stern"]
                e["gitter_differenz_omega2"] = d_
                krit["gitter_differenz_unter_1e-6"] = abs(d_) <= 1e-6
            else:
                krit["h002_konvergiert"] = False
                krit["gitter_differenz_unter_1e-6"] = False
            if wr is not None:
                e["randprobe_minus_h004_omega2"] = wr["x_stern"] - w["x_stern"]
                e["randprobe_R_aus"] = wr.get("R_fest")
            om2 = e.get("omega2_h002", w["x_stern"])
            eps = om2 - OM2MIN
            u_om2 = abs(e.get("gitter_differenz_omega2") or 0.0) + max(w.get("breite_end") or 0.0,
                                                                        (w2 or {}).get("breite_end") or 0.0) + \
                max(w.get("rauschmass_x") or 0.0, (w2 or {}).get("rauschmass_x") or 0.0) + \
                abs(e.get("randprobe_minus_h004_omega2") or 0.0)
            u_z = u_om2 / eps ** 2
            e.update({"omega2": om2, "eps": eps, "z": 1.0 / eps, "unsicherheit_omega2": u_om2, "unsicherheit_z": u_z,
                      "lage_aus": "h002" if "omega2_h002" in e else "h004"})
            e["klasse"] = ("A (< 1e-3)" if u_z < 1e-3 else "B (< 1e-2)" if u_z < 1e-2 else "C (< 5e-2)"
                           if u_z < 5e-2 else "D (>= 5e-2)")
            krit["unsicherheit_z_unter_0_05"] = u_z < 0.05
            krit["abstand_fensterrand_groesser_unsicherheit"] = min(e["z"] - lo, hi - e["z"]) > u_z
            hart = ["abtastung_deckt_fenster", "abtastung_fein", "ein_L1_ast_je_zeile", "zielast_alle_zeilen",
                    "ast_richtung_gleich", "ast_stetig", "randzeilen_widerspruchsfrei", "vorzeichen_sicher",
                    "alle_wechsel_verfeinert",
                    "keine_beinahe_nullstelle", "wurzel_h004_konvergiert", "wechsel_in_wurzellauf_bestaetigt",
                    "ast_konsistent_wurzellauf", "umlauf_pm1", "umlauf_wechselt", "h002_konvergiert",
                    "gitter_differenz_unter_1e-6", "unsicherheit_z_unter_0_05",
                    "abstand_fensterrand_groesser_unsicherheit"]
            verletzt = [kk for kk in hart if not krit.get(kk)]
            e["harte_kriterien_verletzt"] = verletzt
            if verletzt:
                e["status"] = "UNRESOLVED"
                gr.append("verletzt: " + ", ".join(verletzt))
            else:
                e["status"] = "OK"
                z_prev, u_prev = e["z"], re.get("umlauf_kreuzung")
        e["kriterien"] = krit
        e["grund"] = "; ".join(gr) if gr else None
        if e["status"] != "OK":
            offen_ab = k
        erg.append(e)
    n_ok = sum(1 for e in erg if e["status"] == "OK")
    if n_ok == len(k_liste):
        gesamt = "vollstaendig"
    elif n_ok == 0:
        gesamt = "gescheitert (keine Fortsetzung eindeutig)"
    else:
        gesamt = f"teilweise UNRESOLVED ab k = {offen_ab}"
    ziele = {str(k): next(e["status"] for e in erg if e["k"] == k) for k in (-10, -18, -25)}
    out = {"titel": "R33 Messseite: Fortsetzungen k = -3 .. -25 der radialen 3D-Leiter bei beta = 1 (VERSIEGELT)",
           "erzeugt": jetzt(), "gesamtstatus": gesamt, "n_gemessen": n_ok, "ziele_status": ziele,
           "konventionen": {"eps": "omega^2 - 3/4", "z": "1/eps", "omega2": "Wurzel auf h = 0,02 (h002), sonst h004",
                            "umlauf": "Kreuzungszaehlung des Rechtecks auf den Startzeilen (h = 0,04)",
                            "unsicherheit_omega2": "|h002 - h004| + groessere Endklammer + groesseres Rauschmass "
                                                   "+ |Randprobe - h004| (falls gerechnet)",
                            "fenster": "[z_prev + b/2, z_prev + 3b/2], b = b_inf = 2,6186 (woertlich)"},
           "start": {"k": -2, "z": a.z_start, "umlauf": a.umlauf_start, "quelle": a.start_quelle},
           "b_inf": B_INF, "abtastung": {"dz": dz, "z_min": z_alle[0] if z_alle else None,
                                         "z_max": z_alle[-1] if z_alle else None, "n_z": len(z_alle),
                                         "dateien": {f: sha(f) for f in dateien}},
           "randzeilen_doppelt": dup, "fortsetzungen": erg,
           "code_sha256": sha(__file__), "bic2_sha256": sha(B.__file__)}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    speichern(a.out, out)
    print(f"kette: {gesamt}, {n_ok} gemessen", flush=True)


_SMAX = {}


def _smax_datei(f):
    if f not in _SMAX:
        with open(f) as fh:
            d = json.load(fh)
        _SMAX[f] = max([abs(r["s"]) for r in d["zeilen"] if r.get("s") is not None] or [0.0])
    return _SMAX[f]


def _lade_wurzeln(muster):
    if not muster:
        return []
    dateien = sorted(set(sum([glob.glob(m) for m in muster.split(",")], [])))
    alle = []
    for f in dateien:
        with open(f) as fh:
            for w in json.load(fh)["wurzeln"]:
                w["_datei"] = f
                alle.append(w)
    return alle


def _passend(ws, x):
    for w in ws:
        if w.get("x_stern") is None:
            continue
        if abs(w["klammer_start"][0] - x[0]) < 1e-12 and abs(w["klammer_start"][1] - x[1]) < 1e-12:
            return w
    return None


def _passend_eng(ws, w0):
    """Lauf aus enger Klammer um die h004-Wurzel w0 (Quelle x_stern_h004 gleich)."""
    for w in ws:
        q = w.get("quelle")
        if isinstance(q, dict) and abs(q.get("x_stern_h004", -1.0) - w0["x_stern"]) < 1e-14 and \
                w.get("x_stern") is not None:
            return w
    return None


# ================================================================ Hauptprogramm

def main():
    ap = argparse.ArgumentParser(description="RUNDE-33 r33-messung (stabilisiert)")
    ap.add_argument("kommando", choices=["zeilen", "wurzel", "kette", "profilvergleich"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--h", type=float, default=0.04)
    ap.add_argument("--n-orth", type=int, default=8)
    ap.add_argument("--z-liste", default="")
    ap.add_argument("--z0", type=float, default=0.0)
    ap.add_argument("--dz", type=float, default=0.0)
    ap.add_argument("--j-von", type=int, default=0)
    ap.add_argument("--j-bis", type=int, default=-1)
    ap.add_argument("--rho0", type=float, default=1.7975138785288294)     # RUNDE-31 k = -2 (h002)
    ap.add_argument("--eps0", type=float, default=0.02488277581474896)
    ap.add_argument("--rho-steig", type=float, default=0.881)
    ap.add_argument("--n-rho", type=int, default=600)
    ap.add_argument("--n-dicht", type=int, default=401)
    ap.add_argument("--dicht-halb", type=float, default=0.04)
    ap.add_argument("--n-zoom", type=int, default=201)
    ap.add_argument("--zoom-runden", type=int, default=2)
    ap.add_argument("--n-rho-schritt", type=int, default=100)
    ap.add_argument("--n-dicht-schritt", type=int, default=201)
    ap.add_argument("--dicht-halb-schritt", type=float, default=2e-4)
    ap.add_argument("--r-zusatz", type=float, default=0.0)
    ap.add_argument("--vergleich", default="")
    ap.add_argument("--r31", default="nein")
    ap.add_argument("--budget", type=float, default=540.0)
    ap.add_argument("--reserve", type=float, default=30.0)
    ap.add_argument("--klammer-x", default="")
    ap.add_argument("--aus-zeilen", default="")
    ap.add_argument("--aus-wurzeln", default="")
    ap.add_argument("--aus-h002", default="")
    ap.add_argument("--aus-rand", default="")
    ap.add_argument("--teil", type=int, default=0)
    ap.add_argument("--teile", type=int, default=1)
    ap.add_argument("--nur-letzte", type=int, default=0)
    ap.add_argument("--klammer-halb", type=float, default=1e-5)
    ap.add_argument("--fortsetzen", action="store_true")
    ap.add_argument("--iter-x", type=int, default=30)
    ap.add_argument("--tol-x", type=float, default=1e-10)
    ap.add_argument("--ast-tol", type=float, default=0.03)
    ap.add_argument("--rechteck", default="ja")
    ap.add_argument("--u-n", type=int, default=60)
    ap.add_argument("--u-runden", type=int, default=30)
    ap.add_argument("--pr-drho", type=float, default=0.01)
    ap.add_argument("--pr-drho-max", type=float, default=0.03)
    ap.add_argument("--z-start", type=float, default=40.18844229618716)    # RUNDE-31 sprossen.json, k = -2, h002
    ap.add_argument("--umlauf-start", type=float, default=-1.0)
    ap.add_argument("--start-quelle", default="RUNDE-31/phase-3d-blind/lauf-69/sprossen.json (b1-km2, h002)")
    ap.add_argument("--beinahe", type=float, default=0.05)
    a = ap.parse_args()
    torch.set_num_threads(1)
    print(f"r33_stab {a.kommando} Start {jetzt()}, torch {torch.__version__}", flush=True)
    {"zeilen": cmd_zeilen, "wurzel": cmd_wurzel, "kette": cmd_kette, "profilvergleich": cmd_profilvergleich}[
        a.kommando](a)
    print(f"Ende {jetzt()}, {uhr():.1f} s", flush=True)


if __name__ == "__main__":
    main()
