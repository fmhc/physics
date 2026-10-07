#!/usr/bin/env python3
"""sprossen_l1l2.py - Runde 21 SPROSSEN-L1L2, Code-Agent (2026-10-02). Verfahren: PLAN.md (eingefroren).

Grundlage (unveraendert importiert): l = 1: dipol.py (HUELLEN-DIPOL), l = 2: quadrupol.py (HUELLEN-QUADRUPOL). Beide
importieren stille3.py (Code 1), huellen_leiter.py (Runde 18) und beutel.py unveraendert und ersetzen zur Laufzeit
HL.werte_k, S3.regulaer und S3.abklingend durch die l-Fassungen. Newton auf W (S3.newton_E1), Rechteck-Umlauf
(S3.umlauf_mit_rueckfall), Zeile (HL.zeile_k), Profile (HL.cmd_profile) und Zeilenregel (HL.cmd_liste) wie dort.
Neu sind nur die Startpunkte (vorhergesagtes R), die Kurvenzuordnung ueber Rang und Stetigkeit von rho(R) und die Wertung.
Aufruf: python sprossen_l1l2.py ell=<1|2> <befehl> <argumente>
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import time
import math
import glob
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)

ELL = None
if len(sys.argv) > 1 and sys.argv[1].startswith('ell='):
    ELL = int(sys.argv[1][4:])
if ELL == 1:
    import dipol as LM          # HUELLEN-DIPOL, unveraendert
elif ELL == 2:
    import quadrupol as LM      # HUELLEN-QUADRUPOL, unveraendert
    LM.ELL = 2
else:
    raise SystemExit('erstes Argument: ell=1 oder ell=2')
S3 = LM.S3
HL = LM.HL

W_GRENZE = 1e-9          # Karte: |W| <= 1e-9
SVR_GRENZE = 1e-6        # Rangabfall sigma2/sigma1
RANG_TOL = 1e-6          # Abstand Wurzel zur Nullstelle der Zeile mit Rang k
STETIG_FAKTOR = 0.1      # Karte: kleiner als ein Zehntel des Abstands zur Nachbarkurve
FENSTER = 0.5            # Karte: gefunden = angenommen innerhalb +-0,5 in R
STUFEN_TOL = 1e-6        # Karte: Stufen auf 1e-6
ABSTAND_BEKANNT = 1.0    # Stuetzstellen: bekannte Stellen mit R < R_ziel - 1
NACHSTARTS = (0.0, -0.25, 0.25)
W2_UNTEN_NEU = 0.78      # Hintergruende bis omega^2 = 0,78 (R ~ 26)
GROSS = 0.3              # Bedeutung: Abweichung > 0,3
T0 = time.time()

L4_ZIELE = {1: [(0, 16.593), (0, 19.02), (1, 15.839), (1, 18.024), (2, 17.094), (2, 19.378), (3, 15.584), (3, 18.1)],
            2: [(0, 15.172), (0, 17.63), (1, 16.565), (1, 18.787), (2, 15.268), (2, 17.68)]}
# Karte (woertlich, mit Berichtigung der Leitung 17:56:55: l = 1, k = 1, P2 zweite Sprosse 22,316)
VORHERSAGE = {1: {0: dict(satz='A', plin=(21.447, 23.874), p2=(21.443, 23.862)),
                  1: dict(satz='A', plin=(20.209, 22.394), p2=(20.182, 22.316)),
                  2: dict(satz='A', plin=(21.662, 23.946), p2=(21.607, 23.789)),
                  3: dict(satz='B', plin=(20.616, 23.132), p2=(None, None))},
              2: {0: dict(satz='A', plin=(20.088, 22.546), p2=(20.071, 22.498)),
                  1: dict(satz='A', plin=(21.009, 23.231), p2=(20.973, 23.129)),
                  2: dict(satz='B', plin=(20.092, 22.504), p2=(19.972, 22.162))}}
W1_TOL = 0.06
W2_TOL = 0.15


def log(*a):
    print('[%7.1fs]' % (time.time() - T0), *a, flush=True)


schreibe = S3.schreibe


# ------------------------------------------------------------------ Fortsetzung und Nachbarabstand (PLAN 3)
def stuetz_vor(bek, k, R_ziel):
    """Die letzten drei bekannten Stellen der Kurve k mit R < R_ziel - 1."""
    return sorted([d for d in bek if d['k'] == k and d['R'] < R_ziel - ABSTAND_BEKANNT], key=lambda d: d['R'])[-3:]


def fort_punkte(bek, k, R_ziel):
    """Stuetzstellen (PLAN 3): mindestens zwei Stellen vor dem Ziel -> 'vor'; sonst die Fortsetzung des Tests fuer diese
    Kurve (letzte drei bzw. zwei bekannte Stellen) -> 'formal' (nur in L4 moeglich, Zielstelle ist dann Stuetzstelle)."""
    st = stuetz_vor(bek, k, R_ziel)
    if len(st) >= 2:
        return st, 'vor'
    kurve = sorted([d for d in bek if d['k'] == k], key=lambda d: d['R'])
    return kurve[-3:], 'formal'


def rho_fort(st, R):
    """Polynom in x = 1/R durch die Stuetzstellen (Lagrange): drei -> quadratisch, zwei -> Gerade."""
    n = len(st)
    if n == 0:
        return float('nan')
    x = [1.0 / d['R'] for d in st]
    y = [d['rho'] for d in st]
    x0 = 1.0 / R
    out = 0.0
    for i in range(n):
        li = 1.0
        for j in range(n):
            if j != i:
                li *= (x0 - x[j]) / (x[i] - x[j])
        out += li * y[i]
    return float(out)


def nachbarabstand(kv):
    """Kleinerer Abstand der Nullstelle mit Rang j zu den Nullstellen mit Rang j - 1 und j + 1 derselben Zeile."""
    rr = kv['rho_null']
    j = kv['rang']
    c = []
    if j > 0:
        c.append(rr[j] - rr[j - 1])
    if j + 1 < len(rr):
        c.append(rr[j + 1] - rr[j])
    return float(min(c)) if c else float('nan')


# ------------------------------------------------------------------ Hilfen (wie HUELLEN-DIPOL/-QUADRUPOL bzw. Vorbild)
def tabelle_R(tab1json):
    info = json.load(open(tab1json))
    t = sorted(((d['Rchi'], d['w2']) for d in info if np.isfinite(d.get('Rchi', float('nan')))))
    return np.array([a for a, b in t]), np.array([b for a, b in t])


def w2_von_R(tab, R):
    Rs, ws = tab
    return float(np.interp(R, Rs, ws))


def anker_von(pdir, liste, w2):
    """Wie HL.cmd_umlauf: naechste Zeile mit omega^2 <= Start (groesseres Gebiet)."""
    kand = [x for x in liste if x <= w2]
    za = max(kand) if kand else min(liste)
    return za, S3.lade_profil(HL.ppfad(pdir, za))


def dw2_zeile_an(liste, w2):
    s = sorted(liste, reverse=True)
    for a, b in zip(s[:-1], s[1:]):
        if a >= w2 > b:
            return a - b
    return abs(s[-2] - s[-1])


def am_punkt(mod, U, w2, rho):
    v = U.werte(S3.werte_E1, [w2], [rho])
    pr = U.profil(w2)
    return dict(W=[float(v['W'][0].real), float(v['W'][0].imag)], absW=float(abs(v['W'][0])), svr=float(v['svr'][0]),
                m_ab=float(v['m_ab'][0]), Rchi=HL.r_chi(pr), chi0=float(pr['chi0']), bereich=S3.bereich(mod, w2, rho))


def kurve_an(mod, U, w2, rho):
    """Rang der naechsten Nullstelle von m_bc von unten in der Zeile bei omega^2 der Wurzel (HL.zeile_k, l-Fassung)."""
    p = dict(U.profil(w2))
    p['Rchi'] = HL.r_chi(p)
    p['m0sq'] = HL.m0sq(mod, p)
    t1 = time.time()
    d = HL.zeile_k(mod, p)
    rr = np.array([z['rho'] for z in d['null']])
    if len(rr) == 0:
        return dict(rang=None, n=0, sekunden=time.time() - t1)
    j = int(np.argmin(np.abs(rr - rho)))
    gap = HL.luecke(d, j)
    return dict(rang=j, d_rho=float(rr[j] - rho), knoten=int(d['null'][j]['knoten']), n=int(len(rr)),
                rho_null=[float(x) for x in rr], knoten_alle=[int(z['knoten']) for z in d['null']],
                sicher=[bool(z['sicher']) for z in d['null']], vorzeichen=d['vorzeichen'], gap=gap, lo=d['lo'],
                hi=d['hi'], sekunden=time.time() - t1)


def halbbreite(mod, w2, rho, gap, dw2_zeile):
    """Wie HL.cmd_umlauf: min(1e-3, 0,4 Schwellenabstand, 0,25 Luecke, 0,5 Zeilenabstand)."""
    w = math.sqrt(w2)
    abst = min(rho - (math.sqrt(mod.m2) - w), math.sqrt(mod.mc2) - rho, w + math.sqrt(mod.m2) - rho)
    return min(S3.HALB, 0.4 * abst, 0.25 * gap, 0.5 * dw2_zeile)


def rechteck(U, w2, rho, hmax):
    t1 = time.time()
    e = S3.umlauf_mit_rueckfall(U, S3.werte_E1, 'W', w2, rho, hmax)
    e['hmax'] = hmax
    e['sekunden'] = time.time() - t1
    return e


# ------------------------------------------------------------------ Befehle Vorbereitung
def cmd_liste(aus):
    HL.W2_UNTEN = W2_UNTEN_NEU      # Runde-18-Regel wie HUELLEN-DIPOL, Untergrenze 0,78
    HL.cmd_liste(aus)


def cmd_pruef(dateien):
    import py_compile
    for f in dateien:
        py_compile.compile(f, doraise=True)
        log('py_compile ok', f)


# ------------------------------------------------------------------ Test (L4 und Sprossen, gleicher Code)
def cmd_test(stufe, pdir, listejson, bekjson, tab1json, aus, auswahl, modus):
    mod = S3.modell_von('M2')
    liste = json.load(open(listejson))['w2']
    bek = json.load(open(bekjson))['stellen']
    assert all(int(d['ell']) == ELL for d in bek), 'bekannte Stellen passen nicht zu l'
    tab = tabelle_R(tab1json)
    erg = dict(ell=ELL, stufe=stufe, modus=modus, sprossen=[])
    for item in auswahl.split(','):
        k, Rz = int(item.split(':')[0]), float(item.split(':')[1])
        st, art = fort_punkte(bek, k, Rz)
        sp = dict(ell=ELL, k=k, R_ziel=Rz, fort_art=art,
                  fort_aus=[dict(quelle=d['quelle'], R=d['R'], rho=d['rho']) for d in st], versuche=[])
        gefunden = None
        for dR in NACHSTARTS:
            Rs = Rz + dR
            t1 = time.time()
            w2s = w2_von_R(tab, Rs)
            rhos = rho_fort(st, Rs)
            za, anker = anker_von(pdir, liste, w2s)
            U = S3.Umgebung(mod, anker)
            v = dict(R_start=Rs, start=[w2s, rhos], anker=za, r_m=U.n_m * anker['hp'], N=anker['N'])
            fehler = None
            try:
                w2, rho, ok, verl = S3.newton_E1(U, w2s, rhos)
            except Exception as ex:
                w2, rho, ok, verl, fehler = w2s, rhos, False, [], repr(ex)
            S = dict(w2=w2, rho=rho, ok=ok, verl=verl, fehler=fehler)
            if fehler is None:
                try:
                    S.update(am_punkt(mod, U, w2, rho))
                except Exception as ex:
                    S['fehler'] = repr(ex)
            v['S'] = S
            pruef = dict(konv=bool(ok and S.get('fehler') is None and S.get('absW', 1.0) <= W_GRENZE),
                         W_1e10=bool(ok and S.get('absW', 1.0) < 1e-10),
                         svr=bool(S.get('svr', 1.0) <= SVR_GRENZE),
                         bereich=bool(S.get('bereich') == 'E1'))
            kv = None
            if pruef['konv'] and pruef['bereich']:
                try:
                    kv = kurve_an(mod, U, w2, rho)
                except Exception as ex:
                    kv = dict(rang=None, fehler=repr(ex))
                v['kurve'] = kv
                pruef['rang'] = bool(kv.get('rang') == k and abs(kv.get('d_rho', 1.0)) <= RANG_TOL)
                if kv.get('rang') is not None:
                    d_nb = nachbarabstand(kv)
                    rf = rho_fort(st, S['Rchi'])
                    e = abs(rho - rf)
                    v['stetig'] = dict(rho_fort=rf, fehler=float(e), d_nb=d_nb, schwelle=STETIG_FAKTOR * d_nb,
                                       verhaeltnis=(float(e / d_nb) if d_nb > 0 else None), rang_bezug=kv['rang'],
                                       art=art)
                    pruef['stetig'] = bool(np.isfinite(d_nb) and d_nb > 0 and e < STETIG_FAKTOR * d_nb)
                else:
                    pruef['stetig'] = False
                pruef['fenster'] = bool(abs(S['Rchi'] - Rz) <= FENSTER)
            v['pruef'] = pruef
            v['lokal_ok'] = bool(all(pruef.get(x, False) for x in ('konv', 'svr', 'bereich', 'rang', 'stetig',
                                                                     'fenster')))
            if v['lokal_ok']:
                dwz = dw2_zeile_an(liste, w2)
                hmax = halbbreite(mod, w2, rho, kv['gap'], dwz)
                v['hmax'] = hmax
                v['dw2_zeile'] = dwz
                S['umlauf'] = rechteck(U, w2, rho, hmax)
            v['sekunden'] = time.time() - t1
            sp['versuche'].append(v)
            erg['sprossen'] = [q for q in erg['sprossen'] if not (q['k'] == k and q['R_ziel'] == Rz)] + [sp]
            schreibe(aus, erg)
            um = S.get('umlauf', {})
            log('%s l=%d k=%d Rz=%.3f Rs=%.3f stufe=%d ok=%s w2=%.10f rho=%.10f R=%s |W|=%s svr=%s stetig=%s '
                'pruef=%s umlauf=%s/%s | %.1fs' % (modus, ELL, k, Rz, Rs, stufe, ok, w2, rho, S.get('Rchi'),
                                                    S.get('absW'), S.get('svr'), json.dumps(v.get('stetig')),
                                                    json.dumps(pruef), um.get('umlauf'), um.get('aufgeloest'),
                                                    v['sekunden']))
            if v['lokal_ok']:
                gefunden = len(sp['versuche']) - 1
                break
        sp['gefunden_versuch'] = gefunden
        schreibe(aus, erg)
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


# ------------------------------------------------------------------ Auswertung (reine Datenrechnung)
def lade(adir, modus):
    out = {}
    for fn in sorted(glob.glob(os.path.join(adir, '%s-l*-st*-*.json' % modus))):
        d = json.load(open(fn))
        for q in d['sprossen']:
            out[(int(d['ell']), int(d['stufe']), int(q['k']), round(q['R_ziel'], 3))] = q
    return out


def zeile_auswerten(sp, ell, k, Rz):
    z = dict(ell=ell, k=k, R_ziel=Rz)
    v = {}
    for st in (1, 2):
        q = sp.get((ell, st, k, round(Rz, 3)))
        if q is None:
            z['st%d' % st] = dict(fehlt=True)
            continue
        g = q.get('gefunden_versuch')
        vv = q['versuche'][g] if g is not None else (q['versuche'][-1] if q['versuche'] else None)
        v[st] = vv
        if vv is None:
            z['st%d' % st] = dict(fehlt=True)
            continue
        S, kv, ste = vv['S'], vv.get('kurve', {}), vv.get('stetig', {})
        um = S.get('umlauf', {})
        z['st%d' % st] = dict(versuch=g, n_versuche=len(q['versuche']), lokal_ok=vv['lokal_ok'], pruef=vv['pruef'],
                             w2=S['w2'], rho=S['rho'], R=S.get('Rchi'), absW=S.get('absW'), svr=S.get('svr'),
                             it=len(S['verl']), rang=kv.get('rang'), d_rho=kv.get('d_rho'), n_null=kv.get('n'),
                             knoten_info=kv.get('knoten'), gap=kv.get('gap'), rho_fort=ste.get('rho_fort'),
                             fort_fehler=ste.get('fehler'), d_nb=ste.get('d_nb'), verhaeltnis=ste.get('verhaeltnis'),
                             fort_art=q.get('fort_art'), umlauf=um.get('umlauf'), aufgeloest=um.get('aufgeloest'),
                             sprung=um.get('groesster_sprung'), punkte=um.get('punkte'), versuch_rechteck=um.get('versuch'),
                             hmax=vv.get('hmax'), anker=vv.get('anker'), fort_aus=q['fort_aus'],
                             sekunden=[x['sekunden'] for x in q['versuche']], start=vv.get('start'),
                             R_start=vv.get('R_start'))
    ok12 = all(st in v and v[st] is not None and v[st]['lokal_ok'] for st in (1, 2))
    if ok12:
        dst = [v[2]['S']['w2'] - v[1]['S']['w2'], v[2]['S']['rho'] - v[1]['S']['rho']]
        uml = [v[st]['S'].get('umlauf', {}) for st in (1, 2)]
        z['d_stufen'] = dst
        z['umlauf_ok'] = bool(all(u.get('aufgeloest') and abs(u.get('umlauf', 0)) == 1 for u in uml))
        z['stufen_ok'] = bool(abs(dst[0]) <= STUFEN_TOL and abs(dst[1]) <= STUFEN_TOL)
        z['angenommen'] = bool(z['umlauf_ok'] and z['stufen_ok'])
    else:
        z['angenommen'] = False
    if z['angenommen']:
        z['R_gefunden'] = v[1]['S']['Rchi']
        z['dR'] = z['R_gefunden'] - Rz
        z['umlauf'] = [v[1]['S']['umlauf']['umlauf'], v[2]['S']['umlauf']['umlauf']]
    return z


def schritt_ok(a, b):
    return bool(a['umlauf'] is not None and b['umlauf'] is not None and a['umlauf'][0] == a['umlauf'][1]
                and b['umlauf'][0] == b['umlauf'][1] and a['umlauf'][0] in (1, -1) and a['umlauf'][0] == -b['umlauf'][0])


def cmd_ausw(adir, bek1json, bek2json, modus, aus, l4json=None):
    bek = {1: json.load(open(bek1json))['stellen'], 2: json.load(open(bek2json))['stellen']}
    sp = lade(adir, modus)
    erg = dict(modus=modus)
    if modus == 'l4':
        zeilen = []
        for ell in (1, 2):
            for k, Rz in L4_ZIELE[ell]:
                z = zeile_auswerten(sp, ell, k, Rz)
                kand = [d for d in bek[ell] if d['k'] == k and abs(d['R'] - Rz) < 0.01]
                if kand and 'w2' in z.get('st1', {}):
                    d = kand[0]
                    b = dict(quelle=d['quelle'], R=d['R'], w2=d['w2'], rho=d['rho'], umlauf_zelle=d['umlauf_zelle'],
                             d_w2_zelle=z['st1']['w2'] - d['w2'], d_rho_zelle=z['st1']['rho'] - d['rho'])
                    for st in (1, 2):
                        n = d.get('newton_st%d' % st)
                        if n and 'w2' in z.get('st%d' % st, {}):
                            b['newton_st%d' % st] = dict(w2=n['w2'], rho=n['rho'], umlauf=n['umlauf'],
                                                         d_w2=z['st%d' % st]['w2'] - n['w2'],
                                                         d_rho=z['st%d' % st]['rho'] - n['rho'])
                    z['bekannt'] = b
                    if z['angenommen']:
                        z['umlauf_wie_bekannt'] = bool(z['umlauf'][0] == b.get('newton_st1', {}).get('umlauf')
                                                       and z['umlauf'][1] == b.get('newton_st2', {}).get('umlauf'))
                zeilen.append(z)
        erg['sprossen'] = zeilen
        erg['bestanden'] = bool(all(z['angenommen'] for z in zeilen))
        erg['n_angenommen'] = int(sum(z['angenommen'] for z in zeilen))
        erg['n'] = len(zeilen)
        log('L4 bestanden=%s (%d von %d)' % (erg['bestanden'], erg['n_angenommen'], len(zeilen)))
    else:
        l4 = json.load(open(l4json))
        l4z = {(z['ell'], z['k'], round(z['R_ziel'], 3)): z for z in l4['sprossen']}
        zeilen = []
        for ell in (1, 2):
            for k in sorted(VORHERSAGE[ell]):
                vh = VORHERSAGE[ell][k]
                for i in (0, 1):
                    z = zeile_auswerten(sp, ell, k, vh['plin'][i])
                    z.update(satz=vh['satz'], sprosse=i + 1, P_lin=vh['plin'][i], P2=vh['p2'][i])
                    z['gefunden'] = bool(z['angenommen'] and abs(z['dR']) <= FENSTER)
                    if z['angenommen']:
                        z['dev_lin'] = z['R_gefunden'] - vh['plin'][i]
                        z['dev_p2'] = (z['R_gefunden'] - vh['p2'][i]) if vh['p2'][i] is not None else None
                    tol = W1_TOL if i == 0 else W2_TOL
                    z['toleranz_lin'] = tol
                    z['treffer_lin'] = bool(z['angenommen'] and abs(z['dev_lin']) <= tol)
                    zeilen.append(z)
        erg['sprossen'] = zeilen
        A = [z for z in zeilen if z['satz'] == 'A']
        A1 = [z for z in A if z['sprosse'] == 1]
        A2 = [z for z in A if z['sprosse'] == 2]
        W1 = 'eingetroffen' if all(z['treffer_lin'] for z in A1) else 'nicht eingetroffen'
        n2 = int(sum(z['treffer_lin'] for z in A2))
        W2 = 'eingetroffen' if n2 >= 4 else 'nicht eingetroffen'
        # W3: Folgen je Kurve (letzte bekannte Stelle aus L4, dann die zwei neuen), Umlauf beider Stufen
        folgen, schritte = {}, []
        for ell in (1, 2):
            for k in sorted(VORHERSAGE[ell]):
                Rl = max(R for kk, R in L4_ZIELE[ell] if kk == k)
                q = l4z.get((ell, k, round(Rl, 3)))
                folge = [dict(name='bekannt %.3f' % Rl, R=q.get('R_gefunden') if q else None,
                              umlauf=q.get('umlauf') if q and q['angenommen'] else None, neu=False)]
                for z in [z for z in zeilen if z['ell'] == ell and z['k'] == k]:
                    folge.append(dict(name='neu %.3f' % z['R_ziel'], R=z.get('R_gefunden'),
                                      umlauf=z.get('umlauf') if z['angenommen'] else None, neu=True))
                folgen['l%d-k%d' % (ell, k)] = folge
                for a, b in zip(folge[:-1], folge[1:]):
                    if a['umlauf'] is None or b['umlauf'] is None:
                        continue
                    schritte.append(dict(ell=ell, k=k, satz=VORHERSAGE[ell][k]['satz'], von=a['name'], nach=b['name'],
                                         umlauf_von=a['umlauf'], umlauf_nach=b['umlauf'], erfuellt=schritt_ok(a, b)))
        sA = [s for s in schritte if s['satz'] == 'A']
        kurven_A = [(ell, k) for ell in (1, 2) for k in VORHERSAGE[ell] if VORHERSAGE[ell][k]['satz'] == 'A']
        jede = all(any(s['ell'] == ell and s['k'] == k for s in sA) for ell, k in kurven_A)
        if any(not s['erfuellt'] for s in sA):
            W3 = 'nicht eingetroffen'
        elif sA and jede:
            W3 = 'eingetroffen'
        else:
            W3 = 'offen'
        # W4: mittlere Abweichung (Betrag) ueber die angenommenen Satz-A-Sprossen, gleiche Menge fuer beide Regeln
        An = [z for z in A if z['angenommen']]
        if An:
            m_lin = float(np.mean([abs(z['dev_lin']) for z in An]))
            m_p2 = float(np.mean([abs(z['dev_p2']) for z in An]))
            W4 = 'eingetroffen' if m_p2 < m_lin else 'nicht eingetroffen'
            W4z = dict(n=len(An), mittel_abs_lin=m_lin, mittel_abs_p2=m_p2,
                       mittel_lin=float(np.mean([z['dev_lin'] for z in An])),
                       mittel_p2=float(np.mean([z['dev_p2'] for z in An])))
        else:
            W4, W4z = 'offen', dict(n=0)
        gross = [dict(ell=z['ell'], k=z['k'], sprosse=z['sprosse'], R_ziel=z['R_ziel'], dev_lin=z.get('dev_lin'),
                      angenommen=z['angenommen']) for z in A if (not z['gefunden']) or abs(z['dev_lin']) > GROSS]
        bed = []
        if not l4['bestanden']:
            bed.append('nicht auswertbar (L4 nicht bestanden)')
        else:
            if W1 == 'eingetroffen' and W2 == 'eingetroffen' and W3 == 'eingetroffen':
                bed.append('Die Sprossenregel sagt auch l = 1- und l = 2-Stellen vorab voraus [H, im Modell gestuetzt]')
            elif gross:
                bed.append('Die Regel traegt fuer l > 0 nicht')
            else:
                bed.append('Zwischenausgang (weder W1 bis W3 eingetroffen noch Abweichung > 0,3 bei Satz A)')
            if W4 == 'eingetroffen':
                bed.append('Der schrumpfende Abstand verbessert die Vorhersage; das stuetzt das Bild '
                           'Delta R ~ pi/k_innen(R) [H]')
        B = [z for z in zeilen if z['satz'] == 'B']
        Bn = [z for z in B if z['angenommen']]
        satzB = dict(n=len(B), n_angenommen=len(Bn),
                     treffer_lin=[(z['ell'], z['k'], z['sprosse'], z['treffer_lin']) for z in B],
                     schritte=[s for s in schritte if s['satz'] == 'B'])
        erg.update(L4_bestanden=l4['bestanden'], W1=W1, W1_treffer=[z['treffer_lin'] for z in A1], W2=W2,
                   W2_n_treffer=n2, W3=W3, W3_schritte=schritte, W3_folgen=folgen, W4=W4, W4_zahlen=W4z,
                   ausloeser_abweichung=gross, bedeutung=bed, satz_B=satzB)
        log('W1=%s W2=%s (%d von 5) W3=%s W4=%s %s Bedeutung=%s' % (W1, W2, n2, W3, W4, json.dumps(W4z), bed))
    schreibe(aus, erg)


# ------------------------------------------------------------------ Fortsetzungsfehler an allen bekannten Stellen
def cmd_fortfehler(bek1json, bek2json, aus):
    out = []
    for ell, fn in ((1, bek1json), (2, bek2json)):
        bek = json.load(open(fn))['stellen']
        for k in sorted(set(d['k'] for d in bek)):
            kurve = sorted([d for d in bek if d['k'] == k], key=lambda d: d['R'])
            for i, d in enumerate(kurve):
                e = dict(ell=ell, k=k, quelle=d['quelle'], R=d['R'], rho=d['rho'], gap=d.get('gap'))
                for name, Rgrenze in (('ein_schritt', d['R']), ('zwei_schritte', kurve[i - 1]['R'] if i > 0 else None)):
                    if Rgrenze is None:
                        continue
                    st = stuetz_vor(bek, k, Rgrenze)
                    if len(st) < 2:
                        continue
                    f = d['rho'] - rho_fort(st, d['R'])
                    e[name] = dict(fehler=f, grad=len(st) - 1, aus=[x['quelle'] for x in st],
                                   verhaeltnis_gap=(abs(f) / d['gap'] if d.get('gap') else None))
                out.append(e)
    schreibe(aus, dict(regel='Fortsetzung: Polynom in 1/R durch die letzten drei (zwei: Gerade) bekannten Stellen der '
                             'Kurve mit R < R_grenze - 1; ein_schritt: R_grenze = R der Stelle; zwei_schritte: '
                             'R_grenze = R der Vorgaengerstelle. gap: Luecke der Vorlaeufer (stellen.json)',
                       stellen=out))
    log('fortfehler', len(out))


def main():
    a = sys.argv[2:]
    c = a[0]
    a = a[1:]
    log('l =', ELL, 'Befehl', c)
    if c == 'pruef':
        cmd_pruef(a)
    elif c == 'liste':
        cmd_liste(a[0])
    elif c == 'profile':
        HL.cmd_profile('M2', int(a[0]), a[1], a[2], weiter=(len(a) > 3 and a[3] == 'weiter'))
    elif c == 'test':
        cmd_test(int(a[0]), a[1], a[2], a[3], a[4], a[5], a[6], a[7])
    elif c == 'ausw':
        cmd_ausw(a[0], a[1], a[2], a[3], a[4], a[5] if len(a) > 5 else None)
    elif c == 'fortfehler':
        cmd_fortfehler(a[0], a[1], a[2])
    else:
        raise SystemExit('unbekannt: ' + c)
    log('fertig')


if __name__ == '__main__':
    main()
