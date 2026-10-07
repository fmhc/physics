#!/usr/bin/env python3
"""TWIST-SPIN-1 (Runde 41, fmhc-physics): Wirken die Gitterdrehungen auf die verdrehten Levin/Wen-Huepfer als Symmetrie,
und welche Darstellung tragen die Fadenend-Fermionen? Exakte Rechnung ueber GF(2)/Z4, keine Gleitkommazahl im Urteil.

Importiert den eingefrorenen Code von TWIST-PYRO-1 unveraendert (twist_pyro.py, sha256 17875033...): Netze, kleinste
Schleifen, Projektionen P1-P3, Rahmungen (Schleifen links oben, Huepfer rechts unten), Lesart S.
Begriffe (PLAN.md Abschnitt 1 und 3):
  D(g)   Fehlmenge g T(C) + T(gC) der Drehmengen (Huepfer und Schleifen)
  Stufe W  jede Fehlmenge ist ein Korand (Summe von Sternen = Faktoren (-1)^Q je Knoten)        [Kartenwortlaut]
  Stufe K  Vertauschungsgraph K der Huepfer g-invariant; dann U'_g = V_g P_g (CZ-Phase) mit U' h_l = h_gl;
           dazu Schleifenvorzeichen sigma: U'(B~_p) = +B~_gp (bzw. Adjungierte)                          [Plan]
  Stufe F  Fermionfluss Phi_p (Huepferprodukt um p im Sektor B~ = +1) g-invariant                         [Zusatz]
  PSG    Eichfaktoren eta_g je Knoten fuer das Einteilchen-Huepfproblem, Relationswerte (C3)^3, (C2)^2, ...
Aufruf: python twist_spin.py <rauch|haupt> <ausgabe.json>
"""
import sys
import json
import time
import platform
import os
import twist_pyro as tp

Pauli = tp.Pauli
PS = ("P1", "P2", "P3")

# ------------------------------------------------------------------ Gruppen
A3 = ((0, 0, 1), (1, 0, 0), (0, 1, 0))      # C3 um [111]: (x,y,z) -> (z,x,y)
B2Z = ((-1, 0, 0), (0, -1, 0), (0, 0, 1))   # C2 um z
C4Z = ((0, -1, 0), (1, 0, 0), (0, 0, 1))    # C4 um z: (x,y,z) -> (-y,x,z)
B2D = ((0, -1, 0), (-1, 0, 0), (0, 0, -1))  # C2 um [1,-1,0]: (x,y,z) -> (-y,-x,-z)
EINS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
GRUPPEN = {
    "T": {"gen": {"a": A3, "b": B2Z}, "rel": {"C3^3": "aaa", "C2^2": "bb", "(C2C3)^3": "ababab"}},
    "O": {"gen": {"a": A3, "c": C4Z}, "rel": {"C3^3": "aaa", "C4^4": "cccc", "(C4C3)^2": "acac"}},
    "D3": {"gen": {"a": A3, "b": B2D}, "rel": {"C3^3": "aaa", "C2^2": "bb", "(C2C3)^2": "abab"}},
}
# Faelle: (Netz, Groessen haupt, Groessen rauch, Gruppe, Drehzentrum, Fixknoten oder None)
FAELLE = [
    ("diamant", [2, 3], [2], "T", (0, 0, 0), (0, 0, 0)),
    ("pyro", [1, 2], [1], "T", (0, 0, 0), None),
    ("pyro", [1, 2], [1], "D3", (1, 1, 1), (1, 1, 1)),
    ("kubisch", [3, 4], [3], "O", (0, 0, 0), (0, 0, 0)),
]
BEZUG_PYRO = (1, 1, 1)   # Normierungsknoten, wenn kein Knoten fest bleibt


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def mv(R, v):
    return (R[0][0] * v[0] + R[0][1] * v[1] + R[0][2] * v[2], R[1][0] * v[0] + R[1][1] * v[1] + R[1][2] * v[2],
            R[2][0] * v[0] + R[2][1] * v[1] + R[2][2] * v[2])


def gruppe_elemente(gen):
    """Abschluss per Breitensuche; Name = kuerzestes Wort (Buchstaben in Zeitfolge: erst links anwenden)."""
    el = {EINS: "e"}
    rand = [EINS]
    while rand:
        neu = []
        for R in rand:
            for b in sorted(gen):
                S = mm(gen[b], R)           # erst R, dann b
                if S not in el:
                    el[S] = ("" if el[R] == "e" else el[R]) + b
                    neu.append(S)
        rand = neu
    return el


def art_von(R):
    tr = R[0][0] + R[1][1] + R[2][2]
    return {3: "E", 0: "C3", -1: "C2", 1: "C4"}.get(tr, "?")


def wort_matrix(gen, wort):
    R = EINS
    for b in wort:
        R = mm(gen[b], R)
    return R


# ------------------------------------------------------------------ GF(2)-Hilfen
def popc(x):
    return x.bit_count()


class Graph:
    """Knoten-Kanten-Inzidenz fuer Korandloeser (delta y = D) per Breitensuche-Baum."""

    def __init__(self, N):
        self.nv = len(N.sites)
        self.links = N.links
        adj = [[] for _ in range(self.nv)]
        for l, (a, b) in enumerate(N.links):
            adj[a].append((b, l))
            adj[b].append((a, l))
        self.adj = adj
        self.ordnung = []
        self.eltern = [None] * self.nv
        gesehen = [False] * self.nv
        gesehen[0] = True
        q = [0]
        while q:
            v = q.pop(0)
            self.ordnung.append(v)
            for (w, l) in adj[v]:
                if not gesehen[w]:
                    gesehen[w] = True
                    self.eltern[w] = (v, l)
                    q.append(w)
        self.zusammenhaengend = all(gesehen)
        self.alle = (1 << self.nv) - 1

    def korand(self, D):
        """y mit y_u + y_w = D_l fuer alle Kanten, oder None."""
        y = 0
        for v in self.ordnung[1:]:
            p, l = self.eltern[v]
            if ((y >> p) & 1) ^ ((D >> l) & 1):
                y |= 1 << v
        for l, (a, b) in enumerate(self.links):
            if ((y >> a) & 1) ^ ((y >> b) & 1) != (D >> l) & 1:
                return None
        return y

    def klein(self, y):
        return y if popc(y) * 2 <= self.nv else y ^ self.alle


def gf2_loese(zeilen):
    """zeilen: (maske, rhs). Rueckgabe: spezielle Loesung (freie Variablen 0) oder None bei Widerspruch."""
    piv = {}
    for m, r in zeilen:
        while m:
            hb = m.bit_length() - 1
            if hb in piv:
                m ^= piv[hb][0]
                r ^= piv[hb][1]
            else:
                piv[hb] = (m, r)
                break
        if m == 0 and r:
            return None
    x = 0
    for hb in sorted(piv):
        m, r = piv[hb]
        val = r ^ (popc((m ^ (1 << hb)) & x) & 1)
        if val:
            x |= 1 << hb
    return x


def phase(k):
    k %= 4
    return {0: 1, 2: -1}.get(k, "i^%d" % k)


# ------------------------------------------------------------------ Netz und Drehmengen
class Modell:
    def __init__(self, art, n):
        t0 = time.time()
        self.art, self.n = art, n
        N = tp.Netz(art, n)
        self.N = N
        self.G = Graph(N)
        roh = N.schleifen()
        self.schl = []
        self.schl_id = {}
        for s in roh:
            kn = s["knoten"]
            k = len(kn)
            ls = [N.kante_id(kn[i], kn[(i + 1) % k]) for i in range(k)]
            X = 0
            for l in ls:
                X |= 1 << l
            seq = [N.idx[N.mod(v)] for v in kn]
            self.schl_id[frozenset(ls)] = len(self.schl)
            self.schl.append({"knoten": kn, "typ": s["typ"], "X": X, "links": ls, "seq": seq})
        self.hop_kurve = []
        for l, (ti, hi) in enumerate(N.links):
            u = N.sites[ti]
            w = [tp.add(u, b) for b in N.bonds(u) if N.idx[N.mod(tp.add(u, b))] == hi][0]
            self.hop_kurve.append([u, w])
        self.beine = [[] for _ in N.sites]       # Kanten je Knoten
        for l, (a, b) in enumerate(N.links):
            self.beine[a].append(l)
            self.beine[b].append(l)
        self.zeit_aufbau = round(time.time() - t0, 2)

    def drehmengen(self, M):
        """Lesart S (TWIST-PYRO-1 Hauptlesart): Huepfer rechts unten, Schleifen links oben."""
        N = self.N
        z = {"ent_schnitt": 0, "unklar": 0, "fern": 0, "nah": 0, "torus_zusammenfall": 0, "unklar_beispiele": []}
        TS = [tp.drehung(N, M, s["knoten"], True, tp.DELTA_P, z)[0] for s in self.schl]
        TH = [tp.drehung(N, M, self.hop_kurve[l], False, tp.DELTA_H, z)[0] for l in range(len(N.links))]
        z.pop("unklar_beispiele")
        z["ent_knoten"] = tp.knoten_entartung(N, M)
        return TH, TS, z

    # ---------------- Gruppenwirkung
    def wirkung(self, R, c):
        N = self.N
        km = []
        for s in N.sites:
            d = tp.sub3(s, c)
            km.append(N.idx[N.mod(tp.add(c, mv(R, d)))])
        lm = []
        for (a, b) in N.links:
            lm.append(N.lid[frozenset((km[a], km[b]))])
        sm, rich = [], []
        for s in self.schl:
            ls = frozenset(lm[l] for l in s["links"])
            j = self.schl_id.get(ls)
            sm.append(j)
            if j is None:
                rich.append(None)
                continue
            img = [km[v] for v in s["seq"]]
            k = len(img)
            ei = {(img[i], img[(i + 1) % k]) for i in range(k)}
            own = self.schl[j]["seq"]
            eo = {(own[i], own[(i + 1) % k]) for i in range(k)}
            rich.append(1 if ei == eo else (-1 if ei == {(b, a) for (a, b) in eo} else 0))
        return km, lm, sm, rich


def bild(menge, lm):
    out = 0
    l = 0
    while menge:
        if menge & 1:
            out |= 1 << lm[l]
        menge >>= 1
        l += 1
    return out


def kmatrix_paare(Mo, TH):
    """Alle Paare (l, m) an einem Knoten mit K_lm."""
    out = {}
    for v, ls in enumerate(Mo.beine):
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                l, m = ls[i], ls[j]
                out[(l, m)] = ((TH[l] >> m) & 1) ^ ((TH[m] >> l) & 1)
    return out


def anwenden(abb, P):
    """Clifford-Abbildung abb = (imgX, imgZ) auf Pauli P = i^k X^x Z^z."""
    imgX, imgZ = abb
    R = Pauli(P.k, 0, 0)
    x, l = P.x, 0
    while x:
        if x & 1:
            R = R * imgX[l]
        x >>= 1
        l += 1
    z, l = P.z, 0
    while z:
        if z & 1:
            R = R * imgZ[l]
        z >>= 1
        l += 1
    return R


def fermionfluss(Mo, TH, TS, minus=0):
    """Phi_p je Schleife: Huepferprodukt um p bei einem Fermion am Startknoten, Sektor B~ = +1, Partner fern.
    Alle Startknoten und beide Umlaufrichtungen muessen dasselbe Vorzeichen geben."""
    N = Mo.N
    H = [Pauli(2 * ((minus >> l) & 1), 1 << l, TH[l]) for l in range(len(N.links))]
    phi, info = [], {"inkonsistent": 0, "kein_korand": 0, "max_V": 0, "phase_nicht_reell": 0, "phase_minus": 0,
                     "start_in_V": 0, "E_T_ungerade": 0, "auswertungen": 0}
    for p, s in enumerate(Mo.schl):
        ls, seq = s["links"], s["seq"]
        if popc(s["X"] & TS[p]) % 2:
            info["E_T_ungerade"] += 1
        k = len(ls)
        werte = []
        Sz = None
        y = None
        for richtung in (1, -1):
            for st in range(k):
                if richtung == 1:
                    folge = [ls[(st + j) % k] for j in range(k)]
                else:
                    folge = [ls[(st - 1 - j) % k] for j in range(k)]
                O = H[folge[0]]
                for l in folge[1:]:
                    O = H[l] * O
                if Sz is None:
                    Sz = O.z
                    y = Mo.G.korand(O.z ^ TS[p])
                    if y is None:
                        info["kein_korand"] += 1
                        break
                    y = Mo.G.klein(y)
                    info["max_V"] = max(info["max_V"], popc(y))
                if O.x != s["X"] or O.z != Sz:
                    werte.append(None)
                    continue
                if O.k % 2:
                    info["phase_nicht_reell"] += 1
                    werte.append(None)
                    continue
                v = 1 if O.k % 4 == 0 else -1
                info["auswertungen"] += 1
                if v == -1:
                    info["phase_minus"] += 1
                if richtung == -1 and popc(s["X"] & TS[p]) % 2:
                    v = -v
                if (y >> seq[st]) & 1:
                    info["start_in_V"] += 1
                    v = -v
                werte.append(v)
            if y is None:
                break
        if y is None or None in werte or len(set(werte)) != 1:
            if y is not None:
                info["inkonsistent"] += 1
            phi.append(None)
        else:
            phi.append(werte[0])
    return phi, info


# ------------------------------------------------------------------ Kaefige (Frustrationsprobe)
def kaefige(Mo):
    """Geschlossene Flaechen aus kleinsten Schleifen um bekannte Zellzentren (Mindestbild-Abstand)."""
    N, art, per = Mo.N, Mo.art, Mo.N.per
    if art == "kubisch":
        skala, zentren, r2 = 2, [(2 * x + 1, 2 * y + 1, 2 * z + 1) for (x, y, z) in N.sites], 3
        listen = [(skala, zentren, r2)]
    elif art == "diamant":
        A = [s for s in N.sites if s[0] % 2 == 0]
        listen = [(1, [N.mod(tp.add(a, (2, 2, 2))) for a in A] + [N.mod(tp.add(a, (3, 3, 3))) for a in A], 4)]
    else:
        A = N.zentren_A
        tetra = A + [N.mod(tp.add(a, (2, 2, 2))) for a in A]
        leer = [N.mod(tp.add(a, (4, 4, 4))) for a in A] + [N.mod(tp.add(a, (6, 6, 6))) for a in A]
        listen = [(1, tetra, 3), (1, leer, 11)]
    out = []
    for skala, zentren, r2 in listen:
        P2 = per * skala
        for c in zentren:
            sel = []
            for p, s in enumerate(Mo.schl):
                ok = True
                for v in s["seq"]:
                    q = N.sites[v]
                    d2 = 0
                    for i in range(3):
                        d = (q[i] * skala - c[i]) % P2
                        if d > P2 // 2:
                            d -= P2
                        d2 += d * d
                    if d2 > r2 * 1:
                        ok = False
                        break
                if ok:
                    sel.append(p)
            out.append((c, sel))
    return out


def kaefig_vorzeichen(Mo, TS, sel):
    """Vorzeichen des orientierten Produkts der B~_p ueber eine geschlossene Flaeche, Ladung-0-Sektor."""
    N = Mo.N
    zaehl = {}
    for p in sel:
        for l in Mo.schl[p]["links"]:
            zaehl[l] = zaehl.get(l, 0) + 1
    if not sel or any(c != 2 for c in zaehl.values()):
        return "nicht_geschlossen"

    def lauf(p, l):
        s = Mo.schl[p]
        i = s["links"].index(l)
        k = len(s["seq"])
        a, b = s["seq"][i], s["seq"][(i + 1) % k]
        return 1 if N.links[l] == (a, b) else -1
    eps = {sel[0]: 1}
    q = [sel[0]]
    while q:
        p = q.pop()
        for l in Mo.schl[p]["links"]:
            for r in sel:
                if r != p and l in Mo.schl[r]["links"]:
                    soll = -eps[p] * lauf(p, l) * lauf(r, l)
                    if r not in eps:
                        eps[r] = soll
                        q.append(r)
                    elif eps[r] != soll:
                        return "nicht_orientierbar"
    if len(eps) != len(sel):
        return "nicht_zusammenhaengend"
    P = Pauli(0, 0, 0)
    for p in sel:
        P = P * Pauli(0, Mo.schl[p]["X"], TS[p])
    if P.x != 0:
        return "X_rest"
    y = Mo.G.korand(P.z)
    if y is None:
        return "Z_kein_korand"
    if P.k % 2:
        return "phase_nicht_reell"
    v = 1 if P.k % 4 == 0 else -1
    for p in sel:
        if eps[p] == -1 and popc(Mo.schl[p]["X"] & TS[p]) % 2:
            v = -v
    return v


# ------------------------------------------------------------------ Analyse je Gruppe
def analyse(Mo, TH, TS, gname, zentrum, fix, gedreht):
    N = Mo.N
    gen = GRUPPEN[gname]["gen"]
    elemente = gruppe_elemente(gen)
    nl = len(N.links)
    kp = kmatrix_paare(Mo, TH)
    phi, finfo = fermionfluss(Mo, TH, TS)
    res = {"gruppe": gname, "zentrum": list(zentrum), "elemente": {}, "fluss": finfo}
    werte = [v for v in phi if v is not None]
    res["fluss"]["plus"] = werte.count(1)
    res["fluss"]["minus"] = werte.count(-1)
    nach_typ = {}
    for p, s in enumerate(Mo.schl):
        key = "%s:%s" % (s["typ"], phi[p])
        nach_typ[key] = nach_typ.get(key, 0) + 1
    res["fluss"]["nach_typ"] = nach_typ
    # Gegenprobe der Vorzeichenbuchhaltung: Huepfer auf Kante 0 mit -1; genau die Schleifen mit Kante 0 muessen kippen
    phi_m, _ = fermionfluss(Mo, TH, TS, minus=1)
    mit0 = {p for p, s in enumerate(Mo.schl) if s["X"] & 1}
    gekippt = {p for p in range(len(phi)) if phi_m[p] != phi[p]}
    res["fluss"]["gegenprobe_kante0"] = {"schleifen_mit_kante0": len(mit0), "gekippt": len(gekippt),
                                         "genau_diese": gekippt == mit0}
    abb = {}
    karten = {}
    for R, name in sorted(elemente.items(), key=lambda t: (len(t[1]), t[1])):
        km, lm, sm, rich = Mo.wirkung(R, zentrum)
        karten[name] = (km, lm, sm, rich)
        e = {"art": art_von(R), "matrix": [list(r) for r in R], "schleife_fehlt": sm.count(None),
             "richtung_unklar": rich.count(0)}
        # Stufe W: Fehlmengen
        DH = [bild(TH[l], lm) ^ TH[lm[l]] for l in range(nl)]
        e["W_huepfer_D_nichtleer"] = sum(1 for d in DH if d)
        e["W_huepfer_kein_korand"] = sum(1 for d in DH if d and Mo.G.korand(d) is None)
        DS = []
        for p in range(len(Mo.schl)):
            DS.append(None if sm[p] is None else bild(TS[p], lm) ^ TS[sm[p]])
        e["W_schleife_D_nichtleer"] = sum(1 for d in DS if d)
        e["W_schleife_kein_korand"] = sum(1 for d in DS if d and Mo.G.korand(d) is None)
        e["stufe_W"] = (e["W_huepfer_kein_korand"] == 0 and e["W_schleife_kein_korand"] == 0
                        and e["schleife_fehlt"] == 0)
        # Stufe K: Vertauschungsgraph
        nk = 0
        for (l, m), v in kp.items():
            a, b = lm[l], lm[m]
            key = (a, b) if (a, b) in kp else (b, a)
            if kp.get(key) != v:
                nk += 1
        e["K_abweichungen"] = nk
        e["stufe_K_graph"] = nk == 0
        if nk == 0:
            imgX = [Pauli(0, 1 << lm[l], DH[l]) for l in range(nl)]
            imgZ = [Pauli(0, 0, 1 << lm[l]) for l in range(nl)]
            abb[name] = (imgX, imgZ)
            hok = 0
            for l in range(nl):
                Q = anwenden(abb[name], Pauli(0, 1 << l, TH[l]))
                if not (Q.x == 1 << lm[l] and Q.z == TH[lm[l]] and Q.k % 4 == 0):
                    hok += 1
            sig = {"plus": 0, "minus": 0, "falsch": 0}
            for p, s in enumerate(Mo.schl):
                if sm[p] is None or rich[p] == 0:
                    sig["falsch"] += 1
                    continue
                Q = anwenden(abb[name], Pauli(0, s["X"], TS[p]))
                j = sm[p]
                if Q.x != Mo.schl[j]["X"] or Q.z != TS[j] or Q.k % 2:
                    sig["falsch"] += 1
                    continue
                v = 1 if Q.k % 4 == 0 else -1
                if rich[p] == -1 and popc(Mo.schl[j]["X"] & TS[j]) % 2:
                    v = -v
                sig["plus" if v == 1 else "minus"] += 1
            e["K_huepfer_falsch"] = hok
            e["K_sigma"] = sig
            e["stufe_K"] = hok == 0 and sig["minus"] == 0 and sig["falsch"] == 0
        else:
            e["stufe_K"] = False
        # Stufe F: Fermionfluss
        nf = 0
        for p in range(len(Mo.schl)):
            if sm[p] is None or phi[p] is None or phi[sm[p]] is None or phi[sm[p]] != phi[p]:
                nf += 1
        e["F_abweichungen"] = nf
        e["stufe_F"] = nf == 0 and finfo["inkonsistent"] == 0 and finfo["kein_korand"] == 0
        # Gegenprobe: Fluss der Schleife 0 umgedreht
        phi2 = list(phi)
        if phi2 and phi2[0] is not None:
            phi2[0] = -phi2[0]
        e["F_gegenprobe_abweichungen"] = sum(1 for p in range(len(Mo.schl)) if sm[p] is not None
                                            and phi2[p] is not None and phi2[sm[p]] != phi2[p])
        res["elemente"][name] = e
    # ---------------- Relationen: Stufe K (Clifford, falls alle Buchstaben K-symmetrisch)
    fixidx = N.idx[N.mod(fix)] if fix is not None else N.idx[N.mod(BEZUG_PYRO)]
    l0 = Mo.beine[fixidx][0]
    a0, b0 = N.links[l0]
    nachbar = b0 if a0 == fixidx else a0
    rel = {}
    for rname, wort in GRUPPEN[gname]["rel"].items():
        r = {"wort": wort, "matrix_identitaet": wort_matrix(gen, wort) == EINS}
        if all(b in abb for b in wort):
            ident = True
            for l in range(nl):
                for P in (Pauli(0, 1 << l, 0), Pauli(0, 0, 1 << l)):
                    Q = P
                    for b in wort:
                        Q = anwenden(abb[b], Q)
                    if not (Q.x == P.x and Q.z == P.z and Q.k % 4 == 0):
                        ident = False
            Q = Pauli(0, 1 << l0, TH[l0])
            for b in wort:
                Q = anwenden(abb[b], Q)
            r["K_identitaet"] = ident
            r["K_paarerzeuger"] = phase(Q.k) if (Q.x == 1 << l0 and Q.z == TH[l0]) else "falsch"
        else:
            r["K_identitaet"] = None
            r["K_paarerzeuger"] = None
        rel[rname] = r
    res["relationen"] = rel
    # ---------------- PSG (Stufe F fuer die ganze Gruppe)
    alle_F = all(e["stufe_F"] for e in res["elemente"].values())
    psg = {"versucht": alle_F}
    if alle_F:
        x = gf2_loese([(s["X"], 1 if phi[p] == -1 else 0) for p, s in enumerate(Mo.schl)])
        psg["fluss_loesbar"] = x is not None
        if x is not None:
            schnitte = [0, 0, 0]
            for l, (u, w) in enumerate(Mo.hop_kurve):
                for i in range(3):
                    if not 0 <= w[i] < N.per:
                        schnitte[i] |= 1 << l
            gefunden = None
            for maske in range(8):
                xs = x
                for i in range(3):
                    if maske >> i & 1:
                        xs ^= schnitte[i]
                ys = {}
                for b, Rb in gen.items():
                    km, lm, sm, rich = Mo.wirkung(Rb, zentrum)
                    xg = 0
                    for l in range(nl):
                        if (xs >> l) & 1:
                            xg |= 1 << lm[l]
                    y = Mo.G.korand(xs ^ xg)
                    if y is None:
                        break
                    if (y >> fixidx) & 1:
                        y ^= Mo.G.alle
                    ys[b] = (y, km)
                if len(ys) == len(gen):
                    gefunden = (maske, ys)
                    break
            psg["holonomie_maske"] = None if gefunden is None else gefunden[0]
            if gefunden is not None:
                ys = gefunden[1]
                rw = {}
                for rname, wort in GRUPPEN[gname]["rel"].items():
                    vals = set()
                    lam = {}
                    for I in range(len(N.sites)):
                        pos, val = I, 0
                        for b in wort:
                            y, km = ys[b]
                            pos = km[pos]
                            val ^= (y >> pos) & 1
                        if pos != I:
                            vals.add("bahn_offen")
                        lam[I] = -1 if val else 1
                        vals.add(lam[I])
                    rw[rname] = {"werte": sorted(str(v) for v in vals), "am_bezugsknoten": lam[fixidx],
                                 "paarerzeuger": lam[fixidx] * lam[nachbar]}
                psg["relationen"] = rw
                inv = {"T": "C2^2", "O": "C4^4"}.get(gname)
                psg["invariante_name"] = inv
                if inv is not None and len(rw[inv]["werte"]) == 1:
                    psg["invariante"] = int(rw[inv]["werte"][0])
                else:
                    psg["invariante"] = None
    res["psg"] = psg
    res["gedreht"] = gedreht
    return res


def fig5_probe(Mo, TH, TS):
    """Handrechnung PLAN.md 1.7: xz-Plakette am Ursprung, kubisch L=4, P1: Phi = +1, V' = {(1,0,0), (0,0,1)}."""
    N = Mo.N
    kn = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)]
    ls = frozenset(N.kante_id(kn[i], kn[(i + 1) % 4]) for i in range(4))
    p = Mo.schl_id[ls]
    phi, info = fermionfluss(Mo, TH, TS)
    H = [Pauli(0, 1 << l, TH[l]) for l in range(len(N.links))]
    s = Mo.schl[p]
    O = H[s["links"][0]]
    for l in s["links"][1:]:
        O = H[l] * O
    y = Mo.G.klein(Mo.G.korand(O.z ^ TS[p]))
    V = sorted(list(N.sites[v]) for v in range(len(N.sites)) if (y >> v) & 1)
    return {"phi": phi[p], "V_strich": V, "start": list(N.sites[s["seq"][0]]), "erwartet_phi": 1,
            "erwartet_V": [[0, 0, 1], [1, 0, 0]], "gleich": phi[p] == 1 and V == [[0, 0, 1], [1, 0, 0]]}


def main():
    modus, aus = sys.argv[1], sys.argv[2]
    t0 = time.time()
    erg = {"meta": {"modus": modus, "python": platform.python_version(), "PROJ": {k: [list(r) for r in v]
                                                                                for k, v in tp.PROJ.items()},
                    "DELTA_P": list(tp.DELTA_P), "DELTA_H": list(tp.DELTA_H), "lesart": "S"},
           "faelle": {}}
    modelle = {}
    for netz, gh, gr, gname, zentrum, fix in FAELLE:
        for n in (gr if modus == "rauch" else gh):
            key = (netz, n)
            if key not in modelle:
                Mo = Modell(netz, n)
                dm = {}
                for P in PS:
                    TH, TS, z = Mo.drehmengen(tp.PROJ[P])
                    dm[P] = (TH, TS, z)
                modelle[key] = (Mo, dm)
            Mo, dm = modelle[key]
            fall = "%s-%d-%s" % (netz, n, gname)
            out = {"knoten": len(Mo.N.sites), "kanten": len(Mo.N.links), "schleifen": len(Mo.schl),
                   "zusammenhaengend": Mo.G.zusammenhaengend, "proj": {}}
            nl = len(Mo.N.links)
            out["ungedreht"] = analyse(Mo, [0] * nl, [0] * len(Mo.schl), gname, zentrum, fix, False)
            for P in PS:
                TH, TS, z = dm[P]
                r = analyse(Mo, TH, TS, gname, zentrum, fix, True)
                r["generik"] = z
                kf = {"plus": 0, "minus": 0, "anders": {}}
                for c, sel in kaefige(Mo):
                    v = kaefig_vorzeichen(Mo, TS, sel)
                    if v == 1:
                        kf["plus"] += 1
                    elif v == -1:
                        kf["minus"] += 1
                    else:
                        kf["anders"][v] = kf["anders"].get(v, 0) + 1
                r["kaefige"] = kf
                if netz == "kubisch" and P == "P1":
                    r["fig5_probe"] = fig5_probe(Mo, TH, TS)
                out["proj"][P] = r
            kfu = {"plus": 0, "minus": 0, "anders": {}}
            for c, sel in kaefige(Mo):
                v = kaefig_vorzeichen(Mo, [0] * len(Mo.schl), sel)
                if v in (1, -1):
                    kfu["plus" if v == 1 else "minus"] += 1
                else:
                    kfu["anders"][v] = kfu["anders"].get(v, 0) + 1
            out["ungedreht"]["kaefige"] = kfu
            out["zeit_s"] = round(time.time() - t0, 2)
            erg["faelle"][fall] = out
            print(fall, out["zeit_s"], "s", flush=True)
    erg["laufzeit_s"] = round(time.time() - t0, 2)
    with open(aus + ".tmp", "w") as fh:
        json.dump(erg, fh, indent=1, sort_keys=True)
    os.replace(aus + ".tmp", aus)
    print("fertig", modus, erg["laufzeit_s"], "s")


if __name__ == "__main__":
    main()
