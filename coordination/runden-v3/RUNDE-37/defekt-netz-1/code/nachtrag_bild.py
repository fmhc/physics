#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DEFEKT-NETZ-1, Nachtrag nach dem Einfrieren (beschreibend, kein Urteil): dasselbe Bild wie dn.py bild, nur die Legende
oben in der Mitte statt unten links (dort lief die V-Kurve durch den Legendentext). Liest nur lauf/tt-*.json."""
import json, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402


def main():
    out = sys.argv[1]
    tt = {}
    for p in sys.argv[2:]:
        with open(p) as fh:
            r = json.load(fh)['ergebnis']
        tt[r['netz']] = r
    farbe = {'C15': '#2a78d6', 'A15': '#eb6834', 'V': '#1baf7a'}
    fig, ax = plt.subplots(figsize=(9.0, 5.2), dpi=150)
    fig.patch.set_facecolor('#fcfcfb')
    ax.set_facecolor('#fcfcfb')
    for name in ('V', 'A15', 'C15'):
        d = tt[name]['pfad']
        w = np.array([x if x[0] is not None else [np.nan, np.nan] for x in d['w2k2']], float)
        mittel = tt[name]['w_mittel']
        x = np.array(d['winkel_grad'])
        rel = (w / mittel - 1.0) * 100.0
        lab = '%s  (Spanne s = %.2f %%, Mittel omega^2/k^2 = %.4f)' % (name, 100 * tt[name]['spanne'], mittel)
        ax.plot(x, rel[:, 0], color=farbe[name], lw=2.0, label=lab)
        ax.plot(x, rel[:, 1], color=farbe[name], lw=2.0, ls='--')
        ax.annotate(name, (x[-1], rel[-1, 1]), xytext=(6, 0), textcoords='offset points', color='#0b0b0b', fontsize=9,
                    va='center')
    ecken = tt['C15']['pfad']['winkel_grad']
    m = (len(ecken) - 1) // 3
    xt = [ecken[0], ecken[m], ecken[2 * m], ecken[-1]]
    ax.set_xticks(xt)
    ax.set_xticklabels(['[100]', '[110]', '[111]', '[100]'])
    for v in xt:
        ax.axvline(v, color='#d9d8d4', lw=0.8, zorder=0)
    ax.axhline(0.0, color='#b5b4ae', lw=0.8, zorder=0)
    ax.grid(axis='y', color='#ecebe7', lw=0.6)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_color('#8a8984')
    ax.tick_params(colors='#52514e')
    ax.set_ylabel('omega^2/k^2 relativ zum Mittel je Netz [%]', color='#0b0b0b')
    ax.set_xlabel('Richtung von k laengs [100] -> [110] -> [111] -> [100] (|k| = 1e-3, A1R1, J = 1)', color='#0b0b0b')
    ax.set_title('DEFEKT-NETZ-1: TT-Tempo ueber der Richtung (durchgezogen: unterer Zweig, gestrichelt: oberer)',
                 color='#0b0b0b', fontsize=10)
    ax.legend(frameon=False, fontsize=8, loc='upper center', bbox_to_anchor=(0.58, 1.0), labelcolor='#0b0b0b')
    fig.tight_layout()
    fig.savefig(out, facecolor=fig.get_facecolor())
    print('fertig nachtrag_bild', out, flush=True)


if __name__ == '__main__':
    main()
