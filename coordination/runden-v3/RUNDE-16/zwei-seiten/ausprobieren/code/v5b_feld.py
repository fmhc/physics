#!/usr/bin/env python3
"""V5 Diskretes sextisches Feld auf dem Rad-Graphen (Ring N + Zentrum), Runde 16, ausprobieren.
psi_i'' + sum_j J (psi_i - psi_j) + V'(|psi_i|^2) psi_i = 0, V'(s) = 1 - 2 s + 1.5 s^2.
Stationaer psi = phi e^{i omega t} (reell), Newton; Stabilitaet im mitrotierenden Phasenbild
(gyroskopisch), Q = 2 omega sum phi^2, dQ/domega zweifach; Zeitentwicklung als Kontrolle.
Fassung v5b (Nachtrag, nicht im eingefrorenen Plan): stetige Kennzahlen bei festem omega^2 fuer N = 4..26,
damit 11 und 19 volle Nachbarschaften haben; Existenzgrenze der Zentrumsmode N_max(J).
Aufruf: python v5b_feld.py <ausgabeordner> [schnell]
"""
import json, os, sys, time
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
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



res = {"versuch": "V5b", "tol": TOL}
Ns = list(range(4, 27)) if not SCHNELL else [10, 11, 12]
ziel = {0.05: 0.8, 0.1: 0.8, 0.2: 0.74}
fest = []
for J, w2 in ziel.items():
    for N in Ns:
        L, Adj = laplace(N, J)
        phi, ok = loese(N, J, w2, 0, "klein")
        e = {"J": J, "w2": w2, "N": N, "ok": bool(ok)}
        if ok:
            s = phi * phi
            PR = float(np.sum(s) ** 2 / np.sum(s * s))
            if np.argmax(np.abs(phi)) == 0 and PR < 3:
                mr, art, dQ, _ = stab(L, w2, phi)
                n = N + 1
                w = np.sqrt(w2)
                Ku = L + np.diag(Vp(s) + 2 * s * Vpp(s) - w2)
                Kv = L + np.diag(Vp(s) - w2)
                K = np.block([[Ku, np.zeros((n, n))], [np.zeros((n, n)), Kv]])
                G = np.block([[np.zeros((n, n)), -2 * w * np.eye(n)], [2 * w * np.eye(n), np.zeros((n, n))]])
                A = np.zeros((4 * n, 4 * n))
                A[:2 * n, 2 * n:] = np.eye(2 * n)
                A[2 * n:, :2 * n] = -K
                A[2 * n:, 2 * n:] = -G
                ev = np.linalg.eigvals(A)
                keep = np.abs(ev) > 1e-6
                e.update({"Q": 2 * w * float(np.sum(s)), "PR": PR, "amp": float(abs(phi[0])), "maxRe": mr,
                          "art": art, "dQdw": dQ, "omega_int_min": float(np.min(np.abs(ev[keep].imag))),
                          "zentrum_amp": float(abs(phi[N]))})
            else:
                e["ok"] = False
        fest.append(e)
        print({k: e.get(k) for k in ("J", "N", "ok", "Q", "PR", "maxRe", "omega_int_min", "zentrum_amp")}, flush=True)
res["fest"] = fest


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
        z = (X[idx] - fit) / sig if sig > 0 else float("inf")
        out[int(N)] = {"z": float(z), "rel": float(rel), "auffaellig": bool(abs(z) > 3 and rel > 0.01)}
    return out


zt = {}
for J in ziel:
    sel = [e for e in fest if e["J"] == J]
    for key in ("Q", "PR", "omega_int_min", "zentrum_amp"):
        X = [e.get(key, np.nan) if e.get("ok") else np.nan for e in sel]
        zt[f"J{J}_{key}"] = ztest([e["N"] for e in sel], X)
res["ztest"] = zt
for k, v in zt.items():
    print(k, "z11", v.get(11, {}).get("z"), "rel11", v.get(11, {}).get("rel"), "z19", v.get(19, {}).get("z"),
          "rel19", v.get(19, {}).get("rel"), "auffaellig", [N for N, d in v.items() if d["auffaellig"]], flush=True)

# Existenzgrenze der Zentrumsmode
grenze = []
w2g = np.round(np.arange(0.300, 0.9951, 0.005), 6)
for J in ((0.03, 0.04, 0.05, 0.06, 0.08) if not SCHNELL else (0.05,)):
    nmax = None
    for N in range(4, 41):
        da = False
        for w2 in w2g:
            phi, ok = loese(N, J, w2, N, "klein")
            if ok:
                s = phi * phi
                PR = float(np.sum(s) ** 2 / np.sum(s * s))
                if np.argmax(np.abs(phi)) == N and PR < 3 and abs(phi[N]) > 1e-3:
                    da = True
                    break
        if da:
            nmax = N
        else:
            break
    grenze.append({"J": J, "N_max_zentrumsmode": nmax, "J_mal_Nmax": None if nmax is None else J * nmax})
    print(grenze[-1], flush=True)
res["zentrumsmode_grenze"] = grenze
res["sekunden_gesamt"] = time.time() - T0
with open(os.path.join(OUT, "v5b_feld.json" if not SCHNELL else "v5b_feld_schnell.json"), "w") as f:
    json.dump(res, f, indent=1)
print("fertig", res["sekunden_gesamt"])
