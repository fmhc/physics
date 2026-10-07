#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KRUEMMUNGS-SANDHAUFEN-2D-1 (Runde 48, Finns Idee): Kruemmungs-Sandhaufen auf Dreiecksflaechen, BTW-Eichung, Auswertung.

Modell (KARTE.md): Kruemmungsladung q_v = 6 - c(v). Eine innere Ecke mit |q_v| >= 2 kippt:
  q_v >= 2: Flip einer Ringkante (u,w) -> (v,z), v gewinnt eine Kante;
  q_v <= -2: Flip einer Kante (v,x) -> (c,d), v verliert eine Kante.
Zulaessig: kein Grad < 3, keine Doppelkante. Antrieb: ein zufaelliger zulaessiger Flip einer inneren Kante je Schritt,
die Lawine laeuft vor dem naechsten Antrieb zu Ende. Scheibe: Randecken kippen nie (Senke). Kugel: keine Senke.
Arme: Z (Reihenfolge innerhalb einer Welle zufaellig, Flip gleichverteilt unter den zulaessigen),
      D (Reihenfolge aufsteigende Eckennummer, Flip = zulaessiger Flip mit kleinstem Kantenschluessel).
Regeln und Schwellen: PLAN.md (eingefroren).

Aufruf nur ueber kleintest.sh auf der .69:
  python ksh.py lauf --geo kugel --arm Z --N 500,2000,8000 --budget 50,90,300 --seed 11 --out lauf/kugel-Z [--r 0] [--rauch]
  python ksh.py btw --N 500,2000,8000 --budget 40,80,300 --seed 16 --out lauf/btw [--rauch]
  python ksh.py aus --ein lauf/kugel-Z.json lauf/kugel-D.json ... --out aus/urteile.json --bild aus [--rauch]
"""
import argparse, json, sys, time, os, math, random, hashlib, platform, resource

import numpy as np

SMIN = 2            # untere Fenstergrenze aller Fits (PLAN 6)
CAPF = 50           # Abbruch einer Lawine bei s >= CAPF * N (PLAN 4)
RELAXF = 100        # Abbruch der Anfangsrelaxation bei RELAXF * N Flips
EINF = 10           # Einschwingen: EINF * N Schritte (PLAN 5)
EIN_ANTEIL = 0.4    # hoechstens dieser Anteil des Fallbudgets fuer das Einschwingen
MMAX = 300000       # hoechstens so viele Messschritte je Fall
VOLLPRUEF = 2000    # volle Strukturpruefung alle VOLLPRUEF Mess- bzw. Einschwingschritte
REIHE = 1000        # Zeitreihe alle REIHE Schritte
BTW_EINF = 2        # BTW-Einschwingen: BTW_EINF * N Koerner nach dem Start aus der hoechsten stabilen Belegung
M64 = (1 << 64) - 1


def code_sha():
    with open(os.path.abspath(__file__), 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def h64(x):
    x = (x + 0x9E3779B97F4A7C15) & M64
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & M64
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & M64
    return x ^ (x >> 31)


# ---------------------------------------------------------------- Netze
def netz_kugel(N, seed):
    from scipy.spatial import ConvexHull
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(N, 3))
    x /= np.linalg.norm(x, axis=1)[:, None]
    h = ConvexHull(x)
    tris = [tuple(int(t) for t in s) for s in h.simplices]
    used = set(v for t in tris for v in t)
    if len(used) != N or len(tris) != 2 * N - 4:
        raise RuntimeError('Kugelnetz unvollstaendig: %d Ecken, %d Dreiecke' % (len(used), len(tris)))
    return tris, [False] * N, {'bau': 'konvexe Huelle von N gleichverteilten Punkten auf S^2 (spharisches Delaunay)',
                               'saat': seed, 'N_rand': 0, 'F': len(tris)}


def netz_scheibe(N, seed):
    from scipy.spatial import Delaunay
    nb = int(round(2.0 * math.sqrt(math.pi * N)))
    ni = N - nb
    for versuch in range(20):
        rng = np.random.default_rng(seed + 7919 * versuch)
        phi = 2.0 * math.pi * np.arange(nb) / nb
        xb = np.c_[np.cos(phi), np.sin(phi)]
        hb = 2.0 * math.pi / nb
        r = (1.0 - 0.5 * hb) * np.sqrt(rng.random(ni))
        t = 2.0 * math.pi * rng.random(ni)
        x = np.r_[xb, np.c_[r * np.cos(t), r * np.sin(t)]]
        d = Delaunay(x)
        tris = [tuple(int(v) for v in s) for s in d.simplices]
        cnt = {}
        for (a, b, c) in tris:
            for (p, q) in ((a, b), (b, c), (c, a)):
                k = (p, q) if p < q else (q, p)
                cnt[k] = cnt.get(k, 0) + 1
        rand_k = set(k for k, v in cnt.items() if v == 1)
        soll = set(((i, (i + 1) % nb) if i < (i + 1) % nb else ((i + 1) % nb, i)) for i in range(nb))
        used = set(v for t in tris for v in t)
        deg = [0] * N
        for (p, q) in cnt:
            deg[p] += 1
            deg[q] += 1
        if rand_k == soll and len(used) == N and min(deg) >= 3 and max(cnt.values()) <= 2:
            return tris, [i < nb for i in range(N)], {
                'bau': 'Delaunay: N_rand Punkte gleichabstaendig auf dem Einheitskreis, N - N_rand gleichverteilt '
                       'im Kreis vom Radius 1 - h/2', 'saat': seed + 7919 * versuch, 'versuch': versuch,
                'N_rand': nb, 'F': len(tris)}
    raise RuntimeError('Scheibennetz nach 20 Versuchen nicht gueltig')


def baue(tris, n):
    adj = [set() for _ in range(n)]
    opp = {}
    for (a, b, c) in tris:
        for (x, y, z) in ((a, b, c), (b, c, a), (c, a, b)):
            k = x * n + y if x < y else y * n + x
            adj[x].add(y)
            adj[y].add(x)
            l = opp.get(k)
            if l is None:
                opp[k] = [z]
            else:
                l.append(z)
    for k, l in opp.items():
        if len(l) == 1:
            l.append(-1)
        if len(l) != 2:
            raise RuntimeError('Kante mit %d Dreiecken' % len(l))
    deg = [len(s) for s in adj]
    return adj, opp, deg


def vollpruefung(n, adj, opp, deg, rand, chi_soll, E0):
    """Unabhaengige Strukturpruefung: Grade, Kantenzahl, Dreiecke, Euler, Ladungssumme, Sterne (Kreis bzw. Weg)."""
    fehler = []
    for v in range(n):
        if deg[v] != len(adj[v]):
            fehler.append('grad %d' % v)
            break
    if len(opp) != E0:
        fehler.append('kantenzahl %d statt %d' % (len(opp), E0))
    if sum(len(s) for s in adj) != 2 * len(opp):
        fehler.append('adj-opp')
    nt = 0
    for k, (c, d) in opp.items():
        a, b = divmod(k, n)
        if a >= b or b not in adj[a] or a == b:
            fehler.append('schluessel %d' % k)
            break
        for z in (c, d):
            if z >= 0:
                nt += 1
                if z not in adj[a] or z not in adj[b] or z == a or z == b:
                    fehler.append('apex %d' % k)
                    break
    if nt % 3:
        fehler.append('dreiecke')
    F = nt // 3
    chi = n - len(opp) + F
    if chi != chi_soll:
        fehler.append('euler %d' % chi)
    if min(deg) < 3:
        fehler.append('grad<3')
    qs = sum((4 if rand[v] else 6) - deg[v] for v in range(n))
    if qs != 6 * chi_soll:
        fehler.append('ladungssumme %d' % qs)
    for v in range(n):
        nb = adj[v]
        ends = 0
        ok = True
        for u in nb:
            c, d = opp[v * n + u if v < u else u * n + v]
            m = 0
            for z in (c, d):
                if z >= 0:
                    m += 1
                    if z not in nb:
                        ok = False
            if m == 1:
                ends += 1
        if not ok:
            fehler.append('stern %d' % v)
            break
        if (rand[v] and ends != 2) or ((not rand[v]) and ends != 0):
            fehler.append('sternrand %d' % v)
            break
        start = next(iter(nb))
        seen = {start}
        stack = [start]
        while stack:
            u = stack.pop()
            for z in opp[v * n + u if v < u else u * n + v]:
                if z >= 0 and z not in seen:
                    seen.add(z)
                    stack.append(z)
        if len(seen) != len(nb):
            fehler.append('ring %d' % v)
            break
    return fehler


# ---------------------------------------------------------------- Kruemmungs-Sandhaufen
def simuliere(geo, arm, N, budget, seed, r=0.0, rauch=False):
    t_case = time.time()
    if geo == 'kugel':
        tris, rand, info = netz_kugel(N, 1000 + N)
        chi = 2
    else:
        tris, rand, info = netz_scheibe(N, 2000 + N)
        chi = 1
    n = N
    adj, opp, deg = baue(tris, n)
    inner = [not b for b in rand]
    E0 = len(opp)
    S0 = sum(deg)
    voll = []
    f = vollpruefung(n, adj, opp, deg, rand, chi, E0)
    voll.append({'phase': 'start', 'fehler': f})
    grad_start = {}
    for v in range(n):
        if inner[v]:
            grad_start[deg[v]] = grad_start.get(deg[v], 0) + 1
    elist = [k for k, l in opp.items() if l[0] >= 0 and l[1] >= 0]
    epos = {k: i for i, k in enumerate(elist)}
    ne = len(elist)
    rng = random.Random(seed * 1000003 + N * 7 + (1 if arm == 'D' else 0) + int(round(r * 1e6)) * 13)
    rnd = rng.random
    det = (arm == 'D')
    cap = CAPF * N
    unst = set(v for v in range(n) if inner[v] and (deg[v] <= 4 or deg[v] >= 8))
    zh = 0
    if det:
        for k in opp:
            zh ^= h64(k)
    verletz = {'summe': 0, 'grad': 0, 'kanten': 0, 'doppel': 0}
    zaehl = {'extra_antrieb': 0, 'blockiert_versuche': 0, 'pruef_schritte': 0, 'antrieb_fehlversuche': 0}

    def flip(k, a, b, c, d):
        nonlocal zh
        k2 = c * n + d if c < d else d * n + c
        if k2 in opp:
            verletz['doppel'] += 1
            raise RuntimeError('Doppelkante bei Flip')
        del opp[k]
        opp[k2] = [a, b]
        l = opp[a * n + c if a < c else c * n + a]
        l[0 if l[0] == b else 1] = d
        l = opp[b * n + c if b < c else c * n + b]
        l[0 if l[0] == a else 1] = d
        l = opp[a * n + d if a < d else d * n + a]
        l[0 if l[0] == b else 1] = c
        l = opp[b * n + d if b < d else d * n + b]
        l[0 if l[0] == a else 1] = c
        adj[a].discard(b)
        adj[b].discard(a)
        adj[c].add(d)
        adj[d].add(c)
        deg[a] -= 1
        deg[b] -= 1
        deg[c] += 1
        deg[d] += 1
        i = epos.pop(k)
        elist[i] = k2
        epos[k2] = i
        if det:
            zh ^= h64(k) ^ h64(k2)
        for x in (a, b, c, d):
            if inner[x]:
                g = deg[x]
                if g <= 4 or g >= 8:
                    unst.add(x)
                else:
                    unst.discard(x)

    def antrieb():
        for _ in range(100000):
            k = elist[int(rnd() * ne)]
            c, d = opp[k]
            a, b = divmod(k, n)
            if deg[a] >= 4 and deg[b] >= 4 and d not in adj[c]:
                flip(k, a, b, c, d)
                return
            zaehl['antrieb_fehlversuche'] += 1
        raise RuntimeError('kein zulaessiger Antriebsflip')

    def kand_plus(v):
        av = adj[v]
        res = []
        seen = set()
        for u in av:
            for w in opp[v * n + u if v < u else u * n + v]:
                if w < 0:
                    continue
                k = u * n + w if u < w else w * n + u
                if k in seen:
                    continue
                seen.add(k)
                c, d = opp[k]
                z = d if c == v else c
                if z < 0:
                    continue
                if deg[u] >= 4 and deg[w] >= 4 and z not in av:
                    res.append((k, u, w, v, z))
        return res

    def kand_minus(v):
        res = []
        for x in adj[v]:
            k = v * n + x if v < x else x * n + v
            c, d = opp[k]
            if c < 0 or d < 0:
                continue
            if deg[x] >= 4 and d not in adj[c]:
                res.append((k, v, x, c, d))
        return res

    def lawine(cap_s):
        s = 0
        T = 0
        area = set()
        status = 0
        hs = set() if det else None
        if det:
            hs.add(zh)
        while unst:
            welle = list(unst)
            if det:
                welle.sort()
            else:
                rng.shuffle(welle)
            nf = 0
            for v in welle:
                g = deg[v]
                if 4 < g < 8:
                    continue
                res = kand_plus(v) if g <= 4 else kand_minus(v)
                if not res:
                    zaehl['blockiert_versuche'] += 1
                    continue
                ch = min(res) if det else res[int(rnd() * len(res))]
                flip(*ch)
                s += 1
                nf += 1
                area.add(v)
                if r > 0.0 and rnd() < r:
                    antrieb()
                    zaehl['extra_antrieb'] += 1
                if s >= cap_s:
                    break
            if nf == 0:
                status = 1
                break
            T += 1
            if s >= cap_s:
                status = 2
                break
            if det:
                if zh in hs:
                    status = 3
                    break
                hs.add(zh)
        return s, T, len(area), status

    kugel = (geo == 'kugel')

    def pruef_schritt():
        zaehl['pruef_schritte'] += 1
        sd = sum(deg)
        if kugel:
            if 6 * n - sd != 12:
                verletz['summe'] += 1
        elif sd != S0:
            verletz['summe'] += 1
        if min(deg) < 3:
            verletz['grad'] += 1
        if len(opp) != E0:
            verletz['kanten'] += 1

    def zustand():
        nd = 0
        q2 = 0
        ni = 0
        for v in range(n):
            if inner[v]:
                q = 6 - deg[v]
                ni += 1
                if q:
                    nd += 1
                    q2 += q * q
        rd = [deg[v] for v in range(n) if rand[v]]
        return [nd / ni, q2 / ni, len(unst), (sum(rd) / len(rd)) if rd else None, max(rd) if rd else None,
                min(deg), max(deg)]

    # Anfangsrelaxation (nicht gemessen)
    s0, T0, A0, st0 = lawine(RELAXF * N)
    pruef_schritt()
    relax = {'s': s0, 'T': T0, 'A': A0, 'status': st0, 'instabil_danach': len(unst)}
    f = vollpruefung(n, adj, opp, deg, rand, chi, E0)
    voll.append({'phase': 'nach_relaxation', 'fehler': f})

    # Einschwingen
    t_ein = time.time()
    ein_soll = EINF * N
    ein = 0
    reihe_ein = []
    sl = []
    while ein < ein_soll and (time.time() - t_case) < EIN_ANTEIL * budget:
        antrieb()
        s, T, A, st = lawine(cap)
        pruef_schritt()
        ein += 1
        sl.append(s)
        if ein % REIHE == 0:
            reihe_ein.append([ein, sum(sl) / len(sl)] + zustand())
            sl = []
        if ein % VOLLPRUEF == 0:
            f = vollpruefung(n, adj, opp, deg, rand, chi, E0)
            if f:
                voll.append({'phase': 'einschwingen %d' % ein, 'fehler': f})
    t_ein = time.time() - t_ein
    f = vollpruefung(n, adj, opp, deg, rand, chi, E0)
    voll.append({'phase': 'nach_einschwingen', 'fehler': f})

    # Messung
    t_mess = time.time()
    S = []
    TT = []
    AA = []
    ST = []
    reihe = []
    sl = []
    m = 0
    while m < MMAX and (time.time() - t_case) < budget:
        antrieb()
        s, T, A, st = lawine(cap)
        pruef_schritt()
        S.append(s)
        TT.append(T)
        AA.append(A)
        ST.append(st)
        m += 1
        sl.append(s)
        if m % REIHE == 0:
            reihe.append([m, sum(sl) / len(sl)] + zustand())
            sl = []
        if m % VOLLPRUEF == 0:
            f = vollpruefung(n, adj, opp, deg, rand, chi, E0)
            if f:
                voll.append({'phase': 'messung %d' % m, 'fehler': f})
    t_mess = time.time() - t_mess
    f = vollpruefung(n, adj, opp, deg, rand, chi, E0)
    voll.append({'phase': 'ende', 'fehler': f})
    voll_n = 3 + (ein // VOLLPRUEF) + (m // VOLLPRUEF) + 1
    grad_ende = {}
    for v in range(n):
        if inner[v]:
            grad_ende[deg[v]] = grad_ende.get(deg[v], 0) + 1
    rd = [deg[v] for v in range(n) if rand[v]]
    info.update({'N': N, 'E': E0, 'chi': chi, 'innere_kanten': ne})
    out = {
        'netz': info, 'relax': relax,
        'einschwingen': {'soll': ein_soll, 'schritte': ein, 'zeit_s': round(t_ein, 2),
                         'zeitbegrenzt': ein < ein_soll},
        'messung': {'schritte': m, 'zeit_s': round(t_mess, 2), 'mmax': MMAX, 'budget_s': budget},
        'kh0': {'verletzungen': verletz, 'pruef_schritte': zaehl['pruef_schritte'],
                'vollpruefungen': voll_n, 'vollpruefung_fehler': [x for x in voll if x['fehler']]},
        'zaehler': zaehl, 'cap': cap,
        'zeitreihe_spalten': ['schritt', 's_mittel_1000', 'defektanteil', 'q2_mittel', 'instabil', 'rand_grad_mittel',
                              'rand_grad_max', 'grad_min', 'grad_max'],
        'zeitreihe_einschwingen': reihe_ein, 'zeitreihe_messung': reihe,
        'grad_hist_innen_start': {str(k): v for k, v in sorted(grad_start.items())},
        'grad_hist_innen_ende': {str(k): v for k, v in sorted(grad_ende.items())},
        'rand_grad_ende': ({'mittel': sum(rd) / len(rd), 'min': min(rd), 'max': max(rd)} if rd else None),
        'instabil_ende': len(unst), 'zeit_fall_s': round(time.time() - t_case, 2),
    }
    roh = {'s': np.array(S, dtype=np.int64), 'T': np.array(TT, dtype=np.int64), 'A': np.array(AA, dtype=np.int64),
           'st': np.array(ST, dtype=np.int8)}
    return out, roh


# ---------------------------------------------------------------- BTW auf demselben Scheibengraphen
def btw_fall(N, budget, seed):
    t_case = time.time()
    tris, rand, info = netz_scheibe(N, 2000 + N)
    adj, opp, deg = baue(tris, N)
    nbr = [list(s) for s in adj]
    inner = [not b for b in rand]
    inn = [v for v in range(N) if inner[v]]
    ni = len(inn)
    thr = deg[:]
    z = [thr[v] - 1 for v in range(N)]
    rng = random.Random(seed * 1000003 + N)
    rnd = rng.random

    def korn():
        v = inn[int(rnd() * ni)]
        z[v] += 1
        if z[v] < thr[v]:
            return 0, 0, 0
        cur = [v]
        s = 0
        T = 0
        area = set()
        while cur:
            nxt = []
            for x in cur:
                if z[x] >= thr[x]:
                    z[x] -= thr[x]
                    s += 1
                    area.add(x)
                    for u in nbr[x]:
                        if inner[u]:
                            z[u] += 1
                            if z[u] == thr[u]:
                                nxt.append(u)
                    if z[x] >= thr[x]:
                        nxt.append(x)
            T += 1
            cur = nxt
        return s, T, len(area)

    ein_soll = BTW_EINF * N
    ein = 0
    while ein < ein_soll and (time.time() - t_case) < EIN_ANTEIL * budget:
        korn()
        ein += 1
    S = []
    TT = []
    AA = []
    m = 0
    t_mess = time.time()
    while m < MMAX and (time.time() - t_case) < budget:
        s, T, A = korn()
        S.append(s)
        TT.append(T)
        AA.append(A)
        m += 1
    info.update({'N': N, 'E': len(opp)})
    out = {'netz': info, 'einschwingen': {'soll': ein_soll, 'schritte': ein, 'zeitbegrenzt': ein < ein_soll},
           'messung': {'schritte': m, 'zeit_s': round(time.time() - t_mess, 2), 'mmax': MMAX, 'budget_s': budget},
           'stabil_ende': all(z[v] < thr[v] for v in range(N)), 'zeit_fall_s': round(time.time() - t_case, 2)}
    roh = {'s': np.array(S, dtype=np.int64), 'T': np.array(TT, dtype=np.int64), 'A': np.array(AA, dtype=np.int64),
           'st': np.zeros(len(S), dtype=np.int8)}
    return out, roh


def kopf(modus, args):
    import scipy
    return {'karte': 'KRUEMMUNGS-SANDHAUFEN-2D-1', 'modus': modus, 'code_sha256': code_sha(),
            'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__,
            'host': platform.node(), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'rauch': bool(getattr(args, 'rauch', False)), 'argv': sys.argv[1:],
            'konstanten': {'SMIN': SMIN, 'CAPF': CAPF, 'RELAXF': RELAXF, 'EINF': EINF, 'EIN_ANTEIL': EIN_ANTEIL,
                           'MMAX': MMAX, 'VOLLPRUEF': VOLLPRUEF, 'REIHE': REIHE, 'BTW_EINF': BTW_EINF}}


def cmd_lauf(args):
    res = kopf('lauf', args)
    res.update({'geo': args.geo, 'arm': args.arm, 'seed': args.seed})
    Ns = [int(x) for x in args.N.split(',')]
    bs = [float(x) for x in args.budget.split(',')]
    rs = [float(x) for x in args.r.split(',')]
    faelle = []
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    for r in rs:
        for N, b in zip(Ns, bs):
            name = '%s-%s-N%d' % (args.geo, args.arm, N) + (('-r%g' % r) if r > 0 else '')
            out, roh = simuliere(args.geo, args.arm, N, b, args.seed, r=r, rauch=args.rauch)
            npz = '%s-%s.npz' % (args.out, name)
            np.savez_compressed(npz, **roh)
            out.update({'name': name, 'geo': args.geo, 'arm': args.arm, 'N': N, 'r': r, 'npz': os.path.basename(npz)})
            faelle.append(out)
            print('fall %s fertig: %.1f s' % (name, out['zeit_fall_s']), flush=True)
    res['faelle'] = faelle
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    with open(args.out + '.json', 'w') as f:
        json.dump(res, f, indent=1)


def cmd_btw(args):
    res = kopf('btw', args)
    res.update({'geo': 'scheibe', 'arm': 'BTW', 'seed': args.seed})
    Ns = [int(x) for x in args.N.split(',')]
    bs = [float(x) for x in args.budget.split(',')]
    faelle = []
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    for N, b in zip(Ns, bs):
        name = 'btw-N%d' % N
        out, roh = btw_fall(N, b, args.seed)
        npz = '%s-%s.npz' % (args.out, name)
        np.savez_compressed(npz, **roh)
        out.update({'name': name, 'geo': 'scheibe', 'arm': 'BTW', 'N': N, 'r': 0.0, 'npz': os.path.basename(npz)})
        faelle.append(out)
        print('fall %s fertig: %.1f s' % (name, out['zeit_fall_s']), flush=True)
    res['faelle'] = faelle
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    with open(args.out + '.json', 'w') as f:
        json.dump(res, f, indent=1)


# ---------------------------------------------------------------- Auswertung (PLAN 6, mechanisch)
class Stuetze:
    """Traeger [smin, sup] ganzzahlig. Exakte Summe bis GRENZE, darueber Integral auf log-Gitter (Euler-Maclaurin)."""
    GRENZE = 3000

    def __init__(self, smin, sup):
        self.smin = smin
        self.sup = int(sup)
        self.umax = math.log10(max(self.sup, 10)) + 4.0
        m = min(self.sup, self.GRENZE)
        self.s1 = np.arange(smin, m + 1, dtype=float)
        self.l1 = np.log(self.s1)
        if self.sup > m:
            lx = np.linspace(math.log(m + 0.5), math.log(self.sup + 0.5), 4001)
            dl = lx[1] - lx[0]
            w = np.full(lx.size, dl)
            w[0] = w[-1] = dl / 2.0
            self.s2 = np.exp(lx)
            self.l2 = lx
            self.lw2 = np.log(w) + lx
        else:
            self.s2 = None

    def logz(self, f):
        a = f(self.s1, self.l1)
        if self.s2 is not None:
            a = np.concatenate([a, f(self.s2, self.l2) + self.lw2])
        m = a.max()
        return m + math.log(np.exp(a - m).sum())


def nll_m1(p, st, n, slog, ssum):
    tau, u = float(p[0]), float(p[1])
    if not (-3.0 < tau < 6.0 and -1.0 < u < st.umax):
        return 1e300
    lam = 10.0 ** (-u)
    lz = st.logz(lambda s, l: -tau * l - lam * s)
    return n * lz + tau * slog + lam * ssum


def fit_m1(st, n, slog, ssum, start=None):
    from scipy.optimize import minimize
    if start is None:
        best = None
        for tau in np.arange(-1.0, 3.01, 0.25):
            for u in np.linspace(0.0, st.umax - 0.5, 14):
                v = nll_m1((tau, u), st, n, slog, ssum)
                if best is None or v < best[0]:
                    best = (v, tau, u)
        start = (best[1], best[2])
    r = minimize(nll_m1, np.array(start, dtype=float), args=(st, n, slog, ssum), method='Nelder-Mead',
                 options={'xatol': 1e-5, 'fatol': 1e-7, 'maxiter': 4000})
    return float(r.x[0]), float(r.x[1]), float(r.fun)


def fit_m2(st, n, ssum):
    from scipy.optimize import minimize_scalar

    def f(u):
        lam = 10.0 ** (-u)
        return n * st.logz(lambda s, l: -lam * s) + lam * ssum
    r = minimize_scalar(f, bounds=(-2.0, st.umax), method='bounded', options={'xatol': 1e-7})
    return float(r.x), float(r.fun)


def nll_m3(p, st, lvals, cnts, n):
    lb, u = float(p[0]), float(p[1])
    if not (-5.0 < lb < 1.2 and -2.0 < u < st.umax):
        return 1e300
    beta = math.exp(lb)
    ls0 = u * math.log(10.0)
    with np.errstate(over='ignore'):
        lz = st.logz(lambda s, l: -np.exp(beta * (l - ls0)))
        dat = float((cnts * np.exp(beta * (lvals - ls0))).sum())
    if not np.isfinite(dat) or not np.isfinite(lz):
        return 1e300
    return n * lz + dat


def fit_m3(st, lvals, cnts, n):
    from scipy.optimize import minimize
    best = None
    for b in (0.03, 0.06, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0):
        for u in np.linspace(-1.0, st.umax - 0.5, 14):
            v = nll_m3((math.log(b), u), st, lvals, cnts, n)
            if best is None or v < best[0]:
                best = (v, math.log(b), u)
    r = minimize(nll_m3, np.array(best[1:], dtype=float), args=(st, lvals, cnts, n), method='Nelder-Mead',
                 options={'xatol': 1e-5, 'fatol': 1e-7, 'maxiter': 4000})
    return float(math.exp(r.x[0])), float(r.x[1]), float(r.fun)


def m1_pmf_auf(st, tau, u, s_int):
    lam = 10.0 ** (-u)
    lz = st.logz(lambda s, l: -tau * l - lam * s)
    return np.exp(-tau * np.log(s_int) - lam * s_int - lz)


def bins_fuer(smax):
    e = np.unique(np.floor(SMIN * 10.0 ** (np.arange(0, 90) / 10.0)).astype(np.int64))
    e = e[e <= smax]
    return np.append(e, smax + 1)


def bin_pruefung(x, tau, u, st):
    """Log-Bins (10 je Dekade ab SMIN); beobachtet gegen M1 erwartet. Gibt Tabelle und Kriterium (c) zurueck."""
    n = x.size
    smax = int(x.max())
    e = bins_fuer(smax)
    obs = np.histogram(x, bins=e.astype(float) - 0.5)[0]
    s_all = np.arange(SMIN, smax + 1, dtype=float)
    p = m1_pmf_auf(st, tau, u, s_all)
    cp = np.concatenate([[0.0], np.cumsum(p)])
    exp_ = n * (cp[e[1:] - SMIN] - cp[e[:-1] - SMIN])
    sc = 10.0 ** u
    grenze = min(sc / 2.0, smax)
    tab = []
    dev = 0.0
    nb = 0
    for i in range(len(obs)):
        lo, hi = int(e[i]), int(e[i + 1] - 1)
        ok = (obs[i] >= 100 and hi <= grenze and exp_[i] > 0)
        d = math.log10(obs[i] / exp_[i]) if (obs[i] > 0 and exp_[i] > 0) else None
        if ok:
            nb += 1
            dev = max(dev, abs(d))
        tab.append([lo, hi, int(obs[i]), float(exp_[i]), d, bool(ok)])
    return {'bins': tab, 'max_abw_log10': dev if nb else None, 'n_bins_geprueft': nb, 'grenze': grenze}


def blockgrenzen(m, B):
    return [(m * i) // B for i in range(B + 1)]


def analyse_fall(fall, roh, sup_override=None, boot_tau=100, boot_sc=200, seed=7):
    s = roh['s']
    st_ = roh['st']
    N = fall['N']
    res = {'name': fall['name'], 'geo': fall['geo'], 'arm': fall['arm'], 'N': N, 'r': fall.get('r', 0.0)}
    m = int(s.size)
    pos = s >= 1
    nav = int(pos.sum())
    res.update({'schritte': m, 'lawinen_s_ge_1': nav, 'anteil_s0': (1.0 - nav / m) if m else None})
    if nav == 0:
        res['p2d'] = {'urteil': 'nicht bestimmbar', 'gruende': ['keine Lawinen']}
        return res
    sp = s[pos].astype(float)
    stp = st_[pos]
    res.update({'s_mittel': float(sp.mean()), 's_max': int(sp.max()),
                'anteil_status': {str(k): float((stp == k).mean()) for k in (0, 1, 2, 3)}})
    abbruch = float(((stp == 2) | (stp == 3)).mean())
    res['abbruchanteil'] = abbruch
    # Momentverhaeltnis s_c2 = <s^2>/<s> ueber alle Lawinen s >= 1
    res['sc2'] = float((sp ** 2).sum() / sp.sum())
    rng = np.random.default_rng(seed + N)
    B = 20
    g = blockgrenzen(nav, B)
    s1b = np.array([sp[g[i]:g[i + 1]].sum() for i in range(B)])
    s2b = np.array([(sp[g[i]:g[i + 1]] ** 2).sum() for i in range(B)])
    sc2_boot = []
    for _ in range(boot_sc):
        idx = rng.integers(0, B, B)
        sc2_boot.append(float(s2b[idx].sum() / s1b[idx].sum()) if s1b[idx].sum() > 0 else float('nan'))
    res['sc2_boot'] = sc2_boot
    res['sc2_ki95'] = [float(np.nanpercentile(sc2_boot, 2.5)), float(np.nanpercentile(sc2_boot, 97.5))]
    # Stationaritaet: Haelften, Blockfehler
    h = nav // 2
    zs = {}
    for nm, arr in (('erste', sp[:h]), ('zweite', sp[h:])):
        gg = blockgrenzen(arr.size, 10)
        bm = np.array([arr[gg[i]:gg[i + 1]].mean() for i in range(10) if gg[i + 1] > gg[i]])
        zs[nm] = [float(arr.mean()) if arr.size else None,
                  float(bm.std(ddof=1) / math.sqrt(bm.size)) if bm.size > 1 else None]
    zz = None
    if zs['erste'][1] and zs['zweite'][1]:
        zz = abs(zs['erste'][0] - zs['zweite'][0]) / math.sqrt(zs['erste'][1] ** 2 + zs['zweite'][1] ** 2)
    res['stationaritaet'] = {'mittel_se_erste': zs['erste'], 'mittel_se_zweite': zs['zweite'], 'z': zz,
                             'drift': (zz is not None and zz > 3.0)}
    # Fitstichprobe: s >= SMIN, Status 0 oder 1
    mask = (s >= SMIN) & ((st_ == 0) | (st_ == 1))
    x = s[mask].astype(float)
    nf = int(x.size)
    res['n_fit'] = nf
    sup = sup_override if sup_override else CAPF * N
    res['traeger_oben'] = int(sup)
    if nf < 50:
        res['p2d'] = {'urteil': 'nein' if abbruch > 0.001 else 'nicht bestimmbar',
                      'gruende': ['n_fit < 50'] + (['(e) Abbruchanteil'] if abbruch > 0.001 else [])}
        return res
    stz = Stuetze(SMIN, max(sup, int(x.max())))
    slog = float(np.log(x).sum())
    ssum = float(x.sum())
    tau, u, nll1 = fit_m1(stz, nf, slog, ssum)
    u2, nll2 = fit_m2(stz, nf, ssum)
    vals, cnts = np.unique(x, return_counts=True)
    beta, u3, nll3 = fit_m3(stz, np.log(vals), cnts.astype(float), nf)
    aic1, aic2, aic3 = 4 + 2 * nll1, 2 + 2 * nll2, 4 + 2 * nll3
    res['m1'] = {'tau': tau, 'log10_sc': u, 'sc': 10.0 ** u, 'nll': nll1, 'aic': aic1}
    res['m2'] = {'log10_s0': u2, 'nll': nll2, 'aic': aic2}
    res['m3'] = {'beta': beta, 'log10_s0': u3, 'nll': nll3, 'aic': aic3}
    bp = bin_pruefung(x, tau, u, stz)
    res['bins'] = bp
    # Bootstrap tau (Bloecke in Zeitordnung)
    gx = blockgrenzen(nf, B)
    bl = [(gx[i + 1] - gx[i], float(np.log(x[gx[i]:gx[i + 1]]).sum()), float(x[gx[i]:gx[i + 1]].sum()))
          for i in range(B)]
    tb = []
    sb = []
    for _ in range(boot_tau):
        idx = rng.integers(0, B, B)
        nn = sum(bl[i][0] for i in idx)
        sl = sum(bl[i][1] for i in idx)
        ss = sum(bl[i][2] for i in idx)
        t_, u_, _ = fit_m1(stz, nn, sl, ss, start=(tau, u))
        tb.append(t_)
        sb.append(u_)
    res['m1']['tau_ki95'] = [float(np.percentile(tb, 2.5)), float(np.percentile(tb, 97.5))]
    res['m1']['log10_sc_ki95'] = [float(np.percentile(sb, 2.5)), float(np.percentile(sb, 97.5))]
    # Kriterien (a)-(e)
    n_gross = int((x >= 100 * SMIN).sum())
    krit = {
        'a_aic_m2_minus_m1': aic2 - aic1, 'a_aic_m3_minus_m1': aic3 - aic1,
        'a': bool(aic2 - aic1 >= 10.0 and aic3 - aic1 >= 10.0),
        'b_sc_durch_smin': 10.0 ** u / SMIN, 'b': bool(10.0 ** u >= 100 * SMIN),
        'c_max_abw_log10': bp['max_abw_log10'], 'c_n_bins': bp['n_bins_geprueft'],
        'c': bool(bp['max_abw_log10'] is not None and bp['max_abw_log10'] <= 0.15),
        'd_n_ueber_100smin': n_gross, 'd': bool(n_gross >= 50),
        'e_abbruchanteil': abbruch, 'e': bool(abbruch <= 0.001),
    }
    gruende = [k for k in 'abcde' if not krit[k]]
    if not krit['e']:
        urteil = 'nein'
    elif all(krit[k] for k in 'abcde'):
        urteil = 'ja' if nf >= 5000 else 'nicht bestimmbar'
    else:
        urteil = 'nein' if nf >= 1000 else 'nicht bestimmbar'
    res['p2d'] = {'urteil': urteil, 'gruende': gruende, 'kriterien': krit}
    # Dauer und Flaeche (beschreibend): M1 auf T >= 2 bzw. A >= 2
    for nm in ('T', 'A'):
        y = roh[nm][mask]
        y = y[y >= SMIN].astype(float)
        if y.size >= 50:
            sty = Stuetze(SMIN, max(int(y.max()) * 10, 1000))
            t_, u_, _ = fit_m1(sty, int(y.size), float(np.log(y).sum()), float(y.sum()))
            res['m1_' + nm] = {'tau': t_, 'log10_c': u_, 'mittel': float(y.mean()), 'max': int(y.max()),
                               'n': int(y.size)}
    return res


def d_fit(rs):
    """D aus log sc2 gegen log N (OLS), Bootstrap aus den sc2-Bootstraps je N (unabhaengig)."""
    if not all(('sc2' in r and 'sc2_boot' in r) for r in rs):
        return None
    Ns = np.array([r['N'] for r in rs], dtype=float)
    sc = np.array([r['sc2'] for r in rs], dtype=float)
    D = float(np.polyfit(np.log(Ns), np.log(sc), 1)[0])
    bs = np.array([r['sc2_boot'] for r in rs], dtype=float)
    Db = []
    for j in range(bs.shape[1]):
        y = bs[:, j]
        if np.all(np.isfinite(y)) and np.all(y > 0):
            Db.append(float(np.polyfit(np.log(Ns), np.log(y), 1)[0]))
    mono = bool(np.all(np.diff(sc) > 0))
    out = {'N': Ns.tolist(), 'sc2': sc.tolist(), 'D': D, 'D_ki95': [float(np.percentile(Db, 2.5)),
                                                                     float(np.percentile(Db, 97.5))],
           'D_ki68': [float(np.percentile(Db, 16)), float(np.percentile(Db, 84))], 'monoton': mono,
           'n_boot': len(Db)}
    if all('m1' in r for r in rs):
        y = np.array([r['m1']['log10_sc'] for r in rs]) * math.log(10.0)
        out['D_m1'] = float(np.polyfit(np.log(Ns), y, 1)[0])
    return out


def urteil_kh3(d):
    if d['D_ki95'][0] > 0.3 and d['monoton']:
        return 'eingetroffen'
    if d['D_ki95'][1] <= 0.3:
        return 'nicht eingetroffen'
    return 'nicht entscheidbar'


def bild_gruppe(pfad, titel, faelle_roh, analysen, farben=('#2a78d6', '#eb6834', '#1baf7a'),
                marker=('o', 's', '^'), etiketten=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7.2, 5.0), dpi=130)
    fig.patch.set_facecolor('#fcfcfb')
    ax.set_facecolor('#fcfcfb')
    for i, ((fall, roh), an) in enumerate(zip(faelle_roh, analysen)):
        s = roh['s']
        ok = (s >= 1) & ((roh['st'] == 0) | (roh['st'] == 1))
        x = s[ok]
        if x.size == 0:
            continue
        e = np.unique(np.floor(10.0 ** (np.arange(0, 90) / 10.0)).astype(np.int64))
        e = e[e <= x.max()]
        e = np.append(e, x.max() + 1)
        h = np.histogram(x, bins=e.astype(float) - 0.5)[0]
        w = np.diff(e)
        c = np.sqrt(e[:-1] * (e[1:] - 1).clip(min=e[:-1]))
        y = h / (x.size * w)
        k = h > 0
        lab = etiketten[i] if etiketten else 'N = %d' % fall['N']
        ax.plot(c[k], y[k], linestyle='none', marker=marker[i % 3], markersize=5, color=farben[i % 3],
                label='%s (%d Lawinen)' % (lab, int(x.size)))
        if 'm1' in an:
            stz = Stuetze(SMIN, an['traeger_oben'])
            sx = np.unique(np.logspace(math.log10(SMIN), math.log10(max(x.max(), SMIN + 1)), 200).astype(int))
            sx = sx[sx >= SMIN].astype(float)
            p = m1_pmf_auf(stz, an['m1']['tau'], an['m1']['log10_sc'], sx) * (an['n_fit'] / x.size)
            ax.plot(sx, p, linestyle='--', linewidth=1.2, color=farben[i % 3])
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Lawinengroesse s (Kipp-Flips)', color='#0b0b0b')
    ax.set_ylabel('P(s) (log-gebinnt, je Wert)', color='#0b0b0b')
    ax.set_title(titel, color='#0b0b0b', fontsize=11)
    ax.grid(True, which='major', color='#e4e3df', linewidth=0.6)
    for sp_ in ax.spines.values():
        sp_.set_color('#8a8984')
    ax.tick_params(colors='#52514e')
    if ax.get_legend_handles_labels()[0]:
        ax.legend(frameon=False, fontsize=8, loc='lower left')
    ax.text(0.99, 0.99, 'Punkte: Messung; gestrichelt: Fit M1 (s >= %d)\nsynthetisch, keine Messdaten' % SMIN,
            transform=ax.transAxes, ha='right', va='top', fontsize=7.5, color='#52514e')
    fig.tight_layout()
    fig.savefig(pfad, facecolor=fig.get_facecolor())
    plt.close(fig)


def cmd_aus(args):
    res = kopf('aus', args)
    laeufe = []
    alle = []
    for pf in args.ein:
        with open(pf) as f:
            L = json.load(f)
        laeufe.append({'datei': pf, 'code_sha256': L['code_sha256'], 'rauch': L['rauch'], 'modus': L['modus']})
        d = os.path.dirname(os.path.abspath(pf))
        for fall in L['faelle']:
            z = np.load(os.path.join(d, fall['npz']))
            roh = {k: z[k] for k in ('s', 'T', 'A', 'st')}
            alle.append((fall, roh))
    res['laeufe'] = laeufe
    an = {}
    for fall, roh in alle:
        sup = None
        if fall['arm'] == 'BTW':
            sup = max(CAPF * fall['N'], int(roh['s'].max()) * 10 if roh['s'].size else 10)
        a = analyse_fall(fall, roh, sup_override=sup)
        if fall['arm'] != 'BTW':
            a['kh0'] = fall['kh0']
            a['einschwingen'] = fall['einschwingen']
            a['relax'] = fall['relax']
            a['instabil_ende'] = fall['instabil_ende']
            a['rand_grad_ende'] = fall['rand_grad_ende']
            a['zaehler'] = fall['zaehler']
        an[fall['name']] = a
        print('analyse %s' % fall['name'], flush=True)
    res['faelle'] = an
    Ns = (500, 2000, 8000)

    def hol(geo, arm, N, r=0.0):
        nm = '%s-%s-N%d' % (geo, arm, N) + (('-r%g' % r) if r > 0 else '')
        return an.get(nm)

    # Eichung
    btw8 = an.get('btw-N8000')
    eich = bool(btw8 is not None and btw8['p2d']['urteil'] == 'ja')
    res['eichung_btw'] = {'p2d_N8000': btw8['p2d']['urteil'] if btw8 else None,
                          'tau_N8000': btw8['m1']['tau'] if btw8 and 'm1' in btw8 else None, 'bestanden': eich}
    U = {}
    # KH0
    kf = [hol('kugel', a, N) for a in ('Z', 'D') for N in Ns]
    if all(k is not None for k in kf):
        v = sum(sum(k['kh0']['verletzungen'].values()) for k in kf)
        vf = sum(len(k['kh0']['vollpruefung_fehler']) for k in kf)
        ps = sum(k['kh0']['pruef_schritte'] for k in kf)
        U['KH0'] = {'plan': 'eingetroffen' if (v == 0 and vf == 0) else 'nicht eingetroffen',
                    'wortlaut': 'eingetroffen' if (v == 0 and vf == 0) else 'nicht eingetroffen',
                    'verletzungen': v, 'vollpruefung_fehler': vf, 'gepruefte_schritte': ps,
                    'vollpruefungen': sum(k['kh0']['vollpruefungen'] for k in kf)}

    def kh1_arm(arm):
        a = hol('scheibe', arm, 8000)
        if a is None:
            return 'fehlt', None
        p = a['p2d']['urteil']
        tau = a['m1']['tau'] if 'm1' in a else None
        if p == 'ja':
            return ('eingetroffen' if 1.0 <= tau <= 1.6 else 'nicht eingetroffen'), tau
        if p == 'nein':
            return ('nicht eingetroffen' if eich else 'nicht entscheidbar (Eichung)'), tau
        return 'nicht entscheidbar', tau

    def kh2_arm(arm):
        ps = []
        for N in Ns:
            a = hol('kugel', arm, N)
            ps.append(a['p2d']['urteil'] if a else 'fehlt')
        if 'ja' in ps:
            return 'nicht eingetroffen', ps
        if all(p == 'nein' for p in ps):
            return ('eingetroffen' if eich else 'nicht entscheidbar (Eichung)'), ps
        return 'nicht entscheidbar', ps

    def wortlaut(u1, u2):
        if u1 == u2:
            return u1
        if 'nicht entscheidbar' in u1 or 'nicht entscheidbar' in u2 or 'fehlt' in (u1, u2):
            return 'nicht entscheidbar'
        return 'armabhaengig (teilweise)'

    k1z, tz = kh1_arm('Z')
    k1d, td = kh1_arm('D')
    U['KH1'] = {'plan': k1z, 'wortlaut': wortlaut(k1z, k1d), 'arm_Z': k1z, 'arm_D': k1d, 'tau_Z': tz, 'tau_D': td}
    k2z, pz = kh2_arm('Z')
    k2d, pd = kh2_arm('D')
    U['KH2'] = {'plan': k2z, 'wortlaut': wortlaut(k2z, k2d), 'arm_Z': k2z, 'arm_D': k2d, 'p2d_Z': pz, 'p2d_D': pd}
    dfits = {}
    for arm in ('Z', 'D'):
        rs = [hol('scheibe', arm, N) for N in Ns]
        if all(r is not None for r in rs):
            dfits['scheibe-' + arm] = d_fit(rs)
    rs = [an.get('btw-N%d' % N) for N in Ns]
    if all(r is not None for r in rs):
        dfits['btw'] = d_fit(rs)
    for arm in ('Z', 'D'):
        rs = [hol('kugel', arm, N) for N in Ns]
        if all(r is not None for r in rs):
            dfits['kugel-' + arm] = d_fit(rs)
    res['d_fits'] = dfits
    dfits = {k: v for k, v in dfits.items() if v is not None}
    res['d_fits'] = dfits
    if 'scheibe-Z' in dfits:
        k3z = urteil_kh3(dfits['scheibe-Z'])
        k3d = urteil_kh3(dfits['scheibe-D']) if 'scheibe-D' in dfits else 'fehlt'
        U['KH3'] = {'plan': k3z, 'wortlaut': wortlaut(k3z, k3d), 'arm_Z': k3z, 'arm_D': k3d,
                    'D_Z': dfits['scheibe-Z']['D'], 'D_Z_ki95': dfits['scheibe-Z']['D_ki95'],
                    'D_D': dfits['scheibe-D']['D'] if 'scheibe-D' in dfits else None}
    # Antriebsrate (Kontrolle, beschreibend)
    rk = []
    for r in (0.0, 0.01, 0.1):
        a = hol('scheibe', 'Z', 2000, r)
        if a is not None:
            rk.append({'r': r, 'tau': a['m1']['tau'] if 'm1' in a else None,
                       'sc2': a['sc2'], 'sc2_ki95': a['sc2_ki95'], 'p2d': a['p2d']['urteil']})
    res['kontrolle_antriebsrate'] = rk
    if len(rk) >= 2 and rk[0]['tau'] is not None:
        res['kontrolle_antriebsrate_flag'] = {
            'dtau_r0.01': (rk[1]['tau'] - rk[0]['tau']) if rk[1]['tau'] is not None else None,
            'exponent_stabil_r0.01': bool(rk[1]['tau'] is not None and abs(rk[1]['tau'] - rk[0]['tau']) <= 0.1)}
    res['urteile'] = U
    # Bilder
    os.makedirs(args.bild, exist_ok=True)
    bilder = []
    gruppen = [('kugel', 'Z'), ('kugel', 'D'), ('scheibe', 'Z'), ('scheibe', 'D')]
    for geo, arm in gruppen:
        fr = [(f, r) for (f, r) in alle if f['geo'] == geo and f['arm'] == arm and f.get('r', 0.0) == 0.0]
        fr.sort(key=lambda t: t[0]['N'])
        if fr:
            p = os.path.join(args.bild, 'bild-Ps-%s-%s.png' % (geo, arm))
            bild_gruppe(p, 'Kruemmungs-Sandhaufen, %s, Arm %s' % (geo, arm), fr, [an[f['name']] for f, _ in fr])
            bilder.append(p)
    fr = sorted([(f, r) for (f, r) in alle if f['arm'] == 'BTW'], key=lambda t: t[0]['N'])
    if fr:
        p = os.path.join(args.bild, 'bild-Ps-btw.png')
        bild_gruppe(p, 'BTW-Sandhaufen auf denselben Scheibengraphen (Eichung)', fr, [an[f['name']] for f, _ in fr])
        bilder.append(p)
    fr = sorted([(f, r) for (f, r) in alle if f['geo'] == 'scheibe' and f['arm'] == 'Z' and f['N'] == 2000],
                key=lambda t: t[0].get('r', 0.0))
    if len(fr) > 1:
        p = os.path.join(args.bild, 'bild-Ps-antriebsrate.png')
        bild_gruppe(p, 'Antriebsrate: Scheibe, Arm Z, N = 2000', fr, [an[f['name']] for f, _ in fr],
                    etiketten=['r = %g' % f.get('r', 0.0) for f, _ in fr])
        bilder.append(p)
    res['bilder'] = bilder
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    for k, a in res['faelle'].items():
        a.pop('sc2_boot', None)
    with open(args.out, 'w') as f:
        json.dump(res, f, indent=1)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    a = sp.add_parser('lauf')
    a.add_argument('--geo', choices=['kugel', 'scheibe'], required=True)
    a.add_argument('--arm', choices=['Z', 'D'], required=True)
    a.add_argument('--N', default='500,2000,8000')
    a.add_argument('--budget', default='50,90,300')
    a.add_argument('--seed', type=int, required=True)
    a.add_argument('--r', default='0')
    a.add_argument('--out', required=True)
    a.add_argument('--rauch', action='store_true')
    b = sp.add_parser('btw')
    b.add_argument('--N', default='500,2000,8000')
    b.add_argument('--budget', default='40,80,300')
    b.add_argument('--seed', type=int, required=True)
    b.add_argument('--out', required=True)
    b.add_argument('--rauch', action='store_true')
    c = sp.add_parser('aus')
    c.add_argument('--ein', nargs='+', required=True)
    c.add_argument('--out', required=True)
    c.add_argument('--bild', required=True)
    c.add_argument('--rauch', action='store_true')
    args = ap.parse_args()
    {'lauf': cmd_lauf, 'btw': cmd_btw, 'aus': cmd_aus}[args.cmd](args)


if __name__ == '__main__':
    main()
