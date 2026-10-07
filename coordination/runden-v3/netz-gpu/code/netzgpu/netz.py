# -*- coding: utf-8 -*-
"""Periodische Netze in kubischen Superzellen, Inzidenzen und gewichtete Hodge-Sterne (netzgpu).

Geometrie von V und S wie RUNDE-37/.../ew.py (geometrie), Sterne wie rv.py (sterne) und la.py (tet_beitraege), hier
vektorisiert in torch. Einheiten: Lagen in a (kubische Kante von V), intern ganzzahlig in a/8.
V: 10 Ecken, 68 Kanten, 116 Dreiecke, 58 Tetraeder je primitiver fcc-Zelle (4 primitive Zellen je kubischer Zelle).
S: 6 Ecken je primitiver Zelle (Achse C1-C2 statt Sechseckmitte H). Kuhn: einfach kubisch, 6 Tetraeder je Wuerfel.
Gewichte (Hebehoehe) fuer V: Kammermitte w_C = -23/7, w_H = -32/7 (a/8)^2 bei w_P = 0 (HOEHE-ISOTROP-1, SCHWERE-MASSE-V).
"""
import itertools
import math

import numpy as np
import torch

R8 = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
FCC8 = np.array([[0, 0, 0], [0, 4, 4], [4, 0, 4], [4, 4, 0]])       # fcc-Translationen in einer kubischen Zelle (a/8)
PAARE = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
FLAECHE = [(1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2)]               # Flaeche j = gegenueber Ecke j
W_MITTE_V = {'P': 0.0, 'C': -23.0 / 7.0, 'H': -32.0 / 7.0}           # (a/8)^2


def _sechseck_zyklus(punkte):
    P = [np.asarray(p, int) for p in punkte]
    n = len(P)
    nb = {i: [j for j in range(n) if j != i and int(((P[i] - P[j]) ** 2).sum()) == 8] for i in range(n)}
    assert all(len(v) == 2 for v in nb.values()), nb
    zyk = [0, nb[0][0]]
    while len(zyk) < n:
        zyk.append([j for j in nb[zyk[-1]] if j != zyk[-2]][0])
    return [P[i] for i in zyk]


def basis_geometrie(typ):
    """Ecken (a/8, mit Bahnname) und Tetraeder (Liste von 4 Lagen in a/8) einer primitiven Zelle; Translationen."""
    if typ in ('V', 'S'):
        C1 = np.array([-2, -2, -2])
        C2 = np.array([4, 4, 4])
        ecken = [(R8[a], 'P') for a in range(4)] + [(C1, 'C'), (C2, 'C')]
        if typ == 'V':
            ecken += [(C1 - R8[a], 'H') for a in range(4)]
        tets = [[R8[a] for a in range(4)], [np.array([2, 2, 2]) - R8[b] for b in range(4)]]
        for c, sg, name in ((C1, 1, 'T1'), (C2, -1, 'T2')):
            for a in range(4):
                tets.append([c] + [c + sg * (2 * R8[a] + R8[b]) for b in range(4) if b != a])
            for a in range(4):
                sechs = [c + sg * (2 * R8[b] + R8[d]) for b in range(4) for d in range(4) if a not in (b, d) and b != d]
                zyk = _sechseck_zyklus(sechs)
                if typ == 'V':
                    H = c - sg * R8[a]
                    for i in range(6):
                        tets.append([c, H, zyk[i], zyk[(i + 1) % 6]])
                elif name == 'T1':
                    C2p = c - 2 * R8[a]
                    for i in range(6):
                        tets.append([c, C2p, zyk[i], zyk[(i + 1) % 6]])
        return ecken, tets, FCC8, 8
    if typ == 'Kuhn':
        ecken = [(np.zeros(3, int), 'K')]
        tets = []
        E = np.eye(3, dtype=int) * 8
        for perm in itertools.permutations(range(3)):
            p0 = np.zeros(3, int)
            p1 = p0 + E[perm[0]]
            p2 = p1 + E[perm[1]]
            p3 = p2 + E[perm[2]]
            tets.append([p0, p1, p2, p3])
        return ecken, tets, np.zeros((1, 3), int), 8
    raise ValueError(typ)


def _schluessel(c, M):
    c = np.mod(c, M)
    return (c[..., 0] * M + c[..., 1]) * M + c[..., 2]


class Netz:
    """Periodisches Tetraedernetz in einer Superzelle aus zellen = (nx, ny, nz) kubischen Zellen.

    Attribute (torch auf device): x (N_e,3) Lagen in a; kanten (N_k,2), kvec (N_k,3) = x_j - x_i (entfaltet);
    dreiecke (N_d,3); tetraeder (N_t,4) (aufsteigend sortiert); tX (N_t,4,3) entfaltete Tetraederlagen;
    t_kante (N_t,6) Kanten je Tetraeder (Reihenfolge PAARE), t_flaeche (N_t,4) Dreieck gegenueber Ecke j;
    d0 (N_k x N_e), d1 (N_d x N_k), d2 (N_t x N_d) als torch-Sparse (CSR); w (N_e) Gewichte in a^2.
    """

    def __init__(self, typ='V', zellen=(4, 4, 4), device='cuda', dtype=torch.float64, gewichte='mitte'):
        t0 = __import__('time').time()
        self.typ, self.device, self.dtype = typ, torch.device(device), dtype
        nx, ny, nz = (zellen, zellen, zellen) if isinstance(zellen, int) else tuple(zellen)
        assert min(nx, ny, nz) >= 2, 'mindestens 2 kubische Zellen je Richtung'
        self.zellen = (nx, ny, nz)
        ecken0, tets0, trans0, kante8 = basis_geometrie(typ)
        Mv = np.array([8 * nx, 8 * ny, 8 * nz])
        self.box = (float(nx), float(ny), float(nz))
        # Translationen der Superzelle
        cub = np.array(list(itertools.product(range(nx), range(ny), range(nz)))) * 8
        T = (cub[:, None, :] + trans0[None, :, :]).reshape(-1, 3)        # (n_prim, 3)
        self.n_prim = len(T)
        tb = np.array([[np.asarray(p, int) for p in t] for t in tets0])  # (Tb, 4, 3)
        X8 = (T[:, None, None, :] + tb[None, :, :, :]).reshape(-1, 4, 3)  # (N_t, 4, 3), entfaltet
        # Ecken: Lage modulo Superzelle
        def key(c):
            c = np.mod(c, Mv)
            return (c[..., 0] * Mv[1] + c[..., 1]) * Mv[2] + c[..., 2]
        e8 = np.array([np.asarray(p, int) for p, _ in ecken0])
        alle = (T[:, None, :] + e8[None, :, :]).reshape(-1, 3)
        bahn = np.array([b for _, b in ecken0] * len(T))
        k_alle = key(alle)
        uk, first = np.unique(k_alle, return_index=True)
        assert len(uk) == len(alle), 'Ecken nicht eindeutig'
        self.N_e = len(uk)
        pos8 = np.mod(alle[first], Mv)
        self.bahn = bahn[first]
        gid = np.searchsorted(uk, key(X8))                                 # (N_t, 4)
        assert np.all(uk[gid] == key(X8)), 'Tetraederecke ist keine Netzecke'
        # Tetraeder aufsteigend sortieren (lokale Reihenfolge = globale Reihenfolge)
        o = np.argsort(gid, axis=1)
        gid = np.take_along_axis(gid, o, 1)
        X8 = np.take_along_axis(X8, o[:, :, None], 1)
        assert np.all(np.diff(gid, axis=1) > 0), 'Tetraeder mit doppelter Ecke'
        N_t = len(gid)
        # Kanten
        pi = np.array(PAARE)
        ka = gid[:, pi[:, 0]]
        kb = gid[:, pi[:, 1]]
        kk = ka.astype(np.int64) * self.N_e + kb
        uk_k, first_k, inv_k = np.unique(kk.ravel(), return_index=True, return_inverse=True)
        self.N_k = len(uk_k)
        t_kante = inv_k.reshape(N_t, 6)
        kanten = np.stack([uk_k // self.N_e, uk_k % self.N_e], 1)
        dX = (X8[:, pi[:, 1]] - X8[:, pi[:, 0]]).reshape(-1, 3)
        kvec8 = dX[first_k]
        # Dreiecke (Flaeche j gegenueber Ecke j)
        fl = np.array(FLAECHE)
        fa, fb, fc = gid[:, fl[:, 0]], gid[:, fl[:, 1]], gid[:, fl[:, 2]]
        fk = (fa.astype(np.int64) * self.N_e + fb) * self.N_e + fc
        uk_f, first_f, inv_f = np.unique(fk.ravel(), return_index=True, return_inverse=True)
        self.N_d = len(uk_f)
        t_flaeche = inv_f.reshape(N_t, 4)
        dreiecke = np.stack([uk_f // (self.N_e * self.N_e), (uk_f // self.N_e) % self.N_e, uk_f % self.N_e], 1)
        self.N_t = N_t
        # Orientierung der Tetraeder (sortierte Reihenfolge)
        D = X8[:, 1:] - X8[:, :1]
        det = np.linalg.det(D.astype(float))
        assert np.all(np.abs(det) > 1e-9), 'entarteter Tetraeder'
        self.t_vorzeichen = np.sign(det)
        # Euler-Probe (Torus: 0)
        self.euler = self.N_e - self.N_k + self.N_d - self.N_t
        # torch
        dev, dt = self.device, dtype
        self.x = torch.tensor(pos8 / 8.0, device=dev, dtype=dt)
        self.kanten = torch.tensor(kanten, device=dev, dtype=torch.int64)
        self.kvec = torch.tensor(kvec8 / 8.0, device=dev, dtype=dt)
        self.dreiecke = torch.tensor(dreiecke, device=dev, dtype=torch.int64)
        self.tetraeder = torch.tensor(gid, device=dev, dtype=torch.int64)
        self.tX = torch.tensor(X8 / 8.0, device=dev, dtype=dt)
        self.t_kante = torch.tensor(t_kante, device=dev, dtype=torch.int64)
        self.t_flaeche = torch.tensor(t_flaeche, device=dev, dtype=torch.int64)
        # Inzidenzen
        E = self.N_k
        r0 = np.repeat(np.arange(E), 2)
        c0 = kanten.ravel()
        v0 = np.tile([-1.0, 1.0], E)
        self.d0 = self._csr(r0, c0, v0, (E, self.N_e))
        # d1: Dreieck (a<b<c): +(a,b) +(b,c) -(a,c)
        def kid(i, j):
            kk_ = i.astype(np.int64) * self.N_e + j
            idx = np.searchsorted(uk_k, kk_)
            assert np.all(uk_k[idx] == kk_)
            return idx
        a_, b_, c_ = dreiecke[:, 0], dreiecke[:, 1], dreiecke[:, 2]
        r1 = np.repeat(np.arange(self.N_d), 3)
        c1 = np.stack([kid(a_, b_), kid(b_, c_), kid(a_, c_)], 1).ravel()
        v1 = np.tile([1.0, 1.0, -1.0], self.N_d)
        self.d1 = self._csr(r1, c1, v1, (self.N_d, E))
        # d2: Tetraeder (p<q<r<s): +(q,r,s) -(p,r,s) +(p,q,s) -(p,q,r), mal Orientierung
        r2 = np.repeat(np.arange(N_t), 4)
        c2 = t_flaeche.ravel()
        v2 = (np.array([1.0, -1.0, 1.0, -1.0])[None, :] * self.t_vorzeichen[:, None]).ravel()
        self.d2 = self._csr(r2, c2, v2, (N_t, self.N_d))
        # Gewichte
        w = np.zeros(self.N_e)
        if gewichte == 'mitte' and typ == 'V':
            w = np.array([W_MITTE_V[b] for b in self.bahn]) / 64.0
            w = w - w.mean()
        elif isinstance(gewichte, np.ndarray):
            w = gewichte
        self.w = torch.tensor(w, device=dev, dtype=dt)
        # Typen modulo Gittertranslation (fuer Bloch-Reduktion)
        self._typen(pos8, kanten, kvec8, trans0)
        self.bauzeit_s = __import__('time').time() - t0

    def _csr(self, r, c, v, shape):
        i = torch.tensor(np.stack([r, c]), device=self.device, dtype=torch.int64)
        A = torch.sparse_coo_tensor(i, torch.tensor(v, device=self.device, dtype=self.dtype), shape).coalesce()
        return A.to_sparse_csr()

    def _typen(self, pos8, kanten, kvec8, trans0):
        """Klassen von Ecken und Kanten modulo der Gittertranslationen (fcc bzw. kubisch)."""
        if self.typ in ('V', 'S'):
            Lt = np.array([[0, 4, 4], [4, 0, 4], [4, 4, 0]])
        else:
            Lt = np.eye(3, dtype=int) * 8
        # Reduktion: Koordinaten in Gitterbasis, Bruchteil
        Linv = np.linalg.inv(Lt.T.astype(float))
        def red(p):                       # p in a/8 (auch halbzahlig moeglich), Rueckgabe Schluessel des Bruchteils
            f = (p.astype(float)) @ Linv.T
            f = f - np.floor(f + 1e-9)
            return np.round(f * 64).astype(np.int64) % 64
        fe = red(pos8)
        ke_ = (fe[:, 0] * 64 + fe[:, 1]) * 64 + fe[:, 2]
        ut, self.ecken_typ = np.unique(ke_, return_inverse=True)
        self.n_ecken_typ = len(ut)
        mid = pos8[kanten[:, 0]] + 0.5 * kvec8
        fm = red(mid)
        d = kvec8.copy()
        sg = np.ones(len(d))
        first_nz = np.argmax(d != 0, axis=1)
        sg = np.sign(d[np.arange(len(d)), first_nz])
        dn = d * sg[:, None]
        kt = (((fm[:, 0] * 64 + fm[:, 1]) * 64 + fm[:, 2]) * 64 + (dn[:, 0] + 32)) * 64 * 64 + (dn[:, 1] + 32) * 64 \
            + (dn[:, 2] + 32)
        ut2, self.kanten_typ = np.unique(kt, return_inverse=True)
        self.n_kanten_typ = len(ut2)
        self.kanten_vz = sg                     # Vorzeichen gegen die Klassenrichtung
        self.kanten_mitte = (pos8[kanten[:, 0]] + 0.5 * kvec8) / 8.0

    # ---------------------------------------------------------------------------------------------- Geometrie
    def laengen(self):
        return torch.linalg.norm(self.kvec, dim=1)

    def t_laengen(self, l=None):
        """Kantenlaengen je Tetraeder (N_t, 6) in PAARE-Reihenfolge."""
        if l is None:
            l = self.laengen()
        return l[self.t_kante]

    @staticmethod
    def einbetten(l6):
        """Tetraederlagen (T,4,3) aus 6 Kantenlaengen (Reihenfolge PAARE)."""
        l01, l02, l03, l12, l13, l23 = [l6[:, i] for i in range(6)]
        T = l6.shape[0]
        X = torch.zeros((T, 4, 3), dtype=l6.dtype, device=l6.device)
        X[:, 1, 0] = l01
        x2 = (l01 ** 2 + l02 ** 2 - l12 ** 2) / (2 * l01)
        y2 = torch.sqrt(torch.clamp(l02 ** 2 - x2 ** 2, min=0.0))
        X[:, 2, 0], X[:, 2, 1] = x2, y2
        x3 = (l01 ** 2 + l03 ** 2 - l13 ** 2) / (2 * l01)
        y3 = (l02 ** 2 + l03 ** 2 - l23 ** 2 - 2 * x2 * x3) / (2 * y2)
        z3 = torch.sqrt(torch.clamp(l03 ** 2 - x3 ** 2 - y3 ** 2, min=0.0))
        X[:, 3, 0], X[:, 3, 1], X[:, 3, 2] = x3, y3, z3
        return X

    @staticmethod
    def tet_beitraege(X, wt):
        """Je Tetraeder wie la.tet_beitraege (vektorisiert): duale Flaeche je Kante (T,6), duale Laenge je Dreieck (T,4),
        Dreiecksflaeche (T,4), Kantenlaenge (T,6). X (T,4,3), wt (T,4) in a^2."""
        q = (X * X).sum(-1) - wt
        A = 2.0 * (X[:, 1:] - X[:, :1])
        b = (q[:, 1:] - q[:, :1]).unsqueeze(-1)
        z = torch.linalg.solve(A, b).squeeze(-1)                         # gewichteter Umkreismittelpunkt
        cf, nu, dl, af = [], [], [], []
        for j in range(4):
            i0, i1, i2 = FLAECHE[j]
            e1, e2 = X[:, i1] - X[:, i0], X[:, i2] - X[:, i0]
            g11, g12, g22 = (e1 * e1).sum(-1), (e1 * e2).sum(-1), (e2 * e2).sum(-1)
            r1 = 0.5 * (g11 + wt[:, i0] - wt[:, i1])
            r2 = 0.5 * (g22 + wt[:, i0] - wt[:, i2])
            det = g11 * g22 - g12 * g12
            a1 = (g22 * r1 - g12 * r2) / det
            a2 = (g11 * r2 - g12 * r1) / det
            c = X[:, i0] + a1[:, None] * e1 + a2[:, None] * e2
            nv = torch.cross(e1, e2, dim=-1)
            nn = torch.linalg.norm(nv, dim=-1)
            af.append(0.5 * nn)
            nv = nv / nn[:, None]
            s = torch.sign(((X[:, j] - X[:, i0]) * nv).sum(-1))
            nv = nv * s[:, None]
            cf.append(c)
            nu.append(nv)
            dl.append(((z - c) * nv).sum(-1))
        Ae, le = [], []
        for (i, j) in PAARE:
            k, l_ = [m for m in range(4) if m not in (i, j)]
            e = X[:, j] - X[:, i]
            ll = torch.linalg.norm(e, dim=-1)
            eh = e / ll[:, None]
            cij = X[:, i] + ((ll * ll + wt[:, i] - wt[:, j]) / (2 * ll))[:, None] * eh
            tot = torch.zeros_like(ll)
            for (a, bb) in ((k, l_), (l_, k)):
                u = (X[:, a] - X[:, i]) - ((X[:, a] - X[:, i]) * eh).sum(-1, keepdim=True) * eh
                u = u / torch.linalg.norm(u, dim=-1, keepdim=True)
                h1 = ((cf[bb] - cij) * u).sum(-1)
                h2 = ((z - cf[bb]) * nu[bb]).sum(-1)
                tot = tot + 0.5 * h1 * h2
            Ae.append(tot)
            le.append(ll)
        return torch.stack(Ae, 1), torch.stack(dl, 1), torch.stack(af, 1), torch.stack(le, 1)

    def sterne(self, l=None, w=None, block=200000):
        """Gewichtete Hodge-Sterne. l (N_k) Kantenlaengen (Standard: flach), w (N_e) Gewichte in a^2.
        Rueckgabe: s0 (N_e, duales Volumen), s1 (N_k, A*/l), s2 (N_d, delta/A), A_f, l, Ast (N_k), delta (N_d)."""
        if w is None:
            w = self.w
        flach = l is None
        if flach:
            l = self.laengen()
        Ast = torch.zeros(self.N_k, dtype=self.dtype, device=self.device)
        dlt = torch.zeros(self.N_d, dtype=self.dtype, device=self.device)
        Af = torch.zeros(self.N_d, dtype=self.dtype, device=self.device)
        for s in range(0, self.N_t, block):
            sl = slice(s, min(s + block, self.N_t))
            if flach:
                X = self.tX[sl]
            else:
                X = self.einbetten(l[self.t_kante[sl]])
            wt = w[self.tetraeder[sl]]
            A6, d4, a4, _ = self.tet_beitraege(X, wt)
            Ast.index_add_(0, self.t_kante[sl].reshape(-1), A6.reshape(-1))
            dlt.index_add_(0, self.t_flaeche[sl].reshape(-1), d4.reshape(-1))
            Af.index_put_((self.t_flaeche[sl].reshape(-1),), a4.reshape(-1), accumulate=False)
        s1 = Ast / l
        s2 = dlt / Af
        a, b = self.kanten[:, 0], self.kanten[:, 1]
        wa, wb = w[a], w[b]
        s0 = torch.zeros(self.N_e, dtype=self.dtype, device=self.device)
        s0.index_add_(0, a, Ast * (l * l + wa - wb) / (2 * l) / 3.0)
        s0.index_add_(0, b, Ast * (l * l + wb - wa) / (2 * l) / 3.0)
        return {'s0': s0, 's1': s1, 's2': s2, 'A_f': Af, 'l': l, 'Ast': Ast, 'delta': dlt}

    def volumen(self):
        return float(np.prod(self.box))

    def pruefung(self, st=None):
        """Kontrollen: d1 d0 = 0, d2 d1 = 0, Euler, Summe *0 = Volumen, Summe A* l t t^T = V I, Vorzeichen."""
        if st is None:
            st = self.sterne()
        out = {'N_e': self.N_e, 'N_k': self.N_k, 'N_d': self.N_d, 'N_t': self.N_t, 'euler': int(self.euler),
               'n_prim': self.n_prim, 'typen_ecken': int(self.n_ecken_typ), 'typen_kanten': int(self.n_kanten_typ)}
        x = torch.randn(self.N_e, dtype=self.dtype, device=self.device)
        y = torch.randn(self.N_k, dtype=self.dtype, device=self.device)
        out['d1d0'] = float((self.d1 @ (self.d0 @ x)).abs().max())
        out['d2d1'] = float((self.d2 @ (self.d1 @ y)).abs().max())
        V = self.volumen()
        out['id_vol'] = float(abs(st['s0'].sum().item() - V) / V)
        t = self.kvec / st['l'][:, None]
        T1 = torch.einsum('e,ei,ej->ij', st['Ast'] * st['l'], t, t) / V
        out['id_T1'] = float((T1 - torch.eye(3, dtype=self.dtype, device=self.device)).abs().max())
        out['min_s0'] = float(st['s0'].min())
        out['min_s1'] = float(st['s1'].min())
        out['min_s2'] = float(st['s2'].min())
        out['vol_tet_summe_rel'] = float(abs(np.abs(self._tetvol()).sum() - V) / V)
        return out

    def _tetvol(self):
        D = self.tX[:, 1:] - self.tX[:, :1]
        return (torch.linalg.det(D) / 6.0).cpu().numpy()

    def ecken_minbild(self, x0):
        """Abstandsvektor (minimales Bild) jeder Ecke zu x0 (in a)."""
        B = torch.tensor(self.box, dtype=self.dtype, device=self.device)
        d = self.x - torch.as_tensor(x0, dtype=self.dtype, device=self.device)
        return d - B * torch.round(d / B)
