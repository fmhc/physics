#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UMKLAPP-FOLGE-1 (fmhc-physics, Runde 50, schlanke Karte), Code-Agent fuer die Leitung claude-primary.

Frage: kumulativer Energiefehler einer Folge von Umklappzuegen in einer echten Zeitentwicklung (TAKT-DYNAMIK-1-Aufbau,
td.lauf unveraendert), mit der Traegheit M_eff aus der 4D-Zeltwirkung (wie UMKLAPP-4D-1: ganze Box, k = 0, h = 2^-10,
Hubfolge nach Eckindex, Schema ls) statt Form A1/A2.

Umsetzung: td.Netz wird (wie in hm_td) durch NetzM ersetzt. NetzM baut td.Netz (S, B_red, Flaechen, TT-Leser) und setzt
A = M_eff^-1, A_red = S^T M_eff^-1 S (wie UMKLAPP-4D-1 / uv.reduktion). M_eff wird je neuer Zerlegung neu aus dem
4D-Zeltgitter berechnet, hier mit duennbesetzten Matrizen (meff_schnell): Bei k = 0 traegt nur J^(0) den Gitterrest L,
also D_p = -(1/h) J_L^T H_p J_L, P_p[q, L] = -(1/h) sum_{a+b=p} (-1)^a J_q,a^T H_b J_L, P_p[L, q] = -(1/h) sum_{b+c=p}
J_L^T H_b J_q,c; Schur ueber L wie uw.bloecke2. Gegenprobe gegen umklapp4d.bloecke_reell im Modus rauch.
Arme (td.lauf): a = feste Zerlegung (Referenz), b = Delaunay-gesteuerte Zuege, Lesart R oder P.
Importiert unveraendert: td, tg, uk, tu (TAKT-DYNAMIK-1-Stand), uv, rk, rk2 (UEBERLEITUNG-V-2), umklapp4d (UMKLAPP-4D-1).
"""
import argparse, json, os, sys, time, types, platform, resource
import numpy as np
import scipy
import scipy.sparse as sp
import scipy.linalg as sla

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import tg  # noqa: E402
import uk  # noqa: E402
import tu  # noqa: E402
import td  # noqa: E402
import uv  # noqa: E402
import rk  # noqa: E402
import rk2  # noqa: E402
import umklapp4d as u4  # noqa: E402

H_ZELT = 2.0 ** -10
TOL = 1e-10
KONTR = []
_TDNetz = td.Netz


def _summe(terme, form):
    X = None
    for f, Y in terme:
        if f == 0.0:
            continue
        X = f * Y if X is None else X + f * Y
    if X is None:
        return sp.csr_matrix(form) if isinstance(form, tuple) else np.zeros(form)
    return X


def meff_schnell(LV, pos, G, O, mod, h=H_ZELT):
    """M_eff (= S_2 auf q) und V_eff (= S_0 auf q) in tg-Kanten, duennbesetzt bei k = 0."""
    t0 = time.time()
    u4._BAU['glas'] = (LV, pos, G, O)
    V = uv.Vier('glas', h)
    t1 = time.time()
    NE, nq, NV = V.NE, V.nq, V.NV
    lau = V.lau
    ii, jj = lau.idx // NE, lau.idx % NE
    Ld = sp.diags(V.g.l)
    Ca = {}
    for m in lau.ms:
        s = lau.sel[m]
        C = sp.coo_matrix((lau.w[s], (ii[s], jj[s])), shape=(NE, NE)).tocsr()
        Ca[m] = (Ld @ C @ Ld).tocsr()
    fak = [1.0, 1.0, 2.0]
    Hr = [_summe([((m * h) ** p / fak[p], Ca[m]) for m in Ca], (NE, NE)).tocsr() for p in range(3)]
    V.L_basis = types.MethodType(u4.L_basis_reell, V)
    Jm, nL, rB = V.J_mats(np.zeros(3), 'ls')
    nK = nq + 4 * NV
    for m in Jm:
        assert np.abs(Jm[m].imag).max() == 0.0
        if m != 0:
            assert np.abs(Jm[m][:, nK:]).max() == 0.0
    JQm = {m: sp.csr_matrix(Jm[m][:, :nq].real) for m in Jm}
    JL = np.ascontiguousarray(Jm[0][:, nK:].real)
    del Jm
    JQ = [_summe([((m * h) ** p / fak[p], JQm[m]) for m in JQm], (NE, nq)).tocsr() for p in range(3)]
    HJL = [Hr[p] @ JL for p in range(3)]
    D = [-(JL.T @ HJL[p]) / h for p in range(3)]
    Bq, Bt, Aq = [], [], {}
    for p in range(3):
        X = np.zeros((nq, nL))
        for a in range(p + 1):
            X += ((-1.0) ** a) * (JQ[a].T @ HJL[p - a])
        Bq.append(-X / h)
        Y = np.zeros((nq, nL))
        for b in range(p + 1):
            Y += (Hr[b] @ JQ[p - b]).T @ JL
        Bt.append(-Y.T / h)
    for p in (0, 2):
        X = None
        for a in range(p + 1):
            for b in range(p + 1 - a):
                c = p - a - b
                T = ((-1.0) ** a) * (JQ[a].T @ (Hr[b] @ JQ[c]))
                X = T if X is None else X + T
        Aq[p] = -X.toarray() / h
    D0s = 0.5 * (D[0] + D[0].T)
    evD = np.linalg.eigvalsh(D0s)
    amax = float(np.abs(evD).max())
    dg = {'NE': int(NE), 'nq': int(nq), 'n_L': int(nL), 'rang_B_s': int(rB), 'n_tot': len(V.tot),
          'D0_n_neg': int((evD < 0).sum()), 'D0_min_rel': float(np.abs(evD).min() / amax),
          'D_asym': [float(np.abs(D[p] - (1 if p != 1 else -1) * D[p].T).max() / np.abs(D[p]).max()) for p in range(3)]}
    if dg['D0_min_rel'] < 1e-10 or rB != 3 * NV:
        dg['grund'] = 'D0_singulaer' if dg['D0_min_rel'] < 1e-10 else 'schema_rang'
        return None, dg
    E0 = np.linalg.inv(D[0])
    E1 = -E0 @ (D[1] @ E0)
    E2 = -E0 @ (D[1] @ E1 + D[2] @ E0)
    Y2 = E0 @ Bt[0]
    Y1 = E0 @ Bt[1] + E1 @ Bt[0]
    Y0 = E0 @ Bt[2] + E1 @ Bt[1] + E2 @ Bt[0]
    S2 = Aq[2] - (Bq[0] @ Y0 + Bq[1] @ Y1 + Bq[2] @ Y2)
    S0 = Aq[0] - Bq[0] @ Y2
    zu = uv.Zuordnung(V, mod, LV)
    U = zu.U(np.zeros(3))
    assert np.abs(U.imag).max() == 0.0
    U = U.real
    Mrk = -S2
    dg['S2_asym'] = float(np.abs(Mrk - Mrk.T).max() / np.abs(Mrk).max())
    M = U.T @ Mrk @ U
    M = 0.5 * (M + M.T)
    Ve = U.T @ S0 @ U
    Ve = 0.5 * (Ve + Ve.T)
    ev = np.linalg.eigvalsh(M)
    s = float(np.abs(ev).max())
    dg.update({'M_n_neg': int((ev < -TOL * s).sum()), 'M_n_null': int((np.abs(ev) <= TOL * s).sum()),
               'M_absmin_rel': float(np.abs(ev).min() / s), 't_vier_s': t1 - t0, 't_gesamt_s': time.time() - t0})
    return {'M': M, 'V': Ve}, dg


class NetzM(_TDNetz):
    """td.Netz mit A = M_eff^-1 aus der 4D-Zeltwirkung (A_red = S^T M_eff^-1 S)."""

    def __init__(self, LV, pos, G, O, k1, hp, hx, eigen=True):
        t0 = time.time()
        super().__init__(LV, pos, G, O, k1, hp, hx, eigen=False)
        res, dg = meff_schnell(LV, pos, G, O, self.mod)
        if res is None:
            raise RuntimeError('M_eff nicht bestimmbar: %s' % json.dumps(dg))
        Bd = self.B.toarray()
        dg['r_V_gegen_B'] = float(np.linalg.norm(res['V'] - Bd) / np.linalg.norm(Bd))
        A = np.linalg.inv(res['M'])
        A = 0.5 * (A + A.T)
        self.A = A
        Ar = self.S.T @ A @ self.S
        self.Ar = 0.5 * (Ar + Ar.T)
        self.lu = sla.lu_factor(self.Ar)
        eA = np.linalg.eigvalsh(self.Ar)
        self.n_A_neg = int((eA < -1e-12 * np.abs(eA).max()).sum())
        self.A_min_rel = float(eA.min() / np.abs(eA).max())
        try:
            self.L = np.linalg.cholesky(self.Ar)
            self.A_pd = True
        except np.linalg.LinAlgError:
            self.L = None
            self.A_pd = False
        self.meff = dg
        self.eig = None
        if eigen:
            self.spektrum()
        self.t_bau = time.time() - t0
        dg.update({'T': int(len(G)), 'E': int(self.E), 'A_pd': bool(self.A_pd), 'n_A_neg': self.n_A_neg,
                   'w2_max': (self.eig or {}).get('w2_max'), 'n_wachsend': (self.eig or {}).get('n_wachsend'),
                   't_bau_s': self.t_bau})
        KONTR.append(dg)


def rauch(a):
    """Gegenprobe meff_schnell gegen umklapp4d.bloecke_reell, Bauzeit NetzM, omega_max und NT."""
    out = {}
    LV, pos, G0, O0, ninfo = td.netz_bauen(a.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    NA1 = _TDNetz(LV, pos, G0, O0, k1, hp, hx, eigen=False)
    t = time.time()
    rs, ds = meff_schnell(LV, pos, G0, O0, NA1.mod)
    out['t_schnell_s'] = time.time() - t
    t = time.time()
    rr, dr = u4.meff_aus_4d(LV, pos, G0, O0, NA1.mod, H_ZELT, False)
    out['t_reell_s'] = time.time() - t
    out['diag_schnell'], out['diag_reell'] = ds, dr
    out['M_rel'] = float(np.abs(rs['M'] - rr['M']).max() / np.abs(rr['M']).max())
    out['V_rel'] = float(np.abs(rs['V'] - rr['V']).max() / np.abs(rr['V']).max())
    t = time.time()
    N = NetzM(LV, pos, G0, O0, k1, hp, hx)
    N.hp = hp
    out['t_netzM_s'] = time.time() - t
    out['eig'] = N.eig
    out['A_pd'] = N.A_pd
    mode, xm, w2, Qm = td.tt_mode(N, a.A, k1)
    Tper = 2 * np.pi / mode['omega']
    wmax = float(np.sqrt(N.eig['w2_max']))
    out.update({'omega': mode['omega'], 'anteil_TT': mode['anteil_TT_welle'], 'omega_max': wmax,
                'NT_h05': int(np.ceil(Tper * wmax / 0.5)), 'NT_h025': int(np.ceil(Tper * wmax / 0.25))})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf', 'rauch'])
    ap.add_argument('--netz', default='glas-N128-s1')
    ap.add_argument('--A', type=float, default=1e-3)
    ap.add_argument('--arm', default='a', choices=['a', 'b'])
    ap.add_argument('--lesart', default='R', choices=['R', 'P'])
    ap.add_argument('--h', type=float, default=0.5, help='omega_max * dt')
    ap.add_argument('--perioden', type=int, default=10)
    ap.add_argument('--proben', type=int, default=200)
    ap.add_argument('--budget', type=float, default=450.0)
    ap.add_argument('--ereignisse', default=None)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    me = os.path.abspath(__file__)
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'skript_sha256': td.sha(me),
            'module_sha256': {m.__name__: td.sha(os.path.abspath(m.__file__)) for m in (tg, uk, tu, td, uv, rk, rk2, u4)},
            'h_zelt': H_ZELT, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    td.Netz = NetzM
    if a.modus == 'rauch':
        erg = rauch(a)
    else:
        erg = td.lauf(a)
        erg['meff_netze'] = KONTR
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], 'fertig=%s' % erg.get('fertig'), flush=True)


if __name__ == '__main__':
    main()
