import torch,json,math,hashlib,time
from pathlib import Path
P=Path(__file__).resolve().parent
inp=P.parent/'higgs-minima-20261008/results/RESULT.json'
raw=inp.read_bytes();assert hashlib.sha256(raw).hexdigest()=='a4a5fd942db57ab7a6b351840d0e64877eb29f7136450385d0c66cada4b601d9'
assert torch.cuda.is_available();torch.set_num_threads(1);torch.backends.cuda.preferred_linalg_library('cusolver')
dev='cuda';dt=torch.float64;pi=math.pi;a=125**2/(2*246**2*.01);y0=.492;b=.5;eta=.05;Q=600.
out=P/'results';out.mkdir(exist_ok=False)
def save(n,v):
 t=out/(n+'.tmp');t.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n');t.replace(out/n)
def T(v):return torch.tensor(v,device=dev,dtype=dt)
save('PROVENANCE.json',dict(gpu=torch.cuda.get_device_name(),torch=torch.__version__,compute='CUDA float64 analytic Hessians, autograd HVP, cuSOLVER eigensystems; CPU IO and control',input_sha256=hashlib.sha256(raw).hexdigest(),hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['PLAN.md','run.py']}))
rows=[];qas=[];begin=time.perf_counter()
for old in json.loads(raw):
 if old['method']!='full' or old['seed']!=0:continue
 r=T(old['r']);u=T(old['u']);z=T(old['z']);h=old['h'];n=len(r);omega=old['omega'];rho=(u/r)**2;S=rho.sum(0);y=y0+z/r;D=y*y-y0*y0
 lap=torch.diag(torch.full((n,),2/h**2,device=dev,dtype=dt))+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dt),1)+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dt),-1)
 W=1-2*rho+1.5*rho*rho-.5*rho.flip(0)+b/2*D-omega**2
 Hm=torch.zeros((2*n,2*n),device=dev,dtype=dt);Hr=torch.zeros((3*n,3*n),device=dev,dtype=dt)
 for i in range(2):
  sl=slice(i*n,(i+1)*n);Hm[sl,sl]=lap+torch.diag(W[i]);Hr[sl,sl]=lap+torch.diag(W[i]-4*rho[i]+6*rho[i]**2)
 Hm[:n,n:]=Hm[n:,:n]=torch.diag(torch.full((n,),-eta,device=dev,dtype=dt))
 Hr[:n,n:2*n]=Hr[n:2*n,:n]=torch.diag(-eta-u[0]*u[1]/r**2)
 Hr[2*n:,2*n:]=lap+torch.diag(a*(3*y*y-y0*y0)+b*S)
 for i in range(2):
  sl=slice(i*n,(i+1)*n);cross=torch.diag(math.sqrt(2)*b*y*u[i]/r);Hr[sl,2*n:]=cross;Hr[2*n:,sl]=cross
 U=torch.cat((u.flatten(),torch.zeros_like(z)));rank=4*omega**2*torch.outer(U,U)/u.square().sum()
 w0=torch.cat((u,z[None]/math.sqrt(2),torch.zeros_like(u)),dim=0)
 def energy(w,l):
  ur=w[:2];zz=w[2]*math.sqrt(2);vi=w[3:];rh=(ur*ur+vi*vi)/r**2;ss=rh.sum(0);yy=y0+zz/r;dd=yy*yy-y0*y0
  I=4*pi*h*(ur*ur+vi*vi).sum();A=Q**2/(4*I) if l==0 else -omega**2*I
  kin=4*pi/h*(torch.nn.functional.pad(ur,(1,1)).diff(dim=-1).square().sum()+torch.nn.functional.pad(vi,(1,1)).diff(dim=-1).square().sum()+.5*torch.nn.functional.pad(zz,(1,1)).diff().square().sum())
  pot=(rh-rh*rh+.5*rh**3).sum(0)-.5*rh[0]*rh[1]-2*eta*(ur[0]*ur[1]+vi[0]*vi[1])/r**2+a/4*dd*dd+b/2*dd*ss
  return (A+kin+4*pi*h*(r*r*pot).sum())/(8*pi*h)+.5*((w-w0)**2*l*(l+1)/r**2).sum()
 derivative=lambda v:(torch.nn.functional.pad(v,(1,1))[...,2:]-torch.nn.functional.pad(v,(1,1))[...,:-2])/(2*h)-v/r
 translation=torch.cat((derivative(u).flatten(),derivative(z)/math.sqrt(2)));phase=u.flatten()
 for ell in range(4):
  angular=ell*(ell+1)/r**2;real=Hr+torch.diag(angular.repeat(3))+(rank if ell==0 else 0);imag=Hm+torch.diag(angular.repeat(2))
  probe=torch.stack([r*torch.exp(-r*r/16)*torch.sin((i+1)*.7*r+.2*i) for i in range(5)]);probe=probe/probe.norm()
  hv=torch.autograd.functional.hvp(lambda w:energy(w,ell),w0,probe)[1]
  expected=torch.cat(((real@probe[:3].flatten()).reshape(3,n),(imag@probe[3:].flatten()).reshape(2,n)))
  hv_err=float((hv-expected).norm()/expected.norm());assert hv_err<1e-9,('HVP',old['stage'],ell,hv_err)
  for sector,H in [('real',real),('imag',imag)]:
   vals,vecs=torch.linalg.eigh(H);v=vecs[:,:8];lam=vals[:8];res=float((H@v-v*lam).norm(dim=0).max());orth=float((v.T@v-torch.eye(8,device=dev,dtype=dt)).abs().max())
   qa=dict(stage=old['stage'],ell=ell,sector=sector,hvp_relative_error=hv_err,eigen_residual_max=res,orthogonality_max=orth)
   qas.append(qa);save('QA.json',qas);assert res<1e-7 and orth<1e-10,qa
   sym=translation if sector=='real' and ell==1 else (phase if sector=='imag' and ell==0 else None)
   overlaps=((v.T@sym)**2/sym.square().sum()).tolist() if sym is not None else [0.]*8
   vfields=v.reshape(3 if sector=='real' else 2,n,8);anti=((vfields[0]-vfields[1])**2).sum(0)/2
   rec=dict(stage=old['stage'],h=h,R=old['R'],ell=ell,sector=sector,eigenvalues=lam.tolist(),minimum_all=float(vals[0]),negative_count=int((vals < -1e-6).sum()),symmetry_overlap_squared=overlaps,antisymmetric_matter_weight=anti.tolist(),higgs_weight=(vfields[2].square().sum(0)).tolist() if sector=='real' else [0.]*8)
   if sector=='imag' and ell==0:
    ward=float((H@phase).norm()/phase.norm());rec['phase_ward_residual']=ward;assert ward<1e-6
   if sym is not None:rec['symmetry_rayleigh']=float(sym@(H@sym)/(sym@sym))
   rows.append(rec);save('RESULT.json',rows)
   print(json.dumps(dict(stage=old['stage'],ell=ell,sector=sector,eigenvalues=lam[:3].tolist(),overlaps=overlaps[:3],elapsed_s=time.perf_counter()-begin)),flush=True)
   del vals,vecs,v,H
save('STATUS.json',dict(complete=True,matrices=len(rows),elapsed_s=time.perf_counter()-begin,gpu_peak_allocated_bytes=torch.cuda.max_memory_allocated()))
