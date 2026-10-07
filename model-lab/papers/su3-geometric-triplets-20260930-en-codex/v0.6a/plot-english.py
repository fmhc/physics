"""Render saved shell-detuning data on .69; no fit or physics calculation."""
import json
from pathlib import Path
import platform
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

assert platform.node() == 'ubuntu-auto'
p = Path(__file__).resolve().parent
d = json.loads((p / 'FIGURE-DATA.json').read_text())
plt.rcParams.update({'font.size': 12, 'axes.spines.top': False,
                     'axes.spines.right': False, 'svg.fonttype': 'none'})
fig, axs = plt.subplots(1, 2, figsize=(9.8, 5.5), layout='constrained')
scan = d['scan']
root = d['roots'][-1]
axs[0].plot([s['A'] for s in scan], [s['Pmax'] for s in scan], 'o-',
            color='#216b91', label='Prespecified grid', markersize=4)
axs[0].scatter([root['A']], [1], s=90, marker='*', color='#d47d1f',
               zorder=5, label='Frequencies matched')
axs[0].axvline(4, color='#777', ls=':', lw=1)
axs[0].set(xlabel='Outer well depth $V_a$',
            ylabel='Maximum canonical transfer',
            title='Detuning limits transfer', ylim=(0, 1.06))
axs[0].yaxis.set_major_formatter(PercentFormatter(1))
axs[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.19),
               fontsize=11, frameon=False)
for label, col, name in [('original', '#216b91', 'Original'),
                         ('frequency_matched', '#d47d1f', 'Matched')]:
    r = next(x for x in d['runs'] if x['label'] == label and x['h'] == .0125)
    axs[1].plot(r['sample_times'], r['sample_modal_outer'], color=col,
                label=name + ': modes', lw=1.8)
    axs[1].scatter([0, r['tmax'], 2*r['tmax']],
                   [r['initial_outer_fraction'], r['outer_at_canonical_max'],
                    r['outer_at_return']], color=col, marker='x', s=55,
                   zorder=5, label=name + ': energy')
axs[1].set(xlabel='Time (model units)',
            ylabel='Canonical population (lines) /\nspatial energy fraction (crosses)',
            title='Reversible exchange', ylim=(0, 1.06))
axs[1].yaxis.set_major_formatter(PercentFormatter(1))
axs[1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.19),
               fontsize=11, ncol=2, frameon=False, columnspacing=0.9,
               handlelength=1.3)
fig.suptitle('Concentric linear control model: shell radii 6 and 10', fontsize=14)
for extension in ['png', 'svg', 'pdf']:
    fig.savefig(p / ('transfer-detuning.' + extension), dpi=180)
