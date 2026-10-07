#!/usr/bin/env python3
"""BAG-DIM (Runde 24): Beutel-Q-Ball (FLS) auf Graphen. Code-Agent fuer die Leitung claude-primary, 03.10.2026.

MINKOWSKI-DIM-1 (Runde 48, 05.10.2026): Kopie von RUNDE-24/bag-dim/code/bagdim.py (sha256 d6d42765...) mit genau
diesen Zusaetzen: Graph st:<stufe> (Sierpinski-Tetraeder aus Ecken und Kanten der 4^stufe kleinsten Teiltetraeder),
Bauprobe und Eigenwerte im Spektrum-Modus fuer st, Option --periode P (Rasterfaktor r = P^(1/8)), out["ratio"].
Modell, Minimierung, Starts, Wahl und Diagnose sind unveraendert.

Karte: RUNDE-24/bag-dim/KARTE.md. Energie bei festem Q (f, chi reell; Knoten- und Kantengewicht 1, L = Graph-Laplace):
  E = Q^2/(4 S) + f.L f + chi.L chi + Sum_i [(1/4)(chi_i^2 - 1)^2 + chi_i^2 f_i^2],   S = Sum f_i^2,   omega = Q/(2 S)
Minimierung: L-BFGS-B (scipy) mit analytischem Gradienten und fester Jacobi-Skalierung je Minimierung.

Aufrufe:
  python bagdim.py spektrum <graph> <aus.json> [--klein n]
      K0: Spur des Waermeleitungskerns, Plateau wie URSUPPE-1 (Fenster [t, 4t], kleinste relative Schwankung,
      P(t) > 2 c/N, t >= 0,5). Gitter: exakte Produktformel der Pfad-Eigenwerte (Bauprobe gegen eigvalsh eines
      kleinen Gitters aus demselben Code, --klein); sonst volles eigvalsh.
  python bagdim.py beutel <graph> <aus.json> --q0 Q0 --ratio r --k0 K0 --k1 K1 --ra a --rb b [weitere Optionen]
      E(Q) auf dem Raster Q_k = Q0 r^k, k = K0..K1. Starts je Q: Fortsetzung (vorige angenommene Loesung, f mal
      sqrt(Q/Q_vorher)), frischer Beutel mit Radius R0 = max(--rmin, a Q^b) (mit --ohne-frisch nur am ersten k und an
      --pruef-k); an --pruef-k zusaetzlich R0*1,5 und R0/1,5; an --flach-k (oder mit --flach-immer bei jedem Q) ein
      flacher Start. Angenommen (--wahl zentral): kleinste Energie unter den konvergierten kompakten Beuteln am
      Mittelknoten; --wahl alle: unter allen konvergierten Starts.
Graphen: g2:<n> (n x n, offener Rand), g3:<n> (n^3, offener Rand), sg:<stufe> (Sierpinski-Dreieck),
         zr:<N>:<z>:<saat> (zufaelliger z-regulaerer Graph, Erzeuger wie RUNDE-22/ursuppe-1/code/ursuppe.py)
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import argparse
import json
import math
import random
import sys
import time

import numpy as np
import scipy
import scipy.sparse as sp
from scipy.optimize import minimize
from scipy.sparse.csgraph import connected_components, shortest_path

T_START = time.time()


# ---------------------------------------------------------------- Graphen

def gitter(dim, n):
    shape = (n,) * dim
    idx = np.arange(n ** dim).reshape(shape)
    a_l, b_l = [], []
    for ax in range(dim):
        s0 = [slice(None)] * dim
        s1 = [slice(None)] * dim
        s0[ax] = slice(0, n - 1)
        s1[ax] = slice(1, n)
        a_l.append(idx[tuple(s0)].ravel())
        b_l.append(idx[tuple(s1)].ravel())
    a = np.concatenate(a_l)
    b = np.concatenate(b_l)
    coords = np.stack(np.unravel_index(np.arange(n ** dim), shape), axis=1).astype(float)
    m = n // 2
    center = int(np.ravel_multi_index((m,) * dim, shape))
    return dict(N=n ** dim, a=a, b=b, coords=coords, center=center, art=f"g{dim}", dim=dim, n=n)


def sierpinski(stufe):
    """Kleinste Aufwaerts-Dreiecke (A, B) mit A + B < 2^stufe und A & B == 0 (Pascal mod 2), Ecken (A,B), (A+1,B),
    (A,B+1). Mittelknoten = Mitte der Seite (0,0)-(m,0), Abstand 2^(stufe-1) zu zwei Ecken, 2^stufe zur dritten."""
    m = 2 ** stufe
    A, B = np.meshgrid(np.arange(m), np.arange(m), indexing="ij")
    sel = ((A + B) < m) & ((A & B) == 0)
    A = A[sel].ravel()
    B = B[sel].ravel()
    K = m + 1
    v1 = A * K + B
    v2 = (A + 1) * K + B
    v3 = A * K + (B + 1)
    alle = np.unique(np.concatenate([v1, v2, v3]))
    i1, i2, i3 = (np.searchsorted(alle, v) for v in (v1, v2, v3))
    a = np.concatenate([i1, i1, i2])
    b = np.concatenate([i2, i3, i3])
    x = alle // K
    y = alle % K
    coords = np.stack([x + 0.5 * y, y * math.sqrt(3.0) / 2.0], axis=1).astype(float)
    center = int(np.searchsorted(alle, (m // 2) * K + 0))
    assert alle[center] == (m // 2) * K
    return dict(N=len(alle), a=a, b=b, coords=coords, center=center, art="sg", stufe=stufe, dreiecke=int(len(A)))


def sierpinski_tetraeder(stufe):
    """MINKOWSKI-DIM-1: Ecken und Kanten der 4^stufe kleinsten Teiltetraeder. Grosses Tetraeder mit den Ecken
    (0,0,0), (1,1,0), (1,0,1), (0,1,1) mal m = 2^stufe (ganzzahlig). Mittelknoten = Mitte der Kante (0,0,0)-(m,m,0):
    Abstand 2^(stufe-1) zu zwei Ecken, 2^stufe zu den anderen beiden."""
    m = 2 ** stufe
    v = np.array([[0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=np.int64)
    o = np.zeros((1, 3), dtype=np.int64)
    for i in range(stufe):
        s = 2 ** (stufe - 1 - i)
        o = (o[:, None, :] + s * v[None, :, :]).reshape(-1, 3)
    K = m + 1
    ecken = o[:, None, :] + v[None, :, :]
    code = (ecken[..., 0] * K + ecken[..., 1]) * K + ecken[..., 2]
    alle, inv = np.unique(code.ravel(), return_inverse=True)
    inv = np.asarray(inv).reshape(-1, 4)
    paare = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    a = np.concatenate([inv[:, i] for i, j in paare])
    b = np.concatenate([inv[:, j] for i, j in paare])
    x = alle // (K * K)
    y = (alle // K) % K
    z = alle % K
    coords = np.stack([x, y, z], axis=1).astype(float)
    mc = ((m // 2) * K + (m // 2)) * K + 0
    center = int(np.searchsorted(alle, mc))
    assert alle[center] == mc
    return dict(N=len(alle), a=a, b=b, coords=coords, center=center, art="st", stufe=stufe, tetraeder=int(len(o)))


def kanten_von(adj):
    return [(a, b) for a in range(len(adj)) for b in adj[a] if a < b]


def zufall_regulaer(N, z, rng, mischen_je_knoten=100):
    """Wortgleich aus RUNDE-22/ursuppe-1/code/ursuppe.py: Zirkulant C_N(1..z/2), dann mischen_je_knoten * N
    gradgleiche Doppelkanten-Tauschversuche (nur gueltige werden ausgefuehrt)."""
    if z % 2:
        raise ValueError("z gerade")
    adj = [set() for _ in range(N)]
    for v in range(N):
        for s in range(1, z // 2 + 1):
            w = (v + s) % N
            adj[v].add(w)
            adj[w].add(v)
    klist = kanten_von(adj)
    pos = {k: i for i, k in enumerate(klist)}
    for _ in range(mischen_je_knoten * N):
        (a, b), (c, d) = klist[rng.randrange(len(klist))], klist[rng.randrange(len(klist))]
        if len({a, b, c, d}) < 4:
            continue
        if rng.random() < 0.5:
            c, d = d, c
        if c in adj[a] or d in adj[b]:
            continue
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(c); adj[c].add(a); adj[b].add(d); adj[d].add(b)
        for ka, kn in (((a, b), (a, c)), ((c, d), (b, d))):
            ka, kn = (min(ka), max(ka)), (min(kn), max(kn))
            i = pos.pop(ka)
            klist[i] = kn
            pos[kn] = i
    return adj


def zufall(N, z, saat):
    adj = zufall_regulaer(N, z, random.Random(saat))
    kl = kanten_von(adj)
    a = np.array([k[0] for k in kl], dtype=np.int64)
    b = np.array([k[1] for k in kl], dtype=np.int64)
    return dict(N=N, a=a, b=b, coords=None, center=0, art="zr", z=z, saat=saat)


def baue(spec):
    t = spec.split(":")
    if t[0] == "g2":
        G = gitter(2, int(t[1]))
    elif t[0] == "g3":
        G = gitter(3, int(t[1]))
    elif t[0] == "sg":
        G = sierpinski(int(t[1]))
    elif t[0] == "st":
        G = sierpinski_tetraeder(int(t[1]))
    elif t[0] == "zr":
        G = zufall(int(t[1]), int(t[2]), int(t[3]))
    else:
        raise ValueError(spec)
    N, a, b = G["N"], G["a"], G["b"]
    A = sp.coo_matrix((np.ones(len(a)), (a, b)), shape=(N, N))
    A = (A + A.T).tocsr()
    A.sum_duplicates()
    deg = np.asarray(A.sum(axis=1)).ravel()
    L = (sp.diags(deg) - A).tocsr()
    dist = shortest_path(A, method="D", unweighted=True, indices=G["center"])
    ncomp = int(connected_components(A, directed=False)[0])
    dmax = deg.max()
    rand = np.where(deg < dmax)[0]
    d_rand = float(dist[rand].min()) if len(rand) else float("inf")
    if G["coords"] is not None and G["art"] in ("g2", "g3"):
        d_start = np.sqrt(((G["coords"] - G["coords"][G["center"]]) ** 2).sum(1))
    else:
        d_start = dist.copy()
    G.update(spec=spec, A=A, L=L, deg=deg, dist=dist, d_start=d_start, komponenten=ncomp, d_rand=d_rand,
             kanten=int(len(a)), max_eintrag=float(A.max()), grad_min=float(deg.min()), grad_max=float(dmax),
             exzentrizitaet=float(dist[np.isfinite(dist)].max()))
    return G


def graph_info(G):
    return {k: G[k] for k in ("spec", "art", "N", "center", "komponenten", "d_rand", "kanten", "max_eintrag",
                              "grad_min", "grad_max", "exzentrizitaet") if k in G}


# ---------------------------------------------------------------- K0: spektrale Dimension

def plateau(tg, ds, P, c, N):
    """Wortgleich zur Plateau-Regel von RUNDE-22/ursuppe-1/code/ursuppe.py (messen)."""
    gut = P > 2.0 * c / N
    best = None
    for i in range(len(tg)):
        if not gut[i] or tg[i] < 0.5:
            continue
        j = np.searchsorted(tg, 4.0 * tg[i])
        if j >= len(tg) or not gut[j]:
            continue
        seg = ds[i:j + 1]
        var = float((seg.max() - seg.min()) / seg.mean())
        if best is None or var < best["schwankung"]:
            best = {"t0": float(tg[i]), "t1": float(tg[j]), "d_s": float(seg.mean()), "schwankung": var}
    return best


def lauf_spektrum(args):
    G = baue(args.graph)
    N = G["N"]
    c = G["komponenten"]
    tg = np.logspace(-1, 4, 400)
    out = {"modus": "spektrum", "graph": graph_info(G), "scipy": scipy.__version__, "numpy": np.__version__}
    t0 = time.time()
    if G["art"] in ("g2", "g3"):
        n, dim = G["n"], G["dim"]
        lam1 = 2.0 - 2.0 * np.cos(np.pi * np.arange(n) / n)
        w1 = np.exp(-np.outer(tg, lam1))
        z1 = w1.sum(1)
        z1p = (w1 * lam1).sum(1)
        Z = z1 ** dim
        ds = dim * 2.0 * tg * z1p / z1
        P = Z / N
        out["verfahren"] = "Produktformel (Pfad-Eigenwerte 2 - 2 cos(pi k/n))"
        # Bauprobe: kleines Gitter derselben Art aus demselben Code
        nk = args.klein
        Gk = baue(f"g{dim}:{nk}")
        lk = np.sort(np.linalg.eigvalsh(Gk["L"].toarray()))
        l1 = 2.0 - 2.0 * np.cos(np.pi * np.arange(nk) / nk)
        grids = np.meshgrid(*([l1] * dim), indexing="ij")
        lp = np.sort(sum(grids).ravel())
        out["bauprobe"] = {"n_klein": nk, "max_abweichung": float(np.abs(lk - lp).max()), "N_klein": int(Gk["N"])}
    else:
        M = G["L"].toarray()
        lam = np.linalg.eigvalsh(M)
        del M
        lam = np.clip(lam, 0.0, None)
        w = np.exp(-np.outer(tg, lam))
        P = w.sum(1) / N
        ds = 2.0 * tg * (w * lam).sum(1) / w.sum(1)
        out["verfahren"] = "volles eigvalsh"
        out["lambda_2"] = float(np.sort(lam)[min(c, N - 1)])
        out["lambda_max"] = float(lam.max())
        if G["art"] == "sg":
            s = G["stufe"]
            out["bauprobe"] = {"N_soll": (3 ** (s + 1) + 3) // 2, "N": N, "kanten_soll": 3 ** (s + 1),
                               "kanten": G["kanten"], "grad2": int(np.sum(G["deg"] == 2)),
                               "grad4": int(np.sum(G["deg"] == 4))}
        if G["art"] == "st":
            s = G["stufe"]
            out["bauprobe"] = {"N_soll": 2 * 4 ** s + 2, "N": N, "kanten_soll": 6 * 4 ** s, "kanten": G["kanten"],
                               "grad3": int(np.sum(G["deg"] == 3)), "grad6": int(np.sum(G["deg"] == 6)),
                               "d_rand": G["d_rand"], "d_rand_soll": 2 ** (s - 1)}
            out["eigenwerte"] = np.sort(lam).tolist()
    out["sek_eig"] = time.time() - t0
    best = plateau(tg, ds, P, c, N)
    out["plateau"] = best
    out["plateau_ja"] = bool(best is not None and best["schwankung"] < 0.2)
    out["kurve"] = {"t": tg[::5].tolist(), "d_s": ds[::5].tolist(), "P": P[::5].tolist()}
    out["sek"] = time.time() - T_START
    schreibe(args.aus, out)
    print(f"spektrum {args.graph}: plateau {best}, {out['sek']:.1f} s", flush=True)


# ---------------------------------------------------------------- Beutel

def energie(L, Q, f, c):
    S = f @ f
    Lf = L @ f
    Lc = L @ c
    c2 = c * c
    f2 = f * f
    E = Q * Q / (4.0 * S) + f @ Lf + c @ Lc + 0.25 * np.sum((c2 - 1.0) ** 2) + np.sum(c2 * f2)
    om = Q / (2.0 * S)
    gf = 2.0 * Lf + 2.0 * c2 * f - 2.0 * om * om * f
    gc = 2.0 * Lc + c * (c2 - 1.0) + 2.0 * c * f2
    return E, gf, gc


def minimiere(G, Q, f0, c0, maxiter, gtol):
    N = G["N"]
    deg = G["deg"]
    L = G["L"]
    sf = 1.0 / np.sqrt(2.0 * deg + 2.0)
    sc = 1.0 / np.sqrt(2.0 * deg + 2.0 * f0 * f0 + 2.0)

    def fun(x):
        E, gf, gc = energie(L, Q, x[:N] * sf, x[N:] * sc)
        return E, np.concatenate([gf * sf, gc * sc])

    t = time.time()
    res = minimize(fun, np.concatenate([f0 / sf, c0 / sc]), jac=True, method="L-BFGS-B",
                   options=dict(maxiter=maxiter, maxfun=2 * maxiter, maxcor=20, ftol=1e-16, gtol=gtol))
    f = res.x[:N] * sf
    c = res.x[N:] * sc
    E, gf, gc = energie(L, Q, f, c)
    return f, c, {"E": float(E), "nit": int(res.nit), "nfev": int(res.nfev), "msg": str(res.message),
                  "gmax_f": float(np.abs(gf).max()), "gmax_chi": float(np.abs(gc).max()),
                  "sek": time.time() - t}


def diagnose(G, Q, f, c):
    N = G["N"]
    L = G["L"]
    dist = G["dist"]
    S = float(f @ f)
    om = Q / (2.0 * S)
    teile = {"EQ": Q * Q / (4.0 * S), "Egf": float(f @ (L @ f)), "Egc": float(c @ (L @ c)),
             "Epot": float(0.25 * np.sum((c * c - 1.0) ** 2)), "Eint": float(np.sum(c * c * f * f))}
    E = sum(teile.values())
    B = np.where(c < 0.5)[0]
    nB = int(len(B))
    if nB:
        komp = int(connected_components(G["A"][B][:, B], directed=False)[0])
        Rg = float(dist[B].max())
        dmin = float(dist[B].min())
        fin = float(np.sum(f[B] ** 2) / S)
        Rmittel = float(dist[B].mean())
    else:
        komp, Rg, dmin, fin, Rmittel = 0, -1.0, float("inf"), 0.0, -1.0
    imax = int(np.argmax(np.abs(f)))
    # Randabstand: groesster Start-Abstand (Gitter euklidisch, sonst Graphabstand) der Beutelknoten plus 10 <= d_rand
    Rs = float(G["d_start"][B].max()) if nB else -1.0
    nicht_fuellend = bool(nB <= N / 4 and Rs + 10 <= G["d_rand"])
    kompakt = bool(nB >= 1 and komp == 1 and dmin <= 2 and dist[imax] <= 3 and fin >= 0.5 and nicht_fuellend)
    if G["art"] == "g2":
        Reff = math.sqrt(nB / math.pi)
    elif G["art"] == "g3":
        Reff = (3.0 * nB / (4.0 * math.pi)) ** (1.0 / 3.0)
    else:
        Reff = Rg
    return {"E": float(E), "omega": float(om), "S": S, "p_omega": float(Q * om / E), "teile": teile,
            "nB": nB, "komp": komp, "Rg": Rg, "Rs": Rs, "Rmittel": Rmittel, "dmin": dmin, "f2_innen": fin,
            "Reff": Reff,
            "chi_zentrum": float(c[G["center"]]), "chi_min": float(c.min()), "chi_max": float(c.max()),
            "f_zentrum": float(f[G["center"]]), "fmax": float(np.abs(f).max()), "fmin": float(f.min()),
            "d_fmax": float(dist[imax]), "nicht_fuellend": nicht_fuellend, "kompakt": kompakt}


def start_beutel(G, Q, R0):
    d = G["d_start"]
    c = np.clip(np.tanh((d - R0) / 2.0), 0.0, 1.0)
    prof = np.where(d < R0, np.cos(0.5 * np.pi * d / R0), 0.0)
    if prof.sum() <= 0:
        prof[G["center"]] = 1.0
    mu = (prof @ (G["L"] @ prof) + np.sum(c * c * prof * prof)) / (prof @ prof)
    S = Q / (2.0 * math.sqrt(mu))
    f = prof * math.sqrt(S / (prof @ prof))
    return f, c


def start_flach(G, Q):
    N = G["N"]
    f2 = Q / (2.0 * N)
    rng = np.random.default_rng(12345)
    f = math.sqrt(f2) * (1.0 + 1e-3 * rng.standard_normal(N))
    c2 = 1.0 - 2.0 * f2
    c = np.full(N, math.sqrt(c2) if c2 > 0 else 0.0)
    return f, c


def profil(G, f, c):
    """chi und f entlang der +x-Achse vom Mittelknoten (nur Gitter)."""
    if G["art"] not in ("g2", "g3"):
        return None
    n, dim = G["n"], G["dim"]
    m = n // 2
    ks = list(range(0, n - m))
    ids = [int(np.ravel_multi_index(tuple([m + k] + [m] * (dim - 1)), (n,) * dim)) for k in ks]
    return {"x": ks, "chi": [float(c[i]) for i in ids], "f": [float(f[i]) for i in ids]}


def schreibe(pfad, obj):
    with open(pfad + ".tmp", "w") as fh:
        json.dump(obj, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)


def lauf_beutel(args):
    G = baue(args.graph)
    if args.pruef_k == "alle":
        pruef = set(range(args.k0, args.k1 + 1))
    else:
        pruef = set(int(x) for x in args.pruef_k.split(",") if x != "")
    dq = set(int(x) for x in args.dq_k.split(",") if x != "")
    prof_k = set(int(x) for x in args.profil_k.split(",") if x != "")
    flach_ks = set(int(x) for x in args.flach_k.split(",") if x != "")
    out = {"modus": "beutel", "graph": graph_info(G), "argv": sys.argv, "scipy": scipy.__version__,
           "numpy": np.__version__, "punkte": [], "sek_aufbau": time.time() - T_START, "ratio": args.ratio}
    print(f"aufbau {args.graph}: N {G['N']}, {out['sek_aufbau']:.1f} s, d_rand {G['d_rand']}", flush=True)
    prev = None
    t_letzt = 0.0
    for k in range(args.k0, args.k1 + 1):
        Q = args.q0 * args.ratio ** k
        verbraucht = time.time() - T_START
        if verbraucht + 1.3 * t_letzt > args.budget:
            out["abbruch"] = f"Budget: vor k={k} verbraucht {verbraucht:.1f} s, letzter Punkt {t_letzt:.1f} s"
            print(out["abbruch"], flush=True)
            break
        tq = time.time()
        R0 = max(args.rmin, args.ra * Q ** args.rb)
        starts = []
        if prev is not None:
            starts.append(("fort", prev[1] * math.sqrt(Q / prev[0]), prev[2].copy()))
        if prev is None or not args.ohne_frisch or k in pruef:
            starts.append(("frisch", *start_beutel(G, Q, R0)))
        if k in pruef:
            starts.append(("frisch_x1.5", *start_beutel(G, Q, 1.5 * R0)))
            starts.append(("frisch_x0.667", *start_beutel(G, Q, R0 / 1.5)))
        if k in flach_ks or args.flach_immer:
            starts.append(("flach", *start_flach(G, Q)))
        erg = []
        felder = []
        for name, f0, c0 in starts:
            f, c, info = minimiere(G, Q, f0, c0, args.maxiter, args.gtol)
            d = diagnose(G, Q, f, c)
            gmax = max(info["gmax_f"], info["gmax_chi"])
            konv = bool(gmax <= args.gok * max(1.0, d["fmax"]))
            eintrag = {"start": name, "R0": (1.5 * R0 if name == "frisch_x1.5" else R0 / 1.5 if name == "frisch_x0.667"
                                             else R0 if name == "frisch" else None),
                       "konvergiert": konv, **info, "diag": d}
            erg.append(eintrag)
            felder.append((f, c, d))

        def wahl(bed):
            idx = [i for i, e in enumerate(erg) if bed(e)]
            return min(idx, key=lambda i: erg[i]["E"]) if idx else None

        # Wahl: zentral = kleinste Energie unter konvergierten kompakten Beuteln am Mittelknoten; alle = unter allen
        # konvergierten Starts. Fortsetzung nur von einer regulaer gewaehlten Loesung.
        if args.wahl == "zentral":
            i = wahl(lambda e: e["konvergiert"] and e["diag"]["kompakt"])
        else:
            i = wahl(lambda e: e["konvergiert"])
        marke = ""
        if i is None:
            i = wahl(lambda e: e["konvergiert"])
            marke = "(kein kompakter Beutel)"
        if i is None:
            i = wahl(lambda e: True)
            marke = "(nicht konvergiert)"
        best = (erg[i]["E"], erg[i]["start"] + marke, felder[i][0], felder[i][1], felder[i][2])
        i_alle = wahl(lambda e: e["konvergiert"])
        punkt = {"k": k, "Q": Q, "angenommen": best[1], "E": best[0], "diag": best[4], "starts": erg,
                 "tiefster_insgesamt": (None if i_alle is None else
                                        {"start": erg[i_alle]["start"], "E": erg[i_alle]["E"],
                                         "kompakt": erg[i_alle]["diag"]["kompakt"],
                                         "dmin": erg[i_alle]["diag"]["dmin"], "nB": erg[i_alle]["diag"]["nB"]})}
        if k in dq:
            fb, cb = best[2], best[3]
            Es = {}
            for s in (+1, -1):
                Qs = Q * (1.0 + s * args.dq_delta)
                f2_, c2_, inf2 = minimiere(G, Qs, fb * math.sqrt(Qs / Q), cb.copy(), args.maxiter, args.gtol)
                Es[s] = inf2
            D = (Es[1]["E"] - Es[-1]["E"]) / (2.0 * args.dq_delta * Q)
            om = best[4]["omega"]
            punkt["dEdQ"] = {"delta": args.dq_delta, "E_plus": Es[1]["E"], "E_minus": Es[-1]["E"], "D": D,
                             "omega": om, "rel": D / om - 1.0,
                             "gmax_plus": max(Es[1]["gmax_f"], Es[1]["gmax_chi"]),
                             "gmax_minus": max(Es[-1]["gmax_f"], Es[-1]["gmax_chi"])}
        if k in prof_k:
            punkt["profil"] = profil(G, best[2], best[3])
        prev = (Q, best[2], best[3]) if marke == "" else None
        del felder
        t_letzt = time.time() - tq
        punkt["sek"] = t_letzt
        out["punkte"].append(punkt)
        out["sek"] = time.time() - T_START
        schreibe(args.aus, out)
        d = best[4]
        print(f"k={k} Q={Q:.6g} E={best[0]:.10g} {best[1]} omega={d['omega']:.5g} p_om={d['p_omega']:.4f} "
              f"nB={d['nB']} Rg={d['Rg']} Reff={d['Reff']:.2f} chi0={d['chi_zentrum']:.3g} kompakt={d['kompakt']} "
              f"starts={[(e['start'], round(e['E'], 6), e['nit'], e['konvergiert']) for e in erg]} "
              f"{t_letzt:.1f} s", flush=True)
    out["sek"] = time.time() - T_START
    out["fertig"] = "abbruch" not in out
    schreibe(args.aus, out)
    print(f"beutel {args.graph} fertig: {len(out['punkte'])} Punkte, {out['sek']:.1f} s", flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("modus", choices=["spektrum", "beutel"])
    p.add_argument("graph")
    p.add_argument("aus")
    p.add_argument("--klein", type=int, default=12)
    p.add_argument("--q0", type=float, default=100.0)
    p.add_argument("--ratio", type=float, default=10 ** 0.125)
    p.add_argument("--k0", type=int, default=0)
    p.add_argument("--k1", type=int, default=0)
    p.add_argument("--ra", type=float, default=1.0)
    p.add_argument("--rb", type=float, default=0.25)
    p.add_argument("--rmin", type=float, default=2.0)
    p.add_argument("--pruef-k", default="")
    p.add_argument("--dq-k", default="")
    p.add_argument("--profil-k", default="")
    p.add_argument("--flach-k", default="", help="flacher Start an diesen k")
    p.add_argument("--dq-delta", type=float, default=1e-3)
    p.add_argument("--flach-immer", action="store_true")
    p.add_argument("--ohne-frisch", action="store_true", help="frischer Start nur am ersten k und an --pruef-k")
    p.add_argument("--wahl", choices=["zentral", "alle"], default="zentral")
    p.add_argument("--maxiter", type=int, default=20000)
    p.add_argument("--gtol", type=float, default=1e-9)
    p.add_argument("--gok", type=float, default=1e-5)
    p.add_argument("--budget", type=float, default=560.0)
    p.add_argument("--periode", type=float, default=0.0, help="MINKOWSKI-DIM-1: Rasterfaktor r = periode^(1/8)")
    args = p.parse_args()
    if args.periode > 0:
        args.ratio = args.periode ** (1.0 / 8.0)
    if args.modus == "spektrum":
        lauf_spektrum(args)
    else:
        lauf_beutel(args)


if __name__ == "__main__":
    main()
