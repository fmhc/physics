#!/usr/bin/env python3
"""V3 Federring N+1 (Runde 16, ausprobieren).
N Massen auf dem Kreis + Zentrum, Nachbarfedern und Speichen mit Ruhelaengen, Rotation Omega.
R(Omega) aus der Kraeftebilanz; lineare Stabilitaet im mitrotierenden System (gyroskopisch).
Variante F0: L_s = 1, L_r = 2 sin(pi/N) (spannungsfrei bei Omega = 0); F1: L_s = L_r = 1.
Methode A: analytische Hesse-Matrix (2D, 3D); Methode B: finite Differenzen (2D).
Aufruf: python v3_federring.py <ausgabeordner> [schnell]
"""
import json, os, sys, time
import numpy as np

OUT = sys.argv[1] if len(sys.argv) > 1 else "aus"
SCHNELL = len(sys.argv) > 2 and sys.argv[2] == "schnell"
os.makedirs(OUT, exist_ok=True)
T0 = time.time()
TOL = 1e-6
KS = KR = 1.0


def geom(N, Om, var, dim):
    s = np.sin(np.pi / N)
    Ls = 1.0
    Lr = 2 * s if var == "F0" else 1.0
    K = KS + 4 * KR * s * s
    if Om ** 2 >= K:
        return None
    R = (KS * Ls + 2 * KR * Lr * s) / (K - Om ** 2)
    th = 2 * np.pi * np.arange(N) / N
    X = np.zeros((N + 1, dim))
    X[1:, 0] = R * np.cos(th)
    X[1:, 1] = R * np.sin(th)
    springs = [(0, j, KS, Ls) for j in range(1, N + 1)] + [(j, 1 + (j % N), KR, Lr) for j in range(1, N + 1)]
    return X, springs, R


def grad_U(X, springs):
    g = np.zeros_like(X)
    for (i, j, k, L0) in springs:
        d = X[i] - X[j]
        L = np.linalg.norm(d)
        f = k * (L - L0) * d / L
        g[i] += f
        g[j] -= f
    return g


def hess_U(X, springs):
    n, dim = X.shape
    H = np.zeros((n * dim, n * dim))
    I = np.eye(dim)
    for (i, j, k, L0) in springs:
        d = X[i] - X[j]
        L = np.linalg.norm(d)
        u = d / L
        B = k * np.outer(u, u) + (k * (L - L0) / L) * (I - np.outer(u, u))
        si, sj = slice(dim * i, dim * i + dim), slice(dim * j, dim * j + dim)
        H[si, si] += B
        H[sj, sj] += B
        H[si, sj] -= B
        H[sj, si] -= B
    return H


def hess_fd(X, springs, h=1e-5):
    n, dim = X.shape
    H = np.zeros((n * dim, n * dim))
    xf = X.ravel()
    for c in range(xf.size):
        e = np.zeros(xf.size)
        e[c] = h
        H[:, c] = (grad_U((xf + e).reshape(n, dim), springs).ravel()
                   - grad_U((xf - e).reshape(n, dim), springs).ravel()) / (2 * h)
    return 0.5 * (H + H.T)


def companion(H, n, dim, Om):
    P = np.eye(dim)
    Jm = np.zeros((dim, dim))
    Jm[0, 1], Jm[1, 0] = -1, 1
    if dim == 3:
        P[2, 2] = 0
    Keff = H - Om ** 2 * np.kron(np.eye(n), P)
    G = 2 * Om * np.kron(np.eye(n), Jm)
    A = np.zeros((2 * n * dim, 2 * n * dim))
    A[:n * dim, n * dim:] = np.eye(n * dim)
    A[n * dim:, :n * dim] = -Keff
    A[n * dim:, n * dim:] = -G
    return A, Keff


def spektrum(N, Om, var, dim=2, fd=False):
    g = geom(N, Om, var, dim)
    if g is None:
        return None
    X, springs, R = g
    H = hess_fd(X, springs) if fd else hess_U(X, springs)
    A, Keff = companion(H, N + 1, dim, Om)
    s = np.linalg.eigvals(A)
    gr = grad_U(X, springs)
    P = np.ones(dim)
    if dim == 3:
        P[2] = 0
    resid = float(np.max(np.abs(gr - Om ** 2 * X * P)))
    return s, R, resid, H


def kennzahlen(s, Om):
    mr = float(np.max(s.real))
    # weichste nicht-triviale Frequenz: ohne |s| < 1e-6 (Drehung) und ohne +-i Omega (Schwerpunkt)
    keep = (np.abs(s) > 1e-6) & (np.abs(s - 1j * Om) > 1e-6) & (np.abs(s + 1j * Om) > 1e-6)
    soft = float(np.min(np.abs(s[keep].imag))) if np.any(keep) else None
    return mr, soft


def ztest(Ns, X):
    Ns = np.array(Ns)
    X = np.array(X, float)
    out = {}
    for idx, N in enumerate(Ns):
        if N < 8 or N > 28:
            continue
        nb = [i for i in range(len(Ns)) if 1 <= abs(Ns[i] - N) <= 4 and np.isfinite(X[i])]
        if len(nb) < 8 or not np.isfinite(X[idx]):
            continue
        c = np.polyfit(Ns[nb], X[nb], 2)
        resn = X[nb] - np.polyval(c, Ns[nb])
        sig = np.std(resn, ddof=3)
        fit = np.polyval(c, N)
        rel = abs(X[idx] - fit) / max(abs(X[idx]), 1e-300)
        z = (X[idx] - fit) / sig if sig > 0 else np.inf
        out[int(N)] = {"z": float(z), "rel": float(rel), "auffaellig": bool(abs(z) > 3 and rel > 0.01)}
    return out


res = {"versuch": "V3", "tol": TOL}
Ns = list(range(4, 33)) if not SCHNELL else list(range(4, 13))
for var in ("F0", "F1"):
    tab = []
    for N in Ns:
        e = {"N": N}
        for Om in (0.3, 0.6, 0.9):
            sp = spektrum(N, Om, var, 2)
            s2, R, resid, H = sp
            mr2, soft = kennzahlen(s2, Om)
            s3 = spektrum(N, Om, var, 3)[0]
            mr3 = float(np.max(s3.real))
            sB, _, _, HB = spektrum(N, Om, var, 2, fd=True)
            mrB = float(np.max(sB.real))
            e[f"Om{Om}"] = {"R": R, "kraeftebilanz_resid": resid, "maxRe_2D": mr2, "maxRe_3D": mr3,
                            "maxRe_B_fd": mrB, "hesse_fd_relabw": float(np.max(np.abs(HB - H)) / np.max(np.abs(H))),
                            "stabil_2D": mr2 <= TOL, "stabil_3D": mr3 <= TOL, "stabil_B_tol1e-4": mrB <= 1e-4,
                            "omega_soft": soft, "n_eig_nahe_0": int(np.sum(np.abs(s2) < 1e-6)),
                            "n_eig_nahe_pm_iOm": int(np.sum(np.abs(np.abs(s2.imag) - Om) < 1e-6) - 0)}
        # Omega-Raster bis 0.999 sqrt(K) und Bisektion der ersten Instabilitaet
        K = KS + 4 * KR * np.sin(np.pi / N) ** 2
        oms = np.linspace(0, 0.999 * np.sqrt(K), 120)
        mrs = []
        for Om in oms:
            s_ = spektrum(N, Om, var, 2)[0]
            mrs.append(float(np.max(s_.real)))
        mrs = np.array(mrs)
        st = mrs <= TOL
        e["omega_raster_maxRe"] = mrs.tolist()
        e["omega_raster"] = oms.tolist()
        e["wechsel"] = int(np.sum(st[1:] != st[:-1]))
        if np.any(~st):
            iu = int(np.argmax(~st))
            if iu == 0:
                e["Omega_c"] = 0.0
            else:
                lo, hi = oms[iu - 1], oms[iu]
                for _ in range(40):
                    mid = 0.5 * (lo + hi)
                    if np.max(spektrum(N, mid, var, 2)[0].real) <= TOL:
                        lo = mid
                    else:
                        hi = mid
                e["Omega_c"] = float(lo)
                e["Omega_c_rel_sqrtK"] = float(lo / np.sqrt(K))
                s3c = spektrum(N, lo * 0.999, var, 3)[0]
                e["maxRe_3D_knapp_unter"] = float(np.max(s3c.real))
        else:
            e["Omega_c"] = None
        # nachtraeglich (nicht im Plan): Stabilisierungs-Omega, falls bei kleinem Omega instabil
        if (not st[0]) and st[-1]:
            iL = int(len(st) - 1 - np.argmax(~st[::-1]))  # letzter instabiler Rasterpunkt
            lo, hi = oms[iL], oms[iL + 1]
            for _ in range(40):
                mid = 0.5 * (lo + hi)
                if np.max(spektrum(N, mid, var, 2)[0].real) <= TOL:
                    hi = mid
                else:
                    lo = mid
            e["Omega_stab"] = float(hi)
        # 3D-Raster
        mr3s = np.array([float(np.max(spektrum(N, Om, var, 3)[0].real)) for Om in oms])
        e["omega_raster_maxRe_3D"] = mr3s.tolist()
        st3 = mr3s <= TOL
        e["wechsel_3D"] = int(np.sum(st3[1:] != st3[:-1]))
        e["Omega_c_3D_raster"] = float(oms[int(np.argmax(~st3))]) if np.any(~st3) else None
        e["sqrtK"] = float(np.sqrt(K))
        tab.append(e)
        print(var, N, {k: (v["maxRe_2D"], v["omega_soft"]) for k, v in e.items() if k.startswith("Om0")},
              "Omega_c", e.get("Omega_c"), "rel", e.get("Omega_c_rel_sqrtK"), "wechsel", e["wechsel"], "Omega_stab", e.get("Omega_stab"),
              "3D: wechsel", e["wechsel_3D"], "Om_c3D", e["Omega_c_3D_raster"], flush=True)
    res[var] = tab
    # Auffaelligkeit
    zt = {}
    zt["Omega_c"] = ztest(Ns, [t["Omega_c"] if t.get("Omega_c") is not None else np.nan for t in tab])
    zt["Omega_c_rel"] = ztest(Ns, [t.get("Omega_c_rel_sqrtK", np.nan) for t in tab])
    zt["Omega_stab (nachtraeglich)"] = ztest(Ns, [t.get("Omega_stab", np.nan) for t in tab])
    zt["omega_soft_Om0.6"] = ztest(Ns, [t["Om0.6"]["omega_soft"] for t in tab])
    for Om in (0.3, 0.6, 0.9):
        zt[f"S_Om{Om}"] = ztest(Ns, [t[f"Om{Om}"]["maxRe_2D"] for t in tab])
    res[var + "_ztest"] = zt
    for k, v in zt.items():
        auff = [N for N, d in v.items() if d["auffaellig"]]
        print(var, k, "z11", v.get(11, {}).get("z"), "z19", v.get(19, {}).get("z"), "auffaellig", auff, flush=True)
res["sekunden_gesamt"] = time.time() - T0
with open(os.path.join(OUT, "v3_federring.json" if not SCHNELL else "v3_federring_schnell.json"), "w") as f:
    json.dump(res, f, indent=1)
print("fertig", res["sekunden_gesamt"])
