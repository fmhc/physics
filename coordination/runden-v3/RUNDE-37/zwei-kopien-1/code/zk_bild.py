#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZWEI-KOPIEN-1: Spektrum-Bild (Pfad Gamma -> X, Gamma -> K, Gamma -> L) je Fassung, aus lauf/zk-*.json."""
import argparse, json, os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    fass = ('K2', 'K2e', 'K4')
    ziele = ('X', 'K', 'L')
    stil = [('P|0', '#7f7f7f', 'o', 'ungekoppelt (kappa = 0)'), ('P|0.1', '#1f77b4', 'o', 'kappa = 0,1, Lesart P'),
            ('P|1', '#d62728', 'o', 'kappa = 1, Lesart P'), ('R|1', '#2ca02c', 'x', 'kappa = 1, Lesart R')]
    fig, ax = plt.subplots(len(fass), len(ziele), figsize=(13, 10), sharey='row')
    for i, f in enumerate(fass):
        with open(os.path.join(a.lauf, 'zk-%s.json' % f)) as fh:
            p = json.load(fh)['pfad']
        t = np.array(p['t'])
        for j, zz in enumerate(ziele):
            axx = ax[i, j]
            for key, col, mk, lab in stil:
                for ti, w2 in zip(t, p[zz][key]):
                    w2 = np.array(w2)
                    om = np.sign(w2) * np.sqrt(np.abs(w2))
                    axx.scatter(np.full(len(om), ti), om, s=7 if mk == 'o' else 12, c=col, marker=mk, linewidths=0.8,
                                label=lab if (ti == t[0]) else None, alpha=0.85)
            axx.axhline(0, color='k', lw=0.5)
            axx.set_title('%s: Gamma -> %s' % (f, zz), fontsize=10)
            axx.set_xlim(0, 1.02)
            if j == 0:
                axx.set_ylabel('omega (negativ: -sqrt|omega^2|)')
            if i == len(fass) - 1:
                axx.set_xlabel('Anteil des Wegs')
    h, l = ax[0, 0].get_legend_handles_labels()
    fig.legend(h, l, loc='upper center', ncol=4, fontsize=9, frameon=False)
    fig.suptitle('ZWEI-KOPIEN-1: Spektrum der physikalischen Moden (B1-Netz, zwei Kopien, Eckkopplung)', y=0.995, fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(a.out + '.tmp.png', dpi=110)
    os.replace(a.out + '.tmp.png', a.out)
    print('fertig bild', a.out, flush=True)


if __name__ == '__main__':
    main()
