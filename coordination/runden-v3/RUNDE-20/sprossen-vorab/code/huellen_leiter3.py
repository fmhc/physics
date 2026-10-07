#!/usr/bin/env python3
"""huellen_leiter3.py - Runde 19 HUELLEN-LEITER-3, Code-Agent (2026-10-02). Verfahren: PLAN.md (eingefroren).

Grundlage: huellen_leiter2.py (HUELLEN-LEITER-2, unveraendert importiert; Variante S = PotStab, chi < 1e-12 -> 0)
und stille3.py (Code 1, unveraendert). Neu: Variante F (chi im Inneren durch die analytische Fortsetzung
chi(r_a) sinh(m0 r)/r / (sinh(m0 r_a)/r_a) ersetzt), gedaempfter Newton auf W, Befehle k0, test, auswertung.
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
os.environ['KOPPLUNG'] = 'stab'
import sys
import json
import time
import math
import glob
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import huellen_leiter2 as HL2   # unveraendert (Variante S, Zeilen, Profile)
S3 = HL2.S3                    # Code 1, unveraendert

CHI_SCHWELLE = HL2.CHI_SCHWELLE
OrigPot = HL2.OrigPot
PotStab = HL2.PotStab
STATF = dict(n_pot=0, n_punkte=0, n_fort=0, n_luecke=0, n_aenderung_aa=0, n_aenderung_ab=0, n_aenderung_ac=0,
             n_aenderung_cc=0, chi0_F_min=None, chi0_F_max=None)
KNOTEN_R18 = {0: 0, 1: 0, 2: 2, 3: 2}     # Zeilen 100 bis 110 der Runde 18, beide Stufen (PLAN 4)
W_GRENZE = 1e-9                           # PLAN 4 (Abweichung, Grund dort); woertlich 1e-10 wird berichtet
SVR_GRENZE = 1e-6
T0 = time.time()


def log(*a):
    print('[%7.1fs]' % (time.time() - T0), *a, flush=True)


schreibe = HL2.schreibe


# ------------------------------------------------------------------ Variante F
def chi_fort(mod, r, S, g):
    """chi_F: Punkte mit Index <= i_s (groesster Index mit g < 1e-12) durch die Fortsetzung ersetzt."""
    m = g < CHI_SCHWELLE
    if not m.any():
        return g, dict(n_fort=0, n_luecke=0)
    i_s = int(np.nonzero(m)[0].max())
    ia = i_s + 1
    m0 = math.sqrt(float(mod.d(float(S[0]), 0.0)[3]))

    def phi(x):
        x = np.asarray(x, float)
        out = np.full(x.shape, m0)
        z = x > 0
        out[z] = np.sinh(m0 * x[z]) / x[z]
        return out
    ge = g.copy()
    ge[:ia] = g[ia] * phi(r[:ia]) / float(phi(r[ia:ia + 1])[0])
    return ge, dict(n_fort=ia, n_luecke=int(np.sum(~m[:ia])), m0=m0, r_a=float(r[ia]), chi_a=float(g[ia]),
                    chi0_F=float(ge[0]))


class PotFort(OrigPot):
    def __init__(self, mod, profs):
        self.hp = profs[0]['hp']
        self.N = profs[0]['N']
        K = len(profs)
        self.K = K
        self.Maa = np.empty((K, self.N + 1))
        self.Mab = np.empty((K, self.N + 1))
        self.Mac = np.empty((K, self.N + 1))
        self.Mcc = np.empty((K, self.N + 1))
        for q, p in enumerate(profs):
            assert p['N'] == self.N and abs(p['hp'] - self.hp) < 1e-15
            r, f, g = S3.fg_aus(p['F'], p['H'], self.hp, self.N)
            S = f * f
            ge, info = chi_fort(mod, r, S, g)
            US, USS, Ug, Ugg, USg = mod.d(S, ge)
            self.Maa[q] = US + S * USS
            self.Mab[q] = S * USS
            self.Mac[q] = f * USg
            self.Mcc[q] = Ugg
            US0, USS0, Ug0, Ugg0, USg0 = mod.d(S, g)
            STATF['n_pot'] += 1
            STATF['n_punkte'] += int(len(g))
            STATF['n_fort'] += info['n_fort']
            STATF['n_luecke'] += info['n_luecke']
            STATF['n_aenderung_aa'] += int(np.sum((US0 + S * USS0) != self.Maa[q]))
            STATF['n_aenderung_ab'] += int(np.sum((S * USS0) != self.Mab[q]))
            STATF['n_aenderung_ac'] += int(np.sum((f * USg0) != self.Mac[q]))
            STATF['n_aenderung_cc'] += int(np.sum(Ugg0 != self.Mcc[q]))
            if info['n_fort']:
                c0 = info['chi0_F']
                STATF['chi0_F_min'] = c0 if STATF['chi0_F_min'] is None else min(STATF['chi0_F_min'], c0)
                STATF['chi0_F_max'] = c0 if STATF['chi0_F_max'] is None else max(STATF['chi0_F_max'], c0)


VARIANTEN = {'alt': OrigPot, 'S': PotStab, 'F': PotFort}


def setze_variante(v):
    S3.Pot = VARIANTEN[v]


# ------------------------------------------------------------------ Newton, Rechteck, Kurve
def newton_W(U, w2, rho, maxit=30, dw=1e-6, dr=1e-6, cap_w=2e-4, cap_r=2e-3):
    """Gedaempfter Newton auf W = m_ac + i m_bc (PLAN 2)."""
    verl = []
    ok = False
    fehler = None
    for it in range(maxit):
        try:
            W = U.werte(S3.werte_E1, [w2, w2 + dw, w2], [rho, rho, rho + dr])['W']
        except Exception as ex:
            fehler = repr(ex)
            break
        J11 = (W[1].real - W[0].real) / dw
        J21 = (W[1].imag - W[0].imag) / dw
        J12 = (W[2].real - W[0].real) / dr
        J22 = (W[2].imag - W[0].imag) / dr
        det = J11 * J22 - J12 * J21
        dx = -(J22 * W[0].real - J12 * W[0].imag) / det
        dy = -(-J21 * W[0].real + J11 * W[0].imag) / det
        if not (np.isfinite(dx) and np.isfinite(dy)):
            fehler = 'Schritt nicht endlich'
            break
        s = max(abs(dx), abs(dy))
        fak = 1.0
        if abs(dx) > cap_w:
            fak = min(fak, cap_w / abs(dx))
        if abs(dy) > cap_r:
            fak = min(fak, cap_r / abs(dy))
        w2 += fak * dx
        rho += fak * dy
        verl.append([float(s), float(fak)])
        if s < 1e-10:
            ok = True
            break
    return float(w2), float(rho), ok, verl, fehler


def am_punkt(mod, U, w2, rho):
    v = U.werte(S3.werte_E1, [w2], [rho])
    pr = U.profil(w2)
    return dict(W=[float(v['W'][0].real), float(v['W'][0].imag)], absW=float(abs(v['W'][0])),
                svr=float(v['svr'][0]), m_ab=float(v['m_ab'][0]), Rchi=HL2.r_chi(pr), chi0=float(pr['chi0']),
                bereich=S3.bereich(mod, w2, rho))


def halbbreite(mod, w2, rho, gap, dw2_zeile):
    w = math.sqrt(w2)
    abst = min(rho - (math.sqrt(mod.m2) - w), math.sqrt(mod.mc2) - rho, w + math.sqrt(mod.m2) - rho)
    return min(S3.HALB, 0.4 * abst, 0.25 * gap, 0.5 * dw2_zeile)


def rechteck(U, w2, rho, hmax):
    t1 = time.time()
    e = S3.umlauf_mit_rueckfall(U, S3.werte_E1, 'W', w2, rho, hmax)
    e['hmax'] = hmax
    e['sekunden'] = time.time() - t1
    return e


def kurve_an(mod, U, w2, rho):
    """Rang der Nullstelle von m_bc von unten in der Zeile bei w2 (zeile_k aus HUELLEN-LEITER-2), Knotenzahl."""
    p = dict(U.profil(w2))
    p['Rchi'] = HL2.r_chi(p)
    p['m0sq'] = HL2.m0sq(mod, p)
    t1 = time.time()
    d = HL2.zeile_k(mod, p)
    rr = np.array([z['rho'] for z in d['null']])
    if len(rr) == 0:
        return dict(rang=None, n=0, sekunden=time.time() - t1)
    j = int(np.argmin(np.abs(rr - rho)))
    gap = HL2.luecke(d, j)
    return dict(rang=j, d_rho=float(rr[j] - rho), knoten=int(d['null'][j]['knoten']), n=int(len(rr)),
                rho_null=[float(x) for x in rr], knoten_alle=[int(z['knoten']) for z in d['null']],
                sicher=[bool(z['sicher']) for z in d['null']], gap=gap, lo=d['lo'], hi=d['hi'],
                sekunden=time.time() - t1)


def anker_von(pdir, liste, w2):
    kand = [x for x in liste if x <= w2]
    za = max(kand) if kand else min(liste)
    return za, S3.lade_profil(HL2.ppfad(pdir, za))


def dw2_zeile_an(liste, w2):
    s = sorted(liste, reverse=True)
    for a, b in zip(s[:-1], s[1:]):
        if a >= w2 > b:
            return a - b
    return abs(s[-2] - s[-1])


# ------------------------------------------------------------------ K0'
def cmd_k0(stufe, pdir, listejson, refjson, aus, nrs, modus):
    mod = S3.modell_von('M2')
    liste = json.load(open(listejson))['w2']
    ref = {d['nr']: d for d in json.load(open(refjson))['stellen']}
    erg = dict(stufe=stufe, modus=modus, punkte=[])
    for nr in nrs:
        d = ref[nr]
        w2s = d['w2'] if stufe == 1 else d['w2_2']
        rhos = d['rho'] if stufe == 1 else d['rho_2']
        za, anker = anker_von(pdir, liste, w2s)
        U = S3.Umgebung(mod, anker)
        e = dict(nr=nr, k=d['k'], R=d['R'], start=[w2s, rhos], anker=za, r_m=U.n_m * anker['hp'],
                 umlauf_r18=d['umlauf_1'] if stufe == 1 else d['umlauf_2'], gap=d['gap'], dw2_zeile=d['dw2_zeile'])
        varianten = ('alt', 'S', 'F') if modus == 'haupt' else ('S',)
        for var in varianten:
            setze_variante(var)
            t1 = time.time()
            w2, rho, ok, verl, fehler = newton_W(U, w2s, rhos)
            x = dict(w2=w2, rho=rho, ok=ok, verl=verl, fehler=fehler)
            if fehler is None:
                x.update(am_punkt(mod, U, w2, rho))
            x['sekunden_newton'] = time.time() - t1
            e[var] = x
        uvar = 'F' if modus == 'haupt' else 'S'
        setze_variante(uvar)
        x = e[uvar]
        if x['ok']:
            hmax = halbbreite(mod, x['w2'], x['rho'], d['gap'], d['dw2_zeile'])
            x['umlauf'] = rechteck(U, x['w2'], x['rho'], hmax)
        setze_variante('S')
        e['statF'] = dict(STATF)
        e['statS'] = dict(HL2.STAT)
        erg['punkte'].append(e)
        schreibe(aus, erg)
        kurz = {v: (e[v]['ok'], e[v]['w2'], e[v]['rho']) for v in varianten}
        log('k0 nr=%d k=%d stufe=%d %s umlauf(%s)=%s' % (nr, d['k'], stufe, json.dumps(kurz), uvar,
            json.dumps({k: x.get('umlauf', {}).get(k) for k in ('umlauf', 'aufgeloest', 'groesster_sprung', 'punkte',
                                                              'sekunden')})))
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


# ------------------------------------------------------------------ Test
def tabelle_R(tab1json):
    info = json.load(open(tab1json))
    t = sorted(((d['Rchi'], d['w2']) for d in info if np.isfinite(d.get('Rchi', float('nan')))))
    return np.array([a for a, b in t]), np.array([b for a, b in t])


def w2_von_R(tab, R):
    Rs, ws = tab
    return float(np.interp(R, Rs, ws))


def rho_start(ref, k, R):
    st = sorted([d for d in ref if d['gezaehlt'] and d['bereich'] and d['k'] == k], key=lambda d: d['R'])[-3:]
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
    return float(out), [d['nr'] for d in st]


def cmd_test(stufe, pdir, listejson, refjson, tab1json, aus, auswahl):
    mod = S3.modell_von('M2')
    liste = json.load(open(listejson))['w2']
    ref = json.load(open(refjson))['stellen']
    tab = tabelle_R(tab1json)
    erg = dict(stufe=stufe, sprossen=[])
    for item in auswahl.split(','):
        k, Rp = int(item.split(':')[0]), float(item.split(':')[1])
        sp = dict(k=k, R_vorhergesagt=Rp, kontaminiert=bool(k == 1 and abs(Rp - 40.51) < 1e-9), versuche=[])
        gefunden = None
        for Rs in (Rp, Rp - 0.25, Rp + 0.25):
            t1 = time.time()
            w2s = w2_von_R(tab, Rs)
            rhos, nrs = rho_start(ref, k, Rs)
            za, anker = anker_von(pdir, liste, w2s)
            U = S3.Umgebung(mod, anker)
            v = dict(R_start=Rs, start=[w2s, rhos], rho_aus=nrs, anker=za, r_m=U.n_m * anker['hp'])
            setze_variante('S')
            w2, rho, ok, verl, fehler = newton_W(U, w2s, rhos)
            S = dict(w2=w2, rho=rho, ok=ok, verl=verl, fehler=fehler)
            if fehler is None:
                try:
                    S.update(am_punkt(mod, U, w2, rho))
                except Exception as ex:
                    S['fehler'] = repr(ex)
            v['S'] = S
            pruef = dict(konv=bool(ok and S.get('fehler') is None and S.get('absW', 1.0) <= W_GRENZE),
                         W_woertlich=bool(ok and S.get('absW', 1.0) < 1e-10),
                         svr=bool(S.get('svr', 1.0) <= SVR_GRENZE),
                         bereich=bool(S.get('bereich') == 'E1'))
            if pruef['konv'] and pruef['bereich']:
                try:
                    kv = kurve_an(mod, U, w2, rho)
                except Exception as ex:
                    kv = dict(rang=None, fehler=repr(ex))
                v['kurve'] = kv
                pruef['kurve'] = bool(kv.get('rang') == k and abs(kv.get('d_rho', 1.0)) <= 1e-6)
                pruef['knoten'] = bool(kv.get('knoten') == KNOTEN_R18[k])
                pruef['fenster'] = bool(abs(S['Rchi'] - Rp) <= 0.5)
            v['pruef'] = pruef
            v['lokal_ok'] = bool(all(pruef.get(x, False) for x in ('konv', 'svr', 'bereich', 'kurve', 'knoten',
                                                                     'fenster')))
            # Kontrolle (F ab der S-Wurzel) und Rechtecke nur fuer den Kandidaten
            if v['lokal_ok']:
                setze_variante('F')
                t2 = time.time()
                w2F, rhoF, okF, verlF, fF = newton_W(U, w2, rho)
                F = dict(w2=w2F, rho=rhoF, ok=okF, verl=verlF, fehler=fF, dw2=w2F - w2, drho=rhoF - rho)
                if fF is None:
                    F.update(am_punkt(mod, U, w2F, rhoF))
                F['sekunden_newton'] = time.time() - t2
                dwz = dw2_zeile_an(liste, w2)
                hmax = halbbreite(mod, w2, rho, v['kurve']['gap'], dwz)
                v['hmax'] = hmax
                v['dw2_zeile'] = dwz
                if okF:
                    F['umlauf'] = rechteck(U, w2F, rhoF, halbbreite(mod, w2F, rhoF, v['kurve']['gap'], dwz))
                v['F'] = F
                setze_variante('S')
                S['umlauf'] = rechteck(U, w2, rho, hmax)
            v['sekunden'] = time.time() - t1
            v['statF'] = dict(STATF)
            v['statS'] = dict(HL2.STAT)
            sp['versuche'].append(v)
            erg['sprossen'] = [q for q in erg['sprossen'] if not (q['k'] == k and q['R_vorhergesagt'] == Rp)] + [sp]
            schreibe(aus, erg)
            log('test k=%d Rp=%.2f Rs=%.2f stufe=%d S ok=%s w2=%.10f rho=%.10f R=%s |W|=%s svr=%s pruef=%s | %.1fs' % (
                k, Rp, Rs, stufe, ok, w2, rho, S.get('Rchi'), S.get('absW'), S.get('svr'), json.dumps(pruef),
                v['sekunden']))
            if v['lokal_ok']:
                gefunden = len(sp['versuche']) - 1
                break
        sp['gefunden_versuch'] = gefunden
        schreibe(aus, erg)
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


# ------------------------------------------------------------------ Auswertung
def lade_punkte(muster, schl):
    out = []
    for fn in sorted(glob.glob(muster)):
        out += json.load(open(fn))[schl]
    return out


def ausw_k0(adir, refjson, aus):
    ref = {d['nr']: d for d in json.load(open(refjson))['stellen']}
    nrs = [62, 72, 81, 69, 78, 88, 68, 76, 85, 65, 74, 83]
    zeilen = []
    alle = True
    for nr in nrs:
        z = dict(nr=nr, k=ref[nr]['k'], R=ref[nr]['R'])
        for st in (1, 2):
            pk = [p for p in lade_punkte(os.path.join(adir, 'k0', 'k0-st%d-*.json' % st), 'punkte') if p['nr'] == nr]
            ps = [p for p in lade_punkte(os.path.join(adir, 'k0', 'k0s-st%d-*.json' % st), 'punkte') if p['nr'] == nr]
            if not pk:
                z['st%d' % st] = dict(fehlt=True)
                alle = False
                continue
            p = pk[-1]
            a, S, F = p['alt'], p['S'], p['F']
            u = F.get('umlauf', {})
            dS = [S['w2'] - a['w2'], S['rho'] - a['rho']]
            dF = [F['w2'] - a['w2'], F['rho'] - a['rho']]
            k0a = bool(a['ok'] and S['ok'] and abs(dS[0]) <= 1e-8 and abs(dS[1]) <= 1e-8)
            kF = bool(F['ok'] and abs(dF[0]) <= 1e-8 and abs(dF[1]) <= 1e-8)
            k0b = bool(u.get('aufgeloest') and u.get('umlauf') == p['umlauf_r18'])
            uS = ps[-1]['S'].get('umlauf', {}) if ps else {}
            z['st%d' % st] = dict(alt_ok=a['ok'], S_ok=S['ok'], F_ok=F['ok'], dS=dS, dF=dF,
                                 d_tabelle_alt=[a['w2'] - p['start'][0], a['rho'] - p['start'][1]],
                                 absW=dict(alt=a.get('absW'), S=S.get('absW'), F=F.get('absW')),
                                 svr=dict(alt=a.get('svr'), S=S.get('svr'), F=F.get('svr')),
                                 umlauf_r18=p['umlauf_r18'], umlauf_F=u.get('umlauf'), aufgeloest_F=u.get('aufgeloest'),
                                 sprung_F=u.get('groesster_sprung'), punkte_F=u.get('punkte'), hmax_F=u.get('hmax'),
                                 versuch_F=u.get('versuch'), umlauf_S=uS.get('umlauf'), aufgeloest_S=uS.get('aufgeloest'),
                                 sprung_S=uS.get('groesster_sprung'), k0a=k0a, k0F=kF, k0b=k0b,
                                 it=dict(alt=len(a['verl']), S=len(S['verl']), F=len(F['verl'])))
            alle = alle and k0a and kF and k0b
        zeilen.append(z)
    erg = dict(bestanden=bool(alle), stellen=zeilen,
               regel='PLAN 3: K0a S-alt 1e-8, F-alt 1e-8, K0b F-Rechteck aufgeloest = Umlauf R18; 12 Stellen, beide Stufen')
    schreibe(aus, erg)
    log('K0prime bestanden=%s' % alle)


def ausw_test(adir, k0json, aus):
    k0 = json.load(open(k0json))
    letzte = {0: 81, 1: 88, 2: 85, 3: 83}
    vorh = [(0, 39.59), (0, 42.00), (1, 40.51), (1, 42.62), (2, 40.24), (2, 42.36), (3, 39.77), (3, 41.93)]
    sp = {}
    for st in (1, 2):
        for q in lade_punkte(os.path.join(adir, 'test', 'test-st%d-*.json' % st), 'sprossen'):
            sp[(st, q['k'], round(q['R_vorhergesagt'], 2))] = q
    zeilen = []
    for k, Rp in vorh:
        z = dict(k=k, R_vorhergesagt=Rp, kontaminiert=bool(k == 1 and Rp == 40.51))
        v = {}
        for st in (1, 2):
            q = sp.get((st, k, Rp))
            if q is None:
                z['st%d' % st] = dict(fehlt=True)
                continue
            g = q.get('gefunden_versuch')
            vv = q['versuche'][g] if g is not None else (q['versuche'][-1] if q['versuche'] else None)
            v[st] = vv
            if vv is None:
                z['st%d' % st] = dict(fehlt=True)
                continue
            S, F = vv['S'], vv.get('F', {})
            z['st%d' % st] = dict(versuch=g, n_versuche=len(q['versuche']), lokal_ok=vv['lokal_ok'], pruef=vv['pruef'],
                                 w2=S['w2'], rho=S['rho'], R=S.get('Rchi'), absW=S.get('absW'), svr=S.get('svr'),
                                 it=len(S['verl']), rang=vv.get('kurve', {}).get('rang'),
                                 knoten=vv.get('kurve', {}).get('knoten'), gap=vv.get('kurve', {}).get('gap'),
                                 umlauf_F=F.get('umlauf', {}).get('umlauf'),
                                 aufgeloest_F=F.get('umlauf', {}).get('aufgeloest'),
                                 sprung_F=F.get('umlauf', {}).get('groesster_sprung'),
                                 umlauf_S=S.get('umlauf', {}).get('umlauf'),
                                 aufgeloest_S=S.get('umlauf', {}).get('aufgeloest'),
                                 sprung_S=S.get('umlauf', {}).get('groesster_sprung'),
                                 F_ok=F.get('ok'), dF=[F.get('dw2'), F.get('drho')], hmax=vv.get('hmax'))
        ok12 = all(st in v and v[st] is not None and v[st]['lokal_ok'] for st in (1, 2))
        if ok12:
            dst = [v[2]['S']['w2'] - v[1]['S']['w2'], v[2]['S']['rho'] - v[1]['S']['rho']]
            uml = [v[st].get('F', {}).get('umlauf', {}) for st in (1, 2)]
            uml_ok = all(u.get('aufgeloest') and abs(u.get('umlauf', 0)) == 1 for u in uml)
            z['d_stufen'] = dst
            z['umlauf_ok'] = bool(uml_ok)
            z['stufen_ok'] = bool(abs(dst[0]) <= 1e-6 and abs(dst[1]) <= 1e-6)
            z['angenommen'] = bool(uml_ok and z['stufen_ok'])
        else:
            z['angenommen'] = False
        if z['angenommen']:
            z['R_gefunden'] = v[1]['S']['Rchi']
            z['dR'] = z['R_gefunden'] - Rp
            z['umlauf'] = [v[1]['F']['umlauf']['umlauf'], v[2]['F']['umlauf']['umlauf']]
            z['F_kontrolle'] = [dict(ok=v[st]['F']['ok'], dw2=v[st]['F']['dw2'], drho=v[st]['F']['drho'])
                                for st in (1, 2)]
        zeilen.append(z)
    # Kontrolle der Stabilisierung (PLAN 5)
    reihen = sorted([z for z in zeilen if z['angenommen'] and not z['kontaminiert']], key=lambda z: z['R_vorhergesagt'])
    kontr = reihen[:2]
    kontr_ok = bool(len(kontr) == 2 and all(all(c['ok'] and abs(c['dw2']) <= 1e-8 and abs(c['drho']) <= 1e-8
                                                 for c in z['F_kontrolle']) for z in kontr))
    # P1'
    unk = [z for z in zeilen if not z['kontaminiert']]
    p1_treffer = [bool(z['angenommen'] and abs(z['dR']) <= 0.10) for z in unk]
    p1 = 'eingetroffen' if all(p1_treffer) else 'nicht eingetroffen'
    # P2'
    k0st = {s['nr']: s for s in k0['stellen']}
    schritte, schritte_kont = [], []
    for k in range(4):
        u_last = [k0st[letzte[k]]['st%d' % st].get('umlauf_F') for st in (1, 2)]
        folge = [dict(name='Nr %d' % letzte[k], R=k0st[letzte[k]]['R'], umlauf=u_last, kont=False)]
        for z in [z for z in zeilen if z['k'] == k]:
            if z['angenommen']:
                folge.append(dict(name='%.2f' % z['R_vorhergesagt'], R=z['R_gefunden'], umlauf=z['umlauf'],
                                  kont=z['kontaminiert']))
            else:
                folge.append(None)
        for a, b in zip(folge[:-1], folge[1:]):
            if a is None or b is None:
                continue
            gleich_a = a['umlauf'][0] == a['umlauf'][1]
            gleich_b = b['umlauf'][0] == b['umlauf'][1]
            erf = bool(gleich_a and gleich_b and a['umlauf'][0] == -b['umlauf'][0] and a['umlauf'][0] in (1, -1))
            s = dict(k=k, von=a['name'], nach=b['name'], umlauf_von=a['umlauf'], umlauf_nach=b['umlauf'], erfuellt=erf)
            (schritte_kont if (a['kont'] or b['kont']) else schritte).append(s)
    if not schritte:
        p2 = 'offen'
    elif all(s['erfuellt'] for s in schritte):
        p2 = 'eingetroffen'
    else:
        p2 = 'nicht eingetroffen'
    gross = [z for z in unk if (not z['angenommen']) or abs(z['dR']) > 0.3]
    if not k0['bestanden'] or not kontr_ok:
        p1g, p2g, bed = 'offen', 'offen', 'nicht auswertbar (K0prime oder Kontrolle nicht bestanden)'
    else:
        p1g, p2g = p1, p2
        if p1 == 'eingetroffen' and p2 == 'eingetroffen':
            bed = 'Die Sprossenregel sagt neue stille Stellen voraus [H]'
        elif gross:
            bed = 'Die Regel gilt nur im bisherigen Bereich'
        else:
            bed = 'Zwischenausgang (keine der beiden Aussagen der Karte)'
    erg = dict(k0_bestanden=k0['bestanden'], kontrolle=dict(bestanden=kontr_ok, stellen=[
        dict(k=z['k'], R_vorhergesagt=z['R_vorhergesagt'], F=z['F_kontrolle']) for z in kontr]),
        P1=p1g, P1_roh=p1, P1_treffer=p1_treffer, P2=p2g, P2_roh=p2, P2_schritte=schritte,
        P2_schritte_kontaminiert=schritte_kont, bedeutung=bed, sprossen=zeilen,
        max_abs_dR_unkontaminiert=(max(abs(z['dR']) for z in unk if z['angenommen'])
                                   if any(z['angenommen'] for z in unk) else None))
    schreibe(aus, erg)
    log('P1=%s P2=%s Kontrolle=%s Bedeutung=%s' % (p1g, p2g, kontr_ok, bed))


def main():
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == 'profile':
        HL2.cmd_profile(a[0], int(a[1]), a[2], a[3])
    elif c == 'k0':
        cmd_k0(int(a[0]), a[1], a[2], a[3], a[4], [int(x) for x in a[5].split(',')], a[6])
    elif c == 'test':
        cmd_test(int(a[0]), a[1], a[2], a[3], a[4], a[5], a[6])
    elif c == 'ausw-k0':
        ausw_k0(a[0], a[1], a[2])
    elif c == 'ausw-test':
        ausw_test(a[0], a[1], a[2])
    else:
        raise SystemExit('unbekannt: ' + c)
    log('fertig', json.dumps(dict(F=STATF, S=HL2.STAT)))


if __name__ == '__main__':
    main()
