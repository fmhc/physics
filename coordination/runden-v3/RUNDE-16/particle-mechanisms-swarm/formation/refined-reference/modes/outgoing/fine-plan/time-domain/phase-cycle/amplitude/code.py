#!/usr/bin/env python3
"""Six missing small-amplitude arms; direct field differences on one spatial grid.
External caps 159 CPU-s / 240 wall-s required. No causal target or fitted order.
"""
import time
START = time.process_time()
import argparse
import json
from pathlib import Path
import numpy as np

PHASE_CODE = '3509332b4732c8497e9246855fc7be6254ff1681e3e2e99b823457180aaa1446'
PHASE_RESULT = 'b7d938e4bda00bb05598f540f05320b2e3cad7a8a8f3f4be940a9d5884b8eafd'
TIME_CODE = '74ba12a56e60241a967c2ff143a6489adbd7b27a3b72ddeeb0d3d29fee3c43c6'
OBSERVED = 'a3f302b50f184ef2b7fdf9d92afb903068e22436d2b3547fa4248f80e9a56cc3'
SPLIT_CODE = 'ac87c195092b607cdf106a9ad7a88606bcf0579623cd581297485f76bf7cceaa'
H, T, SMALL, LARGE = .05, 128., .001, .002
LEVELS = (('base', .01), ('time', .005))
COMPONENTS = ('theta0', 'theta90', 'D', 'H2')


def sha(path):
    import hashlib
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def checked(path, digest):
    require(sha(path) == digest, 'Hash mismatch: '+str(path))
    return path


def module(path, digest, name):
    import importlib.util
    checked(path, digest)
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time()-START >= 150:
        raise RuntimeError('INCOMPLETE: 150 CPU-s checkpoint; external cap 159 CPU-s')


def save(directory, result):
    result['cpu_seconds'] = time.process_time()-START
    tmp = directory/'RESULT.tmp'
    tmp.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    tmp.replace(directory/'RESULT.json')


def artifact(directory, filename, **arrays):
    checkpoint()
    target = directory/filename
    tmp = directory/(filename+'.tmp')
    with tmp.open('wb') as stream:
        np.savez_compressed(stream, **arrays)
    tmp.replace(target)
    return dict(file=filename, sha256=sha(target))


def load_saved(args, pc, mode, metadata):
    old = json.loads(checked(args.observed_dir/'RESULT.json', OBSERVED).read_text())
    phase = json.loads(checked(args.phase_dir/'RESULT.json', PHASE_RESULT).read_text())
    require(old['status']=='UNRESOLVED' and old['code_sha256']==TIME_CODE,
            'Original nonlinear identity mismatch')
    require(phase['status']=='CONTROLLED_PHASE_CYCLE_CAUSAL_COMPONENTS'
            and phase['terminal_complete'] and phase['code_sha256']==PHASE_CODE
            and phase['bound_hashes']['observed']==OBSERVED, 'Phase-cycle identity mismatch')
    ours = [m for m in metadata if m['h']==H]
    require(len(ours)==1, 'Input metadata ambiguous')
    for prior in (old, phase):
        require([m for m in prior['inputs'] if m['h']==H]==ours,
                'Reference/Ritz/gauge metadata mismatch')
    g=mode['grid']; indices=np.flatnonzero((g['r']>=40-2*H)&(g['r']<=50+2*H))
    times=np.arange(1281)*.1; r=g['r'][indices]
    data={}; provenance=[]; scale=None
    for level,dt in LEVELS:
        data[level]={}
        requests=[(0,0.,old,args.observed_dir)]
        requests += [(0,e,old,args.observed_dir) for e in (LARGE,-LARGE)]
        requests += [(90,e,phase,args.phase_dir) for e in (LARGE,-LARGE)]
        if level=='base':
            requests += [(0,e,old,args.observed_dir) for e in (SMALL,-SMALL)]
        for angle,eps,source,directory in requests:
            checkpoint()
            rows=[a for a in source['arms'] if a['level']==level and a['epsilon']==eps]
            require(len(rows)==1, 'Saved arm absent/ambiguous')
            arm=rows[0]; samples=arm['samples']; meta=arm['initial']
            require(arm['complete'] and arm['h']==H and arm['dt']==dt and len(samples)==321,
                    'Saved arm incomplete/wrong discretization')
            require(np.allclose([d['t'] for d in samples],np.arange(321)*.4,rtol=0,atol=1e-12),
                    'Saved diagnostic times mismatch')
            if angle==90:
                require(arm['phase']==np.pi/2, 'Saved phase mismatch')
            for d in samples:
                pc.diagnostic_gate(d,samples[0]['E'],eps==0)
            require(meta['charge_identity_error']<1e-10 and meta['canonical_start_error']<1e-10,
                    'Saved adapter QA failure')
            if scale is None:
                scale=meta['reference_norm']
            require(meta['reference_norm']==scale and meta['alpha']==eps*scale,
                    'Saved canonical normalization mismatch')
            for key in ('initial_artifact','final_artifact'):
                checked(directory/arm[key]['file'],arm[key]['sha256'])
            fields=pc.read_ring(directory,arm['ring_artifact'],times,r,
                                (1281,4,len(r)),'rotating_fields')
            data[level][angle,eps]=fields
            provenance.append(dict(level=level,phase_degrees=angle,epsilon=eps,
                directory=str(directory),initial=meta,
                artifacts={k:arm[k] for k in ('initial_artifact','final_artifact','ring_artifact')}))
            if eps>0:
                if angle==0:
                    lev=[l for l in old['levels'] if l['level']==level]
                    require(len(lev)==1 and lev[0]['complete'],'Old pair level missing')
                    pairs=[p for p in lev[0]['pairs'] if p['epsilon']==eps]
                    require(len(pairs)==1 and pairs[0]['passed'] and pairs[0]['max_error']<.05,
                            'Saved full odd gate failure')
                else:
                    pairs=[p for p in phase['pairs'] if p['level']==level]
                    require(len(pairs)==1 and pairs[0]['complete'] and pairs[0]['odd_passed']
                            and pairs[0]['odd_max_error']<.05,'Saved quadrature odd gate failure')
    return times,r,indices,data,scale,provenance

# Pair evolution and measurement driver follow below.

def run_pair(args,result,pc,td,dyn,exc,mode,level,dt,angle,indices,scale):
    checkpoint()
    rotated=dict(mode); rotated['v']=mode['v']*(1j if angle==90 else 1.)
    omega=mode['reference'][2]; alpha=SMALL*scale
    arms={}; states={}; starts={}; first={}; flux={}; oldflux={}
    rings={e:np.empty((1281,4,len(indices)),complex) for e in (SMALL,-SMALL)}
    prefix=f'{level}-phase{angle}'
    for eps in (SMALL,-SMALL):
        g,state,meta=exc.initial(dyn,H,eps,mode['reference'],rotated)
        require(meta['alpha']==eps*scale and meta['reference_norm']==scale,
                'New canonical normalization mismatch')
        require(np.array_equal(g.r,mode['grid']['r']) and np.array_equal(g.vol,mode['grid']['vol']),
                'Evolution/operator grid mismatch')
        arm=dict(level=level,h=H,dt=dt,epsilon=eps,phase_degrees=angle,
                 initial=meta,samples=[],complete=False)
        arm['initial_artifact']=artifact(args.out,f'{prefix}-eps{eps:g}-initial.npz',
            r=g.r,phi=state[0],pi=state[1],chi=state[2],chi_t=state[3])
        result['arms'].append(arm); arms[eps]=arm; states[eps]=state
        starts[eps]=tuple(x.copy() for x in state); first[eps]=dyn.diagnose(g,state,starts[eps])
        flux[eps]=0.; oldflux[eps]=dyn.outward_flux(g,state[0]); save(args.out,result)
    pair=dict(level=level,dt=dt,phase_degrees=angle,complete=False,last_time=0.,
              odd_max_error=0.,odd_samples=[])
    result['pairs'].append(pair); save(args.out,result)
    root=np.sqrt(g.vol); norm=float(np.linalg.norm(rotated['v']))
    for step in range(round(T/dt)+1):
        t=step*dt
        if step%20==0:
            checkpoint()
            require(all(np.all(np.isfinite(x)) for s in states.values() for x in s),
                    'Nonfinite nonlinear state')
        if step%round(.1/dt)==0:
            for eps in (SMALL,-SMALL):
                rings[eps][step//round(.1/dt)]=td.rotating_ring(states[eps],omega,t,indices)
        if step%round(.4/dt)==0:
            for eps in (SMALL,-SMALL):
                d=dyn.diagnose(g,states[eps],starts[eps]); f=first[eps]
                d.update(t=t,Edrift=abs(d['E']/f['E']-1),Qdrift=abs(d['Q']/f['Q']-1),
                    balance=abs(d['Qcore']-f['Qcore']+flux[eps])/abs(f['Q']),flux_integral=flux[eps])
                pc.diagnostic_gate(d,f['E']); arms[eps]['samples'].append(d)
            odd=(exc.canonical(states[SMALL],omega,t,root)
                 -exc.canonical(states[-SMALL],omega,t,root))/(2*alpha)
            target=np.real(rotated['v']*np.exp(1j*mode['rho']*t))
            error=float(np.linalg.norm(odd-target)/norm)
            require(np.isfinite(error),'Nonfinite full odd norm')
            pair['odd_max_error']=max(pair['odd_max_error'],error)
            pair['odd_samples'].append(dict(t=t,error=error)); pair['last_time']=t
            if step%round(4/dt)==0:
                save(args.out,result)
        if step==round(T/dt):
            break
        for eps in (SMALL,-SMALL):
            states[eps]=dyn.advance(g,states[eps],dt)
            current=dyn.outward_flux(g,states[eps][0])
            flux[eps]+=.5*dt*(oldflux[eps]+current); oldflux[eps]=current
    for eps in (SMALL,-SMALL):
        s=states[eps]; arm=arms[eps]
        arm['final_artifact']=artifact(args.out,f'{prefix}-eps{eps:g}-final.npz',
            r=g.r,phi=s[0],pi=s[1],chi=s[2],chi_t=s[3])
        arm['ring_artifact']=artifact(args.out,f'{prefix}-eps{eps:g}-ring.npz',
            t=np.arange(1281)*.1,r=g.r[indices],rotating_fields=rings[eps],
            components=np.array(['phi','phi_t','chi','chi_t']))
        arm['complete']=True; save(args.out,result)
    pair.update(complete=True,odd_passed=pair['odd_max_error']<.05)
    save(args.out,result)
    require(pair['odd_passed'],'Full odd gate failed; no subsequent pair permitted')
    return rings


def differences(data,alpha):
    fields={}; hull={}
    for level,_ in LEVELS:
        d=data[level]; b=d[0,0.]; p={}; a={}
        for angle in (0,90):
            for eps in (SMALL,LARGE):
                p[angle,eps]=d[angle,eps]+d[angle,-eps]
                a[angle,eps]=abs(d[angle,eps][:,0])+abs(d[angle,-eps][:,0])
        numerator={angle:p[angle,LARGE]-4*p[angle,SMALL] for angle in (0,90)}
        envelope={angle:a[angle,LARGE]+4*a[angle,SMALL] for angle in (0,90)}
        # H is formed before any baseline subtraction, matching its baseline-free hull.
        fields[level]=np.stack(((numerator[0]+6*b)/(2*alpha**2),
                                (numerator[90]+6*b)/(2*alpha**2),
                                (numerator[0]+numerator[90]+12*b)/(4*alpha**2),
                                (numerator[0]-numerator[90])/(4*alpha**2)),axis=1)
        hull[level]=np.stack(((envelope[0]+6*abs(b[:,0]))/(2*alpha**2),
                              (envelope[90]+6*abs(b[:,0]))/(2*alpha**2),
                              (envelope[0]+envelope[90]+12*abs(b[:,0]))/(4*alpha**2),
                              (envelope[0]+envelope[90])/(4*alpha**2)),axis=1)
        require(np.all(np.isfinite(fields[level])) and np.all(np.isfinite(hull[level])),
                'Nonfinite amplitude difference/hull')
    return fields,hull


def analyse(td,split,mode,times,r,indices,fields,hull):
    rows=[]; vol=mode['grid']['vol'][indices]
    for wi,left in enumerate((88.,104.5)):
        checkpoint(); right=left+2*np.pi/mode['rho']; nu=2*mode['rho']
        interval={lev:split.interval(times,fields[lev],left,right) for lev,_ in LEVELS}
        ts=interval['base'][0]; weights=np.diff(ts)
        require(np.array_equal(ts,interval['time'][0]),'Interval times differ')
        band={lev:td.coefficient(times,fields[lev],left,right,nu) for lev,_ in LEVELS}
        positive={lev:split.interval(times,hull[lev],left,right)[1] for lev,_ in LEVELS}
        average={lev:td.coefficient(times,hull[lev],left,right,0.).real for lev,_ in LEVELS}
        for si,(lo,hi) in enumerate(td.SHELLS):
            mask=(r>=lo)&(r<hi); vv=vol[mask]
            require(np.any(mask),'Empty shell')
            def spatial(x):
                return float(np.sqrt(np.sum(vv*abs(x[mask])**2)))
            def temporal(x):
                density=np.sum(vv*abs(x[:,mask])**2,axis=1)
                return float(np.sqrt(np.sum(.5*(density[1:]+density[:-1])*weights)))
            for ci,name in enumerate(COMPONENTS):
                fine=interval['time'][1][:,ci,0]; coarse=interval['base'][1][:,ci,0]
                norms=dict(time=temporal(fine),band=spatial(band['time'][ci,0]))
                coarse_norms=dict(time=temporal(coarse),band=spatial(band['base'][ci,0]))
                change=dict(time=temporal(fine-coarse),band=spatial(band['time'][ci,0]-band['base'][ci,0]))
                factor=64*np.finfo(np.float64).eps
                eta_levels={lev:dict(time=factor*temporal(positive[lev][:,ci]),
                                    band=factor*spatial(average[lev][ci])) for lev,_ in LEVELS}
                eta={key:max(x[key] for x in eta_levels.values()) for key in ('time','band')}
                flags={key:bool(np.isfinite(norms[key]) and np.isfinite(change[key])
                           and np.isfinite(eta[key]) and norms[key]>10*change[key]
                           and norms[key]>100*eta[key]) for key in ('time','band')}
                rows.append(dict(component=name,time_window=wi,shell=si,window=[left,right],
                    radius_window=[lo,hi],fine_delta_norm=norms,coarse_delta_norm=coarse_norms,
                    delta_field_dt_difference=change,eta_by_level=eta_levels,eta=eta,
                    dt_reserve={k:10*x for k,x in change.items()},
                    arithmetic_reserve={k:100*x for k,x in eta.items()},flags=flags,
                    relative_dt_difference={k:td.ratio(change[k],norms[k]) for k in norms}))
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('phase-code','time-code','split-code','excitation','dynamics','operator',
                 'outgoing','response-code','reference','source-dir','prepared-dir',
                 'response-dir','search-dir','observed-dir','phase-dir','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',terminal_complete=False,code_sha256=sha(__file__),
        bound_hashes=dict(phase_code=PHASE_CODE,phase_result=PHASE_RESULT,time_code=TIME_CODE,
                          observed=OBSERVED,split_code=SPLIT_CODE),
        budget=dict(total_cpu_seconds=160,checkpoint_seconds=150,
                    external_cpu_seconds=159,external_wall_seconds=240),
        gates=dict(dt_reserve_factor=10,arithmetic_reserve_factor=100,arithmetic_factor=64,
                   odd=.05,energy_charge_balance=1e-5,collar=1e-8,baseline=.004,adapter=1e-10),
        arms=[],pairs=[],measurements=[],delta_artifacts=[],
        interpretation='Finite-amplitude difference on fixed h=.05; no order, continuum, stationarity or lifetime claim',
        arithmetic_interpretation='max of both dt positive summand envelopes times 64*float64eps; sensitivity only, not evolution roundoff certification')
    save(args.out,result)
    try:
        pc=module(args.phase_code,PHASE_CODE,'unchanged_phase_cycle')
        td=module(args.time_code,TIME_CODE,'unchanged_time_domain')
        split=module(args.split_code,SPLIT_CODE,'unchanged_interval_helper')
        exc=module(args.excitation,td.HASH['excitation'],'unchanged_excitation')
        dyn=module(args.dynamics,td.HASH['dynamics'],'unchanged_dynamics')
        op=module(args.operator,td.HASH['operator'],'unchanged_operator')
        out=module(args.outgoing,td.HASH['outgoing'],'unchanged_outgoing')
        response=module(args.response_code,td.HASH['response_code'],'unchanged_response_loader')
        result['dependency_hashes']=td.HASH
        checkpoint(); modes,metadata=td.load_inputs(args,op,out,response)
        result['inputs']=metadata; mode=modes[H]
        times,r,indices,data,scale,provenance=load_saved(args,pc,mode,metadata)
        result['saved_inputs']=provenance
        result['normalization']=dict(s=scale,alpha_small=SMALL*scale,alpha_large=LARGE*scale,
            theta90_multiplier=[0.,1.],renormalized=False,rho=mode['rho'],omega=mode['reference'][2])
        save(args.out,result)
        for level,dt,angle in (('base',.01,90),('time',.005,0),('time',.005,90)):
            rings=run_pair(args,result,pc,td,dyn,exc,mode,level,dt,angle,indices,scale)
            for eps in (SMALL,-SMALL):
                data[level][angle,eps]=rings[eps]
            del rings
        checkpoint(); fields,hull=differences(data,LARGE*scale)
        del data
        for level,_ in LEVELS:
            entry=artifact(args.out,f'{level}-amplitude-differences.npz',t=times,r=r,
                delta_fields=fields[level],phi_positive_summand_hull=hull[level],
                delta_components=np.array(COMPONENTS),field_components=np.array(['phi','phi_t','chi','chi_t']))
            result['delta_artifacts'].append(dict(level=level,artifact=entry)); save(args.out,result)
        result['measurements']=analyse(td,split,mode,times,r,indices,fields,hull)
        expected={(level,angle,eps) for level,angle in (('base',90),('time',0),('time',90))
                  for eps in (SMALL,-SMALL)}
        actual={(a['level'],a['phase_degrees'],a['epsilon']) for a in result['arms']}
        pair_keys={(p['level'],p['phase_degrees']) for p in result['pairs']}
        measurement_keys={(m['component'],m['time_window'],m['shell']) for m in result['measurements']}
        complete=(len(result['arms'])==6 and actual==expected
            and all(a['complete'] and len(a['samples'])==321 and a['samples'][-1]['t']==T for a in result['arms'])
            and len(result['pairs'])==3 and pair_keys=={('base',90),('time',0),('time',90)}
            and all(p['complete'] and p['last_time']==T and len(p['odd_samples'])==321 for p in result['pairs'])
            and len(result['measurements'])==16
            and measurement_keys=={(c,w,s) for c in COMPONENTS for w in (0,1) for s in (0,1)})
        require(complete,'Terminal six-arm/32-norm completeness failed')
        result['terminal_complete']=True
        result['all_odd_passed']=all(p['odd_passed'] for p in result['pairs'])
        result['resolved_norm_count']=sum(int(x) for m in result['measurements'] for x in m['flags'].values())
        passed=result['all_odd_passed'] and result['resolved_norm_count']==32
        result['status']='RESOLVED_AMPLITUDE_DIFFERENCE_ON_FIXED_GRID' if passed else 'UNRESOLVED'
    except Exception as error:
        result['status']='INCOMPLETE'; result['error']=repr(error)
    save(args.out,result)
    return 0 if result['status']=='RESOLVED_AMPLITUDE_DIFFERENCE_ON_FIXED_GRID' else 2


if __name__=='__main__':
    raise SystemExit(main())
