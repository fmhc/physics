#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IMPULS-NETZ-1, Nachtrag auf Bitte der Leitung (08:1x, nach TAKT-UMKLAPP-1): beschreibender Nebenarm, kein Urteil.

Dieselbe Rechnung wie inz.py, aber die Materie-Energie je Tetraeder mit umkreisbasierten Hodge-Gewichten *1 statt P1
(3D-Kotangens). Gewicht der Kante e = (i, j) im Tetraeder t (k, l die beiden anderen Ecken):
  w_e^t = (1/4) Summe_{m in (k, l)} cot(Winkel bei o im Dreieck (o, i, j)) beta_m 3 V_t/A_m,   o = die andere von k, l,
  beta = baryzentrische Koordinaten der Umkugelmitte, A_m = Flaeche gegenueber m (also (i, j, o)).
  Probe von Hand: Ecktetraeder (0, e1, e2, e3): Kante 0-e1 -> 1/4 (P1: 1/6), Kante e1-e2 -> -1/24 (P1: 0).
Umsetzung: pn.K_aus_laengen wird NUR in diesem Prozess durch K_umkreis ersetzt (Dateien unveraendert); dann laufen
inz.lauf (8 x 16 Richtungen) und inz.zusatz wie eingefroren. Eckvolumina (V1, J) bleiben baryzentrisch wie in inz.py.
Aufruf: python nachtrag_umkreis.py --out nachtrag/umkreis.json
"""
import argparse, json, sys, time, platform, os, resource, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402
import pn  # noqa: E402
import inz  # noqa: E402
import nachtrag_iso as ni  # noqa: E402

K_P1 = pn.K_aus_laengen


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def K_umkreis(paare, lv):
    """Umkreisbasierte *1-Form eines Tetraeders aus 6 Kantenlaengen (komplex erlaubt): E = (1/2) phi^T K phi."""
    L2 = {}
    for p, (i, j) in enumerate(paare):
        L2[(i, j)] = lv[p] ** 2
        L2[(j, i)] = lv[p] ** 2
    for i in range(4):
        L2[(i, i)] = 0.0 * lv[0]
    g = np.zeros((3, 3), complex)
    for a in range(1, 4):
        for b in range(1, 4):
            g[a - 1, b - 1] = 0.5 * (L2[(0, a)] + L2[(0, b)] - L2[(a, b)])
    V = np.sqrt(np.linalg.det(g)) / 6.0
    lam = 0.5 * np.linalg.solve(g, np.diag(g).copy())
    beta = np.concatenate([[1.0 - lam.sum()], lam])
    K = np.zeros((4, 4), complex)
    for (i, j) in paare:
        k, l = [m for m in range(4) if m not in (i, j)]
        w = 0.0
        for m, o in ((k, l), (l, k)):
            uu, vv = L2[(o, i)], L2[(o, j)]
            uv = 0.5 * (L2[(o, i)] + L2[(o, j)] - L2[(i, j)])
            A = 0.5 * np.sqrt(uu * vv - uv * uv)
            w = w + (uv / (2.0 * A)) * beta[m] * 3.0 * V / A
        w = 0.25 * w
        K[i, i] += w
        K[j, j] += w
        K[i, j] -= w
        K[j, i] -= w
    return K


def proben():
    """Ecktetraeder und regulaeres Tetraeder: Gewichte P1 gegen umkreisbasiert."""
    paare = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    out = {}
    for nm, X in (('ecke', np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]], float)),
                  ('regulaer', np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float))):
        lv = np.array([np.linalg.norm(X[j] - X[i]) for (i, j) in paare]).astype(complex)
        Kp = np.real(K_P1(paare, lv))
        Ku = np.real(K_umkreis(paare, lv))
        V = abs(np.linalg.det(X[1:] - X[0])) / 6.0
        out[nm] = {'w_P1': [float(-Kp[i, j]) for (i, j) in paare], 'w_umkreis': [float(-Ku[i, j]) for (i, j) in paare],
                   'summe_l2w_P1_ueber_3V': float(sum(-Kp[i, j] * abs(lv[p]) ** 2 for p, (i, j) in enumerate(paare)) / (3 * V)),
                   'summe_l2w_umkreis_ueber_3V': float(sum(-Ku[i, j] * abs(lv[p]) ** 2 for p, (i, j) in enumerate(paare)) / (3 * V))}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'host': platform.node(), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)), 'inz_sha256': sha(os.path.abspath(inz.__file__)),
            'pn_sha256': sha(os.path.abspath(pn.__file__))}
    out = {'info': info, 'proben': proben()}
    mod = ew.baue('V')
    tder_p1 = pn.tet_ableitungen(mod)
    out['gewichte_P1'] = ni.p1_gewichte(mod, tder_p1)
    pn.K_aus_laengen = K_umkreis                      # nur in diesem Prozess
    tder_u = pn.tet_ableitungen(mod)
    out['gewichte_umkreis'] = ni.p1_gewichte(mod, tder_u)
    # gleichfoermige Spannung: Summe sigma_e n_e n_e^T gegen -V_Zelle T (je Basis-Tensor), umkreisbasiert
    Q = ni.Q_map(mod, tder_u)
    dev = []
    for i in range(3):
        for j in range(i, 3):
            T = np.zeros((3, 3))
            T[i, j] = T[j, i] = 1.0
            lhs = np.einsum('e,ei,ej->ij', ni.sigma_T(Q, T), mod['n'], mod['n'])
            dev.append(float(np.abs(lhs + pn.VCELL * T).max()))
    out['kontrolle_affin_umkreis_max'] = max(dev)
    out['kontrolle_affin_umkreis_je_tensor'] = dev
    r = inz.lauf(nt=8, nphi=16)
    out['lauf'] = {'G_rad_ueber_G_N_kl001': r['G_rad_ueber_G_N_kl001'], 'kontrollen': r['kontrollen'], 'G_N_ueber_G': r['G_N_ueber_G'],
                   'quellen': r['quellen'], 'c0': r['c0'],
                   'tabelle_iso': {q: [{k: z[k] for k in ('kl', 'P_S_ueber_P_E', 'P_V1S_ueber_P_E', 'P_SJ_ueber_P_E', 'P_V1SJ_ueber_P_E')}
                                       for z in zeilen if z['kl'] <= 0.3] for q, zeilen in r['tabelle']['iso'].items()}}
    z = inz.zusatz()
    out['zusatz'] = {k: z[k] for k in ('KE_max_rel', 'isotropie_gitter_kl001', 'kreisbahnen_kl001')}
    out['zusatz']['isotropie_benannt_kl001'] = [{'name': x['name'], 'ohneJ': x['ohneJ'], 'mitJ': x['mitJ']}
                                                 for x in z['isotropie_benannt'] if x['kl'] == 0.01]
    out['laufzeit_s'] = time.time() - t0
    out['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(out, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_umkreis laufzeit %.1f s' % out['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
