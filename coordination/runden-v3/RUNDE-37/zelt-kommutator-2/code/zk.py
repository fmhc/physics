#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZELT-KOMMUTATOR-2 (fmhc-physics, Runde 49), Code-Agent fuer die Leitung claude-primary.

Erweitert die unveraenderte Kopie pt.py (PACHNER-TAKT-1, eingefroren, sha256 bc360991...) durch Import.
Modi:
  kb       Kombinatorik der Schichten AB und BA, Breitensuche nach kuerzesten Pachner-Folgen in der Region R,
           Geometrie-Pruefung aller kuerzesten Wege (Kandidaten der Schiebung, tau), Auswahl des kanonischen Weges.
  ki       isolierte Zuege (2-4/4-2 und 3-3) an sechs allgemeinen Punkten, gekruemmte und flache Randdaten.
  defekte  Teil A: Defekte je Zug auf dem kanonischen Weg (eine Variante, alle tau, eps, L/a), nichtlinear und linear.
  uhr      Teil B: unimodulare Uhr DeltaT = Summe V_sigma bei tau = 0 fuer AB und BA, dazu D (Vergleich PACHNER-TAKT-1).
"""
import argparse, json, sys, time, platform, os, resource, hashlib
from itertools import combinations
from collections import defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pt  # noqa: E402

N = 4
VAR = {'L': (0.3, 0.5), 'G': (0.4, 0.4)}
TAUS = [0.2, 0.1, 0.05, 0.025]
TAU_HAUPT = 0.1
KANDIDATEN = [('A', 1), ('A', -1), ('B', 1), ('B', -1)]
NULL = (0, 0, 0)
LAS = [4.0, 8.0, 16.0, 32.0]
EPSS = [1e-3, 1e-4]


# ================================================================================================= Bau
def bau(var, kipp=None, tau=0.0, ordnung='AB'):
    """Schicht wie pt.lauf_kommutator. kipp = ('A'|'B', s): A' bzw. B' raeumlich um tau*s*e_z verschoben."""
    NA, NB = VAR[var]
    nz = pt.Netz(N, 'klasse', 'C2')
    A = nz.idx[(N, N, N)]
    B = nz.idx[(N + 1, N + 1, N)]
    sig0 = set(nz.sigma)
    if ordnung == 'AB':
        a2 = nz.zelt(A, NA)
        b2 = nz.zelt(B, NB)
    else:
        b2 = nz.zelt(B, NB)
        a2 = nz.zelt(A, NA)
    if kipp is not None and tau != 0.0:
        w = a2 if kipp[0] == 'A' else b2
        nz.X[w] = nz.X[w] + np.array([0.0, 0.0, tau * kipp[1]])
    sigT = set(nz.sigma)
    simp = []
    for refs in nz.simp:
        for (v, s) in refs:
            assert tuple(s) == NULL, refs
        simp.append(frozenset(v for (v, s) in refs))
    return {'nz': nz, 'sig0': sig0, 'sigT': sigT, 'A': A, 'B': B, 'a2': a2, 'b2': b2, 'simp': simp}


def fuenfeck(sig0, A, B):
    kanten = []
    for key in sig0:
        vs = set(v for v, s in key)
        if A in vs and B in vs:
            kanten.append(tuple(sorted(vs - {A, B})))
    nb = defaultdict(list)
    for a, b in kanten:
        nb[a].append(b)
        nb[b].append(a)
    assert all(len(x) == 2 for x in nb.values()), nb
    start = min(nb)
    zyk = [start]
    prev, cur = start, min(nb[start])
    while cur != start:
        zyk.append(cur)
        a, b = nb[cur]
        prev, cur = cur, (a if b == prev else b)
    return zyk


def regionen(b):
    A, B, a2, b2 = b['A'], b['B'], b['a2'], b['b2']
    zyk = fuenfeck(b['sig0'], A, B)
    k = len(zyk)
    spalten = [(zyk[i], zyk[(i + 1) % k]) for i in range(k)]
    R0 = set()
    R5 = set()
    for c, d in spalten:
        R0 |= {frozenset((A, a2, B, c, d)), frozenset((a2, B, b2, c, d))}
        R5 |= {frozenset((A, B, b2, c, d)), frozenset((A, a2, b2, c, d))}
    AB = set(b['simp'])
    assert R0 <= AB, 'R0 nicht in AB'
    C = AB - R0
    return {'zyk': zyk, 'spalten': spalten, 'R0': frozenset(R0), 'R5': frozenset(R5), 'C': C}


def flaechen_von(S):
    tet, tri, kan = defaultdict(list), defaultdict(list), defaultdict(list)
    for s in S:
        ss = sorted(s)
        for f in combinations(ss, 4):
            tet[frozenset(f)].append(s)
        for f in combinations(ss, 3):
            tri[frozenset(f)].append(s)
        for f in combinations(ss, 2):
            kan[frozenset(f)].append(s)
    return tet, tri, kan


def zuege(S, Cf):
    """Alle 2-4-, 3-3- und 4-2-Zuege, deren Simplizes ganz in S (Region R) liegen."""
    Ctet, Ctri, Ckan = Cf
    tet, tri, kan = flaechen_von(S)
    out = []
    for tau, ss in tet.items():
        if len(ss) == 2 and tau not in Ctet:
            u = next(iter(ss[0] - tau))
            w = next(iter(ss[1] - tau))
            e = frozenset((u, w))
            if e in kan or e in Ckan:
                continue
            neu = [frozenset(f) | e for f in combinations(sorted(tau), 3)]
            out.append((('2-4', tuple(sorted(tau)), tuple(sorted(e))), frozenset((S - {ss[0], ss[1]}) | set(neu))))
    for t, ss in tri.items():
        if len(ss) == 3 and t not in Ctri:
            link = frozenset().union(*ss) - t
            if len(link) != 3 or link in tri or link in Ctri:
                continue
            neu = [link | frozenset(p) for p in combinations(sorted(t), 2)]
            out.append((('3-3', tuple(sorted(t)), tuple(sorted(link))), frozenset((S - set(ss)) | set(neu))))
    for e, ss in kan.items():
        if len(ss) == 4 and e not in Ckan:
            link = frozenset().union(*ss) - e
            if len(link) != 4 or link in tet or link in Ctet:
                continue
            u, w = sorted(e)
            neu = [link | {u}, link | {w}]
            out.append((('4-2', tuple(sorted(e)), tuple(sorted(link))), frozenset((S - set(ss)) | set(neu))))
    return out


def bfs(S0, Cf, tiefe):
    ebenen = [{S0: []}]
    gesehen = {S0: 0}
    for d in range(1, tiefe + 1):
        neu = {}
        for S in ebenen[-1]:
            for mv, S2 in zuege(S, Cf):
                if S2 in gesehen and gesehen[S2] < d:
                    continue
                neu.setdefault(S2, []).append(S)
                gesehen[S2] = d
        ebenen.append(neu)
    return ebenen


def pfade(ebenen, M, d):
    if d == 0:
        return [[M]]
    out = []
    for P in set(ebenen[d][M]):
        for p in pfade(ebenen, P, d - 1):
            out.append(p + [M])
    return out


def zug_zwischen(X, Y, Cf):
    for mv, S2 in zuege(X, Cf):
        if S2 == Y:
            return mv
    raise RuntimeError('kein Zug')


def positionen(b):
    nz = b['nz']
    vs = sorted(set().union(*b['simp']))
    return {v: nz.pos((v, NULL)) for v in vs}


def geo_pruefung(simplizes, P, ref_rand=None):
    tet = defaultdict(list)
    vrel = []
    for s in simplizes:
        vs = sorted(s)
        M = np.array([P[v] - P[vs[0]] for v in vs[1:]])
        V = np.linalg.det(M) / 24.0
        lmax = max(np.linalg.norm(P[a] - P[c]) for a, c in combinations(vs, 2))
        vrel.append(abs(V) / lmax ** 4)
        for f in combinations(vs, 4):
            apex = next(iter(s - frozenset(f)))
            M = np.array([P[x] - P[f[0]] for x in f[1:]] + [P[apex] - P[f[0]]])
            tet[f].append(float(np.sign(np.linalg.det(M))))
    innen_falsch = sum(1 for v in tet.values() if len(v) == 2 and v[0] * v[1] >= 0)
    mehrfach = sum(1 for v in tet.values() if len(v) > 2)
    rand = {f: v[0] for f, v in tet.items() if len(v) == 1}
    rand_falsch = None
    if ref_rand is not None:
        rand_falsch = sum(1 for f, sg in rand.items() if ref_rand.get(f) != sg) + len(set(ref_rand) ^ set(rand))
    ok = (min(vrel) > 1e-10) and innen_falsch == 0 and mehrfach == 0 and (rand_falsch in (None, 0))
    return {'vol_rel_min': float(min(vrel)), 'innen_falsch': innen_falsch, 'mehrfach': mehrfach,
            'rand_falsch': rand_falsch, 'geometrisch': bool(ok)}, rand


def zustand_liste(S):
    return sorted(tuple(sorted(s)) for s in S)


# ================================================================================================= Modus kb
def lauf_kb():
    t0 = time.time()
    out = {}
    bL = bau('L')
    reg = regionen(bL)
    A, B, a2, b2 = bL['A'], bL['B'], bL['a2'], bL['b2']
    C, R0, R5 = reg['C'], reg['R0'], reg['R5']
    # BA wie pt.lauf_kommutator gebaut, umbenannt in AB-Indizes
    bBA = bau('L', ordnung='BA')
    umb = {bBA['a2']: a2, bBA['b2']: b2}
    BA = set(frozenset(umb.get(v, v) for v in s) for s in bBA['simp'])
    AB = set(bL['simp'])
    out['kombinatorik'] = {
        'A': A, 'B': B, "A'": a2, "B'": b2, 'n_AB': len(AB), 'n_BA': len(BA),
        'AB_ohne_BA': len(AB - BA), 'BA_ohne_AB': len(BA - AB), 'gemeinsam': len(AB & BA),
        'AB_ohne_BA_gleich_R0': (AB - BA) == set(R0), 'BA_ohne_AB_gleich_R5': (BA - AB) == set(R5),
        'BA_gleich_C_plus_R5': BA == (C | set(R5)),
        'stern_A': sum(1 for key in bL['sig0'] if A in [v for v, s in key]),
        'stern_B': sum(1 for key in bL['sig0'] if B in [v for v, s in key]),
        'fuenfeck': reg['zyk'], 'k': len(reg['zyk']),
        'fuenfeck_raeumlich_rel_A': [[float(x) for x in (bL['nz'].X[c] - bL['nz'].X[A])] for c in reg['zyk']],
        'fuenfeck_klasse': [bL['nz'].kl[c] for c in reg['zyk']],
        'grad_ApB_in_AB': sum(1 for s in AB if a2 in s and B in s),
        'grad_ABp_in_BA': sum(1 for s in BA if A in s and b2 in s),
        'link_ApB': sorted(tuple(sorted(s - {a2, B})) for s in AB if a2 in s and B in s),
    }
    # G: gleiche Kombinatorik?
    bG = bau('G')
    out['kombinatorik']['G_gleiche_simplizes'] = set(bG['simp']) == AB
    # Breitensuche in R
    Cf = flaechen_von(C)
    Cf = (set(Cf[0]), set(Cf[1]), set(Cf[2]))
    tb = time.time()
    vor = bfs(R0, Cf, 3)
    rueck = bfs(R5, Cf, 2)
    treffer = {}
    for i in range(len(vor)):
        for j in range(len(rueck)):
            for M in vor[i]:
                if M in rueck[j]:
                    treffer.setdefault(i + j, []).append((i, j, M))
    laenge = min(treffer) if treffer else None
    out['bfs'] = {'zustaende_vor': [len(e) for e in vor], 'zustaende_rueck': [len(e) for e in rueck],
                  'laengen_mit_treffer': sorted(treffer), 'kuerzeste_laenge': laenge,
                  't_s': time.time() - tb}
    wege = set()
    if laenge is not None:
        for (i, j, M) in treffer[laenge]:
            for pv in pfade(vor, M, i):
                for pr in pfade(rueck, M, j):
                    wege.add(tuple(pv + pr[::-1][1:]))
    wl = []
    for w in wege:
        zg = [zug_zwischen(w[q], w[q + 1], Cf) for q in range(len(w) - 1)]
        wl.append((zg, w))
    wl.sort(key=lambda x: x[0])
    out['bfs']['n_kuerzeste'] = len(wl)
    out['bfs']['typen'] = sorted(set(tuple(z[0] for z in zg) for zg, w in wl))
    out['bfs']['jeder_mit_33'] = all(any(z[0] == '3-3' for z in zg) for zg, w in wl) if wl else None
    out['bfs']['zusammensetzung'] = sorted(set(tuple(sorted(z[0] for z in zg)) for zg, w in wl))
    # Geometrie
    zust = {}
    for zg, w in wl:
        for S in w:
            zust.setdefault(S, len(zust))
    geo = {}
    for kand in [None] + KANDIDATEN:
        for var in ('L', 'G'):
            for tau in ([0.0] if kand is None else TAUS):
                b = bau(var, kand, tau)
                P = positionen(b)
                r0, ref = geo_pruefung(list(C | set(R0)), P)
                gz = {}
                for S, zi in zust.items():
                    g, _ = geo_pruefung(list(C | set(S)), P, ref)
                    gz[zi] = g
                geom_wege = [q for q, (zg, w) in enumerate(wl) if all(gz[zust[S]]['geometrisch'] for S in w)]
                schl = '%s|%s|%g' % ('-' if kand is None else '%s%+d' % kand, var, tau)
                geo[schl] = {'AB': r0, 'BA': gz[zust[R5]] if R5 in zust else None,
                             'geometrische_wege': geom_wege,
                             'zwischen_geometrisch': sum(1 for S, zi in zust.items()
                                                         if S not in (R0, R5) and gz[zi]['geometrisch']),
                             'vol_rel_min_zwischen': min(gz[zi]['vol_rel_min'] for S, zi in zust.items()
                                                         if S not in (R0, R5)) if len(zust) > 2 else None}
    out['geometrie'] = geo
    # Auswahl
    auswahl = None
    for kand in KANDIDATEN:
        sets = [set(geo['%s%+d|%s|%g' % (kand[0], kand[1], var, tau)]['geometrische_wege'])
                for var in ('L', 'G') for tau in TAUS]
        gem = set.intersection(*sets)
        if gem:
            q = min(gem)
            zg, w = wl[q]
            auswahl = {'kandidat': list(kand), 'weg_index': q, 'zuege': [list(map(lambda x: list(x) if isinstance(x, tuple) else x, z)) for z in zg],
                       'zustaende': [zustand_liste(S) for S in w],
                       'je_variante_erster': {var: min(set.intersection(*[set(geo['%s%+d|%s|%g' % (kand[0], kand[1], var, tau)]['geometrische_wege']) for tau in TAUS]) or {None}, key=lambda x: -1 if x is None else x) for var in ('L', 'G')},
                       'geometrische_wege_haupt_L': geo['%s%+d|L|%g' % (kand[0], kand[1], TAU_HAUPT)]['geometrische_wege'],
                       'geometrische_wege_haupt_G': geo['%s%+d|G|%g' % (kand[0], kand[1], TAU_HAUPT)]['geometrische_wege']}
            break
    out['auswahl'] = auswahl
    out['C'] = zustand_liste(C)
    out['alle_wege'] = [{'zuege': [[z[0], list(z[1]), list(z[2])] for z in zg], 'zustaende': [zustand_liste(S) for S in w]}
                        for zg, w in wl]
    out['t_kb_s'] = time.time() - t0
    return out


# ================================================================================================= Schicht-Hilfen
def schicht(b, S_liste):
    simp = [[(v, NULL) for v in s] for s in S_liste]
    return pt.Schicht(b['nz'], b['sig0'], b['sigT'], simp=simp)


def bd_ordnung(sch):
    inv = {i: k for k, i in sch.ekey.items()}
    keys = sorted(inv[e] for e in sch.bd)
    return keys, np.array([sch.ekey[k] for k in keys])


def volumen(sch, l):
    X = pt.koord_aus_laengen(l[sch.egid])
    V = np.linalg.det(X[:, 1:, :] - X[:, :1, :]) / 24.0
    return float(V.sum()), float(V.min())


def loese_voll(sch, lbd, ordn):
    l, Sw, g, res, nit, phi = pt.loese(sch, lbd)
    T, vmin = volumen(sch, l)
    return {'p': g[ordn], 'S': Sw, 'res': res, 'nit': nit, 'T': T, 'vmin': vmin,
            'innen_fehl_max': float(np.abs(phi[~sch.tri_bd]).max()) if (~sch.tri_bd).any() else 0.0}


def loese_start(sch, lbd, maxit=40):
    """Wie pt.loese (kopiert), aber Start der Innenkanten bei lbd (Laengen aller Kanten aus derselben Vorschrift)
    statt bei den flachen Laengen. Rauchtest r2: Start bei flachen Innenlaengen macht duenne Q-Simplizes unrealisierbar."""
    l = lbd.copy()
    inn = sch.inn
    for it in range(maxit):
        Sw, g, X, phi = sch.bewerte(l)
        res = float(np.abs(g[inn]).max())
        if res < 1e-15:
            break
        geo = pt.geometrie(X)
        H = sch.hesse(geo)
        l[inn] += np.linalg.solve(H[np.ix_(inn, inn)], -g[inn])
    Sw, g, X, phi = sch.bewerte(l)
    return l, Sw, g, float(np.abs(g[inn]).max()), it + 1, phi


def loese_voll_start(sch, lbd, ordn):
    try:
        l, Sw, g, res, nit, phi = loese_start(sch, lbd)
        if not np.all(np.isfinite(g)):
            raise FloatingPointError('nicht endlich')
    except (np.linalg.LinAlgError, FloatingPointError, ValueError) as e:
        return {'fehler': type(e).__name__ + ': ' + str(e)}
    T, vmin = volumen(sch, l)
    return {'p': g[ordn], 'S': Sw, 'res': res, 'nit': nit, 'T': T, 'vmin': vmin,
            'innen_fehl_max': float(np.abs(phi[~sch.tri_bd]).max()) if (~sch.tri_bd).any() else 0.0}


def w_flach(sch, La):
    """Ableitung von pt.flach_laengen nach eps bei eps = 0 (Formel von xi aus pt.flach_laengen kopiert)."""
    Lc = La / np.sqrt(2.0)
    kv = 2 * np.pi / Lc * np.array([1.0, 0.3, 0.2])

    def xi(P):
        ph = P[:, :3] @ kv
        return np.stack([0.7 * np.sin(ph), 0.4 * np.cos(ph), 0.3 * np.sin(2 * ph), 0.5 * np.cos(ph + 0.4 * P[:, 3])], 1)
    p1 = sch.emid - 0.5 * sch.evec
    p2 = sch.emid + 0.5 * sch.evec
    return np.sum(sch.evec * (xi(p2) - xi(p1)), axis=1) / sch.lflat


def schur(sch, ordn):
    H = sch.hesse(pt.geometrie(sch.Xs))
    ii = sch.inn
    Hii = H[np.ix_(ii, ii)]
    Q = H[np.ix_(ordn, ordn)] - H[np.ix_(ordn, ii)] @ np.linalg.solve(Hii, H[np.ix_(ii, ordn)])
    return Q, float(np.linalg.cond(Hii))


# ================================================================================================= Modus defekte
def lauf_defekte(var, kb, taus, epss, las, alle_wege=True):
    aw = kb['auswahl']
    kand = tuple(aw['kandidat'])
    C = [tuple(s) for s in kb['C']]
    weg = [[tuple(s) for s in Z] for Z in aw['zustaende']]
    typen = [z[0] for z in aw['zuege']]
    out = {'variante': var, 'kandidat': list(kand), 'zuege': aw['zuege'], 'typen': typen, 'tau': []}
    for tau in taus:
        tt = time.time()
        b = bau(var, kand, tau)
        xA = b['nz'].X[b['A']]
        schs = [schicht(b, C + Z) for Z in weg]
        keys0, ordn0 = bd_ordnung(schs[0])
        ordns = []
        for s in schs:
            k, o = bd_ordnung(s)
            assert k == keys0
            ordns.append(o)
        r = {'tau': tau, 'n_inn': [len(s.inn) for s in schs], 'n_simp': [len(s.simp) for s in schs],
             'n_bd': len(keys0)}
        geo_flach = []
        for s in schs:
            geo = pt.geometrie(s.Xs)
            Sw, g, X, phi = s.bewerte(s.lflat)
            geo_flach.append({'vol_rel_min': float(geo['vol_rel'].min()), 'schlaefli': geo['schlaefli'],
                              'M_sym': geo['M_sym'],
                              'innen_fehl_flach': float(np.abs(phi[~s.tri_bd]).max()) if (~s.tri_bd).any() else 0.0,
                              'grad_innen_flach': float(np.abs(g[s.inn]).max())})
        r['flach_geometrie'] = geo_flach
        # linear
        Qs, conds = [], []
        for s, o in zip(schs, ordns):
            Q, c = schur(s, o)
            Qs.append(Q)
            conds.append(c)
        r['Hii_cond'] = conds
        lin = []
        for La in las:
            _, w = pt.welle_laengen(schs[0], 1.0, La, xA)
            wv = w[ordns[0]]
            dl = [float(np.linalg.norm((Qs[j] - Qs[j - 1]) @ wv)) for j in range(1, len(Qs))]
            lin.append({'La': La, 'd_lin': dl, 'D_lin': float(np.linalg.norm((Qs[-1] - Qs[0]) @ wv))})
        r['linear'] = lin
        wf = w_flach(schs[0], 4.0)[ordns[0]]
        pf = schs[0].bewerte(schs[0].lflat)[1][ordns[0]]
        r['linear_flach'] = {'d_lin': [float(np.linalg.norm((Qs[j] - Qs[j - 1]) @ wf)) for j in range(1, len(Qs))],
                             'D_lin': float(np.linalg.norm((Qs[-1] - Qs[0]) @ wf)), 'w_norm': float(np.linalg.norm(wf)),
                             'p0_norm': float(np.linalg.norm(pf))}

        def fall(eps, La, art):
            res = []
            for s, o in zip(schs, ordns):
                if art == 'welle':
                    lbd, _ = pt.welle_laengen(s, eps, La, xA)
                else:
                    lbd = pt.flach_laengen(s, eps, La)
                res.append(loese_voll_start(s, lbd, o))
            fehler = [x.get('fehler') for x in res]
            if any(f is not None for f in fehler):
                o = {'eps': eps, 'La': La, 'art': art, 'fehler': fehler}
                if fehler[0] is None and fehler[-1] is None:
                    o['D'] = float(np.linalg.norm(res[-1]['p'] - res[0]['p']))
                    o['p_norm'] = float(np.linalg.norm(res[0]['p']))
                    o['res_enden'] = [res[0]['res'], res[-1]['res']]
                return o
            p = [x['p'] for x in res]
            d = [float(np.linalg.norm(p[j] - p[j - 1])) for j in range(1, len(p))]
            D = float(np.linalg.norm(p[-1] - p[0]))
            tele = float(np.linalg.norm(sum(p[j] - p[j - 1] for j in range(1, len(p))) - (p[-1] - p[0])))
            return {'eps': eps, 'La': La, 'art': art, 'd': d, 'D': D, 'summe_d': float(sum(d)),
                    'p_norm': float(np.linalg.norm(p[0])), 'teleskop': tele,
                    'S': [x['S'] for x in res], 'dS': [res[j]['S'] - res[j - 1]['S'] for j in range(1, len(res))],
                    'T': [x['T'] for x in res], 'dT': [res[j]['T'] - res[j - 1]['T'] for j in range(1, len(res))],
                    'res': [x['res'] for x in res], 'nit': [x['nit'] for x in res],
                    'vmin': [x['vmin'] for x in res], 'innen_fehl_max': [x['innen_fehl_max'] for x in res]}
        r['welle'] = [fall(e, La, 'welle') for e in epss for La in las]
        r['flach'] = [fall(e, 4.0, 'flach') for e in (1e-3, 1e-4)]
        r['null'] = fall(0.0, 4.0, 'welle')
        r['t_s'] = time.time() - tt
        out['tau'].append(r)
        print('defekte %s tau=%g fertig nach %.1f s' % (var, tau, time.time() - tt), flush=True)
    # alle geometrischen kuerzesten Wege beim Haupt-tau (beschreibend)
    if alle_wege and TAU_HAUPT in taus:
        idx = kb['auswahl']['geometrische_wege_haupt_' + var]
        b = bau(var, kand, TAU_HAUPT)
        xA = b['nz'].X[b['A']]
        cache = {}
        aw_out = []
        for q in idx:
            Zs = [tuple(tuple(s) for s in Z) for Z in kb['alle_wege'][q]['zustaende']]
            ps = []
            for Z in Zs:
                if Z not in cache:
                    s = schicht(b, C + list(Z))
                    k, o = bd_ordnung(s)
                    _, w = pt.welle_laengen(s, 1.0, 4.0, xA)
                    Q, _c = schur(s, o)
                    cache[Z] = Q @ w[o]
                ps.append(cache[Z])
            d = [float(np.linalg.norm(ps[j] - ps[j - 1])) for j in range(1, len(ps))]
            aw_out.append({'weg': q, 'typen': [z[0] for z in kb['alle_wege'][q]['zuege']], 'd_lin': d,
                           'summe_d_lin': float(sum(d)), 'D_lin': float(np.linalg.norm(ps[-1] - ps[0]))})
        out['alle_geometrischen_wege_haupt'] = aw_out
    return out


# ================================================================================================= Modus uhr
def lauf_uhr(var, epss, las):
    out = {'variante': var}
    bA = bau(var)
    reg = regionen(bA)
    C = [tuple(sorted(s)) for s in reg['C']]
    T0 = [tuple(sorted(s)) for s in reg['R0']]
    T5 = [tuple(sorted(s)) for s in reg['R5']]
    bB = bau(var, ordnung='BA')
    sA = schicht(bA, C + T0)
    s5 = schicht(bA, C + T5)
    sB = pt.Schicht(bB['nz'], bB['sig0'], bB['sigT'])   # wie pt.lauf_kommutator
    # Randkanten nach Etikett (orig, gen) ordnen
    def etik_ordnung(nz, sch):
        lab = [pt.etikett(nz, sch, e) for e in sch.bd]
        o = np.argsort([str(x) for x in lab])
        return np.array(sch.bd)[o], sorted(str(x) for x in lab)
    oA, labA = etik_ordnung(bA['nz'], sA)
    o5, lab5 = etik_ordnung(bA['nz'], s5)
    oB, labB = etik_ordnung(bB['nz'], sB)
    assert labA == lab5 == labB
    xA = bA['nz'].X[bA['A']]
    out['T_analytisch'] = {'L': 5.0 / 24.0, 'G': 0.2}[var]
    out['n_simp'] = [len(sA.simp), len(s5.simp), len(sB.simp)]

    def fall(eps, La, art):
        r = {}
        for nm, s, o in (('AB', sA, oA), ('T5', s5, o5), ('BApt', sB, oB)):
            if art == 'welle':
                lbd, _ = pt.welle_laengen(s, eps, La, xA)
            else:
                lbd = pt.flach_laengen(s, eps, La)
            r[nm] = loese_voll(s, lbd, o)
        TA, T5_, TB = r['AB']['T'], r['T5']['T'], r['BApt']['T']
        return {'eps': eps, 'La': La, 'art': art, 'T_AB': TA, 'T_BA': T5_, 'T_BApt': TB,
                'D_T': abs(TA - T5_) / TA, 'D_T_pt': abs(TA - TB) / TA,
                'D': float(np.linalg.norm(r['AB']['p'] - r['T5']['p'])),
                'D_pt': float(np.linalg.norm(r['AB']['p'] - r['BApt']['p'])),
                'p_T5_gegen_pt': float(np.linalg.norm(r['T5']['p'] - r['BApt']['p'])),
                'p_norm': float(np.linalg.norm(r['AB']['p'])),
                'res': [r[x]['res'] for x in ('AB', 'T5', 'BApt')], 'vmin': [r[x]['vmin'] for x in ('AB', 'T5', 'BApt')]}
    out['welle'] = [fall(e, La, 'welle') for e in epss for La in las]
    out['null'] = [fall(0.0, La, 'welle') for La in las]
    out['flach'] = [fall(e, 4.0, 'flach') for e in (1e-3, 3e-2)]
    return out


# ================================================================================================= Modus ki
class GK(pt.Schicht):
    """Allgemeiner Komplex: Punkte P (n x 4), Simplizes als 5-Tupel, Innenkanten explizit."""
    def __init__(self, P, simp, innen):
        self.simp = [tuple(s) for s in simp]
        S = len(self.simp)
        self.ekey, self.tkey = {}, {}
        self.egid = np.zeros((S, 10), int)
        self.tgid = np.zeros((S, 10), int)
        for si, s in enumerate(self.simp):
            for i, (a, c) in enumerate(pt.PAARE5):
                self.egid[si, i] = self.ekey.setdefault(tuple(sorted((s[a], s[c]))), len(self.ekey))
            for i, tr in enumerate(pt.DREI5):
                self.tgid[si, i] = self.tkey.setdefault(tuple(sorted(s[x] for x in tr)), len(self.tkey))
        self.NE, self.NT = len(self.ekey), len(self.tkey)
        tc = defaultdict(int)
        for s in self.simp:
            for f in combinations(sorted(s), 4):
                tc[f] += 1
        bdtri = set()
        for f, c in tc.items():
            if c == 1:
                for t in combinations(f, 3):
                    bdtri.add(t)
        self.tri_bd = np.zeros(self.NT, bool)
        for k, i in self.tkey.items():
            self.tri_bd[i] = k in bdtri
        self.inn = sorted(self.ekey[tuple(sorted(e))] for e in innen)
        self.bd = sorted(set(range(self.NE)) - set(self.inn))
        self.tri_edges = np.zeros((self.NT, 3), int)
        for si in range(S):
            for k in range(10):
                self.tri_edges[self.tgid[si, k]] = self.egid[si, pt.DREI_KANTEN[k]]
        self.Xs = np.array([[P[v] for v in s] for s in self.simp])
        self.evec = np.zeros((self.NE, 4))
        for k, i in self.ekey.items():
            self.evec[i] = P[k[1]] - P[k[0]]
        self.lflat = np.linalg.norm(self.evec, axis=1)


def gk_impulse(gk, lbd_dict):
    lbd = np.array([lbd_dict[k] for k in sorted(gk.ekey, key=gk.ekey.get)])
    keys = sorted(k for k, i in gk.ekey.items() if i in set(gk.bd))
    o = np.array([gk.ekey[k] for k in keys])
    if gk.inn:
        l, Sw, g, res, nit, phi = pt.loese(gk, lbd)
    else:
        Sw, g, X, phi = gk.bewerte(lbd)
        res, nit = 0.0, 0
    return keys, g[o], Sw, res


def lauf_ki():
    rng = np.random.default_rng(11)
    out = {}
    # 2-4 / 4-2
    tet = 0.5 * np.array([[1, 1, 1, 0], [1, -1, -1, 0], [-1, 1, -1, 0], [-1, -1, 1, 0]], float)
    tet = tet + 0.03 * rng.normal(size=tet.shape) * np.array([1, 1, 1, 0])
    P = np.vstack([tet, [0.05, -0.03, 0.02, 0.6], [-0.04, 0.02, 0.03, -0.5]])
    zwei = [(0, 1, 2, 3, 4), (0, 1, 2, 3, 5)]
    vier = [(4, 5) + tr for tr in combinations(range(4), 3)]
    alle = [tuple(sorted(e)) for e in combinations(range(6), 2)]
    r24 = []
    for art, eps in (('gekruemmt', 1e-3), ('gekruemmt', 1e-2), ('flach', 1e-2)):
        if art == 'gekruemmt':
            rr = rng.normal(size=len(alle))
            lmap = {e: float(np.linalg.norm(P[e[1]] - P[e[0]]) * (1 + eps * x)) for e, x in zip(alle, rr)}
        else:
            Pv = P + eps * rng.normal(size=P.shape)
            lmap = {e: float(np.linalg.norm(Pv[e[1]] - Pv[e[0]])) for e in alle}
        g2 = GK(P, zwei, [])
        g4 = GK(P, vier, [(4, 5)])
        k2, p2, S2, _ = gk_impulse(g2, lmap)
        k4, p4, S4, res4 = gk_impulse(g4, lmap)
        assert k2 == k4
        r24.append({'art': art, 'eps': eps, 'defekt_rel': float(np.linalg.norm(p4 - p2) / np.linalg.norm(p2)),
                    'dS': abs(S4 - S2), 'newton_rest': res4,
                    'vol_rel_min': [float(pt.geometrie(g.Xs)['vol_rel'].min()) for g in (g2, g4)]})
    out['zug_24'] = r24
    # 3-3
    t = np.array([[1, 0, 0, 0], [-0.5, 0.866, 0, 0], [-0.5, -0.866, 0, 0]], float)
    tp = np.array([[0, 0, 1, 0], [0, 0, -0.5, 0.866], [0, 0, -0.5, -0.866]], float)
    P3 = np.vstack([t, tp]) + 0.05 * rng.normal(size=(6, 4))
    vor = [(0, 1, 2) + pr for pr in combinations((3, 4, 5), 2)]
    nach = [(3, 4, 5) + pr for pr in combinations((0, 1, 2), 2)]
    r33 = []
    for art, eps in (('gekruemmt', 1e-3), ('gekruemmt', 1e-2), ('flach', 1e-2)):
        if art == 'gekruemmt':
            rr = rng.normal(size=len(alle))
            lmap = {e: float(np.linalg.norm(P3[e[1]] - P3[e[0]]) * (1 + eps * x)) for e, x in zip(alle, rr)}
        else:
            Pv = P3 + eps * rng.normal(size=P3.shape)
            lmap = {e: float(np.linalg.norm(Pv[e[1]] - Pv[e[0]])) for e in alle}
        gv = GK(P3, vor, [])
        gn = GK(P3, nach, [])
        kv, pv, Sv, _ = gk_impulse(gv, lmap)
        kn, pn, Sn, _ = gk_impulse(gn, lmap)
        assert kv == kn
        r33.append({'art': art, 'eps': eps, 'defekt_rel': float(np.linalg.norm(pn - pv) / np.linalg.norm(pv)),
                    'dS': abs(Sn - Sv),
                    'vol_rel_min': [float(pt.geometrie(g.Xs)['vol_rel'].min()) for g in (gv, gn)],
                    'innen_dreieck': [[k for k, i in g.tkey.items() if not g.tri_bd[i]] for g in (gv, gn)]})
    out['zug_33'] = r33
    # Geometrie der isolierten Konfigurationen (Seitenprobe)
    Pd = {i: P[i] for i in range(6)}
    out['geo_24'] = [geo_pruefung([frozenset(s) for s in zwei], Pd)[0], geo_pruefung([frozenset(s) for s in vier], Pd)[0]]
    Pd3 = {i: P3[i] for i in range(6)}
    out['geo_33'] = [geo_pruefung([frozenset(s) for s in vor], Pd3)[0], geo_pruefung([frozenset(s) for s in nach], Pd3)[0]]
    return out


# ================================================================================================= main
def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['kb', 'ki', 'defekte', 'uhr'])
    ap.add_argument('--variante', default='L')
    ap.add_argument('--kb', default=None)
    ap.add_argument('--tau', default=','.join(str(x) for x in TAUS))
    ap.add_argument('--eps', default=','.join(str(x) for x in EPSS))
    ap.add_argument('--La', default=','.join(str(x) for x in LAS))
    ap.add_argument('--alle_wege', type=int, default=1)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    here = os.path.dirname(os.path.abspath(__file__))
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'pt_sha256': sha(os.path.join(here, 'pt.py'))}
    res = {'info': info}
    taus = [float(x) for x in a.tau.split(',')]
    epss = [float(x) for x in a.eps.split(',')]
    las = [float(x) for x in a.La.split(',')]
    if a.modus == 'kb':
        res['kb'] = lauf_kb()
    elif a.modus == 'ki':
        res['ki'] = lauf_ki()
    elif a.modus == 'defekte':
        with open(a.kb) as f:
            kb = json.load(f)
        info['kb_sha256'] = sha(a.kb)
        res['defekte'] = lauf_defekte(a.variante, kb['kb'], taus, epss, las, bool(a.alle_wege))
    else:
        res['uhr'] = {v: lauf_uhr(v, epss, las) for v in a.variante.split(',')}
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else (sorted(o) if isinstance(o, (set, frozenset)) else str(o)))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
