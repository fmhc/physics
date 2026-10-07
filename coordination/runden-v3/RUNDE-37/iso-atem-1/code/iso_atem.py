#!/usr/bin/env python3
# ISO-ATEM-1 (Runde 42), Code-Agent fuer claude-primary.
# Starre regulaere Tetraeder (Kante 1 PU), eckenteilend in Finns Topologie (ideales beta-Cristobalit:
# Mitten = Diamant, Ecken = Pyrochlor), Kugelgelenke, periodische kubische Zelle mit 8 Tetraedern (16 Ecken).
# Modi: kontrolle (K0, Teil A, Gamma-Ansatz), ast (Teil B, P2_13), zufall (Teil C), auswertung, bild.
# Laeuft nur auf der .69 ueber kleintest.sh (1 Thread).
import argparse, json, sys, os, time, hashlib, platform
import numpy as np

S = np.sqrt(3.0 / 8.0)                 # Umkugelradius bei Kante 1
A0 = 2.0 * np.sqrt(2.0)                # ideale kubische Zellkante
D = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float) / np.sqrt(3.0)
FCC = np.array([[0, 0, 0], [0, .5, .5], [.5, 0, .5], [.5, .5, 0]], float)
C0 = np.vstack([FCC * A0, (FCC + .25) * A0])          # 0..3 = A (oben), 4..7 = B (unten)
TYP = np.array([0] * 4 + [1] * 4)
T_OFF = np.stack([S * D if t == 0 else -S * D for t in TYP])   # (8,4,3)
NV = np.ones(3) / np.sqrt(3.0)
I3 = np.eye(3)

# P2_13, International Tables Nr. 198 (Bruchteile der Zelle)
OPS = [
    ((1, 0, 0, 0, 1, 0, 0, 0, 1), (0, 0, 0)),
    ((-1, 0, 0, 0, -1, 0, 0, 0, 1), (.5, 0, .5)),
    ((-1, 0, 0, 0, 1, 0, 0, 0, -1), (0, .5, .5)),
    ((1, 0, 0, 0, -1, 0, 0, 0, -1), (.5, .5, 0)),
    ((0, 0, 1, 1, 0, 0, 0, 1, 0), (0, 0, 0)),
    ((0, 0, 1, -1, 0, 0, 0, -1, 0), (.5, .5, 0)),
    ((0, 0, -1, -1, 0, 0, 0, 1, 0), (.5, 0, .5)),
    ((0, 0, -1, 1, 0, 0, 0, -1, 0), (0, .5, .5)),
    ((0, 1, 0, 0, 0, 1, 1, 0, 0), (0, 0, 0)),
    ((0, -1, 0, 0, 0, 1, -1, 0, 0), (0, .5, .5)),
    ((0, 1, 0, 0, 0, -1, -1, 0, 0), (.5, .5, 0)),
    ((0, -1, 0, 0, 0, -1, 1, 0, 0), (.5, 0, .5)),
]
OPQ = [np.array(q, float).reshape(3, 3) for q, _ in OPS]
OPT = [np.array(t, float) for _, t in OPS]


def alle_O24():
    out = []
    import itertools
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3))
            for i in range(3):
                M[i, perm[i]] = sg[i]
            if np.linalg.det(M) > 0:
                out.append(M)
    return out


O24 = alle_O24()


def skew(v):
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def rodrigues(w):
    th = np.linalg.norm(w)
    K = skew(w)
    if th < 1e-8:
        a, b = 1 - th ** 2 / 6, 0.5 - th ** 2 / 24
    else:
        a, b = np.sin(th) / th, (1 - np.cos(th)) / th ** 2
    return I3 + a * K + b * (K @ K)


def rot_axis(n, phi):
    n = np.asarray(n, float)
    return rodrigues(n / np.linalg.norm(n) * phi)


def drehwinkel_achse(R):
    c = np.clip((np.trace(R) - 1) / 2, -1, 1)
    th = np.arccos(c)
    v = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]])
    nv = np.linalg.norm(v)
    if nv < 1e-12:
        if th < 1e-6:
            return 0.0, np.array([0., 0., 1.])
        w, U = np.linalg.eigh((R + R.T) / 2)
        return float(th), U[:, np.argmax(w)]
    return float(th), v / nv


# ---------------- Topologie aus der Ideallage ----------------
def topologie():
    P = C0[:, None, :] + T_OFF
    paare = []
    for j in range(4):
        for k in range(4):
            gef = []
            for jp in range(4, 8):
                for kp in range(4):
                    d = (P[j, k] - P[jp, kp]) / A0
                    n = np.round(d)
                    if np.max(np.abs(d - n)) < 1e-9:
                        gef.append((j, k, jp, kp, n.astype(int)))
            assert len(gef) == 1, (j, k, len(gef))
            paare.append(gef[0])
    bv = sorted((p[2], p[3]) for p in paare)
    assert len(set(bv)) == 16
    return paare


PAARE = topologie()
PJ = np.array([p[0] for p in PAARE]); PK = np.array([p[1] for p in PAARE])
PJ2 = np.array([p[2] for p in PAARE]); PK2 = np.array([p[3] for p in PAARE])
PN = np.array([p[4] for p in PAARE], float)
TOP = {(p[0], p[2], tuple(int(x) for x in p[4])): (p[1], p[3]) for p in PAARE}


def rest(c, R, F):
    v1 = c[PJ] + np.einsum('pab,pb->pa', R[PJ], T_OFF[PJ, PK])
    v2 = c[PJ2] + np.einsum('pab,pb->pa', R[PJ2], T_OFF[PJ2, PK2]) + A0 * (PN @ F.T)
    return v1 - v2


def rmax(D_):
    return float(np.max(np.linalg.norm(D_, axis=1)))


def rrms(D_):
    return float(np.sqrt(np.mean(np.sum(D_ ** 2, axis=1))))


# ---------------- P2_13-Bau (Teil B) ----------------
def zuordnung():
    out = []
    for j in range(8):
        ref = C0[0] if j < 4 else C0[4]
        gef = None
        for oi in range(12):
            x = OPQ[oi] @ ref + OPT[oi] * A0
            d = (C0[j] - x) / A0
            m = np.round(d)
            if np.max(np.abs(d - m)) < 1e-9:
                gef = (oi, m)
                break
        assert gef is not None
        out.append(gef)
    return out


ZUORD = zuordnung()


def baue_p213(y):
    phiA, phiB, uA, uB, lam = y
    a = lam * A0
    cA1, cB1 = uA * NV, uB * NV
    RA1, RB1 = rot_axis(NV, phiA), rot_axis(NV, phiB)
    c = np.zeros((8, 3)); R = np.zeros((8, 3, 3))
    for j in range(8):
        oi, m = ZUORD[j]
        Q, t = OPQ[oi], OPT[oi]
        if j < 4:
            c[j] = Q @ cA1 + (t + m) * a; R[j] = Q @ RA1 @ Q.T
        else:
            c[j] = Q @ cB1 + (t + m) * a; R[j] = Q @ RB1 @ Q.T
    return c, R


def G_ast(y):
    c, R = baue_p213(y)
    return rest(c, R, y[4] * I3).ravel()


def jac_fd(fun, y, h=1e-6):
    f0 = fun(y)
    J = np.zeros((f0.size, y.size))
    for i in range(y.size):
        e = np.zeros(y.size); e[i] = h
        J[:, i] = (fun(y + e) - fun(y - e)) / (2 * h)
    return J


Y0 = np.array([0.0, 0.0, 0.0, 2 * S, 1.0])


# ---------------- Geometrie: Winkel, Beruehrung, O-O ----------------
def ecken(c, R):
    return c[:, None, :] + np.einsum('jab,jkb->jka', R, T_OFF)


def achsen_tetra(Vj):
    fn = []
    for f in range(4):
        idx = [i for i in range(4) if i != f]
        n = np.cross(Vj[idx[1]] - Vj[idx[0]], Vj[idx[2]] - Vj[idx[0]])
        fn.append(n / np.linalg.norm(n))
    ed = []
    for a in range(4):
        for b in range(a + 1, 4):
            e = Vj[b] - Vj[a]
            ed.append(e / np.linalg.norm(e))
    return np.array(fn), np.array(ed)


def sat_gap(P, Q, fnP, edP, fnQ, edQ):
    cr = np.cross(edP[:, None, :], edQ[None, :, :]).reshape(-1, 3)
    nc = np.linalg.norm(cr, axis=1)
    cr = cr[nc > 1e-9] / nc[nc > 1e-9, None]
    ax = np.vstack([fnP, fnQ, cr])
    pP = P @ ax.T; pQ = Q @ ax.T
    g = np.maximum(pQ.min(0) - pP.max(0), pP.min(0) - pQ.max(0))
    return float(g.max())


def kandidaten(c, F, rcut):
    out = []
    rng = [-1, 0, 1]
    for j in range(8):
        for jp in range(j, 8):
            for n1 in rng:
                for n2 in rng:
                    for n3 in rng:
                        n = np.array([n1, n2, n3])
                        if jp == j and tuple(n) <= (0, 0, 0):
                            continue
                        d = np.linalg.norm(c[jp] + A0 * (F @ n) - c[j])
                        if d < rcut:
                            out.append((j, jp, n))
    return out


def geometrie(c, R, F, ttrunc=0.05):
    V = ecken(c, R)
    ach = [achsen_tetra(V[j]) for j in range(8)]
    g_nb, g_adj = np.inf, np.inf
    d_oo = np.inf
    for (j, jp, n) in kandidaten(c, F, 2 * S + 1 + 1e-9):
        shift = A0 * (F @ n)
        Pj, Qj = V[j], V[jp] + shift
        dd = np.linalg.norm(Pj[:, None, :] - Qj[None, :, :], axis=2)
        dd = dd[dd > 1e-6]
        if dd.size:
            d_oo = min(d_oo, float(dd.min()))
        if np.linalg.norm(c[jp] + shift - c[j]) >= 2 * S + 1e-9 or jp == j:
            continue
        key = (j, jp, tuple(int(x) for x in n))
        fnP, edP = ach[j]; fnQ, edQ = ach[jp]
        if key in TOP:
            k, kp = TOP[key]
            v = Pj[k]
            P = np.vstack([v + ttrunc * (Pj[i] - v) for i in range(4) if i != k] + [Pj[i] for i in range(4) if i != k])
            Q = np.vstack([v + ttrunc * (Qj[i] - v) for i in range(4) if i != kp] + [Qj[i] for i in range(4) if i != kp])
            g_adj = min(g_adj, sat_gap(P, Q, fnP, edP, fnQ, edQ))
        else:
            g_nb = min(g_nb, sat_gap(Pj, Qj, fnP, edP, fnQ, edQ))
    return {'g_nb': g_nb if np.isfinite(g_nb) else None, 'g_adj': g_adj if np.isfinite(g_adj) else None,
            'd_OO': d_oo if np.isfinite(d_oo) else None}


def o1_maske():
    m = []
    for p in PAARE:
        j, k = p[0], p[1]
        oi, _ = ZUORD[j]
        ax = OPQ[oi] @ NV
        m.append(abs(D[k] @ ax) > 0.999)
    return np.array(m)


O1M = o1_maske()


def eckwinkel(c, R, F):
    v = c[PJ] + np.einsum('pab,pb->pa', R[PJ], T_OFF[PJ, PK])
    a = c[PJ] - v
    b = c[PJ2] + A0 * (PN @ F.T) - v
    cosw = np.sum(a * b, 1) / np.linalg.norm(a, axis=1) / np.linalg.norm(b, axis=1)
    return np.degrees(np.arccos(np.clip(cosw, -1, 1)))


# ---------------- Symmetrie-Tests ----------------
def wrap(d, a):
    f = d / a
    return (f - np.round(f)) * a


def sym_test(c, R, lam, tol=1e-7, tol_s=1e-6):
    a = lam * A0
    V = c[PJ] + np.einsum('pab,pb->pa', R[PJ], T_OFF[PJ, PK])
    akz = []
    for qi, Q in enumerate(O24):
        taus = []
        for jp in range(8):
            tau = c[jp] - Q @ c[0]
            mc = c @ Q.T + tau
            ec = np.linalg.norm(wrap(mc[:, None, :] - c[None, :, :], a), axis=2).min(1).max()
            mv = V @ Q.T + tau
            ev = np.linalg.norm(wrap(mv[:, None, :] - V[None, :, :], a), axis=2).min(1).max()
            if max(ec, ev) < tol:
                taus.append(tau / a)
        akz.append(taus)
    # T = Drehteile von P2_13
    def idx(Q):
        for i, M in enumerate(O24):
            if np.allclose(M, Q):
                return i
    t_ok = all(len(akz[idx(Q)]) > 0 for Q in OPQ)
    schraube = True
    for e, Q in [(np.array([1., 0, 0]), np.diag([1., -1, -1])), (np.array([0, 1., 0]), np.diag([-1., 1, -1])),
                 (np.array([0, 0, 1.]), np.diag([-1., -1, 1]))]:
        ok = False
        for tf in akz[idx(Q)]:
            comp = (tf @ e) % 1.0
            if abs(comp - 0.5) < tol_s:
                ok = True
        schraube = schraube and ok
    n_O = sum(1 for t in akz if len(t) > 0)
    # Platztest: Dreierachse durch jede Mitte
    achs = []
    for j in range(8):
        gef = None
        for Q in OPQ:
            if np.allclose(Q, I3) or np.allclose(np.diag(np.diag(Q)), Q):
                continue
            for tf in akz[idx(Q)]:
                d = Q @ c[j] + tf * a - c[j]
                if np.linalg.norm(wrap(d, a)) < tol:
                    w, U = np.linalg.eig(Q)
                    ax = np.real(U[:, np.argmin(np.abs(w - 1))])
                    ax = ax / np.linalg.norm(ax)
                    gef = int(np.argmax(np.abs(D @ ax)))
                    break
            if gef is not None:
                break
        achs.append(gef)
    platz = all(x is not None for x in achs) and len(set(achs[:4])) == 4 and len(set(achs[4:])) == 4
    return {'P213': bool(t_ok and schraube), 'T_alle': bool(t_ok), 'schrauben': bool(schraube), 'n_O24': int(n_O),
            'platz': bool(platz), 'achsen': achs}


# ---------------- LM fuer Teil C ----------------
def jac_voll(c, R):
    J = np.zeros((48, 45))
    RT1 = np.einsum('pab,pb->pa', R[PJ], T_OFF[PJ, PK])
    RT2 = np.einsum('pab,pb->pa', R[PJ2], T_OFF[PJ2, PK2])
    for p in range(16):
        j, jp = PJ[p], PJ2[p]
        rows = slice(3 * p, 3 * p + 3)
        if j >= 1:
            J[rows, 3 * (j - 1):3 * j] += I3
        if jp >= 1:
            J[rows, 3 * (jp - 1):3 * jp] -= I3
        J[rows, 21 + 3 * j:21 + 3 * j + 3] += -skew(RT1[p])
        J[rows, 21 + 3 * jp:21 + 3 * jp + 3] += skew(RT2[p])
    return J


def lm(c, R, lam, itmax=400):
    F = lam * I3
    c = c.copy(); R = R.copy()
    r = rest(c, R, F).ravel(); cost = r @ r; mu = 1e-3
    it = 0
    for it in range(itmax):
        if np.max(np.linalg.norm(r.reshape(16, 3), axis=1)) < 1e-13:
            break
        J = jac_voll(c, R)
        A = J.T @ J; g = J.T @ r
        while True:
            dx = -np.linalg.solve(A + mu * np.eye(45), g)
            cn = c.copy(); Rn = R.copy()
            cn[1:] += dx[:21].reshape(7, 3)
            for j in range(8):
                Rn[j] = rodrigues(dx[21 + 3 * j:24 + 3 * j]) @ R[j]
            rn = rest(cn, Rn, F).ravel(); cn_cost = rn @ rn
            if cn_cost < cost:
                c, R, r, cost = cn, Rn, rn, cn_cost
                mu = max(mu / 3, 1e-15)
                break
            mu *= 4
            if mu > 1e12:
                break
        if mu > 1e12:
            break
    return c, R, it


def zufallsdrehung(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    w, x, y, z = q
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


def kugel_w(rng, rmax_):
    while True:
        w = rng.uniform(-rmax_, rmax_, 3)
        if np.linalg.norm(w) <= rmax_:
            return w


# ---------------- Modi ----------------
def meta(args):
    with open(os.path.abspath(__file__), 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    return {'code_sha256': h, 'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
            'host': platform.node(), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}


def modus_kontrolle(args):
    out = {'meta': meta(args)}
    # K0: Ideallage
    c0, R0 = baue_p213(Y0)
    out['K0'] = {'r_max_ideal_p213': rmax(rest(c0, R0, I3)),
                 'abw_mitten': float(np.max(np.abs(c0 - C0))),
                 'r_max_ideal_direkt': rmax(rest(C0.copy(), np.stack([I3] * 8), I3)),
                 'sym_ideal': sym_test(C0.copy(), np.stack([I3] * 8), 1.0)}
    # Teil A
    ta = []
    for phd in [1, 5, 10, 20, 30]:
        ph = np.radians(phd)
        RA, RB = rot_axis([0, 0, 1], ph), rot_axis([0, 0, 1], -ph)
        F = np.diag([np.cos(ph), np.cos(ph), 1.0])
        R = np.stack([RA] * 4 + [RB] * 4)
        c = C0 @ F.T
        Dd = rest(c, R, F)
        ta.append({'phi_grad': phd, 'r_max': rmax(Dd), 'V_V0': float(np.linalg.det(F)), 'cos2': float(np.cos(ph) ** 2)})
    out['teilA'] = ta
    # Gamma-Ansatz mit F = lambda I
    from scipy.optimize import least_squares
    rng = np.random.default_rng(args.saat_gamma)
    ga = []
    for lam in [0.99, 0.97, 0.95, 0.90]:
        F = lam * I3

        def fun(x):
            RA, RB = rodrigues(x[0:3]), rodrigues(x[3:6])
            R = np.stack([RA] * 4 + [RB] * 4)
            c = lam * C0.copy(); c[4:] += x[6:9]
            return rest(c, R, F).ravel()
        best_rms, best_max, alle = np.inf, np.inf, []
        for s_ in range(args.n_gamma):
            x0 = np.zeros(9)
            for q in range(2):
                th, ax = drehwinkel_achse(zufallsdrehung(rng))
                x0[3 * q:3 * q + 3] = th * ax
            res = least_squares(fun, x0, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
            Dd = res.fun.reshape(16, 3)
            best_rms = min(best_rms, rrms(Dd)); best_max = min(best_max, rmax(Dd))
            alle.append(rrms(Dd))
        ga.append({'lambda': lam, 'n_starts': args.n_gamma, 'min_r_rms': best_rms, 'min_r_max': best_max,
                   'formel_rms': (1 - lam) / np.sqrt(2), 'quantile_r_rms': [float(np.quantile(alle, q)) for q in (0, .5, 1)]})
    out['gamma'] = ga
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    return out


def korrektor(y, t, ypred, fix_lam=None, itmax=30):
    z = ypred.copy()
    for _ in range(itmax):
        if fix_lam is None:
            g = G_ast(z); J = jac_fd(G_ast, z)
            A = np.vstack([J, t[None, :]]); b = np.concatenate([-g, [-(t @ (z - ypred))]])
            dz = np.linalg.lstsq(A, b, rcond=None)[0]
            z = z + dz
        else:
            f = lambda q: G_ast(np.concatenate([q, [fix_lam]]))
            q = z[:4]
            g = f(q); J = jac_fd(f, q)
            dq = np.linalg.lstsq(J, -g, rcond=None)[0]
            z = np.concatenate([q + dq, [fix_lam]])
            dz = dq
        if np.max(np.abs(dz)) < 1e-15:
            break
    return z


def astpunkt(y):
    c, R = baue_p213(y)
    F = y[4] * I3
    Dd = rest(c, R, F)
    w = eckwinkel(c, R, F)
    geo = geometrie(c, R, F)
    pA, pB, lam = y[0], y[1], y[4]
    km_lam = lam - (1 + np.cos(pA) + np.cos(pB)) / 3
    km_key = np.cos(pA + np.pi / 3) + np.cos(pB - np.pi / 3) - 1
    return {'phiA_grad': float(np.degrees(pA)), 'phiB_grad': float(np.degrees(pB)),
            'phim_grad': float(np.degrees((pA + pB) / 2)), 'uA': float(y[2]), 'uB': float(y[3]),
            'lambda': float(lam), 'V_V0': float(lam ** 3), 'r_max': rmax(Dd),
            'w_O1_min': float(w[O1M].min()), 'w_O1_max': float(w[O1M].max()),
            'w_O2_min': float(w[~O1M].min()), 'w_O2_max': float(w[~O1M].max()),
            'g_nb': geo['g_nb'], 'g_adj': geo['g_adj'], 'd_OO': geo['d_OO'],
            'KM_lam': float(km_lam), 'KM_key': float(km_key)}


def modus_ast(args):
    out = {'meta': meta(args)}
    J0 = jac_fd(G_ast, Y0)
    sv = np.linalg.svd(J0, compute_uv=False)
    out['start'] = {'r_max': rmax(G_ast(Y0).reshape(16, 3)), 'singulaerwerte': [float(x) for x in sv]}
    aeste = {}
    for richtung in (+1, -1):
        y = Y0.copy()
        _, _, Vt = np.linalg.svd(jac_fd(G_ast, y))
        t = Vt[-1]
        if t[0] * richtung < 0:
            t = -t
        pkt = [astpunkt(y)]
        ys = [y.copy()]
        for st in range(args.n_schritte):
            yp = y + args.h * t
            z = korrektor(y, t, yp)
            _, _, Vt = np.linalg.svd(jac_fd(G_ast, z))
            tn = Vt[-1]
            if tn @ t < 0:
                tn = -tn
            y, t = z, tn
            pkt.append(astpunkt(y)); ys.append(y.copy())
            if y[4] < args.lam_stop:
                break
        aeste['plus' if richtung > 0 else 'minus'] = {'punkte': pkt, 'y': [list(map(float, v)) for v in ys]}
    out['aeste'] = aeste
    # exakte Loesungen bei festen lambda
    exakt = []
    for name, ast in aeste.items():
        Y = np.array(ast['y'])
        for lam in [0.99, 0.97, 0.95, 0.90]:
            # erster Astpunkt, der lambda unterschreitet, und Vorgaenger
            idx = np.where(Y[:, 4] <= lam)[0]
            if idx.size == 0:
                exakt.append({'ast': name, 'lambda': lam, 'gefunden': False})
                continue
            i = idx[0]
            ys = Y[i - 1] + (lam - Y[i - 1, 4]) / (Y[i, 4] - Y[i - 1, 4]) * (Y[i] - Y[i - 1])
            ys[4] = lam
            z = korrektor(None, None, ys, fix_lam=lam, itmax=60)
            c, R = baue_p213(z)
            p = astpunkt(z)
            p.update({'ast': name, 'gefunden': True, 'sym': sym_test(c, R, lam), 'y': list(map(float, z))})
            J = jac_voll(c, R)
            sv = np.linalg.svd(J, compute_uv=False)
            p['nullitaet_fest'] = int(np.sum(sv < 1e-8 * sv[0]))
            Jl = np.hstack([J, (-A0 * PN).reshape(48, 1)])
            svl = np.linalg.svd(Jl, compute_uv=False)
            p['nullitaet_lam_frei'] = int(np.sum(svl < 1e-8 * svl[0]))
            p['sv_klein_fest'] = [float(x) for x in sv[-12:]]
            exakt.append(p)
    out['exakt'] = exakt
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    return out


def modus_zufall(args):
    out = {'meta': meta(args), 'laeufe': []}
    lams = [float(x) for x in args.lams.split(',')]
    for li, lam in enumerate(lams):
        rng_n = np.random.default_rng(31 + 100 * int(round(lam * 100)))
        rng_w = np.random.default_rng(32 + 100 * int(round(lam * 100)))
        erg = []
        for art, rng, N in (('nah', rng_n, args.n_nah), ('weit', rng_w, args.n_weit)):
            for s_ in range(N):
                c = lam * C0.copy(); R = np.zeros((8, 3, 3))
                for j in range(8):
                    if art == 'nah':
                        R[j] = rodrigues(kugel_w(rng, 0.5))
                        if j >= 1:
                            c[j] += rng.normal(0, 0.05, 3)
                    else:
                        R[j] = zufallsdrehung(rng)
                        if j >= 1:
                            c[j] += rng.normal(0, 0.2, 3)
                cE, RE, it = lm(c, R, lam, args.itmax)
                Dd = rest(cE, RE, lam * I3)
                e = {'art': art, 'i': s_, 'r_max': rmax(Dd), 'r_rms': rrms(Dd), 'iter': int(it)}
                if e['r_max'] < 1e-10:
                    e['klasse'] = 'Loesung'
                    e['sym'] = sym_test(cE, RE, lam)
                    J = jac_voll(cE, RE)
                    sv = np.linalg.svd(J, compute_uv=False)
                    e['nullitaet_fest'] = int(np.sum(sv < 1e-8 * sv[0]))
                    geo = geometrie(cE, RE, lam * I3)
                    e['g_nb'], e['g_adj'], e['d_OO'] = geo['g_nb'], geo['g_adj'], geo['d_OO']
                    wk = [drehwinkel_achse(RE[j]) for j in range(8)]
                    e['drehwinkel_grad'] = [float(np.degrees(x[0])) for x in wk]
                    e['achse_111_abw'] = [float(1 - np.max(np.abs(D @ x[1]))) for x in wk]
                    e['mitten'] = cE.tolist(); e['R'] = RE.tolist()
                elif e['r_max'] < 1e-6:
                    e['klasse'] = 'fast'
                else:
                    e['klasse'] = 'keine'
                erg.append(e)
        out['laeufe'].append({'lambda': lam, 'starts': erg})
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    return out


def lade(p):
    with open(p) as f:
        return json.load(f)


def modus_auswertung(args):
    ko = lade(args.kontrolle); ast = lade(args.ast)
    zf = []
    for p in args.zufall.split(','):
        zf += lade(p)['laeufe']
    out = {'meta': meta(args), 'eingaben_code_sha256': {'kontrolle': ko['meta']['code_sha256'],
                                                        'ast': ast['meta']['code_sha256']}}
    # IA1
    a_ok = all(x['r_max'] <= 1e-12 for x in ko['teilA'])
    g97 = [g for g in ko['gamma'] if abs(g['lambda'] - 0.97) < 1e-12][0]
    ia1_plan = a_ok and g97['min_r_rms'] > 1e-3
    ia1_wort = ia1_plan and all(g['min_r_rms'] > 1e-6 for g in ko['gamma'])
    # IA2
    plus = ast['aeste']['plus']['punkte']
    ok_ast, erreicht = True, False
    for p in plus:
        if p['r_max'] >= 1e-10:
            ok_ast = False
            break
        if p['lambda'] <= 0.97:
            erreicht = True
            break
    ex97 = [e for e in ast['exakt'] if e.get('gefunden') and e['ast'] == 'plus' and abs(e['lambda'] - 0.97) < 1e-12]
    ex97_ok = bool(ex97) and ex97[0]['r_max'] < 1e-10
    alle_r = [e['r_max'] for e in ast['exakt'] if e.get('gefunden')]
    c_r = {}
    c97 = None
    for L in zf:
        rs = [s['r_max'] for s in L['starts']]
        c_r[str(L['lambda'])] = min(rs)
        if abs(L['lambda'] - 0.97) < 1e-12:
            c97 = L
    if ok_ast and erreicht and ex97_ok:
        ia2_plan = 'eingetroffen'
    elif min(alle_r + list(c_r.values())) >= 1e-6:
        ia2_plan = 'nicht eingetroffen'
    else:
        ia2_plan = 'uneindeutig'
    r97 = [e['r_max'] for e in ex97] + ([min(s['r_max'] for s in c97['starts'])] if c97 else [])
    ia2_wort = 'eingetroffen' if (r97 and min(r97) < 1e-10) else 'nicht eingetroffen'
    # IA3
    b_sym = bool(ex97) and ex97[0]['sym']['P213'] and ex97[0]['sym']['platz']
    c_loes = [s for s in c97['starts'] if s['klasse'] == 'Loesung'] if c97 else []
    c_p213 = [s for s in c_loes if s['sym']['P213']]
    if ia2_plan == 'eingetroffen' and b_sym and len(c_p213) == len(c_loes):
        ia3_plan = 'eingetroffen'
    elif ia2_plan == 'eingetroffen' and b_sym:
        ia3_plan = 'teilweise'
    else:
        ia3_plan = 'nicht eingetroffen'
    if ex97 and ex97[0]['r_max'] < 1e-10:
        ia3_wort = 'eingetroffen' if b_sym else 'nicht eingetroffen'
    elif c_loes:
        best = min(c_loes, key=lambda s: s['r_max'])
        ia3_wort = 'eingetroffen' if (best['sym']['P213'] and best['sym']['platz']) else 'nicht eingetroffen'
    else:
        ia3_wort = 'nicht eingetroffen'
    # Teil C Klassen
    klassen = {}
    for L in zf:
        st = L['starts']
        lo = [s for s in st if s['klasse'] == 'Loesung']
        klassen[str(L['lambda'])] = {
            'n': len(st), 'Loesung': len(lo), 'fast': sum(s['klasse'] == 'fast' for s in st),
            'keine': sum(s['klasse'] == 'keine' for s in st),
            'Loesung_P213': sum(1 for s in lo if s['sym']['P213']),
            'Loesung_nicht_P213': sum(1 for s in lo if not s['sym']['P213']),
            'Loesung_ueberlappungsfrei': sum(1 for s in lo if (s['g_nb'] is None or s['g_nb'] > 0) and (s['g_adj'] is None or s['g_adj'] > 0)),
            'nicht_P213_ueberlappungsfrei': sum(1 for s in lo if not s['sym']['P213'] and (s['g_nb'] is None or s['g_nb'] > 0) and (s['g_adj'] is None or s['g_adj'] > 0)),
            'nah_Loesung': sum(1 for s in lo if s['art'] == 'nah'), 'weit_Loesung': sum(1 for s in lo if s['art'] == 'weit'),
            'nullitaeten': sorted(set(s['nullitaet_fest'] for s in lo)),
            'n_O24_werte': sorted(set(s['sym']['n_O24'] for s in lo)),
            'min_r_max': min(s['r_max'] for s in st)}
    # Beruehrung entlang des Asts (beschreibend)
    ber = {}
    for name in ('plus', 'minus'):
        pk = ast['aeste'][name]['punkte']
        first = None
        for p in pk:
            gs = [g for g in (p['g_nb'], p['g_adj']) if g is not None]
            if gs and min(gs) <= 0:
                first = p
                break
        oo = None
        for p in pk:
            if p['d_OO'] is not None and p['d_OO'] < 1.0:
                oo = p
                break
        ber[name] = {'beruehrung': first, 'd_OO_unter_1': oo, 'n_punkte': len(pk),
                     'max_r_max': max(p['r_max'] for p in pk), 'max_KM_lam': max(abs(p['KM_lam']) for p in pk),
                     'max_KM_key': max(abs(p['KM_key']) for p in pk), 'lambda_end': pk[-1]['lambda']}
    out['urteile'] = {'IA1': {'plan': 'eingetroffen' if ia1_plan else 'nicht eingetroffen',
                              'wortlaut': 'eingetroffen' if ia1_wort else 'nicht eingetroffen',
                              'teilA_max_r': max(x['r_max'] for x in ko['teilA']), 'gamma97_min_r_rms': g97['min_r_rms'],
                              'gamma_min_r_rms': {str(g['lambda']): g['min_r_rms'] for g in ko['gamma']}},
                      'IA2': {'plan': ia2_plan, 'wortlaut': ia2_wort, 'ast_ok': ok_ast, 'ast_erreicht_097': erreicht,
                              'exakt097_r_max': ex97[0]['r_max'] if ex97 else None, 'C_min_r_max': c_r},
                      'IA3': {'plan': ia3_plan, 'wortlaut': ia3_wort, 'B_sym': ex97[0]['sym'] if ex97 else None,
                              'C097_Loesungen': len(c_loes), 'C097_P213': len(c_p213)}}
    out['teilC'] = klassen
    out['ast'] = ber
    return out


def modus_bild(args):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    ast = lade(args.ast)
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.8))
    ax = axs[0]
    farben = {'plus': '#1f5fa8', 'minus': '#b5651d'}
    for name in ('plus', 'minus'):
        pk = ast['aeste'][name]['punkte']
        x = [abs(p['phim_grad']) for p in pk]; v = [p['V_V0'] for p in pk]
        ax.plot(x, v, color=farben[name], lw=2 if name == 'plus' else 1, ls='-' if name == 'plus' else '--',
                label='P2_13-Ast ' + ('(phi > 0)' if name == 'plus' else '(phi < 0, Spiegel)'))
        for p in pk:
            gs = [g for g in (p['g_nb'], p['g_adj']) if g is not None]
            if gs and min(gs) <= 0:
                ax.axvline(abs(p['phim_grad']), color=farben[name], lw=0.8, ls=':')
                ax.annotate('Beruehrung', (abs(p['phim_grad']), p['V_V0']), fontsize=8, color=farben[name])
                break
    ph = np.linspace(0, 60, 200)
    ax.plot(ph, np.cos(np.radians(ph)) ** 2, color='0.5', lw=1, label='Teil A: Gegendrehung um [001], V/V0 = cos^2 phi')
    ax.set_xlabel('Kippwinkel |phi_m| = |phi_A + phi_B|/2 (Grad)')
    ax.set_ylabel('V/V0 = lambda^3 (Teil A: cos^2 phi)')
    ax.set_title('ISO-ATEM-1: Volumen gegen Kippwinkel')
    ax.legend(fontsize=8); ax.grid(alpha=.3)
    ax = axs[1]
    pk = ast['aeste']['plus']['punkte']
    x = [abs(p['phim_grad']) for p in pk]
    ax.plot(x, [p['w_O2_min'] for p in pk], color='#1f5fa8', label='Winkel an O2-Ecken (12 je Zelle)')
    ax.plot(x, [p['w_O1_min'] for p in pk], color='#2e8b57', ls='--', label='Winkel an O1-Ecken (4, auf der Achse)')
    ax.set_xlabel('Kippwinkel |phi_m| (Grad)')
    ax.set_ylabel('Mitte-Ecke-Mitte-Winkel ("Si-O-Si", Grad)')
    ax.set_title('Winkel an der geteilten Ecke (Ast phi > 0)')
    ax.legend(fontsize=8); ax.grid(alpha=.3)
    fig.tight_layout()
    fig.savefig(args.png, dpi=130)
    return {'meta': meta(args), 'png': args.png}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['kontrolle', 'ast', 'zufall', 'auswertung', 'bild'])
    ap.add_argument('--out', required=True)
    ap.add_argument('--n_gamma', type=int, default=200)
    ap.add_argument('--saat_gamma', type=int, default=21)
    ap.add_argument('--h', type=float, default=0.002)
    ap.add_argument('--n_schritte', type=int, default=2500)
    ap.add_argument('--lam_stop', type=float, default=0.6)
    ap.add_argument('--lams', default='0.99,0.97,0.95,0.90')
    ap.add_argument('--n_nah', type=int, default=300)
    ap.add_argument('--n_weit', type=int, default=300)
    ap.add_argument('--itmax', type=int, default=400)
    ap.add_argument('--kontrolle'); ap.add_argument('--ast'); ap.add_argument('--zufall')
    ap.add_argument('--png')
    args = ap.parse_args()
    t0 = time.time()
    res = {'kontrolle': modus_kontrolle, 'ast': modus_ast, 'zufall': modus_zufall,
           'auswertung': modus_auswertung, 'bild': modus_bild}[args.modus](args)
    res['laufzeit_s'] = time.time() - t0
    with open(args.out + '.neu', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.tolist() if hasattr(o, 'tolist') else str(o))
    os.replace(args.out + '.neu', args.out)
    print('fertig', args.modus, '%.1f s' % res['laufzeit_s'])


if __name__ == '__main__':
    main()
