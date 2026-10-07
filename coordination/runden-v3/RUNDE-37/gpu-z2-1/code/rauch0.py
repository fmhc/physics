#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GPU-Z2-1, Rauchtest 0 (nur Technik): torch mit CUDA, Karte, Speicher, FP64-Grundoperationen.
Synthetische Modellrechnung, keine Messdaten. Aufruf nur ueber kleintest.sh auf der .69."""
import json
import os
import sys
import time

out = {"python": sys.version.split()[0], "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES")}
try:
    import numpy as np
    import scipy
    out["numpy"] = np.__version__
    out["scipy"] = scipy.__version__
except Exception as e:  # noqa: BLE001
    out["numpy_fehler"] = repr(e)
try:
    import torch
    out["torch"] = torch.__version__
    out["torch_cuda"] = torch.version.cuda
    out["cuda_verfuegbar"] = bool(torch.cuda.is_available())
    if torch.cuda.is_available():
        out["geraete"] = torch.cuda.device_count()
        out["name"] = torch.cuda.get_device_name(0)
        out["faehigkeit"] = list(torch.cuda.get_device_capability(0))
        out["arch_liste"] = torch.cuda.get_arch_list()
        frei, gesamt = torch.cuda.mem_get_info(0)
        out["speicher_frei_mib"] = frei / 2**20
        out["speicher_gesamt_mib"] = gesamt / 2**20
        dev = torch.device("cuda")
        n = 2_000_000
        g = torch.Generator(device=dev)
        g.manual_seed(1)
        x = torch.rand(n, dtype=torch.float64, device=dev, generator=g)
        a = torch.randint(0, n, (2 * n,), device=dev, generator=g)
        b = torch.randint(0, n, (2 * n,), device=dev, generator=g)
        torch.cuda.synchronize()
        t0 = time.time()
        for _ in range(20):
            d = x[a] - x[b]
            s = torch.sin(2.0 * d)
            G = torch.zeros_like(x)
            G.index_add_(0, a, s)
            G.index_add_(0, b, -s)
        torch.cuda.synchronize()
        out["zeit_je_gradient_2e6_knoten_ms"] = (time.time() - t0) / 20 * 1e3
        xs = x.cpu().numpy()
        an = a.cpu().numpy()
        bn = b.cpu().numpy()
        sn = np.sin(2.0 * (xs[an] - xs[bn]))
        Gn = np.zeros_like(xs)
        np.add.at(Gn, an, sn)
        np.add.at(Gn, bn, -sn)
        out["max_abw_gegen_numpy"] = float(np.abs(G.cpu().numpy() - Gn).max())
        out["dtype"] = str(G.dtype)
        out["speicher_spitze_mib"] = torch.cuda.max_memory_allocated() / 2**20
except Exception as e:  # noqa: BLE001
    out["torch_fehler"] = repr(e)
ziel = sys.argv[1] if len(sys.argv) > 1 else "rauch0.json"
with open(ziel, "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out))
