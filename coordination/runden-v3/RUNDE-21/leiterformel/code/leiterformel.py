#!/usr/bin/env python3
"""leiterformel.py - Runde 21 LEITERFORMEL, Code-Agent (2026-10-02).

Phasenbedingung der Innenwelle: Delta Phi = k_innen(R_n+1) R_n+1 - k_innen(R_n) R_n je Sprossenpaar.
k_innen aus dem a-b-Block wie Runde 18 (ERGEBNIS Abschnitt 4), S0 = f(0)^2 des Hintergrundprofils an der Stelle
(Rechenweg der Vorlaeufer: Anker = gespeichertes Runde-18-Zeilenprofil mit w2 <= w2 der Stelle, stille3.Umgebung).
Methode und Wertung: PLAN.md (eingefroren 2026-10-02 18:44:29).
Befehle: k0, stellen, ausw.
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import time
import math
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import stille3 as S3          # Runde 18 / Code 1, unveraendert
import huellen_leiter as HL   # Runde 18, unveraendert

T0 = time.time()
PI = math.pi
K0_STELLEN = {'R18 Nr 81': (2.37, 2.368), 'R18 Nr 88': (2.07, 2.065)}
TOL_K0 = 0.01
TOL_LF = 0.03


def log(*a):
    print('[%7.1fs]' % (time.time() - T0), *a, flush=True)


def schreibe(pfad, obj):
    S3.schreibe(pfad, obj)


# ------------------------------------------------------------------ k_innen (Runde 18, woertlich)
def k_innen(w2, rho, S0):
    w = math.sqrt(w2)
    gs = S0 * (3.0 * S0 - 2.0)
    Va = w2 + S0 * (3.0 * S0 - 2.0)
    Ea = (w + rho) ** 2
    Eb = (w - rho) ** 2
    mitte = (Va - Ea + Va - Eb) / 2.0
    wurzel = math.sqrt(((Ea - Eb) / 2.0) ** 2 + gs ** 2)
    lm = mitte - wurzel
    lp = mitte + wurzel
    k = math.sqrt(-lm) if lm < 0 else float('nan')
    return k, lm, lp


def s0_wurzel(w2):
    # U_S(S) = 1 - 2 S + 1,5 S^2 = w2 bei g = 0 (M2), groessere Wurzel
    return (2.0 + math.sqrt(6.0 * w2 - 2.0)) / 3.0


def k_mitte(mod, pr, w2, rho):
    """Zusatzkontrolle (nicht im Plan): unterer Eigenwert des a-b-Blocks von M - E mit der Matrix der Kanalrechnung
    (stille3.Pot) am Gitterpunkt r = 0 des Profils."""
    pot = S3.Pot(mod, [pr])
    a, b = float(pot.Maa[0, 0]), float(pot.Mab[0, 0])
    w = math.sqrt(w2)
    Ea, Eb = (w + rho) ** 2, (w - rho) ** 2
    ev = np.linalg.eigvalsh(np.array([[a - Ea, b], [b, a - Eb]]))
    return (math.sqrt(-ev[0]) if ev[0] < 0 else float('nan')), a, b


# ------------------------------------------------------------------ Profil an der Stelle
def anker_w2(liste, w2):
    kand = [x for x in liste if x <= w2]
    return max(kand) if kand else min(liste)


def stelle_rechnen(mod, pdir, liste, st):
    t1 = time.time()
    za = anker_w2(liste, st['w2'])
    pfad = HL.ppfad(pdir, za)
    if not os.path.exists(pfad):
        raise SystemExit('Ankerprofil fehlt: %s' % pfad)
    anker = S3.lade_profil(pfad)
    U = S3.Umgebung(mod, anker)
    pr = U.profil(st['w2'])
    f0 = float(pr['f0'])
    S0 = f0 * f0
    k, lm, lp = k_innen(st['w2'], st['rho'], S0)
    S0w = s0_wurzel(st['w2'])
    kw, lmw, lpw = k_innen(st['w2'], st['rho'], S0w)
    km, Maa0, Mab0 = k_mitte(mod, pr, st['w2'], st['rho'])
    Rchi = HL.r_chi(pr)
    e = dict(st)
    e.update(anker=za, N=int(pr['N']), f0=f0, S0=S0, chi0=float(pr['chi0']), Rchi=Rchi, dRchi=Rchi - st['R'],
             k_innen=k, lam_m=lm, lam_p=lp, phi=k * st['R'], pi_k=PI / k,
             S0_wurzel=S0w, dS0=S0 - S0w, k_wurzel=kw, phi_wurzel=kw * st['R'],
             k_mitte=km, Maa0=Maa0, Mab0=Mab0, newton_profil=len(pr.get('newton', [])),
             sekunden=time.time() - t1)
    return e


def cmd_k0(pdir, eingabe, aus):
    mod = S3.modell_von('M2')
    liste = HL.zeilenliste()
    st = [s for s in json.load(open(eingabe))['stellen'] if s['quelle'] in K0_STELLEN]
    out = dict(befehl='k0', pdir=pdir, stellen=[])
    ok_alle = True
    for s in st:
        e = stelle_rechnen(mod, pdir, liste, s)
        karte, r18 = K0_STELLEN[s['quelle']]
        e['karte'] = karte
        e['r18_3stellig'] = r18
        e['d_karte'] = e['pi_k'] - karte
        e['d_r18'] = e['pi_k'] - r18
        e['pi_k_wurzel'] = PI / e['k_wurzel']
        e['bestanden'] = abs(e['d_karte']) <= TOL_K0
        ok_alle = ok_alle and e['bestanden']
        out['stellen'].append(e)
        log('K0 %s k=%d w2=%.8f rho=%.8f S0=%.10f S0w=%.10f k=%.8f pi/k=%.6f (Karte %.2f, d=%.2e; R18 %.3f, d=%.2e) '
            'pi/k_wurzel=%.6f k_mitte=%.8f Rchi=%.6f (R %.6f) chi0=%.2e' % (
                s['quelle'], s['k'], s['w2'], s['rho'], e['S0'], e['S0_wurzel'], e['k_innen'], e['pi_k'], karte,
                e['d_karte'], r18, e['d_r18'], e['pi_k_wurzel'], e['k_mitte'], e['Rchi'], s['R'], e['chi0']))
    out['K0_bestanden'] = bool(ok_alle and len(out['stellen']) == 2)
    schreibe(aus, out)
    log('K0 bestanden:', out['K0_bestanden'])


def cmd_stellen(pdir, eingabe, aus, i0, i1):
    mod = S3.modell_von('M2')
    liste = HL.zeilenliste()
    alle = json.load(open(eingabe))['stellen']
    out = dict(befehl='stellen', pdir=pdir, i0=i0, i1=i1, stellen=[])
    for i in range(i0, min(i1, len(alle))):
        e = stelle_rechnen(mod, pdir, liste, alle[i])
        e['index'] = i
        out['stellen'].append(e)
        schreibe(aus, out)
        log('%3d l=%d k=%d R=%.4f w2=%.8f S0=%.8f dS0=%.1e k=%.6f phi=%.5f dRchi=%.1e chi0=%.1e km-k=%.1e %.2fs' % (
            i, e['l'], e['k'], e['R'], e['w2'], e['S0'], e['dS0'], e['k_innen'], e['phi'], e['dRchi'], e['chi0'],
            e['k_mitte'] - e['k_innen'], e['sekunden']))
    out['fertig'] = True
    schreibe(aus, out)


# ------------------------------------------------------------------ Auswertung
def spearman(x, y):
    from scipy.stats import spearmanr
    if len(x) < 3:
        return None
    r = spearmanr(x, y)
    return dict(rho=float(r[0]), p=float(r[1]), n=len(x))


def stat(v):
    v = np.asarray(v, float)
    if len(v) == 0:
        return dict(n=0)
    return dict(n=int(len(v)), mittel=float(v.mean()), sd=float(v.std(ddof=1)) if len(v) > 1 else None,
                min=float(v.min()), max=float(v.max()), mittel_abs=float(np.abs(v).mean()))


def anteil_tol(paare):
    n = len(paare)
    ok = sum(1 for p in paare if abs(p['rest']) <= TOL_LF)
    return dict(n=n, n_ok=ok, anteil=(ok / n if n else None))


def vorzeichen(paare):
    n = len(paare)
    pos = sum(1 for p in paare if p['rest'] > 0)
    neg = sum(1 for p in paare if p['rest'] < 0)
    maj = max(pos, neg)
    return dict(n=n, positiv=pos, negativ=neg, anteil_mehrheit=(maj / n if n else None),
                mehrheit=('+' if pos >= neg else '-'))


def komma(x, f):
    return (f % x).replace('.', ',')


def cmd_ausw(k0json, aus, md, *teile):
    k0 = json.load(open(k0json))
    st = []
    for t in teile:
        d = json.load(open(t))
        assert d.get('fertig'), t
        st.extend(d['stellen'])
    st.sort(key=lambda e: (e['l'], e['k'], e['R']))
    # Doppelte
    doppelt = []
    for a, b in zip(st, st[1:]):
        if a['l'] == b['l'] and a['k'] == b['k'] and abs(a['R'] - b['R']) < 0.01:
            doppelt.append([a['quelle'], b['quelle']])
    kurven = {}
    for e in st:
        kurven.setdefault((e['l'], e['k']), []).append(e)
    paare = []
    for (l, k), ss in sorted(kurven.items()):
        if len(ss) < 2:
            continue
        dRs = [b['R'] - a['R'] for a, b in zip(ss, ss[1:])]
        med = float(np.median(dRs))
        for a, b in zip(ss, ss[1:]):
            dR = b['R'] - a['R']
            wechsel = (a['umlauf'] is not None and b['umlauf'] is not None and a['umlauf'] * b['umlauf'] < 0)
            abst_ok = dR <= 1.5 * med
            dphi = b['phi'] - a['phi']
            pik = 0.5 * (a['pi_k'] + b['pi_k'])
            dphi_w = b['phi_wurzel'] - a['phi_wurzel']
            mcm = l * (l + 1) / (2 * PI) * (1.0 / a['phi'] - 1.0 / b['phi']) if l > 0 else 0.0
            paare.append(dict(
                l=l, k=k, R_n=a['R'], R_n1=b['R'], quelle_n=a['quelle'], quelle_n1=b['quelle'],
                flag=' / '.join(x for x in (a.get('flag', ''), b.get('flag', '')) if x),
                umlauf=[a['umlauf'], b['umlauf']], wechsel=wechsel, median_dR=med, abstand_ok=abst_ok,
                gezaehlt=bool(wechsel and abst_ok), dR=dR, k_n=a['k_innen'], k_n1=b['k_innen'], phi_n=a['phi'], phi_n1=b['phi'],
                dphi=dphi, dphi_pi=dphi / PI, rest=dphi / PI - 1.0, pik_mittel=pik, rel_pik=pik / dR - 1.0,
                rest_wurzel=dphi_w / PI - 1.0, mcmahon=mcm, chi0_max=max(a['chi0'], b['chi0']),
                w2=[a['w2'], b['w2']], rho=[a['rho'], b['rho']]))
    gez = [p for p in paare if p['gezaehlt']]
    erg = dict(n_stellen=len(st), n_paare=len(paare), n_gezaehlt=len(gez),
               nicht_gezaehlt=[{x: p[x] for x in ('l', 'k', 'R_n', 'R_n1', 'umlauf', 'wechsel', 'dR', 'median_dR')}
                               for p in paare if not p['gezaehlt']],
               doppelt=doppelt)
    # Kontrollen je Stelle
    erg['kontrollen'] = dict(
        max_abs_dRchi=max(abs(e['dRchi']) for e in st),
        max_abs_dRchi_je_quelle={q: max(abs(e['dRchi']) for e in st if e['quelle'].split(' ')[0] == q)
                                 for q in sorted(set(e['quelle'].split(' ')[0] for e in st))},
        lam_m_negativ=all(e['lam_m'] < 0 for e in st), lam_p_positiv=all(e['lam_p'] > 0 for e in st),
        max_abs_dS0=max(abs(e['dS0']) for e in st),
        max_abs_dS0_R_ab_10=max(abs(e['dS0']) for e in st if e['R'] >= 10),
        max_rel_k_mitte=max(abs(e['k_mitte'] / e['k_innen'] - 1) for e in st),
        max_rel_k_mitte_R_ab_10=max(abs(e['k_mitte'] / e['k_innen'] - 1) for e in st if e['R'] >= 10),
        chi0_ueber_1e3=[[e['l'], e['k'], e['R'], e['chi0']] for e in st if e['chi0'] > 1e-3],
        max_abs_rest_minus_rest_wurzel=max(abs(p['rest'] - p['rest_wurzel']) for p in paare),
        max_abs_rest_minus_rest_wurzel_R_ab_10=max((abs(p['rest'] - p['rest_wurzel']) for p in paare
                                                     if p['R_n'] >= 10), default=None))
    # LF0
    erg['LF0'] = dict(eingetroffen=bool(k0['K0_bestanden']),
                      werte=[{x: e[x] for x in ('quelle', 'k', 'pi_k', 'karte', 'd_karte', 'r18_3stellig', 'd_r18',
                                                'pi_k_wurzel', 'S0', 'S0_wurzel', 'bestanden')} for e in k0['stellen']])
    # LF1
    m1 = [p for p in gez if p['l'] == 0 and p['R_n'] >= 15]
    a1 = anteil_tol(m1)
    erg['LF1'] = dict(a1, eingetroffen=bool(a1['n'] and a1['anteil'] >= 0.8), rest=stat([p['rest'] for p in m1]))
    # LF2
    m2 = [p for p in gez if p['l'] in (1, 2) and p['R_n'] >= 10]
    a2 = anteil_tol(m2)
    m2o = [p for p in m2 if not p['flag']]
    a2o = anteil_tol(m2o)
    erg['LF2'] = dict(a2, eingetroffen=bool(a2['n'] and a2['anteil'] >= 0.7), rest=stat([p['rest'] for p in m2]),
                      ohne_gekennzeichnete=dict(a2o, eingetroffen=bool(a2o['n'] and a2o['anteil'] >= 0.7)),
                      je_l={l: anteil_tol([p for p in m2 if p['l'] == l]) for l in (1, 2)})
    # LF3
    m3 = [p for p in gez if p['l'] == 0]
    phi_abw = float(np.mean([abs(p['rest']) for p in m3]))
    pik_abw = float(np.mean([abs(p['rel_pik']) for p in m3]))
    m3b = [p for p in m3 if p['R_n'] >= 15]
    erg['LF3'] = dict(n=len(m3), mittel_abs_rest=phi_abw, mittel_abs_rel_pik=pik_abw,
                      eingetroffen=bool(phi_abw < pik_abw),
                      nebenlesart_R_ab_15=dict(n=len(m3b), mittel_abs_rest=float(np.mean([abs(p['rest']) for p in m3b])),
                                               mittel_abs_rel_pik=float(np.mean([abs(p['rel_pik']) for p in m3b]))),
                      rel_pik=stat([p['rel_pik'] for p in m3]))
    # LF4
    v4 = vorzeichen(gez)
    erg['LF4'] = dict(v4, eingetroffen=bool(v4['n'] and v4['anteil_mehrheit'] >= 0.8),
                      je_l={l: vorzeichen([p for p in gez if p['l'] == l]) for l in (0, 1, 2)},
                      LF1_menge=vorzeichen(m1), LF2_menge=vorzeichen(m2))
    # Beschreibung (PLAN 6)
    besch = dict(je_l={}, l0_je_k={}, l0_k0=[], mcmahon={})
    for l in (0, 1, 2):
        pl = [p for p in gez if p['l'] == l]
        besch['je_l'][l] = dict(rest=stat([p['rest'] for p in pl]),
                                spearman_rest_R=spearman([p['R_n'] for p in pl], [p['rest'] for p in pl]),
                                R_ab_10=stat([p['rest'] for p in pl if p['R_n'] >= 10]),
                                R_unter_10=stat([p['rest'] for p in pl if p['R_n'] < 10]))
    for k in sorted(set(p['k'] for p in gez if p['l'] == 0)):
        pk = [p for p in gez if p['l'] == 0 and p['k'] == k]
        if len(pk) >= 3:
            besch['l0_je_k'][k] = dict(stat([p['rest'] for p in pk]),
                                       spearman_rest_R=spearman([p['R_n'] for p in pk], [p['rest'] for p in pk]))
    besch['l0_k0'] = [[p['R_n'], p['rest']] for p in gez if p['l'] == 0 and p['k'] == 0]
    for l in (1, 2):
        pl = [p for p in gez if p['l'] == l]
        besch['mcmahon'][l] = dict(rest=stat([p['rest'] for p in pl]), mcmahon=stat([p['mcmahon'] for p in pl]),
                                   rest_minus_mcmahon=stat([p['rest'] - p['mcmahon'] for p in pl]),
                                   R_ab_10_rest_minus_mcmahon=stat([p['rest'] - p['mcmahon'] for p in pl
                                                                    if p['R_n'] >= 10]))
    erg['beschreibung'] = besch
    erg['paare'] = paare
    schreibe(aus, erg)
    # Tabelle
    z = ['| l | k | R_n | R_n+1 | gemessener Abstand | pi/k_innen (Mittel) | Delta Phi / pi | Restabweichung | '
         'gezaehlt | Merker |', '|---|---|---|---|---|---|---|---|---|---|']
    for p in paare:
        merk = []
        if not p['wechsel']:
            merk.append('Umlauf ohne Wechsel')
        if not p['abstand_ok']:
            merk.append('Abstand > 1,5 Median')
        if p['flag']:
            merk.append('gekennzeichnete Stelle R = 22,29')
        if p['chi0_max'] > 1e-3:
            merk.append('chi0 = %s' % komma(p['chi0_max'], '%.1e'))
        z.append('| %d | %d | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            p['l'], p['k'], komma(p['R_n'], '%.3f'), komma(p['R_n1'], '%.3f'), komma(p['dR'], '%.4f'),
            komma(p['pik_mittel'], '%.4f'), komma(p['dphi_pi'], '%.4f'), komma(p['rest'], '%+.4f'),
            'ja' if p['gezaehlt'] else 'nein', '; '.join(merk) if merk else '-'))
    with open(md, 'w') as fh:
        fh.write('\n'.join(z) + '\n')
    log('Paare %d, gezaehlt %d' % (len(paare), len(gez)))
    for x in ('LF1', 'LF2', 'LF3', 'LF4'):
        log(x, json.dumps({kk: vv for kk, vv in erg[x].items() if kk not in ('je_l',)})[:600])
    log('LF0', erg['LF0']['eingetroffen'])
    log('Kontrollen', json.dumps(erg['kontrollen'])[:900])


def main():
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == 'k0':
        cmd_k0(a[0], a[1], a[2])
    elif c == 'stellen':
        cmd_stellen(a[0], a[1], a[2], int(a[3]), int(a[4]))
    elif c == 'ausw':
        cmd_ausw(a[0], a[1], a[2], *a[3:])
    else:
        raise SystemExit('unbekannt: ' + c)
    log('fertig')


if __name__ == '__main__':
    main()
