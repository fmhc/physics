#!/usr/bin/env python3
"""WINKELFELD-1 (Runde 22), Leitung claude-primary, 02.10.2026. Karte: RUNDE-22/winkelfeld-1/KARTE.md.

Federnetze mit Winkelquellen:
  2D: Dreiecksgitter-Scheibe (Radius R, Gitterkonstante 1). Winkelquelle der Staerke s (Grad) an Ecke v: die sechs
      Randkanten des Sechsecks um v bekommen die Ruhelaenge 2 sin(theta/2), theta = (360 - s)/6 Grad; Speichen bleiben 1.
      Flach (2D-Koordinaten) oder beulend (3D-Koordinaten, Biegeenergie kappa Sum (1 - n1.n2) ueber Nachbardreiecke).
      Nichtlineare Federn, L-BFGS (scipy) mit Gradient aus torch-Autograd.
  3D: Kuhn-/Freudenthal-Triangulierung des Wuerfels [0, L]^3 (6 Tetraeder je Einheitszelle, alle Tetraederkanten als
      Federn, Ruhelaengen = Bezugslaengen 1, sqrt2, sqrt3). Kantenquelle an Kante (a, b): in jedem Tetraeder, das (a, b)
      enthaelt, bekommt die gegenueberliegende Kante (c, d) die Ruhelaenge (1 - eps) mal Bezugslaenge.
      Linear elastisch: E = 1/2 min_u || B u - dL ||^2 (B Vertraeglichkeitsmatrix), per scipy.sparse.linalg.lsqr.
Aufruf: python winkelfeld.py <arm> <aus.json> [optionen als schluessel=wert]
  arme: F1, F2, F3, B1, D3a, D3b, K
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import json
import math
import sys
import time

import numpy as np
import torch
from scipy.optimize import minimize
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import lsqr

torch.set_num_threads(1)
NB6 = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]      # Nachbarn im Dreiecksgitter, gegen den Uhrzeigersinn


# ------------------------------------------------------------------ 2D-Scheibe
def scheibe(R):
    idx, pos = {}, []
    n = int(math.ceil(2 * R)) + 2
    for j in range(-n, n + 1):
        for i in range(-n, n + 1):
            x, y = i + 0.5 * j, j * math.sqrt(3.0) / 2.0
            if x * x + y * y <= R * R + 1e-9:
                idx[(i, j)] = len(pos)
                pos.append((x, y))
    kanten = []
    for (i, j), a in idx.items():
        for di, dj in ((1, 0), (0, 1), (-1, 1)):
            b = idx.get((i + di, j + dj))
            if b is not None:
                kanten.append((a, b))
    dreiecke = []
    for (i, j), a in idx.items():
        b, c = idx.get((i + 1, j)), idx.get((i, j + 1))
        if b is not None and c is not None:
            dreiecke.append((a, b, c))                          # oben, gegen den Uhrzeigersinn
        d = idx.get((i + 1, j + 1))
        if b is not None and c is not None and d is not None:
            dreiecke.append((b, d, c))                          # unten, gegen den Uhrzeigersinn
    return idx, np.array(pos), kanten, dreiecke


def ecken_quelle(idx, v, s_grad, ruhe):
    """setzt die Ruhelaengen der sechs Randkanten um v (dict ruhe[(min, max)])."""
    th = math.radians((360.0 - s_grad) / 6.0)
    L = 2.0 * math.sin(0.5 * th)
    i, j = v
    nb = [idx.get((i + di, j + dj)) for di, dj in NB6]
    if any(x is None for x in nb):
        raise ValueError("Quelle zu nah am Rand")
    for k in range(6):
        a, b = nb[k], nb[(k + 1) % 6]
        key = (min(a, b), max(a, b))
        if key in ruhe and abs(ruhe[key] - 1.0) > 1e-15:
            raise ValueError("Randkanten zweier Quellen ueberlappen")
        ruhe[key] = L


def kegel_delta(idx, pos, kanten, apex, s_grad):
    """Ruhelaengen-Aenderung dL_e (gegen 1) fuer eine Kegel-Ruhemetrik mit Fehlwinkel s an der Gitterecke apex:
    Abwicklung theta -> theta (1 - s/2pi) um den Apex; L = sqrt(ri^2 + rj^2 - 2 ri rj cos(dphi)) (Kosinussatz, ohne
    Schnittproblem). Netto-Winkelladung s; der Ausgleich sitzt im verkuerzten Randumfang (Gauss-Bonnet)."""
    c = pos[idx[apex]]
    f = 1.0 - math.radians(s_grad) / (2.0 * math.pi)
    d = {}
    for a, b in kanten:
        ua, ub = pos[a] - c, pos[b] - c
        ra, rb = float(np.hypot(*ua)), float(np.hypot(*ub))
        if ra < 1e-12 or rb < 1e-12:
            L = max(ra, rb)
        else:
            dth = math.atan2(ub[1], ub[0]) - math.atan2(ua[1], ua[0])
            dth = (dth + math.pi) % (2.0 * math.pi) - math.pi
            L = math.sqrt(max(0.0, ra * ra + rb * rb - 2.0 * ra * rb * math.cos(dth * f)))
        d[(min(a, b), max(a, b))] = L - float(np.hypot(*(pos[b] - pos[a])))
    return d


def ruhe_aus_delta(*deltas):
    ruhe = {}
    for dd in deltas:
        for k, v in dd.items():
            ruhe[k] = ruhe.get(k, 1.0) + v
    return ruhe


def nachbarpaare(dreiecke):
    kante_zu = {}
    for t, (a, b, c) in enumerate(dreiecke):
        for x, y in ((a, b), (b, c), (c, a)):
            kante_zu.setdefault((min(x, y), max(x, y)), []).append(t)
    return [tuple(v) for v in kante_zu.values() if len(v) == 2]


def relax2d(pos, kanten, ruhe, dim=2, kappa=0.0, dreiecke=None, saat=1, maxiter=40000):
    N = len(pos)
    E = torch.tensor(kanten, dtype=torch.long)
    L = torch.tensor([ruhe.get((min(a, b), max(a, b)), 1.0) for a, b in kanten], dtype=torch.float64)
    x0 = np.zeros((N, dim))
    x0[:, :2] = pos
    if dim == 3:
        rng = np.random.default_rng(saat)
        x0[:, 2] = 0.01 * rng.standard_normal(N)
        T = torch.tensor(dreiecke, dtype=torch.long)
        P = torch.tensor(nachbarpaare(dreiecke), dtype=torch.long)

    def eg(xf):
        X = torch.tensor(xf.reshape(N, dim), dtype=torch.float64, requires_grad=True)
        d = X[E[:, 1]] - X[E[:, 0]]
        en = 0.5 * ((torch.sqrt((d * d).sum(1)) - L) ** 2).sum()
        if dim == 3 and kappa > 0.0:
            a, b, c = X[T[:, 0]], X[T[:, 1]], X[T[:, 2]]
            n = torch.linalg.cross(b - a, c - a)
            n = n / torch.sqrt((n * n).sum(1, keepdim=True))
            en = en + kappa * (1.0 - (n[P[:, 0]] * n[P[:, 1]]).sum(1)).sum()
        en.backward()
        return float(en.detach()), X.grad.detach().numpy().ravel().copy()

    res = minimize(eg, x0.ravel(), jac=True, method="L-BFGS-B",
                   options=dict(maxiter=maxiter, maxfun=2 * maxiter, gtol=1e-11, ftol=1e-16, maxcor=30))
    g = eg(res.x)[1]
    out = {"E": float(res.fun), "gnorm_max": float(np.abs(g).max()), "nit": int(res.nit), "meldung": str(res.message)}
    if dim == 3:
        X = res.x.reshape(N, 3)
        out["z_spanne"] = float(X[:, 2].max() - X[:, 2].min())
    return out


# ------------------------------------------------------------------ 3D-Kuhn-Netz
def kuhn(L):
    def vid(i, j, k):
        return (i * (L + 1) + j) * (L + 1) + k

    pos = np.array([(i, j, k) for i in range(L + 1) for j in range(L + 1) for k in range(L + 1)], dtype=np.float64)
    tets = []
    e = [np.array((1, 0, 0)), np.array((0, 1, 0)), np.array((0, 0, 1))]
    for i in range(L):
        for j in range(L):
            for k in range(L):
                p = np.array((i, j, k))
                for perm in itertools.permutations(range(3)):
                    q1 = p + e[perm[0]]
                    q2 = q1 + e[perm[1]]
                    q3 = p + 1
                    tets.append(tuple(vid(*v) for v in (p, q1, q2, q3)))
    kanten = set()
    for t in tets:
        for a, b in itertools.combinations(t, 2):
            kanten.add((min(a, b), max(a, b)))
    return pos, sorted(kanten), tets, vid


def kanten_quelle(tets, a, b, eps, pos, aend):
    for t in tets:
        if a in t and b in t:
            c, d = [x for x in t if x not in (a, b)]
            key = (min(c, d), max(c, d))
            L0 = float(np.linalg.norm(pos[c] - pos[d]))
            aend[key] = aend.get(key, 0.0) - eps * L0


def energie_linear(pos, kanten, aend):
    """E = 1/2 min_u ||B u - dL||^2 mit dL_e = Ruhelaengen-Aenderung (nur Kanten mit Aenderung ungleich null)."""
    N, M = len(pos), len(kanten)
    zeilen, spalten, werte = [], [], []
    for r, (a, b) in enumerate(kanten):
        n = pos[b] - pos[a]
        n = n / np.linalg.norm(n)
        for k in range(3):
            zeilen += [r, r]
            spalten += [3 * a + k, 3 * b + k]
            werte += [-n[k], n[k]]
    B = coo_matrix((werte, (zeilen, spalten)), shape=(M, 3 * N)).tocsr()
    dL = np.zeros(M)
    index = {k: r for r, k in enumerate(kanten)}
    for key, v in aend.items():
        dL[index[key]] = v
    sol = lsqr(B, dL, atol=1e-15, btol=1e-15, iter_lim=200000)
    u = sol[0]
    rest = B @ u - dL
    return {"E": 0.5 * float(rest @ rest), "lsqr_istop": int(sol[1]), "lsqr_iter": int(sol[2]),
            "dL_norm2_halbe": 0.5 * float(dL @ dL)}


# ------------------------------------------------------------------ Arme
def arm_2d_einzel(Rs, s, dim, kappa, art="kegel"):
    """art 'kegel': Netto-Winkelladung s (Kegel-Ruhemetrik); art 'neutral': Sechseck-Randkanten (netto null)."""
    aus = []
    for R in Rs:
        idx, pos, kanten, dreiecke = scheibe(R)
        if art == "kegel":
            ruhe = ruhe_aus_delta(kegel_delta(idx, pos, kanten, (0, 0), s))
        else:
            ruhe = {}
            ecken_quelle(idx, (0, 0), s, ruhe)
        r = relax2d(pos, kanten, ruhe, dim=dim, kappa=kappa, dreiecke=dreiecke)
        r.update(R=R, N=len(pos), art=art)
        aus.append(r)
        print(f"  R = {R}: E = {r['E']:.8g}, |g| = {r['gnorm_max']:.1e}", flush=True)
    return aus


def arm_2d_dipol(Rs, s, abstand):
    """Kegel +s bei (0, 0) und Kegel -s bei (abstand, 0), Ruhelaengen-Aenderungen ueberlagert."""
    aus = []
    for R in Rs:
        idx, pos, kanten, _ = scheibe(R)
        ruhe = ruhe_aus_delta(kegel_delta(idx, pos, kanten, (0, 0), s),
                              kegel_delta(idx, pos, kanten, (abstand, 0), -s))
        r = relax2d(pos, kanten, ruhe)
        r.update(R=R, N=len(pos))
        aus.append(r)
        print(f"  R = {R}: E = {r['E']:.8g}, |g| = {r['gnorm_max']:.1e}", flush=True)
    return aus


def arm_2d_paar(R, s, ds):
    """zwei gleichnamige Kegel +s im Abstand d (ueberlagerte Ruhelaengen-Aenderungen)."""
    idx, pos, kanten, _ = scheibe(R)
    aus = []
    for d in ds:
        a, b = (-(d // 2), 0), (d - d // 2, 0)
        werte = {}
        da, db = kegel_delta(idx, pos, kanten, a, s), kegel_delta(idx, pos, kanten, b, s)
        for name, deltas in (("beide", (da, db)), ("a", (da,)), ("b", (db,))):
            werte[name] = relax2d(pos, kanten, ruhe_aus_delta(*deltas))
        e_int = werte["beide"]["E"] - werte["a"]["E"] - werte["b"]["E"]
        aus.append({"d": d, "E_int": e_int, "E_beide": werte["beide"]["E"], "E_a": werte["a"]["E"], "E_b": werte["b"]["E"],
                    "gnorm_max": max(w["gnorm_max"] for w in werte.values())})
        print(f"  d = {d}: E_int = {e_int:.8g}", flush=True)
    return aus


def arm_3d_einzel(Ls, eps):
    aus = []
    for L in Ls:
        pos, kanten, tets, vid = kuhn(L)
        m = L // 2
        aend = {}
        kanten_quelle(tets, vid(m, m, m), vid(m, m, m + 1), eps, pos, aend)
        r = energie_linear(pos, kanten, aend)
        r.update(L=L, N=len(pos), E_durch_eps2=r["E"] / eps ** 2)
        aus.append(r)
        print(f"  L = {L}: E/eps^2 = {r['E_durch_eps2']:.10g} (istop {r['lsqr_istop']})", flush=True)
    return aus


def arm_3d_paar(L, eps, ds):
    pos, kanten, tets, vid = kuhn(L)
    m = L // 2
    aus = []
    for d in ds:
        ia, ib = m - d // 2, m - d // 2 + d
        qa, qb = (vid(ia, m, m), vid(ia, m, m + 1)), (vid(ib, m, m), vid(ib, m, m + 1))
        werte = {}
        ea, eb = {}, {}
        kanten_quelle(tets, qa[0], qa[1], eps, pos, ea)
        kanten_quelle(tets, qb[0], qb[1], eps, pos, eb)
        ueberlapp = len(set(ea) & set(eb))
        for name, quellen in (("beide", (qa, qb)), ("a", (qa,)), ("b", (qb,))):
            aend = {}
            for q in quellen:
                kanten_quelle(tets, q[0], q[1], eps, pos, aend)
            werte[name] = energie_linear(pos, kanten, aend)
        e_int = werte["beide"]["E"] - werte["a"]["E"] - werte["b"]["E"]
        aus.append({"d": d, "E_int": e_int, "E_int_durch_eps2": e_int / eps ** 2, "ueberlappende_kanten": ueberlapp,
                    "E_a_durch_eps2": werte["a"]["E"] / eps ** 2, "istop": [w["lsqr_istop"] for w in werte.values()]})
        print(f"  d = {d}: E_int/eps^2 = {e_int / eps ** 2:.6e}", flush=True)
    return aus


def main():
    arm, pfad = sys.argv[1], sys.argv[2]
    opt = dict(a.split("=", 1) for a in sys.argv[3:])
    t0 = time.time()
    out = {"arm": arm, "optionen": opt}
    if arm == "F1":
        out["werte"] = arm_2d_einzel([int(x) for x in opt.get("R", "6,9,12,15,18,24").split(",")], float(opt.get("s", 60)), 2, 0.0)
    elif arm == "N1":
        out["werte"] = arm_2d_einzel([int(x) for x in opt.get("R", "6,9,12,15,18,24").split(",")], float(opt.get("s", 60)), 2, 0.0,
                                     art="neutral")
    elif arm == "F2":
        out["werte"] = arm_2d_dipol([int(x) for x in opt.get("R", "6,9,12,15,18,24").split(",")], float(opt.get("s", 60)),
                                    int(opt.get("abstand", 2)))
    elif arm == "F3":
        out["werte"] = arm_2d_paar(int(opt.get("R", 24)), float(opt.get("s", 60)),
                                   [int(x) for x in opt.get("d", "2,3,4,5,6,8,10,12").split(",")])
    elif arm == "B1":
        out["werte"] = arm_2d_einzel([int(x) for x in opt.get("R", "6,9,12,15,18,24").split(",")], float(opt.get("s", 60)), 3,
                                     float(opt.get("kappa", 0.01)))
    elif arm == "D3a":
        out["werte"] = arm_3d_einzel([int(x) for x in opt.get("L", "8,10,12,14").split(",")], float(opt.get("eps", 0.05)))
    elif arm == "D3b":
        out["werte"] = arm_3d_paar(int(opt.get("L", 16)), float(opt.get("eps", 0.05)),
                                   [int(x) for x in opt.get("d", "2,3,4,5,6").split(",")])
    elif arm == "K":
        idx, pos, kanten, dreiecke = scheibe(9)
        out["flach_ohne_quelle"] = relax2d(pos, kanten, {})
        out["beulend_ohne_quelle"] = relax2d(pos, kanten, {}, dim=3, kappa=0.01, dreiecke=dreiecke)
        pk, kk, tk, vk = kuhn(6)
        out["kuhn_ohne_quelle"] = energie_linear(pk, kk, {})
        out["kuhn_kanten"] = len(kk)
        out["kuhn_tetraeder"] = len(tk)
        ruhe = {}
        ecken_quelle(idx, (0, 0), 0.0, ruhe)
        out["flach_quelle_null"] = relax2d(pos, kanten, ruhe)
    else:
        raise SystemExit("unbekannter Arm")
    out["sek"] = time.time() - t0
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    print(f"winkelfeld fertig: {arm}, {out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
