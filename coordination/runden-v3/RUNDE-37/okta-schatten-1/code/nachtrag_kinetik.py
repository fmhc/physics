#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EINE-WELT-LOCH-1, Nachtrag nach dem Einfrieren (beschreibend, kein Urteil).

Frage: Haengt die Stabilitaet (EW1 gegen EW3) an der Festlegung [F] der Bewegungsenergie oder an der Reduktion?
Da B_phys positiv definit ist, ist omega^2 = eig(A_red B_phys) reell und hat die Vorzeichen von A_red (Sylvester).
Geprueft werden drei Bewegungsenergien und zwei Reduktionen:
  A1: wie im Hauptlauf (je Tetraeder (n.n)^2 - 1/2, J = 1)
  A2: volumengewichtet, J_t = V_Finn / V_t
  A3: Lagrange-Form je Tetraeder, K = sum_t (V_t/V_Finn) Phi_t^-T G^-1 Phi_t^-1, A3 = K^-1 (ohne Fuellung = A1)
  Reduktion R1: A_red = S^dagger A S (Werkzeug tp.py, Hauptlauf); R2: A_red = (S^dagger A^-1 S)^-1 (holonome Zwangsbedingung).
Benutzt ew.py (eingefroren, unveraendert) und tp.py (unveraendert).
"""
import argparse, json, sys, os, time, hashlib, platform, resource
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402
import ew  # noqa: E402


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def zell_matrizen(mod):
    """Je kinetischer Zelle: A0, A0 volumengewichtet, Lagrange-Matrix K_t."""
    vref = [z['vol'] for z in mod['zellen'] if z['art'].startswith('finn')][0]
    Ginv = np.eye(6) - np.outer(tp.TR, tp.TR)
    out = []
    for z in mod['zellen']:
        if not z['kin']:
            continue
        X = np.array(z['X8'], float) / 8.0
        nz = np.array([(X[j] - X[i]) / np.linalg.norm(X[j] - X[i]) for (i, j) in z['paare']])
        Phi = np.array([[n @ tp.B6[s] @ n for s in range(6)] for n in nz])
        Pi = np.linalg.inv(Phi)
        K = (z['vol'] / vref) * Pi.T @ Ginv @ Pi
        out.append((z, z['A0'], (vref / z['vol']) * z['A0'], K))
    return out


def assemble(mod, k, mats, welche):
    sh = k.shape[:-1]
    E = mod['E']
    A = np.zeros(sh + (E, E), complex)
    for tup in mats:
        z, Mz = tup[0], tup[welche]
        ph = [np.exp(1j * (k @ T)) for (e, T) in z['kanten']]
        idx = [e for (e, T) in z['kanten']]
        for i in range(len(idx)):
            for j in range(len(idx)):
                A[..., idx[i], idx[j]] += Mz[i, j] * np.conj(ph[i]) * ph[j]
    return A


def traegheit(H, tol=1e-9):
    e = np.linalg.eigvalsh(H)
    s = np.abs(e).max()
    return int((e < -tol * s).sum()), int((np.abs(e) <= tol * s).sum()), int((e > tol * s).sum()), float(np.abs(e).max() / max(np.abs(e).min(), 1e-300))


def analyse_k(mod, mats, k):
    o = ew.ops(mod, k[None, :])
    B, M, c = o['B'][0], o['M'][0], o['c'][0]
    U, r, s = ew.phys_basis_rr(M, c)
    S = U[:, r:]
    Bp = np.conj(S.T) @ B @ S
    res = {'B_phys': traegheit(Bp)}
    for name, w in (('A1', 1), ('A2', 2), ('A3', 3)):
        A = assemble(mod, k[None, :], mats, w)[0] if w != 3 else None
        if w == 3:
            K = assemble(mod, k[None, :], mats, 3)[0]
            res[name + '_K_voll'] = traegheit(K)
            A = np.linalg.inv(K)
        res[name + '_voll'] = traegheit(A)
        R1 = np.conj(S.T) @ A @ S
        res[name + '_R1'] = traegheit(R1)
        try:
            Ai = np.linalg.inv(A)
            R2i = np.conj(S.T) @ Ai @ S
            res[name + '_R2inv'] = traegheit(R2i)
            R2 = np.linalg.inv(R2i)
        except np.linalg.LinAlgError:
            R2 = None
        for red, Ar in (('R1', R1), ('R2', R2)):
            if Ar is None:
                continue
            w2 = np.linalg.eigvals(Ar @ Bp)
            res[name + '_' + red + '_w2'] = sorted(float(x) for x in w2.real)
            res[name + '_' + red + '_w2_im_max'] = float(np.abs(w2.imag).max())
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=8)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'ew_sha256': sha(os.path.abspath(ew.__file__)),
                    'tp_sha256': sha(os.path.abspath(tp.__file__)), 'numpy': np.__version__, 'host': platform.node(),
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}}
    g = np.arange(a.L)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    kg = (mm / a.L) @ ew.BV
    for f in ('ohne', 'V', 'S'):
        mod = ew.baue(f)
        mats = zell_matrizen(mod)
        z = {'gitter': {}, 'klein': []}
        # Gitter: Traegheiten zaehlen
        zaehl = {}
        w2min = {}
        for k in kg:
            r = analyse_k(mod, mats, k)
            for key, v in r.items():
                if isinstance(v, tuple):
                    zaehl.setdefault(key, {})
                    kk = 'neg%d_null%d' % (v[0], v[1])
                    zaehl[key][kk] = zaehl[key].get(kk, 0) + 1
                elif key.endswith('_w2'):
                    w2min[key] = min(w2min.get(key, np.inf), min(v))
        z['gitter'] = {'L': a.L, 'nk': int(len(kg)), 'traegheit_verteilung': zaehl, 'w2_min': w2min}
        # kleines k: Tempo der masselosen Moden je Variante
        for nm, d in ew.richtungen()[:3]:
            for eps in (1e-3, 2e-3):
                r = analyse_k(mod, mats, eps * d)
                zz = {'richtung': nm, 'eps': eps}
                for key, v in r.items():
                    if key.endswith('_w2'):
                        arr = np.array(v)
                        zz[key + '_masselos_ueber_k2'] = [float(x) / eps ** 2 for x in arr if abs(x) <= 1e3 * eps ** 2]
                        zz[key + '_negativ'] = int((arr < -1e-9 * np.abs(arr).max()).sum())
                        zz[key + '_kleinster_rest'] = float(min([x for x in arr if abs(x) > 1e3 * eps ** 2], default=np.nan))
                    elif isinstance(v, tuple):
                        zz[key] = v
                z['klein'].append(zz)
        res[f] = z
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
