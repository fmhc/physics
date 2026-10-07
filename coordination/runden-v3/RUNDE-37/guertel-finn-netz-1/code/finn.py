#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUERTEL-FINN-NETZ-1 (Runde 43, RUNDE-37/guertel-finn-netz-1): Guertel-Trick auf Finns Tetraeder-Netz (Diamant).

Synthetische Modellrechnung, keine Messdaten. Modell, Ablauf und Regeln: PLAN.md.
Feld, FIRE, Protokoll und Stoss sind Kopien aus GUERTEL-2 (guertel2.py, sha256 c9374a98...) und GUERTEL-FELD-STAB-1
(stab.py, sha256 b7093e59...), auf einen allgemeinen Nachbargraphen umgestellt (Klasse Netz). Feldtyp (so3, so2) und
Raum sind getrennt; das Profil h ist auf beiden Netzen das harmonische 3D-Profil.

Modi:
  prot   Drehprotokoll auf --netz (diamant, z3) mit --feld (so3, so2), Schritt --fdtheta (10: P10, 30: P30) bis --tmax.
  wahl   Winkelwahl fuer Teil B aus den Diamant-SO(3)-Protokollen P10 (Plan) und P30 (Wortlaut).
  stoss  Zustand bei --theta bzw. Wahl-Index --wahl_k laden, stossen (eps; eps = 0: ohne Stoss), FIRE bis --nmax.
         Mit --ref 1 und --wahl_k: Referenzlauf beim Winkel refsumme - theta (eps = 0).
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
import guertel2 as g2  # noqa: E402  (GUERTEL-2, unveraendert)
import stab  # noqa: E402  (GUERTEL-FELD-STAB-1, unveraendert)

EZ = np.array([0.0, 0.0, 1.0])
EY = np.array([0.0, 1.0, 0.0])
KONJ = np.array([1.0, -1.0, -1.0, -1.0])
# Diamant in doppelten Koordinaten: A-Knoten 2p (p ganzzahlig, gerade Summe), B-Knoten 2p + (1, 1, 1).
D_A = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
START_UTC = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def kopf(args):
    return {"karte": "GUERTEL-FINN-NETZ-1 (Runde 43)", "modus": args.modus, "args": vars(args),
            "code_sha256": sha_datei(os.path.abspath(__file__)),
            "stab_code_sha256": sha_datei(os.path.abspath(stab.__file__)),
            "g2_code_sha256": sha_datei(os.path.abspath(g2.__file__)),
            "g1_code_sha256": sha_datei(os.path.abspath(g2.g1.__file__)),
            "start_utc": START_UTC, "schreibzeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "numpy": np.__version__}


def maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def diamant_knoten(R):
    """Diamant mit kubischer Zellkante a = 2 (Knotendichte 1 wie Z^3), Zentrum auf einem A-Knoten.
    Rueckgabe: doppelte ganzzahlige Koordinaten (Ort = ganz / 2), r, Bindungen (a: A-Knoten, b: B-Knoten)."""
    n = int(np.ceil(R)) + 2
    ax = np.arange(-n, n + 1)
    g = np.meshgrid(ax, ax, ax, indexing="ij")
    p = np.stack([gg.ravel() for gg in g], 1)
    p = p[(p.sum(1) % 2) == 0]
    alle = np.concatenate([2 * p, 2 * p + 1])
    r = np.sqrt((alle.astype(float) ** 2).sum(1)) / 2.0
    keep = r <= R + 1.0 + 1e-9
    alle, r = alle[keep], r[keep]
    N = len(alle)
    m = 2 * n + 2
    lut = -np.ones((2 * m + 1,) * 3, int)
    lut[tuple((alle + m).T)] = np.arange(N)
    iA = np.nonzero((alle[:, 0] % 2) == 0)[0]
    al, bl = [], []
    for d in D_A:
        nb = alle[iA] + d
        ok = (np.abs(nb) <= m).all(1)
        j = np.full(len(iA), -1)
        j[ok] = lut[tuple((nb[ok] + m).T)]
        k = j >= 0
        al.append(iA[k])
        bl.append(j[k])
    return alle, r, np.concatenate(al), np.concatenate(bl)


class Netz:
    """Feld auf einem allgemeinen Nachbargraphen. Methoden sind Kopien aus g2.Feld (dim 3 -> so3, dim 2 -> so2)."""

    def __init__(self, art, r0, R, feld="so3", chunk=8):
        self.art, self.feld, self.so3 = art, feld, feld == "so3"
        self.r0, self.R, self.chunk = float(r0), float(R), chunk
        self.z3_gleich_g2 = None
        if art == "z3":
            g = g2.Feld(3, r0, R, chunk=chunk)
            self.ganz = stab.gitterpunkte(3, R)
            self.pos = self.ganz.astype(float)
            r, self.a, self.b = g.r, g.a, g.b
        elif art == "diamant":
            self.ganz, r, self.a, self.b = diamant_knoten(R)
            self.pos = self.ganz / 2.0
        else:
            raise SystemExit("unbekanntes Netz")
        self.N = len(r)
        self.r = r
        self.nbond = len(self.a)
        self.kern = r <= self.r0 + 1e-9
        self.rand = r > self.R + 1e-9
        self.frei = ~self.kern & ~self.rand
        rc = np.maximum(r, self.r0)
        h = (1.0 / rc - 1.0 / self.R) / (1.0 / self.r0 - 1.0 / self.R)
        h = np.clip(h, 0.0, 1.0)
        h[self.kern] = 1.0
        h[self.rand] = 0.0
        self.h = h
        ones = np.ones(self.nbond)
        idx = np.arange(self.nbond)
        self.inc_a = sps.csr_matrix((ones, (self.a, idx)), shape=(self.N, self.nbond))
        self.inc_b = sps.csr_matrix((ones, (self.b, idx)), shape=(self.N, self.nbond))
        self.k = 4 if self.so3 else 1
        if art == "z3":
            self.z3_gleich_g2 = bool(np.array_equal(self.h, g.h) and np.array_equal(self.kern, g.kern)
                                     and np.array_equal(self.rand, g.rand) and np.array_equal(self.frei, g.frei)
                                     and len(self.pos) == g.N)

    def info(self):
        grad = np.bincount(np.concatenate([self.a, self.b]), minlength=self.N)
        bl = np.sqrt(((self.pos[self.a] - self.pos[self.b]) ** 2).sum(1))
        return {"art": self.art, "feld": self.feld, "N": int(self.N), "frei": int(self.frei.sum()),
                "kern": int(self.kern.sum()), "rand": int(self.rand.sum()), "bindungen": int(self.nbond),
                "grad_frei_min": int(grad[self.frei].min()), "grad_frei_max": int(grad[self.frei].max()),
                "bindungslaenge_min": float(bl.min()), "bindungslaenge_max": float(bl.max()),
                "innen_frei": int((self.frei & (self.h >= 0.5)).sum()), "z3_gleich_g2": self.z3_gleich_g2}

    def linien(self):
        """Knoten auf der +x- und der +z-Achse (radial nach aussen sortiert)."""
        out = {}
        for name, d in (("x", 0), ("z", 2)):
            andere = [k for k in range(3) if k != d]
            m = (self.ganz[:, andere[0]] == 0) & (self.ganz[:, andere[1]] == 0) & (self.ganz[:, d] >= 0)
            idx = np.nonzero(m)[0]
            out[name] = idx[np.argsort(self.ganz[idx, d])]
        return out

    # --- Energie, Gradient, Sonde (Kopie g2.Feld.energie) ---
    def energie(self, x, grad=True):
        """so3: E = sum 4(1-(q_a.q_b)^2); Sonde min q_a.q_b (> 0: kein Gittersprung).
        so2: E = sum 2(1-cos(phi_a-phi_b)); Sonde max |phi_a - phi_b| (< pi)."""
        B = x.shape[1]
        E = np.zeros(B)
        mon = np.zeros(B)
        G = np.zeros_like(x) if grad else None
        for s in range(0, B, self.chunk):
            xs = x[:, s:s + self.chunk]
            bb = xs.shape[1]
            xa = xs[self.a]
            xb = xs[self.b]
            if self.so3:
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
        return mon > 0.0 if self.so3 else mon < np.pi

    def laufend(self, alt, neu):
        return np.minimum(alt, neu) if self.so3 else np.maximum(alt, neu)

    def tang(self, G, x):
        if self.so3:
            G = G - (G * x).sum(-1, keepdims=True) * x
        G = G.copy()
        G[~self.frei] = 0.0
        return G

    def norm(self, x):
        if self.so3:
            return x / np.sqrt((x * x).sum(-1, keepdims=True))
        return x

    def setze(self, x, theta):
        if self.so3:
            x[self.kern] = g2.qachse(np.array([0.0, 0.0, 1.0]), np.array(theta))[None]
            x[self.rand] = np.array([1.0, 0.0, 0.0, 0.0])
        else:
            x[self.kern] = theta
            x[self.rand] = 0.0
        return x

    def null(self, B=1):
        x = np.zeros((self.N, B, self.k))
        if self.so3:
            x[..., 0] = 1.0
        return x

    def praediktor(self, x, dth):
        if self.so3:
            dq = g2.qachse(np.array([0.0, 0.0, 1.0]), dth * self.h)[:, None, :]
            y = g2.qmul(dq, x)
            x = np.where(self.frei[:, None, None], y, x)
        else:
            x = x + (dth * self.h * self.frei)[:, None, None]
        return x

    def rauschen(self, x, rng, sigma):
        if sigma <= 0:
            return x
        if self.so3:
            eta = rng.normal(0.0, sigma / np.sqrt(3.0), x.shape[:-1] + (3,))
            y = g2.qmul(g2.qexp(eta), x)
            x = np.where(self.frei[:, None, None], y, x)
        else:
            x = x + rng.normal(0.0, sigma, x.shape) * self.frei[:, None, None]
        return x


def fire_feld(netz, x, nmax, ftol, dtmax, dtstart=0.02, capw=0.05):
    """Wortgleiche Kopie von g2.fire_feld (ohne rec), laufende Sonde je Feldtyp."""
    B = x.shape[1]
    E, G, mon = netz.energie(x)
    F = -netz.tang(G, x)
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
        x = netz.norm(x + dx)
        v = netz.tang(v, x)
        E, G, mon = netz.energie(x)
        mon_lauf = netz.laufend(mon_lauf, mon)
        F = -netz.tang(G, x)
        fmax = np.sqrt((F * F).sum(-1)).max(0)
    return x, E, fmax, it, mon, mon_lauf


def kipp_amplitude(netz, x):
    """so3: P = Wurzel aus Summe q1^2 + q2^2 ueber freie Knoten (Kopie stab.kipp_amplitude). so2: 0 (keine Kippung)."""
    if not netz.so3:
        return 0.0
    q = x[netz.frei, 0]
    return float(np.sqrt((q[:, 1] ** 2 + q[:, 2] ** 2).sum()))


def struktur(netz, x, lin=None):
    q = x[:, 0]
    fr = netz.frei
    aussen = fr & (netz.h < 0.5)
    innen = fr & (netz.h >= 0.5)
    if netz.so3:
        s = {"qz_mittel_aussen": float(q[aussen, 3].mean()), "qz_mittel_innen": float(q[innen, 3].mean()),
             "q0_min_frei": float(q[fr, 0].min()), "kipp_amplitude": kipp_amplitude(netz, x)}
    else:
        s = {"phi_mittel_aussen": float(q[aussen, 0].mean()), "phi_mittel_innen": float(q[innen, 0].mean()),
             "phi_min_frei": float(q[fr, 0].min()), "phi_max_frei": float(q[fr, 0].max()), "kipp_amplitude": 0.0}
    if lin is not None:
        s["linie_x"] = q[lin["x"]]
        s["linie_z"] = q[lin["z"]]
    return s


def fire_log(netz, x, nmax, ftol, dtmax, dtstart=0.02, capw=0.05):
    """Wortgleiche Kopie von stab.fire_log (Aufzeichnung je Schritt: E, Sonde, fmax, Kipp-Amplitude)."""
    B = x.shape[1]
    E, G, mon = netz.energie(x)
    F = -netz.tang(G, x)
    v = np.zeros_like(x)
    dt = np.full(B, dtstart)
    alpha = np.full(B, 0.1)
    npos = np.zeros(B, int)
    fmax = np.sqrt((F * F).sum(-1)).max(0)
    mon_lauf = mon.copy()
    hE, hS, hF, hP = [float(E[0])], [float(mon[0])], [float(fmax[0])], [kipp_amplitude(netz, x)]
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
        x = netz.norm(x + dx)
        v = netz.tang(v, x)
        E, G, mon = netz.energie(x)
        mon_lauf = netz.laufend(mon_lauf, mon)
        F = -netz.tang(G, x)
        fmax = np.sqrt((F * F).sum(-1)).max(0)
        schritte += 1
        hE.append(float(E[0]))
        hS.append(float(mon[0]))
        hF.append(float(fmax[0]))
        hP.append(kipp_amplitude(netz, x))
    return x, E, fmax, schritte, mon, mon_lauf, {"E": hE, "sonde": hS, "fmax": hF, "kipp": hP}


def protokoll(netz, args, rng, speicher):
    """Kopie von stab.protokoll / g2.feld_protokoll (gleiche Arithmetik, gleiche Zufallsfolge), auf Netz umgestellt.
    Zusaetzlich: laufende Sonde je Winkel (nach allen Relaxationen des Winkels), Rasterwerte alle --raster Grad und
    Zustaende bei den Winkeln in speicher."""
    t0 = time.time()
    x = netz.setze(netz.null(1), 0.0)
    dth_deg = args.fdtheta
    nst = int(round(args.tmax / dth_deg))
    E_l, mon_l, th_l, ml_l = [], [], [], []
    gitter, Eg, mong, fmg, zust = [], [], [], [], {}
    ras = {"theta": [], "E": [], "sonde": [], "sonde_lauf": [], "struktur": []}
    x, E, fm, it, mon, ml = fire_feld(netz, x, args.fngitter, args.fftol, args.fdtmax)
    lauf = float(ml[0])
    for j in range(0, nst + 1):
        th = j * dth_deg
        if j > 0:
            x = netz.praediktor(x, np.deg2rad(dth_deg))
            x = netz.setze(x, np.deg2rad(th))
            x = netz.rauschen(x, rng, args.frausch)
            x, E, fm, it, mon, ml = fire_feld(netz, x, args.fnrelax, args.fftol, args.fdtmax)
            lauf = float(netz.laufend(lauf, float(ml[0])))
        E_l.append(float(E[0]))
        mon_l.append(float(mon[0]))
        th_l.append(th)
        if abs(th / args.fgitter - round(th / args.fgitter)) < 1e-9:
            x, E, fm, it, mon, ml = fire_feld(netz, x, args.fngitter, args.fftol, args.fdtmax)
            lauf = float(netz.laufend(lauf, float(ml[0])))
            gitter.append(th)
            Eg.append(float(E[0]))
            mong.append(float(mon[0]))
            fmg.append(float(fm[0]))
        ml_l.append(lauf)
        if abs(th / args.raster - round(th / args.raster)) < 1e-9:
            ras["theta"].append(th)
            ras["E"].append(float(E[0]))
            ras["sonde"].append(float(mon[0]))
            ras["sonde_lauf"].append(lauf)
            ras["struktur"].append(struktur(netz, x))
        if any(abs(th - s) < 1e-9 for s in speicher):
            zust["%d" % int(round(th))] = x[:, 0].copy()
    return {"theta_schritt": th_l, "E_schritt": E_l, "sonde_schritt": mon_l, "sonde_lauf_schritt": ml_l,
            "gitter": gitter, "E_gitter": Eg, "sonde_gitter": mong, "fmax_gitter": fmg, "raster": ras,
            "laufzeit_s": time.time() - t0}, zust


# --- Regeln fuer theta_max und Gueltigkeit (PLAN Abschnitt 3 und 5); auch von auswertung_fn.py benutzt ---

def ist_sprung(feld, s):
    if s is None:
        return True
    return (not (s > 0.0)) if feld == "so3" else (not (s < np.pi))


def theta_max(prj):
    """Kleinster Rasterwinkel mit laufender Sonde im Sprungbereich; None = kein Sprung bis tmax."""
    feld = prj["kopf"]["args"]["feld"]
    ras = prj["protokoll"]["raster"]
    for t, s in zip(ras["theta"], ras["sonde_lauf"]):
        if ist_sprung(feld, s):
            return float(t)
    return None


def theta_sprung_fein(prj):
    """Erster Protokollwinkel (Schrittweite des Protokolls) mit laufender Sonde im Sprungbereich; None = keiner."""
    feld = prj["kopf"]["args"]["feld"]
    pr = prj["protokoll"]
    for t, s in zip(pr["theta_schritt"], pr["sonde_lauf_schritt"]):
        if ist_sprung(feld, s):
            return float(t)
    return None


def sinn_aussen(feld, st):
    return st["qz_mittel_aussen"] if feld == "so3" else st["phi_mittel_aussen"]


def gueltig_plan(prj, theta):
    """Vorwaertsast gueltig bis theta: an allen Rasterwinkeln <= theta kein Sprung und, fuer Rasterwinkel > 0,
    Drehsinn aussen > 0 (bei 0 Grad gibt es keine Verdrillung; Befund des Rauchlaufs)."""
    feld = prj["kopf"]["args"]["feld"]
    ras = prj["protokoll"]["raster"]
    if not any(abs(t - theta) < 1e-9 for t in ras["theta"]):
        return False
    for t, s, st in zip(ras["theta"], ras["sonde_lauf"], ras["struktur"]):
        if t <= theta + 1e-9 and (ist_sprung(feld, s) or (t > 0.0 and not (sinn_aussen(feld, st) > 0.0))):
            return False
    return True


def gueltig_wort(prj, theta):
    """Nur Sonde: an allen Rasterwinkeln <= theta kein Sprung."""
    feld = prj["kopf"]["args"]["feld"]
    ras = prj["protokoll"]["raster"]
    if not any(abs(t - theta) < 1e-9 for t in ras["theta"]):
        return False
    for t, s in zip(ras["theta"], ras["sonde_lauf"]):
        if t <= theta + 1e-9 and ist_sprung(feld, s):
            return False
    return True


def wahl_regel(prj, art, grenze, unten, ziel):
    ok = (lambda t: gueltig_plan(prj, t)) if art == "plan" else (lambda t: gueltig_wort(prj, t))
    tm = theta_max(prj)
    if (tm is None or tm > grenze) and ok(grenze):
        return [float(z) for z in ziel]
    kand = [float(t) for t in prj["protokoll"]["raster"]["theta"] if unten < t <= grenze and ok(t)]
    return [max(kand)] if kand else []


def lade_json(p):
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)


# --- Stoss ---

def kipp(netz, x, theta_rad, eps):
    """so3: wortgleich stab.kipp (Drillachse der inneren Haelfte um delta = eps sin(pi f_i) kippen).
    so2: einzig moeglicher Stoss phi -> phi + delta (keine Kipprichtung)."""
    fi = np.clip(2.0 * netz.h - 1.0, 0.0, 1.0)
    delta = eps * np.sin(np.pi * fi)
    delta[~netz.frei] = 0.0
    if netz.so3:
        qs = g2.qachse(EZ, np.array(theta_rad / 2.0))
        qy = g2.qachse(EY, delta)
        qsb = np.broadcast_to(qs, qy.shape)
        A = g2.qmul(g2.qmul(qsb, qy), qsb * KONJ)
        y = g2.qmul(g2.qmul(A[:, None, :], x), (qy * KONJ)[:, None, :])
        y = netz.norm(y)
        x = np.where(netz.frei[:, None, None], y, x)
    else:
        x = x + delta[:, None, None]
    return netz.setze(x, theta_rad), delta


def saat_fuer(args):
    s = [42, 3 if args.feld == "so3" else 2, int(round(args.r0 * 10)), int(round(args.R))]
    if args.netz == "diamant":
        s.append(4)
    return s


def modus_prot(args):
    t0 = time.time()
    netz = Netz(args.netz, args.r0, args.R, args.feld, chunk=args.fchunk)
    saat = saat_fuer(args)
    rng = np.random.default_rng(saat)
    speicher = [float(s) for s in args.speicher.split(",")] if args.speicher else []
    pr, zust = protokoll(netz, args, rng, speicher)
    tag = "prot-%s-%s-d%d" % (args.netz, args.feld, int(round(args.fdtheta)))
    aus = {"kopf": kopf(args), "saat": saat, "netz_info": netz.info(), "protokoll": pr,
           "laufzeit_s": time.time() - t0, "maxrss_mb": maxrss_mb()}
    tm = theta_max(aus)
    aus["theta_max_raster"] = tm
    aus["theta_sprung_fein"] = theta_sprung_fein(aus)
    if zust:
        np.savez_compressed(os.path.join(args.aus, tag + "-zust.npz"), **zust)
    g2.schreibe_json(os.path.join(args.aus, tag + ".json"), aus)
    print("prot fertig %s laufzeit %.1f s" % (tag, aus["laufzeit_s"]))


def modus_wahl(args):
    p10 = lade_json(os.path.join(args.lauf, "prot-diamant-so3-d10.json"))
    p30 = lade_json(os.path.join(args.lauf, "prot-diamant-so3-d30.json"))
    ziel = [float(z) for z in args.ziel.split(",")]
    plan = wahl_regel(p10, "plan", args.grenze, args.unten, ziel) if p10 is not None else []
    wort = wahl_regel(p30, "wort", args.grenze, args.unten, ziel) if p30 is not None else []
    alle = sorted(set(plan) | set(wort))
    aus = {"kopf": kopf(args), "plan": plan, "wort": wort, "alle": alle,
           "refs": {"%d" % int(round(t)): args.refsumme - t for t in alle},
           "p10_da": p10 is not None, "p30_da": p30 is not None}
    g2.schreibe_json(os.path.join(args.aus, "wahl.json"), aus)
    print("wahl fertig: %d Winkel" % len(alle))


def modus_stoss(args):
    t0 = time.time()
    theta = args.theta
    if args.wahl_k >= 0:
        w = lade_json(args.wahl)
        if w is None or args.wahl_k >= len(w["alle"]):
            print("keine Aufgabe fuer wahl_k = %d" % args.wahl_k)
            return
        theta = w["alle"][args.wahl_k]
        if args.ref:
            theta = w["refs"]["%d" % int(round(theta))]
    if args.ref and args.eps != 0.0:
        raise SystemExit("Referenz nur mit eps = 0")
    netz = Netz(args.netz, args.r0, args.R, args.feld, chunk=args.fchunk)
    d = np.load(args.zust)
    q0 = d["%d" % int(round(theta))]
    th = np.deg2rad(float(theta))
    lin = netz.linien()
    x = q0[:, None, :].copy()
    E_vor, _, mon_vor = netz.energie(x, grad=False)
    s_vor = struktur(netz, x, lin)
    if args.eps > 0.0:
        x, delta = kipp(netz, x, th, args.eps)
    else:
        x = netz.setze(x, th)
        delta = np.zeros(netz.N)
    E_nach, _, mon_nach = netz.energie(x, grad=False)
    s_nach = struktur(netz, x, lin)
    x, E, fm, schritte, mon, mon_l, hist = fire_log(netz, x, args.nmax, args.fftol, args.fdtmax)
    s_end = struktur(netz, x, lin)
    aus = {"kopf": kopf(args), "netz": args.netz, "feld": args.feld, "theta": float(theta), "eps": float(args.eps),
           "ref": int(args.ref), "kipp_delta_max": float(np.abs(delta).max()),
           "kipp_plaetze": int((np.abs(delta) > 0).sum()),
           "E_vor": float(E_vor[0]), "sonde_vor": float(mon_vor[0]), "struktur_vor": s_vor,
           "E_nach_stoss": float(E_nach[0]), "sonde_nach_stoss": float(mon_nach[0]), "struktur_nach_stoss": s_nach,
           "E_end": float(E[0]), "sonde_end": float(mon[0]), "sonde_lauf": float(mon_l[0]),
           "fmax_end": float(fm[0]), "schritte": int(schritte), "struktur_end": s_end, "verlauf": hist,
           "laufzeit_s": time.time() - t0, "maxrss_mb": maxrss_mb()}
    tag = "stoss-%s-%s-T%d-e%g" % (args.netz, args.feld, int(round(theta)), args.eps)
    np.savez_compressed(os.path.join(args.aus, tag + "-end.npz"), q=x[:, 0])
    g2.schreibe_json(os.path.join(args.aus, tag + ".json"), aus)
    print("stoss fertig %s schritte %d laufzeit %.1f s" % (tag, schritte, aus["laufzeit_s"]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("modus", choices=["prot", "wahl", "stoss"])
    p.add_argument("--aus", default=".")
    p.add_argument("--netz", default="diamant", choices=["diamant", "z3"])
    p.add_argument("--feld", default="so3", choices=["so3", "so2"])
    p.add_argument("--r0", type=float, default=12.0)
    p.add_argument("--R", type=float, default=24.0)
    p.add_argument("--tmax", type=float, default=720.0)
    p.add_argument("--raster", type=float, default=30.0)
    p.add_argument("--speicher", default="270,300,330,360,390,420,450")
    p.add_argument("--fdtheta", type=float, default=10.0)
    p.add_argument("--fgitter", type=float, default=90.0)
    p.add_argument("--fnrelax", type=int, default=30)
    p.add_argument("--fngitter", type=int, default=150)
    p.add_argument("--fftol", type=float, default=1.0e-5)
    p.add_argument("--fdtmax", type=float, default=0.1)
    p.add_argument("--frausch", type=float, default=1.0e-3)
    p.add_argument("--fchunk", type=int, default=8)
    p.add_argument("--lauf", default=".")
    p.add_argument("--ziel", default="420,450")
    p.add_argument("--grenze", type=float, default=450.0)
    p.add_argument("--unten", type=float, default=360.0)
    p.add_argument("--refsumme", type=float, default=720.0)
    p.add_argument("--zust", default="prot-diamant-so3-d10-zust.npz")
    p.add_argument("--wahl", default="wahl.json")
    p.add_argument("--wahl_k", type=int, default=-1)
    p.add_argument("--ref", type=int, default=0)
    p.add_argument("--theta", type=float, default=450.0)
    p.add_argument("--eps", type=float, default=0.0)
    p.add_argument("--nmax", type=int, default=3000)
    args = p.parse_args()
    os.makedirs(args.aus, exist_ok=True)
    {"prot": modus_prot, "wahl": modus_wahl, "stoss": modus_stoss}[args.modus](args)


if __name__ == "__main__":
    main()
