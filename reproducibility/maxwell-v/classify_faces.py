#!/usr/bin/env python3
"""Postprocess the fixed negative faces; exact embedded time equality is integer-valued."""
import argparse
import json
from pathlib import Path
from reproduce import geometry, face_key, TRIANGLES

ap=argparse.ArgumentParser()
ap.add_argument('--input',type=Path,default=Path('result.json'))
ap.add_argument('--output',type=Path,default=Path('face-classification.json'))
a=ap.parse_args()
r=json.loads(a.input.read_text())
_,simp=geometry()
faces=sorted({face_key([s[i] for i in tri]) for s in simp for tri in TRIANGLES})
out={'tau':r['tau'],'definition':'embedded Euclidean time = tau*(b/10+n_t); same embedded time means equal integer b+10*n_t, not merely equal n_t','arms':{}}
for name,arm in r['arms'].items():
    negative=[]
    for f,w in zip(faces,arm['weights']):
        if w>=0: continue
        integers=[b+10*n[3] for b,n in f]
        negative.append({'vertices':f,'weight':w,'embedded_times_in_tau_tenths':integers,'same_embedded_time':len(set(integers))==1,'same_integer_time_layer':len({n[3] for b,n in f})==1})
    out['arms'][name]={'negative_faces':negative,'count':len(negative),'same_embedded_time_count':sum(x['same_embedded_time'] for x in negative),'same_integer_time_layer_count':sum(x['same_integer_time_layer'] for x in negative)}
a.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({name:{k:v for k,v in arm.items() if k!='negative_faces'} for name,arm in out['arms'].items()}))
