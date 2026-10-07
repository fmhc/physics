#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PACHNER-TAKT-1, Nachtrag nach dem Einfrieren (beschreibend, kein Urteil).
Ganzes Singulaerwertspektrum von Omega~ fuer m-Takt-Schichten: Gibt es bei E - G eine Luecke, auch wenn die feste
Schwelle 1e-9 im Hauptlauf mitten durch einen glatten Auslauf schnitt? Benutzt das eingefrorene pt.py unveraendert."""
import sys, os, json, time, hashlib
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pt


def spektrum(variante, n, m):
    nz = pt.Netz(n, 'klasse', variante)
    sig0 = set(nz.sigma)
    for _ in range(m):
        nz.takt(variante)
    sch = pt.Schicht(nz, sig0, set(nz.sigma))
    geo = pt.geometrie(sch.Xs)
    H = sch.hesse(geo)
    inn, e0, eT = sch.inn, sch.e0, sch.eT
    w, U = np.linalg.eigh(H[np.ix_(inn, inn)])
    nz_ = np.abs(w) > 1e-10 * np.abs(w).max()
    Unz = U[:, nz_]
    Q = H[np.ix_(e0, eT)] - (H[np.ix_(e0, inn)] @ Unz) @ ((Unz.T @ H[np.ix_(inn, eT)]) / w[nz_][:, None])
    s = np.linalg.svd(Q, compute_uv=False)
    s = s / s[0]
    G = int(np.linalg.matrix_rank(sch.eich(sch.v0, e0)))
    EG = len(e0) - G
    q = s[:-1] / np.maximum(s[1:], 1e-300)
    i_max = int(np.argmax(q))
    return {'variante': variante, 'n': n, 'm': m, 'E': len(e0), 'G': G, 'E_minus_G': EG,
            'anzahl_ueber': {str(t): int((s > t).sum()) for t in (1e-6, 1e-8, 1e-9, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14)},
            'groesste_luecke_nach_index': i_max + 1, 'groesste_luecke_faktor': float(q[i_max]),
            's_um_EG': [float(x) for x in s[max(0, EG - 6):EG + 6]],
            's_kleinste_physikalisch': float(s[EG - 1]), 's_erste_eich': float(s[EG]) if EG < len(s) else None}


def main():
    out = {'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           'pt_sha256': hashlib.sha256(open(pt.__file__, 'rb').read()).hexdigest(), 'faelle': []}
    for var, n, m in (('TT', 2, 3), ('C2', 2, 3), ('C3', 2, 3), ('C2', 2, 2), ('C2', 3, 3), ('C3', 3, 3)):
        out['faelle'].append(spektrum(var, n, m))
        print('spektrum', var, n, m, 'fertig', flush=True)
    out['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(sys.argv[1] + '.tmp', 'w') as f:
        json.dump(out, f, indent=1)
    os.replace(sys.argv[1] + '.tmp', sys.argv[1])


if __name__ == '__main__':
    main()
