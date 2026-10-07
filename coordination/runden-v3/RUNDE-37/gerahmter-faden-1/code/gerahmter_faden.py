#!/usr/bin/env python3
"""GERAHMTER-FADEN-1 (Runde 50, fmhc-physics, RUNDE-37/gerahmter-faden-1): gerahmte Levin/Wen-Faeden auf Finns
Diamantnetz. Karte: KARTE.md (Varianten A, B, C; Rahmenklassen R0, R1, R2; Messgroessen M1 bis M4).

Importiert unveraendert: twist_pyro.py (TWIST-PYRO-1, sha256 17875033...) und twist_spin.py (TWIST-SPIN-1, 3136d4e9...).
Lesart S lokal formuliert: Ein Bein m am Kurvenknoten v kreuzt die Rahmung nahe v genau dann, wenn der Push-off delta
im offenen Kegel {alpha P d_m - beta P d_e; alpha, beta > 0} liegt (e = anliegende Kurvenkante, P = Projektion an v).
Damit haengt alles nur an knotenweisen Konventionen (Projektion P_v, Push-off delta_v):
  A: P_v = feste Projektion (P1, P2, P3 aus TWIST-PYRO-1), ganzzahlig exakt; muss tp.drehung bitgleich treffen.
  B: P_v = Projektion laengs n_v = q_v z q_v^-1, Push-off w (fester Laborvektor), Gleitkomma mit Randabstandspruefung;
     bei R0 (n = z) ganzzahlig exakt.
  C: wie A; Huepfer mit c-Zahl s_l = sign(q_u . q_w) (kurzer Lift), Schleifen mit w2(p) = prod s (Kopplungsgesetz).
Aufruf (nur ueber kleintest.sh auf der .69): python gerahmter_faden.py <rauch|basis|m3> <ausgabe.json> [n ...]
"""
import sys
import json
import time
import math
import os
import random
import platform
import hashlib
from types import SimpleNamespace

import twist_pyro as tp
import twist_spin as ts

Pauli = tp.Pauli
W_HAUPT = (-5, 4, 0)    # Push-off der Schleifen in B: TWIST-PYRO-1 DELTA_P ("links oben") in xy-Koordinaten
W_ALT = (-1, 0, 0)      # Kontrast: groesster Winkelabstand zu den projizierten Diamantbeinen bei n = z
RAND_MIN = 1e-9
THETAS = (15, 30, 45, 60)
MODEN = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1),
         (1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))
EZ = (0.0, 0.0, 1.0)
T0 = time.time()


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# ------------------------------------------------------------------ Quaternionen (w, x, y, z)
def qmul(a, b):
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return (w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2, w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2, w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2)


def qkonj(a):
    return (a[0], -a[1], -a[2], -a[3])


def qachse(n, alpha):
    c, s = math.cos(alpha / 2.0), math.sin(alpha / 2.0)
    return (c, n[0] * s, n[1] * s, n[2] * s)


def qexp(eta):
    a = math.sqrt(eta[0] ** 2 + eta[1] ** 2 + eta[2] ** 2)
    if a < 1e-300:
        return (1.0, 0.0, 0.0, 0.0)
    return qachse((eta[0] / a, eta[1] / a, eta[2] / a), a)


def qdreh(q, v):
    p = qmul(qmul(q, (0.0, v[0], v[1], v[2])), qkonj(q))
    return (p[1], p[2], p[3])


def qdot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]


def bwinkel(a, b):
    return 2.0 * math.acos(min(1.0, abs(qdot(a, b))))


def norm3(v):
    l = math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
    return (v[0] / l, v[1] / l, v[2] / l)


def dot3(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


# ------------------------------------------------------------------ knotenweise Konventionen
class Konv:
    """Projektion M_v (2x3), Push-off dp_v (Schleifen) und dh_v (Huepfer), Flag ganzzahlig-exakt."""

    def __init__(self, nv):
        self.M = [None] * nv
        self.dp = [None] * nv
        self.dh = [None] * nv
        self.ex = [True] * nv

    def kopie(self):
        k = Konv(0)
        k.M, k.dp, k.dh, k.ex = list(self.M), list(self.dp), list(self.dh), list(self.ex)
        return k


def konv_global(nv, M, dp, dh):
    k = Konv(nv)
    for i in range(nv):
        k.M[i], k.dp[i], k.dh[i], k.ex[i] = M, dp, dh, True
    return k


M_Z = ((1, 0, 0), (0, 1, 0))


def basis_zu(n):
    ax = min(range(3), key=lambda j: abs(n[j]))
    r = [0.0, 0.0, 0.0]
    r[ax] = 1.0
    d = dot3(r, n)
    e1 = norm3((r[0] - d * n[0], r[1] - d * n[1], r[2] - d * n[2]))
    e2 = (n[1] * e1[2] - n[2] * e1[1], n[2] * e1[0] - n[0] * e1[2], n[0] * e1[1] - n[1] * e1[0])
    return (e1, e2)


def setze_B(k, i, n, w, wh):
    e1, e2 = basis_zu(n)
    k.M[i] = (e1, e2)
    k.dp[i] = (dot3(e1, w), dot3(e2, w))
    k.dh[i] = (dot3(e1, wh), dot3(e2, wh))
    k.ex[i] = False


def konv_B(nv, q, w, wh, exakt_r0=False):
    """B: Projektion laengs n_i = q_i z q_i^-1, Push-off w. exakt_r0: alle q_i = 1, ganzzahlig (M_Z)."""
    if exakt_r0:
        return konv_global(nv, M_Z, (w[0], w[1]), (wh[0], wh[1]))
    k = Konv(nv)
    for i in range(nv):
        setze_B(k, i, qdreh(q[i], EZ), w, wh)
    return k


def proj(M, d):
    return (M[0][0] * d[0] + M[0][1] * d[1] + M[0][2] * d[2], M[1][0] * d[0] + M[1][1] * d[1] + M[1][2] * d[2])


def neues_st():
    return {"entartet": 0, "rand": 1.0}


def kegel(dl, a, b, ex, st):
    """1, wenn dl im offenen Kegel {alpha a + beta b; alpha, beta > 0} liegt (Kreuzung nahe dem Knoten)."""
    D = a[0] * b[1] - a[1] * b[0]
    Da = dl[0] * b[1] - dl[1] * b[0]
    Db = a[0] * dl[1] - a[1] * dl[0]
    ab = a[0] * b[0] + a[1] * b[1]
    if ex:
        if Da == 0 or Db == 0 or (D == 0 and ab < 0):
            st["entartet"] += 1
            return 0
    else:
        na = math.hypot(a[0], a[1])
        nb = math.hypot(b[0], b[1])
        nd = math.hypot(dl[0], dl[1])
        r = min(abs(Da) / (nd * nb), abs(Db) / (na * nd))
        if ab < 0:
            r = min(r, abs(D) / (na * nb))
        if r < st["rand"]:
            st["rand"] = r
        if r < RAND_MIN:
            st["entartet"] += 1
            return 0
    if D == 0:
        return 0
    return 1 if ((Da > 0) == (D > 0) and (Db > 0) == (D > 0)) else 0


class Lokal:
    """Lesart S als Summe knotenweiser Beitraege."""

    def __init__(self, Mo):
        N = Mo.N
        self.N = N
        self.Mo = Mo
        self.beine = [[(b, N.kante_id(s, tp.add(s, b))) for b in N.bonds(s)] for s in N.sites]
        self.schl_ecken = []
        for s in Mo.schl:
            kn = s["knoten"]
            k = len(kn)
            self.schl_ecken.append([(N.idx[N.mod(kn[j])], tp.sub3(kn[(j + 1) % k], kn[j]),
                                     tp.sub3(kn[(j - 1) % k], kn[j])) for j in range(k)])
        self.hop_enden = []
        for (u, w) in Mo.hop_kurve:
            self.hop_enden.append([(N.idx[N.mod(u)], tp.sub3(w, u)), (N.idx[N.mod(w)], tp.sub3(u, w))])
        nv = len(N.sites)
        self.schl_an = [[] for _ in range(nv)]
        for p, ecken in enumerate(self.schl_ecken):
            for (vi, de, de2) in ecken:
                self.schl_an[vi].append(p)
        self.hop_an = [[] for _ in range(nv)]
        for l, en in enumerate(self.hop_enden):
            for (xi, dx) in en:
                self.hop_an[xi].append(l)
        self.stern = [0] * nv
        for vi in range(nv):
            for (b, l) in self.beine[vi]:
                self.stern[vi] |= 1 << l

    def t_ecke(self, k, vi, de, de2, st):
        M, dl, ex = k.M[vi], k.dp[vi], k.ex[vi]
        pe, pe2 = proj(M, de), proj(M, de2)
        me, me2 = (-pe[0], -pe[1]), (-pe2[0], -pe2[1])
        T = 0
        for (b, l) in self.beine[vi]:
            pb = proj(M, b)
            c = 0
            if b != de:
                c += kegel(dl, pb, me, ex, st)
            if b != de2:
                c += kegel(dl, pb, me2, ex, st)
            if c & 1:
                T |= 1 << l
        return T

    def t_ende(self, k, xi, dx, st):
        M, dl, ex = k.M[xi], k.dh[xi], k.ex[xi]
        pd = proj(M, dx)
        md = (-pd[0], -pd[1])
        T = 0
        for (b, l) in self.beine[xi]:
            if b == dx:
                continue
            if kegel(dl, proj(M, b), md, ex, st):
                T |= 1 << l
        return T

    def T_schleife(self, k, p, st):
        T = 0
        for (vi, de, de2) in self.schl_ecken[p]:
            T ^= self.t_ecke(k, vi, de, de2, st)
        return T

    def T_huepfer(self, k, l, st):
        T = 0
        for (xi, dx) in self.hop_enden[l]:
            T ^= self.t_ende(k, xi, dx, st)
        return T

    def alle(self, k, st):
        TH = [self.T_huepfer(k, l, st) for l in range(len(self.hop_enden))]
        TS = [self.T_schleife(k, p, st) for p in range(len(self.schl_ecken))]
        return TH, TS

    def signatur(self, k, vi, st):
        sig = []
        for l in self.hop_an[vi]:
            for (xi, dx) in self.hop_enden[l]:
                if xi == vi:
                    sig.append(self.t_ende(k, vi, dx, st))
        for p in self.schl_an[vi]:
            for (xj, de, de2) in self.schl_ecken[p]:
                if xj == vi:
                    sig.append(self.t_ecke(k, vi, de, de2, st))
        return tuple(sig)


# ------------------------------------------------------------------ Messgroessen M1, M2
def m1m2(Mo, TH, TS):
    nl = len(Mo.N.links)
    schl = [{"X": s["X"], "typ": s["typ"], "knoten": s["knoten"], "Z": TS[p]} for p, s in enumerate(Mo.schl)]
    ss = tp.schleifen_paare(schl, "Z")
    hop_x = [1 << l for l in range(nl)]
    hs = tp.huepfer_schleifen(hop_x, TH, schl, "Z")
    t2 = tp.t2_messung(Mo.N, hop_x, TH)
    return {"schleifenpaare": ss["paare"], "schleife_schleife": ss["antikommut"],
            "huepfer_schleife_paare": hs["paare"], "huepfer_schleife": hs["antikommut"],
            "M1_summe": ss["antikommut"] + hs["antikommut"],
            "tripel": t2["anzahl"], "tripel_werte": t2["V1"], "tripel_inkonsistent": t2["inkonsistent"]}


def g1_zahl(Mo, TS, THg):
    schl = [{"X": s["X"], "Z": TS[p]} for p, s in enumerate(Mo.schl)]
    return tp.huepfer_schleifen([1 << l for l in range(len(Mo.N.links))], THg, schl, "Z")["antikommut"]


# ------------------------------------------------------------------ Rahmenfelder
def feld_R0(N):
    return [(1.0, 0.0, 0.0, 0.0) for _ in N.sites]


def feld_R1(N, theta_grad, saat):
    """Glatt zufaellig: Drehvektorfeld aus 13 periodischen Grundmoden, skaliert auf groessten Bindungswinkel."""
    rng = random.Random(1000 + saat)   # gleiche Feldform fuer alle theta_max je Saat
    amp = [(tuple(rng.gauss(0, 1) for _ in range(3)), tuple(rng.gauss(0, 1) for _ in range(3))) for _ in MODEN]
    eta = []
    for s in N.sites:
        e = [0.0, 0.0, 0.0]
        for (kv, (a, b)) in zip(MODEN, amp):
            ph = 2.0 * math.pi * (kv[0] * s[0] + kv[1] * s[1] + kv[2] * s[2]) / N.per
            c, sn = math.cos(ph), math.sin(ph)
            for j in range(3):
                e[j] += a[j] * c + b[j] * sn
        eta.append(e)

    def qs(lam):
        return [qexp((lam * e[0], lam * e[1], lam * e[2])) for e in eta]

    def maxw(qq):
        return max(bwinkel(qq[a], qq[b]) for (a, b) in N.links)
    ziel = math.radians(theta_grad)
    lo, hi = 0.0, 0.05
    while maxw(qs(hi)) < ziel and hi < 1e3:
        hi *= 2.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if maxw(qs(mid)) < ziel:
            lo = mid
        else:
            hi = mid
    return qs(lo)


def min_bild(N, s):
    out = []
    for j in range(3):
        d = s[j] % N.per
        if d > N.per / 2:
            d -= N.per
        out.append(d)
    return out


def feld_R2(N, achse, r0=1.8):
    """Kern (r <= r0 um den Knoten (0,0,0)) um 360 Grad gedreht, Profil h = (1/r - 1/R)/(1/r0 - 1/R) wie
    Z2-SCHUTZ (finn.Netz), R = halbe Zellkante des Torus (kleine Kugel)."""
    R = N.per / 2.0
    q = []
    for s in N.sites:
        d = min_bild(N, s)
        r = math.sqrt(d[0] ** 2 + d[1] ** 2 + d[2] ** 2)
        rc = max(r, r0)
        h = min(1.0, max(0.0, (1.0 / rc - 1.0 / R) / (1.0 / r0 - 1.0 / R)))
        q.append(qachse(achse, 2.0 * math.pi * h))
    return q


def feld_info(Mo, q):
    N = Mo.N
    bw = [math.degrees(bwinkel(q[a], q[b])) for (a, b) in N.links]
    s = [1 if qdot(q[a], q[b]) > 0 else -1 for (a, b) in N.links]
    nz = [math.degrees(math.acos(max(-1.0, min(1.0, qdreh(qq, EZ)[2])))) for qq in q]
    rot = [math.degrees(2.0 * math.acos(min(1.0, abs(qq[0])))) for qq in q]
    w2 = []
    for sc in Mo.schl:
        v = 1
        for l in sc["links"]:
            v *= s[l]
        w2.append(v)
    return {"bindungswinkel_max": round(max(bw), 6), "bindungswinkel_mittel": round(sum(bw) / len(bw), 4),
            "lift_minus_bindungen": s.count(-1), "w2_minus_schleifen": w2.count(-1),
            "n_abweichung_max_grad": round(max(nz), 4), "drehwinkel_max_grad": round(max(rot), 4)}, s, w2


# ------------------------------------------------------------------ M4 (PSG unter T, TWIST-SPIN-1 unveraendert)
def m4(Mo, TH, TS):
    r = ts.analyse(Mo, TH, TS, "T", (0, 0, 0), (0, 0, 0), True)
    el = r["elemente"]
    psg = r["psg"]
    return {"K_untergruppe": sorted(nm for nm, e in el.items() if e["stufe_K"]),
            "F_alle_elemente": all(e["stufe_F"] for e in el.values()),
            "fluss": {k: r["fluss"].get(k) for k in ("plus", "minus", "inkonsistent", "kein_korand")},
            "psg_invariante_C2hoch2": psg.get("invariante"),
            "psg_relationen": psg.get("relationen"),
            "K_relationen": {k: {"K_identitaet": v.get("K_identitaet"), "K_paarerzeuger": v.get("K_paarerzeuger")}
                             for k, v in r["relationen"].items()}}


# ------------------------------------------------------------------ M3 (oertliche Drehung von q_i)
def fluss_an(Mo, TH, TS, sch):
    sub = SimpleNamespace(N=Mo.N, G=Mo.G, schl=[Mo.schl[p] for p in sch])
    phi, info = ts.fermionfluss(sub, TH, [TS[p] for p in sch])
    return tuple(phi), info


def m1_lokal(Mo, lok, i, TH, TS):
    S = Mo.schl
    sch = lok.schl_an[i]
    n = 0
    for p in sch:
        Xp, Zp = S[p]["X"], TS[p]
        for q2 in range(len(S)):
            if q2 != p and ((Xp & TS[q2]).bit_count() + (Zp & S[q2]["X"]).bit_count()) & 1:
                n += 1
    for l in range(len(Mo.N.links)):
        for p in sch:
            if ((((1 << l) & TS[p]).bit_count()) + (TH[l] & S[p]["X"]).bit_count()) & 1:
                n += 1
    for l in lok.hop_an[i]:
        for q2 in range(len(S)):
            if q2 not in sch and ((((1 << l) & TS[q2]).bit_count()) + (TH[l] & S[q2]["X"]).bit_count()) & 1:
                n += 1
    return n


def ereignis(Mo, lok, i, TH0, TS0, TH1, TS1):
    hops = lok.hop_an[i]
    stern = lok.stern[i]
    C = {l: TH0[l] ^ TH1[l] for l in hops}
    sym = True
    for l in hops:
        if C[l] & ~stern or (C[l] >> l) & 1:
            sym = False
        for m in hops:
            if m != l and ((C[l] >> m) & 1) != ((C[m] >> l) & 1):
                sym = False

    def kgraph(TH):
        return tuple(((TH[l] >> m) & 1) ^ ((TH[m] >> l) & 1) for a, l in enumerate(hops) for m in hops[a + 1:])
    out = {"K_symmetrisch": sym, "K_graph_gleich": kgraph(TH0) == kgraph(TH1),
           "huepfer_geaendert": sum(1 for l in hops if C[l]),
           "schleifen_geaendert": sum(1 for p in lok.schl_an[i] if TS0[p] != TS1[p]), "schleifen": None}
    if sym:
        hm = 0
        for l in hops:
            hm |= 1 << l
        w = {"plus": 0, "minus": 0, "A_i": 0, "anders": 0, "imag": 0}
        for p in lok.schl_an[i]:
            x = Mo.schl[p]["X"]
            R = Pauli(0, x & ~hm, 0)
            for l in hops:
                if (x >> l) & 1:
                    R = R * Pauli(0, 1 << l, C[l])
            R = R * Pauli(0, 0, TS0[p])
            if R.x != x:
                w["anders"] += 1
                continue
            d = R.z ^ TS1[p]
            if d == 0:
                if R.k % 2:
                    w["imag"] += 1
                elif R.k % 4 == 0:
                    w["plus"] += 1
                else:
                    w["minus"] += 1
            elif d == stern:
                w["A_i"] += 1
            else:
                w["anders"] += 1
        out["schleifen"] = w
    out["M1_lokal"] = m1_lokal(Mo, lok, i, TH1, TS1)
    return out


def m3_B(Mo, lok, q, kv, TH, TS, i, achse, winkel, K, w, wh):
    st = neues_st()
    k = kv.kopie()
    sig0 = lok.signatur(k, i, st)
    sig = sig0
    TH, TS = list(TH), list(TS)
    sch = lok.schl_an[i]
    phi0, inf0 = fluss_an(Mo, TH, TS, sch)
    phi_start = phi0
    z = {"ereignisse": 0, "K_symmetrisch": 0, "K_graph_geaendert": 0, "schleifen_plus": 0, "schleifen_minus": 0,
         "schleifen_A_i": 0, "schleifen_anders": 0, "schleifen_imag": 0, "M1_verletzt_ereignisse": 0, "M1_max": 0,
         "fluss_geaendert": 0, "fluss_undefiniert": 0}
    liste = []
    Ctot = {l: 0 for l in lok.hop_an[i]}
    for s in range(1, K + 1):
        t = winkel * s / K
        qi = qmul(qachse(achse, t), q[i])
        setze_B(k, i, qdreh(qi, EZ), w, wh)
        sig1 = lok.signatur(k, i, st)
        if sig1 == sig:
            continue
        TH1, TS1 = list(TH), list(TS)
        for l in lok.hop_an[i]:
            TH1[l] = lok.T_huepfer(k, l, st)
        for p in sch:
            TS1[p] = lok.T_schleife(k, p, st)
        e = ereignis(Mo, lok, i, TH, TS, TH1, TS1)
        z["ereignisse"] += 1
        if e["K_symmetrisch"]:
            z["K_symmetrisch"] += 1
            for l in Ctot:
                Ctot[l] ^= TH[l] ^ TH1[l]
        if not e["K_graph_gleich"]:
            z["K_graph_geaendert"] += 1
        if e["schleifen"] is not None:
            for kk, vv in e["schleifen"].items():
                z["schleifen_" + kk] += vv
        if e["M1_lokal"]:
            z["M1_verletzt_ereignisse"] += 1
            z["M1_max"] = max(z["M1_max"], e["M1_lokal"])
        phi1, inf1 = fluss_an(Mo, TH1, TS1, sch)
        if None in phi1 or inf1["inkonsistent"] or inf1["kein_korand"]:
            z["fluss_undefiniert"] += 1
        elif phi1 != phi0:
            z["fluss_geaendert"] += 1
        if len(liste) < 24:
            liste.append({"t_grad": round(math.degrees(t), 3), "K_sym": e["K_symmetrisch"],
                          "K_gleich": e["K_graph_gleich"], "dH": e["huepfer_geaendert"],
                          "dS": e["schleifen_geaendert"], "schleifen": e["schleifen"], "M1": e["M1_lokal"],
                          "phi": [x if x is not None else 0 for x in phi1]})
        TH, TS, sig, phi0 = TH1, TS1, sig1, phi1
    z["zurueck_am_start"] = (sig == sig0)
    z["fluss_start_gleich_ende"] = (phi0 == phi_start)
    z["fluss_start"] = [x if x is not None else 0 for x in phi_start]
    z["fluss_start_info"] = {kk: inf0[kk] for kk in ("inkonsistent", "kein_korand")}
    alle_k = (z["ereignisse"] == z["K_symmetrisch"] and z["schleifen_minus"] == 0 and z["schleifen_A_i"] == 0
              and z["schleifen_anders"] == 0 and z["schleifen_imag"] == 0 and z["M1_verletzt_ereignisse"] == 0)
    z["C_gesamt_null"] = all(v == 0 for v in Ctot.values())
    # Stufe K: Transport = Produkt der CZ-Clifford-Abbildungen; bei Rueckkehr C_gesamt = 0 -> Identitaet -> +1
    z["M3_K_ende"] = (1 if z["C_gesamt_null"] else "Rest") if alle_k else None
    z["M3_F_ende"] = 1 if (z["fluss_undefiniert"] == 0 and z["fluss_geaendert"] == 0
                           and z["M1_verletzt_ereignisse"] == 0) else None
    z["M3_ohne_ende"] = 1 if alle_k or z["M3_F_ende"] == 1 else None
    z["min_rand"] = st["rand"]
    z["entartet"] = st["entartet"]
    z["ereignisliste"] = liste
    return z


def m3_C(Mo, lok, q, i, achse, winkel, K, partner):
    N = Mo.N
    nb = []
    for l, (a, b) in enumerate(N.links):
        if a == i:
            nb.append((l, b))
        elif b == i:
            nb.append((l, a))
    s_start = {l: (1 if qdot(q[i], q[j]) > 0 else -1) for (l, j) in nb}
    s_alt = dict(s_start)
    F = 0
    flips = {l: 0 for (l, j) in nb}
    for st_ in range(1, K + 1):
        qi = qmul(qachse(achse, winkel * st_ / K), q[i])
        for (l, j) in nb:
            s = 1 if qdot(qi, q[j]) > 0 else -1
            if s != s_alt[l]:
                F ^= 1 << l
                flips[l] += 1
                s_alt[l] = s
    # Transport je Kippung: Z_l (Fluss von a ueber l angepasst). Huepfer mit Hebungsbuchhaltung s_l X_l Z_T(l):
    # Z_l h Z_l = -h  <->  s_l kippt. Konsistenz: [l in F] == (s_ende != s_start).
    konsistent = all(((F >> l) & 1) == (1 if s_alt[l] != s_start[l] else 0) for (l, j) in nb)
    y = Mo.G.korand(F)
    if y is None:
        ende, ohne = None, None
    else:
        ende = -1 if (((y >> i) & 1) ^ ((y >> partner) & 1)) else 1
        ohne = 1
    return {"flips_je_bindung": [flips[l] for (l, j) in nb], "F_ist_stern": F == lok.stern[i], "F_leer": F == 0,
            "transport_konsistent": konsistent, "M3_ende": ende, "M3_ohne_ende": ohne}


def achsen(qi):
    # a2, a3 generisch (nach dem Rauchlauf: die Achse genau x traf bei R0 exakt entartete Projektionen, n = (0,1,1)/sqrt2)
    return {"a1_n_i": qdreh(qi, EZ), "a2_fast_senkrecht": qdreh(qi, norm3((1.0, 0.27, -0.13))),
            "a3_schraeg": qdreh(qi, norm3((0.37, 0.61, 0.70)))}


def fluss_zaehlung(Mo, TH, TS):
    phi, info = ts.fermionfluss(Mo, TH, TS)
    return {"plus": phi.count(1), "minus": phi.count(-1), "undefiniert": phi.count(None),
            "inkonsistent": info["inkonsistent"], "kein_korand": info["kein_korand"]}


# ------------------------------------------------------------------ Laeufe
def rahmen_liste(N, saaten, mit_r2=True):
    out = [("R0", None, None, feld_R0(N))]
    for th in THETAS:
        for sd in range(saaten):
            out.append(("R1", th, sd, feld_R1(N, th, sd)))
    if mit_r2:
        out.append(("R2z", None, None, feld_R2(N, EZ)))
        out.append(("R2x", None, None, feld_R2(N, (1.0, 0.0, 0.0))))
    return out


def lauf_basis(n, saaten, mit_m4):
    t0 = time.time()
    Mo = ts.Modell("diamant", n)
    lok = Lokal(Mo)
    N = Mo.N
    nv = len(N.sites)
    out = {"knoten": nv, "kanten": len(N.links), "schleifen": len(Mo.schl), "A": {}, "rahmen": [], "M4": {}}
    THA, TSA = {}, {}
    # ---- Variante A (GFR0): lokale Formulierung gegen tp.drehung, M1, M2, G1
    for P in ("P1", "P2", "P3"):
        M = tp.PROJ[P]
        TH0, TS0, zg = Mo.drehmengen(M)
        st = neues_st()
        k = konv_global(nv, M, tp.DELTA_P, tp.DELTA_H)
        TH, TS = lok.alle(k, st)
        kg = konv_global(nv, M, tp.DELTA_P, tp.DELTA_P)
        THg, _ = lok.alle(kg, neues_st())
        r = m1m2(Mo, TH, TS)
        r["bitgleich_huepfer"] = TH == TH0
        r["bitgleich_schleifen"] = TS == TS0
        r["abweichend_huepfer"] = sum(1 for a, b in zip(TH, TH0) if a != b)
        r["abweichend_schleifen"] = sum(1 for a, b in zip(TS, TS0) if a != b)
        r["generik_tp"] = zg
        r["entartet_lokal"] = st["entartet"]
        r["G1_gleichsinnig"] = g1_zahl(Mo, TS, THg)
        r["fermionfluss"] = fluss_zaehlung(Mo, TH, TS)
        out["A"][P] = r
        THA[P], TSA[P] = TH, TS
    # ---- Rahmenklassen: B (zwei Push-offs), C
    rC0 = m1m2(Mo, THA["P2"], TSA["P2"])
    kz = {}
    for wn, w in (("w_haupt", W_HAUPT), ("w_alt", W_ALT)):
        kz[wn] = konv_B(nv, None, w, (-w[0], -w[1], -w[2]), exakt_r0=True)
    for (rk, th, sd, q) in rahmen_liste(N, saaten):
        info, s, w2 = feld_info(Mo, q)
        e = {"klasse": rk, "theta_max": th, "saat": sd, "feld": info, "B": {}}
        for wn, w in (("w_haupt", W_HAUPT), ("w_alt", W_ALT)):
            wh = (-w[0], -w[1], -w[2])
            st = neues_st()
            if rk == "R0":
                kB = kz[wn]
            else:
                kB = konv_B(nv, q, w, wh)
            TH, TS = lok.alle(kB, st)
            r = m1m2(Mo, TH, TS)
            r["entartet"] = st["entartet"]
            r["min_rand"] = st["rand"]
            stz = neues_st()
            r["knoten_signatur_anders_als_z"] = sum(1 for vi in range(nv)
                                                    if lok.signatur(kB, vi, stz) != lok.signatur(kz[wn], vi, stz))
            kg = konv_B(nv, q, w, w, exakt_r0=(rk == "R0"))
            THg, _ = lok.alle(kg, neues_st())
            r["G1_gleichsinnig"] = g1_zahl(Mo, TS, THg)
            r["fermionfluss"] = fluss_zaehlung(Mo, TH, TS)
            if rk == "R0":
                kf = konv_B(nv, q, w, wh)     # Gleitkomma-Fassung bei q = 1 muss die exakte treffen
                THf, TSf = lok.alle(kf, neues_st())
                r["gleitkomma_gleich_exakt"] = (THf == TH and TSf == TS)
                if mit_m4:
                    out["M4"]["B_R0_" + wn] = m4(Mo, TH, TS)
            e["B"][wn] = r
        # C: Z-Mengen wie A (P2), c-Zahlen s_l, w2(p): Vertauschungsvorzeichen unveraendert
        rC = dict(rC0)
        rC["huepfer_mit_s_minus"] = s.count(-1)
        rC["schleifen_mit_w2_minus"] = w2.count(-1)
        e["C_P2"] = rC
        out["rahmen"].append(e)
        print("n", n, rk, th, sd, round(time.time() - t0, 1), "s", flush=True)
    # Gegenprobe G2 [nach dem Rauchlauf ergaenzt]: Schleifen mit ungeradem Index nehmen am selben Knoten eine andere
    # Push-off-Richtung (w_alt statt w_haupt, R0 exakt). Die Schleifenpaar-Pruefung muss dann anschlagen koennen.
    _, TS1 = lok.alle(kz["w_haupt"], neues_st())
    _, TS2 = lok.alle(kz["w_alt"], neues_st())
    TSg = [TS1[p] if p % 2 == 0 else TS2[p] for p in range(len(TS1))]
    schl = [{"X": s["X"], "typ": s["typ"], "knoten": s["knoten"], "Z": TSg[p]} for p, s in enumerate(Mo.schl)]
    out["G2_schleifenpaare_gemischt"] = tp.schleifen_paare(schl, "Z")["antikommut"]
    if mit_m4:
        for P in ("P1", "P2", "P3"):
            out["M4"]["A_" + P] = m4(Mo, THA[P], TSA[P])
        out["M4"]["C_R0_P2"] = "identisch mit A_P2 (R0: alle s = +1, w2 = +1; gleiche Operatoren)"
    out["zeit_s"] = round(time.time() - t0, 2)
    return out


def lauf_m3(n, K, saat_r1, ws, mit_doppelt):
    t0 = time.time()
    Mo = ts.Modell("diamant", n)
    lok = Lokal(Mo)
    N = Mo.N
    nv = len(N.sites)
    i0 = N.idx[(0, 0, 0)]
    i1 = N.idx[(1, 1, 1)]
    part = {i0: N.idx[N.mod((2 * n, 2 * n, 0))], i1: N.idx[N.mod((2 * n + 1, 2 * n + 1, 1))]}
    out = {"K": K, "knoten": {"i0": list(N.sites[i0]), "i1": list(N.sites[i1])},
           "partner": {"i0": list(N.sites[part[i0]]), "i1": list(N.sites[part[i1]])}, "faelle": []}
    rl = [("R0", None, None, feld_R0(N))] + [("R1", th, saat_r1, feld_R1(N, th, saat_r1)) for th in THETAS] + \
         [("R2z", None, None, feld_R2(N, EZ)), ("R2x", None, None, feld_R2(N, (1.0, 0.0, 0.0)))]
    for (rk, th, sd, q) in rl:
        info, s, w2 = feld_info(Mo, q)
        for wn in ws:
            w = W_HAUPT if wn == "w_haupt" else W_ALT
            wh = (-w[0], -w[1], -w[2])
            kv = konv_B(nv, q, w, wh)
            stb = neues_st()
            TH, TS = lok.alle(kv, stb)
            m1g = m1m2(Mo, TH, TS)["M1_summe"]
            for (iname, i) in (("i0", i0), ("i1", i1)):
                for an, a in achsen(q[i]).items():
                    for wg in (2, 4):
                        f = {"klasse": rk, "theta_max": th, "saat": sd, "w": wn, "knoten": iname, "achse": an,
                             "winkel_pi": wg, "M1_rahmen_gesamt": m1g}
                        f["B"] = m3_B(Mo, lok, q, kv, TH, TS, i, a, wg * math.pi, wg // 2 * K, w, wh)
                        if wn == ws[0]:
                            f["C"] = m3_C(Mo, lok, q, i, a, wg * math.pi, wg // 2 * K, part[i])
                            f["A"] = {"ereignisse": 0, "M3_ende": 1, "M3_ohne_ende": 1,
                                      "grund": "Konvention haengt nicht vom Rahmen ab"}
                        if mit_doppelt and wg == 2 and rk in ("R0", "R1") and (th in (None, 30)) and iname == "i0":
                            d = m3_B(Mo, lok, q, kv, TH, TS, i, a, wg * math.pi, 2 * K, w, wh)
                            f["B_K_doppelt"] = {kk: d[kk] for kk in ("ereignisse", "K_symmetrisch", "K_graph_geaendert",
                                                                    "M1_verletzt_ereignisse", "fluss_geaendert",
                                                                    "fluss_undefiniert", "M3_K_ende", "M3_F_ende")}
                        out["faelle"].append(f)
            print("m3 n", n, rk, th, wn, round(time.time() - t0, 1), "s", flush=True)
        out.setdefault("felder", []).append({"klasse": rk, "theta_max": th, "saat": sd, "feld": info})
    out["zeit_s"] = round(time.time() - t0, 2)
    return out


def main():
    modus, aus = sys.argv[1], sys.argv[2]
    ns = [int(x) for x in sys.argv[3:]] or [2]
    erg = {"meta": {"karte": "GERAHMTER-FADEN-1 (Runde 50)", "modus": modus, "python": platform.python_version(),
                    "code_sha256": sha(os.path.abspath(__file__)), "tp_sha256": sha(os.path.abspath(tp.__file__)),
                    "ts_sha256": sha(os.path.abspath(ts.__file__)), "W_HAUPT": W_HAUPT, "W_ALT": W_ALT,
                    "RAND_MIN": RAND_MIN, "start_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(T0))}}
    if modus == "rauch":
        erg["basis"] = {str(n): lauf_basis(n, 1, True) for n in ns}
        erg["m3"] = {str(n): lauf_m3(n, 360, 0, ("w_haupt",), False) for n in ns}
    elif modus == "basis":
        erg["basis"] = {str(n): lauf_basis(n, 6, True) for n in ns}
    elif modus == "g2":
        # Gegenprobe G2 (nach dem Basislauf ergaenzt, Vorhersage in ERGEBNIS.md vor diesem Lauf): Schleifen mit
        # ungeradem Index nehmen am selben Knoten (R0, n = z, exakt) eine andere Push-off-Richtung.
        erg["g2"] = {}
        for n in ns:
            Mo = ts.Modell("diamant", n)
            lok = Lokal(Mo)
            nv = len(Mo.N.sites)
            r = {}
            for name, w2 in (("gleicher_sektor_w_alt", W_ALT), ("gegenrichtung_minus_w", (5, -4, 0)),
                             ("anderer_sektor_4_5_0", (4, 5, 0))):
                st = neues_st()
                _, TS1 = lok.alle(konv_B(nv, None, W_HAUPT, (5, -4, 0), exakt_r0=True), st)
                _, TS2 = lok.alle(konv_B(nv, None, w2, (-w2[0], -w2[1], -w2[2]), exakt_r0=True), st)
                TSg = [TS1[p] if p % 2 == 0 else TS2[p] for p in range(len(TS1))]
                schl = [{"X": s["X"], "typ": s["typ"], "knoten": s["knoten"], "Z": TSg[p]}
                        for p, s in enumerate(Mo.schl)]
                r[name] = {"schleifenpaare_antikommut": tp.schleifen_paare(schl, "Z")["antikommut"],
                           "schleifen_mit_anderem_T": sum(1 for a, b in zip(TS1, TS2) if a != b),
                           "entartet": st["entartet"]}
            erg["g2"][str(n)] = r
    elif modus in ("m3", "m3h", "m3a"):
        ws = {"m3": ("w_haupt", "w_alt"), "m3h": ("w_haupt",), "m3a": ("w_alt",)}[modus]
        erg["m3"] = {str(n): lauf_m3(n, 1440, 0, ws, True) for n in ns}
    else:
        raise SystemExit("unbekannter Modus")
    erg["laufzeit_s"] = round(time.time() - T0, 2)
    with open(aus + ".tmp", "w") as fh:
        json.dump(erg, fh, indent=1, sort_keys=True, default=str)
    os.replace(aus + ".tmp", aus)
    print("fertig", modus, erg["laufzeit_s"], "s")


if __name__ == "__main__":
    main()
