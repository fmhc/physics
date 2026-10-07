#!/usr/bin/env python3
"""REGGE-4D-1 (Runde 36, Code-Agent): linearisierte Regge-Wirkung auf dem Kuhn-Gitter.

Hauptfall n = 4 (Gelenke = Dreiecke), Kontrolle n = 3 (Gelenke = Kanten). Reines numpy, float64.

  1. Kuhn-Zerlegung des n-Wuerfels (n! Simplizes je Wuerfel), periodischer Torus L^n.
  2. Einbettung jedes Simplex aus seinen Kantenlaengenquadraten s = l^2 (Gram-Matrix, Cholesky). Diederwinkel an
     jedem Gelenk ueber das orthogonale Komplement der Gelenkebene (2-dimensional).
  3. Fehlwinkel eps_t = 2 pi - sum theta. Flachheit.
  4. Weg T: d eps_t / d s_e fuer die 2^n - 1 Kantentypen an der Ursprungsecke per zentraler Differenz auf dem Torus
     (Richardson aus h und h/2). Weg J: lokale Jacobimatrix je Simplextyp, ohne Torus (Gegenprobe).
  5. dV_t/ds_e analytisch (n = 4: Heron; n = 3: 1/(2 l)).
  6. M(k) = A(k)^+ E(k) in Mittelpunktskonvention (Phase exp(i k.(x + d/2)) je Kante). H = -M: Vorzeichen der
     euklidischen Einstein-Hilbert-Wirkung I_E = -(1/8 pi G) sum A eps (PLAN [F2]).
  7. Spektren, Klassen (Null, Kontinuum, Gitter), effektive Form auf h_mu_nu (Schur), Spinprojektoren.

Aufruf: python regge4d.py <modus: rauch | haupt> <ausgabe.json>
"""
import itertools
import json
import sys
import time

import numpy as np

ZWEI_PI = 2.0 * np.pi
NULL_REL = 1e-6          # Nullmoden: |lambda| < NULL_REL * max|lambda| (Karte G1, PLAN [F9])
PINV_RCOND = 1e-8        # Pseudoinverse im Schur-Komplement (PLAN [F6])
H_STUFE = 1e-3           # Richardson aus h und h/2 (PLAN [F4]); Fehlerschaetzung mit 2h und h
BETRAEGE = [0.05, 0.1, 0.2, 0.4]


def richtungen(n):
    """Feste Richtungsliste (PLAN [F8])."""
    if n == 4:
        roh = {
            "achse_1000": (1, 0, 0, 0),
            "flaeche_1100": (1, 1, 0, 0),
            "gegen_1m100": (1, -1, 0, 0),
            "raum_1110": (1, 1, 1, 0),
            "hyper_1111": (1, 1, 1, 1),
            "quer_11m1m1": (1, 1, -1, -1),
            "schief_111m1": (1, 1, 1, -1),
            "allg_1234": (1, 2, 3, 4),
        }
    else:
        roh = {
            "achse_100": (1, 0, 0),
            "flaeche_110": (1, 1, 0),
            "gegen_1m10": (1, -1, 0),
            "raum_111": (1, 1, 1),
            "quer_11m1": (1, 1, -1),
            "allg_123": (1, 2, 3),
        }
    return {k: np.array(v, float) / np.linalg.norm(v) for k, v in roh.items()}


class Gitter:
    def __init__(self, n, L):
        self.n, self.L = n, L
        dirs = [d for d in itertools.product((0, 1), repeat=n) if any(d)]
        dirs.sort(key=lambda d: (sum(d), tuple(-x for x in d)))
        self.dirs = np.array(dirs, dtype=np.int64)
        self.nE = len(dirs)
        self.dir_index = {tuple(d): i for i, d in enumerate(dirs)}
        self.top = self.dir_index[tuple([1] * n)]          # Hyperdiagonale (n = 4) bzw. Raumdiagonale (n = 3)
        # Gelenktypen: Ketten aus n-1 Ecken mit n-2 disjunkten, nicht leeren 0/1-Schritten
        typen = []
        for zuord in itertools.product(range(n - 1), repeat=n):
            if all(any(z == j for z in zuord) for j in range(1, n - 1)):
                schritte = [tuple(1 if z == j else 0 for z in zuord) for j in range(1, n - 1)]
                typen.append(tuple(schritte))
        typen.sort()
        self.gtypen = typen
        self.nH = len(typen)
        self.gtyp_index = {t: i for i, t in enumerate(typen)}
        # Ecken, Schwerpunkt, Kanten (Basis, Richtung) je Gelenktyp
        self.g_ecken, self.g_mitte, self.g_kanten = [], [], []
        for t in typen:
            w = [np.zeros(n, dtype=np.int64)]
            for st in t:
                w.append(w[-1] + np.array(st))
            self.g_ecken.append(w)
            self.g_mitte.append(np.mean(np.array(w, float), axis=0))
            kanten = []
            for i, j in itertools.combinations(range(len(w)), 2):
                kanten.append((w[i].copy(), self.dir_index[tuple(w[j] - w[i])]))
            self.g_kanten.append(kanten)
        self.g_mitte = np.array(self.g_mitte)
        # Simplextypen (Permutationen); lokale Kanten und Gelenke
        self.perms = list(itertools.permutations(range(n)))
        self.nP = len(self.perms)
        self.paare = list(itertools.combinations(range(n + 1), 2))           # lokale Kanten (i < j)
        self.lok_gelenke = []                                                  # (Eckenliste, ausgelassenes Paar)
        for m, mm in itertools.combinations(range(n + 1), 2):
            rest = [v for v in range(n + 1) if v not in (m, mm)]
            self.lok_gelenke.append((rest, (m, mm)))
        E = np.eye(n, dtype=np.int64)
        self.p_ecken = []        # je Typ: (n+1, n) Ecken relativ zur Basis
        self.p_kanten = []       # je Typ: Liste (Basis, Richtungsindex) in lokaler Kantenreihenfolge
        self.p_gelenke = []      # je Typ: Liste (Basis, Gelenktypindex) in lokaler Gelenkreihenfolge
        for p in self.perms:
            v = [np.zeros(n, dtype=np.int64)]
            for a in p:
                v.append(v[-1] + E[a])
            v = np.array(v)
            self.p_ecken.append(v)
            self.p_kanten.append([(v[i].copy(), self.dir_index[tuple(v[j] - v[i])]) for i, j in self.paare])
            gl = []
            for rest, _ in self.lok_gelenke:
                st = tuple(tuple(v[rest[q + 1]] - v[rest[q]]) for q in range(len(rest) - 1))
                gl.append((v[rest[0]].copy(), self.gtyp_index[st]))
            self.p_gelenke.append(gl)
        # Torus
        self.N = L ** n
        self.coords = np.array(list(itertools.product(range(L), repeat=n)), dtype=np.int64)
        sk, sg = [], []
        for x in self.coords:
            for ip in range(self.nP):
                sk.append([self.vidx(x + b) * self.nE + d for b, d in self.p_kanten[ip]])
                sg.append([self.vidx(x + b) * self.nH + t for b, t in self.p_gelenke[ip]])
        self.simp_kanten = np.array(sk, dtype=np.int64)
        self.simp_gelenke = np.array(sg, dtype=np.int64)
        self.s0 = np.tile(np.sum(self.dirs ** 2, axis=1).astype(float), self.N)

    def vidx(self, y):
        y = np.mod(y, self.L)
        r = 0
        for c in y:
            r = r * self.L + int(c)
        return r

    # ---------------------------------------------------------------- Geometrie
    def winkel(self, sq):
        """Diederwinkel (Ns, Gelenke) aus Kantenlaengenquadraten (Ns, Kanten) in lokaler Reihenfolge."""
        n = self.n
        Ns = sq.shape[0]
        S = np.zeros((Ns, n + 1, n + 1))
        for k, (i, j) in enumerate(self.paare):
            S[:, i, j] = sq[:, k]
            S[:, j, i] = sq[:, k]
        G = 0.5 * (S[:, 0, 1:, None] + S[:, 0, None, 1:] - S[:, 1:, 1:])
        Lc = np.linalg.cholesky(G)
        P = np.concatenate([np.zeros((Ns, 1, n)), Lc], axis=1)
        ang = np.empty((Ns, len(self.lok_gelenke)))
        for h, (rest, (m, mm)) in enumerate(self.lok_gelenke):
            basis = P[:, rest[0]]
            V = np.stack([P[:, v] - basis for v in rest[1:]], axis=2)
            Q, _ = np.linalg.qr(V, mode="complete")
            Qc = Q[:, :, n - 2:]
            u = np.einsum("sij,si->sj", Qc, P[:, m] - basis)
            w = np.einsum("sij,si->sj", Qc, P[:, mm] - basis)
            ang[:, h] = np.abs(np.arctan2(u[:, 0] * w[:, 1] - u[:, 1] * w[:, 0], u[:, 0] * w[:, 0] + u[:, 1] * w[:, 1]))
        return ang

    def fehlwinkel(self, s_glob):
        ang = self.winkel(s_glob[self.simp_kanten])
        summe = np.bincount(self.simp_gelenke.ravel(), weights=ang.ravel(), minlength=self.N * self.nH)
        return ZWEI_PI - summe

    def gelenkvolumen(self, sq):
        """Volumen eines Gelenks aus seinen Kantenquadraten (n = 4: Dreieck; n = 3: Kante)."""
        if self.n == 3:
            return np.sqrt(sq[0])
        a, b, c = sq
        return 0.25 * np.sqrt(2 * a * b + 2 * b * c + 2 * c * a - a * a - b * b - c * c)

    def gelenk_ableitung(self, t):
        """dV/ds fuer die Kanten des flachen Gelenktyps t (analytisch)."""
        kanten = self.g_kanten[t]
        sq = [float(np.sum(self.dirs[d] ** 2)) for _, d in kanten]
        if self.n == 3:
            return [0.5 / np.sqrt(sq[0])]
        A = self.gelenkvolumen(sq)
        out = []
        for x in range(3):
            y, z = [q for q in range(3) if q != x]
            out.append((sq[y] + sq[z] - sq[x]) / (16.0 * A))
        return out

    # ---------------------------------------------------------------- Weg T (Torus)
    def ableitung_T(self, h=H_STUFE):
        s0 = self.s0
        cache = {}

        def F(g, hh):
            key = (g, hh)
            if key not in cache:
                sp = s0.copy()
                sp[g] += hh
                cache[key] = self.fehlwinkel(sp)
            return cache[key]

        def D(g, hh):
            return (F(g, hh) - F(g, -hh)) / (2.0 * hh)

        eT = []
        fehler = []
        betroffen = []
        for d in range(self.nE):
            g = 0 * self.nE + d
            R1 = (4.0 * D(g, h / 2) - D(g, h)) / 3.0
            R2 = (4.0 * D(g, h) - D(g, 2 * h)) / 3.0
            idx = np.nonzero(R1)[0]
            v = idx // self.nH
            tau = idx % self.nH
            x = self.coords[v]
            u = np.mod(x + 1, self.L) - 1
            assert np.max(np.abs(u)) <= 1, "Ueberlappung: betroffenes Gelenk ausserhalb [-1,1]^n"
            eT.append((tau, -u, R1[idx]))
            fehler.append(float(np.max(np.abs(R1 - R2))))
            betroffen.append(int(len(idx)))
            cache.clear()
        return eT, fehler, betroffen

    # ---------------------------------------------------------------- Weg J (lokal)
    def jacobi_lokal(self, h=H_STUFE):
        nEs = len(self.paare)
        sq0 = np.array([[float(np.sum(self.dirs[d] ** 2)) for _, d in self.p_kanten[ip]] for ip in range(self.nP)])
        stufen = [h, -h, h / 2, -h / 2]
        batch = []
        for ip in range(self.nP):
            for e in range(nEs):
                for st in stufen:
                    q = sq0[ip].copy()
                    q[e] += st
                    batch.append(q)
        ang = self.winkel(np.array(batch)).reshape(self.nP, nEs, 4, -1)
        D1 = (ang[:, :, 0] - ang[:, :, 1]) / (2 * h)
        D2 = (ang[:, :, 2] - ang[:, :, 3]) / h
        J = (4 * D2 - D1) / 3.0                       # (nP, Kanten, Gelenke): d theta_g / d s_e
        J = np.transpose(J, (0, 2, 1))                # (nP, Gelenke, Kanten)
        ang0 = self.winkel(sq0)
        return J, ang0, sq0

    def eT_aus_J(self, J):
        """Koeffizienten e_{tau,d'}(R') = d eps_(0,tau) / d s_(R',d') aus den lokalen Jacobimatrizen."""
        dic = {}
        for ip in range(self.nP):
            for hl, (bh, tau) in enumerate(self.p_gelenke[ip]):
                for el, (be, d) in enumerate(self.p_kanten[ip]):
                    key = (tau, d, tuple(be - bh))
                    dic[key] = dic.get(key, 0.0) - J[ip, hl, el]
        return dic

    # ---------------------------------------------------------------- Fourier
    def matrizen(self, ks, eT):
        """A(k), E(k) (Nk, nH, nE) und M(k) = A^+ E (Nk, nE, nE)."""
        ks = np.atleast_2d(ks)
        Nk = ks.shape[0]
        Em = np.zeros((Nk, self.nH, self.nE), complex)
        for d in range(self.nE):
            tau, Rp, val = eT[d]
            pos = Rp + 0.5 * self.dirs[d][None, :] - self.g_mitte[tau]
            ph = np.exp(1j * ks @ pos.T) * val[None, :]
            S = np.zeros((len(tau), self.nH))
            S[np.arange(len(tau)), tau] = 1.0
            Em[:, :, d] = ph @ S
        Am = np.zeros((Nk, self.nH, self.nE), complex)
        for t in range(self.nH):
            abl = self.gelenk_ableitung(t)
            for (be, d), a in zip(self.g_kanten[t], abl):
                pos = be + 0.5 * self.dirs[d] - self.g_mitte[t]
                Am[:, t, d] += a * np.exp(1j * ks @ pos)
        M = np.einsum("kti,ktj->kij", Am.conj(), Em)
        return Am, Em, M

    # ---------------------------------------------------------------- h-Abbildung und Projektoren
    def sym_basis(self):
        n = self.n
        basis, namen = [], []
        for m in range(n):
            X = np.zeros((n, n))
            X[m, m] = 1.0
            basis.append(X)
            namen.append(f"h{m}{m}")
        for m, mm in itertools.combinations(range(n), 2):
            X = np.zeros((n, n))
            X[m, mm] = X[mm, m] = 1.0 / np.sqrt(2.0)
            basis.append(X)
            namen.append(f"h{m}{mm}")
        return basis, namen

    def B0(self):
        """delta s_d = d^mu d^nu h_mu_nu, in der Frobenius-orthonormalen Basis (nE x n(n+1)/2)."""
        basis, _ = self.sym_basis()
        return np.array([[float(d @ X @ d) for X in basis] for d in self.dirs.astype(float)])

    def projektoren(self, nhat):
        n = self.n
        basis, _ = self.sym_basis()
        th = np.eye(n) - np.outer(nhat, nhat)
        om = np.outer(nhat, nhat)

        def mat(f):
            return np.array([[np.sum(Xa * f(Xb)) for Xb in basis] for Xa in basis])

        P2 = mat(lambda X: th @ X @ th - th * np.trace(th @ X) / (n - 1))
        P1 = mat(lambda X: th @ X @ om + om @ X @ th)
        P0s = mat(lambda X: th * np.trace(th @ X) / (n - 1))
        P0w = mat(lambda X: om * np.trace(om @ X))
        svec = np.array([np.sum(Xa * th) for Xa in basis]) / np.sqrt(n - 1)
        wvec = np.array([np.sum(Xa * om) for Xa in basis])
        return P2, P1, P0s, P0w, svec, wvec

    def eich_basis(self, k):
        """Gitter-Eichmoden (Eckenverschiebungen) in Mittelpunktskonvention: u_d ~ sin(k.d/2) d_mu."""
        return np.sin(0.5 * (self.dirs @ k))[:, None] * self.dirs.astype(float)


def h_von_M(M):
    """H = -(M + M^+)/2, reeller Teil (Mittelpunktskonvention: M reell)."""
    Ms = 0.5 * (M + np.conj(np.swapaxes(M, -1, -2)))
    return -Ms.real, float(np.max(np.abs(Ms.imag)) / max(np.max(np.abs(Ms.real)), 1e-300))


def analyse_punkt(git, k, H, B, Pi_h, Cc, mit_form=True):
    """Spektrum, Klassen und effektive Form an einem k-Punkt."""
    lam, V = np.linalg.eigh(H)
    Lam = float(np.max(np.abs(lam)))
    null = np.abs(lam) < NULL_REL * Lam
    eta = np.einsum("ij,ik,kj->j", V, Pi_h, V)
    kont = (~null) & (eta > 0.5)
    gitt = (~null) & (eta <= 0.5)
    out = {
        "k": [float(x) for x in k],
        "betrag": float(np.linalg.norm(k)),
        "Lambda": Lam,
        "eigenwerte": [float(x) for x in lam],
        "eta": [float(x) for x in eta],
        "n_null": int(np.sum(null)),
        "n_kont_pos": int(np.sum(kont & (lam > 0))),
        "n_kont_neg": int(np.sum(kont & (lam < 0))),
        "n_gitter_pos": int(np.sum(gitt & (lam > 0))),
        "n_gitter_neg": int(np.sum(gitt & (lam < 0))),
        "kont_werte": [float(x) for x in np.sort(lam[kont])],
        "gitter_werte": [float(x) for x in np.sort(lam[gitt])],
        "null_werte_rel": [float(x) / Lam for x in lam[null]],
    }
    e_top = np.zeros(git.nE)
    e_top[git.top] = 1.0
    out["top_residuum_rel"] = float(np.linalg.norm(H @ e_top) / Lam)
    kn = np.linalg.norm(k)
    if kn > 0:
        G = git.eich_basis(k)
        Qg, _ = np.linalg.qr(G)
        out["eich_residuum_rel"] = float(np.linalg.norm(H @ Qg, 2) / Lam)
        # Nullraum ausserhalb span(Eichmoden, e_top)
        Z, _ = np.linalg.qr(np.column_stack([Qg, e_top]))
        nullv = V[:, null]
        if nullv.shape[1] > 0:
            rest = nullv - Z @ (Z.T @ nullv)
            out["nullraum_ausserhalb_eich_top"] = float(np.max(np.linalg.svd(rest, compute_uv=False)))
    if not mit_form or kn == 0:
        return out
    # effektive Form: Schur-Komplement mit Komplement Cc (PLAN [F6]) und direkte Form
    Khh = B.T @ H @ B
    Khw = B.T @ H @ Cc
    Kww = Cc.T @ H @ Cc
    ww, Uw = np.linalg.eigh(Kww)
    behalten = np.abs(ww) > PINV_RCOND * np.max(np.abs(ww))
    Kww_pinv = (Uw[:, behalten] / ww[behalten]) @ Uw[:, behalten].T
    out["Kww_verworfen"] = int(np.sum(~behalten))
    K_schur = Khh - Khw @ Kww_pinv @ Khw.T
    K_schur = 0.5 * (K_schur + K_schur.T)
    out["Kww_eigenwerte"] = [float(x) for x in np.linalg.eigvalsh(Kww)]
    nhat = k / kn
    P2, P1, P0s, P0w, svec, wvec = git.projektoren(nhat)
    for name, K in (("schur", K_schur), ("direkt", Khh)):
        out["form_" + name] = spin_zerlegung(git, K, kn, P2, P1, P0s, P0w, svec, wvec, B, k)
    out["schur_minus_direkt_rel"] = float(np.linalg.norm(K_schur - Khh) / np.linalg.norm(Khh))
    return out


def spin_zerlegung(git, K, kn, P2, P1, P0s, P0w, svec, wvec, B, k):
    n = git.n
    r2 = int(round(np.trace(P2)))
    r1 = int(round(np.trace(P1)))
    k2 = kn * kn
    c2 = float(np.trace(P2 @ K) / (r2 * k2))
    c1 = float(np.trace(P1 @ K) / (r1 * k2))
    c0s = float(svec @ K @ svec / k2)
    c0w = float(wvec @ K @ wvec / k2)
    c0sw = float(svec @ K @ wvec / k2)
    w2, U2 = np.linalg.eigh(P2)
    Q2 = U2[:, w2 > 0.5]
    spin2 = np.linalg.eigvalsh(Q2.T @ K @ Q2) / k2
    w1, U1 = np.linalg.eigh(P1)
    Q1 = U1[:, w1 > 0.5]
    spin1 = np.linalg.eigvalsh(Q1.T @ K @ Q1) / k2
    P0 = P0s + P0w
    nK = np.linalg.norm(K)
    misch = {
        "2-1": float(np.linalg.norm(P2 @ K @ P1) / nK),
        "2-0": float(np.linalg.norm(P2 @ K @ P0) / nK),
        "1-0": float(np.linalg.norm(P1 @ K @ P0) / nK),
    }
    K_eh = 0.25 * k2 * (P2 - (n - 2) * P0s)
    dev_fest = float(np.linalg.norm(K - K_eh) / np.linalg.norm(K_eh))
    dev_norm = float(np.linalg.norm(K - 4 * c2 * K_eh) / np.linalg.norm(4 * c2 * K_eh)) if c2 != 0 else None
    # Kontinuums-Eichmoden h = k xi + xi k
    basis, _ = git.sym_basis()
    res = []
    for mu in range(n):
        xi = np.zeros(n)
        xi[mu] = 1.0
        X = np.outer(k, xi) + np.outer(xi, k)
        hv = np.array([np.sum(Xa * X) for Xa in basis])
        res.append(np.linalg.norm(K @ hv) / (np.linalg.norm(K, 2) * np.linalg.norm(hv)))
    ev = np.linalg.eigvalsh(K) / k2
    return {
        "c2": c2, "c1": c1, "c0s": c0s, "c0w": c0w, "c0sw": c0sw,
        "verhaeltnis_0s_2": c0s / c2 if c2 != 0 else None,
        "spin2_eigenwerte": [float(x) for x in spin2],
        "spin1_eigenwerte": [float(x) for x in spin1],
        "mischung": misch,
        "abweichung_EH_fest_1_4": dev_fest,
        "abweichung_EH_normiert": dev_norm,
        "kontinuums_eich_residuum_rel": float(max(res)),
        "eigenwerte_durch_k2": [float(x) for x in ev],
    }


def komplement(git, B):
    """Komplement C = [e_top, C_rest], C_rest = orthogonales Komplement von range(B ohne top-Zeile) in R^(nE-1)."""
    rows = [i for i in range(git.nE) if i != git.top]
    Bp = B[rows]
    U, sv, _ = np.linalg.svd(Bp, full_matrices=True)
    rang = int(np.sum(sv > 1e-10 * sv[0]))
    rest = U[:, rang:]
    C = np.zeros((git.nE, 1 + rest.shape[1]))
    C[git.top, 0] = 1.0
    C[np.array(rows), 1:] = rest
    return C, rang


def lauf(n, L, modus, protokoll):
    t0 = time.time()
    git = Gitter(n, L)
    res = {"n": n, "L": L, "kanten_je_ecke": git.nE, "gelenke_je_ecke": git.nH, "simplizes_je_ecke": git.nP}
    # Flachheit
    eps0 = git.fehlwinkel(git.s0)
    zahl = np.bincount(git.simp_gelenke.ravel(), minlength=git.N * git.nH)
    res["flach_max_abs_eps"] = float(np.max(np.abs(eps0)))
    res["simplizes_je_gelenk_min_max"] = [int(zahl.min()), int(zahl.max())]
    kz = np.bincount(git.simp_kanten.ravel(), minlength=git.N * git.nE)
    res["simplizes_je_kante_min_max"] = [int(kz.min()), int(kz.max())]
    # gleichmaessige Skalierung bleibt flach
    res["flach_skaliert_1_3"] = float(np.max(np.abs(git.fehlwinkel(1.69 * git.s0))))
    # zufaellige affine Verzerrung bleibt flach
    rng = np.random.default_rng(20261004)
    A = np.eye(n) + 0.1 * rng.standard_normal((n, n))
    Gm = A.T @ A
    s_aff = np.tile(np.einsum("di,ij,dj->d", git.dirs, Gm, git.dirs), git.N)
    res["flach_affin"] = float(np.max(np.abs(git.fehlwinkel(s_aff))))
    J, ang0, sq0 = git.jacobi_lokal()
    res["diederwinkel_flach_durch_pi"] = sorted(set(round(float(a) / np.pi, 12) for a in ang0.ravel()))
    # Schlaefli je Simplex: sum_g V_g d theta_g / d s_e = 0
    schl = 0.0
    for ip in range(git.nP):
        V = []
        for rest, _ in git.lok_gelenke:
            sq = [sq0[ip][git.paare.index((rest[a], rest[b]))] for a, b in itertools.combinations(range(len(rest)), 2)]
            V.append(git.gelenkvolumen(sq))
        schl = max(schl, float(np.max(np.abs(np.array(V) @ J[ip]))))
    res["schlaefli_je_simplex_max"] = schl
    protokoll(f"n={n} L={L}: Geometrie fertig ({time.time() - t0:.1f} s), max|eps| = {res['flach_max_abs_eps']:.2e}")
    if res["flach_max_abs_eps"] > 1e-8:
        res["abbruch"] = "Flachheit verfehlt"
        return res
    # Weg T
    eT, fehler, betroffen = git.ableitung_T()
    res["weg_T_fehlerschaetzung_max"] = float(max(fehler))
    res["weg_T_betroffene_gelenke"] = betroffen
    # Weg T gegen Weg J
    dJ = git.eT_aus_J(J)
    dT = {}
    for d in range(git.nE):
        tau, Rp, val = eT[d]
        for t_, r_, v_ in zip(tau, Rp, val):
            dT[(int(t_), d, tuple(int(x) for x in r_))] = float(v_)
    keys = set(dJ) | set(dT)
    diff = max(abs(dJ.get(q, 0.0) - dT.get(q, 0.0)) for q in keys)
    res["weg_T_gegen_J_max_abs"] = float(diff)
    res["weg_T_max_abs"] = float(max(abs(v) for v in dT.values()))
    res["weg_J_nur_nahe_null"] = float(max([abs(v) for q, v in dJ.items() if q not in dT] + [0.0]))
    protokoll(f"n={n}: Ableitungen fertig ({time.time() - t0:.1f} s), T gegen J {diff:.2e}")
    B = git.B0()
    Pi_h = B @ np.linalg.solve(B.T @ B, B.T)
    Cc, rangB = komplement(git, B)
    res["rang_B_ohne_top"] = rangB
    res["komplement_dim"] = int(Cc.shape[1])
    # Schlaefli global bei k = 0 und Hermitezitaet auf einer Stichprobe
    k0 = np.zeros((1, n))
    Am, Em, M0 = git.matrizen(k0, eT)
    Vt = np.array([git.gelenkvolumen([float(np.sum(git.dirs[d] ** 2)) for _, d in git.g_kanten[t]])
                   for t in range(git.nH)])
    res["schlaefli_global_k0"] = float(np.max(np.abs(Vt @ Em[0].real)))
    res["top_spalte_A_max"] = float(np.max(np.abs(Am[0][:, git.top])))
    # Stichprobe zufaelliger k fuer die Hermitezitaet
    ks_zuf = rng.uniform(-np.pi, np.pi, size=(64, n))
    _, _, Mz = git.matrizen(ks_zuf, eT)
    herm = np.max(np.abs(Mz - np.conj(np.swapaxes(Mz, 1, 2))), axis=(1, 2)) / np.max(np.abs(Mz), axis=(1, 2))
    res["hermitesch_zufall_max_rel"] = float(np.max(herm))
    res["imag_zufall_max_rel"] = float(np.max(np.abs(Mz.imag)) / np.max(np.abs(Mz.real)))
    if modus == "rauch" and n == 4:
        protokoll("Rauchlauf n = 4: Spektrum nicht berechnet (nur Geometrie und Ableitungen)")
        return res
    # k-Punkte: k = 0 und die Leiter je Richtung
    R = richtungen(n)
    punkte = [("null", 0.0, np.zeros(n))]
    for name, nh in R.items():
        for b in BETRAEGE:
            punkte.append((name, b, b * nh))
    ks = np.array([p[2] for p in punkte])
    _, _, Mk = git.matrizen(ks, eT)
    herm_k = np.max(np.abs(Mk - np.conj(np.swapaxes(Mk, 1, 2))), axis=(1, 2)) / np.max(np.abs(Mk), axis=(1, 2))
    res["hermitesch_leiter_max_rel"] = float(np.max(herm_k))
    Hk, imag = h_von_M(Mk)
    res["imag_leiter_max_rel"] = imag
    erg = []
    for (name, b, k), H in zip(punkte, Hk):
        a = analyse_punkt(git, k, H, B, Pi_h, Cc)
        a["richtung"] = name
        a["betrag_nominal"] = b
        erg.append(a)
    res["punkte"] = erg
    # k = 0: Nullraum gegen affine Verzerrungen
    H0 = Hk[0]
    Lam0 = np.max(np.abs(np.linalg.eigvalsh(H0)))
    Qb, _ = np.linalg.qr(B)
    res["k0_affin_residuum_rel"] = float(np.linalg.norm(H0 @ Qb, 2) / Lam0)
    lam0, V0 = np.linalg.eigh(H0)
    nullv = V0[:, np.abs(lam0) < NULL_REL * Lam0]
    # Anteil des Nullraums ausserhalb der affinen Verzerrungen
    rest0 = nullv - Qb @ (Qb.T @ nullv)
    sv = np.linalg.svd(rest0, compute_uv=False)
    res["k0_nullraum_ausserhalb_affin_singulaerwerte"] = [float(x) for x in sv]
    e_top = np.zeros(git.nE)
    e_top[git.top] = 1.0
    res["k0_top_residuum_rel"] = float(np.linalg.norm(H0 @ e_top) / Lam0)
    protokoll(f"n={n}: Leiter fertig ({time.time() - t0:.1f} s)")
    if modus != "haupt" and n == 4:
        return res
    # feine Kurven fuer Bilder (beschreibend)
    fein = np.logspace(-2, np.log10(np.pi), 36)
    kurven = {}
    for name, nh in R.items():
        ksf = fein[:, None] * nh[None, :]
        _, _, Mf = git.matrizen(ksf, eT)
        Hf, _ = h_von_M(Mf)
        ev, kl, c2, r = [], [], [], []
        for kk, H in zip(ksf, Hf):
            a = analyse_punkt(git, kk, H, B, Pi_h, Cc)
            ev.append(a["eigenwerte"])
            kl.append(["n" if abs(x) < NULL_REL * a["Lambda"] else ("k" if e > 0.5 else "g")
                       for x, e in zip(a["eigenwerte"], a["eta"])])
            c2.append(a["form_schur"]["c2"])
            r.append(a["form_schur"]["verhaeltnis_0s_2"])
        kurven[name] = {"betrag": [float(x) for x in fein], "eigenwerte": ev, "klasse": kl, "c2": c2, "r": r}
    res["kurven"] = kurven
    if modus != "haupt":
        return res
    # Brillouin-Zone (beschreibend): 8^n Gitterimpulse
    Lb = 8 if n == 4 else 16
    qs = 2 * np.pi * np.array(list(itertools.product(range(Lb), repeat=n)), float) / Lb
    qs = np.where(qs > np.pi, qs - 2 * np.pi, qs)
    zaehl = {}
    min_rel = []
    for start in range(0, len(qs), 512):
        _, _, Mb = git.matrizen(qs[start:start + 512], eT)
        Hb, _ = h_von_M(Mb)
        lb = np.linalg.eigvalsh(Hb)
        Lb_ = np.max(np.abs(lb), axis=1)
        for q, l_, L_ in zip(qs[start:start + 512], lb, Lb_):
            nn = int(np.sum(np.abs(l_) < NULL_REL * L_))
            npos = int(np.sum(l_ >= NULL_REL * L_))
            nneg = int(np.sum(l_ <= -NULL_REL * L_))
            key = f"{nn}/{npos}/{nneg}"
            zaehl[key] = zaehl.get(key, 0) + 1
            if np.linalg.norm(q) > 0:
                nz = np.abs(l_[np.abs(l_) >= NULL_REL * L_])
                min_rel.append(float(np.min(nz) / L_ / max(np.dot(q, q), 1e-300)))
    res["bz_zaehlung_null_pos_neg"] = zaehl
    res["bz_punkte"] = int(len(qs))
    res["bz_min_nichtnull_durch_Lambda_q2"] = float(min(min_rel))
    protokoll(f"n={n}: fertig ({time.time() - t0:.1f} s)")
    return res


def main():
    modus = sys.argv[1]
    ziel = sys.argv[2]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    out = {"modus": modus, "numpy": np.__version__}
    out["n3"] = lauf(3, 4, modus, protokoll)
    out["n4"] = lauf(4, 4, modus, protokoll)
    if modus == "haupt":
        out["n4_L3"] = lauf_klein_L3(protokoll)
    out["laufzeit_s"] = time.time() - t0
    out["protokoll"] = log
    with open(ziel, "w") as f:
        json.dump(out, f, indent=1)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s")


def lauf_klein_L3(protokoll):
    """Gegenprobe der Torusgroesse: Weg T auf L = 3 gegen L = 4 (nur Koeffizienten)."""
    g3 = Gitter(4, 3)
    g4 = Gitter(4, 4)
    eps3 = float(np.max(np.abs(g3.fehlwinkel(g3.s0))))
    e3, _, _ = g3.ableitung_T()
    e4, _, _ = g4.ableitung_T()

    def dic(eT):
        d_ = {}
        for d in range(len(eT)):
            tau, Rp, val = eT[d]
            for t_, r_, v_ in zip(tau, Rp, val):
                d_[(int(t_), d, tuple(int(x) for x in r_))] = float(v_)
        return d_

    a, b = dic(e3), dic(e4)
    keys = set(a) | set(b)
    diff = max(abs(a.get(q, 0.0) - b.get(q, 0.0)) for q in keys)
    protokoll(f"L=3 gegen L=4: {diff:.2e}")
    return {"flach_max_abs_eps_L3": eps3, "weg_T_L3_gegen_L4_max_abs": float(diff), "schluessel": len(keys)}


if __name__ == "__main__":
    main()
