#!/usr/bin/env python3
"""Synthetic checks of classify only. No PDE or time integration."""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

EXPECTED='0ce21bee477cb41ade234611fd832abc5a7a90ed10d83d526f532cf28c6fd899'


def baseline():
    arms=[]
    for level in ('base','space','time'):
        for kind in ('reference','cloud'):
            samples=[]
            for i in range(81):
                samples.append(dict(t=.8*i,Q=1100.,omega=1.02,Qcore=.85*1100,
                    rphi=.001,rchi=.001,tphi=.001,tchi=.001,
                    driftphi=.001,driftchi=.001,chimin=.1,chi_first_cell=.1,
                    r50_density=10. if i==0 else 7.))
            arms.append(dict(level=level,kind=kind,complete=True,samples=samples))
    return dict(arms=arms)


def select(data,kind,level):
    return next(a for a in data['arms'] if a['kind']==kind and a['level']==level)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    source=Path(__file__).with_name('maincode.py')
    digest=hashlib.sha256(source.read_bytes()).hexdigest()
    if digest!=EXPECTED:
        raise ValueError('Classifer source hash changed; review required')
    spec=importlib.util.spec_from_file_location('m2_classifier_target',source)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Import only: target's guarded main, qa, advance, run_arm are never called.
    cases=[]
    data=baseline()
    cases.append(('all_gates_pass',data,'RADIAL_FORMATION_CANDIDATE'))
    data=baseline()
    for arm in data['arms']:
        if arm['kind']=='cloud':
            for i,s in enumerate(arm['samples']):
                s['tphi']=s['tchi']=.01 if i%2==0 else .03
    cases.append(('compact_pulsating_same_Q_omega',data,'NO_CANDIDATE_IN_FIXED_WINDOW'))
    data=baseline()
    select(data,'reference','space')['samples'][70]['rchi']=.005
    cases.append(('one_bad_reference',data,'NUMERICALLY_UNRESOLVED_REFERENCE'))
    data=baseline()
    select(data,'cloud','time')['complete']=False
    cases.append(('one_incomplete_numerical_arm',data,'INCOMPLETE'))
    data=baseline()
    select(data,'cloud','space')['samples'][70]['Qcore']+=.003*1100
    cases.append(('one_bad_grid_sensitivity',data,'NUMERICALLY_UNRESOLVED_SENSITIVITY'))
    data=baseline()
    for s in select(data,'cloud','time')['samples'][1:]:
        s['r50_density']=8.1
    cases.append(('one_grid_fails_contraction',data,'NO_CANDIDATE_IN_FIXED_WINDOW'))
    results=[]
    for name,data,expected in cases:
        actual=module.classify(copy.deepcopy(data))
        results.append(dict(case=name,expected=expected,actual=actual,passed=actual==expected))
    structural=[]
    for name in ('missing_sample','unsynchronised_sample','duplicate_arm',
                 'empty_samples','wrong_end_time','nan_time'):
        data=baseline()
        samples=select(data,'cloud','space')['samples']
        if name=='missing_sample':
            samples.pop()
        elif name=='unsynchronised_sample':
            samples[70]['t']+=.1
        elif name=='duplicate_arm':
            data['arms'][-1]=copy.deepcopy(data['arms'][0])
        elif name=='empty_samples':
            samples.clear()
        elif name=='wrong_end_time':
            samples[-1]['t']=63.2
        elif name=='nan_time':
            samples[70]['t']=float('nan')
        try:
            actual=module.classify(data)
            rejected=actual=='NUMERICALLY_UNRESOLVED_SAMPLE_STRUCTURE'
        except Exception as exc:
            actual='EXCEPTION: '+repr(exc)
            rejected=False
        structural.append(dict(case=name,actual=actual,rejected=rejected,
                               note='Malformed input must not yield a formation candidate'))
    status=('FAIL' if not all(x['passed'] for x in results) else
            'CLASSIFIER_GAPS_FOUND' if not all(x['rejected'] for x in structural) else 'PASS')
    result=dict(status=status,
                synthetic_only=True,time_steps=0,source_sha256=digest,
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cases=results,
                structural_probes=structural)
    args.out.mkdir(parents=True,exist_ok=False)
    (args.out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    return 0 if result['status']=='PASS' else 2


if __name__=='__main__':
    raise SystemExit(main())
