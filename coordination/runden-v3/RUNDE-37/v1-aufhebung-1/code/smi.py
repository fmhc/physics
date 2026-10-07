#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SKALAR-MISCH-1, Runde 48 (fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage: Traegt die Quer-Laengs-Mischung (nn-Anteil von e_j = (1 - P_c) A p_j) den Bahnlagen-Gang 0,004077 der
Kreisbahn-Leckage (IMPULS-NETZ-1 5.2), und lassen Gewichte je Tetraederart (kubisch) TT-Spanne und Gang zugleich
verschwinden?
inz.py, pn.py, ew.py, tp.py, mn.py, nachtrag_iso.py unveraendert aus IMPULS-NETZ-1 (sha256 wie dort).
Schnellrechnung: A = Summe_t J_t A_t ist linear in den Gewichten; B, M, c, S, B_red, Spannungsmuster und P_M sigma
haengen nicht von J ab und werden je Richtung und |k| einmal vorbereitet. Kopplung wie inz.py (R1 mit Impulsquelle):
  f = S^H(-sigma) - A_red^-1 S^H A P_M sigma,  g_j = X_j^H f,  Gn = g/(omega sqrt(C_E)),  C_E = 4 V^2/s^2.
tau(n) = Gn_TT^-1 Gn_rest: effektive TT-Spannung einer Einheits-Spannung L1, L2, nn, Ptr (Basis h+, hx wie ni.basis_tt).
Langwellig (k -> 0): Masse der zwei weichen Moden in der affinen TT-Basis Mh = H^-H (V_s^H A_red^-1 V_s) H^-1,
H = pinv(S^H a_aff) V_s; Extrapolation in s^2 aus |k| = 0,01 ... 0,04 (Lagrange, 4 Punkte).
Aufruf nur ueber kleintest.sh auf der .69:
  python smi.py rauch   --out rauch/r1.json
  python smi.py tabelle --out lauf/tabelle.json
  python smi.py suche   --out lauf/suche.json
  python smi.py karte   --out lauf/karte.json
  python smi.py urteil  --tabelle lauf/tabelle.json --suche lauf/suche.json --out lauf/urteile.json
  python smi.py bild    --tabelle lauf/tabelle.json --suche lauf/suche.json --karte lauf/karte.json --bild lauf/bild-skalar-misch.png --out lauf/bild.json
"""
import argparse, json, sys, time, platform, os, resource, hashlib, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402  (unveraendert)
import pn  # noqa: E402  (unveraendert)
import inz  # noqa: E402  (unveraendert)
import nachtrag_iso as ni  # noqa: E402  (unveraendert)

LP, VCELL, KG = pn.LP, pn.VCELL, pn.KG
cT, herm = pn.cT, pn.herm
ARTEN = ['finn_auf', 'finn_ab', 'kegel_T1', 'kegel_T2', 'sechs_T1', 'sechs_T2']
NAMEN6 = ['h+', 'hx', 'L1', 'L2', 'nn', 'Ptr']
W_ISO = np.array([pn.J_ISO[a] for a in ARTEN])
X_ISO_F1 = np.array([pn.XK, pn.XS])
GANG_P = 0.004077                       # IMPULS-NETZ-1 5.2 [P]
G_P = {'001': 0.9985035624546907, '111': 1.0012214250603886, '110': 1.000541959252857, '123': 1.0005419594652303,
       'z0': 1.0006756118270757, 'z1': 1.0005967975722636, 'z2': 1.0004154898659323, 'z3': 1.0008404930221992,
       'z4': 1.0010993438706333, 'z5': 0.9998092818299712, 'z6': 1.0007186246400144, 'z7': 0.9985516885463013}
S0_LISTE = (0.01, 0.02, 0.03, 0.04)     # |k| (kubische Einheiten) fuer die Extrapolation k -> 0
EPS_TTISO = (1e-3, 2e-3)                # TT-ISO-1-Definition der Spanne
KL_GANG = 0.01                          # IMPULS-NETZ-1: kl = 0,01
LO, HI = -2.0, 2.0                      # log10-Bereich der Gewichte relativ zu finn_auf (wie TT-ISO-1)
T0 = time.time()
RAUCH = False


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def richtungen13():
    m = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (2, 1, 1), (2, 2, 1), (3, 1, 0), (3, 1, 1), (3, 2, 0), (3, 2, 1),
         (3, 2, 2), (3, 3, 1), (3, 3, 2)]
    return [''.join(str(x) for x in v) for v in m], np.array([np.array(v, float) / np.linalg.norm(v) for v in m])


def bahnen():
    """12 Kreisbahnen wie inz.zusatz (Saat 31): S = (u + i w)(u + i w)^T."""
    normalen = [('001', [0, 0, 1]), ('111', [1, 1, 1]), ('110', [1, 1, 0]), ('123', [1, 2, 3])]
    rng = np.random.default_rng(31)
    for i, v in enumerate(rng.normal(size=(8, 3))):
        normalen.append(('z%d' % i, v.tolist()))
    out = []
    for nm, v in normalen:
        m = np.array(v, float) / np.linalg.norm(v)
        u = np.cross(m, [0.3, 0.5, 0.7])
        u /= np.linalg.norm(u)
        w = np.cross(m, u)
        e = u + 1j * w
        out.append((nm, m, np.outer(e, e)))
    return out


def gewichte(x, fam):
    """log10-Gewichte -> J je Art (finn_auf = 1). F1 (Fd-3m): x = (kegel, sechs); F2 (F-43m): x = (finn_ab, kegel_T1,
    kegel_T2, sechs_T1, sechs_T2)."""
    x = np.asarray(x, float)
    if fam == 'F1':
        return np.array([1.0, 1.0, 10 ** x[0], 10 ** x[0], 10 ** x[1], 10 ** x[1]])
    return np.concatenate([[1.0], 10.0 ** x])


def volumen_je_art(mod):
    v = {}
    for z in mod['zellen']:
        v.setdefault(z['art'], []).append(z['vol'])
    return {a: [float(min(x)), float(max(x)), len(x)] for a, x in v.items()}


def A_teile(mod, k):
    """A je Tetraeder-Art (wie pn.A_J mit Gewicht 1 fuer genau eine Art): (6, ..., E, E)."""
    sh = k.shape[:-1]
    E = mod['E']
    A = np.zeros((len(ARTEN),) + sh + (E, E), complex)
    for z in mod['zellen']:
        if not z['kin']:
            continue
        t = ARTEN.index(z['art'])
        ph = [np.exp(1j * (k @ T)) for (e, T) in z['kanten']]
        idx = [e for (e, T) in z['kanten']]
        A0 = z['A0']
        for i in range(len(idx)):
            pci = np.conj(ph[i])
            for j in range(len(idx)):
                A[t, ..., idx[i], idx[j]] += A0[i, j] * pci * ph[j]
    return A


def vorbereiten(mod, Q, ndir, s, spannung=True, chunk=64):
    """J-unabhaengige Teile je Richtung bei |k| = s (kubische Einheiten)."""
    teile = []
    for i0 in range(0, len(ndir), chunk):
        nn = ndir[i0:i0 + chunk]
        k = s * nn
        o = ew.ops(mod, k)
        B, M, c = o['B'], o['M'], o['c']
        S, r = inz.basis(None, M, c)
        Sh = cT(S)
        Bred = herm(Sh @ B @ S)
        lb, Vb = np.linalg.eigh(Bred)
        At = A_teile(mod, k)
        Art = np.stack([herm(Sh @ At[t] @ S) for t in range(len(ARTEN))])
        ph = np.exp(1j * (k @ mod['mitte'].T))
        Tb = np.zeros((len(nn), 6, 3, 3))
        LD = np.zeros((len(nn), 2))
        for j, n in enumerate(nn):
            tens, e1, e2 = ni.basis_tt(n)
            for a, nm in enumerate(NAMEN6):
                Tb[j, a] = tens[nm]
            Lam = inz.lam_proj(n, np.diag(n ** 2))
            LD[j] = [np.sum(Lam * tens['h+']), np.sum(Lam * tens['hx'])]
        aff = np.einsum('ei,kaij,ej->kae', mod['n'], Tb[:, :2], mod['n']) * ph[:, None, :]
        Y = np.einsum('ked,kae->kda', np.conj(S), aff)
        d = {'rang': r, 'Bred': Bred, 'lb': lb, 'Vs': Vb[:, :, :2], 'Art': Art, 'Tb': Tb, 'LD': LD, 'Y': Y}
        if spannung:
            Mx = Tb - np.einsum('kaii->ka', Tb)[:, :, None, None] * np.eye(3)
            sig = np.einsum('eij,kaij->kae', Q, Mx) * ph[:, None, :]
            f0 = np.einsum('ked,kae->kad', np.conj(S), -sig)
            MhM = herm(cT(M) @ M)
            zz = np.linalg.solve(MhM, np.einsum('kev,kae->kva', np.conj(M), sig))
            PMs = np.einsum('kev,kva->kae', M, zz)
            SAP = np.stack([np.einsum('ked,kae->kad', np.conj(S), np.einsum('kef,kaf->kae', At[t], PMs))
                            for t in range(len(ARTEN))])
            d.update({'f0': f0, 'SAP': SAP})
        teile.append(d)
    pre = {}
    for key in teile[0]:
        pre[key] = np.concatenate([d[key] for d in teile], axis=(1 if key in ('Art', 'SAP') else 0))
    pre['s'] = float(s)
    pre['n'] = np.asarray(ndir)
    return pre


def auswerten(pre, w, kopplung=True):
    s = pre['s']
    Ared = np.einsum('t,tkab->kab', w, pre['Art'])
    L = np.linalg.cholesky(Ared)
    om2, U = np.linalg.eigh(herm(cT(L) @ pre['Bred'] @ L))
    out = {'w2': om2[:, :2] / s ** 2, 'luecke': om2[:, 2] / om2[:, 1]}
    Vs = pre['Vs']
    Mm = herm(cT(Vs) @ np.linalg.solve(Ared, Vs))
    Y = pre['Y']
    H = np.linalg.solve(herm(cT(Y) @ Y), cT(Y)) @ Vs
    Hi = np.linalg.inv(H)
    out['Mh'] = herm(cT(Hi) @ Mm @ Hi)
    out['Kh'] = herm(cT(Hi) @ (pre['lb'][:, :2, None] * Hi)) / s ** 2
    if kopplung:
        X = L @ U[:, :, :2]
        SAP = np.einsum('t,tkad->kad', w, pre['SAP'])
        fJ = -np.linalg.solve(Ared, np.swapaxes(SAP, 1, 2))
        f = pre['f0'] + np.swapaxes(fJ, 1, 2)
        g = np.einsum('kdj,kad->kja', np.conj(X), f)
        CE = 4 * VCELL ** 2 / s ** 2
        Gn = g / np.sqrt(om2[:, :2, None] * CE)
        gs = np.einsum('kdj,kad->kja', np.conj(Vs), f)
        out['Gn'] = Gn
        out['tau_dyn'] = np.linalg.solve(Gn[:, :, :2], Gn[:, :, 2:])
        out['tau_stat'] = np.linalg.solve(gs[:, :, :2], gs[:, :, 2:])
        out['C_stat'] = (np.abs(gs) ** 2 / pre['lb'][:, :2, None]).sum(1) / CE
    return out


def lagrange0(s_list):
    x = np.array(s_list, float) ** 2
    return np.array([np.prod([x[j] / (x[j] - x[i]) for j in range(len(x)) if j != i]) for i in range(len(x))])


# ------------------------------------------------------------------------------------------------ Bahnen und Gang
def G_exakt(Gn, Tb, wd, bl):
    """wie inz.kreisbahnen dyn: Summe_n w |Gn . T|^2 / Summe_n w |T_TT|^2 (lineare Zerlegung, alle 6 Spalten)."""
    out = []
    for nm, m, T in bl:
        Ta = np.einsum('kaij,ij->ka', Tb, T)
        amp = np.einsum('kja,ka->kj', Gn, Ta)
        out.append(float((wd * (np.abs(amp) ** 2).sum(-1)).sum() / (wd * (np.abs(Ta[:, :2]) ** 2).sum(-1)).sum()))
    return np.array(out)


def G_tau(tau, Tb, wd, bl, nur=None):
    """TT-Kopplung als isotrop gesetzt: Summe w |T_TT + tau T_rest|^2 / Summe w |T_TT|^2; nur = Spaltenauswahl von tau."""
    out = []
    for nm, m, T in bl:
        Ta = np.einsum('kaij,ij->ka', Tb, T)
        tt = tau if nur is None else tau * np.array([1.0 if i in nur else 0.0 for i in range(4)])[None, None, :]
        Te = Ta[:, :2] + np.einsum('kia,ka->ki', tt, Ta[:, 2:])
        out.append(float((wd * (np.abs(Te) ** 2).sum(-1)).sum() / (wd * (np.abs(Ta[:, :2]) ** 2).sum(-1)).sum()))
    return np.array(out)


def G_W2_quad(kappa, LD, Tb, wd, bl):
    out = []
    for nm, m, T in bl:
        Ta = np.einsum('kaij,ij->ka', Tb, T)
        Te = Ta[:, :2] + kappa * Ta[:, 4:5] * LD
        out.append(float((wd * (np.abs(Te) ** 2).sum(-1)).sum() / (wd * (np.abs(Ta[:, :2]) ** 2).sum(-1)).sum()))
    return np.array(out)


def G_W2_formel(kappa, m4):
    """Winkelformel (PLAN 2.2, vorab): G = 1 + (4/315) kappa^2 + (Summe m^4 - 3/5)(5 kappa/126 - kappa^2/819)."""
    m4 = np.asarray(m4, float)
    return 1.0 + 4.0 / 315.0 * kappa ** 2 + (m4 - 0.6) * (5.0 * kappa / 126.0 - kappa ** 2 / 819.0)


def gang_fit(G, m4):
    """G = a + b Summe m^4 (kleinste Quadrate); Gang = -b (Vorzeichen wie IMPULS-NETZ-1: G = 1 + Gang (c - Summe m^4))."""
    A = np.stack([np.ones(len(m4)), np.asarray(m4)], 1)
    (a, b), *_ = np.linalg.lstsq(A, np.asarray(G), rcond=None)
    rest = float(np.abs(A @ np.array([a, b]) - G).max())
    return {'gang': float(-b), 'a': float(a), 'c': float(-(a - 1.0) / b) if b != 0 else None, 'fitrest_max': rest,
            'iso_anteil': float(a + 0.6 * b - 1.0)}


def kappa_fit(tau_nn, LD, wd):
    den = (wd * (LD ** 2).sum(-1)).sum()
    kr = float((wd * (np.real(tau_nn) * LD).sum(-1)).sum() / den)
    ki = float((wd * (np.imag(tau_nn) * LD).sum(-1)).sum() / den)
    rest = math.sqrt(float((wd * (np.abs(tau_nn - kr * LD) ** 2).sum(-1)).sum() / max((wd * (np.abs(tau_nn) ** 2).sum(-1)).sum(), 1e-300)))
    return kr, ki, rest


# ------------------------------------------------------------------------------------------------ langwellige Masse
def tt_null(pres, w):
    lw = lagrange0([p['s'] for p in pres])
    res = [auswerten(p, w, kopplung=False) for p in pres]
    Mh0 = sum(lw[i] * res[i]['Mh'] for i in range(len(pres)))
    Kh0 = sum(lw[i] * res[i]['Kh'] for i in range(len(pres)))
    em = np.linalg.eigvalsh(herm(Mh0))
    ek = np.linalg.eigvalsh(herm(Kh0))
    mq = float(np.real(np.trace(Mh0, axis1=1, axis2=2)).mean() / 2)
    r = np.stack([np.real(Mh0[:, 0, 0]) / mq - 1, np.real(Mh0[:, 1, 1]) / mq - 1, np.real(Mh0[:, 0, 1]) / mq,
                  np.imag(Mh0[:, 0, 1]) / mq], 1).ravel()
    w2 = np.array([res[i]['w2'] for i in range(len(pres))])
    return {'spanne0': float(em.max() / em.min() - 1), 'Kh0_spanne': float(ek.max() / ek.min() - 1),
            'Kh0_mittel': float(ek.mean()), 'Mh0_mittel': mq, 'Mh0_eig': em, 'res': r, 'w2_je_s': w2,
            'w2_0_aus_masse': float(ek.mean() / mq), 'im_max': float(np.abs(np.imag(Mh0)).max() / mq)}


def spanne_ttiso(pres_eps, w):
    w2 = np.concatenate([auswerten(p, w, kopplung=False)['w2'] for p in pres_eps])
    return float(w2.max() / w2.min() - 1), w2


def gang_null(pres200, w, wd, bl, m4):
    lw = lagrange0([p['s'] for p in pres200])
    Gs = []
    for p in pres200:
        a = auswerten(p, w)
        Gs.append(G_tau(a['tau_stat'], p['Tb'], wd, bl))
    G0 = sum(lw[i] * Gs[i] for i in range(len(pres200)))
    return gang_fit(G0, m4), G0, np.array(Gs)


def gang_kl(pre_kl, w, wd, bl, m4):
    a = auswerten(pre_kl, w)
    G = G_exakt(a['Gn'], pre_kl['Tb'], wd, bl)
    return gang_fit(G, m4), G, a


# ------------------------------------------------------------------------------------------------ Suche (Levenberg-Marquardt)
def lm(fun, x0, maxit=40, h=1e-6, ftol=1e-30, zeit=None):
    x = np.array(x0, float)
    r = fun(x)
    F = float(r @ r)
    mu = 1e-3
    hist = [{'it': 0, 'F': F, 'x': x.tolist()}]
    for it in range(1, maxit + 1):
        if zeit is not None and time.time() > zeit:
            hist.append({'it': it, 'abbruch': 'zeit'})
            break
        Jm = np.empty((len(r), len(x)))
        for i in range(len(x)):
            e = np.zeros(len(x))
            e[i] = h
            Jm[:, i] = (fun(np.clip(x + e, LO, HI)) - fun(np.clip(x - e, LO, HI))) / (2 * h)
        g = Jm.T @ r
        Hm = Jm.T @ Jm
        ok = False
        while mu < 1e14:
            try:
                dx = -np.linalg.solve(Hm + mu * np.diag(np.diag(Hm) + 1e-300), g)
            except np.linalg.LinAlgError:
                mu *= 4
                continue
            xn = np.clip(x + dx, LO, HI)
            rn = fun(xn)
            Fn = float(rn @ rn)
            if Fn < F:
                x, r, F = xn, rn, Fn
                mu = max(mu / 4, 1e-15)
                ok = True
                break
            mu *= 4
        hist.append({'it': it, 'F': F, 'x': x.tolist(), 'mu': mu})
        if not ok or F < ftol:
            break
    return x, r, hist


class Ziel:
    """Residuen fuer die Suche. art: 'tt0' (TT langwellig), 'tt0_gang0' (dazu Gang langwellig), 'ttiso_gangkl'."""

    def __init__(self, fam, art, pres13, pres200, pres_eps, pre_kl, wd, bl, m4, gw=1.0, p2=None):
        self.fam, self.art, self.p13, self.p200, self.peps, self.pkl = fam, art, pres13, pres200, pres_eps, pre_kl
        self.wd, self.bl, self.m4, self.gw, self.p2 = wd, bl, m4, gw, p2
        self.n_eval = 0

    def __call__(self, x):
        self.n_eval += 1
        w = gewichte(x, self.fam)
        if self.art == 'kompakt':
            try:
                d, q, off = dtt_q(self.p2, w)
                gg, _, _ = gang_null(self.p200, w, self.wd, self.bl, self.m4)
                return np.array([d, math.sqrt(max(q, 0.0)), off, self.gw * gg['gang']])
            except np.linalg.LinAlgError:
                return np.full(4, 1e3)
        try:
            if self.art.startswith('tt0'):
                r = tt_null(self.p13, w)['res']
                if self.art == 'tt0_gang0':
                    gg, _, _ = gang_null(self.p200, w, self.wd, self.bl, self.m4)
                    r = np.concatenate([r, [self.gw * gg['gang']]])
            else:
                sp, w2 = spanne_ttiso(self.peps, w)
                r = (w2.ravel() / w2.mean() - 1)
                gg, _, _ = gang_kl(self.pkl, w, self.wd, self.bl, self.m4)
                r = np.concatenate([r, [self.gw * gg['gang']]])
        except np.linalg.LinAlgError:
            r = np.full(53 if self.art == 'ttiso_gangkl' else (53 if self.art == 'tt0_gang0' else 52), 1e3)
        return r


def messen(w, P, wd, bl, m4):
    """Alle Kennzahlen fuer einen Gewichtssatz."""
    out = {'w': w.tolist()}
    try:
        t0 = tt_null(P['p13'], w)
        out['tt_spanne0'] = t0['spanne0']
        out['Kh0_spanne'] = t0['Kh0_spanne']
        out['Mh0_im_max'] = t0['im_max']
        out['tt_spanne_ttiso'], _ = spanne_ttiso(P['peps'], w)
        g0, G0, _ = gang_null(P['p200'], w, wd, bl, m4)
        out['gang0'] = g0['gang']
        out['iso0'] = g0['iso_anteil']
        out['G0'] = G0.tolist()
        gk, Gk, a = gang_kl(P['pkl'], w, wd, bl, m4)
        out['gang_kl001'] = gk['gang']
        out['iso_kl001'] = gk['iso_anteil']
        out['G_kl001'] = Gk.tolist()
        kr, ki, rest = kappa_fit(a['tau_dyn'][:, :, 2], P['pkl']['LD'], wd)
        out['kappa_kl001'] = kr
        out['kappa_im'] = ki
        out['kappa_rest'] = rest
        out['luecke_max'] = float(a['luecke'].max())
        out['ok'] = True
    except np.linalg.LinAlgError:
        out['ok'] = False
    return out


def stabil(mod, w, L=8, chunk=64):
    g = np.arange(L)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    kall = (mm / L) @ ew.BV
    nA, nB, wmin = 0, 0, np.inf
    for i0 in range(0, len(kall), chunk):
        k = kall[i0:i0 + chunk]
        o = ew.ops(mod, k)
        S, r = inz.basis(None, o['M'], o['c'])
        Bred = herm(cT(S) @ o['B'] @ S)
        At = A_teile(mod, k)
        Ared = herm(np.einsum('t,tkef->kef', w, np.stack([cT(S) @ At[t] @ S for t in range(len(ARTEN))])))
        eB = np.linalg.eigvalsh(Bred)
        eA = np.linalg.eigvalsh(Ared)
        nB += int((eB.min(-1) <= 0).sum())
        nA += int((eA.min(-1) <= 0).sum())
        for j in range(len(k)):
            if eA[j].min() > 0 and eB[j].min() > 0:
                Lc = np.linalg.cholesky(Ared[j])
                om = np.linalg.eigvalsh(herm(cT(Lc) @ Bred[j] @ Lc))
                wmin = min(wmin, float(om.min() / om.max()))
    return {'nk': int(len(kall)), 'k_A_red_nicht_pd': nA, 'k_B_red_nicht_pd': nB, 'w2_min_rel': wmin,
            'stabil': bool(nA == 0 and nB == 0 and wmin > 0)}


# ------------------------------------------------------------------------------------------------ Vorbereitung gemeinsam
def alles_vorbereiten(mod, Q, mit200=True, nt=10, nphi=20):
    nm13, n13 = richtungen13()
    P = {'nm13': nm13, 'n13': n13}
    P['p13'] = [vorbereiten(mod, Q, n13, s, spannung=False) for s in S0_LISTE]
    P['peps'] = [vorbereiten(mod, Q, n13, e, spannung=False) for e in EPS_TTISO]
    n2 = np.array([[1.0, 0, 0], [1 / math.sqrt(2), 1 / math.sqrt(2), 0]])
    P['p2'] = [vorbereiten(mod, Q, n2, s, spannung=False) for s in S0_LISTE]
    if mit200:
        nd, wd = pn.richtungen(nt, nphi)
        P['nd'], P['wd'] = nd, wd
        P['p200'] = [vorbereiten(mod, Q, nd, s) for s in S0_LISTE]
        P['pkl'] = vorbereiten(mod, Q, nd, KL_GANG / LP)
    return P


# ------------------------------------------------------------------------------------------------ Modi
def rauch():
    """<= 120 s: Zeiten, Genauigkeitsboden (Symmetriebilder), Steifigkeitsprobe, F1-Frage der Karte (TT allein)."""
    t0 = time.time()
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = ni.Q_map(mod, tder)
    out = {'t_mod': time.time() - t0}
    # Kontrolle A_teile gegen pn.A_J (J_iso)
    k = 0.03 * np.array([[0.3, 0.5, 0.81]])
    At = A_teile(mod, k)
    out['KA_A_teile_gegen_A_J'] = float(np.abs(np.einsum('t,tkef->kef', W_ISO, At) - pn.A_J(mod, k, pn.J_ISO)).max())
    # Symmetriebilder: [100]-Bilder, [111]-Bilder, allgemeine Richtung und ihre Permutationen/Vorzeichen
    g = np.array([0.31, 0.52, 0.795])
    g /= np.linalg.norm(g)
    bilder = [np.array(v, float) / np.linalg.norm(v) for v in ([1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1], [1, -1, -1],
                                                             [-1, 1, -1], [-1, -1, 1])]
    bilder += [g[list(p)] * sgn for p in ((0, 1, 2), (1, 2, 0), (2, 0, 1), (1, 0, 2)) for sgn in (np.array([1, 1, 1]), np.array([-1, 1, 1]))]
    bilder = np.array(bilder)
    t1 = time.time()
    pb = [vorbereiten(mod, Q, bilder, s, spannung=False) for s in S0_LISTE]
    out['t_vorb_15x4'] = time.time() - t1
    tn = tt_null(pb, W_ISO)
    em = tn['Mh0_eig']
    out['boden'] = {'100_bilder': float(np.ptp(em[0:3], axis=0).max() / tn['Mh0_mittel']),
                    '111_bilder': float(np.ptp(em[3:7], axis=0).max() / tn['Mh0_mittel']),
                    'allgemein_bilder': float(np.ptp(em[7:], axis=0).max() / tn['Mh0_mittel']),
                    'Mh0_im_max': tn['im_max']}
    # 3 statt 4 Punkte (Extrapolationsrest)
    tn3 = tt_null(pb[:3], W_ISO)
    out['extrapolation_3_gegen_4'] = float(np.abs(tn3['Mh0_eig'] - em).max() / tn['Mh0_mittel'])
    out['Kh0'] = {'mittel': tn['Kh0_mittel'], 'spanne': tn['Kh0_spanne']}
    # Vorbereitung 13 Richtungen und Zeit einer 200-Richtungen-Auswertung
    t1 = time.time()
    P = alles_vorbereiten(mod, Q, mit200=False)
    out['t_vorb_13'] = time.time() - t1
    nd, wd = pn.richtungen(10, 20)
    t1 = time.time()
    p200 = vorbereiten(mod, Q, nd, KL_GANG / LP)
    out['t_vorb_200'] = time.time() - t1
    t1 = time.time()
    auswerten(p200, W_ISO)
    out['t_ausw_200'] = time.time() - t1
    # F1-Frage der Karte: TT allein (2 Verhaeltnisse, 2 Bedingungen), LM ab J_iso
    t1 = time.time()
    z = Ziel('F1', 'tt0', P['p13'], None, None, None, None, None, None)
    sp_start = tt_null(P['p13'], W_ISO)['spanne0']
    x, r, hist = lm(z, X_ISO_F1, maxit=25, zeit=time.time() + 40)
    w = gewichte(x, 'F1')
    out['F1_tt_allein'] = {'x_start': X_ISO_F1.tolist(), 'spanne0_start': sp_start,
                           'spanne_ttiso_start': spanne_ttiso(P['peps'], W_ISO)[0],
                           'x_ende': x.tolist(), 'spanne0_ende': tt_null(P['p13'], w)['spanne0'],
                           'spanne_ttiso_ende': spanne_ttiso(P['peps'], w)[0], 'F_verlauf': [h_.get('F') for h_ in hist],
                           'n_eval': z.n_eval, 't': time.time() - t1}
    out['t_gesamt'] = time.time() - t0
    return out


def tt_diagnose(p13, w):
    """Zerlegung der langwelligen TT-Masse an [100], [110], [111] (Indizes 0, 1, 2 von richtungen13)."""
    t = tt_null(p13, w)
    em = t['Mh0_eig'] / t['Mh0_mittel']
    return {'100': em[0].tolist(), '110': em[1].tolist(), '111': em[2].tolist(),
            'dTT_100': float(em[0, 1] - em[0, 0]), 'spanne0': t['spanne0']}


def rauch2():
    """<= 120 s: F1-Frage der Karte genauer: Gitter der langwelligen TT-Spanne, LM aus den besten Gitterpunkten."""
    t0 = time.time()
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = ni.Q_map(mod, tder)
    P = alles_vorbereiten(mod, Q, mit200=False)
    x0s = np.linspace(-2.0, 1.0, 41)
    x1s = np.linspace(-1.5, 1.5, 41)
    G = np.full((41, 41), np.nan)
    for i, a_ in enumerate(x0s):
        for j, b_ in enumerate(x1s):
            try:
                G[i, j] = tt_null(P['p13'], gewichte([a_, b_], 'F1'))['spanne0']
            except np.linalg.LinAlgError:
                pass
    out = {'t_gitter': time.time() - t0, 'gitter_min': float(np.nanmin(G)), 'gitter_ungueltig': int(np.isnan(G).sum())}
    # lokale Minima im Gitter
    lok = []
    for i in range(1, 40):
        for j in range(1, 40):
            v = G[i, j]
            if np.isfinite(v) and all(not np.isfinite(G[i + a, j + b]) or G[i + a, j + b] >= v for a in (-1, 0, 1) for b in (-1, 0, 1)):
                lok.append((float(v), float(x0s[i]), float(x1s[j])))
    lok.sort()
    out['lokale_minima'] = lok[:6]
    out['diagnose_J_iso'] = tt_diagnose(P['p13'], W_ISO)
    lm_res = []
    starts = [np.array([v[1], v[2]]) for v in lok[:3]] + [X_ISO_F1]
    for x0 in starts:
        if time.time() - t0 > 95:
            break
        z = Ziel('F1', 'tt0', P['p13'], None, None, None, None, None, None)
        x, r, hist = lm(z, x0, maxit=80, zeit=min(time.time() + 20, t0 + 105))
        w = gewichte(x, 'F1')
        lm_res.append({'x0': x0.tolist(), 'x': x.tolist(), 'diagnose': tt_diagnose(P['p13'], w),
                       'F': [h_.get('F') for h_ in hist][::5], 'mu_ende': hist[-1].get('mu'), 'n_it': len(hist) - 1})
    out['lm'] = lm_res
    out['t_gesamt'] = time.time() - t0
    return out


def dtt_q(p2, w):
    """[100]: dTT = (m_E - m_T)/m (Basis h+ = E_g, hx = T2g); [110]: Q = (m_+ - m_x)/m - (3/4) dTT (Lambda[D]-Anteil)."""
    lw = lagrange0([p['s'] for p in p2])
    res = [auswerten(p, w, kopplung=False) for p in p2]
    M0 = np.real(sum(lw[i] * res[i]['Mh'] for i in range(len(p2))))
    m = 0.5 * (M0[0, 0, 0] + M0[0, 1, 1])
    d = (M0[0, 0, 0] - M0[0, 1, 1]) / m
    q = (M0[1, 0, 0] - M0[1, 1, 1]) / m - 0.75 * d
    return float(d), float(q), float(M0[1, 0, 1] / m)


def rauch3():
    """<= 120 s: F1 entlang der Kurve dTT = 0: Minimum von Q (Lambda[D]-Anteil der TT-Masse)."""
    t0 = time.time()
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q_ = ni.Q_map(mod, tder)
    n2 = np.array([[1.0, 0, 0], [1 / math.sqrt(2), 1 / math.sqrt(2), 0]])
    p2 = [vorbereiten(mod, Q_, n2, s, spannung=False) for s in S0_LISTE]
    nm13, n13 = richtungen13()
    p13 = [vorbereiten(mod, Q_, n13, s, spannung=False) for s in S0_LISTE]
    out = {'J_iso': dtt_q(p2, W_ISO)}
    x0g = np.linspace(-2.0, 1.0, 61)

    def wurzeln(x1):
        vals = []
        for a_ in x0g:
            try:
                vals.append(dtt_q(p2, gewichte([a_, x1], 'F1'))[0])
            except np.linalg.LinAlgError:
                vals.append(np.nan)
        rs = []
        for i in range(len(x0g) - 1):
            if np.isfinite(vals[i]) and np.isfinite(vals[i + 1]) and vals[i] * vals[i + 1] < 0:
                lo_, hi_ = x0g[i], x0g[i + 1]
                flo = vals[i]
                for _ in range(48):
                    mid = 0.5 * (lo_ + hi_)
                    fm = dtt_q(p2, gewichte([mid, x1], 'F1'))[0]
                    if fm * flo < 0:
                        hi_ = mid
                    else:
                        lo_, flo = mid, fm
                rs.append(0.5 * (lo_ + hi_))
        return rs
    kurve = []
    for x1 in np.linspace(-1.0, 1.0, 21):
        if time.time() - t0 > 70:
            break
        for r0 in wurzeln(x1):
            d, q, off = dtt_q(p2, gewichte([r0, x1], 'F1'))
            kurve.append({'x1': float(x1), 'x0': float(r0), 'dTT': d, 'Q': q, 'off110': off})
    out['kurve'] = kurve
    # Verfeinerung: Minimum von Q entlang des Asts mit dem kleinsten Q (Goldener Schnitt in x1)
    if kurve:
        best = min(kurve, key=lambda z: z['Q'])
        a_, b_ = best['x1'] - 0.1, best['x1'] + 0.1
        gr = (math.sqrt(5) - 1) / 2

        def qv(x1):
            rs = [r for r in wurzeln(x1) if abs(r - best['x0']) < 0.3]
            if not rs:
                return np.inf, None
            r0 = min(rs, key=lambda r: abs(r - best['x0']))
            return dtt_q(p2, gewichte([r0, x1], 'F1'))[1], r0
        c_, d_ = b_ - gr * (b_ - a_), a_ + gr * (b_ - a_)
        fc, fd = qv(c_)[0], qv(d_)[0]
        for _ in range(30):
            if time.time() - t0 > 105:
                break
            if fc < fd:
                b_, d_, fd = d_, c_, fc
                c_ = b_ - gr * (b_ - a_)
                fc = qv(c_)[0]
            else:
                a_, c_, fc = c_, d_, fd
                d_ = a_ + gr * (b_ - a_)
                fd = qv(d_)[0]
        xm = 0.5 * (a_ + b_)
        qm, r0 = qv(xm)
        if r0 is not None:
            w = gewichte([r0, xm], 'F1')
            out['minimum'] = {'x': [r0, xm], 'Q': qm, 'dTT': dtt_q(p2, w)[0], 'spanne0': tt_null(p13, w)['spanne0'],
                              'diagnose': tt_diagnose(p13, w)}
    out['t_gesamt'] = time.time() - t0
    return out


def tabelle():
    """Schritt 1 und 2: nn-Tabelle (200 Richtungen, kl = 0,01, J_iso), Winkelformel, 12 Bahnen, Kontrollen."""
    t0 = time.time()
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = ni.Q_map(mod, tder)
    nd, wd = pn.richtungen(10, 20)
    bl = bahnen()
    m4 = np.array([float((m ** 4).sum()) for _, m, _ in bl])
    pre = vorbereiten(mod, Q, nd, KL_GANG / LP)
    a = auswerten(pre, W_ISO)
    Gn, tau = a['Gn'], a['tau_dyn']
    out = {'kl': KL_GANG, 'nd': int(len(nd)), 'rang': sorted(set(int(x) for x in pre['rang'])), 'bahnen': [b[0] for b in bl],
           'summe_m4': m4.tolist()}
    # Schritt 1: nn-Anteil je Zweig und Richtung
    Ctt = (np.abs(Gn[:, :, :2]) ** 2).sum(-1)               # (nd, 2) TT-Kopplung je Zweig
    Cnn = np.abs(Gn[:, :, 4]) ** 2                          # (nd, 2)
    anteil = Cnn / Ctt
    tnn = tau[:, :, 2]
    s4 = (nd ** 4).sum(-1)
    f_LD = (pre['LD'] ** 2).sum(-1)
    out['tabelle'] = [{'n': nd[i].tolist(), 'w2_ueber_k2': a['w2'][i].tolist(), 'C_TT_je_zweig': Ctt[i].tolist(),
                       'C_nn_je_zweig': Cnn[i].tolist(), 'nn_anteil_je_zweig': anteil[i].tolist(),
                       'tau_nn_re': np.real(tnn[i]).tolist(), 'tau_nn_im': np.imag(tnn[i]).tolist(),
                       'LamD': pre['LD'][i].tolist(), 'summe_n4': float(s4[i]),
                       'C_L_max': float(np.abs(Gn[i, :, 2:4]).max() ** 2), 'C_Ptr_max': float(np.abs(Gn[i, :, 5]).max() ** 2)}
                      for i in range(len(nd))]
    kr, ki, rest = kappa_fit(tnn, pre['LD'], wd)
    tab = {'kappa': kr, 'kappa_im': ki, 'kappa_rest_rel': rest,
           'tau_nn_betrag2_max': float((np.abs(tnn) ** 2).sum(-1).max()),
           'C_nn_summe_max': float(Cnn.sum(-1).max()), 'nn_anteil_max': float(anteil.max()),
           'nn_anteil_mittel': float((wd[:, None] * anteil).sum() / (2 * wd.sum())),
           'C_L_max': float((np.abs(Gn[:, :, 2:4]) ** 2).max()), 'C_Ptr_max': float((np.abs(Gn[:, :, 5]) ** 2).max()),
           'tau_im_max': float(np.abs(np.imag(tnn)).max()), 'w2_spanne_kl001': float(a['w2'].max() / a['w2'].min() - 1)}
    # kappa je Kubik-Invariante: Quotient tau/LamD auf Richtungen mit |LamD|^2 > 1e-3
    sel = f_LD > 1e-3
    q = (np.real(tnn) * pre['LD']).sum(-1)[sel] / f_LD[sel]
    tab['kappa_lokal_min_max'] = [float(q.min()), float(q.max())]
    A_ = np.stack([np.ones(sel.sum()), s4[sel] - 0.6], 1)
    cf, *_ = np.linalg.lstsq(A_, q, rcond=None)
    tab['kappa_lokal_gegen_s4'] = {'k0': float(cf[0]), 'k1': float(cf[1])}
    out['zusammenfassung'] = tab
    # benannte Richtungen
    nm_b = [('110', [1, 1, 0]), ('210', [2, 1, 0]), ('211', [2, 1, 1]), ('123', [1, 2, 3]), ('100', [1, 0, 0]), ('111', [1, 1, 1])]
    nb = np.array([np.array(v, float) / np.linalg.norm(v) for _, v in nm_b])
    pb = vorbereiten(mod, Q, nb, KL_GANG / LP)
    ab = auswerten(pb, W_ISO)
    out['benannt'] = {nm: {'C_nn_summe': float((np.abs(ab['Gn'][i, :, 4]) ** 2).sum()),
                           'C_nn_stat': float(ab['C_stat'][i, 4]), 'tau_nn': np.real(ab['tau_dyn'][i, :, 2]).tolist(),
                           'LamD': pb['LD'][i].tolist(), 'kappa_lokal': float((np.real(ab['tau_dyn'][i, :, 2]) * pb['LD'][i]).sum()
                                                                             / max((pb['LD'][i] ** 2).sum(), 1e-300))}
                      for i, (nm, _) in enumerate(nm_b)}
    # Schritt 2: Winkelformel gegen 12 Bahnen
    G_ex = G_exakt(Gn, pre['Tb'], wd, bl)
    G_W2f = G_W2_formel(kr, m4)
    G_W2q = G_W2_quad(kr, pre['LD'], pre['Tb'], wd, bl)
    G_W1 = G_tau(tau, pre['Tb'], wd, bl, nur=[2])
    G_alle = G_tau(tau, pre['Tb'], wd, bl)
    GP = np.array([G_P[b[0]] for b in bl])
    out['bahnen_G'] = {'P': GP.tolist(), 'exakt_neu': G_ex.tolist(), 'W2_formel': G_W2f.tolist(), 'W2_quadratur': G_W2q.tolist(),
                       'W1_tabelle_nn': G_W1.tolist(), 'tau_alle': G_alle.tolist()}
    out['gang'] = {k_: gang_fit(v, m4) for k_, v in (('P', GP), ('exakt_neu', G_ex), ('W2_formel', G_W2f),
                                                     ('W2_quadratur', G_W2q), ('W1_tabelle_nn', G_W1), ('tau_alle', G_alle))}
    out['abw'] = {'exakt_neu_gegen_P_max': float(np.abs(G_ex - GP).max()), 'W2_formel_gegen_P_max': float(np.abs(G_W2f - GP).max()),
                  'W2_quad_gegen_formel_max': float(np.abs(G_W2q - G_W2f).max()), 'W1_gegen_P_max': float(np.abs(G_W1 - GP).max())}
    # Kontrolle: inz.kreisbahnen (eingefroren, J_iso) fuer dieselben 12 Bahnen
    t1 = time.time()
    quellen = {('bahn_' + nm): T for nm, m, T in bl}
    kb = inz.kreisbahnen(mod, Q, quellen, nd, wd)
    out['kontrolle_inz_kreisbahnen'] = {nm: kb['bahn_' + nm]['voll']['dyn_J_iso'] for nm, _, _ in bl}
    out['kontrolle_inz_gegen_exakt_max'] = float(np.abs(np.array([kb['bahn_' + nm]['voll']['dyn_J_iso'] for nm, _, _ in bl]) - G_ex).max())
    out['t_kreisbahnen'] = time.time() - t1
    out['zeiten_s'] = {'gesamt': time.time() - t0}
    return out


def suche(fam_wahl):
    """Schritt 3: Gewichte F1 und F2; Hodge-Punkte (Zusatz der Leitung 09:2x); Stabilitaet."""
    t0 = time.time()
    ende = t0 + 520
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = ni.Q_map(mod, tder)
    P = alles_vorbereiten(mod, Q)
    wd = P['wd']
    bl = bahnen()
    m4 = np.array([float((m ** 4).sum()) for _, m, _ in bl])
    out = {'fam': fam_wahl, 't_vorbereitung': time.time() - t0, 'volumen_je_art': volumen_je_art(mod)}
    if fam_wahl == 'F1':
        out['J_iso'] = messen(W_ISO, P, wd, bl, m4)
        # Zusatz der Leitung 09:2x: Hodge-Masse (beschreibend)
        vol = {a: v[0] for a, v in out['volumen_je_art'].items()}
        w_V = np.array([vol[a] / vol['finn_auf'] for a in ARTEN])
        out['hodge_J_prop_V'] = messen(w_V, P, wd, bl, m4)
        out['hodge_J_prop_1_durch_V'] = messen(1.0 / w_V, P, wd, bl, m4)
    laeufe = []
    if fam_wahl == 'F1':
        # (a) Kurve dTT = 0 (Ast bei J_iso), parametrisiert durch x0 = log10 J(Kegel); x1 per Halbierung
        kurve = []
        x1g = np.linspace(-0.7, 0.3, 41)
        for x0 in (np.linspace(-2.0, -0.3, 18) if not RAUCH else [-1.2]):
            if time.time() > ende - 200:
                break
            vals = []
            for b_ in x1g:
                try:
                    vals.append(dtt_q(P['p2'], gewichte([x0, b_], 'F1'))[0])
                except np.linalg.LinAlgError:
                    vals.append(np.nan)
            for i in range(len(x1g) - 1):
                if np.isfinite(vals[i]) and np.isfinite(vals[i + 1]) and vals[i] * vals[i + 1] < 0:
                    lo_, hi_, flo = x1g[i], x1g[i + 1], vals[i]
                    for _ in range(50):
                        mid = 0.5 * (lo_ + hi_)
                        fm = dtt_q(P['p2'], gewichte([x0, mid], 'F1'))[0]
                        if fm * flo < 0:
                            hi_ = mid
                        else:
                            lo_, flo = mid, fm
                    x1 = 0.5 * (lo_ + hi_)
                    d, q, off = dtt_q(P['p2'], gewichte([x0, x1], 'F1'))
                    kurve.append({'x': [float(x0), float(x1)], 'dTT': d, 'Q': q, 'off110': off,
                                  'messung': messen(gewichte([x0, x1], 'F1'), P, wd, bl, m4)})
        out['kurve_dTT0'] = kurve
        starts = [('kompakt', X_ISO_F1)]
    else:
        # (a) Ableitungen bei J_iso nach den 5 log-Gewichten (zentral, h = 1e-4)
        xi = np.array([0.0, pn.XK, pn.XK, pn.XS, pn.XS])
        jac = []
        for i in range(5):
            e = np.zeros(5)
            e[i] = 1e-4
            vp = dtt_q(P['p2'], gewichte(xi + e, 'F2')) + (gang_null(P['p200'], gewichte(xi + e, 'F2'), wd, bl, m4)[0]['gang'],)
            vm = dtt_q(P['p2'], gewichte(xi - e, 'F2')) + (gang_null(P['p200'], gewichte(xi - e, 'F2'), wd, bl, m4)[0]['gang'],)
            jac.append([(a_ - b_) / 2e-4 for a_, b_ in zip(vp, vm)])
        out['ableitung_J_iso'] = {'zeilen_x': ['finn_ab', 'kegel_T1', 'kegel_T2', 'sechs_T1', 'sechs_T2'],
                                  'spalten': ['dTT', 'Q', 'off110', 'gang0'], 'werte': jac}
        starts = [('kompakt', xi), ('kompakt', np.log10([0.829, 9.78, 99.8, 31.9, 0.049])),
                  ('kompakt', xi + np.random.default_rng(5).uniform(-0.2, 0.2, 5))]
    for art, x0 in (starts if not RAUCH else starts[:1]):
        if time.time() > ende - 90:
            laeufe.append({'art': art, 'fam': fam_wahl, 'abbruch': 'zeit vor Start'})
            continue
        t1 = time.time()
        z = Ziel(fam_wahl, art, P['p13'], P['p200'], P['peps'], P['pkl'], wd, bl, m4, p2=P['p2'])
        x, r, hist = lm(z, x0, maxit=(25 if not RAUCH else 1), zeit=min(ende - 60, time.time() + 150))
        w = gewichte(x, fam_wahl)
        verlauf = []
        for h_ in hist:
            if 'x' in h_:
                wi = gewichte(h_['x'], fam_wahl)
                try:
                    tsp = tt_null(P['p13'], wi)['spanne0']
                    gg = gang_null(P['p200'], wi, wd, bl, m4)[0]['gang']
                except np.linalg.LinAlgError:
                    tsp, gg = None, None
                verlauf.append({'it': h_['it'], 'F': h_['F'], 'tt_spanne0': tsp, 'gang0': gg, 'x': h_['x']})
        laeufe.append({'art': art, 'fam': fam_wahl, 'x0': np.asarray(x0).tolist(), 'x': x.tolist(), 'w': w.tolist(),
                       'am_rand': bool(np.any(np.abs(np.abs(x) - 2.0) < 1e-9)), 'messung': messen(w, P, wd, bl, m4),
                       'rest': r.tolist(), 'verlauf': verlauf, 'n_eval': z.n_eval, 't': time.time() - t1})
    out['laeufe'] = laeufe
    # Stabilitaet (511 k) fuer J_iso und die Endpunkte
    stab = {'J_iso': stabil(mod, W_ISO)} if fam_wahl == 'F1' else {}
    for i, l_ in enumerate(laeufe):
        if 'w' in l_ and time.time() < ende:
            stab['lauf%d' % i] = stabil(mod, np.array(l_['w']))
    if fam_wahl == 'F1' and out.get('kurve_dTT0') and time.time() < ende:
        kk = out['kurve_dTT0']
        b = min(range(len(kk)), key=lambda i: kk[i]['messung']['tt_spanne_ttiso'] if kk[i]['messung'].get('ok') else np.inf)
        if kk[b]['messung'].get('ok'):
            out['kurve_bester_index'] = b
            stab['kurve_bester'] = stabil(mod, gewichte(kk[b]['x'], 'F1'))
    out['stabil'] = stab
    out['zeiten_s'] = {'gesamt': time.time() - t0}
    return out


def karte(n0=31, n1=31):
    """F1-Karte (beschreibend, fuer das Bild): TT-Spanne langwellig und Gang (kl = 0,01) ueber (log10 Kegel, log10 Sechseck)."""
    t0 = time.time()
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = ni.Q_map(mod, tder)
    nm13, n13 = richtungen13()
    p13 = [vorbereiten(mod, Q, n13, s, spannung=False) for s in S0_LISTE]
    nd, wd = pn.richtungen(10, 20)
    pkl = vorbereiten(mod, Q, nd, KL_GANG / LP)
    bl = bahnen()
    m4 = np.array([float((m ** 4).sum()) for _, m, _ in bl])
    x0s = np.linspace(-2.0, 1.0, n0)
    x1s = np.linspace(-1.5, 1.5, n1)
    TT = np.full((n0, n1), np.nan)
    GA = np.full((n0, n1), np.nan)
    for i, a_ in enumerate(x0s):
        for j, b_ in enumerate(x1s):
            if time.time() - t0 > 540:
                break
            w = gewichte([a_, b_], 'F1')
            try:
                TT[i, j] = tt_null(p13, w)['spanne0']
                GA[i, j] = gang_kl(pkl, w, wd, bl, m4)[0]['gang']
            except np.linalg.LinAlgError:
                pass
    return {'x_kegel': x0s.tolist(), 'x_sechs': x1s.tolist(), 'tt_spanne0': TT.tolist(), 'gang_kl001': GA.tolist(),
            'zeiten_s': {'gesamt': time.time() - t0}}


# ------------------------------------------------------------------------------------------------ Urteile (PLAN Abschnitt 5)
def suche_lesen(p_su):
    """Mehrere Suchdateien (F1, F2) zusammenfuehren; Laeufe und Stabilitaet mit Familienpraefix."""
    su = {'laeufe': [], 'stabil': {}}
    for p in p_su:
        with open(p) as f:
            s_ = json.load(f)['suche']
        for i, l_ in enumerate(s_['laeufe']):
            l_ = dict(l_)
            l_['schluessel'] = '%s_lauf%d' % (s_['fam'], i)
            su['laeufe'].append(l_)
            if 'lauf%d' % i in s_['stabil']:
                su['stabil'][l_['schluessel']] = s_['stabil']['lauf%d' % i]
        for k_ in ('J_iso', 'hodge_J_prop_V', 'hodge_J_prop_1_durch_V', 'volumen_je_art', 'kurve_dTT0', 'kurve_bester_index',
                   'ableitung_J_iso'):
            if k_ in s_:
                su[k_] = s_[k_]
        for k_ in ('J_iso', 'kurve_bester'):
            if k_ in s_['stabil']:
                su['stabil'][k_] = s_['stabil'][k_]
    return su


def urteil(p_tab, p_su):
    with open(p_tab) as f:
        tb = json.load(f)['tabelle']
    su = suche_lesen(p_su)
    E_ = lambda b: 'eingetroffen' if b else 'verfehlt'
    u = {}
    gW = tb['gang']['W2_formel']['gang']
    kontrolle_ok = tb['abw']['exakt_neu_gegen_P_max'] <= 1e-9
    wort = abs(gW / GANG_P - 1) <= 0.10
    plan = wort and tb['abw']['W2_formel_gegen_P_max'] <= 0.1 * GANG_P * (2.0 / 3.0)
    u['SM1'] = {'kartenwortlaut': E_(wort), 'plan': (E_(plan) if kontrolle_ok else 'nicht entscheidbar (Kontrolle)'),
                'gang_W2': gW, 'rel_abw': gW / GANG_P - 1, 'kappa': tb['zusammenfassung']['kappa'],
                'W2_gegen_P_max': tb['abw']['W2_formel_gegen_P_max'], 'kontrolle_exakt_gegen_P': tb['abw']['exakt_neu_gegen_P_max']}
    kand = [('J_iso', su['J_iso'], su['stabil'].get('J_iso'))]
    for l_ in su['laeufe']:
        if 'messung' in l_:
            kand.append(('%s_%s' % (l_['schluessel'], l_['art']), l_['messung'], su['stabil'].get(l_['schluessel'])))
    for nm in ('hodge_J_prop_V', 'hodge_J_prop_1_durch_V'):
        kand.append((nm, su[nm], None))
    for i, z in enumerate(su.get('kurve_dTT0', [])):
        st = su['stabil'].get('kurve_bester') if i == su.get('kurve_bester_index') else None
        kand.append(('F1_kurve%d' % i, z['messung'], st))
    sm2w, sm2p, sm3w, sm3p = [], [], [], []
    for nm, m, st in kand:
        if not m.get('ok'):
            continue
        stab_ok = bool(st and st['stabil'])
        if m['tt_spanne_ttiso'] < 1e-6 and abs(m['gang_kl001']) < 1e-5:
            sm2w.append(nm)
            if stab_ok and m['tt_spanne0'] < 1e-6 and abs(m['gang0']) < 1e-5:
                sm2p.append(nm)
        if m['tt_spanne0'] < 1e-12 and abs(m['gang0']) < 1e-12:
            sm3w.append(nm)
            if stab_ok:
                sm3p.append(nm)
    best = min((m for _, m, _ in kand if m.get('ok')), key=lambda m: max(m['tt_spanne0'], abs(m['gang0'])))
    u['SM2'] = {'kartenwortlaut': E_(bool(sm2w)), 'plan': E_(bool(sm2p)), 'treffer_wort': sm2w, 'treffer_plan': sm2p}
    u['SM3'] = {'kartenwortlaut': E_(bool(sm3w)), 'plan': E_(bool(sm3p)), 'treffer_wort': sm3w, 'treffer_plan': sm3p,
                'bester_max_tt0_gang0': max(best['tt_spanne0'], abs(best['gang0']))}
    u['kandidaten'] = {nm: dict({k_: m.get(k_) for k_ in ('w', 'tt_spanne_ttiso', 'tt_spanne0', 'gang_kl001', 'gang0', 'iso0',
                                                          'kappa_kl001', 'Kh0_spanne', 'Mh0_im_max', 'luecke_max')},
                                stabil=(st['stabil'] if st else None)) for nm, m, st in kand if m.get('ok')}
    return {'urteile': u, 'tabelle_sha256': sha(p_tab), 'suche_sha256': [sha(p) for p in p_su]}


def bild(p_tab, p_su, p_ka, pfad_bild):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with open(p_tab) as f:
        tb = json.load(f)['tabelle']
    su = suche_lesen(p_su)
    with open(p_ka) as f:
        ka = json.load(f)['karte']
    fig, ax = plt.subplots(1, 5, figsize=(27, 5.2))
    a4 = ax[4]
    ku = su.get('kurve_dTT0', [])
    if ku:
        xk = np.array([z['x'][0] for z in ku])
        for key, sty, lab in (('tt_spanne_ttiso', 'o-', 'TT-Spanne (TT-ISO-1-Def.)'), ('tt_spanne0', 's--', 'TT-Spanne langwellig'),
                              ('gang_kl001', '^-', '|Gang| kl = 0,01'), ('gang0', 'v--', '|Gang| langwellig')):
            a4.semilogy(xk, [abs(z['messung'].get(key, np.nan)) if z['messung'].get('ok') else np.nan for z in ku], sty, ms=4, label=lab)
        a4.axhline(1e-6, color='gray', ls=':', lw=0.8)
        a4.axhline(1e-5, color='gray', ls='-.', lw=0.8)
        a4.axvline(pn.XK, color='r', lw=0.8, label='J_iso')
        a4.set_xlabel('log10 J(Kegel)/J(Finn) auf der Kurve dTT = 0 (F1)')
        a4.set_ylabel('Betrag')
        a4.set_title('F1: entlang dTT = 0 (E- gleich T2-Masse)')
        a4.legend(fontsize=6.5)
    x0 = np.array(ka['x_kegel'])
    x1 = np.array(ka['x_sechs'])
    TT = np.array(ka['tt_spanne0'], float)
    GA = np.array(ka['gang_kl001'], float)
    a0 = ax[0]
    im = a0.pcolormesh(x1, x0, np.log10(np.abs(TT)), shading='nearest', cmap='viridis')
    fig.colorbar(im, ax=a0, label='log10 TT-Spanne (langwellig)')
    a0.contour(x1, x0, GA, levels=[0.0], colors='w', linewidths=1.5)
    a1 = ax[1]
    vm = np.nanmax(np.abs(GA))
    im = a1.pcolormesh(x1, x0, GA, shading='nearest', cmap='RdBu_r', vmin=-vm, vmax=vm)
    fig.colorbar(im, ax=a1, label='Bahnlagen-Gang (kl = 0,01)')
    a1.contour(x1, x0, GA, levels=[0.0], colors='k', linewidths=1.2)
    a1.contour(x1, x0, np.log10(np.abs(TT)), levels=[-6, -5, -4], colors='g', linewidths=0.8)
    for a_ in (a0, a1):
        a_.plot([pn.XS], [pn.XK], 'r*', ms=12, label='J_iso (TT-ISO-1)')
        for i, l_ in enumerate(su['laeufe']):
            if l_.get('fam') == 'F1' and 'x' in l_:
                xs = np.array([v['x'] for v in l_['verlauf']])
                a_.plot(xs[:, 1], xs[:, 0], 'o-', ms=3, label='F1-Suche %s' % l_['art'])
        if ku:
            a_.plot([z['x'][1] for z in ku], [z['x'][0] for z in ku], 'm.-', ms=4, label='Kurve dTT = 0')
        a_.set_xlabel('log10 J(Sechseck)/J(Finn)')
        a_.set_ylabel('log10 J(Kegel)/J(Finn)')
        a_.legend(fontsize=6)
    a0.set_title('F1 (Fd-3m): TT-Spanne langwellig; weiss: Gang = 0')
    a1.set_title('F1: Gang (kl = 0,01); schwarz: Gang = 0; gruen: TT 1e-6..1e-4')
    a2 = ax[2]
    for i, l_ in enumerate(su['laeufe']):
        if 'verlauf' not in l_:
            continue
        it = [v['it'] for v in l_['verlauf']]
        a2.semilogy(it, [max(abs(v['tt_spanne0'] or np.nan), 1e-17) for v in l_['verlauf']], 'o-', ms=3,
                    label='TT, %s %s' % (l_['fam'], l_['art']))
        gg = [(v['it'], abs(v['gang0'])) for v in l_['verlauf'] if v['gang0'] is not None]
        if gg:
            a2.semilogy([g_[0] for g_ in gg], [max(g_[1], 1e-17) for g_ in gg], 's--', ms=3, label='|Gang0|, %s %s' % (l_['fam'], l_['art']))
    a2.axhline(1e-6, color='gray', ls=':', lw=0.8)
    a2.axhline(1e-12, color='k', ls=':', lw=0.8)
    a2.set_xlabel('LM-Iteration')
    a2.set_ylabel('TT-Spanne bzw. |Gang| (langwellig)')
    a2.set_title('Suche: TT-Spanne und Gang gegen Iteration')
    a2.legend(fontsize=5.5)
    a3 = ax[3]
    m4 = np.array(tb['summe_m4'])
    o = np.argsort(m4)
    a3.plot(m4[o], np.array(tb['bahnen_G']['P'])[o], 'ko', label='IMPULS-NETZ-1 [P]')
    a3.plot(m4[o], np.array(tb['bahnen_G']['exakt_neu'])[o], 'c+', ms=10, label='neu (Tabelle, exakt)')
    a3.plot(m4[o], np.array(tb['bahnen_G']['W2_formel'])[o], 'r-', label='Winkelformel W2 (kappa aus Schritt 1)')
    a3.set_xlabel('Summe m_i^4 der Bahnnormale')
    a3.set_ylabel('G_rad/G (kl = 0,01, J_iso, mit J)')
    a3.set_title('Kreisbahnen: Winkelformel gegen Rechnung')
    a3.legend(fontsize=7)
    fig.suptitle('SKALAR-MISCH-1: Netz V, A1R1, mit Impulskopplung (synthetische Gitterrechnung, keine Messdaten)')
    fig.tight_layout()
    fig.savefig(pfad_bild + '.tmp.png', dpi=105)
    os.replace(pfad_bild + '.tmp.png', pfad_bild)
    return {'bild': pfad_bild}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'rauch2', 'rauch3', 'tabelle', 'suche', 'karte', 'urteil', 'bild'])
    ap.add_argument('--tabelle')
    ap.add_argument('--suche', nargs='+')
    ap.add_argument('--fam', default='F1', choices=['F1', 'F2'])
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--karte')
    ap.add_argument('--bild')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    global RAUCH
    RAUCH = a.rauch
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'inz_sha256': sha(os.path.abspath(inz.__file__)),
            'pn_sha256': sha(os.path.abspath(pn.__file__)), 'ew_sha256': sha(os.path.abspath(ew.__file__)),
            'ni_sha256': sha(os.path.abspath(ni.__file__)), 'tp_sha256': sha(os.path.abspath(ew.tp.__file__))}
    res = {'info': info}
    if a.modus == 'rauch3':
        res['rauch3'] = rauch3()
    elif a.modus == 'rauch2':
        res['rauch2'] = rauch2()
    elif a.modus == 'rauch':
        res['rauch'] = rauch()
    elif a.modus == 'tabelle':
        res['tabelle'] = tabelle()
    elif a.modus == 'suche':
        res['suche'] = suche(a.fam)
    elif a.modus == 'karte':
        res['karte'] = karte() if not a.rauch else karte(3, 3)
    elif a.modus == 'urteil':
        res['urteil'] = urteil(a.tabelle, a.suche)
    else:
        for p in [a.tabelle, a.karte] + a.suche:
            info['eingabe_sha256_' + os.path.basename(p)] = sha(p)
        res['bild'] = bild(a.tabelle, a.suche, a.karte, a.bild)
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.tolist() if hasattr(o, 'tolist') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], 'maxrss %.0f MB' % res['maxrss_MB'], flush=True)


if __name__ == '__main__':
    main()
