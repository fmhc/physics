#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 S6: Zusammenfassung der Flussauswertungen (ana_flow.py-Ausgaben) fuer Nt_c = 6 und Vergleich mit S5 (Nt_c = 4).
Aufruf: zusammen_s6.py S5DIR S6DIR   (S5DIR enthaelt ana-k.json, ana-n.json, ana-extra.json; S6DIR enthaelt ana-s6-k.json, ana-s6-n.json)
Beschreibend: lineare Extrapolation in x = 1/Nt_c^2 durch zwei Punkte (kein Freiheitsgrad, kein Test der Linearitaet)."""
import json
import sys
import numpy as np

D5, D6 = sys.argv[1], sys.argv[2]
A5, A6 = {}, {}
for f in ('ana-k.json', 'ana-n.json', 'ana-extra.json'):
    A5.update(json.load(open(D5 + '/' + f)))
for f in ('ana-s6-k.json', 'ana-s6-n.json', 'ana-s6-n4.json'):
    A6.update(json.load(open(D6 + '/' + f)))


def g(A, n, c='c0.3'):
    r = A[n]
    k = sorted([x for x in r if x.startswith(c + '_nbin')], key=lambda s: -int(s.split('nbin')[1]))[0]
    return r[k]


def rel(v, e):
    return e / v


print('=== Tabelle S6 (c = 0,3, Jackknife leave-one-out) ===')
for n in A6:
    v = g(A6, n)
    r = A6[n]
    print('%-8s n=%2d  t0=%.5g +- %.2g (%.1f%%)  w0=%.5g  w0/sqrt(t0)=%.4f +- %.4f  Tc sqrt(t0)=%.4f +- %.4f  Es/Et(t0)=%.3f  E0=%.5g' % (
        n, r['n_cfg'], v['t0'], v['err_t0'], v['rel_err_t0_pct'], v['w0'], v['w0_over_sqrt_t0'], v['err_w0_over_sqrt_t0'],
        v['Tc_sqrt_t0'], v['err_Tc_sqrt_t0'], r['Es_zu_Et_bei_t0'], r['E0_mittel']))
print('=== Robustheit nbin (c = 0,3) ===')
for n in A6:
    for x in sorted(k for k in A6[n] if k.startswith('c0.3_nbin')):
        v = A6[n][x]
        print('%-8s %-14s t0=%.5g +- %.2g  w0/sqt0=%.4f +- %.4f  TcSqt0=%.4f +- %.4f' % (n, x, v['t0'], v['err_t0'], v['w0_over_sqrt_t0'], v['err_w0_over_sqrt_t0'], v['Tc_sqrt_t0'], v['err_Tc_sqrt_t0']))


def verh(a, b, key):
    r = a[key] / b[key]
    er = r * np.hypot(a['err_' + key] / a[key], b['err_' + key] / b[key])
    return r, er


kc5, nc5 = g(A5, 'k230'), g(A5, 'n329-pool')
kc6, nc6 = g(A6, 'k243'), g(A6, 'n341')
RT5, eT5 = verh({'Tc_sqrt_t0': nc5['Tc_sqrt_t0'], 'err_Tc_sqrt_t0': nc5['err_Tc_sqrt_t0']}, {'Tc_sqrt_t0': kc5['Tc_sqrt_t0'], 'err_Tc_sqrt_t0': kc5['err_Tc_sqrt_t0']}, 'Tc_sqrt_t0')
RT6, eT6 = verh({'Tc_sqrt_t0': nc6['Tc_sqrt_t0'], 'err_Tc_sqrt_t0': nc6['err_Tc_sqrt_t0']}, {'Tc_sqrt_t0': kc6['Tc_sqrt_t0'], 'err_Tc_sqrt_t0': kc6['err_Tc_sqrt_t0']}, 'Tc_sqrt_t0')
Rw5, ew5 = verh({'w': nc5['w0_over_sqrt_t0'], 'err_w': nc5['err_w0_over_sqrt_t0']}, {'w': kc5['w0_over_sqrt_t0'], 'err_w': kc5['err_w0_over_sqrt_t0']}, 'w')
Rw6, ew6 = verh({'w': nc6['w0_over_sqrt_t0'], 'err_w': nc6['err_w0_over_sqrt_t0']}, {'w': kc6['w0_over_sqrt_t0'], 'err_w': kc6['err_w0_over_sqrt_t0']}, 'w')
print('=== Verhaeltnisse Netz/Hyperkubus (c = 0,3, nur Statistik; beta_c-Zuordnung: S5 3,29/2,30; S6 3,41/2,43) ===')
print('T_c sqrt t0: S5 %.4f +- %.4f (%+.1f%%)   S6 %.4f +- %.4f (%+.1f%%)' % (RT5, eT5, 100 * (RT5 - 1), RT6, eT6, 100 * (RT6 - 1)))
print('w0/sqrt t0 : S5 %.4f +- %.4f (%+.1f%%)   S6 %.4f +- %.4f (%+.1f%%)' % (Rw5, ew5, 100 * (Rw5 - 1), Rw6, ew6, 100 * (Rw6 - 1)))
for c in ('c0.1125',):
    k5, n5, k6, n6 = g(A5, 'k230', c), g(A5, 'n329-pool', c), g(A6, 'k243', c), g(A6, 'n341', c)
    print('c=0,1125: T_c sqrt t0 Verhaeltnis S5 %.4f S6 %.4f ; w0/sqrt t0 Verhaeltnis S5 %.4f S6 %.4f ; sqrt t0 Netz S6 %.4f a, t0 Netz %.5g ; Hyperkubus Tc sqrt t0 S6 %.4f' % (
        n5['Tc_sqrt_t0'] / k5['Tc_sqrt_t0'], n6['Tc_sqrt_t0'] / k6['Tc_sqrt_t0'], n5['w0_over_sqrt_t0'] / k5['w0_over_sqrt_t0'],
        n6['w0_over_sqrt_t0'] / k6['w0_over_sqrt_t0'], n6['sqrt_t0'], n6['t0'], k6['Tc_sqrt_t0']))

# ---------------- beta-Steigung und Fenster
def steig(A, ns, bl, nm):
    ls = np.array([np.log(g(A, n)['sqrt_t0']) for n in ns])
    p = np.polyfit(bl, ls, 1)
    print(nm, 'ln sqrt t0 =', ls.round(4), ' Steigung unten %.2f oben %.2f gesamt %.2f je beta' % ((ls[1] - ls[0]) / (bl[1] - bl[0]), (ls[2] - ls[1]) / (bl[2] - bl[1]), p[0]))
    return p[0]
sh = steig(A6, ('k238', 'k243', 'k248'), (2.38, 2.43, 2.48), 'Hyperkubus S6')
sn = steig(A6, ('n336', 'n341', 'n346'), (3.36, 3.41, 3.46), 'Netz S6')
bn = np.array([3.36, 3.41, 3.46])
ltn = np.array([np.log(g(A6, n)['Tc_sqrt_t0']) for n in ('n336', 'n341', 'n346')])
pn = np.polyfit(bn, ltn, 2)
bk = np.array([2.38, 2.43, 2.48])
ltk = np.array([np.log(g(A6, n)['Tc_sqrt_t0']) for n in ('k238', 'k243', 'k248')])
pk = np.polyfit(bk, ltk, 2)
ref = kc6['Tc_sqrt_t0']
bb = np.linspace(3.30, 3.52, 2201)
v = np.exp(np.polyval(pn, bb))
i = np.argmin(np.abs(v - ref))
print('beta* mit T_c sqrt t0(Netz) = Hyperkubus 2,43 (%.4f): %.4f' % (ref, bb[i]))
for lo, hi, name in ((0.85, 1.15, '15%'), (0.9, 1.1, '10%'), (0.95, 1.05, '5%'), (0.98, 1.02, '2%')):
    m = (v / ref >= lo) & (v / ref <= hi)
    print('beta_c-Fenster Netz fuer |Abweichung| < %s: %.4f bis %.4f' % (name, bb[m].min() if m.any() else float('nan'), bb[m].max() if m.any() else float('nan')))
for b0, txt in ((3.386, 'heiss'), (3.411, 'Regel'), (3.430, '5-Punkt'), (3.381, 'Regel-0,03'), (3.441, 'Regel+0,03')):
    print('beta_c(Netz)=%.3f (%s): T_c sqrt t0 Netz %.4f, Verhaeltnis zu Hyperkubus(2,43) %.3f' % (b0, txt, np.exp(np.polyval(pn, b0)), np.exp(np.polyval(pn, b0)) / ref))
for b0 in (2.4291, 2.43, 2.437, 2.457):
    print('Hyperkubus beta=%.4f: T_c sqrt t0 = %.4f ; Verhaeltnis Netz(3,411)/Hyperkubus = %.3f' % (b0, np.exp(np.polyval(pk, b0)), np.exp(np.polyval(pn, 3.411)) / np.exp(np.polyval(pk, b0))))

# ---------------- Extrapolation in x = 1/Nt_c^2 (beschreibend)
x5, x6 = 1.0 / 16, 1.0 / 36
a_, b_ = x5 / (x5 - x6), x6 / (x5 - x6)
def extra(q5, e5, q6, e6, nm):
    q0 = a_ * q6 - b_ * q5
    e0 = np.hypot(a_ * e6, b_ * e5)
    print('%-26s Nt_c=4: %.4f +- %.4f ; Nt_c=6: %.4f +- %.4f ; linear in 1/Nt_c^2 nach 0: %.4f +- %.4f' % (nm, q5, e5, q6, e6, q0, e0))
print('=== beschreibende Extrapolation (zwei Punkte; Faktoren %.3f und %.3f; Fehler nur statistisch) ===' % (a_, b_))
extra(RT5, eT5, RT6, eT6, 'R_T = Tc sqrt t0 Netz/Hyp.')
extra(Rw5, ew5, Rw6, ew6, 'R_w = w0/sqrt t0 Netz/Hyp.')
extra(kc5['Tc_sqrt_t0'], kc5['err_Tc_sqrt_t0'], kc6['Tc_sqrt_t0'], kc6['err_Tc_sqrt_t0'], 'Tc sqrt t0 Hyperkubus')
extra(nc5['Tc_sqrt_t0'], nc5['err_Tc_sqrt_t0'], nc6['Tc_sqrt_t0'], nc6['err_Tc_sqrt_t0'], 'Tc sqrt t0 Netz')
extra(kc5['w0_over_sqrt_t0'], kc5['err_w0_over_sqrt_t0'], kc6['w0_over_sqrt_t0'], kc6['err_w0_over_sqrt_t0'], 'w0/sqrt t0 Hyperkubus')
extra(nc5['w0_over_sqrt_t0'], nc5['err_w0_over_sqrt_t0'], nc6['w0_over_sqrt_t0'], nc6['err_w0_over_sqrt_t0'], 'w0/sqrt t0 Netz')
# Mit beta-Unsicherheit des Netzes (Steigung * 0,03): Band von R_T je Abstand
print('beta-Band R_T: S5 (beta_c +-0,03, Steigung 4,69): +-%.1f%% ; S6 (+-0,03, Steigung Netz %.2f, Hyperkubus %.2f): +-%.1f%% (Netz) und +-%.1f%% (Hyperkubus 0,01)' % (
    100 * 4.69 * 0.03, sn, sh, 100 * sn * 0.03, 100 * sh * 0.01))
# ---------------- kappa_eff
print('=== implizites kappa (Diagnose, haengt an beta_c): kappa_eff/kappa = (T_c sqrt t0 Hyp./T_c sqrt t0 Netz)^2 ===')
print('S5 %.3f ; S6 %.3f ; Verhaeltnis S6/S5 %.3f' % ((1 / RT5) ** 2, (1 / RT6) ** 2, (RT5 / RT6) ** 2))
# ---------------- Endvolumen
if 'n4' in A6:
    print('Endvolumen Netz S6: t0(L=4)/t0(L=6) = %.4f ; Fehler %.3f' % (g(A6, 'n4')['t0'] / nc6['t0'], g(A6, 'n4')['t0'] / nc6['t0'] * np.hypot(g(A6, 'n4')['err_t0'] / g(A6, 'n4')['t0'], nc6['err_t0'] / nc6['t0'])))
print('E_s/E_t bei t0 (Freifeld-Vorhersage 0,4568):', {n: round(A6[n]['Es_zu_Et_bei_t0'], 3) for n in A6})
print('t0 je Konfiguration (Mittel, Std):', {n: [round(x, 4) for x in A6[n]['t0_je_cfg_mittel_std']] for n in A6}, ' Lag1:', {n: round(A6[n]['t0_lag1'], 2) for n in A6})
