#!/usr/bin/env python3
"""RAUTE-ATEM-1, VARIANTE [Zusatz Leitung] (eps_C = eps_D = eps/2), Anzeige (nach dem Einfrieren geschrieben, nicht Teil der Auswertung).
Liest die Zeitreihen (npz) und auswertung.json; schreibt raute-kraefte.png und faltwinkel.png.
Darstellungslauf B = 0,05, Saat 1 (mittleres B, erste Saat; vor Sicht festgelegt)."""
import json
import math
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

L = sys.argv[1]
OMEGA = 2 * math.pi
NAMEN = ['AB', 'AC', 'BC', 'AD', 'BD', 'CD']
I = [0, 0, 1, 0, 1, 2]
J = [1, 2, 2, 3, 3, 3]
B_WERTE = (0.03, 0.05, 0.08)
SERIE = ['#2a78d6', '#eb6834', '#1baf7a', '#eda100']
ZUG, DRUCK = '#e34948', '#2a78d6'
INK, INK2, MUTED, GRID = '#0b0b0b', '#52514e', '#898781', '#e1e0d9'
plt.rcParams.update({'font.size': 9, 'axes.edgecolor': '#c3c2b7', 'axes.labelcolor': INK2, 'xtick.color': MUTED,
                     'ytick.color': MUTED, 'axes.titlecolor': INK, 'figure.facecolor': '#fcfcfb',
                     'axes.facecolor': '#fcfcfb', 'savefig.facecolor': '#fcfcfb'})

with open(os.path.join(L, 'auswertung_var.json')) as f:
    A = json.load(f)


def npz(dim, B, s):
    with open(os.path.join(L, f'haupt_d{dim}_B{B:.2f}.json')) as f:
        js = json.load(f)
    r = [x for x in js['laeufe'] if x['seed'] == s][0]
    return np.load(r['npz'])


def zeichne_stabwerk(ax, x, mt, B, titel, proj3d):
    lab = 'ABCD'
    amax = max(abs(v) for v in mt) / B
    for b in range(6):
        if mt[b] == 0.0 and b == 5:
            continue
        p, q = x[I[b]], x[J[b]]
        w = 1.0 + 5.0 * abs(mt[b]) / B / max(amax, 1e-12)
        col = ZUG if mt[b] > 0 else DRUCK
        if proj3d:
            ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]], color=col, lw=w, solid_capstyle='round')
            m = p + [0.5, 0.5, 0.3, 0.7, 0.5, 0.5][b] * (q - p)
            ax.text(m[0], m[1], m[2], f'{NAMEN[b]} {mt[b] / B:+.2f}B', color=INK, fontsize=7)
        else:
            ax.plot([p[0], q[0]], [p[1], q[1]], color=col, lw=w, solid_capstyle='round')
            m = 0.5 * (p + q)
            ax.text(m[0], m[1], f'{NAMEN[b]} {mt[b] / B:+.2f}B', color=INK, fontsize=7, ha='center', va='bottom')
    for i in range(4):
        if proj3d:
            ax.scatter([x[i, 0]], [x[i, 1]], [x[i, 2]], s=60, color='#fcfcfb', edgecolor=INK, zorder=5)
            ax.text(x[i, 0], x[i, 1], x[i, 2] + 0.06, lab[i], color=INK, fontsize=10, weight='bold')
        else:
            ax.scatter([x[i, 0]], [x[i, 1]], s=60, color='#fcfcfb', edgecolor=INK, zorder=5)
            ax.text(x[i, 0] + 0.05, x[i, 1] + 0.05, lab[i], color=INK, fontsize=10, weight='bold')
    ax.set_title(titel, fontsize=9, loc='left')


fig = plt.figure(figsize=(13.5, 4.6))
# (a) 3D, FP-Fenster des Darstellungslaufs
m3 = A['laeufe']['var_haupt_d3_B0.05_s1']
d = npz(3, 0.05, 1)
if m3['fp_fenster'] is not None:
    mt = np.array([m3['stab_mittel'][n] for n in NAMEN])
    th = d['theta']
    if m3['fp_fenster'] == 'zu':
        idx = np.nonzero(d['cd'])[0]
    else:
        idx = np.nonzero(th <= math.radians(125))[0]
    x = d['x'][idx[len(idx) // 2]]
    x = x - x.mean(axis=0)
    ax = fig.add_subplot(1, 3, 1, projection='3d')
    zeichne_stabwerk(ax, x, mt, 0.05, f"3D, B = 0,05, Saat 1, Fenster '{m3['fp_fenster']}'\n"
                     f"Zeitmittel der Stabkraft (rot Zug, blau Druck)", True)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.view_init(elev=18, azim=-60)
# (b) 2D, zweite Haelfte
m2 = A['laeufe']['var_haupt_d2_B0.05_s1']
d2 = npz(2, 0.05, 1)
h = len(d2['t']) // 2
mt2 = np.array([m2['zweite_haelfte']['stab_mittel'][n] for n in NAMEN])
x2 = d2['x'][-1] - d2['x'][-1].mean(axis=0)
ax = fig.add_subplot(1, 3, 2)
zeichne_stabwerk(ax, x2, mt2, 0.05, '2D, B = 0,05, Saat 1, t = 250 bis 500\nZeitmittel der Stabkraft (rot Zug, blau Druck)',
                 False)
ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values():
    s.set_visible(False)
# (c) Mittel/B je Stab, 3D Zu-Fenster, je B (Saatenmittel), mit Statik-Soll fester Phasen
ax = fig.add_subplot(1, 3, 3)
breite = 0.26
for k, B in enumerate(B_WERTE):
    vals, errs = [], []
    for n in NAMEN:
        v = [A['laeufe'][f'var_haupt_d3_B{B:.2f}_s{s}']['stab_mittel'][n] / B for s in (1, 2, 3, 4)
             if A['laeufe'][f'var_haupt_d3_B{B:.2f}_s{s}']['fp_fenster'] is not None]
        vals.append(np.mean(v) if v else np.nan)
        errs.append(np.std(v) if v else 0.0)
    xs = np.arange(6) + (k - 1) * breite
    ax.bar(xs, vals, width=breite - 0.03, color=SERIE[k], label=f'B = {B:.2f}', yerr=errs, ecolor=INK2,
           error_kw={'lw': 0.8, 'capsize': 2})
soll = [0.5, 0.5, 0.5, 0.5, 0.5, -1.0]
ax.scatter(np.arange(6), soll, marker='_', s=300, color=INK, zorder=6, label='Statik, Kartenannahme 120 Grad')
ax.scatter(np.arange(6), [-1, 1, 1, 1, 1, -1], marker='x', s=40, color=INK2, zorder=6, label='Statik, Phasen nach A1 (A=B, C=D gegen)')
ax.axhline(0, color='#c3c2b7', lw=0.8)
ax.set_xticks(np.arange(6))
ax.set_xticklabels(['A-B\n(Scharnier)', 'A-C', 'B-C', 'A-D', 'B-D', 'C-D\n(Schluss)'])
ax.set_ylabel('Zeitmittel Stabkraft / B  (Zug +, Druck -)')
ax.set_title('3D geschlossen: Saatenmittel (Strich: Saatenstreuung)', fontsize=9, loc='left')
ax.grid(axis='y', color=GRID, lw=0.6)
ax.set_axisbelow(True)
ax.legend(fontsize=7, frameon=False, loc='lower left')
fig.tight_layout()
fig.savefig(os.path.join(L, 'var-raute-kraefte.png'), dpi=130)

# ---------------- Faltwinkel und C-D-Phasendifferenz ueber der Zeit
fig, axs = plt.subplots(3, 2, figsize=(13, 8.2), sharex=True)
for k, B in enumerate(B_WERTE):
    for s in (1, 2, 3, 4):
        d = npz(3, B, s)
        t = d['t']
        st = slice(None, None, 4)
        axs[k, 0].plot(t[st], np.degrees(d['theta'][st]), color=SERIE[s - 1], lw=1.0, label=f'Saat {s}')
        dcd = np.abs((d['phi'][:, 2] - d['phi'][:, 3] + np.pi) % (2 * np.pi) - np.pi)
        axs[k, 1].plot(t[st], np.degrees(dcd[st]), color=SERIE[s - 1], lw=1.0, label=f'Saat {s}')
    axs[k, 0].axhline(math.degrees(math.acos(1 / 3)), color=INK2, lw=0.8, ls='--')
    axs[k, 0].axhline(88.0, color=MUTED, lw=0.8, ls=':')
    axs[k, 0].axvline(200, color=MUTED, lw=0.6)
    axs[k, 0].set_ylabel(f'B = {B:.2f}\nFaltwinkel (Grad)')
    axs[k, 0].set_ylim(40, 185)
    axs[k, 1].axhline(90, color=INK2, lw=0.8, ls='--')
    axs[k, 1].set_ylabel('|Phase C - Phase D| (Grad)')
    axs[k, 1].set_ylim(-5, 185)
    for a in axs[k]:
        a.grid(color=GRID, lw=0.5)
        a.set_axisbelow(True)
axs[0, 0].set_title('Faltwinkel um A-B (180 flach; gestrichelt 70,5 = Tetraeder; punktiert ~88 = Plan-Schwelle "offen")',
                    fontsize=9, loc='left')
axs[0, 1].set_title('C-D-Phasendifferenz (gestrichelt 90: darueber stossen C und D sich ab)', fontsize=9, loc='left')
axs[0, 0].legend(fontsize=7, frameon=False, ncol=4, loc='upper right')
axs[2, 0].set_xlabel('Zeit (Takte)')
axs[2, 1].set_xlabel('Zeit (Takte)')
fig.tight_layout()
fig.savefig(os.path.join(L, 'var-faltwinkel.png'), dpi=120)
print('Bilder geschrieben')
