import json,math,hashlib,time,socket,os
from pathlib import Path
import torch
P=Path(__file__).resolve().parent
inp=P/'B13-PROFILES.json'
expected='1aa779f171b0ab3c3eb1b844d98934b18cb6dc129b398fff10ea7e33ce801a7d'
raw=inp.read_bytes(); assert hashlib.sha256(raw).hexdigest()==expected
assert torch.cuda.is_available(); torch.set_num_threads(1)
dev='cuda';dtype=torch.float64
a=125**2/(2*246**2*.01);y0=math.sqrt(.01)*246/50;M2=6.25
out=P/'results-second-order';out.mkdir(exist_ok=False)
def save(name,d):
 t=out/(name+'.tmp');t.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');t.replace(out/name)
def inv(q,h):
 N=q.numel()+1
 odd=torch.cat((q.new_zeros(1),q,q.new_zeros(1),-q.flip(0)))
 k=torch.arange(2*N,device=dev,dtype=dtype)
 eig=4/h**2*torch.sin(math.pi*k/(2*N))**2+M2
 return torch.fft.ifft(torch.fft.fft(odd)/eig).real[1:N]
def lap(z,h):
 full=torch.nn.functional.pad(z,(1,1));return (full[2:]-2*z+full[:-2])/h**2
def energy(z,r,h,S,b):
 y=y0+z/r;D=y*y-y0*y0
 return 4*math.pi*h*(.5*torch.nn.functional.pad(z,(1,1)).diff().square().sum()/h**2+(r*r*(a/4*D**2+b/2*D*S)).sum())
def residual(z,r,h,S,b):
 y=y0+z/r
 return -lap(z,h)+r*(a*y*(y*y-y0*y0)+b*y*S)
begin=time.perf_counter()
prov=dict(host=socket.gethostname(),gpu=torch.cuda.get_device_name(0),cuda_visible_devices=os.getenv('CUDA_VISIBLE_DEVICES'),torch=torch.__version__,compute='CUDA float64 operators, norms, energy and autograd; CPU control, JSON and scalar grouping',input_sha256=expected,source_hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['followup.py','PLAN.md','FOLLOWUP-PLAN.md']})
save('PROVENANCE.json',prov)
# Independent small dense operator and analytic eigenmode.
n=31;h=.08;r=torch.arange(1,n+1,device=dev,dtype=dtype)*h
q=torch.sin(r)+.23*torch.cos(3*r)
A=torch.diag(torch.full((n,),2/h**2+M2,device=dev,dtype=dtype))+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dtype),1)+torch.diag(torch.full((n-1,),-1/h**2,device=dev,dtype=dtype),-1)
dense=torch.linalg.solve(A,q);fft=inv(q,h)
e1=float(torch.linalg.vector_norm(fft-dense)/torch.linalg.vector_norm(dense))
sine=torch.sin(math.pi*torch.arange(1,n+1,device=dev,dtype=dtype)/(n+1));ev=4/h**2*math.sin(math.pi/(2*(n+1)))**2+M2
e2=float(torch.linalg.vector_norm(inv(sine,h)-sine/ev)/torch.linalg.vector_norm(sine/ev))
S=.7*torch.exp(-r*r);b=.1;z=(-.02*r*torch.exp(-r*r)).requires_grad_(True)
g=torch.autograd.grad(energy(z,r,h,S,b),z)[0];ex=4*math.pi*h*residual(z,r,h,S,b)
e3=float(torch.linalg.vector_norm(g-ex)/torch.linalg.vector_norm(ex))
zero=inv(torch.zeros_like(r),h);e4=float(zero.abs().max());e5=abs(float(energy(zero,r,h,S,0)))
qa=dict(fft_dense_relative=e1,fft_sine_relative=e2,energy_gradient_relative=e3,zero_response_max=e4,zero_energy_abs=e5)
qa['passed']=max(e1,e2,e3)<1e-10 and max(e4,e5)<1e-12
save('QA.json',qa);assert qa['passed'],qa
rows=[]
for row in json.loads(raw):
 assert row['passed']
 r=torch.tensor(row['r'],device=dev,dtype=dtype);h=row['h'];b=row['portal_g']/.01
 F=torch.tensor(row['F'],device=dev,dtype=dtype);S=(F*F).sum(0)
 ref=r*torch.tensor(row['higgs_deviation'],device=dev,dtype=dtype)
 J=b*y0*r*S;En=energy(ref,r,h,S,b);den=torch.linalg.vector_norm(ref)
 assert float(En)<0 and float(den)>0 and float(J.norm())>0 and bool((y0+ref/r>0).all())
 approx={'N':-inv(J,h),'L':-J/M2,'P':r*(torch.sqrt(torch.clamp(y0*y0-b/a*S,min=0))-y0)}
 z1=approx['N']
 approx['N2']=z1-inv(b*S*z1+3*a*y0*z1*z1/r,h)
 rec={k:row[k] for k in ['stage','R','h','eta','portal_g','c8']}
 rec.update(reference_higgs_energy=float(En),reference_residual_relative=float(residual(ref,r,h,S,b).norm()/J.norm()),max_abs_chi_over_y0=float((ref/r/y0).abs().max()),max_bS_over_M2=float((b*S/M2).max()),reference_min_relative=float((ref/r/y0).min()),methods={})
 for name,z in approx.items():
  E=energy(z,r,h,S,b)
  rec['methods'][name]=dict(profile_relative_L2=float((z-ref).norm()/den),higgs_energy_relative_error=float((E-En).abs()/En.abs()),higgs_energy=float(E),full_residual_relative=float(residual(z,r,h,S,b).norm()/J.norm()),core_depression_relative_error=float(((z/r).min()-(ref/r).min()).abs()/(ref/r).min().abs()))
 if row['stage']=='grid':
  rec['profile']={'r':r.tolist(),'reference_chi_over_y0':(ref/r/y0).tolist(),**{name:(z/r/y0).tolist() for name,z in approx.items()}}
 rows.append(rec)
groups=[]
for eta in [.05,.1]:
 for portal in [.001,.005]:
  for c8 in [0,1]:
   stages={x['stage']:x for x in rows if (x['eta'],x['portal_g'],x['c8'])==(eta,portal,c8)}
   assert set(stages)=={'base','grid','box'}
   for method in ['N','L','P','N2']:
    vals={s:{k:stages[s]['methods'][method][k] for k in ['profile_relative_L2','higgs_energy_relative_error']} for s in stages}
    drift=max(abs(vals[s][k]-vals['base'][k]) for s in ['grid','box'] for k in vals[s])
    largest=max(v for d in vals.values() for v in d.values());smallest_worst=min(max(d.values()) for d in vals.values())
    verdict='brauchbar' if largest+drift<=.05 and drift<=.005 else ('unzureichend' if smallest_worst-drift>.05 and drift<=.005 else 'unentschieden')
    groups.append(dict(eta=eta,portal_g=portal,c8=c8,method=method,verdict=verdict,observed_grid_box_indicator=drift,worst_error=largest,fine_errors=vals['grid']))
old=json.loads((P/'results/RESULT.json').read_text())
max_reproduction_error=max(abs(new['methods'][m][k]-prev['methods'][m][k]) for new,prev in zip(rows,old['rows']) for m in ['N','L','P'] for k in prev['methods'][m])
assert max_reproduction_error<1e-12,max_reproduction_error
save('REPRODUCTION.json',dict(max_absolute_difference=max_reproduction_error,passed=True))
torch.cuda.synchronize()
save('RESULT.json',dict(rows=rows,groups=groups,elapsed_s=time.perf_counter()-begin,gpu_peak_allocated_bytes=torch.cuda.max_memory_allocated(),scope='fixed-profile stationary radial 3D approximation audit; no reoptimization, no new evolution'))
print(json.dumps(dict(qa=qa,rows=len(rows),groups=groups,elapsed_s=time.perf_counter()-begin),indent=2))
