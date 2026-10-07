#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZWEI-KOPIEN-1, Runde 43 (fmhc-physics), Code-Agent fuer die Leitung claude-primary.

B1-Netz aus TENSOR-EIS-PYRO-1 (zwei Kopien, 12 Kanten je primitiver Zelle) mit Eckkopplung kappa * K.
  K2  : phi_v = mittlere Dehnung der 6 Kanten des Auf-Tetraeders minus die der 6 Kanten des Ab-Tetraeders an der Ecke v;
        K = sum_v phi_v^2
  K2e : wie K2, Mittel nur ueber die 3 Kanten je Tetraeder an v (Variante, beschreibend)
  K4  : psi_v^(c) = (LBAR/3) * Summe der Fehlwinkel-Aenderungen der 3 Kanten der Kopie c an v; K = sum_v psi^(1) psi^(2)
Lesarten: P = Komplement von [M, c] (wie TENSOR-EIS-PYRO-1), R = Komplement von [M N, c] mit N = Kern(K M).
Bloch-Phasen an den wirklichen Orten (Kopie 1: Staebe zwischen Ab-Mitten, Kopie 2: zwischen Auf-Mitten); die
kopieninternen Operatoren von tp.ops_pyro sind translationsinvariant und gelten unveraendert.
tp.py (TENSOR-EIS-PYRO-1, sha256 419d7da6...) wird unveraendert importiert.
"""
import argparse, json, sys, time, platform, os, resource, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402

R8 = tp.R8
PAARE = tp.PAARE
LBAR = tp.LBAR
BM8 = np.rint(tp.BM * 8).astype(int)
KAPPA_HAUPT = (0.01, 0.1, 1.0)
KAPPA_LEITER = (1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0)
EPS = (1e-3, 2e-3)


def schl(les, kap, eps=None):
    return '%s|%g' % (les, kap) if eps is None else '%s|%g|%g' % (les, kap, eps)


def bar_typ(v8):
    for m in range(6):
        if np.array_equal(v8, BM8[m]):
            return m, 1
        if np.array_equal(v8, -BM8[m]):
            return m, -1
    raise ValueError(v8)


def auf_kanten(ecke=None):
    """Kopie-1-Staebe der Kanten des Auf-Tetraeders R = 0: (m, Start*8). Kante (p, q) -> Stab 2 r_p -> 2 r_q."""
    out = []
    for (p, q) in PAARE:
        if ecke is not None and ecke not in (p, q):
            continue
        m, s = bar_typ(2 * (R8[q] - R8[p]))
        out.append((m, 2 * R8[p] if s > 0 else 2 * R8[q]))
    return out


def ab_kanten(D8, ecke=None):
    """Kopie-2-Staebe der Kanten des Ab-Tetraeders mit Mitte D8/8: Kante (p, q) -> Stab D - 2 r_p -> D - 2 r_q."""
    out = []
    for (p, q) in PAARE:
        if ecke is not None and ecke not in (p, q):
            continue
        m, s = bar_typ(2 * (R8[p] - R8[q]))
        out.append((m, D8 - 2 * R8[p] if s > 0 else D8 - 2 * R8[q]))
    return out


def ph8(k, x8):
    return np.exp(1j * (k @ (np.asarray(x8, float) / 8.0)))


def koppel_zeilen(k, fassung, B1, B2):
    """Eckfunktionale je Ecke a der Auf-Zelle R = 0 (Phase e^{i k.R} herausgezogen), (..., 4, 12).
    K2/K2e: (F, None); K4: (F1, F2) mit F1 nur auf Kopie 1, F2 nur auf Kopie 2."""
    sh = k.shape[:-1]
    if fassung in ('K2', 'K2e'):
        F = np.zeros(sh + (4, 12), complex)
        for a in range(4):
            D8 = 2 * R8[a]
            ecke = None if fassung == 'K2' else a
            w = 1.0 / 6.0 if fassung == 'K2' else 1.0 / 3.0
            for (m, x8) in auf_kanten(ecke):
                F[..., a, m] += w * ph8(k, x8)
            for (m, x8) in ab_kanten(D8, ecke):
                F[..., a, 6 + m] -= w * ph8(k, x8)
        return F, None
    F1 = np.zeros(sh + (4, 12), complex)
    F2 = np.zeros(sh + (4, 12), complex)
    for a in range(4):
        D8 = 2 * R8[a]
        for (m, x8) in auf_kanten(a):
            F1[..., a, 0:6] += -(1.0 / 3.0) * ph8(k, x8)[..., None] * B1[..., m, :]
        for (m, x8) in ab_kanten(D8, a):
            F2[..., a, 6:12] += -(1.0 / 3.0) * ph8(k, x8)[..., None] * B2[..., m, :]
    return F1, F2


def K_matrix(F, F2=None):
    if F2 is None:
        return np.einsum('...ai,...aj->...ij', np.conj(F), F)
    X = np.einsum('...ai,...aj->...ij', np.conj(F), F2)
    return 0.5 * (X + np.conj(np.swapaxes(X, -1, -2)))


def ops12(k, fassung):
    o1 = tp.ops_pyro(k, kopie=1)
    o2 = tp.ops_pyro(k, kopie=2)
    sh = k.shape[:-1]
    B = np.zeros(sh + (12, 12), complex)
    A = np.zeros(sh + (12, 12), complex)
    M = np.zeros(sh + (12, 6), complex)
    c = np.zeros(sh + (12, 2), complex)
    B[..., :6, :6] = o1['B']
    B[..., 6:, 6:] = o2['B']
    A[..., :6, :6] = o1['A']
    A[..., 6:, 6:] = o2['A']
    M[..., :6, :3] = o1['M']
    M[..., 6:, 3:] = o2['M']
    c[..., :6, 0] = o1['c']
    c[..., 6:, 1] = o2['c']
    F1, F2 = koppel_zeilen(k, fassung, o1['B'], o2['B'])
    K = K_matrix(F1, F2)
    return {'B': B, 'A': A, 'M': M, 'c': c, 'K': K, 'F1': F1, 'F2': F2}


def phys_raum(M, c, K, lesart, tol=1e-8):
    """Orthonormalbasis des physikalischen Raums (12 x d) an einem k; Zahl gebrochener Eichrichtungen."""
    nb = 0
    Mr = M
    if lesart == 'R':
        U, sv, Vh = np.linalg.svd(K @ M)
        skal = max(np.linalg.norm(K, 2) * np.linalg.norm(M, 2), 1e-300)
        nb = int((sv > tol * skal).sum())
        Mr = M @ np.conj(Vh[nb:].T)
    X = np.concatenate([Mr, c], axis=1)
    U, sv, _ = np.linalg.svd(X)
    r = int((sv > 1e-9 * sv.max()).sum())
    return U[:, r:], nb, r


def tt_beide(a, kk):
    H1 = tp.tensor_aus('pyro1', a[:6], kk)
    H2 = tp.tensor_aus('pyro2', a[6:], kk)
    _, ntt1, nt1 = tp.tt_anteil(H1, kk)
    _, ntt2, nt2 = tp.tt_anteil(H2, kk)
    ntt, nt = ntt1 + ntt2, nt1 + nt2
    return float(ntt / max(ntt + nt, 1e-300))


def spektrum_k(o, j, kap, les, kk=None):
    """Alle omega^2 auf dem physikalischen Raum an k-Index j; mit kk (3,) auch TT-Anteil und Kopienanteil je Mode."""
    B = o['B'][j] + kap * o['K'][j]
    A = o['A'][j]
    S, nb, r = phys_raum(o['M'][j], o['c'][j], o['K'][j], les)
    Ar = np.conj(S.T) @ A @ S
    Br = np.conj(S.T) @ B @ S
    Ar = 0.5 * (Ar + np.conj(Ar.T))
    Br = 0.5 * (Br + np.conj(Br.T))
    eA = np.linalg.eigvalsh(Ar)
    eB = np.linalg.eigvalsh(Br)
    w2, V = np.linalg.eig(Ar @ Br)
    o_ = np.argsort(w2.real)
    w2, V = w2[o_], V[:, o_]
    z = {'w2_re': [float(x) for x in w2.real], 'w2_im': [float(x) for x in w2.imag], 'dim': int(S.shape[1]),
         'n_gebrochen': nb, 'rang_Mc': r, 'eA_min': float(eA.min()), 'eA_max': float(eA.max()),
         'eB_min': float(eB.min()), 'eB_max': float(eB.max())}
    if kk is not None:
        tt, w1 = [], []
        for jj in range(V.shape[1]):
            a = S @ V[:, jj]
            tt.append(tt_beide(a, kk))
            w1.append(float(np.linalg.norm(a[:6]) ** 2 / max(np.linalg.norm(a) ** 2, 1e-300)))
        z['tt'] = tt
        z['w1'] = w1
    return z


def richtungen26():
    out = []
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for l in (-1, 0, 1):
                if (i, j, l) != (0, 0, 0):
                    d = np.array([i, j, l], float)
                    out.append(('%d,%d,%d' % (i, j, l), d / np.linalg.norm(d)))
    return out


def richtungen23(seed=3):
    """Dieselben 23 Richtungen wie tp.spektrum_modell (TENSOR-EIS-PYRO-1)."""
    rng = np.random.default_rng(seed)
    r = [('100', np.array([1., 0, 0])), ('110', np.array([1., 1, 0]) / np.sqrt(2)), ('111', np.array([1., 1, 1]) / np.sqrt(3))]
    r += [('z%d' % i, x / np.linalg.norm(x)) for i, x in enumerate(rng.normal(size=(20, 3)))]
    return r


def klein_punkte(fassung, richt, konfig):
    out = []
    for nm, d in richt:
        z = {'richtung': nm, 'd': d.tolist()}
        for eps in EPS:
            kk = eps * d
            o = ops12(kk[None, :], fassung)
            for (kap, les) in konfig:
                z[schl(les, kap, eps)] = spektrum_k(o, 0, kap, les, kk=kk)
        out.append(z)
    return out


def gitter(fassung, L, konfig, mit_m=False):
    g = np.arange(L)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    k = (mm / L) @ tp.BV
    o = ops12(k, fassung)
    res = {'L': L, 'nk': int(len(k))}
    if mit_m:
        res['m_je_k'] = mm.tolist()
    for (kap, les) in konfig:
        pos, neg, kom, nul, aneg, bneg, wmin, dims, nbs = [], [], [], [], [], [], [], [], []
        for j in range(len(k)):
            z = spektrum_k(o, j, kap, les)
            re, im = np.array(z['w2_re']), np.array(z['w2_im'])
            s = max(float(np.sqrt(re ** 2 + im ** 2).max()), 1e-300)
            pos.append(int(((re > 1e-9 * s) & (np.abs(im) <= 1e-9 * s)).sum()))
            neg.append(int(((re < -1e-9 * s) & (np.abs(im) <= 1e-9 * s)).sum()))
            kom.append(int((np.abs(im) > 1e-9 * s).sum()))
            nul.append(int(((np.abs(re) <= 1e-9 * s) & (np.abs(im) <= 1e-9 * s)).sum()))
            sa = max(abs(z['eA_min']), abs(z['eA_max']), 1e-300)
            sb = max(abs(z['eB_min']), abs(z['eB_max']), 1e-300)
            aneg.append(int(z['eA_min'] < -1e-9 * sa))
            bneg.append(int(z['eB_min'] < -1e-9 * sb))
            wmin.append(float(re.min() / s))
            dims.append(z['dim'])
            nbs.append(z['n_gebrochen'])

        def vert(x):
            x = np.asarray(x)
            return {str(int(v)): int((x == v).sum()) for v in np.unique(x)}
        e = {'positiv_verteilung': vert(pos), 'negativ_k': int((np.array(neg) > 0).sum()),
             'komplex_k': int((np.array(kom) > 0).sum()), 'null_verteilung': vert(nul),
             'A_neg_k': int(sum(aneg)), 'B_neg_k': int(sum(bneg)), 'w2_min_rel': float(min(wmin)),
             'dim_verteilung': vert(dims), 'gebrochen_verteilung': vert(nbs)}
        if mit_m:
            e['positiv_je_k'] = pos
        res[schl(les, kap)] = e
    return res


def pfad(fassung, n, konfig):
    ziele = {'X': np.array([0., 0., 2 * np.pi]), 'K': 1.5 * np.pi * np.array([1., 1., 0.]),
             'L': np.pi * np.array([1., 1., 1.])}
    t = np.arange(1, n + 1) / n
    out = {'t': t.tolist()}
    for nm, kz in ziele.items():
        k = t[:, None] * kz[None, :]
        o = ops12(k, fassung)
        zz = {}
        for (kap, les) in konfig:
            zz[schl(les, kap)] = [spektrum_k(o, j, kap, les)['w2_re'] for j in range(len(k))]
        out[nm] = zz
    return out


def kontrolle(fassung, seed=17):
    rng = np.random.default_rng(seed)
    kz = rng.uniform(0, 1, (50, 3)) @ tp.BV
    o = ops12(kz, fassung)
    B, K, M, c = o['B'], o['K'], o['M'], o['c']
    sB = np.abs(B).max()
    sK = max(np.abs(K).max(), 1e-300)
    eK = np.linalg.eigvalsh(K)
    out = {'B_herm': float(np.abs(B - np.conj(np.swapaxes(B, -1, -2))).max() / sB),
           'K_herm': float(np.abs(K - np.conj(np.swapaxes(K, -1, -2))).max() / sK),
           'BM_null': float(np.abs(B @ M).max() / (sB * np.abs(M).max())),
           'cM_null': float(np.abs(np.conj(np.swapaxes(c, -1, -2)) @ M).max() / (np.abs(c).max() * np.abs(M).max())),
           'KM_rel': float(np.abs(K @ M).max() / (sK * np.abs(M).max())),
           'K_eig_min_rel': float((eK.min(-1) / np.abs(eK).max(-1)).min()),
           'K_eig_max_rel_neg': float((eK.max(-1) / np.abs(eK).max(-1)).min())}
    rk = []
    for j in range(len(kz)):
        sv = np.linalg.svd(K[j] @ M[j], compute_uv=False)
        skal = max(np.linalg.norm(K[j], 2) * np.linalg.norm(M[j], 2), 1e-300)
        rk.append(int((sv > 1e-8 * skal).sum()))
    out['rang_KM_verteilung'] = {str(int(v)): int((np.array(rk) == v).sum()) for v in np.unique(rk)}
    if fassung in ('K2', 'K2e'):
        # Schreibtischformeln: (1) k = 0, gleichfoermige Dehnung; (2) K2: F M gegen (8/3)(u, e^{2ik.r_a} conj(u))
        h1 = rng.normal(size=(3, 3)); h1 = h1 + h1.T
        h2 = rng.normal(size=(3, 3)); h2 = h2 + h2.T
        a1 = np.array([tp.NM[m] @ h1 @ tp.NM[m] for m in range(6)])
        a2 = np.array([tp.NM[m] @ h2 @ tp.NM[m] for m in range(6)])
        F0, _ = koppel_zeilen(np.zeros((1, 3)), fassung, None, None)
        phi = F0[0] @ np.concatenate([a1, a2])
        if fassung == 'K2':
            soll = np.full(4, (np.trace(h1) - np.trace(h2)) / 3.0)
        else:
            soll = np.array([((np.trace(h1) + R8[a] @ h1 @ R8[a]) - (np.trace(h2) + R8[a] @ h2 @ R8[a])) / 6.0 for a in range(4)])
        out['schreibtisch_k0_max_abw'] = float(np.abs(phi - soll).max())
        if fassung == 'K2':
            F = o['F1']
            FM = F @ M
            r = R8.astype(float) / 8.0
            dmax = 0.0
            for j in range(len(kz)):
                u = (r * np.exp(2j * (r @ kz[j]))[:, None]).sum(0)
                for a in range(4):
                    soll_a = (8.0 / 3.0) * np.concatenate([u, np.exp(2j * (kz[j] @ r[a])) * np.conj(u)])
                    dmax = max(dmax, float(np.abs(FM[j, a] - soll_a).max()))
            out['schreibtisch_FM_max_abw'] = dmax
    return out


def vergleich_ref(fassung, ref_pfad, k23, gitter16):
    with open(ref_pfad) as f:
        ref = json.load(f)['spektren']
    p1, p2 = ref['pyro1'], ref['pyro2']
    out = {}
    assert p1['phys']['m_je_k'] == gitter16['m_je_k'] == p2['phys']['m_je_k']
    alt = np.array(p1['phys']['positiv_je_k']) + np.array(p2['phys']['positiv_je_k'])
    neu = np.array(gitter16[schl('P', 0.0)]['positiv_je_k'])
    out['gitter_positiv_gleich_alle'] = bool(np.all(alt == neu))
    out['gitter_abweichungen'] = int((alt != neu).sum())
    out['gitter_alt_verteilung'] = {str(int(x)): int((alt == x).sum()) for x in np.unique(alt)}
    out['gitter_neu_verteilung'] = {str(int(x)): int((neu == x).sum()) for x in np.unique(neu)}
    zeilen, dw, dv = [], 0.0, 0.0
    for z1, z2, zn in zip(p1['klein_k'], p2['klein_k'], k23):
        assert z1['richtung'] == z2['richtung'] == zn['richtung']
        for eps in EPS:
            a = np.sort(np.array(z1['eps_%g' % eps]['w2_ueber_k2'] + z2['eps_%g' % eps]['w2_ueber_k2']))
            n = np.sort(np.array(zn[schl('P', 0.0, eps)]['w2_re']) / eps ** 2)
            if len(a) == len(n):
                d1 = float(np.abs(a - n).max())
                d2 = float(np.abs(np.sqrt(np.abs(a)) - np.sqrt(np.abs(n))).max())
            else:
                d1 = d2 = float('inf')
            dw, dv = max(dw, d1), max(dv, d2)
            zeilen.append({'richtung': zn['richtung'], 'eps': eps, 'alt': a.tolist(), 'neu': n.tolist(), 'abw_w2k2': d1, 'abw_v': d2})
    out['max_abw_w2_ueber_k2'] = dw
    out['max_abw_v'] = dv
    out['zeilen'] = zeilen
    return out


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf'])
    ap.add_argument('--fassung', required=True, choices=['K2', 'K2e', 'K4'])
    ap.add_argument('--L', type=int, default=16)
    ap.add_argument('--Lleiter', type=int, default=8)
    ap.add_argument('--npfad', type=int, default=40)
    ap.add_argument('--ref')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'tp_sha256': sha(os.path.abspath(tp.__file__))}
    if a.ref:
        info['ref_sha256'] = sha(a.ref)
    res = {'info': info, 'fassung': a.fassung}
    haupt = [(0.0, 'P')] + [(kp, les) for kp in KAPPA_HAUPT for les in ('P', 'R')]
    leiter = [(kp, les) for kp in KAPPA_LEITER for les in ('P', 'R')]
    alle = list(dict.fromkeys(haupt + leiter))
    t = time.time(); res['kontrolle'] = kontrolle(a.fassung); print('kontrolle %.1f s' % (time.time() - t), flush=True)
    t = time.time(); res['klein26'] = klein_punkte(a.fassung, richtungen26(), alle); print('klein26 %.1f s' % (time.time() - t), flush=True)
    t = time.time(); res['klein23'] = klein_punkte(a.fassung, richtungen23(), [(0.0, 'P')]); print('klein23 %.1f s' % (time.time() - t), flush=True)
    t = time.time(); res['gitter'] = gitter(a.fassung, a.L, haupt, mit_m=(a.L == 16)); print('gitter %.1f s' % (time.time() - t), flush=True)
    t = time.time(); res['leiter_gitter'] = gitter(a.fassung, a.Lleiter, leiter); print('leiter %.1f s' % (time.time() - t), flush=True)
    t = time.time(); res['pfad'] = pfad(a.fassung, a.npfad, [(0.0, 'P'), (0.1, 'P'), (1.0, 'P'), (0.1, 'R'), (1.0, 'R')]); print('pfad %.1f s' % (time.time() - t), flush=True)
    if a.ref and a.L == 16:
        res['zk0_ref'] = vergleich_ref(a.fassung, a.ref, res['klein23'], res['gitter'])
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=0, default=lambda x: x.item() if hasattr(x, 'item') else str(x))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.fassung, 'laufzeit %.1f s' % res['laufzeit_s'], 'maxrss %.0f MB' % res['maxrss_MB'], flush=True)


if __name__ == '__main__':
    main()
