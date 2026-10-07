import math,cmath,json,time,socket,pathlib,hashlib,resource
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
pi=math.pi;start=time.process_time()
def run(K,kick,dt,control=''):
 g=(1,1 if control else 1.03);theta=0 if control else .7
 q=[1+0j,0j,complex(math.cos(theta/2)),-1j*math.sin(theta/2)]
 if control=='stationary':q=[complex(1/math.sqrt(2))]*4
 def f(q):
  a,b,c,d=q;v=K*(abs(a)**2-abs(b)**2-abs(c)**2+abs(d)**2)
  return [-1j*(g[0]*b+v*a),-1j*(g[0]*a-v*b),-1j*(g[1]*d-v*c),-1j*(g[1]*c+v*d)]
 def E(q):
  a,b,c,d=q;z=abs(a)**2-abs(b)**2-abs(c)**2+abs(d)**2
  return 2*g[0]*(a.conjugate()*b).real+2*g[1]*(c.conjugate()*d).real+K*z*z/2
 def obs(q):
  zs=[abs(q[i])**2-abs(q[i+1])**2 for i in [0,2]]
  ys=[2*(q[i].conjugate()*q[i+1]).imag for i in [0,2]]
  return zs,[math.atan2(-y,z) for y,z in zip(ys,zs)],[math.hypot(y,z) for y,z in zip(ys,zs)]
 windows=[dict(lo=20*pi,hi=40*pi,diffs=[],radius=1.,ticks=[[],[]]),dict(lo=60*pi,hi=100*pi,diffs=[],radius=1.,ticks=[[],[]])]
 t=0.;energy_ref=E(q);energy0=energy_ref;nerr=0.;eerr=0.;work=0.;kicked=False
 zs,ph,rs=obs(q);up=ph[:]
 while t<100*pi-1e-12:
  if not kicked and t>=40*pi-1e-12:
   c,s=math.cos(kick/2),math.sin(kick/2);a,b=q[2:];old=E(q);q[2:]=[c*a-1j*s*b,c*b-1j*s*a];work=E(q)-old;energy_ref=E(q);kicked=True
   zs,ph,rs=obs(q);up=ph[:] # restart relative phase origin after intervention; window ranges invariant
  h=min(dt,100*pi-t,40*pi-t if not kicked else 100*pi-t)
  k1=f(q);k2=f([x+h*y/2 for x,y in zip(q,k1)]);k3=f([x+h*y/2 for x,y in zip(q,k2)]);k4=f([x+h*y for x,y in zip(q,k3)])
  q=[x+h*(a+2*b+2*c+d)/6 for x,a,b,c,d in zip(q,k1,k2,k3,k4)]
  newt=t+h;nz,np,nr=obs(q)
  up=[u+math.atan2(math.sin(p-old),math.cos(p-old)) for u,p,old in zip(up,np,ph)]
  for w in windows:
   if w['lo']<=newt<=w['hi']+1e-10:
    w['diffs'].append(up[1]-up[0]);w['radius']=min(w['radius'],*nr)
    for j in range(2):
     if zs[j]<0<=nz[j]:
      crossing=t+h*(-zs[j])/(nz[j]-zs[j])
      if crossing>=w['lo']:w['ticks'][j].append(crossing)
  nerr=max(nerr,*(abs(abs(q[i])**2+abs(q[i+1])**2-1) for i in [0,2]));eerr=max(eerr,abs(E(q)-energy_ref)/max(1,abs(energy_ref)))
  t=newt;zs,ph,rs=nz,np,nr
 out=[]
 for w in windows:
  ds=w['diffs'];means=[(ts[-1]-ts[0])/(len(ts)-1) if len(ts)>=10 else None for ts in w['ticks']]
  ratio=means[1]/means[0] if all(means) else None
  out.append(dict(min_radius=w['radius'],phase_range=max(ds)-min(ds),phase_drift=ds[-1]-ds[0],concentration=abs(sum(cmath.exp(1j*d) for d in ds)/len(ds)),tick_counts=list(map(len,w['ticks'])),mean_periods=means,period_ratio=ratio,finite_lock=bool(w['radius']>=.05 and ratio is not None and abs(ratio-1)<.01 and max(ds)-min(ds)<pi)))
 assert nerr<1e-5 and eerr<1e-5,(K,kick,dt,nerr,eerr)
 return dict(K=K,kick=kick,dt=dt,control=control,norm_error=nerr,energy_error=eerr,kick_work=work,energy_initial=energy0,windows=out)
cases=[(K,k,'') for K in [0,.2,1] for k in [0,.2]]+[(1,0,'identical'),(1,0,'stationary')]
rows=[run(K,k,dt,c) for K,k,c in cases for dt in [.01,.005]]
for a,b in zip(rows[::2],rows[1::2]):
 for x,y in zip(a['windows'],b['windows']):
  if min(x['min_radius'],y['min_radius'])>=.05:
   assert abs(x['phase_range']-y['phase_range'])<.05
   assert abs(x['concentration']-y['concentration'])<.01
out=dict(host=socket.gethostname(),cpu_seconds=time.process_time()-start,code_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),rows=rows,status='PASS numerical gates, finite-window labels only')
pathlib.Path('RESULT.json').write_text(json.dumps(out,indent=2))
for r in rows[1::2]:print(r['K'],r['kick'],r['control'],json.dumps(r['windows'][-1]),'errors',r['norm_error'],r['energy_error'],'work',r['kick_work'])
print('CPU seconds',out['cpu_seconds'])
