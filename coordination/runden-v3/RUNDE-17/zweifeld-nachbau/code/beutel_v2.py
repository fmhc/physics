#!/usr/bin/env python3
# BEUTEL-1 (Runde 16): radiale Q-Ball-Loesungen fuer M1, M2, M3 der Karte. Eigener Code (numpy/scipy).
# Diskretes Funktional auf zellzentriertem Gitter, Newton bei festem omega oder festem Q (geraendert),
# Saat per Gradientenfluss bei festem Q. Siehe PLAN.md Abschnitt 2.
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_k, "1")
import sys, json, time, argparse
import numpy as np
from scipy.linalg import solve_banded


class Model:
    def __init__(self, name):
        assert name in ("M1", "M2", "M3")
        self.name = name
        self.m2 = 1.0 if name == "M1" else 2.0  # psi-Vakuummasse^2

    def U(self, S, g):
        if self.name == "M1":
            return S - S**2 + 0.5 * S**3
        if self.name == "M2":
            return 0.25 * (g * g - 1) ** 2 + (1 + g * g) * S - S**2 + 0.5 * S**3
        return 0.25 * (g * g - 1) ** 2 + 2 * g * g * S

    def d(self, S, g):
        # U_S, U_SS, U_g, U_gg, U_Sg
        z = np.zeros_like(S)
        if self.name == "M1":
            return 1 - 2 * S + 1.5 * S**2, -2 + 3 * S, z, z, z
        if self.name == "M2":
            return ((1 + g * g) - 2 * S + 1.5 * S**2, -2 + 3 * S,
                    g * (g * g - 1) + 2 * g * S, 3 * g * g - 1 + 2 * S, 2 * g)
        return (2 * g * g, z, g * (g * g - 1) + 4 * g * S, 3 * g * g - 1 + 4 * S, 4 * g)


class Grid:
    def __init__(self, dr, Rmax):
        self.dr = dr
        self.N = N = int(round(Rmax / dr))
        i = np.arange(N)
        self.r = (i + 0.5) * dr
        self.a = 4 * np.pi * ((i + 1) * dr) ** 2          # Flaeche bei r_{i+1/2}
        self.am = np.concatenate([[0.0], self.a[:-1]])     # Flaeche bei r_{i-1/2}, am[0] = 0
        self.V = 4 * np.pi * dr * (self.r**2 + dr * dr / 12.0)  # exaktes Schalenvolumen
        self.Rmax = N * dr


def lap(G, u, ubc):
    up = np.append(u[1:], ubc)
    um = np.concatenate([[0.0], u[:-1]])
    return (G.a * (up - u) - G.am * (u - um)) / G.dr


def residual(M, G, f, g, lam):
    S = f * f
    US, USS, Ug, Ugg, USg = M.d(S, g)
    Rf = G.V * (2 * f * US - 2 * lam * f) - 2 * lap(G, f, 0.0)
    Rg = G.V * Ug - lap(G, g, 1.0)
    return Rf, Rg


def pack(f, g):
    x = np.empty(2 * f.size)
    x[0::2] = f
    x[1::2] = g
    return x


def resnorm(G, Rf, Rg):
    return float(max(np.max(np.abs(Rf) / G.V), np.max(np.abs(Rg) / G.V)))


def jac_banded(M, G, f, g, lam):
    N = G.N
    S = f * f
    US, USS, Ug, Ugg, USg = M.d(S, g)
    d_ff = G.V * (2 * US + 4 * S * USS - 2 * lam) + 2 * (G.a + G.am) / G.dr
    d_gg = G.V * Ugg + (G.a + G.am) / G.dr
    d_fg = G.V * 2 * f * USg
    o_ff = -2 * G.a / G.dr
    o_gg = -G.a / G.dr
    ab = np.zeros((5, 2 * N))
    ab[2, 0::2] = d_ff
    ab[2, 1::2] = d_gg
    ab[1, 1::2] = d_fg          # A[f_i, g_i]
    ab[3, 0::2] = d_fg          # A[g_i, f_i]
    ab[0, 2::2] = o_ff[:-1]     # A[f_i, f_i+1]
    ab[0, 3::2] = o_gg[:-1]     # A[g_i, g_i+1]
    ab[4, 0:-2:2] = o_ff[:-1]   # A[f_i+1, f_i]
    ab[4, 1:-2:2] = o_gg[:-1]   # A[g_i+1, g_i]
    return ab


def newton_w(M, G, f, g, lam, tol=1e-9, maxit=30):
    f = f.copy(); g = g.copy()
    err = np.inf
    for it in range(maxit + 1):
        Rf, Rg = residual(M, G, f, g, lam)
        err = resnorm(G, Rf, Rg)
        if not np.isfinite(err):
            return f, g, it, err, False
        if err < tol:
            return f, g, it, err, True
        if it == maxit:
            break
        ab = jac_banded(M, G, f, g, lam)
        dx = solve_banded((2, 2), ab, -pack(Rf, Rg), check_finite=False)
        f += dx[0::2]; g += dx[1::2]
    return f, g, maxit, err, False


def newton_Q(M, G, f, g, lam, Q, tol=1e-9, maxit=30):
    f = f.copy(); g = g.copy()
    err = np.inf
    for it in range(maxit + 1):
        if not (lam > 0):
            return f, g, lam, it, np.inf, False
        Rf, Rg = residual(M, G, f, g, lam)
        N2 = float(np.sum(G.V * f * f))
        C = 2 * np.sqrt(lam) * N2 - Q
        err = max(resnorm(G, Rf, Rg), abs(C) / Q)
        if not np.isfinite(err):
            return f, g, lam, it, err, False
        if err < tol:
            return f, g, lam, it, err, True
        if it == maxit:
            break
        ab = jac_banded(M, G, f, g, lam)
        R = pack(Rf, Rg)
        z = np.zeros_like(g)
        b = pack(-2 * G.V * f, z)
        c = pack(4 * np.sqrt(lam) * G.V * f, z)
        dd = N2 / np.sqrt(lam)
        y = solve_banded((2, 2), ab, np.column_stack([-R, b]), check_finite=False)
        y1, y2 = y[:, 0], y[:, 1]
        dlam = (-C - c @ y1) / (dd - c @ y2)
        dx = y1 - y2 * dlam
        f += dx[0::2]; g += dx[1::2]; lam += dlam
    return f, g, lam, maxit, err, False


def implicit_solve(G, coef, dt, rhs, ubc):
    w = dt * coef / G.V
    ab = np.zeros((3, G.N))
    ab[1] = 1 + w * (G.a + G.am) / G.dr
    ab[0, 1:] = -(w * G.a / G.dr)[:-1]
    ab[2, :-1] = -(w * G.am / G.dr)[1:]
    r = rhs.copy()
    r[-1] += w[-1] * G.a[-1] / G.dr * ubc
    return solve_banded((1, 1), ab, r, check_finite=False)


def flow(M, G, f, g, Q, dt=0.05, tmax=400.0, tol=1e-6):
    """Gradientenfluss auf E_Q[f,g] = Q^2/(4 Int f^2) + Int[f'^2 + g'^2/2 + U], halbimplizit."""
    f = f.copy(); g = g.copy()
    err = np.inf
    n = 0
    for n in range(int(tmax / dt)):
        N2 = np.sum(G.V * f * f)
        lam = (Q / (2 * N2)) ** 2
        US, USS, Ug, Ugg, USg = M.d(f * f, g)
        f = implicit_solve(G, 2.0, dt, f - dt * (2 * f * US - 2 * lam * f), 0.0)
        g = implicit_solve(G, 1.0, dt, g - dt * Ug, 1.0)
        if n % 200 == 0:
            lam = (Q / (2 * np.sum(G.V * f * f))) ** 2
            err = resnorm(G, *residual(M, G, f, g, lam))
            if err < tol:
                break
    lam = (Q / (2 * np.sum(G.V * f * f))) ** 2
    return f, g, float(lam), float(err), n


def observables(M, G, f, g, lam):
    S = f * f
    U = M.U(S, g)
    df = np.append(f[1:], 0.0) - f
    dg = np.append(g[1:], 1.0) - g
    Tf = float(np.sum(G.a * df * df) / G.dr)
    Tg = float(0.5 * np.sum(G.a * dg * dg) / G.dr)
    T = Tf + Tg
    N2 = float(np.sum(G.V * S))
    om = float(np.sqrt(lam))
    Q = 2 * om * N2
    Upot = float(np.sum(G.V * U))
    E = lam * N2 + Upot + T
    P = lam * N2 - Upot
    shell = Tg + float(np.sum(G.V * 0.25 * (g * g - 1) ** 2))
    S0 = float(S[0])
    below = np.nonzero(S < 0.5 * S0)[0]
    if below.size and below[0] > 0:
        k = below[0]
        Rh = float(G.r[k - 1] + (0.5 * S0 - S[k - 1]) * (G.r[k] - G.r[k - 1]) / (S[k] - S[k - 1]))
    else:
        Rh = float("nan")
    f0 = float(f[0])
    nodes = int(np.sum(f < -1e-10 * abs(f0)))
    chimono = bool(np.all(np.diff(g) >= -1e-10)) if M.name != "M1" else True
    Rf, Rg = residual(M, G, f, g, lam)
    return dict(omega2=float(lam), omega=om, Q=Q, E=E, EQ=E / Q, S0=S0, chi0=float(g[0]),
                h=shell / E, T=T, P3=3 * P, vir=abs(T - 3 * P) / T, err=resnorm(G, Rf, Rg),
                Rhalf=Rh, ftail=float(abs(f[-1]) / abs(f0)), gtail=float(abs(1 - g[-1])),
                fmin_rel=float(np.min(f) / f0), nodes=nodes, chimono=chimono,
                dr=G.dr, Rmax=G.Rmax)


def initial_profile(M, G, Q):
    r = G.r
    if M.name == "M3":
        R0 = Q ** 0.25
        prof = np.where(r < R0, np.sinc(r / R0), 0.0)
        om = np.pi / R0
        A = np.sqrt((Q / (2 * om)) / np.sum(G.V * prof**2))
        f = A * prof
        g = 0.5 * (1 + np.tanh(2 * (r - R0)))
        return f, g
    fin, om, g_in = (1.0, 0.75, None) if M.name == "M1" else (np.sqrt(1.18), 0.9, 0.0)
    R0 = (Q / (2 * om * fin**2 * 4 * np.pi / 3)) ** (1 / 3)
    f = fin * 0.5 * (1 - np.tanh(r - R0))
    g = np.ones_like(r) if M.name == "M1" else 0.5 * (1 + np.tanh(r - R0))
    return f, g


def to_grid(Gfrom, Gto, f, g):
    return (np.interp(Gto.r, Gfrom.r, f, right=0.0), np.interp(Gto.r, Gfrom.r, g, right=1.0))


def q_sweep(M, G, f, g, lam, Q, Qmax, out, prof, sexp, fac0=1.25, margin=40.0, log=print):
    fac = fac0
    hist = [(np.log(Q), lam)]
    while Q < Qmax * (1 - 1e-12):
        Qn = min(Q * fac, Qmax)
        s = (Qn / Q) ** sexp
        fp = np.interp(G.r / s, G.r, f, right=0.0)
        gp = np.interp(G.r / s, G.r, g, right=1.0)
        if len(hist) >= 2:
            (l1, a1), (l0, a0) = hist[-1], hist[-2]
            lamp = a1 + (np.log(Qn) - l1) * (a1 - a0) / (l1 - l0)
        else:
            lamp = lam
        if lamp <= 0:
            lamp = lam
        fp *= np.sqrt(Qn / (2 * np.sqrt(lamp) * np.sum(G.V * fp * fp)))
        fn, gn, lamn, it, err, ok = newton_Q(M, G, fp, gp, lamp, Qn)
        if ok and fn[0] > 0 and np.min(fn) > -1e-8 * fn[0]:
            f, g, lam, Q = fn, gn, lamn, Qn
            hist.append((np.log(Q), lam))
            o = observables(M, G, f, g, lam); o["sweep"] = "Q"; o["it"] = it
            out.append(o); prof.append((f.copy(), g.copy()))
            if o["Rhalf"] > G.Rmax - margin:
                log(f"Q-Fortsetzung: Rand erreicht bei Q={Q:.4g}, Rhalf={o['Rhalf']:.1f}")
                break
            if it <= 5:
                fac = min(fac ** 1.5, fac0)
        else:
            fac = np.sqrt(fac)
            log(f"Q-Fortsetzung: kein Erfolg bei Qn={Qn:.4g} (it={it}, err={err:.2e}); fac -> {fac:.5f}")
            if fac < 1.0005:
                log("Q-Fortsetzung abgebrochen")
                break
    return f, g, lam, Q


def mu_sweep(M, G, f, g, lam, mu_end, out, prof, step0=0.05, stepmax=0.15, log=print):
    mu = M.m2 - lam
    step = step0
    hist = [(np.log(mu), f.copy(), g.copy())]
    Qprev = observables(M, G, f, g, lam)["Q"]
    while mu > mu_end * (1 + 1e-9):
        lnn = max(np.log(mu) - step, np.log(mu_end))
        if len(hist) >= 2:
            (l1, f1, g1), (l0, f0, g0) = hist[-1], hist[-2]
            t = (lnn - l1) / (l1 - l0)
            fp = f1 + t * (f1 - f0); gp = g1 + t * (g1 - g0)
        else:
            fp, gp = hist[-1][1], hist[-1][2]
        lamn = M.m2 - np.exp(lnn)
        fn, gn, it, err, ok = newton_w(M, G, fp, gp, lamn)
        sane = False
        if ok:
            o = observables(M, G, fn, gn, lamn)
            sane = (o["nodes"] == 0 and fn[0] > 0 and abs(np.log(o["Q"] / Qprev)) < 0.3)
        if ok and sane:
            mu = np.exp(lnn); f, g, lam = fn, gn, lamn
            hist.append((lnn, f.copy(), g.copy()))
            if len(hist) > 2:
                hist.pop(0)
            o["sweep"] = "mu"; o["it"] = it
            out.append(o); prof.append((f.copy(), g.copy()))
            Qprev = o["Q"]
            if it <= 4:
                step = min(step * 1.3, stepmax)
        else:
            step /= 2
            log(f"mu-Fortsetzung: kein Erfolg bei omega2={lamn:.6f} (ok={ok}, it={it}, err={err:.2e}); step -> {step:.2e}")
            if step < 1e-4:
                log("mu-Fortsetzung abgebrochen (moegliche Faltung in omega)")
                break
    return f, g, lam


def control(M, Gc, pts, profs, Gn, log=print):
    res = []
    for o, (f, g) in zip(pts, profs):
        fi, gi = to_grid(Gc, Gn, f, g)
        if o["sweep"] == "mu":
            fn, gn, it, err, ok = newton_w(M, Gn, fi, gi, o["omega2"])
            lamn = o["omega2"]
        else:
            fn, gn, lamn, it, err, ok = newton_Q(M, Gn, fi, gi, o["omega2"], o["Q"])
        if ok:
            q = observables(M, Gn, fn, gn, lamn)
        else:
            q = dict(failed=True, err=err)
        q["sweep"] = o["sweep"]; q["ok"] = bool(ok)
        res.append(q)
    return res


def initial_profile_B(M, G, Q):
    """Nachtrag N3: alternativer Start, Gauss-Profil fuer f, chi = 1 ueberall."""
    r = G.r
    if M.name == "M3":
        R0 = Q ** 0.25
    else:
        R0 = (Q / (2 * 0.8 * np.sqrt(M.m2) * 4 * np.pi / 3)) ** (1 / 3)
    om = 0.9 * np.sqrt(M.m2)
    prof = np.exp(-(r / (0.8 * R0)) ** 2)
    A = np.sqrt((Q / (2 * om)) / np.sum(G.V * prof**2))
    return A * prof, np.ones_like(r)


def konkurrenz(M, dr, Qs, log=print):
    res = []
    for Q in Qs:
        Rest = Q ** 0.25 if M.name == "M3" else (Q / 4.0) ** (1 / 3)
        Gk = Grid(dr, max(40.0, 3 * Rest + 20))
        row = dict(Q=Q)
        for tag, init in (("A", initial_profile), ("B", initial_profile_B)):
            f, g = init(M, Gk, Q)
            f, g, lam, ferr, nfl = flow(M, Gk, f, g, Q, tmax=600.0)
            f, g, lam, it, err, ok = newton_Q(M, Gk, f, g, lam, Q)
            o = observables(M, Gk, f, g, lam) if ok else dict(E=float("nan"))
            row[tag] = dict(ok=bool(ok), flow_steps=nfl, flow_err=ferr, newton_it=it, E=o.get("E"),
                            omega2=o.get("omega2"), S0=o.get("S0"), chi0=o.get("chi0"), nodes=o.get("nodes"))
        row["dE_rel_BminusA"] = (row["B"]["E"] - row["A"]["E"]) / row["A"]["E"]
        log(f"Konkurrenz Q={Q:.4g}: E_A={row['A']['E']:.10g} E_B={row['B']['E']:.10g} rel={row['dE_rel_BminusA']:.2e}")
        res.append(row)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dr3", action="store_true")
    ap.add_argument("--konkurrenz", default="")
    ap.add_argument("--model", required=True)
    ap.add_argument("--dr", type=float, default=0.04)
    ap.add_argument("--rmax", type=float, default=350.0)
    ap.add_argument("--qseed", type=float, required=True)
    ap.add_argument("--qmax", type=float, required=True)
    ap.add_argument("--muend", type=float, default=0.01)
    ap.add_argument("--seedR", type=float, default=40.0)
    ap.add_argument("--nocontrol", action="store_true")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    logs = []

    def log(s):
        line = f"[{time.time() - t0:7.1f}s] {s}"
        print(line, flush=True); logs.append(line)

    M = Model(a.model)
    Gs = Grid(a.dr, a.seedR)
    f, g = initial_profile(M, Gs, a.qseed)
    f, g, lam, ferr, nfl = flow(M, Gs, f, g, a.qseed)
    log(f"Fluss: Schritte={nfl}, err={ferr:.2e}, omega2={lam:.6f}")
    f, g, lam, it, err, ok = newton_Q(M, Gs, f, g, lam, a.qseed)
    log(f"Saat-Newton klein: ok={ok}, it={it}, err={err:.2e}, omega2={lam:.8f}")
    G = Grid(a.dr, a.rmax)
    f, g = to_grid(Gs, G, f, g)
    f, g, lam, it, err, ok = newton_Q(M, G, f, g, lam, a.qseed)
    log(f"Saat-Newton gross: ok={ok}, it={it}, err={err:.2e}, omega2={lam:.8f}")
    if not ok:
        log("Saat gescheitert"); sys.exit(2)
    pts, profs = [], []
    o = observables(M, G, f, g, lam); o["sweep"] = "seed"; o["it"] = it
    pts.append(o); profs.append((f.copy(), g.copy()))
    seed = (f.copy(), g.copy(), lam)
    sexp = 0.25 if a.model == "M3" else 1 / 3
    q_sweep(M, G, f, g, lam, a.qseed, a.qmax, pts, profs, sexp, log=log)
    log(f"Q-Ast fertig: {sum(p['sweep'] == 'Q' for p in pts)} Punkte, groesstes Q={max(p['Q'] for p in pts):.4g}")
    f, g, lam = seed
    mu_sweep(M, G, f, g, lam, a.muend, pts, profs, log=log)
    log(f"mu-Ast fertig: {sum(p['sweep'] == 'mu' for p in pts)} Punkte, groesstes omega2={max(p['omega2'] for p in pts):.6f}")
    result = dict(model=a.model, args=vars(a), points=pts)
    if not a.nocontrol:
        Gf = Grid(a.dr / 2, a.rmax)
        result["control_fine"] = control(M, G, pts, profs, Gf, log=log)
        log("Kontrolle feines Gitter fertig")
        Gb = Grid(a.dr, a.rmax * 1.5)
        result["control_bigR"] = control(M, G, pts, profs, Gb, log=log)
        log("Kontrolle grosser Radius fertig")
    if a.dr3:
        G3 = Grid(a.dr / 4, a.rmax)
        result["control_fine2"] = control(M, G, pts, profs, G3, log=log)
        log("Nachtrag N1: drittes Gitter dr/4 fertig")
    if a.konkurrenz:
        result["konkurrenz"] = konkurrenz(M, a.dr, [float(x) for x in a.konkurrenz.split(",")], log=log)
        log("Nachtrag N3: Konkurrenzpruefung fertig")
    result["laufzeit_s"] = time.time() - t0
    result["log"] = logs
    with open(a.out + ".json", "w") as fh:
        json.dump(result, fh, indent=1)
    sub = slice(0, None, 4)
    np.savez_compressed(a.out + "-profile.npz", r=G.r[sub],
                        f=np.array([p[0][sub] for p in profs], dtype=np.float32),
                        g=np.array([p[1][sub] for p in profs], dtype=np.float32),
                        Q=np.array([p["Q"] for p in pts]), omega2=np.array([p["omega2"] for p in pts]),
                        sweep=np.array([p["sweep"] for p in pts]))
    log(f"fertig, {len(pts)} Punkte")


if __name__ == "__main__":
    main()
