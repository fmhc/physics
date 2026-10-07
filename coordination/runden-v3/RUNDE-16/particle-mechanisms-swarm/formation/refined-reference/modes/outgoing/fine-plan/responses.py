#!/usr/bin/env python3
"""Fixed fine-grid forced responses; no preparation, eigensolve or evolution."""
import time
START = time.process_time()
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

OUT_HASH = '75b1dce542aa728fe6bf58ecea4aec4a2ddf8a6a5a6e236666075c6902bbd292'
OP_HASH = '467ad3e19cd8efcdac4ec2dcc670b50aaa59cc6f7e9e44d625ebbf94ba0d32c6'
NULL_HASH = '06403a8a39de37c8f9eeac872173c4f22e210f3254894d3741383759b889e600'
FREE_HASH = '4b5184197e81e203998cd2fe7430cf45aa2bec8438ef20f66ff512550792a64d'
CASES = ((60., .05), (120., .05), (60., .025), (120., .025))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path, digest, name):
    if sha(path) != digest:
        raise ValueError('Module hash mismatch')
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time() - START >= 6:
        raise RuntimeError('INCOMPLETE: 6 CPU-s checkpoint')


def save(directory, result):
    result['cpu_seconds'] = time.process_time() - START
    tmp = directory / 'RESULT.tmp'
    tmp.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    tmp.replace(directory / 'RESULT.json')


def read_json(path, expected):
    if sha(path) != expected:
        raise ValueError('Result provenance mismatch: ' + str(path))
    return json.loads(path.read_text())


def artifact(directory, row):
    path = directory / row['artifact']
    if sha(path) != row['artifact_sha256']:
        raise ValueError('Artifact hash mismatch')
    return path


def archived_qa(null_path, free_path, out):
    old = read_json(null_path, NULL_HASH)
    free = read_json(free_path, FREE_HASH)
    if old['status'] != 'DIAGNOSTIC_COMPLETE' or free['status'] != 'REMAINING_FREE_CONTROLS_PASSED_H005':
        raise ValueError('Archived control status mismatch')
    selected = []
    nullrows = []
    for h in (.05, .025):
        for kind in ('gaussian', 'null_bump'):
            rows = [r for r in old['cases'] if r['h'] == h and r['kind'] == kind]
            if len(rows) != 1 or not rows[0]['original_QA_passed'] or not all(rows[0]['original_QA_flags'].values()):
                raise ValueError('Missing or failed archived fine control')
            row = rows[0]
            artifact(null_path.parent, row)
            selected.append(dict(source_sha256=NULL_HASH, case=row))
            if kind == 'null_bump':
                nullrows.append(row)
    gaussian = [r for r in old['cases'] if r['h'] == .05 and r['kind'] == 'gaussian'][0]['analytic_A']
    ratio = out.quotient(nullrows[0]['null_amplitude'], nullrows[1]['null_amplitude'])
    below_floor = all(r['null_amplitude'] < 1e-10 * gaussian for r in nullrows)
    if not (below_floor or (ratio is not None and 2 < ratio < 6)):
        raise ValueError('Archived fine null amplitude reduction failed')
    for kind in ('closed', 'wrong_robin'):
        rows = [r for r in free['cases'] if r['h'] == .05 and r['kind'] == kind]
        if len(rows) != 1 or not rows[0]['passed'] or not all(rows[0]['flags'].values()):
            raise ValueError('Missing or failed archived remaining control')
        artifact(free_path.parent, rows[0])
        selected.append(dict(source_sha256=FREE_HASH, case=rows[0]))
    return dict(reused=selected, fine_null_ratio=ratio, below_original_floor=below_floor,
                historical_coarse_status=old['original_status_unchanged'])


def fine_controls(op, out, directory, result):
    g = op.grid(30., .025)
    zero = np.zeros(g['n']); one = np.ones(g['n'])
    gaussian = np.exp(-g['r']**2 / 4)
    for kind in ('closed', 'wrong_robin'):
        checkpoint()
        src = np.zeros((3, g['n']), dtype=complex)
        src[2 if kind == 'closed' else 0] = gaussian
        row, answer, _ = out.solve(g, zero, one, .8, 1., src, ((15, 20), (20, 25)),
                                   incoming=kind == 'wrong_robin')
        row.update(kind=kind, h=.025, R=30.)
        flags = dict(row['algebra_flags'])
        if kind == 'closed':
            row['open_closed_norm_ratio'] = out.quotient(out.norm(g, answer[0]), out.norm(g, answer[2]))
            row['closed_rot_flux_ratio'] = out.quotient(abs(row['FV_rot_flux']), row['work_scale'])
            flags.update(open_zero=out.below(row['open_closed_norm_ratio'], 1e-12),
                         closed_zero=out.below(row['closed_rot_flux_ratio'], 1e-12))
        else:
            flags['negative_flux'] = row['FV_rot_flux'] < 0
        row['flags'] = flags; row['passed'] = all(flags.values())
        filename = 'QA-' + kind + '-h0.025.npz'
        np.savez_compressed(directory / filename, r=g['r'], answer_channels=answer, source_channels=src)
        row.update(artifact=filename, artifact_sha256=sha(directory / filename))
        result['new_qa'].append(row); save(directory, result)
        if not row['passed']:
            raise ValueError('Fine free control failed: ' + kind)


def load_prepared(path, expected, op, out, reference, source_dir):
    manifest = read_json(path, expected)
    if manifest['status'] != 'FINE_INPUTS_PREPARED':
        raise ValueError('Fine preparation incomplete')
    refs, sources, meta = out.load_sources(source_dir, op, reference)
    if meta['manifest_sha256'] != manifest['old_inputs']['reference']['manifest_sha256']:
        raise ValueError('Old reference manifest mismatch')
    old = manifest['old_inputs']['source_profile']
    if old['h'] != .05 or sources[.05][2]['sha256'] != old['source_sha256']:
        raise ValueError('Old source provenance mismatch')
    if not all(manifest['selected_ritz']['flags'].values()):
        raise ValueError('Fine Ritz gate mismatch')
    if not all(r['passed'] for r in manifest['profile_checks']):
        raise ValueError('Fine prepared profile gate mismatch')
    refrow = manifest['reference']['artifact']
    srcrow = manifest['source']['artifact']
    if manifest['source']['reference_sha256'] != refrow['sha256'] or manifest['source']['ritz_sha256'] != manifest['ritz_task']['artifact']['sha256']:
        raise ValueError('Fine reference/source/Ritz linkage mismatch')
    files = {}
    for key, row in (('reference', refrow), ('source', srcrow), ('ritz', manifest['ritz_task']['artifact'])):
        file = path.parent / row['file']
        if sha(file) != row['sha256']:
            raise ValueError('Fine preparation artifact mismatch')
        files[key] = file
    entries = []
    oldf, oldc, oldomega = refs[.05]
    oldsrc, oldnu, oldprov = sources[.05]
    entries.append((.05, oldf, oldc, oldomega, oldnu/2, oldsrc, None,
                    dict(h=.05, omega=oldomega, rho=oldnu/2, source=oldprov)))
    with np.load(files['reference'], allow_pickle=False) as z:
        finegrid = op.grid(120., .025)
        if not np.array_equal(z['r'], finegrid['r']):
            raise ValueError('Fine reference exact grid mismatch')
        f = z['f'].copy(); c = z['chi'].copy(); omega = float(z['omega'])
    with np.load(files['source'], allow_pickle=False) as z:
        if not np.array_equal(z['r'], finegrid['r']) or float(z['omega']) != omega:
            raise ValueError('Fine source grid/frequency mismatch')
        if float(z['canonical_q_normalization']) != 1.:
            raise ValueError('Fine source normalization mismatch')
        entries.append((.025, f, c, omega, float(z['rho']), z['local_channels'].copy(), z['J2'].copy(), manifest['source']))
    profiles = {}
    for h, f, c, omega, rho, src, j2, row in entries:
        g = op.grid(120., h)
        if f.dtype != np.float64 or c.dtype != np.float64 or f.shape != (g['n'],) or c.shape != f.shape:
            raise ValueError('Prepared profile shape/dtype mismatch')
        if src.shape != (3, g['n']):
            raise ValueError('Prepared source shape mismatch')
        if not all(np.all(np.isfinite(a)) for a in (f, c, src, omega, rho)):
            raise ValueError('Nonfinite prepared data')
        if omega != row['omega'] or rho != row['rho']:
            raise ValueError('Prepared frequency mismatch')
        if j2 is not None:
            if j2.shape != src.shape or not np.all(np.isfinite(j2)):
                raise ValueError('Fine J2 shape/finite mismatch')
            combined = np.array([(j2[0]+1j*j2[1])/np.sqrt(2), (j2[0]-1j*j2[1])/np.sqrt(2), j2[2]])
            if not np.allclose(src, combined, rtol=1e-12, atol=0):
                raise ValueError('Prepared channel convention mismatch')
        profiles[h] = (f, c, omega, 2*rho, src, row)
    if set(profiles) != {.05, .025}:
        raise ValueError('Missing fine grid')
    return profiles, manifest


def compare(rows, out):
    bykey = {(r['R'], r['h']): r for r in rows}
    def mean(row):
        w = row['windows'][0]
        return complex(w['A_real'], w['A_imag'])
    checks = []; changes = []
    for h in (.05, .025):
        left = mean(bykey[(60., h)]); right = mean(bykey[(120., h)])
        change = abs(left-right); relative = out.quotient(change, abs(right))
        changes.append(change)
        checks.append(dict(kind='R', h=h, absolute_amplitude_change=change, relative=relative, passed=out.below(relative, .01)))
    for radius in (60., 120.):
        coarse = mean(bykey[(radius, .05)]); fine = mean(bykey[(radius, .025)])
        change = abs(abs(coarse)-abs(fine)); relative = out.quotient(change, abs(fine))
        changes.append(change)
        checks.append(dict(kind='h_magnitude', R=radius, absolute_amplitude_change=change, relative=relative, passed=out.below(relative, .02)))
    reserve = 5*max(changes+[w['max_absolute_spread'] for r in rows for w in r['windows']])
    signal = [dict(R=r['R'], h=r['h'], amplitude=abs(mean(r)), reserve=reserve,
                   passed=abs(mean(r)) > reserve and abs(mean(r)) > 0) for r in rows]
    return dict(sensitivity=checks, signal_resolution=signal), all(x['passed'] for x in checks+signal)


def main():
    parser = argparse.ArgumentParser()
    for key in ('outgoing', 'operator', 'prepared', 'reference', 'source-dir', 'null-result', 'free-result', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--prepared-sha256', required=True)
    args = parser.parse_args(); args.out.mkdir(parents=True, exist_ok=False)
    result = dict(status='INCOMPLETE', code_sha256=sha(__file__), cases=[], new_qa=[],
                  outgoing_sha256=OUT_HASH, operator_sha256=OP_HASH,
                  interpretation='New fixed fine forced response; alpha^4 coefficient power; no lifetime or historical status change')
    save(args.out, result)
    try:
        out = module(args.outgoing, OUT_HASH, 'unchanged_outgoing')
        op = module(args.operator, OP_HASH, 'unchanged_operator')
        result['archived_qa'] = archived_qa(args.null_result, args.free_result, out)
        profiles, manifest = load_prepared(args.prepared, args.prepared_sha256, op, out, args.reference, args.source_dir)
        result['preparation'] = dict(sha256=sha(args.prepared), manifest=manifest)
        save(args.out, result)
        fine_controls(op, out, args.out, result)
        for radius, h in CASES:
            checkpoint()
            g = op.grid(radius, h); full = op.grid(120., h)
            ff, cc, omega, nu, fullsrc, provenance = profiles[h]
            n = g['n']; f = ff[:n]; c = cc[:n]; src = fullsrc[:, :n]
            profile = op.profile_check(g, f, c, omega, 2*omega*np.sum(full['vol']*ff*ff))
            if not profile['passed']:
                raise ValueError('Background truncation/phase gate failed')
            row, answer, means = out.solve(g, f, c, omega, nu, src, ((40, 45), (45, 50)))
            row.update(R=radius, h=h, background_check=profile, source_provenance=provenance)
            allnorm = out.norm(full, fullsrc)**2
            omitted = float(np.sum(full['vol'][n:]*abs(fullsrc[:, n:])**2))
            collar = g['r'] > radius-10
            row['source_omitted_fraction'] = out.quotient(omitted, allnorm)
            row['source_collar_fraction'] = out.quotient(float(np.sum(g['vol'][collar]*abs(src[:, collar])**2)), allnorm)
            row['boundary_background'] = dict(f=float(f[-1]), chi_minus_vac=float(c[-1]-1),
                D=float(-2*f[-1]**2+3*f[-1]**4), B=float(2*c[-1]*f[-1]))
            difference = out.quotient(abs(means[0]-means[1]), abs(means[1]))
            flags = dict(row['algebra_flags'])
            flags.update(positive_flux=row['FV_rot_flux'] > 0,
                nonzero=all(abs(a) > 0 for a in means),
                windows=all(out.below(w['relative_spread'], .01) for w in row['windows']),
                between_windows=out.below(difference, .01),
                continuum_flux=all(out.below(w['continuum_FV_relative'], .02) for w in row['windows']))
            row.update(between_windows_relative=difference, flags=flags, passed=all(flags.values()))
            filename = f'ANSWER-R{radius:g}-h{h}.npz'
            np.savez_compressed(args.out/filename, r=g['r'], answer_channels=answer, source_channels=src, omega=omega, nu=nu)
            row.update(artifact=filename, artifact_sha256=sha(args.out/filename))
            result['cases'].append(row); save(args.out, result)
            if not row['passed']:
                raise ValueError('Fine production case gate failed')
        checkpoint()
        result['comparison'], passed = compare(result['cases'], out)
        result['status'] = 'CONTROLLED_FINE_FORCED_RESPONSE' if passed else 'UNRESOLVED'
    except Exception as exc:
        result['error'] = repr(exc)
        result['status'] = 'INCOMPLETE' if isinstance(exc, RuntimeError) else 'UNRESOLVED'
    save(args.out, result)
    return 0 if result['status'] == 'CONTROLLED_FINE_FORCED_RESPONSE' else 2


if __name__ == '__main__':
    raise SystemExit(main())
