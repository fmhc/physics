#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-1, NACHTRAG nach dem Einfrieren (beschreibend): lesbareres Bild. Links wie uk_bild (Umklappanteil gegen a),
Mitte Spanne je Netz gegen f mit logarithmischer Achse (offen = nicht regulaer/instabil), rechts Zahl der wachsenden
Moden je Netz gegen die Zahl der 2-3-Zuege. Liest auswertung.json und nachtrag/tabelle.json."""
import argparse, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402

FARBE = {128: '#1f6fb4', 256: '#c0392b'}
MK = {128: 'o', 256: 's'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aus', required=True)
    ap.add_argument('--tab', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    d = json.load(open(a.aus))
    tb = json.load(open(a.tab))
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(17, 5))
    for N in (128, 256):
        m = d['mb'][str(N)]
        x = np.array(m['a'])
        ax1.errorbar(x, m['phi_T'], yerr=m['phi_T_se'], marker=MK[N], color=FARBE[N], capsize=3,
                     label='N = %d: Anteil geaenderter Tetraeder' % N)
        ax1.plot(x, m['phi_F'], ls='--', marker=MK[N], ms=4, mfc='none', color=FARBE[N], label='N = %d: verletzte Flaechen' % N)
    al = d['mb']['alle']
    x = np.array(al['a'])
    ax1.plot(x, al['dehnung_phi_F'], ls=':', marker='^', color='k', label='lange TT-Welle (affine Dehnung)')
    ax1.plot(x, 7.5 * x, color='grey', lw=0.8, label='7,5 a (Steigung 1)')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel('Amplitude a (Eckverschiebung / mittlere Kantenlaenge)')
    ax1.set_ylabel('Anteil')
    ax1.set_title('M-B: Delaunay-Umklappungen, linear ohne Schwelle')
    ax1.legend(fontsize=7)
    ax1.grid(alpha=0.3, which='both')
    for n in d['tt_netze']:
        if not n.get('vollstaendig') or n.get('spanne') is None:
            continue
        reg = bool(n['regulaer'])
        ax2.plot(n['f'] + (0.004 if n['N'] == 256 else -0.004), 100 * n['spanne'], marker=MK[n['N']], ms=7, ls='none',
                 color=FARBE[n['N']], mfc=FARBE[n['N']] if reg else 'none')
    for N in (128, 256):
        ax2.plot([], [], marker=MK[N], ls='none', color=FARBE[N], label='N = %d regulaer (stabil)' % N)
        ax2.plot([], [], marker=MK[N], ls='none', color=FARBE[N], mfc='none', label='N = %d nicht regulaer (instabil)' % N)
    ax2.set_yscale('log')
    ax2.set_xlabel('Anteil f zufaellig umgeklappter Flaechen')
    ax2.set_ylabel('Spanne von omega^2/k^2 je Netz (%)')
    ax2.set_title('TT-Spanne je Netz (nur Netze mit 26 Werten)')
    ax2.legend(fontsize=7)
    ax2.grid(alpha=0.3, which='both')
    for z in tb['zeilen']:
        ax3.plot(z['zuege_je_netz'], z['n_wachsend_max_je_netz'], marker=MK[z['N']], ls='none', color=FARBE[z['N']], ms=7)
    for N in (128, 256):
        ax3.plot([], [], marker=MK[N], ls='none', color=FARBE[N], label='N = %d' % N)
    zz = np.linspace(0, 700, 2)
    ax3.plot(zz, 0.2 * zz, color='grey', lw=0.8, label='0,2 je Zug')
    ax3.set_xlabel('Zahl der zufaelligen 2-3-Zuege je Netz')
    ax3.set_ylabel('wachsende Moden je k-Punkt (Hoechstwert je Netz)')
    ax3.set_title('Freie Zuege: Instabilitaet waechst mit der Zugzahl')
    ax3.legend(fontsize=8)
    ax3.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(a.out, dpi=120)
    print('fertig nachtrag bild', a.out, flush=True)


if __name__ == '__main__':
    main()
