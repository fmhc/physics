#!/usr/bin/env python3
"""Runde 8 (runden-v3), Karte GF-BIC: Spektrum der zweiten Komponente psi_2 der Gesamtformel (N = 2, J = 1),
linearisiert um den einkomponentigen Q-Ball psi_1 = f(r) e^{-i omega t}. Explorativ. Plan: PLAN.md (gleicher Ordner).
Code begonnen 2026-09-30 06:18:10 CEST (date).

Modell (gesamtformel-20260921/KANDIDAT.md): L = sum_a (|d_t psi_a|^2 - |grad psi_a|^2) - U(S) + g J Re[(psi_1^* psi_2)^2],
U = S - S^2 + beta S^3, beta = 1/2. psi_2 = e^{-i omega t} (u e^{-i nu t} + v^* e^{i nu^* t}), A = r u, B = r v (l = 0):
    A'' = [dp - (omega + nu)^2] A + sp B,  B'' = sp A + [dp - (omega - nu)^2] B
    psi_2: dp = U'(S) = 1 - 2S + 3 beta S^2, sp = -g J S
    psi_1 (N = 1, Kontrolle): dp = U' + S U'' = 1 - 4S + 9 beta S^2, sp = S U'' = -2S + 6 beta S^2
Konvention wie resonanz3d.py: Im nu < 0 = abklingend (Resonanz), Im nu > 0 = anwachsend (Instabilitaet).

Loeser: resonanz3d.py (Runde 6), unveraendert importiert: Profil, Verbundmatrix-Determinante det(), newton(), illinois().
Eigener Teil: psi_2-Koeffizienten (auch mit g je Stapelelement), FD-Kasten (quadratisches Eigenwertproblem, linearisiert),
Zwei-Moden-Formel, Floquet-Monodromie mit der Atmungsmode als Pumpe, Ueberlappintegral des Gegenlaeufers (Frage 3).
Kommandos: rauch | spektrum | kontrolle1 | floquet | ueberlapp
"""
import argparse
import cmath
import datetime
import hashlib
import json
import math
import os
import sys
import time
import traceback

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")          # ein Kern (CPUQuota 100 % der Unit)

import numpy as np  # noqa: E402
import scipy.linalg as sla
import scipy.sparse as sps
import scipy.sparse.linalg as spla
import torch

HIER = os.path.dirname(os.path.abspath(__file__))
R3_PFAD = None
for _p in (HIER, os.path.normpath(os.path.join(HIER, "..", "..", "RUNDE-06", "resonanz3d"))):
    if os.path.isfile(os.path.join(_p, "resonanz3d.py")):
        sys.path.insert(0, _p)
        R3_PFAD = os.path.join(_p, "resonanz3d.py")
        break
import resonanz3d as R3  # noqa: E402

F64, C128 = torch.float64, torch.complex128
BETA = 0.5
JK = 1.0                      # J_12
T0 = time.perf_counter()
STELLEN = {"P1": (0.797677, 1.744618), "P2": (0.685129, None), "P3": (0.631449, 1.652588),
           "P4": (0.601422, 1.628113), "P5": (0.582417, 1.611309)}
N1_POL_07 = complex(1.7018102, -1.468e-3)     # RUNDE-06 pol07: 1,7018102865 - 1,468e-3 i (h = 0,02)


def uhr():
    return time.perf_counter() - T0


def jetzt():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def sha256(pfad):
    h = hashlib.sha256()
    with open(pfad, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def fz(z, n=10):
    return f"{z.real:.{n}f} {'-' if z.imag < 0 else '+'} {abs(z.imag):.4e} i"


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, (complex, np.complexfloating)):
        return [float(x.real), float(x.imag)]
    if isinstance(x, (np.floating,)):
        x = float(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return x


class Budget:
    def __init__(self, sek):
        self.sek = sek
        self.abgebrochen = []

    def ok(self, was, reserve=0.0):
        if uhr() + reserve < self.sek:
            return True
        self.abgebrochen.append(f"{was} (bei {uhr():.0f} s)")
        print(f"ZEIT: {was} entfaellt ({uhr():.0f} s von {self.sek:.0f} s)", flush=True)
        return False


def U1(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S * S


def U2(S):
    return -2.0 + 6.0 * BETA * S


def koeff(art, S, g):
    """(dp, sp) als Funktion von S (numpy oder float)."""
    if art == "psi2":
        return U1(S), -g * JK * S
    if art == "psi1":
        return 1.0 - 4.0 * S + 9.0 * BETA * S * S, -2.0 * S + 6.0 * BETA * S * S
    if art == "frei":
        return 1.0 + 0.0 * S, 0.0 * S
    raise ValueError(art)


# ================================================================ Profil, Momente, Zwei-Moden-Formel

def profil_momente(w2, hp, dev):
    t0 = uhr()
    prof = R3.profil(w2, 3.0, BETA, hp, dev)
    n = int(R3.radius_wo(prof, 1e-13 * prof["f0"]) / hp) + 2
    f, _ = R3.f_werte(prof, n)
    f = np.array(f)
    r = hp * np.arange(n)
    w = np.full(n, hp)
    w[0] = w[-1] = 0.5 * hp
    N2 = float(np.sum(w * f ** 2 * r ** 2))
    N4 = float(np.sum(w * f ** 4 * r ** 2))
    return prof, {"w2": w2, "omega": math.sqrt(w2), "hp": hp, "S0": prof["f0"] ** 2, "N2": N2, "N4": N4,
                  "kappa": N4 / N2, "R_halb": R3.r_halb(prof), "r_cut": prof["r_cut"], "sek_profil": uhr() - t0,
                  "Q": 8.0 * math.pi * math.sqrt(w2) * N2}


def lambda2(w2, kappa, g):
    x = g * JK * kappa
    return math.sqrt(max(0.0, -2.0 * w2 + math.sqrt(4.0 * w2 * w2 + x * x)))


# ================================================================ Schiessen (Verbundmatrix aus resonanz3d)

def basis(prof, h, f_rand, dev):
    """Geometrie und S auf dem Halbgitter wie R3.lin_aufbau; Koeffizienten spaeter je Stapelelement."""
    lin = R3.lin_aufbau(prof, h, f_rand)
    K = lin["K"]
    f, _ = R3.f_werte(prof, 2 * K + 1)
    S = torch.tensor(f, dtype=F64, device=dev) ** 2
    s0 = prof["f0"] ** 2
    S2 = 2.0 * prof["f0"] * prof["f2"]
    return {"h": h, "K": K, "Km": lin["Km"], "R_aus": lin["R_aus"], "r_m": lin["r_m"], "omega": lin["omega"],
            "cf": lin["cf"], "S": S, "s0": s0, "S2": S2, "dev": dev, "f_rand": f_rand}


def lin_g(B, art, gs):
    """lin fuer R3.det mit eigenem g je Stapelelement (dv, sv als (2K+1, n)-Tensoren)."""
    dev = B["dev"]
    g = torch.tensor([float(x) for x in gs], dtype=F64, device=dev)
    n = g.numel()
    S = B["S"].unsqueeze(1)
    if art == "psi2":
        dv = (1.0 - 2.0 * S + 3.0 * BETA * S * S).expand(-1, n)
        sv = -JK * S * g.unsqueeze(0)
        s0, S2 = B["s0"], B["S2"]
        d0 = torch.full((n,), 1.0 - 2.0 * s0 + 3.0 * BETA * s0 * s0, dtype=F64, device=dev)
        d2 = torch.full((n,), (-2.0 + 6.0 * BETA * s0) * S2, dtype=F64, device=dev)
        reihe = (d0, d2, -JK * g * s0, -JK * g * S2)
    elif art == "psi1":
        dv = (1.0 - 4.0 * S + 9.0 * BETA * S * S).expand(-1, n)
        sv = (-2.0 * S + 6.0 * BETA * S * S).expand(-1, n)
        s0, S2 = B["s0"], B["S2"]
        eins = torch.ones(n, dtype=F64, device=dev)
        reihe = (eins * (1.0 - 4.0 * s0 + 9.0 * BETA * s0 * s0), eins * (-4.0 + 18.0 * BETA * s0) * S2,
                 eins * (-2.0 * s0 + 6.0 * BETA * s0 * s0), eins * (-2.0 + 12.0 * BETA * s0) * S2)
    elif art == "frei":
        dv = torch.ones_like(S).expand(-1, n)
        sv = torch.zeros_like(S).expand(-1, n)
        eins = torch.ones(n, dtype=F64, device=dev)
        reihe = (eins, 0.0 * eins, 0.0 * eins, 0.0 * eins)
    else:
        raise ValueError(art)
    return {"h": B["h"], "K": B["K"], "Km": B["Km"], "R_aus": B["R_aus"], "r_m": B["r_m"], "omega": B["omega"],
            "dv": dv, "sv": sv, "cf": B["cf"], "reihe": reihe, "dev": dev}


def det_g(B, art, pts, gs):
    if not pts:
        return []
    lin = lin_g(B, art, gs)
    rho = torch.tensor([complex(z) for z in pts], dtype=C128)
    ordn = torch.ones(len(pts), dtype=F64)       # l = 0, dim = 3: Ordnung nu = l + 1 = 1
    return [complex(z) for z in R3.det(lin, rho, ordn).cpu().tolist()]


def newton_g(B, art, keime, gs, iters=30, tol=1e-12, schritt_max=0.05, delta=1e-7):
    """wie R3.newton (2D-Newton auf Re/Im D, Vorwaertsdifferenzen), aber mit eigenem g je Keim."""
    nu = [complex(z) for z in keime]
    n = len(nu)
    aktiv = list(range(n))
    konv = [False] * n
    it_n = [0] * n
    for it in range(iters):
        if not aktiv:
            break
        pts = [nu[i] for i in aktiv] + [nu[i] + delta for i in aktiv] + [nu[i] + 1j * delta for i in aktiv]
        D = det_g(B, art, pts, [gs[i] for i in aktiv] * 3)
        m = len(aktiv)
        neu = []
        for a_, i in enumerate(aktiv):
            d0, dx, dy = D[a_], D[m + a_], D[2 * m + a_]
            j11, j21 = (dx - d0).real / delta, (dx - d0).imag / delta
            j12, j22 = (dy - d0).real / delta, (dy - d0).imag / delta
            dd = j11 * j22 - j12 * j21
            if dd == 0.0 or not math.isfinite(dd):
                continue
            st = complex(-(j22 * d0.real - j12 * d0.imag) / dd, -(-j21 * d0.real + j11 * d0.imag) / dd)
            if abs(st) > schritt_max:
                st = st * (schritt_max / abs(st))
            nu[i] = nu[i] + st
            it_n[i] = it + 1
            if abs(st) < tol * max(1.0, abs(nu[i])):
                konv[i] = True
            else:
                neu.append(i)
        aktiv = neu
    Dend = det_g(B, art, nu, gs)
    return [{"nu": nu[i], "g": gs[i], "absD": abs(Dend[i]), "konvergiert": konv[i], "iter": it_n[i]} for i in range(n)]


def illinois_g(B, art, a, b, fa, fb, gs, iters=40, tol=1e-12):
    """reelle Nullstellen von Re D in Klammern [a, b], g je Klammer (gebundene Zustaende)."""
    a, b, fa, fb = list(a), list(b), list(fa), list(fb)
    n = len(a)
    for _ in range(iters):
        offen = [i for i in range(n) if abs(b[i] - a[i]) > tol * max(1.0, abs(b[i]))]
        if not offen:
            break
        c = {}
        for i in offen:
            x = b[i] - fb[i] * (b[i] - a[i]) / (fb[i] - fa[i]) if fb[i] != fa[i] else 0.5 * (a[i] + b[i])
            lo, hi = min(a[i], b[i]), max(a[i], b[i])
            if not (lo < x < hi):
                x = 0.5 * (a[i] + b[i])
            c[i] = x
        D = det_g(B, art, [complex(c[i], 0.0) for i in offen], [gs[i] for i in offen])
        for k, i in enumerate(offen):
            fc = D[k].real
            if fc * fb[i] < 0:
                a[i], fa[i] = b[i], fb[i]
            else:
                fa[i] = 0.5 * fa[i]
            b[i], fb[i] = c[i], fc
            if fc == 0.0:
                a[i] = b[i]
    return [{"nu": b[i], "g": gs[i], "klammer": abs(b[i] - a[i])} for i in range(n)]


# ================================================================ Finite Differenzen im Kasten

def fd_gitter(prof, hp, delta, R):
    k = int(round(delta / hp))
    if abs(k * hp - delta) > 1e-12:
        raise ValueError("delta muss Vielfaches des Profilschritts sein")
    M = int(round(R / delta)) - 1
    f, _ = R3.f_werte(prof, k * (M + 1) + 1)
    f = np.array(f)[k::k][:M]
    r = delta * np.arange(1, M + 1)
    return r, f


def fd_matrizen(r, f, w, delta, art, g, sigma=None):
    """K0 (2M x 2M, dicht) und Gamma-Diagonale fuer H(nu) = K0 - nu Gamma - nu^2."""
    M = len(r)
    S = f ** 2
    dp, spv = koeff(art, S, g)
    haupt = 2.0 / delta ** 2 + dp - w * w
    neben = -np.ones(M - 1) / delta ** 2
    return haupt, neben, spv


def fd_pencil_sparse(r, f, w, delta, art, g):
    M = len(r)
    haupt, neben, spv = fd_matrizen(r, f, w, delta, art, g)
    Kaa = sps.diags([neben, haupt, neben], [-1, 0, 1], format="csr")
    C = sps.diags(spv, 0, format="csr")
    K0 = sps.bmat([[Kaa, C], [C, Kaa]], format="csr")
    Gam = sps.diags(np.concatenate([2.0 * w * np.ones(M), -2.0 * w * np.ones(M)]), 0, format="csr")
    I2 = sps.identity(2 * M, format="csr")
    A = sps.bmat([[None, I2], [K0, -Gam]], format="csc")
    return A


def fd_pencil_dicht(r, f, w, delta, art, g):
    return fd_pencil_sparse(r, f, w, delta, art, g).toarray()


def fd_eig_dicht(r, f, w, delta, art, g, R_loc):
    A = fd_pencil_dicht(r, f, w, delta, art, g)
    ev, V = sla.eig(A)
    M = len(r)
    x = V[:2 * M, :]
    nrm = np.sum(np.abs(x) ** 2, axis=0)
    innen = np.concatenate([r < R_loc, r < R_loc])
    loc = np.sum(np.abs(x[innen, :]) ** 2, axis=0) / np.maximum(nrm, 1e-300)
    return ev, loc, x


def fd_eig_nahe(r, f, w, delta, art, g, ziel, k=6):
    A = fd_pencil_sparse(r, f, w, delta, art, g)
    ev, V = spla.eigs(A.astype(complex), k=k, sigma=complex(ziel), which="LM")
    return ev, V


def lu_zaehlung(r, f, w, delta, g):
    """Eigenwerte von L_u = -D2 + U' - w^2 - g J S und L_v (+), jeweils die kleinsten; L_0-Spektrum unter 1."""
    S = f ** 2
    base = 2.0 / delta ** 2 + U1(S)
    neben = -np.ones(len(r) - 1) / delta ** 2
    lu = sla.eigh_tridiagonal(base - w * w - g * JK * S, neben, select="i", select_range=(0, 5), eigvals_only=True)
    lv = sla.eigh_tridiagonal(base - w * w + g * JK * S, neben, select="i", select_range=(0, 5), eigvals_only=True)
    l0 = sla.eigh_tridiagonal(base, neben, select="v", select_range=(-10.0, 1.0), eigvals_only=True)
    return lu, lv, l0


# ================================================================ Kommando spektrum

def spektrum_stelle(name, w2, rho_star, gs, a, dev, budget, zeilen):
    om = math.sqrt(w2)
    kante, oben = 1.0 - om, 1.0 + om
    erg = {"stelle": name, "omega2": w2, "omega": om, "rho_star": rho_star, "kante": kante, "oben": oben}
    zeilen.append(f"=== {name}: omega^2 = {w2}, omega = {om:.8f}, Kanal a offen ab nu = {kante:.6f}, "
                  f"Kanal b ab {oben:.6f}; 2 omega = {2 * om:.8f}")
    # ---- Profile (Stufe A: h = a.hA, Stufe B: h = a.hB) und Momente
    profA, momA = profil_momente(w2, 0.5 * a.hA, dev)
    profB, momB = profil_momente(w2, 0.5 * a.hB, dev)
    erg["momente"] = {"A": momA, "B": momB}
    zeilen.append(f"  Profil: S0 = {momB['S0']:.6f}, R_halb = {momB['R_halb']:.4f}, Q = {momB['Q']:.4f}, "
                  f"kappa = <f^4>/<f^2> = {momB['kappa']:.8f} (Stufe A {momA['kappa']:.8f}); "
                  f"Profilzeit {momA['sek_profil']:.1f} + {momB['sek_profil']:.1f} s")
    lam2 = {g: lambda2(w2, momB["kappa"], g) for g in gs}
    erg["lambda2"] = lam2
    zeilen.append("  Zwei-Moden-Formel lambda_2(g): " + ", ".join(f"g = {g}: {lam2[g]:.8f}" for g in gs))

    # ---- FD-Kasten (dicht) bei Delta = a.dfd, Kasten R = max(40, R_halb + 30)
    Rbox = max(a.rbox, momB["R_halb"] + 30.0)
    R_loc = momB["R_halb"] + 12.0
    fd = {}
    E_ang = []
    if budget.ok("FD-Kasten", 60.0):
        r, f = fd_gitter(profB, 0.5 * a.hB, a.dfd, Rbox)
        for g in gs:
            if not budget.ok(f"FD g = {g}", 40.0):
                break
            t0 = uhr()
            ev, loc, _ = fd_eig_dicht(r, f, om, a.dfd, "psi2", g, R_loc)
            lu, lv, l0 = lu_zaehlung(r, f, om, a.dfd, g)
            inst = [complex(z) for z, lc in zip(ev, loc) if z.imag > 1e-7]
            inst.sort(key=lambda z: -z.imag)
            geb = sorted(float(z.real) for z, lc in zip(ev, loc)
                         if abs(z.imag) <= 1e-7 and -1e-9 <= z.real < kante - 1e-4 and lc > 0.9)
            eingebettet = sorted([(float(z.real), float(lc)) for z, lc in zip(ev, loc)
                                  if abs(z.imag) <= 1e-7 and kante < z.real < oben and lc > 0.5], key=lambda t: t[0])
            fd[g] = {"instabil": inst, "gebunden": geb, "lokalisiert_im_fenster": eingebettet,
                     "Lu_klein": lu.tolist(), "Lv_klein": lv.tolist(), "n_Lu": int(np.sum(lu < 0)),
                     "n_Lv": int(np.sum(lv < 0)), "L0_unter_1": l0.tolist(), "sek": uhr() - t0, "M": len(r),
                     "R_kasten": Rbox}
            if g == 0.0 or not E_ang:
                E_ang = [float(e) for e in l0]
            zeilen.append(f"  FD (Delta {a.dfd}, R {Rbox:.1f}, M {len(r)}) g = {g}: n(L_u) = {fd[g]['n_Lu']}, "
                          f"n(L_v) = {fd[g]['n_Lv']}, L_u min {lu[0]:.6e}, L_v min {lv[0]:.6e}; instabil "
                          f"{[fz(z, 8) for z in inst[:4]]}; gebunden 0 <= nu < 1 - omega: {[round(x, 8) for x in geb]}; "
                          f"lokalisiert im Fenster: {[(round(x, 6), round(lc, 3)) for x, lc in eingebettet[:6]]} "
                          f"({fd[g]['sek']:.1f} s)")
        zeilen.append(f"  L_0 = -Lap + U'(f^2), Eigenwerte unter 1 (FD): {[round(e, 8) for e in E_ang]} "
                      f"(E_0 soll omega^2 = {w2} sein)")
    erg["fd"] = fd
    erg["L0"] = E_ang

    # ---- FD fein fuer die Instabilitaet (Richardson Delta, Delta/2)
    fdfein = {}
    for g in gs:
        if g == 0.0 or not budget.ok(f"FD fein g = {g}", 30.0):
            continue
        werte = []
        for d in (a.dfd, 0.5 * a.dfd):
            try:
                r_, f_ = fd_gitter(profB, 0.5 * a.hB, d, Rbox)
                ziel = 1j * (fd[g]["instabil"][0].imag if fd.get(g, {}).get("instabil") else lam2[g])
                ev, _ = fd_eig_nahe(r_, f_, om, d, "psi2", g, ziel, k=4)
                z = min(ev, key=lambda x: abs(x - ziel))
                werte.append(complex(z))
            except Exception as err:          # noqa: BLE001
                werte.append(None)
                zeilen.append(f"  FD fein g = {g}, Delta {d}: Fehler {err}")
        if all(v is not None for v in werte):
            rich = werte[1] + (werte[1] - werte[0]) / 3.0
            fdfein[g] = {"Delta": werte[0], "Delta_halb": werte[1], "richardson": rich}
            zeilen.append(f"  FD Instabilitaet g = {g}: {fz(werte[0], 10)} | {fz(werte[1], 10)} | Richardson "
                          f"{fz(rich, 10)}")
    erg["fd_fein"] = fdfein

    # ---- Schiessen: Stufen A und B
    stufen = {}
    for stufe, prof, h, frand in (("A", profA, a.hA, a.frandA), ("B", profB, a.hB, a.frandB)):
        if not budget.ok(f"Schiessen Stufe {stufe}", 60.0):
            continue
        t0 = uhr()
        B = basis(prof, h, frand, dev)
        st = {"h": h, "R_aus": B["R_aus"], "r_m": B["r_m"], "K": B["K"]}
        # Nullstellen bei g = 0: D(0) (doppelte Nullmode) und D(2 omega) (Gegenlaeufer)
        d0 = det_g(B, "psi2", [0.0, 1e-3, 2e-3, 2 * om, 2 * om + 1e-3], [0.0] * 5)
        st["g0_D"] = {"D0": abs(d0[0]), "D_1e-3": abs(d0[1]), "D_2e-3": abs(d0[2]), "D_2omega": abs(d0[3]),
                      "D_2omega_plus": abs(d0[4])}
        # Keime
        keime, kg, art_k = [], [], []
        for g in gs:
            if g != 0.0:
                zi = (fd.get(g, {}).get("instabil") or [1j * lam2[g]])[0]
                keime.append(complex(0.0, abs(zi.imag)))
                kg.append(g)
                art_k.append("instabil")
                if g == gs[1] if len(gs) > 1 else False:
                    keime.append(complex(0.0, abs(zi.imag)))
                    kg.append(-g)
                    art_k.append("instabil(-g)")
            keime.append(complex(2 * om, -1e-6 if g else 0.0))
            kg.append(g)
            art_k.append("2omega")
            if g == (gs[1] if len(gs) > 1 else None):
                keime.append(complex(2 * om, -1e-6))
                kg.append(-g)
                art_k.append("2omega(-g)")
            for E in E_ang[1:]:
                keime.append(complex(om + math.sqrt(E), -1e-6 if g else 0.0))
                kg.append(g)
                art_k.append(f"omega+sqrt(E_{E:.4f})")
            # komplexe FD-Eigenwerte (Quartette) als Keime
            for z in (fd.get(g, {}).get("instabil") or [])[1:]:
                keime.append(complex(z))
                kg.append(g)
                art_k.append("FD-instabil")
        # Resonanzsuche: Minima von |D| auf der reellen Achse im Fenster
        nr = a.n_scan
        xs = [kante + 0.002 + (oben - kante - 0.004) * i / (nr - 1) for i in range(nr)]
        if budget.ok("Scan", 30.0):
            D = det_g(B, "psi2", [complex(x, 0.0) for x in xs] * len(gs), [g for g in gs for _ in xs])
            for ig, g in enumerate(gs):
                ab = [abs(z) for z in D[ig * nr:(ig + 1) * nr]]
                for k in R3.lokale_minima(ab):
                    if any(abs(xs[k] - kk.real) < 0.01 and gg == g for kk, gg in zip(keime, kg)):
                        continue
                    keime.append(complex(xs[k], -1e-4))
                    kg.append(g)
                    art_k.append("scan")
        st["n_keime"] = len(keime)
        pole = []
        if budget.ok(f"Newton Stufe {stufe}", 40.0):
            nw = newton_g(B, "psi2", keime, kg, iters=a.iter_newton)
            for w_, ak in zip(nw, art_k):
                w_["art"] = ak
                pole.append(w_)
        st["pole"] = pole
        # gebundene Zustaende: Vorzeichenwechsel von Re D auf (0, 1 - omega)
        geb = []
        if budget.ok(f"gebunden Stufe {stufe}", 30.0):
            nb = a.n_geb
            xb = [1e-4 + (kante - 2e-4) * i / (nb - 1) for i in range(nb)]
            D = det_g(B, "psi2", [complex(x, 0.0) for x in xb] * len(gs), [g for g in gs for _ in xb])
            kl = []
            for ig, g in enumerate(gs):
                re = [z.real for z in D[ig * nb:(ig + 1) * nb]]
                for k in range(nb - 1):
                    if re[k] * re[k + 1] < 0:
                        kl.append((xb[k], xb[k + 1], re[k], re[k + 1], g))
            if kl:
                geb = illinois_g(B, "psi2", [k_[0] for k_ in kl], [k_[1] for k_ in kl], [k_[2] for k_ in kl],
                                 [k_[3] for k_ in kl], [k_[4] for k_ in kl], iters=a.iter_illinois)
        st["gebunden"] = geb
        # Negativkontrolle ohne Ball an den gefundenen Stellen
        pk = [p_["nu"] for p_ in pole if p_["konvergiert"]] + [complex(x["nu"], 0.0) for x in geb]
        if pk and budget.ok("Negativkontrolle", 10.0):
            Df = det_g(B, "frei", pk, [0.0] * len(pk))
            st["frei_min_absD"] = min(abs(z) for z in Df)
        st["sek"] = uhr() - t0
        stufen[stufe] = st
        zeilen.append(f"  Schiessen Stufe {stufe} (h {h}, R {B['R_aus']:.2f}, r_m {B['r_m']:.2f}): g = 0: |D(0)| "
                      f"{st['g0_D']['D0']:.2e} (|D(1e-3)| {st['g0_D']['D_1e-3']:.2e}, Verh. 2e-3/1e-3 "
                      f"{st['g0_D']['D_2e-3'] / max(st['g0_D']['D_1e-3'], 1e-300):.3f}), |D(2 omega)| "
                      f"{st['g0_D']['D_2omega']:.2e} (|D(2 omega + 1e-3)| {st['g0_D']['D_2omega_plus']:.2e}); "
                      f"{len(keime)} Keime, {st['sek']:.1f} s")
    erg["stufen"] = stufen

    # ---- Tabelle: Pole je Art und g, Stufe A | B
    if "B" in stufen:
        polA = stufen.get("A", {}).get("pole", [])
        polB = stufen["B"]["pole"]
        zeilen.append("  Pole (Stufe B; in Klammern Abstand zu Stufe A). Im > 0 = anwachsend, Im < 0 = abklingend:")
        gesehen = []
        for i, p_ in enumerate(polB):
            if not (p_["konvergiert"] and p_["absD"] < 1e-8):
                continue
            if any(abs(p_["nu"] - q["nu"]) < 1e-7 and p_["g"] == q["g"] for q in gesehen):
                continue
            gesehen.append(p_)
            kandA = [q["nu"] for q in polA if q["konvergiert"] and q["g"] == p_["g"] and q["absD"] < 1e-8]
            pa = min(kandA, key=lambda z: abs(z - p_["nu"])) if kandA else None
            abst = f"{abs(p_['nu'] - pa):.1e}" if pa is not None else "-"
            extra = ""
            if p_["art"].startswith("instabil") and p_["g"] != 0:
                l2 = lam2.get(abs(p_["g"]), lambda2(w2, momB["kappa"], p_["g"]))
                extra = f", lambda/lambda_2 = {p_['nu'].imag / l2:.6f}, |Re|/Im = {abs(p_['nu'].real) / max(p_['nu'].imag, 1e-300):.1e}"
            zeilen.append(f"    g = {p_['g']:+.2f} [{p_['art']}]: nu = {fz(p_['nu'], 10)} (A: {abst}), |D| "
                          f"{p_['absD']:.1e}{extra}")
        for x in stufen["B"].get("gebunden", []):
            zeilen.append(f"    g = {x['g']:+.2f} [gebunden, reell]: nu = {x['nu']:.10f} (Klammer {x['klammer']:.1e})")
        if "frei_min_absD" in stufen["B"]:
            zeilen.append(f"    Negativkontrolle ohne Ball: min |D_frei| an diesen Stellen = "
                          f"{stufen['B']['frei_min_absD']:.3e}")
    return erg


# ================================================================ Kommando kontrolle1 (N = 1-Grenze)

def kontrolle1(a, dev, budget, zeilen):
    erg = {}
    for w2, keim, name in ((0.7, N1_POL_07, "Pol omega^2 = 0,7"), (0.797677, complex(1.744618, -1e-7), "BIC P1")):
        if not budget.ok(name, 60.0):
            continue
        res = {}
        for stufe, h, frand in (("A", a.hA, a.frandA), ("B", a.hB, a.frandB)):
            prof, mom = profil_momente(w2, 0.5 * h, dev)
            B = basis(prof, h, frand, dev)
            nw = newton_g(B, "psi1", [keim], [0.0], iters=a.iter_newton)[0]
            res[stufe] = nw
            zeilen.append(f"  N = 1 ({name}), Stufe {stufe} (h {h}): rho = {fz(nw['nu'], 10)}, |D| {nw['absD']:.1e}, "
                          f"konvergiert {nw['konvergiert']}")
        erg[name] = res
    return erg


# ================================================================ Kommando floquet

def pumpmode(r, f, w, delta, rho_star, R_loc):
    """Atmungsmode (N = 1, l = 0) im FD-Kasten nahe rho*: (a, b) reell, normiert max|a + b| = 1 (wie Codex)."""
    ev, V = fd_eig_nahe(r, f, w, delta, "psi1", 0.0, rho_star, k=8)
    M = len(r)
    innen = np.concatenate([r < R_loc, r < R_loc])
    best = None
    for i in range(len(ev)):
        x = V[:2 * M, i]
        loc = float(np.sum(np.abs(x[innen]) ** 2) / np.sum(np.abs(x) ** 2))
        kand = (loc, i)
        if best is None or kand[0] > best[0]:
            best = kand
    loc, i = best
    x = V[:2 * M, i]
    j = int(np.argmax(np.abs(x)))
    x = x * (abs(x[j]) / x[j])
    im_rest = float(np.max(np.abs(x.imag)) / np.max(np.abs(x.real)))
    x = x.real
    A_, B_ = x[:M], x[M:]
    a_, b_ = A_ / r, B_ / r
    s = a_ + b_
    k = int(np.argmax(np.abs(s)))
    norm = s[k]
    a_, b_ = a_ / norm, b_ / norm
    aussen = r > R_loc
    rest_aussen = float(np.max(np.abs((A_ / norm)[aussen]))) if np.any(aussen) else 0.0
    return {"rho": complex(ev[i]), "loc": loc, "im_rest": im_rest, "a": a_, "b": b_,
            "alle_ev": [complex(z) for z in ev], "max_A_aussen": rest_aussen}


def monodromie(r, f, w, delta, rho, g, eps, a_, b_, sigma, nt, dev):
    """Monodromie ueber T = 2 pi/rho fuer (P, Q, P_t, Q_t), P = r p, Q = r q, chi = p + i q (mitdrehend)."""
    M = len(r)
    S = f ** 2
    t = lambda x: torch.tensor(x, dtype=F64, device=dev).unsqueeze(1)
    base = t(U1(S) - w * w)
    Pm = t(U2(S) * 2.0 * f * (a_ + b_))
    Qr0 = t(2.0 * f * (a_ + b_))
    Qi0 = t(2.0 * f * (b_ - a_))
    Sg = t(S)
    sig = t(sigma)
    n = 4 * M
    Y = torch.eye(n, dtype=F64, device=dev)
    T = 2.0 * math.pi / rho
    dt = T / nt
    inv_d2 = 1.0 / delta ** 2

    def lap(X):
        out = -2.0 * X
        out[1:] += X[:-1]
        out[:-1] += X[1:]
        return out * inv_d2

    def rhs(tt, Y):
        P, Q, Pt, Qt = Y[:M], Y[M:2 * M], Y[2 * M:3 * M], Y[3 * M:]
        c, s_ = math.cos(rho * tt), math.sin(rho * tt)
        mod = eps * c
        Vu = base + mod * Pm - g * JK * (Sg + mod * Qr0)
        Vv = base + mod * Pm + g * JK * (Sg + mod * Qr0)
        W = g * JK * eps * s_ * Qi0
        dPt = -2.0 * w * Qt + lap(P) - Vu * P + W * Q - sig * (Pt + w * Q)
        dQt = 2.0 * w * Pt + lap(Q) - Vv * Q + W * P - sig * (Qt - w * P)
        return torch.cat([Pt, Qt, dPt, dQt], 0)

    tt = 0.0
    for _ in range(nt):
        k1 = rhs(tt, Y)
        k2 = rhs(tt + 0.5 * dt, Y + (0.5 * dt) * k1)
        k3 = rhs(tt + 0.5 * dt, Y + (0.5 * dt) * k2)
        k4 = rhs(tt + dt, Y + dt * k3)
        Y = Y + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        tt += dt
    mu = np.linalg.eigvals(Y.cpu().numpy())
    raten = np.log(np.abs(mu)) / T
    return mu, raten, T


def floquet(a, dev, budget, zeilen):
    erg = {}
    gs = [float(x) for x in a.g.split(",")]
    epss = [float(x) for x in a.eps.split(",")]
    for name in a.stellen.split(","):
        w2, rho_star = STELLEN[name]
        if rho_star is None:
            zeilen.append(f"=== {name}: rho* unbekannt, entfaellt")
            continue
        om = math.sqrt(w2)
        prof, mom = profil_momente(w2, a.hp, dev)
        Rbox = max(a.rbox, mom["R_halb"] + 30.0)
        R_loc = mom["R_halb"] + 12.0
        r, f = fd_gitter(prof, a.hp, a.dfd, Rbox)
        pm = pumpmode(r, f, om, a.dfd, rho_star, R_loc)
        rho = pm["rho"].real
        sigma = np.where(r > Rbox - a.lsp, a.sig0 * ((r - (Rbox - a.lsp)) / a.lsp) ** 2, 0.0)
        nt = int(math.ceil((2.0 * math.pi / rho) / (a.dtfak * a.dfd)))
        e = {"omega2": w2, "rho_star_kontinuum": rho_star, "rho_fd": pm["rho"], "pump_loc": pm["loc"],
             "pump_im_rest": pm["im_rest"], "pump_max_A_aussen": pm["max_A_aussen"],
             "pump_ev_nahe": pm["alle_ev"], "R_kasten": Rbox, "M": len(r), "nt": nt, "laeufe": []}
        zeilen.append(f"=== {name}: omega^2 = {w2}, FD Delta {a.dfd}, R {Rbox:.1f}, M {len(r)}, Schwamm {a.lsp} "
                      f"(sigma0 {a.sig0}); Pumpe rho_FD = {fz(pm['rho'], 8)} (Kontinuum {rho_star}), Lokalisierung "
                      f"{pm['loc']:.6f}, max|A| aussen {pm['max_A_aussen']:.2e}; T = {2 * math.pi / rho:.6f}, nt {nt}")
        # FD-Eigenwertproblem ohne Pumpe als Bezug (Instabilitaet)
        for g in gs:
            bez = None
            if g != 0.0:
                try:
                    ev, _ = fd_eig_nahe(r, f, om, a.dfd, "psi2", g, 1j * lambda2(w2, mom["kappa"], g), k=4)
                    bez = complex(min(ev, key=lambda z: abs(z - 1j * lambda2(w2, mom["kappa"], g))))
                except Exception as err:          # noqa: BLE001
                    zeilen.append(f"  Bezug g = {g}: Fehler {err}")
            for eps in epss:
                if not budget.ok(f"Floquet {name} g = {g} eps = {eps}", a.reserve):
                    continue
                t0 = uhr()
                mu, raten, T = monodromie(r, f, om, a.dfd, rho, g, eps, pm["a"], pm["b"], sigma, nt, dev)
                ordn = np.argsort(-raten)
                top = [(float(raten[i]), complex(mu[i])) for i in ordn[:6]]
                n_inst = int(np.sum(raten > a.schwelle))
                lauf = {"g": g, "eps": eps, "top": top, "n_instabil": n_inst, "sek": uhr() - t0,
                        "bezug_fd_lambda": bez.imag if bez is not None else None}
                # Raten nahe 0 (neutraler Sektor), fuer g = 0: groesste |Rate| unter den |mu| ~ 1
                nah = np.abs(np.abs(mu) - 1.0) < 0.05
                lauf["max_rate_neutral"] = float(np.max(raten[nah])) if np.any(nah) else None
                e["laeufe"].append(lauf)
                zeilen.append(f"  g = {g:+.2f}, eps = {eps:.4f}: groesste Raten {[round(x[0], 9) for x in top[:4]]}, "
                              f"n(Rate > {a.schwelle:g}) = {n_inst}"
                              + (f", Bezug FD lambda = {bez.imag:.9f}" if bez is not None else "")
                              + f" ({lauf['sek']:.1f} s)")
        erg[name] = e
    return erg


# ================================================================ Kommando ueberlapp (Frage 3)

def ueberlapp_eins(w2, hp, dev):
    """Gegenlaeufer v = f bei nu = 2 omega koppelt ueber -g J f^2 in Kanal a bei (omega + nu)^2 = 9 omega^2.
    Phi'' = (U'(S) - 9 omega^2) Phi, Phi(0) = 0, Phi'(0) = 1; I = int Phi f^3 r dr; A = Amplitude von Phi aussen.
    Goldene Regel (PLAN 1.3, Herleitung im Ergebnis): -Im nu ~ g^2 J^2 I^2 / (2 omega k A^2 N2)."""
    prof, mom = profil_momente(w2, hp, dev)
    om = math.sqrt(w2)
    E = 9.0 * w2
    k = math.sqrt(E - 1.0)
    h = 2.0 * hp
    r_end = mom["R_halb"] + 25.0
    n = int(math.ceil(r_end / h))
    f, _ = R3.f_werte(prof, 2 * n + 3)
    f = np.array(f)
    S = f ** 2
    V = U1(S) - E

    def ab(j, y):
        return np.array([y[1], V[j] * y[0]])
    rr = h
    y = np.array([h * (1.0 + (U1(S[0]) - E) * h * h / 6.0), 1.0 + (U1(S[0]) - E) * h * h / 2.0])
    I = h * y[0] * f[2] ** 3 * rr          # Trapez: Punkt r = h innen (Gewicht h), r = 0 traegt 0 bei
    for m in range(1, n):
        j0 = 2 * m
        k1 = ab(j0, y)
        k2 = ab(j0 + 1, y + 0.5 * h * k1)
        k3 = ab(j0 + 1, y + 0.5 * h * k2)
        k4 = ab(j0 + 2, y + h * k3)
        y = y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        rr = (m + 1) * h
        wgt = 0.5 * h if m == n - 1 else h
        I += wgt * y[0] * f[2 * (m + 1)] ** 3 * rr
    A = math.sqrt(y[0] ** 2 + (y[1] / k) ** 2)
    gam_pro_g2 = JK ** 2 * I ** 2 / (2.0 * om * k * A ** 2 * mom["N2"])
    return {"w2": w2, "I": I, "A": A, "I_durch_A": I / A, "k": k, "N2": mom["N2"], "Gamma_durch_g2": gam_pro_g2,
            "S0": mom["S0"], "R_halb": mom["R_halb"]}


def ueberlapp(a, dev, budget, zeilen):
    xs = [float(x) for x in np.arange(a.xmin, a.xmax + 1e-9, a.dx)]
    werte = []
    for x in xs:
        if not budget.ok(f"ueberlapp {x}", 20.0):
            break
        u = ueberlapp_eins(x, a.hp, dev)
        werte.append(u)
        zeilen.append(f"  omega^2 = {x:.4f}: I/A = {u['I_durch_A']:+.6e}, Gamma_FGR/g^2 = {u['Gamma_durch_g2']:.4e}, "
                      f"S0 = {u['S0']:.4f}, R_halb = {u['R_halb']:.3f}")
    wechsel = []
    for i in range(len(werte) - 1):
        if werte[i]["I_durch_A"] * werte[i + 1]["I_durch_A"] < 0:
            x0, x1 = werte[i]["w2"], werte[i + 1]["w2"]
            y0, y1 = werte[i]["I_durch_A"], werte[i + 1]["I_durch_A"]
            wechsel.append(x0 - y0 * (x1 - x0) / (y1 - y0))
    zeilen.append(f"  Vorzeichenwechsel von I (linear interpoliert): {[round(w, 5) for w in wechsel]}")
    erg = {"werte": werte, "wechsel": wechsel, "pole": []}
    # 2 omega-Pol bei endlichem g an Rasterpunkten und an den Wechseln (Newton, Schiessen Stufe h)
    gl = [float(x) for x in a.g.split(",")]
    punkte = sorted(set([round(w, 6) for w in wechsel] + [round(w + d, 6) for w in wechsel for d in (-0.01, 0.01)]))
    punkte += [x for x in [float(v) for v in a.pol_extra.split(",") if v]]
    for x in punkte:
        if not budget.ok(f"2omega-Pol {x}", 40.0):
            break
        prof, mom = profil_momente(x, 0.5 * a.h, dev)
        B = basis(prof, a.h, a.frand, dev)
        om = math.sqrt(x)
        u = ueberlapp_eins(x, a.hp, dev)
        keime = [complex(2 * om, -u["Gamma_durch_g2"] * g * g) for g in gl]
        nw = newton_g(B, "psi2", keime, gl, iters=a.iter_newton)
        for g, w_ in zip(gl, nw):
            erg["pole"].append({"w2": x, "g": g, "nu": w_["nu"], "absD": w_["absD"], "konv": w_["konvergiert"],
                                "Gamma_FGR": u["Gamma_durch_g2"] * g * g})
            zeilen.append(f"  2 omega-Pol omega^2 = {x:.6f}, g = {g}: nu = {fz(w_['nu'], 10)}, |D| {w_['absD']:.1e}, "
                          f"konv {w_['konvergiert']}; goldene Regel -Im = {u['Gamma_durch_g2'] * g * g:.4e}")
    return erg


# ================================================================ Rahmen

def argumente():
    ap = argparse.ArgumentParser(description="Runde 8 GF-BIC")
    ap.add_argument("kommando", choices=["rauch", "spektrum", "kontrolle1", "floquet", "ueberlapp"])
    ap.add_argument("--stellen", default="P1")
    ap.add_argument("--g", default="0,0.2,0.5,1.0")
    ap.add_argument("--eps", default="0,0.01,0.02,-0.02,0.04")
    ap.add_argument("--hA", type=float, default=0.02)
    ap.add_argument("--hB", type=float, default=0.01)
    ap.add_argument("--frandA", type=float, default=1e-6)
    ap.add_argument("--frandB", type=float, default=1e-8)
    ap.add_argument("--h", type=float, default=0.02, help="ueberlapp: Schiess-Schritt fuer den 2 omega-Pol")
    ap.add_argument("--frand", type=float, default=1e-7)
    ap.add_argument("--hp", type=float, default=0.01, help="Profilschritt (floquet, ueberlapp)")
    ap.add_argument("--dfd", type=float, default=0.1, help="FD-Gitterschritt")
    ap.add_argument("--rbox", type=float, default=40.0)
    ap.add_argument("--lsp", type=float, default=12.0, help="floquet: Schwammbreite")
    ap.add_argument("--sig0", type=float, default=1.5, help="floquet: Schwammstaerke")
    ap.add_argument("--dtfak", type=float, default=0.5, help="floquet: dt = dtfak * Delta (hoechstens)")
    ap.add_argument("--schwelle", type=float, default=1e-5, help="floquet: Rate, ab der eine Mode instabil zaehlt")
    ap.add_argument("--reserve", type=float, default=30.0)
    ap.add_argument("--n-scan", dest="n_scan", type=int, default=300)
    ap.add_argument("--n-geb", dest="n_geb", type=int, default=200)
    ap.add_argument("--iter-newton", dest="iter_newton", type=int, default=25)
    ap.add_argument("--iter-illinois", dest="iter_illinois", type=int, default=30)
    ap.add_argument("--xmin", type=float, default=0.52)
    ap.add_argument("--xmax", type=float, default=0.98)
    ap.add_argument("--dx", type=float, default=0.01)
    ap.add_argument("--pol-extra", dest="pol_extra", default="")
    ap.add_argument("--geraet", default="cpu", choices=["cpu", "cuda"])
    ap.add_argument("--out", default=None)
    ap.add_argument("--budget", type=float, default=540.0)
    return ap.parse_args()


def main():
    a = argumente()
    if a.geraet == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("--geraet cuda, aber kein CUDA-Geraet")
        dev = torch.device("cuda")
    else:
        torch.set_num_threads(1)
        dev = torch.device("cpu")
    budget = Budget(a.budget)
    out = a.out or os.path.join(HIER, f"ausgabe-{a.kommando}")
    os.makedirs(out, exist_ok=True)
    start = jetzt()
    kopf = (f"Runde 8 GF-BIC {a.kommando} Start {start}, Geraet {a.geraet}, torch {torch.__version__}, "
            f"numpy {np.__version__}; gfbic.py sha256 {sha256(os.path.abspath(__file__))[:16]}, resonanz3d.py "
            f"{R3_PFAD} sha256 {sha256(R3_PFAD)[:16]}")
    zeilen = [kopf]
    print(kopf, flush=True)
    ergebnis = {"start": start, "kommando": a.kommando, "argumente": vars(a), "ergebnisse": {},
                "sha256_gfbic": sha256(os.path.abspath(__file__)), "sha256_resonanz3d": sha256(R3_PFAD)}

    def sichern():
        ergebnis["ende"] = jetzt()
        ergebnis["sek"] = uhr()
        ergebnis["entfallen"] = budget.abgebrochen
        with open(os.path.join(out, f"{a.kommando}.json"), "w") as fh:
            json.dump(jsonfest(ergebnis), fh, indent=1)
        with open(os.path.join(out, f"{a.kommando}_bericht.txt"), "w") as fh:
            fh.write("\n".join(zeilen) + "\n")

    rc = 0
    try:
        if a.kommando == "rauch":
            a.hA, a.hB, a.frandA, a.frandB = 0.08, 0.04, 1e-5, 1e-6
            a.n_scan, a.n_geb, a.iter_newton, a.iter_illinois, a.dfd = 40, 30, 6, 8, 0.2
            ergebnis["ergebnisse"]["spektrum"] = spektrum_stelle("P1", 0.797677, 1.744618, [0.0, 0.2], a, dev,
                                                                 budget, zeilen)
            sichern()
            a.stellen, a.g, a.eps, a.hp = "P1", "0,0.2", "0,0.02", 0.02
            ergebnis["ergebnisse"]["floquet"] = floquet(a, dev, budget, zeilen)
            sichern()
            a.xmin, a.xmax, a.dx, a.h, a.g = 0.78, 0.80, 0.02, 0.08, "0.2"
            ergebnis["ergebnisse"]["ueberlapp"] = ueberlapp(a, dev, budget, zeilen)
        elif a.kommando == "spektrum":
            gs = [float(x) for x in a.g.split(",")]
            for name in a.stellen.split(","):
                w2, rs = STELLEN[name]
                ergebnis["ergebnisse"][name] = spektrum_stelle(name, w2, rs, gs, a, dev, budget, zeilen)
                sichern()
        elif a.kommando == "kontrolle1":
            ergebnis["ergebnisse"]["kontrolle1"] = kontrolle1(a, dev, budget, zeilen)
        elif a.kommando == "floquet":
            ergebnis["ergebnisse"]["floquet"] = floquet(a, dev, budget, zeilen)
        elif a.kommando == "ueberlapp":
            ergebnis["ergebnisse"]["ueberlapp"] = ueberlapp(a, dev, budget, zeilen)
    except Exception:                               # noqa: BLE001
        tb = traceback.format_exc()
        zeilen.append("FEHLER:\n" + tb)
        ergebnis["fehler"] = tb
        print(tb, flush=True)
        rc = 1
    zeilen.append(f"Ende {jetzt()}, {uhr():.1f} s; entfallen: {budget.abgebrochen or 'nichts'}")
    sichern()
    print("\n".join(zeilen[1:]), flush=True)
    sys.exit(rc)


if __name__ == "__main__":
    main()
