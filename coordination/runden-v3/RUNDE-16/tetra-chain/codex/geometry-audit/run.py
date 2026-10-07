"""Run ONLY on .69. Numerical evidence for reconstructed chains, not a proof."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import csv
import hashlib
import itertools
import json
from pathlib import Path
import resource
import socket
import time

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
import numpy as np
import scipy
from scipy.optimize import linprog

SOLVER_TOL = 1e-9
ACCEPT_TOL = 1e-7
GROUP_TOL = 1e-12
OPTIONS = dict(primal_feasibility_tolerance=SOLVER_TOL,
               dual_feasibility_tolerance=SOLVER_TOL)


def solve(c, eq, rhs, ub=None, ubrhs=None):
    r = linprog(c, A_eq=eq, b_eq=rhs, A_ub=ub, b_ub=ubrhs,
                bounds=(0, None), method='highs', options=OPTIONS)
    rec = {'status': int(r.status), 'message': r.message}
    if r.success:
        residual = max(float(np.max(np.abs(eq @ r.x - rhs))),
                       float(max(0, -np.min(r.x))))
        dual = float(rhs @ r.eqlin.marginals)
        if ub is not None:
            residual = max(residual, float(max(0, np.max(ub @ r.x - ubrhs))))
            dual += float(ubrhs @ r.ineqlin.marginals)
        rec.update(objective=float(r.fun), primal_residual=residual,
                   primal_dual_gap=float(abs(r.fun - dual)), witness=r.x.tolist())
    return r, rec


def pair(a, b, ida, idb):
    shared = sorted(set(ida) & set(idb))
    # First four variables are lambda in a; last four are mu in b.
    eq = np.zeros((5, 8))
    eq[:3, :4], eq[:3, 4:] = a.T, -b.T
    eq[3, :4], eq[4, 4:] = 1, 1
    rhs = np.array([0., 0., 0., 1., 1.])
    c = np.array([-float(i not in shared) for i in ida] + [0.] * 4)
    r, rec = solve(c, eq, rhs)
    if shared:
        verdict = ('pass_within_tolerance' if r.success and -r.fun <= ACCEPT_TOL
                   and rec['primal_residual'] <= ACCEPT_TOL
                   and rec['primal_dual_gap'] <= ACCEPT_TOL else 'fail_or_unresolved')
    else:
        verdict = 'pass_numerically_infeasible' if r.status == 2 else 'unexpected_contact_or_unresolved'
    out = dict(shared=shared, verdict=verdict, intersection_lp=rec)
    if r.success:
        # Both tetrahedra have interior intersection iff max min(lambda,mu)>0.
        ieq = np.column_stack((eq, np.zeros(5)))
        ub = np.column_stack((-np.eye(8), np.ones(8)))
        interior, irec = solve(np.array([0.] * 8 + [-1.]), ieq, rhs, ub, np.zeros(8))
        out['interior_lp'] = irec
        out['positive_volume_overlap_detected'] = bool(interior.success and -interior.fun > ACCEPT_TOL)
        if shared:
            # Any feasible x is within mass*diameter(A) of conv(shared), apart
            # from solver residuals. This is descriptive, not a rigorous bound.
            diameter = max(np.linalg.norm(x-y) for x in a for y in a)
            out['off_simplex_barycentric_mass'] = float(-r.fun)
            out['distance_proxy_mass_times_diameter'] = float(max(0, -r.fun)*diameter)
    return out


def controls():
    a = np.array([[0., 0., 0.], [1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
    b = a.copy(); b[3, 2] = -1
    cases = [
        ('identical_unrelated_ids', a, list(range(4)), list(range(4, 8)), False, True),
        ('translated_overlap', a + .1, list(range(4)), list(range(4, 8)), False, True),
        ('separated', a + 3, list(range(4)), list(range(4, 8)), True, False),
        ('shared_face', b, list(range(4)), [0, 1, 2, 4], True, False),
        ('false_face_contact', b, list(range(4)), list(range(4, 8)), False, False),
    ]
    result = []
    for name, second, ia, ib, expected_pass, expected_overlap in cases:
        row = pair(a, second, ia, ib)
        row['name'] = name
        row['control_ok'] = (row['verdict'].startswith('pass') == expected_pass and
                             row.get('positive_volume_overlap_detected', False) == expected_overlap)
        result.append(row)
    return result


def ticks(v, edges):
    # A vertex on the z axis would be hit at every t, invalidating this sweep.
    if np.any(np.linalg.norm(v[:, :2], axis=1) < GROUP_TOL):
        return [], {'ok': False, 'reason': 'vertex permanently in rotating plane'}
    events = sorted(((float((np.arctan2(y, x)+np.pi/2) % np.pi / np.pi), i)
                     for i, (x, y, _) in enumerate(v)))
    groups = []
    for t, i in events:
        if groups and t-groups[-1][-1][0] <= GROUP_TOL:
            groups[-1].append((t, i))
        else:
            groups.append([(t, i)])
    if len(groups) > 1 and groups[0][0][0]+1-groups[-1][-1][0] <= GROUP_TOL:
        groups[0] = [(t-1, i) for t, i in groups.pop()] + groups[0]
    rows = []
    for index, group in enumerate(groups):
        lo, hi = group[0][0], group[-1][0]
        prev = groups[index-1][-1][0] if index else groups[-1][-1][0]-1
        nxt = groups[index+1][0][0] if index+1 < len(groups) else groups[0][0][0]+1
        before_t, after_t = lo-(lo-prev)/4, hi+(nxt-hi)/4
        ns = np.array([[np.cos(np.pi*t), np.sin(np.pi*t), 0] for t in [before_t, after_t]])
        dots = ns @ v.T
        signs = dots > 0
        changed = set(np.flatnonzero(signs[0] != signs[1]).tolist())
        vertices = set(i for _, i in group)
        p = [sum(bool(s[a] != s[b]) for a, b in edges) for s in signs]
        boundary = [(a, b) for a, b in edges if (a in vertices) != (b in vertices)]
        d = len(boundary)
        k = sum(bool(signs[0, a] != signs[0, b]) for a, b in boundary)
        rows.append(dict(t=0.5*(lo+hi), vertices=';'.join(map(str, sorted(vertices))),
                         before_t=before_t, after_t=after_t, left_gap=lo-prev, right_gap=nxt-hi,
                         before=p[0], after=p[1], delta=p[1]-p[0], d=d, k=k,
                         expected_delta=d-2*k, changed_matches_group=changed == vertices,
                         min_sample_abs_dot=float(np.min(np.abs(dots))),
                         ok=(changed == vertices and p[1]-p[0] == d-2*k)))
    return rows, {'ok': all(r['ok'] for r in rows), 'groups': len(groups),
                  'parameterization': 'n(t)=(cos(pi*t),sin(pi*t),0); no bundle axis match claimed',
                  'group_tolerance': GROUP_TOL}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=Path(__file__).resolve().parent.parent/'RESULT.json')
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    start = time.process_time()
    raw = args.input.read_bytes()
    data = json.loads(raw)
    out = dict(status='numerical_audit_not_rigorous_proof', input_sha256=hashlib.sha256(raw).hexdigest(),
               code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               hostname=socket.gethostname(), compute='CPU float64, scipy HiGHS; no CUDA',
               numpy=np.__version__, scipy=scipy.__version__, solver_tolerance=SOLVER_TOL,
               acceptance_tolerance=ACCEPT_TOL, controls=controls(), models={},
               limitations='Only reconstructed input coordinates; infeasibility is a floating-point solver verdict. '
               'No rigorous error enclosure. Overlaps below tolerance and near-infeasible contacts cannot be excluded. '
               'Barycentric mass tolerance is dimensionless, not a certified Euclidean tolerance.')
    args.output.mkdir(parents=True, exist_ok=True)
    for label, model in data['models'].items():
        v = np.array(model['vertices'], dtype=float)
        tets = [list(range(i, i+4)) for i in range(len(v)-3)]
        edges = sorted(set(e for tet in tets for e in itertools.combinations(tet, 2)))
        rows = []
        for i, j in itertools.combinations(range(len(tets)), 2):
            row = pair(v[tets[i]], v[tets[j]], tets[i], tets[j])
            row.update(i=i, j=j)
            rows.append(row)
        determinants = [float(np.linalg.det((v[t[1:]]-v[t[0]]).T)) for t in tets]
        tr, tm = ticks(v, edges)
        if tr:
            with (args.output / f'TICKS-{label}.csv').open('w', newline='') as f:
                w = csv.DictWriter(f, fieldnames=list(tr[0])); w.writeheader(); w.writerows(tr)
        out['models'][label] = dict(vertices=len(v), tetrahedra=len(tets), pairs=rows,
            determinants=determinants, nondegenerate=all(abs(d)>ACCEPT_TOL for d in determinants),
            edges_match_input=edges == [tuple(e) for e in model['edges']],
            all_pairs_pass=all(r['verdict'].startswith('pass') for r in rows), ticks=tm)
    out['cpu_seconds'] = time.process_time()-start
    out['all_checks_pass'] = (all(c['control_ok'] for c in out['controls']) and all(
        m['nondegenerate'] and m['edges_match_input'] and m['all_pairs_pass'] and m['ticks']['ok']
        for m in out['models'].values()))
    target = args.output / 'AUDIT.json'
    tmp = target.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out, indent=2)+'\n'); tmp.replace(target)
    print(json.dumps({'output': str(target), 'all_checks_pass': out['all_checks_pass'],
                      'cpu_seconds': out['cpu_seconds']}))


if __name__ == '__main__':
    main()
