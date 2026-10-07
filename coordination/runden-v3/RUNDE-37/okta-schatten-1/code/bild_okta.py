#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OKTA-SCHATTEN-1, Nachtrag Bild (nach dem Einfrieren; nur Darstellung, keine Rechnung).

Grund: okta.bild (eingefroren) las L['varianten'] statt L['ergebnis']['varianten'] (KeyError im Lauf L3) und haette
die Spanne von H3 (negativ, weil ein Zweig omega^2 < 0 hat) als 1e-12 gezeichnet. Diese Fassung liest die
Ergebnisdateien von L1 und L2 unveraendert und zeichnet H3 als "instabil" statt als Balken.
Aufruf (nur ueber kleintest.sh): python bild_okta.py <licht.json> <schwer.json> <bild.png>
"""
import json
import sys

import numpy as np

EPS1 = 1e-3


def main(pl, ps, png):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with open(pl) as f:
        L = json.load(f)['ergebnis']
    with open(ps) as f:
        S = json.load(f)['ergebnis']
    fig, ax = plt.subplots(2, 2, figsize=(15, 10.5))
    # (a) Baender ohne und mit Sechsecken (DEC-Gewichte)
    for var, col, lw, lab in (('ohne', 'tab:red', 2.6, 'ohne Sechsecke: alles flach (0 und 8)'),
                              ('dec', 'tab:blue', 1.2, 'mit Sechsecken (DEC): 2 Photonen, 2 flach bei 8')):
        bp = L['varianten'][var]['bandpfad']
        x = np.array(bp['x'])
        om = np.array(bp['omega'])
        for j in range(om.shape[1]):
            ax[0, 0].plot(x, om[:, j], '-', color=col, lw=lw, alpha=0.75, label=(lab if j == 0 else None))
    mk = L['varianten']['dec']['bandpfad']['marken']
    ax[0, 0].set_xticks([m[1] for m in mk])
    ax[0, 0].set_xticklabels([m[0].replace('G', 'Gamma') for m in mk])
    for m in mk:
        ax[0, 0].axvline(m[1], color='0.85', lw=0.6)
    ax[0, 0].set_ylabel('omega (1/l), l = Tetraederkante')
    ax[0, 0].set_title('(a) Maxwell auf den Pyrochlor-Kanten: physikalische Baender')
    ax[0, 0].legend(loc='center right', fontsize=8)
    # (b) a2 je Richtung, beide Photonzweige, DEC und Einheitsgewichte
    farbe = {'100': 'tab:blue', '110': 'tab:orange', '111': 'tab:green'}
    xt, xl, x = [], [], 0
    for var in ('dec', 'eins'):
        er = L['varianten'][var]['dispersion_voll']
        for z, zz in enumerate(er['fenster']['W0']):
            for e in zz['je_richtung']:
                if e.get('a2') is None:
                    continue
                ax[0, 1].plot(x + 0.15 * (['100', '110', '111'].index(e['klasse']) - 1), e['a2'], 'o',
                              color=farbe[e['klasse']], ms=4)
            xt.append(x)
            xl.append('%s / Zweig %d' % (var, z))
            x += 1
    for y in (-1.0 / 12, -5.0 / 48, -1.0 / 9):
        ax[0, 1].axhline(y, color='0.6', ls=':', lw=1)
    ax[0, 1].set_xticks(xt)
    ax[0, 1].set_xticklabels(xl, fontsize=8)
    ax[0, 1].set_ylabel('a2 (k in 1/l)')
    ax[0, 1].set_title('(b) a2 der Photonen (blau 100, orange 110, gruen 111); grau: M-D (Diamant) zum Vergleich')
    # (c) TT omega^2/k^2 je Richtung (|k| = 1e-3), relativ zum Mittel der Variante
    vs = [('H3', 'tab:blue'), ('R12', 'tab:green'), ('Z8', 'tab:purple'), ('D1z', 'tab:red')]
    rows0 = [r for r in S['varianten']['H3']['p13'] if r['eps'] == EPS1]
    namen13 = [r['richtung'] for r in rows0]
    for i, (var, col) in enumerate(vs):
        rows = [r for r in S['varianten'][var]['p13'] if r['eps'] == EPS1 and r['z'] is not None]
        w = np.array([r['z']['w'] for r in rows])
        m = np.abs(w).mean()
        for b in range(2):
            ax[1, 0].plot(np.arange(len(rows)) + 0.08 * i, w[:, b] / m, 'o-' if b == 0 else 's--', color=col, ms=3,
                          lw=0.8, label=(var if b == 0 else None))
    ax[1, 0].axhline(0, color='k', lw=0.6)
    ax[1, 0].set_xticks(range(len(namen13)))
    ax[1, 0].set_xticklabels(namen13, rotation=60, fontsize=8)
    ax[1, 0].set_ylabel('omega^2/k^2 geteilt durch Mittel von |omega^2/k^2|')
    ax[1, 0].set_title('(c) TT-Zweige der Tetraeder-Oktaeder-Wabe (A1R1, J = 1); unter 0: instabil')
    ax[1, 0].legend(fontsize=8)
    # (d) Spannen gegen V
    namen = ['V (Finn, gefuellt)', 'H3 (Haupt)', 'R12 (starr)', 'Z8 (Mitte)', 'D1z (eine Diag.)', 'K (TT-ISO-1)']
    sp = [S['referenz_V']['spanne_tti'], S['varianten']['H3']['spanne13'], S['varianten']['R12']['spanne13'],
          S['varianten']['Z8']['spanne13'], S['varianten']['D1z']['spanne13'],
          S['kontrolle_K']['max'] / S['kontrolle_K']['min'] - 1]
    cols = ['0.5', 'tab:blue', 'tab:green', 'tab:purple', 'tab:red', '0.75']
    for i, (v, c) in enumerate(zip(sp, cols)):
        if v is None or v <= 0:
            ax[1, 1].text(i, 1e-2, 'instabil\n(omega^2 < 0)', ha='center', va='bottom', fontsize=8, color=c)
        else:
            ax[1, 1].bar(i, v, color=c)
            ax[1, 1].text(i, v * 1.3, '%.2g' % v, ha='center', fontsize=8)
    ax[1, 1].set_yscale('log')
    ax[1, 1].set_ylim(1e-8, 10)
    ax[1, 1].axhline(S['referenz_V']['spanne_tti'], color='0.5', ls='--', lw=1)
    ax[1, 1].set_xticks(range(len(namen)))
    ax[1, 1].set_xticklabels(namen, rotation=20, fontsize=8)
    ax[1, 1].set_ylabel('Spanne max/min - 1 (13 Richtungen x 2 Zweige x 2 |k|)')
    ax[1, 1].set_title('(d) TT-Spanne ohne Abstimmung: Wabe gegen V (gestrichelt, 6,34 %)')
    fig.suptitle('OKTA-SCHATTEN-1: Schattenformen am Tetraeder-Netz (synthetische Rechnung, keine Messdaten)')
    fig.tight_layout()
    fig.savefig(png, dpi=110)
    print('bild ->', png, flush=True)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
