import torch,json,math,hashlib,socket,time,os
from pathlib import Path
P=Path(__file__).resolve().parent
inp=P.parent/'higgs-response-20261008/B13-PROFILES.json'
raw=inp.read_bytes();assert hashlib.sha256(raw).hexdigest()=='1aa779f171b0ab3c3eb1b844d98934b18cb6dc129b398fff10ea7e33ce801a7d'
assert torch.cuda.is_available();torch.set_num_threads(1);dev='cuda';dt=torch.float64
out=P/'results';out.mkdir(exist_ok=False)
def save(n,x):
 t=out/(n+'.tmp');t.write_text(json.dumps(x,indent=2,allow_nan=False)+'\n');t.replace(out/n)
a=125**2/(2*246**2*.01);y0=math.sqrt(.01)*246/50;M2=6.25
save('PROVENANCE.json',dict(host=socket.gethostname(),gpu=torch.cuda.get_device_name(0),torch=torch.__version__,compute='CUDA float64 FFT, energies, derivatives, norms and finite differences; CPU IO/control/scalar grouping',input_sha256=hashlib.sha256(raw).hexdigest(),source_hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['run.py','PLAN.md']}))
def inv(q,h):
 N=q.numel()+1;k=torch.arange(2*N,device=dev,dtype=dt)
 odd=torch.cat((q.new_zeros(1),q,q.new_zeros(1),-q.flip(0)))
 eig=4/h**2*torch.sin(math.pi*k/(2*N))**2+M2
 return torch.fft.ifft(torch.fft.fft(odd)/eig).real[1:N]
def response(S,r,h,b):
 z1=-inv(b*y0*r*S,h)
 z2=-inv(b*S*z1+3*a*y0*z1*z1/r,h)
 return z1,z2
# Energy terms use exactly B13 radial quadrature.
def eh(z,S,r,h,b):
 y=y0+z/r;D=y*y-y0*y0
 return 4*math.pi*h*(.5*torch.nn.functional.pad(z,(1,1)).diff().square().sum()/h**2+(r*r*(a/4*D*D+b/2*D*S)).sum())
def energies(S,r,h,b):
 z1,z2=response(S,r,h,b)
 e2=4*math.pi*h*.5*(b*y0*r*S*z1).sum()
 e3=e2+4*math.pi*h*(b/2*S*z1*z1+a*y0*z1**3/r).sum()
 ec=eh(z1+z2,S,r,h,b)
 return {'E2':e2,'E3':e3,'Ecomp':ec},(z1,z2)
rows=[];qas=[];begin=time.perf_counter()
for old in json.loads(raw):
 r=torch.tensor(old['r'],device=dev,dtype=dt);h=old['h'];b=old['portal_g']/.01
 F=torch.tensor(old['F'],device=dev,dtype=dt);u=r*F
 S=(F*F).sum(0).requires_grad_(True);w=4*math.pi*h*r*r
 refchi=torch.tensor(old['higgs_deviation'],device=dev,dtype=dt);Cref=b/2*((y0+refchi)**2-y0*y0)
 Eref=eh(r*refchi,S,r,h,b).detach();fnorm=(u*Cref).norm();assert float(fnorm)>0 and float(Eref)<0
 E,(z1,z2)=energies(S,r,h,b);chi1=z1/r;chi2=z2/r
 Cs={k:torch.autograd.grad(e,S,create_graph=True,retain_graph=True)[0]/w for k,e in E.items()}
 analytic=b*y0*(chi1+chi2)+b/2*chi1**2
 plug=b*y0*(chi1+chi2)+b/2*(chi1+chi2)**2
 cgerr=float(((Cs['E3']-analytic)*u).norm()/(Cs['E3']*u).norm())
 direction=(S.detach()*(torch.sin(.7*r)+.3*torch.cos(1.1*r)))
 fd={}
 for method in ['E3','Ecomp']:
  exact=(w*Cs[method]*direction).sum().detach();assert abs(float(exact))>1e-14
  diffs=[]
  for eps in [.01,.005,.0025]:
   ep=energies(S.detach()+eps*direction,r,h,b)[0][method]
   em=energies(S.detach()-eps*direction,r,h,b)[0][method]
   approx=(ep-em)/(2*eps);diffs.append(float((approx-exact).abs()/exact.abs()))
  fd[method]=diffs
 dirs=[S.detach()*torch.exp(-r*r/4),S.detach()*r*r/(1+r*r)]
 curl={}
 for method,C in {**{k:Cs[k] for k in ['E3','Ecomp']},'Cplug':plug}.items():
  aa=torch.autograd.grad((w*C*dirs[0]).sum(),S,retain_graph=True)[0]
  bb=torch.autograd.grad((w*C*dirs[1]).sum(),S,retain_graph=True)[0]
  ab=(aa*dirs[1]).sum();ba=(bb*dirs[0]).sum();scale=torch.maximum(ab.abs(),ba.abs()).clamp_min(1e-30)
  curl[method]=dict(relative_defect=float((ab-ba).abs()/scale),cross_ab=float(ab),cross_ba=float(ba))
 ez,(zz1,zz2)=energies(S.detach(),r,h,0.)
 zero=max(float(zz1.abs().max()),float(zz2.abs().max()),*[abs(float(v)) for v in ez.values()])
 passed=cgerr<1e-10 and max(v[-1] for v in fd.values())<1e-6 and max(curl[k]['relative_defect'] for k in ['E3','Ecomp'])<1e-8 and zero<1e-12
 ident={k:old[k] for k in ['stage','eta','portal_g','c8','h','R']}
 qas.append(dict(**ident,analytic_C3_relative_error=cgerr,finite_difference_relative_errors=fd,cross_derivative=curl,zero_limit_max=zero,passed=passed))
 rec=dict(**ident,reference_higgs_energy=float(Eref),methods={})
 for k in E:
  rec['methods'][k]=dict(force_relative_error=float(((Cs[k]-Cref)*u).norm()/fnorm),higgs_energy_relative_error=float((E[k]-Eref).abs()/Eref.abs()),higgs_energy=float(E[k]))
 rec['Cplug_force_relative_error']=float(((plug-Cref)*u).norm()/fnorm)
 rec['omitted_chain_force_relative']=float(((plug-Cs['Ecomp'])*u).norm()/(Cs['Ecomp']*u).norm())
 rec['Cplug_cross_derivative_defect']=curl['Cplug']['relative_defect']
 if old['stage']=='grid':rec['profile']=dict(r=r.tolist(),Cref=Cref.tolist(),Cplug=plug.detach().tolist(),**{k:C.detach().tolist() for k,C in Cs.items()})
 rows.append(rec)
save('QA.json',dict(passed=all(x['passed'] for x in qas),rows=qas));assert all(x['passed'] for x in qas),'QA failed; no verdict publication'
groups=[]
for eta in [.05,.1]:
 for g in [.001,.005]:
  for c in [0,1]:
   stages={x['stage']:x for x in rows if (x['eta'],x['portal_g'],x['c8'])==(eta,g,c)}
   for m in ['E2','E3','Ecomp']:
    vals={s:{k:stages[s]['methods'][m][k] for k in ['force_relative_error','higgs_energy_relative_error']} for s in stages}
    drift=max(abs(vals[s][k]-vals['base'][k]) for s in ['grid','box'] for k in vals[s]);largest=max(v for d in vals.values() for v in d.values());smallest=min(max(d.values()) for d in vals.values())
    verdict='brauchbar' if largest+drift<=.05 and drift<=.005 else ('unzureichend' if smallest-drift>.05 and drift<=.005 else 'unentschieden')
    groups.append(dict(eta=eta,portal_g=g,c8=c,method=m,verdict=verdict,observed_grid_box_indicator=drift,fine_errors=vals['grid']))
torch.cuda.synchronize();elapsed=time.perf_counter()-begin
save('RESULT.json',dict(rows=rows,groups=groups,elapsed_s=elapsed,gpu_peak_allocated_bytes=torch.cuda.max_memory_allocated(),scope='static reduced forces on fixed archived radial 3D profiles; no evolution or relaxation'))
print(json.dumps(dict(qa_passed=True,rows=len(rows),groups=groups,elapsed_s=elapsed),indent=2))
