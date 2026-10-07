#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-ISO-1 (Runde 43, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage: Lassen sich die zwei masselosen TT-Zweige auf dem gefuellten Netz (V, S) durch Gewichte langwellig isotrop machen?
ew.py, nachtrag_kinetik.py, tp.py werden unveraendert aus EINE-WELT-LOCH-1 importiert.

Paarungen (wie Nachtrag EINE-WELT-LOCH-1), Gewicht J_t je Tetraeder-Art (ew.py 'art'), multiplikativ je Zelle:
  A1R1: A = sum_t J_t A0_t,               A_red = S^+ A S
  A2R1: A = sum_t J_t (V_F/V_t) A0_t,     A_red = S^+ A S
  A3R2: K = sum_t J_t (V_t/V_F) Phi^-T G^-1 Phi^-1,  A_red = (S^+ K S)^-1
Regelgewicht g je Kantenart: c_v = - B w_v^g mit (w_v^g)_e = g(e) fuer die Kanten an v (g = 1 ist ew.ops).
Masselose Moden: 1/omega^2 = betragsgroesste Eigenwerte von Z = L^-1 A_red^-1 L^-+ mit B_red = L L^+.
"""
import argparse, json, sys, os, time, hashlib, platform, resource, itertools
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402
import ew  # noqa: E402
import nachtrag_kinetik as nk  # noqa: E402

PAARUNGEN = ('A1R1', 'A2R1', 'A3R2')
EPS = (1e-3, 2e-3)
REF_ART = {'V': 'finn_auf', 'S': 'finn_auf', 'ohne': 'finn1'}
REF_KANTE = 'pyro'
LUECKE_MAX = 1e-2          # |1/w2|_3 / |1/w2|_2 muss darunter liegen (masselos klar getrennt)
ABBRUCH = []                # Zeitabbrueche der Optimierung (Plan: Abbruchregel)
T0 = time.time()


def richtungen13():
    m = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (2, 1, 1), (2, 2, 1), (3, 1, 0), (3, 1, 1), (3, 2, 0), (3, 2, 1),
         (3, 2, 2), (3, 3, 1), (3, 3, 2)]
    return [(''.join(str(x) for x in v), np.array(v, float) / np.linalg.norm(v)) for v in m]


def kpunkte(richt, epsl=EPS):
    ks, ee, nn = [], [], []
    for nm, d in richt:
        for e in epsl:
            ks.append(e * d)
            ee.append(e)
            nn.append(nm)
    return np.array(ks), np.array(ee), nn


def kantenart(mod):
    def typ(s):
        return 'P' if s < 4 else ('C' if s < 6 else 'H')
    namen = {'PP': 'pyro', 'CP': 'c_speiche', 'HP': 'h_speiche', 'CH': 'ch', 'CC': 'achse'}
    return [namen[''.join(sorted(typ(s) + typ(s2)))] for (s, s2, n2) in mod['kliste']]


class Netz:
    def __init__(self, f):
        self.f = f
        self.mod = ew.baue(f)
        self.mats = nk.zell_matrizen(self.mod)
        self.arten = sorted(set(t[0]['art'] for t in self.mats))
        self.kart = kantenart(self.mod) if f != 'ohne' else ['pyro'] * self.mod['E']
        self.karten = sorted(set(self.kart))
        self.frei_arten = [a for a in self.arten if a != REF_ART[f]]
        self.frei_kanten = [a for a in self.karten if a != REF_KANTE]

    def J_aus_log(self, x):
        """x: (..., n_frei) log10-Gewichte -> (..., n_arten), Referenzart = 1."""
        x = np.atleast_2d(x)
        J = np.ones((x.shape[0], len(self.arten)))
        for i, a in enumerate(self.frei_arten):
            J[:, self.arten.index(a)] = 10.0 ** x[:, i]
        return J

    def g_aus_log(self, y):
        g = {a: 1.0 for a in self.karten}
        for i, a in enumerate(self.frei_kanten):
            g[a] = float(10.0 ** y[i])
        return g


def c_gew(mod, B, k, gvec):
    sh = k.shape[:-1]
    crow = np.zeros(sh + (mod['nV'], mod['E']), complex)
    for e, (s, s2, n2) in enumerate(mod['kliste']):
        ph = np.exp(1j * (k @ mod['T'][e]))
        crow[..., s, :] -= gvec[e] * B[..., e, :]
        crow[..., s2, :] -= gvec[e] * np.conj(ph)[..., None] * B[..., e, :]
    return np.conj(np.swapaxes(crow, -1, -2))


def basis(netz, kpts):
    o = ew.ops(netz.mod, kpts)
    teile = {}
    for a in netz.arten:
        sub = [t for t in netz.mats if t[0]['art'] == a]
        teile[a] = [nk.assemble(netz.mod, kpts, sub, w) for w in (1, 2, 3)]
    return {'k': kpts, 'B': o['B'], 'M': o['M'], 'teile': teile}


def prep(netz, ba, gk):
    gvec = np.array([gk[a] for a in netz.kart], float)
    c = c_gew(netz.mod, ba['B'], ba['k'], gvec)
    out = []
    for j in range(len(ba['k'])):
        U, r, s = ew.phys_basis_rr(ba['M'][j], c[j])
        S = U[:, r:]
        Sh = np.conj(S.T)
        Br = Sh @ ba['B'][j] @ S
        Br = 0.5 * (Br + np.conj(Br.T))
        eB = np.linalg.eigvalsh(Br)
        if eB.min() <= 0:
            out.append(None)
            continue
        L = np.linalg.cholesky(Br)
        Li = np.linalg.inv(L)
        P1 = np.array([Sh @ ba['teile'][a][0][j] @ S for a in netz.arten])
        P2 = np.array([Sh @ ba['teile'][a][1][j] @ S for a in netz.arten])
        Q3 = np.array([Li @ (Sh @ ba['teile'][a][2][j] @ S) @ np.conj(Li.T) for a in netz.arten])
        out.append({'Li': Li, 'P1': P1, 'P2': P2, 'Q3': Q3, 'dim': int(S.shape[1]), 'rang': int(r), 'S': S, 'Br': Br})
    return out


def auswerten(pr, eps, paarung, J, chunk=1500):
    """J (N, n_arten). Rueckgabe w (N, nk, 2) omega^2/k^2 der masselosen Moden, neg (N,) Zahl k-Punkte mit negativer
    Mode, luecke (N,) max ueber k von |ev3|/|ev2|, ok (N,) Klassifikation eindeutig und beide masselosen positiv."""
    N = J.shape[0]
    nkp = len(pr)
    w = np.full((N, nkp, 2), np.nan)
    neg = np.zeros(N, int)
    luecke = np.zeros(N)
    pos2 = np.ones(N, bool)
    for i0 in range(0, N, chunk):
        Jc = J[i0:i0 + chunk]
        for j, p in enumerate(pr):
            if p is None:
                neg[i0:i0 + len(Jc)] += 1
                pos2[i0:i0 + len(Jc)] = False
                continue
            if paarung == 'A3R2':
                Z = np.einsum('nt,tab->nab', Jc, p['Q3'])
            else:
                P = p['P1'] if paarung == 'A1R1' else p['P2']
                Ar = np.einsum('nt,tab->nab', Jc, P)
                try:
                    Ai = np.linalg.inv(Ar)
                except np.linalg.LinAlgError:
                    Ai = np.array([np.linalg.pinv(x) for x in Ar])
                Z = p['Li'] @ Ai @ np.conj(p['Li'].T)
            Z = 0.5 * (Z + np.conj(np.swapaxes(Z, -1, -2)))
            ev = np.linalg.eigvalsh(Z)
            o = np.argsort(-np.abs(ev), axis=1)
            evs = np.take_along_axis(ev, o, axis=1)
            top = evs[:, :2]
            w[i0:i0 + len(Jc), j, :] = np.sort(1.0 / top, axis=1) / eps[j] ** 2
            luecke[i0:i0 + len(Jc)] = np.maximum(luecke[i0:i0 + len(Jc)], np.abs(evs[:, 2]) / np.abs(evs[:, 1]))
            neg[i0:i0 + len(Jc)] += (ev < 0).any(axis=1)
            pos2[i0:i0 + len(Jc)] &= (top > 0).all(axis=1)
    ok = pos2 & (luecke < LUECKE_MAX)
    return w, neg, luecke, ok


def spanne(w):
    """w (N, nk, 2) -> max/min - 1 je Zeile."""
    return np.nanmax(w, axis=(1, 2)) / np.nanmin(w, axis=(1, 2)) - 1.0


def nelder_mead(f, x0, schritt=0.25, maxit=300, lo=-2.0, hi=2.0, tol=1e-12, bis=None):
    n = len(x0)
    clip = lambda x: np.clip(x, lo, hi)  # noqa: E731
    pts = [clip(np.array(x0, float))]
    for i in range(n):
        x = pts[0].copy()
        x[i] = x[i] + schritt if x[i] + schritt <= hi else x[i] - schritt
        pts.append(clip(x))
    vals = [f(p) for p in pts]
    nf = len(pts)
    for it in range(maxit):
        if bis is not None and time.time() > bis:
            ABBRUCH.append(1)
            break
        o = np.argsort(vals)
        pts = [pts[i] for i in o]
        vals = [vals[i] for i in o]
        if it > 20 and abs(vals[-1] - vals[0]) <= tol * max(abs(vals[0]), 1e-300):
            break
        c = np.mean(pts[:-1], axis=0)
        xr = clip(c + (c - pts[-1]))
        fr = f(xr)
        nf += 1
        if fr < vals[0]:
            xe = clip(c + 2 * (c - pts[-1]))
            fe = f(xe)
            nf += 1
            if fe < fr:
                pts[-1], vals[-1] = xe, fe
            else:
                pts[-1], vals[-1] = xr, fr
        elif fr < vals[-2]:
            pts[-1], vals[-1] = xr, fr
        else:
            xc = clip(c + 0.5 * (pts[-1] - c))
            fc = f(xc)
            nf += 1
            if fc < vals[-1]:
                pts[-1], vals[-1] = xc, fc
            else:
                for i in range(1, len(pts)):
                    pts[i] = clip(pts[0] + 0.5 * (pts[i] - pts[0]))
                    vals[i] = f(pts[i])
                    nf += 1
    i = int(np.argmin(vals))
    return pts[i], float(vals[i]), nf


# ------------------------------------------------------------------------------------------------ direkte Rechnung (eig)
def red_k(netz, kk, gk, paarung, J):
    """Ein k: S, A_red, B_red, M (direkt, wie ew/nachtrag)."""
    ba = basis(netz, kk[None, :])
    gvec = np.array([gk[a] for a in netz.kart], float)
    c = c_gew(netz.mod, ba['B'], ba['k'], gvec)[0]
    U, r, s = ew.phys_basis_rr(ba['M'][0], c)
    S = U[:, r:]
    Sh = np.conj(S.T)
    Br = Sh @ ba['B'][0] @ S
    w = {'A1R1': 0, 'A2R1': 1, 'A3R2': 2}[paarung]
    T = sum(J[i] * ba['teile'][a][w][0] for i, a in enumerate(netz.arten))
    Ar = np.linalg.inv(Sh @ T @ S) if paarung == 'A3R2' else Sh @ T @ S
    return S, Ar, Br, ba['M'][0]


def tt_pruefung(netz, gk, paarung, J, richt):
    out = []
    for nm, d in richt:
        kk = 1e-3 * d
        S, Ar, Br, M = red_k(netz, kk, gk, paarung, J)
        ww, vv = np.linalg.eig(Ar @ Br)
        o = np.argsort(np.abs(ww))
        tt = []
        for j in o[:2]:
            H, rest = ew.tensor_fit(netz.mod, S @ vv[:, j], kk, M)
            tt.append(float(tp.tt_anteil(H, kk)[0]))
        out.append({'richtung': nm, 'w2k2_eig': sorted(float(x) for x in ww[o[:2]].real / 1e-6),
                    'im_max': float(np.abs(ww.imag).max()), 'tt': tt})
    return out


def stabil(netz, gk, paarung, J, L=8, chunk=128):
    g = np.arange(L)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    kall = (mm / L) @ ew.BV
    gvec = np.array([gk[a] for a in netz.kart], float)
    wsel = {'A1R1': 0, 'A2R1': 1, 'A3R2': 2}[paarung]
    nneg, nkom, wmin, bneg, aneg = 0, 0, np.inf, 0, 0
    for i0 in range(0, len(kall), chunk):
        k = kall[i0:i0 + chunk]
        ba = basis(netz, k)
        c = c_gew(netz.mod, ba['B'], k, gvec)
        T = sum(J[i] * ba['teile'][a][wsel] for i, a in enumerate(netz.arten))
        for j in range(len(k)):
            U, r, s = ew.phys_basis_rr(ba['M'][j], c[j])
            S = U[:, r:]
            Sh = np.conj(S.T)
            Br = Sh @ ba['B'][j] @ S
            Ar = Sh @ T[j] @ S
            if paarung == 'A3R2':
                aneg += int((np.linalg.eigvalsh(0.5 * (Ar + np.conj(Ar.T))) <= 0).any())
                Ar = np.linalg.inv(Ar)
            else:
                aneg += int((np.linalg.eigvalsh(0.5 * (Ar + np.conj(Ar.T))) <= 0).any())
            eB = np.linalg.eigvalsh(0.5 * (Br + np.conj(Br.T)))
            bneg += int((eB <= 0).any())
            w2 = np.linalg.eigvals(Ar @ Br)
            sk = max(np.abs(w2).max(), 1e-300)
            nneg += int((w2.real < -1e-9 * sk).any())
            nkom += int((np.abs(w2.imag) > 1e-9 * sk).any())
            wmin = min(wmin, float(w2.real.min() / sk))
    return {'L': L, 'nk': int(len(kall)), 'k_mit_negativ': nneg, 'k_mit_komplex': nkom, 'w2_min_rel': wmin,
            'k_mit_B_red_nicht_pd': bneg, 'k_mit_A_oder_K_red_nicht_pd': aneg}


# ------------------------------------------------------------------------------------------------ Modi
def g_eins(netz):
    return {a: 1.0 for a in netz.karten}


def w2_klein(netz, gk, paarung, J, richt, epsl=EPS):
    kp, ee, nn = kpunkte(richt, epsl)
    pr = prep(netz, basis(netz, kp), gk)
    w, neg, lu, ok = auswerten(pr, ee, paarung, np.atleast_2d(J))
    return w[0], int(neg[0]), float(lu[0]), bool(ok[0]), nn, ee


def lauf_kontrolle(ref):
    out = {}
    with open(ref) as f:
        kin = json.load(f)
    r3 = ew.richtungen()[:3]
    # (a) Nachtragswerte J = 1, g = 1, drei Paarungen, V und S, an [100], [110], [111] x 2 eps
    alt_key = {'A1R1': 'A1_R1_w2_masselos_ueber_k2', 'A2R1': 'A2_R1_w2_masselos_ueber_k2',
               'A3R2': 'A3_R2_w2_masselos_ueber_k2'}
    for f in ('V', 'S'):
        netz = Netz(f)
        J1 = np.ones(len(netz.arten))
        for p in PAARUNGEN:
            w, neg, lu, ok, nn, ee = w2_klein(netz, g_eins(netz), p, J1, r3)
            dmax = 0.0
            zeilen = []
            for j, (nm, e) in enumerate(zip(nn, ee)):
                alt = [z for z in kin[f]['klein'] if z['richtung'] == nm and abs(z['eps'] - e) < 1e-12][0][alt_key[p]]
                d = float(np.max(np.abs(np.sort(alt) - w[j]) / np.sort(alt)))
                dmax = max(dmax, d)
                zeilen.append({'richtung': nm, 'eps': float(e), 'neu': w[j].tolist(), 'alt': sorted(alt)})
            out['nachtrag_%s_%s' % (f, p)] = {'abw_rel_max': dmax, 'neg': neg, 'luecke': lu, 'ok': ok, 'zeilen': zeilen}
    # (b) Hauptlauf V, A1R1, 23 Richtungen von ew
    netz = Netz('V')
    J1 = np.ones(len(netz.arten))
    w, neg, lu, ok, nn, ee = w2_klein(netz, g_eins(netz), 'A1R1', J1, ew.richtungen())
    out['hauptlauf_V_23'] = {'min': float(np.nanmin(w)), 'max': float(np.nanmax(w)),
                             'spanne_max_min': float(np.nanmax(w) / np.nanmin(w) - 1),
                             'spanne_mittel': float((np.nanmax(w) - np.nanmin(w)) / np.nanmean(w)),
                             'w100_eps1e-3': w[0].tolist(), 'ok': ok, 'neg': neg}
    # (c) ohne Fuellung, A1R1, 13 Richtungen: alle vier masselos
    no = Netz('ohne')
    kp, ee, nn = kpunkte(richtungen13())
    ba = basis(no, kp)
    pr = prep(no, ba, g_eins(no))
    alle = []
    for j, p in enumerate(pr):
        Jn = np.ones(len(no.arten))
        Ar = np.einsum('t,tab->ab', Jn, p['P1'])
        ww = np.linalg.eigvals(Ar @ p['Br'])
        alle += list(ww.real / ee[j] ** 2)
    alle = np.array(alle)
    out['ohne_A1R1_13'] = {'n': int(len(alle)), 'min': float(alle.min()), 'max': float(alle.max()),
                           'abw_0_25_max': float(np.abs(alle - 0.25).max())}
    # (d) Symmetrie: 48 Bilder einer allgemeinen Richtung, J = 1 und zufaellig, g = 1 und zufaellig
    ops48 = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            Rm = np.zeros((3, 3))
            for i in range(3):
                Rm[i, perm[i]] = sg[i]
            ops48.append(Rm)
    n0 = np.array([0.26, 0.45, 0.85])
    n0 = n0 / np.linalg.norm(n0)
    rng = np.random.default_rng(5)
    sym = {}
    for f in ('V', 'S'):
        netz = Netz(f)
        Jz = 10.0 ** rng.uniform(-1, 1, len(netz.arten))
        gz = {a: float(10.0 ** rng.uniform(-0.5, 0.5)) for a in netz.karten}
        for p in ('A1R1', 'A3R2'):
            for tag, J, gk in (('J1_g1', np.ones(len(netz.arten)), g_eins(netz)), ('Jzuf_g1', Jz, g_eins(netz)),
                               ('Jzuf_gzuf', Jz, gz)):
                richt = [('o%d' % i, Rm @ n0) for i, Rm in enumerate(ops48)]
                w, neg, lu, ok, nn, ee = w2_klein(netz, gk, p, J, richt, epsl=(1e-3,))
                ref0 = w[0]
                sym['%s_%s_%s' % (f, p, tag)] = {'abw_rel_max': float(np.max(np.abs(w - ref0[None, :]) / ref0[None, :])),
                                                  'ok': ok}
    out['symmetrie_48'] = sym
    out['symmetrie_zufall'] = {'J_V_S': 'seed 5, log10 U(-1,1) je Art; g log10 U(-0.5,0.5) je Kantenart'}
    # (e) Steifigkeit der affinen TT-Welle (beschreibend): K(n) = a^+ B a / k^2 auf TT(n), Frobenius-Basis
    st = {}
    for f in ('V', 'S', 'ohne'):
        netz = Netz(f)
        zeilen = []
        for nm, d in richtungen13():
            kk = 1e-3 * d
            o = ew.ops(netz.mod, kk[None, :])
            u = np.cross(d, [0.3, 0.5, 0.7])
            u = u / np.linalg.norm(u)
            v = np.cross(d, u)
            hs = [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]
            ph = np.exp(1j * (netz.mod['mitte'] @ kk))
            av = [np.array([nv @ h @ nv for nv in netz.mod['n']]) * ph for h in hs]
            Km = np.array([[np.conj(a1) @ o['B'][0] @ a2 for a2 in av] for a1 in av]) / 1e-6
            ev = np.linalg.eigvalsh(0.5 * (Km + np.conj(Km.T)))
            zeilen.append({'richtung': nm, 'K_ueber_k2': ev.tolist()})
        allev = np.array([z['K_ueber_k2'] for z in zeilen])
        st[f] = {'zeilen': zeilen, 'spanne_max_min': float(allev.max() / allev.min() - 1)}
    out['steifigkeit_affin'] = st
    return out


def lauf_gitter(f, paarung, npkt):
    netz = Netz(f)
    kp, ee, nn = kpunkte(richtungen13())
    t = time.time()
    pr = prep(netz, basis(netz, kp), g_eins(netz))
    t_prep = time.time() - t
    ach = np.linspace(-2, 2, npkt)
    X = np.array(list(itertools.product(ach, repeat=len(netz.frei_arten))))
    J = netz.J_aus_log(X)
    t = time.time()
    w, neg, lu, ok = auswerten(pr, ee, paarung, J)
    t_ausw = time.time() - t
    sp = spanne(w)
    sp_plan = np.where(ok & (neg == 0), sp, np.nan)
    sp_wort = np.where(ok, sp, np.nan)
    o = np.argsort(np.where(np.isnan(sp_plan), np.inf, sp_plan))
    besten = [{'x': X[i].tolist(), 'spanne': float(sp_plan[i])} for i in o[:10] if np.isfinite(sp_plan[i])]
    # symmetrische Teilmenge (Fd-3m): finn_ab = finn_auf, T1 = T2
    symm = sym_maske(netz, X)
    i_s = [i for i in o if symm[i] and np.isfinite(sp_plan[i])]
    i_w = int(np.nanargmin(sp_wort)) if np.isfinite(sp_wort).any() else None
    return {'netz': f, 'paarung': paarung, 'arten': netz.arten, 'frei_arten': netz.frei_arten, 'achse_log10': ach.tolist(),
            'n_J': int(len(J)), 't_prep_s': t_prep, 't_auswertung_s': t_ausw,
            'n_ok': int(ok.sum()), 'n_ok_ohne_neg': int((ok & (neg == 0)).sum()),
            'besten_plan': besten,
            'bester_symm_plan': ({'x': X[i_s[0]].tolist(), 'spanne': float(sp_plan[i_s[0]])} if i_s else None),
            'bester_wortlaut': ({'x': X[i_w].tolist(), 'spanne': float(sp_wort[i_w]), 'neg': int(neg[i_w])}
                                if i_w is not None else None),
            'spanne_J1': float(sp[np.argmin(np.abs(X).sum(1))]),
            'spanne_plan_alle': [None if not np.isfinite(x) else round(float(x), 7) for x in sp_plan]}


def sym_maske(netz, X):
    J = netz.J_aus_log(X)
    a = netz.arten
    m = np.ones(len(X), bool)
    for p, q in (('finn_auf', 'finn_ab'), ('kegel_T1', 'kegel_T2'), ('sechs_T1', 'sechs_T2')):
        if p in a and q in a:
            m &= np.isclose(J[:, a.index(p)], J[:, a.index(q)])
    return m


def sym_J(netz, y):
    """Fd-3m-Unterraum: y = log10 (kegel, sechs|achse) relativ zu finn."""
    x = np.zeros(len(netz.frei_arten))
    for i, a in enumerate(netz.frei_arten):
        if a.startswith('kegel'):
            x[i] = y[0]
        elif a.startswith('sechs') or a == 'achse':
            x[i] = y[1]
    return x


def lauf_verfeinern(f, paarung, gitterdatei, ng, nmf=1.0, Lst=8):
    netz = Netz(f)
    if gitterdatei:
        with open(gitterdatei) as fh:
            gi = json.load(fh)['ergebnis']
    else:
        gi = {'besten_plan': [{'x': [0.0] * len(netz.frei_arten)}], 'bester_symm_plan': None}
    mi = lambda m: max(2, int(round(m * nmf)))  # noqa: E731
    kp, ee, nn = kpunkte(richtungen13())
    ba = basis(netz, kp)
    pr1 = prep(netz, ba, g_eins(netz))

    def fJ(x, pr=pr1):
        w, neg, lu, ok = auswerten(pr, ee, paarung, netz.J_aus_log(x))
        return float(spanne(w)[0]) if (ok[0] and neg[0] == 0) else 1e3
    out = {'netz': f, 'paarung': paarung, 'arten': netz.arten, 'kantenarten': netz.karten}
    # TB1: Mehrfachstart aus den besten Gitterpunkten, dann Neustart mit kleinem Schritt
    t = time.time()
    starts = [np.array(b['x']) for b in gi['besten_plan'][:4]]
    res = []
    for x0 in starts:
        x1, v1, n1 = nelder_mead(fJ, x0, schritt=0.25, maxit=mi(250), bis=T0 + 150)
        x2, v2, n2 = nelder_mead(fJ, x1, schritt=0.05, maxit=mi(250), bis=T0 + 150)
        res.append({'start': x0.tolist(), 'x': x2.tolist(), 'spanne': v2, 'nf': n1 + n2})
    best = min(res, key=lambda r: r['spanne'])
    out['tb1_starts'] = res
    out['tb1_best'] = best
    out['t_tb1_s'] = time.time() - t
    # symmetrischer Unterraum (2 Verhaeltnisse)
    fS = lambda y: fJ(sym_J(netz, y))  # noqa: E731
    y0 = np.array([0.0, 0.0])
    if gi.get('bester_symm_plan'):
        xs = np.array(gi['bester_symm_plan']['x'])
        y0 = np.array([xs[[i for i, a in enumerate(netz.frei_arten) if a.startswith('kegel')][0]],
                       xs[[i for i, a in enumerate(netz.frei_arten) if a.startswith('sechs') or a == 'achse'][0]]])
    y1, v1, n1 = nelder_mead(fS, y0, schritt=0.25, maxit=mi(200), bis=T0 + 200)
    y2, v2, n2 = nelder_mead(fS, y1, schritt=0.05, maxit=mi(200), bis=T0 + 200)
    out['tb1_symm_best'] = {'y_kegel_sechs': y2.tolist(), 'x': sym_J(netz, y2).tolist(), 'spanne': v2, 'nf': n1 + n2}
    # TB2: Gitter ueber Regelgewichte bei J = bestes TB1, dann gemeinsame Verfeinerung
    xJ = np.array(best['x'])
    ach = np.linspace(-2, 2, ng)
    Y = np.array(list(itertools.product(ach, repeat=len(netz.frei_kanten))))
    gs = []
    t = time.time()
    for y in Y:
        pr = prep(netz, ba, netz.g_aus_log(y))
        w, neg, lu, ok = auswerten(pr, ee, paarung, netz.J_aus_log(xJ))
        gs.append(float(spanne(w)[0]) if (ok[0] and neg[0] == 0) else np.nan)
    out['tb2_g_gitter_t_s'] = time.time() - t
    gs = np.array(gs)
    out['tb2_g_gitter_n_ok'] = int(np.isfinite(gs).sum())
    og = np.argsort(np.where(np.isfinite(gs), gs, np.inf))
    out['tb2_g_gitter_besten'] = [{'y': Y[i].tolist(), 'spanne': float(gs[i])} for i in og[:5] if np.isfinite(gs[i])]
    nJ = len(netz.frei_arten)

    def fJg(z):
        pr = prep(netz, ba, netz.g_aus_log(z[nJ:]))
        w, neg, lu, ok = auswerten(pr, ee, paarung, netz.J_aus_log(z[:nJ]))
        return float(spanne(w)[0]) if (ok[0] and neg[0] == 0) else 1e3
    res2 = []
    t = time.time()
    starts2 = [np.concatenate([xJ, Y[i]]) for i in og[:2] if np.isfinite(gs[i])] + [np.concatenate([xJ, np.zeros(len(netz.frei_kanten))])]
    for z0 in starts2:
        z1, v1, n1 = nelder_mead(fJg, z0, schritt=0.25, maxit=mi(150), bis=T0 + 470)
        z2, v2, n2 = nelder_mead(fJg, z1, schritt=0.05, maxit=mi(150), bis=T0 + 470)
        res2.append({'start': z0.tolist(), 'z': z2.tolist(), 'spanne': v2, 'nf': n1 + n2})
    best2 = min(res2, key=lambda r: r['spanne'])
    out['tb2_starts'] = res2
    out['tb2_best'] = best2
    out['t_tb2_nm_s'] = time.time() - t
    # Bestwahl-Pruefung: Spanne auf 23 ew-Richtungen, TT-Anteil, Stabilitaet 511 k
    t = time.time()
    for tag, J, gk in (('tb1', netz.J_aus_log(np.array(best['x']))[0], g_eins(netz)),
                       ('tb1_symm', netz.J_aus_log(np.array(out['tb1_symm_best']['x']))[0], g_eins(netz)),
                       ('tb2', netz.J_aus_log(np.array(best2['z'][:nJ]))[0], netz.g_aus_log(np.array(best2['z'][nJ:])))):
        w, neg, lu, ok, nn2, ee2 = w2_klein(netz, gk, paarung, J, ew.richtungen())
        w13, neg13, lu13, ok13, _, _ = w2_klein(netz, gk, paarung, J, richtungen13())
        out['pruef_' + tag] = {'J': dict(zip(netz.arten, J.tolist())), 'g': gk,
                               'spanne_13': float(np.nanmax(w13) / np.nanmin(w13) - 1), 'w13_min': float(np.nanmin(w13)),
                               'w13_max': float(np.nanmax(w13)), 'luecke_13': lu13,
                               'spanne_23ew': float(np.nanmax(w) / np.nanmin(w) - 1), 'ok_23ew': ok, 'neg_23ew': neg,
                               'w13_je_richtung': {nm: w13[2 * i].tolist() for i, (nm, d) in enumerate(richtungen13())},
                               'tt': tt_pruefung(netz, gk, paarung, J, richtungen13()[:3]),
                               'stabil_L8': stabil(netz, gk, paarung, J, L=Lst)}
    out['t_pruef_s'] = time.time() - t
    out['zeitabbruch_nm'] = len(ABBRUCH)
    return out


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def nur_schluessel(x, tiefe=0):
    if isinstance(x, dict):
        return {k: nur_schluessel(v, tiefe + 1) for k, v in x.items()} if tiefe < 2 else sorted(x.keys())
    return type(x).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['kontrolle', 'gitter', 'verfeinern'])
    ap.add_argument('--netz', default='V', choices=['V', 'S'])
    ap.add_argument('--paarung', default='A1R1', choices=list(PAARUNGEN))
    ap.add_argument('--npkt', type=int, default=9)
    ap.add_argument('--ng', type=int, default=5)
    ap.add_argument('--gitterdatei')
    ap.add_argument('--nmfaktor', type=float, default=1.0)
    ap.add_argument('--Lst', type=int, default=8)
    ap.add_argument('--ref')
    ap.add_argument('--rauch', action='store_true', help='nur Schluessel und Laufzeiten ausgeben, keine Werte')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'ew_sha256': sha(os.path.abspath(ew.__file__)),
            'nk_sha256': sha(os.path.abspath(nk.__file__)), 'tp_sha256': sha(os.path.abspath(tp.__file__))}
    if a.gitterdatei:
        info['gitterdatei_sha256'] = sha(a.gitterdatei)
    if a.ref:
        info['ref_sha256'] = sha(a.ref)
    if a.modus == 'kontrolle':
        erg = lauf_kontrolle(a.ref)
    elif a.modus == 'gitter':
        erg = lauf_gitter(a.netz, a.paarung, a.npkt)
    else:
        erg = lauf_verfeinern(a.netz, a.paarung, a.gitterdatei, a.ng, nmf=a.nmfaktor, Lst=a.Lst)
    res = {'info': info, 'ergebnis': erg}
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    if a.rauch:
        res = {'info': info, 'schluessel': nur_schluessel(erg), 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'],
               't': {k: v for k, v in erg.items() if k.startswith('t_') or k.endswith('_t_s')}, 'n_J': erg.get('n_J'),
               'nf_tb1': [r['nf'] for r in erg.get('tb1_starts', [])], 'nf_tb2': [r['nf'] for r in erg.get('tb2_starts', [])]}
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, a.netz, a.paarung, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
