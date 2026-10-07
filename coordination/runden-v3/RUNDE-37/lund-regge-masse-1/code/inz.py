#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IMPULS-NETZ-1, Runde 46 (fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Spuert Finns Hamilton-Netz (ew.py, V, A1R1) den Impuls der Materie?
Impulsregel = Verschiebungsregel M^H p = J (erster Klasse, B M = 0), Materie-Impuls J je Ecke aus der Gitter-Bilanz
J' = -M^H sigma. R1: a = S x + a_c, p = S y + p_J, p_J = M (M^H M)^-1 J.
  x' = (A_red y + S^H A p_J)/kappa_g, y' = -kappa_g B_red x + f_red
  => effektive Kraft f_eff = f_red + A_red^-1 S^H A p_J',  p_J' = -P_M sigma  (in Phase mit der Spannung).
Leistung per Goldener Regel (wie pn.py), statische/quasistatische Kopplung, Eichprobe (M^H G a = 0), Kreisbahnen,
Mitfuehrung (Schur-Komplement H_min(J) gegen 8 pi G c_0^2 V abs(e_T)^2/k^2).
pn.py, ew.py, tp.py, mn.py, nachtrag_iso.py werden unveraendert importiert (aus PUMPE-NETZ-1).
Aufruf nur ueber kleintest.sh auf der .69:
  python inz.py lauf --out lauf/h1.json [--rauch] [--nt 10 --nphi 20]
  python inz.py zusatz --out lauf/zusatz.json [--rauch]
  python inz.py urteil --h1 lauf/h1.json --zusatz lauf/zusatz.json --out lauf/urteile.json
  python inz.py bild --h1 lauf/h1.json --zusatz lauf/zusatz.json --bild lauf/bild-impuls-netz.png --out lauf/bild.json
"""
import argparse, json, sys, time, platform, os, resource, hashlib, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402  (unveraendert)
import mn  # noqa: E402  (unveraendert)
import pn  # noqa: E402  (PUMPE-NETZ-1, unveraendert)
import nachtrag_iso as ni  # noqa: E402  (PUMPE-NETZ-1, unveraendert)

LP, VCELL, GN, KG, KP = pn.LP, pn.VCELL, pn.GN, pn.KG, pn.KP
J_ISO = pn.J_ISO
KL_AUS = pn.KL_AUS
cT, herm = pn.cT, pn.herm
G_REF = {'001': 1.1844050923687857, '111': 0.9087749678217026, '123': 0.9769646539098713}
G_KARTE = {'001': 1.18, '111': 0.91, '123': 0.98}
NAMEN = [('100', [1, 0, 0]), ('110', [1, 1, 0]), ('111', [1, 1, 1]), ('1-1-1', [1, -1, -1]), ('-11-1', [-1, 1, -1]),
         ('-1-11', [-1, -1, 1]), ('210', [2, 1, 0]), ('211', [2, 1, 1]), ('123', [1, 2, 3]), ('001', [0, 0, 1])]
DREI = [('001', [0.0, 0.0, 1.0]), ('111', [1.0, 1.0, 1.0]), ('123', [1.0, 2.0, 3.0])]


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def basis(N, M, c):
    """S = Komplement von Bild [M, c] (wie pn.py), Rang je k."""
    U, sv, _ = np.linalg.svd(np.concatenate([M, c], -1))
    r = (sv > 1e-9 * sv[..., :1]).sum(-1)
    return U[..., :, 40:], r


def proj_M(M, MhM, v):
    """P_M v = M (M^H M)^-1 M^H v fuer v (..., E)."""
    z = np.linalg.solve(MhM, (cT(M) @ v[..., None]))
    return (M @ z)[..., 0]


def kraft_J(S, A, Ared, PMsig):
    """Zusatzkraft der Impulskopplung: -A_red^-1 S^H A P_M sigma."""
    return -np.linalg.solve(Ared, cT(S) @ (A @ PMsig[..., None]))[..., 0]


def statisch(Vb, lb, f):
    """Kopplung an die zwei weichen Moden von B_red: Summe abs(v_j^H f)^2/lambda_j (einzeln oder je k)."""
    if Vb.ndim == 2:
        pr = np.conj(Vb[:, :2].T) @ f
        return float((np.abs(pr) ** 2 / lb[:2]).sum())
    pr = np.einsum('kaj,ka->kj', np.conj(Vb[:, :, :2]), f)
    return (np.abs(pr) ** 2 / lb[:, :2]).sum(-1)


# ------------------------------------------------------------------------------------------------ Hauptlauf (wie pn.lauf, mit J)
def lauf(rauch=False, nt=10, nphi=20, w_lP=pn.W_LP, d_lP=pn.D_LP, voll=False):
    t0 = time.time()
    mod = ew.baue('V')
    E, nV = mod['E'], mod['nV']
    pos = np.array(mod['pos'])
    vv = pn.eckvolumen(mod)
    if rauch:
        ndir, wdir = pn.richtungen(4, 6)
        kl_grid = np.geomspace(0.005, 1.0, 6)
    else:
        ndir, wdir = pn.richtungen(nt, nphi)
        kl_grid = np.geomspace(0.005, 1.0, 28)
    nd = len(ndir)
    tder = pn.tet_ableitungen(mod)
    out = {'E': E, 'nV': nV, 'nd': nd, 'kl_grid': kl_grid.tolist(), 'w_lP': w_lP, 'd_lP': d_lP, 'nt': nt, 'nphi': nphi,
           'J_iso': J_ISO, 'G': GN, 'kappa_g': KG, 'kappa_strich': KP, 'summe_eckvolumen': float(vv.sum()),
           'kontrollen': {'P1': pn.kontrolle_p1(mod, tder)}}
    quellen = []
    for nm, ach in pn.ACHSEN:
        q = pn.quelle(mod, tder, ach, w=w_lP * LP, d=d_lP * LP)
        q['name'] = nm
        quellen.append(q)
    out['quellen'] = {q['name']: {'achse': q['achse'].tolist(), 'S0_TF_norm': float(np.linalg.norm(pn.tf(q['S0']))),
                                  'S0_spur': float(np.trace(q['S0'])), 'rand_anteil': q['rand_anteil']} for q in quellen}
    t_quelle = time.time() - t0
    nq = len(quellen)
    Jvar = [('iso', J_ISO), ('eins', None)]
    nk = len(kl_grid)
    lam = np.zeros((nk, nd, 3))
    Cst = {x: np.zeros((nk, nq, nd)) for x in ('S', 'V1', 'V1S', 'E', 'SJ_iso', 'V1SJ_iso', 'SJ_eins', 'V1SJ_eins')}
    dyn = {jn: {'Om2': np.zeros((nk, nd, 3)), 'gS': np.zeros((nk, nq, nd, 2), complex), 'gSJ': np.zeros((nk, nq, nd, 2), complex),
                'gV': np.zeros((nk, nd, 2), complex)} for jn, _ in Jvar}
    nnS = np.zeros((nk, nq, nd), complex)
    rang = []
    kd = {'cM_rel_max': 0.0, 'MB_rel_max': 0.0, 'KJ_MhPMsig_rel_max': 0.0, 'KJ_cHpJ_rel_max': 0.0, 'chol_ok': True,
          'J_anteil_kraft_rel': {jn: [] for jn, _ in Jvar}}
    for ik, kl in enumerate(kl_grid):
        s = kl / LP
        k = s * ndir
        o = ew.ops(mod, k)
        B, A1, M, c = o['B'], o['A'], o['M'], o['c']
        kd['cM_rel_max'] = max(kd['cM_rel_max'], float(np.abs(cT(c) @ M).max() / (np.abs(c).max() * np.abs(M).max())))
        kd['MB_rel_max'] = max(kd['MB_rel_max'], float(np.abs(cT(M) @ B).max() / (np.abs(M).max() * np.abs(B).max())))
        S, r = basis(None, M, c)
        rang += [int(x) for x in np.unique(r)]
        Bred = herm(cT(S) @ B @ S)
        lb, Vb = np.linalg.eigh(Bred)
        lam[ik] = lb[:, :3]
        MhM = herm(cT(M) @ M)
        m_u = (vv / VCELL)[None, :] * np.exp(1j * (k @ pos.T))
        cHc = cT(c) @ c
        ac = c @ np.linalg.solve(cHc, m_u[..., None])
        fV = -(KG / KP) * (B @ ac)[..., 0]
        frV = (cT(S) @ fV[..., None])[..., 0]
        frS, PMs = [], []
        for iq, q in enumerate(quellen):
            sig = np.exp(-1j * (k @ q['Rcells'].T)) @ q['sigR']
            frS.append((cT(S) @ (-sig)[..., None])[..., 0])
            PMsig = proj_M(M, MhM, sig)
            PMs.append(PMsig)
            MhS = (cT(M) @ sig[..., None])[..., 0]
            kd['KJ_MhPMsig_rel_max'] = max(kd['KJ_MhPMsig_rel_max'],
                                           float(np.abs((cT(M) @ PMsig[..., None])[..., 0] - MhS).max() / np.abs(MhS).max()))
            kd['KJ_cHpJ_rel_max'] = max(kd['KJ_cHpJ_rel_max'],
                                        float(np.abs((cT(c) @ PMsig[..., None])).max() / (np.abs(c).max() * np.abs(PMsig).max())))
            St = pn.S_tilde(q, k)
            nnS[ik, iq] = np.einsum('ki,kij,kj->k', ndir, St, ndir)
            Cst['E'][ik, iq] = 4.0 * pn.lam_kontrakt(ndir, St) / s ** 2
            for x, f in (('S', frS[iq]), ('V1', nnS[ik, iq][:, None] * frV), ('V1S', frS[iq] + nnS[ik, iq][:, None] * frV)):
                Cst[x][ik, iq] = statisch(Vb, lb, f)
        for jn, J in Jvar:
            A = A1 if J is None else pn.A_J(mod, k, J)
            Ared = herm(cT(S) @ A @ S)
            try:
                L = np.linalg.cholesky(Ared)
            except np.linalg.LinAlgError:
                kd['chol_ok'] = False
                raise
            Dm = herm(cT(L) @ Bred @ L)
            om2, Uu = np.linalg.eigh(Dm)
            dyn[jn]['Om2'][ik] = om2[:, :3]
            X = L @ Uu[:, :, :2]
            dyn[jn]['gV'][ik] = np.einsum('kaj,ka->kj', np.conj(X), frV)
            for iq in range(nq):
                frJ = kraft_J(S, A, Ared, PMs[iq])
                fSJ = frS[iq] + frJ
                kd['J_anteil_kraft_rel'][jn].append(float(np.median(np.linalg.norm(frJ, axis=-1) / np.linalg.norm(frS[iq], axis=-1))))
                dyn[jn]['gS'][ik, iq] = np.einsum('kaj,ka->kj', np.conj(X), frS[iq])
                dyn[jn]['gSJ'][ik, iq] = np.einsum('kaj,ka->kj', np.conj(X), fSJ)
                Cst['SJ_' + jn][ik, iq] = statisch(Vb, lb, fSJ)
                Cst['V1SJ_' + jn][ik, iq] = statisch(Vb, lb, fSJ + nnS[ik, iq][:, None] * frV)
    t_k = time.time() - t0 - t_quelle
    kd['rang_MC'] = sorted(set(rang))
    kd['J_anteil_kraft_rel'] = {jn: {'min': float(min(v)), 'max': float(max(v))} for jn, v in kd['J_anteil_kraft_rel'].items()}
    out['kontrollen'].update(kd)
    s0 = kl_grid[0] / LP
    c0 = {jn: float(np.sqrt(dyn[jn]['Om2'][0, :, :2].mean() / s0 ** 2)) for jn, _ in Jvar}
    out['c0'] = c0
    out['Om2_ueber_k2_kl0'] = {jn: {'min': float((dyn[jn]['Om2'][0, :, :2] / s0 ** 2).min()), 'max': float((dyn[jn]['Om2'][0, :, :2] / s0 ** 2).max())}
                               for jn, _ in Jvar}
    # ---------------------------------------------------------------- Massenschale und Leistung (wie pn.py, plus SJ, V1SJ)
    ls = np.log(kl_grid / LP)
    pref = (math.pi / (4 * KG)) * VCELL / (2 * math.pi) ** 3
    kanal = ('S', 'V1', 'V1S', 'SJ', 'V1SJ')
    tab = {}
    for jn, _ in Jvar:
        Om2 = dyn[jn]['Om2']
        tab[jn] = {}
        for iq, q in enumerate(quellen):
            zeilen = []
            for klt in KL_AUS:
                om = c0[jn] * klt / LP
                Pd = {x: np.zeros(nd) for x in kanal}
                bad = 0
                zw = range(1) if jn == 'iso' else range(2)
                for d_ in range(nd):
                    for jz in zw:
                        if jn == 'iso':
                            Om = np.sqrt(Om2[:, d_, :2].mean(-1))
                            eps = (c0[jn] ** 2) * (kl_grid / LP) ** 2 / Om ** 2 * nnS[:, iq, d_]
                            gS_ = dyn[jn]['gS'][:, iq, d_, :]
                            gSJ_ = dyn[jn]['gSJ'][:, iq, d_, :]
                            gV_ = eps[:, None] * dyn[jn]['gV'][:, d_, :]
                            gg = {'S': (np.abs(gS_) ** 2).sum(-1), 'V1': (np.abs(gV_) ** 2).sum(-1), 'V1S': (np.abs(gS_ + gV_) ** 2).sum(-1),
                                  'SJ': (np.abs(gSJ_) ** 2).sum(-1), 'V1SJ': (np.abs(gSJ_ + gV_) ** 2).sum(-1)}
                        else:
                            Om = np.sqrt(Om2[:, d_, jz])
                            eps = (c0[jn] ** 2) * (kl_grid / LP) ** 2 / Om ** 2 * nnS[:, iq, d_]
                            gS_ = dyn[jn]['gS'][:, iq, d_, jz]
                            gSJ_ = dyn[jn]['gSJ'][:, iq, d_, jz]
                            gV_ = eps * dyn[jn]['gV'][:, d_, jz]
                            gg = {'S': np.abs(gS_) ** 2, 'V1': np.abs(gV_) ** 2, 'V1S': np.abs(gS_ + gV_) ** 2,
                                  'SJ': np.abs(gSJ_) ** 2, 'V1SJ': np.abs(gSJ_ + gV_) ** 2}
                        lo = np.log(Om)
                        if np.any(np.diff(lo) <= 0):
                            bad += 1
                        so = np.interp(np.log(om), lo, ls, left=np.nan, right=np.nan)
                        if not np.isfinite(so):
                            bad += 1
                            continue
                        dlo = np.gradient(lo, ls)
                        slope = np.interp(so, ls, dlo)
                        s_on = math.exp(so)
                        v = om / s_on * slope
                        for x in kanal:
                            val = math.exp(np.interp(so, ls, np.log(np.maximum(gg[x], 1e-300))))
                            Pd[x][d_] += pref * s_on ** 2 / v * val
                P = {x: float((wdir * Pd[x]).sum()) for x in kanal}
                kE = klt / LP
                lamE = pn.lam_kontrakt(ndir, pn.S_tilde(q, kE * ndir))
                PE = float(GN * om ** 2 / (4 * math.pi * c0[jn]) * (wdir * lamE).sum())
                z = {'kl': klt, 'omega': om, 'P_E': PE, 'nicht_monoton_oder_aussen': bad}
                for x in kanal:
                    z['P_' + x] = P[x]
                    z['P_' + x + '_ueber_P_E'] = P[x] / PE
                z['A_R'] = math.sqrt(P['V1'] / P['S'])
                zeilen.append(z)
            tab[jn][q['name']] = zeilen
    out['tabelle'] = tab
    # statische bzw. quasistatische Kopplung je kl
    stat = {}
    for iq, q in enumerate(quellen):
        zeilen = []
        for klt in KL_AUS:
            so = math.log(klt / LP)
            I = {}
            for x in Cst:
                vals = np.array([math.exp(np.interp(so, ls, np.log(np.maximum(Cst[x][:, iq, d_], 1e-300)))) for d_ in range(nd)])
                I[x] = float((wdir * vals).sum())
            z = {'kl': klt, 'C_E': I['E']}
            for x in Cst:
                if x != 'E':
                    z['C_' + x + '_ueber_C_E'] = I[x] / I['E']
            zeilen.append(z)
        stat[q['name']] = zeilen
    out['statisch'] = stat
    # KN: G_N/G wie pn.py
    s1 = 0.01 / LP
    kk = s1 * ndir
    o = ew.ops(mod, kk)
    W = mn.W_of(mod, kk)
    Pm = herm(-cT(W) @ o['B'] @ W)
    evp = np.linalg.eigvalsh(Pm)[:, 0] / s1 ** 2
    out['kontrollen']['KN_P_weich_ueber_k2'] = {'min': float(evp.min()), 'max': float(evp.max()), 'mittel': float(evp.mean())}
    GN_rel = 0.2 / float(evp.mean())
    out['G_N_ueber_G'] = GN_rel
    # G_rad/G_N je Achse bei kl = 0,01
    g = {}
    for qn in tab['iso']:
        z0 = tab['iso'][qn][0]
        ze = tab['eins'][qn][0]
        st = stat[qn][0]
        g[qn] = {'dyn_V1S_ohneJ': z0['P_V1S_ueber_P_E'] / GN_rel, 'dyn_S_ohneJ': z0['P_S_ueber_P_E'] / GN_rel,
                 'dyn_V1SJ': z0['P_V1SJ_ueber_P_E'] / GN_rel, 'dyn_SJ': z0['P_SJ_ueber_P_E'] / GN_rel,
                 'dyn_V1SJ_eins_naeherung': ze['P_V1SJ_ueber_P_E'] / GN_rel, 'dyn_SJ_eins_naeherung': ze['P_SJ_ueber_P_E'] / GN_rel,
                 'stat_S_ohneJ': st['C_S_ueber_C_E'] / GN_rel, 'quasistat_SJ_iso': st['C_SJ_iso_ueber_C_E'] / GN_rel,
                 'quasistat_V1SJ_iso': st['C_V1SJ_iso_ueber_C_E'] / GN_rel, 'quasistat_SJ_eins': st['C_SJ_eins_ueber_C_E'] / GN_rel,
                 'KDJ_dyn_SJ_gegen_quasistat': z0['P_SJ_ueber_P_E'] / st['C_SJ_iso_ueber_C_E']}
    out['G_rad_ueber_G_N_kl001'] = g
    out['zeiten_s'] = {'quelle': t_quelle, 'k_schleife': t_k, 'gesamt': time.time() - t0}
    if rauch and not voll:
        out = {'rauch': True, 'schluessel': sorted(out.keys()), 'zeiten_s': out['zeiten_s']}
    return out


# ------------------------------------------------------------------------------------------------ Zusatz: Isotropie, Eichprobe, Kreisbahnen, Mitfuehrung
def eichkraefte(S, M, MhM, sig, frJ, G):
    """Kraft ohne J und mit J in der Eichung M^H G a = 0 (G diagonal, positiv)."""
    GM = G[:, None] * M
    MGM = herm(cT(M) @ GM)
    Kmat = np.linalg.solve(MGM, cT(GM) @ S)                      # (M^H G M)^-1 M^H G S
    T = S - M @ Kmat
    f_noJ = -(cT(T) @ sig)
    f_J = f_noJ - cT(Kmat) @ (cT(M) @ sig) + frJ
    return f_noJ, f_J


def isotropie(mod, Q, n, kl, gauges):
    s = kl / LP
    k = s * n
    o = ew.ops(mod, k[None])
    B, A1, M, c = o['B'][0], o['A'][0], o['M'][0], o['c'][0]
    S, r = basis(None, M, c)
    Bred = herm(cT(S) @ B @ S)
    lb, Vb = np.linalg.eigh(Bred)
    MhM = herm(cT(M) @ M)
    A = pn.A_J(mod, k[None], J_ISO)[0]
    Ared = herm(cT(S) @ A @ S)
    L = np.linalg.cholesky(Ared)
    om2, Uu = np.linalg.eigh(herm(cT(L) @ Bred @ L))
    X = L @ Uu[:, :2]
    tens, e1, e2 = ni.basis_tt(n)
    ph = np.exp(1j * (mod['mitte'] @ k))
    CE = 4 * VCELL ** 2 / s ** 2
    z = {'kl': kl, 'n': n.tolist(), 'rang': int(r), 'lam_weich_ueber_k2': [float(x / s ** 2) for x in lb[:2]]}
    fr = {'ohneJ': {}, 'mitJ': {}}
    ke = {'ohneJ': {}, 'mitJ': {}}
    kraft = {'ohneJ': {}, 'mitJ': {}}
    for nm, T in tens.items():
        sig = ni.sigma_T(Q, T) * ph
        f0 = cT(S) @ (-sig)
        PMsig = proj_M(M, MhM, sig)
        frJ = -np.linalg.solve(Ared, cT(S) @ (A @ PMsig))
        fr['ohneJ'][nm] = f0
        fr['mitJ'][nm] = f0 + frJ
        for art in ('ohneJ', 'mitJ'):
            ke[art][nm] = [float(statisch(Vb, lb, fr[art][nm]) / CE)]
            kraft[art][nm] = []
        for G in gauges:
            fG0, fGJ = eichkraefte(S, M, MhM, sig, frJ, G)
            ke['ohneJ'][nm].append(float(statisch(Vb, lb, fG0) / CE))
            ke['mitJ'][nm].append(float(statisch(Vb, lb, fGJ) / CE))
            kraft['ohneJ'][nm].append(float(np.linalg.norm(fG0 - f0) / np.linalg.norm(f0)))
            kraft['mitJ'][nm].append(float(np.linalg.norm(fGJ - fr['mitJ'][nm]) / np.linalg.norm(fr['mitJ'][nm])))
    for art in ('ohneJ', 'mitJ'):
        Pm = np.stack([np.conj(Vb[:, :2].T) @ fr[art]['h+'], np.conj(Vb[:, :2].T) @ fr[art]['hx']], 1)
        R = herm((cT(Pm) @ np.diag(1 / lb[:2]) @ Pm) / CE)
        Gd = np.stack([np.conj(X.T) @ fr[art]['h+'], np.conj(X.T) @ fr[art]['hx']], 1)
        Rd = herm((cT(Gd) @ np.diag(1 / om2[:2]) @ Gd) / CE)
        zz = {'R_eig': [float(x) for x in np.linalg.eigvalsh(R)], 'R_mittel': float(0.5 * np.trace(R).real),
              'Rdyn_mittel': float(0.5 * np.trace(Rd).real)}
        for nm in ('L1', 'L2', 'nn', 'Ptr'):
            zz['C_' + nm + '_ueber_CE'] = ke[art][nm][0]
            zz['C_' + nm + '_dyn_ueber_CE'] = float((np.abs(np.conj(X.T) @ fr[art][nm]) ** 2 / om2[:2]).sum() / CE)
        z[art] = zz
    # Eichprobe: Kopplung C/C_E in R1 und den Eichungen G; Unterschied skaliert mit max(C_R1, 1), relativ, und Kraft
    z['KE'] = {}
    for art in ('ohneJ', 'mitJ'):
        z['KE'][art] = {nm: {'C': ke[art][nm], 'dC_skal': [float(abs(v - ke[art][nm][0]) / max(ke[art][nm][0], 1.0)) for v in ke[art][nm][1:]],
                             'dC_rel': [float(abs(v / ke[art][nm][0] - 1)) if ke[art][nm][0] > 0 else None for v in ke[art][nm][1:]],
                             'kraft_rel': kraft[art][nm]} for nm in ke[art]}
    return z


def lam_proj(n, S):
    P = np.eye(3) - np.outer(n, n)
    PSP = P @ S @ P
    return PSP - 0.5 * P * np.trace(P @ S)


def kreisbahnen(mod, Q, quellen, nd, wd, kl=0.01, chunk=50):
    s = kl / LP
    arten = ('stat_ohneJ', 'stat_J_iso', 'stat_J_eins', 'dyn_ohneJ_iso', 'dyn_J_iso')
    res = {nm: {v: {a: 0.0 for a in arten} for v in ('voll', 'nurTT')} for nm in quellen}
    for nm in quellen:
        res[nm]['E'] = 0.0
    for i0 in range(0, len(nd), chunk):
        nn = nd[i0:i0 + chunk]
        ww = wd[i0:i0 + chunk]
        k = s * nn
        o = ew.ops(mod, k)
        B, A1, M, c = o['B'], o['A'], o['M'], o['c']
        S, r = basis(None, M, c)
        Bred = herm(cT(S) @ B @ S)
        lb, Vb = np.linalg.eigh(Bred)
        MhM = herm(cT(M) @ M)
        Ai = pn.A_J(mod, k, J_ISO)
        Ared_i = herm(cT(S) @ Ai @ S)
        Ared_1 = herm(cT(S) @ A1 @ S)
        L = np.linalg.cholesky(Ared_i)
        om2, Uu = np.linalg.eigh(herm(cT(L) @ Bred @ L))
        X = L @ Uu[:, :, :2]
        ph = np.exp(1j * (k @ mod['mitte'].T))
        for nm, Sc in quellen.items():
            for v in ('voll', 'nurTT'):
                if v == 'voll':
                    Tj = np.broadcast_to(Sc, (len(nn), 3, 3))
                else:
                    Tj = np.stack([lam_proj(n_, Sc) for n_ in nn])
                Mx = Tj - np.einsum('kii->k', Tj)[:, None, None] * np.eye(3)[None]
                sig = np.einsum('eab,kab->ke', Q, Mx) * ph
                f0 = (cT(S) @ (-sig)[..., None])[..., 0]
                PMsig = proj_M(M, MhM, sig)
                fJi = f0 + kraft_J(S, Ai, Ared_i, PMsig)
                fJ1 = f0 + kraft_J(S, A1, Ared_1, PMsig)
                res[nm][v]['stat_ohneJ'] += float((ww * statisch(Vb, lb, f0)).sum())
                res[nm][v]['stat_J_iso'] += float((ww * statisch(Vb, lb, fJi)).sum())
                res[nm][v]['stat_J_eins'] += float((ww * statisch(Vb, lb, fJ1)).sum())
                for a_, f in (('dyn_ohneJ_iso', f0), ('dyn_J_iso', fJi)):
                    g_ = np.einsum('kaj,ka->kj', np.conj(X), f)
                    res[nm][v][a_] += float((ww * (np.abs(g_) ** 2 / om2[:, :2]).sum(-1)).sum())
            for j in range(len(nn)):
                L_ = lam_proj(nn[j], Sc)
                res[nm]['E'] += ww[j] * 4 * VCELL ** 2 * float(np.real(np.sum(L_ * np.conj(Sc)))) / s ** 2
    out = {}
    for nm, rr in res.items():
        out[nm] = {v: {a: rr[v][a] / rr['E'] for a in arten} for v in ('voll', 'nurTT')}
    return out


def mitfuehrung(mod, kls, nd, wd, chunk=100):
    """Schur-Komplement H_min(J) fuer J_v = V_v e e^(i k.p_v); r = H_min k^2/(8 pi G c_0^2 V_Zelle)."""
    E, nV = mod['E'], mod['nV']
    pos = np.array(mod['pos'])
    vv = pn.eckvolumen(mod)
    c0 = {'iso': None, 'eins': None}
    res = {}
    Lachs = {nm: np.array(v) / np.linalg.norm(v) for nm, v in DREI}
    for jn, J in (('iso', J_ISO), ('eins', None)):
        res[jn] = {}
        for kl in kls:
            s = kl / LP
            Qall = np.zeros((len(nd), 3, 3), complex)
            kgm = 0.0
            stat_rest = 0.0
            om2min = []
            for i0 in range(0, len(nd), chunk):
                nn = nd[i0:i0 + chunk]
                k = s * nn
                o = ew.ops(mod, k)
                B, A1, M, c = o['B'], o['A'], o['M'], o['c']
                S, r = basis(None, M, c)
                A = A1 if J is None else pn.A_J(mod, k, J)
                Ared = herm(cT(S) @ A @ S)
                MhM = herm(cT(M) @ M)
                Bred = herm(cT(S) @ B @ S)
                Lc = np.linalg.cholesky(Ared)
                om2 = np.linalg.eigvalsh(herm(cT(Lc) @ Bred @ Lc))
                om2min.append(om2[:, :2] / s ** 2)
                ph = np.exp(1j * (k @ pos.T))                          # (nch, nV)
                P_, SAp, Y = [], [], []
                Js = []
                for a in range(3):
                    Jv = np.zeros((len(nn), 3 * nV), complex)
                    Jv[:, a::3] = vv[None, :] * ph
                    Js.append(Jv)
                    z = np.linalg.solve(MhM, Jv[..., None])
                    p = (M @ z)[..., 0]
                    sap = (cT(S) @ (A @ p[..., None]))[..., 0]
                    y = np.linalg.solve(Ared, sap[..., None])[..., 0]
                    P_.append(p); SAp.append(sap); Y.append(y)
                for a in range(3):
                    Ap_a = (A @ P_[a][..., None])[..., 0]
                    for b in range(3):
                        Qall[i0:i0 + len(nn), a, b] = (np.einsum('ke,ke->k', np.conj(P_[a]), (A @ P_[b][..., None])[..., 0])
                                                       - np.einsum('ke,ke->k', np.conj(SAp[a]), Y[b])) / (2 * KG)
                    # KGM: H_min = (1/2) J^H lambda, lambda = (M^H M)^-1 M^H A p_stat/kappa_g
                    pst = P_[a] - (S @ Y[a][..., None])[..., 0]
                    Apst = (A @ pst[..., None])[..., 0]
                    lam_ = np.linalg.solve(MhM, (cT(M) @ Apst[..., None]))[..., 0] / KG
                    Hb = 0.5 * np.einsum('ke,ke->k', np.conj(Js[a]), lam_)
                    kgm = max(kgm, float(np.abs(Hb - Qall[i0:i0 + len(nn), a, a]).max() / np.abs(Qall[i0:i0 + len(nn), a, a]).max()))
                    rest = (cT(S) @ Apst[..., None])[..., 0]
                    stat_rest = max(stat_rest, float(np.abs(rest).max() / np.abs(Ap_a).max()))
            om2min = np.concatenate(om2min, 0)
            if c0[jn] is None:
                c0[jn] = float(np.sqrt(om2min.mean()))
            norm = s ** 2 / (8 * math.pi * GN * c0[jn] ** 2 * VCELL)
            normL = s ** 2 / (2 * math.pi * GN * c0[jn] ** 2 * VCELL)
            rT_eig, rT_mit, rL, kreuz = [], [], [], []
            for d_, n in enumerate(nd):
                tens, e1, e2 = ni.basis_tt(n)
                Et = np.stack([e1, e2], 1)
                QT = herm(Et.T @ Qall[d_] @ Et)
                ev = np.linalg.eigvalsh(QT).real * norm
                rT_eig.append(ev)
                rT_mit.append(0.5 * np.trace(QT).real * norm)
                rL.append(float(np.real(n @ Qall[d_] @ n)) * normL)
                kreuz.append(float(max(abs(e1 @ Qall[d_] @ n), abs(e2 @ Qall[d_] @ n))
                                   / max(math.sqrt(abs(np.trace(QT).real / 2) * abs(np.real(n @ Qall[d_] @ n))), 1e-300)))
            rT_eig = np.array(rT_eig)
            rT_mit = np.array(rT_mit)
            z = {'kl': kl, 'c0': c0[jn], 'R_iso': float((wd * rT_mit).sum() / wd.sum()), 'r_min': float(rT_eig.min()),
                 'r_max': float(rT_eig.max()), 'r_mittel_min': float(rT_mit.min()), 'r_mittel_max': float(rT_mit.max()),
                 'laengs_mittel': float((wd * np.array(rL)).sum() / wd.sum()), 'laengs_min': float(min(rL)), 'laengs_max': float(max(rL)),
                 'kreuz_TL_max': float(max(kreuz)), 'KGM_rel_max': kgm, 'stat_rest_rel_max': stat_rest,
                 'H_min_T_positiv': bool(rT_eig.min() > 0), 'R_rot': {}, 'R_mov': {}}
            for nm, Lv in Lachs.items():
                num_r, den_r, num_m, den_m = 0.0, 0.0, 0.0, 0.0
                for d_, n in enumerate(nd):
                    eL = np.cross(Lv, n)
                    num_r += wd[d_] * float(np.real(eL @ Qall[d_] @ eL)) * norm
                    den_r += wd[d_] * float(eL @ eL)
                    vT = Lv - n * (n @ Lv)
                    num_m += wd[d_] * float(np.real(vT @ Qall[d_] @ vT)) * norm
                    den_m += wd[d_] * float(vT @ vT)
                z['R_rot'][nm] = num_r / den_r
                z['R_mov'][nm] = num_m / den_m
            # benannte Richtungen
            z['benannt'] = {}
            for nmr, vr in NAMEN:
                n = np.array(vr, float) / np.linalg.norm(vr)
                kk = (s * n)[None]
                o = ew.ops(mod, kk)
                B, A1, M, c = o['B'], o['A'], o['M'], o['c']
                S, r = basis(None, M, c)
                A = A1 if J is None else pn.A_J(mod, kk, J)
                Ared = herm(cT(S) @ A @ S)
                MhM = herm(cT(M) @ M)
                ph = np.exp(1j * (kk @ pos.T))
                Qn = np.zeros((3, 3), complex)
                Pl, Sl, Yl = [], [], []
                for a in range(3):
                    Jv = np.zeros((1, 3 * nV), complex)
                    Jv[:, a::3] = vv[None, :] * ph
                    p = (M @ np.linalg.solve(MhM, Jv[..., None]))[..., 0]
                    sap = (cT(S) @ (A @ p[..., None]))[..., 0]
                    y = np.linalg.solve(Ared, sap[..., None])[..., 0]
                    Pl.append(p); Sl.append(sap); Yl.append(y)
                for a in range(3):
                    for b in range(3):
                        Qn[a, b] = (np.vdot(Pl[a][0], (A[0] @ Pl[b][0])) - np.vdot(Sl[a][0], Yl[b][0])) / (2 * KG)
                tens, e1, e2 = ni.basis_tt(n)
                Et = np.stack([e1, e2], 1)
                QT = herm(Et.T @ Qn @ Et)
                z['benannt'][nmr] = {'r_eig': [float(x) for x in np.linalg.eigvalsh(QT).real * norm],
                                     'laengs': float(np.real(n @ Qn @ n)) * normL}
            res[jn]['kl_%g' % kl] = z
    return res


def zusatz(rauch=False, voll=False):
    t0 = time.time()
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = ni.Q_map(mod, tder)
    out = {'E': mod['E'], 'nV': mod['nV']}
    rng = np.random.default_rng(41)
    g1 = rng.uniform(0.25, 4.0, mod['E'])
    rng = np.random.default_rng(43)
    g2 = rng.uniform(0.25, 4.0, mod['E'])
    gauges = [g1, g2]
    # Isotropie und Eichprobe
    namen = NAMEN[:3] if rauch else NAMEN
    rows = []
    for nm, v in namen:
        n = np.array(v, float) / np.linalg.norm(v)
        for kl in (0.01, 0.1):
            z = isotropie(mod, Q, n, kl, gauges)
            z['name'] = nm
            rows.append(z)
    out['isotropie_benannt'] = rows
    ke_max = {'mitJ': 0.0, 'ohneJ_dC_skal': 0.0, 'ohneJ_dC_rel_TT_L': 0.0, 'ohneJ_kraft_rel': 0.0}
    for z in rows:
        for nm_ in ('h+', 'hx', 'L1', 'L2', 'nn'):
            kj = z['KE']['mitJ'][nm_]
            ke_max['mitJ'] = max(ke_max['mitJ'], max(kj['dC_skal'] + kj['kraft_rel']))
            k0 = z['KE']['ohneJ'][nm_]
            ke_max['ohneJ_dC_skal'] = max(ke_max['ohneJ_dC_skal'], max(k0['dC_skal']))
            ke_max['ohneJ_kraft_rel'] = max(ke_max['ohneJ_kraft_rel'], max(k0['kraft_rel']))
            if nm_ in ('h+', 'hx', 'L1', 'L2') and k0['C'][0] > 1e-6:
                ke_max['ohneJ_dC_rel_TT_L'] = max(ke_max['ohneJ_dC_rel_TT_L'], max(k0['dC_rel']))
    out['KE_max_rel'] = ke_max
    nd6, wd6 = pn.richtungen(2, 3) if rauch else pn.richtungen(6, 12)
    gl = [isotropie(mod, Q, n, 0.01, []) for n in nd6]
    zz = {}
    for art in ('ohneJ', 'mitJ'):
        Rm = np.array([z[art]['R_mittel'] for z in gl])
        ev = np.array([z[art]['R_eig'] for z in gl])
        zz[art] = {'R_mittel_winkelmittel': float((wd6 * Rm).sum() / wd6.sum()), 'R_eig_min': float(ev.min()), 'R_eig_max': float(ev.max()),
                   'C_L_max': float(max(max(z[art]['C_L1_ueber_CE'], z[art]['C_L2_ueber_CE']) for z in gl)),
                   'C_nn_max': float(max(z[art]['C_nn_ueber_CE'] for z in gl)), 'C_Ptr_max': float(max(z[art]['C_Ptr_ueber_CE'] for z in gl))}
    out['isotropie_gitter_kl001'] = zz
    t_iso = time.time() - t0
    # Kreisbahnen und kompakte phi-Quellen
    quellen = {}
    normalen = [('001', [0, 0, 1]), ('111', [1, 1, 1]), ('110', [1, 1, 0]), ('123', [1, 2, 3])]
    rng = np.random.default_rng(31)
    for i, v in enumerate(rng.normal(size=(2 if rauch else 8, 3))):
        normalen.append(('z%d' % i, v.tolist()))
    m4 = {}
    for nm, v in normalen:
        m = np.array(v, float) / np.linalg.norm(v)
        u = np.cross(m, [0.3, 0.5, 0.7])
        u /= np.linalg.norm(u)
        w = np.cross(m, u)
        quellen['bahn_' + nm] = np.outer(u + 1j * w, u + 1j * w)
        m4['bahn_' + nm] = {'m': m.tolist(), 'summe_m4': float((m ** 4).sum())}
    if not rauch:
        for nm, ach in pn.ACHSEN:
            q = pn.quelle(mod, tder, ach)
            quellen['phi_' + nm] = q['S0'].astype(complex)
    nd, wd = pn.richtungen(4, 6) if rauch else pn.richtungen(10, 20)
    kb = kreisbahnen(mod, Q, quellen, nd, wd)
    for nm in kb:
        if nm in m4:
            kb[nm].update(m4[nm])
    out['kreisbahnen_kl001'] = kb
    t_bahn = time.time() - t0 - t_iso
    # Mitfuehrung
    kls = [0.01, 0.02] if rauch else [0.01, 0.02, 0.05, 0.1, 0.2]
    out['mitfuehrung'] = mitfuehrung(mod, kls, nd, wd)
    out['zeiten_s'] = {'isotropie': t_iso, 'kreisbahnen': t_bahn, 'gesamt': time.time() - t0}
    if rauch and not voll:
        out = {'rauch': True, 'schluessel': sorted(out.keys()), 'zeiten_s': out['zeiten_s']}
    return out


# ------------------------------------------------------------------------------------------------ Urteile (PLAN Abschnitt 5)
def urteil(p_h1, p_zu):
    with open(p_h1) as f:
        h1 = json.load(f)['lauf']
    with open(p_zu) as f:
        zu = json.load(f)['zusatz']
    E_ = lambda b: 'eingetroffen' if b else 'nicht eingetroffen'
    g = h1['G_rad_ueber_G_N_kl001']
    urt = {}
    det = {qn: {'G_ohneJ': g[qn]['dyn_V1S_ohneJ'], 'rel_zu_ref': g[qn]['dyn_V1S_ohneJ'] / G_REF[qn] - 1,
                'rel_zu_karte': g[qn]['dyn_V1S_ohneJ'] / G_KARTE[qn] - 1} for qn in G_REF}
    urt['IN0'] = {'plan': E_(all(abs(d['rel_zu_ref']) <= 0.01 for d in det.values())),
                  'kartenwortlaut': E_(all(abs(d['rel_zu_karte']) <= 0.01 for d in det.values())), 'det': det}
    k = h1['kontrollen']
    teile = {'rang_40': k['rang_MC'] == [40], 'KR_cM': k['cM_rel_max'] <= 1e-10, 'KF_MB': k['MB_rel_max'] <= 1e-10,
             'KJ': max(k['KJ_MhPMsig_rel_max'], k['KJ_cHpJ_rel_max']) <= 1e-10, 'cholesky': bool(k['chol_ok']),
             'KE_mitJ': zu['KE_max_rel']['mitJ'] <= 1e-8}
    urt['IN1'] = {'plan': E_(all(teile.values())), 'kartenwortlaut': E_(all(teile.values())), 'teile': teile,
                  'werte': {'cM': k['cM_rel_max'], 'MB': k['MB_rel_max'], 'KJ_MhPMsig': k['KJ_MhPMsig_rel_max'],
                            'KJ_cHpJ': k['KJ_cHpJ_rel_max'], 'KE': zu['KE_max_rel']}}
    det = {qn: {'G_V1SJ': g[qn]['dyn_V1SJ'], 'G_SJ': g[qn]['dyn_SJ']} for qn in G_REF}
    ok = all(abs(d['G_V1SJ'] - 1) <= 0.01 for d in det.values())
    urt['IN2'] = {'plan': E_(ok), 'kartenwortlaut': E_(ok), 'det': det}
    mi = zu['mitfuehrung']['iso']['kl_0.01']
    sechs = [mi['R_rot'][x] for x in ('001', '111', '123')] + [mi['R_mov'][x] for x in ('001', '111', '123')]
    urt['IN3'] = {'plan': E_(all(0.9 <= x <= 1.1 for x in sechs)), 'kartenwortlaut': E_(0.9 <= mi['R_iso'] <= 1.1),
                  'R_rot': mi['R_rot'], 'R_mov': mi['R_mov'], 'R_iso': mi['R_iso'], 'r_min': mi['r_min'], 'r_max': mi['r_max']}
    return {'urteile': urt, 'h1_sha256': sha(p_h1), 'zusatz_sha256': sha(p_zu)}


# ------------------------------------------------------------------------------------------------ Bild
def bild(p_h1, p_zu, pfad_bild):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with open(p_h1) as f:
        h1 = json.load(f)['lauf']
    with open(p_zu) as f:
        zu = json.load(f)['zusatz']
    fig, ax = plt.subplots(1, 3, figsize=(17, 5.4))
    a0 = ax[0]
    g = h1['G_rad_ueber_G_N_kl001']
    kb = zu['kreisbahnen_kl001']
    labels, ohne, mit, mitS = [], [], [], []
    for qn in ('001', '111', '123'):
        labels.append('phi-Quelle\nAchse %s' % qn)
        ohne.append(g[qn]['dyn_V1S_ohneJ']); mit.append(g[qn]['dyn_V1SJ']); mitS.append(g[qn]['dyn_SJ'])
    for nm in ('bahn_001', 'bahn_111', 'bahn_110', 'bahn_123'):
        labels.append('Kreisbahn\nNormale %s' % nm[5:])
        ohne.append(kb[nm]['voll']['dyn_ohneJ_iso']); mit.append(kb[nm]['voll']['dyn_J_iso']); mitS.append(np.nan)
    x = np.arange(len(labels))
    a0.bar(x - 0.2, ohne, 0.38, color='#b0b0b0', label='ohne Impulskopplung (PUMPE-NETZ-1)')
    a0.bar(x + 0.2, mit, 0.38, color='#1f77b4', label='mit Impulskopplung (phi: V1+S+J; Bahn: S+J)')
    a0.plot(x[:3] + 0.2, mitS[:3], 'k_', ms=18, mew=2, label='phi: nur S+J (ohne V1)')
    a0.axhline(1, color='k', lw=0.8)
    a0.axhspan(0.99, 1.01, color='#2ca02c', alpha=0.15, label='IN2-Band 1 +- 0,01')
    a0.set_xticks(x); a0.set_xticklabels(labels, fontsize=7)
    a0.set_ylabel('G_rad/G_N (kl = 0,01, J_iso, dynamisch)')
    lo = min(min(ohne), min(mit)); hi = max(max(ohne), max(mit))
    a0.set_ylim(min(0.85, lo - 0.02), max(1.2, hi + 0.02))
    a0.set_title('G_rad/G_N je Quellachse bzw. Bahnlage')
    a0.legend(fontsize=6.5, loc='upper right')
    a1 = ax[1]
    farben = {'001': '#1f77b4', '111': '#d62728', '123': '#2ca02c'}
    for qn, zeilen in h1['tabelle']['iso'].items():
        kl = [z['kl'] for z in zeilen]
        a1.semilogx(kl, [z['P_V1S_ueber_P_E'] / h1['G_N_ueber_G'] for z in zeilen], 'o--', color=farben[qn], ms=3, mfc='none',
                    label='ohne J, Achse %s' % qn)
        a1.semilogx(kl, [z['P_V1SJ_ueber_P_E'] / h1['G_N_ueber_G'] for z in zeilen], 's-', color=farben[qn], ms=4,
                    label='mit J (V1+S+J), Achse %s' % qn)
    a1.axhline(1, color='k', lw=0.8)
    a1.set_xlabel('k l (l = l_P, Massenschale)'); a1.set_ylabel('P / P_E / (G_N/G)')
    a1.set_title('phi-Quadrupol: Abstrahlung gegen Einstein, J_iso')
    a1.legend(fontsize=6.5)
    a2 = ax[2]
    mi = zu['mitfuehrung']['iso']
    kls = sorted(mi.keys(), key=lambda s_: float(s_.split('_')[1]))
    klv = [mi[k_]['kl'] for k_ in kls]
    a2.semilogx(klv, [mi[k_]['R_iso'] for k_ in kls], 'ko-', label='R_iso (Mittel, quer)')
    a2.fill_between(klv, [mi[k_]['r_min'] for k_ in kls], [mi[k_]['r_max'] for k_ in kls], color='gray', alpha=0.25,
                    label='Spanne r(n, e) ueber Richtungen')
    for nm, cc in farben.items():
        a2.semilogx(klv, [mi[k_]['R_rot'][nm] for k_ in kls], '^-', color=cc, ms=4, label='rotierend, L = %s' % nm)
        a2.semilogx(klv, [mi[k_]['R_mov'][nm] for k_ in kls], 'v:', color=cc, ms=4, label='bewegt, v = %s' % nm)
    a2.axhline(1, color='k', lw=0.8)
    a2.axhspan(0.9, 1.1, color='#2ca02c', alpha=0.12, label='IN3-Band 1 +- 0,1')
    a2.set_xlabel('k l'); a2.set_ylabel('Mitfuehrung Gitter / Einstein')
    a2.set_title('Mitfuehrung (gravitomagnetisch), J_iso')
    a2.legend(fontsize=6)
    fig.suptitle('IMPULS-NETZ-1: Netz V, A1R1, Impulsregel M^H p = J (synthetische Gitterrechnung, keine Messdaten)')
    fig.tight_layout()
    fig.savefig(pfad_bild + '.tmp.png', dpi=110)
    os.replace(pfad_bild + '.tmp.png', pfad_bild)
    return {'bild': pfad_bild}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf', 'zusatz', 'urteil', 'bild'])
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--voll', action='store_true')
    ap.add_argument('--nt', type=int, default=10)
    ap.add_argument('--nphi', type=int, default=20)
    ap.add_argument('--h1')
    ap.add_argument('--zusatz')
    ap.add_argument('--bild')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'pn_sha256': sha(os.path.abspath(pn.__file__)),
            'ew_sha256': sha(os.path.abspath(ew.__file__)), 'mn_sha256': sha(os.path.abspath(mn.__file__)),
            'tp_sha256': sha(os.path.abspath(ew.tp.__file__)), 'ni_sha256': sha(os.path.abspath(ni.__file__))}
    res = {'info': info}
    if a.modus == 'lauf':
        res['lauf'] = lauf(rauch=a.rauch, nt=a.nt, nphi=a.nphi, voll=a.voll)
    elif a.modus == 'zusatz':
        res['zusatz'] = zusatz(rauch=a.rauch, voll=a.voll)
    elif a.modus == 'urteil':
        res['urteil'] = urteil(a.h1, a.zusatz)
    else:
        info['h1_sha256'] = sha(a.h1)
        info['zusatz_sha256'] = sha(a.zusatz)
        res['bild'] = bild(a.h1, a.zusatz, a.bild)
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], 'maxrss %.0f MB' % res['maxrss_MB'], flush=True)


if __name__ == '__main__':
    main()
