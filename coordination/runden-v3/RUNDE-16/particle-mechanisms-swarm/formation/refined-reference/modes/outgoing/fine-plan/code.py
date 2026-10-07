#!/usr/bin/env python3
"""One new Q1100 grid, one fixed Ritz task, one quadratic source. No outgoing solve."""
import time
START = time.process_time()
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

HASH = dict(beutel='f831e818b4f2a00f56e281f5972badb1d9ed344dcd2242826ab6b31076917ecb',
            operator='467ad3e19cd8efcdac4ec2dcc670b50aaa59cc6f7e9e44d625ebbf94ba0d32c6',
            source_code='5ba2d7e001f6145ff5f75afedadf6850565df8fac25412f84cab1c1c1a21443f',
            dynamics='466b25fb813770a1ab13eea962c93b39308dfe1ad22171fe638c60fdafef998d',
            seed='1bb153a166e15d8ca43848613e638e8e0d20978833be6c564dcf7bc33f926d8c',
            search='77ecf9bbe03b96db901d76728e074a897725eb52213f90dae76c7200ba5364ea',
            source='a2270a05c7270eeeb16e5fd04d12bd1367bff38af0205062b2643aea05b2a574')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked(path, expected):
    if sha(path) != expected:
        raise ValueError('Hash mismatch: ' + str(path))
    return path


def module(path, expected, name):
    checked(path, expected)
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time() - START >= 10:
        raise RuntimeError('INCOMPLETE: 10 CPU-s checkpoint')


def save(out, result):
    result['cpu_seconds'] = time.process_time() - START
    tmp = out / 'RESULT.tmp'
    tmp.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    tmp.replace(out / 'RESULT.json')


def artifact(out, name, **arrays):
    path = out / name
    np.savez_compressed(path, **arrays)
    return dict(file=name, sha256=sha(path))


def main():
    parser = argparse.ArgumentParser()
    for name in ('beutel', 'operator', 'source-code', 'dynamics', 'seed',
                 'reference', 'search-dir', 'source-dir', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    result = dict(status='INCOMPLETE', code_sha256=sha(__file__), input_hashes=HASH,
                  interpretation='Fine-grid diagnostic Ritz source only; old localization FAIL and outgoing UNRESOLVED unchanged')
    save(args.out, result)
    try:
        b = module(args.beutel, HASH['beutel'], 'fine_beutel')
        op = module(args.operator, HASH['operator'], 'fine_modes')
        src = module(args.source_code, HASH['source_code'], 'fine_source')
        dyn = module(args.dynamics, HASH['dynamics'], 'fine_dynamics')
        checked(args.seed, HASH['seed'])
        search = json.loads(checked(args.search_dir / 'RESULT.json', HASH['search']).read_text())
        old_source = json.loads(checked(args.source_dir / 'RESULT.json', HASH['source']).read_text())
        refs, meta = op.load_refs(args.reference)
        if (search['reference']['manifest_sha256'] != meta['manifest_sha256'] or
            old_source['reference']['manifest_sha256'] != meta['manifest_sha256'] or
            search['code_sha256'] != HASH['operator'] or
            old_source['status'] != 'LOCAL_SOURCE_DIAGNOSTICS_COMPLETE'):
            raise ValueError('Old reference/search/source association mismatch')
        old_rows = [r for r in old_source['profiles'] if r['h'] == .05]
        tasks = [r for r in search['tasks'] if r['h'] == .05 and r['R'] == 120 and r['shift'] == .3]
        if len(old_rows) != 1 or len(tasks) != 1 or not tasks[0]['complete']:
            raise ValueError('Missing/ambiguous old source or Ritz task')
        old_row, task = old_rows[0], tasks[0]
        checked(args.source_dir / old_row['source_artifact'], old_row['source_sha256'])
        checked(args.search_dir / task['artifact'], task['artifact_sha256'])
        if old_row['ritz_sha256'] != task['artifact_sha256']:
            raise ValueError('Old source Ritz association mismatch')
        coarse = op.grid(120., .05)
        with np.load(args.search_dir / task['artifact'], allow_pickle=False) as z:
            ix = np.flatnonzero((z['eigenvalues'].imag > .38) & (z['eigenvalues'].imag < .39))
            if len(ix) != 1:
                raise ValueError('Old Ritz ambiguity')
            j = int(ix[0]); old_value = complex(z['eigenvalues'][j])
            old_q = z['eigenvectors'][:3*coarse['n'], j].copy()
        if (abs(old_value.imag-task['ritz'][j]['rho']) > 1e-12 or
            abs(old_value.real-task['ritz'][j]['lambda_real']) > 1e-12 or
            old_value.imag != old_row['rho'] or refs[.05][2] != old_row['omega']):
            raise ValueError('Old Ritz metadata mismatch')
        old_q /= np.linalg.norm(old_q)
        result['old_inputs'] = dict(reference=meta, source_profile=old_row,
                                   ritz_task=task, original_search_status=search['status'])
        result['source_qa'] = src.qa(dyn)
        save(args.out, result)
        if not result['source_qa']['passed']:
            raise ValueError('Unchanged quadratic-source QA failed')
        checkpoint()

        with np.load(args.seed, allow_pickle=False) as z:
            ix = np.flatnonzero((abs(z['Q']-1100) < 1e-5) & (z['sweep'] == 'seed') &
                                (abs(z['omega2']-1.03666310756389) < 1e-10))
            if len(ix) != 1:
                raise ValueError('Archived seed ambiguous')
            j = int(ix[0]); r = z['r'].astype(float)
            fs = z['f'][j].astype(float); cs = z['g'][j].astype(float)
            omega_seed = float(np.sqrt(z['omega2'][j]))
        h = .025; grid = op.grid(120., h); G = b.Grid(h, 120.); M = b.Model('M2')
        if not np.array_equal(G.r, grid['r']) or not np.allclose(G.V, grid['vol'], rtol=1e-14, atol=0):
            raise ValueError('BEUTEL/operator grid mismatch')
        f0 = np.interp(G.r, r, fs, left=fs[0], right=0.)
        c0 = np.interp(G.r, r, cs, left=cs[0], right=1.)
        f, c = f0.copy(), c0.copy()
        lam = (1100/(2*np.sum(G.V*f*f)))**2
        E0 = b.observables(M, G, f, c, lam)['E']
        row = dict(h=h, R=120., iterations=[], initial_E=float(E0), seed_omega=omega_seed)
        result['reference'] = row
        converged = False
        for it in range(31):
            checkpoint()
            if not (np.isfinite(lam) and lam > 0 and np.all(np.isfinite(f)) and np.all(np.isfinite(c))):
                raise ValueError('Invalid Newton state; last valid iteration retained')
            obs = b.observables(M, G, f, c, lam)
            df = float(np.sqrt(np.sum(G.V*(f-f0)**2)/np.sum(G.V*f0*f0)))
            dc = float(np.sqrt(np.sum(G.V*(c-c0)**2)/np.sum(G.V*(c0-1)**2)))
            qerr = abs(obs['Q']/1100-1)
            err = max(b.resnorm(G, *b.residual(M, G, f, c, lam)), qerr)
            if not all(np.isfinite(x) for x in (df, dc, err, obs['E'], obs['Q'], obs['omega'])):
                raise ValueError('Nonfinite Newton diagnostics')
            row['iterations'].append(dict(iteration=it, err=float(err), df=df, dc=dc,
                                          omega=float(obs['omega']), Q=float(obs['Q']), E=float(obs['E'])))
            save(args.out, result)
            if max(df, dc) > .02 or abs(obs['omega']/omega_seed-1) > .01:
                raise ValueError('Original Newton branch-neighbourhood gate failed')
            if f.min() < -1e-10 or c.min() < -1e-8 or c.max() > 1+1e-8:
                raise ValueError('Original profile range gate failed')
            if abs(obs['E']/E0-1) > .02:
                raise ValueError('Original energy-departure gate failed')
            if err < 1e-9:
                converged = True
                break
            if it < 30:
                f, c, lam, _, _, _ = b.newton_Q(M, G, f, c, lam, 1100, tol=1e-9, maxit=1)
        if not converged or qerr >= 1e-10 or obs['E']/1100 >= np.sqrt(2):
            raise ValueError('Original final reference gate failed')
        s = f*f; potential = .25*(c*c-1)**2+(1+c*c)*s-s*s+.5*s**3
        energy = float(np.sum(G.V*(lam*s+potential)) +
                       np.sum(G.a*(np.diff(np.append(f, 0))**2+.5*np.diff(np.append(c, 1))**2))/h)
        manifest = json.loads((args.reference/'MANIFEST.json').read_text())
        eold = [r['E'] for r in manifest['profiles'] if r['h'] == .05]
        if len(eold) != 1 or abs(energy/obs['E']-1) >= 1e-12 or abs(eold[0]/energy-1) >= 1e-3:
            raise ValueError('Hamiltonian or cross-grid energy gate failed')
        omega = float(obs['omega'])
        row.update(E=energy, omega=omega, Q=float(obs['Q']), final_residual=float(err),
                   cross_grid_energy_relative=float(abs(eold[0]/energy-1)),
                   artifact=artifact(args.out, 'reference-h0.025.npz', r=G.r, f=f, chi=c,
                                     omega=omega, Q=float(obs['Q']), h=h,
                                     seed_sha256=HASH['seed'], source_sha256=HASH['beutel']))
        result['profile_checks'] = []
        for radius in (120., 60.):
            gg = op.grid(radius, h); n = gg['n']
            check = op.profile_check(gg, f[:n], c[:n], omega, float(obs['Q']))
            check.update(R=radius, h=h); result['profile_checks'].append(check)
            save(args.out, result)
            if not check['passed']:
                raise ValueError('Fine reference/phase/truncated-box gate failed')
        checkpoint()

        A, K, gyro, blocks = op.operators(grid, f, c, omega); A = A.astype(complex)
        index = np.arange(6*grid['n'], dtype=float)
        start = (1+.1*np.cos(index*.17))+1j*.1*np.sin(index*.11)
        start /= np.linalg.norm(start)
        task = dict(R=120., h=h, shift=.3, complete=False, ritz=[])
        result['ritz_task'] = task; save(args.out, result)
        values, vectors = op.eigs(A, k=4, sigma=.3j, which='LM', ncv=20,
                                  tol=1e-9, maxiter=300, v0=start)
        if not np.all(np.isfinite(values)) or not np.all(np.isfinite(vectors)):
            raise ValueError('Nonfinite Ritz data')
        for j, value in enumerate(values):
            diag, _ = op.diagnostic(grid, f, omega, A, K, gyro, blocks, value, vectors[:, j])
            task['ritz'].append(diag)
        task.update(complete=True, artifact=artifact(args.out, 'R120-h0.025-shift0.3.npz',
                                                     eigenvalues=values, eigenvectors=vectors))
        save(args.out, result)
        checkpoint()
        ix = np.flatnonzero((values.imag > .38) & (values.imag < .39))
        if len(ix) != 1:
            raise ValueError('New Ritz selection ambiguous/missing')
        j = int(ix[0]); value = values[j]; diag = task['ritz'][j]
        _, q = op.diagnostic(grid, f, omega, A, K, gyro, blocks, value, vectors[:, j])
        ov, retained_fine, retained_old = op.overlap(q, grid, old_q, coarse)
        flags = dict(real_part=abs(value.real)<1e-7,
                     frequency=.001 < value.imag < np.sqrt(2)-omega-.001,
                     first_residual=diag['first_order_residual']<1e-8,
                     quadratic_residual=diag['quadratic_residual']<1e-8,
                     charge=diag['deltaQ_scaled']<1e-7,
                     frequency_comparison=abs(value.imag-old_value.imag)<5e-4, overlap=ov>.98)
        result['selected_ritz'] = dict(index=j, diagnostic=diag,
            flags={k:bool(v) for k,v in flags.items()}, frequency_difference=float(abs(value.imag-old_value.imag)),
            field_overlap=ov, retained_norms=[retained_fine, retained_old],
            original_localization_candidate_flag_unchanged=diag['candidate'])
        save(args.out, result)
        if not all(flags.values()):
            raise ValueError('Fine diagnostic Ritz numerical/branch gate failed')

        physq = q.reshape(3, grid['n'])/grid['root']
        j2 = src.source(f, c, physq)/4
        dc = .5*(src.source(f, c, physq.real)+src.source(f, c, physq.imag))
        channels = np.array([(j2[0]+1j*j2[1])/np.sqrt(2), (j2[0]-1j*j2[1])/np.sqrt(2), j2[2]])
        if not all(np.all(np.isfinite(x)) for x in (dc, j2, channels)):
            raise ValueError('Nonfinite quadratic source')
        rho = float(value.imag)
        result['source'] = dict(h=h, R=120., rho=rho, omega=omega,
            canonical_q_normalization=1., reference_sha256=row['artifact']['sha256'],
            ritz_sha256=task['artifact']['sha256'],
            artifact=artifact(args.out, 'SOURCE-h0.025.npz', r=grid['r'], DC=dc, J2=j2,
                              local_channels=channels, rho=rho, omega=omega, canonical_q_normalization=1.),
            local_channel_L2=[src.norm(grid['vol'], x) for x in channels],
            DC_component_L2=[src.norm(grid['vol'], x) for x in dc],
            J2_component_L2=[src.norm(grid['vol'], x) for x in j2])
        checkpoint()
        result['status'] = 'FINE_INPUTS_PREPARED'
    except Exception as exc:
        result['error'] = repr(exc)
        result['status'] = 'INCOMPLETE' if isinstance(exc, RuntimeError) else 'UNRESOLVED'
    save(args.out, result)
    return 0 if result['status'] == 'FINE_INPUTS_PREPARED' else 2


if __name__ == '__main__':
    raise SystemExit(main())
