#!/usr/bin/env python3
"""LADUNG-MONOPOL-2 (Runde 38): Teil B auf Finns Netz.

Spinloses Teilchen der Ladung q auf dem Pyrochlor-Netz (Knoten = Pyrochlor-Ecken, 6 Kanten je Knoten) um einen
Einheitsmonopol in der Mitte eines Tetraeders; Kern-Topf -V0 auf den 4 Ecken dieses Tetraeders.

Koordinaten: ganzzahlig in Einheiten von 1/8 der kubischen Zellkante, relativ zur Monopol-Tetraedermitte (alle
Ecken haben dann ungerade Koordinaten). Kantenlaenge a = sqrt(8). Box: Wuerfel der Kante L Zellen, zentriert auf den
Monopol (|x_i| <= 4 L), damit die Drehgruppe T der Tetraedermitte exakt erhalten bleibt.

Zellkomplex: Flaechen = Dreiecke der Tetraeder und die (ebenen) Kagome-Sechsecke; Zellen = Tetraeder und
abgestumpfte Tetraeder (4 Sechsecke + 4 Dreiecke). Fluss Phi_f = Omega_f/2 (Sechseck als Faecher aus Schwerpunkt
und 6 Dreiecken). Eichfeld per lsqr mit Dirac-String (gieriger Weg durch die Zellen bis zum Rand).

Modi: rauch, gitter, schwelle, scan. Nur auf der .69 ueber kleintest.sh starten (Spur p4000a).
"""
import argparse
import itertools
import json
import time

import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.sparse.csgraph import breadth_first_order, connected_components

ZWEIPI = 2.0 * np.pi
V0_RASTER = [0.0, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0]
Q_RASTER = [0, 1, 2]
E_KANTE = -6.0
E_MARGE = 1e-3
R_KERN2 = 72          # (3 Kantenlaengen)^2 = 9 * 8 in (Zellkante/8)^2
W_MIN = 0.9
REL_ENTARTUNG = 1e-8
K_EIG = 16
K_BERICHT = 12
BISEKTION_BREITE = 1e-3
STRING_V0 = [0.0, 4.0, 12.0]
STRINGS = {'s1': (1.0, 0.31, 0.17), 's2': (-0.23, 1.0, 0.41), 's3': (0.37, -0.53, -1.0)}
HAUPT = 's1'
F_FCC = np.array([[0, 0, 0], [0, 4, 4], [4, 0, 4], [4, 4, 0]])
B_PYR = np.array([[0, 0, 0], [0, 2, 2], [2, 0, 2], [2, 2, 0]])
D_PYR = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
MITTE = np.array([1, 1, 1])
NN = np.array([v for v in itertools.product((-2, 0, 2), repeat=3) if sorted(abs(x) for x in v) == [0, 2, 2]])
OMEGA = np.exp(2j * np.pi / 3)

# Drehungen um die Tetraedermitte (eigentlich, Gruppe T) und eine Spiegelung (nur antiunitaer eine Symmetrie)
ROT = {
    'Rx': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),   # pi um x
    'Ry': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),   # pi um y
    'C3': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),     # 2 pi/3 um (1,1,1): x -> y -> z
}
SIGMA_D = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])      # Spiegelung x <-> y (kehrt den Monopol um)


def raumwinkel_dreieck(r1, r2, r3):
    """Van Oosterom-Strackee: vorzeichenbehafteter Raumwinkel des Dreiecks (r1, r2, r3) vom Ursprung."""
    r1, r2, r3 = np.atleast_2d(r1), np.atleast_2d(r2), np.atleast_2d(r3)
    n1 = np.linalg.norm(r1, axis=1)
    n2 = np.linalg.norm(r2, axis=1)
    n3 = np.linalg.norm(r3, axis=1)
    zaehler = np.einsum('ij,ij->i', r1, np.cross(r2, r3))
    nenner = (n1 * n2 * n3 + np.einsum('ij,ij->i', r1, r2) * n3
              + np.einsum('ij,ij->i', r1, r3) * n2 + np.einsum('ij,ij->i', r2, r3) * n1)
    return 2.0 * np.arctan2(zaehler, nenner)


# ----------------------------------------------------------------------------------------------
# Gitter und Zellkomplex
# ----------------------------------------------------------------------------------------------
class Gitter:
    def __init__(self, L):
        self.L = L
        h = 4 * L
        m = L // 2 + 2
        zellen = np.array(list(itertools.product(range(-m, m + 1), repeat=3)))
        fcc = (zellen[:, None, :] * 8 + F_FCC[None, :, :]).reshape(-1, 3)
        self.fcc_rel = fcc          # Mitten der oberen Tetraeder (relativ zum Monopol); untere: fcc - (2,2,2)
        ecken = np.unique((fcc[:, None, :] + B_PYR[None, :, :]).reshape(-1, 3) - MITTE, axis=0)
        ecken = ecken[np.all(np.abs(ecken) <= h, axis=1)]
        self.pos = ecken.astype(np.int64)
        self.N = len(ecken)
        self.idx = {tuple(p): i for i, p in enumerate(self.pos.tolist())}
        self.r2 = np.sum(self.pos ** 2, axis=1)
        self.kern = np.zeros(self.N, bool)
        self.kern_idx = []
        for d in D_PYR:
            i = self.idx[tuple((-d).tolist())]
            self.kern[i] = True
            self.kern_idx.append(i)
        self.innen = self.r2 <= R_KERN2
        kf, kt = [], []
        nb = [[] for _ in range(self.N)]
        for i, p in enumerate(self.pos.tolist()):
            for v in NN.tolist():
                j = self.idx.get((p[0] + v[0], p[1] + v[1], p[2] + v[2]))
                if j is not None:
                    nb[i].append(j)
                    if j > i:
                        kf.append(i)
                        kt.append(j)
        self.nb = nb
        self.kf = np.array(kf)
        self.kt = np.array(kt)
        self.nk = len(kf)
        self.kante = {(a, b): e for e, (a, b) in enumerate(zip(kf, kt))}
        self.grad = np.array([len(x) for x in nb])
        self._komplex()

    def _komplex(self):
        P = self.pos
        fv, ftyp, fm3, fminus, fplus = [], [], [], [], []
        self.tet_ecken = {}
        for f in self.fcc_rel:
            for c, sg in ((f, -1), (f - 2, 1)):
                e = [self.idx.get(tuple((c + sg * d).tolist())) for d in D_PYR]
                da = [x for x in e if x is not None]
                if len(da) < 3:
                    continue
                key = ('T',) + tuple((3 * c).tolist())
                if len(da) == 4:
                    self.tet_ecken[key] = e
                for a, b, cc in itertools.combinations(da, 3):
                    s3 = P[a] + P[b] + P[cc]
                    n = s3 - 3 * c
                    N_ = np.cross(P[b] - P[a], P[cc] - P[a])
                    if N_ @ n < 0:
                        b, cc = cc, b
                    fv.append([a, b, cc])
                    ftyp.append(3)
                    fm3.append(s3)
                    fminus.append(key)
                    fplus.append(('S',) + tuple((s3 + 5 * n).tolist()))
        # Kagome-Sechsecke: an Ecke i Nachbarn j, k aus verschiedenen Tetraedern unter 120 Grad, Mitte x_j + x_k - x_i
        hexe = {}
        for i in range(self.N):
            for j, k in itertools.combinations(self.nb[i], 2):
                u, w = P[j] - P[i], P[k] - P[i]
                if u @ w != -4:
                    continue
                c = P[j] + P[k] - P[i]
                n = np.sign(np.cross(u, w)).astype(np.int64)
                if n[0] < 0:
                    n = -n
                hexe[tuple(c.tolist()) + tuple(n.tolist())] = True
        self.hex_eben_max = 0.0
        self.hex_unvollstaendig = 0
        for key in hexe:
            c = np.array(key[:3])
            n = np.array(key[3:])
            vs = [v for v in NN if v @ n == 0]
            e1 = vs[0].astype(float)
            e2 = np.cross(n, e1).astype(float)
            vs.sort(key=lambda v: np.arctan2(v @ e2, v @ e1))
            verts = [self.idx.get(tuple((c + v).tolist())) for v in vs]
            if any(x is None for x in verts):
                self.hex_unvollstaendig += 1
                continue
            X = P[verts].astype(float)
            N_ = np.cross(X[1] - X[0], X[2] - X[0])
            if N_ @ n < 0:
                verts = verts[::-1]
            nn = n / np.linalg.norm(n)
            self.hex_eben_max = max(self.hex_eben_max, float(np.max(np.abs((X - X.mean(0)) @ nn))))
            fv.append(verts)
            ftyp.append(6)
            fm3.append(3 * c)
            fminus.append(('S',) + tuple((3 * c - 3 * n).tolist()))
            fplus.append(('S',) + tuple((3 * c + 3 * n).tolist()))
        self.fv = fv
        self.ftyp = np.array(ftyp)
        self.fm3 = np.array(fm3)
        self.fminus = fminus
        self.fplus = fplus
        self.nf = len(fv)
        # Inzidenzmatrix Flaeche x Kante (orientiert)
        rows, cols, vals = [], [], []
        for fi, vs in enumerate(fv):
            m = len(vs)
            for t in range(m):
                a, b = vs[t], vs[(t + 1) % m]
                e = self.kante.get((a, b))
                if e is not None:
                    rows.append(fi); cols.append(e); vals.append(1.0)
                else:
                    e = self.kante[(b, a)]
                    rows.append(fi); cols.append(e); vals.append(-1.0)
        self.D = sp.csr_matrix((vals, (rows, cols)), shape=(self.nf, self.nk))
        # Zellen: Schluessel -> [(Flaeche, sigma)], sigma = +1, wenn die Normale aus der Zelle herauszeigt
        zellen = {}
        for fi in range(self.nf):
            zellen.setdefault(self.fminus[fi], []).append((fi, 1))
            zellen.setdefault(self.fplus[fi], []).append((fi, -1))
        voll = {}
        for key, lst in zellen.items():
            if key[0] == 'T' and key in self.tet_ecken and len(lst) == 4:
                voll[key] = lst
            elif key[0] == 'S' and len(lst) == 8:
                voll[key] = lst
        self.zellen = voll
        self.monopolzelle = ('T', 0, 0, 0)
        assert self.monopolzelle in voll

    def pruefungen(self):
        P = self.pos
        pr = {'N': int(self.N), 'kanten': int(self.nk), 'flaechen': int(self.nf),
              'dreiecke': int(np.sum(self.ftyp == 3)), 'sechsecke': int(np.sum(self.ftyp == 6)),
              'zellen': len(self.zellen),
              'tetraeder': sum(1 for k in self.zellen if k[0] == 'T'),
              'stumpftetraeder': sum(1 for k in self.zellen if k[0] == 'S'),
              'grad_min_max': [int(self.grad.min()), int(self.grad.max())],
              'sechseck_eben_max': self.hex_eben_max,
              'sechsecke_unvollstaendig_verworfen': int(self.hex_unvollstaendig)}
        pr['euler'] = int(self.N - self.nk + self.nf - len(self.zellen))
        ncomp, _ = connected_components(sp.csr_matrix((np.ones(self.nk), (self.kf, self.kt)),
                                                      shape=(self.N, self.N)), directed=False)
        pr['zusammenhang'] = int(ncomp)
        # Rand der Flaechen geschlossen (D: jede Flaeche ist ein Zyklus): Summe der Inzidenzen je Ecke
        # Zellen: Rand der Zelle ist geschlossen (sum_f sigma D_f = 0) und Ecken liegen auf der Umkugel
        keys = list(self.zellen)
        r_, c_, v_ = [], [], []
        for ci, key in enumerate(keys):
            for fi, sg in self.zellen[key]:
                r_.append(ci); c_.append(fi); v_.append(float(sg))
        C = sp.csr_matrix((v_, (r_, c_)), shape=(len(keys), self.nf))
        Z = (C @ self.D).tocsr()
        rand_max = float(np.max(np.abs(Z.data))) if Z.nnz else 0.0
        umkugel_ok = True
        for key, lst in self.zellen.items():
            c3 = np.array(key[1:])
            ecken = set(v for fi, _ in lst for v in self.fv[fi])
            d2 = {int(np.sum((3 * P[v] - c3) ** 2)) for v in ecken}
            soll = (27, 4) if key[0] == 'T' else (99, 12)
            if d2 != {soll[0]} or len(ecken) != soll[1]:
                umkugel_ok = False
        pr['zellrand_max'] = rand_max
        pr['zellen_ecken_umkugel_ok'] = bool(umkugel_ok)
        # Inzidenz im Inneren: jede Flaeche mit Mitte mindestens eine Zellkante vom Rand liegt in genau zwei vollen Zellen
        h3 = 3 * (4 * self.L - 8)
        innen = np.all(np.abs(self.fm3) <= h3, axis=1)
        zwei = [(self.fminus[fi] in self.zellen) and (self.fplus[fi] in self.zellen) for fi in range(self.nf)]
        pr['innen_flaechen'] = int(np.sum(innen))
        pr['innen_flaechen_in_zwei_zellen'] = int(np.sum(np.array(zwei) & innen))
        # Flaechen je Kante (innen: 2 Dreiecke + 2 Sechsecke)
        pr['kante_in_flaechen_min_max'] = [int(np.diff(self.D.tocsc().indptr).min()),
                                           int(np.diff(self.D.tocsc().indptr).max())]
        return pr

    def zentren(self):
        return self.fm3 / 3.0


def fluss(G):
    """Phi_f = Omega_f / 2; Dreiecke direkt, Sechsecke als Faecher (Schwerpunkt + 6 Dreiecke), orientiert wie gespeichert."""
    X = G.pos.astype(float)
    phi = np.zeros(G.nf)
    tri = np.nonzero(G.ftyp == 3)[0]
    T = np.array([G.fv[i] for i in tri])
    phi[tri] = 0.5 * raumwinkel_dreieck(X[T[:, 0]], X[T[:, 1]], X[T[:, 2]])
    hx = np.nonzero(G.ftyp == 6)[0]
    if len(hx):
        Hh = np.array([G.fv[i] for i in hx])
        c = X[Hh].mean(1)
        om = np.zeros(len(hx))
        for t in range(6):
            om += raumwinkel_dreieck(c, X[Hh[:, t]], X[Hh[:, (t + 1) % 6]])
        phi[hx] = 0.5 * om
    return phi


def divergenz(G, F):
    """Auswaerts-Summe von F ueber die Flaechen jeder vollen Zelle."""
    return {key: float(sum(sg * F[fi] for fi, sg in lst)) for key, lst in G.zellen.items()}


def string_weg(G, richtung):
    """Gieriger Weg durch volle Zellen vom Monopol-Tetraeder bis zu einer Flaeche am Rand; n_f = sigma."""
    d = np.array(richtung, float)
    d /= np.linalg.norm(d)
    n = np.zeros(G.nf)
    X = G.monopolzelle
    besucht = {X}
    weg = []
    mitten = G.zentren()
    for _ in range(100000):
        cx = np.array(X[1:], float) / 3.0
        best = None
        for fi, sg in G.zellen[X]:
            andere = G.fplus[fi] if sg == 1 else G.fminus[fi]
            if andere in besucht:
                continue
            wert = (mitten[fi] - cx) @ d
            if best is None or wert > best[0]:
                best = (wert, fi, sg, andere)
        if best is None:
            raise RuntimeError('String: Sackgasse')
        _, fi, sg, andere = best
        n[fi] = sg
        weg.append(int(fi))
        if andere not in G.zellen:
            return n, weg
        besucht.add(andere)
        X = andere
    raise RuntimeError('String: kein Ende')


def eichfeld(G, F):
    t0 = time.time()
    erg = spla.lsqr(G.D, F, atol=1e-15, btol=1e-15, conlim=1e14, iter_lim=50000)
    A = erg[0]
    iters = [int(erg[2])]
    for _ in range(3):
        res = G.D @ A - F
        if np.max(np.abs(res)) <= 1e-12:
            break
        e2 = spla.lsqr(G.D, -res, atol=1e-15, btol=1e-15, conlim=1e14, iter_lim=50000)
        A = A + e2[0]
        iters.append(int(e2[2]))
    res = G.D @ A - F
    return A, float(np.max(np.abs(res))), iters, time.time() - t0


# ----------------------------------------------------------------------------------------------
# Hamilton, Spektrum, Stufen
# ----------------------------------------------------------------------------------------------
def hueppfen(G, A, q):
    ph = np.exp(1j * q * A)
    K = sp.coo_matrix((np.concatenate([ph, np.conj(ph)]),
                       (np.concatenate([G.kf, G.kt]), np.concatenate([G.kt, G.kf]))),
                      shape=(G.N, G.N)).tocsr()
    K.sort_indices()
    return K


def hamilton(G, K, V0):
    return (-K - V0 * sp.diags(G.kern.astype(float))).tocsr()


def spektrum(H, k=K_EIG, seed=0, ncv=None):
    N = H.shape[0]
    rng = np.random.default_rng(1000 + seed)
    v0 = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    if ncv is None:
        ncv = min(N - 1, 64)
    t0 = time.time()
    w, V = spla.eigsh(H, k=k, which='SA', tol=0, ncv=ncv, v0=v0, maxiter=200000)
    o = np.argsort(w)
    return w[o], V[:, o], time.time() - t0


def stufen(w):
    gr = []
    a = 0
    for i in range(1, len(w)):
        if abs(w[i] - w[i - 1]) > REL_ENTARTUNG * max(abs(w[i]), abs(w[i - 1])):
            gr.append((a, i))
            a = i
    gr.append((a, len(w)))
    return gr


RANG_TOL = 1e-6   # nach dem Einfrieren von 1e-8 angehoben: Rauschverstaerkung in der Vervollstaendigung (ERGEBNIS, Selbstanzeige)
RES_TOL = 1e-6


def orth(Z):
    U, s, _ = np.linalg.svd(Z, full_matrices=False)
    if s.size == 0 or s[0] == 0:
        return Z[:, :0]
    return U[:, :int(np.sum(s > RANG_TOL * s[0]))]


def vervollstaendigen(H, w0, V0_, ops, k):
    """Je eigsh-Stufe den Raum unter allen Symmetrien (auch der antiunitaeren) abschliessen, vereinigen, Rayleigh-Ritz."""
    bloecke = []
    for (a, b) in stufen(w0):
        S = orth(V0_[:, a:b])
        for _ in range(8):
            S_neu = orth(np.hstack([S] + [U.an(S) for U in ops]))
            if S_neu.shape[1] <= S.shape[1]:
                break
            S = S_neu
        bloecke.append(S)
    Q = orth(np.hstack(bloecke))
    Hs = Q.conj().T @ (H @ Q)
    Hs = 0.5 * (Hs + Hs.conj().T)
    ew, ev = np.linalg.eigh(Hs)
    V = Q @ ev
    res = np.linalg.norm(H @ V - V * ew, axis=0) / np.maximum(1.0, np.abs(ew))
    gut = res <= RES_TOL
    ew, V, res = ew[gut], V[:, gut], res[gut]
    info = {'w_roh': [float(x) for x in w0], 'n_raum': int(Q.shape[1]), 'verworfen': int(np.sum(~gut)),
            'ergaenzt': int(Q.shape[1] - len(w0))}
    ew, V, res = ew[:k], V[:, :k], res[:k]
    info['res_max'] = float(np.max(res)) if res.size else None
    return ew, V, info


def eigen(H, rots, k=K_EIG, seed=0, ncv=None):
    w0, V0_, dt = spektrum(H, k=k, seed=seed, ncv=ncv)
    w, V, info = vervollstaendigen(H, w0, V0_, list(rots.values()), k)
    info['sek'] = dt
    return w, V, info


class Drehung:
    """U_R = D_g P_R (unitaer) bzw. A = D_g P_R K (antiunitaer, K komplexe Konjugation); (P_R v)(x) = v(R^-1 x)."""

    def __init__(self, G, K, R, anti=False):
        N = G.N
        J = G.pos @ R
        self.perm = np.array([G.idx[tuple(t)] for t in J.tolist()])
        self.perm_inv = np.empty(N, int)
        self.perm_inv[self.perm] = np.arange(N)
        self.anti = anti
        P = sp.csr_matrix((np.ones(N), (np.arange(N), self.perm)), shape=(N, N))
        KR = (P @ (K.conj() if anti else K) @ P.T).tocsr()
        KR.sort_indices()
        ratio = K.multiply(KR.conj()).tocsr()
        assert ratio.nnz == K.nnz, 'Drehung bildet Kanten nicht auf Kanten ab'
        muster = sp.csr_matrix((np.ones(K.nnz), K.indices, K.indptr), shape=K.shape)
        order, pred = breadth_first_order(muster, 0, directed=False, return_predecessors=True)
        assert len(order) == N
        rc = ratio.tocoo()
        d = dict(zip(zip(rc.row.tolist(), rc.col.tolist()), rc.data.tolist()))
        g = np.zeros(N, complex)
        g[order[0]] = 1.0
        for j in order[1:]:
            i = pred[j]
            g[j] = np.conj(d[(int(i), int(j))]) * g[i]
        self.g = g
        diff = (sp.diags(g) @ KR @ sp.diags(np.conj(g)) - K).tocsr()
        self.defekt = float(np.max(np.abs(diff.data))) if diff.nnz else 0.0

    def an(self, V):
        W = np.conj(V) if self.anti else V
        if W.ndim == 2:
            return self.g[:, None] * W[self.perm]
        return self.g * W[self.perm]

    def inv(self, W):
        assert not self.anti
        if W.ndim == 2:
            return (np.conj(self.g)[:, None] * W)[self.perm_inv]
        return (np.conj(self.g) * W)[self.perm_inv]


def c3_normieren(G, U, q):
    """Physikalische Phasenwahl (PLAN 1.4): Produkt der Phasen an den innersten Fixecken beiderseits des Monopols = 1
    und U^3 = (-1)^q. Gibt die Fixpunkt-Phasen vor und nach der Normierung zurueck."""
    fix = [i for i in range(G.N) if U.perm[i] == i]
    t = {i: int(G.pos[i, 0]) for i in fix}
    assert all(G.pos[i, 0] == G.pos[i, 1] == G.pos[i, 2] for i in fix)
    minus = max((i for i in fix if t[i] < 0), key=lambda i: t[i])
    plus = min((i for i in fix if t[i] > 0), key=lambda i: t[i])
    gm, gp = U.g[minus], U.g[plus]
    c = np.sqrt(gm * gp)
    if abs((gm / c) ** 3 - (-1) ** q) > 1e-6:
        c = -c
    U.g = U.g / c
    return {'fix_t': [t[i] for i in sorted(fix, key=lambda i: t[i])],
            'fix_phase_grad': [float(np.degrees(np.angle(U.g[i]))) for i in sorted(fix, key=lambda i: t[i])],
            'g_minus_grad': float(np.degrees(np.angle(U.g[minus]))),
            'g_plus_grad': float(np.degrees(np.angle(U.g[plus]))),
            'verhaeltnis_minus_plus_grad': float(np.degrees(np.angle(U.g[minus] / U.g[plus]))),
            'kubik_minus_abw': float(abs(U.g[minus] ** 3 - (-1) ** q))}


def drehungen(G, K, q):
    rots = {nm: Drehung(G, K, R) for nm, R in ROT.items()}
    rots['Asd'] = Drehung(G, K, SIGMA_D, anti=True)
    norm = c3_normieren(G, rots['C3'], q)
    return rots, {nm: U.defekt for nm, U in rots.items()}, norm


def kommutator(rots, V):
    Ux, Uy = rots['Rx'], rots['Ry']
    return Ux.an(Uy.an(Ux.inv(Uy.inv(V))))


def operator_tests(G, rots, seed=7):
    rng = np.random.default_rng(seed)
    v = rng.standard_normal(G.N) + 1j * rng.standard_normal(G.N)
    out = {}
    for nm, f in (('kommutator', lambda x: kommutator(rots, x)),
                  ('C3_hoch3', lambda x: rots['C3'].an(rots['C3'].an(rots['C3'].an(x)))),
                  ('Rx_quadrat', lambda x: rots['Rx'].an(rots['Rx'].an(x))),
                  ('Asd_quadrat', lambda x: rots['Asd'].an(rots['Asd'].an(x)))):
        w = f(v)
        c = np.vdot(v, w) / np.vdot(v, v)
        out[nm] = {'c_re': float(c.real), 'c_im': float(c.imag),
                   'rest': float(np.linalg.norm(w - c * v) / np.linalg.norm(v))}
    return out


def zaehle(ew, ziele, tol=1e-6):
    n = [0] * len(ziele)
    rest = 0
    for x in ew:
        d = [abs(x - z) for z in ziele]
        j = int(np.argmin(d))
        if d[j] <= tol:
            n[j] += 1
        else:
            rest += 1
    return n, rest


def etikett(q, ew_c3, chi_rx_abs):
    """Darstellung der Doppelgruppe 2T aus den C3-Eigenwerten (physikalische Phasenwahl).
    q ungerade: G4 = {e^{i pi/3}, e^{-i pi/3}} (j=1/2-artig), G5 = {-1, e^{i pi/3}}, G6 = {-1, e^{-i pi/3}} (G5+G6 = F_3/2).
    q gerade: A = {1}, E1 = {omega}, E2 = {omega^2}, T = {1, omega, omega^2} mit |chi(Rx)| = 1."""
    if q % 2:
        (na, nb, nc), rest = zaehle(ew_c3, [np.exp(1j * np.pi / 3), np.exp(-1j * np.pi / 3), -1.0])
        n4, n5, n6 = (na + nb - nc), (na - nb + nc), (nb + nc - na)
        if rest or any(x % 2 or x < 0 for x in (n4, n5, n6)):
            return 'unklar', [na, nb, nc, rest]
        n4, n5, n6 = n4 // 2, n5 // 2, n6 // 2
        return '+'.join(['G4'] * n4 + ['G5'] * n5 + ['G6'] * n6), [na, nb, nc, rest]
    (n1, nw, nw2), rest = zaehle(ew_c3, [1.0, OMEGA, OMEGA ** 2])
    if rest:
        return 'unklar', [n1, nw, nw2, rest]
    m = n1 + nw + nw2
    nT = min(n1, nw, nw2)
    # T gegen A+E1+E2: |chi(Rx)| = nT * 1 (T: chi(C2) = -1) bzw. 3 nT (Einzelne: chi = +1); nur der reine Fall wird benannt
    if m == 3 and nT == 1:
        if abs(chi_rx_abs - 1.0) < 1e-6:
            return 'T', [n1, nw, nw2, rest]
        if abs(chi_rx_abs - 3.0) < 1e-6:
            return 'A+E1+E2', [n1, nw, nw2, rest]
        return 'unklar', [n1, nw, nw2, rest]
    if m == 1:
        return ['A', 'E1', 'E2'][[n1, nw, nw2].index(1)], [n1, nw, nw2, rest]
    if m == 2 and nw == 1 and nw2 == 1:
        return 'E1+E2', [n1, nw, nw2, rest]
    return 'gemischt', [n1, nw, nw2, rest]


def analyse(G, w, V, rots, q):
    out = []
    for (a, b) in stufen(w):
        m = b - a
        Vs = V[:, a:b]
        E = float(np.mean(w[a:b]))
        gew = float(np.sum(np.abs(Vs[G.innen]) ** 2) / m)
        geb = bool((E < E_KANTE - E_MARGE) and (gew >= W_MIN))
        info = {'a': int(a), 'm': int(m), 'E': E, 'spanne': float(w[b - 1] - w[a]), 'gewicht': gew,
                'gebunden': geb, 'voll': bool(b < len(w))}
        if rots is not None:
            CV = kommutator(rots, Vs)
            s = np.trace(Vs.conj().T @ CV) / m
            info['s_re'] = float(s.real)
            info['s_im'] = float(s.imag)
            rest = 0.0
            for nm, U in rots.items():
                W = U.an(Vs)
                M = Vs.conj().T @ W
                rest = max(rest, float(np.max(np.abs(W - Vs @ M))))
                if nm == 'C3':
                    ew = np.linalg.eigvals(M)
                    chi = np.trace(M)
                    info['chi_c3_re'] = float(chi.real)
                    info['chi_c3_im'] = float(chi.imag)
                    info['c3_ew_grad'] = sorted(float(np.degrees(np.angle(x))) for x in ew)
                    ew_c3 = ew
                if nm == 'Rx':
                    info['chi_rx_abs'] = float(abs(np.trace(M)))
            info['sym_rest'] = rest
            et, zahl = etikett(q, ew_c3, info['chi_rx_abs'])
            info['etikett'] = et
            info['c3_zaehlung'] = zahl
        out.append(info)
    return out


def tiefste_gebundene(stf):
    for s in stf:
        if s['gebunden'] and s['voll']:
            return s
    return None


def k4_schreibtisch(G, K, rots, q):
    """Grenzfall tiefer Topf: nur die 4 Kernecken (K4 mit Fluss q pi/2 je Dreieck)."""
    ki = G.kern_idx
    Hk = -K[ki][:, ki].toarray()
    ew, ev = np.linalg.eigh(Hk)
    stf = []
    for (a, b) in stufen(ew):
        V = np.zeros((G.N, b - a), complex)
        V[ki, :] = ev[:, a:b]
        W = rots['C3'].an(V)
        M = V.conj().T @ W
        e3 = np.linalg.eigvals(M)
        Wx = rots['Rx'].an(V)
        chi_rx = abs(np.trace(V.conj().T @ Wx))
        et, zahl = etikett(q, e3, chi_rx)
        stf.append({'E': float(np.mean(ew[a:b])), 'm': int(b - a), 'etikett': et,
                    'c3_ew_grad': sorted(float(np.degrees(np.angle(x))) for x in e3),
                    'abgeschlossen': float(np.max(np.abs(W - V @ M)))})
    return stf


# ----------------------------------------------------------------------------------------------
# Aufbau je L
# ----------------------------------------------------------------------------------------------
def aufbau(L, strings=(HAUPT,)):
    t0 = time.time()
    G = Gitter(L)
    geo = {'L': L, 'pruef': G.pruefungen(), 'sek_gitter': time.time() - t0}
    phi = fluss(G)
    div = divergenz(G, phi)
    mz = G.monopolzelle
    geo['fluss'] = {'zelle_aussen_max': float(max(abs(v) for k, v in div.items() if k != mz)),
                    'monopolzelle_minus_2pi': float(div[mz] - ZWEIPI),
                    'phi_betrag_max': float(np.max(np.abs(phi))),
                    'monopol_dreiecke_minus_pi_halbe': float(max(abs(phi[fi] * sg - np.pi / 2)
                                                                 for fi, sg in G.zellen[mz]))}
    A = {}
    geo['eich'] = {}
    for nm in strings:
        n, weg = string_weg(G, STRINGS[nm])
        F = phi - ZWEIPI * n
        divF = divergenz(G, F)
        Ar, rest, iters, dt = eichfeld(G, F)
        A[nm] = Ar
        geo['eich'][nm] = {'schliessung_max': float(max(abs(v) for v in divF.values())), 'rest_max': rest,
                           'lsqr_iter': iters, 'sek': dt, 'string_flaechen': len(weg),
                           'string_sechsecke': int(sum(1 for f in weg if G.ftyp[f] == 6))}
    return G, phi, A, geo


def json_schreiben(pfad, obj):
    with open(pfad, 'w') as f:
        json.dump(obj, f, indent=1)


def kopf(modus, args):
    return {'modus': modus, 'args': vars(args), 'numpy': np.__version__, 'scipy': scipy.__version__,
            'start_utc': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}


def punkt(G, K, rots, q, V0, seed=0, ncv=None):
    H = hamilton(G, K, V0)
    w, V, info = eigen(H, rots, seed=seed, ncv=ncv)
    return {'V0': V0, 'w': [float(x) for x in w], 'eig': info, 'stufen': analyse(G, w, V, rots, q)}


def modus_gitter(args, rauch=False):
    out = kopf('rauch' if rauch else 'gitter', args)
    out['laengen'] = {}
    for L in args.L:
        t0 = time.time()
        G, phi, A, geo = aufbau(L, tuple(STRINGS))
        res = {'geo': geo, 'q': {}}
        v0_liste = STRING_V0 if rauch else V0_RASTER
        for q in Q_RASTER:
            K = hueppfen(G, A[HAUPT], q)
            rots, defekte, norm = drehungen(G, K, q)
            qd = {'defekte': defekte, 'c3_normierung': norm, 'operator': operator_tests(G, rots),
                  'k4': k4_schreibtisch(G, K, rots, q), 'punkte': [], 'string': [], 'dicht': []}
            for V0 in v0_liste:
                qd['punkte'].append(punkt(G, K, rots, q, V0))
            for nm in STRINGS:
                if nm == HAUPT:
                    continue
                Kr = hueppfen(G, A[nm], q)
                rots_r, def_r, _ = drehungen(G, Kr, q)
                for V0 in STRING_V0:
                    ref = next(p for p in qd['punkte'] if p['V0'] == V0)['w']
                    wr, _, inf = eigen(hamilton(G, Kr, V0), rots_r)
                    d = float(np.max(np.abs(np.array(wr[:K_BERICHT]) - np.array(ref[:K_BERICHT]))))
                    qd['string'].append({'V0': V0, 'string': nm, 'max_diff': d, 'defekte': def_r,
                                         'ergaenzt': inf['ergaenzt']})
            if L == args.dicht:
                for V0 in v0_liste:
                    t1 = time.time()
                    wd = np.linalg.eigvalsh(hamilton(G, K, V0).toarray())[:K_EIG]
                    ref = next(p for p in qd['punkte'] if p['V0'] == V0)['w']
                    qd['dicht'].append({'V0': V0, 'max_diff': float(np.max(np.abs(wd - np.array(ref)))),
                                        'stufen_dicht': [b - a for a, b in stufen(wd)],
                                        'stufen_eigsh': [b - a for a, b in stufen(np.array(ref))],
                                        'w_dicht': [float(x) for x in wd], 'sek': time.time() - t1})
            res['q'][str(q)] = qd
        res['sek'] = time.time() - t0
        out['laengen'][str(L)] = res
    if rauch:
        t0 = time.time()
        G, phi, A, geo = aufbau(args.zeitprobe, (HAUPT,))
        K = hueppfen(G, A[HAUPT], 1)
        rots, defekte, norm = drehungen(G, K, 1)
        p = punkt(G, K, rots, 1, 4.0)
        out['zeitprobe'] = {'geo': geo, 'defekte': defekte, 'norm': norm, 'punkt': p,
                            'sek_gesamt': time.time() - t0}
    out['ende_utc'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    json_schreiben(args.aus, out)


def gebunden_bei(G, K, rots, q, V0, kriterium):
    H = hamilton(G, K, V0)
    w, V, info = eigen(H, rots)
    stf = analyse(G, w, V, None, q)
    if kriterium == 'karte':
        t = tiefste_gebundene(stf)
        return t is not None, t, w
    return bool(w[0] < E_KANTE - E_MARGE), stf[0], w


def klammer(raster):
    lo = max([v for v, g in raster if not g], default=None)
    hi = min([v for v, g in raster if g and (lo is None or v > lo)], default=None)
    return lo, hi


def modus_schwelle(args):
    out = kopf('schwelle', args)
    gitter = [json.load(open(p)) for p in args.ein.split(',') if p]
    raster_k, raster_e = {}, {}
    for gj in gitter:
        for Ls, res in gj['laengen'].items():
            for qs, qd in res['q'].items():
                key = (int(Ls), int(qs))
                raster_k[key] = [(p['V0'], tiefste_gebundene(p['stufen']) is not None) for p in qd['punkte']]
                raster_e[key] = [(p['V0'], bool(p['w'][0] < E_KANTE - E_MARGE)) for p in qd['punkte']]
    out['ergebnis'] = {}
    for L in args.L:
        G, phi, A, geo = aufbau(L, (HAUPT,))
        for q in args.q:
            K = hueppfen(G, A[HAUPT], q)
            rots, _, _ = drehungen(G, K, q)
            eintrag = {'L': L, 'q': q}
            for krit, raster in (('karte', raster_k[(L, q)]), ('energie', raster_e[(L, q)])):
                flags = [g for _, g in raster]
                monoton = all((not flags[i]) or flags[i + 1] for i in range(len(flags) - 1))
                lo, hi = klammer(raster)
                erweitert = False
                if lo is not None and hi is None:
                    v = 12.0
                    while v < 48.0 and hi is None:
                        v *= 2.0
                        b, _, _ = gebunden_bei(G, K, rots, q, v, krit)
                        erweitert = True
                        if b:
                            hi = v
                        else:
                            lo = v
                if lo is None or hi is None:
                    eintrag[krit] = {'raster': raster, 'monoton': monoton, 'lo': lo, 'hi': hi, 'V0c': None,
                                     'erweitert': erweitert}
                    continue
                schritte = 0
                t0 = time.time()
                while hi - lo > BISEKTION_BREITE:
                    mid = 0.5 * (lo + hi)
                    b, _, _ = gebunden_bei(G, K, rots, q, mid, krit)
                    if b:
                        hi = mid
                    else:
                        lo = mid
                    schritte += 1
                b, t, w = gebunden_bei(G, K, rots, q, hi, krit)
                b2, t2, w2 = gebunden_bei(G, K, rots, q, lo, krit)
                eintrag[krit] = {'raster': raster, 'monoton': monoton, 'erweitert': erweitert,
                                 'lo': lo, 'hi': hi, 'V0c': 0.5 * (lo + hi), 'schritte': schritte,
                                 'sek': time.time() - t0, 'oben_gebunden': b, 'oben_stufe': t,
                                 'oben_w': [float(x) for x in w[:K_BERICHT]], 'unten_gebunden': b2,
                                 'unten_w': [float(x) for x in w2[:K_BERICHT]]}
            out['ergebnis'][f'{L}_{q}'] = eintrag
    out['zweitlauf'] = []
    if args.zweit:
        Lz = max(args.L)
        G, phi, A, geo = aufbau(Lz, (HAUPT,))
        for q in [x for x in (1, 2) if x in args.q]:
            K = hueppfen(G, A[HAUPT], q)
            rots, _, _ = drehungen(G, K, q)
            V0c = out['ergebnis'].get(f'{Lz}_{q}', {}).get('karte', {}).get('V0c')
            for V0 in V0_RASTER:
                if V0c is not None and V0 > V0c:
                    p = punkt(G, K, rots, q, V0, seed=1, ncv=96)
                    out['zweitlauf'].append({'L': Lz, 'q': q, 'punkt': p})
            hi = out['ergebnis'].get(f'{Lz}_{q}', {}).get('karte', {}).get('hi')
            if hi is not None:
                p = punkt(G, K, rots, q, hi)
                out['zweitlauf'].append({'L': Lz, 'q': q, 'oberes_ende': True, 'punkt': p})
    out['ende_utc'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    json_schreiben(args.aus, out)


def modus_scan(args):
    out = kopf('scan', args)
    out['scan'] = {}
    for L in args.L:
        G, phi, A, geo = aufbau(L, (HAUPT,))
        for q in Q_RASTER:
            K = hueppfen(G, A[HAUPT], q)
            rots, _, _ = drehungen(G, K, q)
            pts = []
            for V0 in np.arange(0.0, 12.0 + 1e-9, args.schritt):
                p = punkt(G, K, rots, q, float(V0))
                pts.append({'V0': float(V0), 'w': p['w'][:K_BERICHT],
                            'stufen': [{k: s[k] for k in ('a', 'm', 'E', 'gewicht', 'gebunden', 'voll', 'etikett',
                                                          's_re', 'sym_rest')} for s in p['stufen']]})
            out['scan'][f'{L}_{q}'] = pts
    out['ende_utc'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    json_schreiben(args.aus, out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'gitter', 'schwelle', 'scan'])
    ap.add_argument('--L', type=int, nargs='+', default=[4])
    ap.add_argument('--aus', required=True)
    ap.add_argument('--ein', default='')
    ap.add_argument('--schritt', type=float, default=0.25)
    ap.add_argument('--zeitprobe', type=int, default=8)
    ap.add_argument('--zweit', action='store_true')
    ap.add_argument('--dicht', type=int, default=4)
    ap.add_argument('--q', type=int, nargs='+', default=Q_RASTER)
    args = ap.parse_args()
    t0 = time.time()
    if args.modus == 'rauch':
        modus_gitter(args, rauch=True)
    elif args.modus == 'gitter':
        modus_gitter(args)
    elif args.modus == 'schwelle':
        modus_schwelle(args)
    else:
        modus_scan(args)
    print(f'fertig {args.modus} L={args.L} in {time.time() - t0:.1f} s -> {args.aus}', flush=True)


if __name__ == '__main__':
    main()
