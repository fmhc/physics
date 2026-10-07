# QBALL-GITTER-1: zwei Laufausgaben (npz) feldweise vergleichen (Rauch: Fortsetzung bitgleich?).
import sys, json
import numpy as np

a = np.load(sys.argv[1]); b = np.load(sys.argv[2])
out = {}
for k in a.files:
    x = np.asarray(a[k], float); y = np.asarray(b[k], float)
    if x.shape != y.shape:
        out[k] = "Form %s gegen %s" % (x.shape, y.shape)
        continue
    d = np.abs(x - y)
    d = d[np.isfinite(d)]
    out[k] = float(d.max()) if d.size else 0.0
print(json.dumps(out))
