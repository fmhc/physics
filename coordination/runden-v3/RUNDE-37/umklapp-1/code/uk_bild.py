#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-1: Bild aus auswertung.json (links Umklappanteil gegen a, rechts TT-Spanne je Netz gegen f)."""
import argparse, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402

FARBE = {'128': '#1f6fb4', '256': '#c0392b'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aus', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    d = json.load(open(a.aus))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.8))
    for N in ('128', '256'):
        if N in d.get('mb', {}):
            m = d['mb'][N]
            x = np.array(m['a'])
            y = np.array(m['phi_T'])
            ok = y > 0
            ax1.errorbar(x[ok], y[ok], yerr=np.array(m['phi_T_se'])[ok], marker='o', color=FARBE[N], capsize=3,
                         label='N = %s: Anteil geaenderter Tetraeder (Delaunay neu)' % N)
            yf = np.array(m['phi_F'])
            ax1.plot(x[yf > 0], yf[yf > 0], ls='--', marker='s', ms=4, color=FARBE[N], alpha=0.6,
                     label='N = %s: verletzte Flaechen (alte Verbindung)' % N)
    if 'alle' in d.get('mb', {}):
        al = d['mb']['alle']
        x = np.array(al['a'])
        yd = np.array(al['dehnung_phi_F'])
        ax1.plot(x[yd > 0], yd[yd > 0], ls=':', marker='^', color='k', label='affine TT-Dehnung: verletzte Flaechen')
        i = list(x).index(1e-2)
        ax1.plot(x, al['phi_T'][i] * x / 1e-2, color='grey', lw=0.8, label='Steigung 1 (durch alle bei a = 1e-2)')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel('Amplitude a (Effektivwert der Eckverschiebung / mittlere Kantenlaenge)')
    ax1.set_ylabel('Anteil')
    ax1.set_title('M-B: Delaunay-Umklappungen gegen Amplitude')
    ax1.legend(fontsize=7)
    ax1.grid(alpha=0.3, which='both')
    mk = {'128': 'o', '256': 's'}
    for N in ('128', '256'):
        nets = [n for n in d.get('tt_netze', []) if n.get('vollstaendig') and str(n['N']) == N and n.get('spanne') is not None]
        for s in sorted(set(n['saat'] for n in nets)):
            pts = sorted((n['f'], n['spanne']) for n in nets if n['saat'] == s)
            ax2.plot([p[0] for p in pts], [100 * p[1] for p in pts], marker=mk[N], ms=4, color=FARBE[N], alpha=0.35, lw=0.8)
        tz = [t for t in d.get('tabelle_tt', []) if str(t['N']) == N and t['spanne_mittel'] is not None]
        if tz:
            ax2.errorbar([t['f'] for t in tz], [100 * t['spanne_mittel'] for t in tz],
                         yerr=[100 * (t['spanne_sd'] or 0) for t in tz], marker=mk[N], ms=7, color=FARBE[N], lw=2, capsize=4,
                         label='N = %s: Mittel +- SD (regulaere Netze)' % N)
    ax2.set_xlabel('Anteil f umgeklappter Flaechen (2-3-Zuege / Flaechen des Ausgangsnetzes)')
    ax2.set_ylabel('Spanne von omega^2/k^2 je Netz (%)')
    ax2.set_title('TT-Wellen: Richtungsspanne gegen f (duenn: einzelne Netze)')
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(a.out, dpi=130)
    print('fertig bild', a.out, flush=True)


if __name__ == '__main__':
    main()
