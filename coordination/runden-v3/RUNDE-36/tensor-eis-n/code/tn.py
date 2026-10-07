#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TENSOR-EIS-N, Runde 36 (fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Nachbau von Gu/Wen 2009 (arXiv:0907.1203v3) auf dem kubischen Gitter, quadratische (klassische) Ordnung wie
Gu/Wen Abschn. VI.C.1 und VII.D.1 (k-Raum-Lagrangedichte S. 19):
  L-Typ: H = (J/2) C^i_j C^i_j + (g/2) R^ij R^ij                      (Gl. 27)
  N-Typ: H = (J/2) [E^ij E^ij - 1/2 (E^ii)^2] + (g/2) a_ij R^ij         (Gl. 32)
  Zwangsbedingungen d_i E^ij = 0 (Gl. 13), R^ii = 0 (Gl. 21/22); Strafterme (U/2)(d_i E^ij)^2, (U/2)(R^ii)^2
  (Gl. 55/62, quadratische Entwicklung von H_U, Gl. 39). Masse = Verletzung R^ii = m delta (Gl. 31).

Gitter: a_ij (Koordinate, Gu/Wen theta) und E^ij (Impuls, Gu/Wen phi), symmetrisch, gestaffelt wie Gu/Wen S. 12
(Diagonale auf Knoten, xy auf n+(1/2,1/2,0) usw.). Ableitung = Differenz naechster Nachbarn, Fourier-Symbol i*K_a,
K_a = 2 sin(q_a/2) (physikalische FT mit Ort n + delta). Koeffizienten in der Frobenius-Orthonormalbasis
(xx, yy, zz, sqrt2*xy, sqrt2*yz, sqrt2*zx); dann ist H = 1/2 E.A.E + 1/2 a.B.a und die Paarung E^ij da_ij kanonisch.
Die Zerlegung in Moden (TT, Spur, Eichung) wird NICHT benutzt; alles per Zahl (pinv, eigh, SVD, Rang).

Aufrufe:
  tn.py rauch     --out X.json
  tn.py statik    --L 64 [--L 128 ...] --chunk 4 --out X.json --npz Y.npz
  tn.py spektrum  --L 32 --out X.json --npz Y.npz
  tn.py kontrolle --out X.json       (Ortsraum L=6, Gu/Wen-Matrix S. 19, exakte Bruchrechnung)
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


def lauf_statik(L, chunk, typen=('N', 'L'), g=1.0, mit_min=False):
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


# ------------------------------------------------------------------------------------------------ main
def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'statik', 'spektrum', 'kontrolle'])
    ap.add_argument('--L', type=int, action='append')
    ap.add_argument('--chunk', type=int, default=4)
    ap.add_argument('--mitmin', action='store_true')
    ap.add_argument('--out', required=True)
    ap.add_argument('--npz')
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__))}
    if a.modus == 'rauch':
        try:
            import matplotlib
            info['matplotlib'] = matplotlib.__version__
        except Exception as ex:
            info['matplotlib'] = 'FEHLT: %r' % (ex,)
        try:
            import scipy
            info['scipy'] = scipy.__version__
        except Exception as ex:
            info['scipy'] = 'FEHLT: %r' % (ex,)
        res = {'info': info}
        zeiten = {}
        for L in (16, 32):
            r, w = lauf_statik(L, 4, mit_min=(L == 16))
            zeiten['statik_%d' % L] = r['t_gesamt_s']
            res['statik_%d_stat' % L] = r['stat']
            res['statik_%d_sym' % L] = r['sym']
        res['zeiten'] = zeiten
        t = time.time()
        sp, _ = lauf_spektrum(8)
        res['spektrum_8_kontr'] = sp['kontr']
        res['zeit_spektrum_8'] = time.time() - t
        t = time.time()
        res['ortsraum_L4'] = {k: v for k, v in kontrolle_ortsraum(4).items() if k in ('Inc_sym', 'c_summe_null', 't_s')}
        res['zeit_ortsraum_4'] = time.time() - t
        t = time.time()
        res['exakt_1punkt'] = exakt_analyse([F(1, 2), F(-1, 3), F(2, 5)], 'N', F(1), F(1))['alle_w2_reell_nichtneg']
        res['zeit_exakt_1punkt'] = time.time() - t
    elif a.modus == 'statik':
        res = {'info': info, 'laeufe': []}
        arr = {}
        for L in a.L:
            r, w = lauf_statik(L, a.chunk, mit_min=a.mitmin)
            res['laeufe'].append(r)
            for t, W in w.items():
                arr['%s_L%d' % (t, L)] = W
            print('statik L=%d fertig nach %.1f s' % (L, time.time() - t0), flush=True)
        if a.npz:
            np.savez_compressed(a.npz + '.tmp.npz', **arr)
            os.replace(a.npz + '.tmp.npz', a.npz)
    elif a.modus == 'spektrum':
        sp, lin = lauf_spektrum(a.L[0])
        res = {'info': info, 'spektrum': sp, 'linien': lin}
    else:
        res = {'info': info}
        t = time.time(); res['ortsraum'] = kontrolle_ortsraum(6); print('ortsraum %.1f s' % (time.time() - t), flush=True)
        t = time.time(); res['gw_s19'] = kontrolle_gw(); print('gw %.1f s' % (time.time() - t), flush=True)
        t = time.time(); res['exakt'] = kontrolle_exakt(); print('exakt %.1f s' % (time.time() - t), flush=True)
        t = time.time(); res['drift'] = drift_demo(); print('drift %.1f s' % (time.time() - t), flush=True)
    res['laufzeit_s'] = time.time() - t0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
