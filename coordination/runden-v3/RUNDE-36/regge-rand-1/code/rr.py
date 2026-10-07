#!/usr/bin/env python3
"""REGGE-RAND-1 (Runde 36): Regge-Fehlwinkel auf dem Kuhn-Tetraedergitter, konformer Ansatz,
linearisierter Eckenoperator, Punktquelle und Klumpen, Gauss-Randmasse.

Nur auf der .69 ueber kleintest.sh (Spur p4000a); float64; reines numpy.
Modi:
  rauch   : Flachheit, lokale Jacobi-Matrix, Schablone (L = 8), Normierungspruefung (quadratisches psi),
            kleines Spektrum (L = 8), Symbol bei kleinem k. Nur Kontrollen, keine Urteilsgroessen.
  linear  : alle linearen Groessen fuer RR0 bis RR4 (L = 8/10/12 dicht; L = 32/64 Loesungen; Groessenreihe
            64/128/256 fuer die Punktquelle).
Konventionen (PLAN.md):
  Ecken n in Z^3_L (periodisch), 7 positive Kantenrichtungen, 6 Kuhn-Tetraeder je Wuerfel (Permutationen).
  l_e = l0_e * psi_e^2, psi_e = (psi_a + psi_b)/2;  eps_e = 2 pi - Summe der Diederwinkel um e;
  Eckenregel F_v = sum_{e an v} l_e eps_e = 16 pi G m_v;  linear: A dpsi = 16 pi G (m - mquer).
"""
import argparse
import itertools
import json
import math
import sys
import time

import numpy as np

G = 1.0
XI_SC = -2.837297  # Ewald-Konstante des einfach kubischen Torus [L], nur fuer die Hintergrundkorrektur
DIRS = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)], dtype=int)
DTUP = [tuple(int(x) for x in d) for d in DIRS]
L0 = np.sqrt((DIRS ** 2).sum(axis=1).astype(float))
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
PERMS = list(itertools.permutations(range(3)))
AX = (-3, -2, -1)
TYP = ["achse", "achse", "achse", "flaeche", "flaeche", "flaeche", "raum"]


def _dir_index(v):
    for i, d in enumerate(DIRS):
        if np.array_equal(d, v):
            return i
    raise ValueError(v)


# Tetraeder je Zelle n und Permutation p: Pfad P0 = n, P1 = n + e_p0, P2 = P1 + e_p1, P3 = n + (1,1,1).
# Je Kante (Paar i<j im Pfad): (Versatz des Startpunkts P_i relativ zu n, Richtungsindex von P_j - P_i).
TETS = []
for _p in PERMS:
    _P = [np.zeros(3, dtype=int)]
    for _k in range(3):
        _P.append(_P[-1] + np.eye(3, dtype=int)[_p[_k]])
    TETS.append([(tuple(int(x) for x in _P[i]), _dir_index(_P[j] - _P[i])) for (i, j) in PAIRS])


def get(a, off):
    """b[n] = a[n + off] (periodisch, letzte drei Achsen)."""
    return np.roll(a, shift=tuple(-o for o in off), axis=AX)


def put(b, off):
    """c[n + off] = b[n] (periodisch, letzte drei Achsen)."""
    return np.roll(b, shift=tuple(off), axis=AX)


def dihedrals(dsq):
    """Diederwinkel eines Tetraeders aus den quadrierten Kantenlaengen (Liste in PAIRS-Reihenfolge).
    Kante (i,j), uebrige Ecken k,l: Winkel zwischen den auf (P_j - P_i) senkrechten Anteilen von P_k - P_i
    und P_l - P_i. Analytisch in den Eingaben (komplexer Schritt moeglich)."""
    D = {}
    for (i, j), d in zip(PAIRS, dsq):
        D[(i, j)] = d
        D[(j, i)] = d
    out = []
    for (i, j) in PAIRS:
        k, l = [m for m in range(4) if m not in (i, j)]
        aa = D[(i, j)]
        ab = 0.5 * (D[(i, j)] + D[(i, k)] - D[(j, k)])
        ac = 0.5 * (D[(i, j)] + D[(i, l)] - D[(j, l)])
        bc = 0.5 * (D[(i, k)] + D[(i, l)] - D[(k, l)])
        bb = D[(i, k)]
        cc = D[(i, l)]
        num = bc - ab * ac / aa
        den = np.sqrt((bb - ab * ab / aa) * (cc - ac * ac / aa))
        out.append(np.arccos(num / den))
    return out


def lengths(psi):
    return [L0[t] * (0.5 * (psi + get(psi, DTUP[t]))) ** 2 for t in range(7)]


def deficits(lt):
    S = [np.zeros_like(lt[0]) for _ in range(7)]
    for tet in TETS:
        th = dihedrals([get(lt[tau], off) ** 2 for (off, tau) in tet])
        for (off, tau), a in zip(tet, th):
            S[tau] = S[tau] + put(a, off)
    return [2.0 * np.pi - s for s in S]


def tet_count(L):
    one = np.ones((L, L, L))
    S = [np.zeros((L, L, L)) for _ in range(7)]
    for tet in TETS:
        for (off, tau) in tet:
            S[tau] = S[tau] + put(one, off)
    return [float(s.min()) for s in S], [float(s.max()) for s in S]


def vertex_sum(lt, eps):
    F = np.zeros_like(lt[0])
    for t in range(7):
        X = lt[t] * eps[t]
        F = F + X + put(X, DTUP[t])
    return F


def F_psi(psi):
    lt = lengths(psi)
    eps = deficits(lt)
    return vertex_sum(lt, eps), lt, eps


def local_jacobians(h=1e-30):
    """d theta_k / d l_m je Tetraeder-Orientierung (6 x 6), komplexer Schritt, am flachen Hintergrund."""
    Js = []
    for tet in TETS:
        l = np.array([L0[tau] for (off, tau) in tet], dtype=complex)
        J = np.zeros((6, 6))
        for m in range(6):
            lc = l.copy()
            lc[m] += 1j * h
            th = dihedrals([x * x for x in lc])
            J[:, m] = np.array([np.imag(t) for t in th]) / h
        Js.append(J)
    return Js


def local_jacobians_fd(h=1e-6):
    Js = []
    for tet in TETS:
        l = np.array([L0[tau] for (off, tau) in tet], dtype=float)
        J = np.zeros((6, 6))
        for m in range(6):
            lp = l.copy()
            lm = l.copy()
            lp[m] += h
            lm[m] -= h
            tp = np.array(dihedrals([x * x for x in lp]))
            tm = np.array(dihedrals([x * x for x in lm]))
            J[:, m] = (tp - tm) / (2 * h)
        Js.append(J)
    return Js


def apply_A(dpsi, Js):
    """Linearisierter Eckenoperator ueber die lokalen Jacobi-Matrizen:
    dl_e = l0_e (dpsi_a + dpsi_b); deps_e = -sum_t dtheta_{t,e}; (A dpsi)_v = sum_{e an v} l0_e deps_e."""
    dl = [L0[t] * (dpsi + get(dpsi, DTUP[t])) for t in range(7)]
    S = [np.zeros_like(dpsi) for _ in range(7)]
    for tet, J in zip(TETS, Js):
        g = [get(dl[tau], off) for (off, tau) in tet]
        for k, (off, tau) in enumerate(tet):
            dth = J[k, 0] * g[0]
            for m in range(1, 6):
                dth = dth + J[k, m] * g[m]
            S[tau] = S[tau] + put(dth, off)
    out = np.zeros_like(dpsi)
    for t in range(7):
        X = -L0[t] * S[t]
        out = out + X + put(X, DTUP[t])
    return out


def apply_A_cs(dpsi, h=1e-30):
    """Derselbe Operator unabhaengig: komplexer Schritt durch die volle nichtlineare Eckenregel F(psi)."""
    F, _, _ = F_psi(1.0 + 1j * h * dpsi.astype(complex))
    return F.imag / h


def stencil(Js, L=8):
    d0 = np.zeros((L, L, L))
    d0[0, 0, 0] = 1.0
    r = apply_A(d0, Js)  # r[v] = A[v, 0] = a(-v), a(d) := Koeffizient von psi_{v+d} in (A psi)_v
    st = {}
    mask = np.ones((L, L, L), bool)
    for d in itertools.product((-1, 0, 1), repeat=3):
        st[d] = float(r[(-d[0]) % L, (-d[1]) % L, (-d[2]) % L])
        mask[d[0] % L, d[1] % L, d[2] % L] = False
    rest = float(np.abs(r[mask]).max())
    return st, rest


def symbol_r(st, L):
    s = np.zeros((L, L, L))
    for d, v in st.items():
        s[d[0] % L, d[1] % L, d[2] % L] += v
    sh = np.fft.rfftn(s)
    return sh.real, float(np.abs(sh.imag).max())


def symbol_at(st, k):
    k = np.asarray(k, float)
    return float(sum(v * math.cos(float(np.dot(k, d))) for d, v in st.items()))


def coords(L):
    n = np.arange(L)
    c = ((n + L // 2) % L) - L // 2
    X, Y, Z = np.meshgrid(c, c, c, indexing="ij")
    return X, Y, Z


def solve_fft(m, symr):
    sym = symr.copy()
    sym[0, 0, 0] = np.inf
    return np.fft.irfftn(16 * np.pi * G * np.fft.rfftn(m) / sym, s=m.shape, axes=(0, 1, 2))


def dense_A(Js, L):
    N = L ** 3
    A = np.zeros((N, N))
    for j in range(N):
        e = np.zeros(N)
        e[j] = 1.0
        A[:, j] = apply_A(e.reshape(L, L, L), Js).ravel()
    return A


RAYS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1),
        (1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]


def torus_corr_point(L, r2, M=1.0):
    return G * M * (XI_SC / (2 * L) + np.pi * r2 / (3 * L ** 3))


def flux(psi, offs_coef, inD):
    tot = 0.0
    for d, a in offs_coef:
        if d == (0, 0, 0) or a == 0.0:
            continue
        sel = inD & ~get(inD, d)
        tot += a * float(np.sum((get(psi, d) - psi)[sel]))
    return tot


def trilin(psi, P):
    L = psi.shape[0]
    f = np.floor(P).astype(int)
    t = P - f
    val = np.zeros(P.shape[0])
    for c in itertools.product((0, 1), repeat=3):
        cc = np.array(c)
        w = np.prod(np.where(cc[None, :] == 1, t, 1 - t), axis=1)
        idx = (f + cc[None, :]) % L
        val += w * psi[idx[:, 0], idx[:, 1], idx[:, 2]]
    return val


def fib_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)


def measure(psi, m, st, L, label, R_list, ball=None):
    """Messgroessen fuer eine Loesung psi (= delta psi) auf dem Torus L, Quelle um die Ecke 0."""
    X, Y, Z = coords(L)
    r2 = (X ** 2 + Y ** 2 + Z ** 2).astype(float)
    r = np.sqrt(r2)
    M = float(m.sum())
    mbar = M / L ** 3
    if ball is None:
        corr = torus_corr_point(L, r2, M)
    else:
        s2 = float((m * r2).sum())
        corr = G * M * XI_SC / (2 * L) + np.pi * G * (M * r2 + s2) / (3 * L ** 3)
    pc = psi - corr
    f_raw = r * psi / (G * M / 2)
    f_cor = r * pc / (G * M / 2)
    res = {"label": label, "L": L, "M": M}
    # RR2: alle Gitterpunkte 6 <= |x| <= L/4
    sel = (r >= 6) & (r <= L / 4)
    dev = np.abs(f_cor[sel] - 1)
    i = int(np.argmax(dev))
    pts = np.stack([X[sel], Y[sel], Z[sel]], 1)
    res["rr2"] = {"n_punkte": int(sel.sum()), "max_abw_korr": float(dev.max()),
                  "ort_max": [int(v) for v in pts[i]], "r_max": float(r[sel][i]),
                  "f_korr_min": float(f_cor[sel].min()), "f_korr_max": float(f_cor[sel].max()),
                  "max_abw_roh": float(np.abs(f_raw[sel] - 1).max())}
    # RR3: Schale 11,5 <= |x| <= 12,5 (und weitere Schalen zum Bild)
    shells = {}
    for r0 in (6, 8, 10, 12, 14, 16):
        if r0 + 0.5 > L / 2 - 1:
            continue
        s = (r >= r0 - 0.5) & (r <= r0 + 0.5)
        fc = f_cor[s]
        fr = f_raw[s]
        shells[str(r0)] = {"n": int(s.sum()), "S_korr": float((fc.max() - fc.min()) / fc.mean()),
                           "std_rel_korr": float(fc.std() / fc.mean()), "mittel_korr": float(fc.mean()),
                           "min_korr": float(fc.min()), "max_korr": float(fc.max()),
                           "S_roh": float((fr.max() - fr.min()) / fr.mean())}
    res["schalen"] = shells
    # Shell-Punkte r = 12 fuer das Bild (Winkel zur Raumdiagonale)
    s = (r >= 11.5) & (r <= 12.5)
    cosd = (X[s] + Y[s] + Z[s]) / (np.sqrt(3) * r[s])
    res["schale12_punkte"] = {"cos_111": cosd.tolist(), "f_korr": f_cor[s].tolist(), "r": r[s].tolist()}
    # Strahlen
    rays = {}
    for u in RAYS:
        uu = np.array(u)
        lst = []
        n = 1
        while np.linalg.norm(n * uu) <= L / 2 - 2:
            p = n * uu
            idx = tuple(int(v) % L for v in p)
            lst.append([float(np.linalg.norm(p)), float(psi[idx]), float(pc[idx])])
            n += 1
        rays[str(u)] = lst
    res["strahlen"] = rays
    # Gauss-Massen auf Wuerfelschalen
    offs = list(st.items())
    seven = [((1, 0, 0), 1.0), ((-1, 0, 0), 1.0), ((0, 1, 0), 1.0), ((0, -1, 0), 1.0), ((0, 0, 1), 1.0),
             ((0, 0, -1), 1.0)]
    gl = []
    for R in R_list:
        if R + 1 > L / 2 - 1:
            continue
        inD = (np.abs(X) <= R) & (np.abs(Y) <= R) & (np.abs(Z) <= R)
        nD = int(inD.sum())
        f_op = flux(psi, offs, inD)
        f_7 = flux(psi, seven, inD)
        MD = float(m[inD].sum())
        # Kugel-Gauss (nur Bericht): Fibonacci-Punkte, radiale Differenz +-0,5 mit trilinearer Interpolation
        nh = fib_sphere(4000)
        dr = (trilin(psi, (R + 0.5) * nh) - trilin(psi, (R - 0.5) * nh))
        M_sph = -(1 / (2 * np.pi * G)) * 4 * np.pi * R ** 2 * float(dr.mean()) + mbar * (4 / 3) * np.pi * R ** 3
        gl.append({"R": R, "n_D": nD, "M_D": MD,
                   "M_op_roh": f_op / (16 * np.pi * G), "M_op": f_op / (16 * np.pi * G) + mbar * nD,
                   "M_G_roh": -f_7 / (2 * np.pi * G), "M_G": -f_7 / (2 * np.pi * G) + mbar * nD,
                   "M_kugel": M_sph})
    res["gauss"] = gl
    return res


def modus_rauch(out):
    t0 = time.time()
    R = {}
    L = 8
    psi1 = np.ones((L, L, L))
    F1, lt, eps = F_psi(psi1)
    R["flach_max_eps"] = float(max(np.abs(e).max() for e in eps))
    R["flach_max_F"] = float(np.abs(F1).max())
    R["tet_zahl_min_max"] = tet_count(L)
    psi13 = 1.3 * np.ones((L, L, L))
    F13, _, eps13 = F_psi(psi13)
    R["skaliert_1p3_max_eps"] = float(max(np.abs(e).max() for e in eps13))
    Js = local_jacobians()
    Jf = local_jacobians_fd()
    R["J_cs_minus_fd"] = float(max(np.abs(a - b).max() for a, b in zip(Js, Jf)))
    R["J_gleich_fuer_alle_6"] = float(max(np.abs(J - Js[0]).max() for J in Js))
    R["J0"] = Js[0].tolist()
    st, rest = stencil(Js, L)
    R["schablone"] = {str(k): v for k, v in st.items()}
    R["schablone_rest_ausserhalb"] = rest
    # Normierung: psi = 1 + h x_i x_j / 2 um die Mitte c, F_c / h gegen -8 delta_ij
    Lq = 12
    X, Y, Z = coords(Lq)
    XX = [X, Y, Z]
    norm = {}
    for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
        q = 0.5 * XX[i] * XX[j]
        Fc = apply_A_cs(q)[0, 0, 0]
        Fj = apply_A(q, Js)[0, 0, 0]
        hnl = 1e-4
        Fnl = F_psi(1.0 + hnl * q)[0][0, 0, 0] / hnl
        norm[f"x{i}x{j}/2"] = {"cs": float(Fc), "jac": float(Fj), "nichtlinear_h1e-4": float(Fnl),
                               "soll": -8.0 if i == j else 0.0}
    R["normierung_quadratisch"] = norm
    # Symbol bei kleinem k
    small = {}
    for u in [(1, 0, 0), (1, 1, 0), (1, -1, 0), (1, 1, 1), (1, 1, -1), (1, 2, 3)]:
        uu = np.array(u, float) / np.linalg.norm(u)
        vals = []
        for kk in (2 * np.pi / 256, 2 * np.pi / 64, 2 * np.pi / 16):
            k = kk * uu
            vals.append([kk, symbol_at(st, k) / (8 * kk ** 2)])
        small[str(u)] = vals
    R["symbol_klein_k_durch_8k2"] = small
    # kleines Spektrum L = 8 (dicht)
    A = dense_A(Js, L)
    R["L8_sym"] = float(np.abs(A - A.T).max() / np.abs(A).max())
    R["L8_A_mal_1"] = float(np.abs(A.sum(axis=1)).max() / np.abs(A).max())
    ev = np.linalg.eigvalsh(0.5 * (A + A.T))
    R["L8_eig_kleinste"] = ev[:5].tolist()
    R["L8_eig_groesste"] = ev[-3:].tolist()
    # Probe des komplexen Schritts gegen Jacobi-Weg auf L = 8, Zufallsfeld
    rng = np.random.default_rng(1)
    dp = rng.standard_normal((L, L, L))
    R["L8_cs_minus_jac"] = float(np.abs(apply_A_cs(dp) - apply_A(dp, Js)).max())
    R["zeit_s"] = time.time() - t0
    with open(out, "w") as fh:
        json.dump(R, fh, indent=1)
    print(json.dumps({k: R[k] for k in R if k not in ("J0", "schablone")}, indent=1))


def modus_linear(out, groessen):
    t0 = time.time()
    R = {"start_unix": t0}
    # RR0 (a): Flachheit auf L = 8 und L = 64
    for L in (8, 64):
        F1, lt, eps = F_psi(np.ones((L, L, L)))
        R[f"rr0_flach_L{L}"] = {"max_eps": float(max(np.abs(e).max() for e in eps)),
                                "max_eps_je_typ": [float(np.abs(e).max()) for e in eps],
                                "max_F": float(np.abs(F1).max())}
    R["tet_zahl_min_max_L8"] = tet_count(8)
    Fs, _, epss = F_psi(1.3 * np.ones((8, 8, 8)))
    R["skaliert_1p3_max_eps"] = float(max(np.abs(e).max() for e in epss))
    Js = local_jacobians()
    Jf = local_jacobians_fd()
    R["J_cs_minus_fd"] = float(max(np.abs(a - b).max() for a, b in zip(Js, Jf)))
    R["J_gleich_fuer_alle_6"] = float(max(np.abs(J - Js[0]).max() for J in Js))
    lv = np.array([L0[tau] for (off, tau) in TETS[0]])
    K0 = Js[0]
    R["J0"] = K0.tolist()
    R["J0_symmetrie"] = float(np.abs(K0 - K0.T).max())
    R["schlaefli_l_mal_J"] = float(np.abs(lv @ K0).max())
    st, rest = stencil(Js, 8)
    R["schablone"] = {str(k): v for k, v in st.items()}
    R["schablone_rest_ausserhalb"] = rest
    # Normierung (wie Rauchlauf, im Hauptlauf wiederholt)
    X, Y, Z = coords(12)
    XX = [X, Y, Z]
    norm = {}
    for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
        q = 0.5 * XX[i] * XX[j]
        norm[f"x{i}x{j}/2"] = {"cs": float(apply_A_cs(q)[0, 0, 0]), "jac": float(apply_A(q, Js)[0, 0, 0]),
                               "soll": -8.0 if i == j else 0.0}
    R["normierung_quadratisch"] = norm
    # RR0 (b,c), RR1: dicht auf L = 8, 10, 12
    dense = {}
    for L in (8, 10, 12):
        A = dense_A(Js, L)
        amax = float(np.abs(A).max())
        w, V = np.linalg.eigh(0.5 * (A + A.T))
        lmax = float(w[-1])
        tol = 1e-9 * lmax
        n0 = int(np.sum(np.abs(w) <= tol))
        i0 = int(np.argmin(np.abs(w)))
        c = np.ones(L ** 3) / math.sqrt(L ** 3)
        ov = float(abs(V[:, i0] @ c))
        # Symbol auf dem vollen L-Gitter (fftn) zum Vergleich mit den Eigenwerten
        s = np.zeros((L, L, L))
        for d, v in st.items():
            s[d[0] % L, d[1] % L, d[2] % L] += v
        sfull = np.sort(np.fft.fftn(s).real.ravel())
        dense[str(L)] = {"sym_rel": float(np.abs(A - A.T).max() / amax),
                         "A_mal_1_rel": float(np.abs(A.sum(axis=1)).max() / amax),
                         "eig_min": float(w[0]), "eig_2": float(w[1]), "eig_3": float(w[2]), "eig_max": lmax,
                         "n_null": n0, "ueberlapp_konst": ov,
                         "n_negativ": int(np.sum(w < -tol)),
                         "eig_minus_symbol_max": float(np.abs(np.sort(w) - sfull).max()),
                         "zweitkleinster_soll_8(2-2cos(2pi/L))": 8 * (2 - 2 * math.cos(2 * math.pi / L))}
        del A, V
    R["dicht"] = dense
    # Symbol auf dem L = 64-Gitter und an Zonenrandpunkten
    symr64, imag64 = symbol_r(st, 64)
    sy = symr64.copy()
    sy[0, 0, 0] = np.inf
    R["symbol_L64"] = {"min_k_ungleich_0": float(sy.min()), "max": float(symr64.max()), "imag_max": imag64}
    zb = {}
    for k in [(np.pi, 0, 0), (0, np.pi, 0), (0, 0, np.pi), (np.pi, np.pi, 0), (np.pi, 0, np.pi), (0, np.pi, np.pi),
              (np.pi, np.pi, np.pi), (np.pi, -np.pi, 0), (2 * np.pi / 3, 2 * np.pi / 3, 2 * np.pi / 3),
              (np.pi / 2, np.pi / 2, np.pi / 2)]:
        zb[str(tuple(round(x, 4) for x in k))] = symbol_at(st, k)
    R["symbol_zonenrand"] = zb
    # Symbol entlang Weg und Kleink-Verhaeltnis
    small = {}
    for u in [(1, 0, 0), (1, 1, 0), (1, -1, 0), (1, 1, 1), (1, 1, -1), (1, 2, 3)]:
        uu = np.array(u, float) / np.linalg.norm(u)
        small[str(u)] = [[kk, symbol_at(st, kk * uu) / (8 * kk ** 2)] for kk in
                         (2 * np.pi / 256, 2 * np.pi / 64, 2 * np.pi / 16, 2 * np.pi / 8, 2 * np.pi / 4)]
    R["symbol_klein_k_durch_8k2"] = small
    # Loesungen
    sols = {}
    for L in groessen:
        X, Y, Z = coords(L)
        r2 = X ** 2 + Y ** 2 + Z ** 2
        symr, _ = symbol_r(st, L)
        m_a = np.zeros((L, L, L))
        m_a[0, 0, 0] = 1.0
        ball = r2 <= 36
        m_b = np.where(ball, 1.0 / ball.sum(), 0.0)
        Rl = [10, 12, 14, 16, 18, 20, 24, 28]
        entry = {"n_kugel": int(ball.sum())}
        quellen = (("punkt", m_a), ("kugel6", m_b)) if L <= 64 else (("punkt", m_a),)
        for lab, mm in quellen:
            psi = solve_fft(mm, symr)
            if L <= 64:
                rres = apply_A(psi, Js) - 16 * np.pi * G * (mm - mm.mean())
                entry[f"{lab}_residuum_jac"] = float(np.abs(rres).max() / (16 * np.pi * G * mm.max()))
                if L <= 64:
                    rcs = apply_A_cs(psi) - 16 * np.pi * G * (mm - mm.mean())
                    entry[f"{lab}_residuum_cs"] = float(np.abs(rcs).max() / (16 * np.pi * G * mm.max()))
                entry[lab] = measure(psi, mm, st, L, lab, Rl, ball=(None if lab == "punkt" else True))
            else:
                # nur Strahlen fuer die Groessenreihe (Punktquelle)
                if lab == "punkt":
                    rays = {}
                    for u in RAYS:
                        uu = np.array(u)
                        lst = []
                        n = 1
                        while np.linalg.norm(n * uu) <= 16.5:
                            p = n * uu
                            lst.append([float(np.linalg.norm(p)), float(psi[tuple(int(v) % L for v in p)])])
                            n += 1
                        rays[str(u)] = lst
                    entry["punkt_strahlen_roh"] = rays
            del psi
        sols[str(L)] = entry
        print(f"L={L} fertig {time.time() - t0:.1f}s", flush=True)
    R["loesungen"] = sols
    R["zeit_s"] = time.time() - t0
    with open(out, "w") as fh:
        json.dump(R, fh)
    print("fertig", R["zeit_s"])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--modus", required=True, choices=["rauch", "linear"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--groessen", default="32,64,128,256")
    a = ap.parse_args()
    if a.modus == "rauch":
        modus_rauch(a.out)
    else:
        modus_linear(a.out, [int(x) for x in a.groessen.split(",")])
