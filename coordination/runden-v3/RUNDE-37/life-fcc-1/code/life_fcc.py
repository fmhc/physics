#!/usr/bin/env python3
# LIFE-FCC-1 (Runde 38): Gleitersuche in den 7098 Intervallregeln auf dem fcc-Gitter (12 Nachbarn).
# Code-Agent fuer die Leitung claude-primary. Laeuft nur auf der .69 ueber kleintest.sh (Spur cpu7), 1 Thread.
# Grundlage: RUNDE-37/life-diamant-1/code/life_diamant.py (unbegrenztes Gitter, Formkennung, Einordnung, Zerlegung,
# Gleiterpruefung, Drehverhalten). Hier: kartesische Knoten (x+y+z gerade), 12 Nachbarn, Saaten als Stapel
# (Saatnummer in den oberen Schluesselbits, ein numpy-Schritt fuer alle Saaten einer Regel).
# Aufruf:
#   life_fcc.py kontrolle <aus.json>
#   life_fcc.py stufe1 <aus.jsonl> <zeitgrenze_s> [regeln]      regeln: "a-b" (a..b-1) oder "i,j,k"; Standard alle
#   life_fcc.py stufe2 <stufe1.jsonl[,..]> <aus.jsonl> <zeitgrenze_s>
# Fortsetzung: bereits in <aus.jsonl> stehende Regelindizes werden uebersprungen.
# Regelindex = bi*91 + si; bi zaehlt B = [b1..b2] (b1 = 1..12, b2 = b1..12), si zaehlt S = [s1..s2] (s1 = 0..12, s2 = s1..12).
import sys, json, time, itertools, math, hashlib, os
import numpy as np
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

PARAM = dict(T=256, C_max=600, T_iso=128, C_iso=300, R=4.5, pruefpunkte=[64, 128, 192], klein=200, t_klein=8,
             m1=5, dichten=[0.15, 0.3, 0.45, 0.6], saaten_je_dichte=6, saat_basis=380441,
             W1=1500000, W1_obj=600000, max_obj=400,
             m2=[5, 7, 9], n2=[48, 32, 16], W2=6000000, W2_obj=1500000, N2_max=None)

# ---------------------------------------------------------------- Gitter
# Knoten: ganzzahlige (x, y, z) mit gerader Summe (Einheit a/2, a = kubische Zellkante). 12 Nachbarn (+-1, +-1, 0) und
# Vertauschungen. Schluessel: (saat << 48) | (x+OFF) << 32 | (y+OFF) << 16 | (z+OFF).
BITS = 16
OFF = 1 << (BITS - 1)
MASK = (1 << BITS) - 1
SH = 3 * BITS
NB = np.array([v for v in itertools.product((-1, 0, 1), repeat=3) if sum(abs(c) for c in v) == 2], dtype=np.int64)
OFFS = NB[:, 0] * (1 << (2 * BITS)) + NB[:, 1] * (1 << BITS) + NB[:, 2]
W2R = math.sqrt(2.0)
KL = ['tot', 'still', 'osz', 'gleiter', 'gross', 'offen']


def kodiere(x, y, z, sid=0):
    x = np.asarray(x, dtype=np.int64); y = np.asarray(y, dtype=np.int64); z = np.asarray(z, dtype=np.int64)
    s = np.asarray(sid, dtype=np.int64)
    return (s << SH) | ((x + OFF) << (2 * BITS)) | ((y + OFF) << BITS) | (z + OFF)


def dekodiere(k):
    k = np.asarray(k, dtype=np.int64)
    return ((k >> (2 * BITS)) & MASK) - OFF, ((k >> BITS) & MASK) - OFF, (k & MASK) - OFF, k >> SH


def kart(k):
    x, y, z, _ = dekodiere(k)
    return np.stack([x, y, z], axis=-1)


def ist_knoten(xyz):
    xyz = np.asarray(xyz, dtype=np.int64)
    return (xyz.sum(axis=-1) % 2) == 0


def aus_kart(xyz, sid=0):
    xyz = np.asarray(xyz, dtype=np.int64).reshape(-1, 3)
    if not np.all(ist_knoten(xyz)):
        raise ValueError('kein fcc-Knoten')
    return np.unique(kodiere(xyz[:, 0], xyz[:, 1], xyz[:, 2], sid))


B_INT = [(b1, b2) for b1 in range(1, 13) for b2 in range(b1, 13)]
S_INT = [(s1, s2) for s1 in range(0, 13) for s2 in range(s1, 13)]
NREG = len(B_INT) * len(S_INT)


def intname(a, b):
    return str(a) if a == b else '%d-%d' % (a, b)


def regel_masken(idx):
    """idx 0..7097: Intervallregeln der Karte. idx 7098..7175: Zusatz (nicht geurteilt), B-Intervall bi = idx - 7098
    mit S leer ("Seeds"-Typ); dort ist (s1, s2) = (-1, -1)."""
    idx = int(idx)
    if idx >= NREG:
        (b1, b2) = B_INT[idx - NREG]
        bm = np.zeros(13, dtype=bool); bm[b1:b2 + 1] = True
        return bm, np.zeros(13, dtype=bool), 'B%s/S' % intname(b1, b2), (b1, b2, -1, -1)
    bi, si = divmod(idx, len(S_INT))
    (b1, b2), (s1, s2) = B_INT[bi], S_INT[si]
    bm = np.zeros(13, dtype=bool); bm[b1:b2 + 1] = True
    sm = np.zeros(13, dtype=bool); sm[s1:s2 + 1] = True
    return bm, sm, 'B%s/S%s' % (intname(b1, b2), intname(s1, s2)), (b1, b2, s1, s2)


def regel_index(b1, b2, s1, s2):
    return B_INT.index((b1, b2)) * len(S_INT) + S_INT.index((s1, s2))


def schritt(live, bmask, smask):
    """Ein synchroner Schritt (aussen-totalistisch). live: sortiertes, eindeutiges int64-Array (auch Stapel)."""
    if live.size == 0:
        return live
    nb = (OFFS[:, None] + live[None, :]).ravel()
    nb.sort()
    neu = np.empty(nb.size, dtype=bool); neu[0] = True
    np.not_equal(nb[1:], nb[:-1], out=neu[1:])
    st = np.flatnonzero(neu)
    keys = nb[st]
    cnt = np.diff(np.append(st, nb.size))
    pos = np.minimum(np.searchsorted(keys, live), keys.size - 1)
    cl = np.where(keys[pos] == live, cnt[pos], 0)
    surv = live[smask[cl]]
    posl = np.minimum(np.searchsorted(live, keys), live.size - 1)
    born = keys[(live[posl] != keys) & bmask[cnt]]
    out = np.concatenate((surv, born)); out.sort()
    return out


def regel_fn(idx):
    bm, sm, name, _ = regel_masken(idx)
    return (lambda L, t=None: schritt(L, bm, sm)), name


def form(live):
    """Verschiebungsfreie Kennung (Bezugsecke = komponentenweises Minimum) und Bezugsecke (Rohfelder)."""
    u1 = (live >> (2 * BITS)) & MASK; u2 = (live >> BITS) & MASK; u3 = live & MASK
    m1, m2, m3 = int(u1.min()), int(u2.min()), int(u3.min())
    sid = int(live[0] >> SH)
    shift = (sid << SH) | (m1 << (2 * BITS)) | (m2 << BITS) | m3
    return (live - np.int64(shift)).tobytes(), (m1, m2, m3)


# ---------------------------------------------------------------- Laeufe als Stapel
def lauf_stapel(muster, sf, T, cmax, pruef=(), beim_pruefpunkt=None, budget=None):
    """Alle Muster (Schluessel mit Saat 0) gleichzeitig. Abbruch je Muster bei tot, gross (> cmax), Formwiederkehr;
    sonst offen bei T. budget: Knotenschritte (Summe der lebenden Knoten ueber die Schritte); danach offen (gekappt)."""
    n = len(muster)
    assert n < 16000
    erg = [None] * n
    teile = []; aktiv = []; seen = {}
    for i, m in enumerate(muster):
        if m.size == 0:
            erg[i] = dict(klasse='tot', t=0, live=m)
            continue
        mm = m + (np.int64(i) << SH)
        teile.append(mm); aktiv.append(i)
        f, anc = form(mm)
        seen[i] = {f: (0, anc)}
    live = np.sort(np.concatenate(teile)) if teile else np.empty(0, dtype=np.int64)
    aktiv = np.array(aktiv, dtype=np.int64)
    arbeit = 0; t = 0; gekappt = False
    pruef = set(pruef)
    while aktiv.size and t < T:
        t += 1
        live = sf(live, t)
        arbeit += int(live.size)
        lo = np.searchsorted(live, aktiv << SH); hi = np.searchsorted(live, (aktiv + 1) << SH)
        ne = hi > lo
        mins = None
        if np.any(ne):
            ix = lo[ne]
            u1 = (live >> (2 * BITS)) & MASK; u2 = (live >> BITS) & MASK; u3 = live & MASK
            m1 = np.minimum.reduceat(u1, ix); m2 = np.minimum.reduceat(u2, ix); m3 = np.minimum.reduceat(u3, ix)
            sh = (aktiv[ne] << SH) | (m1 << (2 * BITS)) | (m2 << BITS) | m3
            mins = dict(zip(aktiv[ne].tolist(), zip(sh.tolist(), m1.tolist(), m2.tolist(), m3.tolist())))
        fertig = []
        for j in range(aktiv.size):
            i = int(aktiv[j]); a, b = int(lo[j]), int(hi[j])
            if a == b:
                erg[i] = dict(klasse='tot', t=t, live=np.empty(0, dtype=np.int64)); fertig.append(i); continue
            seg = live[a:b]
            if b - a > cmax:
                erg[i] = dict(klasse='gross', t=t, live=seg - (np.int64(i) << SH)); fertig.append(i); continue
            shv, c1, c2, c3 = mins[i]
            f = (seg - np.int64(shv)).tobytes(); anc = (c1, c2, c3)
            s = seen[i]
            if f in s:
                t0, a0 = s[f]
                d = (anc[0] - a0[0], anc[1] - a0[1], anc[2] - a0[2])
                kl = 'gleiter' if d != (0, 0, 0) else ('still' if t - t0 == 1 else 'osz')
                erg[i] = dict(klasse=kl, t=t, t0=t0, p=t - t0, d=d, live=seg - (np.int64(i) << SH))
                fertig.append(i); continue
            s[f] = (t, anc)
            if beim_pruefpunkt is not None and t in pruef:
                beim_pruefpunkt(i, seg - (np.int64(i) << SH), t)
        if fertig:
            fa = np.array(fertig, dtype=np.int64)
            live = live[~np.isin(live >> SH, fa)]
            aktiv = aktiv[~np.isin(aktiv, fa)]
            for i in fertig:
                seen.pop(i, None)
        if budget is not None and arbeit > budget and aktiv.size and t < T:
            gekappt = True
            break
    if aktiv.size:
        lo = np.searchsorted(live, aktiv << SH); hi = np.searchsorted(live, (aktiv + 1) << SH)
        for j in range(aktiv.size):
            i = int(aktiv[j])
            erg[i] = dict(klasse='offen', t=t, live=live[int(lo[j]):int(hi[j])] - (np.int64(i) << SH), gekappt=gekappt)
    return erg, arbeit, gekappt


def zerlege(live, R=None):
    R = PARAM['R'] if R is None else R
    if live.size == 0:
        return []
    xyz = kart(live).astype(float)
    pairs = cKDTree(xyz).query_pairs(R, output_type='ndarray')
    k = live.size
    if len(pairs) == 0:
        return [live[i:i + 1] for i in range(k)]
    g = coo_matrix((np.ones(len(pairs)), (pairs[:, 0], pairs[:, 1])), shape=(k, k))
    nc, lab = connected_components(g, directed=False)
    return [live[lab == c] for c in range(nc)]


# ---------------------------------------------------------------- Symmetrie (Oh, 48 Elemente)
TETRA = {(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)}


def element_typ(M):
    det = int(round(np.linalg.det(M))); tr = int(np.trace(M))
    diag = bool(np.count_nonzero(M - np.diag(np.diag(M))) == 0)
    if det == 1:
        return {3: 'E', -1: 'C2' if diag else "C2'", 0: 'C3', 1: 'C4'}[tr]
    return {-3: 'i', 1: 'sigma_h' if diag else 'sigma_d', -1: 'S4', 0: 'S6'}[tr]


def oh_gruppe():
    out = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3), dtype=np.int64)
        for i, j in enumerate(perm):
            P[i, j] = 1
        for sg in itertools.product([1, -1], repeat=3):
            M = np.diag(sg) @ P
            det = int(round(np.linalg.det(M)))
            in_T = det == 1 and {tuple(M @ np.array(e)) for e in TETRA} == TETRA
            out.append(dict(M=M, det=det, typ=element_typ(M), echt=det == 1, in_T=bool(in_T)))
    return out


GRUPPE48 = oh_gruppe()


def transformiere(keys, M):
    return aus_kart(kart(keys) @ np.asarray(M).T)


def hid(b):
    return hashlib.sha256(b).hexdigest()[:16]


# ---------------------------------------------------------------- Gleiter
def richtung(dc):
    a = np.abs(np.asarray(dc, dtype=np.int64))
    g = int(np.gcd.reduce(a[a > 0])) if np.any(a > 0) else 1
    n = tuple(sorted((a // g).tolist()))
    if n == (0, 1, 1):
        return '<110>', 'Nachbarrichtung'
    if n == (0, 0, 1):
        return '<100>', 'Wuerfelachse'
    if n == (1, 1, 1):
        return '<111>', 'Raumdiagonale'
    return '<%d%d%d>' % (n[2], n[1], n[0]), 'andere'


def lichtkegel_f(dc, p):
    dc = np.abs(np.asarray(dc, dtype=np.int64))
    return max(float(dc.sum()) / (2 * p), float(dc.max()) / p)


def gleiter_aus(r, sf):
    """Phasen, Kennungen, Geschwindigkeit eines erkannten Gleiters (r aus lauf_stapel, Schluessel mit Saat 0)."""
    p = int(r['p']); d = tuple(int(x) for x in r['d'])
    L = r['live']; ph = []
    for _ in range(p):
        ph.append(L)
        L = sf(L, None)
    formen = [form(x)[0] for x in ph]
    fL, aL = form(L) if L.size else (b'', (0, 0, 0))
    a0 = form(ph[0])[1]
    geprueft = bool(fL == formen[0] and tuple(aL[i] - a0[i] for i in range(3)) == d)
    k0 = min(range(p), key=lambda k: formen[k])
    ph = ph[k0:] + ph[:k0]; formen = formen[k0:] + formen[:k0]
    dc = np.array(d, dtype=np.int64)
    betrag = float(np.sqrt((dc ** 2).sum()))
    v_c = betrag / (p * W2R)
    f_lk = lichtkegel_f(dc, p)
    typ, art = richtung(dc)
    return dict(id=hid(formen[0]), p=p, d=list(d), v_c=v_c, f_lichtkegel=f_lk,
                v_grenze_c=(v_c / f_lk) if f_lk > 0 else None, richtung=typ, richtung_art=art,
                zellen_min=int(min(x.size for x in ph)), zellen_max=int(max(x.size for x in ph)),
                geprueft=geprueft, _phasen=ph, _formen=formen)


def phase_kart(keys):
    xyz = kart(keys)
    return (xyz - xyz.min(axis=0)).tolist()


def drehverhalten(gl, alle, gruppe):
    dc = np.array(gl['d'])
    eintr = []; bahn = []
    for j, el in enumerate(gruppe):
        bild_ph = [transformiere(x, el['M']) for x in gl['_phasen']]
        bf = [form(x)[0] for x in bild_ph]
        bahn.extend(bf)
        db = (el['M'] @ dc).tolist()
        f0 = bf[0]
        if f0 in gl['_formen']:
            k = gl['_formen'].index(f0)
            eintr.append(dict(el=j, typ=el['typ'], echt=el['echt'], in_T=el['in_T'], bild='selbst', phasenversatz=int(k),
                              d_bild=db, d_gleich=bool(db == gl['d'])))
        elif f0 in alle:
            eintr.append(dict(el=j, typ=el['typ'], echt=el['echt'], in_T=el['in_T'], bild='anderer', gleiter=alle[f0],
                              d_bild=db))
        else:
            eintr.append(dict(el=j, typ=el['typ'], echt=el['echt'], in_T=el['in_T'], bild='nicht gefunden', d_bild=db))
    return eintr, hid(min(bahn))


# ---------------------------------------------------------------- Saaten
def bereich(m):
    pts = np.array([(x, y, z) for x in range(m) for y in range(m) for z in range(m)], dtype=np.int64)
    return aus_kart(pts[ist_knoten(pts)])


def saaten(stufe=1, P=PARAM):
    out = []
    if stufe == 1:
        keys = bereich(P['m1'])
        for di, rho in enumerate(P['dichten']):
            for i in range(P['saaten_je_dichte']):
                rng = np.random.default_rng([P['saat_basis'], di, i])
                out.append((rho, i, keys[rng.random(keys.size) < rho], P['m1']))
        return out
    for q, (m, n) in enumerate(zip(P['m2'], P['n2'])):
        keys = bereich(m)
        for i in range(n // len(P['dichten'])):
            for di, rho in enumerate(P['dichten']):
                rng = np.random.default_rng([P['saat_basis'], 1000 + 100 * q + di, i])
                out.append((rho, i, keys[rng.random(keys.size) < rho], m))
    return out


# ---------------------------------------------------------------- Suche je Regel
def suche_regel(idx, start, W, W_obj, sf=None, name=None, P=PARAM, voll=False):
    t_anf = time.time()
    if sf is None:
        sf, name = regel_fn(idx)
    queue = {}; refs = {}
    zaehl = dict(zu_gross=0, obj_verworfen=0)

    def reg_objekt(i, cl, art, t):
        if cl.size > P['C_iso']:
            refs.setdefault(i, []).append((None, art, t)); return
        f, _ = form(cl)
        if f not in queue:
            if len(queue) >= P['max_obj']:
                refs.setdefault(i, []).append(('verworfen', art, t)); return
            queue[f] = cl
        refs.setdefault(i, []).append((f, art, t))

    def pruefpunkt(i, live, t):
        cls = zerlege(live)
        if len(cls) >= 2:
            for cl in cls:
                reg_objekt(i, cl, 'objekt', t)

    erg, arbeit, gekappt = lauf_stapel([s[2] for s in start], sf, P['T'], P['C_max'], P['pruefpunkte'], pruefpunkt, W)
    ganz = {}
    for i, r in enumerate(erg):
        if r['klasse'] in ('offen', 'gleiter'):  # [F] gross-Enden werden nicht zerlegt (Laufzeit, PLAN 4)
            cls = zerlege(r['live'])
            if r['klasse'] == 'gleiter' and len(cls) == 1:
                ganz[i] = 'einzeln'
            elif r['klasse'] == 'gleiter' or len(cls) >= 2 or r['klasse'] == 'offen':
                for cl in cls:
                    reg_objekt(i, cl, 'objekt-ende', r['t'])
                if r['klasse'] == 'gleiter':
                    ganz[i] = 'zusammengesetzt?'
    of = list(queue.keys())
    if of:
        oerg, oarbeit, ogekappt = lauf_stapel([queue[f] for f in of], sf, P['T_iso'], P['C_max'], budget=W_obj)
    else:
        oerg, oarbeit, ogekappt = [], 0, False
    okl = {}
    gleiter = {}

    def registriere(g, quelle):
        if g['id'] in gleiter:
            gleiter[g['id']]['funde'] += 1
        else:
            g['funde'] = 1; g['erste_quelle'] = quelle
            gleiter[g['id']] = g
        return g['id']

    gl_obj = {}
    for f, r in zip(of, oerg):
        if r['klasse'] == 'gleiter':
            g = gleiter_aus(r, sf)
            gl_obj[f] = g
            okl[f] = 'gleiter'
        elif r['klasse'] == 'offen' and r.get('gekappt'):
            okl[f] = 'gekappt'
        else:
            okl[f] = r['klasse']
    saat_out = []
    obj_klassen = {}
    for i, r in enumerate(erg):
        rho, si, live0, ber = start[i]
        gids = set(); ende = {}; pp = 0
        for f, art, t in refs.get(i, []):
            if f is None:
                kl = 'zu_gross'
            elif f == 'verworfen':
                kl = 'verworfen'
            else:
                kl = okl[f]
            if art == 'objekt-ende':
                ende[kl] = ende.get(kl, 0) + 1
            obj_klassen[kl] = obj_klassen.get(kl, 0) + 1
            if kl == 'gleiter':
                gids.add(registriere(gl_obj[f], dict(rho=rho, saat=si, bereich=ber, t=t, art=art)))
                if art == 'objekt':
                    pp += 1
        if ganz.get(i) == 'einzeln':
            gids.add(registriere(gleiter_aus(r, sf), dict(rho=rho, saat=si, bereich=ber, t=r['t'], art='ganz')))
        elif ganz.get(i) == 'zusammengesetzt?' and ende.get('gleiter', 0) == 0:
            g = gleiter_aus(r, sf); g['zusammengesetzt'] = True
            gids.add(registriere(g, dict(rho=rho, saat=si, bereich=ber, t=r['t'], art='ganz-zusammengesetzt')))
        e = dict(k=KL.index(r['klasse']), t=int(r['t']), n=int(r['live'].size), p=int(r.get('p', 0)),
                 ende=ende, gl=sorted(gids), pp=pp, gekappt=bool(r.get('gekappt', False)))
        if r['klasse'] == 'gleiter':
            e['d'] = [int(x) for x in r['d']]
        saat_out.append(e)
    # Drehverhalten und Bahnen
    gruppe = GRUPPE48
    alle = {}
    for gid, g in gleiter.items():
        for f in g['_formen']:
            alle[f] = gid
    gl_out = []
    for gid, g in gleiter.items():
        eintr, bahn = drehverhalten(g, alle, gruppe)
        g['bahn_id'] = bahn
        g['symmetrie'] = eintr
        for nm, sel in (('dreh24', lambda x: x['echt']), ('dreh12_T', lambda x: x['in_T']), ('alle48', lambda x: True)):
            sub = [x for x in eintr if sel(x)]
            g[nm] = dict(selbst=sum(x['bild'] == 'selbst' for x in sub),
                         selbst_d_gleich=sum(x['bild'] == 'selbst' and x['d_gleich'] for x in sub),
                         anderer=sum(x['bild'] == 'anderer' for x in sub),
                         nicht_gefunden=sum(x['bild'] == 'nicht gefunden' for x in sub))
        g['stabilisator'] = [dict(el=x['el'], typ=x['typ'], phasenversatz=x['phasenversatz']) for x in eintr
                             if x['bild'] == 'selbst' and x['d_gleich']]
        g['bahn_groesse'] = 48 // max(1, len(g['stabilisator']))
        g['halbe_periode_um_laufachse'] = [dict(el=x['el'], typ=x['typ'], echt=x['echt']) for x in eintr
                                           if x['bild'] == 'selbst' and x['typ'] != 'E' and x['d_gleich']
                                           and g['p'] % 2 == 0 and x['phasenversatz'] == g['p'] // 2]
        g['phasen_kart'] = [phase_kart(x) for x in g['_phasen']]
        g['regel'] = name; g['regel_index'] = int(idx)
        gl_out.append({k: v for k, v in g.items() if not k.startswith('_')})
    kl_saat = [KL[e['k']] for e in saat_out]
    offen_unaufg = any(KL[e['k']] == 'offen' and (e['gekappt'] or any(k in ('offen', 'gross', 'zu_gross', 'gekappt', 'verworfen')
                                                                  for k in e['ende'])) for e in saat_out)
    if gl_out:
        rk = 'Gleiter'
    elif 'gross' in kl_saat:
        rk = 'Wachstum'
    elif offen_unaufg:
        rk = 'offen'
    elif 'osz' in kl_saat or obj_klassen.get('osz', 0):
        rk = 'Oszillator'
    elif 'still' in kl_saat or obj_klassen.get('still', 0):
        rk = 'Stilleben'
    else:
        rk = 'ausgestorben'
    zaehler = {k: kl_saat.count(k) for k in KL}
    perioden = {}
    for e in saat_out:
        if KL[e['k']] == 'osz':
            perioden[str(e['p'])] = perioden.get(str(e['p']), 0) + 1
    score = sum(1 for e in saat_out if KL[e['k']] in ('still', 'osz', 'offen', 'gleiter') and e['n'] <= P['klein']
                and e['t'] >= P['t_klein'])
    out = dict(index=int(idx), name=name, klasse=rk, saat_klassen=zaehler, n_saaten=len(saat_out), score=score,
               perioden=perioden, max_ende=max([e['n'] for e in saat_out if KL[e['k']] != 'gross'] or [0]),
               gekappt=bool(gekappt), arbeit=int(arbeit), objekt_laeufe=len(of), objekt_arbeit=int(oarbeit),
               objekt_gekappt=bool(ogekappt), objekt_klassen=obj_klassen, n_gleiter=len(gl_out),
               n_bahnen=len({g['bahn_id'] for g in gl_out}), zeit_s=round(time.time() - t_anf, 3), gleiter=gl_out)
    if voll:
        out['saaten'] = saat_out
    else:
        out['saaten'] = [[e['k'], e['t'], e['n'], e['p'], len(e['gl'])] for e in saat_out]
    if idx is not None and idx >= 0:
        out['b'] = list(regel_masken(idx)[3][:2]); out['s'] = list(regel_masken(idx)[3][2:])
    return out


# ---------------------------------------------------------------- Kontrollen (LF0 und Zusatz)
def verschiebe(keys, d):
    x, y, z, s = dekodiere(keys)
    return np.sort(kodiere(x + d[0], y + d[1], z + d[2], s))


def kunst_schritt(R, tv, zgrenze=1000):
    """Kunst-Schritt fuer die Durchgangsprobe: Knoten mit z < zgrenze gehen auf R x + t (R, t fcc-erhaltend), die
    anderen bleiben stehen. Haengt nur von der Lage ab, nicht von der Zeit."""
    R = np.asarray(R, dtype=np.int64); tv = np.asarray(tv, dtype=np.int64)

    def sf(live, t=None):
        if live.size == 0:
            return live
        x, y, z, sid = dekodiere(live)
        xyz = np.stack([x, y, z], axis=-1)
        lauf = z < zgrenze
        neu = xyz.copy()
        neu[lauf] = xyz[lauf] @ R.T + tv
        return np.unique(kodiere(neu[:, 0], neu[:, 1], neu[:, 2], sid))
    return sf


def kontrolle():
    out = {}
    # (a) Gitter: periodischer kubischer Kasten W = 8 (4 Zellen je Kante, 4 L^3 = 256 Knoten), Nachbarn per Abstand
    W = 8
    pts = np.array([(x, y, z) for x in range(W) for y in range(W) for z in range(W)], dtype=np.int64)
    pts = pts[ist_knoten(pts)]
    n = len(pts)
    dd = pts[:, None, :] - pts[None, :, :]
    dd = (dd + W // 2) % W - W // 2
    adj = (dd ** 2).sum(-1) == 2
    grad = adj.sum(1)
    keys = aus_kart(pts)
    xyz_k = kart(keys)
    abweich = 0
    for k, p0 in zip(keys, xyz_k):
        nbk = kart(np.int64(k) + OFFS)
        i0 = np.nonzero((pts == p0 % W).all(1))[0][0]
        if {tuple(x) for x in (nbk % W)} != {tuple(x) for x in pts[adj[i0]]}:
            abweich += 1
        if {tuple(x) for x in (nbk - p0)} != {tuple(x) for x in NB}:
            abweich += 1
        if not np.all(ist_knoten(nbk)):
            abweich += 1
    # Schalen und Graphabstand im unbegrenzten Gitter (Wuerfel [-6, 6]^3)
    q = np.array([(x, y, z) for x in range(-6, 7) for y in range(-6, 7) for z in range(-6, 7)], dtype=np.int64)
    q = q[ist_knoten(q)]
    r2 = (q ** 2).sum(1)
    schalen = {int(s): int((r2 == s).sum()) for s in (2, 4, 6, 8)}
    dist = {(0, 0, 0): 0}; front = [(0, 0, 0)]
    for t in range(1, 5):
        nf = []
        for v in front:
            for e in NB.tolist():
                w = (v[0] + e[0], v[1] + e[1], v[2] + e[2])
                if w not in dist:
                    dist[w] = t; nf.append(w)
        front = nf
    knorm = lambda v: max((abs(v[0]) + abs(v[1]) + abs(v[2])) // 2, max(abs(v[0]), abs(v[1]), abs(v[2])))
    bfs_fehler = sum(1 for v, t in dist.items() if knorm(v) != t)
    soll4 = sum(1 for v in q.tolist() if knorm(v) <= 4)
    out['a_gitter'] = dict(knoten=int(n), soll=4 * (W // 2) ** 3, grad_min=int(grad.min()), grad_max=int(grad.max()),
                           nachbarn_je_knoten=int(len(OFFS)), schluessel_abweichungen=int(abweich), schalen=schalen,
                           bfs_knoten_bis_4=len(dist), soll_knorm_bis_4=int(soll4), bfs_fehler=int(bfs_fehler))
    out['a_ok'] = bool(n == 256 and grad.min() == 12 and grad.max() == 12 and len(OFFS) == 12 and abweich == 0
                       and schalen == {2: 12, 4: 6, 6: 24, 8: 12} and bfs_fehler == 0 and len(dist) == soll4)

    # (b) Kunstfolgen: vorgegebene Phasen, je Periode um d verschobene Kopie -> Einordnung
    rng = np.random.default_rng(11)

    def zufall(rng, k=12):
        b = kart(bereich(5))
        return aus_kart(b[rng.choice(len(b), k, replace=False)])

    faelle = []
    for (p, d, vorlauf) in [(3, (3, -1, 2), 0), (4, (0, 0, 0), 0), (1, (0, 0, 0), 0), (1, (1, 1, 0), 0),
                            (5, (0, -2, 2), 10), (2, (-1, -1, 0), 3), (7, (2, 2, -2), 5)]:
        ph = [zufall(rng, 8 + j) for j in range(p)]
        junk = [zufall(rng, 30 + j) for j in range(vorlauf)]

        def folge(Lx, t, ph=ph, p=p, d=d, junk=junk, vorlauf=vorlauf):
            if t < vorlauf:
                return junk[t]
            u = t - vorlauf
            return verschiebe(ph[u % p], tuple(c * (u // p) for c in d))

        st = junk[0] if vorlauf else ph[0]
        r = lauf_stapel([st], folge, 100, 600)[0][0]
        soll = 'gleiter' if d != (0, 0, 0) else ('still' if p == 1 else 'osz')
        faelle.append(dict(p=p, d=list(d), vorlauf=vorlauf, klasse=r['klasse'], p_erk=r.get('p'),
                           d_erk=list(r.get('d', ())), ok=bool(r['klasse'] == soll and r.get('p') == p
                                                             and tuple(r.get('d', ())) == d)))
    inv_ok = 0
    for _ in range(100):
        m = zufall(rng, 10)
        tv = rng.integers(-50, 50, 3); tv[2] += int(tv.sum() % 2)
        inv_ok += form(m)[0] == form(verschiebe(m, tv))[0]
    m1 = zufall(rng, 15); m2 = verschiebe(zufall(rng, 15), (10, 10, 10))
    m3 = verschiebe(zufall(rng, 15), (1, 1, 0))
    z2 = len(zerlege(np.union1d(m1, m2)))
    z1 = len(zerlege(np.union1d(m1, m3)))
    out['b_kunstfolgen'] = dict(faelle=faelle, verschiebung_invariant=int(inv_ok), zerlegung_getrennt=z2, zerlegung_nah=z1)
    out['b_ok'] = bool(all(f['ok'] for f in faelle) and inv_ok == 100 and z2 == 2 and z1 == 1)

    # (c) Durchgangsprobe der ganzen Gleiterkette mit Kunst-Schritten (Kunst-Gleiter = je Schritt R x + t)
    typen = [('p1_110', np.eye(3, dtype=np.int64), (1, 1, 0), 1, (1, 1, 0), '<110>'),
             ('p3_111', np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]), (1, 1, 0), 3, (2, 2, 2), '<111>'),
             ('p4_100', np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]), (1, 0, 1), 4, (0, 0, 4), '<100>')]
    s1 = saaten(1)
    dicht = [s for s in s1 if s[0] == PARAM['dichten'][-1]]
    block = verschiebe(bereich(4), (0, 0, 2000))
    probe = []
    for nm, R, tv, p_soll, d_soll, r_soll in typen:
        sf = kunst_schritt(R, tv)
        start = [dicht[0]]
        for k in (1, 2, 3):
            rho, i, live0, ber = dicht[k]
            start.append((rho, i, np.union1d(live0, block), ber))
        r = suche_regel(-1, start, PARAM['W1'], PARAM['W1_obj'], sf=sf, name='Kunst-' + nm, voll=True)
        ok_gl = [g for g in r['gleiter'] if g['p'] == p_soll and tuple(g['d']) == d_soll and g['richtung'] == r_soll
                 and g['geprueft'] and abs(g['f_lichtkegel'] - 1.0) < 1e-12]
        arten = sorted({g['erste_quelle']['art'] for g in r['gleiter']})
        je_saat = [len(e['gl']) for e in r['saaten']]
        ok = bool(r['n_gleiter'] >= 1 and len(ok_gl) == r['n_gleiter'] and all(x >= 1 for x in je_saat)
                  and 'ganz' in arten and 'objekt' in arten)
        probe.append(dict(typ=nm, p_soll=p_soll, d_soll=list(d_soll), richtung_soll=r_soll, n_gleiter=r['n_gleiter'],
                          mit_erwartung=len(ok_gl), gleiter_je_saat=je_saat, quellen_arten=arten,
                          saat_klassen=r['saat_klassen'], v_c=[g['v_c'] for g in r['gleiter']],
                          dreh24=[g['dreh24'] for g in r['gleiter']], ok=ok))
    out['c_durchgangsprobe'] = probe
    out['c_ok'] = bool(all(x['ok'] for x in probe))

    # (d) Zusatz: Gleichverhalten unter Oh (48) und fcc-Verschiebungen; Stapel = Einzellaeufe
    gruppe = oh_gruppe()
    fehler = 0; tests = 0
    regeln_d = [regel_index(1, 12, 0, 12), regel_index(2, 2, 0, 0), regel_index(3, 4, 2, 5), regel_index(4, 4, 3, 4),
                regel_index(5, 7, 4, 8), regel_index(6, 12, 0, 3), regel_index(2, 3, 1, 1), regel_index(12, 12, 12, 12)]
    for ridx in regeln_d:
        sf, _ = regel_fn(ridx)
        for _ in range(4):
            m = zufall(rng, 25)
            sm1 = sf(m)
            for el in gruppe:
                tests += 1
                fehler += not np.array_equal(sf(transformiere(m, el['M'])), transformiere(sm1, el['M']))
            tv = rng.integers(-20, 20, 3); tv[2] += int(tv.sum() % 2)
            tests += 1
            fehler += not np.array_equal(sf(verschiebe(m, tv)), verschiebe(sm1, tv))
    stapel_fehler = 0; stapel_tests = 0
    for ridx in regeln_d[1:6]:
        sf, _ = regel_fn(ridx)
        st = [s[2] for s in s1]
        e_st = lauf_stapel(st, sf, 128, PARAM['C_max'])[0]
        for m, a in zip(st, e_st):
            b = lauf_stapel([m], sf, 128, PARAM['C_max'])[0][0]
            stapel_tests += 1
            stapel_fehler += not (a['klasse'] == b['klasse'] and a['t'] == b['t'] and a.get('p') == b.get('p')
                                  and a.get('d') == b.get('d') and np.array_equal(a['live'], b['live']))
    out['d_symmetrie'] = dict(gruppe=len(gruppe), echte=sum(g['echt'] for g in gruppe), in_T=sum(g['in_T'] for g in gruppe),
                              tests=tests, fehler=int(fehler), stapel_tests=stapel_tests, stapel_fehler=int(stapel_fehler))
    out['d_ok'] = bool(fehler == 0 and len(gruppe) == 48 and sum(g['echt'] for g in gruppe) == 24
                       and sum(g['in_T'] for g in gruppe) == 12 and stapel_fehler == 0)
    # (e) Zusatz: Lichtkegel B1-12/S0-12 aus einem Knoten = Kuboktaeder {K-Norm <= t}
    sf, _ = regel_fn(regel_index(1, 12, 0, 12))
    Lx = kodiere(0, 0, 0)[None]
    lk = []
    for t in range(1, 7):
        Lx = sf(Lx)
        xyz = kart(Lx)
        soll = {tuple(v) for v in q.tolist() if knorm(v) <= t} if t <= 6 else None
        lk.append(dict(t=t, zellen=int(Lx.size), soll=len(soll), gleich=bool({tuple(v) for v in xyz.tolist()} == soll)))
    out['e_lichtkegel'] = lk
    out['e_ok'] = bool(all(x['gleich'] and x['zellen'] == [13, 55, 147, 309, 561, 923][x['t'] - 1] for x in lk))
    out['LF0_ok'] = bool(out['a_ok'] and out['b_ok'] and out['c_ok'])
    out['zusatz_ok'] = bool(out['d_ok'] and out['e_ok'])
    return out


# ---------------------------------------------------------------- Bloecke
def regelliste(arg):
    if '-' in arg:
        a, b = arg.split('-')
        return list(range(int(a), int(b)))
    return [int(x) for x in arg.split(',')]


def fertige(pfad):
    s = set()
    if os.path.exists(pfad):
        for z in open(pfad):
            z = z.strip()
            if z:
                try:
                    s.add(json.loads(z)['index'])
                except Exception:
                    pass
    return s


def ist_b1(idx):
    return regel_masken(idx)[3][0] == 1


def ist_s_voll(idx):
    q = regel_masken(idx)[3]
    return q[2] == 0 and q[3] == 12


def stufe2_liste(pfade):
    rs = []
    for p in pfade.split(','):
        for z in open(p):
            z = z.strip()
            if z:
                r = json.loads(z)
                rs.append((r['index'], r['score']))
    kand = [(sc, i) for i, sc in rs if sc >= 1 and not ist_b1(i) and not ist_s_voll(i)]
    kand.sort(key=lambda x: (-x[0], x[1]))
    return [i for sc, i in kand[:PARAM['N2_max']]], len(kand)


def main():
    modus = sys.argv[1]
    t0 = time.time()
    if modus == 'kontrolle':
        out = kontrolle()
        out['param'] = PARAM; out['zeit_s'] = round(time.time() - t0, 2)
        json.dump(out, open(sys.argv[2], 'w'), indent=1)
        print(json.dumps({k: v for k, v in out.items() if k.endswith('ok')}), 'zeit', out['zeit_s'], flush=True)
        return
    if modus == 'stufe1':
        aus = sys.argv[2]; grenze = float(sys.argv[3])
        regeln = regelliste(sys.argv[4]) if len(sys.argv) > 4 else list(range(NREG))
        st = saaten(1); W, Wo = PARAM['W1'], PARAM['W1_obj']; stufe = 1
    elif modus == 'stufe2':
        aus = sys.argv[3]; grenze = float(sys.argv[4])
        regeln, n_kand = stufe2_liste(sys.argv[2])
        print('stufe2 kandidaten', n_kand, 'gewaehlt', len(regeln), flush=True)
        st = saaten(2); W, Wo = PARAM['W2'], PARAM['W2_obj']; stufe = 2
    else:
        raise SystemExit('unbekannter Modus')
    schon = fertige(aus)
    n_neu = 0
    with open(aus, 'a') as fh:
        for idx in regeln:
            if idx in schon:
                continue
            if time.time() - t0 > grenze:
                print('zeitgrenze erreicht vor regel', idx, flush=True)
                break
            r = suche_regel(idx, st, W, Wo)
            r['stufe'] = stufe
            fh.write(json.dumps(r) + '\n'); fh.flush()
            n_neu += 1
            if r['n_gleiter'] or r['zeit_s'] > 2.0 or n_neu % 250 == 0:
                print(idx, r['name'], r['klasse'], r['saat_klassen'], 'gleiter', r['n_gleiter'], 'bahnen', r['n_bahnen'],
                      'obj', r['objekt_laeufe'], 'gekappt', r['gekappt'], r['objekt_gekappt'], 'zeit', r['zeit_s'],
                      'gesamt', round(time.time() - t0, 1), flush=True)
    # Berichtigung nach dem Einfrieren (ERGEBNIS, Selbstanzeige): fertige(aus) stand in der Listenbedingung und las die
    # Ausgabedatei je Regel neu ein; Stufe 1a hing deshalb nach der letzten Regel bis zur 600-s-Kappe. Ergebnisse unberuehrt.
    fertig_jetzt = fertige(aus)
    rest = [i for i in regeln if i not in fertig_jetzt]
    print('block fertig', round(time.time() - t0, 1), 's', 'neu', n_neu, 'offen', len(rest), flush=True)


if __name__ == '__main__':
    main()
