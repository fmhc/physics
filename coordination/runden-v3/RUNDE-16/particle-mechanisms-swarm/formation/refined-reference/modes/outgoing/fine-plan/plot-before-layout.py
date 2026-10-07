#!/usr/bin/env python3
"""Saved-data figure only: no PDE, eigensolve, fit or new physics gates."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import socket
if socket.gethostname().split('.')[0] != 'ubuntu-auto':
    raise SystemExit('Remote plotting only: ubuntu-auto')
import resource
resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
import time
START = time.process_time()
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

RESULT_HASH = '2cd3dfc3b9d1d2a315daeb8be9c0661a8358c10e2879189202157708cb04ca5a'
CODE_HASH = 'ab9d00726e8f4fc6d4c7f839610d274609cf481485f6312776558cb672558e06'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--result', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if sha(args.result) != RESULT_HASH:
        raise ValueError('Saved result hash mismatch')
    result = json.loads(args.result.read_text())
    if result['status'] != 'CONTROLLED_FINE_FORCED_RESPONSE' or result['code_sha256'] != CODE_HASH:
        raise ValueError('Unexpected saved result status/code')
    ordered = []
    for h, radius in ((.05, 60.), (.05, 120.), (.025, 60.), (.025, 120.)):
        rows = [row for row in result['cases'] if row['h'] == h and row['R'] == radius]
        if len(rows) != 1 or not rows[0]['passed']:
            raise ValueError('Missing or failed saved case')
        ordered.append(rows[0])
    fine = ordered[-1]
    path = args.result.parent / fine['artifact']
    if sha(path) != fine['artifact_sha256']:
        raise ValueError('Fine saved field hash mismatch')
    with np.load(path, allow_pickle=False) as data:
        r = data['r'].copy()
        answer = data['answer_channels'].copy()
    if answer.shape != (3, len(r)) or not np.all(np.isfinite(answer)) or not np.all(np.isfinite(r)):
        raise ValueError('Invalid saved field')
    mask = (r >= 20) & (r <= 60)
    if not np.any(mask):
        raise ValueError('Empty saved outer region')
    args.out.mkdir(parents=True, exist_ok=False)
    plt.rcParams.update({'font.size': 10, 'axes.titlesize': 11})
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    ax = axes[0]
    ax.plot(r[mask], r[mask]*abs(answer[0, mask]), color='#185b86', lw=1.5,
            label='Gespeichertes Feld: R=120, h=0.025')
    for i, (lo, hi) in enumerate(((40, 45), (45, 50))):
        color = ('#df9900', '#348b58')[i]
        ax.axvspan(lo, hi, color=color, alpha=.13,
                   label=f'Auslesefenster {lo}–{hi}')
        ax.hlines(fine['windows'][i]['A_abs'], lo, hi, color=color, lw=2)
    ax.set(xlim=(20, 60), ylim=(0, None), xlabel='Radius r',
           ylabel=r'Amplitudenkoeffizient $r\,|p(r)|$', title='Außenfeld und feste Auslesefenster')
    ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useOffset=False)
    ax.legend(loc='lower right', fontsize=8)
    ax.grid(alpha=.2)
    ax = axes[1]
    values = [row['windows'][0]['A_abs'] for row in ordered]
    colors = ['#185b86', '#185b86', '#9a4735', '#9a4735']
    labels = [f"h={row['h']:g}\nR={row['R']:g}" for row in ordered]
    for i, (value, color) in enumerate(zip(values, colors)):
        ax.plot(i, value, 'o', color=color, ms=7)
        ax.annotate(f'{value:.7e}', (i, value), xytext=(0, 11),
                    textcoords='offset points', ha='center', fontsize=8)
    ax.set_xticks(range(4), labels)
    ax.set(xlim=(-.55, 3.55), ylabel=r'$|\langle r p(r)e^{ikr}\rangle_{40\ldots45}|$',
           title='Vier gespeicherte Fernamplituden (Ausschnitt der y-Achse)')
    ax.margins(y=.35)
    ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useOffset=False)
    ax.grid(axis='y', alpha=.2)
    fig.suptitle('M2: erzwungene zweite Harmonische', fontsize=15, y=.98)
    fig.text(.5, .045,
             'Norm: ||q||L² = 1. Physische Antwort = α² × Koeffizient; Leistung = α⁴ × Koeffizient.\n'
             'Stationäre Antwort auf vorgegebene Quelle; keine Lebensdauer. Status: CONTROLLED_FINE_FORCED_RESPONSE',
             ha='center', va='bottom', fontsize=9)
    fig.tight_layout(rect=(0, .16, 1, .92))
    target = args.out / 'M2-FORCED-HARMONIC.png'
    fig.savefig(target, dpi=160)
    plt.close(fig)
    receipt = dict(status='SAVED_DATA_PLOT_COMPLETE', code_sha256=sha(__file__),
                   source_result_sha256=RESULT_HASH, field_sha256=sha(path),
                   figure=target.name, figure_sha256=sha(target),
                   host=socket.gethostname(), compute='CPU saved-data plot only',
                   cpu_seconds=time.process_time()-START,
                   window=[40, 45], plotted_amplitudes=values,
                   interpretation='No new physics calculation, thresholds or lifetime estimate')
    temporary = args.out / 'RECEIPT.tmp'
    temporary.write_text(json.dumps(receipt, indent=2, allow_nan=False)+'\n')
    temporary.replace(args.out / 'RECEIPT.json')


if __name__ == '__main__':
    main()
