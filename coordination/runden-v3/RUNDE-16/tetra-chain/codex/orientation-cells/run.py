"""Float64 spherical-cell reconstruction, not interval certification."""
import numpy as np
from scipy.optimize import linprog
from itertools import combinations
import json,time,os
from collections import deque,defaultdict
start=time.process_time()
def checktime():
    if time.process_time()-start>50:raise RuntimeError('CPU budget checkpoint')
def partition(v,edges):
    normals=[];mapping=[]
    for p in v:
        if np.linalg.norm(p)<1e-12:raise ValueError('central vertex')
        p=p/np.linalg.norm(p);orient=1
        if p[np.argmax(abs(p))]<0:p=-p;orient=-1
        found=next((i for i,q in enumerate(normals) if np.linalg.norm(p-q)<1e-10),None)
        if found is None:found=len(normals);normals.append(p)
        mapping.append((found,orient))
    a=np.array(normals);m=len(a);corners=[]
    for i,j in combinations(range(m),2):
        c=np.cross(a[i],a[j]);cn=np.linalg.norm(c)
        if cn>1e-10:
            c/=cn;corners.extend([c,-c])
    # Unique vertices; degeneracies are retained as coincident circle intersections.
    unique=[]
    for c in corners:
        if all(np.linalg.norm(c-q)>1e-9 for q in unique):unique.append(c)
    corners=np.array(unique);seed=np.array([1,.371,.239]);seed/=np.linalg.norm(seed)
    if np.min(abs(a@seed))<1e-9:raise ValueError('seed degeneracy')
    initial=tuple(np.where(a@seed>0,1,-1));queue=deque([initial]);seen={initial};cells=[];unresolved=[]
    while queue:
        s=np.array(queue.popleft());checktime();b=s[:,None]*a
        fit=linprog([0,0,0,-1],A_ub=np.column_stack([-b,np.ones(m)]),b_ub=np.zeros(m),bounds=[(-1,1)]*3+[(None,None)],method='highs')
        if not fit.success:raise RuntimeError(fit.message)
        t=fit.x[-1]
        if t<=1e-9:
            if t>1e-11:unresolved.append({'sign':s.tolist(),'margin':float(t)})
            continue
        center=fit.x[:3];center/=np.linalg.norm(center)
        poly=corners[np.all(corners@b.T>=-1e-9,axis=1)]
        if len(poly)<3:raise RuntimeError('polygon has fewer than 3 vertices')
        u=poly[0]-center*np.dot(center,poly[0]);u/=np.linalg.norm(u);w=np.cross(center,u)
        angle=np.arctan2(poly@w,poly@u);poly=poly[np.argsort(angle)]
        area=0
        for x,y in zip(poly,np.roll(poly,-1,axis=0)):
            area+=2*np.arctan2(abs(np.dot(center,np.cross(x,y))),1+center@x+x@y+y@center)
        vs=np.array([s[i]*o for i,o in mapping]);p=sum(vs[i]!=vs[j] for i,j in edges)
        hit=np.array([len(set(vs[k:k+4]))==2 for k in range(len(v)-3)])
        face=sum(len(set(vs[k+1:k+4]))==2 for k in range(len(v)-4))
        c=int(hit.sum()-face)
        cells.append({'sign':s.tolist(),'area':float(area),'P':int(p),'C_face':c,'margin':float(t)})
        for i in range(m):
            child=s.copy();child[i]*=-1;key=tuple(child)
            if key not in seen:seen.add(key);queue.append(key)
    total=sum(c['area'] for c in cells);dist=defaultdict(float)
    lookup={tuple(c['sign']):c for c in cells};anti=0
    for c in cells:
        partner=lookup.get(tuple(-np.array(c['sign'])))
        if partner is None:raise RuntimeError('missing antipode')
        anti=max(anti,abs(partner['area']-c['area']))
        dist[c['P']]+=c['area']/(4*np.pi)
    if unresolved or abs(total-4*np.pi)>1e-7 or anti>1e-7:raise RuntimeError('area/antipode/margin gate failed')
    return {'cell_count':len(cells),'unique_circles':m,'area_sum':total,'antipodal_area_error':anti,'distribution':dict(sorted(dist.items())),'mean':sum(p*q for p,q in dist.items()),'multi_face_probability':sum(c['area'] for c in cells if c['C_face']>1)/(4*np.pi),'cells':cells}
# Octants of the sphere: eight equal regions. No tetrahedral interpretation here.
control=partition(np.eye(3),[(0,1),(1,2),(0,2)])
assert control['cell_count']==8 and max(abs(c['area']-np.pi/2) for c in control['cells'])<1e-10
source=json.load(open('INPUT.json'));out={'method':'float64 LP and spherical areas; numerical, not rigorous certificate','control_octants':True,'models':{}}
for label,m in source['models'].items():
    out['models'][label]=partition(np.array(m['vertices']),m['edges'])
    out['cpu_seconds']=time.process_time()-start
    with open('RESULT.partial.json','w') as f:json.dump(out,f,indent=2)
os.replace('RESULT.partial.json','RESULT.json')
print(json.dumps({k:{x:y for x,y in v.items() if x!='cells'} for k,v in out['models'].items()},indent=2))
