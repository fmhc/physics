#!/usr/bin/env python3
"""VORTEX-RAD (Runde 18, Code-Agent fuer claude-primary): Wirbel mit Ladung m auf dem Rad-Graphen.

Gleichung wie V5: Psi_i'' + Sum_j J (Psi_i - Psi_j) + V'(|Psi_i|^2) Psi_i = 0, V'(S) = 1 - 2S + 1,5 S^2.
Stationaer Psi = phi e^{i omega t}, phi komplex: L phi + (V'(|phi|^2) - omega^2) phi = 0.
Newton in 2(N+1) reellen Unbekannten, Phase fixiert (Im phi_g = 0: Unbekannte b_g und Gleichung Im F_g entfallen,
Endkontrolle auf allen Gleichungen). Stabilitaet im mitrotierenden Bild: W'' + G W' + K W = 0, Begleitmatrix.

Aufruf: python vortex_rad.py <modus> <aus.json> [J] [Nmin Nmax]
  modus: schnell | kontrolle | nmax | scan (mit J) | lokal | zeit
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import glob
import json
import sys
import time

import numpy as np

TOL = 1e-8        # max Re nach Abzug der Phasen-Nullmode
TOL_IM = 1e-6     # |Im| > TOL_IM heisst oszillatorisch
RES_TOL = 1e-12   # Newton: max |F|
NC = 30           # Rasterpunkte je Fenster
JS = (0.02, 0.05, 0.1)
T0 = time.time()


def Vp(s):
    return 1 - 2 * s + 1.5 * s * s


def Vpp(s):
    return -2 + 3 * s


def V(s):
    return s - s * s + 0.5 * s ** 3


def s_ast(c, gross):
    """Einzelplatzloesung V'(S) = c; kleiner Ast S < 2/3, grosser Ast S > 2/3; None, wenn keine positive Loesung."""
    disc = 6 * c - 2
    if disc < 0:
        return None
    S = (2 + np.sqrt(disc)) / 3 if gross else (2 - np.sqrt(disc)) / 3
    return float(S) if S > 0 else None


def c_raster(n=NC):
    return [1 / 3 + (2 / 3) * (k - 0.5) / n for k in range(1, n + 1)]


def laplace(N, J):
    n = N + 1
    A = np.zeros((n, n))
    for i in range(N):
        A[i, (i + 1) % N] = A[(i + 1) % N, i] = 1
        A[i, N] = A[N, i] = 1
    return J * (np.diag(A.sum(1)) - A)


def laplace_tw(d, J, tau):
    """Fundamentalbereich aus d Ringknoten, phi_{j+d} = tau phi_j, Nabe = 0 (Symmetrie); Grad 3 inkl. Nabenkante."""
    Lc = np.zeros((d, d), complex)
    for j in range(d):
        Lc[j, j] += 3 * J
        if j + 1 < d:
            Lc[j, j + 1] -= J
        else:
            Lc[j, 0] -= J * tau
        if j - 1 >= 0:
            Lc[j, j - 1] -= J
        else:
            Lc[j, d - 1] -= J * np.conj(tau)
    return Lc


def residuum(Lc, w2, phi):
    s = (phi * np.conj(phi)).real
    return Lc @ phi + (Vp(s) - w2) * phi


def kmatrix(Lc, w2, phi):
    """Reelle symmetrische 2n x 2n Matrix: Jacobi-Matrix des Residuums in (a, b) = K der Linearisierung."""
    n = phi.size
    a, b = phi.real, phi.imag
    s = a * a + b * b
    Lr = np.real(Lc)
    Li = np.imag(Lc)
    d0 = Vp(s) - w2
    v2 = Vpp(s)
    K = np.empty((2 * n, 2 * n))
    K[:n, :n] = Lr + np.diag(d0 + 2 * v2 * a * a)
    K[:n, n:] = -Li + np.diag(2 * v2 * a * b)
    K[n:, :n] = Li + np.diag(2 * v2 * a * b)
    K[n:, n:] = Lr + np.diag(d0 + 2 * v2 * b * b)
    return K


def newton(Lc, w2, phi, g, itmax=60, maxamp=10.0):
    n = phi.size
    phi = np.array(phi, complex)
    if abs(phi[g]) > 0:
        phi = phi * np.exp(-1j * np.angle(phi[g]))
    keep = np.ones(2 * n, bool)
    keep[n + g] = False
    for it in range(itmax):
        F = residuum(Lc, w2, phi)
        if np.max(np.abs(F)) < RES_TOL:
            return phi, True, it
        Fr = np.concatenate([F.real, F.imag])[keep]
        K = kmatrix(Lc, w2, phi)[np.ix_(keep, keep)]
        try:
            dx = np.linalg.solve(K, -Fr)
        except np.linalg.LinAlgError:
            return phi, False, it
        voll = np.zeros(2 * n)
        voll[keep] = dx
        phi = phi + voll[:n] + 1j * voll[n:]
        if not np.all(np.isfinite(phi)) or np.max(np.abs(phi)) > maxamp:
            return phi, False, it
    F = residuum(Lc, w2, phi)
    return phi, bool(np.max(np.abs(F)) < RES_TOL), itmax


def fortsetzen(Lfun, w2fun, J, phi0, g, schritte):
    """Fortsetzung in J von J = 0 (Startloesung phi0, phi0[g] reell positiv) in gleichen Schritten."""
    phi = np.array(phi0, complex)
    for k in range(1, schritte + 1):
        Jk = J * k / schritte
        neu, ok, _ = newton(Lfun(Jk), w2fun(Jk), phi, g)
        if not ok:
            return neu, False, k, "newton"
        if np.max(np.abs(neu)) < 1e-3:
            return neu, False, k, "null"
        if np.max(np.abs(neu - phi)) > 0.3:
            return neu, False, k, "sprung"
        phi = neu
    return phi, True, schritte, "ok"


def stab(L, w2, phi):
    """Lineare Stabilitaet im mitrotierenden Bild, Krein-Signaturen, Indexzaehlung."""
    n = phi.size
    w = np.sqrt(w2)
    g = int(np.argmax(np.abs(phi)))
    phi = phi * np.exp(-1j * np.angle(phi[g]))
    K = kmatrix(L, w2, phi)
    G = np.zeros((2 * n, 2 * n))
    G[:n, n:] = -2 * w * np.eye(n)
    G[n:, :n] = 2 * w * np.eye(n)
    A = np.zeros((4 * n, 4 * n))
    A[:2 * n, 2 * n:] = np.eye(2 * n)
    A[2 * n:, :2 * n] = -K
    A[2 * n:, 2 * n:] = -G
    ev, vec = np.linalg.eig(A)
    order = np.argsort(np.abs(ev))
    null_betrag = float(np.abs(ev[order[1]]))
    rest = order[2:]
    evr = ev[rest]
    vr = vec[:, rest]
    mr = float(np.max(evr.real))

    def art_bei(tol):
        u = evr[evr.real > tol]
        if u.size == 0:
            return "stabil"
        re = np.abs(u.imag) <= TOL_IM
        if np.all(re):
            return "reell"
        if not np.any(re):
            return "oszillatorisch"
        return "gemischt"

    dom, dom_im = None, None
    if mr > TOL:
        k = int(np.argmax(evr.real))
        dom = "reell" if abs(evr[k].imag) <= TOL_IM else "oszillatorisch"
        dom_im = float(abs(evr[k].imag))
    N_r = int(np.sum((evr.real > TOL) & (np.abs(evr.imag) <= TOL_IM)))
    N_c = int(np.sum((evr.real > TOL) & (evr.imag > TOL_IM)))
    ax = np.where((np.abs(evr.real) <= TOL) & (evr.imag > 1e-9))[0]
    n_minus, unklar, sig_minus, sig_plus = 0, 0, [], []
    for i in ax:
        x = vr[:2 * n, i]
        sg = float(evr[i].imag)
        xx = float(np.real(np.vdot(x, x)))
        E = float(np.real(np.vdot(x, K @ x))) + sg * sg * xx
        if abs(E) <= 1e-9 * xx * (1 + sg * sg):
            unklar += 1
        elif E < 0:
            n_minus += 1
            sig_minus.append(sg)
        else:
            sig_plus.append(sg)
    weitere_null = int(np.sum((np.abs(evr.real) <= TOL) & (np.abs(evr.imag) <= 1e-9)))
    kev = np.linalg.eigvalsh(K)
    nK = int(np.sum(kev < -1e-9))
    X = np.concatenate([phi.real, phi.imag])
    keep = np.ones(2 * n, bool)
    keep[n + g] = False
    dX = np.zeros(2 * n)
    try:
        dX[keep] = np.linalg.solve(K[np.ix_(keep, keep)], 2 * w * X[keep])
        dQ = float(2 * X @ X + 4 * w * X @ dX)
    except np.linalg.LinAlgError:
        dQ = float("nan")
    nD = 1 if dQ < 0 else 0
    return {"maxRe": mr, "art": art_bei(TOL), "art_1e-6": art_bei(1e-6), "art_1e-10": art_bei(1e-10),
            "dom": dom, "dom_im": dom_im, "N_r": N_r, "N_c": N_c, "n_minus": n_minus, "krein_unklar": unklar,
            "sig_minus": sorted(sig_minus)[:8], "sig_plus_min": (min(sig_plus) if sig_plus else None),
            "weitere_null": weitere_null, "nK": nK, "dQdw": dQ, "kks_l": N_r + 2 * N_c + 2 * n_minus,
            "kks_r": nK - nD, "null_betrag": null_betrag, "kmin": float(np.sort(np.abs(kev))[1])}


# ---------------------------------------------------------------- Familie U (gleichfoermiger Wirbel)

def wirbel(N, m, J, gross, c, schritte=20, rng=None, mit_stab=True):
    gm = 3 - 2 * np.cos(2 * np.pi * m / N)
    w2 = c + J * gm
    S_end = s_ast(c, gross)
    j = np.arange(N)
    S0 = s_ast(w2, gross)
    phi0 = np.zeros(N + 1, complex)
    if S0 is not None:
        pfad = "A"
        phi0[:N] = np.sqrt(S0) * np.exp(2j * np.pi * m * j / N)
        phi, ok, k, grund = fortsetzen(lambda Jk: laplace(N, Jk), lambda Jk: w2, J, phi0, 0, schritte)
    else:
        pfad = "B"
        phi0[:N] = np.sqrt(S_end) * np.exp(2j * np.pi * m * j / N)
        phi, ok, k, grund = fortsetzen(lambda Jk: laplace(N, Jk), lambda Jk: c + Jk * gm, J, phi0, 0, schritte)
    r = {"N": N, "m": m, "J": J, "ast": "gross" if gross else "klein", "c": c, "w2": w2, "pfad": pfad,
         "konvergiert": bool(ok), "grund": grund, "schritt": k}
    if not ok:
        return r, None
    L = laplace(N, J)
    s = np.abs(phi[:N]) ** 2
    dphase = np.angle(phi[:N] * np.exp(-2j * np.pi * m * j / N))
    r.update(S_formel=S_end, formel_abw=float(np.max(np.abs(s - S_end))), nabe=float(abs(phi[N])),
             phasen_abw=float(np.max(np.abs(dphase))), residuum=float(np.max(np.abs(residuum(L, w2, phi)))))
    if rng is not None:
        p = phi + 1e-3 * (rng.standard_normal(N + 1) + 1j * rng.standard_normal(N + 1))
        p2, ok2, _ = newton(L, w2, p, 0)
        r["neustart_ok"] = bool(ok2)
        if ok2:
            r["neustart_abw"] = float(np.max(np.abs(np.abs(p2) - np.abs(phi))))
            r["neustart_nabe"] = float(abs(p2[N]))
    if mit_stab:
        r.update(stab(L, w2, phi))
    return r, phi


def scan(J, Ns, ms_fn=None, cs=None, pfad=None):
    rng = np.random.default_rng(1802)
    cs = c_raster() if cs is None else cs
    out = {"modus": "scan", "J": J, "punkte": []}
    for N in Ns:
        ms = range(1, N // 2 + 1) if ms_fn is None else ms_fn(N)
        for m in ms:
            for gross in (False, True):
                for c in cs:
                    r, _ = wirbel(N, m, J, gross, c, rng=rng)
                    out["punkte"].append(r)
        out["sekunden"] = time.time() - T0
        if pfad:
            schreibe(out, pfad)
        print("scan J", J, "N", N, "fertig", round(time.time() - T0, 1), "s", flush=True)
    return out


# ---------------------------------------------------------------- Lokalisierte Wirbel

def teilring(N, K, mp, J, gross, w2, schritte=40):
    d = N // K
    tau = np.exp(2j * np.pi * mp / K)
    r = {"fam": "L-a", "N": N, "K": K, "m": mp, "J": J, "ast": "gross" if gross else "klein", "w2": w2}
    S0 = s_ast(w2, gross)
    if S0 is None:
        r.update(existiert=False, grund="kein_start")
        return r, None
    psi0 = np.zeros(d, complex)
    psi0[0] = np.sqrt(S0)
    psi, ok, k, grund = fortsetzen(lambda Jk: laplace_tw(d, Jk, tau), lambda Jk: w2, J, psi0, 0, schritte)
    r.update(grund=grund, schritt=k)
    if not ok:
        r["existiert"] = False
        return r, None
    phi = np.zeros(N + 1, complex)
    for kk in range(K):
        phi[kk * d:(kk + 1) * d] = tau ** kk * psi
    L = laplace(N, J)
    res = float(np.max(np.abs(residuum(L, w2, phi))))
    sp = np.abs(psi) ** 2
    anteil = float(sp[0] / sp.sum())
    r.update(residuum=res, anteil=anteil, amp=float(abs(psi[0])))
    r["existiert"] = bool(res < 1e-10 and anteil >= 0.5)
    if r["existiert"]:
        r.update(stab(L, w2, phi))
    return r, phi


def drei_orte(N):
    return [0, int(round(N / 3)), int(round(2 * N / 3))]


def dreier(N, J, gross, w2, schritte=40):
    pos = drei_orte(N)
    r = {"fam": "L-b", "N": N, "orte": pos, "J": J, "ast": "gross" if gross else "klein", "w2": w2}
    S0 = s_ast(w2, gross)
    if S0 is None:
        r.update(existiert=False, grund="kein_start")
        return r, None
    phi0 = np.zeros(N + 1, complex)
    for q, p in enumerate(pos):
        phi0[p] = np.sqrt(S0) * np.exp(2j * np.pi * q / 3)
    phi, ok, k, grund = fortsetzen(lambda Jk: laplace(N, Jk), lambda Jk: w2, J, phi0, 0, schritte)
    r.update(grund=grund, schritt=k)
    if not ok:
        r["existiert"] = False
        return r, None
    ph = np.angle(phi[pos])
    dif = np.angle(np.exp(1j * (np.roll(ph, -1) - ph)))
    windung = int(round(float(np.sum(dif)) / (2 * np.pi)))
    s = np.abs(phi) ** 2
    anteil = float(s[pos].sum() / s.sum())
    r.update(windung=windung, anteil=anteil, phasenschritt_abw=float(np.max(np.abs(dif - 2 * np.pi / 3))),
             nabe=float(abs(phi[N])), residuum=float(np.max(np.abs(residuum(laplace(N, J), w2, phi)))))
    r["existiert"] = bool(windung == 1 and anteil >= 0.5)
    if r["existiert"]:
        r.update(stab(laplace(N, J), w2, phi))
    return r, phi


def bogen(N, K, m, J, gross, w2, schritte=40):
    r = {"fam": "L-c", "N": N, "K": K, "m": m, "J": J, "ast": "gross" if gross else "klein", "w2": w2}
    S0 = s_ast(w2, gross)
    if S0 is None:
        r.update(existiert=False, grund="kein_start")
        return r, None
    phi0 = np.zeros(N + 1, complex)
    jj = np.arange(K)
    phi0[:K] = np.sqrt(S0) * np.exp(2j * np.pi * m * jj / N)
    phi, ok, k, grund = fortsetzen(lambda Jk: laplace(N, Jk), lambda Jk: w2, J, phi0, 0, schritte)
    r.update(grund=grund, schritt=k)
    if not ok:
        r["existiert"] = False
        return r, None
    dif = np.angle(phi[1:K] * np.conj(phi[:K - 1]))
    s = np.abs(phi) ** 2
    r.update(phasenschritte=[float(x) for x in dif], anteil=float(s[:K].sum() / s.sum()))
    r["existiert"] = bool(np.max(np.abs(dif - 2 * np.pi * m / N)) < 0.3 and r["anteil"] >= 0.5)
    return r, phi


def teiler_faelle(Ns):
    f = []
    for N in Ns:
        for K in range(3, N):
            if N % K == 0:
                for mp in range(1, (K - 1) // 2 + 1):
                    f.append((N, K, mp))
    return f


def lokal(Ns, Js, w2s, pfad=None, bogen_N=(11, 12, 19, 20), bogen_w2=(0.6, 0.8)):
    out = {"modus": "lokal", "L-a": [], "L-b": [], "L-c": []}
    for (N, K, mp) in teiler_faelle(Ns):
        for J in Js:
            for gross in (False, True):
                for w2 in w2s:
                    r, _ = teilring(N, K, mp, J, gross, w2)
                    out["L-a"].append(r)
        if pfad:
            out["sekunden"] = time.time() - T0
            schreibe(out, pfad)
        print("L-a", N, K, mp, round(time.time() - T0, 1), "s", flush=True)
    for N in Ns:
        if N < 7 or N % 3 == 0:
            continue
        for J in Js:
            for gross in (False, True):
                for w2 in w2s:
                    r, _ = dreier(N, J, gross, w2)
                    out["L-b"].append(r)
        if pfad:
            out["sekunden"] = time.time() - T0
            schreibe(out, pfad)
        print("L-b", N, round(time.time() - T0, 1), "s", flush=True)
    for N in [x for x in bogen_N if x in Ns]:
        for K in (3, 4):
            for J in Js:
                for gross in (False, True):
                    for w2 in bogen_w2:
                        r, _ = bogen(N, K, 1, J, gross, w2)
                        out["L-c"].append(r)
    out["sekunden"] = time.time() - T0
    if pfad:
        schreibe(out, pfad)
    print("L-c fertig", round(time.time() - T0, 1), "s", flush=True)
    return out


# ---------------------------------------------------------------- Kontrolle gegen V5 (m = 0, reell)

V5_RASTER = [float(x) for x in np.round(np.arange(0.300, 0.9951, 0.005), 6)]


def v5_punkt(N, J, w2, site, gross, schritte=12):
    S0 = s_ast(w2, gross)
    if S0 is None:
        return None
    phi0 = np.zeros(N + 1, complex)
    phi0[site] = np.sqrt(S0)
    phi, ok, _, _ = fortsetzen(lambda Jk: laplace(N, Jk), lambda Jk: w2, J, phi0, site, schritte)
    if not ok:
        return None
    s = np.abs(phi) ** 2
    PR = float(s.sum() ** 2 / np.sum(s * s))
    if not (int(np.argmax(np.abs(phi))) == site and PR < 3.0 and abs(phi[site]) > 1e-3):
        return None
    return phi


def kontrolle(pfad=None, Ns=range(8, 22), Js=(0.05, 0.1), raster=V5_RASTER):
    out = {"modus": "kontrolle", "punkte": []}
    for J in Js:
        for N in Ns:
            L = laplace(N, J)
            for mode in ("ring", "zentrum"):
                site = N if mode == "zentrum" else 0
                for gross in (False, True):
                    for w2 in raster:
                        phi = v5_punkt(N, J, w2, site, gross)
                        if phi is None:
                            continue
                        r = {"N": N, "J": J, "mode": mode, "ast": "gross" if gross else "klein", "w2": w2,
                             "imag_max": float(np.max(np.abs(phi.imag)))}
                        r.update(stab(L, w2, phi))
                        r["v5_regel_stabil"] = bool(r["nK"] == 0 or (r["nK"] == 1 and r["dQdw"] < 0))
                        out["punkte"].append(r)
            if pfad:
                out["sekunden"] = time.time() - T0
                schreibe(out, pfad)
            print("kontrolle J", J, "N", N, round(time.time() - T0, 1), "s", flush=True)
    return out


def nmax(pfad=None, Js=(0.03, 0.04, 0.05, 0.06, 0.08), Ns=range(4, 27), raster=V5_RASTER):
    out = {"modus": "nmax", "existenz": []}
    for J in Js:
        for N in Ns:
            for gross in (False, True):
                gef = [w2 for w2 in raster if v5_punkt(N, J, w2, N, gross) is not None]
                out["existenz"].append({"J": J, "N": N, "ast": "gross" if gross else "klein", "anzahl": len(gef),
                                        "w2_min": (min(gef) if gef else None), "w2_max": (max(gef) if gef else None)})
        if pfad:
            out["sekunden"] = time.time() - T0
            schreibe(out, pfad)
        print("nmax J", J, round(time.time() - T0, 1), "s", flush=True)
    return out


# ---------------------------------------------------------------- Zeitentwicklung

def zeitlauf(N, m, J, gross, c, T=400.0, seed=7):
    from scipy.integrate import solve_ivp
    r, phi = wirbel(N, m, J, gross, c)
    if phi is None:
        return r
    w2 = r["w2"]
    w = np.sqrt(w2)
    L = laplace(N, J)
    n = N + 1
    rng = np.random.default_rng(seed)
    p0 = phi + 1e-6 * (rng.standard_normal(n) + 1j * rng.standard_normal(n))
    v0 = 1j * w * p0
    y0 = np.concatenate([p0.real, p0.imag, v0.real, v0.imag])

    def rhs(t, y):
        p = y[:n] + 1j * y[n:2 * n]
        acc = -(L @ p) - Vp(np.abs(p) ** 2) * p
        return np.concatenate([y[2 * n:], acc.real, acc.imag])

    def inv(y):
        p = y[:n] + 1j * y[n:2 * n]
        pd = y[2 * n:3 * n] + 1j * y[3 * n:]
        E = float(np.sum(np.abs(pd) ** 2) + np.real(np.conj(p) @ L @ p) + np.sum(V(np.abs(p) ** 2)))
        Q = float(2 * np.sum(np.imag(np.conj(p) * pd)))
        return E, Q

    t1 = time.time()
    ts = np.linspace(0, T, 4001)
    sol = solve_ivp(rhs, (0, T), y0, method="DOP853", rtol=1e-10, atol=1e-12, t_eval=ts)
    P = sol.y[:n] + 1j * sol.y[n:2 * n]
    Qr = P * np.exp(-1j * w * sol.t)[None, :]
    alpha = np.angle(np.conj(phi) @ Qr)
    dev = np.max(np.abs(Qr * np.exp(-1j * alpha)[None, :] - phi[:, None]), axis=0)
    EQ = np.array([inv(sol.y[:, k]) for k in range(sol.y.shape[1])])
    E0, Q0 = EQ[0]
    sel = (dev > 1e-5) & (dev < 1e-2)
    rate = None
    if np.sum(sel) >= 20:
        rate = float(np.polyfit(sol.t[sel], np.log(dev[sel]), 1)[0])
    r.update(T=T, status=int(sol.status), dev_start=float(dev[0]), dev_max=float(dev.max()), dev_ende=float(dev[-1]),
             rate_fit=rate, rel_dE=float(np.max(np.abs(EQ[:, 0] - E0)) / abs(E0)),
             rel_dQ=float(np.max(np.abs(EQ[:, 1] - Q0)) / abs(Q0)), sekunden=time.time() - t1,
             t=[float(x) for x in sol.t[::10]], dev=[float(x) for x in dev[::10]])
    return r


def zeit(pfad, faelle_extra=True):
    out = {"modus": "zeit", "laeufe": []}
    faelle = [(12, 1, 0.05, True, 0.6), (12, 5, 0.05, True, 0.6), (12, 1, 0.05, False, 0.6), (12, 5, 0.05, False, 0.6)]
    if faelle_extra:
        ordner = os.path.dirname(os.path.abspath(pfad))
        kand = []
        for f in sorted(glob.glob(os.path.join(ordner, "scan_J*.json"))):
            with open(f) as fh:
                for p in json.load(fh)["punkte"]:
                    if p.get("konvergiert") and p.get("art") == "oszillatorisch":
                        kand.append(p)
        wahl = [p for p in kand if p["N"] in (11, 12)] or kand
        if wahl:
            p = max(wahl, key=lambda q: q["maxRe"])
            faelle.append((p["N"], p["m"], p["J"], p["ast"] == "gross", p["c"]))
        out["oszillatorisch_kandidaten"] = len(kand)
    for (N, m, J, gross, c) in faelle:
        r = zeitlauf(N, m, J, gross, c)
        out["laeufe"].append(r)
        print({k: r.get(k) for k in ("N", "m", "J", "ast", "c", "maxRe", "art", "rate_fit", "dev_max", "rel_dE",
                                     "rel_dQ", "sekunden")}, flush=True)
        out["sekunden"] = time.time() - T0
        schreibe(out, pfad)
    return out


# ---------------------------------------------------------------- Hilfen

def schreibe(obj, pfad):
    with open(pfad + ".tmp", "w") as f:
        json.dump(obj, f)
    os.replace(pfad + ".tmp", pfad)


def main():
    modus, pfad = sys.argv[1], sys.argv[2]
    os.makedirs(os.path.dirname(os.path.abspath(pfad)), exist_ok=True)
    if modus == "schnell":
        out = {"modus": "schnell"}
        rng = np.random.default_rng(1)
        pk = []
        for N in (11, 12):
            for m in (1, 3):
                for gross in (False, True):
                    for c in (0.40, 0.6, 0.9):
                        r, _ = wirbel(N, m, 0.05, gross, c, rng=rng)
                        pk.append(r)
                        print({k: r.get(k) for k in ("N", "m", "ast", "c", "w2", "pfad", "konvergiert", "formel_abw",
                                                     "nabe", "neustart_abw", "maxRe", "art", "dom", "n_minus",
                                                     "kks_l", "kks_r", "null_betrag")}, flush=True)
        out["U"] = pk
        out["lokal"] = lokal([11, 12], [0.05], [0.6, 0.8], bogen_N=(11,), bogen_w2=(0.6,))
        for fam in ("L-a", "L-b", "L-c"):
            for r in out["lokal"][fam]:
                print(fam, {k: r.get(k) for k in ("N", "K", "m", "ast", "w2", "existiert", "grund", "residuum",
                                                  "anteil", "windung", "maxRe", "art", "kks_l", "kks_r")}, flush=True)
        kt = kontrolle(Ns=[11], Js=[0.05], raster=[0.5, 0.7, 0.9, 0.95])
        for r in kt["punkte"]:
            print("V5", {k: r.get(k) for k in ("N", "mode", "ast", "w2", "maxRe", "art", "nK", "dQdw",
                                              "v5_regel_stabil", "kks_l", "kks_r")}, flush=True)
        out["kontrolle"] = kt
        z = zeitlauf(12, 1, 0.05, False, 0.6, T=60.0)
        print("zeit", {k: z.get(k) for k in ("maxRe", "art", "rate_fit", "dev_max", "rel_dE", "rel_dQ", "sekunden")})
        out["sekunden"] = time.time() - T0
        schreibe(out, pfad)
    elif modus == "kontrolle":
        kontrolle(pfad=pfad)
    elif modus == "nmax":
        nmax(pfad=pfad)
    elif modus == "scan":
        J = float(sys.argv[3])
        Ns = range(int(sys.argv[4]), int(sys.argv[5]) + 1) if len(sys.argv) > 5 else range(4, 25)
        scan(J, Ns, pfad=pfad)
    elif modus == "lokal":
        Ns = list(range(int(sys.argv[3]), int(sys.argv[4]) + 1)) if len(sys.argv) > 4 else list(range(4, 25))
        lokal(Ns, JS, c_raster(), pfad=pfad)
    elif modus == "zeit":
        zeit(pfad)
    print("fertig", modus, round(time.time() - T0, 1), "s", flush=True)


if __name__ == "__main__":
    main()
