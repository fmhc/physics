#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S5: Zusammenfassung aus ana-*.json: Verhaeltnisse Netz/Hyperkubus, Steigung nach beta, beta*-Fenster."""
import json
import sys
import numpy as np
D = sys.argv[1]
A = {}
for f in ('ana-k.json', 'ana-n.json', 'ana-extra.json'):
    A.update(json.load(open(D + '/' + f)))
A.pop('n334', None)  # tmax 15 reichte nicht (t^2 E < 0,3), ersetzt durch n334b
def q(n, c='c0.3', k=None):
    r = A[n]
    k = k or [x for x in r if x.startswith(c + '_nbin')]
    return r, {x: r[x] for x in k}
print('--- nbin-Robustheit (c=0.3): n, t0 +- err, w0/sqrt t0 +- err')
for n in A:
    for x in sorted(k for k in A[n] if k.startswith('c0.3_nbin')):
        v = A[n][x]
        print('%-10s %-14s t0=%.5g +- %.2g  w0/sqt0=%.4f +- %.4f  TcSqt0=%.4f +- %.4f' % (n, x, v['t0'], v['err_t0'], v['w0_over_sqrt_t0'], v['err_w0_over_sqrt_t0'], v['Tc_sqrt_t0'], v['err_Tc_sqrt_t0']))
def g(n, c='c0.3'):
    r = A[n]
    k = [x for x in r if x.startswith(c + '_nbin')]
    k = sorted(k, key=lambda s: -int(s.split('nbin')[1]))[0]
    return r[k]
kc, nc = g('k230'), g('n329-pool')
rat = nc['Tc_sqrt_t0'] / kc['Tc_sqrt_t0']
er = rat * np.hypot(nc['err_Tc_sqrt_t0'] / nc['Tc_sqrt_t0'], kc['err_Tc_sqrt_t0'] / kc['Tc_sqrt_t0'])
print('Netz/Hyperkubus T_c sqrt t0 (c=0.3, beta 3.29 / 2.30): %.4f +- %.4f (%.1f %%)' % (rat, er, 100 * (rat - 1)))
rw = nc['w0_over_sqrt_t0'] / kc['w0_over_sqrt_t0']
erw = rw * np.hypot(nc['err_w0_over_sqrt_t0'] / nc['w0_over_sqrt_t0'], kc['err_w0_over_sqrt_t0'] / kc['w0_over_sqrt_t0'])
print('Netz/Hyperkubus w0/sqrt t0: %.4f +- %.4f (%.1f %%)' % (rw, erw, 100 * (rw - 1)))
# c = 0.1125
kc2, nc2 = g('k230', 'c0.1125'), g('n329-pool', 'c0.1125')
print('c=0.1125: T_c sqrt t0 Netz/Hyperkubus %.4f ; sqrt t0 netz %.4f a ; t0 netz %.5g ; w0/sqrt t0 cube %.4f netz %.4f' % (
    nc2['Tc_sqrt_t0'] / kc2['Tc_sqrt_t0'], nc2['sqrt_t0'], nc2['t0'], kc2['w0_over_sqrt_t0'], nc2['w0_over_sqrt_t0']))
# beta-Steigung
for nm, bl, ns in (('Hyperkubus', (2.25, 2.30, 2.35), ('k225', 'k230', 'k235')), ('Netz', (3.24, 3.29, 3.34), ('n324', 'n329-pool', 'n334b'))):
    ls = np.array([np.log(g(n)['sqrt_t0']) for n in ns])
    es = np.array([0.5 * g(n)['err_t0'] / g(n)['t0'] for n in ns])
    print(nm, 'ln sqrt t0:', ls.round(4), 'Steigung unten %.2f oben %.2f gesamt %.2f je beta' % ((ls[1] - ls[0]) / (bl[1] - bl[0]), (ls[2] - ls[1]) / (bl[2] - bl[1]), np.polyfit(bl, ls, 1)[0]))
# Fenster fuer beta_c des Netzes (S5b: |Abw| < 15 %) mit linearer Interpolation von ln(Tc sqrt t0) ueber 3.24..3.34
bl = np.array([3.24, 3.29, 3.34])
lt = np.array([np.log(g(n)['Tc_sqrt_t0']) for n in ('n324', 'n329-pool', 'n334b')])
p = np.polyfit(bl, lt, 2)
bb = np.linspace(3.2, 3.38, 1801)
v = np.exp(np.polyval(p, bb))
ref = kc['Tc_sqrt_t0']
for lo, hi, name in ((0.0, 0.0, 'gleich'), (0.85, 1.15, '15%-Fenster'), (0.9, 1.1, '10%'), (0.95, 1.05, '5%')):
    if name == 'gleich':
        i = np.argmin(np.abs(v - ref))
        print('beta* mit T_c sqrt t0(netz) = Hyperkubus (%.4f): %.4f' % (ref, bb[i]))
    else:
        m = (v / ref >= lo) & (v / ref <= hi)
        print('beta_c-Fenster fuer %s: %.4f bis %.4f' % (name, bb[m].min(), bb[m].max()))
for b0 in (3.25, 3.27, 3.30, 3.33):
    print('beta_c=%.2f: T_c sqrt t0 netz %.4f, Verhaeltnis zu Hyperkubus 2.30: %.3f' % (b0, np.exp(np.polyval(p, b0)), np.exp(np.polyval(p, b0)) / ref))
for b0 in (2.2986, 2.304, 2.30):
    bk = np.array([2.25, 2.30, 2.35])
    lk = np.array([np.log(g(n)['Tc_sqrt_t0']) for n in ('k225', 'k230', 'k235')])
    pk = np.polyfit(bk, lk, 2)
    print('Hyperkubus beta=%.4f: T_c sqrt t0 = %.4f' % (b0, np.exp(np.polyval(pk, b0))))
# Endvolumen
print('Endvolumen: Netz L=4 / L=6 (t0, c=0.3): %.4f ; Hyperkubus L=8,Nt=8 / L=12,Nt=12: %.4f' % (g('n4t12')['t0'] / g('n329-pool')['t0'], g('k8t8')['t0'] / g('k230')['t0']))
print('E_s/E_t bei t0:', {n: round(A[n]['Es_zu_Et_bei_t0'], 3) for n in A}, ' bei Flusszeit 0:', {n: round(A[n]['Es_zu_Et_bei_t=0'], 3) for n in A if n.startswith('n')})
print('t0 je Konfiguration: Mittel, Std:', {n: [round(x, 4) for x in A[n]['t0_je_cfg_mittel_std']] for n in A})
