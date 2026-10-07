#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGIME-K-1 (fmhc-physics, Runde 48), Code-Agent fuer die Leitung claude-primary.

Bloch-Hesse-Matrix H(k) der linearisierten euklidischen 4D-Regge-Wirkung S = Summe_t A_t eps_t auf periodischen
4D-Gittern:
  B1   Raum = B1-Kopie aus PACHNER-TAKT-1 (fcc, Tetraeder-Oktaeder-Wabe, eine Diagonale je Oktaeder),
       Zeit = Treppen-Triangulierung der Zeltzuege (Klassenfolge 0, X, Y, Z; Klassenhoehen 0, 1/4, 1/2, 3/4 mal tau;
       Hub tau; innerhalb einer Klasse die Diagonalenden in Achsrichtung von unten nach oben). Periodisch in Raum
       (kubisch) und Zeit (Periode tau).
  KW   Kuhn-Wuerfelgitter (Rocek/Williams; REGGE-4D-1), gleiche Treppen-Konstruktion ueber dem 3D-Kuhn-Gitter.
  KW2  dasselbe Kuhn-Gitter mit verdoppelter Zelle (Codeprobe fuer Kanten zwischen verschiedenen Grundecken).
Geometrie je 4-Simplex (Diederwinkel, Flaechen, M = (dA/dl)^T (dtheta/dl), komplexer Schritt) und das B1-Netz aus
pt.py (unveraenderte Kopie aus RUNDE-37/pachner-takt-1/code). H = Hesse von S nach den Kantenlaengen = -Summe M.

Modi:
  gitter      Aufbau, Kontrollen, Spektren an allen Richtungen und kl-Werten -> JSON
  auswertung  Urteile RK0 bis RK3, Pipeline-Kontrolle und beschreibende Zahlen nach PLAN.md -> JSON
"""
import argparse, json, sys, os, time, platform, hashlib, resource, itertools
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pt  # noqa: E402

PAARE5, DREI5 = pt.PAARE5, pt.DREI5
KL_RASTER = [0.005, 0.01, 0.02, 0.03, 0.05, 0.07, 0.1, 0.14, 0.2]
KL_FIT = [0.005, 0.01, 0.02, 0.05, 0.1]
KL_EXP = [0.05, 0.07, 0.1, 0.14, 0.2]
TOL_NULL = 1e-12      # Nullmode: |lambda| <= TOL_NULL * max|lambda|
TOL_CC = 1e-12        # Pseudo-Inverse im Gitterblock
SEED = 20261005
XB_B1 = [(0.0, 0.0, 0.0), (0.0, 0.5, 0.5), (0.5, 0.0, 0.5), (0.5, 0.5, 0.0)]   # Klassen 0, X, Y, Z (pt.PAR2KL)
HB_B1 = [0.0, 0.25, 0.5, 0.75]                                                # Klassenhoehen in Einheiten von tau


# ================================================================================================= Tensorbasen
def sym_basis():
    S = []
    for i in range(4):
        m = np.zeros((4, 4)); m[i, i] = 1.0; S.append(m)
    for i, j in itertools.combinations(range(4), 2):
        m = np.zeros((4, 4)); m[i, j] = m[j, i] = 1.0 / np.sqrt(2.0); S.append(m)
    return np.array(S)


SB = sym_basis()                              # Frobenius-orthonormale Basis der symmetrischen 4x4-Matrizen
A3B = [np.eye(3) / np.sqrt(3.0), np.diag([1.0, -1.0, 0.0]) / np.sqrt(2.0), np.diag([1.0, 1.0, -2.0]) / np.sqrt(6.0)]
for _i, _j in ((0, 1), (0, 2), (1, 2)):
    _m = np.zeros((3, 3)); _m[_i, _j] = _m[_j, _i] = 1.0 / np.sqrt(2.0); A3B.append(_m)
A3B = np.array(A3B)                           # Index 0 = Spur (konform), 1..5 spurfrei (TT)


def transversal(kh):
    """10 x 6: Frobenius-orthonormale Basis der zu kh transversalen symmetrischen Tensoren; Spalte 0 = P_k / sqrt3."""
    Q, _ = np.linalg.qr(np.c_[kh, np.eye(4)])
    Q = Q[:, 1:4]
    T = np.zeros((10, 6))
    for j in range(6):
        T[:, j] = np.einsum('aij,ij->a', SB, Q @ A3B[j] @ Q.T)
    return T


# ================================================================================================= Kombinatorik
def kanon_menge(verts):
    """Normalform einer Eckmenge [(b, n)] modulo Gittertranslationen."""
    best = None
    for (b0, n0) in verts:
        tv = tuple(sorted((int(b), tuple(int(x) - int(y) for x, y in zip(n, n0))) for (b, n) in verts))
        if best is None or tv < best:
            best = tv
    return best


def kanon_kante(v1, v2):
    (b1, n1), (b2, n2) = v1, v2
    d = tuple(int(y) - int(x) for x, y in zip(n1, n2))
    if b1 == b2 and not any(d):
        raise ValueError('entartete Kante')
    if b1 < b2 or (b1 == b2 and d > tuple([0] * len(d))):
        return (int(b1), int(b2), d), tuple(int(x) for x in n1)
    return (int(b2), int(b1), tuple(-x for x in d)), tuple(int(x) for x in n2)


def b1_raum():
    """Raeumliche Tetraeder der B1-Kopie je kubischer Zelle, aus pt.Netz(2) (kanonisch modulo Z^3)."""
    nz = pt.Netz(2, 'klasse', 'TT')
    xb = np.array(XB_B1)
    zaehl, rest = {}, 0.0
    for key in nz.sigma:
        verts = []
        for (v, s) in key:
            p = nz.X[v] + nz.n * np.array(s, float)
            b = nz.kl[v]
            q = p - xb[b]
            n3 = np.round(q).astype(int)
            rest = max(rest, float(np.abs(q - n3).max()))
            verts.append((b, tuple(int(x) for x in n3)))
        kk = kanon_menge(verts)
        zaehl[kk] = zaehl.get(kk, 0) + 1
    tets = [list(k) for k in sorted(zaehl)]
    return tets, {'tets_superzelle_n2': len(nz.sigma), 'tet_klassen': len(tets),
                  'tet_je_klasse': sorted(set(zaehl.values())), 'rundungsrest': rest}


def kuhn_raum():
    tets = []
    for perm in itertools.permutations(range(3)):
        v = [0, 0, 0]
        T = [(0, tuple(v))]
        for a in perm:
            v = list(v); v[a] += 1
            T.append((0, tuple(v)))
        tets.append(T)
    return tets


def kuhn2_raum():
    tets = []
    for ax in (0, 1):
        for T in kuhn_raum():
            verts = []
            for (_, n) in T:
                p = np.array(n) + np.array([ax, 0, 0])
                b = int(p[0] % 2)
                verts.append((b, (int((p[0] - b) // 2), int(p[1]), int(p[2]))))
            tets.append(verts)
    return tets


def ord_b1(g, v):
    """Hubfolge B1: Klasse zuerst (0, X, Y, Z), dann Lage (Diagonalenden in Achsrichtung von unten nach oben)."""
    b, n = v
    x = g.xb[b] + g.A3 @ np.array(n, float)
    return (b, x[0], x[1], x[2])


def ord_kuhn(g, v):
    """Hubfolge Kuhn: umgekehrte Inklusionsfolge (groesste Koordinatensumme zuerst) -> 4D-Kuhn-Zerlegung."""
    b, n = v
    x = g.xb[b] + g.A3 @ np.array(n, float)
    return (-float(x.sum()), x[0], x[1], x[2])


# ================================================================================================= Gitter
class Gitter:
    def __init__(self, name, xb, hb, A3, tets3, ordnung, tau):
        self.name, self.tau = name, float(tau)
        self.xb = np.array(xb, float); self.hb = np.array(hb, float); self.NV = len(self.xb)
        self.A3 = np.array(A3, float)
        self.A = np.zeros((4, 4)); self.A[:3, :3] = self.A3; self.A[3, 3] = self.tau
        self.Vc = float(abs(np.linalg.det(self.A)))
        self.tets3 = tets3
        simp = []
        for tet in tets3:
            vs = sorted(tet, key=lambda v: ordnung(self, v))
            for j in range(4):
                simp.append([(b, tuple(n) + (1,)) for (b, n) in vs[:j + 1]] +
                            [(b, tuple(n) + (0,)) for (b, n) in vs[j:]])
        self.simp = simp
        self.S = len(simp)
        ekey = {}
        egid = np.zeros((self.S, 10), int); eT = np.zeros((self.S, 10, 4), int)
        for s, Sv in enumerate(simp):
            for i, (a, c) in enumerate(PAARE5):
                key, T = kanon_kante(Sv[a], Sv[c])
                egid[s, i] = ekey.setdefault(key, len(ekey))
                eT[s, i] = T
        self.ekeys = sorted(ekey, key=ekey.get)
        self.NE = len(self.ekeys)
        self.egid, self.eT = egid, eT
        self.Tphys = eT.astype(float) @ self.A.T
        self.b1 = np.array([k[0] for k in self.ekeys]); self.b2 = np.array([k[1] for k in self.ekeys])
        self.Rd = np.array([self.A @ np.array(k[2], float) for k in self.ekeys])
        self.p1 = np.array([self.pos(k[0], (0, 0, 0, 0)) for k in self.ekeys])
        self.E = np.array([self.pos(k[1], k[2]) for k in self.ekeys]) - self.p1
        self.l = np.linalg.norm(self.E, axis=1)
        self.u = self.E / self.l[:, None]
        self.mid = self.p1 + 0.5 * self.E
        self.lmean = float(self.l.mean())
        self.P0 = np.einsum('ei,aij,ej->ea', self.E, SB, self.E) / (2.0 * self.l[:, None])
        self.Xs = np.array([[self.pos(b, n) for (b, n) in Sv] for Sv in simp])
        self.geo = pt.geometrie(self.Xs)
        self.Hloc = -self.geo['M']

    def pos(self, b, n):
        return np.r_[self.xb[b], self.tau * self.hb[b]] + self.A @ np.asarray(n, float)

    # --------------------------------------------------------------------------------------------- Kontrollen
    def kontrollen(self):
        th = self.geo['th']
        winkel, nsimp_t, tet_n = {}, {}, {}
        for s, Sv in enumerate(self.simp):
            for k in range(10):
                key = kanon_menge([Sv[x] for x in DREI5[k]])
                winkel[key] = winkel.get(key, 0.0) + th[s, k]
                nsimp_t[key] = nsimp_t.get(key, 0) + 1
            for j in range(5):
                key = kanon_menge([Sv[x] for x in range(5) if x != j])
                tet_n[key] = tet_n.get(key, 0) + 1
        defz = np.array([2 * np.pi - v for v in winkel.values()])
        simp_keys = [kanon_menge(Sv) for Sv in self.simp]
        vol = np.linalg.det(self.Xs[:, 1:, :] - self.Xs[:, :1, :]) / 24.0
        lgeo = self.geo['l']
        # tote Kanten: alle lokalen Zeilen null
        zeile = np.zeros(self.NE)
        for s in range(self.S):
            for i in range(10):
                e = self.egid[s, i]
                zeile[e] = max(zeile[e], float(np.abs(self.Hloc[s, i, :]).max()))
        hmax = float(np.abs(self.Hloc).max())
        return {'NE': self.NE, 'S': self.S, 'NV': self.NV, 'Vc': self.Vc, 'lmean': self.lmean,
                'kantenlaengen': sorted(set(round(float(x), 12) for x in self.l)),
                'dreiecke': len(winkel), 'simplizes_je_dreieck': [min(nsimp_t.values()), max(nsimp_t.values())],
                'tetraeder': len(tet_n), 'tetraeder_inzidenz': sorted(set(tet_n.values())),
                'simplizes_verschieden': len(set(simp_keys)),
                'fehlwinkel_max_abs': float(np.abs(defz).max()),
                'vol_summe_abs': float(np.abs(vol).sum()), 'vol_summe_rel_fehler': float(abs(np.abs(vol).sum() / self.Vc - 1)),
                'vol_min_rel': float(np.abs(vol).min() / self.lmean ** 4),
                'vol_vorzeichen': [int((vol > 0).sum()), int((vol < 0).sum())],
                'kantenlaenge_geo_gegen_kanon': float(np.abs(lgeo - self.l[self.egid]).max()),
                'schlaefli': self.geo['schlaefli'], 'M_sym': self.geo['M_sym'],
                'tote_kanten': [list(self.ekeys[e][:2]) + [list(self.ekeys[e][2])] for e in range(self.NE)
                                if zeile[e] <= 1e-12 * hmax]}

    # --------------------------------------------------------------------------------------------- Bloch
    def H(self, k):
        ph = np.exp(1j * (self.Tphys @ k))
        W = self.Hloc * (np.conj(ph)[:, :, None] * ph[:, None, :])
        idx = (self.egid[:, :, None] * self.NE + self.egid[:, None, :]).ravel()
        n2 = self.NE * self.NE
        Hk = np.bincount(idx, W.real.ravel(), minlength=n2) + 1j * np.bincount(idx, W.imag.ravel(), minlength=n2)
        return Hk.reshape(self.NE, self.NE)

    def G(self, k):
        Gk = np.zeros((self.NE, 4 * self.NV), complex)
        ph = np.exp(1j * (self.Rd @ k))
        for e in range(self.NE):
            Gk[e, 4 * self.b2[e]:4 * self.b2[e] + 4] += self.u[e] * ph[e]
            Gk[e, 4 * self.b1[e]:4 * self.b1[e] + 4] -= self.u[e]
        return Gk

    def P(self, k):
        return self.P0 * np.exp(1j * (self.mid @ k))[:, None]

    def analyse(self, k):
        kn = float(np.linalg.norm(k)); kh = k / kn
        H0 = self.H(k)
        Hn = float(np.abs(H0).max())
        herm = float(np.abs(H0 - H0.conj().T).max() / Hn)
        Hk = 0.5 * (H0 + H0.conj().T)
        w, U = np.linalg.eigh(Hk)
        aw = np.abs(w); wmax = float(aw.max())
        nul = aw <= TOL_NULL * wmax
        n0 = int(nul.sum())
        srt = np.sort(aw)
        luecke = float(srt[n0] / srt[n0 - 1]) if (0 < n0 < len(srt) and srt[n0 - 1] > 0) else None
        Gk = self.G(k)
        sg = np.linalg.svd(Gk, compute_uv=False)
        rG = int((sg > 1e-10 * sg[0]).sum())
        HG = float(np.abs(Hk @ Gk).max() / (wmax * np.abs(Gk).max()))
        sin_ng = None
        if n0 == rG and n0 > 0:
            Qg, _ = np.linalg.qr(Gk)
            cs = np.linalg.svd(U[:, nul].conj().T @ Qg[:, :rG], compute_uv=False)
            sin_ng = float(np.sqrt(max(0.0, 1.0 - float(cs.min()) ** 2)))
        Z = U[:, ~nul]; wz = w[~nul]
        T = transversal(kh)
        B = Z.conj().T @ (self.P(k) @ T)
        UB, sB, _ = np.linalg.svd(B, full_matrices=True)
        C = UB[:, 6:]
        HB = wz[:, None] * B; HC = wz[:, None] * C
        Hbb = B.conj().T @ HB; Hbc = B.conj().T @ HC; Hcc = C.conj().T @ HC
        Hcc = 0.5 * (Hcc + Hcc.conj().T)
        ec, Vcc = np.linalg.eigh(Hcc)
        ok = np.abs(ec) > TOL_CC * wmax
        X = Vcc[:, ok] @ ((Vcc[:, ok].conj().T @ Hbc.conj().T) / ec[ok][:, None])
        M6 = Hbb - Hbc @ X
        M6 = 0.5 * (M6 + M6.conj().T)
        Hbb = 0.5 * (Hbb + Hbb.conj().T)
        k2V = kn ** 2 * self.Vc
        out = {'n0': n0, 'luecke': luecke, 'rG': rG, 'HG': HG, 'herm': herm, 'sin_null_eich': sin_ng,
               'hart': float(np.abs(ec[ok]).min() / wmax) if ok.any() else None, 'ncc_null': int((~ok).sum()),
               'im_rel': float(np.abs(M6.imag).max() / np.abs(M6.real).max()),
               'B_kond': float(sB[0] / sB[-1])}
        for art, M in (('gerade', 0.5 * (M6.real + M6.real.T)), ('voll', M6), ('affin', 0.5 * (Hbb.real + Hbb.real.T))):
            lam, V = np.linalg.eigh(M)
            ov = np.abs(V[0, :]) ** 2
            ic = int(np.argmax(ov))
            rest = [j for j in range(6) if j != ic]
            out['tt_' + art] = sorted(float(lam[j] / k2V) for j in rest)
            out['konf_' + art] = float(lam[ic] / k2V)
            out['ovk_' + art] = float(ov[ic])
            out['ovt_' + art] = float(max(ov[j] for j in rest))
        return out


def baue(name, tau=1.0, hoehen_fest=False):
    if name == 'B1':
        tets, info = b1_raum()
        hb = np.array(HB_B1) / (tau if hoehen_fest else 1.0)
        g = Gitter('B1', XB_B1, hb, np.eye(3), tets, ord_b1, tau)
        g.info_raum = info
    elif name == 'KW':
        g = Gitter('KW', [(0.0, 0.0, 0.0)], [0.0], np.eye(3), kuhn_raum(), ord_kuhn, tau)
        g.info_raum = {'tet_klassen': 6}
    elif name == 'KW2':
        g = Gitter('KW2', [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)], [0.0, 0.0], np.diag([2.0, 1.0, 1.0]), kuhn2_raum(),
                   ord_kuhn, tau)
        g.info_raum = {'tet_klassen': 12}
    else:
        raise ValueError(name)
    return g


# ================================================================================================= Kontrollen
def superzelle(g, N):
    N = np.array(N)
    cells = list(itertools.product(*[range(int(x)) for x in N]))
    cid = {c: i for i, c in enumerate(cells)}
    NEs = g.NE * len(cells)
    Hs = np.zeros(NEs * NEs)
    for c in cells:
        cc = np.array(c)
        lab = np.zeros((g.S, 10), int)
        for s in range(g.S):
            for i in range(10):
                lab[s, i] = g.egid[s, i] + g.NE * cid[tuple(int(x) for x in (cc + g.eT[s, i]) % N)]
        idx = (lab[:, :, None] * NEs + lab[:, None, :]).ravel()
        Hs += np.bincount(idx, g.Hloc.ravel(), minlength=NEs * NEs)
    Hs = Hs.reshape(NEs, NEs)
    ws = np.linalg.eigvalsh(0.5 * (Hs + Hs.T))
    Ainv = np.linalg.inv(g.A)
    wb = []
    for c in cells:
        k = 2 * np.pi * Ainv.T @ (np.array(c, float) / N)
        Hk = g.H(k)
        wb.extend(np.linalg.eigvalsh(0.5 * (Hk + Hk.conj().T)))
    wb = np.array(wb)
    return {'N': [int(x) for x in N], 'NE_super': int(NEs),
            'spektrum_diff_rel': float(np.abs(np.sort(ws) - np.sort(wb)).max() / np.abs(ws).max()),
            'super_sym_rel': float(np.abs(Hs - Hs.T).max() / np.abs(Hs).max())}


def pt_vergleich(g):
    """B1, tau = 1: Simplizes eines TT-Takts aus pt.py (n = 3) gegen das periodische Treppengitter."""
    nz = pt.Netz(3, 'klasse', 'TT')
    nz.takt('TT')
    mine = set(kanon_menge(Sv) for Sv in g.simp)
    n = tr = ni = tri = 0
    rest = 0.0
    for refs in nz.simp:
        verts = []
        for (v, s) in refs:
            p = nz.pos((v, s)); b = nz.kl[v]
            q = np.r_[p[:3] - g.xb[b], (p[3] - g.tau * g.hb[b]) / g.tau]
            nn = np.round(q).astype(int)
            rest = max(rest, float(np.abs(q - nn).max()))
            verts.append((b, tuple(int(x) for x in nn)))
        hit = kanon_menge(verts) in mine
        n += 1; tr += int(hit)
        if all(tuple(s) == (0, 0, 0) for (v, s) in refs):
            ni += 1; tri += int(hit)
    return {'pt_simplizes': n, 'treffer': tr, 'ohne_rand': ni, 'ohne_rand_treffer': tri, 'rundungsrest': rest}


def richtungen():
    D, nm = [], []
    E = np.eye(4); ax = 'xyzt'
    for i in range(4):
        D.append(E[i]); nm.append('a_' + ax[i])
    for i, j in itertools.combinations(range(4), 2):
        for sg in (1, -1):
            D.append((E[i] + sg * E[j]) / np.sqrt(2.0)); nm.append('f_%s%s%s' % (ax[i], '+' if sg > 0 else '-', ax[j]))
    for z in range(4):
        idx = [i for i in range(4) if i != z]
        for s1 in (1, -1):
            for s2 in (1, -1):
                v = np.zeros(4); v[idx[0]] = 1.0; v[idx[1]] = s1; v[idx[2]] = s2
                D.append(v / np.sqrt(3.0)); nm.append('d3_ohne%s_%+d%+d' % (ax[z], s1, s2))
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                D.append(np.array([1.0, s1, s2, s3]) / 2.0); nm.append('d4_%+d%+d%+d' % (s1, s2, s3))
    rng = np.random.default_rng(SEED)
    for i in range(40):
        v = rng.normal(size=4); D.append(v / np.linalg.norm(v)); nm.append('z4_%02d' % i)
    for i in range(12):
        v = rng.normal(size=3); D.append(np.r_[v / np.linalg.norm(v), 0.0]); nm.append('z3_%02d' % i)
    return np.array(D), nm


def lauf_gitter(g, rauch=False, mit_pt=False):
    t0 = time.time()
    D, nm = richtungen()
    kl = KL_RASTER
    if rauch:
        sel = [0, 3, 4, 20, 40, 80]
        D = D[sel]; nm = [nm[i] for i in sel]
    out = {'gitter': g.name, 'tau': g.tau, 'hb': g.hb.tolist(), 'A': g.A.tolist(), 'info_raum': g.info_raum,
           'kontrollen': g.kontrollen(), 'richtungen': D.tolist(), 'richtungsnamen': nm, 'kl': kl}
    out['t_aufbau_s'] = time.time() - t0
    # k = 0
    Hz = g.H(np.zeros(4)); Hz = 0.5 * (Hz + Hz.conj().T)
    wz = np.linalg.eigvalsh(Hz); awz = np.abs(wz); mz = float(awz.max())
    srt = np.sort(awz); n0z = int((awz <= TOL_NULL * mz).sum())
    Gz = g.G(np.zeros(4))
    out['k0'] = {'n0': n0z, 'luecke': float(srt[n0z] / srt[n0z - 1]) if 0 < n0z < len(srt) else None,
                 'eig_rel_um_null': [float(x / mz) for x in srt[max(0, n0z - 2):n0z + 6]],
                 'HP0_rel': float(np.abs(Hz @ g.P0).max() / (mz * np.abs(g.P0).max())),
                 'HG0_rel': float(np.abs(Hz @ Gz).max() / (mz * np.abs(Gz).max())) if np.abs(Gz).max() > 0 else None,
                 'rang_G0': int(np.linalg.matrix_rank(Gz)), 'rang_P0': int(np.linalg.matrix_rank(g.P0)),
                 'rang_P0_G0': int(np.linalg.matrix_rank(np.c_[g.P0, Gz]))}
    out['superzelle'] = superzelle(g, (2, 2, 2, 2) if not rauch else (2, 1, 1, 2))
    if mit_pt:
        out['pt_vergleich'] = pt_vergleich(g)
    out['t_kontrollen_s'] = time.time() - t0
    felder = None
    for di, d in enumerate(D):
        for xi, x in enumerate(kl):
            r = g.analyse((x / g.lmean) * d)
            if felder is None:
                felder = {key: np.full((len(D), len(kl)) + np.shape(val), np.nan) if val is not None and not isinstance(val, int)
                          else np.full((len(D), len(kl)), np.nan) for key, val in r.items()}
            for key, val in r.items():
                felder[key][di, xi] = np.nan if val is None else val
    out['spektren'] = {key: ohne_nan(val.tolist()) for key, val in felder.items()}
    out['t_gesamt_s'] = time.time() - t0
    return out


def ohne_nan(x):
    """NaN -> None (JSON null), damit jq die Dateien lesen kann."""
    if isinstance(x, list):
        return [ohne_nan(y) for y in x]
    if isinstance(x, float) and x != x:
        return None
    return x


# ================================================================================================= Auswertung
def w0_fit(xs, Y, gerade=True):
    x = np.array(xs, float)
    X = np.c_[np.ones_like(x), x ** 2, x ** 4] if gerade else np.c_[np.ones_like(x), x, x ** 2, x ** 3]
    coef = np.linalg.lstsq(X, np.asarray(Y, float).T, rcond=None)[0]
    return coef[0], coef


def spanne(W):
    W = np.asarray(W, float).ravel()
    if W.size == 0 or np.isnan(W).any() or not (np.all(W > 0) or np.all(W < 0)):
        return None
    a = np.abs(W)
    return float(a.max() / a.min() - 1.0)


def exponent(xs, ys):
    if any(y is None or not (y > 0) for y in ys):
        return None
    return float(np.polyfit(np.log(xs), np.log(ys), 1)[0])


def kennzahlen(J, art):
    kl = J['kl']; sp = J['spektren']
    tt = np.array(sp['tt_' + art]); konf = np.array(sp['konf_' + art])
    D = np.array(J['richtungen']); ND = len(D)
    ger = art != 'voll'
    jf = [kl.index(x) for x in KL_FIT]; je = [kl.index(x) for x in KL_EXP]
    Y = tt[:, jf, :].transpose(0, 2, 1).reshape(-1, len(jf))
    w0 = w0_fit(KL_FIT, Y, ger)[0].reshape(ND, 5)
    c0 = w0_fit(KL_FIT, konf[:, jf], ger)[0]
    raum = np.abs(D[:, 3]) < 1e-12
    it = J['richtungsnamen'].index('a_t')
    spannen = [spanne(tt[:, j, :]) for j in range(len(kl))]
    sp_raum = [spanne(tt[raum, j, :]) for j in range(len(kl))]
    k = {'s0': spanne(w0), 's0_raum': spanne(w0[raum]), 'n_richtungen': int(ND), 'n_raum': int(raum.sum()),
         'w0_min': float(w0.min()), 'w0_max': float(w0.max()), 'w0_mittel': float(w0.mean()),
         'konf0_min': float(c0.min()), 'konf0_max': float(c0.max()),
         'konf_zu_tt': float(c0.mean() / w0.mean()),
         'R_zeit_raum': float(w0[it].mean() / w0[raum].mean()),
         'w0_zeit': [float(x) for x in w0[it]],
         'spanne_je_kl': dict(zip([str(x) for x in kl], spannen)),
         'spanne_raum_je_kl': dict(zip([str(x) for x in kl], sp_raum)),
         'p': exponent(KL_EXP, [spannen[j] for j in je]),
         'p_raum': exponent(KL_EXP, [sp_raum[j] for j in je]),
         'lokal_p': [exponent([KL_EXP[i], KL_EXP[i + 1]], [spannen[je[i]], spannen[je[i + 1]]]) for i in range(len(je) - 1)]}
    if k['s0'] is not None:
        ex = [s - k['s0'] if s is not None else None for s in [spannen[j] for j in je]]
        k['p_ohne_s0'] = exponent(KL_EXP, ex)
    return k


def urteil_paar(plan, karte_zusatz):
    """Kartenwortlaut: eingetroffen nur, wenn beide Fassungen eintreffen; beide verfehlt -> verfehlt; sonst unklar."""
    if plan and karte_zusatz:
        return 'eingetroffen'
    if not plan and not karte_zusatz:
        return 'nicht eingetroffen'
    return 'unklar'


def lauf_auswertung(pfade):
    J = {nm: json.load(open(p)) for nm, p in pfade.items()}
    out = {'eingaben': {nm: {'pfad': p, 'sha256': sha(p), 'skript': J[nm]['info']['skript_sha256']} for nm, p in pfade.items()}}
    K = {nm: {art: kennzahlen(J[nm], art) for art in ('gerade', 'voll', 'affin')} for nm in J}
    out['kennzahlen'] = K
    # Nullmoden und Eichung je Gitter
    nz = {}
    for nm in J:
        sp = J[nm]['spektren']
        n0 = np.array(sp['n0'], float); lu = np.array(sp['luecke'], float); HG = np.array(sp['HG'], float)
        rG = np.array(sp['rG'], float)
        sn = np.array(sp['sin_null_eich'], float)
        nz[nm] = {'n0_min': int(n0.min()), 'n0_max': int(n0.max()),
                  'luecke_min': float(np.nanmin(lu)) if np.isfinite(lu).any() else None,
                  'HG_max': float(HG.max()), 'rG_min': int(rG.min()), 'rG_max': int(rG.max()),
                  'sin_null_eich_max': float(np.nanmax(sn)) if np.isfinite(sn).any() else None,
                  'herm_max': float(np.max(sp['herm'])), 'hart_min': float(np.nanmin(np.array(sp['hart'], float))),
                  'ncc_null_max': int(np.max(sp['ncc_null'])), 'im_rel_max': float(np.max(sp['im_rel'])),
                  'im_rel_je_kl': [float(np.max(np.array(sp['im_rel'])[:, j])) for j in range(len(J[nm]['kl']))],
                  'ovk_gerade_min': float(np.min(sp['ovk_gerade'])), 'ovt_gerade_max': float(np.max(sp['ovt_gerade'])),
                  'fehlwinkel_max_abs': J[nm]['kontrollen']['fehlwinkel_max_abs'],
                  'k0_n0': J[nm]['k0']['n0'], 'zahl_k': int(n0.size)}
    out['nullmoden'] = nz
    U = {}
    # Pipeline-Kontrolle PK (Kuhn-Gitter, reproduziert REGGE-4D-1)
    if 'KW' in K:
        kg = K['KW']['gerade']
        pk = (kg['s0'] is not None and kg['s0'] < 1e-6 and abs(kg['w0_mittel'] / -0.25 - 1) <= 1e-3
              and abs(kg['konf_zu_tt'] + 2) <= 2e-3)
    else:
        pk = False
    U['PK'] = {'urteil': 'bestanden' if pk else 'nicht bestanden', 's0': K.get('KW', {}).get('gerade', {}).get('s0'),
               'w0_mittel': K.get('KW', {}).get('gerade', {}).get('w0_mittel'),
               'konf_zu_tt': K.get('KW', {}).get('gerade', {}).get('konf_zu_tt')}
    # RK0
    teil = {}
    for nm in ('B1-t1', 'B1-t15'):
        if nm in nz:
            z = nz[nm]
            teil[nm] = {'flach': z['fehlwinkel_max_abs'] <= 1e-12,
                        'n0_16': z['n0_min'] == 4 * J[nm]['kontrollen']['NV'] and z['n0_max'] == 4 * J[nm]['kontrollen']['NV'],
                        'luecke': z['luecke_min'] is not None and z['luecke_min'] >= 1e3,
                        'eich': z['HG_max'] <= 1e-12 and z['rG_min'] == 16 and z['rG_max'] == 16
                        and z['sin_null_eich_max'] is not None and z['sin_null_eich_max'] <= 1e-6}
    rk0 = len(teil) == 2 and all(all(v.values()) for v in teil.values())
    U['RK0'] = {'plan': 'eingetroffen' if rk0 else 'nicht eingetroffen', 'karte': 'eingetroffen' if rk0 else 'nicht eingetroffen',
                'teile': teil}
    # RK1
    g1, v1 = K['B1-t1']['gerade'], K['B1-t1']['voll']
    a1 = g1['s0'] is not None and g1['s0'] < 1e-6
    b1 = v1['s0'] is not None and v1['s0'] < 1e-6
    U['RK1'] = {'plan': 'eingetroffen' if a1 else 'nicht eingetroffen', 'karte': urteil_paar(a1, b1),
                's0_gerade': g1['s0'], 's0_voll': v1['s0']}
    # RK2
    a2 = g1['p'] is not None and 1.8 <= g1['p'] <= 2.2
    b2 = v1['p'] is not None and 1.8 <= v1['p'] <= 2.2
    U['RK2'] = {'plan': 'eingetroffen' if a2 else 'nicht eingetroffen', 'karte': urteil_paar(a2, b2),
                'p_gerade': g1['p'], 'p_voll': v1['p']}
    # RK3
    g3, v3 = K['B1-t15']['gerade'], K['B1-t15']['voll']
    a3 = g3['s0_raum'] is not None and g3['s0_raum'] < 1e-6 and abs(g3['R_zeit_raum'] - 1) <= 1e-6
    b3 = v3['s0_raum'] is not None and v3['s0_raum'] < 1e-6 and abs(v3['R_zeit_raum'] - 1) <= 1e-6
    U['RK3'] = {'plan': 'eingetroffen' if a3 else 'nicht eingetroffen', 'karte': urteil_paar(a3, b3),
                's0_raum_gerade': g3['s0_raum'], 'R_gerade': g3['R_zeit_raum'],
                's0_raum_voll': v3['s0_raum'], 'R_voll': v3['R_zeit_raum']}
    if not pk:
        for r in ('RK1', 'RK2', 'RK3'):
            U[r]['plan_vor_PK'] = U[r]['plan']; U[r]['karte_vor_PK'] = U[r]['karte']
            U[r]['plan'] = 'unklar (Pipeline)'; U[r]['karte'] = 'unklar (Pipeline)'
    out['urteile'] = U
    return out


# ================================================================================================= main
def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['gitter', 'auswertung'])
    ap.add_argument('--gitter', default='B1', choices=['B1', 'KW', 'KW2'])
    ap.add_argument('--tau', type=float, default=1.0)
    ap.add_argument('--hoehen-fest', action='store_true')
    ap.add_argument('--pt', action='store_true')
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--ein', nargs='*', default=[])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)),
            'pt_sha256': sha(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pt.py'))}
    if a.modus == 'gitter':
        g = baue(a.gitter, a.tau, a.hoehen_fest)
        res = lauf_gitter(g, rauch=a.rauch, mit_pt=a.pt)
    else:
        pfade = dict(x.split('=', 1) for x in a.ein)
        res = lauf_auswertung(pfade)
    res['info'] = info
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, a.gitter if a.modus == 'gitter' else '', 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
