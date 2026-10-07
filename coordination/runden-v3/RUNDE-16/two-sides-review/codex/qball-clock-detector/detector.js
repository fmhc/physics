import {RadialSimulation} from './live-solver.js';
export class DetectorSimulation extends RadialSimulation {
 constructor(options){
  super(options);this.alpha=options.alpha;this.OmegaD=options.ratio*this.rho;
  this.detIndex=8*this.N;
  const y=new Float64Array(this.detIndex+2);y.set(this._y);this._y=y;
  this._work=new Float64Array(y.length);this._k=Array.from({length:4},()=>new Float64Array(y.length));
  this.weight=Float64Array.from(this.r,r=>Math.exp(-(r*r)/4)/(8*Math.PI**1.5));
  y[this.detIndex]=this.alpha*this.functional(y);
 }
 functional(y){let v=0;const n=this.N;for(let i=1;i<n-1;i++)v+=(i%2?4:2)*this.weight[i]*(y[i]**2+y[n+i]**2-(this.r[i]*this._f[i])**2);return v*4*Math.PI*this.h/3;}
 detector(y=this._y){const X=y[this.detIndex],P=y[this.detIndex+1],F=this.functional(y);return {X,P,F,D:(P*P+this.OmegaD**2*(X-this.alpha*F)**2)/2,K:P*P/2};}
 _rhs(y,out,rates){
  super._rhs(y,out,rates);const d=this.detector(y),n=this.N;
  const force=this.OmegaD**2*this.alpha*(d.X-this.alpha*d.F);
  for(let i=1;i<n-1;i++){out[2*n+i]+=force*this.weight[i]*y[i];out[3*n+i]+=force*this.weight[i]*y[n+i];}
  out[this.detIndex]=d.P;out[this.detIndex+1]=-(this.OmegaD**2)*(d.X-this.alpha*d.F);
 }
}
export function gradientCheck(profile){
 const s=new DetectorSimulation({profile,h:.2,R:80,epsilon:.005,alpha:1,ratio:1});
 s._y[s.detIndex]+=.1;const y=s._y,i=5,dx=1e-5,old=y[i];
 y[i]=old+dx;const plus=s.detector().D;y[i]=old-dx;const minus=s.detector().D;y[i]=old;
 const numerical=(plus-minus)/(2*dx),d=s.detector();
 const actual=new Float64Array(y.length),base=new Float64Array(y.length);
 s._rhs(y,actual,new Float64Array(4));
 RadialSimulation.prototype._rhs.call(s,y,base,new Float64Array(4));
 const force=actual[2*s.N+i]-base[2*s.N+i];
 const volume=4*Math.PI*s.h/3*(i%2?4:2),expected=-2*volume*force;
 const err=Math.abs(numerical-expected)/Math.max(1e-30,Math.abs(expected));
 const mutant=Math.abs(numerical+expected)/Math.max(1e-30,Math.abs(expected));
 return {numerical,expected,relativeError:err,wrongSignError:mutant,pass:err<1e-6&&mutant>1e-2};
}
