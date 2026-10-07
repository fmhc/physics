#!/usr/bin/env python3
"""Bounded radial M2 mode candidates, six coupled blocks. Not executed by author."""
import time
CPU_START=time.process_time()
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs,ArpackNoConvergence

HASHES={.1:'8265a508c85b5823e1a46f47ea3a9cadb26c790fe89f8ad711699164483d3adb',
        .05:'bf03078bb52e4fe515cb3a5fbd01608efec3df18b8845a3ae37aaef6c9661011'}
GRIDS=((120.,.1),(120.,.05),(60.,.1),(60.,.05))
SHIFTS=(.10,.30)


def checkpoint():
    if time.process_time()-CPU_START>=25:
        raise RuntimeError('INCOMPLETE: internal 25 CPU-s checkpoint')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(out,result):
    result['cpu_seconds']=time.process_time()-CPU_START
    temp=out/'RESULT.tmp'
    temp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    temp.replace(out/'RESULT.json')


def grid(radius,h):
    n=int(round(radius/h)); r=(np.arange(n)+.5)*h
    vol=4*np.pi*h*(r*r+h*h/12); root=np.sqrt(vol)
    edge=4*np.pi*((np.arange(n)+1)*h)**2/h
    diagonal=edge+np.r_[0.,edge[:-1]]
    D=sparse.diags((-edge[:-1]/(root[:-1]*root[1:]),diagonal/vol,
                    -edge[:-1]/(root[:-1]*root[1:])),(-1,0,1),format='csc')
    return dict(n=n,r=r,h=h,R=radius,vol=vol,root=root,D=D)


def operators(g,f,c,omega):
    s=f*f; D=g['D']; n=g['n']; I=sparse.eye(n,format='csc')
    plus=D+sparse.diags(1+c*c-omega*omega-6*s+7.5*s*s)
    minus=D+sparse.diags(1+c*c-omega*omega-2*s+1.5*s*s)
    chi=D+sparse.diags(3*c*c-1+2*s)
    C=sparse.diags(2*np.sqrt(2)*c*f)
    K=sparse.bmat([[plus,None,C],[None,minus,None],[C,None,chi]],format='csc')
    G=sparse.bmat([[None,-2*omega*I,None],[2*omega*I,None,None],
                  [None,None,sparse.csc_matrix((n,n))]],format='csc')
    zero=sparse.csc_matrix((3*n,3*n)); identity=sparse.eye(3*n,format='csc')
    A=sparse.bmat([[zero,identity],[-K,-G]],format='csc')
    return A,K,G,(plus,minus,chi,C)


def load_refs(directory):
    directory=Path(directory); manifest=json.loads((directory/'MANIFEST.json').read_text())
    if manifest['status']!='PREPARED_REFERENCES': raise ValueError('Invalid reference manifest')
    refs={}; meta=[]
    for row in manifest['profiles']:
        h=float(row['h']); path=directory/row['file']; digest=sha(path)
        if h not in HASHES or digest!=HASHES[h] or digest!=row['sha256']:
            raise ValueError('Reference provenance mismatch')
        with np.load(path,allow_pickle=False) as z:
            full=grid(120,h)
            if not np.array_equal(z['r'],full['r']): raise ValueError('Reference grid mismatch')
            if z['f'].dtype!=np.float64 or z['chi'].dtype!=np.float64:
                raise ValueError('Reference not float64')
            refs[h]=(z['f'].copy(),z['chi'].copy(),float(z['omega']))
        meta.append(dict(h=h,sha256=digest,file=str(path)))
    if set(refs)!=set(HASHES): raise ValueError('Missing reference grid')
    return refs,dict(manifest_sha256=sha(directory/'MANIFEST.json'),profiles=meta)


def profile_check(g,f,c,omega,fullcharge):
    root=g['root']; s=f*f
    rp=(g['D']@(root*f))/root+(1+c*c-omega*omega-2*s+1.5*s*s)*f
    rc=(g['D']@(root*(c-1)))/root+c*(c*c-1+2*s)
    q=2*omega*np.sum(g['vol']*s)
    remainder=abs(q/fullcharge-1)
    err=float(max(np.max(abs(rp)),np.max(abs(rc))))
    A,_,_,_=operators(g,f,c,omega)
    phase=np.zeros(6*g['n']); phase[g['n']:2*g['n']]=root*f
    ph=float(np.linalg.norm(A@phase)/np.linalg.norm(phase))
    row=dict(stationary_max=err,truncated_charge_fraction=float(remainder),phase_anchor=ph)
    row['passed']=err<1e-8 and remainder<1e-10 and ph<1e-8
    return row


def qa():
    # Mixed x/z derivative of the rotating potential in canonical coordinates.
    g=grid(4,.1); r=g['r']; vol=g['vol']
    f=.5*np.exp(-r*r/4); c=1-.3*np.exp(-r*r/3)
    x=.3*np.exp(-r*r/5); z=.4*np.exp(-r*r/6); eps=1e-5; omega=1.0181382710767997
    def gx(ch):
        s=f*f
        return np.sqrt(2)*(1+ch*ch-2*s+1.5*s*s-omega*omega)*f
    numerical=np.sum(vol*x*(gx(c+eps*z)-gx(c-eps*z)))/(2*eps)
    exact=np.sum(vol*x*(2*np.sqrt(2)*c*f)*z)
    mixed_error=float(abs(numerical-exact)/max(1,abs(exact)))
    mutant_error=float(abs(numerical-2*exact)/max(1,abs(exact)))
    if mixed_error>=1e-7 or mutant_error<=1e-3:
        raise ValueError('Mixed canonical derivative QA failed')
    # Independent full quadratic Hessian directional derivative in canonical fields.
    y=.2*np.exp(-r*r/7); q=np.concatenate([g['root']*a for a in (x,y,z)])
    _,K,_,_=operators(g,f,c,omega)
    def gradient(e):
        a=f+e*x/np.sqrt(2); b=e*y/np.sqrt(2); ch=c+e*z
        s=a*a+b*b; F=1+ch*ch-2*s+1.5*s*s-omega*omega
        return np.concatenate((g['root']*np.sqrt(2)*F*a,
                               g['root']*np.sqrt(2)*F*b,
                               g['root']*ch*(ch*ch-1+2*s)))
    spatial=sparse.block_diag([g['D']]*3,format='csc')
    numeric=(gradient(eps)-gradient(-eps))/(2*eps)+spatial@q
    hessian_error=float(np.linalg.norm(numeric-K@q)/max(1,np.linalg.norm(K@q)))
    if hessian_error>=1e-7: raise ValueError('Full Hessian derivative QA failed')
    # Free finite-volume channels: a small independent dense eigenvalue comparison.
    zero=np.zeros(g['n']); one=np.ones(g['n'])
    A,_,_,_=operators(g,zero,one,omega)
    d=np.linalg.eigvalsh(g['D'].toarray()); nu=np.sqrt(d+2)
    expected=np.sort(np.r_[nu-omega,nu+omega,nu])
    vals=np.linalg.eigvals(A.toarray())
    got=np.sort(vals.imag[vals.imag>1e-8])
    if len(got)!=len(expected): raise ValueError('Free channel count mismatch')
    free_error=float(np.max(abs(got-expected)))
    real_error=float(np.max(abs(vals.real)))
    if max(free_error,real_error)>=1e-8 or got[0]<=np.sqrt(2)-omega:
        raise ValueError('Free negative/channel QA failed')
    return dict(mixed_derivative_error=mixed_error,mutant_error=mutant_error,
                hessian_error=hessian_error,free_frequency_error=free_error,
                free_real_error=real_error,free_lowest=float(got[0]))


def diagnostic(g,f,omega,A,K,G,blocks,value,vector):
    n=g['n']; q=vector[:3*n].copy(); p=vector[3*n:].copy()
    scale=np.linalg.norm(q)
    if scale==0: raise ValueError('Zero eigenvector position block')
    q/=scale; p/=scale; whole=np.r_[q,p]
    rho=float(value.imag)
    av=A@whole
    residual=float(np.linalg.norm(av-value*whole)/(np.linalg.norm(av)+abs(value)*np.linalg.norm(whole)+1e-14))
    # Direct quadratic pencil, independent assembly from its four blocks.
    u=q[:n]; v=1j*q[n:2*n]; w=q[2*n:]
    plus,minus,chi,C=blocks
    terms=(plus@u,minus@v,chi@w)
    cross=(C@w,C@u)
    harmonic=np.r_[u,v,w]
    gyro=np.r_[-2*omega*rho*v,-2*omega*rho*u,np.zeros(n)]
    spatial=np.r_[terms[0]+cross[0],terms[1],terms[2]+cross[1]]
    quad=spatial-rho*rho*harmonic+gyro
    qr=float(np.linalg.norm(quad)/(np.linalg.norm(spatial)+rho*rho*np.linalg.norm(harmonic)+np.linalg.norm(gyro)+1e-14))
    ff=g['root']*f
    delta=np.sqrt(2)*np.sum(ff*(2*omega*q[:n]+p[n:2*n]))
    denom=np.sqrt(2)*np.linalg.norm(ff)*(2*omega*np.linalg.norm(q[:n])+np.linalg.norm(p[n:2*n]))+1e-14
    charge_error=float(abs(delta)/denom)
    density=np.sum(abs(q.reshape(3,n))**2,axis=0)
    tail=float(np.sum(density[g['r']>20])/np.sum(density))
    cumulative=np.cumsum(density); j=int(np.searchsorted(cumulative,.5*cumulative[-1]))
    previous=0 if j==0 else cumulative[j-1]
    fraction=(.5*cumulative[-1]-previous)/(cumulative[j]-previous)
    r50=float(((j*g['h'])**3+fraction*((j+1)**3-j**3)*g['h']**3)**(1/3))
    passed=(abs(value.real)<1e-7 and .001<rho<np.sqrt(2)-omega-.001
            and residual<1e-8 and qr<1e-8 and charge_error<1e-7 and tail<1e-4 and r50<12)
    row=dict(lambda_real=float(value.real),rho=rho,first_order_residual=residual,
             quadratic_residual=qr,deltaQ_scaled=charge_error,outer20_fraction=tail,
             canonical_radius50=r50,candidate=bool(passed))
    return row,q


def restrict(q,source,target):
    # Fields q/sqrtV averaged by exact cell volumes, then transformed back.
    field=q.reshape(3,source['n'])/source['root']
    count=int(round(target['R']/source['h']))
    field=field[:,:count]; weight=source['vol'][:count]
    ratio=int(round(target['h']/source['h']))
    if ratio<1 or abs(ratio*source['h']-target['h'])>1e-12:
        raise ValueError('Restriction requires aligned coarser grid')
    avg=np.sum((field*weight).reshape(3,target['n'],ratio),axis=2)/target['vol']
    mapped=(avg*target['root']).reshape(-1)
    retained=float(np.sum(abs(q.reshape(3,source['n'])[:,:count])**2))
    return mapped,retained


def overlap(left,lg,right,rg):
    common=grid(min(lg['R'],rg['R']),max(lg['h'],rg['h']))
    l,ln=restrict(left,lg,common); r,rn=restrict(right,rg,common)
    ov=float(abs(np.vdot(l,r))/(np.linalg.norm(l)*np.linalg.norm(r)))
    return ov,ln,rn


def compare(candidates,grids):
    anchor=(120.,.1); results=[]
    # No frequency-only equivalence: every match requires phase-invariant overlap.
    unique={}
    for key in GRIDS:
        unique[key]=[]
        for row,q in candidates[key]:
            if not any(abs(row['rho']-rr['rho'])<1e-6 and
                       overlap(q,grids[key],qq,grids[key])[0]>.999
                       for rr,qq in unique[key]): unique[key].append((row,q))
    for row,q in unique[anchor]:
        record=dict(anchor_rho=row['rho'],matches=[],confirmed=True)
        for key in GRIDS[1:]:
            matches=[]
            for rr,qq in unique[key]:
                delta=abs(rr['rho']-row['rho']); ov,ln,rn=overlap(q,grids[anchor],qq,grids[key])
                if delta<5e-4 and ov>.98:
                    matches.append(dict(R=key[0],h=key[1],rho=rr['rho'],delta_rho=delta,
                                        overlap=ov,anchor_retained_norm=ln,target_retained_norm=rn))
            # Duplicates from shifts allowed if same frequency; nearby ambiguity unresolved.
            matches.sort(key=lambda x:x['delta_rho'])
            if not matches: record['confirmed']=False
            elif len(matches)>1:
                record['confirmed']=False
                record['matches'].append(dict(R=key[0],h=key[1],ambiguous_matches=matches))
            else: record['matches'].append(matches[0])
        results.append(record)
    return results


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--reference',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--qa-only',action='store_true')
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',code_sha256=sha(__file__),tasks=[],profile_checks=[],
                execution='CPU float64/complex128; no CUDA',completeness_claim=False)
    candidates={}; grids={}
    try:
        refs,meta=load_refs(args.reference); result['reference']=meta
        result['qa']=qa(); save(args.out,result); checkpoint()
        for radius,h in GRIDS:
            checkpoint(); g=grid(radius,h); fullf,fullc,omega=refs[h]
            full=grid(120,h); fq=2*omega*np.sum(full['vol']*fullf*fullf)
            f=fullf[:g['n']]; c=fullc[:g['n']]
            check=profile_check(g,f,c,omega,fq); check.update(R=radius,h=h)
            result['profile_checks'].append(check); save(args.out,result)
            if not check['passed']: raise ValueError('Background/phase/box gate failed')
            if args.qa_only: continue
            A,K,G,blocks=operators(g,f,c,omega); A=A.astype(complex)
            candidates[(radius,h)]=[]; grids[(radius,h)]=g
            index=np.arange(6*g['n'],dtype=float)
            start=(1+.1*np.cos(index*.17))+1j*.1*np.sin(index*.11)
            start/=np.linalg.norm(start)
            for shift in SHIFTS:
                checkpoint(); before=time.process_time()
                task=dict(R=radius,h=h,shift=shift,complete=False,ritz=[])
                result['tasks'].append(task); save(args.out,result)
                try:
                    values,vectors=eigs(A,k=4,sigma=1j*shift,which='LM',ncv=20,
                        tol=1e-9,maxiter=300,v0=start)
                    complete=True
                except ArpackNoConvergence as exc:
                    values,vectors=exc.eigenvalues,exc.eigenvectors; complete=False
                if values is not None:
                    for j,value in enumerate(values):
                        row,q=diagnostic(g,f,omega,A,K,G,blocks,value,vectors[:,j])
                        task['ritz'].append(row)
                        if row['candidate']: candidates[(radius,h)].append((row,q))
                    name=f'R{radius:g}-h{h}-shift{shift}.npz'
                    np.savez_compressed(args.out/name,eigenvalues=values,eigenvectors=vectors)
                    task['artifact']=name; task['artifact_sha256']=sha(args.out/name)
                task['complete']=complete; task['cpu_seconds']=time.process_time()-before
                save(args.out,result)
                if not complete: raise RuntimeError('INCOMPLETE ARPACK convergence')
                checkpoint()
        if args.qa_only: result['status']='QA_ONLY_COMPLETE'
        else:
            result['matches']=compare(candidates,grids)
            result['status']=('LOCALIZED_INTERNAL_MODE_CANDIDATE' if
                any(x['confirmed'] for x in result['matches']) else 'NO_CONFIRMED_CANDIDATE_IN_FIXED_SEARCH')
    except Exception as exc:
        result['error']=repr(exc)
        result['status']='INCOMPLETE' if isinstance(exc,RuntimeError) else 'NUMERICALLY_UNRESOLVED'
    save(args.out,result)
    return 0 if result['status'] not in ('INCOMPLETE','NUMERICALLY_UNRESOLVED') else 2


if __name__=='__main__':
    raise SystemExit(main())
