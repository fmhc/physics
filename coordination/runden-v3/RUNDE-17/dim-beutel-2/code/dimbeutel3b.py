#!/usr/bin/env python3
# DIM-BEUTEL-2 (Runde 17): Beutel-Funktional wie DIM-BEUTEL (RUNDE-16/dim-beutel/code/dimbeutel2.py) auf Fraktalen.
# E = Q^2/(4 Sum phi^2) + phi^T L phi + (1/2) chi^T L chi + Sum[(1/4)(chi^2-1)^2 + 2 chi^2 phi^2], L = D - A.
# Neu gegenueber DIM-BEUTEL:
#  - Vicsek-Fraktal (Plus-Fassung) als Baum aus Gitterzellen mit Naechstnachbarkanten.
#  - Frische Starts je Ladungsstufe: Startform A (Kugel R0 um den Mittelpunkt), B- und B+ (R0 / f und R0 * f).
#  - Teilgebiet: Knoten mit Graphabstand <= Rcut vom Mittelpunkt; ausserhalb Vakuum (phi = 0, chi = 1) fest.
#    Pruefung: Randlage (Abstand >= Rcut - 4) muss phi/max <= 1e-10 und |1 - chi| <= 1e-10 haben, sonst Rcut groesser.
#  - dE/dQ = omega je Stufe: Fortsetzung der besten Loesung nach Q e^(+-eps), p_fd = ln(E+/E-)/(2 eps).
#  - d_s des Vicsek-Graphen: Eigenwertzaehlung N(lambda) per Traegheitssatz (Baum-Elimination) und Irrfahrt.
# Plan: ../PLAN.md.eingefroren-*; Version 3b (PLAN-NACHTRAG-4): Formzustaende je Stufe, sonst identisch mit 3.
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_k] = "1"
import json, time, argparse
import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import shortest_path, breadth_first_order
from scipy.optimize import minimize, Bounds

T0 = time.time()
PERIODE = {"sierpinski": 3.0 * np.sqrt(5.0), "vicsek": 5.0 * np.sqrt(15.0)}


def log(msg):
    print(f"[{time.time() - T0:8.1f}s] {msg}", flush=True)


def Qk(frak, k):
    # 12 Indexschritte je selbstaehnlicher Periode
    return float(PERIODE[frak] ** (k / 12.0))


class Obj:
    pass


# ----------------------------------------------------------------------------------------------------------------
# Graphen

def sierpinski(g):
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
    assert n == (3 ** (g + 1) + 3) // 2
    i0 = np.searchsorted(allk, c0)
    i1 = np.searchsorted(allk, c1)
    i2 = np.searchsorted(allk, c2)
    G = Obj()
    G.n = n
    G.I = np.concatenate([i0, i1, i2])
    G.J = np.concatenate([i1, i2, i0])
    assert G.I.size == 3 ** (g + 1)
    xa = allk // (S + 1)
    yb = allk % (S + 1)
    G.coords = np.stack([xa + 0.5 * yb, yb * np.sqrt(3.0) / 2.0], 1).astype(float)
    H = 2 ** (g - 2)
    ks = key(np.int64(H), np.int64(H))  # s1 = (H, H): Mittelpunkt hoher Generation (wie DIM-BEUTEL)
    j = int(np.searchsorted(allk, ks))
    assert allk[j] == ks
    G.s = j
    G.R_self = float(H)   # bis Graphabstand H exakt selbstaehnliche Umgebung (zwei Dreiecke der Seite H)
    G.name = f"sierpinski-g{g}"
    G.frak = "sierpinski"
    G.g = g
    G.baum = False
    return G


def vicsek(g):
    # Plus-Fassung: Zelle (x, y) in [0, 3^g)^2 bleibt, wenn an jeder Ternaerstelle x_d = 1 oder y_d = 1 ist
    # (Mitte und vier Kreuzarme). Knoten = Zellen, Kanten = Naechstnachbarn (4er-Nachbarschaft). Baum mit 5^g Knoten.
    off = np.array([[1, 1], [0, 1], [2, 1], [1, 0], [1, 2]], dtype=np.int64)
    pts = np.zeros((1, 2), dtype=np.int64)
    for t in range(g):
        pts = (pts[None, :, :] + (3 ** t) * off[:, None, :]).reshape(-1, 2)
    S = 3 ** g
    key = pts[:, 0] * S + pts[:, 1]
    o = np.argsort(key)
    key = key[o]
    pts = pts[o]
    n = key.size
    assert n == 5 ** g
    I, J = [], []
    for dx, dy in ((1, 0), (0, 1)):
        x2 = pts[:, 0] + dx
        y2 = pts[:, 1] + dy
        ok = (x2 < S) & (y2 < S)
        nb = x2 * S + y2
        pos = np.minimum(np.searchsorted(key, nb), n - 1)
        hit = ok & (key[pos] == nb)
        I.append(np.nonzero(hit)[0])
        J.append(pos[hit])
    G = Obj()
    G.n = n
    G.I = np.concatenate(I)
    G.J = np.concatenate(J)
    assert G.I.size == n - 1, ("kein Baum", G.I.size, n - 1)
    G.coords = pts.astype(float)
    c = (S - 1) // 2
    j = int(np.searchsorted(key, c * S + c))
    assert key[j] == c * S + c
    G.s = j
    G.R_self = float((S - 1) // 2)  # Graphradius des Ganzen; bis dahin exakt selbstaehnlich um die Mitte
    G.name = f"vicsek-g{g}"
    G.frak = "vicsek"
    G.g = g
    G.baum = True
    return G


def finish_graph(G):
    n = G.n
    A = sp.coo_matrix((np.ones(G.I.size), (G.I, G.J)), shape=(n, n))
    A = (A + A.T).tocsr()
    A.sum_duplicates()
    assert A.max() == 1.0
    G.A = A
    G.deg = np.asarray(A.sum(axis=1)).ravel()
    G.dist = shortest_path(A, unweighted=True, indices=[G.s], directed=False)[0]
    assert np.all(np.isfinite(G.dist)), "nicht zusammenhaengend"
    G.maxdist = float(G.dist.max())
    # Randbereich des ganzen Graphen (nur fuer Rechnungen auf dem vollen Graphen):
    if G.frak == "sierpinski":
        G.rand_full = G.dist >= G.R_self          # wie DIM-BEUTEL (Ferngebiet)
    else:
        G.rand_full = G.dist >= 0.75 * G.R_self   # Gebiet nahe den vier aeusseren Spitzen
    return G


def make_graph(frak, g):
    return finish_graph(sierpinski(g) if frak == "sierpinski" else vicsek(g))


_SUBCACHE = {}


def make_sub(G, Rcut):
    """Teilgebiet dist <= Rcut, ausserhalb Vakuum fest. Rcut <= 0 oder >= maxdist: voller Graph."""
    full = (Rcut <= 0) or (Rcut >= G.maxdist)
    keyc = (id(G), -1.0 if full else float(Rcut))
    if keyc in _SUBCACHE:
        return _SUBCACHE[keyc]
    S = Obj()
    if full:
        idx = np.arange(G.n)
        A = G.A
    else:
        idx = np.nonzero(G.dist <= Rcut)[0]
        A = G.A[idx][:, idx].tocsr()
    S.idx = idx
    S.n = idx.size
    S.A = A
    S.deg = G.deg[idx]
    S.b = S.deg - np.asarray(A.sum(axis=1)).ravel()   # Kanten ins feste Vakuum
    S.sumb = float(S.b.sum())
    S.L = (sp.diags(S.deg) - A).tocsr()
    S.dist = G.dist[idx]
    S.s = int(np.searchsorted(idx, G.s))
    assert idx[S.s] == G.s
    S.full = full
    S.Rcut = G.maxdist if full else float(Rcut)
    S.rand = G.rand_full[idx] if full else (S.dist >= Rcut - 4)
    S.coords = G.coords[idx]
    _SUBCACHE.clear()
    _SUBCACHE[keyc] = S
    return S


# ----------------------------------------------------------------------------------------------------------------
# Energie (wie DIM-BEUTEL, plus Vakuum-Randterm fuer chi auf dem Teilgebiet)

def energy_grad(S, Q, x):
    n = S.n
    phi = x[:n]
    chi = x[n:]
    Lphi = S.L @ phi
    Lchi = S.L @ chi
    N = float(phi @ phi)
    chi2 = chi * chi
    phi2 = phi * phi
    om = Q / (2.0 * N)
    E = Q * Q / (4.0 * N) + float(phi @ Lphi) + 0.5 * (float(chi @ Lchi) - 2.0 * float(S.b @ chi) + S.sumb) \
        + float(np.sum(0.25 * (chi2 - 1.0) ** 2 + 2.0 * chi2 * phi2))
    g = np.empty(2 * n)
    g[:n] = 2.0 * (Lphi + 2.0 * chi2 * phi - om * om * phi)
    g[n:] = Lchi - S.b + chi * (chi2 - 1.0) + 4.0 * chi * phi2
    return E, g


def measure(S, Q, x):
    n = S.n
    phi = x[:n]
    chi = x[n:]
    E, g = energy_grad(S, Q, x)
    pg = g.copy()
    act = (phi <= 0.0) & (g[:n] > 0.0)
    pg[:n][act] = 0.0
    N = float(phi @ phi)
    om = Q / (2.0 * N)
    Echi = 0.5 * (float(chi @ (S.L @ chi)) - 2.0 * float(S.b @ chi) + S.sumb) \
        + float(np.sum(0.25 * (chi * chi - 1.0) ** 2))
    bag = chi < 0.5
    Vb = int(bag.sum())
    mf = bag.astype(float)
    wand = float(mf @ (S.A @ (1.0 - mf)))
    pmax = max(float(phi.max()), 1e-300)
    rec = dict(Q=Q, E=E, omega=om, p_loc=om * Q / E, Echi=Echi, h=Echi / E,
               ident=abs(E - om * Q - Echi) / E, gmax=float(np.max(np.abs(pg))),
               chi_s=float(chi[S.s]), chi_min=float(chi.min()), phi_max=float(phi.max()),
               Vbag=Vb, Rbag=float(S.dist[bag].max()) if Vb else 0.0, wand=wand,
               d_phimax=float(S.dist[int(np.argmax(phi))]),
               rand_phi=float(phi[S.rand].max() / pmax) if S.rand.any() else 0.0,
               rand_chi=float(np.max(np.abs(1.0 - chi[S.rand]))) if S.rand.any() else 0.0,
               nsub=int(S.n), Rcut=float(S.Rcut), voll=bool(S.full))
    return rec


def solve(S, Q, x0, a):
    n = S.n
    phi0 = x0[:n]
    chi0 = x0[n:]
    if a.skal:
        N0 = float(phi0 @ phi0)
        om2 = (Q / (2.0 * N0)) ** 2
        dphi = np.maximum(2.0 * (S.deg + 2.0 * chi0 ** 2 - om2), 0.5)
        dchi = np.maximum(S.deg + 3.0 * chi0 ** 2 - 1.0 + 4.0 * phi0 ** 2, 0.5)
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
        E, gx = energy_grad(S, Q, s * y)
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
    E, gx = energy_grad(S, Q, x)
    gy = s * gx
    act = (y[:n] <= 0.0) & (gy[:n] > 0.0)
    gy[:n][act] = 0.0
    return x, nit, nfev, msg, float(np.max(np.abs(gy)))


def start_x(S, Q, R0):
    """Startform: Kugel vom Graphradius R0 um den Mittelpunkt, innen chi = 0, phi ~ 1 - (r/R0)^2.
    Amplitude aus dem Rayleigh-Quotienten (Minimum von E entlang der Amplitude)."""
    r = S.dist
    prof = np.clip(1.0 - (r / R0) ** 2, 0.0, None)
    chi = np.where(r < R0, 0.0, 1.0)
    pp = float(prof @ prof)
    K = (float(prof @ (S.L @ prof)) + 2.0 * float(np.sum(chi * chi * prof * prof))) / pp
    N = Q / (2.0 * np.sqrt(K))
    return np.concatenate([np.sqrt(N / pp) * prof, chi])


def embed(S_old, x_old, S_new):
    n0, n1 = S_old.n, S_new.n
    phi = np.zeros(n1)
    chi = np.ones(n1)
    pos = np.searchsorted(S_new.idx, S_old.idx)
    assert np.all(S_new.idx[pos] == S_old.idx)
    phi[pos] = x_old[:n0]
    chi[pos] = x_old[n0:]
    return np.concatenate([phi, chi])


def solve_adaptiv(G, Q, Rcut, a, x0fun):
    """Loesen auf dem Teilgebiet; ist die Randlage nicht Vakuum (> 1e-10), Rcut vergroessern und weiterrechnen."""
    S = make_sub(G, Rcut)
    x0 = x0fun(S)
    tsum = 0.0
    nit_sum = 0
    for versuch in range(4):
        t1 = time.time()
        x, nit, nfev, msg, gsk = solve(S, Q, x0, a)
        tsum += time.time() - t1
        nit_sum += max(nit, 0)
        rec = measure(S, Q, x)
        rec.update(nit=nit_sum, nfev=nfev, msg=msg, gskal=gsk, sek=tsum, versuche=versuch + 1)
        if S.full or msg == "ZEITGRENZE" or (rec["rand_phi"] <= 1e-10 and rec["rand_chi"] <= 1e-10):
            return S, x, rec
        Rneu = 1.5 * S.Rcut + 10.0
        log(f"   Randlage nicht Vakuum (phi {rec['rand_phi']:.1e}, chi {rec['rand_chi']:.1e}): Rcut {S.Rcut:.0f} -> {Rneu:.0f}")
        S_old, x_old = S, x
        S = make_sub(G, Rneu)
        x0 = embed(S_old, x_old, S)
    return S, x, rec


def gueltig_konv(rec, a):
    return (rec["msg"] != "ZEITGRENZE") and (rec["gskal"] <= 100.0 * a.gtol) and (rec["ident"] <= 1e-6)


def save_profile(G, S, outdir, tag, k, form, x, rec):
    n = S.n
    R = rec["Rbag"] * 1.5 + 15.0
    m = S.dist <= R
    p = os.path.join(outdir, f"profil-{tag}-k{k:03d}-{form}.npz")
    np.savez_compressed(p, phi=x[:n][m].astype(np.float32), chi=x[n:][m].astype(np.float32),
                        dist=S.dist[m].astype(np.int32), xy=S.coords[m].astype(np.float32))


# ----------------------------------------------------------------------------------------------------------------

def r0_A(frak, Q):
    if frak == "sierpinski":
        return max(Q ** 0.4, 2.0)                       # wie DIM-BEUTEL Z3
    return max(1.2 * Q ** (np.log(3.0) / np.log(PERIODE["vicsek"])), 2.0)   # 1,2 Q^0,3707 (Schreibtisch)


def run_frisch(a):
    G = make_graph(a.frak, a.g)
    os.makedirs(a.out, exist_ok=True)
    tag = a.tag
    info = dict(frak=a.frak, g=a.g, name=G.name, n=G.n, kanten=int(G.A.nnz // 2), s=int(G.s),
                deg_s=float(G.deg[G.s]), maxdist=G.maxdist, R_self=G.R_self, periode_Q=PERIODE[a.frak],
                args=vars(a))
    with open(os.path.join(a.out, f"info-{tag}.json"), "w") as fh:
        json.dump(info, fh, indent=1)
    log(f"Graph {G.name}: n={G.n}, Kanten={G.A.nnz // 2}, deg(s)={G.deg[G.s]:.0f}, maxdist={G.maxdist:.0f}, "
        f"R_self={G.R_self:.0f}")
    pfad = os.path.join(a.out, f"stufen-{tag}.jsonl")
    fertig = set()
    if os.path.exists(pfad):
        with open(pfad) as fh:
            for z in fh:
                r = json.loads(z)
                if r.get("typ") == "stufe":
                    fertig.add(int(r["k"]))
    fp = open(pfad, "a")
    lauf = time.strftime("%Y%m%d-%H%M%S")
    fakt = np.sqrt(2.0) if a.frak == "sierpinski" else np.sqrt(3.0)
    formen = a.formen.split(",")
    tlast = 0.0
    for k in [int(v) for v in a.klist.split(",")]:
        if k in fertig:
            continue
        el = time.time() - T0
        if el + a.wachstum * tlast > a.tmax:
            log(f"Zeit: {el:.0f}s + {a.wachstum} x {tlast:.0f}s > {a.tmax}s, Ende vor k={k}")
            break
        t1 = time.time()
        Q = Qk(a.frak, k)
        RA = r0_A(a.frak, Q)
        R0s = {"A": RA, "Bm": max(RA / fakt, 2.0), "Bp": RA * fakt}
        Rcut0 = 0.0 if a.voll else 1.4 * max(R0s[f] for f in formen) + 25.0
        loes = {}
        abbruch = False
        for form in formen:
            # Version 3b (Nachtrag 4): fertige Formen einer unvollstaendigen Stufe aus dem Formzustand laden.
            zf = os.path.join(a.out, f"formzustand-{tag}-k{k:03d}-{form}.npz")
            if os.path.exists(zf):
                z = np.load(zf, allow_pickle=False)
                rec = json.loads(str(z["rec"]))
                S = make_sub(G, float(z["Rcut_arg"]))
                x = np.array(z["x"])
                assert S.n * 2 == x.size
                rec.update(lauf=lauf, aus_zustand=True)
                fp.write(json.dumps(rec) + "\n")
                fp.flush()
                log(f"k={k} {form} aus Formzustand: E={rec['E']:.10g} konv={rec['konv']}")
                loes[form] = (S, x, rec)
                continue
            S, x, rec = solve_adaptiv(G, Q, Rcut0, a, lambda S_, R0=R0s[form]: start_x(S_, Q, R0))
            rec.update(typ="form", k=k, form=form, R0=R0s[form], tag=tag, lauf=lauf,
                       konv=gueltig_konv(rec, a), aus_zustand=False)
            fp.write(json.dumps(rec) + "\n")
            fp.flush()
            if rec["msg"] != "ZEITGRENZE":
                tmpf = zf + ".tmp.npz"
                np.savez(tmpf, x=x, Rcut_arg=np.float64(0.0 if S.full else S.Rcut), rec=json.dumps(rec))
                os.replace(tmpf, zf)
            log(f"k={k} {form} Q={Q:.4g} R0={R0s[form]:.1f} E={rec['E']:.10g} p={rec['p_loc']:.5f} "
                f"V={rec['Vbag']} Rb={rec['Rbag']:.0f} wand={rec['wand']:.0f} g={rec['gskal']:.1e} id={rec['ident']:.1e} "
                f"rand={rec['rand_phi']:.0e}/{rec['rand_chi']:.0e} nsub={rec['nsub']} nit={rec['nit']} {rec['sek']:.1f}s")
            if rec["msg"] == "ZEITGRENZE":
                abbruch = True
                break
            loes[form] = (S, x, rec)
        if abbruch:
            log(f"ZEITGRENZE in Stufe k={k}; Stufe unvollstaendig, naechster Aufruf rechnet sie neu")
            break
        konv = [f for f in loes if loes[f][2]["konv"]]
        kand = konv if konv else list(loes)
        bestf = min(kand, key=lambda f: loes[f][2]["E"])
        S, x, rb = loes[bestf]
        st = dict(typ="stufe", k=k, Q=Q, beste=bestf, beste_konv=bool(konv), tag=tag, lauf=lauf,
                  E={f: loes[f][2]["E"] for f in loes}, konv={f: loes[f][2]["konv"] for f in loes})
        for key_ in ("E", "omega", "p_loc", "h", "ident", "gskal", "chi_min", "Vbag", "Rbag", "wand", "rand_phi",
                     "rand_chi", "nsub", "Rcut", "voll"):
            st["b_" + key_] = rb[key_]
        save_profile(G, S, a.out, tag, k, bestf, x, rb)
        if a.pm:
            eps = a.eps
            pm = {}
            for sg in (-1, 1):
                Q2 = Q * np.exp(sg * eps)
                x0 = x.copy()
                x0[:S.n] *= np.exp(0.5 * sg * eps)
                x2, nit, nfev, msg, gsk = solve(S, Q2, x0, a)
                r2 = measure(S, Q2, x2)
                r2.update(nit=nit, msg=msg, gskal=gsk)
                pm[sg] = r2
                if msg == "ZEITGRENZE":
                    break
            if len(pm) == 2 and all(pm[s_]["msg"] != "ZEITGRENZE" for s_ in pm):
                Em, Ep = pm[-1]["E"], pm[1]["E"]
                p_fd = np.log(Ep / Em) / (2.0 * eps)
                dEdQ = (Ep - Em) / (pm[1]["Q"] - pm[-1]["Q"])
                st.update(pm_eps=eps, E_m=Em, E_p=Ep, p_fd=float(p_fd), dEdQ=float(dEdQ),
                          dEdQ_rel=float(dEdQ / rb["omega"] - 1.0), dp_fd=float(p_fd - rb["p_loc"]),
                          pm_konv=bool(all(gueltig_konv(pm[s_], a) for s_ in pm)),
                          pm_Vbag=[pm[-1]["Vbag"], pm[1]["Vbag"]], pm_nit=[pm[-1]["nit"], pm[1]["nit"]])
            else:
                log(f"ZEITGRENZE in der +-Fortsetzung bei k={k}; Stufe unvollstaendig")
                break
        st["sek"] = time.time() - t1
        fp.write(json.dumps(st) + "\n")
        fp.flush()
        tlast = st["sek"]
        log(f"STUFE k={k} Q={Q:.4g} beste={bestf} E={rb['E']:.10g} p_loc={rb['p_loc']:.5f} "
            f"p_fd={st.get('p_fd', float('nan')):.5f} Rbag={rb['Rbag']:.0f} V={rb['Vbag']} {tlast:.1f}s")
    fp.close()


# ----------------------------------------------------------------------------------------------------------------
# d_s des Vicsek-Graphen

def baum_zaehlung(G, lams):
    """N(lambda) = Zahl der Eigenwerte von L = D - A unter lambda, per Traegheitssatz (Sylvester):
    Gauss-Elimination von den Blaettern zur Wurzel ohne Auffuellung; Zahl der negativen Pivots."""
    order, pred = breadth_first_order(G.A, G.s, directed=False, return_predecessors=True)
    depth = G.dist[order].astype(np.int64)
    gruppen = []
    grenzen = np.searchsorted(depth, np.arange(depth.max() + 2))
    for d in range(depth.max() + 1):
        gruppen.append(order[grenzen[d]:grenzen[d + 1]])
    out = []
    for lam in lams:
        Ssum = np.zeros(G.n)
        piv = np.empty(G.n)
        for d in range(len(gruppen) - 1, -1, -1):
            nd = gruppen[d]
            pv = G.deg[nd] - lam - Ssum[nd]
            piv[nd] = pv
            if d > 0:
                np.add.at(Ssum, pred[nd], 1.0 / pv)
        out.append(int(np.sum(piv < 0.0)))
    return out


def run_ds(a):
    os.makedirs(a.out, exist_ok=True)
    out = {"soll_ds": 2.0 * np.log(5.0) / np.log(15.0)}
    pfad = os.path.join(a.out, "ds-vicsek.json")
    for g in [int(v) for v in a.ds_g.split(",") if v]:
        G = make_graph("vicsek", g)
        t1 = time.time()
        # Kontrolle der Zaehlung gegen dichte Eigenwerte (nur kleine g)
        kontr = None
        if G.n <= 3200:
            ev = np.linalg.eigvalsh(G.A.toarray() * -1.0 + np.diag(G.deg))
            lt = [0.003, 0.03, 0.3, 1.1, 2.5]
            kontr = dict(lams=lt, dicht=[int(np.sum(ev < l)) for l in lt], baum=baum_zaehlung(G, lt))
        lams = 8.0 * 15.0 ** (-np.arange(0, 8 * 8 + 1) / 8.0)   # 8 Punkte je Spektralperiode (Faktor 15)
        N = baum_zaehlung(G, lams)
        rows = []
        for i in range(len(lams) - 8):
            if N[i + 8] > 0:
                rows.append(dict(lam=float(lams[i]), N=N[i], N15=N[i + 8],
                                 ds_half=float(np.log(N[i] / N[i + 8]) / np.log(15.0))))
        out[f"zaehlung_g{g}"] = dict(n=G.n, sek=time.time() - t1, lams=[float(v) for v in lams], N=N, rows=rows,
                                     kontrolle_dicht=kontr)
        log(f"Zaehlung g={g}: n={G.n}, {time.time() - t1:.1f}s; " +
            ", ".join(f"{r['lam']:.2e}:{r['ds_half']:.4f}" for r in rows[::4]))
        with open(pfad, "w") as fh:
            json.dump(out, fh, indent=1)
    for g in [int(v) for v in a.walk_g.split(",") if v]:
        G = make_graph("vicsek", g)
        Dinv = 1.0 / G.deg
        p = np.zeros(G.n)
        p[G.s] = 1.0
        tmax = a.walk_tmax
        ret = np.empty(tmax + 1)
        ret[0] = 1.0
        t1 = time.time()
        A = G.A.tocsr()
        for t in range(1, tmax + 1):
            p = 0.5 * (p + A @ (Dinv * p))
            ret[t] = p[G.s]
        np.save(os.path.join(a.out, f"rueckkehr-vicsek-g{g}.npy"), ret)
        rows = []
        t0_ = 1
        while 15 * t0_ <= tmax:
            rows.append(dict(t=t0_, P=float(ret[t0_]), P15=float(ret[15 * t0_]),
                             ds_half=float(-np.log(ret[15 * t0_] / ret[t0_]) / np.log(15.0))))
            t0_ *= 15
        tt = np.arange(225, tmax + 1)
        sl = np.polyfit(np.log(tt), np.log(ret[225:]), 1)[0]
        out[f"irrfahrt_g{g}"] = dict(n=G.n, tmax=tmax, sek=time.time() - t1, rows=rows, fit_slope_225_tmax=float(sl),
                                     masse=float(p.sum()))
        log(f"Irrfahrt g={g}: " + ", ".join(f"t={r['t']}:{r['ds_half']:.4f}" for r in rows) + f", fit {sl:.4f}, "
            f"{time.time() - t1:.1f}s")
        with open(pfad, "w") as fh:
            json.dump(out, fh, indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["frisch", "ds"])
    ap.add_argument("--frak", default="sierpinski", choices=["sierpinski", "vicsek"])
    ap.add_argument("--g", type=int, default=10)
    ap.add_argument("--tag", default="x")
    ap.add_argument("--out", default="aus")
    ap.add_argument("--klist", default="46")
    ap.add_argument("--formen", default="A,Bm,Bp")
    ap.add_argument("--voll", type=int, default=0)
    ap.add_argument("--pm", type=int, default=1)
    ap.add_argument("--eps", type=float, default=0.01)
    ap.add_argument("--wachstum", type=float, default=2.0)
    ap.add_argument("--tmax", type=float, default=540.0)
    ap.add_argument("--gtol", type=float, default=1e-7)
    ap.add_argument("--maxiter", type=int, default=30000)
    ap.add_argument("--maxcor", type=int, default=20)
    ap.add_argument("--skal", type=int, default=1)
    ap.add_argument("--ds-g", dest="ds_g", default="5,7,8")
    ap.add_argument("--walk-g", dest="walk_g", default="7")
    ap.add_argument("--walk-tmax", dest="walk_tmax", type=int, default=50625)
    a = ap.parse_args()
    log(f"start {a.modus} numpy {np.__version__}")
    if a.modus == "frisch":
        run_frisch(a)
    else:
        run_ds(a)
    log("fertig")


if __name__ == "__main__":
    main()
