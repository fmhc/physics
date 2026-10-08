import torch,json,math,time,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
inp=P.parent/'higgs-minima-20261008/results/RESULT.json'
raw=inp.read_bytes();assert hashlib.sha256(raw).hexdigest()=='a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9'
assert torch.cuda.is_available();torch.set_num_threads(1);torch.backends.cuda.preferred_linalg_library('cusolver')
dev='cuda';dt=torch.float64;pi=math.pi;a=125**2/(2*246**2*.01);y0=.492;b=.5;eta=.05;Q=600.
out=P/'results';out.mkdir(exist_ok=False)
def T(v):return torch.tensor(v,device=dev,dtype=dt)
def save(n,v):
 t=out/(n+'.tmp');t.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n');t.replace(out/n)
save('PROVENANCE.json',dict(gpu=torch.cuda.get_device_name(),torch=torch.__version__,compute='CUDA float64 Hessians, solves, norms, eigensystems; CPU IO/control',input_sha256=hashlib.sha256(raw).hexdigest(),hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['PLAN.md','run.py']}))
source=json.loads(raw);rows=[];checks=[];comparisons=[];begin=time.perf_counter()
for stage in ['base','grid','box']:
 old=next(x for x in source if (x['stage'],x['method'],x['seed'])==(stage,'full',0));r=T(old['r']);h=old['h'];n=len(r);N=n+1
 lap=torch.diag(torch.full((n,),2/h**2,device=dev,dtype=dt))+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dt),1)+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dt),-1)
 eig=4/h**2*torch.sin(pi*torch.arange(2*N,device=dev,dtype=dt)/(2*N))**2+6.25
 def inv(q):
  odd=torch.cat((torch.zeros_like(q[...,:1]),q,torch.zeros_like(q[...,:1]),-q.flip(-1)),dim=-1)
  return torch.fft.ifft(torch.fft.fft(odd)/eig).real[...,1:N]
 def eh(S,method):
  z1=-inv(b*y0*r*S);z2=-inv(b*S*z1+3*a*y0*z1*z1/r)
  if method=='E3':return 4*pi*h*(.5*b*y0*r*S*z1+b/2*S*z1*z1+a*y0*z1**3/r).sum()
  z=z1+z2;D=(y0+z/r)**2-y0*y0
  return 4*pi*h*(.5*torch.nn.functional.pad(z,(1,1)).diff().square().sum()/h**2+(r*r*(a/4*D*D+b/2*D*S)).sum())
 def energy(ur,vi,method):
  rho=(ur*ur+vi*vi)/r**2;S=rho.sum(0);I=4*pi*h*(ur*ur+vi*vi).sum()
  kin=4*pi/h*(torch.nn.functional.pad(ur,(1,1)).diff(dim=-1).square().sum()+torch.nn.functional.pad(vi,(1,1)).diff(dim=-1).square().sum())
  pot=(rho-rho*rho+.5*rho**3).sum(0)-.5*rho[0]*rho[1]-2*eta*(ur[0]*ur[1]+vi[0]*vi[1])/r**2
  return (Q**2/(4*I)+kin+4*pi*h*(r*r*pot).sum()+eh(S,method))/(8*pi*h)
 def imag_matrix(u,C,omega):
  rho=(u/r)**2;W=1-2*rho+1.5*rho*rho-.5*rho.flip(0)+C-omega**2
  H=torch.zeros((2*n,2*n),device=dev,dtype=dt)
  H[:n,:n]=lap+torch.diag(W[0]);H[n:,n:]=lap+torch.diag(W[1]);H[:n,n:]=H[n:,:n]=torch.diag(torch.full((n,),-eta,device=dev,dtype=dt))
  return H
 refs={}
 for method in ['full','E3','Ecomp']:
  old=next(x for x in source if (x['stage'],x['method'],x['seed'])==(stage,method,0));u=T(old['u']);omega=Q/(8*pi*h*u.square().sum());qa=dict(stage=stage,method=method)
  if method=='full':
   z=T(old['z']);rho=(u/r)**2;S=rho.sum(0);y=y0+z/r;D=y*y-y0*y0
   Hm=imag_matrix(u,b/2*D,omega);A=Hm.clone();A[:n,:n]+=torch.diag(-4*rho[0]+6*rho[0]**2);A[n:,n:]+=torch.diag(-4*rho[1]+6*rho[1]**2)
   cross=torch.diag(-u[0]*u[1]/r**2);A[:n,n:]+=cross;A[n:,:n]+=cross
   A+=4*omega**2*torch.outer(u.flatten(),u.flatten())/u.square().sum()
   C=lap+torch.diag(a*(3*y*y-y0*y0)+b*S);B=torch.cat([torch.diag(math.sqrt(2)*b*y*u[i]/r) for i in range(2)],dim=0)
   cmin=float(torch.linalg.eigvalsh(C)[0]);assert cmin>0;chol=torch.linalg.cholesky(C);sol=torch.cholesky_solve(B.T,chol)
   sr=float((C@sol-B.T).norm()/B.norm());assert sr<1e-10;Hr=A-B@sol;qa.update(higgs_block_minimum=cmin,schur_solve_relative_residual=sr)
  else:
   x=u.flatten().detach().requires_grad_(True);E=energy(x.reshape(2,n),torch.zeros_like(u),method);g=torch.autograd.grad(E,x,create_graph=True)[0];Hr=torch.empty((2*n,2*n),device=dev,dtype=dt)
   for start in range(0,2*n,32):
    count=min(32,2*n-start);basis=torch.zeros((count,2*n),device=dev,dtype=dt);basis[torch.arange(count,device=dev),torch.arange(start,start+count,device=dev)]=1
    Hr[start:start+count]=torch.autograd.grad(g,x,grad_outputs=basis,is_grads_batched=True,retain_graph=True)[0].detach()
   S=(u/r).square().sum(0).requires_grad_(True);Cportal=torch.autograd.grad(eh(S,method),S)[0]/(4*pi*h*r*r);Hm=imag_matrix(u,Cportal.detach(),omega)
   fd={};direction=torch.stack([r*torch.exp(-r*r/16)*torch.sin((i+1)*.7*r+.2*i) for i in range(2)]);direction*=u.norm()/direction.norm()
   for sector,H in [('real',Hr),('imag',Hm)]:
    exact=H@direction.flatten();errors=[]
    for eps in [.001,.0005,.00025]:
     grads=[]
     for sign in [1,-1]:
      var=(u+sign*eps*direction if sector=='real' else sign*eps*direction).detach().requires_grad_(True)
      E=energy(var,torch.zeros_like(u),method) if sector=='real' else energy(u,var,method)
      grads.append(torch.autograd.grad(E,var)[0].flatten())
     errors.append(float(((grads[0]-grads[1])/(2*eps)-exact).norm()/exact.norm()))
    fd[sector]=errors
   qa['finite_difference_relative_errors']=fd;assert max(v[-1] for v in fd.values())<1e-5,qa
  qa['raw_hessian_asymmetry_max']=float((Hr-Hr.T).abs().max());assert qa['raw_hessian_asymmetry_max']<1e-8
  for sector,H in [('real',Hr),('imag',Hm)]:
   H=(H+H.T)/2;vals,vecs=torch.linalg.eigh(H);lam=vals[:8];v=vecs[:,:8];res=float((H@v-v*lam).norm(dim=0).max());orth=float((v.T@v-torch.eye(8,device=dev,dtype=dt)).abs().max());assert res<1e-7 and orth<1e-10
   overlap=((v.T@u.flatten())**2/u.square().sum()).tolist() if sector=='imag' else [0.]*8
   rec=dict(stage=stage,method=method,sector=sector,eigenvalues=lam.tolist(),phase_overlap_squared=overlap,eigen_residual_max=res,orthogonality_max=orth,negative_count=int((vals< -1e-6).sum()))
   rows.append(rec)
   if method=='full':refs[sector]=(H.detach().clone(),lam.detach().clone(),v.detach().clone())
   else:
    refH,refvals,refvec=refs[sector];start=1 if sector=='imag' else 0
    comparisons.append(dict(stage=stage,method=method,sector=sector,relative_eigenvalue_errors=((lam[start:]-refvals[start:]).abs()/refvals[start:].abs()).tolist(),eigenvector_overlap_squared=((refvec[:,start:]*v[:,start:]).sum(0)**2).tolist(),operator_relative_frobenius=float((H-refH).norm()/refH.norm())))
  checks.append(qa);save('QA.json',checks);save('RESULT.json',rows);save('COMPARISONS.json',comparisons)
  print(json.dumps(dict(stage=stage,method=method,elapsed_s=time.perf_counter()-begin)),flush=True)
save('STATUS.json',dict(complete=True,matrices=len(rows),elapsed_s=time.perf_counter()-begin,gpu_peak_allocated_bytes=torch.cuda.max_memory_allocated()))
