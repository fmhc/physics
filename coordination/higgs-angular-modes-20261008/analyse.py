import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent;rows=json.loads((P/'results/RESULT.json').read_text());cc=json.loads((P/'results/COMPARISONS.json').read_text());qa=json.loads((P/'results/QA.json').read_text());assert len(rows)==36 and len(cc)==24
translations=[]
for method in ['full','E3','Ecomp']:
 rr={x['stage']:x for x in rows if x['method']==method and x['ell']==1 and x['sector']=='real'};vals={s:x['eigenvalues'][0] for s,x in rr.items()};over={s:x['translation_overlap_squared'][0] for s,x in rr.items()}
 passed=min(over.values())>.95 and abs(vals['grid'])<=.4*abs(vals['base'])+1e-6 and abs(vals['box']-vals['base'])<=max(.1*abs(vals['base']),1e-6)
 translations.append(dict(method=method,eigenvalues=vals,overlap_squared=over,passed=passed))
groups=[]
for method in ['E3','Ecomp']:
 rr=[x for x in cc if x['method']==method];mx=max(v for x in rr for v in x['relative_errors']);drift=max(abs(v-next(y['relative_errors'][i] for y in rr if y['stage']=='base' and (y['ell'],y['sector'])==(x['ell'],x['sector']))) for x in rr for i,v in enumerate(x['relative_errors']))
 pos=all(min(x['eigenvalues'][1:] if x['ell']==1 and x['sector']=='real' else x['eigenvalues'])>1e-6 for x in rows if x['method'] in ['full',method]);transok=all(x['passed'] for x in translations if x['method'] in ['full',method])
 groups.append(dict(method=method,maximum_relative_error=mx,drift=drift,nontrivial_positive=pos,translation_passed=transok,minimum_overlap_squared=min(v for x in rr for v in x['overlap_squared']),verdict='bestanden' if pos and transok and mx+drift<=.05 and drift<=.005 else 'unentschieden'))
s=dict(groups=groups,translations=translations,max_radial_hvp_error=max(x.get('radial_jet_hvp_error',0) for x in qa),max_angular_fd_error=max(v[-1] for x in qa for k,v in x.items() if k.startswith('angular_fd')),max_quadrature_error=max(x['quadrature_error'] for x in qa),max_inverse_solve_error=max(x['inverse_solve_error'] for x in qa),max_raw_asymmetry=max(x['raw_asymmetry'] for x in rows),max_eigen_residual=max(x['eigen_residual'] for x in rows),max_orthogonality=max(x['orthogonality'] for x in rows))
(P/'SUMMARY.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
plt.rcParams.update({'svg.fonttype':'none','font.size':11})
fig,axs=plt.subplots(1,2,figsize=(11.5,4.5),layout='constrained');cats=[(1,'real'),(1,'imag'),(2,'real'),(2,'imag')]
for j,(method,col) in enumerate([('E3','#c17827'),('Ecomp','#18826b')]):
 vals=[100*max(v for x in cc if x['method']==method and (x['ell'],x['sector'])==key for v in x['relative_errors']) for key in cats]
 axs[0].plot(range(4),vals,'o-',label=method,color=col)
axs[0].set_yscale('log');axs[0].set_xticks(range(4),['l=1\nAmplitude','l=1\nPhase','l=2\nAmplitude','l=2\nPhase']);axs[0].set_ylabel('Maximaler Eigenwertfehler [%]');axs[0].set_title('Nichttriviale Energiekrümmungen');axs[0].legend()
for tr,col in zip(translations,['#397ba8','#c17827','#18826b']):axs[1].plot(range(3),[abs(tr['eigenvalues'][s]) for s in ['base','grid','box']],'o-',label=tr['method'],color=col)
axs[1].set_yscale('log');axs[1].set_xticks(range(3),['Basis','feiner','größere Box']);axs[1].set_ylabel('|λ der Translation|');axs[1].set_title('Verschiebung als Symmetriekontrolle');axs[1].legend()
for ax in axs:ax.grid(alpha=.2)
fig.suptitle('Reduzierte Higgsmodelle · nicht-kugelsymmetrische Störungen')
fig.supxlabel('Statische Higgs-Mitreaktion · drei Gitter · ein Parameterpunkt · keine Zeitfrequenzen',fontsize=10)
fig.savefig(P/'angular-mode-errors.svg',metadata={'Date':None});p=P/'angular-mode-errors.svg';p.write_text('\n'.join(l.rstrip() for l in p.read_text().splitlines())+'\n')
