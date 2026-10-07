#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SPLITTER-FREI-1 (Runde 48, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage: Kommen die wachsenden Moden auf dem Glas N = 128 (A1RH, A2RH; Lund-Regge-Masse mit R1 = A2LR1) von fast
flachen Splitter-Tetraedern?
- Originalglas: tg.zufallsnetz(128, s) (TT-GLAS-1), Saaten 1 bis 4.
- Splitterarmes Glas: dieselben Punkte, kleine zufaellige Stoerung einzelner Ecken schlechter Tetraeder, angenommen nur,
  wenn das Formdefizit sinkt, bis kein Tetraeder unter der Formschranke q_s liegt. Delaunay bleibt die Zerlegungsregel
  (dieselbe periodische Zerlegung wie tg.zufallsnetz, Funktion triang).
- Formmass je Tetraeder: q = 27 V / (8 sqrt(3) R^3), V Volumen, R Umkugelradius (regulaer 1, flach -> 0).
Unveraendert importiert: tp, ew, tg, tti, hm (HODGE-MASSE-1), lrm (LUND-REGGE-MASSE-1) und deren Abhaengigkeiten.
Modi (nur ueber kleintest.sh auf der .69):
  rauch-form | rauch-bau | rauch-punkt | bau | hm | lr | aw
"""
import argparse, json, sys, os, time, hashlib, platform, resource, math
import numpy as np
import scipy
import scipy.linalg as sla
from scipy.spatial import Delaunay

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402
import ew  # noqa: E402
import tg  # noqa: E402
import tti  # noqa: E402
import hm  # noqa: E402
import lrm  # noqa: E402

N_GLAS = 128
SAATEN = (1, 2, 3, 4)
SAAT_SF = 9137                     # eigene Zufallsquelle der Stoerung (je Saat [SAAT_SF, N, s])
QNORM = 27.0 / (8.0 * math.sqrt(3.0))
ANTEIL_SCHLECHT = 0.05             # SF1: 5 % Tetraeder mit kleinstem q
KL_LR = (0.005, 0.2)               # LR-Satz: kl-Werte aus LUND-REGGE-MASSE-1 (Teilmenge), 13 Richtungen
RC_Q6 = 1.35                       # Nachbarschaftsradius fuer Q6 (Dichte 1)
NMAX_S = 7                         # Strukturfaktor: |n| <= 7 (q bis 2 pi 7 / L)
S_KRIST = 32.0                     # kristallin, wenn max S(q) >= N/4
Q6_KRIST = 0.25                    # kristallin, wenn Q6 global (r < RC_Q6) >= 0,25
herm = hm.herm


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def schreibe(pfad, res):
    def conv(o):
        if hasattr(o, 'tolist'):
            return o.tolist()
        if hasattr(o, 'item'):
            return o.item()
        return str(o)
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=conv)
    os.replace(pfad + '.tmp', pfad)


def lade(p):
    with open(p) as fh:
        return json.load(fh)


# ------------------------------------------------------------------------------------------------ Punkte, Zerlegung, Form
def punkte_original(N, saat):
    """Dieselben Punkte wie tg.zufallsnetz(N, saat)."""
    rng = np.random.default_rng([tg.SAAT_BASIS, int(N), int(saat)])
    L = float(N) ** (1.0 / 3.0)
    return L, rng.uniform(0.0, L, size=(N, 3))


def triang(pos, L, saum=tg.SAUM):
    """Periodische Delaunay-Zerlegung gegebener Punkte, Wortlaut von tg.zufallsnetz ab der Punktwahl."""
    offs = np.array([(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)], dtype=np.int64)
    Pl, Il, Ol = [], [], []
    for o in offs:
        Q = pos + o * L
        m = np.all((Q >= -saum) & (Q <= L + saum), axis=1)
        Pl.append(Q[m])
        Il.append(np.nonzero(m)[0])
        Ol.append(np.repeat(o[None, :], int(m.sum()), axis=0))
    P = np.concatenate(Pl)
    gidx = np.concatenate(Il)
    goff = np.concatenate(Ol)
    S = Delaunay(P).simplices
    X = P[S]
    cen = X.mean(axis=1)
    halte = np.all((cen >= 0.0) & (cen < L), axis=1)
    S, X = S[halte], X[halte]
    A = 2.0 * (X[:, 1:] - X[:, :1])
    b = (X[:, 1:] ** 2).sum(-1) - (X[:, :1] ** 2).sum(-1)
    C = np.linalg.solve(A, b[..., None])[..., 0]
    R = np.linalg.norm(C - X[:, 0], axis=1)
    verletzt = int(np.sum(np.any((C - R[:, None] < -saum) | (C + R[:, None] > L + saum), axis=1)))
    pr = {'saum': saum, 'umkugel_ausserhalb_saum': verletzt, 'R_umkugel_max': float(R.max()),
          'punkte_mit_kopien': int(len(P))}
    return np.eye(3) * L, pos, gidx[S], goff[S], pr


def tet_X(LV, pos, G, O):
    return pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)


def form(X):
    """q = 27 V / (8 sqrt3 R^3) je Tetraeder (X: T x 4 x 3); Rueckgabe q, V, R."""
    D = X[:, 1:] - X[:, :1]
    V = np.abs(np.linalg.det(D)) / 6.0
    cc = np.linalg.solve(2.0 * D, (D ** 2).sum(-1)[..., None])[..., 0]      # Umkugelmitte relativ zu X0
    R = np.linalg.norm(cc, axis=1)
    return QNORM * V / R ** 3, V, R


def form_statistik(q, V):
    qs = np.sort(q)
    T = len(q)
    nb = int(math.ceil(ANTEIL_SCHLECHT * T))
    return {'T': int(T), 'q_min': float(qs[0]), 'q_1proz': float(np.quantile(q, 0.01)), 'q_5proz': float(np.quantile(q, 0.05)),
            'q_10proz': float(np.quantile(q, 0.10)), 'q_median': float(np.median(q)), 'q_mittel': float(q.mean()),
            'q_schwelle_5proz_satz': float(qs[nb - 1]), 'n_5proz_satz': nb,
            'n_q_unter': {('%g' % s): int((q < s).sum()) for s in (0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3)},
            'vol_min_rel_mittel': float(V.min() / V.mean()), 'q_hist_0_1_20': np.histogram(q, bins=20, range=(0, 1))[0].tolist()}


def defizit(q, qs):
    return float(np.clip(qs - q, 0.0, None).sum())


def minbild(d, L):
    return d - L * np.round(d / L)


# ------------------------------------------------------------------------------------------------ Splitterarmes Glas
def bau_sf(N, saat, qs, zeit_max, r0, rmax, saum_bau=2.0, max_vers=10 ** 9, protokoll=200):
    """Stoerung einzelner Ecken schlechter Tetraeder (Wahl gewichtet mit dem Defizit qs - q), angenommen nur bei
    sinkendem Formdefizit F = Summe max(0, qs - q). Schrittweite r: Start r0, nach je 25 Fehlversuchen x 1,5 (bis rmax),
    nach einem Erfolg / 1,2 (nicht unter r0).
    Schnellzerlegung im Bau mit Saum saum_bau; angenommen wird nur, wenn keine Umkugel den Saum verlaesst (dann sind die
    behaltenen Tetraeder genau die periodischen Delaunay-Tetraeder). Start und Schluss mit dem vollen Saum tg.SAUM; ist
    der Schluss mit vollem Saum nicht unter der Schranke, laeuft die Schleife mit vollem Saum weiter."""
    t0 = time.time()
    L, pos0 = punkte_original(N, saat)
    rng = np.random.default_rng([SAAT_SF, int(N), int(saat)])
    pos = pos0.copy()
    LV, _, G, O, pr = triang(pos, L)
    q = form(tet_X(LV, pos, G, O))[0]
    F = defizit(q, qs)
    F0, nbad0 = F, int((q < qs).sum())
    r, fehl, vers, ann, n_voll = r0, 0, 0, 0, 0
    saum = saum_bau
    verlauf = [{'vers': 0, 't_s': 0.0, 'F': F, 'n_unter': nbad0, 'q_min': float(q.min()), 'r': r}]
    schluss = []
    while time.time() - t0 < zeit_max and vers < max_vers:
        if F <= 0:
            LVv, _, Gv, Ov, prv = triang(pos, L)            # Schlusspruefung mit vollem Saum
            qv = form(tet_X(LVv, pos, Gv, Ov))[0]
            Fv = defizit(qv, qs)
            schluss.append({'vers': vers, 'F_voll': Fv, 'verletzt': prv['umkugel_ausserhalb_saum']})
            G, O, q, F, pr = Gv, Ov, qv, Fv, prv
            if Fv <= 0 and prv['umkugel_ausserhalb_saum'] == 0:
                break
            saum = tg.SAUM
            continue
        bad = np.nonzero(q < qs)[0]
        w = qs - q[bad]
        t = bad[rng.choice(len(bad), p=w / w.sum())]
        v = G[t, rng.integers(4)]
        u = rng.normal(size=3)
        u /= np.linalg.norm(u)
        d = u * r * rng.uniform() ** (1.0 / 3.0)
        pn_ = pos.copy()
        pn_[v] = np.mod(pos[v] + d, L)
        LVn, _, Gn, On, prn = triang(pn_, L, saum)
        if prn['umkugel_ausserhalb_saum'] > 0 and saum < tg.SAUM:
            LVn, _, Gn, On, prn = triang(pn_, L, tg.SAUM)      # Rueckfall auf den vollen Saum (exakt)
            n_voll += 1
        qn = form(tet_X(LVn, pn_, Gn, On))[0]
        Fn = defizit(qn, qs)
        vers += 1
        if Fn < F and prn['umkugel_ausserhalb_saum'] == 0:
            pos, G, O, q, F, pr = pn_, Gn, On, qn, Fn, prn
            ann += 1
            fehl = 0
            r = max(r0, r / 1.2)
        else:
            fehl += 1
            if fehl % 25 == 0:
                r = min(r * 1.5, rmax)
        if vers % protokoll == 0:
            verlauf.append({'vers': vers, 't_s': time.time() - t0, 'F': F, 'n_unter': int((q < qs).sum()),
                            'q_min': float(q.min()), 'r': r})
    LVv, _, Gv, Ov, prv = triang(pos, L)                    # Endzustand immer mit vollem Saum
    qv = form(tet_X(LVv, pos, Gv, Ov))[0]
    F, q, pr = defizit(qv, qs), qv, prv
    dv = minbild(pos - pos0, L)
    dl = np.linalg.norm(dv, axis=1)
    out = {'saat': int(saat), 'N': int(N), 'L': L, 'qs': qs, 'r0': r0, 'rmax': rmax, 'saum_bau': saum_bau,
           'erreicht': bool(F <= 0 and pr['umkugel_ausserhalb_saum'] == 0), 'schlusspruefungen': schluss,
           'n_rueckfall_voller_saum': n_voll,
           'versuche': vers, 'angenommen': ann, 't_s': time.time() - t0, 'F_start': F0, 'n_unter_start': nbad0,
           'F_ende': F, 'n_unter_ende': int((q < qs).sum()), 'q_min_ende': float(q.min()),
           'verschiebung': {'n_bewegt': int((dl > 0).sum()), 'mittel_alle': float(dl.mean()), 'max': float(dl.max()),
                            'mittel_bewegte': float(dl[dl > 0].mean()) if (dl > 0).any() else 0.0,
                            'mittlerer_nn_abstand_original': float(nn_abstand(pos0, L).mean())},
           'verlauf': verlauf, 'pos': pos.tolist(), 'pos_sha256': hashlib.sha256(np.ascontiguousarray(pos).tobytes()).hexdigest(),
           'zerlegung': pr}
    return out


def nn_abstand(pos, L):
    d = minbild(pos[:, None, :] - pos[None, :, :], L)
    r = np.linalg.norm(d, axis=-1)
    np.fill_diagonal(r, np.inf)
    return r.min(1)


# ------------------------------------------------------------------------------------------------ Kristallisationsprobe
def assoc_legendre(l, m, x):
    """P_l^m(x) ueber die Standard-Rekursion (mit Condon-Shortley-Phase; fuer |Y|^2 ohne Belang)."""
    pmm = np.ones_like(x)
    if m > 0:
        somx2 = np.sqrt(np.clip((1.0 - x) * (1.0 + x), 0.0, None))
        fact = 1.0
        for _ in range(m):
            pmm = -pmm * fact * somx2
            fact += 2.0
    if l == m:
        return pmm
    pmmp1 = x * (2 * m + 1) * pmm
    if l == m + 1:
        return pmmp1
    for ll in range(m + 2, l + 1):
        pll = ((2 * ll - 1) * x * pmmp1 - (ll + m - 1) * pmm) / (ll - m)
        pmm, pmmp1 = pmmp1, pll
    return pmmp1


def ql_global(bvec, l=6):
    """Q_l global (Steinhardt) ueber Bindungsvektoren: sqrt(4 pi/(2l+1) Summe_m |<Y_lm>|^2)."""
    u = bvec / np.linalg.norm(bvec, axis=1)[:, None]
    ct = u[:, 2]
    ph = np.arctan2(u[:, 1], u[:, 0])
    s = 0.0
    for m in range(l + 1):
        nrm = math.sqrt((2 * l + 1) / (4 * math.pi) * math.factorial(l - m) / math.factorial(l + m))
        Y = nrm * assoc_legendre(l, m, ct) * np.exp(1j * m * ph)
        s += (1.0 if m == 0 else 2.0) * abs(Y.mean()) ** 2
    return float(math.sqrt(4 * math.pi / (2 * l + 1) * s))


def paarbindungen(pos, L, rc):
    d = minbild(pos[:, None, :] - pos[None, :, :], L)
    r = np.linalg.norm(d, axis=-1)
    iu = np.triu_indices(len(pos), 1)
    m = r[iu] < rc
    return d[iu][m], r[iu]


def strukturfaktor(pos, L, nmax=NMAX_S):
    g = np.arange(-nmax, nmax + 1)
    n = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    m2 = (n ** 2).sum(1)
    erst = np.array([next((x for x in row if x != 0), 0) for row in n])
    sel = (m2 > 0) & (m2 <= nmax ** 2) & (erst > 0)
    n = n[sel]
    qv = 2.0 * np.pi * n / L
    S = np.abs(np.exp(1j * pos @ qv.T).sum(0)) ** 2 / len(pos)
    qb = np.linalg.norm(qv, axis=1)
    j = int(np.argmax(S))
    return {'S_max': float(S.max()), 'q_bei_S_max': float(qb[j]), 'n_bei_S_max': n[j].tolist(), 'n_q': int(len(S)),
            'S_mittel': float(S.mean())}


def kristall(pos, L, bvec_delaunay=None):
    bv, rall = paarbindungen(pos, L, RC_Q6)
    h, kanten = np.histogram(rall, bins=50, range=(0.0, 2.5))
    rm = 0.5 * (kanten[1:] + kanten[:-1])
    dr = kanten[1] - kanten[0]
    N = len(pos)
    ideal = (N * (N - 1) / 2.0) * 4 * np.pi * rm ** 2 * dr / L ** 3
    gr = h / ideal
    j = int(np.argmax(gr))
    out = {'Q6_rc': ql_global(bv, 6) if len(bv) else None, 'Q4_rc': ql_global(bv, 4) if len(bv) else None,
           'n_bindungen_rc': int(len(bv)), 'mittlere_nachbarn_rc': float(2.0 * len(bv) / N),
           'g_max': float(gr.max()), 'r_bei_g_max': float(rm[j]), 'r_min_paar': float(rall.min()),
           'g_r': gr.tolist(), 'r_mitte': rm.tolist()}
    out.update(strukturfaktor(pos, L))
    if bvec_delaunay is not None:
        out['Q6_delaunay'] = ql_global(bvec_delaunay, 6)
    out['kristallin'] = bool(out['S_max'] >= S_KRIST or (out['Q6_rc'] is not None and out['Q6_rc'] >= Q6_KRIST))
    return out


def bcc_probe(N=N_GLAS):
    L = float(N) ** (1.0 / 3.0)
    a = L / 4.0
    g = np.arange(4)
    p = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3).astype(float)
    pos = np.concatenate([p, p + 0.5]) * a
    rng = np.random.default_rng(5)
    return {'bcc_ideal': kristall(pos, L), 'bcc_gestoert_0.05': kristall(np.mod(pos + 0.05 * rng.normal(size=pos.shape), L), L)}


# ------------------------------------------------------------------------------------------------ Netze
def netz(art, saat, baudatei=None):
    """art 'orig': tg.zufallsnetz(128, s) selbst; art 'sf': gespeicherte Punkte aus dem Bau, Zerlegung triang."""
    if art == 'orig':
        LV, pos, G, O, pr = tg.zufallsnetz(N_GLAS, saat)
        return LV, pos, G, O, {'quelle': 'tg.zufallsnetz(128, %d)' % saat, 'pruefung': pr}
    d = lade(baudatei)['ergebnis']['saaten'][str(saat)]['bau']
    pos = np.array(d['pos'], float)
    if hashlib.sha256(np.ascontiguousarray(pos).tobytes()).hexdigest() != d['pos_sha256']:
        raise RuntimeError('pos_sha256 weicht ab')
    LV, pos, G, O, pr = triang(pos, d['L'])
    return LV, pos, G, O, {'quelle': 'sf.triang(Bau %s, Saat %d)' % (os.path.basename(baudatei), saat), 'pruefung': pr,
                           'pos_sha256': d['pos_sha256'], 'qs': d['qs']}


def masken(mod, geo):
    q, V, R = form(geo['X'])
    T = len(q)
    E = mod['E']
    out, info = {}, {}
    o_q = np.argsort(q, kind='stable')
    o_v = np.argsort(V, kind='stable')
    for nm, o, ant in (('q5', o_q, 0.05), ('q1', o_q, 0.01), ('q10', o_q, 0.10), ('v5', o_v, 0.05)):
        nb = int(math.ceil(ant * T))
        m = np.zeros(E, bool)
        m[np.unique(mod['eidx'][o[:nb]])] = True
        out[nm] = m
        info[nm] = {'n_tetra': nb, 'n_kanten': int(m.sum()), 'kantenanteil': float(m.sum() / E),
                    'q_grenze': float(q[o[nb - 1]]) if nm.startswith('q') else None}
    return out, info, q, V


def lokal(mod, geo, k, mk):
    """Wachsende Moden (Eigenwerte < 0 von Z, wie hm.z_auswerten) fuer A1RH, A2RH (SF1) und A2LR1, A2LRH
    (beschreibend): Kantenvektor a = S x der Lage-Eigenrichtung x, Anteil sum_{e in Maske} |a_e|^2 / sum |a_e|^2."""
    t0 = time.time()
    Bs, A1s, M, c = tg.ops(mod, k)
    B = Bs.tocsr()
    A1 = hm.assemble_sp(mod, geo['A1t'], k)
    A2 = hm.assemble_sp(mod, geo['A2t'], k)
    K = hm.assemble_sp(mod, geo['Kt'], k)
    S, Q, C, weg, svrel = hm.zerlege(M, c)
    Sh = np.conj(S.T)
    Br = herm(Sh @ (B @ S))
    try:
        L = np.linalg.cholesky(Br)
    except np.linalg.LinAlgError:
        return {'B_red_pd': False, 't_s': time.time() - t0}
    Li = sla.solve_triangular(L, np.eye(L.shape[0]), lower=True)
    A2L = np.linalg.inv(K.toarray())
    Ared = {'A1RH': hm.rh_A(A1, S, C), 'A2RH': hm.rh_A(A2, S, C), 'A2LR1': Sh @ A2L @ S, 'A2LRH': hm.rh_A(A2L, S, C)}
    out = {'B_red_pd': True}
    for v, Ar in Ared.items():
        Kv = herm(np.linalg.inv(herm(Ar)))
        Z = herm(Li @ Kv @ np.conj(Li.T))
        ev, U = np.linalg.eigh(Z)
        neg = np.nonzero(ev < 0)[0]
        X = np.conj(Li.T) @ U[:, neg]
        a = S @ X
        w = np.abs(a) ** 2
        tot = w.sum(0)
        moden = []
        for j in range(len(neg)):
            mo = {'ev': float(ev[neg[j]]), 'pr': float(tot[j] ** 2 / (w.shape[0] * (w[:, j] ** 2).sum()))}
            for nm, m in mk.items():
                mo['f_' + nm] = float(w[m, j].sum() / tot[j])
            moden.append(mo)
        out[v] = {'n_neg_eigh': int(len(neg)), 'moden': moden}
    out['t_s'] = time.time() - t0
    return out


# ------------------------------------------------------------------------------------------------ Laeufe
def lauf_bau(saaten, qs, zeit, r0, rmax):
    out = {'qs': qs, 'r0': r0, 'rmax': rmax, 'zeit_je_saat': zeit, 'saaten': {}}
    for s in saaten:
        b = bau_sf(N_GLAS, s, qs, zeit, r0, rmax)
        e = {'bau': b}
        L = b['L']
        for art, pos in (('orig', punkte_original(N_GLAS, s)[1]), ('sf', np.array(b['pos']))):
            LV, p, G, O, pr = triang(pos, L)
            mod = tg.modell(LV, p, G, O, pr)
            q, V, R = form(tet_X(LV, p, G, O))
            e[art] = {'pruefung': mod['pruefung'], 'form': form_statistik(q, V),
                      'kristall': kristall(p, L, mod['n'] * mod['l'][:, None]),
                      'l_mittel': float(np.mean(mod['l'])), 'E': int(mod['E']), 'T': int(mod['T'])}
        # Kontrolle: triang der Originalpunkte = tg.zufallsnetz
        LV0, p0, G0, O0, pr0 = tg.zufallsnetz(N_GLAS, s)
        LV1, p1, G1, O1, pr1 = triang(punkte_original(N_GLAS, s)[1], L)
        e['kontr_triang_gleich_tg'] = bool(np.array_equal(G0, G1) and np.array_equal(O0, O1) and np.array_equal(p0, p1))
        out['saaten'][str(s)] = e
    out['bcc_probe'] = bcc_probe()
    return out


def lauf_hm(art, saat, baudatei, rauch=False, ridx=None):
    t00 = time.time()
    LV, pos, G, O, info = netz(art, saat, baudatei)
    mod = tg.modell(LV, pos, G, O, {})
    geo = hm.tet_geo(LV, pos, G, O, mod)
    mk, mkinfo, q, V = masken(mod, geo)
    richt = tg.richtungen13w()
    epsl = (tg.EPS1, tg.EPS2)
    idx = list(range(len(richt))) if ridx is None else list(ridx)
    if rauch:
        idx = idx[:1]
    zeilen = []
    for ir in idx:
        nm, d = richt[ir]
        tt3 = nm in ('100', '110', '111')
        z = {'ridx': int(ir), 'richtung': nm, 'd': d.tolist()}
        for i, e in enumerate(epsl):
            if i == 1 and not tt3:
                continue                       # wie hm.lauf_spanne: |k| = 2e-2 nur an [100], [110], [111]
            p = hm.punkt(mod, geo, e * d, mit_tt=(i == 0 and tt3), mit_kontr=False, mit_vert=False)
            p['lokal'] = lokal(mod, geo, e * d, mk)
            z['eps%d' % (i + 1)] = p
        zeilen.append(z)
    out = {'art': art, 'saat': saat, 'info': info, 'E': int(mod['E']), 'T': int(mod['T']), 'nV': int(mod['nV']),
           'pruefung': mod['pruefung'], 'geo_kontr': geo['kontr'], 'vref': geo['vref'], 'eps': list(epsl), 'ridx': idx,
           'masken': mkinfo, 'form': form_statistik(q, V), 'zeilen': zeilen, 't_s': time.time() - t00}
    return out


def lauf_lr(art, saat, baudatei, rauch=False):
    t00 = time.time()
    LV, pos, G, O, info = netz(art, saat, baudatei)
    mod = tg.modell(LV, pos, G, O, {})
    geo = hm.tet_geo(LV, pos, G, O, mod)
    net = {'name': '%s-s%d' % (art, saat), 'LV': np.asarray(LV, float), 'mod': mod, 'geo': geo, 'info': info,
           'l_mittel': float(np.mean(mod['l'])), 'glas': True}
    l = net['l_mittel']
    richt = tg.richtungen13w()[:1] if rauch else tg.richtungen13w()
    zeilen = []
    for nm, d in richt:
        z = {'richtung': nm, 'd': d.tolist()}
        for kl in KL_LR:
            k = (kl / l) * d                     # wie lrm.lauf_spanne
            z['kl%g' % kl] = lrm.punkt(net, k, mit_a1=True, voll=False)
        zeilen.append(z)
    return {'art': art, 'saat': saat, 'info': info, 'E': int(mod['E']), 'T': int(mod['T']), 'l_mittel': l,
            'kl': list(KL_LR), 'zeilen': zeilen, 't_s': time.time() - t00}


# ------------------------------------------------------------------------------------------------ Rauchtests (nur Geometrie, Zeiten, Schluessel)
def lauf_rauch_form():
    out = {'saaten': {}}
    for s in SAATEN:
        t = time.time()
        LV, p, G, O, pr = tg.zufallsnetz(N_GLAS, s)
        t_tg = time.time() - t
        L, p1 = punkte_original(N_GLAS, s)
        t = time.time()
        LV1, p1, G1, O1, pr1 = triang(p1, L)
        t_tr = time.time() - t
        t = time.time()
        q, V, R = form(tet_X(LV1, p1, G1, O1))
        t_form = time.time() - t
        mod = tg.modell(LV, p, G, O, pr)
        out['saaten'][str(s)] = {'triang_gleich_tg': bool(np.array_equal(G, G1) and np.array_equal(O, O1)),
                                 't_tg_s': t_tg, 't_triang_s': t_tr, 't_form_s': t_form, 'form': form_statistik(q, V),
                                 'kristall': kristall(p, L, mod['n'] * mod['l'][:, None]),
                                 'nn_mittel': float(nn_abstand(p, L).mean())}
    out['bcc_probe'] = bcc_probe()
    rng = np.random.default_rng(3)
    u = rng.normal(size=(1, 3))
    out['Q6_eine_bindung'] = ql_global(u, 6)
    return out


def nur_schluessel(x, tiefe=0):
    if isinstance(x, dict):
        return {k: nur_schluessel(v, tiefe + 1) for k, v in x.items()} if tiefe < 3 else sorted(x.keys())
    if isinstance(x, list):
        return 'list[%d]' % len(x)
    return type(x).__name__


def lauf_rauch_punkt(art, saat, baudatei):
    """Laufzeiten je Punkt (HM-Satz mit lokal, LR-Satz); Ausgabe nur Zeiten und Schluessel, keine Werte."""
    t = time.time()
    h = lauf_hm(art, saat, baudatei, rauch=True)
    t_hm = time.time() - t
    t = time.time()
    r = lauf_lr(art, saat, baudatei, rauch=True)
    t_lr = time.time() - t
    z = h['zeilen'][0]
    return {'t_hm_1richtung_2punkte_s': t_hm, 't_hm_punkt_s': [z[e]['t_s'] for e in ('eps1', 'eps2') if e in z],
            't_lokal_s': [z[e]['lokal']['t_s'] for e in ('eps1', 'eps2') if e in z],
            't_lr_1richtung_s': t_lr, 't_lr_punkt_s': [r['zeilen'][0]['kl%g' % kl]['t_s'] for kl in KL_LR],
            'schluessel_hm': nur_schluessel(h), 'schluessel_lr': nur_schluessel(r)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch-form', 'rauch-bau', 'rauch-punkt', 'bau', 'hm', 'lr', 'aw'])
    ap.add_argument('--saaten', default='1')
    ap.add_argument('--saat', type=int, default=1)
    ap.add_argument('--art', choices=['orig', 'sf'], default='orig')
    ap.add_argument('--bau', default=None, help='Baudatei (JSON) des splitterarmen Glases')
    ap.add_argument('--qs', type=float, default=None)
    ap.add_argument('--zeit', type=float, default=100.0)
    ap.add_argument('--r0', type=float, default=0.05)
    ap.add_argument('--rmax', type=float, default=0.4)
    ap.add_argument('--ridx', default=None, help='Richtungsindizes des HM-Satzes, z. B. 0-6')
    ap.add_argument('--rauch', action='store_true', help='Absturzprobe: nur die erste Richtung')
    ap.add_argument('--lauf', default='lauf')
    ap.add_argument('--hmref', default='/home/fmh/fmhc-physics-remote/hodge-masse-1/lauf')
    ap.add_argument('--lrref', default='/home/fmh/fmhc-physics-remote/lund-regge-masse-1/lauf')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    hier = os.path.dirname(os.path.abspath(__file__))
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'sha256': {f: sha(os.path.join(hier, f)) for f in sorted(os.listdir(hier)) if f.endswith('.py')}}
    saaten = [int(x) for x in a.saaten.split(',')]
    if a.modus == 'rauch-form':
        erg = lauf_rauch_form()
    elif a.modus == 'rauch-bau':
        erg = {'saaten': {}}
        for s in saaten:
            b = bau_sf(N_GLAS, s, a.qs, a.zeit, a.r0, a.rmax)
            p = np.array(b.pop('pos'))
            LV, p, G, O, pr = triang(p, b['L'])
            mod = tg.modell(LV, p, G, O, pr)
            q, V, R = form(tet_X(LV, p, G, O))
            b['form_ende'] = form_statistik(q, V)
            b['kristall_ende'] = kristall(p, b['L'], mod['n'] * mod['l'][:, None])
            b['pruefung_ende'] = mod['pruefung']
            erg['saaten'][str(s)] = b
    elif a.modus == 'rauch-punkt':
        erg = lauf_rauch_punkt(a.art, a.saat, a.bau)
    elif a.modus == 'bau':
        erg = lauf_bau(saaten, a.qs, a.zeit, a.r0, a.rmax)
    elif a.modus == 'hm':
        ridx = None
        if a.ridx:
            lo, hi = a.ridx.split('-')
            ridx = list(range(int(lo), int(hi) + 1))
        erg = lauf_hm(a.art, a.saat, a.bau, rauch=a.rauch, ridx=ridx)
    elif a.modus == 'lr':
        erg = lauf_lr(a.art, a.saat, a.bau, rauch=a.rauch)
    else:
        import sf_aw
        erg = sf_aw.auswerten(a.lauf, a.hmref, a.lrref, a.out)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
