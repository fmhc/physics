"""WOLFRAM-RUHE-1 (Runde 42, Code-Agent fuer Leitung claude-primary): Kernfunktionen.

Regel R2 der Technical Introduction (Wolfram 2020, Abschnitt 6.8, Druckseite 283-284):
    {{x,y,y},{x,z,u}} -> {{u,v,v},{v,z,y},{x,y,v}}
Standard-Aktualisierung nach TI Druckseite 243, Kausalgraph nach TI Druckseite 361 (Kante A -> B, wenn B eine von A
erzeugte Relation verbraucht), Kegel, Intervalle (N, laengste Kette L), Kontrollen Poisson 1+1 und Nullgitter.
Nur ueber kleintest.sh auf der .69 starten (kein lokaler Start).
"""
import bisect
import hashlib
import math
import random

import numpy as np

ANFANG_STANDARD = ((0, 0, 0), (0, 0, 0))   # TI Z. 1025-1026: Selbstschleifen Table[0, n, k]
ANFANG_LHS = ((1, 2, 2), (1, 3, 4))        # Diagnose: Kopie der linken Seite (TI Z. 1022-1023)


def datei_sha(pfad):
    with open(pfad, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


class R2:
    """Zustand eines R2-Laufs mit Ereignisprotokoll (Erzeugungsnummern der Relationen steigen monoton)."""

    def __init__(self, anfang):
        self.rel = {}
        self.erzeuger = {}
        self.rel_gen = {}
        self.by_first = {}
        self.marken = set()
        self.next_rel = 0
        self.next_node = 1 + max(max(t) for t in anfang)
        self.ev_T = []
        self.ev_parents = []
        self.ev_depth = []
        self.ev_marken_nachher = []
        for trip in anfang:
            self._hinzu(tuple(trip), -1, 0)

    def _hinzu(self, trip, ereignis, gen):
        rid = self.next_rel
        self.next_rel += 1
        self.rel[rid] = trip
        self.erzeuger[rid] = ereignis
        self.rel_gen[rid] = gen
        self.by_first.setdefault(trip[0], set()).add(rid)
        if trip[1] == trip[2]:
            self.marken.add(rid)

    def _weg(self, rid):
        trip = self.rel.pop(rid)
        s = self.by_first[trip[0]]
        s.discard(rid)
        if not s:
            del self.by_first[trip[0]]
        self.marken.discard(rid)
        del self.erzeuger[rid]
        del self.rel_gen[rid]

    def treffer_tiefe(self, t, p):
        d = 0
        for rid in (t, p):
            e = self.erzeuger[rid]
            if e >= 0:
                d = max(d, self.ev_depth[e])
        return d + 1

    def anwenden(self, t, p, T=None):
        """Ereignis mit Marke t (Relation 1) und Partner p (Relation 2)."""
        x, y, y2 = self.rel[t]
        x2, z, u = self.rel[p]
        assert y == y2 and x2 == x and t != p
        v = self.next_node
        self.next_node += 1
        eltern = set()
        gen_ein = 0
        for rid in (t, p):
            e = self.erzeuger[rid]
            if e >= 0:
                eltern.add(e)
            gen_ein = max(gen_ein, self.rel_gen[rid])
        for rid in (t, p):
            self._weg(rid)
        eid = len(self.ev_T)
        if T is None:
            T = gen_ein + 1
        self.ev_T.append(T)
        self.ev_parents.append(tuple(sorted(eltern)))
        self.ev_depth.append(1 + max((self.ev_depth[q] for q in eltern), default=0))
        for trip in ((u, v, v), (v, z, y), (x, y, v)):
            self._hinzu(trip, eid, T)
        self.ev_marken_nachher.append(len(self.marken))
        return eid

    def alle_treffer(self):
        out = []
        for t in self.marken:
            a = self.rel[t][0]
            for p in self.by_first.get(a, ()):
                if p != t:
                    out.append((t, p))
        out.sort()
        return out

    def standard_generation(self, g):
        """Ein Gesamtschritt der Standard-Aktualisierung (TI S. 243): Relationen vom aeltesten zum neuesten,
        jede wird benutzt, wenn ein Ereignis ohne schon benutzte Relation moeglich ist; nur Relationen vom
        Schrittbeginn. Partnerwahl (Plan): aeltester Partner, bei Gleichstand Rolle Marke zuerst."""
        grenze = self.next_rel
        kand = set()
        for t in list(self.marken):
            a = self.rel[t][0]
            ps = [p for p in self.by_first.get(a, ()) if p != t]
            if ps:
                kand.add(t)
                kand.update(ps)
        n = 0
        for r in sorted(kand):
            if r not in self.rel or r >= grenze:
                continue
            best = None
            a = self.rel[r][0]
            r_marke = r in self.marken
            for q in self.by_first.get(a, ()):
                if q == r or q >= grenze:
                    continue
                if r_marke:
                    key = (q, 0)
                    if best is None or key < best[0]:
                        best = (key, r, q)
                if q in self.marken:
                    key = (q, 1)
                    if best is None or key < best[0]:
                        best = (key, q, r)
            if best is not None:
                self.anwenden(best[1], best[2], T=g)
                n += 1
        return n


def standard_lauf(anfang, E_max):
    s = R2(anfang)
    proto = []
    g = 0
    while len(s.ev_T) < E_max:
        g += 1
        n = s.standard_generation(g)
        proto.append((g, n, len(s.rel), len(s.marken)))
        if n == 0:
            break
    return s, proto


def standard_bis_tiefe(anfang, D, E_cap=200000):
    s = R2(anfang)
    g = 0
    while len(s.ev_T) < E_cap:
        tr = s.alle_treffer()
        if not tr or min(s.treffer_tiefe(t, p) for t, p in tr) > D:
            break
        g += 1
        if s.standard_generation(g) == 0:
            break
    return s


def zufall_lauf(anfang, saat, E_max=None, D_stop=None, E_cap=200000):
    rng = random.Random(saat)
    s = R2(anfang)
    while len(s.ev_T) < E_cap:
        tr = s.alle_treffer()
        if not tr:
            break
        if D_stop is not None and min(s.treffer_tiefe(t, p) for t, p in tr) > D_stop:
            break
        if E_max is not None and len(s.ev_T) >= E_max:
            break
        t, p = tr[rng.randrange(len(tr))]
        s.anwenden(t, p)
    return s


def kinder_liste(parents):
    ch = [[] for _ in parents]
    for e, ps in enumerate(parents):
        for q in ps:
            ch[q].append(e)
    return ch


def teilgraph_tiefe(s, D):
    import networkx as nx
    G = nx.DiGraph()
    for e, d in enumerate(s.ev_depth):
        if d <= D:
            G.add_node(e, d=d)
    for e in list(G.nodes):
        for q in s.ev_parents[e]:
            G.add_edge(q, e)
    return G


def isomorph(G1, G2):
    import networkx as nx
    if G1.number_of_nodes() != G2.number_of_nodes() or G1.number_of_edges() != G2.number_of_edges():
        return False
    if sorted(d for _, d in G1.in_degree()) != sorted(d for _, d in G2.in_degree()):
        return False
    if sorted(d for _, d in G1.out_degree()) != sorted(d for _, d in G2.out_degree()):
        return False
    return nx.is_isomorphic(G1, G2, node_match=lambda a, b: a["d"] == b["d"])


def geo_kegel(children, T, start, tmax):
    """Geodaetischer Kegel (TI S. 366-367): Zahl der ueber <= t gerichtete Kanten erreichbaren Ereignisse."""
    gesehen = {start}
    front = [start]
    C = [1]
    Tmax = [T[start]]
    for _ in range(tmax):
        neu = []
        for e in front:
            for f in children[e]:
                if f not in gesehen:
                    gesehen.add(f)
                    neu.append(f)
        front = neu
        C.append(len(gesehen))
        Tmax.append(max([Tmax[-1]] + [T[f] for f in neu]))
    return C, Tmax


def gen_kegel(children, T, start, Tmax):
    """Generationskegel: Zahl der f mit start <= f (Ordnung) und T(f) - T(start) <= Tm, Tm = 0..Tmax (T ganzzahlig)."""
    T0 = T[start]
    gesehen = {start}
    stapel = [start]
    while stapel:
        e = stapel.pop()
        for f in children[e]:
            if f not in gesehen and T[f] - T0 <= Tmax:
                gesehen.add(f)
                stapel.append(f)
    hist = np.zeros(Tmax + 1, dtype=np.int64)
    for f in gesehen:
        hist[T[f] - T0] += 1
    return np.cumsum(hist)


def eichung_c(Ts, C):
    """Quadratische Anpassung C = A + B T + (c^2/2) T^2; gibt (c, Koeffizienten) zurueck, c = nan bei c^2 <= 0."""
    k = np.polyfit(np.asarray(Ts, float), np.asarray(C, float), 2)
    q = k[0]
    c = math.sqrt(2.0 * q) if q > 0 else float("nan")
    return c, [float(z) for z in k]


def exponent(ts, C):
    return float(np.polyfit(np.log(np.asarray(ts, float)), np.log(np.asarray(C, float)), 1)[0])


def intervall(T, parents, children, p, q):
    """Allgemeine Intervall-Routine: [p, q] = Zukunft(p) geschnitten Vergangenheit(q); N mit Endpunkten, L = Zahl der
    Elemente der laengsten Kette von p nach q. T muss entlang jeder Kante streng steigen. None, wenn q nicht nach p."""
    Tq = T[q]
    Tp = T[p]
    fw = {p}
    stapel = [p]
    while stapel:
        e = stapel.pop()
        for f in children[e]:
            if f not in fw and T[f] <= Tq:
                fw.add(f)
                stapel.append(f)
    if q not in fw:
        return None
    iv = {q}
    stapel = [q]
    while stapel:
        e = stapel.pop()
        for f in parents[e]:
            if f in fw and f not in iv and T[f] >= Tp:
                iv.add(f)
                stapel.append(f)
    ordnung = sorted(iv, key=lambda e: (T[e], e))
    L = {}
    for e in ordnung:
        best = 0
        for f in parents[e]:
            if f in L and L[f] > best:
                best = L[f]
        L[e] = best + 1
    return len(iv), L[q]


def lis_laenge(folge):
    tails = []
    for w in folge:
        k = bisect.bisect_left(tails, w)
        if k == len(tails):
            tails.append(w)
        else:
            tails[k] = w
    return len(tails)


def poisson_intervall(rng, U, V):
    """Poisson-Intervall in 1+1 (Dichte 1 je du dv), p = (0,0), q = (U,V); N mit Endpunkten, L = 2 + LIS."""
    n = int(rng.poisson(U * V))
    u = rng.random(n) * U
    v = rng.random(n) * V
    o = np.argsort(u)
    L = 2 + lis_laenge(v[o].tolist())
    return n + 2, L, U + V, u, v


def poisson_als_graph(u, v, U, V):
    """Dieselbe Poisson-Menge als allgemeiner Graph (Eltern = alle Vorgaenger), fuer die Programmprobe."""
    pu = np.concatenate([[0.0], u, [U]])
    pv = np.concatenate([[0.0], v, [V]])
    n = len(pu)
    T = (pu + pv).tolist()
    parents = []
    for j in range(n):
        m = (pu < pu[j]) & (pv < pv[j])
        parents.append(tuple(int(i) for i in np.nonzero(m)[0]))
    children = kinder_liste(parents)
    return T, parents, children, 0, n - 1


def gitter_graph(M):
    T = [0] * (M * M)
    parents = [()] * (M * M)
    for i in range(M):
        for j in range(M):
            k = i * M + j
            T[k] = i + j
            ps = []
            if i > 0:
                ps.append((i - 1) * M + j)
            if j > 0:
                ps.append(i * M + j - 1)
            parents[k] = tuple(ps)
    return T, parents, kinder_liste(parents)


def poisson_kegel_eichung(rng, Tmax=100, wdh=20):
    """Generationskegel einer Poisson-Streuung: Punkte im Dreieck u, v >= 0, u + v <= Tmax, Start im Ursprung."""
    Ts = np.arange(10, Tmax + 1)
    summe = np.zeros(len(Ts))
    for _ in range(wdh):
        n = int(rng.poisson(Tmax * Tmax / 2.0))
        # gleichverteilt im Dreieck
        a = rng.random(n)
        b = rng.random(n)
        spiegel = a + b > 1.0
        a[spiegel] = 1.0 - a[spiegel]
        b[spiegel] = 1.0 - b[spiegel]
        tt = (a + b) * Tmax
        tt.sort()
        summe += 1.0 + np.searchsorted(tt, Ts, side="right")
    C = summe / wdh
    return eichung_c(Ts, C) + (C.tolist(),)


def x_wert(c, dT, N):
    return c * (dT + 1.0) / (2.0 * math.sqrt(N))


def kontrollen(rng, n_int, M_gitter=420, Tmax=100):
    """WR0-Daten: Gitter ueber die allgemeine Graph-Routine, Poisson ueber Koordinaten (LIS)."""
    T, parents, children = gitter_graph(M_gitter)
    start = 10 * M_gitter + 10
    Cg = gen_kegel(children, T, start, Tmax)
    Ts = np.arange(10, Tmax + 1)
    c_G, k_G = eichung_c(Ts, Cg[10:Tmax + 1])
    c_P, k_P, C_P = poisson_kegel_eichung(rng, Tmax)
    G = {"N": [], "L": [], "dT": [], "x": [], "eta_wahr": [], "cosh_wahr": [], "a": [], "b": []}
    while len(G["N"]) < n_int:
        eta = rng.random() * 2.0
        Nz = math.exp(math.log(50) + rng.random() * (math.log(2000) - math.log(50)))
        a = int(round(math.sqrt(Nz) * math.exp(eta))) - 1
        b = int(round(math.sqrt(Nz) * math.exp(-eta))) - 1
        if b < 1 or a < 1 or a > M_gitter - 2 or not (50 <= (a + 1) * (b + 1) <= 2000):
            continue
        i0 = int(rng.integers(0, M_gitter - a))
        j0 = int(rng.integers(0, M_gitter - b))
        p = i0 * M_gitter + j0
        q = (i0 + a) * M_gitter + (j0 + b)
        N, L = intervall(T, parents, children, p, q)
        dT = T[q] - T[p]
        G["N"].append(N)
        G["L"].append(L)
        G["dT"].append(dT)
        G["x"].append(x_wert(c_G, dT, N))
        G["eta_wahr"].append(0.5 * math.log(a / b))
        G["cosh_wahr"].append((a + b) / (2.0 * math.sqrt(a * b)))
        G["a"].append(a)
        G["b"].append(b)
    P = {"N": [], "L": [], "dT": [], "x": [], "eta_wahr": [], "cosh_wahr": []}
    while len(P["N"]) < n_int:
        eta = rng.random() * 2.0
        Nz = math.exp(math.log(50) + rng.random() * (math.log(2000) - math.log(50)))
        U = math.sqrt(Nz) * math.exp(eta)
        V = math.sqrt(Nz) * math.exp(-eta)
        N, L, dT, _, _ = poisson_intervall(rng, U, V)
        if not (50 <= N <= 2000):
            continue
        P["N"].append(N)
        P["L"].append(L)
        P["dT"].append(dT)
        P["x"].append(x_wert(c_P, dT, N))
        P["eta_wahr"].append(eta)
        P["cosh_wahr"].append(math.cosh(eta))
    return {"gitter": G, "poisson": P, "c_gitter": c_G, "c_gitter_koeff": k_G, "c_poisson": c_P,
            "c_poisson_koeff": k_P, "M_gitter": M_gitter}


def programmprobe(rng, anzahl=40):
    """LIS (Koordinaten) gegen allgemeine Graph-Routine an kleinen Poisson-Intervallen."""
    abw = 0
    faelle = []
    for _ in range(anzahl):
        eta = rng.random() * 2.0
        Nz = 30 + rng.random() * 170
        U = math.sqrt(Nz) * math.exp(eta)
        V = math.sqrt(Nz) * math.exp(-eta)
        N, L, dT, u, v = poisson_intervall(rng, U, V)
        T, parents, children, p, q = poisson_als_graph(u, v, U, V)
        N2, L2 = intervall(T, parents, children, p, q)
        if (N, L) != (N2, L2):
            abw += 1
        faelle.append([N, L, N2, L2])
    return {"anzahl": anzahl, "abweichungen": abw, "faelle": faelle}


def r2_wr1(anfang, E, n_start=40, tmax=100, Tmax=100, saat=42):
    """WR1-Groessen fuer einen Standardlauf."""
    s, proto = standard_lauf(anfang, E)
    T = s.ev_T
    parents = s.ev_parents
    children = kinder_liste(parents)
    G_letzt = proto[-1][0] if proto else 0
    rng = random.Random(saat)
    lo, hi = int(0.1 * G_letzt), int(0.3 * G_letzt)
    kandid = [e for e in range(len(T)) if lo <= T[e] <= hi]
    starts = sorted(rng.sample(kandid, min(n_start, len(kandid)))) if kandid else []
    grenze_T = G_letzt - 0.02 * G_letzt
    Cgeo = np.zeros(tmax + 1)
    t_g = tmax
    Cgen = np.zeros(Tmax + 1)
    for e in starts:
        C, Tm = geo_kegel(children, T, e, tmax)
        Cgeo += np.asarray(C, float)
        for t in range(tmax + 1):
            if Tm[t] >= grenze_T:
                t_g = min(t_g, t - 1)
                break
        Cgen += gen_kegel(children, T, e, Tmax)
    if starts:
        Cgeo /= len(starts)
        Cgen /= len(starts)
    erg = {"E": len(T), "G": G_letzt, "anzahl_starts": len(starts), "t_g": int(t_g),
           "C_geo": Cgeo.tolist(), "C_gen": Cgen.tolist()}
    # (a)
    if t_g >= 40:
        ts = np.arange(max(1, t_g // 4), t_g + 1)
        erg["D_geo"] = exponent(ts, Cgeo[ts])
        erg["D_geo_fenster"] = [int(ts[0]), int(ts[-1])]
    else:
        erg["D_geo"] = None
    # lokale Steigungen geodaetisch (Diagnose)
    erg["D_geo_lokal"] = [float(math.log(Cgeo[t + 5] / Cgeo[t]) / math.log((t + 5) / t)) for t in range(5, tmax - 4, 5)]
    # (c)
    Ts = np.arange(25, Tmax + 1)
    erg["D_gen"] = exponent(Ts, Cgen[Ts])
    c_R2, k_R2 = eichung_c(np.arange(10, Tmax + 1), Cgen[10:Tmax + 1])
    erg["c_R2"] = c_R2
    erg["c_R2_koeff"] = k_R2
    # (b)
    gens = np.array([z[0] for z in proto])
    nev = np.array([z[1] for z in proto], float)
    nrel = np.array([z[2] for z in proto], float)
    nmark = np.array([z[3] for z in proto])
    fenster = np.array_split(np.arange(len(gens)), 20)
    f_ev = [float(nev[f].mean()) for f in fenster if len(f)]
    f_rel = [float(nrel[f[-1]]) for f in fenster if len(f)]
    zweite = slice(len(f_ev) // 2, len(f_ev))
    if len(f_ev) >= 4 and min(f_ev[zweite]) > 0:
        erg["s_b"] = float(np.polyfit(np.log(f_rel[zweite]), np.log(f_ev[zweite]), 1)[0])
    else:
        erg["s_b"] = None
    letzt = max(1, len(gens) // 10)
    erg["ereignisse_je_gen_letztes_zehntel"] = float(nev[-letzt:].mean())
    erg["fenster_ereignisse_je_gen"] = f_ev
    erg["fenster_relationen"] = f_rel
    erg["ereignisse_je_gen_max"] = int(nev.max()) if len(nev) else 0
    erg["ereignisse_je_gen_hist"] = {str(int(k)): int((nev == k).sum()) for k in np.unique(nev)}
    erg["marken_hist"] = {str(int(k)): int((nmark == k).sum()) for k in np.unique(nmark)}
    erg["marken_letzt"] = int(nmark[-1]) if len(nmark) else 0
    erg["halt"] = bool(len(proto) and proto[-1][1] == 0)
    # Kettenprobe
    ok = sum(1 for k in range(10, len(T)) if (k - 1) in parents[k])
    erg["kettenprobe_anteil"] = ok / max(1, len(T) - 10)
    erg["ausgrad_max"] = max((len(c) for c in children), default=0)
    erg["eingrad_max"] = max((len(p) for p in parents), default=0)
    return erg, s, children


def r2_intervalle(s, children, anzahl, saat=7, versuche_max=60000):
    """R2-Intervalle (nur Daten fuer WR2): p aus Generationen [0,1 G; 0,6 G], Ziel-Delta T log-gleichverteilt [5, 3000]."""
    T = s.ev_T
    parents = s.ev_parents
    rng = random.Random(saat)
    G = max(T)
    nach_gen = {}
    for e, t in enumerate(T):
        nach_gen.setdefault(t, []).append(e)
    pool = [e for e in range(len(T)) if 0.1 * G <= T[e] <= 0.6 * G]
    out = {"N": [], "L": [], "dT": []}
    versuche = 0
    abgewiesen_nicht_kausal = 0
    while len(out["N"]) < anzahl and versuche < versuche_max and pool:
        versuche += 1
        p = rng.choice(pool)
        dTz = int(round(math.exp(math.log(5) + rng.random() * (math.log(3000) - math.log(5)))))
        tz = T[p] + dTz
        if tz not in nach_gen:
            continue
        q = rng.choice(nach_gen[tz])
        res = intervall(T, parents, children, p, q)
        if res is None:
            abgewiesen_nicht_kausal += 1
            continue
        N, L = res
        if not (50 <= N <= 2000):
            continue
        out["N"].append(N)
        out["L"].append(L)
        out["dT"].append(T[q] - T[p])
    out["versuche"] = versuche
    out["abgewiesen_nicht_kausal"] = abgewiesen_nicht_kausal
    return out


def ki_probe(Ds, saaten):
    """Kausalinvarianz-Probe: Teilgraph 'Tiefe <= D' fuer Standard und Zufallsreihenfolgen, Isomorphie."""
    erg = {}
    for D in Ds:
        ref = teilgraph_tiefe(standard_bis_tiefe(ANFANG_STANDARD, D), D)
        zeilen = []
        for saat in saaten:
            g = teilgraph_tiefe(zufall_lauf(ANFANG_STANDARD, saat, D_stop=D), D)
            zeilen.append({"saat": saat, "knoten": g.number_of_nodes(), "kanten": g.number_of_edges(),
                           "isomorph_zu_standard": bool(isomorph(ref, g))})
        erg[str(D)] = {"standard_knoten": ref.number_of_nodes(), "standard_kanten": ref.number_of_edges(),
                       "zufall": zeilen,
                       "alle_isomorph": all(z["isomorph_zu_standard"] for z in zeilen)}
    erg["urteil"] = "KI ohne Gegenbeispiel" if all(erg[str(D)]["alle_isomorph"] for D in Ds) else "KI verletzt"
    return erg


def r2_diagnose(anfang, E, zufall_saat=None):
    """Diagnose ohne Urteil: Ereignisse je Generation, Marken, Kettenprobe fuer anderen Anfang bzw. Zufallsreihenfolge."""
    if zufall_saat is None:
        s, proto = standard_lauf(anfang, E)
        nev = [z[1] for z in proto]
    else:
        s = zufall_lauf(anfang, zufall_saat, E_max=E)
        zaehl = {}
        for t in s.ev_T:
            zaehl[t] = zaehl.get(t, 0) + 1
        nev = [zaehl[t] for t in sorted(zaehl)]
    T = s.ev_T
    parents = s.ev_parents
    ok = sum(1 for k in range(10, len(T)) if (k - 1) in parents[k])
    mk = s.ev_marken_nachher
    return {"E": len(T), "G": max(T) if T else 0, "ereignisse_je_gen_max": max(nev) if nev else 0,
            "ereignisse_je_gen_mittel": float(np.mean(nev)) if nev else 0.0,
            "marken_max": max(mk) if mk else 0, "marken_letzt": mk[-1] if mk else 0,
            "kettenprobe_anteil": ok / max(1, len(T) - 10),
            "tiefe_max": max(s.ev_depth) if s.ev_depth else 0}
