#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUERTEL-1 (Runde 41, RUNDE-37/guertel-1): angebundener Tetraeder-Knoten mit vier Faeden.

Synthetische Modellrechnung, keine Messdaten. Modell und Regeln: PLAN.md.

Modi:
  rauch      Laufzeit, Stabilitaet, Durchdringungsprobe (gibt keine Energie- und Windungswerte aus)
  protokoll  Drehprotokoll 0..1440 Grad in kleinen Schritten mit Relaxation (drei Systeme je Fadenlaenge)
  abkuehlen  Langevin-Abkuehlen je Gitterwinkel und Saat bei festem Koerper
  sperre     Stringmethode zwischen gewickeltem 720-Grad-Zustand und entwirrtem Endzustand

Aufruf nur ueber kleintest.sh auf der .69.
"""
import argparse
import hashlib
import json
import os
import sys
import time

import numpy as np
import scipy.sparse as sps

# ---------------- feste Modellgroessen (PLAN.md Abschnitt 2) ----------------
A_KOERPER = 1.0                 # Radius der Ausschlusskugel des Koerpers
SIG = 0.2                       # Fadendicke = Kontaktabstand der Mittellinien
R_AUSSEN = 3.0                  # Aussenwand (Ankerkugel)
R_ATT = A_KOERPER + SIG / 2.0   # Ansatzpunkte am Koerper
R_ANK = R_AUSSEN - SIG / 2.0    # Anker
D_GERADE = R_ANK - R_ATT        # gerader Abstand 1.8
K_DEHN = 20.0                   # k_s * b0^2
K_BIEG = 2.0                    # Biegung je Gelenk und Einspannung
SG_FF = SIG / 2.0 ** (1.0 / 6.0)
SG_W = (SIG / 2.0) / 2.0 ** (1.0 / 6.0)
GRENZE_FF = 0.5 * SIG           # Ausschlussgrenze Faden-Faden (Mittellinien)
SEGMENTE = {1.3: 12, 1.8: 16}
H_DREH = 1.0e-4                 # Schrittweite (rad) fuer das Drehmoment
GITTER = list(range(0, 721, 30)) + [1080, 1440]

U_TET = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float) / np.sqrt(3.0)
U_EBENE = np.array([[0, 1, 1], [0, -1, -1], [0, 1, -1], [0, -1, 1]], float) / np.sqrt(2.0)
ACHSE_2 = np.array([1.0, 0.0, 0.0])
ACHSE_G = np.array([4.0, 2.0, 1.0]) / np.sqrt(21.0)
SYSTEME = [
    {"name": "zweizaehlig", "U": U_TET, "achse": ACHSE_2, "eben": False},
    {"name": "allgemein", "U": U_TET, "achse": ACHSE_G, "eben": False},
    {"name": "ebene", "U": U_EBENE, "achse": ACHSE_2, "eben": True},
]


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def rot(n, th):
    """Drehmatrizen (B,3,3) um Achsen n (B,3) mit Winkeln th (B,) (Rodrigues, rechte Hand)."""
    c = np.cos(th)
    s = np.sin(th)
    C = 1.0 - c
    x, y, z = n[:, 0], n[:, 1], n[:, 2]
    R = np.empty((len(th), 3, 3))
    R[:, 0, 0] = c + x * x * C
    R[:, 0, 1] = x * y * C - z * s
    R[:, 0, 2] = x * z * C + y * s
    R[:, 1, 0] = y * x * C + z * s
    R[:, 1, 1] = c + y * y * C
    R[:, 1, 2] = y * z * C - x * s
    R[:, 2, 0] = z * x * C - y * s
    R[:, 2, 1] = z * y * C + x * s
    R[:, 2, 2] = c + z * z * C
    return R


class Netz:
    """Index-Struktur fuer vier Faeden mit je ns Segmenten."""

    def __init__(self, lfak):
        self.lfak = float(lfak)
        ns = SEGMENTE[self.lfak]
        self.ns = ns
        self.npf = ns + 1
        self.nb = 4 * self.npf
        self.S = 4 * ns
        self.L = self.lfak * D_GERADE
        self.b0 = self.L / ns
        self.ks = K_DEHN / self.b0 ** 2
        sa, sb, sf, sk = [], [], [], []
        for i in range(4):
            for k in range(ns):
                sa.append(self.bead(i, k))
                sb.append(self.bead(i, k + 1))
                sf.append(i)
                sk.append(k)
        self.seg_a = np.array(sa)
        self.seg_b = np.array(sb)
        self.seg_f = np.array(sf)
        self.seg_k = np.array(sk)
        j1, j2 = [], []
        for i in range(4):
            for k in range(ns - 1):
                j1.append(i * ns + k)
                j2.append(i * ns + k + 1)
        self.j1 = np.array(j1)
        self.j2 = np.array(j2)
        self.s_erst = np.array([i * ns for i in range(4)])
        self.s_letzt = np.array([i * ns + ns - 1 for i in range(4)])
        pi, pj, em = [], [], []
        for s1 in range(self.S):
            for s2 in range(s1 + 1, self.S):
                gleich = sf[s1] == sf[s2]
                dk = abs(sk[s1] - sk[s2])
                if gleich and dk <= 1:
                    continue  # gemeinsame Perle: keine Probe, keine Energie
                pi.append(s1)
                pj.append(s2)
                em.append(not (gleich and dk <= 2))
        self.pi = np.array(pi)
        self.pj = np.array(pj)
        self.emask = np.array(em)
        frei = np.ones(self.nb, bool)
        for i in range(4):
            frei[self.bead(i, 0)] = False
            frei[self.bead(i, ns)] = False
        self.frei = frei
        rows = np.arange(self.S)
        self.IncA = sps.csr_matrix((np.ones(self.S), (self.seg_a, rows)), shape=(self.nb, self.S))
        self.IncB = sps.csr_matrix((np.ones(self.S), (self.seg_b, rows)), shape=(self.nb, self.S))

    def bead(self, i, k):
        return i * self.npf + k


class Stapel:
    """B unabhaengige Systeme gleicher Fadenlaenge (System-Index, Winkel je Eintrag)."""

    def __init__(self, netz, sysidx, theta):
        self.n = netz
        self.sysidx = np.asarray(sysidx, int)
        self.B = len(self.sysidx)
        self.theta = np.asarray(theta, float).copy()
        self.U = np.stack([SYSTEME[s]["U"] for s in self.sysidx])
        self.achse = np.stack([SYSTEME[s]["achse"] for s in self.sysidx])
        self.eben = np.array([SYSTEME[s]["eben"] for s in self.sysidx])
        self.ua = np.ascontiguousarray(self.U.transpose(1, 0, 2))
        self.wca = 1.0  # 0.0 nur in der Gegenprobe (Ausschluss Faden-Faden und Faden-Koerper aus)

    def setze_fest(self, X, theta=None):
        th = self.theta if theta is None else theta
        R = rot(self.achse, th)
        cb = np.einsum("bij,bfj->fbi", R, self.U)
        n = self.n
        for i in range(4):
            X[n.bead(i, 0)] = R_ATT * cb[i]
            X[n.bead(i, n.ns)] = R_ANK * self.ua[i]
        return cb

    def projiziere(self, V):
        V[~self.n.frei] = 0.0
        if self.eben.any():
            nrm = self.achse
            comp = (V * nrm[None]).sum(-1)
            V -= (comp * self.eben[None])[..., None] * nrm[None]
        return V


def naechste(P1, D1, P2, D2):
    """Naechste Punkte zweier Strecken (Ericson), vektorisiert; gibt s, t, C1-C2, Abstand."""
    r = P1 - P2
    a = (D1 * D1).sum(-1)
    e = (D2 * D2).sum(-1)
    f = (D2 * r).sum(-1)
    c = (D1 * r).sum(-1)
    b = (D1 * D2).sum(-1)
    den = a * e - b * b
    ok = den > 1.0e-12 * a * e
    s = np.where(ok, np.clip((b * f - c * e) / np.where(ok, den, 1.0), 0.0, 1.0), 0.0)
    t = (b * s + f) / e
    tlo = t < 0.0
    thi = t > 1.0
    s = np.where(tlo, np.clip(-c / a, 0.0, 1.0), np.where(thi, np.clip((b - c) / a, 0.0, 1.0), s))
    t = np.clip(t, 0.0, 1.0)
    Cd = (P1 + s[:, None] * D1) - (P2 + t[:, None] * D2)
    dist = np.sqrt((Cd * Cd).sum(-1))
    return s, t, Cd, dist


def streu(G, perlen, sysi, werte):
    nb, B, _ = G.shape
    flat = perlen * B + sysi
    for c in range(3):
        G[:, :, c] += np.bincount(flat, weights=werte[:, c], minlength=nb * B).reshape(nb, B)


def energie(st, X, cb, grad=True):
    """Gesamtenergie (B,), Gradient (nb,B,3) und Sonde (dmin_e, dmin_p, rho_min, r_max)."""
    n = st.n
    B = X.shape[1]
    P = X[n.seg_a]
    Q = X[n.seg_b]
    D = Q - P
    Ls = np.sqrt((D * D).sum(-1))
    T = D / Ls[..., None]
    E = np.zeros(B)
    ex = Ls - n.b0
    E += 0.5 * n.ks * (ex * ex).sum(0)
    t1 = T[n.j1]
    t2 = T[n.j2]
    E += K_BIEG * (1.0 - (t1 * t2).sum(-1)).sum(0)
    tf = T[n.s_erst]
    tl = T[n.s_letzt]
    E += K_BIEG * (1.0 - (tf * cb).sum(-1)).sum(0)
    E += K_BIEG * (1.0 - (tl * st.ua).sum(-1)).sum(0)
    # Koerperwand (Segment-Kugel)
    pd = (P * D).sum(-1)
    sst = np.clip(-pd / (Ls * Ls), 0.0, 1.0)
    C = P + sst[..., None] * D
    rho = np.sqrt((C * C).sum(-1))
    dl = rho - A_KOERPER
    mw = dl < SIG / 2.0
    dlc = np.maximum(dl, 1.0e-4)
    srw = (SG_W / dlc) ** 6
    E += st.wca * np.where(mw, 4.0 * (srw * srw - srw) + 1.0, 0.0).sum(0)
    # Aussenwand (freie Perlen)
    r = np.sqrt((X * X).sum(-1))
    do = R_AUSSEN - r
    mo = (do < SIG / 2.0) & n.frei[:, None]
    doc = np.maximum(do, 1.0e-4)
    sro = (SG_W / doc) ** 6
    E += np.where(mo, 4.0 * (sro * sro - sro) + 1.0, 0.0).sum(0)
    # Faden-Faden (Kapseln), Vorauswahl ueber Mittelpunktabstand
    M = 0.5 * (P + Q)
    Mb = np.ascontiguousarray(M.transpose(1, 0, 2))
    nq = (Mb * Mb).sum(-1)
    G2 = np.matmul(Mb, Mb.transpose(0, 2, 1))
    d2 = nq[:, :, None] + nq[:, None, :] - 2.0 * G2
    dmp = np.sqrt(np.maximum(d2[:, n.pi, n.pj], 0.0))
    LsT = Ls.T
    lb = dmp - 0.5 * (LsT[:, n.pi] + LsT[:, n.pj])
    kb, kp = np.nonzero(lb < SIG)
    dmin_e = np.full(B, SIG)
    dmin_p = np.full(B, SIG)
    if len(kp):
        s1 = n.pi[kp]
        s2 = n.pj[kp]
        s, t, Cd, dist = naechste(P[s1, kb], D[s1, kb], P[s2, kb], D[s2, kb])
        np.minimum.at(dmin_p, kb, dist)
        eme = n.emask[kp]
        if eme.any():
            np.minimum.at(dmin_e, kb[eme], dist[eme])
        me = eme & (dist < SIG)
        dd = np.maximum(dist, 1.0e-6)
        sr = (SG_FF / dd) ** 6
        Uf = st.wca * np.where(me, 4.0 * (sr * sr - sr) + 1.0, 0.0)
        E += np.bincount(kb, weights=Uf, minlength=B)
    sonde = (dmin_e, dmin_p, rho.min(0), r.max(0))
    if not grad:
        return E, None, sonde
    dEdD = (n.ks * ex)[..., None] * T
    dEdT = np.zeros_like(T)
    dEdT[n.j1] += -K_BIEG * t2
    dEdT[n.j2] += -K_BIEG * t1
    dEdT[n.s_erst] += -K_BIEG * cb
    dEdT[n.s_letzt] += -K_BIEG * st.ua
    dEdD += (dEdT - (dEdT * T).sum(-1, keepdims=True) * T) / Ls[..., None]
    dUw = st.wca * np.where(mw, (24.0 / dlc) * (-2.0 * srw * srw + srw), 0.0)
    gC = (dUw / np.maximum(rho, 1.0e-12))[..., None] * C
    gA = (1.0 - sst)[..., None] * gC - dEdD
    gB = sst[..., None] * gC + dEdD
    G = (n.IncA @ gA.reshape(n.S, -1) + n.IncB @ gB.reshape(n.S, -1)).reshape(n.nb, B, 3)
    dUo = np.where(mo, (24.0 / doc) * (-2.0 * sro * sro + sro), 0.0)
    G += (dUo * (-1.0 / np.maximum(r, 1.0e-12)))[..., None] * X
    if len(kp):
        dUf = st.wca * np.where(me, (24.0 / dd) * (-2.0 * sr * sr + sr), 0.0)
        g = (dUf / dd)[:, None] * Cd
        perlen = np.concatenate([n.seg_a[s1], n.seg_b[s1], n.seg_a[s2], n.seg_b[s2]])
        sysi = np.concatenate([kb, kb, kb, kb])
        werte = np.concatenate([(1.0 - s)[:, None] * g, s[:, None] * g,
                                -(1.0 - t)[:, None] * g, -t[:, None] * g])
        streu(G, perlen, sysi, werte)
    st.projiziere(G)
    return E, G, sonde


class Sonde:
    """Durchdringungsprobe je System (PLAN.md 4.2)."""

    def __init__(self, B):
        self.min_ff = np.full(B, np.inf)
        self.min_rand_ff = np.full(B, np.inf)
        self.min_rho = np.full(B, np.inf)
        self.min_rand_k = np.full(B, np.inf)
        self.max_r = np.zeros(B)
        self.max_schritt = np.zeros(B)
        self.schritte = 0

    def vor(self, so, dmax):
        de, dp, rh, rr = so
        self.min_ff = np.minimum(self.min_ff, de)
        self.min_rho = np.minimum(self.min_rho, rh)
        self.max_r = np.maximum(self.max_r, rr)
        self.min_rand_ff = np.minimum(self.min_rand_ff, dp - 2.0 * dmax)
        self.min_rand_k = np.minimum(self.min_rand_k, rh - dmax - A_KOERPER)
        self.max_schritt = np.maximum(self.max_schritt, dmax)
        self.schritte += 1

    def ok(self):
        return ((self.min_ff >= GRENZE_FF) & (self.min_rand_ff > 0.0) & (self.min_rho >= A_KOERPER)
                & (self.min_rand_k > 0.0) & (self.max_r <= R_AUSSEN))

    def als_dict(self, idx=None):
        sel = slice(None) if idx is None else idx
        return {
            "ok": self.ok()[sel].tolist(),
            "min_ff": self.min_ff[sel].tolist(),
            "min_rand_ff": self.min_rand_ff[sel].tolist(),
            "min_rho": self.min_rho[sel].tolist(),
            "min_rand_k": self.min_rand_k[sel].tolist(),
            "max_r": self.max_r[sel].tolist(),
            "max_schritt": self.max_schritt[sel].tolist(),
            "schritte": self.schritte,
        }


def fmax_von(F):
    return np.sqrt((F * F).sum(-1)).max(0)


def fire(st, X, nmax, ftol, sonde, dtmax=0.01, dtstart=0.002, cap=0.01):
    """FIRE je System (Bitzek u. a. 2006) mit Schrittbegrenzung; feste Perlen bleiben fest."""
    B = st.B
    cb = st.setze_fest(X)
    E, G, so = energie(st, X, cb)
    F = -G
    v = np.zeros_like(X)
    dt = np.full(B, dtstart)
    alpha = np.full(B, 0.1)
    npos = np.zeros(B, int)
    fmax = fmax_von(F)
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
        E, G, so = energie(st, X, cb)
        F = -G
        fmax = fmax_von(F)
    sonde.vor(so, np.zeros(B))
    return X, E, fmax, it, so


def langevin(st, X, nL, T0, rng, sonde, dt0, capl, rahmen_sel=None, nsave=25):
    """Ueberdaempftes Langevin-Abkuehlen T0 -> 0 (linear), Drift- und Schrittbegrenzung je Perle."""
    cb = st.setze_fest(X)
    E, G, so = energie(st, X, cb)
    rahmen = []
    for it in range(nL):
        T = T0 * (1.0 - it / nL)
        F = -G
        fmax = fmax_von(F)
        dt = np.minimum(dt0, capl / np.maximum(fmax, 1.0e-300))
        xi = rng.standard_normal(X.shape)
        st.projiziere(xi)
        dx = F * dt[None, :, None] + np.sqrt(2.0 * T * dt)[None, :, None] * xi
        dn = np.sqrt((dx * dx).sum(-1))
        fac = np.minimum(1.0, (2.0 * capl) / np.maximum(dn, 1.0e-300))
        dx *= fac[..., None]
        dmax = (dn * fac).max(0)
        sonde.vor(so, dmax)
        if rahmen_sel is not None and it % nsave == 0:
            rahmen.append(X[:, rahmen_sel].copy())
        X += dx
        E, G, so = energie(st, X, cb)
    return X, E, rahmen, so


def drehmoment(st, X):
    """M = dE/dtheta bei festgehaltenen freien Perlen (Haltemoment um die Drehachse), PLAN.md 3.2."""
    Xp = X.copy()
    cbp = st.setze_fest(Xp, st.theta + H_DREH)
    Ep = energie(st, Xp, cbp, grad=False)[0]
    Xm = X.copy()
    cbm = st.setze_fest(Xm, st.theta - H_DREH)
    Em = energie(st, Xm, cbm, grad=False)[0]
    return (Ep - Em) / (2.0 * H_DREH)


def windungen(st, X):
    """Windung W_i jedes Fadens um die Drehachse, vom Anker zum Ansatz (rechte Hand), (B,4)."""
    n = st.n
    nrm = st.achse
    ref = np.where(np.abs(nrm[:, 2:3]) < 0.9, np.array([[0.0, 0.0, 1.0]]), np.array([[1.0, 0.0, 0.0]]))
    e1 = np.cross(nrm, ref)
    e1 /= np.linalg.norm(e1, axis=1, keepdims=True)
    e2 = np.cross(nrm, e1)
    W = np.zeros((st.B, 4))
    for i in range(4):
        idx = [n.bead(i, k) for k in range(n.ns, -1, -1)]
        x = X[idx]
        phi = np.arctan2((x * e2[None]).sum(-1), (x * e1[None]).sum(-1))
        dphi = np.diff(phi, axis=0)
        dphi = (dphi + np.pi) % (2.0 * np.pi) - np.pi
        W[:, i] = dphi.sum(0) / (2.0 * np.pi)
    return W


def startzustand(st, seed):
    """Gerade, gestauchte Faeden mit kleiner Stoerung (knicken beim ersten Relaxieren aus)."""
    n = st.n
    rng = np.random.default_rng(seed)
    X = np.zeros((n.nb, st.B, 3))
    for i in range(4):
        for k in range(n.npf):
            f = k / n.ns
            X[n.bead(i, k)] = ((1.0 - f) * R_ATT + f * R_ANK) * st.ua[i]
    pert = 0.01 * rng.standard_normal(X.shape)
    st.projiziere(pert)
    X += pert
    st.setze_fest(X)
    return X


def reparam(pfad, M, frei):
    """Pfad (K,nb,3) auf M Bilder gleicher Bogenlaenge (freie Perlen) linear umverteilen."""
    d = pfad[1:, frei] - pfad[:-1, frei]
    seg = np.sqrt((d * d).sum((1, 2)))
    s = np.concatenate([[0.0], np.cumsum(seg)])
    ziel = np.linspace(0.0, s[-1], M)
    out = np.empty((M,) + pfad.shape[1:])
    j = np.searchsorted(s, ziel, side="right") - 1
    j = np.clip(j, 0, len(s) - 2)
    for m in range(M):
        jj = j[m]
        w = 0.0 if seg[jj] <= 0 else (ziel[m] - s[jj]) / seg[jj]
        w = min(max(w, 0.0), 1.0)
        out[m] = (1.0 - w) * pfad[jj] + w * pfad[jj + 1]
    out[0] = pfad[0]
    out[-1] = pfad[-1]
    return out


def schreibe_json(pfad, obj):
    tmp = pfad + ".neu"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, pfad)


def kopf(args):
    return {
        "karte": "GUERTEL-1 (Runde 41)",
        "modus": args.modus,
        "args": vars(args),
        "code_sha256": sha_datei(os.path.abspath(__file__)),
        "start_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "numpy": np.__version__,
        "konstanten": {"A_KOERPER": A_KOERPER, "SIG": SIG, "R_AUSSEN": R_AUSSEN, "K_DEHN": K_DEHN,
                       "K_BIEG": K_BIEG, "GRENZE_FF": GRENZE_FF, "SEGMENTE": {str(k): v for k, v in SEGMENTE.items()},
                       "ACHSE_G": ACHSE_G.tolist(), "GITTER": GITTER},
    }


# ---------------------------------------------------------------- Modi

def modus_protokoll(args):
    t0 = time.time()
    netz = Netz(args.lfak)
    st = Stapel(netz, [0, 1, 2], np.zeros(3))
    X = startzustand(st, 4100 + int(round(args.lfak * 10)))
    son_ges = Sonde(st.B)
    X, E, fmax, it, so = fire(st, X, args.nstart, args.ftol, son_ges)
    gitter = [g for g in GITTER if g <= args.tmax + 1e-9]
    schritte = int(round(args.tmax / args.dtheta))
    aus = {"kopf": kopf(args), "systeme": [s["name"] for s in SYSTEME], "gitter": [], "E": [], "M": [],
           "W": [], "fmax": [], "sonde_intervall": [], "fein_theta": [], "fein_E": [], "fein_M": [],
           "fein_fmax": []}
    Xg = []
    son_int = Sonde(st.B)
    for j in range(0, schritte + 1):
        th_deg = j * args.dtheta
        if j > 0:
            Xalt = X.copy()
            st.theta[:] = np.deg2rad(th_deg)
            st.setze_fest(X)
            sprung = np.sqrt(((X - Xalt) ** 2).sum(-1)).max(0)
            son_ges.vor(so, sprung)
            son_int.vor(so, sprung)
            X, E, fmax, it, so = fire(st, X, args.nrelax, args.ftol, son_int)
            son_ges.vor(so, np.zeros(st.B))
        Mf = drehmoment(st, X)
        aus["fein_theta"].append(th_deg)
        aus["fein_E"].append(E.tolist())
        aus["fein_M"].append(Mf.tolist())
        aus["fein_fmax"].append(fmax.tolist())
        if any(abs(th_deg - g) < 1e-9 for g in gitter):
            X, E, fmax, it, so = fire(st, X, args.ngitter, args.ftol, son_int)
            Mg = drehmoment(st, X)
            W = windungen(st, X)
            aus["gitter"].append(th_deg)
            aus["E"].append(E.tolist())
            aus["M"].append(Mg.tolist())
            aus["W"].append(W.tolist())
            aus["fmax"].append(fmax.tolist())
            for k in ("min_ff", "min_rand_ff", "min_rho", "min_rand_k", "max_r", "max_schritt"):
                getattr(son_ges, k)[:] = (np.minimum if k.startswith("min") else np.maximum)(
                    getattr(son_ges, k), getattr(son_int, k))
            aus["sonde_intervall"].append(son_int.als_dict())
            son_int = Sonde(st.B)
            Xg.append(X.copy())
    aus["sonde_gesamt"] = son_ges.als_dict()
    aus["laufzeit_s"] = time.time() - t0
    stamm = os.path.join(args.aus, "protokoll-L%.1f" % args.lfak)
    np.savez_compressed(stamm + ".npz", X=np.stack(Xg), gitter=np.array(aus["gitter"]))
    schreibe_json(stamm + ".json", aus)
    print("protokoll fertig L=%.1f laufzeit %.1f s" % (args.lfak, aus["laufzeit_s"]))


def modus_abkuehlen(args):
    t0 = time.time()
    netz = Netz(args.lfak)
    stamm_p = os.path.join(args.aus_protokoll, "protokoll-L%.1f" % args.lfak)
    prot = np.load(stamm_p + ".npz")
    gitter = [float(g) for g in prot["gitter"]]
    Xg = prot["X"]
    sysi = args.system
    winkel = [float(w) for w in args.winkel.split(",")] if args.winkel else gitter
    sysl, th, X0, wl, sl = [], [], [], [], []
    for w in winkel:
        g = gitter.index(w)
        for s in range(args.saaten):
            sysl.append(sysi)
            th.append(np.deg2rad(w))
            X0.append(Xg[g, :, sysi, :])
            wl.append(w)
            sl.append(s)
    st = Stapel(netz, sysl, th)
    X = np.ascontiguousarray(np.stack(X0, axis=1))
    cb = st.setze_fest(X)
    E0 = energie(st, X, cb, grad=False)[0]
    W0 = windungen(st, X)
    rng = np.random.default_rng([41, sysi, int(round(args.lfak * 10)), args.saat_basis])
    sel = np.array([b for b in range(st.B) if abs(wl[b] - args.rahmen_winkel) < 1e-9], int)
    son = Sonde(st.B)
    X, E, rahmen, so = langevin(st, X, args.nL, args.T0, rng, son, args.dt0, args.capl,
                                rahmen_sel=sel if len(sel) else None, nsave=args.nsave)
    t1 = time.time()
    X, E, fmax, it, so = fire(st, X, args.nF, args.ftol, son)
    Mf = drehmoment(st, X)
    W1 = windungen(st, X)
    aus = {"kopf": kopf(args), "system": SYSTEME[sysi]["name"], "winkel": wl, "saat": sl,
           "E_start": E0.tolist(), "E_end": E.tolist(), "M_end": Mf.tolist(), "W_start": W0.tolist(),
           "W_end": W1.tolist(), "fmax_end": fmax.tolist(), "fire_schritte": int(it),
           "sonde": son.als_dict(), "laufzeit_s": time.time() - t0, "laufzeit_langevin_s": t1 - t0,
           "rahmen_winkel": args.rahmen_winkel, "rahmen_sel": sel.tolist()}
    stamm = os.path.join(args.aus, "abkuehlen-L%.1f-s%d" % (args.lfak, sysi))
    np.savez_compressed(stamm + ".npz", X_end=X, X_start=np.stack(X0, axis=1),
                        rahmen=np.stack(rahmen) if rahmen else np.zeros(0), sel=sel)
    schreibe_json(stamm + ".json", aus)
    print("abkuehlen fertig L=%.1f system=%d B=%d laufzeit %.1f s" % (args.lfak, sysi, st.B, aus["laufzeit_s"]))


def string_pfad(netz, sysi, theta, pfad, M, niter, dts, cap, reparam_alle=5):
    st = Stapel(netz, [sysi] * M, np.full(M, theta))
    bilder = reparam(pfad, M, netz.frei)
    Xs = np.ascontiguousarray(bilder.transpose(1, 0, 2))
    cb = st.setze_fest(Xs)
    for it in range(niter):
        E, G, so = energie(st, Xs, cb)
        F = -G
        F[:, 0] = 0.0
        F[:, -1] = 0.0
        dx = F * dts
        dn = np.sqrt((dx * dx).sum(-1))
        dx *= np.minimum(1.0, cap / np.maximum(dn, 1.0e-300))[..., None]
        Xs += dx
        if it % reparam_alle == reparam_alle - 1:
            Xs = np.ascontiguousarray(reparam(Xs.transpose(1, 0, 2).copy(), M, netz.frei).transpose(1, 0, 2))
            st.setze_fest(Xs)
    E, G, so = energie(st, Xs, cb)
    W = windungen(st, Xs)
    img = Xs.transpose(1, 0, 2)
    delta = np.sqrt(((img[1:] - img[:-1]) ** 2).sum(-1)).max(1)
    de, dp, rh, rr = so
    rand_ff = np.minimum(dp[:-1], dp[1:]) - 2.0 * delta
    rand_k = np.minimum(rh[:-1], rh[1:]) - delta - A_KOERPER
    pruef = {
        "min_ff": float(de.min()), "min_rho": float(rh.min()), "max_r": float(rr.max()),
        "min_rand_ff_zwischen": float(rand_ff.min()), "min_rand_k_zwischen": float(rand_k.min()),
        "max_bildabstand": float(delta.max()),
    }
    pruef["ok"] = bool(pruef["min_ff"] >= GRENZE_FF and pruef["min_rho"] >= A_KOERPER and pruef["max_r"] <= R_AUSSEN
                       and pruef["min_rand_ff_zwischen"] > 0 and pruef["min_rand_k_zwischen"] > 0)
    fm = fmax_von(F)
    return E, W, pruef, fm


def modus_sperre(args):
    t0 = time.time()
    netz = Netz(args.lfak)
    sysi = args.system
    stamm_a = os.path.join(args.aus_abkuehlen, "abkuehlen-L%.1f-s%d" % (args.lfak, sysi))
    js = json.load(open(stamm_a + ".json"))
    ab = np.load(stamm_a + ".npz")
    sel = list(ab["sel"])
    aus = {"kopf": kopf(args), "system": SYSTEME[sysi]["name"], "kandidaten": []}
    kand = []
    for k, b in enumerate(sel):
        Wm = np.abs(np.array(js["W_end"][b])).mean()
        ok = js["sonde"]["ok"][b]
        aus["kandidaten"].append({"b": int(b), "saat": js["saat"][b], "W_end_mittel_abs": float(Wm),
                                  "sonde_ok": bool(ok), "E_end": js["E_end"][b]})
        if ok and Wm < 0.5:
            kand.append((js["E_end"][b], k, b))
    if not kand:
        aus["ergebnis"] = "keine_entwirrung"
        schreibe_json(os.path.join(args.aus, "sperre-L%.1f-s%d.json" % (args.lfak, sysi)), aus)
        print("sperre: keine entwirrte Saat bei 720 Grad")
        return
    kand.sort()
    _, k, b = kand[0]
    rahmen = ab["rahmen"]
    pfad = np.concatenate([ab["X_start"][:, b][None], rahmen[:, :, k], ab["X_end"][:, b][None]], axis=0)
    th = np.deg2rad(args.rahmen_winkel)
    E, W, pruef, fm = string_pfad(netz, sysi, th, pfad, args.bilder, args.niter, args.dts, args.cap)
    imax = int(np.argmax(E))
    aus.update({"ergebnis": "string", "b": int(b), "saat": js["saat"][b], "E_profil": E.tolist(),
                "W_profil": W.tolist(), "pruefung": pruef, "imax": imax, "S": float(E[imax] - E[0]),
                "E_anfang": float(E[0]), "E_ende": float(E[-1]), "fmax_bilder": fm.tolist(),
                "laufzeit_s": time.time() - t0})
    schreibe_json(os.path.join(args.aus, "sperre-L%.1f-s%d.json" % (args.lfak, sysi)), aus)
    print("sperre fertig L=%.1f system=%d laufzeit %.1f s" % (args.lfak, sysi, aus["laufzeit_s"]))


def modus_rauch(args):
    """Nur Laufzeit, Stabilitaet und Sonde; keine Energie- und Windungswerte in der Ausgabe."""
    t0 = time.time()
    bericht = {"kopf": kopf(args)}
    for lfak in (1.3, 1.8):
        netz = Netz(lfak)
        st = Stapel(netz, [0, 1, 2], np.zeros(3))
        X = startzustand(st, 4100 + int(round(lfak * 10)))
        son = Sonde(3)
        ta = time.time()
        X, E, fmax, it, so = fire(st, X, args.nstart, args.ftol, son)
        n_ev = it + 2
        ta2 = time.time()
        prot = {"start_fire_schritte": int(it), "start_fmax": fmax.tolist(), "zeit_start_s": ta2 - ta}
        schritte = int(round(args.tmax / args.dtheta))
        n_ev = 0
        tb = time.time()
        fm_list = []
        for j in range(1, schritte + 1):
            Xalt = X.copy()
            st.theta[:] = np.deg2rad(j * args.dtheta)
            st.setze_fest(X)
            sprung = np.sqrt(((X - Xalt) ** 2).sum(-1)).max(0)
            son.vor(so, sprung)
            X, E, fmax, it, so = fire(st, X, args.nrelax, args.ftol, son)
            n_ev += it + 2
            fm_list.append(fmax.tolist())
            _ = drehmoment(st, X)
        tb2 = time.time()
        prot.update({"drehschritte": schritte, "energie_auswertungen": n_ev, "zeit_dreh_s": tb2 - tb,
                     "s_je_auswertung_B3": (tb2 - tb) / max(n_ev, 1), "fmax_nach_schritt_max": np.max(fm_list, 0).tolist(),
                     "sonde": son.als_dict()})
        Xg = X.copy()
        # Abkuehl-Takt: B = 6 (je System 2 Saaten) kurz
        sysl = [0, 0, 1, 1, 2, 2]
        st6 = Stapel(netz, sysl, np.full(6, np.deg2rad(args.tmax)))
        X6 = np.ascontiguousarray(np.stack([Xg[:, s] for s in sysl], axis=1))
        rng = np.random.default_rng(99)
        son6 = Sonde(6)
        tc = time.time()
        X6, E6, rahmen, so6 = langevin(st6, X6, args.nL, args.T0, rng, son6, args.dt0, args.capl,
                                       rahmen_sel=np.array([0]), nsave=args.nsave)
        tc2 = time.time()
        X6, E6, fm6, it6, so6 = fire(st6, X6, args.nF, args.ftol, son6)
        tc3 = time.time()
        prot.update({"langevin_s_je_schritt_B6": (tc2 - tc) / args.nL,
                     "fire_schritte_B6": int(it6), "fire_s_B6": tc3 - tc2, "fmax_B6": fm6.tolist(),
                     "sonde_B6": son6.als_dict()})
        # Zeit je Auswertung bei B = 135
        Bg = 135
        stg = Stapel(netz, [0] * Bg, np.full(Bg, np.deg2rad(args.tmax)))
        Xb = np.ascontiguousarray(np.repeat(Xg[:, 0:1], Bg, axis=1))
        Xb += 0.003 * np.random.default_rng(5).standard_normal(Xb.shape)
        stg.projiziere(Xb)
        cbg = stg.setze_fest(Xb)
        td = time.time()
        for _ in range(20):
            energie(stg, Xb, cbg)
        prot["s_je_auswertung_B135"] = (time.time() - td) / 20
        # Stringmethode als Maschinenprobe (Pfad aus Langevin-Rahmen von System 0, Saat 0)
        pfad = np.concatenate([np.stack(rahmen)[:, :, 0], X6[:, 0][None]], axis=0)
        te = time.time()
        Es, Ws, pruef, fm = string_pfad(netz, 0, np.deg2rad(args.tmax), pfad, 21, 50, 1.0e-4, 0.005)
        prot["string_s_je_iteration_M21"] = (time.time() - te) / 50
        prot["string_pruefung"] = pruef
        bericht["L%.1f" % lfak] = prot
    bericht["laufzeit_s"] = time.time() - t0
    schreibe_json(os.path.join(args.aus, "rauch.json"), bericht)
    print("rauch fertig laufzeit %.1f s" % bericht["laufzeit_s"])


def modus_gegenprobe(args):
    """Gegenprobe der Sonde: Ausschluss Faden-Faden und Faden-Koerper aus; Ebene und zweizaehlige Achse.

    Erwartung (PLAN.md 4.4): die Sonde schlaegt an (Mittellinie im Koerper oder Kreuzungsrand <= 0),
    und die Windungen der Ebene gehen beim Abkuehlen verloren. Die Werte sind keine Ergebnisse der Karte.
    """
    t0 = time.time()
    netz = Netz(args.lfak)
    st = Stapel(netz, [2, 0], np.zeros(2))
    st.wca = 0.0
    X = startzustand(st, 4100 + int(round(args.lfak * 10)))
    son = Sonde(st.B)
    X, E, fmax, it, so = fire(st, X, args.nstart, args.ftol, son)
    schritte = int(round(args.tmax / args.dtheta))
    for j in range(1, schritte + 1):
        Xalt = X.copy()
        st.theta[:] = np.deg2rad(j * args.dtheta)
        st.setze_fest(X)
        sprung = np.sqrt(((X - Xalt) ** 2).sum(-1)).max(0)
        son.vor(so, sprung)
        X, E, fmax, it, so = fire(st, X, args.nrelax, args.ftol, son)
    W_vor = windungen(st, X)
    son_vor = son.als_dict()
    rng = np.random.default_rng(77)
    son2 = Sonde(st.B)
    X, E, rahmen, so = langevin(st, X, args.nL, args.T0, rng, son2, args.dt0, args.capl)
    X, E, fmax, it, so = fire(st, X, args.nF, args.ftol, son2)
    W_nach = windungen(st, X)
    aus = {"kopf": kopf(args), "systeme": ["ebene", "zweizaehlig"], "W_vor_abkuehlen": W_vor.tolist(),
           "W_nach_abkuehlen": W_nach.tolist(), "sonde_drehen": son_vor, "sonde_abkuehlen": son2.als_dict(),
           "laufzeit_s": time.time() - t0}
    schreibe_json(os.path.join(args.aus, "gegenprobe-L%.1f.json" % args.lfak), aus)
    print("gegenprobe fertig L=%.1f laufzeit %.1f s" % (args.lfak, aus["laufzeit_s"]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("modus", choices=["rauch", "protokoll", "abkuehlen", "sperre", "gegenprobe"])
    p.add_argument("--lfak", type=float, default=1.8)
    p.add_argument("--system", type=int, default=0)
    p.add_argument("--aus", default=".")
    p.add_argument("--aus_protokoll", default=".")
    p.add_argument("--aus_abkuehlen", default=".")
    p.add_argument("--dtheta", type=float, default=1.0)
    p.add_argument("--tmax", type=float, default=1440.0)
    p.add_argument("--nstart", type=int, default=5000)
    p.add_argument("--nrelax", type=int, default=80)
    p.add_argument("--ngitter", type=int, default=1500)
    p.add_argument("--ftol", type=float, default=1.0e-3)
    p.add_argument("--saaten", type=int, default=5)
    p.add_argument("--saat_basis", type=int, default=0)
    p.add_argument("--winkel", default="")
    p.add_argument("--nL", type=int, default=6000)
    p.add_argument("--nF", type=int, default=2500)
    p.add_argument("--T0", type=float, default=0.5)
    p.add_argument("--dt0", type=float, default=2.0e-4)
    p.add_argument("--capl", type=float, default=0.01)
    p.add_argument("--nsave", type=int, default=25)
    p.add_argument("--rahmen_winkel", type=float, default=720.0)
    p.add_argument("--bilder", type=int, default=61)
    p.add_argument("--niter", type=int, default=1500)
    p.add_argument("--dts", type=float, default=1.0e-4)
    p.add_argument("--cap", type=float, default=0.005)
    args = p.parse_args()
    os.makedirs(args.aus, exist_ok=True)
    {"rauch": modus_rauch, "protokoll": modus_protokoll, "abkuehlen": modus_abkuehlen,
     "sperre": modus_sperre, "gegenprobe": modus_gegenprobe}[args.modus](args)


if __name__ == "__main__":
    main()
