#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERGABE-KONFLUENZ-1 (Runde 48, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage (KARTE.md): Haengt der Zustand nach zwei gleichzeitig faelligen Umklappzuegen X, Y von ihrer Reihenfolge ab
(XY gegen YX), mit Feldern?

Aufbau (PLAN.md):
  Netz: Glas N = 128 (tg.zufallsnetz, TT-GLAS-1, Saaten 1 bis 4), Hintergrund flach, Operatoren wie td.py (Lesart H).
  Eine kleine Eckverschiebung des Hintergrunds macht genau zwei Flaechen X, Y gleichzeitig nicht lokal Delaunay
  (mu = -MU_ZIEL). Ueberlappungsarten: T = gemeinsames Tetraeder, K = gemeinsame Flaechenkante ohne gemeinsames
  Tetraeder, D = Doppelpyramiden ohne gemeinsame Ecke (Kontrolle UK0).
  Reihenfolge XY: Zug an X, dann "umklappen bis Delaunay" (Regel wie tu.reparatur: staerkste Verletzung zuerst,
  2-3 wenn konvex, sonst 3-2); YX: Zug an Y, dann dieselbe Regel.
  Zustand: Geometrie = TT-Mode (td.tt_mode) mit TT-Amplitude A_Q, Phase PHASE (x und y ungleich null);
  Skalar auf den Ecken (phi, pi), stehende Welle cos(k1 . r + PHI_PHASE), Amplituden A_PHI.
  Uebergabe Geometrie: td.abbilden unveraendert (Lesart R: Laengen und Raten stetig, Projektion; Lesart P: Impulse).
  Uebergabe Skalar: Ecken bleiben bei 2-3/3-2; phi stetig; Lesart R: dphi/dt = pi / *0 stetig; Lesart P: pi stetig.
  Bewegungsenergie: Form A = A1 (td.Netz) und A2 (hm_td, Kartenformel); Form B = A2L (hm_td), nur wenn A_red im
  Ausgangsnetz positiv definit ist ("startbar").
  Zeitumkehr (statisch): Endzustand von XY mit umgekehrten Impulsen durch die inversen Zuege in umgekehrter Reihenfolge,
  dann Impulse zurueck, Vergleich mit dem Anfangszustand.
Unveraendert importiert: td.py, hm_td.py, tg.py, uk.py, tu.py (und deren Importe tp.py, ew.py, mn.py, tg_auswertung.py).
Modi: lauf (eine Saat), haeufigkeit (vorhandene TAKT-DYNAMIK-1-Laeufe), auswertung (Urteile nach PLAN 7).
"""
import argparse, json, os, sys, time, hashlib, platform, resource, glob
from collections import Counter
import numpy as np
import scipy
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import uk  # noqa: E402
import tu  # noqa: E402
import td  # noqa: E402
import hm_td  # noqa: E402

TOL_MU = tu.TOL_MU           # 1e-9: mu < -TOL_MU = Delaunay verletzt (wie tu.reparatur)
MU_ZIEL = 1e-3               # Zielverletzung der beiden Flaechen nach der Verschiebung: mu = -MU_ZIEL
DELTA_MAX_REL = 0.1          # Eckverschiebung hoechstens 0,1 x mittlere Kantenlaenge (je Ecke)
N_FAELLE = 5                 # Faelle je Ueberlappungsart und Saat
N_KAND = 80                  # hoechstens so viele Kandidatenpaare je Art (nach Score)
N_D_FLAECHEN = 40            # D: Paare unter den N_D_FLAECHEN Flaechen mit kleinstem mu0
A_Q = 1e-3                   # Geometrie: TT-Amplitude der Mode (wie TAKT-DYNAMIK-1)
PHASE = 1.0                  # Phase der stehenden Mode (rad): x = sin(PHASE) x_Mode
PHI_PHASE = 0.3              # Skalar: phi_v = A cos(k1 . r_v + PHI_PHASE)
A_PHI = [0.0, 1e-3, 1e-2]    # Skalar-Amplituden (Karte)
Z_S = 8.0                    # Skalar-Energie: H_phi = 1/2 pi^T *0^-1 pi + Z_S/2 (d0 phi)^T *1 (d0 phi) (Takt-Normierung)
MAX_ZUEGE = 12
ARTEN = ['D', 'T', 'K']
FORMEN = ['A1', 'A2', 'A2L']
LESARTEN = ['R', 'P']


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def schreibe(pfad, res):
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(pfad + '.tmp', pfad)


# ------------------------------------------------------------------------------------------------ Netze und Formen
def netz(form, LV, pos, G, O, k1, hp, hx):
    """Operatoren der Zerlegung (G, O) auf den Hintergrundlagen pos; Form A1 = td.Netz, A2 / A2L = hm_td.NetzHM (R1)."""
    if form == 'A1':
        N = td.Netz(LV, pos, G, O, k1, hp, hx, eigen=False)
    else:
        hm_td.KIN = form
        hm_td.RED = 'R1'
        N = hm_td.NetzHM(LV, pos, G, O, k1, hp, hx, eigen=False)
    N.hp = hp
    return N


def tet_menge(G, O):
    return frozenset(map(tuple, uk.tetra_schluessel(G, O).tolist()))


# ------------------------------------------------------------------------------------------------ Skalar auf den Ecken
def skalar_ops(N):
    """*0 je Ecke und *1 je Kante (umkreisbasiert, vorzeichenbehaftet; tu.hodge unveraendert, *0 aus dessen Formel)."""
    h, s1, s2, Ast = tu.hodge(N.LV, N.pos, N.G, N.O, N.mod)
    X = tu.tet_X(N.LV, N.pos, N.G, N.O)
    s0 = np.zeros(N.nV)
    for p, (i, j, _, _) in enumerate(tg.PAARE):
        lt = np.linalg.norm(X[:, j] - X[:, i], axis=1)
        w = lt * Ast[:, p] / 6.0
        s0 += np.bincount(N.G[:, i], w, N.nV) + np.bincount(N.G[:, j], w, N.nV)
    return {'s0': s0, 's1': s1, 'es': N.mod['es'], 'es2': N.mod['es2'],
            'kontr_s0_durch_V': float(s0.sum() / N.mod['Vbox']), 's0_min_rel': float(s0.min() / s0.mean()),
            'stern1_n_neg': int(h['stern1_n_neg']), 'stern0_n_neg': int(h['stern0_n_neg']),
            'mu_n_verletzt': int(h['mu_n_verletzt'])}


def H_phi(sk, phi, pi):
    d = phi[sk['es2']] - phi[sk['es']]
    return 0.5 * float(np.sum(pi ** 2 / sk['s0'])) + 0.5 * Z_S * float(np.sum(sk['s1'] * d ** 2))


def skalar_ueber(sk, sk2, phi, pi, lesart):
    """Uebergabe ueber einen Zug (Ecken unveraendert): phi stetig; R: dphi/dt = pi / *0 stetig; P: pi stetig."""
    if lesart == 'R':
        return phi.copy(), sk2['s0'] * (pi / sk['s0'])
    return phi.copy(), pi.copy()


# ------------------------------------------------------------------------------------------------ Zuege
def zug_waehlen(N, j, vmin, geo=None):
    """Zug an Flaeche j wie tu.reparatur: 2-3, wenn die Doppelpyramide konvex ist (tu.zug23_ok), sonst 3-2 ueber die
    Kante, hinter der d-e die Flaechenebene trifft (Grad 3, tu.zug32_vorbereiten). Ausfuehrung td.zug_ausfuehren."""
    if geo is None:
        _, geo = tu.flaechen_geo(N.LV, N.pos, N.G, N.O)
    v = geo['v'][j]
    if (v > 0).all() or (v < 0).all():
        aus = td.zug_ausfuehren(N, j, 23, None, vmin)
        return None if aus is None else (23, None, aus)
    r = tu.ungerade(v)
    if r is None:
        return None
    aus = td.zug_ausfuehren(N, j, 32, r, vmin)
    return None if aus is None else (32, r, aus)


def folge(N0, erster, vmin, bau):
    """Zug an Flaeche 'erster', dann umklappen bis Delaunay auf dem Hintergrund. Rueckgabe Netze, Beschreibungen, Zuege,
    Status ('ok', 'stecken', 'max', 'erster nicht ausfuehrbar')."""
    netze, beschr, zuege = [N0], [], []
    N = N0
    fl, geo = tu.flaechen_geo(N.LV, N.pos, N.G, N.O)
    mu = uk.raender(N.LV, N.pos, N.G, N.O, fl)
    j = int(erster)
    w = zug_waehlen(N, j, vmin, geo)
    if w is None:
        return netze, beschr, zuege, 'erster nicht ausfuehrbar'
    while True:
        typ, r, (Gn, On, b) = w
        zuege.append({'typ': int(typ), 'mu': float(mu[j]), 'kante_neu': b['kante_neu'], 'kante_weg': b['kante_weg']})
        N = bau(Gn, On)
        netze.append(N)
        beschr.append(b)
        fl, geo = tu.flaechen_geo(N.LV, N.pos, N.G, N.O)
        mu = uk.raender(N.LV, N.pos, N.G, N.O, fl)
        verl = np.nonzero(mu < -TOL_MU)[0]
        if len(verl) == 0:
            return netze, beschr, zuege, 'ok'
        if len(zuege) >= MAX_ZUEGE:
            return netze, beschr, zuege, 'max'
        verl = verl[np.argsort(mu[verl])]
        w = None
        for jj in verl:
            w = zug_waehlen(N, int(jj), vmin, geo)
            if w is not None:
                j = int(jj)
                break
        if w is None:
            return netze, beschr, zuege, 'stecken'


def invers(b):
    """Beschreibung des inversen Zugs (2-3 <-> 3-2) fuer td.abbilden: dieselben 9 Kanten der flachen Doppelpyramide."""
    return {'alt': b['neu'], 'neu': b['alt'], 'kante_neu': b['kante_weg'], 'kante_weg': b['kante_neu'], 'k9': b['k9'],
            'tets_alt_idx': None}


def uebertrage(netze, beschr, x, y, lesart):
    infos = []
    for i in range(len(beschr)):
        x, y, info = td.abbilden(netze[i], netze[i + 1], x, y, beschr[i], lesart)
        infos.append({k: info[k] for k in ('proj_rest_a', 'proj_rest_ad', 'proj_rest_p', 'delta_nichtflach') if k in info})
    return x, y, infos


def zurueck(netze, beschr, x, y, lesart):
    for i in reversed(range(len(beschr))):
        x, y, _ = td.abbilden(netze[i + 1], netze[i], x, y, invers(beschr[i]), lesart)
    return x, y


def skalar_kette(sks, phi, pi, lesart, rueck=False):
    idx = range(len(sks) - 1)
    if not rueck:
        for i in idx:
            phi, pi = skalar_ueber(sks[i], sks[i + 1], phi, pi, lesart)
    else:
        for i in reversed(idx):
            phi, pi = skalar_ueber(sks[i + 1], sks[i], phi, pi, lesart)
    return phi, pi


def rel(u, v):
    n = max(float(np.linalg.norm(u)), float(np.linalg.norm(v)))
    return float(np.linalg.norm(u - v) / n) if n > 0 else 0.0


# ------------------------------------------------------------------------------------------------ Auswahl der Paare
def mu_teil(LV, pos, G, O, fl, idx):
    idx = np.asarray(idx)
    sub = {'t1': fl['t1'][idx], 'i2': fl['i2'][idx], 't2': fl['t2'][idx], 'sh': fl['sh'][idx]}
    return uk.raender(LV, pos, G, O, sub)


def newton(LV, pos, G, O, fl, v, idx, lbar):
    """Kleinste Verschiebung der Ecke v, mit der die Flaechen idx genau mu = -MU_ZIEL erreichen (Gauss-Newton,
    Mindestnorm, zentrale Differenzen)."""
    dl = np.zeros(3)
    h = 1e-6 * lbar
    for _ in range(40):
        p = pos.copy()
        p[v] += dl
        F = mu_teil(LV, p, G, O, fl, idx) + MU_ZIEL
        if np.abs(F).max() < 1e-12:
            return dl
        J = np.zeros((len(idx), 3))
        for c in range(3):
            pp = p.copy()
            pp[v, c] += h
            pm = p.copy()
            pm[v, c] -= h
            J[:, c] = (mu_teil(LV, pp, G, O, fl, idx) - mu_teil(LV, pm, G, O, fl, idx)) / (2 * h)
        JJ = J @ J.T
        if not np.all(np.isfinite(JJ)) or np.linalg.cond(JJ) > 1e10:
            return None
        dl = dl - J.T @ np.linalg.solve(JJ, F)
        if not np.all(np.isfinite(dl)) or np.linalg.norm(dl) > 3 * DELTA_MAX_REL * lbar:
            return None
    return None


def ausfuehrbar(LV, pos2, G, O, j, vmin):
    fl, geo = tu.flaechen_geo(LV, pos2, G, O)
    v = geo['v'][j]
    if (v > 0).all() or (v < 0).all():
        km = set(uk.kanten(LV, pos2, G, O, len(pos2))[0].tolist())
        return 23 if tu.zug23_ok(LV, pos2, G, O, geo, j, km, vmin) else None
    r = tu.ungerade(v)
    if r is None:
        return None
    info = tu.zug32_vorbereiten(LV, pos2, G, O, fl, geo, j, r, tu.tet_dict(G, O), vmin)
    return 32 if info is not None else None


def paare(N, mu0, art):
    """Kandidatenpaare (X, Y) der Art, nach Score max(mu0_X, mu0_Y) aufsteigend."""
    fl = N.fl
    F = fl['F']
    t1, i1, t2, i2 = fl['t1'], fl['i1'], fl['t2'], fl['i2']
    V5 = np.concatenate([N.G[t1[:, None], uk.FL[i1]], N.G[t1, i1][:, None], N.G[t2, i2][:, None]], 1)
    gut = np.array([len(set(r)) == 5 for r in V5.tolist()])
    kand = set()
    if art == 'T':
        tf = [[] for _ in range(len(N.G))]
        for f in range(F):
            tf[t1[f]].append(f)
            tf[t2[f]].append(f)
        for lst in tf:
            for a in range(len(lst)):
                for b in range(a + 1, len(lst)):
                    kand.add((min(lst[a], lst[b]), max(lst[a], lst[b])))
    elif art == 'K':
        ef = {}
        for f in range(F):
            for e in N.f9[f, :3].tolist():
                ef.setdefault(e, []).append(f)
        for lst in ef.values():
            for a in range(len(lst)):
                for b in range(a + 1, len(lst)):
                    x, y = lst[a], lst[b]
                    if {t1[x], t2[x]} & {t1[y], t2[y]}:
                        continue
                    kand.add((min(x, y), max(x, y)))
    else:
        o = np.argsort(mu0)
        o = [int(f) for f in o if gut[f]][:N_D_FLAECHEN]
        for a in range(len(o)):
            for b in range(a + 1, len(o)):
                x, y = o[a], o[b]
                if set(V5[x].tolist()) & set(V5[y].tolist()):
                    continue
                kand.add((min(x, y), max(x, y)))
    kand = [(x, y) for (x, y) in kand if gut[x] and gut[y]]
    kand.sort(key=lambda q: (max(mu0[q[0]], mu0[q[1]]), q))
    return kand, V5


def verschiebung(LV, pos, G, O, fl, X, Y, V5, art, lbar, vz0, vbar):
    """Beste (kleinste) zulaessige Eckverschiebung fuer das Paar; None, wenn keine."""
    vmin = td.VMIN_B * vbar
    opt = []
    sX, sY = set(V5[X].tolist()), set(V5[Y].tolist())
    if art in ('T', 'K'):
        for v in sorted(sX & sY):
            dl = newton(LV, pos, G, O, fl, v, [X, Y], lbar)
            if dl is not None and np.linalg.norm(dl) <= DELTA_MAX_REL * lbar:
                opt.append((float(np.linalg.norm(dl)), [(v, dl)]))
    ox, oy = [], []
    for v in sorted(sX - sY):
        dl = newton(LV, pos, G, O, fl, v, [X], lbar)
        if dl is not None and np.linalg.norm(dl) <= DELTA_MAX_REL * lbar:
            ox.append((float(np.linalg.norm(dl)), v, dl))
    for v in sorted(sY - sX):
        dl = newton(LV, pos, G, O, fl, v, [Y], lbar)
        if dl is not None and np.linalg.norm(dl) <= DELTA_MAX_REL * lbar:
            oy.append((float(np.linalg.norm(dl)), v, dl))
    ox.sort(key=lambda q: q[0])
    oy.sort(key=lambda q: q[0])
    for a in ox[:3]:
        for b in oy[:3]:
            if a[1] != b[1]:
                opt.append((float(np.hypot(a[0], b[0])), [(a[1], a[2]), (b[1], b[2])]))
    opt.sort(key=lambda q: q[0])
    for norm, vs in opt:
        p2 = pos.copy()
        for v, dl in vs:
            p2[v] = p2[v] + dl
        mu = uk.raender(LV, p2, G, O, fl)
        if set(np.nonzero(mu < -TOL_MU)[0].tolist()) != {X, Y}:
            continue
        if not np.array_equal(tu.vorzeichen_vol(LV, p2, G, O), vz0):
            continue
        tX = ausfuehrbar(LV, p2, G, O, X, vmin)
        tY = ausfuehrbar(LV, p2, G, O, Y, vmin)
        if tX is None or tY is None:
            continue
        mo = mu.copy()
        mo[[X, Y]] = np.inf
        return {'pos': p2, 'ecken': [[int(v), [float(q) for q in dl]] for v, dl in vs], 'norm': norm,
                'norm_rel': norm / lbar, 'typ_X': tX, 'typ_Y': tY, 'mu_X': float(mu[X]), 'mu_Y': float(mu[Y]),
                'mu_andere_min': float(mo.min())}
    return None


# ------------------------------------------------------------------------------------------------ ein Fall
def fall_rechnen(LV, pos2, G0, O0, k1, hp, hx, X, Y):
    out = {}
    t0 = time.time()
    # Kombinatorik und A1-Netze
    bau1 = lambda G, O: netz('A1', LV, pos2, G, O, k1, hp, hx)  # noqa: E731
    N0 = bau1(G0, O0)
    vmin = td.VMIN_B * N0.vbar
    ketten = {}
    for ordn, erster in (('XY', X), ('YX', Y)):
        netze, beschr, zuege, st = folge(N0, erster, vmin, bau1)
        ketten[ordn] = {'A1': netze, 'beschr': beschr, 'zuege': zuege, 'status': st,
                        'GO': [(N.G, N.O) for N in netze]}
        out['zuege_' + ordn] = zuege
        out['status_' + ordn] = st
    ok = ketten['XY']['status'] == 'ok' and ketten['YX']['status'] == 'ok'
    gleich = bool(ok and tet_menge(*ketten['XY']['GO'][-1]) == tet_menge(*ketten['YX']['GO'][-1]))
    out['gleiche_endzerlegung'] = gleich
    out['t_kombinatorik_s'] = time.time() - t0
    if not gleich:
        return out
    NXY, NYX = ketten['XY']['A1'][-1], ketten['YX']['A1'][-1]
    out['gleiche_kanten'] = bool(np.array_equal(NXY.keys, NYX.keys))
    # Skalar (formunabhaengig)
    for ordn in ('XY', 'YX'):
        ketten[ordn]['sk'] = [skalar_ops(N) for N in ketten[ordn]['A1']]
    sk0 = ketten['XY']['sk'][0]
    out['skalar_kontrolle'] = {'s0_durch_V_anfang': sk0['kontr_s0_durch_V'], 's0_min_rel_anfang': sk0['s0_min_rel'],
                               's0_min_rel_alle': float(min(s['s0_min_rel'] for o in ('XY', 'YX') for s in ketten[o]['sk'])),
                               'stern0_n_neg_max': int(max(s['stern0_n_neg'] for o in ('XY', 'YX') for s in ketten[o]['sk'])),
                               'mu_n_verletzt_ende': [ketten[o]['sk'][-1]['mu_n_verletzt'] for o in ('XY', 'YX')]}
    ph = pos2 @ k1 + PHI_PHASE
    kk = float(np.linalg.norm(k1))
    sk_res = {}
    for les in LESARTEN:
        sk_res[les] = {}
        for amp in A_PHI:
            phi0 = amp * np.cos(ph)
            pi0 = sk0['s0'] * amp * kk * np.sin(ph)
            r = {}
            fin = {}
            for ordn in ('XY', 'YX'):
                fin[ordn] = skalar_kette(ketten[ordn]['sk'], phi0, pi0, les)
            (pX, qX), (pY, qY) = fin['XY'], fin['YX']
            r['d_phi_rel'], r['d_pi_rel'] = rel(pX, pY), rel(qX, qY)
            r['d_phi_abs'], r['d_pi_abs'] = float(np.linalg.norm(pX - pY)), float(np.linalg.norm(qX - qY))
            r['H_XY'] = H_phi(ketten['XY']['sk'][-1], pX, qX)
            r['H_YX'] = H_phi(ketten['YX']['sk'][-1], pY, qY)
            r['H0'] = H_phi(sk0, phi0, pi0)
            # Zeitumkehr (statisch) fuer beide Reihenfolgen
            for ordn in ('XY', 'YX'):
                pb, qb = skalar_kette(ketten[ordn]['sk'], fin[ordn][0], -fin[ordn][1], les, rueck=True)
                r['tu_' + ordn + '_phi_rel'] = rel(pb, phi0)
                r['tu_' + ordn + '_pi_rel'] = rel(-qb, pi0)
            sk_res[les]['%g' % amp] = r
    out['skalar'] = sk_res
    out['licht'] = 'nicht gerechnet (kein Lichtsektor im Vorlagencode)'
    # Geometrie je Form
    formen = {}
    for form in FORMEN:
        t1 = time.time()
        fr = {}
        hm_td.VREF = None
        if form == 'A1':
            nets = {o: ketten[o]['A1'] for o in ('XY', 'YX')}
        else:
            n0 = netz(form, LV, pos2, G0, O0, k1, hp, hx)
            fr['startbar'] = bool(n0.A_pd)
            fr['n_A_neg'] = int(n0.n_A_neg)
            if not n0.A_pd:
                formen[form] = fr
                continue
            nets = {}
            for o in ('XY', 'YX'):
                nets[o] = [n0] + [netz(form, LV, pos2, G, O, k1, hp, hx) for (G, O) in ketten[o]['GO'][1:]]
        n0 = nets['XY'][0]
        fr['startbar'] = bool(n0.A_pd)
        fr['n_A_neg'] = int(n0.n_A_neg)
        if not n0.A_pd:
            formen[form] = fr
            continue
        mode, xm, w2, Qm = td.tt_mode(n0, A_Q, k1)
        fr['mode'] = {k: mode[k] for k in ('omega', 'anteil_TT_welle')}
        x0 = np.sin(PHASE) * xm
        y0 = sla.lu_solve(n0.lu, mode['omega'] * np.cos(PHASE) * xm)
        a0, p0 = n0.S @ x0, n0.S @ y0
        fr['H0_geo'] = n0.energie(x0, y0)[0]
        fr['A_pd_alle'] = bool(all(N.A_pd for o in ('XY', 'YX') for N in nets[o]))
        for les in LESARTEN:
            r = {}
            fin = {}
            for o in ('XY', 'YX'):
                x, y, infos = uebertrage(nets[o], ketten[o]['beschr'], x0, y0, les)
                N = nets[o][-1]
                fin[o] = (N.S @ x, N.S @ y, N.energie(x, y)[0])
                r['infos_' + o] = infos
                xb, yb = zurueck(nets[o], ketten[o]['beschr'], x, -y, les)
                yb = -yb
                r['tu_' + o + '_q_rel'] = rel(n0.S @ xb, a0)
                r['tu_' + o + '_p_rel'] = rel(n0.S @ yb, p0)
            (aX, pX, HX), (aY, pY, HY) = fin['XY'], fin['YX']
            r['d_q_rel'], r['d_p_rel'] = rel(aX, aY), rel(pX, pY)
            r['d_q_abs'], r['d_p_abs'] = float(np.linalg.norm(aX - aY)), float(np.linalg.norm(pX - pY))
            r['H_XY'], r['H_YX'] = HX, HY
            r['d_H_geo_rel'] = abs(HX - HY) / abs(HX) if HX != 0 else 0.0
            r['zwangsrest_XY_summe'] = float(sum(i.get('proj_rest_a', 0.0) for i in r['infos_XY']))
            r['zwangsrest_YX_summe'] = float(sum(i.get('proj_rest_a', 0.0) for i in r['infos_YX']))
            # Delta_H gesamt je Skalar-Amplitude
            r['d_H_gesamt_rel'] = {}
            for amp in A_PHI:
                s = sk_res[les]['%g' % amp]
                hx_, hy_ = HX + s['H_XY'], HY + s['H_YX']
                r['d_H_gesamt_rel']['%g' % amp] = abs(hx_ - hy_) / abs(hx_) if hx_ != 0 else 0.0
            fr[les] = r
        fr['t_s'] = time.time() - t1
        formen[form] = fr
    out['formen'] = formen
    out['t_gesamt_s'] = time.time() - t0
    return out


def lauf(args):
    T0 = time.time()
    s = args.saat
    LV, pos, G0, O0, pr = tg.zufallsnetz(128, s)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    N = netz('A1', LV, pos, G0, O0, k1, hp, hx)
    lbar = float(N.l0.mean())
    vbar = float(N.vbar)
    fl = N.fl
    mu0 = uk.raender(LV, pos, G0, O0, fl)
    vz0 = tu.vorzeichen_vol(LV, pos, G0, O0)
    res = {'saat': s, 'netz': {'nV': int(N.nV), 'E': int(N.E), 'T': int(len(G0)), 'F': int(fl['F']), 'l_mittel': lbar,
                               'mu0_min': float(mu0.min()), 'mu0_n_verletzt': int((mu0 < -TOL_MU).sum())},
           'faelle': [], 'auswahl': {}}
    n_faelle = 1 if args.rauch else (args.faelle if args.faelle else N_FAELLE)
    for art in ARTEN:
        t1 = time.time()
        kand, V5 = paare(N, mu0, art)
        ang, versucht, benutzt = 0, 0, set()
        for (X, Y) in kand[:N_KAND]:
            if ang >= n_faelle:
                break
            if X in benutzt or Y in benutzt:
                continue
            versucht += 1
            v = verschiebung(LV, pos, G0, O0, fl, X, Y, V5, art, lbar, vz0, vbar)
            if v is None:
                continue
            f = {'art': art, 'X': int(X), 'Y': int(Y), 'V5_X': V5[X].tolist(), 'V5_Y': V5[Y].tolist(),
                 'mu0_X': float(mu0[X]), 'mu0_Y': float(mu0[Y]),
                 'verschiebung': {k: v[k] for k in v if k != 'pos'}}
            f.update(fall_rechnen(LV, v['pos'], G0, O0, k1, hp, hx, X, Y))
            res['faelle'].append(f)
            benutzt |= {X, Y}
            ang += 1
        res['auswahl'][art] = {'kandidaten': len(kand), 'versucht': versucht, 'angenommen': ang,
                               't_s': time.time() - t1}
    res['wand_s'] = time.time() - T0
    return res


# ------------------------------------------------------------------------------------------------ Haeufigkeit (beschreibend)
def haeufigkeit(ordner):
    out = []
    for s in (1, 2, 3, 4):
        for h, suf in ((0.5, ''), (0.25, '-h025')):
            p = os.path.join(ordner, 'td-glas-N128-s%d-A1e-3-b%s.json' % (s, suf))
            if not os.path.exists(p):
                out.append({'saat': s, 'h': h, 'fehlt': p})
                continue
            d = json.load(open(p))['ergebnis']
            ev = d['ereignisse']
            c_alle = Counter(int(e['n']) for e in ev)
            c_zug = Counter(int(e['n']) for e in ev if e.get('ausgefuehrt'))
            nges = int(d['nges'])
            z = {'saat': s, 'h': h, 'datei': os.path.basename(p), 'sha256': sha(p), 'fertig': d['fertig'],
                 'nges': nges, 'n_schritte_gelaufen': int(d['n']), 'NT': int(d['NT']), 'n_ereignisse': len(ev),
                 'n_zuege': int(sum(c_zug.values())),
                 'schritte_mit_ereignis': len(c_alle), 'schritte_mit_zug': len(c_zug),
                 'schritte_ge2_ereignisse': int(sum(1 for v in c_alle.values() if v >= 2)),
                 'schritte_ge2_zuege': int(sum(1 for v in c_zug.values() if v >= 2)),
                 'max_ereignisse_je_schritt': int(max(c_alle.values())) if c_alle else 0,
                 'nach_zug_verletzt_summe': int(sum(e.get('nach_zug_verletzt', 0) for e in ev if e.get('ausgefuehrt'))),
                 'nach_zug_verletzt_ge1': int(sum(1 for e in ev if e.get('ausgefuehrt') and e.get('nach_zug_verletzt', 0) >= 1))}
            nn = max(int(d['n']), 1)
            z['anteil_ge2_ereignisse'] = z['schritte_ge2_ereignisse'] / nn
            z['anteil_ge2_zuege'] = z['schritte_ge2_zuege'] / nn
            z['anteil_ge2_unter_schritten_mit_ereignis'] = (z['schritte_ge2_ereignisse'] / z['schritte_mit_ereignis']
                                                           if z['schritte_mit_ereignis'] else None)
            out.append(z)
    return out


# ------------------------------------------------------------------------------------------------ Auswertung (PLAN 7)
BODEN = 1e-12


def _med(v):
    return float(np.median(v)) if len(v) else None


def auswertung(ordner, haeuf_pfad):
    F = []
    ein = {}
    for p in sorted(glob.glob(os.path.join(ordner, 'konfluenz-s*.json'))):
        d = json.load(open(p))
        if 'ergebnis' not in d:
            continue
        ein[os.path.basename(p)] = sha(p)
        for f in d['ergebnis']['faelle']:
            f = dict(f)
            f['saat'] = d['ergebnis']['saat']
            F.append(f)
    U = {}
    ok = [f for f in F if f.get('gleiche_endzerlegung')]

    def feld(f, les, amp, art='rel'):
        s = f['skalar'][les]['%g' % amp]
        return max(s['d_phi_' + art], s['d_pi_' + art])
    # UK0
    D = [f for f in ok if f['art'] == 'D']
    dmax = []
    for f in D:
        for les in LESARTEN:
            for form in ('A1', 'A2'):
                g = f['formen'].get(form, {}).get(les)
                if g is not None:
                    dmax += [g['d_q_rel'], g['d_p_rel']]
            for amp in A_PHI[1:]:
                dmax.append(feld(f, les, amp))
    komb = [bool(f.get('gleiche_endzerlegung')) for f in F]
    if not F:
        U['UK0'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar', 'grund': 'keine Faelle'}
    else:
        teil2 = all(komb)
        if D:
            teil1 = max(dmax) < BODEN
            u = 'eingetroffen' if (teil1 and teil2) else 'verfehlt'
        else:
            teil1 = None
            u = 'verfehlt' if not teil2 else 'nicht entscheidbar'
        U['UK0'] = {'plan': u, 'wortlaut': u, 'D_faelle': len(D), 'D_max_delta': max(dmax) if dmax else None,
                    'faelle': len(F), 'gleiche_endzerlegung': int(sum(komb)), 'teil_disjunkt': teil1, 'teil_kombinatorik': teil2}
    # UK1
    TK = {art: [f for f in ok if f['art'] == art] for art in ('T', 'K')}
    med = {art: _med([feld(f, 'R', 1e-3) for f in TK[art]]) for art in TK}
    mx = {art: (max([feld(f, 'R', 1e-3) for f in TK[art]]) if TK[art] else None) for art in TK}
    if not TK['T'] and not TK['K']:
        U['UK1'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar'}
    else:
        U['UK1'] = {'plan': 'eingetroffen' if any(m is not None and m > 1e-6 for m in med.values()) else 'verfehlt',
                    'wortlaut': 'eingetroffen' if any(m is not None and m > 1e-6 for m in mx.values()) else 'verfehlt',
                    'median_T': med['T'], 'median_K': med['K'], 'max_T': mx['T'], 'max_K': mx['K'],
                    'n_T': len(TK['T']), 'n_K': len(TK['K'])}
    # UK2
    sl_plan, sl_wort = [], []
    for f in TK['T'] + TK['K']:
        for les in LESARTEN:
            a3, a2 = feld(f, les, 1e-3, 'abs'), feld(f, les, 1e-2, 'abs')
            r3, r2 = feld(f, les, 1e-3), feld(f, les, 1e-2)
            if a3 > 0 and a2 > 0:
                sl = float(np.log10(a2 / a3))
                sl_wort.append(sl)
                if r3 > BODEN and r2 > BODEN:
                    sl_plan.append(sl)

    def urteil_sl(v):
        if not v:
            return 'nicht entscheidbar'
        m = float(np.median(v))
        return 'eingetroffen' if 0.9 <= m <= 1.1 else 'verfehlt'
    U['UK2'] = {'plan': urteil_sl(sl_plan), 'wortlaut': urteil_sl(sl_wort), 'n_plan': len(sl_plan), 'n_wortlaut': len(sl_wort),
                'median_steigung_plan': _med(sl_plan), 'median_steigung_wortlaut': _med(sl_wort)}
    # UK3
    alle = TK['T'] + TK['K']
    mR = _med([feld(f, 'R', 1e-3) for f in alle])
    mP = _med([feld(f, 'P', 1e-3) for f in alle])
    if mR is None:
        U['UK3'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar'}
    else:
        if mR <= BODEN and mP <= BODEN:
            up = 'nicht entscheidbar'
        elif mP <= BODEN:
            up = 'eingetroffen'
        elif mR <= BODEN:
            up = 'verfehlt'
        else:
            up = 'eingetroffen' if mR / mP >= 10 else 'verfehlt'
        if mP > 0:
            uw = 'eingetroffen' if mR / mP >= 10 else 'verfehlt'
        else:
            uw = 'eingetroffen' if mR > 0 else 'nicht entscheidbar'
        U['UK3'] = {'plan': up, 'wortlaut': uw, 'median_R': mR, 'median_P': mP,
                    'verhaeltnis': (mR / mP) if mP else None}
    # UK4
    stb = [f for f in alle if f['formen'].get('A2L', {}).get('startbar')]
    nneg = [f['formen'].get('A2L', {}).get('n_A_neg') for f in F if 'formen' in f]
    if not stb:
        U['UK4'] = {'plan': 'nicht entscheidbar', 'wortlaut': 'nicht entscheidbar', 'grund': 'Form B (A2L) nicht startbar',
                    'n_A_neg_A2L': nneg}
    else:
        r2 = [f['formen']['A2L']['R']['d_p_rel'] / f['formen']['A2']['R']['d_p_rel'] for f in stb
              if 'R' in f['formen'].get('A2', {}) and f['formen']['A2']['R']['d_p_rel'] > 0]
        r1 = [f['formen']['A2L']['R']['d_p_rel'] / f['formen']['A1']['R']['d_p_rel'] for f in stb
              if 'R' in f['formen'].get('A1', {}) and f['formen']['A1']['R']['d_p_rel'] > 0]

        def aus(m):
            return m is not None and (m > 2 or m < 0.5)
        m2, m1 = _med(r2), _med(r1)
        U['UK4'] = {'plan': 'eingetroffen' if aus(m2) else 'verfehlt',
                    'wortlaut': 'eingetroffen' if (aus(m2) and aus(m1)) else 'verfehlt',
                    'median_B_durch_A2': m2, 'median_B_durch_A1': m1, 'n': len(stb)}
    # Tabellen-Rohdaten
    zeilen = []
    for f in F:
        z = {'saat': f['saat'], 'art': f['art'], 'X': f['X'], 'Y': f['Y'], 'verschiebung_rel': f['verschiebung']['norm_rel'],
             'typ_X': f['verschiebung']['typ_X'], 'typ_Y': f['verschiebung']['typ_Y'],
             'zuege_XY': [z_['typ'] for z_ in f.get('zuege_XY', [])], 'zuege_YX': [z_['typ'] for z_ in f.get('zuege_YX', [])],
             'status': [f.get('status_XY'), f.get('status_YX')], 'gleich': f.get('gleiche_endzerlegung')}
        if f.get('gleiche_endzerlegung'):
            for form in FORMEN:
                g = f['formen'].get(form, {})
                z[form] = {'startbar': g.get('startbar'), 'n_A_neg': g.get('n_A_neg')}
                for les in LESARTEN:
                    if les in g:
                        z[form][les] = {k: g[les][k] for k in ('d_q_rel', 'd_p_rel', 'd_q_abs', 'd_p_abs', 'd_H_geo_rel',
                                                              'tu_XY_q_rel', 'tu_XY_p_rel', 'tu_YX_q_rel', 'tu_YX_p_rel',
                                                              'zwangsrest_XY_summe', 'zwangsrest_YX_summe', 'd_H_gesamt_rel')}
            z['skalar'] = {les: {a: {k: v for k, v in f['skalar'][les][a].items()} for a in f['skalar'][les]} for les in LESARTEN}
        zeilen.append(z)
    hf = json.load(open(haeuf_pfad))['ergebnis'] if haeuf_pfad and os.path.exists(haeuf_pfad) else None
    if haeuf_pfad and os.path.exists(haeuf_pfad):
        ein[os.path.basename(haeuf_pfad)] = sha(haeuf_pfad)
    return {'eingaben_sha256': ein, 'urteile': U, 'zusammenfassung': zusammenfassung(F), 'zeilen': zeilen,
            'haeufigkeit': hf}


def zusammenfassung(F):
    """Median, Minimum, Maximum je Art, Form, Lesart (Geometrie) bzw. je Art, Lesart, Amplitude (Skalar); beschreibend."""
    ok = [f for f in F if f.get('gleiche_endzerlegung')]
    Z = {'geometrie': [], 'skalar': [], 'zuege': []}

    def mmm(row, k, v):
        row[k + '_median'] = float(np.median(v))
        row[k + '_min'] = float(np.min(v))
        row[k + '_max'] = float(np.max(v))
    for art in ARTEN:
        fa = [f for f in ok if f['art'] == art]
        for form in FORMEN:
            for les in LESARTEN:
                g = [f['formen'][form][les] for f in fa if les in f['formen'].get(form, {})]
                if not g:
                    continue
                row = {'art': art, 'form': form, 'lesart': les, 'n': len(g)}
                for k in ('d_q_rel', 'd_p_rel', 'd_H_geo_rel', 'tu_XY_q_rel', 'tu_XY_p_rel', 'tu_YX_q_rel', 'tu_YX_p_rel',
                          'zwangsrest_XY_summe', 'zwangsrest_YX_summe'):
                    mmm(row, k, [x[k] for x in g])
                Z['geometrie'].append(row)
        for les in LESARTEN:
            for amp in A_PHI[1:]:
                s = [f['skalar'][les]['%g' % amp] for f in fa]
                if not s:
                    continue
                row = {'art': art, 'lesart': les, 'amp': amp, 'n': len(s)}
                for k in ('d_phi_rel', 'd_pi_rel', 'd_phi_abs', 'd_pi_abs', 'tu_XY_phi_rel', 'tu_XY_pi_rel', 'tu_YX_phi_rel',
                          'tu_YX_pi_rel'):
                    mmm(row, k, [x[k] for x in s])
                row['d_H_phi_rel_max'] = float(max(abs(x['H_XY'] - x['H_YX']) / abs(x['H_XY']) if x['H_XY'] else 0.0
                                                   for x in s))
                Z['skalar'].append(row)
        fa_all = [f for f in F if f['art'] == art]
        Z['zuege'].append({'art': art, 'n': len(fa_all), 'gleiche_endzerlegung': int(sum(1 for f in fa_all
                                                                                         if f.get('gleiche_endzerlegung'))),
                           'status': dict(Counter('%s/%s' % (f.get('status_XY'), f.get('status_YX')) for f in fa_all)),
                           'zugzahl_XY_YX': dict(Counter('%d/%d' % (len(f.get('zuege_XY', [])), len(f.get('zuege_YX', [])))
                                                         for f in fa_all)),
                           'typen_X_Y': dict(Counter('%s/%s' % (f['verschiebung']['typ_X'], f['verschiebung']['typ_Y'])
                                                     for f in fa_all)),
                           'verschiebung_rel_median': float(np.median([f['verschiebung']['norm_rel'] for f in fa_all]))
                           if fa_all else None})
    return Z


def g3(x):
    if x is None:
        return '-'
    if isinstance(x, str):
        return x
    if x == 0:
        return '0'
    return '%.3g' % x


def tabellen(aw_pfad, out_md):
    """Markdown aus auswertung.json (nur Darstellung)."""
    d = json.load(open(aw_pfad))['ergebnis']
    L = ['# UEBERGABE-KONFLUENZ-1: Tabellen aus %s (synthetisch, keine Messdaten)' % os.path.basename(aw_pfad), '']
    L += ['## Urteile (mechanisch, PLAN 7)', '', '| Nr | nach Plan | nach Kartenwortlaut | Kennzahlen |', '|---|---|---|---|']
    for k, u in d['urteile'].items():
        kz = '; '.join('%s = %s' % (a, g3(b) if not isinstance(b, (list, dict, bool)) else json.dumps(b))
                       for a, b in u.items() if a not in ('plan', 'wortlaut'))
        L.append('| %s | %s | %s | %s |' % (k, u['plan'], u['wortlaut'], kz))
    Z = d['zusammenfassung']
    L += ['', '## Zuege und Kombinatorik je Art', '', '| Art | Faelle | gleiche Endzerlegung | Status XY/YX | Zugzahl XY/YX | Typ X/Y | Verschiebung / l (Median) |',
          '|---|---|---|---|---|---|---|']
    for z in Z['zuege']:
        L.append('| %s | %d | %d | %s | %s | %s | %s |' % (z['art'], z['n'], z['gleiche_endzerlegung'], json.dumps(z['status']),
                                                           json.dumps(z['zugzahl_XY_YX']), json.dumps(z['typen_X_Y']),
                                                           g3(z['verschiebung_rel_median'])))
    L += ['', '## Geometrie: Delta je Sektor (relativ), Median [Min, Max] ueber Faelle', '',
          '| Art | Form | Lesart | n | Delta_q | Delta_p | Delta_H_geo | Zeitumkehr q (XY) | Zeitumkehr p (XY) | Zwangsrest XY (Summe) |',
          '|---|---|---|---|---|---|---|---|---|---|']
    for r in Z['geometrie']:
        def c(k):
            return '%s [%s, %s]' % (g3(r[k + '_median']), g3(r[k + '_min']), g3(r[k + '_max']))
        L.append('| %s | %s | %s | %d | %s | %s | %s | %s | %s | %s |' % (r['art'], r['form'], r['lesart'], r['n'], c('d_q_rel'),
                                                                        c('d_p_rel'), c('d_H_geo_rel'), c('tu_XY_q_rel'),
                                                                        c('tu_XY_p_rel'), c('zwangsrest_XY_summe')))
    L += ['', '## Skalar: Delta je Sektor, Median [Min, Max] ueber Faelle', '',
          '| Art | Lesart | Amplitude | n | Delta_phi rel | Delta_pi rel | Delta_phi abs | Delta_pi abs | Zeitumkehr phi / pi (XY, max) | Delta_H_phi (max) |',
          '|---|---|---|---|---|---|---|---|---|---|']
    for r in Z['skalar']:
        def c(k):
            return '%s [%s, %s]' % (g3(r[k + '_median']), g3(r[k + '_min']), g3(r[k + '_max']))
        L.append('| %s | %s | %s | %d | %s | %s | %s | %s | %s / %s | %s |' % (
            r['art'], r['lesart'], g3(r['amp']), r['n'], c('d_phi_rel'), c('d_pi_rel'), c('d_phi_abs'), c('d_pi_abs'),
            g3(r['tu_XY_phi_rel_max']), g3(r['tu_XY_pi_rel_max']), g3(r['d_H_phi_rel_max'])))
    L += ['', '## Faelle (Lesart R und P, Formen A1 / A2; Skalar-Amplitude 1e-3)', '',
          '| Saat | Art | X / Y | Typ X/Y | Zuege XY | Zuege YX | gleich | A1 R: Dq / Dp | A1 P: Dq / Dp | A2 R: Dq / Dp | A2 P: Dq / Dp | A2L startbar (neg.) | Skalar R / P: max(Dphi, Dpi) |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for z in d['zeilen']:
        def gp(form, les):
            q = z.get(form, {}).get(les)
            return '%s / %s' % (g3(q['d_q_rel']), g3(q['d_p_rel'])) if q else '-'
        sk = z.get('skalar')
        skt = '-'
        if sk:
            skt = ' / '.join(g3(max(sk[les]['0.001']['d_phi_rel'], sk[les]['0.001']['d_pi_rel'])) for les in LESARTEN)
        a2l = z.get('A2L', {})
        L.append('| %d | %s | %d / %d | %s/%s | %s | %s | %s | %s | %s | %s | %s | %s (%s) | %s |' % (
            z['saat'], z['art'], z['X'], z['Y'], z['typ_X'], z['typ_Y'], '-'.join(map(str, z['zuege_XY'])),
            '-'.join(map(str, z['zuege_YX'])), z['gleich'], gp('A1', 'R'), gp('A1', 'P'), gp('A2', 'R'), gp('A2', 'P'),
            a2l.get('startbar'), a2l.get('n_A_neg'), skt))
    if d.get('haeufigkeit'):
        L += ['', '## Haeufigkeit doppelter Ereignisse in TAKT-DYNAMIK-1 (A = 1e-3, Arm b, Lesart R; beschreibend)', '',
              '| Saat | h | Schritte | Ereignisse | Zuege | Schritte mit Ereignis | Schritte mit >= 2 Ereignissen | Anteil (alle Schritte) | Anteil (Schritte mit Ereignis) | Schritte mit >= 2 Zuegen | Zuege mit danach verletzter Flaeche |',
              '|---|---|---|---|---|---|---|---|---|---|---|']
        for h in d['haeufigkeit']:
            if 'fehlt' in h:
                L.append('| %d | %s | fehlt | | | | | | | | |' % (h['saat'], h['h']))
                continue
            L.append('| %d | %s | %d | %d | %d | %d | %d | %s | %s | %d | %d |' % (
                h['saat'], h['h'], h['n_schritte_gelaufen'], h['n_ereignisse'], h['n_zuege'], h['schritte_mit_ereignis'],
                h['schritte_ge2_ereignisse'], g3(h['anteil_ge2_ereignisse']), g3(h['anteil_ge2_unter_schritten_mit_ereignis']),
                h['schritte_ge2_zuege'], h['nach_zug_verletzt_ge1']))
    with open(out_md + '.tmp', 'w') as fh:
        fh.write('\n'.join(L) + '\n')
    os.replace(out_md + '.tmp', out_md)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf', 'haeufigkeit', 'auswertung', 'tabellen'])
    ap.add_argument('--saat', type=int, default=1)
    ap.add_argument('--ordner', default='lauf')
    ap.add_argument('--haeufigkeit', default=None)
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--faelle', type=int, default=None, help='nur Rauchtest: Faelle je Art')
    ap.add_argument('--out', required=True)
    ap.add_argument('--aw', default=None, help='tabellen: Pfad zu auswertung.json')
    a = ap.parse_args()
    t0 = time.time()
    me = os.path.abspath(__file__)
    if a.modus == 'tabellen':
        tabellen(a.aw, a.out)
        print('fertig tabellen', flush=True)
        return
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'argv': sys.argv, 'skript_sha256': sha(me),
            'module_sha256': {m.__name__: sha(os.path.abspath(m.__file__)) for m in (tg, uk, tu, td, hm_td)},
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'lauf':
        erg = lauf(a)
    elif a.modus == 'haeufigkeit':
        erg = haeufigkeit(a.ordner)
    else:
        erg = auswertung(a.ordner, a.haeufigkeit)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        res = {'info': info, 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'],
               'schluessel': tg.nur_schluessel(erg),
               'auswahl_angenommen': {k: v['angenommen'] for k, v in erg.get('auswahl', {}).items()},
               'auswahl_t_s': {k: v['t_s'] for k, v in erg.get('auswahl', {}).items()},
               'fall_t_s': [f.get('t_gesamt_s', f.get('t_kombinatorik_s')) for f in erg.get('faelle', [])],
               'wand_s': erg.get('wand_s')}
    schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
