#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZWEI-KOPIEN-1, Nachtrag nach dem Einfrieren (beschreibend, kein Urteil).
Frage: Haengt die K2-Luecke in Lesart P am Eichschnitt? Fuer jede Mode in Lesart P (K2, kappa = 0,1 und 1, 26 Richtungen,
|k| = 1e-3 und 2e-3): K2-Gehalt des P-Vertreters q_P = |F a|^2/|a|^2 und das Minimum ueber die Eichbahn
q_min = min_xi |F (a + M xi)|^2/|a|^2 (kleinste Quadrate; |a + M xi| >= |a|, weil der P-Vertreter senkrecht auf dem
Eichbild steht). zk.py (eingefroren) wird unveraendert importiert."""
import json, sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zk  # noqa: E402


def main():
    out = {'zk_sha256': zk.sha(os.path.abspath(zk.__file__)), 'tp_sha256': zk.sha(os.path.abspath(zk.tp.__file__)),
           'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    zeilen = []
    for nm, d in zk.richtungen26():
        for eps in zk.EPS:
            kk = eps * d
            o = zk.ops12(kk[None, :], 'K2')
            F = o['F1'][0]
            M = o['M'][0]
            FM = F @ M
            for kap in (0.1, 1.0):
                z = zk.spektrum_k(o, 0, kap, 'P', kk=kk)
                S, nb, r = zk.phys_raum(M, o['c'][0], o['K'][0], 'P')
                A = o['A'][0]
                B = o['B'][0] + kap * o['K'][0]
                Ar = np.conj(S.T) @ A @ S
                Br = np.conj(S.T) @ B @ S
                Ar = 0.5 * (Ar + np.conj(Ar.T))
                Br = 0.5 * (Br + np.conj(Br.T))
                w2, V = np.linalg.eig(Ar @ Br)
                o_ = np.argsort(w2.real)
                w2, V = w2[o_], V[:, o_]
                for j in range(V.shape[1]):
                    a = S @ V[:, j]
                    a = a / np.linalg.norm(a)
                    qP = float(np.linalg.norm(F @ a) ** 2)
                    xi, *_ = np.linalg.lstsq(FM, -(F @ a), rcond=None)
                    qmin = float(np.linalg.norm(F @ a + FM @ xi) ** 2)
                    zeilen.append({'richtung': nm, 'eps': eps, 'kappa': kap, 'j': j, 'w2': float(w2[j].real),
                                   'w2_ueber_k2': float(w2[j].real) / eps ** 2, 'tt': zk.tt_beide(a, kk), 'qP': qP,
                                   'qmin': qmin, 'w2_gleich_hauptlauf': abs(float(w2[j].real) - z['w2_re'][j])})
    out['zeilen'] = zeilen
    luecke = [r for r in zeilen if r['w2_ueber_k2'] > 100]
    masselos = [r for r in zeilen if r['w2_ueber_k2'] <= 100]
    out['zusammenfassung'] = {
        'n_luecke_moden': len(luecke),
        'luecke_qP_min': min([r['qP'] for r in luecke], default=None),
        'luecke_qmin_max': max([r['qmin'] for r in luecke], default=None),
        'luecke_w2_durch_kappa_qP_spanne': [min([r['w2'] / (r['kappa'] * r['qP']) for r in luecke], default=None),
                                           max([r['w2'] / (r['kappa'] * r['qP']) for r in luecke], default=None)],
        'masselos_qP_max': max([r['qP'] for r in masselos], default=None),
        'masselos_qmin_max': max([r['qmin'] for r in masselos], default=None),
        'w2_abw_hauptlauf_max': max(r['w2_gleich_hauptlauf'] for r in zeilen)}
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    p = sys.argv[1]
    with open(p + '.tmp', 'w') as f:
        json.dump(out, f, indent=0)
    os.replace(p + '.tmp', p)
    print('fertig nachtrag', json.dumps(out['zusammenfassung']), flush=True)


if __name__ == '__main__':
    main()
