#!/usr/bin/env python3
"""Physical FV transport from 18 saved rings; no PDE or new evolution."""
import time
START=time.process_time()
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

HASH=dict(dynamics='466b25fb813770a1ab13eea962c93b39308dfe1ad22171fe638c60fdafef998d',
 time_code='74ba12a56e60241a967c2ff143a6489adbd7b27a3b72ddeeb0d3d29fee3c43c6',
 phase_code='3509332b4732c8497e9246855fc7be6254ff1681e3e2e99b823457180aaa1446',
 amplitude_code='5e8f8c201f9d0f0090f442f6d6173c9e4f1362cfecbd55fc9ac9f823614dc4c9',
 time='a3f302b50f184ef2b7fdf9d92afb903068e22436d2b3547fa4248f80e9a56cc3',
 phase='b7d938e4bda00bb05598f540f05320b2e3cad7a8a8f3f4be940a9d5884b8eafd',
 amplitude='2fa8c40331f18ed677788629733806109dbc9a622c4d8ff22e065c82979adefd')
EPS=np.finfo(np.float64).eps
GAM=float(64*EPS/(1-64*EPS))
H=.05
TIMES=np.arange(1281)*.1
OBS=('E','Q','G')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(ok,message):
    if not ok:
        raise ValueError(message)


def checked(path,digest):
    require(sha(path)==digest,'Hash mismatch: '+str(path))
    return path


def module(path,digest,name):
    import importlib.util
    checked(path,digest)
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec); spec.loader.exec_module(obj)
    return obj


def checkpoint():
    if time.process_time()-START>=8:
        raise RuntimeError('INCOMPLETE: 8 CPU-s checkpoint; 10 CPU-s total target')


def save(directory,result):
    result['cpu_seconds']=time.process_time()-START
    tmp=directory/'RESULT.tmp'
    tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    tmp.replace(directory/'RESULT.json')


# Fixed local forward-sensitivity formulas, not interval/ball arithmetic.
# Inputs are stored float64 values; no prior evolution uncertainty is included.
def add_error(x,y,ex=0.,ey=0.):
    return ex+ey+GAM*(abs(x)+abs(y))


def product_error(x,y,ex=0.,ey=0.):
    return abs(x)*ey+abs(y)*ex+ex*ey+GAM*abs(x)*abs(y)


def square_error(x,ex=0.):
    return 2*abs(x)*ex+ex*ex+GAM*abs(x)**2


def weighted(x,ex,w):
    value=w*x
    # Fixed geometric weight evaluation plus its multiplication.
    error=product_error(w,x,GAM*abs(w),ex)
    return value,error


def reduction(x,ex,axis=-1):
    n=x.shape[axis]; gu=float((n-1)*EPS/(1-(n-1)*EPS))
    return np.sum(x,axis=axis),np.sum(ex,axis=axis)+gu*np.sum(abs(x),axis=axis)


def physical_series(r,p,v,c,w,ev,omega):
    """Return shell E/Q/G and face E/Q/G, and propagated local errors."""
    s=abs(p)**2; es=square_error(p)
    kin=abs(v)**2; ekin=square_error(v,ev)
    wc=.5*w*w; ewc=.5*square_error(w)+GAM*abs(wc)
    cm=c-1; cp=c+1
    eg=product_error(cm,cp,GAM*(abs(c)+1),GAM*(abs(c)+1)); cg=cm*cp
    vac=.25*cg*cg; evac=.25*square_error(cg,eg)+GAM*abs(vac)
    c2=c*c; ec2=square_error(c)
    factor=1+c2; efactor=ec2+GAM*(1+abs(c2))
    quadratic=factor*s; equadratic=product_error(factor,s,efactor,es)
    s2=s*s; es2=square_error(s,es)
    s3=.5*s2*s; es3=.5*product_error(s2,s,es2,es)+GAM*abs(s3)
    onsite=kin+wc+vac+quadratic-s2+s3
    eonsite=ekin+ewc+evac+equadratic+es2+es3+GAM*(abs(kin)+abs(wc)+abs(vac)+abs(quadratic)+abs(s2)+abs(s3))
    vol=4*np.pi*H*(r*r+H*H/12)
    cellE,errE=weighted(onsite,eonsite,vol)
    rawQ=2*np.imag(np.conj(p)*v)
    erawQ=2*product_error(p,v,0.,ev)+GAM*abs(rawQ)
    cellQ,errQ=weighted(rawQ,erawQ,vol)
    dp=p[:,1:]-p[:,:-1]; dc=c[:,1:]-c[:,:-1]
    edp=GAM*(abs(p[:,1:])+abs(p[:,:-1])); edc=GAM*(abs(c[:,1:])+abs(c[:,:-1]))
    gp=abs(dp)**2; gc=.5*dc*dc
    egp=square_error(dp,edp); egc=.5*square_error(dc,edc)+GAM*abs(gc)
    face=.5*(r[1:]+r[:-1]); k=4*np.pi*face**2/H
    edge,eedge=weighted(gp+gc,add_error(gp,gc,egp,egc),k)
    vs=v[:,1:]+v[:,:-1]; ws=w[:,1:]+w[:,:-1]
    evs=add_error(v[:,1:],v[:,:-1],ev[:,1:],ev[:,:-1])
    ews=GAM*(abs(w[:,1:])+abs(w[:,:-1]))
    fp=np.real(np.conj(vs)*dp); fc=.5*ws*dc
    efp=product_error(vs,dp,evs,edp)
    efc=.5*product_error(ws,dc,ews,edc)+GAM*abs(fc)
    FE,eFE=weighted(-(fp+fc),add_error(fp,fc,efp,efc),k)
    qface=-2*np.imag(np.conj(p[:,:-1])*p[:,1:])
    eqface=2*product_error(p[:,:-1],p[:,1:])+GAM*abs(qface)
    FQ,eFQ=weighted(qface,eqface,k)
    shells=[]; shell_errors=[]
    for lo,hi in ((40.,45.),(45.,50.)):
        cells=np.flatnonzero((r>=lo)&(r<hi)); first=int(cells[0]); last=int(cells[-1])
        require(first>0 and last+1<len(r),'Missing shell halo')
        weights=np.ones(last-first+2); weights[[0,-1]]=.5
        evv,eee=weighted(edge[:,first-1:last+1],eedge[:,first-1:last+1],weights)
        ee,eeerr=reduction(evv,eee)
        ce,ceerr=reduction(cellE[:,cells],errE[:,cells]); cq,cqerr=reduction(cellQ[:,cells],errQ[:,cells])
        energy=ce+ee; energyerr=add_error(ce,ee,ceerr,eeerr)
        rot=energy-omega*cq
        roterr=add_error(energy,omega*cq,energyerr,abs(omega)*cqerr+GAM*abs(omega*cq))
        shells.append(np.stack((energy,cq,rot),axis=-1)); shell_errors.append(np.stack((energyerr,cqerr,roterr),axis=-1))
    indices=[]
    for radius in (40.,45.,50.):
        ix=np.flatnonzero(abs(face-radius)<1e-12)
        require(len(ix)==1,'Face absent/ambiguous'); indices.append(int(ix[0]))
    FE=FE[:,indices]; eFE=eFE[:,indices]; FQ=FQ[:,indices]; eFQ=eFQ[:,indices]
    FG=FE-omega*FQ
    eFG=add_error(FE,omega*FQ,eFE,abs(omega)*eFQ+GAM*abs(omega*FQ))
    values=dict(shell=np.stack(shells,axis=1),flux=np.stack((FE,FQ,FG),axis=-1))
    errors=dict(shell=np.stack(shell_errors,axis=1),flux=np.stack((eFE,eFQ,eFG),axis=-1))
    require(all(np.all(np.isfinite(x)) for x in list(values.values())+list(errors.values())),
            'Nonfinite local observables/errors')
    return values,errors


def analytic_qa(dyn):
    g=dyn.Grid(H); r=g.r; rows=[]
    for kind in ('regular','vacuum','chi_only'):
        c=1+.02*np.exp(-((r-44)/9)**2); w=.03*np.exp(-((r-47)/11)**2)
        p=.02*np.exp(-((r-46)/12)**2)*np.exp(.17j*r)
        v=(.013+.027j)*np.exp(-((r-43)/13)**2)
        if kind!='regular':
            p=np.zeros_like(p); v=np.zeros_like(v)
        if kind=='vacuum':
            c=np.ones_like(r); w=np.zeros_like(r)
        series,errors=physical_series(r,p[None],v[None],c[None],w[None],np.zeros((1,len(r))),1.)
        ap,ac=dyn.forces(g,p,c); s=abs(p)**2
        terms=(2*np.real(np.conj(v)*ap),w*ac,
               2*(1+c*c-2*s+1.5*s*s)*np.real(np.conj(p)*v),c*(c*c-1+2*s)*w)
        cell_dot=g.vol*sum(terms)
        qdot=2*g.vol*np.imag(np.conj(v)*v+np.conj(p)*ap)
        dp=np.diff(p); dc=np.diff(c); dv=np.diff(v); dw=np.diff(w)
        edgedot=g.area[:-1]/H*(2*np.real(np.conj(dp)*dv)+dc*dw)
        for si,(lo,hi) in enumerate(((40.,45.),(45.,50.))):
            ix=np.flatnonzero((r>=lo)&(r<hi)); a=int(ix[0]); b=int(ix[-1])
            ed=float(np.sum(cell_dot[ix])+np.sum(edgedot[a:b])+.5*(edgedot[a-1]+edgedot[b]))
            qd=float(np.sum(qdot[ix]))
            rhs=series['flux'][0,si]-series['flux'][0,si+1]
            escale=float(np.sum(g.vol[ix]*sum(abs(t[ix]) for t in terms))
                +np.sum(abs(edgedot[a-1:b+1]))+abs(rhs[0]))
            qscale=float(np.sum(abs(qdot[ix]))+abs(rhs[1]))
            er=abs(ed-float(rhs[0])); qr=abs(qd-float(rhs[1]))
            passed=(er==0 if escale==0 else er/escale<1e-10)
            passed=passed and (qr==0 if qscale==0 else qr/qscale<1e-10)
            rows.append(dict(kind=kind,shell=si,energy_defect=er,charge_defect=qr,
                energy_scale=escale,charge_scale=qscale,passed=bool(passed)))
        if kind=='vacuum':
            require(all(np.all(x==0) for x in series.values()),'Vacuum observables nonzero')
            # Local difference-square uncertainty is O(gamma64²), not O(gamma64).
            e=GAM*2.; null_square=float(square_error(0.,e))
            require(null_square==e*e,'Vacuum square error lost quadratic scaling')
        if kind=='chi_only':
            require(np.max(abs(series['flux'][...,0]))>0 and np.all(series['flux'][...,1]==0),
                    'Real chi energy flux missing')
    require(all(x['passed'] for x in rows),'Analytical FV balance QA failed')
    return rows


def load_manifests(args):
    docs={k:json.loads(checked(getattr(args,k+'_dir')/'RESULT.json',HASH[k]).read_text())
          for k in ('time','phase','amplitude')}
    require(docs['time']['status']=='UNRESOLVED','Old nonlinear identity changed')
    for k,status in (('phase','CONTROLLED_PHASE_CYCLE_CAUSAL_COMPONENTS'),
                     ('amplitude','RESOLVED_AMPLITUDE_DIFFERENCE_ON_FIXED_GRID')):
        require(docs[k]['status']==status and docs[k]['terminal_complete'],'Incomplete predecessor '+k)
    identity=[x for x in docs['time']['inputs'] if x['h']==H]
    require(len(identity)==1,'Ambiguous common inputs')
    for name,doc in docs.items():
        require(doc['code_sha256']==HASH[name+'_code'],'Predecessor code mismatch')
        require([x for x in doc['inputs'] if x['h']==H]==identity,'Input gauge mismatch')
    require(docs['phase']['bound_hashes']['observed']==HASH['time']
            and docs['amplitude']['bound_hashes']['observed']==HASH['time']
            and docs['amplitude']['bound_hashes']['phase_result']==HASH['phase'],'History mismatch')
    phase=docs['phase']['phase_change']; norm=docs['amplitude']['normalization']
    require(phase['alpha']==norm['alpha_large'] and phase['rho']==norm['rho']
            and phase['omega']==norm['omega'] and phase['multiplier']==[0.,1.]
            and not phase['renormalized'] and not norm['renormalized'],'Phase/normalization mismatch')
    requests=[]
    for level,dt in (('base',.01),('time',.005)):
        for angle,eps in [(0,0.)]+[(angle,e) for angle in (0,90) for e in (.001,-.001,.002,-.002)]:
            source=('time' if eps==0 or (angle==0 and (abs(eps)==.002 or level=='base'))
                    else 'phase' if abs(eps)==.002 else 'amplitude')
            doc=docs[source]
            matches=[a for a in doc['arms'] if a['level']==level and a['epsilon']==eps
                and (source!='amplitude' or a['phase_degrees']==angle)]
            require(len(matches)==1,'Saved arm absent/ambiguous')
            arm=matches[0]; samples=arm['samples']; meta=arm['initial']
            require(arm['complete'] and arm['h']==H and arm['dt']==dt and len(samples)==321,
                    'Incomplete arm samples')
            require(np.allclose([x['t'] for x in samples],np.arange(321)*.4,rtol=0,atol=1e-12),
                    'Diagnostic sample times changed')
            for d in samples:
                require(all(np.isfinite(d[k]) for k in ('E','Q','Edrift','Qdrift','balance','collar'))
                        and max(d['Edrift'],d['Qdrift'],d['balance'])<=1e-5
                        and d['collar']/samples[0]['E']<=1e-8,'Stored conservation gate failed')
                if eps==0:
                    require(all(np.isfinite(d[k]) and d[k]<.004 for k in
                        ('rphi','rchi','tphi','tchi','driftphi','driftchi')),'Stored baseline failed')
            require(meta['reference_norm']==norm['s'] and meta['alpha']==eps*norm['s']
                    and meta['canonical_start_error']<1e-10 and meta['charge_identity_error']<1e-10,
                    'Stored initial normalization/adapter failed')
            if eps!=0:
                if source=='time':
                    lev=[x for x in doc['levels'] if x['level']==level]
                    require(len(lev)==1 and lev[0]['complete'],'Original pair level absent')
                    pairs=[x for x in lev[0]['pairs'] if x['epsilon']==abs(eps)]
                    require(len(pairs)==1 and pairs[0]['passed'] and pairs[0]['max_error']<.05,
                            'Original full odd gate failed')
                else:
                    pairs=[x for x in doc['pairs'] if x['level']==level
                        and (source!='amplitude' or x['phase_degrees']==angle)]
                    require(len(pairs)==1 and pairs[0]['complete'] and pairs[0]['odd_passed']
                            and pairs[0]['odd_max_error']<.05,'Phase/amplitude full odd gate failed')
            if source=='phase':
                require(arm['phase']==np.pi/2,'Saved theta90 mismatch')
            requests.append(dict(level=level,dt=dt,phase_degrees=angle,epsilon=eps,
                source=source,ring_artifact=arm['ring_artifact'],initial=meta))
    require(len(requests)==18,'Expected exactly 18 saved arms')
    return requests,phase,identity[0]


def read_arm(args,request,r,omega):
    entry=request['ring_artifact']; directory=getattr(args,request['source']+'_dir')
    path=checked(directory/entry['file'],entry['sha256'])
    with np.load(path,allow_pickle=False) as z:
        require(np.array_equal(z['t'],TIMES) and np.array_equal(z['r'],r)
                and list(z['components'])==['phi','phi_t','chi','chi_t'],'Ring axes/schema mismatch')
        fields=z['rotating_fields']
        require(fields.shape==(1281,4,len(r)) and fields.dtype==np.complex128
                and np.all(np.isfinite(fields)),'Nonfinite/wrong ring')
        require(np.all(fields[:,2:].imag==0),'Stored chi fields not real')
        p=fields[:,0]; d=fields[:,1]; c=fields[:,2].real; w=fields[:,3].real
        v=d+1j*omega*p
        ev=GAM*(abs(d)+abs(omega*p))+GAM*abs(omega*p)
        return physical_series(r,p,v,c,w,ev,omega)


def window(times,x,ex,left,right):
    def endpoint(t):
        j=int(np.searchsorted(times,t))
        if j<len(times) and abs(times[j]-t)<1e-12:
            return x[j],ex[j]
        require(0<j<len(times),'Window outside stored range')
        denominator=times[j]-times[j-1]
        a=(t-times[j-1])/denominator
        en=GAM*(abs(t)+abs(times[j-1]))
        ed=GAM*(abs(times[j])+abs(times[j-1]))
        require(abs(denominator)>ed,'Unresolved interpolation denominator')
        ea=(en+abs(a)*ed)/(abs(denominator)-ed)+GAM*abs(a)
        left_part=(1-a)*x[j-1]; right_part=a*x[j]
        value=left_part+right_part
        el=product_error(1-a,x[j-1],ea+GAM*(1+abs(a)),ex[j-1])
        er=product_error(a,x[j],ea,ex[j])
        error=add_error(left_part,right_part,el,er)
        return value,error
    vl,el=endpoint(left); vr,er=endpoint(right); inside=(times>left)&(times<right)
    return np.r_[left,times[inside],right],np.concatenate((vl[None],x[inside],vr[None])),np.concatenate((el[None],ex[inside],er[None]))


def integral(t,x,ex):
    weights=np.diff(t); ew=GAM*(abs(t[1:])+abs(t[:-1]))
    average=.5*(x[1:]+x[:-1])
    ea=.5*add_error(x[1:],x[:-1],ex[1:],ex[:-1])+GAM*abs(average)
    terms=weights*average; errors=product_error(weights,average,ew,ea)
    value,error=reduction(terms,errors)
    return float(value),float(error)


def reduce_measurements(series,errors,rho,identity):
    shell_rows=[]; face_rows=[]
    for stride in (1,2):
        t=TIMES[::stride]
        for wi,left in enumerate((88.,104.5)):
            right=left+2*np.pi/rho
            ts,x,ex=window(t,series['shell'][::stride],errors['shell'][::stride],left,right)
            tf,f,ef=window(t,series['flux'][::stride],errors['flux'][::stride],left,right)
            require(np.array_equal(ts,tf),'Shell/flux quadrature mismatch')
            joints={}
            for face in range(3):
                for oi,observable in enumerate(OBS):
                    values=f[:,face,oi]; errs=ef[:,face,oi]
                    net,en=integral(tf,values,errs)
                    positive,ep=integral(tf,np.maximum(values,0),errs)
                    negative,em=integral(tf,np.maximum(-values,0),errs)
                    absolute=positive+negative
                    row=dict(**identity,time_window=wi,window=[left,right],sample_spacing=.1*stride,
                        face=face,radius=(40.,45.,50.)[face],observable=observable,J=net,J_error=en,
                        Jpositive=positive,Jnegative=negative,Jabsolute=absolute,
                        Jpositive_error=ep,Jnegative_error=em,
                        net_over_absolute=float(net/absolute) if absolute>0 else None,
                        positive_negative_identity=float(net-(positive-negative)))
                    face_rows.append(row); joints[face,oi]=(net,en)
            for shell in range(2):
                for oi,observable in enumerate(OBS):
                    before=float(x[0,shell,oi]); after=float(x[-1,shell,oi])
                    change=after-before
                    ec=float(add_error(after,before,float(ex[-1,shell,oi]),float(ex[0,shell,oi])))
                    inner,ei=joints[shell,oi]; outer,eo=joints[shell+1,oi]
                    balance=change+outer-inner
                    eb=ec+eo+ei+GAM*(abs(change)+abs(outer)+abs(inner))
                    shell_rows.append(dict(**identity,time_window=wi,window=[left,right],sample_spacing=.1*stride,
                        shell=shell,radius_window=((40.,45.),(45.,50.))[shell],observable=observable,
                        initial_storage=before,final_storage=after,storage_change=change,storage_change_error=ec,
                        inner_transfer=inner,outer_transfer=outer,balance=balance,balance_error=float(eb)))
    return shell_rows,face_rows


def pair_series(plus,minus,baseline):
    values={}; errors={}
    for key in ('shell','flux'):
        p,ep=plus[0][key],plus[1][key]; m,em=minus[0][key],minus[1][key]
        b,eb=baseline[0][key],baseline[1][key]
        mean=.5*(p+m)
        e_mean=.5*add_error(p,m,ep,em)+GAM*abs(mean)
        values[key]=mean-b; errors[key]=add_error(mean,b,e_mean,eb)
    return values,errors


def classify(result):
    faces=result['pair_faces']; shells=result['pair_shells']
    reserves=[]; decisions=[]
    for angle in (0,90):
        for epsilon in (.001,.002):
            for wi in (0,1):
                for observable in OBS:
                    fs=[x for x in faces if x['phase_degrees']==angle and x['epsilon']==epsilon
                        and x['time_window']==wi and x['observable']==observable]
                    ss=[x for x in shells if x['phase_degrees']==angle and x['epsilon']==epsilon
                        and x['time_window']==wi and x['observable']==observable]
                    per_face={}
                    for face in range(3):
                        indexed={(x['dt'],x['sample_spacing']):x for x in fs if x['face']==face}
                        require(len(indexed)==4,'Missing face discretization')
                        fine=indexed[.005,.1]
                        delta_dt=abs(fine['J']-indexed[.01,.1]['J'])
                        delta_sample=max(abs(indexed[d,.1]['J']-indexed[d,.2]['J']) for d in (.01,.005))
                        adjacent=[x for x in ss if x['shell'] in (face-1,face)]
                        require(len(adjacent)==(8 if face==1 else 4),'Missing adjacent balances')
                        balance=max(abs(x['balance']) for x in adjacent)
                        eta=max([x['J_error'] for x in indexed.values()]+[x['balance_error'] for x in adjacent])
                        reserve=float(max(delta_dt,delta_sample)+balance+eta)
                        require(all(np.isfinite(x) for x in (reserve,fine['J'],eta,balance,delta_dt,delta_sample)),
                                'Nonfinite classification inputs')
                        outward=bool(reserve>0 and fine['J']>10*reserve)
                        inward=bool(reserve>0 and fine['J']<-10*reserve)
                        row=dict(phase_degrees=angle,epsilon=epsilon,time_window=wi,observable=observable,
                            face=face,radius=fine['radius'],primary_dt=.005,primary_sample_spacing=.1,
                            J=fine['J'],delta_dt=float(delta_dt),delta_sampling=float(delta_sample),
                            max_adjacent_balance=float(balance),eta=float(eta),u=reserve,
                            outward=outward,inward=inward,
                            status='NETTO_AUSWAERTS_AUFGELOEST' if outward else 'NETTO_EINWAERTS_AUFGELOEST' if inward else 'UNRESOLVED')
                        reserves.append(row); per_face[face]=row
                    for shell in range(2):
                        left,right=per_face[shell],per_face[shell+1]
                        outward=left['outward'] and right['outward']; inward=left['inward'] and right['inward']
                        decisions.append(dict(phase_degrees=angle,epsilon=epsilon,time_window=wi,
                            observable=observable,shell=shell,
                            status='NETTO_AUSWAERTS_AUFGELOEST' if outward else 'NETTO_EINWAERTS_AUFGELOEST' if inward else 'UNRESOLVED',
                            inner_J=left['J'],outer_J=right['J'],inner_reserve=left['u'],outer_reserve=right['u']))
    require(len(reserves)==72 and len(decisions)==48,'Classification completeness failed')
    return reserves,decisions


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('dynamics','time-code','phase-code','amplitude-code','time-dir','phase-dir','amplitude-dir','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=False)
    result=dict(status='INCOMPLETE',complete=False,code_sha256=sha(__file__),bound_hashes=HASH,
        budget=dict(total_cpu_target=10,checkpoint_cpu_seconds=8),
        gates=dict(transport_reserve_factor=10,qa=1e-10,local_gamma=GAM),
        interpretation='Finite local transport of pair-minus-baseline observables; no irreversibility, lifetime or alpha4 assumption',
        reserve_limit='Local evaluation sensitivity only; no rigorous accumulated evolution, common-mode balance or sampling error bound',
        qa=[],arms=[],raw_shells=[],raw_faces=[],pair_shells=[],pair_faces=[],face_reserves=[],decisions=[])
    save(args.out,result)
    try:
        dyn=module(args.dynamics,HASH['dynamics'],'unchanged_dynamics_for_algebraic_QA')
        for key in ('time_code','phase_code','amplitude_code'):
            checked(getattr(args,key),HASH[key])
        checkpoint(); result['qa']=analytic_qa(dyn); save(args.out,result)
        requests,phase,identity=load_manifests(args)
        result['common_input']=identity; result['phase']=phase
        fullr=(np.arange(2400)+.5)*H
        r=fullr[(fullr>=40-2*H)&(fullr<=50+2*H)]
        reduced={}
        for request in requests:
            checkpoint(); values,errors=read_arm(args,request,r,phase['omega'])
            key=(request['dt'],request['phase_degrees'],request['epsilon'])
            require(key not in reduced,'Duplicate physical arm'); reduced[key]=(values,errors)
            identity=dict(dt=request['dt'],phase_degrees=request['phase_degrees'],epsilon=request['epsilon'])
            shell_rows,face_rows=reduce_measurements(values,errors,phase['rho'],identity)
            result['raw_shells'].extend(shell_rows); result['raw_faces'].extend(face_rows)
            result['arms'].append(dict(**request,complete=True)); save(args.out,result)
        for dt in (.01,.005):
            baseline=reduced[dt,0,0.]
            for angle in (0,90):
                for eps in (.001,.002):
                    checkpoint(); values,errors=pair_series(reduced[dt,angle,eps],reduced[dt,angle,-eps],baseline)
                    identity=dict(dt=dt,phase_degrees=angle,epsilon=eps)
                    shell_rows,face_rows=reduce_measurements(values,errors,phase['rho'],identity)
                    result['pair_shells'].extend(shell_rows); result['pair_faces'].extend(face_rows)
                    save(args.out,result)
        require(len(result['arms'])==18 and len(result['raw_shells'])==432 and len(result['raw_faces'])==648
            and len(result['pair_shells'])==192 and len(result['pair_faces'])==288,'Arm/measurement completeness failed')
        checkpoint(); result['face_reserves'],result['decisions']=classify(result)
        result['complete']=True; result['status']='PHYSICAL_TRANSPORT_DIAGNOSIS_COMPLETE'
    except Exception as error:
        result['status']='INCOMPLETE'; result['error']=repr(error)
    save(args.out,result)
    return 0 if result['complete'] else 2


if __name__=='__main__':
    raise SystemExit(main())
