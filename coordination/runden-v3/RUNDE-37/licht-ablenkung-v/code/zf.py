#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LICHT-ABLENKUNG-V: Zusammenfassung der Hauptlaeufe (nur Lesen der JSON-Dateien, Verhaeltnisse, Bild).

Aufruf nur ueber kleintest.sh auf der .69:
  python zf.py <aus.json> <bild.png> lauf/haupt-L16.json lauf/haupt-L24.json lauf/haupt-L32.json
"""
import hashlib
import json
import os
import sys
import time

import numpy as np


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def q(a, b):
    return a / b if (a is not None and b not in (None, 0.0)) else None


def stats(x):
    x = np.array([v for v in x if v is not None and np.isfinite(v)])
    if len(x) == 0:
        return None
    return {'n': int(len(x)), 'median': float(np.median(x)), 'min': float(x.min()), 'max': float(x.max())}


def main():
    aus, bild, ein = sys.argv[1], sys.argv[2], sys.argv[3:]
    out = {'eingaben': {p: sha(p) for p in ein}, 'laeufe': {}}
    daten = {}
    for p in ein:
        d = json.load(open(p))
        L = d['L']
        daten[L] = d
        zl = {'statik_kontrollen': d['statik_kontrollen'], 'quellen': {}}
        for nm, z in d['quellen'].items():
            A = z['fit']['A']
            sae = [s for s in z['saeulen'] if not s['ziel_mit_quellecke'] and s['b'] >= 1.5]
            r = {}
            for teil in ('gesamt', 'takt', 'laengen'):
                r['alpha_' + teil + '_ueber_ziel'] = stats([q(s['alpha_zur_masse'][teil], s['alpha_zur_masse']['ziel'])
                                                            for s in sae])
                r['T_' + teil + '_ueber_ziel'] = stats([q(s['T'][teil], s['T']['ziel']) for s in sae])
            # fit-freies Mass: Laengen-Anteil / Takt-Anteil (ART: 1), je Saeule bzw. Saeulenpaar
            r['alpha_laengen_ueber_takt'] = stats([q(s['alpha_zur_masse']['laengen'], s['alpha_zur_masse']['takt'])
                                                   for s in z['saeulen'] if s['b'] >= 1.5])
            r['T_laengen_ueber_takt'] = stats([q(s['T']['laengen'], s['T']['takt']) for s in z['saeulen'] if s['b'] >= 1.5])
            r['alpha_quer_ueber_radial'] = stats([abs(s['alpha_quer']['gesamt']) / abs(s['alpha_zur_masse']['ziel'])
                                                  for s in sae])
            r['alpha_ziel_ueber_4A_b'] = stats([q(s['alpha_zur_masse']['ziel'], s['ART_4A_ueber_b']) for s in sae])
            r['saeulen_b_bereich'] = [min(s['b'] for s in sae), max(s['b'] for s in sae)] if sae else None
            sp = [s for s in z['shapiro_paare'] if abs(s['b1'] - s['b2']) > 1e-9 and s['b1'] >= 1.5]
            r['shapiro_dT_gesamt_ueber_ziel'] = stats([q(s['dT']['gesamt'], s['dT']['ziel']) for s in sp])
            r['shapiro_dT_takt_ueber_ziel'] = stats([q(s['dT']['takt'], s['dT']['ziel']) for s in sp])
            r['shapiro_dT_laengen_ueber_ziel'] = stats([q(s['dT']['laengen'], s['dT']['ziel']) for s in sp])
            r['shapiro_dT_ziel_ueber_4A_ln'] = stats([q(s['dT']['ziel'], s['ART_gerade_4A_ln']) for s in sp])
            r['shapiro_dT_laengen_ueber_takt'] = stats([q(s['dT']['laengen'], s['dT']['takt']) for s in sp])
            r['shapiro_dT_gesamt_ueber_4A_ln'] = stats([q(s['dT']['gesamt'], s['ART_gerade_4A_ln']) for s in sp])
            r['fit'] = z['fit']
            r['eigen_probe_abw_rel_max'] = z['eigen_probe_abw_rel_max']
            r['schalen'] = [{k: s.get(k) for k in ('r0', 'r1', 'n', 'n_minus_1', 'takt', 'laengen', 'ziel_ART',
                                                    'ART_2A_ueber_r', 'gesamt_ueber_ziel', 'takt_ueber_halbziel',
                                                    'laengen_ueber_takt', 'laengen_ueber_takt_zelle_min',
                                                    'laengen_ueber_takt_zelle_max', 'gesamt_ueber_ziel_zelle_min',
                                                    'gesamt_ueber_ziel_zelle_max', 'dn_radial_tangential_mittel_rel',
                                                    'doppelbrechung_zelle_rel_max', 'epsL_iso', 'muL_iso')}
                            for s in z['schalen']]
            r['varianten_L_ueber_T'] = {vn: [(s['r0'], s['r1'], s['laengen_ueber_takt'], s['gesamt_ueber_ziel'])
                                             for s in sv] for vn, sv in z['varianten_schalen'].items()}
            r['nah'] = z['nah'][:8]
            zl['quellen'][nm] = r
            print('L=%d %s A=%.6f (soll %.6f) rms=%.1e eigen=%.1e' % (L, nm, A, z['fit']['A_soll'], z['fit']['rms_rel'],
                                                                   z['eigen_probe_abw_rel_max']))
            for k in ('alpha_gesamt_ueber_ziel', 'alpha_takt_ueber_ziel', 'alpha_laengen_ueber_ziel',
                      'alpha_laengen_ueber_takt', 'T_laengen_ueber_takt',
                      'T_gesamt_ueber_ziel', 'alpha_quer_ueber_radial', 'alpha_ziel_ueber_4A_b',
                      'shapiro_dT_gesamt_ueber_ziel', 'shapiro_dT_takt_ueber_ziel', 'shapiro_dT_laengen_ueber_ziel',
                      'shapiro_dT_laengen_ueber_takt', 'shapiro_dT_ziel_ueber_4A_ln', 'shapiro_dT_gesamt_ueber_4A_ln'):
                print('   %-32s %s' % (k, json.dumps(r[k])))
            for s in r['schalen']:
                print('   Schale [%4.1f,%4.1f) n=%5d ges/ziel=%s L/T=%.4f (Zellen %.3f..%.3f) rt=%s epsL=% .3e muL=% .3e' % (
                    s['r0'], s['r1'], s['n'],
                    ('%.4f' % s['gesamt_ueber_ziel']) if s['gesamt_ueber_ziel'] is not None else '-',
                    s['laengen_ueber_takt'], s['laengen_ueber_takt_zelle_min'], s['laengen_ueber_takt_zelle_max'],
                    '%.1e' % s['dn_radial_tangential_mittel_rel'], s['epsL_iso'], s['muL_iso']))
            print('   b-Bereich Saeulen', r['saeulen_b_bereich'])
        out['laeufe'][str(L)] = zl
    with open(aus + '.tmp', 'w') as f:
        json.dump(out, f, indent=1)
    os.replace(aus + '.tmp', aus)
    # Bild: L groesstes
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    Lm = max(daten)
    fig, ax = plt.subplots(2, 2, figsize=(13, 9.5))
    farben = {'P0': '#1f77b4', 'C1': '#d62728'}
    for nm, z in daten[Lm]['quellen'].items():
        S = [s for s in z['schalen'] if s['ziel_ART'] is not None]
        rm = [0.5 * (s['r0'] + s['r1']) for s in S]
        ax[0, 0].plot(rm, [s['n_minus_1'] for s in S], 'o-', color=farben[nm], ms=4, label='%s Gitter n-1' % nm)
        ax[0, 0].plot(rm, [s['ziel_ART'] for s in S], 'k--', lw=0.8)
        ax[0, 0].plot(rm, [s['takt'] for s in S], 's:', color=farben[nm], ms=3, label='%s nur Takt' % nm)
        ax[0, 0].plot(rm, [s['laengen'] for s in S], 'x:', color=farben[nm], ms=4, label='%s nur Laengen' % nm)
        ax[0, 1].plot(rm, [s['laengen_ueber_takt'] for s in S], 'o-', color=farben[nm], ms=4, label='%s Laengen/Takt' % nm)
        ax[0, 1].plot(rm, [s['gesamt_ueber_ziel'] for s in S], 's--', color=farben[nm], ms=4, label='%s (n-1)/Ziel' % nm)
        for vn, sv in z['varianten_schalen'].items():
            if vn == 'fest':
                continue
            ax[0, 1].plot([0.5 * (s['r0'] + s['r1']) for s in sv], [s['laengen_ueber_takt'] for s in sv], ':', lw=0.8,
                          color=farben[nm], label='%s L/T Gewichte %s' % (nm, vn))
        sae = [s for s in z['saeulen'] if not s['ziel_mit_quellecke'] and s['b'] >= 1.0]
        bb = [s['b'] for s in sae]
        ax[1, 0].plot(bb, [s['alpha_zur_masse']['gesamt'] for s in sae], 'o', color=farben[nm], ms=4, label='%s Gitter' % nm)
        ax[1, 0].plot(bb, [s['alpha_zur_masse']['ziel'] for s in sae], 'k+', ms=6)
        ax[1, 0].plot(bb, [s['alpha_zur_masse']['takt'] for s in sae], 's', color=farben[nm], ms=2, alpha=0.6)
        ax[1, 0].plot(bb, [s['alpha_zur_masse']['laengen'] for s in sae], 'x', color=farben[nm], ms=3, alpha=0.6)
        ax[1, 1].plot(bb, [s['alpha_zur_masse']['gesamt'] / s['alpha_zur_masse']['ziel'] for s in sae], 'o',
                      color=farben[nm], ms=4, label='%s gesamt/Ziel' % nm)
        ax[1, 1].plot(bb, [s['alpha_zur_masse']['takt'] / s['alpha_zur_masse']['ziel'] for s in sae], 's',
                      color=farben[nm], ms=3, alpha=0.6, label='%s Takt/Ziel' % nm)
        ax[1, 1].plot(bb, [s['alpha_zur_masse']['laengen'] / s['alpha_zur_masse']['ziel'] for s in sae], 'x',
                      color=farben[nm], ms=4, alpha=0.6, label='%s Laengen/Ziel' % nm)
    ax[0, 0].set_xscale('log'); ax[0, 0].set_yscale('symlog', linthresh=1e-4)
    ax[0, 0].set_xlabel('r / l_P (Zellmitte)'); ax[0, 0].set_ylabel('n - 1 (Schalenmittel, Einheitsquelle)')
    ax[0, 0].set_title('Index je Schale; gestrichelt: ART-Ziel 2 x Takt-Anteil mit Newton-Phi'); ax[0, 0].legend(fontsize=7)
    ax[0, 1].axhline(1, color='k', lw=0.5); ax[0, 1].set_ylim(0.6, 1.4); ax[0, 1].set_xscale('log')
    ax[0, 1].set_xlabel('r / l_P'); ax[0, 1].set_title('Laengen-Anteil / Takt-Anteil (ART: 1)'); ax[0, 1].legend(fontsize=6)
    ax[1, 0].set_xlabel('Stossparameter b / l_P (Saeule laengs [100])'); ax[1, 0].set_ylabel('Ablenkung zur Masse')
    ax[1, 0].set_title('Eikonal-Ablenkung; +: Ziel; kleine Zeichen: nur Takt / nur Laengen'); ax[1, 0].legend(fontsize=7)
    ax[1, 1].axhline(1, color='k', lw=0.5); ax[1, 1].axhline(0.5, color='k', lw=0.5, ls=':'); ax[1, 1].set_ylim(0, 1.3)
    ax[1, 1].set_xlabel('b / l_P'); ax[1, 1].set_title('Ablenkung / Ziel (1 = ART, 0,5 = halbe)'); ax[1, 1].legend(fontsize=6)
    fig.suptitle('LICHT-ABLENKUNG-V, gefuelltes Netz V, L = %d (synthetische Gitterrechnung, Einheitsquelle)' % Lm)
    fig.tight_layout()
    fig.savefig(bild + '.tmp.png', dpi=105)
    os.replace(bild + '.tmp.png', bild)
    print('fertig', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))


if __name__ == '__main__':
    main()
