#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""G2 steifer Integrator (N4 / CFL). Neue Datei, nn.py unveraendert.

Stufen:
  freeze  — M_eff/B am Hintergrund, implizite Mitte, CFL aus omega_max von N0
  period  — wie freeze, zusaetzlich NetzG je Periode am aktuellen x; bei Metrikfehler alten Operator behalten
  g1cfl   — G1-Zuege wie nn.lauf Arm b, aber nach jedem Operatorwechsel dt so dass omega_max*dt <= cfl
"""
from __future__ import print_function
import argparse, json, os, sys, time
import numpy as np
import scipy.linalg as sla

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import nn  # noqa: E402
import td  # noqa: E402
import tu  # noqa: E402


def mitte(Ar, Br, x, y, dt):
    m = Ar.shape[0]
    Msys = np.eye(m) + (dt * dt / 4.0) * (Ar @ Br)
    xm = np.linalg.solve(Msys, x + (dt / 2.0) * (Ar @ y))
    ym = y - (dt / 2.0) * (Br @ xm)
    return 2.0 * xm - x, 2.0 * ym - y


def dt_cfl(N, cfl):
    w2 = float((N.eig or {}).get('w2_max') or 0.0)
    wmax = np.sqrt(max(w2, 0.0))
    if wmax <= 0.0:
        return 1e-3, wmax
    return cfl / wmax, wmax


def bau_gedehnt(N0, LV, pos, G, O, k1, hp, hx, x, rolle):
    a = N0.S @ x if (G is N0.G or np.array_equal(G, N0.G)) else None
    if a is None:
        # gleiche Topologie angenommen: S von N0
        a = N0.S @ x
    f = 1.0 + a
    try:
        N2 = nn.NetzG(LV, pos, G, O, k1, hp, hx, f=f, rolle=rolle)
        return N2, None
    except (RuntimeError, AssertionError, np.linalg.LinAlgError) as exc:
        return None, repr(exc)[:300]


def json_dump(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump(obj, fh, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(tmp, path)


def lauf_n4(args):
    t0 = time.time()
    LV, pos, G0, O0, ninfo = td.netz_bauen(args.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    N0 = nn.NetzG(LV, pos, G0, O0, k1, hp, hx, rolle='start')
    if not N0.A_pd:
        raise RuntimeError('A_red nicht positiv definit am Start')
    mode, xm, w2, Qm = td.tt_mode(N0, args.A, k1)
    om = mode['omega']
    Tper = 2 * np.pi / om
    dt0, wmax0 = dt_cfl(N0, args.cfl)
    NT = max(1, int(np.ceil(Tper / dt0)))
    dt = Tper / NT
    nges = int(NT * args.perioden)
    x = np.zeros(N0.m)
    y = sla.lu_solve(N0.lu, om * xm)
    H0, V0, K0 = N0.energie(x, y)
    N = N0
    proben = []
    rebuilds = []
    dH_max = 0.0

    def probe(nstep):
        H, V, K = N.energie(x, y)
        dH = abs(H - H0) / abs(H0) if H0 != 0 else abs(H)
        rec = {'n': nstep, 't': nstep * dt, 'H': H, 'V': V, 'K': K, 'dH_rel': (H - H0) / H0,
               'A_pd': bool(N.A_pd), 'M_n_neg': N.meff.get('M_n_neg'),
               'n_wachsend': (N.eig or {}).get('n_wachsend'), 'w2_max': (N.eig or {}).get('w2_max'),
               'a_max': float(np.abs(N0.S @ x).max())}
        proben.append(rec)
        return dH

    dH_max = max(dH_max, probe(0))
    n = 0
    abbruch = None
    while n < nges:
        if time.time() - t0 > args.budget:
            abbruch = 'budget'
            break
        if args.stufe == 'period' and n > 0 and n % NT == 0:
            N2, err = bau_gedehnt(N0, LV, pos, G0, O0, k1, hp, hx, x, 'period_%d' % (n // NT))
            rec = {'n': n, 'ok': N2 is not None, 'fehler': err, 't_bau_s': None}
            if N2 is not None:
                rec.update({'A_pd': bool(N2.A_pd), 'M_n_neg': N2.meff.get('M_n_neg'),
                            'n_wachsend': (N2.eig or {}).get('n_wachsend'),
                            'w2_max': (N2.eig or {}).get('w2_max'), 't_bau_s': N2.t_bau,
                            'dAr_rel': float(np.linalg.norm(N2.Ar - N.Ar) / max(np.linalg.norm(N.Ar), 1e-30))})
                if N2.A_pd:
                    N = N2
                    dt_neu, wmax = dt_cfl(N, args.cfl)
                    # Periode in gleichmaessige Schritte teilen, CFL einhalten
                    NT_neu = max(NT, int(np.ceil(Tper / dt_neu)))
                    # dt bleibt Tper/NT des Startgitters, Unterschritte falls noetig
                    rec['wmax'] = wmax
                    rec['dt_cfl'] = dt_neu
                    rec['nsub'] = max(1, int(np.ceil(dt / dt_neu)))
                else:
                    rec['behalten'] = 'A_red indefinit'
            else:
                rec['behalten'] = 'Metrik oder M_eff'
            rebuilds.append(rec)
        nsub = 1
        if args.stufe == 'period' and N is not N0:
            dt_neu, _ = dt_cfl(N, args.cfl)
            nsub = max(1, int(np.ceil(dt / dt_neu)))
        dts = dt / nsub
        for _ in range(nsub):
            x, y = mitte(N.Ar, N.Br.toarray() if hasattr(N.Br, 'toarray') else N.Br, x, y, dts)
        n += 1
        if not np.all(np.isfinite(x)):
            abbruch = 'nicht endlich'
            break
        if n % NT == 0 or n == nges:
            dH_max = max(dH_max, probe(n))
            print('periode %d dH_rel=%.3e A_pd=%s M_n_neg=%s' % (
                n // NT, proben[-1]['dH_rel'], N.A_pd, N.meff.get('M_n_neg')), flush=True)

    out = {
        'stufe': args.stufe, 'netz': args.netz, 'A': args.A, 'cfl': args.cfl, 'perioden_soll': args.perioden,
        'ninfo': {k: v for k, v in ninfo.items() if k != 'pruefung'},
        'H0': H0, 'V0': V0, 'K0': K0, 'T': Tper, 'NT': NT, 'dt': dt, 'wmax0': wmax0,
        'N0': nn.kurz(N0), 'n': n, 'nges': nges, 'dH_max_abs': dH_max,
        'N4_grenze_1e-8': bool(dH_max < 1e-8), 'fertig': n >= nges and abbruch is None,
        'abbruch': abbruch, 'proben': proben, 'rebuilds': rebuilds,
        'N_ende': nn.kurz(N), 'wand_s': time.time() - t0,
        'rechenort': 'fmh@192.168.178.69 CPU kleintest, CUDA nicht benutzt',
    }
    json_dump(args.out, out)
    return out


def lauf_g1cfl(args):
    """G1 wie nn.lauf, aber nach Operatorwechsel Unterschritte nach CFL."""
    t0 = time.time()
    # nn.lauf erwartet ein args-Objekt mit denselben Feldern
    class A:
        pass
    a = A()
    a.netz = args.netz
    a.A = args.A
    a.arm = 'b'
    a.lesart = args.lesart
    a.h = args.h
    a.perioden = args.perioden
    a.proben = 10
    a.out = args.out + '.nn'
    a.budget = args.budget
    a.hmax = 1e3
    a.zugmax = 200
    a.split = True
    a.vergleich = True
    a.vorlauf = args.vorlauf
    a.bgd = 1
    # Wir fahren eine eigene Schleife, die kdk in CFL-Stuecken macht.
    LV, pos, G0, O0, ninfo = td.netz_bauen(args.netz)
    rez = 2 * np.pi * np.linalg.inv(LV).T
    k1 = rez[0]
    hp, hx = td.polarisation(k1)
    nn.B_GD['an'] = True
    N0 = nn.NetzG(LV, pos, G0, O0, k1, hp, hx, rolle='start')
    if not N0.A_pd:
        raise RuntimeError('A_red nicht positiv definit')
    mode, xm, w2, Qm = td.tt_mode(N0, args.A, k1)
    om = mode['omega']
    Tper = 2 * np.pi / om
    wmax0 = np.sqrt(N0.eig['w2_max'])
    NT = int(np.ceil(Tper * wmax0 / args.h))
    dt0 = Tper / NT
    nges = NT * args.perioden
    x = np.zeros(N0.m)
    y = sla.lu_solve(N0.lu, om * xm)
    H0 = N0.energie(x, y)[0]
    N = N0
    n = 0
    ereig = []
    proben = []
    gesperrt = set()
    abbruch = None
    fkeys0 = set(map(tuple, N0.fkeys.tolist()))

    def nsub_von(Ncur, tau):
        dt_c, wmax = dt_cfl(Ncur, args.cfl)
        return max(1, int(np.ceil(tau / dt_c))), wmax, dt_c

    def schritt(Ncur, x0, y0, tau):
        ns, wmax, dtc = nsub_von(Ncur, tau)
        dts = tau / ns
        x1, y1, Bx = x0, y0, None
        for _ in range(ns):
            x1, y1, Bx = td.kdk(Ncur, x1, y1, dts, None)
        return x1, y1, ns, wmax

    def probe(nstep):
        H, V, K = N.energie(x, y)
        mu = N.mu_alle(x)
        proben.append({'n': nstep, 't': nstep * dt0, 'H': H, 'dH_rel': (H - H0) / H0, 'V': V, 'K': K,
                       'n_mu_neg': int((mu < 0).sum()), 'mu_min': float(mu.min()),
                       'A_pd': bool(N.A_pd), 'M_n_neg': N.meff.get('M_n_neg'),
                       'n_wachsend': (N.eig or {}).get('n_wachsend'),
                       'n_zuege': len([e for e in ereig if e.get('ausgefuehrt')])})

    probe(0)
    while n < nges:
        if time.time() - t0 > args.budget:
            abbruch = {'grund': 'budget', 'n': n}
            break
        rem = dt0
        t_cur = n * dt0
        while rem > 0:
            x1, y1, ns, wmax = schritt(N, x, y, rem)
            ev = None
            mu1 = N.mu_alle(x1)
            kand = np.nonzero(mu1 < 0)[0]
            kand = [j for j in kand if tuple(N.fkeys[N.fl['t1'][j] * 4 + N.fl['i1'][j]].tolist()) not in gesperrt]
            if kand:
                v1 = N.Ar @ y
                v2 = N.Ar @ (N.Br @ x)
                best = None
                for j in kand:
                    lo, hi = 0.0, rem
                    if N.mu_eine(j, x) < 0:
                        continue
                    for _ in range(td.BISEKT):
                        mid = 0.5 * (lo + hi)
                        if N.mu_eine(j, x + mid * v1 - 0.5 * mid * mid * v2) < 0:
                            hi = mid
                        else:
                            lo = mid
                    if best is None or hi < best[1]:
                        best = (j, hi)
                if best is not None:
                    ev = best
            if ev is None:
                x, y = x1, y1
                rem = 0.0
                break
            j, tau = ev
            xe, ye, ns_e, wmax_e = schritt(N, x, y, tau)
            te = t_cur + tau
            rec_wmax = wmax_e
            H1, V1, K1 = N.energie(xe, ye)
            rec = {'t': te, 'n': n, 'tau_rel': tau / dt0, 'nsub': ns_e, 'wmax_vor': rec_wmax}
            abc, d, e = td.flaechen_ecken(N, j)
            L9 = N.l9_0[j] * (1.0 + N.S[N.f9[j]] @ xe)
            vv = td.vol_bipyr(L9)
            if np.all(vv > 0) or np.all(vv < 0):
                typ, r = 23, None
            else:
                typ, r = 32, tu_ungerade(vv)
            mu_hg = float(td.mu_bipyr(N.l9_0[j][None, :])[0])
            rec.update({'typ': typ, 'mu_hg': mu_hg})
            aus = None if (typ == 32 and r is None) else td.zug_ausfuehren(N, j, typ, r, td.VMIN_B * N0.vbar)
            if aus is None:
                rec['ausgefuehrt'] = False
                gesperrt.add(tuple(N.fkeys[N.fl['t1'][j] * 4 + N.fl['i1'][j]].tolist()))
                ereig.append(rec)
                x, y = xe, ye
                rem -= tau
                t_cur = te
                continue
            Gn, On, besch = aus
            a_alt = N.S @ xe
            f_alt = 1.0 + a_alt
            l_extra = {}
            if besch['kante_neu'] is not None:
                i9, ok9 = N.idx_von_keys(besch['k9'])
                L9g = N.l0[i9] * (1.0 + a_alt[i9])
                l_extra[besch['kante_neu']] = float(td.l_de_flach(L9g[None, :])[0])
            if args.vorlauf > 0:
                v1 = N.Ar @ ye
                v2 = N.Ar @ (N.Br @ xe)
                xv = xe + args.vorlauf * dt0 * v1 - 0.5 * (args.vorlauf * dt0) ** 2 * v2
                a_alt = N.S @ xv
                f_alt = 1.0 + a_alt
                rec['vorlauf'] = args.vorlauf

            def f_neu_fn(N2, N=N, f_alt=f_alt, besch=besch, l_extra=l_extra):
                idx, ok = N2.idx_von_keys(N.keys)
                fn = np.ones(N2.E)
                fn[idx[ok]] = f_alt[ok]
                if besch['kante_neu'] is not None:
                    inew, okn = N2.idx_von_keys(np.array([besch['kante_neu']]))
                    fn[inew[0]] = l_extra[besch['kante_neu']] / N2.l0[inew[0]]
                return fn

            try:
                N2 = nn.NetzG(LV, pos, Gn, On, k1, hp, hx, f_fn=f_neu_fn, rolle='neu_gd')
            except (RuntimeError, AssertionError, np.linalg.LinAlgError) as exc:
                rec['ausgefuehrt'] = False
                rec['fehler'] = repr(exc)
                ereig.append(rec)
                abbruch = {'t': te, 'n': n, 'grund': 'Operator: ' + repr(exc)[:300]}
                break
            x2, y2, minfo = td.abbilden(N, N2, xe, ye, besch, args.lesart)
            H2 = N2.energie(x2, y2)[0]
            rec.update({'ausgefuehrt': True, 'dH_rel': (H2 - H1) / H0, 'nach': nn.kurz(N2),
                        'abbildung': {k: v for k, v in minfo.items() if k != 'jrow'}})
            ereig.append(rec)
            N, x, y = N2, x2, y2
            rem -= tau
            t_cur = te
            mu_n = N.mu_alle(x)
            for jj in np.nonzero(mu_n < 0)[0]:
                gesperrt.add(tuple(N.fkeys[N.fl['t1'][jj] * 4 + N.fl['i1'][jj]].tolist()))
        if abbruch is not None:
            break
        n += 1
        if gesperrt:
            mu_n = N.mu_alle(x)
            fk = N.fkeys[N.fl['t1'] * 4 + N.fl['i1']]
            frei = set(tuple(r_) for r_ in fk[mu_n > 0].tolist())
            gesperrt -= frei
        if n % NT == 0 or n == nges:
            probe(n)
            print('periode %d dH_rel=%.3e zuege=%d M_n_neg=%s A_pd=%s' % (
                n // NT, proben[-1]['dH_rel'], proben[-1]['n_zuege'],
                N.meff.get('M_n_neg'), N.A_pd), flush=True)
        Hn = N.energie(x, y)[0]
        if not np.all(np.isfinite(x)) or abs(Hn - H0) > 1e3 * abs(H0):
            abbruch = {'n': n, 'grund': 'Kaskade oder nicht endlich'}
            probe(n)
            break

    out = {
        'stufe': 'g1cfl', 'netz': args.netz, 'lesart': args.lesart, 'A': args.A, 'cfl': args.cfl,
        'vorlauf': args.vorlauf, 'H0': H0, 'T': Tper, 'NT': NT, 'dt0': dt0, 'wmax0': wmax0,
        'n': n, 'nges': int(nges), 'fertig': n >= nges and abbruch is None, 'abbruch': abbruch,
        'N0': nn.kurz(N0), 'N_ende': nn.kurz(N), 'proben': proben, 'ereignisse': ereig,
        'n_zuege': len([e for e in ereig if e.get('ausgefuehrt')]),
        'wand_s': time.time() - t0,
        'rechenort': 'fmh@192.168.178.69 CPU kleintest, CUDA nicht benutzt',
        'ninfo': {k: v for k, v in ninfo.items() if k != 'pruefung'},
    }
    json_dump(args.out, out)
    return out


def tu_ungerade(vv):
    import tu
    return tu.ungerade(vv)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('stufe', choices=['freeze', 'period', 'g1cfl'])
    ap.add_argument('--netz', default='glas-N128-s4')
    ap.add_argument('--out', required=True)
    ap.add_argument('--A', type=float, default=1e-3)
    ap.add_argument('--perioden', type=int, default=10)
    ap.add_argument('--cfl', type=float, default=0.25)
    ap.add_argument('--budget', type=float, default=540.0)
    ap.add_argument('--h', type=float, default=0.5)
    ap.add_argument('--lesart', default='P', choices=['P', 'R'])
    ap.add_argument('--vorlauf', type=float, default=0.0)
    args = ap.parse_args()
    if args.stufe == 'g1cfl':
        lauf_g1cfl(args)
    else:
        lauf_n4(args)


if __name__ == '__main__':
    main()
