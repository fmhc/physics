#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DANZER-TT-1 (Runde 48, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage (KARTE.md): Werden die TT-Moden (Schwerewellen) des Hamilton-Netzes (EINE-WELT-LOCH-1, Paarung A1R1, J = 1 je
Tetraeder) auf den Ammann-Kramer-Naeherungen 1/1, 2/1, 3/2 eines Ikosaeder-Quasikristalls von Stufe zu Stufe
richtungsgleicher?

Bausteine, alle unveraendert importiert:
  danzer_naeherung.py (DANZER-NAEHERUNG-1/-2, 0571953e...): naeherung, ecken (Fenster), rhomboeder, saat_rng, ETA,
      SIGMA_D, OFFS. Der Delaunay-Bau unten ist Zeile fuer Zeile dn2.netz2 (Zeilen 135-150), damit Saat, Fenster-
      Stoerung gamma, Zitter und Gleichstands-Aufloesung genau wie in DANZER-NAEHERUNG-2 sind.
  dn2.py (DANZER-NAEHERUNG-2, eingefroren a834b826...): netz2 als Gegenprobe (gleiche Kanten, Pruefungen, *1-Klasse).
  tg.py (TT-GLAS-1, ec48a258...): modell (Regge-B, A1-Masse, Eichung M, skalare Regel c) und punkt (Reduktion R1,
      Klassen, masselose Werte, TT-Anteil), affin.
  tti.py (TT-ISO-1, 6d6b6f7b...): richtungen13 (die 13 Plan-Richtungen von TT-ISO-1).
  dn.py (DEFEKT-NETZ-1, 0cd5d13e...): baue (A15, C15), kurz.
Messung wie TT-ISO-1 / DEFEKT-NETZ-1: Spanne s = max/min - 1 ueber 52 Werte omega^2/k^2 (13 Richtungen x 2 TT-Zweige
x |k| = 1e-3, 2e-3).

Aufruf (nur ueber kleintest.sh auf der .69):
  dtt.py rauch --ordnungen 1/1,2/1,3/2 --saat 0 --out rauch/r1.json        (nur Zeiten, Groessen, Schluessel)
  dtt.py kontrolle --out lauf/kontrolle.json                                (V, A15, C15)
  dtt.py netz --ordnung 2/1 --saaten 0,1 [--zitter 0] [--ridx 0-12] [--eps 1e-3,2e-3] [--bz 4] [--bz-teil i/n]
              [--wuerfel] [--affin] [--dn2] --out lauf/x.json
  dtt.py auswerten --out lauf/auswertung.json --png lauf/bild.png lauf/*.json
"""
import argparse, json, sys, os, time, hashlib, platform, resource, glob
from collections import Counter, defaultdict
import numpy as np
import scipy
from scipy.spatial import Delaunay, cKDTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import danzer_naeherung as dzn  # noqa: E402  (DANZER-NAEHERUNG-1/-2, unveraendert)
import dn2  # noqa: E402  (DANZER-NAEHERUNG-2, eingefroren, unveraendert)
import tg  # noqa: E402  (TT-GLAS-1, unveraendert)
import tti  # noqa: E402  (TT-ISO-1, unveraendert)
import ew  # noqa: E402
import tp  # noqa: E402
import dn as dnetz  # noqa: E402  (DEFEKT-NETZ-1, unveraendert)

EPS_TT = (1e-3, 2e-3)                    # |k| wie TT-ISO-1 und DEFEKT-NETZ-1
TT_DREI = ('100', '110', '111')
S_V_TTISO = 0.06338809562866454          # TT-ISO-1 lauf-69/gitter-V-A1R1.json, spanne_J1
S_V_KARTE = 0.0634                       # Karte DT0 ("6,34 %")
S_A15 = 0.009338681518611835             # DEFEKT-NETZ-1 lauf-69/tt-A15.json, ergebnis.spanne
S_C15 = 0.02684718450960677              # DEFEKT-NETZ-1 lauf-69/tt-C15.json, ergebnis.spanne
DT0_TOL = 1e-3
DT1_DRITTEL = 1.0 / 3.0
REIHE = ['1/1', '2/1', '3/2']


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def sha_arr(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


def js(o):
    if isinstance(o, dict):
        return {str(k): js(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [js(v) for v in o]
    if isinstance(o, np.ndarray):
        return js(o.tolist())
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def schreibe(pfad, res):
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(js(res), fh, indent=1)
    os.replace(pfad + '.tmp', pfad)


def info_kopf():
    d = os.path.dirname(os.path.abspath(__file__))
    return {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'sha256': {f: sha(os.path.join(d, f)) for f in ('dtt.py', 'danzer_naeherung.py', 'dn2.py', 'tg.py', 'tti.py',
                                                             'ew.py', 'tp.py', 'dn.py', 'licht_netz.py', 'nachtrag_kinetik.py')},
            'omp': os.environ.get('OMP_NUM_THREADS'), 'openblas': os.environ.get('OPENBLAS_NUM_THREADS')}


# ------------------------------------------------------------------------------------------------ Netz (wie dn2.netz2)
def netz_danzer(ordnung, saat, zitter_versatz=0):
    """Ecken und periodisches Delaunay genau wie dn2.netz2 (Zeilen 135-150 woertlich; gleiche Saat, gleiche
    Fenster-Stoerung gamma, gleicher Zitter-Strom). Geometrie mit den unverzitterten Ecken r (wie netz2: X = r[vid] + L off).
    Rueckgabe in der Form von tg.modell: Gittervektoren (Zeilen), Lagen, Tetraeder (T,4), Bildversaetze (T,4,3)."""
    t0 = time.time()
    nh = dzn.naeherung(ordnung)
    p, q = nh["p"], nh["q"]
    rng = dzn.saat_rng(nh["ordnung"], saat)
    xi = rng.normal(size=3)
    xi /= np.linalg.norm(xi)
    gamma = dzn.ETA * xi
    ek = dzn.ecken(nh, gamma)
    rh = dzn.rhomboeder(nh, ek, gamma)
    r, L, N = ek["r"], nh["L"], ek["N"]
    rz = rng if zitter_versatz == 0 else np.random.default_rng([3746, p, q, int(saat), 1000 + int(zitter_versatz)])
    rj = r + dzn.SIGMA_D * rz.normal(size=r.shape)
    big = (rj[None, :, :] + L * dzn.OFFS[:, None, :]).reshape(-1, 3)
    tri = Delaunay(big)
    S = tri.simplices
    cent = big[S].mean(axis=1)
    S = S[np.all((cent >= 0.0) & (cent < L), axis=1)]
    vid, off = S % N, dzn.OFFS[S // N]
    T = len(S)
    X = r[vid] + L * off
    vols = np.einsum("ti,ti->t", np.cross(X[:, 1] - X[:, 0], X[:, 2] - X[:, 0]), X[:, 3] - X[:, 0]) / 6.0
    # Leerkugel und Kugel-Gleichstaende an den unverzitterten Ecken (wie netz2)
    bigE = (r[None, :, :] + L * dzn.OFFS[:, None, :]).reshape(-1, 3)
    baum = cKDTree(bigE)
    ct = dn2.umkreis_tet(X)
    R = np.linalg.norm(ct - X[:, 0], axis=1)
    idxs = baum.query_ball_point(ct, R * (1 + 1e-9))
    verletzt, kugel_entartet, tet_entartet = 0, 0, 0
    for t in range(T):
        dist = np.linalg.norm(bigE[idxs[t]] - ct[t], axis=1)
        verletzt += int(np.sum(dist < R[t] * (1 - 1e-9)))
        z = int(max(0, np.sum(np.abs(dist - R[t]) <= 1e-9 * R[t]) - 4))
        kugel_entartet += z
        tet_entartet += int(z > 0)
    # Fingerabdruck der Zerlegung: sortierte kanonische Tetraeder (Ecken mit relativen Bildversaetzen)
    keys = []
    for t in range(T):
        best = None
        for m in range(4):
            lst = tuple(sorted((int(vid[t, u]), tuple(int(c) for c in (off[t, u] - off[t, m]))) for u in range(4)))
            if best is None or lst < best:
                best = lst
        keys.append(best)
    tet_sha = hashlib.sha256(repr(sorted(keys)).encode()).hexdigest()
    info = {'ordnung': ordnung, 'saat': int(saat), 'zitter_versatz': int(zitter_versatz), 'L': float(L),
            'eps_phason': float(nh['eps']), 'gamma': gamma.tolist(), 'N': int(N), 'N_erwartet': ek['N_erwartet'],
            'T': int(T), 'ecken_sha': sha_arr(ek["x6"]), 'tetraeder_sha': tet_sha,
            'fenster': {k: v for k, v in ek.items() if k not in ('x6', 'r')}, 'rhomboeder': rh,
            'vol_min': float(np.abs(vols).min()), 'vol_max': float(np.abs(vols).max()),
            'vol_rel_abw': float(abs(np.abs(vols).sum() - L ** 3) / L ** 3), 'tetraeder_flach_1e-10': int(np.sum(np.abs(vols) < 1e-10)),
            'delaunay_verletzt': int(verletzt), 'kugel_entartet_zusatzpunkte': int(kugel_entartet),
            'tetraeder_mit_gleichstand': int(tet_entartet), 't_bau_s': time.time() - t0}
    return np.eye(3) * L, r, vid.astype(np.int64), off.astype(np.int64), info, nh


def dn2_gegenprobe(nh, saat, zv, mod):
    """netz2 aus DANZER-NAEHERUNG-2: gleiche Kantenzahl, gleiche Ecken; *1-Klasse (Fingerabdruck) fuer den Bericht."""
    t0 = time.time()
    bau, pruef, dec, ek = dn2.netz2(nh, saat, zitter_versatz=zv)
    # Kantenmengen vergleichen: (kleinere Ecke, groessere Ecke, Versatz) wie tg.modell bzw. danzer_naeherung.kanten_key
    k_dn2 = set((int(a), int(b), tuple(int(x) for x in d)) for a, b, d in zip(bau['ei'], bau['ej'], bau['ed']))
    k_tg = set()
    for s, s2, d in zip(mod['es'], mod['es2'], (mod['Tedge'] / bau['L']).round().astype(int)):
        k, _, _ = dzn.kanten_key(s, np.zeros(3, int), s2, d)
        k_tg.add((k[0], k[1], k[2]))
    return {'E_dn2': int(bau['E']), 'T_dn2': int(pruef['T']), 'E_tg': int(mod['E']), 'T_tg': int(mod['T']),
            'kantenmengen_gleich': bool(k_dn2 == k_tg), 'ecken_sha_dn2': pruef['ecken_sha'],
            's1_klasse_sha': pruef['s1_positiv_sortiert_sha'][:8], 's0_klasse_sha': pruef['s0_sortiert_sha'][:8],
            'kugel_entartet_dn2': pruef['kugel_entartet_zusatzpunkte'], 'delaunay_verletzt_dn2': pruef['delaunay_verletzt'],
            'euler': pruef['euler'], 'flaechen_sonst': pruef['flaechen_sonst'], 'komponenten': pruef['zusammenhang_komponenten'],
            'stern1': pruef['stern1'], 'stern2': pruef['stern2'], 't_s': time.time() - t0}


# ------------------------------------------------------------------------------------------------ duenner Rechenweg
NEV = 4                # Eigenwerte naechst null (2 TT + 2 darueber)
NACHIT = 2             # Nachiterationen je Sattelpunkt-Loesung
TAU_D = 1e-6           # wachsend: Re omega^2 < -TAU_D eps^2 oder |Im omega^2| > TAU_D eps^2 (nur unter den NEV Werten)


ORDNUNG_LU = 'COLAMD'          # Rauchtests R9/R10: COLAMD 45 s, MMD_AT_PLUS_A ueber 105 s je LU-Paar bei 3/2
SV_SCHWELLE = 1e-6             # Ritz-Raum: Richtungen von X2 mit Singulaerwert > 1e-6 x groesster
PROTOKOLL = True               # Zwischenzeiten auf stdout (Log)


def punkt_duenn(mod, k, mit_tt=False, verfahren='ritz', nev=NEV):
    """Reduktion R1 wie tg.punkt, aber nur die Werte omega^2 naechst null.
    tg.punkt: omega^2 = Eigenwerte von (S^H A S)(S^H B S), S = orthonormale Basis von Bild(N)^perp, N = [M, c] (tg.ops),
    also die von null verschiedenen Eigenwerte von P A P B P (P = S S^H) bzw. die Eigenwerte des hermitesch-definiten
    Paars (S^H B S, (S^H A S)^-1). (P A P)^+ v = x aus [A N; N^H 0][x; mu] = [v; 0] (ebenso B), splu mit Nachiteration.
    Op = (P B P)^+ (P A P)^+ hat die Eigenwerte 1/omega^2.
    verfahren 'ritz' (Hauptweg): Block-Inversiteration aus den 6 affinen Wellen a_e = n_e^T h n_e e^{i k.m_e}
      (h = tp.B6, wie tg.tensor_fit): X1 = Op X0, X2 = Op X1; Rayleigh-Ritz auf span[X1, X2] (12 Vektoren) mit
      Bm = V^H B V und Mm = V^H (PAP)^+ V. Ritz-Werte sind obere Schranken (Min-Max), die zwei kleinsten sind die TT-Werte.
    verfahren 'arpack' (Diagnose): eigs auf Op, nev Werte groessten Betrags, Wert = Rayleigh-Quotient."""
    import scipy.sparse as sps
    import scipy.sparse.linalg as spla
    import scipy.linalg as sla
    t0 = time.time()
    eps = float(np.linalg.norm(k))
    B, A, M, c = tg.ops(mod, k)
    E = mod['E']
    N = sps.hstack([sps.csr_matrix(M), sps.csr_matrix(c)]).tocsr()
    nX = N.shape[1]
    NH = N.conj().T.tocsr()
    z = {'eps': eps, 'nX': int(nX), 'dim': int(E - nX), 'weg': 'duenn-' + verfahren, 'A_red_pd': None, 'B_red_neg': None,
         'sv_rel_min': None}
    KA = sps.bmat([[A, N], [NH, None]], format='csc')
    KB = sps.bmat([[B, N], [NH, None]], format='csc')
    try:
        luA = spla.splu(KA, permc_spec=ORDNUNG_LU)
        luB = spla.splu(KB, permc_spec=ORDNUNG_LU)
    except RuntimeError as err:
        z['fehler'] = 'splu: %s' % err
        z['t_s'] = time.time() - t0
        return z
    z['t_lu_s'] = time.time() - t0
    if PROTOKOLL:
        print('    LU %.1f s (nnz %d), Ordnung %s' % (z['t_lu_s'], luA.L.nnz + luA.U.nnz + luB.L.nnz + luB.U.nnz, ORDNUNG_LU), flush=True)
    zaehl = [0]

    def loese(lu, K, V):
        V = np.asarray(V, complex)
        eins = V.ndim == 1
        V2 = V[:, None] if eins else V
        b = np.concatenate([V2, np.zeros((nX, V2.shape[1]), complex)], 0)
        x = lu.solve(b)
        for _ in range(NACHIT):            # Nachiteration (iterative refinement)
            x = x + lu.solve(b - K @ x)
        zaehl[0] += V2.shape[1]
        return x[:E, 0] if eins else x[:E]

    def op(V):
        return loese(luB, KB, loese(luA, KA, V))

    tau = TAU_D * eps ** 2
    if verfahren == 'ritz':
        Es = np.einsum('ei,sij,ej->es', mod['n'], tp.B6, mod['n'])
        ph = np.exp(1j * (mod['mitte'] @ k))
        X1 = op(Es * ph[:, None])
        X2 = op(X1)
        # nur die tragenden Richtungen von X2 (Singulaerwerte > SV_SCHWELLE x groesster): Restrichtungen waeren
        # numerisches Rauschen (Eich- und Regelanteile im Rundungsbereich) und verfaelschten die Ritz-Werte
        Us, sv, _ = np.linalg.svd(X2 / np.linalg.norm(X2, axis=0), full_matrices=False)
        r_ = int((sv > SV_SCHWELLE * sv[0]).sum())
        z['ritz_rang'] = r_
        z['ritz_sv_rel'] = [float(x / sv[0]) for x in sv]
        V = Us[:, :r_]
        W = loese(luA, KA, V)
        Bm = np.conj(V.T) @ (B @ V)
        Mm = np.conj(V.T) @ W
        Bm = 0.5 * (Bm + np.conj(Bm.T))
        Mm = 0.5 * (Mm + np.conj(Mm.T))
        eM = np.linalg.eigvalsh(Mm)
        z['Mm_pd'] = bool(eM.min() > 0)
        z['Mm_cond'] = float(eM.max() / eM.min()) if eM.min() > 0 else None
        if z['Mm_pd']:
            w2, C = sla.eigh(Bm, Mm)
            w2im = np.zeros_like(w2)
        else:
            w2c, C = sla.eig(Bm, Mm)
            o_ = np.argsort(w2c.real)
            w2, w2im, C = w2c.real[o_], w2c.imag[o_], C[:, o_]
        U = V @ C
    else:
        Op = spla.LinearOperator((E, E), matvec=lambda v: op(np.asarray(v).ravel()), dtype=complex)
        g0 = np.random.default_rng([4711, E]).normal(size=(2, E))
        mu, U = spla.eigs(Op, k=nev, which='LM', v0=g0[0] + 1j * g0[1], ncv=max(2 * nev + 1, 20))
        w2c = 1.0 / mu
        o_ = np.argsort(w2c.real)
        w2, w2im, U = w2c.real[o_], w2c.imag[o_], U[:, o_]
    wachs = (w2 < -tau) | (np.abs(w2im) > tau)
    masse = (~wachs) & (np.abs(w2) <= tg.MASSELOS_MAX * eps ** 2)
    luecke = (~wachs) & (w2 >= tg.LUECKE_MIN * eps ** 2)
    unklar = ~(wachs | masse | luecke)
    im = np.nonzero(masse & (w2 > tau))[0]
    im = im[np.argsort(np.abs(w2[im]))]
    sel = sorted(im[:2], key=lambda j: w2[j])
    # je TT-Paar: Rayleigh-Quotient u^H B u / u^H (PAP)^+ u, Residuum |Op u - u/omega^2| / |u/omega^2|, Nebenbedingung N^H u
    rq, res, nb = [], [], []
    for j in sel:
        u = U[:, j]
        wv = loese(luA, KA, u)
        q = float(np.real(np.vdot(u, B @ u) / np.vdot(u, wv)))
        rq.append(q)
        res.append(float(np.linalg.norm(op(u) - u / q) / (np.linalg.norm(u) / abs(q))))
        nb.append(float(np.linalg.norm(NH @ u) / (np.linalg.norm(u) * abs(N).max())))
    z.update({'skala': None, 'tau': tau, 'n_wachsend': int(wachs.sum()), 'n_masselos': int(masse.sum()),
              'n_luecke': int(luecke.sum()), 'n_unklar': int(unklar.sum()), 'w2_kleinste': [float(x) for x in w2[:6]],
              'w2im_max': float(np.abs(w2im).max()), 'w2_min_re': float(w2.min()),
              'luecke_min': float(w2[luecke].min()) if luecke.any() else None,
              'unklar_werte': [float(x) for x in w2[unklar]][:6],
              'residuum_tt': res, 'residuum_max': float(max(res)) if res else None,
              'nebenbedingung_max': float(max(nb)) if nb else None,
              'w2k2_eigen': [float(w2[j] / eps ** 2) for j in sel],
              'rq_gegen_eigen_max': float(max(abs(x / (w2[j] / 1.0) - 1.0) for x, j in zip(rq, sel))) if sel else None,
              'matvec': int(zaehl[0]), 'lu_nnz': int(luA.L.nnz + luA.U.nnz + luB.L.nnz + luB.U.nnz)})
    z['w2k2_masselos'] = [x / eps ** 2 for x in rq]
    if mit_tt:
        tt, rest = [], []
        for j in sel:
            H, rr = tg.tensor_fit(mod, U[:, j], k, M)
            tt.append(float(tp.tt_anteil(H, k)[0]))
            rest.append(rr)
        z['tt_anteil'] = tt
        z['fit_rest'] = rest
    z['t_s'] = time.time() - t0
    return z


PUNKT = {'duenn': punkt_duenn, 'dicht': tg.punkt}


def kurz2(p):
    out = dnetz.kurz(p)
    for k in ('residuum_max', 'nebenbedingung_max', 'matvec', 'lu_nnz', 'fehler', 'w2k2_eigen', 'rq_gegen_eigen_max', 'residuum_tt', 'Mm_pd', 'Mm_cond', 't_lu_s', 'ritz_rang', 'ritz_sv_rel'):
        if k in p:
            out[k] = p[k]
    return out


# ------------------------------------------------------------------------------------------------ Messung
def ridx_lesen(txt):
    if '-' in txt:
        i0, i1 = txt.split('-')
        return list(range(int(i0), int(i1) + 1))
    return [int(x) for x in txt.split(',')]


def messen(mod, ridx, epsl, weg='duenn'):
    """13 Plan-Richtungen von TT-ISO-1 (Teilmenge ridx) x |k| in epsl; wie dn.lauf_tt Teil (1)."""
    zeilen = []
    r13 = tti.richtungen13()
    for i in ridx:
        nm, d = r13[i]
        z = {'ridx': int(i), 'richtung': nm, 'd': d.tolist(), 'weg': weg}
        for e in epsl:
            if weg == 'dicht':
                pnt = tg.punkt(mod, e * d, mit_tt=(nm in TT_DREI and e == EPS_TT[0]), mit_kontr=(nm == '100' and e == EPS_TT[0]))
            else:
                pnt = punkt_duenn(mod, e * d, mit_tt=(nm in TT_DREI and e == EPS_TT[0]))
            z['eps%g' % e] = kurz2(pnt)
            print('  %s richtung %s |k| %g: %.1f s' % (weg, nm, e, pnt['t_s']), flush=True)
        zeilen.append(z)
    return zeilen


def vergleich(zd, zs):
    """Gegenprobe: masselose Werte duenn gegen dicht (relative Abweichung), je Zeile und |k|."""
    abw, n = 0.0, 0
    for a_, b_ in zip(zd, zs):
        for e in EPS_TT:
            ke = 'eps%g' % e
            if ke in a_ and ke in b_:
                x, y = a_[ke]['w2k2_masselos'], b_[ke]['w2k2_masselos']
                if len(x) == 2 and len(y) == 2:
                    abw = max(abw, float(np.max(np.abs(np.array(y) / np.array(x) - 1.0))))
                    n += 1
                else:
                    abw = np.inf
    return {'abw_rel_max': abw, 'n_punkte': n}


def wuerfel(mod):
    """Beschreibend: 13 Wuerfelachsen von TT-GLAS-1 (decken die Halbkugel ohne Wuerfelsymmetrie ab), |k| = 1e-3."""
    out = []
    for nm, d in tg.richtungen13w():
        pnt = tg.punkt(mod, EPS_TT[0] * d)
        out.append({'richtung': nm, 'p': dnetz.kurz(pnt)})
    return out


def bz(mod, LV, Lk, teil=None):
    """Stabilitaet auf dem Gitter Lk^3 der Zelle ohne k = 0 (wie dn.lauf_tt Teil (7)); teil = (i, n): jeder n-te Punkt."""
    BVc = 2 * np.pi * np.linalg.inv(LV).T
    g = np.arange(Lk)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    if teil is not None:
        mm = mm[teil[0]::teil[1]]
    nw, napd, nbn, wrel, nsvd, nun = 0, 0, 0, np.inf, 0, 0
    liste = []
    for m in mm:
        k = (m / Lk) @ BVc
        pnt = tg.punkt(mod, k)
        nw += int(pnt['n_wachsend'] > 0)
        napd += int(not pnt['A_red_pd'])
        nbn += int(pnt['B_red_neg'] > 0)
        nsvd += int(pnt['weg'] == 'svd')
        nun += int(pnt['n_unklar'] > 0)
        wrel = min(wrel, pnt['w2_min_re'] / pnt['skala'])
        liste.append({'m': m.tolist(), 'n_wachsend': int(pnt['n_wachsend']), 'A_red_pd': bool(pnt['A_red_pd']),
                      'B_red_neg': int(pnt['B_red_neg']), 'w2_min_rel': float(pnt['w2_min_re'] / pnt['skala']),
                      'n_unklar': int(pnt['n_unklar']), 'w2im_max': float(pnt['w2im_max']), 't_s': float(pnt['t_s'])})
    return {'Lk': int(Lk), 'teil': list(teil) if teil else None, 'nk': int(len(mm)), 'k_mit_wachsend': nw,
            'k_A_red_nicht_pd': napd, 'k_B_red_neg': nbn, 'k_rangverlust_Mc': nsvd, 'k_mit_unklar': nun,
            'w2_min_rel': float(wrel), 'punkte': liste}


# ------------------------------------------------------------------------------------------------ Modi
def modus_rauch(a):
    """Nur Zeiten, Groessen und Schluessel; keine Werte."""
    res = {'info': info_kopf(), 'netze': []}
    for o in a.ordnungen.split(','):
        z = {'ordnung': o}
        t0 = time.time()
        if o == 'V':
            LV, pos, G, O = tg.netz_V()[:4]
            inf = {'N': int(len(pos)), 'T': int(len(G))}
        elif o in ('A15', 'C15'):
            LV, pos, typ, G, O, keys, binfo = dnetz.baue(o, 'delaunay')
            inf = {'N': int(len(pos)), 'T': int(len(G))}
        else:
            LV, pos, G, O, inf, nh = netz_danzer(o, a.saat)
        z['t_bau_s'] = time.time() - t0
        print('  bau %s %.1f s' % (o, z['t_bau_s']), flush=True)
        t0 = time.time()
        mod = tg.modell(LV, pos, G, O, {})
        z['t_modell_s'] = time.time() - t0
        z.update({'N': inf['N'], 'T': inf['T'], 'E': int(mod['E'])})
        if a.dn2 and o not in ('V', 'A15', 'C15'):
            gp = dn2_gegenprobe(nh, a.saat, 0, mod)
            z['dn2_t_s'] = gp['t_s']
            z['dn2_E_T_gleich'] = bool(gp['E_dn2'] == gp['E_tg'] and gp['T_dn2'] == gp['T_tg'])
            z['dn2_kanten_gleich'] = gp['kantenmengen_gleich']
            z['dn2_ecken_gleich'] = bool(gp['ecken_sha_dn2'] == inf['ecken_sha'])
        d = tti.richtungen13()[3][1]
        t0 = time.time()
        p1 = punkt_duenn(mod, EPS_TT[0] * d)
        z['t_duenn_ohne_tt_s'] = time.time() - t0
        z['duenn_schluessel'] = sorted(p1.keys())
        z['duenn_matvec'] = p1.get('matvec')
        z['duenn_lu_nnz'] = p1.get('lu_nnz')
        t0 = time.time()
        p2 = punkt_duenn(mod, EPS_TT[0] * tti.richtungen13()[0][1], mit_tt=True)
        z['t_duenn_mit_tt_s'] = time.time() - t0
        if a.dicht:
            t0 = time.time()
            p3 = tg.punkt(mod, EPS_TT[0] * d)
            z['t_dicht_ohne_tt_s'] = time.time() - t0
            # Gegenprobe ohne Werte: nur relative Abweichung der masselosen Werte duenn gegen dicht
            x, y = p3['w2k2_masselos'], p1['w2k2_masselos']
            z['duenn_gegen_dicht_abw_rel'] = (float(np.max(np.abs(np.array(y) / np.array(x) - 1.0)))
                                              if len(x) == 2 and len(y) == 2 else 'nicht je 2 Werte')
            z['duenn_residuum_max'] = p1.get('residuum_max')
            z['duenn_nebenbedingung_max'] = p1.get('nebenbedingung_max')
            z['duenn_residuum_tt'] = p1.get('residuum_tt')
            z['duenn_rq_gegen_eigen'] = p1.get('rq_gegen_eigen_max')
            z['duenn_t_lu_s'] = p1.get('t_lu_s')
            z['duenn_Mm_cond'] = p1.get('Mm_cond')
            z['duenn_ritz_rang'] = p1.get('ritz_rang')
            z['duenn_ritz_sv_rel'] = p1.get('ritz_sv_rel')
        z['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
        res['netze'].append(z)
        print('rauch', o, {k: v for k, v in z.items() if k.startswith('t_') or k in ('N', 'T', 'E', 'maxrss_MB')}, flush=True)
    schreibe(a.out, res)


def tt_satz(name, LV, pos, G, O, mit_affin=True):
    mod = tg.modell(LV, pos, G, O, {})
    out = {'netz': name, 'pruefung': mod['pruefung'], 'plan13_duenn': messen(mod, list(range(13)), EPS_TT, 'duenn'),
           'plan13_dicht': messen(mod, list(range(13)), EPS_TT, 'dicht')}
    out['vergleich'] = vergleich(out['plan13_dicht'], out['plan13_duenn'])
    if mit_affin:
        out['affin'] = tg.affin(mod)
    return out


def modus_kontrolle(a):
    res = {'info': info_kopf(), 'netze': {}}
    t0 = time.time()
    res['netze']['V'] = tt_satz('V', *tg.netz_V()[:4])
    for name in ('A15', 'C15'):
        LV, pos, typ, G, O, keys, info = dnetz.baue(name, 'delaunay')
        res['netze'][name] = tt_satz(name, LV, pos, G, O)
        res['netze'][name]['bau_info'] = info
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    schreibe(a.out, res)
    print('kontrolle fertig %.1f s' % res['laufzeit_s'], flush=True)


def modus_netz(a):
    res = {'info': info_kopf(), 'saaten': []}
    t00 = time.time()
    epsl = [float(x) for x in a.eps.split(',')] if a.eps else []
    ridx = ridx_lesen(a.ridx) if a.ridx else []
    teil = tuple(int(x) for x in a.bz_teil.split('/')) if a.bz_teil else None
    for s in [int(x) for x in a.saaten.split(',')]:
        t0 = time.time()
        LV, pos, G, O, inf, nh = netz_danzer(a.ordnung, s, a.zitter)
        mod = tg.modell(LV, pos, G, O, {})
        z = {'ordnung': a.ordnung, 'saat': s, 'zitter_versatz': int(a.zitter), 'netz': inf, 'pruefung': mod['pruefung'],
             'E': int(mod['E']), 'nV': int(mod['nV'])}
        print('%s Saat %d Zitter %d: N=%d E=%d T=%d (%.1f s)' % (a.ordnung, s, a.zitter, inf['N'], mod['E'], inf['T'],
                                                               time.time() - t0), flush=True)
        if a.dn2:
            z['dn2'] = dn2_gegenprobe(nh, s, a.zitter, mod)
        if ridx and epsl:
            z['plan13_' + a.weg] = messen(mod, ridx, epsl, a.weg)
            if a.dicht and a.weg == 'duenn':
                z['plan13_dicht'] = messen(mod, ridx, epsl, 'dicht')
                z['vergleich'] = vergleich(z['plan13_dicht'], z['plan13_duenn'])
        if a.wuerfel:
            z['wuerfel13'] = wuerfel(mod)
        if a.affin:
            z['affin'] = tg.affin(mod)
        if a.bz:
            z['bz'] = bz(mod, LV, a.bz, teil)
        z['t_s'] = time.time() - t0
        res['saaten'].append(z)
        schreibe(a.out, res)   # nach jeder Saat sichern
    res['laufzeit_s'] = time.time() - t00
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    schreibe(a.out, res)
    print('netz fertig %.1f s' % res['laufzeit_s'], flush=True)


# ------------------------------------------------------------------------------------------------ Auswertung
def kennzahlen(zeilen):
    """Spanne und Regularitaet aus 13 Plan-Zeilen (wie dn.lauf_tt (1))."""
    werte, pk = [], []
    for z in zeilen:
        for e in EPS_TT:
            p = z['eps%g' % e]
            pk.append(p)
            werte += p['w2k2_masselos']
    w = np.array(werte, float)
    n2 = all(len(p['w2k2_masselos']) == 2 for p in pk)
    tt = [x for z in zeilen if z['richtung'] in TT_DREI for x in z['eps%g' % EPS_TT[0]].get('tt_anteil', [])]
    lin = []
    for z in zeilen:
        a_, b_ = z['eps%g' % EPS_TT[0]]['w2k2_masselos'], z['eps%g' % EPS_TT[1]]['w2k2_masselos']
        if len(a_) == 2 and len(b_) == 2:
            lin += [abs(b_[i] / a_[i] - 1.0) for i in range(2)]
    def mx(key, f=max):
        v = [p[key] for p in pk if p.get(key) is not None]
        return float(f(v)) if v else None
    reg = {'n_punkte': len(pk), 'genau_2_masselos_alle': bool(all(p['n_masselos'] == 2 for p in pk)), 'zwei_positive_werte_alle': bool(n2),
           'wachsend_summe': int(sum(p['n_wachsend'] for p in pk)), 'unklar_summe': int(sum(p['n_unklar'] for p in pk)),
           'A_red_pd_alle': bool(all(p['A_red_pd'] for p in pk if p.get('A_red_pd') is not None)),
           'A_red_geprueft': int(sum(p.get('A_red_pd') is not None for p in pk)),
           'B_red_neg_summe': int(sum(p['B_red_neg'] for p in pk if p.get('B_red_neg') is not None)),
           'tt_anteil_min': float(min(tt)) if tt else None, 'n_tt_werte': len(tt), 'linear_max': float(max(lin)) if lin else None,
           'luecke_min': mx('luecke_min', min), 'w2im_max': mx('w2im_max'), 'sv_rel_min': mx('sv_rel_min', min),
           'residuum_max': mx('residuum_max'), 'nebenbedingung_max': mx('nebenbedingung_max'),
           'wege': sorted(set(p.get('weg', '?') for p in pk)),
           'n_masselos_je_punkt': sorted(Counter(int(p['n_masselos']) for p in pk).items())}
    reg['regulaer'] = bool(reg['genau_2_masselos_alle'] and n2 and reg['wachsend_summe'] == 0 and reg['unklar_summe'] == 0
                           and reg['A_red_pd_alle'] and reg['B_red_neg_summe'] == 0 and reg['tt_anteil_min'] is not None
                           and reg['tt_anteil_min'] >= 0.99 and reg['n_tt_werte'] == 6 and reg['linear_max'] is not None
                           and reg['linear_max'] <= 1e-2)
    out = {'spanne': float(w.max() / w.min() - 1.0) if (len(w) == 4 * len(zeilen) and len(zeilen) == 13) else None,
           'n_werte': int(len(w)), 'w_min': float(w.min()) if len(w) else None, 'w_max': float(w.max()) if len(w) else None,
           'w_mittel': float(w.mean()) if len(w) else None, 'regel': reg}
    a1 = np.array([z['eps%g' % EPS_TT[0]]['w2k2_masselos'] for z in zeilen if len(z['eps%g' % EPS_TT[0]]['w2k2_masselos']) == 2])
    if len(a1):
        out['richtungsspanne_zweigmittel'] = float(a1.mean(1).max() / a1.mean(1).min() - 1.0)
        out['aufspaltung_max'] = float((a1[:, 1] / a1[:, 0] - 1.0).max())
        i_max = int(np.argmax(a1[:, 1] / a1[:, 0]))
        out['aufspaltung_max_richtung'] = [z['richtung'] for z in zeilen if len(z['eps%g' % EPS_TT[0]]['w2k2_masselos']) == 2][i_max]
        out['w2k2_eps1'] = {z['richtung']: z['eps%g' % EPS_TT[0]]['w2k2_masselos'] for z in zeilen}
    return out


def urteil3(flags):
    if not flags:
        return 'nicht entscheidbar'
    if all(flags):
        return 'eingetroffen'
    if not any(flags):
        return 'nicht eingetroffen'
    return 'geteilt'


def modus_auswerten(a):
    dateien = sorted(set(a.eingaben))
    kontrolle, netze = None, defaultdict(lambda: {'plan13': {}, 'plan13_dicht': {}, 'bz': [], 'wuerfel13': None, 'affin': None,
                                                  'netz': None, 'dn2': None, 'pruefung': None, 'quellen': []})
    shas = {}
    for f in dateien:
        with open(f) as fh:
            d = json.load(fh)
        shas[os.path.basename(f)] = d['info']['sha256']['dtt.py']
        if 'netze' in d and isinstance(d['netze'], dict):
            kontrolle = d
            continue
        for z in d.get('saaten', []):
            key = (z['ordnung'], int(z['saat']), int(z['zitter_versatz']))
            n = netze[key]
            n['quellen'].append(os.path.basename(f))
            for k in ('netz', 'dn2', 'pruefung', 'affin', 'wuerfel13'):
                if z.get(k) is not None:
                    n[k] = z[k]
            for quelle, ziel in (('plan13_duenn', 'plan13'), ('plan13_dicht', 'plan13_dicht')):
                for row in z.get(quelle, []):
                    alt = n[ziel].setdefault(row['richtung'], {'ridx': row['ridx'], 'richtung': row['richtung'], 'd': row['d']})
                    for e in EPS_TT:
                        if ('eps%g' % e) in row:
                            alt['eps%g' % e] = row['eps%g' % e]
            if z.get('bz'):
                n['bz'].append(z['bz'])
    tab = {'dateien': dateien, 'dtt_sha256': shas, 'netze': {}, 'kontrolle': {}}
    # Kontrollnetze
    if kontrolle:
        for name, z in kontrolle['netze'].items():
            kz = kennzahlen(z['plan13_duenn'])
            kd = kennzahlen(z['plan13_dicht'])
            kz['dicht'] = {k: kd[k] for k in ('spanne', 'w_min', 'w_max', 'regel')}
            kz['vergleich_duenn_dicht'] = z['vergleich']
            kz['affin'] = {k: z['affin'][k] for k in ('min', 'max', 'spanne_max_min')} if z.get('affin') else None
            tab['kontrolle'][name] = kz
    # Danzer-Netze je Saat
    je_ordnung = defaultdict(list)
    for (o, s, zv), n in sorted(netze.items()):
        zeilen = [n['plan13'][k] for k in sorted(n['plan13'], key=lambda r: n['plan13'][r]['ridx'])
                  if all(('eps%g' % e) in n['plan13'][k] for e in EPS_TT)]
        e = {'ordnung': o, 'saat': s, 'zitter_versatz': zv, 'quellen': n['quellen'], 'n_richtungen_voll': len(zeilen)}
        if n['netz']:
            e['netz'] = {k: n['netz'][k] for k in ('N', 'T', 'L', 'eps_phason', 'ecken_sha', 'tetraeder_sha', 'vol_min', 'vol_max',
                                                   'vol_rel_abw', 'tetraeder_flach_1e-10', 'delaunay_verletzt',
                                                   'kugel_entartet_zusatzpunkte', 'tetraeder_mit_gleichstand')}
            e['netz']['fenster_entartet_1e-5'] = n['netz']['fenster'].get('fenster_entartet_1e-5')
        if n['dn2']:
            e['dn2'] = {k: n['dn2'][k] for k in ('E_dn2', 'E_tg', 'T_dn2', 'T_tg', 'kantenmengen_gleich', 's1_klasse_sha',
                                                 's0_klasse_sha', 'kugel_entartet_dn2', 'euler', 'flaechen_sonst', 'komponenten')}
            e['dn2']['ecken_gleich'] = bool(n['netz'] and n['dn2']['ecken_sha_dn2'] == n['netz']['ecken_sha'])
        if n['pruefung']:
            e['pruefung'] = {k: n['pruefung'][k] for k in ('E', 'T', 'nV', 'selbstkanten', 'volumen_summe_rel_abw', 'vol_min_rel_mittel',
                                                           'dieder_summe_minus_2pi_max', 'dieder_min_grad', 'dieder_max_grad',
                                                           'D_sym_max', 'schlaefli_lD_max', 'l_min', 'l_max')}
        if zeilen:
            e.update(kennzahlen(zeilen))
        # beschreibend: Spanne nur bei |k| = 1e-3 (26 Werte), auch wenn 2e-3 fehlt
        z1 = [n['plan13'][k] for k in n['plan13'] if ('eps%g' % EPS_TT[0]) in n['plan13'][k]]
        w1 = [x for r in z1 for x in r['eps%g' % EPS_TT[0]]['w2k2_masselos']]
        e['spanne_eps1'] = float(max(w1) / min(w1) - 1.0) if (len(z1) == 13 and len(w1) == 26) else None
        e['n_richtungen_eps1'] = len(z1)
        if z1 and 'w2k2_eps1' not in e:
            e['w2k2_eps1'] = {r['richtung']: r['eps%g' % EPS_TT[0]]['w2k2_masselos'] for r in z1}
        if z1 and 'regel' not in e:
            pk1 = [r['eps%g' % EPS_TT[0]] for r in z1]
            e['regel_eps1'] = {'n_punkte': len(pk1), 'wachsend_summe': int(sum(p['n_wachsend'] for p in pk1)),
                               'genau_2_masselos_alle': bool(all(p['n_masselos'] == 2 for p in pk1)),
                               'tt_anteil_min': min([x for p in pk1 for x in p.get('tt_anteil', [])] or [None]) if any(p.get('tt_anteil') for p in pk1) else None}
        if n['plan13_dicht']:
            gem = [r for r in n['plan13_dicht'] if r in n['plan13']]
            g = vergleich([n['plan13_dicht'][r] for r in gem], [n['plan13'][r] for r in gem])
            pkd = [r['eps%g' % ee] for r in n['plan13_dicht'].values() for ee in EPS_TT if ('eps%g' % ee) in r]
            g.update({'richtungen': sorted(n['plan13_dicht'].keys()), 'n_punkte_dicht': len(pkd),
                      'wachsend': int(sum(p['n_wachsend'] for p in pkd)), 'A_red_nicht_pd': int(sum((not p['A_red_pd']) for p in pkd)),
                      'B_red_neg': int(sum(p['B_red_neg'] for p in pkd)), 'n_masselos_2': int(sum(p['n_masselos'] == 2 for p in pkd)),
                      'tt_anteil': [x for p in pkd for x in p.get('tt_anteil', [])]})
            e['gegenprobe_dicht'] = g
        if n['affin']:
            e['affin'] = {k: n['affin'][k] for k in ('min', 'max', 'spanne_max_min')}
        if n['wuerfel13']:
            ww = [x for r in n['wuerfel13'] for x in r['p']['w2k2_masselos']]
            alle = ww + [x for r in zeilen for x in r['eps%g' % EPS_TT[0]]['w2k2_masselos']]
            e['wuerfel13'] = {'n_werte': len(ww), 'n_punkte': len(n['wuerfel13']),
                              'spanne_wuerfel13': float(max(ww) / min(ww) - 1) if ww else None,
                              'spanne_26_richtungen_eps1': float(max(alle) / min(alle) - 1) if alle else None,
                              'wachsend': int(sum(r['p']['n_wachsend'] for r in n['wuerfel13'])),
                              'nicht_2_masselos': int(sum(r['p']['n_masselos'] != 2 for r in n['wuerfel13']))}
        if n['bz']:
            e['bz'] = {'Lk': sorted(set(b['Lk'] for b in n['bz'])), 'nk': int(sum(b['nk'] for b in n['bz'])),
                       'k_mit_wachsend': int(sum(b['k_mit_wachsend'] for b in n['bz'])),
                       'k_A_red_nicht_pd': int(sum(b['k_A_red_nicht_pd'] for b in n['bz'])),
                       'k_B_red_neg': int(sum(b['k_B_red_neg'] for b in n['bz'])),
                       'k_rangverlust_Mc': int(sum(b['k_rangverlust_Mc'] for b in n['bz'])),
                       'k_mit_unklar': int(sum(b['k_mit_unklar'] for b in n['bz'])),
                       'w2_min_rel': float(min(b['w2_min_rel'] for b in n['bz']))}
        tab['netze']['%s s%d z%d' % (o, s, zv)] = e
        if zv == 0 and e.get('spanne') is not None:
            je_ordnung[o].append(e)
    # je Ordnung (nur Zitter 0)
    stufen = {}
    for o in REIHE:
        L_ = je_ordnung.get(o, [])
        sp = np.array([x['spanne'] for x in L_], float)
        stufen[o] = {'saaten': [x['saat'] for x in L_], 'spannen': sp.tolist(),
                     'mittel': float(sp.mean()) if len(sp) else None, 'sd': float(sp.std(ddof=1)) if len(sp) > 1 else None,
                     'min': float(sp.min()) if len(sp) else None, 'max': float(sp.max()) if len(sp) else None,
                     'eps_phason': (L_[0]['netz']['eps_phason'] if L_ and L_[0].get('netz') else None),
                     'alle_regulaer': bool(all(x['regel']['regulaer'] for x in L_)) if L_ else None}
    tab['stufen'] = stufen
    # Zitter-Kontrolle
    zk = {}
    for (o, s, zv), n in netze.items():
        if zv != 0:
            a0 = tab['netze'].get('%s s%d z0' % (o, s))
            a1 = tab['netze'].get('%s s%d z%d' % (o, s, zv))
            if a0 and a1 and a0.get('spanne_eps1') is not None and a1.get('spanne_eps1') is not None:
                gem = sorted(set(a0['w2k2_eps1']) & set(a1['w2k2_eps1']))
                w0 = np.array([a0['w2k2_eps1'][r] for r in gem], float)
                w1 = np.array([a1['w2k2_eps1'][r] for r in gem], float)
                zk['%s s%d z%d' % (o, s, zv)] = {'spanne_z0': a0.get('spanne'), 'spanne_zv': a1.get('spanne'),
                                                  'spanne_eps1_z0': a0['spanne_eps1'], 'spanne_eps1_zv': a1['spanne_eps1'],
                                                  'spanne_eps1_abw': float(a1['spanne_eps1'] - a0['spanne_eps1']),
                                                  'w_rel_abw_max': float(np.max(np.abs(w1 / w0 - 1))),
                                                  'tetraeder_gleich': bool(a0.get('netz', {}).get('tetraeder_sha') == a1.get('netz', {}).get('tetraeder_sha')),
                                                  'ecken_gleich': bool(a0.get('netz', {}).get('ecken_sha') == a1.get('netz', {}).get('ecken_sha'))}
    tab['zitter_kontrolle'] = zk
    # ---------------------------------------------------------------- Urteile (PLAN Abschnitt 6)
    U = {}
    sv = tab['kontrolle'].get('V', {}).get('spanne')
    if sv is not None:
        abw_plan = abs(sv / S_V_TTISO - 1.0)
        abw_karte = abs(sv / S_V_KARTE - 1.0)
        reg_v = tab['kontrolle']['V']['regel']['regulaer']
        U['DT0'] = {'s_V': sv, 'abw_rel_gegen_ttiso': abw_plan, 'abw_rel_gegen_6_34': abw_karte, 'V_regulaer': reg_v,
                    'plan': 'eingetroffen' if (abw_plan <= DT0_TOL and reg_v) else 'nicht eingetroffen',
                    'karte': 'eingetroffen' if abw_karte <= DT0_TOL else 'nicht eingetroffen'}
    else:
        U['DT0'] = {'plan': 'nicht entscheidbar', 'karte': 'nicht entscheidbar'}
    m11, m32 = stufen['1/1']['mittel'], stufen['3/2']['mittel']
    if m11 is not None and m32 is not None:
        R = m32 / m11
        streng = stufen['3/2']['max'] / stufen['1/1']['min']
        U['DT1'] = {'R_mittel': R, 'R_streng_max32_min11': streng, 'schwelle': DT1_DRITTEL,
                    'plan': 'eingetroffen' if R <= DT1_DRITTEL else 'nicht eingetroffen',
                    'karte': 'eingetroffen' if streng <= DT1_DRITTEL else 'nicht eingetroffen',
                    'n_saaten': [len(stufen['1/1']['spannen']), len(stufen['3/2']['spannen'])]}
    else:
        U['DT1'] = {'plan': 'nicht entscheidbar', 'karte': 'nicht entscheidbar'}
    # DT2: alle gerechneten k aller Netze 1/1 bis 3/2 (alle Saaten, auch Zitter-Netze): kein wachsender Mode
    stab = {}
    for o in REIHE:
        ks = [x for k_, x in tab['netze'].items() if x['ordnung'] == o]
        npkt = sum(x.get('regel', {}).get('n_punkte', 0) + x.get('regel_eps1', {}).get('n_punkte', 0) for x in ks) + sum(x.get('bz', {}).get('nk', 0) for x in ks) \
            + sum(x.get('wuerfel13', {}).get('n_punkte', 0) for x in ks)
        nw = sum(x.get('regel', {}).get('wachsend_summe', 0) + x.get('regel_eps1', {}).get('wachsend_summe', 0) for x in ks) + sum(x.get('bz', {}).get('k_mit_wachsend', 0) for x in ks) \
            + sum(x.get('wuerfel13', {}).get('wachsend', 0) for x in ks) \
            + sum(x.get('gegenprobe_dicht', {}).get('wachsend', 0) for x in ks)
        stab[o] = {'netze': len(ks), 'k_punkte': int(npkt), 'wachsend': int(nw),
                   'A_red_nicht_pd': int(sum(x.get('bz', {}).get('k_A_red_nicht_pd', 0) for x in ks)
                                         + sum(x.get('gegenprobe_dicht', {}).get('A_red_nicht_pd', 0) for x in ks)),
                   'B_red_neg': int(sum(x.get('bz', {}).get('k_B_red_neg', 0) for x in ks)
                                    + sum(x.get('gegenprobe_dicht', {}).get('B_red_neg', 0) for x in ks)),
                   'k_voll_geprueft_dicht': int(sum(x.get('bz', {}).get('nk', 0) for x in ks)
                                                + sum(x.get('gegenprobe_dicht', {}).get('n_punkte_dicht', 0) for x in ks)),
                   'bz_k': int(sum(x.get('bz', {}).get('nk', 0) for x in ks))}
    voll = all(stab[o]['k_punkte'] > 0 for o in REIHE)
    if voll:
        ok = all(stab[o]['wachsend'] == 0 for o in REIHE)
        U['DT2'] = {'je_ordnung': stab, 'plan': 'eingetroffen' if ok else 'nicht eingetroffen',
                    'karte': 'eingetroffen' if ok else 'nicht eingetroffen'}
    else:
        U['DT2'] = {'je_ordnung': stab, 'plan': 'nicht entscheidbar', 'karte': 'nicht entscheidbar'}
    if m32 is not None:
        U['DT3'] = {'mittel_32': m32, 'max_32': stufen['3/2']['max'], 's_A15': S_A15,
                    'plan': 'eingetroffen' if m32 < S_A15 else 'nicht eingetroffen',
                    'karte': urteil3([x < S_A15 for x in stufen['3/2']['spannen']])}
    else:
        U['DT3'] = {'plan': 'nicht entscheidbar', 'karte': 'nicht entscheidbar'}
    tab['urteile'] = U
    # beschreibend: Verhaeltnisse
    vh = {}
    for o1, o2 in (('1/1', '2/1'), ('2/1', '3/2'), ('1/1', '3/2')):
        if stufen[o1]['mittel'] and stufen[o2]['mittel']:
            vh['%s:%s' % (o2, o1)] = {'spanne': stufen[o2]['mittel'] / stufen[o1]['mittel'],
                                      'abs_eps': abs(stufen[o2]['eps_phason'] / stufen[o1]['eps_phason'])}
    tab['verhaeltnisse'] = vh
    schreibe(a.out, tab)
    if a.png:
        bild(tab, a.png)
    print(json.dumps(js(U), indent=1), flush=True)


def bild(tab, png):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=150)
    xs = {o: i for i, o in enumerate(REIHE)}
    for o in REIHE:
        st = tab['stufen'][o]
        if st['spannen']:
            ax.scatter([xs[o]] * len(st['spannen']), [100 * x for x in st['spannen']], s=22, color='#1f5fa8', alpha=0.75,
                       zorder=3, label='Danzer-Naeherung, je Saat' if o == '1/1' else None)
    mo = [o for o in REIHE if tab['stufen'][o]['mittel'] is not None]
    if mo:
        ax.plot([xs[o] for o in mo], [100 * tab['stufen'][o]['mittel'] for o in mo], '-', color='#1f5fa8', lw=1.6, zorder=2,
                label='Mittel ueber Saaten')
    k = tab.get('kontrolle', {})
    ref = [('V (Finn, gefuellt)', k.get('V', {}).get('spanne'), '#b23a3a', '--'),
           ('C15 (= S)', k.get('C15', {}).get('spanne'), '#d08a1e', '-.'),
           ('A15', k.get('A15', {}).get('spanne'), '#2e8b57', ':')]
    for nm, v, c, ls in ref:
        if v is not None:
            ax.axhline(100 * v, color=c, ls=ls, lw=1.3, label='%s %.3g %%' % (nm, 100 * v))
    ax.set_yscale('log')
    ax.set_xticks(range(len(REIHE)))
    ax.set_xticklabels(['%s\neps = %+.4f' % (o, tab['stufen'][o]['eps_phason']) if tab['stufen'][o]['eps_phason'] is not None else o
                        for o in REIHE])
    ax.set_xlim(-0.4, len(REIHE) - 0.6)
    ax.set_xlabel('Naeherungsstufe (Ammann-Kramer p/q), eps = Phason-Verzerrung')
    ax.set_ylabel('TT-Spanne max/min - 1 von omega^2/k^2 [%]')
    ax.set_title('DANZER-TT-1: TT-Spanne (A1R1, J = 1) je Stufe', fontsize=10)
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=7.5, loc='best')
    fig.tight_layout()
    fig.savefig(png)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'kontrolle', 'netz', 'auswerten'])
    ap.add_argument('--ordnungen', default='1/1')
    ap.add_argument('--ordnung', default='1/1')
    ap.add_argument('--saat', type=int, default=0)
    ap.add_argument('--saaten', default='0')
    ap.add_argument('--zitter', type=int, default=0)
    ap.add_argument('--ridx', default='')
    ap.add_argument('--eps', default='')
    ap.add_argument('--bz', type=int, default=0)
    ap.add_argument('--bz-teil', dest='bz_teil', default='')
    ap.add_argument('--wuerfel', action='store_true')
    ap.add_argument('--affin', action='store_true')
    ap.add_argument('--dn2', action='store_true')
    ap.add_argument('--mit-tt', dest='mit_tt', action='store_true')
    ap.add_argument('--dicht', action='store_true', help='zusaetzlich dichter Rechenweg tg.punkt (Gegenprobe)')
    ap.add_argument('--weg', default='duenn', choices=['duenn', 'dicht'])
    ap.add_argument('--png', default='')
    ap.add_argument('--alarm', type=int, default=0, help='Selbstabbruch nach so vielen Sekunden (Rauchtests)')
    ap.add_argument('--lu-ordnung', dest='lu_ordnung', default='')
    ap.add_argument('--out', required=True)
    ap.add_argument('eingaben', nargs='*')
    a = ap.parse_intermixed_args()
    if a.lu_ordnung:
        global ORDNUNG_LU
        ORDNUNG_LU = a.lu_ordnung
    if a.alarm > 0:
        import signal
        signal.alarm(a.alarm)
    {'rauch': modus_rauch, 'kontrolle': modus_kontrolle, 'netz': modus_netz, 'auswerten': modus_auswerten}[a.modus](a)


if __name__ == '__main__':
    main()
