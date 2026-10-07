#!/usr/bin/env python3
# SPIEGEL-HAELFTE-1, Runde 42 (fmhc-physics). Code-Agent fuer die Leitung claude-primary.
# Einbahn-Automat W = C_x S_+ auf BCC mit 4 Zustaenden (T:2+2' aus QCA-DIAMANT-4),
#   C_x = e^{i alpha} P_2 + e^{i beta_x} P_2', beta_x je BCC-Knoten fest, gleichverteilt in [beta - W/2, beta + W/2].
# Teil A: die Schreibtischpruefung "FJ = Kompression auf Komponente 2" numerisch nachgerechnet, an der Projekt-Loesung
#   (code/qcad4_repr_2p2s.json und code/qcad4_repr_2p2ss.json, per jq kopiert aus qca-diamant-4/lauf-69/haupt_B{b,c}.json).
#   Gruppenaufbau (closure_T) aus qca-diamant-4/code/qca_diamant.py kopiert.
# Teil B: Paket in Komponente 2 nahe k = 0; Gewicht auf 2, Ausbreitung, Anteil grosser k; FJ-Referenz (iterierte Kompression
#   P_2 W P_2); Bloch-Kontrolle bei W = 0.
# Rahmen: Unter S_+ zerfaellt das BCC-Gitter in vier entkoppelte FCC-Familien (je Zeitschritt ein Nebenklassenwechsel).
#   Gerechnet wird eine Familie (das ist das Raumzeitgitter von Foster/Jacobson). Bezugssystem mit zyklischem Versatz
#   o_t = h_{t mod 4}; die Summe ueber vier Schritte ist null, Paket und Unordnung ruhen daher im Rechengitter.
#   Komponente a springt im Rechengitter um h_a - h_c (c = t mod 4), im n-Gitter um E4[a] - E4[c].
# Start nur auf der .69 ueber kleintest.sh (1 Thread).
# Aufruf: spiegel_haelfte.py --teil A|B|FJ --out DATEI.json [--N N] [--sigma S] [--sigmas S1,S2] [--W w1,w2]
#         [--saaten n] [--saatbasis s] [--schritte T] [--blind] [--bloch]
import argparse
import itertools
import json
import resource
import sys
import time

import numpy as np

TV = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=int)  # t_a, Sprunglaenge sqrt3 (ganzzahlig)
SQ3 = np.sqrt(3.0)
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]
OMEGA = np.exp(2j * np.pi / 3)
C2X = np.diag([1, -1, -1])
R3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
E4 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=int)
ALPHA = 0.0          # Phase auf 2 (Festlegung PLAN 2.2)
BETA = np.pi         # mittlere Phase auf 2' (Gegentakt, wie A = (P_2 - P_2') S_+ in QCA-DIRAC-T-1)
SNAP = (10, 25, 50, 100)


def maxabs(M):
    return float(np.max(np.abs(M)))


def key3(M):
    return tuple(int(x) for x in np.asarray(M).ravel())


# ---------------------------------------------------------------- Gruppe T mit Spinor-Lift (aus qca_diamant.py kopiert)
def closure_T():
    gens = [(C2X, -1j * SX, 0), (R3, 0.5 * (I2 - 1j * (SX + SY + SZ)), 1)]
    start = (np.eye(3, dtype=int), I2.copy(), 0)
    elems = {key3(start[0]): start}
    order = [key3(start[0])]
    frontier = [start]
    fehler = 0
    while frontier:
        new = []
        for (M, U, n) in frontier:
            for (G, V, m) in gens:
                P, W, q = G @ M, V @ U, (m + n) % 3
                k = key3(P)
                if k in elems:
                    P0, U0, n0 = elems[k]
                    if not (np.allclose(W, U0, atol=1e-12) or np.allclose(W, -U0, atol=1e-12)):
                        fehler += 1
                    if n0 != q:
                        fehler += 1
                else:
                    elems[k] = (P, W, q)
                    order.append(k)
                    new.append((P, W, q))
        frontier = new
    return [elems[k] for k in order], fehler


# ---------------------------------------------------------------- Teil A
def lade_repr(pfad):
    with open(pfad) as f:
        d = json.load(f)
    rep = d["repr"]
    A = np.array(rep["A"]["re"]) + 1j * np.array(rep["A"]["im"])
    F = np.array(rep["freqs"], dtype=int)
    return d, A, F


def fj_operator(z, H, sign):
    # (1/2) sum_a z_a P_a mit P_a = (1 + sign * h_a.sigma)/2 (sign = +1: FJ rechtshaendig, -1: P-quer)
    out = np.zeros((2, 2), dtype=complex)
    for a in range(4):
        P = 0.5 * (I2 + sign * sum(H[a, j] * PAULI[j] for j in range(3)))
        out += 0.5 * z[a] * P
    return out


def spin_richtungen(V):
    # V: 2x4, Spalte a = v_a; m_a = 2 <v_a|sigma|v_a>
    return np.array([[2 * float(np.real(np.vdot(V[:, a], PAULI[j] @ V[:, a]))) for j in range(3)] for a in range(4)])


def bargmann(P):
    return complex(P[0, 1] * P[1, 2] * P[2, 0])


def teil_a_repr(pfad, darst, rng):
    d, A, F = lade_repr(pfad)
    out = {"datei": pfad, "fall": d.get("fall"), "quelle": d.get("quelle")}
    plus = [int(np.where((F == t).all(1))[0][0]) for t in TV]
    minus = [int(np.where((F == -t).all(1))[0][0]) for t in TV]
    wp = float(sum(np.sum(np.abs(A[i]) ** 2) for i in plus))
    wm = float(sum(np.sum(np.abs(A[i]) ** 2) for i in minus))
    sgn = 1 if wp >= wm else -1
    idx = plus if sgn > 0 else minus
    out.update({"gewicht_S+": wp, "gewicht_S-": wm, "richtung": "S+" if sgn > 0 else "S-"})
    Aa = A[idx]
    H = sgn * TV / SQ3
    C = Aa.sum(0)
    P2rep = np.diag([1, 1, 0, 0]).astype(complex)
    out["C_unitaer_abw"] = maxabs(C.conj().T @ C - np.eye(4))
    out["C_P2_kommutator"] = maxabs(C @ P2rep - P2rep @ C)
    al = float(np.angle(np.trace(C[:2, :2]) / 2))
    be = float(np.angle(np.trace(C[2:, 2:]) / 2))
    out["phase_2"], out["phase_2s"] = al, be
    out["C_ist_Phase_auf_2_abw"] = maxabs(C[:2, :2] - np.exp(1j * al) * I2)
    out["C_ist_Phase_auf_2s_abw"] = maxabs(C[2:, 2:] - np.exp(1j * be) * I2)
    Pi = [C.conj().T @ Aa[a] for a in range(4)]
    out["Pi_projektor_abw"] = max(maxabs(Pi[a] @ Pi[b] - (Pi[a] if a == b else 0)) for a in range(4) for b in range(4))
    out["Pi_summe_abw"] = maxabs(sum(Pi) - np.eye(4))
    ps = []
    for a in range(4):
        w, v = np.linalg.eigh(0.5 * (Pi[a] + Pi[a].conj().T))
        ps.append(v[:, int(np.argmax(w))])
    Pm = np.array(ps).T
    out["Pm_unitaer_abw"] = maxabs(Pm.conj().T @ Pm - np.eye(4))
    P2s = Pm.conj().T @ P2rep @ Pm
    out["P2_diag_abw_von_1/2"] = maxabs(np.diag(P2s) - 0.5)
    off = np.abs(P2s[~np.eye(4, dtype=bool)]) ** 2
    out["P2_off_betrag2_min_max"] = [float(off.min()), float(off.max())]
    V = Pm[:2, :].copy()
    Vs = Pm[2:, :].copy()
    out["VVdag_abw"] = maxabs(V @ V.conj().T - I2)
    out["VdagV_minus_P2_abw"] = maxabs(V.conj().T @ V - P2s)
    m2 = spin_richtungen(V)
    m2s = spin_richtungen(Vs)
    out["spin_2_mal_h"] = [float(m2[a] @ H[a]) for a in range(4)]
    out["spin_2s_mal_h"] = [float(m2s[a] @ H[a]) for a in range(4)]
    out["spin_betrag_abw"] = max(abs(float(np.linalg.norm(m2[a])) - 1) for a in range(4))
    # Bargmann-Invarianten (eichinvariant) gegen FJ-Spinoren laengs +h_a bzw. -h_a
    b_rep = bargmann(P2s)
    gfj = {}
    for nm, sg in (("plus_h", 1), ("minus_h", -1)):
        vecs = []
        for a in range(4):
            Pa = 0.5 * (I2 + sg * sum(H[a, j] * PAULI[j] for j in range(3)))
            w, v = np.linalg.eigh(Pa)
            vv = v[:, int(np.argmax(w))] * np.exp(1j * rng.uniform(0, 2 * np.pi))  # beliebige Phasenwahl
            vecs.append(vv / np.sqrt(2))
        Vf = np.array(vecs).T
        G = Vf.conj().T @ Vf
        gfj[nm] = {"bargmann": [b_rep.real, b_rep.imag], "bargmann_fj": [bargmann(G).real, bargmann(G).imag],
                   "bargmann_abw": abs(bargmann(G) - b_rep)}
        # Eichung D (diagonal) mit D^dag G D = P2s, wenn die Invarianten passen
        dph = np.ones(4, dtype=complex)
        for b in range(1, 4):
            dph[b] = (P2s[0, b] / G[0, b]) / abs(P2s[0, b] / G[0, b])
        D = np.diag(dph)
        gfj[nm]["eichung_abw"] = maxabs(D.conj().T @ G @ D - P2s)
    out["fj_vergleich"] = gfj
    # saubere (exakte) Fassung fuer Teil B: Gram-Projektor der FJ-Spinoren mit der Haendigkeit der Projekt-Loesung
    chir = "plus_h" if gfj["plus_h"]["bargmann_abw"] < gfj["minus_h"]["bargmann_abw"] else "minus_h"
    sg = 1 if chir == "plus_h" else -1
    vecs = []
    for a in range(4):
        Pa = 0.5 * (I2 + sg * sum(H[a, j] * PAULI[j] for j in range(3)))
        w, v = np.linalg.eigh(Pa)
        vecs.append(v[:, int(np.argmax(w))] / np.sqrt(2))
    Vc = np.array(vecs).T
    P2c = Vc.conj().T @ Vc
    wq, xq = np.linalg.eigh(np.eye(4) - P2c)
    Vcs = xq[:, wq > 0.5].conj().T
    out["haendigkeit_2_relativ_zu_h"] = chir
    out["sauber_VVdag_abw"] = maxabs(Vc @ Vc.conj().T - I2)
    out["sauber_P2_projektor_abw"] = maxabs(P2c @ P2c - P2c)
    out["sauber_gegen_repr_bargmann_abw"] = gfj[chir]["bargmann_abw"]
    out["sauber_gegen_repr_nach_eichung_abw"] = gfj[chir]["eichung_abw"]
    # Phasenunabhaengigkeit: zweite, zufaellige Phasenwahl der Spinoren
    D2 = np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, 4)))
    Vc2 = Vc @ D2
    k = rng.normal(size=3)
    S = np.diag(np.exp(-1j * (H @ k)))
    out["phasenwahl_A_gleich_abw"] = maxabs(Vc2 @ S @ Vc2.conj().T - Vc @ S @ Vc.conj().T)
    out["phasenwahl_P2_eichverwandt_abw"] = maxabs(D2.conj().T @ P2c @ D2 - Vc2.conj().T @ Vc2)
    out["_sauber"] = (P2c, Vc, Vcs)
    # Kompression V S V^dag = (1/2) sum z_a Q_a = FJ (P oder P-quer), zufaellige k
    dev_q, dev_fj_p, dev_fj_m, dev_iter = 0.0, 0.0, 0.0, 0.0
    for _ in range(20):
        k = rng.normal(size=3) * rng.uniform(0.01, 3.0)
        z = np.exp(-1j * (H @ k))
        S = np.diag(z)
        comp = V @ S @ V.conj().T
        Q = sum(0.5 * z[a] * 2 * np.outer(V[:, a], V[:, a].conj()) for a in range(4))
        dev_q = max(dev_q, maxabs(comp - Q))
        dev_fj_p = max(dev_fj_p, maxabs(comp - fj_operator(z, H, 1)))
        dev_fj_m = max(dev_fj_m, maxabs(comp - fj_operator(z, H, -1)))
        Wk = (np.exp(1j * ALPHA) * P2s + np.exp(1j * BETA) * (np.eye(4) - P2s)) @ S
        X = np.eye(4, dtype=complex)
        Y = np.eye(2, dtype=complex)
        for t in range(1, 11):
            X = P2s @ Wk @ P2s @ X
            Y = comp @ Y
            dev_iter = max(dev_iter, maxabs(X - np.exp(1j * ALPHA * t) * V.conj().T @ Y @ V))
    out["kompression_gleich_halbe_summe_Q_abw"] = dev_q
    out["kompression_minus_FJ_P_abw"] = dev_fj_p
    out["kompression_minus_FJ_Pquer_abw"] = dev_fj_m
    out["iterierte_kompression_minus_FJ_hoch_t_abw"] = dev_iter
    # T-Kovarianz: Darstellung in der Verschiebungsbasis monomial, P2s vertauscht
    T, fehler = closure_T()
    cov_mono, cov_p2, cov_S = 0.0, 0.0, 0.0
    for (R, U, n) in T:
        if darst == "2+2'":
            Vr = np.zeros((4, 4), dtype=complex)
            Vr[:2, :2] = U
            Vr[2:, 2:] = OMEGA ** n * U
        else:
            Vr = np.zeros((4, 4), dtype=complex)
            Vr[:2, :2] = U
            Vr[2:, 2:] = OMEGA ** (2 * n) * U
        Vsb = Pm.conj().T @ Vr @ Pm
        perm = []
        for a in range(4):
            tgt = R @ (sgn * TV[a])
            perm.append(int(np.where((sgn * TV == tgt).all(1))[0][0]))
        Mabs = np.zeros((4, 4))
        for a in range(4):
            Mabs[perm[a], a] = 1.0
        cov_mono = max(cov_mono, maxabs(np.abs(Vsb) - Mabs))
        cov_p2 = max(cov_p2, maxabs(Vsb @ P2s - P2s @ Vsb))
        k = rng.normal(size=3)
        S = np.diag(np.exp(-1j * (H @ k)))
        S2 = np.diag(np.exp(-1j * (H @ (R @ k))))
        cov_S = max(cov_S, maxabs(Vsb @ S @ Vsb.conj().T - S2))
    out["T_ordnung"], out["T_konsistenzfehler"] = len(T), fehler
    out["kov_monomial_abw"], out["kov_P2_abw"], out["kov_S_abw"] = cov_mono, cov_p2, cov_S
    # Kovarianz der sauberen Fassung: monomiale Darstellung V_m(g)|b> = phi_b |pi(b)>, phi_b = <n_pi(b)|U|n_b>
    # (Betrag 1 pruefen); P2c muss mit V_m(g) vertauschen, und V_m S(k) V_m^dag = S(Rk).
    P2c, Vc, Vcs = out["_sauber"]
    cphi, cp2, cs = 0.0, 0.0, 0.0
    for (R, U, n) in T:
        perm = []
        for a in range(4):
            tgt = R @ (sgn * TV[a])
            perm.append(int(np.where((sgn * TV == tgt).all(1))[0][0]))
        Vm = np.zeros((4, 4), dtype=complex)
        for b in range(4):
            phi_b = 2 * np.vdot(Vc[:, perm[b]], U @ Vc[:, b])
            cphi = max(cphi, abs(abs(phi_b) - 1))
            Vm[perm[b], b] = phi_b
        cp2 = max(cp2, maxabs(Vm @ P2c - P2c @ Vm))
        k = rng.normal(size=3)
        S = np.diag(np.exp(-1j * (H @ k)))
        S2 = np.diag(np.exp(-1j * (H @ (R @ k))))
        cs = max(cs, maxabs(Vm @ S @ Vm.conj().T - S2))
    out["sauber_kov_phasenbetrag_abw"] = cphi
    out["sauber_kov_P2_abw"] = cp2
    out["sauber_kov_S_abw"] = cs
    del out["_sauber"]
    return out, (P2s, V, Vs), (P2c, Vc, Vcs), sgn


def fib_dirs(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], 1)


def bloch_kegel(P2s, V, Vs, H):
    # Bloch-Analyse W(k) = C diag(e^{-i k.h_a}) (Realraum: Komponente a springt um +h_a), Hop-Einheiten
    C = np.exp(1j * ALPHA) * P2s + np.exp(1j * BETA) * (np.eye(4) - P2s)
    out = {}
    w0 = np.sort(np.angle(np.linalg.eigvals(C)))
    out["eigenphasen_W0"] = [float(x) for x in w0]
    soll = np.sort(np.angle(np.exp(1j * np.array([ALPHA, ALPHA, BETA, BETA]))))
    d = np.abs(np.exp(1j * w0) - np.exp(1j * soll))
    out["eigenphasen_W0_abw"] = float(d.max())
    ks = 1e-5
    sl2, sl2s, g2, g2s = [], [], [], []
    for dv in fib_dirs(60):
        Wk = C @ np.diag(np.exp(-1j * (H @ (ks * dv))))
        lam, vec = np.linalg.eig(Wk)
        for j in range(4):
            dal = abs(np.angle(lam[j] * np.exp(-1j * ALPHA)))
            dbe = abs(np.angle(lam[j] * np.exp(-1j * BETA)))
            v = vec[:, j] / np.linalg.norm(vec[:, j])
            w2 = float(np.real(np.vdot(v, P2s @ v)))
            if dal < dbe:
                sl2.append(dal / ks)
                g2.append(w2)
            else:
                sl2s.append(dbe / ks)
                g2s.append(1 - w2)
    out["steigung_auf_2_min_max"] = [float(min(sl2)), float(max(sl2))]
    out["steigung_auf_2s_min_max"] = [float(min(sl2s)), float(max(sl2s))]
    out["P2_gewicht_kegel_2_min"] = float(min(g2))
    out["P2s_gewicht_kegel_2s_min"] = float(min(g2s))
    out["anzahl_zweige_2_2s"] = [len(sl2), len(sl2s)]
    # Chiralitaet: M_ij = (1/4) sum_a h_ai m_aj (erste Ordnung im V-Bild)
    for nm, VV in (("2", V), ("2s", Vs)):
        m = spin_richtungen(VV)
        M = 0.25 * sum(np.outer(H[a], m[a]) for a in range(4))
        out["M_" + nm + "_det"] = float(np.linalg.det(M))
        out["M_" + nm + "_singulaer"] = [float(x) for x in np.linalg.svd(M, compute_uv=False)]
    return out


# ---------------------------------------------------------------- Gitter (eine FCC-Familie, Rechengitter n in Z_N^3)
class Gitter:
    def __init__(self, N, Hint):
        self.N = N
        self.B = (Hint[1:] - Hint[0]).T.astype(float) / SQ3  # Spalten b_1..b_3 in Hop-Einheiten
        m = np.arange(N) - N // 2
        mi = np.stack(np.meshgrid(m, m, m, indexing="ij"))  # (3,N,N,N), Index = m + N//2
        best_r2 = None
        best_Y = None
        for s in itertools.product((-1, 0, 1), repeat=3):
            mm = mi + N * np.array(s)[:, None, None, None]
            Y = np.tensordot(self.B, mm, axes=(1, 0))
            r2 = (Y ** 2).sum(0)
            if best_r2 is None:
                best_r2, best_Y = r2, Y
            else:
                sel = r2 < best_r2
                best_r2 = np.where(sel, r2, best_r2)
                best_Y = np.where(sel[None], Y, best_Y)
        # Index i <-> m = i - N//2; Paketmitte bei Index N//2 (m = 0); die Rollen wirken periodisch auf den Index
        self.Y = best_Y
        self.r2 = best_r2
        self.zentrum = (N // 2,) * 3
        # Inkugel der Wigner-Seitz-Zelle des N-Uebergitters: halber kuerzester Uebergittervektor
        self.R_in = 0.5 * N * float(min(np.linalg.norm(self.B[:, i]) for i in range(3)))
        # Impulse: k = G q / N, G = 2 pi B^{-T}; minimales Bild
        G = 2 * np.pi * np.linalg.inv(self.B).T
        q = np.fft.fftfreq(N) * N
        qi = np.stack(np.meshgrid(q, q, q, indexing="ij"))
        kb = None
        for s in itertools.product((-1, 0, 1), repeat=3):
            qq = qi / N + np.array(s)[:, None, None, None]
            K = np.tensordot(G, qq, axes=(1, 0))
            k2 = (K ** 2).sum(0)
            kb = k2 if kb is None else np.minimum(kb, k2)
        self.kabs = np.sqrt(kb)
        self.q1 = np.arange(N)

    def phase(self, s):
        # e^{-2 pi i q.s / N} fuer FFT-Index q (numpy-Konvention); s ganzzahlig (3,)
        N = self.N
        e = [np.exp(-2j * np.pi * self.q1 * int(s[i]) / N) for i in range(3)]
        return e[0][:, None, None] * e[1][None, :, None] * e[2][None, None, :]


def verschiebung(psi, t):
    c = t % 4
    out = np.empty_like(psi)
    for a in range(4):
        s = E4[a] - E4[c]
        ax = tuple(i for i in range(3) if s[i] != 0)
        if ax:
            out[a] = np.roll(psi[a], tuple(int(s[i]) for i in ax), axis=ax)
        else:
            out[a] = psi[a]
    return out


def paket(g, sigma, u):
    env = np.exp(-g.r2 / (4 * sigma ** 2))
    psi = u[:, None, None, None] * env[None].astype(complex)
    return psi / np.sqrt(np.vdot(psi, psi).real)


def momente(p, g):
    w = float(p.sum())
    mean = np.array([float((p * g.Y[i]).sum()) / w for i in range(3)])
    R2 = float((p * g.r2).sum()) / w - float(mean @ mean)
    return w, mean, R2


def randgewicht(p, g):
    w = float(p.sum())
    return {"jenseits_0.75Rin": float(p[g.r2 > (0.75 * g.R_in) ** 2].sum()) / w,
            "jenseits_0.9Rin": float(p[g.r2 > (0.9 * g.R_in) ** 2].sum()) / w}


def k_anteil(x, g, kc):
    # Anteil des Gewichts von x (4,N,N,N) mit |k| > kc
    tot = 0.0
    big = 0.0
    mask = g.kabs > kc
    for a in range(4):
        f = np.abs(np.fft.fftn(x[a])) ** 2
        tot += float(f.sum())
        big += float(f[mask].sum())
    return big / tot


def radialprofil(p, g, dr=2.0, rmax=90.0):
    r = np.sqrt(g.r2)
    edges = np.arange(0.0, rmax + dr, dr)
    h, _ = np.histogram(r, bins=edges, weights=p)
    return {"dr": dr, "gewicht": [float(x) for x in h / p.sum()]}


def fj_referenz(g, P2s, psi0, T, kc, schnapp=True):
    ea = np.exp(1j * ALPHA)
    phi = psi0.copy()
    NFJ = [1.0]
    R2 = {}
    fb = {}
    snaps = {}
    w, mean0, r20 = momente((np.abs(phi) ** 2).sum(0), g)
    R2[0] = r20
    fb[0] = k_anteil(phi, g, kc)
    rand = {"jenseits_0.75Rin": 0.0, "jenseits_0.9Rin": 0.0}
    for t in range(T):
        phi = verschiebung(phi, t)
        phi = ea * np.tensordot(P2s, phi, axes=(1, 0))
        n = float(np.vdot(phi, phi).real)
        NFJ.append(n)
        tt = t + 1
        if tt % 5 == 0:
            p = (np.abs(phi) ** 2).sum(0)
            R2[tt] = momente(p, g)[2]
            rg = randgewicht(p, g)
            for kk in rand:
                rand[kk] = max(rand[kk], rg[kk])
        if tt % 10 == 0:
            fb[tt] = k_anteil(phi, g, kc)
        if schnapp and tt in SNAP:
            snaps[tt] = phi.copy()
    return {"N_FJ": NFJ, "R2_FJ": {str(k): v for k, v in R2.items()}, "fbig_FJ": {str(k): v for k, v in fb.items()},
            "rand_FJ": rand}, snaps


def lauf_unordnung(g, P2s, psi0, T, W, saat, kc, snaps, blind, mit_psi=False):
    rng = np.random.default_rng(saat)
    beta = BETA + W * (rng.random((4, g.N, g.N, g.N)) - 0.5)
    Er = np.exp(1j * beta)
    del beta
    ea = np.exp(1j * ALPHA)
    psi = psi0.copy()
    w2 = [1.0]
    normabw = 0.0
    R2 = {}
    mean = {}
    fb = {}
    ov = {}
    rand = {"jenseits_0.75Rin": 0.0, "jenseits_0.9Rin": 0.0}
    rand_tot = {"jenseits_0.75Rin": 0.0, "jenseits_0.9Rin": 0.0}
    p0 = (np.abs(psi0) ** 2).sum(0)
    _, m0, r20 = momente(p0, g)
    R2[0], mean[0] = r20, [float(x) for x in m0]
    fb[0] = k_anteil(psi0, g, kc)
    prof = None
    t0 = time.time()
    for t in range(T):
        psi = verschiebung(psi, t)
        P2psi = np.tensordot(P2s, psi, axes=(1, 0))
        w2.append(float(np.vdot(P2psi, P2psi).real))
        r = (t + 1) % 4
        psi -= P2psi
        psi *= Er[r][None]
        P2psi *= ea
        psi += P2psi
        tt = t + 1
        if tt % 5 == 0:
            ptot = (np.abs(psi) ** 2).sum(0)
            normabw = max(normabw, abs(float(ptot.sum()) - 1.0))
            rgt = randgewicht(ptot, g)
            for kk in rand_tot:
                rand_tot[kk] = max(rand_tot[kk], rgt[kk])
            p = (np.abs(P2psi) ** 2).sum(0)
            ww, mm, rr = momente(p, g)
            R2[tt], mean[tt] = rr, [float(x) for x in mm]
            rg = randgewicht(p, g)
            for kk in rand:
                rand[kk] = max(rand[kk], rg[kk])
            if tt == T:
                prof = radialprofil(p, g)
        if tt % 10 == 0:
            fb[tt] = k_anteil(P2psi, g, kc)
        if tt in snaps:
            ov[tt] = complex(np.vdot(snaps[tt], P2psi))
        del P2psi
    lz = time.time() - t0
    if blind:
        return {"saat": saat, "W": W, "laufzeit_s": lz, "norm_abw_max": normabw, "rand_gesamt": rand_tot}, None
    return {"saat": saat, "W": W, "laufzeit_s": lz, "norm_abw_max": normabw, "w2": w2,
            "R2_2": {str(k): v for k, v in R2.items()}, "schwerpunkt_2": {str(k): v for k, v in mean.items()},
            "fbig_2": {str(k): v for k, v in fb.items()},
            "ueberlapp_FJ": {str(k): [v.real, v.imag] for k, v in ov.items()},
            "rand_2": rand, "rand_gesamt": rand_tot, "radialprofil_2_T": prof}, (psi if mit_psi else None)


def bloch_kontrolle(g, P2s, psi0, T, psi_real_T, w2_real):
    # exakte Bloch-Entwicklung im k-Raum: schrittweise (w2-Kurve) und per Zyklusoperator^(T/4) (Endzustand)
    C = np.exp(1j * ALPHA) * P2s + np.exp(1j * BETA) * (np.eye(4) - P2s)
    ph = {}
    for c in range(4):
        for a in range(4):
            ph[(c, a)] = g.phase(E4[a] - E4[c])
    psih = np.stack([np.fft.fftn(psi0[a]) for a in range(4)])
    nf = float(g.N ** 3)
    w2b = [1.0]
    for t in range(T):
        c = t % 4
        for a in range(4):
            psih[a] *= ph[(c, a)]
        psih = np.tensordot(C, psih, axes=(1, 0))
        x = np.tensordot(P2s, psih, axes=(1, 0))
        w2b.append(float(np.vdot(x, x).real) / nf)
    out = {"w2_bloch": w2b, "w2_abw_max": float(max(abs(a - b) for a, b in zip(w2b, w2_real)))}
    # Zyklusoperator U(q) = W_3 W_2 W_1 W_0, Potenz T/4 per wiederholtem Quadrieren
    if T % 4 == 0:
        Nq = g.N ** 3
        U = np.broadcast_to(np.eye(4, dtype=complex), (Nq, 4, 4)).copy()
        for c in range(4):
            D = np.stack([ph[(c, a)].ravel() for a in range(4)], 1)  # (Nq,4)
            U = D[:, :, None] * U
            U = np.einsum("ab,qbc->qac", C, U)
        n = T // 4
        R = np.broadcast_to(np.eye(4, dtype=complex), (Nq, 4, 4)).copy()
        Pw = U
        while n:
            if n & 1:
                R = np.matmul(Pw, R)
            n >>= 1
            if n:
                Pw = np.matmul(Pw, Pw)
        del U, Pw
        h0 = np.stack([np.fft.fftn(psi0[a]).ravel() for a in range(4)], 1)  # (Nq,4)
        hT = np.einsum("qab,qb->qa", R, h0)
        hreal = np.stack([np.fft.fftn(psi_real_T[a]).ravel() for a in range(4)], 1)
        out["zustand_T_abw_rel"] = float(np.abs(hT - hreal).max() / np.abs(hreal).max())
        out["zustand_T_schritt_gegen_zyklus_abw_rel"] = float(
            np.abs(hT - psih.reshape(4, -1).T).max() / np.abs(hT).max())
    return out


def ru_maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teil", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--N", type=int, default=96)
    ap.add_argument("--sigma", type=float, default=4.5)
    ap.add_argument("--sigmas", default="")
    ap.add_argument("--W", default="")
    ap.add_argument("--saaten", type=int, default=1)
    ap.add_argument("--saatbasis", type=int, default=42000)
    ap.add_argument("--schritte", type=int, default=100)
    ap.add_argument("--blind", action="store_true")
    ap.add_argument("--bloch", action="store_true")
    ap.add_argument("--fjcheck", action="store_true")
    ap.add_argument("--repr", default="qcad4_repr_2p2s.json")
    ap.add_argument("--repr2", default="qcad4_repr_2p2ss.json")
    args = ap.parse_args()
    t_start = time.time()
    res = {"teil": args.teil, "N": args.N, "schritte": args.schritte, "alpha": ALPHA, "beta": BETA,
           "numpy": np.__version__, "argv": sys.argv[1:]}
    rng = np.random.default_rng(4242)
    ta, (P2r, Vr, Vrs), (P2s, V, Vs), sgn = teil_a_repr(args.repr, "2+2'", rng)
    Hint = sgn * TV
    H = Hint / SQ3
    if args.teil == "A":
        res["teil_A_2p2s"] = ta
        ta2, (P2r2, Vr2, Vrs2), _, sgn2 = teil_a_repr(args.repr2, "2+2''", rng)
        res["teil_A_2p2ss"] = ta2
        res["bloch_kegel_sauber"] = bloch_kegel(P2s, V, Vs, H)
        res["bloch_kegel_repr_2p2s"] = bloch_kegel(P2r, Vr, Vrs, H)
        res["bloch_kegel_repr_2p2ss"] = bloch_kegel(P2r2, Vr2, Vrs2, sgn2 * TV / SQ3)
    else:
        res["teil_A_kurz"] = {k: ta[k] for k in ("richtung", "haendigkeit_2_relativ_zu_h", "VdagV_minus_P2_abw",
                                                 "kompression_minus_FJ_P_abw", "kompression_minus_FJ_Pquer_abw",
                                                 "sauber_gegen_repr_nach_eichung_abw", "sauber_kov_P2_abw")}
        g = Gitter(args.N, Hint)
        res["R_in_hop"] = g.R_in
        chi = np.array([1.0, 0.0], dtype=complex)  # Spin auf +z im 2-Block
        u = V.conj().T @ chi
        res["u"] = [[float(x.real), float(x.imag)] for x in u]
        res["P2u_minus_u"] = maxabs(P2s @ u - u)
        if args.teil == "FJ":
            res["fj"] = {}
            for s in [float(x) for x in args.sigmas.split(",") if x]:
                t0 = time.time()
                psi0 = paket(g, s, u)
                kc = 2.0 / s
                r, _ = fj_referenz(g, P2s, psi0, args.schritte, kc, schnapp=False)
                r["laufzeit_s"] = time.time() - t0
                r["kc"] = kc
                res["fj"][str(s)] = r
        else:
            psi0 = paket(g, args.sigma, u)
            kc = 2.0 / args.sigma
            res["sigma"], res["kc"] = args.sigma, kc
            res["anfang_P2_abw"] = maxabs(np.tensordot(P2s, psi0, axes=(1, 0)) - psi0)
            t0 = time.time()
            fj, snaps = fj_referenz(g, P2s, psi0, args.schritte, kc)
            fj["laufzeit_s"] = time.time() - t0
            if args.fjcheck:
                # FJ-Regel in C^2 (Gl. 11 der Quelle mit Q_a = 2 v_a v_a^dag) gegen V phi_t
                Psi = np.tensordot(V, psi0, axes=(1, 0))
                phi = psi0.copy()
                Q = [2 * np.outer(V[:, a], V[:, a].conj()) for a in range(4)]
                dmax = 0.0
                for t in range(min(args.schritte, 40)):
                    c = t % 4
                    new = np.zeros_like(Psi)
                    for a in range(4):
                        s = E4[a] - E4[c]
                        ax = tuple(i for i in range(3) if s[i] != 0)
                        x = np.tensordot(Q[a], Psi, axes=(1, 0))
                        if ax:
                            x = np.roll(x, tuple(int(s[i]) for i in ax), axis=tuple(i + 1 for i in ax))
                        new += 0.5 * x
                    Psi = new
                    phi = verschiebung(phi, t)
                    phi = np.exp(1j * ALPHA) * np.tensordot(P2s, phi, axes=(1, 0))
                    ref = np.exp(-1j * ALPHA * (t + 1)) * np.tensordot(V, phi, axes=(1, 0))
                    dmax = max(dmax, maxabs(Psi - ref))
                fj["C2_regel_gegen_kompression_abw"] = dmax
            res["fj"] = fj
            res["laeufe"] = []
            Ws = [float(eval(x, {"pi": np.pi})) for x in args.W.split(",") if x]
            for iw, W in enumerate(Ws):
                nsaat = 1 if W == 0.0 else args.saaten
                for s in range(nsaat):
                    saat = args.saatbasis + 100 * iw + s
                    mit = (W == 0.0 and args.bloch and not args.blind)
                    r, psiT = lauf_unordnung(g, P2s, psi0, args.schritte, W, saat, kc, snaps, args.blind, mit_psi=mit)
                    if mit:
                        # Bloch-Kontrolle: Endzustand der Unordnungs-Fassung (bei W = 0) gegen den k-Raum
                        r["bloch"] = bloch_kontrolle(g, P2s, psi0, args.schritte, psiT, r["w2"])
                        # zweite Realraum-Fassung (Muenze als volle 4x4-Matrix) gegen die Unordnungs-Fassung
                        psi = psi0.copy()
                        C = np.exp(1j * ALPHA) * P2s + np.exp(1j * BETA) * (np.eye(4) - P2s)
                        for t in range(args.schritte):
                            psi = verschiebung(psi, t)
                            psi = np.tensordot(C, psi, axes=(1, 0))
                        r["bloch"]["realraum_zwei_fassungen_abw"] = maxabs(psi - psiT)
                        del psi, psiT
                    res["laeufe"].append(r)
                    print("lauf W=%.4f saat=%d %.1fs maxrss=%.0fMB" % (W, saat, r["laufzeit_s"], ru_maxrss_mb()),
                          flush=True)
    res["laufzeit_s"] = time.time() - t_start
    res["maxrss_MB"] = ru_maxrss_mb()
    with open(args.out, "w") as f:
        json.dump(res, f)
    print("fertig", args.out, "%.1fs" % res["laufzeit_s"], "maxrss %.0f MB" % res["maxrss_MB"], flush=True)


if __name__ == "__main__":
    main()
