#!/usr/bin/env python3
"""AFM-KANAL-2 (Runde 12 nach v3, explorativ): stille Stelle (W = 0 bei reellem rho) im gekoppelten AFM-Ball.

Neu geschrieben. Importiert unveraendert (Kopien im selben Ordner, sha256 in PLAN.md):
  afm_kanal.py (AFM-KANAL-1: AFM-Profile, V_u, V_v, Ableitungen, Wandgeometrie)
  nls2.py      (RUNDE-10/nls-leiter: KG-Q-Ball-Profil fuer die Positivkontrolle)

Lineares Problem (afm-kanal1/HERLEITUNG.md), l = 0, y = r w, Zeitfaktor e^{-i rho t}:
   y1'' = (A + B rho - rho^2) y1 + C y2      Kanal 1 geschlossen (w = u + i v), Schwelle 1 + Omega
   y2'' = C y1 + (A - B rho - rho^2) y2      Kanal 2 offen (w~ = u - i v), Schwelle 1 - Omega
   AFM: A = (V_u + V_v)/2, B = 2 Omega cos Theta, C = (V_u - V_v)/2
   KG (Positivkontrolle, U = S - S^2 + S^3/2, wie bic2): A = dp - omega^2, B = 2 omega, C = sp
       (bic2: V = geschlossener Kanal omega - rho, U = offener Kanal omega + rho)
Gemeinsamer Codepfad (die Modelle gehen nur ueber A, B, C ein):
   y_a regulaer mit offenem Start (y2'(0) = 1), y_b regulaer mit geschlossenem Start (y1'(0) = 1): RK4, Schritt h,
   von 0 bis r_m (Koeffizienten vom Profilgitter h/2). z2 abklingend im geschlossenen Kanal: bei R y1 = 1,
   y1' = -kappa_c, offener Teil 0; RK4 von R nach r_m, je Schritt mit e^{-kappa_c h} skaliert (positiv, glatt in rho).
   L(y) = Omega(y, z2) = Wronski-Summe. W = L(y_a) + i L(y_b). W = 0 <=> z2 liegt in der regulaeren (Lagrange-)Ebene
   <=> regulaere, in beiden Kanaelen abfallende Loesung bei reellem rho = stille Stelle (wie bic2 exakt/kurve).
   s = L(y_a) an den Nullstellen von L(y_b), direkt gesucht: Raster, dann zwei Feinraster je Klammer, dann W exakt an
       der Nullstelle (keine lineare Interpolation von s ueber das Raster; Lehre LEITER-2D-PRAEZ).
   Umlauf: Phase von W auf dem Rand von Rechtecken in (Omega^2, rho), gegen den Uhrzeigersinn, adaptiv verfeinert
       (rho-Seiten halbiert, Omega^2-Seiten mit neuen Profilen), aufgeloest = jeder Phasensprung < 0,4 rad.
   Pole: D = det[y_a, y_b, j1, j2] bei komplexem rho (Jost-Ebene j1 ~ z2, j2 ~ auslaufend, fortlaufend
       orthonormiert), 2D-Newton wie bic2.
Kommandos: familie (AFM oder KG, eine Gitterstufe) | auswertung
"""
import argparse
import datetime
import glob
import json
import math
import os
import sys
import time

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
if HIER not in sys.path:
    sys.path.insert(0, HIER)
import afm_kanal as AK  # noqa: E402  (Kopie aus AFM-KANAL-1, unveraendert)

T0 = time.perf_counter()
PI = math.pi
SPRUNG = 0.4          # aufgeloest: jeder Phasensprung auf dem Rand < 0,4 rad (wie bic2)
RAND = 0.002          # Abstand der rho-Abtastung von den Schwellen 1 - Omega und 1 + Omega (wie bic2 kurve)
THETA_RAND = 1e-6     # Aussenrand R: Profilamplitude < 1e-6 * Amplitude(0), mindestens r = 20
FS = [0.5, 0.575, 0.65, 0.725, 0.8, 0.875, 0.95]
KG_X = [0.785, 0.79, 0.795, 0.80, 0.805, 0.81, 0.815]
KG_ZIEL = (0.797677, 1.744618)


def jetzt():
    return datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def uhr():
    return time.perf_counter() - T0


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, np.ndarray):
        return jsonfest(x.tolist())
    if isinstance(x, (complex, np.complexfloating)):
        return [jsonfest(float(x.real)), jsonfest(float(x.imag))]
    if isinstance(x, np.floating):
        x = float(x)
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, np.bool_):
        return bool(x)
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return x


class Budget:
    def __init__(self, sek):
        self.sek = sek
        self.entfallen = []

    def ok(self, was, reserve=0.0):
        if uhr() + reserve < self.sek:
            return True
        self.entfallen.append(f"{was} (bei {uhr():.0f} s)")
        return False


# ----------------------------------------------------------------------------------------------------------------------
# Profile -> Koeffizienten A, B, C
# ----------------------------------------------------------------------------------------------------------------------

def lin_aufbau(x, Om, r, amp, A, B, C, Rw, h, info):
    hp = float(r[1] - r[0])
    if abs(hp - 0.5 * h) > 1e-12:
        raise ValueError("Profil braucht Schritt h/2")
    J = len(r) - 1
    klein = np.nonzero(np.abs(amp) < THETA_RAND * abs(amp[0]))[0]
    j_r = int(klein[0]) if len(klein) else J
    j_r = min(max(j_r, int(math.ceil(20.0 / hp))), J)
    K = j_r // 2
    Km = max(2, min(K - 2, int(round(Rw / h))))
    j = 2 * K
    abw = max(abs(A[j] - (1.0 - Om * Om)), abs(B[j] - 2.0 * Om), abs(C[j]))
    return {"x": float(x), "Omega": float(Om), "h": h, "K": K, "Km": Km, "R": K * h, "r_m": Km * h, "R_w": float(Rw),
            "Al": [float(v) for v in A[:j + 1]], "Bl": [float(v) for v in B[:j + 1]], "Cl": [float(v) for v in C[:j + 1]],
            "rand_abw": float(abw), "info": info}


def profile_lin(modell, kap, xs, h, prot):
    """Profile fuer die Liste xs = Omega^2 (AFM: f = (x - 1 - kappa)/|kappa|; KG: omega^2); None = ungueltig."""
    hp = 0.5 * h
    t0 = uhr()
    aus = []
    if not xs:
        return aus
    if modell == "afm":
        fs = [(x - 1.0 - kap) / abs(kap) for x in xs]
        prs = AK.afm_profile([kap] * len(xs), fs, h, prot)
        for x, p in zip(xs, prs):
            if not p.get("gueltig"):
                aus.append(None)
                prot.append(f"Profil x = {x:.9f} (f = {p['f']:.6f}) ungueltig: {p.get('schiessen')} "
                            f"{p.get('ausgeschlossen', '')}")
                continue
            th = p["_th"]
            dth = AK.d1_fd4(th, hp, gerade=True)
            Vu, Vv = AK.V_uv(th, dth, 1.0 - p["Omega2"], kap)
            info = {"f": p["f"], "theta0": p["theta0"], "R_w": p["R_w"], "delta": p["delta"], "R_max": p["R_max"],
                    "newton_iter": p["newton_iter"], "K3_phase": p["K3_phase"], "K3_transl": p["K3_transl"]}
            aus.append(lin_aufbau(x, p["Omega"], p["_r"], th, 0.5 * (Vu + Vv), 2.0 * p["Omega"] * np.cos(th),
                                  0.5 * (Vu - Vv), p["R_w"], h, info))
    else:
        import nls2
        nls2.MODELL.clear()
        nls2.MODELL.update({"art": "qball", "beta": 0.5, "d": 3})
        prs = nls2.profile(list(xs), hp)
        for x, p in zip(xs, prs):
            f = p["phi"]
            S = f * f
            om = math.sqrt(x)
            Rw = AK.wandgeometrie(p["r"], f, S)[0]
            info = {"f0": p["f0"], "R_w": Rw, "R_aus": p["R_aus"], "grund": p["grund"], "f_anschluss": p["f_anschluss"]}
            aus.append(lin_aufbau(x, om, p["r"], f, 1.0 - 4.0 * S + 4.5 * S * S - x, np.full(len(f), 2.0 * om),
                                  -2.0 * S + 3.0 * S * S, Rw, h, info))
    prot.append(f"Profile ({modell}, {len(xs)} Stueck, h = {h}): {uhr() - t0:.1f} s")
    return aus


# ----------------------------------------------------------------------------------------------------------------------
# Lineare Loesungen (gemeinsamer Codepfad)
# ----------------------------------------------------------------------------------------------------------------------

def _rk4(y, A, B, C, rr, q2, j0, n, sg, hs, fak=None):
    """n RK4-Schritte fuer y'' = M y, M = [[A + B rho - rho^2, C], [C, A - B rho - rho^2]]; Koeffizienten auf dem
    Gitter h/2 (Index j0, j0 + sg, ...). y = (y1, y2, y1', y2'), vektorisiert ueber rho."""
    y1, y2, p1, p2 = y
    h2 = 0.5 * hs
    h6 = hs / 6.0
    j = j0
    a_ = A[j] - q2
    b_ = B[j] * rr
    m11a = a_ + b_
    m22a = a_ - b_
    ca = C[j]
    for _ in range(n):
        jm = j + sg
        je = jm + sg
        a_ = A[jm] - q2
        b_ = B[jm] * rr
        m11b = a_ + b_
        m22b = a_ - b_
        cb = C[jm]
        a_ = A[je] - q2
        b_ = B[je] * rr
        m11c = a_ + b_
        m22c = a_ - b_
        cc = C[je]
        k1p1 = m11a * y1 + ca * y2
        k1p2 = ca * y1 + m22a * y2
        t1 = y1 + h2 * p1
        t2 = y2 + h2 * p2
        k2y1 = p1 + h2 * k1p1
        k2y2 = p2 + h2 * k1p2
        k2p1 = m11b * t1 + cb * t2
        k2p2 = cb * t1 + m22b * t2
        t1 = y1 + h2 * k2y1
        t2 = y2 + h2 * k2y2
        k3y1 = p1 + h2 * k2p1
        k3y2 = p2 + h2 * k2p2
        k3p1 = m11b * t1 + cb * t2
        k3p2 = cb * t1 + m22b * t2
        t1 = y1 + hs * k3y1
        t2 = y2 + hs * k3y2
        k4y1 = p1 + hs * k3p1
        k4y2 = p2 + hs * k3p2
        k4p1 = m11c * t1 + cc * t2
        k4p2 = cc * t1 + m22c * t2
        y1 = y1 + h6 * (p1 + 2.0 * (k2y1 + k3y1) + k4y1)
        y2 = y2 + h6 * (p2 + 2.0 * (k2y2 + k3y2) + k4y2)
        p1 = p1 + h6 * (k1p1 + 2.0 * (k2p1 + k3p1) + k4p1)
        p2 = p2 + h6 * (k1p2 + 2.0 * (k2p2 + k3p2) + k4p2)
        if fak is not None:
            y1 = y1 * fak
            y2 = y2 * fak
            p1 = p1 * fak
            p2 = p2 * fak
        m11a, m22a, ca = m11c, m22c, cc
        j = je
    return y1, y2, p1, p2


def W_reell(L, rhos, chunk=6000):
    """W = L(y_a) + i L(y_b) bei reellem rho im Fenster (1 - Omega, 1 + Omega). Rueckgabe (La, Lb, Wachstum y)."""
    rho_all = np.atleast_1d(np.asarray(rhos, dtype=float))
    n_all = rho_all.size
    La = np.empty(n_all)
    Lb = np.empty(n_all)
    wa = np.empty(n_all)
    for s0 in range(0, n_all, chunk):
        rho = rho_all[s0:s0 + chunk]
        N = rho.size
        rr = np.concatenate([rho, rho])
        q2 = rr * rr
        p1 = np.zeros(2 * N)
        p1[N:] = 1.0
        p2 = np.zeros(2 * N)
        p2[:N] = 1.0
        y1, y2, p1, p2 = _rk4((np.zeros(2 * N), np.zeros(2 * N), p1, p2), L["Al"], L["Bl"], L["Cl"], rr, q2, 0,
                              L["Km"], 1, L["h"])
        kc = np.sqrt(1.0 - (rho - L["Omega"]) ** 2)
        z1, z2, zp1, zp2 = _rk4((np.ones(N), np.zeros(N), -kc, np.zeros(N)), L["Al"], L["Bl"], L["Cl"], rho, rho * rho,
                                2 * L["K"], L["K"] - L["Km"], -1, -L["h"], fak=np.exp(-kc * L["h"]))
        La[s0:s0 + N] = y1[:N] * zp1 - p1[:N] * z1 + y2[:N] * zp2 - p2[:N] * z2
        Lb[s0:s0 + N] = y1[N:] * zp1 - p1[N:] * z1 + y2[N:] * zp2 - p2[N:] * z2
        g = np.maximum.reduce([np.abs(y1), np.abs(y2), np.abs(p1), np.abs(p2)])
        wa[s0:s0 + N] = np.maximum(g[:N], g[N:])
    return La, Lb, wa


def W_multi(Ls, rho_listen):
    """W fuer mehrere Profile derselben Gitterstufe in einem Stapel (Spalte = (Profil, rho)). Koeffizienten bis zum
    groessten R mit den Aussenwerten (1 - Omega^2, 2 Omega, 0) verlaengert, gemeinsamer Anschluss r_m (Median R_w).
    Ergebnis = W_reell bis auf einen positiven Faktor je Spalte (andere R, r_m): gleiche Phase, gleiche Nullstellen."""
    h = Ls[0]["h"]
    Kx = max(L["K"] for L in Ls)
    Kmc = max(2, min(min(L["K"] for L in Ls) - 2, int(round(float(np.median([L["R_w"] for L in Ls])) / h))))
    n = 2 * Kx + 1
    Am = np.empty((len(Ls), n))
    Bm = np.empty((len(Ls), n))
    Cm = np.zeros((len(Ls), n))
    for p, L in enumerate(Ls):
        m = 2 * L["K"] + 1
        Am[p, :m], Bm[p, :m], Cm[p, :m] = L["Al"][:m], L["Bl"][:m], L["Cl"][:m]
        Am[p, m:] = 1.0 - L["Omega"] ** 2
        Bm[p, m:] = 2.0 * L["Omega"]
    pidx = np.concatenate([np.full(len(r_), p, dtype=int) for p, r_ in enumerate(rho_listen)])
    rho = np.concatenate([np.asarray(r_, dtype=float) for r_ in rho_listen])
    Om = np.array([Ls[p]["Omega"] for p in pidx])
    AT, BT, CT = Am[pidx].T.copy(), Bm[pidx].T.copy(), Cm[pidx].T.copy()     # (n, Spalten)
    N = rho.size
    rr = np.concatenate([rho, rho])
    A2, B2, C2 = np.concatenate([AT, AT], 1), np.concatenate([BT, BT], 1), np.concatenate([CT, CT], 1)
    p1 = np.zeros(2 * N)
    p1[N:] = 1.0
    p2 = np.zeros(2 * N)
    p2[:N] = 1.0
    y1, y2, p1, p2 = _rk4((np.zeros(2 * N), np.zeros(2 * N), p1, p2), A2, B2, C2, rr, rr * rr, 0, Kmc, 1, h)
    kc = np.sqrt(1.0 - (rho - Om) ** 2)
    z1, z2, zp1, zp2 = _rk4((np.ones(N), np.zeros(N), -kc, np.zeros(N)), AT, BT, CT, rho, rho * rho, 2 * Kx,
                            Kx - Kmc, -1, -h, fak=np.exp(-kc * h))
    La = y1[:N] * zp1 - p1[:N] * z1 + y2[:N] * zp2 - p2[:N] * z2
    Lb = y1[N:] * zp1 - p1[N:] * z1 + y2[N:] * zp2 - p2[N:] * z2
    aus, o = [], 0
    for r_ in rho_listen:
        aus.append((La[o:o + len(r_)], Lb[o:o + len(r_)]))
        o += len(r_)
    return aus


def _gs2(Z, N):
    a = np.stack([v[:N] for v in Z], 0)
    b = np.stack([v[N:] for v in Z], 0)
    a = a / np.sqrt(np.sum(np.abs(a) ** 2, 0))
    b = b - np.sum(np.conj(a) * b, 0) * a
    b = b / np.sqrt(np.sum(np.abs(b) ** 2, 0))
    return tuple(np.concatenate([a[k], b[k]]) for k in range(4))


def D_komplex(L, rhos, n_gs=4):
    """Normierte Anschlussdeterminante D(rho) = det[y_a, y_b, j1, j2](r_m) / (|y_a| |y_b|) bei komplexem rho."""
    rho = np.atleast_1d(np.asarray(rhos, dtype=complex))
    N = rho.size
    rr = np.concatenate([rho, rho])
    q2 = rr * rr
    z0 = np.zeros(2 * N, dtype=complex)
    p1 = z0.copy()
    p1[N:] = 1.0
    p2 = z0.copy()
    p2[:N] = 1.0
    y = _rk4((z0.copy(), z0.copy(), p1, p2), L["Al"], L["Bl"], L["Cl"], rr, q2, 0, L["Km"], 1, L["h"])
    kc = np.sqrt(1.0 - (rho - L["Omega"]) ** 2)
    q = np.sqrt((rho + L["Omega"]) ** 2 - 1.0)
    one, nul = np.ones(N, dtype=complex), np.zeros(N, dtype=complex)
    Z = (np.concatenate([one, nul]), np.concatenate([nul, one]), np.concatenate([-kc, nul]),
         np.concatenate([nul, 1j * q]))
    k = L["K"]
    rest = L["K"] - L["Km"]
    while rest > 0:
        n = min(n_gs, rest)
        Z = _rk4(Z, L["Al"], L["Bl"], L["Cl"], rr, q2, 2 * k, n, -1, -L["h"])
        k -= n
        rest -= n
        Z = _gs2(Z, N)
    M = np.empty((N, 4, 4), dtype=complex)
    for c, (v, sl) in enumerate(((y, slice(0, N)), (y, slice(N, 2 * N)), (Z, slice(0, N)), (Z, slice(N, 2 * N)))):
        col = np.stack([w[sl] for w in v], 1)
        if c < 2:
            col = col / np.sqrt(np.sum(np.abs(col) ** 2, 1))[:, None]
        M[:, :, c] = col
    return np.linalg.det(M)


def pole(L, starts, iters=25, tol=1e-11, delta=1e-7, schritt_max=0.01):
    rho = np.array(starts, dtype=complex)
    n = len(rho)
    konv = np.zeros(n, dtype=bool)
    it_n = np.zeros(n, dtype=int)
    for it in range(iters):
        akt = np.nonzero(~konv)[0]
        if len(akt) == 0:
            break
        e = rho[akt]
        D = D_komplex(L, np.concatenate([e, e + delta, e + 1j * delta]))
        m = len(akt)
        d0, dx, dy = D[:m], D[m:2 * m], D[2 * m:]
        j11, j21 = (dx - d0).real / delta, (dx - d0).imag / delta
        j12, j22 = (dy - d0).real / delta, (dy - d0).imag / delta
        dd = j11 * j22 - j12 * j21
        ok = np.isfinite(dd) & (dd != 0)
        dd = np.where(ok, dd, 1.0)
        st = np.where(ok, (-(j22 * d0.real - j12 * d0.imag) + 1j * (-(-j21 * d0.real + j11 * d0.imag))) / dd, 0.0)
        gross = np.abs(st) > schritt_max
        st = np.where(gross, st * schritt_max / np.maximum(np.abs(st), 1e-300), st)
        rho[akt] = e + st
        it_n[akt] = it + 1
        konv[akt] = ok & (np.abs(st) < tol)
    Dend = np.abs(D_komplex(L, rho)) if n else np.zeros(0)
    return rho, konv, Dend, it_n


# ----------------------------------------------------------------------------------------------------------------------
# Nullstellen von L(y_b), s, Umlauf
# ----------------------------------------------------------------------------------------------------------------------

def wurzeln(L, rho, La, Lb, n_fein=100, stufen=1):
    """Alle Vorzeichenwechsel von L(y_b) auf dem Raster, je ein Feinraster (Klammer / 100), dann W exakt an der
    Nullstelle (Sekante in der Endklammer). s = L(y_a) dort."""
    sg = np.sign(Lb)
    idx = np.nonzero(sg[:-1] * sg[1:] < 0)[0]
    kl = [(float(rho[i]), float(rho[i + 1]), float(Lb[i]), float(Lb[i + 1])) for i in idx]
    for _ in range(stufen):
        if not kl:
            break
        pts = np.concatenate([np.linspace(a, b, n_fein + 1)[1:-1] for a, b, _, _ in kl])
        _, lbs, _ = W_reell(L, pts)
        m = n_fein - 1
        neu = []
        for q, (a, b, fa, fb) in enumerate(kl):
            xs_ = np.concatenate([[a], pts[q * m:(q + 1) * m], [b]])
            fs_ = np.concatenate([[fa], lbs[q * m:(q + 1) * m], [fb]])
            for t in np.nonzero(np.sign(fs_[:-1]) * np.sign(fs_[1:]) < 0)[0]:
                neu.append((float(xs_[t]), float(xs_[t + 1]), float(fs_[t]), float(fs_[t + 1])))
        kl = neu
    if not kl:
        return []
    rts = [a - fa * (b - a) / (fb - fa) for a, b, fa, fb in kl]
    la, lb, _ = W_reell(L, rts)
    aus = []
    for (a, b, fa, fb), r_, sa, sb in zip(kl, rts, la, lb):
        aus.append({"rho": float(r_), "s": float(sa), "lb_rest": float(sb), "breite": float(b - a),
                    "richtung": 1 if fb > fa else -1, "steigung_lb": float((fb - fa) / (b - a))})
    return aus


def umlauf(W):
    W = np.asarray(W, dtype=complex)
    sp = np.angle(np.roll(W, -1) * np.conj(W))
    return float(sp.sum() / (2.0 * PI)), float(np.abs(sp).max()), int(np.argmax(np.abs(sp)))


def _spruenge(w):
    w = np.asarray(w, dtype=complex)
    return np.abs(np.angle(w[1:] * np.conj(w[:-1])))


def rechteck(modell, kap, h, xl, xr, rlo, rhi, Ll, Lr, prot, budget, links=None, rechts=None, mitte=None,
             n_rho=41, runden_x=8, runden_r=40, max_prof=60):
    """Umlaufzahl von W = L(y_a) + i L(y_b) auf dem Rand von [xl, xr] x [rlo, rhi] in (Omega^2, rho), gegen den
    Uhrzeigersinn (unten x steigt, rechts rho steigt, oben x faellt, links rho faellt). links/rechts: vorhandene
    rho-Seiten (rho-Liste aufsteigend von rlo bis rhi, W-Liste); mitte: vorhandene Zwischenprofile
    [(x, L, ecken)], ecken = (W(x, rlo), W(x, rhi)) oder None."""
    t0 = uhr()

    def seite(L, vorgabe):
        if vorgabe is not None:
            return [float(v) for v in vorgabe[0]], [complex(v) for v in vorgabe[1]]
        r_ = np.linspace(rlo, rhi, n_rho)
        la, lb, _ = W_reell(L, r_)
        return [float(v) for v in r_], [complex(a_, b_) for a_, b_ in zip(la, lb)]
    rl, wl = seite(Ll, links)
    rr_, wr = seite(Lr, rechts)
    xs = [xl, xr]
    wu = [wl[0], wr[0]]
    wo = [wl[-1], wr[-1]]
    luecken = []

    def einfuegen(neu):
        offen = [(x, L) for x, L, ecken in neu if L is not None and ecken is None]
        berechnet = {}
        if offen:
            for (x, L), (la, lb) in zip(offen, W_multi([L for _, L in offen], [[rlo, rhi]] * len(offen))):
                berechnet[x] = (complex(la[0], lb[0]), complex(la[1], lb[1]))
        for x, L, ecken in neu:
            if L is None:
                luecken.append(x)
                continue
            if ecken is None:
                ecken = berechnet[x]
            k = int(np.searchsorted(xs, x))
            xs.insert(k, x)
            wu.insert(k, ecken[0])
            wo.insert(k, ecken[1])
    if mitte:
        einfuegen([m for m in mitte if xl < m[0] < xr])
    n_prof = 0
    for _ in range(runden_x):
        sp = np.maximum(_spruenge(wu), _spruenge(wo))
        neu_x = [xs[i] + (xs[i + 1] - xs[i]) * q / 4.0 for i in np.nonzero(sp > SPRUNG)[0]
                 if not any(xs[i] < g < xs[i + 1] for g in luecken) for q in (1, 2, 3)]
        if not neu_x or n_prof + len(neu_x) > max_prof or not budget.ok("Rechteck: neue Profile", 30.0):
            break
        Ls = profile_lin(modell, kap, neu_x, h, prot)
        n_prof += len(neu_x)
        einfuegen([(x, L, None) for x, L in zip(neu_x, Ls)])
    for L, r_, w_ in ((Ll, rl, wl), (Lr, rr_, wr)):
        for _ in range(runden_r):
            sp = _spruenge(w_)
            idx = np.nonzero(sp > SPRUNG)[0]
            if len(idx) == 0 or not budget.ok("Rechteck: rho-Seite", 10.0):
                break
            mids = [0.5 * (r_[i] + r_[i + 1]) for i in idx]
            la, lb, _ = W_reell(L, mids)
            for i, m_, a_, b_ in sorted(zip(idx, mids, la, lb), reverse=True):
                r_.insert(i + 1, m_)
                w_.insert(i + 1, complex(a_, b_))
    pfad = wu + wr[1:] + wo[::-1][1:] + wl[::-1][1:-1]
    u, sprung, ks = umlauf(pfad)
    aufl = bool(sprung < SPRUNG and not luecken)
    # Gegenprobe ohne Phasenaufloesung: Vorzeichenwechsel von L(y_b) auf dem Weg, gewichtet mit sgn L(y_a) dort
    # (L(y_a) linear interpoliert); Umlauf = (1/2) sum sgn(L_a) * sgn(Delta L_b).
    P = np.asarray(pfad + pfad[:1])
    kr = 0.0
    for k in np.nonzero(np.sign(P[:-1].imag) * np.sign(P[1:].imag) < 0)[0]:
        t = P[k].imag / (P[k].imag - P[k + 1].imag)
        la = P[k].real + t * (P[k + 1].real - P[k].real)
        kr += 0.5 * np.sign(la) * np.sign(P[k + 1].imag - P[k].imag)
    seiten = {"unten": float(_spruenge(wu).max()), "oben": float(_spruenge(wo).max()),
              "rechts": float(_spruenge(wr).max()), "links": float(_spruenge(wl).max())}
    return {"x_lo": xl, "x_hi": xr, "rho_lo": rlo, "rho_hi": rhi, "umlauf_roh": u, "umlauf": int(round(u)),
            "umlauf_kreuzung": float(kr), "max_sprung_seiten": seiten,
            "max_sprung": sprung, "aufgeloest": aufl, "punkte": len(pfad), "x_punkte": len(xs),
            "rho_punkte_links": len(rl), "rho_punkte_rechts": len(rr_), "neue_profile": n_prof,
            "luecken_ungueltig": luecken, "min_absW": float(min(abs(w) for w in pfad)),
            "median_absW": float(np.median(np.abs(pfad))), "zeit": uhr() - t0}


# ----------------------------------------------------------------------------------------------------------------------
# Reihen, Aeste, Lokalisierung
# ----------------------------------------------------------------------------------------------------------------------

def fenster(x):
    om = math.sqrt(x)
    return 1.0 - om + RAND, 1.0 + om - RAND


def reihe(L, n1, n2, dicht, extra):
    lo, hi = fenster(L["x"])
    teile = [np.linspace(lo, hi, n1)]
    dlo, dhi = max(lo, dicht[0]), min(hi, dicht[1])
    if n2 > 0 and dhi > dlo:
        teile.append(np.linspace(dlo, dhi, n2))
    teile.append(np.array([e for e in extra if lo <= e <= hi]))
    rho = np.unique(np.concatenate(teile))
    t0 = uhr()
    La, Lb, wa = W_reell(L, rho)
    t1 = uhr()
    wz = wurzeln(L, rho, La, Lb)
    absW = np.hypot(La, Lb)
    med = float(np.median(absW))
    for w in wz:
        w["s_rel"] = w["s"] / med
    return {"x": L["x"], "Omega": L["Omega"], "fenster": [lo, hi], "R": L["R"], "r_m": L["r_m"], "K": L["K"],
            "R_w": L["R_w"], "rand_abw": L["rand_abw"], "info": L["info"], "n_rho": int(rho.size),
            "drho_max": float(np.max(np.diff(rho))), "wachstum_max": float(np.max(wa)), "median_absW": med,
            "min_absW": float(np.min(absW)), "wurzeln": wz, "zeit_abtastung": t1 - t0, "zeit_wurzeln": uhr() - t1,
            "_rho": rho, "_La": La, "_Lb": Lb}


def paaren(w1, w2, tol):
    """Wechselseitig naechste Nullstellen gleicher Richtung (Vorzeichen von dL(y_b)/drho), |Abstand| < tol."""
    paare = []
    for i, a in enumerate(w1):
        k2 = [(abs(b["rho"] - a["rho"]), j) for j, b in enumerate(w2) if b["richtung"] == a["richtung"]]
        if not k2:
            continue
        d, j = min(k2)
        if d > tol:
            continue
        k1 = [(abs(c["rho"] - w2[j]["rho"]), k) for k, c in enumerate(w1) if c["richtung"] == w2[j]["richtung"]]
        if min(k1)[1] != i:
            continue
        paare.append((i, j))
    return paare


def lokalisieren(modell, kap, h, xa, ra, sa, xb, rb, sb, richtung, prot, budget, iters=10, tol_x=1e-7):
    """Illinois in x = Omega^2 auf s(x) entlang des Astes L(y_b) = 0 (neue Profile, rho lokal fein)."""
    schritte = []
    xa0, xb0 = xa, xb
    for it in range(iters):
        if not budget.ok(f"Lokalisierung Schritt {it}", 40.0):
            break
        xn = xb - sb * (xb - xa) / (sb - sa) if sb != sa else 0.5 * (xa + xb)
        lo_, hi_ = min(xa, xb), max(xa, xb)
        if not (lo_ < xn < hi_):
            xn = 0.5 * (xa + xb)
        rp = ra + (rb - ra) * (xn - xa) / (xb - xa)
        L = profile_lin(modell, kap, [xn], h, prot)[0]
        if L is None:
            schritte.append({"x": xn, "fehler": "Profil ungueltig"})
            break
        flo, fhi = fenster(xn)
        w = max(4.0 * abs(rb - ra), 2e-3)
        grid = np.linspace(max(flo, rp - w), min(fhi, rp + w), 401)
        La, Lb, _ = W_reell(L, grid)
        wz = [v for v in wurzeln(L, grid, La, Lb) if v["richtung"] == richtung]
        if not wz:
            schritte.append({"x": xn, "rho_pred": rp, "fehler": "Ast verloren"})
            break
        v = min(wz, key=lambda q: abs(q["rho"] - rp))
        sn, rn = v["s"], v["rho"]
        schritte.append({"x": xn, "rho": rn, "s": sn, "rho_pred": rp, "lb_rest": v["lb_rest"]})
        if sn * sb < 0:
            xa, sa, ra = xb, sb, rb
        else:
            sa = 0.5 * sa
        xb, sb, rb = xn, sn, rn
        if abs(xb - xa) < tol_x or sn == 0.0:
            break
    if sb == sa:
        xs_, rs_ = xb, rb
    else:
        t = sb / (sb - sa)
        xs_ = xb + t * (xa - xb)
        rs_ = rb + t * (ra - rb)
    steig = (rb - ra) / (xb - xa) if xb != xa else 0.0
    return {"x_stern": float(xs_), "rho_stern": float(rs_), "klammer_x": [float(min(xa, xb)), float(max(xa, xb))],
            "klammer_breite": float(abs(xb - xa)), "steigung_rho_x": float(steig), "schritte": schritte,
            "start": [xa0, xb0]}


# ----------------------------------------------------------------------------------------------------------------------
# Kommando familie
# ----------------------------------------------------------------------------------------------------------------------

def ohne_arrays(rw):
    return {k: v for k, v in rw.items() if not k.startswith("_")}


def ecken_aus(rw, lo, hi):
    """W(x, rlo) und W(x, rhi) aus einer Reihe, die diese rho-Werte exakt enthaelt; sonst None."""
    if rw is None:
        return None
    r = rw["_rho"]
    i1 = int(np.argmin(np.abs(r - lo)))
    i2 = int(np.argmin(np.abs(r - hi)))
    if abs(r[i1] - lo) > 1e-14 or abs(r[i2] - hi) > 1e-14:
        return None
    return (complex(rw["_La"][i1], rw["_Lb"][i1]), complex(rw["_La"][i2], rw["_Lb"][i2]))


def cmd_familie(a, erg, zeilen, sichern, npz):
    budget = Budget(a.budget)
    modell = a.modell
    kap = a.kappa
    h = a.h
    if modell == "afm":
        fs = [float(v) for v in a.f.split(",")] if a.f else FS
        xs = sorted(1.0 + kap + f * abs(kap) for f in fs)
    else:
        xs = sorted(float(v) for v in a.x.split(",")) if a.x else KG_X
    erg.update({"modell": modell, "kappa": kap if modell == "afm" else None, "h": h, "x_mitglieder": xs})
    prot = []
    Ls = profile_lin(modell, kap, xs, h, prot)
    zeilen += prot
    prot.clear()
    sichern()
    fen = [fenster(x) for x in xs]
    # 1. Mitglieder: dichte rho-Abtastung, Nullstellen von L(y_b), s
    reihen = []
    erg["mitglieder"] = reihen
    for i, (x, L) in enumerate(zip(xs, Ls)):
        if L is None:
            reihen.append({"x": x, "gueltig": False})
            sichern()
            continue
        extra = list(fen[i - 1]) if i > 0 else []
        rw = reihe(L, a.n1, a.n2, (a.dicht_lo, a.dicht_hi), extra)
        rw["gueltig"] = True
        rw["mitglied"] = True
        reihen.append(rw)
        npz[f"m{i}_rho"], npz[f"m{i}_La"], npz[f"m{i}_Lb"] = rw["_rho"], rw["_La"], rw["_Lb"]
        zeilen.append(f"Mitglied x = Omega^2 = {x:.6f} (Omega {L['Omega']:.6f}): R = {L['R']:.2f}, r_m = {L['r_m']:.2f}, "
                      f"Rand-Abw. {L['rand_abw']:.1e}, {rw['n_rho']} rho-Punkte (max Abstand {rw['drho_max']:.1e}), "
                      f"Wachstum {rw['wachstum_max']:.1e}, {len(rw['wurzeln'])} Nullstellen von L(y_b): "
                      + "; ".join(f"rho {w['rho']:.7f} s {w['s']:+.3e} (rel {w['s_rel']:+.1e}, {w['richtung']:+d})"
                                  for w in rw["wurzeln"]) + f"; {rw['zeit_abtastung']:.1f} + {rw['zeit_wurzeln']:.1f} s")
        sichern()
    # 2. Zwischenreihen (n_mid je Streifen, gleichabstaendig): Profile fuer die Omega^2-Seiten und feinere Aeste
    zw = []
    for i in range(len(xs) - 1):
        if Ls[i] is None or Ls[i + 1] is None:
            continue
        for k in range(1, a.n_mid + 1):
            zw.append((i, xs[i] + (xs[i + 1] - xs[i]) * k / (a.n_mid + 1)))
    zw_reihen = {}
    if zw and budget.ok("Zwischenreihen", 60.0):
        Lz = profile_lin(modell, kap, [x for _, x in zw], h, prot)
        zeilen += prot
        prot.clear()
        for (i, x), L in zip(zw, Lz):
            if L is None:
                zw_reihen.setdefault(i, []).append((x, None, None))
                continue
            if not budget.ok("Zwischenreihe", 30.0):
                zw_reihen.setdefault(i, []).append((x, L, None))
                continue
            rw = reihe(L, a.n_zw, 0, (a.dicht_lo, a.dicht_hi), list(fen[i]))
            rw["gueltig"] = True
            rw["mitglied"] = False
            rw["streifen"] = i
            zw_reihen.setdefault(i, []).append((x, L, rw))
        erg["zwischenreihen"] = [ohne_arrays(rw) for i in sorted(zw_reihen) for (_, _, rw) in zw_reihen[i]
                                 if rw is not None]
        zeilen.append(f"Zwischenreihen: {len(zw)} Profile, {len(erg['zwischenreihen'])} abgetastet ({a.n_zw} rho-Punkte)")
        sichern()
    # 3. Streifen-Umlauf zwischen benachbarten Mitgliedern
    streifen = []
    erg["streifen"] = streifen
    for i in range(len(xs) - 1):
        if Ls[i] is None or Ls[i + 1] is None:
            streifen.append({"i": i, "fehler": "Profil ungueltig"})
            continue
        if not budget.ok(f"Streifen {i}", 30.0):
            streifen.append({"i": i, "fehler": "Zeit"})
            sichern()
            continue
        lo, hi = fen[i]
        r1, La1, Lb1 = reihen[i]["_rho"], reihen[i]["_La"], reihen[i]["_Lb"]
        r2, La2, Lb2 = reihen[i + 1]["_rho"], reihen[i + 1]["_La"], reihen[i + 1]["_Lb"]
        m2 = (r2 >= lo - 1e-15) & (r2 <= hi + 1e-15)
        mitte = [(x, L, ecken_aus(rw, lo, hi)) for (x, L, rw) in zw_reihen.get(i, [])]
        e = rechteck(modell, kap, h, xs[i], xs[i + 1], lo, hi, Ls[i], Ls[i + 1], prot, budget,
                     links=(r1, La1 + 1j * Lb1), rechts=(r2[m2], La2[m2] + 1j * Lb2[m2]), mitte=mitte)
        zeilen += prot
        prot.clear()
        e["i"] = i
        streifen.append(e)
        zeilen.append(f"Streifen {i}: Omega^2 {xs[i]:.6f} .. {xs[i + 1]:.6f}, rho {lo:.4f} .. {hi:.4f}: Umlauf "
                      f"{e['umlauf_roh']:+.4f} (Kreuzungszaehlung {e['umlauf_kreuzung']:+.1f}), groesster Sprung "
                      f"{e['max_sprung']:.3f} rad {json.dumps({k: round(v, 3) for k, v in e['max_sprung_seiten'].items()})}, "
                      f"aufgeloest {e['aufgeloest']}, {e['punkte']} Punkte ({e['x_punkte']} in Omega^2, "
                      f"{e['neue_profile']} neue Profile), min|W|/median {e['min_absW'] / e['median_absW']:.1e}, "
                      f"{e['zeit']:.1f} s")
        sichern()
    # 4. Aeste und Vorzeichenwechsel von s (Mitglieder und Zwischenreihen, nach Omega^2 geordnet)
    alle = [rw for rw in reihen if rw.get("gueltig")]
    for i in zw_reihen:
        alle += [rw for (_, _, rw) in zw_reihen[i] if rw is not None]
    alle.sort(key=lambda q: q["x"])
    wechsel = []
    ungepaart = []
    for r1, r2 in zip(alle, alle[1:]):
        pa = paaren(r1["wurzeln"], r2["wurzeln"], a.ast_tol)
        gi = {i for i, _ in pa}
        gj = {j for _, j in pa}
        ungepaart.append({"x1": r1["x"], "x2": r2["x"], "n1": len(r1["wurzeln"]), "n2": len(r2["wurzeln"]),
                          "gepaart": len(pa), "rho_ungepaart_1": [w["rho"] for k, w in enumerate(r1["wurzeln"]) if k not in gi],
                          "rho_ungepaart_2": [w["rho"] for k, w in enumerate(r2["wurzeln"]) if k not in gj]})
        for i, j in pa:
            w1, w2 = r1["wurzeln"][i], r2["wurzeln"][j]
            if w1["s"] * w2["s"] < 0:
                wechsel.append({"x1": r1["x"], "rho1": w1["rho"], "s1": w1["s"], "x2": r2["x"], "rho2": w2["rho"],
                                "s2": w2["s"], "richtung": w1["richtung"]})
    erg["paarung"] = ungepaart
    erg["vorzeichenwechsel"] = wechsel
    zeilen.append(f"Vorzeichenwechsel von s ({len(alle)} Reihen, Ast-Toleranz {a.ast_tol}): {len(wechsel)}")
    for w in wechsel:
        zeilen.append(f"  zwischen Omega^2 {w['x1']:.7f} (rho {w['rho1']:.6f}, s {w['s1']:+.3e}) und {w['x2']:.7f} "
                      f"(rho {w['rho2']:.6f}, s {w['s2']:+.3e})")
    n_ung = sum(len(u["rho_ungepaart_1"]) + len(u["rho_ungepaart_2"]) for u in ungepaart)
    zeilen.append(f"Ungepaarte Nullstellen (alle Reihenpaare zusammen): {n_ung}")
    sichern()
    # 5. Lokalisierung und kleines Rechteck je Vorzeichenwechsel
    kand = []
    erg["kandidaten"] = kand
    for w in wechsel[:a.max_kand]:
        if not budget.ok("Lokalisierung", 90.0):
            kand.append({"wechsel": w, "fehler": "Zeit"})
            break
        lok = lokalisieren(modell, kap, h, w["x1"], w["rho1"], w["s1"], w["x2"], w["rho2"], w["s2"], w["richtung"],
                           prot, budget)
        zeilen += prot
        prot.clear()
        e = {"wechsel": w, "lokal": lok}
        kand.append(e)
        zeilen.append(f"Lokalisiert: Omega*^2 = {lok['x_stern']:.8f}, rho* = {lok['rho_stern']:.8f} (Klammer "
                      f"{lok['klammer_breite']:.1e}, {len(lok['schritte'])} Schritte)")
        sichern()
        if not budget.ok("Rechteck", 60.0):
            e["rechteck"] = {"fehler": "Zeit"}
            continue
        dx = a.rdx
        drho = min(max(a.rdrho, 3.0 * abs(lok["steigung_rho_x"]) * dx), 0.02)
        xc, rc = lok["x_stern"], lok["rho_stern"]
        rlo, rhi = max(rc - drho, fenster(xc - dx)[0]), min(rc + drho, fenster(xc - dx)[1])
        Lr = profile_lin(modell, kap, [xc - dx, xc + dx] + [xc + dx * (2.0 * k / (a.r_nx - 1) - 1.0)
                                                           for k in range(1, a.r_nx - 1)], h, prot)
        zeilen += prot
        prot.clear()
        if Lr[0] is None or Lr[1] is None:
            e["rechteck"] = {"fehler": "Profil ungueltig"}
            continue
        mitte = [(xc + dx * (2.0 * k / (a.r_nx - 1) - 1.0), L, None) for k, L in zip(range(1, a.r_nx - 1), Lr[2:])]
        ru = rechteck(modell, kap, h, xc - dx, xc + dx, rlo, rhi, Lr[0], Lr[1], prot, budget, mitte=mitte)
        zeilen += prot
        prot.clear()
        e["rechteck"] = ru
        zeilen.append(f"  Rechteck Omega^2 {xc - dx:.7f} .. {xc + dx:.7f}, rho {rlo:.6f} .. {rhi:.6f}: Umlauf "
                      f"{ru['umlauf_roh']:+.4f} (Kreuzungszaehlung {ru['umlauf_kreuzung']:+.1f}), groesster Sprung "
                      f"{ru['max_sprung']:.3f} rad, aufgeloest {ru['aufgeloest']}, "
                      f"{ru['punkte']} Punkte, min|W|/median {ru['min_absW'] / ru['median_absW']:.1e}")
        sichern()
    # 6. Pole an den Nullstellen von L(y_b) der Mitglieder (Breiten), soweit die Zeit reicht
    if a.pole == "ja":
        for i, (rw, L) in enumerate(zip(reihen, Ls)):
            if not rw.get("gueltig") or not rw["wurzeln"]:
                continue
            if not budget.ok(f"Pole Mitglied {i}", 60.0):
                rw["pole_fehler"] = "Zeit"
                continue
            t0 = uhr()
            # Schwellennahe Nullstellen (rho < 1 - Omega + 0,02) ausgelassen: dort laeuft Newton weg (Rauchtest)
            ws = [w for w in rw["wurzeln"] if w["rho"] > 1.0 - rw["Omega"] + 0.02]
            if not ws:
                continue
            st = [complex(w["rho"], -1e-6) for w in ws]
            rho_p, konv, absd, itn = pole(L, st, iters=15)
            for w, p_, k_, d_, n_ in zip(ws, rho_p, konv, absd, itn):
                w["pol"] = complex(p_)
                w["Gamma"] = float(-p_.imag)
                w["pol_konvergiert"] = bool(k_)
                w["pol_absD"] = float(d_)
                w["pol_iter"] = int(n_)
            rw["zeit_pole"] = uhr() - t0
            zeilen.append(f"Pole x = {rw['x']:.6f} ({rw['zeit_pole']:.1f} s): " + "; ".join(
                f"{w['pol'].real:.7f} {w['pol'].imag:+.2e}i ({'k' if w['pol_konvergiert'] else 'n'})" for w in ws))
            sichern()
    erg["budget_entfallen"] = budget.entfallen


# ----------------------------------------------------------------------------------------------------------------------
# Kommando auswertung (bindende Regel aus KARTE.md)
# ----------------------------------------------------------------------------------------------------------------------

def cmd_auswertung(a, erg, zeilen, sichern, npz):
    laeufe = []
    for p in sorted(glob.glob(os.path.join(a.aus, "*.json"))):
        if os.path.basename(p).startswith("auswertung"):
            continue
        d = json.load(open(p))
        if "modell" in d and "mitglieder" in d:
            d["_datei"] = os.path.basename(p)
            laeufe.append(d)
    zeilen.append(f"Auswertung: {len(laeufe)} Laeufe: " + ", ".join(d["_datei"] for d in laeufe))

    def treffer(d):
        aus = []
        for k in d.get("kandidaten", []):
            r = k.get("rechteck", {})
            if "lokal" in k and "umlauf" in r:
                aus.append({"x": k["lokal"]["x_stern"], "rho": k["lokal"]["rho_stern"], "umlauf": r["umlauf"],
                            "umlauf_roh": r["umlauf_roh"], "aufgeloest": r["aufgeloest"], "datei": d["_datei"]})
        return aus
    # Positivkontrolle
    kg = {d["h"]: d for d in laeufe if d["modell"] == "kg"}
    pk = {}
    for h, d in sorted(kg.items()):
        ok = [t for t in treffer(d) if abs(t["x"] - KG_ZIEL[0]) < 1e-4 and abs(t["rho"] - KG_ZIEL[1]) < 1e-4
              and t["aufgeloest"] and abs(t["umlauf"]) == 1]
        pk[h] = {"treffer": treffer(d), "bestanden": bool(ok)}
        zeilen.append(f"Positivkontrolle h = {h}: {'bestanden' if ok else 'VERFEHLT'}; Treffer: {treffer(d)}")
    pk_ok = len(pk) >= 2 and all(v["bestanden"] for v in pk.values())
    erg["positivkontrolle"] = {"stufen": pk, "bestanden": pk_ok}
    # AFM-Familie
    afm = [d for d in laeufe if d["modell"] == "afm"]
    kaps = sorted({d["kappa"] for d in afm})
    hs = sorted({d["h"] for d in afm})
    gesehen = []
    irgendwas = []
    tab = []
    for kap in kaps:
        ds = {}
        for d in afm:
            if d["kappa"] == kap:
                ds.setdefault(d["h"], []).append(d)     # Teilaufrufe (Haelften) je Stufe zusammenfassen
        for h, dl in sorted(ds.items()):
            st = [s for d in dl for s in d.get("streifen", []) if "umlauf" in s]
            st_n0 = [s for s in st if s["umlauf"] != 0]
            st_unaufl = [s for s in st if not s["aufgeloest"]]
            st_fehl = [s for d in dl for s in d.get("streifen", []) if "umlauf" not in s]
            vw = [w for d in dl for w in d.get("vorzeichenwechsel", [])]
            rk = [t for d in dl for t in treffer(d) if t["umlauf"] != 0]
            mx = {round(m["x"], 12) for d in dl for m in d.get("mitglieder", []) if m.get("gueltig")}
            ung = [m["x"] for d in dl for m in d.get("mitglieder", []) if not m.get("gueltig")]
            tab.append({"kappa": kap, "h": h, "dateien": [d["_datei"] for d in dl], "mitglieder_gueltig": len(mx),
                        "streifen": len(st), "streifen_umlauf_ungleich_0": len(st_n0),
                        "streifen_nicht_aufgeloest": len(st_unaufl), "streifen_fehlend": len(st_fehl),
                        "vorzeichenwechsel": len(vw), "rechtecke_ungleich_0": rk})
            if st_n0 or vw or rk:
                irgendwas.append((kap, h))
            if st_unaufl or st_fehl or len(mx) < 7 or len(st) < 6 or ung:
                irgendwas.append((kap, h, "Raster unvollstaendig oder nicht aufgeloest"))
        if len(ds) >= 2:
            h1, h2 = sorted(ds)[:2]
            for t1 in [t for d in ds[h1] for t in treffer(d)]:
                for t2 in [t for d in ds[h2] for t in treffer(d)]:
                    if (t1["aufgeloest"] and t2["aufgeloest"] and abs(t1["umlauf"]) == 1 and abs(t2["umlauf"]) == 1
                            and abs(t1["x"] - t2["x"]) < 1e-3 and abs(t1["rho"] - t2["rho"]) < 1e-3):
                        gesehen.append({"kappa": kap, "h": [h1, h2], "t1": t1, "t2": t2})
    erg["tabelle"] = tab
    erg["gesehen"] = gesehen
    if not pk_ok:
        ausgang = "nicht auswertbar (Positivkontrolle verfehlt)"
    elif gesehen:
        ausgang = "Stille Stelle gesehen"
    elif not irgendwas and len(kaps) == 3 and len(hs) == 2:
        ausgang = "Auf dem Raster nicht gesehen"
    else:
        ausgang = "Unentschieden"
    erg["ausgang"] = ausgang
    erg["hinweise"] = [list(v) for v in irgendwas]
    for t in tab:
        zeilen.append("  " + json.dumps(jsonfest(t)))
    zeilen.append(f"Ausgang nach der bindenden Regel: {ausgang}; Hinweise: {irgendwas}")


def argumente():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kommando", choices=["familie", "auswertung"])
    ap.add_argument("--modell", choices=["afm", "kg"], default="afm")
    ap.add_argument("--kappa", type=float, default=-0.2)
    ap.add_argument("--f", type=str, default="")
    ap.add_argument("--x", type=str, default="")
    ap.add_argument("--h", type=float, default=0.02)
    ap.add_argument("--n1", type=int, default=4000)
    ap.add_argument("--n2", type=int, default=2000)
    ap.add_argument("--dicht-lo", type=float, default=1.6)
    ap.add_argument("--dicht-hi", type=float, default=1.8)
    ap.add_argument("--n-mid", type=int, default=2)
    ap.add_argument("--n-zw", type=int, default=1500)
    ap.add_argument("--ast-tol", type=float, default=0.3)
    ap.add_argument("--max-kand", type=int, default=4)
    ap.add_argument("--rdx", type=float, default=4e-4)
    ap.add_argument("--rdrho", type=float, default=2e-3)
    ap.add_argument("--r-nx", type=int, default=5)
    ap.add_argument("--pole", choices=["ja", "nein"], default="ja")
    ap.add_argument("--budget", type=float, default=540.0)
    ap.add_argument("--aus", type=str, default="aus")
    ap.add_argument("--name", type=str, default="")
    return ap.parse_args()


def main():
    a = argumente()
    name = a.name or a.kommando
    os.makedirs(a.aus, exist_ok=True)
    zeilen = [f"afm_bic.py {a.kommando} ({name}), Start {jetzt()}", "Argumente: " + json.dumps(vars(a))]
    erg = {"argumente": vars(a), "start": jetzt()}
    npz = {}

    def sichern():
        e = dict(erg)
        e["mitglieder"] = [ohne_arrays(m) for m in erg.get("mitglieder", [])]
        e["stand"] = jetzt()
        e["laufzeit_bisher"] = uhr()
        tmp = os.path.join(a.aus, f".{name}.json.tmp")
        with open(tmp, "w") as fh:
            json.dump(jsonfest(e), fh, indent=1)
        os.replace(tmp, os.path.join(a.aus, f"{name}.json"))
        with open(os.path.join(a.aus, f"{name}.txt"), "w") as fh:
            fh.write("\n".join(zeilen) + "\n")
    rc = 0
    try:
        {"familie": cmd_familie, "auswertung": cmd_auswertung}[a.kommando](a, erg, zeilen, sichern, npz)
    except Exception:
        import traceback
        zeilen.append("FEHLER: " + traceback.format_exc())
        erg["fehler"] = traceback.format_exc()
        rc = 1
    zeilen.append(f"Ende {jetzt()}, Laufzeit {uhr():.1f} s")
    erg["ende"] = jetzt()
    erg["laufzeit"] = uhr()
    sichern()
    if npz:
        np.savez_compressed(os.path.join(a.aus, f"{name}-abtastung.npz"), **npz)
    print("\n".join(zeilen))
    return rc


if __name__ == "__main__":
    sys.exit(main())
