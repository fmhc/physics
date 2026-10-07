#!/usr/bin/env python3
"""BILDUNG-3D (Runde 23), Hilfsskript: zwei Rohdateien von zeit3d.py (lauf) bitweise vergleichen.
Rauchlauf-Probe fuer die Abschnitte bis=/weiter. Aufruf: python vergleich.py <a.roh.pt> <b.roh.pt>"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import sys  # noqa: E402

import torch  # noqa: E402

torch.set_num_threads(1)
a = torch.load(sys.argv[1], weights_only=False)
b = torch.load(sys.argv[2], weights_only=False)
print("ts gleich:", a["ts"] == b["ts"], len(a["ts"]))
print("schnapp_t gleich:", a["schnapp_t"] == b["schnapp_t"])
for k in ("zentrum", "ladung", "energie", "schnapp"):
    print(k, "bitgleich:", torch.equal(a[k], b[k]), tuple(a[k].shape))
