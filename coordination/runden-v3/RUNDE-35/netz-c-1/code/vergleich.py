# NETZ-C-1 Rauch: fortgesetzter Lauf (Checkpoints) gegen ununterbrochenen Lauf, bitgleich?
import sys, json
import numpy as np
a = np.load(sys.argv[1]); b = np.load(sys.argv[2])
out = {}
for f in a.files:
    x = a[f]; y = b[f]
    out[f] = dict(laenge=[len(x), len(y)], max_abs_diff=float(np.nanmax(np.abs(x - y))) if len(x) == len(y) else None)
print(json.dumps(out))
print(json.dumps(json.load(open(sys.argv[1].replace(".npz", ".json")))))
