#!/usr/bin/env python3
"""ATEM-NETZ-1: Auswertung (Urteilsregeln aus PLAN.md Abschn. 7, vor den Hauptlaeufen eingefroren).

Aufruf auf der .69 (kleintest.sh): auswertung.py <lauf-ordner>  ->  <lauf-ordner>/auswertung.json und Bilder (PNG).
"""
import json
import math
import os
import sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = sys.argv[1]


def lade(name):
    p = os.path.join(D, name)
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def med(x):
    x = [v for v in x if v is not None]
    return float(np.median(x)) if x else None


out = {'fehlend': []}

# ------------------------------------------------------------------ AN0 (Teil A)
A, K = {}, None
for fn in ('A1.json', 'A2.json', 'A3.json', 'A4.json'):
    a = lade(fn)
    if a is None:
        out['fehlend'].append(fn)
        continue
    K = a['K']
    for name in ('paar', 'kette', 'quadrat', 'dreieck', 'diamant'):
        if name in a:
            A.setdefault(name, []).extend(a[name]['seeds'])
an0 = {}
if 'paar' in A:
    p = A['paar']
    an0['paar_abstand_pi_end_voll'] = [s['voll']['abstand_pi_end'] for s in p]
    an0['paar_rate_voll_2K'] = [s['voll']['rate'] / (2 * K) if s['voll']['rate'] else None for s in p]
    an0['paar_rate_mittel_2K'] = [s['mittel']['rate'] / (2 * K) if s['mittel']['rate'] else None for s in p]
    i_ok = all(d <= 0.05 for d in an0['paar_abstand_pi_end_voll'])
    mr = med(an0['paar_rate_voll_2K'])
    an0['paar_rate_median'] = mr
    iv_paar = mr is not None and 0.9 <= mr <= 1.1
else:
    i_ok, iv_paar = False, False
ii_plan, ii_karte, iv_gitter = True, True, True
for name in ('kette', 'quadrat', 'diamant'):
    if name not in A:
        ii_plan = ii_karte = False
        continue
    g = [s['voll']['gegentakt_end'] for s in A[name]]
    gm = [s['mittel']['gegentakt_end'] for s in A[name]]
    an0[name] = {'gegentakt_voll': g, 'gegentakt_mittel': gm, 'median': med(g), 'min': min(g)}
    ii_plan &= med(g) >= 0.95
    ii_karte &= min(g) >= 0.95
if 'dreieck' in A:
    c = [s['voll']['chi_betrag_mittel'] for s in A['dreieck']]
    cmin = [s['voll']['chi_betrag_min'] for s in A['dreieck']]
    an0['dreieck'] = {'chi_betrag_mittel_voll': c, 'chi_betrag_min_voll': cmin,
                      'anteil_chi_09_voll': [s['voll']['anteil_chi_09'] for s in A['dreieck']],
                      'chi_betrag_mittel_gemittelt': [s['mittel']['chi_betrag_mittel'] for s in A['dreieck']],
                      'gegentakt_voll': [s['voll']['gegentakt_end'] for s in A['dreieck']],
                      'median': med(c)}
    iii_plan = med(c) >= 0.9
    iii_karte = min(cmin) >= 0.9
else:
    iii_plan = iii_karte = False
for name in ('kette', 'quadrat', 'dreieck', 'diamant'):
    if name not in A:
        iv_gitter = False
        continue
    q = []
    for s in A[name]:
        tv, tm = s['voll']['t_halb'], s['mittel']['t_halb']
        q.append(tv / tm if (tv is not None and tm not in (None, 0)) else None)
    an0.setdefault(name, {})['t_halb_verhaeltnis'] = q
    an0[name]['t_halb_median'] = med(q)
    iv_gitter &= (med(q) is not None and 0.9 <= med(q) <= 1.1)
iv = iv_paar and iv_gitter
an0['teilurteile'] = {'i': i_ok, 'ii_plan': ii_plan, 'ii_karte': ii_karte, 'iii_plan': iii_plan,
                      'iii_karte': iii_karte, 'iv': iv, 'iv_paar': iv_paar, 'iv_gitter': iv_gitter}
an0['urteil_plan'] = 'eingetroffen' if (i_ok and ii_plan and iii_plan and iv) else 'verfehlt'
an0['urteil_karte'] = 'eingetroffen' if (i_ok and ii_karte and iii_karte and iv) else 'verfehlt'
out['AN0'] = an0

# ------------------------------------------------------------------ AN1 (Teil B1)
an1 = {'saaten': []}
for fn in ('B1_pyro_s1.json', 'B1_pyro_s2.json'):
    b = lade(fn)
    if b is None:
        out['fehlend'].append(fn)
        continue
    z = b['reihe'][-1]
    pl = z['anteil_summe_klein'] >= 0.9 and z['P1'] >= 0.8 and z['anteil_22'] >= 0.8
    ka = z['anteil_summe_klein'] >= 0.9 and z['S'] >= 0.8 and z['anteil_22'] >= 0.8
    an1['saaten'].append({'datei': fn, 'takt': z['takt'], 'werte': z, 'plan': pl, 'karte': ka})


def urteil(liste):
    if len(liste) < 2:
        return 'nicht entscheidbar'
    if all(liste):
        return 'eingetroffen'
    if not any(liste):
        return 'verfehlt'
    return 'unentschieden'


an1['urteil_plan'] = urteil([s['plan'] for s in an1['saaten']])
an1['urteil_karte'] = urteil([s['karte'] for s in an1['saaten']])
bd = lade('B1_dia_s1.json')
if bd is not None:
    an1['diamant_kontrolle_ende'] = bd['reihe'][-1]
out['AN1'] = an1

# ------------------------------------------------------------------ AN2 (Teil B2)


def kappa50(res, seeds=None):
    ks = sorted(set(r['kappa'] for r in res))
    f = []
    for k in ks:
        v = [r['gefroren'] for r in res if r['kappa'] == k and (seeds is None or r['seed'] in seeds)]
        f.append(float(np.mean(v)))
    for i, (k, fv) in enumerate(zip(ks, f)):
        if fv >= 0.5:
            if i == 0:
                return None, 'unterhalb des Bereichs', ks, f
            k0, f0 = ks[i - 1], f[i - 1]
            t = (0.5 - f0) / (fv - f0)
            return float(math.exp(math.log(k0) + t * (math.log(k) - math.log(k0)))), 'ok', ks, f
    return None, 'nicht bestimmbar', ks, f


an2 = {}
bp, bdd = lade('B2_pyro.json'), lade('B2_dia.json')
if bp is not None and bdd is not None:
    kp, sp_, ksp, fp = kappa50(bp['res'])
    kd, sd_, ksd, fd = kappa50(bdd['res'])
    an2.update({'kappa50_pyro': kp, 'status_pyro': sp_, 'kappa50_dia': kd, 'status_dia': sd_,
                'kurve_pyro': list(zip(ksp, fp)), 'kurve_dia': list(zip(ksd, fd))})
    if kp and kd:
        R = kd / kp
        an2['R'] = R
        an2['R_durch_koordination_1_5'] = R / 1.5
        an2['urteil_plan'] = an2['urteil_karte'] = 'eingetroffen' if R >= 1.5 else 'verfehlt'
    else:
        an2['urteil_plan'] = an2['urteil_karte'] = 'nicht entscheidbar'
    for s in (1, 2):
        a_, _, _, _ = kappa50(bp['res'], [s])
        b_, _, _, _ = kappa50(bdd['res'], [s])
        an2['saat_%d' % s] = {'kappa50_pyro': a_, 'kappa50_dia': b_, 'R': (b_ / a_) if (a_ and b_) else None}
    an2['muster_pyro'] = [{k: r[k] for k in r if k in ('kappa', 'seed', 'gefroren', 'sin_gefroren_mittel',
                                                        'tetra_gefroren_hist', 'cos_laufende_bindungen')}
                          for r in bp['res']]
    an2['muster_dia'] = [{k: r[k] for k in r if k in ('kappa', 'seed', 'gefroren', 'gefroren_A', 'gefroren_B',
                                                       'sin_gefroren_mittel', 'cos_laufende_bindungen')}
                         for r in bdd['res']]
else:
    out['fehlend'] += ['B2_pyro.json/B2_dia.json']
    an2['urteil_plan'] = an2['urteil_karte'] = 'nicht entscheidbar'
out['AN2'] = an2

# ------------------------------------------------------------------ AN3, AN4 (Teil C, 2D)
an3 = {}
c84 = lade('C2_084.json')
if c84 is not None:
    w, k = c84['schwach'], c84['kontrolle']
    C = w['kontakt_cos']
    an3.update({'kontakt_cos': C, 'msd_0_100': w.get('msd_0_100'), 'msd_100_200': w.get('msd_100_200'),
                'kontrolle_msd_0_100': k.get('msd_0_100'), 'kontrolle_msd_100_200': k.get('msd_100_200')})
    m01, m12, k01, k12 = w.get('msd_0_100'), w.get('msd_100_200'), k.get('msd_0_100'), k.get('msd_100_200')
    if None in (C, m01, m12, k01, k12):
        an3['urteil_plan'] = an3['urteil_karte'] = 'nicht entscheidbar'
    else:
        pl = C <= -0.5 and m12 >= max(2 * k12, 0.01)
        ka = C <= -0.5 and m01 >= 2 * k01
        an3['urteil_plan'] = 'eingetroffen' if pl else 'verfehlt'
        an3['urteil_karte'] = 'eingetroffen' if ka else 'verfehlt'
        an3['teil_msd_karte'] = m01 >= 2 * k01
        an3['teil_msd_plan'] = m12 >= max(2 * k12, 0.01)
else:
    out['fehlend'].append('C2_084.json')
    an3['urteil_plan'] = an3['urteil_karte'] = 'nicht entscheidbar'
out['AN3'] = an3

an4 = {'r': {}, 'steigung': {}}
rs = []
for tag in ('080', '084', '088'):
    c = lade('C2_%s.json' % tag)
    if c is None:
        out['fehlend'].append('C2_%s.json' % tag)
        continue
    r = c['schwach'].get('pump_r')
    an4['r'][tag] = r
    an4['steigung'][tag] = c['schwach'].get('pump_steigung')
    rs.append(r)
if len(rs) == 3 and all(r is not None for r in rs):
    hit = sum(r >= 0.3 for r in rs) >= 2 or sum(r <= -0.3 for r in rs) >= 2
    an4['urteil_plan'] = an4['urteil_karte'] = 'eingetroffen' if hit else 'verfehlt'
else:
    an4['urteil_plan'] = an4['urteil_karte'] = 'nicht entscheidbar'
c0 = lade('C0.json')
if c0 is not None:
    an4['C0'] = c0['res']
out['AN4'] = an4

# ------------------------------------------------------------------ Zaehlung "was bildet sich von selbst"
zl = {}
for tag, fn in (('2D_080', 'C2_080.json'), ('2D_084', 'C2_084.json'), ('2D_088', 'C2_088.json'),
                ('3D_060', 'C3_060.json'), ('3D_064', 'C3_064.json'), ('3D_068', 'C3_068.json')):
    c = lade(fn)
    if c is None:
        out['fehlend'].append(fn)
        continue
    e = {'entspannung': c['entspannung']}
    for art in ('schwach', 'stark', 'kontrolle'):
        if art not in c:
            continue
        r = c[art]
        e[art] = {k: r[k] for k in r if k not in ('bild', 'pump_probe')}
    zl[tag] = e
b3 = lade('B3.json')
if b3 is not None:
    zl['B3_gemittelt_pyro'] = [{'T_rel': l['T_rel'], 'ende': l['reihe'][-1]} for l in b3['laeufe']]
out['zaehlung'] = zl

with open(os.path.join(D, 'auswertung.json'), 'w') as fh:
    json.dump(out, fh, indent=1)

# ------------------------------------------------------------------ Bilder
fig, ax = plt.subplots(1, 3, figsize=(16, 4.6))
for fn, ls in (('B1_pyro_s1.json', '-'), ('B1_pyro_s2.json', '--')):
    b = lade(fn)
    if b is None:
        continue
    t = [z['takt'] for z in b['reihe']]
    for key, col in (('P1', 'C0'), ('S', 'C1'), ('anteil_summe_klein', 'C2'), ('anteil_22', 'C3'), ('anteil_31', 'C4')):
        ax[0].plot(t, [z.get(key) for z in b['reihe']], ls, color=col, label=key if ls == '-' else None)
if bd is not None:
    ax[0].plot([z['takt'] for z in bd['reihe']], [-z['e'] for z in bd['reihe']], ':', color='k', label='Diamant Gegentakt')
ax[0].axhline(0.8, color='grey', lw=0.5)
ax[0].set_xlabel('Takt')
ax[0].set_title('B1 Pyrochlor, volle Dynamik (Saat 1 -, 2 --)')
ax[0].legend(fontsize=7)
if bp is not None and bdd is not None:
    ax[1].semilogx(ksp, fp, 'o-', label='Pyrochlor (z = 6)')
    ax[1].semilogx(ksd, fd, 's-', label='Diamant (z = 4)')
    for kk, col in ((0.0347, 'C0'), (0.0335, 'C0'), (0.0521, 'C1')):
        ax[1].axvline(kk, color=col, lw=0.6, ls=':')
    ax[1].axhline(0.5, color='grey', lw=0.5)
    ax[1].set_xlabel('kappa = mu k eps^2 / (8 omega)')
    ax[1].set_ylabel('Anteil eingefrorener Takte')
    ax[1].set_title('B2 Takt-Stillstand (Punkte: Vorhersagen K1/K4)')
    ax[1].legend(fontsize=8)
if b3 is not None:
    for l, ls in zip(b3['laeufe'], ('--', '-')):
        t = [z['t_K'] for z in l['reihe']]
        ax[2].semilogx(t, [z['P1'] for z in l['reihe']], ls, color='C0', label='P(1), T/K=%g' % l['T_rel'])
        ax[2].semilogx(t, [z['S'] for z in l['reihe']], ls, color='C1', label='S, T/K=%g' % l['T_rel'])
        ax[2].semilogx(t, [z['anteil_summe_klein'] for z in l['reihe']], ls, color='C2',
                       label='Summe<0,1, T/K=%g' % l['T_rel'])
    ax[2].axhline(0.8, color='grey', lw=0.5)
    ax[2].set_xlabel('t K (gemittelte XY-Dynamik)')
    ax[2].set_title('B3 Diagnose: lange Zeiten, gemittelt')
    ax[2].legend(fontsize=7)
fig.tight_layout()
fig.savefig(os.path.join(D, 'bild_B.png'), dpi=110)
plt.close(fig)

fig, ax = plt.subplots(1, 3, figsize=(16, 5.2))
if c84 is not None and 'bild' in c84['schwach']:
    bb = c84['schwach']['bild']
    x = np.array(bb['x'])
    th = np.array(bb['th'])
    fr = np.array(bb['gefroren'])
    sc = ax[0].scatter(x[:, 0], x[:, 1], c=np.mod(th, 2 * np.pi), cmap='hsv', s=18, vmin=0, vmax=2 * np.pi)
    if fr.any():
        ax[0].scatter(x[fr, 0], x[fr, 1], facecolors='none', edgecolors='k', s=40)
    ax[0].set_aspect('equal')
    ax[0].set_title('2D frei, Fuellgrad 0,84, schwach: Phase (Farbe) am Ende')
    plt.colorbar(sc, ax=ax[0], fraction=0.04)
for tag, col in (('080', 'C0'), ('084', 'C1'), ('088', 'C2')):
    c = lade('C2_%s.json' % tag)
    if c is None or not c['schwach'].get('pump_probe'):
        continue
    pr = np.array(c['schwach']['pump_probe'])
    ax[1].scatter(pr[:, 0], pr[:, 1], s=3, alpha=0.4, color=col,
                  label='0,%s: r = %.3f' % (tag[1:], c['schwach'].get('pump_r') or float('nan')))
xx = np.linspace(-1, 1, 3)
ax[1].plot(xx, -np.pi / 2 * 0.01 * xx, 'k-', lw=1, label='Einzeldreieck (C0-Vorzeichen), (pi/2) eps^2')
ax[1].set_xlabel('Drehsinn chi (Takt n)')
ax[1].set_ylabel('Drehung dpsi (Takt n -> n+1), rad')
ax[1].set_title('Pumpen: Beruehrungsdreiecke 2D, schwach')
ax[1].legend(fontsize=7)
for name, col in (('kette', 'C0'), ('quadrat', 'C1'), ('dreieck', 'C2'), ('diamant', 'C3')):
    if name in A:
        s = A[name][0]
        tv = np.arange(len(s['voll']['e'])) * 10
        ax[2].plot(tv, s['voll']['e'], '-', color=col, label=name + ' voll')
        ax[2].plot(tv, s['mittel']['e'], '--', color=col, label=name + ' gemittelt')
ax[2].set_xscale('symlog', linthresh=10)
ax[2].set_xlabel('Takt')
ax[2].set_ylabel('Mittel cos(Delta) ueber Beruehrungen')
ax[2].set_title('Teil A: volle gegen gemittelte Dynamik (Saat 1)')
ax[2].legend(fontsize=7)
fig.tight_layout()
fig.savefig(os.path.join(D, 'bild_A_C.png'), dpi=110)
plt.close(fig)

print(json.dumps({k: (v.get('urteil_plan'), v.get('urteil_karte')) for k, v in out.items()
                  if isinstance(v, dict) and 'urteil_plan' in v}))
print('fehlend', out['fehlend'])
