#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGIME-K-2 (fmhc-physics, Runde 49), Code-Agent fuer die Leitung claude-primary.

Linearisierte 4D-Regge-Wirkung S = Summe_t A_t eps_t auf Zeltstangen-Treppen ueber 3D-Netzen:
  KW, B1-t1  aus rk.py (REGIME-K-1, unveraendert importiert)
  V-A, V-B   Finns gefuelltes Netz V (ew.geometrie('V'), TT-ISO-1, unveraendert importiert), Hubfolge A bzw. umgekehrt
  S-A        Fuellung S (Achse C1-C2 durch jedes Sechseck), Hubfolge A
Modi:
  gitter      euklidische Bloch-Hesse, Eichabzug, Schur-Form, 92 Richtungen x 9 kl (rk.lauf_gitter, unveraendert)
  vorzeichen  Vorzeichenzaehlung von H_E = -Hesse(S): Brillouin-Zone 8^4 und die 828 Rasterpunkte
  welle       echte Zeit ueber komplexes k_tau (Laurent-Form in z = exp(i k_tau tau), Verfahren REGGE-WELLE-1:
              festes Komplement, Polynom-Eigenwertproblem, Aberth, Windungszahl; Funktionen aus
              regge-welle-1/code/regge_welle.py uebernommen und auf rk.Gitter angepasst)
  auswertung  Urteile RQ0 bis RQ4 und Pipeline-Kontrollen nach PLAN.md
"""
import argparse, json, sys, os, time, platform, hashlib, resource
import numpy as np
import scipy.linalg as sla

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import rk  # noqa: E402  (REGIME-K-1, unveraendert)
import ew  # noqa: E402  (TT-ISO-1 / EINE-WELT-LOCH-1, unveraendert)
import tp  # noqa: E402

TOL_NULL = rk.TOL_NULL
SEED = 20261005
BZ_N = 8
# echte Zeit (PLAN 5, wie REGGE-WELLE-1)
R_RE, R_IM = 3.0, 0.5
N_RAND_H, N_RAND_V = 1000, 200
PHASE_MAX = 0.5
RHO_MIN = 0.05
S_WURZEL = 1e-9
PHYS_MIN = 0.1
TRIM_REL = 1e-10
LAUF_IM = 1e-6
S_ECHT = 1e-8          # nach Rauchtest r1: komplementfreie Echtheitspruefung (s_voll)
ZENSUS_RE_MAX = 2.4
BATCH = 256


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def ohne_nan(x):
    return rk.ohne_nan(x)


# ================================================================================================= Netze
def netz_raum(fuellung):
    """Raeumliche Tetraeder von V bzw. S (ew.geometrie), Ecken als (Untergitter, Koeffizienten in a1..a3)."""
    pos8, zellen = ew.geometrie(fuellung)
    tets = [[ew.zerlege(x, pos8) for x in z['X8']] for z in zellen]
    arten = {}
    for z in zellen:
        arten[z['art']] = arten.get(z['art'], 0) + 1
    xb = [np.asarray(p, float) / 8.0 for p in pos8]
    return xb, tets, arten


def raum_info(tets):
    kanten, dreiecke, tetk = set(), set(), set()
    gleich = 0
    for T in tets:
        tetk.add(rk.kanon_menge(T))
        for i in range(4):
            for j in range(i + 1, 4):
                key, _ = rk.kanon_kante(T[i], T[j])
                if key not in kanten and key[0] == key[1]:
                    gleich += 1
                kanten.add(key)
            for j in range(i + 1, 4):
                for l in range(j + 1, 4):
                    dreiecke.add(rk.kanon_menge([T[i], T[j], T[l]]))
    return {'kanten': len(kanten), 'dreiecke': len(dreiecke), 'tetraeder': len(tetk),
            'kanten_im_untergitter': gleich}


def ord_rang(rang):
    def f(g, v):
        b, n = v
        x = g.xb[b] + g.A3 @ np.array(n, float)
        return (rang[b], x[0], x[1], x[2])
    return f


def baue2(arm):
    """Arme nach PLAN 2.3; tau = 1 fuer alle."""
    if arm == 'KW':
        g = rk.baue('KW', 1.0)
    elif arm == 'B1-t1':
        g = rk.baue('B1', 1.0)
    elif arm in ('V-A', 'V-B', 'S-A'):
        xb, tets, arten = netz_raum(arm[0])
        NV = len(xb)
        folge = list(range(NV)) if arm.endswith('A') else list(range(NV))[::-1]
        rang = {b: j for j, b in enumerate(folge)}
        hb = [rang[b] / float(NV) for b in range(NV)]
        g = rk.Gitter(arm, xb, hb, tp.AV.T, tets, ord_rang(rang), 1.0)
        info = raum_info(tets)
        info.update({'arten': arten, 'untergitter': NV, 'folge': folge, 'hoehen': hb,
                     'euler_raum': NV - info['kanten'] + info['dreiecke'] - info['tetraeder']})
        g.info_raum = info
    else:
        raise ValueError(arm)
    g.name = arm
    return g


def tote_idx(g):
    zeile = np.zeros(g.NE)
    for s in range(g.S):
        for i in range(10):
            e = g.egid[s, i]
            zeile[e] = max(zeile[e], float(np.abs(g.Hloc[s, i, :]).max()))
    hmax = float(np.abs(g.Hloc).max())
    return [int(e) for e in range(g.NE) if zeile[e] <= 1e-12 * hmax]


# ================================================================================================= Laurent-Form
class Laurent:
    """H(k)_ee' = Summe_m C_m(k_s) z^m, z = exp(i k_tau tau) (analytisch; fuer reelles k gleich rk.Gitter.H)."""

    def __init__(self, g):
        self.g = g
        ei = np.repeat(g.egid[:, :, None], 10, axis=2)
        ej = np.repeat(g.egid[:, None, :], 10, axis=1)
        nt = g.eT[:, :, 3]
        m = nt[:, None, :] - nt[:, :, None]
        Ts = g.Tphys[:, :, :3]
        dTs = Ts[:, None, :, :] - Ts[:, :, None, :]
        self.idx = (ei * g.NE + ej).ravel()
        self.m = m.ravel()
        self.dTs = dTs.reshape(-1, 3)
        self.w = g.Hloc.ravel()
        self.ms = sorted(set(int(x) for x in self.m))
        self.sel = {mm: self.m == mm for mm in self.ms}

    def koeff(self, ks):
        NE = self.g.NE
        ph = self.w * np.exp(1j * (self.dTs @ ks))
        C = {}
        for mm in self.ms:
            s = self.sel[mm]
            Cm = np.bincount(self.idx[s], ph[s].real, minlength=NE * NE) + \
                1j * np.bincount(self.idx[s], ph[s].imag, minlength=NE * NE)
            C[mm] = Cm.reshape(NE, NE)
        return C


def lauf_eval(Fm, w, tau, abl=False):
    """F(omega) = Summe_m F_m z^m, z = exp(-omega tau) (k_tau = i omega); dF/domega = Summe (-m tau) F_m z^m."""
    w = np.atleast_1d(np.asarray(w, complex))
    z = np.exp(-tau * w)
    n = next(iter(Fm.values())).shape[0]
    F = np.zeros((len(z), n, n), complex)
    dF = np.zeros((len(z), n, n), complex) if abl else None
    for m, Cm in Fm.items():
        zm = z ** m
        F += zm[:, None, None] * Cm[None]
        if abl:
            dF += (-m * tau) * zm[:, None, None] * Cm[None]
    return (F, dF) if abl else F


def G_batch(g, K):
    """rk.Gitter.G fuer viele (auch komplexe) k: (B, NE, 4 NV)."""
    K = np.atleast_2d(np.asarray(K, complex))
    B = K.shape[0]
    Gk = np.zeros((B, g.NE, 4 * g.NV), complex)
    ph = np.exp(1j * (K @ g.Rd.T))
    e = np.arange(g.NE)[:, None]
    c4 = np.arange(4)[None, :]
    Gk[:, e, 4 * g.b2[:, None] + c4] += g.u[None, :, :] * ph[:, :, None]
    Gk[:, e, 4 * g.b1[:, None] + c4] -= g.u[None, :, :]
    return Gk


def nullbasis(g, K, tot):
    N = G_batch(g, K)
    if tot:
        E = np.zeros((N.shape[0], g.NE, len(tot)), complex)
        for j, e in enumerate(tot):
            E[:, e, j] = 1.0
        N = np.concatenate([N, E], axis=2)
    return N


def orth_bild(N):
    """Orthonormalbasis von range N je Batch (Rang ueber Singulaerwerte > 1e-10 s_max)."""
    U, s, _ = np.linalg.svd(N, full_matrices=False)
    r = int((s[0] > 1e-10 * s[0, 0]).sum())
    return U[:, :, :r], r


def rho_wert(Qn0, N):
    Qn, _ = orth_bild(N)
    M = np.einsum('ai,kaj->kij', Qn0.conj(), Qn)
    return np.linalg.svd(M, compute_uv=False)[:, -1]


def pep_wurzeln(Fm, tau):
    """aus regge_welle.py (REGGE-WELLE-1), angepasst: z = exp(i k_tau tau), omega = -log(z)/tau."""
    mx = max(np.max(np.abs(v)) for v in Fm.values())
    behalten = {m: v for m, v in Fm.items() if np.max(np.abs(v)) > TRIM_REL * mx}
    weg = max([float(np.max(np.abs(v))) / mx for m, v in Fm.items() if m not in behalten] + [0.0])
    ms = sorted(behalten)
    m0, D = ms[0], ms[-1] - ms[0]
    n = next(iter(Fm.values())).shape[0]
    P = [behalten.get(m0 + j, np.zeros((n, n), complex)) for j in range(D + 1)]
    A = np.zeros((n * D, n * D), complex)
    B = np.eye(n * D, dtype=complex)
    if D > 1:
        A[:n * (D - 1), n:] = np.eye(n * (D - 1))
    for j in range(D):
        A[n * (D - 1):, n * j:n * (j + 1)] = -P[j]
    B[n * (D - 1):, n * (D - 1):] = P[D]
    al, be = sla.eig(A, B, right=False, homogeneous_eigvals=True)
    ok = (np.abs(be) > 1e-13 * np.abs(al)) & (np.abs(al) > 1e-300)
    zz = al[ok] / be[ok]
    zz = zz[np.abs(zz) > 1e-300]
    return -np.log(zz) / tau, {'m_bereich': [int(m0), int(ms[-1])], 'grad': int(D), 'weggelassen_rel_max': weg,
                               'eigenwerte_endlich': int(len(zz)), 'eigenwerte_gesamt': int(n * D)}


def logabl(Fm, w, tau):
    F, dF = lauf_eval(Fm, w, tau, abl=True)
    return np.trace(np.linalg.solve(F, dF), axis1=1, axis2=2)


def aberth(Fm, w0, tau, skala, maxit=80):
    """aus regge_welle.py (REGGE-WELLE-1), mit tau."""
    w = np.array(w0, complex)
    schritt = np.inf
    it = -1
    for it in range(maxit):
        L = logabl(Fm, w, tau)
        diff = w[:, None] - w[None, :]
        np.fill_diagonal(diff, np.inf)
        S = np.sum(1.0 / diff, axis=1)
        st = 1.0 / (L - S)
        w = w - st
        schritt = float(np.max(np.abs(st)))
        if schritt < 1e-14 * skala:
            break
    return w, it + 1, schritt


def s_wert(Fm, w, tau):
    out = []
    w = np.atleast_1d(w)
    for a in range(0, len(w), BATCH):
        F = lauf_eval(Fm, w[a:a + BATCH], tau)
        sv = np.linalg.svd(F, compute_uv=False)
        out.append(sv[:, -1] / sv[:, 0])
    return np.concatenate(out) if out else np.array([])


def randpunkte(kb, faktor):
    nh, nv = N_RAND_H * faktor, N_RAND_V * faktor
    a, b, h = 0.0, R_RE * kb, R_IM * kb
    unten = np.linspace(a, b, nh, endpoint=False) - 1j * h
    rechts = b + 1j * np.linspace(-h, h, nv, endpoint=False)
    oben = np.linspace(b, a, nh, endpoint=False) + 1j * h
    links = a + 1j * np.linspace(h, -h, nv, endpoint=False)
    p = np.concatenate([unten, rechts, oben, links])
    return np.concatenate([p, p[:1]])


def windung(Fm, kb, tau):
    for faktor in (1, 2, 4):
        p = randpunkte(kb, faktor)
        ph = []
        for a in range(0, len(p), BATCH):
            F = lauf_eval(Fm, p[a:a + BATCH], tau)
            sgn, _ = np.linalg.slogdet(F)
            ph.append(np.angle(sgn))
        ph = np.concatenate(ph)
        dph = np.angle(np.exp(1j * np.diff(ph)))
        mx = float(np.max(np.abs(dph)))
        w = float(np.sum(dph) / (2 * np.pi))
        if mx < PHASE_MAX:
            break
    return {'windung': w, 'zahl': int(round(w)), 'rest': abs(w - round(w)), 'max_phasensprung': mx,
            'faktor': faktor, 'punkte': int(len(p))}, p


def s_voll(C, w, tau, r):
    """Komplementfreie Echtheitspruefung (nach Rauchtest r1): (r+1)-kleinster Singulaerwert der vollen H(k_s, i omega)
    relativ zum groessten; r = Rang der Nullbasis (Eichung + tote Kanten). Echte Nullstelle: ~0."""
    z = np.exp(-tau * complex(w))
    H = sum(Cm * z ** m for m, Cm in C.items())
    sv = np.linalg.svd(H, compute_uv=False)
    return float(sv[len(sv) - r - 1] / sv[0])


def tt_kanten(g, ks_hat, k4):
    """Kantenbild der Kontinuums-TT-Moden h_+, h_x (raeumlich, transversal zu n, spurfrei) ueber P(k) (analytisch)."""
    U, _, _ = np.linalg.svd(np.outer(ks_hat, ks_hat))
    Ea = np.r_[U[:, 1], 0.0]
    Eb = np.r_[U[:, 2], 0.0]
    hp = (np.outer(Ea, Ea) - np.outer(Eb, Eb)) / np.sqrt(2)
    hx = (np.outer(Ea, Eb) + np.outer(Eb, Ea)) / np.sqrt(2)
    a = np.array([np.einsum('aij,ij->a', rk.SB, h) for h in (hp, hx)]).T
    Pk = g.P0 * np.exp(1j * (g.mid @ k4))[:, None]
    QT, _ = np.linalg.qr(Pk @ a)
    return QT


def tt_klasse(u, Nw, QT):
    R = np.eye(len(u)) - QT @ QT.conj().T
    c, *_ = np.linalg.lstsq(R @ Nw, -(R @ u), rcond=None)
    w = u + Nw @ c
    return float(np.linalg.norm(QT.conj().T @ w) / np.linalg.norm(w))


def richtungen_rw24():
    """24 raeumliche Richtungen aus REGGE-WELLE-1 (regge_welle.richtungen, unveraendert uebernommen)."""
    roh = [("x+", (1, 0, 0)), ("x-", (-1, 0, 0)), ("xy+", (1, 1, 0)), ("xy-", (-1, -1, 0)), ("x-y", (1, -1, 0)),
           ("xyz+", (1, 1, 1)), ("xyz-", (-1, -1, -1)), ("xy-z", (1, 1, -1)), ("-x-yz", (-1, -1, 1)),
           ("123", (1, 2, 3)), ("312", (3, 1, 2)), ("-1-2-3", (-1, -2, -3))]
    ga = np.pi * (3.0 - np.sqrt(5.0))
    for i in range(12):
        zz = 1.0 - (2.0 * i + 1.0) / 12.0
        r = np.sqrt(1.0 - zz * zz)
        roh.append((f"fib{i:02d}", (r * np.cos(i * ga), r * np.sin(i * ga), zz)))
    return [(nm, np.array(v, float) / np.linalg.norm(v)) for nm, v in roh]


def richtungen_rk25():
    D, nm = rk.richtungen()
    return [('rk_' + n, d[:3] / np.linalg.norm(d[:3])) for d, n in zip(D, nm) if abs(d[3]) < 1e-12]


def welle_punkt(g, lau, tot, nm, nhat, kb):
    t0 = time.time()
    tau = g.tau
    ks = kb * nhat
    C = lau.koeff(ks)
    N0 = nullbasis(g, np.r_[ks, 0.0][None, :], tot)[0]
    U, sv0, _ = np.linalg.svd(N0, full_matrices=True)
    r0 = int((sv0 > 1e-10 * sv0[0]).sum())
    Qn0, Q0 = U[:, :r0], U[:, r0:]
    Fm = {m: Q0.conj().T @ Cm @ Q0 for m, Cm in C.items()}
    out = {'richtung': nm, 'n': nhat.tolist(), 'betrag': kb, 'rang_N0': r0, 'dim_F': int(Q0.shape[1]),
           'N0_sing_rel_min': float(sv0[r0 - 1] / sv0[0])}
    wurz, pinfo = pep_wurzeln(Fm, tau)
    out['pep'] = pinfo
    inR2 = (wurz.real >= -0.2 * kb) & (wurz.real <= 1.2 * R_RE * kb) & (np.abs(wurz.imag) <= 1.2 * R_IM * kb)
    kand = wurz[inR2]
    if len(kand):
        verf, nit, letzter = aberth(Fm, kand, tau, kb)
    else:
        verf, nit, letzter = kand, 0, 0.0
    out['aberth'] = {'iterationen': int(nit), 'letzter_schritt': float(letzter), 'kandidaten': int(len(kand)),
                     'max_verschiebung_rel': float(np.max(np.abs(verf - kand)) / kb) if len(kand) else 0.0}
    inR = (verf.real > 0) & (verf.real <= R_RE * kb) & (np.abs(verf.imag) <= R_IM * kb)
    wR = verf[inR]
    wR = wR[np.argsort(wR.real)]
    sR = s_wert(Fm, wR, tau) if len(wR) else np.array([])
    wd, p = windung(Fm, kb, tau)
    rho_rand = np.concatenate([rho_wert(Qn0, nullbasis(g, np.c_[np.tile(ks, (len(p[a:a + BATCH]), 1)),
                                                               1j * p[a:a + BATCH]], tot))
                               for a in range(0, len(p), BATCH)])
    wd['rho_rand_min'] = float(np.min(rho_rand))
    out['windung'] = wd
    nst = []
    for w, sw in zip(wR, sR):
        Fw = lauf_eval(Fm, [w], tau)[0]
        _, svw, Vh = np.linalg.svd(Fw)
        v = np.conj(Vh[-1])
        u = Q0 @ v
        k4 = np.r_[ks, 1j * w]
        Nw = nullbasis(g, k4[None, :], tot)[0]
        Qn, _ = orth_bild(Nw[None])
        Qn = Qn[0]
        phys = float(np.linalg.norm(u - Qn @ (Qn.conj().T @ u)) / np.linalg.norm(u))
        QT = tt_kanten(g, nhat, k4)
        tt = tt_klasse(u, Nw, QT)
        tt2 = tt_klasse(Q0 @ np.conj(Vh[-2]), Nw, QT)
        nst.append({'re': float(w.real), 'im': float(w.imag), 'v_re': float(w.real / kb), 'v_im': float(w.imag / kb),
                    's': float(sw), 's2_rel': float(svw[-2] / svw[0]), 'rho': float(rho_wert(Qn0, Nw[None])[0]),
                    'physikalisch': phys, 'tt_anteil': tt, 'tt_anteil_2': tt2, 's_voll': s_voll(C, w, tau, r0)})
    out['nullstellen'] = nst
    # Sperren (PLAN 6, wie REGGE-WELLE-1 [F7])
    sp = []
    if wd['rest'] > 0.05 or wd['max_phasensprung'] >= PHASE_MAX:
        sp.append('windung')
    if wd['zahl'] != len(nst):
        sp.append('windung_ne_nullstellen')
    if any(x['s'] > S_WURZEL for x in nst):
        sp.append('s')
    if any(x['rho'] < RHO_MIN or x['physikalisch'] < PHYS_MIN for x in nst):
        sp.append('rho_phys')
    if wd['rho_rand_min'] < RHO_MIN:
        sp.append('rho_rand')
    if any(x['s_voll'] > S_ECHT for x in nst):
        sp.append('unecht')
    out['sperren'] = sp
    out['erfuellt'] = bool(len(nst) == 2 and wd['zahl'] == 2 and all(abs(x['v_im']) <= LAUF_IM for x in nst))
    # Zensus light (beschreibend)
    zz = wurz[(wurz.real > 0) & (wurz.real <= ZENSUS_RE_MAX) & ~((wurz.real <= R_RE * kb) & (np.abs(wurz.imag) <= R_IM * kb))]
    zen = {'zahl': int(len(zz))}
    if len(zz):
        szz = s_wert(Fm, zz, tau)
        Nz = nullbasis(g, np.c_[np.tile(ks, (len(zz), 1)), 1j * zz], tot)
        rz = rho_wert(Qn0, Nz)
        ph = []
        for w in zz:
            Fw = lauf_eval(Fm, [w], tau)[0]
            _, _, Vh = np.linalg.svd(Fw)
            u = Q0 @ np.conj(Vh[-1])
            Nw = nullbasis(g, np.r_[ks, 1j * w][None, :], tot)
            Qn, _ = orth_bild(Nw)
            Qn = Qn[0]
            ph.append(float(np.linalg.norm(u - Qn @ (Qn.conj().T @ u)) / np.linalg.norm(u)))
        ph = np.array(ph)
        sv_ = np.array([s_voll(C, w, tau, r0) for w in zz])
        alt = (szz <= S_WURZEL) & (rz >= RHO_MIN) & (ph >= PHYS_MIN)
        intr = (szz <= S_WURZEL) & (sv_ <= S_ECHT)
        zen.update({'rho_phys_kriterium': int(alt.sum()), 'intrinsisch': int(intr.sum()),
                    'intrinsisch_nicht_reell': int((intr & (np.abs(zz.imag) > LAUF_IM * kb)).sum()),
                    'intrinsisch_liste': [[float(x.real), float(x.imag)] for x in zz[intr]][:40],
                    's_voll_min_ausserhalb': float(sv_.min())})
    out['zensus_light'] = zen
    out['laufzeit_s'] = time.time() - t0
    return out


def w0_kontrollen(g, lau, tot, rng):
    abw, res = [], []
    for _ in range(64):
        k = rng.uniform(-np.pi, np.pi, size=4)
        C = lau.koeff(k[:3])
        z = np.exp(1j * k[3] * g.tau)
        M = sum(Cm * z ** m for m, Cm in C.items())
        Hr = g.H(k)
        abw.append(float(np.abs(M - Hr).max() / np.abs(Hr).max()))
    for _ in range(64):
        ks = rng.uniform(-np.pi, np.pi, size=3)
        kt = rng.uniform(-np.pi, np.pi) + 1j * rng.uniform(-2.4, 2.4)
        C = lau.koeff(ks)
        z = np.exp(1j * kt * g.tau)
        M = sum(Cm * z ** m for m, Cm in C.items())
        N = nullbasis(g, np.r_[ks, kt][None, :], tot)[0]
        r = np.max(np.linalg.norm(M @ N, axis=0) / np.linalg.norm(N, axis=0)) / np.linalg.norm(M, 2)
        res.append(float(r))
    return {'a_max': max(abw), 'b_max': max(res), 'a_punkte': len(abw), 'b_punkte': len(res)}


def lauf_welle(g, betraege, lesart, rliste, rauch=False):
    t0 = time.time()
    lau = Laurent(g)
    tot = tote_idx(g)
    rng = np.random.default_rng(SEED)
    out = {'gitter': g.name, 'tau': g.tau, 'lmean': g.lmean, 'NE': g.NE, 'NV': g.NV, 'tote_kanten_idx': tot,
           'laurent_m': lau.ms, 'lesart': lesart, 'betraege_eingabe': betraege}
    out['w0'] = w0_kontrollen(g, lau, tot, rng)
    R = []
    if rliste in ('rw24', 'beide'):
        R += richtungen_rw24()
    if rliste in ('rk25', 'beide'):
        R += richtungen_rk25()
    if rauch:
        R = [r for r in R if r[0] in ('x+', 'xyz+', 'fib05')]
    pkt = []
    for x in betraege:
        kb = x / g.lmean if lesart == 'kl' else x
        for nm, nh in R:
            a = welle_punkt(g, lau, tot, nm, nh, kb)
            a['eingabe'] = x
            if g.name == 'KW':
                a['v_hyperkubisch'] = float(2 * np.arcsinh(np.sqrt(np.sum(np.sin(kb * nh / 2) ** 2))) / kb)
            pkt.append(a)
            print('%s %s |k|=%.4g: Windung %.3f, NS %d, %.1f s' % (g.name, nm, kb, a['windung']['windung'],
                                                                 len(a['nullstellen']), a['laufzeit_s']), flush=True)
    out['punkte'] = pkt
    out['t_gesamt_s'] = time.time() - t0
    return out


# ================================================================================================= Vorzeichen
def zaehle(g, k):
    Hk = g.H(k)
    Hk = 0.5 * (Hk + Hk.conj().T)
    lam = -np.linalg.eigvalsh(Hk)              # H_E = -Hesse(S)
    a = np.abs(lam)
    mx = float(a.max())
    nul = a <= TOL_NULL * mx
    sg = np.linalg.svd(g.G(k), compute_uv=False)
    rG = int((sg > 1e-10 * sg[0]).sum()) if sg[0] > 0 else 0
    nz = a[~nul]
    return {'null': int(nul.sum()), 'pos': int(((lam > 0) & ~nul).sum()), 'neg': int(((lam < 0) & ~nul).sum()),
            'rG': rG, 'min_nichtnull_rel': float(nz.min() / mx) if nz.size else None,
            'min_neg_rel': float(lam[(lam < 0) & ~nul].max() / mx) if ((lam < 0) & ~nul).any() else None}


def lauf_vorzeichen(g, rauch=False):
    t0 = time.time()
    nb = 2 if rauch else BZ_N
    Ainv = np.linalg.inv(g.A)
    bz = []
    import itertools
    for m in itertools.product(range(nb), repeat=4):
        k = 2 * np.pi * Ainv.T @ (np.array(m, float) / nb)
        z = zaehle(g, k)
        z['m'] = list(m)
        bz.append(z)
    D, nm = rk.richtungen()
    if rauch:
        D = D[[0, 3, 4, 20, 40, 80]]
        nm = [nm[i] for i in (0, 3, 4, 20, 40, 80)]
    ras = []
    for di, d in enumerate(D):
        for x in rk.KL_RASTER:
            z = zaehle(g, (x / g.lmean) * d)
            z['richtung'] = nm[di]
            z['kl'] = x
            ras.append(z)

    def vert(L, key):
        out = {}
        for z in L:
            out[str(z[key])] = out.get(str(z[key]), 0) + 1
        return out
    bz0 = [z for z in bz if not any(z['m'])]
    bzn = [z for z in bz if any(z['m'])]
    sig = {}
    for z in bzn:
        s = '%d/%d/%d' % (z['null'], z['pos'], z['neg'])
        sig[s] = sig.get(s, 0) + 1
    sig_r = {}
    for z in ras:
        s = '%d/%d/%d' % (z['null'], z['pos'], z['neg'])
        sig_r[s] = sig_r.get(s, 0) + 1
    out = {'gitter': g.name, 'NE': g.NE, 'NV': g.NV, 'bz_n': nb, 'q0': bz0[0],
           'bz_signaturen': sig, 'bz_neg': vert(bzn, 'neg'), 'bz_null': vert(bzn, 'null'), 'bz_rG': vert(bzn, 'rG'),
           'bz_min_nichtnull_rel': float(min(z['min_nichtnull_rel'] for z in bzn)),
           'raster_signaturen': sig_r, 'raster_neg': vert(ras, 'neg'), 'raster_null': vert(ras, 'null'),
           'raster_rG': vert(ras, 'rG'), 'zahl_bz': len(bzn), 'zahl_raster': len(ras),
           'bz_punkte': bz, 'raster_punkte': ras, 't_gesamt_s': time.time() - t0}
    return out


# ================================================================================================= Auswertung
def kennz2(J, art):
    k = rk.kennzahlen(J, art)
    sp = J['spektren']
    tt = np.array(sp['tt_' + art])
    konf = np.array(sp['konf_' + art])
    kl = J['kl']
    ND = tt.shape[0]
    jf = [kl.index(x) for x in rk.KL_FIT]
    ger = art != 'voll'
    Y = tt[:, jf, :].transpose(0, 2, 1).reshape(-1, len(jf))
    w0 = rk.w0_fit(rk.KL_FIT, Y, ger)[0].reshape(ND, 5)
    c0 = rk.w0_fit(rk.KL_FIT, konf[:, jf], ger)[0]
    r = c0 / w0.mean(1)
    k['r_je_richtung_min'] = float(r.min())
    k['r_je_richtung_max'] = float(r.max())
    k['r_abw_max'] = float(np.max(np.abs(r + 2)))
    return k


def nullmoden(J):
    sp = J['spektren']
    n0 = np.array(sp['n0'], float)
    lu = np.array(sp['luecke'], float)
    sn = np.array(sp['sin_null_eich'], float)
    return {'n0_min': int(n0.min()), 'n0_max': int(n0.max()),
            'luecke_min': float(np.nanmin(lu)) if np.isfinite(lu).any() else None,
            'HG_max': float(np.max(sp['HG'])), 'rG_min': int(np.min(sp['rG'])), 'rG_max': int(np.max(sp['rG'])),
            'sin_max': float(np.nanmax(sn)) if np.isfinite(sn).any() else None,
            'herm_max': float(np.max(sp['herm'])), 'im_rel_max': float(np.max(sp['im_rel'])),
            'hart_min': float(np.nanmin(np.array(sp['hart'], float))), 'ncc_null_max': int(np.max(sp['ncc_null'])),
            'tt_gerade_max': float(np.max(sp['tt_gerade'])), 'tt_gerade_min': float(np.min(sp['tt_gerade'])),
            'konf_gerade_min': float(np.min(sp['konf_gerade'])), 'konf_gerade_max': float(np.max(sp['konf_gerade'])),
            'k0_n0': J['k0']['n0'], 'fehlwinkel_max_abs': J['kontrollen']['fehlwinkel_max_abs'],
            'tote_kanten': J['kontrollen']['tote_kanten'], 'zahl_k': int(n0.size)}


def welle_urteil(W, vmin, vmax):
    """Dreiwertig (PLAN 6): Verstoss an ungesperrtem Punkt -> nicht eingetroffen; sonst gesperrt -> nicht auswertbar."""
    verstoss, gesperrt, v_alle, im_max = [], [], [], 0.0
    for p in W['punkte']:
        ok = p['erfuellt'] and all(vmin <= x['v_re'] <= vmax for x in p['nullstellen'])
        for x in p['nullstellen']:
            v_alle.append(x['v_re'])
            im_max = max(im_max, abs(x['v_im']))
        if p['sperren']:
            gesperrt.append(p['richtung'])
        elif not ok:
            verstoss.append(p['richtung'])
    if verstoss:
        u = 'nicht eingetroffen'
    elif gesperrt:
        u = 'nicht auswertbar'
    else:
        u = 'eingetroffen'
    nz = [len(p['nullstellen']) for p in W['punkte']]
    wz = [p['windung']['zahl'] for p in W['punkte']]
    return {'urteil': u, 'verstoss': verstoss, 'gesperrt': gesperrt, 'punkte': len(W['punkte']),
            'v_min': min(v_alle) if v_alle else None, 'v_max': max(v_alle) if v_alle else None,
            'abs_im_rel_max': im_max, 'nullstellen_je_punkt': sorted(set(nz)), 'windung_je_punkt': sorted(set(wz)),
            'betrag': W['punkte'][0]['betrag'] if W['punkte'] else None}


def paar(a, b):
    if a == b:
        return a
    return 'unklar'


def lauf_auswertung(pfade):
    J = {nm: json.load(open(p)) for nm, p in pfade.items()}
    out = {'eingaben': {nm: {'pfad': p, 'sha256': sha(p), 'skript': J[nm]['info']['skript_sha256']}
                        for nm, p in pfade.items()}}
    K = {}
    for nm in J:
        if nm.startswith('gitter-'):
            K[nm[7:]] = {art: kennz2(J[nm], art) for art in ('gerade', 'voll', 'affin')}
            K[nm[7:]]['nullmoden'] = nullmoden(J[nm])
            K[nm[7:]]['kontrollen'] = J[nm]['kontrollen']
            K[nm[7:]]['k0'] = J[nm]['k0']
            K[nm[7:]]['superzelle'] = J[nm]['superzelle']
            K[nm[7:]]['info_raum'] = J[nm].get('info_raum')
    out['kennzahlen'] = K
    V = {nm[5:]: {k: J[nm][k] for k in J[nm] if k not in ('bz_punkte', 'raster_punkte')}
         for nm in J if nm.startswith('vorz-')}
    out['vorzeichen'] = V
    Wz = {}
    grp = {}
    for nm in J:
        if nm.startswith('welle-'):
            base = nm[6:]
            for suf in ('-rw24', '-rk25'):
                if base.endswith(suf):
                    base = base[:-len(suf)]
            grp.setdefault(base, []).append(nm)
    for base, nms in grp.items():
        W = {'w0': {'a_max': max(J[n]['w0']['a_max'] for n in nms), 'b_max': max(J[n]['w0']['b_max'] for n in nms)},
             'tote_kanten_idx': J[nms[0]]['tote_kanten_idx'], 'lmean': J[nms[0]]['lmean'],
             'punkte': [p for n in sorted(nms) for p in J[n]['punkte']], 'dateien': sorted(nms)}
        if True:
            Wz[base] = {'w0': W['w0'], 'tote_kanten_idx': W['tote_kanten_idx'], 'lmean': W['lmean'], 'dateien': W['dateien'],
                          'urteil_0999': welle_urteil(W, 0.999, 1.001), 'urteil_09997': welle_urteil(W, 0.9997, 0.9999),
                          'zensus_intrinsisch_nicht_reell_max': max(p['zensus_light'].get('intrinsisch_nicht_reell', 0)
                                                                    for p in W['punkte']),
                          'zensus_intrinsisch_max': max(p['zensus_light'].get('intrinsisch', 0) for p in W['punkte'])}
    out['welle'] = Wz
    U = {}
    # Pipeline-Kontrollen
    kg = K['KW']['gerade']
    pk = (kg['s0'] is not None and kg['s0'] < 1e-6 and abs(kg['w0_mittel'] / -0.25 - 1) <= 1e-3
          and abs(kg['konf_zu_tt'] + 2) <= 2e-3)
    U['PK'] = {'urteil': 'bestanden' if pk else 'nicht bestanden', 's0': kg['s0'], 'w0_mittel': kg['w0_mittel'],
               'konf_zu_tt': kg['konf_zu_tt']}
    vk = V['KW']
    q0 = vk['q0']
    pkv = (q0['null'] == 11 and q0['pos'] == 4 and q0['neg'] == 0 and vk['bz_signaturen'] == {'5/9/1': 4095})
    U['PK-V'] = {'urteil': 'bestanden' if pkv else 'nicht bestanden', 'q0': [q0['null'], q0['pos'], q0['neg']],
                 'bz_signaturen': vk['bz_signaturen']}
    w0ok = {a: (Wz[a]['w0']['a_max'] <= 1e-12 and Wz[a]['w0']['b_max'] <= 1e-10) for a in Wz}
    U['W0'] = {a: {'ok': w0ok[a], 'a_max': Wz[a]['w0']['a_max'], 'b_max': Wz[a]['w0']['b_max']} for a in Wz}
    # RQ0
    wk = Wz['KW-koord']['urteil_09997']
    a0 = wk['urteil'] == 'eingetroffen'
    b1g, b1v = K['B1-t1']['gerade']['s0'], K['B1-t1']['voll']['s0']
    b0 = b1g is not None and b1g < 1e-8
    b0v = b1v is not None and b1v < 1e-8
    U['RQ0'] = {'plan': 'eingetroffen' if (a0 and b0) else 'nicht eingetroffen',
                'karte': ('eingetroffen' if (a0 and b0 and b0v) else
                          ('nicht eingetroffen' if (not a0 or (not b0 and not b0v)) else 'unklar')),
                'a_KW_welle': wk, 'b_B1_s0_gerade': b1g, 'b_B1_s0_voll': b1v, 'a': a0, 'b': b0}
    # RQ1
    g1, v1 = K['V-A']['gerade'], K['V-A']['voll']
    a1 = g1['s0'] is not None and g1['s0'] < 1e-6 and g1['r_abw_max'] <= 1e-4
    c1 = v1['s0'] is not None and v1['s0'] < 1e-6 and v1['r_abw_max'] <= 1e-4
    U['RQ1'] = {'plan': 'eingetroffen' if a1 else 'nicht eingetroffen', 'karte': rk.urteil_paar(a1, c1),
                's0_gerade': g1['s0'], 's0_voll': v1['s0'], 'r_abw_max_gerade': g1['r_abw_max'],
                'r_abw_max_voll': v1['r_abw_max'], 'n_richtungen': g1['n_richtungen'], 'w0_mittel': g1['w0_mittel'],
                'konf_zu_tt': g1['konf_zu_tt']}
    if not pk or not b0:
        U['RQ1']['plan_vor_PK'] = U['RQ1']['plan']
        U['RQ1']['karte_vor_PK'] = U['RQ1']['karte']
        U['RQ1']['plan'] = U['RQ1']['karte'] = 'unklar (Pipeline)'
    # RQ2
    nzv = K['V-A']['nullmoden']
    NVv = J['gitter-V-A']['kontrollen']['NV']
    vv = V['V-A']
    t2 = {'raster': (nzv['n0_min'] == 4 * NVv and nzv['n0_max'] == 4 * NVv and nzv['luecke_min'] is not None
                     and nzv['luecke_min'] >= 1e3 and nzv['rG_min'] == 4 * NVv and nzv['rG_max'] == 4 * NVv
                     and nzv['HG_max'] <= 1e-12 and nzv['sin_max'] is not None and nzv['sin_max'] <= 1e-6),
          'bz': vv['bz_null'] == {str(4 * NVv): 4095} and vv['bz_rG'] == {str(4 * NVv): 4095},
          'keine_tote_kante': len(nzv['tote_kanten']) == 0}
    r2 = all(t2.values())
    U['RQ2'] = {'plan': 'eingetroffen' if r2 else 'nicht eingetroffen', 'karte': 'eingetroffen' if r2 else 'nicht eingetroffen',
                'teile': t2, 'n0': [nzv['n0_min'], nzv['n0_max']], 'bz_null': vv['bz_null'], 'bz_rG': vv['bz_rG'],
                'tote_kanten': nzv['tote_kanten'], 'k0_n0': nzv['k0_n0']}
    # RQ3
    t3 = {'raster_ein_negativer': vv['raster_neg'] == {'1': 828},
          'bz_ein_negativer': vv['bz_neg'] == {'1': 4095},
          'q0_kein_negativer': vv['q0']['neg'] == 0,
          'tt_pos_konf_neg': nzv['tt_gerade_max'] < 0 and nzv['konf_gerade_min'] > 0}
    r3 = all(t3.values())
    U['RQ3'] = {'plan': 'eingetroffen' if r3 else 'nicht eingetroffen', 'karte': 'eingetroffen' if r3 else 'nicht eingetroffen',
                'teile': t3, 'raster_neg': vv['raster_neg'], 'bz_neg': vv['bz_neg'], 'q0': vv['q0'],
                'bz_signaturen': vv['bz_signaturen'], 'raster_signaturen': vv['raster_signaturen']}
    if not pkv:
        U['RQ3']['plan_vor_PK'] = U['RQ3']['plan']
        U['RQ3']['plan'] = U['RQ3']['karte'] = 'unklar (Pipeline)'
    # RQ4
    hk = Wz['V-A-koord']['urteil_0999']
    nk = Wz['V-A-kl']['urteil_0999']
    U['RQ4'] = {'plan': hk['urteil'], 'karte': paar(hk['urteil'], nk['urteil']), 'hauptlesart': hk, 'nebenlesart_kl': nk}
    if not a0 or not w0ok.get('V-A-koord', False) or not w0ok.get('V-A-kl', False):
        U['RQ4']['plan_vor_PK'] = U['RQ4']['plan']
        U['RQ4']['karte_vor_PK'] = U['RQ4']['karte']
        U['RQ4']['plan'] = U['RQ4']['karte'] = 'unklar (Pipeline)'
    out['urteile'] = U
    return out


# ================================================================================================= main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['gitter', 'vorzeichen', 'welle', 'auswertung'])
    ap.add_argument('--arm', default='V-A', choices=['KW', 'B1-t1', 'V-A', 'V-B', 'S-A'])
    ap.add_argument('--betraege', default='0.05')
    ap.add_argument('--lesart', default='koord', choices=['koord', 'kl'])
    ap.add_argument('--richtungen', default='beide', choices=['rw24', 'rk25', 'beide'])
    ap.add_argument('--pt', action='store_true')
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--ein', nargs='*', default=[])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)),
            'rk_sha256': sha(os.path.join(HIER, 'rk.py')), 'pt_sha256': sha(os.path.join(HIER, 'pt.py')),
            'ew_sha256': sha(os.path.join(HIER, 'ew.py')), 'tp_sha256': sha(os.path.join(HIER, 'tp.py'))}
    if a.modus == 'auswertung':
        res = lauf_auswertung(dict(x.split('=', 1) for x in a.ein))
    else:
        g = baue2(a.arm)
        if a.modus == 'gitter':
            res = rk.lauf_gitter(g, rauch=a.rauch, mit_pt=a.pt)
            res['tote_kanten_idx'] = tote_idx(g)
        elif a.modus == 'vorzeichen':
            res = lauf_vorzeichen(g, rauch=a.rauch)
        else:
            res = lauf_welle(g, [float(x) for x in a.betraege.split(',')], a.lesart, a.richtungen, rauch=a.rauch)
        res['arm'] = a.arm
    res['info'] = info
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, a.arm if a.modus != 'auswertung' else '', 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
