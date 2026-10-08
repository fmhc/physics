#!/usr/bin/env python3
"""Exact vertex obstruction to pure time reflection; no numerical dependencies."""
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import socket


def geometry_representatives():
    # Independently transcribed from ../maxwell/reproduce.py:geometry().
    r = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    c1, c2 = (-2, -2, -2), (4, 4, 4)
    return r + [c1, c2] + [tuple(c1[i] - p[i] for i in range(3)) for p in r]


def same_fcc_coset(p, q):
    x, y, z = (p[i] - q[i] for i in range(3))
    # Inverse of FCC translation matrix, multiplied by eight.
    return all(k % 8 == 0 for k in (-x+y+z, x-y+z, x+y-z))


def matching_sublattices(c, offsets):
    return [b for b, offset in enumerate(offsets) if (c-2*offset).denominator == 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('result.json'))
    args = parser.parse_args()
    pos8 = geometry_representatives()
    offsets = [Fraction(b, 10) for b in range(10)]
    equivalence = [[same_fcc_coset(p, q) for q in pos8] for p in pos8]
    candidates = sorted({(2*offset) % 1 for offset in offsets})
    candidate_results = [dict(c=str(c), t0_over_tau=str(c/2),
                              matching_sublattices=matching_sublattices(c, offsets))
                         for c in candidates]
    valid = [entry['c'] for entry in candidate_results
             if len(entry['matching_sublattices']) == len(offsets)]
    checks = {
        'ten_distinct_spatial_cosets': all(equivalence[i][j] == (i == j)
                                         for i in range(10) for j in range(10)),
        'five_candidate_plane_classes': len(candidates) == 5,
        'two_sublattices_per_candidate': all(len(entry['matching_sublattices']) == 2
                                             for entry in candidate_results),
        'no_pure_time_reflection': valid == [],
        'b0_b1_obstruction': ((2*offsets[1]-2*offsets[0]) % 1) == Fraction(1, 5),
        'synchronous_vertex_control': matching_sublattices(Fraction(0), [Fraction(0)]*10)
                                      == list(range(10)),
        'individual_sublattice_controls': all(b in matching_sublattices(2*offset, offsets)
                                              for b, offset in enumerate(offsets)),
        'fcc_translation_control': same_fcc_coset(pos8[0], (pos8[0][0], pos8[0][1]+4,
                                                           pos8[0][2]+4)),
    }
    root = Path(__file__).resolve().parent
    output = {
        'schema': 1, 'spatial_dimensions': 3, 'euclidean_time_dimensions': 1,
        'question': 'Pure time reflection with spatial positions fixed modulo FCC translations',
        'spatial_representatives_in_eighths': pos8,
        'temporal_offsets_over_tau': [str(o) for o in offsets],
        'spatial_coset_equivalence': equivalence,
        'candidate_planes_modulo_half_tau': candidate_results,
        'valid_c_classes': valid,
        'simplex_matching': 'not reached: vertex-set invariance is necessary and fails',
        'certificate': {'b0_requires': 'c = 0 modulo 1',
                        'b1_requires': 'c = 1/5 modulo 1',
                        'contradiction': '1/5 is not an integer'},
        'checks': checks, 'passed': all(checks.values()),
        'provenance': {'utc': datetime.now(timezone.utc).isoformat(),
                       'host': socket.gethostname(), 'python': platform.python_version(),
                       'backend': 'single-process CPU, exact integer/rational arithmetic',
                       'sha256': {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
                                  for name in ['check_reflection.py', 'PLAN.md']}},
    }
    args.output.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'passed': output['passed'], 'checks': checks,
                      'valid_c_classes': valid}))
    raise SystemExit(0 if output['passed'] else 1)


if __name__ == '__main__':
    main()
