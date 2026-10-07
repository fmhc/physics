#!/usr/bin/env python3
"""Regional error diagnosis of fixed free controls; never runs M2 production."""
import time
START=time.process_time()
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

OUT='75b1dce542aa728fe6bf58ecea4aec4a2ddf8a6a5a6e236666075c6902bbd292'
OP='467ad3e19cd8efcdac4ec2dcc670b50aaa59cc6f7e9e44d625ebbf94ba0d32c6'
OLD='9f0b975784c3b5111fc95ae804db89b33cbbca750637ff2161c084c211a55e9f'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path,digest,name):
    if sha(path)!=digest: raise ValueError('Module hash mismatch')
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec); spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time()-START>=2.5: raise RuntimeError('INCOMPLETE 2.5 CPU-s checkpoint')


def save(out,result):
    result['cpu_seconds']=time.process_time()-START
    tmp=out/'RESULT.tmp'; tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    tmp.replace(out/'RESULT.json')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--outgoing',type=Path,required=True)
    parser.add_argument('--operator',type=Path,required=True)
    parser.add_argument('--previous',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',cases=[],code_sha256=sha(__file__),
                outgoing_sha256=OUT,operator_sha256=OP,previous_sha256=OLD,
                interpretation='Regional free-control diagnosis only; no gate change or M2 authorization')
    try:
        if sha(args.previous)!=OLD: raise ValueError('Previous result hash mismatch')
        previous=json.loads(args.previous.read_text())
        result['original_status_unchanged']=previous['status']
        out=module(args.outgoing,OUT,'unchanged_outgoing_solver')
        op=module(args.operator,OP,'unchanged_grid')
        omega=.8; nu=1.; k=np.sqrt((omega+nu)**2-2); length=2.
        exact=float(np.sqrt(np.pi)*length**3/4*np.exp(-k*k*length*length/4))
        nullrows=[]
        for h in (.1,.05,.025):
            grid=op.grid(30.,h); r=grid['r']; vol=grid['vol']
            zero=np.zeros(grid['n']); one=np.ones(grid['n'])
            for kind in ('gaussian','null_bump'):
                checkpoint(); source=np.zeros((3,grid['n']),dtype=complex)
                bump=np.maximum(1-r*r/16,0)**4
                if kind=='gaussian': source[0]=np.exp(-r*r/4)
                else:
                    mask=r<4; u=r[mask]**2/16
                    source[0,mask]=24/16*(1-u)**3-48*r[mask]**2/256*(1-u)**2-k*k*(1-u)**4
                row,answer,means=out.solve(grid,zero,one,omega,nu,source,((15,20),(20,25)))
                row.update(kind=kind,h=h,R=30)
                flags=dict(row['algebra_flags'])
                if kind=='gaussian':
                    row['magnitude_errors']=[float(abs(abs(a)-exact)/exact) for a in means]
                    row['complex_errors']=[float(abs(a-exact)/exact) for a in means]
                    flags.update(magnitude=all(x<.005 for x in row['magnitude_errors']),
                        complex_phase=all(x<.02 for x in row['complex_errors']),
                        continuum_flux=all(out.below(w['continuum_FV_relative'],.005) for w in row['windows']))
                    row['analytic_A']=exact
                    row['gaussian_omitted_A_bound']=float(length**2*np.exp(-30**2/length**2)/(2*k))
                else:
                    error=answer[0]-bump; error2=float(np.sum(vol*abs(error)**2))
                    bnorm2=float(np.sum(vol*bump*bump)); regions=[]
                    for lo,hi in ((0,4),(4,10),(10,30)):
                        mask=(r>=lo)&(r<hi); e2=float(np.sum(vol[mask]*abs(error[mask])**2))
                        predicted=float(4*np.pi*abs(means[0])**2*(hi-lo)) if lo>=4 else None
                        regions.append(dict(bounds=[lo,hi],error_squared=e2,
                            relative_L2=float(np.sqrt(e2/bnorm2)),
                            outgoing_tail_predicted_norm_squared=predicted,
                            measured_over_outgoing_prediction=out.quotient(e2,predicted) if predicted is not None else None))
                    relative=float(np.sqrt(error2/bnorm2)); amplitude=float(max(abs(a) for a in means))
                    fraction=out.quotient(regions[1]['error_squared']+regions[2]['error_squared'],error2)
                    row.update(regions=regions,total_error_squared=error2,bump_norm_squared=bnorm2,
                        region_sum_minus_total=float(sum(x['error_squared'] for x in regions)-error2),
                        relative_L2_error=relative,outside4_error_squared_fraction=fraction,
                        null_amplitude=amplitude,null_amplitude_over_gaussian=amplitude/exact)
                    flags.update(nontrivial_source=out.norm(grid,source)>1e-3,
                                 null_amplitude=amplitude/exact<.005,bump_profile=relative<.005)
                    nullrows.append(row)
                row['original_QA_flags']=flags; row['original_QA_passed']=all(flags.values())
                filename=f'{kind}-h{h}.npz'
                np.savez_compressed(args.out/filename,r=r,answer_channels=answer,source_channels=source,
                                    exact_bump=bump,omega=omega,nu=nu)
                row['artifact']=filename; row['artifact_sha256']=sha(args.out/filename)
                result['cases'].append(row); save(args.out,result)
                if not all(row['algebra_flags'].values()):
                    raise ValueError('Invalid algebraic residual/work balance; diagnostic stopped after saving case')
        checkpoint()
        ratios=[out.quotient(nullrows[i]['relative_L2_error'],nullrows[i+1]['relative_L2_error']) for i in (0,1)]
        amp_ratios=[out.quotient(nullrows[i]['null_amplitude'],nullrows[i+1]['null_amplitude']) for i in (0,1)]
        dominance=all(x['outside4_error_squared_fraction'] is not None and
                      x['outside4_error_squared_fraction']>.8 for x in nullrows)
        reduction=all(x is not None and 2<x<6 for x in ratios)
        ampchecks=[]
        for i,ratio in enumerate(amp_ratios):
            under=all(nullrows[j]['null_amplitude']<1e-10*exact for j in (i,i+1))
            ampchecks.append(dict(below_original_floor=under,ratio=ratio,
                                 original_reduction_passed=under or (ratio is not None and 2<ratio<6)))
        result['regional_diagnosis']=dict(all_outside4_fractions_above_80percent=dominance,
            global_L2_reduction_ratios=ratios,reduction_between2and6=reduction,
            numerical_outer_remainder_dominates=dominance and reduction,
            null_amplitude_reductions=ampchecks,
            limitation='This diagnostic does not pass the original coarse profile gate or authorize M2 runs')
        result['status']='DIAGNOSTIC_COMPLETE'
    except Exception as exc:
        result['error']=repr(exc)
        result['status']='INCOMPLETE' if isinstance(exc,RuntimeError) else 'UNRESOLVED'
    save(args.out,result)
    return 0 if result['status']=='DIAGNOSTIC_COMPLETE' else 2


if __name__=='__main__':
    raise SystemExit(main())
