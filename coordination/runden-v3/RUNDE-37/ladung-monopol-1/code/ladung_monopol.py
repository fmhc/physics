#!/usr/bin/env python3
"""LADUNG-MONOPOL-1 (Runde 38), Teil A.

Spinloses Teilchen der Ladung q auf dem kubischen Gitter (offene Box L^3) um einen kompakten
Gitter-Monopol (Fluss 2 pi im Mittelwuerfel) mit Kern-Topf -V0 auf den 8 Ecken des Mittelwuerfels.

Modi:
  rauch     kleine Probe (L = 12, drei V0) plus Zeitprobe L = 24
  gitter    Raster q x V0 fuer die Laengen aus --L, String-Probe, dichte Gegenprobe (L = 12)
  schwelle  Bisektion V0c je q und L (Kartenkriterium und reines Energiekriterium), Zweitlaeufe
  scan      feines V0-Raster (beschreibend, fuer das Bild)

Nur auf der .69 ueber kleintest.sh starten (Spur p4000a). Ausgabe: JSON unter --aus.
"""
import argparse
import json
import time

import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.sparse.csgraph import breadth_first_order

ZWEIPI = 2.0 * np.pi
V0_RASTER = [0.0, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0]
Q_RASTER = [0, 1, 2]
E_KANTE = -6.0
E_MARGE = 1e-3
R_KERN = 3.0
W_MIN = 0.9
REL_ENTARTUNG = 1e-8
K_EIG = 16          # berechnete Eigenwerte (Stufen, die in den tiefsten 12 beginnen, sind damit vollstaendig)
K_BERICHT = 12      # berichtete tiefste Eigenwerte (Karte)
BISEKTION_BREITE = 1e-3
STRING_V0 = [0.0, 4.0, 12.0]
STRING_RICHTUNGEN = ['+z', '-z', '+x']

# Drehmatrizen (wirken auf Koordinaten relativ zum Wuerfelmittelpunkt)
ROT = {
    'Rx': np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),   # pi um x
    'Ry': np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),   # pi um y
    'C3': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),     # 2 pi/3 um (1,1,1)
    'C4z': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),   # pi/2 um z
}


# ----------------------------------------------------------------------------------------------
# Gitter, Fluss, Eichfeld
# ----------------------------------------------------------------------------------------------
class Gitter:
    def __init__(self, L):
        assert L % 2 == 0, 'L muss gerade sein (Monopol im Mittelwuerfel)'
        self.L = L
        N = L ** 3
        self.N = N
        ar = np.arange(L)
        I = np.stack(np.meshgrid(ar, ar, ar, indexing='ij'), axis=-1).reshape(-1, 3)
        self.I = I
        self.c = (L - 1) / 2.0
        self.pos = I.astype(float) - self.c
        self.r = np.linalg.norm(self.pos, axis=1)
        self.kern = np.all(np.abs(self.pos) == 0.5, axis=1)
        assert int(self.kern.sum()) == 8
        self.innen = self.r <= R_KERN + 1e-9
        # Kanten s -> s + e_mu
        fr, to, mu = [], [], []
        for m in range(3):
            s = np.nonzero(I[:, m] < L - 1)[0]
            e = np.zeros(3, int)
            e[m] = 1
            fr.append(s)
            to.append(self.index(I[s] + e))
            mu.append(np.full(len(s), m))
        self.kf = np.concatenate(fr)
        self.kt = np.concatenate(to)
        self.kmu = np.concatenate(mu)
        self.nk = len(self.kf)
        self.kante_von = -np.ones((3, N), int)
        self.kante_von[self.kmu, self.kf] = np.arange(self.nk)
        # Plaketten mit Normale nu, Ebene (a, b) = ((nu+1)%3, (nu+2)%3), e_a x e_b = e_nu
        pr, pc, pv, pnu, pecke = [], [], [], [], []
        P = 0
        for nu in range(3):
            a, b = (nu + 1) % 3, (nu + 2) % 3
            s = np.nonzero((I[:, a] < L - 1) & (I[:, b] < L - 1))[0]
            ea = np.zeros(3, int)
            ea[a] = 1
            eb = np.zeros(3, int)
            eb[b] = 1
            s_a = self.index(I[s] + ea)
            s_b = self.index(I[s] + eb)
            k1 = self.kante_von[a, s]      # s -> s+ea
            k2 = self.kante_von[b, s_a]    # s+ea -> s+ea+eb
            k3 = self.kante_von[a, s_b]    # s+eb -> s+ea+eb (rueckwaerts durchlaufen)
            k4 = self.kante_von[b, s]      # s -> s+eb (rueckwaerts durchlaufen)
            assert min(k1.min(), k2.min(), k3.min(), k4.min()) >= 0
            n = len(s)
            rows = np.arange(P, P + n)
            pr += [rows] * 4
            pc += [k1, k2, k3, k4]
            pv += [np.ones(n), np.ones(n), -np.ones(n), -np.ones(n)]
            pnu.append(np.full(n, nu))
            pecke.append(s)
            P += n
        self.npl = P
        self.D = sp.csr_matrix((np.concatenate(pv), (np.concatenate(pr), np.concatenate(pc))),
                               shape=(P, self.nk))
        self.pnu = np.concatenate(pnu)
        self.pecke = np.concatenate(pecke)
        self.plak_von = -np.ones((3, N), int)
        self.plak_von[self.pnu, self.pecke] = np.arange(P)

    def index(self, J):
        J = np.atleast_2d(J)
        return (J[:, 0] * self.L + J[:, 1]) * self.L + J[:, 2]


def raumwinkel_dreieck(r1, r2, r3):
    """Van Oosterom-Strackee: vorzeichenbehafteter Raumwinkel des Dreiecks (r1, r2, r3) vom Ursprung."""
    n1 = np.linalg.norm(r1, axis=1)
    n2 = np.linalg.norm(r2, axis=1)
    n3 = np.linalg.norm(r3, axis=1)
    zaehler = np.einsum('ij,ij->i', r1, np.cross(r2, r3))
    nenner = (n1 * n2 * n3 + np.einsum('ij,ij->i', r1, r2) * n3
              + np.einsum('ij,ij->i', r1, r3) * n2 + np.einsum('ij,ij->i', r2, r3) * n1)
    return 2.0 * np.arctan2(zaehler, nenner)


def fluss(G):
    """Phi_p = Omega_p / 2, Omega_p Raumwinkel der Plakette (orientiert nach ihrer Normale) vom Monopol."""
    phi = np.zeros(G.npl)
    for nu in range(3):
        a, b = (nu + 1) % 3, (nu + 2) % 3
        sel = G.pnu == nu
        v1 = G.pos[G.pecke[sel]]
        ea = np.zeros(3)
        ea[a] = 1.0
        eb = np.zeros(3)
        eb[b] = 1.0
        v2 = v1 + ea
        v3 = v1 + ea + eb
        v4 = v1 + eb
        phi[sel] = 0.5 * (raumwinkel_dreieck(v1, v2, v3) + raumwinkel_dreieck(v1, v3, v4))
    return phi


def wuerfelsummen(G, F):
    """Auswaerts-Summe von F ueber die 6 Flaechen jedes Elementarwuerfels; Rueckgabe (Eckindex, Summe)."""
    L = G.L
    s = np.nonzero(np.all(G.I < L - 1, axis=1))[0]
    tot = np.zeros(len(s))
    for nu in range(3):
        e = np.zeros(3, int)
        e[nu] = 1
        s_plus = G.index(G.I[s] + e)
        tot += F[G.plak_von[nu, s_plus]] - F[G.plak_von[nu, s]]
    return s, tot


def string_n(G, richtung):
    """n_p: Plaketten, die der Dirac-String vom Mittelwuerfel zum Rand durchstoesst (Vorzeichen bzgl. +Normale)."""
    L = G.L
    h = L // 2
    n = np.zeros(G.npl)
    if richtung == '+z':
        for iz in range(h, L):
            n[G.plak_von[2, G.index([h - 1, h - 1, iz])[0]]] = 1.0
    elif richtung == '-z':
        for iz in range(0, h):
            n[G.plak_von[2, G.index([h - 1, h - 1, iz])[0]]] = -1.0
    elif richtung == '+x':
        for ix in range(h, L):
            n[G.plak_von[0, G.index([ix, h - 1, h - 1])[0]]] = 1.0
    else:
        raise ValueError(richtung)
    return n


def eichfeld(G, F):
    """A auf den Kanten mit rot A = F (kleinste Quadrate, lsqr, bis zu 3 Nachbesserungen)."""
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
# Hamilton-Operator, Spektrum, Stufen
# ----------------------------------------------------------------------------------------------
def hueppfen(G, A, q):
    """K_ij = exp(i q A_ij) auf jeder Kante (beide Richtungen, A_ji = -A_ij)."""
    ph = np.exp(1j * q * A)
    K = sp.coo_matrix((np.concatenate([ph, np.conj(ph)]),
                       (np.concatenate([G.kf, G.kt]), np.concatenate([G.kt, G.kf]))),
                      shape=(G.N, G.N)).tocsr()
    K.sort_indices()
    return K


def hamilton(G, K, V0):
    return (-K - V0 * sp.diags(G.kern.astype(float))).tocsr()


def spektrum(H, k=K_EIG, seed=0, ncv=None, nur_werte=False):
    N = H.shape[0]
    rng = np.random.default_rng(1000 + seed)
    v0 = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    if ncv is None:
        ncv = min(N - 1, 64)
    t0 = time.time()
    if nur_werte:
        w = spla.eigsh(H, k=k, which='SA', tol=0, ncv=ncv, v0=v0, maxiter=200000,
                       return_eigenvectors=False)
        return np.sort(w), None, time.time() - t0
    w, V = spla.eigsh(H, k=k, which='SA', tol=0, ncv=ncv, v0=v0, maxiter=200000)
    o = np.argsort(w)
    return w[o], V[:, o], time.time() - t0


def stufen(w):
    """Ketten benachbarter Eigenwerte mit relativem Abstand <= 1e-8 (Abstand / max(|E|))."""
    gr = []
    a = 0
    for i in range(1, len(w)):
        if abs(w[i] - w[i - 1]) > REL_ENTARTUNG * max(abs(w[i]), abs(w[i - 1])):
            gr.append((a, i))
            a = i
    gr.append((a, len(w)))
    return gr


RANG_TOL = 1e-8
RES_TOL = 1e-6


def orth(Z):
    U, s, _ = np.linalg.svd(Z, full_matrices=False)
    if s.size == 0 or s[0] == 0:
        return Z[:, :0]
    return U[:, :int(np.sum(s > RANG_TOL * s[0]))]


def vervollstaendigen(H, w0, V0_, rots, k):
    """Symmetrie-Vervollstaendigung und Rayleigh-Ritz.

    eigsh rechnet komplexe hermitesche Matrizen mit dem Arnoldi-Treiber (eigs). Der kann Kopien entarteter Eigenwerte
    verpassen und liefert in entarteten Stufen nicht orthogonale Vektoren (Rauchlauf 1). Darum: je eigsh-Stufe den Raum
    unter U_x, U_y, U_C3, U_C4z abschliessen (U vertauscht mit H, also bleiben es Eigenvektoren), alle Raeume
    vereinigen, orthonormieren und H im vereinigten Raum exakt diagonalisieren. Ritz-Paare mit Residuum > 1e-6 werden
    verworfen (Rauschrichtungen). Die Stufen werden danach wie gehabt aus den Eigenwerten gebildet.
    """
    ops = [rots[n] for n in ('Rx', 'Ry', 'C3', 'C4z')]
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
    HQ = H @ Q
    Hs = Q.conj().T @ HQ
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
    w, V, info = vervollstaendigen(H, w0, V0_, rots, k)
    info['sek'] = dt
    return w, V, info


class Drehung:
    """Magnetische Drehung U_R = D_g P_R mit (P_R v)(x) = v(R^-1 x) und g aus g_i conj(g_j) = K_ij / K^R_ij."""

    def __init__(self, G, K, R):
        N = G.N
        q_ = G.pos @ R                        # Zeilen: R^-1 x (R orthogonal)
        J = np.rint(q_ + G.c).astype(int)
        assert np.max(np.abs(q_ + G.c - J)) < 1e-9 and J.min() >= 0 and J.max() < G.L
        self.perm = G.index(J)
        self.perm_inv = np.empty(N, int)
        self.perm_inv[self.perm] = np.arange(N)
        P = sp.csr_matrix((np.ones(N), (np.arange(N), self.perm)), shape=(N, N))
        KR = (P @ K @ P.T).tocsr()            # KR_ij = K_{R^-1 i, R^-1 j}
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
        if V.ndim == 2:
            return self.g[:, None] * V[self.perm]
        return self.g * V[self.perm]

    def inv(self, W):
        if W.ndim == 2:
            return (np.conj(self.g)[:, None] * W)[self.perm_inv]
        return (np.conj(self.g) * W)[self.perm_inv]


def kommutator(rots, V):
    """C V = U_x U_y U_x^-1 U_y^-1 V."""
    Ux, Uy = rots['Rx'], rots['Ry']
    return Ux.an(Uy.an(Ux.inv(Uy.inv(V))))


def operator_test(G, rots, seed=7):
    rng = np.random.default_rng(seed)
    v = rng.standard_normal(G.N) + 1j * rng.standard_normal(G.N)
    Cv = kommutator(rots, v)
    c = np.vdot(v, Cv) / np.vdot(v, v)
    rest = np.linalg.norm(Cv - c * v) / np.linalg.norm(v)
    return {'c_re': float(c.real), 'c_im': float(c.imag), 'rest': float(rest)}


def analyse(G, w, V, rots):
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
            chi = {}
            for nm, U in rots.items():
                W = U.an(Vs)
                M = Vs.conj().T @ W
                rest = max(rest, float(np.max(np.abs(W - Vs @ M))))
                chi[nm] = float(abs(np.trace(M)))
            info['sym_rest'] = rest
            info['chi_abs'] = chi
        out.append(info)
    return out


def tiefste_gebundene(stf):
    for s in stf:
        if s['gebunden'] and s['voll']:
            return s
    return None


# ----------------------------------------------------------------------------------------------
# Aufbau je L
# ----------------------------------------------------------------------------------------------
def aufbau(L, richtungen=('+z',)):
    G = Gitter(L)
    phi = fluss(G)
    s, tot = wuerfelsummen(G, phi)
    s0 = G.index([L // 2 - 1] * 3)[0]
    zentral = np.nonzero(s == s0)[0][0]
    rest_aussen = float(np.max(np.abs(np.delete(tot, zentral))))
    geo = {'L': L, 'N': G.N, 'kanten': G.nk, 'plaketten': G.npl,
           'wuerfel_aussen_max': rest_aussen,
           'wuerfel_zentral_minus_2pi': float(tot[zentral] - ZWEIPI),
           'phi_betrag_max': float(np.max(np.abs(phi))),
           'phi_max_minus_pi_drittel': float(np.max(np.abs(phi)) - np.pi / 3),
           'eich': {}}
    A = {}
    for r in richtungen:
        n = string_n(G, r)
        F = phi - ZWEIPI * n
        _, totF = wuerfelsummen(G, F)
        Ar, rest, iters, dt = eichfeld(G, F)
        A[r] = Ar
        geo['eich'][r] = {'schliessung_max': float(np.max(np.abs(totF))), 'rest_max': rest,
                          'lsqr_iter': iters, 'sek': dt, 'string_plaketten': int(np.sum(n != 0))}
    return G, phi, A, geo


def drehungen(G, K):
    rots = {nm: Drehung(G, K, R) for nm, R in ROT.items()}
    return rots, {nm: U.defekt for nm, U in rots.items()}


def json_schreiben(pfad, obj):
    with open(pfad, 'w') as f:
        json.dump(obj, f, indent=1, sort_keys=False)


def kopf(modus, args):
    return {'modus': modus, 'args': vars(args), 'numpy': np.__version__, 'scipy': scipy.__version__,
            'start_utc': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}


# ----------------------------------------------------------------------------------------------
# Modi
# ----------------------------------------------------------------------------------------------
def punkt(G, K, rots, V0, seed=0, ncv=None, k=K_EIG):
    H = hamilton(G, K, V0)
    w, V, info = eigen(H, rots, k=k, seed=seed, ncv=ncv)
    stf = analyse(G, w, V, rots)
    return {'V0': V0, 'w': [float(x) for x in w], 'eig': info, 'stufen': stf}


def modus_gitter(args, rauch=False):
    out = kopf('rauch' if rauch else 'gitter', args)
    out['laengen'] = {}
    for L in args.L:
        t0 = time.time()
        G, phi, A, geo = aufbau(L, STRING_RICHTUNGEN)
        res = {'geo': geo, 'q': {}}
        v0_liste = STRING_V0 if rauch else V0_RASTER
        for q in Q_RASTER:
            K = hueppfen(G, A['+z'], q)
            rots, defekte = drehungen(G, K)
            qd = {'defekte': defekte, 'operator': operator_test(G, rots), 'punkte': [], 'string': [],
                  'dicht': []}
            for V0 in v0_liste:
                qd['punkte'].append(punkt(G, K, rots, V0))
            # String-Richtung: Spektrum fuer -z und +x gegen +z
            for r in ('-z', '+x'):
                Kr = hueppfen(G, A[r], q)
                rots_r, def_r = drehungen(G, Kr)
                for V0 in STRING_V0:
                    ref = next(p for p in qd['punkte'] if p['V0'] == V0)['w']
                    wr, _, inf = eigen(hamilton(G, Kr, V0), rots_r)
                    d = float(np.max(np.abs(np.array(wr[:K_BERICHT]) - np.array(ref[:K_BERICHT]))))
                    qd['string'].append({'V0': V0, 'richtung': r, 'max_diff': d, 'sek': inf['sek'],
                                         'defekte': def_r, 'ergaenzt': inf['ergaenzt']})
            # Dichte Gegenprobe (nur L = 12)
            if L == 12:
                for V0 in STRING_V0:
                    H = hamilton(G, K, V0).toarray()
                    t1 = time.time()
                    wd = np.linalg.eigvalsh(H)[:K_EIG]
                    ref = next(p for p in qd['punkte'] if p['V0'] == V0)['w']
                    gd = [b - a for a, b in stufen(wd)]
                    ge = [b - a for a, b in stufen(np.array(ref))]
                    qd['dicht'].append({'V0': V0, 'max_diff': float(np.max(np.abs(wd - np.array(ref)))),
                                        'stufen_dicht': gd, 'stufen_eigsh': ge, 'sek': time.time() - t1})
            res['q'][str(q)] = qd
        res['sek'] = time.time() - t0
        out['laengen'][str(L)] = res
    if rauch:
        # Zeitprobe L = 24, ein Punkt
        t0 = time.time()
        G, phi, A, geo = aufbau(24, ('+z',))
        K = hueppfen(G, A['+z'], 1)
        rots, defekte = drehungen(G, K)
        p = punkt(G, K, rots, 4.0)
        out['zeitprobe_L24'] = {'geo': geo, 'defekte': defekte, 'punkt': p, 'sek_gesamt': time.time() - t0}
    out['ende_utc'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    json_schreiben(args.aus, out)


def gebunden_bei(G, K, rots, V0, kriterium):
    H = hamilton(G, K, V0)
    w, V, info = eigen(H, rots)
    stf = analyse(G, w, V, None)
    if kriterium == 'karte':
        t = tiefste_gebundene(stf)
        return t is not None, t, w
    return bool(w[0] < E_KANTE - E_MARGE), stf[0], w


def klammer(raster):
    """Rasterklammer: lo = groesstes V0 ohne Bindung, hi = kleinstes V0 > lo mit Bindung."""
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
        G, phi, A, geo = aufbau(L, ('+z',))
        for q in Q_RASTER:
            K = hueppfen(G, A['+z'], q)
            rots, _ = drehungen(G, K)
            eintrag = {'L': L, 'q': q}
            for krit, raster in (('karte', raster_k[(L, q)]), ('energie', raster_e[(L, q)])):
                flags = [g for _, g in raster]
                monoton = all((not flags[i]) or flags[i + 1] for i in range(len(flags) - 1))
                lo, hi = klammer(raster)
                erweitert = False
                if lo is not None and hi is None:
                    # Erweiterung nach oben (ausserhalb des Kartenrasters)
                    v = 12.0
                    while v < 48.0 and hi is None:
                        v *= 2.0
                        b, _, _ = gebunden_bei(G, K, rots, v, krit)
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
                    b, _, _ = gebunden_bei(G, K, rots, mid, krit)
                    if b:
                        hi = mid
                    else:
                        lo = mid
                    schritte += 1
                b, t, w = gebunden_bei(G, K, rots, hi, krit)
                b2, t2, w2 = gebunden_bei(G, K, rots, lo, krit)
                eintrag[krit] = {'raster': raster, 'monoton': monoton, 'erweitert': erweitert,
                                 'lo': lo, 'hi': hi, 'V0c': 0.5 * (lo + hi), 'schritte': schritte,
                                 'sek': time.time() - t0,
                                 'oben_gebunden': b, 'oben_stufe': t, 'oben_w': [float(x) for x in w[:K_BERICHT]],
                                 'unten_gebunden': b2,
                                 'unten_w': [float(x) for x in w2[:K_BERICHT]]}
            out['ergebnis'][f'{L}_{q}'] = eintrag
    # Zweitlaeufe (anderer Startvektor, ncv = 96) an den L = 24-Rasterpunkten ueber der Schwelle, q = 1, 2
    out['zweitlauf'] = []
    if 24 in args.L:
        G, phi, A, geo = aufbau(24, ('+z',))
        for q in (1, 2):
            K = hueppfen(G, A['+z'], q)
            rots, defekte = drehungen(G, K)
            V0c = out['ergebnis'].get(f'24_{q}', {}).get('karte', {}).get('V0c')
            for V0 in V0_RASTER:
                if V0c is not None and V0 > V0c:
                    p = punkt(G, K, rots, V0, seed=1, ncv=96)
                    out['zweitlauf'].append({'q': q, 'punkt': p})
            # oberes Bisektionsende mit Drehungen (Entartung und s direkt an der Schwelle, beschreibend)
            hi = out['ergebnis'].get(f'24_{q}', {}).get('karte', {}).get('hi')
            if hi is not None:
                p = punkt(G, K, rots, hi)
                out['zweitlauf'].append({'q': q, 'oberes_ende': True, 'punkt': p})
    out['ende_utc'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    json_schreiben(args.aus, out)


def modus_scan(args):
    out = kopf('scan', args)
    out['scan'] = {}
    for L in args.L:
        G, phi, A, geo = aufbau(L, ('+z',))
        for q in Q_RASTER:
            K = hueppfen(G, A['+z'], q)
            rots, _ = drehungen(G, K)
            pts = []
            for V0 in np.arange(0.0, 12.0 + 1e-9, args.schritt):
                H = hamilton(G, K, float(V0))
                w, V, info = eigen(H, rots)
                stf = analyse(G, w, V, None)
                pts.append({'V0': float(V0), 'w': [float(x) for x in w[:K_BERICHT]],
                            'stufen': [{k: s[k] for k in ('a', 'm', 'E', 'gewicht', 'gebunden', 'voll')}
                                       for s in stf]})
            out['scan'][f'{L}_{q}'] = pts
    out['ende_utc'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    json_schreiben(args.aus, out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'gitter', 'schwelle', 'scan'])
    ap.add_argument('--L', type=int, nargs='+', default=[12])
    ap.add_argument('--aus', required=True)
    ap.add_argument('--ein', default='')
    ap.add_argument('--schritt', type=float, default=0.25)
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
