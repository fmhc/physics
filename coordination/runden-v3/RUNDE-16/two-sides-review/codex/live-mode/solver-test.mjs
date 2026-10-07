import assert from 'node:assert/strict';
import {createGraph,RotorSimulation,FieldSimulation,sectionMeasure} from '../../../../../../model-lab/simulation-environment/qball-explorer/causal-solver.js';
const near=(a,b,t=1e-10)=>assert.ok(Math.abs(a-b)<t,`${a} != ${b}`);
for(const [kind,n] of [['triangle',3],['square',4],['tetrahedron',4],['star4',4],['chain12',12],['chain20',20]]){
  const g=createGraph(kind);assert.equal(g.positions.length,n);
  for(const [i,j]of g.edges)near(Math.hypot(...g.positions[i].map((v,k)=>v-g.positions[j][k])),1);
  for(let k=0;k<3;k++)near(g.positions.reduce((s,p)=>s+p[k],0),0);
  const r=new RotorSimulation({graph:g});const before=r.getState(),after=r.step();
  assert.equal(after.eventIndex,1);assert.ok(g.edges.some(([i,j])=>i===before.token&&j===after.token||j===before.token&&i===after.token));
  before.rotors.forEach((v,i)=>{if(i!==before.token)assert.equal(v,after.rotors[i]);});
  assert.equal(after.lastEvent.portAfter,(after.lastEvent.portBefore+1)%r.neighbors[before.token].length);
  const idle=new RotorSimulation({graph:g,token:null}),initial=idle.getState();assert.deepEqual(idle.step(),initial);
}
const triangle=createGraph('triangle'),rotor=new RotorSimulation({graph:triangle});
for(let i=0;i<200&&!rotor.cycle;i++)rotor.step();assert.ok(rotor.cycle?.period>0);
const tetra=createGraph('tetrahedron'),section=sectionMeasure(tetra,tetra.positions,[0,0,1],0);
assert.equal(section.edgepointcount,3);assert.ok(section.tetraareasum>0);
const doubled=tetra.positions.map(p=>p.map(v=>2*v));near(sectionMeasure(tetra,doubled,[0,0,1],0).tetraareasum,4*section.tetraareasum);
assert.equal(sectionMeasure(triangle,triangle.positions,[1,0,0],0).tetraareasum,null);
const rest=new FieldSimulation({graph:tetra,kind:'elastic',kick:0});for(let i=0;i<20;i++)rest.step();assert.deepEqual(rest.positions,tetra.positions);near(rest.getState().energy,0);
function run(dt,kind,moving){const sim=new FieldSimulation({graph:tetra,kind,dt,moving});let maxE=0,maxQ=0;for(let i=0;i<Math.round(1/dt);i++){const s=sim.step();maxE=Math.max(maxE,Math.abs(s.relativeEnergyError));maxQ=Math.max(maxQ,Math.abs(s.relativeChargeError));}return {sim,maxE,maxQ};}
for(const [kind,moving]of [['elastic',true],['two-field',false],['two-field',true]]){
  const coarse=run(.01,kind,moving),fine=run(.005,kind,moving),finest=run(.0025,kind,moving);
  assert.ok(coarse.maxE<.001);assert.ok(fine.maxE<coarse.maxE*.35);assert.ok(finest.maxE<fine.maxE*.35);assert.ok(finest.maxQ<1e-11);
  if(!moving)assert.deepEqual(finest.sim.positions,tetra.positions);
  const momentum=finest.sim.velocities.reduce((s,v)=>s.map((x,k)=>x+v[k]),[0,0,0]);momentum.forEach(x=>near(x,0));
}
// Numerical action gradient: mechanical and internal masses must agree.
const coupled=new FieldSimulation({graph:tetra,kind:'two-field',moving:true});
coupled.chi[0]=.8;coupled.chi[1]=1.1;coupled.psi[0][1]=.13;coupled.positions[0][1]+=.07;
const f=coupled.forces(),eps=1e-6;
for(const [name,index,component,expected,mass]of [['positions',0,0,f.x[0][0],1],['positions',0,1,f.x[0][1],1],['psi',0,0,f.p[0][0],2],['psi',0,1,f.p[0][1],2],['chi',0,null,f.c[0],1]]){
  const read=()=>component===null?coupled[name][index]:coupled[name][index][component];
  const write=v=>{if(component===null)coupled[name][index]=v;else coupled[name][index][component]=v;};
  const value=read();write(value+eps);const plus=coupled.energyCharge().energy;write(value-eps);const minus=coupled.energyCharge().energy;write(value);
  near(-(plus-minus)/(2*eps*mass),expected,1e-8);
}
assert.throws(()=>new FieldSimulation({graph:tetra,dt:1}));
const pair=new FieldSimulation({graph:{positions:[[0,0,0],[1,0,0]],edges:[[0,1]],cells:[]},kind:'two-field',moving:true,kick:0});
pair.psi=[[.3,0],[0,0]];pair.chi=[1,1];
const outward=pair.forces().x;
assert.ok(outward[0][0]<0&&outward[1][0]>0);near(outward[0][0]+outward[1][0],0);
coupled.psi[0][0]=NaN;assert.throws(()=>coupled.step());assert.ok(coupled.failed);assert.throws(()=>coupled.step());
console.log('PASS graph geometry, local rotor events/cycle, passive sections, free mechanics, action gradients, Verlet convergence, charge and momentum conservation, fail-stop');
