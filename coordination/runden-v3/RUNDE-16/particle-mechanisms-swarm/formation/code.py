#!/usr/bin/env python3
"""Prospective M2 radial formation pilot. NOT executed or validated locally."""
import time
START_CPU = time.process_time()
import argparse
import hashlib
import json
import os
import resource
from pathlib import Path
import numpy as np

Q0, R, T, RC = 1100.0, 120.0, 64.0, 12.0
LEVELS = (("base", .1, .02), ("space", .05, .02), ("time", .1, .01))


def budget():
    if time.process_time() - START_CPU > 165:
        raise RuntimeError("CPU checkpoint at 165 s; INCOMPLETE")


class Grid:
    def __init__(self, h, radius=R):
        self.h = h
        self.n = int(round(radius / h))
        i = np.arange(self.n)
        self.r = (i + .5) * h
        self.area = 4 * np.pi * ((i + 1) * h)**2
        self.vol = 4 * np.pi * h * (self.r**2 + h*h/12)
        self.core = self.r < RC
        self.collar = self.r > radius - 8

    def edges(self, x, boundary):
        return np.diff(np.append(x, boundary))

    def lap(self, x, boundary):
        flux = self.area * self.edges(x, boundary) / self.h
        return (flux - np.concatenate(([0], flux[:-1]))) / self.vol

    def norm(self, x, mask=None):
        mask = np.ones(self.n, dtype=bool) if mask is None else mask
        return float(np.sqrt(np.sum(self.vol[mask] * np.abs(x[mask])**2)))


def potential(p, c):
    s = abs(p)**2
    return .25*(c*c-1)**2 + (1+c*c)*s - s*s + .5*s**3


def forces(g, p, c):
    s = abs(p)**2
    return (g.lap(p, 0) - (1+c*c-2*s+1.5*s*s)*p,
            g.lap(c, 1) - c*(c*c-1+2*s))


def advance(g, state, dt):
    p, v, c, w = state
    a, b = forces(g, p, c)
    vh, wh = v+.5*dt*a, w+.5*dt*b
    pn, cn = p+dt*vh, c+dt*wh
    an, bn = forces(g, pn, cn)
    return pn, vh+.5*dt*an, cn, wh+.5*dt*bn


def charge(g, p, v, mask=None):
    mask = np.ones(g.n, dtype=bool) if mask is None else mask
    return float(2*np.sum(g.vol[mask]*np.imag(np.conj(p[mask])*v[mask])))


def energy(g, state):
    p, v, c, w = state
    return float(np.sum(g.vol*(abs(v)**2+.5*w*w+potential(p,c)))
                 + np.sum(g.area*(abs(g.edges(p,0))**2
                                    + .5*g.edges(c,1)**2))/g.h)


def outward_flux(g, p):
    k = int(round(RC/g.h))-1
    return float(-2*g.area[k]*np.imag(np.conj(p[k])*p[k+1])/g.h)


def diagnose(g, state, initial):
    p,v,c,w = state
    mask = g.core
    nphi = max(g.norm(p,mask), 1e-14)
    nchi = max(g.norm(c-1,mask), 1e-14)
    icore = nphi*nphi
    qc = charge(g,p,v,mask)
    omega = qc/(2*icore)
    ap,ac = forces(g,p,c)
    # Raw dimensional residual divided by vacuum m^2=2 times field norm.
    rp = g.norm(ap+omega*omega*p,mask)/(2*nphi)
    rc = g.norm(ac,mask)/(2*nchi)
    tp = g.norm(v-1j*omega*p,mask)/(np.sqrt(2)*nphi)
    tc = g.norm(w,mask)/(np.sqrt(2)*nchi)
    p0,_,c0,_ = initial
    overlap = np.sum(g.vol*np.conj(p0)*p)
    phase = overlap/abs(overlap) if abs(overlap)>0 else 1
    driftp = g.norm(p/phase-p0)/max(g.norm(p0),1e-14)
    driftc = g.norm(c-c0)/max(g.norm(c0-1),1e-14)
    # Positive collar diagnostic; gradient edges assigned to their left cell.
    positive = g.vol*(abs(v)**2+.5*w*w+potential(p,c))
    positive += g.area*(abs(g.edges(p,0))**2+.5*g.edges(c,1)**2)/g.h
    cumulative=np.cumsum(g.vol*abs(p)**2)
    r50=float(np.interp(.5*cumulative[-1],cumulative,g.r))
    return dict(E=energy(g,state), Q=charge(g,p,v), Qcore=qc,
                omega=omega, rphi=rp, rchi=rc, tphi=tp, tchi=tc,
                driftphi=driftp, driftchi=driftc,
                chimin=float(np.min(c[mask])),
                chi0=float(c[0]),r50=r50,
                rphi_max=float(np.max(abs((ap+omega*omega*p)[mask]))),
                rchi_max=float(np.max(abs(ac[mask]))),
                collar=float(np.sum(positive[g.collar])))


def load_reference(path):
    raw = Path(path).read_bytes()
    with np.load(path, allow_pickle=False) as z:
        # BEUTEL-1 schema: r, f[profile,r], g[profile,r], Q, omega2, sweep.
        idx = np.flatnonzero((abs(z['Q']-Q0)<1e-5) & (z['sweep']=='seed') &
                            (abs(z['omega2']-1.03666310756389)<1e-10))
        if len(idx)!=1:
            raise ValueError("Expected exactly one stored Q1100 reference")
        k = int(idx[0])
        r = np.asarray(z['r'],dtype=float)
        f = np.asarray(z['f'][k],dtype=float)
        c = np.asarray(z['g'][k],dtype=float)
        om = float(np.sqrt(z['omega2'][k]))
        meta = dict(path=str(path), sha256=hashlib.sha256(raw).hexdigest(),
                    row=k, original_dtype=str(z['f'].dtype),
                    sampled_dr=float(r[1]-r[0]), stored_omega=om,
                    stored_Q=float(z['Q'][k]), interpolation="linear; constant left; vacuum right")
    if not (np.all(np.isfinite(r)) and np.all(np.diff(r)>0)
            and np.all(np.isfinite(f)) and np.all(np.isfinite(c))):
        raise ValueError("Invalid reference data")
    return r,f,c,om,meta


def prepare(g, kind, reference):
    if kind == "cloud":
        p = np.exp(-g.r*g.r/(2*8**2)).astype(complex)
        om = np.sqrt(2)
        p *= np.sqrt(Q0/(2*om*np.sum(g.vol*abs(p)**2)))
        c = np.ones(g.n)
        metadata = dict(omega=om, Q_normalized=True)
    else:
        r,f,cold,stored_om,_ = reference
        p = np.interp(g.r,r,f,left=f[0],right=0).astype(complex)
        c = np.interp(g.r,r,cold,left=cold[0],right=1)
        # No amplitude/profile relaxation. Small Q repair via phase speed only.
        om = Q0/(2*np.sum(g.vol*abs(p)**2))
        metadata = dict(omega=om, original_omega=stored_om,
                        omega_correction=om-stored_om, Q_normalized=True)
    return (p,1j*om*p,c,np.zeros(g.n)),metadata


def qa():
    """Three deterministic checks, intended only for authorized remote execution."""
    g=Grid(.1,4)
    # 1: discrete energy variation checks both gradient and local factors.
    p=(.15+.05j)*np.exp(-g.r*g.r)
    c=1-.1*np.exp(-g.r*g.r)
    dp=(.2-.07j)*np.exp(-.7*g.r*g.r)
    dc=.13*np.exp(-.9*g.r*g.r)
    a,b=forces(g,p,c)
    analytic=-2*np.real(np.sum(g.vol*np.conj(a)*dp))-np.sum(g.vol*b*dc)
    eps=1e-5
    zero=np.zeros(g.n)
    ep=energy(g,(p+eps*dp,zero,c+eps*dc,zero))
    em=energy(g,(p-eps*dp,zero,c-eps*dc,zero))
    variation=abs((ep-em)/(2*eps)-analytic)/max(1,abs(analytic))
    assert variation<1e-7, ("energy variation",variation)
    # 2: instantaneous Noether identity. No time integration in QA.
    g=Grid(.1,16)
    p=(.2+.1j)*np.exp(-g.r*g.r/100+1j*.03*g.r*g.r)
    c=1-.1*np.exp(-g.r*g.r/50)
    state=(p,1j*1.2*p,c,np.zeros(g.n))
    q=charge(g,*state[:2]); qc=charge(g,*state[:2],g.core)
    a,b=forces(g,p,c)
    errq=abs(charge(g,p,a))/abs(q)
    errf=abs(charge(g,p,a,g.core)+outward_flux(g,p))/abs(q)
    assert max(errq,errf)<1e-11, ("charge/flux",errq,errf)
    # 3: exact vacuum force and energy, no integration.
    z=np.zeros(g.n); vac=(z.astype(complex),z.astype(complex),np.ones(g.n),z)
    va,vb=forces(g,vac[0],vac[2])
    assert np.all(va==0) and np.all(vb==0) and energy(g,vac)==0
    return dict(energy_variation=variation,Q_derivative_error=errq,
                flux_derivative_error=errf,vacuum_exact=True,time_steps=0)


def save(out, result):
    temp=out/'RESULT.tmp'
    temp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    temp.replace(out/'RESULT.json')


def run_arm(out, result, level, h, dt, kind, reference):
    g=Grid(h); state,meta=prepare(g,kind,reference)
    initial=tuple(x.copy() for x in state)
    arm=dict(level=level,h=h,dt=dt,kind=kind,initial=meta,samples=[],complete=False)
    result['arms'].append(arm)
    sample_every=int(round(.8/dt)); nsteps=int(round(T/dt))
    flux=0.; oldflux=outward_flux(g,state[0])
    for step in range(nsteps+1):
        if step%20==0:
            budget()
            if not all(np.all(np.isfinite(x)) for x in state):
                raise FloatingPointError("nonfinite state")
        if step%sample_every==0:
            d=diagnose(g,state,initial); d.update(t=step*dt,flux_integral=flux)
            arm['samples'].append(d)
            first=arm['samples'][0]
            d['Edrift']=abs(d['E']/first['E']-1)
            d['Qdrift']=abs(d['Q']/first['Q']-1)
            d['balance']=abs(d['Qcore']-first['Qcore']+flux)/Q0
            if max(d['Edrift'],d['Qdrift'],d['balance'])>1e-5:
                raise FloatingPointError("conservation gate")
            if d['collar']/first['E']>1e-8:
                raise FloatingPointError("collar gate")
        if step==nsteps:
            break
        state=advance(g,state,dt)
        newflux=outward_flux(g,state[0]); flux+=dt*.5*(oldflux+newflux); oldflux=newflux
    arm['complete']=True
    np.savez_compressed(out/(kind+'-'+level+'-final.npz'),r=g.r,
                        phi=state[0],pi=state[1],chi=state[2],chi_t=state[3])
    save(out,result)


def classify(result):
    arms=result['arms']
    if len(arms)!=6 or not all(a['complete'] for a in arms):
        return 'INCOMPLETE'
    # Reference control checks apply over the entire interval.
    keys=('rphi','rchi','tphi','tchi','driftphi','driftchi')
    controls=[a for a in arms if a['kind']=='reference']
    if any(s[k]>=.004 for a in controls for s in a['samples'] for k in keys):
        return 'NUMERICALLY_UNRESOLVED_REFERENCE'
    clouds={a['level']:a for a in arms if a['kind']=='cloud'}
    base=clouds['base']['samples']
    # Compare stationarity only in the terminal window: initial chi norm is zero.
    for level in ('space','time'):
        for x,y in zip(base,clouds[level]['samples']):
            if abs(x['Qcore']-y['Qcore'])/Q0>=.002:
                return 'NUMERICALLY_UNRESOLVED_SENSITIVITY'
            if x['t']>=48-1e-10 and any(abs(x[k]-y[k])>=.004
                                         for k in ('rphi','rchi','tphi','tchi')):
                return 'NUMERICALLY_UNRESOLVED_SENSITIVITY'
    passed=[]
    for a in clouds.values():
        last=[s for s in a['samples'] if s['t']>=48-1e-10]
        q=[s['Qcore']/Q0 for s in last]
        passed.append(min(q)>=.8 and max(q)-min(q)<=.01
                      and all(s[k]<.02 for s in last for k in ('rphi','rchi','tphi','tchi'))
                      and all(s['chimin']<.5 for s in last))
        passed[-1] = passed[-1] and all(s['chi0']<.2 and
                          s['r50']<=.8*a['samples'][0]['r50'] for s in last)
    return 'RADIAL_FORMATION_CANDIDATE' if all(passed) else 'NO_CANDIDATE_IN_FIXED_WINDOW'


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--reference',type=Path)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--qa-only',action='store_true')
    args=parser.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    # Includes interpreter/import CPU. Outer receipt and wallclock cap required.
    resource.setrlimit(resource.RLIMIT_CPU,(175,178))
    result=dict(status='INCOMPLETE',arms=[],model='FADEN-KERN-1 / BEUTEL-1 M2',
                code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                pid=os.getpid(),host=os.uname().nodename,execution='CPU numpy float64')
    try:
        result['qa']=qa(); budget()
        if args.reference is None:
            raise ValueError('--reference is required, also for full QA-only preflight')
        ref=load_reference(args.reference); result['reference']=ref[-1]
        result['initial_checks']=[]
        for level,h,dt in LEVELS:
            g=Grid(h)
            for kind in ('reference','cloud'):
                state,meta=prepare(g,kind,ref)
                d=diagnose(g,state,state)
                check=dict(level=level,h=h,dt=dt,kind=kind,preparation=meta,diagnostics=d)
                check['Q_pass']=abs(d['Q']/Q0-1)<1e-11
                check['reference_residual_pass']=(kind!='reference' or
                    all(d[k]<.004 for k in ('rphi','rchi','tphi','tchi')))
                result['initial_checks'].append(check)
        result['initial_gate_pass']=all(x['Q_pass'] and x['reference_residual_pass']
                                        for x in result['initial_checks'])
        if args.qa_only:
            result['status']=('QA_ONLY_COMPLETE' if result['initial_gate_pass'] else
                              'NUMERICALLY_UNRESOLVED_REFERENCE_INITIAL')
        else:
            if not result['initial_gate_pass']:
                raise ValueError('Reference initial gate failed; no time integration')
            for level,h,dt in LEVELS:
                for kind in ('reference','cloud'):
                    run_arm(args.out,result,level,h,dt,kind,ref)
            result['status']=classify(result)
    except Exception as exc:
        result['error']=repr(exc)
        result['status']='INCOMPLETE' if isinstance(exc,RuntimeError) else 'NUMERICALLY_UNRESOLVED'
    result['cpu_seconds']=time.process_time()-START_CPU
    result['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    save(args.out,result)
    return 0 if result['status'] in ('QA_ONLY_COMPLETE','RADIAL_FORMATION_CANDIDATE',
                                    'NO_CANDIDATE_IN_FIXED_WINDOW') else 2


if __name__=='__main__':
    raise SystemExit(main())
