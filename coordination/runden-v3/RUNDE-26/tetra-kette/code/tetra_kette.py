#!/usr/bin/env python3
"""TETRA-KETTE (Runde 26). Code-Agent fuer die Leitung claude-primary, 03.10.2026.
Karte: RUNDE-26/tetra-kette/KARTE.md; Plan: RUNDE-26/tetra-kette/PLAN.md.

Kette aus M flaechenverbundenen Tetraedern (Boerdijk-Coxeter-Helix, Kantenlaenge L = 1): Ecken v_0 .. v_(M+2),
Staebe (i, i+1), (i, i+2), (i, i+3), zusammen 3 M + 3. Jeder Stab ist elastisch und von Natur aus gerade (B = 1, L = 1,
Ks = 25600), N Segmente, an beiden Enden in starren Verbindern (Lage X, Drehvektor r, Drehung exp(schief(r)))
eingespannt. Keine Torsion.
Energieformen wie TETRA-STAB (RUNDE-24/tetra-stab/code/tetra_stab.py):
  Dehnung (Ks/2) Summe (|e| - l0)^2 / l0; Biegung (B/l0) Summe (1 - t_i . t_(i+1)); Einspannung (2B/l0)(1 -+ d . t).
Neu gegen TETRA-STAB: alle Staebe gebuendelt (torch.func.vmap), exakte Hesse-Matrix je Stab (torch.func.hessian), global
dicht zusammengesetzt; gedaempfter Newton ab dem geraden Bezugszustand.
Einspannrichtung im Bezug: gerade Kantenrichtung, um alpha zur Mitte des Tetraeders mit dem kleinsten k geneigt, das den
Stab enthaelt (alpha_0 fuer alle Staebe, alpha_d fuer den Defektstab (v_0, v_1)). Ein Verbinder ist fest (Lage, Drehung).
Kraft des Stabs auf den Verbinder: -dE_Stab/dX; Moment: -d x dE_Stab/dd (d = aktuelle Einspannrichtung).

Aufruf: python tetra_kette.py <name> <M> <N> <alpha_d_grad> <alpha_0_grad> <fest (-1 = letzter)> <hesse 0/1> <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import scipy.linalg as sla  # noqa: E402
import torch  # noqa: E402
from torch.func import grad, hessian, vmap  # noqa: E402

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
B, L, KS = 1.0, 1.0, 25600.0
ORDNUNG_EXP = 24          # Potenzreihe fuer exp(schief(r)); fuer |r| < 1 ist der Abbruchfehler < 1e-24


def tetrahelix(M):
    """Boerdijk-Coxeter-Helix mit Kantenlaenge 1: v_n = (rho cos n th, rho sin n th, n h),
    th = arccos(-2/3), rho = 3 sqrt(3)/10, h = 1/sqrt(10)."""
    th = math.acos(-2.0 / 3.0)
    rho = 3.0 * math.sqrt(3.0) / 10.0
    h = 1.0 / math.sqrt(10.0)
    n = np.arange(M + 3, dtype=float)
    return np.stack([rho * np.cos(n * th), rho * np.sin(n * th), n * h], 1)


def staebe_der_kette(M):
    nv = M + 3
    return [(i, i + d) for i in range(nv) for d in (1, 2, 3) if i + d < nv]


def tetra_kleinstes_k(i, j):
    """Kleinstes k mit i, j in {k, ..., k+3} (eindeutige Zuordnung Stab -> Tetraeder)."""
    return max(0, j - 3)


def schief(v):
    z = torch.zeros_like(v[0])
    return torch.stack([torch.stack([z, -v[2], v[1]]), torch.stack([v[2], z, -v[0]]),
                        torch.stack([-v[1], v[0], z])])


def drehung(r):
    """exp(schief(r)) als Potenzreihe (Horner), glatt und vmap-/jacfwd-tauglich."""
    K = schief(r)
    eins = torch.eye(3, dtype=r.dtype)
    S = eins
    for n in range(ORDNUNG_EXP, 0, -1):
        S = eins + (K @ S) / n
    return S


def energie_kern(innen, Xi, Xj, di, dj, l0):
    y = torch.cat([Xi[None], innen, Xj[None]], 0)
    e = y[1:] - y[:-1]
    le = torch.sqrt((e * e).sum(1))
    t = e / le[:, None]
    es = 0.5 * KS * ((le - l0) ** 2).sum() / l0
    eb = (B / l0) * (1.0 - (t[:-1] * t[1:]).sum(1)).sum()
    ec = (2.0 * B / l0) * ((1.0 - (di * t[0]).sum()) + (1.0 + (dj * t[-1]).sum()))
    return es + eb + ec


class Modell:
    def __init__(self, M, N, alpha_d, alpha_0, fest):
        self.M, self.N = M, N
        self.l0 = L / N
        self.P = tetrahelix(M)
        self.nv = M + 3
        self.fest = fest if fest >= 0 else self.nv - 1
        self.staebe = staebe_der_kette(M)
        self.R = len(self.staebe)
        self.kt = [tetra_kleinstes_k(i, j) for (i, j) in self.staebe]
        d0i, d0j = [], []
        for m, (i, j) in enumerate(self.staebe):
            k = self.kt[m]
            c = self.P[k:k + 4].mean(0)
            al = alpha_d if (i, j) == (0, 1) else alpha_0
            for (u, v, ziel) in ((i, j, d0i), (j, i, d0j)):
                e = (self.P[v] - self.P[u]) / np.linalg.norm(self.P[v] - self.P[u])
                nv = (c - self.P[u]) - np.dot(c - self.P[u], e) * e
                nv /= np.linalg.norm(nv)
                ziel.append(math.cos(al) * e + math.sin(al) * nv)
        self.D0I = torch.tensor(np.array(d0i))
        self.D0J = torch.tensor(np.array(d0j))
        self.nin = 3 * (N - 1)
        self.nloc = self.nin + 12
        self.frei = [q for q in range(self.nv) if q != self.fest]
        self.basis = {q: self.R * self.nin + 6 * a for a, q in enumerate(self.frei)}
        self.nx = self.R * self.nin + 6 * len(self.frei)
        self.konst = torch.tensor(np.concatenate([self.P[self.fest], np.zeros(3)]))
        gidx = np.full((self.R, self.nloc), -1, dtype=np.int64)
        gfull = np.zeros((self.R, self.nloc), dtype=np.int64)
        for m, (i, j) in enumerate(self.staebe):
            gidx[m, :self.nin] = m * self.nin + np.arange(self.nin)
            gfull[m, :self.nin] = gidx[m, :self.nin]
            for s, q in ((0, i), (1, j)):
                sl = slice(self.nin + 6 * s, self.nin + 6 * s + 6)
                if q == self.fest:
                    gfull[m, sl] = self.nx + np.arange(6)
                else:
                    gidx[m, sl] = self.basis[q] + np.arange(6)
                    gfull[m, sl] = gidx[m, sl]
        self.gidx = gidx
        self.gfull = torch.tensor(gfull)
        self.f_E = vmap(self._stab)
        self.f_G = vmap(grad(self._stab))
        self.f_H = vmap(hessian(self._stab))

    def _stab(self, z, d0i, d0j):
        innen = z[:self.nin].reshape(self.N - 1, 3)
        o = self.nin
        Xi, ri, Xj, rj = z[o:o + 3], z[o + 3:o + 6], z[o + 6:o + 9], z[o + 9:o + 12]
        di = drehung(ri) @ d0i
        dj = drehung(rj) @ d0j
        return energie_kern(innen, Xi, Xj, di, dj, self.l0)

    def startvektor(self):
        teile = []
        s = np.linspace(0.0, 1.0, self.N + 1)[1:-1]
        for (i, j) in self.staebe:
            teile.append((self.P[i][None, :] + s[:, None] * (self.P[j] - self.P[i])[None, :]).ravel())
        for q in self.frei:
            teile.append(np.concatenate([self.P[q], np.zeros(3)]))
        return np.concatenate(teile)

    def lokal(self, x):
        xf = torch.cat([torch.as_tensor(x, dtype=torch.float64), self.konst])
        return xf[self.gfull]

    def energie(self, x):
        return float(self.f_E(self.lokal(x), self.D0I, self.D0J).sum())

    def gradient(self, x):
        G = self.f_G(self.lokal(x), self.D0I, self.D0J).numpy()
        g = np.zeros(self.nx)
        maske = self.gidx >= 0
        np.add.at(g, self.gidx[maske], G[maske])
        return g

    def hesse(self, x):
        Hl = self.f_H(self.lokal(x), self.D0I, self.D0J).numpy()
        H = np.zeros((self.nx, self.nx))
        for m in range(self.R):
            ok = self.gidx[m] >= 0
            ii = self.gidx[m][ok]
            H[np.ix_(ii, ii)] += Hl[m][np.ix_(ok, ok)]
        return 0.5 * (H + H.T)


def newton(mod, x0, maxit=80):
    """Gedaempfter Newton mit exakter Hesse-Matrix (Cholesky, bei Bedarf verschoben) und Armijo-Rueckschritt."""
    x = x0.copy()
    E = mod.energie(x)
    g = mod.gradient(x)
    verlauf = []
    meldung = "maxit"
    for it in range(maxit):
        gn = float(np.linalg.norm(g))
        if gn < 1e-13:
            verlauf.append([it, E, gn, 0.0, 0.0])
            meldung = "gradnorm < 1e-13"
            break
        H = mod.hesse(x)
        mu = 0.0
        dmax = float(np.abs(np.diag(H)).max())
        while True:
            try:
                cf = sla.cho_factor(H + mu * np.eye(mod.nx), lower=True)
                break
            except np.linalg.LinAlgError:
                mu = 1e-8 * dmax if mu == 0.0 else 10.0 * mu
        p = -sla.cho_solve(cf, g)
        gp = float(g @ p)
        s = 1.0
        while True:
            xn = x + s * p
            En = mod.energie(xn)
            if En <= E + 1e-4 * s * gp + 1e-13 * abs(E):
                break
            s *= 0.5
            if s < 1e-10:
                break
        verlauf.append([it, E, gn, mu, s])
        if s < 1e-10:
            meldung = "Liniensuche ohne Abstieg"
            break
        gnn = mod.gradient(xn)
        if float(np.linalg.norm(gnn)) >= gn and gn < 1e-8:
            meldung = "Rundungsboden (kein Fortschritt mehr)"
            break
        x, E, g = xn, En, gnn
    return x, verlauf, meldung


def lasten(mod, x):
    """Kraft und Moment jedes Stabs auf seine beiden Verbinder, gebuendelt."""
    Z = mod.lokal(x)
    o = mod.nin
    innen = Z[:, :o].reshape(mod.R, mod.N - 1, 3)
    Xi, ri, Xj, rj = Z[:, o:o + 3], Z[:, o + 3:o + 6], Z[:, o + 6:o + 9], Z[:, o + 9:o + 12]
    di = torch.einsum("rab,rb->ra", vmap(drehung)(ri), mod.D0I)
    dj = torch.einsum("rab,rb->ra", vmap(drehung)(rj), mod.D0J)
    l0 = mod.l0

    def kern(a, b, c, d, e):
        return energie_kern(a, b, c, d, e, l0)

    gXi, gXj, gdi, gdj = vmap(grad(kern, argnums=(1, 2, 3, 4)))(innen, Xi, Xj, di, dj)
    Fi, Fj = (-gXi).numpy(), (-gXj).numpy()
    Ti = (-torch.linalg.cross(di, gdi)).numpy()
    Tj = (-torch.linalg.cross(dj, gdj)).numpy()
    Xin, Xjn, innen_n = Xi.numpy(), Xj.numpy(), innen.numpy()
    staebe = []
    for m, (i, j) in enumerate(mod.staebe):
        sehne = Xjn[m] - Xin[m]
        a = float(np.linalg.norm(sehne))
        eh = sehne / a
        rel = innen_n[m] - Xin[m][None, :]
        quer = rel - (rel @ eh)[:, None] * eh[None, :]
        staebe.append({"i": i, "j": j, "familie": j - i, "k_eindeutig": mod.kt[m], "a": a,
                       "stich": float(np.linalg.norm(quer, axis=1).max()),
                       "F_i": Fi[m].tolist(), "F_j": Fj[m].tolist(), "tau_i": Ti[m].tolist(), "tau_j": Tj[m].tolist(),
                       "F_i_axial": float(Fi[m] @ eh), "F_j_axial": float(Fj[m] @ (-eh)),
                       "F_i_betrag": float(np.linalg.norm(Fi[m])), "F_j_betrag": float(np.linalg.norm(Fj[m])),
                       "tau_i_betrag": float(np.linalg.norm(Ti[m])), "tau_j_betrag": float(np.linalg.norm(Tj[m]))})
    verbinder = []
    for q in range(mod.nv):
        F = np.zeros(3)
        T = np.zeros(3)
        for m, (i, j) in enumerate(mod.staebe):
            if q == i:
                F += Fi[m]
                T += Ti[m]
            elif q == j:
                F += Fj[m]
                T += Tj[m]
        verbinder.append({"q": q, "fest": q == mod.fest, "F_summe": float(np.linalg.norm(F)),
                          "tau_summe": float(np.linalg.norm(T))})
    return staebe, verbinder


def je_tetraeder(mod, staebe):
    """Groesstes Endmoment und groesste Kraft je Tetraeder k: eindeutig (kleinstes k) und nach Mitgliedschaft."""
    aus = []
    for k in range(mod.M):
        eind = [s for s in staebe if s["k_eindeutig"] == k]
        mitg = [s for s in staebe if s["i"] >= k and s["j"] <= k + 3]

        def tmax(lst):
            return max(max(s["tau_i_betrag"], s["tau_j_betrag"]) for s in lst)

        def fmax(lst):
            return max(max(s["F_i_betrag"], s["F_j_betrag"]) for s in lst)

        aus.append({"k": k, "T_eind": tmax(eind), "F_eind": fmax(eind), "T_mitg": tmax(mitg), "F_mitg": fmax(mitg),
                    "staebe_eind": [[s["i"], s["j"]] for s in eind],
                    "axial_eind": [s["F_i_axial"] for s in eind]})
    ecken = []
    for q in range(mod.nv):
        enden = [(s["tau_i_betrag"], s["F_i_betrag"]) for s in staebe if s["i"] == q] + \
                [(s["tau_j_betrag"], s["F_j_betrag"]) for s in staebe if s["j"] == q]
        ecken.append({"q": q, "T_ecke": max(e[0] for e in enden), "F_ecke": max(e[1] for e in enden)})
    return aus, ecken


def geometrie_pruefen(mod):
    P = mod.P
    kanten = [abs(float(np.linalg.norm(P[j] - P[i])) - 1.0) for (i, j) in mod.staebe]
    vol_soll = 1.0 / (6.0 * math.sqrt(2.0))
    vol = [abs(float(np.dot(P[k + 1] - P[k], np.cross(P[k + 2] - P[k], P[k + 3] - P[k])))) / 6.0 for k in range(mod.M)]
    nicht = [float(np.linalg.norm(P[i + 4] - P[i])) for i in range(mod.nv - 4)]
    return {"kante_max_abw": max(kanten), "volumen_max_abw_rel": max(abs(v - vol_soll) / vol_soll for v in vol),
            "kleinster_abstand_nichtkante_i_i4": min(nicht) if nicht else None, "anzahl_staebe": mod.R}


def main():
    name, M, N, agd, ag0, fest, hesse_an, pfad = (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]),
                                                    float(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), sys.argv[8])
    t0 = time.time()
    mod = Modell(M, N, math.radians(agd), math.radians(ag0), fest)
    geo = geometrie_pruefen(mod)
    x, verlauf, meldung = newton(mod, mod.startvektor())
    gn = float(np.linalg.norm(mod.gradient(x)))
    staebe, verbinder = lasten(mod, x)
    tet, ecken = je_tetraeder(mod, staebe)
    out = {"name": name, "M": M, "N": N, "alpha_d_grad": agd, "alpha_0_grad": ag0, "fest": mod.fest, "B": B, "L": L,
           "Ks": KS, "nx": mod.nx, "geometrie": geo, "energie": mod.energie(x), "gradnorm": gn,
           "newton_verlauf": verlauf, "newton_meldung": meldung, "staebe": staebe, "verbinder": verbinder,
           "tetraeder": tet, "ecken": ecken}
    if hesse_an:
        ev = np.linalg.eigvalsh(mod.hesse(x))
        out["hesse_kleinste"] = [float(v) for v in ev[:8]]
    out["sek"] = time.time() - t0
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    taus = [max(s["tau_i_betrag"], s["tau_j_betrag"]) for s in staebe]
    Fs = [max(s["F_i_betrag"], s["F_j_betrag"]) for s in staebe]
    frei = [v for v in verbinder if not v["fest"]]
    print(f"{name}: M {M}, N {N}, alpha_d {agd}, alpha_0 {ag0}, fest v_{mod.fest}, nx {mod.nx}, "
          f"Newton {len(verlauf)} ({meldung}), |grad| {gn:.1e}, tau max {max(taus):.6e}, |F| max {max(Fs):.6e}, "
          f"Rest frei F {max(v['F_summe'] for v in frei):.1e} tau {max(v['tau_summe'] for v in frei):.1e}, "
          f"Kante {geo['kante_max_abw']:.1e}, {out['sek']:.1f} s", flush=True)
    print("T_eind: " + " ".join(f"{t['T_eind']:.3e}" for t in tet), flush=True)


if __name__ == "__main__":
    main()
