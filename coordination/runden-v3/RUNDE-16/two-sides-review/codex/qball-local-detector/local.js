import {RadialSimulation} from './live-solver.js';
export class LocalDetector extends RadialSimulation{
 constructor(o){
  super(o);this.a=o.a;this.mu=o.ratio*this.rho;const n=this.N;
  const y=new Float64Array(10*n+1);y.set(this._y);this._y=y;
  this._work=new Float64Array(y.length);this._k=Array.from({length:4},()=>new Float64Array(y.length));
  this.weight=Float64Array.from(this.r,r=>r<4?(1-r*r/16)**4:0);
 }
 mismatch(y,i){const n=this.N,r=this.r[i];return y[8*n+i]-this.a*this.weight[i]*((y[i]**2+y[n+i]**2)/r-r*this._f[i]**2);}
 _rhs(y,out,rates){
  super._rhs(y,out,rates);const n=this.N;let sink=0;
  for(let i=1;i<n-1;i++){
   const z=this.mismatch(y,i),p=y[9*n+i],force=this.mu**2*this.a*this.weight[i]*z/this.r[i];
   out[2*n+i]+=force*y[i];out[3*n+i]+=force*y[n+i];
   out[8*n+i]=p;out[9*n+i]=this._laplacian(y,8*n,i)-this.mu**2*z-2*this._sigma[i]*p;
   sink+=(i%2?4:2)*this._sigma[i]*p*p;
  }
  out[10*n]=8*Math.PI*this.h/3*sink;
 }
 potential(y=this._y){let sum=0;for(let i=1;i<this.N-1;i++)sum+=(i%2?4:2)*this.mu**2*this.mismatch(y,i)**2/2;return sum*4*Math.PI*this.h/3;}
 detector(){
  const n=this.N,y=this._y,v=y.subarray(8*n,9*n);let sum=0,kin=0;
  for(let i=1;i<n-1;i++){
   const p=y[9*n+i],grad=this._derivative(v,i)-v[i]/this.r[i],z=this.mismatch(y,i),w=i%2?4:2;
   sum+=w*(p*p+grad*grad+this.mu**2*z*z)/2;kin+=w*p*p/2;
  }
  const i=Math.round(12/this.h),r=this.r[i];
  return {D:sum*4*Math.PI*this.h/3,K:kin*4*Math.PI*this.h/3,absorbed:y[10*n],chi8:v[Math.round(8/this.h)]/8,chi12:v[i]/r,flux12:-4*Math.PI*y[9*n+i]*(this._derivative(v,i)-v[i]/r)};
 }
}
export function check(profile){
 const s=new LocalDetector({profile,h:.2,R:80,epsilon:.005,a:.1,ratio:.5}),y=s._y,n=s.N,i=5;y[8*n+i]=.1;
 const rhs=new Float64Array(y.length),base=new Float64Array(y.length);s._rhs(y,rhs,new Float64Array(4));RadialSimulation.prototype._rhs.call(s,y,base,new Float64Array(4));
 const weight=4*Math.PI*s.h/3*(i%2?4:2),dx=1e-5,rows=[];
 for(const [index,expected] of [[i,-2*weight*(rhs[2*n+i]-base[2*n+i])],[8*n+i,-weight*(rhs[9*n+i]-s._laplacian(y,8*n,i))]]){
  const old=y[index];y[index]=old+dx;const plus=s.potential();y[index]=old-dx;const minus=s.potential();y[index]=old;
  const numerical=(plus-minus)/(2*dx),error=Math.abs(numerical-expected)/Math.abs(expected),wrong=Math.abs(numerical+expected)/Math.abs(expected);rows.push({numerical,expected,error,wrong,pass:error<1e-6&&wrong>1e-2});
 }
 return {rows,pass:rows.every(x=>x.pass)};
}
