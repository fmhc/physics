#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGIME-K-3 Folgeauftrag "h-Gang" (Leitung 05.10., ohne Karte, explorativ): dieselbe Takt-Transfermatrix wie rk3.py
(eingefroren, unveraendert importiert) fuer Zeltstangenhoehen h = tau (Untergitterhoehen hb mal h, wie
UEBERLEITUNG-V-1). Leichtere Fassung: Nachschaerfen (Newton auf der vollen 4D-Form) nur fuer die TT-Kandidaten;
alle anderen Eigenwerte aus T mit Fehlerschaetzung T gegen QZ. Keine s_voll-Pruefung.
Modi:
  lauf        --arm KW|B1-t1|V-A --satz raster|bz --h 1,0.5,... [--rauch]  -> JSON
  auswertung  --ein pfad ...  -> JSON (Zaehlungen je Netz und h)
"""
import argparse, json, sys, os, time, platform, hashlib
import numpy as np
import scipy.linalg as sla

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import rk   # noqa: E402
import rk2  # noqa: E402
import rk3  # noqa: E402

ZEIT_MAX = 540.0
THETA = 1e-6


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def baue(arm, h):
    if arm == 'KW':
        g = rk.baue('KW', h)
    elif arm == 'B1-t1':
        g = rk.baue('B1', h)
    elif arm == 'V-A':
        xb, tets, arten = rk2.netz_raum('V')
        NV = len(xb)
        rang = {b: j for j, b in enumerate(range(NV))}
        hb = [rang[b] / float(NV) for b in range(NV)]
        g = rk.Gitter('V-A', xb, hb, rk2.tp.AV.T, tets, rk2.ord_rang(rang), h)
    else:
        raise ValueError(arm)
    g.name = arm
    return g


def punkt_h(sch, lau, tot, ks, kb):
    """wie rk3.punkt bis zu den T-Eigenwerten; dann Newton nur fuer TT-Kandidaten (abs(Log z) <= 3 kb h)."""
    g = sch.g
    Es, NB, NV = sch.Es, sch.NB, g.NV
    H0 = sch.H(ks)
    hmax = float(np.abs(H0).max())
    H = 0.5 * (H0 + H0.conj().T)
    ib = np.arange(Es, Es + NB)
    rnd = np.r_[np.arange(Es), np.arange(Es + NB, 2 * Es + NB)]
    w, U = np.linalg.eigh(H[np.ix_(ib, ib)])
    wmax = float(np.abs(w).max())
    nul = np.abs(w) <= rk3.TOL_BB * wmax
    Up, wp, Nb = U[:, ~nul], w[~nul], U[:, nul]
    Hrb = H[np.ix_(rnd, ib)]
    X = (Up.conj().T @ Hrb.conj().T) / wp[:, None]
    E = H[np.ix_(rnd, rnd)] - (Hrb @ Up) @ X
    E = 0.5 * (E + E.conj().T)
    A, B, Bs, D = E[:Es, :Es], E[:Es, Es:], E[Es:, :Es], E[Es:, Es:]
    nn = int(nul.sum())
    tolk = rk3.TOL_KOPPL * hmax
    P, Pp = Hrb[:Es] @ Nb, Hrb[Es:] @ Nb
    if nn:
        R_vor, R_nach = rk3.kern(Pp, tolk), rk3.kern(P, tolk)
        spann = int(np.linalg.matrix_rank(np.c_[R_vor, R_nach], tol=1e-8)) if (R_vor.shape[1] + R_nach.shape[1]) else 0
        Cv, Cn = rk3.orth(P @ R_vor, tolk), rk3.orth(Pp @ R_nach, tolk)
    else:
        spann = 0
        Cv = Cn = np.zeros((Es, 0), complex)
    n_gem = nn - spann
    sinC = (float(np.linalg.norm(Cn - Cv @ (Cv.conj().T @ Cn), 2)) if Cv.shape[1] else 0.0) \
        if Cv.shape[1] == Cn.shape[1] else None
    Gl = sch.Gl(ks)
    M = np.c_[Gl, Cv]
    Um, sm, _ = np.linalg.svd(M, full_matrices=True)
    rM = int((sm > rk3.TOL_RANG * sm[0]).sum())
    W = Um[:, rM:]
    d = Es - rM
    gn = float(np.abs(Gl).max()); En = float(np.abs(E).max())
    eich = max(float(np.abs(W.conj().T @ B @ Gl).max() / (En * gn)),
               float(np.abs(W.conj().T @ B.conj().T @ Gl).max() / (En * gn)),
               float(np.abs(W.conj().T @ (A + D) @ Gl).max() / (En * gn)))
    AW, BW, BsW, DW = (W.conj().T @ Q @ W for Q in (A, B, Bs, D))
    Ub, sB, Vhb = np.linalg.svd(BW)
    stat = sB <= rk3.TOL_STAT * sB[0]
    ns = int(stat.sum())
    pfad = 'T'
    Ae, Be, Bse, De = AW, BW, BsW, DW
    Rb, Sb, MsM = np.eye(d, dtype=complex), np.zeros((d, 0), complex), None
    if ns:
        Kr, Kl = Vhb[stat].conj().T, Ub[:, stat]
        sinK = float(np.linalg.norm(Kl - Kr @ (Kr.conj().T @ Kl), 2))
        if sinK <= rk3.TOL_KERN:
            pfad = 'statisch'
            Sb, Rb = Kr, Vhb[~stat].conj().T
            Mx = AW + DW
            MsM = np.linalg.solve(Sb.conj().T @ Mx @ Sb, Sb.conj().T @ Mx @ Rb)
            Me = Rb.conj().T @ Mx @ Rb - (Rb.conj().T @ Mx @ Sb) @ MsM
            Me = 0.5 * (Me + Me.conj().T)
            Ae = De = 0.5 * Me
            Be, Bse = Rb.conj().T @ BW @ Rb, Rb.conj().T @ BsW @ Rb
        else:
            pfad = 'buendel'
    dd = Be.shape[0]
    I, Z0 = np.eye(dd), np.zeros((dd, dd))
    Ac = np.block([[Z0, I], [-Bse, -(Ae + De)]])
    Bc = np.block([[I, Z0], [Z0, Be]])
    s_sym = None
    if pfad in ('T', 'statisch'):
        Bi = np.linalg.inv(Be)
        T = np.block([[-Bi @ Ae, -Bi], [Bse - De @ Bi @ Ae, -De @ Bi]])
        z, VR = sla.eig(T, right=True)
        J = np.block([[Z0, I], [-I, Z0]])
        s_sym = float(np.abs(T.conj().T @ J @ T - J).max() / max(1.0, float(np.abs(T).max()) ** 2))
        vR = VR[:dd]
        ab = sla.eig(Ac, Bc, right=False, homogeneous_eigvals=True)
        zq = np.where(np.abs(ab[1]) > 1e-13 * np.abs(ab[0]), ab[0] / np.where(ab[1] == 0, 1, ab[1]), np.inf)
        frei = list(range(len(zq)))
        err = []
        for zj in z:
            i = min(frei, key=lambda q: abs(zq[q] - zj) if np.isfinite(zq[q]) else np.inf)
            err.append(float(abs(zq[i] - zj))); frei.remove(i)
        err = np.array(err)
    else:
        ab, VRc = sla.eig(Ac, Bc, right=True, homogeneous_eigvals=True)
        ok = np.abs(ab[1]) > 1e-13 * np.abs(ab[0])
        zall = np.where(ok, ab[0] / np.where(ab[1] == 0, 1, ab[1]), np.inf)
        phys = ok & (np.abs(zall) > rk3.Z_KLEIN) & (np.abs(zall) < rk3.Z_GROSS)
        z = zall[phys]; vR = VRc[:dd, phys]
        err = np.full(len(z), np.nan)
    vec = (Rb @ vR - Sb @ (MsM @ vR)) if pfad == 'statisch' else vR
    z = np.array(z, complex)
    zT = z.copy()
    tt = np.zeros(len(z))
    kand = [j for j in range(len(z)) if kb <= 0.25 and abs(np.log(z[j])) <= rk3.TT_FENSTER * kb * g.tau]
    n_it = []
    if kand:
        C = lau.koeff(ks)
        tb = sch.tt_basis(ks)
        phs = np.exp(1j * (sch.mid[:, :3] @ ks))
        gefunden = []
        for j in kand:
            zz, st, it = rk3.verfeinere(g, C, ks, tot, z[[j]], defl=gefunden)
            z[j] = zz[0]; err[j] = max(2.0 * float(st[0]), 1e-15 * abs(zz[0])); n_it.append(it)
            gefunden.append(zz[0])
            u = W @ vec[:, j]
            u = u / np.linalg.norm(u)
            tf = np.exp(np.log(z[j]) * sch.mid[:, 3] / g.tau)
            QT, _ = np.linalg.qr(tb * (phs * tf)[:, None])
            tt[j] = rk2.tt_klasse(u, Gl, QT)
    sperren = []
    if n_gem > 0 or sinC is None or sinC > rk3.TOL_C:
        sperren.append('bulk')
    if eich > rk3.TOL_EICH:
        sperren.append('eichung')
    if s_sym is not None and s_sym > rk3.TOL_SYM:
        sperren.append('symplektisch')
    if kand:
        verf = max(abs(z[j] - zT[j]) / abs(zT[j]) for j in kand)
        if verf > rk3.VERF_MAX:
            sperren.append('verfeinerung')
    else:
        verf = None
    kon = {'d': int(d), 'nn': nn, 'ns': ns, 'pfad': pfad, 'eich': eich, 'sinC': sinC, 's_sym': s_sym,
           'cond_B': float(sB[0] / sB[-1]) if sB[-1] > 0 else None, 'bb_min': float(np.abs(w).min() / wmax),
           'err_max': float(np.nanmax(err)) if len(err) and np.isfinite(err).any() else None, 'verf_tt': verf,
           'n_eig': int(len(z)), 'n_kand': len(kand), 'sperren': sperren}
    return {'kontrollen': kon, 'z_re': z.real.tolist(), 'z_im': z.imag.tolist(),
            'err': [float(x) if np.isfinite(x) else None for x in err], 'tt': tt.tolist()}


def lauf(arm, satz, hs, rauch):
    t0 = time.time()
    out = {'arm': arm, 'satz': satz, 'h': {}, 'abgebrochen': False}
    g1 = baue(arm, 1.0)          # gleiche physikalische k fuer alle h: Raster aus dem h = 1-Gitter (lmean dort)
    basis = rk3.raster_punkte(g1) if satz == 'raster' else rk3.bz_punkte(g1, arm)
    if rauch:
        basis = basis[::max(1, len(basis) // 4)][:4]
    out['lmean_h1'] = g1.lmean
    for h in hs:
        g = baue(arm, h)
        sch = rk3.Schicht(g)
        lau = rk2.Laurent(g)
        tot = rk2.tote_idx(g)
        pts = [dict(p) for p in basis]
        k1 = rk3.k1_kontrolle(sch, np.random.default_rng(rk3.SEED), 4)
        res = []
        for p in pts:
            if time.time() - t0 > ZEIT_MAX:
                out['abgebrochen'] = True
                break
            r = punkt_h(sch, lau, tot, np.array(p['ks'], float), p['kb'])
            p.update(r)
            res.append(p)
        out['h'][repr(h)] = {'tau': g.tau, 'lmean': g.lmean, 'K1': k1, 'punkte': res, 'zahl_soll': len(pts)}
        print('%s %s h=%g: %d/%d Punkte, %.1f s' % (arm, satz, h, len(res), len(pts), time.time() - t0), flush=True)
        if out['abgebrochen']:
            break
    return out


# ================================================================================================= Auswertung
def auswertung(pfade):
    daten = {}
    for p in pfade:
        d = json.load(open(p))
        for hk, v in d['h'].items():
            daten.setdefault((d['arm'], d['satz'], float(hk)), []).extend(v['punkte'])
    res = {}
    stabil_ab = {}
    for (arm, satz, h), pts in sorted(daten.items()):
        n_takt, n_rate, n_uns, g_max, rate_max = [], [], 0, 0.0, 0.0
        tt05, tt10, gesp = [], [], 0
        for p in pts:
            if p['kontrollen']['sperren']:
                gesp += 1
                continue
            E = [rk3.ev(a, b, c if c is not None else 0.0) for a, b, c in zip(p['z_re'], p['z_im'], p['err'])]
            st = [rk3.test(e, THETA) for e in E]
            n_takt.append(st.count(2))
            n_uns += int(1 in st)
            sr = [rk3.test({'delta': e['delta'] / h, 'eps': e['eps'] / h, 'schnitt': e['schnitt']}, THETA) for e in E]
            n_rate.append(sr.count(2))
            g_max = max([g_max] + [e['g'] for e in E])
            rate_max = max([rate_max] + [e['delta'] / h for e in E])
            if satz == 'raster':
                kand, ok = rk3.tt_zuordnung(p, E, h)
                if ok:
                    gt = max(E[j]['g'] for j in kand)
                    if p['betrag_label'] == 'kl0.05':
                        tt05.append(gt)
                    if p['betrag_label'] == 'kl0.1':
                        tt10.append(gt)
                key = (arm, p['betrag_label'], p['richtung'])
                stabil_ab.setdefault(key, {})[h] = st.count(2) == 0 and 1 not in st
        res.setdefault(arm, {}).setdefault(satz, {})[repr(h)] = {
            'punkte': len(pts), 'gesperrt': gesp, 'mit_unsicher': n_uns,
            'n_inst_median': float(np.median(n_takt)) if n_takt else None,
            'n_inst_max': int(max(n_takt)) if n_takt else None,
            'n_inst_min': int(min(n_takt)) if n_takt else None,
            'k_ganz_stabil': int(sum(1 for x in n_takt if x == 0)),
            'n_rate_median': float(np.median(n_rate)) if n_rate else None,
            'n_rate_max': int(max(n_rate)) if n_rate else None,
            'g_max': g_max, 'rate_max': rate_max,
            'tt_g_kl005_max': max(tt05) if tt05 else None, 'tt_g_kl005_median': float(np.median(tt05)) if tt05 else None,
            'tt_kl005_zahl': len(tt05),
            'tt_g_kl01_max': max(tt10) if tt10 else None, 'tt_g_kl01_median': float(np.median(tt10)) if tt10 else None,
            'tt_kl01_zahl': len(tt10)}
    # Schwelle je Rasterpunkt: groesstes h der Liste, ab dem fuer alle kleineren h alles stabil ist
    schwelle = {}
    for (arm, lab, rich), dh in stabil_ab.items():
        hs = sorted(dh)
        best = None
        for h in hs:
            if all(dh[x] for x in hs if x <= h):
                best = h
        schwelle.setdefault(arm, {}).setdefault(lab, {})[rich] = best
    zus = {}
    for arm, L in schwelle.items():
        for lab, R in L.items():
            v = list(R.values())
            zus.setdefault(arm, {})[lab] = {'richtungen': len(v), 'nie_stabil': sum(1 for x in v if x is None),
                                            'verteilung': {repr(x): v.count(x) for x in sorted(set(x for x in v if x is not None), reverse=True)}}
    return {'je_netz_satz_h': res, 'stabil_ab_h': zus, 'stabil_ab_h_koord005': {a: schwelle[a].get('koord0.05') for a in schwelle},
            'stabil_ab_h_kl01': {a: schwelle[a].get('kl0.1') for a in schwelle}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf', 'auswertung'])
    ap.add_argument('--arm', default='V-A')
    ap.add_argument('--satz', default='raster')
    ap.add_argument('--h', default='1')
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--ein', nargs='*', default=[])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'argv': sys.argv,
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'skript_sha256': sha(os.path.abspath(__file__)), 'rk3_sha256': sha(os.path.join(HIER, 'rk3.py'))}
    if a.modus == 'lauf':
        res = lauf(a.arm, a.satz, [float(x) for x in a.h.split(',')], a.rauch)
    else:
        res = auswertung(a.ein)
    res['info'] = info
    res['laufzeit_s'] = time.time() - t0
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
