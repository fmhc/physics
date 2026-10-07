#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GRUND-1, Nachtrag nach Sicht (beschreibend, kein Urteil), geschrieben nach dem Lesen von karte-V.json und
profil-S-V.json.

Anlass: Die eingefrorene Wortlaut-Regel (PLAN 2: "Wortlaut-gueltig: jeder endliche Wert") zaehlt negative
"Spannen" max/min - 1 mit. Sie entstehen an ungueltigen Punkten, an denen die zwei betragsgroessten 1/omega^2 nicht
beide positiv sind; dort ist max/min - 1 keine Spanne. Dieser Nachtrag zaehlt die Wortlaut-Menge mit der
Zusatzbedingung Spanne >= 0 neu, nur aus den gespeicherten Dateien (keine neue Physik-Rechnung).
"""
import json, sys, hashlib, time
import numpy as np


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def komponenten(B):
    lab = np.zeros(B.shape, int)
    n, gr = 0, []
    for i0, j0 in zip(*np.nonzero(B)):
        if lab[i0, j0]:
            continue
        n += 1
        st = [(i0, j0)]
        lab[i0, j0] = n
        g = 0
        while st:
            i, j = st.pop()
            g += 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + di, j + dj
                if 0 <= a < B.shape[0] and 0 <= b < B.shape[1] and B[a, b] and not lab[a, b]:
                    lab[a, b] = n
                    st.append((a, b))
        gr.append(int(g))
    return {'anzahl': int(n), 'groessen': sorted(gr, reverse=True)[:10]}


def main():
    karte, profile, out = sys.argv[1], sys.argv[2:-1], sys.argv[-1]
    K = json.load(open(karte))['ergebnis']
    W = np.array([[np.nan if v is None else v for v in r] for r in K['spanne_wort']], float)
    P = np.array([[np.nan if v is None else v for v in r] for r in K['spanne_plan']], float)
    n = W.shape[0]
    res = {'info': {'karte_sha256': sha(karte), 'profile_sha256': {p: sha(p) for p in profile},
                    'skript_sha256': sha(__file__), 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}}
    res['n_wort_negativ'] = int(np.sum(W < 0))
    res['n_wort_null_bis_1e-4'] = int(np.sum((W >= 0) & (W < 1e-4)))
    res['n_plan_unter_1e-4'] = int(np.sum(P < 1e-4))
    res['n_wort_nichtneg_unter_1e-4_aber_plan_ungueltig'] = int(np.sum((W >= 0) & (W < 1e-4) & ~np.isfinite(P)))
    B = (W >= 0) & (W < 1e-4)
    blk = np.ones((n - 2, n - 2), bool)
    for di in range(3):
        for dj in range(3):
            blk &= B[di:n - 2 + di, dj:n - 2 + dj]
    res['block3_wort_nichtneg'] = int(blk.sum())
    res['komponenten_wort_nichtneg'] = komponenten(B)
    Bn = W < 0
    blkn = np.ones((n - 2, n - 2), bool)
    for di in range(3):
        for dj in range(3):
            blkn &= Bn[di:n - 2 + di, dj:n - 2 + dj]
    res['block3_nur_negativ'] = int(blkn.sum())
    pr = {}
    for p in profile:
        Pr = json.load(open(p))['ergebnis']
        z_w = [z for z in Pr['zeilen'] if z.get('min_wort')]
        pr[Pr['achse']] = {'n_zeilen': len(Pr['zeilen']), 'n_zeilen_mit_min_wort': len(z_w),
                           'n_min_wort_negativ': sum(1 for z in z_w if z['min_wort']['spanne'] < 0),
                           'n_min_wort_nichtneg': sum(1 for z in z_w if z['min_wort']['spanne'] >= 0)}
    res['profile'] = pr
    with open(out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1)
    import os
    os.replace(out + '.tmp', out)
    print('fertig nachtrag_wortlaut', flush=True)


if __name__ == '__main__':
    main()
