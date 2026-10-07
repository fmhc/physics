#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NETZ-DYN-1: Auswertung der Lauf-Zusammenfassungen aus/*.json -> aus/auswertung.md (Tabellen fuer ERGEBNIS.md)."""
import json, glob, math, os, sys
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
AUS = os.path.join(HIER, '..', 'aus')


def lade(name):
    p = os.path.join(AUS, name + '.json')
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)


def ds_bei(J, sig):
    d = dict((int(s), v) for s, v in J.get('ds', []))
    return d.get(sig)


def ds_max(J, smin=5):
    xs = [(v, s) for s, v in J.get('ds', []) if s >= smin]
    return max(xs) if xs else (float('nan'), 0)


def ds_plateau(J, s1, s2):
    xs = [v for s, v in J.get('ds', []) if s1 <= s <= s2]
    return (float(np.mean(xs)), float(np.std(xs))) if xs else (float('nan'), float('nan'))


def dh_fenster(J, r1, r2):
    """Steigung von log n(r) gegen log r im Fenster, plus 1 = d_H."""
    sch = np.array(J.get('schalen', []))
    rs = np.arange(len(sch))
    m = (rs >= r1) & (rs <= r2) & (sch > 0)
    if m.sum() < 3:
        return float('nan')
    a = np.polyfit(np.log(rs[m]), np.log(sch[m]), 1)
    return 1.0 + a[0]


def mittl_abstand(J):
    sch = np.array(J.get('schalen', []))
    if sch.size == 0:
        return float('nan'), False
    rs = np.arange(len(sch))
    abgeschn = sch[-1] > 0.01 * sch.max()
    return float((rs * sch).sum() / sch.sum()), bool(abgeschn)


def f(x, n=3):
    if x is None:
        return '-'
    if isinstance(x, float) and (math.isnan(x)):
        return 'nan'
    return ('%.' + str(n) + 'f') % x


def zeile_geo(name, J):
    if J is None:
        return '| %s | (fehlt) |' % name
    N = J.get('mittel_N', J['N'])
    N0 = J.get('mittel_N0', J['N0'])
    n41 = J.get('mittel_N41', J['N41'])
    dsm, sm = ds_max(J)
    pl = ds_plateau(J, 20, 60)
    return '| %s | %d | %d | %s | %s | %s | %s | %s | %s | %s | %s (s=%d) | %s +- %s | %s | %s | %s/%s |' % (
        name, J['sweep'], J.get('n_mess', 0), f(N, 0), f(N0 / N), f(n41 / N) if J['modus'] != 'dt4' else '-',
        f(J['k0_ende'] if 'k0_ende' in J else J['k0'], 2), f(J['k4'], 3), f(J.get('profil_relstreu'), 3),
        f(J.get('profil_max_durch_mittel'), 3), f(dsm, 2), sm, f(pl[0], 2), f(pl[1], 2), f(dh_fenster(J, 3, 8), 2),
        f(J.get('mittel_grad_mittel'), 1), f(J.get('mittel_grad_max'), 0), f(J.get('mittel_n_sp'), 2))


def main():
    out = []
    out.append('# NETZ-DYN-1 Auswertung (automatisch aus aus/*.json)\n')
    # S0
    out.append('## S0: 1+1D\n')
    out.append('| Lauf | Sweeps | Messungen | N2 | T | d_H (Fenster r 6-20) | d_H (r 10-30) | d_H (r 20-40) | d_s (sigma 30) | d_s (sigma 100) | d_s (sigma 300) | <r> | abgeschnitten |')
    out.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    rr = {}
    for name in ('s0-flach', 's0a', 's0b', 's0a2', 's0b2'):
        J = lade(name)
        if J is None:
            continue
        r, ab = mittl_abstand(J)
        rr[name] = (J.get('mittel_N', J['N']), r)
        out.append('| %s | %d | %d | %s | %d | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            name, J['sweep'], J.get('n_mess', 0), f(J.get('mittel_N', J['N']), 0), J['args']['T'],
            f(dh_fenster(J, 6, 20)), f(dh_fenster(J, 10, 30)), f(dh_fenster(J, 20, 40)), f(ds_bei(J, 30)),
            f(ds_bei(J, 100)), f(ds_bei(J, 300)), f(r, 2), ab))
    if 's0a2' in rr and 's0b2' in rr:
        (Na, ra), (Nb, rb) = rr['s0a2'], rr['s0b2']
        if ra > 0 and rb > 0:
            out.append('\nEndliche Groessen (T proportional zu Wurzel N2): d_H = ln(N_a/N_b)/ln(<r>_a/<r>_b) = %s\n'
                       % f(math.log(Na / Nb) / math.log(ra / rb)))
    out.append('\nLokales d_H(r) = 1 + dln n/dln r (Auszug):\n')
    for name in ('s0-flach', 's0a', 's0b', 's0a2', 's0b2'):
        J = lade(name)
        if J is None:
            continue
        loc = dict((int(r), v) for r, v in J.get('dH_lokal', []))
        out.append('- %s: ' % name + ', '.join('r=%d: %s' % (r, f(loc.get(r), 2)) for r in (4, 8, 12, 16, 20, 25, 30, 40, 50)))
    # S1, D3, S2
    out.append('\n## 4D: Kennzahlen je Lauf\n')
    out.append('| Lauf | Sweeps | Messungen | N4 | N0/N4 | N41/N4 | k0 (Ende) | k4 | Profil rel. Streuung | Profil max/mittel | d_s max (bei sigma) | d_s Mittel sigma 20-60 | d_H (r 3-8) | Grad mittel | Grad max/Superpunkte je Messung |')
    out.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    namen = sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(AUS, '*.json')))
    v4 = [n for n in namen if n.startswith(('s1', 'd3', 'f', 'k-'))]
    for name in v4:
        out.append(zeile_geo(name, lade(name)))
    out.append('\n## 4D: d_s(sigma) Auszug\n')
    sigs = (5, 10, 20, 30, 50, 80, 120, 200, 300, 390)
    out.append('| Lauf | ' + ' | '.join('s=%d' % s for s in sigs) + ' |')
    out.append('|---' * (len(sigs) + 1) + '|')
    for name in v4:
        J = lade(name)
        out.append('| %s | ' % name + ' | '.join(f(ds_bei(J, s), 2) for s in sigs) + ' |')
    out.append('\n## Zuege (angenommen / gueltig vorgeschlagen)\n')
    for name in namen:
        J = lade(name)
        if J is None:
            continue
        a, p = J.get('angenommen', {}), J.get('vorschlaege', {})
        out.append('- %s: ' % name + ', '.join('%s %d/%d' % (k, a.get(k, 0), p[k]) for k in sorted(p)))
    out.append('\n## Superpunkte und Felder\n')
    out.append('| Lauf | Superpunkte je Messung | Lebensdauer n / max / mittel / >10 Sweeps | Plakette U(1) | Plakette SU(2) | Rahmen |m| | Rahmen <R.R> | Q an Superpunkten (n, Mittel, |Q|, Ganzzahl-Abw.) | Q normal (n, Mittel, |Q|) | Igel an SP (Mittel, |I|) | Igel normal | Orient.-Fehler |')
    out.append('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for name in namen:
        J = lade(name)
        if J is None or name.startswith('r') or name.startswith('s0'):
            continue
        L = J.get('sp_leben', {})
        q = J.get('ladung_sp', {})
        qn = J.get('ladung_normal', {})
        out.append('| %s | %s | %s / %s / %s / %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            name, f(J.get('mittel_n_sp'), 2), L.get('n'), L.get('max'), f(L.get('mittel'), 1), L.get('n_ueber_10'),
            f(J.get('mittel_plak_u1')), f(J.get('mittel_plak_su2')), f(J.get('mittel_rahmen_m')),
            f(J.get('mittel_rahmen_e')),
            '%s, %s, %s, %s' % (q.get('n'), f(q.get('Q_mittel')), f(q.get('Q_betrag')), f(q.get('Q_ganzzahl_abw'), 4)) if q else '-',
            '%s, %s, %s' % (qn.get('n'), f(qn.get('Q_mittel')), f(qn.get('Q_betrag'))) if qn else '-',
            '%s, %s' % (f(q.get('Igel_mittel')), f(q.get('Igel_betrag'))) if q else '-',
            '%s, %s' % (f(qn.get('Igel_mittel')), f(qn.get('Igel_betrag'))) if qn else '-',
            J.get('orient_fehler')))
    out.append('\n## Mittlere Feld-Logarithmusgewichte je Zugart (Rueckwirkung)\n')
    for name in namen:
        J = lade(name)
        if J is None or 'feld_logw_mittel' not in J:
            continue
        out.append('- %s: ' % name + ', '.join('%s %s (n=%d)' % (k, f(v, 2), J['feld_logw_n'][k])
                                              for k, v in sorted(J['feld_logw_mittel'].items())))
    out.append('\n## Profile (Mittel je Schicht)\n')
    for name in v4:
        J = lade(name)
        if J and 'profil_mittel' in J:
            out.append('- %s: %s' % (name, ', '.join(f(x, 1) for x in J['profil_mittel'])))
    out.append('\n## Pruefungen (letzte)\n')
    for name in namen:
        J = lade(name)
        if J is None:
            continue
        pr = J.get('pruefung', [])
        if pr:
            out.append('- %s: chi=%s, f=%s, chi_schicht=%s' % (name, pr[-1].get('chi'), pr[-1].get('f'),
                                                               pr[-1].get('chi_schicht', '-')))
    txt = '\n'.join(out) + '\n'
    with open(os.path.join(AUS, 'auswertung.md.neu'), 'w') as fh:
        fh.write(txt)
    os.replace(os.path.join(AUS, 'auswertung.md.neu'), os.path.join(AUS, 'auswertung.md'))
    print(txt)


if __name__ == '__main__':
    main()
