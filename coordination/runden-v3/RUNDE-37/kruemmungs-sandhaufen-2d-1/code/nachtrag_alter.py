#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KRUEMMUNGS-SANDHAUFEN-2D-1, NACHTRAG NACH SICHT (nur beschreibend, kein Urteil).

Anlass: Die Scheibe (Arm Z) driftet (z = 5,6 bei N = 8000; Randgrad steigt, mittleres s faellt). Die drei N hatten
verschieden lange Antriebszeiten in Einheiten von N (Einschwingen 10 N, Messung 300 000 Schritte = 600 N, 150 N, 37,5 N).
Hier: s_c2 = <s^2>/<s> in gleichen Altersfenstern (Alter = Schritte seit Antriebsbeginn / N) und D daraus,
Block-Bootstrap wie im eingefrorenen Plan (20 Bloecke, 200 Ziehungen), dazu mittleres s je Viertel der Messung.

Aufruf nur ueber kleintest.sh auf der .69:
  python nachtrag_alter.py --ein lauf/scheibe-Z.json lauf/kugel-Z.json --out nachtrag/alter.json
"""
import argparse, json, os, math, hashlib
import numpy as np


def sc2(x):
    x = x[x >= 1].astype(float)
    return float((x ** 2).sum() / x.sum()) if x.size else float('nan'), int(x.size)


def boot_sc2(x, rng, B=20, n=200):
    x = x[x >= 1].astype(float)
    m = x.size
    g = [(m * i) // B for i in range(B + 1)]
    s1 = np.array([x[g[i]:g[i + 1]].sum() for i in range(B)])
    s2 = np.array([(x[g[i]:g[i + 1]] ** 2).sum() for i in range(B)])
    out = []
    for _ in range(n):
        idx = rng.integers(0, B, B)
        out.append(float(s2[idx].sum() / s1[idx].sum()) if s1[idx].sum() > 0 else float('nan'))
    return np.array(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ein', nargs='+', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    res = {'art': 'Nachtrag nach Sicht, beschreibend', 'code_sha256':
           hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(), 'gruppen': {}}
    rng = np.random.default_rng(4242)
    fenster = {'alter_10_bis_47.5': (10.0, 47.5), 'alter_30_bis_47.5': (30.0, 47.5)}
    for pf in a.ein:
        L = json.load(open(pf))
        d = os.path.dirname(os.path.abspath(pf))
        gr = {}
        for f in L['faelle']:
            if f.get('r', 0.0) != 0.0:
                continue
            N = f['N']
            s = np.load(os.path.join(d, f['npz']))['s']
            ein = f['einschwingen']['schritte']
            alter = (ein + np.arange(1, s.size + 1)) / float(N)
            e = {'N': N, 'einschwingen': ein, 'mess': int(s.size), 'alter_ende': float(alter[-1]) if s.size else None}
            q = [(s.size * i) // 4 for i in range(5)]
            e['s_mittel_viertel'] = [float(s[q[i]:q[i + 1]].mean()) for i in range(4)]
            e['sc2_viertel'] = [sc2(s[q[i]:q[i + 1]])[0] for i in range(4)]
            for nm, (lo, hi) in fenster.items():
                m = (alter > lo) & (alter <= hi + 1e-9)
                v, n = sc2(s[m])
                bs = boot_sc2(s[m], rng) if n >= 20 else None
                e[nm] = {'sc2': v, 'lawinen': n, 'boot': bs.tolist() if bs is not None else None}
            e['letzte_20_prozent'] = {'sc2': sc2(s[int(0.8 * s.size):])[0],
                                      'alter_von': float(alter[int(0.8 * s.size)]) if s.size else None}
            gr[f['name']] = e
        # D je Fenster
        names = sorted(gr, key=lambda k: gr[k]['N'])
        Ns = np.array([gr[k]['N'] for k in names], dtype=float)
        dd = {}
        for nm in fenster:
            y = np.array([gr[k][nm]['sc2'] for k in names])
            if np.all(np.isfinite(y)) and np.all(y > 0) and all(gr[k][nm]['boot'] for k in names):
                D = float(np.polyfit(np.log(Ns), np.log(y), 1)[0])
                bs = np.array([gr[k][nm]['boot'] for k in names])
                Db = [float(np.polyfit(np.log(Ns), np.log(bs[:, j]), 1)[0]) for j in range(bs.shape[1])
                      if np.all(np.isfinite(bs[:, j])) and np.all(bs[:, j] > 0)]
                dd[nm] = {'sc2': y.tolist(), 'D': D, 'D_ki95': [float(np.percentile(Db, 2.5)),
                                                                 float(np.percentile(Db, 97.5))]}
        y = np.array([gr[k]['letzte_20_prozent']['sc2'] for k in names])
        dd['letzte_20_prozent'] = {'sc2': y.tolist(), 'D': float(np.polyfit(np.log(Ns), np.log(y), 1)[0])}
        for k in names:
            for nm in fenster:
                gr[k][nm].pop('boot', None)
        res['gruppen'][os.path.basename(pf)] = {'faelle': gr, 'D': dd}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(res, open(a.out, 'w'), indent=1)


if __name__ == '__main__':
    main()
