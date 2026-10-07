#!/usr/bin/env python3
"""SCHWEBUNGSUHR (Runde 23). Code-Agent im Auftrag der Leitung claude-primary, 02.10.2026.
Karte: RUNDE-23/schwebungsuhr/KARTE.md. Plan: PLAN.md (vor dem ersten echten Lauf eingefroren).

Modell M1 in 1D: psi_tt = psi_xx - U'(|psi|^2) psi, U(S) = S - S^2 + S^3/2, U'(S) = 1 - 2 S + 1,5 S^2.
Vorbild: RUNDE-22/bildung-leiter/code/zeit2d_v2.py (Leapfrog dt = 0,4 dx, Daempfungsschicht SIGMA0 = 1 quadratisch,
Dirichlet am Rand, exakter Startschritt f exp(+i w_d dt), w_d = (2/dt) asin(w dt/2)). matrix_pencil aus
RUNDE-12/leiter2d-praez/bic2_2d_praez_v2.py, hier nach numpy uebertragen (gleiche Rechenvorschrift).

Profil: geschlossene 1D-Loesung S(x) = 2 k^2 / (1 + s cosh(2 k x)), k^2 = 1 - w^2, s = sqrt(2 w^2 - 1), als
Startwert; danach Newton auf der diskreten Gleichung desselben Gitters (Halbachse, Spiegelung bei j = 0, f_M = 0),
damit der Einzelball im Zeitlauf exakt stationaer ist.

Aufrufe:
  python schwebung1d.py profil <dx> <aus.json>
  python schwebung1d.py einzel <w2> <dx> <T> <L> <aus.json>
  python schwebung1d.py paar <w2a> <w2b> <D> <theta_durch_pi> <dx> <T> <L> <aus.json>
  python schwebung1d.py auswerten <aus.json.roh.npz> <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.linalg import solve_banded  # noqa: E402

SIGMA0 = 1.0          # Daempfungsstaerke der Randschicht (wie zeit2d_v2)
BREITE_ABS = 60.0     # Breite der Daempfungsschicht an jedem Rand
MESS = 0.2            # Messabstand in Zeiteinheiten
D_KANDIDATEN = [round(5.6 + 0.2 * i, 1) for i in range(10)]   # Vielfache von 0,2: Zentren auf Knoten beider Gitter
FENSTER_GLEIT = 50.0  # gleitender Phasenfit
D_MERGE = 1.5         # Maximaabstand unter 1,5: verschmolzen
SCHWELLE_RE = 0.005   # Pencil: Komponenten mit |Re| < 0,005 gelten als Gleichanteil/Drift
T_START = time.time()


def u(S):
    return S - S * S + 0.5 * S ** 3


def u1(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def u2(S):
    return -2.0 + 3.0 * S


def kontinuum(w2, x):
    k2 = 1.0 - w2
    k = math.sqrt(k2)
    s = math.sqrt(2.0 * w2 - 1.0)
    z = np.minimum(2.0 * k * np.abs(x), 700.0)
    return np.sqrt(2.0 * k2 / (1.0 + s * np.cosh(z)))


def ladung_kontinuum(w2):
    om = math.sqrt(w2)
    s = math.sqrt(2.0 * w2 - 1.0)
    return 4.0 * math.sqrt(2.0) * om * math.atanh(math.sqrt((1.0 - s) / (1.0 + s)))


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, (np.floating, np.integer)):
        x = x.item()
    if isinstance(x, complex):
        return [x.real, x.imag]
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return x


def schreiben(out, pfad):
    with open(pfad + ".tmp", "w") as fh:
        json.dump(jsonfest(out), fh, indent=1)
    os.replace(pfad + ".tmp", pfad)


# ================================================================ Profil

def residuum(f, w2, dx):
    M = f.size - 1
    h2 = 1.0 / (dx * dx)
    lap = np.zeros(M + 1)
    lap[1:M] = (f[2:] - 2.0 * f[1:M] + f[:M - 1]) * h2
    lap[0] = 2.0 * (f[1] - f[0]) * h2
    return (lap + (w2 - u1(f * f)) * f)[:M]


def profil_diskret(w2, dx, M, iters=30, tol=1e-12):
    """Newton auf F_j = (f_{j+1} - 2 f_j + f_{j-1})/dx^2 + (w2 - U'(f_j^2)) f_j = 0, j = 0..M-1, f_{-1} = f_1, f_M = 0."""
    f = kontinuum(w2, np.arange(M + 1) * dx)
    f[M] = 0.0
    h2 = 1.0 / (dx * dx)
    verlauf = []
    for _ in range(iters):
        F = residuum(f, w2, dx)
        res = float(np.abs(F).max())
        verlauf.append(res)
        if res < tol:
            break
        Sm = f[:M] * f[:M]
        ab = np.zeros((3, M))
        ab[0, 1:] = h2
        ab[0, 1] = 2.0 * h2                     # dF_0/df_1 (Spiegelung)
        ab[1, :] = -2.0 * h2 + w2 - u1(Sm) - 2.0 * Sm * u2(Sm)
        ab[2, :-1] = h2                         # dF_{j+1}/df_j
        f[:M] += solve_banded((1, 1), ab, -F)
    verlauf.append(float(np.abs(residuum(f, w2, dx)).max()))
    return f, verlauf


def platzieren(f, c, N):
    d = np.abs(np.arange(N + 1) - c)
    g = np.where(d < f.size, f[np.minimum(d, f.size - 1)], 0.0)
    g[0] = 0.0
    g[N] = 0.0
    return g


# ================================================================ Matrix-Pencil (numpy-Uebertragung)

def matrix_pencil(y, dt, K=12, max_n=2400):
    """Summe gedaempfter Exponentiale y_n = sum c_k z_k^n, z = exp(-i rho dt) -> rho = i ln z / dt
    (Re rho = Frequenz, Im rho < 0 = abklingend). Unterabtastung auf hoechstens max_n Punkte."""
    y = np.asarray(y, dtype=np.complex128)
    schritt = max(1, int(math.ceil(y.size / max_n)))
    y = y[::schritt]
    dt = dt * schritt
    N = y.size
    L = N // 3
    if N < 12:
        return []
    idx = np.arange(N - L)[:, None] + np.arange(L + 1)[None, :]
    Y = y[idx]
    _, S, Vh = np.linalg.svd(Y, full_matrices=False)
    K = max(1, min(K, int((S > S[0] * 1e-11).sum())))
    W = Vh[:K, :].T
    T = np.linalg.pinv(W[:-1, :]) @ W[1:, :]
    z = np.linalg.eigvals(T)
    n = np.arange(N, dtype=np.float64)
    V = z[None, :] ** n[:, None]
    c = np.linalg.pinv(V) @ y
    rho = 1j * np.log(z) / dt
    aus = [{"re": float(rho[k].real), "im": float(rho[k].imag), "amp": float(abs(c[k]))} for k in range(z.size)]
    aus.sort(key=lambda e: -e["amp"])
    rest = float(np.abs(y - V @ c).max() / max(float(np.abs(y).max()), 1e-300))
    for e in aus:
        e["rel_rest"] = rest
    return aus


# ================================================================ Gitter, Zeitschritt

def gitter(dx, L):
    N = int(round(2.0 * L / dx))
    if N % 2:
        N += 1
    j0 = N // 2
    x = (np.arange(N + 1) - j0) * dx
    Lw = j0 * dx
    x_sd = Lw - BREITE_ABS
    gam = np.where(np.abs(x) > x_sd, SIGMA0 * ((np.abs(x) - x_sd) / (Lw - x_sd)) ** 2, 0.0)
    jL = int(np.argmax(x >= -x_sd))                 # erster Knoten innen
    jR = int(N - np.argmax(x[::-1] <= x_sd))        # letzter Knoten innen
    return N, j0, x, Lw, x_sd, gam, jL, jR


def energie(psi, vel, dx):
    S = psi.real ** 2 + psi.imag ** 2
    grad = np.abs(np.diff(psi)) ** 2 / (dx * dx)
    return float(dx * ((np.abs(vel) ** 2 + u(S)).sum() + grad.sum()))


def zeitlauf(modus, w2a, w2b, D, theta, dx, T, L):
    t_wand = time.time()
    dt = 0.4 * dx
    N, j0, x, Lw, x_sd, gam, jL, jR = gitter(dx, L)
    oma = math.sqrt(w2a)
    oma_d = 2.0 / dt * math.asin(0.5 * oma * dt)
    fa, res_a = profil_diskret(w2a, dx, N)
    meta = {"modus": modus, "w2a": w2a, "w2b": w2b, "D": D, "theta_durch_pi": theta, "dx": dx, "dt": dt, "T": T,
            "L": Lw, "x_sd": x_sd, "N": N, "mess": MESS, "omega_a": oma, "omega_a_diskret": oma_d,
            "newton_a": res_a, "f0_a": float(fa[0]), "S0_a": float(fa[0] ** 2),
            "Q_a_kontinuum": ladung_kontinuum(w2a), "version": "schwebung1d"}
    if modus == "einzel":
        ca = j0
        psi_a = platzieren(fa, ca, N).astype(np.complex128)
        psi_b = np.zeros(N + 1, dtype=np.complex128)
        omb, omb_d, cb = 0.0, 0.0, None
    else:
        h = D / (2.0 * dx)
        if abs(h - round(h)) > 1e-9:
            raise SystemExit("D/(2 dx) muss ganzzahlig sein")
        ca, cb = j0 - int(round(h)), j0 + int(round(h))
        omb = math.sqrt(w2b)
        omb_d = 2.0 / dt * math.asin(0.5 * omb * dt)
        fb, res_b = profil_diskret(w2b, dx, N)
        meta.update({"omega_b": omb, "omega_b_diskret": omb_d, "newton_b": res_b, "f0_b": float(fb[0]),
                     "S0_b": float(fb[0] ** 2), "Q_b_kontinuum": ladung_kontinuum(w2b),
                     "x_a": float(x[ca]), "x_b": float(x[cb]),
                     "dichte_b_bei_a": float(fb[cb - ca] ** 2), "dichte_a_bei_b": float(fa[cb - ca] ** 2),
                     "delta_omega_nominal": abs(omb - oma), "delta_omega_diskret": abs(omb_d - oma_d)})
        psi_a = platzieren(fa, ca, N).astype(np.complex128)
        psi_b = platzieren(fb, cb, N) * complex(math.cos(math.pi * theta), math.sin(math.pi * theta))
    psi = psi_a + psi_b
    old = psi_a * complex(math.cos(oma_d * dt), math.sin(oma_d * dt))
    if modus != "einzel":
        old = old + psi_b * complex(math.cos(omb_d * dt), math.sin(omb_d * dt))
    old[0] = 0.0
    old[N] = 0.0
    # Startstoerung und Startgroessen (kontinuierliche Zeitableitung -i w psi je Ball)
    vel_a, vel_b = -1j * oma * psi_a, -1j * omb * psi_b
    Sa, Sb, S = np.abs(psi_a) ** 2, np.abs(psi_b) ** 2, np.abs(psi) ** 2
    kreuz = -u1(S) * psi + u1(Sa) * psi_a + u1(Sb) * psi_b
    meta["start"] = {
        "Q_a_diskret": float(2.0 * oma * dx * Sa.sum()), "Q_b_diskret": float(2.0 * omb * dx * Sb.sum()),
        "Q_gesamt": float(-2.0 * dx * (np.conj(psi) * (vel_a + vel_b)).imag.sum()),
        "E_a": energie(psi_a, vel_a, dx), "E_b": energie(psi_b, vel_b, dx) if modus != "einzel" else 0.0,
        "E_gesamt": energie(psi, vel_a + vel_b, dx),
        "kreuzbeschleunigung_max": float(np.abs(kreuz).max()),
        "kreuzbeschleunigung_l2": float(math.sqrt(dx * (np.abs(kreuz) ** 2).sum())),
        "beschleunigung_ball_a_max": float(np.abs(w2a * psi_a).max()),
    }
    meta["start"]["E_wechselwirkung"] = meta["start"]["E_gesamt"] - meta["start"]["E_a"] - meta["start"]["E_b"]
    dmp = 0.5 * dt * gam
    fakp = 1.0 / (1.0 + dmp)
    jl1, jr0 = jL, jR + 1
    dmpL, fpL, dmpR, fpR = dmp[:jl1], fakp[:jl1], dmp[jr0:], fakp[jr0:]
    n_mess = int(round(MESS / dt))
    n_schritte = int(round(T / dt))
    dt2 = dt * dt
    h2 = 1.0 / (dx * dx)
    x0 = float(x[0])
    sub = max(1, int(round(0.5 / dx)))
    n_bild = int(round(100.0 / dt))
    reihen = {k: [] for k in ("t", "S_mitte", "S_null", "p1", "p2", "ph1", "ph2", "Q1", "Q2", "Q1_null", "Q2_null",
                              "X1", "X2", "S_p1", "S_p2", "Q_innen", "S_zentrum", "ph_zentrum")}
    bilder, bild_t = [], []
    xin = x[jL:jR + 1]

    def interp(arr, p):
        uu = (p - x0) / dx
        k = int(math.floor(uu))
        w = uu - k
        return (1.0 - w) * arr[k] + w * arr[k + 1]

    def parab(Sv, k):
        a, b, c = Sv[k - 1], Sv[k], Sv[k + 1]
        den = a - 2.0 * b + c
        off = 0.5 * (a - c) / den if den < 0.0 else 0.0
        return x0 + (k + max(-0.5, min(0.5, off))) * dx

    def messen(t, old, psi, new, Sv):
        r = reihen
        r["t"].append(t)
        v = (new[jL:jR + 1] - old[jL:jR + 1]) * (0.5 / dt)
        pin = psi[jL:jR + 1]
        rho = -2.0 * (pin.real * v.imag - pin.imag * v.real)
        r["Q_innen"].append(float(dx * rho.sum()))
        if modus == "einzel":
            r["S_zentrum"].append(float(Sv[j0]))
            r["ph_zentrum"].append(math.atan2(psi[j0].imag, psi[j0].real))
            return
        kl = jL + int(np.argmax(Sv[jL:j0]))
        kr = j0 + 1 + int(np.argmax(Sv[j0 + 1:jR + 1]))
        p1, p2 = parab(Sv, kl), parab(Sv, kr)
        m = 0.5 * (p1 + p2)
        z1, z2, zm = interp(psi, p1), interp(psi, p2), interp(psi, m)
        r["p1"].append(p1)
        r["p2"].append(p2)
        r["S_p1"].append(float(Sv[kl]))
        r["S_p2"].append(float(Sv[kr]))
        r["ph1"].append(math.atan2(z1.imag, z1.real))
        r["ph2"].append(math.atan2(z2.imag, z2.real))
        r["S_mitte"].append(float(zm.real ** 2 + zm.imag ** 2))
        r["S_null"].append(float(Sv[j0]))
        km = int(math.ceil((m - x0) / dx - 1e-12)) - jL          # erster Innenknoten mit x >= m
        km = max(1, min(rho.size - 1, km))
        q1 = float(dx * rho[:km].sum())
        q2 = float(dx * rho[km:].sum())
        r["Q1"].append(q1)
        r["Q2"].append(q2)
        r["X1"].append(float(dx * (xin[:km] * rho[:km]).sum()) / q1 if q1 != 0.0 else float("nan"))
        r["X2"].append(float(dx * (xin[km:] * rho[km:]).sum()) / q2 if q2 != 0.0 else float("nan"))
        k0 = j0 - jL
        r["Q1_null"].append(float(dx * (rho[:k0].sum() + 0.5 * rho[k0])))
        r["Q2_null"].append(float(dx * (rho[k0 + 1:].sum() + 0.5 * rho[k0])))

    sek_profil = time.time() - t_wand
    t_schleife = time.time()
    for n in range(n_schritte + 1):
        Sv = psi.real * psi.real + psi.imag * psi.imag
        new = 2.0 * psi - old
        pc = psi[1:-1]
        new[1:-1] += dt2 * ((psi[2:] + psi[:-2] - 2.0 * pc) * h2 - u1(Sv[1:-1]) * pc)
        new[:jl1] = (new[:jl1] + dmpL * old[:jl1]) * fpL
        new[jr0:] = (new[jr0:] + dmpR * old[jr0:]) * fpR
        new[0] = 0.0
        new[N] = 0.0
        if n % n_mess == 0:
            messen(n * dt, old, psi, new, Sv)
        if n % n_bild == 0:
            bilder.append(Sv[::sub].astype(np.float32))
            bild_t.append(n * dt)
        if n == 2000:
            je = (time.time() - t_schleife) / 2000.0
            print(f"  nach 2000 Schritten: {je * 1e3:.3f} ms je Schritt, geschaetzt {je * n_schritte:.0f} s", flush=True)
        old, psi = psi, new
    meta["sek_profil"] = sek_profil
    meta["sek_schleife"] = time.time() - t_schleife
    meta["n_schritte"] = n_schritte
    roh = {k: np.asarray(v, dtype=np.float64) for k, v in reihen.items()}
    roh["bilder"] = np.stack(bilder)
    roh["bild_t"] = np.asarray(bild_t)
    roh["bild_x"] = x[::sub]
    meta["sek_bis_roh"] = time.time() - t_wand
    return roh, meta


# ================================================================ Auswertung

def idx(t0, t1, n):
    i0 = max(0, int(math.ceil(t0 / MESS - 1e-9)))
    i1 = min(n, int(math.floor(t1 / MESS + 1e-9)) + 1)
    return i0, i1


def steigung(t, y, t0, t1):
    i0, i1 = idx(t0, t1, t.size)
    if i1 - i0 < 3:
        return None
    return float(np.polyfit(t[i0:i1], y[i0:i1], 1)[0])


def mittel(t, y, t0, t1):
    i0, i1 = idx(t0, t1, t.size)
    return float(np.mean(y[i0:i1])) if i1 > i0 else None


def median(t, y, t0, t1):
    i0, i1 = idx(t0, t1, t.size)
    return float(np.median(y[i0:i1])) if i1 > i0 else None


def pencil_dom(t, y, t0, t1, K=12):
    i0, i1 = idx(t0, t1, t.size)
    if i1 - i0 < 12:
        return {"t0": t0, "t1": t1, "dominant": None, "liste": []}
    seg = y[i0:i1] - y[i0:i1].mean()
    p = matrix_pencil(seg, MESS, K)
    kand = [e for e in p if abs(e["re"]) >= SCHWELLE_RE]
    dom = max(kand, key=lambda e: e["amp"]) if kand else None
    return {"t0": t0, "t1": t1, "dominant": dom, "liste": p[:8], "spanne": float(seg.max() - seg.min())}


def gleitend(t, ph, w=FENSTER_GLEIT, schritt=5.0):
    tcs, oms = [], []
    tc = w / 2.0
    while tc <= t[-1] - w / 2.0 + 1e-9:
        s = steigung(t, ph, tc - w / 2.0, tc + w / 2.0)
        tcs.append(tc)
        oms.append(-s)
        tc += schritt
    return np.asarray(tcs), np.asarray(oms)


def auswerten(roh, meta):
    t_an = time.time()
    t = roh["t"]
    T = meta["T"]
    a = {}
    if meta["modus"] == "einzel":
        sz = roh["S_zentrum"]
        ph = np.unwrap(roh["ph_zentrum"])
        a["S_zentrum_anfang"] = float(sz[0])
        a["S_zentrum_rel_abw_max"] = float(np.max(np.abs(sz - sz[0])) / sz[0])
        a["omega_fit_gesamt"] = -steigung(t, ph, 0.0, T)
        tcs, oms = gleitend(t, ph)
        a["omega_gleitend_min"] = float(oms.min())
        a["omega_gleitend_max"] = float(oms.max())
        a["omega_diskret_soll"] = meta["omega_a_diskret"]
        a["Q_innen_anfang"] = float(roh["Q_innen"][0])
        a["Q_innen_ende"] = float(roh["Q_innen"][-1])
        a["kriterium_1e-8"] = bool(a["S_zentrum_rel_abw_max"] < 1e-8)
        meta["analyse"] = a
        meta["sek_analyse"] = time.time() - t_an
        return
    dwn = meta["delta_omega_nominal"]
    P = 2.0 * math.pi / dwn if dwn > 0 else 200.0
    fa, fe = (50.0, 50.0 + 2.0 * P), (T - 2.0 * P, T)
    drittel = [(50.0, T / 3.0), (T / 3.0, 2.0 * T / 3.0), (2.0 * T / 3.0, T)]
    a["periode_nominal"] = P
    a["fenster_anfang"], a["fenster_ende"], a["drittel"] = fa, fe, drittel
    ph1, ph2 = np.unwrap(roh["ph1"]), np.unwrap(roh["ph2"])
    d = roh["p2"] - roh["p1"]
    dX = roh["X2"] - roh["X1"]
    # Frequenzen
    w = {}
    for nm, (t0, t1) in (("anfang", fa), ("ende", fe)):
        o1, o2 = -steigung(t, ph1, t0, t1), -steigung(t, ph2, t0, t1)
        w[nm] = {"omega1": o1, "omega2": o2, "delta": o2 - o1, "betrag_delta": abs(o2 - o1)}
    w["drittel"] = []
    for (t0, t1) in drittel:
        o1, o2 = -steigung(t, ph1, t0, t1), -steigung(t, ph2, t0, t1)
        w["drittel"].append({"t0": t0, "t1": t1, "omega1": o1, "omega2": o2, "delta": o2 - o1})
    tcs, o1g = gleitend(t, ph1)
    _, o2g = gleitend(t, ph2)
    w["gleitend"] = {"omega1_min": float(o1g.min()), "omega1_max": float(o1g.max()),
                     "omega2_min": float(o2g.min()), "omega2_max": float(o2g.max()),
                     "delta_min": float((o2g - o1g).min()), "delta_max": float((o2g - o1g).max()),
                     "tc": tcs[::4].tolist(), "omega1": o1g[::4].tolist(), "omega2": o2g[::4].tolist()}
    ref = w["anfang"]["betrag_delta"]
    w["rel_aenderung_betrag_delta_gemessen"] = (abs(w["ende"]["betrag_delta"] - ref) / ref) if ref > 0 else None
    w["rel_aenderung_betrag_delta_nominal"] = (abs(w["ende"]["betrag_delta"] - dwn) / dwn) if dwn > 0 else None
    a["frequenzen"] = w
    # Schwebung in der Mittelpunktsdichte (beweglicher Mittelpunkt, gewertet) und bei x = 0 (fest, Vergleich)
    a["schwebung_mitte"] = [pencil_dom(t, roh["S_mitte"], t0, t1) for (t0, t1) in drittel]
    a["schwebung_null"] = [pencil_dom(t, roh["S_null"], t0, t1) for (t0, t1) in drittel]
    a["schwebung_mitte_gesamt"] = pencil_dom(t, roh["S_mitte"], 50.0, T)
    # Ladungen
    q = {}
    for nm, (t0, t1) in (("anfang", fa), ("ende", fe)):
        q[nm] = {"Q1": mittel(t, roh["Q1"], t0, t1), "Q2": mittel(t, roh["Q2"], t0, t1),
                 "Q1_null": mittel(t, roh["Q1_null"], t0, t1), "Q2_null": mittel(t, roh["Q2_null"], t0, t1),
                 "Q_innen": mittel(t, roh["Q_innen"], t0, t1)}
    q["netto_Q1"] = q["ende"]["Q1"] - q["anfang"]["Q1"]
    q["netto_Q1_rel"] = q["netto_Q1"] / q["anfang"]["Q1"]
    q["netto_Q1_null_rel"] = (q["ende"]["Q1_null"] - q["anfang"]["Q1_null"]) / q["anfang"]["Q1_null"]
    q["pendel_Q1"] = [pencil_dom(t, roh["Q1"], t0, t1) for (t0, t1) in drittel]
    q["Q1_spanne_drittel"] = [p.get("spanne") for p in q["pendel_Q1"]]
    q["Q_innen_start"] = float(roh["Q_innen"][0])
    q["Q_innen_ende"] = float(roh["Q_innen"][-1])
    a["ladungen"] = q
    # Abstaende
    i500 = idx(0.0, 500.0, t.size)[1]
    abst = {"maxima_anfang": mittel(t, d, fa[0], fa[1]), "maxima_ende": mittel(t, d, fe[0], fe[1]),
            "maxima_median_letzte100": median(t, d, T - 100.0, T), "maxima_min_bis500": float(d[:i500].min()),
            "maxima_min": float(d.min()), "maxima_max": float(d.max()),
            "schwerpunkt_anfang": mittel(t, dX, fa[0], fa[1]), "schwerpunkt_ende": mittel(t, dX, fe[0], fe[1]),
            "p1_ende": float(roh["p1"][-1]), "p2_ende": float(roh["p2"][-1]),
            "p_betrag_max": float(max(np.abs(roh["p1"]).max(), np.abs(roh["p2"]).max()))}
    unter = np.nonzero(d < D_MERGE)[0]
    abst["erstmals_verschmolzen_t"] = float(t[unter[0]]) if unter.size else None
    abst["verschmolzen_bei_T"] = bool(abst["maxima_median_letzte100"] < D_MERGE)
    rand = np.nonzero(np.maximum(np.abs(roh["p1"]), np.abs(roh["p2"])) > meta["x_sd"] - 20.0)[0]
    abst["rand_erreicht_t"] = float(t[rand[0]]) if rand.size else None
    sch = max(1, t.size // 1500)
    abst["roh_t"] = t[::sch].tolist()
    abst["roh_maxima"] = d[::sch].tolist()
    a["abstaende"] = abst
    a["roh_S_mitte"] = roh["S_mitte"][::sch].tolist()
    a["roh_Q1"] = roh["Q1"][::sch].tolist()
    # Urteile nach PLAN (Regeln vor dem Lauf festgelegt)
    u_ = {}
    if dwn > 0:
        doms = [s["dominant"] for s in a["schwebung_mitte"]]
        u_["S1_abw_rel_je_drittel"] = [abs(abs(e["re"]) - dwn) / dwn if e else None for e in doms]
        u_["S1_erfuellt"] = bool(all(v is not None and v <= 0.01 for v in u_["S1_abw_rel_je_drittel"])
                                 and not abst["verschmolzen_bei_T"])
        pd = [s["dominant"] for s in q["pendel_Q1"]]
        u_["S2_pendel_abw_rel_je_drittel"] = [abs(abs(e["re"]) - dwn) / dwn if e else None for e in pd]
        u_["S2_netto_ok"] = bool(abs(q["netto_Q1_rel"]) < 0.05)
        u_["S2_pendel_ok"] = bool(all(v is not None and v <= 0.05 for v in u_["S2_pendel_abw_rel_je_drittel"]))
        u_["S2_erfuellt"] = bool(u_["S2_netto_ok"] and u_["S2_pendel_ok"] and not abst["verschmolzen_bei_T"])
        r_ = w["rel_aenderung_betrag_delta_gemessen"]
        u_["S3_erfuellt_wenn_D"] = bool(r_ is not None and r_ < 0.10 and not abst["verschmolzen_bei_T"])
        u_["S4_erfuellt_wenn_Dstrich"] = bool((r_ is not None and r_ >= 0.10) or abst["verschmolzen_bei_T"])
    else:
        u_["S0_anziehung"] = bool(abst["maxima_min_bis500"] < meta["D"] - 1.0)
        u_["S0_verschmolzen_bei_T"] = abst["verschmolzen_bei_T"]
        u_["S0_abstossung"] = bool(abst["maxima_median_letzte100"] > meta["D"] + 1.0)
    a["urteile"] = u_
    meta["analyse"] = a
    meta["sek_analyse"] = time.time() - t_an


# ================================================================ Hauptprogramm

def profil_tabelle(dx, pfad):
    t0 = time.time()
    M = int(round(40.0 / dx))
    out = {"dx": dx, "profile": {}, "kandidaten": []}
    prof = {}
    for w2 in (0.60, 0.65):
        f, res = profil_diskret(w2, dx, M)
        prof[w2] = f
        out["profile"][str(w2)] = {"f0": float(f[0]), "S0": float(f[0] ** 2), "newton": res,
                                   "S0_kontinuum": float(kontinuum(w2, np.zeros(1))[0] ** 2),
                                   "Q_diskret": float(2.0 * math.sqrt(w2) * dx * (f[0] ** 2 + 2.0 * (f[1:] ** 2).sum())),
                                   "Q_kontinuum": ladung_kontinuum(w2)}
    for D in D_KANDIDATEN + [4.4, 4.6, 4.8, 14.4, 14.6, 14.8]:
        j = int(round(D / dx))
        sb_a = float(prof[0.65][j] ** 2)       # Dichte von Ball b (0,65) am Zentrum von a
        sa_b = float(prof[0.60][j] ** 2)       # Dichte von Ball a (0,60) am Zentrum von b
        jm = int(round(D / (2.0 * dx)))
        out["kandidaten"].append({"D": D, "dichte_b_bei_a": sb_a, "dichte_a_bei_b": sa_b,
                                  "geom_mittel": math.sqrt(sb_a * sa_b),
                                  "abstand_log10_zu_1e-3": abs(math.log10(math.sqrt(sb_a * sa_b)) + 3.0),
                                  "S_a_mitte": float(prof[0.60][jm] ** 2), "S_b_mitte": float(prof[0.65][jm] ** 2)})
    gew = min([k for k in out["kandidaten"] if k["D"] in D_KANDIDATEN], key=lambda k: k["abstand_log10_zu_1e-3"])
    out["D_gewaehlt"] = gew["D"]
    out["sek"] = time.time() - t0
    schreiben(out, pfad)
    print(f"profil dx {dx}: D = {gew['D']} (geom. Mittel {gew['geom_mittel']:.3e})", flush=True)


def main():
    modus = sys.argv[1]
    if modus == "profil":
        profil_tabelle(float(sys.argv[2]), sys.argv[3])
        return
    if modus == "auswerten":
        z = np.load(sys.argv[2], allow_pickle=False)
        roh = {k: z[k] for k in z.files}
        meta = json.loads(str(roh.pop("meta_json")))
        auswerten(roh, meta)
        meta["ausgewertet_aus"] = sys.argv[2]
        schreiben(meta, sys.argv[3])
        print(f"ausgewertet: {sys.argv[2]}", flush=True)
        return
    if modus == "einzel":
        w2a, dx, T, L, pfad = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), sys.argv[6]
        roh, meta = zeitlauf("einzel", w2a, 0.0, 0.0, 0.0, dx, T, L)
    elif modus == "paar":
        w2a, w2b, D, th = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
        dx, T, L, pfad = float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), sys.argv[9]
        roh, meta = zeitlauf("paar", w2a, w2b, D, th, dx, T, L)
    else:
        raise SystemExit("modus: profil | einzel | paar | auswerten")
    np.savez_compressed(pfad + ".roh.tmp.npz", meta_json=np.asarray(json.dumps(jsonfest(meta))), **roh)
    os.replace(pfad + ".roh.tmp.npz", pfad + ".roh.npz")
    try:
        auswerten(roh, meta)
    except Exception as e:                      # Rohdaten sind gesichert; Fehler nur vermerken
        meta["analyse_fehler"] = repr(e)
        meta["sek_analyse"] = 0.0
    meta["sek"] = time.time() - T_START
    schreiben(meta, pfad)
    print(f"schwebung1d fertig: {modus} {sys.argv[2:-1]}, Profil {meta['sek_profil']:.1f} s, Schleife "
          f"{meta['sek_schleife']:.1f} s, Analyse {meta['sek_analyse']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
