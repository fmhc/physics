#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TENSOR-EIS-PYRO-1, Nachtrag nach dem Einfrieren (beschreibend, kein Urteil).
Grund: Der Hauptlauf SP zeigt auf Finns Netz einen Spur-Eichdefekt von 0,27 auch am kleinsten Gitter-k. Frage: Geht er
fuer k -> 0 gegen null (Gitterkorrektur), oder enthaelt die Regge-Skalarregel schon in fuehrender Ordnung einen
richtungsabhaengigen TT-Anteil? Benutzt nur Funktionen aus dem eingefrorenen tp.py (unveraendert)."""
import sys, os, json, time, hashlib
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def zerlege(S, k):
    kh = k / np.linalg.norm(k)
    P = np.eye(3) - np.outer(kh, kh)
    tPS = np.trace(P @ S)
    Stt = P @ S @ P - 0.5 * P * tPS
    ntt = float(np.sum(np.abs(Stt) ** 2))
    nt = float(abs(tPS) ** 2 / 2.0)
    nl = float(np.linalg.norm(S @ kh))
    return ntt / max(ntt + nt, 1e-300), nl / max(np.linalg.norm(S), 1e-300)


def main():
    out = {'tp_sha256': sha(tp.__file__), 'skript_sha256': sha(os.path.abspath(__file__)),
           'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    richt = [('100', [1, 0, 0]), ('110', [1, 1, 0]), ('111', [1, 1, 1]), ('z', [0.3, 0.5, 0.81])]
    for name in ('pyro1', 'kubisch'):
        z = {}
        for nm, d in richt:
            d = np.array(d, float) / np.linalg.norm(d)
            rows = []
            for eps in (3e-1, 1e-1, 3e-2, 1e-2, 3e-3, 1e-3):
                k = eps * d
                o = tp.ops(name, k[None, :])
                A, B, M, c = o['A'][0], o['B'][0], o['M'][0], o['c'][0]
                Q, _ = np.linalg.qr(M)
                Ac = A @ c
                rest = Ac - Q @ (np.conj(Q.T) @ Ac)
                defekt = float(np.linalg.norm(rest) / np.linalg.norm(Ac))
                # Skalarregel als Tensor-Funktional s:H auf glatten Verzerrungen H
                if name == 'kubisch':
                    s = np.conj(c)
                else:
                    Es = np.array([[tp.NM[m] @ tp.B6[q] @ tp.NM[m] for q in range(6)] for m in range(6)])
                    ph = np.exp(0.5j * (tp.BM @ k))
                    s = np.conj(c) @ (ph[:, None] * Es)
                S = np.einsum('a,aij->ij', s, tp.B6)
                tt, laengs = zerlege(S, k)
                rows.append({'eps': eps, 'spur_eichdefekt': defekt, 'skalarregel_tt_anteil': tt, 'skalarregel_laengs_rel': laengs})
            z[nm] = rows
        out[name] = z
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(sys.argv[1] + '.tmp', 'w') as f:
        json.dump(out, f, indent=1)
    os.replace(sys.argv[1] + '.tmp', sys.argv[1])
    print('fertig nachtrag', flush=True)


if __name__ == '__main__':
    main()
