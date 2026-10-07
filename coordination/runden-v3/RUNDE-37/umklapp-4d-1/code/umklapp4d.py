#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-4D-1 (fmhc-physics, Runde 50, ohne Karte), Code-Agent fuer die Leitung claude-primary.

Frage: Wird der Energiesprung der Geometrie beim 2-3-Zug kleiner, wenn die Traegheit aus der 4D-Zeltwirkung kommt
(M_eff der stetigen Grenze, h = 2^-10) statt aus Form A2 (KANON-TRANSFER-1)?

Aufbau:
  Faelle wie KANON-TRANSFER-1 (Glas N = 128, gespeicherte Verschiebung bei mu = -1e-3, Newton bei mu = -1e-4),
  Zug X (und Y) als 2-3-Zug auf der Ausgangszerlegung.
  Je Zerlegung (vor und nach dem Zug): 4D-Zeltgitter ueber der ganzen periodischen Box (Grundzelle = Box, Bloch k = 0),
  Hubfolge nach Eckindex (wie V-A: Rang b = b, Hoehe b / N), Zelthoehe h = 2^-10. Bloecke wie uw.bloecke2 (Schema ls,
  Fassung B), hier reell gerechnet: bei k = 0 sind alle Phasen 1, die Taylor-Faktoren i^p werden herausgezogen
  (P_p = i^p Pr_p, S_p = i^p Sr_p, M_eff = S_2 = -Sr_2 auf q). M_eff in tg-Kanten ueber uv.Zuordnung.
  3D-Hamiltonform wie td.Netz (dieselbe S, dieselbe B_red), nur A = M_eff^-1 statt A2: A_red = S^T M_eff^-1 S
  (wie uv.reduktion: Ar = S^H Meff^-1 S).
  Uebergabe td.abbilden unveraendert: Lesart R (Laengen und Raten stetig, neue Kante aus der flachen Fortsetzung der
  Doppelpyramide, dann Projektion); Lesart P (Impulse stetig, neue Kante p = 0, Projektion).
  Zum Vergleich Form A2 im selben Lauf neu gerechnet (wie kanon.py) und gegen die gespeicherten KANON-TRANSFER-1-Werte.
Unveraendert importiert: konfluenz, td, hm_td, tg, uk, tu (kanon-transfer-1/code) und uv, rk, rk2, pt, hm, tti
(ueberleitung-v-2/code).
Modi: rauch (Kontrollen, Zeiten), lauf (ein Fall, ein mu), tabelle (alle Laufdateien -> Markdown und JSON).
"""
import argparse, json, os, sys, time, types, copy, platform, resource, glob
import numpy as np
import scipy
import scipy.linalg as sla

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import tg  # noqa: E402
import uk  # noqa: E402
import tu  # noqa: E402
import td  # noqa: E402
import hm_td  # noqa: E402
import konfluenz as kf  # noqa: E402
import uv  # noqa: E402
import rk  # noqa: E402
import rk2  # noqa: E402

H_HAUPT = 2.0 ** -10
TOL = 1e-10
LESARTEN = ['R', 'P']
sha = kf.sha
schreibe = kf.schreibe


# ================================================================================================= 4D-Seite
HUBFOLGE = 'index'                       # 'index' (Haupt, wie V-A), 'umgekehrt', 'zufall' (nur Kontrolle)
SAAT_HUB = 5101


def gitter_glas(LV, pos, G, O, h):
    """4D-Zeltgitter ueber der Glasbox (Grundzelle = Box), Hubfolge nach Eckindex, Hoehen b / N (wie V-A)."""
    NV = len(pos)
    tets3 = [[(int(G[t, i]), tuple(int(x) for x in O[t, i])) for i in range(4)] for t in range(len(G))]
    if HUBFOLGE == 'index':
        folge = list(range(NV))
    elif HUBFOLGE == 'umgekehrt':
        folge = list(range(NV))[::-1]
    else:
        folge = [int(x) for x in np.random.default_rng(SAAT_HUB).permutation(NV)]
    rang = {b: j for j, b in enumerate(folge)}
    hb = [rang[b] / float(NV) for b in range(NV)]
    return rk.Gitter('glas', np.asarray(pos, float), hb, LV.T, tets3, rk2.ord_rang(rang), h)


_BAU = {}
_baue_orig = uv.baue_gitter


def _baue(netz, h):
    if netz == 'glas':
        return gitter_glas(*_BAU['glas'], h)
    return _baue_orig(netz, h)


uv.baue_gitter = _baue                    # uv.Vier.__init__ ruft uv.baue_gitter


def L_basis_reell(self, ks, schema):
    """Wie uv.Vier.L_basis (Schema ls), bei k = 0 reell (SVD einer reellen Matrix)."""
    assert schema == 'ls' and not np.any(ks)
    w1, w2 = uv.SCHEMA_W[schema]
    By = self.shift_matrix(ks, w1, w2)
    assert np.abs(By.imag).max() == 0.0
    U, sv, _ = np.linalg.svd(By.real, full_matrices=True)
    rB = int((sv > 1e-9 * sv[0]).sum())
    return U[:, rB:], rB


def bloecke_reell(V, mit_J_sv=True):
    """Wie uw.bloecke2 bei k = 0 (pmax = 2), reell. Rueckgabe Sr_0, Sr_1, Sr_2 (S_p = i^p Sr_p) und Diagnose."""
    h = V.h
    ks = np.zeros(3)
    C = V.lau.koeff(ks)
    lD = V.g.l
    Ca = {}
    for m, Cm in C.items():
        assert np.abs(Cm.imag).max() == 0.0
        Ca[m] = lD[:, None] * Cm.real * lD[None, :]
    del C
    fak = [1.0, 1.0, 2.0]
    Hr = [sum(Ca[m] * (m * h) ** p for m in Ca) / fak[p] for p in range(3)]
    del Ca
    V.L_basis = types.MethodType(L_basis_reell, V)
    Jm, nL, rB = V.J_mats(ks, 'ls')
    Jrm = {}
    for m, X in Jm.items():
        assert np.abs(X.imag).max() == 0.0
        Jrm[m] = np.ascontiguousarray(X.real)
    del Jm
    Jr = [sum(Jrm[m] * (m * h) ** p for m in Jrm) / fak[p] for p in range(3)]
    del Jrm
    HJ = {}
    for b in range(3):
        for c in range(3 - b):
            HJ[(b, c)] = Hr[b] @ Jr[c]
    Pr = []
    for p in range(3):
        X = 0.0
        for a in range(p + 1):
            Y = sum(HJ[(b, p - a - b)] for b in range(p + 1 - a))
            X = X + ((-1.0) ** a) * (Jr[a].T @ Y)
        Pr.append(-X / h)
    del HJ, Hr
    diag = {'NE': int(V.NE), 'NV': int(V.NV), 'nq': int(V.nq), 'n_L': int(nL), 'rang_B_s': int(rB),
            'n_tot': len(V.tot),
            'P_sym': [float(np.abs(Pr[p] - (1 if p != 1 else -1) * Pr[p].T).max() / np.abs(Pr[p]).max())
                      for p in range(3)]}
    rows_live = [e for e in range(V.NE) if e not in V.tot]
    if mit_J_sv:
        sv = np.linalg.svd(Jr[0][rows_live], compute_uv=False)
        diag['J_sv_min_rel'] = float(sv[-1] / sv[0])
        diag['J_rang_ok'] = bool(sv[-1] > 1e-10 * sv[0] and Jr[0].shape[1] <= len(rows_live) and rB == 3 * V.NV)
    nK = V.nq + 4 * V.NV
    IK = np.arange(nK)
    IL = np.arange(nK, nK + nL)
    A = [P[np.ix_(IK, IK)] for P in Pr]
    B = [P[np.ix_(IK, IL)] for P in Pr]
    Bt = [P[np.ix_(IL, IK)] for P in Pr]
    D = [P[np.ix_(IL, IL)] for P in Pr]
    del Pr
    evD = np.linalg.eigvalsh(0.5 * (D[0] + D[0].T))
    amax = float(np.abs(evD).max())
    diag.update({'D0_min_rel': float(np.abs(evD).min() / amax), 'D0_n_neg': int((evD < 0).sum()),
                 'D0_eig_min_rel': float(evD.min() / amax), 'D0_absmax': amax})
    if diag['D0_min_rel'] < 1e-10:
        diag['grund'] = 'D0_singulaer'
        return None, diag
    E0 = np.linalg.inv(D[0])
    E = [E0]
    for p in range(1, 3):
        E.append(-E0 @ sum(D[j] @ E[p - j] for j in range(1, p + 1)))
    Sr = []
    for p in range(3):
        X = A[p].copy()
        for a in range(p + 1):
            for b in range(p + 1 - a):
                X = X - B[a] @ E[b] @ Bt[p - a - b]
        Sr.append(X)
    return Sr, diag


def meff_aus_4d(LV, pos, G, O, mod, h=H_HAUPT, mit_J_sv=True):
    """M_eff (= S_2 auf q), V_eff (= S_0 auf q), C (= S_0 qn) in tg-Kanten fuer die Zerlegung (G, O)."""
    t0 = time.time()
    _BAU['glas'] = (LV, pos, G, O)
    V = uv.Vier('glas', h)
    t1 = time.time()
    Sr, dg = bloecke_reell(V, mit_J_sv)
    t2 = time.time()
    dg['t_vier_s'] = t1 - t0
    dg['t_bloecke_s'] = t2 - t1
    if Sr is None:
        return None, dg
    zu = uv.Zuordnung(V, mod, LV)
    U = zu.U(np.zeros(3))
    assert np.abs(U.imag).max() == 0.0
    U = U.real
    nq, NV = V.nq, V.NV
    S2 = -Sr[2][:nq, :nq]
    S0 = Sr[0]
    dg['S2_asym'] = float(np.abs(S2 - S2.T).max() / np.abs(S2).max())
    dg['S1_qq_rel'] = float(np.abs(Sr[1][:nq, :nq]).max() / np.abs(S0[:nq, :nq]).max())
    M = U.T @ S2 @ U
    M = 0.5 * (M + M.T)
    Ve = U.T @ S0[:nq, :nq] @ U
    Ve = 0.5 * (Ve + Ve.T)
    C = U.T @ S0[:nq, nq:nq + NV]
    ev = np.linalg.eigvalsh(M)
    s = float(np.abs(ev).max())
    dg.update({'M_n_neg': int((ev < -TOL * s).sum()), 'M_n_null': int((np.abs(ev) <= TOL * s).sum()),
               'M_absmin_rel': float(np.abs(ev).min() / s), 'M_eig_min': float(ev.min()), 'M_eig_max': float(ev.max()),
               'M_eig_neg_max': float(ev[ev < 0].max()) if (ev < 0).any() else None,
               'M_eig_pos_min': float(ev[ev > 0].min()) if (ev > 0).any() else None,
               't_gesamt_s': time.time() - t0})
    return {'M': M, 'V': Ve, 'C': C}, dg


# ================================================================================================= 3D-Seite
def netz_meff(NA1, M):
    """td.Netz (A1) kopieren und A = M^-1 setzen: A_red = S^T M^-1 S (wie uv.reduktion)."""
    N = copy.copy(NA1)
    A = np.linalg.inv(M)
    A = 0.5 * (A + A.T)
    N.A_voll = A
    Ar = N.S.T @ A @ N.S
    N.Ar = 0.5 * (Ar + Ar.T)
    N.lu = sla.lu_factor(N.Ar)
    eA = np.linalg.eigvalsh(N.Ar)
    N.n_A_neg = int((eA < -1e-12 * np.abs(eA).max()).sum())
    N.A_min_rel = float(eA.min() / np.abs(eA).max())
    try:
        N.L = np.linalg.cholesky(N.Ar)
        N.A_pd = True
    except np.linalg.LinAlgError:
        N.L = None
        N.A_pd = False
    return N


def geo_zug(n0, n1, b, k1):
    """TT-Mode auf n0 (wie kanon.py), Uebergabe R und P auf n1; Spruenge gesamt, Potential, kinetisch."""
    out = {'A_pd_vor': bool(n0.A_pd), 'A_pd_nach': bool(n1.A_pd), 'n_A_neg_vor': int(n0.n_A_neg),
           'n_A_neg_nach': int(n1.n_A_neg)}
    if not n0.A_pd:
        out['grund'] = 'A_red vor dem Zug nicht positiv definit'
        return out
    mode, xm, w2, Qm = td.tt_mode(n0, kf.A_Q, k1)
    x0 = np.sin(kf.PHASE) * xm
    y0 = sla.lu_solve(n0.lu, mode['omega'] * np.cos(kf.PHASE) * xm)
    H0, V0, K0 = n0.energie(x0, y0)
    out.update({'omega': mode['omega'], 'omega_durch_k1': mode['omega'] / float(np.linalg.norm(k1)),
                'anteil_TT_welle': mode['anteil_TT_welle'], 'H0': float(H0), 'V0': float(V0), 'K0': float(K0)})
    for L in LESARTEN:
        x1, y1, info = td.abbilden(n0, n1, x0, y0, b, L)
        H1, V1, K1 = n1.energie(x1, y1)
        out['dH_' + L] = float(H1 - H0)
        out['dV_' + L] = float(V1 - V0)
        out['dK_' + L] = float(K1 - K0)
        out['proj_rest_a_' + L] = info['proj_rest_a']
        if 'proj_rest_p' in info:
            out['proj_rest_p_' + L] = info['proj_rest_p']
    return out


def einbettung(N0, N1, b):
    """J (E1 x E0): gemeinsame Kanten Einheit, neue Kante d-e = jrow . a9 (flache Fortsetzung, wie td.abbilden R)."""
    idx, ok = N1.idx_von_keys(N0.keys)
    assert ok.all()
    J = np.zeros((N1.E, N0.E))
    J[idx, np.arange(N0.E)] = 1.0
    i9, ok9 = N0.idx_von_keys(b['k9'])
    assert ok9.all()
    jr, _ = td.jrow_flach(N0.l0[i9])
    inew, okn = N1.idx_von_keys(np.array([b['kante_neu']]))
    assert okn[0]
    J[inew[0], i9] = jr
    return J, idx, int(inew[0])


def sprung_matrizen(J, idx, M0, M1, A0, A1, B0, B1):
    """Beschreibend: relative Aenderung der Lagrange-Masse (J^T M1 J gegen M0), der Hamilton-Masse auf den alten
    Kanten (A1[alt, alt] gegen A0) und des Potentials (J^T B1 J gegen B0), Frobenius."""
    def r(X, Y):
        return float(np.linalg.norm(X - Y) / np.linalg.norm(Y))
    out = {}
    if M0 is not None:
        out['dM_pull_rel'] = r(J.T @ M1 @ J, M0)
    out['dA_alt_rel'] = r(A1[np.ix_(idx, idx)], A0)
    out['dB_pull_rel'] = r(J.T @ B1 @ J, B0)
    return out


# ================================================================================================= ein Fall
def basis_laden(saat):
    LV, pos, G0, O0, pr = tg.zufallsnetz(128, saat)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    Nu = kf.netz('A1', LV, pos, G0, O0, k1, hp, hx)
    return {'LV': LV, 'pos': pos, 'G0': G0, 'O0': O0, 'k1': k1, 'hp': hp, 'hx': hx, 'fl': Nu.fl,
            'lbar': float(Nu.l0.mean()), 'vbar': float(Nu.vbar), 'vz0': tu.vorzeichen_vol(LV, pos, G0, O0)}


def lagen(f, mu_ziel, ba):
    """Verschobene Lagen wie kanon.fall (gespeichert bei 1e-3, Newton bei 1e-4) und Gueltigkeit."""
    LV, pos, G0, O0, fl, lbar = ba['LV'], ba['pos'], ba['G0'], ba['O0'], ba['fl'], ba['lbar']
    X, Y = int(f['X']), int(f['Y'])
    ecken = f['verschiebung']['ecken']
    if mu_ziel == 1e-3:
        vs = [(int(v), np.array(dl, float)) for v, dl in ecken]
    else:
        kf.MU_ZIEL = mu_ziel
        try:
            if len(ecken) == 1:
                v = int(ecken[0][0])
                vs = [(v, kf.newton(LV, pos, G0, O0, fl, v, [X, Y], lbar))]
            else:
                vs = [(int(ecken[0][0]), kf.newton(LV, pos, G0, O0, fl, int(ecken[0][0]), [X], lbar)),
                      (int(ecken[1][0]), kf.newton(LV, pos, G0, O0, fl, int(ecken[1][0]), [Y], lbar))]
        finally:
            kf.MU_ZIEL = 1e-3
        if any(dl is None for _, dl in vs):
            return None, {'gueltig': False, 'grund': 'newton'}
    pos2 = pos.copy()
    for v, dl in vs:
        pos2[v] = pos2[v] + dl
    mu = uk.raender(LV, pos2, G0, O0, fl)
    verl = set(np.nonzero(mu < -tu.TOL_MU)[0].tolist())
    mo = mu.copy()
    mo[[X, Y]] = np.inf
    info = {'mu_X': float(mu[X]), 'mu_Y': float(mu[Y]), 'mu_andere_min': float(mo.min()),
            'nur_X_Y_verletzt': verl == {X, Y},
            'vorzeichen_gleich': bool(np.array_equal(tu.vorzeichen_vol(LV, pos2, G0, O0), ba['vz0'])),
            'norm_rel_max': float(max(np.linalg.norm(dl) for _, dl in vs) / lbar)}
    info['gueltig'] = bool(info['nur_X_Y_verletzt'] and info['vorzeichen_gleich'])
    return pos2, info


def fall_lauf(saat, nr, mu_ziel, zuege, kanon_pfad, h=H_HAUPT, mit_J_sv=True):
    T0 = time.time()
    d = json.load(open(os.path.join(HIER, '..', 'eingabe', 'konfluenz-s%d.json' % saat)))['ergebnis']
    assert int(d['saat']) == saat
    f = d['faelle'][nr]
    ba = basis_laden(saat)
    LV, G0, O0, k1, hp, hx = ba['LV'], ba['G0'], ba['O0'], ba['k1'], ba['hp'], ba['hx']
    pos2, info = lagen(f, mu_ziel, ba)
    out = {'saat': saat, 'nr': nr, 'art': f['art'], 'X': int(f['X']), 'Y': int(f['Y']), 'mu': -mu_ziel, 'h': h,
           'lagen': info, 'zuege': {}}
    if pos2 is None or not info['gueltig']:
        return out
    # gespeicherte A2-Werte (KANON-TRANSFER-1)
    gesp = None
    if kanon_pfad and os.path.exists(kanon_pfad):
        kd = json.load(open(kanon_pfad))['ergebnis']
        for kfall in kd['faelle']:
            if kfall['nr'] == nr:
                gesp = kfall['mu']['%g' % mu_ziel]
        out['kanon_sha256'] = sha(kanon_pfad)
    # Ausgangsnetze
    NA1_0 = kf.netz('A1', LV, pos2, G0, O0, k1, hp, hx)
    vmin = td.VMIN_B * NA1_0.vbar
    _, geo = tu.flaechen_geo(LV, pos2, G0, O0)
    hm_td.VREF = None
    n2_0 = kf.netz('A2', LV, pos2, G0, O0, k1, hp, hx)
    out['vref'] = hm_td.VREF
    m0, dg0 = meff_aus_4d(LV, pos2, G0, O0, NA1_0.mod, h, mit_J_sv)
    out['meff_vor'] = dg0
    Bs, A1s, Mm, cc = tg.ops(NA1_0.mod, np.zeros(3))
    B0 = Bs.real.toarray()
    c0 = cc.real
    if m0 is not None:
        out['meff_vor']['r_V_gegen_B'] = float(np.linalg.norm(m0['V'] - B0) / np.linalg.norm(B0))
        kap = float(np.sum(c0 * m0['C']) / np.sum(c0 * c0))
        out['meff_vor']['kappa'] = kap
        out['meff_vor']['C_rest_kappa'] = float(np.linalg.norm(m0['C'] - kap * c0) / np.linalg.norm(m0['C']))
        nm_0 = netz_meff(NA1_0, m0['M'])
    for name in zuege:
        j = int(f['X']) if name == 'X' else int(f['Y'])
        t1 = time.time()
        w = kf.zug_waehlen(NA1_0, j, vmin, geo)
        z = {'flaeche': j}
        if w is None or w[0] != 23:
            z.update({'gueltig': False, 'grund': 'kein 2-3' if w is not None else 'nicht ausfuehrbar'})
            out['zuege'][name] = z
            continue
        typ, r, (Gn, On, b) = w
        z['gueltig'] = True
        NA1_1 = kf.netz('A1', LV, pos2, Gn, On, k1, hp, hx)
        n2_1 = kf.netz('A2', LV, pos2, Gn, On, k1, hp, hx)
        J, idx, inew = einbettung(NA1_0, NA1_1, b)
        Bs1, _, _, _ = tg.ops(NA1_1.mod, np.zeros(3))
        B1 = Bs1.real.toarray()
        # Form A2 (wie kanon.py)
        z['A2'] = geo_zug(n2_0, n2_1, b, k1)
        z['A2'].update(sprung_matrizen(J, idx, None, None, n2_0.A.toarray(), n2_1.A.toarray(), B0, B1))
        if gesp is not None and gesp.get('gueltig'):
            gz = gesp['zuege'][name].get('geo', {})
            z['A2_gespeichert'] = {L: gz.get('dH_' + L) for L in LESARTEN}
            z['A2_gespeichert']['Hg0'] = gz.get('Hg0')
        # Form M_eff
        if m0 is not None:
            m1, dg1 = meff_aus_4d(LV, pos2, Gn, On, NA1_1.mod, h, mit_J_sv)
            z['meff_nach'] = dg1
            if m1 is not None:
                nm_1 = netz_meff(NA1_1, m1['M'])
                z['M'] = geo_zug(nm_0, nm_1, b, k1)
                z['M'].update(sprung_matrizen(J, idx, m0['M'], m1['M'], nm_0.A_voll, nm_1.A_voll, B0, B1))
                z['M']['dV_eff_pull_rel'] = float(np.linalg.norm(J.T @ m1['V'] @ J - m0['V']) / np.linalg.norm(m0['V']))
        z['t_s'] = time.time() - t1
        out['zuege'][name] = z
    out['t_s'] = time.time() - T0
    return out


# ================================================================================================= Rauchtest
def rauch(args):
    out = {}
    # (1) reell gegen komplex auf V bei k = 0 (uw/uv-Code, NE = 146)
    t0 = time.time()
    try:
        Vv = uv.Vier('V', H_HAUPT)
        Sc, dc = Vv.bloecke(np.zeros(3), 'ls', 2)
        Vv2 = uv.Vier('V', H_HAUPT)
        Sr, dr = bloecke_reell(Vv2)
        r = {'diag_komplex': {k: v for k, v in dc.items()}, 'diag_reell': dr}
        if Sc is not None and Sr is not None:
            nq = Vv.nq
            r['S2_rel'] = float(np.abs(Sc[2][:nq, :nq] - (-Sr[2][:nq, :nq])).max() / np.abs(Sc[2][:nq, :nq]).max())
            r['S0_rel'] = float(np.abs(Sc[0] - Sr[0]).max() / np.abs(Sc[0]).max())
            r['S1_rel'] = float(np.abs(Sc[1] - 1j * Sr[1]).max() / np.abs(Sc[1]).max())
        out['V_k0'] = r
    except Exception as e:  # noqa: BLE001
        out['V_k0'] = {'fehler': repr(e)}
    out['t_V_s'] = time.time() - t0
    # (2) ein Glasfall, mu = -1e-3, Zug X
    out['glas'] = fall_lauf(args.saat, args.fall, 1e-3, ['X'], args.kanon, H_HAUPT, True)
    # (3) Konvergenz in h: M_eff des Ausgangsnetzes bei 2^-12 (nur mit --h12)
    if args.h12:
        d = json.load(open(os.path.join(HIER, '..', 'eingabe', 'konfluenz-s%d.json' % args.saat)))['ergebnis']
        f = d['faelle'][args.fall]
        ba = basis_laden(args.saat)
        pos2, info = lagen(f, 1e-3, ba)
        NA1 = kf.netz('A1', ba['LV'], pos2, ba['G0'], ba['O0'], ba['k1'], ba['hp'], ba['hx'])
        ma, da = meff_aus_4d(ba['LV'], pos2, ba['G0'], ba['O0'], NA1.mod, 2.0 ** -10, False)
        mb, db = meff_aus_4d(ba['LV'], pos2, ba['G0'], ba['O0'], NA1.mod, 2.0 ** -12, False)
        out['h12'] = {'diag_10': da, 'diag_12': db}
        if ma is not None and mb is not None:
            out['h12']['r12_M'] = float(np.linalg.norm(mb['M'] - ma['M']) / np.linalg.norm(ma['M']))
            out['h12']['r12_V'] = float(np.linalg.norm(mb['V'] - ma['V']) / np.linalg.norm(ma['V']))
    return out


# ================================================================================================= Tabelle
def g3(x):
    if x is None:
        return '-'
    if x == 0:
        return '0'
    return '%.3g' % x


def tabelle(ordner, out_md, out_json, muster='u4-s*-f*-mu*.json'):
    zeilen = []
    for p in sorted(glob.glob(os.path.join(ordner, muster))):
        dd = json.load(open(p))
        e = dd.get('ergebnis')
        if not e:
            continue
        for zn, z in e.get('zuege', {}).items():
            if not z.get('gueltig'):
                zeilen.append({'datei': os.path.basename(p), 'saat': e['saat'], 'nr': e['nr'], 'art': e['art'],
                               'zug': zn, 'mu': e['mu'], 'gueltig': False, 'grund': z.get('grund')})
                continue
            a2, m = z.get('A2', {}), z.get('M', {})
            r = {'datei': os.path.basename(p), 'saat': e['saat'], 'nr': e['nr'], 'art': e['art'], 'zug': zn,
                 'mu': e['mu'], 'gueltig': True, 'mu_zug': e['lagen']['mu_' + zn]}
            for tag, g in (('A2', a2), ('M', m)):
                for k in ('H0', 'V0', 'K0', 'omega_durch_k1', 'dH_R', 'dH_P', 'dV_R', 'dK_R', 'dV_P', 'dK_P',
                          'proj_rest_a_R', 'dM_pull_rel', 'dA_alt_rel', 'dB_pull_rel', 'A_pd_vor', 'A_pd_nach',
                          'n_A_neg_vor', 'n_A_neg_nach'):
                    r[tag + '_' + k] = g.get(k)
                for L in LESARTEN:
                    if g.get('H0') and g.get('dH_' + L) is not None:
                        r[tag + '_rel_' + L] = abs(g['dH_' + L]) / g['H0']
            r['A2_gesp_R'] = z.get('A2_gespeichert', {}).get('R')
            r['A2_gesp_P'] = z.get('A2_gespeichert', {}).get('P')
            mv, mn = e.get('meff_vor', {}), z.get('meff_nach', {})
            for k in ('M_n_neg', 'M_n_null', 'M_absmin_rel', 'D0_n_neg', 'D0_min_rel', 'J_sv_min_rel', 'r_V_gegen_B',
                      'kappa', 'C_rest_kappa'):
                r['vor_' + k] = mv.get(k)
                r['nach_' + k] = mn.get(k)
            zeilen.append(r)
    # Verhaeltnisse mu = -1e-3 / -1e-4 je Zug
    by = {}
    for r in zeilen:
        if r['gueltig']:
            by.setdefault((r['saat'], r['nr'], r['zug']), {})[r['mu']] = r
    verh = []
    for key, v in sorted(by.items()):
        if -1e-3 in v and -1e-4 in v:
            q = {'saat': key[0], 'nr': key[1], 'zug': key[2]}
            for tag in ('A2', 'M'):
                for L in LESARTEN:
                    a, b_ = v[-1e-3].get(tag + '_dH_' + L), v[-1e-4].get(tag + '_dH_' + L)
                    q[tag + '_' + L] = (abs(a) / abs(b_)) if (a is not None and b_) else None
                    q[tag + '_' + L + '_p'] = float(np.log10(q[tag + '_' + L])) if q[tag + '_' + L] else None
            verh.append(q)
    L_ = ['# UMKLAPP-4D-1: Tabelle (synthetisch, keine Messdaten)', '',
          '| Saat | Fall | Art | Zug | mu | A2 dH_R | A2 dH_P | A2 gespeichert R / P | M_eff dH_R | M_eff dH_P | '
          'A2 rel R / P | M_eff rel R / P | M_eff omega/k1 | A2 omega/k1 |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in zeilen:
        if not r['gueltig']:
            L_.append('| %d | %d | %s | %s | %g | ungueltig: %s | | | | | | | | |' % (r['saat'], r['nr'], r['art'], r['zug'],
                                                                                  r['mu'], r['grund']))
            continue
        L_.append('| %d | %d | %s | %s | %g | %s | %s | %s / %s | %s | %s | %s / %s | %s / %s | %s | %s |' % (
            r['saat'], r['nr'], r['art'], r['zug'], r['mu'], g3(r['A2_dH_R']), g3(r['A2_dH_P']), g3(r['A2_gesp_R']),
            g3(r['A2_gesp_P']), g3(r['M_dH_R']), g3(r['M_dH_P']), g3(r.get('A2_rel_R')), g3(r.get('A2_rel_P')),
            g3(r.get('M_rel_R')), g3(r.get('M_rel_P')), g3(r['M_omega_durch_k1']), g3(r['A2_omega_durch_k1'])))
    L_ += ['', '## Zerlegung (Potential dV, kinetisch dK) je Lesart', '',
           '| Saat | Fall | Zug | mu | A2 dV_R | A2 dK_R | A2 dK_P | M dV_R | M dK_R | M dK_P | A2 dA_alt | M dA_alt | M dM_pull | dB_pull |',
           '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in zeilen:
        if r['gueltig']:
            L_.append('| %d | %d | %s | %g | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
                r['saat'], r['nr'], r['zug'], r['mu'], g3(r['A2_dV_R']), g3(r['A2_dK_R']), g3(r['A2_dK_P']),
                g3(r['M_dV_R']), g3(r['M_dK_R']), g3(r['M_dK_P']), g3(r['A2_dA_alt_rel']), g3(r['M_dA_alt_rel']),
                g3(r['M_dM_pull_rel']), g3(r['M_dB_pull_rel'])))
    L_ += ['', '## M_eff-Kontrollen', '',
           '| Saat | Fall | Zug | mu | n_neg vor / nach | n_null | min abs rel | D0 n_neg vor / nach | D0 min rel | J sv min | r_V | kappa | A_red pd vor / nach (n_neg) |',
           '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in zeilen:
        if r['gueltig']:
            L_.append('| %d | %d | %s | %g | %s / %s | %s / %s | %s / %s | %s / %s | %s / %s | %s | %s | %s | %s / %s (%s / %s) |' % (
                r['saat'], r['nr'], r['zug'], r['mu'], r['vor_M_n_neg'], r['nach_M_n_neg'], r['vor_M_n_null'],
                r['nach_M_n_null'], g3(r['vor_M_absmin_rel']), g3(r['nach_M_absmin_rel']), r['vor_D0_n_neg'],
                r['nach_D0_n_neg'], g3(r['vor_D0_min_rel']), g3(r['nach_D0_min_rel']), g3(r['vor_J_sv_min_rel']),
                g3(r['vor_r_V_gegen_B']), g3(r['vor_kappa']), r['M_A_pd_vor'], r['M_A_pd_nach'], r['M_n_A_neg_vor'],
                r['M_n_A_neg_nach']))
    L_ += ['', '## Verhaeltnis |dH(mu = -1e-3)| / |dH(mu = -1e-4)| je Zug (log10 = Exponent p)', '',
           '| Saat | Fall | Zug | A2 R | A2 P | M_eff R | M_eff P |', '|---|---|---|---|---|---|---|']
    for q in verh:
        L_.append('| %d | %d | %s | %s | %s | %s | %s |' % (q['saat'], q['nr'], q['zug'], g3(q['A2_R']), g3(q['A2_P']),
                                                         g3(q['M_R']), g3(q['M_P'])))
    with open(out_md + '.tmp', 'w') as fh:
        fh.write('\n'.join(L_) + '\n')
    os.replace(out_md + '.tmp', out_md)
    schreibe(out_json, {'zeilen': zeilen, 'verhaeltnisse': verh})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'lauf', 'tabelle'])
    ap.add_argument('--saat', type=int, default=1)
    ap.add_argument('--fall', type=int, default=0)
    ap.add_argument('--mu', type=float, default=1e-3)
    ap.add_argument('--zuege', default='X')
    ap.add_argument('--kanon', default=None)
    ap.add_argument('--h12', action='store_true')
    ap.add_argument('--ordner', default='lauf')
    ap.add_argument('--out', required=True)
    ap.add_argument('--md', default=None)
    ap.add_argument('--h', type=float, default=H_HAUPT)
    ap.add_argument('--hubfolge', default='index', choices=['index', 'umgekehrt', 'zufall'])
    ap.add_argument('--muster', default='u4-s*-f*-mu*.json')
    a = ap.parse_args()
    t0 = time.time()
    me = os.path.abspath(__file__)
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'skript_sha256': sha(me),
            'module_sha256': {m.__name__: sha(os.path.abspath(m.__file__)) for m in (tg, uk, tu, td, hm_td, kf, uv, rk, rk2)},
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'tabelle':
        tabelle(a.ordner, a.md, a.out, a.muster)
        print('fertig tabelle', flush=True)
        return
    if a.modus == 'rauch':
        erg = rauch(a)
    else:
        global HUBFOLGE
        HUBFOLGE = a.hubfolge
        erg = fall_lauf(a.saat, a.fall, a.mu, a.zuege.split(','), a.kanon, a.h)
        erg['hubfolge'] = HUBFOLGE
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
