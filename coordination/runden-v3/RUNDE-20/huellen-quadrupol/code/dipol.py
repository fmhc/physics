#!/usr/bin/env python3
"""dipol.py - Runde 19 HUELLEN-DIPOL, Code-Agent (2026-10-02).

Stille Dipol-Stellen (l = 1) in E1 des Zweifeldmodells M2. Methode und Wertung: PLAN.md (eingefroren).
Code 1 (stille3.py, STILLE-ZWEIFELD) und HUELLEN-LEITER (huellen_leiter.py) werden unveraendert importiert; zur Laufzeit
werden genau drei Kanalfunktionen durch l-Fassungen ersetzt: HL.werte_k, S3.regulaer, S3.abklingend.
l(l+1)/r^2 in allen drei Kanaelen; regulaerer Start u = r^(l+1) [v + r^2 V0 v / (2(2l+3))] bei r0 = 2 hp;
abklingender Start fuer l = 1: u = e^{-k r}(1 + 1/(k r)), u'/u = -(1 + kR + k^2 R^2) / (R (1 + kR)).
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

ELL = 1
T0 = time.time()
schreibe = S3.schreibe
K1_ZEILEN = [0.77, 0.76, 0.75, 0.74, 0.73]
K1_REF = (0.75449601378264, 1.82634203018107)     # BEWEIS-2, Satz T2
K1_KARTE = (0.7544960184, 1.8263420673)           # Karte
SCHNITT = 1e-12                                   # D4: Rundungsschutz (PLAN 9)


def log(*a):
    print('[%7.1fs]' % (time.time() - T0), *a, flush=True)


# ------------------------------------------------------------------ Kanaele mit l
def start_regulaer(pot, qidx, E, ell):
    P = E[0].shape[0]
    Y = np.zeros((P, 6, 3))
    if ell == 0:
        for j in range(3):
            Y[:, 3 + j, j] = 1.0
        return Y, 0
    n0 = 2
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
        else:
            raise ValueError('nur l = 0 oder 1')
    return integriere_l(pot, qidx, E[0], E[1], E[2], Z, n_z, n_m, list(range(len(kanaele))), ell)[0]


def werte_k_l(mod, pot, qidx, w2, rho, n_m, n_z, ell=None):
    """Ersatz fuer HL.werte_k (Suche): m_ac, m_bc, m_ab, Knotenzahl c-Komponente von Y_c."""
    ell = ELL if ell is None else ell
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


def selbsttest(mod, p):
    """l = 0: Ersatzfunktionen gegen die Originale (PLAN 1)."""
    pot = S3.Pot(mod, [p])
    n_m = S3.n_mitte(p)
    n_z = HL.n_start(mod, pot, n_m, p['w2'])
    w = math.sqrt(p['w2'])
    lo = math.sqrt(mod.m2) - w + 0.01
    hi = min(math.sqrt(mod.mc2), w + math.sqrt(mod.m2)) - 0.01
    rho = np.linspace(lo, hi, 5)
    q = np.zeros(5, int)
    w2s = np.full(5, p['w2'])
    a = HL_werte_k_orig(mod, pot, q, w2s, rho, n_m, n_z)
    b = werte_k_l(mod, pot, q, w2s, rho, n_m, n_z, ell=0)
    E = S3.energien(w2s, rho)
    Ya = S3_regulaer_orig(pot, q, E, n_m, [2, 1, 0])
    Y0, n0 = start_regulaer(pot, q, E, 0)
    Yb = integriere_l(pot, q, E[0], E[1], E[2], Y0, n0, n_m, [2, 1, 0], 0)[0]
    Za = S3_abklingend_orig(mod, pot, q, E, n_m, [1, 2])
    Zb = abklingend_l(mod, pot, q, E, n_m, [1, 2], 0, pot.N)
    c = werte_k_l(mod, pot, q, w2s, rho, n_m, n_z, ell=1)
    return dict(w2=p['w2'], rho=rho.tolist(),
                d_mac=float(np.max(np.abs(a['m_ac'] - b['m_ac']))), d_mbc=float(np.max(np.abs(a['m_bc'] - b['m_bc']))),
                d_mab=float(np.max(np.abs(a['m_ab'] - b['m_ab']))), kn_gleich=bool(np.all(a['kn'] == b['kn'])),
                d_Y=float(np.max(np.abs(Ya - Yb))), d_Z=float(np.max(np.abs(Za - Zb))),
                l1_mbc=c['m_bc'].tolist(), l1_mac=c['m_ac'].tolist(), l0_mbc=a['m_bc'].tolist())


# ------------------------------------------------------------------ Befehle
def cmd_pruef(dateien):
    import py_compile
    for f in dateien:
        py_compile.compile(f, doraise=True)
        log('py_compile ok', f)


def cmd_liste(aus):
    HL.W2_UNTEN = 0.80          # PLAN 5: Runde-18-Regel, Untergrenze 0,80
    HL.cmd_liste(aus)


def cmd_k1(stufe, aus):
    """K1 (PLAN 4): bewiesene M1-Dipolstelle, Modell K1E1, l = 1, Kette wie HUELLEN-LEITER cmd_k1."""
    mod = S3.modell_von('K1E1')
    hp = S3.STUFEN[stufe]
    p0 = S3.saat(mod, 'M1', 200.0, hp)
    profs = {}
    p = p0
    for x in sorted([w for w in K1_ZEILEN if w <= p0['w2']], reverse=True):
        p = S3.fortsetzung(mod, p, x, hp)
        profs[x] = p
    p = p0
    for x in sorted([w for w in K1_ZEILEN if w > p0['w2']]):
        p = S3.fortsetzung(mod, p, x, hp)
        profs[x] = p
    ws = sorted(profs, reverse=True)
    erg = dict(stufe=stufe, ell=ELL, referenz=K1_REF, karte=K1_KARTE, saat_w2=p0['w2'])
    erg['selbsttest_l0'] = selbsttest(mod, profs[0.75])
    log('Selbsttest l=0:', json.dumps({k: v for k, v in erg['selbsttest_l0'].items() if not k.startswith('l')}))
    schreibe(aus, erg)
    zeilen = []
    for x in ws:
        pr = profs[x]
        pr['Rchi'] = float('nan')
        pr['m0sq'] = HL.m0sq(mod, pr)
        d = HL.zeile_k(mod, pr)
        zeilen.append(d)
        log('K1 zeile %.2f: n=%d %s rho=%s kn=%s' % (x, len(d['null']), d['vorzeichen'],
                                                    [round(z['rho'], 5) for z in d['null']],
                                                    [z['knoten'] for z in d['null']]))
    punkte = []
    kurven = []
    for i in range(len(ws) - 1):
        pp, kk = HL.lokal_paar(mod, zeilen[i], zeilen[i + 1], profs[ws[i + 1]])
        punkte += pp
        kurven.append(kk)
    erg.update(zeilen=[{k: z[k] for k in ('w2', 'null', 'vorzeichen')} for z in zeilen], punkte=punkte, kurven=kurven)
    schreibe(aus, erg)
    res = []
    for q in punkte:
        anker = profs[max(x for x in ws if x <= q['w2'])]
        e = S3.e1_kandidat(mod, anker, dict(w2=q['w2'], rho=q['rho']), 0.72, 0.78)
        e['zelle'] = dict(k=q['k'], umlauf_zelle=q['umlauf_zelle'], w2=q['w2'], rho=q['rho'])
        e['abstand_referenz'] = [e['w2'] - K1_REF[0], e['rho'] - K1_REF[1]]
        e['abstand_karte'] = [e['w2'] - K1_KARTE[0], e['rho'] - K1_KARTE[1]]
        res.append(e)
        log('K1 kand', json.dumps({k: e[k] for k in e if k not in ('newton',)}))
        erg['kandidaten'] = res
        schreibe(aus, erg)
    erg['kandidaten'] = res
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


class PotSchnitt(S3.Pot):
    """D4: Kopplung Mac = 0, wo |chi| < SCHNITT (Rundungsschutz, PLAN 9)."""

    def __init__(self, mod, profs):
        super().__init__(mod, profs)
        self.n_schnitt = 0
        for q, p in enumerate(profs):
            r, f, g = S3.fg_aus(p['F'], p['H'], self.hp, self.N)
            m = np.abs(g) < SCHNITT
            self.Mac[q, m] = 0.0
            self.n_schnitt = max(self.n_schnitt, int(m.sum()))


def cmd_d4(stufe, k1json, aus):
    """D4 (PLAN 9): Homotopie lam 0 -> 1 bei cpot = 0,25 wie Code 1 cmd_homotopie, l = 1."""
    S3.Pot = PotSchnitt
    hp = S3.STUFEN[stufe]
    pdir = os.path.join(os.path.dirname(aus), 'd4-prof')
    os.makedirs(pdir, exist_ok=True)
    if os.path.exists(aus):
        erg = json.load(open(aus))
    else:
        erg = None
    if erg and erg.get('schritte'):
        last = erg['schritte'][-1]
        w2, rho, N, n_m = last['w2'], last['rho'], erg['N'], int(round(erg['r_m'] / hp))
        p = S3.lade_profil(os.path.join(pdir, 'p-lam%.2f.npz' % last['lam']))
        lam_done = last['lam']
        log('weiter ab lam=%.2f' % lam_done)
    else:
        k1 = json.load(open(k1json))
        kk = [e for e in k1['kandidaten'] if e.get('konvergiert')]
        best = min(kk, key=lambda e: abs(e['w2'] - K1_REF[0]) + abs(e['rho'] - K1_REF[1]))
        w2, rho = best['w2'], best['rho']
        mod0 = S3.Modell(0.0, 0.25)
        p = S3.saat(mod0, 'M1', 200.0, hp)
        p = S3.fortsetzung(mod0, p, w2, hp)
        n_m = S3.n_mitte(p)
        Rest = 1.3736 / (w2 - 0.7281) + 0.55
        Rbg = 1.5 * Rest + 25.0 / math.sqrt(2.0 - w2) + 5.0
        N = int(round(0.02 * math.ceil(Rbg / 0.02 - 1e-9) / hp))
        N += N % 2
        F, H = S3.uebertrage(p, hp, N)
        p = S3.loese(mod0, w2, hp, N, F, H)
        if p is None:
            raise RuntimeError('Startprofil auf grossem Gebiet gescheitert')
        erg = dict(stufe=stufe, start=dict(w2=w2, rho=rho), N=N, Rbg=N * hp, r_m=n_m * hp, schritte=[],
                   schnitt=SCHNITT)
        lam_done = -1.0
    lams = [round(0.05 * k, 10) for k in range(21)]
    for lam in lams:
        if lam <= lam_done + 1e-9:
            continue
        mod = S3.Modell(lam, 0.25)
        q = S3.loese(mod, w2, hp, N, p['F'], p['H'])
        if q is None:
            lam0 = erg['schritte'][-1]['lam'] if erg['schritte'] else 0.0
            q = p
            for t in np.linspace(lam0, lam, 9)[1:]:
                q2 = S3.loese(S3.Modell(t, 0.25), w2, hp, N, q['F'], q['H'])
                if q2 is None:
                    q = None
                    break
                q = q2
        if q is None:
            erg['abbruch'] = 'Profil bei lam=%.2f gescheitert' % lam
            schreibe(aus, erg)
            log(erg['abbruch'])
            break
        try:
            s, w2n, rhon, pq = d4_schritt(mod, q, n_m, lam, w2, rho)
        except Exception as ex:
            erg['abbruch'] = 'Schritt lam=%.2f: %r' % (lam, ex)
            schreibe(aus, erg)
            log(erg['abbruch'])
            break
        S3.speichere_profil(os.path.join(pdir, 'p-lam%.2f.npz' % lam), pq)
        erg['schritte'].append(s)
        log('D4', json.dumps({k: s[k] for k in s if k not in ('gn', 'newton', 'G')}))
        schreibe(aus, erg)
        w2, rho, p = w2n, rhon, pq
    erg['sekunden_letzter_lauf'] = time.time() - T0
    schreibe(aus, erg)


def d4_schritt(mod, q, n_m, lam, w2, rho):
    if True:
        U = S3.Umgebung(mod, q, n_m=n_m)
        ber = S3.bereich(mod, w2, rho)
        s = dict(lam=lam, bereich_start=ber)
        t1 = time.time()
        if ber == 'E1':
            w2n, rhon, ok, verl = S3.newton_E1(U, w2, rho)
            v = U.werte(S3.werte_E1, [w2n], [rhon])
            s.update(art='E1', w2=w2n, rho=rhon, ok=ok, svr=float(v['svr'][0]),
                     lebt=bool(ok and v['svr'][0] < 1e-6), newton=verl)
        else:
            def grenze(a, b, mod=mod):
                a = min(max(a, 0.70), mod.m2 - 0.02)
                w = math.sqrt(a)
                b = min(max(b, math.sqrt(mod.mc2) + S3.RAND), w + math.sqrt(mod.m2) - S3.RAND)
                return a, b
            w2n, rhon, v, verl = S3.gn_E2(U, w2, rho, grenze)
            s.update(art='E2', w2=w2n, rho=rhon, T=float(v['T'][0]), G=v['G'][0].tolist(), gn=verl)
            if abs(rhon - (math.sqrt(mod.mc2) + S3.RAND)) < 1e-6:
                # PLAN 9: an der Klemme -> Newton auf W in E1 ab (w2, sqrt2 - 1e-3)
                try:
                    w2e, rhoe, oke, verle = S3.newton_E1(U, w2n, math.sqrt(mod.mc2) - S3.RAND)
                    be = S3.bereich(mod, w2e, rhoe)
                    ve = U.werte(S3.werte_E1, [w2e], [rhoe]) if be == 'E1' else None
                    s['e1_versuch'] = dict(w2=w2e, rho=rhoe, ok=oke, bereich=be,
                                           svr=(float(ve['svr'][0]) if ve is not None else None))
                    if oke and be == 'E1' and ve['svr'][0] < 1e-6:
                        w2n, rhon = w2e, rhoe
                        s.update(art='E1', w2=w2n, rho=rhon, ok=True, svr=float(ve['svr'][0]), lebt=True)
                except Exception as ex:
                    s['e1_versuch'] = dict(fehler=repr(ex))
        pq = U.profil(w2n)
        s['chi0'] = pq['chi0']
        s['Rchi'] = HL.r_chi(pq)
        s['rhalf'] = pq['rhalf']
        s['Q'] = pq['Q']
        s['bereich_ende'] = S3.bereich(mod, w2n, rhon)
        s['sekunden'] = time.time() - t1
        s['n_schnitt'] = int(getattr(S3.Pot(mod, [pq]), 'n_schnitt', -1))
        return s, w2n, rhon, pq


def main():
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == 'pruef':
        cmd_pruef(a)
    elif c == 'liste':
        cmd_liste(a[0])
    elif c == 'k1':
        cmd_k1(int(a[0]), a[1])
    elif c == 'profile':
        HL.cmd_profile('M2', int(a[0]), a[1], a[2], weiter=(len(a) > 3 and a[3] == 'weiter'))
    elif c == 'block':
        HL.cmd_block('M2', int(a[0]), a[1], a[2], a[3], int(a[4]), int(a[5]))
    elif c == 'umlauf':
        HL.cmd_umlauf('M2', int(a[0]), a[1], a[2], a[3], a[4], int(a[5]), int(a[6]))
    elif c == 'd4':
        cmd_d4(int(a[0]), a[1], a[2])
    else:
        raise SystemExit('unbekannt: ' + c)
    log('fertig')


if __name__ == '__main__':
    main()
