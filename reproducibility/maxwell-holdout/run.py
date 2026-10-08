#!/usr/bin/env python3
"""Fixed-weight new-momentum diagnostic. CUDA spectral kernels only."""
import argparse
import hashlib
import importlib.util
import json
import platform
from pathlib import Path
import time
import numpy as np
import torch

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    'reproduce.py': 'a05feb97c8f1c8d0b35924fbe92c51f2bbe60130abea2282ec36d10c2ab2f283',
    'result.json': '153a695ff94816ce1597cf83b45bb4fef668a0133d3851434c8db3ef5b166222',
    'archive/gwp.json': 'a91fdfd0c86026d0f211dd8f1bb6812db966007f87bbd84d66cc67da16f6fa35',
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', type=Path, default=ROOT.parent/'maxwell-v')
    ap.add_argument('--output', type=Path, default=ROOT/'result.json')
    args = ap.parse_args()
    hashes = {p: hashlib.sha256((args.base/p).read_bytes()).hexdigest() for p in EXPECTED}
    if hashes != EXPECTED:
        raise SystemExit('Frozen input hash mismatch')
    if not torch.cuda.is_available():
        raise SystemExit('CUDA required; no CPU fallback')
    torch.set_num_threads(1)
    started = time.time()
    spec = importlib.util.spec_from_file_location('reproduction', args.base/'reproduce.py')
    r = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r)
    archived = json.loads((args.base/'result.json').read_text())
    pos, simplices = r.geometry()
    faces = sorted({r.face_key([s[i] for i in tri]) for s in simplices for tri in r.TRIANGLES})
    edges = list(dict.fromkeys(r.edge_key(s[a],s[b])[0] for s in simplices for a,b in r.PAIRS))
    eid = {e:i for i,e in enumerate(edges)}
    rows, cols, signs, shifts = [], [], [], []
    for f,vs in enumerate(faces):
        for a,b in [(0,1),(1,2),(2,0)]:
            e,t,s = r.edge_key(vs[a],vs[b])
            rows.append(f); cols.append(eid[e]); signs.append(s); shifts.append(t)
    rows = torch.tensor(rows,device='cuda'); cols = torch.tensor(cols,device='cuda')
    signs = r.tensor(signs); shifts = r.tensor(shifts)
    es = r.tensor([e[2] for e in edges])
    b0 = torch.tensor([e[0] for e in edges],device='cuda')
    b1 = torch.tensor([e[1] for e in edges],device='cuda')
    er = torch.arange(len(edges),device='cuda')
    points = [{'kind':'random','q':q} for q in np.random.default_rng(20261008).uniform(-np.pi,np.pi,(256,4)).tolist()]
    directions = [('axis'+str(i),[int(j==i) for j in range(4)]) for i in range(4)]
    directions += [('diagonal4',[1,1,1,1]),('spatial111',[1,1,1,0])]
    for name,d in directions:
        norm = sum(x*x for x in d)**.5
        for sign in [1,-1]:
            for scale in [1.,.1,.01,.001]:
                points.append({'kind':'ray','direction':name,'sign':sign,'scale':scale,'q':[sign*scale*x/norm for x in d]})
    old = {tuple(q) for q in archived['momenta']}
    assert not any(tuple(p['q']) in old for p in points)
    weights = {name:r.tensor(arm['weights']) for name,arm in archived['arms'].items()}
    output = {'schema':1,'seed':20261008,'tau':archived['tau'],'counts':dict(vertices=len(pos),edges=len(edges),faces=len(faces),simplices=len(simplices)), 'tolerance':1e-10,'points':points,'arms':{name:[] for name in weights}}
    ranks=[]; identities=[]; singular_ratios=[]
    for point in points:
        q=r.tensor(point['q'])
        d1=torch.zeros((len(faces),len(edges)),dtype=torch.complex128,device='cuda')
        d1.index_put_((rows,cols),signs*torch.exp(1j*(shifts@q)),accumulate=True)
        d0=torch.zeros((len(edges),len(pos)),dtype=torch.complex128,device='cuda')
        d0.index_put_((er,b1),torch.exp(1j*(es@q)),accumulate=True)
        d0.index_put_((er,b0),-torch.ones(len(edges),dtype=torch.complex128,device='cuda'),accumulate=True)
        identities.append(float((d1@d0).abs().max()))
        u,sv,_=torch.linalg.svd(d0,full_matrices=True)
        rank=int((sv>1e-10*sv[0]).sum()); ranks.append(rank)
        singular_ratios.append(float(sv[-1]/sv[0]))
        d=d1@u[:,rank:]
        for name,w in weights.items():
            k=d.mH@(w[:,None]*d); k=(k+k.mH)/2
            ev,v=torch.linalg.eigh(k); vmax=ev.abs().max(); v0=v[:,0]
            relative=float(ev[0]/vmax)
            residual=float(torch.linalg.vector_norm(k@v0-ev[0]*v0)/vmax)
            rayleigh=float(((v0.conj()@(k@v0)).real-ev[0]).abs()/vmax)
            output['arms'][name].append({'lowest_five':ev[:5].tolist(),'max_abs':float(vmax),'min_relative':relative,'classification':'negative' if relative < -1e-10 else 'positive' if relative > 1e-10 else 'unresolved','residual':residual,'rayleigh_discrepancy':rayleigh})
    output['gauge_ranks']=ranks; output['d1d0_max']=max(identities)
    output['d0_smallest_over_largest_singular_value']=singular_ratios
    output['checks']={'counts':output['counts']==dict(vertices=10,edges=146,faces=484,simplices=232),'gauge_rank':set(ranks)=={10},'gauge_identity':max(identities)<1e-10,'sample_count':len(points)==304,'residuals':all(s['residual']<1e-10 and s['rayleigh_discrepancy']<1e-10 for arm in output['arms'].values() for s in arm)}
    output['summary']={name:{'classifications':{c:sum(s['classification']==c for s in arm) for c in ['negative','positive','unresolved']},'min_relative':min(s['min_relative'] for s in arm),'max_residual':max(s['residual'] for s in arm)} for name,arm in output['arms'].items()}
    torch.cuda.synchronize()
    output['provenance']={'input_hashes':hashes,'source_hash':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'plan_hash':hashlib.sha256((ROOT/'PLAN.md').read_bytes()).hexdigest(),'python':platform.python_version(),'numpy':np.__version__,'torch':torch.__version__,'cuda':torch.version.cuda,'device':torch.cuda.get_device_name(),'elapsed_s':time.time()-started,'peak_cuda_allocated_bytes':torch.cuda.max_memory_allocated(),'backend':'CUDA complex128 eigensystems; CPU integer geometry, PRNG, IO'}
    output['passed']=all(output['checks'].values())
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'checks':output['checks'],'summary':output['summary'],'provenance':output['provenance']}))
    raise SystemExit(0 if output['passed'] else 1)

if __name__=='__main__':
    main()
