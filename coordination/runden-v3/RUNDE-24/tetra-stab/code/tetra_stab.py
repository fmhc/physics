#!/usr/bin/env python3
"""TETRA-STAB (Runde 24), Leitung claude-primary, 03.10.2026. Karte: RUNDE-24/tetra-stab/KARTE.md.

Tetraeder aus sechs elastischen, von Natur aus geraden Staeben (Biegesteifigkeit B = 1, Laenge L = 1), an vier starren
Verbindern eingespannt. Die Einspannrichtungen sind gegen die Kanten des regulaeren Tetraeders um alpha zur Mitte geneigt.
Verbinder A ist fest (Lage und Drehung), die anderen drei sind frei. Keine Torsion.
Diskret: N Segmente je Stab, Laenge l0 = L/N; Biegung (B/l0) Summe (1 - t_i . t_(i+1)) an inneren Knoten,
(2B/l0)(1 - cos) an den Einspannknoten (halbe Voronoi-Laenge); Dehnung (Ks/2) Summe (|e| - l0)^2 / l0 mit
Ks = 4 L^2/r^2 B = 25600 (Knicklicht 20 cm, 5 mm).
Kraft des Stabs auf den Verbinder: -dE_Stab/dX; Moment: -d x dE_Stab/dd (d = Einspannrichtung).

Aufruf: python tetra_stab.py <name> <N> <alpha_grad> <alpha_AB_grad> <hesse 0/1> <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402
from scipy.optimize import minimize  # noqa: E402

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
B, L, KS = 1.0, 1.0, 25600.0
ECKEN = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=float)  # A, B, C, D
STAEBE = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]                           # AB AC AD BC BD CD
NAMEN = ["AB", "AC", "AD", "BC", "BD", "CD"]


def schief(v):
    z = torch.zeros((), dtype=v.dtype)
    return torch.stack([torch.stack([z, -v[2], v[1]]), torch.stack([v[2], z, -v[0]]), torch.stack([-v[1], v[0], z])])


class Modell:
    def __init__(self, N, alpha, alpha_ab):
        self.N = N
        self.l0 = L / N
        self.alpha = [alpha_ab if m == 0 else alpha for m in range(6)]
        a_soll = (L / alpha) * math.sin(alpha) if alpha > 0 else L
        P = ECKEN / np.linalg.norm(ECKEN[0] - ECKEN[1]) * a_soll                         # Kante a_soll, Mitte 0
        self.P = P
        # Referenz-Einspannrichtungen d0[j][m] (vom Verbinder j in den Stab m hinein)
        self.d0 = {}
        for m, (j, k) in enumerate(STAEBE):
            for (u, v) in ((j, k), (k, j)):
                e = (P[v] - P[u]) / np.linalg.norm(P[v] - P[u])
                n = -P[u] - np.dot(-P[u], e) * e
                n /= np.linalg.norm(n)
                al = self.alpha[m]
                self.d0[(u, m)] = math.cos(al) * e + math.sin(al) * n
        # Startwerte: gerade Staebe zwischen den Ecken
        self.innen0 = []
        for (j, k) in STAEBE:
            s = np.linspace(0.0, 1.0, N + 1)[1:-1]
            self.innen0.append(P[j][None, :] + s[:, None] * (P[k] - P[j])[None, :])
        self.n_innen = 6 * (N - 1) * 3

    def entpacken(self, x):
        N = self.N
        innen = x[:self.n_innen].reshape(6, N - 1, 3)
        Xf = x[self.n_innen:self.n_innen + 9].reshape(3, 3)
        rf = x[self.n_innen + 9:self.n_innen + 18].reshape(3, 3)
        X = torch.cat([torch.tensor(self.P[0:1]), Xf], 0)
        r = torch.cat([torch.zeros(1, 3), rf], 0)
        return innen, X, r

    def startvektor(self):
        x = np.concatenate([np.concatenate([i.ravel() for i in self.innen0]), self.P[1:].ravel(), np.zeros(9)])
        return x

    def teile(self, x):
        """Energie je Stab und die Einspannrichtungen (fuer Kraefte und Momente)."""
        innen, X, r = self.entpacken(x)
        R = [torch.matrix_exp(schief(r[j])) for j in range(4)]
        dvec = {key: R[key[0]] @ torch.tensor(v) for key, v in self.d0.items()}
        E = []
        for m, (j, k) in enumerate(STAEBE):
            y = torch.cat([X[j:j + 1], innen[m], X[k:k + 1]], 0)
            e = y[1:] - y[:-1]
            le = torch.sqrt((e * e).sum(1))
            t = e / le[:, None]
            es = 0.5 * KS * ((le - self.l0) ** 2).sum() / self.l0
            eb = (B / self.l0) * (1.0 - (t[:-1] * t[1:]).sum(1)).sum()
            ec = (2.0 * B / self.l0) * ((1.0 - (dvec[(j, m)] * t[0]).sum()) + (1.0 + (dvec[(k, m)] * t[-1]).sum()))
            E.append(es + eb + ec)
        return E, dvec, X

    def energie(self, x):
        E, _, _ = self.teile(x)
        return sum(E)


def loesen(mod):
    def eg(xf):
        x = torch.tensor(xf, requires_grad=True)
        en = mod.energie(x)
        g, = torch.autograd.grad(en, x)
        return float(en), g.numpy().copy()

    res = minimize(eg, mod.startvektor(), jac=True, method="L-BFGS-B",
                   options=dict(maxiter=20000, maxfun=40000, gtol=1e-7, ftol=1e-15, maxcor=50))
    x = res.x.copy()
    # gedaempfte Newton-Politur mit der vollen Hesse-Matrix
    for _ in range(8):
        e0, g = eg(x)
        if np.linalg.norm(g) < 1e-11:
            break
        H = torch.autograd.functional.hessian(mod.energie, torch.tensor(x)).numpy()
        schritt = np.linalg.solve(H, g)
        s = 1.0
        while s > 1e-4:
            xn = x - s * schritt
            if eg(xn)[0] <= e0 + 1e-14 * abs(e0):
                break
            s *= 0.5
        x = xn
    _, g = eg(x)
    return x, res, float(np.linalg.norm(g))


def lasten(mod, x):
    """Kraft und Moment jedes Stabs auf seine beiden Verbinder (Stabenergie einzeln differenziert)."""
    assert mod.N % 2 == 0
    res = []
    innen2, X2, r2 = mod.entpacken(torch.tensor(x))
    Xn = X2.numpy()
    zentrum = Xn.mean(0)
    for m, (j, k) in enumerate(STAEBE):
        # Lagegradient: Ableitung nach einer Verschiebung von X_j bzw. X_k
        dXj = torch.zeros(3, requires_grad=True)
        dXk = torch.zeros(3, requires_grad=True)
        R2 = [torch.matrix_exp(schief(r2[q])) for q in range(4)]
        dj = (R2[j] @ torch.tensor(mod.d0[(j, m)])).detach().requires_grad_(True)
        dk = (R2[k] @ torch.tensor(mod.d0[(k, m)])).detach().requires_grad_(True)
        y = torch.cat([(X2[j] + dXj)[None, :], innen2[m], (X2[k] + dXk)[None, :]], 0)
        e = y[1:] - y[:-1]
        le = torch.sqrt((e * e).sum(1))
        t = e / le[:, None]
        es = 0.5 * KS * ((le - mod.l0) ** 2).sum() / mod.l0
        eb = (B / mod.l0) * (1.0 - (t[:-1] * t[1:]).sum(1)).sum()
        ec = (2.0 * B / mod.l0) * ((1.0 - (dj * t[0]).sum()) + (1.0 + (dk * t[-1]).sum()))
        Em = es + eb + ec
        gj, gk, gdj, gdk = torch.autograd.grad(Em, [dXj, dXk, dj, dk])
        Fj, Fk = (-gj).numpy(), (-gk).numpy()
        tj = (-torch.linalg.cross(dj, gdj)).detach().numpy()
        tk = (-torch.linalg.cross(dk, gdk)).detach().numpy()
        sehne = Xn[k] - Xn[j]
        a = float(np.linalg.norm(sehne))
        eh = sehne / a
        mitte = innen2[m][mod.N // 2 - 1].detach().numpy()          # Knoten y_(N/2)
        mp = 0.5 * (Xn[j] + Xn[k])
        stich = float(np.linalg.norm((mitte - mp) - np.dot(mitte - mp, eh) * eh))
        rin = zentrum - mp
        nach_innen = float(np.dot(mitte - mp, rin) / (np.linalg.norm(rin) + 1e-300))
        # Kruemmung aus den Knotenwinkeln
        tt = t.detach().numpy()
        cosw = np.clip((tt[:-1] * tt[1:]).sum(1), -1.0, 1.0)
        kap = np.arccos(cosw) / mod.l0
        res.append({"stab": NAMEN[m], "a": a, "stich": stich, "stich_nach_innen": nach_innen,
                    "kappa_mittel": float(kap.mean()), "kappa_streuung": float(kap.std()),
                    "F_j": Fj.tolist(), "F_k": Fk.tolist(), "tau_j": tj.tolist(), "tau_k": tk.tolist(),
                    "F_j_axial": float(np.dot(Fj, eh)), "F_k_axial": float(np.dot(Fk, -eh)),
                    "F_j_betrag": float(np.linalg.norm(Fj)), "F_k_betrag": float(np.linalg.norm(Fk)),
                    "tau_j_betrag": float(np.linalg.norm(tj)), "tau_k_betrag": float(np.linalg.norm(tk))})
    knoten = []
    for q in range(4):
        F = np.zeros(3)
        T = np.zeros(3)
        for m, (j, k) in enumerate(STAEBE):
            if q == j:
                F += np.array(res[m]["F_j"])
                T += np.array(res[m]["tau_j"])
            elif q == k:
                F += np.array(res[m]["F_k"])
                T += np.array(res[m]["tau_k"])
        knoten.append({"verbinder": "ABCD"[q], "F_summe": float(np.linalg.norm(F)), "tau_summe": float(np.linalg.norm(T))})
    return res, knoten


def main():
    name, N, ag, agab, hesse, pfad = (sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]),
                                      int(sys.argv[5]), sys.argv[6])
    al, alab = math.radians(ag), math.radians(agab)
    t0 = time.time()
    mod = Modell(N, al, alab)
    x, res, gnorm = loesen(mod)
    stab, knoten = lasten(mod, x)
    out = {"name": name, "N": N, "alpha_grad": ag, "alpha_AB_grad": agab, "B": B, "L": L, "Ks": KS,
           "energie": float(mod.energie(torch.tensor(x))), "gradnorm": gnorm, "lbfgs_nit": int(res.nit),
           "lbfgs_meldung": str(res.message), "staebe": stab, "verbinder": knoten,
           "soll_tau_2Balpha_L": 2.0 * B * al / L,
           "soll_a": (L / al) * math.sin(al) if al > 0 else L}
    if hesse:
        H = torch.autograd.functional.hessian(mod.energie, torch.tensor(x)).numpy()
        ev = np.linalg.eigvalsh(0.5 * (H + H.T))
        out["hesse_kleinste"] = [float(v) for v in ev[:8]]
    out["sek"] = time.time() - t0
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    taus = [s["tau_j_betrag"] for s in stab] + [s["tau_k_betrag"] for s in stab]
    Fs = [s["F_j_betrag"] for s in stab] + [s["F_k_betrag"] for s in stab]
    print(f"{name}: N {N}, alpha {ag}/{agab} Grad, |grad| {gnorm:.1e}, tau {min(taus):.6f}..{max(taus):.6f} "
          f"(soll {out['soll_tau_2Balpha_L']:.6f}), |F| max {max(Fs):.2e}, a {stab[5]['a']:.6f} "
          f"(soll {out['soll_a']:.6f}), {out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
