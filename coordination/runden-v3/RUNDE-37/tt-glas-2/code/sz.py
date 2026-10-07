#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GLAS-2 (Runde 46, fmhc-physics), Code-Agent fuer die Leitung claude-primary. Aufgaben 2 und 3, Kontrolle TG2-0.

Lange TT-Wellen (|k| = 1e-2, 13 Wuerfelachsen wie tg.richtungen13w) mit duennbesetztem Loeser (Shift-Invert um 0).
Modellteile unveraendert aus tg.py (Netz, B, A, Eichung, skalare Regel). Varianten (PLAN.md Abschnitt 3):
  a  voll (wie TT-GLAS-1): R1, omega^2 = eig(A_red B_red) auf P = Komplement von Bild[M, c].
     Operator B_red^-1 A_red^-1, je ein KKT-System [[H, X], [X^+, 0]] (H = A bzw. B, X = [M, c]), splu.
  b  affin eingefroren (nur Bewegungsenergie): Rayleigh-Ritz des R1-Modells auf Z = Pi [a_h1, a_h2]
     (affine TT-Wellen, auf P projiziert); Lagrange-Masse G = A_red^-1; omega^2 = eig(Z^+ G Z, Z^+ B Z).
  c  isotrope Ersatzmasse (nur Relaxation): Lagrange-Masse K3 = sum_t (V_t / mittleres V) Phi_t^-T (1 - TR TR^T) Phi_t^-1
     (A3 aus EINE-WELT-LOCH-1/TT-ISO-1), Reduktion R2 (q in P): omega^2 = eig(K3_red^-1 B_red); Operator B_red^-1 K3.
  d  Kontrolle zu c: Rayleigh-Ritz von c auf Z.
  e  [M] unprojiziert: a_h^+ B a_h und a_h^+ K3 a_h (vorab isotrop, Pruefung).
"""
import argparse, json, os, sys, time, hashlib, platform, resource
import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402  (TT-GLAS-1, unveraendert)
import tp  # noqa: E402

NEV = 6
NCV = 24
TOL = 1e-11
GINV = np.eye(6) - np.outer(tp.TR, tp.TR)   # |h|^2 - (tr h)^2 in der B6-Basis


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def ops_sparse(mod, k):
    """B, A (wie tg.ops_BA), M und c duenn besetzt (gleiche Eintraege wie tg.ops)."""
    E, nV = mod['E'], mod['nV']
    B, A = tg.ops_BA(mod, k)
    phe = np.exp(1j * (mod['Tedge'] @ k))
    nl = mod['n'] / mod['l'][:, None]
    rr = np.arange(E)
    rows = np.concatenate([np.repeat(rr, 3), np.repeat(rr, 3)])
    cols = np.concatenate([(3 * mod['es2'][:, None] + np.arange(3)[None, :]).ravel(),
                           (3 * mod['es'][:, None] + np.arange(3)[None, :]).ravel()])
    vals = np.concatenate([(nl * phe[:, None]).ravel(), (-nl).ravel()])
    M = sp.coo_matrix((vals, (rows, cols)), shape=(E, 3 * nV)).tocsr()
    Wh = sp.coo_matrix((np.concatenate([np.ones(E), phe]), (np.concatenate([rr, rr]), np.concatenate([mod['es'], mod['es2']]))),
                       shape=(E, nV)).tocsr()
    c = -(B @ Wh)
    return B.tocsr(), A.tocsr(), M, sp.csr_matrix(c)


def k3_tetra(mod, X):
    """Lagrange-Masse A3 je Tetraeder (T,6,6): (V_t / mittleres V) Phi_t^-T (1 - TR TR^T) Phi_t^-1."""
    et = np.stack([X[:, j] - X[:, i] for (i, j, _, _) in tg.PAARE], 1)
    nt = et / np.linalg.norm(et, axis=2)[..., None]
    Phi = np.einsum('tpi,sij,tpj->tps', nt, tp.B6, nt)
    Pi = np.linalg.inv(Phi)
    vol = np.abs(np.linalg.det(X[:, 1:] - X[:, :1])) / 6.0
    w = vol / vol.mean()
    K = w[:, None, None] * np.einsum('tsp,su,tuq->tpq', Pi, GINV, Pi)
    return K, {'phi_cond_max': float(np.linalg.cond(Phi).max()), 'K3_absmax': float(np.abs(K).max())}


def assemble(mod, Kt, k):
    E, eidx = mod['E'], mod['eidx']
    ph = np.exp(1j * (mod['Tcopy'] @ k))
    f = np.conj(ph)[:, :, None] * ph[:, None, :]
    rows = np.repeat(eidx[:, :, None], 6, 2).ravel()
    cols = np.repeat(eidx[:, None, :], 6, 1).ravel()
    return sp.coo_matrix(((Kt * f).ravel(), (rows, cols)), shape=(E, E)).tocsr()


class KKT:
    def __init__(self, H, X):
        self.E, self.n4 = X.shape
        Kk = sp.bmat([[H, X], [X.conj().T, None]], format='csc')
        t0 = time.time()
        self.lu = spla.splu(Kk, permc_spec='MMD_AT_PLUS_A')
        self.t = time.time() - t0
        self.nnz = int(self.lu.L.nnz + self.lu.U.nnz)
        self.n_solve = 0

    def solve(self, y):
        self.n_solve += 1
        r = np.concatenate([y, np.zeros(self.n4, complex)])
        return self.lu.solve(r)[:self.E]


def eig_si(matvec, E, v0, nev=NEV):
    Lop = spla.LinearOperator((E, E), matvec=matvec, dtype=complex)
    vals, vecs = spla.eigs(Lop, k=nev, which='LM', v0=v0, ncv=NCV, tol=TOL, maxiter=10000)
    w2 = 1.0 / vals
    o = np.argsort(w2.real)
    return w2[o], vecs[:, o]


def klass(w2, eps):
    """Klassen der gefundenen (betragskleinsten) Werte: masselos, Luecke, negativ, komplex."""
    re, im = w2.real, w2.imag
    kompl = np.abs(im) > 1e-6 * np.abs(w2)
    neg = (~kompl) & (re < -1e-6 * eps ** 2)
    masse = (~kompl) & (~neg) & (np.abs(re) <= 30 * eps ** 2) & (re > 0)
    luecke = (~kompl) & (re >= 100 * eps ** 2)
    unklar = ~(kompl | neg | masse | luecke)
    return {'n_masselos': int(masse.sum()), 'n_luecke': int(luecke.sum()), 'n_negativ': int(neg.sum()),
            'n_komplex': int(kompl.sum()), 'n_unklar': int(unklar.sum()), 'masse': masse}


def ritz(Kz, Gz):
    """2x2 Rayleigh-Ritz: Eigenwerte von Gz^-1 Kz (Steifigkeit Kz, Masse Gz), aufsteigend; Real- und Imaginaerteil."""
    Kz = 0.5 * (Kz + Kz.conj().T)
    Gz = 0.5 * (Gz + Gz.conj().T)
    w = np.linalg.eigvals(np.linalg.solve(Gz, Kz))
    w = w[np.argsort(w.real)]
    return [float(x) for x in w.real], float(np.abs(w.imag).max()), [float(x) for x in np.linalg.eigvalsh(Gz)]


def affin_wellen(mod, kk, dvec):
    """Die zwei affinen TT-Wellen wie tg.affin (Frobenius-Norm 1)."""
    u = np.cross(dvec, [0.3, 0.5, 0.7])
    u = u / np.linalg.norm(u)
    v = np.cross(dvec, u)
    hs = [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]
    ph = np.exp(1j * (mod['mitte'] @ kk))
    return np.stack([np.einsum('ei,ij,ej->e', mod['n'], h, mod['n']) * ph for h in hs], 1)


def punkt(mod, K3t, kk, varianten, rng):
    t0 = time.time()
    eps = float(np.linalg.norm(kk))
    dvec = kk / eps
    E = mod['E']
    B, A, M, c = ops_sparse(mod, kk)
    X = sp.hstack([M, c]).tocsr()
    z = {'eps': eps}
    kb = KKT(B, X)
    v0 = rng.standard_normal(E) + 1j * rng.standard_normal(E)
    if 'a' in varianten or 'b' in varianten:
        ka = KKT(A, X)
    if 'a' in varianten:
        w2, vec = eig_si(lambda y: kb.solve(ka.solve(y)), E, v0)
        kl = klass(w2, eps)
        im = np.nonzero(kl.pop('masse'))[0]
        im = im[np.argsort(np.abs(w2.real[im]))][:2]
        im = sorted(im, key=lambda j: w2.real[j])
        z['a'] = {'w2': [float(x) for x in w2.real], 'w2im': [float(x) for x in w2.imag],
                  'w2k2_masselos': [float(w2.real[j] / eps ** 2) for j in im], **kl}
        # Residuum der TT-Moden im Originalproblem: A_red B_red x = w2 x
        res_ = []
        for j in im:
            x = vec[:, j]
            y = ka.solve(x)          # A_red^-1 x
            yb = kb.solve(y)         # B_red^-1 A_red^-1 x  = x / w2
            res_.append(float(np.linalg.norm(yb - x / w2[j]) / np.linalg.norm(x / w2[j])))
        z['a']['residuum'] = res_
    if 'b' in varianten or 'd' in varianten or 'e' in varianten:
        ah = affin_wellen(mod, kk, dvec)
        ki = KKT(sp.identity(E, dtype=complex, format='csr'), X)
        Z = np.stack([ki.solve(ah[:, j]) for j in range(2)], 1)     # Pi a_h
        BZ = B @ Z
        Kz = Z.conj().T @ BZ
        z['proj_anteil_weg'] = [float(np.linalg.norm(ah[:, j] - Z[:, j]) / np.linalg.norm(ah[:, j])) for j in range(2)]
        z['Bz_k2V'] = [float(x) for x in np.linalg.eigvalsh(0.5 * (Kz + Kz.conj().T)) / (eps ** 2 * mod['Vbox'])]
    if 'b' in varianten:
        GZ = np.stack([ka.solve(Z[:, j]) for j in range(2)], 1)       # A_red^-1 Z
        Gz = Z.conj().T @ GZ
        w, wim, gev = ritz(Kz, Gz)
        z['b'] = {'w2k2': [x / eps ** 2 for x in w], 'w2im_max': wim, 'masse_ev': gev}
    if 'c' in varianten or 'd' in varianten or 'e' in varianten:
        K3 = assemble(mod, K3t, kk)
    if 'c' in varianten:
        w2, vec = eig_si(lambda y: kb.solve(K3 @ y), E, v0)
        kl = klass(w2, eps)
        im = np.nonzero(kl.pop('masse'))[0]
        im = im[np.argsort(np.abs(w2.real[im]))][:2]
        im = sorted(im, key=lambda j: w2.real[j])
        z['c'] = {'w2': [float(x) for x in w2.real], 'w2im': [float(x) for x in w2.imag],
                  'w2k2_masselos': [float(w2.real[j] / eps ** 2) for j in im], **kl}
    if 'd' in varianten:
        Gd = Z.conj().T @ (K3 @ Z)
        w, wim, gev = ritz(Kz, Gd)
        z['d'] = {'w2k2': [x / eps ** 2 for x in w], 'w2im_max': wim, 'masse_ev': gev}
    if 'e' in varianten:
        Ke = ah.conj().T @ (B @ ah)
        Ge = ah.conj().T @ (K3 @ ah)
        w, wim, gev = ritz(Ke, Ge)
        z['e'] = {'w2k2': [x / eps ** 2 for x in w], 'w2im_max': wim, 'masse_ev': gev,
                  'B_k2V': [float(x) for x in np.linalg.eigvalsh(0.5 * (Ke + Ke.conj().T)) / (eps ** 2 * mod['Vbox'])]}
    z['lu'] = {'t_B': kb.t, 'nnz_B': kb.nnz, 'solves_B': kb.n_solve}
    if 'a' in varianten or 'b' in varianten:
        z['lu'].update({'t_A': ka.t, 'nnz_A': ka.nnz, 'solves_A': ka.n_solve})
    z['t_s'] = time.time() - t0
    return z


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
    ap.add_argument('--N', type=int, required=True)
    ap.add_argument('--saaten', default='1')
    ap.add_argument('--ridx', default='0-12')
    ap.add_argument('--varianten', default='a,b,c,d,e')
    ap.add_argument('--lin', action='store_true', help='Linearitaet: zusaetzlich |k| = 2e-2 an [100], [110], [111] (nur a)')
    ap.add_argument('--frist', type=float, default=540.0)
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--out', required=True, help='Ausgabedatei (bei mehreren Saaten: Praefix)')
    a = ap.parse_args()
    t_start = time.time()
    varianten = set(a.varianten.split(','))
    if '-' in a.ridx:
        i0, i1 = a.ridx.split('-')
        ridx = list(range(int(i0), int(i1) + 1))
    else:
        ridx = [int(x) for x in a.ridx.split(',')]
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)), 'tg_sha256': sha(os.path.abspath(tg.__file__)),
            'tp_sha256': sha(os.path.abspath(tp.__file__)), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    saaten = [int(s) for s in a.saaten.split(',')]
    rl = tg.richtungen13w()
    for saat in saaten:
        t0 = time.time()
        rng = np.random.default_rng([2046, a.N, saat])
        LV, pos, G, O, pr = tg.zufallsnetz(a.N, saat)
        mod = tg.modell(LV, pos, G, O, pr)
        Xg = pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)
        K3t, k3pr = k3_tetra(mod, Xg)
        zeilen = []
        abgebrochen = False
        for i in ridx:
            if time.time() - t_start > a.frist:
                abgebrochen = True
                break
            nm, dvec = rl[i]
            zl = {'ridx': i, 'richtung': nm, 'd': dvec.tolist(), 'eps1': punkt(mod, K3t, tg.EPS1 * dvec, varianten, rng)}
            if a.lin and nm in tg.TT_RICHT and 'a' in varianten:
                zl['eps2'] = punkt(mod, K3t, tg.EPS2 * dvec, {'a'}, rng)
            zeilen.append(zl)
        erg = {'N': a.N, 'saat': saat, 'ridx_geplant': ridx, 'ridx_fertig': [z['ridx'] for z in zeilen], 'abgebrochen_frist': abgebrochen,
               'varianten': sorted(varianten), 'zeilen': zeilen, 'pruefung': mod['pruefung'], 'k3': k3pr,
               'E': mod['E'], 'nV': mod['nV'], 'T': mod['T'], 'Vbox': mod['Vbox']}
        res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
               'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
               'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
        if a.rauch:
            res = {'info': info, 'schluessel': nur_schluessel(erg), 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'],
                   't_punkt_s': [z['eps1']['t_s'] for z in zeilen], 'lu': [z['eps1']['lu'] for z in zeilen],
                   'abgebrochen_frist': abgebrochen, 'E': mod['E'], 'nV': mod['nV'], 'T': mod['T']}
        pfad = a.out if len(saaten) == 1 else '%s-N%d-s%d.json' % (a.out, a.N, saat)
        schreibe(pfad, res)
        print('fertig sz N=%d saat=%d richtungen=%d laufzeit %.1f s' % (a.N, saat, len(zeilen), time.time() - t0), flush=True)
        if abgebrochen:
            break


if __name__ == '__main__':
    main()
