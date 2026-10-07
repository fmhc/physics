#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OKTA-SCHATTEN-1 (Runde 46, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Teil L  Licht: Maxwell auf den Pyrochlor-Kanten (Finns Netz). A auf den 12 Kanten je Zelle, Eichung d0 (4 Ecken),
        Plaketten: 8 Dreiecke (Finns Tetraederflaechen), mit Schattenform dazu 4 Sechsecke der Stumpftetraeder-Loecher.
        K = C^+ W C (W = *2 je Plakette), omega^2 = Eigenwerte von K / s1 (s1 = *1, alle Kanten gleich) auf dem
        Komplement von Bild d0 (Gauss). Varianten: ohne (nur Dreiecke), dec (umkreisbasierte Hodge-Sterne, Haupt),
        eins (Einheitsgewichte), Abtastung w_H / w_D. Fit wie LICHT-FINN-NETZ-1 (licht_netz.py, unveraendert).
Teil T  Schwerewellen: Tetraeder-Oktaeder-Wabe (fcc, eine Kopie), Hamilton-Netz wie EINE-WELT-LOCH-1 / TT-ISO-1
        (ew.py unveraendert; A1R1, J = 1 je Zelle). Oktaeder: H3 (Haupt: je Diagonale in 4 Tetraeder, Mittel ueber
        die 3 Diagonalen, Gewicht 1/3), R12 (starres Oktaeder als eine Zelle), Z8 (Mittelpunkt, 8 Tetraeder),
        D1x/D1y/D1z (nur eine Diagonale). Kontrollen: K (ew 'ohne' wie TT-ISO-1 Kontrolle c), V (Spanne 6,339 %).
Teil B  beschreibend: Diagonalwahl als Drei-Zustands-Feld (Dieder, Schur, Kinetik), duale Zellen (umkreisbasierte
        Hodge-Gewichte der Rhombendodekaeder, Takt-Operator W^+ B W gegen *1-Laplace).
Aufruf (nur ueber kleintest.sh):
  python okta.py licht  --out lauf/licht.json  [--klein] [--rauch]
  python okta.py schwer --out lauf/schwer.json [--klein] [--rauch]
  python okta.py bild --licht lauf/licht.json --schwer lauf/schwer.json --png lauf/bild.png
Koordinaten wie ew.py: kubische Kante 1, Orte ganzzahlig in Einheiten 1/8. Licht in l = Pyrochlorkante = 1.
"""
import argparse
import hashlib
import itertools
import json
import math
import os
import platform
import resource
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402  (TENSOR-EIS-PYRO-1, unveraendert)
import ew  # noqa: E402  (EINE-WELT-LOCH-1, unveraendert)
import licht_netz as ln  # noqa: E402  (LICHT-FINN-NETZ-1, unveraendert)
import tti  # noqa: E402  (TT-ISO-1, unveraendert)

R8, AV, BV = tp.R8, tp.AV, tp.BV
E3 = np.eye(3, dtype=int)
LP = math.sqrt(2.0) / 4.0          # Pyrochlorkante in kubischen Einheiten
SK = 1.0 / LP                      # kubisch -> l (Tetraederkante = 1)
TOL_NULL = 1e-10                   # Nullmode: |omega^2| <= TOL_NULL * max|omega^2| am selben k
TOL_FLACH = 1e-9                   # flaches Band: ein Wert kommt an allen k vor (innerhalb TOL_FLACH * S)
ISO_C = 1e-6                       # OS1 (ii): Spannweite rel. des langwelligen Tempos
EPS = (1e-3, 2e-3)
HAND = {'dreieck': 2.0 * math.sqrt(2.0), 'sechseck': math.sqrt(2.0) / 3.0, 'kante': math.sqrt(2.0)}  # PLAN 1.2 [M]
OS_SOLL_V = 0.06339                # TT-ISO-1 TB0, V A1R1 J = 1, max/min - 1 (Kartenwert 6,34 %)
T_START = time.time()


def js(x):
    return ln.js(x)


def herm(X):
    return 0.5 * (X + np.conj(np.swapaxes(X, -1, -2)))


def ops48():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            Rm = np.zeros((3, 3))
            for i in range(3):
                Rm[i, perm[i]] = sg[i]
            out.append(Rm)
    return out


N0 = np.array([0.26, 0.45, 0.85]) / np.linalg.norm([0.26, 0.45, 0.85])


# ================================================================================================ Teil L: Geometrie
def pyro_geometrie():
    pos8 = [R8[a].astype(int) for a in range(4)]
    auf = [R8[a].astype(int) for a in range(4)]
    ab = [np.array([2, 2, 2]) - R8[b] for b in range(4)]
    dreiecke = [[t[i], t[j], t[m]] for t in (auf, ab) for (i, j, m) in itertools.combinations(range(4), 3)]
    C1 = np.array([-2, -2, -2])
    sechsecke = []
    for a in range(4):
        sechs = [C1 + 2 * R8[b] + R8[d] for b in range(4) for d in range(4) if a not in (b, d) and b != d]
        sechsecke.append(ew.sechseck_zyklus(sechs))
    return pos8, dreiecke, sechsecke


def pyro_zellen(n=2):
    """Zellen (Art, Mitte x8, Eckenmenge x8) aller Gittertranslationen in [-n, n]^3."""
    U, D = np.zeros(3, int), np.array([2, 2, 2])
    C1, C2 = np.array([-2, -2, -2]), np.array([4, 4, 4])
    basis = [('finn_auf', U, [U + R8[a] for a in range(4)]),
             ('finn_ab', D, [D - R8[b] for b in range(4)]),
             ('stumpf_T1', C1, [C1 + 2 * R8[b] + R8[d] for b in range(4) for d in range(4) if b != d]),
             ('stumpf_T2', C2, [C2 - 2 * R8[b] - R8[d] for b in range(4) for d in range(4) if b != d])]
    out = []
    for nn in itertools.product(range(-n, n + 1), repeat=3):
        T8 = np.array(nn) @ ew.AV8
        for art, m, ecken in basis:
            out.append((art, np.asarray(m + T8, float), {tuple(int(v) for v in (x + T8)) for x in ecken},
                        [np.asarray(x + T8, float) for x in ecken]))
    return out


class Komplex:
    """Kanten (kanonisch wie ew.baue), Plaketten als Zyklen; Bloch-Matrizen C(k), d0(k) (k in kubischen Einheiten)."""

    def __init__(self, pos8):
        self.pos8 = [np.asarray(p, int) for p in pos8]
        self.idx, self.kl, self.flaechen = {}, [], []

    def kante(self, a8, b8):
        (si, ni), (sj, nj) = ew.zerlege(a8, self.pos8), ew.zerlege(b8, self.pos8)
        d = tuple(int(v) for v in np.subtract(nj, ni))
        k1, k2 = (si, sj, d), (sj, si, tuple(-v for v in d))
        key = min(k1, k2)
        if key not in self.idx:
            self.idx[key] = len(self.kl)
            self.kl.append(key)
        sg = 1 if key == k1 else -1
        T = np.array(ni if key == k1 else nj, float) @ AV
        return self.idx[key], sg, T

    def flaeche(self, art, punkte):
        z = [self.kante(punkte[i], punkte[(i + 1) % len(punkte)]) for i in range(len(punkte))]
        self.flaechen.append((art, z, [np.asarray(p, int) for p in punkte]))

    def endpunkte8(self, e):
        s, s2, d = self.kl[e]
        return self.pos8[s].astype(float), self.pos8[s2] + np.array(d) @ ew.AV8

    def C(self, k, arten):
        rows = [f for f in self.flaechen if f[0] in arten]
        C = np.zeros((len(rows), len(self.kl)), complex)
        for p, (art, z, _) in enumerate(rows):
            for e, sg, T in z:
                C[p, e] += sg * np.exp(1j * (k @ T))
        return C, [r[0] for r in rows]

    def d0(self, k):
        G = np.zeros((len(self.kl), len(self.pos8)), complex)
        for e, (s, s2, d) in enumerate(self.kl):
            G[e, s2] += np.exp(1j * (k @ (np.array(d, float) @ AV)))
            G[e, s] -= 1.0
        return G


def pyro_komplex():
    pos8, dr, se = pyro_geometrie()
    kx = Komplex(pos8)
    for p in dr:
        kx.flaeche('dreieck', p)
    for p in se:
        kx.flaeche('sechseck', p)
    return kx


def polygon_flaeche(P, mitte=None):
    P = np.asarray(P, float)
    m = P.mean(0) if mitte is None else mitte
    s = np.zeros(3)
    for i in range(len(P)):
        s += np.cross(P[i] - m, P[(i + 1) % len(P)] - m)
    return 0.5 * float(np.linalg.norm(s)), s


def um_achse_sortiert(punkte, a, b):
    t = (b - a) / np.linalg.norm(b - a)
    m = 0.5 * (a + b)
    u = np.cross(t, [0.3, 0.5, 0.7])
    u /= np.linalg.norm(u)
    v = np.cross(t, u)
    w = [math.atan2((p - m) @ v, (p - m) @ u) for p in punkte]
    return [punkte[i] for i in np.argsort(w)], m, t


def umkreismitte(X):
    X = np.asarray(X, float)
    if len(X) == 4:
        A = 2.0 * (X[1:] - X[0])
        b = (X[1:] ** 2).sum(1) - (X[0] ** 2).sum()
        return np.linalg.solve(A, b)
    return X.mean(0)


def duale_masse(kx, zellen, skal, zellvolumen):
    """Umkreisbasierte duale Masse je Kante (*1) und Plakette (*2); zellen: (Art, Mitte, Eckenmenge, Ecken)."""
    mitten = [umkreismitte(Z[3]) for Z in zellen]
    umk_abw = max(float(np.ptp([np.linalg.norm(x - m) for x in Z[3]])) for Z, m in zip(zellen, mitten))
    kanten = []
    for e in range(len(kx.kl)):
        a, b = kx.endpunkte8(e)
        ta, tb = tuple(int(v) for v in np.rint(a)), tuple(int(v) for v in np.rint(b))
        cs = [m for Z, m in zip(zellen, mitten) if ta in Z[2] and tb in Z[2]]
        arts = sorted(Z[0] for Z in zellen if ta in Z[2] and tb in Z[2])
        cs_s, mm, t = um_achse_sortiert(cs, a, b)
        A, _ = polygon_flaeche(cs_s, mitte=mm)
        eben = max(abs(float((c - mm) @ t)) for c in cs) if cs else None
        le = float(np.linalg.norm(b - a))
        kanten.append({'e': e, 'zellen': arts, 'n_zellen': len(cs), 'laenge': le * skal, 'dual_flaeche': A * skal ** 2,
                       'stern1': A * skal ** 2 / (le * skal), 'abstand_von_mittelebene_max': eben,
                       'richtung': ((b - a) / le).tolist()})
    flaechen = []
    for art, z, punkte in kx.flaechen:
        P = [tuple(int(v) for v in p) for p in punkte]
        cs = [m for Z, m in zip(zellen, mitten) if all(p in Z[2] for p in P)]
        A, nv = polygon_flaeche(np.array(punkte, float))
        if len(cs) == 2:
            dv = cs[0] - cs[1]
            dl = float(np.linalg.norm(dv))
            senk = float(np.linalg.norm(np.cross(dv, nv)) / max(dl * np.linalg.norm(nv), 1e-300)) if dl > 0 else 0.0
        else:
            dl, senk = None, None
        flaechen.append({'art': art, 'n_zellen': len(cs), 'flaeche': A * skal ** 2,
                         'dual_laenge': None if dl is None else dl * skal,
                         'stern2': None if dl is None else dl * skal / (A * skal ** 2), 'nicht_senkrecht': senk,
                         'normale': (nv / max(np.linalg.norm(nv), 1e-300)).tolist()})
    V = zellvolumen * (8.0 * skal) ** 3          # zellvolumen in kubischen Einheiten, skal: x8 -> Zielmass
    s1 = sum(k['laenge'] * k['dual_flaeche'] / 3.0 for k in kanten)
    s2 = sum(f['flaeche'] * f['dual_laenge'] / 3.0 for f in flaechen if f['dual_laenge'] is not None)
    T1 = sum(k['stern1'] * k['laenge'] ** 2 * np.outer(k['richtung'], k['richtung']) for k in kanten)
    T2 = sum(f['stern2'] * f['flaeche'] ** 2 * np.outer(f['normale'], f['normale']) for f in flaechen
             if f['stern2'] is not None)
    return {'kanten': kanten, 'flaechen': flaechen, 'zellvolumen': V, 'umkreis_abw_max': umk_abw,
            'summe_kanten_rauten_durch_V': s1 / V, 'summe_flaechen_doppelpyramiden_durch_V': s2 / V,
            'patch_1form_abw': float(np.abs(T1 / V - np.eye(3)).max()),
            'patch_2form_abw': float(np.abs(T2 / V - np.eye(3)).max()) if len(flaechen) else None}


# ================================================================================================ Teil L: Spektren
def licht_ev(kx, k_c, w, s1):
    """Physikalische omega^2 (in 1/l^2) bei k (kubische Einheiten); Gewichte w je Plakettenart in l-Einheiten."""
    arten = [a for a in ('dreieck', 'sechseck') if w.get(a, 0.0) != 0.0]
    C, rows = kx.C(k_c, arten)
    W = np.array([w[a] for a in rows])
    K = C.conj().T @ (W[:, None] * C)
    G = kx.d0(k_c)
    U, s, _ = np.linalg.svd(G)
    r = int((s > 1e-9 * s.max()).sum()) if s.max() > 0 else 0
    Q = U[:, r:]
    return np.linalg.eigvalsh(herm(Q.conj().T @ K @ Q)) / s1, r


def kliste_licht(L, nzuf, seed, richt, kl_l):
    g = np.arange(L)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    kg = (mm / L) @ BV
    rng = np.random.default_rng(seed)
    kz = rng.uniform(0, 1, (nzuf, 3)) @ BV
    kk = [k * d / LP for k in kl_l for d in richt]
    return np.concatenate([kg, kz, np.array(kk).reshape(-1, 3)], 0)


def flach_zaehlung(EV):
    """EV (nk, nb). Flache Baender: Werte, die an allen k mit fester Vielfachheit vorkommen (kreuzungsfest)."""
    S = max(float(np.abs(EV).max()), 1e-300)
    kand = []
    for v in np.sort(EV[0]):
        if not kand or abs(v - kand[-1]) > TOL_FLACH * S:
            kand.append(float(v))
    out = []
    for v in kand:
        tr = np.abs(EV - v) <= TOL_FLACH * S
        m = int(tr.sum(1).min())
        if m > 0:
            out.append({'wert': float(np.median(EV[tr])), 'vielfachheit': m,
                        'breite_rel': float((EV[tr].max() - EV[tr].min()) / S), 'null': bool(abs(v) <= 1e-9 * S)})
    return {'S': S, 'baender': out, 'n_flach': int(sum(b['vielfachheit'] for b in out)),
            'n_flach_null': int(sum(b['vielfachheit'] for b in out if b['null'])),
            'n_flach_nicht_null': int(sum(b['vielfachheit'] for b in out if not b['null']))}


def baender_analyse(kx, w, s1, kliste):
    EV, rr = [], []
    for k in kliste:
        ev, r = licht_ev(kx, k, w, s1)
        EV.append(ev)
        rr.append(r)
    EV = np.array(EV)
    nnull = [int((np.abs(e) <= TOL_NULL * max(np.abs(e).max(), 1e-300)).sum()) for e in EV]
    fl = flach_zaehlung(EV)
    return {'nk': int(len(kliste)), 'n_phys_je_k': sorted(set(int(EV.shape[1]) for _ in [0])),
            'eichrang_verteilung': {str(v): int(rr.count(v)) for v in sorted(set(rr))},
            'nullmoden_verteilung': {str(v): int(nnull.count(v)) for v in sorted(set(nnull))},
            'nullmoden_max': int(max(nnull)), 'nullmoden_min': int(min(nnull)), 'flach': fl,
            'omega2_min': float(EV.min()), 'omega2_max': float(EV.max()),
            'kleinster_nicht_null_rel': float(min(min([x for x in e if abs(x) > TOL_NULL * np.abs(e).max()], default=np.inf)
                                                  for e in EV) / fl['S'])}


def bandpfad(kx, w, s1, n=30):
    G0 = np.zeros(3)
    X = 2 * np.pi * np.array([1.0, 0, 0])
    W = 2 * np.pi * np.array([1.0, 0.5, 0])
    Lp = np.pi * np.ones(3)
    K = 1.5 * np.pi * np.array([1.0, 1, 0])
    ecken = [('G', G0), ('X', X), ('W', W), ('L', Lp), ('G', G0), ('K', K)]
    xs, oms, marken = [], [], [(ecken[0][0], 0.0)]
    x0 = 0.0
    for (na, a), (nb, b) in zip(ecken[:-1], ecken[1:]):
        for t in np.linspace(0, 1, n, endpoint=False):
            k = a + t * (b - a)
            if np.linalg.norm(k) < 1e-12:
                k = a + 1e-4 * (b - a) / np.linalg.norm(b - a)
            ev, _ = licht_ev(kx, k, w, s1)
            xs.append(x0 + t * np.linalg.norm(b - a) * LP)
            oms.append(np.sqrt(np.maximum(ev, 0.0)))
        x0 += np.linalg.norm(b - a) * LP
        marken.append((nb, x0))
    return {'x': xs, 'omega': [list(o) for o in oms], 'marken': marken}


def photon_op(kx, w, s1):
    def f(k_l):
        ev, _ = licht_ev(kx, np.asarray(k_l, float) / LP, w, s1)
        return [math.sqrt(max(v, 0.0)) for v in ev[:2]]
    return f, 2


def disp_kurz(erg):
    out = {'zweige': []}
    for z, zz in enumerate(erg['fenster']['W0']):
        jr = zz['je_richtung']
        kl = {}
        for cls in ('100', '110', '111'):
            v = [e['a2'] for e in jr if e['klasse'] == cls and e.get('a2') is not None]
            kl[cls] = {'mittel': float(np.mean(v)), 'spannweite': float(np.max(v) - np.min(v))} if v else None
        out['zweige'].append({'c': zz['voll']['c'], 'a1': zz['voll']['a1'], 'a2': zz['voll']['a2'],
                              'a3': zz['voll']['a3'], 'a4': zz['voll']['a4'], 'a2_klassen': kl,
                              'rms_rel': zz['voll']['rms_rel'], 'gueltige_richtungen': zz['gueltige_richtungen']})
    w0 = erg['fenster']['W0']
    if len(w0) == 2:
        d = [abs(a['a2'] - b['a2']) for a, b in zip(w0[0]['je_richtung'], w0[1]['je_richtung'])
             if a.get('a2') is not None and b.get('a2') is not None]
        out['doppelbrechung_a2_max'] = float(max(d)) if d else None
        dc = [abs(a['c'] - b['c']) for a, b in zip(w0[0]['je_richtung'], w0[1]['je_richtung'])]
        out['doppelbrechung_c_max'] = float(max(dc))
    proben = {}
    for fen in erg['fenster']:
        if fen == 'W0':
            continue
        dm = 0.0
        for z in range(len(w0)):
            for a, b in zip(w0[z]['je_richtung'], erg['fenster'][fen][z]['je_richtung']):
                if a.get('a2') is not None and b.get('a2') is not None:
                    dm = max(dm, abs(a['a2'] - b['a2']))
        proben[fen] = dm
    out['a2_abw_probefenster'] = proben
    if 'kugel_a2_W0' in erg:
        out['kugel_a2'] = erg['kugel_a2_W0']
    return out


def symm48_licht(kx, w, s1, kl=0.2):
    om = []
    for Rm in ops48():
        ev, _ = licht_ev(kx, kl * (Rm @ N0) / LP, w, s1)
        om.append(np.sqrt(np.maximum(ev, 0.0)))
    om = np.array(om)
    return {'k_l': kl, 'abw_rel_max': float(np.abs(om - om[0]).max() / np.abs(om[0]).max())}


def lauf_licht(klein=False, rauch=False):
    t0 = time.time()
    if klein:
        ln.FENSTER = {"W0": (0.01, 0.30, 12, 6)}
    kx = pyro_komplex()
    zellen = pyro_zellen(2)
    dm = duale_masse(kx, zellen, SK / 8.0, 0.25)
    st1 = [k['stern1'] for k in dm['kanten']]
    st2d = [f['stern2'] for f in dm['flaechen'] if f['art'] == 'dreieck']
    st2h = [f['stern2'] for f in dm['flaechen'] if f['art'] == 'sechseck']
    w_dec = {'dreieck': float(np.mean(st2d)), 'sechseck': float(np.mean(st2h))}
    s1_dec = float(np.mean(st1))
    geo = {'E': len(kx.kl), 'V': len(kx.pos8), 'F_dreieck': sum(1 for f in kx.flaechen if f[0] == 'dreieck'),
           'F_sechseck': sum(1 for f in kx.flaechen if f[0] == 'sechseck'),
           'kantenlaengen_l': sorted(set(round(k['laenge'], 12) for k in dm['kanten'])),
           'zellen_je_kante': sorted(set(tuple(k['zellen']) for k in dm['kanten'])),
           'zellen_je_flaeche': sorted(set(f['n_zellen'] for f in dm['flaechen'])),
           'stern1': [min(st1), max(st1)], 'stern2_dreieck': [min(st2d), max(st2d)],
           'stern2_sechseck': [min(st2h), max(st2h)],
           'hand_abw': {'dreieck': abs(w_dec['dreieck'] - HAND['dreieck']), 'sechseck': abs(w_dec['sechseck'] - HAND['sechseck']),
                        'kante': abs(s1_dec - HAND['kante'])},
           'duale': {k: v for k, v in dm.items() if k not in ('kanten', 'flaechen')},
           'mittelebene_max': max(k['abstand_von_mittelebene_max'] for k in dm['kanten']),
           'nicht_senkrecht_max': max(f['nicht_senkrecht'] for f in dm['flaechen'] if f['nicht_senkrecht'] is not None)}
    rng = np.random.default_rng([46, 1])
    cd = 0.0
    for _ in range(20):
        k = rng.normal(size=3) * 3
        C, _ = kx.C(k, ('dreieck', 'sechseck'))
        cd = max(cd, float(np.abs(C @ kx.d0(k)).max()))
    geo['rot_grad_max'] = cd
    out = {'geometrie': geo, 'gewichte_dec': {'w': w_dec, 's1': s1_dec, 'verhaeltnis_H_D': w_dec['sechseck'] / w_dec['dreieck']}}
    varianten = {'ohne': ({'dreieck': w_dec['dreieck']}, s1_dec), 'dec': (w_dec, s1_dec),
                 'ohne_eins': ({'dreieck': 1.0}, 1.0), 'eins': ({'dreieck': 1.0, 'sechseck': 1.0}, 1.0)}
    richt = ln.richtungen26()
    r13 = [d for _, d in tti.richtungen13()]
    if klein:
        klist = kliste_licht(2, 5, 46, r13[:2], (1e-3, 1e-1))
    else:
        klist = kliste_licht(8, 200, 46, list(richt), (1e-3, 1e-2, 1e-1))
    out['kliste_n'] = int(len(klist))
    out['varianten'] = {}
    for name, (w, s1) in varianten.items():
        v = {'w': w, 's1': s1, 'baender': baender_analyse(kx, w, s1, klist)}
        v['bandpfad'] = bandpfad(kx, w, s1, n=(6 if klein else 30))
        out['varianten'][name] = v
    # Dispersion der Photonen (nur mit Sechsecken; ohne Sechsecke gibt es kein laufendes Licht)
    for name in ('dec', 'eins'):
        w, s1 = varianten[name]
        op, nz = photon_op(kx, w, s1)
        erg = ln.operator_auswerten('P-' + name, op, nz, richt if not klein else richt[:3],
                                    kugel=(None if klein else ln.fib(200)), mit_kurven=False)
        out['varianten'][name]['dispersion'] = disp_kurz(erg)
        out['varianten'][name]['dispersion_voll'] = erg
        out['varianten'][name]['symm48'] = symm48_licht(kx, w, s1)
    # Abtastung w_H / w_D (beschreibend)
    verh = [0.0, 1e-3, 1e-2, 1e-1, 1.0 / 6.0, 1.0, 10.0, 100.0]
    kl_s = kliste_licht(4, 50, 47, r13[:3], (1e-3,)) if not klein else kliste_licht(2, 3, 47, r13[:1], (1e-3,))
    ab = []
    for q in verh:
        w = {'dreieck': w_dec['dreieck'], 'sechseck': q * w_dec['dreieck']}
        ba = baender_analyse(kx, w, s1_dec, kl_s)
        cs = []
        for d in (r13 if not klein else r13[:2]):
            ev, _ = licht_ev(kx, 1e-3 * d / LP, w, s1_dec)
            cs.append(np.sqrt(np.maximum(ev[:2], 0.0)) / 1e-3)
        cs = np.array(cs)
        ab.append({'w_H_durch_w_D': q, 'n_flach': ba['flach']['n_flach'], 'n_flach_null': ba['flach']['n_flach_null'],
                   'flache_werte': [b['wert'] for b in ba['flach']['baender']], 'nullmoden_max': ba['nullmoden_max'],
                   'c_k1e-3_mittel': float(cs.mean()), 'c_k1e-3_spannweite_rel': float(np.ptp(cs) / max(cs.mean(), 1e-300))})
    out['abtastung'] = ab
    # Kontrolle KL: Maxwell M-D von LICHT-FINN-NETZ-1 mit dem kopierten Fit (a2 = -1/12, -5/48, -1/9)
    C_d, G_d, nk_d, nringe = ln.maxwell_diamant()
    op, nz = ln.op_maxwell(C_d, nk_d)
    em = ln.operator_auswerten('M-D', op, nz, richt if not klein else richt[:3], kugel=None, mit_kurven=False)
    soll = {'100': -1.0 / 12.0, '110': -5.0 / 48.0, '111': -1.0 / 9.0}
    abw = 0.0
    for zz in em['fenster']['W0']:
        for e in zz['je_richtung']:
            abw = max(abw, abs(e['a2'] - soll[e['klasse']]))
    out['kontrolle_KL'] = {'a2_abw_max': abw, 'ok': bool(abw < 1e-6), 'sechsringe': nringe}
    out['urteile'] = urteile_licht(out) if not klein else None
    out['laufzeit_s'] = time.time() - t0
    return out


def urteile_licht(o):
    u = {}
    oh = o['varianten']['ohne']['baender']
    os0_plan = (oh['nullmoden_min'] == 2 and oh['nullmoden_max'] == 2 and oh['flach']['n_flach_null'] == 2)
    os0_wort = (oh['flach']['n_flach'] == 2)
    u['OS0'] = {'plan': 'eingetroffen' if os0_plan else 'nicht eingetroffen',
                'karte': 'eingetroffen' if os0_wort else 'nicht eingetroffen',
                'nullmoden_je_k': oh['nullmoden_verteilung'], 'n_flach_null': oh['flach']['n_flach_null'],
                'n_flach': oh['flach']['n_flach'], 'flache_werte': [b['wert'] for b in oh['flach']['baender']]}
    de = o['varianten']['dec']
    b = de['baender']
    i_plan = (b['nullmoden_max'] == 0 and b['flach']['n_flach_null'] == 0)
    i_wort = (b['flach']['n_flach'] == 0 and b['nullmoden_max'] == 0)
    zw = de['dispersion']['zweige']
    iso = [z['c']['spannweite_rel'] for z in zw]
    ii = all(x is not None and x < ISO_C for x in iso)

    def u2(a, bb):
        return 'eingetroffen' if (a and bb) else ('nicht eingetroffen' if not (a or bb) else 'geteilt')
    u['OS1'] = {'plan': u2(i_plan, ii), 'karte': u2(i_wort, ii), 'teil_i_plan_nullbaender_weg': i_plan,
                'teil_i_karte_alle_flachen_weg': i_wort, 'teil_ii_tempo_isotrop': ii, 'c_spannweite_rel': iso,
                'c_mittel': [z['c']['mittel'] for z in zw], 'nullmoden_max': b['nullmoden_max'],
                'n_flach': b['flach']['n_flach'], 'flache_werte': [x['wert'] for x in b['flach']['baender']]}
    return u


# ================================================================================================ Teil T: Tetraeder-Oktaeder-Wabe
D0 = np.array([2, 2, 2])
C1T = np.array([-2, -2, -2])
C2T = np.array([4, 4, 4])
EW_GEO = ew.geometrie


def okt_ecken(C):
    return [C + 4 * E3[0], C - 4 * E3[0], C + 4 * E3[1], C - 4 * E3[1], C + 4 * E3[2], C - 4 * E3[2]]


def viertel(C, ax):
    X = okt_ecken(C)
    N, S = X[2 * ax], X[2 * ax + 1]
    j, m = [i for i in range(3) if i != ax]
    ring = [C + 4 * E3[j], C + 4 * E3[m], C - 4 * E3[j], C - 4 * E3[m]]
    return [[N, S, ring[i], ring[(i + 1) % 4]] for i in range(4)]


def geo_toh(var):
    def geo(_f):
        pos8 = [D0.copy()]
        zellen = [ew.tet([2 * R8[a] for a in range(4)], kin=True, art='tet_auf'),
                  ew.tet([C2T - 2 * R8[a] for a in range(4)], kin=True, art='tet_ab')]
        if var == 'R12':
            z = ew.okt(C1T)
            z['kin'] = True
            zellen.append(z)
        elif var in ('H3', 'D1x', 'D1y', 'D1z'):
            achsen = (0, 1, 2) if var == 'H3' else ({'D1x': 0, 'D1y': 1, 'D1z': 2}[var],)
            for ax in achsen:
                for t in viertel(C1T, ax):
                    z = ew.tet(t, kin=True, art='okt_d%d' % ax)
                    z['gewicht'] = 1.0 / len(achsen)
                    zellen.append(z)
        elif var == 'Z8':
            pos8.append(C1T.copy())
            X = okt_ecken(C1T)
            for sx in (0, 1):
                for sy in (0, 1):
                    for sz in (0, 1):
                        zellen.append(ew.tet([C1T, X[sx], X[2 + sy], X[4 + sz]], kin=True, art='okt_z'))
        else:
            raise ValueError(var)
        return pos8, zellen
    return geo


def baue_toh(var):
    ew.geometrie = geo_toh(var)
    try:
        mod = ew.baue('toh-' + var)
    finally:
        ew.geometrie = EW_GEO
    for z in mod['zellen']:
        g = z.get('gewicht', 1.0)
        z['Dl'] = g * z['Dl']
        z['A0'] = g * z['A0']
    mod['variante'] = var
    return mod


def zell_kontrolle(mod):
    out = {'E': mod['E'], 'V': mod['nV'], 'T': mod['nT'], 'arten': {}}
    for z in mod['zellen']:
        out['arten'][z['art']] = out['arten'].get(z['art'], 0) + 1
    vol = sum(z.get('gewicht', 1.0) * (z['vol'] if z['vol'] is not None else 1.0 / 6.0) for z in mod['zellen'])
    out['volumen_gewichtet'] = float(vol)
    # Ebenheit je Zerlegung: Diedersumme 2 pi an jeder Kante des jeweiligen Komplexes
    arten = sorted(out['arten'])
    gruppen = [[a for a in arten if not a.startswith('okt_d')] + [d] for d in arten if d.startswith('okt_d')] or [arten]
    dmax = 0.0
    for gr in gruppen:
        summe = {}
        for z in mod['zellen']:
            if z['art'] not in gr:
                continue
            for (e, T), th in zip(z['kanten'], z['theta0']):
                summe[e] = summe.get(e, 0.0) + th
        dmax = max(dmax, max(abs(v - 2 * np.pi) for v in summe.values()))
    out['dieder_summe_minus_2pi_max'] = float(dmax)
    out['D_sym_max'] = max(float(np.abs(z['D'] - z['D'].T).max() / np.abs(z['D']).max()) for z in mod['zellen'])
    out['kantenlaengen'] = sorted(set(round(float(x), 9) for x in mod['l']))
    rng = np.random.default_rng([46, 2])
    k = rng.normal(size=(8, 3)) * 3
    out['ops'] = ew.kontrollen_ops(ew.ops(mod, k))
    return out


def red(mod, k):
    o = ew.ops(mod, k[None, :])
    B, A, M, c = o['B'][0], o['A'][0], o['M'][0], o['c'][0]
    U, r, s = ew.phys_basis_rr(M, c)
    S = U[:, r:]
    Sh = S.conj().T
    return S, herm(Sh @ A @ S), herm(Sh @ B @ S), M, int(r)


def z_werte(Ar, Br, eps):
    """Wie tti.auswerten (A1R1, ein J): 1/omega^2 = Eigenwerte von Z = L^-1 A_red^-1 L^-+, B_red = L L^+."""
    eB = np.linalg.eigvalsh(Br)
    if eB.min() <= 0:
        return None
    Li = np.linalg.inv(np.linalg.cholesky(Br))
    try:
        Ai = np.linalg.inv(Ar)
    except np.linalg.LinAlgError:
        Ai = np.linalg.pinv(Ar)
    ev = np.linalg.eigvalsh(herm(Li @ Ai @ Li.conj().T))
    evs = ev[np.argsort(-np.abs(ev))]
    top = evs[:2]
    return {'w': np.sort(1.0 / top) / eps ** 2, 'luecke': float(abs(evs[2]) / abs(evs[1])) if len(evs) > 2 else 0.0,
            'neg': bool((ev < 0).any()), 'pos2': bool((top > 0).all())}


def direkt(mod, S, Ar, Br, M, kk, eps):
    ww, vv = np.linalg.eig(Ar @ Br)
    o = np.argsort(ww.real)
    ww, vv = ww[o], vv[:, o]
    s = max(float(np.abs(ww).max()), 1e-300)
    kl, tt = [], []
    for j, x in enumerate(ww):
        if x.real < -1e-9 * s or abs(x.imag) > 1e-9 * s:
            c = 'wachsend'
        elif abs(x) <= 1e3 * eps ** 2:
            c = 'masselos'
        elif x.real >= 1e-4 * s and x.real >= 2e3 * eps ** 2:
            c = 'luecke'
        else:
            c = 'unklar'
        kl.append(c)
        if c == 'masselos':
            H, _ = ew.tensor_fit(mod, S @ vv[:, j], kk, M)
            tt.append(float(tp.tt_anteil(H, kk)[0]))
        else:
            tt.append(None)
    return {'w2_re': [float(x) for x in ww.real], 'w2_im_max': float(np.abs(ww.imag).max()), 'klasse': kl, 'tt': tt, 's': s}


def tt_punkte(mod, richt, epsl=EPS, mit_direkt=True):
    rows = []
    for nm, d in richt:
        for eps in epsl:
            kk = eps * np.asarray(d, float)
            S, Ar, Br, M, r = red(mod, kk)
            zw = z_werte(Ar, Br, eps)
            row = {'richtung': nm, 'eps': eps, 'dim': int(S.shape[1]), 'rang': r,
                   'z': None if zw is None else {'w': zw['w'].tolist(), 'luecke': zw['luecke'], 'neg': zw['neg'],
                                                 'pos2': zw['pos2']}}
            if mit_direkt:
                row['direkt'] = direkt(mod, S, Ar, Br, M, kk, eps)
            rows.append(row)
    return rows


def spanne(rows, eps=None):
    w = [r['z']['w'] for r in rows if r['z'] is not None and (eps is None or r['eps'] == eps)]
    if not w or any(r['z'] is None for r in rows):
        return None
    w = np.array(w)
    return float(w.max() / w.min() - 1.0)


def z_gueltig(rows):
    return bool(all(r['z'] is not None and r['z']['pos2'] and not r['z']['neg'] and r['z']['luecke'] < tti.LUECKE_MAX
                    for r in rows))


def richardson(rows):
    """w0 = (4 w(1e-3) - w(2e-3)) / 3 je Richtung und Zweig (beschreibend)."""
    by = {}
    for r in rows:
        if r['z'] is not None:
            by.setdefault(r['richtung'], {})[r['eps']] = np.array(r['z']['w'])
    w0 = [(4 * v[EPS[0]] - v[EPS[1]]) / 3.0 for v in by.values() if EPS[0] in v and EPS[1] in v]
    if not w0:
        return None
    w0 = np.array(w0)
    return {'spanne': float(w0.max() / w0.min() - 1.0), 'mittel': float(w0.mean()), 'min': float(w0.min()),
            'max': float(w0.max())}


def os2_regel(rows):
    """EW1-Regel (EINE-WELT-LOCH-1 PLAN 3) an allen Punkten: genau 2 masselose TT, sonst Luecke, nichts wachsend."""
    gruende = []
    by = {}
    for r in rows:
        by.setdefault(r['richtung'], {})[r['eps']] = r
    for nm, pe in by.items():
        mw, lu = {}, {}
        for eps, r in pe.items():
            d = r['direkt']
            kl = d['klasse']
            if any(c in ('wachsend', 'unklar') for c in kl):
                gruende.append('%s eps %g: %s' % (nm, eps, ','.join(c for c in kl if c in ('wachsend', 'unklar'))))
            m = [j for j, c in enumerate(kl) if c == 'masselos']
            if len(m) != 2:
                gruende.append('%s eps %g: %d masselos' % (nm, eps, len(m)))
            for j in m:
                if not (d['w2_re'][j] > 1e-9 * d['s'] and d['tt'][j] is not None and d['tt'][j] >= 0.99):
                    gruende.append('%s eps %g: masselos nicht TT (tt %s)' % (nm, eps, d['tt'][j]))
            mw[eps] = sorted(d['w2_re'][j] for j in m)
            lv = [d['w2_re'][j] for j, c in enumerate(kl) if c == 'luecke']
            lu[eps] = min(lv) if lv else None
        if EPS[0] in mw and EPS[1] in mw and len(mw[EPS[0]]) == len(mw[EPS[1]]) == 2:
            for a, b in zip(mw[EPS[0]], mw[EPS[1]]):
                if not abs(b / (4 * a) - 1) <= 0.01:
                    gruende.append('%s: nicht linear (%g)' % (nm, b / (4 * a) - 1))
        if lu.get(EPS[0]) is not None and lu.get(EPS[1]) is not None:
            q = lu[EPS[1]] / lu[EPS[0]]
            if not 0.5 <= q <= 2:
                gruende.append('%s: Luecke nicht konstant (%g)' % (nm, q))
    n_masselos = sorted(set(sum(1 for c in r['direkt']['klasse'] if c == 'masselos') for r in rows))
    tt_min = min([t for r in rows for t in r['direkt']['tt'] if t is not None], default=None)
    return {'ok': not gruende, 'gruende': gruende[:20], 'n_gruende': len(gruende), 'n_masselos_werte': n_masselos,
            'tt_min': tt_min, 'n_punkte': len(rows),
            'n_wachsend': int(sum(sum(1 for c in r['direkt']['klasse'] if c == 'wachsend') for r in rows)),
            'w2_im_max_rel': float(max(r['direkt']['w2_im_max'] / r['direkt']['s'] for r in rows))}


def stabil_gitter(mod, L=8, chunk=128):
    g = np.arange(L)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    kall = (mm / L) @ BV
    nneg = nkom = bneg = aneg = 0
    wmin = np.inf
    dims = {}
    for i0 in range(0, len(kall), chunk):
        k = kall[i0:i0 + chunk]
        o = ew.ops(mod, k)
        for j in range(len(k)):
            U, r, s = ew.phys_basis_rr(o['M'][j], o['c'][j])
            S = U[:, r:]
            Sh = S.conj().T
            Br = herm(Sh @ o['B'][j] @ S)
            Ar = herm(Sh @ o['A'][j] @ S)
            aneg += int((np.linalg.eigvalsh(Ar) <= 0).any())
            bneg += int((np.linalg.eigvalsh(Br) <= 0).any())
            w2 = np.linalg.eigvals(Ar @ Br)
            sk = max(float(np.abs(w2).max()), 1e-300)
            nneg += int((w2.real < -1e-9 * sk).any())
            nkom += int((np.abs(w2.imag) > 1e-9 * sk).any())
            wmin = min(wmin, float(w2.real.min() / sk))
            dims[str(S.shape[1])] = dims.get(str(S.shape[1]), 0) + 1
    return {'L': L, 'nk': int(len(kall)), 'k_mit_negativ': nneg, 'k_mit_komplex': nkom, 'w2_min_rel': wmin,
            'k_mit_B_red_nicht_pd': bneg, 'k_mit_A_red_nicht_pd': aneg, 'dim_verteilung': dims}


def symm48_tt(mod, eps=1e-3):
    w = []
    for Rm in ops48():
        S, Ar, Br, M, r = red(mod, eps * (Rm @ N0))
        zw = z_werte(Ar, Br, eps)
        w.append(zw['w'] if zw is not None else np.array([np.nan, np.nan]))
    w = np.array(w)
    return {'abw_rel_max': float(np.nanmax(np.abs(w - w[0]) / w[0]))}


def affine_steifigkeit(mod, richt):
    """K(n) = a^+ B a / k^2 der affinen TT-Welle (wie tti Kontrolle e), beschreibend."""
    zeilen = []
    for nm, d in richt:
        kk = 1e-3 * d
        o = ew.ops(mod, kk[None, :])
        u = np.cross(d, [0.3, 0.5, 0.7])
        u = u / np.linalg.norm(u)
        v = np.cross(d, u)
        hs = [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]
        ph = np.exp(1j * (mod['mitte'] @ kk))
        av = [np.array([nv @ h @ nv for nv in mod['n']]) * ph for h in hs]
        Km = np.array([[np.conj(a1) @ o['B'][0] @ a2 for a2 in av] for a1 in av]) / 1e-6
        zeilen.append(np.linalg.eigvalsh(herm(Km)).tolist())
    a = np.array(zeilen)
    return {'min': float(a.min()), 'max': float(a.max()), 'spanne': float(a.max() / a.min() - 1)}


def v_referenz(richt13):
    netz = tti.Netz('V')
    J1 = np.ones(len(netz.arten))
    w, neg, lu, ok, nn, ee = tti.w2_klein(netz, tti.g_eins(netz), 'A1R1', J1, richt13)
    sp_tti = float(np.nanmax(w) / np.nanmin(w) - 1)
    mod = ew.baue('V')
    rows = tt_punkte(mod, richt13, mit_direkt=False)
    return {'spanne_tti': sp_tti, 'spanne_eigene_kette': spanne(rows), 'tti_ok': bool(ok), 'tti_neg': int(neg),
            'abw_eigene_gegen_tti': abs(spanne(rows) - sp_tti), 'abw_gegen_6339': abs(sp_tti - OS_SOLL_V),
            'w100': w[0].tolist(), 'mittel': float(np.nanmean(w))}


def k_kontrolle(richt13):
    mod = ew.baue('ohne')
    alle = []
    for nm, d in richt13:
        for eps in EPS:
            S, Ar, Br, M, r = red(mod, eps * d)
            ww = np.linalg.eigvals(Ar @ Br)
            alle += list(ww.real / eps ** 2)
    alle = np.array(alle)
    return {'n': int(len(alle)), 'min': float(alle.min()), 'max': float(alle.max()),
            'abw_0_25_max': float(np.abs(alle - 0.25).max()), 'ok': bool(np.abs(alle - 0.25).max() <= 2.5e-4)}


def schur_vergleich(mod_d, mod_r, kliste):
    idx_r = {key: i for i, key in enumerate(mod_r['kliste'])}
    aussen = [i for i, key in enumerate(mod_d['kliste']) if key in idx_r]
    innen = [i for i, key in enumerate(mod_d['kliste']) if key not in idx_r]
    perm = [idx_r[mod_d['kliste'][i]] for i in aussen]
    ab = 0.0
    Bd_all = ew.ops(mod_d, kliste)['B']
    Br_all = ew.ops(mod_r, kliste)['B']
    for Bd, Brr in zip(Bd_all, Br_all):
        Boo = Bd[np.ix_(aussen, aussen)]
        Boi = Bd[np.ix_(aussen, innen)]
        Bii = Bd[np.ix_(innen, innen)]
        Beff = Boo - Boi @ np.linalg.solve(Bii, Boi.conj().T)
        Bref = Brr[np.ix_(perm, perm)]
        ab = max(ab, float(np.abs(Beff - Bref).max() / np.abs(Bref).max()))
    return {'n_aussen': len(aussen), 'n_innen': len(innen), 'abw_rel_max': ab}


def toh_zellen(var, n=2):
    """Zellen (Art, Mitte, Eckenmenge, Ecken) der Variante fuer Translationen in [-n, n]^3 (Umkreismitten)."""
    basis = [('tet_auf', [2 * R8[a] for a in range(4)]), ('tet_ab', [C2T - 2 * R8[a] for a in range(4)])]
    if var == 'R12':
        basis.append(('okt', okt_ecken(C1T)))
    elif var.startswith('D1'):
        ax = {'D1x': 0, 'D1y': 1, 'D1z': 2}[var]
        basis += [('okt_d%d' % ax, t) for t in viertel(C1T, ax)]
    out = []
    for nn in itertools.product(range(-n, n + 1), repeat=3):
        T8 = np.array(nn) @ ew.AV8
        for art, ecken in basis:
            X = [np.asarray(x + T8, float) for x in ecken]
            out.append((art, None, {tuple(int(v) for v in x) for x in X}, X))
    return out


def toh_duale(var, mod):
    kx = Komplex([D0])
    for key in mod['kliste']:
        kx.idx[key] = len(kx.kl)
        kx.kl.append(key)
    zl = toh_zellen(var)
    # Plaketten: alle Dreiecke der Zellen (fuer *2), kanonisch ueber die Eckenmenge
    gesehen = set()
    for art, _, _, X in zl:
        if len(X) == 4:
            fl = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        else:
            fl = [(0 + sx, 2 + sy, 4 + sz) for sx in (0, 1) for sy in (0, 1) for sz in (0, 1)]
        for f in fl:
            P = [X[i] for i in f]
            sch = tuple(sorted(tuple(int(v) for v in p) for p in P))
            ref = np.array(sch[0])
            n = (ref - D0) @ ew.AV8INV
            if not np.allclose(n, np.rint(n)):
                continue
            T8 = np.rint(n) @ ew.AV8
            sch0 = tuple(sorted(tuple(int(v) for v in (np.array(p) - T8)) for p in sch))
            if sch0 in gesehen:
                continue
            gesehen.add(sch0)
            kx.flaechen.append(('dreieck', [], [np.array(p, int) - T8.astype(int) for p in sch0]))
    dm = duale_masse(kx, zl, 1.0 / 8.0, 0.25)
    return dm


def takt_vergleich(mod, stern1, kliste):
    """P(k) = W^+ B W mit W_e = (1 + e^{i k.T_e})/2 (Eckskalierung), L(k) = sum_e *1_e |1 - e^{i k.T_e}|^2."""
    T = np.array([np.array(d, float) @ AV for (s, s2, d) in mod['kliste']])
    o = ew.ops(mod, kliste)
    q = []
    for j, k in enumerate(kliste):
        ph = np.exp(1j * (T @ k))
        W = 0.5 * (1 + ph)
        P = float(np.real(np.conj(W) @ o['B'][j] @ W))
        L = float(np.sum(np.asarray(stern1) * np.abs(1 - ph) ** 2))
        q.append(P / L)
    q = np.array(q)
    return {'kappa_mittel': float(q.mean()), 'kappa_min': float(q.min()), 'kappa_max': float(q.max()),
            'spannweite_rel': float(np.ptp(q) / abs(q.mean()))}


def lauf_schwer(klein=False, rauch=False):
    t0 = time.time()
    r13 = tti.richtungen13()
    r23 = ew.richtungen()
    if klein:
        r13, r23 = r13[:2], r23[:2]
    out = {'varianten': {}, 'zeiten': {}}
    mods = {}
    for var in ('H3', 'R12', 'Z8', 'D1x', 'D1y', 'D1z'):
        t = time.time()
        mod = baue_toh(var)
        mods[var] = mod
        v = {'kontrolle': zell_kontrolle(mod)}
        if var in ('H3', 'R12', 'Z8', 'D1z'):
            v['p13'] = tt_punkte(mod, r13)
            v['p23'] = tt_punkte(mod, r23)
            v['spanne13'] = spanne(v['p13'])
            v['spanne13_je_eps'] = {str(e): spanne(v['p13'], e) for e in EPS}
            v['spanne23'] = spanne(v['p23'])
            v['z_gueltig13'] = z_gueltig(v['p13'])
            v['richardson13'] = richardson(v['p13'])
            v['os2_13'] = os2_regel(v['p13'])
            v['os2_23'] = os2_regel(v['p23'])
            v['mittel13'] = float(np.mean([r['z']['w'] for r in v['p13'] if r['z'] is not None])) if v['p13'] else None
            v['symm48'] = symm48_tt(mod)
            v['affin'] = affine_steifigkeit(mod, r13)
            v['stabil'] = stabil_gitter(mod, L=(2 if klein else 8))
        else:
            v['p13'] = tt_punkte(mod, r13, mit_direkt=False)
            v['spanne13'] = spanne(v['p13'])
        out['varianten'][var] = v
        out['zeiten'][var] = time.time() - t
    t = time.time()
    out['kontrolle_K'] = k_kontrolle(r13)
    out['zeiten']['K'] = time.time() - t
    t = time.time()
    out['referenz_V'] = v_referenz(r13)
    out['zeiten']['V'] = time.time() - t
    # Teil B (beschreibend)
    t = time.time()
    rng = np.random.default_rng([46, 3])
    kz = np.concatenate([rng.uniform(0, 1, (20, 3)) @ BV, 1e-3 * np.array([d for _, d in r13[:3]])], 0)
    out['diagonale'] = {'schur_gegen_R12': {v: schur_vergleich(mods[v], mods['R12'], kz) for v in ('D1x', 'D1y', 'D1z', 'H3')},
                        'dieder': {v: out['varianten'][v]['kontrolle']['dieder_summe_minus_2pi_max']
                                   for v in ('D1x', 'D1y', 'D1z', 'H3', 'R12', 'Z8')},
                        'spanne13': {v: out['varianten'][v]['spanne13'] for v in ('D1x', 'D1y', 'D1z', 'H3', 'R12')},
                        'w100_eps1e-3': {v: out['varianten'][v]['p13'][0]['z']['w'] if out['varianten'][v]['p13'][0]['z']
                                         else None for v in ('D1x', 'D1y', 'D1z', 'H3', 'R12')}}
    du = {}
    g = np.arange(8 if not klein else 2)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    kg = np.concatenate([(mm / (8 if not klein else 2)) @ BV, 1e-3 * np.array([d for _, d in r13])], 0)
    for var in ('R12', 'D1z'):
        dm = toh_duale(var, mods[var])
        st1 = [k['stern1'] for k in dm['kanten']]
        du[var] = {'stern1': st1, 'stern1_aussen': sorted(set(round(s, 12) for s, k in zip(st1, dm['kanten'])
                                                               if abs(k['laenge'] - math.sqrt(0.5)) < 1e-9)),
                   'stern1_diagonale': [s for s, k in zip(st1, dm['kanten']) if abs(k['laenge'] - 1.0) < 1e-9],
                   'zellen_je_kante': sorted(set(tuple(k['zellen']) for k in dm['kanten'])),
                   'stern2': sorted(set(round(f['stern2'], 12) for f in dm['flaechen'] if f['stern2'] is not None)),
                   'n_flaechen': len(dm['flaechen']),
                   'duale': {k: v for k, v in dm.items() if k not in ('kanten', 'flaechen')},
                   'rauten_flaeche': sorted(set(round(k['dual_flaeche'], 12) for k in dm['kanten']))}
        du[var]['takt'] = takt_vergleich(mods[var], st1, kg)
    st_aussen = du['R12']['stern1']
    stH = [st_aussen[mods['R12']['kliste'].index(key)] if key in mods['R12']['kliste'] else 0.0 for key in mods['H3']['kliste']]
    du['H3'] = {'takt': takt_vergleich(mods['H3'], stH, kg), 'stern1_diagonalen': 0.0}
    out['duale'] = du
    out['zeiten']['B'] = time.time() - t
    out['urteile'] = urteile_schwer(out) if not klein else None
    out['laufzeit_s'] = time.time() - t0
    return out


def urteile_schwer(o):
    u = {}
    h = o['varianten']['H3']
    ok2 = h['os2_13']['ok'] and h['os2_23']['ok']
    tts = [x for x in (h['os2_13']['tt_min'], h['os2_23']['tt_min']) if x is not None]
    u['OS2'] = {'plan': 'eingetroffen' if ok2 else 'nicht eingetroffen', 'karte': 'eingetroffen' if ok2 else 'nicht eingetroffen',
                'gruende_13': h['os2_13']['gruende'], 'gruende_23': h['os2_23']['gruende'],
                'n_masselos': sorted(set(h['os2_13']['n_masselos_werte'] + h['os2_23']['n_masselos_werte'])),
                'tt_min': min(tts) if tts else None}
    sp, ref = h['spanne13'], o['referenz_V']['spanne_tti']
    if sp is None or not h['z_gueltig13']:
        plan = 'nicht entscheidbar'
    else:
        plan = 'eingetroffen' if sp < ref else 'nicht eingetroffen'
    u['OS3'] = {'plan': plan, 'karte': ('nicht entscheidbar' if sp is None else
                                        ('eingetroffen' if sp < 0.0634 else 'nicht eingetroffen')),
                'spanne_H3': sp, 'spanne_V_neu': ref, 'z_gueltig': h['z_gueltig13']}
    u['beschreibend'] = {v: {'os2': (o['varianten'][v]['os2_13']['ok'] and o['varianten'][v]['os2_23']['ok']),
                             'spanne13': o['varianten'][v]['spanne13'], 'z_gueltig': o['varianten'][v]['z_gueltig13']}
                         for v in ('R12', 'Z8', 'D1z')}
    return u


# ================================================================================================ Bild
def bild(pl, ps, png):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with open(pl) as f:
        L = json.load(f)
    with open(ps) as f:
        S = json.load(f)
    fig, ax = plt.subplots(2, 2, figsize=(15, 10.5))
    # (a) Baender
    for var, col, lw, lab in (('ohne', 'tab:red', 2.6, 'ohne Sechsecke'), ('dec', 'tab:blue', 1.2, 'mit Sechsecken (DEC)')):
        bp = L['varianten'][var]['bandpfad']
        x = np.array(bp['x'])
        om = np.array(bp['omega'])
        for j in range(om.shape[1]):
            ax[0, 0].plot(x, om[:, j], '-', color=col, lw=lw, alpha=0.75, label=(lab if j == 0 else None))
    mk = L['varianten']['dec']['bandpfad']['marken']
    ax[0, 0].set_xticks([m[1] for m in mk])
    ax[0, 0].set_xticklabels([m[0].replace('G', 'Gamma') for m in mk])
    for m in mk:
        ax[0, 0].axvline(m[1], color='0.8', lw=0.6)
    ax[0, 0].set_ylabel('omega (1/l), DEC-Gewichte, c = 1 erwartet')
    ax[0, 0].set_title('(a) Licht auf den Pyrochlor-Kanten: physikalische Baender')
    ax[0, 0].legend(loc='upper right', fontsize=8)
    # (b) a2 je Richtung
    farbe = {'100': 'tab:blue', '110': 'tab:orange', '111': 'tab:green'}
    xt, xl = [], []
    x = 0
    for var in ('dec', 'eins'):
        er = L['varianten'][var]['dispersion_voll']
        for z, zz in enumerate(er['fenster']['W0']):
            for e in zz['je_richtung']:
                if e.get('a2') is None:
                    continue
                ax[0, 1].plot(x + 0.15 * (['100', '110', '111'].index(e['klasse']) - 1), e['a2'], 'o',
                              color=farbe[e['klasse']], ms=4)
            xt.append(x)
            xl.append('%s/%d' % (var, z))
            x += 1
    ax[0, 1].axhline(-1.0 / 12, color='0.6', ls=':', lw=1)
    ax[0, 1].axhline(-1.0 / 9, color='0.6', ls=':', lw=1)
    ax[0, 1].set_xticks(xt)
    ax[0, 1].set_xticklabels(xl)
    ax[0, 1].set_ylabel('a2 (k in 1/l)')
    ax[0, 1].set_title('(b) a2 der zwei Photonzweige (blau 100, orange 110, gruen 111); grau: M-D -1/12, -1/9')
    # (c) TT omega^2/k^2 relativ je Richtung
    vs = [('H3', 'tab:blue'), ('R12', 'tab:green'), ('Z8', 'tab:purple'), ('D1z', 'tab:red')]
    r13 = [r['richtung'] for r in S['varianten']['H3']['p13'] if r['eps'] == EPS[0]]
    for i, (var, col) in enumerate(vs):
        rows = [r for r in S['varianten'][var]['p13'] if r['eps'] == EPS[0] and r['z'] is not None]
        w = np.array([r['z']['w'] for r in rows])
        m = w.mean()
        for b in range(2):
            ax[1, 0].plot(np.arange(len(rows)) + 0.1 * i, w[:, b] / m - 1, 'o-' if b == 0 else 's--', color=col, ms=3,
                          lw=0.8, label=(var if b == 0 else None))
    ax[1, 0].set_xticks(range(len(r13)))
    ax[1, 0].set_xticklabels(r13, rotation=60, fontsize=8)
    ax[1, 0].set_ylabel('omega^2/k^2 / Mittel - 1 (|k| = 1e-3)')
    ax[1, 0].set_title('(c) TT-Zweige der Tetraeder-Oktaeder-Wabe je Richtung (A1R1, J = 1)')
    ax[1, 0].legend(fontsize=8)
    # (d) Spannen
    namen = ['V (Finn, gefuellt)', 'H3 (Haupt)', 'R12', 'Z8', 'D1z', 'K (ew ohne)']
    werte = [S['referenz_V']['spanne_tti'], S['varianten']['H3']['spanne13'], S['varianten']['R12']['spanne13'],
             S['varianten']['Z8']['spanne13'], S['varianten']['D1z']['spanne13'],
             S['kontrolle_K']['max'] / S['kontrolle_K']['min'] - 1]
    cols = ['0.5', 'tab:blue', 'tab:green', 'tab:purple', 'tab:red', '0.75']
    ax[1, 1].bar(range(len(werte)), [max(v, 1e-12) if v is not None else np.nan for v in werte], color=cols)
    ax[1, 1].set_yscale('log')
    ax[1, 1].axhline(S['referenz_V']['spanne_tti'], color='0.5', ls='--', lw=1)
    ax[1, 1].set_xticks(range(len(werte)))
    ax[1, 1].set_xticklabels(namen, rotation=20, fontsize=8)
    ax[1, 1].set_ylabel('Spanne max/min - 1 (13 Richtungen x 2 Zweige x 2 |k|)')
    ax[1, 1].set_title('(d) TT-Spanne ohne Abstimmung: Wabe gegen V (6,34 %)')
    fig.suptitle('OKTA-SCHATTEN-1: Schattenformen am Tetraeder-Netz (synthetische Rechnung, keine Messdaten)')
    fig.tight_layout()
    fig.savefig(png, dpi=110)
    print('bild ->', png, flush=True)


# ================================================================================================ Hauptteil
def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def nur_schluessel(x, tiefe=0):
    if isinstance(x, dict):
        return {k: nur_schluessel(v, tiefe + 1) for k, v in x.items()} if tiefe < 2 else sorted(x.keys())
    return type(x).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['licht', 'schwer', 'bild'])
    ap.add_argument('--out')
    ap.add_argument('--licht')
    ap.add_argument('--schwer')
    ap.add_argument('--png')
    ap.add_argument('--klein', action='store_true')
    ap.add_argument('--rauch', action='store_true', help='nur Schluessel, Laufzeiten und technische Proben ausgeben')
    a = ap.parse_args()
    if a.modus == 'bild':
        bild(a.licht, a.schwer, a.png)
        return
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'ew_sha256': sha(os.path.abspath(ew.__file__)),
            'tp_sha256': sha(os.path.abspath(tp.__file__)), 'ln_sha256': sha(os.path.abspath(ln.__file__)),
            'tti_sha256': sha(os.path.abspath(tti.__file__))}
    erg = lauf_licht(a.klein, a.rauch) if a.modus == 'licht' else lauf_schwer(a.klein, a.rauch)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - T_START,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        tech = {}
        if a.modus == 'licht':
            g = erg['geometrie']
            tech = {k: g[k] for k in ('E', 'V', 'F_dreieck', 'F_sechseck', 'kantenlaengen_l', 'zellen_je_kante',
                                      'zellen_je_flaeche', 'hand_abw', 'duale', 'mittelebene_max', 'nicht_senkrecht_max',
                                      'rot_grad_max')}
            tech['kontrolle_KL_ok'] = erg['kontrolle_KL']['ok']
        else:
            tech = {v: erg['varianten'][v]['kontrolle'] for v in erg['varianten']}
            tech['K_ok'] = erg['kontrolle_K']['ok']
            tech['V_abw_gegen_6339'] = erg['referenz_V']['abw_gegen_6339']
            tech['zeiten'] = erg['zeiten']
        res = {'info': info, 'schluessel': nur_schluessel(erg), 'technik': tech, 'laufzeit_s': res['laufzeit_s'],
               'maxrss_MB': res['maxrss_MB']}
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(js(res), fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
