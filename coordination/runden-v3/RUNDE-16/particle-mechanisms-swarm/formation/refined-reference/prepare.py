#!/usr/bin/env python3
"""New discrete Q1100 references from the archived seed; no branch scan."""
import argparse
import hashlib
import json
import time
from pathlib import Path
import numpy as np

SOURCE_HASH='f831e818b4f2a00f56e281f5972badb1d9ed344dcd2242826ab6b31076917ecb'
SEED_HASH='1bb153a166e15d8ca43848613e638e8e0d20978833be6c564dcf7bc33f926d8c'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--seed',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args(); a.out.mkdir(parents=True,exist_ok=False)
    start=time.process_time()
    result=dict(status='INCOMPLETE',profiles=[],source_hash=sha(Path(__file__).with_name('beutel_source.py')),
                seed_hash=sha(a.seed),code_hash=sha(__file__))
    try:
        if result['source_hash']!=SOURCE_HASH or result['seed_hash']!=SEED_HASH:
            raise ValueError('Source or seed hash differs from prospective provenance')
        import beutel_source as b
        with np.load(a.seed,allow_pickle=False) as z:
            ix=np.flatnonzero((abs(z['Q']-1100)<1e-5)&(z['sweep']=='seed')&
                              (abs(z['omega2']-1.03666310756389)<1e-10))
            if len(ix)!=1: raise ValueError('Ambiguous seed')
            k=int(ix[0]); r=z['r'].astype(float)
            fs=z['f'][k].astype(float); cs=z['g'][k].astype(float)
            omega_seed=float(np.sqrt(z['omega2'][k]))
        M=b.Model('M2')
        for h in (.1,.05):
            G=b.Grid(h,120.)
            f0=np.interp(G.r,r,fs,left=fs[0],right=0)
            c0=np.interp(G.r,r,cs,left=cs[0],right=1)
            lam0=(1100/(2*np.sum(G.V*f0*f0)))**2
            f,c,lam=f0.copy(),c0.copy(),lam0
            E0=b.observables(M,G,f,c,lam)['E']
            row=dict(h=h,iterations=[],initial_E=E0,seed_omega=omega_seed)
            result['profiles'].append(row)
            ok=False
            for it in range(31):
                if not (np.isfinite(lam) and lam>0 and np.all(np.isfinite(f)) and np.all(np.isfinite(c))):
                    raise ValueError('Invalid Newton state before observables; last valid iterate retained in log')
                obs=b.observables(M,G,f,c,lam)
                df=float(np.sqrt(np.sum(G.V*(f-f0)**2)/np.sum(G.V*f0*f0)))
                dc=float(np.sqrt(np.sum(G.V*(c-c0)**2)/np.sum(G.V*(c0-1)**2)))
                qerr=abs(obs['Q']/1100-1)
                err=max(b.resnorm(G,*b.residual(M,G,f,c,lam)),qerr)
                if not all(np.isfinite(x) for x in (df,dc,err,obs['E'],lam)):
                    raise ValueError('Nonfinite Newton state')
                row['iterations'].append(dict(iteration=it,err=err,df=df,dc=dc,
                    omega=obs['omega'],Q=obs['Q'],E=obs['E']))
                if max(df,dc)>.02 or abs(obs['omega']/omega_seed-1)>.01:
                    raise ValueError('Branch-neighbourhood gate failed')
                if f.min()<-1e-10 or c.min()<-1e-8 or c.max()>1+1e-8:
                    raise ValueError('Profile sign/range gate failed')
                if abs(obs['E']/E0-1)>.02:
                    raise ValueError('Energy departure >2%')
                if err<1e-9:
                    ok=True; break
                if it==30: break
                # Exactly one original bordered Newton update, no line search/flow.
                f,c,lam,_,_,_=b.newton_Q(M,G,f,c,lam,1100,tol=1e-9,maxit=1)
            if not ok: raise ValueError('30 Newton steps exhausted')
            if qerr>=1e-10 or obs['E']/1100>=np.sqrt(2):
                raise ValueError('Final Q/free-threshold gate failed')
            # Independently written discrete Hamiltonian cross-check.
            s=f*f
            V=.25*(c*c-1)**2+(1+c*c)*s-s*s+.5*s**3
            E=float(np.sum(G.V*(lam*s+V))+np.sum(G.a*(np.diff(np.append(f,0))**2+
                           .5*np.diff(np.append(c,1))**2))/h)
            if abs(E/obs['E']-1)>=1e-12: raise ValueError('Hamiltonian mismatch')
            path=a.out/('reference-h'+str(h)+'.npz')
            np.savez_compressed(path,r=G.r.astype(np.float64),f=f.astype(np.float64),
                 chi=c.astype(np.float64),omega=np.float64(obs['omega']),Q=np.float64(obs['Q']),
                 h=np.float64(h),seed_sha256=SEED_HASH,source_sha256=SOURCE_HASH)
            row.update(file=path.name,sha256=sha(path),E=E,omega=obs['omega'],Q=obs['Q'],
                       converged=True,final_residual=err)
        if abs(result['profiles'][0]['E']/result['profiles'][1]['E']-1)>=1e-3:
            raise ValueError('Cross-grid energy sensitivity >=1e-3')
        result['status']='PREPARED_REFERENCES'
    except Exception as exc:
        result['error']=repr(exc)
    result['cpu_seconds']=time.process_time()-start
    (a.out/'MANIFEST.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    return 0 if result['status']=='PREPARED_REFERENCES' else 2


if __name__=='__main__':
    raise SystemExit(main())
