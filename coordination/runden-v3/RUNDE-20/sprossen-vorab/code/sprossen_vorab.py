#!/usr/bin/env python3
"""sprossen_vorab.py - Runde 20 SPROSSEN-VORAB, Code-Agent (2026-10-02). Verfahren: PLAN.md (eingefroren).

Grundlage: huellen_leiter3.py (HUELLEN-LEITER-3, unveraendert importiert: Variante S fuer Lagen, Variante F fuer den
Umlauf, gedaempfter Newton auf W, Rechteck-Umlauf, Zeilenrechnung), huellen_leiter2.py, stille3.py, beutel.py
(unveraendert). Neu: Kurvenzuordnung nur ueber Rang und Stetigkeit von rho(R) (keine Knotenzahl), Befehle test,
ausw, fortfehler.
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import time
import glob
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import huellen_leiter3 as H3   # unveraendert
HL2 = H3.HL2
S3 = H3.S3

W_GRENZE = 1e-9          # Karte: |W| <= 1e-9 (begruendet in HUELLEN-LEITER-3)
SVR_GRENZE = 1e-6        # Rangabfall sigma2/sigma1
RANG_TOL = 1e-6          # Abstand Wurzel zur Nullstelle der Zeile mit Rang k
STETIG_FAKTOR = 0.1      # Karte: kleiner als ein Zehntel des Abstands zur Nachbarkurve
FENSTER = 0.5            # Karte: gefunden = angenommen innerhalb +-0,5 in R
STUFEN_TOL = 1e-6        # Karte: Stufen auf 1e-6
ABSTAND_BEKANNT = 1.0    # Fortsetzung aus den letzten drei bekannten Stellen mit R < R_ziel - 1
NACHSTARTS = (0.0, -0.25, 0.25)
T0 = time.time()

L4_ZIELE = [(0, 39.594), (0, 42.004), (1, 40.506), (1, 42.613), (2, 40.229), (2, 42.351), (3, 39.765), (3, 41.912),
            (4, 36.92), (5, 38.26), (6, 37.19), (7, 38.27)]
TEST_ZIELE = [(0, 44.414), (1, 44.720), (2, 44.473), (3, 44.059), (4, 39.13), (4, 41.33), (5, 40.51), (5, 42.76),
              (6, 39.51), (6, 41.83), (7, 40.65), (7, 43.03)]
TOLERANZ = {0: 0.06, 1: 0.06, 2: 0.06, 3: 0.06, 4: 0.12, 5: 0.12, 6: 0.12, 7: 0.12}


def log(*a):
    print('[%7.1fs]' % (time.time() - T0), *a, flush=True)


schreibe = HL2.schreibe


# ------------------------------------------------------------------ Fortsetzung und Nachbarabstand (PLAN 2)
def fort_punkte(bek, k, R_ziel):
    return sorted([d for d in bek if d['k'] == k and d['R'] < R_ziel - ABSTAND_BEKANNT], key=lambda d: d['R'])[-3:]


def rho_fort(st, R):
    """Quadratisches Polynom in x = 1/R durch drei Stellen (Lagrange), ausgewertet bei 1/R."""
    assert len(st) == 3
    x = [1.0 / d['R'] for d in st]
    y = [d['rho'] for d in st]
    x0 = 1.0 / R
    out = 0.0
    for i in range(3):
        li = 1.0
        for j in range(3):
            if j != i:
                li *= (x0 - x[j]) / (x[i] - x[j])
        out += li * y[i]
    return float(out)


def nachbarabstand(kv):
    """Abstand der Nullstelle mit Rang j zu den Nullstellen mit Rang j - 1 und j + 1 derselben Zeile (kleinerer)."""
    rr = kv['rho_null']
    j = kv['rang']
    c = []
    if j > 0:
        c.append(rr[j] - rr[j - 1])
    if j + 1 < len(rr):
        c.append(rr[j + 1] - rr[j])
    return float(min(c)) if c else float('nan')


# ------------------------------------------------------------------ Test (L4 und Sprossen, gleicher Code)
def cmd_test(stufe, pdir, listejson, bekjson, tab1json, aus, auswahl, modus):
    mod = S3.modell_von('M2')
    liste = json.load(open(listejson))['w2']
    bek = json.load(open(bekjson))['stellen']
    tab = H3.tabelle_R(tab1json)
    erg = dict(stufe=stufe, modus=modus, sprossen=[])
    for item in auswahl.split(','):
        k, Rp = int(item.split(':')[0]), float(item.split(':')[1])
        st = fort_punkte(bek, k, Rp)
        sp = dict(k=k, R_ziel=Rp, fort_aus=[dict(quelle=d['quelle'], R=d['R'], rho=d['rho']) for d in st], versuche=[])
        gefunden = None
        for dR in NACHSTARTS:
            Rs = Rp + dR
            t1 = time.time()
            w2s = H3.w2_von_R(tab, Rs)
            rhos = rho_fort(st, Rs)
            za, anker = H3.anker_von(pdir, liste, w2s)
            U = S3.Umgebung(mod, anker)
            v = dict(R_start=Rs, start=[w2s, rhos], anker=za, r_m=U.n_m * anker['hp'])
            H3.setze_variante('S')
            w2, rho, ok, verl, fehler = H3.newton_W(U, w2s, rhos)
            S = dict(w2=w2, rho=rho, ok=ok, verl=verl, fehler=fehler)
            if fehler is None:
                try:
                    S.update(H3.am_punkt(mod, U, w2, rho))
                except Exception as ex:
                    S['fehler'] = repr(ex)
            v['S'] = S
            pruef = dict(konv=bool(ok and S.get('fehler') is None and S.get('absW', 1.0) <= W_GRENZE),
                         W_woertlich=bool(ok and S.get('absW', 1.0) < 1e-10),
                         svr=bool(S.get('svr', 1.0) <= SVR_GRENZE),
                         bereich=bool(S.get('bereich') == 'E1'))
            if pruef['konv'] and pruef['bereich']:
                try:
                    kv = H3.kurve_an(mod, U, w2, rho)
                except Exception as ex:
                    kv = dict(rang=None, fehler=repr(ex))
                v['kurve'] = kv
                pruef['rang'] = bool(kv.get('rang') == k and abs(kv.get('d_rho', 1.0)) <= RANG_TOL)
                if kv.get('rang') is not None:
                    d_nb = nachbarabstand(kv)
                    rf = rho_fort(st, S['Rchi'])
                    e = abs(rho - rf)
                    v['stetig'] = dict(rho_fort=rf, fehler=float(e), d_nb=d_nb, schwelle=STETIG_FAKTOR * d_nb,
                                       verhaeltnis=float(e / d_nb) if d_nb > 0 else None, rang_bezug=kv['rang'])
                    pruef['stetig'] = bool(np.isfinite(d_nb) and d_nb > 0 and e < STETIG_FAKTOR * d_nb)
                else:
                    pruef['stetig'] = False
                pruef['fenster'] = bool(abs(S['Rchi'] - Rp) <= FENSTER)
            v['pruef'] = pruef
            v['lokal_ok'] = bool(all(pruef.get(x, False) for x in ('konv', 'svr', 'bereich', 'rang', 'stetig',
                                                                     'fenster')))
            # Umlauf (F ab der S-Wurzel) und S-Rechteck (Information) nur fuer den Kandidaten, wie HUELLEN-LEITER-3
            if v['lokal_ok']:
                H3.setze_variante('F')
                t2 = time.time()
                w2F, rhoF, okF, verlF, fF = H3.newton_W(U, w2, rho)
                F = dict(w2=w2F, rho=rhoF, ok=okF, verl=verlF, fehler=fF, dw2=w2F - w2, drho=rhoF - rho)
                if fF is None:
                    F.update(H3.am_punkt(mod, U, w2F, rhoF))
                F['sekunden_newton'] = time.time() - t2
                dwz = H3.dw2_zeile_an(liste, w2)
                hmax = H3.halbbreite(mod, w2, rho, v['kurve']['gap'], dwz)
                v['hmax'] = hmax
                v['dw2_zeile'] = dwz
                if okF:
                    F['umlauf'] = H3.rechteck(U, w2F, rhoF, H3.halbbreite(mod, w2F, rhoF, v['kurve']['gap'], dwz))
                v['F'] = F
                H3.setze_variante('S')
                S['umlauf'] = H3.rechteck(U, w2, rho, hmax)
            v['sekunden'] = time.time() - t1
            v['statF'] = dict(H3.STATF)
            v['statS'] = dict(HL2.STAT)
            sp['versuche'].append(v)
            erg['sprossen'] = [q for q in erg['sprossen'] if not (q['k'] == k and q['R_ziel'] == Rp)] + [sp]
            schreibe(aus, erg)
            log('%s k=%d Rz=%.3f Rs=%.3f stufe=%d S ok=%s w2=%.10f rho=%.10f R=%s |W|=%s svr=%s stetig=%s pruef=%s | '
                '%.1fs' % (modus, k, Rp, Rs, stufe, ok, w2, rho, S.get('Rchi'), S.get('absW'), S.get('svr'),
                           json.dumps(v.get('stetig')), json.dumps(pruef), v['sekunden']))
            if v['lokal_ok']:
                gefunden = len(sp['versuche']) - 1
                break
        sp['gefunden_versuch'] = gefunden
        schreibe(aus, erg)
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


# ------------------------------------------------------------------ Auswertung
def lade(adir, modus, st):
    out = {}
    for fn in sorted(glob.glob(os.path.join(adir, modus, '%s-st%d-*.json' % (modus, st)))):
        for q in json.load(open(fn))['sprossen']:
            out[(q['k'], round(q['R_ziel'], 3))] = q
    return out


def zeile_auswerten(sp, k, Rz):
    z = dict(k=k, R_ziel=Rz)
    v = {}
    for st in (1, 2):
        q = sp[st].get((k, round(Rz, 3)))
        if q is None:
            z['st%d' % st] = dict(fehlt=True)
            continue
        g = q.get('gefunden_versuch')
        vv = q['versuche'][g] if g is not None else (q['versuche'][-1] if q['versuche'] else None)
        v[st] = vv
        if vv is None:
            z['st%d' % st] = dict(fehlt=True)
            continue
        S, F, kv, ste = vv['S'], vv.get('F', {}), vv.get('kurve', {}), vv.get('stetig', {})
        z['st%d' % st] = dict(versuch=g, n_versuche=len(q['versuche']), lokal_ok=vv['lokal_ok'], pruef=vv['pruef'],
                             w2=S['w2'], rho=S['rho'], R=S.get('Rchi'), absW=S.get('absW'), svr=S.get('svr'),
                             it=len(S['verl']), rang=kv.get('rang'), d_rho=kv.get('d_rho'), n_null=kv.get('n'),
                             knoten_info=kv.get('knoten'), gap=kv.get('gap'), rho_fort=ste.get('rho_fort'),
                             fort_fehler=ste.get('fehler'), d_nb=ste.get('d_nb'), verhaeltnis=ste.get('verhaeltnis'),
                             umlauf_F=F.get('umlauf', {}).get('umlauf'), aufgeloest_F=F.get('umlauf', {}).get('aufgeloest'),
                             sprung_F=F.get('umlauf', {}).get('groesster_sprung'),
                             punkte_F=F.get('umlauf', {}).get('punkte'), versuch_F=F.get('umlauf', {}).get('versuch'),
                             umlauf_S=S.get('umlauf', {}).get('umlauf'), aufgeloest_S=S.get('umlauf', {}).get('aufgeloest'),
                             F_ok=F.get('ok'), dF=[F.get('dw2'), F.get('drho')], hmax=vv.get('hmax'),
                             fort_aus=q['fort_aus'], sekunden=[x['sekunden'] for x in q['versuche']])
    ok12 = all(st in v and v[st] is not None and v[st]['lokal_ok'] for st in (1, 2))
    if ok12:
        dst = [v[2]['S']['w2'] - v[1]['S']['w2'], v[2]['S']['rho'] - v[1]['S']['rho']]
        uml = [v[st].get('F', {}).get('umlauf', {}) for st in (1, 2)]
        z['d_stufen'] = dst
        z['umlauf_ok'] = bool(all(u.get('aufgeloest') and abs(u.get('umlauf', 0)) == 1 for u in uml))
        z['stufen_ok'] = bool(abs(dst[0]) <= STUFEN_TOL and abs(dst[1]) <= STUFEN_TOL)
        z['angenommen'] = bool(z['umlauf_ok'] and z['stufen_ok'])
    else:
        z['angenommen'] = False
    if z['angenommen']:
        z['R_gefunden'] = v[1]['S']['Rchi']
        z['dR'] = z['R_gefunden'] - Rz
        z['umlauf'] = [v[1]['F']['umlauf']['umlauf'], v[2]['F']['umlauf']['umlauf']]
    return z


def ausw(adir, bekjson, modus, aus, l4json=None):
    bek = json.load(open(bekjson))
    sp = {st: lade(adir, modus, st) for st in (1, 2)}
    ziele = L4_ZIELE if modus == 'l4' else TEST_ZIELE
    zeilen = [zeile_auswerten(sp, k, Rz) for k, Rz in ziele]
    erg = dict(modus=modus, sprossen=zeilen)
    if modus == 'l4':
        # Bezug: die bekannte Stelle selbst (Abstand der S-Wurzel Stufe 1 zur bekannten Lage, nur berichtet)
        for z in zeilen:
            kand = [d for d in bek['stellen'] if d['k'] == z['k'] and abs(d['R'] - z['R_ziel']) < 0.01]
            if kand and 'w2' in z.get('st1', {}):
                d = kand[0]
                z['bekannt'] = dict(quelle=d['quelle'], R=d['R'], w2=d['w2'], rho=d['rho'],
                                    umlauf_bekannt=d.get('umlauf_bekannt'),
                                    d_w2=z['st1']['w2'] - d['w2'], d_rho=z['st1']['rho'] - d['rho'])
        erg['bestanden'] = bool(all(z['angenommen'] for z in zeilen))
        erg['n_angenommen'] = int(sum(z['angenommen'] for z in zeilen))
        log('L4 bestanden=%s (%d von %d)' % (erg['bestanden'], erg['n_angenommen'], len(zeilen)))
    else:
        l4 = json.load(open(l4json))
        for z in zeilen:
            z['toleranz'] = TOLERANZ[z['k']]
            z['gefunden'] = bool(z['angenommen'] and abs(z['dR']) <= FENSTER)
            z['treffer'] = bool(z['angenommen'] and abs(z['dR']) <= TOLERANZ[z['k']])
            hb = bek['bekannte_stelle_hl2']
            z['nicht_blind'] = bool(z['angenommen'] and abs(z['R_gefunden'] - hb['R']) <= 0.01
                                    and abs(z['st1']['rho'] - hb['rho']) <= 0.005)
        v1 = [z for z in zeilen if z['k'] <= 3]
        v2 = [z for z in zeilen if z['k'] >= 4]
        V1 = 'eingetroffen' if all(z['treffer'] for z in v1) else 'nicht eingetroffen'
        n2 = int(sum(z['treffer'] for z in v2))
        V2 = 'eingetroffen' if n2 >= 7 else 'nicht eingetroffen'
        nb = [z for z in v2 if z['nicht_blind']]
        if nb:
            rest = [z for z in v2 if not z['nicht_blind']]
            n2b = int(sum(z['treffer'] for z in rest))
            V2b = dict(ohne=[(z['k'], z['R_ziel']) for z in nb], n_treffer=n2b, n=len(rest),
                       ausgang=('eingetroffen' if n2b >= len(rest) - 1 else 'nicht eingetroffen'))
        else:
            V2b = dict(ohne=[], ausgang='nicht anwendbar (keine angenommene Sprosse faellt mit der Stelle zusammen)')
        # V3: Folgen je Kurve, F-Umlauf beider Stufen
        l4z = {(z['k'], round(z['R_ziel'], 3)): z for z in l4['sprossen']}
        anfang = {0: [(0, 39.594), (0, 42.004)], 1: [(1, 40.506), (1, 42.613)], 2: [(2, 40.229), (2, 42.351)],
                  3: [(3, 39.765), (3, 41.912)], 4: [(4, 36.92)], 5: [(5, 38.26)], 6: [(6, 37.19)], 7: [(7, 38.27)]}
        schritte, folgen = [], {}
        for k in range(8):
            folge = []
            for kk, Rz in anfang[k]:
                q = l4z.get((kk, round(Rz, 3)))
                folge.append(dict(name='bekannt %.3f' % Rz, R=q.get('R_gefunden') if q else None,
                                  umlauf=q.get('umlauf') if q and q['angenommen'] else None, neu=False))
            for z in [z for z in zeilen if z['k'] == k]:
                folge.append(dict(name='neu %.3f' % z['R_ziel'], R=z.get('R_gefunden'),
                                  umlauf=z.get('umlauf') if z['angenommen'] else None, neu=True))
            folgen[k] = folge
            for a, b in zip(folge[:-1], folge[1:]):
                if not b['neu']:
                    continue          # gewertet werden nur Schritte zu einer neuen Sprosse
                if a['umlauf'] is None or b['umlauf'] is None:
                    continue
                gleich_a = a['umlauf'][0] == a['umlauf'][1]
                gleich_b = b['umlauf'][0] == b['umlauf'][1]
                erf = bool(gleich_a and gleich_b and a['umlauf'][0] == -b['umlauf'][0] and a['umlauf'][0] in (1, -1))
                schritte.append(dict(k=k, von=a['name'], nach=b['name'], umlauf_von=a['umlauf'], umlauf_nach=b['umlauf'],
                                     erfuellt=erf))
        if not schritte:
            V3 = 'offen'
        elif all(s['erfuellt'] for s in schritte):
            V3 = 'eingetroffen'
        else:
            V3 = 'nicht eingetroffen'
        gross = [dict(k=z['k'], R_ziel=z['R_ziel'], dR=z.get('dR'), angenommen=z['angenommen']) for z in zeilen
                 if (not z['gefunden']) or abs(z['dR']) > 0.3]
        if not l4['bestanden']:
            bed = 'nicht auswertbar (L4 nicht bestanden)'
        elif V1 == 'eingetroffen' and V2 == 'eingetroffen' and V3 == 'eingetroffen':
            bed = 'Die Sprossenregel sagt neue stille Stellen vorab gewertet voraus [H, im Modell gestuetzt]'
        elif gross:
            bed = 'Die Regel bricht jenseits R ~ 42 zusammen; Grund suchen'
        else:
            bed = 'Zwischenausgang (keine der beiden Aussagen der Karte)'
        erg.update(V0_l4_bestanden=l4['bestanden'], V1=V1, V1_treffer=[z['treffer'] for z in v1], V2=V2, V2_n_treffer=n2,
                   V2_nebenlesart=V2b, V3=V3, V3_schritte=schritte, V3_folgen=folgen, ausloeser_abweichung=gross,
                   bedeutung=bed)
        log('V1=%s V2=%s (%d von 8) V3=%s Bedeutung=%s' % (V1, V2, n2, V3, bed))
    schreibe(aus, erg)


# ------------------------------------------------------------------ Fortsetzungsfehler an bekannten Stellen (Bericht)
def cmd_fortfehler(bekjson, aus):
    bek = json.load(open(bekjson))['stellen']
    out = []
    for k in sorted(set(d['k'] for d in bek)):
        kurve = sorted([d for d in bek if d['k'] == k], key=lambda d: d['R'])
        for i, d in enumerate(kurve):
            e = dict(k=k, quelle=d['quelle'], R=d['R'], rho=d['rho'], gap=d.get('gap'))
            for name, Rgrenze in (('ein_schritt', d['R']), ('zwei_schritte', kurve[i - 1]['R'] if i > 0 else None)):
                if Rgrenze is None:
                    continue
                st = fort_punkte(bek, k, Rgrenze)
                if len(st) < 3:
                    continue
                f = d['rho'] - rho_fort(st, d['R'])
                e[name] = dict(fehler=f, aus=[x['quelle'] for x in st], verhaeltnis_gap=(abs(f) / d['gap']
                                                                                         if d.get('gap') else None))
            out.append(e)
    schreibe(aus, dict(regel='Fortsetzung: quadratisch in 1/R durch die letzten drei bekannten Stellen mit R < R_grenze - 1; '
                             'ein_schritt: R_grenze = R der Stelle; zwei_schritte: R_grenze = R der Vorgaengerstelle. '
                             'gap: Nachbarabstand der Runde 18 (Zeilenpaar) bzw. der Zeile an der HL3-Wurzel',
                       stellen=out))
    log('fortfehler', len(out))


def main():
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == 'test':
        cmd_test(int(a[0]), a[1], a[2], a[3], a[4], a[5], a[6], a[7])
    elif c == 'ausw':
        ausw(a[0], a[1], a[2], a[3], a[4] if len(a) > 4 else None)
    elif c == 'fortfehler':
        cmd_fortfehler(a[0], a[1])
    else:
        raise SystemExit('unbekannt: ' + c)
    log('fertig', json.dumps(dict(F=H3.STATF, S=HL2.STAT)))


if __name__ == '__main__':
    main()
