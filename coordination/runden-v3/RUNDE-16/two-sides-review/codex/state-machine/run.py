import itertools,json,time,resource,socket,hashlib
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
assert socket.gethostname().split('.')[0]=='ubuntu-auto'
t0=time.process_time()
graphs={'triangle':[[1,2],[0,2],[0,1]],'square':[[1,3],[0,2],[1,3],[0,2]],'tetrahedron':[[1,2,3],[0,2,3],[0,1,3],[0,1,2]],'star4':[[1,2,3],[0],[0],[0]]}
out={'interpretation':'Event counts only. No physical energy or duration assigned.','graphs':{}}
def transition(v,r,g):
    if v is None:return (None,r)
    rr=list(r);rr[v]=(rr[v]+1)%len(g[v]);return (g[v][rr[v]],tuple(rr))
for name,g in graphs.items():
    states=list(itertools.product(range(len(g)),itertools.product(*(range(len(a)) for a in g))))
    lookup={s:i for i,s in enumerate(states)};nxt=[]
    for v,r in states:
        nxt.append(lookup[transition(v,r,g)])
    assert all(transition(None,r,g)==(None,r) for _,r in states)
    indegrees=[0]*len(states)
    for j in nxt:indegrees[j]+=1
    cycles=set();maxtrans=0
    for start in range(len(states)):
        seen={};path=[];s=start
        while s not in seen:
            seen[s]=len(path);path.append(s);s=nxt[s]
        cyc=path[seen[s]:];idx=cyc.index(min(cyc));cyc=tuple(cyc[idx:]+cyc[:idx]);cycles.add(cyc)
        maxtrans=max(maxtrans,seen[s])
    periods=sorted(set(map(len,cycles)));arcs=sum(map(len,g))
    assert periods==[arcs]
    arc_checks=[]
    for cycle in cycles:
        traversals=[(states[i][0],states[nxt[i]][0]) for i in cycle]
        arc_checks.append(len(set(traversals))==arcs)
    assert all(arc_checks)
    first=min(cycles)
    out['graphs'][name]={'vertices':len(g),'degrees':list(map(len,g)),'states':len(states),'cycles':len(cycles),'periods_events':periods,'recurrent_states':sum(map(len,cycles)),'max_transient_events':maxtrans,'full_map_bijective':all(i==1 for i in indegrees),'indegree_histogram':{str(i):indegrees.count(i) for i in sorted(set(indegrees))},'every_arc_once_per_cycle':all(arc_checks),'one_cycle':[{'token':states[i][0],'rotors':list(states[i][1])} for i in first]}
pop=lambda x:bin(x).count('1')
gates=[p for p in itertools.permutations(range(4)) if all(pop(i)==pop(p[i]) for i in range(4))]
assert gates==[(0,1,2,3),(0,2,1,3)]
def fredkin(i):
    a,b,c=(i>>2)&1,(i>>1)&1,i&1
    return (a<<2)|((c if a else b)<<1)|(b if a else c)
f=[fredkin(i) for i in range(8)]
assert len(set(f))==8 and all(f[f[i]]==i and pop(f[i])==pop(i) for i in range(8))
out['two_bit_number_preserving_permutations']=gates;out['fredkin_map']=f
out['empty_token']='all rotor configurations tested stationary without token; rule-defined'
counter=[0]
for _ in range(4):counter.append((counter[-1]+1)%4)
assert counter==[0,1,2,3,0]
out['forced_four_phase_counter']={'trace':counter,'interpretation':'period4 by construction, not emergent'}
out['cpu_seconds']=time.process_time()-t0;out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
Path('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
