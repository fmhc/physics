import torch,json,math,time,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
inp=P.parent/'higgs-minima-20261008/results/RESULT.json'
raw=inp.read_bytes();assert hashlib.sha256(raw).hexdigest()=='a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9'
assert torch.cuda.is_available();torch.set_num_threads(1);torch.backends.cuda.preferred_linalg_library('cusolver')
dev='cuda';dt=torch.float64;pi=math.pi;a=125**2/(2*246**2*.01);y0=.492;b=.5;eta=.05;Q=600.
out=P/'results';out.mkdir(exist_ok=False)
def T(x):return torch.tensor(x,device=dev,dtype=dt)
def save(n,v):
 t=out/(n+'.tmp');t.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n');t.replace(out/n)
save('PROVENANCE.json',dict(gpu=torch.cuda.get_device_name(),torch=torch.__version__,compute='CUDA float64 angular jets, quadrature, Hessians, solves and eigenvalues; CPU IO/control',input_sha256=hashlib.sha256(raw).hexdigest(),hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['PLAN.md','run.py']}))
# Independent finite-angle integration: normalized Legendre polynomials.
k=torch.arange(1,24,device=dev,dtype=dt);off=k/torch.sqrt(4*k*k-1);jac=torch.diag(off,1)+torch.diag(off,-1);mu,V=torch.linalg.eigh(jac);weights=V[0]**2
polys=[torch.ones_like(mu),mu]
for L in range(1,8):polys.append(((2*L+1)*mu*polys[-1]-L*polys[-2])/(L+1))
Y=torch.stack([math.sqrt(2*L+1)*polys[L] for L in range(9)]);qerr=float(((Y*weights)@Y.T-torch.eye(9,device=dev,dtype=dt)).abs().max());assert qerr<1e-12
source=json.loads(raw);rows=[];checks=[];comparisons=[];begin=time.perf_counter()
for stage in ['base','grid','box']:
 old=next(x for x in source if (x['stage'],x['method'],x['seed'])==(stage,'full',0));r=T(old['r']);h=old['h'];n=len(r);N=n+1
 lap=torch.diag(torch.full((n,),2/h**2,device=dev,dtype=dt))+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dt),1)+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dt),-1)
 eig=4/h**2*torch.sin(pi*torch.arange(2*N,device=dev,dtype=dt)/(2*N))**2+6.25
 invs={};solveerr=0.
 for L in range(1,9 if stage=='base' else 3):
  K=lap+torch.diag(6.25+L*(L+1)/r**2);C=torch.linalg.cholesky(K);invK=torch.cholesky_inverse(C)
  err=float((K@invK-torch.eye(n,device=dev,dtype=dt)).norm()/math.sqrt(n));solveerr=max(solveerr,err);assert err<1e-10;invs[L]=invK
 def inv(q,L):
  if L:return invs[L]@q
  odd=torch.cat((q.new_zeros(1),q,q.new_zeros(1),-q.flip(0)))
  return torch.fft.ifft(torch.fft.fft(odd)/eig).real[1:N]
 def response(S):
  z1=-inv(b*y0*r*S,0);z2=-inv(b*S*z1+3*a*y0*z1*z1/r,0);return z1,z2
 def radial_energy(u,method):
  rho=(u/r)**2;S=rho.sum(0);I=4*pi*h*u.square().sum();z1,z2=response(S)
  kin=4*pi/h*torch.nn.functional.pad(u,(1,1)).diff(dim=-1).square().sum()
  pot=(rho-rho*rho+.5*rho**3).sum(0)-.5*rho[0]*rho[1]-2*eta*u[0]*u[1]/r**2
  if method=='E3':EH=4*pi*h*(.5*b*y0*r*S*z1+b/2*S*z1*z1+a*y0*z1**3/r).sum()
  else:
   z=z1+z2;D=(y0+z/r)**2-y0*y0;EH=4*pi*h*(.5*torch.nn.functional.pad(z,(1,1)).diff().square().sum()/h**2+(r*r*(a/4*D*D+b/2*D*S)).sum())
  return (Q**2/(4*I)+kin+4*pi*h*(r*r*pot).sum()+EH)/(8*pi*h)
 def jet(d,u,method,L,sector):
  rho=(u/r)**2;S=rho.sum(0);omega=Q/(8*pi*h*u.square().sum());s2=(d/r).square().sum(0)
  rho1=2*u*d/r**2 if sector=='real' else torch.zeros_like(u);s1=rho1.sum(0);rho2=(d/r)**2
  z10,z20=response(S);z11=-inv(b*y0*r*s1,L);z12=-inv(b*y0*r*s2,0)
  z21=-inv(b*(S*z11+s1*z10)+6*a*y0*z10*z11/r,L)
  z22=-inv(b*(S*z12+s1*z11+s2*z10)+3*a*y0*(2*z10*z12+z11*z11)/r,0)
  kin=4*pi/h*torch.nn.functional.pad(d,(1,1)).diff(dim=-1).square().sum()+4*pi*h*(L*(L+1)*d.square()/r**2).sum()
  vp=((1-2*rho+1.5*rho*rho)*rho2+(-1+1.5*rho)*rho1.square()).sum(0)-.5*(rho[0]*rho2[1]+rho[1]*rho2[0]+rho1[0]*rho1[1])-2*eta*d[0]*d[1]/r**2
  charge=-4*pi*h*omega**2*d.square().sum()
  if L==0 and sector=='real':charge=charge+4*pi*h*4*omega**2*(u*d).sum()**2/u.square().sum()
  if method=='E3':
   eh2=4*pi*h*(.5*b*y0*r*(S*z12+s1*z11+s2*z10)+b/2*(S*(2*z10*z12+z11*z11)+2*s1*z10*z11+s2*z10*z10)+a*y0*(3*z10*z10*z12+3*z10*z11*z11)/r).sum()
  else:
   z0=z10+z20;z1=z11+z21;z2=z12+z22;yy=y0+z0/r;d0=yy*yy-y0*y0;d1=2*yy*z1/r;d2=(z1/r)**2+2*yy*z2/r
   diff=lambda x:torch.nn.functional.pad(x,(1,1)).diff()
   eh2=4*pi*h*(.5*(2*diff(z0)*diff(z2)+diff(z1)**2).sum()/h**2+.5*(L*(L+1)*z1*z1/r**2).sum()+(r*r*(a/4*(d1*d1+2*d0*d2)+b/2*(d0*s2+d1*s1+d2*S))).sum())
  return (charge+kin+4*pi*h*(r*r*vp).sum()+eh2)/(8*pi*h)
 def angle_energy(eps,d,u,method,L,sector):
  ur=u[:,:,None]+(eps*d[:,:,None]*Y[L] if sector=='real' else 0);vi=eps*d[:,:,None]*Y[L] if sector=='imag' else torch.zeros((2,n,24),device=dev,dtype=dt)
  rho=(ur*ur+vi*vi)/r[None,:,None]**2;S=rho.sum(0);Sl=(S*weights)@Y.T
  z1c=torch.stack([-inv(b*y0*r*Sl[:,j],j) for j in range(9)],1);z1=z1c@Y
  src=b*S*z1+3*a*y0*z1*z1/r[:,None];srcL=(src*weights)@Y.T
  z2c=torch.stack([-inv(srcL[:,j],j) for j in range(9)],1)
  I=4*pi*h*((rho.sum(0)*weights)*r[:,None]**2).sum()
  # Angular means remove the linear background-perturbation kinetic cross term.
  kin=4*pi/h*(torch.nn.functional.pad(u,(1,1)).diff(dim=-1).square().sum()+eps**2*torch.nn.functional.pad(d,(1,1)).diff(dim=-1).square().sum())+4*pi*h*eps**2*(L*(L+1)*d.square()/r**2).sum()
  pot=(rho-rho*rho+.5*rho**3).sum(0)-.5*rho[0]*rho[1]-2*eta*(ur[0]*ur[1]+vi[0]*vi[1])/r[:,None]**2
  if method=='E3':EH=4*pi*h*((.5*b*y0*r[:,None]*S*z1+b/2*S*z1*z1+a*y0*z1**3/r[:,None])*weights).sum()
  else:
   zc=z1c+z2c;z=zc@Y;D=(y0+z/r[:,None])**2-y0*y0;ang=T([j*(j+1) for j in range(9)])
   grad=.5*torch.nn.functional.pad(zc.T,(1,1)).diff(dim=-1).square().sum()/h**2+.5*(zc.square()*ang/r[:,None]**2).sum()
   EH=4*pi*h*(grad+((r[:,None]**2*(a/4*D*D+b/2*D*S))*weights).sum())
  return (Q**2/(4*I)+kin+4*pi*h*((r[:,None]**2*pot)*weights).sum()+EH)/(8*pi*h)
 def dense_hessian(fun):
  x=torch.zeros(2*n,device=dev,dtype=dt,requires_grad=True);g=torch.autograd.grad(fun(x),x,create_graph=True)[0];H=torch.empty((2*n,2*n),device=dev,dtype=dt)
  for j in range(0,2*n,32):
   count=min(32,2*n-j);B=torch.zeros((count,2*n),device=dev,dtype=dt);B[torch.arange(count,device=dev),torch.arange(j,j+count,device=dev)]=1
   H[j:j+count]=torch.autograd.grad(g,x,grad_outputs=B,is_grads_batched=True,retain_graph=True)[0].detach()
  return H
 refs={}
 for method in ['full','E3','Ecomp']:
  old=next(x for x in source if (x['stage'],x['method'],x['seed'])==(stage,method,0));u=T(old['u']);omega=Q/(8*pi*h*u.square().sum());rho=(u/r)**2;S=rho.sum(0);qa=dict(stage=stage,method=method,quadrature_error=qerr,inverse_solve_error=solveerr)
  d=torch.stack([r*torch.exp(-r*r/16)*torch.sin((i+1)*.7*r+.2*i) for i in range(2)]);d*=u.norm()/d.norm()
  if method!='full':
   exact=torch.autograd.functional.hvp(lambda v:radial_energy(v,method),u,d)[1]
   got=torch.autograd.functional.hvp(lambda v:jet(v,u,method,0,'real'),torch.zeros_like(u),d)[1]
   qe=float((got-exact).norm()/exact.norm());qa['radial_jet_hvp_error']=qe;assert qe<1e-9,qa
  for L in [1,2]:
   for sector in ['real','imag']:
    if method=='full':
     z=T(old['z']);y=y0+z/r;D=y*y-y0*y0;W=1-2*rho+1.5*rho*rho-.5*rho.flip(0)+b/2*D-omega**2;ang=L*(L+1)/r**2
     H=torch.zeros((2*n,2*n),device=dev,dtype=dt)
     for i in range(2):H[i*n:(i+1)*n,i*n:(i+1)*n]=lap+torch.diag(W[i]+ang+(-4*rho[i]+6*rho[i]**2 if sector=='real' else 0))
     cross=torch.diag(-eta-u[0]*u[1]/r**2 if sector=='real' else torch.full_like(r,-eta));H[:n,n:]=H[n:,:n]=cross
     if sector=='real':
      C=lap+torch.diag(a*(3*y*y-y0*y0)+b*S+ang);B=torch.cat([torch.diag(math.sqrt(2)*b*y*u[i]/r) for i in range(2)]);chol=torch.linalg.cholesky(C);sol=torch.cholesky_solve(B.T,chol);err=float((C@sol-B.T).norm()/B.norm());assert err<1e-10;qa['schur_residual_l'+str(L)]=err;H=H-B@sol
    else:
     H=dense_hessian(lambda v:jet(v.reshape(2,n),u,method,L,sector))
     if stage=='base':
      expected=float(2*jet(d,u,method,L,sector));assert abs(expected)>1e-10;errs=[];E0=angle_energy(0.,d,u,method,L,sector)
      for eps in [.003,.0015,.00075]:
       approx=(angle_energy(eps,d,u,method,L,sector)+angle_energy(-eps,d,u,method,L,sector)-2*E0)/eps**2
       errs.append(abs(float(approx)/expected-1))
      qa[f'angular_fd_{L}_{sector}']=errs;save('QA-IN-PROGRESS.json',qa);assert errs[-1]<1e-4,qa
    asym=float((H-H.T).abs().max());assert asym<1e-8;H=(H+H.T)/2;vals,vecs=torch.linalg.eigh(H);lam=vals[:8];v=vecs[:,:8];res=float((H@v-v*lam).norm(dim=0).max());orth=float((v.T@v-torch.eye(8,device=dev,dtype=dt)).abs().max());assert res<1e-7 and orth<1e-10
    du=(torch.nn.functional.pad(u,(1,1))[:,2:]-torch.nn.functional.pad(u,(1,1))[:,:-2])/(2*h)-u/r
    overlap=((v.T@du.flatten())**2/du.square().sum()).tolist() if L==1 and sector=='real' else [0.]*8
    rows.append(dict(stage=stage,method=method,ell=L,sector=sector,eigenvalues=lam.tolist(),translation_overlap_squared=overlap,eigen_residual=res,orthogonality=orth,raw_asymmetry=asym,negative_count=int((vals< -1e-6).sum())))
    if method=='full':refs[L,sector]=(lam.detach().clone(),v.detach().clone())
    else:
     refvals,refvec=refs[L,sector];start=1 if L==1 and sector=='real' else 0
     comparisons.append(dict(stage=stage,method=method,ell=L,sector=sector,relative_errors=((lam[start:]-refvals[start:]).abs()/refvals[start:].abs()).tolist(),overlap_squared=((v[:,start:]*refvec[:,start:]).sum(0)**2).tolist()))
    save('RESULT.json',rows);save('COMPARISONS.json',comparisons)
   print(json.dumps(dict(stage=stage,method=method,ell=L,elapsed_s=time.perf_counter()-begin)),flush=True)
  checks.append(qa);save('QA.json',checks)
save('STATUS.json',dict(complete=True,matrices=len(rows),elapsed_s=time.perf_counter()-begin,gpu_peak_allocated_bytes=torch.cuda.max_memory_allocated()))
