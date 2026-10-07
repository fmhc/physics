#!/usr/bin/env python3
"""V2 Maxwell-Ring mit Gravitation (Runde 16, ausprobieren).
N Massen eps auf R = 1 um M = 1 (im Schwerpunkt, beweglich), G = 1.
Lineare Stabilitaet im mitrotierenden System:
  Methode A: volles (N+1)-Koerper-System, analytische Hesse-Matrix, 2D und 3D.
  Methode B: heliozentrisch (Schwerpunkt abgetrennt), Jacobi-Matrix per finiter Differenzen, 2D.
eps-Raster, Bisektion der Grenze eps_c(N), Skalierung, Zeitentwicklung N = 6 und 8.
Aufruf: python v2_maxwell.py <ausgabeordner> [schnell]
"""
import json, os, sys, time
import numpy as np
from scipy.integrate import solve_ivp

OUT = sys.argv[1] if len(sys.argv) > 1 else "aus"
SCHNELL = len(sys.argv) > 2 and sys.argv[2] == "schnell"
os.makedirs(OUT, exist_ok=True)
T0 = time.time()
TOL = 1e-6


def config(N, eps, dim=2):
    th = 2 * np.pi * np.arange(N) / N
    X = np.zeros((N + 1, dim))
    X[1:, 0] = np.cos(th)
    X[1:, 1] = np.sin(th)
    m = np.concatenate([[1.0], np.full(N, eps)])
    S = np.sum(1.0 / np.sin(np.pi * np.arange(1, N) / N))
    Om = np.sqrt(1.0 + eps * S / 4.0)
    return X, m, Om


def grad_eff(X, m, Om):
    n, dim = X.shape
    g = np.zeros_like(X)
    for i in range(n):
        d = X[i] - X
        r = np.linalg.norm(d, axis=1)
        r[i] = np.inf
        g[i] = np.sum((m[i] * m / r ** 3)[:, None] * d, axis=0)
    P = np.ones(dim)
    if dim == 3:
        P[2] = 0
    return g - Om ** 2 * m[:, None] * X * P


def hess_U(X, m):
    n, dim = X.shape
    H = np.zeros((n * dim, n * dim))
    I = np.eye(dim)
    for i in range(n):
        for j in range(i + 1, n):
            d = X[i] - X[j]
            r = np.linalg.norm(d)
            u = d / r
            B = m[i] * m[j] / r ** 3 * (I - 3 * np.outer(u, u))
            si, sj = slice(dim * i, dim * i + dim), slice(dim * j, dim * j + dim)
            H[si, si] += B
            H[sj, sj] += B
            H[si, sj] -= B
            H[sj, si] -= B
    return H


def companion_A(N, eps, dim=2):
    X, m, Om = config(N, eps, dim)
    n = N + 1
    H = hess_U(X, m)
    P = np.eye(dim)
    Jm = np.zeros((dim, dim))
    Jm[0, 1], Jm[1, 0] = -1, 1
    if dim == 3:
        P[2, 2] = 0
    Mv = np.repeat(m, dim)
    Keff = H - Om ** 2 * np.kron(np.diag(m), P)
    G = 2 * Om * np.kron(np.diag(m), Jm)
    Minv = 1.0 / Mv
    A = np.zeros((2 * n * dim, 2 * n * dim))
    A[:n * dim, n * dim:] = np.eye(n * dim)
    A[n * dim:, :n * dim] = -Minv[:, None] * Keff
    A[n * dim:, n * dim:] = -Minv[:, None] * G
    return A, Om


def helio_acc(r, eps):
    # r: (N,2) heliozentrisch; Beschleunigung im Inertialsystem
    N = r.shape[0]
    rn = np.linalg.norm(r, axis=1)
    a = -(1.0 + eps) * r / rn[:, None] ** 3
    for i in range(N):
        d = r - r[i]
        dn = np.linalg.norm(d, axis=1)
        dn[i] = np.inf
        a[i] += eps * np.sum(d / dn[:, None] ** 3, axis=0)
        mask = np.ones(N, bool)
        mask[i] = False
        a[i] -= eps * np.sum(r[mask] / rn[mask][:, None] ** 3, axis=0)
    return a


def companion_B(N, eps, h=1e-6):
    X, m, Om = config(N, eps, 2)
    r0 = X[1:] - X[0]
    n2 = 2 * N
    Df = np.zeros((n2, n2))
    for c in range(n2):
        e = np.zeros(n2)
        e[c] = h
        Df[:, c] = (helio_acc((r0.ravel() + e).reshape(N, 2), eps).ravel()
                    - helio_acc((r0.ravel() - e).reshape(N, 2), eps).ravel()) / (2 * h)
    Jm = np.array([[0, -1], [1, 0]], float)
    A = np.zeros((2 * n2, 2 * n2))
    A[:n2, n2:] = np.eye(n2)
    A[n2:, :n2] = Df + Om ** 2 * np.eye(n2)
    A[n2:, n2:] = -2 * Om * np.kron(np.eye(N), Jm)
    resid = helio_acc(r0, eps) + Om ** 2 * r0
    return A, Om, float(np.max(np.abs(resid)))


def maxre(A):
    s = np.linalg.eigvals(A)
    return float(np.max(s.real)), s


def maxre_ohne_dreh(s):
    # die zwei Eigenwerte mit kleinstem |s| = Drehmode und Partner (Jordan-Block bei 0)
    idx = np.argsort(np.abs(s))
    rest = s[idx[2:]]
    return float(np.max(rest.real)), float(np.max(np.abs(s[idx[:2]])))


res = {"versuch": "V2", "tol": TOL}

# 1) Tabelle N = 3..16, eps = 1e-6, 1e-4: A 2D, B 2D, A 3D
tab = []
for N in range(3, 17):
    for eps in (1e-6, 1e-4):
        X, m, Om = config(N, eps, 2)
        g = float(np.max(np.abs(grad_eff(X, m, Om)) / m[:, None]))
        A2, _ = companion_A(N, eps, 2)
        mA, sA = maxre(A2)
        B2, _, rB = companion_B(N, eps)
        mB, sB = maxre(B2)
        A3, _ = companion_A(N, eps, 3)
        m3, s3 = maxre(A3)
        mA_od, nullA = maxre_ohne_dreh(sA)
        mB_od, nullB = maxre_ohne_dreh(sB)
        m3_od, null3 = maxre_ohne_dreh(s3)
        n0 = int(np.sum(np.abs(sA) < 1e-6))
        nOm = int(np.sum(np.abs(sA - 1j * Om) < 1e-6) + np.sum(np.abs(sA + 1j * Om) < 1e-6))
        tab.append({"N": N, "eps": eps, "Omega": Om, "kraeftebilanz_resid": g, "helio_resid": rB,
                    "maxRe_A2D": mA, "maxRe_B2D": mB, "maxRe_A3D": m3,
                    "maxRe_A2D_ohne_dreh": mA_od, "maxRe_B2D_ohne_dreh": mB_od, "maxRe_A3D_ohne_dreh": m3_od,
                    "betrag_drehpaar_A_B_3D": [nullA, nullB, null3],
                    "stabil_A2D": mA <= TOL, "stabil_B2D": mB_od <= TOL, "stabil_A3D": m3 <= TOL,
                    "stabil_tol1e-5": mA <= 1e-5, "stabil_tol1e-7": mA <= 1e-7,
                    "n_eig_nahe_0": n0, "n_eig_nahe_pm_iOmega": nOm})
        print(f"N={N:2d} eps={eps:g} maxRe A2D={mA:.3e} B2D={mB:.3e} (ohne Dreh {mB_od:.3e}) A3D={m3:.3e} n0={n0} nOm={nOm}", flush=True)
res["tabelle"] = tab

# Hesse-Kontrolle per finiter Differenzen (N = 7)
X, m, Om = config(7, 1e-4, 2)
H = hess_U(X, m)
h = 1e-5
Hfd = np.zeros_like(H)
xf = X.ravel()


def gradU(xf_):
    Xq = xf_.reshape(X.shape)
    return (grad_eff(Xq, m, 0.0)).ravel()


for c in range(xf.size):
    e = np.zeros(xf.size)
    e[c] = h
    Hfd[:, c] = (gradU(xf + e) - gradU(xf - e)) / (2 * h)
res["hesse_fd_relabw_N7"] = float(np.max(np.abs(Hfd - H)) / np.max(np.abs(H)))

# 2) eps-Raster und Bisektion
Ns = list(range(3, 41)) + ([48, 64] if not SCHNELL else [])
if SCHNELL:
    Ns = list(range(3, 11))
grid = 10.0 ** np.linspace(-9, -1, 81)
scan = []
for N in Ns:
    mr = []
    for eps in grid:
        A2, _ = companion_A(N, eps, 2)
        mr.append(maxre(A2)[0])
    mr = np.array(mr)
    st = mr <= TOL
    wechsel = int(np.sum(st[1:] != st[:-1]))
    eintrag = {"N": N, "maxRe": mr.tolist(), "stabil": st.tolist(), "wechsel": wechsel}
    if st[0]:
        iu = np.argmax(~st) if np.any(~st) else None
        if iu is not None and iu > 0:
            lo, hi = np.log10(grid[iu - 1]), np.log10(grid[iu])
            for _ in range(40):
                mid = 0.5 * (lo + hi)
                if maxre(companion_A(N, 10 ** mid, 2)[0])[0] <= TOL:
                    lo = mid
                else:
                    hi = mid
            eintrag["eps_c"] = 10 ** lo
            eintrag["eps_c_N3"] = 10 ** lo * N ** 3
            # Kontrolle der Grenze mit Methode B und tol 1e-5/1e-7
            ec = 10 ** lo
            eintrag["B_knapp_unter"] = maxre_ohne_dreh(maxre(companion_B(N, ec * 0.99)[0])[1])[0]
            eintrag["B_knapp_ueber"] = maxre_ohne_dreh(maxre(companion_B(N, ec * 1.01)[0])[1])[0]
            eintrag["A3D_knapp_unter"] = maxre(companion_A(N, ec * 0.99, 3)[0])[0]
    scan.append(eintrag)
    print(f"N={N:2d} wechsel={wechsel} eps_c={eintrag.get('eps_c')} eps_c*N^3={eintrag.get('eps_c_N3')}", flush=True)
res["eps_raster"] = grid.tolist()
res["scan"] = scan
pts = [(e["N"], e["eps_c"]) for e in scan if "eps_c" in e and e["N"] >= 20]
if len(pts) >= 3:
    lN = np.log([p[0] for p in pts])
    le = np.log([p[1] for p in pts])
    p_, c_ = np.polyfit(lN, le, 1)
    res["fit_N20plus"] = {"steigung": float(p_), "vorfaktor": float(np.exp(c_))}
    print("Fit N>=20: Steigung", p_, "Vorfaktor", np.exp(c_), flush=True)

# 3) Zeitentwicklung N = 6 und 8, eps = 1e-4
def rhs(t, y, m):
    n = m.size
    x = y[:2 * n].reshape(n, 2)
    v = y[2 * n:]
    a = np.zeros((n, 2))
    for i in range(n):
        d = x - x[i]
        r = np.linalg.norm(d, axis=1)
        r[i] = np.inf
        a[i] = np.sum((m / r ** 3)[:, None] * d, axis=0)
    return np.concatenate([v, a.ravel()])


def inv(y, m):
    n = m.size
    x = y[:2 * n].reshape(n, 2)
    v = y[2 * n:].reshape(n, 2)
    E = 0.5 * np.sum(m * np.sum(v ** 2, axis=1))
    for i in range(n):
        for j in range(i + 1, n):
            E -= m[i] * m[j] / np.linalg.norm(x[i] - x[j])
    L = np.sum(m * (x[:, 0] * v[:, 1] - x[:, 1] * v[:, 0]))
    return E, L


def shape(y, m):
    n = m.size
    x = y[:2 * n].reshape(n, 2)
    r = x[1:] - x[0]
    rad = np.linalg.norm(r, axis=1)
    ang = np.sort(np.mod(np.arctan2(r[:, 1], r[:, 0]), 2 * np.pi))
    gaps = np.diff(np.concatenate([ang, [ang[0] + 2 * np.pi]]))
    return float(np.sqrt(np.std(rad) ** 2 + np.std(gaps) ** 2 * np.mean(rad) ** 2))


zeitl = []
Tend = 600.0 if SCHNELL else 3000.0
for N in (6, 8):
    eps = 1e-4
    X, m, Om = config(N, eps, 2)
    V = np.zeros_like(X)
    V[:, 0] = -Om * X[:, 1]
    V[:, 1] = Om * X[:, 0]
    rng = np.random.default_rng(2)
    Xp = X.copy()
    Xp[1:] += 1e-7 * rng.standard_normal((N, 2))
    y0 = np.concatenate([Xp.ravel(), V.ravel()])
    E0, L0_ = inv(y0, m)
    A2, _ = companion_A(N, eps, 2)
    mA = maxre(A2)[0]
    for rtol in (1e-10, 1e-12):
        t1 = time.time()
        ts = np.linspace(0, Tend, 3001)
        sol = solve_ivp(rhs, (0, Tend), y0, method="DOP853", rtol=rtol, atol=rtol * 1e-3, t_eval=ts, args=(m,))
        D = np.array([shape(sol.y[:, k_], m) for k_ in range(sol.y.shape[1])])
        Ee = np.array([inv(sol.y[:, k_], m) for k_ in range(sol.y.shape[1])])
        dE = float(np.max(np.abs(Ee[:, 0] - E0)) / abs(E0))
        dL = float(np.max(np.abs(Ee[:, 1] - L0_)) / abs(L0_))
        sel = (D > 1e3 * D[0]) & (D < 1e-2)
        rate = float(np.polyfit(sol.t[sel], np.log(D[sel]), 1)[0]) if np.sum(sel) > 10 else None
        zeitl.append({"N": N, "eps": eps, "rtol": rtol, "T": Tend, "D0": float(D[0]), "Dmax": float(D.max()),
                      "D_ende": float(D[-1]), "wachstumsrate_fit": rate, "maxRe_linear": mA,
                      "rel_dE": dE, "rel_dL": dL, "sekunden": time.time() - t1, "status": sol.status})
        np.savez_compressed(os.path.join(OUT, f"v2_zeit_N{N}_rtol{rtol:g}.npz"), t=sol.t, D=D)
        print(zeitl[-1], flush=True)
res["zeitentwicklung"] = zeitl
res["sekunden_gesamt"] = time.time() - T0
with open(os.path.join(OUT, "v2_maxwell.json" if not SCHNELL else "v2_maxwell_schnell.json"), "w") as f:
    json.dump(res, f, indent=1)
print("fertig", res["sekunden_gesamt"])
