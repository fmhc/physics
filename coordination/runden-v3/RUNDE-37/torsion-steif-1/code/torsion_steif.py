#!/usr/bin/env python3
# TORSION-STEIF-1 (Runde 45): Hesse-Matrix der 3D-Regge-Wirkung mit Torsion (Yan/Ding/Ma/Zhang, arXiv 2610.00593,
# Gl. 47) um h = 1 auf dem flachen periodischen 3D-Kuhn-Gitter, Bloch-Zerlegung Q(k) (36 x 36) und volle Matrix
# H(k) = [[0, M], [M^+, Q]] (61 x 61) gegen die Eichbahnen; Arm "Linien" (Kegeldefekt); Arm "Rahmenenergie".
# Nur numpy, CPU, 1 Thread. Aufruf auf der .69 nur ueber kleintest.sh:
#   python torsion_steif.py --modus haupt --out haupt.json
#   python torsion_steif.py --modus rauch --out rauch.json   (Rauchtest: druckt nur Laufzeiten und Schluessel)
import argparse
import itertools
import json
import time

import numpy as np

T_START = time.time()
E3 = np.eye(3, dtype=int)
TOL_NULL = 1e-9          # Nullmode: |lambda| <= TOL_NULL * max|lambda| (PLAN 5)
TOL_KONTR = 1e-9         # Kontrollen: relative Residuen (PLAN 6)


def hat(v):
    v = np.asarray(v)
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]], dtype=v.dtype if v.dtype.kind == 'c' else float)


def vee(A):
    return np.array([A[2, 1], A[0, 2], A[1, 0]])


def rodrigues(x):
    th = np.linalg.norm(x)
    K = hat(x)
    if th < 1e-8:
        return np.eye(3) + K + 0.5 * K @ K
    return np.eye(3) + np.sin(th) / th * K + (1 - np.cos(th)) / th ** 2 * K @ K


def rotlog(R):
    c = np.clip((np.trace(R) - 1) / 2, -1.0, 1.0)
    th = np.arccos(c)
    v = 0.5 * vee(R - R.T)
    if th < 1e-6:
        return v * (1 + th ** 2 / 6)
    return v * th / np.sin(th)


# ---------------------------------------------------------------- Gitter (PLAN 2)
PERMS = list(itertools.permutations(range(3)))


def tet_verts(j):
    v = [np.zeros(3, int)]
    for a in PERMS[j]:
        v.append(v[-1] + E3[a])
    return v


TETV = [tet_verts(j) for j in range(6)]
EDGES = [np.array(d) for d in itertools.product((0, 1), repeat=3) if any(d)]
EDGE_INDEX = {tuple(d): i for i, d in enumerate(EDGES)}
TRIS = []
for _a in itertools.product((0, 1), repeat=3):
    for _b in itertools.product((0, 1), repeat=3):
        _A, _B = np.array(_a), np.array(_b)
        if _A.any() and _B.any() and not (_A & _B).any():
            TRIS.append((_A, _B))
TRI_INDEX = {(tuple(a), tuple(b)): i for i, (a, b) in enumerate(TRIS)}
assert len(TRIS) == 12 and len(EDGES) == 7


def canon(verts):
    vs = sorted({tuple(int(c) for c in v) for v in verts}, key=lambda t: (sum(t), t))
    base = np.array(vs[0])
    steps = [np.array(vs[i + 1]) - np.array(vs[i]) for i in range(len(vs) - 1)]
    return base, steps


def tri_id(verts):
    base, (a, b) = canon(verts)
    return TRI_INDEX[(tuple(a), tuple(b))], base


# Tet-Kanten: (Kantentyp, Basisversatz v_alpha, Vektor d)
TET_EDGES = []
for j in range(6):
    lst = []
    for al, be in itertools.combinations(range(4), 2):
        d = TETV[j][be] - TETV[j][al]
        lst.append((EDGE_INDEX[tuple(d)], TETV[j][al].copy(), d))
    TET_EDGES.append(lst)


def gram_basis(edges):
    # d^T G d = s_p fuer die 6 Kanten -> G = sum_p s_p Gamma_p
    A = np.array([[d[0] ** 2, d[1] ** 2, d[2] ** 2, 2 * d[0] * d[1], 2 * d[0] * d[2], 2 * d[1] * d[2]] for d in edges], float)
    Ai = np.linalg.inv(A)
    out = []
    for p in range(len(edges)):
        g = Ai[:, p]
        out.append(np.array([[g[0], g[3], g[4]], [g[3], g[1], g[5]], [g[4], g[5], g[2]]]))
    return out


GAMMA = [gram_basis([e[2] for e in TET_EDGES[j]]) for j in range(6)]

# Dreieck -> zwei Tetraeder (A, B), sortiert; x_tau = Drehvektor von h_{A->B}
TRI_TETS = []
for tau, (a, b) in enumerate(TRIS):
    tv = {tuple(v) for v in (np.zeros(3, int), a, a + b)}
    found = []
    for R in itertools.product((-1, 0, 1), repeat=3):
        for j in range(6):
            if tv <= {tuple(np.array(R) + v) for v in TETV[j]}:
                found.append((j, tuple(R)))
    assert len(found) == 2, (tau, found)
    found.sort(key=lambda t: (t[1], t[0]))
    TRI_TETS.append(found)


def perp_basis(d):
    dh = d / np.linalg.norm(d)
    t = np.array([1.0, 0, 0]) if abs(dh[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = t - dh * (t @ dh)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(dh, e1)
    return dh, e1, e2


# Gelenke (Kanten): Tetraeder im Umlauf (Rechte-Hand-Regel um d), Durchgaenge (tau, Dreiecksbasis, Vorzeichen)
HINGES = []
for e, d in enumerate(EDGES):
    ev = {(0, 0, 0), tuple(int(c) for c in d)}
    tets = []
    for R in itertools.product((-1, 0, 1), repeat=3):
        for j in range(6):
            vs = [tuple(int(c) for c in np.array(R) + v) for v in TETV[j]]
            if ev <= set(vs):
                tets.append((j, tuple(R), [w for w in vs if w not in ev]))
    m = len(tets)
    W = sorted({w for t in tets for w in t[2]})
    assert len(W) == m
    dh, e1, e2 = perp_basis(d.astype(float))
    ang = {w: np.arctan2(np.array(w) @ e2, np.array(w) @ e1) for w in W}
    Ws = sorted(W, key=lambda w: ang[w])
    T = []
    for k in range(m):
        cand = [t for t in tets if set(t[2]) == {Ws[k - 1], Ws[k]}]
        assert len(cand) == 1
        T.append((cand[0][0], cand[0][1]))
    cross = []
    for k in range(m):
        tau, base = tri_id([(0, 0, 0), tuple(int(c) for c in d), Ws[k]])
        A = (TRI_TETS[tau][0][0], tuple(int(c) for c in base + np.array(TRI_TETS[tau][0][1])))
        B = (TRI_TETS[tau][1][0], tuple(int(c) for c in base + np.array(TRI_TETS[tau][1][1])))
        frm, to = T[k], T[(k + 1) % m]
        if (frm, to) == (A, B):
            sig = 1
        elif (frm, to) == (B, A):
            sig = -1
        else:
            raise RuntimeError('Durchgang passt nicht')
        cross.append((tau, tuple(int(c) for c in base), sig))
    HINGES.append(dict(e=e, d=d, m=m, T=T, cross=cross))


def w_avg(dist, m):
    # Paargewicht der Startpunkt-Mittelung (PLAN 1): w(d) = 1 - 2 d / m, d = (b - a) mod m
    return 0.0 if dist == 0 else 1.0 - 2.0 * dist / m


def w_single(a, b, m):
    # Variante E1 (beschreibend): fester Start im Sektor 0 der Winkelordnung
    return 0.0 if a == b else (1.0 if b > a else -1.0)


NG = 25   # Geometrie: 7 x ds_e, 6 x 3 Omega_j
NX = 36   # 12 x 3 Drehvektoren x_tau


def build_terms(variante='mittel'):
    Qt, Mt = [], []   # (row, col, coef, rho)
    for H in HINGES:
        l = H['d'].astype(float)
        L = hat(l)
        m = H['m']
        cr = H['cross']
        for a in range(m):
            for b in range(m):
                if a == b:
                    continue
                if variante == 'mittel':
                    W = w_avg((b - a) % m, m)
                else:
                    W = w_single(a, b, m)
                ta, ba, sa = cr[a]
                tb, bb, sb = cr[b]
                blk = 0.5 * sa * sb * W * L
                rho = np.array(bb) - np.array(ba)
                for r in range(3):
                    for c in range(3):
                        if blk[r, c] != 0:
                            Qt.append((3 * ta + r, 3 * tb + c, blk[r, c], rho))
        for (j, Rt) in H['T']:
            Rt = np.array(Rt)
            for (ta, ba, sa) in cr:
                rho_x = np.array(ba)
                blk = sa / m * L        # Omega_i^T [l] y_a / m
                for r in range(3):
                    for c in range(3):
                        if blk[r, c] != 0:
                            Mt.append((7 + 3 * j + r, 3 * ta + c, blk[r, c], rho_x - Rt))
                for p, (et, va, dv) in enumerate(TET_EDGES[j]):
                    vec = 0.5 / m * sa * (GAMMA[j][p] @ l)
                    for c in range(3):
                        if vec[c] != 0:
                            Mt.append((et, 3 * ta + c, vec[c], rho_x - (Rt + va)))
    return Qt, Mt


def pack(terms):
    rows = np.array([t[0] for t in terms])
    cols = np.array([t[1] for t in terms])
    coef = np.array([t[2] for t in terms])
    rho = np.array([t[3] for t in terms], float)
    return rows, cols, coef, rho


def assemble(packed, shape, k):
    rows, cols, coef, rho = packed
    A = np.zeros(shape, complex)
    np.add.at(A, (rows, cols), coef * np.exp(1j * rho @ k))
    return A


def gauge_vectors(k):
    Z = []
    for j in range(6):
        for c in range(3):
            z = np.zeros(NG + NX, complex)
            z[7 + 3 * j + c] = 1
            for tau in range(12):
                (jA, rA), (jB, rB) = TRI_TETS[tau]
                if jB == j:
                    z[NG + 3 * tau + c] += np.exp(1j * np.array(rB) @ k)
                if jA == j:
                    z[NG + 3 * tau + c] -= np.exp(1j * np.array(rA) @ k)
            Z.append(z)
    for c in range(3):
        z = np.zeros(NG + NX, complex)
        for e, d in enumerate(EDGES):
            z[e] = 2 * d[c] * (np.exp(1j * d @ k) - 1)
        for j in range(6):
            V = TETV[j]
            D = np.array([V[1] - V[0], V[2] - V[0], V[3] - V[0]], float).T
            r = np.array([np.exp(1j * V[b] @ k) - np.exp(1j * V[0] @ k) for b in (1, 2, 3)])
            G = np.outer(E3[c].astype(complex), r @ np.linalg.inv(D))
            z[7 + 3 * j: 10 + 3 * j] = vee(0.5 * (G - G.T))
        Z.append(z)
    return np.array(Z).T     # (61, 21)


def eps_map(j, rho_t, d, k):
    # eps_i d als lineare Abbildung der Geometrievariablen (3 x 25), Tetraeder (j, rho_t) relativ zur Dreiecksbasis
    E = np.zeros((3, NG), complex)
    for p, (et, va, dv) in enumerate(TET_EDGES[j]):
        E[:, et] += 0.5 * (GAMMA[j][p] @ d) * np.exp(1j * (np.array(rho_t) + va) @ k)
    E[:, 7 + 3 * j: 10 + 3 * j] += -hat(d.astype(float)) * np.exp(1j * np.array(rho_t) @ k)
    return E


def torsionfrei_J(k):
    J = np.zeros((NX, NG), complex)
    res = 0.0
    for tau, (a, b) in enumerate(TRIS):
        (jA, rA), (jB, rB) = TRI_TETS[tau]
        d1, d2 = a.astype(float), (a + b).astype(float)
        K = np.vstack([-hat(d1), -hat(d2)])
        r = np.vstack([eps_map(jB, rB, d1, k) - eps_map(jA, rA, d1, k), eps_map(jB, rB, d2, k) - eps_map(jA, rA, d2, k)])
        X, *_ = np.linalg.lstsq(K, r, rcond=None)
        res = max(res, np.linalg.norm(K @ X - r) / max(1.0, np.linalg.norm(r)))
        J[3 * tau: 3 * tau + 3] = X
    return J, res


def counts(ev, scale):
    t = TOL_NULL * scale
    return int(np.sum(ev < -t)), int(np.sum(np.abs(ev) <= t)), int(np.sum(ev > t))


def analyse_k(k, QP, MP, QP1=None, kappas=()):
    Q = assemble(QP, (NX, NX), k)
    M = assemble(MP, (NG, NX), k)
    H = np.zeros((NG + NX, NG + NX), complex)
    H[:NG, NG:] = M
    H[NG:, :NG] = M.conj().T
    H[NG:, NG:] = Q
    out = {}
    out['herm_Q'] = float(np.linalg.norm(Q - Q.conj().T) / np.linalg.norm(Q))
    evQ = np.linalg.eigvalsh(0.5 * (Q + Q.conj().T))
    sQ = float(np.max(np.abs(evQ)))
    out['Q_eig'] = evQ.tolist()
    out['Q_neg_null_pos'] = counts(evQ, sQ)
    out['Q_trace'] = float(np.real(np.trace(Q)))
    evH = np.linalg.eigvalsh(H)
    sH = float(np.max(np.abs(evH)))
    out['H_neg_null_pos'] = counts(evH, sH)
    out['H_absmin'] = np.sort(np.abs(evH))[:26].tolist()
    Z = gauge_vectors(k)
    sv = np.linalg.svd(Z, compute_uv=False)
    out['eich_rang'] = int(np.sum(sv > TOL_NULL * sv[0]))
    out['eich_residuum'] = float(np.linalg.norm(H @ Z) / (np.linalg.norm(H) * np.linalg.norm(Z)))
    out['eich_res_rot'] = float(np.linalg.norm(H @ Z[:, :18]) / (np.linalg.norm(H) * max(1e-300, np.linalg.norm(Z[:, :18]))))
    out['eich_res_trans'] = float(np.linalg.norm(H @ Z[:, 18:]) / (np.linalg.norm(H) * max(1e-300, np.linalg.norm(Z[:, 18:]))))
    J, resJ = torsionfrei_J(k)
    out['J_konsistenz'] = float(resJ)
    out['KX'] = float(np.linalg.norm(M.conj().T + Q @ J) / np.linalg.norm(M))
    R = M @ J
    out['R_herm'] = float(np.linalg.norm(R - R.conj().T) / max(1e-300, np.linalg.norm(R)))
    out['R_gegen_JQJ'] = float(np.linalg.norm(R + J.conj().T @ Q @ J) / max(1e-300, np.linalg.norm(R)))
    evR = np.linalg.eigvalsh(0.5 * (R[:7, :7] + R[:7, :7].conj().T))
    out['Rss_eig'] = evR.tolist()
    out['Rss_neg_null_pos'] = counts(evR, max(1e-300, float(np.max(np.abs(evR)))))
    out['R_omega_norm'] = float(np.linalg.norm(R[7:, :]) / max(1e-300, np.linalg.norm(R)))
    if QP1 is not None:
        Q1 = assemble(QP1, (NX, NX), k)
        ev1 = np.linalg.eigvalsh(0.5 * (Q1 + Q1.conj().T))
        out['Q1_neg_null_pos'] = counts(ev1, float(np.max(np.abs(ev1))))
        out['Q1_absmin'] = float(np.min(np.abs(ev1)))
    if kappas:
        P = Z[NG:, :18]
        rk = {}
        for kap in kappas:
            Qk = Q + 2 * kap * np.eye(NX)
            ev = np.linalg.eigvalsh(0.5 * (Qk + Qk.conj().T))
            Hk = H.copy()
            Hk[NG:, NG:] = Qk
            evHk = np.linalg.eigvalsh(Hk)
            Wf = P.conj().T @ Qk @ P
            Gram = P.conj().T @ P
            evW = np.linalg.eigvalsh(0.5 * (Wf + Wf.conj().T))
            rk[str(kap)] = dict(Q_neg_null_pos=counts(ev, float(np.max(np.abs(ev)))), Q_absmin=float(np.min(np.abs(ev))),
                                H_neg_null_pos=counts(evHk, float(np.max(np.abs(evHk)))),
                                weitz_eig=evW.tolist(), weitz_gram_eig=np.linalg.eigvalsh(0.5 * (Gram + Gram.conj().T)).tolist())
        out['rahmen'] = rk
    return out


# ---------------------------------------------------------------- nichtlineare Kontrolle auf dem Torus (PLAN 6, KN/KG)
def exact_S(g, x, L):
    # g: (L,L,L,25), x: (L,L,L,36) reell. Gl. 47 mit h = exp([sigma x]), Startpunkt-Mittelung, l_B(i) = (1 + eps_i) d_B
    S = 0.0
    for R in itertools.product(range(L), repeat=3):
        R = np.array(R)
        for H in HINGES:
            m = H['m']
            d = H['d'].astype(float)
            hs = []
            for (tau, base, sig) in H['cross']:
                c = tuple((R + np.array(base)) % L)
                hs.append(rodrigues(sig * x[c][3 * tau: 3 * tau + 3]))
            for k0 in range(m):
                P = np.eye(3)
                for step in range(m):
                    P = hs[(k0 + step) % m] @ P
                j, Rt = H['T'][k0]
                ct = (R + np.array(Rt)) % L
                G = np.zeros((3, 3))
                for p, (et, va, dv) in enumerate(TET_EDGES[j]):
                    G += GAMMA[j][p] * g[tuple((ct + va) % L)][et]
                eps = 0.5 * G + hat(g[tuple(ct)][7 + 3 * j: 10 + 3 * j])
                lB = d + eps @ d
                S += lB @ rotlog(P) / m
    return S


def quad_bloch(g, x, L, QP, MP):
    N = L ** 3
    z = np.concatenate([g, x], axis=-1)
    U = np.fft.fftn(z, axes=(0, 1, 2)) / N   # U[n] = (1/N) sum_R e^{-2 pi i n R / L} z(R)
    tot = 0.0
    for n in itertools.product(range(L), repeat=3):
        k = 2 * np.pi * np.array(n) / L
        Q = assemble(QP, (NX, NX), k)
        M = assemble(MP, (NG, NX), k)
        H = np.zeros((NG + NX, NG + NX), complex)
        H[:NG, NG:] = M
        H[NG:, :NG] = M.conj().T
        H[NG:, NG:] = Q
        u = U[n]
        tot += N * np.real(u.conj() @ H @ u)
    return tot


# ---------------------------------------------------------------- Arm "Linien" (PLAN 7)
def cm_embed(sq):
    # sq: 4x4 Matrix der Kantenquadrate -> Koordinaten (Ecke 0 im Ursprung) per Gram + Cholesky
    G = np.array([[0.5 * (sq[0, a] + sq[0, b] - sq[a, b]) for b in (1, 2, 3)] for a in (1, 2, 3)])
    Lc = np.linalg.cholesky(G)
    return np.vstack([np.zeros(3), Lc])


def random_rotation(rng):
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    a, b, c, d = q
    return np.array([[a * a + b * b - c * c - d * d, 2 * (b * c - a * d), 2 * (b * d + a * c)],
                     [2 * (b * c + a * d), a * a - b * b + c * c - d * d, 2 * (c * d - a * b)],
                     [2 * (b * d - a * c), 2 * (c * d + a * b), a * a - b * b - c * c + d * d]])


def linien_arm(e_idx, eta, stoer, seed):
    rng = np.random.default_rng(seed)
    H = HINGES[e_idx]
    d = H['d']
    P0, P1 = (0, 0, 0), tuple(int(c) for c in d)
    verts = {}
    for (j, Rt) in H['T']:
        for v in TETV[j]:
            w = tuple(int(c) for c in np.array(Rt) + v)
            verts[w] = np.array(w, float)
    sq = {}

    def s_of(u, v):
        key = tuple(sorted([u, v]))
        if key not in sq:
            base = float(np.sum((np.array(u) - np.array(v)) ** 2))
            f = 1 + stoer * rng.uniform(-1, 1)
            if set(key) == {P0, P1}:
                f = 1 + eta
            sq[key] = base * f
        return sq[key]

    m = H['m']
    # dritte Ecken der Dreiecke im Umlauf: Durchgang k geht durch (P0, P1, Ws[k]); Tetraeder k enthaelt Ws[k-1], Ws[k]
    Ws = []
    for k in range(m):
        tau, base, sig = H['cross'][k]
        a, b = TRIS[tau]
        tri = [tuple(int(c) for c in base), tuple(int(c) for c in base + a), tuple(int(c) for c in base + a + b)]
        Ws.append([w for w in tri if w not in (P0, P1)][0])
    emb = []
    for k, (j, Rt) in enumerate(H['T']):
        vs = [tuple(int(c) for c in np.array(Rt) + v) for v in TETV[j]]
        order = [P0, P1, Ws[k - 1], Ws[k]]     # positive Orientierung wie die Cholesky-Einbettung
        assert set(order) == set(vs)
        S4 = np.array([[0.0 if a == b else s_of(order[a], order[b]) for b in range(4)] for a in range(4)])
        X = cm_embed(S4)
        Lam = random_rotation(rng)
        emb.append({order[i]: Lam @ X[i] for i in range(4)})
    # Diederwinkel am Gelenk je Tetraeder (eingebettet, eichunabhaengig)
    theta = []
    for k in range(m):
        C = emb[k]
        others = [w for w in C if w not in (P0, P1)]
        a = C[P1] - C[P0]
        a /= np.linalg.norm(a)
        u = [C[w] - C[P0] for w in others]
        u = [x - a * (x @ a) for x in u]
        theta.append(np.arccos(np.clip(u[0] @ u[1] / (np.linalg.norm(u[0]) * np.linalg.norm(u[1])), -1, 1)))
    delta = 2 * np.pi - float(np.sum(theta))
    # torsionsfreie Holonomie (Gl. 28): Drehung, die (d1, d2, d1 x d2) des gemeinsamen Dreiecks von k nach k+1 abbildet
    hs, orth = [], 0.0
    for k in range(m):
        C0, C1 = emb[k], emb[(k + 1) % m]
        w = Ws[k]
        F0 = np.column_stack([C0[P1] - C0[P0], C0[w] - C0[P0], np.cross(C0[P1] - C0[P0], C0[w] - C0[P0])])
        F1 = np.column_stack([C1[P1] - C1[P0], C1[w] - C1[P0], np.cross(C1[P1] - C1[P0], C1[w] - C1[P0])])
        h = F1 @ np.linalg.inv(F0)
        orth = max(orth, float(np.linalg.norm(h.T @ h - np.eye(3))), abs(float(np.linalg.det(h)) - 1))
        hs.append(h)
    P = np.eye(3)
    for k in range(m):
        P = hs[k] @ P
    psi = float(np.arccos(np.clip((np.trace(P) - 1) / 2, -1, 1)))
    lhat = emb[0][P1] - emb[0][P0]
    lhat /= np.linalg.norm(lhat)
    ax = vee(P - P.T)
    s = float(np.sign(ax @ lhat)) if np.linalg.norm(ax) > 1e-14 else 0.0
    achse = float(np.linalg.norm(np.cross(ax / max(1e-300, np.linalg.norm(ax)), lhat))) if np.linalg.norm(ax) > 1e-14 else 0.0
    # Band: Rahmen (Tangente = Linkkante in Tetraeder 0, markierte Seite senkrecht dazu)
    t = emb[0][Ws[0]] - emb[0][Ws[-1]]
    t /= np.linalg.norm(t)
    n = np.cross(lhat, t)
    n /= np.linalg.norm(n)
    F = np.column_stack([t, n, np.cross(t, n)])
    Fend = P @ F
    band = float(np.arccos(np.clip((np.trace(Fend @ F.T) - 1) / 2, -1, 1)))
    return dict(kante=d.tolist(), m=m, eta=eta, stoer=stoer, delta=delta, psi_signed=s * psi, band_drehung=band,
                abw_signed=abs(s * psi - delta), abw_betrag=abs(psi - abs(delta)), achsfehler=achse, orth_fehler=orth)


# ---------------------------------------------------------------- Hauptprogramm
def k_mengen(modus):
    rng = np.random.default_rng(20261005)
    sets = {}
    n = 12 if modus == 'haupt' else 2
    sets['gitter'] = [2 * np.pi * np.array(v) / n for v in itertools.product(range(n), repeat=3)]
    dirs = {'GX': ([0, 0, 0], [1, 0, 0]), 'GM': ([0, 0, 0], [1, 1, 0]), 'GR': ([0, 0, 0], [1, 1, 1]),
            'XM': ([1, 0, 0], [1, 1, 0]), 'MR': ([1, 1, 0], [1, 1, 1]), 'G-allg': ([0, 0, 0], [1, 0.37, 0.61]),
            'G-allg2': ([0, 0, 0], [-0.83, 0.29, 0.47])}
    ns = 241 if modus == 'haupt' else 3
    for name, (s, e) in dirs.items():
        s, e = np.pi * np.array(s, float), np.pi * np.array(e, float)
        sets['linie-' + name] = [s + (e - s) * q for q in np.linspace(0, 1, ns)]
    nr = 500 if modus == 'haupt' else 2
    sets['zufall'] = [rng.uniform(-np.pi, np.pi, 3) for _ in range(nr)]
    sets['klein'] = [q * np.array([1, 0.37, 0.61]) / np.linalg.norm([1, 0.37, 0.61]) for q in (1e-3, 1e-2, 0.05, 0.1, 0.2, 0.4)]
    return sets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--modus', choices=['haupt', 'rauch', 'rauchvoll'], default='rauch')
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    t0 = time.time()
    QP_terms, MP_terms = build_terms('mittel')
    QP, MP = pack(QP_terms), pack(MP_terms)
    QP1 = pack(build_terms('einzel')[0])
    res = dict(karte='TORSION-STEIF-1', modus=args.modus, laufzeit={}, gitter={})
    res['gitter'] = dict(m_je_kante={str(H['d'].tolist()): H['m'] for H in HINGES}, n_Q_terme=len(QP_terms), n_M_terme=len(MP_terms))
    res['laufzeit']['aufbau_s'] = time.time() - t0
    # Arm Linien
    t1 = time.time()
    lin = []
    for e_idx in range(7):
        for eta, stoer, seed in ((0.0, 0.0, 1), (0.05, 0.0, 2), (-0.05, 0.0, 3), (0.05, 0.01, 4), (-0.08, 0.02, 5)):
            lin.append(linien_arm(e_idx, eta, stoer, seed))
    res['linien'] = lin
    res['laufzeit']['linien_s'] = time.time() - t1
    # nichtlineare Kontrolle
    t2 = time.time()
    L = 3
    rng = np.random.default_rng(7)
    kn = []
    nz = 3 if args.modus == 'haupt' else 1
    for i in range(nz):
        g = rng.normal(size=(L, L, L, NG))
        x = rng.normal(size=(L, L, L, NX))
        qb = quad_bloch(g, x, L, QP, MP)
        sec = {}
        for tt in (2e-3, 1e-3):
            sp, sm = exact_S(tt * g, tt * x, L), exact_S(-tt * g, -tt * x, L)
            sec[str(tt)] = dict(zweite=(sp + sm) / tt ** 2, erste=(sp - sm) / (2 * tt))
        rich = (4 * sec['0.001']['zweite'] - sec['0.002']['zweite']) / 3
        kn.append(dict(quad_bloch=qb, zweite_diff=sec, richardson=rich, rel_abw=abs(rich - qb) / abs(qb),
                       grad_rel=abs(sec['0.001']['erste']) / max(1e-300, abs(qb) * 1e-3)))
    res['KN'] = kn
    res['laufzeit']['KN_s'] = time.time() - t2
    # k-Mengen
    t3 = time.time()
    sets = k_mengen(args.modus)
    kappas = (0.0, 0.25, 1.0)
    out = {}
    for name, ks in sets.items():
        lst = []
        for k in ks:
            r = analyse_k(np.array(k, float), QP, MP, QP1=QP1, kappas=kappas if name.startswith('linie-G') or name == 'klein' else ())
            r['k'] = list(map(float, k))
            lst.append(r)
        out[name] = lst
    res['k'] = out
    res['laufzeit']['k_s'] = time.time() - t3
    res['laufzeit']['gesamt_s'] = time.time() - T_START
    if args.modus == 'rauch':
        # Rauchtest vor dem Einfrieren: nur Laufzeiten und Schluessel, keine Werte
        nur = dict(laufzeit=res['laufzeit'], schluessel=sorted(res.keys()), schluessel_k=sorted(out['gitter'][0].keys()),
                   schluessel_linie=sorted(out['linie-GX'][0].keys()), k_mengen={kk: len(v) for kk, v in out.items()},
                   schluessel_linien=sorted(res['linien'][0].keys()), schluessel_KN=sorted(res['KN'][0].keys()))
        with open(args.out, 'w') as f:
            json.dump(nur, f)
        print('rauch: Laufzeiten', json.dumps(res['laufzeit']))
        print('rauch: Schluessel', json.dumps({kk: vv for kk, vv in nur.items() if kk != 'laufzeit'}))
    else:
        # haupt; rauchvoll = kleine k-Mengen mit Werten nur als Eingabe fuer den Rauchtest von auswertung.py (nicht ansehen)
        with open(args.out, 'w') as f:
            json.dump(res, f)
        print('fertig', json.dumps(res['laufzeit']))


if __name__ == '__main__':
    main()
