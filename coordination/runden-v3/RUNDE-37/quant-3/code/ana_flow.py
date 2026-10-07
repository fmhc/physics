#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S5: Auswertung der Flusslaeufe (numpy, CPU). t0, w0, T_c*Wurzel(t0), Jackknife ueber Konfigurationsbloecke.
Aufruf: ana_flow.py AUS.json DIR gruppe:kappa:Tc:name:datei1[+datei2]:iβ ...  (iβ = Index der Kopplung im npz)
Flusszeit in a^2: t = kappa * t_Lauf. t0: t^2 E = c; w0: W(w0^2) = c, W = t d(t^2 E)/dt."""
import json
import sys
import numpy as np

CS = (0.3, 0.1125)


def kreuzung(t, y, c, ab=0):
    """erste Kreuzung y = c von unten, Interpolation linear in (ln t, ln y); t,y aufsteigend in t"""
    for i in range(max(ab, 0), len(t) - 1):
        if y[i] < c <= y[i + 1]:
            f = (np.log(c) - np.log(y[i])) / (np.log(y[i + 1]) - np.log(y[i]))
            return float(np.exp(np.log(t[i]) + f * (np.log(t[i + 1]) - np.log(t[i]))))
    return float('nan')


def groessen(E, t, kappa, c):
    """E: Mittel der Energie (nt,) zu den Zeiten t (Lauf); liefert t0, w0 (in a^2 bzw. a^2)"""
    tp = kappa * t
    f = tp ** 2 * E
    m = tp > 0
    tp, f = tp[m], f[m]
    t0 = kreuzung(tp, f, c)
    lt = np.log(tp)
    W = (f[1:] - f[:-1]) / (lt[1:] - lt[:-1])
    tm = np.exp(0.5 * (lt[1:] + lt[:-1]))
    w2 = kreuzung(tm, W, c)
    return t0, w2, float(f.max()), float(W.max())


def jk(Eall, t, kappa, c, nbin):
    n = len(Eall)
    nb = min(nbin, n)
    sz = n // nb
    idx = [np.arange(i * sz, (i + 1) * sz if i < nb - 1 else n) for i in range(nb)]
    voll = groessen(Eall.mean(0), t, kappa, c)
    ps = []
    for b in range(nb):
        keep = np.setdiff1d(np.arange(n), idx[b])
        ps.append(groessen(Eall[keep].mean(0), t, kappa, c)[:2])
    ps = np.array(ps)
    fehl = np.sqrt((nb - 1) / nb * ((ps - ps.mean(0)) ** 2).sum(0))
    return voll, ps, fehl, nb


def main():
    aus, dr = sys.argv[1], sys.argv[2]
    res = {}
    for spec in sys.argv[3:]:
        gr, kappa, Tc, name, dat, ib = spec.split(':')
        kappa, Tc, ib = float(kappa), float(Tc), int(ib)
        Es = []
        for d in dat.split('+'):
            z = np.load('%s/%s.npz' % (dr, d))
            Es.append(z['E_%d' % ib])
            t = z['t']
        Eall = np.concatenate(Es)[:, :, :]
        n = len(Eall)
        r = {'gruppe': gr, 'datei': dat, 'ib': ib, 'kappa': kappa, 'Tc': Tc, 'n_cfg': n, 'E0_mittel': float(Eall[:, 0, 0].mean()),
             'E0_Fehler': float(Eall[:, 0, 0].std(ddof=1) / np.sqrt(n))}
        for c in CS:
            for nbin in (n, max(2, n // 2)):
                voll, ps, fe, nb = jk(Eall[:, :, 0], t, kappa, c, nbin)
                t0, w2, fmax, Wmax = voll
                key = 'c%g_nbin%d' % (c, nb)
                rr = {'t0': t0, 'w0_quadrat': w2, 'sqrt_t0': float(np.sqrt(t0)) if t0 == t0 else float('nan'),
                      'w0': float(np.sqrt(w2)) if w2 == w2 else float('nan'), 'err_t0': float(fe[0]), 'err_w02': float(fe[1]), 'max_t2E': fmax, 'max_W': Wmax}
                if t0 == t0:
                    rr['rel_err_t0_pct'] = 100 * float(fe[0]) / t0
                    # Fehler fortgepflanzt auf Wurzel und Tc*Wurzel(t0)
                    rr['Tc_sqrt_t0'] = Tc * np.sqrt(t0)
                    rr['err_Tc_sqrt_t0'] = Tc * 0.5 * fe[0] / np.sqrt(t0)
                if t0 == t0 and w2 == w2:
                    rat = ps[:, 1] ** 0.5 / ps[:, 0] ** 0.5
                    rv = np.sqrt(w2) / np.sqrt(t0)
                    rr['w0_over_sqrt_t0'] = float(rv)
                    rr['err_w0_over_sqrt_t0'] = float(np.sqrt((nb - 1) / nb * ((rat - rat.mean()) ** 2).sum()))
                r[key] = rr
        # Anteil E_s/E_t bei Flusszeit t0 (c=0.3), Mittel
        tp = kappa * t
        m = np.argmin(np.abs(tp - groessen(Eall[:, :, 0].mean(0), t, kappa, 0.3)[0]))
        r['Es_zu_Et_bei_t0'] = float(Eall[:, m, 1].mean() / Eall[:, m, 2].mean()) if np.isfinite(m) else None
        r['Es_zu_Et_bei_t=0'] = float(Eall[:, 0, 1].mean() / Eall[:, 0, 2].mean())
        # Einzelkonfigurationen: t0 je Konfiguration (Streuung)
        t0c = [groessen(E[:, 0], t, kappa, 0.3)[0] for E in Eall]
        r['t0_je_cfg_mittel_std'] = [float(np.nanmean(t0c)), float(np.nanstd(t0c, ddof=1))]
        # Autokorrelationshinweis: t0 je Konfiguration, Lag-1-Korrelation
        a = np.array(t0c)
        a = a - a.mean()
        r['t0_lag1'] = float((a[1:] * a[:-1]).sum() / (a * a).sum()) if len(a) > 2 else None
        res[name] = r
        k = 'c0.3_nbin%d' % min(n, n)
        q = r[k]
        print('%-12s n=%2d beta_i=%d E0=%.4g  t0=%.5g +- %.2g (%.2f%%)  w0=%.5g  w0/sqrt(t0)=%s+-%s  Tc sqrt(t0)=%s  Es/Et(t0)=%.3f  lag1=%s' % (
            name, n, ib, r['E0_mittel'], q['t0'], q['err_t0'], q.get('rel_err_t0_pct', float('nan')), q['w0'],
            ('%.4f' % q['w0_over_sqrt_t0']) if 'w0_over_sqrt_t0' in q else 'nan',
            ('%.4f' % q['err_w0_over_sqrt_t0']) if 'err_w0_over_sqrt_t0' in q else 'nan',
            ('%.4f+-%.4f' % (q['Tc_sqrt_t0'], q['err_Tc_sqrt_t0'])) if 'Tc_sqrt_t0' in q else 'nan', r['Es_zu_Et_bei_t0'], r['t0_lag1']))
        k2 = 'c0.1125_nbin%d' % n
        q2 = r[k2]
        print('   c=0.1125: t0=%.5g w0=%.5g Tc sqrt t0=%s  max t2E=%.3g max W=%.3g' % (q2['t0'], q2['w0'], q2.get('Tc_sqrt_t0'), q['max_t2E'], q['max_W']))
    with open(aus, 'w') as f:
        json.dump(res, f, indent=1)


if __name__ == '__main__':
    main()
