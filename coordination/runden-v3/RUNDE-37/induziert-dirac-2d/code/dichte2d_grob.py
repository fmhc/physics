#!/usr/bin/env python3
"""INDUZIERT-DICHTE-2D (Runde 38, Code-Agent): induzierte Steifigkeit der konformen Mode eines masselosen P1-Skalars,
wenn die Punkte mit fester Dichte in der physikalischen Flaeche der Metrik g = e^(2 sigma) delta gestreut und neu
vernetzt werden ("Zahl = Volumen"). 2D-Torus [0, L)^2, L = sqrt(N), sigma = s cos(k.x).

Wiederverwendet (unveraendert): zufall2d.py aus INDUZIERT-ZUFALL-2D (Netz, Kotangens-Laplace, log det' per Erdung
und duenner LU, Netzpruefungen). Konvention wie dort: Gamma = 1/2 log det' K, K aus den Kantenlaengen.

Kopplung (gemeinsame Zufallszahlen): Grundpunkte z_i gleichverteilt (Saat wie INDUZIERT-ZUFALL-2D). Bildpunkte
x_i = psi_s(z_i): Phase phi = k.z, phi' = Phi_s^(-1)(phi) mit Phi_s(t) = int_0^t e^(2 s cos u) du / I0(2s)
= t + sum_m 2 I_m(2s)/(m I0(2s)) sin(m t); x = z + khat (phi' - phi)/|k|, Querkoordinate fest. Die Bildpunkte sind
exakt unabhaengig mit Koordinatendichte e^(2 sigma(x))/I0(2s) verteilt (N fest, physikalische Dichte N/A_g).

Netz bei s != 0:
  koord: Delaunay der Bildpunkte in Koordinaten (Kartenwortlaut)
  intr:  daraus durch Kantenkippen, wo die andere Diagonale ein groesseres physikalisches Kotangens-Gewicht hat
         (moeglichst Delaunay in der physikalischen Metrik; neue Kanten bekommen ihre Laenge aus der Metrik)
Physikalische Laengen (geo): Geodaete zweiter Ordnung um den Kantenmittelpunkt m,
  log l = log|d| + sigma(m) + [b + a^2 - (d x grad sigma)^2]/24, a = d.grad sigma(m), b = (d.grad)^2 sigma(m).
Messgroesse je k: D(S) = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/S^2, y = D/A (A = L^2 = N).

Aufruf (nur ueber kleintest.sh):
  python dichte2d.py kontrolle <aus.json>
  python dichte2d.py fest <N> <saat0> <anzahl> <aus.json> <n-Liste> <S>
  python dichte2d.py dichte <N> <saat0> <anzahl> <aus.json> <n-Liste> <S-Liste> [richtungen=r000,r090] [intr=0/1]

INDUZIERT-DICHTE-2D-GROB (Runde 38): Kopie von dichte2d.py (eingefroren 20261004-073639) mit L als Argument.
  Neu im Modus dichte: Option A=<Torusflaeche>, L = sqrt(A) (Vorgabe A = N, also L = sqrt N wie eingefroren).
  Randstreifen RAND gilt in mittleren Abstaenden L/sqrt(N) (bei L = sqrt N unveraendert 8). Sonst nichts geaendert.
"""
import json
import math
import os
import sys
import time

import numpy as np
from scipy.spatial import Delaunay
from scipy.special import iv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zufall2d as z2  # noqa: E402  (unveraendert aus INDUZIERT-ZUFALL-2D)

POLYAKOV = -1.0 / (24.0 * math.pi)
SAAT_BASIS = 20261004            # wie INDUZIERT-ZUFALL-2D: gleiche Saat -> gleiche Grundpunkte
H_FEST = 1e-2                    # Schritt der Kontrolle "feste Punkte" (Richardson wie INDUZIERT-ZUFALL-2D)
RAND = 8.0                       # Breite der periodischen Randstreifen fuer Delaunay (mittlerer Abstand 1)
W_TOL = 1e-12                    # Kotangens-Gewicht < -W_TOL gilt als nicht Delaunay
FOURIER_M = 30
RICHTUNGEN = {"r000": (1, 0), "r045": (1, 1), "r090": (0, 1), "r135": (-1, 1)}


# ---------------------------------------------------------------------- Grundpunkte, Abbildung psi
def grundpunkte(N, saat, L=None):
    rng = np.random.default_rng([SAAT_BASIS, int(N), int(saat)])
    L = math.sqrt(N) if L is None else L
    return rng.uniform(0.0, L, size=(N, 2)), L


def falten(x, L):
    y = x - L * np.floor(x / L)
    y[y >= L] -= L
    y[y < 0] += L
    return y


def phi_vorwaerts(t, s):
    """Phi_s(t) = int_0^t e^(2 s cos u) du / I0(2s) und Ableitung."""
    tt = 2.0 * s
    i0 = iv(0, tt)
    m = np.arange(1, FOURIER_M + 1)
    coef = 2.0 * iv(m, tt) / (i0 * m)
    F = t + np.sin(np.outer(t, m)) @ coef
    dF = np.exp(tt * np.cos(t)) / i0
    return F, dF


def psi(z, kvec, s, L):
    """Bildpunkte mit Koordinatendichte e^(2 s cos(k.x))/I0(2s); exakte Umkehr der Verteilungsfunktion laengs k."""
    if s == 0.0:
        return z.copy(), {"newton_iter": 0, "residuum": 0.0}
    kb = float(np.linalg.norm(kvec))
    khat = kvec / kb
    phi = np.mod(z @ kvec, 2 * np.pi)
    x = phi - 2.0 * (iv(1, 2 * s) / iv(0, 2 * s)) * np.sin(phi)   # Startwert erster Ordnung
    it = 0
    for it in range(1, 60):
        F, dF = phi_vorwaerts(x, s)
        dx = (F - phi) / dF
        x = x - dx
        if np.max(np.abs(dx)) < 1e-14:
            break
    F, _ = phi_vorwaerts(x, s)
    res = float(np.max(np.abs(F - phi)))
    y = z + np.outer((x - phi) / kb, khat)
    return falten(y, L), {"newton_iter": it, "residuum": res}


# ---------------------------------------------------------------------- periodische Delaunay-Triangulierung
def periodisches_netz(pos, L, art="koord"):
    """Delaunay der Punkte plus Randstreifen der Breite RAND aus den 8 Nachbarkopien (Qhull); behalten werden die
    Dreiecke mit Schwerpunkt im Grundbereich (genau ein Bild je Torusdreieck), Ecken modulo N, Orientierung > 0."""
    N = pos.shape[0]
    rand = RAND * (L / math.sqrt(N))     # RAND in mittleren Abstaenden; bei L = sqrt N genau 8
    tp, ti = [pos], [np.arange(N)]
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            if a == 0 and b == 0:
                continue
            q = pos + np.array([a, b], dtype=float) * L
            m = (q[:, 0] > -rand) & (q[:, 0] < L + rand) & (q[:, 1] > -rand) & (q[:, 1] < L + rand)
            tp.append(q[m])
            ti.append(np.nonzero(m)[0])
    P = np.concatenate(tp)
    I = np.concatenate(ti)
    S = Delaunay(P).simplices
    cen = P[S].mean(axis=1)
    halte = (cen[:, 0] >= 0) & (cen[:, 0] < L) & (cen[:, 1] >= 0) & (cen[:, 1] < L)
    S = S[halte]
    Q = P[S]
    cr = (Q[:, 1, 0] - Q[:, 0, 0]) * (Q[:, 2, 1] - Q[:, 0, 1]) - (Q[:, 1, 1] - Q[:, 0, 1]) * (Q[:, 2, 0] - Q[:, 0, 0])
    tri = I[S]
    flip = cr < 0
    tri[flip] = tri[flip][:, [0, 2, 1]]
    return z2.Netz(pos, tri, L, art)


def netz_pruefen(nz, l):
    """Topologie und Geometrie eines Torusnetzes; Gewichte mit den Laengen l."""
    w, A = nz.gewichte(l)
    return {"V": nz.N, "E": nz.E, "F": nz.F, "euler": int(nz.N - nz.E + nz.F),
            "kanten_genau_zwei": bool(np.all(nz.kanten_zaehl == 2)),
            "orient_min": float(np.min(nz.orient)),
            "koord_flaeche_rel_abw": float(abs(math.fsum(nz.orient.tolist()) / nz.A - 1.0)),
            "phys_flaeche_min": float(np.min(A)), "w_min": float(np.min(w)),
            "w_negativ": int(np.sum(w < -W_TOL)), "w_neg_summe": float(np.sum(w[w < -W_TOL])),
            "l_max_durch_L": float(np.max(nz.l0) / nz.L)}


def gueltig(p):
    return (p["euler"] == 0 and p["kanten_genau_zwei"] and p["orient_min"] > 0 and p["koord_flaeche_rel_abw"] <= 1e-9
            and p["E"] == 3 * p["V"] and p["F"] == 2 * p["V"] and p["phys_flaeche_min"] > 0
            and p["l_max_durch_L"] < 0.25)


# ---------------------------------------------------------------------- physikalische Kantenlaengen
def laengen_geo(nz, kvec, s):
    """Geodaete zweiter Ordnung um den Kantenmittelpunkt (sigma = s cos(k.x))."""
    d = nz.ev
    m = nz.pos[nz.ki] + 0.5 * d
    ph = m @ kvec
    kd = d @ kvec
    kx = d[:, 0] * kvec[1] - d[:, 1] * kvec[0]
    c, sn = np.cos(ph), np.sin(ph)
    korr = (-s * kd * kd * c + s * s * sn * sn * (kd * kd - kx * kx)) / 24.0
    return nz.l0 * np.exp(s * c + korr)


def laengen_ecken(nz, kvec, s):
    sig = np.cos(nz.pos @ kvec)
    return nz.l0 * np.exp(0.5 * s * (sig[nz.ki] + sig[nz.kj]))


def laengen_mitte(nz, kvec, s):
    m = nz.pos[nz.ki] + 0.5 * nz.ev
    return nz.l0 * np.exp(s * np.cos(m @ kvec))


# ---------------------------------------------------------------------- intrinsische Kantenkippung
def geo_paar(pos, i, j, kvec, s, L):
    """Physikalische Laenge (Geodaete zweiter Ordnung) fuer beliebige Punktpaare i -> j (minimales Bild)."""
    d = pos[j] - pos[i]
    d = d - L * np.round(d / L)
    l0 = np.hypot(d[:, 0], d[:, 1])
    m = pos[i] + 0.5 * d
    ph = m @ kvec
    kd = d @ kvec
    kx = d[:, 0] * kvec[1] - d[:, 1] * kvec[0]
    c, sn = np.cos(ph), np.sin(ph)
    return l0 * np.exp(s * c + (-s * kd * kd * c + s * s * sn * sn * (kd * kd - kx * kx)) / 24.0)


def intrinsisch(nz, kvec, s, max_runden=40):
    """Kippt Kanten mit negativem Kotangens-Gewicht (physikalische Laengen) in unabhaengigen Durchgaengen, aber nur,
    wenn die andere Diagonale (Laenge aus der Metrik) ein groesseres Gewicht hat ("nur verbessern"; sonst pendeln
    Vierecke, deren Kruemmungsdefekt groesser als ihr Abstand vom Kozirkularen ist). Prueft die Orientierung."""
    tri = nz.tri.copy()
    gesamt, runden = 0, 0
    pos, L = nz.pos, nz.L
    while True:
        l = laengen_geo(nz, kvec, s)
        w, _ = nz.gewichte(l)
        bad = np.nonzero(w < -W_TOL)[0]
        if bad.size == 0 or runden >= max_runden:
            break
        order = np.argsort(nz.tk.ravel(), kind="stable")
        tr = (order // 3).reshape(-1, 2)
        lc = (order % 3).reshape(-1, 2)
        t1, t2 = tr[bad, 0], tr[bad, 1]
        c1, c2 = lc[bad, 0], lc[bad, 1]
        p, a, b = tri[t1, c1], tri[t1, (c1 + 1) % 3], tri[t1, (c1 + 2) % 3]
        q = tri[t2, c2]
        konsistent = (tri[t2, (c2 + 1) % 3] == b) & (tri[t2, (c2 + 2) % 3] == a)
        e_bp, e_pa = nz.tk[t1, (c1 + 1) % 3], nz.tk[t1, (c1 + 2) % 3]
        e_aq, e_qb = nz.tk[t2, (c2 + 1) % 3], nz.tk[t2, (c2 + 2) % 3]
        l_pq = geo_paar(pos, p, q, kvec, s, L)
        A1 = z2.flaeche_kahan(l[e_aq], l[e_pa], l_pq)
        A2 = z2.flaeche_kahan(l[e_qb], l[e_bp], l_pq)
        with np.errstate(divide="ignore", invalid="ignore"):
            w_alt = (0.125 * (l[e_aq] ** 2 + l[e_pa] ** 2 - l_pq ** 2) / A1
                     + 0.125 * (l[e_qb] ** 2 + l[e_bp] ** 2 - l_pq ** 2) / A2)

        def rel(u, v):
            d = pos[u] - pos[v]
            return d - L * np.round(d / L)
        vq, vp, vb = rel(q, a), rel(p, a), rel(b, a)
        o1 = vq[:, 0] * vp[:, 1] - vq[:, 1] * vp[:, 0]
        o2 = (vb[:, 0] - vq[:, 0]) * (vp[:, 1] - vq[:, 1]) - (vb[:, 1] - vq[:, 1]) * (vp[:, 0] - vq[:, 0])
        kand = konsistent & (o1 > 0) & (o2 > 0) & (A1 > 0) & (A2 > 0) & np.isfinite(w_alt) & (w_alt > w[bad])
        idx = np.nonzero(kand)[0]
        idx = idx[np.argsort(w[bad][idx])]
        used = np.zeros(nz.F, dtype=bool)
        neu = tri.copy()
        n_flip = 0
        for j in idx:
            u1, u2 = int(t1[j]), int(t2[j])
            if used[u1] or used[u2]:
                continue
            neu[u1] = (a[j], q[j], p[j])
            neu[u2] = (q[j], b[j], p[j])
            used[u1] = used[u2] = True
            n_flip += 1
        if n_flip == 0:
            break
        tri = neu
        nz = z2.Netz(pos, tri, L, "intr")
        gesamt += n_flip
        runden += 1
    l = laengen_geo(nz, kvec, s)
    w, _ = nz.gewichte(l)
    neg = w < -W_TOL
    return nz, l, {"gekippt": gesamt, "durchgaenge": runden, "rest_negativ": int(np.sum(neg)),
                   "w_min": float(np.min(w)), "w_neg_summe": float(np.sum(w[neg]))}


def kanten_schluessel(nz):
    return nz.ki * nz.N + nz.kj


def neue_kanten(nz, schluessel0):
    return int(np.sum(~np.isin(kanten_schluessel(nz), schluessel0, assume_unique=True)))


# ---------------------------------------------------------------------- eine Auswertung bei (k, s)
def auswerten_s(z, L, kvec, s, schluessel0, mit_intr=False):
    t0 = time.time()
    x, pinfo = psi(z, kvec, s, L)
    nz = periodisches_netz(x, L, "koord")
    t_netz = time.time() - t0
    lk = laengen_geo(nz, kvec, s)
    pk = netz_pruefen(nz, lk)
    out = {"s": s, "psi": pinfo, "koord_pruefung": pk, "koord_neue_kanten": neue_kanten(nz, schluessel0)}
    out["gamma_koord"] = nz.gamma(lk)
    out["lu"] = {"koord": dict(nz.lu_info)}
    if mit_intr:
        t1 = time.time()
        ni, li, finfo = intrinsisch(nz, kvec, s)
        out["intr"] = finfo
        out["intr_pruefung"] = netz_pruefen(ni, li)
        out["intr_neue_kanten"] = neue_kanten(ni, schluessel0)
        out["gamma_intr"] = ni.gamma(li) if ni is not nz else out["gamma_koord"]
        out["lu"]["intr"] = dict(ni.lu_info)
        out["sek_kippen"] = time.time() - t1
    out["sek"] = {"netz": t_netz, "gesamt": time.time() - t0}
    return out


# ---------------------------------------------------------------------- Modi
def modus_dichte(N, saat0, anzahl, ziel, nlist, Slist, richtungen, mit_intr, protokoll, out, A_torus=None):
    A_torus = float(N) if A_torus is None else float(A_torus)
    out.update({"N": N, "L": math.sqrt(A_torus), "A": A_torus, "nlist": nlist, "S": Slist, "richtungen": richtungen,
                "mit_intr": mit_intr, "saaten": []})
    for saat in range(saat0, saat0 + anzahl):
        t0 = time.time()
        z, L = grundpunkte(N, saat, math.sqrt(A_torus))
        n0 = periodisches_netz(z, L, "basis")
        p0 = netz_pruefen(n0, n0.l0)
        p0_z2 = n0.pruefen()
        g0 = n0.gamma(n0.l0)
        sch0 = kanten_schluessel(n0)
        A = A_torus
        pts = []
        for rn in richtungen:
            r = RICHTUNGEN[rn]
            for n in nlist:
                kint = (n * r[0], n * r[1])
                kvec = 2 * np.pi * np.asarray(kint, dtype=float) / L
                kb = float(np.linalg.norm(kvec))
                pt = {"richtung": rn, "n": n, "kint": list(kint), "betrag": kb, "k2A": kb * kb * A, "je_S": []}
                for S in Slist:
                    plus = auswerten_s(z, L, kvec, S, sch0, mit_intr)
                    minus = auswerten_s(z, L, kvec, -S, sch0, mit_intr)
                    Dk = (plus["gamma_koord"] + minus["gamma_koord"] - 2 * g0) / (S * S)
                    e = {"S": S, "plus": plus, "minus": minus, "D_koord": Dk, "y_koord": Dk / A,
                         "c_koord_direkt": Dk / (kb * kb * A)}
                    if mit_intr:
                        Di = (plus["gamma_intr"] + minus["gamma_intr"] - 2 * g0) / (S * S)
                        e.update({"D_intr": Di, "y_intr": Di / A, "c_intr_direkt": Di / (kb * kb * A)})
                    pt["je_S"].append(e)
                pts.append(pt)
                protokoll(f"N={N} saat={saat} {rn} n={n} |k|={kb:.4f}: " + "; ".join(
                    f"S={e['S']}: y_koord {e['y_koord']:+.6f}"
                    + (f" y_intr {e['y_intr']:+.6f} kipp_i {e['plus']['intr']['gekippt']} rest "
                       f"{e['plus']['intr']['rest_negativ']}" if mit_intr else "")
                    + f" neu {e['plus']['koord_neue_kanten']} neg {e['plus']['koord_pruefung']['w_negativ']}"
                    f" {e['plus']['sek']['gesamt']:.1f}s" for e in pt["je_S"]))
        out["saaten"].append({"saat": saat, "gamma0": g0, "pruefung0": p0, "pruefung0_z2": p0_z2, "punkte": pts,
                              "lu0": dict(n0.lu_info), "sekunden": time.time() - t0})
        with open(ziel + ".tmp", "w") as f:
            json.dump(out, f)
        os.replace(ziel + ".tmp", ziel)
        protokoll(f"N={N} saat={saat} fertig in {time.time() - t0:.1f} s")
    return out


def modus_fest(N, saat0, anzahl, ziel, nlist, S, richtungen, protokoll, out):
    """Kontrolle ID0: feste Grundpunkte und festes Netz, nur die Kantenlaengen aendern sich."""
    out.update({"N": N, "L": math.sqrt(N), "nlist": nlist, "S": S, "h": H_FEST, "richtungen": richtungen,
                "saaten": []})
    for saat in range(saat0, saat0 + anzahl):
        t0 = time.time()
        z, L = grundpunkte(N, saat)
        n0 = periodisches_netz(z, L, "basis")
        p0 = n0.pruefen()
        g0 = n0.gamma(n0.l0)
        A = float(N)
        pts = []
        for rn in richtungen:
            r = RICHTUNGEN[rn]
            for n in nlist:
                kint = (n * r[0], n * r[1])
                kvec = 2 * np.pi * np.asarray(kint, dtype=float) / L
                kb = float(np.linalg.norm(kvec))
                pt = {"richtung": rn, "n": n, "kint": list(kint), "betrag": kb, "k2A": kb * kb * A}
                for name, lf in (("geo", laengen_geo), ("ecken", laengen_ecken), ("mitte", laengen_mitte)):
                    R, D1, D2, g1 = z2.zweite(lambda s, lf=lf: n0.gamma(lf(n0, kvec, s)), H_FEST, g0)
                    pt[name] = {"gamma2": R, "D_h": D1, "D_2h": D2, "c": R / (kb * kb * A),
                                "richardson_abw_rel": abs(D1 - R) / max(abs(R), 1e-300)}
                DS = (n0.gamma(laengen_geo(n0, kvec, S)) + n0.gamma(laengen_geo(n0, kvec, -S)) - 2 * g0) / (S * S)
                pt["geo_S"] = {"S": S, "D": DS, "c": DS / (kb * kb * A), "y": DS / A}
                pts.append(pt)
                protokoll(f"fest N={N} saat={saat} {rn} n={n} |k|={kb:.4f}: c geo {pt['geo']['c']:.6f} ecken "
                          f"{pt['ecken']['c']:.6f} mitte {pt['mitte']['c']:.6f} geo(S={S}) {pt['geo_S']['c']:.6f}")
        out["saaten"].append({"saat": saat, "gamma0": g0, "pruefung0": p0, "punkte": pts, "lu": dict(n0.lu_info),
                              "sekunden": time.time() - t0})
        with open(ziel + ".tmp", "w") as f:
            json.dump(out, f)
        os.replace(ziel + ".tmp", ziel)
    return out


def geodaete_numerisch(x0, d, kvec, s, ordnung=64):
    """Laenge der kuerzesten Kurve aus der Familie gamma(t) = x0 + t d + n (c1 t(1-t) + c2 t(1-t)(2t-1)) in der Metrik
    e^(2 sigma); Gauss-Legendre."""
    from scipy.optimize import minimize
    tg, wg = np.polynomial.legendre.leggauss(ordnung)
    t = 0.5 * (tg + 1)
    w = 0.5 * wg
    l = np.linalg.norm(d)
    nvec = np.array([-d[1], d[0]]) / l

    def laenge(c):
        b1, b2 = t * (1 - t), t * (1 - t) * (2 * t - 1)
        db1, db2 = 1 - 2 * t, (1 - t) * (2 * t - 1) - t * (2 * t - 1) + 2 * t * (1 - t)
        g = x0[None, :] + t[:, None] * d[None, :] + (c[0] * b1 + c[1] * b2)[:, None] * nvec[None, :]
        dg = d[None, :] + (c[0] * db1 + c[1] * db2)[:, None] * nvec[None, :]
        return float(np.sum(w * np.exp(s * np.cos(g @ kvec)) * np.linalg.norm(dg, axis=1)))

    r = minimize(laenge, np.zeros(2), method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-15,
                                                                         "maxiter": 4000})
    return r.fun, laenge(np.zeros(2))


def modus_kontrolle(protokoll, kipp_N=(16000,)):
    out = {}
    # (K1) Abbildung psi: Newton-Residuum, Momente und KS-Abstand der Bildphasen
    N = 64000
    z, L = grundpunkte(N, 990)
    k1 = []
    for kint in ((2, 0), (3, 3)):
        kvec = 2 * np.pi * np.asarray(kint, float) / L
        for s in (0.25, -0.25, 0.5, -0.5):
            x, info = psi(z, kvec, s, L)
            ph = np.mod(x @ kvec, 2 * np.pi)
            F, _ = phi_vorwaerts(np.sort(ph), s)
            emp = (np.arange(1, N + 1) - 0.5) / N
            ks = float(np.max(np.abs(F / (2 * np.pi) - emp)))
            m1 = float(np.mean(np.exp(-2 * s * np.cos(ph))))
            m2 = float(np.mean(np.cos(ph)))
            k1.append({"kint": list(kint), "s": s, "newton": info, "ks": ks, "ks_mal_wurzelN": ks * math.sqrt(N),
                       "mittel_e^-2sigma": m1, "soll_1/I0": float(1 / iv(0, 2 * s)),
                       "mittel_cos": m2, "soll_I1/I0": float(iv(1, 2 * s) / iv(0, 2 * s)),
                       "z_e^-2sigma": (m1 - 1 / iv(0, 2 * s)) / (np.std(np.exp(-2 * s * np.cos(ph))) / math.sqrt(N)),
                       "z_cos": (m2 - iv(1, 2 * s) / iv(0, 2 * s)) / (np.std(np.cos(ph)) / math.sqrt(N)),
                       "querkoordinate_unveraendert": float(np.max(np.abs(
                           ((x - z) - L * np.round((x - z) / L)) @ np.array([-kvec[1], kvec[0]]))))})
            protokoll(f"K1 psi kint={kint} s={s}: Newton {info}, KS*sqrt(N) {ks * math.sqrt(N):.3f}, "
                      f"z(e^-2sig) {k1[-1]['z_e^-2sigma']:+.2f}, z(cos) {k1[-1]['z_cos']:+.2f}")
    out["K1_psi"] = k1
    # (K2) Randstreifen-Delaunay gegen 9 Kopien (zufall2d.zufallsnetz) und gegen Bildpunkte
    k2 = []
    for Nk, saat in ((4000, 990), (16000, 991)):
        za, La = grundpunkte(Nk, saat)
        a = periodisches_netz(za, La)
        b = z2.zufallsnetz(Nk, saat)
        ta = np.sort(np.sort(a.tri, axis=1), axis=0)
        tb = np.sort(np.sort(b.tri, axis=1), axis=0)
        sa = set(map(tuple, np.sort(a.tri, axis=1).tolist()))
        sb = set(map(tuple, np.sort(b.tri, axis=1).tolist()))
        kvec = 2 * np.pi * np.array([2.0, 0.0]) / La
        x, _ = psi(za, kvec, 0.5, La)
        c = periodisches_netz(x, La)
        P = np.concatenate([x + np.array([i, j], float) * La for i in (-1, 0, 1) for j in (-1, 0, 1)])
        Sx = Delaunay(P).simplices
        cen = P[Sx].mean(axis=1)
        h = (cen[:, 0] >= 0) & (cen[:, 0] < La) & (cen[:, 1] >= 0) & (cen[:, 1] < La)
        sx = set(map(tuple, np.sort(Sx[h] % Nk, axis=1).tolist()))
        sc = set(map(tuple, np.sort(c.tri, axis=1).tolist()))
        k2.append({"N": Nk, "saat": saat, "gleich_grund": sa == sb, "gleich_bild_s0.5": sx == sc,
                   "F": int(a.F), "gamma_streifen": a.gamma(a.l0), "gamma_9kopien": b.gamma(b.l0),
                   "pruefung_bild": netz_pruefen(c, laengen_geo(c, kvec, 0.5)), "_shape": [int(ta.shape[0]),
                                                                                          int(tb.shape[0])]})
        protokoll(f"K2 N={Nk}: Streifen = 9 Kopien {sa == sb}, Bildpunkte {sx == sc}, Gamma "
                  f"{k2[-1]['gamma_streifen']:.10f} / {k2[-1]['gamma_9kopien']:.10f}")
    out["K2_streifen"] = k2
    # (K3) Laengenformel gegen numerische Geodaete (Zwei-Parameter-Kurvenfamilie) und Linienintegral
    rng = np.random.default_rng(SAAT_BASIS + 3)
    k3 = []
    for _ in range(60):
        kb = rng.uniform(0.05, 0.4)
        th = rng.uniform(0, 2 * np.pi)
        kvec = kb * np.array([np.cos(th), np.sin(th)])
        s = rng.choice([0.25, 0.5]) * rng.choice([-1, 1])
        x0 = rng.uniform(0, 50, 2)
        l = rng.uniform(0.3, 3.0)
        ph = rng.uniform(0, 2 * np.pi)
        d = l * np.array([np.cos(ph), np.sin(ph)])

        class E:
            pass
        e = E()
        e.ev = d[None, :]
        e.pos = x0[None, :]
        e.ki = np.array([0])
        e.l0 = np.array([l])
        lg = float(laengen_geo(e, kvec, s)[0])
        lm = float(laengen_mitte(e, kvec, s)[0])
        le = float(np.exp(0.5 * s * (np.cos(x0 @ kvec) + np.cos((x0 + d) @ kvec))) * l)
        lnum, lline = geodaete_numerisch(x0, d, kvec, s)
        k3.append({"k": kb, "s": s, "l": l, "kl_s": abs(s) * kb * l, "rel_geo": lg / lnum - 1,
                   "rel_mitte": lm / lnum - 1, "rel_ecken": le / lnum - 1, "rel_linie": lline / lnum - 1})
    arr = {key: np.array([x[key] for x in k3]) for key in ("kl_s", "rel_geo", "rel_mitte", "rel_ecken")}
    out["K3_geodaete"] = {"einzeln": k3, "max_abs_rel_geo": float(np.max(np.abs(arr["rel_geo"]))),
                          "max_abs_rel_mitte": float(np.max(np.abs(arr["rel_mitte"]))),
                          "max_abs_rel_ecken": float(np.max(np.abs(arr["rel_ecken"]))),
                          "max_kl_s": float(np.max(arr["kl_s"]))}
    protokoll(f"K3 Geodaete (max |s| k l = {np.max(arr['kl_s']):.3f}): geo {np.max(np.abs(arr['rel_geo'])):.2e}, "
              f"mitte {np.max(np.abs(arr['rel_mitte'])):.2e}, ecken {np.max(np.abs(arr['rel_ecken'])):.2e}")
    # (K4) log det' per LU gegen dicht auf kleinen Bildnetzen (koord und intr, physikalische Laengen)
    k4 = []
    for saat in (990, 991):
        za, La = grundpunkte(400, saat)
        kvec = 2 * np.pi * np.array([1.0, 1.0]) / La
        x, _ = psi(za, kvec, 0.5, La)
        nz = periodisches_netz(x, La)
        lk = laengen_geo(nz, kvec, 0.5)
        ni, li, fi = intrinsisch(nz, kvec, 0.5)
        for name, nn, ll in (("koord", nz, lk), ("intr", ni, li)):
            w, _ = nn.gewichte(ll)
            K = nn.matrix_voll_dicht(w)
            sgn, ld = np.linalg.slogdet(K + 1.0 / 400)
            ev = np.linalg.eigvalsh(K)
            g = nn.gamma(ll)
            k4.append({"saat": saat, "netz": name, "gamma_lu": g, "abw_slogdet": abs(g - 0.5 * ld),
                       "abw_eigen": abs(g - 0.5 * math.fsum(np.log(ev[1:]).tolist())), "vorzeichen": float(sgn),
                       "eigen_min_abs": float(abs(ev[0])), "eigen_2": float(ev[1]), "w_negativ": int(np.sum(w < -W_TOL)),
                       "kippen": fi if name == "intr" else None})
            protokoll(f"K4 N=400 saat={saat} {name}: LU gegen slogdet {k4[-1]['abw_slogdet']:.2e}, Eigenwerte "
                      f"{k4[-1]['abw_eigen']:.2e}, negative Gewichte {k4[-1]['w_negativ']}")
    out["K4_logdet"] = k4
    # (K5) Kantenkippen gegen s (ohne LU)
    k5 = []
    for Nk in kipp_N:
        za, La = grundpunkte(Nk, 990)
        n0 = periodisches_netz(za, La)
        sch0 = kanten_schluessel(n0)
        for kb_soll in (0.05, 0.1, 0.2, 0.3):
            n = max(1, int(round(kb_soll * La / (2 * np.pi))))
            kvec = 2 * np.pi * np.array([n, 0.0]) / La
            for s in (1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.2, 0.3, 0.5):
                x, _ = psi(za, kvec, s, La)
                nz = periodisches_netz(x, La)
                lk = laengen_geo(nz, kvec, s)
                w, _ = nz.gewichte(lk)
                ni, li, fi = intrinsisch(nz, kvec, s)
                k5.append({"N": Nk, "n": n, "betrag": float(np.linalg.norm(kvec)), "s": s,
                           "koord_neu": neue_kanten(nz, sch0), "intr_neu": neue_kanten(ni, sch0),
                           "koord_negativ": int(np.sum(w < -W_TOL)), "intr": fi, "E": int(nz.E)})
            protokoll(f"K5 N={Nk} n={n}: " + ", ".join(f"s={x['s']}: {x['koord_neu']}/{x['intr_neu']} "
                                                       f"(neg {x['koord_negativ']})" for x in k5 if x['n'] == n and
                                                       x['N'] == Nk))
    out["K5_kippen"] = k5
    return out


def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    import scipy
    out = {"modus": modus, "argv": sys.argv[1:], "numpy": np.__version__, "scipy": scipy.__version__}
    if modus == "kontrolle":
        ziel = sys.argv[2]
        kipp = tuple(int(x) for x in sys.argv[3].split(",")) if len(sys.argv) > 3 else (16000,)
        out.update(modus_kontrolle(protokoll, kipp))
    elif modus == "fest":
        N, saat0, anzahl, ziel = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        nlist = [int(x) for x in sys.argv[6].split(",")]
        S = float(sys.argv[7])
        richt = sys.argv[8].split("=")[1].split(",") if len(sys.argv) > 8 else ["r000", "r090"]
        modus_fest(N, saat0, anzahl, ziel, nlist, S, richt, protokoll, out)
    elif modus == "dichte":
        N, saat0, anzahl, ziel = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        nlist = [int(x) for x in sys.argv[6].split(",")]
        Slist = [float(x) for x in sys.argv[7].split(",")]
        opt = dict(a.split("=", 1) for a in sys.argv[8:])
        richt = opt.get("richtungen", "r000,r090").split(",")
        mit_intr = opt.get("intr", "0") == "1"
        A_torus = float(opt["A"]) if "A" in opt else None
        modus_dichte(N, saat0, anzahl, ziel, nlist, Slist, richt, mit_intr, protokoll, out, A_torus)
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["protokoll"] = log
    with open(ziel + ".tmp", "w") as f:
        json.dump(out, f)
    os.replace(ziel + ".tmp", ziel)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
