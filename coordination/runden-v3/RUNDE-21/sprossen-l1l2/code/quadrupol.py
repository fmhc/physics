#!/usr/bin/env python3
"""quadrupol.py - Runde 20 HUELLEN-QUADRUPOL, Code-Agent (2026-10-02).

Stille Quadrupol-Stellen (l = 2) in E1 des Zweifeldmodells M2. Methode und Wertung: PLAN.md (eingefroren).
Abgeleitet aus dipol.py (Runde 19, HUELLEN-DIPOL): gleiche Kanalfunktionen, l jetzt als Parameter (0, 1, 2).
Code 1 (stille3.py), HUELLEN-LEITER (huellen_leiter.py) und beutel.py werden unveraendert importiert; zur Laufzeit
werden genau drei Kanalfunktionen durch l-Fassungen ersetzt: HL.werte_k, S3.regulaer, S3.abklingend.
l(l+1)/r^2 in allen drei Kanaelen; regulaerer Start u = r^(l+1) [v + r^2 V0 v / (2(2l+3))] bei r0 = n0 hp (n0 = 2);
abklingender Start (modifizierte Kugel-Bessel-Funktion k_l, u = r k_l(kappa r)):
  l = 0: u'/u = -kappa
  l = 1: u = e^{-x}(1 + 1/x),            u'/u = -(x^2 + x + 1) / (R (x + 1))
  l = 2: u = e^{-x}(1 + 3/x + 3/x^2),    u'/u = -(x^3 + 3x^2 + 6x + 6) / (R (x^2 + 3x + 3)),   x = kappa R.
Aufruf: python quadrupol.py ell=<l> <befehl> <argumente>   (ohne ell=: l = 2)
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
import stille3 as S3            # Code 1, unveraendert
import huellen_leiter as HL     # HUELLEN-LEITER, unveraendert

ELL = 2
N0_START = 2                    # regulaerer Start bei r0 = N0_START hp (Probe: 4)
NZ_RAND = False                 # Probe: abklingender Start der Suche am Gebietsrand statt bei n_start
T0 = time.time()
schreibe = S3.schreibe


def log(*a):
    print('[%7.1fs]' % (time.time() - T0), *a, flush=True)


# ------------------------------------------------------------------ Kanaele mit l (wie dipol.py, l allgemein)
def start_regulaer(pot, qidx, E, ell, n0=None):
    P = E[0].shape[0]
    Y = np.zeros((P, 6, 3))
    if ell == 0:
        for j in range(3):
            Y[:, 3 + j, j] = 1.0
        return Y, 0
    n0 = N0_START if n0 is None else n0
    r0 = n0 * pot.hp
    a0, b0, c0, e0 = pot.an(qidx, 0)

    def vek(x):
        return np.broadcast_to(np.asarray(x, float).reshape(-1), (P,))
    aa, bb, cc, ee = vek(a0), vek(b0), vek(c0), vek(e0)
    V = np.zeros((P, 3, 3))
    V[:, 0, 0] = aa - E[0][:, 0]
    V[:, 0, 1] = bb
    V[:, 0, 2] = cc
    V[:, 1, 0] = bb
    V[:, 1, 1] = aa - E[1][:, 0]
    V[:, 1, 2] = cc
    V[:, 2, 0] = cc
    V[:, 2, 1] = cc
    V[:, 2, 2] = ee - E[2][:, 0]
    fak = 1.0 / (2.0 * (2 * ell + 3))
    I = np.eye(3)[None, :, :]
    Y[:, 0:3, :] = r0 ** (ell + 1) * (I + fak * r0 ** 2 * V)
    Y[:, 3:6, :] = (ell + 1) * r0 ** ell * I + (ell + 3) * fak * r0 ** (ell + 2) * V
    return Y, n0


def integriere_l(pot, qidx, Ea, Eb, Ec, Y, n0, n1, ordnung, ell, zaehle=False):
    """Wie Code 1 / HUELLEN-LEITER (RK4, Gram-Schmidt alle GS_LEN), dazu l(l+1)/r^2 in allen Kanaelen."""
    hp = pot.hp
    d = 2 if n1 > n0 else -2
    h = d * hp
    gsn = int(round(S3.GS_LEN / hp))
    L2 = float(ell * (ell + 1))

    def acc(u, k):
        a, b, c, e = pot.an(qidx, k)
        out = np.empty_like(u)
        u0, u1, u2 = u[:, 0], u[:, 1], u[:, 2]
        out[:, 0] = (a - Ea) * u0 + b * u1 + c * u2
        out[:, 1] = b * u0 + (a - Eb) * u1 + c * u2
        out[:, 2] = c * (u0 + u1) + (e - Ec) * u2
        if L2 != 0.0:
            out += (L2 / (k * hp) ** 2) * u
        return out

    assert (n1 - n0) % 2 == 0, 'ungerade Knotenzahl'
    n = n0
    Y = Y.copy()
    kn = np.zeros(Y.shape[0], int)
    sv = np.zeros(Y.shape[0])
    while n != n1:
        u = Y[:, 0:3]
        p = Y[:, 3:6]
        k1p = acc(u, n)
        k2u = p + (0.5 * h) * k1p
        k2p = acc(u + (0.5 * h) * p, n + d // 2)
        k3u = p + (0.5 * h) * k2p
        k3p = acc(u + (0.5 * h) * k2u, n + d // 2)
        k4u = p + h * k3p
        k4p = acc(u + h * k3u, n + d)
        Yn = np.empty_like(Y)
        Yn[:, 0:3] = u + (h / 6.0) * (p + 2 * k2u + 2 * k3u + k4u)
        Yn[:, 3:6] = p + (h / 6.0) * (k1p + 2 * k2p + 2 * k3p + k4p)
        Y = Yn
        n += d
        if zaehle:
            sg = np.sign(Y[:, 2, 2])
            kn += (sg * sv) < 0
            sv = np.where(sg != 0, sg, sv)
        if n % gsn == 0:
            Y = S3.gs(Y, ordnung)
    return S3.gs(Y, ordnung), kn


def abklingend_l(mod, pot, qidx, E, n_m, kanaele, ell, n_z):
    P = E[0].shape[0]
    kanaele = list(kanaele)
    Z = np.zeros((P, 6, len(kanaele)))
    mm = (mod.m2, mod.m2, mod.mc2)
    Rz = n_z * pot.hp
    for j, ch in enumerate(kanaele):
        kap = np.sqrt(np.maximum(mm[ch] - E[ch][:, 0], 0.0))
        Z[:, ch, j] = 1.0
        if ell == 0:
            Z[:, 3 + ch, j] = -kap
        elif ell == 1:
            kr = kap * Rz
            Z[:, 3 + ch, j] = -(1.0 + kr + kr * kr) / (Rz * (1.0 + kr))
        elif ell == 2:
            x = kap * Rz
            Z[:, 3 + ch, j] = -(x ** 3 + 3.0 * x * x + 6.0 * x + 6.0) / (Rz * (x * x + 3.0 * x + 3.0))
        else:
            raise ValueError('nur l = 0, 1 oder 2')
    return integriere_l(pot, qidx, E[0], E[1], E[2], Z, n_z, n_m, list(range(len(kanaele))), ell)[0]


def werte_k_l(mod, pot, qidx, w2, rho, n_m, n_z, ell=None):
    """Ersatz fuer HL.werte_k (Suche): m_ac, m_bc, m_ab, Knotenzahl c-Komponente von Y_c."""
    ell = ELL if ell is None else ell
    if NZ_RAND:
        n_z = pot.N
    w2 = np.atleast_1d(np.asarray(w2, float))
    rho = np.atleast_1d(np.asarray(rho, float))
    E = S3.energien(w2, rho)
    Y0, n0 = start_regulaer(pot, qidx, E, ell)
    Y, kn = integriere_l(pot, qidx, E[0], E[1], E[2], Y0, n0, n_m, [2, 1, 0], ell, zaehle=True)
    Z = abklingend_l(mod, pot, qidx, E, n_m, (1, 2), ell, n_z)
    G = S3.paar(Y, Z)
    m_ac = G[:, 0, 0] * G[:, 2, 1] - G[:, 0, 1] * G[:, 2, 0]
    m_bc = G[:, 1, 0] * G[:, 2, 1] - G[:, 1, 1] * G[:, 2, 0]
    m_ab = G[:, 0, 0] * G[:, 1, 1] - G[:, 0, 1] * G[:, 1, 0]
    return dict(m_ac=m_ac, m_bc=m_bc, m_ab=m_ab, kn=kn)


def regulaer_S3(pot, qidx, E, n_m, ordnung):
    """Ersatz fuer S3.regulaer (gleiche Signatur)."""
    Y0, n0 = start_regulaer(pot, qidx, E, ELL)
    return integriere_l(pot, qidx, E[0], E[1], E[2], Y0, n0, n_m, ordnung, ELL)[0]


def abklingend_S3(mod, pot, qidx, E, n_m, kanaele):
    """Ersatz fuer S3.abklingend (gleiche Signatur; Start bei R_bg wie Code 1)."""
    return abklingend_l(mod, pot, qidx, E, n_m, kanaele, ELL, pot.N)


HL_werte_k_orig = HL.werte_k
S3_regulaer_orig = S3.regulaer
S3_abklingend_orig = S3.abklingend
HL.werte_k = werte_k_l
S3.regulaer = regulaer_S3
S3.abklingend = abklingend_S3


# ------------------------------------------------------------------ Befehle
def cmd_pruef(dateien):
    import py_compile
    for f in dateien:
        py_compile.compile(f, doraise=True)
        log('py_compile ok', f)


def cmd_liste(aus):
    HL.W2_UNTEN = 0.80          # PLAN 5: Runde-18-Regel, Untergrenze 0,80 (wie HUELLEN-DIPOL)
    HL.cmd_liste(aus)


def cmd_k1(stufe, pdir, listejson, refjson, adir, aus):
    """K1 (PLAN 4): bekannte Stellen mit derselben Kette wiederfinden (Zeilen i, i+1, Paar i; dann Newton und
    Rechteck wie HL.cmd_umlauf). Nur Referenzen mit ell == ELL."""
    liste = json.load(open(listejson))['w2']
    refs = [r for r in json.load(open(refjson))['stellen'] if int(r['ell']) == ELL]
    erg = dict(stufe=stufe, ell=ELL, n_ref=len(refs), stellen=[])
    for r in refs:
        t1 = time.time()
        i = int(r['i'])
        HL.cmd_block('M2', stufe, pdir, adir, listejson, i, i + 1)
        pf = os.path.join(adir, 'paar-st%d-%04d.json' % (stufe, i))
        d = json.load(open(pf))
        kand = [q for q in d['punkte'] if q['k'] == int(r['k'])]
        e = dict(name=r['name'], ell=ELL, i=i, k=int(r['k']), ref=dict(w2=r['w2'], rho=r['rho'], umlauf=r['umlauf']),
                 n_punkte_paar=len(d['punkte']), n_kand_kurve=len(kand), gefunden=bool(kand))
        if kand:
            q = dict(min(kand, key=lambda q: abs(q['w2'] - r['w2'])))
            q['name'] = r['name']
            q['dw2_zeile'] = liste[i] - liste[i + 1]
            pj = os.path.join(adir, 'k1-punkt-%s-st%d.json' % (r['name'], stufe))
            uj = os.path.join(adir, 'k1-umlauf-%s-st%d.json' % (r['name'], stufe))
            schreibe(pj, dict(punkte=[q]))
            HL.cmd_umlauf('M2', stufe, pdir, listejson, pj, uj, 0, 1)
            u = json.load(open(uj))['punkte'][0]
            um = u.get('umlauf') or {}
            dw2, drho = u['w2'] - r['w2'], u['rho'] - r['rho']
            ok = bool(u['konvergiert'] and abs(dw2) <= 1e-6 and abs(drho) <= 1e-6 and um.get('aufgeloest')
                      and um.get('umlauf') == r['umlauf'] and q['umlauf_zelle'] == r['umlauf'] and not q['weg']
                      and q['steig'] != 0)
            e.update(zelle=dict(w2=q['w2'], rho=q['rho'], R=q['R'], umlauf_zelle=q['umlauf_zelle'], weg=q['weg'],
                                steig=q['steig'], gap=q['gap']),
                     newton=dict(w2=u['w2'], rho=u['rho'], konvergiert=u['konvergiert'], svr=u.get('svr'),
                                 schritte=len(u['newton']), bereich=u['bereich']),
                     d_ref=[dw2, drho], umlauf=dict(umlauf=um.get('umlauf'), aufgeloest=um.get('aufgeloest'),
                                                     sprung=um.get('groesster_sprung'), punkte=um.get('punkte'),
                                                     versuch=um.get('versuch'), hmax=u.get('hmax')),
                     ok=ok)
        else:
            e['ok'] = False
        e['sekunden'] = time.time() - t1
        erg['stellen'].append(e)
        log('K1', json.dumps({k: e[k] for k in e if k not in ('ref',)}))
        schreibe(aus, erg)
    erg['bestanden'] = bool(refs and all(e['ok'] for e in erg['stellen']))
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)
    log('K1 l=%d Stufe %d bestanden=%s' % (ELL, stufe, erg['bestanden']))


def cmd_probe(stufe, pdir, listejson, idxs, aus):
    """Diagnose l = 2 (PLAN 4, nur berichtet): Nullstellen von m_bc einer Zeile mit Standardstart (r0 = 2 hp,
    Abklingstart n_start) gegen r0 = 4 hp und gegen Abklingstart am Gebietsrand."""
    global N0_START, NZ_RAND
    mod = S3.modell_von('M2')
    liste = json.load(open(listejson))['w2']
    erg = dict(stufe=stufe, ell=ELL, zeilen=[])
    for i in idxs:
        p = S3.lade_profil(HL.ppfad(pdir, liste[i]))
        res = {}
        for name, n0, rand in (('standard', 2, False), ('r0_4hp', 4, False), ('nz_rand', 2, True)):
            N0_START, NZ_RAND = n0, rand
            d = HL.zeile_k(mod, p)
            res[name] = dict(rho=[z['rho'] for z in d['null']], s=[z['s'] for z in d['null']],
                             vz=d['vorzeichen'], n=len(d['null']), n_z=d['n_z'], N=p['N'])
        N0_START, NZ_RAND = 2, False
        a = res['standard']
        e = dict(i=i, w2=liste[i], R=p.get('Rchi'), varianten=res)
        for name in ('r0_4hp', 'nz_rand'):
            b = res[name]
            if b['n'] == a['n'] and a['n'] > 0:
                e['d_' + name] = dict(gleich_n=True, max_drho=float(np.max(np.abs(np.array(a['rho']) - np.array(b['rho'])))),
                                      max_ds_rel=float(np.max(np.abs(np.array(a['s']) - np.array(b['s'])) /
                                                              np.maximum(np.abs(np.array(a['s'])), 1e-300))),
                                      vz_gleich=bool(a['vz'] == b['vz']))
            else:
                e['d_' + name] = dict(gleich_n=bool(b['n'] == a['n']), n_a=a['n'], n_b=b['n'])
        erg['zeilen'].append(e)
        log('Probe', json.dumps({k: e[k] for k in e if k != 'varianten'}))
        schreibe(aus, erg)
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


def main():
    global ELL
    a = sys.argv[1:]
    if a and a[0].startswith('ell='):
        ELL = int(a[0][4:])
        a = a[1:]
    log('l =', ELL)
    c = a[0]
    a = a[1:]
    if c == 'pruef':
        cmd_pruef(a)
    elif c == 'liste':
        cmd_liste(a[0])
    elif c == 'profile':
        HL.cmd_profile('M2', int(a[0]), a[1], a[2], weiter=(len(a) > 3 and a[3] == 'weiter'))
    elif c == 'k1':
        cmd_k1(int(a[0]), a[1], a[2], a[3], a[4], a[5])
    elif c == 'probe':
        cmd_probe(int(a[0]), a[1], a[2], [int(x) for x in a[3].split(',')], a[4])
    elif c == 'block':
        HL.cmd_block('M2', int(a[0]), a[1], a[2], a[3], int(a[4]), int(a[5]))
    elif c == 'umlauf':
        HL.cmd_umlauf('M2', int(a[0]), a[1], a[2], a[3], a[4], int(a[5]), int(a[6]))
    else:
        raise SystemExit('unbekannt: ' + c)
    log('fertig')


if __name__ == '__main__':
    main()
