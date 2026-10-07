#!/usr/bin/env python3
# QCA-WINDUNG-1 (Runde 41, fmhc-physics). Code-Agent fuer die Leitung claude-primary.
# Windungszahl W3 = (1/24 pi^2) Int d^3u eps^ijk tr(U^dag d_i U U^dag d_j U U^dag d_k U) der Einschritt-Operatoren
# U(u) = Sum_f A_f exp(i u.f), u = k/sqrt3 (Konvention W_at in qca_tetra.py / qca_rueck.py; u -> k ist eine positive
# Streckung und aendert W3 nicht). Dazu: Inversionstest, Weyl-Punkte mit Quasienergie und Chiralitaet (lokaler Grad
# = Vorzeichen von det M, M_lj = Re tr(G_l sigma_j)/2, G_l = Q^dag U^dag d_l U Q / i im Zweifach-Cluster), globale
# Bandbeschriftung (Windung von det U), Netto-Chiralitaet je Luecke.
# Start nur auf der .69 ueber kleintest.sh. Aufruf:
#   windung.py --teil K --modus rauch|haupt --out DATEI.json                       (Kontrollen)
#   windung.py --teil A --modus rauch|haupt --out DATEI.json --ein J1.json ...     (gespeicherte Repraesentanten)
#   windung.py --teil B --modus haupt --out DATEI.json --ein W1.json ...           (Treffer der Wiederholung, A_zusatz)
# Im Modus rauch werden fuer Projekt-Automaten keine W3-Werte, Weyl-Punkte oder Chiralitaeten ausgegeben, nur Zeiten,
# Unitaritaet, Inversion und die Nachbaupruefung bei Gamma (PLAN.md Abschnitt 5).
import argparse
import json
import sys
import time

import numpy as np
from scipy.linalg import schur

SQ3 = np.sqrt(3.0)
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = np.array([SX, SY, SZ])
B_BCC = np.pi * np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], float).T  # Spalten b1, b2, b3: Periodengitter in u
B_WUERFEL = 2 * np.pi * np.eye(3)
GITTER_W3 = (16, 24, 32, 48)
GANZ_TOL = 0.05            # Karte: abs(W3 - round(W3)) < 0,05 beim feinsten Gitter
CUTS = (1.2345678, 1.2345678 + np.pi - 0.4321)
U_REF_T = np.array([0.1234567, 0.2345678, 0.3456789])
TV = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=int)
S_BCC = np.concatenate([TV, -TV])


# ---------------------------------------------------------------- Automaten
class Fourier:
    """U(u) = sum_f A_f exp(i u.f)."""

    def __init__(self, A, freqs):
        self.A = np.asarray(A, complex)
        self.F = np.asarray(freqs, float)
        self.s = self.A.shape[-1]
        self.Af = self.A.reshape(len(self.F), self.s * self.s)

    def UdU(self, u):
        u = np.atleast_2d(u)
        ph = np.exp(1j * (u @ self.F.T))
        U = (ph @ self.Af).reshape(-1, self.s, self.s)
        dU = [((1j * self.F[:, j][None, :] * ph) @ self.Af).reshape(-1, self.s, self.s) for j in range(3)]
        return U, dU

    def U(self, u):
        u = np.atleast_2d(u)
        return (np.exp(1j * (u @ self.F.T)) @ self.Af).reshape(-1, self.s, self.s)


class Grad1:
    """Synthetische Abbildung der Karte: (sin u1, sin u2, sin u3, m - Sum cos u_i) normiert, als SU(2)-Element
    U = (d4 I + i d.sigma)/|d|. vorz = -1 liefert U(-u). Periode 2 pi in jeder Richtung."""

    def __init__(self, m=2.0, vorz=1):
        self.m, self.v, self.s = m, vorz, 2

    def UdU(self, u):
        u = np.atleast_2d(u) * self.v
        sn, cs = np.sin(u), np.cos(u)
        d4 = self.m - cs.sum(1)
        n = np.sqrt(d4 ** 2 + (sn ** 2).sum(1))
        D = d4[:, None, None] * I2 + 1j * np.einsum("ni,ijk->njk", sn, PAULI)
        U = D / n[:, None, None]
        dU = []
        for j in range(3):
            dd = np.zeros_like(sn)
            dd[:, j] = cs[:, j]
            dd4 = sn[:, j]
            dD = dd4[:, None, None] * I2 + 1j * np.einsum("ni,ijk->njk", dd, PAULI)
            dn = (d4 * dd4 + (sn * dd).sum(1)) / n
            dU.append(self.v * (dD / n[:, None, None] - D * (dn / n ** 2)[:, None, None]))
        return U, dU

    def U(self, u):
        return self.UdU(u)[0]


class Produkt:
    def __init__(self, a, b):
        self.a, self.b, self.s = a, b, a.s

    def UdU(self, u):
        Ua, dUa = self.a.UdU(u)
        Ub, dUb = self.b.UdU(u)
        return Ua @ Ub, [dUa[j] @ Ub + Ua @ dUb[j] for j in range(3)]

    def U(self, u):
        return self.a.U(u) @ self.b.U(u)


class Summe:
    def __init__(self, a, b):
        self.a, self.b, self.s = a, b, a.s + b.s

    def _bd(self, X, Y):
        n = X.shape[0]
        Z = np.zeros((n, self.s, self.s), dtype=complex)
        Z[:, :self.a.s, :self.a.s] = X
        Z[:, self.a.s:, self.a.s:] = Y
        return Z

    def UdU(self, u):
        Ua, dUa = self.a.UdU(u)
        Ub, dUb = self.b.UdU(u)
        return self._bd(Ua, Ub), [self._bd(dUa[j], dUb[j]) for j in range(3)]

    def U(self, u):
        return self._bd(self.a.U(u), self.b.U(u))


def weyl_quelle(sign):
    # D'Ariano/Perinotti 2014 Eq. (24), identisch mit weyl_quelle() in qca_rueck.py und weyl_A() in qca_tetra.py
    z = (1 + sign * 1j) / 4
    zc = np.conj(z)
    Ap = [np.array([[zc, 0], [zc, 0]]), np.array([[0, zc], [0, zc]]), np.array([[0, -zc], [0, zc]]),
          np.array([[zc, 0], [-zc, 0]])]
    Am = [np.array([[0, -z], [0, z]]), np.array([[z, 0], [-z, 0]]), np.array([[z, 0], [z, 0]]),
          np.array([[0, z], [0, z]])]
    return np.array(Ap + Am, dtype=complex)


def muenze_schiebung_8(rng):
    # U = X1 S(u) X2 S(u), S(u) = diag(exp(i u.f_a)) ueber die 8 BCC-Richtungen; W3 = 0 [M], Dichte nicht 0
    def zuf_unitaer():
        Z = rng.standard_normal((8, 8)) + 1j * rng.standard_normal((8, 8))
        Q, R = np.linalg.qr(Z)
        return Q * (np.diag(R) / np.abs(np.diag(R)))[None, :]
    teile = []
    for _ in range(2):
        X = zuf_unitaer()
        A = np.zeros((8, 8, 8), dtype=complex)
        for a in range(8):
            A[a][:, a] = X[:, a]
        teile.append(Fourier(A, S_BCC))
    return Produkt(teile[0], teile[1])


# ---------------------------------------------------------------- W3
def gitter_t(N, offset):
    t1 = (np.arange(N) + offset) / N
    return np.stack(np.meshgrid(t1, t1, t1, indexing="ij"), -1).reshape(-1, 3)


def w3_integral(aut, B, N, offset=0.5, chunk=4096):
    T = gitter_t(N, offset)
    vol = abs(np.linalg.det(B))
    acc = 0.0 + 0.0j
    for i in range(0, len(T), chunk):
        U, dU = aut.UdU(T[i:i + chunk] @ B.T)
        Ud = np.conj(np.transpose(U, (0, 2, 1)))
        X = [Ud @ dU[j] for j in range(3)]
        K = X[1] @ X[2] - X[2] @ X[1]
        acc += np.einsum("nij,nji->n", X[0], K).sum()
    val = acc * vol / len(T) / (8 * np.pi ** 2)  # (1/24 pi^2) eps tr(XXX) = (1/8 pi^2) tr(X1 [X2, X3])
    return float(val.real), float(val.imag)


def unitaritaet(aut, B, N=12):
    U = aut.U(gitter_t(N, 0.25) @ B.T)
    return float(np.abs(np.conj(np.transpose(U, (0, 2, 1))) @ U - np.eye(aut.s)).max())


def w3_alle(aut, B, B_alt=None):
    out = {"gitter": {}, "zeit_s": {}}
    for N in GITTER_W3:
        t0 = time.time()
        re, im = w3_integral(aut, B, N)
        out["gitter"][str(N)] = {"W3": re, "im": im}
        out["zeit_s"][str(N)] = time.time() - t0
    fein = out["gitter"][str(GITTER_W3[-1])]["W3"]
    out["W3_fein"] = fein
    out["W3_rund"] = int(np.round(fein))
    out["ganzzahl_abw"] = float(abs(fein - np.round(fein)))
    out["konvergiert"] = bool(out["ganzzahl_abw"] < GANZ_TOL)
    vals = [out["gitter"][str(N)]["W3"] for N in GITTER_W3]
    out["spannweite_ueber_gitter"] = float(max(vals) - min(vals))
    if B_alt is not None:
        # Probe Jacobi-Faktor: Wuerfel [0, 2pi)^3 in u ueberdeckt die primitive Zelle |det B_alt|/|det B| mal
        re, _ = w3_integral(aut, B_alt, 16)
        fak = abs(np.linalg.det(B_alt)) / abs(np.linalg.det(B))
        out["wuerfel_probe"] = {"W3_wuerfel_durch_faktor": re / fak, "faktor": fak}
    return out


# ---------------------------------------------------------------- Inversion
def inversion(aut, rng, n=32):
    s = aut.s
    u = rng.uniform(-np.pi, np.pi, (n, 3))
    Up, Um = aut.U(u), aut.U(-u)
    Is = np.eye(s)
    rows = [np.kron(Up[i].T, Is) - np.kron(Is, Um[i]) for i in range(n)]
    _, sv, vh = np.linalg.svd(np.concatenate(rows))
    rel = sv / max(sv[0], 1e-300)
    null = [vh.conj()[i].reshape(s, s, order="F") for i in range(len(sv)) if rel[i] <= 1e-9]
    out = {"s_min_rel": float(rel[-1]), "s_2_rel": float(rel[-2]), "nullraum": len(null)}
    ja = False
    if null:
        c = rng.standard_normal(len(null)) + 1j * rng.standard_normal(len(null))
        V = sum(ci * Xi for ci, Xi in zip(c, null))
        V = V / np.linalg.norm(V) * np.sqrt(s)
        kond = float(np.linalg.cond(V))
        u2 = rng.uniform(-np.pi, np.pi, (16, 3))
        res = float(max(np.abs(V @ a - b @ V).max() for a, b in zip(aut.U(u2), aut.U(-u2))))
        out.update({"kondition": kond, "rest": res})
        ja = bool(kond < 1e6 and res < 1e-8)
    out["inversion"] = ja
    return out


# ---------------------------------------------------------------- Weyl-Punkte
def paar(aut, u, ziel):
    U, dU = aut.UdU(u[None, :])
    U = U[0]
    T, Z = schur(U, output="complex")
    ph = np.angle(np.diag(T))
    dist = np.abs(np.angle(np.exp(1j * (ph - ziel))))
    o = np.argsort(dist)
    i, k = o[0], o[1]
    Q = Z[:, [i, k]]
    W2 = Q.conj().T @ U @ Q
    phc = float(np.angle(np.trace(W2)))
    e = np.exp(-1j * phc)
    b = np.array([np.real(np.trace(e * W2 @ P) / 2j) for P in PAULI])
    G = [e * (Q.conj().T @ dU[l][0] @ Q) / 1j for l in range(3)]
    M = np.array([[np.real(np.trace(G[l] @ P)) / 2 for P in PAULI] for l in range(3)])
    luecke = float(abs(np.angle(T[i, i] / T[k, k])))
    rest = float(min(abs(np.angle(np.exp(1j * (ph[o[m]] - phc)))) for m in range(2, len(o)))) if len(o) > 2 else float(np.pi)
    return phc, b, M, luecke, rest


def newton(aut, u0, ziel, maxit=40):
    u = np.array(u0, float)
    for _ in range(maxit):
        phc, b, M, luecke, rest = paar(aut, u, ziel)
        if luecke < 1e-12:
            break
        try:
            du = -np.linalg.solve(M.T, b)
        except np.linalg.LinAlgError:
            return None
        st = float(np.linalg.norm(du))
        if not np.isfinite(st):
            return None
        if st > 0.3:
            du *= 0.3 / st
        u = u + du
        ziel = phc
    phc, b, M, luecke, rest = paar(aut, u, ziel)
    if luecke > 1e-9:
        return None
    dM = float(np.linalg.det(M))
    return {"u": u, "phase": phc, "detM": dM, "chi": int(np.sign(dM)), "luecke": luecke, "rest": rest}


def eigenphasen(aut, u, chunk=4096):
    out = []
    for i in range(0, len(u), chunk):
        out.append(np.angle(np.linalg.eigvals(aut.U(u[i:i + chunk]))))
    return np.concatenate(out)


def drehgruppe_T():
    # die 12 eigentlichen Drehungen des Tetraeders (erzeugt von C2x und der 120-Grad-Drehung um (1,1,1))
    gens = [np.diag([1, -1, -1]), np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])]
    els = [np.eye(3, dtype=int)]
    neu = list(els)
    while neu:
        nn = []
        for M in neu:
            for G in gens:
                P = G @ M
                if not any((P == X).all() for X in els):
                    els.append(P)
                    nn.append(P)
        neu = nn
    return els


ROT_T = drehgruppe_T()


def bahn_ergaenzen(aut, funde):
    # Weyl-Punkte eines T-kovarianten Automaten liegen in T-Bahnen (U(Rk) = V U(k) V^dag). Jeder Fund wird auf seine
    # Bildpunkte R u abgebildet und dort geprueft (Paarluecke <= 1e-9 an der Bildstelle, gleiche Phase); nur
    # bestaetigte Bildpunkte kommen dazu. Fuer nicht kovariante Automaten bestaetigt sich in der Regel keiner.
    extra = []
    for f in funde:
        for R in ROT_T[1:]:
            u2 = R @ f["u"]
            phc, b, M, luecke, rest = paar(aut, u2, f["phase"])
            if luecke <= 1e-9 and abs(np.angle(np.exp(1j * (phc - f["phase"])))) < 1e-6:
                dM = float(np.linalg.det(M))
                extra.append({"u": u2, "phase": phc, "detM": dM, "chi": int(np.sign(dM)), "luecke": luecke, "rest": rest})
    return funde + extra


U_HOCHSYM = np.array([[0, 0, 0], [0, 0, np.pi], [np.pi / 2] * 3, [np.pi / 2, np.pi / 2, 3 * np.pi / 2]])  # Gamma, H, P, P'


def hochsym_punkte(aut):
    # Zweifach-Cluster an Gamma, H, P, P' direkt (dort erzwingt T Entartungen); nur exakt entartete Paare
    out = []
    for u0 in U_HOCHSYM:
        U = aut.U(u0[None, :])[0]
        T, _ = schur(U, output="complex")
        ph = np.angle(np.diag(T))
        for i in range(len(ph)):
            for j in range(i + 1, len(ph)):
                if abs(np.angle(np.exp(1j * (ph[i] - ph[j])))) < 1e-9:
                    phc, b, M, luecke, rest = paar(aut, u0.copy(), float(ph[i]))
                    if luecke <= 1e-9:
                        dM = float(np.linalg.det(M))
                        out.append({"u": u0.copy(), "phase": phc, "detM": dM, "chi": int(np.sign(dM)), "luecke": luecke,
                                    "rest": rest})
    return out


def weyl_suche(aut, B, Ng, offset, cuts, max_kand=400, gmax=0.3):
    s = aut.s
    T = gitter_t(Ng, offset)
    u = T @ B.T
    ph = eigenphasen(aut, u)
    funde, n_start = hochsym_punkte(aut), 0
    for c in cuts:
        psi = np.sort(np.mod(ph - c, 2 * np.pi), axis=1)
        gaps = np.concatenate([np.diff(psi, axis=1), psi[:, :1] + 2 * np.pi - psi[:, -1:]], axis=1)
        G = gaps.reshape(Ng, Ng, Ng, s)
        for j in range(s):
            g = G[..., j]
            loc = np.ones_like(g, dtype=bool)
            for ax in range(3):
                for sh in (1, -1):
                    loc &= g <= np.roll(g, sh, axis=ax)
            idx = np.argwhere(loc & (g < gmax))
            if len(idx) == 0:
                continue
            vals = g[tuple(idx.T)]
            for o in np.argsort(vals)[:max_kand]:
                lin = int(np.ravel_multi_index(tuple(idx[o]), (Ng, Ng, Ng)))
                p = psi[lin]
                mid = c + ((p[j] + p[j + 1]) / 2 if j < s - 1 else (p[-1] + p[0] + 2 * np.pi) / 2)
                n_start += 1
                r = newton(aut, u[lin], mid)
                if r is not None:
                    funde.append(r)
    funde = zusammenfassen(funde, B)
    if len(funde) > MAX_PUNKTE:
        # Knotenflaechen o. ae. (keine isolierten Weyl-Punkte): keine Bahnergaenzung; die Suche gilt als nicht einfach
        return funde, n_start
    return zusammenfassen(bahn_ergaenzen(aut, funde), B), n_start


MAX_PUNKTE = 400


def bahn_fehlstellen(L, B):
    # beschreibend: wie viele T-Bildpunkte (R u, gleiche Phase) fehlen in der Liste? 0 bei T-invarianter Menge
    if not L:
        return 0
    Binv = np.linalg.inv(B)
    TT = np.array([w["t"] for w in L])
    PP = np.array([w["phase"] for w in L])
    fehlt = 0
    for w in L:
        for R in ROT_T[1:]:
            t2 = np.mod(Binv @ (R @ w["u"]), 1.0)
            dt = TT - t2
            dt -= np.round(dt)
            dp = np.abs(np.angle(np.exp(1j * (PP - w["phase"]))))
            if not np.any((np.abs(dt).max(1) < 1e-6) & (dp < 1e-6)):
                fehlt += 1
    return fehlt


def zusammenfassen(funde, B):
    Binv = np.linalg.inv(B)
    liste, TT, PP = [], [], []
    for f in funde:
        t = np.mod(Binv @ f["u"], 1.0)
        treffer = []
        if TT:
            dt = np.asarray(TT) - t
            dt -= np.round(dt)
            dp = np.abs(np.angle(np.exp(1j * (np.asarray(PP) - f["phase"]))))
            treffer = np.where((np.abs(dt).max(1) < 1e-6) & (dp < 1e-6))[0]
        if len(treffer):
            g = liste[int(treffer[0])]
            g["n"] += 1
            g["detM_streu"] = max(g["detM_streu"], abs(f["detM"] - g["detM"]))
        else:
            liste.append({"t": t, "u": B @ t, "phase": f["phase"], "detM": f["detM"], "chi": f["chi"],
                          "luecke": f["luecke"], "rest": f["rest"], "n": 1, "detM_streu": 0.0})
            TT.append(t)
            PP.append(f["phase"])
    return liste


def gleiche_mengen(L1, L2):
    if len(L1) != len(L2):
        return False
    frei = list(range(len(L2)))
    for a in L1:
        tr = None
        for j in frei:
            b = L2[j]
            dt = a["t"] - b["t"]
            dt -= np.round(dt)
            if np.abs(dt).max() < 1e-6 and abs(np.angle(np.exp(1j * (a["phase"] - b["phase"])))) < 1e-6 and a["chi"] == b["chi"]:
                tr = j
                break
        if tr is None:
            return False
        frei.remove(tr)
    return True


def det_phase_pfad(aut, us):
    d = np.linalg.det(aut.U(us))
    st = np.angle(d[1:] / d[:-1])
    return float(st.sum()), float(np.abs(st).max())


def det_windungen(aut, B, nstep=1200):
    u0 = B @ U_REF_T
    out, smax = [], 0.0
    for i in range(3):
        us = u0[None, :] + np.outer(np.linspace(0, 1, nstep + 1), B[:, i])
        th, mx = det_phase_pfad(aut, us)
        out.append(th / (2 * np.pi))
        smax = max(smax, mx)
    return out, smax


def luecken_zuordnung(aut, B, wps, nstep=1500):
    s = aut.s
    if not wps:
        return {"schnitt": None, "netto_je_luecke": [0] * s, "pfad_unabhaengig": True, "max_schritt_det": 0.0}
    phs = np.sort(np.mod([w["phase"] for w in wps], 2 * np.pi))
    d = np.diff(np.concatenate([phs, phs[:1] + 2 * np.pi]))
    j = int(np.argmax(d))
    c = float(phs[j] + d[j] / 2)  # Schnitt in der groessten Luecke der Weyl-Phasen
    u_ref = B @ U_REF_T
    psi_ref = np.sort(np.mod(eigenphasen(aut, u_ref[None, :])[0] - c, 2 * np.pi))
    th_ref = s * c + psi_ref.sum()
    u_mid = B @ np.array([0.61, 0.27, 0.83])
    netto = np.zeros(s, dtype=int)
    pfad_ok, smax = True, 0.0
    for w in wps:
        werte = []
        for weg in ([u_ref, w["u"]], [u_ref, u_mid, w["u"]]):
            th, mx = th_ref, 0.0
            for a, b in zip(weg[:-1], weg[1:]):
                dth, m = det_phase_pfad(aut, a[None, :] + np.outer(np.linspace(0, 1, nstep + 1), b - a))
                th += dth
                mx = max(mx, m)
            smax = max(smax, mx)
            psi = np.sort(np.mod(eigenphasen(aut, w["u"][None, :])[0] - c, 2 * np.pi))
            verschiebung = (th - s * c - psi.sum()) / (2 * np.pi)
            werte.append(verschiebung)
        vs = [int(np.round(x)) for x in werte]
        if vs[0] != vs[1] or max(abs(x - np.round(x)) for x in werte) > 0.05:
            pfad_ok = False
        psi = np.sort(np.mod(eigenphasen(aut, w["u"][None, :])[0] - c, 2 * np.pi))
        pw = np.mod(w["phase"] - c, 2 * np.pi)
        # untere Fensterposition (0-basiert) des entarteten Paares dieses Weyl-Punkts (nach seiner Phase gewaehlt)
        jl = int(np.argmin(np.abs(psi[:-1] - pw) + np.abs(psi[1:] - pw)))
        w["paar_abw"] = float(abs(psi[jl] - pw) + abs(psi[jl + 1] - pw))
        if w["paar_abw"] > 1e-6:
            pfad_ok = False
        g = (jl - vs[0]) % s  # globale Luecke g (0-basiert): zwischen Band g und g+1 (g = s-1: Band s und Band 1 + 2 pi)
        w["luecke_global"] = g + 1
        netto[g] += w["chi"]
    return {"schnitt": c, "netto_je_luecke": netto.tolist(), "pfad_unabhaengig": pfad_ok, "max_schritt_det": smax}


def takt(phase):
    if abs(phase) < 1e-6:
        return "Takt (0)"
    if abs(abs(phase) - np.pi) < 1e-6:
        return "Gegentakt (pi)"
    return "dazwischen"


def weyl_analyse(aut, B, W3_rund):
    out = {}
    t0 = time.time()
    L1, n1 = weyl_suche(aut, B, 40, 0.0, CUTS[:1])
    L2, n2 = weyl_suche(aut, B, 35, 0.5, CUTS[1:])
    out["starts"] = [n1, n2]
    out["anzahl"] = [len(L1), len(L2)]
    out["bahn_fehlt"] = [bahn_fehlstellen(L, B) for L in (L1, L2)]
    out["gleich"] = bool(gleiche_mengen(L1, L2))
    einfach = all(abs(w["detM"]) > 1e-10 and w["rest"] > 1e-6 for w in L1 + L2) and max(len(L1), len(L2)) <= MAX_PUNKTE
    out["einfach"] = bool(einfach)
    out["vollstaendig"] = bool(out["gleich"] and einfach)
    win, smax = det_windungen(aut, B)
    out["det_windungen"] = win
    out["det_max_schritt"] = smax
    out["global"] = bool(all(abs(x) < 0.05 for x in win) and smax < 1.0)
    out["summe_chi"] = int(sum(w["chi"] for w in L1))
    out["s_mal_W3"] = int(aut.s * W3_rund)
    if out["global"] and len(L1) <= MAX_PUNKTE:
        out["luecken"] = luecken_zuordnung(aut, B, L1)
    out["punkte"] = [{"k": (SQ3 * w["u"]).tolist(), "t": w["t"].tolist(), "phase": w["phase"], "chi": w["chi"],
                      "detM_u": w["detM"], "luecke_global": w.get("luecke_global"), "takt": takt(w["phase"]),
                      "n_kand": w["n"], "rest": w["rest"]} for w in L1]
    tab = {}
    for w in L1:
        key = takt(w["phase"])
        tab.setdefault(key, {"anzahl": 0, "chi_plus": 0, "chi_minus": 0, "netto": 0})
        tab[key]["anzahl"] += 1
        tab[key]["chi_plus" if w["chi"] > 0 else "chi_minus"] += 1
        tab[key]["netto"] += w["chi"]
    out["takt_tabelle"] = tab
    out["zeit_s"] = time.time() - t0
    return out


# ---------------------------------------------------------------- Nachbaupruefung bei Gamma (gespeicherte Kennzahlen)
def gamma_cluster(aut, tol=1e-7):
    U, dU = aut.UdU(np.zeros((1, 3)))
    T, Z = schur(U[0], output="complex")
    ph = np.angle(np.diag(T))
    s = len(ph)
    lab = list(range(s))

    def find(i):
        while lab[i] != i:
            i = lab[i]
        return i
    for i in range(s):
        for j in range(i + 1, s):
            if abs(np.angle(np.exp(1j * (ph[i] - ph[j])))) < tol:
                lab[find(i)] = find(j)
    gr = {}
    for i in range(s):
        gr.setdefault(find(i), []).append(i)
    out = []
    for g in gr.values():
        c = float(np.angle(np.mean(np.exp(1j * ph[g]))))
        e = {"phase": c, "m": len(g)}
        if len(g) == 2:
            Q = Z[:, g]
            G = [np.exp(-1j * c) * (Q.conj().T @ dU[l][0] @ Q) / 1j for l in range(3)]
            M = np.array([[np.real(np.trace(G[l] @ P)) / 2 for P in PAULI] for l in range(3)])
            e["chiral_det_k"] = float(np.linalg.det(M)) / SQ3 ** 3  # Ableitung nach k = sqrt3 u wie qca_rueck.py
        out.append(e)
    return out


def nachbau_vergleich(aut, gespeichert):
    meine = gamma_cluster(aut)
    if gespeichert is None:
        return {"geprueft": False}
    pd, cd, fehlt = 0.0, 0.0, 0
    for e in gespeichert:
        cand = [m for m in meine if m["m"] == e["m"]]
        if not cand:
            fehlt += 1
            continue
        m = min(cand, key=lambda x: abs(np.angle(np.exp(1j * (x["phase"] - e["phase"])))))
        pd = max(pd, abs(np.angle(np.exp(1j * (m["phase"] - e["phase"])))))
        if e.get("chiral_det") is not None and m.get("chiral_det_k") is not None:
            cd = max(cd, abs(m["chiral_det_k"] - e["chiral_det"]) / max(abs(e["chiral_det"]), 1e-300))
    return {"geprueft": True, "n_gespeichert": len(gespeichert), "n_mein": len(meine), "fehlt": fehlt,
            "phase_abw_max": pd, "chiral_det_abw_rel_max": cd,
            "ok": bool(fehlt == 0 and len(meine) == len(gespeichert) and pd <= 1e-9 and cd <= 1e-6)}


# ---------------------------------------------------------------- Sammeln gespeicherter Automaten
def cplx_aus(d):
    return np.array(d["re"], float) + 1j * np.array(d["im"], float)


def sammle_repr(pfad, praefix):
    with open(pfad) as fh:
        J = json.load(fh)
    out = []

    def gamma_von(klass):
        try:
            return [{"phase": c["phase"], "m": c["m"], "chiral_det": c.get("chiral_det")} for c in klass["gamma"]["cluster"]]
        except (KeyError, TypeError):
            return None

    def lauf(obj, weg):
        if isinstance(obj, dict):
            if "repr" in obj and isinstance(obj["repr"], dict) and "A" in obj["repr"] and "freqs" in obj["repr"]:
                r = obj["repr"]
                kat = r.get("kategorie", r.get("klasse"))
                gam = None
                if "hits" in obj:
                    for h in obj["hits"]:
                        if h.get("kategorie", h.get("klasse")) == kat:
                            gam = gamma_von(h.get("klass"))
                            break
                elif "klass" in obj:
                    gam = gamma_von(obj["klass"])
                out.append({"name": praefix + "/".join(weg), "A": cplx_aus(r["A"]), "freqs": r["freqs"],
                            "kategorie": kat, "gamma": gam})
            for k, v in obj.items():
                if k not in ("repr", "hits"):
                    lauf(v, weg + [k])
    lauf(J, [])
    return out


def sammle_treffer(pfad, praefix):
    with open(pfad) as fh:
        J = json.load(fh)
    out = []
    for fk, st in J.get("faelle", {}).items():
        for i, h in enumerate(st.get("hits", [])):
            if "A_zusatz" not in h:
                continue
            gam = None
            try:
                gam = [{"phase": c["phase"], "m": c["m"], "chiral_det": c.get("chiral_det")} for c in h["klass"]["gamma"]["cluster"]]
            except (KeyError, TypeError):
                pass
            freqs = S_BCC.tolist() if np.asarray(h["A_zusatz"]["re"]).shape[0] == 8 else \
                np.concatenate([S_BCC, np.zeros((1, 3), dtype=int)]).tolist()
            out.append({"name": f"{praefix}{fk}#{i}", "A": cplx_aus(h["A_zusatz"]), "freqs": freqs,
                        "kategorie": h.get("kategorie"), "gamma": gam, "D_voll": h.get("D_voll"),
                        "gueltig": h.get("gueltig")})
    return out


def trivial_pruefung(aut, B):
    # Spannweite des Spektrums ueber k (0 = konstantes Spektrum, dann keine isolierten Weyl-Punkte und W3 = 0 [M])
    ph = eigenphasen(aut, gitter_t(8, 0.3) @ B.T)
    p0 = np.sort(np.mod(ph[0], 2 * np.pi))
    d = np.diff(np.concatenate([p0, p0[:1] + 2 * np.pi]))
    j = int(np.argmax(d))
    c = p0[j] + d[j] / 2
    ph = np.sort(np.mod(ph - c, 2 * np.pi), axis=1)
    return float((ph.max(0) - ph.min(0)).max())


def analyse(aut, B, B_alt, rng, name, rauch_projekt=False, gamma=None, extra=None, mit_weyl=True):
    t0 = time.time()
    e = {"name": name, "s": int(aut.s)}
    if extra:
        e.update(extra)
    e["unitaer_abw"] = unitaritaet(aut, B)
    e["inversion"] = inversion(aut, rng)
    e["nachbau_gamma"] = nachbau_vergleich(aut, gamma) if gamma is not None else {"geprueft": False}
    e["spektrum_spannweite"] = trivial_pruefung(aut, B)
    # trivial wie einordnen() in qca_rueck.py: Sprunggewicht < 1e-10 (nur Vor-Ort-Term) oder konstantes Spektrum
    if isinstance(aut, Fourier):
        nz = np.abs(aut.F).sum(1) > 0
        e["gewicht_spruenge"] = float(np.sum(np.abs(aut.A[nz]) ** 2))
    else:
        e["gewicht_spruenge"] = None
    e["trivial"] = bool(e["spektrum_spannweite"] < 1e-8 or (e["gewicht_spruenge"] is not None and e["gewicht_spruenge"] < 1e-10))
    w = w3_alle(aut, B, B_alt)
    if rauch_projekt:
        e["w3_zeit_s"] = w["zeit_s"]
    else:
        e["w3"] = w
    if mit_weyl and not e["trivial"]:
        wa = weyl_analyse(aut, B, w["W3_rund"])
        if rauch_projekt:
            # Rauchlauf: nur Zeit und Vollstaendigkeit der Suche, keine Phasen, Chiralitaeten oder W3
            e["weyl_rauch"] = {k: wa[k] for k in ("zeit_s", "anzahl", "gleich", "einfach", "vollstaendig", "starts", "global", "bahn_fehlt")}
        else:
            e["weyl"] = wa
    e["zeit_s"] = time.time() - t0
    return e


def dp_tabelle(aut):
    # QCA-TETRA-1 Tabelle QT3: W(k) an Gamma, P, H, P' (k in Einheiten wie dort, u = k/sqrt3)
    pkt = {"Gamma": [0, 0, 0], "P": [np.pi / 2] * 3, "H": [0, 0, np.pi], "P'": [np.pi / 2, np.pi / 2, 3 * np.pi / 2]}
    out = {}
    for lab, u in pkt.items():
        W = aut.U(np.array([u], float))[0]
        out[lab] = {"plus_I": float(np.abs(W - I2).max()), "minus_I": float(np.abs(W + I2).max())}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teil", choices=["K", "A", "B"], required=True)
    ap.add_argument("--modus", choices=["rauch", "haupt"], required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ein", nargs="*", default=[])
    ap.add_argument("--praefix", nargs="*", default=[])
    ap.add_argument("--nur", type=int, default=None)
    ap.add_argument("--weyl", type=int, default=1)
    args = ap.parse_args()
    t_start = time.time()
    rng = np.random.default_rng(4141 if args.modus == "haupt" else 41410)
    res = {"teil": args.teil, "modus": args.modus, "numpy": np.__version__, "gitter_w3": list(GITTER_W3),
           "ganz_tol": GANZ_TOL, "automaten": []}
    if args.teil == "K":
        kon = [("K-S1 Grad-1 (m=2)", Grad1(2.0, 1), B_WUERFEL, None, "synthetisch"),
               ("K-S1q Quadrat", Produkt(Grad1(2.0, 1), Grad1(2.0, 1)), B_WUERFEL, None, "synthetisch"),
               ("K-S1m U(-u)", Grad1(2.0, -1), B_WUERFEL, None, "synthetisch"),
               ("K-S1inv U(u)+U(-u)", Summe(Grad1(2.0, 1), Grad1(2.0, -1)), B_WUERFEL, None, "synthetisch"),
               ("K-MS8 Muenze x Schiebung zweimal", muenze_schiebung_8(np.random.default_rng(77)), B_BCC, B_WUERFEL,
                "synthetisch"),
               ("DP A+", Fourier(weyl_quelle(1), S_BCC), B_BCC, B_WUERFEL, "DP"),
               ("DP A-", Fourier(weyl_quelle(-1), S_BCC), B_BCC, B_WUERFEL, "DP")]
        for name, aut, B, Balt, art in kon:
            extra = {"art": art}
            if art == "DP":
                extra["qt3"] = dp_tabelle(aut)
            e = analyse(aut, B, Balt, rng, name, extra=extra)
            res["automaten"].append(e)
            w = e["w3"]
            print(f"[K] {name}: W3 je Gitter " + ", ".join(f"{N}:{w['gitter'][str(N)]['W3']:+.6f}" for N in GITTER_W3)
                  + f" inv={e['inversion']['inversion']} t={e['zeit_s']:.1f}s", flush=True)
    else:
        auts = []
        for i, p in enumerate(args.ein):
            pr = args.praefix[i] if i < len(args.praefix) else p.split("/")[-1] + ":"
            auts += sammle_repr(p, pr) if args.teil == "A" else sammle_treffer(p, pr)
        if args.nur is not None:
            auts = auts[:args.nur]
        res["anzahl_gesammelt"] = len(auts)
        for a in auts:
            aut = Fourier(a["A"], a["freqs"])
            extra = {"art": "projekt", "kategorie": a.get("kategorie"), "nfreq": len(a["freqs"])}
            for k in ("D_voll", "gueltig"):
                if k in a:
                    extra[k] = a[k]
            e = analyse(aut, B_BCC, B_WUERFEL, rng, a["name"], rauch_projekt=(args.modus == "rauch"),
                        gamma=a.get("gamma"), extra=extra, mit_weyl=bool(args.weyl))
            res["automaten"].append(e)
            if args.modus == "rauch":
                wr = e.get("weyl_rauch", {})
                print(f"[{args.teil}] {a['name']}: s={aut.s} inv={e['inversion']['inversion']} "
                      f"nachbau={e['nachbau_gamma'].get('ok')} trivial={e['trivial']} weyl_anzahl={wr.get('anzahl')} "
                      f"gleich={wr.get('gleich')} einfach={wr.get('einfach')} bahn_fehlt={wr.get('bahn_fehlt')} starts={wr.get('starts')} t={e['zeit_s']:.1f}s", flush=True)
            else:
                print(f"[{args.teil}] {a['name']}: s={aut.s} fertig t={e['zeit_s']:.1f}s", flush=True)
    res["laufzeit_s"] = time.time() - t_start
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(f"fertig, {res['laufzeit_s']:.1f} s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
