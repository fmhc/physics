#!/usr/bin/env python3
# DIM-BEUTEL (Runde 16): FLS-artiges Zweifeldmodell (wie BEUTEL-1 M3) auf Graphen, Energie bei fester Ladung Q.
# E = Q^2/(4 Sum phi^2) + phi^T L phi + (1/2) chi^T L chi + Sum[(1/4)(chi^2-1)^2 + 2 chi^2 phi^2], L = D - A.
# Minimierung per L-BFGS-B (phi >= 0), Fortsetzung in Q auf dem Gitter Q_k = r^k, r = (3 sqrt5)^(1/12).
# Siehe PLAN.md.eingefroren-20261002-095901 und PLAN-NACHTRAG-1. Version 2 (10:12): ZEITGRENZE-Punkt wird beim Fortsetzen neu gerechnet.
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_k] = "1"
import sys, json, time, argparse
import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import shortest_path
from scipy.optimize import minimize, Bounds

T0 = time.time()
R_Q = (3.0 * np.sqrt(5.0)) ** (1.0 / 12.0)


def log(msg):
    print(f"[{time.time() - T0:8.1f}s] {msg}", flush=True)


def Qk(k):
    return float(R_Q ** k)


# ----------------------------------------------------------------------------------------------------------------
# Graphen

class Graph:
    pass


def lattice(dims):
    dims = tuple(int(d) for d in dims)
    n = int(np.prod(dims))
    idx = np.arange(n).reshape(dims)
    I, J = [], []
    for ax in range(len(dims)):
        sl_a = [slice(None)] * len(dims)
        sl_b = [slice(None)] * len(dims)
        sl_a[ax] = slice(0, dims[ax] - 1)
        sl_b[ax] = slice(1, dims[ax])
        I.append(idx[tuple(sl_a)].ravel())
        J.append(idx[tuple(sl_b)].ravel())
    G = Graph()
    G.n = n
    G.I = np.concatenate(I)
    G.J = np.concatenate(J)
    G.coords = np.stack(np.unravel_index(np.arange(n), dims), axis=1).astype(float)
    G.dims = dims
    G.dnom = len(dims)
    center = tuple(d // 2 for d in dims)
    G.s = int(np.ravel_multi_index(center, dims))
    # Randbereich: Knoten mit einer Koordinate <= 1 oder >= L-2 (PLAN-NACHTRAG-1)
    c = G.coords
    rand = np.zeros(n, bool)
    for ax in range(len(dims)):
        rand |= (c[:, ax] <= 1) | (c[:, ax] >= dims[ax] - 2)
    G.rand = rand
    # Schnitt durch die Mitte entlang Achse 0
    sl = [slice(None)] + [center[a] for a in range(1, len(dims))]
    G.cut = idx[tuple(sl)].ravel()
    G.name = "x".join(str(d) for d in dims)
    G.kind = "gitter"
    return G


def sierpinski(g, start):
    S = 2 ** g
    a = np.arange(S, dtype=np.int64)
    A_, B_ = np.meshgrid(a, a, indexing="ij")
    m = ((A_ & B_) == 0) & (A_ + B_ < S)
    ta = A_[m]
    tb = B_[m]
    del A_, B_, m
    key = lambda x, y: x * (S + 1) + y
    c0 = key(ta, tb)
    c1 = key(ta + 1, tb)
    c2 = key(ta, tb + 1)
    allk = np.unique(np.concatenate([c0, c1, c2]))
    n = allk.size
    assert n == (3 ** (g + 1) + 3) // 2, (n, (3 ** (g + 1) + 3) // 2)
    i0 = np.searchsorted(allk, c0)
    i1 = np.searchsorted(allk, c1)
    i2 = np.searchsorted(allk, c2)
    G = Graph()
    G.n = n
    G.I = np.concatenate([i0, i1, i2])
    G.J = np.concatenate([i1, i2, i0])
    assert G.I.size == 3 ** (g + 1)
    xa = allk // (S + 1)
    yb = allk % (S + 1)
    G.ab = np.stack([xa, yb], 1)
    G.coords = np.stack([xa + 0.5 * yb, yb * np.sqrt(3.0) / 2.0], 1).astype(float)
    H = 2 ** (g - 2)
    if start == "s1":
        sa, sb = H, H
    elif start == "s2":
        sa, sb = H + 8, 8
    else:
        raise ValueError(start)
    ks = key(np.int64(sa), np.int64(sb))
    j = int(np.searchsorted(allk, ks))
    assert j < n and allk[j] == ks, "Startknoten ist kein Knoten"
    G.s = j
    G.sab = (int(sa), int(sb))
    G.H = H
    G.dnom = 1.5
    G.cut = None
    G.name = f"g{g}-{start}"
    G.kind = "sierpinski"
    G.g = g
    return G


def finish_graph(G):
    n = G.n
    A = sp.coo_matrix((np.ones(G.I.size), (G.I, G.J)), shape=(n, n))
    A = (A + A.T).tocsr()
    A.sum_duplicates()
    assert A.max() == 1.0, "Mehrfachkanten"
    G.A = A
    G.deg = np.asarray(A.sum(axis=1)).ravel()
    G.L = (sp.diags(G.deg) - A).tocsr()
    G.dist = shortest_path(A, unweighted=True, indices=[G.s], directed=False)[0]
    if G.kind == "sierpinski":
        G.rand = G.dist >= G.H  # Ferngebiet: Graphabstand >= H (PLAN 3)
    G.alpha = 1.0 / (G.dnom + 1.0)
    return G


def make_graph(kind, size, start):
    if kind == "kette":
        G = lattice((size,))
    elif kind == "quadrat":
        G = lattice((size, size))
    elif kind == "kubisch":
        G = lattice((size, size, size))
    elif kind == "sierpinski":
        G = sierpinski(size, start)
    else:
        raise ValueError(kind)
    return finish_graph(G)


# ----------------------------------------------------------------------------------------------------------------
# Energie

def energy_grad(G, Q, x):
    n = G.n
    phi = x[:n]
    chi = x[n:]
    Lphi = G.L @ phi
    Lchi = G.L @ chi
    N = float(phi @ phi)
    chi2 = chi * chi
    phi2 = phi * phi
    om = Q / (2.0 * N)
    E = Q * Q / (4.0 * N) + float(phi @ Lphi) + 0.5 * float(chi @ Lchi) \
        + float(np.sum(0.25 * (chi2 - 1.0) ** 2 + 2.0 * chi2 * phi2))
    g = np.empty(2 * n)
    g[:n] = 2.0 * (Lphi + 2.0 * chi2 * phi - om * om * phi)
    g[n:] = Lchi + chi * (chi2 - 1.0) + 4.0 * chi * phi2
    return E, g


def measure(G, Q, x):
    n = G.n
    phi = x[:n]
    chi = x[n:]
    E, g = energy_grad(G, Q, x)
    pg = g.copy()
    act = (phi <= 0.0) & (g[:n] > 0.0)
    pg[:n][act] = 0.0
    N = float(phi @ phi)
    om = Q / (2.0 * N)
    Echi = 0.5 * float(chi @ (G.L @ chi)) + float(np.sum(0.25 * (chi * chi - 1.0) ** 2))
    bag = chi < 0.5
    Vb = int(bag.sum())
    rec = dict(Q=Q, E=E, omega=om, p_loc=om * Q / E, Echi=Echi, h=Echi / E,
               ident=abs(E - om * Q - Echi) / E, gmax=float(np.max(np.abs(pg))),
               chi_s=float(chi[G.s]), chi_min=float(chi.min()), phi_max=float(phi.max()),
               Vbag=Vb, Rgraph=float(G.dist[bag].max()) if Vb else 0.0,
               d_phimax=float(G.dist[int(np.argmax(phi))]),
               rand_phi=float(phi[G.rand].max() / max(phi.max(), 1e-300)),
               rand_chi=float(np.max(np.abs(1.0 - chi[G.rand]))))
    if G.kind == "gitter":
        d = G.dnom
        om_d = {1: 2.0, 2: np.pi, 3: 4.0 * np.pi / 3.0}[d]
        rec["Rvol"] = float((Vb / om_d) ** (1.0 / d))
        if Vb:
            r = np.sqrt(np.sum((G.coords[bag] - G.coords[G.s]) ** 2, axis=1))
            rec["Reuk"] = float(r.max())
        else:
            rec["Reuk"] = 0.0
    return rec


def solve(G, Q, x0, a):
    n = G.n
    phi0 = x0[:n]
    chi0 = x0[n:]
    if a.skal:
        N0 = float(phi0 @ phi0)
        om2 = (Q / (2.0 * N0)) ** 2
        dphi = np.maximum(2.0 * (G.deg + 2.0 * chi0 ** 2 - om2), 0.5)
        dchi = np.maximum(G.deg + 3.0 * chi0 ** 2 - 1.0 + 4.0 * phi0 ** 2, 0.5)
        s = 1.0 / np.sqrt(np.concatenate([dphi, dchi]))
    else:
        s = np.ones(2 * n)

    deadline = T0 + a.tmax
    best = {"E": np.inf, "y": None}

    class Zeit(Exception):
        pass

    def f(y):
        if time.time() > deadline:
            raise Zeit()
        E, gx = energy_grad(G, Q, s * y)
        if E < best["E"]:
            best["E"] = E
            best["y"] = y.copy()
        return E, s * gx

    lb = np.concatenate([np.zeros(n), np.full(n, -np.inf)])
    ub = np.full(2 * n, np.inf)
    y0 = x0 / s
    y0[:n] = np.maximum(y0[:n], 0.0)
    try:
        res = minimize(f, y0, jac=True, method="L-BFGS-B", bounds=Bounds(lb, ub),
                       options=dict(maxiter=a.maxiter, maxfun=2 * a.maxiter, maxcor=a.maxcor,
                                    ftol=1e-15, gtol=a.gtol, maxls=50))
        y = res.x
        nit, nfev, msg = int(res.nit), int(res.nfev), str(res.message)
    except Zeit:
        y = best["y"] if best["y"] is not None else y0
        nit, nfev, msg = -1, -1, "ZEITGRENZE"
    x = s * y
    E, gx = energy_grad(G, Q, x)
    gy = s * gx
    act = (y[:n] <= 0.0) & (gy[:n] > 0.0)
    gy[:n][act] = 0.0
    return x, nit, nfev, msg, float(np.max(np.abs(gy)))


def start_form(G, Q, form):
    n = G.n
    if G.kind == "gitter":
        r = np.sqrt(np.sum((G.coords - G.coords[G.s]) ** 2, axis=1))
    else:
        r = G.dist.copy()
    R0 = Q ** G.alpha if G.kind == "gitter" else Q ** 0.4
    R0 = max(R0, 1.0)
    if form == "A":
        prof = np.clip(1.0 - (r / R0) ** 2, 0.0, None)
        chi = np.where(r < R0, 0.0, 1.0)
    else:
        prof = np.exp(-(r / R0) ** 2)
        prof[prof < 1e-30] = 0.0
        chi = np.ones(n)
    c = np.sqrt(Q * R0 / (2.0 * float(prof @ prof)))
    return np.concatenate([c * prof, chi]), R0


def save_state(path, x, k, fertig=True):
    tmp = path + ".tmp.npz"
    np.savez(tmp, x=x, k=k, fertig=fertig)
    os.replace(tmp, path)


def save_profile(G, outdir, tag, k, x):
    n = G.n
    p = os.path.join(outdir, f"profil-{tag}-k{k:03d}.npz")
    if G.kind == "gitter":
        np.savez_compressed(p, phi=x[:n][G.cut], chi=x[n:][G.cut], pos=G.coords[G.cut, 0] - G.coords[G.s, 0])
    else:
        np.savez_compressed(p, phi=x[:n].astype(np.float32), chi=x[n:].astype(np.float32),
                            dist=G.dist.astype(np.int32))


PROFILE_K = (40, 52, 64, 76, 86)


def run_branch(a):
    G = make_graph(a.graph, a.size, a.start)
    tag = a.tag
    os.makedirs(a.out, exist_ok=True)
    log(f"Graph {a.graph} {G.name}: n={G.n}, Kanten={G.I.size}, s={G.s}, deg(s)={G.deg[G.s]:.0f}, "
        f"Rand/Fern-Knoten={int(G.rand.sum())}, max dist={G.dist.max():.0f}")
    info = dict(graph=a.graph, name=G.name, n=G.n, edges=int(G.I.size), s=G.s, deg_s=float(G.deg[G.s]),
                maxdist=float(G.dist.max()), nrand=int(G.rand.sum()), args=vars(a), r=R_Q)
    if G.kind == "sierpinski":
        info.update(H=G.H, sab=G.sab, g=G.g)
    with open(os.path.join(a.out, f"info-{tag}.json"), "w") as fh:
        json.dump(info, fh, indent=1)
    if a.weiter:
        z = np.load(a.weiter)
        x = z["x"]
        kprev = int(z["k"])
        log(f"weiter aus {a.weiter}, k={kprev}")
        fertig = (bool(z["fertig"]) if "fertig" in z.files else True) and not a.neu
        k = kprev + a.richtung if fertig else kprev
        x = x.copy()
        if fertig:
            x[:G.n] *= R_Q ** (a.richtung * G.alpha)
    else:
        k = a.kstart
        x, R0 = start_form(G, Qk(k), "A")
        log(f"Saat Startform A bei k={k}, Q={Qk(k):.4g}, R0={R0:.3g}")
    fp = open(os.path.join(a.out, f"punkte-{tag}.jsonl"), "a")
    tlast = 0.0
    while True:
        if (a.richtung > 0 and k > a.kende) or (a.richtung < 0 and k < a.kende):
            log("Ziel erreicht")
            break
        el = time.time() - T0
        if el + 1.5 * tlast > a.tmax:
            log(f"Zeitgrenze: {el:.0f}s + 1.5 x {tlast:.0f}s > {a.tmax}s, Abbruch vor k={k}")
            break
        t1 = time.time()
        Q = Qk(k)
        x, nit, nfev, msg, gsk = solve(G, Q, x, a)
        tlast = time.time() - t1
        rec = measure(G, Q, x)
        rec.update(k=k, nit=nit, nfev=nfev, msg=msg, sek=tlast, tag=tag, gskal=gsk)
        fp.write(json.dumps(rec) + "\n")
        fp.flush()
        save_state(os.path.join(a.out, f"zustand-{tag}.npz"), x, k, fertig=(msg != "ZEITGRENZE"))
        if k == a.kstart and not a.weiter:
            save_state(os.path.join(a.out, f"zustand-{tag}-saat.npz"), x, k)
        if k in PROFILE_K:
            save_profile(G, a.out, tag, k, x)
        log(f"k={k:3d} Q={Q:10.4g} E={rec['E']:.10g} p={rec['p_loc']:.5f} h={rec['h']:.5f} "
            f"chi_min={rec['chi_min']:.2e} Vbag={rec['Vbag']} Rg={rec['Rgraph']:.0f} g={rec['gmax']:.1e}/{gsk:.1e} "
            f"id={rec['ident']:.1e} rand={rec['rand_phi']:.1e}/{rec['rand_chi']:.1e} nit={nit} {tlast:.1f}s")
        k += a.richtung
        x = x.copy()
        x[:G.n] *= R_Q ** (a.richtung * G.alpha)
    fp.close()


def run_fresh(a):
    G = make_graph(a.graph, a.size, a.start)
    os.makedirs(a.out, exist_ok=True)
    fp = open(os.path.join(a.out, f"frisch-{a.tag}.jsonl"), "a")
    for k in [int(v) for v in a.klist.split(",")]:
        for form in a.formen.split(","):
            el = time.time() - T0
            if el > a.tmax - 30:
                log("Zeitgrenze, Abbruch")
                fp.close()
                return
            t1 = time.time()
            Q = Qk(k)
            x0, R0 = start_form(G, Q, form)
            x, nit, nfev, msg, gsk = solve(G, Q, x0, a)
            rec = measure(G, Q, x)
            rec.update(k=k, form=form, R0=R0, nit=nit, nfev=nfev, msg=msg, sek=time.time() - t1, tag=a.tag, gskal=gsk)
            fp.write(json.dumps(rec) + "\n")
            fp.flush()
            log(f"frisch {form} k={k} Q={Q:.4g} E={rec['E']:.10g} p={rec['p_loc']:.5f} chi_min={rec['chi_min']:.2e} "
                f"g={rec['gmax']:.1e} nit={nit} {rec['sek']:.1f}s")
    fp.close()


def run_ds(a):
    import scipy.linalg as sla
    os.makedirs(a.out, exist_ok=True)
    out = {}
    for g in [int(v) for v in a.ds_g.split(",") if v]:
        G = make_graph("sierpinski", g, "s1")
        Ld = G.L.toarray()
        t1 = time.time()
        ev = sla.eigvalsh(Ld)
        del Ld
        ev.sort()
        np.save(os.path.join(a.out, f"eigen-g{g}.npy"), ev)
        rows = []
        for j in range(0, 8):
            lam = 0.3 * 5.0 ** (-j)
            N1 = int(np.sum(ev <= lam))
            N0 = int(np.sum(ev <= lam / 5.0))
            rows.append(dict(j=j, lam=lam, N=N1, N_5=N0,
                             ds_half=(np.log(N1 / N0) / np.log(5.0)) if N0 > 0 else None,
                             ds_half_ohne_null=(np.log((N1 - 1) / (N0 - 1)) / np.log(5.0)) if N0 > 1 else None))
        out[f"spektrum_g{g}"] = dict(n=G.n, sek=time.time() - t1, ev_min=float(ev[0]), ev1=float(ev[1]),
                                     ev_max=float(ev[-1]), rows=rows)
        log(f"Spektrum g={g}: n={G.n}, {time.time() - t1:.1f}s, " +
            ", ".join(f"j={r['j']}:{r['ds_half']}" for r in rows))
        with open(os.path.join(a.out, "ds.json"), "w") as fh:
            json.dump(out, fh, indent=1)
    for start in a.walk_starts.split(","):
        if not start:
            continue
        G = make_graph("sierpinski", a.walk_g, start)
        Dinv = 1.0 / G.deg
        p = np.zeros(G.n)
        p[G.s] = 1.0
        tmax = a.walk_tmax
        ret = np.empty(tmax + 1)
        ret[0] = 1.0
        t1 = time.time()
        AT = G.A.tocsr()
        for t in range(1, tmax + 1):
            p = 0.5 * (p + AT @ (Dinv * p))
            ret[t] = p[G.s]
        np.save(os.path.join(a.out, f"rueckkehr-g{a.walk_g}-{start}.npy"), ret)
        rows = []
        j = 0
        while 5 ** (j + 1) <= tmax:
            t0_ = 5 ** j
            rows.append(dict(t=t0_, P=float(ret[t0_]), P5=float(ret[5 * t0_]),
                             ds_half=float(-np.log(ret[5 * t0_] / ret[t0_]) / np.log(5.0))))
            j += 1
        tt = np.arange(25, tmax + 1)
        sl = np.polyfit(np.log(tt), np.log(ret[25:]), 1)[0]
        out[f"irrfahrt_g{a.walk_g}_{start}"] = dict(n=G.n, tmax=tmax, sek=time.time() - t1, rows=rows,
                                                   fit_slope_25_tmax=float(sl), mass=float(p.sum()),
                                                   s=G.s, deg_s=float(G.deg[G.s]))
        log(f"Irrfahrt {start}: " + ", ".join(f"t={r['t']}:{r['ds_half']:.4f}" for r in rows) + f", fit {sl:.4f}")
        with open(os.path.join(a.out, "ds.json"), "w") as fh:
            json.dump(out, fh, indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["ast", "frisch", "ds"])
    ap.add_argument("--graph", default="kette")
    ap.add_argument("--size", type=int, default=4096)
    ap.add_argument("--start", default="s1")
    ap.add_argument("--tag", default="x")
    ap.add_argument("--out", default="aus")
    ap.add_argument("--kstart", type=int, default=40)
    ap.add_argument("--kende", type=int, default=79)
    ap.add_argument("--richtung", type=int, default=1)
    ap.add_argument("--weiter", default="")
    ap.add_argument("--neu", type=int, default=0)
    ap.add_argument("--klist", default="30,50,70")
    ap.add_argument("--formen", default="A,B")
    ap.add_argument("--tmax", type=float, default=540.0)
    ap.add_argument("--gtol", type=float, default=1e-7)
    ap.add_argument("--maxiter", type=int, default=20000)
    ap.add_argument("--maxcor", type=int, default=20)
    ap.add_argument("--skal", type=int, default=1)
    ap.add_argument("--ds-g", dest="ds_g", default="7")
    ap.add_argument("--walk-g", dest="walk_g", type=int, default=10)
    ap.add_argument("--walk-starts", dest="walk_starts", default="s1,s2")
    ap.add_argument("--walk-tmax", dest="walk_tmax", type=int, default=15625)
    a = ap.parse_args()
    log(f"start {a.modus} numpy {np.__version__}")
    if a.modus == "ast":
        run_branch(a)
    elif a.modus == "frisch":
        run_fresh(a)
    else:
        run_ds(a)
    log("fertig")


if __name__ == "__main__":
    main()
