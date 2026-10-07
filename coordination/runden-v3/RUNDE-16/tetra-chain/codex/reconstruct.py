import numpy as np, json, time
from itertools import combinations
start=time.process_time()
def geometry(n):
    v=[np.array(x,float) for x in [(0,0,0),(1,0,0),(.5,np.sqrt(3)/2,0),(.5,np.sqrt(3)/6,np.sqrt(2/3))]]
    while len(v)<n:
        a,b,c=v[-3:]; normal=np.cross(b-a,c-a); normal/=np.linalg.norm(normal)
        old=v[-4]; v.append(old-2*np.dot(old-a,normal)*normal)
    v=np.array(v);return v-v.mean(axis=0)
def measure(v,normals):
    signs=normals@v.T>0;n=len(v)
    edges=sorted(set(e for k in range(n-3) for e in combinations(range(k,k+4),2)))
    p=sum(signs[:,a]!=signs[:,b] for a,b in []) if False else np.zeros(len(normals),int)
    for a,b in edges:p+=(signs[:,a]!=signs[:,b])
    counts=np.stack([signs[:,k:k+4].sum(axis=1) for k in range(n-3)],axis=1)
    hit=(counts>0)&(counts<4);t3=((counts==1)|(counts==3)).sum(axis=1);t4=(counts==2).sum(axis=1)
    faces=np.stack([signs[:,k+1:k+4].sum(axis=1) for k in range(n-4)],axis=1)
    c=hit.sum(axis=1)-((faces>0)&(faces<3)).sum(axis=1)
    return p,c,t3,t4,edges
out={'status':'hypothesis_reconstruction','seed':20261002,'sample_size':200000,'measure':'uniform sphere; plane through vertex centroid','models':{}}
for n,label in [(12,'11+1'),(20,'19+1')]:
    v=geometry(n);rng=np.random.default_rng(20261002);ns=rng.normal(size=(200000,3));ns/=np.linalg.norm(ns,axis=1)[:,None]
    p,c,t3,t4,edges=measure(v,ns)
    ticks=[]
    for i,(x,y,z) in enumerate(v):
        t=(np.arctan2(y,x)+np.pi/2)%np.pi/np.pi
        nn=np.array([[np.cos(np.pi*(t+s)),np.sin(np.pi*(t+s)),0] for s in [-1e-8,1e-8]])
        pp,*_=measure(v,nn);ticks.append({'t':float(t),'vertex':i,'before':int(pp[0]),'after':int(pp[1])})
    vals,cnts=np.unique(p,return_counts=True)
    out['models'][label]={'vertices':v.tolist(),'edges':edges,'distribution':dict(zip(map(str,vals),map(lambda x:float(x/len(p)),cnts))),'mean':float(p.mean()),'median':float(np.median(p)),'min':int(p.min()),'max':int(p.max()),'islands_probability':float((c>1).mean()),'formula_failures':int(np.sum(p!=t3+2*t4+2*c)),'edge_error':float(max(abs(np.linalg.norm(v[a]-v[b])-1) for a,b in edges)),'antipodal_ok':bool(np.array_equal(p,measure(v,-ns)[0])),'ticks':sorted(ticks,key=lambda a:a['t'])}
out['cpu_seconds']=time.process_time()-start
with open('RESULT.json','w') as f:json.dump(out,f,indent=2)
print(json.dumps({k:{x:y for x,y in v.items() if x not in ['vertices','edges','ticks']} for k,v in out['models'].items()},indent=2))
