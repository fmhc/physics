#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PUMPE-NETZ-1, Nachtrag nach Sicht (beschreibend, aendert kein Urteil).

Anlass: Warnung der Leitung (06:20, aus HODGE-L): Isotropie der Spannungskopplung je Richtung und Polarisation pruefen.
Nach Sicht auf H1 zusaetzlich: Haengt die Richtungsabhaengigkeit von G_rad an der TT-Spannung selbst (echte Anisotropie
der relaxierten Antwort) oder an Laengs-/Spuranteilen der nicht erhaltenen Quelle (Eichbeimischung der R1-TT-Moden)?
pn.py, ew.py, mn.py werden unveraendert importiert (eingefroren 2026-10-05 06:28:18).

Gleichfoermige Spannung T mit Wellenvektor k: Kantenkraft je Zelle sigma_e(T) = Summe_{z,p->e} Q_zp : (T - tr(T) 1)
(P1-Form, linear in T), Bloch-Amplitude sigma_e(k) = sigma_e(T) e^(i k.m_e). Statische Kopplung an die zwei weichen
Moden von B_red gegen Einstein (C_E = 4 V_Zelle^2 abs(T^TT)^2/k^2); dynamisch (J_iso) zur Kontrolle.
Aufruf: python nachtrag_iso.py --out nachtrag/iso.json
"""
import argparse, json, sys, time, platform, os, resource, hashlib, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402
import mn  # noqa: E402
import pn  # noqa: E402

LP, VCELL = pn.LP, pn.VCELL


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def Q_map(mod, tder):
    Q = np.zeros((mod['E'], 3, 3))
    for z, (K0, dK) in zip(mod['zellen'], tder):
        X0 = np.array(z['X8'], float) / 8.0
        for p, (e, T) in enumerate(z['kanten']):
            Q[e] += 0.5 * z['l'][p] * X0.T @ dK[p] @ X0
    return Q


def sigma_T(Q, T):
    M = T - np.trace(T) * np.eye(3)
    return np.einsum('eij,ij->e', Q, M)


def basis_tt(n):
    ach = np.eye(3)
    proj = [np.linalg.norm(a - n * (n @ a)) for a in ach]
    a = ach[int(np.argmax(proj))]
    e1 = a - n * (n @ a)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    hp = (np.outer(e1, e1) - np.outer(e2, e2)) / math.sqrt(2)
    hx = (np.outer(e1, e2) + np.outer(e2, e1)) / math.sqrt(2)
    L1 = (np.outer(n, e1) + np.outer(e1, n)) / math.sqrt(2)
    L2 = (np.outer(n, e2) + np.outer(e2, n)) / math.sqrt(2)
    NN = np.outer(n, n)
    PT = (np.eye(3) - NN) / math.sqrt(2)
    return {'h+': hp, 'hx': hx, 'L1': L1, 'L2': L2, 'nn': NN, 'Ptr': PT}, e1, e2


def eine_richtung(mod, Q, n, kl, mit_dyn=True):
    s = kl / LP
    k = s * n
    o = ew.ops(mod, k[None])
    B, M, c = o['B'][0], o['M'][0], o['c'][0]
    U, sv, _ = np.linalg.svd(np.concatenate([M, c], -1))
    S = U[:, 40:]
    Bred = pn.herm(np.conj(S.T) @ B @ S)
    lb, Vb = np.linalg.eigh(Bred)
    tens, e1, e2 = basis_tt(n)
    ph = np.exp(1j * (mod['mitte'] @ k))
    proj = {}
    fr = {}
    for nm, T in tens.items():
        f = -sigma_T(Q, T) * ph
        fr[nm] = np.conj(S.T) @ f
        proj[nm] = np.conj(Vb[:, :2].T) @ fr[nm]
    CE = 4 * VCELL ** 2 / s ** 2
    Pm = np.stack([proj['h+'], proj['hx']], 1)
    R = (np.conj(Pm.T) @ np.diag(1 / lb[:2]) @ Pm) / CE
    R = 0.5 * (R + np.conj(R.T))
    ev = np.linalg.eigvalsh(R)
    z = {'kl': kl, 'n': n.tolist(), 'e1': e1.tolist(), 'R_pp': float(R[0, 0].real), 'R_xx': float(R[1, 1].real),
         'R_px_abs': float(abs(R[0, 1])), 'R_eig': [float(x) for x in ev], 'R_mittel': float(0.5 * np.trace(R).real),
         'lam_weich_ueber_k2': [float(x / s ** 2) for x in lb[:2]]}
    for nm in ('L1', 'L2', 'nn', 'Ptr'):
        z['C_' + nm + '_ueber_CE'] = float((np.abs(proj[nm]) ** 2 / lb[:2]).sum() / CE)
    if mit_dyn:
        A = pn.A_J(mod, k[None], pn.J_ISO)[0]
        Ared = pn.herm(np.conj(S.T) @ A @ S)
        L = np.linalg.cholesky(Ared)
        om2, Uu = np.linalg.eigh(pn.herm(np.conj(L.T) @ Bred @ L))
        X = L @ Uu[:, :2]
        G = np.stack([np.conj(X.T) @ fr['h+'], np.conj(X.T) @ fr['hx']], 1)
        Rd = (np.conj(G.T) @ np.diag(1 / om2[:2]) @ G) / CE
        z['Rdyn_eig'] = [float(x) for x in np.linalg.eigvalsh(0.5 * (Rd + np.conj(Rd.T)))]
        z['Rdyn_mittel'] = float(0.5 * np.trace(Rd).real)
    return z


def p1_gewichte(mod, tder, seed=23):
    """Kantengewichte w_e = -Summe K0_t[i,j] (P1 = 3D-Kotangens); Zahl negativer Gewichte; Positivitaet des P1-Laplace."""
    w = np.zeros(mod['E'])
    for z, (K0, dK) in zip(mod['zellen'], tder):
        for p, ((i, j), (e, T)) in enumerate(zip(z['paare'], z['kanten'])):
            w[e] += -K0[i, j]
    rng = np.random.default_rng(seed)
    kz = rng.uniform(0, 1, (300, 3)) @ ew.BV
    Dm = np.zeros((len(kz), mod['E'], mod['nV']), complex)
    for e, (s_, s2, n2) in enumerate(mod['kliste']):
        phs = np.exp(1j * (kz @ mod['T'][e]))
        Dm[:, e, s2] += phs
        Dm[:, e, s_] -= 1.0
    Lk = np.conj(np.swapaxes(Dm, 1, 2)) @ (w[None, :, None] * Dm)
    ev = np.linalg.eigvalsh(0.5 * (Lk + np.conj(np.swapaxes(Lk, 1, 2))))
    # Gegenprobe: Summe der Tetraeder-Formen bei einem k
    return {'n_kanten': int(mod['E']), 'n_negativ': int((w < -1e-12).sum()), 'w_min': float(w.min()), 'w_max': float(w.max()),
            'laengen_der_negativen_lP': sorted(set(round(float(x) / LP, 6) for x in mod['l'][w < -1e-12])),
            'laplace_min_eig_300k': float(ev[:, 0].min()), 'laplace_max_eig_300k': float(ev[:, -1].max())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'host': platform.node(), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)), 'pn_sha256': sha(os.path.abspath(pn.__file__)),
            'ew_sha256': sha(os.path.abspath(ew.__file__)), 'mn_sha256': sha(os.path.abspath(mn.__file__))}
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = Q_map(mod, tder)
    # Kontrolle: Summe_e sigma_e(T) n_e n_e^T = -V_Zelle T fuer 6 Basis-Tensoren
    kq = 0.0
    for i in range(3):
        for j in range(i, 3):
            T = np.zeros((3, 3))
            T[i, j] = T[j, i] = 1.0
            lhs = np.einsum('e,ei,ej->ij', sigma_T(Q, T), mod['n'], mod['n'])
            kq = max(kq, float(np.abs(lhs + VCELL * T).max()))
    out = {'info': info, 'kontrolle_affin_max': kq, 'p1': p1_gewichte(mod, tder)}
    r3 = math.sqrt(3.0)
    benannt = [('100', [1, 0, 0]), ('110', [1, 1, 0]), ('111', [1, 1, 1]), ('1-1-1', [1, -1, -1]), ('-11-1', [-1, 1, -1]),
               ('-1-11', [-1, -1, 1]), ('210', [2, 1, 0]), ('211', [2, 1, 1]), ('123', [1, 2, 3]), ('001', [0, 0, 1])]
    rows = []
    for nm, v in benannt:
        n = np.array(v, float) / np.linalg.norm(v)
        for kl in (0.01, 0.1):
            z = eine_richtung(mod, Q, n, kl)
            z['name'] = nm
            rows.append(z)
    out['benannt'] = rows
    nd, wd = pn.richtungen(6, 12)
    gl = []
    for n in nd:
        gl.append(eine_richtung(mod, Q, n, 0.01, mit_dyn=False))
    Rm = np.array([z['R_mittel'] for z in gl])
    ev = np.array([z['R_eig'] for z in gl])
    out['gitter_6x12_kl001'] = {'R_mittel_winkelmittel': float((wd * Rm).sum() / wd.sum()), 'R_mittel_min': float(Rm.min()),
                                'R_mittel_max': float(Rm.max()), 'R_eig_min': float(ev.min()), 'R_eig_max': float(ev.max()),
                                'C_L_max': float(max(max(z['C_L1_ueber_CE'], z['C_L2_ueber_CE']) for z in gl)),
                                'C_nn_max': float(max(z['C_nn_ueber_CE'] for z in gl)), 'C_Ptr_max': float(max(z['C_Ptr_ueber_CE'] for z in gl))}
    out['laufzeit_s'] = time.time() - t0
    out['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(out, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_iso laufzeit %.1f s' % out['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
