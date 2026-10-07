# EIS-1 (Runde 34): Versionsprobe der Python-Umgebung auf der .69 (laeuft nur ueber kleintest.sh).
import sys, time, os
print("python", sys.version.split()[0])
for name in ("numpy", "scipy", "numba", "torch"):
    try:
        m = __import__(name)
        print(name, getattr(m, "__version__", "?"))
    except Exception as e:
        print(name, "FEHLT", type(e).__name__, e)
print("OMP_NUM_THREADS", os.environ.get("OMP_NUM_THREADS"))
try:
    import numba
    from numba import njit
    import numpy as np

    @njit(cache=False)
    def lauf(n, seed):
        np.random.seed(seed)
        s = 0
        for k in range(n):
            s += np.random.randint(0, 4)
        return s

    t0 = time.time(); lauf(1000, 1); t1 = time.time()
    lauf(100_000_000, 2); t2 = time.time()
    print("numba jit %.2f s, 1e8 Zufallszahlen %.2f s" % (t1 - t0, t2 - t1))
except Exception as e:
    print("numba-Test fehlgeschlagen", e)
