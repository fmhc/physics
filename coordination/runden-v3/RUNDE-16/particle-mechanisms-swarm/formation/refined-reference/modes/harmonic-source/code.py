#!/usr/bin/env python3
"""Local quadratic source diagnostics only. No evolution/eigenvalue solve."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

DYN='466b25fb813770a1ab13eea962c93b39308dfe1ad22171fe638c60fdafef998d'
OP='467ad3e19cd8efcdac4ec2dcc670b50aaa59cc6f7e9e44d625ebbf94ba0d32c6'
RES='77ecf9bbe03b96db901d76728e074a897725eb52213f90dae76c7200ba5364ea'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path,expected,name):
    if sha(path)!=expected: raise ValueError('Module hash mismatch')
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec); spec.loader.exec_module(obj)
    return obj


def source(f,g,direction):
    x,y,z=direction; s=f*f
    a=-2+3*s; b=-3+7.5*s; c=-1+1.5*s
    return np.array([-np.sqrt(2)*f*(z*z+b*x*x+c*y*y)-2*g*x*z,
                     -2*g*y*z-np.sqrt(2)*f*a*x*y,
                     -3*g*z*z-2*np.sqrt(2)*f*x*z-g*(x*x+y*y)])


def norm(vol,x):
    return float(np.sqrt(np.sum(vol*abs(x)**2)))


def qa(dyn):
    grid=dyn.Grid(.1,8); r=grid.r; vol=grid.vol
    f=.6*np.exp(-r*r/9); g=1-.3*np.exp(-r*r/7)
    directions=np.array([.2*np.exp(-r*r/5),.17*np.exp(-r*r/6),.13*np.exp(-r*r/4)])
    exact=source(f,g,directions); denominator=norm(vol,exact)
    def accel(e):
        x,y,z=directions
        ap,ac=dyn.forces(grid,f+e*(x+1j*y)/np.sqrt(2),g+e*z)
        return np.array([np.sqrt(2)*ap.real,np.sqrt(2)*ap.imag,ac])
    zero=accel(0); errors=[]
    for step in (.02,.01,.005):
        numerical=(accel(step)-2*zero+accel(-step))/(2*step*step)
        errors.append(norm(vol,numerical-exact)/denominator)
    ratios=[errors[i]/errors[i+1] if errors[i+1]>0 else None for i in (0,1)]
    factor=norm(vol,numerical-2*exact)/denominator
    sign=norm(vol,numerical+exact)/denominator
    complex_direction=directions*np.array([1+.3j,.7-.4j,.8+.2j])[:,None]
    dc=.5*(source(f,g,complex_direction.real)+source(f,g,complex_direction.imag))
    twice=source(f,g,complex_direction)/4
    samples=[]
    phases=np.arange(8)*2*np.pi/8
    for theta in phases:
        samples.append(source(f,g,np.real(complex_direction*np.exp(1j*theta))))
    samples=np.array(samples)
    measured_dc=np.mean(samples,axis=0)
    measured_twice=np.mean(samples*np.exp(-2j*phases)[:,None,None],axis=0)
    dc_error=norm(vol,measured_dc-dc)/norm(vol,dc)
    twice_error=norm(vol,measured_twice-twice)/norm(vol,twice)
    passed=(errors[-1]<1e-5 and all(r is not None and 2<r<6 for r in ratios)
            and factor>.1 and sign>.1 and max(dc_error,twice_error)<1e-12)
    return dict(passed=bool(passed),steps=[.02,.01,.005],relative_errors=errors,
                error_reduction_ratios=ratios,wrong_factor_error=factor,wrong_sign_error=sign,
                fourier_dc_error=dc_error,fourier_second_error=twice_error)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--dynamics',type=Path,required=True)
    parser.add_argument('--operator',type=Path,required=True)
    parser.add_argument('--search-dir',type=Path,required=True)
    parser.add_argument('--reference',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',code_sha256=sha(__file__),profiles=[],
        minus_convention='Local (J2x-i J2y)/sqrt2 is conjugate of the lower lab sideband Fourier coefficient; norms unchanged.',
        interpretation='Local source only; no outgoing amplitude, radiation rate or gate reclassification')
    try:
        dyn=module(args.dynamics,DYN,'existing_forces')
        op=module(args.operator,OP,'existing_mode_loader')
        path=args.search_dir/'RESULT.json'
        if sha(path)!=RES: raise ValueError('Search result hash mismatch')
        old=json.loads(path.read_text()); refs,meta=op.load_refs(args.reference)
        if old['reference']['manifest_sha256']!=meta['manifest_sha256'] or old['code_sha256']!=OP:
            raise ValueError('Reference/operator provenance mismatch')
        result.update(dynamics_sha256=DYN,operator_sha256=OP,search_sha256=RES,reference=meta,
                      original_search_status=old['status'])
        result['qa']=qa(dyn)
        if not result['qa']['passed']: raise ValueError('Quadratic source QA failed')
        sources={}; grids={}
        for h in (.1,.05):
            tasks=[t for t in old['tasks'] if t['R']==120 and t['h']==h and t['shift']==.3]
            if len(tasks)!=1 or not tasks[0]['complete']: raise ValueError('Ritz task missing')
            task=tasks[0]; file=args.search_dir/task['artifact']
            if sha(file)!=task['artifact_sha256']: raise ValueError('Ritz artifact mismatch')
            with np.load(file,allow_pickle=False) as z:
                values=z['eigenvalues']; ix=np.flatnonzero((values.imag>.38)&(values.imag<.39))
                if len(ix)!=1: raise ValueError('Ritz selection ambiguous')
                j=int(ix[0]); value=values[j]; eigenvector=z['eigenvectors'][:,j].copy()
            if abs(value.imag-task['ritz'][j]['rho'])>1e-12 or abs(value.real-task['ritz'][j]['lambda_real'])>1e-12:
                raise ValueError('Ritz row mismatch')
            grid=op.grid(120,h); n=grid['n']; vol=grid['vol']
            if len(eigenvector)!=6*n or not np.all(np.isfinite(eigenvector)):
                raise ValueError('Ritz vector invalid')
            q=eigenvector[:3*n]; original_norm=float(np.linalg.norm(q))
            if original_norm==0: raise ValueError('Zero Ritz q')
            physq=(q/original_norm).reshape(3,n)/grid['root']
            f,g,omega=refs[h]; rho=float(value.imag)
            j2=source(f,g,physq)/4
            dc=.5*(source(f,g,physq.real)+source(f,g,physq.imag))
            channels=np.array([(j2[0]+1j*j2[1])/np.sqrt(2),
                               (j2[0]-1j*j2[1])/np.sqrt(2),j2[2]])
            norms={name:norm(vol,channels[k]) for k,name in enumerate(('plus','minus','chi'))}
            tail={}
            for k,name in enumerate(('plus','minus','chi')):
                total=norm(vol,channels[k])**2
                tail[name]=float(np.sum(vol[grid['r']>20]*abs(channels[k,grid['r']>20])**2)/total) if total>0 else None
            filename=f'SOURCE-h{h}.npz'
            np.savez_compressed(args.out/filename,r=grid['r'],DC=dc,J2=j2,local_channels=channels,
                                rho=rho,omega=omega,canonical_q_normalization=1.)
            row=dict(h=h,R=120,rho=rho,omega=omega,second_frequency=2*rho,
                original_qnorm=original_norm,source_artifact=filename,source_sha256=sha(args.out/filename),
                ritz_sha256=task['artifact_sha256'],
                free_wavenumber_squared=[(omega+2*rho)**2-2,(omega-2*rho)**2-2,(2*rho)**2-2],
                DC_component_L2=[norm(vol,x) for x in dc],J2_component_L2=[norm(vol,x) for x in j2],
                local_channel_L2=norms,local_channel_outer20_fraction=tail)
            result['profiles'].append(row); sources[h]=(dc,j2); grids[h]=grid
        result['grid_comparison']={}
        for index,name in enumerate(('DC','J2')):
            coarse=sources[.1][index]; fine=sources[.05][index]
            weighted=(fine*grids[.05]['root']).reshape(-1)
            mapped,_=op.restrict(weighted,grids[.05],grids[.1])
            mapped=mapped.reshape(3,-1)/grids[.1]['root']
            vol=grids[.1]['vol']; coarse_norm=norm(vol,coarse); fine_norm=norm(grids[.05]['vol'],fine)
            denom=coarse_norm*norm(vol,mapped)
            overlap=float(abs(np.sum(vol*np.conj(coarse)*mapped))/denom) if denom>0 else None
            result['grid_comparison'][name]=dict(coarse_L2=coarse_norm,fine_L2=fine_norm,
                raw_norm_difference=fine_norm-coarse_norm,
                absolute_profile_difference_L2=norm(vol,abs(mapped)-abs(coarse)),
                absolute_hermitian_overlap=overlap)
        result['status']='LOCAL_SOURCE_DIAGNOSTICS_COMPLETE'
    except Exception as exc:
        result['status']='UNRESOLVED'; result['error']=repr(exc)
    (args.out/'RESULT.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    return 0 if result['status']=='LOCAL_SOURCE_DIAGNOSTICS_COMPLETE' else 2


if __name__=='__main__':
    raise SystemExit(main())
