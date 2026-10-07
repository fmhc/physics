#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DEFEKT-NETZ-1 (Runde 47, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage: Laufen die masselosen TT-Moden des Hamilton-Netzes (EINE-WELT-LOCH-1, Paarung A1R1, J = 1) auf den
Frank-Kasper-Kristallen C15 (MgCu2) und A15 (Cr3Si) gleichmaessiger in alle Richtungen als auf Finns Netz V
(s(V) = 6,34 %, TT-ISO-1)?

Unveraendert importiert: tg.py (TT-GLAS-1: modell, punkt, affin, netz_V), tti.py (TT-ISO-1: richtungen13),
ew.py, tp.py (EINE-WELT-LOCH-1 / TENSOR-EIS-PYRO-1).
Lagen (kubische Kante a = 1): NRL Crystal Lattice Structures (Mehl et al.), Spiegel
www.atomic-scale-physics.de/lattice/struk/c15.html (Wyckoff Vol. I, S. 365-367) und .../a15.html (Nevitt).
Modi: dn0 (Bau, Gleichstaende, Kanten, Symmetrie), tt (Spektrum je Netz), auswertung (Urteile), bild.
"""
import argparse, json, sys, os, time, hashlib, platform, resource, itertools
from collections import Counter
import numpy as np
import scipy
from scipy.spatial import Delaunay

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402  (sha256 419d7da6..., unveraendert)
import ew  # noqa: E402  (sha256 fa7b6417..., unveraendert)
import tg  # noqa: E402  (TT-GLAS-1, sha256 ec48a258..., unveraendert)
import tti  # noqa: E402  (TT-ISO-1, sha256 6d6b6f7b..., unveraendert)

GSHIFT = np.array([0.01234, 0.02345, 0.03456])   # generische Verschiebung der Zellzuordnung (kein Schwerpunkt auf dem Rand)
EPS_TT = (1e-3, 2e-3)                             # |k| wie TT-ISO-1
TOL_KUGEL = 1e-9                                  # "auf der Umkugel": | |P - C| / R - 1 | <= 1e-9
CUTOFF = {'C15': 0.52, 'A15': 0.66}               # erste Nachbarschale (FK-Koordination); Luecke wird geprueft
LUECKE_CUT = 0.03                                 # kein Paarabstand in [cutoff - 0,03; cutoff + 0,03]
Q_SOLL = {'C15': 5.1, 'A15': 46.0 / 9.0}
S_V_TTISO = 0.06338809562866454                   # TT-ISO-1 lauf-69/gitter-V-A1R1.json, spanne_J1
S_S_TTISO = 0.026847167230505953                  # TT-ISO-1 lauf-69/gitter-S-A1R1.json, spanne_J1 (Netz S)
S_V_KARTE = 0.0634
VERSCHIEBUNG_S_C15 = np.array([3.0, 3.0, 3.0]) / 8.0   # ew-Netz S + (3/8, 3/8, 3/8) = C15-Lagen der Quelle [M]
FCC = np.array([[0, 0, 0], [0, .5, .5], [.5, 0, .5], [.5, .5, 0]])
TT_DREI = ('100', '110', '111')


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def nur_schluessel(x, tiefe=0):
    if isinstance(x, dict):
        return {k: nur_schluessel(v, tiefe + 1) for k, v in x.items()} if tiefe < 3 else sorted(x.keys())
    if isinstance(x, list) and x and isinstance(x[0], dict):
        return [nur_schluessel(x[0], tiefe + 1)]
    return type(x).__name__


def schreibe(pfad, res):
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(pfad + '.tmp', pfad)


# ------------------------------------------------------------------------------------------------ Lagen
def kristall(name):
    """Kubische Zelle (a = 1): Gittervektoren (Zeilen), Lagen, Typen. Quelle siehe Kopf."""
    if name == 'C15':
        basis = [((1 / 8, 1 / 8, 1 / 8), 'Mg'), ((7 / 8, 7 / 8, 7 / 8), 'Mg'),
                 ((1 / 2, 1 / 2, 1 / 2), 'Cu'), ((1 / 2, 1 / 4, 1 / 4), 'Cu'), ((1 / 4, 1 / 2, 1 / 4), 'Cu'),
                 ((1 / 4, 1 / 4, 1 / 2), 'Cu')]
        pos, typ = [], []
        for p, ty in basis:
            for t in FCC:
                pos.append(np.mod(np.array(p, float) + t, 1.0))
                typ.append(ty)
    elif name == 'A15':
        basis = [((0, 0, 0), 'Si'), ((.5, .5, .5), 'Si'), ((.25, .5, 0), 'Cr'), ((.75, .5, 0), 'Cr'),
                 ((0, .25, .5), 'Cr'), ((0, .75, .5), 'Cr'), ((.5, 0, .25), 'Cr'), ((.5, 0, .75), 'Cr')]
        pos = [np.array(p, float) for p, ty in basis]
        typ = [ty for p, ty in basis]
    else:
        raise ValueError(name)
    pos = np.array(pos)
    Y = np.rint(pos * 8).astype(int)
    assert np.allclose(pos * 8, Y) and len(set(map(tuple, Y % 8))) == len(pos)
    return np.eye(3), pos, typ


def superzelle(LV, pos, typ, m):
    """m x m x m Superzelle der kubischen Zelle."""
    P, T = [], []
    for s in itertools.product(range(m), repeat=3):
        P.append(pos + np.array(s, float) @ LV)
        T += list(typ)
    return LV * m, np.concatenate(P), T


def kopien(LV, pos, r=1):
    offs = np.array(list(itertools.product(range(-r, r + 1), repeat=3)), dtype=np.int64)
    P = (pos[None, :, :] + (offs.astype(float) @ LV)[:, None, :]).reshape(-1, 3)
    gidx = np.tile(np.arange(len(pos)), len(offs))
    goff = np.repeat(offs, len(pos), axis=0)
    return P, gidx, goff


def kanon(X, gi, go, LV):
    """Kanonische Form eines Simplex (Ecken X, Untergitter gi, Versaetze go): Schwerpunkt + GSHIFT in die Zelle,
    Ecken lexikographisch sortiert. Schluessel in Einheiten 1/64 (alle Lagen sind Vielfache von 1/8)."""
    f = X.mean(0) @ np.linalg.inv(LV) + GSHIFT
    n = np.floor(f).astype(np.int64)
    X2 = X - n.astype(float) @ LV
    Y = np.rint(X2 * 64).astype(np.int64)
    assert np.allclose(X2 * 64, Y, atol=1e-6)
    o = np.lexsort(Y.T[::-1])
    return tuple(Y[o].ravel().tolist()), gi[o], go[o] - n[None, :]


# ------------------------------------------------------------------------------------------------ Bau
def periodisch_delaunay(LV, pos):
    """Periodische Delaunay-Zerlegung ueber 27 Kopien (scipy/Qhull, Standardoptionen wie tg.zufallsnetz); behalten wird
    je Tetraeder die Kopie mit Schwerpunkt + GSHIFT in der Zelle."""
    P, gidx, goff = kopien(LV, pos, 1)
    tri = Delaunay(P)
    S = tri.simplices
    X = P[S]
    f = X.mean(1) @ np.linalg.inv(LV) + GSHIFT
    halte = np.all((f >= 0.0) & (f < 1.0), axis=1)
    S = S[halte]
    G, O, keys = [], [], []
    for row in S:
        key, gi, go = kanon(P[row], gidx[row], goff[row], LV)
        G.append(gi)
        O.append(go)
        keys.append(key)
    info = {'n_punkte_kopien': int(len(P)), 'n_simplices_gesamt': int(len(tri.simplices)),
            'qhull_coplanar': int(len(tri.coplanar)), 'n_behalten': int(len(S)),
            'n_schluessel_verschieden': int(len(set(keys)))}
    return np.array(G, np.int64), np.array(O, np.int64), keys, info


def abstaende(LV, pos):
    P, gidx, goff = kopien(LV, pos, 1)
    d = np.linalg.norm(P[None, :, :] - pos[:, None, :], axis=2)
    return d


def schalen(LV, pos, typ, cutoff):
    d = abstaende(LV, pos)
    P, gidx, goff = kopien(LV, pos, 1)
    werte = np.unique(np.round(d[(d > 1e-9) & (d < 1.0)], 9))
    paare = {}
    for i in range(len(pos)):
        for j in np.nonzero((d[i] > 1e-9) & (d[i] < 1.0))[0]:
            kk = '-'.join(sorted([typ[i], typ[gidx[j]]]))
            paare.setdefault(kk, set()).add(round(float(d[i, j]), 6))
    nah = (d > 1e-9) & (d < cutoff)
    z = nah.sum(1)
    in_luecke = int(np.sum((d > cutoff - LUECKE_CUT) & (d < cutoff + LUECKE_CUT)))
    return {'abstaende_unter_1': werte.tolist()[:12], 'paar_abstaende': {k: sorted(v)[:4] for k, v in paare.items()},
            'cutoff': cutoff, 'paare_in_luecke': in_luecke,
            'koordination': {str(k): int(v) for k, v in sorted(Counter(z.tolist()).items())},
            'koordination_je_typ': {t: sorted(Counter(int(z[i]) for i in range(len(pos)) if typ[i] == t).items())
                                    for t in sorted(set(typ))}}


def fk_tetraeder(LV, pos, cutoff):
    """Kristallographische FK-Tetraeder: alle 4-Cliquen des Nachbargraphen (Abstand < cutoff)."""
    P, gidx, goff = kopien(LV, pos, 1)
    N = len(pos)
    tets = {}
    for s in range(N):
        i0 = int(np.nonzero((gidx == s) & np.all(goff == 0, axis=1))[0][0])
        d = np.linalg.norm(P - pos[s], axis=1)
        J = np.nonzero((d > 1e-9) & (d < cutoff))[0]
        Q = P[J]
        adj = np.linalg.norm(Q[:, None] - Q[None], axis=2) < cutoff
        for a, b, c in itertools.combinations(range(len(J)), 3):
            if adj[a, b] and adj[a, c] and adj[b, c]:
                idx = np.array([i0, J[a], J[b], J[c]])
                key, gi, go = kanon(P[idx], gidx[idx], goff[idx], LV)
                tets[key] = (gi, go)
    keys = sorted(tets)
    G = np.array([tets[k][0] for k in keys], np.int64)
    O = np.array([tets[k][1] for k in keys], np.int64)
    return G, O, keys


def umkugeln(X):
    A = 2.0 * (X[:, 1:] - X[:, :1])
    b = (X[:, 1:] ** 2).sum(-1) - (X[:, :1] ** 2).sum(-1)
    C = np.linalg.solve(A, b[..., None])[..., 0]
    R = np.linalg.norm(C - X[:, 0], axis=1)
    return C, R


def gleichstaende(LV, pos, G, O):
    """Zahl der Punkte auf und in der Umkugel je Tetraeder (alle 27 Kopien)."""
    P, gidx, goff = kopien(LV, pos, 1)
    X = pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)
    C, R = umkugeln(X)
    d = np.linalg.norm(P[None, :, :] - C[:, None, :], axis=2)
    rel = d / R[:, None] - 1.0
    auf = (np.abs(rel) <= TOL_KUGEL).sum(1)
    innen = (rel < -TOL_KUGEL).sum(1)
    marge = np.where(np.abs(rel) <= TOL_KUGEL, np.inf, rel).min(1)
    gl = np.nonzero(auf >= 5)[0]
    kugeln = set((tuple(np.rint(C[i] * 1e6).astype(int).tolist()), int(round(R[i] * 1e6))) for i in gl)
    fr = C @ np.linalg.inv(LV)
    rr = R / np.min(np.linalg.norm(LV, axis=1))
    rand = float(min((fr - rr[:, None] + 1.0).min(), (2.0 - fr - rr[:, None]).min()))
    return {'n_tetraeder': int(len(G)), 'tetraeder_mit_5_oder_mehr_auf_umkugel': int(len(gl)),
            'gleichstaende_kugeln': int(len(kugeln)), 'punkte_auf_umkugel_max': int(auf.max()),
            'punkte_auf_umkugel_min': int(auf.min()), 'tetraeder_mit_punkt_innen': int((innen > 0).sum()),
            'marge_min_rel': float(marge.min()), 'R_min': float(R.min()), 'R_max': float(R.max()),
            'abstand_kugel_zu_kopienrand_min': rand}


def baue(name, bau, m=1):
    LV, pos, typ = kristall(name)
    if m > 1:
        LV, pos, typ = superzelle(LV, pos, typ, m)
    if bau == 'delaunay':
        G, O, keys, info = periodisch_delaunay(LV, pos)
    elif bau == 'fk':
        G, O, keys = fk_tetraeder(LV, pos, CUTOFF[name])
        info = {'n_behalten': int(len(G))}
    else:
        raise ValueError(bau)
    return LV, pos, typ, G, O, keys, info


def netz_ew(f):
    """V (tg.netz_V, unveraendert) bzw. S (dieselbe Umformung von ew.geometrie)."""
    if f == 'V':
        return tg.netz_V()
    pos8, zellen = ew.geometrie(f)
    G, O = [], []
    for z in zellen:
        assert len(z['X8']) == 4 and z['kin']
        ids = [ew.zerlege(x, pos8) for x in z['X8']]
        G.append([s for (s, n) in ids])
        O.append([list(n) for (s, n) in ids])
    pos = np.array([np.asarray(p, float) / 8.0 for p in pos8])
    return np.array(ew.AV, float), pos, np.array(G, np.int64), np.array(O, np.int64), {}


# ------------------------------------------------------------------------------------------------ Netzproben
def kantenstatistik(mod, typ, LV, pos):
    E, T = mod['E'], mod['T']
    zahl = np.bincount(mod['eidx'].ravel(), minlength=E)
    vec = mod['n'] * mod['l'][:, None]
    es, es2 = mod['es'], mod['es2']
    zt = Counter(zahl.tolist())
    out = {'E': int(E), 'T': int(T), 'nV': int(mod['nV']), 'tetraeder_je_kante': {str(k): int(v) for k, v in sorted(zt.items())},
           'nur_5_oder_6': bool(set(zt) <= {5, 6}), 'q': float(zahl.mean()), 'q_6T_durch_E': float(6.0 * T / E),
           'f6': float(np.mean(zahl == 6)), 'n6': int(np.sum(zahl == 6))}
    arten = Counter()
    for e in range(E):
        arten[('-'.join(sorted([typ[es[e]], typ[es2[e]]])), int(zahl[e]), round(float(mod['l'][e]), 6))] += 1
    out['kantenarten'] = [{'paar': a, 'tetraeder': z, 'laenge': l, 'anzahl': n} for (a, z, l), n in sorted(arten.items())]
    e6 = np.nonzero(zahl == 6)[0]
    grad6 = np.bincount(np.concatenate([es[e6], es2[e6]]), minlength=mod['nV'])
    out['grad6_je_typ'] = {t: sorted(Counter(int(grad6[i]) for i in range(mod['nV']) if typ[i] == t).items())
                          for t in sorted(set(typ))}
    vek = {i: [] for i in range(mod['nV'])}
    for e in e6:
        vek[es[e]].append(vec[e])
        vek[es2[e]].append(-vec[e])
    return out, zahl, e6, vek


def diamantprobe(mod, typ, LV, pos, zahl, e6, vek):
    """6er-Kanten von C15 = Diamantnetz der Mg: (i) nur Mg-Mg; (ii) Grad 4 an jedem Mg; (iii) Menge der 6er-Kanten =
    Menge der naechsten Mg-Mg-Paare (Abstand sqrt(3)/4); (iv) die 4 Bindungsvektoren je Mg sind (1/4)(+-1,+-1,+-1)
    mit festem Vorzeichenprodukt, paarweise Winkel arccos(-1/3); (v) die zwei fcc-Untergitter wechseln sich ab."""
    es, es2 = mod['es'], mod['es2']
    nur_mg = all(typ[es[e]] == 'Mg' and typ[es2[e]] == 'Mg' for e in e6)
    mg = [i for i in range(mod['nV']) if typ[i] == 'Mg']
    grad4 = all(len(vek[i]) == 4 for i in mg)
    # (iii) naechste Mg-Mg-Paare
    P, gidx, goff = kopien(LV, pos, 1)
    soll = set()
    for i in mg:
        d = np.linalg.norm(P - pos[i], axis=1)
        for j in np.nonzero((d > 1e-9) & (d < 0.45) & np.array([typ[g] == 'Mg' for g in gidx]))[0]:
            a, b = sorted([(i, (0, 0, 0)), (int(gidx[j]), tuple(int(x) for x in goff[j]))])
            ddv = tuple(np.array(b[1]) - np.array(a[1]))
            soll.add((a[0], b[0], ddv) if a[0] != b[0] else (a[0], b[0], ddv))
    ist = set()
    for e in e6:
        s, s2 = int(es[e]), int(es2[e])
        dd = tuple(int(round(x)) for x in np.linalg.solve(LV.T, mod['Tedge'][e]))
        a, b = sorted([(s, (0, 0, 0)), (s2, dd)])
        ist.add((a[0], b[0], tuple(np.array(b[1]) - np.array(a[1]))))
    gleich = (soll == ist)
    vz, winkel_ok, vek_ok = [], True, True
    for i in mg:
        V = np.array(vek[i])
        if len(V) != 4:
            vek_ok = False
            continue
        if not np.allclose(np.abs(V), 0.25, atol=1e-12):
            vek_ok = False
        prod = set(int(np.sign(np.prod(v))) for v in V)
        vz.append(prod.pop() if len(prod) == 1 else 0)
        G = V @ V.T / (3 / 16)
        if not np.allclose(G[~np.eye(4, dtype=bool)], -1.0 / 3.0, atol=1e-12):
            winkel_ok = False
    zweiteilig = bool(sorted(Counter(vz).items()) == [(-1, len(mg) // 2), (1, len(mg) // 2)])
    ok = bool(nur_mg and grad4 and gleich and vek_ok and winkel_ok and zweiteilig)
    return {'nur_Mg_Mg': bool(nur_mg), 'grad_4_je_Mg': bool(grad4), 'gleich_naechste_Mg_Mg_paare': bool(gleich),
            'n_soll': len(soll), 'n_ist': len(ist), 'vektoren_viertel': bool(vek_ok), 'winkel_tetraedrisch': bool(winkel_ok),
            'vorzeichen_untergitter': sorted(Counter(vz).items()), 'zweiteilig': zweiteilig, 'diamant': ok}


def kettenprobe(mod, typ, zahl, e6, vek):
    """A15 (beschreibend): 6er-Kanten = Cr-Cr-Ketten (Laenge 1/2), je Cr zwei, gegenlaeufig (gerade Kette)."""
    es, es2 = mod['es'], mod['es2']
    nur_cr = all(typ[es[e]] == 'Cr' and typ[es2[e]] == 'Cr' for e in e6)
    laengen = sorted(set(round(float(mod['l'][e]), 9) for e in e6))
    gerade = all(len(vek[i]) == 2 and np.allclose(vek[i][0], -vek[i][1]) for i in range(mod['nV']) if typ[i] == 'Cr')
    achsen = sorted(Counter(int(np.argmax(np.abs(vek[i][0]))) for i in range(mod['nV']) if typ[i] == 'Cr' and vek[i]).items())
    return {'nur_Cr_Cr': bool(nur_cr), 'laengen': laengen, 'gerade_ketten': bool(gerade), 'achsen': achsen}


def dreiecke_und_euler(LV, pos, G, O, E):
    X = pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)
    cnt = Counter()
    for t in range(len(G)):
        for f in itertools.combinations(range(4), 3):
            f = list(f)
            key, _, _ = kanon(X[t][f], G[t][f], O[t][f], LV)
            cnt[key] += 1
    F = len(cnt)
    return {'F': int(F), 'jedes_dreieck_in_genau_2': bool(set(cnt.values()) == {2}),
            'euler_V_minus_E_plus_F_minus_T': int(len(pos) - E + F - len(G))}


def punktoperationen():
    ops = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3), int)
            for i in range(3):
                R[i, perm[i]] = sg[i]
            ops.append(R)
    return ops


def symmetrie(pos, typ, keys):
    """Raumgruppenoperationen (R, t) der Lagen (kubisch, a = 1, Raster 1/8) und ob die Tetraedermenge invariant ist."""
    Y = np.rint(pos * 8).astype(int) % 8
    platz = {tuple(y): t for y, t in zip(Y.tolist(), typ)}
    ops = []
    for R in punktoperationen():
        RY = (Y @ R.T) % 8
        ts = set()
        for y in Y:
            t = tuple(((y - RY[0]) % 8).tolist())
            if t in ts:
                continue
            Z = (RY + np.array(t)) % 8
            if all(tuple(z) in platz and platz[tuple(z)] == typ[i] for i, z in enumerate(Z.tolist())):
                ts.add(t)
                ops.append((R, np.array(t)))
    kset = set(keys)
    LV = np.eye(3)
    fehl = 0
    for R, t in ops:
        for key in keys:
            X = np.array(key, float).reshape(4, 3) / 64.0
            X2 = X @ R.T + t / 8.0
            k2, _, _ = kanon(X2, np.zeros(4, int), np.zeros((4, 3), int), LV)
            if k2 not in kset:
                fehl += 1
                break
    return {'n_operationen_lagen': len(ops), 'n_operationen_tetraeder_nicht_invariant': int(fehl)}


def identitaet_S_C15(keys_c15):
    """Zellen des ew-Netzes S, um (3/8,3/8,3/8) verschoben und mit den vier fcc-Translationen in die kubische Zelle
    gebracht, gegen die C15-Tetraeder (Schluesselmengen)."""
    LVs, poss, Gs, Os, _ = netz_ew('S')
    X = poss[Gs] + np.einsum('tai,ij->taj', Os.astype(float), LVs) + VERSCHIEBUNG_S_C15
    ks = set()
    for t in FCC:
        for Xi in X + t:
            k, _, _ = kanon(Xi, np.zeros(4, int), np.zeros((4, 3), int), np.eye(3))
            ks.add(k)
    kc = set(keys_c15)
    return {'n_S_zellen_primitiv': int(len(Gs)), 'n_S_kubisch': len(ks), 'n_C15': len(kc), 'gleich': bool(ks == kc),
            'nur_in_S': len(ks - kc), 'nur_in_C15': len(kc - ks)}


# ------------------------------------------------------------------------------------------------ Modus dn0
def lauf_dn0():
    out = {}
    for name in ('C15', 'A15'):
        t0 = time.time()
        LV, pos, typ = kristall(name)
        z = {'lagen': {'n': int(len(pos)), 'typen': sorted(Counter(typ).items())}}
        z['schalen'] = schalen(LV, pos, typ, CUTOFF[name])
        Gd, Od, kd, infd = periodisch_delaunay(LV, pos)
        Gf, Of, kf = fk_tetraeder(LV, pos, CUTOFF[name])
        z['delaunay'] = {'info': infd, 'umkugel': gleichstaende(LV, pos, Gd, Od)}
        z['fk'] = {'n': int(len(Gf)), 'umkugel': gleichstaende(LV, pos, Gf, Of)}
        z['delaunay_gleich_fk'] = bool(set(kd) == set(kf))
        z['nur_delaunay'] = len(set(kd) - set(kf))
        z['nur_fk'] = len(set(kf) - set(kd))
        gl = z['delaunay']['umkugel']['tetraeder_mit_5_oder_mehr_auf_umkugel']
        z['bauweg'] = 'delaunay' if gl == 0 else 'fk'
        z['bauweg_regel'] = 'Gleichstaende (>= 5 Punkte auf einer Umkugel) = 0 -> Delaunay, sonst FK (Karte, Zusatz 2)'
        for bau, G, O, keys in (('delaunay', Gd, Od, kd), ('fk', Gf, Of, kf)):
            mod = tg.modell(LV, pos, G, O, {})
            ks, zahl, e6, vek = kantenstatistik(mod, typ, LV, pos)
            ks['pruefung'] = {k: v for k, v in mod['pruefung'].items() if k != 't_modell_s'}
            ks.update(dreiecke_und_euler(LV, pos, G, O, mod['E']))
            if name == 'C15':
                ks['diamant'] = diamantprobe(mod, typ, LV, pos, zahl, e6, vek)
            else:
                ks['ketten'] = kettenprobe(mod, typ, zahl, e6, vek)
            ks['symmetrie'] = symmetrie(pos, typ, keys)
            z['netz_' + bau] = ks
        if name == 'C15':
            z['identitaet_S'] = identitaet_S_C15(kd)
        z['laufzeit_s'] = time.time() - t0
        out[name] = z
    return out


# ------------------------------------------------------------------------------------------------ Modus tt
def laplace(mod, k):
    nV = mod['nV']
    es, es2 = mod['es'], mod['es2']
    ph = np.exp(1j * (mod['Tedge'] @ k))
    L = np.zeros((nV, nV), complex)
    np.add.at(L, (es, es), 1.0)
    np.add.at(L, (es2, es2), 1.0)
    np.add.at(L, (es, es2), -ph)
    np.add.at(L, (es2, es), -np.conj(ph))
    return L


def grundtempo(mod):
    """Skalares Grundtempo: Graph-Laplace mit Einheitsgewichten, c^2 = kleinster Eigenwert / k^2 (wie DANZER S)."""
    r13 = tti.richtungen13()
    c2 = {e: [] for e in EPS_TT}
    herm = 0.0
    for nm, d in r13:
        for e in EPS_TT:
            L = laplace(mod, e * d)
            herm = max(herm, float(np.abs(L - np.conj(L.T)).max()))
            c2[e].append(float(np.linalg.eigvalsh(0.5 * (L + np.conj(L.T)))[0] / e ** 2))
    a, b = np.array(c2[EPS_TT[0]]), np.array(c2[EPS_TT[1]])
    rich = (4.0 * a - b) / 3.0
    sp = lambda c2v: float((np.sqrt(c2v).max() - np.sqrt(c2v).min()) / np.sqrt(c2v).mean())  # noqa: E731
    ops = punktoperationen()
    n0 = np.array([0.26, 0.45, 0.85])
    n0 = n0 / np.linalg.norm(n0)
    c48 = []
    for R in ops:
        L = laplace(mod, EPS_TT[0] * (R @ n0))
        c48.append(float(np.linalg.eigvalsh(0.5 * (L + np.conj(L.T)))[0] / EPS_TT[0] ** 2))
    c48 = np.array(c48)
    return {'c2_eps1': a.tolist(), 'c2_eps2': b.tolist(), 'c2_richardson': rich.tolist(),
            'spanne_c_eps1': sp(a), 'spanne_c_richardson': sp(rich), 'spanne_c_48_eps1': sp(c48),
            'c_mittel_richardson': float(np.sqrt(rich).mean()), 'L_herm_max': herm}


def wedge_richtungen(n=12):
    v1, v2, v3 = np.array([1., 0, 0]), np.array([1., 1, 0]) / np.sqrt(2), np.array([1., 1, 1]) / np.sqrt(3)
    out = []
    for i in range(n + 1):
        for j in range(n + 1 - i):
            v = (i * v2 + j * v3 + (n - i - j) * v1) / n
            out.append(v / np.linalg.norm(v))
    return out


def pfad_richtungen(m=24):
    ecken = [np.array([1., 0, 0]), np.array([1., 1, 0]) / np.sqrt(2), np.array([1., 1, 1]) / np.sqrt(3), np.array([1., 0, 0])]
    out, winkel, w0 = [], [], 0.0
    for a, b in zip(ecken[:-1], ecken[1:]):
        th = np.arccos(np.clip(a @ b, -1, 1))
        for i in range(m):
            t = i / m
            v = (np.sin((1 - t) * th) * a + np.sin(t * th) * b) / np.sin(th)
            out.append(v / np.linalg.norm(v))
            winkel.append(np.degrees(w0 + t * th))
        w0 += th
    out.append(ecken[-1])
    winkel.append(np.degrees(w0))
    return out, winkel


def kurz(p):
    keys = ('eps', 'rang_Mc', 'nX', 'dim', 'weg', 'sv_rel_min', 'B_red_neg', 'B_red_min_rel', 'A_red_pd', 'skala',
            'n_wachsend', 'n_masselos', 'n_luecke', 'n_unklar', 'w2_kleinste', 'w2im_max', 'w2_min_re', 'luecke_min',
            'unklar_werte', 'w2k2_masselos', 'tt_anteil', 'fit_rest', 'kontr_ops', 'A_red_neg', 't_s')
    return {k: p[k] for k in keys if k in p}


def lauf_tt(netz, bauweg, mit_bz=True, mit_dicht=True, m_sz=2):
    t00 = time.time()
    if netz in ('C15', 'A15'):
        LV, pos, typ, G, O, keys, info = baue(netz, bauweg)
    else:
        LV, pos, G, O, info = netz_ew(netz)
        typ = None
    mod = tg.modell(LV, pos, G, O, {})
    out = {'netz': netz, 'bauweg': bauweg, 'bau_info': info,
           'pruefung': {k: v for k, v in mod['pruefung'].items()}}
    # (1) Plan-Messung: 13 Richtungen (TT-ISO-1) x 2 |k|
    zeilen, werte = [], []
    for nm, d in tti.richtungen13():
        z = {'richtung': nm, 'd': d.tolist()}
        for e in EPS_TT:
            p = tg.punkt(mod, e * d, mit_tt=(nm in TT_DREI and e == EPS_TT[0]), mit_kontr=(nm == '100' and e == EPS_TT[0]))
            z['eps%g' % e] = kurz(p)
            werte += p['w2k2_masselos']
        zeilen.append(z)
    out['plan13'] = zeilen
    pk = [z['eps%g' % e] for z in zeilen for e in EPS_TT]
    n2 = all(len(p['w2k2_masselos']) == 2 for p in pk)
    w = np.array(werte, float)
    out['spanne'] = float(w.max() / w.min() - 1.0) if len(w) else None
    out['w_min'] = float(w.min()) if len(w) else None
    out['w_max'] = float(w.max()) if len(w) else None
    out['w_mittel'] = float(w.mean()) if len(w) else None
    tt = [x for z in zeilen if z['richtung'] in TT_DREI for x in z['eps%g' % EPS_TT[0]].get('tt_anteil', [])]
    lin = []
    for z in zeilen:
        a, b = z['eps%g' % EPS_TT[0]]['w2k2_masselos'], z['eps%g' % EPS_TT[1]]['w2k2_masselos']
        if len(a) == 2 and len(b) == 2:
            lin += [abs(b[i] / a[i] - 1.0) for i in range(2)]
    reg = {'genau_2_masselos_alle': bool(all(p['n_masselos'] == 2 for p in pk)), 'zwei_positive_werte_alle': bool(n2),
           'wachsend_summe': int(sum(p['n_wachsend'] for p in pk)), 'unklar_summe': int(sum(p['n_unklar'] for p in pk)),
           'A_red_pd_alle': bool(all(p['A_red_pd'] for p in pk)), 'B_red_neg_summe': int(sum(p['B_red_neg'] for p in pk)),
           'tt_anteil_min': float(min(tt)) if tt else None, 'n_tt_werte': len(tt),
           'linear_max': float(max(lin)) if lin else None,
           'luecke_min': (float(min(p['luecke_min'] for p in pk if p['luecke_min'] is not None))
                          if any(p['luecke_min'] is not None for p in pk) else None),
           'n_masselos_je_punkt': sorted(Counter(int(p['n_masselos']) for p in pk).items())}
    reg['regulaer'] = bool(reg['genau_2_masselos_alle'] and n2 and reg['wachsend_summe'] == 0 and reg['unklar_summe'] == 0
                           and reg['A_red_pd_alle'] and reg['B_red_neg_summe'] == 0 and reg['tt_anteil_min'] is not None
                           and reg['tt_anteil_min'] >= 0.99 and reg['n_tt_werte'] == 6 and reg['linear_max'] is not None
                           and reg['linear_max'] <= 1e-2)
    out['regel'] = reg
    # Zerlegung (beschreibend): Zweigmittel ueber Richtungen und Aufspaltung der Polarisationen bei |k| = 1e-3
    a1 = np.array([z['eps%g' % EPS_TT[0]]['w2k2_masselos'] for z in zeilen if len(z['eps%g' % EPS_TT[0]]['w2k2_masselos']) == 2])
    if len(a1):
        out['zerlegung'] = {'richtungsspanne_zweigmittel': float(a1.mean(1).max() / a1.mean(1).min() - 1.0),
                            'aufspaltung_max': float((a1[:, 1] / a1[:, 0] - 1.0).max())}
    # (2) Symmetrie: 48 Bilder einer allgemeinen Richtung (wie TT-ISO-1)
    n0 = np.array([0.26, 0.45, 0.85])
    n0 = n0 / np.linalg.norm(n0)
    w48 = []
    for R in punktoperationen():
        p = tg.punkt(mod, EPS_TT[0] * (R @ n0))
        w48.append(p['w2k2_masselos'] if len(p['w2k2_masselos']) == 2 else [np.nan, np.nan])
    w48 = np.array(w48)
    out['symmetrie_48'] = {'abw_rel_max': float(np.nanmax(np.abs(w48 - w48[0][None, :]) / w48[0][None, :])),
                           'n_ohne_2': int(np.isnan(w48[:, 0]).sum()), 'w0': w48[0].tolist()}
    # (3) Grundtempo (skalar, Kontrolle)
    out['grundtempo'] = grundtempo(mod)
    # (4) 23 Richtungen von ew (beschreibend)
    w23 = []
    for nm23, d in ew.richtungen():
        p = tg.punkt(mod, EPS_TT[0] * np.asarray(d, float))
        w23 += p['w2k2_masselos']
    out['spanne_23ew'] = float(max(w23) / min(w23) - 1.0)
    # (5) affine Steifigkeit (beschreibend, tg.affin: 13 Wuerfelachsen, |k| = 1e-2)
    out['affin'] = tg.affin(mod)
    # (6) dichte Richtungen im Keil und Pfad fuer das Bild (beschreibend), |k| = 1e-3
    if mit_dicht:
        wd = []
        stat = Counter()
        for d in wedge_richtungen(12):
            p = tg.punkt(mod, EPS_TT[0] * d)
            stat[(p['n_masselos'], p['n_wachsend'], p['n_unklar'])] += 1
            wd.append(p['w2k2_masselos'] if len(p['w2k2_masselos']) == 2 else [np.nan, np.nan])
        wd = np.array(wd)
        out['keil91'] = {'spanne': float(np.nanmax(wd) / np.nanmin(wd) - 1.0), 'min': float(np.nanmin(wd)),
                         'max': float(np.nanmax(wd)), 'klassen': [[list(k), v] for k, v in sorted(stat.items())]}
        pr, win = pfad_richtungen(24)
        wp = []
        for d in pr:
            p = tg.punkt(mod, EPS_TT[0] * d)
            wp.append(p['w2k2_masselos'] if len(p['w2k2_masselos']) == 2 else [None, None])
        out['pfad'] = {'winkel_grad': [float(x) for x in win], 'w2k2': wp, 'ecken': ['100', '110', '111', '100']}
    # (7) Stabilitaet auf dem Gitter L = 8 der Zelle (beschreibend, wie TT-ISO-1 511 k)
    if mit_bz:
        L = 8
        BVc = 2 * np.pi * np.linalg.inv(LV).T
        g = np.arange(L)
        mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
        mm = mm[np.any(mm != 0, axis=1)]
        nw, napd, nbn, wrel, nsvd = 0, 0, 0, np.inf, 0
        for m in mm:
            k = (m / L) @ BVc
            p = tg.punkt(mod, k)
            nw += int(p['n_wachsend'] > 0)
            napd += int(not p['A_red_pd'])
            nbn += int(p['B_red_neg'] > 0)
            nsvd += int(p['weg'] == 'svd')
            wrel = min(wrel, p['w2_min_re'] / p['skala'])
        out['bz_L8'] = {'nk': int(len(mm)), 'k_mit_wachsend': nw, 'k_A_red_nicht_pd': napd, 'k_B_red_neg': nbn,
                        'k_rangverlust_Mc': nsvd, 'w2_min_rel': float(wrel)}
    # (8) Superzelle m^3 (Kontrolle, nur Kristalle): masselose Werte an [100], [110], [111], |k| = 1e-3
    if netz in ('C15', 'A15') and m_sz > 1:
        LV2, pos2, typ2, G2, O2, keys2, info2 = baue(netz, bauweg, m=m_sz)
        mod2 = tg.modell(LV2, pos2, G2, O2, {})
        sz = {'m': m_sz, 'T': int(mod2['T']), 'E': int(mod2['E']), 'nV': int(mod2['nV']), 'info': info2}
        dmax = 0.0
        zz = []
        for z in zeilen:
            if z['richtung'] in TT_DREI:
                p2 = tg.punkt(mod2, EPS_TT[0] * np.array(z['d']))
                a = z['eps%g' % EPS_TT[0]]['w2k2_masselos']
                b = p2['w2k2_masselos']
                if len(a) == 2 and len(b) == 2:
                    dmax = max(dmax, float(np.max(np.abs(np.array(b) / np.array(a) - 1.0))))
                else:
                    dmax = np.inf
                zz.append({'richtung': z['richtung'], 'w2k2': b, 'n_masselos': p2['n_masselos'], 'n_wachsend': p2['n_wachsend']})
        sz['abw_rel_max'] = float(dmax)
        sz['zeilen'] = zz
        out['superzelle'] = sz
    out['t_s'] = time.time() - t00
    return out


# ------------------------------------------------------------------------------------------------ Auswertung (Urteile)
def lauf_auswertung(dn0, tt):
    U = {}
    # DN0 je Netz (Delaunay-Bau, Kartenwortlaut = Plan)
    dn0u = {}
    for name in ('C15', 'A15'):
        z = dn0[name]
        nd = z['netz_delaunay']
        um = z['delaunay']['umkugel']
        pr = nd['pruefung']
        teile = {
            'a_nur_tetraeder': bool(um['tetraeder_mit_5_oder_mehr_auf_umkugel'] == 0 and um['tetraeder_mit_punkt_innen'] == 0
                                    and pr['vol_min_rel_mittel'] > 1e-9 and pr['volumen_summe_rel_abw'] < 1e-12
                                    and nd['jedes_dreieck_in_genau_2'] and z['delaunay']['info']['qhull_coplanar'] == 0),
            'b_kanten_5_oder_6': bool(nd['nur_5_oder_6']),
            'c_q': bool(abs(nd['q_6T_durch_E'] - Q_SOLL[name]) <= 1e-9),
        }
        if name == 'C15':
            teile['d_diamant'] = bool(nd['diamant']['diamant'])
        dn0u[name] = {'teile': teile, 'q': nd['q_6T_durch_E'], 'q_soll': Q_SOLL[name],
                      'q_abw': abs(nd['q_6T_durch_E'] - Q_SOLL[name])}
    alle = all(all(v['teile'].values()) for v in dn0u.values())
    U['DN0'] = {'je_netz': dn0u, 'plan': 'eingetroffen' if alle else 'verfehlt',
                'kartenwortlaut': 'eingetroffen' if alle else 'verfehlt'}
    # Kontrollen
    sV = tt['V']['spanne']
    K = {'V_spanne': sV, 'V_abw_rel_ttiso': abs(sV / S_V_TTISO - 1.0), 'V_kontrolle_ok': bool(abs(sV / S_V_TTISO - 1.0) <= 1e-5)}
    if 'S' in tt:
        K['S_spanne'] = tt['S']['spanne']
        K['S_abw_rel_ttiso'] = abs(tt['S']['spanne'] / S_S_TTISO - 1.0)
    for name in ('C15', 'A15'):
        g = tt[name]['grundtempo']
        K[name + '_grundtempo_spanne_richardson'] = g['spanne_c_richardson']
        K[name + '_grundtempo_isotrop'] = bool(g['spanne_c_richardson'] < 1e-6)
        K[name + '_symmetrie48_abw'] = tt[name]['symmetrie_48']['abw_rel_max']
        K[name + '_symmetrie48_ok'] = bool(tt[name]['symmetrie_48']['abw_rel_max'] <= 1e-6)
    K['C15_gleich_S_spanne_abw'] = abs(tt['C15']['spanne'] / S_S_TTISO - 1.0)
    U['kontrollen'] = K
    sC, sA = tt['C15']['spanne'], tt['A15']['spanne']
    regC, regA = tt['C15']['regel']['regulaer'], tt['A15']['regel']['regulaer']

    def urteil(bed, reg_ok):
        if not reg_ok:
            return 'nicht entscheidbar'
        return 'eingetroffen' if bed else 'verfehlt'
    U['DN1'] = {'plan': urteil(sC < sV, regC and K['V_kontrolle_ok']), 'kartenwortlaut': 'eingetroffen' if sC < S_V_KARTE else 'verfehlt',
                's_C15': sC, 's_V': sV}
    U['DN2'] = {'plan': urteil(sC < sA, regC and regA), 'kartenwortlaut': 'eingetroffen' if sC < sA else 'verfehlt',
                's_C15': sC, 's_A15': sA}
    U['DN3'] = {'plan': urteil(sC < 0.03, regC), 'kartenwortlaut': 'eingetroffen' if sC < 0.03 else 'verfehlt', 's_C15': sC}
    U['tabelle'] = {n: {'spanne': tt[n]['spanne'], 'w_min': tt[n]['w_min'], 'w_max': tt[n]['w_max'], 'w_mittel': tt[n]['w_mittel'],
                        'regulaer': tt[n]['regel']['regulaer'], 'regel': tt[n]['regel'],
                        'grundtempo_spanne_richardson': tt[n]['grundtempo']['spanne_c_richardson'],
                        'symmetrie48': tt[n]['symmetrie_48']['abw_rel_max'], 'spanne_23ew': tt[n]['spanne_23ew'],
                        'keil91_spanne': tt[n].get('keil91', {}).get('spanne'), 'zerlegung': tt[n].get('zerlegung'),
                        'bz_L8': tt[n].get('bz_L8'), 'affin_spanne': tt[n]['affin']['spanne_max_min'],
                        'affin_min': tt[n]['affin']['min'], 'affin_max': tt[n]['affin']['max'],
                        'superzelle_abw': tt[n].get('superzelle', {}).get('abw_rel_max')} for n in tt}
    return U


# ------------------------------------------------------------------------------------------------ Bild
def lauf_bild(tt, pfad):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    farbe = {'C15': '#2a78d6', 'A15': '#eb6834', 'V': '#1baf7a'}
    fig, ax = plt.subplots(figsize=(9.0, 5.2), dpi=150)
    fig.patch.set_facecolor('#fcfcfb')
    ax.set_facecolor('#fcfcfb')
    for name in ('V', 'A15', 'C15'):
        d = tt[name]['pfad']
        w = np.array([x if x[0] is not None else [np.nan, np.nan] for x in d['w2k2']], float)
        mittel = tt[name]['w_mittel']
        x = np.array(d['winkel_grad'])
        rel = (w / mittel - 1.0) * 100.0
        lab = '%s  (Spanne s = %.2f %%, Mittel omega^2/k^2 = %.4f)' % (name, 100 * tt[name]['spanne'], mittel)
        ax.plot(x, rel[:, 0], color=farbe[name], lw=2.0, label=lab)
        ax.plot(x, rel[:, 1], color=farbe[name], lw=2.0, ls='--')
        ax.annotate(name, (x[-1], rel[-1, 1]), xytext=(6, 0), textcoords='offset points', color='#0b0b0b', fontsize=9,
                    va='center')
    ecken = tt['C15']['pfad']['winkel_grad']
    m = (len(ecken) - 1) // 3
    xt = [ecken[0], ecken[m], ecken[2 * m], ecken[-1]]
    ax.set_xticks(xt)
    ax.set_xticklabels(['[100]', '[110]', '[111]', '[100]'])
    for v in xt:
        ax.axvline(v, color='#d9d8d4', lw=0.8, zorder=0)
    ax.axhline(0.0, color='#b5b4ae', lw=0.8, zorder=0)
    ax.grid(axis='y', color='#ecebe7', lw=0.6)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_color('#8a8984')
    ax.tick_params(colors='#52514e')
    ax.set_ylabel('omega^2/k^2 relativ zum Mittel je Netz [%]', color='#0b0b0b')
    ax.set_xlabel('Richtung von k laengs [100] -> [110] -> [111] -> [100] (|k| = 1e-3, A1R1, J = 1)', color='#0b0b0b')
    ax.set_title('DEFEKT-NETZ-1: TT-Tempo ueber der Richtung (durchgezogen: unterer Zweig, gestrichelt: oberer)',
                 color='#0b0b0b', fontsize=10)
    ax.legend(frameon=False, fontsize=8, loc='lower left', labelcolor='#0b0b0b')
    fig.tight_layout()
    fig.savefig(pfad, facecolor=fig.get_facecolor())
    return {'bild': pfad}


# ------------------------------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['dn0', 'tt', 'auswertung', 'bild'])
    ap.add_argument('--netz', choices=['C15', 'A15', 'V', 'S'])
    ap.add_argument('--dn0', help='dn0.json (Bauweg der Kristalle)')
    ap.add_argument('--bauweg', choices=['delaunay', 'fk'], default='delaunay', help='nur ohne --dn0 (Rauchtest)')
    ap.add_argument('--tt', nargs='*', default=[], help='tt-*.json fuer auswertung/bild')
    ap.add_argument('--ohne_bz', action='store_true')
    ap.add_argument('--ohne_dicht', action='store_true')
    ap.add_argument('--sz', type=int, default=2)
    ap.add_argument('--rauch', action='store_true', help='nur Schluessel und Laufzeiten speichern, keine Werte')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'argv': sys.argv, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'skript_sha256': sha(os.path.abspath(__file__)), 'tg_sha256': sha(os.path.abspath(tg.__file__)),
            'tti_sha256': sha(os.path.abspath(tti.__file__)), 'ew_sha256': sha(os.path.abspath(ew.__file__)),
            'tp_sha256': sha(os.path.abspath(tp.__file__))}
    if a.modus == 'dn0':
        erg = lauf_dn0()
    elif a.modus == 'tt':
        if a.netz in ('C15', 'A15') and a.dn0:
            with open(a.dn0) as fh:
                d0 = json.load(fh)
            info['dn0_sha256'] = sha(a.dn0)
            bauweg = d0['ergebnis'][a.netz]['bauweg']
            info['bauweg_quelle'] = 'dn0'
        elif a.netz in ('C15', 'A15'):
            bauweg = a.bauweg                      # nur fuer Rauchtests (Hauptlaeufe lesen den Bauweg aus dn0.json)
            info['bauweg_quelle'] = 'argument'
        else:
            bauweg = 'ew'
        erg = lauf_tt(a.netz, bauweg, mit_bz=not a.ohne_bz, mit_dicht=not a.ohne_dicht, m_sz=a.sz)
    elif a.modus == 'auswertung':
        with open(a.dn0) as fh:
            d0 = json.load(fh)['ergebnis']
        info['dn0_sha256'] = sha(a.dn0)
        tt = {}
        for p in a.tt:
            with open(p) as fh:
                r = json.load(fh)['ergebnis']
            tt[r['netz']] = r
            info['sha256_' + os.path.basename(p)] = sha(p)
        erg = lauf_auswertung(d0, tt)
    else:
        tt = {}
        for p in a.tt:
            with open(p) as fh:
                r = json.load(fh)['ergebnis']
            tt[r['netz']] = r
        erg = lauf_bild(tt, a.out.replace('.json', '.png'))
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        res = {'info': info, 'schluessel': nur_schluessel(erg), 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB']}
    schreibe(a.out, res)
    print('fertig', a.modus, a.netz, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
