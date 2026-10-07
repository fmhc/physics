#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KANON-TRANSFER-1 (Runde 49, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage (KARTE.md): Wie gross sind Energie- und Ladungsfehler des Eckenskalars am Umklappzug mit den Transfers R, P und
dem kanonischen Transfer K (mit Rueckstoss in den geometrischen Impuls), und wie viel des Gesamtsprungs ist Skalar?

Aufbau (PLAN.md):
  Faelle: die 32 gespeicherten Faelle aus UEBERGABE-KONFLUENZ-1 (eingabe/konfluenz-s1..4.json). Verschobenes Netz bei
  mu = -1e-3 (gespeicherte Verschiebung) und mu = -1e-4 (dieselben Ecken, konfluenz.newton mit MU_ZIEL = 1e-4).
  Zuege: X und Y je als erster Zug (2-3) auf der Ausgangszerlegung, konfluenz.zug_waehlen -> td.zug_ausfuehren.
  Skalar: H = sum |pi|^2/(2 *0) + m^2/2 sum *0 |phi|^2 + Z_S/2 sum *1 |d0 phi|^2, Z_S = 8, *0, *1 umkreisbasiert.
  Zustaende: Z1 masselos reell (Welle wie UEBERGABE-KONFLUENZ-1, Phase pi/4 am Zugmittelpunkt), Z2 m = 1,
  omega = 0,8, rotierend, Gauss-Profil sigma = 3 l um den Zug.
  Transfers: R (pi' = D pi), P (pi' = pi), K (phi' = D^-1/2 phi, pi' = D^1/2 pi; Rueckstoss
  dp_a = sum_v Re(conj(pi_v) phi_v)/2 d ln D_v/d a im Kantenraum der neuen Zerlegung, y' += S'^T dp_a).
  Geometrie: Form A2 (hm_td, R1), TT-Mode wie UEBERGABE-KONFLUENZ-1, Lesarten R und P (td.abbilden unveraendert).
Unveraendert importiert: konfluenz.py, td.py, hm_td.py, tg.py, uk.py, tu.py (und deren Importe).
Modi: lauf (eine Saat), auswertung (Urteile nach PLAN 8), tabellen (nur Darstellung).
"""
import argparse, json, os, sys, time, platform, resource, glob
import numpy as np
import scipy
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import uk  # noqa: E402
import tu  # noqa: E402
import td  # noqa: E402
import hm_td  # noqa: E402
import konfluenz as kf  # noqa: E402

Z_S = 8.0                    # wie konfluenz.Z_S
A_Q = 1e-3                   # Geometrie: TT-Amplitude (wie UEBERGABE-KONFLUENZ-1)
PHASE = 1.0                  # Geometrie: Phase der stehenden Mode
A_PHI = 1e-3                 # Skalar-Amplitude Z1, Z2 (Relativgroessen haengen nicht davon ab)
M_Z2 = 1.0                   # Z2: Masse
OMEGA_Z2 = 0.8               # Z2: omega = 0,8 m
SIGMA_L = 3.0                # Z2: Gauss-Breite in mittleren Kantenlaengen
P0_Z1 = np.pi / 4            # Z1: k1 . r_c + p0 = pi/4
MU_LISTE = [1e-3, 1e-4]      # mu = -1e-3, -1e-4
H_CS = 1e-20                 # komplexer Schritt in a_e (Ableitung d *0 / d a, PLAN 5)
T_POS = [1e-5, 1e-6]         # Gegenprobe ueber Eckverschiebungen: Schrittweiten in Einheiten von l
SAAT_PROBE = 4911            # feste Saat der Verschiebungsrichtungen der Gegenprobe
TRANSFERS = ['R', 'P', 'K']
LESARTEN = ['R', 'P']
ZUSTAENDE = ['Z1', 'Z2']
FORM = 'A2'
TOL_KT0 = 1e-12
assert Z_S == kf.Z_S and A_Q == kf.A_Q and PHASE == kf.PHASE

MASKE = np.zeros((4, 6))     # Kante p (tg.PAARE) traegt zu Ecke i bei, wenn i ein Endpunkt ist
for _p, (_i, _j, _, _) in enumerate(tg.PAARE):
    MASKE[_i, _p] = 1.0
    MASKE[_j, _p] = 1.0

sha = kf.sha
schreibe = kf.schreibe


# ------------------------------------------------------------------------------------------------ Skalar
def teile(sk, phi, pi, m):
    kin = np.abs(pi) ** 2 / (2.0 * sk['s0'])
    mas = 0.5 * m * m * sk['s0'] * np.abs(phi) ** 2
    d = phi[sk['es2']] - phi[sk['es']]
    ge = 0.5 * Z_S * sk['s1'] * np.abs(d) ** 2
    return kin, mas, ge


def H_zerlegt(sk, phi, pi, m):
    kin, mas, ge = teile(sk, phi, pi, m)
    k, ms, g = float(kin.sum()), float(mas.sum()), float(ge.sum())
    return {'kin': k, 'masse': ms, 'grad': g, 'H': k + ms + g}


def grad_E(sk, phi):
    d = phi[sk['es2']] - phi[sk['es']]
    return float(0.5 * Z_S * np.sum(sk['s1'] * np.abs(d) ** 2))


def transfer(T, D, phi, pi):
    """R: phi' = phi, pi' = D pi; P: phi' = phi, pi' = pi; K: phi' = D^-1/2 phi, pi' = D^1/2 pi."""
    if T == 'R':
        return phi.copy(), D * pi
    if T == 'P':
        return phi.copy(), pi.copy()
    if T == 'K':
        w = np.sqrt(D)
        return phi / w, w * pi
    raise ValueError(T)


def rel_fehler(ist, soll):
    """max |ist - soll| / |soll| ueber Eintraege mit soll != 0; Eintraege mit soll = 0 absolut gegen max |soll|."""
    ist = np.ravel(np.asarray(ist))
    soll = np.ravel(np.asarray(soll))
    s = float(np.abs(soll).max()) if soll.size else 0.0
    if s == 0.0:
        return float(np.abs(ist).max()) if ist.size else 0.0
    m = np.abs(soll) > 0
    e1 = float(np.max(np.abs(ist[m] - soll[m]) / np.abs(soll[m]))) if m.any() else 0.0
    e0 = float(np.max(np.abs(ist[~m])) / s) if (~m).any() else 0.0
    return max(e1, e0)


def feldblock_fehler(T, D):
    """Klammer {phi'_v, pi'_w} aus den Jacobi-Matrizen des Transfercodes gegen diag(D) (R) bzw. Einheit (P, K)."""
    n = len(D)
    I = np.eye(n)
    z = np.zeros(n)
    Jff, Jpf, Jfp, Jpp = (np.zeros((n, n)) for _ in range(4))
    for v in range(n):
        a, b = transfer(T, D, I[:, v], z)
        Jff[:, v], Jpf[:, v] = a, b
        a, b = transfer(T, D, z, I[:, v])
        Jfp[:, v], Jpp[:, v] = a, b
    B = Jff @ Jpp.T - Jfp @ Jpf.T
    soll = np.diag(D) if T == 'R' else np.eye(n)
    return rel_fehler(B, soll)


# ------------------------------------------------------------------------------------------------ d ln D / d a
# Komplexer Schritt (Rauchtest r1: zentrale Differenzen in den Laengen scheitern an flachen Tetraedern, weil die
# gestoerten Laengen dort nicht mehr einbettbar sind). Dieselben Formeln wie td.tet_X_aus_laengen / td.hodge_teile,
# nur ohne np.maximum, Betrag und Vorzeichen auf komplexen Zahlen (Norm als Wurzel der Quadratsumme, Vorzeichen vom
# Realteil). Gegenprobe: Eckverschiebungen auf den Lagen (zentrale Differenzen, zwei Schrittweiten).
def einheit_c(v):
    return v / np.sqrt((v * v).sum(-1))[..., None]


def tet_X_c(L6):
    l01, l02, l03, l12, l13, l23 = [L6[:, q] for q in range(6)]
    x2 = (l01 ** 2 + l02 ** 2 - l12 ** 2) / (2 * l01)
    y2 = np.sqrt(l02 ** 2 - x2 ** 2)
    x3 = (l01 ** 2 + l03 ** 2 - l13 ** 2) / (2 * l01)
    y3 = (l03 ** 2 - l23 ** 2 + x2 ** 2 + y2 ** 2 - 2 * x3 * x2) / (2 * y2)
    z3 = np.sqrt(l03 ** 2 - x3 ** 2 - y3 ** 2)
    X = np.zeros((len(L6), 4, 3), dtype=complex)
    X[:, 1, 0] = l01
    X[:, 2, 0], X[:, 2, 1] = x2, y2
    X[:, 3, 0], X[:, 3, 1], X[:, 3, 2] = x3, y3, z3
    return X


def hodge_teile_c(X):
    """Wie td.hodge_teile (A*_e,t), komplex fortsetzbar."""
    ct = tu.umkreis_tet(X)
    Ast = np.zeros((len(X), 6), dtype=X.dtype)
    for p, (i, j, k, l) in enumerate(tg.PAARE):
        Xi, Xj, Xk, Xl = X[:, i], X[:, j], X[:, k], X[:, l]
        m = 0.5 * (Xi + Xj)
        e = einheit_c(Xj - Xi)
        hs, hh = [], []
        for Xo, Xa in ((Xk, Xl), (Xl, Xk)):
            u = (Xo - Xi) - ((Xo - Xi) * e).sum(-1)[:, None] * e
            u = einheit_c(u)
            cf = tu.umkreis_drei(Xi, Xj, Xo)
            hs.append(((cf - m) * u).sum(-1))
            nrm = np.cross(Xj - Xi, Xo - Xi)
            nrm = einheit_c(nrm * np.sign(((nrm * (Xa - Xi)).sum(-1)).real)[:, None])
            hh.append(((ct - cf) * nrm).sum(-1))
        Ast[:, p] = 0.5 * (hs[0] * hh[0] + hs[1] * hh[1])
    return Ast


def s0_beitraege_c(L6, slots):
    """Beitrag je Tetraeder (Laengen in tg.PAARE-Reihenfolge) zu *0 der Ecke an Platz slot (wie tu.hodge)."""
    return (MASKE[slots] * L6 * hodge_teile_c(tet_X_c(L6))).sum(1) / 6.0


def ds0_da(N, v):
    """*0_v aus den Laengen und d *0_v / d a_e (a_e = dl_e / l_e) je Kante von N; komplexer Schritt H_CS."""
    ts, slots = np.nonzero(N.G == v)
    E6 = N.mod['eidx'][ts]
    L6 = N.l0[E6].astype(complex)
    s0v = float(np.real(s0_beitraege_c(L6, slots)).sum())
    n = len(ts)
    Lp = np.repeat(L6[:, None, :], 6, axis=1)
    ar = np.arange(6)
    Lp[:, ar, ar] = Lp[:, ar, ar] * (1.0 + 1j * H_CS)
    wp = s0_beitraege_c(Lp.reshape(-1, 6), np.repeat(slots, 6)).reshape(n, 6)
    dw = np.imag(wp) / H_CS
    return s0v, np.bincount(E6.ravel(), dw.ravel(), N.E)


def s0_lagen(N, pos, v):
    ts, slots = np.nonzero(N.G == v)
    X = tu.tet_X(N.LV, pos, N.G[ts], N.O[ts])
    Ast, _, _ = td.hodge_teile(X)
    lt = np.stack([np.linalg.norm(X[:, j] - X[:, i], axis=1) for (i, j, _, _) in tg.PAARE], 1)
    return float(((MASKE[slots] * lt * Ast).sum(1) / 6.0).sum())


def lagen_probe(N, v, g, lbar):
    """Ecke v in fester Zufallsrichtung verschieben: d *0_v / dt aus den Lagen (zentrale Differenzen, Schrittweiten
    T_POS x l) gegen die Kettenregel mit g = d *0_v / d a. Rueckgabe (Kettenregel, [Differenzen])."""
    rng = np.random.default_rng([SAAT_PROBE, int(v)])
    d = rng.normal(size=3)
    d /= np.linalg.norm(d)
    es, es2, nv = N.mod['es'], N.mod['es2'], N.mod['n']
    dl = np.zeros(N.E)
    dl[es == v] -= nv[es == v] @ d
    dl[es2 == v] += nv[es2 == v] @ d
    pred = float(np.sum(g * dl / N.l0))
    fd = []
    for t in T_POS:
        h = t * lbar
        pp = N.pos.copy()
        pp[v] = pp[v] + h * d
        pm = N.pos.copy()
        pm[v] = pm[v] - h * d
        fd.append((s0_lagen(N, pp, v) - s0_lagen(N, pm, v)) / (2.0 * h))
    return pred, fd


def dlnD(N0, N1, V5, lbar):
    """d ln D_v / d a im Kantenraum von N1 (neue Zerlegung) fuer die Ecken V5; alte Kanten ueber die Schluessel."""
    idx01, ok = N1.idx_von_keys(N0.keys)
    assert ok.all()
    out, homog, s0s = [], 0.0, []
    pr_rel, pr_schritt = 0.0, 0.0
    for v in V5:
        s0a, ga = ds0_da(N0, v)
        s0n, gn = ds0_da(N1, v)
        g = gn / s0n
        g[idx01] -= ga / s0a
        out.append(g)
        homog = max(homog, abs(gn.sum() / s0n - 3.0), abs(ga.sum() / s0a - 3.0))
        s0s.append((s0a, s0n))
        for N, gg in ((N0, ga), (N1, gn)):
            pred, fd = lagen_probe(N, v, gg, lbar)
            pr_rel = max(pr_rel, abs(pred - fd[1]) / abs(fd[1]))
            pr_schritt = max(pr_schritt, abs(fd[0] - fd[1]) / abs(fd[1]))
    return np.array(out), homog, s0s, pr_rel, pr_schritt


# ------------------------------------------------------------------------------------------------ ein Zug
def zug(ctx, name, j, gesp):
    LV, pos2, k1, hp, hx = ctx['LV'], ctx['pos2'], ctx['k1'], ctx['hp'], ctx['hx']
    N0, sk0, geo = ctx['N0'], ctx['sk0'], ctx['geo']
    w = kf.zug_waehlen(N0, j, ctx['vmin'], geo)
    if w is None:
        return {'gueltig': False, 'grund': 'nicht ausfuehrbar'}
    typ, r, (Gn, On, b) = w
    res = {'flaeche': int(j), 'typ': int(typ), 'kante_neu_gleich': bool(b['kante_neu'] == gesp['kante_neu'])}
    if typ != 23:
        res.update({'gueltig': False, 'grund': 'kein 2-3'})
        return res
    res['gueltig'] = True
    N1 = kf.netz('A1', LV, pos2, Gn, On, k1, hp, hx)
    sk1 = kf.skalar_ops(N1)
    D = sk1['s0'] / sk0['s0']
    alt = b['alt']
    V5e = [alt[0][0], alt[0][1], alt[0][2], alt[0][3], alt[1][3]]
    V5 = [int(v) for v, _ in V5e]
    R5 = np.array([pos2[v] + np.asarray(o, float) @ LV for v, o in V5e])
    rc = R5.mean(0)
    rest = np.ones(N0.nV, bool)
    rest[V5] = False
    tal = b['tets_alt_idx']
    vbip = float(uk.tet_vol(LV, pos2, N0.G[tal], N0.O[tal]).sum())
    res.update({'V5': V5, 'D_minus_1': (D[V5] - 1.0).tolist(), 'D_max_abs': float(np.abs(D[V5] - 1.0).max()),
                'D_rest_max_abs': float(np.abs(D[rest] - 1.0).max()),
                'vol_erhalt_rel': float(abs(np.sum(sk1['s0']) - np.sum(sk0['s0'])) / vbip),
                'vol_erhalt_V5_rel': float(abs(np.sum(sk1['s0'][V5] - sk0['s0'][V5])) / vbip),
                's0_min_rel_nach': sk1['s0_min_rel'], 'stern0_n_neg_nach': sk1['stern0_n_neg']})
    # Ableitungen (zwei Schrittweiten)
    dl2, hom2, s0s2, pr_rel, pr_schritt = dlnD(N0, N1, V5, ctx['lbar'])
    s0lg = max(max(abs(a - sk0['s0'][v]) / sk0['s0'][v], abs(n_ - sk1['s0'][v]) / sk1['s0'][v])
               for v, (a, n_) in zip(V5, s0s2))
    res['ableitung'] = {'lagen_probe_rel': float(pr_rel), 'lagen_schritt_rel': float(pr_schritt),
                        'homogenitaet_max': float(hom2), 's0_laengen_gegen_lagen': float(s0lg),
                        'norm_dlnD': [float(np.linalg.norm(dl2[i])) for i in range(5)]}
    # Feldblock (zustandsunabhaengig)
    res['feldblock'] = {T: feldblock_fehler(T, D) for T in TRANSFERS}
    # Geometrie (Form A2)
    xy = {}
    gres = None
    if ctx['geo_ok']:
        n0 = ctx['n0']
        n1 = kf.netz(FORM, LV, pos2, Gn, On, k1, hp, hx)
        assert np.array_equal(n1.keys, N1.keys)
        gres = {'A_pd_nach': bool(n1.A_pd), 'Hg0': ctx['Hg0'], 'Kg0': ctx['Kg0'], 'Vg0': ctx['Vg0']}
        for L in LESARTEN:
            x1, y1, info = td.abbilden(n0, n1, ctx['x0'], ctx['y0'], b, L)
            xy[L] = (x1, y1)
            gres['dH_' + L] = float(n1.energie(x1, y1)[0] - ctx['Hg0'])
            gres['proj_rest_a_' + L] = info['proj_rest_a']
        res['geo'] = gres
    # Zustaende
    s0 = sk0['s0']
    k1n = float(np.linalg.norm(k1))
    th = pos2 @ k1 + (P0_Z1 - float(rc @ k1))
    phi1 = A_PHI * np.cos(th) + 0j
    pi1 = s0 * A_PHI * k1n * np.sin(th) + 0j
    sfr = (pos2 - rc) @ np.linalg.inv(LV)
    sfr -= np.round(sfr)
    dvec = sfr @ LV
    sig = SIGMA_L * ctx['lbar']
    fv = np.exp(-(dvec ** 2).sum(1) / (2.0 * sig ** 2))
    phi2 = A_PHI * fv * np.exp(1j * (pos2 @ k1))
    pi2 = 1j * OMEGA_Z2 * s0 * phi2
    res['Z1_phase_min_abs_cos'] = float(np.abs(np.cos(th[V5])).min())
    res['Z1_phase_min_abs_sin'] = float(np.abs(np.sin(th[V5])).min())
    res['Z2_f_zug_ecken'] = [float(x) for x in fv[V5]]
    res['Z2_f_min'] = float(fv.min())
    inV5 = np.zeros(N0.nV, bool)
    inV5[V5] = True
    kmask = inV5[sk0['es']] | inV5[sk0['es2']]
    for Z, phi, pi, m in (('Z1', phi1, pi1, 0.0), ('Z2', phi2, pi2, M_Z2)):
        zr = {}
        H0 = H_zerlegt(sk0, phi, pi, m)
        kin0, mas0, ge0 = teile(sk0, phi, pi, m)
        Q0 = np.imag(np.conj(phi) * pi)
        zr['H0'] = H0
        zr['anteil_lokal'] = float((kin0[inV5].sum() + mas0[inV5].sum() + ge0[kmask].sum()) / H0['H'])
        zr['Q0'] = float(Q0.sum())
        G_st1 = grad_E(sk1, phi) - grad_E(sk0, phi)
        c = np.real(np.conj(pi[V5]) * phi[V5])
        dp = 0.5 * c @ dl2
        zr['c_v'] = [float(x) for x in c]
        zr['dp_norm'] = float(np.linalg.norm(dp))
        for T in TRANSFERS:
            ph_, pi_ = transfer(T, D, phi, pi)
            H1 = H_zerlegt(sk1, ph_, pi_, m)
            dH = H1['H'] - H0['H']
            rec = {'dH': dH, 'rel': abs(dH) / H0['H'], 'dkin': H1['kin'] - H0['kin'], 'dmasse': H1['masse'] - H0['masse'],
                   'dgrad': H1['grad'] - H0['grad'], 'dgrad_stern1': G_st1, 'dgrad_umskal': H1['grad'] - grad_E(sk1, phi)}
            kin1, mas1, _ = teile(sk1, ph_, pi_, m)
            eins = np.ones_like(D)
            fk = {'R': D, 'P': 1.0 / D, 'K': eins}[T]
            rec['f_kin'] = rel_fehler(kin1, fk * kin0)
            if Z == 'Z2':
                fm = {'R': D, 'P': D, 'K': eins}[T]
                fq = {'R': D, 'P': eins, 'K': eins}[T]
                Q1 = np.imag(np.conj(ph_) * pi_)
                rec['f_masse'] = rel_fehler(mas1, fm * mas0)
                rec['f_ladung'] = rel_fehler(Q1, fq * Q0)
                rec['dQ_rel'] = float((Q1.sum() - Q0.sum()) / Q0.sum())
            if T == 'K':
                rec['f_k_stetig'] = max(rel_fehler(np.sqrt(sk1['s0']) * ph_, np.sqrt(s0) * phi),
                                        rel_fehler(pi_ / np.sqrt(sk1['s0']), pi / np.sqrt(s0)))
            zr[T] = rec
        if gres is not None:
            n1s = n1.S
            fak = ctx['Hg0'] / H0['H']                      # (A_s / A)^2: H_phi(A_s) = H_geo,0
            Hs = H_zerlegt(sk0, phi * np.sqrt(fak), pi * np.sqrt(fak), m)
            kt3 = {'fak_amp2': fak, 'A_s': A_PHI * float(np.sqrt(fak)), 'verh_Hphi_Hgeo': Hs['H'] / ctx['Hg0'],
                   'Hphi_s': Hs}
            for L in LESARTEN:
                x1, y1 = xy[L]
                Hb = n1.energie(x1, y1)[0]
                dy = n1s.T @ (fak * dp)
                E_rec = float(n1.energie(x1, y1 + dy)[0] - Hb)
                kt3['E_rec_' + L] = E_rec
                for T in TRANSFERS:
                    kt3['dH_ges_' + L + T] = float(gres['dH_' + L] + fak * zr[T]['dH'] + (E_rec if T == 'K' else 0.0))
            kt3['dH_phi_s'] = {T: float(fak * zr[T]['dH']) for T in TRANSFERS}
            zr['kt3'] = kt3
        res[Z] = zr
    return res


# ------------------------------------------------------------------------------------------------ ein Fall
def fall(f, mu_ziel, basis):
    LV, pos, G0, O0, k1, hp, hx = (basis[k] for k in ('LV', 'pos', 'G0', 'O0', 'k1', 'hp', 'hx'))
    fl, lbar, vbar, vz0 = basis['fl'], basis['lbar'], basis['vbar'], basis['vz0']
    X, Y = int(f['X']), int(f['Y'])
    ecken = f['verschiebung']['ecken']
    out = {'mu_ziel': -mu_ziel, 'ecken': [int(v) for v, _ in ecken]}
    pos2 = pos.copy()
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
            out.update({'gueltig': False, 'grund': 'newton'})
            return out
    for v, dl in vs:
        pos2[v] = pos2[v] + dl
    out['verschiebung'] = [[v, [float(q) for q in dl]] for v, dl in vs]
    out['norm_rel_max'] = float(max(np.linalg.norm(dl) for _, dl in vs) / lbar)
    mu = uk.raender(LV, pos2, G0, O0, fl)
    verl = set(np.nonzero(mu < -tu.TOL_MU)[0].tolist())
    vmin_a = td.VMIN_B * vbar
    tX = kf.ausfuehrbar(LV, pos2, G0, O0, X, vmin_a)
    tY = kf.ausfuehrbar(LV, pos2, G0, O0, Y, vmin_a)
    mo = mu.copy()
    mo[[X, Y]] = np.inf
    out.update({'mu_X': float(mu[X]), 'mu_Y': float(mu[Y]), 'mu_andere_min': float(mo.min()),
                'nur_X_Y_verletzt': verl == {X, Y},
                'vorzeichen_gleich': bool(np.array_equal(tu.vorzeichen_vol(LV, pos2, G0, O0), vz0)),
                'typ_X': tX, 'typ_Y': tY})
    if mu_ziel == 1e-3:
        out['wiedergabe_mu'] = float(max(abs(mu[X] - f['verschiebung']['mu_X']), abs(mu[Y] - f['verschiebung']['mu_Y'])))
    out['gueltig'] = bool(out['nur_X_Y_verletzt'] and out['vorzeichen_gleich'] and tX == 23 and tY == 23
                          and out['norm_rel_max'] <= kf.DELTA_MAX_REL)
    if not out['gueltig']:
        out['grund'] = 'Pruefung'
        return out
    N0 = kf.netz('A1', LV, pos2, G0, O0, k1, hp, hx)
    sk0 = kf.skalar_ops(N0)
    _, geo = tu.flaechen_geo(LV, pos2, G0, O0)
    ctx = {'LV': LV, 'pos2': pos2, 'k1': k1, 'hp': hp, 'hx': hx, 'N0': N0, 'sk0': sk0, 'geo': geo,
           'vmin': td.VMIN_B * N0.vbar, 'lbar': lbar}
    out['skalar_kontrolle'] = {'s0_durch_V': sk0['kontr_s0_durch_V'], 's0_min_rel': sk0['s0_min_rel'],
                               'stern0_n_neg': sk0['stern0_n_neg']}
    hm_td.VREF = None
    n0 = kf.netz(FORM, LV, pos2, G0, O0, k1, hp, hx)
    ctx['geo_ok'] = bool(n0.A_pd)
    out['geo_A_pd'] = ctx['geo_ok']
    out['vref'] = hm_td.VREF
    if ctx['geo_ok']:
        mode, xm, w2, Qm = td.tt_mode(n0, A_Q, k1)
        x0 = np.sin(PHASE) * xm
        y0 = sla.lu_solve(n0.lu, mode['omega'] * np.cos(PHASE) * xm)
        Hg0, Vg0, Kg0 = n0.energie(x0, y0)
        ctx.update({'n0': n0, 'x0': x0, 'y0': y0, 'Hg0': float(Hg0), 'Vg0': float(Vg0), 'Kg0': float(Kg0)})
        out['mode'] = {'omega': mode['omega'], 'anteil_TT_welle': mode['anteil_TT_welle']}
    out['zuege'] = {}
    for name, j, gesp in (('X', X, f['zuege_XY'][0]), ('Y', Y, f['zuege_YX'][0])):
        t1 = time.time()
        out['zuege'][name] = zug(ctx, name, j, gesp)
        out['zuege'][name]['t_s'] = time.time() - t1
    return out


def lauf(args):
    T0 = time.time()
    s = args.saat
    d = json.load(open(args.eingabe))['ergebnis']
    assert int(d['saat']) == s
    LV, pos, G0, O0, pr = tg.zufallsnetz(128, s)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    Nu = kf.netz('A1', LV, pos, G0, O0, k1, hp, hx)
    basis = {'LV': LV, 'pos': pos, 'G0': G0, 'O0': O0, 'k1': k1, 'hp': hp, 'hx': hx, 'fl': Nu.fl,
             'lbar': float(Nu.l0.mean()), 'vbar': float(Nu.vbar), 'vz0': tu.vorzeichen_vol(LV, pos, G0, O0)}
    res = {'saat': s, 'eingabe': os.path.basename(args.eingabe), 'eingabe_sha256': sha(args.eingabe),
           'l_mittel': basis['lbar'], 'l_mittel_gespeichert': d['netz']['l_mittel'],
           'L_kasten': float(abs(np.linalg.det(LV)) ** (1.0 / 3.0)), 'k1': k1.tolist(), 'faelle': []}
    faelle = d['faelle'][:1] if args.rauch else d['faelle']
    for i, f in enumerate(faelle):
        fr = {'nr': i, 'art': f['art'], 'X': int(f['X']), 'Y': int(f['Y']), 'mu': {}}
        for mz in MU_LISTE:
            t1 = time.time()
            r = fall(f, mz, basis)
            r['t_s'] = time.time() - t1
            fr['mu']['%g' % mz] = r
        res['faelle'].append(fr)
        print('fall', i, f['art'], 'fertig %.1f s' % (time.time() - T0), flush=True)
    res['wand_s'] = time.time() - T0
    return res


# ------------------------------------------------------------------------------------------------ Auswertung (PLAN 8)
def _med(v):
    return float(np.median(v)) if len(v) else None


def _mmm(v):
    v = [x for x in v if x is not None]
    if not v:
        return None
    return {'n': len(v), 'median': float(np.median(v)), 'min': float(np.min(v)), 'max': float(np.max(v))}


def zuege_laden(ordner):
    Z, ein = [], {}
    for p in sorted(glob.glob(os.path.join(ordner, 'kanon-s*.json'))):
        d = json.load(open(p))
        if 'ergebnis' not in d:
            continue
        ein[os.path.basename(p)] = sha(p)
        e = d['ergebnis']
        for f in e['faelle']:
            for mk, fm in f['mu'].items():
                if not fm.get('gueltig'):
                    Z.append({'saat': e['saat'], 'nr': f['nr'], 'art': f['art'], 'mu': mk, 'zug': None, 'gueltig': False,
                              'grund': fm.get('grund')})
                    continue
                for zn, z in fm['zuege'].items():
                    Z.append({'saat': e['saat'], 'nr': f['nr'], 'art': f['art'], 'mu': mk, 'zug': zn,
                              'gueltig': bool(z.get('gueltig')), 'z': z, 'fall_mu': fm})
    return Z, ein


def kt3_M(S, Z, L, T):
    v = [abs(r['z'][Z]['kt3']['dH_ges_' + L + T]) for r in S if 'kt3' in r['z'][Z] and r['z']['geo']['A_pd_nach']]
    return _med(v), len(v)


def auswertung(ordner):
    Zg, ein = zuege_laden(ordner)
    alle = [r for r in Zg if r['gueltig']]
    U = {}
    # KT0 (i)
    fehler = {'feldblock': [], 'kin': [], 'masse': [], 'ladung': [], 'k_stetig': []}
    for r in alle:
        z = r['z']
        for T in TRANSFERS:
            fehler['feldblock'].append(z['feldblock'][T])
            for Z in ZUSTAENDE:
                fehler['kin'].append(z[Z][T]['f_kin'])
            fehler['masse'].append(z['Z2'][T]['f_masse'])
            fehler['ladung'].append(z['Z2'][T]['f_ladung'])
        for Z in ZUSTAENDE:
            fehler['k_stetig'].append(z[Z]['K']['f_k_stetig'])
    fmax = {k: (max(v) if v else None) for k, v in fehler.items()}
    teil1 = bool(alle) and all(fmax[k] is not None and fmax[k] <= TOL_KT0 for k in ('feldblock', 'kin', 'masse', 'ladung'))
    # KT0 (ii): gepaarte Zuege
    by = {}
    for r in alle:
        by.setdefault((r['saat'], r['nr'], r['zug']), {})[r['mu']] = r
    paar = [v for v in by.values() if '0.001' in v and '0.0001' in v]
    if paar:
        d3 = max(v['0.001']['z']['D_max_abs'] for v in paar)
        d4 = max(v['0.0001']['z']['D_max_abs'] for v in paar)
        rD = d3 / d4 if d4 > 0 else None
        teil2 = rD is not None and 8.0 <= rD <= 12.0
        rje = [v['0.001']['z']['D_max_abs'] / v['0.0001']['z']['D_max_abs'] for v in paar
               if v['0.0001']['z']['D_max_abs'] > 0]
    else:
        d3 = d4 = rD = None
        teil2 = None
        rje = []
    if teil2 is None:
        u0 = 'nicht entscheidbar' if teil1 else 'verfehlt'
    else:
        u0 = 'eingetroffen' if (teil1 and teil2) else 'verfehlt'
    U['KT0'] = {'plan': u0, 'wortlaut': u0, 'teil_M_saetze': teil1, 'teil_D_skalierung': teil2, 'fehler_max': fmax,
                'D_max_mu3': d3, 'D_max_mu4': d4, 'r_D': rD, 'n_gepaart': len(paar), 'r_D_je_zug': _mmm(rje),
                'n_zuege': len(alle)}
    # KT1, KT2
    S3 = [r for r in alle if r['mu'] == '0.001']
    S3x = [r for r in S3 if r['zug'] == 'X']
    for nr, Z, fak in (('KT1', 'Z1', 0.5), ('KT2', 'Z2', 0.1)):
        u = {}
        for teil, S in (('plan', S3), ('wortlaut', S3x)):
            m = {T: _med([r['z'][Z][T]['rel'] for r in S]) for T in TRANSFERS}
            if not S:
                u[teil] = 'nicht entscheidbar'
            else:
                u[teil] = 'eingetroffen' if m['K'] <= fak * min(m['R'], m['P']) else 'verfehlt'
            u['median_' + teil] = m
            u['n_' + teil] = len(S)
            besser = min(m['R'], m['P']) if S else None
            u['verhaeltnis_besser_durch_K_' + teil] = (besser / m['K']) if (S and m['K'] > 0) else None
        u['schwelle'] = 'm_K <= %g x min(m_R, m_P)' % fak
        U[nr] = u
    # KT3
    u = {}
    for teil, S in (('plan', S3), ('wortlaut', S3x)):
        res = {}
        for Z in ZUSTAENDE:
            M = {}
            n = 0
            for L in LESARTEN:
                for T in TRANSFERS:
                    M[L + T], n = kt3_M(S, Z, L, T)
            if n == 0:
                res[Z] = {'erfuellt': None, 'n': 0}
                continue
            Ls = 'R' if M['RR'] <= M['PP'] else 'P'
            erf = M[Ls + 'K'] >= M[Ls + Ls] / 2.0
            res[Z] = {'M': M, 'L_stern': Ls, 'erfuellt': bool(erf), 'n': n,
                      'verhaeltnis_basis_durch_K': M[Ls + Ls] / M[Ls + 'K'] if M[Ls + 'K'] > 0 else None}
        u['werte_' + teil] = res
    pz = u['werte_plan'].get('Z2', {}).get('erfuellt')
    u['plan'] = 'nicht entscheidbar' if pz is None else ('eingetroffen' if pz else 'verfehlt')
    wz = [u['werte_wortlaut'].get(Z, {}).get('erfuellt') for Z in ZUSTAENDE]
    u['wortlaut'] = 'nicht entscheidbar' if any(x is None for x in wz) else ('eingetroffen' if all(wz) else 'verfehlt')
    U['KT3'] = u
    return {'eingaben_sha256': ein, 'urteile': U, 'zusammenfassung': zusammenfassung(Zg), 'n_eintraege': len(Zg)}


def zusammenfassung(Zg):
    """Beschreibend: Mediane, Minima, Maxima je mu und Zustand; Kontrollen; Anteile."""
    alle = [r for r in Zg if r['gueltig']]
    Zs = {'ungueltig': [{k: r[k] for k in ('saat', 'nr', 'art', 'mu', 'zug', 'grund') if k in r}
                        for r in Zg if not r['gueltig']]}
    for mk in ('0.001', '0.0001'):
        S = [r for r in alle if r['mu'] == mk]
        if not S:
            continue
        B = {'n': len(S), 'D_max_abs': _mmm([r['z']['D_max_abs'] for r in S])}
        B['kontrollen'] = {
            'D_rest_max_abs': _mmm([r['z']['D_rest_max_abs'] for r in S]),
            'vol_erhalt_rel': _mmm([r['z']['vol_erhalt_rel'] for r in S]),
            'vol_erhalt_V5_rel': _mmm([r['z']['vol_erhalt_V5_rel'] for r in S]),
            'lagen_probe_rel': _mmm([r['z']['ableitung']['lagen_probe_rel'] for r in S]),
            'lagen_schritt_rel': _mmm([r['z']['ableitung']['lagen_schritt_rel'] for r in S]),
            'homogenitaet_max': _mmm([r['z']['ableitung']['homogenitaet_max'] for r in S]),
            's0_laengen_gegen_lagen': _mmm([r['z']['ableitung']['s0_laengen_gegen_lagen'] for r in S]),
            'kante_neu_gleich': int(sum(1 for r in S if r['z']['kante_neu_gleich'])),
            'wiedergabe_mu': _mmm([r['fall_mu'].get('wiedergabe_mu') for r in S]),
            'norm_rel_max': _mmm([r['fall_mu']['norm_rel_max'] for r in S]),
            'mu_X': _mmm([r['fall_mu']['mu_X'] for r in S]), 'mu_Y': _mmm([r['fall_mu']['mu_Y'] for r in S]),
            'mu_andere_min': _mmm([r['fall_mu']['mu_andere_min'] for r in S]),
            'stern0_n_neg_nach_max': int(max(r['z']['stern0_n_neg_nach'] for r in S)),
            'geo_A_pd': int(sum(1 for r in S if r['fall_mu'].get('geo_A_pd'))),
            'A_pd_nach': int(sum(1 for r in S if r['z'].get('geo', {}).get('A_pd_nach'))),
            'Z1_phase_min_abs_cos': _mmm([r['z']['Z1_phase_min_abs_cos'] for r in S]),
            'Z1_phase_min_abs_sin': _mmm([r['z']['Z1_phase_min_abs_sin'] for r in S]),
            'Z2_f_zug_ecken_min': _mmm([min(r['z']['Z2_f_zug_ecken']) for r in S]),
            'Z2_f_min': _mmm([r['z']['Z2_f_min'] for r in S])}
        B['norm_dlnD'] = _mmm([x for r in S for x in r['z']['ableitung']['norm_dlnD']])
        geo = [r for r in S if 'geo' in r['z']]
        B['geo'] = {'n': len(geo)}
        for L in LESARTEN:
            B['geo']['dH_rel_' + L] = _mmm([abs(r['z']['geo']['dH_' + L]) / r['z']['geo']['Hg0'] for r in geo])
            B['geo']['dH_signed_rel_' + L] = _mmm([r['z']['geo']['dH_' + L] / r['z']['geo']['Hg0'] for r in geo])
            B['geo']['proj_rest_a_' + L] = _mmm([r['z']['geo']['proj_rest_a_' + L] for r in geo])
        B['geo']['Kg0_anteil'] = _mmm([r['z']['geo']['Kg0'] / r['z']['geo']['Hg0'] for r in geo])
        for Z in ZUSTAENDE:
            C = {}
            C['anteile_H0'] = {k: _mmm([r['z'][Z]['H0'][k] / r['z'][Z]['H0']['H'] for r in S])
                               for k in ('kin', 'masse', 'grad')}
            C['anteil_lokal'] = _mmm([r['z'][Z]['anteil_lokal'] for r in S])
            for T in TRANSFERS:
                C[T] = {'rel': _mmm([r['z'][Z][T]['rel'] for r in S]),
                        'dH_signed_rel': _mmm([r['z'][Z][T]['dH'] / r['z'][Z]['H0']['H'] for r in S])}
                for k in ('dkin', 'dmasse', 'dgrad', 'dgrad_stern1', 'dgrad_umskal'):
                    C[T][k + '_abs_rel'] = _mmm([abs(r['z'][Z][T][k]) / r['z'][Z]['H0']['H'] for r in S])
                if Z == 'Z2':
                    C[T]['dQ_rel_abs'] = _mmm([abs(r['z'][Z][T]['dQ_rel']) for r in S])
            for art in ('D', 'T', 'K'):
                Sa = [r for r in S if r['art'] == art]
                if Sa:
                    C['rel_je_art_' + art] = {T: _mmm([r['z'][Z][T]['rel'] for r in Sa]) for T in TRANSFERS}
            C['dp_norm'] = _mmm([r['z'][Z]['dp_norm'] for r in S])
            k3 = [r for r in S if 'kt3' in r['z'][Z]]
            if k3:
                K3 = {'n': len(k3), 'verh_Hphi_Hgeo': _mmm([r['z'][Z]['kt3']['verh_Hphi_Hgeo'] for r in k3]),
                      'A_s': _mmm([r['z'][Z]['kt3']['A_s'] for r in k3])}
                for L in LESARTEN:
                    K3['E_rec_abs_' + L] = _mmm([abs(r['z'][Z]['kt3']['E_rec_' + L]) for r in k3])
                    K3['E_rec_rel_' + L] = _mmm([abs(r['z'][Z]['kt3']['E_rec_' + L]) / r['z']['geo']['Hg0'] for r in k3])
                    K3['dH_geo_abs_' + L] = _mmm([abs(r['z']['geo']['dH_' + L]) for r in k3])
                    for T in TRANSFERS:
                        K3['dH_ges_abs_' + L + T] = _mmm([abs(r['z'][Z]['kt3']['dH_ges_' + L + T]) for r in k3])
                for T in TRANSFERS:
                    K3['dH_phi_s_abs_' + T] = _mmm([abs(r['z'][Z]['kt3']['dH_phi_s'][T]) for r in k3])
                C['kt3'] = K3
            B[Z] = C
        Zs[mk] = B
    # gepaarte Verhaeltnisse (beschreibend)
    by = {}
    for r in alle:
        by.setdefault((r['saat'], r['nr'], r['zug']), {})[r['mu']] = r
    paar = [v for v in by.values() if '0.001' in v and '0.0001' in v]
    P = {'n': len(paar)}
    P['D_max_abs'] = _mmm([v['0.001']['z']['D_max_abs'] / v['0.0001']['z']['D_max_abs'] for v in paar])
    for Z in ZUSTAENDE:
        for T in TRANSFERS:
            P[Z + '_rel_' + T] = _mmm([v['0.001']['z'][Z][T]['rel'] / v['0.0001']['z'][Z][T]['rel'] for v in paar
                                       if v['0.0001']['z'][Z][T]['rel'] > 0])
        P[Z + '_dp_norm'] = _mmm([v['0.001']['z'][Z]['dp_norm'] / v['0.0001']['z'][Z]['dp_norm'] for v in paar
                                  if v['0.0001']['z'][Z]['dp_norm'] > 0])
    P['norm_dlnD'] = _mmm([np.linalg.norm(v['0.001']['z']['ableitung']['norm_dlnD'])
                           / np.linalg.norm(v['0.0001']['z']['ableitung']['norm_dlnD']) for v in paar])
    Zs['verhaeltnis_mu3_durch_mu4'] = P
    return Zs


def g3(x):
    if x is None:
        return '-'
    if isinstance(x, str):
        return x
    if isinstance(x, bool):
        return str(x)
    if x == 0:
        return '0'
    return '%.3g' % x


def mm(d):
    if not d:
        return '-'
    return '%s [%s, %s] (n=%d)' % (g3(d['median']), g3(d['min']), g3(d['max']), d['n'])


def tabellen(aw_pfad, out_md):
    d = json.load(open(aw_pfad))['ergebnis']
    U, Zs = d['urteile'], d['zusammenfassung']
    L = ['# KANON-TRANSFER-1: Tabellen aus %s (synthetisch, keine Messdaten)' % os.path.basename(aw_pfad), '',
         '## Urteile (mechanisch, PLAN 8)', '', '| Nr | nach Plan | nach Kartenwortlaut |', '|---|---|---|']
    for k in ('KT0', 'KT1', 'KT2', 'KT3'):
        L.append('| %s | %s | %s |' % (k, U[k]['plan'], U[k]['wortlaut']))
    L += ['', '## Urteilsgroessen (JSON)', '', '```']
    for k in ('KT0', 'KT1', 'KT2', 'KT3'):
        L.append('%s: %s' % (k, json.dumps({a: b for a, b in U[k].items() if a not in ('plan', 'wortlaut')})))
    L += ['```', '']
    for mk in ('0.001', '0.0001'):
        if mk not in Zs:
            continue
        B = Zs[mk]
        L += ['## mu = -%s (n = %d Zuege)' % (mk, B['n']), '', 'Median [Min, Max] (n)', '',
              '- max |D - 1| je Zug: ' + mm(B['D_max_abs']),
              '- |d ln D_v / d a| je Zug-Ecke: ' + mm(B['norm_dlnD'])]
        for k, v in B['kontrollen'].items():
            L.append('- Kontrolle %s: %s' % (k, mm(v) if isinstance(v, dict) else g3(v)))
        for k, v in B['geo'].items():
            L.append('- Geometrie %s: %s' % (k, mm(v) if isinstance(v, dict) else g3(v)))
        for Z in ZUSTAENDE:
            C = B[Z]
            L += ['', '### %s' % Z, '', '| Groesse | R | P | K |', '|---|---|---|---|']
            for k in ('rel', 'dH_signed_rel', 'dkin_abs_rel', 'dmasse_abs_rel', 'dgrad_abs_rel', 'dgrad_stern1_abs_rel',
                      'dgrad_umskal_abs_rel', 'dQ_rel_abs'):
                if k in C['R']:
                    L.append('| %s | %s | %s | %s |' % (k, mm(C['R'][k]), mm(C['P'][k]), mm(C['K'][k])))
            for art in ('D', 'T', 'K'):
                if 'rel_je_art_' + art in C:
                    a = C['rel_je_art_' + art]
                    L.append('| rel, Art %s | %s | %s | %s |' % (art, mm(a['R']), mm(a['P']), mm(a['K'])))
            L += ['', '- Anteile H0: ' + '; '.join('%s %s' % (k, mm(v)) for k, v in C['anteile_H0'].items()),
                  '- Anteil Zug-Ecken und anliegende Kanten: ' + mm(C['anteil_lokal']),
                  '- |dp_a| (A = 1e-3): ' + mm(C['dp_norm'])]
            if 'kt3' in C:
                K3 = C['kt3']
                L += ['', '| KT3 (A_s) | Geometrie R | Geometrie P |', '|---|---|---|']
                for T in TRANSFERS:
                    L.append('| |dH_ges| Skalar %s | %s | %s |' % (T, mm(K3['dH_ges_abs_R' + T]), mm(K3['dH_ges_abs_P' + T])))
                L.append('| |dH_geo| | %s | %s |' % (mm(K3['dH_geo_abs_R']), mm(K3['dH_geo_abs_P'])))
                L.append('| |E_rec| | %s | %s |' % (mm(K3['E_rec_abs_R']), mm(K3['E_rec_abs_P'])))
                L.append('| |E_rec| / H_geo | %s | %s |' % (mm(K3['E_rec_rel_R']), mm(K3['E_rec_rel_P'])))
                L += ['', '- |dH_phi(A_s)|: ' + '; '.join('%s %s' % (T, mm(K3['dH_phi_s_abs_' + T])) for T in TRANSFERS),
                      '- H_phi / H_geo: ' + mm(K3['verh_Hphi_Hgeo']) + '; A_s: ' + mm(K3['A_s'])]
        L.append('')
    P = Zs.get('verhaeltnis_mu3_durch_mu4', {})
    L += ['## Verhaeltnisse mu = -1e-3 / mu = -1e-4 (gepaarte Zuege, n = %s)' % P.get('n'), '']
    for k, v in P.items():
        if k != 'n':
            L.append('- %s: %s' % (k, mm(v)))
    L += ['', '## Ungueltige Eintraege', '', json.dumps(Zs.get('ungueltig'))]
    with open(out_md + '.tmp', 'w') as fh:
        fh.write('\n'.join(L) + '\n')
    os.replace(out_md + '.tmp', out_md)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf', 'auswertung', 'tabellen'])
    ap.add_argument('--saat', type=int, default=1)
    ap.add_argument('--eingabe', default=None)
    ap.add_argument('--ordner', default='lauf')
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--out', required=True)
    ap.add_argument('--aw', default=None)
    a = ap.parse_args()
    t0 = time.time()
    me = os.path.abspath(__file__)
    if a.modus == 'tabellen':
        tabellen(a.aw, a.out)
        print('fertig tabellen', flush=True)
        return
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'skript_sha256': sha(me),
            'module_sha256': {m.__name__: sha(os.path.abspath(m.__file__)) for m in (tg, uk, tu, td, hm_td, kf)},
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    erg = lauf(a) if a.modus == 'lauf' else auswertung(a.ordner)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        tech = []
        for f in erg.get('faelle', []):
            for mk, fm in f['mu'].items():
                t = {'mu': mk, 'gueltig': fm.get('gueltig'), 'grund': fm.get('grund'),
                     'wiedergabe_mu': fm.get('wiedergabe_mu'), 'geo_A_pd': fm.get('geo_A_pd'), 't_s': fm.get('t_s')}
                for zn, z in fm.get('zuege', {}).items():
                    ab = z.get('ableitung', {})
                    t[zn] = {'gueltig': z.get('gueltig'), 'kante_neu_gleich': z.get('kante_neu_gleich'), 't_s': z.get('t_s'),
                             'lagen_probe_rel': ab.get('lagen_probe_rel'), 'lagen_schritt_rel': ab.get('lagen_schritt_rel'),
                             'homogenitaet_max': ab.get('homogenitaet_max'),
                             's0_laengen_gegen_lagen': ab.get('s0_laengen_gegen_lagen')}
                tech.append(t)
        res = {'info': info, 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'],
               'schluessel': tg.nur_schluessel(erg), 'technik': tech, 'wand_s': erg.get('wand_s')}
    schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
