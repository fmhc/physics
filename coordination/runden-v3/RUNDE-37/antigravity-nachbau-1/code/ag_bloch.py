#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ANTIGRAVITY-NACHBAU-1 (fmhc-physics, RUNDE-37), Rechen-Agent fuer die Leitung claude-primary.

Teile (Konventionen in VORAB.md):
  ag1   alle Z2-Vorzeichenmuster der kubischen Diamantzelle (8 Knoten, 16 Kanten): Nullstellenmenge und Dimension
  ag5   Eichprobe der eta-Phasen aus dirac_gitter_gpu.py auf dem endlichen Torus (L = 3, 4)
  dim   1D-Kette, 2D-Wabe, 3D-Diamant (ohne und mit Spin-Bahn, FKM) inkl. Spannung (higgs_masse_hierarchie.py)
  teilc Peierls-Kopplung und Noether-Strom (THEORIE-ABC.md Teil C) auf einem Zufallsgraphen
  zahlen AG3 (PPN), AG4 (Lense-Thirring-Phase), gravity_nearfield (alpha, Horizontlage), Pachner-Ziel
Nur numpy/scipy, CPU, 1 Thread.
"""
import json, sys, time, itertools, platform
import numpy as np
import scipy
from scipy import ndimage, optimize

D = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)   # Einheit a/4, a = 4
APOS = np.array([[0, 0, 0], [0, 2, 2], [2, 0, 2], [2, 2, 0]], float)
OUT = {}


# ------------------------------------------------------------------ Zelle und Kanten
def zellkanten():
    ed = []
    for s in range(4):
        for mu in range(4):
            t = (APOS[s] + D[mu]) % 4
            b = int(np.nonzero(np.all(np.isclose(APOS, (t - 1) % 4), 1))[0][0])
            kreuz_x = (APOS[s] + D[mu])[0] < 0
            kreuz = tuple(bool((APOS[s] + D[mu])[i] < 0) for i in range(3))
            ed.append((s, b, mu, kreuz))
    return ed


ED = zellkanten()
assert len(ED) == 16


def baum():
    """BFS-Baum ueber Knoten 0..3 (A), 4..7 (B)."""
    adj = {v: [] for v in range(8)}
    for e, (s, b, mu, _) in enumerate(ED):
        adj[s].append((4 + b, e))
        adj[4 + b].append((s, e))
    seen, tree, q = {0}, [], [0]
    while q:
        v = q.pop(0)
        for w, e in adj[v]:
            if w not in seen:
                seen.add(w)
                tree.append(e)
                q.append(w)
    assert len(seen) == 8 and len(tree) == 7
    return tree


TREE = baum()
COTREE = [e for e in range(16) if e not in TREE]


def eich_fix(sig):
    """Vorzeichen (16) -> Eichung mit Baumkanten +1; Rueckgabe Ko-Baum-Tupel."""
    pot = {0: 1}
    changed = True
    while len(pot) < 8:
        for e in TREE:
            s, b, _, _ = ED[e]
            u, w = s, 4 + b
            if u in pot and w not in pot:
                pot[w] = pot[u] * sig[e]
            elif w in pot and u not in pot:
                pot[u] = pot[w] * sig[e]
    out = []
    for e in range(16):
        s, b, _, _ = ED[e]
        out.append(sig[e] * pot[s] * pot[4 + b])
    assert all(out[e] == 1 for e in TREE)
    return tuple(out[e] for e in COTREE)


def windung(i):
    return np.array([-1 if ED[e][3][i] else 1 for e in range(16)])


def muster(cot):
    sig = np.ones(16, int)
    for c, e in zip(cot, COTREE):
        sig[e] = c
    return sig


def kgitter(N, seite):
    n = (np.arange(N) + 0.5) / N * seite
    return np.stack(np.meshgrid(n, n, n, indexing='ij'), -1).reshape(-1, 3)


def smin_zelle(sig, K):
    P = np.exp(1j * (K @ D.T))                      # (nk, 4)
    De = np.zeros((len(K), 4, 4), complex)
    for e, (s, b, mu, _) in enumerate(ED):
        De[:, s, b] += sig[e] * P[:, mu]
    M = np.einsum('kab,kac->kbc', De.conj(), De)
    return np.sqrt(np.clip(np.linalg.eigvalsh(M)[:, 0], 0, None))


def cluster_periodisch(maske):
    lab, n = ndimage.label(maske)
    if n == 0:
        return 0
    par = list(range(n + 1))

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for ax in range(3):
        a = np.take(lab, 0, axis=ax)
        b = np.take(lab, -1, axis=ax)
        for u, v in zip(a[(a > 0) & (b > 0)], b[(a > 0) & (b > 0)]):
            ru, rv = f(u), f(v)
            if ru != rv:
                par[ru] = rv
    return len({f(i) for i in range(1, n + 1)})


def ag1():
    seite = np.pi / 2                                # reziproke Zelle der kubischen Superzelle (Periode 4)
    Ns = (16, 32)
    KAPPA = 3.0                                      # tau = KAPPA * h, h = seite / N
    klassen = {}
    for bits in itertools.product((1, -1), repeat=9):
        sig = muster(bits)
        rep = min(eich_fix(sig * (windung(0) if wx else 1) * (windung(1) if wy else 1) * (windung(2) if wz else 1))
                  for wx in (0, 1) for wy in (0, 1) for wz in (0, 1))
        klassen.setdefault(rep, []).append(bits)
    res = []
    for rep, mitglieder in sorted(klassen.items()):
        sig = muster(rep)
        treffer, smin, cl = [], [], None
        for N in Ns:
            K = kgitter(N, seite)
            s = smin_zelle(sig, K)
            tau = KAPPA * seite / N
            m = s < tau
            treffer.append(int(m.sum()))
            smin.append(float(s.min()))
            if N == Ns[-1]:
                cl = cluster_periodisch(m.reshape(N, N, N))
        if treffer[-1] == 0:
            art, Dm = 'gelueckt', None
        else:
            Dm = float(np.log2(treffer[1] / max(treffer[0], 1)))
            art = 'punkte' if Dm < 0.5 else 'linien' if Dm < 1.5 else 'flaechen' if Dm < 2.5 else 'flachband'
        minus = int((sig < 0).sum())
        res.append({'rep': list(rep), 'n_muster': len(mitglieder), 'n_minus_kanten': minus, 'treffer': treffer,
                    'D': Dm, 'art': art, 'cluster_N32': cl, 'smin': smin})
    # Punktfaelle genauer: Zahl der Cluster bei N = 48 und Minimum nach Nelder-Mead je Cluster nicht noetig fuer Zaehlung
    for r in res:
        if r['art'] == 'punkte':
            N = 48
            K = kgitter(N, seite)
            s = smin_zelle(muster(r['rep']), K)
            m = s < KAPPA * seite / N
            r['cluster_N48'] = cluster_periodisch(m.reshape(N, N, N))
            r['treffer_N48'] = int(m.sum())
    zus = {}
    for r in res:
        zus[r['art']] = zus.get(r['art'], 0) + 1
    drei = [r for r in res if r['art'] == 'punkte' and r.get('cluster_N48') == 3]
    plain = [r for r in res if r['n_minus_kanten'] == 0]
    OUT['ag1'] = {'n_klassen': len(res), 'klassen_je_art': zus, 'genau_drei_isolierte': len(drei),
                  'drei_details': drei, 'schlicht_alle_plus': plain, 'klassen': res,
                  'kappa': KAPPA, 'N': list(Ns) + [48], 'cotree': COTREE, 'tree': TREE}


# ------------------------------------------------------------------ AG5 / dirac_gitter_gpu.py: Eichprobe
def torus_H(L, eta):
    A = []
    for x, y, z in itertools.product(range(L), repeat=3):
        for a in APOS:
            A.append(np.array([4 * x, 4 * y, 4 * z]) + a)
    A = np.array(A)
    B = A + 1
    idx = {tuple((b % (4 * L)).astype(int)): i for i, b in enumerate(B)}
    n = len(A)
    H = np.zeros((2 * n, 2 * n), complex)
    for i, a in enumerate(A):
        for mu in range(4):
            j = idx[tuple(((a + D[mu]) % (4 * L)).astype(int))]
            H[i, n + j] += eta[mu]
    H = H + H.conj().T
    return np.linalg.eigvalsh(H)


def ag5():
    eta = np.array([1.0, -1.0, 1j, -1j])
    r = {}
    for L in (3, 4):
        e1 = torus_H(L, np.ones(4))
        e2 = torus_H(L, eta)
        r['L%d' % L] = {'N_knoten': len(e1), 'max_abw_sortiert': float(np.abs(np.sort(e1) - np.sort(e2)).max()),
                        'Emin_abs_eta1': float(np.abs(e1).min()), 'Emin_abs_eta': float(np.abs(e2).min()),
                        'n_null_eta1': int((np.abs(e1) < 1e-9).sum()), 'n_null_eta': int((np.abs(e2) < 1e-9).sum())}
    # k0, phi mit eta_mu = exp(i (k0.d_mu + phi))
    th = np.array([0.0, np.pi, np.pi / 2, -np.pi / 2])
    Mx = np.hstack([D, np.ones((4, 1))])
    sol = np.linalg.solve(Mx, th)
    r['k0'] = sol[:3].tolist()
    r['phi'] = float(sol[3])
    r['probe_eta'] = float(np.abs(np.exp(1j * (D @ sol[:3] + sol[3])) - eta).max())
    # schlichter Diamant (= Fadenende mit Fluss +1, TWIST-SPIN-1): Nullstellen-Dimension in der primitiven Zone
    Ns = (24, 48)
    tr = []
    for N in Ns:
        K = kgitter(N, np.pi)
        f = np.abs(np.exp(1j * (K @ D.T)).sum(1))
        tr.append(int((f < 3.0 * np.pi / N).sum()))
    r['schlicht_treffer'] = tr
    r['schlicht_D'] = float(np.log2(tr[1] / tr[0]))
    # Probe: Linie X-W, k = (pi/2, s, 0)
    s = np.linspace(0, np.pi / 4, 9)
    K = np.stack([np.full_like(s, np.pi / 2), s, 0 * s], 1)
    r['linie_X_W_max'] = float(np.abs(np.exp(1j * (K @ D.T)).sum(1)).max())
    OUT['ag5'] = r


# ------------------------------------------------------------------ 1D, 2D, 3D und Higgs-Skript
A1 = np.array([0, 2, 2.0]); A2 = np.array([2, 0, 2.0]); A3 = np.array([2, 2, 0.0])
XS = np.array([[np.pi / 2, 0, 0], [0, np.pi / 2, 0], [0, 0, np.pi / 2]])


def fkm_betrag(K, t, lam):
    """FKM d-Vektor (DIAMANT-NULLSTELLEN-1, fkm_dvektor) mit Bindungsspannung: t = (t0, t1, t2, t3)."""
    x1, x2, x3 = K @ A1, K @ A2, K @ A3
    d1 = t[0] + t[1] * np.cos(x1) + t[2] * np.cos(x2) + t[3] * np.cos(x3)
    d2 = t[1] * np.sin(x1) + t[2] * np.sin(x2) + t[3] * np.sin(x3)
    s = np.sin
    d3 = 2 * lam * (s(x2) - s(x3) - s(x2 - x1) + s(x3 - x1))
    d4 = 2 * lam * (s(x3) - s(x1) - s(x3 - x2) + s(x1 - x2))
    d5 = 2 * lam * (s(x1) - s(x2) - s(x1 - x3) + s(x2 - x3))
    return np.sqrt(d1 ** 2 + d2 ** 2 + d3 ** 2 + d4 ** 2 + d5 ** 2)


def ag_higgs_masse(t):
    """woertlich higgs_masse_hierarchie.f_k an den drei Punkten (pi/2,0,0) usw."""
    out = []
    for k in XS:
        ph = D @ k
        out.append(float(np.hypot((t * np.cos(ph)).sum(), (t * np.sin(ph)).sum())))
    return out


def zone_min(fn, N=96, verfeinern=True):
    K = kgitter(N, np.pi)
    v = fn(K)
    i = np.argsort(v)[:20]
    best = (float(v[i[0]]), K[i[0]])
    if verfeinern:
        for j in i:
            r = optimize.minimize(lambda k: float(fn(k[None, :])[0]), K[j], method='Nelder-Mead',
                                  options={'xatol': 1e-10, 'fatol': 1e-14, 'maxiter': 4000})
            if r.fun < best[0]:
                best = (float(r.fun), r.x)
    return best[0], (best[1] % np.pi).tolist()


def dim():
    r = {}
    k = np.linspace(0, 2 * np.pi, 20001)[:-1]
    for t2 in (1.0, 1.2):
        f = np.abs(1 + t2 * np.exp(1j * k))
        r['1D_t2=%g' % t2] = {'min': float(f.min()), 'k_min': float(k[f.argmin()])}
    g = np.linspace(0, 2 * np.pi, 1201)[:-1]
    k1, k2 = np.meshgrid(g, g, indexing='ij')
    for t3 in (1.0, 1.5, 2.2):
        f = np.abs(1 + np.exp(1j * k1) + t3 * np.exp(1j * k2))
        m = f < 3 * 2 * np.pi / 1200
        lab, n = ndimage.label(m)
        r['2D_t3=%g' % t3] = {'min': float(f.min()), 'cluster_grob': int(n)}
    # 3D ohne Spin-Bahn, Higgs-Spannung aus dem Skript
    strain = np.array([-0.15, 0.05, 0.25, -0.01])
    t = 1 + strain
    plain = lambda K, t=t: np.abs((t[None, :] * np.exp(1j * (K @ D.T))).sum(1))  # noqa: E731
    r['3D_ohneSB_symm_X'] = ag_higgs_masse(np.ones(4))
    r['3D_ohneSB_spannung_X'] = ag_higgs_masse(t)
    r['3D_ohneSB_spannung_zonenmin'] = zone_min(plain)
    # Treffer-Skalierung mit Spannung (Linien?)
    tr = []
    for N in (24, 48):
        K = kgitter(N, np.pi)
        tr.append(int((plain(K) < 3 * np.pi / N).sum()))
    r['3D_ohneSB_spannung_treffer'] = tr
    # FKM: isotrop und mit Skript-Spannung
    lam = 0.25
    r['FKM_iso_X'] = [float(fkm_betrag(x[None, :], np.ones(4), lam)[0]) for x in XS]
    r['FKM_iso_zonenmin'] = zone_min(lambda K: fkm_betrag(K, np.ones(4), lam))
    r['FKM_spannung_X'] = [float(fkm_betrag(x[None, :], t, lam)[0]) for x in XS]
    r['FKM_spannung_zonenmin'] = zone_min(lambda K: fkm_betrag(K, t, lam))
    # beliebige Hierarchie einstellen: e : mu : tau = 0,511 : 105,66 : 1776,86 MeV, groesste Masse 0,5 t
    ziel = np.array([0.51099895, 105.6583755, 1776.86]) / 1776.86 * 0.5
    C = np.array([[1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]], float)
    # t0 = 1, Vorzeichen so, dass alle t positiv
    best = None
    for sg in itertools.product((1, -1), repeat=3):
        rhs = np.array(sg) * ziel - C[:, 0]
        tt = np.linalg.solve(C[:, 1:], rhs)
        tv = np.concatenate([[1.0], tt])
        if np.all(tv > 0) and (best is None or np.abs(tv - 1).max() < np.abs(best - 1).max()):
            best = tv
    r['hierarchie_t'] = best.tolist()
    r['hierarchie_X_skript'] = ag_higgs_masse(best)
    r['hierarchie_FKM_X'] = [float(fkm_betrag(x[None, :], best, lam)[0]) for x in XS]
    r['hierarchie_FKM_zonenmin'] = zone_min(lambda K: fkm_betrag(K, best, lam))
    r['hierarchie_ohneSB_zonenmin'] = zone_min(lambda K: np.abs((best[None, :] * np.exp(1j * (K @ D.T))).sum(1)))
    r['hierarchie_verhaeltnis_X'] = (np.array(sorted(r['hierarchie_X_skript'])) / sorted(r['hierarchie_X_skript'])[0]).tolist()
    OUT['dim'] = r


# ------------------------------------------------------------------ Teil C
def teilc(seed=7):
    rng = np.random.default_rng(seed)
    n = 12
    kanten = set()
    for i in range(n):
        kanten.add((i, (i + 1) % n))
    while len(kanten) < 30:
        i, j = rng.integers(0, n, 2)
        if i != j and (j, i) not in kanten:
            kanten.add((int(i), int(j)))
    kanten = sorted(kanten)
    W = rng.uniform(0.5, 1.5, len(kanten))
    V = rng.uniform(0.5, 1.5, n)
    A = rng.uniform(-np.pi, np.pi, len(kanten))
    q, m2, lam4 = 1.0, 0.7, 0.3
    phi = rng.normal(size=n) + 1j * rng.normal(size=n)
    phid = rng.normal(size=n) + 1j * rng.normal(size=n)

    def lagr(phi, phid, A, A0):
        kin = (V * np.abs(phid - 1j * q * A0 * phi) ** 2).sum()
        pot = (V * (m2 * np.abs(phi) ** 2 + lam4 * np.abs(phi) ** 4)).sum()
        gr = sum(W[e] * abs(phi[j] - np.exp(1j * q * A[e]) * phi[i]) ** 2 for e, (i, j) in enumerate(kanten))
        return kin - pot - gr

    def beschl(phi, A):
        acc = -(m2 + 2 * lam4 * np.abs(phi) ** 2) * phi * V
        for e, (i, j) in enumerate(kanten):
            U = np.exp(1j * q * A[e])
            acc[i] += W[e] * (np.conj(U) * phi[j] - phi[i])
            acc[j] += W[e] * (U * phi[i] - phi[j])
        return acc / V

    def energie(phi, phid, A):
        pot = (V * (m2 * np.abs(phi) ** 2 + lam4 * np.abs(phi) ** 4)).sum()
        gr = sum(W[e] * abs(phi[j] - np.exp(1j * q * A[e]) * phi[i]) ** 2 for e, (i, j) in enumerate(kanten))
        return (V * np.abs(phid) ** 2).sum() + pot + gr

    r = {}
    # 1. Bewegungsgleichung pruefen: dH/dt = 0 (zentral, kleiner Zeitschritt)
    h = 1e-5
    acc = beschl(phi, A)
    Hp = energie(phi + h * phid + 0.5 * h * h * acc, phid + h * acc, A)
    Hm = energie(phi - h * phid + 0.5 * h * h * acc, phid - h * acc, A)
    r['dHdt_rel'] = float(abs(Hp - Hm) / (2 * h) / energie(phi, phid, A))
    # 2. J = dS/dA_ij numerisch (Definition aus THEORIE-ABC.md) gegen Formeln
    A0 = np.zeros(n)
    Jnum = np.zeros(len(kanten))
    for e in range(len(kanten)):
        Ap, Am = A.copy(), A.copy()
        Ap[e] += 1e-6
        Am[e] -= 1e-6
        Jnum[e] = (lagr(phi, phid, Ap, A0) - lagr(phi, phid, Am, A0)) / 2e-6
    J_ag = np.array([2 * q * W[e] * np.imag(np.conj(phi[i]) * np.exp(1j * q * A[e]) * phi[j]) for e, (i, j) in enumerate(kanten)])
    J_kor = np.array([2 * q * W[e] * np.imag(np.conj(phi[i]) * np.exp(-1j * q * A[e]) * phi[j]) for e, (i, j) in enumerate(kanten)])
    sk = np.abs(Jnum).max()
    r['J_num_gegen_AG_rel'] = float(np.abs(Jnum - J_ag).max() / sk)
    r['J_num_gegen_korrigiert_rel'] = float(np.abs(Jnum - J_kor).max() / sk)
    Qnum = np.zeros(n)
    for i in range(n):
        Ap0, Am0 = A0.copy(), A0.copy()
        Ap0[i] += 1e-6
        Am0[i] -= 1e-6
        Qnum[i] = (lagr(phi, phid, A, Ap0) - lagr(phi, phid, A, Am0)) / 2e-6
    Q_ag = 2 * q * V * np.imag(np.conj(phi) * phid)
    r['Q_num_gegen_AG_rel'] = float(np.abs(Qnum - Q_ag).max() / np.abs(Qnum).max())
    r['Q_num_gegen_minusAG_rel'] = float(np.abs(Qnum + Q_ag).max() / np.abs(Qnum).max())
    # 3. Eichinvarianz
    chi = rng.uniform(-np.pi, np.pi, n)
    phi2 = phi * np.exp(1j * chi)
    A2 = np.array([A[e] + (chi[j] - chi[i]) / q for e, (i, j) in enumerate(kanten)])
    J_ag2 = np.array([2 * q * W[e] * np.imag(np.conj(phi2[i]) * np.exp(1j * q * A2[e]) * phi2[j]) for e, (i, j) in enumerate(kanten)])
    J_kor2 = np.array([2 * q * W[e] * np.imag(np.conj(phi2[i]) * np.exp(-1j * q * A2[e]) * phi2[j]) for e, (i, j) in enumerate(kanten)])
    r['eich_AG_max_abw_rel'] = float(np.abs(J_ag2 - J_ag).max() / np.abs(J_ag).max())
    r['eich_korrigiert_max_abw_rel'] = float(np.abs(J_kor2 - J_kor).max() / np.abs(J_kor).max())
    # 4. Kontinuitaet dQ_i/dt + sum_j J_ij = 0 (J_ij von i nach j orientiert: J_ji = -J_ij)
    dQ_kor = -2 * q * V * np.imag(np.conj(phi) * acc)          # Q = dS/dA0 = -2qV Im(phi* phid)
    dQ_ag = 2 * q * V * np.imag(np.conj(phi) * acc)

    def divergenz(J):
        dv = np.zeros(n)
        for e, (i, j) in enumerate(kanten):
            dv[i] += J[e]
            dv[j] -= J[e]
        return dv
    sk = np.abs(dQ_kor).max()
    r['kont_num_Q_num_J'] = float(np.abs(dQ_kor + divergenz(Jnum)).max() / sk)
    r['kont_AG_woertlich'] = float(np.abs(dQ_ag + divergenz(J_ag)).max() / sk)
    r['kont_AG_Q_mit_kor_J'] = float(np.abs(dQ_ag + divergenz(J_kor)).max() / sk)
    r['kont_AG_Q_minus_kor_J'] = float(np.abs(dQ_ag - divergenz(J_kor)).max() / sk)
    r['kont_num_Q_minus_num_J'] = float(np.abs(dQ_kor - divergenz(Jnum)).max() / sk)
    r['A_ungleich_0'] = True
    OUT['teilc'] = r


# ------------------------------------------------------------------ Zahlen AG3, AG4, Gravitation, Pachner-Ziel
def zahlen():
    G, c, hbar = 6.67430e-11, 299792458.0, 1.054571817e-34
    MeV = 1.602176634e-13
    lP = np.sqrt(hbar * G / c ** 3)
    r = {}
    rows = []
    for name, J, E, b in (('Elektron, 1 MeV, b = 1 fm', hbar / 2, 1 * MeV, 1e-15),
                          ('Elektron, 1 MeV, b = Compton 3,86e-13 m', hbar / 2, 1 * MeV, 3.8616e-13),
                          ('Elektron, 1 GeV, b = 1e-18 m', hbar / 2, 1000 * MeV, 1e-18),
                          ('AG-Skript: J = 1e-34, lambda = 1 pm, b = 1 fm', 1e-34, 2 * np.pi * hbar * c / 1e-12, 1e-15)):
        dphi = 4 * G * J * E / (hbar * c ** 4 * b)
        ag = 4 * G * J * E / (hbar * c ** 5 * b ** 2)         # Formel des Skripts, Einheit s/m^2
        rows.append({'fall': name, 'dphi_LT_rad': dphi, 'log10': float(np.log10(dphi)),
                     'skriptformel_wert_in_s_pro_m2': ag})
    r['ag4'] = rows
    r['ag4_bezug_rad'] = {'atominterferometer_pro_schuss': 1e-3, 'optisch_beste_grob': 1e-10}
    # AG3
    gam = (0.999, 1.000, 1.001)
    out = []
    for lab, b in (('A_min', 1.00), ('A_max', 1.02), ('B', 0.95), ('B_min', 0.90), ('B_max', 1.00)):
        out.append({'beta': lab, 'P_gamma1': (2 + 2 * 1.0 - b) / 3, 'P_gamma0.999': (2 + 2 * 0.999 - b) / 3,
                    'P_gamma1.001': (2 + 2 * 1.001 - b) / 3})
    r['ag3'] = out
    # gravity_nearfield_collapse.py
    eps = (-1 + np.sqrt(1 + 4 * 1.5)) / (2 * 1.5)
    r['grav_horizont_eps'] = eps
    r['grav_horizont_r_durch_Rs'] = 1 / eps

    def orbit(alpha, Rs=1.0, r0=10.0, v0=0.3, dt=0.01):
        rx, ry, vx, vy = r0, 0.0, 0.0, v0
        per, prev = [], 0.0
        for _ in range(int(12000 / dt)):
            rn = np.hypot(rx, ry)
            a = -0.5 * (Rs / rn ** 2 + 2 * alpha * Rs ** 2 / rn ** 3)
            vx += a * rx / rn * dt; vy += a * ry / rn * dt
            rx += vx * dt; ry += vy * dt
            d = rx * vx + ry * vy
            if d > 0 and prev <= 0:
                per.append(np.arctan2(ry, rx))
                if len(per) == 3:
                    break
            prev = d
        dp = (per[2] - per[1]) % (2 * np.pi)
        if dp > np.pi:
            dp -= 2 * np.pi
        return dp
    # Bahnparameter p = L^2/(GM), GM = Rs/2 (c = 1)
    Lm = 10.0 * 0.3
    p = Lm ** 2 / 0.5
    rr = {}
    for al in (0.0, 1.5):
        rr['alpha=%g' % al] = orbit(al)
    for dt in (0.01, 0.002):
        rr['alpha=1.5_minus_0_dt%g' % dt] = orbit(1.5, dt=dt) - orbit(0.0, dt=dt)
    rr['ART_erste_Ordnung_3piRs_p'] = 3 * np.pi * 1.0 / p
    rr['Formel_2pi_alpha_Rs_p'] = 2 * np.pi * 1.5 / p
    rr['exakt_zentrifugal'] = 2 * np.pi * (Lm / np.sqrt(Lm ** 2 - 1.5 * 1.0) - 1)
    rr['p'] = p
    r['grav_perihel'] = rr
    # Pachner-Ziel
    M = np.ones((6, 6)); M[0, 0] = 0
    M[1:, 1:] = np.ones((5, 5)) - np.eye(5)
    r['pachner_V4_regulaer'] = float(np.sqrt(np.linalg.det(M) / 9216))
    r['pachner_ziel_skript'] = float(np.sqrt(5 / 96))
    r['sqrt5_durch_96'] = float(np.sqrt(5) / 96)
    xs = np.linspace(0.0, 4.0, 4001)
    v = []
    for x in xs:
        Mx = M.copy(); Mx[1, 5] = Mx[5, 1] = x
        v.append(np.linalg.det(Mx) / 9216)
    v = np.array(v)
    r['pachner_V4_max_ueber_x'] = float(np.sqrt(v.max()))
    r['pachner_x_bei_max'] = float(xs[v.argmax()])
    r['lP'] = lP
    OUT['zahlen'] = r


if __name__ == '__main__':
    t0 = time.time()
    teile = sys.argv[2:] or ['ag1', 'ag5', 'dim', 'teilc', 'zahlen']
    for tname in teile:
        t1 = time.time()
        globals()[tname]()
        OUT.setdefault('zeiten', {})[tname] = time.time() - t1
        print(tname, 'fertig %.1f s' % (time.time() - t1), flush=True)
    OUT['info'] = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
                   'host': platform.node(), 'argv': sys.argv, 'laufzeit_s': time.time() - t0}
    with open(sys.argv[1], 'w') as fh:
        json.dump(OUT, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
