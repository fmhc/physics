#!/usr/bin/env python3
"""TETRA-KOPPLUNG (Runde 17, v3). Code-Agent.
Lineare Elastizitaet von Federgittern: Kopplung E_int zweier eingebetteter Spannungsquellen.
Stufen: pruef | haupt2d | hauptfcc | auswert <haupt2d.json> <hauptfcc.json> | rand
"""
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
import sys
import json
import time
import platform
import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla

EPS = 0.05
SQ3 = np.sqrt(3.0)
AUS = os.path.join(os.getcwd(), "aus")
os.makedirs(AUS, exist_ok=True)
STAMP = time.strftime("%Y%m%d-%H%M%S")
T0 = time.time()

ORIENT = {"M-iso": ((1, 0), (0, 1)), "M-aniso2": ((1, 0), (0, 1)), "M-iso4": ((1, 0), (0, 1)),
          "M-fcc": ((1, 1, 0), (1, -1, 0))}
DIRS = {
    "M-iso": {"0": (1, 0), "19.1": (2, 1), "30": (1, 1), "60": (0, 1), "90": (-1, 2)},
    "M-aniso2": {"0": (1, 0), "26.6": (2, 1), "45": (1, 1), "63.4": (1, 2), "90": (0, 1)},
    "M-iso4": {"0": (1, 0), "26.6": (2, 1), "45": (1, 1), "63.4": (1, 2), "90": (0, 1)},
    "M-fcc": {"[100]": (1, 0, 0), "[110]": (1, 1, 0), "[111]": (1, 1, 1), "[1-10]": (1, -1, 0), "[001]": (0, 0, 1)},
}
PFLICHT = {"M-iso": ["0", "30", "19.1"], "M-aniso2": ["0", "45", "26.6"], "M-iso4": ["0", "45", "26.6"],
           "M-fcc": ["[100]", "[110]", "[111]"]}
R_CHECK = {"M-iso": [(3, 0), (4, 0), (6, 0)], "M-aniso2": [(3, 0), (4, 0), (6, 0)], "M-iso4": [(3, 0), (4, 0), (6, 0)],
           "M-fcc": [(3, 3, 0), (4, 2, 0), (4, 4, 0)]}
WIN2D = {"gesamt": (3.0, 50.0), "fern": (16.0, 50.0)}
HI_FCC = 64 * np.sqrt(2.0) / 4.0
WINFCC = {"gesamt": (3.0, HI_FCC), "fern": (HI_FCC / 3.0, HI_FCC)}


def log(*a):
    print("[%7.1fs]" % (time.time() - T0), *a, flush=True)


def clean(o):
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, np.ndarray):
        return clean(o.tolist())
    if isinstance(o, (bool, np.bool_)):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, (float, np.floating)):
        f = float(o)
        return f if np.isfinite(f) else None
    return o


def jdump(obj, name):
    path = os.path.join(AUS, name)
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(clean(obj), fh, indent=1)
    os.replace(tmp, path)
    log("geschrieben", path)
    return path


# ---------------------------------------------------------------- Medien und Quellen
def medium(name):
    if name == "M-iso":
        A = np.array([[1.0, 0.0], [0.5, SQ3 / 2.0]])
        half = [((1, 0), 1.0), ((0, 1), 1.0), ((-1, 1), 1.0)]
    elif name == "M-aniso2":
        A = np.eye(2)
        half = [((1, 0), 1.0), ((0, 1), 1.0), ((1, 1), 1.0), ((1, -1), 1.0)]
    elif name == "M-iso4":
        A = np.eye(2)
        half = [((1, 0), 1.0), ((0, 1), 1.0), ((1, 1), 0.5), ((1, -1), 0.5)]
    elif name == "M-fcc":
        A = np.eye(3) / np.sqrt(2.0)
        half = [((1, 1, 0), 1.0), ((1, -1, 0), 1.0), ((1, 0, 1), 1.0), ((1, 0, -1), 1.0), ((0, 1, 1), 1.0),
                ((0, 1, -1), 1.0)]
    else:
        raise ValueError(name)
    fcc = name == "M-fcc"
    bonds = []
    for off, k in half:
        off = np.array(off, dtype=np.int64)
        v = off.astype(float) @ A
        L = float(np.linalg.norm(v))
        bonds.append({"off": off, "k": float(k), "L": L, "e": v / L, "v": v})
    A0 = abs(np.linalg.det(A)) * (2.0 if fcc else 1.0)
    return {"name": name, "D": A.shape[0], "A": A, "bonds": bonds, "fcc": fcc, "A0": float(A0)}


def star(med, c):
    out = []
    for j, b in enumerate(med["bonds"]):
        out.append((tuple(int(x) for x in c), j))
        out.append((tuple(int(x) for x in (c - b["off"])), j))
    return out


def source(med, typ, orient=None, origin=None, eps=EPS):
    D = med["D"]
    c0 = np.zeros(D, dtype=np.int64) if origin is None else np.array(origin, dtype=np.int64)
    if typ == "A":
        keys = star(med, c0)
        center = c0.astype(float)
    else:
        o = np.array(orient, dtype=np.int64)
        keys = list(dict.fromkeys(star(med, c0) + star(med, c0 + o)))
        center = c0 + o / 2.0
    return [(n, j, eps * med["bonds"][j]["L"]) for (n, j) in keys], center


def dipole(med, src):
    D = med["D"]
    P = np.zeros((D, D))
    for (n, j, s) in src:
        b = med["bonds"][j]
        P -= b["k"] * s * b["L"] * np.outer(b["e"], b["e"])
    return P


def half_ss(med, src):
    return 0.5 * sum(med["bonds"][j]["k"] * s * s for (n, j, s) in src)


def force_grid(med, src, n):
    D = med["D"]
    f = np.zeros((D,) + (n,) * D)
    for (nd, j, s) in src:
        b = med["bonds"][j]
        p = tuple(int(x) % n for x in nd)
        q = tuple(int(x) % n for x in (np.array(nd, dtype=np.int64) + b["off"]))
        for c in range(D):
            f[(c,) + p] += b["k"] * s * b["e"][c]
            f[(c,) + q] -= b["k"] * s * b["e"][c]
    return f


# ---------------------------------------------------------------- FFT-Loeser (periodisch)
def dyn_inv(med, n):
    D = med["D"]
    shape = (n,) * D
    k1 = 2.0 * np.pi * np.fft.fftfreq(n)
    Dm = np.zeros((D, D) + shape)
    for b in med["bonds"]:
        ph = np.zeros(shape)
        for i in range(D):
            if b["off"][i] != 0:
                sh = [1] * D
                sh[i] = n
                ph = ph + float(b["off"][i]) * k1.reshape(sh)
        w = 2.0 * b["k"] * 2.0 * np.sin(ph / 2.0) ** 2
        for i in range(D):
            for j in range(D):
                Dm[i, j] += w * (b["e"][i] * b["e"][j])
        del ph, w
    zero = [tuple([0] * D)]
    if med["fcc"]:
        zero.append(tuple([n // 2] * D))
    a = Dm
    if D == 2:
        det = a[0, 0] * a[1, 1] - a[0, 1] * a[1, 0]
        for z in zero:
            det[z] = 1.0
        inv = np.empty_like(a)
        inv[0, 0] = a[1, 1] / det
        inv[1, 1] = a[0, 0] / det
        inv[0, 1] = -a[0, 1] / det
        inv[1, 0] = -a[1, 0] / det
    else:
        c00 = a[1, 1] * a[2, 2] - a[1, 2] * a[2, 1]
        c01 = a[1, 2] * a[2, 0] - a[1, 0] * a[2, 2]
        c02 = a[1, 0] * a[2, 1] - a[1, 1] * a[2, 0]
        det = a[0, 0] * c00 + a[0, 1] * c01 + a[0, 2] * c02
        for z in zero:
            det[z] = 1.0
        inv = np.empty_like(a)
        inv[0, 0] = c00 / det
        inv[1, 0] = c01 / det
        inv[2, 0] = c02 / det
        del c00, c01, c02
        inv[0, 1] = (a[0, 2] * a[2, 1] - a[0, 1] * a[2, 2]) / det
        inv[1, 1] = (a[0, 0] * a[2, 2] - a[0, 2] * a[2, 0]) / det
        inv[2, 1] = (a[0, 1] * a[2, 0] - a[0, 0] * a[2, 1]) / det
        inv[0, 2] = (a[0, 1] * a[1, 2] - a[0, 2] * a[1, 1]) / det
        inv[1, 2] = (a[0, 2] * a[1, 0] - a[0, 0] * a[1, 2]) / det
        inv[2, 2] = (a[0, 0] * a[1, 1] - a[0, 1] * a[1, 0]) / det
    zmask = np.zeros(shape, bool)
    for z in zero:
        inv[(slice(None), slice(None)) + z] = 0.0
        zmask[z] = True
    info = {"min_det_ohne_null": float(np.min(det[~zmask])), "max_det": float(np.max(det))}
    del Dm, det
    return inv, info


def fftn_vec(f):
    return np.stack([np.fft.fftn(f[c]) for c in range(f.shape[0])])


def apply_inv(inv, fh):
    D = fh.shape[0]
    uh = np.zeros_like(fh)
    for i in range(D):
        for j in range(D):
            uh[i] += inv[i, j] * fh[j]
    return uh


def emap(uh1, fh2):
    prod = np.zeros(uh1.shape[1:], dtype=complex)
    for c in range(uh1.shape[0]):
        prod += np.conj(fh2[c]) * uh1[c]
    return -np.real(np.fft.ifftn(prod))


def ureal(uh):
    return np.stack([np.real(np.fft.ifftn(uh[c])) for c in range(uh.shape[0])])


# ---------------------------------------------------------------- duenne Matrix (Kontrollen, fester Rand)
def assemble(med, coords, shape, periodic, fixed):
    D = med["D"]
    coords = np.asarray(coords, dtype=np.int64)
    Nn = coords.shape[0]
    shp = np.array(shape, dtype=np.int64)
    look = -np.ones(shape, dtype=np.int64)
    look[tuple(coords.T)] = np.arange(Nn)
    free_id = -np.ones(Nn, dtype=np.int64)
    nf = int((~fixed).sum())
    free_id[~fixed] = np.arange(nf)
    bp, bq, bj = [], [], []
    for j, b in enumerate(med["bonds"]):
        q = coords + b["off"]
        if periodic:
            q = np.mod(q, shp)
            ok = np.ones(Nn, bool)
        else:
            ok = np.all((q >= 0) & (q < shp), axis=1)
        qi = -np.ones(Nn, dtype=np.int64)
        qi[ok] = look[tuple(q[ok].T)]
        ok = qi >= 0
        bp.append(np.nonzero(ok)[0])
        bq.append(qi[ok])
        bj.append(np.full(int(ok.sum()), j, dtype=np.int64))
    bp = np.concatenate(bp)
    bq = np.concatenate(bq)
    bj = np.concatenate(bj)
    Nb = len(bp)
    E = np.array([b["e"] for b in med["bonds"]])[bj]
    kk = np.array([b["k"] for b in med["bonds"]])[bj]
    rows, cols, vals = [], [], []
    ar = np.arange(Nb)
    for node, sg in ((bq, 1.0), (bp, -1.0)):
        fid = free_id[node]
        m = fid >= 0
        for c in range(D):
            rows.append(ar[m])
            cols.append(D * fid[m] + c)
            vals.append(sg * E[m, c])
    B = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(Nb, D * nf))
    K = (B.T @ sp.diags(kk) @ B).tocsc()
    bidx = {(int(p), int(j)): i for i, (p, j) in enumerate(zip(bp, bj))}
    return {"B": B, "K": K, "kk": kk, "look": look, "free_id": free_id, "coords": coords, "bidx": bidx, "D": D,
            "shape": tuple(shape), "periodic": periodic, "nf": nf}


def svec(S, src):
    s = np.zeros(S["B"].shape[0])
    shp = np.array(S["shape"], dtype=np.int64)
    for (n, j, sv) in src:
        p = np.array(n, dtype=np.int64)
        if S["periodic"]:
            p = np.mod(p, shp)
        if np.any(p < 0) or np.any(p >= shp):
            raise ValueError("Quelle ausserhalb")
        pi = int(S["look"][tuple(p)])
        if pi < 0:
            raise ValueError("Knoten fehlt")
        s[S["bidx"][(pi, j)]] += sv
    return s


def sp_solve(S, s, lu):
    f = -(S["B"].T @ (S["kk"] * s))
    u = lu.solve(f)
    delta = S["B"] @ u
    Eb = 0.5 * float(np.sum(S["kk"] * (delta + s) ** 2))
    Ef = 0.5 * float(np.sum(S["kk"] * s ** 2)) - 0.5 * float(f @ u)
    return u, f, Eb, Ef


def u_nodes(S, u):
    U = np.zeros((len(S["coords"]), S["D"]))
    m = S["free_id"] >= 0
    U[m] = u.reshape(-1, S["D"])[S["free_id"][m]]
    return U


def patch(med, R):
    D = med["D"]
    rng = np.arange(-R, R + 1)
    mm = np.stack(np.meshgrid(*([rng] * D), indexing="ij"), -1).reshape(-1, D)
    if med["name"] == "M-iso":
        h = np.max(np.abs(np.stack([mm[:, 0], mm[:, 1], mm[:, 0] + mm[:, 1]], 1)), 1)
    else:
        h = np.max(np.abs(mm), 1)
    keep = h <= R
    if med["fcc"]:
        keep &= (mm.sum(1) % 2 == 0)
    mm = mm[keep]
    h = h[keep]
    return mm + R, h == R, (2 * R + 1,) * D, np.array([R] * D, dtype=np.int64)


# ---------------------------------------------------------------- elastische Konstanten
def dyn_at(med, q):
    D = med["D"]
    M = np.zeros((D, D))
    for b in med["bonds"]:
        M += 2.0 * b["k"] * 2.0 * np.sin(float(q @ b["v"]) / 2.0) ** 2 * np.outer(b["e"], b["e"])
    return M


def elastic_check(med):
    D = med["D"]
    h = 1e-4
    A0 = med["A0"]
    ex = np.zeros(D)
    ex[0] = 1.0
    e45 = np.zeros(D)
    e45[0] = e45[1] = 1.0 / np.sqrt(2.0)
    Mx = dyn_at(med, h * ex) / (A0 * h * h)
    M45 = dyn_at(med, h * e45) / (A0 * h * h)
    C11 = Mx[0, 0]
    C66 = Mx[1, 1]
    C12 = 2.0 * M45[0, 1] - C66
    return {"C11": C11, "C12": C12, "C44_C66": C66, "Anisotropie_A": 2.0 * C66 / (C11 - C12)}


def eshelby(med, P, el):
    D = med["D"]
    p = abs(np.trace(P)) / D
    C11, C12, C66 = el["C11"], el["C12"], el["C44_C66"]
    A0 = med["A0"]
    out = {"p": p}
    if D == 2:
        mu = (C11 - C12 + 2.0 * C66) / 4.0
        Kb = (C11 + C12) / 2.0
        lam = Kb - mu
        for lab, a in (("a=1", 1.0), ("a=WS", np.sqrt(A0 / np.pi))):
            out[lab] = p * p * mu / (2.0 * np.pi * a * a * (lam + mu) * (lam + 2.0 * mu))
    else:
        mu = (C11 - C12 + 3.0 * C66) / 5.0
        Kb = (C11 + 2.0 * C12) / 3.0
        l2m = Kb + 4.0 * mu / 3.0
        for lab, V in (("a=1", 4.0 * np.pi / 3.0), ("a=WS", A0)):
            out[lab] = 2.0 * mu * p * p / (3.0 * Kb * l2m * V)
    out["mu_voigt"] = mu
    out["K_voigt"] = Kb
    return out


# ---------------------------------------------------------------- Stufe pruef
def fixed_four_term(med, R=8):
    coords, fixed, shape, cen = patch(med, R)
    S = assemble(med, coords, shape, False, fixed)
    lu = spla.splu(S["K"])
    out = []
    for typ, o in (("A", None), ("B", ORIENT[med["name"]][0])):
        src1, _ = source(med, typ, o, origin=cen)
        s1 = svec(S, src1)
        u1, f1, E1, _ = sp_solve(S, s1, lu)
        for r in R_CHECK[med["name"]][:2]:
            src2, _ = source(med, typ, o, origin=cen + np.array(r))
            s2 = svec(S, src2)
            u2, f2, E2, _ = sp_solve(S, s2, lu)
            E12 = sp_solve(S, s1 + s2, lu)[2]
            E0 = sp_solve(S, 0.0 * s1, lu)[2]
            out.append({"typ": typ, "r": r, "E_nur1": E1, "E_nur2": E2, "E_beide": E12, "E_keine": E0,
                        "E_int_vier": E12 - E1 - E2 + E0, "E_int_bilinear": float(-f2 @ u1),
                        "E_int_bilinear_umgekehrt": float(-f1 @ u2)})
    return out


def pruef():
    out = {"stamp": STAMP, "versionen": {"python": platform.python_version(), "numpy": np.__version__,
                                         "scipy": scipy.__version__}}
    try:
        import matplotlib
        out["versionen"]["matplotlib"] = matplotlib.__version__
    except Exception as ex:
        out["versionen"]["matplotlib"] = "fehlt: " + str(ex)
    for name in ["M-iso", "M-aniso2", "M-iso4", "M-fcc"]:
        med = medium(name)
        D = med["D"]
        res = {"C5": elastic_check(med), "A0": med["A0"]}
        n = 16 if D == 2 else 12
        shape = (n,) * D
        rng = np.arange(n)
        mm = np.stack(np.meshgrid(*([rng] * D), indexing="ij"), -1).reshape(-1, D)
        if med["fcc"]:
            mm = mm[mm.sum(1) % 2 == 0]
        fixed = np.zeros(len(mm), bool)
        fixed[0] = True
        S = assemble(med, mm, shape, True, fixed)
        lu = spla.splu(S["K"])
        inv, info = dyn_inv(med, n)
        res["dyn_info"] = info
        o1 = ORIENT[name][0]
        for typ, o in (("A", None), ("B", o1)):
            src, cen = source(med, typ, o)
            s1 = svec(S, src)
            u1, f1, Eb, Ef = sp_solve(S, s1, lu)
            U = u_nodes(S, u1)
            U -= U.mean(0)
            fh = fftn_vec(force_grid(med, src, n))
            uh = apply_inv(inv, fh)
            ug = ureal(uh)
            UG = np.stack([ug[c][tuple(mm.T)] for c in range(D)], 1)
            Emap = emap(uh, fh)
            item = {"n_bindungen": len(src), "P": dipole(med, src),
                    "C1_u_maxabw_rel": float(np.max(np.abs(U - UG)) / np.max(np.abs(UG))),
                    "C4_E_bindungssumme": Eb, "C4_E_formel": Ef,
                    "E_self_fft": half_ss(med, src) + 0.5 * float(Emap.flat[0]),
                    "halbe_Summe_k_s2": half_ss(med, src)}
            ft = []
            for r in R_CHECK[name]:
                src2, _ = source(med, typ, o, origin=r)
                s2 = svec(S, src2)
                u2, f2, E2, _ = sp_solve(S, s2, lu)
                E12 = sp_solve(S, s1 + s2, lu)[2]
                E0 = sp_solve(S, 0.0 * s1, lu)[2]
                d = float(np.linalg.norm(np.array(r, float) @ med["A"]))
                ft.append({"r": r, "d": d, "E_nur1": Eb, "E_nur2": E2, "E_keine": E0, "E_beide": E12,
                           "E_int_vier": E12 - Eb - E2 + E0, "E_int_bilinear_sparse": float(-f2 @ u1),
                           "E_int_bilinear_fft": float(Emap[tuple(int(x) % n for x in r)])})
            item["C3"] = ft
            q = {}
            for e_ in (0.025, 0.05, 0.1):
                sa = svec(S, source(med, typ, o, eps=e_)[0])
                sb = svec(S, source(med, typ, o, origin=R_CHECK[name][0], eps=e_)[0])
                Ea = sp_solve(S, sa, lu)[2]
                Eb2 = sp_solve(S, sb, lu)[2]
                Eab = sp_solve(S, sa + sb, lu)[2]
                q[str(e_)] = {"E_self": Ea, "E_int_vier": Eab - Ea - Eb2}
            q["verh_E_self_2eps"] = [q["0.05"]["E_self"] / q["0.025"]["E_self"],
                                     q["0.1"]["E_self"] / q["0.05"]["E_self"]]
            q["verh_E_int_2eps"] = [q["0.05"]["E_int_vier"] / q["0.025"]["E_int_vier"],
                                    q["0.1"]["E_int_vier"] / q["0.05"]["E_int_vier"]]
            item["C2"] = q
            res[typ] = item
            log(name, typ, "C1", item["C1_u_maxabw_rel"], "C3", ft[0]["E_int_vier"], ft[0]["E_int_bilinear_fft"])
        if D == 2:
            res["C3_fester_Rand"] = fixed_four_term(med)
        out[name] = res
    jdump(out, "pruef-%s.json" % STAMP)


# ---------------------------------------------------------------- Strahlen und Auswertung
def n_exact(med, v, delta, dref):
    v = np.array(v, float)
    delta = np.asarray(delta, float)
    step = float(np.linalg.norm(v @ med["A"]))
    cnt = 0
    for t in range(1, int(2.0 * dref / step) + 2):
        c = 0.5 * t * v
        r = c - delta
        if np.all(np.abs(r - np.round(r)) < 1e-9):
            ri = np.round(r).astype(np.int64)
            if med["fcc"] and int(ri.sum()) % 2 != 0:
                continue
            dd = 0.5 * t * step
            if 3.0 <= dd <= dref + 1e-9:
                cnt += 1
    return cnt


def extract_rays(med, emap_arr, n, delta, dirs, dmax, dref):
    D = med["D"]
    A = med["A"]
    sc = float(np.min(np.linalg.svd(A, compute_uv=False)))
    w = min(int(np.ceil(dmax / sc)) + 2, n // 2 - 1)
    rng = np.arange(-w, w + 1)
    mm = np.stack(np.meshgrid(*([rng] * D), indexing="ij"), -1).reshape(-1, D)
    if med["fcc"]:
        mm = mm[mm.sum(1) % 2 == 0]
    c = (mm + np.asarray(delta, float)) @ A
    d = np.linalg.norm(c, axis=1)
    keep = (d >= 2.5) & (d <= dmax + 1e-9)
    mm, c, d = mm[keep], c[keep], d[keep]
    Ev = emap_arr[tuple((mm % n).T)]
    out = {}
    for name, v in dirs.items():
        uu = np.array(v, float) @ A
        uu /= np.linalg.norm(uu)
        along = c @ uu
        perp = np.linalg.norm(c - along[:, None] * uu[None, :], axis=1)
        ex = (perp < 1e-9) & (along > 0)
        # Exaktheit geometrisch entscheiden (gleich fuer alle Groessen): Zahl exakter Punkte in [3, dref]
        approx = n_exact(med, v, delta, dref) < 5
        sel = ((perp <= 0.55) & (along > 0)) if approx else ex
        o = np.argsort(d[sel])
        out[name] = {"m": mm[sel][o], "d": d[sel][o], "perp": perp[sel][o], "E": Ev[sel][o], "approx": bool(approx)}
    return out


def fit_block(d, E, lo, hi):
    res = {"punkte": int(len(d)), "fenster": [lo, hi]}
    if len(d) < 4:
        res.update({"n": None, "grund": "zu wenige sichere Punkte"})
        return res
    sg = np.sign(E)
    if np.all(sg > 0):
        vz = "+"
    elif np.all(sg < 0):
        vz = "-"
    else:
        vz = "wechselnd"
    res["vorzeichen"] = vz
    dd, EE = d, E
    if vz == "wechselnd":
        last = sg[-1]
        k = len(sg) - 1
        while k > 0 and sg[k - 1] == last:
            k -= 1
        res["wechsel_bei_d"] = [float(d[k - 1]), float(d[k])]
        res["schwanz_vorzeichen"] = "+" if last > 0 else "-"
        dd, EE = d[k:], E[k:]
        if len(dd) < 4 or dd[-1] / dd[0] < 2.0:
            res.update({"n": None, "grund": "Vorzeichenwechsel, Schwanz zu kurz"})
            return res
        res["nur_schwanz"] = True
        lo = float(dd[0])
    x = np.log(dd)
    y = np.log(np.abs(EE))
    res["n"] = float(-np.polyfit(x, y, 1)[0])
    mid = np.sqrt(lo * hi)
    lw = dd <= mid
    up = dd >= mid
    res["n_unten"] = float(-np.polyfit(x[lw], y[lw], 1)[0]) if lw.sum() >= 3 else None
    res["n_oben"] = float(-np.polyfit(x[up], y[up], 1)[0]) if up.sum() >= 3 else None
    res["E_bei_dmin"] = [float(dd[0]), float(EE[0])]
    res["E_bei_dmax"] = [float(dd[-1]), float(EE[-1])]
    res["d2E_mittel"] = float(np.mean(EE * dd ** 2))
    res["d3E_mittel"] = float(np.mean(EE * dd ** 3))
    res["d4E_mittel"] = float(np.mean(EE * dd ** 4))
    return res


def analyse(rays_sizes, Ns, b_ana, win):
    N1, N2, N3 = Ns

    def todict(r):
        return {tuple(int(x) for x in m): (float(d), float(e)) for m, d, e in zip(r["m"], r["d"], r["E"])}

    b23, b12 = [], []
    for dn in rays_sizes[0]:
        r1, r2, r3 = (todict(rs[dn]) for rs in rays_sizes)
        for key, (d, e2) in r2.items():
            if 3.0 <= d <= 8.0 and key in r3:
                b23.append((e2 - r3[key][1]) / (1.0 / N2 - 1.0 / N3))
            if 3.0 <= d <= 8.0 and key in r1:
                b12.append((r1[key][1] - e2) / (1.0 / N1 - 1.0 / N2))
    b23 = np.array(b23)
    b12 = np.array(b12)
    b_num = float(np.median(b23))
    spread = float(b23.max() - b23.min())
    if b_ana is not None:
        b_use = b_ana
        unc = abs(b_num - b_ana)
    else:
        b_use = b_num
        unc = spread
    thr = 10.0 * unc / N3 + 1e-16
    dirs_out = {}
    for dn in rays_sizes[0]:
        r2 = todict(rays_sizes[1][dn])
        r3 = rays_sizes[2][dn]
        d3 = np.array(r3["d"], float)
        E3 = np.array(r3["E"], float)
        Einf = E3 - b_use / N3
        comp = []
        for key, (d, e3) in todict(r3).items():
            if key in r2:
                ei3 = e3 - b_use / N3
                ei2 = r2[key][1] - b_use / N2
                comp.append((d, abs(ei2 - ei3) / max(abs(ei3), 1e-300), abs(r2[key][1] - e3) / max(abs(e3), 1e-300)))
        comp.sort()
        gu = None
        gu_roh = None
        ok1 = ok2 = True
        for d, rk, rr in comp:
            ok1 = ok1 and rk < 0.05
            ok2 = ok2 and rr < 0.05
            if ok1:
                gu = d
            if ok2:
                gu_roh = d
        fits = {}
        for wname, (lo, hi) in win.items():
            lo_ = max(lo, 5.0) if r3["approx"] else lo
            sel = (d3 >= lo_ - 1e-9) & (d3 <= hi + 1e-9)
            ok = sel & (np.abs(Einf) > thr)
            fb = fit_block(d3[ok], Einf[ok], lo_, hi)
            fb["unsicher_ausgelassen"] = int(sel.sum() - ok.sum())
            fits[wname] = fb
        dirs_out[dn] = {"approx": r3["approx"], "max_perp": float(np.max(r3["perp"])) if len(d3) else None,
                        "fits": fits, "groessenunabh_bis_d": gu, "groessenunabh_roh_bis_d": gu_roh,
                        "d_vergleich_max": comp[-1][0] if comp else None,
                        "d": d3, "E_inf": Einf, "E_roh_N3": E3}
    return {"b_num": b_num, "b_num_streuung": spread, "b_num_aus_N1N2": float(np.median(b12)) if len(b12) else None,
            "b_ana": b_ana, "b_benutzt": b_use, "schwelle_unsicher": thr, "N": Ns, "richtungen": dirs_out}


def field_data(med, uh, n, w, dref):
    u = ureal(uh)
    D = med["D"]
    rng = np.arange(-w, w + 1)
    g = np.stack(np.meshgrid(rng, rng, indexing="ij"), -1).reshape(-1, 2)
    if D == 2:
        mm = g
    else:
        mm = np.concatenate([g, np.zeros((len(g), 1), np.int64)], 1)
        mm = mm[mm.sum(1) % 2 == 0]
    idx = tuple((mm % n).T)
    U = np.stack([u[c][idx] for c in range(D)], 1)
    X = mm @ med["A"]
    v = np.array(list(DIRS[med["name"]].values())[0], dtype=np.int64)
    if med["fcc"]:
        v = 2 * v
    step = float(np.linalg.norm(v @ med["A"]))
    ts = np.arange(1, int(dref / step) + 1)
    pts = ts[:, None] * v[None, :]
    idx2 = tuple((pts % n).T)
    ua = np.sqrt(sum(u[c][idx2] ** 2 for c in range(D)))
    return X, U, ts * step, ua


def haupt(media, sizes, tag, win, sizefac):
    out = {"stamp": STAMP, "stufe": tag, "eps": EPS, "groessen": sizes}
    npz = {}
    for name in media:
        med = medium(name)
        D = med["D"]
        o1, o2 = ORIENT[name]
        srcA, _ = source(med, "A")
        srcB1, _ = source(med, "B", o1)
        srcB2, _ = source(med, "B", o2)
        deltas = {"AA": np.zeros(D), "BB_par": np.zeros(D), "BB_rot": (np.array(o2, float) - np.array(o1, float)) / 2.0}
        el = elastic_check(med)
        PA = dipole(med, srcA)
        PB = dipole(med, srcB1)
        res = {"P_A": PA, "P_B": PB, "n_bind_A": len(srcA), "n_bind_B": len(srcB1), "A0": med["A0"], "C5": el,
               "groessen": [], "delta_rot": deltas["BB_rot"]}
        rays_all = {k: [] for k in deltas}
        Ns = []
        Lref = sizes[-1] * sizefac / 4.0
        for n in sizes:
            t1 = time.time()
            inv, info = dyn_inv(med, n)
            N = n ** D // (2 if med["fcc"] else 1)
            Ns.append(N)
            dmax = n * sizefac / 4.0
            fh = {"A": fftn_vec(force_grid(med, srcA, n)), "B1": fftn_vec(force_grid(med, srcB1, n)),
                  "B2": fftn_vec(force_grid(med, srcB2, n))}
            uh = {"A": apply_inv(inv, fh["A"]), "B1": apply_inv(inv, fh["B1"])}
            del inv
            maps = {"AA": emap(uh["A"], fh["A"]), "BB_par": emap(uh["B1"], fh["B1"]),
                    "BB_rot": emap(uh["B1"], fh["B2"])}
            EsA = half_ss(med, srcA) + 0.5 * float(maps["AA"].flat[0])
            EsB = half_ss(med, srcB1) + 0.5 * float(maps["BB_par"].flat[0])
            for key in deltas:
                rays_all[key].append(extract_rays(med, maps[key], n, deltas[key], DIRS[name], dmax, Lref))
            g = {"n": n, "N": N, "dmax": dmax, "E_self_A": EsA, "E_self_B": EsB, "dyn_info": info}
            if n == sizes[-1]:
                for typ in ("A", "B1"):
                    X, U, dd, ua = field_data(med, uh[typ], n, 8, dmax)
                    npz["%s_feld%s_X" % (name, typ)] = X
                    npz["%s_feld%s_U" % (name, typ)] = U
                    npz["%s_abfall%s_d" % (name, typ)] = dd
                    npz["%s_abfall%s_u" % (name, typ)] = ua
                if D == 2:
                    for key in maps:
                        npz["%s_%s_map" % (name, key)] = maps[key]
                res["eshelby_A"] = eshelby(med, PA, el)
                res["eshelby_A"]["E_self_gitter"] = EsA
                res["eshelby_A"]["E_self_gitter_durch_halbe_k_s2"] = EsA / half_ss(med, srcA)
            del maps, uh, fh
            g["sek"] = time.time() - t1
            res["groessen"].append(g)
            log(name, "n", n, "E_self_A", EsA, "E_self_B", EsB, "sek", round(g["sek"], 1))
        pA = abs(np.trace(PA)) / D
        res["analyse"] = {}
        for key in deltas:
            b_ana = None
            if key == "AA" and name in ("M-iso", "M-iso4"):
                b_ana = pA * pA / (med["A0"] * el["C11"])
            res["analyse"][key] = analyse(rays_all[key], Ns, b_ana, win)
            for dn, dd in res["analyse"][key]["richtungen"].items():
                f = dd["fits"]["fern"]
                log(name, key, dn, "approx" if dd["approx"] else "exakt", "n_fern", f.get("n"), f.get("n_unten"),
                    f.get("n_oben"), "vz", f.get("vorzeichen"), "gu_bis", dd["groessenunabh_bis_d"])
        res["rays_roh"] = {key: [{dn: {"m": r["m"], "d": r["d"], "E": r["E"]} for dn, r in rs.items()}
                                 for rs in rays_all[key]] for key in rays_all}
        out[name] = res
    jdump(out, "%s-%s.json" % (tag, STAMP))
    np.savez_compressed(os.path.join(AUS, "%s-%s.npz" % (tag, STAMP)), **npz)
    log("npz geschrieben")


# ---------------------------------------------------------------- Auswertung K1-K5 und Bilder
def is_m(fit, m):
    n, lo, hi = fit.get("n"), fit.get("n_unten"), fit.get("n_oben")
    if n is None or lo is None or hi is None:
        return None
    return bool(abs(n - m) <= 0.3 and (m - 0.5 <= lo <= m + 0.5) and (m - 0.5 <= hi <= m + 0.5))


def vz_of(fit):
    v = fit.get("vorzeichen")
    return v if v in ("+", "-") else None


def auswert(f2d, ffcc):
    H2 = json.load(open(f2d))
    HF = json.load(open(ffcc))
    H = {"M-iso": H2["M-iso"], "M-aniso2": H2["M-aniso2"], "M-iso4": H2["M-iso4"], "M-fcc": HF["M-fcc"]}
    K = {}

    def fern(name, key, dn):
        return H[name]["analyse"][key]["richtungen"][dn]["fits"]["fern"]

    # K1
    det = {}
    ok = True
    offen = False
    for dn in PFLICHT["M-iso"]:
        f = fern("M-iso", "AA", dn)
        det[dn] = {"n": f.get("n"), "n_unten": f.get("n_unten"), "n_oben": f.get("n_oben"), "vz": f.get("vorzeichen"),
                   "schwanz_vz": f.get("schwanz_vorzeichen"), "wechsel_bei_d": f.get("wechsel_bei_d"),
                   "1/d^4": is_m(f, 4)}
        if f.get("n") is None or f.get("n_unten") is None or f.get("n_oben") is None:
            offen = True
        elif not (f["n"] >= 2.5 and f["n_unten"] >= 2.2 and f["n_oben"] >= 2.2):
            ok = False
    K["K1"] = {"ausgang": "offen" if offen else ("eingetroffen" if ok else "nicht"), "richtungen": det}
    # K2
    det = {}
    res = []
    for dn in PFLICHT["M-aniso2"]:
        f = fern("M-aniso2", "AA", dn)
        det[dn] = {"n": f.get("n"), "n_unten": f.get("n_unten"), "n_oben": f.get("n_oben"), "vz": f.get("vorzeichen"),
                   "1/d^2": is_m(f, 2)}
    a, dg = det["0"], det["45"]
    if a["1/d^2"] is None or dg["1/d^2"] is None:
        aus = "offen"
    else:
        sw = (a["vz"] in ("+", "-")) and (dg["vz"] in ("+", "-")) and a["vz"] != dg["vz"]
        aus = "eingetroffen" if (a["1/d^2"] and dg["1/d^2"] and sw) else "nicht"
    K["K2"] = {"ausgang": aus, "richtungen": det}
    # K3
    det = {}
    excl = 0
    good = True
    offen = False
    for dn in PFLICHT["M-iso"]:
        f = fern("M-iso", "BB_par", dn)
        det[dn] = {"n": f.get("n"), "n_unten": f.get("n_unten"), "n_oben": f.get("n_oben"), "vz": f.get("vorzeichen"),
                   "1/d^2": is_m(f, 2)}
        if f.get("vorzeichen") == "wechselnd":
            excl += 1
            continue
        if det[dn]["1/d^2"] is None:
            offen = True
        elif not det[dn]["1/d^2"]:
            good = False
    if excl > 1:
        good = False
    vzcmp = {}
    anyopp = False
    for dn in DIRS["M-iso"]:
        vp = vz_of(fern("M-iso", "BB_par", dn))
        vr = vz_of(fern("M-iso", "BB_rot", dn))
        fr = fern("M-iso", "BB_rot", dn)
        vzcmp[dn] = {"parallel": vp, "gedreht": vr, "n_gedreht": fr.get("n"),
                     "gedreht_approx": H["M-iso"]["analyse"]["BB_rot"]["richtungen"][dn]["approx"]}
        if vp and vr and vp != vr:
            anyopp = True
    aus = "offen" if offen else ("eingetroffen" if (good and anyopp) else "nicht")
    K["K3"] = {"ausgang": aus, "parallel": det, "ausgenommen_wechselnd": excl, "vorzeichen_vergleich": vzcmp,
               "mind_eine_richtung_entgegengesetzt": anyopp}
    # K4
    det = {}
    for dn in PFLICHT["M-fcc"]:
        f = fern("M-fcc", "AA", dn)
        det[dn] = {"n": f.get("n"), "n_unten": f.get("n_unten"), "n_oben": f.get("n_oben"), "vz": f.get("vorzeichen"),
                   "1/d^3": is_m(f, 3)}
    if any(det[dn]["1/d^3"] is None for dn in det):
        aus = "offen"
    else:
        sw = vz_of(fern("M-fcc", "AA", "[100]")) and vz_of(fern("M-fcc", "AA", "[111]")) and \
            vz_of(fern("M-fcc", "AA", "[100]")) != vz_of(fern("M-fcc", "AA", "[111]"))
        aus = "eingetroffen" if (all(det[dn]["1/d^3"] for dn in det) and sw) else "nicht"
    K["K4"] = {"ausgang": aus, "richtungen": det}
    # K5
    det = {}
    fr = []
    PA = np.array(H["M-fcc"]["P_A"])
    PB = np.array(H["M-fcc"]["P_B"])
    pa = abs(np.trace(PA)) / 3.0
    pb = abs(np.trace(PB)) / 3.0
    for dn in PFLICHT["M-fcc"]:
        ra = H["M-fcc"]["analyse"]["AA"]["richtungen"][dn]
        rb = H["M-fcc"]["analyse"]["BB_par"]["richtungen"][dn]
        da = {round(d, 6): e for d, e in zip(ra["d"], ra["E_inf"])}
        rows = []
        for d, e in zip(rb["d"], rb["E_inf"]):
            k = round(d, 6)
            if k in da and 3.0 <= d <= HI_FCC + 1e-9:
                rows.append((d, abs(e) / abs(da[k]), abs(e) / abs(da[k]) * (pa * pa) / (pb * pb)))
        frac = float(np.mean([r[1] > 1.0 for r in rows])) if rows else None
        fr.append(frac)
        det[dn] = {"punkte": len(rows), "anteil_verh_gt_1": frac,
                   "verh_min": min(r[1] for r in rows) if rows else None,
                   "verh_max": max(r[1] for r in rows) if rows else None,
                   "verh_normiert_min": min(r[2] for r in rows) if rows else None,
                   "verh_normiert_max": max(r[2] for r in rows) if rows else None,
                   "tabelle": rows}
    if any(x is None for x in fr):
        aus = "offen"
    elif all(x >= 0.9 for x in fr):
        aus = "eingetroffen"
    elif any(x < 0.5 for x in fr):
        aus = "nicht"
    else:
        aus = "offen"
    K["K5"] = {"ausgang": aus, "richtungen": det, "p_A": pa, "p_B": pb}
    out = {"stamp": STAMP, "quellen": [f2d, ffcc], "K": K}
    jdump(out, "auswert-%s.json" % STAMP)
    for k in K:
        log(k, K[k]["ausgang"])
    try:
        bilder(H, f2d, ffcc)
    except Exception as ex:
        log("Bilder fehlgeschlagen:", repr(ex))


def bilder(H, f2d, ffcc):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    Z2 = np.load(f2d.replace(".json", ".npz"))
    ZF = np.load(ffcc.replace(".json", ".npz"))
    titles = {"AA": "Q-A / Q-A", "BB_par": "Q-B / Q-B parallel", "BB_rot": "Q-B / Q-B gedreht"}
    refm = {"M-iso": (2, 4), "M-aniso2": (2, 4), "M-iso4": (2, 4), "M-fcc": (3, 5)}
    for name in ["M-iso", "M-aniso2", "M-iso4", "M-fcc"]:
        R = H[name]
        fig, axs = plt.subplots(1, 3, figsize=(16, 5))
        for ax, key in zip(axs, ["AA", "BB_par", "BB_rot"]):
            an = R["analyse"][key]
            ymax = 0.0
            for i, (dn, dd) in enumerate(an["richtungen"].items()):
                d = np.array(dd["d"], float)
                E = np.array(dd["E_inf"], float)
                col = "C%d" % i
                pos = E > 0
                lab = dn + (" (naeh.)" if dd["approx"] else "")
                ax.plot([], [], "o", color=col, label=lab)
                ax.loglog(d[pos], E[pos], "o", color=col, ms=3.5)
                ax.loglog(d[~pos], -E[~pos], "o", mfc="none", color=col, ms=3.5)
                if len(d):
                    sel = d <= 4.5
                    if sel.any():
                        ymax = max(ymax, float(np.max(np.abs(E[sel]))))
            xs = np.array([3.0, max(max(dd["d"]) for dd in an["richtungen"].values() if len(dd["d"]))])
            for m, ls in zip(refm[name], ("--", ":")):
                ax.loglog(xs, ymax * (xs / 3.0) ** (-m), ls, color="gray", lw=1, label="~ d^-%d" % m)
            ax.set_xlabel("d (Naechstnachbarlaengen)")
            ax.set_ylabel("|E_int|  (gefuellt: E>0 abstossend, offen: E<0 anziehend)")
            ax.set_title("%s: %s" % (name, titles[key]))
            ax.legend(fontsize=7, loc="lower left")
            ax.grid(True, which="both", alpha=0.25)
        fig.tight_layout()
        fn = os.path.join(AUS, "fig-eint-%s-%s.png" % (name, STAMP))
        fig.savefig(fn, dpi=100)
        plt.close(fig)
        log("Bild", fn)
    # Verschiebungsfelder
    fig, axs = plt.subplots(2, 3, figsize=(16, 10))
    panels = [("M-iso", "A", Z2), ("M-iso", "B1", Z2), ("M-aniso2", "A", Z2), ("M-fcc", "A", ZF), ("M-fcc", "B1", ZF)]
    for ax, (name, typ, Z) in zip(axs.flat[:5], panels):
        X = Z["%s_feld%s_X" % (name, typ)]
        U = Z["%s_feld%s_U" % (name, typ)]
        r = np.linalg.norm(X[:, :2], axis=1)
        s = r <= 6.2
        X, U = X[s], U[s]
        mx = float(np.max(np.linalg.norm(U[:, :2], axis=1)))
        ax.quiver(X[:, 0], X[:, 1], U[:, 0], U[:, 1], angles="xy", scale_units="xy", scale=mx / 0.8, width=0.004)
        ax.plot(X[:, 0], X[:, 1], ".", color="gray", ms=2)
        ax.set_aspect("equal")
        lab = "Q-A" if typ == "A" else "Q-B"
        ax.set_title("%s, %s: Verschiebung (max %.4f)%s" % (name, lab, mx, ", Ebene z=0" if name == "M-fcc" else ""))
    ax = axs.flat[5]
    for i, (name, Z) in enumerate((("M-iso", Z2), ("M-aniso2", Z2), ("M-iso4", Z2), ("M-fcc", ZF))):
        d = Z["%s_abfallA_d" % name]
        u = Z["%s_abfallA_u" % name]
        ax.loglog(d, u, "o-", ms=3, label=name + " Q-A (Achse)", color="C%d" % i)
    xs = np.array([1.0, 100.0])
    ax.loglog(xs, 0.02 * xs ** -1.0, "--", color="gray", label="~ d^-1 (2D)")
    ax.loglog(xs, 0.02 * xs ** -2.0, ":", color="gray", label="~ d^-2 (3D)")
    ax.set_xlabel("d")
    ax.set_ylabel("|u|")
    ax.set_title("Abfall der Verschiebung einer Einzelquelle")
    ax.legend(fontsize=8)
    ax.grid(True, which="both", alpha=0.25)
    fig.tight_layout()
    fn = os.path.join(AUS, "fig-feld-%s.png" % STAMP)
    fig.savefig(fn, dpi=100)
    plt.close(fig)
    log("Bild", fn)
    # Winkelabhaengigkeit (2D, groesstes System)
    fig, axs = plt.subplots(2, 3, figsize=(16, 9))
    cases = [("M-iso", "AA", 4), ("M-iso", "BB_par", 2), ("M-iso", "BB_rot", 2), ("M-aniso2", "AA", 2),
             ("M-aniso2", "BB_par", 2), ("M-iso4", "AA", 4)]
    for ax, (name, key, p) in zip(axs.flat, cases):
        med = medium(name)
        an = H[name]["analyse"][key]
        N3 = an["N"][2]
        mp = Z2["%s_%s_map" % (name, key)]
        n = mp.shape[0]
        delta = np.array(H[name]["delta_rot"], float) if key == "BB_rot" else np.zeros(2)
        w = 100
        rng = np.arange(-w, w + 1)
        mm = np.stack(np.meshgrid(rng, rng, indexing="ij"), -1).reshape(-1, 2)
        c = (mm + delta) @ med["A"]
        d = np.linalg.norm(c, axis=1)
        for lo, hi, col in ((10, 20, "C0"), (20, 35, "C1"), (35, 50, "C2")):
            s = (d >= lo) & (d < hi)
            E = mp[tuple((mm[s] % n).T)] - an["b_benutzt"] / N3
            th = np.degrees(np.arctan2(c[s, 1], c[s, 0]))
            ax.plot(th, E * d[s] ** p, ".", ms=1.5, color=col, label="d in [%d,%d)" % (lo, hi))
        ax.axhline(0, color="k", lw=0.6)
        ax.set_xlabel("Winkel theta (Grad)")
        ax.set_ylabel("d^%d E_int" % p)
        ax.set_title("%s, %s" % (name, titles[key]))
        ax.legend(fontsize=7, markerscale=5)
    fig.tight_layout()
    fn = os.path.join(AUS, "fig-winkel-%s.png" % STAMP)
    fig.savefig(fn, dpi=100)
    plt.close(fig)
    log("Bild", fn)


# ---------------------------------------------------------------- fester Rand (optional)
def rand():
    out = {"stamp": STAMP}
    for name in ("M-iso", "M-aniso2"):
        med = medium(name)
        o1 = ORIENT[name][0]
        res = {}
        for R in (50, 100):
            t1 = time.time()
            coords, fixed, shape, cen = patch(med, R)
            S = assemble(med, coords, shape, False, fixed)
            lu = spla.splu(S["K"])
            N = len(coords)
            rr = {}
            for key, typ, o in (("AA", "A", None), ("BB_par", "B", o1)):
                src1, _ = source(med, typ, o, origin=cen)
                u1, f1, E1, _ = sp_solve(S, svec(S, src1), lu)
                rr[key] = {}
                for dn in ("0", list(DIRS[name].keys())[2]):
                    v = np.array(DIRS[name][dn], dtype=np.int64)
                    step = float(np.linalg.norm(v @ med["A"]))
                    lst = []
                    t = 1
                    while t * step <= R / 2.0:
                        if t * step >= 3.0:
                            src2, _ = source(med, typ, o, origin=cen + t * v)
                            s2 = svec(S, src2)
                            f2 = -(S["B"].T @ (S["kk"] * s2))
                            lst.append([t * step, float(-f2 @ u1)])
                        t += 1
                    rr[key][dn] = lst
                rr[key]["E_self_mitte"] = E1
            res[str(R)] = {"N": N, "sek": time.time() - t1, "E": rr}
            log(name, "R", R, "N", N, "sek", round(time.time() - t1, 1))
        out[name] = res
    jdump(out, "rand-%s.json" % STAMP)


if __name__ == "__main__":
    st = sys.argv[1]
    log("Stufe", st, "stamp", STAMP)
    if st == "pruef":
        pruef()
    elif st == "haupt2d":
        haupt(["M-iso", "M-aniso2", "M-iso4"], [100, 200, 400], "haupt2d", WIN2D, 1.0)
    elif st == "hauptfcc":
        mm = [int(x) for x in sys.argv[2:]] if len(sys.argv) > 2 else [16, 32, 64]
        haupt(["M-fcc"], [2 * m for m in mm], "hauptfcc", WINFCC, 1.0 / np.sqrt(2.0))
    elif st == "auswert":
        auswert(sys.argv[2], sys.argv[3])
    elif st == "rand":
        rand()
    log("fertig")
