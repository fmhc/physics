import torch,json,math,time,hashlib,gc
from pathlib import Path
from models import make
P=Path(__file__).resolve().parent
INPUT=Path('/home/fmh/ag-physics-codex/higgs-minima-20261008/results/RESULT.json')
raw=INPUT.read_bytes();assert hashlib.sha256(raw).hexdigest()=='a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9'
assert torch.cuda.is_available();torch.set_num_threads(1);torch.backends.cuda.preferred_linalg_library('cusolver')
dev='cuda';dt=torch.float64;pi=math.pi;a=125**2/(2*246**2*.01);y0=.492;b=.5;eta=.05;Q=600.
out=P/'results';out.mkdir(exist_ok=False)
def T(v):return torch.tensor(v,device=dev,dtype=dt)
def save(name,obj):
 t=out/(name+'.tmp');t.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n');t.replace(out/name)
def norm(x):return torch.linalg.vector_norm(x)
source=json.loads(raw);rows=[];qas=[];comparisons=[];t0=time.perf_counter()
save('PROVENANCE.json',dict(reference_commit='1e885fd0c1c03edef8ff4b2be3b8d983f5d21ac1',gpu=torch.cuda.get_device_name(),torch=torch.__version__,input_sha256=hashlib.sha256(raw).hexdigest(),hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in ['PLAN.md','run.py','models.py','REVIEW.md']},compute='CUDA float64/cuSOLVER all matrix construction, AD, linear solves, norms and eigensystems; CPU IO, control and scalar summaries'))
for stage in ['base','grid','box']:
 old=next(x for x in source if (x['stage'],x['method'],x['seed'])==(stage,'full',0))
 r=T(old['r']);h=old['h'];n=len(r);m=2*n
 eye=torch.eye(m,device=dev,dtype=dt)
 lap=torch.diag(torch.full((n,),2/h**2,device=dev,dtype=dt))+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dt),1)+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dt),-1)
 reduced=make(r,h,lap)
 def full_blocks(u,z,omega,L):
  rho=(u/r)**2;S=rho.sum(0);y=y0+z/r;W=1-2*rho+1.5*rho*rho-.5*rho.flip(0)+b/2*(y*y-y0*y0)-omega**2
  D=torch.zeros((m,m),device=dev,dtype=dt)
  for i in range(2):D[i*n:(i+1)*n,i*n:(i+1)*n]=lap+torch.diag(W[i]+L*(L+1)/r**2)
  D[:n,n:]=D[n:,:n]=torch.diag(torch.full_like(r,-eta));A=D.clone()
  for i in range(2):A[i*n:(i+1)*n,i*n:(i+1)*n]+=torch.diag(-4*rho[i]+6*rho[i]**2)
  cross=torch.diag(-u[0]*u[1]/r**2);A[:n,n:]+=cross;A[n:,:n]+=cross
  C=lap+torch.diag(a*(3*y*y-y0*y0)+b*S+L*(L+1)/r**2)
  B=torch.cat([torch.diag(math.sqrt(2)*b*y*u[i]/r) for i in range(2)],dim=0)
  return A,D,B,C
 def phase_basis(D,u,L):
  vals,V=torch.linalg.eigh((D+D.T)/2);qa={'phase_block_minimum_raw':float(vals[0])}
  if L==0:
   f=u.flatten();over=float((V[:,0]@f)**2/(f@f));ward=float(norm(D@f)/norm(f));qa.update(phase_overlap=over,phase_ward_residual=ward,removed_phase_eigenvalue=float(vals[0]))
   assert abs(float(vals[0]))<1e-6 and over>1-1e-8 and ward<1e-6,qa
   vals,V=vals[1:],V[:,1:]
  assert float(vals[0])>1e-6,qa
  root=V*torch.sqrt(vals)[None,:]
  return vals,root,qa
 def spectrum(name,A,D,Mq,u,omega,L,B=None,C=None,extra=None):
  asym=max(float((X-X.T).abs().max()) for X in [A,D,Mq]);assert asym<1e-8,asym
  A=(A+A.T)/2;D=(D+D.T)/2;Mq=(Mq+Mq.T)/2
  dvals,R,qa=phase_basis(D,u,L);k=len(dvals);Kq=A+4*omega**2*eye;coupling=-2*omega*R
  chol=torch.linalg.cholesky(Mq);mmin=float(torch.linalg.eigvalsh(Mq)[0]);assert mmin>0
  W=torch.linalg.solve_triangular(chol,Kq,upper=False)
  W=torch.linalg.solve_triangular(chol,W.T,upper=False).T
  G=torch.linalg.solve_triangular(chol,coupling,upper=False)
  size=m+k+(n if B is not None else 0);H=torch.zeros((size,size),device=dev,dtype=dt)
  H[:m,:m]=W;H[:m,m:m+k]=G;H[m:m+k,:m]=G.T;H[m:m+k,m:m+k]=torch.diag(dvals)
  if B is not None:
   HB=torch.linalg.solve_triangular(chol,B,upper=False);H[:m,m+k:]=HB;H[m+k:,:m]=HB.T;H[m+k:,m+k:]=C
  hasym=float((H-H.T).abs().max());assert hasym<1e-8;H=(H+H.T)/2
  vals,vecs=torch.linalg.eigh(H);low=vals[:9].clone();V=vecs[:,:9].clone()
  neg=int((vals< -1e-6).sum());minimum=float(vals[0]);maximum=float(vals[-1])
  evres=float((H@V-V*low).norm(dim=0).max()/max(1.,float(low.abs().max())));orth=float((V.T@V-torch.eye(9,device=dev,dtype=dt)).abs().max())
  assert evres<1e-7 and orth<1e-9,(name,evres,orth)
  q=torch.linalg.solve_triangular(chol.T,V[:m],upper=True);w=V[m:m+k];hh=V[m+k:] if B is not None else None
  PP=R@w
  trans=(torch.nn.functional.pad(u,(1,1))[:,2:]-torch.nn.functional.pad(u,(1,1))[:,:-2])/(2*h)-u/r;tv=trans.flatten()
  overlaps=((q.T@tv)**2/(q.square().sum(0)*(tv@tv))).tolist() if L==1 else [0.]*9
  physical=[];charge=[];schur=[];pole=[];hfrac=[]
  cv=torch.linalg.eigvalsh(C) if B is not None else None
  for j in range(9):
   lam=float(low[j])
   if lam<=1e-8:continue
   nu=math.sqrt(lam);qq=q[:,j];pp=(PP[:,j]-2*omega*qq)/nu
   rq=A@qq-lam*(Mq@qq)-2*omega*nu*pp
   rp=D@pp-lam*pp-2*omega*nu*qq
   if B is not None:
    hv=hh[:,j];rq=rq+B@hv;rh=C@hv-lam*hv+B.T@qq
    denom=max(1.,float(norm(A@qq)+norm(B@hv)+lam*norm(qq)+2*omega*nu*norm(pp)))
    er=max(float(norm(rq)),float(norm(rp)),float(norm(rh)))/denom
    distance=float((cv-lam).abs().min());pole.append(distance)
    if distance>1e-7:
     elim=torch.linalg.solve(C-lam*torch.eye(n,device=dev,dtype=dt),B.T@qq)
     se=float(norm((A-lam*eye)@qq-B@elim-2*omega*nu*pp))/denom;schur.append(se);assert se<1e-7,(name,se)
    else:schur.append(None)
    hfrac.append(float(hv.square().sum()/(qq.square().sum()+pp.square().sum()+hv.square().sum())))
   else:
    denom=max(1.,float(norm(A@qq)+lam*norm(Mq@qq)+2*omega*nu*norm(pp)));er=max(float(norm(rq)),float(norm(rp)))/denom
   physical.append(er);assert er<1e-7,(name,er)
   if L==0:
    ff=u.flatten();ce=abs(float(ff@PP[:,j]))/(float(norm(ff))*max(1.,float(norm(PP[:,j]))));charge.append(ce);assert ce<1e-7,(name,ce)
  qa.update(stage=stage,method=name,ell=L,raw_asymmetry=asym,whitened_asymmetry=hasym,mass_minimum=mmin,eigen_residual=evres,orthogonality=orth,original_equations_residuals=physical,linear_charge_residuals=charge,frequency_schur_residuals=schur,higgs_pole_distance=pole)
  if extra:qa.update(extra)
  row=dict(stage=stage,method=name,ell=L,omega=float(omega),h=h,R=old['R'],dimension=size,eigenvalues=low.tolist(),frequencies=[math.sqrt(max(0.,float(x))) for x in low],minimum_all=minimum,maximum_all=maximum,negative_count=neg,growth_max=math.sqrt(max(0.,-minimum)) if minimum < -1e-6 else 0.,translation_overlap_squared=overlaps,higgs_fraction=hfrac)
  rows.append(row);qas.append(qa);save('RESULT.json',rows);save('QA.json',qas)
  print(json.dumps(dict(stage=stage,method=name,ell=L,lowest=low[:3].tolist(),elapsed=time.perf_counter()-t0)),flush=True)
  del H,vals,vecs,V,W,G
  return low,q
 for L in [0,1,2]:
  old=next(x for x in source if (x['stage'],x['method'],x['seed'])==(stage,'full',0));u=T(old['u']);z=T(old['z']);omega=Q/(8*pi*h*u.square().sum())
  A,D,B,C=full_blocks(u,z,omega,L);cc=torch.linalg.cholesky(C);sol=torch.cholesky_solve(B.T,cc);cerr=float(norm(C@sol-B.T)/norm(B));assert cerr<1e-10
  refs={};refs['full']=spectrum('full',A,D,eye,u,omega,L,B,C,{'higgs_minimum':float(torch.linalg.eigvalsh(C)[0]),'schur_solve_error':cerr})
  AR=A-B@sol;MI=eye+sol.T@sol
  refs['Schur-static']=spectrum('Schur-static',AR,D,eye,u,omega,L)
  refs['Schur-inertia']=spectrum('Schur-inertia',AR,D,MI,u,omega,L)
  order1=float((refs['full'][0]-refs['Schur-inertia'][0]).max());order2=float((refs['Schur-inertia'][0]-refs['Schur-static'][0]).max());assert order1<1e-7 and order2<1e-7,(stage,L,order1,order2)
  for method in ['E3','Ecomp']:
   old=next(x for x in source if (x['stage'],x['method'],x['seed'])==(stage,method,0));u=T(old['u']);omega=Q/(8*pi*h*u.square().sum())
   AA,DD,MM,extra=reduced(u,method,L)
   refs[method+'-static']=spectrum(method+'-static',AA,DD,eye,u,omega,L,extra=extra)
   refs[method+'-inertia']=spectrum(method+'-inertia',AA,DD,MM,u,omega,L,extra=extra)
  for name,(vals,q) in refs.items():
   if name=='full':continue
   start=1 if L==1 else 0;v0,q0=refs['full'];vv=vals[start:start+8];rv=v0[start:start+8]
   assert float(rv.min())>1e-6 and float(vv.min())>1e-6,(stage,L,name)
   errors=(torch.sqrt(vv)/torch.sqrt(rv)-1).abs()
   overlaps=((q[:,start:start+8]*q0[:,start:start+8]).sum(0)**2/(q[:,start:start+8].square().sum(0)*q0[:,start:start+8].square().sum(0)))
   comparisons.append(dict(stage=stage,ell=L,method=name,relative_frequency_errors=errors.tolist(),matter_overlap_squared=overlaps.tolist(),ritz_violation_full_inertia=order1,ritz_violation_inertia_static=order2,translation_exclusion_pending_validation=(L==1)))
  save('COMPARISONS.json',comparisons)
  del refs,AA,DD,MM,A,D,B,C,cc,sol,AR,MI;gc.collect();torch.cuda.empty_cache()
 del reduced;gc.collect();torch.cuda.empty_cache()
save('STATUS.json',dict(complete=True,spectra=len(rows),elapsed_seconds=time.perf_counter()-t0,gpu_peak_allocated_bytes=torch.cuda.max_memory_allocated()))
