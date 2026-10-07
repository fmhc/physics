#!/usr/bin/env python3
"""TWIST-PYRO-1 (Runde 40, fmhc-physics): Levin/Wen-Drehung auf kubischem Gitter, Diamant- und Pyrochlor-Kanten.

Quelle [S]: M. Levin, X.-G. Wen, Phys. Rev. B 73, 035122 (2006), arXiv:hep-th/0507118v2:
  Gl. (8)  W~(C) = W(C) (-1)^{Sum_{legs of C} n^c_i L^z_i}, n^c_i = Zahl der Kreuzungen von Kante i mit der Rahmung C'
  Fig. 5   Plakettenrahmung "up and to the left";  Fig. 6 / Gl. (11) Huepferrahmung "down and to the right"
  Gl. (12) L~+_i L~-_j L~+_k = (-1) L~+_k L~-_j L~+_i fuer i, j, k an einem Knoten
Vorzeichenalgebra exakt ueber GF(2): L+- -> X, (-1)^{L^z} -> Z (PLAN.md 1.1). Keine Gleitkommazahl.
Lesart S: nur Kreuzungen nahe dem Kurvenknoten zaehlen; Lesart V: alle Kreuzungen der Beinstrecke (PLAN.md 1.4).
Aufruf: python twist_pyro.py <rauch|haupt> <ausgabe.json>
"""
import sys
import json
import time
import itertools
import platform
import os

S_SKALA = 1 << 30
PROJ = {
    "P1": ((20, 8, 0), (0, 7, 20)),     # LW-artig, Blickrichtung (-8, 20, -7); Rauch 1/2: (10,4,0),(0,3,10)
    "P2": ((11, -10, 0), (6, 0, -5)),   # nahe [111], Blickrichtung (10, 11, 12)
    "P3": ((9, -5, 0), (17, 0, -5)),    # schraeg, Blickrichtung (5, 9, 17); Rauch 1/2: (5,-2,0),(9,0,-2); Rauch 3: (7,-3,0),(13,0,-3)
}
DELTA_P = (-5, 4)   # Schleifen: links oben
DELTA_H = (5, -4)   # Huepfer: rechts unten (= -DELTA_P)
NAH = 10 ** 5       # nah: t < 1e-5
FERN = 10 ** 3      # fern: 1e-3 < t < 1 - 1e-3
D4 = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
KUB = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


# ------------------------------------------------------------------ Pauli-Algebra (wie STRINGENDE-1)
class Pauli:
    __slots__ = ("k", "x", "z")

    def __init__(self, k=0, x=0, z=0):
        self.k = k % 4
        self.x = x
        self.z = z

    def __mul__(self, o):
        return Pauli(self.k + o.k + 2 * (self.z & o.x).bit_count(), self.x ^ o.x, self.z ^ o.z)


def sym(xa, za, xb, zb):
    return ((xa & zb).bit_count() + (za & xb).bit_count()) & 1


def phase_wert(d):
    d %= 4
    return {0: 1, 2: -1}.get(d, "i^%d" % d)


def zaehle(d, wert):
    s = str(wert)
    d[s] = d.get(s, 0) + 1


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub3(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def neg(a):
    return (-a[0], -a[1], -a[2])


# ------------------------------------------------------------------ Netze
class Netz:
    def __init__(self, art, n):
        self.art = art
        self.n = n
        if art == "kubisch":
            self.per = n
            self.sites = [(x, y, z) for x in range(n) for y in range(n) for z in range(n)]
        elif art == "diamant":
            self.per = 4 * n
            A = [(x, y, z) for x in range(0, 4 * n, 2) for y in range(0, 4 * n, 2) for z in range(0, 4 * n, 2)
                 if (x + y + z) % 4 == 0]
            self.sites = A + [self.mod(add(a, (1, 1, 1))) for a in A]
        elif art == "pyro":
            self.per = 8 * n
            A = [(x, y, z) for x in range(0, 8 * n, 4) for y in range(0, 8 * n, 4) for z in range(0, 8 * n, 4)
                 if (x + y + z) % 8 == 0]
            self.zentren_A = A
            self.sites = sorted({self.mod(add(a, d)) for a in A for d in D4})
        else:
            raise ValueError(art)
        self.idx = {s: i for i, s in enumerate(self.sites)}
        self.links = []
        self.lid = {}
        self.mehrfach = 0
        for s in self.sites:
            nb = set()
            for b in self.bonds(s):
                t = self.mod(add(s, b))
                if t == s or t in nb:
                    self.mehrfach += 1
                nb.add(t)
                key = frozenset((self.idx[s], self.idx[t]))
                if key in self.lid:
                    continue
                tail, head = self.orient(s, b, t)
                self.lid[key] = len(self.links)
                self.links.append((self.idx[tail], self.idx[head]))

    def mod(self, p):
        return (p[0] % self.per, p[1] % self.per, p[2] % self.per)

    def pyro_d(self, s):
        for d in D4:
            a = sub3(s, d)
            if a[0] % 4 == 0 and a[1] % 4 == 0 and a[2] % 4 == 0 and (a[0] + a[1] + a[2]) % 8 == 0:
                return d
        raise ValueError(("kein Pyrochlor-Knoten", s))

    def bonds(self, s):
        if self.art == "kubisch":
            return KUB
        if self.art == "diamant":
            return D4 if s[0] % 2 == 0 else tuple(neg(d) for d in D4)
        d = self.pyro_d(s)
        out = []
        for d2 in D4:
            if d2 != d:
                v = sub3(d2, d)
                out.append(v)
                out.append(neg(v))
        return tuple(out)

    def orient(self, s, b, t):
        if self.art == "kubisch":
            pos = sum(b) > 0
        elif self.art == "diamant":
            pos = s[0] % 2 == 0          # A -> B
        else:
            nz = [c for c in b if c != 0]
            pos = nz[0] > 0
        return (s, t) if pos else (t, s)

    def kante_id(self, u, w):
        return self.lid[frozenset((self.idx[self.mod(u)], self.idx[self.mod(w)]))]

    def grad(self):
        return len(self.bonds(self.sites[0]))

    # ---------------- kleinste Schleifen (Knotenlisten in der Ueberlagerung)
    def schleifen(self):
        res = {}
        if self.art == "kubisch":
            for v in self.sites:
                for a, b in ((0, 1), (1, 2), (0, 2)):
                    ea = [0, 0, 0]
                    ea[a] = 1
                    eb = [0, 0, 0]
                    eb[b] = 1
                    ea, eb = tuple(ea), tuple(eb)
                    self._merke(res, [v, add(v, ea), add(add(v, ea), eb), add(v, eb)], "plakette")
        if self.art == "pyro":
            for A in self.zentren_A:
                for zentrum, ecken in ((A, [add(A, d) for d in D4]),
                                       (add(A, (2, 2, 2)), [sub3(add(A, (2, 2, 2)), d) for d in D4])):
                    for tri in itertools.combinations(ecken, 3):
                        self._merke(res, list(tri), "dreieck")
        if self.art in ("diamant", "pyro"):
            for s0 in self.sites:
                i0 = self.idx[s0]
                self._dfs6(res, s0, i0, [s0])
        return list(res.values())

    def _dfs6(self, res, s0, i0, pfad):
        cur = pfad[-1]
        k = len(pfad) - 1
        for b in self.bonds(cur):
            nxt = add(cur, b)
            if k == 5:
                if nxt == s0:
                    self._merke(res, list(pfad), "sechseck")
                continue
            if nxt in pfad or self.idx[self.mod(nxt)] < i0:
                continue
            self._dfs6(res, s0, i0, pfad + [nxt])

    def _merke(self, res, knoten, typ):
        k = len(knoten)
        ids = frozenset(self.kante_id(knoten[i], knoten[(i + 1) % k]) for i in range(k))
        if ids not in res:
            res[ids] = {"knoten": knoten, "typ": typ}


# ------------------------------------------------------------------ Projektion und Kreuzungen
def proj(M, r):
    return (S_SKALA * (M[0][0] * r[0] + M[0][1] * r[1] + M[0][2] * r[2]),
            S_SKALA * (M[1][0] * r[0] + M[1][1] * r[1] + M[1][2] * r[2]))


def cr(a, b):
    return a[0] * b[1] - a[1] * b[0]


def schnitt(A, B, C, D):
    """Strecke AB (Bein) gegen Strecke CD (Rahmung): None, 'ent' oder (tn, td) mit t = tn/td auf AB."""
    d1 = (B[0] - A[0], B[1] - A[1])
    d2 = (D[0] - C[0], D[1] - C[1])
    w = (C[0] - A[0], C[1] - A[1])
    den = cr(d1, d2)
    if den == 0:
        if cr(w, d1) == 0:
            dd = d1[0] * d1[0] + d1[1] * d1[1]
            tc = w[0] * d1[0] + w[1] * d1[1]
            td_ = (D[0] - A[0]) * d1[0] + (D[1] - A[1]) * d1[1]
            lo, hi = min(tc, td_), max(tc, td_)
            if max(lo, 0) <= min(hi, dd):
                return "ent"
        return None
    tn = cr(w, d2)
    sn = cr(w, d1)
    if den < 0:
        den, tn, sn = -den, -tn, -sn
    if tn < 0 or tn > den or sn < 0 or sn > den:
        return None
    if tn == 0 or tn == den or sn == 0 or sn == den:
        return "ent"
    return (tn, den)


def drehung(netz, M, kurve, geschlossen, delta, z):
    """Drehmengen (Lesart S, Lesart V) als Bitmengen auf dem Torus fuer eine Kurve (Knotenliste in der Ueberlagerung)."""
    pts = [proj(M, v) for v in kurve]
    rahmen = [(p[0] + delta[0], p[1] + delta[1]) for p in pts]
    k = len(kurve)
    kanten = [(rahmen[i], rahmen[i + 1], i, i + 1) for i in range(k - 1)]
    if geschlossen:
        kanten.append((rahmen[k - 1], rahmen[0], k - 1, 0))
    pos = {v: i for i, v in enumerate(kurve)}
    beine = {}
    for v in kurve:
        for b in netz.bonds(v):
            w = add(v, b)
            beine.setdefault(frozenset((v, w)), (v, w))
    ZS = 0
    ZV = 0
    gesehen = set()
    for (u, w) in beine.values():
        Pu, Pw = proj(M, u), proj(M, w)
        nS = 0
        nV = 0
        for (C, D, ia, ib) in kanten:
            r = schnitt(Pu, Pw, C, D)
            if r is None:
                continue
            if r == "ent":
                z["ent_schnitt"] += 1
                continue
            tn, td = r
            nV += 1
            nah_u = u in pos and tn * NAH < td and pos[u] in (ia, ib)
            nah_w = w in pos and (td - tn) * NAH < td and pos[w] in (ia, ib)
            if nah_u or nah_w:
                nS += 1
                z["nah"] += 1
            elif tn * FERN > td and (td - tn) * FERN > td:
                z["fern"] += 1
            else:
                z["unklar"] += 1
                if len(z["unklar_beispiele"]) < 6:
                    z["unklar_beispiele"].append({"kurve": [list(v) for v in kurve], "bein": [list(u), list(w)],
                                                  "t": "%.3e" % (tn / td), "rahmenkante": [ia, ib],
                                                  "u_auf_kurve": u in pos, "w_auf_kurve": w in pos})
        l = netz.kante_id(u, w)
        if l in gesehen:
            z["torus_zusammenfall"] += 1
        gesehen.add(l)
        if nS & 1:
            ZS ^= 1 << l
        if nV & 1:
            ZV ^= 1 << l
    return ZS, ZV


def knoten_entartung(netz, M):
    """Zwei Kanten eines Knotens projiziert gleichgerichtet, oder eine Kante parallel zu delta."""
    f = 0
    for s in netz.sites:
        dirs = [(M[0][0] * b[0] + M[0][1] * b[1] + M[0][2] * b[2], M[1][0] * b[0] + M[1][1] * b[1] + M[1][2] * b[2])
                for b in netz.bonds(s)]
        for d in dirs:
            if d == (0, 0) or cr(d, DELTA_P) == 0:
                f += 1
        for a, b in itertools.combinations(dirs, 2):
            if cr(a, b) == 0 and a[0] * b[0] + a[1] * b[1] > 0:
                f += 1
    return f


# ------------------------------------------------------------------ Messungen
def ladung_ok(netz, kurve):
    dq = {}
    k = len(kurve)
    for i in range(k):
        a, b = kurve[i], kurve[(i + 1) % k]
        ia, ib = netz.idx[netz.mod(a)], netz.idx[netz.mod(b)]
        tail, head = netz.links[netz.kante_id(a, b)]
        if (ia, ib) == (tail, head):
            f = 1
        elif (ia, ib) == (head, tail):
            f = -1
        else:
            return False
        dq[head] = dq.get(head, 0) + f
        dq[tail] = dq.get(tail, 0) - f
    return all(v == 0 for v in dq.values())


def einfach(netz, kurve):
    k = len(kurve)
    return len({netz.mod(v) for v in kurve}) == k and \
        len({netz.kante_id(kurve[i], kurve[(i + 1) % k]) for i in range(k)}) == k


def t2_messung(netz, hop_x, hop_z):
    """Vorzeichen nach Gl. (12) fuer alle geordneten Tripel an allen Knoten. V1 Paulimultiplikation, V3 symplektisch."""
    r = {"V1": {}, "inkonsistent": 0, "anzahl": 0}
    for s in netz.sites:
        ls = [netz.kante_id(s, add(s, b)) for b in netz.bonds(s)]
        P = {l: Pauli(0, hop_x[l], hop_z[l]) for l in ls}
        for i, j, k in itertools.permutations(ls, 3):
            A = P[i] * P[j] * P[k]
            B = P[k] * P[j] * P[i]
            v1 = phase_wert(A.k - B.k) if (A.x == B.x and A.z == B.z) else "A!=B"
            e = sym(P[i].x, P[i].z, P[j].x, P[j].z) + sym(P[i].x, P[i].z, P[k].x, P[k].z) \
                + sym(P[j].x, P[j].z, P[k].x, P[k].z)
            v3 = -1 if e & 1 else 1
            if v1 != v3:
                r["inkonsistent"] += 1
            zaehle(r["V1"], v1)
            r["anzahl"] += 1
    return r


def schleifen_paare(schl, zkey):
    n = len(schl)
    cnt = 0
    nach_typ = {}
    beisp = []
    for i in range(n):
        Xi, Zi = schl[i]["X"], schl[i][zkey]
        for j in range(i + 1, n):
            if ((Xi & schl[j][zkey]).bit_count() + (Zi & schl[j]["X"]).bit_count()) & 1:
                cnt += 1
                key = "|".join(sorted((schl[i]["typ"], schl[j]["typ"])))
                nach_typ[key] = nach_typ.get(key, 0) + 1
                if len(beisp) < 5:
                    beisp.append([[list(v) for v in schl[i]["knoten"]], [list(v) for v in schl[j]["knoten"]]])
    return {"paare": n * (n - 1) // 2, "antikommut": cnt, "nach_typ": nach_typ, "beispiele": beisp}


def huepfer_schleifen(hop_x, hop_z, schl, zkey):
    cnt = 0
    for l in range(len(hop_x)):
        x, z = hop_x[l], hop_z[l]
        for p in schl:
            if ((x & p[zkey]).bit_count() + (z & p["X"]).bit_count()) & 1:
                cnt += 1
    return {"paare": len(hop_x) * len(schl), "antikommut": cnt}


def lauf_netz(art, n):
    t0 = time.time()
    N = Netz(art, n)
    roh = N.schleifen()
    schl = []
    t1a_fehler = 0
    nicht_einfach = 0
    typen = {}
    for s in roh:
        kn = s["knoten"]
        k = len(kn)
        X = 0
        for i in range(k):
            X ^= 1 << N.kante_id(kn[i], kn[(i + 1) % k])
        if not ladung_ok(N, kn):
            t1a_fehler += 1
        if not einfach(N, kn):
            nicht_einfach += 1
        typen[s["typ"]] = typen.get(s["typ"], 0) + 1
        schl.append({"knoten": kn, "typ": s["typ"], "X": X})
    erw = {"kubisch": {"plakette": 3 * n ** 3}, "diamant": {"sechseck": 16 * n ** 3},
           "pyro": {"dreieck": 32 * n ** 3, "sechseck": 16 * n ** 3}}[art]
    out = {"art": art, "n": n, "knoten": len(N.sites), "kanten": len(N.links), "grad": N.grad(),
           "mehrfach_fehler": N.mehrfach, "schleifen": typen, "schleifen_erwartet": erw,
           "T1a_fehler": t1a_fehler, "nicht_einfach": nicht_einfach}
    nl = len(N.links)
    hop_x = [1 << l for l in range(nl)]
    # Huepfer: Darstellung in der Ueberlagerung
    hop_kurve = []
    for l, (ti, hi) in enumerate(N.links):
        u = N.sites[ti]
        w = None
        for b in N.bonds(u):
            if N.idx[N.mod(add(u, b))] == hi:
                w = add(u, b)
        hop_kurve.append([u, w])
    out["T3"] = t2_messung(N, hop_x, [0] * nl)
    out["proj"] = {}
    for pn, M in PROJ.items():
        z = {"ent_schnitt": 0, "unklar": 0, "fern": 0, "nah": 0, "torus_zusammenfall": 0, "unklar_beispiele": []}
        r = {"ent_knoten": knoten_entartung(N, M)}
        for s in schl:
            s["ZS"], s["ZV"] = drehung(N, M, s["knoten"], True, DELTA_P, z)
        hz = {"S": [0] * nl, "V": [0] * nl}
        gz = {"S": [0] * nl, "V": [0] * nl}
        for l in range(nl):
            hz["S"][l], hz["V"][l] = drehung(N, M, hop_kurve[l], False, DELTA_H, z)
            gz["S"][l], gz["V"][l] = drehung(N, M, hop_kurve[l], False, DELTA_P, z)
        r.update(z)
        r["schleifen_mit_fernanteil"] = sum(1 for s in schl if s["ZS"] != s["ZV"])
        r["huepfer_mit_fernanteil"] = sum(1 for l in range(nl) if hz["S"][l] != hz["V"][l])
        for les in ("S", "V"):
            zk = "Z" + les
            R = {}
            R["T1b"] = schleifen_paare(schl, zk)
            R["T2"] = t2_messung(N, hop_x, hz[les])
            R["Z3"] = huepfer_schleifen(hop_x, hz[les], schl, zk)
            R["G1_gleichsinnig"] = huepfer_schleifen(hop_x, gz[les], schl, zk)
            r[les] = R
        out["proj"][pn] = r
    out["zeit_s"] = round(time.time() - t0, 2)
    return out


def main():
    modus, aus = sys.argv[1], sys.argv[2]
    if modus == "rauch":
        groessen = [("kubisch", 3), ("diamant", 2), ("pyro", 1)]
    else:
        groessen = [("kubisch", 3), ("kubisch", 4), ("diamant", 2), ("diamant", 3), ("pyro", 1), ("pyro", 2)]
    t0 = time.time()
    erg = {"meta": {"modus": modus, "python": platform.python_version(), "S_SKALA": S_SKALA,
                    "PROJ": {k: [list(r) for r in v] for k, v in PROJ.items()}, "DELTA_P": list(DELTA_P),
                    "DELTA_H": list(DELTA_H), "NAH": "t < 1e-5", "FERN": "1e-3 < t < 1-1e-3"},
           "netze": {}}
    for art, n in groessen:
        erg["netze"]["%s-%d" % (art, n)] = lauf_netz(art, n)
        print(art, n, erg["netze"]["%s-%d" % (art, n)]["zeit_s"], "s", flush=True)
    erg["laufzeit_s"] = round(time.time() - t0, 2)
    with open(aus + ".tmp", "w") as fh:
        json.dump(erg, fh, indent=1, sort_keys=True)
    os.replace(aus + ".tmp", aus)
    print("fertig", modus, erg["laufzeit_s"], "s")


if __name__ == "__main__":
    main()
