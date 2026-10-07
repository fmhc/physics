#!/usr/bin/env python3
"""V4 Ticks ereignisgenau (Runde 16, ausprobieren).
Zwei starre regulaere Tetraeder durchdringen sich (analytische Bahn).
Ticks = Vorzeichenwechsel von chi = det[x_b - x_a, x_c - x_a, x_d - x_a] fuer Ecke-Flaeche- und
Kante-Kante-Paare zwischen den Koerpern, Zeit per brentq, dann Innen-Test.
Naiv: Menge B(t_k) der sich schneidenden (Kante, Flaeche)-Paare, Zahl = sum |B_k Delta B_k+1|.
Aufruf: python v4_ticks.py <ausgabeordner> [schnell]
"""
import json, os, sys, time
import numpy as np
from scipy.optimize import brentq
from scipy.spatial.transform import Rotation

OUT = sys.argv[1] if len(sys.argv) > 1 else "aus"
SCHNELL = len(sys.argv) > 2 and sys.argv[2] == "schnell"
os.makedirs(OUT, exist_ok=True)
T00 = time.time()

TET = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
TET /= np.linalg.norm(TET[0] - TET[1])
FACES = [(1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2)]
EDGES = [(i, j) for i in range(4) for j in range(i + 1, 4)]
OMA = 1.0
OMB = np.sqrt(2.0)
NB = np.array([1.0, 2.0, 2.0]) / 3.0
R0B = Rotation.random(random_state=1).as_matrix()
C0 = np.array([0.25, 0.1, 0.05])
AMP, OMC = 0.3, 0.618


def rot_axis(n, ang):
    # Rodrigues, ang: Feld (K,) -> (K,3,3)
    ang = np.atleast_1d(ang)
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    s, c = np.sin(ang)[:, None, None], np.cos(ang)[:, None, None]
    return np.eye(3)[None] + s * K[None] + (1 - c) * (K @ K)[None]


def positions(t, c0):
    t = np.atleast_1d(t)
    RA = rot_axis(np.array([0, 0, 1.0]), OMA * t)
    RB = rot_axis(NB, OMB * t) @ R0B[None]
    XA = np.einsum("kij,vj->kvi", RA, TET)
    cB = c0[None, :] + np.outer(AMP * np.sin(OMC * t), [1.0, 0, 0])
    XB = np.einsum("kij,vj->kvi", RB, TET) + cB[:, None, :]
    return XA, XB  # (K,4,3)


# Paare: Typ, Koerper der Ecke/ersten Kante, Indizes
PAIRS = []
for p in range(4):
    for f in range(4):
        PAIRS.append(("EF", 0, p, f))  # Ecke von A durch Flaeche von B
        PAIRS.append(("EF", 1, p, f))  # Ecke von B durch Flaeche von A
for ea in range(6):
    for eb in range(6):
        PAIRS.append(("KK", 0, ea, eb))


def det3(u, v, w):
    return np.einsum("...i,...i->...", u, np.cross(v, w))


def chi_all(XA, XB):
    out = np.zeros((XA.shape[0], len(PAIRS)))
    for n, (typ, body, i1, i2) in enumerate(PAIRS):
        if typ == "EF":
            P, Q = (XA, XB) if body == 0 else (XB, XA)
            a, b, c = FACES[i2]
            xa = Q[:, a]
            out[:, n] = det3(Q[:, b] - xa, Q[:, c] - xa, P[:, i1] - xa)
        else:
            a, b = EDGES[i1]
            c, d = EDGES[i2]
            xa = XA[:, a]
            out[:, n] = det3(XA[:, b] - xa, XB[:, c] - xa, XB[:, d] - xa)
    return out


def chi_one(t, n, c0):
    XA, XB = positions(t, c0)
    typ, body, i1, i2 = PAIRS[n]
    if typ == "EF":
        P, Q = (XA, XB) if body == 0 else (XB, XA)
        a, b, c = FACES[i2]
        xa = Q[0, a]
        return float(det3(Q[0, b] - xa, Q[0, c] - xa, P[0, i1] - xa))
    a, b = EDGES[i1]
    c, d = EDGES[i2]
    xa = XA[0, a]
    return float(det3(XA[0, b] - xa, XB[0, c] - xa, XB[0, d] - xa))


def inside(t, n, c0):
    XA, XB = positions(t, c0)
    typ, body, i1, i2 = PAIRS[n]
    if typ == "EF":
        P, Q = (XA, XB) if body == 0 else (XB, XA)
        a, b, c = FACES[i2]
        A_, B_, C_ = Q[0, a], Q[0, b], Q[0, c]
        p = P[0, i1]
        M = np.column_stack([B_ - A_, C_ - A_])
        lam, *_ = np.linalg.lstsq(M, p - A_, rcond=None)
        bary = np.array([1 - lam.sum(), lam[0], lam[1]])
        return bool(np.all(bary >= 0)), float(bary.min())
    a, b = EDGES[i1]
    c, d = EDGES[i2]
    pa, pb, pc, pd = XA[0, a], XA[0, b], XB[0, c], XB[0, d]
    M = np.column_stack([pb - pa, -(pd - pc)])
    su, *_ = np.linalg.lstsq(M, pc - pa, rcond=None)
    return bool(0 <= su[0] <= 1 and 0 <= su[1] <= 1), float(min(su[0], 1 - su[0], su[1], 1 - su[1]))


# (Kante, Flaeche)-Paare fuer den naiven Zustand: Kanten von A gegen Flaechen von B und umgekehrt
def naive_state(XA, XB):
    st = []
    for P, Q in ((XA, XB), (XB, XA)):
        for (p, q) in EDGES:
            for (a, b, c) in FACES:
                xp, xq = P[:, p], P[:, q]
                xa, xb, xc = Q[:, a], Q[:, b], Q[:, c]
                s1 = det3(xb - xa, xc - xa, xp - xa)
                s2 = det3(xb - xa, xc - xa, xq - xa)
                o1 = det3(xq - xp, xa - xp, xb - xp)
                o2 = det3(xq - xp, xb - xp, xc - xp)
                o3 = det3(xq - xp, xc - xp, xa - xp)
                hit = (s1 * s2 < 0) & (((o1 > 0) & (o2 > 0) & (o3 > 0)) | ((o1 < 0) & (o2 < 0) & (o3 < 0)))
                st.append(hit)
    return np.array(st).T  # (K, 48)


def run(dt, T, c0, mit_naiv=True):
    t1 = time.time()
    K = int(round(T / dt))
    ts = np.arange(K + 1) * dt
    ev = []
    n_sign = 0
    nb = 0
    naive_sum = 0
    naive_steps = 0
    chunk = 20000
    last = None
    lastB = None
    for s0 in range(0, K + 1, chunk):
        tt = ts[s0:min(K + 1, s0 + chunk)]
        XA, XB = positions(tt, c0)
        ch = chi_all(XA, XB)
        if last is not None:
            ch = np.vstack([last[None], ch])
            tt = np.concatenate([[last_t], tt])
        sg = np.sign(ch)
        flips = np.argwhere(sg[1:] * sg[:-1] < 0)
        for (k, n) in flips:
            n_sign += 1
            ta, tb = tt[k], tt[k + 1]
            ts_ = brentq(chi_one, ta, tb, args=(n, c0), xtol=1e-14, rtol=1e-15, maxiter=200)
            ok, marg = inside(ts_, n, c0)
            if ok:
                ev.append((int(n), float(ts_), PAIRS[n][0], marg))
        if mit_naiv:
            Bst = naive_state(*positions(ts[s0:min(K + 1, s0 + chunk)], c0))
            if lastB is not None:
                Bst = np.vstack([lastB[None], Bst])
            dif = Bst[1:] != Bst[:-1]
            naive_sum += int(dif.sum())
            naive_steps += int(np.any(dif, axis=1).sum())
            lastB = Bst[-1]
        last = ch[-1]
        last_t = tt[-1]
    ev.sort(key=lambda e: e[1])
    nEF = sum(1 for e in ev if e[2] == "EF")
    nKK = sum(1 for e in ev if e[2] == "KK")
    return {"dt": dt, "T": T, "n_vorzeichenwechsel": n_sign, "N_EF": nEF, "N_KK": nKK, "N_ticks": nEF + nKK,
            "nu": (nEF + nKK) / T, "naiv_summe": naive_sum, "naiv_schritte_mit_wechsel": naive_steps,
            "naiv_soll_3EF_4KK": 3 * nEF + 4 * nKK, "min_innen_rand": float(min([e[3] for e in ev])) if ev else None,
            "sekunden": time.time() - t1}, ev


def match(ev, ref):
    # Abgleich nach Paar und Zeit
    from collections import defaultdict
    d = defaultdict(list)
    for e in ref:
        d[e[0]].append(e[1])
    used = set()
    maxdt = 0.0
    unmatched = 0
    for e in ev:
        cand = d.get(e[0], [])
        if not cand:
            unmatched += 1
            continue
        j = int(np.argmin([abs(c - e[1]) for c in cand]))
        if abs(cand[j] - e[1]) < 1e-6 and (e[0], j) not in used:
            used.add((e[0], j))
            maxdt = max(maxdt, abs(cand[j] - e[1]))
        else:
            unmatched += 1
    return maxdt, unmatched, len(ref) - len(used)


res = {"versuch": "V4", "parameter": {"omega_A": OMA, "omega_B": OMB, "n_B": NB.tolist(), "c0": C0.tolist(),
                                       "amp": AMP, "omega_c": OMC}}
T = 100.0 if SCHNELL else 200.0
dts = [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]
dtref = 0.005 if SCHNELL else 0.001
rref, evref = run(dtref, T, C0)
res["referenz"] = rref
print("Referenz", rref, flush=True)
laeufe = []
for dt in dts:
    r, ev = run(dt, T, C0)
    mdt, un_ev, un_ref = match(ev, evref)
    r["max_abw_ereigniszeit_gegen_ref"] = mdt
    r["ereignisse_ohne_partner_in_ref"] = un_ev
    r["ref_ereignisse_verpasst"] = un_ref
    laeufe.append(r)
    print(r, flush=True)
res["laeufe_T200"] = laeufe
# Rate gegen Laufzeit
if not SCHNELL:
    r4, _ = run(0.005, 400.0, C0, mit_naiv=False)
    res["lauf_T400_dt0.005"] = r4
    print("T400", r4, flush=True)
# Robustheit: 5 Stoerungen von c0
rng = np.random.default_rng(5)
rob = []
for i in range(5 if not SCHNELL else 2):
    c0p = C0 + 1e-3 * rng.standard_normal(3)
    r, _ = run(0.01, T, c0p, mit_naiv=False)
    rob.append({"c0": c0p.tolist(), "N_ticks": r["N_ticks"], "nu": r["nu"]})
res["stoerungen"] = rob
print("Stoerungen", rob, flush=True)
# Zeitreihe fuer die Abbildung: Ereigniszeiten der Referenz
np.savez_compressed(os.path.join(OUT, "v4_ref_ereignisse.npz"), t=np.array([e[1] for e in evref]),
                    pair=np.array([e[0] for e in evref]), typ=np.array([1 if e[2] == "KK" else 0 for e in evref]))
res["sekunden_gesamt"] = time.time() - T00
with open(os.path.join(OUT, "v4_ticks.json" if not SCHNELL else "v4_ticks_schnell.json"), "w") as f:
    json.dump(res, f, indent=1)
print("fertig", res["sekunden_gesamt"])
