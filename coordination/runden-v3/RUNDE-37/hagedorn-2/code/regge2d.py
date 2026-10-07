#!/usr/bin/env python3
"""RUNDE-06, Karte RG-1: Bilden drehende Q-Baelle einen Regge-Turm? 2D, radiales Schiessen, numpy float64, CPU.

Plan, Herleitung, Vorhersagen und Aufrufe: PLAN.md daneben. Explorativ (v3), keine formale Bestaetigung.

Modell (wie tests2d_r3.py und r5_2d_a.py): L = |phi_t|^2 - |grad phi|^2 - U(S), S = |phi|^2, U(S) = S - S^2 + S^3/2.
Ansatz phi = f(r) exp(i m theta - i omega t), a = 1 - omega^2:
    f'' + f'/r - m^2 f/r^2 = a f - 2 f^3 + (3/2) f^5
    Q = 2 omega Int f^2 d^2x,  E = Int [omega^2 f^2 + f'^2 + m^2 f^2/r^2 + U(f^2)] d^2x,  J = m Q.
NLS-Grenze omega -> 1 (Zeilen "nls"): f = sqrt(a) g(sqrt(a) r) mit g'' + g'/rho - m^2 g/rho^2 = g - 2 g^3.
    Dort Q -> 2 N_T(m) und E/Q -> 1 (N_T = Int g^2 d^2rho). N_T(0) = 5,8505 (halbe Townes-Norm 11,701).

Schiessen: berichtigte Coleman-Regel aus RUNDE-05/r5-2d-a/r5_2d_a.py (PLAN.md dort, Abschnitt 0.2), fuer alle m gleich:
    Ueberschuss: f > f_top (ueber die Kuppe) oder f < 0 (durch null) oder nicht endlich.
    Unterschuss: f' > 0 unterhalb der Talsohle f_tal, nachdem die Bahn gefallen ist (m = 0 von Anfang an, m >= 1 nach
    dem ersten Maximum).
    m = 0: p = f(0) linear eingeschachtelt (1e-3 bis f_top). m >= 1: ln p eingeschachtelt, p = f^(m)(0)/m!.
Abweichungen von r5_2d_a.py (vor dem Lauf festgelegt, PLAN.md Abschnitt 2):
    1. numpy statt torch, CPU, ein Kern. Einschachtelung mit 15 Kandidaten je Zeile und Runde, bis die Klammer 8 ulp
       breit ist (statt 5 Runden x 2048 Kandidaten). Kandidaten ausserhalb der laufenden Klammer werden nicht weiter
       gerechnet.
    2. ln-p-Klammer -150 bis 5 statt ln(1e-6) bis ln(10): bei m = 8 und omega^2 = 0,99 ist p etwa 1e-19.
    3. Schrittweite je Zeile h = h0 * min(3, max(1, 0,3/sqrt(a))): im dickwandigen Bereich ist die Laengenskala
       1/sqrt(a) bis 10. Fuer omega^2 <= 0,9 und die NLS-Zeilen gilt h = h0 (wie R3/R5 bei h0 = 0,01).
    4. Start bei r0 = n0 h mit n0 = 1 (m = 0, wie R3/R5) bzw. n0 = 2m (m >= 1) aus der Reihe
       f = p r^m (1 + a r^2/(4(m+1))); vermeidet RK4-Schritte mit h m/r > 1/2 nahe r = 0.
    5. Schiessbereich je Zeile bis r_cap = n0 h + 60 + 30/kappa + 6 m/kappa (kappa = sqrt(a)) statt fest 60.
    6. Schwanz ab f < 1e-3 f_max (im Abfall, wie R3/R5) aus der linearen Gleichung f'' + f'/r - m^2 f/r^2 = a f,
       rueckwaerts gerechnet (exakt K_m(kappa r) bis auf RK4), statt der Naeherung erster Ordnung.
    7. Integrale mit der Simpsonregel (R3/R5: Riemann-Summe, Fehler O(h^2) bei r = 0 fuer m = 0).
Codeprobe J = m Q: Feld auf ein kartesisches Gitter legen, spektrale Ableitungen, J = Int (x p_y - y p_x) direkt,
dazu Q, E und das Residuum der 2D-Feldgleichung (kennt kein m^2/r^2).

Aufruf:
    python3 regge2d.py tabelle [--h 0.01] [--out ORDNER] [--m 0,1,...] [--w2 0.52,...] [--ohne-nls] [--ohne-gitter]
    python3 regge2d.py bahn --tabelle ORDNER/ergebnis.json [--l3 ORDNER2/ergebnis.json] [--out ORDNER3]
    python3 regge2d.py rauch [--out ORDNER] [--ohne-zeitprobe]
Ausgaben je Aufruf: bericht.txt und ergebnis.json im --out-Ordner.
"""
import os

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import datetime
import json
import math
import platform
import sys
import time

import numpy as np

EPS = float(np.finfo(np.float64).eps)
ZWEIPI = 2.0 * math.pi

# ---- Tabelle (vor dem Lauf festgelegt, PLAN.md Abschnitt 2) ----
M_STANDARD = tuple(range(9))
W2_STANDARD = (0.52, 0.55, 0.575, 0.60, 0.625, 0.65, 0.675, 0.70, 0.725, 0.75, 0.775, 0.80, 0.825, 0.85, 0.875,
               0.90, 0.92, 0.94, 0.95, 0.96, 0.97, 0.975, 0.98, 0.985, 0.99)
H_STANDARD = 0.01
K_KAND = 15                 # Kandidaten je Zeile und Runde
RUNDEN_MAX = 40
LNP_LO, LNP_HI = -150.0, 5.0
P0_LO, P0_HI_NLS = 1e-3, 4.0
SCHNITT = 1e-3              # Schwanz ab f < SCHNITT * f_max im Abfall
SCHWANZ_LAENGE = 30.0       # Schwanz bis r_cut + 30/kappa
KOMPAKT = 64                # alle 64 Schritte: entschiedene und ausgeklammerte Kandidaten entfernen
RAUSCH_REL = 1e-9           # Vertauschung Unter/Ueber bis 1e-9 (relativ) = Rauschboden, darueber "nicht monoton"
VIRIAL_MAX = 1e-5           # Zeilen mit |Virialrest| darueber gehen nicht in die Fits

# ---- Codeprobe auf dem Gitter ----
GITTER_ZEILEN = tuple((m, 0.80) for m in range(9)) + ((1, 0.55), (4, 0.55), (8, 0.55), (1, 0.95), (4, 0.95),
                                                      (8, 0.95))
GITTER_N_MAX = 1024
GITTER_PUNKTE_JE_SKALA = 10.0

# ---- Auswertung (vor dem Lauf festgelegt, PLAN.md Abschnitte 4 und 5) ----
M_FIT = (3, 4, 5, 6, 7, 8)
W2_RING = (0.55, 0.70, 0.80, 0.90, 0.95, 0.99)
Q_ROTOR = (300.0, 1000.0)
ALPHA_H, ALPHA_TOL = 2.0, 0.1       # H getragen: |alpha - 2| <= 0,1
ALPHA_GEGEN = 1.6                    # Gegenhypothese getragen: alpha <= 1,6 (beta >= 1,67)
BETA_TOL = 0.1                       # Ring-Mechanismus: |beta - 1| <= 0,1
L3_TOL_FIT, L3_TOL_REL = 0.01, 1e-5  # L3: |d alpha|, |d beta| <= 0,01; |dQ/Q|, |dE/E| <= 1e-5 in den Fitzeilen
GITTER_TOL_J, GITTER_TOL_Q, GITTER_TOL_E = 1e-4, 1e-4, 1e-4

# RUNDE-03/tests2d-r3/lauf-69/ausgabe/profile_bericht.txt, nur m = 0 (die m = 1-Zeilen dort sind falsch)
R3_M0 = {0.52: dict(p=1.009669999580558, Q=1421.4529, E=1045.9545, S_max=1.019434, R_halb=17.497),
         0.55: dict(p=1.022994303264939, Q=238.4322, E=185.8629, S_max=1.046517, R_halb=6.880),
         0.60: dict(p=1.030139156258561, Q=66.6160, E=56.5272, S_max=1.061187, R_halb=3.358),
         0.70: dict(p=0.921968444982739, Q=23.9958, E=22.6258, S_max=0.850026, R_halb=1.916),
         0.80: dict(p=0.736248149041047, Q=16.2315, E=15.9460, S_max=0.542061, R_halb=1.788)}
R3_TOL = dict(p=1e-9, Q=1e-4, E=1e-4, S_max=1e-5, R_halb=2e-3)   # p, S_max, R_halb absolut; Q, E relativ

# ---- Rauchtest ----
RAUCH_M = (0, 1, 3, 8)
RAUCH_W2 = (0.52, 0.80, 0.99)
RAUCH_H = (0.02, 0.01)
RAUCH_GITTER = ((0, 0.80), (3, 0.80))


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def upot(s):
    return s - s * s + 0.5 * s ** 3


def upot_ab(s):
    return 1.0 - 2.0 * s + 1.5 * s * s


def w2_schluessel(w2):
    return None if w2 is None else round(float(w2), 6)


# ---------------------------------------------------------------- Zeilen und Parameter

def zeilen_bauen(m_liste, w2_liste, nls):
    zeilen = [dict(m=int(m), w2=float(w2), nls=False) for w2 in w2_liste for m in m_liste]
    if nls:
        zeilen += [dict(m=int(m), w2=None, nls=True) for m in m_liste]
    return zeilen


def kuppe_tal(a, c5):
    """f_top (Kuppe von Phi = (omega^2 S - U)/2; ohne Quintik unendlich) und f_tal (Talsohle)."""
    wurzel = np.sqrt(np.maximum(4.0 - 6.0 * a * c5, 0.0))
    c5s = np.where(c5 > 0.0, c5, 1.0)
    s_top = np.where(c5 > 0.0, (2.0 + wurzel) / (3.0 * c5s), np.inf)
    s_tal = np.where(c5 > 0.0, (2.0 - wurzel) / (3.0 * c5s), 0.5 * a)
    return np.sqrt(s_top), np.sqrt(s_tal)


def parameter(zeilen, h0):
    """Arrays je Zeile: a, c5, m, h, n0, f_top, f_tal, r_cap, Klammer."""
    n = len(zeilen)
    nls = np.array([z["nls"] for z in zeilen])
    m = np.array([float(z["m"]) for z in zeilen])
    a = np.array([1.0 if z["nls"] else 1.0 - z["w2"] for z in zeilen])
    c5 = np.where(nls, 0.0, 1.0)
    kappa = np.sqrt(a)
    h = h0 * np.where(nls, 1.0, np.clip(0.3 / kappa, 1.0, 3.0))
    n0 = np.where(m == 0.0, 1, np.maximum(1, 2 * m.astype(int)))
    ftop, ftal = kuppe_tal(a, c5)
    logp = m > 0.0
    lo = np.where(logp, LNP_LO, P0_LO)
    hi = np.where(logp, LNP_HI, np.where(np.isfinite(ftop), ftop, P0_HI_NLS))
    rcap = n0 * h + 60.0 + 30.0 / kappa + 6.0 * m / kappa
    return dict(n=n, nls=nls, m=m, a=a, c5=c5, kappa=kappa, h=h, n0=n0, ftop=ftop, ftal=ftal, logp=logp,
                lo0=lo, hi0=hi, rcap=rcap)


def reihe(p, a, c5, m, r):
    """f, f' aus der Reihe um r = 0. m = 0: f = p + g r^2/4, g = (U'(p^2) - omega^2) p (wie R3/R5).
    m >= 1: f = p r^m (1 + a r^2/(4(m+1)))."""
    p, a, c5, m, r = np.broadcast_arrays(*(np.asarray(v, dtype=float) for v in (p, a, c5, m, r)))
    s = p * p
    g = (a - 2.0 * s + 1.5 * c5 * s * s) * p
    m1 = np.maximum(m, 1.0)
    k2 = a / (4.0 * (m1 + 1.0))
    rs = np.where(r > 0.0, r, 1.0)
    rm = rs ** m1
    f = np.where(m == 0.0, p + 0.25 * g * r * r, np.where(r > 0.0, p * rm * (1.0 + k2 * r * r), 0.0))
    fp_pos = p * (rm / rs) * (m1 + (m1 + 2.0) * k2 * r * r)
    fp = np.where(m == 0.0, 0.5 * g * r, np.where(r > 0.0, fp_pos, np.where(m == 1.0, p, 0.0)))
    return f, fp


def rk4_schritt(r, h, f, fp, a, q5, m2):
    """Ein RK4-Schritt fuer f'' = ((1,5 c5 f^2 - 2) f^2 + a) f - f'/r + m^2 f/r^2 (q5 = 1,5 c5)."""
    hh = 0.5 * h
    i0 = 1.0 / r
    i1 = 1.0 / (r + hh)
    i2 = 1.0 / (r + h)
    c0 = m2 * i0 * i0
    c1 = m2 * i1 * i1
    c2 = m2 * i2 * i2
    s = f * f
    k1 = ((q5 * s - 2.0) * s + a + c0) * f - fp * i0
    f2 = f + hh * fp
    p2 = fp + hh * k1
    s = f2 * f2
    k2 = ((q5 * s - 2.0) * s + a + c1) * f2 - p2 * i1
    f3 = f + hh * p2
    p3 = fp + hh * k2
    s = f3 * f3
    k3 = ((q5 * s - 2.0) * s + a + c1) * f3 - p3 * i1
    f4 = f + h * p3
    p4 = fp + h * k3
    s = f4 * f4
    k4 = ((q5 * s - 2.0) * s + a + c2) * f4 - p4 * i2
    h6 = h / 6.0
    return f + h6 * (fp + 2.0 * (p2 + p3) + p4), fp + h6 * (k1 + 2.0 * (k2 + k3) + k4)


def rk4_linear(r, h, f, fp, a, m2):
    """RK4 fuer die lineare Schwanzgleichung f'' = (a + m^2/r^2) f - f'/r (Loesung K_m(sqrt(a) r))."""
    hh = 0.5 * h
    i0 = 1.0 / r
    i1 = 1.0 / (r + hh)
    i2 = 1.0 / (r + h)
    c0 = a + m2 * i0 * i0
    c1 = a + m2 * i1 * i1
    c2 = a + m2 * i2 * i2
    k1 = c0 * f - fp * i0
    f2 = f + hh * fp
    p2 = fp + hh * k1
    k2 = c1 * f2 - p2 * i1
    f3 = f + hh * p2
    p3 = fp + hh * k2
    k3 = c1 * f3 - p3 * i1
    f4 = f + h * p3
    p4 = fp + h * k3
    k4 = c2 * f4 - p4 * i2
    h6 = h / 6.0
    return f + h6 * (fp + 2.0 * (p2 + p3) + p4), fp + h6 * (k1 + 2.0 * (k2 + k3) + k4)


# ---------------------------------------------------------------- Schiessen

def kandidaten_entscheiden(zi, par, P, lo, hi):
    """Alle Kandidaten zugleich integrieren; +1 Ueberschuss, -1 Unterschuss, 0 offen (bis r_cap oder ausgeklammert)."""
    n_k = par.size
    zust = np.zeros(n_k)
    p = np.where(P["logp"][zi], np.exp(np.minimum(par, 700.0)), par)
    a = P["a"][zi]
    c5 = P["c5"][zi]
    q5 = 1.5 * c5
    mm = P["m"][zi]
    m2 = mm * mm
    h = P["h"][zi]
    ft = P["ftop"][zi]
    fl = P["ftal"][zi]
    rcap = P["rcap"][zi]
    r = P["n0"][zi] * h
    f, fp = reihe(p, a, c5, mm, r)
    gef = mm == 0.0
    idx = np.arange(n_k)
    schritte = 0
    while idx.size:
        f, fp = rk4_schritt(r, h, f, fp, a, q5, m2)
        r = r + h
        schritte += 1
        ueber = ~(f <= ft) | (f < 0.0)
        unter = gef & (fp > 0.0) & (f < fl) & ~ueber
        gef = gef | (fp < 0.0)
        ent = ueber | unter
        if ent.any():
            zust[idx[ueber]] = 1.0
            zust[idx[unter]] = -1.0
            f = np.where(ent, 0.0, f)
            fp = np.where(ent, 0.0, fp)
        if schritte % KOMPAKT == 0:
            u = zust < 0.0
            o = zust > 0.0
            lo_z = lo.copy()
            hi_z = hi.copy()
            np.maximum.at(lo_z, zi[u], par[u])
            np.minimum.at(hi_z, zi[o], par[o])
            zz = zi[idx]
            pp = par[idx]
            bleibt = (zust[idx] == 0.0) & (r < rcap) & (pp > lo_z[zz]) & (pp < hi_z[zz])
            if not bleibt.all():
                idx, f, fp, r, h, a, q5, m2, ft, fl, rcap, gef = (v[bleibt] for v in
                                                                   (idx, f, fp, r, h, a, q5, m2, ft, fl, rcap, gef))
    return zust, schritte


def schiessen(P, log):
    n = P["n"]
    lo = P["lo0"].copy()
    hi = P["hi0"].copy()
    fertig = np.zeros(n, bool)
    still = np.zeros(n, int)
    nichtmonoton = np.zeros(n, bool)
    runden = np.zeros(n, int)
    geschlossen = np.zeros(n, bool)
    rauschboden = np.zeros(n)
    frac = np.arange(1, K_KAND + 1) / (K_KAND + 1.0)
    schritte_ges = 0
    for runde in range(RUNDEN_MAX):
        aktiv = np.nonzero(~fertig)[0]
        if aktiv.size == 0:
            break
        zi = np.repeat(aktiv, K_KAND)
        par = lo[zi] + (hi[zi] - lo[zi]) * np.tile(frac, aktiv.size)
        t0 = time.perf_counter()
        zust, schritte = kandidaten_entscheiden(zi, par, P, lo, hi)
        schritte_ges += schritte
        u = zust < 0.0
        o = zust > 0.0
        lo_neu = lo.copy()
        hi_neu = hi.copy()
        np.maximum.at(lo_neu, zi[u], par[u])
        np.minimum.at(hi_neu, zi[o], par[o])
        mu = np.full(n, -np.inf)
        mo = np.full(n, np.inf)
        np.maximum.at(mu, zi[u], par[u])
        np.minimum.at(mo, zi[o], par[o])
        # Unterschuss oberhalb eines Ueberschusses: oberhalb des Rauschbodens ein echter Befund (nicht monoton),
        # darunter ist die Einschachtelung am Rauschboden der Integration angekommen (Klammer gilt als geschlossen).
        verl = mu - mo
        rausch = RAUSCH_REL * np.maximum(1.0, np.abs(0.5 * (lo + hi)))
        nichtmonoton |= verl > rausch
        am_boden = (verl > 0.0) & (verl <= rausch)
        rauschboden = np.maximum(rauschboden, np.where(am_boden, verl, 0.0))
        lo_neu, hi_neu = np.minimum(lo_neu, hi_neu), np.maximum(lo_neu, hi_neu)
        gleich = (lo_neu == lo) & (hi_neu == hi)
        still = np.where(~fertig & gleich, still + 1, 0)
        lo, hi = lo_neu, hi_neu
        runden[aktiv] += 1
        breite = hi - lo
        tol = 8.0 * EPS * np.maximum(1.0, np.abs(0.5 * (lo + hi)))
        geschlossen |= (breite <= tol) | am_boden
        fertig |= geschlossen
        fertig |= still >= 2
        log(f"  Runde {runde + 1}: {aktiv.size} Zeilen offen, {schritte} Schritte, "
            f"{time.perf_counter() - t0:.1f} s, noch offen {int((~fertig).sum())}")
    konvergiert = geschlossen
    return dict(lo=lo, hi=hi, konvergiert=konvergiert, stillstand=(still >= 2) & ~konvergiert,
                nichtmonoton=nichtmonoton, runden=runden, schritte=schritte_ges, rauschboden=rauschboden)


# ---------------------------------------------------------------- Profile, Schwanz, Integrale

def bahnen_bis_schnitt(P, lo, hi):
    """Drei Bahnen je Zeile (lo, Mitte, hi). Die Mitte wird bis zum Schnitt gespeichert; lo und hi geben die
    Spreizung am Schnitt. Rueckgabe: Bahn der Mitte (Schritte x Zeilen), Schnittindex, Gruende."""
    n = P["n"]
    mitte = 0.5 * (lo + hi)
    par = np.concatenate([lo, mitte, hi])
    zi = np.tile(np.arange(n), 3)
    p = np.where(P["logp"][zi], np.exp(np.minimum(par, 700.0)), par)
    a = P["a"][zi]
    c5 = P["c5"][zi]
    q5 = 1.5 * c5
    mm = P["m"][zi]
    m2 = mm * mm
    h = P["h"][zi]
    ft = P["ftop"][zi]
    fl = P["ftal"][zi]
    r = P["n0"][zi] * h
    f, fp = reihe(p, a, c5, mm, r)
    gef = mm == 0.0
    zust = np.zeros(3 * n)
    fmax = f.copy()
    faellt = np.zeros(3 * n, bool)
    bahn_f = [f[n:2 * n].copy()]
    bahn_fp = [fp[n:2 * n].copy()]
    j_cut = np.full(n, -1)
    spreiz = np.full(n, np.nan)
    fertig = np.zeros(n, bool)
    grund = np.array(["offen"] * n, dtype=object)
    rcap = P["rcap"]
    s = 0
    while not fertig.all():
        f, fp = rk4_schritt(r, h, f, fp, a, q5, m2)
        r = r + h
        s += 1
        offen = zust == 0.0
        ueber = offen & (~(f <= ft) | (f < 0.0))
        unter = offen & ~ueber & gef & (fp > 0.0) & (f < fl)
        gef = gef | (fp < 0.0)
        zust[ueber] = 1.0
        zust[unter] = -1.0
        tot = zust != 0.0
        f = np.where(tot, 0.0, f)
        fp = np.where(tot, 0.0, fp)
        fmax = np.maximum(fmax, f)
        faellt = faellt | (fp < 0.0)
        fm = f[n:2 * n]
        neu = ~fertig & ~tot[n:2 * n] & faellt[n:2 * n] & (fm < SCHNITT * fmax[n:2 * n])
        if neu.any():
            j_cut[neu] = P["n0"][neu] + s
            f_lo, f_hi = f[:n], f[2 * n:]
            ok = ~tot[:n] & ~tot[2 * n:]
            spreiz[neu] = np.where(ok[neu], np.abs(f_hi[neu] - f_lo[neu]) / fm[neu], np.inf)
            grund[neu] = "ok"
            fertig |= neu
        klass = ~fertig & tot[n:2 * n]
        if klass.any():
            grund[klass] = np.where(zust[n:2 * n][klass] > 0, "Mitte-Bahn vor dem Schwanz ueber (Ueberschuss)",
                                    "Mitte-Bahn vor dem Schwanz umgekehrt (Unterschuss)")
            fertig |= klass
        kappe = ~fertig & (r[n:2 * n] >= rcap)
        if kappe.any():
            grund[kappe] = "Schwanzschwelle bis r_cap nicht erreicht"
            fertig |= kappe
        bahn_f.append(fm.copy())
        bahn_fp.append(fp[n:2 * n].copy())
    return np.array(bahn_f), np.array(bahn_fp), j_cut, spreiz, grund, mitte


def schwanz(P, zz, j_cut):
    """Lineare Schwanzgleichung f'' = (a + m^2/r^2) f - f'/r rueckwaerts von r_end bis r_cut, normiert auf f(r_cut) = 1.
    Rueckwaerts ist K_m(kappa r) die anwachsende Loesung, I_m faellt ab: stabil."""
    kappa = P["kappa"][zz]
    h = P["h"][zz]
    n_t = np.ceil(SCHWANZ_LAENGE / (kappa * h)).astype(int)
    n_t = n_t + ((j_cut + n_t) % 2)                 # j_end gerade: Simpson ueber 0..j_end
    j_end = j_cut + n_t
    nz = zz.size
    n_max = int(n_t.max())
    TF = np.zeros((nz, n_max + 1))
    TP = np.zeros((nz, n_max + 1))
    a = P["a"][zz]
    m2 = P["m"][zz] ** 2
    r = j_end * h
    f = np.ones(nz)
    fp = -(kappa + 0.5 / r)
    rows = np.arange(nz)
    TF[rows, n_t] = f
    TP[rows, n_t] = fp
    for s in range(n_max):
        akt = s < n_t
        i = rows[akt]
        f_a, fp_a = rk4_linear(r[i], -h[i], f[i], fp[i], a[i], m2[i])
        f[i], fp[i] = f_a, fp_a
        r[i] = r[i] - h[i]
        TF[i, n_t[i] - s - 1] = f_a
        TP[i, n_t[i] - s - 1] = fp_a
    norm = TF[:, 0:1].copy()
    return TF / norm, TP / norm, n_t


def simpson_gewichte(n_pkt, h):
    w = np.ones(n_pkt)
    w[1:-1:2] = 4.0
    w[2:-1:2] = 2.0
    return w * (h / 3.0)


def radien(r, s):
    j = int(np.argmax(s))
    smax = s[j]
    rmax = r[j]
    if 0 < j < s.size - 1:
        d = s[j - 1] - 2.0 * s[j] + s[j + 1]
        if d < 0.0:
            rmax = r[j] + 0.5 * (s[j - 1] - s[j + 1]) / d * (r[1] - r[0])
    halb = 0.5 * smax
    innen = 0.0
    if s[0] < halb:
        k = int(np.argmax(s >= halb))
        innen = r[k - 1] + (halb - s[k - 1]) / (s[k] - s[k - 1]) * (r[k] - r[k - 1])
    nach = np.nonzero(s[j:] < halb)[0]
    aussen = float("nan")
    if nach.size:
        k = j + int(nach[0])
        aussen = r[k - 1] + (s[k - 1] - halb) / (s[k - 1] - s[k]) * (r[k] - r[k - 1])
    return smax, rmax, innen, aussen


def profile_bauen(P, sch, zeilen, gitter_schluessel, log):
    n = P["n"]
    lo, hi = sch["lo"], sch["hi"]
    B_f, B_fp, j_cut, spreiz, grund, mitte = bahnen_bis_schnitt(P, lo, hi)
    p_mitte = np.where(P["logp"], np.exp(np.minimum(mitte, 700.0)), mitte)
    gut = (j_cut > 0) & sch["konvergiert"] & ~sch["nichtmonoton"]
    zz = np.nonzero(j_cut > 0)[0]
    TF = TP = n_t = None
    if zz.size:
        TF, TP, n_t = schwanz(P, zz, j_cut[zz])
    pos = {int(z): k for k, z in enumerate(zz)}
    ergebnis = []
    profile = {}
    for i in range(n):
        z = zeilen[i]
        m = int(P["m"][i])
        a = float(P["a"][i])
        h = float(P["h"][i])
        n0 = int(P["n0"][i])
        zeile = dict(m=m, w2=z["w2"], nls=bool(z["nls"]), a=a, h=h, n0=n0,
                     p=float(p_mitte[i]), par_klammer=float(hi[i] - lo[i]),
                     klammer_art="ln p" if P["logp"][i] else "p", runden=int(sch["runden"][i]),
                     konvergiert=bool(sch["konvergiert"][i]), stillstand=bool(sch["stillstand"][i]),
                     rauschboden=float(sch["rauschboden"][i]),
                     nichtmonoton=bool(sch["nichtmonoton"][i]), grund=str(grund[i]), gueltig=False)
        if not sch["konvergiert"][i]:
            zeile["grund"] = "Klammer nicht geschlossen (keine Entscheidung bis r_cap)" if sch["stillstand"][i] \
                else "Klammer nach RUNDEN_MAX offen"
        elif sch["nichtmonoton"][i]:
            zeile["grund"] = "Einschachtelung nicht monoton (Unterschuss oberhalb eines Ueberschusses)"
        if j_cut[i] <= 0:
            ergebnis.append(zeile)
            continue
        k = pos[i]
        jc = int(j_cut[i])
        js = np.arange(n0) * h
        f_r, fp_r = reihe(p_mitte[i], a, P["c5"][i], float(m), js)
        f_b = B_f[:jc - n0 + 1, i]
        fp_b = B_fp[:jc - n0 + 1, i]
        c = f_b[-1]
        f = np.concatenate([f_r, f_b, c * TF[k, 1:n_t[k] + 1]])
        fp = np.concatenate([fp_r, fp_b, c * TP[k, 1:n_t[k] + 1]])
        r = np.arange(f.size) * h
        w = simpson_gewichte(f.size, h) * ZWEIPI * r
        s = f * f
        with np.errstate(divide="ignore", invalid="ignore"):
            zentr = np.where(r > 0.0, m * m * s / np.where(r > 0.0, r * r, 1.0), 0.0)
        N = float(np.sum(w * s))
        G = float(np.sum(w * (fp * fp + zentr)))
        Nr = float(np.sum(w * s * r))
        smax, rmax, rin, raus = radien(r, s)
        kappa = math.sqrt(a)
        sprung = float((fp_b[-1] - c * TP[k, 0]) / (kappa * c))
        zeile.update(N=N, G=G, S_max=float(smax), R_max=float(rmax), R_innen=float(rin), R_aussen=float(raus),
                     dicke=float(raus - rin), r_mittel=Nr / N, r_cut=jc * h, r_end=(f.size - 1) * h,
                     schwanzsprung=sprung, spreizung=float(spreiz[i]))
        if P["nls"][i]:
            V4 = float(np.sum(w * s * s))
            zeile.update(V4=V4, pohozaev=(V4 - N) / (V4 + N), G_minus_N=(G - N) / N,
                         Q=2.0 * N, E=2.0 * N, E_durch_Q=1.0, J=2.0 * m * N, omega=1.0)
            virial = zeile["pohozaev"]
            el = zeile["G_minus_N"]
        else:
            w2 = z["w2"]
            om = math.sqrt(w2)
            VU = float(np.sum(w * upot(s)))
            SUp = float(np.sum(w * s * upot_ab(s)))
            Q = 2.0 * om * N
            E = w2 * N + G + VU
            virial = (VU - w2 * N) / (VU + w2 * N)
            el = (G + SUp - w2 * N) / (G + SUp + w2 * N)
            zeile.update(VU=VU, Q=Q, E=E, E_durch_Q=E / Q, J=m * Q, omega=om, virial=virial, el_rest=el)
        zeile["virial"] = float(virial)
        zeile["el_rest"] = float(el)
        zeile["gueltig"] = bool(gut[i])
        if not gut[i] and zeile["grund"] == "ok":
            zeile["grund"] = "Klammer nicht geschlossen" if not sch["konvergiert"][i] else "nicht monoton"
        ergebnis.append(zeile)
        if (m, w2_schluessel(z["w2"]), bool(z["nls"])) in gitter_schluessel:
            profile[(m, w2_schluessel(z["w2"]), bool(z["nls"]))] = (f, fp, h)
    return ergebnis, profile


# ---------------------------------------------------------------- Codeprobe auf dem Gitter

def hermite(f_tab, fp_tab, h, r):
    u = r / h
    j = np.clip(np.floor(u), 0, f_tab.size - 2)
    t = np.clip(u - j, 0.0, 1.0)
    j = j.astype(np.int64)
    f0, f1 = f_tab[j], f_tab[j + 1]
    d0, d1 = fp_tab[j] * h, fp_tab[j + 1] * h
    t2 = t * t
    t3 = t2 * t
    f = (2 * t3 - 3 * t2 + 1) * f0 + (t3 - 2 * t2 + t) * d0 + (-2 * t3 + 3 * t2) * f1 + (t3 - t2) * d1
    return np.where(u <= f_tab.size - 1, f, 0.0)


def gitterprobe(zeile, prof):
    f_tab, fp_tab, h = prof
    m = zeile["m"]
    w2 = zeile["w2"]
    om = math.sqrt(w2)
    fmax = float(np.max(f_tab))
    r_tab = np.arange(f_tab.size) * h
    ueber = np.nonzero(f_tab > 1e-8 * fmax)[0]
    L = float(r_tab[ueber[-1]]) + 2.0
    skala = fmax / float(np.max(np.abs(fp_tab)))
    dx = min(0.25, skala / GITTER_PUNKTE_JE_SKALA)
    N = int(math.ceil(2.0 * L / dx))
    N += N % 2
    if N > GITTER_N_MAX:
        N = GITTER_N_MAX
    dx = 2.0 * L / N
    x = -L + dx * np.arange(N)
    X, Y = np.meshgrid(x, x, indexing="ij")
    R = np.hypot(X, Y)
    fr = hermite(f_tab, fp_tab, h, R)
    if m == 0:
        psi = fr.astype(np.complex128)
    else:
        with np.errstate(invalid="ignore", divide="ignore"):
            ph = np.where(R > 0.0, (X + 1j * Y) / np.where(R > 0.0, R, 1.0), 0.0)
        psi = fr * ph ** m
    del fr
    k = 2.0 * math.pi * np.fft.fftfreq(N, d=dx)
    KX, KY = np.meshgrid(k, k, indexing="ij")
    psik = np.fft.fft2(psi)
    dpx = np.fft.ifft2(1j * KX * psik)
    dpy = np.fft.ifft2(1j * KY * psik)
    lap = np.fft.ifft2(-(KX * KX + KY * KY) * psik)
    del psik, KX, KY
    s = (psi * np.conj(psi)).real
    dA = dx * dx
    Q_g = 2.0 * om * float(np.sum(s)) * dA
    J_g = 2.0 * om * float(np.sum((np.conj(psi) * (X * dpy - Y * dpx)).imag)) * dA
    E_g = float(np.sum(w2 * s + (dpx * np.conj(dpx)).real + (dpy * np.conj(dpy)).real + upot(s))) * dA
    res = -lap + (upot_ab(s) - w2) * psi
    res_rel = math.sqrt(float(np.sum((res * np.conj(res)).real)) / float(np.sum(w2 * w2 * s)))
    Q, E = zeile["Q"], zeile["E"]
    return dict(m=m, w2=w2, N=N, dx=dx, L=L, Q_gitter=Q_g, J_gitter=J_g, E_gitter=E_g,
                J_durch_mQ_minus_1=(J_g / (m * Q_g) - 1.0) if m > 0 else None, J_durch_Q=J_g / Q_g,
                Q_rel=Q_g / Q - 1.0, E_rel=E_g / E - 1.0, feldgleichung_rest=res_rel)


# ---------------------------------------------------------------- Tabelle

def tabelle_rechnen(m_liste, w2_liste, h0, nls, gitter, log):
    t0 = time.perf_counter()
    zeilen = zeilen_bauen(m_liste, w2_liste, nls)
    P = parameter(zeilen, h0)
    log(f"Tabelle: {P['n']} Zeilen (m = {list(m_liste)}, {len(w2_liste)} Werte omega^2, NLS-Grenze: {nls}), "
        f"h0 = {h0}")
    sch = schiessen(P, log)
    t1 = time.perf_counter()
    gschl = set((m, w2_schluessel(w2), False) for m, w2 in gitter)
    zeilen_erg, profile = profile_bauen(P, sch, zeilen, gschl, log)
    t2 = time.perf_counter()
    proben = []
    for (m, w2k, _nls), prof in sorted(profile.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        z = next(z for z in zeilen_erg if z["m"] == m and not z["nls"] and w2_schluessel(z["w2"]) == w2k)
        if z["gueltig"]:
            tg = time.perf_counter()
            pr = gitterprobe(z, prof)
            pr["dauer_s"] = time.perf_counter() - tg
            proben.append(pr)
            log(f"  Gitterprobe m = {m}, omega^2 = {w2k}: N = {pr['N']}, J/Q = {pr['J_durch_Q']:.9f}, "
                f"Q_rel = {pr['Q_rel']:.1e}, E_rel = {pr['E_rel']:.1e}, Rest = {pr['feldgleichung_rest']:.1e}")
    t3 = time.perf_counter()
    dauer = dict(schiessen_s=t1 - t0, profile_s=t2 - t1, gitterprobe_s=t3 - t2, gesamt_s=t3 - t0,
                 rk4_schritte_schiessen=int(sch["schritte"]))
    return dict(h0=h0, m_liste=list(m_liste), w2_liste=list(w2_liste), nls=nls, zeilen=zeilen_erg,
                gitterprobe=proben, dauer=dauer)


# ---------------------------------------------------------------- Auswertung

def fit_gerade(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if x.size < 2:
        return None
    A = np.vstack([x, np.ones_like(x)]).T
    (b, c), *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - (b * x + c)
    se = float("nan")
    if x.size > 2:
        se = math.sqrt(float(np.sum(res * res)) / (x.size - 2) / float(np.sum((x - x.mean()) ** 2)))
    return dict(steigung=float(b), achse=float(c), rms=float(math.sqrt(np.mean(res * res))), se=se, n=int(x.size))


def familien(zeilen):
    fam = {}
    for z in zeilen:
        if z["nls"] or not z.get("gueltig") or abs(z.get("virial", 1.0)) > VIRIAL_MAX:
            continue
        fam.setdefault(z["m"], []).append(z)
    for m in fam:
        fam[m].sort(key=lambda z: z["w2"])
    return fam


def auswerten(tab):
    zeilen = tab["zeilen"]
    fam = familien(zeilen)
    w2_alle = sorted(set(w2_schluessel(z["w2"]) for z in zeilen if not z["nls"]))
    aus = dict(zeilen_gesamt=len(zeilen), zeilen_gueltig=sum(1 for z in zeilen if z["gueltig"]),
               zeilen_ungueltig=[dict(m=z["m"], w2=z["w2"], nls=z["nls"], grund=z["grund"]) for z in zeilen
                                 if not z["gueltig"]],
               zeilen_virial_zu_gross=[dict(m=z["m"], w2=z["w2"], virial=z.get("virial")) for z in zeilen
                                       if z["gueltig"] and abs(z.get("virial", 0.0)) > VIRIAL_MAX])
    # Q_min(m), E_min(m) im Gitter
    qmin = {}
    for m, zz in sorted(fam.items()):
        iq = int(np.argmin([z["Q"] for z in zz]))
        ie = int(np.argmin([z["E"] for z in zz]))
        zq = zz[iq]
        lage = "Rand oben (groesstes omega^2)" if iq == len(zz) - 1 else ("Rand unten" if iq == 0 else "innen")
        monoton = bool(np.all(np.diff([z["Q"] for z in zz]) < 0.0))
        qmin[m] = dict(Q_min=zq["Q"], w2_bei_Qmin=zq["w2"], E_bei_Qmin=zq["E"], E_min=zz[ie]["E"],
                       w2_bei_Emin=zz[ie]["w2"], lage=lage, Q_faellt_monoton_mit_w2=monoton, n_zeilen=len(zz),
                       R_max_bei_Qmin=zq["R_max"], J_bei_Qmin=m * zq["Q"])
    aus["qmin"] = {str(m): v for m, v in qmin.items()}
    nls = {z["m"]: z for z in zeilen if z["nls"] and z["gueltig"]}
    aus["nls_grenze"] = {str(m): dict(N_T=z["N"], Q_lim=z["Q"], rho_max=z["R_max"], rho_max_durch_m=(
        z["R_max"] / m if m else None), dicke=z["dicke"], pohozaev=z["pohozaev"], G_minus_N=z["G_minus_N"])
        for m, z in sorted(nls.items())}
    # beta
    mf = [m for m in M_FIT if m in qmin]
    aus["beta"] = fit_gerade(np.log(mf), np.log([qmin[m]["Q_min"] for m in mf])) if len(mf) >= 2 else None
    mfl = [m for m in M_FIT if m in nls]
    aus["beta_lim"] = fit_gerade(np.log(mfl), np.log([nls[m]["Q"] for m in mfl])) if len(mfl) >= 2 else None
    aus["beta_lokal"] = {f"{m1}-{m2}": math.log(qmin[m2]["Q_min"] / qmin[m1]["Q_min"]) / math.log(m2 / m1)
                         for m1, m2 in zip(mf[:-1], mf[1:])}
    # Ecken der fuehrenden Bahn: (E_min(m), J = m Q an derselben Stelle)
    ecken = {}
    for m, zz in fam.items():
        if m == 0:
            continue
        ie = int(np.argmin([z["E"] for z in zz]))
        ecken[m] = dict(E=zz[ie]["E"], J=m * zz[ie]["Q"], w2=zz[ie]["w2"], alpha_strich=m * zz[ie]["Q"] / zz[ie]["E"] ** 2)
    aus["ecken"] = {str(m): v for m, v in sorted(ecken.items())}
    me = [m for m in M_FIT if m in ecken]
    aus["alpha"] = fit_gerade(np.log([ecken[m]["E"] for m in me]), np.log([ecken[m]["J"] for m in me])) \
        if len(me) >= 2 else None
    if len(mfl) >= 2:
        aus["alpha_lim"] = fit_gerade(np.log([nls[m]["E"] for m in mfl]), np.log([nls[m]["J"] for m in mfl]))
    else:
        aus["alpha_lim"] = None
    aus["alpha_lokal"] = {f"{m1}-{m2}": math.log(ecken[m2]["J"] / ecken[m1]["J"]) / math.log(ecken[m2]["E"] /
                                                                                              ecken[m1]["E"])
                          for m1, m2 in zip(me[:-1], me[1:])}
    # Huellen: E_min(J) (Karte) und J_max(E) (Chew-Frautschi)
    kurven = {}
    for m, zz in fam.items():
        if m == 0 or len(zz) < 2:
            continue
        lnJ = np.log([m * z["Q"] for z in zz])
        lnE = np.log([z["E"] for z in zz])
        o = np.argsort(lnJ)
        kurven[m] = (lnJ[o], lnE[o])
    huelle = {}
    if len(me) >= 2 and all(m in kurven for m in me):
        jg = np.linspace(math.log(ecken[me[0]]["J"]), math.log(ecken[me[-1]]["J"]), 400)
        E_env = np.full(jg.size, np.inf)
        m_env = np.zeros(jg.size, int)
        for m, (lnJ, lnE) in kurven.items():
            drin = (jg >= lnJ[0]) & (jg <= lnJ[-1])
            e = np.where(drin, np.interp(jg, lnJ, lnE), np.inf)
            besser = e < E_env
            E_env = np.where(besser, e, E_env)
            m_env = np.where(besser, m, m_env)
        ok = np.isfinite(E_env)
        fe = fit_gerade(jg[ok], E_env[ok])
        spruenge = int(np.sum(np.diff(E_env[ok]) < 0.0))
        eg = np.linspace(math.log(ecken[me[0]]["E"]), math.log(ecken[me[-1]]["E"]), 400)
        J_env = np.full(eg.size, -np.inf)
        for m, (lnJ, lnE) in kurven.items():
            o = np.argsort(lnE)
            drin = (eg >= lnE[o][0]) & (eg <= lnE[o][-1])
            jj = np.where(drin, np.interp(eg, lnE[o], lnJ[o]), -np.inf)
            J_env = np.maximum(J_env, jj)
        ok2 = np.isfinite(J_env)
        fj = fit_gerade(eg[ok2], J_env[ok2])
        huelle = dict(E_min_von_J=dict(fit_lnE_gegen_lnJ=fe, alpha_huelle=(1.0 / fe["steigung"]) if fe else None,
                                       abwaertsspruenge=spruenge, m_anteile={str(m): int(np.sum(m_env == m))
                                                                             for m in sorted(set(m_env[ok]))}),
                      J_max_von_E=dict(fit_lnJ_gegen_lnE=fj, alpha_cf=fj["steigung"] if fj else None))
    aus["huelle"] = huelle
    # Ringbild
    ring = {}
    for w2 in W2_RING:
        k = w2_schluessel(w2)
        rr = {m: z for m, zz in fam.items() for z in zz if w2_schluessel(z["w2"]) == k}
        ms = [m for m in M_FIT if m in rr]
        eintrag = dict(R_max={str(m): rr[m]["R_max"] for m in sorted(rr)},
                       r_mittel={str(m): rr[m]["r_mittel"] for m in sorted(rr)},
                       dicke_durch_R={str(m): rr[m]["dicke"] / rr[m]["R_max"] for m in sorted(rr) if m > 0},
                       R_max_mal_kappa_durch_m={str(m): rr[m]["R_max"] * math.sqrt(1.0 - w2) / m
                                                for m in sorted(rr) if m > 0})
        if len(ms) >= 2:
            eintrag["gamma_R_max"] = fit_gerade(np.log(ms), np.log([rr[m]["R_max"] for m in ms]))
            eintrag["gamma_r_mittel"] = fit_gerade(np.log(ms), np.log([rr[m]["r_mittel"] for m in ms]))
        ring[str(k)] = eintrag
    if len(mfl) >= 2:
        ring["nls"] = dict(gamma_rho_max=fit_gerade(np.log(mfl), np.log([nls[m]["R_max"] for m in mfl])),
                           rho_max_durch_m={str(m): nls[m]["R_max"] / m for m in sorted(nls) if m > 0},
                           dicke_durch_rho={str(m): nls[m]["dicke"] / nls[m]["R_max"] for m in sorted(nls) if m > 0})
    aus["ring"] = ring
    # Rotorprobe bei festem Q (Nebenprobe)
    rotor = {}
    for qf in Q_ROTOR:
        e_m = {}
        for m, zz in fam.items():
            lnQ = np.log([z["Q"] for z in zz])
            lnE = np.log([z["E"] for z in zz])
            o = np.argsort(lnQ)
            if lnQ[o][0] <= math.log(qf) <= lnQ[o][-1]:
                e_m[m] = float(np.exp(np.interp(math.log(qf), lnQ[o], lnE[o])))
        eintrag = dict(E={str(m): v for m, v in sorted(e_m.items())})
        if 0 in e_m:
            dm = [m for m in sorted(e_m) if m > 0]
            eintrag["dE"] = {str(m): e_m[m] - e_m[0] for m in dm}
            pos = [m for m in dm if e_m[m] - e_m[0] > 0.0]
            if len(pos) >= 3:
                eintrag["exponent_dE_gegen_m"] = fit_gerade(np.log(pos), np.log([e_m[m] - e_m[0] for m in pos]))
        rotor[str(qf)] = eintrag
    aus["rotor"] = rotor
    # Nebenprobe dE = omega dQ (Trapez zwischen Nachbarzeilen, grob)
    de = {}
    for m, zz in fam.items():
        res = []
        for z1, z2 in zip(zz[:-1], zz[1:]):
            dE = z2["E"] - z1["E"]
            res.append(abs(dE - 0.5 * (z1["omega"] + z2["omega"]) * (z2["Q"] - z1["Q"])) / abs(dE))
        if res:
            de[str(m)] = max(res)
    aus["dE_omega_dQ_max_rest"] = de
    # L2: Anschluss m = 0 an RUNDE-03
    r3 = {}
    for w2, soll in R3_M0.items():
        z = next((z for z in zeilen if not z["nls"] and z["m"] == 0 and w2_schluessel(z["w2"]) == w2_schluessel(w2)),
                 None)
        if z is None:
            continue
        if not z["gueltig"]:
            r3[str(w2)] = dict(gueltig=False)
            continue
        ab = dict(p=z["p"] - soll["p"], Q=z["Q"] / soll["Q"] - 1.0, E=z["E"] / soll["E"] - 1.0,
                  S_max=z["S_max"] - soll["S_max"], R_halb=z["R_aussen"] - soll["R_halb"])
        p_zaehlt = abs(z["h"] - 0.01) < 1e-12        # p haengt an h; R3 rechnete mit h = 0,01
        r3[str(w2)] = dict(gueltig=True, abweichung=ab, p_zaehlt=p_zaehlt, h=z["h"],
                           bestanden=all(abs(ab[k]) <= R3_TOL[k] for k in ab if k != "p" or p_zaehlt))
    aus["l2_r3"] = r3
    aus["l2_r3_bestanden"] = bool(r3) and all(v.get("bestanden", False) for v in r3.values())
    # L2: Codeprobe J = m Q
    gp = tab.get("gitterprobe", [])
    aus["l2_gitter_bestanden"] = bool(gp) and all(
        (p["J_durch_mQ_minus_1"] is None or abs(p["J_durch_mQ_minus_1"]) <= GITTER_TOL_J) and
        abs(p["Q_rel"]) <= GITTER_TOL_Q and abs(p["E_rel"]) <= GITTER_TOL_E for p in gp)
    aus["l2_gitter_max"] = dict(
        J=max([abs(p["J_durch_mQ_minus_1"]) for p in gp if p["J_durch_mQ_minus_1"] is not None], default=None),
        J_m0=max([abs(p["J_durch_Q"]) for p in gp if p["m"] == 0], default=None),
        Q=max([abs(p["Q_rel"]) for p in gp], default=None), E=max([abs(p["E_rel"]) for p in gp], default=None),
        feldgleichung=max([p["feldgleichung_rest"] for p in gp], default=None))
    # Urteile (Regeln vorab in PLAN.md Abschnitt 5)
    urteil = {}
    if aus["alpha"]:
        al = aus["alpha"]["steigung"]
        urteil["alpha"] = ("H getragen (alpha = 2 innerhalb 0,1)" if abs(al - ALPHA_H) <= ALPHA_TOL else
                           "Gegenhypothese getragen (alpha <= 1,6)" if al <= ALPHA_GEGEN else "Zwischenwert")
    if aus["beta"]:
        be = aus["beta"]["steigung"]
        urteil["beta"] = "Ring-Mechanismus getragen (beta = 1 innerhalb 0,1)" if abs(be - 1.0) <= BETA_TOL \
            else "beta weicht von 1 ab"
    urteil["qmin_lage"] = sorted(set(v["lage"] for v in qmin.values()))
    aus["urteil"] = urteil
    return aus


def l3_vergleich(tab1, tab2, aus1, aus2):
    z2 = {(z["m"], w2_schluessel(z["w2"]), z["nls"]): z for z in tab2["zeilen"]}
    fitz = set()
    for m in M_FIT:
        q = aus1["qmin"].get(str(m))
        if q:
            fitz.add((m, w2_schluessel(q["w2_bei_Qmin"]), False))
            fitz.add((m, w2_schluessel(q["w2_bei_Emin"]), False))
        fitz.add((m, None, True))
    zeilen = []
    for z in tab1["zeilen"]:
        k = (z["m"], w2_schluessel(z["w2"]), z["nls"])
        y = z2.get(k)
        if not (z["gueltig"] and y and y["gueltig"]):
            continue
        zeilen.append(dict(m=z["m"], w2=z["w2"], nls=z["nls"], dQ=y["Q"] / z["Q"] - 1.0, dE=y["E"] / z["E"] - 1.0,
                           dR_max=y["R_max"] - z["R_max"], fitzeile=k in fitz))
    def diff(schl):
        a1, a2 = aus1.get(schl), aus2.get(schl)
        return (a2["steigung"] - a1["steigung"]) if (a1 and a2) else None
    d = dict(alpha=diff("alpha"), beta=diff("beta"), alpha_lim=diff("alpha_lim"), beta_lim=diff("beta_lim"))
    maxfit = max([max(abs(v["dQ"]), abs(v["dE"])) for v in zeilen if v["fitzeile"]], default=None)
    maxall = max([max(abs(v["dQ"]), abs(v["dE"])) for v in zeilen], default=None)
    bestanden = (maxfit is not None and maxfit <= L3_TOL_REL and
                 all(v is not None and abs(v) <= L3_TOL_FIT for v in (d["alpha"], d["beta"])))
    return dict(h1=tab1["h0"], h2=tab2["h0"], differenzen=d, max_rel_fitzeilen=maxfit, max_rel_alle=maxall,
                bestanden=bool(bestanden), zeilen=zeilen)


# ---------------------------------------------------------------- Bericht

def f6(x, fmt="{:.6g}"):
    if x is None:
        return "-"
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return fmt.format(x)


def tabellen_text(tab):
    zeilen = [f"Profiltabelle, h0 = {tab['h0']} (Schrittweite je Zeile h = h0 * min(3, max(1, 0,3/sqrt(a))))",
              "m  omega^2 | h      | p bzw. g(0)          | Klammer | Q            | E            | E/Q      | "
              "S_max    | R_max    | R_innen  | R_aussen | r_mittel | Virialrest | EL-Rest  | Schwanzsprung | "
              "Spreizung | gueltig"]
    for z in tab["zeilen"]:
        w = "NLS " if z["nls"] else f"{z['w2']:.3f}"
        if "Q" not in z:
            zeilen.append(f"{z['m']:<2} {w:>7} | {z['h']:.4f} | {z['p']:.15g} | {z['par_klammer']:.1e} | NEIN: {z['grund']}")
            continue
        zeilen.append(
            f"{z['m']:<2} {w:>7} | {z['h']:.4f} | {z['p']:.15g} | {z['par_klammer']:.1e} | {z['Q']:12.6f} | "
            f"{z['E']:12.6f} | {z['E_durch_Q']:.6f} | {z['S_max']:.6f} | {z['R_max']:8.3f} | {z['R_innen']:8.3f} | "
            f"{z['R_aussen']:8.3f} | {z['r_mittel']:8.3f} | {z['virial']:+.1e} | {z['el_rest']:+.1e} | "
            f"{z['schwanzsprung']:+.1e} | {z['spreizung']:.1e} | "
            f"{'ja' if z['gueltig'] else 'NEIN: ' + z['grund']}")
    return zeilen


def auswertung_text(aus, l3=None):
    t = []
    t.append(f"Zeilen: {aus['zeilen_gesamt']}, gueltig {aus['zeilen_gueltig']}")
    for u in aus["zeilen_ungueltig"]:
        t.append(f"  keine Loesung: m = {u['m']}, omega^2 = {u['w2'] if not u['nls'] else 'NLS'}: {u['grund']}")
    for u in aus["zeilen_virial_zu_gross"]:
        t.append(f"  Virialrest zu gross (nicht in den Fits): m = {u['m']}, omega^2 = {u['w2']}: {u['virial']:.1e}")
    t.append("")
    t.append("Q_min(m) im Gitter (kleinste Ladung je m) und NLS-Grenze omega -> 1 (Q_lim = 2 N_T):")
    t.append("m | Q_min        | bei omega^2 | Lage                        | E_min        | J = m Q_min  | "
             "Q faellt monoton | Q_lim (NLS)  | rho_max/m (NLS)")
    for m in range(9):
        q = aus["qmin"].get(str(m))
        nl = aus["nls_grenze"].get(str(m), {})
        if not q:
            t.append(f"{m} | keine gueltigen Zeilen")
            continue
        t.append(f"{m} | {q['Q_min']:12.5f} | {q['w2_bei_Qmin']:.3f}       | {q['lage']:<27} | {q['E_min']:12.5f} | "
                 f"{q['J_bei_Qmin']:12.4f} | {'ja' if q['Q_faellt_monoton_mit_w2'] else 'nein':<16} | "
                 f"{f6(nl.get('Q_lim'), '{:12.5f}')} | {f6(nl.get('rho_max_durch_m'), '{:.4f}')}")
    for schl, name in (("beta", "beta (Gitter, m = 3..8)"), ("beta_lim", "beta (NLS-Grenze, m = 3..8)"),
                       ("alpha", "alpha (Ecken der fuehrenden Bahn, Gitter, m = 3..8)"),
                       ("alpha_lim", "alpha (Ecken, NLS-Grenze, m = 3..8)")):
        fz = aus.get(schl)
        if fz:
            t.append(f"{name}: {fz['steigung']:.5f} (Standardfehler {fz['se']:.1e}, rms {fz['rms']:.1e}, n = {fz['n']})")
    t.append("beta lokal: " + ", ".join(f"{k}: {v:.4f}" for k, v in aus["beta_lokal"].items()))
    t.append("alpha lokal: " + ", ".join(f"{k}: {v:.4f}" for k, v in aus["alpha_lokal"].items()))
    t.append("Ecken (E_min(m), J = m Q): " + "; ".join(
        f"m={m}: E={v['E']:.3f}, J={v['J']:.2f}, J/E^2={v['alpha_strich']:.5f}, w2={v['w2']:.3f}"
        for m, v in aus["ecken"].items()))
    hu = aus.get("huelle") or {}
    if hu:
        e = hu["E_min_von_J"]
        j = hu["J_max_von_E"]
        t.append(f"Huelle E_min(J) (Karte): alpha = 1/Steigung(ln E gegen ln J) = {f6(e['alpha_huelle'], '{:.4f}')}, "
                 f"Abwaertsspruenge (Saegezahn): {e['abwaertsspruenge']}, Anteile je m: {e['m_anteile']}")
        t.append(f"Huelle J_max(E) (Chew-Frautschi): alpha = {f6(j['alpha_cf'], '{:.4f}')}")
    t.append("")
    t.append("Ringbild: Exponent gamma aus ln R_max gegen ln m (m = 3..8); R_max sqrt(a)/m (NLS-Duennring: sqrt 2 = 1,4142)")
    for k, v in aus["ring"].items():
        if k == "nls":
            g = v["gamma_rho_max"]
            t.append(f"  NLS: gamma = {g['steigung']:.4f}; rho_max/m: " +
                     ", ".join(f"{m}: {x:.4f}" for m, x in v["rho_max_durch_m"].items()) +
                     "; Dicke/rho_max: " + ", ".join(f"{m}: {x:.3f}" for m, x in v["dicke_durch_rho"].items()))
            continue
        g = v.get("gamma_R_max")
        t.append(f"  omega^2 = {k}: gamma = {f6(g['steigung'] if g else None, '{:.4f}')}; R_max: " +
                 ", ".join(f"{m}: {x:.2f}" for m, x in v["R_max"].items()) + "; R_max sqrt(a)/m: " +
                 ", ".join(f"{m}: {x:.3f}" for m, x in v["R_max_mal_kappa_durch_m"].items()) + "; Dicke/R: " +
                 ", ".join(f"{m}: {x:.3f}" for m, x in v["dicke_durch_R"].items()))
    t.append("")
    t.append("Rotorprobe (Nebenprobe): bei festem Q Energie je m; Exponent aus ln(E_m - E_0) gegen ln m (starrer Rotor: 2)")
    for q, v in aus["rotor"].items():
        ex = v.get("exponent_dE_gegen_m")
        t.append(f"  Q = {q}: E_m = " + ", ".join(f"{m}: {x:.3f}" for m, x in v["E"].items()) +
                 f"; Exponent = {f6(ex['steigung'] if ex else None, '{:.3f}')}")
    t.append("Nebenprobe dE = omega dQ (Trapez zwischen Nachbarzeilen, max. relativer Rest je m): " +
             ", ".join(f"{m}: {v:.1e}" for m, v in aus["dE_omega_dQ_max_rest"].items()))
    t.append("")
    t.append("L2 Anschluss m = 0 an RUNDE-03 (Abweichungen: p, S_max, R_halb absolut; Q, E relativ; Grenzen "
             f"{R3_TOL}):")
    for w2, v in aus["l2_r3"].items():
        if not v["gueltig"]:
            t.append(f"  omega^2 = {w2}: Zeile ungueltig")
            continue
        ab = v["abweichung"]
        t.append(f"  omega^2 = {w2} (h = {v['h']}): dp = {ab['p']:+.2e}, dQ/Q = {ab['Q']:+.2e}, dE/E = {ab['E']:+.2e}, "
                 f"dS_max = {ab['S_max']:+.2e}, dR_halb = {ab['R_halb']:+.2e}"
                 f"{'' if v['p_zaehlt'] else ' (p nicht gewertet: h ungleich 0,01)'} -> "
                 f"{'bestanden' if v['bestanden'] else 'NICHT bestanden'}")
    t.append(f"  L2 (R3-Anschluss): {'bestanden' if aus['l2_r3_bestanden'] else 'NICHT bestanden oder fehlt'}")
    g = aus["l2_gitter_max"]
    t.append(f"L2 Codeprobe J = m Q auf dem Gitter: max |J/(mQ) - 1| = {f6(g['J'], '{:.1e}')}, m = 0: max |J/Q| = "
             f"{f6(g['J_m0'], '{:.1e}')}, max |Q_gitter/Q - 1| = {f6(g['Q'], '{:.1e}')}, max |E_gitter/E - 1| = "
             f"{f6(g['E'], '{:.1e}')}, max Rest der 2D-Feldgleichung = {f6(g['feldgleichung'], '{:.1e}')} -> "
             f"{'bestanden' if aus['l2_gitter_bestanden'] else 'NICHT bestanden oder fehlt'}")
    if l3:
        d = l3["differenzen"]
        t.append(f"L3 halbe Schrittweite (h0 = {l3['h1']} gegen {l3['h2']}): d alpha = {f6(d['alpha'], '{:+.2e}')}, "
                 f"d beta = {f6(d['beta'], '{:+.2e}')}, d alpha_lim = {f6(d['alpha_lim'], '{:+.2e}')}, "
                 f"d beta_lim = {f6(d['beta_lim'], '{:+.2e}')}, max |dQ/Q|, |dE/E| in den Fitzeilen = "
                 f"{f6(l3['max_rel_fitzeilen'], '{:.1e}')}, in allen Zeilen = {f6(l3['max_rel_alle'], '{:.1e}')} -> "
                 f"{'bestanden' if l3['bestanden'] else 'NICHT bestanden'}")
    t.append("")
    t.append("Urteile (Regeln vorab, PLAN.md Abschnitt 5): " + json.dumps(aus["urteil"], ensure_ascii=False))
    return t


def schreiben(out, ergebnis, text):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "ergebnis.json"), "w") as fh:
        json.dump(ergebnis, fh, indent=1, ensure_ascii=False, default=float)
    with open(os.path.join(out, "bericht.txt"), "w") as fh:
        fh.write("\n".join(text) + "\n")


def kopf(titel, start):
    return [f"{titel}. Start {start}, Ende {jetzt()}, {platform.node()}, Python {platform.python_version()}, "
            f"numpy {np.__version__}, OMP_NUM_THREADS={os.environ.get('OMP_NUM_THREADS')}",
            "Explorativ (v3). Plan und Vorhersagen: PLAN.md. Gueltig = Klammer geschlossen, Mitte-Bahn erreicht die "
            "Schwanzschwelle, Einschachtelung monoton."]


# ---------------------------------------------------------------- Unterbefehle

def zahlenliste(s, typ):
    return [typ(x) for x in s.split(",") if x.strip()]


def cmd_tabelle(args):
    start = jetzt()
    m_liste = zahlenliste(args.m, int) if args.m else list(M_STANDARD)
    w2_liste = zahlenliste(args.w2, float) if args.w2 else list(W2_STANDARD)
    tab = tabelle_rechnen(m_liste, w2_liste, args.h, not args.ohne_nls, () if args.ohne_gitter else GITTER_ZEILEN,
                          print)
    aus = auswerten(tab)
    ergebnis = dict(befehl="tabelle", start=start, ende=jetzt(), tabelle=tab, auswertung=aus)
    d = tab["dauer"]
    text = kopf("RG-1 Tabelle", start)
    text.append(f"Dauer [s]: Schiessen {d['schiessen_s']:.1f}, Profile {d['profile_s']:.1f}, Gitterprobe "
                f"{d['gitterprobe_s']:.1f}, gesamt {d['gesamt_s']:.1f}; RK4-Schritte im Schiessen {d['rk4_schritte_schiessen']}")
    text += [""] + tabellen_text(tab) + [""] + auswertung_text(aus)
    schreiben(args.out, ergebnis, text)
    print("\n".join(text[-40:]))


def cmd_bahn(args):
    start = jetzt()
    with open(args.tabelle) as fh:
        tab1 = json.load(fh)["tabelle"]
    aus1 = auswerten(tab1)
    l3 = None
    aus2 = None
    if args.l3:
        with open(args.l3) as fh:
            tab2 = json.load(fh)["tabelle"]
        aus2 = auswerten(tab2)
        l3 = l3_vergleich(tab1, tab2, aus1, aus2)
    ergebnis = dict(befehl="bahn", start=start, ende=jetzt(), quelle=args.tabelle, quelle_l3=args.l3,
                    auswertung=aus1, auswertung_l3_tabelle=aus2, l3=l3)
    text = kopf("RG-1 Bahn (Auswertung)", start) + [f"Tabelle: {args.tabelle}; L3-Tabelle: {args.l3}", ""]
    text += auswertung_text(aus1, l3)
    schreiben(args.out, ergebnis, text)
    print("\n".join(text))


def cmd_rauch(args):
    start = jetzt()
    t0 = time.perf_counter()
    tabs = []
    for h0 in RAUCH_H:
        print(f"Rauchtest-Tabelle h0 = {h0}")
        tabs.append(tabelle_rechnen(RAUCH_M, RAUCH_W2, h0, True, RAUCH_GITTER, print))
    aus = [auswerten(t) for t in tabs]
    l3 = l3_vergleich(tabs[0], tabs[1], aus[0], aus[1])
    zeitprobe = None
    if not args.ohne_zeitprobe:
        # Hochrechnung: eine Schiessrunde der vollen Tabelle (erste Runde ist die teuerste)
        zeilen = zeilen_bauen(M_STANDARD, W2_STANDARD, True)
        P = parameter(zeilen, H_STANDARD)
        zi = np.repeat(np.arange(P["n"]), K_KAND)
        frac = np.arange(1, K_KAND + 1) / (K_KAND + 1.0)
        par = P["lo0"][zi] + (P["hi0"][zi] - P["lo0"][zi]) * np.tile(frac, P["n"])
        tz = time.perf_counter()
        _z, schritte = kandidaten_entscheiden(zi, par, P, P["lo0"], P["hi0"])
        dz = time.perf_counter() - tz
        runden_rauch = max(int(np.max([z["runden"] for z in t["zeilen"]])) for t in tabs)
        # Obere Schranke: jede Runde mit allen Kandidaten ueber die volle Schrittzahl der ersten Runde
        rr = 5.0 + np.arange(zi.size) * 1e-4
        ff = np.full(zi.size, 0.3)
        gg = np.zeros(zi.size)
        tb = time.perf_counter()
        for _ in range(200):
            f2, g2 = rk4_schritt(rr, P["h"][zi], ff, gg, P["a"][zi], 1.5 * P["c5"][zi], P["m"][zi] ** 2)
            _k = (~(f2 <= P["ftop"][zi]) | (f2 < 0.0)) | ((g2 > 0.0) & (f2 < P["ftal"][zi]))
        t_schritt = (time.perf_counter() - tb) / 200.0
        schranke = runden_rauch * schritte * t_schritt
        zeitprobe = dict(erste_runde_s=dz, schritte=schritte, runden_erwartet=runden_rauch,
                         sekunden_je_schritt_volle_breite=t_schritt,
                         tabelle_h001_schaetzung_s=dz * runden_rauch * 1.3,
                         tabelle_h001_obere_schranke_schiessen_s=schranke,
                         tabelle_h0005_obere_schranke_schiessen_s=2.0 * schranke)
    dauer = time.perf_counter() - t0
    ergebnis = dict(befehl="rauch", start=start, ende=jetzt(), dauer_s=dauer, tabellen=tabs, auswertungen=aus, l3=l3,
                    zeitprobe=zeitprobe)
    text = kopf("RG-1 Rauchtest (Zahlen nur Vorschau, kleines m- und omega-Raster)", start)
    text.append(f"Dauer gesamt {dauer:.1f} s; Tabellen: " + ", ".join(
        f"h0 = {t['h0']}: {t['dauer']['gesamt_s']:.1f} s ({t['dauer']['rk4_schritte_schiessen']} RK4-Schritte)" for t in tabs))
    if zeitprobe:
        text.append(f"Zeitprobe volle Tabelle (234 Zeilen), erste Schiessrunde: {zeitprobe['erste_runde_s']:.1f} s, "
                    f"{zeitprobe['schritte']} Schritte, {zeitprobe['runden_erwartet']} Runden erwartet. Schaetzung "
                    f"Schiessen h0 = 0,01: etwa {zeitprobe['tabelle_h001_schaetzung_s'] / 60:.1f} min (Runden x erste "
                    f"Runde x 1,3); obere Schranke (alle Kandidaten jede Runde ueber die volle Schrittzahl, "
                    f"{zeitprobe['sekunden_je_schritt_volle_breite'] * 1e3:.2f} ms je Schritt): h0 = 0,01 "
                    f"{zeitprobe['tabelle_h001_obere_schranke_schiessen_s'] / 60:.1f} min, h0 = 0,005 "
                    f"{zeitprobe['tabelle_h0005_obere_schranke_schiessen_s'] / 60:.1f} min; dazu Profile und "
                    f"Gitterprobe (15 Zeilen) etwa 1 min")
    for t, a in zip(tabs, aus):
        text += [""] + tabellen_text(t) + [""] + auswertung_text(a, l3 if t is tabs[0] else None)
    schreiben(args.out, ergebnis, text)
    print("\n".join(text))


def main():
    ap = argparse.ArgumentParser(description="RG-1: Regge-Turm drehender Q-Baelle in 2D")
    sub = ap.add_subparsers(dest="befehl", required=True)
    a1 = sub.add_parser("tabelle")
    a1.add_argument("--h", type=float, default=H_STANDARD)
    a1.add_argument("--out", default="ausgabe/tabelle")
    a1.add_argument("--m", default="")
    a1.add_argument("--w2", default="")
    a1.add_argument("--ohne-nls", action="store_true")
    a1.add_argument("--ohne-gitter", action="store_true")
    a2 = sub.add_parser("bahn")
    a2.add_argument("--tabelle", required=True)
    a2.add_argument("--l3", default=None)
    a2.add_argument("--out", default="ausgabe/bahn")
    a3 = sub.add_parser("rauch")
    a3.add_argument("--out", default="lauf-lokal/rauch")
    a3.add_argument("--ohne-zeitprobe", action="store_true")
    args = ap.parse_args()
    {"tabelle": cmd_tabelle, "bahn": cmd_bahn, "rauch": cmd_rauch}[args.befehl](args)


if __name__ == "__main__":
    main()
