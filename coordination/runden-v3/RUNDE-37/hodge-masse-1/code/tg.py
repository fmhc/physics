#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GLAS-1 (Runde 45, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage: Laufen die masselosen TT-Moden des Hamilton-Netzes (EINE-WELT-LOCH-1, Paarung A1R1, J = 1) auf periodischen
3D-Poisson-Delaunay-Netzen ("Glas") im Mittel in alle Richtungen gleich, und wie gross ist die Richtungsspanne je Netz?

Modell wie ew.py (EINE-WELT-LOCH-1), aber allgemein fuer jede periodische Triangulierung (Kasten = Superzelle, Bloch-k):
  Kantenwerte a_e = delta l / l; B = sum_t l D_t l (Regge, D = d theta / d l je Tetraeder, komplexer Schritt und C^+);
  Eichung = Eckverschiebung M; skalare Regel je Ecke c_v = -B w_v (Gewicht l_e); Bewegungsenergie je Tetraeder
  A0 = (n_e . n_f)^2 - 1/2 (J = 1); Zwangsflaeche S = orthonormales Komplement von Bild[M, c];
  omega^2 = Eigenwerte von (S^+ A S)(S^+ B S) (Reduktion R1).
ew.py und tp.py werden unveraendert importiert (Geometrie des Kontrollnetzes V, tensor_fit-Basis B6, tt_anteil).
"""
import argparse, json, sys, os, time, hashlib, platform, resource
import numpy as np
import scipy
import scipy.sparse as sp
from scipy.spatial import Delaunay

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402  (TENSOR-EIS-PYRO-1, sha256 419d7da6..., unveraendert)
import ew  # noqa: E402  (EINE-WELT-LOCH-1, sha256 fa7b6417..., unveraendert)

SAAT_BASIS = 4537
SAUM = 4.0
H_CS = 1e-20
PAARE = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2), (1, 2, 0, 3), (1, 3, 0, 2), (2, 3, 0, 1)]
EPS1, EPS2 = 1e-2, 2e-2      # Bloch-|k| (Punktdichte 1, Abstand ~1); 1e-2 statt 1e-3 wegen grosser Skala s (Splitter)
TAU_REL = 1e-12               # numerische Toleranz relativ zu s = max |omega^2|
MASSELOS_MAX = 30.0           # masselos: |omega^2| <= 30 eps^2
LUECKE_MIN = 100.0            # Luecke: omega^2 >= 100 eps^2
TT_RICHT = ('100', '110', '111')


# ------------------------------------------------------------------------------------------------ Richtungen
def richtungen13w():
    """13 Wuerfelachsen (3 Flaechen, 6 Kanten, 4 Raumdiagonalen): decken die Halbkugel ab (omega(k) = omega(-k))."""
    m = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1),
         (1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]
    return [(''.join(str(x) for x in v), np.array(v, float) / np.linalg.norm(v)) for v in m]


# ------------------------------------------------------------------------------------------------ Netze
def zufallsnetz(N, saat):
    """N Poisson-Punkte (Dichte 1) im Torus [0, L)^3, periodische Delaunay-Triangulierung ueber Saum-Kopien
    (wie strich-netz-1/spinnetz.zufallsnetz). Rueckgabe: Gittervektoren LV (Zeilen), Lagen, Tetraeder G (T,4),
    Bildversaetze O (T,4,3) in Einheiten von LV, Pruefgroessen."""
    rng = np.random.default_rng([SAAT_BASIS, int(N), int(saat)])
    L = float(N) ** (1.0 / 3.0)
    pos = rng.uniform(0.0, L, size=(N, 3))
    offs = np.array([(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)], dtype=np.int64)
    Pl, Il, Ol = [], [], []
    for o in offs:
        Q = pos + o * L
        m = np.all((Q >= -SAUM) & (Q <= L + SAUM), axis=1)
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
    # Umkugel innerhalb des Saums (sonst waere die Triangulierung am Rand nicht Delaunay-sicher)
    A = 2.0 * (X[:, 1:] - X[:, :1])
    b = (X[:, 1:] ** 2).sum(-1) - (X[:, :1] ** 2).sum(-1)
    C = np.linalg.solve(A, b[..., None])[..., 0]
    R = np.linalg.norm(C - X[:, 0], axis=1)
    verletzt = int(np.sum(np.any((C - R[:, None] < -SAUM) | (C + R[:, None] > L + SAUM), axis=1)))
    pr = {'saum': SAUM, 'umkugel_ausserhalb_saum': verletzt, 'R_umkugel_max': float(R.max()),
          'punkte_mit_kopien': int(len(P))}
    return np.eye(3) * L, pos, gidx[S], goff[S], pr


def netz_V():
    """Finns gefuelltes Netz V aus ew.geometrie (unveraendert), in dieselbe allgemeine Form gebracht."""
    pos8, zellen = ew.geometrie('V')
    G, O = [], []
    for z in zellen:
        assert len(z['X8']) == 4 and z['kin']
        ids = [ew.zerlege(x, pos8) for x in z['X8']]
        G.append([s for (s, n) in ids])
        O.append([list(n) for (s, n) in ids])
    pos = np.array([np.asarray(p, float) / 8.0 for p in pos8])
    return np.array(ew.AV, float), pos, np.array(G, np.int64), np.array(O, np.int64), {}


# ------------------------------------------------------------------------------------------------ Geometrie je Tetraeder
def dieder_batch(X):
    """Innere Diederwinkel (T,6) an den Kanten PAARE; X (T,4,3), komplexer Schritt erlaubt (wie tp.dieder)."""
    out = []
    for (i, j, k, l) in PAARE:
        e = X[:, j] - X[:, i]
        ee = e / np.sqrt((e * e).sum(-1))[:, None]
        u = X[:, k] - X[:, i]
        u = u - (u * ee).sum(-1)[:, None] * ee
        w = X[:, l] - X[:, i]
        w = w - (w * ee).sum(-1)[:, None] * ee
        out.append(np.arccos((u * w).sum(-1) / np.sqrt((u * u).sum(-1) * (w * w).sum(-1))))
    return np.stack(out, 1)


def zelle_D_batch(X):
    """D = d theta / d l (T,6,6) ueber komplexen Schritt nach den Eckkoordinaten und C^+ (wie ew.zelle_D)."""
    T = len(X)
    J = np.zeros((T, 6, 12))
    for v in range(4):
        for c in range(3):
            Xc = X.astype(complex)
            Xc[:, v, c] += 1j * H_CS
            J[:, :, 3 * v + c] = np.imag(dieder_batch(Xc)) / H_CS
    th0 = np.real(dieder_batch(X.astype(complex)))
    C = np.zeros((T, 6, 12))
    for p, (i, j, _, _) in enumerate(PAARE):
        e = X[:, j] - X[:, i]
        n = e / np.linalg.norm(e, axis=1)[:, None]
        C[:, p, 3 * j:3 * j + 3] = n
        C[:, p, 3 * i:3 * i + 3] = -n
    Ct = np.transpose(C, (0, 2, 1))
    Cp = Ct @ np.linalg.inv(C @ Ct)
    return J @ Cp, th0


def modell(LV, pos, G, O, pr0):
    t0 = time.time()
    T, nV = len(G), len(pos)
    X = pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)
    ia = [p[0] for p in PAARE]
    ib = [p[1] for p in PAARE]
    ga, gb = G[:, ia], G[:, ib]
    Oa, Ob = O[:, ia], O[:, ib]
    d = Ob - Oa
    nz = d != 0
    erst = np.argmax(nz, axis=2)
    erst_wert = np.take_along_axis(d, erst[..., None], axis=2)[..., 0]
    use1 = (ga < gb) | ((ga == gb) & (erst_wert < 0))
    s = np.where(use1, ga, gb)
    s2 = np.where(use1, gb, ga)
    dd = np.where(use1[..., None], d, -d)
    Ost = np.where(use1[..., None], Oa, Ob)
    assert np.abs(dd).max() <= 7
    key = (((s.astype(np.int64) * nV + s2) * 16 + dd[..., 0] + 8) * 16 + dd[..., 1] + 8) * 16 + dd[..., 2] + 8
    uniq, first, inv = np.unique(key.ravel(), return_index=True, return_inverse=True)
    E = len(uniq)
    eidx = inv.reshape(T, 6)
    es = s.ravel()[first]
    es2 = s2.ravel()[first]
    ed = dd.reshape(-1, 3)[first]
    start = pos[es]
    vec = pos[es2] + ed @ LV - start
    l = np.linalg.norm(vec, axis=1)
    n = vec / l[:, None]
    mitte = start + 0.5 * vec
    Tedge = ed.astype(float) @ LV
    Tcopy = np.einsum('tpi,ij->tpj', Ost.astype(float), LV)
    D, th0 = zelle_D_batch(X)
    et = np.stack([X[:, j] - X[:, i] for (i, j, _, _) in PAARE], 1)
    lt = np.linalg.norm(et, axis=2)
    nt = et / lt[..., None]
    laengen_abw = float(np.abs(lt - l[eidx]).max())
    Dl = lt[:, :, None] * D * lt[:, None, :]
    A0 = np.einsum('tpi,tqi->tpq', nt, nt) ** 2 - 0.5
    vol = np.abs(np.linalg.det(X[:, 1:] - X[:, :1])) / 6.0
    Vbox = abs(np.linalg.det(LV))
    dsum = np.bincount(eidx.ravel(), th0.ravel(), E)
    pr = dict(pr0)
    pr.update({'T': int(T), 'E': int(E), 'nV': int(nV), 'kanten_je_ecke': float(2 * E / nV), 'tetra_je_ecke': float(T / nV),
               'selbstkanten': int(np.sum(es == es2)), 'laengen_abw_max': laengen_abw,
               'volumen_summe_rel_abw': float(abs(vol.sum() / Vbox - 1)), 'vol_min': float(vol.min()),
               'vol_min_rel_mittel': float(vol.min() / vol.mean()),
               'dieder_summe_minus_2pi_max': float(np.abs(dsum - 2 * np.pi).max()),
               'dieder_min_grad': float(np.degrees(th0.min())), 'dieder_max_grad': float(np.degrees(th0.max())),
               'D_sym_max': float((np.abs(D - np.transpose(D, (0, 2, 1))).max(axis=(1, 2)) / np.abs(D).max(axis=(1, 2))).max()),
               'schlaefli_lD_max': float((np.abs(np.einsum('tp,tpq->tq', lt, D)).max(1) / (np.abs(D).max(axis=(1, 2)) * lt.max(1))).max()),
               'D_absmax': float(np.abs(D).max()), 'l_min': float(l.min()), 'l_max': float(l.max()),
               'Vbox': float(Vbox), 't_modell_s': time.time() - t0})
    return {'T': T, 'E': E, 'nV': nV, 'eidx': eidx, 'es': es, 'es2': es2, 'l': l, 'n': n, 'mitte': mitte, 'Tedge': Tedge,
            'Tcopy': Tcopy, 'Dl': Dl, 'A0': A0, 'Vbox': Vbox, 'pruefung': pr}


# ------------------------------------------------------------------------------------------------ Operatoren
def ops_BA(mod, k):
    """B, A (sparse E x E) bei Bloch-Vektor k (wie ew.ops)."""
    E, eidx = mod['E'], mod['eidx']
    ph = np.exp(1j * (mod['Tcopy'] @ k))
    f = np.conj(ph)[:, :, None] * ph[:, None, :]
    rows = np.repeat(eidx[:, :, None], 6, 2).ravel()
    cols = np.repeat(eidx[:, None, :], 6, 1).ravel()
    B = sp.coo_matrix(((mod['Dl'] * f).ravel(), (rows, cols)), shape=(E, E)).tocsr()
    A = sp.coo_matrix(((mod['A0'] * f).ravel(), (rows, cols)), shape=(E, E)).tocsr()
    return B, A


def ops(mod, k):
    """B, A (sparse E x E), M (E x 3V dicht), c (E x V dicht) bei Bloch-Vektor k (wie ew.ops)."""
    E, nV = mod['E'], mod['nV']
    B, A = ops_BA(mod, k)
    phe = np.exp(1j * (mod['Tedge'] @ k))
    nl = mod['n'] / mod['l'][:, None]
    rr = np.arange(E)
    M = np.zeros((E, 3 * nV), complex)
    for c in range(3):
        np.add.at(M, (rr, 3 * mod['es2'] + c), nl[:, c] * phe)
        np.add.at(M, (rr, 3 * mod['es'] + c), -nl[:, c])
    Wh = sp.coo_matrix((np.concatenate([np.ones(E), phe]), (np.concatenate([rr, rr]), np.concatenate([mod['es'], mod['es2']]))),
                       shape=(E, nV)).tocsr()
    c = -(B @ Wh).toarray()
    return B, A, M, c


def kontr_ops(B, A, M, c):
    Bd = B.toarray()
    sB = np.abs(Bd).max()
    BM = np.abs(B @ M).max() / (sB * np.abs(M).max())
    cM = np.abs(np.conj(c.T) @ M).max() / (np.abs(c).max() * np.abs(M).max())
    Ad = A.toarray()
    return {'B_herm': float(np.abs(Bd - np.conj(Bd.T)).max() / sB), 'A_herm': float(np.abs(Ad - np.conj(Ad.T)).max() / np.abs(Ad).max()),
            'BM_null': float(BM), 'cM_null': float(cM)}


def tensor_fit(mod, a, k, M):
    """Wie ew.tensor_fit: a = sum_s x_s (n^T B6_s n) e^{i k . m_e} + M xi (Eichanteil frei), kleinste Quadrate."""
    Es = np.einsum('ei,sij,ej->es', mod['n'], tp.B6, mod['n'])
    ph = np.exp(1j * (mod['mitte'] @ k))
    X = np.concatenate([Es * ph[:, None], M], axis=1)
    x, *_ = np.linalg.lstsq(X, a, rcond=None)
    rest = float(np.linalg.norm(a - X @ x) / max(np.linalg.norm(a), 1e-300))
    H = np.einsum('a,aij->ij', x[:6], tp.B6)
    return H, rest


def klassen(w2re, w2im, eps):
    s = max(float(np.max(np.abs(w2re + 1j * w2im))), 1e-300)
    tau = TAU_REL * s
    wachs = (w2re < -tau) | (np.abs(w2im) > tau)
    masse = (~wachs) & (np.abs(w2re) <= MASSELOS_MAX * eps ** 2)
    luecke = (~wachs) & (w2re >= LUECKE_MIN * eps ** 2)
    unklar = ~(wachs | masse | luecke)
    return s, tau, wachs, masse, luecke, unklar


def punkt(mod, k, mit_tt=False, mit_kontr=False):
    """Ein Bloch-k: alle omega^2 auf der Zwangsflaeche (R1), Klassen, masselose Werte, TT-Anteil (optional)."""
    t0 = time.time()
    eps = float(np.linalg.norm(k))
    B, A, M, c = ops(mod, k)
    X = np.concatenate([M, c], 1)
    nX = X.shape[1]
    Q, R = np.linalg.qr(X, mode='complete')
    sv = np.linalg.svd(R[:nX], compute_uv=False)
    r = int((sv > 1e-9 * sv.max()).sum())
    weg = 'qr'
    if r < nX:
        U, s_, _ = np.linalg.svd(X)
        r = int((s_ > 1e-9 * s_.max()).sum())
        S = U[:, r:]
        weg = 'svd'
    else:
        S = Q[:, nX:]
    del Q
    Sh = np.conj(S.T)
    Ar = Sh @ (A @ S)
    Br = Sh @ (B @ S)
    Ar = 0.5 * (Ar + np.conj(Ar.T))
    Br = 0.5 * (Br + np.conj(Br.T))
    eB = np.linalg.eigvalsh(Br)
    z = {'eps': eps, 'rang_Mc': r, 'nX': nX, 'dim': int(S.shape[1]), 'weg': weg,
         'sv_rel_min': float(sv.min() / sv.max()),
         'B_red_neg': int((eB < -1e-9 * np.abs(eB).max()).sum()), 'B_red_min_rel': float(eB.min() / np.abs(eB).max())}
    Y = None
    try:
        La = np.linalg.cholesky(Ar)
        z['A_red_pd'] = True
        Wm = np.conj(La.T) @ Br @ La
        Wm = 0.5 * (Wm + np.conj(Wm.T))
        if mit_tt:
            w2, Y = np.linalg.eigh(Wm)
        else:
            w2 = np.linalg.eigvalsh(Wm)
        w2im = np.zeros_like(w2)
    except np.linalg.LinAlgError:
        z['A_red_pd'] = False
        eA = np.linalg.eigvalsh(Ar)
        z['A_red_neg'] = int((eA < 0).sum())
        wc = np.linalg.eigvals(Ar @ Br)
        o = np.argsort(wc.real)
        w2, w2im = wc.real[o], wc.imag[o]
    s, tau, wachs, masse, luecke, unklar = klassen(w2, w2im, eps)
    z.update({'skala': s, 'tau': tau, 'n_wachsend': int(wachs.sum()), 'n_masselos': int(masse.sum()), 'n_luecke': int(luecke.sum()),
              'n_unklar': int(unklar.sum()), 'w2_kleinste': [float(x) for x in w2[:8]], 'w2im_max': float(np.abs(w2im).max()),
              'w2_min_re': float(w2.min()), 'luecke_min': float(w2[luecke].min()) if luecke.any() else None,
              'unklar_werte': [float(x) for x in w2[unklar][:10]]})
    im = np.nonzero(masse & (w2 > tau))[0]
    im = im[np.argsort(np.abs(w2[im]))]
    z['w2k2_masselos'] = [float(w2[j] / eps ** 2) for j in sorted(im[:2], key=lambda j: w2[j])]
    if mit_tt and Y is not None:
        tt, rest = [], []
        for j in sorted(im[:2], key=lambda j: w2[j]):
            a = S @ (La @ Y[:, j])
            H, rr = tensor_fit(mod, a, k, M)
            tt.append(float(tp.tt_anteil(H, k)[0]))
            rest.append(rr)
        z['tt_anteil'] = tt
        z['fit_rest'] = rest
    if mit_kontr:
        z['kontr_ops'] = kontr_ops(B, A, M, c)
    z['t_s'] = time.time() - t0
    return z


def spektrum(mod, ridx, tt=True):
    out = []
    rl = richtungen13w()
    for i in ridx:
        nm, dvec = rl[i]
        zeile = {'ridx': int(i), 'richtung': nm, 'd': dvec.tolist()}
        ist_tt = tt and nm in TT_RICHT
        zeile['eps1'] = punkt(mod, EPS1 * dvec, mit_tt=ist_tt, mit_kontr=(i == 0))
        if ist_tt:
            zeile['eps2'] = punkt(mod, EPS2 * dvec)
        out.append(zeile)
    return out


def affin(mod):
    """Zusatz (beschreibend): Regge-Steifigkeit affiner TT-Wellen K = a^+ B a / (k^2 Vbox), a_e = n^T h n e^{i k . m_e}."""
    out = []
    for nm, dvec in richtungen13w():
        kk = EPS1 * dvec
        B, A = ops_BA(mod, kk)
        u = np.cross(dvec, [0.3, 0.5, 0.7])
        u = u / np.linalg.norm(u)
        v = np.cross(dvec, u)
        hs = [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]
        ph = np.exp(1j * (mod['mitte'] @ kk))
        av = [np.einsum('ei,ij,ej->e', mod['n'], h, mod['n']) * ph for h in hs]
        Km = np.array([[np.conj(a1) @ (B @ a2) for a2 in av] for a1 in av]) / (EPS1 ** 2 * mod['Vbox'])
        ev = np.linalg.eigvalsh(0.5 * (Km + np.conj(Km.T)))
        out.append({'richtung': nm, 'K_ueber_k2_V': ev.tolist()})
    allev = np.array([z['K_ueber_k2_V'] for z in out])
    return {'zeilen': out, 'min': float(allev.min()), 'max': float(allev.max()), 'spanne_max_min': float(allev.max() / allev.min() - 1)}


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['kontrolle', 'netz', 'affin'])
    ap.add_argument('--N', type=int, default=64)
    ap.add_argument('--saaten', default='1')
    ap.add_argument('--ridx', default='0-12', help='Richtungsindizes, z.B. 0-12 oder 0,3,9')
    ap.add_argument('--rauch', action='store_true', help='nur Schluessel und Laufzeiten speichern, keine Werte')
    ap.add_argument('--out', required=True, help='Ausgabedatei (bei mehreren Saaten: Praefix)')
    a = ap.parse_args()
    if '-' in a.ridx:
        i0, i1 = a.ridx.split('-')
        ridx = list(range(int(i0), int(i1) + 1))
    else:
        ridx = [int(x) for x in a.ridx.split(',')]
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)), 'ew_sha256': sha(os.path.abspath(ew.__file__)),
            'tp_sha256': sha(os.path.abspath(tp.__file__))}
    if a.modus == 'kontrolle':
        jobs = [('V', None)]
    else:
        jobs = [(a.N, int(s)) for s in a.saaten.split(',')]
    for (N, saat) in jobs:
        t0 = time.time()
        inf = dict(info)
        inf['start_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        if N == 'V':
            mod = modell(*netz_V())
        else:
            mod = modell(*zufallsnetz(N, saat))
        erg = {'N': N, 'saat': saat, 'pruefung': mod['pruefung']}
        if a.modus == 'affin':
            erg['affin'] = affin(mod)
        else:
            erg['ridx'] = ridx
            erg['spektrum'] = spektrum(mod, ridx)
            if a.modus == 'kontrolle':
                erg['affin'] = affin(mod)
        res = {'info': inf, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
               'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
               'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
        if a.rauch:
            tz = [z['eps1']['t_s'] for z in erg.get('spektrum', [])]
            res = {'info': inf, 'schluessel': nur_schluessel(erg), 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'],
                   't_punkt_s': tz, 't_modell_s': mod['pruefung']['t_modell_s'], 'E': mod['E'], 'nV': mod['nV'], 'T': mod['T']}
        pfad = a.out if len(jobs) == 1 else '%s-N%d-s%d.json' % (a.out, N, saat)
        schreibe(pfad, res)
        print('fertig', a.modus, N, saat, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
