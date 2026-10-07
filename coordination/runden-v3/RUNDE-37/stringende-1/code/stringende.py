#!/usr/bin/env python3
"""STRINGENDE-1 (Runde 37, fmhc-physics): Vertauschungsphasen von Stringenden, exakt ueber GF(2).

Regel [S]: Levin/Wen 2003, Phys. Rev. B 67, 245316 (arXiv cond-mat/0302460v2), Eq. (4):
    t_il t_ki t_ij = e^{i theta} t_ij t_ki t_il ;  t_ij bewegt ein Teilchen von j nach i (Eq. 2).
Kartenform (umgestellt): e^{i theta} = W3 W2^-1 W1 W3^-1 W2 W1^-1 mit W1 = W_ij, W2 = W_ik, W3 = W_il.
Paulioperatoren als i^k X^x Z^z (x, z Bitvektoren als Python-int, k mod 4). Keine Zustandsvektoren, kein float.
Aufruf: python stringende.py <rauch|haupt> <ausgabe.json>
"""
import sys
import json
import time
import random
import itertools
import platform


# ------------------------------------------------------------------ Pauli-Algebra
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

    def ist_eins(self):
        return self.x == 0 and self.z == 0 and self.k == 0

    def ist_phase(self):
        return self.x == 0 and self.z == 0

    def hermitesch(self):
        return (self.k - (self.x & self.z).bit_count()) % 2 == 0

    def gleich(self, o):
        return self.k == o.k and self.x == o.x and self.z == o.z

    def verschoben(self, n):
        return Pauli(self.k, self.x << n, self.z << n)


def sym(a, b):
    """1, wenn a und b antikommutieren, sonst 0."""
    return ((a.x & b.z).bit_count() + (a.z & b.x).bit_count()) & 1


def Xq(q):
    return Pauli(0, 1 << q, 0)


def Zq(q):
    return Pauli(0, 0, 1 << q)


def Yq(q):
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
    """W1 = W_ij (j->i), W2 = W_ik (k->i), W3 = W_il (l->i). Rueckgabe (V1, V2, V3)."""
    Wki = W2.inv()
    A = W3 * Wki * W1  # W_il W_ki W_ij
    B = W1 * Wki * W3  # W_ij W_ki W_il
    v1 = phase_wert(A.k - B.k) if (A.x == B.x and A.z == B.z) else "A!=B"
    C = W3 * W2.inv() * W1 * W3.inv() * W2 * W1.inv()
    v2 = phase_wert(C.k) if C.ist_phase() else "keine Phase"
    v3 = -1 if (sym(W1, W2) + sym(W1, W3) + sym(W2, W3)) & 1 else 1
    return v1, v2, v3


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


def zaehle(d, wert):
    s = str(wert)
    d[s] = d.get(s, 0) + 1


# ------------------------------------------------------------------ Wege
def lerw(rng, start, ziel, erlaubt, nachbarn):
    """Schleifengeloeschter Zufallsweg von start bis ziel, Schritte nur in 'erlaubt'."""
    pfad = [start]
    pos = {start: 0}
    cur = start
    n = 0
    while cur != ziel:
        nb = [q for q in nachbarn(cur) if q in erlaubt]
        nxt = nb[rng.randrange(len(nb))]
        n += 1
        if n > 2_000_000:
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


def manhattan(start, ziel):
    pfad = [tuple(start)]
    cur = list(start)
    for ax in range(len(start)):
        while cur[ax] != ziel[ax]:
            cur[ax] += 1 if ziel[ax] > cur[ax] else -1
            pfad.append(tuple(cur))
    return pfad


def nachbarn2(p):
    x, y = p
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def nachbarn3(p):
    x, y, z = p
    return ((x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1))


def box2(x1, x2, y1, y2):
    return {(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)}


def box3(x1, x2, y1, y2, z1, z2):
    return {(x, y, z) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) for z in range(z1, z2 + 1)}


def rechteck_zyklus(x1, x2, y1, y2):
    c = [(x, y1) for x in range(x1, x2 + 1)]
    c += [(x2, y) for y in range(y1 + 1, y2 + 1)]
    c += [(x, y2) for x in range(x2 - 1, x1 - 1, -1)]
    c += [(x1, y) for y in range(y2 - 1, y1 - 1, -1)]
    return c


# ------------------------------------------------------------------ 2D Torus-Code
class Torus2D:
    def __init__(self, L, lagen=1):
        self.L = L
        self.lagen = lagen
        self.nq = 2 * L * L * lagen
        self.sterne = {}
        self.plak = {}
        for l in range(lagen):
            for x in range(L):
                for y in range(L):
                    self.sterne[(l, x, y)] = prod([Xq(q) for q in (self.h(x, y, l), self.h(x - 1, y, l),
                                                                   self.v(x, y, l), self.v(x, y - 1, l))])
                    self.plak[(l, x, y)] = prod([Zq(q) for q in (self.h(x, y, l), self.h(x, y + 1, l),
                                                                 self.v(x, y, l), self.v(x + 1, y, l))])
        self.bx = GF2()
        self.bz = GF2()
        for S in self.sterne.values():
            self.bx.add(S.x)
        for B in self.plak.values():
            self.bz.add(B.z)

    def h(self, x, y, l=0):
        L = self.L
        return l * 2 * L * L + 2 * ((y % L) * L + (x % L))

    def v(self, x, y, l=0):
        L = self.L
        return l * 2 * L * L + 2 * ((y % L) * L + (x % L)) + 1

    def kante(self, a, b, l=0):
        (x1, y1), (x2, y2) = a, b
        d = (x2 - x1, y2 - y1)
        if d == (1, 0):
            return self.h(x1, y1, l)
        if d == (-1, 0):
            return self.h(x2, y2, l)
        if d == (0, 1):
            return self.v(x1, y1, l)
        if d == (0, -1):
            return self.v(x2, y2, l)
        raise ValueError((a, b))

    def dualkante(self, p, q, l=0):
        (x1, y1), (x2, y2) = p, q
        d = (x2 - x1, y2 - y1)
        if d == (1, 0):
            return self.v(x1 + 1, y1, l)
        if d == (-1, 0):
            return self.v(x1, y1, l)
        if d == (0, 1):
            return self.h(x1, y1 + 1, l)
        if d == (0, -1):
            return self.h(x1, y1, l)
        raise ValueError((p, q))

    def zpfad(self, knoten, l=0):
        z = 0
        for a, b in zip(knoten, knoten[1:]):
            z ^= 1 << self.kante(a, b, l)
        return Pauli(0, 0, z)

    def xpfad(self, plaketten, l=0):
        x = 0
        for p, q in zip(plaketten, plaketten[1:]):
            x ^= 1 << self.dualkante(p, q, l)
        return Pauli(0, x, 0)

    def anecken(self, W):
        m = set()
        for key, S in self.sterne.items():
            if sym(W, S):
                m.add(("A",) + key)
        for key, B in self.plak.items():
            if sym(W, B):
                m.add(("B",) + key)
        return m

    def in_gruppe(self, P):
        return self.bx.enthaelt(P.x) and self.bz.enthaelt(P.z)

    def m(self, p):
        return (p[0] % self.L, p[1] % self.L)


GEOM2 = {
    "G1": [((1, 4), (1, 6, 4, 6)), ((8, 11), (6, 8, 6, 11)), ((11, 3), (6, 11, 3, 6))],
    "G2": [((8, 1), (6, 8, 1, 6)), ((1, 8), (1, 6, 6, 8)), ((9, 11), (6, 9, 6, 11))],
    "G3": [((11, 8), (6, 11, 6, 8)), ((4, 1), (4, 6, 1, 6)), ((1, 9), (1, 6, 6, 9))],
    "G4": [((4, 11), (4, 6, 6, 11)), ((11, 4), (6, 11, 4, 6)), ((3, 1), (3, 6, 1, 6))],
}
MITTE2 = (6, 6)

# Sorte -> (Lage des Z-Teils oder None, Lage des X-Teils oder None)
SORTEN1 = {"e": (0, None), "m": (None, 0), "eps": (0, 0)}
SORTEN2 = {"e0m1": (0, 1), "e1m0": (1, 0), "e0m0": (0, 0), "e1m1": (1, 1)}


def pruefe_geometrie2(beine):
    for a, (oa, (x1, x2, y1, y2)) in enumerate(beine):
        assert x1 <= oa[0] <= x2 and y1 <= oa[1] <= y2
        assert x1 <= MITTE2[0] <= x2 and y1 <= MITTE2[1] <= y2
        for b, (ob, _) in enumerate(beine):
            if a != b:
                assert not (x1 <= ob[0] <= x2 and y1 <= ob[1] <= y2), ("Geometrie", a, b)


def bein_wege2(rng, bein, zufall):
    o, (x1, x2, y1, y2) = bein
    erlaubt = box2(x1, x2, y1, y2)
    if zufall:
        kp = lerw(rng, o, MITTE2, erlaubt, nachbarn2)
        pp = lerw(rng, o, MITTE2, erlaubt, nachbarn2)
    else:
        kp = manhattan(o, MITTE2)
        pp = manhattan(o, MITTE2)
    return kp, pp


def string2(T, kp, pp, sorte_def):
    lz, lx = sorte_def
    W = Pauli()
    if lz is not None:
        W = W * T.zpfad(kp, lz)
    if lx is not None:
        W = W * T.xpfad(pp, lx)
    return W, (T.zpfad(kp, lz) if lz is not None else Pauli()), (T.xpfad(pp, lx) if lx is not None else Pauli())


def soll_anecken2(T, kp, pp, sorte_def):
    lz, lx = sorte_def
    s = set()
    if lz is not None:
        a, b = T.m(kp[0]), T.m(kp[-1])
        if a != b:
            s |= {("A", lz) + a, ("A", lz) + b}
    if lx is not None:
        a, b = T.m(pp[0]), T.m(pp[-1])
        if a != b:
            s |= {("B", lx) + a, ("B", lx) + b}
    return s


def lauf_lang2(T, rng, sorten, N, mit_zerlegung):
    erg = {}
    for gname, beine in GEOM2.items():
        pruefe_geometrie2(beine)
        erg[gname] = {}
        for sname, sdef in sorten.items():
            r = {"V1": {}, "inkonsistent": 0, "endpunkt_fehler": 0, "aequivalenz_fehler": 0, "anzahl": 0}
            if mit_zerlegung and sdef[0] is not None and sdef[1] is not None:
                r["zerlegung"] = {"z_teil": {}, "x_teil": {}, "kreuz": {}, "produkt_gleich_V1_fehler": 0}
            bezug = [None, None, None]
            for n in range(N + 1):
                Ws, Zs, Xs = [], [], []
                for a in range(3):
                    kp, pp = bein_wege2(rng, beine[a], zufall=(n > 0))
                    W, Zt, Xt = string2(T, kp, pp, sdef)
                    if T.anecken(W) != soll_anecken2(T, kp, pp, sdef):
                        r["endpunkt_fehler"] += 1
                    if n == 0:
                        bezug[a] = W
                    elif not T.in_gruppe(W * bezug[a].inv()):
                        r["aequivalenz_fehler"] += 1
                    Ws.append(W)
                    Zs.append(Zt)
                    Xs.append(Xt)
                v1, v2, v3 = vertauschung(Ws[0], Ws[1], Ws[2])
                if not (v1 == v2 == v3):
                    r["inkonsistent"] += 1
                zaehle(r["V1"], v1)
                r["anzahl"] += 1
                if "zerlegung" in r:
                    zt = vertauschung(Zs[0], Zs[1], Zs[2])[0]
                    xt = vertauschung(Xs[0], Xs[1], Xs[2])[0]
                    kr = 0
                    for a, b in itertools.combinations(range(3), 2):
                        kr += sym(Zs[a], Xs[b]) + sym(Xs[a], Zs[b])
                    kreuz = -1 if kr & 1 else 1
                    zaehle(r["zerlegung"]["z_teil"], zt)
                    zaehle(r["zerlegung"]["x_teil"], xt)
                    zaehle(r["zerlegung"]["kreuz"], kreuz)
                    if isinstance(zt, int) and isinstance(xt, int) and zt * xt * kreuz != v1:
                        r["zerlegung"]["produkt_gleich_V1_fehler"] += 1
            erg[gname][sname] = r
    return erg


def lauf_durchgang2(T):
    erg = {}
    for gname, beine in GEOM2.items():
        Ws = []
        for a in range(3):
            kp, pp = bein_wege2(None, beine[a], zufall=False)
            Ws.append(string2(T, kp, pp, SORTEN1["eps"])[0])
        basis = vertauschung(Ws[0], Ws[1], Ws[2])[0]
        vk = beine[1][0]
        pl = beine[2][0]
        proben = {
            "A(v_k)": (T.sterne[(0,) + T.m(vk)], "Wechsel"),
            "B(p_l)": (T.plak[(0,) + T.m(pl)], "Wechsel"),
            "A(v_k)B(p_l)": (T.sterne[(0,) + T.m(vk)] * T.plak[(0,) + T.m(pl)], "kein Wechsel"),
            "A(v0)": (T.sterne[(0,) + MITTE2], "kein Wechsel"),
            "B(p0)": (T.plak[(0,) + MITTE2], "kein Wechsel"),
        }
        g = {"basis_V1": basis}
        for name, (S, erw) in proben.items():
            v = vertauschung(Ws[0] * S, Ws[1], Ws[2])
            beob = "Wechsel" if v[0] != basis else "kein Wechsel"
            g[name] = {"erwartet": erw, "beobachtet": beob, "V": list(v), "passt": beob == erw}
        erg[gname] = g
    return erg


def lauf_lokal2(T):
    L = T.L
    erg = {}
    # eps nach Fig. 3: Plakette p, Ecke I, Z und X auf den beiden Kanten von p an I
    r = {"V1": {}, "inkonsistent": 0, "anzahl": 0}
    for x in range(L):
        for y in range(L):
            ecken = {
                (x, y): (T.h(x, y), T.v(x, y)),
                (x + 1, y): (T.h(x, y), T.v(x + 1, y)),
                (x, y + 1): (T.h(x, y + 1), T.v(x, y)),
                (x + 1, y + 1): (T.h(x, y + 1), T.v(x + 1, y)),
            }
            for _, (qa, qb) in ecken.items():
                hops = [Zq(qa), Zq(qb), Xq(qa), Xq(qb)]
                for t in itertools.permutations(range(4), 3):
                    v = vertauschung(hops[t[0]], hops[t[1]], hops[t[2]])
                    if not (v[0] == v[1] == v[2]):
                        r["inkonsistent"] += 1
                    zaehle(r["V1"], v[0])
                    r["anzahl"] += 1
    erg["eps_fig3"] = r
    for sname in ("e", "m"):
        r = {"V1": {}, "inkonsistent": 0, "anzahl": 0}
        for x in range(L):
            for y in range(L):
                if sname == "e":
                    hops = [Zq(q) for q in (T.h(x, y), T.h(x - 1, y), T.v(x, y), T.v(x, y - 1))]
                else:
                    hops = [Xq(q) for q in (T.h(x, y), T.h(x, y + 1), T.v(x, y), T.v(x + 1, y))]
                for t in itertools.permutations(range(4), 3):
                    v = vertauschung(hops[t[0]], hops[t[1]], hops[t[2]])
                    if not (v[0] == v[1] == v[2]):
                        r["inkonsistent"] += 1
                    zaehle(r["V1"], v[0])
                    r["anzahl"] += 1
        erg[sname] = r
    return erg


def zufallsrechteck(rng, L):
    x1 = rng.randrange(0, L - 1)
    x2 = rng.randrange(x1 + 1, L)
    y1 = rng.randrange(0, L - 1)
    y2 = rng.randrange(y1 + 1, L)
    return x1, x2, y1, y2


def lauf_gegenseitig2(T, rng, N):
    L = T.L
    erg = {}
    alles = box2(0, L - 1, 0, L - 1)
    enden = ((3, 3), (8, 8))
    # e um m
    pp = lerw(rng, enden[0], enden[1], alles, nachbarn2)
    Wm = T.xpfad(pp)
    r = {"faelle": 0, "abweichungen": 0, "schleife_nicht_stabilisator": 0, "klassen": {}}
    for _ in range(N):
        x1, x2, y1, y2 = zufallsrechteck(rng, L)
        C = T.zpfad(rechteck_zyklus(x1, x2, y1, y2))
        innen = [(x, y) for x in range(x1, x2) for y in range(y1, y2)]
        if not C.gleich(prod([T.plak[(0, x, y)] for (x, y) in innen])):
            r["schleife_nicht_stabilisator"] += 1
        n_um = sum(1 for e in enden if (x1 <= e[0] <= x2 - 1 and y1 <= e[1] <= y2 - 1))
        vorher = -1 if n_um % 2 else 1
        beob = -1 if sym(C, Wm) else 1
        zaehle(r["klassen"], "%d_umschlossen:%d" % (n_um, beob))
        r["faelle"] += 1
        if beob != vorher:
            r["abweichungen"] += 1
    erg["e_um_m"] = r
    # m um e
    kp = lerw(rng, enden[0], enden[1], alles, nachbarn2)
    We = T.zpfad(kp)
    r = {"faelle": 0, "abweichungen": 0, "schleife_nicht_stabilisator": 0, "klassen": {}}
    for _ in range(N):
        x1, x2, y1, y2 = zufallsrechteck(rng, L)
        C = T.xpfad(rechteck_zyklus(x1, x2, y1, y2))
        innen = [(x, y) for x in range(x1 + 1, x2 + 1) for y in range(y1 + 1, y2 + 1)]
        if not C.gleich(prod([T.sterne[(0, x, y)] for (x, y) in innen])):
            r["schleife_nicht_stabilisator"] += 1
        n_um = sum(1 for e in enden if (x1 + 1 <= e[0] <= x2 and y1 + 1 <= e[1] <= y2))
        vorher = -1 if n_um % 2 else 1
        beob = -1 if sym(C, We) else 1
        zaehle(r["klassen"], "%d_umschlossen:%d" % (n_um, beob))
        r["faelle"] += 1
        if beob != vorher:
            r["abweichungen"] += 1
    erg["m_um_e"] = r
    # lokale Form Abschnitt V: Z_q gegen X_q'
    r = {"paare": 0, "fehler": 0}
    for q in range(2 * L * L):
        for q2 in range(2 * L * L):
            s = sym(Zq(q), Xq(q2))
            if s != (1 if q == q2 else 0):
                r["fehler"] += 1
            r["paare"] += 1
    erg["lokal_abschnitt_V"] = r
    # eps um eps (beschreibend, Anhang-A-Konsistenz)
    kp = lerw(rng, enden[0], enden[1], alles, nachbarn2)
    pp = lerw(rng, enden[0], enden[1], alles, nachbarn2)
    Weps = T.zpfad(kp) * T.xpfad(pp)
    r = {"faelle": 0, "abweichungen": 0, "klassen": {}}
    for _ in range(N):
        x1, x2, y1, y2 = zufallsrechteck(rng, L)
        C = T.zpfad(rechteck_zyklus(x1, x2, y1, y2)) * T.xpfad(rechteck_zyklus(x1, x2 - 1, y1, y2 - 1)) \
            if (x2 - 1 > x1 and y2 - 1 > y1) else T.zpfad(rechteck_zyklus(x1, x2, y1, y2))
        zaehler = 0
        for e in enden:
            if x1 <= e[0] <= x2 - 1 and y1 <= e[1] <= y2 - 1:
                zaehler += 1  # e-Schleife umschliesst die Plakette des Endes
            if (x2 - 1 > x1 and y2 - 1 > y1) and (x1 + 1 <= e[0] <= x2 - 1 and y1 + 1 <= e[1] <= y2 - 1):
                zaehler += 1  # m-Schleife umschliesst den Knoten des Endes
        vorher = -1 if zaehler % 2 else 1
        beob = -1 if sym(C, Weps) else 1
        zaehle(r["klassen"], "zaehler%d:%d" % (zaehler, beob))
        r["faelle"] += 1
        if beob != vorher:
            r["abweichungen"] += 1
    erg["eps_um_eps_beschreibend"] = r
    # Endpunkte der drei Paar-Strings (SE0 a)
    f = 0
    f += T.anecken(Wm) != {("B", 0) + enden[0], ("B", 0) + enden[1]}
    f += T.anecken(We) != {("A", 0) + enden[0], ("A", 0) + enden[1]}
    f += T.anecken(Weps) != {("A", 0) + enden[0], ("A", 0) + enden[1], ("B", 0) + enden[0], ("B", 0) + enden[1]}
    erg["paar_endpunkt_fehler"] = int(f)
    return erg


def lauf_drehung2(T1, T2):
    erg = {}
    beine = GEOM2["G1"]
    kp, pp = bein_wege2(None, beine[0], zufall=False)
    W = T1.zpfad(kp) * T1.xpfad(pp)
    Rv = T1.sterne[(0,) + MITTE2]
    # Huepfprodukt des m-Teils NO -> NW -> SW -> SO -> NO um v0
    x, y = MITTE2
    hops = [Xq(T1.v(x, y)), Xq(T1.h(x - 1, y)), Xq(T1.v(x, y - 1)), Xq(T1.h(x, y))]
    R_hops = prod(hops)
    Rp = T1.plak[(0,) + MITTE2]
    erg["eps_um_e_teil"] = -1 if sym(Rv, W) else 1
    erg["huepfprodukt_gleich_A_v0"] = R_hops.gleich(Rv)
    erg["eps_um_m_teil"] = -1 if sym(Rp, W) else 1
    erg["vier_pi_ist_eins"] = (Rv * Rv).ist_eins() and (Rp * Rp).ist_eins()
    W2 = T2.zpfad(kp, 0) * T2.xpfad(pp, 1)
    erg["e0m1_um_e_teil"] = -1 if sym(T2.sterne[(1,) + MITTE2], W2) else 1
    erg["e0m1_um_m_teil"] = -1 if sym(T2.plak[(0,) + MITTE2], W2) else 1
    return erg


def lauf_stabilisatoren2(T):
    alle = list(T.sterne.values()) + list(T.plak.values())
    fehler = 0
    for a, b in itertools.combinations(alle, 2):
        fehler += sym(a, b)
    return {"anzahl": len(alle), "paar_fehler": fehler,
            "prod_A_eins": prod(list(T.sterne.values())).ist_eins(),
            "prod_B_eins": prod(list(T.plak.values())).ist_eins()}


# ------------------------------------------------------------------ 3D: Levin/Wen-Modell
RICHT = {"x": (1, 0, 0), "X": (-1, 0, 0), "y": (0, 1, 0), "Y": (0, -1, 0), "z": (0, 0, 1), "Z": (0, 0, -1)}
ACHSE = {"x": 0, "X": 0, "y": 1, "Y": 1, "z": 2, "Z": 2}
POS = "xyz"
BAR = {"x": "X", "X": "x", "y": "Y", "Y": "y", "z": "Z", "Z": "z"}
EBENE = {frozenset((0, 1)): "xy", frozenset((1, 2)): "yz", frozenset((0, 2)): "zx"}


def gamma_tabelle():
    X0, X1, Y0, Y1, Z0 = Xq(0), Xq(1), Yq(0), Yq(1), Zq(0)
    g = {"x": X0 * X1, "X": Y0 * X1, "y": Z0 * X1, "Y": Y1}  # Anhang B: s1(x)s1, s2(x)s1, s3(x)s1, s0(x)s2
    g5 = g["x"] * g["X"] * g["y"] * g["Y"]
    G = {}
    for a in "xXyY":
        G[(a, "z")] = g[a]                      # (B1)
        G[("z", a)] = g[a].neg()
        G[(a, "Z")] = (g[a] * g5).mal_i()       # (B2)
        G[("Z", a)] = G[(a, "Z")].neg()
        for b in "xXyY":
            if a != b:
                G[(a, b)] = (g[a] * g[b]).mal_i()  # (B3)
    G[("z", "Z")] = (G[("z", "x")] * G[("x", "Z")]).mal_i().neg()  # aus (12) abgeleitet [M]
    G[("Z", "z")] = G[("z", "Z")].neg()
    return G, g, g5


def pruefe_algebra(G, g):
    idx = "xXyYzZ"
    f = {"antisym": 0, "hermitesch": 0, "quadrat": 0, "kette": 0, "kommut": 0, "dirac_antikommut": 0}
    n = {"paare": 0, "ketten": 0, "vierer": 0}
    for a in idx:
        for b in idx:
            if a == b:
                continue
            n["paare"] += 1
            if not G[(a, b)].gleich(G[(b, a)].neg()):
                f["antisym"] += 1
            if not G[(a, b)].hermitesch():
                f["hermitesch"] += 1
            if not (G[(a, b)] * G[(a, b)]).ist_eins():
                f["quadrat"] += 1
            for c in idx:
                if c in (a, b):
                    continue
                n["ketten"] += 1
                if not (G[(a, b)] * G[(b, c)]).gleich(G[(a, c)].mal_i()):
                    f["kette"] += 1
                for d in idx:
                    if d in (a, b, c):
                        continue
                    n["vierer"] += 1
                    if sym(G[(a, b)], G[(c, d)]):
                        f["kommut"] += 1
    for a, b in itertools.combinations("xXyY", 2):
        if not sym(g[a], g[b]):
            f["dirac_antikommut"] += 1
    return f, n


class LW3D:
    def __init__(self, L, G):
        self.L = L
        self.G = G
        self.nq = 2 * L ** 3
        self.F = {}
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    i = (x, y, z)
                    self.F[("xy", i)] = (self.g("y", "x", i) * self.g("X", "y", self.add(i, (1, 0, 0)))
                                         * self.g("Y", "X", self.add(i, (1, 1, 0))) * self.g("x", "Y", self.add(i, (0, 1, 0))))
                    self.F[("yz", i)] = (self.g("z", "y", i) * self.g("Y", "z", self.add(i, (0, 1, 0)))
                                         * self.g("Z", "Y", self.add(i, (0, 1, 1))) * self.g("y", "Z", self.add(i, (0, 0, 1))))
                    self.F[("zx", i)] = (self.g("x", "z", i) * self.g("Z", "x", self.add(i, (0, 0, 1)))
                                         * self.g("X", "Z", self.add(i, (1, 0, 1))) * self.g("z", "X", self.add(i, (1, 0, 0))))
        self._basis = None

    def mod(self, p):
        return tuple(c % self.L for c in p)

    def add(self, p, d):
        return self.mod((p[0] + d[0], p[1] + d[1], p[2] + d[2]))

    def site(self, p):
        L = self.L
        return (p[0] % L) + L * ((p[1] % L) + L * (p[2] % L))

    def g(self, a, b, p):
        return self.G[(a, b)].verschoben(2 * self.site(p))

    def kante(self, s, a):
        """Kante am Knoten s in Richtung a (Buchstabe) -> (unterer Knoten mod L, Achse)."""
        if a in POS:
            return (self.mod(s), ACHSE[a])
        return (self.add(s, RICHT[a]), ACHSE[a])

    def angrenzend(self, kante):
        s, d = kante
        res = set()
        for e in range(3):
            if e == d:
                continue
            ori = EBENE[frozenset((d, e))]
            u = [0, 0, 0]
            u[e] = -1
            res.add((ori, self.mod(s)))
            res.add((ori, self.add(s, tuple(u))))
        return res

    def richtung(self, s, t):
        d = (t[0] - s[0], t[1] - s[1], t[2] - s[2])
        for a, v in RICHT.items():
            if v == d:
                return a
        raise ValueError((s, t))

    def huepfer(self, s, von, nach):
        """Huepfer am Knoten s von Kante (s, von) nach Kante (s, nach): gamma^{nach von}_s [S]."""
        return self.g(nach, von, s)

    def string(self, pfad):
        W = Pauli()
        for m in range(1, len(pfad) - 1):
            s = pfad[m]
            t = self.huepfer(s, self.richtung(s, pfad[m - 1]), self.richtung(s, pfad[m + 1]))
            W = t * W
        return W

    def endkanten(self, pfad):
        a = self.kante(pfad[0], self.richtung(pfad[0], pfad[1]))
        b = self.kante(pfad[-2], self.richtung(pfad[-2], pfad[-1]))
        return a, b

    def anecken(self, W):
        return {key for key, F in self.F.items() if sym(W, F)}

    def basis(self):
        if self._basis is None:
            b = GF2()
            for F in self.F.values():
                b.add((F.x << self.nq) | F.z)
            self._basis = b
        return self._basis

    def in_gruppe(self, P):
        return self.basis().enthaelt((P.x << self.nq) | P.z)


def lauf_modell3(L, G, voll):
    M = LW3D(L, G)
    r = {"L": L, "plaketten": len(M.F)}
    Fs = list(M.F.items())
    f_herm = sum(1 for _, F in Fs if not F.hermitesch())
    f_quad = sum(1 for _, F in Fs if not (F * F).ist_eins())
    f_komm = 0
    for (_, A), (_, B) in itertools.combinations(Fs, 2):
        f_komm += sym(A, B)
    r.update({"F_nicht_hermitesch": f_herm, "F_quadrat_fehler": f_quad, "F_paar_antikommut": f_komm})
    # Wuerfelprodukte
    wuerfel = {}
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = (x, y, z)
                flaechen = [("xy", i), ("xy", M.add(i, (0, 0, 1))), ("yz", i), ("yz", M.add(i, (1, 0, 0))),
                            ("zx", i), ("zx", M.add(i, (0, 1, 0)))]
                P = prod([M.F[f] for f in flaechen])
                zaehle(wuerfel, phase_wert(P.k) if P.ist_phase() else "kein Vielfaches der Eins")
    r["wuerfelprodukt"] = wuerfel
    # Huepfer-Eigenschaft
    f_hop = 0
    n_hop = 0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                s = (x, y, z)
                for a in "xXyYzZ":
                    for b in "xXyYzZ":
                        if a == b:
                            continue
                        t = M.g(a, b, s)
                        soll = M.angrenzend(M.kante(s, a)) ^ M.angrenzend(M.kante(s, b))
                        if M.anecken(t) != soll:
                            f_hop += 1
                        n_hop += 1
    r["huepfer_geprueft"] = n_hop
    r["huepfer_fehler"] = f_hop
    if voll:
        # 10-Huepfer-Aussagen und lokale Vertauschung nach Eq. (4)
        f10 = 0
        lok = {"V1": {}, "inkonsistent": 0, "anzahl": 0}
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    for c in POS:
                        s = (x, y, z)
                        t_ = M.add(s, RICHT[c])
                        nb = []  # (Knoten, Richtung der Nachbarkante, Richtung der Mittelkante)
                        for a in "xXyYzZ":
                            if a != c:
                                nb.append((s, a, c))
                        for a in "xXyYzZ":
                            if a != BAR[c]:
                                nb.append((t_, a, BAR[c]))
                        hops = [M.huepfer(u, a, cc) for (u, a, cc) in nb]
                        for p_, q_ in itertools.combinations(range(10), 2):
                            gleich_knoten = (p_ < 5) == (q_ < 5)
                            soll = 1 if gleich_knoten else 0
                            if sym(hops[p_], hops[q_]) != soll:
                                f10 += 1
                        for t3 in itertools.permutations(range(10), 3):
                            v = vertauschung(hops[t3[0]], hops[t3[1]], hops[t3[2]])
                            if not (v[0] == v[1] == v[2]):
                                lok["inkonsistent"] += 1
                            zaehle(lok["V1"], v[0])
                            lok["anzahl"] += 1
        r["zehn_huepfer_fehler"] = f10
        r["lokal"] = lok
    return r


BEINE3 = [
    # (aeusserer Knoten o0, o1, Quader, Ziel r, Anlauf)
    ((0, 3, 3), (1, 3, 3), (1, 3, 2, 6, 2, 6), (3, 4, 4), [(4, 4, 4), (5, 4, 4)]),
    ((5, 7, 5), (5, 6, 5), (2, 6, 5, 6, 2, 6), (4, 5, 4), [(4, 4, 4), (5, 4, 4)]),
    ((6, 5, 0), (6, 5, 1), (5, 7, 2, 6, 1, 3), (5, 4, 3), [(5, 4, 4), (4, 4, 4)]),
]


def pruefe_beine3():
    for a, (o0, o1, q, r, anl) in enumerate(BEINE3):
        x1, x2, y1, y2, z1, z2 = q
        inq = lambda p: x1 <= p[0] <= x2 and y1 <= p[1] <= y2 and z1 <= p[2] <= z2
        assert inq(o1) and inq(r) and not inq(o0)
        for p in anl:
            assert not inq(p)
        for b, (p0, p1, _, _, _) in enumerate(BEINE3):
            if a != b:
                assert not inq(p0) and not inq(p1), ("Quader", a, b)


def bein_pfad3(rng, bein, zufall):
    o0, o1, q, r, anl = bein
    erlaubt = box3(*q)
    mitte = lerw(rng, o1, r, erlaubt, nachbarn3) if zufall else manhattan(o1, r)
    return [o0] + mitte + anl


def lauf_lang3(G, rng, N, L=8):
    pruefe_beine3()
    M = LW3D(L, G)
    r = {"L": L, "V1": {}, "inkonsistent": 0, "endpunkt_fehler": 0, "aequivalenz_fehler": 0, "anzahl": 0}
    bezug = [None, None, None]
    for n in range(N + 1):
        Ws = []
        for a in range(3):
            pfad = bein_pfad3(rng, BEINE3[a], zufall=(n > 0))
            W = M.string(pfad)
            ka, kb = M.endkanten(pfad)
            if M.anecken(W) != (M.angrenzend(ka) ^ M.angrenzend(kb)):
                r["endpunkt_fehler"] += 1
            if n == 0:
                bezug[a] = W
            elif not M.in_gruppe(W * bezug[a].inv()):
                r["aequivalenz_fehler"] += 1
            Ws.append(W)
        v = vertauschung(Ws[0], Ws[1], Ws[2])
        if not (v[0] == v[1] == v[2]):
            r["inkonsistent"] += 1
        zaehle(r["V1"], v[0])
        r["anzahl"] += 1
    # Durchgangs-Gegenprobe 3D mit den Bezugswegen
    Ws = bezug
    basis = vertauschung(Ws[0], Ws[1], Ws[2])[0]
    pf = [bein_pfad3(None, BEINE3[a], zufall=False) for a in range(3)]
    ends = [M.endkanten(p) for p in pf]
    k_aussen = ends[1][0]
    j_aussen, l_aussen, mitte = ends[0][0], ends[2][0], ends[0][1]
    nur_k = sorted(M.angrenzend(k_aussen) - M.angrenzend(mitte) - M.angrenzend(j_aussen) - M.angrenzend(l_aussen))
    nur_c = sorted(M.angrenzend(mitte) - M.angrenzend(k_aussen) - M.angrenzend(j_aussen) - M.angrenzend(l_aussen))
    d = {"basis_V1": basis}
    for name, p, erw in (("F_p an Kante k", nur_k[0], "Wechsel"), ("F_p an Mittelkante", nur_c[0], "kein Wechsel")):
        v = vertauschung(Ws[0] * M.F[p], Ws[1], Ws[2])
        beob = "Wechsel" if v[0] != basis else "kein Wechsel"
        d[name] = {"plakette": [p[0], list(p[1])], "erwartet": erw, "beobachtet": beob, "V": list(v), "passt": beob == erw}
    r["durchgang"] = d
    r["mittelkante_alle_beine_gleich"] = all(e[1] == mitte for e in ends)
    return r


class Torus3D:
    def __init__(self, L):
        self.L = L
        self.nq = 3 * L ** 3
        self.A = {}
        self.B = {}
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    v = (x, y, z)
                    qs = [self.q(v, 0), self.q(v, 1), self.q(v, 2), self.q(self.add(v, (-1, 0, 0)), 0),
                          self.q(self.add(v, (0, -1, 0)), 1), self.q(self.add(v, (0, 0, -1)), 2)]
                    self.A[v] = prod([Xq(q) for q in qs])
                    for (d, e, ori) in ((0, 1, "xy"), (1, 2, "yz"), (0, 2, "zx")):
                        ud = [0, 0, 0]
                        ud[d] = 1
                        ue = [0, 0, 0]
                        ue[e] = 1
                        qs = [self.q(v, d), self.q(v, e), self.q(self.add(v, tuple(ue)), d), self.q(self.add(v, tuple(ud)), e)]
                        self.B[(ori, v)] = prod([Zq(q) for q in qs])

    def mod(self, p):
        return tuple(c % self.L for c in p)

    def add(self, p, d):
        return self.mod((p[0] + d[0], p[1] + d[1], p[2] + d[2]))

    def q(self, v, ax):
        L = self.L
        return 3 * ((v[0] % L) + L * ((v[1] % L) + L * (v[2] % L))) + ax

    def zpfad(self, pfad):
        z = 0
        for a, b in zip(pfad, pfad[1:]):
            d = tuple(b[i] - a[i] for i in range(3))
            ax = [i for i in range(3) if d[i] != 0]
            assert len(ax) == 1 and abs(d[ax[0]]) == 1
            ax = ax[0]
            unten = a if d[ax] == 1 else b
            z ^= 1 << self.q(unten, ax)
        return Pauli(0, 0, z)

    def anecken(self, W):
        m = {("A",) + k for k, S in self.A.items() if sym(W, S)}
        m |= {("B",) + (k[0],) + k[1] for k, S in self.B.items() if sym(W, S)}
        return m


def lauf_torus3(rng, N, L=8):
    T = Torus3D(L)
    stab_fehler = 0
    alle = list(T.A.values()) + list(T.B.values())
    # Stichprobe statt aller Paare (Laufzeit): alle A gegen alle B
    for S in T.A.values():
        for B in T.B.values():
            stab_fehler += sym(S, B)
    r = {"L": L, "V1": {}, "inkonsistent": 0, "endpunkt_fehler": 0, "anzahl": 0, "A_gegen_B_antikommut": stab_fehler,
         "stabilisatoren": len(alle)}
    mitte = (4, 4, 4)
    for n in range(N + 1):
        Ws = []
        for a in range(3):
            o0, o1, q, rr, anl = BEINE3[a]
            erlaubt = box3(*q)
            mit = lerw(rng, o1, rr, erlaubt, nachbarn3) if n > 0 else manhattan(o1, rr)
            pfad = [o0] + mit + ([mitte] if anl[0] == mitte else [anl[0], mitte])
            W = T.zpfad(pfad)
            soll = {("A",) + T.mod(o0), ("A",) + mitte}
            if T.anecken(W) != soll:
                r["endpunkt_fehler"] += 1
            Ws.append(W)
        v = vertauschung(Ws[0], Ws[1], Ws[2])
        if not (v[0] == v[1] == v[2]):
            r["inkonsistent"] += 1
        zaehle(r["V1"], v[0])
        r["anzahl"] += 1
    return r


# ------------------------------------------------------------------ Hauptprogramm
def main():
    modus = sys.argv[1]
    aus = sys.argv[2]
    t0 = time.time()
    haupt = modus == "haupt"
    rng = random.Random(37037 if haupt else 37001)
    N2 = 200 if haupt else 3
    N2b = 100 if haupt else 2
    N_schleifen = 300 if haupt else 10
    N3 = 300 if haupt else 3
    erg = {"meta": {"modus": modus, "python": platform.python_version(), "saat": 37037 if haupt else 37001,
                    "N2": N2, "N2_zweilagen": N2b, "N_schleifen": N_schleifen, "N3": N3}}
    T1 = Torus2D(12, 1)
    T2 = Torus2D(12, 2)
    z = {}
    z["stabilisatoren"] = lauf_stabilisatoren2(T1)
    z["lang"] = lauf_lang2(T1, rng, SORTEN1, N2, mit_zerlegung=True)
    z["zweilagen"] = lauf_lang2(T2, rng, SORTEN2, N2b, mit_zerlegung=False)
    z["durchgang"] = lauf_durchgang2(T1)
    z["lokal"] = lauf_lokal2(T1)
    z["gegenseitig"] = lauf_gegenseitig2(T1, rng, N_schleifen)
    z["drehung"] = lauf_drehung2(T1, T2)
    erg["zweiD"] = z
    erg["zeit_2D_s"] = round(time.time() - t0, 2)
    G, g, g5 = gamma_tabelle()
    d = {}
    f, n = pruefe_algebra(G, g)
    d["algebra"] = {"fehler": f, "anzahl": n, "gamma5": [g5.k, g5.x, g5.z], "gamma_zZ": [G[("z", "Z")].k, G[("z", "Z")].x, G[("z", "Z")].z]}
    d["L4"] = lauf_modell3(4, G, voll=True)
    if haupt:
        d["L6"] = lauf_modell3(6, G, voll=False)
    d["lang_L8"] = lauf_lang3(G, rng, N3, 8)
    d["torus3d_kontrolle"] = lauf_torus3(rng, N3, 8)
    erg["dreiD"] = d
    erg["laufzeit_s"] = round(time.time() - t0, 2)
    with open(aus + ".tmp", "w") as fh:
        json.dump(erg, fh, indent=1, sort_keys=True)
    import os
    os.replace(aus + ".tmp", aus)
    print("fertig", modus, erg["laufzeit_s"], "s")


if __name__ == "__main__":
    main()
