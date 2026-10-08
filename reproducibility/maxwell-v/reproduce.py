#!/usr/bin/env python3
"""Portable fixed-input QUANT-2 Maxwell reproduction. Numerical kernels: CUDA only."""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import time
import numpy as np
import torch

ROOT = Path(__file__).resolve().parent
PAIRS = list(itertools.combinations(range(5), 2))
TRIANGLES = [tuple(i for i in range(5) if i not in pair) for pair in PAIRS]
BIVECTORS = list(itertools.combinations(range(4), 2))


def add(*vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(3))


def mul(c, v):
    return tuple(c*x for x in v)


def geometry():
    """Exact-integer translation of ew.geometrie('V'), rk2.netz_raum and tent lifting."""
    r = [(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)]
    c1, c2 = (-2,-2,-2), (4,4,4)
    pos8 = r + [c1,c2] + [add(c1,mul(-1,p)) for p in r]
    tets = [r, [add((2,2,2),mul(-1,p)) for p in r]]
    for c, sg in [(c1,1),(c2,-1)]:
        for a in range(4):
            tets.append([c]+[add(c,mul(sg,add(mul(2,r[a]),r[b]))) for b in range(4) if b != a])
        for a in range(4):
            p = [add(c,mul(sg,add(mul(2,r[b]),r[d]))) for b in range(4) for d in range(4) if a not in (b,d) and b != d]
            nb = [[j for j in range(6) if j != i and sum((p[i][k]-p[j][k])**2 for k in range(3)) == 8] for i in range(6)]
            assert all(len(n)==2 for n in nb)
            cycle = [0,nb[0][0]]
            while len(cycle)<6:
                cycle.append(next(j for j in nb[cycle[-1]] if j != cycle[-2]))
            assert cycle[0] in nb[cycle[-1]]
            h = add(c,mul(-sg,r[a]))
            for i in range(6):
                tets.append([c,h,p[cycle[i]],p[cycle[(i+1)%6]]])
    def decompose(p):
        for b,s in enumerate(pos8):
            x,y,z = [p[i]-s[i] for i in range(3)]
            n8 = (-x+y+z,x-y+z,x+y-z)
            if all(n%8 == 0 for n in n8):
                return b,tuple(n//8 for n in n8)
        raise ValueError('not a lattice vertex')
    def position(v):
        b,(x,y,z) = v
        return tuple(pos8[b][i]+(4*(y+z),4*(x+z),4*(x+y))[i] for i in range(3))
    simplices = []
    for tet in tets:
        vs = sorted(map(decompose,tet),key=lambda v:(v[0],*position(v)))
        for j in range(4):
            simplices.append([(b,n+(1,)) for b,n in vs[:j+1]]+[(b,n+(0,)) for b,n in vs[j:]])
    return pos8,simplices


def face_key(vs):
    return min(tuple(sorted((b,tuple(x-y for x,y in zip(n,n0))) for b,n in vs)) for _,n0 in vs)


def edge_key(a,b):
    ba,na=a; bb,nb=b
    d=tuple(y-x for x,y in zip(na,nb))
    if ba<bb or (ba==bb and d>(0,0,0,0)):
        return (ba,bb,d),na,1
    return (bb,ba,tuple(-x for x in d)),nb,-1


def tensor(x,complex_=False):
    return torch.tensor(x,dtype=torch.complex128 if complex_ else torch.float64,device='cuda')


def orthocenter(p,w):
    e=p[:,1:]-p[:,:1]
    gram=e@e.transpose(-1,-2)
    rhs=gram.diagonal(dim1=-2,dim2=-1)-(w[:,1:]-w[:,:1])
    coeff=torch.linalg.solve(2*gram,rhs.unsqueeze(-1)).squeeze(-1)
    return p[:,0]+torch.einsum('sm,smi->si',coeff,e)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=Path('result.json'))
    args=ap.parse_args()
    if not torch.cuda.is_available():
        raise SystemExit('CUDA is required; no CPU fallback is permitted.')
    torch.set_num_threads(1)
    started=time.time()
    archived=json.loads((ROOT/'archive/gwp.json').read_text())
    tau=archived['tau']
    pos8,simp=geometry()
    faces=sorted({face_key([s[i] for i in tri]) for s in simp for tri in TRIANGLES})
    fid={f:i for i,f in enumerate(faces)}
    edges=list(dict.fromkeys(edge_key(s[a],s[b])[0] for s in simp for a,b in PAIRS))
    eid={e:i for i,e in enumerate(edges)}
    labels=torch.tensor([[fid[face_key([s[i] for i in tri])] for tri in TRIANGLES] for s in simp],device='cuda')
    sub=torch.tensor([[b for b,_ in s] for s in simp],device='cuda')
    def pos(v):
        b,(x,y,z,t)=v
        return [pos8[b][0]/8+(y+z)/2,pos8[b][1]/8+(x+z)/2,pos8[b][2]/8+(x+y)/2,tau*(b/10+t)]
    x=tensor([[pos(v) for v in s] for s in simp])
    p=tensor([[pos(v) for v in f] for f in faces])
    a,b=p[:,1]-p[:,0],p[:,2]-p[:,0]
    biv=.5*torch.stack([a[:,m]*b[:,n]-a[:,n]*b[:,m] for m,n in BIVECTORS],1)
    area=torch.linalg.vector_norm(biv,dim=1)
    rows,cols,signs,shifts=[],[],[],[]
    for f,vs in enumerate(faces):
        for a,b in [(0,1),(1,2),(2,0)]:
            e,t,s=edge_key(vs[a],vs[b]); rows.append(f); cols.append(eid[e]); signs.append(s); shifts.append(t)
    rows=torch.tensor(rows,device='cuda'); cols=torch.tensor(cols,device='cuda')
    signs=tensor(signs); shifts=tensor(shifts)
    edge_shifts=tensor([e[2] for e in edges])
    edge_b0=torch.tensor([e[0] for e in edges],device='cuda')
    edge_b1=torch.tensor([e[1] for e in edges],device='cuda')
    er=torch.arange(len(edges),device='cuda')
    qs=np.random.default_rng(99).uniform(-np.pi,np.pi,(96,4)).tolist()
    dq=[]; d1d0max=0.; ranklist=[]
    for qvalues in qs:
        q=tensor(qvalues)
        d1=torch.zeros((len(faces),len(edges)),dtype=torch.complex128,device='cuda')
        d1.index_put_((rows,cols),signs*torch.exp(1j*(shifts@q)),accumulate=True)
        d0=torch.zeros((len(edges),len(pos8)),dtype=torch.complex128,device='cuda')
        d0.index_put_((er,edge_b1),torch.exp(1j*(edge_shifts@q)),accumulate=True)
        d0.index_put_((er,edge_b0),-torch.ones(len(edges),dtype=torch.complex128,device='cuda'),accumulate=True)
        d1d0max=max(d1d0max,float((d1@d0).abs().max()))
        u,sv,_=torch.linalg.svd(d0,full_matrices=True)
        rank=int((sv>1e-10*sv[0]).sum()); ranklist.append(rank)
        dq.append(d1@u[:,rank:])
    out={'schema':1,'input_dimension':'3 spatial + 1 Euclidean time','tau':tau,'counts':{'vertices':len(pos8),'edges':len(edges),'faces':len(faces),'simplices':len(simp)},'seed':99,'momenta':qs,'d1d0_max':d1d0max,'gauge_ranks':ranklist,'arms':{},'checks':{}}
    for name,omega,archive_key in [('circumcentric',[0.]*10,'omega0_nq96'),('archived_power_dual',archived['omega'],'gewichtet_nq96')]:
        wv=tensor(omega)[sub]
        cs=orthocenter(x,wv)
        ct=torch.stack([orthocenter(x[:,[i for i in range(5) if i != m]],wv[:,[i for i in range(5) if i != m]]) for m in range(5)],1)
        cf=torch.stack([orthocenter(x[:,list(tri)],wv[:,list(tri)]) for tri in TRIANGLES],1)
        dual=torch.zeros(len(faces),dtype=torch.float64,device='cuda')
        for k,(l0,m0) in enumerate(PAIRS):
            for l,m in [(l0,m0),(m0,l0)]:
                t=ct[:,m]; d1=t-cf[:,k]; d2=cs-t
                s1=torch.sign((d1*(x[:,l]-cf[:,k])).sum(1)); s2=torch.sign((d2*(x[:,m]-t)).sum(1))
                contribution=.5*s1*s2*torch.linalg.vector_norm(d1,dim=1)*torch.linalg.vector_norm(d2,dim=1)
                # Fixed order sum avoids nondeterministic GPU floating scatter atomics.
                for f in range(len(faces)):
                    dual[f]+=contribution[labels[:,k]==f].sum()
        weights=dual/area
        normalization=float((torch.einsum('f,fa,fb->ab',weights,biv,biv)-tau/4*torch.eye(6,dtype=torch.float64,device='cuda')).abs().max()/(tau/4))
        spectra=[]
        for d in dq:
            k=d.mH@(weights[:,None]*d)
            ev=torch.linalg.eigvalsh((k+k.mH)/2)
            spectra.append({'min':float(ev[0]),'max_abs':float(ev.abs().max()),'min_relative':float(ev[0]/ev.abs().max())})
        minrel=min(s['min_relative'] for s in spectra)
        negq=sum(s['min_relative']<0 for s in spectra)
        negw=int((weights<0).sum())
        arm={'omega':omega,'weights':weights.tolist(),'n_negative_weights':negw,'n_negative_weights_tol_1e12':int((weights < -1e-12*weights.abs().max()).sum()),'normalization_relative_error':normalization,'minimum_eigenvalue_relative':minrel,'negative_momenta':negq,'spectra':spectra}
        out['arms'][name]=arm
        expected=archived[archive_key]
        out['checks'][name]={'normalization':normalization<1e-10,'negative_weights':negw==expected['n_neg_w'],'negative_momenta':negq==expected['bloch_q_neg'],'minimum_eigenvalue':abs(minrel-expected['bloch_lmin_rel'])<1e-8,'all_momenta':len(spectra)==96}
    out['checks']['structure']={'counts':out['counts']==dict(vertices=10,edges=146,faces=484,simplices=232),'gauge_identity':d1d0max<1e-10,'gauge_rank':set(ranklist)=={10}}
    out['passed']=all(all(c.values()) for c in out['checks'].values())
    torch.cuda.synchronize()
    out['provenance']={'python':platform.python_version(),'numpy':np.__version__,'torch':torch.__version__,'cuda':torch.version.cuda,'device':torch.cuda.get_device_name(),'numeric_backend':'CUDA float64/complex128; CPU integer geometry, PRNG, IO','elapsed_s':time.time()-started,'peak_cuda_allocated_bytes':torch.cuda.max_memory_allocated(),'sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),ROOT/'PLAN.md',ROOT/'archive/gwp.json',ROOT/'requirements.txt']}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'passed':out['passed'],'counts':out['counts'],'checks':out['checks'],'elapsed_s':out['provenance']['elapsed_s']}))
    raise SystemExit(0 if out['passed'] else 1)

if __name__=='__main__':
    main()
