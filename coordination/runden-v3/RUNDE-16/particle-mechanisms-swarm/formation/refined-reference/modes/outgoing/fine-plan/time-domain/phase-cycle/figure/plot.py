#!/usr/bin/env python3
"""Saved-data illustration only; no evolution, fitting or new gate evaluation."""
import argparse
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

PHASE_SHA = 'b7d938e4bda00bb05598f540f05320b2e3cad7a8a8f3f4be940a9d5884b8eafd'
CAUSAL_SHA = '15593347f6b1caff683315fab65ce74734ae85fb5eff97b8a25d9276c0a568b9'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def read_result(directory, expected):
    path = directory / 'RESULT.json'
    require(digest(path) == expected, f'Result hash mismatch: {path}')
    return json.loads(path.read_text())


def one(rows):
    require(len(rows) == 1, 'Missing or ambiguous selected row')
    return rows[0]


def load_ring(directory, entry):
    require(Path(entry['file']).name == entry['file'], 'Artifact must be a basename')
    path = directory / entry['file']
    require(digest(path) == entry['sha256'], f'Artifact hash mismatch: {path}')
    with np.load(path, allow_pickle=False) as data:
        t, r = data['t'].copy(), data['r'].copy()
        fields = data['rotating_fields_by_source'].copy()
        require(data['sources'].tolist() == ['DC', 'H2'], 'Source order mismatch')
    require(t.ndim == r.ndim == 1 and fields.shape == (len(t), 2, 4, len(r)),
            'Unexpected ring shape')
    require(np.all(np.diff(t) > 0) and np.all(np.diff(r) > 0), 'Nonmonotone axes')
    require(np.all(np.isfinite(t)) and np.all(np.isfinite(r))
            and np.all(np.isfinite(fields)), 'Nonfinite data')
    return t, r, fields


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase-dir', type=Path, required=True)
    parser.add_argument('--causal-dir', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    phase = read_result(args.phase_dir, PHASE_SHA)
    causal = read_result(args.causal_dir, CAUSAL_SHA)
    require(phase['status'] == 'CONTROLLED_PHASE_CYCLE_CAUSAL_COMPONENTS'
            and phase['terminal_complete'], 'Phase-cycle result incomplete')
    require(causal['status'] == 'CAUSAL_SPLIT_DIAGNOSIS_COMPLETE', 'Wrong causal result')
    require(phase['saved_inputs']['split_sha256'] == CAUSAL_SHA, 'Broken input linkage')
    pair = one([x for x in phase['pairs'] if x['level'] == 'time'])
    run = one([x for x in causal['runs'] if x['dt'] == .01])
    require(pair['complete'] and pair['dt'] == .005 and run['complete'], 'Incomplete selected pair')
    pt, pr, pf = load_ring(args.phase_dir, pair['separated_artifact'])
    ct, cr, cf = load_ring(args.causal_dir, run['ring_artifact'])
    require(np.array_equal(pt, ct) and np.array_equal(pr, cr), 'Ring coordinates differ')
    index = int(np.argmin(abs(pr - 42.5)))
    radius = float(pr[index])
    require(40 <= radius < 45, 'Selected cell outside intended shell')
    mask = (pt >= 88) & (pt <= 121)
    require(np.count_nonzero(mask) > 2, 'Missing illustration interval')
    # The arrays already contain the coefficient of alpha^2. No re-scaling,
    # phase anchoring, interpolation, smoothing or reference fitting follows.
    fig, axes = plt.subplots(2, 1, figsize=(10.6, 8.4), sharex=True)
    fig.subplots_adjust(top=.86, bottom=.23, left=.12, right=.97, hspace=.31)
    for ci, (ax, name) in enumerate(zip(axes, ('DC-Quellgeschichte', 'H2-Quellgeschichte'))):
        ax.plot(pt[mask], pf[mask, ci, 0, index].real, color='#176b98', lw=2.2,
                label='Phasenzyklus, dt = 0.005')
        ax.plot(ct[mask], cf[mask, ci, 0, index].real, color='#d27020', lw=1.7,
                ls='--', label='Kausale Referenz, dt = 0.01')
        ax.set_title(name, loc='left', fontsize=12)
        ax.set_ylabel(r'Re($\phi^{(2)}$)')
        ax.grid(alpha=.24)
        ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
        ax.legend(loc='best', fontsize=9, framealpha=.95)
    axes[-1].set_xlabel('Zeit t')
    axes[-1].set_xlim(88, 121)
    fig.suptitle('M2: Phasenzyklus der kausalen zweiten Ordnung', fontsize=16, y=.97)
    fig.text(.5, .917, f'Skalierte Antwort: physischer Beitrag alpha² · phi⁽²⁾ | '
             f'r = {radius:.6f}, h = 0.05, R = 120', ha='center', fontsize=10)

    # Only summarize stored, already evaluated gate numbers. The point curve
    # above is not assigned a new error threshold or a new integration window.
    summary = []
    for component in ('DC', 'H2'):
        rows = [x for x in phase['measurements']
                if x['component'] == component and x['level'] == 'time']
        require(len(rows) == 4 and all(all(x['flags'].values()) for x in rows),
                'Unexpected saved component gates')
        summary.append(f"{component}: Zeit {max(x['errors']['time'] for x in rows):.6f}, "
                       f"Band {max(x['errors']['band'] for x in rows):.6f}")
    require(len(phase['dt_comparisons']) == 8
            and all(all(x['flags'].values()) for x in phase['dt_comparisons']),
            'Unexpected saved dt gates')
    text = ('Gespeicherte Schalen-Gates, maximale relative Fehler (dt = 0.005):\n'
            + '   |   '.join(summary)
            + '\nKomponenten-Grenze 0.05; alle 8 dt-Vergleiche < 0.01; Nennerreserven bestanden.'
            + '\nOrtskurven sind illustrativ. Gates: Volumennormen in r = 40–45 / 45–50,'
            + '\nZeitfenster 88–104.4373 / 104.5–120.9373; Band bei +2rho.'
            + '\nKein BIC- oder Stabilitätsnachweis; keine stationäre Strahlungs- oder Lebensdaueraussage.')
    fig.text(.12, .177, text, va='top', fontsize=9, linespacing=1.55)
    args.out.mkdir(parents=True, exist_ok=True)
    for suffix in ('png', 'svg'):
        fig.savefig(args.out / f'M2-phase-cycle.{suffix}', dpi=180,
                    metadata={'Description': 'Saved-data illustration; no new gate evaluation'})
    plt.close(fig)
    provenance = dict(plot_code_sha256=digest(Path(__file__)), phase_result_sha256=PHASE_SHA,
                      causal_result_sha256=CAUSAL_SHA,
                      phase_artifact=pair['separated_artifact'], causal_artifact=run['ring_artifact'],
                      selected_radius=radius, selected_cell_index=index,
                      displayed_time=[float(pt[mask][0]), float(pt[mask][-1])],
                      component='phi', scaling='coefficient of alpha squared, already stored',
                      new_gate_evaluation=False)
    (args.out / 'PROVENANCE.json').write_text(json.dumps(provenance, indent=2) + '\n')


if __name__ == '__main__':
    main()
