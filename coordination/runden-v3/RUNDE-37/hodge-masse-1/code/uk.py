#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-1 (Runde 46, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Finn (05.10.2026): "Meine Tetraeder koennen zufaellig und unregelmaessig sein. Zellen umklappen - wie und mit welchem
Mechanismus? Try it."  Elementarzug: Pachner-Zug 2-3 auf festen Ecken (PLAN.md Abschnitt 2).

Modi:
  kontrolle : UK0. Regge-Wirkung S = sum_e l_e (2 pi - sum_t theta_te) auf dem flachen Zufallsnetz vor und nach
              zufaelligen 2-3-Zuegen (Anteile F_LISTE), Netzproben, affine TT-Steifigkeit (tg.affin, beschreibend).
  mb        : M-B. Zufaellige Eckverschiebungen (Effektivwert a mal mittlere Kantenlaenge), Delaunay neu, Vergleich der
              Tetraedermengen, Cluster (2-3, 3-2, sonst), verletzte Flaechen bei alter Verbindung, Randabstaende mu0;
              Zusatz W: affine TT-Dehnung a h (nur verletzte Flaechen).
  tt        : TT-Spektrum mit tg.modell und tg.spektrum (unveraendert) nach round(f F0) zufaelligen 2-3-Zuegen.
tg.py (TT-GLAS-1, sha256 ec48a258...), ew.py und tp.py werden unveraendert importiert.
"""
import argparse, json, sys, os, time, hashlib, platform, resource
from collections import Counter
import numpy as np
import scipy
from scipy.spatial import Delaunay

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402  (TT-GLAS-1, unveraendert)

SAAT_ZUG = 4538               # Saatbasis der Zugfolgen: rng([SAAT_ZUG, N, saat]) -> Folgen sind geschachtelt
SAAT_MB = 4539                # Saatbasis der Verschiebungen
VMIN_REL = 1e-3               # neue Tetraeder: Volumen >= VMIN_REL x mittleres Tetraedervolumen des Ausgangsnetzes
A_LISTE = [1e-4, 1e-3, 1e-2, 3e-2, 1e-1]
F_LISTE = [0.05, 0.2]
X_CDF = [1e-4, 1e-3, 1e-2, 3e-2, 1e-1]
FL = np.array([[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]])      # Flaeche gegenueber Ecke i
IA = np.array([p[0] for p in tg.PAARE])
IB = np.array([p[1] for p in tg.PAARE])


# ------------------------------------------------------------------------------------------------ Grundbausteine
def absolut(LV, pos, G, O):
    return pos[G] + np.einsum('...i,ij->...j', O.astype(float), LV)


def vol6(p0, p1, p2, p3):
    """6 x orientiertes Volumen, vektorisiert ueber die erste Achse."""
    return np.einsum('...i,...i->...', np.cross(p1 - p0, p2 - p0), p3 - p0)


def tet_vol(LV, pos, G, O):
    X = absolut(LV, pos, G, O)
    return np.abs(vol6(X[:, 0], X[:, 1], X[:, 2], X[:, 3])) / 6.0


def kanten_schluessel(va, oa, vb, ob, nV):
    """Kanonischer Kantenschluessel wie in tg.modell (Anfangsecke, Endecke, Kastenversatz)."""
    d = ob - oa
    erst = np.argmax(d != 0, axis=-1)
    erst_wert = np.take_along_axis(d, erst[..., None], axis=-1)[..., 0]
    use1 = (va < vb) | ((va == vb) & (erst_wert < 0))
    s = np.where(use1, va, vb)
    s2 = np.where(use1, vb, va)
    dd = np.where(use1[..., None], d, -d)
    assert np.abs(dd).max() <= 7
    return (((s.astype(np.int64) * nV + s2) * 16 + dd[..., 0] + 8) * 16 + dd[..., 1] + 8) * 16 + dd[..., 2] + 8


def kanten(LV, pos, G, O, nV):
    k = kanten_schluessel(G[:, IA], O[:, IA], G[:, IB], O[:, IB], nV)
    uniq, first, inv = np.unique(k.ravel(), return_index=True, return_inverse=True)
    X = absolut(LV, pos, G, O)
    lt = np.linalg.norm(X[:, IB] - X[:, IA], axis=2).ravel()
    return uniq, np.asarray(inv).reshape(k.shape), lt[first], lt


def flaechen(G, O):
    """Alle Flaechen: je kanonischem Schluessel genau zwei (Tetraeder, Gegenecke); sh bringt t2 in den Rahmen von t1."""
    gv = G[:, FL].reshape(-1, 3)
    go = O[:, FL].reshape(-1, 3, 3)
    srt = np.sort(gv, axis=1)
    assert np.all(srt[:, 1:] != srt[:, :-1]), 'Ecke doppelt in einer Flaeche'
    order = np.argsort(gv, axis=1)
    gvs = np.take_along_axis(gv, order, 1)
    gos = np.take_along_axis(go, order[:, :, None], 1)
    s0 = gos[:, 0, :]
    rel = gos - s0[:, None, :]
    key = np.concatenate([gvs, rel.reshape(-1, 9)], axis=1)
    _, inv, cnt = np.unique(key, axis=0, return_inverse=True, return_counts=True)
    assert np.all(cnt == 2), 'Flaeche nicht genau zweimal'
    inv = np.asarray(inv).reshape(-1)
    o = np.argsort(inv, kind='stable')
    a, b = o[0::2], o[1::2]
    assert np.all(inv[a] == inv[b])
    return {'t1': a // 4, 'i1': a % 4, 't2': b // 4, 'i2': b % 4, 'sh': s0[a] - s0[b], 'F': int(len(a))}


# ------------------------------------------------------------------------------------------------ 2-3-Zug
def kandidaten(LV, pos, G, O, nV, vmin):
    """Fuer jede Flaeche: konvexe Doppelpyramide (alle drei neuen Volumina gleiches Vorzeichen), Volumen >= vmin,
    neue Kante d-e verbindet zwei verschiedene Ecken und existiert noch nicht."""
    fl = flaechen(G, O)
    t1, i1, t2, i2, sh = fl['t1'], fl['i1'], fl['t2'], fl['i2'], fl['sh']
    fv = G[t1[:, None], FL[i1]]
    fo = O[t1[:, None], FL[i1]]
    dv, do = G[t1, i1], O[t1, i1]
    ev, eo = G[t2, i2], O[t2, i2] + sh

    def P(v, o):
        return pos[v] + o.astype(float) @ LV
    A_, B_, C_ = P(fv[:, 0], fo[:, 0]), P(fv[:, 1], fo[:, 1]), P(fv[:, 2], fo[:, 2])
    D_, E_ = P(dv, do), P(ev, eo)
    v1, v2, v3 = vol6(A_, B_, D_, E_) / 6.0, vol6(B_, C_, D_, E_) / 6.0, vol6(C_, A_, D_, E_) / 6.0
    konvex = ((v1 > 0) & (v2 > 0) & (v3 > 0)) | ((v1 < 0) & (v2 < 0) & (v3 < 0))
    vmn = np.minimum(np.minimum(np.abs(v1), np.abs(v2)), np.abs(v3))
    volok = konvex & (vmn >= vmin)
    eigen = dv != ev
    km = kanten(LV, pos, G, O, nV)[0]
    neu = ~np.isin(kanten_schluessel(dv, do, ev, eo, nV), km)
    ok = volok & eigen & neu
    return {'fl': fl, 'konvex': konvex, 'volok': volok, 'neu': neu, 'eigen': eigen, 'ok': ok}


def zug23(LV, pos, G, O, fl, j):
    """2-3-Zug an Flaeche j: (abcd, abce) -> (abde, bcde, cade); neue Tetraeder mit Schwerpunkt im Grundwuerfel."""
    t1, i1, t2, i2, sh = fl['t1'][j], fl['i1'][j], fl['t2'][j], fl['i2'][j], fl['sh'][j]
    a, b, c = [(G[t1, q], O[t1, q]) for q in FL[i1]]
    d = (G[t1, i1], O[t1, i1])
    e = (G[t2, i2], O[t2, i2] + sh)
    neu = [(a, b, d, e), (b, c, d, e), (c, a, d, e)]
    Gn = np.array([[x[0] for x in tt] for tt in neu], np.int64)
    On = np.array([[x[1] for x in tt] for tt in neu], np.int64)
    cen = absolut(LV, pos, Gn, On).mean(1)
    On = On - np.floor(cen @ np.linalg.inv(LV)).astype(np.int64)[:, None, :]
    keep = np.ones(len(G), bool)
    keep[[t1, t2]] = False
    return np.concatenate([G[keep], Gn]), np.concatenate([O[keep], On])


def zugfolge(LV, pos, G, O, nV, f_liste, rng):
    """Zufaellige 2-3-Zuege: je Schritt gleichverteilt unter allen derzeit erlaubten Flaechen. Zustaende nach
    round(f F0) Zuegen fuer jedes f in f_liste (aufsteigend; die Folge ist fuer alle f dieselbe)."""
    T0 = len(G)
    F0 = 2 * T0
    vbar = float(tet_vol(LV, pos, G, O).mean())
    vmin = VMIN_REL * vbar
    k = kandidaten(LV, pos, G, O, nV, vmin)
    st = {'T0': T0, 'F0': F0, 'vbar': vbar, 'vmin': vmin,
          'start': {'konvex': float(k['konvex'].mean()), 'volok': float(k['volok'].mean()), 'neu_und_konvex':
                    float((k['konvex'] & k['neu']).mean()), 'zug_ok': float(k['ok'].mean())}}
    zust = []
    n = 0
    t0 = time.time()
    for f in f_liste:
        ziel = int(round(f * F0))
        while n < ziel:
            idx = np.nonzero(k['ok'])[0]
            if len(idx) == 0:
                break
            j = idx[rng.integers(len(idx))]
            G, O = zug23(LV, pos, G, O, k['fl'], j)
            n += 1
            k = kandidaten(LV, pos, G, O, nV, vmin)
        zust.append((f, G.copy(), O.copy(), {'f': f, 'n_ziel': ziel, 'n_zuege': n, 'f_eff': n / F0, 'T': int(len(G)),
                                             'anteil_zug_ok': float(k['ok'].mean()),
                                             'anteil_konvex': float(k['konvex'].mean()), 't_s': time.time() - t0}))
    return zust, st


# ------------------------------------------------------------------------------------------------ Regge-Wirkung
def regge(LV, pos, G, O, nV):
    X = absolut(LV, pos, G, O)
    th = np.real(tg.dieder_batch(X.astype(complex)))
    uniq, inv, l, lt = kanten(LV, pos, G, O, nV)
    dsum = np.bincount(inv.ravel(), th.ravel(), len(uniq))
    eps = 2 * np.pi - dsum
    vol = tet_vol(LV, pos, G, O)
    return {'S': float(np.sum(l * eps)), 'skala_2pi_sum_l': float(2 * np.pi * l.sum()), 'eps_absmax': float(np.abs(eps).max()),
            'E': int(len(uniq)), 'T': int(len(G)), 'vol_summe_rel_abw': float(abs(vol.sum() / abs(np.linalg.det(LV)) - 1)),
            'vol_min_rel_mittel': float(vol.min() / vol.mean()), 'laengen_abw_max': float(np.abs(lt - l[inv.ravel()]).max()),
            'l_mittel': float(l.mean())}


def affin_kurz(mod):
    af = tg.affin(mod)
    return {'min': af['min'], 'max': af['max'], 'spanne_max_min': af['spanne_max_min']}


def modus_kontrolle(N, saaten):
    out = []
    for saat in saaten:
        t0 = time.time()
        LV, pos, G, O, pr = tg.zufallsnetz(N, saat)
        nV = len(pos)
        r0 = regge(LV, pos, G, O, nV)
        z = {'N': N, 'saat': saat, 'netz0': r0, 'affin0': affin_kurz(tg.modell(LV, pos, G, O, pr)), 'nach': []}
        zust, st = zugfolge(LV, pos, G, O, nV, F_LISTE, np.random.default_rng([SAAT_ZUG, N, saat]))
        z['zugstat'] = st
        for (f, Gf, Of, sf) in zust:
            rf = regge(LV, pos, Gf, Of, nV)
            mod = tg.modell(LV, pos, Gf, Of, pr)
            z['nach'].append({'f': f, 'zuege': sf, 'regge': rf, 'dS': rf['S'] - r0['S'],
                              'dS_rel': abs(rf['S'] - r0['S']) / rf['skala_2pi_sum_l'], 'affin': affin_kurz(mod),
                              'pruefung': mod['pruefung']})
        z['t_s'] = time.time() - t0
        out.append(z)
        print('kontrolle', N, saat, '%.1f s' % z['t_s'], flush=True)
    return out


# ------------------------------------------------------------------------------------------------ M-B
def delaunay_periodisch(pos, L):
    """Wie tg.zufallsnetz, aber fuer gegebene (nicht zurueckgefaltete) Lagen; Wuerfel L."""
    offs = np.array([(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)], dtype=np.int64)
    Pl, Il, Ol = [], [], []
    for o in offs:
        Q = pos + o * L
        m = np.all((Q >= -tg.SAUM) & (Q <= L + tg.SAUM), axis=1)
        Pl.append(Q[m])
        Il.append(np.nonzero(m)[0])
        Ol.append(np.repeat(o[None, :], int(m.sum()), axis=0))
    P = np.concatenate(Pl)
    gidx = np.concatenate(Il)
    goff = np.concatenate(Ol)
    S = Delaunay(P).simplices
    X = P[S]
    cen = X.mean(axis=1)
    halte = np.all((cen >= 0.0) & (cen < L), axis=1)
    S, X = S[halte], X[halte]
    A = 2.0 * (X[:, 1:] - X[:, :1])
    b = (X[:, 1:] ** 2).sum(-1) - (X[:, :1] ** 2).sum(-1)
    C = np.linalg.solve(A, b[..., None])[..., 0]
    R = np.linalg.norm(C - X[:, 0], axis=1)
    verletzt = int(np.sum(np.any((C - R[:, None] < -tg.SAUM) | (C + R[:, None] > L + tg.SAUM), axis=1)))
    return gidx[S], goff[S], verletzt


def tetra_schluessel(G, O):
    srt = np.sort(G, axis=1)
    assert np.all(srt[:, 1:] != srt[:, :-1]), 'Ecke doppelt in einem Tetraeder'
    order = np.argsort(G, axis=1)
    gs = np.take_along_axis(G, order, 1)
    os_ = np.take_along_axis(O, order[:, :, None], 1)
    rel = os_ - os_[:, :1, :]
    return np.concatenate([gs, rel.reshape(-1, 12)], axis=1)


def flaechen_je_tet(G, O):
    gv = G[:, FL]
    go = O[:, FL]
    order = np.argsort(gv, axis=2)
    gvs = np.take_along_axis(gv, order, 2)
    gos = np.take_along_axis(go, order[..., None], 2)
    rel = gos - gos[:, :, :1, :]
    return np.concatenate([gvs, rel.reshape(len(G), 4, 9)], axis=2)


def cluster(Gr, Or, Ga, Oa):
    """Zusammenhaengende Aenderungsbereiche: entfernte und neue Tetraeder, verbunden ueber gemeinsame Flaechen."""
    kk = np.concatenate([flaechen_je_tet(Gr, Or), flaechen_je_tet(Ga, Oa)]) if len(Ga) else flaechen_je_tet(Gr, Or)
    nr = len(Gr)
    n = len(kk)
    par = list(range(n))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    seen = {}
    for i in range(n):
        for row in kk[i]:
            t = tuple(row.tolist())
            if t in seen:
                ra, rb = find(i), find(seen[t])
                if ra != rb:
                    par[ra] = rb
            else:
                seen[t] = i
    comp = {}
    for i in range(n):
        r = find(i)
        c = comp.setdefault(r, [0, 0])
        c[0 if i < nr else 1] += 1
    typ = Counter(tuple(v) for v in comp.values())
    return {'n_cluster': len(comp), 'n_23': typ.get((2, 3), 0), 'n_32': typ.get((3, 2), 0),
            'n_sonst': len(comp) - typ.get((2, 3), 0) - typ.get((3, 2), 0),
            'typen': {'%d-%d' % k: v for k, v in typ.most_common(6)}}


def raender(LV, pos, G, O, fl):
    """mu = (|e - C1|^2 - R1^2) / R1^2: Lage der Gegenecke e relativ zur Umkugel von t1; mu < 0 = Delaunay verletzt."""
    t1, i2, t2 = fl['t1'], fl['i2'], fl['t2']
    X1 = absolut(LV, pos, G[t1], O[t1])
    e = pos[G[t2, i2]] + (O[t2, i2] + fl['sh']).astype(float) @ LV
    x0 = X1[:, 0]
    Y = X1 - x0[:, None, :]
    ee = e - x0
    A = 2.0 * Y[:, 1:]
    b = (Y[:, 1:] ** 2).sum(-1)
    C = np.linalg.solve(A, b[..., None])[..., 0]
    R2 = (C ** 2).sum(-1)
    return ((ee - C) ** 2).sum(-1) / R2 - 1.0


def tt_polarisationen(nm):
    for name, d in tg.richtungen13w():
        if name == nm:
            u = np.cross(d, [0.3, 0.5, 0.7])
            u = u / np.linalg.norm(u)
            v = np.cross(d, u)
            return [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]
    raise KeyError(nm)


def modus_mb(N, saaten, n_zieh):
    out = []
    for saat in saaten:
        t0 = time.time()
        LV, pos0, G0, O0, pr = tg.zufallsnetz(N, saat)
        L = float(LV[0, 0])
        nV = len(pos0)
        T0 = len(G0)
        _, _, l, _ = kanten(LV, pos0, G0, O0, nV)
        lbar = float(l.mean())
        k0 = tetra_schluessel(G0, O0)
        k0l = list(map(tuple, k0.tolist()))
        K0 = set(k0l)
        Gs, Os, _ = delaunay_periodisch(pos0.copy(), L)
        selbst = set(map(tuple, tetra_schluessel(Gs, Os).tolist())) == K0
        fl = flaechen(G0, O0)
        mu0 = raender(LV, pos0, G0, O0, fl)
        z = {'N': N, 'saat': saat, 'T0': T0, 'F0': fl['F'], 'E0': int(len(l)), 'l_mittel': lbar, 'selbsttest_a0': bool(selbst),
             'mu0_min': float(mu0.min()), 'mu0_n_neg': int((mu0 < 0).sum()),
             'mu0_cdf': {('%g' % x): int((mu0 < x).sum()) for x in X_CDF}, 'n_zieh': n_zieh, 'a': A_LISTE, 'zufall': [],
             'dehnung': []}
        rng = np.random.default_rng([SAAT_MB, N, saat])
        xis = [rng.normal(size=(nV, 3)) for _ in range(n_zieh)]
        for a in A_LISTE:
            rec = {'a': a, 'n_weg': [], 'n_neu': [], 'T_neu': [], 'n_verletzt': [], 'n_cluster': [], 'n_23': [], 'n_32': [],
                   'n_sonst': [], 'saum_verletzt': [], 'typen': Counter()}
            for xi in xis:
                pos = pos0 + xi * (a * lbar / np.sqrt(3.0))
                Gn, On, v = delaunay_periodisch(pos, L)
                kn = tetra_schluessel(Gn, On)
                knl = list(map(tuple, kn.tolist()))
                Kn = set(knl)
                rem = np.array([i for i, t in enumerate(k0l) if t not in Kn], np.int64)
                add = np.array([i for i, t in enumerate(knl) if t not in K0], np.int64)
                if len(rem) or len(add):
                    cl = cluster(G0[rem], O0[rem], Gn[add] if len(add) else Gn[:0], On[add] if len(add) else On[:0])
                else:
                    cl = {'n_cluster': 0, 'n_23': 0, 'n_32': 0, 'n_sonst': 0, 'typen': {}}
                mu = raender(LV, pos, G0, O0, fl)
                rec['n_weg'].append(int(len(rem)))
                rec['n_neu'].append(int(len(add)))
                rec['T_neu'].append(int(len(Gn)))
                rec['n_verletzt'].append(int((mu < 0).sum()))
                for kx in ('n_cluster', 'n_23', 'n_32', 'n_sonst'):
                    rec[kx].append(int(cl[kx]))
                rec['saum_verletzt'].append(v)
                rec['typen'].update(cl['typen'])
            rec['typen'] = dict(rec['typen'].most_common(8))
            z['zufall'].append(rec)
        for nm in ('100', '110', '111'):
            for ip, h in enumerate(tt_polarisationen(nm)):
                zeile = {'richtung': nm, 'pol': ip, 'n_verletzt': []}
                for a in A_LISTE:
                    Fm = np.eye(3) + a * h
                    mu = raender(LV @ Fm, pos0 @ Fm, G0, O0, fl)
                    zeile['n_verletzt'].append(int((mu < 0).sum()))
                z['dehnung'].append(zeile)
        z['t_s'] = time.time() - t0
        out.append(z)
        print('mb', N, saat, '%.1f s' % z['t_s'], flush=True)
    return out


# ------------------------------------------------------------------------------------------------ TT
def modus_tt(N, saat, f, ridx):
    LV, pos, G, O, pr = tg.zufallsnetz(N, saat)
    st = None
    if f > 0:
        zust, st = zugfolge(LV, pos, G, O, len(pos), [f], np.random.default_rng([SAAT_ZUG, N, saat]))
        _, G, O, sf = zust[-1]
        st['ende'] = sf
    mod = tg.modell(LV, pos, G, O, pr)
    return {'N': N, 'saat': saat, 'f': f, 'zugstat': st, 'pruefung': mod['pruefung'], 'ridx': ridx,
            'spektrum': tg.spektrum(mod, ridx)}


# ------------------------------------------------------------------------------------------------ main
def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['kontrolle', 'mb', 'tt'])
    ap.add_argument('--N', type=int, required=True)
    ap.add_argument('--saaten', default='1', help='z.B. 1,2,3 oder 1-24')
    ap.add_argument('--f', type=float, default=0.0)
    ap.add_argument('--ridx', default='0-12')
    ap.add_argument('--zieh', type=int, default=8)
    ap.add_argument('--rauch', action='store_true', help='nur Schluessel und Laufzeiten speichern, keine Werte')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    def liste(s):
        if '-' in s and ',' not in s:
            i0, i1 = s.split('-')
            return list(range(int(i0), int(i1) + 1))
        return [int(x) for x in s.split(',')]
    saaten = liste(a.saaten)
    ridx = liste(a.ridx)
    t0 = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)), 'tg_sha256': sha(os.path.abspath(tg.__file__)),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'kontrolle':
        erg = modus_kontrolle(a.N, saaten)
    elif a.modus == 'mb':
        erg = modus_mb(a.N, saaten, a.zieh)
    else:
        erg = [modus_tt(a.N, s, a.f, ridx) for s in saaten]
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        tz = []
        if a.modus == 'tt':
            tz = [[z['eps1']['t_s'] for z in e['spektrum']] for e in erg]
        res = {'info': info, 'schluessel': tg.nur_schluessel(erg[0]) if erg else None, 'laufzeit_s': res['laufzeit_s'],
               'maxrss_MB': res['maxrss_MB'], 't_punkt_s': tz}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, a.N, a.saaten, 'f=%g' % a.f, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
