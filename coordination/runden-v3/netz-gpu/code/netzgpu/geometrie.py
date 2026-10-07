# -*- coding: utf-8 -*-
"""Schwerewellen-Sektor der stetigen Grenze (netzgpu.geometrie), fmhc-physics, 05.10.2026.

Linear um flach, synthetisch, keine Messdaten. Modell wie UEBERLEITUNG-V-2 (RUNDE-37/ueberleitung-v-2/ERGEBNIS.md):
  Kantenwerte q = delta l / l auf den 68 Kanten je primitiver fcc-Zelle von V (Reihenfolge des Projektcodes tg.modell),
  Potential B (3D-Regge), Traegheit M_eff (omega^2-Block der 4D-Zeltstangen-Wirkung bei EINER Hoehe h, Schema ls),
  Lapse-Regel c (R1), Eichung M_disp (Eckverschiebung). Reduktion wie uv.reduktion (ohne statische Richtungen):
  S = orthonormales Komplement von Bild[M_disp, c], Ar = S^H M_eff^-1 S, Br = S^H B S, omega^2 = Eigenwerte von Ar Br;
  die zwei kleinsten sind die TT-Schwerewellen.

Arbeitsteilung:
  Projektcode (alt_geo/, unveraendert kopiert von der .69, CPU/numpy): Bloecke M_eff(k), B(k), c(k), M_disp(k) je k
    (uw.bau, uw.bloecke2, tg.ops, uv.Zuordnung), dazu uv.reduktion als CPU-Gegenprobe.
  Neu (dieses Modul, torch FP64/complex128 auf der GPU): Reduktion und Eigenzerlegung gebuendelt ueber viele k,
    TT-Moden mit Impuls- und Kraftvektoren, spektrale Zeitentwicklung (exakt je Mode, cos/sin), k-Gitter der
    Superzelle, Zuordnung tg-Kante <-> netz.py-Kante (Klasse, Phase e^{i k.R}), Synthese und Analyse im Ortsraum,
    Pruefungen (Eichkern, Regge-Defizit per Differenzenquotient auf netz.py).

Bedienung (Beispiel):
    from netzgpu.netz import Netz
    from netzgpu import geometrie as geo
    P = geo.Projekt(h=2**-10)                       # Projekt-Bloecke (CPU)
    gi = geo.KGitter(10)                            # k der Superzelle 10^3 (Halbmenge)
    bl = P.bloecke_viele(gi.ks)                     # CPU, ca. 0,1 s je k
    sp = geo.reduktion_gpu(bl, gi.ks)               # GPU, gebuendelt
    N = Netz('V', (10, 10, 10)); zo = geo.NetzZuordnung(P, N)
    w = geo.TTWelle(P, zo, gi, sp, sigma=1.0, x0=(5, 5, 5))
    f = w.felder([0.0, 1.0])                        # q, qd, p, Bq je Netzkante, Energie je Ecke
"""
import itertools
import math
import os
import sys
import time

import numpy as np
import torch

HIER = os.path.dirname(os.path.abspath(__file__))
ALT = os.path.join(HIER, 'alt_geo')
H_HAUPT = 2.0 ** -10
TOL_NULL = 1e-10          # wie uw.TOL_NULL
TOL_W = 1e-9              # wie uv.TOL_W
RANG_TOL = 1e-9           # wie hm.zerlege
LUECKE_MAX = 1e-2         # wie hm.LUECKE_MAX
C128 = torch.complex128
F64 = torch.float64


def _alt():
    if ALT not in sys.path:
        sys.path.insert(0, ALT)
    import uw  # noqa: F401  (patcht uv.baue_gitter nur fuer S und B1; V geht unveraendert an uv)
    import uv
    import tg
    return uw, uv, tg


def herm(X):
    return 0.5 * (X + X.conj().transpose(-1, -2))


# ================================================================================================ Projektbloecke (CPU)
class Projekt:
    """Bloecke je k aus dem kopierten Projektcode, Kantenreihenfolge tg (E = 68 Kanten, nV = 10 Ecken je Zelle)."""

    def __init__(self, h=H_HAUPT, netz='V'):
        t0 = time.time()
        self.uw, self.uv, self.tg = _alt()
        vl, mod, LV, zu, _ = self.uw.bau(netz, hs=[h])
        self.V, self.mod, self.LV, self.zu, self.h, self.netz = vl[0], mod, LV, zu, float(h), netz
        self.E, self.nV = int(mod['E']), int(mod['nV'])
        assert self.V.nq == self.E, (self.V.nq, self.E)
        self.lm = float(mod['l'].mean())
        self.t_bau_s = time.time() - t0

    def bloecke(self, ks):
        """M_eff, B, c, M_disp bei einem k (wie uw.punkt2, Paarung a): alles in tg-Reihenfolge."""
        ks = np.asarray(ks, float)
        Bs, _, Md, c = self.tg.ops(self.mod, ks)
        B = self.uv.herm(Bs.toarray())
        S, d = self.uw.bloecke2(self.V, ks)
        if S is None:
            return None, d
        U = self.zu.U(ks)
        nq = self.E
        Meff = self.uv.herm(np.conj(U.T) @ S[2][:nq, :nq] @ U)
        return {'M': Meff, 'B': B, 'c': c, 'Md': Md}, d

    def bloecke_viele(self, ks_liste, log=None, alle=50):
        K, E, nV = len(ks_liste), self.E, self.nV
        out = {'M': np.zeros((K, E, E), complex), 'B': np.zeros((K, E, E), complex),
               'c': np.zeros((K, E, nV), complex), 'Md': np.zeros((K, E, 3 * nV), complex), 'ok': np.zeros(K, bool)}
        gruende = {}
        t0 = time.time()
        for i, ks in enumerate(ks_liste):
            b, d = self.bloecke(ks)
            if b is None:
                g = d.get('grund', '?')
                gruende[g] = gruende.get(g, 0) + 1
                continue
            for x in ('M', 'B', 'c', 'Md'):
                out[x][i] = b[x]
            out['ok'][i] = True
            if log and (i + 1) % alle == 0:
                log('bloecke %d/%d, %.1f s' % (i + 1, K, time.time() - t0))
        out['t_s'] = time.time() - t0
        out['gruende'] = gruende
        return out


# ================================================================================================ Reduktion (GPU)
def reduktion_gpu(bl, ks, dev='cuda', ntt=2, charge=512):
    """Gebuendelte Reduktion R1 wie uv.reduktion (Fall ohne statische Richtungen) fuer K Punkte.

    bl: dict mit M, B (K,E,E), c (K,E,nV), Md (K,E,3nV) (numpy oder torch), ok (K). Rueckgabe (torch auf dev):
      w2 (K,d) aufsteigend; u (K,E,ntt) Moden im q-Raum (B_r-normiert: s^H Br s = 1);
      Bu = B u; P = S Br s (Impulsvektor mal omega^2); gueltig (K) bool; Kennzahlen je k (n_neg, n_null, Luecke ...).
    """
    K = len(ks)
    ks_t = torch.as_tensor(np.asarray(ks, float), dtype=F64, device=dev)
    eps = torch.linalg.norm(ks_t, dim=1)
    res = {k: [] for k in ('w2', 'u', 'Bu', 'P', 'n_null', 'n_neg', 'rang_ok', 'chol_ok', 'rang_rel', 'M_min_rel')}
    for a in range(0, K, charge):
        sl = slice(a, min(a + charge, K))
        M = torch.as_tensor(bl['M'][sl], dtype=C128, device=dev)
        B = torch.as_tensor(bl['B'][sl], dtype=C128, device=dev)
        c = torch.as_tensor(bl['c'][sl], dtype=C128, device=dev)
        Md = torch.as_tensor(bl['Md'][sl], dtype=C128, device=dev)
        ev, Uv = torch.linalg.eigh(herm(M))
        smax = ev.abs().amax(-1, keepdim=True)
        n_null = (ev.abs() <= TOL_NULL * smax).sum(-1)
        n_neg = (ev < -TOL_NULL * smax).sum(-1)
        Ap = (Uv * (1.0 / ev).to(C128).unsqueeze(-2)) @ Uv.conj().transpose(-1, -2)          # M_eff^-1
        X = torch.cat([Md, c], -1)
        nX = X.shape[-1]
        Q, R = torch.linalg.qr(X, mode='complete')
        dR = torch.diagonal(R[:, :nX, :nX], dim1=-2, dim2=-1).abs()
        rrel = dR.amin(-1) / dR.amax(-1)
        S = Q[:, :, nX:]
        SH = S.conj().transpose(-1, -2)
        Ar = herm(SH @ Ap @ S)
        Br = herm(SH @ B @ S)
        L, info = torch.linalg.cholesky_ex(Br)
        LH = L.conj().transpose(-1, -2)
        Mh = herm(LH @ Ar @ L)
        w2, Y = torch.linalg.eigh(Mh)
        s = torch.linalg.solve_triangular(LH, Y[:, :, :ntt], upper=True)                    # s_j = L^-H y_j
        u = S @ s
        res['w2'].append(w2)
        res['u'].append(u)
        res['Bu'].append(B @ u)
        res['P'].append(S @ (Br @ s))
        res['n_null'].append(n_null)
        res['n_neg'].append(n_neg)
        res['rang_ok'].append(rrel > RANG_TOL)
        res['rang_rel'].append(rrel)
        res['chol_ok'].append(info == 0)
        res['M_min_rel'].append(ev.abs().amin(-1) / smax[:, 0])
    out = {k: torch.cat(v, 0) for k, v in res.items()}
    ok_b = torch.as_tensor(np.asarray(bl['ok'], bool), device=dev)
    w2 = out['w2']
    s = w2.abs().amax(-1)
    out['n_wachsend'] = (w2 < -TOL_W * s[:, None]).sum(-1)
    out['luecke'] = w2[:, ntt - 1].abs() / w2[:, ntt].abs()
    out['pos2'] = (w2[:, :ntt] > 0).all(-1)
    out['gueltig'] = ok_b & (out['n_null'] == 0) & out['rang_ok'] & out['chol_ok']
    out['tt_ok'] = out['gueltig'] & out['pos2'] & (out['luecke'] < LUECKE_MAX)
    out['w2k2'] = w2[:, :ntt] / (eps[:, None] ** 2).clamp_min(1e-300)
    out['ks'] = ks_t
    return out


def reduktion_cpu(P, bl, ks, idx):
    """Gegenprobe mit dem Projektcode (uv.reduktion, CPU) an den Punkten idx: w2k2 (2 kleinste) je Punkt."""
    out = []
    for i in idx:
        eps = float(np.linalg.norm(ks[i]))
        r = P.uv.reduktion(bl['M'][i], bl['B'][i], bl['c'][i], bl['Md'][i], eps, TOL_NULL)
        out.append(r.get('w2k2'))
    return out


# ================================================================================================ k-Gitter der Superzelle
class KGitter:
    """Bloch-k einer Superzelle aus n^3 kubischen Zellen von V (fcc): k = 2 pi m / n (1/a), m modulo n * bcc.

    Halbmenge K+ (je Paar +-k einer), ohne die 8 selbstkonjugierten Punkte; ks = kuerzester Vertreter."""

    def __init__(self, n):
        n = int(n)
        self.n = n
        ms = np.array(list(itertools.product(range(2 * n), range(2 * n), range(n))), np.int64)

        def schl(m):
            m = np.mod(m, 2 * n)
            hoch = m[:, 2] >= n
            m[hoch] = np.mod(m[hoch] - n, 2 * n)
            return (m[:, 0] * 2 * n + m[:, 1]) * n + m[:, 2]

        sp, sm = schl(ms.copy()), schl(-ms)
        assert len(np.unique(sp)) == len(ms) == 4 * n ** 3
        self.n_selbst = int((sp == sm).sum())
        mh = ms[sp < sm]
        gs = np.array([g for g in itertools.product(range(-2, 3), repeat=3) if len(set(np.mod(g, 2).tolist())) == 1])
        cand = mh[:, None, :] + n * gs[None, :, :]
        best = cand[np.arange(len(mh)), np.argmin((cand.astype(float) ** 2).sum(-1), 1)]
        self.m = best
        self.ks = 2.0 * np.pi * best / n
        self.K = len(best)
        self.K_voll = 4 * n ** 3


# ================================================================================================ Zuordnung zu netz.py
def _in_fcc(v, tol=1e-9):
    w = 2.0 * np.asarray(v, float)
    r = np.rint(w)
    return bool(np.all(np.abs(w - r) < tol) and int(r.sum()) % 2 == 0)


class NetzZuordnung:
    """tg-Kante e <-> Kantenklasse von netz.py; je Netzkante j: e(j) und fcc-Gittervektor R_j = m_j - mitte_e - s0.

    Ein Kantenwert der tg-Kante e in der Zelle R ist q_e(k) e^{i k.R} (Bloch-Konvention von tg.ops: Zelle der
    Startecke). Die Mitte dieser Kante liegt bei mitte_e + R; also gehoert zu Netzkante j die Phase e^{i k.R_j}."""

    def __init__(self, P, netz):
        t0 = time.time()
        mod = P.mod
        self.netz, self.E = netz, P.E
        mitte = np.asarray(mod['mitte'], float)
        vec = np.asarray(mod['n'] * mod['l'][:, None], float)
        kt = np.asarray(netz.kanten_typ)
        m = np.asarray(netz.kanten_mitte, float)
        kv = netz.kvec.detach().cpu().numpy()
        assert netz.n_kanten_typ == self.E, (netz.n_kanten_typ, self.E)
        _, first = np.unique(kt, return_index=True)
        # globaler Versatz s0 zwischen den Rahmen (erwartet 0: beide aus ew.geometrie)
        self.s0 = None
        for s0 in [np.zeros(3)] + [m[first[0]] - mitte[e] for e in range(self.E)]:
            e_von = np.full(len(first), -1)
            gut = True
            for c, j in enumerate(first):
                d = kv[j]
                kand = [e for e in range(self.E)
                        if np.linalg.norm(np.cross(vec[e], d)) < 1e-9 and abs(np.linalg.norm(vec[e]) - np.linalg.norm(d)) < 1e-9
                        and _in_fcc(m[j] - mitte[e] - s0)]
                if len(kand) != 1:
                    gut = False
                    break
                e_von[c] = kand[0]
            if gut and sorted(e_von.tolist()) == list(range(self.E)):
                self.s0 = s0
                break
        assert self.s0 is not None, 'Zuordnung tg <-> netz.py nicht gefunden'
        self.e_von_typ = e_von
        self.e_j = e_von[kt]
        R = m - mitte[self.e_j] - self.s0
        w = 2.0 * R
        self.fcc_rest = float(np.abs(w - np.rint(w)).max())
        self.fcc_paritaet_ok = bool(np.all(np.mod(np.rint(w).sum(1), 2) == 0))
        self.laenge_rest = float(np.abs(np.linalg.norm(kv, axis=1) - mod['l'][self.e_j]).max())
        self.richtung_rest = float(np.abs(np.cross(kv, vec[self.e_j])).max())
        dev = netz.device
        self.dev = dev
        self.R = torch.as_tensor(R, dtype=F64, device=dev)
        self.idx = [torch.as_tensor(np.nonzero(self.e_j == e)[0], dtype=torch.int64, device=dev) for e in range(self.E)]
        self.N_c = int(len(self.idx[0]))
        assert all(len(ix) == self.N_c for ix in self.idx)
        self.t_s = time.time() - t0

    def info(self):
        return {'versatz_s0': [float(x) for x in self.s0], 'fcc_rest': self.fcc_rest, 'fcc_paritaet_ok': self.fcc_paritaet_ok,
                'laenge_rest': self.laenge_rest, 'richtung_rest': self.richtung_rest, 'N_c': self.N_c, 't_s': self.t_s}

    def synthese(self, F, ks, kblock=1024):
        """F (K,E,nf) komplex (k aus der Halbmenge K+), ks (K,3) -> x (N_k,nf) reell: x_j = sum_k 2 Re[F_k,e(j) e^{ik.R_j}]."""
        ks_t = torch.as_tensor(ks, dtype=F64, device=self.dev)
        F = torch.as_tensor(F, dtype=C128, device=self.dev)
        nf = F.shape[-1]
        out = torch.zeros((self.netz.N_k, nf), dtype=F64, device=self.dev)
        K = ks_t.shape[0]
        for e in range(self.E):
            ix = self.idx[e]
            acc = torch.zeros((len(ix), nf), dtype=C128, device=self.dev)
            for a in range(0, K, kblock):
                ph = torch.exp(1j * (self.R[ix] @ ks_t[a:a + kblock].T))
                acc += ph @ F[a:a + kblock, e, :]
            out[ix] = 2.0 * acc.real
        return out

    def analyse(self, x, ks):
        """x (N_k,) reell -> a (K,E) mit x = sum_alle k a_k e^{ikR}: a_e(k) = (1/N_c) sum_{j in e} x_j e^{-ik.R_j}."""
        ks_t = torch.as_tensor(ks, dtype=F64, device=self.dev)
        x = torch.as_tensor(x, dtype=F64, device=self.dev)
        a = torch.zeros((len(ks), self.E), dtype=C128, device=self.dev)
        for e in range(self.E):
            ix = self.idx[e]
            ph = torch.exp(-1j * (self.R[ix] @ ks_t.T))
            a[:, e] = (x[ix].to(C128) @ ph) / self.N_c
        return a


# ================================================================================================ Pruefungen
def defizit(netz, l):
    """Regge-Defizitwinkel je Netzkante aus Kantenlaengen l (eigene Rechnung auf netz.py, unabhaengig von tg)."""
    from .netz import Netz, PAARE
    X = Netz.einbetten(l[netz.t_kante])
    th = []
    for (i, j) in PAARE:
        k, m = [x for x in range(4) if x not in (i, j)]
        e = X[:, j] - X[:, i]
        e = e / torch.linalg.norm(e, dim=-1, keepdim=True)
        u = X[:, k] - X[:, i]
        u = u - (u * e).sum(-1, keepdim=True) * e
        w = X[:, m] - X[:, i]
        w = w - (w * e).sum(-1, keepdim=True) * e
        cz = (u * w).sum(-1) / (torch.linalg.norm(u, dim=-1) * torch.linalg.norm(w, dim=-1))
        th.append(torch.arccos(cz.clamp(-1.0, 1.0)))
    th = torch.stack(th, 1)
    s = torch.zeros(netz.N_k, dtype=l.dtype, device=l.device)
    s.index_add_(0, netz.t_kante.reshape(-1), th.reshape(-1))
    return 2.0 * math.pi - s


def pruefe_regge(netz, q, Bq, eta=1e-5):
    """delta eps (Differenzenquotient der eigenen Defizitwinkel bei l0 (1 +- eta q)) gegen -(B q)_j / l_j (Projekt-B)."""
    l0 = netz.laengen()
    e0 = defizit(netz, l0)
    dp = defizit(netz, l0 * (1.0 + eta * q))
    dm = defizit(netz, l0 * (1.0 - eta * q))
    de = (dp - dm) / (2.0 * eta)
    ziel = -Bq / l0
    return {'defizit_flach_max': float(e0.abs().max()), 'rel_fehler': float((de - ziel).abs().max() / ziel.abs().max()),
            'ziel_max': float(ziel.abs().max()), 'eta': eta}


def pruefe_eichkern(P, zo, gi, n_k=24, saat=1):
    """Zufaellige Eckverschiebung u auf netz.py -> Dehnung q_j = (u_b - u_a).kvec / l^2 -> Analyse je k muss im Bild
    von M_disp(k) liegen (Zuordnung, Phasen und Kantenvorzeichen zusammen)."""
    netz = zo.netz
    g = torch.Generator(device='cpu').manual_seed(saat)
    u = torch.randn((netz.N_e, 3), generator=g, dtype=F64).to(zo.dev)
    a, b = netz.kanten[:, 0], netz.kanten[:, 1]
    l = netz.laengen()
    q = ((u[b] - u[a]) * netz.kvec).sum(1) / l ** 2
    rng = np.random.default_rng(saat)
    idx = rng.choice(gi.K, size=min(n_k, gi.K), replace=False)
    A = zo.analyse(q, gi.ks[idx]).cpu().numpy()
    rest = []
    for r, i in enumerate(idx):
        _, _, Md, c = P.tg.ops(P.mod, gi.ks[i])
        U_, s_, _ = np.linalg.svd(Md, full_matrices=False)
        Qm = U_[:, s_ > 1e-9 * s_[0]]
        x = A[r]
        rest.append(float(np.linalg.norm(x - Qm @ (np.conj(Qm.T) @ x)) / max(np.linalg.norm(x), 1e-300)))
    return {'k': int(len(idx)), 'rest_max': float(max(rest)), 'rest_median': float(np.median(rest))}


# ================================================================================================ TT-Wellenpaket
def tensor_H(art='zirkular_z'):
    H = np.zeros((3, 3), complex)
    if art == 'zirkular_z':                     # e+ + i ex um z: keine Nullrichtung der TT-Abstrahlung
        H[0, 0], H[1, 1] = 1.0, -1.0
        H[0, 1] = H[1, 0] = 1j
    elif art == 'plus_z':
        H[0, 0], H[1, 1] = 1.0, -1.0
    else:
        raise ValueError(art)
    return H


class TTWelle:
    """Spektral exakte Zeitentwicklung eines TT-Pakets (linear um flach, R1, M_eff bei einem h).

    Anfang: q_ref(k)_e = exp(-|k|^2 sigma^2 / 2) e^{i k.(mitte_e + s0 - x0)} (n_e^T H n_e) / 2, qd = 0; davon nur der
    B_r-orthogonale Anteil in den zwei TT-Moden (c_j = P_j^H q_ref). Je Mode: q = sum_j c_j cos(w_j t) u_j,
    qd = -sum_j c_j w_j sin(w_j t) u_j, p = -sum_j c_j sin(w_j t) / w_j P_j, Bq = sum_j c_j cos(w_j t) Bu_j,
    Energie je k = 1/2 sum_j |c_j|^2 (konstant). Real im Ortsraum: Summe ueber K+ mit 2 Re."""

    def __init__(self, P, zo, gi, sp, sigma=1.0, x0=(0.0, 0.0, 0.0), H='zirkular_z', amplitude=1e-3, ntt=2):
        dev = zo.dev
        self.zo, self.gi, self.dev, self.ntt = zo, gi, dev, ntt
        mod = P.mod
        nvec = np.asarray(mod['n'], float)
        Hm = tensor_H(H) if isinstance(H, str) else np.asarray(H, complex)
        nHn = np.einsum('ei,ij,ej->e', nvec, Hm, nvec) / 2.0
        ks = gi.ks
        ph = np.exp(1j * ((np.asarray(mod['mitte'], float) + zo.s0 - np.asarray(x0, float)[None, :]) @ ks.T)).T  # (K,E)
        g = np.exp(-0.5 * (ks ** 2).sum(1) * sigma ** 2)
        qref = torch.as_tensor(g[:, None] * ph * nHn[None, :], dtype=C128, device=dev)
        self.u = sp['u'][:, :, :ntt]
        self.Bu = sp['Bu'][:, :, :ntt]
        self.Pv = sp['P'][:, :, :ntt]
        w2 = sp['w2'][:, :ntt]
        gueltig = sp['gueltig'] & (w2 > 0).all(-1)
        self.w = torch.sqrt(w2.clamp_min(0.0))
        c = torch.einsum('kej,ke->kj', self.Pv.conj(), qref)
        c = torch.where(gueltig[:, None], c, torch.zeros_like(c))
        self.n_ausgelassen = int((~gueltig).sum())
        self.g_ausgelassen_max = float(np.max(g[~gueltig.cpu().numpy()])) if self.n_ausgelassen else 0.0
        self.c = c
        x = self.zo.synthese(torch.einsum('kj,kej->ke', c, self.u)[:, :, None], ks)[:, 0]
        self.skala = amplitude / float(x.abs().max())
        self.c = c * self.skala
        self.N_c = zo.N_c
        self.sigma, self.x0, self.H = sigma, tuple(float(v) for v in x0), H

    def energie_k(self):
        """Gesamtenergie aus den Modenamplituden (exakt erhalten): 2 N_c sum_K+ 1/2 sum_j |c_j|^2."""
        return float(self.N_c * (self.c.abs() ** 2).sum())

    def koeff(self, zeiten):
        """F (K,E,4T): Spalten q, qd, p, Bq je Zeit (k-Raum)."""
        t = torch.as_tensor(np.asarray(zeiten, float), dtype=F64, device=self.dev)
        wt = self.w[:, :, None] * t[None, None, :]                               # (K,j,T)
        cs, sn = torch.cos(wt), torch.sin(wt)
        winv = torch.where(self.w > 0, 1.0 / self.w, torch.zeros_like(self.w))
        cq = self.c[:, :, None] * cs
        cqd = -self.c[:, :, None] * (self.w[:, :, None] * sn)
        cp = -self.c[:, :, None] * (winv[:, :, None] * sn)
        q = torch.einsum('kjt,kej->ket', cq.to(C128), self.u)
        qd = torch.einsum('kjt,kej->ket', cqd.to(C128), self.u)
        p = torch.einsum('kjt,kej->ket', cp.to(C128), self.Pv)
        Bq = torch.einsum('kjt,kej->ket', cq.to(C128), self.Bu)
        return torch.cat([q, qd, p, Bq], -1), len(zeiten)

    def energie_k_t(self, zeiten):
        """Energie aus den k-Feldern zur Zeit t (Kontrolle der Modenformel): 2 N_c sum 1/2 Re(qd^H p + q^H Bq)."""
        F, T = self.koeff(zeiten)
        q, qd, p, Bq = F[..., :T], F[..., T:2 * T], F[..., 2 * T:3 * T], F[..., 3 * T:]
        e = 0.5 * ((qd.conj() * p).real + (q.conj() * Bq).real).sum((0, 1))
        return (2.0 * self.N_c * e).cpu().numpy()

    def felder(self, zeiten):
        """Reale Felder je Netzkante (N_k, T) fuer q, qd, p, Bq; Energiedichte je Kante und je Ecke."""
        F, T = self.koeff(zeiten)
        x = self.zo.synthese(F, self.gi.ks)
        q, qd, p, Bq = x[:, :T], x[:, T:2 * T], x[:, 2 * T:3 * T], x[:, 3 * T:]
        eps_k = 0.5 * (p * qd + q * Bq)
        netz = self.zo.netz
        e_v = torch.zeros((netz.N_e, T), dtype=F64, device=self.dev)
        e_v.index_add_(0, netz.kanten[:, 0], 0.5 * eps_k)
        e_v.index_add_(0, netz.kanten[:, 1], 0.5 * eps_k)
        return {'q': q, 'qd': qd, 'p': p, 'Bq': Bq, 'eps_kante': eps_k, 'energie_ecke': e_v}


def richtungen_kubisch():
    """[100] (6), [110] (12), [111] (8) als Einheitsvektoren."""
    out = {'100': [], '110': [], '111': []}
    for v in itertools.product((-1, 0, 1), repeat=3):
        nz = sum(1 for x in v if x)
        if nz == 0:
            continue
        out[{1: "100", 2: "110", 3: "111"}[nz]].append(np.array(v, float) / math.sqrt(nz))
    return out


def schalenradien(netz, e_v, x0, rmax, kegel_grad=20.0):
    """Energiegewichteter mittlerer Radius (nur positive Energieanteile) in Kegeln um [100], [110], [111]
    (je ueber alle gleichwertigen Richtungen gepoolt), nur Ecken mit r < rmax. e_v (N_e,) torch."""
    r = netz.ecken_minbild(x0)
    rr = torch.linalg.norm(r, dim=1)
    w = e_v.clamp_min(0.0)
    cmin = math.cos(math.radians(kegel_grad))
    out = {}
    for nm, ds in richtungen_kubisch().items():
        D = torch.as_tensor(np.array(ds), dtype=F64, device=r.device)
        cz = (r @ D.T) / rr.clamp_min(1e-12)[:, None]
        msk = ((cz > cmin) & (rr < rmax)[:, None] & (rr > 1e-9)[:, None]).any(1)
        ww = w[msk]
        out[nm] = float((ww * rr[msk]).sum() / ww.sum().clamp_min(1e-300))
    v = np.array([out['100'], out['110'], out['111']])
    out['spanne'] = float(v.max() / v.min() - 1.0)
    return out
