#!/usr/bin/env python3
"""Four new quadrature-phase arms; immutable saved baselines and causal targets.

Run only after independent review, with an external timeout and 120 CPU-s cap.
No old experiment entry point is called. No energy of the composed fields is
interpreted as a physical ensemble energy or radiation cancellation.
"""
import time
START = time.process_time()
import argparse
import json
from pathlib import Path
import numpy as np

TIME_HASH = '74ba12a56e60241a967c2ff143a6489adbd7b27a3b72ddeeb0d3d29fee3c43c6'
SPLIT_HASH = 'ac87c195092b607cdf106a9ad7a88606bcf0579623cd581297485f76bf7cceaa'
OBS_HASH = 'a3f302b50f184ef2b7fdf9d92afb903068e22436d2b3547fa4248f80e9a56cc3'
SPLIT_RESULT_HASH = '15593347f6b1caff683315fab65ce74734ae85fb5eff97b8a25d9276c0a568b9'
H = .05
EPS = .002
T = 128.
LEVELS = (('base', .01), ('time', .005))
GATES = dict(residual=.05, dt_change=.01, odd=.05,
             energy_charge_balance=1e-5, collar=1e-8, baseline=.004,
             reference_reserve_factor=100., arithmetic_factor=64.)


def sha(path):
    import hashlib
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked(path, digest):
    if sha(path) != digest:
        raise ValueError('Provenance mismatch: ' + str(path))
    return path


def module(path, digest, name):
    import importlib.util
    checked(path, digest)
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time() - START >= 115:
        raise RuntimeError('INCOMPLETE: 115 CPU-s checkpoint; total external cap 120 CPU-s')


def save(directory, result):
    result['cpu_seconds'] = time.process_time() - START
    tmp = directory / 'RESULT.tmp'
    tmp.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    tmp.replace(directory / 'RESULT.json')


def artifact(directory, filename, **arrays):
    checkpoint()
    target = directory / filename
    tmp = directory / (filename + '.tmp')
    with tmp.open('wb') as stream:
        np.savez_compressed(stream, **arrays)
    tmp.replace(target)
    return dict(file=filename, sha256=sha(target))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def diagnostic_gate(d, initial_energy, baseline=False):
    require(all(np.isfinite(d[k]) for k in ('E', 'Q', 'Edrift', 'Qdrift', 'balance', 'collar')),
            'Nonfinite conservation diagnostic')
    require(max(d['Edrift'], d['Qdrift'], d['balance']) <= GATES['energy_charge_balance']
            and d['collar'] / initial_energy <= GATES['collar'], 'Conservation/collar gate failed')
    if baseline:
        require(all(np.isfinite(d[k]) and d[k] < GATES['baseline']
                    for k in ('rphi', 'rchi', 'tphi', 'tchi', 'driftphi', 'driftchi')),
                'Saved baseline stationarity gate failed')


def read_ring(directory, entry, times, r, shape, field_key):
    path = checked(directory / entry['file'], entry['sha256'])
    with np.load(path, allow_pickle=False) as z:
        require(np.array_equal(z['t'], times) and np.array_equal(z['r'], r), 'Ring grid/time mismatch')
        fields = z[field_key].copy()
        labels = z['sources'] if field_key == 'rotating_fields_by_source' else z['components']
        expected = ['DC', 'H2'] if field_key == 'rotating_fields_by_source' else ['phi', 'phi_t', 'chi', 'chi_t']
        require(list(labels) == expected, 'Ring component labels mismatch')
    require(fields.shape == shape and np.all(np.isfinite(fields)), 'Ring shape/finite mismatch')
    return fields


def load_saved(args, td, mode, metadata):
    observed = json.loads(checked(args.observed_dir / 'RESULT.json', OBS_HASH).read_text())
    split = json.loads(checked(args.split_dir / 'RESULT.json', SPLIT_RESULT_HASH).read_text())
    require(observed['status'] == 'UNRESOLVED' and observed['code_sha256'] == TIME_HASH,
            'Saved nonlinear identity/status mismatch')
    require(split['status'] == 'CAUSAL_SPLIT_DIAGNOSIS_COMPLETE' and split['code_sha256'] == SPLIT_HASH
            and split['sum_validation_passed'] and split['observed']['result_sha256'] == OBS_HASH,
            'Saved causal identity/status mismatch')
    # Exact common Ritz/source gauge; no refit or independent phase convention.
    ours = [m for m in metadata if m['h'] == H]
    require(len(ours) == 1, 'Input metadata ambiguity')
    for prior in (observed, split):
        previous = [m for m in prior['inputs'] if m['h'] == H]
        require(len(previous) == 1 and previous[0] == ours[0], 'Saved/common input gauge mismatch')
    g = mode['grid']; indices = np.flatnonzero((g['r'] >= 40-2*H) & (g['r'] <= 50+2*H))
    times = np.arange(1281)*.1; r = g['r'][indices]
    saved = {}; provenance = []
    for level, dt in LEVELS:
        arms = {}; fields = {}
        for eps in (0., EPS, -EPS):
            rows = [a for a in observed['arms'] if a['level'] == level and a['epsilon'] == eps]
            require(len(rows) == 1, 'Saved arm missing/duplicated')
            arm = rows[0]; samples = arm['samples']
            require(arm['complete'] and arm['h'] == H and arm['dt'] == dt and len(samples) == 321,
                    'Saved arm incomplete/grid mismatch')
            require(np.allclose([d['t'] for d in samples], np.arange(321)*.4, rtol=0, atol=1e-12),
                    'Saved diagnostic times mismatch')
            for d in samples:
                diagnostic_gate(d, samples[0]['E'], eps == 0.)
            for key in ('initial_artifact', 'final_artifact'):
                entry = arm[key]; checked(args.observed_dir / entry['file'], entry['sha256'])
            fields[eps] = read_ring(args.observed_dir, arm['ring_artifact'], times, r,
                                   (1281, 4, len(r)), 'rotating_fields')
            arms[eps] = arm
        levels = [l for l in observed['levels'] if l['level'] == level]
        require(len(levels) == 1 and levels[0]['complete'], 'Saved level incomplete')
        pairs = [p for p in levels[0]['pairs'] if p['epsilon'] == EPS]
        require(len(pairs) == 1 and pairs[0]['passed'] and pairs[0]['max_error'] < GATES['odd'],
                'Saved full odd comparison failed')
        alpha = arms[EPS]['initial']['alpha']
        require(alpha > 0 and arms[-EPS]['initial']['alpha'] == -alpha
                and arms[0.]['initial']['alpha'] == 0, 'Saved alpha pair mismatch')
        saved[level] = dict(baseline=fields[0.], alpha=alpha, arms=arms,
                            phase0_pair_sum=fields[EPS]+fields[-EPS],
                            phase0_phi_hull=abs(fields[EPS][:,0])+abs(fields[-EPS][:,0]),
                            even0=(fields[EPS]+fields[-EPS]-2*fields[0.])/(2*alpha**2))
        provenance.append(dict(level=level, dt=dt, alpha=alpha, odd_max_error=pairs[0]['max_error'],
                               arms=[dict(epsilon=e, initial=a['initial'],
                                          ring_artifact=a['ring_artifact'],
                                          initial_artifact=a['initial_artifact'],
                                          final_artifact=a['final_artifact']) for e,a in arms.items()]))
    require(saved['base']['alpha'] == saved['time']['alpha'] == split['observed']['alpha'],
            'Cross-level/split alpha mismatch')
    causal = {}
    for dt in (.02, .01):
        rows = [row for row in split['runs'] if row['dt'] == dt]
        require(len(rows) == 1 and rows[0]['complete'] and rows[0]['last_time'] == T,
                'Saved causal run incomplete')
        causal[dt] = read_ring(args.split_dir, rows[0]['ring_artifact'], times, r,
                               (1281, 2, 4, len(r)), 'rotating_fields_by_source')
    return times, r, indices, saved, causal, dict(observed_sha256=OBS_HASH,
            split_sha256=SPLIT_RESULT_HASH, reused_levels=provenance,
            causal_runs=[dict(dt=x['dt'], ring_artifact=x['ring_artifact']) for x in split['runs']])


def run_pair(args, result, td, dyn, exc, mode90, level, dt, saved, indices):
    checkpoint(); omega = mode90['reference'][2]
    arms = {}; states = {}; starts = {}; first = {}; flux = {}; oldflux = {}
    rings = {eps: np.empty((1281, 4, len(indices)), complex) for eps in (EPS, -EPS)}
    for eps in (EPS, -EPS):
        g, state, meta = exc.initial(dyn, H, eps, mode90['reference'], mode90)
        require(meta['alpha'] == saved['arms'][eps]['initial']['alpha']
                and meta['reference_norm'] == saved['arms'][eps]['initial']['reference_norm'],
                'Phase change altered canonical alpha/reference norm')
        arm = dict(level=level, h=H, dt=dt, epsilon=eps, phase=np.pi/2,
                   initial=meta, samples=[], complete=False)
        arm['initial_artifact'] = artifact(args.out, f'{level}-phase90-eps{eps:g}-initial.npz',
                r=g.r, phi=state[0], pi=state[1], chi=state[2], chi_t=state[3])
        result['arms'].append(arm); arms[eps] = arm; states[eps] = state
        starts[eps] = tuple(x.copy() for x in state)
        first[eps] = dyn.diagnose(g, state, starts[eps]); flux[eps] = 0.
        oldflux[eps] = dyn.outward_flux(g, state[0]); save(args.out, result)
    pair = dict(level=level, dt=dt, complete=False, last_time=0., odd_max_error=0., odd_samples=[])
    result['pairs'].append(pair); save(args.out, result)
    root = np.sqrt(g.vol); norm = float(np.linalg.norm(mode90['v']))
    for step in range(round(T/dt)+1):
        t = step*dt
        if step % 20 == 0:
            checkpoint()
            require(all(np.all(np.isfinite(x)) for state in states.values() for x in state),
                    'Nonfinite new nonlinear state')
        if step % round(.1/dt) == 0:
            for eps in (EPS, -EPS):
                rings[eps][step//round(.1/dt)] = td.rotating_ring(states[eps], omega, t, indices)
        if step % round(.4/dt) == 0:
            for eps in (EPS, -EPS):
                d = dyn.diagnose(g, states[eps], starts[eps]); f = first[eps]
                d.update(t=t, Edrift=abs(d['E']/f['E']-1), Qdrift=abs(d['Q']/f['Q']-1),
                         balance=abs(d['Qcore']-f['Qcore']+flux[eps])/abs(f['Q']), flux_integral=flux[eps])
                diagnostic_gate(d, f['E']); arms[eps]['samples'].append(d)
            odd = (exc.canonical(states[EPS], omega, t, root)
                   - exc.canonical(states[-EPS], omega, t, root))/(2*saved['alpha'])
            target = np.real(mode90['v']*np.exp(1j*mode90['rho']*t))
            err = float(np.linalg.norm(odd-target)/norm)
            require(np.isfinite(err), 'Nonfinite full odd diagnostic')
            pair['odd_max_error'] = max(pair['odd_max_error'], err)
            pair['odd_samples'].append(dict(t=t, error=err))
            pair['last_time'] = t
            if step % round(4/dt) == 0:
                save(args.out, result)
        if step == round(T/dt):
            break
        for eps in (EPS, -EPS):
            states[eps] = dyn.advance(g, states[eps], dt)
            current = dyn.outward_flux(g, states[eps][0])
            flux[eps] += .5*dt*(oldflux[eps]+current); oldflux[eps] = current
    for eps in (EPS, -EPS):
        state = states[eps]; arm = arms[eps]
        arm['final_artifact'] = artifact(args.out, f'{level}-phase90-eps{eps:g}-final.npz',
                r=g.r, phi=state[0], pi=state[1], chi=state[2], chi_t=state[3])
        arm['ring_artifact'] = artifact(args.out, f'{level}-phase90-eps{eps:g}-ring.npz',
                t=np.arange(1281)*.1, r=g.r[indices], rotating_fields=rings[eps],
                components=np.array(['phi', 'phi_t', 'chi', 'chi_t']))
        arm['complete'] = True; save(args.out, result)
    pair.update(complete=True, odd_passed=pair['odd_max_error'] < GATES['odd'])
    even90 = (rings[EPS]+rings[-EPS]-2*saved['baseline'])/(2*saved['alpha']**2)
    # Source-history components, not physically coexisting fields.
    # Algebraically (even0 +/- even90)/2. Cancel the common baseline
    # before evaluating H, matching its baseline-free summand envelope.
    pair90 = rings[EPS]+rings[-EPS]
    separated = np.stack((saved['phase0_pair_sum']+pair90-4*saved['baseline'],
                          saved['phase0_pair_sum']-pair90), axis=1)/(4*saved['alpha']**2)
    pair['separated_artifact'] = artifact(args.out, f'{level}-separated-ring.npz',
            t=np.arange(1281)*.1, r=g.r[indices], rotating_fields_by_source=separated,
            sources=np.array(['DC', 'H2']))
    save(args.out, result)
    # Positive pointwise summand envelopes for phi only. Baseline cancels
    # algebraically in H, while D contains -4*Ubase, all over 4*alpha^2.
    # eta is an empirical sensitivity scale, not a floating-point error
    # enclosure for the evolution, integration or all accumulated operations.
    common_hull = (saved['phase0_phi_hull']+abs(rings[EPS][:,0])+abs(rings[-EPS][:,0]))
    envelope = np.stack((common_hull+4*abs(saved['baseline'][:,0]),common_hull),axis=1)
    envelope /= 4*saved['alpha']**2
    return dict(fields=separated, envelope=envelope, even90=even90, even0=saved['even0'])


def analyse(td, split_code, mode, times, r, indices, separated, causal):
    rows = []; differences = []; phase90_diagnostics = []; vol = mode['grid']['vol'][indices]
    for wi, left in enumerate((88., 104.5)):
        checkpoint(); right = left+2*np.pi/mode['rho']; nu = 2*mode['rho']
        ts, ref = split_code.interval(times, causal[.01], left, right)
        _, coarse = split_code.interval(times, causal[.02], left, right)
        refcoef = td.coefficient(times, causal[.01], left, right, nu)
        coarsecoef = td.coefficient(times, causal[.02], left, right, nu)
        actual = {lev: split_code.interval(times, data['fields'], left, right)[1] for lev,data in separated.items()}
        coeff = {lev: td.coefficient(times, data['fields'], left, right, nu) for lev,data in separated.items()}
        hull = {lev: split_code.interval(times, data['envelope'], left, right)[1] for lev,data in separated.items()}
        # Positive time average, NEVER the oscillatory Fourier coefficient of
        # the positive hull (which might cancel). Same endpoint interpolation.
        hull_mean = {lev: td.coefficient(times, data['envelope'], left, right, 0.).real
                     for lev,data in separated.items()}
        weights = np.diff(ts)
        for si, (lo, hi) in enumerate(td.SHELLS):
            mask = (r >= lo) & (r < hi); vv = vol[mask]
            def norm(field):
                return float(np.sqrt(np.sum(vv*abs(field[mask])**2)))
            def time_norm(field):
                density = np.sum(vv*abs(field[:, mask])**2, axis=1)
                return float(np.sqrt(np.sum(.5*(density[1:]+density[:-1])*weights)))
            for ci, name in enumerate(('DC', 'H2')):
                nt = time_norm(ref[:, ci, 0]); nc = norm(refcoef[ci, 0])
                delta_ref = dict(time=time_norm(ref[:,ci,0]-coarse[:,ci,0]),
                                 band=norm(refcoef[ci,0]-coarsecoef[ci,0]))
                delta_dt = dict(time=time_norm(actual['time'][:,ci,0]-actual['base'][:,ci,0]),
                                band=norm(coeff['time'][ci,0]-coeff['base'][ci,0]))
                factor = GATES['arithmetic_factor']*np.finfo(np.float64).eps
                eta_by_level = {lev:dict(time=factor*time_norm(hull[lev][:,ci]),
                                         band=factor*norm(hull_mean[lev][ci])) for lev,_ in LEVELS}
                eta = {key:max(item[key] for item in eta_by_level.values()) for key in ('time','band')}
                reserve = {key:GATES['reference_reserve_factor']*max(delta_ref[key],delta_dt[key],eta[key])
                           for key in ('time','band')}
                resolved = dict(time=bool(np.isfinite(nt) and nt>reserve['time']),
                                band=bool(np.isfinite(nc) and nc>reserve['band']))
                ref_dt = dict(time=td.ratio(delta_ref['time'],nt),band=td.ratio(delta_ref['band'],nc))
                common = dict(component=name, time_window=wi, window=[left,right], shell=si,
                              radius_window=[lo,hi], reference_time_L2=nt, reference_band_L2=nc,
                              causal_dt_change=ref_dt,absolute_causal_dt_change=delta_ref,
                              absolute_nonlinear_dt_change=delta_dt,eta_arithmetic_by_level=eta_by_level,
                              reference_reserve=reserve,reference_resolved=resolved)
                for lev, _ in LEVELS:
                    et = time_norm(actual[lev][:,ci,0]-ref[:,ci,0])
                    ec = norm(coeff[lev][ci,0]-refcoef[ci,0])
                    errors = dict(time=td.ratio(et,nt), band=td.ratio(ec,nc))
                    flags = {key:td.below(value,GATES['residual']) for key,value in errors.items()}
                    flags.update({key+'_reference_resolved':value for key,value in resolved.items()})
                    rows.append(dict(**common, level=lev, absolute_errors=dict(time=et,band=ec),
                                     errors=errors,flags=flags))
                errors = dict(time=td.ratio(delta_dt['time'],nt), band=td.ratio(delta_dt['band'],nc))
                flags = {key:td.below(value,GATES['dt_change']) for key,value in errors.items()}
                flags.update({key+'_reference_resolved':value for key,value in resolved.items()})
                differences.append(dict(**common, absolute_changes=delta_dt, errors=errors,flags=flags))
            # Independent saved causal D-H, not our algebraic separated D-H.
            predicted_time = ref[:,0,0]-ref[:,1,0]
            predicted_coef = refcoef[0,0]-refcoef[1,0]
            for lev,_ in LEVELS:
                data = separated[lev]
                _, phase90 = split_code.interval(times,data['even90'],left,right)
                _, phase0 = split_code.interval(times,data['even0'],left,right)
                phase90coef = td.coefficient(times,data['even90'],left,right,nu)
                phase0coef = td.coefficient(times,data['even0'],left,right,nu)
                nt0 = time_norm(phase0[:,0]); nc0 = norm(phase0coef[0])
                phase90_diagnostics.append(dict(level=lev,time_window=wi,shell=si,window=[left,right],
                    radius_window=[lo,hi],normalization='saved phase0 even phi; diagnostic only, no gate',
                    phase0_time_L2=nt0,phase0_band_L2=nc0,
                    time_error_over_phase0=td.ratio(time_norm(phase90[:,0]-predicted_time),nt0),
                    band_error_over_phase0=td.ratio(norm(phase90coef[0]-predicted_coef),nc0)))
    return rows, differences, phase90_diagnostics


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('time-code','split-code','excitation','dynamics','operator','outgoing','response-code',
                 'reference','source-dir','prepared-dir','response-dir','search-dir','observed-dir','split-dir','out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args(); args.out.mkdir(parents=True, exist_ok=False)
    result = dict(status='INCOMPLETE', terminal_complete=False, code_sha256=sha(__file__),
            bound_hashes=dict(time_code=TIME_HASH,split_code=SPLIT_HASH,observed=OBS_HASH,split=SPLIT_RESULT_HASH),
            gates=GATES, budget=dict(cpu_seconds=120,checkpoint_seconds=115,external_timeout_required=True),
            arms=[],pairs=[],measurements=[],dt_comparisons=[],phase90_diagnostics=[],
            arithmetic_reserve_interpretation='64*float64_eps times positive summand hull norm; empirical sensitivity only, not accumulated-error certification',
            interpretation='Finite phase-cycle causal-component comparison; old UNRESOLVED unchanged; no ensemble flux claim')
    save(args.out, result)
    try:
        td = module(args.time_code,TIME_HASH,'unchanged_time_domain')
        split_code = module(args.split_code,SPLIT_HASH,'unchanged_causal_split')
        exc = module(args.excitation,td.HASH['excitation'],'unchanged_excitation')
        dyn = module(args.dynamics,td.HASH['dynamics'],'unchanged_dynamics')
        op = module(args.operator,td.HASH['operator'],'unchanged_operator')
        out = module(args.outgoing,td.HASH['outgoing'],'unchanged_outgoing')
        response = module(args.response_code,td.HASH['response_code'],'unchanged_response_loader')
        result['dependency_hashes'] = td.HASH
        checkpoint(); modes, metadata = td.load_inputs(args,op,out,response)
        mode = modes[H]; result['inputs'] = metadata
        times,r,indices,saved,causal,provenance = load_saved(args,td,mode,metadata)
        result['saved_inputs'] = provenance
        mode90 = dict(mode); mode90['v'] = mode['v'].copy()*1j
        require(np.array_equal(mode90['v'],1j*mode['v']), 'Full-vector quadrature phase mismatch')
        result['phase_change'] = dict(multiplier=[0.,1.],renormalized=False,rho=mode['rho'],
                omega=mode['reference'][2],alpha=saved['base']['alpha'],full_vector_size=len(mode['v']))
        save(args.out,result); separated = {}
        for level,dt in LEVELS:
            separated[level] = run_pair(args,result,td,dyn,exc,mode90,level,dt,saved[level],indices)
        checkpoint()
        result['measurements'],result['dt_comparisons'],result['phase90_diagnostics'] = analyse(
                td,split_code,mode,times,r,indices,separated,causal)
        expected = {(level,eps) for level,_ in LEVELS for eps in (EPS,-EPS)}
        complete = (len(result['arms']) == 4 and {(a['level'],a['epsilon']) for a in result['arms']} == expected
                    and all(a['complete'] and len(a['samples']) == 321 and a['samples'][-1]['t'] == T
                            for a in result['arms'])
                    and len(result['pairs']) == 2 and all(p['complete'] and p['last_time'] == T
                            and len(p['odd_samples']) == 321 for p in result['pairs'])
                    and len(result['measurements']) == 16 and len(result['dt_comparisons']) == 8
                    and len(result['phase90_diagnostics']) == 8)
        require(complete,'Terminal completeness failed')
        result['terminal_complete'] = True
        passed = (all(p['odd_passed'] for p in result['pairs']) and
                  all(all(row['flags'].values()) for row in result['measurements']+result['dt_comparisons']))
        result['status'] = 'CONTROLLED_PHASE_CYCLE_CAUSAL_COMPONENTS' if passed else 'UNRESOLVED'
    except Exception as error:
        result['error'] = repr(error)
        result['status'] = 'INCOMPLETE'
    save(args.out,result)
    return 0 if result['status'] == 'CONTROLLED_PHASE_CYCLE_CAUSAL_COMPONENTS' else 2


if __name__ == '__main__':
    raise SystemExit(main())
