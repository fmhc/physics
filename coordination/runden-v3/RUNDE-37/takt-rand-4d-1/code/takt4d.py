#!/usr/bin/env python3
# TAKT-RAND-4D-1 (Runde 42, fmhc-physics). Code-Agent fuer die Leitung claude-primary.
# Teile:
#   R2: 2D-Kontrolle, Rudner/Lindner/Berg/Levin 2013 (PRX 3, 031005), Schrittplan Eq. (1) auf dem Quadratgitter,
#       Streifen offen in y; Netto-Randfluss je Rand und Luecke (Fensterformel ohne Zustandsverfolgung, PLAN Abschn. 3).
#       Dazu Kontrolle K-chi der Chiralitaetskonvention an U = exp(-i d.sigma), d = (sin k1, sin k2, sin k3).
#   P4: 4D-Schrittplan (Floquet-Fassung des Gitter-Dirac-Modells von Qi/Hughes/Zhang 2008, Eq. 62, aus streng lokalen
#       Schritten), Platte: k1, k2, k3 periodisch, x4 = w endlich (L Lagen). Volumenluecken, Randknoten (Weyl-Punkte der
#       Randzustaende) je Rand und Luecke mit Chiralitaet (lokaler Grad), zwei Suchgitter, Isotropie des tiefsten Kegels.
# Aufruf nur auf der .69 ueber kleintest.sh:
#   takt4d.py --teil R2 --modus rauch|haupt --out DATEI.json
#   takt4d.py --teil P4 --modell P4a|P4b|P4t|P4c|P4cr|P4aL24 --modus rauch|haupt --out DATEI.json
# Im Modus rauch schreibt P4 keine Volumenluecken, Knoten, Zahlen, Chiralitaeten oder Isotropiewerte (nur Zeiten,
# Speicher, Unitaritaet, ob die Kette ohne Ausnahme durchlief).
import argparse
import json
import resource
import sys
import time

import numpy as np
from scipy.linalg import schur

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]
I4 = np.eye(4, dtype=complex)
# fuenf antikommutierende 4x4-Gamma-Matrizen (Gamma_1..Gamma_4 fuer k1..k4, Gamma_5 fuer die Masse)
G1, G2, G3, G4, G5 = np.kron(SX, SX), np.kron(SX, SY), np.kron(SX, SZ), np.kron(SY, I2), np.kron(SZ, I2)
GAM = [G1, G2, G3, G4]


def speicher_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def fib_dirs(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], -1)


def kreis(x):
    return np.angle(np.exp(1j * x))


# ================================================================ Teil R2: Rudner-Modell
RB = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # b1 = -b3 = (a, 0), b2 = -b4 = (0, a)  (Quelle, S. 4)


def rudner_bulk(kx, ky, J, d, umkehr=False):
    # H(k, t) = -Sum_n J_n(t) (e^{i b_n.k} s+ + e^{-i b_n.k} s-) + d sz; fuenf Abschnitte T/5, T = 1 (Quelle Eq. 1)
    n = len(kx)
    U = np.broadcast_to(I2, (n, 2, 2)).copy()
    for s in ([0, 1, 2, 3, 4] if not umkehr else [4, 3, 2, 1, 0]):
        h = np.zeros((n, 2, 2), complex)
        h[:, 0, 0], h[:, 1, 1] = d, -d
        if s < 4:
            ph = np.exp(1j * (RB[s][0] * kx + RB[s][1] * ky))
            h[:, 0, 1] = -J * ph
            h[:, 1, 0] = -J * np.conj(ph)
            E = np.sqrt(J ** 2 + d ** 2)
        else:
            E = abs(d)
        if E > 0:
            step = np.cos(E / 5) * I2[None] - 1j * (np.sin(E / 5) / E) * h
        else:
            step = np.broadcast_to(I2, (n, 2, 2)).copy()
        U = step @ U
    return U


def rudner_streifen(k, J, d, W, umkehr=False):
    # Zelle m = 0..W-1 (y), A(m) = 2m, B(m) = 2m+1; Term e^{i b.k} s+ <-> A(r) - B(r + b)
    n2 = 2 * W
    U = np.eye(n2, dtype=complex)
    for s in ([0, 1, 2, 3, 4] if not umkehr else [4, 3, 2, 1, 0]):
        H = np.zeros((n2, n2), complex)
        if s == 0 or s == 2:
            ph = np.exp(1j * k * RB[s][0])
            for m in range(W):
                H[2 * m, 2 * m + 1] += -J * ph
        elif s == 1 or s == 3:
            dy = RB[s][1]
            for m in range(W):
                if 0 <= m + dy < W:
                    H[2 * m, 2 * (m + dy) + 1] += -J
        H = H + H.conj().T
        H[np.arange(0, n2, 2), np.arange(0, n2, 2)] += d
        H[np.arange(1, n2, 2), np.arange(1, n2, 2)] += -d
        e, V = np.linalg.eigh(H)
        U = ((V * np.exp(-1j * e / 5)[None, :]) @ V.conj().T) @ U
    return U


def volumen_luecken_2d(J, d, umkehr, Nk=240):
    g = -np.pi + 2 * np.pi * (np.arange(Nk) + 0.5) / Nk
    KX, KY = np.meshgrid(g, g, indexing="ij")
    U = rudner_bulk(KX.ravel(), KY.ravel(), J, d, umkehr)
    ph = np.angle(np.linalg.eigvals(U)).ravel()
    return {"halb_0": float(np.abs(ph).min()), "halb_pi": float((np.pi - np.abs(ph)).min())}


def fenster(r, dw):
    return np.where(np.abs(r) < dw, (1 + np.cos(np.pi * r / dw)) / (2 * dw), 0.0)


def randfluss_2d(J, d, umkehr, W, Nk, luecken, h=1e-4):
    # N_b(phi0) = - Int dk Re Tr[P_b g(U) V], V = -i U^dag dU/dk (Quasienergie eps = -phi; Vorzeichen = d eps/dk)
    ks = -np.pi + 2 * np.pi * (np.arange(Nk) + 0.5) / Nk
    zelle = np.arange(2 * W) // 2
    P = {"oben": (zelle >= W // 2).astype(float), "unten": (zelle < W // 2).astype(float), "alle": np.ones(2 * W)}
    acc = {L["name"]: {b: 0.0 for b in P} for L in luecken}
    for k in ks:
        U = rudner_streifen(k, J, d, W, umkehr)
        dU = (rudner_streifen(k + h, J, d, W, umkehr) - rudner_streifen(k - h, J, d, W, umkehr)) / (2 * h)
        V = -1j * U.conj().T @ dU
        T, Z = schur(U, output="complex")
        ph = np.angle(np.diag(T))
        X = Z.conj().T @ V @ Z
        for L in luecken:
            g = fenster(kreis(ph - L["phi0"]), L["dw"])
            if not np.any(g):
                continue
            for b, p in P.items():
                Y = Z.conj().T @ (p[:, None] * Z)
                acc[L["name"]][b] += float(np.real(np.sum(g * np.einsum("nm,mn->n", X, Y))))
    out = {}
    for L in luecken:
        a = acc[L["name"]]
        out[L["name"]] = {"phi0": L["phi0"], "dw": L["dw"], "N_oben": -a["oben"] * 2 * np.pi / Nk,
                          "N_unten": -a["unten"] * 2 * np.pi / Nk, "N_alle": -a["alle"] * 2 * np.pi / Nk}
    return out


R2_FAELLE = {  # J, delta in Einheiten pi/T (Quelle Fig. 2 und Fig. 3)
    "R1_sonder": (2.5, 0.0, False),     # J T / 5 = pi/2, delta = 0: U_F = 1 im Volumen (Fig. 2)
    "R2_anomal": (2.5, 0.5, False),     # Fig. 3c: W0 = 1, Wpi = 1, C = 0
    "R2r_anomal_umkehr": (2.5, 0.5, True),  # Takt 5-4-3-2-1
    "R3_chern": (1.5, 0.5, False),      # Fig. 3b: W0 = 0, Wpi = 1, C = 1
}


def teil_R2(modus):
    res = {}
    W, Nk = (40, 1200) if modus == "haupt" else (24, 300)
    for name, (Jp, dp, umk) in R2_FAELLE.items():
        t0 = time.time()
        J, d = Jp * np.pi, dp * np.pi
        vl = volumen_luecken_2d(J, d, umk)
        luecken = []
        for gname, phi0, halb in (("0", 0.0, vl["halb_0"]), ("pi", np.pi, vl["halb_pi"])):
            if halb >= 0.05:
                luecken.append({"name": gname, "phi0": phi0, "dw": float(min(0.5 * halb, 0.5))})
        e = {"J_pi": Jp, "delta_pi": dp, "umkehr": umk, "volumen": vl, "W": W, "Nk": Nk,
             "fluss": randfluss_2d(J, d, umk, W, Nk, luecken)}
        # Unitaritaet des Streifens an drei k
        e["unitaer_abw"] = float(max(np.abs(rudner_streifen(k, J, d, W, umk).conj().T @ rudner_streifen(k, J, d, W, umk)
                                            - np.eye(2 * W)).max() for k in (0.3, 1.1, -2.0)))
        e["zeit_s"] = time.time() - t0
        res[name] = e
        print(f"[R2] {name}: Luecken {vl} t={e['zeit_s']:.1f}s", flush=True)
    res["K_chi"] = kontrolle_chi()
    print(f"[R2] K-chi: {res['K_chi']}", flush=True)
    return res


# ================================================================ Knoten-Werkzeuge (allgemein)
def eigen_rand(U, ptop, ctol=1e-7):
    """Eigenzerlegung einer Unitaeren (komplexe Schur-Form); in (fast) entarteten Haufen (Phasenabstand < ctol) wird die
    Basis so gedreht, dass sie P_oben diagonalisiert (reine Rand-Zustaende). Rueckgabe: Phasen, Vektoren, Gewicht oben."""
    T, Z = schur(U, output="complex")
    ph = np.angle(np.diag(T))
    o = np.argsort(ph)
    ps = ph[o]
    cuts = np.where(np.diff(ps) > ctol)[0]
    gruppen = np.split(o, cuts + 1)
    if len(gruppen) > 1 and (ps[0] + 2 * np.pi - ps[-1]) < ctol:
        gruppen[0] = np.concatenate([gruppen[-1], gruppen[0]])
        gruppen.pop()
    for g in gruppen:
        if len(g) > 1:
            Zc = Z[:, g]
            Pm = Zc.conj().T @ (ptop[:, None] * Zc)
            _, Vr = np.linalg.eigh(Pm)
            Z[:, g] = Zc @ Vr
    wt = np.real(np.sum(np.abs(Z) ** 2 * ptop[:, None], axis=0))
    return ph, Z, wt


def auswahl(ph, wt, rand, fenster_fn):
    if rand == "oben":
        m = wt > 0.9
    elif rand == "unten":
        m = wt < 0.1
    else:
        m = np.ones(len(ph), bool)
    return np.where(m & fenster_fn(ph))[0]


def paar(model, k, rand, fenster_fn, ziel):
    U, dU = model.UdU(np.asarray(k, float)[None, :])
    U = U[0]
    dU = [x[0] for x in dU]
    ph, Z, wt = eigen_rand(U, model.ptop)
    sel = auswahl(ph, wt, rand, fenster_fn)
    if len(sel) < 2:
        return None
    o = sel[np.argsort(np.abs(kreis(ph[sel] - ziel)))]
    i, j = o[0], o[1]
    Q = Z[:, [i, j]]
    W2 = Q.conj().T @ U @ Q
    phc = float(np.angle(np.trace(W2)))
    e = np.exp(-1j * phc)
    b = np.array([np.real(np.trace(e * W2 @ P) / 2j) for P in PAULI])
    G = [e * (Q.conj().T @ dU[l] @ Q) / 1j for l in range(3)]
    M = np.array([[np.real(np.trace(G[l] @ P)) / 2 for P in PAULI] for l in range(3)])
    spalt = float(abs(kreis(ph[i] - ph[j])))
    return {"phc": phc, "b": b, "M": M, "spalt": spalt, "wt": [float(wt[i]), float(wt[j])]}


def newton(model, k0, rand, fenster_fn, ziel, maxit=40):
    k = np.array(k0, float)
    for _ in range(maxit):
        p = paar(model, k, rand, fenster_fn, ziel)
        if p is None:
            return None
        if p["spalt"] < 1e-12:
            break
        try:
            dk = -np.linalg.solve(p["M"].T, p["b"])
        except np.linalg.LinAlgError:
            return None
        st = float(np.linalg.norm(dk))
        if not np.isfinite(st):
            return None
        if st > 0.3:
            dk *= 0.3 / st
        k = k + dk
        ziel = p["phc"]
    p = paar(model, k, rand, fenster_fn, ziel)
    if p is None or p["spalt"] > 1e-9:
        return None
    dM = float(np.linalg.det(p["M"]))
    V = -p["M"]  # H_eff = Sum_l q_l V_lj sigma_j (U = exp(-i H)); chi = sign det V (H = +q.sigma -> +1)
    sv = np.linalg.svd(V, compute_uv=False)
    return {"k": kreis(k).tolist(), "phase": p["phc"], "detM": dM, "chi": int(np.sign(np.linalg.det(V))),
            "sv": sv.tolist(), "spalt": p["spalt"], "wt": p["wt"]}


class Weyl2:
    """Kontrolle K-chi: U = exp(-i d.sigma), d = (sin k1, sin k2, sin k3); bei Gamma H = +k.sigma (chi = +1)."""

    def __init__(self):
        self.ptop = np.ones(2)

    def UdU(self, k, h=1e-6):
        def U_(kk):
            d = np.sin(kk)
            n = np.linalg.norm(d, axis=1)
            s = np.where(n > 1e-300, np.sin(n) / np.maximum(n, 1e-300), 1.0)
            return np.cos(n)[:, None, None] * I2[None] - 1j * s[:, None, None] * np.einsum("ni,ijk->njk", d, np.array(PAULI))
        U = U_(k)
        dU = []
        for j in range(3):
            e = np.zeros(3)
            e[j] = h
            dU.append((U_(k + e) - U_(k - e)) / (2 * h))
        return U, dU


def kontrolle_chi():
    m = Weyl2()
    alle = lambda ph: np.ones(len(ph), bool)
    out = {}
    for name, k0 in (("Gamma", (0.05, -0.03, 0.02)), ("X1", (np.pi - 0.04, 0.03, -0.02)), ("X12", (np.pi + 0.03, np.pi - 0.02, 0.04)),
                     ("R", (np.pi - 0.03, np.pi + 0.02, np.pi - 0.04))):
        r = newton(m, k0, "alle", alle, 0.0)
        out[name] = None if r is None else {"k": r["k"], "chi": r["chi"], "phase": r["phase"]}
    return out


# ================================================================ Teil P4: 4D-Schrittplan und Platte
def w_j(j, k, a):
    # exp(-i a A_j(k_j)), A_j = sin k Gamma_j - cos k Gamma_5, A_j^2 = 1; Fourier-Anteile nur 0, +-e_j (streng lokal)
    s, c = np.sin(k)[:, None, None], np.cos(k)[:, None, None]
    return np.cos(a) * I4[None] - 1j * np.sin(a) * (s * GAM[j][None] - c * G5[None])


def dw_j(j, k, a):
    s, c = np.sin(k)[:, None, None], np.cos(k)[:, None, None]
    return -1j * np.sin(a) * (c * GAM[j][None] + s * G5[None])


def w5(b):
    return np.cos(b) * I4 - 1j * np.sin(b) * G5


def W4_platte(L, a):
    # A_4 auf L Lagen (offen): (A psi)(w) = -B psi(w+1) - B^dag psi(w-1), B = (Gamma_5 + i Gamma_4)/2, B^2 = 0.
    # A^2 = Projektor auf die Dimere {Q bei w, (1-Q) bei w+1}; ungepaart: (1-Q) bei w = 0 und Q bei w = L-1.
    # exp(-i a A) = (1 - Pi) + cos a Pi - i sin a A: exakt unitaer, Reichweite 1.
    B = (G5 + 1j * G4) / 2
    D = 4 * L
    A = np.zeros((D, D), complex)
    for w in range(L - 1):
        A[4 * w:4 * w + 4, 4 * (w + 1):4 * (w + 1) + 4] = -B
        A[4 * (w + 1):4 * (w + 1) + 4, 4 * w:4 * w + 4] = -B.conj().T
    Pi = A @ A
    return np.eye(D) - Pi + np.cos(a) * Pi - 1j * np.sin(a) * A


MODELLE = {  # tau, M (Masse beta = M tau), Ordnung, L
    "P4a": (0.3, 3.0, "palin", 16),     # QHZ m = -3: C2 = 1, ein Oberflaechenkegel bei Gamma (Quelle Fig. 9a)
    "P4b": (0.3, 1.0, "palin", 16),     # QHZ m = -1: C2 = -3, drei Kegel an den X-Punkten (Fig. 9b)
    "P4t": (0.3, 5.0, "palin", 16),     # QHZ m = -5: C2 = 0 (Gegenprobe: keine Randknoten)
    "P4c": (0.3, 3.0, "vor", 16),       # Takt 1-2-3-4-5 (ein Drehsinn)
    "P4cr": (0.3, 3.0, "rueck", 16),    # Takt 5-4-3-2-1 (umgekehrt)
    "P4aL24": (0.3, 3.0, "palin", 24),  # wie P4a, dickere Platte (Vermerk; Suchgitter 14/11 wegen Laufzeit)
}


class Plan4D:
    def __init__(self, tau, M, ordnung, L):
        self.tau, self.M, self.ordnung, self.L = tau, M, ordnung, L
        self.D = 4 * L
        self.beta = M * tau
        a = tau / 2 if ordnung == "palin" else tau
        self.a = a
        W4 = W4_platte(L, a)
        W5 = np.kron(np.eye(L), w5(self.beta))
        if ordnung == "palin":
            C = W4 @ W5 @ W4
        elif ordnung == "vor":
            C = W5 @ W4
        else:
            C = W4 @ W5
        self.C = C
        self.Cb = C.reshape(L, 4, L, 4)
        self.ptop = (np.arange(self.D) // 4 >= L // 2).astype(float)

    # g_L, g_R aus den Schritten in k1, k2, k3 (blockdiagonal in w)
    def gLR(self, k):
        a = self.a
        w = [w_j(j, k[:, j], a) for j in range(3)]
        dw = [dw_j(j, k[:, j], a) for j in range(3)]
        n = len(k)
        Id = np.broadcast_to(I4, (n, 4, 4))
        z = np.zeros((n, 4, 4), complex)
        if self.ordnung == "palin":
            gL = w[0] @ w[1] @ w[2]
            gR = w[2] @ w[1] @ w[0]
            dgL = [dw[0] @ w[1] @ w[2], w[0] @ dw[1] @ w[2], w[0] @ w[1] @ dw[2]]
            dgR = [w[2] @ w[1] @ dw[0], w[2] @ dw[1] @ w[0], dw[2] @ w[1] @ w[0]]
        elif self.ordnung == "vor":   # U = W5 W4 W3 W2 W1
            gL, dgL = Id, [z, z, z]
            gR = w[2] @ w[1] @ w[0]
            dgR = [w[2] @ w[1] @ dw[0], w[2] @ dw[1] @ w[0], dw[2] @ w[1] @ w[0]]
        else:                         # U = W1 W2 W3 W4 W5
            gL = w[0] @ w[1] @ w[2]
            dgL = [dw[0] @ w[1] @ w[2], w[0] @ dw[1] @ w[2], w[0] @ w[1] @ dw[2]]
            gR, dgR = Id, [z, z, z]
        return gL, gR, dgL, dgR

    def _bm(self, gL, gR):
        X = np.einsum("nac,wcvd,ndb->nwavb", gL, self.Cb, gR, optimize=True)
        return X.reshape(len(gL), self.D, self.D)

    def UdU(self, k):
        k = np.atleast_2d(k)
        gL, gR, dgL, dgR = self.gLR(k)
        U = self._bm(gL, gR)
        dU = [self._bm(dgL[i], gR) + self._bm(gL, dgR[i]) for i in range(3)]
        return U, dU

    def U(self, k):
        k = np.atleast_2d(k)
        gL, gR, _, _ = self.gLR(k)
        return self._bm(gL, gR)

    # Volumen (4D, 4x4)
    def U4(self, k4d):
        a = self.a
        w = [w_j(j, k4d[:, j], a) for j in range(4)]
        W5 = w5(self.beta)[None]
        if self.ordnung == "palin":
            return w[0] @ w[1] @ w[2] @ w[3] @ W5 @ w[3] @ w[2] @ w[1] @ w[0]
        if self.ordnung == "vor":
            return W5 @ w[3] @ w[2] @ w[1] @ w[0]
        return w[0] @ w[1] @ w[2] @ w[3] @ W5


def volumen_4d(model, N=20, chunk=20000):
    g = -np.pi + 2 * np.pi * np.arange(N) / N  # enthaelt 0 und -pi (= pi)
    K = np.stack(np.meshgrid(g, g, g, g, indexing="ij"), -1).reshape(-1, 4)
    m0, mpi, uab = np.inf, np.inf, 0.0
    for i in range(0, len(K), chunk):
        U = model.U4(K[i:i + chunk])
        ph = np.angle(np.linalg.eigvals(U))
        m0 = min(m0, float(np.abs(ph).min()))
        mpi = min(mpi, float((np.pi - np.abs(ph)).min()))
        if i == 0:
            uab = float(np.abs(np.conj(np.transpose(U[:200], (0, 2, 1))) @ U[:200] - I4[None]).max())
    return {"halb_0": m0, "halb_pi": mpi, "N": N, "unitaer_abw": uab}


def fenster_fns(vol):
    f = {}
    if vol["halb_0"] >= 0.05:
        w0 = 0.97 * vol["halb_0"]
        f["0"] = (lambda ph, w0=w0: np.abs(kreis(ph)) < w0, 0.0)
    if vol["halb_pi"] >= 0.05:
        wp = 0.97 * vol["halb_pi"]
        f["pi"] = (lambda ph, wp=wp: np.abs(kreis(ph)) > np.pi - wp, np.pi)
    return f


HOCHSYM = np.array([[a, b, c] for a in (0.0, np.pi) for b in (0.0, np.pi) for c in (0.0, np.pi)])


def suche(model, fns, Ng, offset, smax=0.6, max_kand=60):
    t = (np.arange(Ng) + offset) / Ng
    K = -np.pi + 2 * np.pi * np.stack(np.meshgrid(t, t, t, indexing="ij"), -1).reshape(-1, 3)
    s = {(r, g): np.full(len(K), np.inf) for r in ("oben", "unten") for g in fns}
    mid = {(r, g): np.zeros(len(K)) for r in ("oben", "unten") for g in fns}
    for i0 in range(0, len(K), 256):
        Ub = model.U(K[i0:i0 + 256])
        for j in range(len(Ub)):
            ph, Z, wt = eigen_rand(Ub[j], model.ptop)
            for (r, g) in s:
                fn, c = fns[g]
                sel = auswahl(ph, wt, r, fn)
                if len(sel) < 2:
                    continue
                rr = np.sort(kreis(ph[sel] - c))
                dd = np.diff(rr)
                q = int(np.argmin(dd))
                s[(r, g)][i0 + j] = dd[q]
                mid[(r, g)][i0 + j] = c + 0.5 * (rr[q] + rr[q + 1])
    funde = {f"{r}|{g}": [] for (r, g) in s}
    n_newton = 0
    for (r, g) in s:
        fn, c = fns[g]
        S = s[(r, g)].reshape(Ng, Ng, Ng)
        loc = np.ones_like(S, dtype=bool)
        for ax in range(3):
            for sh in (1, -1):
                loc &= S <= np.roll(S, sh, axis=ax)
        idx = np.where((loc & (S < smax)).ravel())[0]
        idx = idx[np.argsort(s[(r, g)][idx])][:max_kand]
        starts = [(K[i], mid[(r, g)][i]) for i in idx]
        # Hochsymmetrie-Punkte direkt (dort koennen Knoten genau auf dem Gitter liegen)
        for k0 in HOCHSYM:
            Uh = model.U(k0[None])[0]
            ph, Z, wt = eigen_rand(Uh, model.ptop)
            sel = auswahl(ph, wt, r, fn)
            if len(sel) >= 2:
                rr = np.sort(kreis(ph[sel] - c))
                dd = np.diff(rr)
                for q in np.where(dd < 1e-6)[0]:
                    starts.append((k0 + 1e-9, c + rr[q]))
        for (k0, z0) in starts:
            n_newton += 1
            res = newton(model, k0, r, fn, z0)
            if res is not None:
                funde[f"{r}|{g}"].append(res)
    for key in funde:
        funde[key] = zusammenfassen(funde[key])
    return funde, n_newton


def zusammenfassen(L, ktol=1e-5, ptol=1e-6):
    out = []
    for f in L:
        dup = False
        for o in out:
            if np.max(np.abs(kreis(np.array(f["k"]) - np.array(o["k"])))) < ktol and abs(kreis(f["phase"] - o["phase"])) < ptol:
                dup = True
                break
        if not dup:
            out.append(f)
    return out


def gleich(A, B, ktol=1e-5):
    if len(A) != len(B):
        return False
    for f in A:
        if not any(np.max(np.abs(kreis(np.array(f["k"]) - np.array(o["k"])))) < ktol and f["chi"] == o["chi"] for o in B):
            return False
    return True


def isotropie(model, node, rand, fn, qs=(0.01, 0.05, 0.2), n=400):
    dirs = fib_dirs(n)
    out = {}
    for q in qs:
        k = np.array(node["k"])[None, :] + q * dirs
        v = []
        for i0 in range(0, n, 200):
            Ub = model.U(k[i0:i0 + 200])
            for j in range(len(Ub)):
                ph, Z, wt = eigen_rand(Ub[j], model.ptop)
                sel = auswahl(ph, wt, rand, fn)
                if len(sel) < 2:
                    v.append(np.nan)
                    continue
                o = sel[np.argsort(np.abs(kreis(ph[sel] - node["phase"])))]
                v.append(abs(kreis(ph[o[0]] - ph[o[1]])) / (2 * q))
        v = np.array(v)
        ok = bool(np.all(np.isfinite(v)))
        out[str(q)] = {"v_mittel": float(np.nanmean(v)), "spann_rel": float((np.nanmax(v) - np.nanmin(v)) / np.nanmean(v)),
                       "alle_gefunden": ok}
    sv = np.array(node["sv"])
    out["linear_sv"] = sv.tolist()
    out["linear_spann_rel"] = float((sv.max() - sv.min()) / sv.mean())
    return out


def teil_P4(name, modus):
    tau, M, ordnung, L = MODELLE[name]
    t0 = time.time()
    model = Plan4D(tau, M, ordnung, L)
    res = {"modell": name, "tau": tau, "M": M, "ordnung": ordnung, "L": L}
    kz = np.random.default_rng(7).uniform(-np.pi, np.pi, (6, 3))
    Uz = model.U(kz)
    res["unitaer_platte"] = float(np.abs(np.conj(np.transpose(Uz, (0, 2, 1))) @ Uz - np.eye(model.D)[None]).max())
    t1 = time.time()
    vol = volumen_4d(model, N=20 if modus == "haupt" else 8)
    res["zeit_volumen_s"] = time.time() - t1
    res["unitaer_volumen"] = vol["unitaer_abw"]
    fns = fenster_fns(vol)
    if modus == "rauch":
        # Zeitmessung: kleine Gitter, keine Ausgabe von Physikwerten
        t2 = time.time()
        suche(model, fns, 5, 0.0)  # Ergebnis wird im Rauchlauf nicht geschrieben
        res["zeit_suche_5"] = time.time() - t2
        t3 = time.time()
        for j in range(20):
            eigen_rand(model.U(kz[j % 6][None])[0], model.ptop)
        res["zeit_je_zerlegung_s"] = (time.time() - t3) / 20
        res["laufzeit_s"] = time.time() - t0
        res["speicher_mb"] = speicher_mb()
        res["kette_ok"] = True
        return res
    res["volumen"] = vol
    res["luecken_offen"] = sorted(fns)
    t2 = time.time()
    NgA, NgB = (14, 11) if L > 16 else (20, 17)
    res["suchgitter"] = [NgA, NgB]
    fA, nA = suche(model, fns, NgA, 0.0)
    res["zeit_suche_A_s"] = time.time() - t2
    t3 = time.time()
    fB, nB = suche(model, fns, NgB, 0.5)
    res["zeit_suche_B_s"] = time.time() - t3
    res["newton_starts"] = [nA, nB]
    res["knoten_A"] = fA
    res["knoten_B"] = fB
    zus = {}
    voll = True
    for key in fA:
        g = gleich(fA[key], fB[key])
        voll = voll and g
        chis = [f["chi"] for f in fA[key]]
        zus[key] = {"anzahl": len(chis), "netto": int(sum(chis)), "plus": chis.count(1), "minus": chis.count(-1),
                    "gleich_AB": g, "anzahl_B": len(fB[key]), "netto_B": int(sum(f["chi"] for f in fB[key]))}
    res["zaehlung"] = zus
    res["vollstaendig"] = voll
    res["summenregel"] = {g: zus.get(f"oben|{g}", {}).get("netto", 0) + zus.get(f"unten|{g}", {}).get("netto", 0) for g in fns}
    # tiefster Kegel je Rand (kleinstes |Phase| ueber alle offenen Luecken)
    iso = {}
    for r in ("oben", "unten"):
        kand = [(abs(kreis(f["phase"])), g, f) for g in fns for f in fA[f"{r}|{g}"]]
        if not kand:
            iso[r] = None
            continue
        kand.sort(key=lambda x: x[0])
        _, g, f = kand[0]
        iso[r] = {"luecke": g, "knoten": f, "iso": isotropie(model, f, r, fns[g][0])}
    res["tiefster_kegel"] = iso
    res["laufzeit_s"] = time.time() - t0
    res["speicher_mb"] = speicher_mb()
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teil", choices=["R2", "P4"], required=True)
    ap.add_argument("--modell", default=None)
    ap.add_argument("--modus", choices=["rauch", "haupt"], required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    t0 = time.time()
    res = {"teil": args.teil, "modus": args.modus, "numpy": np.__version__}
    if args.teil == "R2":
        res["r2"] = teil_R2(args.modus)
    else:
        res["p4"] = teil_P4(args.modell, args.modus)
    res["laufzeit_s"] = time.time() - t0
    res["speicher_mb"] = speicher_mb()
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(f"fertig, {res['laufzeit_s']:.1f} s, {res['speicher_mb']:.0f} MB", flush=True)


if __name__ == "__main__":
    sys.exit(main())
