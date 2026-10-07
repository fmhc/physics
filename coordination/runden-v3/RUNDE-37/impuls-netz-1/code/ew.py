#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EINE-WELT-LOCH-1, Runde 41 (fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Allgemeiner Bloch-Baukasten fuer linearisierte Regge-Netze mit Hamilton-Dynamik wie TENSOR-EIS-PYRO-1:
  Kantenwerte a_e = delta l / l, Potential B = l (sum_t d theta_t / d l) l (Regge), Eichung = Eckverschiebung,
  skalare Regel je Ecke sum_{e an v} l_e eps_e, Bewegungsenergie je markierter Zelle (n_e . n_f)^2 - 1/2.
Netze (Argument --fuellung):
  ohne : zwei Kopien von TENSOR-EIS-PYRO-1 (B1 ohne Fuellung; Ecken = Mitten, Staebe = verdoppelte Finn-Kanten,
         Zellen = Tetraeder-Oktaeder-Wabe, Bewegungsenergie nur auf Finns Tetraedern)
  V    : Pyrochlor + Lochmitte C (12 Speichen) + Sechseckmitte H (6 Speichen) + Kanten C-H (Standard)
  S    : Pyrochlor + Lochmitte C (12 Speichen) + Achse C1-C2 durch jedes Sechseck (kantenaermer)
TENSOR-EIS-PYRO-1/code/tp.py wird unveraendert importiert (dieder, tt_anteil, B6, ops_pyro fuer die Gegenprobe).
Koordinaten: kubische Kante 1, Positionen ganzzahlig in Einheiten 1/8.
"""
import argparse, json, sys, time, platform, os, resource, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402  (TENSOR-EIS-PYRO-1, sha256 419d7da6..., unveraendert)

AV = tp.AV
BV = tp.BV
R8 = tp.R8
AV8 = np.rint(AV * 8).astype(int)
AV8INV = np.linalg.inv(AV8.astype(float))
E3 = np.eye(3, dtype=int)


# ------------------------------------------------------------------------------------------------ Geometrie
def zerlege(x8, pos8):
    """Untergitter s und Gitterkoeffizienten n (in a1..a3) mit x8 = pos8[s] + n @ AV8."""
    for s, p in enumerate(pos8):
        n = (np.asarray(x8, float) - p) @ AV8INV
        if np.allclose(n, np.rint(n), atol=1e-9):
            return s, tuple(int(v) for v in np.rint(n))
    raise ValueError('kein Gitterplatz: %s' % (x8,))


def tet(ecken, kin=True, art='tet'):
    X = [np.asarray(x, int) for x in ecken]
    fl = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    return {'X8': X, 'flaechen': fl, 'kin': kin, 'art': art}


def okt(mitte8):
    m = np.asarray(mitte8, int)
    X = []
    for i in range(3):
        X.append(m + 4 * E3[i])
        X.append(m - 4 * E3[i])
    fl = []
    for sx in (0, 1):
        for sy in (0, 1):
            for sz in (0, 1):
                fl.append((0 + sx, 2 + sy, 4 + sz))
    return {'X8': X, 'flaechen': fl, 'kin': False, 'art': 'okt'}


def sechseck_zyklus(punkte):
    """Ordnet 6 Punkte (x8) zyklisch nach Nachbarschaft im Abstand l_P (|diff|^2 = 8 in Einheiten 1/8)."""
    P = [np.asarray(p, int) for p in punkte]
    n = len(P)
    nb = {i: [j for j in range(n) if j != i and int(((P[i] - P[j]) ** 2).sum()) == 8] for i in range(n)}
    assert all(len(v) == 2 for v in nb.values()), nb
    zyk = [0, nb[0][0]]
    while len(zyk) < n:
        nxt = [j for j in nb[zyk[-1]] if j != zyk[-2]][0]
        zyk.append(nxt)
    assert zyk[0] in nb[zyk[-1]]
    return [P[i] for i in zyk]


def geometrie(fuellung):
    zellen = []
    if fuellung == 'ohne':
        D0 = np.array([2, 2, 2])
        C1 = np.array([-2, -2, -2])
        C2 = np.array([4, 4, 4])
        pos8 = [D0, np.zeros(3, int)]                                   # Kopie 1: Ab-Mitten, Kopie 2: Auf-Mitten
        # Kopie 1 (Ecken = Ab-Mitten): Finns Auf-Tetraeder verdoppelt (Mitte U = 0), Gegentetraeder (Mitte C2), Oktaeder (C1)
        zellen.append(tet([2 * R8[a] for a in range(4)], kin=True, art='finn1'))
        zellen.append(tet([C2 - 2 * R8[a] for a in range(4)], kin=False, art='gegen1'))
        zellen.append(okt(C1))
        # Kopie 2 (Ecken = Auf-Mitten): Finns Ab-Tetraeder verdoppelt (Mitte D0), Gegentetraeder (Mitte C1), Oktaeder (C2)
        zellen.append(tet([D0 - 2 * R8[b] for b in range(4)], kin=True, art='finn2'))
        zellen.append(tet([C1 + 2 * R8[a] for a in range(4)], kin=False, art='gegen2'))
        zellen.append(okt(C2))
        return pos8, zellen
    C1 = np.array([-2, -2, -2])
    C2 = np.array([4, 4, 4])
    pos8 = [R8[a].astype(int) for a in range(4)] + [C1, C2]
    if fuellung == 'V':
        pos8 += [C1 - R8[a] for a in range(4)]
    zellen.append(tet([R8[a] for a in range(4)], art='finn_auf'))
    zellen.append(tet([np.array([2, 2, 2]) - R8[b] for b in range(4)], art='finn_ab'))
    for c, sg, name in ((C1, 1, 'T1'), (C2, -1, 'T2')):
        for a in range(4):
            zellen.append(tet([c] + [c + sg * (2 * R8[a] + R8[b]) for b in range(4) if b != a], art='kegel_' + name))
        for a in range(4):
            sechs = [c + sg * (2 * R8[b] + R8[d]) for b in range(4) for d in range(4) if a not in (b, d) and b != d]
            zyk = sechseck_zyklus(sechs)
            if fuellung == 'V':
                H = c - sg * R8[a]
                for i in range(6):
                    zellen.append(tet([c, H, zyk[i], zyk[(i + 1) % 6]], art='sechs_' + name))
            elif fuellung == 'S' and name == 'T1':
                C2p = c - 2 * R8[a]
                for i in range(6):
                    zellen.append(tet([c, C2p, zyk[i], zyk[(i + 1) % 6]], art='achse'))
    return pos8, zellen


def zelle_D(X, paare, dritte):
    """d(Diederwinkel)/d(Kantenlaenge) einer starren Zelle: komplexer Schritt und C^+ (wie tp.baue_zelle)."""
    nV, nE = len(X), len(paare)
    C = np.zeros((nE, 3 * nV))
    for e, (i, j) in enumerate(paare):
        n = (X[j] - X[i]) / np.linalg.norm(X[j] - X[i])
        C[e, 3 * j:3 * j + 3] += n
        C[e, 3 * i:3 * i + 3] -= n
    h = 1e-20
    J = np.zeros((nE, 3 * nV))
    th0 = np.zeros(nE)
    for e, (i, j) in enumerate(paare):
        k_, l_ = dritte[e]
        th0[e] = float(np.real(tp.dieder(X.astype(complex), i, j, k_, l_)))
        for v in range(nV):
            for c in range(3):
                Xc = X.astype(complex)
                Xc[v, c] += 1j * h
                J[e, 3 * v + c] = np.imag(tp.dieder(Xc, i, j, k_, l_)) / h
    Cp = C.T @ np.linalg.inv(C @ C.T)
    return J @ Cp, th0


def baue(fuellung):
    pos8, zellen = geometrie(fuellung)
    kanten, kliste = {}, []
    for z in zellen:
        ids = [zerlege(x, pos8) for x in z['X8']]
        z['ids'] = ids
        paare = sorted(set(tuple(sorted((f[i], f[j]))) for f in z['flaechen'] for i in range(3) for j in range(i + 1, 3)))
        dritte = []
        for (i, j) in paare:
            dr = [[x for x in f if x not in (i, j)][0] for f in z['flaechen'] if i in f and j in f]
            assert len(dr) == 2, (z['art'], i, j, dr)
            dritte.append(tuple(dr))
        z['paare'] = paare
        z['kanten'] = []
        for (i, j) in paare:
            (si, ni), (sj, nj) = ids[i], ids[j]
            d = tuple(int(x) for x in np.subtract(nj, ni))
            k1 = (si, sj, d)
            k2 = (sj, si, tuple(-x for x in d))
            key = min(k1, k2)
            if key not in kanten:
                kanten[key] = len(kliste)
                kliste.append(key)
            T = ni if key == k1 else nj
            z['kanten'].append((kanten[key], np.array(T, float) @ AV))
        X = np.array(z['X8'], float) / 8.0
        D, th0 = zelle_D(X, paare, dritte)
        lz = np.array([np.linalg.norm(X[j] - X[i]) for (i, j) in paare])
        z['D'] = D
        z['theta0'] = th0
        z['l'] = lz
        z['Dl'] = lz[:, None] * D * lz[None, :]
        nz = np.array([(X[j] - X[i]) / np.linalg.norm(X[j] - X[i]) for (i, j) in paare])
        z['A0'] = (nz @ nz.T) ** 2 - 0.5
        z['vol'] = abs(np.linalg.det(np.array([X[1] - X[0], X[2] - X[0], X[3] - X[0]]))) / 6.0 if len(X) == 4 else None
    pos = [np.asarray(p, float) / 8.0 for p in pos8]
    E = len(kliste)
    nV = len(pos8)
    lv, nvv, mitte, start, ende = [], [], [], [], []
    for (s, s2, n2) in kliste:
        x0 = pos[s]
        x1 = pos[s2] + np.array(n2, float) @ AV
        d = x1 - x0
        lv.append(np.linalg.norm(d))
        nvv.append(d / np.linalg.norm(d))
        mitte.append(0.5 * (x0 + x1))
        start.append(x0)
        ende.append(x1)
    mod = {'fuellung': fuellung, 'pos': pos, 'zellen': zellen, 'kliste': kliste, 'E': E, 'nV': nV,
           'l': np.array(lv), 'n': np.array(nvv), 'mitte': np.array(mitte), 'nT': len(zellen),
           'T': [np.array(n2, float) @ AV for (s, s2, n2) in kliste]}
    # Laengen der Zellkanten muessen zu den Variablenkanten passen
    for z in zellen:
        for (e, T), lz in zip(z['kanten'], z['l']):
            assert abs(lz - mod['l'][e]) < 1e-12
    # Zahl der Tetraeder (Zellen) je Ecke, fuer die B1-Abbildung Mitten -> Ecken
    nzell = np.zeros(nV)
    for z in zellen:
        for (s, n) in z['ids']:
            nzell[s] += 1
    mod['n_zellen_je_ecke'] = nzell
    return mod


# ------------------------------------------------------------------------------------------------ Operatoren
def ops(mod, k):
    """B, A, M (Eckverschiebung), c (Spalten je Ecke), fuer k (..., 3)."""
    sh = k.shape[:-1]
    E, nV = mod['E'], mod['nV']
    B = np.zeros(sh + (E, E), complex)
    A = np.zeros(sh + (E, E), complex)
    for z in mod['zellen']:
        ph = [np.exp(1j * (k @ T)) for (e, T) in z['kanten']]
        idx = [e for (e, T) in z['kanten']]
        Dl, A0, kin = z['Dl'], z['A0'], z['kin']
        for i in range(len(idx)):
            pci = np.conj(ph[i])
            for j in range(len(idx)):
                f = pci * ph[j]
                B[..., idx[i], idx[j]] += Dl[i, j] * f
                if kin:
                    A[..., idx[i], idx[j]] += A0[i, j] * f
    M = np.zeros(sh + (E, 3 * nV), complex)
    crow = np.zeros(sh + (nV, E), complex)
    for e, (s, s2, n2) in enumerate(mod['kliste']):
        ph = np.exp(1j * (k @ mod['T'][e]))
        nl = mod['n'][e] / mod['l'][e]
        M[..., e, 3 * s2:3 * s2 + 3] += nl * ph[..., None]
        M[..., e, 3 * s:3 * s + 3] -= nl
        crow[..., s, :] -= B[..., e, :]
        crow[..., s2, :] -= np.conj(ph)[..., None] * B[..., e, :]
    c = np.conj(np.swapaxes(crow, -1, -2))                                # (..., E, nV): Spalten c_v, c_v^dagger a = crow_v . a
    return {'B': B, 'A': A, 'M': M, 'c': c}


def M_B1(mod, k):
    """B1: Eichung an den Mitten aller Zellen, jede Ecke = Mittel der Mitten ihrer Zellen. (..., E, 3 nT)."""
    sh = k.shape[:-1]
    nV, nT = mod['nV'], mod['nT']
    Pc = np.zeros(sh + (3 * nV, 3 * nT), complex)
    for t, z in enumerate(mod['zellen']):
        for (s, n) in z['ids']:
            T = np.array(n, float) @ AV
            ph = np.exp(-1j * (k @ T)) / mod['n_zellen_je_ecke'][s]
            for j in range(3):
                Pc[..., 3 * s + j, 3 * t + j] += ph
    return ops(mod, k)['M'] @ Pc


def rang(X, tol=1e-9):
    s = np.linalg.svd(X, compute_uv=False)
    smax = s.max(-1, keepdims=True)
    smax = np.where(smax > 0, smax, 1.0)
    return (s > tol * smax).sum(-1), s


def phys_basis_rr(M, c, tol=1e-9):
    """Rang-ehrliches Komplement von Bild[M, c]; gibt Liste (Indexmenge, S) gruppiert nach Rang."""
    X = np.concatenate([M, c], -1)
    U, s, _ = np.linalg.svd(X)
    smax = s.max(-1, keepdims=True)
    r = (s > tol * smax).sum(-1)
    return U, r, s


def kontrollen_ops(o):
    B, A, M, c = o['B'], o['A'], o['M'], o['c']
    sB = np.abs(B).max()
    return {'B_herm': float(np.abs(B - np.conj(np.swapaxes(B, -1, -2))).max() / sB),
            'A_herm': float(np.abs(A - np.conj(np.swapaxes(A, -1, -2))).max() / max(np.abs(A).max(), 1e-300)),
            'BM_null': float(np.abs(B @ M).max() / (sB * np.abs(M).max())),
            'cM_null': float(np.abs(np.conj(np.swapaxes(c, -1, -2)) @ M).max() / (np.abs(c).max() * np.abs(M).max()))}


def kontrolle_zellen(mod):
    out = {'D_sym_max': 0.0, 'schlaefli_lD_max': 0.0, 'n_zellen': mod['nT'], 'arten': {}}
    for z in mod['zellen']:
        D = z['D']
        out['D_sym_max'] = max(out['D_sym_max'], float(np.abs(D - D.T).max() / np.abs(D).max()))
        out['schlaefli_lD_max'] = max(out['schlaefli_lD_max'], float(np.abs(z['l'] @ D).max() / (np.abs(D).max() * z['l'].max())))
        out['arten'][z['art']] = out['arten'].get(z['art'], 0) + 1
    # Ebenheit: Summe der Diederwinkel je Kante = 2 pi
    summe = np.zeros(mod['E'])
    for z in mod['zellen']:
        for (e, T), th in zip(z['kanten'], z['theta0']):
            summe[e] += th
    out['dieder_summe_minus_2pi_max'] = float(np.abs(summe - 2 * np.pi).max())
    vols = [z['vol'] for z in mod['zellen'] if z['vol'] is not None]
    out['volumen_summe_tetraeder'] = float(sum(vols))
    out['volumina'] = sorted(set(round(v * 768, 9) for v in vols))
    return out


# ------------------------------------------------------------------------------------------------ Spektrum
def tensor_fit(mod, a, k, M):
    """Grobe Metrik der Mode: a = sum_s x_s (n^T B6_s n) e^{i k . m_e} + M xi (Eichanteil frei), kleinste Quadrate.
    Der TT-Anteil ist unter glatter Eichung sym(k x xi) invariant; die Eichspalten nehmen die Relativverschiebungen
    der Untergitter auf, die sonst den Tensor verfaelschen."""
    Es = np.array([[mod['n'][e] @ tp.B6[s] @ mod['n'][e] for s in range(6)] for e in range(mod['E'])])
    ph = np.exp(1j * (mod['mitte'] @ k))
    X = np.concatenate([Es * ph[:, None], M], axis=1)
    x, *_ = np.linalg.lstsq(X, a, rcond=None)
    rest = float(np.linalg.norm(a - X @ x) / max(np.linalg.norm(a), 1e-300))
    H = np.einsum('a,aij->ij', x[:6], tp.B6)
    return H, rest


def richtungen(seed=3):
    rng = np.random.default_rng(seed)
    r = [('100', np.array([1., 0, 0])), ('110', np.array([1., 1, 0]) / np.sqrt(2)), ('111', np.array([1., 1, 1]) / np.sqrt(3))]
    r += [('z%d' % i, x / np.linalg.norm(x)) for i, x in enumerate(rng.normal(size=(20, 3)))]
    return r


def spektrum_punkt(mod, kk, mit_moden=True):
    """Ein k: alle omega^2 auf der Zwangsflaeche, mit TT-Anteil je Mode."""
    o = ops(mod, kk[None, :])
    B, A, M, c = o['B'][0], o['A'][0], o['M'][0], o['c'][0]
    U, r, s = phys_basis_rr(M, c)
    S = U[:, r:]
    Ar = np.conj(S.T) @ A @ S
    Br = np.conj(S.T) @ B @ S
    eA = np.linalg.eigvalsh(Ar)
    eB = np.linalg.eigvalsh(Br)
    ww, vv = np.linalg.eig(Ar @ Br)
    o_ = np.argsort(ww.real)
    ww, vv = ww[o_], vv[:, o_]
    z = {'rang_Mc': int(r), 'dim': int(S.shape[1]), 'w2_re': [float(x) for x in ww.real], 'w2_im': [float(x) for x in ww.imag],
         'skal_tp': float(np.abs(eA).max() * np.abs(eB).max()), 'A_phys_neg': int((eA < -1e-9 * np.abs(eA).max()).sum()),
         'B_phys_neg': int((eB < -1e-9 * np.abs(eB).max()).sum()), 'A_phys_cond': float(np.abs(eA).max() / max(np.abs(eA).min(), 1e-300))}
    if mit_moden:
        tt, rest = [], []
        for j in range(vv.shape[1]):
            a = S @ vv[:, j]
            H, rr = tensor_fit(mod, a, kk, M)
            tt.append(float(tp.tt_anteil(H, kk)[0]))
            rest.append(rr)
        z['tt_anteil'] = tt
        z['fit_rest'] = rest
    # ohne Skalarregel (beschreibend): Komplement nur des Eichbilds
    U2, r2, _ = phys_basis_rr(M, np.zeros((M.shape[0], 0), complex))
    S2 = U2[:, r2:]
    w2 = np.linalg.eigvals((np.conj(S2.T) @ A @ S2) @ (np.conj(S2.T) @ B @ S2))
    w2 = w2[np.argsort(w2.real)]
    z['ohne_skalar_w2_re'] = [float(x) for x in w2.real]
    z['ohne_skalar_w2_im'] = [float(x) for x in w2.imag]
    return z


def spektrum_klein(mod):
    out = []
    for nm, d in richtungen():
        z = {'richtung': nm, 'd': d.tolist()}
        for eps in (1e-3, 2e-3):
            z['eps_%g' % eps] = spektrum_punkt(mod, eps * d)
        out.append(z)
    return out


def spektrum_gitter(mod, L, chunk=256):
    g = np.arange(L)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    kall = (mm / L) @ BV
    res = {'L': L, 'nk': int(len(kall)), 'm_je_k': mm.tolist()}
    pos, neg, kom, nul, dim, rk, aneg, bneg, wmin, acond = [], [], [], [], [], [], [], [], [], []
    frei_w, frei_neg, eich_def = [], [], []
    kontr = {'B_herm': 0.0, 'A_herm': 0.0, 'BM_null': 0.0, 'cM_null': 0.0}
    for i0 in range(0, len(kall), chunk):
        k = kall[i0:i0 + chunk]
        o = ops(mod, k)
        kc = kontrollen_ops(o)
        for kk_ in kontr:
            kontr[kk_] = max(kontr[kk_], kc[kk_])
        B, A, M, c = o['B'], o['A'], o['M'], o['c']
        U, r, s = phys_basis_rr(M, c)
        for j in range(len(k)):
            S = U[j][:, r[j]:]
            Ar = np.conj(S.T) @ A[j] @ S
            Br = np.conj(S.T) @ B[j] @ S
            eA = np.linalg.eigvalsh(Ar)
            eB = np.linalg.eigvalsh(Br)
            w2 = np.linalg.eigvals(Ar @ Br)
            skal = np.abs(eA).max() * np.abs(eB).max()
            skal = skal if skal > 0 else 1.0
            pos.append(int(((w2.real > 1e-9 * skal) & (np.abs(w2.imag) <= 1e-9 * skal)).sum()))
            neg.append(int(((w2.real < -1e-9 * skal) & (np.abs(w2.imag) <= 1e-9 * skal)).sum()))
            kom.append(int((np.abs(w2.imag) > 1e-9 * skal).sum()))
            nul.append(int(((np.abs(w2.real) <= 1e-9 * skal) & (np.abs(w2.imag) <= 1e-9 * skal)).sum()))
            dim.append(int(S.shape[1]))
            rk.append(int(r[j]))
            aneg.append(int((eA < -1e-9 * np.abs(eA).max()).sum()))
            bneg.append(int((eB < -1e-9 * np.abs(eB).max()).sum()))
            wmin.append(float(w2.real.min() / skal))
            acond.append(float(np.abs(eA).max() / max(np.abs(eA).min(), 1e-300)))
            # freie Dynamik ohne Zwang (beschreibend)
            wf = np.linalg.eigvals(A[j] @ B[j])
            sk = np.linalg.norm(A[j], 2) * np.linalg.norm(B[j], 2)
            frei_w.append(float(max((-wf.real / sk).max(), (np.abs(wf.imag) / sk).max())))
            frei_neg.append(bool(((-wf.real / sk).max() > 1e-6) or ((np.abs(wf.imag) / sk).max() > 1e-6)))
            # Spur-Eichdefekt je Ecke: A c_v im Bild von M?
            Q, _ = np.linalg.qr(M[j])
            Ac = A[j] @ c[j]
            restv = Ac - Q @ (np.conj(Q.T) @ Ac)
            eich_def.append(float((np.linalg.norm(restv, axis=0) / np.maximum(np.linalg.norm(Ac, axis=0), 1e-300)).max()))
    def vert(x):
        x = np.asarray(x)
        return {str(int(v)): int((x == v).sum()) for v in np.unique(x)}
    res['positiv_je_k'] = pos
    res['verteilung'] = {'positiv': vert(pos), 'negativ': vert(neg), 'komplex': vert(kom), 'null': vert(nul),
                         'dim': vert(dim), 'rang_Mc': vert(rk), 'A_phys_neg': vert(aneg), 'B_phys_neg': vert(bneg)}
    res['w2_min_rel'] = float(min(wmin))
    res['A_phys_cond_max'] = float(max(acond))
    res['frei'] = {'wachsend_anteil': float(np.mean(frei_neg)), 'rate_rel_max': float(max(frei_w))}
    res['spur_eichdefekt'] = {'max': float(max(eich_def)), 'median': float(np.median(eich_def))}
    res['kontr'] = kontr
    return res


# ------------------------------------------------------------------------------------------------ Modi
def lauf_zaehlung(nzuf=300, Lz=8, seed=7):
    rng = np.random.default_rng(seed)
    out = {}
    for f in ('V', 'S', 'ohne'):
        mod = baue(f)
        z = {'E': mod['E'], 'V': mod['nV'], 'T': mod['nT'], 'zellen': kontrolle_zellen(mod),
             'kanten_laengen_x8': sorted(set(round(float(x) * 8, 9) for x in mod['l'])),
             'zellen_je_ecke': [int(x) for x in mod['n_zellen_je_ecke']]}
        g = np.arange(Lz)
        mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
        kg = (mm / Lz) @ BV
        kz = rng.uniform(0, 1, (nzuf, 3)) @ BV
        for name, k in (('gitter', kg), ('zufall', kz), ('null', np.zeros((1, 3)))):
            o = ops(mod, k)
            rA, _ = rang(o['M'])
            rc, _ = rang(np.concatenate([o['M'], o['c']], -1))
            zz = {'rang_MA': {str(int(x)): int((rA == x).sum()) for x in np.unique(rA)},
                  'rang_M_plus_c': {str(int(x)): int((rc == x).sum()) for x in np.unique(rc)}}
            if f != 'ohne':
                MB = M_B1(mod, k)
                rB, sB = rang(MB)
                rAB, _ = rang(np.concatenate([o['M'], MB], -1))
                zz['rang_MB1'] = {str(int(x)): int((rB == x).sum()) for x in np.unique(rB)}
                zz['rang_MA_MB1'] = {str(int(x)): int((rAB == x).sum()) for x in np.unique(rAB)}
                srel = np.sort(sB, -1)[:, ::-1]
                rr = int(rB.min())
                zz['MB1_kleinster_sv_rel_im_rang'] = float((srel[:, rr - 1] / srel[:, 0]).min()) if rr > 0 else None
            zz['kontr'] = kontrollen_ops(o)
            z[name] = zz
        # flache Richtungen von B bei k = 0
        o0 = ops(mod, np.zeros((1, 3)))
        eb = np.linalg.eigvalsh(o0['B'][0])
        z['B_flach_k0'] = int((np.abs(eb) < 1e-10 * np.abs(eb).max()).sum())
        z['B_k0_neg'] = int((eb < -1e-10 * np.abs(eb).max()).sum())
        z['B_k0_pos'] = int((eb > 1e-10 * np.abs(eb).max()).sum())
        # kleines k: B auf dem eichfreien Raum
        kl = []
        for nm, d in richtungen():
            kk = 1e-4 * d
            o1 = ops(mod, kk[None, :])
            Uq, sq, _ = np.linalg.svd(o1['M'][0])
            ra = int((sq > 1e-9 * sq.max()).sum())
            Sg = Uq[:, ra:]
            ev = np.linalg.eigvalsh(np.conj(Sg.T) @ o1['B'][0] @ Sg)
            ev = ev[np.argsort(np.abs(ev))]
            kl.append({'richtung': nm, 'rang_M': ra, 'drei_kleinste_ueber_k2': [float(x) / 1e-8 for x in ev[:3]],
                       'vierter_ueber_k2': float(ev[3]) / 1e-8 if len(ev) > 3 else None,
                       'zahl_unter_1e-6': int((np.abs(ev) < 1e-6).sum())})
        z['klein_k_B_eichfrei'] = kl
        out[f] = z
    return out


def lauf_kontrolle(ref_pfad):
    mod = baue('ohne')
    out = {'zellen': kontrolle_zellen(mod), 'E': mod['E'], 'V': mod['nV']}
    t = time.time()
    sp = spektrum_gitter(mod, 16)
    out['gitter'] = {k: v for k, v in sp.items() if k not in ('m_je_k', 'positiv_je_k')}
    kl = spektrum_klein(mod)
    out['t_spektrum_s'] = time.time() - t
    with open(ref_pfad) as f:
        ref = json.load(f)['spektren']
    p1, p2 = ref['pyro1'], ref['pyro2']
    assert p1['phys']['m_je_k'] == sp['m_je_k'] and p2['phys']['m_je_k'] == sp['m_je_k']
    alt = np.array(p1['phys']['positiv_je_k']) + np.array(p2['phys']['positiv_je_k'])
    neu = np.array(sp['positiv_je_k'])
    out['modenzahl_gleich_alle'] = bool(np.all(alt == neu))
    out['modenzahl_abweichungen'] = int((alt != neu).sum())
    out['modenzahl_alt_verteilung'] = {str(int(x)): int((alt == x).sum()) for x in np.unique(alt)}
    out['modenzahl_neu_verteilung'] = {str(int(x)): int((neu == x).sum()) for x in np.unique(neu)}
    dmax = 0.0
    zeilen = []
    for z_alt1, z_alt2, z_neu in zip(p1['klein_k'], p2['klein_k'], kl):
        assert z_alt1['richtung'] == z_neu['richtung'] == z_alt2['richtung']
        for eps in (1e-3, 2e-3):
            key = 'eps_%g' % eps
            a = np.sort(np.array(z_alt1[key]['w2_ueber_k2'] + z_alt2[key]['w2_ueber_k2']))
            n = np.sort(np.array(z_neu[key]['w2_re']) / eps ** 2)
            d = float(np.abs(a - n).max()) if len(a) == len(n) else float('inf')
            dmax = max(dmax, d)
            zeilen.append({'richtung': z_neu['richtung'], 'eps': eps, 'alt': a.tolist(), 'neu': n.tolist(), 'abw': d,
                           'tt_neu': z_neu[key]['tt_anteil']})
    out['tempo_abw_max'] = dmax
    out['tempo_zeilen'] = zeilen
    # Gegenprobe der Operatoren gegen tp.ops_pyro (zwei Kopien) an 20 Zufalls-k
    rng = np.random.default_rng(11)
    kz = rng.uniform(0, 1, (20, 3)) @ BV
    o = ops(mod, kz)
    oa, ob = tp.ops_pyro(kz, kopie=1), tp.ops_pyro(kz, kopie=2)
    gp = {'B_spektrum': 0.0, 'A_spektrum': 0.0, 'w2_phys': 0.0, 'rang_M_neu': [], 'w2_skala': 0.0}
    for j in range(len(kz)):
        eBn = np.sort(np.linalg.eigvalsh(o['B'][j]))
        eBa = np.sort(np.concatenate([np.linalg.eigvalsh(oa['B'][j]), np.linalg.eigvalsh(ob['B'][j])]))
        gp['B_spektrum'] = max(gp['B_spektrum'], float(np.abs(eBn - eBa).max() / np.abs(eBa).max()))
        eAn = np.sort(np.linalg.eigvalsh(o['A'][j]))
        eAa = np.sort(np.concatenate([np.linalg.eigvalsh(oa['A'][j]), np.linalg.eigvalsh(ob['A'][j])]))
        gp['A_spektrum'] = max(gp['A_spektrum'], float(np.abs(eAn - eAa).max() / np.abs(eAa).max()))
        U, r, s = phys_basis_rr(o['M'][j], o['c'][j])
        S = U[:, r:]
        wn = np.sort(np.linalg.eigvals((np.conj(S.T) @ o['A'][j] @ S) @ (np.conj(S.T) @ o['B'][j] @ S)).real)
        wa = []
        for oo in (oa, ob):
            Sa, _ = tp.phys_basis(oo['M'][j], oo['c'][j])
            wa += list(np.linalg.eigvals((np.conj(Sa.T) @ oo['A'][j] @ Sa) @ (np.conj(Sa.T) @ oo['B'][j] @ Sa)).real)
        wa = np.sort(np.array(wa))
        gp['w2_phys'] = max(gp['w2_phys'], float(np.abs(wn - wa).max() / np.abs(wa).max()))
        gp['w2_skala'] = max(gp['w2_skala'], float(np.abs(wa).max()))
        gp['rang_M_neu'].append(int(r))
    gp['rang_M_neu'] = sorted(set(gp['rang_M_neu']))
    out['gegenprobe_tp'] = gp
    return out


def lauf_spektrum(fuellung, L):
    mod = baue(fuellung)
    out = {'fuellung': fuellung, 'E': mod['E'], 'V': mod['nV'], 'T': mod['nT'], 'zellen': kontrolle_zellen(mod)}
    t = time.time()
    out['klein_k'] = spektrum_klein(mod)
    out['t_klein_s'] = time.time() - t
    t = time.time()
    if L > 0:
        out['gitter'] = spektrum_gitter(mod, L)
    out['t_gitter_s'] = time.time() - t
    return out


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['zaehlung', 'kontrolle', 'spektrum'])
    ap.add_argument('--fuellung', default='V', choices=['V', 'S', 'ohne'])
    ap.add_argument('--L', type=int, default=16)
    ap.add_argument('--nzuf', type=int, default=300)
    ap.add_argument('--Lz', type=int, default=8)
    ap.add_argument('--ref')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'tp_sha256': sha(os.path.abspath(tp.__file__))}
    if a.ref:
        info['ref_sha256'] = sha(a.ref)
    res = {'info': info}
    if a.modus == 'zaehlung':
        res['zaehlung'] = lauf_zaehlung(nzuf=a.nzuf, Lz=a.Lz)
    elif a.modus == 'kontrolle':
        res['kontrolle'] = lauf_kontrolle(a.ref)
    else:
        res['spektrum'] = lauf_spektrum(a.fuellung, a.L)
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, a.fuellung, 'laufzeit %.1f s' % res['laufzeit_s'], 'maxrss %.0f MB' % res['maxrss_MB'], flush=True)


if __name__ == '__main__':
    main()
