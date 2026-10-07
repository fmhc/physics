import json, pathlib, hashlib, time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
start=time.process_time()
p=pathlib.Path('profile.json'); raw=p.read_bytes(); d=json.loads(raw)
r=np.asarray(d['r']); f=np.asarray(d['f']); s=f*f
assert np.all(np.diff(r)>0) and np.all(np.isfinite(s)) and s[0]>0
levels=[.05,.3,.8]
radii=[float(np.interp(q*s[0],s[::-1],r[::-1])) for q in levels]
extent=max(8,1.2*radii[0])
x=np.linspace(-extent,extent,321); X,Z=np.meshgrid(x,x)
S=np.interp(np.hypot(X,Z),r,s)/s[0]
fig=plt.figure(figsize=(15,5),layout='constrained')
ax=fig.add_subplot(131,projection='3d')
u=np.linspace(0,2*np.pi,70); v=np.linspace(0,np.pi,36)
for rad,col,alpha in zip(radii,['#60c3c0','#eeab64','#d86248'],[.12,.20,.7]):
    ax.plot_surface(rad*np.outer(np.cos(u),np.sin(v)),rad*np.outer(np.sin(u),np.sin(v)),rad*np.outer(np.ones_like(u),np.cos(v)),color=col,alpha=alpha,linewidth=0,shade=True)
ax.set(xlabel='x',ylabel='y',zlabel='z',title='Kugelflaechen gleicher Felddichte\n5 %, 30 %, 80 % des Zentralwerts')
ax.set_box_aspect((1,1,1))
ax=fig.add_subplot(132)
im=ax.imshow(S,origin='lower',extent=[-extent,extent,-extent,extent],cmap='magma',vmin=0,vmax=1)
ax.set(xlabel='x',ylabel='z',title='Schnitt durch die Mitte: |psi|² / |psi(0)|²')
fig.colorbar(im,ax=ax,shrink=.8)
ax=fig.add_subplot(133)
ax.plot(r,s/s[0],label='normierte Felddichte',color='#278b8b')
for rad,q in zip(radii,levels): ax.plot(rad,q,'o',color='#bd663b')
ax.set(xlim=(0,extent),ylim=(0,1.03),xlabel='Radius r [Modelleinheiten]',ylabel='relative Felddichte',title='Gespeichertes Hintergrundprofil')
ax.grid(alpha=.2)
fig.suptitle('Unser radialer Q-Ball beim BIC-Kandidaten: omega² = %.9f\nRekonstruktion aus gespeichertem f(r); keine neue Simulation, keine Viererstruktur'%d['omega2'],fontsize=12)
fig.savefig('GEOMETRIE.png',dpi=150)
fig.savefig('GEOMETRIE.svg')
pathlib.Path('RENDER.json').write_text(json.dumps({'source_sha256':hashlib.sha256(raw).hexdigest(),'omega2':d['omega2'],'f0':float(f[0]),'density_fraction_radii':dict(zip(map(str,levels),radii)),'monotone_density':bool(np.all(np.diff(s)<=1e-12)),'operation':'render existing radial profile; no PDE solve','host':'ts440 CPU','cpu_seconds':time.process_time()-start},indent=2))
