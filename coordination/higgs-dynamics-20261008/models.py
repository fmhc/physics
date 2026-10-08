# Response and angular quadratic-energy functions from HIGGS-ANGULAR-MODES-1.
import torch,math

def make(r,h,lap):
 n=len(r);dev=r.device;dt=r.dtype;pi=math.pi;a=125**2/(2*246**2*.01);y0=.492;b=.5;eta=.05;Q=600.
 invs={}
 for L in [0,1,2]:
  K=lap+torch.diag(6.25+L*(L+1)/r**2)
  invs[L]=torch.cholesky_inverse(torch.linalg.cholesky(K))
 def inv(q,L):return invs[L]@q
 def response(S):
  z1=-inv(b*y0*r*S,0);z2=-inv(b*S*z1+3*a*y0*z1*z1/r,0);return z1,z2
 def radial_energy(u,method):
  rho=(u/r)**2;S=rho.sum(0);I=4*pi*h*u.square().sum();z1,z2=response(S)
  kin=4*pi/h*torch.nn.functional.pad(u,(1,1)).diff(dim=-1).square().sum()
  pot=(rho-rho*rho+.5*rho**3).sum(0)-.5*rho[0]*rho[1]-2*eta*u[0]*u[1]/r**2
  if method=='E3':EH=4*pi*h*(.5*b*y0*r*S*z1+b/2*S*z1*z1+a*y0*z1**3/r).sum()
  else:
   z=z1+z2;D=(y0+z/r)**2-y0*y0;EH=4*pi*h*(.5*torch.nn.functional.pad(z,(1,1)).diff().square().sum()/h**2+(r*r*(a/4*D*D+b/2*D*S)).sum())
  return (Q**2/(4*I)+kin+4*pi*h*(r*r*pot).sum()+EH)/(8*pi*h)
 def jet(d,u,method,L,sector):
  rho=(u/r)**2;S=rho.sum(0);omega=Q/(8*pi*h*u.square().sum());s2=(d/r).square().sum(0)
  rho1=2*u*d/r**2 if sector=='real' else torch.zeros_like(u);s1=rho1.sum(0);rho2=(d/r)**2
  z10,z20=response(S);z11=-inv(b*y0*r*s1,L);z12=-inv(b*y0*r*s2,0)
  z21=-inv(b*(S*z11+s1*z10)+6*a*y0*z10*z11/r,L)
  z22=-inv(b*(S*z12+s1*z11+s2*z10)+3*a*y0*(2*z10*z12+z11*z11)/r,0)
  kin=4*pi/h*torch.nn.functional.pad(d,(1,1)).diff(dim=-1).square().sum()+4*pi*h*(L*(L+1)*d.square()/r**2).sum()
  vp=((1-2*rho+1.5*rho*rho)*rho2+(-1+1.5*rho)*rho1.square()).sum(0)-.5*(rho[0]*rho2[1]+rho[1]*rho2[0]+rho1[0]*rho1[1])-2*eta*d[0]*d[1]/r**2
  charge=-4*pi*h*omega**2*d.square().sum()
  if L==0 and sector=='real':charge=charge+4*pi*h*4*omega**2*(u*d).sum()**2/u.square().sum()
  if method=='E3':
   eh2=4*pi*h*(.5*b*y0*r*(S*z12+s1*z11+s2*z10)+b/2*(S*(2*z10*z12+z11*z11)+2*s1*z10*z11+s2*z10*z10)+a*y0*(3*z10*z10*z12+3*z10*z11*z11)/r).sum()
  else:
   z0=z10+z20;z1=z11+z21;z2=z12+z22;yy=y0+z0/r;d0=yy*yy-y0*y0;d1=2*yy*z1/r;d2=(z1/r)**2+2*yy*z2/r
   diff=lambda x:torch.nn.functional.pad(x,(1,1)).diff()
   eh2=4*pi*h*(.5*(2*diff(z0)*diff(z2)+diff(z1)**2).sum()/h**2+.5*(L*(L+1)*z1*z1/r**2).sum()+(r*r*(a/4*(d1*d1+2*d0*d2)+b/2*(d0*s2+d1*s1+d2*S))).sum())
  return (charge+kin+4*pi*h*(r*r*vp).sum()+eh2)/(8*pi*h)

 def dense(fun):
  x=torch.zeros(2*n,device=dev,dtype=dt,requires_grad=True)
  grad=torch.autograd.grad(fun(x),x,create_graph=True)[0]
  H=torch.empty((2*n,2*n),device=dev,dtype=dt)
  for j in range(0,2*n,32):
   count=min(32,2*n-j);basis=torch.zeros((count,2*n),device=dev,dtype=dt)
   basis[torch.arange(count,device=dev),torch.arange(j,j+count,device=dev)]=1
   H[j:j+count]=torch.autograd.grad(grad,x,grad_outputs=basis,is_grads_batched=True,retain_graph=True)[0].detach()
  return H
 def reduced(u,method,L):
  A=dense(lambda v:jet(v.reshape(2,n),u,method,L,'real'))
  D=dense(lambda v:jet(v.reshape(2,n),u,method,L,'imag'))
  omega=Q/(8*pi*h*u.square().sum())
  if L==0:A-=4*omega**2*torch.outer(u.flatten(),u.flatten())/u.square().sum()
  S=(u/r).square().sum(0);z1,z2=response(S)
  F=torch.cat([torch.diag(2*u[i]/r) for i in range(2)],dim=1)
  Z1=-b*y0*inv(F,L)
  Z2=-inv((b*S+6*a*y0*z1/r)[:,None]*Z1+b*(z1/r)[:,None]*F,L)
  J1,J2=Z1/math.sqrt(2),Z2/math.sqrt(2)
  M=torch.eye(2*n,device=dev,dtype=dt)+J1.T@J1+J1.T@J2+J2.T@J1
  if method=='Ecomp':M+=J2.T@J2
  direction=torch.stack([r*torch.exp(-r*r/16)*torch.sin((i+1)*.7*r+.2*i) for i in range(2)])
  # Independent AD of angle-dependent first response, holding background fixed.
  def tangent(v):
   ss=2*(u*v).sum(0)/r**2
   zz1=-inv(b*y0*r*ss,L)
   zz2=-inv(b*(S*zz1+ss*z1)+6*a*y0*z1*zz1/r,L)
   return (zz1+zz2)/math.sqrt(2)
  jvp=torch.autograd.functional.jvp(tangent,torch.zeros_like(u),direction)[1]
  jerr=float((jvp-(J1+J2)@direction.flatten()).norm()/jvp.norm())
  qa={'tangent_jvp_error':jerr};assert jerr<1e-9
  if L==0:
   hv=torch.autograd.functional.hvp(lambda v:radial_energy(v,method),u,direction)[1].flatten()
   rank=4*omega**2*torch.outer(u.flatten(),u.flatten())/u.square().sum()
   err=float((hv-(A+rank)@direction.flatten()).norm()/hv.norm());qa['radial_hvp_error']=err;assert err<1e-9
  return A,D,M,qa
 return reduced
