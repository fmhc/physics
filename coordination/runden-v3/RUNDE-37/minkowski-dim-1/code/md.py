#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MINKOWSKI-DIM-1 (Runde 48, fmhc-physics), Code-Agent fuer die Leitung claude-primary, 05.10.2026.

Karte: RUNDE-37/minkowski-dim-1/KARTE.md (unveraendert); Regeln: PLAN.md.
Modi:
  kasten     MD0: Kaestchenzaehlung.
             (a) 2-Geruest von V (Vereinigung aller Dreiecke): Torus der kubischen Zelle (L = 1, Kaestchen 1/m) und
                 Torus aus 8^3 kubischen Zellen (L = 8, Kaestchen 8/m); Dreiecke mit Punktabstand h = eps/8 abgetastet.
             (b) Ecken des Sierpinski-Tetraeders (Stufe 10, Kontrolle Stufe 8), Kaestchen 2^(-7 + j/4), j = 0..20,
                 feste Gitterverschiebung; dazu dyadisch ausgerichtete Kaestchen (nur berichtet).
  kubisch    MD1: d_s(sigma) = 12 sigma (1 - I1(2 sigma)/I0(2 sigma)) (einfaches kubisches Gitter, Graph-Laplace).
  takt       MD3/MD4: d_s(sigma) = 2 sigma <lambda>_sigma aus der Spur von exp(-sigma X) ueber das volle Spektrum.
             X = *0^-1 T (gewertet; T = 8 d0^H *1 d0 = Finns Takt nach HT0), T allein, Graph-Laplace der Netzkanten.
             Periodische Netze: Gamma-zentriertes k-Gitter n^3. Glas: Eigenwerte bei k = 0 (Torus), Kontrolle k-Gitter 2^3.
  auswertung Urteile MD0 bis MD4 nach PLAN.md Abschnitt 5 (liest kasten.json, kubisch.json, takt-*.json, s_st*.json,
             b_st*.json eines Ordners).
Unveraendert importiert: tu.py (TAKT-UMKLAPP-1: hodge, takt_mats, netz_aus_ew, tet_X), tg.py, uk.py, ew.py, mn.py,
tg_auswertung.py, tp.py, dn.py (DEFEKT-NETZ-1: kristall, periodisch_delaunay, gleichstaende, FCC), tti.py,
nachtrag_kinetik.py.
"""
import argparse, json, os, sys, time, hashlib, platform, resource, math, glob

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
import scipy
from scipy import special, optimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import uk  # noqa: E402
import tu  # noqa: E402
import dn  # noqa: E402

T0 = time.time()
TAKT_FAKTOR = 8.0                 # T = 8 d0^H *1 d0 (TAKT-UMKLAPP-1, HT0); fuer d_s ohne Belang (Skala von sigma)
SIG_J0, SIG_J1 = -300, 500        # sigma * lambda_mittel = 10^(j/100), j = -300..500 (8 Dekaden, 100 je Dekade)
ZUL_C = 8.0                       # zulaessig: P(sigma) >= 8 / N_ges (Torus-Bildkorrektur in d_s < 1e-3)
STUFE_STEIG = 0.1                 # Stufe: |d d_s / d log10 sigma| < 0,1 ...
STUFE_BAND = (1.6, 2.4)           # ... und 1,6 <= d_s <= 2,4 ...
STUFE_DEK = 0.5                   # ... ueber mindestens eine halbe Dekade (zusammenhaengend)
K_GEW, K_KONTR = 40, 20           # k-Gitter n^3 (periodische Netze), V/S/A15; C15 (24 Ecken je Zelle) 32 bzw. 16
K_GEW_C15, K_KONTR_C15 = 32, 16
OFF_V = np.array([0.0123457, 0.0234568, 0.0345679])     # Verschiebung des Geruests gegen das Kaestchengitter
OFF_ST = np.array([0.0123457, 0.0234568, 0.0345679])
HF = 8.0                          # Punktabstand h = eps / HF auf den Dreiecken
ST_J = list(range(0, 21))         # Sierpinski-Tetraeder: eps_j = 2^(-7 + j/4)
DS_ST = 2.0 * math.log(4.0) / math.log(6.0)               # 1,5474
P_ST = DS_ST / (1.0 + DS_ST)                               # 0,6074
P_ST_KARTE, P_MINK_KARTE = 0.607, 0.667


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def schreibe(pfad, obj):
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(obj, fh, indent=1)
    os.replace(pfad + '.tmp', pfad)


# ------------------------------------------------------------------------------------------------ Netze
def netz(name):
    if name == 'V':
        LV, pos, G, O, pr = tg.netz_V()
        pr = dict(pr)
    elif name == 'S':
        LV, pos, G, O, pr = tu.netz_aus_ew('S')
        pr = dict(pr)
    elif name in ('C15', 'A15'):
        LV, pos, typ = dn.kristall(name)
        G, O, keys, info = dn.periodisch_delaunay(LV, pos)
        pr = {'delaunay': info, 'umkugel': dn.gleichstaende(LV, pos, G, O)}
    elif name.startswith('glas-'):
        _, nN, ns = name.split('-')
        LV, pos, G, O, pr = tg.zufallsnetz(int(nN[1:]), int(ns[1:]))
        pr = dict(pr)
    else:
        raise ValueError(name)
    return LV, pos, G, O, pr


def stern0(LV, pos, G, O, mod, Ast):
    """*0 je Ecke wie in tu.hodge (dort nicht zurueckgegeben): sum ueber Kanten l A*/6 an beide Enden."""
    X = tu.tet_X(LV, pos, G, O)
    nV = mod['nV']
    s0 = np.zeros(nV)
    for p, (i, j, k, l) in enumerate(tg.PAARE):
        lt = np.linalg.norm(X[:, j] - X[:, i], axis=1)
        w = lt * Ast[:, p] / 6.0
        s0 += np.bincount(G[:, i], w, nV) + np.bincount(G[:, j], w, nV)
    return s0


def matrizen(mod, ks, gew):
    """X(k) = d0(k)^H diag(gew) d0(k) fuer alle k (Nk, nV, nV); d0-Zeile e: -1 an es, +exp(i k.T_e) an es2 (wie tu)."""
    E, nV = mod['E'], mod['nV']
    es, es2 = mod['es'], mod['es2']
    ph = np.exp(1j * (np.asarray(ks) @ mod['Tedge'].T))
    M = np.zeros((len(ks), nV, nV), complex)
    diag = np.bincount(es, gew, nV) + np.bincount(es2, gew, nV)
    M[:, np.arange(nV), np.arange(nV)] += diag
    for e in range(E):
        M[:, es[e], es2[e]] -= gew[e] * ph[:, e]
        M[:, es2[e], es[e]] -= gew[e] * np.conj(ph[:, e])
    return M


def kgitter(LV, n):
    rez = 2 * np.pi * np.linalg.inv(LV).T
    g = np.arange(n)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    return (mm / float(n)) @ rez


def eigenwerte(mod, ks, gew, s0=None, chunk=2048):
    out = []
    d = None if s0 is None else 1.0 / np.sqrt(s0)
    for i in range(0, len(ks), chunk):
        M = matrizen(mod, ks[i:i + chunk], gew)
        if d is not None:
            M = M * d[None, :, None] * d[None, None, :]
        out.append(np.linalg.eigvalsh(M).ravel())
    return np.concatenate(out)


def waerme(lam, sig):
    """P(sigma) = mean exp(-sigma lam); d_s = 2 sigma <lam>; d d_s/d ln sigma = d_s - 2 sigma^2 Var(lam) (exakt)."""
    lam = np.clip(np.asarray(lam, float), 0.0, None)
    n = len(lam)
    P = np.empty(len(sig))
    m1 = np.empty(len(sig))
    m2 = np.empty(len(sig))
    for i, s in enumerate(sig):
        w = np.exp(-s * lam)
        Z = w.sum()
        wl = w * lam
        P[i] = Z / n
        m1[i] = wl.sum() / Z
        m2[i] = (wl * lam).sum() / Z
    ds = 2.0 * sig * m1
    steig_ln = ds - 2.0 * sig ** 2 * (m2 - m1 ** 2)
    return P, ds, steig_ln * math.log(10.0)


def zonen(maske):
    z, i, n = [], 0, len(maske)
    while i < n:
        if maske[i]:
            j = i
            while j + 1 < n and maske[j + 1]:
                j += 1
            z.append((i, j))
            i = j + 1
        else:
            i += 1
    return z


def analyse(sig, P, ds, steig, N_ges):
    zul = P >= ZUL_C / N_ges
    i_end = int(np.nonzero(zul)[0].max())
    imax = int(np.argmax(ds[:i_end + 1]))
    band = (ds >= STUFE_BAND[0]) & (ds <= STUFE_BAND[1]) & (np.abs(steig) < STUFE_STEIG) & zul
    zz = []
    for (a, b) in zonen(band):
        dek = math.log10(sig[b] / sig[a])
        zz.append({'sigma_von': float(sig[a]), 'sigma_bis': float(sig[b]), 'dekaden': dek,
                   'ds_von': float(ds[a]), 'ds_bis': float(ds[b]), 'ist_stufe': bool(dek >= STUFE_DEK - 1e-9)})
    # laengste flache Zone ueberhaupt (|Steigung| < 0,1, ohne Band), nur berichtet
    flach = zonen((np.abs(steig) < STUFE_STEIG) & zul)
    fz = [{'sigma_von': float(sig[a]), 'sigma_bis': float(sig[b]), 'dekaden': math.log10(sig[b] / sig[a]),
           'ds_mittel': float(ds[a:b + 1].mean())} for (a, b) in flach]
    fz = sorted(fz, key=lambda z: -z['dekaden'])[:6]
    nach = ds[imax:i_end + 1]
    return {'N_ges': int(N_ges), 'i_end_zulaessig': i_end, 'sigma_end_zulaessig': float(sig[i_end]),
            'ds_end_zulaessig': float(ds[i_end]), 'P_end': float(P[i_end]),
            'max_ds': float(ds[imax]), 'sigma_max': float(sig[imax]), 'P_bei_max': float(P[imax]),
            'max_innen': bool(0 < imax < i_end), 'min_ds_nach_max': float(nach.min()),
            'ds_nach_max_immer_ueber_3': bool(np.all(nach > 3.0)),
            'stufen_zonen': zz, 'stufe_da': bool(any(z['ist_stufe'] for z in zz)),
            'flache_zonen_berichtet': fz,
            'ds_bei': {('%g' % x): float(np.interp(math.log(x), np.log(sig / sig[imax]), ds)) for x in (0.1, 0.3, 3, 10, 30, 100)}}


def kurve(lam, N_ges, unter=2):
    lam = np.asarray(lam, float)
    lbar = float(np.clip(lam, 0, None).mean())
    sig = 10.0 ** (np.arange(SIG_J0, SIG_J1 + 1) / 100.0) / lbar
    P, ds, st = waerme(lam, sig)
    an = analyse(sig, P, ds, st, N_ges)
    an.update({'lambda_mittel': lbar, 'lambda_min_roh': float(lam.min()), 'lambda_max': float(lam.max()),
               'n_lambda': int(len(lam))})
    return an, {'sigma': sig[::unter].tolist(), 'P': P[::unter].tolist(), 'ds': ds[::unter].tolist(),
                'steig_dek': st[::unter].tolist()}


# ------------------------------------------------------------------------------------------------ Modus takt
def lauf_takt(netze, rauch=False):
    erg = []
    for name in netze:
        t0 = time.time()
        LV, pos, G, O, pr = netz(name)
        mod = tg.modell(LV, pos, G, O, pr)
        h, s1, s2, Ast = tu.hodge(LV, pos, G, O, mod)
        s0 = stern0(LV, pos, G, O, mod, Ast)
        glas = name.startswith('glas-')
        z = {'netz': name, 'nV': int(mod['nV']), 'E': int(mod['E']), 'T': int(mod['T']),
             'pruefung': {k: v for k, v in mod['pruefung'].items() if k != 't_modell_s'}, 'netz_info': pr,
             'hodge': h, 'stern0': {'min': float(s0.min()), 'max': float(s0.max()), 'n_nicht_pos': int((s0 <= 0).sum()),
                                     'summe_durch_V': float(s0.sum() / abs(np.linalg.det(LV)))},
             'stern1_n_nicht_pos': int((s1 <= 0).sum())}
        # Kontrolle: eigene Matrix gegen tu.takt_mats (P = -W^H B W und L1 = d0^H *1 d0) an drei k
        rng = np.random.default_rng([4848, len(name)])
        rez = 2 * np.pi * np.linalg.inv(LV).T
        kk = [rng.uniform(0, 1, 3) @ rez for _ in range(3)]
        rest_L1, rest_P = [], []
        for k in kk:
            Pk, L1k = tu.takt_mats(mod, k, s1)
            Mk = matrizen(mod, k[None, :], s1)[0]
            rest_L1.append(float(np.abs(Mk - L1k).max() / np.abs(L1k).max()))
            rest_P.append(float(np.abs(Pk - TAKT_FAKTOR * L1k).max() / np.abs(Pk).max()))
        z['kontrolle_matrix'] = {'rest_L1_max': max(rest_L1), 'rest_P_gegen_8L1_max': max(rest_P)}
        if glas:
            gitter = {'gewertet': (np.zeros((1, 3)), 'Gamma'), 'kontrolle': (kgitter(LV, 2), 'k-Gitter 2^3')}
        else:
            ng, nk = (K_GEW_C15, K_KONTR_C15) if name == 'C15' else (K_GEW, K_KONTR)
            if rauch:
                ng, nk = 6, 4
            gitter = {'gewertet': (kgitter(LV, ng), 'k-Gitter %d^3' % ng), 'kontrolle': (kgitter(LV, nk), 'k-Gitter %d^3' % nk)}
        ops = {'takt_s0': (TAKT_FAKTOR * s1, s0), 'takt': (TAKT_FAKTOR * s1, None), 'graph': (np.ones(mod['E']), None)}
        z['ops'] = {}
        for on, (gew, w0) in ops.items():
            if w0 is not None and np.any(w0 <= 0):
                z['ops'][on] = {'uebersprungen': '*0 nicht positiv'}
                continue
            z['ops'][on] = {}
            for gn, (ks, gtext) in gitter.items():
                t1 = time.time()
                lam = eigenwerte(mod, ks, gew, w0)
                an, kv = kurve(lam, len(lam))
                an['gitter'] = gtext
                an['n_k'] = int(len(ks))
                an['sek'] = time.time() - t1
                z['ops'][on][gn] = {'analyse': an, 'kurve': kv}
        z['sek'] = time.time() - t0
        erg.append(z)
        print('takt', name, '%.1f s' % z['sek'], flush=True)
    return erg


# ------------------------------------------------------------------------------------------------ Modus kubisch
def ds_kub(s):
    s = np.asarray(s, float)
    return 12.0 * s * (1.0 - special.i1e(2.0 * s) / special.i0e(2.0 * s))


def lauf_kubisch():
    sig = 10.0 ** (np.arange(-300, 401) / 100.0)
    ds = ds_kub(sig)
    imax = int(np.argmax(ds))
    r = optimize.minimize_scalar(lambda x: -float(ds_kub(x)), bounds=(sig[imax - 1], sig[imax + 1]), method='bounded',
                                 options={'xatol': 1e-12})
    nach = ds[imax:]
    von_oben = bool(np.all(nach > 3.0) and np.all(np.diff(nach) <= 0.0) and (ds[-1] - 3.0) <= 1e-3)
    # Kontrollen: periodisches Gitter n = 64 (Produktformel) gegen Bessel bis sigma = 20; eigvalsh 8^3 gegen Produkt
    n = 64
    l1 = 2.0 - 2.0 * np.cos(2.0 * np.pi * np.arange(n) / n)
    ss = sig[sig <= 20.0]
    d64 = np.array([3.0 * 2.0 * s * (l1 * np.exp(-s * l1)).sum() / np.exp(-s * l1).sum() for s in ss])
    m = 8
    idx = np.arange(m ** 3).reshape(m, m, m)
    A = np.zeros((m ** 3, m ** 3))
    for ax in range(3):
        nb = np.roll(idx, -1, axis=ax)
        A[idx.ravel(), nb.ravel()] += 1.0
        A[nb.ravel(), idx.ravel()] += 1.0
    Lm = np.diag(A.sum(1)) - A
    le = np.sort(np.linalg.eigvalsh(Lm))
    l8 = 2.0 - 2.0 * np.cos(2.0 * np.pi * np.arange(m) / m)
    gg = np.meshgrid(l8, l8, l8, indexing='ij')
    lp = np.sort((gg[0] + gg[1] + gg[2]).ravel())
    # numerische Ableitung von ln P (Kontrolle der Formel)
    lnP = lambda s: 3.0 * np.log(special.i0e(2.0 * s))
    hs = 1e-5
    dnum = np.array([-2.0 * s * (lnP(s * (1 + hs)) - lnP(s * (1 - hs))) / (2 * hs * s) for s in (0.3, 0.87, 3.0, 30.0)])
    return {'sigma': sig[::4].tolist(), 'ds': ds[::4].tolist(),
            'max_gitter': {'ds': float(ds[imax]), 'sigma': float(sig[imax])},
            'max_fein': {'ds': float(-r.fun), 'sigma': float(r.x)},
            'von_oben': von_oben, 'ds_ende': float(ds[-1]), 'sigma_ende': float(sig[-1]),
            'nach_max_alle_ueber_3': bool(np.all(nach > 3.0)), 'nach_max_monoton_fallend': bool(np.all(np.diff(nach) <= 0.0)),
            'asymptotik': {('%g' % s): {'ds': float(ds_kub(s)), '3+3/(8s)': 3.0 + 3.0 / (8.0 * s)} for s in (10.0, 100.0, 1000.0, 10000.0)},
            'kontrolle_n64_max_abw_bis_sigma20': float(np.abs(d64 - ds_kub(ss)).max()),
            'kontrolle_eig_8hoch3_max_abw': float(np.abs(le - lp).max()),
            'kontrolle_ableitung_rel': (dnum / ds_kub(np.array([0.3, 0.87, 3.0, 30.0])) - 1.0).tolist(),
            'werte': {('%g' % s): float(ds_kub(s)) for s in (0.1, 0.5, 0.8, 0.85, 0.9, 1.0, 1.5, 2.0, 5.0)}}


# ------------------------------------------------------------------------------------------------ Modus kasten
_BARY = {}


def bary(n):
    if n not in _BARY:
        i, j = np.meshgrid(np.arange(n + 1), np.arange(n + 1), indexing='ij')
        m = (i + j) <= n
        _BARY[n] = (i[m].astype(float) / n, j[m].astype(float) / n)
    return _BARY[n]


def zaehle_dreiecke(tri, L, m, off, hf=HF, max_pkt=4_000_000):
    """Zahl der Kaestchen (Kante eps = L/m) des Torus [0, L)^3, die eine Abtastung der Dreiecke treffen."""
    eps = L / float(m)
    h = eps / hf
    occ = np.zeros(m ** 3, bool)
    A, B, C = tri[:, 0], tri[:, 1], tri[:, 2]
    lmax = np.max(np.stack([np.linalg.norm(B - A, axis=1), np.linalg.norm(C - A, axis=1),
                            np.linalg.norm(C - B, axis=1)]), axis=0)
    nsub = np.maximum(1, np.ceil(lmax / h).astype(int))
    npkt = 0
    for n in np.unique(nsub):
        sel = np.nonzero(nsub == n)[0]
        u, v = bary(int(n))
        step = max(1, max_pkt // len(u))
        for s in range(0, len(sel), step):
            t = sel[s:s + step]
            P = (A[t, None, :] + u[None, :, None] * (B - A)[t, None, :] + v[None, :, None] * (C - A)[t, None, :]).reshape(-1, 3)
            q = np.mod(np.floor((P + off) / eps).astype(np.int64), m)
            occ[(q[:, 0] * m + q[:, 1]) * m + q[:, 2]] = True
            npkt += len(P)
    return int(occ.sum()), npkt


def dreiecke_V():
    LV, pos, G, O, pr = tg.netz_V()
    mod = tg.modell(LV, pos, G, O, pr)
    X = tu.tet_X(LV, pos, G, O)
    fl = uk.flaechen(G, O)
    tri = X[fl['t1'][:, None], uk.FL[fl['i1']]]
    assert abs(abs(np.linalg.det(LV)) - 0.25) < 1e-12
    tri_c = np.concatenate([tri + t for t in dn.FCC])
    fl_inhalt = 0.5 * np.linalg.norm(np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0]), axis=1)
    vol = np.abs(uk.vol6(X[:, 0], X[:, 1], X[:, 2], X[:, 3])) / 6.0
    # groesste Inkugel (Kaestchen darueber treffen sicher)
    Ft = np.stack([0.5 * np.linalg.norm(np.cross(X[:, b] - X[:, a], X[:, c] - X[:, a]), axis=1) for (a, b, c) in uk.FL], 1)
    r_in = 3.0 * vol / Ft.sum(1)
    info = {'F_primitiv': int(fl['F']), 'T_primitiv': int(len(G)), 'E_primitiv': int(mod['E']),
            'a_mittlere_kante': float(mod['l'].mean()), 'l_min': float(mod['l'].min()), 'l_max': float(mod['l'].max()),
            'flaeche_kubische_zelle': float(4 * fl_inhalt.sum()), 'vol_summe_primitiv': float(vol.sum()),
            'inkugel_durchmesser_max': float(2 * r_in.max())}
    return tri_c, info


def st_punkte(stufe):
    v = np.array([[0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=np.int64)
    o = np.zeros((1, 3), dtype=np.int64)
    for i in range(stufe):
        s = 2 ** (stufe - 1 - i)
        o = (o[:, None, :] + s * v[None, :, :]).reshape(-1, 3)
    ecken = (o[:, None, :] + v[None, :, :]).reshape(-1, 3)
    pts = np.unique(ecken, axis=0)
    assert len(pts) == 2 * 4 ** stufe + 2
    return pts.astype(float) / 2 ** stufe


def zaehle_punkte(P, eps, off):
    q = np.floor((P + off) / eps).astype(np.int64)
    q -= q.min(axis=0)
    M = q.max(axis=0) + 1
    return int(len(np.unique((q[:, 0] * M[1] + q[:, 1]) * M[2] + q[:, 2])))


def steigung(eps, N):
    x = np.log(1.0 / np.asarray(eps, float))
    y = np.log(np.asarray(N, float))
    return float(np.polyfit(x, y, 1)[0])


def lauf_kasten(rauch=False):
    out = {}
    t0 = time.time()
    tri, info = dreiecke_V()
    a = info['a_mittlere_kante']
    out['V'] = {'info': info, 'a': a}
    # kleines Fenster: Torus L = 1, eps = 1/m, m_j = round((8/a) 2^(j/4)), j = 0..12, nur a/64 <= eps <= a/8
    mk = sorted(set(int(round((8.0 / a) * 2 ** (j / 4.0))) for j in range(0, 13)))
    if rauch:
        mk = mk[:3]
    klein = []
    for m in mk:
        eps = 1.0 / m
        if not (a / 64.0 - 1e-12 <= eps <= a / 8.0 + 1e-12):
            continue
        t1 = time.time()
        N, npk = zaehle_dreiecke(tri, 1.0, m, OFF_V)
        klein.append({'m': m, 'eps': eps, 'eps_durch_a': eps / a, 'N': N, 'punkte': npk, 'sek': time.time() - t1})
    out['V']['klein'] = klein
    # Uebergang (nur berichtet): Torus L = 1, m = 1..ceil(8/a)
    ueb = []
    for m in range(1, int(math.ceil(8.0 / a)) + 1):
        if rauch and m > 3:
            break
        N, npk = zaehle_dreiecke(tri, 1.0, m, OFF_V)
        ueb.append({'m': m, 'eps': 1.0 / m, 'eps_durch_a': 1.0 / (m * a), 'N': N})
    out['V']['uebergang_L1'] = ueb
    # grosses Fenster: Torus L = 8 (8^3 kubische Zellen), eps = 8/m, 2a <= eps <= 10a
    L = 8
    trL = np.concatenate([tri + np.array(s, float) for s in np.ndindex(L, L, L)]) if not rauch else tri
    LL = L if not rauch else 1
    gross = []
    for m in range(1, 64):
        eps = LL / float(m)
        if not (2.0 * a - 1e-12 <= eps <= 10.0 * a + 1e-12):
            continue
        t1 = time.time()
        N, npk = zaehle_dreiecke(trL, float(LL), m, OFF_V)
        gross.append({'m': m, 'eps': eps, 'eps_durch_a': eps / a, 'N': N, 'm_hoch_3': m ** 3, 'alle_getroffen': bool(N == m ** 3),
                      'punkte': npk, 'sek': time.time() - t1})
    out['V']['gross'] = gross
    out['V']['steigung_klein'] = steigung([r['eps'] for r in klein], [r['N'] for r in klein]) if len(klein) > 1 else None
    out['V']['steigung_gross'] = steigung([r['eps'] for r in gross], [r['N'] for r in gross]) if len(gross) > 1 else None
    out['V']['sekanten_klein'] = [math.log(klein[i + 1]['N'] / klein[i]['N']) / math.log(klein[i]['eps'] / klein[i + 1]['eps'])
                                  for i in range(len(klein) - 1)]
    # Kontrolle: N(L=8, eps=1) = 512 N(L=1, eps=1)
    n81 = [r['N'] for r in gross if r['m'] == 8]
    n11 = [r['N'] for r in ueb if r['m'] == 1]
    out['V']['kontrolle_L8_gegen_L1_bei_eps1'] = {'N_L8': n81[0] if n81 else None, 'N_L1_mal_512': 512 * n11[0] if n11 else None}
    out['V']['sek'] = time.time() - t0
    # Sierpinski-Tetraeder
    for stufe in ((10, 8) if not rauch else (6,)):
        t1 = time.time()
        P = st_punkte(stufe)
        zeilen = []
        for j in ST_J:
            eps = 2.0 ** (-7.0 + j / 4.0)
            zeilen.append({'j': j, 'eps': eps, 'N': zaehle_punkte(P, eps, OFF_ST)})
        dy = [{'eps': 2.0 ** -q, 'N': zaehle_punkte(P, 2.0 ** -q, np.zeros(3))} for q in range(2, 8)]
        out['ST%d' % stufe] = {'stufe': stufe, 'n_punkte': int(len(P)), 'zeilen': zeilen,
                               'steigung': steigung([r['eps'] for r in zeilen], [r['N'] for r in zeilen]),
                               'steigung_je_oktave': [math.log(zeilen[i + 4]['N'] / zeilen[i]['N']) / math.log(2.0)
                                                      for i in range(0, len(zeilen) - 4)],
                               'dyadisch_ausgerichtet': dy,
                               'dyadisch_steigung': steigung([r['eps'] for r in dy], [r['N'] for r in dy]),
                               'sek': time.time() - t1}
    return out


# ------------------------------------------------------------------------------------------------ Modus auswertung
def lade(p):
    with open(p) as fh:
        return json.load(fh)


def w_ber(x, lo, hi):
    return x is not None and lo - 1e-12 <= x <= hi + 1e-12


def aw_md0(k):
    V = k['V']
    sk, sg = V['steigung_klein'], V['steigung_gross']
    sts = 'ST10' if 'ST10' in k else sorted(x for x in k if x.startswith('ST'))[-1]
    st = k[sts]['steigung']
    teile = {'V_klein': {'wert': sk, 'soll': '2,0 +- 0,1', 'ok': w_ber(sk, 1.9, 2.1)},
             'V_gross': {'wert': sg, 'soll': '3,0 +- 0,1', 'ok': w_ber(sg, 2.9, 3.1)},
             sts: {'wert': st, 'soll': '2,00 +- 0,05', 'ok': w_ber(st, 1.95, 2.05)}}
    return {'urteil': 'eingetroffen' if all(t['ok'] for t in teile.values()) else 'nicht eingetroffen', 'teile': teile}


def aw_md1(kb):
    mx = kb['max_fein']['ds']
    ok = w_ber(mx, 3.4, 3.8) and kb['von_oben']
    return {'urteil': 'eingetroffen' if ok else 'nicht eingetroffen', 'max': mx, 'sigma_max': kb['max_fein']['sigma'],
            'von_oben': kb['von_oben'], 'ds_ende': kb['ds_ende']}


def periodenfenster(lam, N, sig_a=1.0, c=10.0):
    """Mittel von d_s ueber eine log-Periode (Faktor 6 in sigma) = -2 ln(P(6 s0)/P(s0)) / ln 6."""
    lam = np.clip(np.asarray(lam, float), 0.0, None)

    def Pf(s):
        return float(np.exp(-s * lam).sum() / len(lam))
    sig = 10.0 ** (np.arange(-200, 601) / 100.0)
    P = np.array([Pf(s) for s in sig])
    zul = (sig >= sig_a) & (P >= c / N)
    if not np.any(zul):
        return None
    sb = float(sig[np.nonzero(zul)[0].max()])
    if sb < 6.0 * sig_a:
        return {'sigma_b': sb, 'gewertet': None}
    mitte = math.sqrt(sig_a * sb)
    s0 = mitte / math.sqrt(6.0)
    gew = -2.0 * math.log(Pf(6.0 * s0) / Pf(s0)) / math.log(6.0)
    gl = []
    for s in sig:
        if s >= sig_a and 6.0 * s <= sb * (1 + 1e-12):
            gl.append({'s0': float(s), 'ds_mittel': -2.0 * math.log(Pf(6.0 * s) / Pf(s)) / math.log(6.0)})
    vals = [g['ds_mittel'] for g in gl]
    return {'sigma_a': sig_a, 'sigma_b': sb, 'P_grenze': c / N, 's0': s0, 'fenster': [s0, 6.0 * s0], 'gewertet': gew,
            'gleitend_min': min(vals), 'gleitend_max': max(vals), 'gleitend_mittel': float(np.mean(vals)),
            'gleitend': gl[::10]}


def beutel_st(ordner):
    g = {'dateien': [], 'k': {}}
    for p in sorted(glob.glob(os.path.join(ordner, 'b_st*.json'))):
        d = lade(p)
        g['spec'] = d['graph']['spec']
        g['graph'] = d['graph']
        g['dateien'].append({'datei': os.path.basename(p), 'fertig': d.get('fertig'), 'abbruch': d.get('abbruch'),
                             'punkte': len(d['punkte']), 'sek': d.get('sek')})
        for pt in d['punkte']:
            e = g['k'].setdefault(pt['k'], {'Q': pt['Q'], 'starts': [], 'dEdQ': []})
            if abs(e['Q'] / pt['Q'] - 1) > 1e-12:
                raise SystemExit('Q passt nicht: k=%d' % pt['k'])
            for s in pt['starts']:
                e['starts'].append(dict(s, datei=os.path.basename(p)))
            if 'dEdQ' in pt:
                e['dEdQ'].append(pt['dEdQ'])
    return g


def laengster_lauf(ks):
    ks = sorted(ks)
    best, cur = [], []
    for k in ks:
        if cur and k == cur[-1] + 1:
            cur.append(k)
        else:
            cur = [k]
        if len(cur) >= len(best):
            best = list(cur)
    return best


def aw_beutel(g):
    tab = {}
    for k in sorted(g['k']):
        e = g['k'][k]
        konv = [s for s in e['starts'] if s['konvergiert']]
        kand = [s for s in konv if s['diag']['kompakt']]
        a = min(kand, key=lambda s: s['E']) if kand else None
        zentral = [s for s in konv if s['diag']['dmin'] <= 2]
        z = {'k': k, 'Q': e['Q'], 'n_starts': len(e['starts']), 'n_konv': len(konv)}
        if a is not None:
            d = a['diag']
            tiefer_zentral = [s for s in zentral if s['E'] < a['E'] * (1 - 1e-9)]
            z.update({'E': a['E'], 'start': a['start'], 'datei': a['datei'], 'p_omega': d['p_omega'], 'nB': d['nB'],
                      'Rg': d['Rg'], 'Rs': d['Rs'], 'kompakt': True, 'omega': d['omega'],
                      'tiefer_zentral_nicht_kompakt': [{'start': s['start'], 'E': s['E'], 'nB': s['diag']['nB'],
                                                        'nicht_fuellend': s['diag']['nicht_fuellend']} for s in tiefer_zentral],
                      'sauber': len(tiefer_zentral) == 0,
                      'kompakt_starts': [{'start': s['start'], 'dE_rel': s['E'] / a['E'] - 1, 'nB': s['diag']['nB']} for s in kand]})
        else:
            z.update({'E': None, 'kompakt': False, 'sauber': False})
        alle = min(konv, key=lambda s: s['E']) if konv else None
        if alle is not None:
            z['tiefster_insgesamt'] = {'start': alle['start'], 'E': alle['E'], 'dmin': alle['diag']['dmin'],
                                       'nB': alle['diag']['nB'], 'kompakt': alle['diag']['kompakt']}
        z['dEdQ'] = e['dEdQ']
        tab[k] = z
    ks = sorted(tab)
    bereich = laengster_lauf([k for k in ks if tab[k]['E'] is not None and tab[k]['sauber']])
    bereich_alt = laengster_lauf([k for k in ks if tab[k]['E'] is not None])

    def sek(k1, k0):
        return math.log(tab[k1]['E'] / tab[k0]['E']) / math.log(tab[k1]['Q'] / tab[k0]['Q'])
    for k in ks:
        if k + 1 in tab and tab[k]['E'] is not None and tab[k + 1]['E'] is not None:
            tab[k]['p_FD'] = sek(k + 1, k)
    res = {'spec': g.get('spec'), 'dateien': g['dateien'], 'bereich': bereich, 'bereich_ohne_sauber_regel': bereich_alt,
           'tabelle': [tab[k] for k in ks]}
    if bereich:
        res['bereich_Q'] = [tab[bereich[0]]['Q'], tab[bereich[-1]]['Q']]
        res['bereich_Rg'] = [tab[bereich[0]]['Rg'], tab[bereich[-1]]['Rg']]
    res['periodenmittel'] = None
    for nper in (2, 1):
        sch = 8 * nper
        if len(bereich) > sch:
            kt = bereich[-1]
            res['periodenmittel'] = {'wert': sek(kt, kt - sch), 'perioden': nper, 'k_oben': kt, 'k_unten': kt - sch,
                                     'Q_oben': tab[kt]['Q'], 'Q_unten': tab[kt - sch]['Q']}
            break
    res['gleitend_1'] = [{'k_oben': k, 'p': sek(k, k - 8)} for k in bereich if k - 8 in bereich]
    res['gleitend_2'] = [{'k_oben': k, 'p': sek(k, k - 16)} for k in bereich if k - 16 in bereich]
    if len(bereich_alt) > 16:
        kt = bereich_alt[-1]
        res['periodenmittel_ohne_sauber_regel'] = sek(kt, kt - 16)
    return res


def lauf_auswertung(ordner):
    out = {}
    k = lade(os.path.join(ordner, 'kasten.json'))['ergebnis']
    out['MD0'] = aw_md0(k)
    kb = lade(os.path.join(ordner, 'kubisch.json'))['ergebnis']
    out['MD1'] = aw_md1(kb)
    # MD2: Waermeleitungsspur (Stufe 6 gewertet, 4 und 5 berichtet) und Beutel
    sp = {}
    for p in sorted(glob.glob(os.path.join(ordner, 's_st*.json'))):
        d = lade(p)
        s = int(d['graph']['spec'].split(':')[1])
        sp[s] = {'N': d['graph']['N'], 'bauprobe': d.get('bauprobe'), 'plateau_regel_bagdim': d.get('plateau'),
                 'fenster': periodenfenster(d['eigenwerte'], d['graph']['N'])}
    out['MD2_spur'] = sp
    bt = beutel_st(ordner)
    out['MD2_beutel'] = aw_beutel(bt) if bt['k'] else None
    ds6 = sp.get(6, {}).get('fenster') or {}
    ds_w = ds6.get('gewertet')
    pm = (out['MD2_beutel'] or {}).get('periodenmittel')
    p_w = pm['wert'] if pm else None
    t1 = w_ber(ds_w, DS_ST - 0.08, DS_ST + 0.08) if ds_w is not None else False
    t1_karte = w_ber(ds_w, 1.547 - 0.08, 1.547 + 0.08) if ds_w is not None else False
    t2 = (p_w is not None and abs(p_w - P_ST_KARTE) <= 0.03 + 1e-12 and abs(p_w - P_ST_KARTE) < abs(p_w - P_MINK_KARTE))
    out['MD2'] = {'urteil': 'eingetroffen' if (t1_karte and t2) else ('offen' if (ds_w is None or p_w is None) else 'nicht eingetroffen'),
                  'ds_periodenmittel': ds_w, 'ds_ok': t1_karte, 'ds_ok_mit_1_5474': t1, 'p': p_w, 'p_ok': bool(t2),
                  'p_perioden': pm['perioden'] if pm else None}
    # MD3 / MD4
    tk = {}
    for p in sorted(glob.glob(os.path.join(ordner, 'takt-*.json'))):
        for z in lade(p)['ergebnis']:
            tk[z['netz']] = z
    out['takt_uebersicht'] = {}
    for n, z in tk.items():
        row = {}
        for on, od in z['ops'].items():
            if 'uebersprungen' in od:
                row[on] = od
                continue
            row[on] = {gn: {kk: od[gn]['analyse'][kk] for kk in ('max_ds', 'sigma_max', 'P_bei_max', 'max_innen', 'stufe_da',
                                                                  'ds_end_zulaessig', 'min_ds_nach_max', 'ds_nach_max_immer_ueber_3',
                                                                  'N_ges', 'gitter')}
                       for gn in od}
        row['kontrolle_matrix'] = z['kontrolle_matrix']
        row['stern0'] = z['stern0']
        row['stern1_n_nicht_pos'] = z['stern1_n_nicht_pos']
        out['takt_uebersicht'][n] = row
    md3 = {}
    for n in ('V', 'C15', 'A15'):
        if n not in tk:
            md3[n] = {'ok': False, 'grund': 'fehlt'}
            continue
        od = tk[n]['ops'].get('takt_s0', {})
        if 'gewertet' not in od:
            od = tk[n]['ops']['takt']
            ersatz = True
        else:
            ersatz = False
        an = od['gewertet']['analyse']
        ok = bool(an['max_ds'] > 3.2 and an['max_innen'] and not an['stufe_da'])
        md3[n] = {'ok': ok, 'max_ds': an['max_ds'], 'max_innen': an['max_innen'], 'stufe_da': an['stufe_da'],
                  'stufen_zonen': an['stufen_zonen'], 'ersatz_ohne_s0': ersatz}
    out['MD3'] = {'urteil': 'eingetroffen' if all(v['ok'] for v in md3.values()) else 'nicht eingetroffen', 'netze': md3}
    gl = [tk[n] for n in sorted(tk) if n.startswith('glas-N512')]
    if gl and 'V' in tk:
        mv = md3['V']['max_ds']
        mg, quelle = [], []
        for z in gl:
            an = z['ops']['takt_s0']['gewertet']['analyse']
            if not an['max_innen']:
                an = z['ops']['takt_s0']['kontrolle']['analyse']
                quelle.append('k-Gitter 2^3 (Gamma-Maximum nicht im Inneren)')
            else:
                quelle.append('Gamma')
            mg.append(an['max_ds'])
        mittel = float(np.mean(mg))
        out['MD4'] = {'urteil': 'eingetroffen' if mittel <= mv - 0.2 + 1e-12 else 'nicht eingetroffen',
                      'max_V': mv, 'max_glas': mg, 'quelle': quelle, 'mittel_glas': mittel, 'abstand': mv - mittel,
                      'alle_vier_einzeln': bool(all(m <= mv - 0.2 for m in mg)), 'n_saaten': len(mg),
                      'max_glas_kontrolle_2hoch3': [z['ops']['takt_s0']['kontrolle']['analyse']['max_ds'] for z in gl]}
    else:
        out['MD4'] = {'urteil': 'offen'}
    return out


# ------------------------------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['kasten', 'kubisch', 'takt', 'auswertung'])
    ap.add_argument('--netze', default='V')
    ap.add_argument('--ordner', default='.')
    ap.add_argument('--rauch', action='store_true', help='kleine Einstellungen, nur Schluessel speichern')
    ap.add_argument('--klein', action='store_true', help='kleine Einstellungen, volle Ausgabe (Probelauf der Auswertung)')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)),
            'module_sha256': {m.__name__: sha(os.path.abspath(m.__file__)) for m in (tg, uk, tu, dn)},
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'kasten':
        erg = lauf_kasten(a.rauch or a.klein)
    elif a.modus == 'kubisch':
        erg = lauf_kubisch()
    elif a.modus == 'takt':
        erg = lauf_takt(a.netze.split(','), a.rauch or a.klein)
    else:
        erg = lauf_auswertung(a.ordner)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - T0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        res = {'info': info, 'schluessel': tg.nur_schluessel(erg), 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB']}
    schreibe(a.out, res)
    print('fertig', a.modus, a.netze if a.modus == 'takt' else '', 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
