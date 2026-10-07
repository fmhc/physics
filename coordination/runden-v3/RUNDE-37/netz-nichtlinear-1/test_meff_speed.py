import time, td, uf
from nn import NetzG
import numpy as np
LV, pos, G0, O0, ninfo = td.netz_bauen('glas-N128-s4')
rez = 2 * np.pi * np.linalg.inv(LV).T
k1 = rez[0]
hp, hx = td.polarisation(k1)
t0 = time.time()
N0 = NetzG(LV, pos, G0, O0, k1, hp, hx, rolle='start')
t1 = time.time()
print(f"NetzG Init dauerte {t1-t0:.3f} Sekunden")
