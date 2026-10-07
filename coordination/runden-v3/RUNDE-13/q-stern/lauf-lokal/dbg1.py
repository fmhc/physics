import sys, numpy as np
sys.path.insert(0, '.')
import qstern as q
q.ALPHA = 0.1
orig = q._klassen
def kl(*a, **k):
    c, klass = orig(*a, **k)
    lo, hi = a[2], a[3]
    print("lo %.17g hi %.17g w %.2e unter %d ueber %d" % (lo[0], hi[0], (hi[0]-lo[0])/hi[0], (klass[0]==-1).sum(), (klass[0]==1).sum()))
    return c, klass
q._klassen = kl
prot = []
p = q.profile("kg", [0.8], 0.02, prot=prot)
print(prot)
