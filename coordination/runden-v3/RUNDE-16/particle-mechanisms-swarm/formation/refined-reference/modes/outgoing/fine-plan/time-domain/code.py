#!/usr/bin/env python3
"""Fixed nonlinear parity experiment; imported M2 Verlet, no fitted frequencies."""
import time
START = time.process_time()
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

HASH = dict(excitation='1af408e1269a53036c080ec820e750940d5f8b70ac41c32e457e5ad531dc5bc1',
 dynamics='466b25fb813770a1ab13eea962c93b39308dfe1ad22171fe638c60fdafef998d',
 operator='467ad3e19cd8efcdac4ec2dcc670b50aaa59cc6f7e9e44d625ebbf94ba0d32c6',
 outgoing='75b1dce542aa728fe6bf58ecea4aec4a2ddf8a6a5a6e236666075c6902bbd292',
 response_code='ab9d00726e8f4fc6d4c7f839610d274609cf481485f6312776558cb672558e06',
 prepared='0c148cf401d6bca109dc311401df1ea59b4b6d10b4ffb919ec1589c8b0b769da',
 response='2cd3dfc3b9d1d2a315daeb8be9c0661a8358c10e2879189202157708cb04ca5a',
 search='77ecf9bbe03b96db901d76728e074a897725eb52213f90dae76c7200ba5364ea')
LEVELS = (('base', .05, .01, (.001, .002)), ('space', .025, .01, (.002,)),
          ('time', .05, .005, (.002,)))
T = 128.
SHELLS = ((40., 45.), (45., 50.))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked(path, expected):
    if sha(path) != expected:
        raise ValueError('Provenance mismatch: ' + str(path))
    return path


def module(path, expected, name):
    checked(path, expected)
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec); spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time()-START >= 280:
        raise RuntimeError('INCOMPLETE: 280 CPU-s checkpoint')


def save(directory, result):
    result['cpu_seconds'] = time.process_time()-START
    tmp = directory/'RESULT.tmp'
    tmp.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    tmp.replace(directory/'RESULT.json')


def artifact(directory, filename, **arrays):
    path = directory/filename
    np.savez_compressed(path, **arrays)
    return dict(file=filename, sha256=sha(path))


def cjson(value):
    return [float(np.real(value)), float(np.imag(value))]


def ratio(num, den):
    return float(num/den) if den > 0 and np.isfinite(num) and np.isfinite(den) else None


def below(x, gate):
    return x is not None and x < gate


def coefficient(times, values, left, right, frequency):
    """Trapezoid on modulated samples, exact off-grid window endpoints."""
    def endpoint(t):
        j = int(np.searchsorted(times, t))
        if j < len(times) and abs(times[j]-t) < 1e-12:
            return values[j]
        if j == 0 or j == len(times):
            raise ValueError('Window outside stored time range')
        a = (t-times[j-1])/(times[j]-times[j-1])
        return (1-a)*values[j-1]+a*values[j]
    inside = (times > left) & (times < right)
    ts = np.r_[left, times[inside], right]
    ys = np.concatenate((endpoint(left)[None], values[inside], endpoint(right)[None]), axis=0)
    phase = np.exp(-1j*frequency*ts).reshape((-1,)+(1,)*(ys.ndim-1))
    integrand = ys*phase
    weights = np.diff(ts).reshape((-1,)+(1,)*(ys.ndim-1))
    return np.sum(.5*(integrand[1:]+integrand[:-1])*weights, axis=0)/(right-left)


def extraction_qa(rho):
    times = np.arange(1281)*.1; nu = 2*rho
    windows = [(start, start+2*np.pi/rho) for start in (88., 104.5)]
    rows = []
    for left, right in windows:
        leak = []
        for frequency in (0., rho, -rho, nu, -nu):
            measured = coefficient(times, np.exp(1j*frequency*times), left, right, nu)
            leak.append(float(abs(measured-(1 if frequency == nu else 0))))
        rows.append(dict(window=[left, right], basis_frequencies=[0.,rho,-rho,nu,-nu], errors=leak,
                         passed=max(leak)<1e-4))
    return rows


def response_extraction_qa(answer, rho, windows):
    """Actual stationary ring fields through the identical tensor extraction path."""
    times=np.arange(1281)*.1; nu=2*rho
    positive=np.array([answer[0],1j*nu*answer[0],answer[2],1j*nu*answer[2]])
    negative=np.array([np.conj(answer[1]),-1j*nu*np.conj(answer[1]),
                       np.conj(answer[2]),-1j*nu*np.conj(answer[2])])
    wave=np.exp(1j*nu*times)[:,None,None]
    samples=wave*positive[None]+np.conj(wave)*negative[None]
    errors=[]
    for window in windows:
        left,right=window['window']
        measured=coefficient(times,samples,left,right,nu)
        errors.append(float(np.linalg.norm(measured-positive)/np.linalg.norm(positive)))
    return dict(relative_errors=errors,passed=max(errors)<1e-4)


def load_inputs(args, op, out, response):
    prepared_path = args.prepared_dir/'RESULT.json'
    profiles, prepared = response.load_prepared(prepared_path, HASH['prepared'], op, out,
                                               args.reference, args.source_dir)
    results = json.loads(checked(args.response_dir/'RESULT.json', HASH['response']).read_text())
    search = json.loads(checked(args.search_dir/'RESULT.json', HASH['search']).read_text())
    if results['status'] != 'CONTROLLED_FINE_FORCED_RESPONSE':
        raise ValueError('Stationary response status mismatch')
    found = {}; provenance = []
    for h in (.05, .025):
        f, c, omega, nu, source, _ = profiles[h]
        if h == .05:
            rows = [x for x in search['tasks'] if x['R']==120 and x['h']==h and x['shift']==.3]
            if len(rows)!=1 or not rows[0]['complete']:
                raise ValueError('Old Ritz task missing')
            task = rows[0]; ritzpath = args.search_dir/task['artifact']; digest = task['artifact_sha256']
            if digest != prepared['old_inputs']['source_profile']['ritz_sha256']:
                raise ValueError('Old Ritz/source mismatch')
        else:
            task = prepared['ritz_task']; rr = task['artifact']
            ritzpath = args.prepared_dir/rr['file']; digest = rr['sha256']
        checked(ritzpath, digest)
        with np.load(ritzpath, allow_pickle=False) as z:
            values = z['eigenvalues']; ix = np.flatnonzero((values.imag>.38)&(values.imag<.39))
            if len(ix)!=1:
                raise ValueError('Ritz selection ambiguous')
            j=int(ix[0]); value=values[j]; v=z['eigenvectors'][:,j].copy()
        g=op.grid(120.,h); n=g['n']
        if (len(v)!=6*n or not np.all(np.isfinite(v)) or
            value.imag!=nu/2 or abs(value.imag-task['ritz'][j]['rho'])>1e-12 or
            abs(value.real-task['ritz'][j]['lambda_real'])>1e-12):
            raise ValueError('Ritz shape/frequency/row mismatch')
        v/=np.linalg.norm(v[:3*n]); pivot=int(np.argmax(abs(v[:3*n])))
        phase=np.exp(-1j*np.angle(v[pivot])); v*=phase
        rows=[x for x in results['cases'] if x['R']==120 and x['h']==h]
        if len(rows)!=1 or not rows[0]['passed'] or not all(rows[0]['flags'].values()):
            raise ValueError('Stationary response missing')
        row=rows[0]; path=args.response_dir/row['artifact']; checked(path,row['artifact_sha256'])
        with np.load(path,allow_pickle=False) as z:
            if (not np.array_equal(z['r'],g['r']) or float(z['omega'])!=omega or float(z['nu'])!=nu or
                not np.array_equal(z['source_channels'],source)):
                raise ValueError('Stationary answer/source grid mismatch')
            answer=z['answer_channels'].copy()*phase**2
        if not np.all(np.isfinite(answer)):
            raise ValueError('Nonfinite stationary answer')
        qa=extraction_qa(nu/2)
        if not all(r['passed'] for r in qa):
            raise ValueError('Fixed-window extraction QA failed')
        ring=(g['r']>=40-2*h)&(g['r']<=50+2*h)
        response_qa=response_extraction_qa(answer[:,ring],nu/2,qa)
        if not response_qa['passed']:
            raise ValueError('Stored full response extraction QA failed')
        check=op.profile_check(g,f,c,omega,1100.)
        if not check['passed']:
            raise ValueError('Profile/phase initial gate failed')
        found[h]=dict(v=v,rho=float(nu/2),reference=(f,c,omega),answer=answer,grid=g,qa=qa)
        provenance.append(dict(h=h,ritz_sha256=digest,response_sha256=row['artifact_sha256'],
                               phase=cjson(phase),pivot=pivot,profile_check=check,extraction_qa=qa,
                               stationary_response_extraction_qa=response_qa))
    return found,provenance


def flux_arrays(r,h,p,velocity):
    face=.5*(r[:-1]+r[1:]); gradient=np.diff(p)/h
    middle=.5*(p[:-1]+p[1:]); v=.5*(velocity[:-1]+velocity[1:])
    area=4*np.pi*face**2
    return face, -2*area*np.imag(np.conj(middle)*gradient), -2*area*np.real(np.conj(v)*gradient)


def flux_qa(h,omega,nu):
    r=(np.arange(int(round(10.2/h)))+.5)*h+39.9
    k=np.sqrt((omega+nu)**2-2); p=np.exp(-1j*k*r)/r
    _,fq,fe=flux_arrays(r,h,p,1j*(omega+nu)*p)
    qexact=8*np.pi*k; eexact=(omega+nu)*qexact
    errq=float(np.max(abs(fq/qexact-1))); erre=float(np.max(abs(fe/eexact-1)))
    _,qin,ein=flux_arrays(r,h,np.conj(p),1j*(omega+nu)*np.conj(p))
    return dict(charge_relative_error=errq,energy_relative_error=erre,
                incoming_negative=bool(np.all(qin<0)&np.all(ein<0)),
                passed=bool(max(errq,erre)<1e-3 and np.all(qin<0) and np.all(ein<0)))


def rotating_ring(state,omega,t,indices):
    p,v,c,w=state; phase=np.exp(-1j*omega*t); rp=p[indices]*phase
    return np.array([rp,v[indices]*phase-1j*omega*rp,c[indices],w[indices]],dtype=complex)


def run_level(args,result,dyn,exc,level,h,dt,epsilons,mode):
    """All states on a level in lockstep; no full spatial time histories."""
    checkpoint(); f,c,omega=mode['reference']; arms={}; states={}; starts={}; flux={}; oldflux={}
    order=(0.,)+tuple(e for positive in epsilons for e in (positive,-positive))
    for eps in order:
        g,state,meta=exc.initial(dyn,h,eps,mode['reference'],mode)
        arm=dict(level=level,h=h,dt=dt,epsilon=eps,initial=meta,samples=[],complete=False)
        arm['initial_artifact']=artifact(args.out,f'{level}-eps{eps:g}-initial.npz',r=g.r,
                                        phi=state[0],pi=state[1],chi=state[2],chi_t=state[3])
        result['arms'].append(arm); arms[eps]=arm; states[eps]=state
        starts[eps]=tuple(x.copy() for x in state); flux[eps]=0.
        oldflux[eps]=dyn.outward_flux(g,state[0]); save(args.out,result)
    # Two extra cell centres give central derivatives throughout both physical shells.
    indices=np.flatnonzero((g.r>=40-2*h)&(g.r<=50+2*h))
    r=g.r[indices]; times=np.arange(1281)*.1
    rings={eps:np.empty((len(times),4,len(indices)),dtype=complex) for eps in order}
    initial_diag={eps:dyn.diagnose(g,states[eps],starts[eps]) for eps in order}
    root=np.sqrt(g.vol); norm=float(np.linalg.norm(mode['v']))
    odd={eps:dict(epsilon=eps,max_error=0.,samples=[]) for eps in epsilons}
    series=dict(level=level,h=h,dt=dt,pairs=list(odd.values()),complete=False)
    result['levels'].append(series); save(args.out,result)
    sample=round(.1/dt); qa_every=round(.4/dt); total=round(T/dt)
    for step in range(total+1):
        t=step*dt
        if step%20==0:
            checkpoint()
            if not all(np.all(np.isfinite(x)) for state in states.values() for x in state):
                raise ValueError('Nonfinite nonlinear state')
        if step%sample==0:
            j=step//sample
            for eps in order:
                rings[eps][j]=rotating_ring(states[eps],omega,t,indices)
        if step%qa_every==0:
            for eps in order:
                d=dyn.diagnose(g,states[eps],starts[eps]); first=initial_diag[eps]
                d.update(t=t,Edrift=abs(d['E']/first['E']-1),Qdrift=abs(d['Q']/first['Q']-1),
                         balance=abs(d['Qcore']-first['Qcore']+flux[eps])/abs(first['Q']),flux_integral=flux[eps])
                arms[eps]['samples'].append(d)
                if max(d['Edrift'],d['Qdrift'],d['balance'])>1e-5 or d['collar']/first['E']>1e-8:
                    save(args.out,result); raise ValueError('Energy/charge/collar QA failed')
                if eps==0 and any(d[k]>=.004 for k in ('rphi','rchi','tphi','tchi','driftphi','driftchi')):
                    save(args.out,result); raise ValueError('Baseline stationarity QA failed')
            target=np.real(mode['v']*np.exp(1j*mode['rho']*t))
            for eps in epsilons:
                alpha=arms[eps]['initial']['alpha']
                u=(exc.canonical(states[eps],omega,t,root)-exc.canonical(states[-eps],omega,t,root))/(2*alpha)
                err=float(np.linalg.norm(u-target)/norm)
                odd[eps]['max_error']=max(odd[eps]['max_error'],err)
                odd[eps]['samples'].append(dict(t=t,error=err))
            if step%round(4/dt)==0:
                series['last_time']=t; save(args.out,result)
        if step==total:
            break
        for eps in order:
            states[eps]=dyn.advance(g,states[eps],dt)
            current=dyn.outward_flux(g,states[eps][0]); flux[eps]+=.5*dt*(oldflux[eps]+current); oldflux[eps]=current
    for eps in order:
        checkpoint(); state=states[eps]
        arms[eps]['final_artifact']=artifact(args.out,f'{level}-eps{eps:g}-final.npz',r=g.r,
                                           phi=state[0],pi=state[1],chi=state[2],chi_t=state[3])
        arms[eps]['ring_artifact']=artifact(args.out,f'{level}-eps{eps:g}-ring.npz',t=times,r=r,
                                           rotating_fields=rings[eps],components=np.array(['phi','phi_t','chi','chi_t']))
        arms[eps]['complete']=True; save(args.out,result)
    records=[]
    for eps in epsilons:
        checkpoint(); alpha=arms[eps]['initial']['alpha']
        even=(rings[eps]+rings[-eps]-2*rings[0])/(2*alpha*alpha)
        pairrecords=analyse_pair(g,indices,times,even,mode,level,eps,alpha)
        odd[eps]['passed']=odd[eps]['max_error']<.05
        records.extend(pairrecords)
        result['measurements'].extend(pairrecords); save(args.out,result)
    series['complete']=True; save(args.out,result)
    return records


def analyse_pair(g,indices,times,even,mode,level,epsilon,alpha):
    r=g.r[indices]; vol=g.vol[indices]; h=g.h; omega=mode['reference'][2]; nu=2*mode['rho']
    k=np.sqrt((omega+nu)**2-2); answer=mode['answer'][:,indices]
    target=np.array([answer[0],1j*nu*answer[0],answer[2],1j*nu*answer[2]])
    records=[]
    for wi,qa in enumerate(mode['qa']):
        left,right=qa['window']; measured=coefficient(times,even,left,right,nu)
        neg=coefficient(times,even,left,right,-nu); dc=coefficient(times,even,left,right,0.)
        fundamental=[coefficient(times,even,left,right,s*mode['rho']) for s in (1,-1)]
        p=measured[0]; derivative=np.gradient(r*p,h,edge_order=2)
        ao=np.exp(1j*k*r)*(r*p+1j*derivative/k)/2
        ai=np.exp(-1j*k*r)*(r*p-1j*derivative/k)/2
        tp=target[0]; td=np.gradient(r*tp,h,edge_order=2)
        tao=np.exp(1j*k*r)*(r*tp+1j*td/k)/2
        face,fq,fe=flux_arrays(r,h,p,measured[1]+1j*omega*p)
        _,tfq,tfe=flux_arrays(r,h,tp,target[1]+1j*omega*tp)
        for si,(lo,hi) in enumerate(SHELLS):
            mask=(r>=lo)&(r<hi); fm=(face>=lo)&(face<hi)
            norm=lambda x:float(np.sqrt(np.sum(vol[mask]*abs(x[mask])**2)))
            targetnorm=norm(tp); err=ratio(norm(p-tp),targetnorm)
            a=complex(np.mean(ao[mask])); at=complex(np.mean(tao[mask]))
            incoming=ratio(float(np.linalg.norm(ai[mask])),float(np.linalg.norm(ao[mask])))
            # Absolute leakage reserve uses actual DC/first/second/negative coefficients.
            # Linear extraction errors are applied to the same Aout spatial operator.
            basis_coeffs=[dc[0],fundamental[0][0],fundamental[1][0],measured[0],neg[0]]
            leakage=0.
            for error,basis in zip(qa['errors'],basis_coeffs):
                deriv=np.gradient(r*basis,h,edge_order=2)
                bound=np.abs((r*basis+1j*deriv/k)/2)
                leakage+=error*float(np.max(bound[mask]))
            energy=float(np.mean(fe[fm])); energy_target=float(np.mean(tfe[fm]))
            charge=float(np.mean(fq[fm])); charge_target=float(np.mean(tfq[fm]))
            flux_error=ratio(abs(energy-energy_target),abs(energy_target))
            row=dict(level=level,h=h,epsilon=epsilon,alpha=alpha,time_window=wi,window=[left,right],
                     shell=si,radius_window=[lo,hi],Aout=cjson(a),Aout_target=cjson(at),
                     Aout_abs=abs(a),target_abs=abs(at),incoming_ratio=incoming,
                     plus_complex_relative_error=err,scaled_plus_E_flux=energy,
                     scaled_plus_Q_flux=charge,scaled_plus_rot_flux=energy-omega*charge,
                     target_E_flux=energy_target,target_Q_flux=charge_target,
                     physical_even_band_E_flux=alpha**4*energy,flux_relative_error=flux_error,
                     extraction_leakage_Aout=leakage,
                     target_plus_L2=targetnorm,
                     DC_phi_norm=norm(dc[0]),first_harmonic_phi_norms=[norm(x[0]) for x in fundamental],
                     negative_phi_absolute_error=norm(neg[0]-np.conj(answer[1])),
                     chi_positive_absolute_error=norm(measured[2]-answer[2]),
                     negative_error_over_plus_target=ratio(norm(neg[0]-np.conj(answer[1])),targetnorm),
                     chi_error_over_plus_target=ratio(norm(measured[2]-answer[2]),targetnorm),
                     velocity_positive_absolute_error=norm(measured[1]-target[1]))
            row['flags']=dict(complex_field=below(err,.10),incoming=below(incoming,.10),
                              band_flux=below(flux_error,.20))
            records.append(row)
    return records


def compare(result):
    rows=result['measurements']; expected={(lev,ep,w,s) for lev,_,_,eps in LEVELS for ep in eps for w in (0,1) for s in (0,1)}
    bykey={(r['level'],r['epsilon'],r['time_window'],r['shell']):r for r in rows}
    if len(rows)!=len(expected) or set(bykey)!=expected:
        raise ValueError('Incomplete/duplicate measurement structure')
    changes=[]; checks=[]
    def add(kind,left,right,limit,complex_difference):
        av=complex(*left['Aout']); bv=complex(*right['Aout'])
        difference=abs(av-bv) if complex_difference else abs(abs(av)-abs(bv))
        relative=ratio(difference,right['target_abs']); changes.append(difference)
        checks.append(dict(kind=kind,left=[left['level'],left['epsilon'],left['time_window'],left['shell']],
                           right=[right['level'],right['epsilon'],right['time_window'],right['shell']],
                           absolute_change=difference,relative=relative,
                           complex_difference_descriptive=cjson(av-bv),passed=below(relative,limit)))
    for level,_,_,epsilons in LEVELS:
        for eps in epsilons:
            for s in (0,1):
                add('late_windows',bykey[(level,eps,0,s)],bykey[(level,eps,1,s)],.10,True)
    for w in (0,1):
        for s in (0,1):
            base=bykey[('base',.002,w,s)]
            add('h_magnitude',bykey[('space',.002,w,s)],base,.05,False)
            add('dt_magnitude',bykey[('time',.002,w,s)],base,.05,False)
            low=bykey[('base',.001,w,s)]
            add('amplitude_magnitude',base,low,.10,False)
            ratio_expected=(base['alpha']/low['alpha'])**4
            actual=ratio(base['physical_even_band_E_flux'],low['physical_even_band_E_flux'])
            error=None if actual is None else abs(actual/ratio_expected-1)
            checks.append(dict(kind='quartic_even_band_flux',time_window=w,shell=s,
                               measured_ratio=actual,expected_ratio=ratio_expected,relative_error=error,
                               passed=below(error,.20)))
    reserve=5*max(changes+[r['extraction_leakage_Aout'] for r in rows])
    for row in rows:
        row['signal_reserve']=reserve
        row['flags']['resolved']=row['target_abs']>reserve
        row['passed']=all(row['flags'].values())
    result['comparisons']=checks; result['signal_reserve']=reserve
    levels=result['levels']; arms=result['arms']
    expected_arms={(lev,ep) for lev,_,_,eps in LEVELS for ep in (0.,)+tuple(x for e in eps for x in (e,-e))}
    complete=(len(arms)==11 and {(a['level'],a['epsilon']) for a in arms}==expected_arms and
              all(a['complete'] and len(a['samples'])==321 and a['samples'][-1]['t']==128 for a in arms) and
              len(levels)==3 and all(l['complete'] for l in levels))
    odd=all(p['passed'] for l in levels for p in l['pairs'])
    return complete and odd and all(r['passed'] for r in rows) and all(c['passed'] for c in checks)


def main():
    parser=argparse.ArgumentParser()
    for name in ('excitation','dynamics','operator','outgoing','response-code','reference',
                 'source-dir','prepared-dir','response-dir','search-dir','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',code_sha256=sha(__file__),bound_hashes=HASH,
                arms=[],levels=[],measurements=[],
                interpretation='Finite-time free nonlinear parity-even second band; no lifetime or old-status reclassification')
    save(args.out,result)
    try:
        exc=module(args.excitation,HASH['excitation'],'existing_excitation')
        dyn=module(args.dynamics,HASH['dynamics'],'existing_nonlinear_dynamics')
        op=module(args.operator,HASH['operator'],'existing_operator')
        out=module(args.outgoing,HASH['outgoing'],'existing_outgoing')
        response=module(args.response_code,HASH['response_code'],'existing_response_loader')
        modes,meta=load_inputs(args,op,out,response); result['inputs']=meta
        result['flux_qa']=[]
        for h in (.05,.025):
            qa=flux_qa(h,modes[h]['reference'][2],2*modes[h]['rho']); qa['h']=h
            result['flux_qa'].append(qa)
            if not qa['passed']:
                raise ValueError('Local harmonic flux QA failed')
        save(args.out,result)
        for level,h,dt,eps in LEVELS:
            checkpoint(); run_level(args,result,dyn,exc,level,h,dt,eps,modes[h])
        checkpoint()
        result['status']='CONTROLLED_NONLINEAR_SECOND_BAND_IN_FIXED_WINDOWS' if compare(result) else 'UNRESOLVED'
    except Exception as exc:
        result['error']=repr(exc)
        result['status']='INCOMPLETE' if isinstance(exc,RuntimeError) else 'UNRESOLVED'
    save(args.out,result)
    return 0 if result['status']=='CONTROLLED_NONLINEAR_SECOND_BAND_IN_FIXED_WINDOWS' else 2


if __name__=='__main__':
    raise SystemExit(main())
