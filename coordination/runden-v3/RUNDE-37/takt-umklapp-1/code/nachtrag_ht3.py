#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TAKT-UMKLAPP-1, NACHTRAG nach dem Einfrieren (beschreibend, aendert kein Urteil).
Anlass: In Lauf A4 verletzt uk-N256-s2-f0.2 bei klein-100-1 die Traegheitsidentitaet um 1; dort zaehlte die
eingefrorene Schwelle (1e-9 max|lambda|) 3V + 1 Eigenwerte von B als null (groesster "null"-Wert 6,7e-10 relativ).
Hier: alle Eigenwerte von B, P, B_red an diesem Punkt (und an zufall-0 zum Vergleich), Zaehlung mit der eingefrorenen
Schwelle und mit einer Schwelle in der Luecke ueber den 3V Eichnullen (10 x groesster der 3V kleinsten |lambda(B)|).
tu.py, tg.py, uk.py unveraendert importiert."""
import argparse, json, os, sys, time, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import tu  # noqa: E402


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def zaehle(ev, tol):
    return {'neg': int((ev < -tol).sum()), 'null': int((np.abs(ev) <= tol).sum()), 'pos': int((ev > tol).sum())}


def punkt(mod, name_k, k):
    B, A, M, c = tg.ops(mod, k)
    Bd = B.toarray()
    Bd = 0.5 * (Bd + Bd.conj().T)
    eB = np.linalg.eigvalsh(Bd)
    sB = np.abs(eB).max()
    nV, E = mod['nV'], mod['E']
    o = np.argsort(np.abs(eB))
    g_max = np.abs(eB[o[3 * nV - 1]])
    tol_l = 10.0 * g_max
    W = np.zeros((E, nV), complex)
    rr = np.arange(E)
    np.add.at(W, (rr, mod['es']), 1.0)
    np.add.at(W, (rr, mod['es2']), np.exp(1j * (mod['Tedge'] @ k)))
    P = -(W.conj().T @ (Bd @ W))
    eP = np.linalg.eigvalsh(0.5 * (P + P.conj().T))
    X = np.concatenate([M, c], 1)
    Q, R = np.linalg.qr(X, mode='complete')
    S = Q[:, X.shape[1]:]
    Br = S.conj().T @ (Bd @ S)
    eBr = np.linalg.eigvalsh(0.5 * (Br + Br.conj().T))
    z = {'k': name_k, 'max_abs_B': float(sB), 'eich_null_groesst_abs': float(g_max),
         'B_um_3V_rel': [float(eB[o[j]] / sB) for j in range(3 * nV - 2, 3 * nV + 4)],
         'B_eingefroren': zaehle(eB, 1e-9 * sB), 'B_luecke': zaehle(eB, tol_l), 'tol_luecke_rel': float(tol_l / sB),
         'P_eingefroren': zaehle(eP, 1e-9 * np.abs(eP).max()), 'P_kleinst_abs_rel': float(np.abs(eP).min() / np.abs(eP).max()),
         'Bred_eingefroren': zaehle(eBr, 1e-9 * np.abs(eBr).max()), 'Bred_kleinst_abs_rel': float(np.abs(eBr).min() / np.abs(eBr).max()),
         'Bred_luecke': zaehle(eBr, tol_l)}
    z['identitaet_luecke'] = z['B_luecke']['neg'] == z['P_eingefroren']['pos'] + z['Bred_luecke']['neg']
    return z


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--netz', default='uk-N256-s2-f0.2')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    LV, pos, G, O, pr, info = tu.netz_bauen(a.netz)
    mod = tg.modell(LV, pos, G, O, pr)
    ks = tu.k_satz(LV, 4, 20, 2)
    sel = [x for x in ks if x[0] in ('klein-100-1', 'zufall-0')]
    res = {'info': {'skript_sha256': sha(os.path.abspath(__file__)), 'tu_sha256': sha(os.path.abspath(tu.__file__)),
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}, 'netz': a.netz, 'zuege': info.get('zuege'),
           'punkte': [punkt(mod, nm, k) for nm, k in sel]}
    res['laufzeit_s'] = time.time() - t0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    tg.schreibe(a.out, res)
    print('fertig nachtrag ht3', a.netz, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
