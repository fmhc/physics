#!/usr/bin/env python3
# LIFE-DIAMANT-1 (Runde 38): Vollsuche der 512 aussen-totalistischen Ja/Nein-Regeln (B ohne 0) auf dem Diamantgitter.
# Code-Agent fuer die Leitung claude-primary. Laeuft nur auf der .69 ueber kleintest.sh (Spur cpu7), 1 Thread.
# Aufruf:
#   life_diamant.py kontrolle <aus.json>
#   life_diamant.py block <regeln> <aus.jsonl> [zeitgrenze_s]     regeln: "a-b" (Indizes a..b-1) oder "i,j,k"
# Regelindex = bmaske*32 + smaske; bmaske Bit k-1 <-> k in B (k = 1..4), smaske Bit k <-> k in S (k = 0..4).
# Duennbesetzte Darstellung (sortierte int64-Schluessel), unbegrenztes Gitter, kein periodischer Kasten.
import sys, json, time, itertools, math, hashlib
import numpy as np
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

PARAM = dict(T=256, C_max=600, T_iso=128, C_iso=300, R=6.0, pruefpunkte=[64, 128, 192],
             dichten=[0.25, 0.4, 0.6], saaten_je_dichte=16, saat_basis=380438,
             stufe2_saaten_2=600, stufe2_saaten_3=300, stufe2_saaten_4=60, stufe2_zeitkappe_s=6.0)

# ---------------------------------------------------------------- Gitter
# Koordinaten in a/4 (a = kubische Zellkante). Knoten (n1, n2, n3, s): Lage n1*A1 + n2*A2 + n3*A3 + s*(1,1,1).
# A (s=0) bei n: B-Nachbarn bei n, n-e1, n-e2, n-e3 (Lage +e_a); B (s=1) bei n: A-Nachbarn bei n, n+e1, n+e2, n+e3 (-e_a).
BITS = 20
OFF = 1 << (BITS - 1)
MASK = (1 << BITS) - 1
SH1 = 2 * BITS + 1
SH2 = BITS + 1
DA = np.array([1, 1 - (1 << SH1), 1 - (1 << SH2), 1 - 2], dtype=np.int64)
DB = -DA
A1 = np.array([0, 2, 2]); A2 = np.array([2, 0, 2]); A3 = np.array([2, 2, 0])
E = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
W3 = math.sqrt(3.0)


def kodiere(n1, n2, n3, s):
    n1 = np.asarray(n1, dtype=np.int64); n2 = np.asarray(n2, dtype=np.int64)
    n3 = np.asarray(n3, dtype=np.int64); s = np.asarray(s, dtype=np.int64)
    return ((((n1 + OFF) << BITS | (n2 + OFF)) << BITS | (n3 + OFF)) << 1) | s


def dekodiere(k):
    k = np.asarray(k, dtype=np.int64)
    s = k & 1
    b = k >> 1
    n3 = (b & MASK) - OFF
    n2 = ((b >> BITS) & MASK) - OFF
    n1 = (b >> (2 * BITS)) - OFF
    return n1, n2, n3, s


def kart(k):
    n1, n2, n3, s = dekodiere(k)
    return np.stack([2 * (n2 + n3) + s, 2 * (n1 + n3) + s, 2 * (n1 + n2) + s], axis=-1)


def ist_knoten(xyz):
    xyz = np.asarray(xyz, dtype=np.int64)
    s = xyz[..., 0] & 1
    ok = ((xyz[..., 1] & 1) == s) & ((xyz[..., 2] & 1) == s)
    r = xyz - s[..., None]
    ok &= ((r[..., 0] & 1) == 0) & ((r.sum(axis=-1) % 4) == 0)
    return ok


def aus_kart(xyz):
    xyz = np.asarray(xyz, dtype=np.int64).reshape(-1, 3)
    if not np.all(ist_knoten(xyz)):
        raise ValueError('kein Diamantknoten')
    s = xyz[:, 0] & 1
    x = xyz[:, 0] - s; y = xyz[:, 1] - s; z = xyz[:, 2] - s
    return np.sort(kodiere((y + z - x) // 4, (x + z - y) // 4, (x + y - z) // 4, s))


def regel_masken(idx):
    bm, sm = idx // 32, idx % 32
    bmask = np.array([False] + [bool((bm >> (k - 1)) & 1) for k in range(1, 5)])
    smask = np.array([bool((sm >> k) & 1) for k in range(5)])
    name = 'B' + ''.join(str(k) for k in range(1, 5) if bmask[k]) + '/S' + ''.join(str(k) for k in range(5) if smask[k])
    return bmask, smask, name


def schritt(live, bmask, smask):
    """Ein synchroner Schritt. live: sortiertes, eindeutiges int64-Array."""
    if live.size == 0:
        return live
    isA = (live & 1) == 0
    nb = np.concatenate(((live[isA][:, None] + DA).ravel(), (live[~isA][:, None] + DB).ravel()))
    keys, cnt = np.unique(nb, return_counts=True)
    pos = np.minimum(np.searchsorted(keys, live), keys.size - 1)
    cl = np.where(keys[pos] == live, cnt[pos], 0)
    surv = live[smask[cl]]
    posl = np.minimum(np.searchsorted(live, keys), live.size - 1)
    isl = live[posl] == keys
    born = keys[(~isl) & bmask[cnt]]
    return np.sort(np.concatenate((surv, born)))


def form(live):
    """Verschiebungsfreie Kennung (fcc-Translationen, Untergitter bleibt im Schluessel) und Bezugsecke."""
    b = live >> 1
    u3 = b & MASK; u2 = (b >> BITS) & MASK; u1 = b >> (2 * BITS)
    m1, m2, m3 = int(u1.min()), int(u2.min()), int(u3.min())
    shift = ((((m1 << BITS) | m2) << BITS) | m3) << 1
    return (live - shift).tobytes(), (m1, m2, m3)


def lauf(live, regel, T, cmax, pruef=None, beim_pruefpunkt=None, schritt_fn=None):
    """Verlauf bis Aussterben, Formwiederkehr, Groessenschranke oder T. Gibt Klasse und Endmuster zurueck."""
    if schritt_fn is None:
        bmask, smask = regel
        sf = lambda L, t: schritt(L, bmask, smask)
    else:
        sf = schritt_fn
    if live.size == 0:
        return dict(klasse='tot', t=0, live=live)
    f, anc = form(live)
    seen = {f: (0, anc)}
    for t in range(1, T + 1):
        live = sf(live, t)
        if live.size == 0:
            return dict(klasse='tot', t=t, live=live)
        if live.size > cmax:
            return dict(klasse='gross', t=t, live=live)
        f, anc = form(live)
        if f in seen:
            t0, a0 = seen[f]
            p = t - t0
            d = (anc[0] - a0[0], anc[1] - a0[1], anc[2] - a0[2])
            kl = 'gleiter' if d != (0, 0, 0) else ('still' if p == 1 else 'osz')
            return dict(klasse=kl, t=t, t0=t0, p=p, d=d, live=live)
        seen[f] = (t, anc)
        if pruef is not None and t in pruef:
            beim_pruefpunkt(live, t)
    return dict(klasse='offen', t=T, live=live)


def zerlege(live, R):
    if live.size == 0:
        return []
    xyz = kart(live).astype(float)
    pairs = cKDTree(xyz).query_pairs(R, output_type='ndarray')
    k = live.size
    g = coo_matrix((np.ones(len(pairs)), (pairs[:, 0], pairs[:, 1])), shape=(k, k)) if len(pairs) else coo_matrix((k, k))
    nc, lab = connected_components(g, directed=False)
    return [live[lab == i] for i in range(nc)]


# ---------------------------------------------------------------- Symmetrie (Td und Bindungsmitten-Inversion)
def td_gruppe():
    Eset = {tuple(e) for e in E}
    out = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            P[i, j] = 1
        for sg in itertools.product([1, -1], repeat=3):
            M = np.diag(sg) @ P
            if {tuple(M @ e) for e in E} == Eset:
                out.append(M)
    return out


def element_typ(L):
    det = int(round(np.linalg.det(L))); tr = int(np.trace(L))
    if det == 1:
        return {3: 'E', -1: 'C2', 0: 'C3', 1: 'C4'}[tr]
    return {-3: 'i', 1: 'sigma', -1: 'S4', 0: 'S6'}[tr]


def gruppe48():
    g = []
    for M in td_gruppe():
        g.append(dict(M=M, inv=False, L=M, typ=element_typ(M), echt=int(round(np.linalg.det(M))) == 1))
        g.append(dict(M=M, inv=True, L=-M, typ='i*' + element_typ(-M), echt=False))
    return g


def transformiere(keys, el):
    xyz = kart(keys) @ el['M'].T
    if el['inv']:
        xyz = 1 - xyz
    return aus_kart(xyz)


def hid(b):
    return hashlib.sha256(b).hexdigest()[:16]


# ---------------------------------------------------------------- Gleiter
def richtung(dc):
    a = np.abs(np.asarray(dc, dtype=np.int64))
    g = int(np.gcd.reduce(a[a > 0])) if np.any(a > 0) else 1
    n = tuple(sorted((a // g).tolist()))
    if n == (1, 1, 1):
        neg = int(np.sum(np.asarray(dc) < 0))
        return '<111>', ('+e (Strichrichtung)' if neg % 2 == 0 else '-e (Gegenrichtung)')
    if n == (0, 0, 1):
        return '<100>', 'Wuerfelachse'
    if n == (0, 1, 1):
        return '<110>', 'Flaechendiagonale'
    return '<%d%d%d>' % (n[2], n[1], n[0]), 'andere'


def gleiter_aus(r, bmask, smask):
    """Phasen, Kennungen, Geschwindigkeit eines erkannten Gleiters (r aus lauf)."""
    p = r['p']; d = r['d']
    L = r['live']; ph = []
    for _ in range(p):
        ph.append(L)
        L = schritt(L, bmask, smask)
    formen = [form(x)[0] for x in ph]
    fL, aL = form(L)
    a0 = form(ph[0])[1]
    geprueft = (fL == formen[0]) and (tuple(aL[i] - a0[i] for i in range(3)) == tuple(d))
    k0 = min(range(p), key=lambda k: formen[k])
    ph = ph[k0:] + ph[:k0]; formen = formen[k0:] + formen[:k0]
    dc = (d[0] * A1 + d[1] * A2 + d[2] * A3).astype(np.int64)
    betrag = float(np.sqrt((dc ** 2).sum()))
    v_c = betrag / (p * W3)
    f_lk = max(float(np.abs(dc).sum()) / (2 * p), float(np.abs(dc).max()) / p)
    typ, art = richtung(dc)
    return dict(id=hid(formen[0]), p=int(p), d_prim=[int(x) for x in d], d_kart=[int(x) for x in dc],
                v_c=v_c, f_lichtkegel=f_lk, richtung=typ, richtung_art=art,
                zellen_min=int(min(x.size for x in ph)), zellen_max=int(max(x.size for x in ph)),
                geprueft=bool(geprueft), _phasen=ph, _formen=formen)


def phase_kart(keys):
    xyz = kart(keys)
    n1, n2, n3, s = dekodiere(keys)
    ref = kart(kodiere(n1.min(), n2.min(), n3.min(), 0))
    return (xyz - ref).tolist()


def drehverhalten(gl, alle, gruppe):
    """Bild jeder Symmetrie: derselbe Gleiter (Phasenversatz k), anderer gefundener Gleiter oder nicht gefunden."""
    dc = np.array(gl['d_kart'])
    eintr = []
    bahn = []
    for j, el in enumerate(gruppe):
        bild_ph = [transformiere(x, el) for x in gl['_phasen']]
        bf = [form(x)[0] for x in bild_ph]
        bahn.extend(bf)
        db = (el['L'] @ dc).tolist()
        f0 = bf[0]
        if f0 in gl['_formen']:
            k = gl['_formen'].index(f0)
            eintr.append(dict(el=j, typ=el['typ'], echt=el['echt'], bild='selbst', phasenversatz=int(k),
                              d_bild=db, d_gleich=bool(db == gl['d_kart'])))
        elif f0 in alle:
            eintr.append(dict(el=j, typ=el['typ'], echt=el['echt'], bild='anderer', gleiter=alle[f0], d_bild=db))
        else:
            eintr.append(dict(el=j, typ=el['typ'], echt=el['echt'], bild='nicht gefunden', d_bild=db))
    return eintr, hid(min(bahn))


# ---------------------------------------------------------------- Saaten
def startbereich(m=8):
    pts = np.array([(x, y, z) for x in range(m) for y in range(m) for z in range(m)])
    return aus_kart(pts[ist_knoten(pts)])


def saaten(P=PARAM, stufe=1):
    """Stufe 1: 48 Saaten im Bereich 2x2x2 Zellen. Stufe 2: 600 weitere (Saatindex 16..215) im Bereich 2x2x2,
    300 im Bereich 3x3x3 Zellen (216 Knoten) und 60 im Bereich 4x4x4 Zellen (512 Knoten), nach Lage verzahnt."""
    out = []
    if stufe == 1:
        keys = startbereich(8)
        for di, rho in enumerate(P['dichten']):
            for i in range(P['saaten_je_dichte']):
                rng = np.random.default_rng([P['saat_basis'], di, i])
                out.append((rho, i, keys[rng.random(keys.size) < rho], 2))
        return out
    k2 = startbereich(8); k3 = startbereich(12); k4 = startbereich(16)
    l2 = []; l3 = []; l4 = []
    for i in range(P['stufe2_saaten_2'] // 3):
        for di, rho in enumerate(P['dichten']):
            j = P['saaten_je_dichte'] + i
            rng = np.random.default_rng([P['saat_basis'], di, j])
            l2.append((rho, j, k2[rng.random(k2.size) < rho], 2))
    for i in range(P['stufe2_saaten_3'] // 3):
        for di, rho in enumerate(P['dichten']):
            rng = np.random.default_rng([P['saat_basis'], 100 + di, i])
            l3.append((rho, i, k3[rng.random(k3.size) < rho], 3))
    for i in range(P['stufe2_saaten_4'] // 3):
        for di, rho in enumerate(P['dichten']):
            rng = np.random.default_rng([P['saat_basis'], 200 + di, i])
            l4.append((rho, i, k4[rng.random(k4.size) < rho], 4))
    ls = [l2, l3, l4]
    lage = [((k + 0.5 * q) / len(l), q, k) for q, l in enumerate(ls) for k in range(len(l))]
    lage.sort()
    return [ls[q][k] for _, q, k in lage]


def stufe2_regeln():
    return [bm * 32 + sm for bm in (2, 4, 6, 8, 10, 12, 14) for sm in range(32)]


# ---------------------------------------------------------------- Suche je Regel
def suche_regel(idx, P=PARAM, start=None, zeitkappe=None, kompakt=False):
    t_anf = time.time()
    bmask, smask, name = regel_masken(idx)
    regel = (bmask, smask)
    cache = {}
    gleiter = {}
    zaehl = dict(objekt_laeufe=0)
    gids = set()

    def registriere(g, quelle):
        gids.add(g['id'])
        if g['id'] in gleiter:
            gleiter[g['id']]['funde'] += 1
        else:
            g['funde'] = 1; g['erste_quelle'] = quelle
            gleiter[g['id']] = g

    def objekt(cl, quelle):
        if cl.size > P['C_iso']:
            return 'objekt_zu_gross'
        f, _ = form(cl)
        if f not in cache:
            zaehl['objekt_laeufe'] += 1
            r = lauf(cl, regel, P['T_iso'], P['C_max'])
            if r['klasse'] == 'gleiter':
                cache[f] = ('gleiter', gleiter_aus(r, bmask, smask))
            else:
                cache[f] = (r['klasse'], None)
        kl, g = cache[f]
        if kl == 'gleiter':
            registriere(g, quelle)
        return kl

    saat_erg = []
    uebersprungen = 0
    for rho, i, live0, ber in (start if start is not None else saaten(P)):
        if zeitkappe is not None and time.time() - t_anf > zeitkappe:
            uebersprungen += 1
            continue
        obj = {}
        gids.clear()

        def pruefpunkt(live, t):
            cls = zerlege(live, P['R'])
            if len(cls) >= 2:
                for cl in cls:
                    kl = objekt(cl, dict(rho=rho, saat=i, bereich=ber, t=t, art='objekt'))
                    if kl == 'gleiter':
                        obj['gleiter_pruefpunkt'] = obj.get('gleiter_pruefpunkt', 0) + 1

        r = lauf(live0, regel, P['T'], P['C_max'], set(P['pruefpunkte']), pruefpunkt)
        ende = {}
        if r['klasse'] in ('gross', 'offen', 'gleiter'):
            cls = zerlege(r['live'], P['R'])
            if r['klasse'] == 'gleiter' and len(cls) == 1:
                registriere(gleiter_aus(r, bmask, smask), dict(rho=rho, saat=i, bereich=ber, t=r['t'], art='ganz'))
                ende['gleiter'] = 1
            elif r['klasse'] == 'gleiter' or len(cls) >= 2 or r['klasse'] == 'offen':
                for cl in cls:
                    kl = objekt(cl, dict(rho=rho, saat=i, bereich=ber, t=r['t'], art='objekt-ende'))
                    ende[kl] = ende.get(kl, 0) + 1
                if r['klasse'] == 'gleiter' and ende.get('gleiter', 0) == 0:
                    g = gleiter_aus(r, bmask, smask); g['zusammengesetzt'] = True
                    registriere(g, dict(rho=rho, saat=i, bereich=ber, t=r['t'], art='ganz-zusammengesetzt'))
        e = dict(rho=rho, saat=i, bereich=ber, klasse=r['klasse'], t=int(r['t']), zellen_ende=int(r['live'].size),
                 ende_objekte=ende)
        if 'p' in r:
            e['p'] = int(r['p']); e['d'] = [int(x) for x in r['d']]; e['t0'] = int(r['t0'])
        if obj:
            e['pruefpunkt'] = obj
        if gids:
            e['gleiter_ids'] = sorted(gids)
        saat_erg.append(e)

    # Drehverhalten und Bahnen
    gruppe = gruppe48()
    alle = {}
    for gid, g in gleiter.items():
        for f in g['_formen']:
            alle[f] = gid
    gl_out = []
    for gid, g in gleiter.items():
        eintr, bahn = drehverhalten(g, alle, gruppe)
        g['bahn_id'] = bahn
        g['symmetrie'] = eintr
        echt = [x for x in eintr if x['echt']]
        g['dreh12'] = dict(selbst=sum(x['bild'] == 'selbst' for x in echt),
                           anderer=sum(x['bild'] == 'anderer' for x in echt),
                           nicht_gefunden=sum(x['bild'] == 'nicht gefunden' for x in echt))
        g['halbe_periode_um_laufachse'] = [dict(el=x['el'], typ=x['typ'], echt=x['echt']) for x in eintr
                                           if x['bild'] == 'selbst' and x['typ'] not in ('E',) and x['d_gleich']
                                           and g['p'] % 2 == 0 and x['phasenversatz'] == g['p'] // 2]
        g['phasen_kart'] = [phase_kart(x) for x in g['_phasen']]
        g['phasen_s'] = [(x & 1).tolist() for x in g['_phasen']]
        g['regel'] = name; g['regel_index'] = idx
        gl_out.append({k: v for k, v in g.items() if not k.startswith('_')})

    kl_saat = [e['klasse'] for e in saat_erg]
    offen_unaufgeloest = any(e['klasse'] == 'offen' and any(k in ('offen', 'gross', 'objekt_zu_gross') for k in e['ende_objekte'])
                             for e in saat_erg)
    if gl_out:
        rk = 'Gleiter'
    elif 'gross' in kl_saat:
        rk = 'Wachstum'
    elif offen_unaufgeloest:
        rk = 'offen'
    elif 'osz' in kl_saat or any('osz' in e['ende_objekte'] for e in saat_erg):
        rk = 'Oszillator'
    elif 'still' in kl_saat or any('still' in e['ende_objekte'] for e in saat_erg):
        rk = 'Stilleben'
    else:
        rk = 'ausgestorben'
    zaehler = {k: kl_saat.count(k) for k in ('tot', 'still', 'osz', 'gleiter', 'gross', 'offen')}
    if kompakt:
        saat_erg = [e for e in saat_erg if 'gleiter_ids' in e]
    return dict(index=idx, name=name, B=[k for k in range(1, 5) if bmask[k]], S=[k for k in range(5) if smask[k]],
                klasse=rk, saat_klassen=zaehler, n_saaten=len(kl_saat), uebersprungen=uebersprungen,
                n_gleiter=len(gl_out), n_bahnen=len({g['bahn_id'] for g in gl_out}),
                objekt_laeufe=zaehl['objekt_laeufe'], zeit_s=round(time.time() - t_anf, 3), saaten=saat_erg, gleiter=gl_out)


# ---------------------------------------------------------------- Kontrollen (LD0)
def kontrolle():
    out = {}
    # (a) Gitter: kubischer periodischer Kasten L=3 (216 Knoten), Nachbarn per Abstand sqrt(3) a/4, Minimalbild
    L = 3; W = 4 * L
    pts = np.array([(x, y, z) for x in range(W) for y in range(W) for z in range(W)])
    pts = pts[ist_knoten(pts)]
    n = len(pts)
    dd = pts[:, None, :] - pts[None, :, :]
    dd = (dd + W // 2) % W - W // 2
    d2 = (dd ** 2).sum(-1)
    adj = d2 == 3
    grad = adj.sum(1)
    s = pts[:, 0] & 1
    kanten_ab = bool(np.all(s[np.nonzero(adj)[0]] != s[np.nonzero(adj)[1]]))
    farbe = -np.ones(n, dtype=int); farbe[0] = 0; queue = [0]; konflikt = 0
    while queue:
        u = queue.pop()
        for v in np.nonzero(adj[u])[0]:
            if farbe[v] < 0:
                farbe[v] = 1 - farbe[u]; queue.append(v)
            elif farbe[v] == farbe[u]:
                konflikt += 1
    keys = aus_kart(pts)
    xyz_k = kart(keys)
    abweich = 0
    for k, p0 in zip(keys, xyz_k):
        d = DA if (k & 1) == 0 else DB
        nbk = kart(np.int64(k) + d) % W
        expl = {tuple(x) for x in pts[adj[np.nonzero((pts == p0 % W).all(1))[0][0]]]}
        if {tuple(x) for x in nbk} != expl:
            abweich += 1
        vek = kart(np.int64(k) + d) - p0
        soll = E if (k & 1) == 0 else -E
        if {tuple(x) for x in vek} != {tuple(x) for x in soll}:
            abweich += 1
    out['a_gitter'] = dict(knoten=int(n), soll=8 * L ** 3, grad_min=int(grad.min()), grad_max=int(grad.max()),
                           kanten_nur_A_B=kanten_ab, bfs_konflikte=int(konflikt), bfs_farbe_gleich_untergitter=bool(
                               np.all(farbe == s) or np.all(farbe == 1 - s)), schluessel_abweichungen=int(abweich))
    out['a_ok'] = bool(n == 8 * L ** 3 and grad.min() == 4 and grad.max() == 4 and kanten_ab and konflikt == 0
                       and out['a_gitter']['bfs_farbe_gleich_untergitter'] and abweich == 0)
    # (b) B leer, S = {0..4}: jedes Muster bleibt fest
    idx = 0 * 32 + 31
    bmask, smask, name = regel_masken(idx)
    rng = np.random.default_rng(7)
    muster = [x[2] for x in saaten()] + [aus_kart(kart(startbereich())[rng.random(64) < 0.5] + 4 * np.array([1, 1, 0]))
                                         for _ in range(20)]
    fest = 0; klass_ok = 0
    for m in muster:
        L1 = m
        ok = True
        for _ in range(5):
            L2 = schritt(L1, bmask, smask)
            ok &= np.array_equal(L1, L2); L1 = L2
        fest += ok
        r = lauf(m, (bmask, smask), 10, 600)
        klass_ok += (r['klasse'] == 'still' and r['p'] == 1 and r['d'] == (0, 0, 0) and r['t'] == 1) or (m.size == 0 and r['klasse'] == 'tot')
    out['b_fest'] = dict(regel=name, muster=len(muster), fest=int(fest), einordnung_still=int(klass_ok))
    out['b_ok'] = bool(fest == len(muster) and klass_ok == len(muster))

    # (c) Kunstmuster: vorgegebene Folgen (Phasen, verschobene Kopien) -> Einordnung
    def zufall(rng, k=12):
        pts = kart(startbereich())
        return aus_kart(pts[rng.choice(len(pts), k, replace=False)])

    def verschiebe(keys, d):
        n1, n2, n3, s = dekodiere(keys)
        return np.sort(kodiere(n1 + d[0], n2 + d[1], n3 + d[2], s))

    faelle = []
    rng = np.random.default_rng(11)
    for (p, d, vorlauf) in [(3, (3, -1, 2), 0), (4, (0, 0, 0), 0), (1, (0, 0, 0), 0), (1, (1, 0, 0), 0),
                            (5, (0, -2, 1), 10), (2, (-1, -1, -1), 3), (7, (2, 2, -3), 5)]:
        ph = [zufall(rng, 8 + j) for j in range(p)]
        junk = [zufall(rng, 30 + j) for j in range(vorlauf)]

        def folge(Lx, t, ph=ph, p=p, d=d, junk=junk, vorlauf=vorlauf):
            if t < vorlauf:
                return junk[t]
            u = t - vorlauf
            return verschiebe(ph[u % p], tuple(c * (u // p) for c in d))

        st = junk[0] if vorlauf else ph[0]
        r = lauf(st, None, 100, 600, schritt_fn=folge)
        soll = 'gleiter' if d != (0, 0, 0) else ('still' if p == 1 else 'osz')
        faelle.append(dict(p=p, d=list(d), vorlauf=vorlauf, klasse=r['klasse'], p_erk=r.get('p'),
                           d_erk=list(r.get('d', ())), ok=bool(r['klasse'] == soll and r.get('p') == p and tuple(r.get('d', ())) == d)))
    # Verschiebungsfreiheit und Untergitter
    inv_ok = 0; unt_ok = 0
    for _ in range(100):
        m = zufall(rng, 10)
        t = rng.integers(-50, 50, 3)
        inv_ok += form(m)[0] == form(verschiebe(m, t))[0]
        mA = m[(m & 1) == 0]
        mB = aus_kart(kart(mA) + 1)
        unt_ok += form(mA)[0] != form(mB)[0]
    # Zerlegung
    m1 = zufall(rng, 15); m2 = verschiebe(zufall(rng, 15), (10, 10, 10))
    m3 = verschiebe(zufall(rng, 15), (1, 0, 0))
    z2 = len(zerlege(np.union1d(m1, m2), PARAM['R']))
    z1 = len(zerlege(np.union1d(m1, np.setdiff1d(m3, m1)), PARAM['R']))
    out['c_kunst'] = dict(faelle=faelle, verschiebung_invariant=int(inv_ok), untergitter_unterschieden=int(unt_ok),
                          zerlegung_getrennt=z2, zerlegung_nah=z1)
    out['c_ok'] = bool(all(f['ok'] for f in faelle) and inv_ok == 100 and unt_ok == 100 and z2 == 2 and z1 == 1)

    # (d) Zusatz: Gleichverhalten des echten Schritts unter Td x Inversion und fcc-Translation
    gruppe = gruppe48()
    fehler = 0; tests = 0
    for ridx in [0 * 32 + 0, 2 * 32 + 0, 3 * 32 + 6, 6 * 32 + 12, 4 * 32 + 31, 10 * 32 + 9, 15 * 32 + 21, 1 * 32 + 1]:
        bm, sm, _ = regel_masken(ridx)
        for _ in range(4):
            m = zufall(rng, 25)
            sm1 = schritt(m, bm, sm)
            for el in gruppe:
                tests += 1
                fehler += not np.array_equal(schritt(transformiere(m, el), bm, sm), transformiere(sm1, el))
            t = rng.integers(-20, 20, 3)
            tests += 1
            fehler += not np.array_equal(schritt(verschiebe(m, t), bm, sm), verschiebe(sm1, t))
    out['d_symmetrie'] = dict(gruppe=len(gruppe), echte=sum(g['echt'] for g in gruppe), tests=tests, fehler=int(fehler))
    out['d_ok'] = bool(fehler == 0 and len(gruppe) == 48)
    # (e) Zusatz: Lichtkegel B1234/S01234 aus einem Knoten: max(|x|+|y|+|z|) = 2t, max|x_i| = t bei geradem t
    bm, sm, _ = regel_masken(15 * 32 + 31)
    Lx = kodiere(0, 0, 0, 0)[None]
    lk = []
    for t in range(1, 9):
        Lx = schritt(Lx, bm, sm)
        if t % 2 == 0:
            xyz = kart(Lx)
            lk.append(dict(t=t, summe_max=int(np.abs(xyz).sum(1).max()), komp_max=int(np.abs(xyz).max()), zellen=int(Lx.size)))
    out['e_lichtkegel'] = lk
    out['e_ok'] = bool(all(x['summe_max'] == 2 * x['t'] and x['komp_max'] == x['t'] for x in lk))
    out['LD0_ok'] = bool(out['a_ok'] and out['b_ok'] and out['c_ok'])
    out['zusatz_ok'] = bool(out['d_ok'] and out['e_ok'])
    return out


def regelliste(arg):
    if '-' in arg:
        a, b = arg.split('-')
        return list(range(int(a), int(b)))
    return [int(x) for x in arg.split(',')]


def main():
    modus = sys.argv[1]
    t0 = time.time()
    if modus == 'kontrolle':
        out = kontrolle()
        out['param'] = PARAM; out['zeit_s'] = round(time.time() - t0, 2)
        json.dump(out, open(sys.argv[2], 'w'), indent=1)
        print(json.dumps({k: v for k, v in out.items() if k.endswith('ok')}), 'zeit', out['zeit_s'])
    elif modus in ('block', 'block2'):
        stufe = 1 if modus == 'block' else 2
        if stufe == 1:
            regeln = regelliste(sys.argv[2])
        else:
            liste = stufe2_regeln()
            regeln = [liste[k] for k in regelliste(sys.argv[2])]
        grenze = float(sys.argv[4]) if len(sys.argv) > 4 else 480.0
        st = saaten(stufe=stufe)
        kappe = PARAM['stufe2_zeitkappe_s'] if stufe == 2 else None
        with open(sys.argv[3], 'a') as fh:
            for idx in regeln:
                if time.time() - t0 > grenze:
                    print('zeitgrenze erreicht vor regel', idx, flush=True)
                    break
                r = suche_regel(idx, start=st, zeitkappe=kappe, kompakt=(stufe == 2))
                r['stufe'] = stufe
                fh.write(json.dumps(r) + '\n'); fh.flush()
                print(idx, r['name'], r['klasse'], r['saat_klassen'], 'gleiter', r['n_gleiter'], 'bahnen', r['n_bahnen'],
                      'obj', r['objekt_laeufe'], 'uebersp', r['uebersprungen'], 'zeit', r['zeit_s'], flush=True)
        print('block fertig', round(time.time() - t0, 1), 's', flush=True)


if __name__ == '__main__':
    main()
