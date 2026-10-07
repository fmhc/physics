"""Exploratory overdamped proxy; run on TS440 only. See VORAB.md."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import resource
resource.setrlimit(resource.RLIMIT_CPU,(590,600))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
import numpy as np
import json,time
from pathlib import Path
start=time.monotonic(); cpu=time.process_time(); out=Path(__file__).parent
N=50; EPS=.15

def rhs(x,theta,model,J,K):
    d=x[None,:,:]-x[:,None,:]
    r=np.sqrt(np.sum(d*d,axis=2)+EPS**2)
    delta=theta[None,:]-theta[:,None]
    if model=='vfw_proxy':
        phase=J*np.cos(delta)/r**3
        full=phase-.05/r**4
    else:
        phase=J*np.cos(delta)/r
        full=1/r+phase-1/r**2
    dx=np.sum(d*full[:,:,None],axis=1)/N
    dp=K*np.sum(np.sin(delta)/r,axis=1)/N
    return dx,dp,np.sum(d*phase[:,:,None],axis=1)/N

def metrics(x,p,model,J,K):
    d=x[None,:,:]-x[:,None,:]
    dist=np.linalg.norm(d,axis=2)
    toward=x[:-1].mean(axis=0)-x[-1]
    norm=np.linalg.norm(toward); toward=toward/max(norm,1e-30)
    v=rhs(x,p,model,J,K)[2][-1]
    m=dict(R=float(abs(np.exp(1j*p).mean())),D=float(dist.sum()/(N*(N-1))),probe=float(v@toward))
    if x.shape[1]==2:
        rel=x-x.mean(axis=0); ang=np.arctan2(rel[:,1],rel[:,0])
        m.update(Splus=float(abs(np.exp(1j*(ang+p)).mean())),Sminus=float(abs(np.exp(1j*(ang-p)).mean())))
    else: m.update(Splus=None,Sminus=None)
    return m

def phase_average(x,p,model,J,K):
    # Frozen positions/source phases; quadrature only over marked probe phase.
    vals=[]
    for angle in np.arange(64)*2*np.pi/64:
        q=p.copy();q[-1]=angle
        vals.append(rhs(x,q,model,J,K)[2][-1])
    return float(np.max(np.abs(np.mean(vals,axis=0))))

records=[]; checks=[]
# Pair sign/J reversal, using the same RHS at the required N.
x=np.zeros((N,1));x[1:,0]=1;p=np.zeros(N)
for model in ('vfw_proxy','standard'):
    plus=rhs(x,p,model,.8,0)[2][0,0]
    p[1:]=np.pi;minus=rhs(x,p,model,.8,0)[2][0,0];p[:]=0
    reverse=rhs(x,p,model,-.8,0)[2][0,0]
    checks.append(dict(model=model,pair_sign=bool(plus>0 and minus<0),reverse_error=abs(float(plus+reverse))))

for dim in (1,2):
 for seed in (31,73):
  rng=np.random.default_rng(seed);x0=rng.uniform(-1,1,(N,dim));x0[-1]=0;x0[-1,0]=3
  p0=rng.uniform(-np.pi,np.pi,N)
  for model in ('vfw_proxy','standard'):
   for arm,J,K in (('main',.8,.8),('K0',.8,0),('reverseJ',-.8,.8),('sync',.8,.8)):
    for dt in (.02,.01):
     x=x0.copy();p=np.zeros(N) if arm=='sync' else p0.copy();initial_p=p.copy()
     first=metrics(x,p,model,J,K);trace=[dict(t=0,**first)]
     nullmax=phase_average(x,p,model,J,K)
     for step in range(round(4/dt)):
        dx,dp,_=rhs(x,p,model,J,K)
        ex,ep,_=rhs(x+dt*dx,p+dt*dp,model,J,K)
        x+=dt*(dx+ex)/2;p+=dt*(dp+ep)/2
        if not (np.isfinite(x).all() and np.isfinite(p).all()):raise RuntimeError('nonfinite')
        if (step+1)%round(.2/dt)==0:trace.append(dict(t=(step+1)*dt,**metrics(x,p,model,J,K)))
     nullmax=max(nullmax,phase_average(x,p,model,J,K))
     end=metrics(x,p,model,J,K)
     center=float(np.max(np.abs(x.mean(axis=0)-x0.mean(axis=0))))
     frozen=float(np.max(np.abs(p-initial_p))) if K==0 else None
     valid=nullmax<=1e-12 and center<=1e-10 and (frozen is None or frozen==0) and (arm!='sync' or abs(end['R']-1)<1e-12)
     rec=dict(dim=dim,seed=seed,model=model,arm=arm,dt=dt,initial=first,end=end,trace=trace,null_error=nullmax,center_error=center,frozen_error=frozen,valid=bool(valid))
     records.append(rec)
     np.savez_compressed(out/f'{model}-{dim}-{seed}-{arm}-{dt}.npz',x=x,phase=p,x0=x0,phase0=initial_p)
     payload=dict(host=os.uname().nodename,wall_seconds=time.monotonic()-start,cpu_seconds=time.process_time()-cpu,checks=checks,records=records)
     temp=out/'RESULT.tmp';temp.write_text(json.dumps(payload));temp.replace(out/'RESULT.json')
print(json.dumps(dict(runs=len(records),valid=sum(r['valid'] for r in records),wall_seconds=time.monotonic()-start,cpu_seconds=time.process_time()-cpu)))
