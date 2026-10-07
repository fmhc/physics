import math,json,time,socket,hashlib,pathlib
start=time.process_time()
def run(g,d,l,dt):
 a,b=1+0j,0j;t=0.;end=20*math.pi;nerr=0.;herr=0.;err=0.;pmax=0.;zmin=1.
 def f(a,b):return -1j*((d/2+l*abs(a)**2)*a+g*b),-1j*(g*a+(-d/2+l*abs(b)**2)*b)
 def energy(a,b):return d*(abs(a)**2-abs(b)**2)/2+2*g*(a*b.conjugate()).real+l*(abs(a)**4+abs(b)**4)/2
 E0=energy(a,b)
 while t<end:
  h=min(dt,end-t);k1=f(a,b);k2=f(a+h*k1[0]/2,b+h*k1[1]/2);k3=f(a+h*k2[0]/2,b+h*k2[1]/2);k4=f(a+h*k3[0],b+h*k3[1])
  a+=h*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6;b+=h*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6;t+=h
  pb=abs(b)**2;pa=abs(a)**2;pmax=max(pmax,pb);zmin=min(zmin,pa-pb)
  nerr=max(nerr,abs(pa+pb-1));herr=max(herr,abs(energy(a,b)-E0)/max(1,abs(E0)))
  if l==0:
   w=math.sqrt(g*g+d*d/4);exact=(g*g/w**2*math.sin(w*t)**2) if w else 0
   err=max(err,abs(pb-exact))
 assert nerr<1e-5 and herr<1e-5,(g,d,l,dt,nerr,herr)
 if l==0:assert err<2e-6
 if g==0:assert pmax==0
 return dict(g=g,delta=d,nonlinearity=l,dt=dt,pB_max_sampled=pmax,z_min=zmin,norm_error=nerr,energy_error=herr,linear_exact_error=err if l==0 else None)
rows=[run(g,d,l,dt) for g,d,l in [(0,0,0),(1,0,0),(1,1,0),(1,2,0),(1,4,0),(1,0,2),(1,0,6)] for dt in [.01,.005]]
assert rows[-1]['z_min']>0
out=dict(host=socket.gethostname(),cpu_seconds=time.process_time()-start,code_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),T=20*math.pi,rows=rows,status='PASS controls; not extra-dimension or time-emergence evidence')
pathlib.Path('RESULT.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
