#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 Auswertung (CPU, numpy; nur ueber kleintest.sh auf der .69).

  ana.py tab  --ein LAUF1 LAUF2 ... --out AUS.json   Tabellen je Stufe und Replika (Jackknife ueber Bins),
                                                     Maximum der Polyakov-Suszeptibilitaet je Gruppe (gleiches Gitter)
  ana.py korr --ein LAUF1 ... --out AUS.json         Polyakov-Korrelatoren (Multihit): Scheiben-Korrelatoren je
                                                     Ebenenfamilie, effektive Energien E, sigma (Nambu-Goto), C(r)
Kennzahlen:
  |L| = Mittel des Betrags des raeumlichen Mittels L = <(1/2) Tr P>; chi_L = nS (<L^2> - <|L|>^2);
  Binder U4 = 1 - <L^4> / (3 <L^2>^2).
  Scheibe (Ebenenindex j = m . n mod L, Abstand d_m = 1/|Summe m_i b_i|): S(Delta) ~ cosh(E d_m (Delta - L/2)).
  Nambu-Goto (geschlossener Faden der Laenge L_t = Nt tau, D = 4): E^2 = sigma^2 L_t^2 - (2 pi/3) sigma.
"""
import argparse
import hashlib
import itertools
import json
import os
import platform
import sys
import time

import numpy as np

T0 = time.time()


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def kopf():
    return {'python': platform.python_version(), 'numpy': np.__version__, 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(T0)), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__))}


def binne(x, nbin):
    n = (len(x) // nbin) * nbin
    return x[:n].reshape((nbin, -1) + x.shape[1:]).mean(1)


def jk(bins, fun):
    n = len(bins)
    full = fun(bins.mean(0))
    js = np.array([fun(np.delete(bins, i, 0).mean(0)) for i in range(n)])
    err = np.sqrt((n - 1) / n * ((js - js.mean(0)) ** 2).sum(0))
    return full, err, js


def lade(p):
    with open(p + '.json') as f:
        res = json.load(f)
    z = np.load(p + '.npz')
    return res, z


def f(x):
    return None if x is None or not np.isfinite(x) else float(x)


# ================================================================================================ Tabellen
def tab(a):
    out = {'kopf': kopf(), 'laeufe': [], 'gruppen': []}
    gruppen = {}
    for p in a.ein:
        res, z = lade(p)
        nS = res['nS']
        d = {'datei': os.path.basename(p), 'gitter': res['gitter'], 'L': res['L'], 'Nt': res['Nt'],
             'tau': res['tau'], 'R': res['R'], 'S': res['S'], 'nor': res['nor'], 'mabst': res['mabst'],
             'ntherm': res['ntherm'], 'abbruch': res['abbruch'], 'zeit_s': res.get('zeit_gesamt_s'),
             'cuda_graph': res.get('cuda_graph'), 'waermebad_ohne_annahme': res.get('waermebad_ohne_annahme'),
             'zeilen': []}
        for s, st in enumerate(res['stufen']):
            if ('pw_%d' % s) not in z.files:
                continue
            PW, PS, PT, LL = z['pw_%d' % s], z['ps_%d' % s], z['pt_%d' % s], z['L_%d' % s]
            LM = z['Lmh_%d' % s] if ('Lmh_%d' % s) in z.files else None
            nm = len(PW)
            nbin = min(a.nbin, nm // 4) if nm >= 8 else 0
            for r in range(res['R']):
                e = {'stufe': s, 'replika': r, 'beta': st['betas'][r], 'start': res['starts'][r], 'nmess': nm}
                if nbin < 4:
                    e['zu_wenig'] = True
                    d['zeilen'].append(e)
                    continue
                Lr = LL[:, r]
                cols = [np.abs(Lr), Lr ** 2, Lr ** 4, PW[:, r], PS[:, r], PT[:, r]]
                if LM is not None:
                    cols += [np.abs(LM[:, r]), LM[:, r]]
                X = np.stack(cols, 1)
                B = binne(X, nbin)
                mean, err, _ = jk(B, lambda v: v)
                chi, chie, _ = jk(B, lambda v: nS * (v[1] - v[0] ** 2))
                bi, bie, _ = jk(B, lambda v: 1.0 - v[2] / (3.0 * v[1] ** 2))
                # grobe Autokorrelationszeit von |L| und pw aus dem Binning
                tauL = 0.5 * (len(Lr) // nbin) * B[:, 0].var(ddof=1) / max(np.abs(Lr).var(), 1e-300)
                tauP = 0.5 * (len(Lr) // nbin) * B[:, 3].var(ddof=1) / max(PW[:, r].var(), 1e-300)
                e.update({'pw': f(mean[3]), 'pw_err': f(err[3]), 'ps': f(mean[4]), 'ps_err': f(err[4]),
                          'pt': f(mean[5]), 'pt_err': f(err[5]), 'absL': f(mean[0]), 'absL_err': f(err[0]),
                          'chiL': f(chi), 'chiL_err': f(chie), 'binder': f(bi), 'binder_err': f(bie),
                          'tau_int_absL': f(tauL), 'tau_int_pw': f(tauP), 'nbin': nbin,
                          'chiP': f(res['nF'] * PW[:, r].var())})
                if LM is not None:
                    e.update({'absLmh': f(mean[6]), 'absLmh_err': f(err[6]), 'Lmh': f(mean[7]),
                              'Lmh_err': f(err[7])})
                # Drift: erste gegen zweite Haelfte der Plakette
                h = nm // 2
                e['pw_haelften'] = [f(PW[:h, r].mean()), f(PW[h:, r].mean())]
                e['absL_haelften'] = [f(np.abs(Lr[:h]).mean()), f(np.abs(Lr[h:]).mean())]
                d['zeilen'].append(e)
                if res['S'] == 1:
                    key = '%s L%d Nt%d %s' % (res['gitter'], res['L'], res['Nt'], a.gruppe or '')
                    gruppen.setdefault(key, []).append((e['beta'], e['chiL'], e['chiL_err'], e['absL'],
                                                        e['binder'], e['start'], d['datei']))
        out['laeufe'].append(d)
        for e in d['zeilen']:
            if e.get('zu_wenig'):
                print(d['datei'], 'Stufe', e['stufe'], 'Replika', e['replika'], 'zu wenig Messungen', flush=True)
                continue
            print('%-14s s%-2d r%-2d %-5s beta %.4f  P %.5f(%2.0f)  Ps %.5f Pt %.5f  |L| %.4f(%3.0f)  chi %.3f(%.3f)'
                  '  U4 %.3f  tauL %.1f' % (d['datei'], e['stufe'], e['replika'], e['start'][:5], e['beta'], e['pw'],
                                         1e5 * e['pw_err'], e['ps'], e['pt'], e['absL'], 1e4 * e['absL_err'],
                                         e['chiL'], e['chiL_err'], e['binder'], e['tau_int_absL']), flush=True)
    rng = np.random.default_rng(1)
    for key, rows in gruppen.items():
        rows = sorted(rows)
        bs = np.array([r[0] for r in rows]); cs = np.array([r[1] for r in rows]); ce = np.array([r[2] for r in rows])
        g = {'gruppe': key, 'beta': bs.tolist(), 'chi': cs.tolist(), 'chi_err': ce.tolist(),
             'absL': [r[3] for r in rows], 'binder': [r[4] for r in rows]}
        # gleiche beta zusammenfassen (gewichtetes Mittel)
        ub = np.unique(bs)
        cm = np.array([np.average(cs[bs == b], weights=1 / np.maximum(ce[bs == b], 1e-12) ** 2) for b in ub])
        cme = np.array([1 / np.sqrt((1 / np.maximum(ce[bs == b], 1e-12) ** 2).sum()) for b in ub])
        i = int(np.argmax(cm))
        g['beta_chimax_gitterpunkt'] = float(ub[i])
        if 0 < i < len(ub) - 1:
            sel = slice(max(0, i - a.halb), min(len(ub), i + a.halb + 1))
            x, y, ye = ub[sel], cm[sel], cme[sel]
            if len(x) >= 3:
                def peak(yy):
                    A = np.polyfit(x, yy, 2, w=1 / ye)
                    return -A[1] / (2 * A[0]) if A[0] < 0 else np.nan
                p0 = peak(y)
                ps = np.array([peak(y + ye * rng.standard_normal(len(y))) for _ in range(2000)])
                ps = ps[np.isfinite(ps)]
                g['beta_c_parabel'] = f(p0)
                g['beta_c_err'] = f(ps.std()) if len(ps) > 10 else None
                g['parabel_punkte'] = x.tolist()
        out['gruppen'].append(g)
        print('GRUPPE', key, 'Max am Gitterpunkt', g['beta_chimax_gitterpunkt'], 'Parabel', g.get('beta_c_parabel'),
              '+-', g.get('beta_c_err'), flush=True)
    with open(a.out, 'w') as fh:
        json.dump(out, fh, indent=1)


# ================================================================================================ Korrelatoren
M_FAM = {'111': [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)], '100': [(1, 1, 0), (1, 0, 1), (0, 1, 1)]}


def cosh_meff(r, L, d1):
    """Effektive Masse aus r = S(D)/S(D+1) mit S ~ cosh(m (D - L/2)); Bisektion."""
    if not np.isfinite(r) or r <= 1.0:
        return np.nan
    lo, hi = 1e-9, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        q = np.cosh(mid * (d1 - L / 2.0)) / np.cosh(mid * (d1 + 1 - L / 2.0))
        if q < r:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def sigma_ng(E, Lt):
    return ((2 * np.pi / 3) + np.sqrt((2 * np.pi / 3) ** 2 + 4 * Lt ** 2 * E ** 2)) / (2 * Lt ** 2)


def korr(a):
    out = {'kopf': kopf(), 'laeufe': []}
    for p in a.ein:
        res, z = lade(p)
        L, Nt, tau, NV = res['L'], res['Nt'], res['tau'], res['NV']
        Lt = Nt * tau
        box = np.array(res['box']); AV = box / L
        Bv = np.linalg.inv(AV).T                       # reziproke Vektoren (ohne 2 pi): a_i . b_j = delta_ij
        rpos = np.array(res['rpos']); xb = rpos[:NV]
        dn = np.array(list(itertools.product(range(L), range(L), range(L))))      # Reihenfolge wie fftn-Achsen
        # Mindestbild-Abstaende je (b, b', Delta n)
        Binv = np.linalg.inv(box)
        dvec = xb[None, :, None, :] - xb[:, None, None, :] + (dn @ AV)[None, None, :, :]   # (NV, NV, L^3, 3)
        fr = dvec @ Binv
        fr = fr - np.round(fr)
        best = None
        for sh in itertools.product((-1, 0, 1), repeat=3):
            nr = np.linalg.norm((fr + np.array(sh)) @ box, axis=-1)
            best = nr if best is None else np.minimum(best, nr)
        rr = best                                                                  # (NV, NV, L^3)
        d = {'datei': os.path.basename(p), 'L': L, 'Nt': Nt, 'tau': tau, 'L_t': Lt, 'stufen': []}
        for s, st in enumerate(res['stufen']):
            if ('kor_%d' % s) not in z.files:
                continue
            K = z['kor_%d' % s]                       # (nb, R, NV, NV, L, L, L)
            nb, R = K.shape[0], K.shape[1]
            betas = np.array(st['betas'])
            for bval in np.unique(betas):
                rs = np.where(betas == bval)[0]
                Ks = K[:, rs].reshape((nb * len(rs), NV, NV, L ** 3))              # Proben = Bins x Replikas
                ns = len(Ks)
                e = {'stufe': s, 'beta': float(bval), 'replikas': rs.tolist(), 'proben': ns, 'familien': {}}
                Csum = Ks.sum(axis=(1, 2))                                       # (ns, L^3)
                for fam, ms in M_FAM.items():
                    Sm = []
                    dm = []
                    for m in ms:
                        idx = (dn @ np.array(m)) % L
                        Sm.append(np.stack([np.bincount(idx, Csum[i], minlength=L) for i in range(ns)]))
                        dm.append(1.0 / np.linalg.norm(np.array(m) @ Bv))
                    Sm = np.mean(Sm, axis=0)                                     # (ns, L)
                    dfam = float(np.mean(dm))
                    mS, eS, jS = jk(Sm, lambda v: v)
                    meff = []
                    for D in range(1, L // 2):
                        fun = lambda v, D=D: cosh_meff(v[D] / v[D + 1], L, D)    # noqa: E731
                        m0, me, _ = jk(Sm, fun)
                        meff.append({'Delta': D, 'm': f(m0), 'm_err': f(me), 'E': f(m0 / dfam),
                                     'E_err': f(me / dfam),
                                     'sigma_NG': f(sigma_ng(m0 / dfam, Lt)) if np.isfinite(m0) else None,
                                     'sigma_naiv': f(m0 / dfam / Lt)})
                    # Fit A cosh(m (D - L/2)) ueber D = Dmin .. L/2 (log-linear in Paaren nicht moeglich: einfache
                    # Gitter-Suche in m, A linear)
                    def fitm(v, Dmin=a.dmin):
                        D = np.arange(Dmin, L // 2 + 1)
                        y = v[D]
                        if (y <= 0).any():
                            return np.nan
                        best = (np.inf, np.nan)
                        for mm in np.linspace(0.01, 12.0, 2400):
                            c = np.cosh(mm * (D - L / 2.0))
                            A = (y * c).sum() / (c * c).sum()
                            ch = (((y - A * c) / y) ** 2).sum()
                            if ch < best[0]:
                                best = (ch, mm)
                        return best[1]
                    mf, mfe, _ = jk(Sm, fitm)
                    e['familien'][fam] = {'d': dfam, 'S': mS.tolist(), 'S_err': eS.tolist(), 'meff': meff,
                                          'fit_m': f(mf), 'fit_m_err': f(mfe), 'fit_E': f(mf / dfam),
                                          'fit_E_err': f(mfe / dfam),
                                          'fit_sigma_NG': f(sigma_ng(mf / dfam, Lt)) if np.isfinite(mf) else None,
                                          'fit_Dmin': a.dmin}
                    print(d['datei'], 'beta', bval, fam, 'd %.4f' % dfam, 'S', np.round(mS, 6).tolist(),
                          'meff', [(x['Delta'], x['E'], x['E_err']) for x in meff], 'fitE', f(mf / dfam),
                          f(mfe / dfam), flush=True)
                # C(r) gebinnt
                edges = np.linspace(0.0, rr.max() + 1e-9, a.rbins + 1)
                Cr = []
                gueltig = np.ones((NV, NV, L ** 3), bool)
                gueltig[np.arange(NV), np.arange(NV), 0] = False
                for i in range(a.rbins):
                    sel = (rr >= edges[i]) & (rr < edges[i + 1]) & gueltig
                    if sel.any():
                        vals = Ks[:, sel].mean(1)
                        mC, eC, _ = jk(vals[:, None], lambda v: v)
                        Cr.append([float(rr[sel].mean()), float(mC[0]), float(eC[0]), int(sel.sum())])
                e['C_r'] = Cr
                d['stufen'].append(e)
        out['laeufe'].append(d)
    with open(a.out, 'w') as fh:
        json.dump(out, fh, indent=1)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='modus', required=True)
    p = sub.add_parser('tab')
    p.add_argument('--ein', nargs='+', required=True)
    p.add_argument('--nbin', type=int, default=20)
    p.add_argument('--halb', type=int, default=2)
    p.add_argument('--gruppe', default='')
    p.add_argument('--out', required=True)
    p = sub.add_parser('korr')
    p.add_argument('--ein', nargs='+', required=True)
    p.add_argument('--dmin', type=int, default=1)
    p.add_argument('--rbins', type=int, default=12)
    p.add_argument('--out', required=True)
    a = ap.parse_args()
    if a.modus == 'tab':
        tab(a)
    else:
        korr(a)


if __name__ == '__main__':
    main()
