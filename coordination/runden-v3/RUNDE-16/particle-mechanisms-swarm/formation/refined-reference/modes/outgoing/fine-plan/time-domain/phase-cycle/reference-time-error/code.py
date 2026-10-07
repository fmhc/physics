#!/usr/bin/env python3
"""Stored-field Richardson diagnosis only. No evolution, inversion, fit or search."""
import time
START=time.process_time()
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

HASH=dict(time_code='74ba12a56e60241a967c2ff143a6489adbd7b27a3b72ddeeb0d3d29fee3c43c6',
 split_code='ac87c195092b607cdf106a9ad7a88606bcf0579623cd581297485f76bf7cceaa',
 phase_code='3509332b4732c8497e9246855fc7be6254ff1681e3e2e99b823457180aaa1446',
 split='15593347f6b1caff683315fab65ce74734ae85fb5eff97b8a25d9276c0a568b9',
 phase='b7d938e4bda00bb05598f540f05320b2e3cad7a8a8f3f4be940a9d5884b8eafd',
 amplitude='2fa8c40331f18ed677788629733806109dbc9a622c4d8ff22e065c82979adefd',
 amplitude_code='5e8f8c201f9d0f0090f442f6d6173c9e4f1362cfecbd55fc9ac9f823614dc4c9',
 observed='a3f302b50f184ef2b7fdf9d92afb903068e22436d2b3547fa4248f80e9a56cc3')
GATES=dict(alignment=.8,remaining_fraction=.5,reserve_factor=2.,qa=1e-10,arithmetic_factor=64.)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(ok,message):
    if not ok:
        raise ValueError(message)


def checked(path,digest):
    require(sha(path)==digest,'Hash mismatch: '+str(path))
    return path


def module(path,digest,name):
    checked(path,digest)
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec); spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time()-START>=4.5:
        raise RuntimeError('INCOMPLETE: 4.5 CPU-s checkpoint; external total target 5 CPU-s')


def save(directory,result):
    result['cpu_seconds']=time.process_time()-START
    tmp=directory/'RESULT.tmp'
    tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    tmp.replace(directory/'RESULT.json')


def load(args):
    manifests={name:json.loads(checked(getattr(args,name+'_dir')/'RESULT.json',HASH[name]).read_text())
               for name in ('split','phase','amplitude')}
    s,p,a=(manifests[k] for k in ('split','phase','amplitude'))
    require(s['status']=='CAUSAL_SPLIT_DIAGNOSIS_COMPLETE' and s['sum_validation_passed']
            and s['code_sha256']==HASH['split_code'],'Causal manifest status/identity mismatch')
    require(p['status']=='CONTROLLED_PHASE_CYCLE_CAUSAL_COMPONENTS' and p['terminal_complete']
            and p['code_sha256']==HASH['phase_code'],'Phase manifest status/identity mismatch')
    require(a['status']=='RESOLVED_AMPLITUDE_DIFFERENCE_ON_FIXED_GRID' and a['terminal_complete']
            and a['code_sha256']==HASH['amplitude_code'],'Amplitude manifest status/identity mismatch')
    require(s['observed']['result_sha256']==HASH['observed']
            and p['bound_hashes']['observed']==HASH['observed']
            and p['bound_hashes']['split']==HASH['split']
            and a['bound_hashes']['phase_result']==HASH['phase']
            and a['bound_hashes']['observed']==HASH['observed'],'Precursor linkage mismatch')
    identity=[m for m in p['inputs'] if m['h']==.05]
    require(len(identity)==1,'Ambiguous phase input metadata')
    for other in (s,a):
        require([m for m in other['inputs'] if m['h']==.05]==identity,'Reference/Ritz/gauge mismatch')
    phase=p['phase_change']; rho=phase['rho']
    require(np.isfinite(rho) and .38<rho<.39 and phase['multiplier']==[0.,1.]
            and not phase['renormalized'] and phase['alpha']==s['observed']['alpha']
            and phase['alpha']==a['normalization']['alpha_large'],'Phase/alpha mismatch')
    times=np.arange(1281)*.1
    fullr=(np.arange(2400)+.5)*.05
    r=fullr[(fullr>=40-.1)&(fullr<=50+.1)]
    fields={}; artifacts=[]
    for key,manifest,directory,dt in (
        ('Rc',s,args.split_dir,.02),('Rf',s,args.split_dir,.01),
        ('Ncoarse',p,args.phase_dir,.01),('N',p,args.phase_dir,.005)):
        checkpoint()
        causal=key in ('Rc','Rf')
        rows=[x for x in manifest['runs' if causal else 'pairs'] if x['dt']==dt]
        require(len(rows)==1 and rows[0]['complete'] and rows[0]['last_time']==128.,
                'Missing/incomplete source field: '+key)
        if not causal:
            require(rows[0]['odd_passed'],'Stored nonlinear odd gate failed')
        entry=rows[0]['ring_artifact' if causal else 'separated_artifact']
        path=checked(directory/entry['file'],entry['sha256'])
        with np.load(path,allow_pickle=False) as z:
            require(np.array_equal(z['t'],times) and np.array_equal(z['r'],r)
                    and list(z['sources'])==['DC','H2'],'Ring axes/source mismatch')
            raw=z['rotating_fields_by_source']
            require(raw.shape==(1281,2,4,len(r)) and np.all(np.isfinite(raw)),
                    'Ring shape/nonfinite values')
            fields[key]=raw[:,:,0].copy()
            del raw
        artifacts.append(dict(role=key,dt=dt,directory=str(directory),**entry))
    return times,r,rho,fields,dict(manifests={k:HASH[k] for k in manifests},
        input_identity=identity[0],phase=phase,artifacts=artifacts,
        amplitude_used_as_context_only=True)


def classify(nz,nc,nright,nwrong,inner,u):
    alignment=float(inner/(nz*nc)) if nz>0 and nc>0 else None
    flags=dict(nonzero=nz>0 and nc>0,
        alignment=alignment is not None and alignment>GATES['alignment'],
        reduction=nright<GATES['remaining_fraction']*nz,
        improvement=nz-nright>GATES['reserve_factor']*u,
        wrong_direction=nwrong-nz>GATES['reserve_factor']*u)
    return alignment,{key:bool(value) for key,value in flags.items()}


def evaluate(td,split,times,r,rho,N,Ncoarse,Rf,Rc,synthetic=False):
    # Direct operations agree exactly with the declared positive summand hulls.
    correction=(Rf-Rc)/3
    z=N-Rf
    right=N-(4/3)*Rf+(1/3)*Rc
    wrong=N-(2/3)*Rf-(1/3)*Rc
    delta=N-Ncoarse
    hulls=(abs(N)+abs(Rf),abs(N)+(4/3)*abs(Rf)+(1/3)*abs(Rc),
           abs(N)+(2/3)*abs(Rf)+(1/3)*abs(Rc))
    values=dict(N=N,Rf=Rf,c=correction,Z=z,right=right,wrong=wrong,dt=delta)
    if synthetic:
        # Here N=F and Rf=F+.01²*A. Expected c is formed from A supplied below.
        values['synthetic_A']=(np.exp(-r/50)[None,None,:]
             *(1+np.exp(2j*rho*times[:,None,None]))) * np.ones((1,2,1))
    rows=[]; vol=4*np.pi*.05*(r*r+.05*.05/12)
    for wi,left in enumerate((88.,104.5)):
        checkpoint(); right_time=left+2*np.pi/rho
        ts=split.interval(times,N,left,right_time)[0]
        weights=np.diff(ts)
        timefields={k:split.interval(times,x,left,right_time)[1] for k,x in values.items()}
        bandfields={k:td.coefficient(times,x,left,right_time,2*rho) for k,x in values.items()}
        timehulls=[split.interval(times,x,left,right_time)[1] for x in hulls]
        bandhulls=[td.coefficient(times,x,left,right_time,0.).real for x in hulls]
        for si,(lo,hi) in enumerate(((40.,45.),(45.,50.))):
            mask=(r>=lo)&(r<hi); vv=vol[mask]
            require(np.any(mask),'Empty shell')
            for ci,name in enumerate(('DC','H2')):
                for measure,items,hs in (('time',timefields,timehulls),('band',bandfields,bandhulls)):
                    def inner(x,y):
                        density=np.sum(vv*np.conj(x[...,mask])*y[...,mask],axis=-1)
                        if measure=='time':
                            return float(np.real(np.sum(.5*(density[1:]+density[:-1])*weights)))
                        return float(np.real(density))
                    def norm(x):
                        return float(np.sqrt(max(0.,inner(x,x))))
                    x={k:(v[:,ci] if measure=='time' else v[ci]) for k,v in items.items()}
                    norms={k:norm(v) for k,v in x.items()}
                    etas=[float(64*np.finfo(np.float64).eps*norm(h[:,ci] if measure=='time' else h[ci])) for h in hs]
                    eta=float(max(etas)); u=float(norms['dt']+eta); cross=inner(x['Z'],x['c'])
                    require(all(np.isfinite(v) for v in list(norms.values())+etas+[u,cross]),
                            'Nonfinite measurement')
                    alignment,flags=classify(norms['Z'],norms['c'],norms['right'],norms['wrong'],cross,u)
                    identity=norms['right']**2-(norms['Z']**2+norms['c']**2-2*cross)
                    row=dict(component=name,time_window=wi,shell=si,measure=measure,
                        window=[left,right_time],radius_window=[lo,hi],norms=norms,
                        real_inner_Z_c=cross,alignment=alignment,quadratic_identity_defect=identity,
                        eta_by_expression=dict(zip(('Z','right','wrong'),etas)),eta=eta,u=u,flags=flags,
                        relative_to_original_Rf={k:td.ratio(v,norms['Rf']) for k,v in norms.items()},
                        status='KONSISTENT_MIT_DOMINANTER_DT2_KOMPONENTE' if all(flags.values()) else 'NICHT_ZUGEORDNET',
                        improvement_under_reserve=bool(norms['Z']-norms['right']<=2*u))
                    if synthetic:
                        known=.01**2*norms['synthetic_A']
                        require(known>0,'Synthetic correction vanishes')
                        # Expected Z=c=-.01²*A, right=0, wrong=-2*.01²*A.
                        errors=dict(extrapolated=norms['right']/known,
                            correction=norm(x['c']+.01**2*x['synthetic_A'])/known,
                            wrong=norm(x['wrong']+2*.01**2*x['synthetic_A'])/known)
                        _,badflags=classify(norms['Z'],norms['c'],norms['wrong'],norms['right'],-cross,u)
                        row['qa']=dict(known_correction_norm=known,errors=errors,
                            passed=all(v<1e-10 for v in errors.values()) and all(flags.values())
                                   and not all(badflags.values()),wrong_sign_passed=all(badflags.values()))
                    rows.append(row)
    require(len(rows)==16,'Measurement completeness failed')
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('time-code','split-code','split-dir','phase-dir','amplitude-dir','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',complete=False,code_sha256=sha(__file__),bound_hashes=HASH,
        gates=GATES,budget=dict(target_cpu_seconds=5,checkpoint_cpu_seconds=4.5),
        qa={},measurements=[],
        interpretation='Directed consistency with leading reference dt² error; not a unique cause or convergence proof',
        reserve_limit='u is empirical; eta covers only new stored-field arithmetic, not previous parity cancellation or evolution',
        original_statuses_unchanged=True)
    save(args.out,result)
    try:
        td=module(args.time_code,HASH['time_code'],'stored_time_measurement')
        split=module(args.split_code,HASH['split_code'],'stored_interval_measurement')
        times,r,rho,fields,provenance=load(args)
        result['inputs']=provenance; save(args.out,result)
        # Fixed calibration fields have nonzero correction in all windows/shells.
        A=np.exp(-r/50)[None,None,:]*(1+np.exp(2j*rho*times[:,None,None]))*np.ones((1,2,1))
        F=np.broadcast_to((1+.25j)*np.exp(-r/60)[None,None,:],A.shape).copy()
        qa=evaluate(td,split,times,r,rho,F,F,F+.01**2*A,F+.02**2*A,synthetic=True)
        result['qa']['exact_dt2']=qa; save(args.out,result)
        require(all(row['qa']['passed'] for row in qa),'Synthetic dt²/sign calibration failed')
        zero=evaluate(td,split,times,r,rho,F,F,F,F)
        result['qa']['zero_correction']=zero; save(args.out,result)
        require(all(not all(row['flags'].values()) and row['norms']['c']==0 for row in zero),
                'Zero correction incorrectly assigned')
        del A,F
        checkpoint()
        result['measurements']=evaluate(td,split,times,r,rho,**fields)
        result['consistent_count']=sum(all(row['flags'].values()) for row in result['measurements'])
        result['complete']=True
        result['status']=('CONSISTENT_WITH_DOMINANT_REFERENCE_DT2_COMPONENT'
                          if result['consistent_count']==16 else 'NOT_GLOBALLY_ASSIGNED')
    except Exception as error:
        result['status']='INCOMPLETE'; result['error']=repr(error)
    save(args.out,result)
    return 0 if result['complete'] else 2


if __name__=='__main__':
    raise SystemExit(main())
