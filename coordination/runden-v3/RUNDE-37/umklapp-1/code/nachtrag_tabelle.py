#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-1, NACHTRAG nach dem Einfrieren (beschreibend, kein Urteil): Tabelle der TT-Kennzahlen je (N, f) ueber ALLE
vollstaendigen Netze, auch nicht regulaere (uk_auswertung mittelt Spanne und Tempo nur ueber regulaere Netze), dazu je
Netz r = Spanne(f) / Spanne(0) - 1 und die relative Aenderung von omega^2/k^2. Liest nur auswertung.json."""
import argparse, json
import numpy as np


def ms(x):
    x = np.array([v for v in x if v is not None], float)
    if len(x) == 0:
        return None
    return [float(x.mean()), float(x.std(ddof=1)) if len(x) > 1 else None, int(len(x))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--aus', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    d = json.load(open(a.aus))
    nl = [n for n in d['tt_netze'] if n.get('vollstaendig')]
    zeilen = []
    for N in sorted(set(n['N'] for n in nl)):
        for f in sorted(set(n['f'] for n in nl if n['N'] == N)):
            g = [n for n in nl if n['N'] == N and n['f'] == f]
            zeilen.append({'N': N, 'f': f, 'n': len(g), 'saaten': [n['saat'] for n in g],
                           'n_regulaer': sum(bool(n['regulaer']) for n in g),
                           'spanne': ms([n.get('spanne') for n in g]), 'w_mittel': ms([n.get('w_mittel') for n in g]),
                           'tempo_mittel': ms([n.get('tempo_mittel') for n in g]),
                           'aufspaltung_max': ms([n.get('aufspaltung_max') for n in g]),
                           'richtungsspanne': ms([n.get('richtungsspanne_mittel_zweige') for n in g]),
                           'n_wachsend_max_je_netz': [n['n_wachsend_max'] for n in g],
                           'B_red_neg_max_je_netz': [n['B_red_neg_max'] for n in g],
                           'A_red_pd_je_netz': [n['A_red_pd_alle'] for n in g],
                           'n_unklar_max_je_netz': [n['n_unklar_max'] for n in g],
                           'n_masselos_je_netz': [n['n_masselos'] for n in g],
                           'tt_min_je_netz': [n['tt_min'] for n in g],
                           'zuege_je_netz': [(n['zugstat'] or {}).get('ende', {}).get('n_zuege', 0) for n in g]})
    paare = []
    for n in nl:
        if n['f'] > 0:
            b = [x for x in nl if x['f'] == 0.0 and x['N'] == n['N'] and x['saat'] == n['saat']]
            if b and n.get('spanne') is not None and b[0].get('spanne') is not None:
                paare.append({'N': n['N'], 'saat': n['saat'], 'f': n['f'], 'regulaer_f': bool(n['regulaer']),
                              'spanne0': b[0]['spanne'], 'spanne_f': n['spanne'], 'r': n['spanne'] / b[0]['spanne'] - 1,
                              'w_rel': n['w_mittel'] / b[0]['w_mittel'] - 1,
                              'tempo_rel': n['tempo_mittel'] / b[0]['tempo_mittel'] - 1})
    out = {'zeilen': zeilen, 'paare_alle': paare}
    for f in sorted(set(p['f'] for p in paare)):
        rr = np.abs([p['r'] for p in paare if p['f'] == f])
        out['median_abs_r_f%g' % f] = float(np.median(rr))
        out['mittel_w_rel_f%g' % f] = float(np.mean([p['w_rel'] for p in paare if p['f'] == f]))
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1)
    import os
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag tabelle', len(zeilen), 'zeilen', len(paare), 'paare', flush=True)


if __name__ == '__main__':
    main()
