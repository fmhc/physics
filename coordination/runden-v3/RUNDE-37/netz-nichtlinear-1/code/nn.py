#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NETZ-NICHTLINEAR-1 (fmhc-physics, Runde 50, schlanke Karte), Code-Agent fuer die Leitung claude-primary.

Frage: Verschwinden die Ausnahmezuege der Umklapp-Dynamik, wenn M_eff (und B) am gedehnten, mitbewegten Netz gerechnet
werden statt am ungedehnten Hintergrund (Lesart H, UMKLAPP-FOLGE-1)?

Lesart G1: Im Zugzeitpunkt t_e (Zustand x_e) gilt fuer jede Kante l = l0 (1 + a), a = S x_e (die neue Kante beim 2-3 aus
der flachen Doppelpyramide der gedehnten 9 Kanten, nichtlinear). Je Tetraeder wird die symmetrische lineare Abbildung F
mit |F e| = l fuer alle 6 Kanten bestimmt. Damit:
  - 4D-Zeltgitter (wie UMKLAPP-FOLGE-1: ganze Box, k = 0, h_Zelt = 2^-10, Hubfolge nach Eckindex, Schema ls): raeumliche
    Lagen je 4-Simplex mit F des zugehoerigen Tetraeders abgebildet, Zeitlagen unveraendert. Hesse-Bloecke Hloc aus
    pt.geometrie der gedehnten Simplizes, 4D-Kantenlaengen und -vektoren (raeumlicher Anteil gestreckt) gedehnt.
    Danach meff_schnell unveraendert (uf.py). M_eff in q = dl / l_gedehnt, umgerechnet auf a = dl / l0: D M D, D = 1/f.
  - B: 3D-Regge-Hesse (tg.zelle_D_batch) an den gedehnten Tetraedern, in a-Variablen (l0 D l0), statt am Hintergrund.
  - S (Zwangsflaeche), Delaunay-Test, Abbildung ueber den Zug (td.abbilden, Lesarten R und P): unveraendert.
  Operatoren bleiben bis zum naechsten Zug fest (Arm a ohne Zuege ist damit gleich UMKLAPP-FOLGE-1 Arm a).
Je Zug zusaetzlich: alte Zerlegung am gedehnten Netz (Neubewertungs-Sprung getrennt vom Zug-Sprung) und, bei 2-3-Zuegen
mit mu_hg > 0, die neue Zerlegung am Hintergrund (Lesart H) zum direkten Vergleich der negativen Richtungen.
Importiert unveraendert: td, tg, uk, tu, uv, rk, rk2, pt, umklapp4d, uf (Kopien aus RUNDE-37/umklapp-folge-1/code).
"""
import argparse, json, os, sys, time, platform, resource
import numpy as np
import scipy
import scipy.sparse as sp
import scipy.linalg as sla

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import tg  # noqa: E402
import uk  # noqa: E402
import tu  # noqa: E402
import td  # noqa: E402
import uv  # noqa: E402
import rk  # noqa: E402
import rk2  # noqa: E402
import pt  # noqa: E402
import umklapp4d as u4  # noqa: E402
import uf  # noqa: E402

_TDNetz = td.Netz
_gg_orig = u4.gitter_glas
DEHN = {'F': None, 'info': None}
NETZE = []
HAKEN = {"zug": None}
VORLAUF_K = [0.1, 0.2, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30, 40, 50, 70, 100]
NEG_SOLL = 128
B_GD = {"an": True}            # Karte G1: B am gedehnten Netz; Variante G1m (--bgd 0): nur M_eff gedehnt, B am Hintergrund


# ------------------------------------------------------------------------------------------------ gedehnte Geometrie
def tet_koord(LV, pos, G, O):
    return pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)


def F_aus_dehnung(X, eidx, f):
    """Je Tetraeder F (T,3,3) symmetrisch positiv mit |F e_p|^2 = |e_p|^2 f_p^2 fuer die 6 Kanten (tg.PAARE)."""
    T = len(X)
    rows = np.zeros((T, 6, 6))
    rhs = np.zeros((T, 6))
    for p, (i, j, _, _) in enumerate(tg.PAARE):
        d = X[:, j] - X[:, i]
        rows[:, p] = np.stack([d[:, 0] ** 2, d[:, 1] ** 2, d[:, 2] ** 2, 2 * d[:, 0] * d[:, 1], 2 * d[:, 0] * d[:, 2],
                               2 * d[:, 1] * d[:, 2]], 1)
        rhs[:, p] = (d * d).sum(1) * f[eidx[:, p]] ** 2
    gv = np.linalg.solve(rows, rhs[..., None])[..., 0]
    Gm = np.zeros((T, 3, 3))
    Gm[:, 0, 0], Gm[:, 1, 1], Gm[:, 2, 2] = gv[:, 0], gv[:, 1], gv[:, 2]
    Gm[:, 0, 1] = Gm[:, 1, 0] = gv[:, 3]
    Gm[:, 0, 2] = Gm[:, 2, 0] = gv[:, 4]
    Gm[:, 1, 2] = Gm[:, 2, 1] = gv[:, 5]
    w, Q = np.linalg.eigh(Gm)
    assert w.min() > 0, 'Metrik nicht positiv'
    F = np.einsum('tij,tj,tkj->tik', Q, np.sqrt(w), Q)
    rest = 0.0
    for p, (i, j, _, _) in enumerate(tg.PAARE):
        d = X[:, j] - X[:, i]
        l1 = np.linalg.norm(np.einsum('tij,tj->ti', F, d), axis=1)
        rest = max(rest, float(np.abs(l1 / (np.linalg.norm(d, axis=1) * f[eidx[:, p]]) - 1).max()))
    return F, rest


def gitter_glas_gd(LV, pos, G, O, h):
    """u4.gitter_glas, danach (wenn DEHN['F'] gesetzt) raeumliche Simplexlagen mit F je Tetraeder abgebildet."""
    g = _gg_orig(LV, pos, G, O, h)
    F = DEHN['F']
    if F is None:
        return g
    assert g.S == 4 * len(F)
    Fs = np.repeat(F, 4, axis=0)
    P = g.Xs[:, :, :3]
    Xn = g.Xs.copy()
    Xn[:, :, :3] = P[:, :1, :] + np.einsum('sij,skj->ski', Fs, P - P[:, :1, :])
    geo = pt.geometrie(Xn)
    f4 = np.ones(g.NE)
    streu = 0.0
    r_alle = []
    for i, (a, c) in enumerate(pt.PAARE5):
        n0 = np.linalg.norm(P[:, c] - P[:, a], axis=1)
        n1 = np.linalg.norm(Xn[:, c, :3] - Xn[:, a, :3], axis=1)
        ok = n0 > 1e-9 * g.lmean
        r = np.where(ok, n1 / np.where(ok, n0, 1.0), 1.0)
        r_alle.append((g.egid[:, i], r))
        f4[g.egid[:, i]] = r
    for e, r in r_alle:
        streu = max(streu, float(np.abs(f4[e] - r).max()))
    E = g.E.copy()
    E[:, :3] *= f4[:, None]
    g.E = E
    g.l = np.linalg.norm(E, axis=1)
    g.u = E / g.l[:, None]
    g.lmean = float(g.l.mean())
    g.Xs = Xn
    g.geo = geo
    g.Hloc = -geo['M']
    DEHN['info'] = {'f4_streuung': streu, 'f4_min': float(f4.min()), 'f4_max': float(f4.max()),
                    'schlaefli_gd': float(geo['schlaefli']), 'M_sym_gd': float(geo['M_sym'])}
    return g


u4.gitter_glas = gitter_glas_gd           # u4._baue ruft gitter_glas ueber den Modulnamensraum


def b_gedehnt(X, F, mod):
    """3D-Regge-Hesse an den gedehnten Tetraedern in a = dl / l0 (Zusammenbau wie tg.ops_BA bei k = 0)."""
    Xg = X[:, :1, :] + np.einsum('tij,tkj->tki', F, X - X[:, :1, :])
    D, th = tg.zelle_D_batch(Xg)
    eidx, E = mod['eidx'], mod['E']
    lt0 = mod['l'][eidx]
    Dl = lt0[:, :, None] * D * lt0[:, None, :]
    rows = np.repeat(eidx[:, :, None], 6, 2).ravel()
    cols = np.repeat(eidx[:, None, :], 6, 1).ravel()
    B = sp.coo_matrix((Dl.ravel(), (rows, cols)), shape=(E, E)).tocsr()
    fehl = 2 * np.pi - np.bincount(eidx.ravel(), th.ravel(), E)
    return B, float(np.abs(fehl).max())


class NetzG(_TDNetz):
    """td.Netz mit A = M_eff^-1 aus der 4D-Zeltwirkung; mit f (l = l0 f je Kante) am gedehnten Netz (M_eff und B)."""

    def __init__(self, LV, pos, G, O, k1, hp, hx, f=None, f_fn=None, eigen=True, rolle=''):
        t0 = time.time()
        super().__init__(LV, pos, G, O, k1, hp, hx, eigen=False)
        self.hp = hp
        if f_fn is not None:
            f = f_fn(self)
        gd = f is not None
        self.f = np.ones(self.E) if f is None else np.asarray(f, float).copy()
        info = {'gedehnt': bool(gd), 'rolle': rolle}
        X = None
        if gd:
            X = tet_koord(LV, pos, G, O)
            F, rest = F_aus_dehnung(X, self.mod['eidx'], self.f)
            DEHN['F'] = F
            info.update({'F_rest': rest, 'a_max': float(np.abs(self.f - 1).max())})
        try:
            DEHN['info'] = None
            res, dg = uf.meff_schnell(LV, pos, G, O, self.mod)
        finally:
            DEHN['F'] = None
        if DEHN['info']:
            info.update(DEHN['info'])
        if res is None:
            raise RuntimeError('M_eff nicht bestimmbar: %s' % json.dumps(dg))
        Dg = 1.0 / self.f
        M = Dg[:, None] * res['M'] * Dg[None, :]
        Ve = Dg[:, None] * res['V'] * Dg[None, :]
        info['b_gd'] = bool(gd and B_GD['an'])
        if gd and B_GD['an']:
            Bbg = self.B.toarray()
            Bg, fehl = b_gedehnt(X, F, self.mod)
            self.B = Bg
            Br = self.S.T @ (self.B @ self.S)
            self.Br = 0.5 * (Br + Br.T)
            Bd = self.B.toarray()
            info.update({'dB_rel': float(np.linalg.norm(Bd - Bbg) / np.linalg.norm(Bbg)), 'fehlwinkel_max': fehl})
        Bd = self.B.toarray()
        dg['r_V_gegen_B'] = float(np.linalg.norm(Ve - Bd) / np.linalg.norm(Bd))
        self.M = M
        A = np.linalg.inv(M)
        A = 0.5 * (A + A.T)
        self.A = A
        Ar = self.S.T @ A @ self.S
        self.Ar = 0.5 * (Ar + Ar.T)
        self.lu = sla.lu_factor(self.Ar)
        eA = np.linalg.eigvalsh(self.Ar)
        self.n_A_neg = int((eA < -1e-12 * np.abs(eA).max()).sum())
        self.A_min_rel = float(eA.min() / np.abs(eA).max())
        try:
            self.L = np.linalg.cholesky(self.Ar)
            self.A_pd = True
        except np.linalg.LinAlgError:
            self.L = None
            self.A_pd = False
        self.eig = None
        if eigen:
            self.spektrum()
        self.t_bau = time.time() - t0
        dg.update(info)
        dg.update({'T': int(len(G)), 'E': int(self.E), 'A_pd': bool(self.A_pd), 'n_A_neg': self.n_A_neg,
                   'A_min_rel': self.A_min_rel, 'w2_max': (self.eig or {}).get('w2_max'),
                   'n_wachsend': (self.eig or {}).get('n_wachsend'), 't_bau_s': self.t_bau})
        self.meff = dg
        NETZE.append({k: dg.get(k) for k in ('rolle', 'gedehnt', 'M_n_neg', 'M_n_null', 'M_absmin_rel', 'A_pd',
                                             'n_A_neg', 'n_wachsend', 'w2_max', 'D0_n_neg', 'dB_rel', 'fehlwinkel_max',
                                             'F_rest', 'f4_streuung', 'a_max', 't_bau_s', 'r_V_gegen_B')})


def kurz(N):
    if N is None:
        return None
    d = N.meff
    return {'M_n_neg': d.get('M_n_neg'), 'M_n_null': d.get('M_n_null'), 'M_absmin_rel': d.get('M_absmin_rel'),
            'D0_n_neg': d.get('D0_n_neg'), 'A_pd': bool(N.A_pd), 'n_A_neg': int(N.n_A_neg), 'A_min_rel': N.A_min_rel,
            'n_wachsend': (N.eig or {}).get('n_wachsend'), 'w2_max': (N.eig or {}).get('w2_max'),
            'w2_wachsend': (N.eig or {}).get('w2_wachsend'), 'dB_rel': d.get('dB_rel'),
            'fehlwinkel_max': d.get('fehlwinkel_max'), 'F_rest': d.get('F_rest'), 'f4_streuung': d.get('f4_streuung'),
            't_bau_s': d.get('t_bau_s')}


# ------------------------------------------------------------------------------------------------ Lauf (wie td.lauf, Arm a/b)
def lauf(args):
    T0w = time.time()
    LV, pos, G0, O0, ninfo = td.netz_bauen(args.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    N0 = NetzG(LV, pos, G0, O0, k1, hp, hx, rolle='start')
    if not N0.A_pd:
        raise RuntimeError('A_red nicht positiv definit')
    mode, xm, w2, Qm = td.tt_mode(N0, args.A, k1)
    om = mode['omega']
    Tper = 2 * np.pi / om
    wmax = np.sqrt(N0.eig['w2_max'])
    NT = int(np.ceil(Tper * wmax / args.h))
    dt = Tper / NT
    nges = NT * args.perioden
    ds = max(1, NT // args.proben)
    fkeys0 = set(map(tuple, N0.fkeys.tolist()))
    zfile = args.out + '.zustand.npz'
    if os.path.exists(zfile):
        z = np.load(zfile, allow_pickle=False)
        G, O, f = z['G'], z['O'], z['f']
        meta = json.load(open(args.out + '.zustand.json'))
        x, y, n = z['x'], z['y'], int(z['n'])
        gleich = len(G) == len(G0) and np.array_equal(G, G0) and np.array_equal(O, O0)
        if gleich and bool(z['f_eins']):
            N = N0
        else:
            N = NetzG(LV, pos, G, O, k1, hp, hx, f=f, rolle='neustart')
        proben, ereig, perioden = meta['proben'], meta['ereignisse'], meta['perioden']
        gesperrt = set(tuple(g) for g in meta['gesperrt'])
        abschnitt = meta['abschnitt'] + 1
    else:
        N = N0
        x = np.zeros(N0.m)
        y = sla.lu_solve(N0.lu, om * xm)
        n = 0
        proben, ereig, perioden = [], [], []
        gesperrt = set()
        abschnitt = 0
    f_eins = N is N0
    H0 = N0.energie(np.zeros(N0.m), sla.lu_solve(N0.lu, om * xm))[0]
    xref = float(np.linalg.norm(xm))
    abbruch = None

    def probe(N, x, y, t):
        H, V, K = N.energie(x, y)
        mu = N.mu_alle(x)
        c4 = N.tt(x)
        proben.append([t, H, V, K] + [float(v) for v in c4] + [len([e for e in ereig if e.get('ausgefuehrt')]),
                                                               int((mu < 0).sum()), float(mu.min())])

    if n == 0 and not proben:
        probe(N, x, y, 0.0)
    Bx = None
    while n < nges:
        if time.time() - T0w > args.budget:
            break
        t_cur = n * dt
        rem = dt
        while rem > 0:
            x1, y1, Bx1 = td.kdk(N, x, y, rem, Bx)
            ev = None
            if args.arm == 'b':
                mu1 = N.mu_alle(x1)
                kand = np.nonzero(mu1 < 0)[0]
                kand = [j for j in kand if tuple(N.fkeys[N.fl['t1'][j] * 4 + N.fl['i1'][j]].tolist()) not in gesperrt]
                if kand:
                    v1 = N.Ar @ y
                    v2 = N.Ar @ (N.Br @ x)
                    best = None
                    for j in kand:
                        lo, hi = 0.0, rem
                        if N.mu_eine(j, x) < 0:
                            continue
                        for _ in range(td.BISEKT):
                            mid = 0.5 * (lo + hi)
                            if N.mu_eine(j, x + mid * v1 - 0.5 * mid * mid * v2) < 0:
                                hi = mid
                            else:
                                lo = mid
                        if best is None or hi < best[1]:
                            best = (j, hi)
                    if best is not None:
                        ev = best
            if ev is None:
                x, y, Bx = x1, y1, Bx1
                rem = 0.0
                break
            j, tau = ev
            xe, ye, _ = td.kdk(N, x, y, tau, Bx)
            te = t_cur + tau
            H1, V1, K1 = N.energie(xe, ye)
            rec = {'t': te, 'n': n, 'tau_rel': tau / dt}
            abc, d, e = td.flaechen_ecken(N, j)
            L9 = N.l9_0[j] * (1.0 + N.S[N.f9[j]] @ xe)
            vv = td.vol_bipyr(L9)
            if np.all(vv > 0) or np.all(vv < 0):
                typ, r = 23, None
            else:
                typ, r = 32, tu.ungerade(vv)
            mu_hg = float(td.mu_bipyr(N.l9_0[j][None, :])[0])
            rec.update({'typ': typ, 'mu_rechts': N.mu_eine(j, xe), 'mu_hg': mu_hg,
                        'flaeche': [int(abc[0][0]), int(abc[1][0]), int(abc[2][0])], 'spitzen': [d[0], e[0]]})
            aus = None if (typ == 32 and r is None) else td.zug_ausfuehren(N, j, typ, r, td.VMIN_B * N0.vbar)
            if aus is None:
                rec['ausgefuehrt'] = False
                gesperrt.add(tuple(N.fkeys[N.fl['t1'][j] * 4 + N.fl['i1'][j]].tolist()))
                ereig.append(rec)
                x, y, Bx = xe, ye, None
                rem -= tau
                t_cur = te
                continue
            Gn, On, besch = aus
            a_alt = N.S @ xe
            f_alt = 1.0 + a_alt
            l_extra = {}
            if besch['kante_neu'] is not None:
                i9, ok9 = N.idx_von_keys(besch['k9'])
                L9g = N.l0[i9] * (1.0 + a_alt[i9])
                l_extra[besch['kante_neu']] = float(td.l_de_flach(L9g[None, :])[0])

            if HAKEN['zug'] is not None:              # nur nn_scan.py (Kreuzungsscan), im Hauptlauf leer
                rec['scan'] = HAKEN['zug'](N=N, Gn=Gn, On=On, besch=besch, a_alt=a_alt, j=j, typ=typ, mu_hg=mu_hg,
                                           LV=LV, pos=pos, k1=k1, hp=hp, hx=hx)
            if args.vorlauf > 0:                       # Variante G1v (nach Kreuzungsscan): Operatoren nicht im Zugzeitpunkt,
                v1 = N.Ar @ ye                         # sondern auf der freien Bahn kurz danach, sobald die Flaeche j
                v2 = N.Ar @ (N.Br @ xe)                # mu <= -vorlauf hat (neue Zerlegung dort Delaunay mit Rand)
                best = None
                for kv in VORLAUF_K:
                    tv = kv * dt
                    xv = xe + tv * v1 - 0.5 * tv * tv * v2
                    mu_v = N.mu_eine(j, xv)
                    if best is None or mu_v < best[1]:
                        best = (kv, mu_v, xv)
                    if mu_v <= -args.vorlauf:
                        best = (kv, mu_v, xv)
                        break
                a_op = N.S @ best[2]
                rec['vorlauf'] = {'tau_dt': best[0], 'mu_flaeche': best[1], 'a_max': float(np.abs(a_op).max())}
                f_alt = 1.0 + a_op
                if besch['kante_neu'] is not None:
                    L9g = N.l0[i9] * (1.0 + a_op[i9])
                    l_extra[besch['kante_neu']] = float(td.l_de_flach(L9g[None, :])[0])

            def f_neu_fn(N2, N=N, f_alt=f_alt, besch=besch, l_extra=l_extra):
                idx, ok = N2.idx_von_keys(N.keys)
                fn = np.ones(N2.E)
                fn[idx[ok]] = f_alt[ok]
                if besch['kante_neu'] is not None:
                    inew, okn = N2.idx_von_keys(np.array([besch['kante_neu']]))
                    assert okn[0]
                    fn[inew[0]] = l_extra[besch['kante_neu']] / N2.l0[inew[0]]
                return fn
            try:
                N1g = NetzG(LV, pos, N.G, N.O, k1, hp, hx, f=f_alt, rolle='alt_gd') if args.split else None
                N2 = NetzG(LV, pos, Gn, On, k1, hp, hx, f_fn=f_neu_fn, rolle='neu_gd')
                N2h = None
                if args.vergleich and typ == 23 and mu_hg > 0:
                    N2h = NetzG(LV, pos, Gn, On, k1, hp, hx, rolle='neu_hg')
            except (RuntimeError, AssertionError, np.linalg.LinAlgError) as exc:
                rec['ausgefuehrt'] = False
                rec['fehler'] = repr(exc)
                ereig.append(rec)
                abbruch = {'t': te, 'n': n, 'grund': 'Operator am gedehnten Netz: ' + repr(exc)[:300]}
                break
            x2, y2, minfo = td.abbilden(N, N2, xe, ye, besch, args.lesart)
            H2, V2, K2 = N2.energie(x2, y2)
            rec.update({'ausgefuehrt': True, 'H_vor': H1, 'V_vor': V1, 'K_vor': K1, 'H_nach': H2, 'V_nach': V2,
                        'K_nach': K2, 'dH_rel': (H2 - H1) / H0, 'dV_rel': (V2 - V1) / H0, 'dK_rel': (K2 - K1) / H0,
                        'abbildung': {k: v for k, v in minfo.items() if k != 'jrow'}, 'E_nach': N2.E,
                        'T_nach': int(len(Gn)), 'nach': kurz(N2),
                        'stabil_dt': float(np.sqrt(max(N2.eig['w2_max'], 0.0)) * dt)})
            if N1g is not None:
                H1g = N1g.energie(xe, ye)[0]
                rec.update({'alt_gd': kurz(N1g), 'dH_neu_rel': (H1g - H1) / H0, 'dH_zug_rel': (H2 - H1g) / H0})
            if N2h is not None:
                x2h, y2h, _ = td.abbilden(N, N2h, xe, ye, besch, args.lesart)
                rec['hg_vergleich'] = kurz(N2h)
                rec['hg_vergleich']['dH_rel'] = (N2h.energie(x2h, y2h)[0] - H1) / H0
            ereig.append(rec)
            N = N2
            f_eins = False
            x, y, Bx = x2, y2, None
            mu_n = N.mu_alle(x)
            for jj in np.nonzero(mu_n < 0)[0]:
                gesperrt.add(tuple(N.fkeys[N.fl['t1'][jj] * 4 + N.fl['i1'][jj]].tolist()))
            rec['nach_zug_verletzt'] = int((mu_n < 0).sum())
            rem -= tau
            t_cur = te
            if time.time() - T0w > args.budget + 110:
                abbruch = {'t': te, 'n': n, 'grund': 'Zeitgrenze innerhalb eines Schritts (Abschnitt nicht fortsetzbar)'}
                break
        if abbruch is not None:
            break
        n += 1
        if args.arm == 'b' and gesperrt:
            mu_n = N.mu_alle(x)
            fk = N.fkeys[N.fl['t1'] * 4 + N.fl['i1']]
            frei = set(tuple(r_) for r_ in fk[mu_n > 0].tolist())
            gesperrt -= frei
        Hn = N.energie(x, y)[0]
        if not np.all(np.isfinite(x)) or float(np.linalg.norm(x)) > 1e6 * xref:
            abbruch = {'t': n * dt, 'n': n, 'grund': 'Zustand > 1e6 x Anfangsmode oder nicht endlich'}
        elif abs(Hn - H0) > args.hmax * H0:
            abbruch = {'t': n * dt, 'n': n, 'grund': '|H - H0| > %g H0 (Kaskade)' % args.hmax}
        elif len([e_ for e_ in ereig if e_.get('ausgefuehrt')]) > args.zugmax:
            abbruch = {'t': n * dt, 'n': n, 'grund': 'mehr als %d Zuege' % args.zugmax}
        if abbruch is not None:
            probe(N, x, y, n * dt)
            break
        if n % ds == 0 or n == nges:
            probe(N, x, y, n * dt)
        if n % NT == 0:
            fk = set(map(tuple, N.fkeys.tolist()))
            gleich = (len(N.G) == len(G0)) and fk == fkeys0
            perioden.append({'periode': n // NT, 't': n * dt, 'flaechen_wie_anfang': len(fkeys0 & fk) / len(fkeys0),
                             'flaechen_neu': len(fk - fkeys0), 'gleiche_zerlegung': bool(gleich), 'eig': N.eig,
                             'n_zuege': len([e_ for e_ in ereig if e_.get('ausgefuehrt')])})
    fertig = (n >= nges) or (abbruch is not None)
    meta = {'proben': proben, 'ereignisse': ereig, 'perioden': perioden, 'gesperrt': [list(g) for g in gesperrt],
            'abschnitt': abschnitt}
    if not fertig:
        with open(args.out + '.zustand.json.tmp', 'w') as fh:
            json.dump(meta, fh, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
        np.savez(args.out + '.zustand.tmp.npz', x=x, y=y, n=n, G=N.G, O=N.O, f=N.f, f_eins=bool(f_eins))
        os.replace(args.out + '.zustand.json.tmp', args.out + '.zustand.json')
        os.replace(args.out + '.zustand.tmp.npz', zfile)
    else:
        for fpath in (zfile, args.out + '.zustand.json'):
            if os.path.exists(fpath):
                os.rename(fpath, fpath + '.erledigt')
    return {'netz': args.netz, 'ninfo': {k: v for k, v in ninfo.items() if k != 'pruefung'}, 'A': args.A,
            'arm': args.arm, 'lesart': args.lesart, 'h': args.h, 'perioden_soll': args.perioden, 'fertig': fertig,
            'abschnitt': abschnitt, 'n': n, 'nges': nges, 'NT': NT, 'dt': dt, 'T': Tper, 'omega_max': float(wmax),
            'mode': {k: v for k, v in mode.items() if k not in ('tt_leser_mode', 'tt_richtung')}, 'H0': H0,
            'N0': {'E': N0.E, 'm': N0.m, 'eig': N0.eig, 'meff': kurz(N0)},
            'proben_spalten': ['t', 'H', 'V', 'K', 'cos+', 'cosx', 'sin+', 'sinx', 'n_zuege', 'n_mu_neg', 'mu_min'],
            'proben': proben, 'ereignisse': ereig, 'perioden': perioden, 'abbruch': abbruch,
            'netze_abschnitt': NETZE, 'wand_s': time.time() - T0w}


# ------------------------------------------------------------------------------------------------ Rauchtest
def rauch(a):
    """NetzG ohne Dehnung gegen NetzM (uf), NetzG mit f = 1 explizit, mit kleiner Dehnung (Zustand nach 0,2 T)."""
    out = {}
    LV, pos, G0, O0, ninfo = td.netz_bauen(a.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    t = time.time()
    Nm = uf.NetzM(LV, pos, G0, O0, k1, hp, hx)
    out['t_netzM_s'] = time.time() - t
    t = time.time()
    N0 = NetzG(LV, pos, G0, O0, k1, hp, hx, rolle='start')
    out['t_netzG_s'] = time.time() - t
    out['Ar_rel_G_gegen_M'] = float(np.abs(N0.Ar - Nm.Ar).max() / np.abs(Nm.Ar).max())
    N1 = NetzG(LV, pos, G0, O0, k1, hp, hx, f=np.ones(N0.E), rolle='f1')
    out['f1'] = kurz(N1)
    out['f1_M_rel'] = float(np.abs(N1.M - N0.M).max() / np.abs(N0.M).max())
    out['f1_Ar_rel'] = float(np.abs(N1.Ar - N0.Ar).max() / np.abs(N0.Ar).max())
    out['f1_Br_rel'] = float(np.abs(N1.Br - N0.Br).max() / np.abs(N0.Br).max())
    mode, xm, w2, Qm = td.tt_mode(N0, a.A, k1)
    # Zustand bei Viertelperiode: x = Mode (Amplitude A)
    aa = N0.S @ xm
    for skal in (1.0, 0.1):
        Nd = NetzG(LV, pos, G0, O0, k1, hp, hx, f=1.0 + skal * aa, rolle='dehn%g' % skal)
        r = kurz(Nd)
        r['dM_rel'] = float(np.linalg.norm(Nd.M - N0.M) / np.linalg.norm(N0.M))
        r['dAr_rel'] = float(np.linalg.norm(Nd.Ar - N0.Ar) / np.linalg.norm(N0.Ar))
        r['dBr_rel'] = float(np.linalg.norm(Nd.Br - N0.Br) / np.linalg.norm(N0.Br))
        y0 = sla.lu_solve(N0.lu, mode['omega'] * xm)
        r['K_rel'] = float((Nd.energie(np.zeros(N0.m), y0)[0] - N0.energie(np.zeros(N0.m), y0)[0]) /
                           N0.energie(np.zeros(N0.m), y0)[0])
        r['V_rel'] = float((Nd.energie(xm, 0 * y0)[1] - N0.energie(xm, 0 * y0)[1]) / N0.energie(xm, 0 * y0)[1])
        r['a_max'] = float(np.abs(skal * aa).max())
        out['dehn_%g' % skal] = r
    out['omega'] = mode['omega']
    out['NT_h05'] = int(np.ceil(2 * np.pi / mode['omega'] * np.sqrt(N0.eig['w2_max']) / 0.5))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf', 'rauch'])
    ap.add_argument('--netz', default='glas-N128-s1')
    ap.add_argument('--A', type=float, default=1e-3)
    ap.add_argument('--arm', default='b', choices=['a', 'b'])
    ap.add_argument('--lesart', default='R', choices=['R', 'P'])
    ap.add_argument('--h', type=float, default=0.5, help='omega_max * dt')
    ap.add_argument('--perioden', type=int, default=10)
    ap.add_argument('--proben', type=int, default=200)
    ap.add_argument('--budget', type=float, default=480.0)
    ap.add_argument('--split', type=int, default=1)
    ap.add_argument('--vergleich', type=int, default=1)
    ap.add_argument('--hmax', type=float, default=100.0)
    ap.add_argument('--zugmax', type=int, default=200)
    ap.add_argument('--bgd', type=int, default=1, help='1: B am gedehnten Netz (Karte G1), 0: B am Hintergrund (G1m)')
    ap.add_argument('--vorlauf', type=float, default=0.0, help='0: G1 (Karte); > 0: G1v, Operatoren bei mu_j <= -vorlauf')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    B_GD['an'] = bool(a.bgd)
    t0 = time.time()
    me = os.path.abspath(__file__)
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'skript_sha256': td.sha(me),
            'module_sha256': {m.__name__: td.sha(os.path.abspath(m.__file__))
                              for m in (tg, uk, tu, td, uv, rk, rk2, pt, u4, uf)},
            'h_zelt': uf.H_ZELT, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'rauch':
        erg = rauch(a)
        erg['netze'] = NETZE
    else:
        erg = lauf(a)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], 'fertig=%s' % erg.get('fertig'), flush=True)


if __name__ == '__main__':
    main()
