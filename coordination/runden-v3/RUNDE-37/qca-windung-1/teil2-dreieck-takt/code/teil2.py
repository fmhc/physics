#!/usr/bin/env python3
# DREIECK-TAKT-1 mit QCA-WINDUNG-2 (Runde 41, Teil 2, fmhc-physics). Code-Agent fuer die Leitung claude-primary.
# windung.py ist die unveraenderte Kopie aus Teil 1 (W3-Integral, Weyl-Suche, Inversion).
# Aufruf nur auf der .69 ueber kleintest.sh:
#   teil2.py --teil P3 --modus rauch|haupt --out DATEI.json   (3D: Produkte, Pyrochlor-Dreieckstakt, Additivitaet,
#                                                              Higashikawa-Nachbau)
#   teil2.py --teil LM --modus rauch|haupt --out DATEI.json   (3D: allgemeine endlichreichweitige Unitaere per Suche)
#   teil2.py --teil H2 --modus rauch|haupt --out DATEI.json   (2D: Wabengitter nach Kitagawa u. a. 2010)
import argparse
import json
import sys
import time

import numpy as np
from scipy.linalg import schur
from scipy.optimize import least_squares

import windung as W1

I2 = W1.I2
PAULI = W1.PAULI
B_W = W1.B_WUERFEL
RICHTUNGEN = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, -1, 0], [1, 0, -1],
                       [0, 1, -1], [1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])


# ---------------------------------------------------------------- Hilfen 3D
def haar(n, rng):
    Z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    Q, R = np.linalg.qr(Z)
    return Q * (np.diag(R) / np.abs(np.diag(R)))[None, :]


def fprod(a, b):
    # exaktes Produkt zweier Fourier-Automaten (Faltung der Koeffizienten)
    d = {}
    for f, Af in zip(np.rint(a.F).astype(int), a.A):
        for g, Bg in zip(np.rint(b.F).astype(int), b.A):
            h = tuple(int(x) for x in (f + g))
            d[h] = d.get(h, 0) + Af @ Bg
    keys = sorted(d)
    A = np.array([d[k] for k in keys])
    F = np.array(keys)
    keep = np.abs(A).reshape(len(A), -1).max(1) > 1e-14
    return W1.Fourier(A[keep], F[keep])


def kette(faktoren):
    out = faktoren[0]
    for f in faktoren[1:]:
        out = fprod(out, f)
    return out


def teilschiebung(P, f):
    n = P.shape[0]
    return W1.Fourier(np.array([np.eye(n) - P, P]), np.array([[0, 0, 0], list(f)]))


def muenze(C):
    return W1.Fourier(np.asarray(C, complex)[None], np.zeros((1, 3)))


def n_exakt(aut):
    # Integrand tr(X1[X2,X3]) ist ein trig. Polynom mit Frequenzen bis 6 M je Richtung; Rechteckregel exakt fuer N > 6M
    M = int(np.abs(np.rint(aut.F)).max()) if len(aut.F) else 0
    return 6 * M + 1


def w3_satz(aut, B=B_W, extra=()):
    out = {"gitter": {}}
    Ns = sorted(set([16, 24, 32, 48] + list(extra)))
    for N in Ns:
        re, im = W1.w3_integral(aut, B, N)
        out["gitter"][str(N)] = {"W3": re, "im": im}
    return out


def unitaer(aut, B=B_W):
    return W1.unitaritaet(aut, B)


# ---------------------------------------------------------------- Pyrochlor-Dreieckstakt (Finns Bild in 3D)
FLAECHEN = [(1, 2, 3), (0, 3, 2), (0, 1, 3), (0, 2, 1)]  # Rand des Simplex [0123], gleich orientiert


def bindungsschritt(a, b, n, theta, N=4):
    # exp(-i theta (e^{i u.n}|a><b| + h.c.)) auf {a, b}; u = (k.a1, k.a2, k.a3), FCC-Grundvektoren
    A0 = np.eye(N, dtype=complex)
    A0[a, a] = A0[b, b] = np.cos(theta)
    if not np.any(n):
        A0[a, b] = A0[b, a] = -1j * np.sin(theta)
        return W1.Fourier(A0[None], np.zeros((1, 3)))
    Ap = np.zeros((N, N), complex)
    Am = np.zeros((N, N), complex)
    Ap[a, b] = -1j * np.sin(theta)
    Am[b, a] = -1j * np.sin(theta)
    return W1.Fourier(np.array([A0, Ap, Am]), np.array([[0, 0, 0], list(n), list(-np.asarray(n))]))


def e_sub(a):
    return np.zeros(3, int) if a == 0 else np.eye(3, dtype=int)[a - 1]


def dreieckstakt(theta, umkehr=False):
    schritte = []
    for unten in (False, True):
        for (a, b, c) in FLAECHEN:
            seq = [(a, b), (b, c), (c, a)]
            if umkehr:
                seq = [(c, b), (b, a), (a, c)]
            for (p, q) in seq:
                n = (e_sub(p) - e_sub(q)) if unten else np.zeros(3, int)
                schritte.append(bindungsschritt(p, q, n, theta))
    # Zeitordnung: erster Schritt wirkt zuerst -> U = S_last ... S_1
    return kette(schritte[::-1]), len(schritte)


# ---------------------------------------------------------------- Higashikawa/Nakagawa/Ueda 2019, Eq. (5)
def hig_faktor(j, sign, achse):
    # U_j^+-(k) = P_j^+- e^{-+ik} + P_j^-+ (Eq. 2: Spin +- springt um +-e_j; Entwicklung U_j^+- ~ sigma_0 -+ i P_j^+- k),
    # P_j^+- = (sigma_0 +- sigma_j)/2; achse = Index von u (k1, k2, q3 = k3/2)
    Pp = (I2 + sign * PAULI[j]) / 2
    Pm = (I2 - sign * PAULI[j]) / 2
    f = np.zeros(3, int)
    f[achse] = -sign
    return W1.Fourier(np.array([Pm, Pp]), np.array([[0, 0, 0], list(f)]))


def higashikawa():
    U1 = {s: hig_faktor(0, s, 0) for s in (1, -1)}
    U2 = {s: hig_faktor(1, s, 1) for s in (1, -1)}
    U3 = {s: hig_faktor(2, s, 2) for s in (1, -1)}  # halbe Verschiebung = ganze auf dem feinen Gitter (q3 = k3/2)
    # U(k) := U1^-(k1) U_h3^-(k3) U2^-(k2) U_h3^+(k3) U1^+(k1) U_h3^-(k3) U2^+(k2) U_h3^+(k3)   (Eq. 5, Matrixprodukt)
    return kette([U1[-1], U3[-1], U2[-1], U3[1], U1[1], U3[-1], U2[1], U3[1]])


def w3_box(aut, u0, L, N):
    t1 = (np.arange(N) + 0.5) / N
    T = np.stack(np.meshgrid(t1, t1, t1, indexing="ij"), -1).reshape(-1, 3)
    vol = float(np.prod(L))
    acc = 0.0 + 0.0j
    for i in range(0, len(T), 4096):
        u = np.asarray(u0)[None, :] + T[i:i + 4096] * np.asarray(L)[None, :]
        U, dU = aut.UdU(u)
        Ud = np.conj(np.transpose(U, (0, 2, 1)))
        X = [Ud @ dU[j] for j in range(3)]
        K = X[1] @ X[2] - X[2] @ X[1]
        acc += np.einsum("nij,nji->n", X[0], K).sum()
    v = acc * vol / len(T) / (8 * np.pi ** 2)
    return float(v.real), float(v.imag)


def rand_abw(aut, u0, L, wert, n=24):
    # max ||U - wert|| auf den sechs Seitenflaechen der Box
    g = (np.arange(n) + 0.5) / n
    A, Bm = np.meshgrid(g, g, indexing="ij")
    A, Bm = A.ravel(), Bm.ravel()
    pts = []
    for ax in range(3):
        for s in (0.0, 1.0):
            t = np.zeros((len(A), 3))
            o = [x for x in range(3) if x != ax]
            t[:, ax] = s
            t[:, o[0]] = A
            t[:, o[1]] = Bm
            pts.append(t)
    t = np.concatenate(pts)
    u = np.asarray(u0)[None, :] + t * np.asarray(L)[None, :]
    return float(np.abs(aut.U(u) - wert[None]).max())


def fib_dirs(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], -1)


def kegel_isotropie(aut, k_betrag, skala=(1.0, 1.0, 0.5), n=400):
    dirs = fib_dirs(n)
    u = k_betrag * dirs * np.asarray(skala)[None, :]
    ev = np.linalg.eigvals(aut.U(u))
    dphi = np.abs(np.angle(ev[:, 0] / ev[:, 1]))
    v = dphi / (2 * k_betrag)
    return {"v_mittel": float(v.mean()), "std_rel": float(v.std() / v.mean()),
            "spann_rel": float((v.max() - v.min()) / v.mean())}


# ---------------------------------------------------------------- allgemeine endlichreichweitige Unitaere (Suche)
F15 = np.array([[0, 0, 0], [1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1],
                [1, 1, 1], [-1, -1, -1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [1, -1, 1], [-1, -1, 1], [1, 1, -1]])


class Koeff:
    """Alle Fourier-Koeffizienten von U^dag U - I fuer U = sum_f A_f exp(i u.f) (exakt), mit analytischer Jacobi-Matrix
    nach (Re A, Im A)."""

    def __init__(self, F, N):
        F = np.asarray(F, int)
        keys, ii, jj, kk = {}, [], [], []
        for i in range(len(F)):
            for j in range(len(F)):
                d = tuple(int(x) for x in (F[i] - F[j]))
                if d not in keys:
                    keys[d] = len(keys)
                ii.append(i)
                jj.append(j)
                kk.append(keys[d])
        self.ii, self.jj, self.kk, self.N, self.nf = np.array(ii), np.array(jj), np.array(kk), N, len(F)
        self.nk = len(keys)
        self.M = np.zeros((len(keys), len(ii)))
        self.M[kk, np.arange(len(ii))] = 1.0
        self.target = np.zeros((len(keys), N * N), dtype=complex)
        self.target[keys[(0, 0, 0)]] = np.eye(N).ravel()
        P = len(ii)
        p, a, b, c = [x.ravel() for x in np.meshgrid(np.arange(P), np.arange(N), np.arange(N), np.arange(N), indexing="ij")]
        N2 = N * N
        # Teil 1 (nach A_i): dQ[c, b] / dA_i[a, b] = conj(A_j[a, c])
        self.r1 = self.kk[p] * N2 + c * N + b
        self.c1 = self.ii[p] * N2 + a * N + b
        self.g1 = (self.jj[p], a, c)
        # Teil 2 (nach A_j): dQ[b, e] / dA_j[a, b] = A_i[a, e]   (hier e -> c)
        self.r2 = self.kk[p] * N2 + b * N + c
        self.c2 = self.jj[p] * N2 + a * N + b
        self.g2 = (self.ii[p], a, c)

    def coeffs(self, A):
        Q = np.einsum("pji,pjk->pik", A[self.jj].conj(), A[self.ii])
        return self.M @ Q.reshape(-1, self.N * self.N) - self.target

    def jac(self, A):
        n_r, n_c = self.nk * self.N * self.N, self.nf * self.N * self.N
        v1 = np.conj(A[self.g1])
        v2 = A[self.g2]
        Gre = np.zeros((n_r, n_c), complex)
        Gim = np.zeros((n_r, n_c), complex)
        np.add.at(Gre, (self.r1, self.c1), v1)
        np.add.at(Gre, (self.r2, self.c2), v2)
        np.add.at(Gim, (self.r1, self.c1), 1j * v1)
        np.add.at(Gim, (self.r2, self.c2), -1j * v2)
        return np.block([[Gre.real, Gim.real], [Gre.imag, Gim.imag]])


def lm_suche(N, nstarts, seed, maxfev):
    unit = Koeff(F15, N)
    m = len(F15) * N * N
    rng = np.random.default_rng(seed)

    def A_of(x):
        return (x[:m] + 1j * x[m:]).reshape(len(F15), N, N)

    def res(x):
        c = unit.coeffs(A_of(x))
        return np.concatenate([c.real.ravel(), c.imag.ravel()])

    out = []
    for s in range(nstarts):
        x0 = rng.standard_normal(2 * m)
        x0 *= np.sqrt(N) / np.linalg.norm(x0)
        t0 = time.time()
        r = least_squares(res, x0, jac=lambda x: unit.jac(A_of(x)), method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15,
                          max_nfev=maxfev)
        A = A_of(r.x)
        D = float(np.sum(np.abs(unit.coeffs(A)) ** 2))
        e = {"start": s, "D": D, "nfev": int(r.nfev), "zeit_s": time.time() - t0}
        if D < 1e-20:
            aut = W1.Fourier(A, F15)
            e["treffer"] = True
            e["unitaer_abw"] = unitaer(aut)
            e["spektrum_spannweite"] = W1.trivial_pruefung(aut, B_W)
            e["w3"] = w3_satz(aut, extra=(n_exakt(aut),))
            e["n_exakt"] = n_exakt(aut)
            gewichte = np.sum(np.abs(A) ** 2, axis=(1, 2))
            e["gewichte"] = gewichte.round(6).tolist()
        else:
            e["treffer"] = False
        out.append(e)
    return out


# ---------------------------------------------------------------- 2D Wabengitter (Kitagawa/Berg/Rudner/Demler 2010)
def kitagawa_J(protokoll, j):
    # Schritt j (0, 1, 2): J_j = lambda J, sonst J; 'voll': J -> 0, lambda J T/3 = pi/2 (T = 1)
    if protokoll["art"] == "voll":
        J = [0.0, 0.0, 0.0]
        J[j] = 1.5 * np.pi
    else:
        J = [protokoll["JT"]] * 3
        J[j] = protokoll["lam"] * protokoll["JT"]
    return J


def bulk_U(th1, th2, protokoll, umkehr=False):
    th1, th2 = np.atleast_1d(th1), np.atleast_1d(th2)
    U = np.broadcast_to(np.eye(2, dtype=complex), (len(th1), 2, 2)).copy()
    reihe = [0, 1, 2] if not umkehr else [2, 1, 0]
    for j in reihe:
        J = kitagawa_J(protokoll, j)
        h = -(J[2] + J[0] * np.exp(1j * th1) + J[1] * np.exp(1j * th2))
        a = np.abs(h)
        tau = 1.0 / 3.0
        c = np.cos(a * tau)
        s = np.where(a > 1e-300, np.sin(a * tau) / np.maximum(a, 1e-300), tau)
        E = np.zeros((len(th1), 2, 2), complex)
        E[:, 0, 0] = c
        E[:, 1, 1] = c
        E[:, 0, 1] = -1j * s * h
        E[:, 1, 0] = -1j * s * np.conj(h)
        U = E @ U  # erster Schritt wirkt zuerst
    return U


def baender_und_chern(protokoll, umkehr, Nk=162):
    g = 2 * np.pi * np.arange(Nk) / Nk
    T1, T2 = np.meshgrid(g, g, indexing="ij")
    U = bulk_U(T1.ravel(), T2.ravel(), protokoll, umkehr)
    w, V = np.linalg.eig(U)
    ph = np.angle(w)
    allp = np.sort(np.mod(ph.ravel(), 2 * np.pi))
    d = np.diff(np.concatenate([allp, allp[:1] + 2 * np.pi]))
    o = np.argsort(d)[::-1][:2]
    luecken = []
    for i in o:
        luecken.append({"mitte": float(np.angle(np.exp(1j * (allp[i] + d[i] / 2)))), "breite": float(d[i])})
    c1, c2 = luecken[0]["mitte"], luecken[1]["mitte"]
    # Band "1": Eigenwert, dessen Phase im Bogen von c1 nach c2 (gegen den Uhrzeigersinn) liegt
    arc = np.mod(c2 - c1, 2 * np.pi)
    in1 = np.mod(ph - c1, 2 * np.pi) < arc
    ch = []
    for band in (True, False):
        idx = np.argmax(in1 == band, axis=1)
        ok = bool(np.all((in1 == band).sum(1) == 1))
        u = V[np.arange(len(idx)), :, idx]
        u = u / np.linalg.norm(u, axis=1)[:, None]
        u = u.reshape(Nk, Nk, 2)
        ux = np.roll(u, -1, axis=0)
        uy = np.roll(u, -1, axis=1)
        l1 = np.einsum("abi,abi->ab", u.conj(), ux)
        l2 = np.einsum("abi,abi->ab", u.conj(), uy)
        l1 /= np.abs(l1)
        l2 /= np.abs(l2)
        F = np.angle(l1 * np.roll(l2, -1, axis=0) * np.conj(np.roll(l1, -1, axis=1)) * np.conj(l2))
        C = float(F.sum() / (2 * np.pi))
        ch.append({"C": C, "C_rund": int(np.round(C)), "eindeutig": ok})
    return {"luecken": luecken, "chern": ch, "bogen_band1": [c1, c2], "nk": Nk,
            "min_abstand_null": float(np.abs(np.angle(np.exp(1j * ph))).min()),
            "min_abstand_pi": float(np.abs(np.angle(-np.exp(1j * ph))).min())}


def streifen_U(k, protokoll, W, umkehr=False):
    n2 = 2 * W
    U = np.eye(n2, dtype=complex)
    reihe = [0, 1, 2] if not umkehr else [2, 1, 0]
    for j in reihe:
        J = kitagawa_J(protokoll, j)
        H = np.zeros((n2, n2), complex)
        for n in range(W):
            A, B = 2 * n, 2 * n + 1
            H[A, B] += -(J[2] + J[0] * np.exp(1j * k))
            if n + 1 < W:
                H[A, 2 * (n + 1) + 1] += -J[1]
        H = H + H.conj().T
        e, V = np.linalg.eigh(H)
        E = (V * np.exp(-1j * e / 3.0)[None, :]) @ V.conj().T
        U = E @ U
    return U


def randfluss(protokoll, umkehr, W=40, Nk=400, luecken=None):
    ks = -np.pi + 2 * np.pi * np.arange(Nk + 1) / Nk
    daten = []
    for k in ks:
        U = streifen_U(k, protokoll, W, umkehr)
        T, Z = schur(U, output="complex")
        ph = np.angle(np.diag(T))
        w = np.abs(Z) ** 2
        cell = np.arange(2 * W) // 2
        w_low = w[cell < W // 4].sum(0)
        w_up = w[cell >= W - W // 4].sum(0)
        daten.append((ph, Z, w_low, w_up))
    out = {}
    for L in luecken:
        phi0 = L["mitte"]
        halb = 0.5 * L["breite"]  # innerhalb der halben Lueckenbreite gibt es nur Randzustaende
        n_up = n_low = n_bulk = 0
        for i in range(Nk):
            ph1, Z1, wl1, wu1 = daten[i]
            ph2, Z2, wl2, wu2 = daten[i + 1]
            r1 = np.angle(np.exp(1j * (ph1 - phi0)))
            r2 = np.angle(np.exp(1j * (ph2 - phi0)))
            kand1 = np.where(np.abs(r1) < np.pi / 2)[0]
            kand2 = np.where(np.abs(r2) < np.pi / 2 + 0.3)[0]
            if len(kand1) == 0 or len(kand2) == 0:
                continue
            ov = np.abs(Z1[:, kand1].conj().T @ Z2[:, kand2])
            for a_i, m in enumerate(kand1):
                n = kand2[int(np.argmax(ov[a_i]))]
                if np.sign(r1[m]) != np.sign(r2[n]) and max(abs(r1[m]), abs(r2[n])) < np.pi / 2 and min(abs(r1[m]), abs(r2[n])) < halb:
                    s_phi = 1 if r2[n] > r1[m] else -1
                    s_eps = -s_phi  # Quasienergie eps = -phi / T
                    wl = 0.5 * (wl1[m] + wl2[n])
                    wu = 0.5 * (wu1[m] + wu2[n])
                    if wu > 0.6:
                        n_up += s_eps
                    elif wl > 0.6:
                        n_low += s_eps
                    else:
                        n_bulk += s_eps
        out[f"{phi0:+.4f}"] = {"phi0": phi0, "halbe_luecke": halb, "N_oben": n_up, "N_unten": n_low, "N_bulk": n_bulk}
    return out


# ---------------------------------------------------------------- Teile
def teil_P3(modus, rng):
    res = {"produkte": [], "takt": [], "additiv": [], "higashikawa": {}}
    nprob = 3 if modus == "rauch" else 12
    for N in (2, 3, 4):
        for s in range(nprob):
            fak = []
            for m in range(4):
                fak.append(muenze(haar(N, rng)))
                r = int(rng.integers(1, N))
                Q = haar(N, rng)[:, :r]
                f = RICHTUNGEN[int(rng.integers(len(RICHTUNGEN)))] * int(rng.choice([-1, 1]))
                fak.append(teilschiebung(Q @ Q.conj().T, f))
            for umk in (False, True):
                aut = kette(fak[::-1] if not umk else fak)
                ne = n_exakt(aut)
                e = {"N": N, "probe": s, "umkehr": umk, "nfreq": int(len(aut.F)), "n_exakt": ne,
                     "unitaer_abw": unitaer(aut), "w3": w3_satz(aut, extra=(ne,))}
                res["produkte"].append(e)
    print(f"[P3] Produkte fertig: {len(res['produkte'])}", flush=True)
    for theta in ((np.pi / 2, np.pi / 3, 0.4) if modus == "haupt" else (np.pi / 3,)):
        for umk in (False, True):
            t0 = time.time()
            aut, nschritte = dreieckstakt(theta, umk)
            ne = n_exakt(aut)
            e = {"theta": theta, "umkehr": umk, "schritte": nschritte, "nfreq": int(len(aut.F)), "n_exakt": ne,
                 "unitaer_abw": unitaer(aut), "w3": w3_satz(aut, extra=(ne,)), "zeit_s": None}
            e["zeit_s"] = time.time() - t0
            res["takt"].append(e)
            print(f"[P3] Dreieckstakt theta={theta:.4f} umkehr={umk}: n_exakt={ne} t={e['zeit_s']:.1f}s", flush=True)
    # Additivitaet mit der quasilokalen Grad-1-Abbildung aus Teil 1
    for s in range(2 if modus == "rauch" else 4):
        fak = []
        for m in range(3):
            fak.append(muenze(haar(2, rng)))
            Q = haar(2, rng)[:, :1]
            f = RICHTUNGEN[int(rng.integers(len(RICHTUNGEN)))]
            fak.append(teilschiebung(Q @ Q.conj().T, f))
        R = kette(fak)
        for lab, aut in (("S1*R", W1.Produkt(W1.Grad1(2.0, 1), R)), ("R*S1", W1.Produkt(R, W1.Grad1(2.0, 1))),
                         ("R", R)):
            res["additiv"].append({"probe": s, "art": lab, "w3": w3_satz(aut)})
    print("[P3] Additivitaet fertig", flush=True)
    # Higashikawa u. a.
    H = higashikawa()
    hz = {"nfreq": int(len(H.F)), "n_exakt": n_exakt(H), "unitaer_abw": unitaer(H)}
    hz["w3_ganzer_feiner_torus"] = w3_satz(H, extra=(n_exakt(H),))
    hz["rand_abw_halbbox_minus_sigma0"] = rand_abw(H, (-np.pi, -np.pi, -np.pi / 2), (2 * np.pi, 2 * np.pi, np.pi), -I2)
    hz["rand_abw_andere_halbbox_minus_sigma0"] = rand_abw(H, (-np.pi, -np.pi, np.pi / 2), (2 * np.pi, 2 * np.pi, np.pi),
                                                         -I2)
    hz["w3_halbbox"] = {str(N): w3_box(H, (-np.pi, -np.pi, -np.pi / 2), (2 * np.pi, 2 * np.pi, np.pi), N)
                        for N in (16, 32, 48, 64)}
    hz["w3_andere_halbbox"] = {str(N): w3_box(H, (-np.pi, -np.pi, np.pi / 2), (2 * np.pi, 2 * np.pi, np.pi), N)
                               for N in (16, 32, 48, 64)}
    # Nachbaupruefung an der Quelle: cos eps(k) = Tr U / 2 = 2 cos^2(k1/2) cos^2(k2/2) cos^2(k3/2) - 1 (S. 2), k3 = 2 q3
    uz = np.random.default_rng(99).uniform(-np.pi, np.pi, (500, 3)) * np.array([1.0, 1.0, 1.0])
    trh = np.trace(H.U(uz), axis1=1, axis2=2).real / 2
    soll = 2 * np.cos(uz[:, 0] / 2) ** 2 * np.cos(uz[:, 1] / 2) ** 2 * np.cos(uz[:, 2]) ** 2 - 1
    hz["eps_formel_abw"] = float(np.abs(trh - soll).max())
    hz["U_bei_k0"] = np.round(H.U(np.zeros((1, 3)))[0], 12).tolist()
    hz["U_bei_k3_2pi"] = np.round(H.U(np.array([[0.0, 0.0, np.pi]]))[0], 12).tolist()
    hz["kegel_k0"] = {str(kb): kegel_isotropie(H, kb) for kb in (1e-4, 0.05, 0.2)}
    w3r = int(np.round(hz["w3_ganzer_feiner_torus"]["gitter"][str(48)]["W3"]))
    if modus == "haupt":
        hz["weyl_feiner_torus"] = W1.weyl_analyse(H, B_W, w3r)
    res["higashikawa"] = hz
    print("[P3] Higashikawa fertig", flush=True)
    return res


def teil_LM(modus, nur_n=None, starts=None):
    res = {}
    cfg = [(2, 4, 3000), (3, 2, 3000)] if modus == "rauch" else [(2, 40, 3000), (3, 30, 3000)]
    if nur_n is not None:
        cfg = [(n, (starts if starts else s), mf) for (n, s, mf) in cfg if n == nur_n]
    for (N, nst, mf) in cfg:
        t0 = time.time()
        res[f"N{N}"] = lm_suche(N, nst, 4100 + N, mf)
        if modus == "rauch":  # Rauchlauf: W3 der Suchtreffer nicht schreiben (Messgroesse von DT1)
            for e in res[f"N{N}"]:
                e.pop("w3", None)
        tr = [e for e in res[f"N{N}"] if e["treffer"]]
        print(f"[LM] N={N}: {len(tr)} Treffer von {nst}, t={time.time() - t0:.1f}s", flush=True)
    return res


PROTOKOLLE = {"voll": {"art": "voll"}, "lam3": {"art": "teil", "JT": 3 * np.pi / 16, "lam": 3.0},
              "lam4": {"art": "teil", "JT": 3 * np.pi / 16, "lam": 4.0}, "lam1": {"art": "teil", "JT": 3 * np.pi / 16, "lam": 1.0}}


def teil_H2(modus):
    res = {}
    W, Nk = (20, 300) if modus == "rauch" else (40, 1200)
    for name, prot in PROTOKOLLE.items():
        for umk in (False, True):
            t0 = time.time()
            b = baender_und_chern(prot, umk)
            e = {"bulk": b}
            if name != "lam1":
                rf = randfluss(prot, umk, W=W, Nk=Nk, luecken=b["luecken"])
                # Rauchlauf: Randfluss (Messgroesse von DT3) nicht schreiben, nur ob er gerechnet wurde
                e["rand"] = rf if modus == "haupt" else {"gerechnet": True, "luecken": len(rf)}
            e["zeit_s"] = time.time() - t0
            res[f"{name}|{'umkehr' if umk else 'vorwaerts'}"] = e
            print(f"[H2] {name} umkehr={umk}: Luecken {[round(L['breite'], 4) for L in b['luecken']]} "
                  f"Chern {[c['C_rund'] for c in b['chern']]} t={e['zeit_s']:.1f}s", flush=True)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teil", choices=["P3", "LM", "H2"], required=True)
    ap.add_argument("--modus", choices=["rauch", "haupt"], required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--lm_n", type=int, default=None)
    ap.add_argument("--lm_starts", type=int, default=None)
    args = ap.parse_args()
    t_start = time.time()
    rng = np.random.default_rng(5150 if args.modus == "haupt" else 51500)
    res = {"teil": args.teil, "modus": args.modus, "numpy": np.__version__}
    if args.teil == "P3":
        res["p3"] = teil_P3(args.modus, rng)
    elif args.teil == "LM":
        res["lm"] = teil_LM(args.modus, args.lm_n, args.lm_starts)
    else:
        res["h2"] = teil_H2(args.modus)
    res["laufzeit_s"] = time.time() - t_start
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(f"fertig, {res['laufzeit_s']:.1f} s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
