#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGEL-1 Nachtrag (NACH dem Einfrieren und NACH dem Ausgang geschrieben, 2026-10-04 ~02:13 CEST; beschreibend).

Anlass: Vorzeichenfehler im eingefrorenen PLAN.md, Abschnitt 4.3/6: Die Formel F = -[U((n*+1)e) - U((n*-1)e)]/(2|e|)
misst die Kraftkomponente NACH AUSSEN (+e, von der schweren Quelle weg). Die Urteilsregel RG3 verlangt aber
"alle a > 0 (Fallen zur schweren Quelle hin)" und benutzt eta = 2|a1 - a2|/(a1 + a2) mit positiven Betraegen.
Bei Anziehung sind die gemessenen a daher negativ; eta wird negativ, und bild-eta.png zeigt nur die Untergrenze 1e-18.

Dieses Skript aendert kein Urteil und keine eingefrorene Datei. Es liest lauf/auswertung.json und rechnet die
Beschleunigungen ZUR QUELLE HIN (a' = -a), dazu eta' = 2|a'_k - a'_g|/(a'_k + a'_g), und zeichnet bild-eta-nachtrag.png.
Aufruf: regel_nachtrag.py --lauf lauf
"""
import argparse, hashlib, json, os, time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ETA_E_MAX = 1e-3
ETA_Q_MIN = 5e-2
D_FALL = 8.0


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lauf', required=True)
    a = ap.parse_args()
    p = os.path.join(a.lauf, 'auswertung.json')
    with open(p) as f:
        aw = json.load(f)
    w = aw['urteile']['RG3']['werte']
    out = {'erzeugt_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'skript_sha256': sha(os.path.abspath(__file__)),
           'quelle_auswertung_sha256': sha(p), 'hinweis': 'beschreibend, nach dem Einfrieren; mechanisches Urteil unveraendert',
           'linien': {}}
    for kp, key in (('energie', 'energie'), ('ladung', 'ladung')):
        for nm, v in w[key].items():
            ak, ag = -v['a_k'], -v['a_g']
            out['linien'].setdefault(nm, {})[kp] = {'a_k_zur_quelle': ak, 'a_g_zur_quelle': ag,
                                                    'eta': 2 * abs(ak - ag) / (ak + ag), 'd_durch_R': v['d_durch_R']}
    alle_zur_quelle = all(x[kp]['a_k_zur_quelle'] > 0 and x[kp]['a_g_zur_quelle'] > 0
                          for x in out['linien'].values() for kp in ('energie', 'ladung'))
    eE = max(x['energie']['eta'] for x in out['linien'].values())
    eQ = min(x['ladung']['eta'] for x in out['linien'].values())
    out['alle_a_zur_quelle_positiv'] = alle_zur_quelle
    out['eta_E_max'] = eE
    out['eta_Q_min'] = eQ
    out['schwellen_der_karte_erfuellt_bei_richtiger_richtung'] = bool(alle_zur_quelle and eE < ETA_E_MAX and eQ > ETA_Q_MIN)
    prof = {}
    for kp in ('E', 'N'):
        zz = aw['tabellen']['eta_profil_100'][kp]
        prof[kp] = [{'d_durch_R': z['d_durch_R'], 'a_k_zur_quelle': -z['a_k'], 'a_g_zur_quelle': -z['a_g'],
                     'eta': 2 * abs(z['a_k'] - z['a_g']) / (-(z['a_k'] + z['a_g']))} for z in zz]
        if not all(z['a_k_zur_quelle'] > 0 and z['a_g_zur_quelle'] > 0 for z in prof[kp]):
            out['profil_warnung_%s' % kp] = 'nicht alle a zur Quelle hin positiv'
    out['eta_profil_100'] = prof
    with open(os.path.join(a.lauf, 'nachtrag-rg3-vorzeichen.json'), 'w') as f:
        json.dump(out, f, indent=1)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    for kp, col, lab in (('E', 'C0', 'Energiekopplung'), ('N', 'C3', 'Ladungskopplung')):
        zz = prof[kp]
        ax[0].semilogy([z['d_durch_R'] for z in zz], [z['eta'] for z in zz], '-o', ms=3, color=col, label=lab)
    ax[0].axhline(ETA_E_MAX, color='C0', ls='--', lw=0.8, label='Schwelle 1e-3 (Energie)')
    ax[0].axhline(ETA_Q_MIN, color='C3', ls='--', lw=0.8, label='Schwelle 5e-2 (Ladung)')
    ax[0].axvline(D_FALL, color='0.6', lw=0.8)
    ax[0].set_xlabel('d / R ([100]), R = R_half(Q = 500)/h')
    ax[0].set_ylabel("eta' = 2 |a'_k - a'_g| / (a'_k + a'_g), a' zur Quelle hin")
    ax[0].set_title('Nachtrag RG3: Q = 150 gegen Q = 500 im Feld von Q = 5000 (L = 256)')
    ax[0].legend(fontsize=8)
    xs = np.arange(3)
    nms = ['100', '110', '111']
    ax[1].bar(xs - 0.2, [out['linien'][nm]['energie']['eta'] for nm in nms], 0.4, label='Energie', color='C0')
    ax[1].bar(xs + 0.2, [out['linien'][nm]['ladung']['eta'] for nm in nms], 0.4, label='Ladung', color='C3')
    ax[1].set_yscale('log')
    ax[1].set_xticks(xs)
    ax[1].set_xticklabels(['[100]', '[110]', '[111]'])
    ax[1].axhline(ETA_E_MAX, color='C0', ls='--', lw=0.8)
    ax[1].axhline(ETA_Q_MIN, color='C3', ls='--', lw=0.8)
    ax[1].set_title("eta' bei d = 8 R (beschreibend, nach dem Einfrieren)")
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(a.lauf, 'bild-eta-nachtrag.png'), dpi=120)
    plt.close(fig)
    print('Nachtrag geschrieben', flush=True)


if __name__ == '__main__':
    main()
