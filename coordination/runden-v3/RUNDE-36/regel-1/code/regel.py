#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGEL-1, Runde 36 (fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Basis: Kopie von RUNDE-36/lambda-1/code/lam.py (LAMBDA-1, eingefroren 20261004-004847, sha256 65dac72d...), Zeilen 31 bis
1219 unveraendert (Operatoren, Hesse-Matrizen, Statik-KKT, Zwangsflaechen-Dynamik, Ortsraum-Stencils). lam.py ist selbst
eine Kopie von tn.py (TENSOR-EIS-N). Entfernt: nur lam.py main(). Neu (Abschnitt REGEL-1 unten):
  - Regel fest eingebaut: Spurkoeffizient c = 1/2 exakt (Gl. 23-Invarianz), ohne Strafterme (U_v = U_s = 0).
  - Teil 1 (Modus wellen): Moden auf der Zwangsflaeche Z = ker c x ker Kv, Zaehlung laufender Moden, Dispersion in
    103 Richtungen, Invarianzdefekt unter Gl. 23, Wachstum (Projektion, Dirac).
  - Teil 2/3 (Modus statik): 3D-Radialprofile von M1 (beta = 1/2) als Quellen R^ii = kappa rho auf dem Gitter
    (rho = Energiedichte oder |phi|^2), statischer Kern je q per KKT (wie TENSOR-EIS-N), Wechselwirkung per
    Kreuzkorrelation, Torus-Korrektur per Ewald (periodisches Kontinuum), Groessenreihe.
  - Modus radial: Radialloeser 3D gegen bekannte Werte (RUNDE-02/tests1d, Test 4), Aufloesungsreihe in h.
  - Modus kontrolle: Ortsraum (Stencils): Invarianz unter Gl. 23, statische Zwei-Quellen-Loesung gegen den Fourierweg,
    Zeitentwicklung auf Z, voller 16x16-KKT bei c = 1/2, Ewald-Unabhaengigkeit von alpha.

Modell M1: L = |phi_t|^2 - |grad phi|^2 - U(|phi|^2), U(S) = S - S^2 + beta S^3, beta = 1/2; phi = f(r) exp(-i omega t).
Energiedichte rho_E = omega^2 f^2 + f'^2 + U(f^2); Ladungsdichte-Mass |phi|^2 = f^2 (int f^2 = Q/(2 omega)).
Einheiten: Gravitationsgitter J = g = 1, kappa = 1; Gitterweite h in Laengeneinheiten von M1 (Masse 1).
"""
import argparse, json, sys, time, platform, os, resource, hashlib
from fractions import Fraction
import numpy as np

S2 = 1.0 / np.sqrt(2.0)
KOMP = ['xx', 'yy', 'zz', 'xy', 'yz', 'zx']
IJ = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0)]
OFF = [(0., 0., 0.), (0., 0., 0.), (0., 0., 0.), (.5, .5, 0.), (0., .5, .5), (.5, 0., .5)]


def eps3():
    e = np.zeros((3, 3, 3))
    for (i, j, k), s in {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}.items():
        e[i, j, k] = s
    return e


EPS = eps3()


def basis6():
    B = np.zeros((6, 3, 3))
    for a, (i, j) in enumerate(IJ):
        if i == j:
            B[a, i, i] = 1.0
        else:
            B[a, i, j] = B[a, j, i] = S2
    return B


B6 = basis6()
TR = np.einsum('aii->a', B6)
# inc(B_a)_ij = - sum eps_imk eps_jln K_m K_l B_a[n,k]   (Gl. 16 mit d -> iK)
W_INC = -np.einsum('imk,jln,ank->aijml', EPS, EPS, B6)
W_INCB = np.einsum('bij,aijml->baml', B6, W_INC)        # <B_b, inc(B_a)>
W_C = np.einsum('aiiml->aml', W_INC)                     # tr inc(B_a)  (Gl. 22)
_BT = B6 - 0.5 * np.einsum('a,nj->anj', TR, np.eye(3))
W_CC = np.einsum('imn,anj->ijam', EPS, _BT)              # C^i_j(B_a) / i  (Gl. 24)


def kvek(q):
    return 2.0 * np.sin(0.5 * q)


def ops(K):
    KK = K[..., :, None] * K[..., None, :]
    Inc = np.einsum('baml,...ml->...ba', W_INCB, KK)
    c = np.einsum('aml,...ml->...a', W_C, KK)
    Kv = np.einsum('...i,aij->...ja', K, B6)                       # d_i E^ij = i Kv.E
    G15 = np.einsum('aij,...i->...aj', B6, K) + np.einsum('ajk,...k->...aj', B6, K)   # a -> a + df + df
    K2 = (K * K).sum(-1)
    G23 = TR * K2[..., None] - np.einsum('aij,...ij->...a', B6, KK)                  # E -> E + (delta K^2 - KK) f0
    Cr = np.einsum('ijam,...m->...ija', W_CC, K).reshape(K.shape[:-1] + (9, 6))
    return {'Inc': Inc, 'c': c, 'Kv': Kv, 'G15': G15, 'G23': G23, 'Cr': Cr, 'K2': K2}


def mT(X):
    return np.swapaxes(X, -1, -2)


def hesse(o, typ, J=1.0, g=1.0, Uv=0.0, Us=0.0, lam=0.5):
    """Hesse-Matrizen A (E-Teil) und B (a-Teil)."""
    if typ == 'N':
        A = J * (np.eye(6) - lam * np.outer(TR, TR)) + 0.0 * o['Inc']
        B = g * o['Inc']
    else:
        A = J * (mT(o['Cr']) @ o['Cr'])
        B = g * (mT(o['Inc']) @ o['Inc'])
    if Uv:
        A = A + Uv * (mT(o['Kv']) @ o['Kv'])
    if Us:
        B = B + Us * (o['c'][..., :, None] * o['c'][..., None, :])
    return A, B


# ------------------------------------------------------------------------------------------------ Statik
def kern_statik(K, typ, g=1.0, rcond=1e-10, mit_min=False):
    """Stationaerer Wert von 1/2 a.B.a unter c.a = rho (exakt), je q, als 1/2 kap |rho|^2 (KKT, pinv)."""
    o = ops(K)
    _, B = hesse(o, typ, g=g)
    c = o['c']
    n = K.shape[:-1]
    M = np.zeros(n + (7, 7))
    M[..., :6, :6] = B
    M[..., :6, 6] = c
    M[..., 6, :6] = c
    P = np.linalg.pinv(M, rcond=rcond, hermitian=True)
    x = P[..., :6, 6]
    kap = np.einsum('...a,...ab,...b->...', x, B, x)
    res = np.einsum('...a,...a->...', c, x) - 1.0
    out = {'kap': kap, 'res': res}
    if mit_min:
        # Tangentialraum der Zwangsflaeche: Projektor auf c-Orthogonalraum; Eigenwerte von P B P
        cn2 = (c * c).sum(-1)
        ok = cn2 > 0
        cn = np.where(ok[..., None], c / np.sqrt(np.where(ok, cn2, 1.0))[..., None], 0.0)
        Pc = np.eye(6) - cn[..., :, None] * cn[..., None, :]
        ev = np.linalg.eigvalsh(Pc @ B @ Pc)
        skal = np.abs(np.linalg.eigvalsh(B)).max(-1)
        out['tan_min_rel'] = np.where(ok, ev.min(-1) / np.where(skal > 0, skal, 1.0), 0.0)
        out['tan_neg'] = np.where(ok, (ev < -1e-9 * skal[..., None]).sum(-1), 0)
        # Gegenweg ohne KKT: kap' = 1 / (c.B^+.c)
        Bp = np.linalg.pinv(B, rcond=rcond, hermitian=True)
        d = np.einsum('...a,...ab,...b->...', c, Bp, c)
        out['kap_alt'] = np.where(ok, 1.0 / np.where(ok, d, 1.0), 0.0)
        out['ok'] = ok
    return out


OKT = 18   # Oktant 0..17 je Achse


def lauf_statik(L, chunk, typen=('N',), g=1.0, mit_min=False):
    t0 = time.time()
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    q3 = 2 * np.pi * np.fft.rfftfreq(L)
    kap = {t: np.empty((L, L, len(q3))) for t in typen}
    stat = {t: {'res_max': 0.0} for t in typen}
    if mit_min:
        for t in typen:
            stat[t].update({'tan_min_rel': np.inf, 'tan_neg_anzahl': 0, 'kap_alt_maxabw': 0.0})
    for i0 in range(0, L, chunk):
        qx, qy, qz = np.meshgrid(q1[i0:i0 + chunk], q1, q3, indexing='ij')
        K = kvek(np.stack([qx, qy, qz], -1))
        null = (qx == 0) & (qy == 0) & (qz == 0)
        for t in typen:
            o = kern_statik(K, t, g, mit_min=mit_min)
            kap[t][i0:i0 + chunk] = o['kap']
            r = np.where(null, 0.0, np.abs(o['res']))
            stat[t]['res_max'] = max(stat[t]['res_max'], float(r.max()))
            if mit_min:
                stat[t]['tan_min_rel'] = min(stat[t]['tan_min_rel'], float(np.where(o['ok'], o['tan_min_rel'], np.inf).min()))
                stat[t]['tan_neg_anzahl'] += int(o['tan_neg'].sum())
                sk = np.abs(o['kap']).max()
                stat[t]['kap_alt_maxabw'] = max(stat[t]['kap_alt_maxabw'],
                                                float(np.abs(np.where(o['ok'], o['kap'] - o['kap_alt'], 0.0)).max() / max(sk, 1e-300)))
    t_kern = time.time() - t0
    res = {'L': L, 't_kern_s': t_kern, 'stat': stat, 'kap_q0': {t: float(kap[t][0, 0, 0]) for t in typen}}
    wuerfel = {}
    ok_ = min(OKT, L // 2 + 1)
    for t in typen:
        G = np.fft.irfftn(kap[t], s=(L, L, L), axes=(0, 1, 2))
        wuerfel[t] = G[:ok_, :ok_, :ok_].copy()
        # Symmetrieprobe: G(r) gegen G(-r) und Achsenvertauschung
        res.setdefault('sym', {})[t] = {
            'spiegel_max': float(np.abs(G[1:ok_, :ok_, :ok_] - G[L - 1:L - ok_:-1, :ok_, :ok_]).max()),
            'tausch_max': float(np.abs(G[:ok_, :ok_, :ok_] - np.transpose(G[:ok_, :ok_, :ok_], (1, 0, 2))).max()),
            'mittel': float(G.mean()), 'G0': float(G[0, 0, 0])}
        del G
    res['t_gesamt_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    return res, wuerfel


# ------------------------------------------------------------------------------------------------ Spektrum
PARAM = {'P0': ('N', 0.0, 0.0), 'P1': ('N', 1.0, 1.0), 'P2': ('N', 0.1, 0.1), 'P3': ('N', 10.0, 10.0),
         'P4': ('N', 100.0, 100.0), 'P5': ('N', 1.0, 0.01), 'P6': ('N', 0.01, 1.0),
         'L0': ('L', 0.0, 0.0), 'L1': ('L', 1.0, 1.0)}
LAM_SCAN = [0.40, 0.45, 0.49, 0.50, 0.51, 0.55, 0.60]
TAU = 1e-6


def nullraum(M, dim):
    """Orthonormalbasis des Nullraums (letzte dim rechte Singulaervektoren), M (...,m,6)."""
    _, s, Vt = np.linalg.svd(M)
    return mT(Vt[..., 6 - dim:, :]), s


def physraeume(o):
    """S_E: ker(Kv) ohne Eichrichtung G23; S_a: ker(c) ohne Eichraum G15. Je 6x2."""
    ME = np.concatenate([o['Kv'], o['G23'][..., None, :]], -2)          # 4x6
    Ma = np.concatenate([o['c'][..., None, :], mT(o['G15'])], -2)        # 4x6
    SE, sE = nullraum(ME, 2)
    Sa, sa = nullraum(Ma, 2)
    ZE, _ = nullraum(o['Kv'], 3)                                         # ker Kv (Zwangsflaeche E, mit Eichung)
    Za, _ = nullraum(o['c'][..., None, :], 5)                            # ker c (Zwangsflaeche a, mit Eichung)
    return SE, Sa, ZE, Za, sE, sa


def projektor(V):
    """Orthogonalprojektor auf das Spaltenbild von V (...,6,k) per SVD."""
    U, s, _ = np.linalg.svd(V, full_matrices=False)
    r = (s > 1e-10 * s.max(-1, keepdims=True))
    U = U * r[..., None, :]
    return U @ mT(U)


def dyn_eig(A, B):
    """omega^2 = Eigenwerte von A B (Hamilton: da = A E, dE = -B a)."""
    return np.linalg.eigvals(A @ B)


def wachstum(w2, A, B):
    s = np.linalg.norm(A, 2, axis=(-2, -1)) * np.linalg.norm(B, 2, axis=(-2, -1))
    s = np.where(s > 0, s, 1.0)
    neg = (-w2.real / s[..., None]).max(-1)
    im = (np.abs(w2.imag) / s[..., None]).max(-1)
    om = np.sqrt(w2.astype(complex))
    gam = np.abs(om.imag).max(-1)
    return neg, im, gam


def lauf_spektrum(L):
    t0 = time.time()
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    qx, qy, qz = np.meshgrid(q1, q1, q1, indexing='ij')
    q = np.stack([qx, qy, qz], -1).reshape(-1, 3)
    nz = np.any(q != 0, axis=1)
    out = {'L': L, 'nq': int(len(q))}
    K = kvek(q[nz])
    o = ops(K)
    # Kontrollen der Operatoren
    out['kontr'] = {
        'Inc_sym': float(np.abs(o['Inc'] - mT(o['Inc'])).max()),
        'divR_null': float(np.abs(np.einsum('...ja,...ab->...jb', o['Kv'], o['Inc'])).max()),   # d_i R^ij = 0 (Gl. 19)
        'Inc_G15_null': float(np.abs(o['Inc'] @ o['G15']).max()),                               # R eichinvariant (Gl. 15)
        'c_G15_null': float(np.abs(np.einsum('...a,...aj->...j', o['c'], o['G15'])).max()),
        'Kv_G23_null': float(np.abs(np.einsum('...ja,...a->...j', o['Kv'], o['G23'])).max()),   # [S, V] = 0
        'c_plus_G23': float(np.abs(o['c'] + o['G23']).max()),
        'C_G23_null': float(np.abs(np.einsum('...ia,...a->...i', o['Cr'], o['G23'])).max()),   # C invariant (Gl. 23)
        'rang_Kv_min': int(np.linalg.matrix_rank(o['Kv']).min()),
        'rang_G15_min': int(np.linalg.matrix_rank(o['G15']).min()),
    }
    SE, Sa, ZE, Za, sE, sa = physraeume(o)
    out['kontr']['phys_E_sing_min'] = float(sE[..., :4].min())
    out['kontr']['phys_a_sing_min'] = float(sa[..., :4].min())
    # Physikalische Unterraeume von E- und a-Seite: gleicher Unterraum? (Hauptwinkel)
    ov = np.linalg.svd(mT(SE) @ Sa, compute_uv=False)
    out['kontr']['phys_E_gleich_a_min_cos'] = float(ov.min())
    # ---- N-Typ ohne Strafterme: Definitheit
    res = {}
    A, B = hesse(o, 'N')
    eA, vA = np.linalg.eigh(A)
    eB, vB = np.linalg.eigh(B)
    sA = np.abs(eA).max(-1)
    sB = np.abs(eB).max(-1)
    res['A_neg_q_anteil'] = float((eA.min(-1) < -1e-9 * sA).mean())
    res['B_neg_q_anteil'] = float((eB.min(-1) < -1e-9 * sB).mean())
    res['A_min'] = float(eA.min())
    res['B_min_rel'] = float((eB.min(-1) / sB).min())
    res['A_neg_anzahl_je_q'] = sorted(set(int(x) for x in (eA < -1e-9 * sA[:, None]).sum(-1)))
    res['B_neg_anzahl_je_q'] = sorted(set(int(x) for x in (eB < -1e-9 * sB[:, None]).sum(-1)))
    # Charakter der negativen Richtungen
    PgE = (o['G23'] / np.linalg.norm(o['G23'], axis=-1, keepdims=True))
    PvE = projektor(mT(o['Kv']))                  # Bild Kv^T = Verletzung der Vektorbedingung
    PgA = projektor(o['G15'])                     # Eichraum (Gl. 15)
    cn = o['c'] / np.linalg.norm(o['c'], axis=-1, keepdims=True)
    vneg = vA[..., :, 0]                          # Eigenvektor zum kleinsten Eigenwert
    w = {'phys': (np.einsum('...ak,...a->...k', SE, vneg) ** 2).sum(-1),
         'eich': np.einsum('...a,...a->...', PgE, vneg) ** 2,
         'verl': np.einsum('...a,...ab,...b->...', vneg, PvE, vneg)}
    res['A_negvek_gewichte'] = {k: [float(v.min()), float(v.max())] for k, v in w.items()}
    vnb = vB[..., :, 0]
    w = {'phys': (np.einsum('...ak,...a->...k', Sa, vnb) ** 2).sum(-1),
         'eich': np.einsum('...a,...ab,...b->...', vnb, PgA, vnb),
         'verl': np.einsum('...a,...a->...', cn, vnb) ** 2}
    res['B_negvek_gewichte'] = {k: [float(v.min()), float(v.max())] for k, v in w.items()}
    # Einschraenkung auf die Zwangsflaeche (mit Eichung) und auf die eichfreie Zwangsflaeche
    eAZ = np.linalg.eigvalsh(mT(ZE) @ A @ ZE)
    eBZ = np.linalg.eigvalsh(mT(Za) @ B @ Za)
    eAP = np.linalg.eigvalsh(mT(SE) @ A @ SE)
    eBP = np.linalg.eigvalsh(mT(Sa) @ B @ Sa)
    res['A_zwang_min_rel'] = float((eAZ.min(-1) / sA).min())
    res['B_zwang_min_rel'] = float((eBZ.min(-1) / sB).min())
    res['A_phys_min_rel'] = float((eAP.min(-1) / sA).min())
    res['B_phys_min_rel'] = float((eBP.min(-1) / sB).min())
    res['A_phys_max_rel'] = float((eAP.max(-1) / sA).max())
    res['B_phys_min_ueber_K2'] = float((eBP.min(-1) / o['K2']).min())
    res['B_phys_max_ueber_K2'] = float((eBP.max(-1) / o['K2']).max())
    # Dynamik nur im physikalischen Raum (exakte Zwangsbedingungen, Eichung herausgenommen)
    Ared = mT(SE) @ A @ SE
    Bred = mT(SE) @ B @ SE      # gleicher Unterraum (s. kontr), Paarung kanonisch
    w2p = np.linalg.eigvals(Ared @ Bred)
    ng, im, gam = wachstum(w2p, Ared, Bred)
    res['phys_dyn'] = {'neg_rel_max': float(ng.max()), 'im_rel_max': float(im.max()), 'gamma_max': float(gam.max()),
                       'w2_ueber_K2_min': float((w2p.real / o['K2'][:, None]).min()),
                       'w2_ueber_K2_max': float((w2p.real / o['K2'][:, None]).max())}
    out['N_definitheit'] = res
    # q = 0 (homogene Moden auf dem Torus), gesondert
    o0 = ops(np.zeros((1, 3)))
    A0, B0 = hesse(o0, 'N')
    out['q0'] = {'A_eig': [float(x) for x in np.linalg.eigvalsh(A0[0])], 'B_eig': [float(x) for x in np.linalg.eigvalsh(B0[0])]}
    # ---- Dynamik: Parametersaetze
    dyn = {}
    for name, (typ, Uv, Us) in PARAM.items():
        A, B = hesse(o, typ, Uv=Uv, Us=Us)
        w2 = dyn_eig(A, B)
        ng, im, gam = wachstum(w2, A, B)
        eA = np.linalg.eigvalsh(A)
        eB = np.linalg.eigvalsh(B)
        dyn[name] = {'typ': typ, 'Uv': Uv, 'Us': Us,
                     'neg_rel_max': float(ng.max()), 'im_rel_max': float(im.max()), 'gamma_max': float(gam.max()),
                     'wachsend_q_anzahl': int(((ng > TAU) | (im > TAU)).sum()),
                     'A_neg_q_anteil': float((eA.min(-1) < -1e-9 * np.abs(eA).max(-1)).mean()),
                     'B_neg_q_anteil': float((eB.min(-1) < -1e-9 * np.abs(eB).max(-1)).mean()),
                     'nullmoden_je_q': sorted(set(int(x) for x in (np.abs(w2) <= 1e-6 * np.abs(w2).max(-1, keepdims=True)).sum(-1)))}
    out['dynamik'] = dyn
    lam = {}
    for lmb in LAM_SCAN:
        for Uv, Us in ((1.0, 1.0), (0.0, 0.0)):
            A, B = hesse(o, 'N', Uv=Uv, Us=Us, lam=lmb)
            w2 = dyn_eig(A, B)
            ng, im, gam = wachstum(w2, A, B)
            lam['%.2f_U%g' % (lmb, Uv)] = {'lam': lmb, 'U': Uv, 'neg_rel_max': float(ng.max()), 'im_rel_max': float(im.max()),
                                           'gamma_max': float(gam.max()), 'wachsend_q_anteil': float(((ng > TAU) | (im > TAU)).mean())}
    out['lam_scan'] = lam
    # ---- Linienschnitte fuer Bilder
    t = np.logspace(-3, np.log10(np.pi), 160)
    linien = {}
    for nm, d in (('100', (1, 0, 0)), ('110', (1, 1, 0)), ('111', (1, 1, 1))):
        dn = np.array(d, float) / np.linalg.norm(d)
        Kl = kvek(t[:, None] * dn)
        ol = ops(Kl)
        z = {'t': t.tolist()}
        for name in ('P0', 'P1', 'L0'):
            typ, Uv, Us = PARAM[name]
            A, B = hesse(ol, typ, Uv=Uv, Us=Us)
            z[name] = {'eigA': np.linalg.eigvalsh(A).tolist(), 'eigB': np.linalg.eigvalsh(B).tolist(),
                       'w2': np.sort(dyn_eig(A, B).real, -1).tolist()}
        SEl, Sal, _, _, _, _ = physraeume(ol)
        A, B = hesse(ol, 'N')
        z['phys_A'] = np.linalg.eigvalsh(mT(SEl) @ A @ SEl).tolist()
        z['phys_B'] = np.linalg.eigvalsh(mT(Sal) @ B @ Sal).tolist()
        linien[nm] = z
    out['t_s'] = time.time() - t0
    return out, linien


# ------------------------------------------------------------------------------------------------ Kontrollen
def ableitung(f, m, off):
    """d_m auf dem gestaffelten Gitter: f liegt bei n + off; Ergebnis bei n + off' (m-te Komponente umgeklappt)."""
    if off[m] == 0.0:
        g = np.roll(f, -1, axis=m) - f
    else:
        g = f - np.roll(f, 1, axis=m)
    o2 = list(off)
    o2[m] = 0.5 - off[m]
    return g, tuple(o2)


def inc_ort(x):
    """x: (6,L,L,L) Orthonormal-Koeffizienten von a -> Koeffizienten von R = inc(a), Ortsraum."""
    L = x.shape[1]
    a = {}
    for al, (i, j) in enumerate(IJ):
        v = x[al] if i == j else x[al] * S2
        a[(i, j)] = (v, OFF[al])
        a[(j, i)] = (v, OFF[al])
    R = np.zeros_like(x)
    for be, (i, j) in enumerate(IJ):
        acc = np.zeros((L, L, L))
        for m in range(3):
            for k in range(3):
                if EPS[i, m, k] == 0:
                    continue
                for l in range(3):
                    for n in range(3):
                        s = EPS[i, m, k] * EPS[j, l, n]
                        if s == 0:
                            continue
                        f, off = a[(n, k)]
                        g1, o1 = ableitung(f, l, off)
                        g2, o2 = ableitung(g1, m, o1)
                        assert np.allclose(o2, OFF[be]), (i, j, m, k, l, n, o2)
                        acc = acc + s * g2
        R[be] = acc if i == j else acc / S2
    return R


def div_ort(y):
    """y: (6,L,L,L) Orthonormal-Koeffizienten von E -> d_i E^ij (3,L,L,L) auf den Links."""
    E = {}
    for al, (i, j) in enumerate(IJ):
        v = y[al] if i == j else y[al] * S2
        E[(i, j)] = (v, OFF[al])
        E[(j, i)] = (v, OFF[al])
    out = []
    for j in range(3):
        acc = 0
        for i in range(3):
            f, off = E[(i, j)]
            g, o2 = ableitung(f, i, off)
            ziel = [0., 0., 0.]
            ziel[j] = 0.5
            assert np.allclose(o2, ziel), (i, j, o2)
            acc = acc + g
        out.append(acc)
    return np.array(out)


def ortsraum_matrizen(L):
    N = L ** 3
    Inc = np.zeros((6 * N, 6 * N))
    Q = np.zeros((3 * N, 6 * N))
    for col in range(6 * N):
        x = np.zeros(6 * N)
        x[col] = 1.0
        x = x.reshape(6, L, L, L)
        Inc[:, col] = inc_ort(x).reshape(-1)
        Q[:, col] = div_ort(x).reshape(-1)
    c = Inc.reshape(6, N, 6 * N)[:3].sum(0)
    return Inc, Q, c


def kontrolle_ortsraum(L=6):
    t0 = time.time()
    N = L ** 3
    Inc, Q, c = ortsraum_matrizen(L)
    out = {'L': L, 'Inc_sym': float(np.abs(Inc - Inc.T).max()), 'c_summe_null': float(np.abs(c.sum(0)).max())}
    vekt = [(1, 0, 0), (2, 0, 0), (3, 0, 0), (1, 1, 0), (2, 1, 1), (2, 2, 2), (3, 3, 3), (1, 2, 3)]
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    qx, qy, qz = np.meshgrid(q1, q1, q1, indexing='ij')
    Kf = kvek(np.stack([qx, qy, qz], -1))
    for typ in ('N', 'L'):
        B = Inc if typ == 'N' else Inc.T @ Inc
        M = np.zeros((7 * N, 7 * N))
        M[:6 * N, :6 * N] = B
        M[:6 * N, 6 * N:] = c.T
        M[6 * N:, :6 * N] = c
        Mp = np.linalg.pinv(M, rcond=1e-10, hermitian=True)

        def energie(rho):
            rho = rho - rho.mean()
            sol = Mp @ np.concatenate([np.zeros(6 * N), rho])
            x = sol[:6 * N]
            return 0.5 * x @ B @ x, float(np.abs(c @ x - rho).max())
        e1, r1 = energie(np.eye(N)[0])
        kap = kern_statik(Kf, typ)['kap']
        G = np.fft.ifftn(kap).real
        rows = []
        rmax = r1
        for v in vekt:
            rho = np.zeros((L, L, L))
            rho[0, 0, 0] += 1.0
            rho[v[0] % L, v[1] % L, v[2] % L] += 1.0
            ep, rr = energie(rho.reshape(-1))
            rmax = max(rmax, rr)
            # Einzelquelle an v hat dieselbe Energie wie am Ursprung (Translation)
            U_ort = ep - 2 * e1
            rows.append({'v': list(v), 'U_ortsraum': float(U_ort), 'U_fourier': float(G[v[0] % L, v[1] % L, v[2] % L])})
        out['statik_' + typ] = {'zeilen': rows, 'zwang_res_max': rmax,
                                'max_abw': max(abs(r['U_ortsraum'] - r['U_fourier']) for r in rows)}
    # Spektrum: Ortsraum-AB gegen Vereinigung der Fourier-AB (N-Typ mit Straftermen P1 und L-Typ L0)
    PE = (Q.T @ Q)
    J = 1.0
    MJ = np.kron(np.eye(6) - 0.5 * np.outer(TR, TR), np.eye(N))
    for name in ('P0', 'P1'):
        typ, Uv, Us = PARAM[name]
        A = J * MJ + Uv * PE
        B = Inc + Us * (c.T @ c)
        w2o = np.sort(np.linalg.eigvals(A @ B).real)
        of = ops(Kf.reshape(-1, 3))
        Af, Bf = hesse(of, 'N', Uv=Uv, Us=Us)
        w2f = np.sort(np.linalg.eigvals(Af @ Bf).real.reshape(-1))
        out['spektrum_' + name] = {'max_abw': float(np.abs(w2o - w2f).max()), 'max_w2': float(np.abs(w2f).max()),
                                   'min_w2_ortsraum': float(w2o.min())}
    out['t_s'] = time.time() - t0
    return out


def gw_matrizen(k, Uphi, Utheta, Jt=1.0, gt=1.0):
    """Gu/Wen S. 19: quadratische k-Raum-Lagrangedichte (Klammern X fuer phi, Y fuer theta), c_a = cos(k_a/2)."""
    cx, cy, cz = np.cos(k[0] / 2), np.cos(k[1] / 2), np.cos(k[2] / 2)
    cxy, cyz, czx = cx * cy, cy * cz, cz * cx
    XJ = np.array([[.25, -.25, -.25, 0, 0, 0], [-.25, .25, -.25, 0, 0, 0], [-.25, -.25, .25, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])
    XU = np.array([[cx ** 2, 0, 0, cxy, 0, czx], [0, cy ** 2, 0, cxy, cyz, 0], [0, 0, cz ** 2, 0, cyz, czx],
                   [cxy, cxy, 0, cx ** 2 + cy ** 2, czx, cyz], [0, cyz, cyz, czx, cy ** 2 + cz ** 2, cxy],
                   [czx, 0, czx, cyz, cxy, cz ** 2 + cx ** 2]])
    Yg = np.array([[0, -2 * cz ** 2, -2 * cy ** 2, 0, 2 * cyz, 0], [-2 * cz ** 2, 0, -2 * cx ** 2, 0, 0, 2 * czx],
                   [-2 * cy ** 2, -2 * cx ** 2, 0, 2 * cxy, 0, 0], [0, 0, 2 * cxy, cz ** 2, -czx, -cyz],
                   [2 * cyz, 0, 0, -czx, cx ** 2, -cxy], [0, 2 * czx, 0, -cyz, -cxy, cy ** 2]])
    v = np.array([cy ** 2 + cz ** 2, cz ** 2 + cx ** 2, cx ** 2 + cy ** 2, cxy, cyz, czx])
    S = np.array([[1, 1, 1, -1, -1, -1]] * 3 + [[-1, -1, -1, 1, 1, 1]] * 3, float)
    YU = np.diag(v) @ S @ np.diag(v)
    X = Jt * XJ + 2 * Uphi * XU
    Y = gt * Yg + 8 * Utheta * YU
    return X, Y


def kontrolle_gw(nq=200, seed=7):
    rng = np.random.default_rng(seed)
    out = {}
    for name, Uv, Us in (('ohne', 0.0, 0.0), ('Uv0.7_Us1.3', 0.7, 1.3)):
        abw_strukt = 0.0
        abw_tausch = 0.0
        sk = 0.0
        for _ in range(nq):
            q = rng.uniform(-np.pi, np.pi, 3)
            k = q + np.pi
            o = ops(kvek(q)[None, :])
            A, B = hesse(o, 'N', Uv=Uv, Us=Us)
            w_m = np.sort(np.linalg.eigvals(A[0] @ B[0]).real)
            X, Y = gw_matrizen(k, Uphi=Uv, Utheta=Us)
            w_g = np.sort(np.linalg.eigvals(X @ Y).real) * 4.0
            X2, Y2 = gw_matrizen(k, Uphi=Us, Utheta=Uv)
            w_t = np.sort(np.linalg.eigvals(X2 @ Y2).real) * 4.0
            sk = max(sk, float(np.abs(w_m).max()))
            abw_strukt = max(abw_strukt, float(np.abs(w_m - w_g).max()))
            abw_tausch = max(abw_tausch, float(np.abs(w_m - w_t).max()))
        out[name] = {'max_abw_strukturgleich': abw_strukt, 'max_abw_vertauscht': abw_tausch, 'skala': sk}
    # Direkter Matrixvergleich (nach rauch3 ergaenzt, weil eig(AB) von U_v, U_s nicht abhaengt):
    # theta = D x, phi = D^-1 y mit D = diag(1,1,1, sqrt2 s_xy, sqrt2 s_yz, sqrt2 s_zx), s = +-1;
    # erwartet A = 2 D^-1 X D^-1 und B = 2 D Y D (X, Y sind Matrizen der quadratischen Formen).
    import itertools
    qs = [rng.uniform(-np.pi, np.pi, 3) for _ in range(nq)]
    best = {}
    for zuord in ('strukturgleich', 'vertauscht'):
        werte = []
        for s in itertools.product((1.0, -1.0), repeat=3):
            D = np.diag([1.0, 1.0, 1.0] + [np.sqrt(2.0) * x for x in s])
            Di = np.linalg.inv(D)
            mA = mB = 0.0
            for q in qs:
                o = ops(kvek(q)[None, :])
                A, B = hesse(o, 'N', Uv=0.7, Us=1.3)
                if zuord == 'strukturgleich':
                    X, Y = gw_matrizen(q + np.pi, Uphi=0.7, Utheta=1.3)
                else:
                    X, Y = gw_matrizen(q + np.pi, Uphi=1.3, Utheta=0.7)
                mA = max(mA, float(np.abs(A[0] - 2 * Di @ X @ Di).max()))
                mB = max(mB, float(np.abs(B[0] - 2 * D @ Y @ D).max()))
            werte.append({'s': list(s), 'max_abw_A': mA, 'max_abw_B': mB})
        best[zuord] = {'bestes': min(werte, key=lambda w: max(w['max_abw_A'], w['max_abw_B'])),
                       'alle': werte}
    out['matrixvergleich'] = best
    # Traegheit (Signatur) der Klammern gegen A, B ohne Strafterme
    sig = []
    for _ in range(50):
        q = rng.uniform(-np.pi, np.pi, 3)
        o = ops(kvek(q)[None, :])
        A, B = hesse(o, 'N')
        X, Y = gw_matrizen(q + np.pi, 0.0, 0.0)

        def tr(M):
            e = np.linalg.eigvalsh(M)
            s = np.abs(e).max()
            return (int((e > 1e-9 * s).sum()), int((np.abs(e) <= 1e-9 * s).sum()), int((e < -1e-9 * s).sum()))
        sig.append([tr(A[0]), tr(X), tr(B[0]), tr(Y)])
    out['signatur_A_X_B_Y'] = sorted(set(json.dumps(s) for s in sig))
    return out


# ---- exakte Bruchrechnung (physikalische Komponenten, Gram-Matrix W = diag(1,1,1,2,2,2))
def F(x, y=1):
    return Fraction(x, y)


def einheit(al):
    i, j = IJ[al]
    U = [[F(0)] * 3 for _ in range(3)]
    U[i][j] = F(1)
    U[j][i] = F(1)
    return U


EPSI = [[[int(EPS[i, j, k]) for k in range(3)] for j in range(3)] for i in range(3)]


def inc_exakt(U, K):
    R = [[F(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            s = F(0)
            for m in range(3):
                for k in range(3):
                    if EPSI[i][m][k] == 0:
                        continue
                    for l in range(3):
                        for n in range(3):
                            if EPSI[j][l][n] == 0:
                                continue
                            s -= EPSI[i][m][k] * EPSI[j][l][n] * K[m] * K[l] * U[n][k]
            R[i][j] = s
    return R


def frob(X, Y):
    return sum(X[i][j] * Y[i][j] for i in range(3) for j in range(3))


def tr3(X):
    return X[0][0] + X[1][1] + X[2][2]


def hesse_exakt(K, typ, J=F(1), g=F(1), Uv=F(0), Us=F(0), lam=F(1, 2)):
    U = [einheit(a) for a in range(6)]
    R = [inc_exakt(u, K) for u in U]
    A = [[F(0)] * 6 for _ in range(6)]
    B = [[F(0)] * 6 for _ in range(6)]
    cvec = [tr3(r) for r in R]
    kv = [[sum(K[i] * U[a][i][j] for i in range(3)) for j in range(3)] for a in range(6)]
    for b in range(6):
        for a in range(6):
            if typ == 'N':
                A[b][a] = J * (frob(U[b], U[a]) - lam * tr3(U[b]) * tr3(U[a]))
                B[b][a] = g * frob(U[b], R[a])
            else:
                Cb = [[sum(EPSI[i][m][n] * K[m] * (U[b][n][j] - (F(1, 2) * tr3(U[b]) if n == j else 0)) for m in range(3) for n in range(3)) for j in range(3)] for i in range(3)]
                Ca = [[sum(EPSI[i][m][n] * K[m] * (U[a][n][j] - (F(1, 2) * tr3(U[a]) if n == j else 0)) for m in range(3) for n in range(3)) for j in range(3)] for i in range(3)]
                A[b][a] = J * frob(Cb, Ca)
                B[b][a] = g * frob(R[b], R[a])
            A[b][a] += Uv * sum(kv[b][j] * kv[a][j] for j in range(3))
            B[b][a] += Us * cvec[b] * cvec[a]
    return A, B


def matmul(X, Y):
    n, m, p = len(X), len(Y), len(Y[0])
    return [[sum(X[i][k] * Y[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def charpoly(M):
    """Faddeev-LeVerrier, exakt: Koeffizienten c[0..n] von det(x I - M) = sum c_k x^k."""
    n = len(M)
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    c = [F(0)] * (n + 1)
    c[n] = F(1)
    Mk = [[F(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        Mk = matmul(M, Mk)
        for i in range(n):
            Mk[i][i] += c[n - k + 1]
        AM = matmul(M, Mk)
        c[n - k] = -sum(AM[i][i] for i in range(n)) / k
    return c


def rang(M):
    M = [row[:] for row in M]
    r = 0
    rows, cols = len(M), len(M[0])
    for col in range(cols):
        piv = next((i for i in range(r, rows) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(rows):
            if i != r and M[i][col] != 0:
                f = M[i][col] / M[r][col]
                M[i] = [M[i][j] - f * M[r][j] for j in range(cols)]
        r += 1
    return r


def poly_trim(p):
    p = p[:]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def poly_rem(a, b):
    """Rest von a durch b (Koeffizientenlisten, Index = Potenz), exakt."""
    a = poly_trim(a)[:]
    b = poly_trim(b)
    db = len(b) - 1
    while len(a) - 1 >= db and not (len(a) == 1 and a[0] == 0):
        f = a[-1] / b[-1]
        sh = len(a) - 1 - db
        for i in range(len(b)):
            a[i + sh] -= f * b[i]
        a.pop()
        a = poly_trim(a) if a else [F(0)]
    return a


def poly_deriv(p):
    return [p[i] * i for i in range(1, len(p))] or [F(0)]


def poly_eval(p, x):
    return sum(c * x ** i for i, c in enumerate(p))


def sturm_anzahl(p, a, b):
    """Anzahl verschiedener reeller Nullstellen in (a, b], a, b endlich oder +-inf (als None fuer +inf)."""
    seq = [poly_trim(p), poly_trim(poly_deriv(p))]
    while len(seq[-1]) > 1 or seq[-1][0] != 0:
        r = poly_rem(seq[-2], seq[-1])
        r = [-x for x in r]
        if all(x == 0 for x in r):
            break
        seq.append(poly_trim(r))

    def wechsel(vals):
        s = [v for v in vals if v != 0]
        return sum(1 for i in range(1, len(s)) if (s[i] > 0) != (s[i - 1] > 0))

    def werte(x):
        if x == 'inf':
            return [q[-1] for q in seq]
        if x == '-inf':
            return [q[-1] * (-1) ** (len(q) - 1) for q in seq]
        return [poly_eval(q, x) for q in seq]
    return wechsel(werte(a)) - wechsel(werte(b))


def poly_gcd(a, b):
    a, b = poly_trim(a), poly_trim(b)
    while not (len(b) == 1 and b[0] == 0):
        a, b = b, poly_rem(a, b)
        if not b:
            b = [F(0)]
    return a


def exakt_analyse(K, typ, Uv=F(0), Us=F(0), lam=F(1, 2)):
    A, B = hesse_exakt(K, typ, Uv=Uv, Us=Us, lam=lam)
    Wi = [F(1), F(1), F(1), F(1, 2), F(1, 2), F(1, 2)]
    Ah = [[Wi[i] * A[i][j] for j in range(6)] for i in range(6)]          # W^-1 A
    Bh = [[Wi[i] * B[i][j] for j in range(6)] for i in range(6)]          # W^-1 B
    Om = matmul(Ah, Bh)                                                  # omega^2-Matrix
    cp = charpoly(Om)
    m0 = next(i for i, x in enumerate(cp) if x != 0)
    qx = cp[m0:]
    deg = len(qx) - 1
    if deg > 0:
        sq = poly_trim(qx)
        gg = poly_gcd(sq, poly_deriv(sq))
        dist = deg - (len(poly_trim(gg)) - 1)
        pos = sturm_anzahl(sq, F(0), 'inf')
        reell = sturm_anzahl(sq, '-inf', 'inf')
    else:
        dist, pos, reell = 0, 0, 0
    # Jordanstruktur: Raenge von Om^k und der 12x12-Bewegungsmatrix D^k
    Z = [[F(0)] * 6 for _ in range(6)]
    D = [Z[i] + Ah[i] for i in range(6)] + [[-x for x in Bh[i]] + Z[i] for i in range(6)]
    rO, rD = [], []
    P = Om
    for k in range(1, 5):
        rO.append(rang(P))
        P = matmul(P, Om)
    P = D
    for k in range(1, 9):
        rD.append(rang(P))
        P = matmul(P, D)
    # Nilpotenzindex bei 0 der Bewegungsmatrix: kleinste Potenz, ab der der Rang steht
    nil = next((k + 1 for k in range(len(rD) - 1) if rD[k] == rD[k + 1]), None)
    return {'charpoly': [str(x) for x in cp], 'null_vielfachheit': m0, 'rest_grad': deg,
            'rest_verschiedene_wurzeln': dist, 'rest_wurzeln_reell': reell, 'rest_wurzeln_positiv': pos,
            'alle_w2_reell_nichtneg': bool(deg == 0 or (pos == dist and reell == dist)),
            'rang_Om_k': rO, 'rang_D_k': rD, 'jordan_max_D_bei_0': nil}


def kontrolle_exakt(n=12, seed=11):
    import random
    rnd = random.Random(seed)
    werte = [F(p, q) for q in (1, 2, 3, 4, 5, 7) for p in range(-2 * q, 2 * q + 1)]
    punkte = []
    while len(punkte) < n:
        K = [rnd.choice(werte) for _ in range(3)]
        if any(k != 0 for k in K):
            punkte.append(K)
    saetze = {'P0': ('N', F(0), F(0), F(1, 2)), 'P1': ('N', F(1), F(1), F(1, 2)), 'P3': ('N', F(10), F(10), F(1, 2)),
              'P5': ('N', F(1), F(1, 100), F(1, 2)), 'L0': ('L', F(0), F(0), F(1, 2)), 'L1': ('L', F(1), F(1), F(1, 2)),
              'lam0.45_P1': ('N', F(1), F(1), F(9, 20)), 'lam0.55_P1': ('N', F(1), F(1), F(11, 20))}
    out = {'punkte': [[str(k) for k in K] for K in punkte], 'saetze': {}}
    for name, (typ, Uv, Us, lam) in saetze.items():
        rows = [exakt_analyse(K, typ, Uv, Us, lam) for K in punkte]
        out['saetze'][name] = {
            'alle_w2_reell_nichtneg_alle_punkte': all(r['alle_w2_reell_nichtneg'] for r in rows),
            'null_vielfachheit': sorted(set(r['null_vielfachheit'] for r in rows)),
            'jordan_max_D_bei_0': sorted(set(str(r['jordan_max_D_bei_0']) for r in rows)),
            'rang_D_k': sorted(set(json.dumps(r['rang_D_k']) for r in rows)),
            'rang_Om_k': sorted(set(json.dumps(r['rang_Om_k']) for r in rows)),
            'beispiel_punkt0': rows[0]}
    return out


def drift_demo():
    """Zeitentwicklung an einem q: Verletzung der Vektorbedingung (E laengs) treibt die Skalarbedingung c.a (N) bzw. nicht (L)."""
    from scipy.linalg import expm
    K = kvek(np.array([0.3, 0.2, 0.1]))[None, :]
    o = ops(K)
    out = {}
    for name in ('P0', 'P1', 'L0'):
        typ, Uv, Us = PARAM[name]
        A, B = hesse(o, typ, Uv=Uv, Us=Us)
        A, B = A[0], B[0]
        D = np.block([[np.zeros((6, 6)), A], [-B, np.zeros((6, 6))]])
        Kv = o['Kv'][0]
        c = o['c'][0]
        # Anfangszustand: a = 0, E = Kv^T e_z (reine Verletzung der Vektorbedingung)
        E0 = Kv.T @ np.array([0., 0., 1.])
        z0 = np.concatenate([np.zeros(6), E0])
        ts = [0.0, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
        rows = []
        for t in ts:
            z = expm(D * t) @ z0
            rows.append({'t': t, 'c_a': float(c @ z[:6]), 'norm_a': float(np.linalg.norm(z[:6])),
                         'Q_E': float(np.linalg.norm(Kv @ z[6:]))})
        out[name] = rows
    return out


# ------------------------------------------------------------------------------------------------ LAMBDA-1: c-Abtastung
C_LISTE = [0.30, 1.0 / 3.0, 0.40, 0.45, 0.48, 0.49, 0.50, 0.51, 0.52, 0.55, 0.60, 0.70]
C_NAMEN = ['0.30', '1/3', '0.40', '0.45', '0.48', '0.49', '0.50', '0.51', '0.52', '0.55', '0.60', '0.70']
C_EXAKT = [F(3, 10), F(1, 3), F(2, 5), F(9, 20), F(12, 25), F(49, 100), F(1, 2), F(51, 100), F(13, 25), F(11, 20),
           F(3, 5), F(7, 10)]
SAETZE = {'P0': (0.0, 0.0), 'P1': (1.0, 1.0), 'P2': (0.1, 0.1), 'P3': (10.0, 10.0), 'P4': (100.0, 100.0),
          'P5': (1.0, 0.01), 'P6': (0.01, 1.0)}
TOL_DIRAC = 1e-9


def norm2(M):
    return np.linalg.norm(M, 2, axis=(-2, -1))


def bz_punkte(L):
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    qx, qy, qz = np.meshgrid(q1, q1, q1, indexing='ij')
    q = np.stack([qx, qy, qz], -1).reshape(-1, 3)
    return q[np.any(q != 0, axis=1)]


def wachs_test(w2, s):
    """w2 (n,m) Eigenwerte omega^2, s (n,) Skala |A||B|. Je Eigenwert: wachsend (TAU-Test wie TENSOR-EIS-N),
    Rate gamma = |Im sqrt(omega^2)| (nur fuer wachsende, sonst 0), -Re/s und |Im|/s."""
    w2 = w2.astype(complex)
    neg = -w2.real / s[:, None]
    im = np.abs(w2.imag) / s[:, None]
    wach = (neg > TAU) | (im > TAU)
    gam = np.abs(np.sqrt(w2).imag)
    return wach, np.where(wach, gam, 0.0), neg, im


def w2_formel(K2, c_spur, Uv, Us, J=1.0, g=1.0):
    """Schreibtisch [M]: omega^2-Spektrum je q (sortiert): g J K^2 (zweimal, TT), J (1 - 2c)(-g K^2 + 2 U_s K^4)
    (T-L-Block), 0 (dreimal). U_v tritt nicht auf."""
    n = K2.shape[0]
    s = J * (1.0 - 2.0 * c_spur) * (-g * K2 + 2.0 * Us * K2 ** 2)
    P = np.stack([g * J * K2, g * J * K2, s, np.zeros(n), np.zeros(n), np.zeros(n)], -1)
    return np.sort(P, -1)


def zerlegung(K1, B1, va, sD):
    """Modenzerlegung des Eigenvektors z = (a, E) der Bewegungsmatrix, a = va, E = -B a / sD, an einem q.
    a-Seite: Skalarbedingung (c-Richtung), Eichung Gl. 15 (Bild G15), Helizitaet 2 (TT).
    E-Seite: Eichrichtung Gl. 23 (G23), Verletzung der Vektorbedingung (Bild Kv^T), Helizitaet 2 (TT)."""
    o = ops(K1[None, :])
    vE = -(B1 @ va) / sD
    c = o['c'][0]
    G23 = o['G23'][0]
    Pc = np.outer(c, c) / (c @ c)
    PG23 = np.outer(G23, G23) / (G23 @ G23)
    PG15 = projektor(o['G15'])[0]
    PKv = projektor(mT(o['Kv']))[0]
    SE, Sa, _, _, _, _ = physraeume(o)
    PTTE = SE[0] @ SE[0].T
    PTTa = Sa[0] @ Sa[0].T

    def w(P, v):
        return float(np.real(np.vdot(v, P @ v)))
    na, nE = w(np.eye(6), va), w(np.eye(6), vE)
    n = na + nE
    a_s = {'skalar': w(Pc, va) / na, 'eich15': w(PG15, va) / na, 'tt': w(PTTa, va) / na}
    E_s = {'eich23': w(PG23, vE) / nE, 'vektor': w(PKv, vE) / nE, 'tt': w(PTTE, vE) / nE}
    ges = {'skalar': w(Pc, va) / n, 'vektor': w(PKv, vE) / n, 'eich': (w(PG15, va) + w(PG23, vE)) / n,
           'tt': (w(PTTa, va) + w(PTTE, vE)) / n}
    ges['summe'] = sum(ges.values())
    ges['f_off'] = float(np.sqrt(max(ges['skalar'] + ges['vektor'], 0.0)))
    a_s['summe'] = sum(a_s.values())
    E_s['summe'] = sum(E_s.values())
    return {'a_seite': a_s, 'E_seite': E_s, 'gesamt': ges, 'E_zu_a_norm': float(np.sqrt(nE / na))}


def frei_scan(q, o, K2, c_spur, Uv, Us, mit_zerlegung=True):
    """Freie lineare Dynamik (wie TENSOR-EIS-N): omega^2 = eig(A B), A mit -c (E^ii)^2."""
    A, B = hesse(o, 'N', Uv=Uv, Us=Us, lam=c_spur)
    s = norm2(A) * norm2(B)
    w2 = np.linalg.eigvals(A @ B)
    wach, gam, neg, im = wachs_test(w2, s)
    gq = gam.max(-1)
    i = int(np.argmax(gq))
    res = {'gamma_max': float(gq[i]), 'anteil_q_wachsend': float(wach.any(-1).mean()),
           'anzahl_q_wachsend': int(wach.any(-1).sum()),
           'neg_rel_max': float(neg.max()), 'im_rel_max': float(im.max()),
           'q_stern': [float(x) for x in q[i]], 'K2_stern': float(K2[i]),
           'anzahl_q_mit_gamma_max': int((np.abs(gq - gq[i]) <= 1e-12 * max(gq[i], 1e-300)).sum()) if gq[i] > 0 else 0}
    pred = w2_formel(K2, c_spur, Uv, Us)
    lat = np.sort(w2.real, -1)
    res['formel_abw_rel_max'] = float((np.abs(lat - pred).max(-1) / s).max())
    if mit_zerlegung and gq[i] > 0:
        wv, V = np.linalg.eig(A[i] @ B[i])
        g1 = np.abs(np.sqrt(wv.astype(complex)).imag)
        j = int(np.argmax(g1))
        sD = np.sqrt(-wv[j].astype(complex))
        z = zerlegung(kvek(q[i]), B[i], V[:, j], sD)
        z['w2'] = [float(wv[j].real), float(wv[j].imag)]
        z['sD'] = [float(sD.real), float(sD.imag)]
        res['zerlegung'] = z
    return res, gq


def zwang_scan(o, Za, ZE, c_spur, Uv, Us):
    """(b) Dynamik orthogonal projiziert auf Z = {a in ker c} x {E in ker Kv} (beide Bedingungen ohne Quelle)."""
    A, B = hesse(o, 'N', Uv=Uv, Us=Us, lam=c_spur)
    M1 = mT(Za) @ A @ ZE          # (n,5,3): d alpha/dt = M1 eps
    M2 = mT(ZE) @ B @ Za          # (n,3,5): d eps/dt = -M2 alpha
    s = norm2(M1) * norm2(M2)
    res = {}
    gmax = np.zeros(A.shape[0])
    for nm, W in (('E', M2 @ M1), ('a', M1 @ M2)):
        w2 = np.linalg.eigvals(W)
        wach, gam, neg, im = wachs_test(w2, s)
        res['w2_' + nm] = {'anzahl_q_wachsend': int(wach.any(-1).sum()), 'neg_rel_max': float(neg.max()),
                           'im_rel_max': float(im.max()), 'gamma_max': float(gam.max())}
        gmax = np.maximum(gmax, gam.max(-1))
    res['gamma_max'] = float(gmax.max())
    res['anzahl_q_wachsend'] = int((gmax > 0).sum())
    n = A.shape[0]
    D = np.zeros((n, 8, 8))
    D[:, :5, 5:] = M1
    D[:, 5:, :5] = -M2
    ev = np.linalg.eigvals(D)
    res['D8_re_max_rel'] = float((ev.real.max(-1) / norm2(D)).max())
    Dv = np.zeros((n, 12, 12))
    Dv[:, :6, 6:] = A
    Dv[:, 6:, :6] = -B
    Q = np.zeros((n, 12, 8))
    Q[:, :6, :5] = Za
    Q[:, 6:, 5:] = ZE
    R = Dv @ Q - Q @ (mT(Q) @ Dv @ Q)
    dz = norm2(R) / norm2(Dv)
    res['invarianz_defekt_rel_max'] = float(dz.max())
    res['invarianz_defekt_rel_min'] = float(dz.min())
    eA = np.linalg.eigvalsh(mT(ZE) @ A @ ZE)
    eB = np.linalg.eigvalsh(mT(Za) @ B @ Za)
    sA = np.abs(np.linalg.eigvalsh(A)).max(-1)
    sB = np.abs(np.linalg.eigvalsh(B)).max(-1)
    res['energie_Z'] = {'A_min_rel': float((eA.min(-1) / sA).min()), 'B_min_rel': float((eB.min(-1) / sB).min()),
                        'A_neg_anteil': float((eA.min(-1) < -1e-9 * sA).mean()),
                        'B_neg_anteil': float((eB.min(-1) < -1e-9 * sB).mean()),
                        'A_min_absolut': float(eA.min())}
    return res, gmax


def dirac_scan(o, Za, ZE, c_spur, Uv, Us, tol=TOL_DIRAC, maxit=8):
    """Gegenprobe: groesster unter der freien Bewegung invarianter Unterraum V* in Z (Dirac-Algorithmus, linear),
    dort die Bewegung exakt eingeschraenkt."""
    A, B = hesse(o, 'N', Uv=Uv, Us=Us, lam=c_spur)
    n = A.shape[0]
    D = np.zeros((n, 12, 12))
    D[:, :6, 6:] = A
    D[:, 6:, :6] = -B
    sk = norm2(D)
    Q = np.zeros((n, 12, 8))
    Q[:, :6, :5] = Za
    Q[:, 6:, 5:] = ZE
    dims = [8]
    einheitlich = True
    for _ in range(maxit):
        d = Q.shape[-1]
        R = D @ Q - Q @ (mT(Q) @ D @ Q)
        _, sv, Vt = np.linalg.svd(R)
        k_q = (sv / sk[:, None] <= tol).sum(-1)
        if not np.all(k_q == k_q[0]):
            einheitlich = False
        k = int(k_q.min())
        if k == d:
            break
        Q = Q @ mT(Vt[:, d - k:, :])
        dims.append(k)
        if k == 0:
            break
    res = {'dims': dims, 'dim': int(Q.shape[-1]), 'einheitlich': einheitlich}
    if Q.shape[-1] > 0:
        Ds = mT(Q) @ D @ Q
        ev = np.linalg.eigvals(Ds)
        ev2 = np.linalg.eigvals(Ds @ Ds)
        sk2 = sk ** 2
        wach = (ev2.real / sk2[:, None] > TAU) | (np.abs(ev2.imag) / sk2[:, None] > TAU)
        gq = np.where(wach.any(-1), ev.real.max(-1), 0.0)
        res.update({'anzahl_q_wachsend': int(wach.any(-1).sum()), 'gamma_max': float(gq.max()),
                    's2_re_max_rel': float((ev2.real / sk2[:, None]).max()),
                    's2_im_max_rel': float((np.abs(ev2.imag) / sk2[:, None]).max()),
                    're_s_max_rel': float((ev.real.max(-1) / sk).max()),
                    'invarianz_rest_rel': float((norm2(D @ Q - Q @ (mT(Q) @ D @ Q)) / sk).max())})
    else:
        res.update({'anzahl_q_wachsend': 0, 'gamma_max': 0.0})
    return res


def statik_voll(K, c_spur, rcond=1e-10):
    """Statik mit vollem H (E- und a-Teil, A mit -c (E^ii)^2) unter Kv E = 0 und c.a = 1, ein 16x16-KKT je q."""
    o = ops(K)
    A, B = hesse(o, 'N', lam=c_spur)
    n = K.shape[:-1]
    M = np.zeros(n + (16, 16))
    M[..., :6, :6] = A
    M[..., 6:12, 6:12] = B
    M[..., 12:15, :6] = o['Kv']
    M[..., :6, 12:15] = mT(o['Kv'])
    M[..., 15, 6:12] = o['c']
    M[..., 6:12, 15] = o['c']
    P = np.linalg.pinv(M, rcond=rcond, hermitian=True)
    x = P[..., :, 15]
    E, a = x[..., :6], x[..., 6:12]
    kap = np.einsum('...a,...ab,...b->...', E, A, E) + np.einsum('...a,...ab,...b->...', a, B, a)
    resE = np.abs(np.einsum('...ja,...a->...j', o['Kv'], E)).max(-1)
    resa = np.einsum('...a,...a->...', o['c'], a) - 1.0
    return kap, np.abs(E).max(-1), resE, resa


def statik_voll_scan(L, nzufall, seed=5):
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    q3 = 2 * np.pi * np.fft.rfftfreq(L)
    qx, qy, qz = np.meshgrid(q1, q1, q3, indexing='ij')
    q = np.stack([qx, qy, qz], -1).reshape(-1, 3)
    q = q[np.any(q != 0, axis=1)]
    rng = np.random.default_rng(seed)
    q = np.concatenate([q, rng.uniform(-np.pi, np.pi, (nzufall, 3))], 0)
    K = kvek(q)
    ref = kern_statik(K, 'N')['kap']
    sk = float(np.abs(ref).max())
    out = {'L': L, 'nzufall': nzufall, 'nq': int(len(q)), 'kap_skala': sk}
    for cn, cs in zip(C_NAMEN, C_LISTE):
        kap, Emax, resE, resa = statik_voll(K, cs)
        out[cn] = {'kap_abw_rel_max': float(np.abs(kap - ref).max() / sk), 'E_max': float(Emax.max()),
                   'resE_max': float(resE.max()), 'resa_max': float(np.abs(resa).max())}
    return out


def linien_scan(nt=160):
    t = np.logspace(-3, np.log10(np.pi), nt)
    out = {'t': t.tolist()}
    for nm, d in (('100', (1, 0, 0)), ('111', (1, 1, 1))):
        dn = np.array(d, float) / np.linalg.norm(d)
        Kl = kvek(t[:, None] * dn)
        ol = ops(Kl)
        K2 = ol['K2']
        z = {'K2': K2.tolist()}
        for S in ('P0', 'P1'):
            Uv, Us = SAETZE[S]
            zz = {}
            for cn, cs in zip(C_NAMEN, C_LISTE):
                A, B = hesse(ol, 'N', Uv=Uv, Us=Us, lam=cs)
                s = norm2(A) * norm2(B)
                w2 = np.linalg.eigvals(A @ B)
                wach, gam, neg, im = wachs_test(w2, s)
                pred = w2_formel(K2, cs, Uv, Us)
                zz[cn] = {'gamma': gam.max(-1).tolist(),
                          'formel_abw_rel_max': float((np.abs(np.sort(w2.real, -1) - pred).max(-1) / s).max())}
            z[S] = zz
        out[nm] = z
    return out


def lauf_scan(L, Ldirac, Lstat, nzufall):
    t0 = time.time()
    q = bz_punkte(L)
    o = ops(kvek(q))
    K2 = o['K2']
    SE, Sa, ZE, Za, _, _ = physraeume(o)
    out = {'L': L, 'nq': int(len(q)), 'c_liste': C_LISTE, 'c_namen': C_NAMEN,
           'lambda_hl': {cn: (None if abs(3 * cs - 1) < 1e-12 else cs / (3 * cs - 1)) for cn, cs in zip(C_NAMEN, C_LISTE)},
           'kontr_Z': {'Kv_ZE_max': float(np.abs(o['Kv'] @ ZE).max()),
                       'c_Za_max': float(np.abs(np.einsum('...a,...ak->...k', o['c'], Za)).max())}}
    iq_min = int(np.argmin(np.abs(q - np.array([2 * np.pi / L, 0.0, 0.0])).sum(-1)))
    out['q_min'] = [float(x) for x in q[iq_min]]
    frei, zwang = {}, {}
    for S, (Uv, Us) in SAETZE.items():
        frei[S] = {}
        if S in ('P0', 'P1'):
            zwang[S] = {}
        for cn, cs in zip(C_NAMEN, C_LISTE):
            r, gq = frei_scan(q, o, K2, cs, Uv, Us, mit_zerlegung=(S in ('P0', 'P1')))
            r['gamma_q_min'] = float(gq[iq_min])
            r['K_q_min'] = float(np.sqrt(K2[iq_min]))
            frei[S][cn] = r
            if S in ('P0', 'P1'):
                zwang[S][cn], _ = zwang_scan(o, Za, ZE, cs, Uv, Us)
        print('scan %s fertig nach %.1f s' % (S, time.time() - t0), flush=True)
    out['frei'] = frei
    out['zwang'] = zwang
    phys = {}
    for cn, cs in zip(C_NAMEN, C_LISTE):
        A, B = hesse(o, 'N', lam=cs)
        Ar = mT(SE) @ A @ SE
        Br = mT(SE) @ B @ SE
        w2 = np.linalg.eigvals(Ar @ Br)
        wach, gam, neg, im = wachs_test(w2, norm2(Ar) * norm2(Br))
        phys[cn] = {'anzahl_q_wachsend': int(wach.any(-1).sum()), 'gamma_max': float(gam.max()),
                    'w2_ueber_K2_min': float((w2.real / K2[:, None]).min()),
                    'w2_ueber_K2_max': float((w2.real / K2[:, None]).max())}
    out['phys'] = phys
    hl = {}
    for S in ('P0', 'P1'):
        Uv, Us = SAETZE[S]
        hl[S] = {}
        for cn, cs in zip(C_NAMEN, C_LISTE):
            w2s = (1 - 2 * cs) * (-K2 + 2 * Us * K2 ** 2)
            hl[S][cn] = {'gamma_max_formel_gitter': float(np.sqrt(np.maximum(0.0, -w2s)).max()),
                         'hl_ir_koeff': float(np.sqrt(max(0.0, 1 - 2 * cs)))}
    out['hl'] = hl
    # Dirac-Gegenprobe
    if Ldirac == L:
        od, Zad, ZEd = o, Za, ZE
    else:
        od = ops(kvek(bz_punkte(Ldirac)))
        _, _, ZEd, Zad, _, _ = physraeume(od)
    dirac = {}
    for S in ('P0', 'P1'):
        Uv, Us = SAETZE[S]
        dirac[S] = {cn: dirac_scan(od, Zad, ZEd, cs, Uv, Us) for cn, cs in zip(C_NAMEN, C_LISTE)}
    out['dirac'] = dirac
    out['Ldirac'] = Ldirac
    print('dirac fertig nach %.1f s' % (time.time() - t0), flush=True)
    out['statik_voll'] = statik_voll_scan(Lstat, nzufall)
    print('statik_voll fertig nach %.1f s' % (time.time() - t0), flush=True)
    out['linien'] = linien_scan()
    out['t_s'] = time.time() - t0
    return out


def kontrolle_ortsraum_c(L=6, c_werte=(0.45, 0.55)):
    """Ortsraum-Spektrum A B (Stencils, np.roll) gegen die Vereinigung der Fourier-Spektren, fuer c != 1/2."""
    t0 = time.time()
    N = L ** 3
    Inc, Q, c = ortsraum_matrizen(L)
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    qx, qy, qz = np.meshgrid(q1, q1, q1, indexing='ij')
    of = ops(kvek(np.stack([qx, qy, qz], -1)).reshape(-1, 3))
    PE = Q.T @ Q
    out = {'L': L}
    for cs in c_werte:
        MJ = np.kron(np.eye(6) - cs * np.outer(TR, TR), np.eye(N))
        for S in ('P0', 'P1'):
            Uv, Us = SAETZE[S]
            A = MJ + Uv * PE
            B = Inc + Us * (c.T @ c)
            w2o = np.linalg.eigvals(A @ B)
            Af, Bf = hesse(of, 'N', Uv=Uv, Us=Us, lam=cs)
            w2f = np.linalg.eigvals(Af @ Bf).reshape(-1)
            ro, rf = np.sort(w2o.real), np.sort(w2f.real)
            out['c%.2f_%s' % (cs, S)] = {'max_abw_real': float(np.abs(ro - rf).max()), 'max_w2': float(np.abs(rf).max()),
                                        'min_w2_ortsraum': float(ro.min()), 'min_w2_fourier': float(rf.min()),
                                        'max_im_ortsraum': float(np.abs(w2o.imag).max()),
                                        'max_im_fourier': float(np.abs(w2f.imag).max())}
    out['t_s'] = time.time() - t0
    return out


def exakt_c_scan(n=6, seed=13):
    """Exakt (Brueche): charakteristisches Polynom der omega^2-Matrix je c gegen x^3 (x - K^2)^2 (x - s),
    s = (1 - 2c)(2 U_s K^4 - K^2) (J = g = 1); Sturm-Zaehlung negativer und nicht reeller Wurzeln."""
    import random
    rnd = random.Random(seed)
    werte = [F(p, qq) for qq in (1, 2, 3, 4, 5, 7) for p in range(-2 * qq, 2 * qq + 1)]
    punkte = []
    while len(punkte) < n:
        K = [rnd.choice(werte) for _ in range(3)]
        if any(k != 0 for k in K):
            punkte.append(K)
    Wi = [F(1), F(1), F(1), F(1, 2), F(1, 2), F(1, 2)]
    out = {'punkte': [[str(k) for k in K] for K in punkte], 'saetze': {}}
    for S, (Uv, Us) in (('P0', (F(0), F(0))), ('P1', (F(1), F(1)))):
        res = {}
        for cn, cf in zip(C_NAMEN, C_EXAKT):
            rows = []
            for K in punkte:
                A, B = hesse_exakt(K, 'N', Uv=Uv, Us=Us, lam=cf)
                Ah = [[Wi[i] * A[i][j] for j in range(6)] for i in range(6)]
                Bh = [[Wi[i] * B[i][j] for j in range(6)] for i in range(6)]
                cp = charpoly(matmul(Ah, Bh))
                K2 = sum(k * k for k in K)
                s = (1 - 2 * cf) * (2 * Us * K2 * K2 - K2)
                erw = [F(0), F(0), F(0), -K2 * K2 * s, 2 * K2 * s + K2 * K2, -(s + 2 * K2), F(1)]
                m0 = next(i for i, x in enumerate(cp) if x != 0)
                sq = poly_trim(cp[m0:])
                deg = len(sq) - 1
                if deg > 0:
                    gg = poly_gcd(sq, poly_deriv(sq))
                    dist = deg - (len(poly_trim(gg)) - 1)
                    reell = sturm_anzahl(sq, '-inf', 'inf')
                    neg = sturm_anzahl(sq, '-inf', F(0))
                else:
                    dist, reell, neg = 0, 0, 0
                rows.append({'gleich_formel': bool(cp == erw), 'null_vielfachheit': m0, 'rest_verschieden': dist,
                             'rest_reell': reell, 'rest_negativ': neg, 's': str(s), 'K2': str(K2)})
            res[cn] = {'alle_gleich_formel': all(r['gleich_formel'] for r in rows),
                       'punkte_mit_negativer_wurzel': sum(1 for r in rows if r['rest_negativ'] > 0),
                       'punkte_mit_nicht_reeller_wurzel': sum(1 for r in rows if r['rest_reell'] < r['rest_verschieden']),
                       'null_vielfachheit': sorted(set(r['null_vielfachheit'] for r in rows)),
                       'zeilen': rows}
        out['saetze'][S] = res
    return out


# ================================================================================================ REGEL-1 (neu)
import itertools
from scipy.linalg import solve_banded, null_space
from scipy.optimize import brentq
from scipy.interpolate import CubicSpline
from scipy.special import erf, erfc

C_REGEL = 0.5            # Spurkoeffizient mit eingebauter Regel (Gl. 23), exakt 1/2
TAU_LAUF = 1e-6          # laufende Mode: omega^2 > TAU_LAUF |M1| |M2| (auf Z)
K_LISTE = (0.025, 0.05, 0.1, 0.2)
LINIEN = {'100': (1, 0, 0), '110': (1, 1, 0), '111': (1, 1, 1)}

# ---- M1, beta = 1/2
BETA = 0.5
OMC2 = 1.0 - 1.0 / (4.0 * BETA)          # 0.5
SIGMA_TW = np.sqrt(2.0) / 4.0
# Bekannte 3D-Werte (RUNDE-02/tests1d/lauf-69/ausgabe/tests1d_bericht.txt, Test 4): omega^2 -> (Q, E)
TABELLE_3D = {0.55: (1.97733e+04, 1.50306e+04), 0.60: (2.87318e+03, 2.33259e+03), 0.70: (4.73413e+02, 4.28641e+02),
              0.80: (1.86110e+02, 1.81912e+02), 0.83: (1.54091e+02, 1.53024e+02), 0.90: (1.15642e+02, 1.17398e+02)}
QMIN_3D = (111.8441, 0.9269)


def U_pot(S):
    return S - S * S + BETA * S ** 3


def dU_pot(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S * S


def d2U_pot(S):
    return -2.0 + 6.0 * BETA * S


class Radial3:
    """3D radial (l = 0), FV-Gitter r_j = (j + 1/2) dr, Dirichlet f = 0 bei r = M dr (wie kegel_q.Radial, Gewicht r^2).
    I = 4 pi dr Sum r^2 f^2, G = 4 pi Sum r_{j+1/2}^2 (f_{j+1} - f_j)^2 / dr, V = 4 pi dr Sum r^2 U(f^2);
    Feldgleichung d/df (G + V - omega^2 I) = 0; Q = 2 omega I, E = omega^2 I + G + V."""

    def __init__(self, dr, rmax):
        self.dr = dr
        self.M = int(round(rmax / dr))
        self.rmax = self.M * dr
        j = np.arange(self.M, dtype=float)
        self.r = (j + 0.5) * dr
        self.rp = (j + 1.0) * dr
        self.rm = j * dr

    def teile(self, f):
        dr = self.dr
        S = f * f
        I = 4 * np.pi * dr * float(np.sum(self.r ** 2 * S))
        fp = np.append(f[1:], 0.0)
        G = 4 * np.pi * float(np.sum(self.rp ** 2 * (fp - f) ** 2)) / dr
        V = 4 * np.pi * dr * float(np.sum(self.r ** 2 * U_pot(S)))
        return I, G, V

    def residuum(self, f, om2):
        fm = np.concatenate(([0.0], f[:-1]))
        fp = np.append(f[1:], 0.0)
        S = f * f
        return (2 * (self.rm ** 2 * (f - fm) - self.rp ** 2 * (fp - f)) / self.dr
                + 2 * self.dr * self.r ** 2 * (dU_pot(S) - om2) * f)

    def rnorm(self, R):
        return float(np.max(np.abs(R / (self.dr * self.r ** 2))))

    def newton(self, f0, om2, tol=1e-10, maxit=80):
        f = f0.copy()
        R = self.residuum(f, om2)
        nr = self.rnorm(R)
        it = 0
        off = -2 * self.rp[:-1] ** 2 / self.dr
        while nr > tol and it < maxit:
            it += 1
            S = f * f
            ab = np.zeros((3, self.M))
            ab[0, 1:] = off
            ab[1, :] = (2 * (self.rm ** 2 + self.rp ** 2) / self.dr
                        + 2 * self.dr * self.r ** 2 * (dU_pot(S) + 2 * S * d2U_pot(S) - om2))
            ab[2, :-1] = off
            df = solve_banded((1, 1), ab, -R)
            t = 1.0
            while True:
                fn = f + t * df
                Rn = self.residuum(fn, om2)
                nn = self.rnorm(Rn)
                if nn < nr or t < 1e-4:
                    break
                t *= 0.5
            f, R, nr = fn, Rn, nn
        return f, it, nr

    def groessen(self, f, om2):
        I, G, V = self.teile(f)
        om = float(np.sqrt(om2))
        S = f * f
        S0 = float(S[0])
        k = int(np.argmax(S < 0.5 * S0))
        r_half = float(self.r[k - 1] + (0.5 * S0 - S[k - 1]) * (self.r[k] - self.r[k - 1]) / (S[k] - S[k - 1]))
        vir = (G + 3 * V - 3 * om2 * I) / (G + 3 * abs(V) + 3 * om2 * I)
        return dict(om2=float(om2), omega=om, Q=2 * om * I, E=om2 * I + G + V, I=I, G=G, V=V, S0=S0, R_half=r_half,
                    kappa_schwanz=float(np.sqrt(1.0 - om2)), virial=float(vir))


def familie3(dr, rmax):
    rad = Radial3(dr, rmax)
    om2_start = 0.62
    R0 = 2.0 * SIGMA_TW / (om2_start - OMC2)
    S = 1.0 / (1.0 + np.exp(np.clip(np.sqrt(2.0) * (rad.r - R0), -700.0, 700.0)))
    f0, it0, nr0 = rad.newton(np.sqrt(S), om2_start)
    if np.max(f0) < 0.05 or nr0 > 1e-8:
        raise RuntimeError('Start der 3D-Familie gescheitert: res %.3e max f %.3e' % (nr0, np.max(f0)))
    ab = [round(om2_start - 0.002 * k, 6) for k in range(1, 41)]        # 0.618 ... 0.540
    auf = [round(om2_start + 0.005 * k, 6) for k in range(1, 62)]       # 0.625 ... 0.925
    erg = {om2_start: (f0, it0, nr0)}
    for folge in (ab, auf):
        f_prev, o_prev, f_pp, o_pp = f0, om2_start, None, None
        for om2 in folge:
            guess = f_prev if f_pp is None else f_prev + (om2 - o_prev) / (o_prev - o_pp) * (f_prev - f_pp)
            f, it, nr = rad.newton(guess, om2)
            if nr > 1e-8 or np.max(f) < 0.05:
                f2, it2, nr2 = rad.newton(f_prev, om2)
                if nr2 < nr and np.max(f2) >= 0.05:
                    f, it, nr = f2, it2, nr2
            erg[om2] = (f, it, nr)
            f_pp, o_pp, f_prev, o_prev = f_prev, o_prev, f, om2
    fam = []
    for om2 in sorted(erg):
        f, it, nr = erg[om2]
        g = rad.groessen(f, om2)
        g['newton_it'] = it
        g['res'] = nr
        fam.append((g, f))
    return rad, fam


def loese_Q3(rad, fam, Qt):
    """Profil mit Ladung Qt auf dem VK-stabilen Ast (dQ/d omega^2 < 0), erste Klammer von kleinem omega^2 her."""
    a = None
    for k in range(len(fam) - 1):
        Qa, Qb = fam[k][0]['Q'], fam[k + 1][0]['Q']
        if (Qa - Qt) * (Qb - Qt) <= 0 and Qb < Qa:
            a = k
            break
    if a is None:
        raise RuntimeError('Ladung %.6f nicht im stabilen Ast der 3D-Familie' % Qt)
    ref = [fam[a][1]]

    def F(om2):
        f, it, nr = rad.newton(ref[0], om2)
        ref[0] = f
        return rad.groessen(f, om2)['Q'] - Qt

    om2 = brentq(F, fam[a][0]['om2'], fam[a + 1][0]['om2'], xtol=1e-15, rtol=1e-14, maxiter=200)
    f, it, nr = rad.newton(ref[0], om2)
    g = rad.groessen(f, om2)
    g['res'] = nr
    g['dQdom2_fam'] = (fam[a + 1][0]['Q'] - fam[a][0]['Q']) / (fam[a + 1][0]['om2'] - fam[a][0]['om2'])
    return g, f


def qball(rad, fam, Qt, r_cut):
    """Ball mit Ladung Qt: Kenngroessen und Spline von f (f'(0) = 0 per Spiegelung, f(rmax) = 0)."""
    g, f = loese_Q3(rad, fam, Qt)
    k = 8
    rr = np.concatenate([-rad.r[:k][::-1], rad.r, [rad.rmax]])
    ff = np.concatenate([f[:k][::-1], f, [0.0]])
    sp = CubicSpline(rr, ff)
    r = rad.r
    S = f * f
    rE = g['om2'] * S + sp(r, 1) ** 2 + U_pot(S)
    w = 4 * np.pi * rad.dr * r ** 2
    g['N'] = g['I']
    g['E_spline'] = float(np.sum(w * rE))
    g['m2_E'] = float(np.sum(w * rE * r ** 2) / np.sum(w * rE))
    g['m2_N'] = float(np.sum(w * S * r ** 2) / np.sum(w * S))
    aus = r > r_cut
    g['anteil_jenseits_rcut_E'] = float(np.sum((w * rE)[aus]) / np.sum(w * rE))
    g['anteil_jenseits_rcut_N'] = float(np.sum((w * S)[aus]) / np.sum(w * S))
    g['E_durch_Q'] = g['E'] / Qt
    g['N_durch_E'] = g['N'] / g['E']
    g['f2_bei_rcut_rel'] = float(sp(min(r_cut, rad.rmax)) ** 2 / g['S0'])
    return g, sp


def dichten_radial(sp, om2, rho, rmax, r_cut):
    rr = np.minimum(rho, rmax)
    f = sp(rr)
    fp = sp(rr, 1)
    aus = (rho > r_cut) | (rho >= rmax)
    f = np.where(aus, 0.0, f)
    fp = np.where(aus, 0.0, fp)
    S = f * f
    return om2 * S + fp * fp + U_pot(S), S


_R3_CACHE = {}


def r3_vielfachheit(nmax2, ne):
    """Anzahl der Gitterpunkte x in Z^3 mit |x_i| <= ne und x.x = n, fuer n = 0..nmax2 (exakt per Faltung)."""
    if (nmax2, ne) in _R3_CACHE:
        return _R3_CACHE[(nmax2, ne)]
    _R3_CACHE[(nmax2, ne)] = _r3(nmax2, ne)
    return _R3_CACHE[(nmax2, ne)]


def _r3(nmax2, ne):
    s = np.zeros(nmax2 + 1)
    for x in range(-ne, ne + 1):
        if x * x <= nmax2:
            s[x * x] += 1
    r2 = np.convolve(s, s)[:nmax2 + 1]
    return np.convolve(r2, s)[:nmax2 + 1]


def gitter_summen(sp, om2, h, r_cut, rmax):
    """Gittersummen h^3 Sum rho(h|x|) ueber |x| <= r_cut/h (Kugelschnitt), dazu zweite Momente (Gittereinheiten)."""
    ne = int(np.floor(r_cut / h))
    n2max = ne * ne
    mult = r3_vielfachheit(n2max, ne)
    n = np.arange(n2max + 1, dtype=float)
    rho = h * np.sqrt(n)
    rE, S = dichten_radial(sp, om2, rho, rmax, r_cut)
    sE = float(np.sum(mult * rE)) * h ** 3
    sN = float(np.sum(mult * S)) * h ** 3
    m2E = float(np.sum(mult * rE * n) / np.sum(mult * rE))
    m2N = float(np.sum(mult * S * n) / np.sum(mult * S))
    return dict(h=h, ne=ne, E_gitter=sE, N_gitter=sN, m2_E_gitter=m2E, m2_N_gitter=m2N)


def ball_box(sp, om2, h, r_cut, rmax):
    ne = int(np.floor(r_cut / h))
    x = np.arange(-ne, ne + 1, dtype=float)
    r2 = x[:, None, None] ** 2 + x[None, :, None] ** 2 + x[None, None, :] ** 2
    rE, S = dichten_radial(sp, om2, h * np.sqrt(r2), rmax, r_cut)
    return rE * h ** 3, S * h ** 3, r2, ne


def einbetten(box, ne, L):
    if 2 * ne + 1 > L:
        raise ValueError('Ball (2 ne + 1 = %d) groesser als der Torus L = %d' % (2 * ne + 1, L))
    arr = np.zeros((L, L, L))
    idx = np.arange(-ne, ne + 1) % L
    arr[np.ix_(idx, idx, idx)] = box
    return arr


def kern_gitter(L, chunk):
    """Statischer Kern kappa(q) je q per 7x7-KKT (kern_statik, wie TENSOR-EIS-N), rfft-Gitter; Vergleich mit -g/(2K^2)."""
    t0 = time.time()
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    q3 = 2 * np.pi * np.fft.rfftfreq(L)
    kap = np.empty((L, L, len(q3)))
    abw = 0.0
    res_max = 0.0
    for i0 in range(0, L, chunk):
        qx, qy, qz = np.meshgrid(q1[i0:i0 + chunk], q1, q3, indexing='ij')
        K = kvek(np.stack([qx, qy, qz], -1))
        o = kern_statik(K, 'N')
        kap[i0:i0 + chunk] = o['kap']
        null = (qx == 0) & (qy == 0) & (qz == 0)
        K2 = (K * K).sum(-1)
        formel = np.where(null, 0.0, -0.5 / np.where(null, 1.0, K2))
        rel = np.where(null, np.abs(o['kap']), np.abs(o['kap'] / np.where(null, 1.0, formel) - 1.0))
        abw = max(abw, float(rel.max()))
        res_max = max(res_max, float(np.where(null, 0.0, np.abs(o['res'])).max()))
    return kap, {'L': L, 'formel_rel_abw_max': abw, 'zwang_res_max': res_max, 'kap_q0': float(kap[0, 0, 0]),
                 't_s': time.time() - t0}


def linien_werte(F, L, nmax):
    n = np.arange(nmax + 1)
    return {nm: F[(n * e[0]) % L, (n * e[1]) % L, (n * e[2]) % L].tolist() for nm, e in LINIEN.items()}


def ewald_W(P, L, alpha_fak=8.0, mmax=16, nreal=2):
    """W(r) = G_per(r) - 1/(4 pi r): periodisches Kontinuum (Kante L, neutralisiert, q = 0 ausgelassen) minus freier Kern,
    in Gittereinheiten; Ewald mit alpha = alpha_fak/L. W(0) endlich."""
    P = np.asarray(P, float).reshape(-1, 3)
    a = alpha_fak / L
    V = float(L) ** 3
    r0 = np.linalg.norm(P, axis=1)
    W = np.where(r0 > 0, -erf(a * r0) / (4 * np.pi * np.where(r0 > 0, r0, 1.0)), -2 * a / (4 * np.pi * np.sqrt(np.pi)))
    for n in itertools.product(range(-nreal, nreal + 1), repeat=3):
        if n == (0, 0, 0):
            continue
        d = np.linalg.norm(P + L * np.array(n, float), axis=1)
        W = W + erfc(a * d) / (4 * np.pi * d)
    m = np.arange(-mmax, mmax + 1)
    Mg = np.stack(np.meshgrid(m, m, m, indexing='ij'), -1).reshape(-1, 3)
    Mg = Mg[np.any(Mg != 0, axis=1)]
    k = 2 * np.pi * Mg / L
    k2 = (k * k).sum(1)
    w = np.exp(-k2 / (4 * a * a)) / k2
    for i0 in range(0, len(P), 32):
        W[i0:i0 + 32] += (np.cos(P[i0:i0 + 32] @ k.T) @ w) / V
    return W - 1.0 / (4 * a * a * V)


# ------------------------------------------------------------------------------------------------ Teil 1: Wellen
def moden_Z(o, Za, ZE, A, B):
    """Bewegung auf Z (bei c = 1/2 invariant): M1 = Za^T A ZE (5x3), M2 = ZE^T B Za (3x5); omega^2 = eig(M2 M1) (3x3).
    Laufend: Re omega^2 > TAU_LAUF s, s = |M1||M2|. Wachstum: -Re > TAU s oder |Im| > TAU s."""
    M1 = mT(Za) @ A @ ZE
    M2 = mT(ZE) @ B @ Za
    s = norm2(M1) * norm2(M2)
    w2, V = np.linalg.eig(M2 @ M1)
    lauf = (w2.real > TAU_LAUF * s[:, None])
    wach = (-w2.real > TAU * s[:, None]) | (np.abs(w2.imag) > TAU * s[:, None])
    null = np.abs(w2) <= TAU_LAUF * s[:, None]
    n = len(s)
    j0 = np.argmin(np.abs(w2), -1)
    v0 = V[np.arange(n), :, j0]
    e6 = np.einsum('nak,nk->na', ZE, v0)
    G23 = o['G23']
    ov = (np.abs(np.einsum('na,na->n', e6.conj(), G23)) ** 2
          / (np.einsum('na,na->n', e6.conj(), e6).real * (G23 * G23).sum(-1)))
    nullG15 = norm2(M2 @ mT(Za) @ o['G15']) / (norm2(M2) * norm2(o['G15']))
    sv = np.linalg.svd(M2, compute_uv=False)
    w2s = np.sort(w2.real, -1)[:, ::-1]
    return {'n_lauf': lauf.sum(-1), 'n_null': null.sum(-1), 'wach': wach.any(-1), 'w2': w2s, 's': s,
            'null_E_anteil_G23': ov, 'null_a_G15_rest': nullG15, 'M2_sv_min3': sv[:, -1] / norm2(M2),
            'neg_rel': (-w2.real / s[:, None]).max(-1), 'im_rel': (np.abs(w2.imag) / s[:, None]).max(-1)}


def invarianz(o, ZE, SE, A):
    """Invarianzdefekt der kinetischen Energie unter Gl. 23 auf ker Kv: |ZE^T A G23| / (|A| |G23|); dazu der
    quadratische Term und die TT-Identitaet |E|^2 - c (E^ii)^2 = |E_TT|^2 auf ker Kv."""
    G23 = o['G23']
    AG = np.einsum('...ab,...b->...a', A, G23)
    proj = np.einsum('...ak,...a->...k', ZE, AG)
    nG = np.linalg.norm(G23, axis=-1)
    nA = norm2(A)
    lin = np.linalg.norm(proj, axis=-1) / (nA * nG)
    quad = np.abs(np.einsum('...a,...a->...', G23, AG)) / (nA * nG ** 2)
    PT = SE @ mT(SE)
    tt = norm2(mT(ZE) @ (A - PT) @ ZE) / nA
    return lin, quad, tt


def richtungen(nfib=100):
    i = np.arange(nfib) + 0.5
    th = np.arccos(1 - 2 * i / nfib)
    ph = np.pi * (1 + 5 ** 0.5) * i
    D = np.stack([np.cos(ph) * np.sin(th), np.sin(ph) * np.sin(th), np.cos(th)], -1)
    spez = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]], float)
    spez /= np.linalg.norm(spez, axis=1, keepdims=True)
    return np.concatenate([D, spez], 0)


def lauf_wellen(L, nfib):
    t0 = time.time()
    out = {'L': L, 'c': C_REGEL, 'Uv': 0.0, 'Us': 0.0}
    q = bz_punkte(L)
    o = ops(kvek(q))
    SE, Sa, ZE, Za, _, _ = physraeume(o)
    A, B = hesse(o, 'N', lam=C_REGEL)
    lin, quad, tt = invarianz(o, ZE, SE, A)
    out['invarianz_bz'] = {'lin_max': float(lin.max()), 'quad_max': float(quad.max()), 'tt_identitaet_max': float(tt.max()),
                           'nq': int(len(q))}
    kontrast = {}
    for cc in (0.45, 0.55):
        Ac, _ = hesse(o, 'N', lam=cc)
        l2, q2, t2 = invarianz(o, ZE, SE, Ac)
        kontrast['%.2f' % cc] = {'lin_max': float(l2.max()), 'lin_min': float(l2.min()), 'quad_max': float(q2.max()),
                                 'tt_identitaet_max': float(t2.max())}
    out['invarianz_kontrast'] = kontrast
    m = moden_Z(o, Za, ZE, A, B)
    out['moden_bz'] = {'n_lauf_werte': sorted(set(int(x) for x in m['n_lauf'])),
                       'anzahl_q_nicht_2': int((m['n_lauf'] != 2).sum()),
                       'n_null_werte': sorted(set(int(x) for x in m['n_null'])),
                       'anzahl_q_wachsend': int(m['wach'].sum()),
                       'neg_rel_max': float(m['neg_rel'].max()), 'im_rel_max': float(m['im_rel'].max()),
                       'null_E_anteil_G23_min': float(m['null_E_anteil_G23'].min()),
                       'null_a_G15_rest_max': float(m['null_a_G15_rest'].max()),
                       'M2_sv_min3_max': float(m['M2_sv_min3'].max()),
                       'w2_lauf_ueber_K2_min': float((m['w2'][:, :2] / o['K2'][:, None]).min()),
                       'w2_lauf_ueber_K2_max': float((m['w2'][:, :2] / o['K2'][:, None]).max()),
                       'w2_rest_rel_max': float((np.abs(m['w2'][:, 2]) / m['s']).max()),
                       'w2_lauf_rel_min': float((m['w2'][:, 1] / m['s']).min())}
    zw, _ = zwang_scan(o, Za, ZE, C_REGEL, 0.0, 0.0)
    out['zwang_projektion'] = zw
    out['zwang_dirac'] = dirac_scan(o, Za, ZE, C_REGEL, 0.0, 0.0)
    print('wellen: BZ fertig nach %.1f s' % (time.time() - t0), flush=True)
    D = richtungen(nfib)
    out['richtungen'] = D.tolist()
    rk = {}
    for kk in K_LISTE:
        qd = kk * D
        od = ops(kvek(qd))
        SEd, Sad, ZEd, Zad, _, _ = physraeume(od)
        Ad, Bd = hesse(od, 'N', lam=C_REGEL)
        md = moden_Z(od, Zad, ZEd, Ad, Bd)
        l2, q2, t2 = invarianz(od, ZEd, SEd, Ad)
        rk['%g' % kk] = {'w2': md['w2'].tolist(), 'n_lauf': md['n_lauf'].tolist(), 'wach': md['wach'].tolist(),
                         'K2': od['K2'].tolist(), 'inv_lin_max': float(l2.max()),
                         'null_E_anteil_G23_min': float(md['null_E_anteil_G23'].min())}
    out['richtungs_k'] = rk
    t = np.logspace(-2, np.log10(np.pi), 90)
    lin_d = {'t': t.tolist()}
    for nm, e in LINIEN.items():
        dn = np.array(e, float) / np.linalg.norm(e)
        ol = ops(kvek(t[:, None] * dn))
        SEl, Sal, ZEl, Zal, _, _ = physraeume(ol)
        Al, Bl = hesse(ol, 'N', lam=C_REGEL)
        ml = moden_Z(ol, Zal, ZEl, Al, Bl)
        lin_d[nm] = {'w2': ml['w2'].tolist(), 'K2': ol['K2'].tolist(), 'n_lauf': ml['n_lauf'].tolist()}
    out['linien'] = lin_d
    out['t_s'] = time.time() - t0
    return out


# ------------------------------------------------------------------------------------------------ Teil 2/3: Statik
BALL_NAMEN = ('k', 'g', 's')     # klein, gross, schwer


def lauf_statik_q(Ls, h, Qs, r_cut, dr, rmax, chunk):
    t0 = time.time()
    rad, fam = familie3(dr, rmax)
    out = {'h': h, 'Q': dict(zip(BALL_NAMEN, Qs)), 'r_cut': r_cut, 'dr': dr, 'rmax': rmax, 'baelle': {}, 'L': {}}
    boxen = {}
    for nm, Qt in zip(BALL_NAMEN, Qs):
        g, sp = qball(rad, fam, Qt, r_cut)
        rE, N, r2, ne = ball_box(sp, g['om2'], h, r_cut, rad.rmax)
        sE, sN = float(rE.sum()), float(N.sum())
        g.update({'E_gitter': sE, 'N_gitter': sN, 'm2_E_gitter': float((rE * r2).sum() / sE),
                  'm2_N_gitter': float((N * r2).sum() / sN), 'ne': ne, 'R_half_gitter': g['R_half'] / h,
                  'E_gitter_rel_abw': sE / g['E'] - 1.0, 'N_gitter_rel_abw': sN / g['N'] - 1.0})
        out['baelle'][nm] = g
        boxen[nm] = (rE, N, ne)
    print('statik: Baelle fertig nach %.1f s' % (time.time() - t0), flush=True)
    for L in Ls:
        kap, kst = kern_gitter(L, chunk)
        res = {'kern': kst, 'imag_rel': {}}
        print('statik L=%d: Kern fertig nach %.1f s' % (L, time.time() - t0), flush=True)
        spec = {}
        for nm in BALL_NAMEN:
            rE, N, ne = boxen[nm]
            for dn, Dd in (('E', rE), ('N', N)):
                F = np.fft.rfftn(einbetten(Dd, ne, L))
                spec[(nm, dn)] = F.real.copy()
                res['imag_rel'][nm + dn] = float(np.abs(F.imag).max() / np.abs(F.real).max())
                del F
        nmax = L // 2 - 1
        lin = {'punkt': linien_werte(np.fft.irfftn(kap, s=(L, L, L)), L, nmax)}
        for a, b in (('k', 'g'), ('g', 'g'), ('k', 'k'), ('k', 's'), ('g', 's')):
            for dn in ('E', 'N'):
                Fld = np.fft.irfftn(kap * spec[(a, dn)] * spec[(b, dn)], s=(L, L, L))
                lin[a + b + dn] = linien_werte(Fld, L, nmax)
                del Fld
        del spec
        W = {}
        for nm, e in LINIEN.items():
            P = np.arange(nmax + 1)[:, None] * np.array(e, float)[None, :]
            W[nm] = ewald_W(P, L).tolist()
        Wpr = ewald_W(np.array([[2.0, 0, 0], [16.0, 0, 0], [40.0, 0, 0], [30.0, 30.0, 0]]), L)
        Wpr2 = ewald_W(np.array([[2.0, 0, 0], [16.0, 0, 0], [40.0, 0, 0], [30.0, 30.0, 0]]), L, alpha_fak=6.0, mmax=12)
        res['ewald_alpha_abw_max'] = float(np.abs(Wpr - Wpr2).max())
        res['linien'] = lin
        res['W'] = W
        res['nmax'] = nmax
        out['L'][str(L)] = res
        del kap
        print('statik L=%d fertig nach %.1f s' % (L, time.time() - t0), flush=True)
    out['t_s'] = time.time() - t0
    return out


# ------------------------------------------------------------------------------------------------ Modus radial
def lauf_radial(Qs, r_cut, dr, rmax, h_liste):
    t0 = time.time()
    out = {'Q': list(Qs), 'r_cut': r_cut, 'dr': [dr, dr / 2], 'tabelle_3d': {str(k): v for k, v in TABELLE_3D.items()}}
    erg = {}
    for d in (dr, dr / 2):
        rad, fam = familie3(d, rmax)
        tab = [g for g, f in fam]
        dev = []
        for k in range(1, len(tab) - 1):
            dEdQ = (tab[k + 1]['E'] - tab[k - 1]['E']) / (tab[k + 1]['Q'] - tab[k - 1]['Q'])
            dev.append(abs(dEdQ / tab[k]['omega'] - 1.0))
        kmin = int(np.argmin([g['Q'] for g in tab]))
        vergleich = {}
        for om2, (Qr, Er) in TABELLE_3D.items():
            hit = [g for g in tab if abs(g['om2'] - om2) < 1e-9]
            if hit:
                vergleich[str(om2)] = {'Q': hit[0]['Q'], 'E': hit[0]['E'], 'Q_rel_abw': hit[0]['Q'] / Qr - 1.0,
                                       'E_rel_abw': hit[0]['E'] / Er - 1.0}
        baelle = {}
        for nm, Qt in zip(BALL_NAMEN, Qs):
            g, sp = qball(rad, fam, Qt, r_cut)
            gp, _ = loese_Q3(rad, fam, Qt * 1.001)
            gm, _ = loese_Q3(rad, fam, Qt * 0.999)
            g['dEdQ_rel_abw'] = (gp['E'] - gm['E']) / (0.002 * Qt) / g['omega'] - 1.0
            g['aufloesung'] = [gitter_summen(sp, g['om2'], hh, r_cut, rad.rmax) for hh in h_liste]
            for a_ in g['aufloesung']:
                a_['E_rel_abw'] = a_['E_gitter'] / g['E'] - 1.0
                a_['N_rel_abw'] = a_['N_gitter'] / g['N'] - 1.0
                a_['R_half_durch_h'] = g['R_half'] / a_['h']
            prof_r = np.linspace(0, min(r_cut, rad.rmax), 401)
            rE, S = dichten_radial(sp, g['om2'], prof_r, rad.rmax, r_cut)
            g['profil'] = {'r': prof_r.tolist(), 'rhoE': rE.tolist(), 'f2': S.tolist()}
            baelle[nm] = g
        erg['dr=%g' % d] = {'familie': [{k: g[k] for k in ('om2', 'Q', 'E', 'R_half', 'S0', 'res', 'virial')} for g in tab],
                            'dEdQ_max_rel_abw': float(max(dev)), 'Q_min': tab[kmin]['Q'], 'om2_Q_min': tab[kmin]['om2'],
                            'virial_max': float(max(abs(g['virial']) for g in tab)),
                            'res_max': float(max(g['res'] for g in tab)), 'vergleich_tabelle': vergleich, 'baelle': baelle}
        print('radial dr=%g fertig nach %.1f s' % (d, time.time() - t0), flush=True)
    out['ergebnisse'] = erg
    a, b = erg['dr=%g' % dr]['baelle'], erg['dr=%g' % (dr / 2)]['baelle']
    out['dr_probe'] = {nm: {k: b[nm][k] / a[nm][k] - 1.0 for k in ('E', 'N', 'R_half', 'om2')} for nm in BALL_NAMEN}
    out['t_s'] = time.time() - t0
    return out


# ------------------------------------------------------------------------------------------------ Modus kontrolle
def g23_ort(f0):
    """Gl. 23 im Ortsraum: Orthonormal-Koeffizienten von (delta_ij d^2 - d_i d_j) f0, f0 auf den Knoten."""
    nul = (0., 0., 0.)
    d2 = []
    for m in range(3):
        g1, o1 = ableitung(f0, m, nul)
        g2, o2 = ableitung(g1, m, o1)
        assert np.allclose(o2, nul)
        d2.append(g2)
    out = np.zeros((6,) + f0.shape)
    for al, (i, j) in enumerate(IJ):
        if i == j:
            out[al] = sum(d2[m] for m in range(3) if m != i)
        else:
            g1, o1 = ableitung(f0, i, nul)
            g2, o2 = ableitung(g1, j, o1)
            assert np.allclose(o2, OFF[al]), (i, j, o2)
            out[al] = -g2 / S2
    return out


def kontrolle_invarianz_ort(L, mats):
    Inc, Q, cm = mats
    N = L ** 3
    G = np.zeros((6 * N, N))
    for n in range(N):
        f0 = np.zeros(N)
        f0[n] = 1.0
        G[:, n] = g23_ort(f0.reshape(L, L, L)).reshape(-1)
    Z = null_space(Q, rcond=1e-10)
    out = {'L': L, 'dim_ker_div': int(Z.shape[1]), 'div_G23_rel': float(np.linalg.norm(Q @ G, 2) / (np.linalg.norm(Q, 2) * np.linalg.norm(G, 2))),
           'c_plus_GT_rel': float(np.abs(cm + G.T).max() / np.abs(cm).max()),
           'c_minus_GT_rel': float(np.abs(cm - G.T).max() / np.abs(cm).max())}
    for cc in (0.5, 0.45, 0.55):
        MJ = np.kron(np.eye(6) - cc * np.outer(TR, TR), np.eye(N))
        out['defekt_c%.2f' % cc] = float(np.linalg.norm(Z.T @ MJ @ G, 2) / (np.linalg.norm(MJ, 2) * np.linalg.norm(G, 2)))
    return out


def kontrolle_statik_ort(L, mats, seed=21):
    """Statische Zwei-Quellen-Loesung im Ortsraum (KKT mit Stencils, Quellen neutralisiert) gegen die Kreuzkorrelation."""
    Inc, Q, cm = mats
    N = L ** 3
    M = np.zeros((7 * N, 7 * N))
    M[:6 * N, :6 * N] = Inc
    M[:6 * N, 6 * N:] = cm.T
    M[6 * N:, :6 * N] = cm
    Mp = np.linalg.pinv(M, rcond=1e-10, hermitian=True)

    def energie(rho):
        rho = rho - rho.mean()
        x = (Mp @ np.concatenate([np.zeros(6 * N), rho.reshape(-1)]))[:6 * N]
        return 0.5 * x @ Inc @ x
    rng = np.random.default_rng(seed)
    r1 = np.zeros((L, L, L))
    r1[:2, :2, :2] = rng.uniform(0.2, 1.0, (2, 2, 2))
    r2 = np.zeros((L, L, L))
    r2[:2, :3, :2] = rng.uniform(0.2, 1.0, (2, 3, 2))
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    qx, qy, qz = np.meshgrid(q1, q1, q1, indexing='ij')
    kap = kern_statik(kvek(np.stack([qx, qy, qz], -1)), 'N')['kap']
    Uf = np.fft.ifftn(kap * np.fft.fftn(r1) * np.conj(np.fft.fftn(r2))).real
    zeilen = []
    for s in [(2, 0, 0), (3, 0, 0), (1, 2, 0), (2, 2, 2), (3, 1, 2)]:
        r2s = np.roll(r2, s, axis=(0, 1, 2))
        U_ort = energie(r1 + r2s) - energie(r1) - energie(r2s)
        zeilen.append({'s': list(s), 'U_ort': float(U_ort), 'U_fourier': float(Uf[s])})
    out = {'L': L, 'asymmetrisch': zeilen, 'asym_max_abw': max(abs(z['U_ort'] - z['U_fourier']) for z in zeilen)}
    # symmetrischer Pfad wie im Hauptlauf (rfftn, Realteil, irfftn, linien_werte): kleiner Kugelball
    box = np.zeros((5, 5, 5))
    x = np.arange(-2, 3)
    r2b = x[:, None, None] ** 2 + x[None, :, None] ** 2 + x[None, None, :] ** 2
    box = np.exp(-0.7 * r2b)
    box2 = np.exp(-0.4 * r2b) * (r2b <= 4)
    kap_r, _ = kern_gitter(L, L)
    A1 = np.fft.rfftn(einbetten(box, 2, L)).real
    A2 = np.fft.rfftn(einbetten(box2, 2, L)).real
    lin = linien_werte(np.fft.irfftn(kap_r * A1 * A2, s=(L, L, L)), L, L // 2)
    zeilen = []
    for nm, e in LINIEN.items():
        for n in range(1, L // 2 + 1):
            b1 = einbetten(box, 2, L)
            b2 = np.roll(einbetten(box2, 2, L), (n * e[0], n * e[1], n * e[2]), axis=(0, 1, 2))
            U_ort = energie(b1 + b2) - energie(b1) - energie(b2)
            zeilen.append({'linie': nm, 'n': n, 'U_ort': float(U_ort), 'U_pfad': float(lin[nm][n])})
    out['symmetrisch'] = zeilen
    out['sym_max_abw'] = max(abs(z['U_ort'] - z['U_pfad']) for z in zeilen)
    out['skala'] = max(abs(z['U_ort']) for z in zeilen)
    return out


def kontrolle_zeit(L, mats, dt=0.05, T_regel=200.0, T_kontrast=20.0, seed=3):
    """Zeitentwicklung (Leapfrog, Stencil-Matrizen) mit Anfangsdaten auf Z; c = 1/2 und Kontrast c = 0,45."""
    import scipy.sparse as sps
    Inc, Q, cm = mats
    N = L ** 3
    Bs = sps.csr_matrix(np.where(np.abs(Inc) > 1e-14, Inc, 0.0))
    Pc = cm.T @ np.linalg.pinv(cm @ cm.T, rcond=1e-12, hermitian=True)
    PQ = Q.T @ np.linalg.pinv(Q @ Q.T, rcond=1e-12, hermitian=True)
    rng = np.random.default_rng(seed)
    a0 = rng.standard_normal(6 * N)
    a0 = a0 - Pc @ (cm @ a0)
    E0 = rng.standard_normal(6 * N)
    E0 = E0 - PQ @ (Q @ E0)
    out = {'L': L, 'dt': dt, 'start_c_a': float(np.abs(cm @ a0).max()), 'start_div_E': float(np.abs(Q @ E0).max())}
    for cc, Tend in ((0.5, T_regel), (0.45, T_kontrast)):
        As = sps.kron(sps.csr_matrix(np.eye(6) - cc * np.outer(TR, TR)), sps.identity(N), format='csr')
        a = a0.copy()
        E = E0 - 0.5 * dt * (Bs @ a)
        nst = int(round(Tend / dt))
        jede = max(1, nst // 200)
        H0 = 0.5 * E0 @ (As @ E0) + 0.5 * a0 @ (Bs @ a0)
        R0 = np.linalg.norm(Bs @ a0)
        rows = []
        for n in range(1, nst + 1):
            a = a + dt * (As @ E)
            Ba = Bs @ a
            E = E - dt * Ba
            if n % jede == 0 or n == nst:
                Ei = E + 0.5 * dt * Ba
                H = 0.5 * Ei @ (As @ Ei) + 0.5 * a @ Ba
                rows.append({'t': n * dt, 'c_a_max': float(np.abs(cm @ a).max()), 'div_E_max': float(np.abs(Q @ Ei).max()),
                             'H_rel': float(H / H0 - 1.0), 'R_rel': float(np.linalg.norm(Ba) / R0),
                             'a_rel': float(np.linalg.norm(a) / np.linalg.norm(a0)), 'E_rel': float(np.linalg.norm(Ei) / np.linalg.norm(E0))})
        out['c%.2f' % cc] = {'T': Tend, 'H0': float(H0), 'zeilen': rows,
                             'c_a_max': max(r['c_a_max'] for r in rows), 'div_E_max': max(r['div_E_max'] for r in rows),
                             'H_rel_max': max(abs(r['H_rel']) for r in rows), 'R_rel_max': max(r['R_rel'] for r in rows),
                             'E_rel_max': max(r['E_rel'] for r in rows), 'a_rel_ende': rows[-1]['a_rel']}
    return out


def kontrolle_voll(nz=3000, seed=9):
    """Voller 16x16-KKT (E- und a-Teil, c = 1/2, Kv E = 0, c.a = 1) gegen den 7x7-Kern an Zufalls-q."""
    rng = np.random.default_rng(seed)
    K = kvek(rng.uniform(-np.pi, np.pi, (nz, 3)))
    kap_v, Emax, resE, resa = statik_voll(K, C_REGEL)
    kap = kern_statik(K, 'N')['kap']
    return {'nq': nz, 'kap_rel_abw_max': float(np.abs(kap_v - kap).max() / np.abs(kap).max()),
            'E_max_rel': float(Emax.max() / np.abs(kap).max()), 'resE_max': float(resE.max()), 'resa_max': float(np.abs(resa).max())}


def lauf_kontrolle(Lort, Lzeit):
    t0 = time.time()
    out = {}
    mats = ortsraum_matrizen(Lort)
    out['invarianz_ort'] = kontrolle_invarianz_ort(Lort, mats)
    print('kontrolle: invarianz_ort %.1f s' % (time.time() - t0), flush=True)
    out['statik_ort'] = kontrolle_statik_ort(Lort, mats)
    print('kontrolle: statik_ort %.1f s' % (time.time() - t0), flush=True)
    mz = ortsraum_matrizen(Lzeit)
    out['zeit'] = kontrolle_zeit(Lzeit, mz)
    print('kontrolle: zeit %.1f s' % (time.time() - t0), flush=True)
    out['voll'] = kontrolle_voll()
    out['t_s'] = time.time() - t0
    return out


# ------------------------------------------------------------------------------------------------ main
def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['radial', 'wellen', 'statik', 'kontrolle'])
    ap.add_argument('--L', type=int, action='append')
    ap.add_argument('--chunk', type=int, default=2)
    ap.add_argument('--h', type=float, default=0.5)
    ap.add_argument('--Q', default='150,500,5000')
    ap.add_argument('--rcut', type=float, default=40.0)
    ap.add_argument('--dr', type=float, default=0.005)
    ap.add_argument('--rmax', type=float, default=60.0)
    ap.add_argument('--nfib', type=int, default=100)
    ap.add_argument('--Lort', type=int, default=6)
    ap.add_argument('--Lzeit', type=int, default=8)
    ap.add_argument('--hliste', default='1.0,0.75,0.5,0.25')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__))}
    try:
        import scipy
        info['scipy'] = scipy.__version__
    except Exception as ex:
        info['scipy'] = 'FEHLT: %r' % (ex,)
    Qs = [float(x) for x in a.Q.split(',')]
    if a.modus == 'radial':
        res = {'info': info, 'radial': lauf_radial(Qs, a.rcut, a.dr, a.rmax, [float(x) for x in a.hliste.split(',')])}
    elif a.modus == 'wellen':
        res = {'info': info, 'wellen': lauf_wellen(a.L[0] if a.L else 32, a.nfib)}
    elif a.modus == 'statik':
        res = {'info': info, 'statik': lauf_statik_q(a.L, a.h, Qs, a.rcut, a.dr, a.rmax, a.chunk)}
    else:
        res = {'info': info, 'kontrolle': lauf_kontrolle(a.Lort, a.Lzeit)}
    res['laufzeit_s'] = time.time() - t0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
