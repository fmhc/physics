#!/usr/bin/env python3
"""V5 Diskretes sextisches Feld auf dem Rad-Graphen (Ring N + Zentrum), Runde 16, ausprobieren.
psi_i'' + sum_j J (psi_i - psi_j) + V'(|psi_i|^2) psi_i = 0, V'(s) = 1 - 2 s + 1.5 s^2.
Stationaer psi = phi e^{i omega t} (reell), Newton; Stabilitaet im mitrotierenden Phasenbild
(gyroskopisch), Q = 2 omega sum phi^2, dQ/domega zweifach; Zeitentwicklung als Kontrolle.
Aufruf: python v5_feld.py <ausgabeordner> [schnell]
"""
import json, os, sys, time
import numpy as np
from scipy.integrate import solve_ivp

OUT = sys.argv[1] if len(sys.argv) > 1 else "aus"
SCHNELL = len(sys.argv) > 2 and sys.argv[2] == "schnell"
os.makedirs(OUT, exist_ok=True)
T0 = time.time()
TOL = 1e-6


def Vp(s):
    return 1 - 2 * s + 1.5 * s * s


def Vpp(s):
    return -2 + 3 * s


def V(s):
    return s - s * s + 0.5 * s ** 3


def laplace(N, J):
    n = N + 1
    A = np.zeros((n, n))
    for i in range(N):
        A[i, (i + 1) % N] = A[(i + 1) % N, i] = 1
        A[i, N] = A[N, i] = 1
    return J * (np.diag(A.sum(1)) - A), A


def newton(L, w2, phi, tol=1e-12, itmax=60):
    for it in range(itmax):
        s = phi * phi
        F = L @ phi + (Vp(s) - w2) * phi
        if np.max(np.abs(F)) < tol:
            return phi, True, it
        JF = L + np.diag(Vp(s) + 2 * s * Vpp(s) - w2)
        try:
            phi = phi - np.linalg.solve(JF, F)
        except np.linalg.LinAlgError:
            return phi, False, it
        if not np.all(np.isfinite(phi)) or np.max(np.abs(phi)) > 10:
            return phi, False, it
    s = phi * phi
    F = L @ phi + (Vp(s) - w2) * phi
    return phi, bool(np.max(np.abs(F)) < tol), itmax


def stab(L, w2, phi):
    n = phi.size
    w = np.sqrt(w2)
    s = phi * phi
    Ku = L + np.diag(Vp(s) + 2 * s * Vpp(s) - w2)
    Kv = L + np.diag(Vp(s) - w2)
    K = np.block([[Ku, np.zeros((n, n))], [np.zeros((n, n)), Kv]])
    G = np.block([[np.zeros((n, n)), -2 * w * np.eye(n)], [2 * w * np.eye(n), np.zeros((n, n))]])
    A = np.zeros((4 * n, 4 * n))
    A[:2 * n, 2 * n:] = np.eye(2 * n)
    A[2 * n:, :2 * n] = -K
    A[2 * n:, 2 * n:] = -G
    ev = np.linalg.eigvals(A)
    mr = float(np.max(ev.real))
    # reelles Paar (VK-artig) gegen komplexes Quartett (oszillatorisch)
    big = ev[ev.real > TOL]
    art = "stabil" if mr <= TOL else ("reell" if np.all(np.abs(big.imag) < 1e-8) else "oszillatorisch")
    dphi = 2 * w * np.linalg.solve(Ku, phi)
    dQ = 2 * np.sum(s) + 4 * w * phi @ dphi
    return mr, art, float(dQ), float(np.sort(np.abs(ev))[1])


def energie(L, Adj, phi, w2):
    s = phi * phi
    kin = w2 * np.sum(s)
    kop = 0.5 * phi @ L @ phi * 2 / 2  # sum_<ij> J (phi_i - phi_j)^2 = phi^T L phi
    return float(kin + phi @ L @ phi + np.sum(V(s)))


def s_branch(w2, big=False):
    disc = 4 - 6 * (1 - w2)
    if disc < 0:
        return None
    return (2 + np.sqrt(disc)) / 3 if big else (2 - np.sqrt(disc)) / 3


def loese(N, J, w2, site, branch, schritte=12):
    """MacKay-Aubry-Fortsetzung: von J = 0 (exakte Anti-Kontinuum-Loesung) in Schritten zu J."""
    sb = s_branch(w2, big=(branch == "gross"))
    if sb is None:
        return None, False
    phi = np.zeros(N + 1)
    phi[site] = np.sqrt(sb)
    for Jk in np.linspace(0, J, schritte + 1)[1:]:
        L, _ = laplace(N, Jk)
        phi_neu, ok, _ = newton(L, w2, phi)
        if not ok or np.max(np.abs(phi_neu)) < 1e-3 or np.max(np.abs(phi_neu - phi)) > 0.3:
            return phi_neu, False
        phi = phi_neu
    return phi, True


def scan(N, J, mode, branch, w2grid):
    L, Adj = laplace(N, J)
    n = N + 1
    site = N if mode == "zentrum" else 0
    rows = []
    prev = None
    for w2 in w2grid:
        phi, ok = loese(N, J, w2, site, branch)
        if not ok:
            rows.append(None)
            prev = None
            continue
        alt = None
        if prev is not None:
            phi2, ok2, _ = newton(L, w2, prev)
            if ok2:
                alt = float(np.max(np.abs(np.abs(phi2) - np.abs(phi))))
        s = phi * phi
        PR = float(np.sum(s) ** 2 / np.sum(s * s))
        lok = bool(np.argmax(np.abs(phi)) == site and PR < 3.0 and np.abs(phi[site]) > 1e-3)
        if not lok:
            rows.append(None)
            prev = None
            continue
        mr, art, dQ, kl = stab(L, w2, phi)
        Ku = L + np.diag(Vp(s) + 2 * s * Vpp(s) - w2)
        nneg = int(np.sum(np.linalg.eigvalsh(Ku) < -1e-12))
        vk_stabil = (nneg == 0) or (nneg == 1 and dQ < 0)
        Q = 2 * np.sqrt(w2) * float(np.sum(s))
        rows.append({"w2": float(w2), "Q": Q, "dQdw": dQ, "PR": PR, "amp": float(np.abs(phi[site])),
                     "maxRe": mr, "art": art, "n_neg_Ku": nneg, "vk_vorhersage_stabil": bool(vk_stabil),
                     "fortsetzung_abw": alt, "E": energie(L, Adj, phi, w2), "phi": phi.tolist()})
        prev = phi
    # dQ/domega per finiter Differenz entlang des Rasters
    for k in range(1, len(rows) - 1):
        if rows[k] and rows[k - 1] and rows[k + 1]:
            w_m, w_p = np.sqrt(rows[k - 1]["w2"]), np.sqrt(rows[k + 1]["w2"])
            rows[k]["dQdw_fd"] = (rows[k + 1]["Q"] - rows[k - 1]["Q"]) / (w_p - w_m)
    return rows


def zusammenfassung(rows):
    ok = [r for r in rows if r]
    if not ok:
        return {"existiert": False}
    w2s = np.array([r["w2"] for r in ok])
    st = np.array([r["maxRe"] <= TOL for r in ok])
    vk_neg = np.array([r["dQdw"] < 0 for r in ok])
    arten = {a: int(sum(1 for r in ok if r["art"] == a)) for a in ("stabil", "reell", "oszillatorisch")}
    # VK-Konsistenz: dQ/dw > 0 soll ein reelles Paar geben
    vk_inkons = int(sum(1 for r in ok if r["vk_vorhersage_stabil"] != (r["maxRe"] <= TOL)))
    vk_inkons_reell = int(sum(1 for r in ok if (not r["vk_vorhersage_stabil"]) and r["art"] != "reell"))
    fdabw = [abs(r["dQdw_fd"] - r["dQdw"]) / max(abs(r["dQdw"]), 1e-12) for r in ok if "dQdw_fd" in r]
    return {"existiert": True, "w2_min": float(w2s.min()), "w2_max": float(w2s.max()), "n_punkte": int(len(ok)),
            "stabil_anteil": float(st.mean()), "w2_stabil_min": float(w2s[st].min()) if st.any() else None,
            "w2_stabil_max": float(w2s[st].max()) if st.any() else None, "arten": arten,
            "vk_negativ_anteil": float(vk_neg.mean()), "vk_inkonsistent": vk_inkons,
            "vk_instabil_aber_nicht_reell": vk_inkons_reell,
            "n_neg_Ku_werte": sorted(set(int(r["n_neg_Ku"]) for r in ok)),
            "dQdw_fd_relabw_median": float(np.median(fdabw)) if fdabw else None,
            "fortsetzung_max_abw": float(max([r["fortsetzung_abw"] for r in ok if r["fortsetzung_abw"] is not None],
                                              default=0.0))}


res = {"versuch": "V5", "tol": TOL}
w2grid = np.round(np.arange(0.300, 0.9951, 0.005), 6)
Ns = list(range(8, 22)) if not SCHNELL else [10, 11, 12]
Js = [0.05, 0.1, 0.2] if not SCHNELL else [0.1]
tab = []
details = {}
for J in Js:
    for N in Ns:
        for mode in ("ring", "zentrum"):
            for br in ("klein", "gross"):
                rows = scan(N, J, mode, br, w2grid)
                zs = zusammenfassung(rows)
                zs.update({"N": N, "J": J, "mode": mode, "zweig": br})
                tab.append(zs)
                if N in (11, 12, 19) or SCHNELL:
                    details[f"N{N}_J{J}_{mode}_{br}"] = [
                        {k: v for k, v in r.items() if k != "phi"} if r else None for r in rows]
                print({k: zs.get(k) for k in ("N", "J", "mode", "zweig", "w2_min", "w2_max", "stabil_anteil",
                                              "w2_stabil_min", "w2_stabil_max", "arten", "vk_inkonsistent",
                                              "dQdw_fd_relabw_median")}, flush=True)
res["tabelle"] = tab
res["details"] = details

# Anti-Kontinuum-Kontrolle J = 1e-4
ak = {}
for mode in ("ring", "zentrum"):
    for br in ("klein", "gross"):
        zs = zusammenfassung(scan(11, 1e-4, mode, br, np.round(np.arange(0.300, 0.9991, 0.001), 6)))
        ak[f"{mode}_{br}"] = {k: zs.get(k) for k in ("w2_min", "w2_max", "stabil_anteil", "w2_stabil_min",
                                                     "w2_stabil_max", "arten", "vk_inkonsistent")}
res["anti_kontinuum_J1e-4_N11"] = ak
print("Anti-Kontinuum", ak, flush=True)


# Auffaelligkeit (wie V3), Kennzahlen: w2_min, w2_max, stabil_anteil der Ringmode (kleiner Zweig)
def ztest(Ns_, X):
    Ns_ = np.array(Ns_)
    X = np.array(X, float)
    out = {}
    for idx, N in enumerate(Ns_):
        nb = [i for i in range(len(Ns_)) if 1 <= abs(Ns_[i] - N) <= 4 and np.isfinite(X[i])]
        if len(nb) < 8 or not np.isfinite(X[idx]):
            continue
        c = np.polyfit(Ns_[nb], X[nb], 2)
        resn = X[nb] - np.polyval(c, Ns_[nb])
        sig = np.std(resn, ddof=3)
        fit = np.polyval(c, N)
        rel = abs(X[idx] - fit) / max(abs(X[idx]), 1e-300)
        z = (X[idx] - fit) / sig if sig > 0 else np.inf
        out[int(N)] = {"z": float(z), "rel": float(rel), "auffaellig": bool(abs(z) > 3 and rel > 0.01)}
    return out


zt = {}
if not SCHNELL:
    for J in Js:
        for mode in ("ring", "zentrum"):
            for br in ("klein", "gross"):
                sel = [t for t in tab if t["J"] == J and t["mode"] == mode and t["zweig"] == br]
                for key in ("w2_min", "w2_max", "stabil_anteil"):
                    X = [t.get(key, np.nan) if t.get(key) is not None else np.nan for t in sel]
                    zt[f"J{J}_{mode}_{br}_{key}"] = ztest([t["N"] for t in sel], X)
    res["ztest"] = zt
    for k, v in zt.items():
        auff = [N for N, d in v.items() if d["auffaellig"]]
        print(k, "z11", v.get(11, {}).get("z"), "z19", v.get(19, {}).get("z"), "auffaellig", auff, flush=True)

# Zeitentwicklung: N = 11, 12, J = 0.1, Ringmode, w2 = 0.8 (kleiner Zweig) und 0.6 (grosser Zweig)
def rhs(t, y, L):
    n = L.shape[0]
    p = y[:n] + 1j * y[n:2 * n]
    acc = -(L @ p) - Vp(np.abs(p) ** 2) * p
    return np.concatenate([y[2 * n:], acc.real, acc.imag])


def inv(y, L):
    n = L.shape[0]
    p = y[:n] + 1j * y[n:2 * n]
    pd = y[2 * n:3 * n] + 1j * y[3 * n:]
    E = float(np.sum(np.abs(pd) ** 2) + np.real(np.conj(p) @ L @ p) + np.sum(V(np.abs(p) ** 2)))
    Q = float(np.sum(np.imag(np.conj(p) * pd)) * 2)  # = -i sum(conj(p) pd - p conj(pd)), Vorzeichen positiv
    return E, Q


zeit = []
Tend = 100.0 if SCHNELL else 500.0
for N in (11, 12):
    L, Adj = laplace(N, 0.1)
    for (w2, br) in ((0.9, "klein"), (0.7, "klein"), (0.6, "gross")):
        phi, ok = loese(N, 0.1, w2, 0, br)
        s_ = phi * phi
        PR = float(np.sum(s_) ** 2 / np.sum(s_ * s_)) if ok else None
        if not ok or PR >= 3.0 or np.argmax(np.abs(phi)) != 0:
            zeit.append({"N": N, "w2": w2, "zweig": br, "konvergiert_lokalisiert": False})
            continue
        mr, art, dQ, _ = stab(L, w2, phi)
        w = np.sqrt(w2)
        rng = np.random.default_rng(7)
        p0 = phi * (1 + 1e-6 * rng.standard_normal(phi.size)) + 1e-6j * rng.standard_normal(phi.size) * phi
        y0 = np.concatenate([p0.real, p0.imag, (1j * w * p0).real, (1j * w * p0).imag])
        E0, Q0 = inv(y0, L)
        for rtol in (1e-10, 1e-12):
            t1 = time.time()
            ts = np.linspace(0, Tend, 2001)
            sol = solve_ivp(rhs, (0, Tend), y0, method="DOP853", rtol=rtol, atol=rtol * 1e-2, t_eval=ts, args=(L,))
            n = N + 1
            amps = np.sqrt(sol.y[:n] ** 2 + sol.y[n:2 * n] ** 2)
            dev = np.max(np.abs(amps - np.abs(phi)[:, None]), axis=0)
            EQ = np.array([inv(sol.y[:, k], L) for k in range(sol.y.shape[1])])
            zeit.append({"N": N, "w2": w2, "zweig": br, "rtol": rtol, "maxRe_linear": mr, "art": art, "dQdw": dQ,
                         "rel_dE": float(np.max(np.abs(EQ[:, 0] - E0)) / abs(E0)),
                         "rel_dQ": float(np.max(np.abs(EQ[:, 1] - Q0)) / abs(Q0)),
                         "Q_formel": float(2 * w * np.sum(phi ** 2)), "Q_zeit0": Q0,
                         "abw_amplitude_max": float(dev.max()), "abw_amplitude_ende": float(dev[-1]),
                         "abw_t100": float(dev[np.searchsorted(ts, min(100.0, Tend)) - 1]),
                         "sekunden": time.time() - t1})
            print(zeit[-1], flush=True)
res["zeitentwicklung"] = zeit
res["sekunden_gesamt"] = time.time() - T0
with open(os.path.join(OUT, "v5_feld.json" if not SCHNELL else "v5_feld_schnell.json"), "w") as f:
    json.dump(res, f, indent=1)
print("fertig", res["sekunden_gesamt"])
