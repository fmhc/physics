#!/usr/bin/env python3
"""Posthoc saved Ritz-vector tail diagnostics. Never calls an eigensolver."""
import argparse
import csv
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import numpy as np

RESULT_HASH='77ecf9bbe03b96db901d76728e074a897725eb52213f90dae76c7200ba5364ea'
CODE_HASH='467ad3e19cd8efcdac4ec2dcc670b50aaa59cc6f7e9e44d625ebbf94ba0d32c6'
MANIFEST_HASH='8c33ace3a5465a8fd481d26b35457425ee3c5d5f0111b3f11c09f4a9dd72fdf4'
GRIDS=((120.,.1),(120.,.05),(60.,.1),(60.,.05))
CHANNELS=('plus','minus','chi')
RADII=(5,10,15,20,25,30,40,50)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def window(r,amplitude,kappa,lo,hi,shared_peak):
    peak=float(np.max(amplitude)); floor=1e-10*max(peak,shared_peak)
    inwindow=(r[:-1]>=lo)&(r[1:]<=hi)
    valid=inwindow&(amplitude[:-1]>floor)&(amplitude[1:]>floor)
    count=int(np.sum(valid)); total=int(np.sum(inwindow))
    row=dict(window=[lo,hi],peak=peak,shared_peak=shared_peak,floor=floor,total_pairs=total,
             valid_pairs=count,unresolved_pairs=total-count,status='RESOLVED' if count else 'UNRESOLVED')
    if not count: return row
    local=-np.log(amplitude[1:][valid]/amplitude[:-1][valid])/np.diff(r)[valid]
    ratio=local/kappa
    row.update(r_mid=((r[:-1]+r[1:])*.5)[valid].tolist(),local_kappa=local.tolist(),
        ratio_min=float(np.min(ratio)),ratio_median=float(np.median(ratio)),ratio_max=float(np.max(ratio)),
        median_abs_theory_error=float(np.median(abs(local-kappa))),
        median_abs_wrong_double_kappa_error=float(np.median(abs(local-2*kappa))))
    return row


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input-dir',type=Path,required=True)
    parser.add_argument('--manifest',type=Path,required=True)
    parser.add_argument('--operator',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--plot',action='store_true')
    args=parser.parse_args()
    resultpath=args.input_dir/'RESULT.json'
    if sha(resultpath)!=RESULT_HASH or sha(args.manifest)!=MANIFEST_HASH or sha(args.operator)!=CODE_HASH:
        raise ValueError('Input hash mismatch')
    original=json.loads(resultpath.read_text()); manifest=json.loads(args.manifest.read_text())
    if original['code_sha256']!=CODE_HASH or original['reference']['manifest_sha256']!=MANIFEST_HASH:
        raise ValueError('Result provenance mismatch')
    omega_by_h={float(p['h']):float(p['omega']) for p in manifest['profiles']}
    spec=importlib.util.spec_from_file_location('saved_mode_operator',args.operator)
    operator=importlib.util.module_from_spec(spec); spec.loader.exec_module(operator)
    rows=[]; stored={}
    for radius,h in GRIDS:
        tasks=[t for t in original['tasks'] if t['R']==radius and t['h']==h and t['shift']==.3]
        if len(tasks)!=1 or not tasks[0]['complete']: raise ValueError('Missing unique completed task')
        task=tasks[0]; file=args.input_dir/task['artifact']
        if sha(file)!=task['artifact_sha256']: raise ValueError('Ritz artifact hash mismatch')
        with np.load(file,allow_pickle=False) as z:
            values=z['eigenvalues']; vectors=z['eigenvectors']
            ix=np.flatnonzero((values.imag>.38)&(values.imag<.39))
            if len(ix)!=1: raise ValueError('Expected one fixed-window Ritz value')
            j=int(ix[0]); value=values[j]
            if abs(value.imag-task['ritz'][j]['rho'])>1e-12 or abs(value.real-task['ritz'][j]['lambda_real'])>1e-12:
                raise ValueError('JSON/NPZ ordering mismatch')
            vector=vectors[:,j].copy()
        g=operator.grid(radius,h); n=g['n']
        if len(vector)!=6*n or not np.all(np.isfinite(vector)): raise ValueError('Vector shape/finite failure')
        q=vector[:3*n]; norm=float(np.linalg.norm(q))
        if norm<=0: raise ValueError('Zero mode')
        q=q/norm; u,v,w=q.reshape(3,n)/g['root']; v=1j*v
        channels=np.array([(u+v)/np.sqrt(2),(u-v)/np.sqrt(2),w])
        rho=float(value.imag); omega=omega_by_h[h]
        squares=np.array([2-(omega+rho)**2,2-(omega-rho)**2,2-rho*rho])
        if np.any(squares<=0): raise ValueError('Fixed Ritz value not below all thresholds')
        kappas=np.sqrt(squares); amplitudes=abs(channels*g['r'])
        density=np.sum(abs(q.reshape(3,n))**2,axis=0)
        row=dict(R=radius,h=h,rho=rho,omega=omega,source=file.name,source_sha256=task['artifact_sha256'],
            original_qnorm=norm,qnorm=float(np.linalg.norm(q)),channels={},
            tail_radii=list(RADII),tail_fractions=[float(np.sum(density[g['r']>r])) for r in RADII])
        for k,name in enumerate(CHANNELS):
            row['channels'][name]=dict(kappa_theory=float(kappas[k]),
                windows=[window(g['r'],amplitudes[k],float(kappas[k]),lo,hi,float(np.max(amplitudes)))
                         for lo,hi in ((20,30),(30,40))])
        rows.append(row); stored[(radius,h)]=(g,q,channels,amplitudes,kappas)
    overlaps=[]
    for left,right in itertools.combinations(GRIDS,2):
        lg,lq,*_=stored[left]; rg,rq,*_=stored[right]
        ov,ln,rn=operator.overlap(lq,lg,rq,rg)
        overlaps.append(dict(left=list(left),right=list(right),overlap=ov,
                             left_retained_norm=ln,right_retained_norm=rn))
    result=dict(original_status=original['status'],original_matches=original.get('matches'),
        interpretation='Posthoc raw Ritz tail diagnosis only; no gate reclassification',
        input_sha256=RESULT_HASH,operator_sha256=CODE_HASH,manifest_sha256=MANIFEST_HASH,
        analysis_sha256=sha(__file__),profiles=rows,posthoc_overlaps=overlaps)
    result['tail_caveat']=('Kappas describe homogeneous free channels. Noncompact background coupling can '
        'drive slower particular tails in fast channels. Slow plus channel is primary; mismatch is '
        'not automatically a solver error or absence of binding.')
    args.out.mkdir(parents=True,exist_ok=False)
    (args.out/'ANALYSIS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    with (args.out/'PROFILES.csv').open('w',newline='') as stream:
        writer=csv.writer(stream); writer.writerow(('R','h','r','channel','real','imag','abs_r_channel'))
        for key in GRIDS:
            g,_,channels,amplitudes,_=stored[key]
            for k,name in enumerate(CHANNELS):
                for i,r in enumerate(g['r']):
                    writer.writerow((*key,float(r),name,float(channels[k,i].real),
                                     float(channels[k,i].imag),float(amplitudes[k,i])))
    if args.plot:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig,axes=plt.subplots(3,1,figsize=(10,10),constrained_layout=True)
        g,q,ch,amp,kappa=stored[(120.,.05)]
        anchor=int(np.searchsorted(g['r'],20)); mask=(g['r']>=10)&(g['r']<=45)
        for k,name in enumerate(CHANNELS):
            line,=axes[0].semilogy(g['r'][mask],np.ma.masked_less_equal(amp[k,mask],0),label=name)
            if amp[k,anchor]>1e-10*np.max(amp):
                theory=amp[k,anchor]*np.exp(-kappa[k]*(g['r'][mask]-g['r'][anchor]))
                axes[0].semilogy(g['r'][mask],theory,'--',color=line.get_color(),label=name+' fixed theory')
        axes[0].set_ylabel('|r channel|, R120 h.05'); axes[0].legend(fontsize=8,ncol=3)
        for row in rows:
            axes[1].semilogy(RADII,row['tail_fractions'],marker='.',label=f"R{row['R']:g} h{row['h']}")
            for k,name in enumerate(CHANNELS):
                for windowrow in row['channels'][name]['windows']:
                    if windowrow['status']=='RESOLVED':
                        center=sum(windowrow['window'])/2
                        axes[2].plot(center,windowrow['ratio_median'],marker=('o','s','^')[k],
                                     linestyle='none',label=f"R{row['R']:g} h{row['h']} {name} {center:g}")
        axes[1].set_ylabel('Canonical norm fraction beyond r'); axes[1].legend(fontsize=8)
        axes[2].axhline(1,color='black',ls='--',label='theory ratio 1')
        axes[2].axhline(2,color='gray',ls=':',label='deliberately wrong ratio 2')
        axes[2].set_ylabel('Median local kappa / fixed theory'); axes[2].set_xticks([25,35])
        axes[2].legend(fontsize=5,ncol=4)
        for ax in axes: ax.set_xlabel('Model radius'); ax.grid(alpha=.2)
        fig.suptitle('Raw Ritz tail diagnosis — no gate reclassification\n'+original['status'],fontsize=12)
        fig.savefig(args.out/'TAIL.png',dpi=140); plt.close(fig)


if __name__=='__main__':
    main()
