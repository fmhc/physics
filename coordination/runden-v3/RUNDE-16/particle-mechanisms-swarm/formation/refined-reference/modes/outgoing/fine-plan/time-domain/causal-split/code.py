#!/usr/bin/env python3
"""Causal DC/second-harmonic split on one fixed finite generator. No nonlinear run."""
import time
START=time.process_time()
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu

TIME_HASH='74ba12a56e60241a967c2ff143a6489adbd7b27a3b72ddeeb0d3d29fee3c43c6'
SOURCE_HASH='5ba2d7e001f6145ff5f75afedadf6850565df8fac25412f84cab1c1c1a21443f'
OBS_HASH='a3f302b50f184ef2b7fdf9d92afb903068e22436d2b3547fa4248f80e9a56cc3'
T=128.; H=.05; DTS=(.02,.01)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked(path,digest):
    if sha(path)!=digest:
        raise ValueError('Provenance mismatch: '+str(path))
    return path


def module(path,digest,name):
    checked(path,digest); spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec); spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time()-START>=80:
        raise RuntimeError('INCOMPLETE: 80 CPU-s checkpoint')


def save(directory,result):
    result['cpu_seconds']=time.process_time()-START
    tmp=directory/'RESULT.tmp'; tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    tmp.replace(directory/'RESULT.json')


def artifact(directory,name,**arrays):
    path=directory/name; np.savez_compressed(path,**arrays)
    return dict(file=name,sha256=sha(path))


def quotient(x,y):
    return float(x/y) if y>0 and np.isfinite(x) and np.isfinite(y) else None


def below(value,bound):
    return value is not None and value<bound


class Midpoint:
    def __init__(self,K,G,dt):
        self.K=K; self.dt=dt
        identity=sparse.eye(K.shape[0],format='csc')
        self.M=(identity+.5*dt*G+.25*dt*dt*K).tocsc()
        self.B=(identity+.5*dt*G-.25*dt*dt*K).tocsc()
        self.lu=splu(self.M)

    def step(self,q,p,force):
        dt=self.dt; rhs=self.B@q+dt*p+.5*dt*dt*force
        qn=self.lu.solve(rhs); pn=2*(qn-q)/dt-p
        applied=self.M@qn
        residual=np.linalg.norm(applied-rhs,axis=0)/(np.linalg.norm(applied,axis=0)+np.linalg.norm(rhs,axis=0)+1e-14)
        if not all(np.all(np.isfinite(x)) for x in (qn,pn,residual)) or np.max(residual)>=1e-10:
            raise ValueError('Midpoint solve finite/residual gate failed')
        return qn,pn,residual

    def energy(self,q,p):
        return .5*np.sum(p*p+q*(self.K@q),axis=0)


def analytic_controls(nu):
    records=[]
    K=sparse.csc_matrix((1,1)); G=K.copy(); stepper=Midpoint(K,G,.02)
    q=np.zeros((1,1)); p=q.copy(); maximum=0.
    for j in range(6400):
        if j%100==0: checkpoint()
        q,p,_=stepper.step(q,p,np.ones((1,1))); t=(j+1)*.02
        exact=np.array([.5*t*t,t]); measured=np.array([q[0,0],p[0,0]])
        maximum=max(maximum,float(np.linalg.norm(measured-exact)/max(np.linalg.norm(exact),1e-14)))
    records.append(dict(kind='null_Jordan_force_0_1',maximum_relative_error=maximum,passed=maximum<1e-10))
    errors=[]; om=.9
    for dt in DTS:
        stepper=Midpoint(sparse.csc_matrix([[om*om]]),G,dt)
        q=np.zeros((1,2)); p=q.copy(); maxerror=np.zeros(2); maxnorm=np.zeros(2)
        for j in range(round(T/dt)):
            if j%100==0: checkpoint()
            q,p,_=stepper.step(q,p,np.array([[1.,np.cos(nu*(j+.5)*dt)]])); t=(j+1)*dt
            qe=np.array([(1-np.cos(om*t))/om**2,(np.cos(nu*t)-np.cos(om*t))/(om**2-nu**2)])
            pe=np.array([np.sin(om*t)/om,(-nu*np.sin(nu*t)+om*np.sin(om*t))/(om**2-nu**2)])
            maxerror=np.maximum(maxerror,np.sqrt((q[0]-qe)**2+(p[0]-pe)**2))
            maxnorm=np.maximum(maxnorm,np.sqrt(qe*qe+pe*pe))
        error=maxerror/maxnorm; errors.append(error)
        records.append(dict(kind='scalar_oscillator',dt=dt,relative_errors=error.tolist(),passed=bool(np.max(error)<.005)))
    ratios=[quotient(errors[0][j],errors[1][j]) for j in (0,1)]
    passed=all((errors[0][j]<1e-10 and errors[1][j]<1e-10) or
               (ratios[j] is not None and 2<ratios[j]<6) for j in (0,1))
    records.append(dict(kind='oscillator_step_reduction',ratios=ratios,passed=passed))
    return records


def load_observed(args,td,g):
    result=json.loads(checked(args.observed_dir/'RESULT.json',OBS_HASH).read_text())
    if result['status']!='UNRESOLVED' or result['code_sha256']!=TIME_HASH:
        raise ValueError('Observed result identity/status mismatch')
    rows=[]; fields={}; times=None; r=None
    for eps in (0.,.002,-.002):
        found=[a for a in result['arms'] if a['level']=='base' and a['epsilon']==eps]
        if len(found)!=1 or not found[0]['complete']:
            raise ValueError('Missing complete observed base arm')
        arm=found[0]; entry=arm['ring_artifact']; path=args.observed_dir/entry['file']
        checked(path,entry['sha256'])
        with np.load(path,allow_pickle=False) as z:
            if times is None:
                times=z['t'].copy(); r=z['r'].copy()
            if not np.array_equal(times,z['t']) or not np.array_equal(r,z['r']):
                raise ValueError('Observed ring synchronization mismatch')
            fields[eps]=z['rotating_fields'].copy()
        rows.append(dict(epsilon=eps,artifact=entry,initial=arm['initial']))
    indices=np.flatnonzero((g['r']>=40-2*H)&(g['r']<=50+2*H))
    if not np.array_equal(r,g['r'][indices]) or not np.array_equal(times,np.arange(1281)*.1):
        raise ValueError('Observed grid/time schema mismatch')
    if any(x.shape!=(1281,4,len(r)) or not np.all(np.isfinite(x)) for x in fields.values()):
        raise ValueError('Observed field schema/finite mismatch')
    alpha=rows[1]['initial']['alpha']
    if alpha<=0 or rows[2]['initial']['alpha']!=-alpha:
        raise ValueError('Observed alpha pair mismatch')
    even=(fields[.002]+fields[-.002]-2*fields[0])/(2*alpha**2)
    return times,r,indices,even,dict(result_sha256=OBS_HASH,arms=rows,alpha=alpha)


def physical_ring(q,p,g,indices):
    n=g['n']; root=g['root'][indices]
    qfield=q.reshape(3,n,2)[:,indices,:]/root[None,:,None]
    pfield=p.reshape(3,n,2)[:,indices,:]/root[None,:,None]
    # output source column, physical component, radial cell
    return np.stack(((qfield[0]+1j*qfield[1])/np.sqrt(2),
                     (pfield[0]+1j*pfield[1])/np.sqrt(2),qfield[2],pfield[2]),axis=0).transpose(2,0,1)


def run_split(args,result,op,source,mode,indices,dt):
    g=mode['grid']; n=g['n']; f,c,omega=mode['reference']; rho=mode['rho']; nu=2*rho
    A,K,G,_=op.operators(g,f,c,omega)
    v=mode['v']; uhat=v[:3*n].reshape(3,n)/g['root']
    j0=(g['root']*.5*(source.source(f,c,uhat.real)+source.source(f,c,uhat.imag))).reshape(-1)
    j2=(g['root']*source.source(f,c,uhat)/4).reshape(-1)
    checkpoint(); stepper=Midpoint(K,G,dt)
    phase=np.r_[np.zeros(n),np.sqrt(2)*g['root']*f,np.zeros(n)]
    phase_state=np.r_[phase,np.zeros(3*n)]
    phase_res=float(np.linalg.norm(A@phase_state)/np.linalg.norm(phase_state))
    qtest,ptest,_=stepper.step(phase[:,None],np.zeros((3*n,1)),np.zeros((3*n,1)))
    phase_step=float(np.linalg.norm(np.r_[qtest[:,0]-phase,ptest[:,0]])/np.linalg.norm(phase))
    row=dict(dt=dt,complete=False,last_time=0.,samples=[],phase_residual=phase_res,phase_step_error=phase_step)
    result['runs'].append(row); save(args.out,result)
    if phase_res>=1e-8 or phase_step>=1e-10:
        raise ValueError('True phase anchor failed')
    q=np.zeros((3*n,2)); p=q.copy(); work=np.zeros(2); abswork=np.zeros(2); maxres=np.zeros(2)
    rings=np.empty((1281,2,4,len(indices)),dtype=complex); sample=round(.1/dt)
    diagnostic=round(.4/dt); h0=stepper.energy(q,p)
    maxbalance=np.zeros(2)
    rootf=g['root']*f
    def linear_charge(q,p):
        return np.sqrt(2)*np.sum(rootf[:,None]*(2*omega*q[:n]+p[n:2*n]),axis=0)
    def quadratic_charge(t):
        whole=np.real(v*np.exp(1j*rho*t)).reshape(6,n)/g['root']
        a=(whole[0]+1j*whole[1])/np.sqrt(2); b=(whole[3]+1j*whole[4])/np.sqrt(2)
        return float(2*np.sum(g['vol']*np.imag(np.conj(a)*(1j*omega*a+b))))
    qinitial=quadratic_charge(0.)
    for j in range(round(T/dt)+1):
        t=j*dt
        if j%100==0: checkpoint()
        if j%sample==0:
            rings[j//sample]=physical_ring(q,p,g,indices)
        if j%diagnostic==0:
            energy=stepper.energy(q,p); balance=abs(energy-h0-work)/(abswork+abs(energy)+1e-14)
            if not all(np.all(np.isfinite(x)) for x in (energy,balance,work,abswork)):
                raise ValueError('Nonfinite energy/work diagnostics; last valid record retained')
            maxbalance=np.maximum(maxbalance,balance)
            charge=linear_charge(q,p); qquad=quadratic_charge(t)
            row['samples'].append(dict(t=t,rotating_quadratic_energy=energy.tolist(),work=work.tolist(),
                work_balance=balance.tolist(),linear_charge_by_source=charge.tolist(),
                first_order_quadratic_charge=qquad,
                charge_identity_defect=float(np.sum(charge)+qquad-qinitial),
                state_norms=np.sqrt(np.sum(q*q+p*p,axis=0)).tolist()))
            if np.max(balance)>=1e-8:
                row['last_time']=t; save(args.out,result); raise ValueError('Discrete quadratic energy/work balance failed')
            if j%round(4/dt)==0:
                row.update(last_time=t,max_solve_residual=maxres.tolist(),max_work_balance=maxbalance.tolist())
                save(args.out,result)
        if j==round(T/dt): break
        force=np.column_stack((j0,2*np.real(j2*np.exp(1j*nu*(t+.5*dt)))))
        qn,pn,res=stepper.step(q,p,force); increment=dt*np.sum(.5*(pn+p)*force,axis=0)
        work+=increment; abswork+=abs(increment); maxres=np.maximum(maxres,res)
        q,p=qn,pn
    row.update(complete=True,last_time=T,max_solve_residual=maxres.tolist(),max_work_balance=maxbalance.tolist(),
        ring_artifact=artifact(args.out,f'split-dt{dt:g}-ring.npz',t=np.arange(1281)*.1,r=g['r'][indices],
                               rotating_fields_by_source=rings,sources=np.array(['DC','H2'])),
        final_artifact=artifact(args.out,f'split-dt{dt:g}-final.npz',r=g['r'],q=q,p=p))
    save(args.out,result)
    return rings


def interval(times,values,left,right):
    def endpoint(t):
        j=int(np.searchsorted(times,t))
        if j<len(times) and abs(times[j]-t)<1e-12: return values[j]
        fraction=(t-times[j-1])/(times[j]-times[j-1])
        return (1-fraction)*values[j-1]+fraction*values[j]
    inside=(times>left)&(times<right)
    return np.r_[left,times[inside],right],np.concatenate((endpoint(left)[None],values[inside],endpoint(right)[None]))


def analyse(td,mode,times,r,indices,observed,coarse,fine):
    nu=2*mode['rho']; vol=mode['grid']['vol'][indices]; target=mode['answer'][0,indices]
    summed=fine[:,0]+fine[:,1]; coarse_sum=coarse[:,0]+coarse[:,1]
    rows=[]
    for wi,start in enumerate((88.,104.5)):
        end=start+2*np.pi/mode['rho']
        dc=td.coefficient(times,fine[:,0],start,end,nu)
        harmonic=td.coefficient(times,fine[:,1],start,end,nu)
        finecoef=dc+harmonic; coarsecoef=td.coefficient(times,coarse_sum,start,end,nu)
        actualcoef=td.coefficient(times,observed,start,end,nu)
        ts,actualtime=interval(times,observed,start,end)
        _,finetime=interval(times,summed,start,end); _,coarsetime=interval(times,coarse_sum,start,end)
        weights=np.diff(ts)
        for si,(lo,hi) in enumerate(((40.,45.),(45.,50.))):
            mask=(r>=lo)&(r<hi); vv=vol[mask]
            def norm(field): return float(np.sqrt(np.sum(vv*abs(field[mask])**2)))
            def time_norm(field):
                density=np.sum(vv*abs(field[:,mask])**2,axis=1)
                return float(np.sqrt(np.sum(.5*(density[1:]+density[:-1])*weights)))
            nt=time_norm(actualtime[:,0]); nc=norm(actualcoef[0])
            errors=dict(dt_time=quotient(time_norm(finetime[:,0]-coarsetime[:,0]),nt),
                        dt_band=quotient(norm(finecoef[0]-coarsecoef[0]),nc),
                        sum_time=quotient(time_norm(finetime[:,0]-actualtime[:,0]),nt),
                        sum_band=quotient(norm(finecoef[0]-actualcoef[0]),nc))
            flags={key:below(value,.01 if key.startswith('dt_') else .05) for key,value in errors.items()}
            C=dc[0]; Hp=harmonic[0]-target; delta=C+Hp; nd=norm(delta)
            targetnorm=norm(target); resolved=nd>=1e-8*targetnorm and targetnorm>0
            ratios=dict(DC_over_deviation=quotient(norm(C),nd),H2_minus_stationary_over_deviation=quotient(norm(Hp),nd))
            row=dict(window=[start,end],time_window=wi,shell=si,radius_window=[lo,hi],errors=errors,flags=flags,
                observed_time_L2=nt,observed_plus_band_L2=nc,target_plus_L2=targetnorm,
                deviation_L2=nd,DC_band_L2=norm(C),H2_minus_stationary_L2=norm(Hp),
                interference=float(2*np.real(np.sum(vv*np.conj(C[mask])*Hp[mask]))),
                deviation_squared=nd*nd,component_square_sum=norm(C)**2+norm(Hp)**2,
                ratios=ratios,deviation_resolved=bool(resolved),
                additional_component_absolute_band_errors=[norm(finecoef[k]-actualcoef[k]) for k in (1,2,3)],
                additional_component_errors_over_plus=[quotient(norm(finecoef[k]-actualcoef[k]),nc) for k in (1,2,3)],
                additional_component_absolute_time_errors=[time_norm(finetime[:,k]-actualtime[:,k]) for k in (1,2,3)],
                additional_component_time_errors_over_plus=[quotient(time_norm(finetime[:,k]-actualtime[:,k]),nt) for k in (1,2,3)])
            actualneg=td.coefficient(times,observed,start,end,-nu)
            predictedneg=td.coefficient(times,summed,start,end,-nu)
            row['negative_band_absolute_error']=norm(predictedneg[0]-actualneg[0])
            row['negative_band_error_over_plus']=quotient(row['negative_band_absolute_error'],nc)
            rows.append(row)
    validation=all(all(row['flags'].values()) for row in rows)
    if not validation:
        attribution='UNRESOLVED_SUM_OR_TIMESTEP_VALIDATION'
    elif not all(row['deviation_resolved'] for row in rows):
        attribution='UNRESOLVED_DEVIATION_DENOMINATOR'
    elif all(below(row['ratios']['DC_over_deviation'],.10) for row in rows):
        attribution='H2_RESPONSE_MINUS_STATIONARY_DOMINANT'
    elif all(below(row['ratios']['H2_minus_stationary_over_deviation'],.10) for row in rows):
        attribution='DC_STARTUP_RESPONSE_DOMINANT'
    else:
        attribution='MIXED_OR_WINDOW_DEPENDENT_WITH_INTERFERENCE'
    return rows,validation,attribution


def main():
    parser=argparse.ArgumentParser()
    for name in ('time-code','source-code','operator','outgoing','response-code','reference',
                 'source-dir','prepared-dir','response-dir','search-dir','observed-dir','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',code_sha256=sha(__file__),runs=[],
                input_hashes=dict(time_code=TIME_HASH,source_code=SOURCE_HASH,observed=OBS_HASH),
                interpretation='Causal source-history diagnosis on fixed finite generator; old UNRESOLVED unchanged')
    save(args.out,result)
    try:
        td=module(args.time_code,TIME_HASH,'unchanged_time_adapter')
        source=module(args.source_code,SOURCE_HASH,'unchanged_quadratic_source')
        op=module(args.operator,td.HASH['operator'],'unchanged_modes')
        out=module(args.outgoing,td.HASH['outgoing'],'unchanged_outgoing')
        response=module(args.response_code,td.HASH['response_code'],'unchanged_response_loader')
        modes,metadata=td.load_inputs(args,op,out,response); mode=modes[H]
        result['inputs']=metadata
        times,r,indices,observed,provenance=load_observed(args,td,mode['grid'])
        result['observed']=provenance
        result['controls']=analytic_controls(2*mode['rho']); save(args.out,result)
        if not all(row['passed'] for row in result['controls']):
            raise ValueError('Known-solution controls failed')
        solutions=[]
        for dt in DTS:
            checkpoint(); solutions.append(run_split(args,result,op,source,mode,indices,dt))
        checkpoint()
        rows,valid,attribution=analyse(td,mode,times,r,indices,observed,*solutions)
        result['comparison']=rows; result['sum_validation_passed']=valid; result['attribution']=attribution
        result['status']='CAUSAL_SPLIT_DIAGNOSIS_COMPLETE' if valid else 'UNRESOLVED'
    except Exception as exc:
        result['error']=repr(exc); result['status']='INCOMPLETE' if isinstance(exc,RuntimeError) else 'UNRESOLVED'
    save(args.out,result)
    return 0 if result['status']=='CAUSAL_SPLIT_DIAGNOSIS_COMPLETE' else 2


if __name__=='__main__':
    raise SystemExit(main())
