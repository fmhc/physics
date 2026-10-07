#!/usr/bin/env python3
"""Fixed coupled outgoing response; sparse linear solves only, no evolution."""
import time
START=time.process_time()
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve

OPHASH='467ad3e19cd8efcdac4ec2dcc670b50aaa59cc6f7e9e44d625ebbf94ba0d32c6'
SOURCEHASH='a2270a05c7270eeeb16e5fd04d12bd1367bff38af0205062b2643aea05b2a574'
CASES=((60.,.1),(120.,.1),(60.,.05),(120.,.05))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checktime():
    if time.process_time()-START>=8:
        raise RuntimeError('INCOMPLETE: 8 CPU-s checkpoint')


def save(out,result):
    result['cpu_seconds']=time.process_time()-START
    tmp=out/'RESULT.tmp'; tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    tmp.replace(out/'RESULT.json')


def finite(*arrays):
    if not all(np.all(np.isfinite(x)) for x in arrays): raise ValueError('Nonfinite arithmetic')


def norm(g,a):
    return float(np.sqrt(np.sum(g['vol']*abs(a)**2)))


def quotient(num,den):
    return float(num/den) if den>0 and np.isfinite(num) and np.isfinite(den) else None


def below(value,limit):
    return value is not None and value<limit


def amplitude(g,p,k,windows):
    values=g['r']*p*np.exp(1j*k*g['r']); rows=[]; means=[]
    for lo,hi in windows:
        mask=(g['r']>=lo)&(g['r']<=hi)
        if not np.any(mask): raise ValueError('Empty fixed extraction window')
        v=values[mask]; mean=complex(np.mean(v)); spread=float(np.max(abs(v-mean)))
        rows.append(dict(window=[lo,hi],A_real=mean.real,A_imag=mean.imag,A_abs=abs(mean),
                         max_absolute_spread=spread,relative_spread=quotient(spread,abs(mean))))
        means.append(mean)
    return rows,means


def solve(g,f,c,omega,nu,source,windows,incoming=False):
    finite(f,c,omega,nu,source)
    n=g['n']; h=g['h']; radius=g['R']; root=g['root']
    k2=(omega+nu)**2-2; km2=2-(omega-nu)**2; kc2=2-nu*nu
    if min(k2,km2,kc2)<=0: raise ValueError('Expected exactly one open plus channel')
    k=np.sqrt(k2); km=np.sqrt(km2); kc=np.sqrt(kc2)
    rl=radius-h/2; rg=radius+h/2
    beta=rl/rg*np.exp(np.array([1j*k*h if incoming else -1j*k*h,-km*h,-kc*h]))
    s=f*f; common=1+c*c-4*s+4.5*s*s-omega*omega-nu*nu
    potentials=(common-2*omega*nu,common+2*omega*nu,3*c*c-1+2*s-nu*nu)
    diagonal=[]; edge=4*np.pi*radius*radius/h
    for i,potential in enumerate(potentials):
        bc=np.zeros(n,dtype=complex); bc[-1]=-edge*beta[i]/g['vol'][-1]
        diagonal.append(g['D'].astype(complex)+sparse.diags(potential+bc))
    D=sparse.diags(-2*s+3*s*s); B=sparse.diags(2*c*f)
    matrix=sparse.bmat([[diagonal[0],D,B],[D,diagonal[1],B],[B,B,diagonal[2]]],format='csc')
    rhs=(source*root).reshape(-1)
    weighted=spsolve(matrix,rhs); finite(weighted)
    answer=weighted.reshape(3,n)/root
    applied=matrix@weighted
    residual=float(np.linalg.norm(applied-rhs)/(np.linalg.norm(applied)+np.linalg.norm(rhs)+1e-30))
    work=float(2*nu*np.imag(np.sum(g['vol']*np.conj(answer)*source)))
    flux=float(2*nu*edge*(-beta[0].imag)*abs(answer[0,-1])**2)
    scale=2*nu*norm(g,answer)*norm(g,source)
    balance=quotient(abs(work-flux),max(abs(work),abs(flux),1e-12*scale))
    rows,means=amplitude(g,answer[0],k,windows)
    for row,mean in zip(rows,means):
        fq=float(8*np.pi*k*abs(mean)**2)
        row.update(continuum_Q_flux=fq,continuum_E_flux=(omega+nu)*fq,
                   continuum_rot_flux=nu*fq,
                   continuum_FV_relative=quotient(abs(nu*fq-flux),abs(flux)))
    flags=dict(finite=True,residual=residual<1e-10,work_balance=below(balance,1e-7))
    row=dict(omega=omega,nu=nu,k=k,kappa_minus=km,kappa_chi=kc,
        r_last=rl,r_ghost=rg,beta_real=beta.real.tolist(),beta_imag=beta.imag.tolist(),
        residual=residual,source_work_rot=work,FV_rot_flux=flux,FV_Q_flux=flux/nu,
        FV_E_flux=(omega+nu)*flux/nu,work_scale=scale,relative_work_balance=balance,
        windows=rows,algebra_flags=flags,
        answer_component_L2=[norm(g,x) for x in answer],source_component_L2=[norm(g,x) for x in source],
        last_answer_real=answer[:,-1].real.tolist(),last_answer_imag=answer[:,-1].imag.tolist())
    return row,answer,means


def analytic_controls(op,out,result):
    omega=.8; nu=1.; k=np.sqrt((omega+nu)**2-2); length=2.; radius=30.
    exact=float(np.sqrt(np.pi)*length**3/4*np.exp(-k*k*length*length/4))
    null_amplitudes=[]
    for h in (.1,.05):
        g=op.grid(radius,h); r=g['r']; zero=np.zeros(g['n']); one=np.ones(g['n'])
        gaussian=np.exp(-r*r/length**2)
        for kind in ('gaussian','null_bump','closed','wrong_robin'):
            checktime(); src=np.zeros((3,g['n']),dtype=complex)
            bump=np.maximum(1-r*r/16,0)**4
            if kind=='null_bump':
                u=r*r/16; inside=r<4
                src[0,inside]=24/16*(1-u[inside])**3-48*r[inside]**2/256*(1-u[inside])**2-k*k*(1-u[inside])**4
            elif kind=='closed': src[2]=gaussian
            else: src[0]=gaussian
            row,answer,means=solve(g,zero,one,omega,nu,src,((15,20),(20,25)),kind=='wrong_robin')
            row.update(kind=kind,h=h,R=radius)
            flags=dict(row['algebra_flags'])
            if kind=='gaussian':
                row['analytic_A']=exact
                row['gaussian_omitted_A_bound']=float(length*length*np.exp(-radius*radius/length**2)/(2*k))
                row['magnitude_errors']=[abs(abs(a)-exact)/exact for a in means]
                row['complex_errors']=[abs(a-exact)/exact for a in means]
                flags.update(magnitude=all(x<.005 for x in row['magnitude_errors']),
                    complex_phase=all(x<.02 for x in row['complex_errors']),
                    continuum_flux=all(below(x['continuum_FV_relative'],.005) for x in row['windows']))
            elif kind=='null_bump':
                amp=max(abs(a) for a in means); null_amplitudes.append(float(amp))
                row['null_amplitude_over_gaussian']=float(amp/exact)
                row['bump_profile_error']=quotient(norm(g,answer[0]-bump),norm(g,bump))
                flags.update(nontrivial_source=norm(g,src)>1e-3,null_amplitude=amp/exact<.005,
                             bump_profile=below(row['bump_profile_error'],.005))
            elif kind=='closed':
                row['open_closed_norm_ratio']=quotient(norm(g,answer[0]),norm(g,answer[2]))
                row['closed_rot_flux_ratio']=quotient(abs(row['FV_rot_flux']),row['work_scale'])
                flags.update(open_zero=below(row['open_closed_norm_ratio'],1e-12),
                             closed_zero=below(row['closed_rot_flux_ratio'],1e-12))
            else:
                flags['negative_flux']=row['FV_rot_flux']<0
            row['flags']=flags; row['passed']=all(flags.values())
            result['qa'].append(row); save(out,result)
            if not row['passed']: raise ValueError('Free control failed: '+kind)
    floor=1e-10*exact
    ratio=quotient(null_amplitudes[0],null_amplitudes[1])
    below_floor=all(x<floor for x in null_amplitudes)
    passed=below_floor or (ratio is not None and 2<ratio<6)
    result['null_reduction']=dict(amplitudes=null_amplitudes,gaussian_scale=exact,
        below_floor=below_floor,coarse_fine_ratio=ratio,passed=passed)
    save(out,result)
    if not passed: raise ValueError('Null source h-reduction control failed')


def load_sources(directory,op,reference):
    path=directory/'RESULT.json'
    if sha(path)!=SOURCEHASH: raise ValueError('Source result provenance mismatch')
    result=json.loads(path.read_text()); refs,meta=op.load_refs(reference)
    if result['status']!='LOCAL_SOURCE_DIAGNOSTICS_COMPLETE' or result['reference']['manifest_sha256']!=meta['manifest_sha256']:
        raise ValueError('Source/reference mismatch')
    sources={}
    for row in result['profiles']:
        h=float(row['h']); path=directory/row['source_artifact']
        if sha(path)!=row['source_sha256']: raise ValueError('Source NPZ hash mismatch')
        with np.load(path,allow_pickle=False) as z:
            grid=op.grid(120.,h)
            if not np.array_equal(z['r'],grid['r']): raise ValueError('Source exact grid mismatch')
            j2=z['J2'].copy(); src=z['local_channels'].copy()
            recombined=np.array([(j2[0]+1j*j2[1])/np.sqrt(2),(j2[0]-1j*j2[1])/np.sqrt(2),j2[2]])
            if not np.allclose(src,recombined,rtol=1e-12,atol=0): raise ValueError('Stored channel convention mismatch')
            omega=float(z['omega']); rho=float(z['rho'])
            if omega!=row['omega'] or rho!=row['rho'] or omega!=refs[h][2]:
                raise ValueError('Source frequency mismatch')
            finite(src)
            sources[h]=(src,2*rho,dict(sha256=row['source_sha256'],file=str(path)))
    if set(sources)!={.1,.05}: raise ValueError('Missing source grid')
    return refs,sources,meta


def comparisons(rows):
    bykey={(x['R'],x['h']):x for x in rows}; checks=[]; changes=[]
    def mean(row):
        w=row['windows'][0]; return complex(w['A_real'],w['A_imag'])
    for h in (.1,.05):
        left=mean(bykey[(60.,h)]); right=mean(bykey[(120.,h)])
        change=abs(left-right); changes.append(change)
        relative=quotient(change,abs(right))
        checks.append(dict(kind='R',h=h,absolute_amplitude_change=change,relative=relative,passed=below(relative,.01)))
    for radius in (60.,120.):
        coarse=mean(bykey[(radius,.1)]); fine=mean(bykey[(radius,.05)])
        change=abs(abs(coarse)-abs(fine)); changes.append(change)
        relative=quotient(change,abs(fine))
        checks.append(dict(kind='h_magnitude',R=radius,absolute_amplitude_change=change,
                           relative=relative,passed=below(relative,.02)))
    spreads=[w['max_absolute_spread'] for x in rows for w in x['windows']]
    reserve=5*max(changes+spreads)
    signal=[]
    for row in rows:
        value=abs(mean(row))
        signal.append(dict(R=row['R'],h=row['h'],amplitude=value,reserve=reserve,passed=value>reserve and value>0))
    return dict(sensitivity=checks,signal_resolution=signal),all(x['passed'] for x in checks+signal)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--operator',type=Path,required=True)
    parser.add_argument('--source-dir',type=Path,required=True)
    parser.add_argument('--reference',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',code_sha256=sha(__file__),qa=[],cases=[],source_result_sha256=SOURCEHASH,
                interpretation='Fixed harmonic forced response; coefficient power, no damping/lifetime conclusion')
    try:
        if sha(args.operator)!=OPHASH: raise ValueError('Operator hash mismatch')
        spec=importlib.util.spec_from_file_location('existing_fv',args.operator)
        op=importlib.util.module_from_spec(spec); spec.loader.exec_module(op)
        result['operator_sha256']=OPHASH
        refs,sources,meta=load_sources(args.source_dir,op,args.reference); result['reference']=meta
        save(args.out,result); analytic_controls(op,args.out,result)
        for radius,h in CASES:
            checktime(); g=op.grid(radius,h); full=op.grid(120.,h)
            ff,cc,omega=refs[h]; fullsrc,nu,provenance=sources[h]
            n=g['n']; f=ff[:n]; c=cc[:n]; src=fullsrc[:,:n]
            profile=op.profile_check(g,f,c,omega,2*omega*np.sum(full['vol']*ff*ff))
            if not profile['passed']: raise ValueError('Background truncation gate failed')
            row,answer,means=solve(g,f,c,omega,nu,src,((40,45),(45,50)))
            row.update(R=radius,h=h,background_check=profile,source_provenance=provenance)
            allnorm=norm(full,fullsrc)**2
            omitted=float(np.sum(full['vol'][n:]*abs(fullsrc[:,n:])**2))
            collar=g['r']>radius-10
            row['source_omitted_fraction']=quotient(omitted,allnorm)
            row['source_collar_fraction']=quotient(float(np.sum(g['vol'][collar]*abs(src[:,collar])**2)),allnorm)
            row['boundary_background']=dict(f=float(f[-1]),chi_minus_vac=float(c[-1]-1),
                D=float(-2*f[-1]**2+3*f[-1]**4),B=float(2*c[-1]*f[-1]))
            difference=quotient(abs(means[0]-means[1]),abs(means[1]))
            flags=dict(row['algebra_flags'])
            flags.update(nonzero=all(abs(x)>0 for x in means),
                windows=all(below(w['relative_spread'],.01) for w in row['windows']),
                between_windows=below(difference,.01),
                continuum_flux=all(below(w['continuum_FV_relative'],.02) for w in row['windows']))
            row['between_windows_relative']=difference; row['flags']=flags; row['passed']=all(flags.values())
            filename=f'ANSWER-R{radius:g}-h{h}.npz'
            np.savez_compressed(args.out/filename,r=g['r'],answer_channels=answer,source_channels=src,omega=omega,nu=nu)
            row['artifact']=filename; row['artifact_sha256']=sha(args.out/filename)
            result['cases'].append(row); save(args.out,result)
        checktime()
        result['comparison'],passed=comparisons(result['cases'])
        result['status']=('CONTROLLED_FORCED_RESPONSE' if passed and all(x['passed'] for x in result['cases'])
                          else 'UNRESOLVED')
    except Exception as exc:
        result['error']=repr(exc)
        result['status']='INCOMPLETE' if isinstance(exc,RuntimeError) else 'UNRESOLVED'
    save(args.out,result)
    return 0 if result['status']=='CONTROLLED_FORCED_RESPONSE' else 2


if __name__=='__main__':
    raise SystemExit(main())
