#!/usr/bin/env python3
"""Two remaining free controls only; no M2 inputs or production."""
import time
START = time.process_time()
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

OUT = '75b1dce542aa728fe6bf58ecea4aec4a2ddf8a6a5a6e236666075c6902bbd292'
OP = '467ad3e19cd8efcdac4ec2dcc670b50aaa59cc6f7e9e44d625ebbf94ba0d32c6'
OLD = '9f0b975784c3b5111fc95ae804db89b33cbbca750637ff2161c084c211a55e9f'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path, digest, name):
    if sha(path) != digest:
        raise ValueError('Module provenance mismatch')
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time() - START >= 2.5:
        raise RuntimeError('INCOMPLETE: 2.5 CPU-s checkpoint')


def save(directory, result):
    result['cpu_seconds'] = time.process_time() - START
    tmp = directory / 'RESULT.tmp'
    tmp.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    tmp.replace(directory / 'RESULT.json')


def main():
    parser = argparse.ArgumentParser()
    for name in ('outgoing', 'operator', 'previous', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    result = dict(status='INCOMPLETE', cases=[], code_sha256=sha(__file__),
                  outgoing_sha256=OUT, operator_sha256=OP, previous_sha256=OLD,
                  interpretation='Two free h=.05 controls only; original coarse FAIL unchanged; no M2 authorization')
    save(args.out, result)
    try:
        if sha(args.previous) != OLD:
            raise ValueError('Previous result provenance mismatch')
        previous = json.loads(args.previous.read_text())
        result['original_status_unchanged'] = previous['status']
        out = module(args.outgoing, OUT, 'unchanged_outgoing')
        op = module(args.operator, OP, 'unchanged_modes_grid')
        grid = op.grid(30., .05)
        r = grid['r']
        zero = np.zeros(grid['n'])
        one = np.ones(grid['n'])
        gaussian = np.exp(-r*r/4)
        for kind in ('closed', 'wrong_robin'):
            checkpoint()
            source = np.zeros((3, grid['n']), dtype=complex)
            source[2 if kind == 'closed' else 0] = gaussian
            row, answer, _ = out.solve(grid, zero, one, .8, 1., source,
                                       ((15, 20), (20, 25)), incoming=kind == 'wrong_robin')
            row.update(kind=kind, h=.05, R=30.)
            flags = dict(row['algebra_flags'])
            if kind == 'closed':
                row['open_closed_norm_ratio'] = out.quotient(out.norm(grid, answer[0]), out.norm(grid, answer[2]))
                row['closed_rot_flux_ratio'] = out.quotient(abs(row['FV_rot_flux']), row['work_scale'])
                flags.update(open_zero=out.below(row['open_closed_norm_ratio'], 1e-12),
                             closed_zero=out.below(row['closed_rot_flux_ratio'], 1e-12))
            else:
                flags['negative_flux'] = row['FV_rot_flux'] < 0
            row['flags'] = flags
            row['passed'] = all(flags.values())
            filename = kind + '-h0.05.npz'
            np.savez_compressed(args.out / filename, r=r, answer_channels=answer,
                                source_channels=source, omega=.8, nu=1.)
            row['artifact'] = filename
            row['artifact_sha256'] = sha(args.out / filename)
            result['cases'].append(row)
            save(args.out, result)
            if not row['passed']:
                raise ValueError('Remaining free control failed: ' + kind)
        checkpoint()
        result['status'] = 'REMAINING_FREE_CONTROLS_PASSED_H005'
    except Exception as exc:
        result['error'] = repr(exc)
        result['status'] = 'INCOMPLETE' if isinstance(exc, RuntimeError) else 'UNRESOLVED'
    save(args.out, result)
    return 0 if result['status'] == 'REMAINING_FREE_CONTROLS_PASSED_H005' else 2


if __name__ == '__main__':
    raise SystemExit(main())
