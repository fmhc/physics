"""Explanatory overview figure (v0.52): Q-ball, balance of terms, channels, cancellation ladder.

Plots stored data and formulas already in the paper; no new physics computation.
Inputs (sha256 in INPUTS-FIG.sha256): inputs/PROFILE.json, inputs/figure-data.json,
inputs/sprossen.json. Gates G1-G6 from the pre-registration note (not published); any FAIL raises before rendering.
Run on the author's workstation, CPU, single core.
"""
import json, hashlib, platform, sys, datetime
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyArrowPatch, Circle
from scipy.interpolate import PchipInterpolator

here = Path(__file__).resolve().parent
inp = here / 'inputs'
out = here / 'out'
out.mkdir(exist_ok=True)

C0_W2 = 0.797676787111865191750
C0_RHO = 1.744617544837398735781
C1_W2 = 0.6851289044582160933
C1_RHO = 1.6903565973281434568
C2_W2 = 0.7544960137826372331
C2_RHO = 1.826342030181069956
BETA = 0.5

prof = json.loads((inp / 'PROFILE.json').read_text())
fdat = json.loads((inp / 'figure-data.json').read_text())
spr = json.loads((inp / 'sprossen.json').read_text())

r = np.array(prof['r'])
st = {s['name']: s for s in prof['stellen']}

ladder = {}
for n, x in zip(fdat['n'], fdat['x']):
    if n <= 14:
        ladder[n] = (x, 'figure-data.json:x[%d]' % (n - 1))
ladder[15] = (spr['pb0']['je_sprosse'][0]['omega2_h002'], 'sprossen.json:pb0.je_sprosse[0].omega2_h002')
for s in spr['sprossen']:
    if s['beta'] == 0.5 and s['index'] in (16, 17, 18):
        ladder[s['index']] = (s['omega2'], 'sprossen.json:sprossen[index=%d].omega2' % s['index'])

classes = {}
for n in (1, 2):
    classes[n] = 'certified'
for n in (3, 4, 6, 7, 8, 9, 10, 15):
    classes[n] = 'winding'
for n in (5, 11, 12, 13, 14):
    classes[n] = 'weaker'
for n in (16, 17, 18):
    classes[n] = 'failed'

gates = {}
def gate(name, ok, detail):
    gates[name] = {'pass': bool(ok), 'detail': detail}
    if not ok:
        raise SystemExit('GATE FAIL %s: %s' % (name, detail))

g1 = sorted(ladder) == list(range(1, 19)) and all(0.5 < ladder[n][0] < 0.8 for n in ladder)
g1 = g1 and abs(ladder[1][0] - fdat['x'][0]) < 1e-12 and abs(ladder[15][0] - 0.5284693357421102) < 1e-12
g1 = g1 and abs(ladder[16][0] - 0.5267154164259079) < 1e-12 and abs(ladder[18][0] - 0.5237874658867491) < 1e-12
gate('G1', g1, {str(n): ladder[n] for n in sorted(ladder)})
n_unc = sum(1 for n in classes if classes[n] != 'certified')
gate('G2', n_unc == 16 and sum(1 for n in classes if classes[n] == 'certified') == 2,
     {'uncertified_radial': n_unc, 'certified_radial': 2, 'certified_dipole': 1})

import re
seq = (inp / 'SEQUENCE-v051.tex').read_text()
rows = re.findall(r'^(\d+)&\$([^$]*)\$&(.*?)\\\\', seq, re.M)
g1b = {}
g2b = {}
for nstr, val, ev in rows:
    n = int(nstr)
    num = re.search(r'0\.(\d+)', val)
    shown = float(num.group(0)); unit = 10.0 ** (-len(num.group(1)))
    g1b[n] = {'table': num.group(0), 'plotted': ladder[n][0], 'diff': abs(ladder[n][0] - shown), 'tol': unit,
              'pass': abs(ladder[n][0] - shown) <= unit}
    if 'Existence enclosure' in ev:
        cl = 'certified'
    elif 'rule failed' in ev or 'phase unresolved' in ev:
        cl = 'failed'
    elif 'Linewidth reconstruction' in ev or 'Sign change' in ev:
        cl = 'weaker'
    elif re.search(r'resolved (numerical )?winding', ev.lower()):
        cl = 'winding'
    else:
        cl = 'unmapped:' + ev
    g2b[n] = {'table_text': ev.strip(), 'class_from_table': cl, 'plotted_class': classes[n], 'pass': cl == classes[n]}
gate('G1b', sorted(g1b) == list(range(1, 19)) and all(v['pass'] for v in g1b.values()), g1b)
gate('G2b', sorted(g2b) == list(range(1, 19)) and all(v['pass'] for v in g2b.values()), g2b)
proof = (inp / 'PROOF-v051.tex').read_text()
cases_tab = re.findall(r'(C[012]) & (\d) & \$([0-9.]+)\\pm[^$]*\$\s*& \$([0-9.]+)\\pm', proof)
consts = {'C0': (C0_W2, C0_RHO), 'C1': (C1_W2, C1_RHO), 'C2': (C2_W2, C2_RHO)}
g7 = {c: {'table_w2': w2s, 'table_rho': rhos, 'pass': float(w2s) == consts[c][0] and float(rhos) == consts[c][1]}
      for c, l, w2s, rhos in cases_tab}
gate('G7', sorted(g7) == ['C0', 'C1', 'C2'] and all(v['pass'] for v in g7.values()), g7)
c0 = st['l0n1']
gate('G3', abs(c0['omega2'] - C0_W2) < 1e-15 and c0['f0'] > 0, {'profile_omega2': c0['omega2'], 'f0': c0['f0']})
w0 = np.sqrt(C0_W2)
gate('G4', (w0 + C0_RHO) > 1 and abs(w0 - C0_RHO) < 1, {'omega_plus_rho': w0 + C0_RHO, 'omega_minus_rho': w0 - C0_RHO})

def U(S):
    return S - S**2 + BETA * S**3

def Vmech(f, w2):
    return 0.5 * (w2 * f**2 - U(f**2))

gate('G5', abs(Vmech(0.0, 0.5)) < 1e-12 and abs(Vmech(1.0, 0.5)) < 1e-12,
     {'V(0)': Vmech(0.0, 0.5), 'V(1)': Vmech(1.0, 0.5)})

OI = {'orange': '#E69F00', 'sky': '#56B4E9', 'green': '#009E73', 'blue': '#0072B2',
      'verm': '#D55E00', 'purple': '#CC79A7', 'black': '#000000', 'grey': '#7F7F7F'}

plt.rcParams.update({'font.size': 8.6, 'axes.titlesize': 9.2, 'axes.labelsize': 8.8,
                     'legend.fontsize': 7.8, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
                     'pdf.fonttype': 42, 'svg.fonttype': 'none'})
fig = plt.figure(figsize=(6.5, 8.0))
gs = GridSpec(3, 2, figure=fig, height_ratios=[1.0, 1.0, 0.86], hspace=0.60, wspace=0.31,
              left=0.095, right=0.98, top=0.958, bottom=0.135)

ax = fig.add_subplot(gs[0, 0])
cols = {'l0n1': OI['verm'], 'l0n2': OI['blue'], 'l0n3': OI['green']}
lss = {'l0n1': '-', 'l0n2': '-.', 'l0n3': (0, (1, 1.2))}
labs = {'l0n1': r'C0 ($\omega^2=0.798$)', 'l0n2': r'C1 ($0.685$)',
        'l0n3': r'$n=3$ ($0.631$)'}
for name in ('l0n1', 'l0n2', 'l0n3'):
    ax.plot(r, np.array(st[name]['S']), color=cols[name], lw=1.6, ls=lss[name], label=labs[name])
eps14 = ladder[14][0] - 0.5
Rtw = 1.0 / (2.0 * np.sqrt(BETA) * eps14)
Stw = (1.0 / (2 * BETA)) / (1.0 + np.exp((r - Rtw) / np.sqrt(BETA)))
ax.plot(r, Stw, color=OI['black'], lw=1.3, ls='--', label=r'thin wall, $n=14$')
ax.set_xlim(0, 31); ax.set_ylim(0, 1.36)
ax.set_xlabel(r'radius $r$ (model units)')
ax.set_ylabel(r'charge density $\propto S=|\phi|^2=f^2$')
ax.set_title('(a) A Q-ball: a lump of rotating field', loc='left')
ax.legend(loc='lower left', bbox_to_anchor=(0.215, 0.025), frameon=True, framealpha=0.95,
          handlelength=1.6, borderpad=0.35, fontsize=7.7, labelspacing=0.3)
ax.text(12.5, 0.89, 'core', ha='center', fontsize=7.8)
ax.annotate('wall', xy=(Rtw - 0.3, 0.70), xytext=(17.5, 0.75), fontsize=7.6, ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color='0.3', lw=0.8))
ax.text(28.0, 0.06, 'vacuum', ha='center', fontsize=7.6, color='0.25')
ax.text(15.0, 1.19, 'internal phase $e^{i\\omega t}$ turns;\n$|\\phi|^2$ stays static (schematic)', ha='center',
        va='center', fontsize=7.7, linespacing=1.1)
ins = ax.inset_axes([0.79, 0.73, 0.20, 0.26])
ins.set_aspect('equal'); ins.axis('off')
ins.add_patch(Circle((0, 0), 1.0, fill=False, ls=':', color='0.4', lw=0.9))
for ang, a in ((0.25 * np.pi, 1.0), (0.85 * np.pi, 0.35), (1.45 * np.pi, 0.35)):
    ins.annotate('', xy=(np.cos(ang) * 0.95, np.sin(ang) * 0.95), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='-|>', color=OI['verm'], lw=1.2, alpha=a))
ins.add_patch(FancyArrowPatch((1.18, -0.25), (0.25, 1.18), connectionstyle='arc3,rad=0.45',
                              arrowstyle='-|>', mutation_scale=7, color='0.2', lw=0.8))
ins.set_xlim(-1.35, 1.45); ins.set_ylim(-1.35, 1.45)

ax = fig.add_subplot(gs[0, 1])
f = np.linspace(0, 1.32, 600)
curves = [(C0_W2, OI['verm'], '-', r'C0: $\omega^2=0.798$'), (C1_W2, OI['blue'], '-.', r'C1: $\omega^2=0.685$'),
          (0.5, OI['black'], '--', r'$\omega^2=\omega_c^2=1/2$ (thin-wall limit)')]
for w2, c, ls, lab in curves:
    ax.plot(f, Vmech(f, w2), color=c, ls=ls, lw=1.5, label=lab)
for name, w2, c in (('l0n1', C0_W2, OI['verm']), ('l0n2', C1_W2, OI['blue'])):
    f0 = st[name]['f0']
    ax.plot([f0], [Vmech(f0, w2)], 'o', color=c, ms=5, mec='k', mew=0.5, zorder=5)
f0 = st['l0n1']['f0']
fpath = np.linspace(f0 - 0.02, 0.05, 200)
ax.plot(fpath, Vmech(fpath, C0_W2) + 0.022, color=OI['verm'], lw=1.0, ls=(0, (1.5, 1.5)))
ax.annotate('', xy=(0.03, Vmech(0.03, C0_W2) + 0.022), xytext=(0.07, Vmech(0.07, C0_W2) + 0.022),
            arrowprops=dict(arrowstyle='-|>', color=OI['verm'], lw=0.9, mutation_scale=9))
ax.text(0.43, -0.142, 'the "particle" starts at rest\nat $f(0)$ (dot), rolls to $f=0$\n'
        'as $r\\to\\infty$; the damping $(2/r)\\,f\'$\nremoves the height difference',
        fontsize=7.7, ha='center', va='center', linespacing=1.1)
ax.axhline(0, color='0.6', lw=0.7)
ax.set_xlim(0, 1.32); ax.set_ylim(-0.24, 0.37)
ax.set_xlabel(r'field amplitude $f$ (position of the "particle")')
ax.set_ylabel(r'$V(f)=\frac{1}{2}[\omega^2f^2-\mathcal{U}(f^2)]$')
ax.set_title('(b) Balance: Coleman\'s rolling particle', loc='left')
ax.legend(loc='upper left', frameon=True, framealpha=0.95, handlelength=1.6, fontsize=7.4, labelspacing=0.25, borderpad=0.3)

ax = fig.add_subplot(gs[1, 0])
cases = [('C0', C0_W2, C0_RHO), ('C1', C1_W2, C1_RHO), ('C2', C2_W2, C2_RHO)]
ax.axhspan(1, 3.2, color=OI['orange'], alpha=0.13, lw=0)
ax.axhspan(-3.2, -1, color=OI['orange'], alpha=0.13, lw=0)
ax.axhspan(-1, 1, color=OI['sky'], alpha=0.13, lw=0)
ax.axhline(1, color='0.4', lw=0.8, ls=':'); ax.axhline(-1, color='0.4', lw=0.8, ls=':')
deriv = {}
for i, (nm, w2, rho) in enumerate(cases):
    w = np.sqrt(w2); x0 = i
    deriv[nm] = {'omega': w, 'omega_plus_rho': w + rho, 'omega_minus_rho': w - rho}
    ax.plot([x0 - 0.28, x0 + 0.28], [w, w], color=OI['black'], lw=2.0)
    ax.plot([x0 - 0.28, x0 + 0.28], [w + rho, w + rho], color=OI['orange'], lw=2.4)
    ax.plot([x0 - 0.28, x0 + 0.28], [w - rho, w - rho], color=OI['blue'], lw=2.4)
    ax.annotate('', xy=(x0 + 0.17, w + rho), xytext=(x0 + 0.17, w),
                arrowprops=dict(arrowstyle='->', color='0.35', lw=0.8))
    ax.annotate('', xy=(x0 - 0.17, w - rho), xytext=(x0 - 0.17, w),
                arrowprops=dict(arrowstyle='->', color='0.35', lw=0.8))
ax.text(2.42, 2.62, r'$\omega+\rho$: open' + '\n(propagates,\ncan radiate)', color='#8a5a00', ha='left',
        va='center', fontsize=7.7)
ax.text(2.42, 0.86, r'carrier $\omega$', ha='left', va='center', fontsize=7.7)
ax.text(2.42, -0.40, r'$\omega-\rho$: closed' + '\n(evanescent,\ntrapped)', color=OI['blue'], ha='left',
        va='center', fontsize=7.7)
ax.text(1.62, -1.42, r'orange: free waves, $|E|>1$; blue: gap, $|E|<1$', fontsize=7.2,
        ha='center', va='center', color='0.2')
ax.set_xticks([0, 1, 2]); ax.set_xticklabels([r'C0 ($\ell=0$)', r'C1 ($\ell=0$)', r'C2 ($\ell=1$)'])
ax.set_xlim(-0.45, 3.7); ax.set_ylim(-1.8, 3.2)
ax.set_ylabel(r'lab frequency $E$ (units of the mass)')
ax.set_title('(c) The two sidebands of an excitation', loc='left')

ax = fig.add_subplot(gs[1, 1])
A = np.array(c0['A']); B = np.array(c0['B'])
m = r <= 16
ax.plot(r[m], B[m], color=OI['blue'], lw=1.7, label=r'$B(r)$, closed channel')
ax.plot(r[m], 5 * A[m], color=OI['orange'], lw=1.7, ls='-.', label=r'$5\times A(r)$, open channel at C0')
rs = np.linspace(0, 16, 800)
on = 0.5 * (1 + np.tanh((rs - 5.0) / 1.0))
generic = 0.16 * on * np.sin(c0['k_offen'] * rs)
ax.plot(rs, generic, color='0.45', lw=1.0, ls='--', label='schematic: generic outgoing wave\n(constant reduced amplitude)')
ax.axhline(0, color='0.6', lw=0.7)
ax.set_xlim(0, 16); ax.set_ylim(-0.45, 1.28)
ax.set_xlabel(r'radius $r$ (model units)')
ax.set_ylabel('reduced radial amplitude')
ax.set_title('(d) At C0 the open-channel tail cancels', loc='left')
ax.legend(loc='upper right', frameon=True, framealpha=0.95, handlelength=1.6, fontsize=7.7, labelspacing=0.3)
ax.text(8.0, -0.36, 'numerical reconstruction, not an enclosure', fontsize=7.7, ha='center',
        color='0.25')
ax.set_xticks([0, 4, 8, 12, 16])

ax = fig.add_subplot(gs[2, :])
ns = np.arange(1, 19)
xs = np.array([1.0 / (ladder[n][0] - 0.5) for n in ns])
pch = PchipInterpolator(xs, ns.astype(float), extrapolate=True)
xx = np.linspace(xs[0] - 1.2, xs[-1] + 1.1, 4000)
ax.plot(xx, np.sin(np.pi * pch(xx))**2, color='0.55', lw=1.0, zorder=1,
        label='schematic width, dips at reported locations')
sty = {'certified': dict(marker='s', mfc=OI['verm'], mec='k', ms=7.0, ls='none', label='computer-assisted proof (C0, C1)'),
       'winding': dict(marker='o', mfc='white', mec=OI['blue'], mew=1.4, ms=6.0, ls='none', label='candidate: resolved numerical winding'),
       'weaker': dict(marker='^', mfc='white', mec=OI['green'], mew=1.4, ms=6.5, ls='none', label='candidate: sign change or width minimum'),
       'failed': dict(marker='x', color=OI['purple'], mew=1.6, ms=6.5, ls='none', label='candidate: final acceptance rule failed')}
for cl in ('certified', 'winding', 'weaker', 'failed'):
    sel = [i for i, n in enumerate(ns) if classes[n] == cl]
    ax.plot(xs[sel], np.zeros(len(sel)), zorder=4, clip_on=False, **sty[cl])
xc2 = 1.0 / (C2_W2 - 0.5)
ax.plot([xc2], [-0.42], marker='D', mfc=OI['verm'], mec='k', ms=6.5, ls='none', clip_on=False, zorder=4,
        label=r'computer-assisted proof, dipole $\ell=1$ (C2)')
ax.text(xc2 + 0.7, -0.42, r'C2 (separate $\ell=1$ channel)', va='center', fontsize=7.8)
ax.text(xs[0], 0.10, 'C0', ha='center', fontsize=7.8); ax.text(xs[1], 0.10, 'C1', ha='center', fontsize=7.8)
for n in (5, 10, 15, 18):
    ax.text(xs[n - 1], 0.10, '%d' % n, ha='center', fontsize=7.7, color='0.25')
ax.annotate('', xy=(xs[14], 1.13), xytext=(xs[13], 1.13), arrowprops=dict(arrowstyle='<->', color='0.2', lw=0.8))
ax.text(0.5 * (xs[13] + xs[14]), 1.19, 'step %.2f' % (xs[14] - xs[13]), ha='center', fontsize=7.8)
ax.text(43.8, 0.55, 'not computed\nbeyond $n=18$;\nno infinite\nladder claimed', fontsize=7.7, ha='left', va='center', color='0.25')
ax.set_xlim(1.4, 52.5); ax.set_ylim(-0.62, 1.36)
ax.set_yticks([0, 1]); ax.set_yticklabels(['0', 'max'])
ax.set_xlabel(r'inverse detuning $1/(\omega^2-1/2)$ $\;$(larger: bigger Q-ball, wall thinner relative to radius)')
ax.set_ylabel('width')
ax.set_title(r'(e) Proved cancellations and numerical candidates, $\ell=0$ sequence ($n=1$–$18$)', loc='left')
top = ax.secondary_xaxis('top', functions=(lambda x: 0.5 + 1.0 / np.maximum(x, 1e-9),
                                           lambda w: 1.0 / np.maximum(w - 0.5, 1e-9)))
top.set_xticks([0.7, 0.6, 0.55, 0.53, 0.525])
top.set_xticklabels(['0.7', '0.6', '0.55', '0.53', '0.525'])
top.set_xlabel(r'$\omega^2$', labelpad=1)
top.tick_params(labelsize=7.4)
h, l = ax.get_legend_handles_labels()
fig.legend(h, l, loc='lower center', bbox_to_anchor=(0.53, 0.0), ncol=2, frameon=False,
           handlelength=1.4, columnspacing=1.2, fontsize=7.7)

stem = 'qball-overview'
fig.savefig(out / (stem + '.pdf'))
fig.savefig(out / (stem + '.png'), dpi=200)
fig.savefig(out / (stem + '.svg'))

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

outs = {p.name: sha(p) for p in sorted(out.glob(stem + '.*'))}
gate('G6', len(outs) == 3, outs)
receipt = {
    'time': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
    'host': platform.node(), 'python': sys.version.split()[0], 'matplotlib': matplotlib.__version__,
    'numpy': np.__version__, 'script_sha256': sha(__file__),
    'inputs_sha256': {p.name: sha(p) for p in sorted(inp.glob('*'))},
    'outputs_sha256': outs, 'gates': gates,
    'derived_values': {'sidebands': deriv,
                       'inverse_detuning': {str(n): float(x) for n, x in zip(ns, xs)},
                       'inverse_detuning_C2': xc2, 'thinwall_R_n14': Rtw,
                       'step_14_15': float(xs[14] - xs[13])},
    'ladder_sources': {str(n): ladder[n][1] for n in sorted(ladder)},
    'evidence_classes': {str(n): classes[n] for n in sorted(classes)},
    'schematic_elements': ['panel (a) phase-rotation inset', 'panel (d) generic open-channel tail (amplitude 0.16, onset r=5, wavenumber k of C0)',
                           'panel (e) width curve sin^2(pi N(x)), N = PCHIP through (x_n, n); reported locations are data (candidates for n=3-18); the schematic zero depth is not established for n=3-18'],
}
(out / 'FIG-OVERVIEW-RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'gates': {k: v['pass'] for k, v in gates.items()}, 'outputs': outs, 'step_14_15': receipt['derived_values']['step_14_15']}))
