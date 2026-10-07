#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GLAS-1, NACHTRAG (nach dem Einfrieren, beschreibend): Tabellen fuer den Bericht aus lauf/auswertung.json
(eingefrorene Auswertung) und den Nachtrag-Dateien. Rechnet nur Mittelwerte, Streuungen und Rundungen fuer die Anzeige;
kein Urteil. Ausgabe: Markdown-Tabellen und eine JSON-Datei."""
import argparse, json, os, glob, hashlib
import numpy as np


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def pz(x, n=2):
    return ('%.' + str(n) + 'f') % (100.0 * x)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--auswertung', required=True)
    ap.add_argument('--nachtrag', required=True)
    ap.add_argument('--out', required=True, help='Praefix: <out>.md und <out>.json')
    a = ap.parse_args()
    aw = json.load(open(a.auswertung))
    out = {'auswertung_sha256': sha(a.auswertung)}
    md = []
    reg = [n for n in aw['netze'] if n.get('vollstaendig') and n.get('regulaer')]
    Ns = sorted(set(n['N'] for n in reg))
    # (a) Spanne je N und Saat
    md.append('### Spanne je Netz (Prozent), regulaere Netze\n')
    md.append('| N | ' + ' | '.join('s%d' % s for s in range(1, 13)) + ' | Mittel | SD |')
    md.append('|---|' + '---|' * 14)
    tab_a = {}
    for N in Ns:
        row = {n['saat']: n['spanne'] for n in reg if n['N'] == N}
        v = np.array(list(row.values()))
        tab_a[N] = row
        md.append('| %d | ' % N + ' | '.join(pz(row[s], 1) if s in row else '-' for s in range(1, 13)) +
                  ' | %s | %s |' % (pz(v.mean(), 1), pz(v.std(ddof=1), 1)))
    out['spanne_je_netz'] = tab_a
    # (b) Kennzahlen je N
    md.append('\n### Kennzahlen je N (Mittel +- SD ueber regulaere Netze)\n')
    md.append('| N | Netze | Spanne % | Richtungsspanne der Zweigmittel % | max. Aufspaltung der Polarisationen % | omega^2/k^2 Mittel | kleinste Luecke omega^2 (min) | TT-Anteil min | Linearitaet max |')
    md.append('|---|---|---|---|---|---|---|---|---|')
    tab_b = {}
    for N in Ns:
        g = [n for n in reg if n['N'] == N]
        f = lambda k: np.array([n[k] for n in g], float)  # noqa: E731
        sp_, rs, au, wm = f('spanne'), f('richtungsspanne_mittel_zweige'), f('aufspaltung_max'), f('w_mittel')
        lu = f('luecke_min')
        tt = f('tt_min')
        li = f('lin_max')
        tab_b[N] = {'n': len(g), 'spanne': [sp_.mean(), sp_.std(ddof=1)], 'richtungsspanne': [rs.mean(), rs.std(ddof=1)],
                    'aufspaltung': [au.mean(), au.std(ddof=1)], 'w_mittel': [wm.mean(), wm.std(ddof=1)],
                    'luecke_min': float(lu.min()), 'tt_min': float(tt.min()), 'lin_max': float(li.max())}
        md.append('| %d | %d | %s +- %s | %s +- %s | %s +- %s | %.3f +- %.3f | %.3g | %.6f | %.1e |' % (
            N, len(g), pz(sp_.mean(), 1), pz(sp_.std(ddof=1), 1), pz(rs.mean(), 1), pz(rs.std(ddof=1), 1),
            pz(au.mean(), 1), pz(au.std(ddof=1), 1), wm.mean(), wm.std(ddof=1), lu.min(), tt.min(), li.max()))
    out['kennzahlen_je_N'] = tab_b
    # (c) Richtungsabweichung je N
    md.append('\n### Mittlere Richtungsabweichung delta_d je N (Prozent, +- Standardfehler; z in Klammern)\n')
    rnamen = None
    for n in reg:
        rnamen = n['richtungen']
        break
    md.append('| Richtung | ' + ' | '.join('N = %d' % N for N in Ns) + ' |')
    md.append('|---|' + '---|' * len(Ns))
    for i, rn in enumerate(rnamen or []):
        cells = []
        for N in Ns:
            j = aw['je_N'][str(N)]
            if 'delta_mittel' in j:
                cells.append('%s +- %s (%.2f)' % (pz(j['delta_mittel'][i], 2), pz(j['delta_se'][i], 2), j['z'][i]))
            else:
                cells.append('-')
        md.append('| [%s] | ' % rn + ' | '.join(cells) + ' |')
    # (d) Nachtrag Gewichte
    gw = []
    for p in sorted(glob.glob(os.path.join(a.nachtrag, 'gewicht-N*.json'))):
        d = json.load(open(p))
        N = d['netze'][0]['N'] if d['netze'] else None
        for art, z in d['zusammenfassung'].items():
            gw.append({'N': N, 'art': art, **z})
        out.setdefault('gewicht_netze', []).extend(d['netze'])
    if gw:
        md.append('\n### Nachtrag: Bewegungsgewicht je Tetraeder (Spanne in Prozent)\n')
        md.append('| N | Gewicht | Netze | regulaer | Spanne Mittel | SD |')
        md.append('|---|---|---|---|---|---|')
        for z in sorted(gw, key=lambda z: (z['N'], z['art'])):
            md.append('| %s | %s | %d | %d | %s | %s |' % (z['N'], z['art'], z['n_netze'], z['n_regulaer'],
                                                        pz(z['spanne_mittel'], 1) if z['spanne_mittel'] is not None else '-',
                                                        pz(z['spanne_sd'], 1) if z['spanne_sd'] is not None else '-'))
        # J1-Kontrolle gegen den Hauptlauf
        haupt = {(n['N'], n['saat']): n['spanne'] for n in reg}
        ab = [abs(z['spanne'] / haupt[(z['N'], z['saat'])] - 1) for z in out.get('gewicht_netze', [])
              if z['art'] == 'J1' and z.get('spanne') is not None and (z['N'], z['saat']) in haupt]
        out['J1_gegen_hauptlauf_max_rel'] = float(max(ab)) if ab else None
        md.append('\nJ1 gegen Hauptlauf (gleiche Netze): groesste relative Abweichung der Spanne %s.' % (
            ('%.1e' % max(ab)) if ab else '-'))
        out['gewicht'] = gw
    # (e) N = 512 (Nachtrag)
    p512 = os.path.join(a.nachtrag, 'n512', 'auswertung-n512.json')
    if os.path.exists(p512):
        d = json.load(open(p512))
        for n in d['netze']:
            if n.get('vollstaendig'):
                out['n512'] = {k: n.get(k) for k in ('N', 'saat', 'regulaer', 'n_gruende', 'gruende', 'spanne', 'w_mittel',
                                                     'aufspaltung_max', 'richtungsspanne_mittel_zweige', 'luecke_min',
                                                     'tt_min', 'lin_max', 'n_masselos', 'n_wachsend_max', 'n_unklar_max')}
                md.append('\nN = 512, Saat 1 (Nachtrag): regulaer %s, Spanne %s %%, omega^2/k^2 Mittel %.3f, kleinste Luecke %.3g.' % (
                    n.get('regulaer'), pz(n['spanne'], 1) if n.get('spanne') is not None else '-',
                    n.get('w_mittel') or float('nan'), n.get('luecke_min') or float('nan')))
            else:
                out['n512'] = {'vollstaendig': False, 'ridx': n.get('ridx')}
                md.append('\nN = 512 (Nachtrag): unvollstaendig, Richtungen %s.' % n.get('ridx'))
    with open(a.out + '.md', 'w') as fh:
        fh.write('\n'.join(md) + '\n')
    with open(a.out + '.json', 'w') as fh:
        json.dump(out, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    print('fertig tabellen', flush=True)


if __name__ == '__main__':
    main()
