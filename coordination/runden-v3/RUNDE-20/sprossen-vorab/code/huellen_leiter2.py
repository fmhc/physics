#!/usr/bin/env python3
"""huellen_leiter2.py - Runde 19 HUELLEN-LEITER-2, Code-Agent (2026-10-02).

Grundlage: huellen_leiter.py der Runde 18 (Endfassung 68c0a1fb...), Suche und Messgroesse unveraendert:
W = m_ac + i m_bc (2x2-Minoren der Wronski-Matrix G mit Zeile c), geschlossene Bedingung m_bc = 0, s = m_ac darauf.
Neu (Runde 19, PLAN.md eingefroren): stabilisierte Kopplung. In der Linearisierung (Klasse Pot von Code 1) wird der
Hintergrund chi = g dort exakt auf 0 gesetzt, wo g < 1e-12 ist (alle vier Matrixelemente; bitweise wirkt das nur auf
die Kopplung M_ac = 2 f g, siehe PLAN). Code 1 (stille3.py) bleibt unveraendert; die Klasse wird hier ersetzt.
Neu ausserdem: Befehl k0newton (K0: Newton-Lage alt gegen neu).
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
import stille3 as S3   # Code 1, unveraendert

# ------------------------------------------------------------------ Stabilisierte Kopplung (Runde 19)
CHI_SCHWELLE = 1e-12
OrigPot = S3.Pot
STAT = dict(n_pot=0, n_punkte=0, n_maske=0, r_maske_max=0.0, n_neg=0,
            n_aenderung_aa=0, n_aenderung_ab=0, n_aenderung_ac=0, n_aenderung_cc=0)


class PotStab(OrigPot):
    """Wie Code-1-Pot, aber g -> 0 wo g < CHI_SCHWELLE (auch negative Rundungswerte). Zaehlt die bitweisen
    Aenderungen je Matrixelement gegen die unstabilisierte Fassung (Pruefung PLAN 1)."""

    def __init__(self, mod, profs):
        self.hp = profs[0]['hp']
        self.N = profs[0]['N']
        K = len(profs)
        self.K = K
        self.Maa = np.empty((K, self.N + 1))
        self.Mab = np.empty((K, self.N + 1))
        self.Mac = np.empty((K, self.N + 1))
        self.Mcc = np.empty((K, self.N + 1))
        self.n_maske = []
        for q, p in enumerate(profs):
            assert p['N'] == self.N and abs(p['hp'] - self.hp) < 1e-15
            r, f, g = S3.fg_aus(p['F'], p['H'], self.hp, self.N)
            S = f * f
            maske = g < CHI_SCHWELLE
            gs = np.where(maske, 0.0, g)
            US, USS, Ug, Ugg, USg = mod.d(S, gs)
            self.Maa[q] = US + S * USS
            self.Mab[q] = S * USS
            self.Mac[q] = f * USg
            self.Mcc[q] = Ugg
            US0, USS0, Ug0, Ugg0, USg0 = mod.d(S, g)
            STAT['n_pot'] += 1
            STAT['n_punkte'] += int(len(g))
            nm = int(maske.sum())
            STAT['n_maske'] += nm
            STAT['n_neg'] += int(np.sum(g < 0))
            if nm:
                STAT['r_maske_max'] = max(STAT['r_maske_max'], float(r[np.nonzero(maske)[0].max()]))
            STAT['n_aenderung_aa'] += int(np.sum((US0 + S * USS0) != self.Maa[q]))
            STAT['n_aenderung_ab'] += int(np.sum((S * USS0) != self.Mab[q]))
            STAT['n_aenderung_ac'] += int(np.sum((f * USg0) != self.Mac[q]))
            STAT['n_aenderung_cc'] += int(np.sum(Ugg0 != self.Mcc[q]))
            self.n_maske.append(nm)


def setze_kopplung(stab):
    S3.Pot = PotStab if stab else OrigPot


def maske_info(p):
    r, f, g = S3.fg_aus(p['F'], p['H'], p['hp'], p['N'])
    m = g < CHI_SCHWELLE
    return dict(n_maske=int(m.sum()), r_maske=(float(r[np.nonzero(m)[0].max()]) if m.any() else None),
                n_neg=int(np.sum(g < 0)), chi0_roh=float(g[0]))


setze_kopplung(os.environ.get('KOPPLUNG', 'stab') != 'alt')

W2C, RA, RB = 0.7281, 1.3736, 0.55      # R(w2) ~ RA/(w2 - W2C) + RB (nur fuer die Zeilenwahl)
DR_ZEILE, DW2_MAX = 0.5, 0.01
W2_OBEN, W2_UNTEN = 1.40, 0.74
RANDM = 1e-4
N_UNI = 201
DQ = 0.2
NSUB = 8
NBIS = 2
T0 = time.time()
def schreibe(pfad, obj):
    """Wie Code 1, aber Zwischendatei je Prozess (zwei Bloecke koennen dieselbe Randzeile schreiben; Inhalt gleich)."""
    d = os.path.dirname(pfad)
    if d:
        os.makedirs(d, exist_ok=True)
    tmp = pfad + '.tmp%d' % os.getpid()
    with open(tmp, 'w') as fh:
        json.dump(obj, fh, indent=1)
    os.replace(tmp, pfad)


S3.schreibe = schreibe


def log(*a):
    print('[%7.1fs]' % (time.time() - T0), *a, flush=True)


# ------------------------------------------------------------------ Zeilen und Profile
def zeilenliste():
    out = [W2_OBEN]
    w2 = W2_OBEN
    while True:
        d = min(DW2_MAX, DR_ZEILE * (w2 - W2C) ** 2 / RA)
        w2n = w2 - d
        if w2n < W2_UNTEN + 0.5 * d:
            out.append(W2_UNTEN)
            break
        out.append(round(w2n, 12))
        w2 = w2n
    return out


def ppfad(pdir, w2):
    return os.path.join(pdir, 'p-%.10f.npz' % w2)


def r_chi(p):
    r, f, g = S3.fg_aus(p['F'], p['H'], p['hp'], p['N'])
    if not (g[0] < 0.5):
        return float('nan')
    k = int(np.argmax(g >= 0.5))
    if k == 0:
        return float('nan')
    return float(r[k - 1] + (0.5 - g[k - 1]) * (r[k] - r[k - 1]) / (g[k] - g[k - 1]))


def m0sq(mod, p):
    return float(mod.d(p['f0'] ** 2, p['chi0'])[3])


def cmd_liste(aus):
    l = zeilenliste()
    R = [RA / (x - W2C) + RB for x in l]
    schreibe(aus, dict(w2=l, R_formel=R, n=len(l), regel='w2_{j+1} = w2_j - min(%g, %g (w2_j - %g)^2 / %g)' % (
        DW2_MAX, DR_ZEILE, W2C, RA)))
    log('Zeilen', len(l), l[:3], l[-3:])


def cmd_profile(tag, stufe, pdir, listejson, weiter=False):
    mod = S3.modell_von(tag)
    hp = S3.STUFEN[stufe]
    liste = json.load(open(listejson))['w2']
    info = []
    if weiter:
        # Fortsetzung eines abgebrochenen Laufs: ab dem kleinsten gespeicherten omega^2 abwaerts (gleiches Verfahren)
        da = sorted(x for x in liste if os.path.exists(ppfad(pdir, x)))
        p0 = S3.lade_profil(ppfad(pdir, da[0]))
        if os.path.exists(os.path.join(pdir, 'profile-info.json')):
            info = json.load(open(os.path.join(pdir, 'profile-info.json')))
        bek = set(round(d['w2'], 10) for d in info)
        for x in da:
            if round(x, 10) not in bek:
                q = S3.lade_profil(ppfad(pdir, x))
                d = {k: v for k, v in q.items() if k not in ('F', 'H', 'newton')}
                d['newton_it'] = len(q['newton'])
                d['nachgetragen'] = True
                info.append(d)
        log('weiter ab w2=%.10f (%d vorhanden, %d in Info)' % (p0['w2'], len(da), len(info)))
        ziele = sorted(set(float(x) for x in liste if x < p0['w2']))
        oben, unten = [], ziele[::-1]
    else:
        p0 = S3.saat(mod, 'M2' if tag == 'M2' else 'M1', 200.0, hp)
        log('Saat w2=%.8f Q=%.4f N=%d' % (p0['w2'], p0['Q'], p0['N']))
        ziele = sorted(set(float(x) for x in liste))
        oben = [x for x in ziele if x >= p0['w2']]
        unten = [x for x in ziele if x < p0['w2']][::-1]
    for folge in (oben, unten):
        p = p0
        for x in folge:
            t1 = time.time()
            q = S3.fortsetzung(mod, p, x, hp)
            if q is None:
                log('FEHLER Profil w2=%.10f' % x)
                break
            q['Rchi'] = r_chi(q)
            q['m0sq'] = m0sq(mod, q)
            S3.speichere_profil(ppfad(pdir, x), q)
            d = {k: v for k, v in q.items() if k not in ('F', 'H', 'newton')}
            d['newton_it'] = len(q['newton'])
            d['sekunden'] = time.time() - t1
            info.append(d)
            log('w2=%.8f Q=%.6f E=%.6f chi0=%.3e rhalf=%.3f Rchi=%.3f m0sq=%.4f N=%d it=%d %.2fs' % (
                x, q['Q'], q['E'], q['chi0'], q['rhalf'], q['Rchi'], q['m0sq'], q['N'], len(q['newton']),
                d['sekunden']))
            p = q
            if len(info) % 10 == 0:
                schreibe(os.path.join(pdir, 'profile-info.json'), sorted(info, key=lambda d: d['w2']))
    schreibe(os.path.join(pdir, 'profile-info.json'), sorted(info, key=lambda d: d['w2']))


# ------------------------------------------------------------------ Kanaele (wie Code 1, plus Knotenzaehlung)
def integriere_k(pot, qidx, Ea, Eb, Ec, Y, n0, n1, ordnung, zaehle=False):
    hp = pot.hp
    d = 2 if n1 > n0 else -2
    h = d * hp
    gsn = int(round(S3.GS_LEN / hp))

    def acc(u, k):
        a, b, c, e = pot.an(qidx, k)
        out = np.empty_like(u)
        u0, u1, u2 = u[:, 0], u[:, 1], u[:, 2]
        out[:, 0] = (a - Ea) * u0 + b * u1 + c * u2
        out[:, 1] = b * u0 + (a - Eb) * u1 + c * u2
        out[:, 2] = c * (u0 + u1) + (e - Ec) * u2
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


def n_start(mod, pot, n_m, w2max):
    mu = math.sqrt(max(mod.m2 - w2max, 1e-6))
    nz = n_m + 2 * int(math.ceil((25.0 / mu + 5.0) / (2 * pot.hp)))
    return min(pot.N, nz)


def werte_k(mod, pot, qidx, w2, rho, n_m, n_z):
    w2 = np.atleast_1d(np.asarray(w2, float))
    rho = np.atleast_1d(np.asarray(rho, float))
    E = S3.energien(w2, rho)
    P = len(rho)
    Y0 = np.zeros((P, 6, 3))
    for j in range(3):
        Y0[:, 3 + j, j] = 1.0
    Y, kn = integriere_k(pot, qidx, E[0], E[1], E[2], Y0, 0, n_m, [2, 1, 0], zaehle=True)
    Z0 = np.zeros((P, 6, 2))
    mm = (mod.m2, mod.m2, mod.mc2)
    for j, ch in enumerate((1, 2)):
        kap = np.sqrt(np.maximum(mm[ch] - E[ch][:, 0], 0.0))
        Z0[:, ch, j] = 1.0
        Z0[:, 3 + ch, j] = -kap
    Z, _ = integriere_k(pot, qidx, E[0], E[1], E[2], Z0, n_z, n_m, [0, 1])
    G = S3.paar(Y, Z)
    m_ac = G[:, 0, 0] * G[:, 2, 1] - G[:, 0, 1] * G[:, 2, 0]
    m_bc = G[:, 1, 0] * G[:, 2, 1] - G[:, 1, 1] * G[:, 2, 0]
    m_ab = G[:, 0, 0] * G[:, 1, 1] - G[:, 0, 1] * G[:, 1, 0]
    return dict(m_ac=m_ac, m_bc=m_bc, m_ab=m_ab, kn=kn)


# ------------------------------------------------------------------ Zeile
def rho_gitter(mod, p):
    w = math.sqrt(p['w2'])
    m, mc = math.sqrt(mod.m2), math.sqrt(mod.mc2)
    lo, hi = m - w + RANDM, min(mc, w + m) - RANDM
    rho = list(np.linspace(lo, hi, N_UNI))
    Rc, m0 = p.get('Rchi', float('nan')), p.get('m0sq', float('nan'))
    nq = 0
    if np.isfinite(Rc) and np.isfinite(m0) and m0 < hi * hi:
        q = DQ
        while True:
            rq = math.sqrt(max(m0, 0.0) + (math.pi * q / Rc) ** 2)
            if rq >= hi:
                break
            if rq > lo:
                rho.append(rq)
                nq += 1
            q += DQ
    return np.unique(np.array(rho)), lo, hi, nq


def illinois(ev, a, b, fa, fb, nmax=30, tol=1e-11):
    """Illinois-Regula-falsi, vektorisiert ueber Klammern [a, b] mit fa fb < 0 (PLAN-NACHTRAG-1)."""
    n = len(a)
    c = 0.5 * (a + b)
    fc = np.zeros(n)
    sc = np.zeros(n)
    kc = np.zeros(n, int)
    aktiv = np.ones(n, bool)
    nit = np.zeros(n, int)
    for it in range(nmax):
        if not aktiv.any():
            break
        j = np.nonzero(aktiv)[0]
        den = fb[j] - fa[j]
        cj = b[j] - fb[j] * (b[j] - a[j]) / np.where(den != 0, den, 1.0)
        lo_, hi_ = np.minimum(a[j], b[j]), np.maximum(a[j], b[j])
        cj = np.where((den != 0) & (cj > lo_) & (cj < hi_), cj, 0.5 * (a[j] + b[j]))
        v = ev(cj)
        fcj = v['m_bc']
        c[j], fc[j], sc[j], kc[j] = cj, fcj, v['m_ac'], v['kn']
        nit[j] += 1
        wech = fcj * fb[j] < 0
        a[j] = np.where(wech, b[j], a[j])
        fa[j] = np.where(wech, fb[j], 0.5 * fa[j])
        b[j] = cj
        fb[j] = fcj
        fertig = (np.abs(b[j] - a[j]) < tol) | (np.abs(fcj) < 1e-12)
        aktiv[j[fertig]] = False
    konv = ~aktiv
    return c, fc, sc, kc, nit, konv


def zeile_k(mod, p):
    pot = S3.Pot(mod, [p])
    n_m = S3.n_mitte(p)
    n_z = n_start(mod, pot, n_m, p['w2'])
    rho, lo, hi, nq = rho_gitter(mod, p)
    P = len(rho)
    v = werte_k(mod, pot, np.zeros(P, int), np.full(P, p['w2']), rho, n_m, n_z)
    nz = S3.nullstellen(rho, v['m_bc'], [v['m_ac']])
    null = []
    if nz:
        c0 = np.array([z['rho'] for z in nz])
        ii = np.array([z['i'] for z in nz])
        breite = rho[ii + 1] - rho[ii]
        dl = np.maximum(1e-4 * breite, 1e-9)
        n = len(c0)
        x = np.concatenate([c0 - dl, c0 + dl])
        vA = werte_k(mod, pot, np.zeros(2 * n, int), np.full(2 * n, p['w2']), x, n_m, n_z)
        fm, fp = vA['m_bc'][:n], vA['m_bc'][n:]
        f1 = (fp - fm) / (2 * dl)
        c1 = c0 - 0.5 * (fm + fp) / f1
        sa1 = (vA['m_ac'][n:] - vA['m_ac'][:n]) / (2 * dl)
        vB = werte_k(mod, pot, np.zeros(n, int), np.full(n, p['w2']), c1, n_m, n_z)
        c2 = c1 - vB['m_bc'] / f1
        s2 = vB['m_ac'] + sa1 * (c2 - c1)
        rest = vB['m_bc'].copy()
        kn = vB['kn'].copy()
        sicher = ((np.abs(c1 - c0) < 0.5 * breite) & (np.abs(c2 - c1) < 0.5 * breite) & (c2 > lo) & (c2 < hi))
        # PLAN-NACHTRAG-1: Illinois in der Gitterklammer, wenn Newton unsicher oder Rest |m_bc| > 1e-3
        ill = np.zeros(n, int)
        idx = np.nonzero((~sicher) | (np.abs(rest) > 1e-3))[0]
        if len(idx):
            a = rho[ii[idx]].copy()
            b = rho[ii[idx] + 1].copy()
            fa = v['m_bc'][ii[idx]].copy()
            fb = v['m_bc'][ii[idx] + 1].copy()

            def ev(x):
                return werte_k(mod, pot, np.zeros(len(x), int), np.full(len(x), p['w2']), x, n_m, n_z)
            c, fc, sc, kc, nit, konv = illinois(ev, a, b, fa, fb)
            c2[idx] = c
            s2[idx] = sc
            rest[idx] = fc
            kn[idx] = kc
            ill[idx] = nit
            sicher[idx] = konv
        for j in range(n):
            null.append(dict(rho=float(c2[j]), s=float(s2[j]), s_roh=float(vB['m_ac'][j]), steig=float(np.sign(f1[j])),
                             dmbc=float(f1[j]), dmac=float(sa1[j]), rest=float(rest[j]), knoten=int(kn[j]),
                             m_ab=float(vB['m_ab'][j]), schritt=float(c1[j] - c0[j]), zelle=float(breite[j]),
                             sicher=bool(sicher[j]), illinois=int(ill[j])))
    d = {k: v for k, v in p.items() if k not in ('F', 'H', 'newton')}
    d.update(n_m=int(n_m), r_m=float(n_m * p['hp']), n_z=int(n_z), lo=lo, hi=hi, n_rho=int(P), n_q=int(nq), null=null,
             n_vw_gitter=int(np.sum(np.sign(v['m_bc'][:-1]) * np.sign(v['m_bc'][1:]) < 0)),
             vorzeichen=''.join('+' if z['s'] > 0 else '-' for z in null), version=2,
             kopplung=('stab' if S3.Pot is PotStab else 'alt'), maske=maske_info(p), stat=dict(STAT))
    return d


def luecke(z, k):
    r = [q['rho'] for q in z['null']]
    c = []
    if k > 0:
        c.append(r[k] - r[k - 1])
    else:
        c.append(r[k] - z['lo'])
    if k + 1 < len(r):
        c.append(r[k + 1] - r[k])
    else:
        c.append(z['hi'] - r[k])
    return float(max(min(c), 1e-7))


# ------------------------------------------------------------------ Unterzeilen und Halbierung je Zeilenpaar
def newton_rho(v, idx_m, idx_p, g, dl):
    fm, fp = v['m_bc'][idx_m], v['m_bc'][idx_p]
    f1 = (fp - fm) / (2 * dl)
    c1 = g - 0.5 * (fm + fp) / f1
    sa = 0.5 * (v['m_ac'][idx_m] + v['m_ac'][idx_p])
    sa1 = (v['m_ac'][idx_p] - v['m_ac'][idx_m]) / (2 * dl)
    s = sa + sa1 * (c1 - g)
    return c1, s, np.sign(f1), v['kn'][idx_p], 0.5 * (fm + fp)


def lokal_paar(mod, za, zb, prof_b, nsub=NSUB, nbis=NBIS):
    """za: obere Zeile (groesseres w2), zb: untere Zeile (Anker, groesseres Gebiet). Kurven nach Rang k."""
    nk = min(len(za['null']), len(zb['null']))
    out_p, out_k = [], []
    if nk == 0:
        return out_p, out_k
    U = S3.Umgebung(mod, prof_b)
    w2a, w2b = za['w2'], zb['w2']
    pot0 = S3.Pot(mod, [prof_b])
    n_z = n_start(mod, pot0, U.n_m, w2a)

    def fn(mod_, pot, qidx, w2s, rhos, n_m):
        return werte_k(mod_, pot, qidx, w2s, rhos, n_m, n_z)

    def rchi_t(t):
        if t <= 0.0:
            return zb.get('Rchi', float('nan'))
        if t >= 1.0:
            return za.get('Rchi', float('nan'))
        return r_chi(U.profil(w2b + t * (w2a - w2b)))

    kurven = []
    for k in range(nk):
        A, B = za['null'][k], zb['null'][k]
        gap = min(luecke(zb, k), luecke(za, k))
        kurven.append(dict(k=k, gap=gap, dl=max(1e-4 * gap, 1e-9),
                           t=[0.0, 1.0], rho=[B['rho'], A['rho']], s=[B['s'], A['s']], steig=[B['steig'], A['steig']],
                           kn=[B['knoten'], A['knoten']], rangsprung=bool(abs(A['rho'] - B['rho']) > 0.5 * gap)))
    # Unterzeilen
    ts = [i / nsub for i in range(1, nsub)]
    W2, RH, ref = [], [], []
    for ci, c in enumerate(kurven):
        for t in ts:
            g = c['rho'][0] + t * (c['rho'][1] - c['rho'][0])
            W2 += [w2b + t * (w2a - w2b)] * 2
            RH += [g - c['dl'], g + c['dl']]
            ref.append((ci, t, g))
    v = U.werte(fn, W2, RH)
    for j, (ci, t, g) in enumerate(ref):
        c = kurven[ci]
        c1, s, st, kn, fg = newton_rho(v, 2 * j, 2 * j + 1, g, c['dl'])
        if abs(c1 - g) < 0.3 * c['gap'] and abs(fg) < 0.1:
            c['t'].append(t)
            c['rho'].append(float(c1))
            c['s'].append(float(s))
            c['steig'].append(float(st))
            c['kn'].append(int(kn))
        else:
            c.setdefault('weg', []).append(t)
    # Vorzeichenwechsel laengs jeder Kurve
    iv = []
    for ci, c in enumerate(kurven):
        o = np.argsort(c['t'])
        for key in ('t', 'rho', 's', 'steig', 'kn'):
            c[key] = [c[key][i] for i in o]
        nw = 0
        for i in range(len(c['t']) - 1):
            if np.sign(c['s'][i]) != np.sign(c['s'][i + 1]):
                nw += 1
                iv.append(dict(ci=ci, ta=c['t'][i], tb=c['t'][i + 1], ra=c['rho'][i], rb=c['rho'][i + 1],
                               sa=c['s'][i], sb=c['s'][i + 1], sta=c['steig'][i], stb=c['steig'][i + 1],
                               kna=c['kn'][i], knb=c['kn'][i + 1]))
        c['n_wechsel'] = nw
        c['n_wechsel_zeile'] = int(np.sign(c['s'][0]) != np.sign(c['s'][-1]))
        out_k.append(dict(k=c['k'], gap=c['gap'], n_wechsel=nw, n_wechsel_zeile=c['n_wechsel_zeile'],
                          rangsprung=c['rangsprung'], weg=c.get('weg', []), t=c['t'], s=c['s'], rho=c['rho'],
                          kn=c['kn']))
    # Halbierung
    for _ in range(nbis):
        if not iv:
            break
        W2, RH = [], []
        for q in iv:
            c = kurven[q['ci']]
            tm = 0.5 * (q['ta'] + q['tb'])
            g = q['ra'] + 0.5 * (q['rb'] - q['ra'])
            q['_tm'], q['_g'] = tm, g
            W2 += [w2b + tm * (w2a - w2b)] * 2
            RH += [g - c['dl'], g + c['dl']]
        v = U.werte(fn, W2, RH)
        for j, q in enumerate(iv):
            c = kurven[q['ci']]
            c1, s, st, kn, fg = newton_rho(v, 2 * j, 2 * j + 1, q['_g'], c['dl'])
            if abs(c1 - q['_g']) >= 0.3 * c['gap'] or abs(fg) >= 0.1:
                q['weg'] = True
                continue
            if np.sign(s) == np.sign(q['sa']):
                q.update(ta=q['_tm'], ra=float(c1), sa=float(s), sta=float(st), kna=int(kn))
            else:
                q.update(tb=q['_tm'], rb=float(c1), sb=float(s), stb=float(st), knb=int(kn))
    for q in iv:
        c = kurven[q['ci']]
        x = q['sa'] / (q['sa'] - q['sb'])
        ts_ = q['ta'] + x * (q['tb'] - q['ta'])
        Ra, Rb = rchi_t(q['ta']), rchi_t(q['tb'])
        steig = q['sta'] if q['sta'] == q['stb'] else 0.0
        out_p.append(dict(k=c['k'], w2=float(w2b + ts_ * (w2a - w2b)), rho=float(q['ra'] + x * (q['rb'] - q['ra'])),
                          R=float(Ra + x * (Rb - Ra)), t=float(ts_), ta=q['ta'], tb=q['tb'],
                          w2_klammer=[float(w2b + q['ta'] * (w2a - w2b)), float(w2b + q['tb'] * (w2a - w2b))],
                          R_klammer=[float(Ra), float(Rb)], sa=q['sa'], sb=q['sb'], steig=steig,
                          umlauf_zelle=int(np.sign(q['sb'] - q['sa']) * steig), kn=[q['kna'], q['knb']],
                          weg=bool(q.get('weg', False)), gap=c['gap'], w2_zeilen=[w2b, w2a]))
    return out_p, out_k


# ------------------------------------------------------------------ Befehle Suche
def braucht_reparatur(d):
    return any((not q['sicher']) or abs(q['rest']) > 1e-3 for q in d['null'])


def zpfad(adir, stufe, i):
    return os.path.join(adir, 'z-st%d-%04d.json' % (stufe, i))


def cmd_block(tag, stufe, pdir, adir, listejson, i0, i1):
    """Zeilen i0..i1 (einschliesslich) rechnen, dann Zeilenpaare (i, i+1) fuer i0 <= i < i1 lokalisieren."""
    mod = S3.modell_von(tag)
    liste = json.load(open(listejson))['w2']
    i1 = min(i1, len(liste) - 1)
    stopp = os.path.join(os.path.dirname(adir), 'stopp-st%d-%d-%d' % (stufe, i0, i1))
    if os.path.exists(stopp):
        log('Block nicht gerechnet (PLAN-NACHTRAG-2, Stoppdatei %s)' % stopp)
        return
    zeilen = {}
    neu = set()

    def zeile_holen(i):
        pf = zpfad(adir, stufe, i)
        if os.path.exists(pf):
            d0 = json.load(open(pf))
            if d0.get('version', 1) >= 2 or not braucht_reparatur(d0):
                zeilen[i] = d0
                return
            # PLAN-NACHTRAG-1: alte Zeile mit unsicherer Nullstelle neu rechnen, alte Datei als alt-* behalten
            os.replace(pf, os.path.join(adir, 'alt-' + os.path.basename(pf)))
        neu.add(i)
        t1 = time.time()
        p = S3.lade_profil(ppfad(pdir, liste[i]))
        assert abs(p['hp'] - S3.STUFEN[stufe]) < 1e-15
        d = zeile_k(mod, p)
        d['index'] = i
        d['sekunden'] = time.time() - t1
        schreibe(pf, d)
        zeilen[i] = d
        log('zeile %d w2=%.8f R=%.3f n=%d (gitter %d, q %d) %s unsicher=%d | %.1fs' % (
            i, d['w2'], d.get('Rchi', float('nan')), len(d['null']), d['n_vw_gitter'], d['n_q'], d['vorzeichen'],
            sum(1 for z in d['null'] if not z['sicher']), d['sekunden']))

    # Reihenfolge (Ablauf): Zeile i0, dann abwechselnd Zeile i+1 und Paar i (Abbruch laesst einen luckenlosen Anfang)
    zeile_holen(i0)
    for i in range(i0, i1):
        zeile_holen(i + 1)
        pf = os.path.join(adir, 'paar-st%d-%04d.json' % (stufe, i))
        if os.path.exists(pf):
            alt = json.load(open(pf))
            veraltet = (i in neu or i + 1 in neu or zeilen[i].get('version', 1) >= 2 or zeilen[i + 1].get('version', 1) >= 2)
            if alt.get('version', 1) >= 2 or not veraltet:
                continue
            os.replace(pf, os.path.join(adir, 'alt-' + os.path.basename(pf)))
        t1 = time.time()
        prof_b = S3.lade_profil(ppfad(pdir, liste[i + 1]))
        punkte, kurven = lokal_paar(mod, zeilen[i], zeilen[i + 1], prof_b)
        schreibe(pf, dict(i=i, w2a=liste[i], w2b=liste[i + 1], punkte=punkte, kurven=kurven,
                          sekunden=time.time() - t1, version=2,
                          kopplung=('stab' if S3.Pot is PotStab else 'alt'), stat=dict(STAT)))
        log('paar %d (%.8f -> %.8f): %d Stellen, Kurven %d, Rangsprung %d, Wechsel fein/zeile %d/%d | %.1fs' % (
            i, liste[i], liste[i + 1], len(punkte), len(kurven), sum(c['rangsprung'] for c in kurven),
            sum(c['n_wechsel'] for c in kurven), sum(c['n_wechsel_zeile'] for c in kurven), time.time() - t1))


# ------------------------------------------------------------------ Umlauf (Code 1: Newton und Rechteck)
def cmd_umlauf(tag, stufe, pdir, listejson, punktejson, aus, i0, i1):
    mod = S3.modell_von(tag)
    liste = json.load(open(listejson))['w2']
    pk = json.load(open(punktejson))['punkte'][i0:i1]
    erg = dict(stufe=stufe, punkte=[])
    for q in pk:
        t1 = time.time()
        # Anker: naechste Zeile mit w2 <= Start (groesseres Gebiet)
        kand = [x for x in liste if x <= q['w2']]
        za = max(kand) if kand else min(liste)
        anker = S3.lade_profil(ppfad(pdir, za))
        U = S3.Umgebung(mod, anker)
        w2, rho, ok, verl = S3.newton_E1(U, q['w2'], q['rho'])
        e = dict(name=q.get('name'), start=q, w2=w2, rho=rho, konvergiert=ok, newton=verl, anker=za,
                 r_m=U.n_m * anker['hp'], bereich=S3.bereich(mod, w2, rho))
        if ok and e['bereich'] == 'E1':
            v = U.werte(S3.werte_E1, [w2], [rho])
            e['svr'] = float(v['svr'][0])
            e['W_am_punkt'] = [float(v['W'][0].real), float(v['W'][0].imag)]
            pr = U.profil(w2)
            e['chi0'] = pr['chi0']
            e['Rchi'] = r_chi(pr)
            w = math.sqrt(w2)
            abst = min(rho - (math.sqrt(mod.m2) - w), math.sqrt(mod.mc2) - rho, w + math.sqrt(mod.m2) - rho)
            hmax = min(S3.HALB, 0.4 * abst, 0.25 * q.get('gap', 1.0), 0.5 * q.get('dw2_zeile', 1.0))
            e['hmax'] = hmax
            e['umlauf'] = S3.umlauf_mit_rueckfall(U, S3.werte_E1, 'W', w2, rho, hmax)
        e['sekunden'] = time.time() - t1
        e['kopplung'] = 'stab' if S3.Pot is PotStab else 'alt'
        e['stat'] = dict(STAT)
        erg['punkte'].append(e)
        schreibe(aus, erg)
        log('umlauf', json.dumps({k: e[k] for k in e if k not in ('start', 'newton')}))


def cmd_k0newton(tag, stufe, pdir, listejson, refjson, aus, i0, i1):
    """K0 (PLAN 3): Newton (Code 1, newton_E1 auf W) ab der Lage der Runde 18, einmal mit alter, einmal mit
    stabilisierter Kopplung, gleiches Ankerprofil und gleiche Umgebung. Lage = Wurzel von W (Rang G <= 1)."""
    mod = S3.modell_von(tag)
    liste = json.load(open(listejson))['w2']
    ref = json.load(open(refjson))['stellen']
    ref = [d for d in ref if d['gezaehlt'] and d['bereich']][i0:i1]
    erg = dict(stufe=stufe, i0=i0, i1=i1, punkte=[])
    for d in ref:
        w2s = d['w2'] if stufe == 1 else d['w2_2']
        rhos = d['rho'] if stufe == 1 else d['rho_2']
        za = max(x for x in liste if x <= w2s)
        anker = S3.lade_profil(ppfad(pdir, za))
        U = S3.Umgebung(mod, anker)
        e = dict(nr=d['nr'], k=d['k'], i=d['i'], R=d['R'], start=[w2s, rhos], anker=za, r_m=U.n_m * anker['hp'])
        for name, stab in (('alt', False), ('neu', True)):
            setze_kopplung(stab)
            t1 = time.time()
            n0 = STAT['n_maske']
            w2, rho, ok, verl = S3.newton_E1(U, w2s, rhos)
            v = U.werte(S3.werte_E1, [w2], [rho])
            e[name] = dict(w2=w2, rho=rho, ok=bool(ok), it=len(verl), verl=verl, svr=float(v['svr'][0]),
                           W=[float(v['W'][0].real), float(v['W'][0].imag)], sekunden=time.time() - t1,
                           maske_dazu=int(STAT['n_maske'] - n0))
        setze_kopplung(True)
        e['dw2'] = e['neu']['w2'] - e['alt']['w2']
        e['drho'] = e['neu']['rho'] - e['alt']['rho']
        e['maske_anker'] = maske_info(anker)
        erg['punkte'].append(e)
        erg['stat'] = dict(STAT)
        schreibe(aus, erg)
        log('k0newton nr=%d k=%d R=%.2f alt ok=%s it=%d neu ok=%s it=%d dw2=%.2e drho=%.2e maske=%d | %.1fs %.1fs' % (
            d['nr'], d['k'], d['R'], e['alt']['ok'], e['alt']['it'], e['neu']['ok'], e['neu']['it'], e['dw2'],
            e['drho'], e['maske_anker']['n_maske'], e['alt']['sekunden'], e['neu']['sekunden']))


def cmd_k1(stufe, pdir, aus):
    """K1: bewiesene M1-Stelle (chi-Kopplung aus, Variante K1E1 wie Code 1) mit derselben Suchkette."""
    mod = S3.modell_von('K1E1')
    hp = S3.STUFEN[stufe]
    zeilen_w2 = [0.80, 0.79, 0.78] + [0.81, 0.82]
    p0 = S3.saat(mod, 'M1', 200.0, hp)
    profs = {}
    p = p0
    for x in sorted([w for w in zeilen_w2 if w <= p0['w2']], reverse=True):
        p = S3.fortsetzung(mod, p, x, hp)
        profs[x] = p
    p = p0
    for x in sorted([w for w in zeilen_w2 if w > p0['w2']]):
        p = S3.fortsetzung(mod, p, x, hp)
        profs[x] = p
    ws = sorted(profs, reverse=True)
    zeilen = []
    for x in ws:
        pr = profs[x]
        pr['Rchi'] = float('nan')
        pr['m0sq'] = m0sq(mod, pr)
        d = zeile_k(mod, pr)
        zeilen.append(d)
        log('K1 zeile %.2f: n=%d %s rho=%s' % (x, len(d['null']), d['vorzeichen'], [round(z['rho'], 5) for z in d['null']]))
    punkte = []
    for i in range(len(ws) - 1):
        pp, kk = lokal_paar(mod, zeilen[i], zeilen[i + 1], profs[ws[i + 1]])
        punkte += pp
    erg = dict(stufe=stufe, zeilen=[{k: z[k] for k in ('w2', 'null', 'vorzeichen')} for z in zeilen], punkte=punkte)
    schreibe(aus, erg)
    res = []
    for q in punkte:
        anker = profs[max(x for x in ws if x <= q['w2'])]
        e = S3.e1_kandidat(mod, anker, dict(w2=q['w2'], rho=q['rho']), 0.75, 0.85)
        e['abstand_zur_bewiesenen'] = [e['w2'] - S3.K1_STELLE[0], e['rho'] - S3.K1_STELLE[1]]
        res.append(e)
        log('K1 kand', json.dumps({k: e[k] for k in e if k not in ('newton',)}))
    erg['kandidaten'] = res
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


# ------------------------------------------------------------------ Auswertung
def lade_paare(adir, stufe):
    out = []
    for fn in sorted(os.listdir(adir)):
        if fn.startswith('paar-st%d-' % stufe) and fn.endswith('.json'):
            out.append(json.load(open(os.path.join(adir, fn))))
    return sorted(out, key=lambda d: d['i'])


def lade_zeilen(adir, stufe):
    out = []
    for fn in sorted(os.listdir(adir)):
        if fn.startswith('z-st%d-' % stufe) and fn.endswith('.json'):
            out.append(json.load(open(os.path.join(adir, fn))))
    return sorted(out, key=lambda d: d['index'])


def main():
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == 'liste':
        cmd_liste(a[0])
    elif c == 'profile':
        cmd_profile(a[0], int(a[1]), a[2], a[3], weiter=(len(a) > 4 and a[4] == 'weiter'))
    elif c == 'block':
        cmd_block(a[0], int(a[1]), a[2], a[3], a[4], int(a[5]), int(a[6]))
    elif c == 'umlauf':
        cmd_umlauf(a[0], int(a[1]), a[2], a[3], a[4], a[5], int(a[6]), int(a[7]))
    elif c == 'k1':
        cmd_k1(int(a[0]), a[1], a[2])
    elif c == 'k0newton':
        cmd_k0newton(a[0], int(a[1]), a[2], a[3], a[4], a[5], int(a[6]), int(a[7]))
    else:
        raise SystemExit('unbekannt: ' + c)
    log('fertig', json.dumps(STAT))


if __name__ == '__main__':
    main()
