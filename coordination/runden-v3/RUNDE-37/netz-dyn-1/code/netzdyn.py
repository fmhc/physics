#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NETZ-DYN-1 (fmhc-physics, Runde 37), Bau- und Rechenagent (Claude-Subagent) fuer die Leitung claude-primary.

Monte-Carlo ueber Verknuepfungen mit Zeitschichten (CDT-artig) und ohne (DT), mit Feldern mit Rueckwirkung.
Ein dimensionsfreier Kern: Simplizes als sortierte Eckentupel, Zeitschicht je Ecke (periodisch, T Schichten).

Modi:
  cdt2  1+1D: Schichten = Ringe. Zuege: 2-2 (Pachner, zeitartig) und (2,4)/(4,2) (Schicht-Pachner 1-2/2-1 hochgehoben).
        S = lam N2 + eps (N2 - Nz)^2           (lam = --k4)
  cdt4  3+1D: Schichten = 3D-Triangulierungen; Start Finns Netz V (ew.geometrie('V'), unveraendert), LxLxL Zellen,
        Treppenzerlegung Tetraeder x Intervall. Zuege [L, Ambjoern/Jurkiewicz/Loll aus dem Gedaechtnis, Annahme]:
        (2,8),(8,2),(4,6),(6,4) = Schicht-Pachner 1-4, 4-1, 2-3, 3-2, hochgehoben auf die Kegel darueber/darunter;
        (2,4),(4,2),(3,3) = 4D-Pachner 2-4, 4-2, 3-3 mit Pruefung: alle neuen Simplizes kausal, keine raumartige
        Teilflaeche entsteht oder verschwindet.
        S = -(k0 + 6 Delta) N0 + k4 N4 + Delta (2 N41 + N32) + eps (N4 - Nz)^2   (AJL-Zaehlform)
  dt4   4D ohne Zeitschichten (freie Pachner-Zuege 1-5, 2-4, 3-3, 4-2, 5-1), S = -k0 N0 + k4 N4 + eps (N4 - Nz)^2
Auswahl: zufaelliges Simplex, zufaellige Teilflaeche; Annahme min(1, N/N' exp(-dS) * Feldfaktor) (Auswahlfaktor N/N').
Felder (optional; Rueckwirkung ueber exakte Rosenbluth-Gewichte des bedingten Waermebads neuer Kanten bzw. Ecken):
  U(1)  auf Kanten, Wilson ueber Dreiecke, Gewicht w = 1:   S = bu * sum_D (1 - cos F_D)
  SU(2) auf Kanten (Einheitsquaternionen):                 S = bs * sum_D (1 - 1/2 Tr U_D)
  Rahmen: SU(2) an Ecken (O(4)-Rotor, Nachbarkopplung):     S = J * sum_Kanten (1 - R_a . R_b)
Messgroessen: Volumenprofil, Schalen n(r) im dualen Netz (Hausdorff), Rueckkehrwahrscheinlichkeit der Diffusion im
  dualen Netz (spektrale Dimension), Gradverteilung, Superpunkte (Grad > 5 x Mittel) mit Lebensdauer, U(1)-Ladung und
  Rahmen-Igelzahl durch die raeumliche Huelle (Link) von Superpunkten, Plakette, Rahmenordnung.
Laeufe hoechstens 10 min: Zeitbudget --zeit, danach Zwischenstand (pickle, neue Datei + mv, nur der letzte bleibt).
"""
import argparse, json, math, os, pickle, random, sys, time, hashlib, itertools, platform
import numpy as np
from scipy.special import i0e, i1e

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)

ZWEI_PI = 2.0 * math.pi


# ------------------------------------------------------------------------------------------------ kleine Helfer
def log_i0(k):
    return math.log(float(i0e(k))) + k


def log_zsu2(x):
    """log Z(x), Z(x) = int dHaar exp(x W0) = 2 I1(x)/x."""
    if x < 1e-9:
        return 0.0
    return math.log(2.0 * float(i1e(x)) / x) + x


def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
            a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)


def qconj(a):
    return (a[0], -a[1], -a[2], -a[3])


def qdot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]


def q_haar(rng):
    while True:
        x = [rng.gauss(0.0, 1.0) for _ in range(4)]
        n = math.sqrt(sum(c * c for c in x))
        if n > 1e-12:
            return tuple(c / n for c in x)


def q_waermebad(x, rng):
    """Einheitsquaternion W mit Dichte ~ exp(x W0) bzgl. Haar (Creutz-Verfahren)."""
    if x < 1e-6:
        return q_haar(rng)
    e2 = math.exp(-2.0 * x)
    while True:
        r1 = rng.random()
        w0 = 1.0 + math.log(r1 + (1.0 - r1) * e2) / x
        if rng.random() < math.sqrt(max(0.0, 1.0 - w0 * w0)):
            break
    z = 2.0 * rng.random() - 1.0
    ph = ZWEI_PI * rng.random()
    s = math.sqrt(max(0.0, 1.0 - z * z))
    r = math.sqrt(max(0.0, 1.0 - w0 * w0))
    return (w0, r * s * math.cos(ph), r * s * math.sin(ph), r * z)


def wrap(x):
    """auf (-pi, pi]"""
    y = math.fmod(x + math.pi, ZWEI_PI)
    if y <= 0.0:
        y += ZWEI_PI
    return y - math.pi


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


# ------------------------------------------------------------------------------------------------ Startnetze
def v_netz(L):
    """Finns gefuelltes Netz V (ew.geometrie('V'), unveraendert importiert), periodisch LxLxL primitive Zellen."""
    import ew  # noqa: E402  (TT-ISO-1 / EINE-WELT-LOCH-1, unveraendert kopiert)
    pos8, zellen = ew.geometrie('V')
    tets = [[ew.zerlege(x, pos8) for x in z['X8']] for z in zellen]
    nsub = len(pos8)

    def vid(s, n, c):
        m = [(n[i] + c[i]) % L for i in range(3)]
        return s + nsub * (m[0] + L * (m[1] + L * m[2]))

    out = set()
    for c in itertools.product(range(L), repeat=3):
        for T in tets:
            vs = tuple(sorted(vid(s, n, c) for (s, n) in T))
            assert len(set(vs)) == 4, 'Tetraeder entartet bei L=%d' % L
            out.add(vs)
    assert len(out) == len(tets) * L ** 3, 'Tetraeder fallen zusammen bei L=%d' % L
    return sorted(out), nsub * L ** 3, len(tets), nsub


def prisma4(tets, nV, T):
    """Treppenzerlegung Tetraeder x Intervall, T Schichten periodisch. Ecke (v, t) -> v + nV t."""
    sims = []
    for t in range(T):
        t1 = (t + 1) % T
        for tt in tets:
            v = sorted(tt)
            for k in range(4):
                s = [v[i] + nV * t for i in range(k + 1)] + [v[i] + nV * t1 for i in range(k, 4)]
                sims.append(tuple(sorted(s)))
    vt = {v + nV * t: t for t in range(T) for v in range(nV)}
    return sims, vt


def ring2(L0, T):
    sims = []
    for t in range(T):
        t1 = (t + 1) % T
        for i in range(L0):
            a, b = sorted((i, (i + 1) % L0))
            sims.append(tuple(sorted((a + L0 * t, a + L0 * t1, b + L0 * t1))))
            sims.append(tuple(sorted((a + L0 * t, b + L0 * t, b + L0 * t1))))
    vt = {v + L0 * t: t for t in range(T) for v in range(L0)}
    return sims, vt


# ------------------------------------------------------------------------------------------------ Kern
class Netz:
    def __init__(self, d, T, kausal, seed, sims, vt):
        self.d, self.T, self.kausal = d, T, kausal
        self.rng = random.Random(seed)
        self.nrng = np.random.default_rng(seed)
        self.simp, self.vstar, self.vt = {}, {}, {}
        self.slist, self.spos = [], {}
        self.nsid, self.nvid = 0, 0
        self.n41 = 0
        for v, t in vt.items():
            self.vt[v] = t
            self.vstar[v] = set()
        self.nvid = max(vt) + 1
        for s in sims:
            self.add_s(s)
        # Wirkung
        self.k0 = self.k4 = self.Delta = self.eps = 0.0
        self.Nz = len(self.slist)
        # Felder
        self.u1 = self.su2 = self.rahmen = None
        self.bu = self.bs = self.J = 0.0
        # Zugstatistik
        self.p_raum = 0.5
        self.pdims = list(range(1, d)) if kausal else list(range(0, d + 1))
        self.prop, self.acc = {}, {}
        self.sweep = 0

    # --- Grundoperationen
    def ist41(self, s):
        t0 = self.vt[s[0]]
        c = 0
        for v in s:
            if self.vt[v] == t0:
                c += 1
        return c == 1 or c == self.d

    def ist_kausal(self, s):
        ts = set(self.vt[v] for v in s)
        if len(ts) != 2:
            return False
        a, b = ts
        return (a - b) % self.T in (1, self.T - 1)

    def ist_raumartig(self, f):
        t0 = self.vt[f[0]]
        for v in f[1:]:
            if self.vt[v] != t0:
                return False
        return True

    def add_s(self, s):
        sid = self.nsid
        self.nsid += 1
        self.simp[sid] = s
        for v in s:
            self.vstar[v].add(sid)
        self.spos[sid] = len(self.slist)
        self.slist.append(sid)
        if self.kausal and self.ist41(s):
            self.n41 += 1
        return sid

    def del_s(self, sid):
        s = self.simp.pop(sid)
        for v in s:
            self.vstar[v].discard(sid)
        i = self.spos.pop(sid)
        last = self.slist.pop()
        if last != sid:
            self.slist[i] = last
            self.spos[last] = i
        if self.kausal and self.ist41(s):
            self.n41 -= 1

    def stern(self, f):
        if len(f) == 1:
            return set(self.vstar[f[0]])
        ss = sorted((self.vstar[v] for v in f), key=len)
        return ss[0].intersection(*ss[1:])

    def existiert(self, f):
        ss = sorted((self.vstar[v] for v in f), key=len)
        if len(ss) == 2:
            return not ss[0].isdisjoint(ss[1])
        return bool(ss[0].intersection(*ss[1:]))

    def S_geo(self, N0, N, N41):
        if self.d == 4 and self.kausal:
            S = -(self.k0 + 6.0 * self.Delta) * N0 + self.k4 * N + self.Delta * (2 * N41 + (N - N41))
        elif self.d == 4:
            S = -self.k0 * N0 + self.k4 * N
        else:
            S = self.k4 * N
        return S + self.eps * (N - self.Nz) ** 2

    # --- Vorschlaege
    def vorschlag_pachner(self):
        sid = self.slist[self.rng.randrange(len(self.slist))]
        s = self.simp[sid]
        d = self.d
        i = self.pdims[self.rng.randrange(len(self.pdims))]
        if i == d:
            if self.kausal:
                return None
            w = self.nvid
            neu = [s[:m] + s[m + 1:] + (w,) for m in range(d + 1)]
            return ('p%d' % i, [sid], neu, w, 0, -1)
        sigma = tuple(sorted(self.rng.sample(s, i + 1)))
        if self.kausal and len(sigma) >= 2 and self.ist_raumartig(sigma):
            return None
        k = d + 1 - i
        st = self.stern(sigma)
        if len(st) != k:
            return None
        tau = set()
        for x in st:
            tau.update(self.simp[x])
        tau.difference_update(sigma)
        if len(tau) != k:
            return None
        tau = tuple(sorted(tau))
        if self.existiert(tau):
            return None
        if self.kausal and self.ist_raumartig(tau):
            return None
        neu = [tuple(sorted(sigma[:m] + sigma[m + 1:] + tau)) for m in range(len(sigma))]
        if self.kausal:
            for x in neu:
                if not self.ist_kausal(x):
                    return None
        weg = sigma[0] if i == 0 else -1
        return ('p%d' % i, list(st), neu, -1, 0, weg)

    def vorschlag_raum(self):
        sid = self.slist[self.rng.randrange(len(self.slist))]
        s = self.simp[sid]
        d, T = self.d, self.T
        ts = [self.vt[v] for v in s]
        t0 = ts[0]
        c0 = ts.count(t0)
        if c0 == d:
            tb = t0
        elif c0 == 1:
            tb = ts[1] if ts[1] != t0 else ts[2]
            if ts.count(tb) != d:
                return None
        else:
            return None
        base = tuple(v for v in s if self.vt[v] == tb)
        j = self.rng.randrange(d)
        sigma = tuple(sorted(self.rng.sample(base, j + 1)))
        k = d - j
        st = self.stern(sigma)
        if len(st) != 2 * k:
            return None
        ups, dns, pa, qa = [], [], set(), set()
        for x in st:
            sx = self.simp[x]
            b = tuple(v for v in sx if self.vt[v] == tb)
            if len(b) != d:
                return None
            a = [v for v in sx if self.vt[v] != tb][0]
            if (self.vt[a] - tb) % T == 1:
                ups.append(b)
                pa.add(a)
            else:
                dns.append(b)
                qa.add(a)
        if len(pa) != 1 or len(qa) != 1 or len(ups) != k or sorted(ups) != sorted(dns):
            return None
        p, q = pa.pop(), qa.pop()
        if j == d - 1:
            w = self.nvid
            nb = [base[:m] + base[m + 1:] + (w,) for m in range(d)]
            neue, tw, weg = w, tb, -1
        else:
            tau = set()
            for b in ups:
                tau.update(b)
            tau.difference_update(sigma)
            if len(tau) != k:
                return None
            tau = tuple(sorted(tau))
            if self.existiert(tau):
                return None
            nb = [tuple(sorted(sigma[:m] + sigma[m + 1:] + tau)) for m in range(len(sigma))]
            neue, tw = -1, 0
            weg = sigma[0] if j == 0 else -1
        neu = [tuple(sorted(b + (p,))) for b in nb] + [tuple(sorted(b + (q,))) for b in nb]
        return ('r%d' % j, list(st), neu, neue, tw, weg)

    # --- Felder: Gewichte fuer Geometriezuege
    def uget(self, e, tmp):
        v = tmp.get(e)
        return self.u1[e] if v is None else v

    def sget(self, e, tmp):
        v = tmp.get(e)
        return self.su2[e] if v is None else v

    def u1_F(self, D, tmp):
        a, b, c = D
        return self.uget((a, b), tmp) + self.uget((b, c), tmp) - self.uget((a, c), tmp)

    def su2_tr(self, D, tmp):
        a, b, c = D
        return qmul(qmul(self.sget((a, b), tmp), self.sget((b, c), tmp)), qconj(self.sget((a, c), tmp)))[0]

    def u1_lokal(self, e, Ds, tmp):
        re = im = 0.0
        for D in Ds:
            a, b, c = D
            e1, e2, e3 = (a, b), (b, c), (a, c)
            if e == e1:
                ph = self.uget(e2, tmp) - self.uget(e3, tmp)
            elif e == e2:
                ph = self.uget(e1, tmp) - self.uget(e3, tmp)
            else:  # e == e3, Vorzeichen -1: s * c = -(th_ab + th_bc)
                ph = -(self.uget(e1, tmp) + self.uget(e2, tmp))
            re += math.cos(ph)
            im += math.sin(ph)
        R = math.hypot(re, im)
        psi = math.atan2(im, re) if R > 0 else 0.0
        return self.bu * R, -psi

    def su2_lokal(self, e, Ds, tmp):
        S = [0.0, 0.0, 0.0, 0.0]
        for D in Ds:
            a, b, c = D
            e1, e2, e3 = (a, b), (b, c), (a, c)
            if e == e1:
                X = qmul(self.sget(e2, tmp), qconj(self.sget(e3, tmp)))
            elif e == e2:
                X = qmul(qconj(self.sget(e3, tmp)), self.sget(e1, tmp))
            else:
                X = qmul(qconj(self.sget(e2, tmp)), qconj(self.sget(e1, tmp)))
            for m in range(4):
                S[m] += X[m]
        k = math.sqrt(sum(c * c for c in S))
        V = tuple(c / k for c in S) if k > 1e-12 else (1.0, 0.0, 0.0, 0.0)
        return self.bs * k, V

    def feld_gewicht(self, alt_t, neu, w, weg):
        E_alt, D_alt, E_neu, D_neu = set(), set(), set(), set()
        for s in alt_t:
            E_alt.update(itertools.combinations(s, 2))
            D_alt.update(itertools.combinations(s, 3))
        for s in neu:
            E_neu.update(itertools.combinations(s, 2))
            D_neu.update(itertools.combinations(s, 3))
        E_add = sorted(E_neu - E_alt)
        E_rem = sorted(E_alt - E_neu)
        D_add = D_neu - D_alt
        D_rem = D_alt - D_neu
        lw = 0.0
        werte = {'E_add': E_add, 'E_rem': E_rem}
        Eadd_s, Erem_s = set(E_add), set(E_rem)
        if self.u1 is not None or self.su2 is not None:
            # Deckung: jedes neue (entfernte) Dreieck an der letzten neuen (entfernten) Kante in Sortierordnung
            dk_add, det_add, dk_rem, det_rem = {}, [], {}, []
            for D in D_add:
                a, b, c = D
                ne = [x for x in ((a, b), (b, c), (a, c)) if x in Eadd_s]
                if ne:
                    dk_add.setdefault(max(ne), []).append(D)
                else:
                    det_add.append(D)
            for D in D_rem:
                a, b, c = D
                ne = [x for x in ((a, b), (b, c), (a, c)) if x in Erem_s]
                if ne:
                    dk_rem.setdefault(max(ne), []).append(D)
                else:
                    det_rem.append(D)
            if self.u1 is not None:
                tmp = {}
                for e in E_add:
                    Ds = dk_add.get(e, [])
                    kap, mu = self.u1_lokal(e, Ds, tmp)
                    tmp[e] = self.rng.vonmisesvariate(mu, kap) if kap > 1e-12 else ZWEI_PI * self.rng.random()
                    lw += log_i0(kap) - self.bu * len(Ds)
                for e in E_rem:
                    Ds = dk_rem.get(e, [])
                    kap, mu = self.u1_lokal(e, Ds, {})
                    lw += self.bu * len(Ds) - log_i0(kap)
                for D in det_add:
                    lw -= self.bu * (1.0 - math.cos(self.u1_F(D, tmp)))
                for D in det_rem:
                    lw += self.bu * (1.0 - math.cos(self.u1_F(D, {})))
                werte['u1'] = tmp
            if self.su2 is not None:
                tmp = {}
                for e in E_add:
                    Ds = dk_add.get(e, [])
                    x, V = self.su2_lokal(e, Ds, tmp)
                    W = q_waermebad(x, self.rng)
                    tmp[e] = qmul(W, qconj(V))
                    lw += log_zsu2(x) - self.bs * len(Ds)
                for e in E_rem:
                    Ds = dk_rem.get(e, [])
                    x, V = self.su2_lokal(e, Ds, {})
                    lw += self.bs * len(Ds) - log_zsu2(x)
                for D in det_add:
                    lw -= self.bs * (1.0 - self.su2_tr(D, tmp))
                for D in det_rem:
                    lw += self.bs * (1.0 - self.su2_tr(D, {}))
                werte['su2'] = tmp
        if self.rahmen is not None:
            R = self.rahmen
            for (a, b) in E_add:
                if a != w and b != w:
                    lw -= self.J * (1.0 - qdot(R[a], R[b]))
            for (a, b) in E_rem:
                if a != weg and b != weg:
                    lw += self.J * (1.0 - qdot(R[a], R[b]))
            if w >= 0:
                nb = [a if b == w else b for (a, b) in E_add if a == w or b == w]
                S = [0.0, 0.0, 0.0, 0.0]
                for n in nb:
                    for m in range(4):
                        S[m] += R[n][m]
                k = math.sqrt(sum(c * c for c in S))
                V = tuple(c / k for c in S) if k > 1e-12 else (1.0, 0.0, 0.0, 0.0)
                x = self.J * k
                W = q_waermebad(x, self.rng)
                werte['Rw'] = qmul(V, W)
                lw += log_zsu2(x) - self.J * len(nb)
            if weg >= 0:
                nb = [a if b == weg else b for (a, b) in E_rem if a == weg or b == weg]
                S = [0.0, 0.0, 0.0, 0.0]
                for n in nb:
                    for m in range(4):
                        S[m] += R[n][m]
                k = math.sqrt(sum(c * c for c in S))
                lw += self.J * len(nb) - log_zsu2(self.J * k)
        return lw, werte

    def feld_anwenden(self, werte, w, weg):
        for e in werte['E_rem']:
            if self.u1 is not None:
                del self.u1[e]
            if self.su2 is not None:
                del self.su2[e]
        if self.u1 is not None:
            self.u1.update(werte['u1'])
        if self.su2 is not None:
            self.su2.update(werte['su2'])
        if self.rahmen is not None:
            if w >= 0:
                self.rahmen[w] = werte['Rw']
            if weg >= 0:
                del self.rahmen[weg]

    @property
    def mit_feldern(self):
        return self.u1 is not None or self.su2 is not None or self.rahmen is not None

    # --- ein Zug
    def schritt(self):
        if self.kausal and self.rng.random() < self.p_raum:
            z = self.vorschlag_raum()
        else:
            z = self.vorschlag_pachner()
        if z is None:
            return False
        typ, alt, neu, w, tw, weg = z
        self.prop[typ] = self.prop.get(typ, 0) + 1
        N = len(self.slist)
        Nn = N - len(alt) + len(neu)
        if w >= 0:
            self.vt[w] = tw
        alt_t = [self.simp[x] for x in alt]
        d41 = 0
        if self.kausal:
            d41 = sum(1 for s in neu if self.ist41(s)) - sum(1 for s in alt_t if self.ist41(s))
        dN0 = (1 if w >= 0 else 0) - (1 if weg >= 0 else 0)
        N0 = len(self.vstar)
        logA = math.log(N / Nn) - (self.S_geo(N0 + dN0, Nn, self.n41 + d41) - self.S_geo(N0, N, self.n41))
        werte = None
        if self.mit_feldern:
            lw, werte = self.feld_gewicht(alt_t, neu, w, weg)
            logA += lw
            if not hasattr(self, 'lwsum'):
                self.lwsum, self.lwn = {}, {}
            self.lwsum[typ] = self.lwsum.get(typ, 0.0) + lw
            self.lwn[typ] = self.lwn.get(typ, 0) + 1
        if logA < 0.0 and self.rng.random() >= math.exp(logA):
            if w >= 0:
                del self.vt[w]
            return False
        if w >= 0:
            self.nvid = w + 1
            self.vstar[w] = set()
        for x in alt:
            self.del_s(x)
        for s in neu:
            self.add_s(s)
        if weg >= 0:
            assert not self.vstar[weg]
            del self.vstar[weg]
            del self.vt[weg]
        if werte is not None:
            self.feld_anwenden(werte, w, weg)
        self.acc[typ] = self.acc.get(typ, 0) + 1
        return True

    # --- Felder: Start und Waermebad
    def alle_kanten(self):
        E = set()
        for s in self.simp.values():
            E.update(itertools.combinations(s, 2))
        return E

    def alle_dreiecke(self):
        D = set()
        for s in self.simp.values():
            D.update(itertools.combinations(s, 3))
        return D

    def felder_an(self, bu=0.0, bs=0.0, J=0.0):
        E = self.alle_kanten()
        if bu > 0:
            self.bu = bu
            self.u1 = {e: 0.0 for e in E}
        if bs > 0:
            self.bs = bs
            self.su2 = {e: (1.0, 0.0, 0.0, 0.0) for e in E}
        if J > 0:
            self.J = J
            self.rahmen = {v: (1.0, 0.0, 0.0, 0.0) for v in self.vstar}

    def dreiecke_an(self, e):
        a, b = e
        st = self.vstar[a] & self.vstar[b]
        cs = set()
        for sid in st:
            cs.update(self.simp[sid])
        cs.discard(a)
        cs.discard(b)
        return [tuple(sorted((a, b, c))) for c in cs]

    def waermebad(self):
        if self.u1 is not None or self.su2 is not None:
            for e in list(self.u1.keys() if self.u1 is not None else self.su2.keys()):
                Ds = self.dreiecke_an(e)
                if self.u1 is not None:
                    kap, mu = self.u1_lokal(e, Ds, {})
                    self.u1[e] = self.rng.vonmisesvariate(mu, kap) if kap > 1e-12 else ZWEI_PI * self.rng.random()
                if self.su2 is not None:
                    x, V = self.su2_lokal(e, Ds, {})
                    self.su2[e] = qmul(q_waermebad(x, self.rng), qconj(V))
        if self.rahmen is not None:
            R = self.rahmen
            for v in list(R.keys()):
                nb = set()
                for sid in self.vstar[v]:
                    nb.update(self.simp[sid])
                nb.discard(v)
                S = [0.0, 0.0, 0.0, 0.0]
                for n in nb:
                    for m in range(4):
                        S[m] += R[n][m]
                k = math.sqrt(sum(c * c for c in S))
                V = tuple(c / k for c in S) if k > 1e-12 else (1.0, 0.0, 0.0, 0.0)
                R[v] = qmul(V, q_waermebad(self.J * k, self.rng))

    def feld_mess(self):
        out = {}
        if self.u1 is not None or self.su2 is not None:
            D = self.alle_dreiecke()
            if self.u1 is not None:
                out['plak_u1'] = float(np.mean([math.cos(self.u1_F(x, {})) for x in D]))
            if self.su2 is not None:
                out['plak_su2'] = float(np.mean([self.su2_tr(x, {}) for x in D]))
        if self.rahmen is not None:
            R = np.array(list(self.rahmen.values()))
            out['rahmen_m'] = float(np.linalg.norm(R.mean(axis=0)))
            E = self.alle_kanten()
            out['rahmen_e'] = float(np.mean([qdot(self.rahmen[a], self.rahmen[b]) for (a, b) in E]))
        return out

    # --- Pruefung
    def pruefe(self):
        d = self.d
        fac = {}
        for s in self.simp.values():
            assert len(set(s)) == d + 1 and list(s) == sorted(s), s
            for m in range(d + 1):
                f = s[:m] + s[m + 1:]
                fac[f] = fac.get(f, 0) + 1
        assert all(c == 2 for c in fac.values()), 'Facette nicht in genau 2 Simplizes'
        assert sum(len(st) for st in self.vstar.values()) == (d + 1) * len(self.simp)
        for v, st in self.vstar.items():
            assert st, 'Ecke ohne Simplex %d' % v
            for sid in st:
                assert v in self.simp[sid]
        assert len(self.slist) == len(self.simp) == len(self.spos)
        faces = [set() for _ in range(d + 1)]
        for s in self.simp.values():
            for k in range(1, d + 2):
                faces[k - 1].update(itertools.combinations(s, k))
        chi = sum((-1) ** k * len(faces[k]) for k in range(d + 1))
        res = {'chi': chi, 'f': [len(x) for x in faces]}
        if self.kausal:
            n41 = 0
            for s in self.simp.values():
                assert self.ist_kausal(s), s
                n41 += self.ist41(s)
            assert n41 == self.n41
            up, dn = {}, {}
            for s in self.simp.values():
                if not self.ist41(s):
                    continue
                ts = [self.vt[v] for v in s]
                for tb in set(ts):
                    if ts.count(tb) == d:
                        b = tuple(v for v in s if self.vt[v] == tb)
                        a = [v for v in s if self.vt[v] != tb][0]
                        if (self.vt[a] - tb) % self.T == 1:
                            up[b] = up.get(b, 0) + 1
                        else:
                            dn[b] = dn.get(b, 0) + 1
            assert set(up) == set(dn) and all(c == 1 for c in up.values()) and all(c == 1 for c in dn.values())
            chis = []
            for t in range(self.T):
                n = [0] * d
                for k in range(d):
                    n[k] = sum(1 for f in faces[k] if self.vt[f[0]] == t and self.ist_raumartig(f))
                chis.append(sum((-1) ** k * n[k] for k in range(d)))
                assert n[d - 1] == sum(1 for b in up if self.vt[b[0]] == t)
            res['chi_schicht'] = chis
        if self.u1 is not None:
            assert set(self.u1) == faces[1]
        if self.su2 is not None:
            assert set(self.su2) == faces[1]
        if self.rahmen is not None:
            assert set(self.rahmen) == set(self.vstar)
        return res

    # --- Messungen
    def profil(self):
        P = [0] * self.T
        d = self.d
        for s in self.simp.values():
            ts = [self.vt[v] for v in s]
            t0 = ts[0]
            c = ts.count(t0)
            if c == d:
                tb = t0
            elif c == 1:
                tb = ts[1] if ts[1] != t0 else ts[2]
            else:
                continue
            a = [x for x in ts if x != tb][0]
            if (a - tb) % self.T == 1:
                P[tb] += 1
        return P

    def grade(self):
        g = {}
        for v, st in self.vstar.items():
            nb = set()
            for sid in st:
                nb.update(self.simp[sid])
            g[v] = len(nb) - 1
        return g

    def dual(self):
        d = self.d
        sids = list(self.simp.keys())
        idx = {s: i for i, s in enumerate(sids)}
        n = len(sids)
        nb = np.empty((n, d + 1), dtype=np.int64)
        fac = {}
        for s in sids:
            S = self.simp[s]
            i = idx[s]
            for m in range(d + 1):
                f = S[:m] + S[m + 1:]
                o = fac.pop(f, None)
                if o is None:
                    fac[f] = (i, m)
                else:
                    nb[i, m] = o[0]
                    nb[o[0], o[1]] = i
        assert not fac
        return nb, sids

    def orientierung(self, nb, sids):
        """Konsistente Orientierung o[i] in {+1,-1} relativ zur sortierten Eckenfolge (BFS ueber das duale Netz)."""
        d = self.d
        n = len(sids)
        o = np.zeros(n, dtype=np.int64)
        o[0] = 1
        stack = [0]
        bad = 0
        while stack:
            i = stack.pop()
            Si = self.simp[sids[i]]
            for m in range(d + 1):
                j = int(nb[i, m])
                Sj = self.simp[sids[j]]
                f = Si[:m] + Si[m + 1:]
                mj = [x for x in range(d + 1) if Sj[x] not in f][0]
                want = -((-1) ** (m + mj)) * o[i]
                if o[j] == 0:
                    o[j] = want
                    stack.append(j)
                elif o[j] != want:
                    bad += 1
        return o, bad


def schalen(nb, start, rmax):
    n = nb.shape[0]
    dist = np.full(n, -1, dtype=np.int32)
    dist[start] = 0
    front = np.array([start], dtype=np.int64)
    out = [1]
    for r in range(1, rmax + 1):
        cand = np.unique(nb[front].ravel())
        cand = cand[dist[cand] < 0]
        if cand.size == 0:
            break
        dist[cand] = r
        out.append(int(cand.size))
        front = cand
    return out


def rueckkehr(nb, starts, smax):
    n, k = nb.shape
    m = len(starts)
    P = np.zeros((n, m))
    P[starts, np.arange(m)] = 1.0
    R = np.empty(smax + 1)
    R[0] = 1.0
    for s in range(1, smax + 1):
        P = 0.5 * P + (0.5 / k) * P[nb].sum(axis=1)
        R[s] = P[starts, np.arange(m)].mean()
    return R


def ds_kurve(P):
    out = []
    for s in range(2, len(P) - 1):
        if P[s + 1] > 0 and P[s - 1] > 0:
            out.append((s, -2.0 * (math.log(P[s + 1]) - math.log(P[s - 1])) / (math.log(s + 1) - math.log(s - 1))))
    return out


def solid(a, b, c):
    num = a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0])
    den = 1.0 + (a[0] * b[0] + a[1] * b[1] + a[2] * b[2]) + (b[0] * c[0] + b[1] * c[1] + b[2] * c[2]) \
        + (c[0] * a[0] + c[1] * a[1] + c[2] * a[2])
    return 2.0 * math.atan2(num, den)


def zachse(q):
    w, x, y, z = q
    return (2 * (x * z + w * y), 2 * (y * z - w * x), 1 - 2 * (x * x + y * y))


# ------------------------------------------------------------------------------------------------ Lauf
class Mess:
    def __init__(self):
        self.reihe = []          # je Messsweep: kleine Kennzahlen
        self.P = None            # Summe Rueckkehrwahrscheinlichkeit
        self.nP = 0
        self.sch = None          # Summe Schalen
        self.nsch = 0
        self.gradhist = np.zeros(1, dtype=np.int64)
        self.sp_aktiv = {}       # Ecke -> erster Sweep
        self.sp_zuletzt = set()
        self.sp_leben = []       # abgeschlossene Lebensdauern (Sweeps)
        self.sp_n = []           # Zahl Superpunkte je Messung
        self.ladung = []         # (Q, Igel) je Superpunkt-Messung
        self.ladung_normal = []  # dieselben Groessen an zufaelligen gewoehnlichen Ecken (Vergleich)
        self.orient_bad = 0


def superpunkt_windung(net, mess, sps, orient):
    """U(1)-Ladung (DeGrand-Toussaint durch die raeumliche Huelle) und Rahmen-Igelzahl um Ecken in sps (nur cdt4)."""
    nb, sids, o = orient
    idx = {s: i for i, s in enumerate(sids)}
    out = []
    for v in sps:
        tb = net.vt[v]
        tris = []
        for sid in net.vstar[v]:
            S = net.simp[sid]
            ts = [net.vt[x] for x in S]
            if ts.count(tb) != 4:
                continue
            p = [x for x in S if net.vt[x] != tb][0]
            if (net.vt[p] - tb) % net.T != 1:
                continue
            B = tuple(x for x in S if x != p)
            mp = S.index(p)
            epsB = ((-1) ** mp) * int(o[idx[sid]])
            mv = B.index(v)
            sg = ((-1) ** mv) * epsB
            tris.append((sg, B[:mv] + B[mv + 1:]))
        Q = Ig = None
        if net.u1 is not None:
            tot = 0.0
            for sg, D in tris:
                tot += wrap(sg * net.u1_F(D, {}))
            Q = -tot / ZWEI_PI
        if net.rahmen is not None:
            tot = 0.0
            for sg, D in tris:
                a, b, c = (zachse(net.rahmen[x]) for x in D)
                tot += sg * solid(a, b, c)
            Ig = tot / (4.0 * math.pi)
        out.append((Q, Ig, len(tris)))
    return out


def messen(net, mess, args, voll):
    rec = {'sweep': net.sweep, 'N': len(net.slist), 'N0': len(net.vstar), 'k4': net.k4, 'k0': net.k0}
    if net.kausal:
        rec['N41'] = net.n41
        rec['profil'] = net.profil()
    g = net.grade()
    gv = np.fromiter(g.values(), dtype=np.int64)
    rec['grad_mittel'] = float(gv.mean())
    rec['grad_max'] = int(gv.max())
    h = np.bincount(gv)
    if h.size > mess.gradhist.size:
        mess.gradhist = np.pad(mess.gradhist, (0, h.size - mess.gradhist.size))
    mess.gradhist[:h.size] += h
    schwelle = 5.0 * gv.mean()
    sps = [v for v, x in g.items() if x > schwelle]
    rec['n_sp'] = len(sps)
    cur = set(sps)
    for v in list(mess.sp_aktiv):
        if v not in cur:
            mess.sp_leben.append(net.sweep - mess.sp_aktiv.pop(v))
    for v in cur:
        if v not in mess.sp_aktiv:
            mess.sp_aktiv[v] = net.sweep
    rec.update(net.feld_mess() if voll else {})
    orient = None
    if voll:
        nb, sids = net.dual()
        n = nb.shape[0]
        starts = net.nrng.choice(n, size=min(args.ds_starts, n), replace=False)
        P = rueckkehr(nb, starts, args.ds_smax)
        if mess.P is None:
            mess.P = np.zeros_like(P)
        mess.P += P
        mess.nP += 1
        for st in starts[:args.sch_starts]:
            sc = np.array(schalen(nb, int(st), args.sch_rmax), dtype=float)
            if mess.sch is None:
                mess.sch = np.zeros(args.sch_rmax + 1)
            if sc.size > mess.sch.size:
                raise ValueError('sch_rmax groesser als im ersten Abschnitt: --neu_mess verwenden')
            mess.sch[:sc.size] += sc
            mess.nsch += 1
        if net.d == 4 and net.kausal and (net.u1 is not None or net.rahmen is not None):
            o, bad = net.orientierung(nb, sids)
            mess.orient_bad += bad
            orient = (nb, sids, o)
            if sps:
                for x in superpunkt_windung(net, mess, sps, orient):
                    mess.ladung.append(x)
            verts = list(net.vstar.keys())
            normal = [verts[i] for i in net.nrng.choice(len(verts), size=min(8, len(verts)), replace=False)
                      if g[verts[i]] <= schwelle]
            for x in superpunkt_windung(net, mess, normal, orient):
                mess.ladung_normal.append(x)
    mess.reihe.append(rec)


def baue(args):
    if args.modus == 'cdt2':
        sims, vt = ring2(args.L0, args.T)
        net = Netz(2, args.T, True, args.seed, sims, vt)
        info = {'start': 'Ringe', 'L0': args.L0}
    else:
        tets, nV, ntz, nsub = v_netz(args.L)
        sims, vt = prisma4(tets, nV, args.T)
        net = Netz(4, args.T, args.modus == 'cdt4', args.seed, sims, vt)
        info = {'start': 'V', 'L': args.L, 'tets_je_zelle': ntz, 'ecken_je_zelle': nsub, 'tets_schicht': len(tets),
                'ecken_schicht': nV}
    net.k0, net.k4, net.Delta, net.eps = args.k0, args.k4, args.Delta, args.eps
    net.Nz = args.Nz if args.Nz > 0 else len(net.slist)
    net.felder_an(args.bu, args.bs, args.J)
    net.mess = Mess()
    net.info = info
    return net


def zusammenfassung(net, args, pruef, t_lauf):
    m = net.mess
    out = {'karte': 'NETZ-DYN-1', 'modus': args.modus, 'args': vars(args), 'info': net.info, 'sweep': net.sweep,
           'k0': net.k0, 'k4': net.k4, 'Delta': net.Delta, 'eps': net.eps, 'Nz': net.Nz,
           'bu': net.bu, 'bs': net.bs, 'J': net.J,
           'N': len(net.slist), 'N0': len(net.vstar), 'N41': net.n41,
           'vorschlaege': net.prop, 'angenommen': net.acc, 'pruefung': pruef, 'laufzeit_s': t_lauf,
           'python': platform.python_version(), 'numpy': np.__version__}
    rs = [r for r in m.reihe if r['sweep'] > args.therm]
    out['n_mess'] = len(rs)
    if rs:
        for key in ('N', 'N0', 'N41', 'grad_mittel', 'grad_max', 'n_sp', 'plak_u1', 'plak_su2', 'rahmen_m', 'rahmen_e'):
            vals = [r[key] for r in rs if key in r]
            if vals:
                out['mittel_' + key] = float(np.mean(vals))
                out['streu_' + key] = float(np.std(vals))
        if 'profil' in rs[0]:
            Pr = np.array([r['profil'] for r in rs], dtype=float)
            out['profil_mittel'] = Pr.mean(axis=0).tolist()
            # relative Streuung je Schicht und Ungleichheit (max/mittel) je Konfiguration
            out['profil_relstreu'] = float((Pr.std(axis=1) / np.maximum(Pr.mean(axis=1), 1e-9)).mean())
            out['profil_max_durch_mittel'] = float((Pr.max(axis=1) / np.maximum(Pr.mean(axis=1), 1e-9)).mean())
    if m.P is not None:
        P = m.P / m.nP
        out['P_rueck'] = P.tolist()
        out['ds'] = ds_kurve(P)
        out['n_P'] = m.nP
    if m.sch is not None:
        sch = m.sch / max(m.nsch, 1)
        out['schalen'] = sch.tolist()
        loc = []
        for r in range(2, len(sch) - 1):
            if sch[r + 1] > 0 and sch[r - 1] > 0:
                loc.append((r, 1.0 + (math.log(sch[r + 1]) - math.log(sch[r - 1])) / (math.log(r + 1) - math.log(r - 1))))
        out['dH_lokal'] = loc
        out['n_schalen'] = m.nsch
    out['gradhist'] = m.gradhist.tolist()
    leben = list(m.sp_leben) + [net.sweep - s for s in m.sp_aktiv.values()]
    out['sp_leben'] = {'n': len(leben), 'max': int(max(leben)) if leben else 0,
                       'mittel': float(np.mean(leben)) if leben else 0.0,
                       'n_ueber_10': int(sum(1 for x in leben if x > 10)), 'aktiv_am_ende': len(m.sp_aktiv)}
    for key, L in (('ladung_sp', m.ladung), ('ladung_normal', m.ladung_normal)):
        if L:
            Q = [x[0] for x in L if x[0] is not None]
            I = [x[1] for x in L if x[1] is not None]
            d = {'n': len(L)}
            if Q:
                d.update({'Q_mittel': float(np.mean(Q)), 'Q_betrag': float(np.mean(np.abs(Q))),
                          'Q_quadrat': float(np.mean(np.square(Q))),
                          'Q_ganzzahl_abw': float(np.max(np.abs(np.array(Q) - np.rint(Q))))})
            if I:
                d.update({'Igel_mittel': float(np.mean(I)), 'Igel_betrag': float(np.mean(np.abs(I))),
                          'Igel_ganzzahl_abw': float(np.max(np.abs(np.array(I) - np.rint(I))))})
            out[key] = d
    out['orient_fehler'] = m.orient_bad
    if hasattr(net, 'lwsum'):
        out['feld_logw_mittel'] = {k: net.lwsum[k] / net.lwn[k] for k in net.lwsum}
        out['feld_logw_n'] = dict(net.lwn)
    out['k0_ende'] = net.k0
    out['reihe_kurz'] = [{k: r[k] for k in r if k != 'profil'} for r in m.reihe[-40:]]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--modus', choices=['cdt2', 'cdt4', 'dt4'], required=True)
    ap.add_argument('--T', type=int, default=4)
    ap.add_argument('--L', type=int, default=2)
    ap.add_argument('--L0', type=int, default=16)
    ap.add_argument('--Nz', type=int, default=0)
    ap.add_argument('--k0', type=float, default=2.2)
    ap.add_argument('--k4', type=float, default=1.0)
    ap.add_argument('--Delta', type=float, default=0.6)
    ap.add_argument('--eps', type=float, default=2e-4)
    ap.add_argument('--bu', type=float, default=0.0)
    ap.add_argument('--bs', type=float, default=0.0)
    ap.add_argument('--J', type=float, default=0.0)
    ap.add_argument('--therm', type=int, default=100)
    ap.add_argument('--sweeps', type=int, default=1000)
    ap.add_argument('--voll_int', type=int, default=10)
    ap.add_argument('--grad_int', type=int, default=1)
    ap.add_argument('--pruef_int', type=int, default=50)
    ap.add_argument('--ds_starts', type=int, default=24)
    ap.add_argument('--ds_smax', type=int, default=400)
    ap.add_argument('--sch_starts', type=int, default=8)
    ap.add_argument('--sch_rmax', type=int, default=60)
    ap.add_argument('--zeit', type=float, default=540.0)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--aus', required=True)
    ap.add_argument('--fort', default='')
    ap.add_argument('--tune_ab', type=int, default=-1, help='k4-Nachfuehrung bis zu diesem Sweep (Standard: therm)')
    ap.add_argument('--nur_start', action='store_true', help='nur Messung am Startnetz (Kontrolle der Messmethode)')
    ap.add_argument('--n0_anteil', type=float, default=0.0, help='Ziel N0/N4 fuer k0-Nachfuehrung (0 = aus)')
    ap.add_argument('--k0_rate', type=float, default=2e-4)
    ap.add_argument('--neu_kopplung', action='store_true', help='bei --fort: Kopplungen aus den Argumenten setzen')
    ap.add_argument('--neu_mess', action='store_true', help='bei --fort: Messreihen neu beginnen')
    ap.add_argument('--felder_aus', action='store_true', help='bei --fort: Felder entfernen, nur Geometrie weiter')
    args = ap.parse_args()
    t0 = time.time()
    if args.fort and os.path.exists(args.fort):
        with open(args.fort, 'rb') as f:
            net = pickle.load(f)
        print('fortgesetzt bei Sweep %d, N=%d' % (net.sweep, len(net.slist)), flush=True)
        if args.neu_kopplung:
            # Startunabhaengigkeit: fremden Endzustand mit neuen Kopplungen weiterfuehren, Zaehlung neu
            net.k0, net.Delta, net.k4 = args.k0, args.Delta, args.k4
            net.sweep = 0
            net.mess = Mess()
            net.prop, net.acc = {}, {}
            net.info = dict(net.info, start_aus=args.fort)
            print('neue Kopplungen k0=%.3f Delta=%.3f k4=%.3f, Zaehlung neu' % (net.k0, net.Delta, net.k4), flush=True)
        if args.felder_aus:
            net.u1 = net.su2 = net.rahmen = None
            net.bu = net.bs = net.J = 0.0
            if hasattr(net, 'lwsum'):
                del net.lwsum, net.lwn
            print('Felder entfernt (Geometrie bleibt)', flush=True)
        if args.neu_mess:
            # Messung neu beginnen (z. B. groesseres sch_rmax), Geometrie und Sweepzaehler bleiben
            net.mess = Mess()
            print('Messreihen neu ab Sweep %d' % net.sweep, flush=True)
    else:
        net = baue(args)
        print('Start: N=%d N0=%d N41=%d info=%s' % (len(net.slist), len(net.vstar), net.n41, net.info), flush=True)
    pruef = [net.pruefe()]
    print('Pruefung Start:', pruef[-1], flush=True)
    if args.nur_start:
        args.therm = -1
        messen(net, net.mess, args, True)
        out = zusammenfassung(net, args, pruef, time.time() - t0)
        with open(args.aus + '.json.neu', 'w') as f:
            json.dump(out, f)
        os.replace(args.aus + '.json.neu', args.aus + '.json')
        print('nur Startmessung', flush=True)
        return
    tune_bis = args.therm if args.tune_ab < 0 else args.tune_ab
    while net.sweep < args.sweeps and time.time() - t0 < args.zeit:
        n = len(net.slist)
        Nsum = 0.0
        for i in range(n):
            net.schritt()
            if i % 64 == 0:
                Nsum += len(net.slist)
        if net.mit_feldern:
            net.waermebad()
        net.sweep += 1
        Nbar = Nsum / ((n + 63) // 64)
        if net.sweep <= tune_bis:
            net.k4 += net.eps * (Nbar - net.Nz)
            if args.n0_anteil > 0:
                # k0-Nachfuehrung auf ein Ziel N0/N4 (nur Thermalisierung; fuer den Feldvergleich bei gleichem N0/N4)
                net.k0 += args.k0_rate * (args.n0_anteil - len(net.vstar) / len(net.slist)) * len(net.slist)
        if net.sweep % args.grad_int == 0:
            voll = net.sweep > args.therm and net.sweep % args.voll_int == 0
            messen(net, net.mess, args, voll)
        if net.sweep % args.pruef_int == 0:
            pruef.append(net.pruefe())
        if net.sweep % 10 == 0:
            r = net.mess.reihe[-1] if net.mess.reihe else {}
            print('sweep %d N=%d N0=%d N41=%d k0=%.3f k4=%.4f gmax=%s nsp=%s t=%.0f' % (
                net.sweep, len(net.slist), len(net.vstar), net.n41, net.k0, net.k4, r.get('grad_max'), r.get('n_sp'),
                time.time() - t0), flush=True)
    pruef.append(net.pruefe())
    t_lauf = time.time() - t0
    out = zusammenfassung(net, args, pruef[-3:], t_lauf)
    tmpj = args.aus + '.json.neu'
    with open(tmpj, 'w') as f:
        json.dump(out, f)
    os.replace(tmpj, args.aus + '.json')
    if args.fort:
        tmpc = args.fort + '.neu'
        with open(tmpc, 'wb') as f:
            pickle.dump(net, f, protocol=pickle.HIGHEST_PROTOCOL)
        os.replace(tmpc, args.fort)
        print('Zwischenstand %s (%.1f MB)' % (args.fort, os.path.getsize(args.fort) / 1e6), flush=True)
    print('fertig sweep=%d N=%d N0=%d t=%.0f s; Zuege %s; angenommen %s' % (
        net.sweep, len(net.slist), len(net.vstar), t_lauf, net.prop, net.acc), flush=True)


if __name__ == '__main__':
    main()
