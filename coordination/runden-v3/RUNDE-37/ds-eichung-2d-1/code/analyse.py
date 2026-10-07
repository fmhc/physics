#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DS-EICHUNG-2D-1: Auswertung aller aus/*.json -> Markdown (stdout). Nutzt die Auswertungsfunktionen aus NETZ-DYN-1 unveraendert."""
import glob, json, math, os, re, sys
import numpy as np

NDC = os.environ.get('NETZDYN_CODE', '/home/fmh/fmhc-physics-remote/netz-dyn-1/code')
sys.path.insert(0, NDC)
import netzdyn as nd
import auswertung as aw

AUS = sys.argv[1] if len(sys.argv) > 1 else 'aus'
ND1 = '/home/fmh/fmhc-physics-remote/netz-dyn-1/aus'


def lade(p):
    with open(p) as f:
        return json.load(f)


def gruppe(files):
    """Mehrere JSON gleicher Groesse zusammenlegen (gewichtet nach Zahl der Messungen)."""
    Js = [lade(p) for p in files]
    Js = [J for J in Js if J.get('schalen') and J.get('n_schalen', 0) > 0]
    if not Js:
        return None
    ns = np.array([J['n_schalen'] for J in Js], dtype=float)
    L = max(len(J['schalen']) for J in Js)
    sch = np.zeros(L)
    for J, n in zip(Js, ns):
        s = np.array(J['schalen'])
        sch[:len(s)] += s * n
    sch /= ns.sum()
    out = {'schalen': sch.tolist(), 'n_schalen': int(ns.sum()), 'files': list(files)}
    nP = np.array([J.get('n_P', 0) for J in Js], dtype=float)
    if nP.sum() > 0:
        Lp = max(len(J['P_rueck']) for J in Js if J.get('P_rueck'))
        P = np.zeros(Lp)
        for J, n in zip(Js, nP):
            if n > 0:
                p = np.array(J['P_rueck'])
                P[:len(p)] += p * n
        P /= nP.sum()
        out['P_rueck'] = P.tolist()
        out['ds'] = nd.ds_kurve(P)
        out['n_P'] = int(nP.sum())
    rm = []
    for J in Js:
        rm += list(J.get('rmean_proben', []))
    out['rmean'] = rm
    out['N'] = Js[0].get('N')
    out['T'] = Js[0].get('T')
    out['proben'] = sum(J.get('proben', 0) or 0 for J in Js)
    for k in ('profil_relstreu', 'profil_max_durch_mittel', 'l_min_mittel'):
        vs = [J[k] for J in Js if J.get(k) is not None]
        if vs:
            out[k] = float(np.mean(vs))
    return out


def f(x, n=2):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return '-'
    return ('%.' + str(n) + 'f') % x


def ds_bei(G, s):
    d = dict((int(a), b) for a, b in G.get('ds', []))
    return d.get(s)


def dh_zentral(G, r):
    sch = np.array(G['schalen'])
    if r + 1 < len(sch) and sch[r + 1] > 0 and sch[r - 1] > 0:
        return 1.0 + (math.log(sch[r + 1]) - math.log(sch[r - 1])) / (math.log(r + 1) - math.log(r - 1))
    return float('nan')


def zeile(name, G, N):
    if G is None:
        return '| %s | (fehlt) |' % name
    rm = np.array(G['rmean'], dtype=float)
    r_av, trunc = aw.mittl_abstand(G)
    sem = float(rm.std(ddof=1) / math.sqrt(len(rm))) if len(rm) > 1 else float('nan')
    pl = aw.ds_plateau(G, 20, 60) if G.get('ds') else (float('nan'), float('nan'))
    dsm = aw.ds_max(G, 5) if G.get('ds') else (float('nan'), 0)
    return '| %s | %s | %d | %d | %s +- %s | %s | %s | %s | %s +- %s | %s (s=%d) |' % (
        name, N, G['proben'], G['n_schalen'], f(r_av, 2), f(sem, 2), 'ja' if trunc else 'nein',
        f(aw.dh_fenster(G, 6, 20), 2), f(ds_bei(G, 30), 2) + ' / ' + f(ds_bei(G, 100), 2) + ' / ' + f(ds_bei(G, 300), 2),
        f(pl[0], 2), f(pl[1], 2), f(dsm[0], 2), dsm[1])


def skalierung(name, gs, B=1000, seed=7):
    """gs = [(N, G)] sortiert; d_H aus <r> ~ N^(1/d_H): Paare und Anpassung ueber alle Groessen; Bootstrap ueber Proben."""
    gs = [(N, G) for N, G in gs if G is not None and len(G['rmean']) >= 3]
    if len(gs) < 2:
        return ['- %s: weniger als zwei Groessen' % name]
    rng = np.random.default_rng(seed)
    N = np.array([g[0] for g in gs], dtype=float)
    rm = [np.array(g[1]['rmean']) for g in gs]
    mean = np.array([r.mean() for r in rm])
    out = []
    for i in range(len(gs) - 1):
        d = math.log(N[i + 1] / N[i]) / math.log(mean[i + 1] / mean[i])
        bs = []
        for _ in range(B):
            a = rng.choice(rm[i], size=len(rm[i])).mean()
            b = rng.choice(rm[i + 1], size=len(rm[i + 1])).mean()
            bs.append(math.log(N[i + 1] / N[i]) / math.log(b / a))
        lo, hi = np.percentile(bs, [16, 84])
        out.append('| %s | %d -> %d | %s | %s bis %s |' % (name, N[i], N[i + 1], f(d, 2), f(lo, 2), f(hi, 2)))
    x = np.log(N)
    y = np.log(mean)
    sl = np.polyfit(x, y, 1)[0]
    bs = []
    for _ in range(B):
        yy = np.log(np.array([rng.choice(r, size=len(r)).mean() for r in rm]))
        bs.append(1.0 / np.polyfit(x, yy, 1)[0])
    lo, hi = np.percentile(bs, [16, 84])
    out.append('| %s | Anpassung alle (%d..%d) | %s | %s bis %s |' % (name, N[0], N[-1], f(1.0 / sl, 2), f(lo, 2), f(hi, 2)))
    # Anpassung ohne die kleinste Groesse
    if len(gs) >= 3:
        sl2 = np.polyfit(x[1:], y[1:], 1)[0]
        out.append('| %s | Anpassung ohne kleinste (%d..%d) | %s | |' % (name, N[1], N[-1], f(1.0 / sl2, 2)))
    return out


def main():
    fam = {}
    for p in sorted(glob.glob(os.path.join(AUS, '*.json'))):
        b = os.path.basename(p)
        if b.startswith('test') or b in ('cdtx-T160-N64000-s303.json', 'quad-N100000-s105.json'):
            continue   # s303, s105: Schalen bei r = 150 abgeschnitten (<r> verzerrt), nur im Text erwaehnt
        m = re.match(r'quad-N(\d+)-', b)
        if m:
            fam.setdefault(('quad', int(m.group(1))), []).append(p)
        m = re.match(r'flip-N(\d+)-', b)
        if m:
            fam.setdefault(('flip', int(m.group(1))), []).append(p)
        m = re.match(r'cdtx-T(\d+)-N(\d+)-', b)
        if m:
            fam.setdefault(('cdtx', int(m.group(2))), []).append(p)
    G = {k: gruppe(v) for k, v in fam.items()}
    print('# Auswertung DS-EICHUNG-2D-1 (automatisch aus aus/*.json)\n')
    print('Spalten: Familie | N | Proben | Schalenmessungen | <r> aus Schalen +- Fehler des Mittels ueber Proben | abgeschnitten? | '
          'd_H lokal (r 6..20) | d_s bei sigma 30 / 100 / 300 | d_s-Plateau (sigma 20..60) Mittel +- Std | d_s-Maximum\n')
    print('| Familie | N | Proben | Schalen | <r> | abgeschn. | d_H lokal 6..20 | d_s 30/100/300 | d_s 20..60 | d_s max |')
    print('|---|---|---|---|---|---|---|---|---|---|')
    for typ, lab in (('quad', 'Vierecke (CVS)'), ('flip', 'Dreiecke (Flips)'), ('cdtx', '1+1D CDT (l-Kette)')):
        for (t, N) in sorted(k for k in G if k[0] == typ):
            print(zeile(lab, G[(t, N)], N))
    # CDT aus netzdyn (Abschnitte)
    print('\n## 1+1D-CDT aus netzdyn (unveraendert), Abschnitte und D1-Altwerte\n')
    print('| Lauf | N2 | Proben | Schalen | <r> | abgeschn. | d_H lokal 6..20 | d_s 30/100/300 | d_s 20..60 | d_s max |')
    print('|---|---|---|---|---|---|---|---|---|---|')
    ndl = []
    for name, p in [('D1 s0b2 (Alt)', ND1 + '/s0b2.json'), ('D1 s0a2 (Alt)', ND1 + '/s0a2.json')] + \
            [(os.path.basename(q)[:-5], q) for q in sorted(glob.glob(os.path.join(AUS, 'cdt-*-c*.json')))]:
        if not os.path.exists(p):
            continue
        J = lade(p)
        J['N'] = J.get('mittel_N', J.get('N'))
        J['proben'] = J.get('n_mess', 0)
        J.setdefault('rmean', [])
        r_av, trunc = aw.mittl_abstand(J)
        pl = aw.ds_plateau(J, 20, 60) if J.get('ds') else (float('nan'), float('nan'))
        dsm = aw.ds_max(J, 5) if J.get('ds') else (float('nan'), 0)
        print('| %s | %s | %s | %s | %s | %s | %s | %s | %s +- %s | %s (s=%d) |' % (
            name, f(J['N'], 0), J.get('n_mess'), J.get('n_schalen'), f(r_av, 2), 'ja' if trunc else 'nein',
            f(aw.dh_fenster(J, 6, 20), 2), f(ds_bei(J, 30), 2) + ' / ' + f(ds_bei(J, 100), 2) + ' / ' + f(ds_bei(J, 300), 2),
            f(pl[0], 2), f(pl[1], 2), f(dsm[0], 2), dsm[1]))
        if J.get('profil_relstreu') is not None:
            print('|  | Profil: relative Streuung %s, max/mittel %s | | | | | | | | |' % (f(J['profil_relstreu'], 3), f(J.get('profil_max_durch_mittel'), 3)))
    # lokale d_H
    print('\n## Lokale d_H(r) = 1 + dln n/dln r (zentrale Differenz) nach Familie und Groesse\n')
    rs = [3, 4, 6, 8, 10, 12, 16, 20, 25, 30, 40]
    print('| Familie | N | ' + ' | '.join('r=%d' % r for r in rs) + ' |')
    print('|---|---|' + '---|' * len(rs))
    for typ, lab in (('quad', 'Vierecke'), ('flip', 'Dreiecke'), ('cdtx', 'CDT l-Kette')):
        for (t, N) in sorted(k for k in G if k[0] == typ):
            g = G[(t, N)]
            print('| %s | %d | ' % (lab, N) + ' | '.join(f(dh_zentral(g, r), 2) for r in rs) + ' |')
    # Skalierung
    print('\n## Groessenskalierung d_H aus <r> (Bootstrap ueber Proben, 16 bis 84 %)\n')
    print('| Familie | Paar / Anpassung | d_H | Bereich |')
    print('|---|---|---|---|')
    for typ, lab in (('quad', 'Vierecke'), ('flip', 'Dreiecke'), ('cdtx', 'CDT l-Kette')):
        gs = sorted(((k[1], G[k]) for k in G if k[0] == typ), key=lambda x: x[0])
        for line in skalierung(lab, gs):
            print(line)
    # Anpassung mit Versatz: <r> = a N^(1/dH) + b, dH fest (Literatur) und frei (>= 4 Groessen)
    print('\n## Anpassung <r> = a N^(1/d_H) + b (Versatz b), Fehler aus den Proben (Gewichte 1/sem^2)\n')
    print('| Familie | d_H fest | a | b | chi2/ndf | Vorhersage naechstgroessere Groesse |')
    print('|---|---|---|---|---|---|')
    for typ, lab, dfix in (('quad', 'Vierecke', 4.0), ('flip', 'Dreiecke', 4.0), ('cdtx', 'CDT l-Kette', 2.0)):
        gs = sorted(((k[1], G[k]) for k in G if k[0] == typ and G[k] is not None and len(G[k]['rmean']) >= 3), key=lambda x: x[0])
        if len(gs) < 3:
            continue
        N = np.array([g[0] for g in gs], dtype=float)
        m = np.array([np.mean(g[1]['rmean']) for g in gs])
        e = np.array([np.std(g[1]['rmean'], ddof=1) / math.sqrt(len(g[1]['rmean'])) for g in gs])
        for dfx in sorted(set([dfix, 2.0, 3.0, 4.0])):
            x = N ** (1.0 / dfx)
            A = np.vstack([x / e, 1.0 / e]).T
            sol, res, rk, sv = np.linalg.lstsq(A, m / e, rcond=None)
            chi = float((((A @ sol) - m / e) ** 2).sum())
            print('| %s | %.1f | %s | %s | %s | |' % (lab, dfx, f(sol[0], 4), f(sol[1], 2), f(chi / max(len(N) - 2, 1), 2)))
    # Versatz im linearen Schalenwachstum (CDT): n(r) = a r + b im Fenster
    print('\n## Lineare Anpassung n(r) = a (r - r0) der gemittelten Schalen (CDT; Fenster)\n')
    print('| Quelle | Fenster | a | r0 = -b/a |')
    print('|---|---|---|---|')
    quellen = [('D1 s0b2 (N2=3982)', lade(ND1 + '/s0b2.json')), ('D1 s0a2 (N2=15939)', lade(ND1 + '/s0a2.json'))]
    quellen += [('l-Kette N=%d' % k[1], G[k]) for k in sorted(G) if k[0] == 'cdtx' and G[k] is not None]
    for name, J in quellen:
        sch = np.array(J['schalen'])
        for (r1, r2) in ((6, 20), (10, 30)):
            rr = np.arange(len(sch))
            mk = (rr >= r1) & (rr <= r2)
            a, b = np.polyfit(rr[mk], sch[mk], 1)
            print('| %s | %d..%d | %s | %s |' % (name, r1, r2, f(a, 3), f(-b / a, 2)))
    # Drift / Gleichgewicht der Flip-Kette und anderer Zeitreihen
    print('\n## Zeitreihe von <r> (Drift: erste gegen zweite Haelfte der Proben je Datei)\n')
    print('| Datei | Proben | <r> erste Haelfte | <r> zweite Haelfte | Thermalisierung: <r> bei Sweep (Auswahl) |')
    print('|---|---|---|---|---|')
    for p in sorted(glob.glob(os.path.join(AUS, '*.json'))):
        J = lade(p)
        if 'reihe' not in J or not J['reihe'] or 'test' in p:
            continue
        rh = [x for x in J['reihe'] if len(x) < 4]
        th = [x for x in J['reihe'] if len(x) >= 4]
        if len(rh) < 4:
            continue
        v = np.array([x[1] for x in rh])
        h = len(v) // 2
        ths = ', '.join('%d: %.1f' % (x[0], x[1]) for x in th[::max(1, len(th) // 6)][:7]) if th else ''
        print('| %s | %d | %s +- %s | %s +- %s | %s |' % (os.path.basename(p), len(v), f(v[:h].mean(), 2),
              f(v[:h].std(ddof=1) / math.sqrt(h), 2), f(v[h:].mean(), 2), f(v[h:].std(ddof=1) / math.sqrt(len(v) - h), 2), ths))
    # d_s mit grossem sigma-Bereich
    fl = sorted(glob.glob(os.path.join(AUS, 'dslang-N*.json')))
    if fl:
        print('\n## d_s bis sigma = 3000 (Viereckskarten)\n')
        ss2 = [30, 100, 300, 600, 1000, 1500, 2000, 2500]
        print('| Datei | N | n_P | ' + ' | '.join('s=%d' % s for s in ss2) + ' | Maximum (sigma) |')
        print('|---|---|---|' + '---|' * len(ss2) + '---|')
        for p in fl:
            J = lade(p)
            dsm = aw.ds_max(J, 5)
            print('| %s | %s | %s | ' % (os.path.basename(p), J.get('N'), J.get('n_P')) + ' | '.join(f(ds_bei(J, s), 2) for s in ss2) + ' | %s (%d) |' % (f(dsm[0], 2), dsm[1]))
    # Zusatz: Skalierung mit Fensterstatistik <r> bei d_s
    print('\n## d_s-Kurven (sigma = 10, 20, 30, 60, 100, 200, 400)\n')
    ss = [10, 20, 30, 60, 100, 200, 400]
    print('| Familie | N | ' + ' | '.join('s=%d' % s for s in ss) + ' |')
    print('|---|---|' + '---|' * len(ss))
    for typ, lab in (('quad', 'Vierecke'), ('flip', 'Dreiecke'), ('cdtx', 'CDT l-Kette')):
        for (t, N) in sorted(k for k in G if k[0] == typ):
            g = G[(t, N)]
            if g.get('ds'):
                print('| %s | %d | ' % (lab, N) + ' | '.join(f(ds_bei(g, s), 2) for s in ss) + ' |')


if __name__ == '__main__':
    main()
