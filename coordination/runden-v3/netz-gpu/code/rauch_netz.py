# -*- coding: utf-8 -*-
"""Rauchtest netzgpu.netz: Netze V, S, Kuhn bauen, Inzidenzen und Sterne pruefen (GPU, FP64)."""
import json
import sys
import time

import torch

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu.netz import Netz  # noqa: E402

out = {'torch': torch.__version__, 'gpu': torch.cuda.get_device_name(0)}
for typ, n in (('V', 2), ('S', 2), ('Kuhn', 3), ('V', 8)):
    t0 = time.time()
    N = Netz(typ, (n, n, n))
    torch.cuda.synchronize()
    tb = time.time() - t0
    t0 = time.time()
    st = N.sterne()
    torch.cuda.synchronize()
    ts = time.time() - t0
    p = N.pruefung(st)
    p.update({'bau_s': round(tb, 3), 'sterne_s': round(ts, 3)})
    # Regge-Weg (Laengen statt Lagen) muss flach dasselbe geben
    st2 = N.sterne(l=N.laengen())
    p['regge_gegen_flach_s1'] = float((st2['s1'] - st['s1']).abs().max())
    p['regge_gegen_flach_s2'] = float((st2['s2'] - st['s2']).abs().max())
    p['regge_gegen_flach_s0'] = float((st2['s0'] - st['s0']).abs().max())
    out['%s-%d' % (typ, n)] = p
    print(typ, n, json.dumps(p), flush=True)
out['speicher_MB'] = torch.cuda.max_memory_allocated() / 1e6
print(json.dumps(out, indent=1))
