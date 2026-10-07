import torch,json,math,time,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
inp=P.parent/'higgs-response-20261008/B13-PROFILES.json'
raw=inp.read_bytes();assert hashlib.sha256(raw).hexdigest()=='1aa779f171b0ab3c3eb1b844d98934b18cb6dc129b398fff10ea7e33ce801a7d'
assert torch.cuda.is_available();torch.set_num_threads(1)
out=P/'results';out.mkdir(exist_ok=False)
def save(n,v):
 t=out/(n+'.tmp');t.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n');t.replace(out/n)
a=125**2/(2*246**2*.01);y0=.492;b=.5;eta=.05;Q=600.;pi=math.pi
rows=[];checks=[];begin=time.perf_counter()
save('PROVENANCE.json',dict(gpu=torch.cuda.get_device_name(),torch=torch.__version__,input_sha256=hashlib.sha256(raw).hexdigest(),hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['PLAN.md','run.py']},compute='CUDA float64 relaxation; CPU control, IO and scalar summaries'))
for old in json.loads(raw):
 if (old['eta'],old['portal_g'],old['c8'])!=(eta,.005,0):continue
 h=old['h'];R=old['R'];r=torch.tensor(old['r'],device='cuda',dtype=torch.float64);N=len(r)+1
 eig=4/h**2*torch.sin(pi*torch.arange(2*N,device='cuda',dtype=torch.float64)/(2*N))**2
 def inv(q,mass):
  odd=torch.cat((torch.zeros_like(q[...,:1]),q,torch.zeros_like(q[...,:1]),-q.flip(-1)),dim=-1)
  return torch.fft.ifft(torch.fft.fft(odd)/(eig+mass)).real[...,1:N]
 def resp(u):
  S=(u/r).square().sum(-2);z1=-inv(b*y0*r*S,6.25);z2=-inv(b*S*z1+3*a*y0*z1*z1/r,6.25)
  return S,z1,z2
 def calc(x,method):
  u=x[:,:2];rho=(u/r).square();S=rho.sum(-2);I=4*pi*h*u.square().sum((-1,-2));omega=Q/(2*I)
  kin=4*pi/h*torch.nn.functional.pad(u,(1,1)).diff(dim=-1).square().sum((-1,-2))
  pot=(rho-rho.square()+.5*rho**3).sum(-2)-.5*rho[:,0]*rho[:,1]-2*eta*u[:,0]*u[:,1]/r**2
  E=Q**2/(4*I)+kin+4*pi*h*(r*r*pot).sum(-1)
  if method=='full':z=x[:,2]
  else:S,z1,z2=resp(u);z=z1+z2
  if method=='E3':EH=4*pi*h*(.5*b*y0*r*S*z1+b/2*S*z1*z1+a*y0*z1**3/r).sum(-1)
  else:
   D=(y0+z/r)**2-y0*y0
   EH=4*pi*h*(.5*torch.nn.functional.pad(z,(1,1)).diff(dim=-1).square().sum(-1)/h**2+(r*r*(a/4*D*D+b/2*D*S)).sum(-1))
  return E+EH,omega,z
 u0=r*torch.tensor(old['F'],device='cuda',dtype=torch.float64);z0=r*torch.tensor(old['higgs_deviation'],device='cuda',dtype=torch.float64)
 full0=torch.cat((u0,z0[None]))[None];energy0=calc(full0,'full')[0][0]
 err=abs(float(energy0)/old['energy']-1);assert err<1e-10
 # Independent original analytic B13 gradient at a perturbed configuration.
 probe=(full0*(1+.03*torch.exp(-r*r/9))).requires_grad_(True)
 E,om,z=calc(probe,'full');u=probe[:,:2];rho=(u/r).square();S=rho.sum(-2);y=y0+z/r;D=y*y-y0*y0
 pad=torch.nn.functional.pad(probe,(1,1));lap=-(pad[...,2:]-2*probe+pad[...,:-2])/h**2
 gu=lap[:,:2]+(1-2*rho+1.5*rho**2-.5*rho.flip(1)-om[:,None,None]**2+b/2*D[:,None])*u-eta*u.flip(1)
 gz=lap[:,2]+r*(a*y*D+b*y*S);metric=torch.tensor([1.,1.,.5],device='cuda')[None,:,None]
 expected=8*pi*h*metric*torch.cat((gu,gz[:,None]),1);actual=torch.autograd.grad(E.sum(),probe)[0]
 ge=float((actual-expected).norm()/expected.norm());assert ge<1e-9
 checks.append(dict(stage=old['stage'],archive_energy_relative_error=err,analytic_gradient_error=ge));save('QA.json',checks)
 for method in ['full','E3','Ecomp']:
  start=full0[0] if method=='full' else u0
  x=torch.stack((start,start*(1+.03*torch.exp(-r*r/9)))).detach()
  metric=torch.ones((1,x.shape[1],1),device='cuda',dtype=torch.float64)
  mass=torch.ones_like(metric)
  if method=='full':metric[:,2]=.5;mass[:,2]=6.25
  accepted_steps=torch.zeros(2,device='cuda',dtype=torch.int64);reason='iteration_limit'
  for it in range(600):
   x=x.detach().requires_grad_(True);E,omega,z=calc(x,method);g=torch.autograd.grad(E.sum(),x)[0]/(8*pi*h*metric)
   res=torch.sqrt(4*pi*h*(metric*g*g).sum((-1,-2))/Q)
   if bool((res<1e-7).all()):reason='target_residual';break
   with torch.no_grad():
    direction=-inv(g,mass);chosen=x.detach().clone();accepted=torch.zeros(2,device='cuda',dtype=torch.bool)
    for bt in range(12):
     trial=x+(4*.5**bt)*direction;Et=calc(trial,method)[0];good=(~accepted)&torch.isfinite(Et)&(Et<E)
     chosen[good]=trial[good];accepted|=good
     if bool(accepted.all()):break
    accepted_steps+=accepted;x=chosen
    if not bool(accepted.any()):reason='no_descent';break
  x=x.detach().requires_grad_(True);E,omega,z=calc(x,method);g=torch.autograd.grad(E.sum(),x)[0]/(8*pi*h*metric);res=torch.sqrt(4*pi*h*(metric*g*g).sum((-1,-2))/Q)
  for j in range(2):
   u=x[j,:2].detach();tail=float(u[:,r>.8*R].square().sum()/u.square().sum())
   rows.append(dict(stage=old['stage'],R=R,h=h,method=method,seed=j,energy=float(E[j]),omega=float(omega[j]),residual=float(res[j]),tail=tail,bound=float(E[j])/Q<math.sqrt(1-eta) and float(omega[j])<math.sqrt(1-eta),iterations=it+1,accepted_steps=int(accepted_steps[j]),stop=reason,r=r.tolist(),u=u.tolist(),z=z[j].detach().tolist()))
  save('RESULT.json',rows);print(json.dumps(dict(stage=old['stage'],method=method,residual=res.tolist(),iterations=it+1,elapsed_s=time.perf_counter()-begin)),flush=True)
save('STATUS.json',dict(complete=True,rows=len(rows),elapsed_s=time.perf_counter()-begin))
