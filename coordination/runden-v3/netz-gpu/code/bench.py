# -*- coding: utf-8 -*-
"""netzgpu Leistung: Bauzeit, Sternzeit, Zeit je Schritt (Licht, Skalar, Rahmen-Gradient), GPU-Speicher je Netzgroesse.
Aufruf (kleintest.sh): python bench.py <aus.json> [n1 n2 ...]"""
import json
import math
import sys
import time

import torch

sys.path.insert(0, '/home/fmh/fmhc-physics-remote/netz-gpu/code')
from netzgpu import licht, rahmen, skalar  # noqa: E402
from netzgpu.netz import Netz  # noqa: E402

out = {'gpu': torch.cuda.get_device_name(0), 'torch': torch.__version__,
       'frei_MB_start': torch.cuda.mem_get_info()[0] / 1e6, 'laeufe': []}
ns = [int(x) for x in sys.argv[2:]] or [8, 16, 24]
for dt_name, dtyp in (('fp64', torch.float64), ('fp32', torch.float32)):
    for n in ns:
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
        r = {'n': n, 'dtype': dt_name}
        try:
            t0 = time.time()
            N = Netz('V', (n, n, n), dtype=dtyp)
            torch.cuda.synchronize()
            r['bau_s'] = time.time() - t0
            r['N'] = [N.N_e, N.N_k, N.N_d, N.N_t]
            t0 = time.time()
            L = licht.Licht(N)
            torch.cuda.synchronize()
            r['sterne_licht_s'] = time.time() - t0
            A = torch.randn(N.N_k, dtype=dtyp, device=N.device) * 1e-3
            P = torch.zeros_like(A)
            A, P = L.schritt(A, P, 0.01, 5)
            torch.cuda.synchronize()
            t0 = time.time()
            A, P = L.schritt(A, P, 0.01, 50)
            torch.cuda.synchronize()
            r['licht_ms_je_schritt'] = (time.time() - t0) / 50 * 1e3
            del L, A, P
            sk = skalar.Skalar(N, h=1.0)
            ph = torch.complex(torch.randn(N.N_e, dtype=dtyp, device=N.device), torch.zeros(N.N_e, dtype=dtyp, device=N.device)) * 0.1
            pi_ = torch.zeros_like(ph)
            ph, pi_ = sk.schritt(ph, pi_, 0.01, 5)
            torch.cuda.synchronize()
            t0 = time.time()
            ph, pi_ = sk.schritt(ph, pi_, 0.01, 50)
            torch.cuda.synchronize()
            r['skalar_ms_je_schritt'] = (time.time() - t0) / 50 * 1e3
            del sk, ph, pi_
            rh = rahmen.Rahmen(N, torch.tensor([n / 2.0] * 3, dtype=dtyp, device=N.device), 1.0, n / 2.0 - 1.0)
            q = rh.praediktor(rh.eins(), math.pi)
            torch.cuda.synchronize()
            t0 = time.time()
            for _ in range(50):
                E, G, c = rh.energie(q)
            torch.cuda.synchronize()
            r['rahmen_gradient_ms'] = (time.time() - t0) / 50 * 1e3
            r['gpu_speicher_max_MB'] = torch.cuda.max_memory_allocated() / 1e6
            del rh, q, N
        except Exception as e:  # noqa: BLE001
            r['fehler'] = repr(e)[:300]
        out['laeufe'].append(r)
        print(json.dumps(r), flush=True)
with open(sys.argv[1], 'w') as f:
    json.dump(out, f, indent=1)
