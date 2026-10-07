#!/usr/bin/env python3
"""KITAEV-DIAMANT-1 (Runde 37, fmhc-physics): Gamma-Matrix-Kitaev-Modell auf dem Diamantgitter.

Modell [S]: S. Ryu, "Three-dimensional topological phase on the diamond lattice", Phys. Rev. B 79, 075124 (2009),
arXiv:0811.2036v2. Benutzt: Eq. (2), (3) Dirac-Matrizen; (15)-(17) Gitter; (18) H; (20)-(25) Majoranas;
(27)-(31) Loesung; Abschnitte VI, VII (Phasen). Vertauschungsphase nach Levin/Wen 2003, Eq. (4) (wie STRINGENDE-1).

Rechenwege:
- Pauli-Operatoren exakt als i^k X^x Z^z (x, z Bitvektoren als Python-int), keine Gleitkommazahl.
- Kleine exakte Diagonalisierungen (Sechseck 4096 Zustaende, periodischer Haufen 256 Zustaende) in numpy.
- Majorana-Spektrum im Impulsraum: |Phi(k)| auf k-Gittern und mit Minimierern (scipy).
Aufruf: python kitaev_diamant.py <rauch|haupt> <ausgabe.json> <bild.png>
"""
import sys
import os
import json
import time
import random
import itertools
import platform
from collections import deque

import numpy as np


# ------------------------------------------------------------------ Pauli-Algebra (aus STRINGENDE-1)
class Pauli:
    __slots__ = ("k", "x", "z")

    def __init__(self, k=0, x=0, z=0):
        self.k = k % 4
        self.x = x
        self.z = z

    def __mul__(self, o):
        # (i^k1 X^x1 Z^z1)(i^k2 X^x2 Z^z2) = i^(k1+k2) (-1)^{|z1 & x2|} X^(x1^x2) Z^(z1^z2)
        return Pauli(self.k + o.k + 2 * (self.z & o.x).bit_count(), self.x ^ o.x, self.z ^ o.z)

    def inv(self):
        return Pauli(-self.k + 2 * (self.z & self.x).bit_count(), self.x, self.z)

    def neg(self):
        return Pauli(self.k + 2, self.x, self.z)

    def mal_i(self):
        return Pauli(self.k + 1, self.x, self.z)

    def mal_minus_i(self):
        return Pauli(self.k + 3, self.x, self.z)

    def ist_eins(self):
        return self.x == 0 and self.z == 0 and self.k == 0

    def ist_phase(self):
        return self.x == 0 and self.z == 0

    def hermitesch(self):
        return (self.k - (self.x & self.z).bit_count()) % 2 == 0

    def gleich(self, o):
        return self.k == o.k and self.x == o.x and self.z == o.z

    def gleiche_basis(self, o):
        return self.x == o.x and self.z == o.z

    def verschoben(self, n):
        return Pauli(self.k, self.x << n, self.z << n)


def sym(a, b):
    """1, wenn a und b antikommutieren, sonst 0."""
    return ((a.x & b.z).bit_count() + (a.z & b.x).bit_count()) & 1


def X(q):
    return Pauli(0, 1 << q, 0)


def Z(q):
    return Pauli(0, 0, 1 << q)


def Y(q):
    return Pauli(1, 1 << q, 1 << q)  # Y = i X Z


def prod(liste):
    P = Pauli()
    for Q in liste:
        P = P * Q
    return P


def phase_wert(d):
    d %= 4
    return {0: 1, 2: -1}.get(d, "i^%d" % d)


def vertauschung(W1, W2, W3):
    """Levin/Wen Eq. (4). W1 = W_ij (j->i), W2 = W_ik, W3 = W_il. Rueckgabe (V1 Quelle, V2 Karte, V3 symplektisch)."""
    Wki = W2.inv()
    A = W3 * Wki * W1  # W_il W_ki W_ij
    B = W1 * Wki * W3  # W_ij W_ki W_il
    v1 = phase_wert(A.k - B.k) if (A.x == B.x and A.z == B.z) else "A!=B"
    C = W3 * W2.inv() * W1 * W3.inv() * W2 * W1.inv()
    v2 = phase_wert(C.k) if C.ist_phase() else "keine Phase"
    v3 = -1 if (sym(W1, W2) + sym(W1, W3) + sym(W2, W3)) & 1 else 1
    return v1, v2, v3


def zaehle(d, wert):
    s = str(wert)
    d[s] = d.get(s, 0) + 1


class GF2:
    def __init__(self):
        self.b = {}

    def add(self, v):
        while v:
            h = v.bit_length() - 1
            if h in self.b:
                v ^= self.b[h]
            else:
                self.b[h] = v
                return True
        return False

    def enthaelt(self, v):
        while v:
            h = v.bit_length() - 1
            if h in self.b:
                v ^= self.b[h]
            else:
                return False
        return True


PH = [1.0 + 0j, 1j, -1.0 + 0j, -1j]


def dichte_matrix(terme, n):
    """Summe c * P (P Pauli auf n Qubits) als dichte komplexe Matrix. P|b> = i^k (-1)^{|z&b|} |b^x>."""
    dim = 1 << n
    b = np.arange(dim, dtype=np.int64)
    H = np.zeros((dim, dim), dtype=complex)
    for c, P in terme:
        par = (np.bitwise_count(b & np.int64(P.z)) & 1).astype(np.int64)  # uint8 -> int64 (sonst 1-2*1 = 255)
        H[b ^ np.int64(P.x), b] += c * PH[P.k] * (1 - 2 * par)
    return H


def eig_reell(H, name):
    im = float(np.abs(H.imag).max())
    herm = float(np.abs(H - H.conj().T).max())
    assert herm < 1e-12, (name, "nicht hermitesch", herm)
    if im < 1e-12:
        return np.linalg.eigvalsh(H.real), im, herm
    return np.linalg.eigvalsh(H), im, herm


# ------------------------------------------------------------------ Dirac-Matrizen nach Ryu Eq. (2), (3), (24)
# Erster Tensorfaktor sigma -> Qubit 0, zweiter Tensorfaktor tau -> Qubit 1 (je Knoten s: Qubits 2s, 2s+1).
SIG = {0: Pauli(), 1: X(0), 2: Y(0), 3: Z(0)}
TAU = {0: Pauli(), 1: X(1), 2: Y(1), 3: Z(1)}  # 1 = x, 2 = y, 3 = z


def dirac():
    alpha = {0: SIG[0] * TAU[3]}          # alpha^0 = sigma^0 (x) tau^z = beta
    zeta = {0: SIG[0] * TAU[1]}           # zeta^0 = sigma^0 (x) tau^x = gamma_5
    for a in (1, 2, 3):
        alpha[a] = SIG[a] * TAU[1]        # alpha^a = sigma^a (x) tau^x
        zeta[a] = (SIG[a] * TAU[3]).neg() # zeta^a = -sigma^a (x) tau^z
    g45 = SIG[0] * TAU[2]                 # Eq. (24) rechts: sigma^0 (x) tau^y
    return alpha, zeta, g45


def pruefe_dirac():
    al, ze, g45 = dirac()
    f = {"alpha_nicht_hermitesch": 0, "alpha_quadrat": 0, "alpha_paar_kommutiert": 0,
         "zeta_nicht_hermitesch": 0, "zeta_quadrat": 0, "zeta_paar_kommutiert": 0,
         "alpha_zeta_muster": 0, "eq24_dirac": 0, "zeta_gleich_i_alpha_g45": 0}
    for name, G in (("alpha", al), ("zeta", ze)):
        for mu in range(4):
            f[name + "_nicht_hermitesch"] += 0 if G[mu].hermitesch() else 1
            f[name + "_quadrat"] += 0 if (G[mu] * G[mu]).ist_eins() else 1
        for mu, nu in itertools.combinations(range(4), 2):
            f[name + "_paar_kommutiert"] += 1 - sym(G[mu], G[nu])
    for mu in range(4):
        for nu in range(4):
            soll = 1 if mu == nu else 0
            f["alpha_zeta_muster"] += 0 if sym(al[mu], ze[nu]) == soll else 1
    P4 = al[1] * al[2] * al[3] * al[0]
    f["eq24_dirac"] = 0 if P4.gleich(g45) else 1
    for mu in range(4):
        f["zeta_gleich_i_alpha_g45"] += 0 if ze[mu].gleich((al[mu] * g45).mal_i()) else 1
    return {"fehler": f, "anzahl": {"paare_je_satz": 6, "matrizen_je_satz": 4, "alpha_zeta_paare": 16}}


# ------------------------------------------------------------------ Diamantgitter nach Ryu Eq. (15)-(17)
# r_A = sum m_i a_i, r_B = r_A + s_0; A(m) ist ueber s_mu mit B(m + DELTA[mu]) verbunden (s_mu - s_0 = r_A(DELTA[mu])).
DELTA = [(0, 0, 0), (0, 0, 1), (-1, 0, 1), (0, -1, 1)]
A_VEK = np.array([[0.5, 0.5, 0.0], [0.0, 0.5, 0.5], [0.5, 0.0, 0.5]])          # a_1, a_2, a_3 (a = 1)
S_VEK = np.array([[-1, 1, -1], [1, 1, 1], [-1, -1, 1], [1, -1, -1]]) / 4.0     # s_0, s_1, s_2, s_3


class Diamant:
    def __init__(self, L):
        self.L = tuple(L)
        L1, L2, L3 = self.L
        self.zellen = [(a, b, c) for c in range(L3) for b in range(L2) for a in range(L1)]
        self.nz = len(self.zellen)
        self.ns = 2 * self.nz
        self.bonds = []
        for m in self.zellen:
            for mu in range(4):
                self.bonds.append((self.A(m), self.B(self.add(m, DELTA[mu])), mu))
        self.nb = {s: [] for s in range(self.ns)}
        self.bond_at = {}
        for bi, (a, b, mu) in enumerate(self.bonds):
            self.nb[a].append((b, mu, bi))
            self.nb[b].append((a, mu, bi))
            assert (a, mu) not in self.bond_at and (b, mu) not in self.bond_at
            self.bond_at[(a, mu)] = bi
            self.bond_at[(b, mu)] = bi
        self._hex = None

    def mod(self, m):
        return (m[0] % self.L[0], m[1] % self.L[1], m[2] % self.L[2])

    def add(self, m, d):
        return self.mod((m[0] + d[0], m[1] + d[1], m[2] + d[2]))

    def cidx(self, m):
        m = self.mod(m)
        return m[0] + self.L[0] * (m[1] + self.L[1] * m[2])

    def A(self, m):
        return 2 * self.cidx(m)

    def B(self, m):
        return 2 * self.cidx(m) + 1

    def zelle(self, s):
        c = s // 2
        L1, L2, _ = self.L
        return (c % L1, (c // L1) % L2, c // (L1 * L2))

    def nachbar(self, s, mu):
        a, b, _ = self.bonds[self.bond_at[(s, mu)]]
        return b if s == a else a

    def nachbarn(self, s):
        return [y for (y, _, _) in self.nb[s]]

    def bond_zwischen(self, s, t):
        for (y, _, bi) in self.nb[s]:
            if y == t:
                return bi
        raise ValueError((s, t))

    def sechsecke(self):
        """Sechserringe: von A(m) ueber die Richtungsfolge mu nu rho mu nu rho; doppelte entfernt."""
        if self._hex is None:
            seen = {}
            entartet = 0
            for m in self.zellen:
                for trip in itertools.permutations(range(4), 3):
                    seq = list(trip) * 2
                    s0 = self.A(m)
                    sites, bonds, cur = [s0], [], s0
                    for t in seq:
                        bonds.append(self.bond_at[(cur, t)])
                        cur = self.nachbar(cur, t)
                        sites.append(cur)
                    assert cur == s0
                    key = frozenset(bonds)
                    if len(key) != 6 or len(set(sites[:-1])) != 6:
                        entartet += 1
                        continue
                    if key not in seen:
                        seen[key] = (sites[:-1], bonds, seq)
            self._hex = list(seen.values())
            self.hex_entartet = entartet
        return self._hex


class Spin:
    """Spinoperatoren des Modells: Knoten s -> Qubits 2s (sigma), 2s+1 (tau)."""

    def __init__(self, D):
        self.D = D
        self.al, self.ze, self.g45 = dirac()

    def a(self, mu, s):
        return self.al[mu].verschoben(2 * s)

    def zt(self, mu, s):
        return self.ze[mu].verschoben(2 * s)

    def G45(self, s):
        return self.g45.verschoben(2 * s)

    def T(self, bi, sorte):
        a, b, mu = self.D.bonds[bi]
        if sorte == "a":
            return self.a(mu, a) * self.a(mu, b)
        if sorte == "z":
            return self.zt(mu, a) * self.zt(mu, b)
        if sorte == "az":
            return self.a(mu, a) * self.a(mu, b) * self.zt(mu, a) * self.zt(mu, b)
        raise ValueError(sorte)

    def schleife(self, hexa, sorte="a"):
        """Geordnetes Produkt der Bindungsoperatoren entlang des Rings; mal i, falls nicht hermitesch."""
        W = Pauli()
        for bi in hexa[1]:
            W = W * self.T(bi, sorte)
        f = "1"
        if not W.hermitesch():
            W = W.mal_i()
            f = "i"
        return W, f


def h_terme(S, J):
    """H = - sum_mu J_mu sum_{mu-Bindungen} (alpha alpha + zeta zeta), Ryu Eq. (18)."""
    t = []
    for bi, (a, b, mu) in enumerate(S.D.bonds):
        t.append((-J[mu], S.T(bi, "a")))
        t.append((-J[mu], S.T(bi, "z")))
    return t


# ------------------------------------------------------------------ KD0: Gamma-Algebra, Schleifen
def lauf_kd0_gitter(L):
    D = Diamant((L, L, L))
    S = Spin(D)
    hexs = D.sechsecke()
    r = {"L": L, "knoten": D.ns, "bindungen": len(D.bonds), "sechsecke": len(hexs),
         "sechsecke_entartet_verworfen": D.hex_entartet}
    je_knoten = {}
    muster_fehler = 0
    for sites, bonds, seq in hexs:
        for s in sites:
            je_knoten[s] = je_knoten.get(s, 0) + 1
        typen = [D.bonds[bi][2] for bi in bonds]
        if not (typen[0:3] == typen[3:6] and len(set(typen[0:3])) == 3):
            muster_fehler += 1
    r["sechsecke_je_knoten"] = sorted(set(je_knoten.values()))
    r["typmuster_fehler"] = muster_fehler
    W = []
    faktoren = {}
    f_herm = f_quad = f_az = 0
    for h in hexs:
        Wa, fa = S.schleife(h, "a")
        Wz, fz = S.schleife(h, "z")
        zaehle(faktoren, fa)
        f_herm += 0 if Wa.hermitesch() else 1
        f_quad += 0 if (Wa * Wa).ist_eins() else 1
        f_az += 0 if Wa.gleich(Wz) else 1
        W.append(Wa)
    r.update({"W_normierung": faktoren, "W_nicht_hermitesch": f_herm, "W_quadrat_fehler": f_quad,
              "W_alpha_ungleich_W_zeta": f_az})
    terme = h_terme(S, (1.0, 1.0, 1.0, 1.0))
    f_hw = 0
    for _, T in terme:
        for Wp in W:
            f_hw += sym(T, Wp)
    f_ww = 0
    for A_, B_ in itertools.combinations(W, 2):
        f_ww += sym(A_, B_)
    r.update({"H_terme": len(terme), "H_gegen_W_paare": len(terme) * len(W), "H_gegen_W_antikommut": f_hw,
              "W_paare": len(W) * (len(W) - 1) // 2, "W_paar_antikommut": f_ww})
    # GF(2)-Relationen zwischen Sechsecken (geschlossene Flaechen): Produkt der W_p muss Vielfaches der Eins sein
    basis = {}
    rel_phasen = {}
    rel_groessen = {}
    nicht_phase = 0
    for hi, (sites, bonds, seq) in enumerate(hexs):
        v = 0
        for bi in bonds:
            v ^= 1 << bi
        c = 1 << hi
        while v:
            p = v.bit_length() - 1
            if p in basis:
                v ^= basis[p][0]
                c ^= basis[p][1]
            else:
                basis[p] = (v, c)
                break
        if v == 0:
            P = Pauli()
            idx = [j for j in range(len(hexs)) if (c >> j) & 1]
            for j in idx:
                P = P * W[j]
            zaehle(rel_groessen, len(idx))
            if P.ist_phase():
                zaehle(rel_phasen, phase_wert(P.k))
            else:
                nicht_phase += 1
    r.update({"rang": len(basis), "relationen": len(hexs) - len(basis), "relation_produkt_phasen": rel_phasen,
              "relation_nicht_phase": nicht_phase, "relation_groessen": rel_groessen})
    return r, D, S, W


# ------------------------------------------------------------------ KD1: Majorana-Darstellung (Ryu Eq. 20-28)
class Maj:
    """Sechs Majoranas je Knoten, globale Jordan-Wigner-Kette: Knoten s -> Moden 3s, 3s+1, 3s+2."""

    def lam(self, p, s):
        q = 3 * s + p // 2
        zmask = (1 << q) - 1
        if p % 2 == 0:
            return Pauli(0, 1 << q, zmask)
        return Pauli(1, 1 << q, zmask | (1 << q))

    def G(self, p, q, s):  # Gamma^{pq} = i lam^p lam^q (Eq. 22)
        return (self.lam(p, s) * self.lam(q, s)).mal_i()

    def Dop(self, s):  # D = i prod_p lam^p (Eq. 21)
        return prod([self.lam(p, s) for p in range(6)]).mal_i()

    def u(self, D, bi):  # u_jk = i lam^mu_j lam^mu_k, j auf A, k auf B (Eq. 28)
        a, b, mu = D.bonds[bi]
        return (self.lam(mu, a) * self.lam(mu, b)).mal_i()


def gleich_auf_sektor(A_, B_, Dop, s):
    """A = B auf dem Unterraum D = s  <=>  A == B oder A == s*B*D (exakte Pauli-Gleichheit)."""
    if A_.gleich(B_):
        return True
    BD = B_ * Dop
    if s < 0:
        BD = BD.neg()
    return A_.gleich(BD)


def relation(A_, B_, Dop, s):
    if gleich_auf_sektor(A_, B_, Dop, s):
        return "+"
    if gleich_auf_sektor(A_, B_.neg(), Dop, s):
        return "-"
    return "keine"


def lauf_majorana_knoten():
    M = Maj()
    lam = [M.lam(p, 0) for p in range(6)]
    f = {"lam_nicht_hermitesch": 0, "lam_quadrat": 0, "lam_paar_kommutiert": 0, "D_nicht_hermitesch": 0,
         "D_quadrat": 0, "D_gegen_Gamma_antikommut": 0}
    for p in range(6):
        f["lam_nicht_hermitesch"] += 0 if lam[p].hermitesch() else 1
        f["lam_quadrat"] += 0 if (lam[p] * lam[p]).ist_eins() else 1
    for p, q in itertools.combinations(range(6), 2):
        f["lam_paar_kommutiert"] += 1 - sym(lam[p], lam[q])
    D = M.Dop(0)
    f["D_nicht_hermitesch"] = 0 if D.hermitesch() else 1
    f["D_quadrat"] = 0 if (D * D).ist_eins() else 1
    for p, q in itertools.combinations(range(6), 2):
        f["D_gegen_Gamma_antikommut"] += sym(D, M.G(p, q, 0))
    G4 = {mu: M.G(mu, 4, 0) for mu in range(4)}
    G5 = {mu: M.G(mu, 5, 0) for mu in range(4)}
    G45 = M.G(4, 5, 0)
    P4 = G4[1] * G4[2] * G4[3] * G4[0]
    sek = {}
    for s in (1, -1):
        sek[str(s)] = {"Eq24_P4_gegen_G45": relation(P4, G45, D, s),
                       "Eq25_G5_gegen_i_G4_P4": [relation(G5[mu], (G4[mu] * P4).mal_i(), D, s) for mu in range(4)]}
    return {"fehler": f, "sektoren": sek}


def lauf_majorana_gitter(D, S, W):
    M = Maj()
    nb = len(D.bonds)
    us = [M.u(D, bi) for bi in range(nb)]
    lam4 = [M.lam(4, s) for s in range(D.ns)]
    lam5 = [M.lam(5, s) for s in range(D.ns)]
    Ds = [M.Dop(s) for s in range(D.ns)]
    f = {"bindung_eq27_alpha": 0, "bindung_eq27_zeta": 0, "u_nicht_hermitesch": 0, "u_quadrat": 0,
         "u_paar_antikommut": 0, "u_gegen_Hterm_antikommut": 0, "Hterm_gegen_D_antikommut": 0,
         "u_gegen_D_muster": 0}
    hterme = []
    for bi, (a, b, mu) in enumerate(D.bonds):
        lhs4 = M.G(mu, 4, a) * M.G(mu, 4, b)
        rhs4 = (us[bi] * lam4[a] * lam4[b]).mal_minus_i()
        lhs5 = M.G(mu, 5, a) * M.G(mu, 5, b)
        rhs5 = (us[bi] * lam5[a] * lam5[b]).mal_minus_i()
        f["bindung_eq27_alpha"] += 0 if lhs4.gleich(rhs4) else 1
        f["bindung_eq27_zeta"] += 0 if lhs5.gleich(rhs5) else 1
        hterme += [lhs4, lhs5]
        f["u_nicht_hermitesch"] += 0 if us[bi].hermitesch() else 1
        f["u_quadrat"] += 0 if (us[bi] * us[bi]).ist_eins() else 1
    for i, j in itertools.combinations(range(nb), 2):
        f["u_paar_antikommut"] += sym(us[i], us[j])
    for U_ in us:
        for T in hterme:
            f["u_gegen_Hterm_antikommut"] += sym(U_, T)
    for T in hterme:
        for Dop in Ds:
            f["Hterm_gegen_D_antikommut"] += sym(T, Dop)
    for bi, (a, b, mu) in enumerate(D.bonds):
        for s in range(D.ns):
            soll = 1 if s in (a, b) else 0
            f["u_gegen_D_muster"] += 0 if sym(us[bi], Ds[s]) == soll else 1
    # Schleifen: Majorana-Bild des Spin-Schleifenoperators = sigma * prod u
    sig = {}
    norm_gleich = 0
    fehler_schleife = 0
    sig_je_hex = []
    for hi, h in enumerate(D.sechsecke()):
        Wm = Pauli()
        for bi in h[1]:
            a, b, mu = D.bonds[bi]
            Wm = Wm * (M.G(mu, 4, a) * M.G(mu, 4, b))
        fm = "1"
        if not Wm.hermitesch():
            Wm = Wm.mal_i()
            fm = "i"
        _, fs = S.schleife(h, "a")
        norm_gleich += 1 if fm == fs else 0
        PU = prod([us[bi] for bi in h[1]])
        if Wm.gleich(PU):
            zaehle(sig, 1)
            sig_je_hex.append(1)
        elif Wm.gleich(PU.neg()):
            zaehle(sig, -1)
            sig_je_hex.append(-1)
        else:
            fehler_schleife += 1
            sig_je_hex.append(0)
    return {"L": D.L, "fehler": f, "schleife_sigma": sig, "schleife_nicht_pm_prod_u": fehler_schleife,
            "normierung_gleich_spin": norm_gleich, "sechsecke": len(D.sechsecke()),
            "anzahl": {"bindungen": nb, "u_paare": nb * (nb - 1) // 2, "u_gegen_Hterm": nb * len(hterme),
                       "Hterm_gegen_D": len(hterme) * D.ns}}, sig_je_hex


def ff_niveaus(svals, sorten=2):
    s = np.tile(np.asarray(svals, dtype=float), sorten)
    occ = np.array(list(itertools.product((0, 1), repeat=len(s))), dtype=float)
    return occ @ (2.0 * s) - s.sum()


def lauf_sechseck_ed(D, hi, sigma, J, C=1000.0):
    """Offener Sechserring (nur Ringbindungen): 6 Knoten, 12 Qubits. ED gegen freie Majoranas je Flusssektor."""
    sites, bonds, seq = D.sechsecke()[hi]
    loc = {s: i for i, s in enumerate(sites)}
    al, ze, g45 = dirac()
    terme = []
    for bi in bonds:
        a, b, mu = D.bonds[bi]
        Ta = al[mu].verschoben(2 * loc[a]) * al[mu].verschoben(2 * loc[b])
        Tz = ze[mu].verschoben(2 * loc[a]) * ze[mu].verschoben(2 * loc[b])
        terme += [(-J[mu], Ta), (-J[mu], Tz)]
    Wl = Pauli()
    for bi in bonds:
        a, b, mu = D.bonds[bi]
        Wl = Wl * (al[mu].verschoben(2 * loc[a]) * al[mu].verschoben(2 * loc[b]))
    if not Wl.hermitesch():
        Wl = Wl.mal_i()
    kommut = sum(sym(T, Wl) for _, T in terme)
    H = dichte_matrix(terme + [(C, Wl)], 12)
    E, im, herm = eig_reell(H, "sechseck")
    del H
    plus = np.sort(E[E > C / 2] - C)
    minus = np.sort(E[E < -C / 2] + C)
    A_sites = [s for s in sites if s % 2 == 0]
    B_sites = [s for s in sites if s % 2 == 1]
    ia = {s: i for i, s in enumerate(A_sites)}
    ib = {s: i for i, s in enumerate(B_sites)}

    def vorhersage(Uf):
        Mh = np.zeros((3, 3))
        for n, bi in enumerate(bonds):
            a, b, mu = D.bonds[bi]
            Mh[ia[a], ib[b]] += J[mu] * (Uf if n == 0 else 1.0)
        sv = np.linalg.svd(Mh, compute_uv=False)
        return np.sort(np.repeat(ff_niveaus(sv), 32)), sv

    pred_s, sv_s = vorhersage(float(sigma))
    pred_m, sv_m = vorhersage(float(-sigma))
    r = {"J": list(J), "sigma": sigma, "W_gegen_Hterme_antikommut": kommut, "imag_max": im,
         "anzahl_plus": int(len(plus)), "anzahl_minus": int(len(minus)),
         "abw_plus": float(np.abs(plus - pred_s).max()) if len(plus) == len(pred_s) else None,
         "abw_minus": float(np.abs(minus - pred_m).max()) if len(minus) == len(pred_m) else None,
         "abw_vertauscht": float(max(np.abs(plus - pred_m).max(), np.abs(minus - pred_s).max()))
         if len(plus) == len(pred_m) and len(minus) == len(pred_s) else None,
         "singulaerwerte_U_sigma": [float(x) for x in sv_s], "singulaerwerte_U_minus_sigma": [float(x) for x in sv_m],
         "E0": float(min(plus.min(), minus.min())),
         "E0_W": 1 if plus.min() < minus.min() else -1}
    return r


def kommutator_max(terme_A, terme_B):
    """[sum a A, sum b B] exakt als Pauli-Summe; Rueckgabe groesster Koeffizient und Zahl der Pauli-Strings."""
    acc = {}
    for ca, A_ in terme_A:
        for cb, B_ in terme_B:
            if sym(A_, B_):
                P = A_ * B_
                key = (P.x, P.z)
                acc[key] = acc.get(key, 0) + 2 * ca * cb * PH[P.k]
    return float(max((abs(v) for v in acc.values()), default=0.0)), len(acc)


def lauf_u1(D, S):
    """Ryu Abschnitt III/VIII: U(1)-Symmetrie (Drehung um tau^y), Erzeuger Q = sum_x Gamma^45_x = sum sigma^0 tau^y."""
    Q = [(1.0, S.G45(s)) for s in range(D.ns)]
    r = {}
    for name, J in (("uniform", (1.0, 1.0, 1.0, 1.0)), ("allgemein", (1.0, 0.7, 1.3, 0.9))):
        mx, n = kommutator_max(h_terme(S, J), Q)
        r[name] = {"kommutator_max": mx, "pauli_strings_im_kommutator": n}
    # Gegenprobe: Q' = sum_x alpha^0_x vertauscht nicht
    mx, n = kommutator_max(h_terme(S, (1.0, 0.7, 1.3, 0.9)), [(1.0, S.a(0, s)) for s in range(D.ns)])
    r["gegenprobe_alpha0"] = {"kommutator_max": mx, "pauli_strings_im_kommutator": n}
    return r


def lauf_cluster112(J):
    """Periodischer Haufen L = (1,1,2): 4 Knoten, 8 Bindungen, jede Richtung je Knoten einmal (Multigraph)."""
    D = Diamant((1, 1, 2))
    S = Spin(D)
    Es, im_s, _ = eig_reell(dichte_matrix(h_terme(S, J), 8), "spin112")
    Es = np.sort(Es)
    M = Maj()
    ext = []
    for bi, (a, b, mu) in enumerate(D.bonds):
        ext.append((-J[mu], M.G(mu, 4, a) * M.G(mu, 4, b)))
        ext.append((-J[mu], M.G(mu, 5, a) * M.G(mu, 5, b)))
    Ds = [M.Dop(s) for s in range(4)]
    for Dop in Ds:
        assert Dop.x == 0 and Dop.k % 2 == 0
    phys = []
    for bvec in range(1 << 12):
        ok = True
        for Dop in Ds:
            ev = PH[Dop.k].real * (1 - 2 * ((Dop.z & bvec).bit_count() & 1))
            if ev != 1:
                ok = False
                break
        if ok:
            phys.append(bvec)
    idx = {bvec: i for i, bvec in enumerate(phys)}
    Hr = np.zeros((len(phys), len(phys)), dtype=complex)
    raus = 0
    for c, P in ext:
        for bvec in phys:
            ziel = bvec ^ P.x
            if ziel not in idx:
                raus += 1
                continue
            Hr[idx[ziel], idx[bvec]] += c * PH[P.k] * (1 - 2 * ((P.z & bvec).bit_count() & 1))
    Er, im_r, _ = eig_reell(Hr, "ext112")
    Er = np.sort(Er)
    # freie Majoranas mit Projektion: prod_s D_s = c * (prod_b u_b) * P_m
    PiD = prod(Ds)
    PiU = prod([M.u(D, bi) for bi in range(len(D.bonds))])
    Pm = prod([M.G(4, 5, s) for s in range(4)])
    R = PiU * Pm
    c = 1 if PiD.gleich(R) else (-1 if PiD.gleich(R.neg()) else 0)

    def m(p, s):  # Materie-Majoranas lam^4_s, lam^5_s auf 4 Qubits (eigene JW-Kette)
        zmask = (1 << s) - 1
        return Pauli(0, 1 << s, zmask) if p == 4 else Pauli(1, 1 << s, zmask | (1 << s))

    Pm_m = prod([(m(4, s) * m(5, s)).mal_i() for s in range(4)])
    pred = []
    E0_frei = []
    for uconf in itertools.product((1, -1), repeat=len(D.bonds)):
        tm = []
        for bi, (a, b, mu) in enumerate(D.bonds):
            tm.append((1j * J[mu] * uconf[bi], m(4, a) * m(4, b)))
            tm.append((1j * J[mu] * uconf[bi], m(5, a) * m(5, b)))
        Hm = dichte_matrix(tm + [(1000.0, Pm_m)], 4)
        e = np.linalg.eigvalsh(Hm)
        U = int(np.prod(uconf))
        erlaubt = c * U
        sel = (e[e > 500] - 1000.0) if erlaubt == 1 else (e[e < -500] + 1000.0)
        pred += list(sel)
        E0_frei.append(float(np.concatenate([e[e > 500] - 1000.0, e[e < -500] + 1000.0]).min()))
    pred = np.sort(np.array(pred))
    ok_len = len(pred) == 8 * len(Es)
    r = {"J": list(J), "spin_dim": int(len(Es)), "phys_dim": len(phys), "ext_terme_aus_phys_raus": raus,
         "abw_spin_gegen_ext": float(np.abs(Es - Er).max()) if len(Es) == len(Er) else None,
         "c_projektion": c, "pred_anzahl": int(len(pred)),
         "abw_spin_gegen_frei_projiziert": float(np.abs(np.repeat(Es, 8) - pred).max()) if ok_len else None,
         "E0_spin": float(Es[0]), "E0_frei_ohne_projektion_min": float(min(E0_frei)), "imag": [im_s, im_r]}
    return r


# ------------------------------------------------------------------ Impulsraum (Ryu Eq. 30, 31)
def phi_theta(J, t1, t2, t3):
    """Phi(k) * exp(-i k.s_0); theta_i = k.a_i. s_1-s_0 = a_3, s_2-s_0 = a_3-a_1, s_3-s_0 = a_3-a_2."""
    return J[0] + J[1] * np.exp(1j * t3) + J[2] * np.exp(1j * (t3 - t1)) + J[3] * np.exp(1j * (t3 - t2))


def phi_kart(J, k):
    """Ryu Eq. (31): Phi(k) = sum_mu J_mu exp(i k.s_mu), k kartesisch (a = 1)."""
    return np.exp(1j * (k @ S_VEK.T)) @ np.asarray(J, dtype=float)


def gitter_min(J, N, deltas=()):
    t = 2 * np.pi * np.arange(N) / N
    T2, T3 = np.meshgrid(t, t, indexing="ij")
    E3 = np.exp(1j * T3)
    E32 = np.exp(1j * (T3 - T2))
    best = np.inf
    zaehl = np.zeros(len(deltas), dtype=np.int64)
    for n1 in range(N):
        val = np.abs(J[0] + J[1] * E3 + J[2] * E3 * np.exp(-1j * t[n1]) + J[3] * E32)
        best = min(best, float(val.min()))
        for i, d in enumerate(deltas):
            zaehl[i] += int((val < d).sum())
    return best, [int(z) for z in zaehl]


def kont_min(J, rng, starts):
    from scipy.optimize import minimize

    J = np.asarray(J, dtype=float)

    def fg(th):
        t1, t2, t3 = th
        e1 = J[1] * np.exp(1j * t3)
        e2 = J[2] * np.exp(1j * (t3 - t1))
        e3 = J[3] * np.exp(1j * (t3 - t2))
        P = J[0] + e1 + e2 + e3
        dP = np.array([-1j * e2, -1j * e3, 1j * (e1 + e2 + e3)])
        return float(abs(P) ** 2), 2.0 * np.real(np.conj(P) * dP)

    best = np.inf
    nullen = []
    for _ in range(starts):
        th0 = rng.uniform(0, 2 * np.pi, 3)
        res = minimize(fg, th0, jac=True, method="BFGS", options={"gtol": 1e-14, "maxiter": 500})
        th = res.x.copy()
        best = min(best, float(np.sqrt(max(res.fun, 0.0))))
        for _ in range(40):  # Gauss-Newton auf (Re Phi, Im Phi), minimale Norm
            t1, t2, t3 = th
            e1 = J[1] * np.exp(1j * t3)
            e2 = J[2] * np.exp(1j * (t3 - t1))
            e3 = J[3] * np.exp(1j * (t3 - t2))
            P = J[0] + e1 + e2 + e3
            dP = np.array([-1j * e2, -1j * e3, 1j * (e1 + e2 + e3)])
            Jm = np.vstack([dP.real, dP.imag])
            F = np.array([P.real, P.imag])
            if np.linalg.norm(F) < 1e-15:
                break
            th = th - np.linalg.pinv(Jm) @ F
        Pend = abs(phi_theta(J, *th))
        best = min(best, float(Pend))
        if Pend < 1e-10:
            nullen.append(th.copy())
    return best, nullen


def theta_zu_k(th):
    return np.linalg.solve(A_VEK, np.asarray(th))


def lauf_kraum(haupt, rng):
    r = {}
    # Codepruefung: reduzierte Form gegen Eq. (31) und gegen 4(ccc - i sss) bei J = 1
    kk = rng.uniform(-10, 10, (200, 3))
    th = kk @ A_VEK.T
    Jt = (1.3, 0.7, 1.1, 0.9)
    a1 = np.abs(np.abs(phi_kart(Jt, kk)) - np.abs(phi_theta(Jt, th[:, 0], th[:, 1], th[:, 2]))).max()
    c = np.cos(kk / 4)
    s = np.sin(kk / 4)
    a2 = np.abs(phi_kart((1, 1, 1, 1), kk) - 4 * (c.prod(axis=1) - 1j * s.prod(axis=1))).max()
    r["code_pruefung"] = {"reduziert_gegen_eq31": float(a1), "J1_gegen_4ccc_minus_i_sss": float(a2)}
    Ns = [8, 9, 16, 17, 32, 33, 64, 65, 128, 129, 256, 257] if haupt else [8, 9, 16, 17, 32, 33, 64, 65]
    starts = 64 if haupt else 8
    # J = 1 (KD1)
    J1 = (1.0, 1.0, 1.0, 1.0)
    gm = {}
    for N in Ns:
        gm[str(N)] = gitter_min(J1, N)[0]
    starts_j1 = 400 if haupt else starts  # mehr Starts fuer J = 1: Lage der Knotenlinien (Bild)
    kmin, nullen = kont_min(J1, rng, starts_j1)
    Nv = 257 if haupt else 33  # ungerade: keine Gitterpunkte genau auf den Knotenlinien
    deltas = [0.4, 0.2, 0.1, 0.05]
    _, zahl = gitter_min(J1, Nv, deltas)
    frac = [z / Nv ** 3 for z in zahl]
    lg = np.log(np.array(deltas[1:]))
    lf = np.log(np.maximum(np.array(frac[1:]), 1e-300))
    steig = float(np.polyfit(lg, lf, 1)[0]) if min(frac[1:]) > 0 else None
    # Lage der Nullstellen: welche Faktoren von 4(ccc - i sss) verschwinden
    lage = {}
    for thn in nullen:
        k = theta_zu_k(thn)
        cc = np.abs(np.cos(k / 4))
        ss = np.abs(np.sin(k / 4))
        key = "c%s_s%s" % ("xyz"[int(np.argmin(cc))], "xyz"[int(np.argmin(ss))])
        if cc.min() > 1e-6 or ss.min() > 1e-6:
            key = "keine_Linie"
        zaehle(lage, key)
    # beschreibend: Zahl der Gitterpunkte mit |Phi| < 2 pi / N gegen N (Linien ~ N^1, Punkte ~ N^0, Flaechen ~ N^2)
    nN = {}
    for N in ([65, 129, 257] if haupt else [17, 33, 65]):
        nN[str(N)] = gitter_min(J1, N, [2 * np.pi / N])[1][0]
    xs_ = np.log([float(n) for n in nN])
    ys_ = np.log([max(v, 1) for v in nN.values()])
    r["J1"] = {"gitter_min": gm, "kont_min": kmin, "nullen_gefunden": len(nullen), "starts": starts_j1,
               "volumenanteil_N": Nv, "deltas": deltas, "volumenanteil": frac, "steigung_loglog": steig,
               "nullstellen_lage": lage, "nahe_null_zahl_beschreibend": nN,
               "nahe_null_exponent_beschreibend": float(np.polyfit(xs_, ys_, 1)[0])}
    # Skan J_0 (KD2), J_1 = J_2 = J_3 = 1
    scan = []
    J0s = [1.0, 1.5, 2.0, 2.5, 2.8, 2.9, 3.0, 3.1, 3.2, 3.5, 4.0, 5.0, 6.0]
    Nsc = [64, 65, 128, 129] if haupt else [16, 17]
    for J0 in J0s:
        Jc = (J0, 1.0, 1.0, 1.0)
        g = {str(N): gitter_min(Jc, N)[0] for N in Nsc}
        km, nl = kont_min(Jc, rng, 32 if haupt else 6)
        scan.append({"J0": J0, "gitter_min": g, "kont_min": km, "nullen_gefunden": len(nl),
                     "vorhersage_schreibtisch": max(0.0, J0 - 3.0)})
    r["scan"] = scan
    prim = {}
    for name, Jc in (("J0_4", (4.0, 1.0, 1.0, 1.0)), ("J0_2", (2.0, 1.0, 1.0, 1.0)),
                     ("J3_4", (1.0, 1.0, 1.0, 4.0)), ("J1_4", (1.0, 4.0, 1.0, 1.0))):
        g = {str(N): gitter_min(Jc, N)[0] for N in Ns}
        km, nl = kont_min(Jc, rng, starts)
        prim[name] = {"J": list(Jc), "gitter_min": g, "kont_min": km, "nullen_gefunden": len(nl)}
    r["kd2"] = prim
    r["_nullen_J1"] = [list(map(float, t)) for t in nullen]
    return r


def lauf_fluss_realraum(rng, haupt):
    """Grundzustandsenergie freier Majoranas je Eichfeld (beschreibend; Quelle: Lieb -> u = 1)."""
    r = {}
    for L in ([4, 5, 6, 7, 8] if haupt else [4, 5]):
        D = Diamant((L, L, L))
        nA = D.nz
        for name, J in (("J1", (1.0, 1.0, 1.0, 1.0)), ("J0_4", (4.0, 1.0, 1.0, 1.0)), ("J0_2", (2.0, 1.0, 1.0, 1.0))):
            def e0(u):
                Mh = np.zeros((nA, nA))
                for bi, (a, b, mu) in enumerate(D.bonds):
                    Mh[a // 2, b // 2] += J[mu] * u[bi]
                sv = np.linalg.svd(Mh, compute_uv=False)
                return -2.0 * sv.sum(), float(sv.min())

            u1 = np.ones(len(D.bonds))
            E1, smin = e0(u1)
            # Realraum gegen Impulsraum (Ryu Eq. 31): Singulaerwerte = |Phi| auf dem L-Gitter
            Mh = np.zeros((nA, nA))
            for bi, (a, b, mu) in enumerate(D.bonds):
                Mh[a // 2, b // 2] += J[mu]
            sv = np.sort(np.linalg.svd(Mh, compute_uv=False))
            t = 2 * np.pi * np.arange(L) / L
            T1, T2, T3 = np.meshgrid(t, t, t, indexing="ij")
            pk = np.sort(np.abs(phi_theta(J, T1, T2, T3)).ravel())
            abw_k = float(np.abs(sv - pk).max())
            uf = u1.copy()
            uf[0] = -1
            Ef, _ = e0(uf)
            dE_typ = {}
            for mu in range(4):  # ein u je Bindungsrichtung kippen (kleinste Wirbelschleife um diese Bindung)
                ut = u1.copy()
                ut[[bi for bi, (_, _, m_) in enumerate(D.bonds) if m_ == mu][0]] = -1
                dE_typ[str(mu)] = e0(ut)[0] - E1
            zufall = []
            for _ in range(20 if haupt else 3):
                uz = rng.choice([-1.0, 1.0], len(D.bonds))
                zufall.append(e0(uz)[0])
            r["L%d_%s" % (L, name)] = {"E0_je_knoten_u1": E1 / D.ns, "min_singulaerwert_u1": smin,
                                       "abw_realraum_gegen_kraum": abw_k,
                                       "dE_ein_u_gekippt": Ef - E1, "dE_ein_u_gekippt_je_richtung": dE_typ,
                                       "E0_je_knoten_zufall_min": min(zufall) / D.ns,
                                       "u1_tiefer_als_alle_zufall": bool(all(E1 < z for z in zufall)),
                                       "anzahl_zufall": len(zufall)}
    return r


# ------------------------------------------------------------------ KD3: Vertauschungsphase (Levin/Wen Eq. 4)
def lerw(rng, start, ziel, erlaubt, nachbarn):
    pfad = [start]
    pos = {start: 0}
    cur = start
    n = 0
    while cur != ziel:
        nb = [q for q in nachbarn(cur) if q in erlaubt]
        nxt = nb[rng.randrange(len(nb))]
        n += 1
        if n > 5_000_000:
            raise RuntimeError("LERW endet nicht")
        if nxt in pos:
            i = pos[nxt]
            for q in pfad[i + 1:]:
                del pos[q]
            pfad = pfad[: i + 1]
        else:
            pfad.append(nxt)
            pos[nxt] = len(pfad) - 1
        cur = nxt
    return pfad


def bfs_pfad(start, ziel, erlaubt, nachbarn):
    vor = {start: None}
    dq = deque([start])
    while dq:
        x = dq.popleft()
        if x == ziel:
            break
        for y in nachbarn(x):
            if y in erlaubt and y not in vor:
                vor[y] = x
                dq.append(y)
    assert ziel in vor, "Bereich nicht zusammenhaengend"
    pfad = [ziel]
    while pfad[-1] != start:
        pfad.append(vor[pfad[-1]])
    return pfad[::-1]


def string_aus_pfad(S, D, pfad, sorte):
    """W = t_{p_n p_{n-1}} ... t_{p_1 p_0} (Levin/Wen Abschnitt IV); t = Bindungsoperator der Sorte."""
    W = Pauli()
    for x, y in zip(pfad, pfad[1:]):
        W = S.T(D.bond_zwischen(x, y), sorte) * W
    return W


def lauf_lokal(L, sorten):
    D = Diamant((L, L, L))
    S = Spin(D)
    r = {}
    for sorte in sorten:
        d = {"V1": {}, "inkonsistent": 0, "anzahl": 0}
        for i in range(D.ns):
            hops = {mu: S.T(D.bond_at[(i, mu)], sorte) for mu in range(4)}
            for t in itertools.permutations(range(4), 3):
                v = vertauschung(hops[t[0]], hops[t[1]], hops[t[2]])
                if not (v[0] == v[1] == v[2]):
                    d["inkonsistent"] += 1
                zaehle(d["V1"], v[0])
                d["anzahl"] += 1
        r[sorte] = d
    return r


def lauf_lang(rng, N, L=8):
    D = Diamant((L, L, L))
    S = Spin(D)
    I = D.A((4, 4, 4))
    E = {"j": D.B((4, 4, 4)), "k": D.B((4, 4, 5)), "l": D.B((3, 4, 5))}
    N4 = D.B((4, 3, 5))
    assert D.nachbar(I, 0) == E["j"] and D.nachbar(I, 1) == E["k"] and D.nachbar(I, 2) == E["l"]
    assert D.nachbar(I, 3) == N4

    def box(r1, r2, r3):
        m = set()
        for a in range(r1[0], r1[1] + 1):
            for b in range(r2[0], r2[1] + 1):
                for c in range(r3[0], r3[1] + 1):
                    m |= {D.A((a, b, c)), D.B((a, b, c))}
        return m

    R = {"j": box((1, 6), (1, 6), (1, 3)) | {E["j"]},
         "k": box((5, 6), (1, 6), (4, 6)) | {E["k"]},
         "l": box((1, 3), (1, 6), (4, 6)) | {E["l"]}}
    O = {"j": D.A((4, 4, 1)), "k": D.A((6, 4, 6)), "l": D.A((1, 4, 6))}
    for a in "jkl":
        assert O[a] in R[a] and I not in R[a] and N4 not in R[a]
        for b in "jkl":
            if a != b:
                assert not (R[a] & R[b]), ("Bereiche", a, b)
    nach = D.nachbarn
    hexs = D.sechsecke()
    Wp = [S.schleife(h, "a")[0] for h in hexs]
    nq = 2 * D.ns
    basis = GF2()
    for W_ in Wp:
        basis.add((W_.x << nq) | W_.z)
    G45 = [S.G45(s) for s in range(D.ns)]
    erg = {"L": L, "N": N, "sechsecke": len(hexs), "schleifen_rang": len(basis.b)}
    ref_pfade = {a: bfs_pfad(O[a], E[a], R[a], nach) + [I] for a in "jkl"}
    for sorte in ("a", "z", "az"):
        d = {"V1": {}, "inkonsistent": 0, "endpunkt_fehler": 0, "aequivalenz_fehler": 0, "anzahl": 0,
             "fluss_antikommut": 0, "fluss_geprueft": 0, "nicht_lokal": 0}
        bezug = {}
        for n in range(N + 1):
            Ws = {}
            for a in "jkl":
                pf = ref_pfade[a] if n == 0 else lerw(rng, O[a], E[a], R[a], nach) + [I]
                W_ = string_aus_pfad(S, D, pf, sorte)
                if sorte in ("a", "z"):
                    enden = {x for x in range(D.ns) if sym(W_, G45[x])}
                    if enden != {O[a], I}:
                        d["endpunkt_fehler"] += 1
                else:
                    if not W_.gleiche_basis(G45[O[a]] * G45[I]):
                        d["nicht_lokal"] += 1
                if n == 0:
                    bezug[a] = W_
                else:
                    P = W_ * bezug[a].inv()
                    if not basis.enthaelt((P.x << nq) | P.z):
                        d["aequivalenz_fehler"] += 1
                if n <= 10:
                    d["fluss_geprueft"] += 1
                    d["fluss_antikommut"] += sum(sym(W_, w) for w in Wp)
                Ws[a] = W_
            v = vertauschung(Ws["j"], Ws["k"], Ws["l"])
            if not (v[0] == v[1] == v[2]):
                d["inkonsistent"] += 1
            zaehle(d["V1"], v[0])
            d["anzahl"] += 1
        # Durchgangsprobe mit den Bezugswegen
        alle_pf = set().union(*[set(p) for p in ref_pfade.values()])
        n_ok = D.nachbar(O["k"], 1)
        assert n_ok not in alle_pf and all(n_ok not in R[a] for a in "jkl")
        assert N4 not in alle_pf
        t1 = S.T(D.bond_at[(O["k"], 1)], sorte)
        t2 = S.T(D.bond_at[(I, 3)], sorte)
        hk = [hi for hi, h in enumerate(hexs) if O["k"] in h[0]][0]
        basis_v = vertauschung(bezug["j"], bezug["k"], bezug["l"])[0]
        dg = {"basis_V1": basis_v}
        # Erwartung vorab [M]: Sorten a, z wie unten; Verbund az ist lokal (Gamma^45-Paar), dort nie ein Wechsel
        e1 = "Wechsel" if sorte in ("a", "z") else "kein Wechsel"
        for name, Fak, erw in (("Huepfer am Ende von k", t1, e1),
                               ("Huepfer am gemeinsamen Knoten (4. Richtung)", t2, "kein Wechsel"),
                               ("Schleife W_p am Ende von k", Wp[hk], "kein Wechsel")):
            v = vertauschung(bezug["j"] * Fak, bezug["k"], bezug["l"])
            beob = "Wechsel" if v[0] != basis_v else "kein Wechsel"
            dg[name] = {"erwartet": erw, "beobachtet": beob, "V": list(v), "passt": beob == erw}
        d["durchgang"] = dg
        erg[sorte] = d
    erg["pfadlaengen_bezug"] = {a: len(ref_pfade[a]) - 1 for a in "jkl"}
    return erg


# ------------------------------------------------------------------ Bild
def bild(pfad, kr):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(13, 10))
    ax1 = fig.add_subplot(2, 2, 1)
    pi = np.pi
    P = {"Γ": (0, 0, 0), "X": (2 * pi, 0, 0), "W": (2 * pi, pi, 0), "L": (pi, pi, pi), "K": (1.5 * pi, 1.5 * pi, 0)}
    weg = ["Γ", "X", "W", "L", "Γ", "K", "X"]
    ks, xs, ticks = [], [], [0.0]
    x0 = 0.0
    for a, b in zip(weg, weg[1:]):
        pa, pb = np.array(P[a], float), np.array(P[b], float)
        t = np.linspace(0, 1, 200)
        seg = pa[None, :] + t[:, None] * (pb - pa)[None, :]
        ks.append(seg)
        xs.append(x0 + t * np.linalg.norm(pb - pa))
        x0 += np.linalg.norm(pb - pa)
        ticks.append(x0)
    ks = np.vstack(ks)
    xs = np.concatenate(xs)
    for J, col in (((1, 1, 1, 1), "C0"), ((2, 1, 1, 1), "C2"), ((4, 1, 1, 1), "C3")):
        e = np.abs(phi_kart(J, ks))
        ax1.plot(xs, e, color=col, label="J = %s" % (J,))
        ax1.plot(xs, -e, color=col)
    ax1.set_xticks(ticks)
    ax1.set_xticklabels(weg)
    ax1.axhline(0, color="k", lw=0.5)
    ax1.set_ylabel("E(k) = ±|Φ(k)|  (Ryu Eq. 31)")
    ax1.set_title("Majorana-Baender, flussfreier Sektor")
    ax1.legend(fontsize=8)
    ax2 = fig.add_subplot(2, 2, 2)
    J0 = [s["J0"] for s in kr["scan"]]
    dk = [s["kont_min"] for s in kr["scan"]]
    ax2.plot(J0, dk, "o", label="gerechnet: min |Φ| (Minimierer)")
    jj = np.linspace(1, 6, 200)
    ax2.plot(jj, np.maximum(0, jj - 3), "-", color="gray", label="Schreibtisch: max(0, J0 - 3)")
    ax2.set_xlabel("J0  (J1 = J2 = J3 = 1)")
    ax2.set_ylabel("Luecke min_k |Φ(k)|")
    ax2.set_title("Luecke gegen Kopplung")
    ax2.legend(fontsize=8)
    ax3 = fig.add_subplot(2, 2, 3)
    for name, lab in (("J1", "J = (1,1,1,1)"), ("J0_4", "J = (4,1,1,1)")):
        g = kr["J1"]["gitter_min"] if name == "J1" else kr["kd2"]["J0_4"]["gitter_min"]
        Ns = sorted(int(n) for n in g)
        odd = [n for n in Ns if n % 2]
        ev = [n for n in Ns if n % 2 == 0]
        ax3.loglog(odd, [max(g[str(n)], 1e-17) for n in odd], "o-", label=lab + ", N ungerade")
        ax3.loglog(ev, [max(g[str(n)], 1e-17) for n in ev], "s--", label=lab + ", N gerade")
    ax3.set_xlabel("k-Gitter N (N^3 Punkte)")
    ax3.set_ylabel("min |Φ| auf dem Gitter")
    ax3.set_title("Lueckengroesse gegen Gittergroesse")
    ax3.legend(fontsize=7)
    ax4 = fig.add_subplot(2, 2, 4, projection="3d")
    nl = np.array(kr["_nullen_J1"]) if kr["_nullen_J1"] else np.zeros((0, 3))
    if len(nl):
        kk = np.array([theta_zu_k(t) for t in nl])
        kk = (kk + 2 * pi) % (4 * pi) - 2 * pi
        ax4.scatter(kk[:, 0] / pi, kk[:, 1] / pi, kk[:, 2] / pi, s=6)
    ax4.set_xlabel("kx a/π")
    ax4.set_ylabel("ky a/π")
    ax4.set_zlabel("kz a/π")
    ax4.set_title("Nullstellen bei J = 1 (Minimierer), gefaltet")
    fig.suptitle("KITAEV-DIAMANT-1: Majorana-Spektrum des Ryu-Modells (synthetisch, keine Messdaten)")
    fig.tight_layout()
    fig.savefig(pfad + ".tmp.png", dpi=110)
    os.replace(pfad + ".tmp.png", pfad)


# ------------------------------------------------------------------ Hauptprogramm
def main():
    modus, aus, bildpfad = sys.argv[1], sys.argv[2], sys.argv[3]
    haupt = modus == "haupt"
    saat = 37137 if haupt else 37101
    rng = random.Random(saat)
    nrng = np.random.default_rng(saat)
    t0 = time.time()
    erg = {"meta": {"modus": modus, "python": platform.python_version(), "numpy": np.__version__, "saat": saat}}
    zeiten = {}
    # KD0
    kd0 = {"dirac": pruefe_dirac(), "gitter": {}}
    gitter = {}
    for L in ([2, 3, 4] if haupt else [2, 3]):
        r, D, S, W = lauf_kd0_gitter(L)
        kd0["gitter"]["L%d" % L] = r
        gitter[L] = (D, S, W)
    erg["kd0"] = kd0
    zeiten["kd0"] = round(time.time() - t0, 2)
    # KD1: Abbildung
    kd1 = {"knoten": lauf_majorana_knoten()}
    D3, S3, W3 = gitter[3]
    mg, sig_je_hex = lauf_majorana_gitter(D3, S3, W3)
    kd1["gitter_L3"] = mg
    kd1["u1_L3"] = lauf_u1(D3, S3)
    hi = 0
    sig0 = sig_je_hex[hi]
    kd1["sechseck_ed"] = {"uniform": lauf_sechseck_ed(D3, hi, sig0, (1.0, 1.0, 1.0, 1.0))}
    if haupt:
        kd1["sechseck_ed"]["allgemein"] = lauf_sechseck_ed(D3, hi, sig0, (1.0, 0.7, 1.3, 0.9))
    kd1["sechseck_ed"]["typen"] = [D3.bonds[bi][2] for bi in D3.sechsecke()[hi][1]]
    kd1["cluster112"] = {"uniform": lauf_cluster112((1.0, 1.0, 1.0, 1.0))}
    if haupt:
        kd1["cluster112"]["allgemein"] = lauf_cluster112((1.0, 0.7, 1.3, 0.9))
    zeiten["kd1_abbildung"] = round(time.time() - t0, 2)
    kr = lauf_kraum(haupt, nrng)
    kd1["kraum"] = {k: v for k, v in kr.items() if k in ("code_pruefung", "J1")}
    kd1["fluss_realraum"] = lauf_fluss_realraum(nrng, haupt)
    erg["kd1"] = kd1
    erg["kd2"] = {"scan": kr["scan"], "faelle": kr["kd2"]}
    zeiten["kraum"] = round(time.time() - t0, 2)
    # KD3
    kd3 = {"lokal_L4": lauf_lokal(4, ("a", "z", "az"))}
    kd3["lang_L8"] = lauf_lang(rng, 300 if haupt else 3)
    erg["kd3"] = kd3
    zeiten["kd3"] = round(time.time() - t0, 2)
    try:
        bild(bildpfad, kr)
        erg["bild"] = os.path.basename(bildpfad)
    except Exception as e:  # Bild ist Beigabe; Fehler wird vermerkt
        erg["bild_fehler"] = repr(e)
    erg["nullen_J1_theta"] = kr["_nullen_J1"][:50]
    erg["zeiten_s"] = zeiten
    erg["laufzeit_s"] = round(time.time() - t0, 2)
    with open(aus + ".tmp", "w") as fh:
        json.dump(erg, fh, indent=1, sort_keys=True, ensure_ascii=False)
    os.replace(aus + ".tmp", aus)
    print("fertig", modus, erg["laufzeit_s"], "s")


if __name__ == "__main__":
    main()
