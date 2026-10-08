from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
read=lambda n:json.loads((P/'results'/n).read_text())
rows=read('RESULT.json');qa=read('QA.json');comp=read('COMPARISONS.json');status=read('STATUS.json')
assert status['complete'] and len(rows)==63 and len(qa)==63 and len(comp)==54
names=['Schur-static','Schur-inertia','E3-static','E3-inertia','Ecomp-static','Ecomp-inertia']
stages=['base','grid','box'];trans={}
for name in ['full']+names:
 rec={r['stage']:r for r in rows if r['method']==name and r['ell']==1}
 ratio=abs(rec['grid']['eigenvalues'][0]/rec['base']['eigenvalues'][0]);over=min(r['translation_overlap_squared'][0] for r in rec.values());mx=max(abs(r['eigenvalues'][0]) for r in rec.values())
 trans[name]=dict(squared_frequencies={s:rec[s]['eigenvalues'][0] for s in stages},grid_ratio=ratio,min_matter_overlap_squared=over,passed=bool(over>.99 and mx<1e-3 and ratio<.4))
assert all(v['passed'] for v in trans.values()),trans
summary={}
for name in names:
 cr=[r for r in comp if r['method']==name];perstage={s:max(max(r['relative_frequency_errors']) for r in cr if r['stage']==s) for s in stages}
 maxerr=max(perstage.values());drift=max(max(next(r for r in cr if r['stage']==s and r['ell']==L)['relative_frequency_errors'][i] for s in stages)-min(next(r for r in cr if r['stage']==s and r['ell']==L)['relative_frequency_errors'][i] for s in stages) for L in [0,1,2] for i in range(8))
 negative=sum(r['negative_count'] for r in rows if r['method']==name)
 summary[name]=dict(max_frequency_error_percent=100*maxerr,drift_percentage_points=100*drift,per_stage_max_percent={s:100*v for s,v in perstage.items()},min_matter_overlap_squared=min(min(r['matter_overlap_squared']) for r in cr),negative_modes=negative,passed=bool(maxerr<=.05 and drift<=.005 and negative==0))
for kind in ['Schur','E3','Ecomp']:
 summary[kind+'-inertia']['improves_maximum_error']=summary[kind+'-inertia']['max_frequency_error_percent']<summary[kind+'-static']['max_frequency_error_percent']
checks=dict(max_original_equation_residual=max(max(q['original_equations_residuals'],default=0) for q in qa),max_schur_frequency_residual=max(max([x for x in q['frequency_schur_residuals'] if x is not None],default=0) for q in qa),frequency_schur_pole_skips=sum(sum(x is None for x in q['frequency_schur_residuals']) for q in qa),max_linear_charge_residual=max(max(q['linear_charge_residuals'],default=0) for q in qa),max_eigen_residual=max(q['eigen_residual'] for q in qa),max_orthogonality=max(q['orthogonality'] for q in qa),max_phase_ward=max(q.get('phase_ward_residual',0) for q in qa),max_tangent_jvp_error=max(q.get('tangent_jvp_error',0) for q in qa),max_radial_hvp_error=max(q.get('radial_hvp_error',0) for q in qa),min_mass_eigenvalue=min(q['mass_minimum'] for q in qa),min_higgs_block_eigenvalue=min(q.get('higgs_minimum',math.inf) for q in qa),max_ritz_violation=max(max(q['ritz_violation_full_inertia'],q['ritz_violation_inertia_static']) for q in comp))
result=dict(complete=True,comparisons=summary,translation=trans,qa=checks,negative_modes_full=sum(r['negative_count'] for r in rows if r['method']=='full'),elapsed_seconds=status['elapsed_seconds'],gpu_peak_allocated_bytes=status['gpu_peak_allocated_bytes'],all_comparison_gates_passed=all(x['passed'] for x in summary.values()),scope='Linear fixed-charge perturbations l=0,1,2; one parameter point, three finite grids; not nonlinear time evolution or quantum stability')
(P/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
colors=['#137c8b','#d17b12','#7754a6'];labels=['Basis','feines Gitter','größere Box']
for j,s in enumerate(stages):
 axes[0].scatter([i+(j-1)*.16 for i in range(6)],[summary[n]['per_stage_max_percent'][s] for n in names],color=colors[j],label=labels[j],s=45)
axes[0].set_yscale('log');axes[0].set_xticks(range(6),['Schur\nstatisch','Schur\n+ Trägheit','E3\nstatisch','E3\n+ Trägheit','Ecomp\nstatisch','Ecomp\n+ Trägheit']);axes[0].set_ylabel('Maximaler relativer Frequenzfehler [%]');axes[0].set_title('Dynamische Frequenzen gegen volle Theorie');axes[0].grid(axis='y',alpha=.22);axes[0].legend(fontsize=8)
for name,col in [('full','#263b53'),('E3-inertia','#d17b12'),('Ecomp-inertia','#137c8b')]:
 axes[1].plot(range(3),[trans[name]['squared_frequencies'][s] for s in stages],'o-',label=name,color=col)
axes[1].set_yscale('log');axes[1].set_xticks(range(3),labels);axes[1].set_ylabel('ν² der diskreten Translationsrichtung');axes[1].set_title('Translation: Gitterrest sinkt mit h²');axes[1].grid(axis='y',alpha=.22);axes[1].legend(fontsize=8)
fig.suptitle('Higgsdynamik: 63 Spektralprobleme, l = 0, 1, 2',fontweight='bold')
fig.savefig(P/'dynamic-frequency-errors.svg');fig.savefig(P/'preview.png',dpi=130);plt.close(fig)
print(json.dumps({k:v for k,v in result.items() if k!='translation'},indent=2))
