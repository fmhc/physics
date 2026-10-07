#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GRUND-1 (Runde 44, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage: Wie sieht die Menge mit TT-Spanne < 1e-4 in der symmetrischen Ebene (J_kegel, J_sechs) aus, und welche Spanne
haben die natuerlichen Massenregeln N1 bis N6? Paarung A1R1, Regelgewicht g = 1 (wie TT-ISO-1), Netz V
(Hauptergebnis), S beschreibend.
tti.py (TT-ISO-1), ew.py, nachtrag_kinetik.py, tp.py werden unveraendert importiert.
Symmetrische Ebene (Fd-3m): finn_auf = finn_ab = 1, kegel_T1 = kegel_T2 = 10^yK, sechs_T1 = sechs_T2 = 10^yS
(S: achse = 10^yS). J gewichtet den Hamilton-Term (inverse Masse), J = m_Finn / m_t.
Modi: kontrolle, karte, profil, regeln, best, urteil, bild.
"""
import argparse, json, sys, os, time, hashlib, platform, resource, itertools
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402
import ew  # noqa: E402
import nachtrag_kinetik as nk  # noqa: E402
import tti  # noqa: E402

PAARUNG = 'A1R1'
SCHWELLE = 1e-4
# Regeln (PLAN.md Abschnitt 2), (J_kegel, J_sechs bzw. J_achse), J = m_Finn / m_t, exakte Brueche
REGELN = {
    'V': {'N1': (1.0, 1.0), 'N2': (4 / 5, 4 / 3), 'N3': (5 / 4, 3 / 4), 'N4': (16 / 25, 16 / 9), 'N5': (4 / 3, 2.0),
          'N6': (64 / 95, 64 / 49)},
    'S': {'N1': (1.0, 1.0), 'N2': (4 / 5, 2 / 3), 'N3': (5 / 4, 3 / 2), 'N4': (16 / 25, 4 / 9), 'N5': (4 / 3, 2.0),
          'N6': (64 / 95, 1 / 2)},
}
TTISO_EXAKT = (-1.0453267293049897, -0.0010098244011669793)   # TT-ISO-1 lauf-69/verf-V-A1R1.json tb1_symm_best
TTISO_GERUNDET = (float(np.log10(0.090)), 0.0)                  # Kartenwortlaut (0,090; 1,00)
POTENZ_V = (float(np.log10(4 / 5)), float(np.log10(4 / 3)))      # m ~ V^p: y = p * POTENZ_V (beschreibend)
T0 = time.time()


def fmt(v, n=6):
    v = float(v)
    return float('%.*g' % (n, v)) if np.isfinite(v) else None


def lade(pfad):
    with open(pfad) as fh:
        d = json.load(fh)
    return d['ergebnis']


class Ebene:
    def __init__(self, f, richt=None, epsl=tti.EPS):
        self.f = f
        self.netz = tti.Netz(f)
        self.richt = richt if richt is not None else tti.richtungen13()
        kp, ee, nn = tti.kpunkte(self.richt, epsl)
        self.ee = ee
        self.pr = tti.prep(self.netz, tti.basis(self.netz, kp), tti.g_eins(self.netz))
        self.n_prep_none = int(sum(p is None for p in self.pr))

    def J(self, Y):
        Y = np.atleast_2d(np.asarray(Y, float))
        X = np.array([tti.sym_J(self.netz, y) for y in Y])
        return self.netz.J_aus_log(X)

    def werte(self, Y):
        w, neg, lu, ok = tti.auswerten(self.pr, self.ee, PAARUNG, self.J(Y))
        return tti.spanne(w), w, neg, lu, ok

    def f_plan(self, y):
        sp, w, neg, lu, ok = self.werte([y])
        return float(sp[0]) if (ok[0] and neg[0] == 0 and np.isfinite(sp[0])) else 1e3

    def f_wort(self, y):
        sp, w, neg, lu, ok = self.werte([y])
        return float(sp[0]) if np.isfinite(sp[0]) else 1e3

    def punkt(self, y):
        sp, w, neg, lu, ok = self.werte([y])
        return {'y': [float(y[0]), float(y[1])], 'J_kegel': float(10 ** y[0]), 'J_sechs': float(10 ** y[1]),
                'spanne': float(sp[0]), 'ok': bool(ok[0]), 'neg_26': int(neg[0]), 'luecke': float(lu[0]),
                'plan_gueltig': bool(ok[0] and neg[0] == 0),
                'w_min': float(np.nanmin(w[0])), 'w_max': float(np.nanmax(w[0]))}


# ------------------------------------------------------------------------------------------------ Geometrie (Regeln)
def geometrie(f):
    """Je Tetraederart: Volumen (x768), Zahl der Ecken auf Finns Netz (Untergitter s < 4), polares Traegheitsmoment
    int |x - x_s|^2 dV = (V/20) sum_i |w_i|^2 (gleiche Dichte, x 8^5), Haupttraegheitsmomente."""
    mod = ew.baue(f)
    arten = {}
    for z in mod['zellen']:
        if not z['kin']:
            continue
        X = np.array(z['X8'], float) / 8.0
        w = X - X.mean(0)
        vol = float(z['vol'])
        polar = vol / 20.0 * float((w ** 2).sum())
        C = vol / 20.0 * (w.T @ w)
        Iten = polar * np.eye(3) - C
        nP = int(sum(1 for (s, n) in z['ids'] if s < 4))
        a = arten.setdefault(z['art'], {'n': 0, 'vol768': [], 'nP': [], 'polar8': [], 'I_haupt8': []})
        a['n'] += 1
        a['vol768'].append(vol * 768)
        a['nP'].append(nP)
        a['polar8'].append(polar * 8 ** 5)
        a['I_haupt8'].append(sorted((np.linalg.eigvalsh(Iten) * 8 ** 5).tolist()))
    zus = {}
    spreiz = 0.0
    for name, a in arten.items():
        zus[name] = {'n': a['n'], 'vol768': [min(a['vol768']), max(a['vol768'])], 'nP': [min(a['nP']), max(a['nP'])],
                     'polar8': [min(a['polar8']), max(a['polar8'])], 'I_haupt8_erste': a['I_haupt8'][0]}
        spreiz = max(spreiz, max(a['vol768']) - min(a['vol768']), max(a['polar8']) - min(a['polar8']),
                     max(a['nP']) - min(a['nP']))
    zweit = 'sechs_T1' if f == 'V' else 'achse'

    def m(art, regel):
        a = zus[art]
        return {'N1': 1.0, 'N2': a['vol768'][0], 'N3': 1.0 / a['vol768'][0], 'N4': a['vol768'][0] ** 2,
                'N5': float(a['nP'][0]), 'N6': a['polar8'][0]}[regel]
    J_geo = {r: [m('finn_auf', r) / m('kegel_T1', r), m('finn_auf', r) / m(zweit, r)] for r in REGELN[f]}
    abw = max(abs(J_geo[r][i] - REGELN[f][r][i]) for r in REGELN[f] for i in (0, 1))
    gleich_T = {}
    for p, q in (('finn_auf', 'finn_ab'), ('kegel_T1', 'kegel_T2'), ('sechs_T1', 'sechs_T2')):
        if p in zus and q in zus:
            gleich_T[p + '=' + q] = bool(zus[p]['vol768'] == zus[q]['vol768'] and zus[p]['nP'] == zus[q]['nP']
                                         and abs(zus[p]['polar8'][0] - zus[q]['polar8'][0]) < 1e-12)
    return {'arten': zus, 'spreizung_innerhalb_art_max': spreiz, 'J_aus_geometrie': J_geo,
            'abw_zu_plan_max': abw, 'T1_gleich_T2': gleich_T}


# ------------------------------------------------------------------------------------------------ Masse gegen Steifigkeit
def zerlegung(eb, y, richt):
    """Bei |k| = 1e-3: weicher 2D-Raum von B_red (zwei kleinste Eigenwerte lam), metrischer TT-Gehalt H_TT der
    Eigenvektoren (ew.tensor_fit), Gram G. kappa = Eig(G^-1 Lam) (Steifigkeit je |H_TT|^2), mu = Eig(G^-1 Ms) mit
    Ms = U2^+ A_red^-1 U2 (Masse je |H_TT|^2), w2 = Eig(Ms^-1 Lam) (gegen Z-Verfahren)."""
    netz = eb.netz
    J = eb.J([y])[0]
    gk = tti.g_eins(netz)
    wz, negz, luz, okz, nnz, eez = tti.w2_klein(netz, gk, PAARUNG, J, richt, epsl=(1e-3,))
    zeilen = []
    kap_all, mu_all, w_all, w_z = [], [], [], []
    for j, (nm, d) in enumerate(richt):
        kk = 1e-3 * d
        S, Ar, Br, M = tti.red_k(netz, kk, gk, PAARUNG, J)
        Br = 0.5 * (Br + np.conj(Br.T))
        lam, U = np.linalg.eigh(Br)
        U2 = U[:, :2]
        Lam = np.diag(lam[:2]) / 1e-6
        n = d / np.linalg.norm(d)
        P = np.eye(3) - np.outer(n, n)
        Hs, rests, ttf = [], [], []
        for i in range(2):
            H, rest = ew.tensor_fit(netz.mod, S @ U2[:, i], kk, M)
            HT = P @ H @ P
            HTT = HT - 0.5 * P * np.trace(HT)
            Hs.append(HTT)
            rests.append(float(rest))
            ttf.append(float(np.sum(np.abs(HTT) ** 2) / max(float(np.sum(np.abs(H) ** 2)), 1e-300)))
        G = np.array([[np.sum(np.conj(Hs[a]) * Hs[b]) for b in range(2)] for a in range(2)])
        Ms = np.conj(U2.T) @ np.linalg.inv(Ar) @ U2
        kap = np.sort(np.linalg.eigvals(np.linalg.solve(G, Lam)).real)
        mu = np.sort(np.linalg.eigvals(np.linalg.solve(G, Ms)).real)
        w2 = np.sort(np.linalg.eigvals(np.linalg.solve(Ms, Lam)).real)
        kap_all += kap.tolist()
        mu_all += mu.tolist()
        w_all += w2.tolist()
        w_z += np.sort(wz[j]).tolist()
        zeilen.append({'richtung': nm, 'lam_ueber_k2': (lam[:2] / 1e-6).tolist(), 'lam3': float(lam[2]),
                       'kappa': kap.tolist(), 'mu': mu.tolist(), 'w2_weich': w2.tolist(), 'w2_Z': np.sort(wz[j]).tolist(),
                       'fit_rest': rests, 'tt_anteil_H': ttf})

    def sp(x):
        x = np.asarray(x, float)
        return float(x.max() / x.min() - 1)
    return {'y': [float(y[0]), float(y[1])], 'zeilen': zeilen, 'spanne_kappa': sp(kap_all), 'spanne_mu': sp(mu_all),
            'spanne_w2_weich': sp(w_all), 'spanne_w2_Z': sp(w_z),
            'abw_weich_Z_rel_max': float(np.max(np.abs(np.array(w_all) - np.array(w_z)) / np.abs(np.array(w_z)))),
            'kappa_min_max': [float(min(kap_all)), float(max(kap_all))], 'mu_min_max': [float(min(mu_all)), float(max(mu_all))]}


def lauf_kontrolle():
    out = {'geometrie': {f: geometrie(f) for f in ('V', 'S')}}
    r13 = tti.richtungen13()
    eb = Ebene('V')
    out['n_prep_none_V'] = eb.n_prep_none
    out['N1_V'] = eb.punkt((0.0, 0.0))
    out['ttiso_exakt_V'] = eb.punkt(TTISO_EXAKT)
    out['ttiso_gerundet_V'] = eb.punkt(TTISO_GERUNDET)
    out['zerlegung_V'] = {'N1': zerlegung(eb, (0.0, 0.0), r13), 'ttiso_exakt': zerlegung(eb, TTISO_EXAKT, r13)}
    ebS = Ebene('S')
    out['N1_S'] = ebS.punkt((0.0, 0.0))
    out['zerlegung_S'] = {'N1': zerlegung(ebS, (0.0, 0.0), r13)}
    return out


# ------------------------------------------------------------------------------------------------ Karte
def komponenten(B):
    B = np.asarray(B, bool)
    lab = np.zeros(B.shape, int)
    n = 0
    groessen = []
    for i0, j0 in zip(*np.nonzero(B)):
        if lab[i0, j0]:
            continue
        n += 1
        stapel = [(i0, j0)]
        lab[i0, j0] = n
        g = 0
        while stapel:
            i, j = stapel.pop()
            g += 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + di, j + dj
                if 0 <= a < B.shape[0] and 0 <= b < B.shape[1] and B[a, b] and not lab[a, b]:
                    lab[a, b] = n
                    stapel.append((a, b))
        groessen.append(int(g))
    return {'anzahl': int(n), 'groessen': sorted(groessen, reverse=True)[:20]}


def lauf_karte(f, npkt, gitter_alt=None):
    eb = Ebene(f)
    ach = np.linspace(-2, 2, npkt)
    YK, YS = np.meshgrid(ach, ach, indexing='ij')            # [i, j] = (yK = ach[i], yS = ach[j])
    Y = np.stack([YK.ravel(), YS.ravel()], -1)
    t = time.time()
    sp, w, neg, lu, ok = eb.werte(Y)
    t_ausw = time.time() - t
    g = ok & (neg == 0)
    spP = np.where(g & np.isfinite(sp), sp, np.inf).reshape(npkt, npkt)
    spW = np.where(np.isfinite(sp), sp, np.inf).reshape(npkt, npkt)
    wmin = np.nanmin(w, axis=(1, 2)).reshape(npkt, npkt)
    out = {'netz': f, 'npkt': npkt, 'achse': ach.tolist(), 'schritt': float(ach[1] - ach[0]), 't_auswertung_s': t_ausw,
           'n_prep_none': eb.n_prep_none, 'n_gueltig': int(g.sum()), 'n_punkte': int(len(Y))}
    for tag, A in (('plan', spP), ('wort', spW)):
        out['n_unter_' + tag] = {('%g' % s): int((A < s).sum()) for s in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6)}
        B = A < SCHWELLE
        blk = np.ones((npkt - 2, npkt - 2), bool)
        for di in range(3):
            for dj in range(3):
                blk &= B[di:npkt - 2 + di, dj:npkt - 2 + dj]
        out['block3_' + tag] = int(blk.sum())
        out['komponenten_' + tag] = komponenten(B)
        i, j = np.unravel_index(int(np.argmin(A)), A.shape)
        out['min_' + tag] = {'y': [float(ach[i]), float(ach[j])], 'spanne': float(A[i, j])}
    out['spanne_plan'] = [[fmt(v) for v in row] for row in spP]
    out['spanne_wort'] = [[fmt(v) for v in row] for row in spW]
    out['w_min'] = [[fmt(v, 5) for v in row] for row in wmin]
    if f == 'V':
        p = np.arange(-16.0, 16.0 + 1e-9, 0.05)
        YP = p[:, None] * np.array(POTENZ_V)[None, :]
        drin = np.all(np.abs(YP) <= 2.0 + 1e-12, axis=1)
        p, YP = p[drin], YP[drin]
        sp2, w2, neg2, lu2, ok2 = eb.werte(YP)
        sp2P = np.where(ok2 & (neg2 == 0) & np.isfinite(sp2), sp2, np.inf)
        k = int(np.argmin(sp2P))
        out['potenzlinie'] = {'p': [fmt(x, 4) for x in p], 'spanne_plan': [fmt(x) for x in sp2P],
                              'min': {'p': float(p[k]), 'y': YP[k].tolist(), 'spanne': float(sp2P[k])}}
    if gitter_alt:
        with open(gitter_alt) as fh:
            gi = json.load(fh)['ergebnis']
        ach9 = np.array(gi['achse_log10'])
        X = np.array(list(itertools.product(ach9, repeat=len(gi['frei_arten']))))
        alt = gi['spanne_plan_alle']
        h = ach[1] - ach[0]
        dmax, nvgl, nversch, nfehl = 0.0, 0, 0, 0
        for idx in range(len(X)):
            x = X[idx]
            if x[0] == 0 and x[1] == x[2] and x[3] == x[4]:
                i = int(round((x[1] + 2) / h))
                j = int(round((x[3] + 2) / h))
                if abs(ach[i] - x[1]) > 1e-9 or abs(ach[j] - x[3]) > 1e-9:
                    nfehl += 1
                    continue
                neu = spP[i, j]
                a = alt[idx]
                if (a is None) != (not np.isfinite(neu)):
                    nversch += 1
                elif a is not None:
                    dmax = max(dmax, abs(a - float(neu)))
                    nvgl += 1
        out['tti_gitter_vergleich'] = {'frei_arten': gi['frei_arten'], 'n_vergleich': nvgl,
                                       'n_gueltigkeit_verschieden': nversch, 'n_nicht_im_raster': nfehl,
                                       'abw_abs_max': dmax}
    return out


# ------------------------------------------------------------------------------------------------ Profile (Talboden)
def golden(f, a, b, tol=1e-7, maxit=80):
    gr = (np.sqrt(5.0) - 1.0) / 2.0
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    fc, fd = f(c), f(d)
    nf = 2
    best = min((fc, c), (fd, d))
    it = 0
    while abs(b - a) > tol and it < maxit:
        if fc <= fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = f(c)
            nf += 1
            best = min(best, (fc, c))
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = f(d)
            nf += 1
            best = min(best, (fd, d))
        it += 1
    return float(best[1]), float(best[0]), nf


def lokale_minima(s, anzahl=3):
    n = len(s)
    idx = [i for i in range(n) if np.isfinite(s[i]) and (i == 0 or s[i] <= s[i - 1]) and (i == n - 1 or s[i] <= s[i + 1])]
    return sorted(idx, key=lambda i: s[i])[:anzahl]


def lauf_profil(f, achse, nprof, nscan, tol, bis_s):
    """achse 'S': Profil ueber yS (v), Minimum ueber yK (u); achse 'K': Profil ueber yK (v), Minimum ueber yS (u)."""
    eb = Ebene(f)
    pv = np.linspace(-2, 2, nprof)
    us = np.linspace(-2, 2, nscan)
    zeilen = []
    abbruch = False
    for v in pv:
        if time.time() > T0 + bis_s:
            abbruch = True
            break
        t = time.time()
        if achse == 'S':
            mk = (lambda u, v=v: (float(u), float(v)))
        else:
            mk = (lambda u, v=v: (float(v), float(u)))
        Y = np.array([mk(u) for u in us])
        sp, w, neg, lu, ok = eb.werte(Y)
        g = ok & (neg == 0)
        spP = np.where(g & np.isfinite(sp), sp, np.inf)
        spW = np.where(np.isfinite(sp), sp, np.inf)
        z = {'v': float(v), 'n_scan_gueltig': int(g.sum()), 'scan_min_plan': fmt(spP.min()),
             'scan_min_wort': fmt(spW.min())}
        for tag, s_arr, fobj in (('plan', spP, eb.f_plan), ('wort', spW, eb.f_wort)):
            if tag == 'wort' and not (spW.min() < spP.min()):
                z['min_wort'] = None                            # Wortlaut = Plan an dieser Zeile
                continue
            minima = []
            for i in lokale_minima(s_arr):
                a, b = us[max(i - 1, 0)], us[min(i + 1, nscan - 1)]
                u, s, nf = golden(lambda uu: fobj(mk(uu)), a, b, tol)
                if s_arr[i] < s:
                    u, s = float(us[i]), float(s_arr[i])
                minima.append({'u': float(u), 'spanne': float(s), 'nf': int(nf)})
            z['minima_' + tag] = minima
            z['min_' + tag] = min(minima, key=lambda m: m['spanne']) if minima else None
        z['t_s'] = time.time() - t
        zeilen.append(z)
    return {'netz': f, 'achse': achse, 'nprof': nprof, 'nscan': nscan, 'tol': tol, 'abbruch': abbruch,
            'n_zeilen': len(zeilen), 'zeilen': zeilen}


# ------------------------------------------------------------------------------------------------ Regeln
def lauf_regeln(Lst):
    out = {}
    for f in ('V', 'S'):
        eb = Ebene(f)
        eb23 = Ebene(f, richt=ew.richtungen())
        gk = tti.g_eins(eb.netz)
        out[f] = {}
        for name, (jk, js) in REGELN[f].items():
            y = (float(np.log10(jk)), float(np.log10(js)))
            d = eb.punkt(y)
            sp23, w23, neg23, lu23, ok23 = eb23.werte([y])
            d['spanne_23ew'] = float(sp23[0])
            d['J_regel'] = [jk, js]
            d['stabil_L8'] = tti.stabil(eb.netz, gk, PAARUNG, eb.J([y])[0], L=Lst)
            d['stabil'] = bool(d['plan_gueltig'] and d['stabil_L8']['k_mit_negativ'] == 0
                               and d['stabil_L8']['k_mit_komplex'] == 0)
            out[f][name] = d
    return out


# ------------------------------------------------------------------------------------------------ bester Punkt
def lauf_best(f, profil_dateien, Lst):
    eb = Ebene(f)
    gk = tti.g_eins(eb.netz)
    kand = [{'quelle': 'ttiso_exakt', 'y': [float(TTISO_EXAKT[0]), float(TTISO_EXAKT[1])],
             'spanne': eb.f_plan(TTISO_EXAKT)}]
    for pfad in profil_dateien:
        P = lade(pfad)
        for z in P['zeilen']:
            for m in z.get('minima_plan') or []:
                y = (m['u'], z['v']) if P['achse'] == 'S' else (z['v'], m['u'])
                kand.append({'quelle': 'profil_' + P['achse'], 'y': [float(y[0]), float(y[1])], 'spanne': m['spanne']})
    kand.sort(key=lambda k: k['spanne'])
    b0 = kand[0]
    y1, v1, n1 = tti.nelder_mead(eb.f_plan, np.array(b0['y']), schritt=0.01, maxit=150)
    y2, v2, n2 = tti.nelder_mead(eb.f_plan, y1, schritt=0.001, maxit=150)
    best_y = np.array(y2) if v2 < b0['spanne'] else np.array(b0['y'])
    out = {'netz': f, 'kandidat_bester': b0, 'nm': {'y': [float(x) for x in y2], 'spanne': float(v2), 'nf': int(n1 + n2)},
           'n_kandidaten': len(kand)}
    out['best'] = eb.punkt(best_y)
    out['best']['stabil_L8'] = tti.stabil(eb.netz, gk, PAARUNG, eb.J([best_y])[0], L=Lst)
    out['best']['stabil'] = bool(out['best']['plan_gueltig'] and out['best']['stabil_L8']['k_mit_negativ'] == 0
                                 and out['best']['stabil_L8']['k_mit_komplex'] == 0)
    eb23 = Ebene(f, richt=ew.richtungen())
    sp23, w23, neg23, lu23, ok23 = eb23.werte([best_y])
    out['best']['spanne_23ew'] = float(sp23[0])
    unter = [k for k in kand if k['spanne'] < SCHWELLE and k['quelle'].startswith('profil')]
    unter.sort(key=lambda k: (k['y'][0], k['y'][1]))
    out['n_unter_schwelle'] = len(unter)
    pick = [unter[int(round(i))] for i in np.linspace(0, len(unter) - 1, min(5, len(unter)))] if unter else []
    out['entlang'] = []
    for k in pick:
        d = eb.punkt(k['y'])
        d['stabil_L8'] = tti.stabil(eb.netz, gk, PAARUNG, eb.J([k['y']])[0], L=Lst)
        d['stabil'] = bool(d['plan_gueltig'] and d['stabil_L8']['k_mit_negativ'] == 0
                           and d['stabil_L8']['k_mit_komplex'] == 0)
        out['entlang'].append(d)
    out['regel_abstand'] = {}
    for name, (jk, js) in REGELN[f].items():
        yr = np.array([np.log10(jk), np.log10(js)])
        if unter:
            dd = [float(np.linalg.norm(np.array(k['y']) - yr)) for k in unter]
            i = int(np.argmin(dd))
            out['regel_abstand'][name] = {'abstand_dex': dd[i], 'naechster': unter[i]}
        else:
            out['regel_abstand'][name] = None
    return out


# ------------------------------------------------------------------------------------------------ Urteile (Plan Abschnitt 4)
def laeufe(werte, schritt):
    """werte: Liste (v, x oder None); zusammenhaengende Laeufe mit x < SCHWELLE."""
    alle, cur = [], []
    for v, x in werte:
        if x is not None and x < SCHWELLE:
            cur.append((v, x))
        else:
            if cur:
                alle.append(cur)
            cur = []
    if cur:
        alle.append(cur)
    return [{'von': l[0][0], 'bis': l[-1][0], 'n': len(l), 'ausdehnung_dex': (len(l) - 1) * schritt,
             'boden_min': min(x for _, x in l), 'boden_max': max(x for _, x in l)} for l in alle]


def lauf_urteil(kontrolle, karte, profile, regeln, best):
    K = lade(kontrolle)
    KA = lade(karte)
    R = lade(regeln)
    B = lade(best)
    PR = [lade(p) for p in profile]
    u = {}
    n1 = K['N1_V']['spanne']
    tex, tge = K['ttiso_exakt_V'], K['ttiso_gerundet_V']
    c1 = abs(n1 - 0.0634) <= 1e-3 * 0.0634
    c2p = bool(tex['plan_gueltig'] and tex['spanne'] <= 2e-5)
    c2w = bool(tge['spanne'] <= 2e-5)
    u['TG0'] = {'plan': 'eingetroffen' if (c1 and c2p) else 'verfehlt',
                'wortlaut': 'eingetroffen' if (c1 and c2w) else 'verfehlt',
                'N1_spanne': n1, 'N1_abw_rel': abs(n1 - 0.0634) / 0.0634, 'ttiso_exakt': tex['spanne'],
                'ttiso_exakt_gueltig': tex['plan_gueltig'], 'ttiso_gerundet': tge['spanne']}
    tg1 = {}
    for tag in ('plan', 'wort'):
        prof = []
        for P in PR:
            schritt = 4.0 / (P['nprof'] - 1)
            werte = []
            for z in P['zeilen']:
                x = z['min_plan']['spanne'] if z.get('min_plan') else None
                if tag == 'wort':
                    xw = z['min_wort']['spanne'] if z.get('min_wort') else None
                    x = min([q for q in (x, xw) if q is not None], default=None)
                werte.append((z['v'], x))
            prof.append({'achse': P['achse'], 'laeufe': laeufe(werte, schritt), 'abbruch': P['abbruch'],
                         'n_zeilen': P['n_zeilen'], 'nprof': P['nprof']})
        aus = [l['ausdehnung_dex'] for a in prof for l in a['laeufe']]
        R_max = max(aus) if aus else None
        gebiet = KA['block3_' + tag] > 0
        nichtleer = bool(aus) or KA['n_unter_' + tag]['0.0001'] > 0 or tex['spanne'] < SCHWELLE
        unvoll = any(a['abbruch'] for a in prof)
        if gebiet:
            form, urt = 'Gebiet', 'verfehlt'
        elif R_max is not None and R_max >= 0.25 - 1e-9:
            form, urt = 'Kurve', 'eingetroffen'
        elif nichtleer and (R_max is None or R_max <= 0.05 + 1e-9) and not unvoll:
            form, urt = 'Punkt', 'verfehlt'
        else:
            form, urt = 'unklar', 'nicht entscheidbar'
        exakt = [l for a in prof for l in a['laeufe'] if l['ausdehnung_dex'] >= 0.25 - 1e-9 and l['boden_max'] < 1e-6]
        tg1[tag] = {'form': form, 'urteil': urt, 'R_max_dex': R_max, 'gebiet_block3': KA['block3_' + tag],
                    'nichtleer': nichtleer, 'profil_unvollstaendig': unvoll, 'profile': prof,
                    'n_laeufe_boden_unter_1e-6_ab_0_25dex': len(exakt)}
    u['TG1'] = {'plan': tg1['plan']['urteil'], 'wortlaut': tg1['wort']['urteil'], 'details': tg1}
    rows = R['V']
    nn = ('N2', 'N3', 'N4', 'N5', 'N6')
    unter_p = [n for n in nn if rows[n]['spanne'] < 1e-3 and rows[n]['plan_gueltig']]
    unter_w = [n for n in nn if rows[n]['spanne'] < 1e-3]
    u['TG2'] = {'plan': 'eingetroffen' if not unter_p else 'verfehlt',
                'wortlaut': 'eingetroffen' if not unter_w else 'verfehlt',
                'unter_0_1_prozent_plan': unter_p, 'unter_0_1_prozent_wort': unter_w,
                'kleinste': min((rows[n]['spanne'], n) for n in nn)}
    u['regeln_tabelle'] = {f: {n: {'J': d['J_regel'], 'spanne': d['spanne'], 'plan_gueltig': d['plan_gueltig'],
                                   'stabil': d['stabil'], 'k_neg': d['stabil_L8']['k_mit_negativ'],
                                   'k_kompl': d['stabil_L8']['k_mit_komplex'], 'w_min': d['w_min'], 'w_max': d['w_max'],
                                   'spanne_23ew': d['spanne_23ew']} for n, d in R[f].items()} for f in R}
    u['best'] = {'y': B['best']['y'], 'J_kegel': B['best']['J_kegel'], 'J_sechs': B['best']['J_sechs'],
                 'spanne': B['best']['spanne'], 'stabil': B['best']['stabil'], 'spanne_23ew': B['best']['spanne_23ew']}
    return u


# ------------------------------------------------------------------------------------------------ Bild
def lauf_bild(karte, profile, regeln, best, png, rauch):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    KA = lade(karte)
    ach = np.array(KA['achse'])
    sp = np.array([[np.nan if v is None else v for v in row] for row in KA['spanne_plan']], float)
    if rauch:
        sp = np.full_like(sp, 1e-2)
    L = np.log10(np.clip(sp, 1e-9, None))
    h = (ach[1] - ach[0]) / 2
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(16, 7), gridspec_kw={'width_ratios': [1.15, 1]})
    im = ax.imshow(L.T, origin='lower', extent=[ach[0] - h, ach[-1] + h, ach[0] - h, ach[-1] + h], cmap='viridis',
                   vmin=-7, vmax=-0.5, aspect='equal', interpolation='nearest')
    fig.colorbar(im, ax=ax, label='log10 TT-Spanne (max/min - 1), Karte %dx%d' % (len(ach), len(ach)))
    if not rauch:
        Lm = np.where(np.isfinite(L), L, 3.0)
        ax.contour(ach, ach, Lm.T, levels=[-4, -3, -2], colors=['white', 'orange', 'red'], linewidths=[1.2, 0.9, 0.9])
    for P0 in profile:
        P = lade(P0)
        xs, ys, vv, mm = [], [], [], []
        for z in P['zeilen']:
            m = z.get('min_plan')
            if not m:
                continue
            vv.append(z['v'])
            mm.append(1e-2 if rauch else m['spanne'])
            if m['spanne'] < SCHWELLE and not rauch:
                if P['achse'] == 'S':
                    xs.append(m['u'])
                    ys.append(z['v'])
                else:
                    xs.append(z['v'])
                    ys.append(m['u'])
        lab = 'log10 J_Sechseck' if P['achse'] == 'S' else 'log10 J_Kegel'
        ax.plot(xs, ys, '.', color='white' if P['achse'] == 'S' else 'cyan', ms=5,
                label='Talboden < 1e-4 (Profil ueber %s)' % lab)
        ax2.semilogy(vv, mm, '.-', label='min. Spanne quer zum Profil, Profil ueber %s' % lab)
    ax2.axhline(SCHWELLE, color='k', ls='--', lw=0.8, label='Schwelle 1e-4')
    ax2.axhline(1e-3, color='gray', ls=':', lw=0.8, label='0,1 %')
    R = lade(regeln)['V']
    for name, d in R.items():
        ax.plot(d['y'][0], d['y'][1], 'o', mfc='none', mec='red', ms=9, mew=1.5)
        ax.annotate(name, (d['y'][0], d['y'][1]), xytext=(6, 6), textcoords='offset points', color='red', fontsize=11)
    ax.plot(TTISO_EXAKT[0], TTISO_EXAKT[1], '*', color='magenta', ms=13, label='TT-ISO-1-Punkt (0,090; 1,00)')
    B = lade(best)
    by = B['best']['y']
    ax.plot(by[0], by[1], 'x', color='black', ms=11, mew=2, label='bester Punkt')
    p = np.linspace(-16, 16, 400)
    yy = p[:, None] * np.array(POTENZ_V)[None, :]
    dr = np.all(np.abs(yy) <= 2, axis=1)
    ax.plot(yy[dr, 0], yy[dr, 1], '--', color='lightgray', lw=1, label='Potenzgesetz m ~ V^p (beschreibend)')
    ax.set_xlim(-2.05, 2.05)
    ax.set_ylim(-2.05, 2.05)
    ax.set_xlabel('log10 J_Kegel (J = m_Finn / m_Kegel)')
    ax.set_ylabel('log10 J_Sechseck (J = m_Finn / m_Sechseck)')
    ax.legend(loc='lower left', fontsize=7.5, framealpha=0.85)
    ax2.set_xlabel('Profilkoordinate (dex)')
    ax2.set_ylabel('kleinste Spanne quer zum Profil (plan-gueltig)')
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3, which='both')
    fig.suptitle('TT-GRUND-1: TT-Spanne in der symmetrischen Ebene, Netz V, Paarung A1R1, g = 1 (synthetische Rechnung)')
    fig.tight_layout()
    fig.savefig(png, dpi=100)
    plt.close(fig)
    return {'png': png, 'png_sha256': sha(png)}


# ------------------------------------------------------------------------------------------------ Rahmen
def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def nur_schluessel(x, tiefe=0):
    if isinstance(x, dict):
        return {k: nur_schluessel(v, tiefe + 1) for k, v in x.items()} if tiefe < 2 else sorted(x.keys())
    return type(x).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['kontrolle', 'karte', 'profil', 'regeln', 'best', 'urteil', 'bild'])
    ap.add_argument('--netz', default='V', choices=['V', 'S'])
    ap.add_argument('--npkt', type=int, default=161)
    ap.add_argument('--achse', default='S', choices=['S', 'K'])
    ap.add_argument('--nprof', type=int, default=81)
    ap.add_argument('--nscan', type=int, default=161)
    ap.add_argument('--tol', type=float, default=1e-7)
    ap.add_argument('--bis', type=float, default=540.0)
    ap.add_argument('--Lst', type=int, default=8)
    ap.add_argument('--gitter_alt')
    ap.add_argument('--kontrolle')
    ap.add_argument('--karte')
    ap.add_argument('--profile', nargs='*', default=[])
    ap.add_argument('--regeln')
    ap.add_argument('--best')
    ap.add_argument('--png')
    ap.add_argument('--rauch', action='store_true', help='Ausgabe nur Schluessel und Laufzeiten; volle Daten in <out>.roh')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'tti_sha256': sha(os.path.abspath(tti.__file__)),
            'ew_sha256': sha(os.path.abspath(ew.__file__)), 'nk_sha256': sha(os.path.abspath(nk.__file__)),
            'tp_sha256': sha(os.path.abspath(tp.__file__))}
    eing = [x for x in [a.gitter_alt, a.kontrolle, a.karte, a.regeln, a.best] + list(a.profile) if x]
    info['eingaben_sha256'] = {x: sha(x) for x in eing}
    if a.modus == 'kontrolle':
        erg = lauf_kontrolle()
    elif a.modus == 'karte':
        erg = lauf_karte(a.netz, a.npkt, a.gitter_alt)
    elif a.modus == 'profil':
        erg = lauf_profil(a.netz, a.achse, a.nprof, a.nscan, a.tol, a.bis)
    elif a.modus == 'regeln':
        erg = lauf_regeln(a.Lst)
    elif a.modus == 'best':
        erg = lauf_best(a.netz, a.profile, a.Lst)
    elif a.modus == 'urteil':
        erg = lauf_urteil(a.kontrolle, a.karte, a.profile, a.regeln, a.best)
    else:
        erg = lauf_bild(a.karte, a.profile, a.regeln, a.best, a.png, a.rauch)
    res = {'info': info, 'ergebnis': erg}
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    dump = lambda o: o.item() if hasattr(o, 'item') else str(o)  # noqa: E731
    if a.rauch:
        with open(a.out + '.roh.tmp', 'w') as fh:
            json.dump(res, fh, indent=1, default=dump)
        os.replace(a.out + '.roh.tmp', a.out + '.roh')
        res = {'info': info, 'schluessel': nur_schluessel(erg), 'laufzeit_s': res['laufzeit_s'],
               'maxrss_MB': res['maxrss_MB'],
               't_zeilen_s': [z.get('t_s') for z in erg.get('zeilen', [])] if isinstance(erg, dict) else None,
               't': {k: v for k, v in erg.items() if k.startswith('t_')} if isinstance(erg, dict) else None,
               'n_punkte': erg.get('n_punkte') if isinstance(erg, dict) else None}
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=dump)
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, a.netz, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
