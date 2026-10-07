#!/usr/bin/env python3
"""Nine prescribed nonlinear M2 excitation arms using the existing Verlet only."""
import time
START=time.process_time()
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

DYNAMICS_HASH='466b25fb813770a1ab13eea962c93b39308dfe1ad22171fe638c60fdafef998d'
OPERATOR_HASH='467ad3e19cd8efcdac4ec2dcc670b50aaa59cc6f7e9e44d625ebbf94ba0d32c6'
RESULT_HASH='77ecf9bbe03b96db901d76728e074a897725eb52213f90dae76c7200ba5364ea'
RITZ_HASH={.1:'868230c0e14a68ebe754cabeac833cf2aaf63cfec86d5026e949f506990f6cae',
           .05:'67658ad2e278e7708e82039ae1b487f86d86ef666e42198ea3752bf765e4fbed'}
LEVELS=(('base',.1,.01),('space',.05,.01),('time',.1,.005))
EPSILONS=(0.,.001,.002)
T=32.


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def imported(path,expected,name):
    if sha(path)!=expected: raise ValueError('Module provenance mismatch: '+name)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def checkpoint():
    if time.process_time()-START>=40:
        raise RuntimeError('INCOMPLETE: 40 CPU-s checkpoint')


def save(out,result):
    result['cpu_seconds']=time.process_time()-START
    temp=out/'RESULT.tmp'
    temp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    temp.replace(out/'RESULT.json')


def modes(directory,refs,operator):
    path=directory/'RESULT.json'
    if sha(path)!=RESULT_HASH: raise ValueError('Search result hash mismatch')
    result=json.loads(path.read_text()); found={}; metadata=[]
    if result['code_sha256']!=OPERATOR_HASH: raise ValueError('Search operator mismatch')
    if refs[-1]['manifest_sha256']!=result['reference']['manifest_sha256']:
        raise ValueError('Reference/search manifest mismatch')
    for h in (.1,.05):
        tasks=[t for t in result['tasks'] if t['R']==120. and t['h']==h and t['shift']==.3]
        if len(tasks)!=1 or not tasks[0]['complete']: raise ValueError('Ritz task missing')
        task=tasks[0]; file=directory/task['artifact']; digest=sha(file)
        if digest!=RITZ_HASH[h] or digest!=task['artifact_sha256']:
            raise ValueError('Ritz source mismatch')
        with np.load(file,allow_pickle=False) as z:
            ev=z['eigenvalues']; ix=np.flatnonzero((ev.imag>.38)&(ev.imag<.39))
            if len(ix)!=1: raise ValueError('Ritz selection not unique')
            j=int(ix[0]); value=ev[j]; v=z['eigenvectors'][:,j].copy()
        if abs(value.imag-task['ritz'][j]['rho'])>1e-12 or abs(value.real-task['ritz'][j]['lambda_real'])>1e-12:
            raise ValueError('Ritz JSON ordering mismatch')
        g=operator.grid(120.,h); n=g['n']
        if len(v)!=6*n or not np.all(np.isfinite(v)): raise ValueError('Invalid Ritz vector')
        v/=np.linalg.norm(v[:3*n])
        pivot=int(np.argmax(abs(v[:3*n]))); phase=np.exp(-1j*np.angle(v[pivot])); v*=phase
        cross_diagnostic=None
        if h==.05:
            coarse=operator.grid(120.,.1)
            mapped,_=operator.restrict(v[:3*n],g,coarse)
            cross=np.vdot(found[.1]['v'][:3*coarse['n']],mapped)
            if abs(cross)==0: raise ValueError('Cross-grid phase overlap vanished')
            cross_diagnostic=dict(real=float(cross.real),imag=float(cross.imag),
                                  phase=float(np.angle(cross)))
        basis=np.column_stack((v.real,-v.imag)); gram=basis.T@basis
        condition=float(np.linalg.cond(gram))
        if condition>=1e8: raise ValueError('Modal projection Gram ill-conditioned')
        found[h]=dict(v=v,rho=float(value.imag),basis=basis,gram=gram,grid=g)
        metadata.append(dict(h=h,file=str(file),sha256=digest,rho=float(value.imag),
             lambda_real=float(value.real),phase_real=float(phase.real),phase_imag=float(phase.imag),
             pivot=pivot,gram_condition=condition,cross_grid_overlap=cross_diagnostic))
    return found,metadata


def initial(dyn,h,epsilon,reference,mode):
    g=dyn.Grid(h); f,c,omega=reference
    root=np.sqrt(g.vol); n=g.n; v=mode['v']
    x,y,z,px,py,pz=v.real.reshape(6,n)/root
    scale=float(np.sqrt(np.sum(g.vol*(2*f*f+(c-1)**2))))
    alpha=epsilon*scale
    a=(x+1j*y)/np.sqrt(2); b=(px+1j*py)/np.sqrt(2)
    phi=f+alpha*a; pi=1j*omega*phi+alpha*b
    state=(phi,pi,c+alpha*z,alpha*pz)
    q1=float(np.sqrt(2)*np.sum(g.vol*f*(2*omega*x+py)))
    q2=float(2*np.sum(g.vol*np.imag(np.conj(a)*(1j*omega*a+b))))
    qb=float(2*omega*np.sum(g.vol*f*f)); q=dyn.charge(g,*state[:2])
    predicted=alpha*q1+alpha*alpha*q2
    identity_error=abs(q-qb-predicted)/1100
    if identity_error>=1e-10: raise ValueError('Adapter quadratic charge identity failed')
    baseline=(f.astype(complex),1j*omega*f,c.copy(),np.zeros(n))
    # Canonical field/momentum reconstruction at t0 independently compared with Re(v).
    obtained=canonical(state,omega,0,root)-canonical(baseline,omega,0,root)
    expected=alpha*v.real
    adapter_error=float(np.linalg.norm(obtained-expected)/max(1,np.linalg.norm(expected)))
    if adapter_error>=1e-10: raise ValueError('Adapter canonical start identity failed')
    meta=dict(epsilon=epsilon,reference_norm=scale,alpha=alpha,deltaQ1=q1,deltaQ2=q2,
        actual_Q_change=q-qb,predicted_Q_change=predicted,charge_identity_error=identity_error,
        canonical_start_error=adapter_error,Q_initial=q,E_initial=dyn.energy(g,state),
        E_baseline=dyn.energy(g,baseline),real_position_norm=float(alpha*np.linalg.norm(v[:3*n].real)))
    return g,state,meta


def canonical(state,omega,t,root):
    phi,pi,chi,ct=state
    rotating=phi*np.exp(-1j*omega*t)
    velocity=pi*np.exp(-1j*omega*t)-1j*omega*rotating
    return np.concatenate((np.sqrt(2)*root*rotating.real,np.sqrt(2)*root*rotating.imag,
                           root*chi,np.sqrt(2)*root*velocity.real,np.sqrt(2)*root*velocity.imag,root*ct))


def residual_diagnostics(z,mode,t):
    v=mode['v']; rho=mode['rho']; norm=float(np.linalg.norm(v))
    target=np.real(v*np.exp(1j*rho*t)); difference=z-target
    coefficients=np.linalg.solve(mode['gram'],mode['basis'].T@z)
    target_coeff=np.array([np.cos(rho*t),np.sin(rho*t)])
    block=difference.reshape(6,-1); blockz=z.reshape(6,-1)
    return dict(linear_error=float(np.linalg.norm(difference)/norm),
                component_errors=(np.linalg.norm(block,axis=1)/norm).tolist(),
                component_norms=np.linalg.norm(blockz,axis=1).tolist(),
                projection_coefficients=coefficients.tolist(),
                projection_error=float(np.linalg.norm(coefficients-target_coeff)))


def run_arm(dyn,op,out,result,level,h,dt,epsilon,refs,mode,baseline_samples,active):
    g,state,meta=initial(dyn,h,epsilon,refs[h],mode)
    omega=refs[h][2]; root=np.sqrt(g.vol); start=tuple(x.copy() for x in state)
    arm=dict(level=level,h=h,dt=dt,epsilon=epsilon,initial=meta,samples=[],complete=False)
    initialfile=out/f'{level}-epsilon{epsilon:g}-initial.npz'
    np.savez_compressed(initialfile,r=g.r,phi=state[0],pi=state[1],chi=state[2],chi_t=state[3])
    arm['initial_artifact']=initialfile.name; arm['initial_sha256']=sha(initialfile)
    result['arms'].append(arm); save(out,result)
    first=dyn.diagnose(g,state,start); q_initial=first['Q']; e_initial=first['E']
    if epsilon==0 and any(first[k]>=.004 for k in ('rphi','rchi','tphi','tchi')):
        raise ValueError('Initial baseline stationarity gate failed')
    flux=0.; oldflux=dyn.outward_flux(g,state[0]); sample_every=round(.4/dt)
    frames=[]; scaled=[]; diagnostics=[]
    total_steps=round(T/dt)
    for step in range(total_steps+1):
        active.update(state=state,t=step*dt,level=level,epsilon=epsilon,r=g.r)
        if step%20==0:
            checkpoint()
            if not all(np.all(np.isfinite(x)) for x in state): raise ValueError('Nonfinite nonlinear state')
        if step%sample_every==0:
            t=step*dt; d=dyn.diagnose(g,state,start)
            d.update(t=t,flux_integral=flux,Edrift=abs(d['E']/e_initial-1),
                     Qdrift=abs(d['Q']/q_initial-1),
                     balance=abs(d['Qcore']-first['Qcore']+flux)/abs(q_initial))
            arm['samples'].append(d)
            if max(d['Edrift'],d['Qdrift'],d['balance'])>1e-5:
                raise ValueError('Energy/charge/flux gate failed')
            if d['collar']/e_initial>1e-8: raise ValueError('Collar gate failed')
            if epsilon==0 and any(d[k]>=.004 for k in ('rphi','rchi','tphi','tchi','driftphi','driftchi')):
                raise ValueError('Baseline control gate failed')
            current=canonical(state,omega,t,root)
            if epsilon==0:
                frames.append(current)
            else:
                j=len(arm['samples'])-1
                z=(current-baseline_samples[j])/meta['alpha']; scaled.append(z)
                zd=residual_diagnostics(z,mode,t)
                n=g.n; f=refs[h][0]
                zd['linear_deltaQ']=float(np.sqrt(2)*np.sum(root*f*(2*omega*z[:n]+z[4*n:5*n])))
                zd['t']=t; diagnostics.append(zd)
                d['mode_response']=zd
            if len(arm['samples'])%8==0: save(out,result)
        if step==total_steps: break
        state=dyn.advance(g,state,dt)
        newflux=dyn.outward_flux(g,state[0]); flux+=.5*dt*(oldflux+newflux); oldflux=newflux
    arm['complete']=True
    file=out/f'{level}-epsilon{epsilon:g}-final.npz'
    np.savez_compressed(file,r=g.r,phi=state[0],pi=state[1],chi=state[2],chi_t=state[3])
    arm['final_artifact']=file.name; arm['final_sha256']=sha(file)
    if epsilon>0:
        errors=[d['linear_error'] for d in diagnostics]
        arm['max_linear_error']=max(errors); arm['final_linear_error']=errors[-1]
    save(out,result)
    return np.array(frames) if epsilon==0 else (np.array(scaled),diagnostics)


def comparisons(op,responses,mode_by_h):
    summary={}; perlevel={}
    for level,h,dt in LEVELS:
        one,diagone=responses[level][.001]; two,diagtwo=responses[level][.002]
        norm=np.linalg.norm(mode_by_h[h]['v'])
        amp=np.linalg.norm(two-one,axis=1)/norm
        errors={str(eps):np.array([d['linear_error'] for d in responses[level][eps][1]]) for eps in (.001,.002)}
        perlevel[level]=(amp,errors)
        summary[level]=dict(amplitude_difference=amp.tolist(),max_amplitude_difference=float(np.max(amp)),
                            linear_errors={k:v.tolist() for k,v in errors.items()})
    sensitivity={}
    for level,h in (('space',.05),('time',.1)):
        amp,err=perlevel[level]; amp0,err0=perlevel['base']
        row=dict(amplitude_diagnostic_difference=float(np.max(abs(amp-amp0))),
                 linear_error_differences={k:float(np.max(abs(err[k]-err0[k]))) for k in err},
                 field_differences={})
        source=op.grid(120.,h); target=op.grid(120.,.1)
        for eps in (.001,.002):
            fields=responses[level][eps][0]; base=responses['base'][eps][0]; differences=[]
            for left,right in zip(base,fields):
                # q and p each have three canonically weighted blocks.
                q,_=op.restrict(right[:3*source['n']],source,target)
                p,_=op.restrict(right[3*source['n']:],source,target)
                differences.append(float(np.linalg.norm(np.r_[q,p]-left)/np.linalg.norm(mode_by_h[.1]['v'])))
            row['field_differences'][str(eps)]=dict(maximum=max(differences),samples=differences)
        sensitivity[level]=row
    physics=all(max(row['linear_errors'][str(eps)])<.05 for row in summary.values() for eps in (.001,.002))
    physics=physics and all(row['max_amplitude_difference']<.05 for row in summary.values())
    resolution=all(row['amplitude_diagnostic_difference']<.01 and
                   all(x<.01 for x in row['linear_error_differences'].values()) for row in sensitivity.values())
    return dict(levels=summary,sensitivity=sensitivity),('LINEAR_NEAR_RESPONSE_IN_FIXED_WINDOW' if physics and resolution
        else 'NUMERICALLY_UNRESOLVED_SENSITIVITY' if not resolution else 'NO_LINEAR_NEAR_RESPONSE_IN_FIXED_WINDOW')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--dynamics',type=Path,required=True)
    parser.add_argument('--operator',type=Path,required=True)
    parser.add_argument('--search-dir',type=Path,required=True)
    parser.add_argument('--reference',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',arms=[],code_sha256=sha(__file__),dynamics_sha256=DYNAMICS_HASH,
                operator_sha256=OPERATOR_HASH,search_sha256=RESULT_HASH,
                interpretation='Nonlinear small-amplitude short-time response, no existence/stability certification')
    active={}; responses={}
    try:
        dyn=imported(args.dynamics,DYNAMICS_HASH,'existing_nonlinear_verlet')
        op=imported(args.operator,OPERATOR_HASH,'existing_mode_operator')
        refs=dyn.load_reference(args.reference); result['reference']=refs[-1]
        mode_by_h,meta=modes(args.search_dir,refs,op); result['ritz']=meta
        save(args.out,result); checkpoint()
        for level,h,dt in LEVELS:
            responses[level]={}; baseline=None
            for eps in EPSILONS:
                checkpoint()
                returned=run_arm(dyn,op,args.out,result,level,h,dt,eps,refs,mode_by_h[h],baseline,active)
                if eps==0: baseline=returned
                else: responses[level][eps]=returned
        result['comparison'],result['status']=comparisons(op,responses,mode_by_h)
    except Exception as exc:
        result['error']=repr(exc)
        result['status']='INCOMPLETE' if isinstance(exc,RuntimeError) else 'NUMERICALLY_UNRESOLVED'
        if active:
            state=active['state']; file=args.out/'LAST-PARTIAL.npz'
            np.savez_compressed(file,r=active['r'],phi=state[0],pi=state[1],chi=state[2],chi_t=state[3])
            result['last_partial']=dict(level=active['level'],epsilon=active['epsilon'],t=active['t'],
                                        artifact=file.name,sha256=sha(file))
    save(args.out,result)
    return 0 if result['status'] in ('LINEAR_NEAR_RESPONSE_IN_FIXED_WINDOW','NO_LINEAR_NEAR_RESPONSE_IN_FIXED_WINDOW') else 2


if __name__=='__main__':
    raise SystemExit(main())
