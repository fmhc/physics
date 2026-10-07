"""V-1-PRAEZISION (Runde 37): Umgebungsprobe auf der .69 (mpmath, Backend, Rechenzeit Ganzzahl-Faltung)."""
import sys
import time

print("python", sys.version.split()[0])
try:
    import mpmath
    print("mpmath", mpmath.__version__, "backend", mpmath.libmp.BACKEND)
except Exception as e:  # noqa: BLE001
    print("mpmath fehlt:", e)
for name in ("gmpy2", "flint"):
    try:
        __import__(name)
        print(name, "vorhanden")
    except Exception as e:  # noqa: BLE001
        print(name, "fehlt:", type(e).__name__)

# Zeitprobe: Faltung mit 200-bit-Ganzzahlen (Festkomma) gegen mpf
import operator  # noqa: E402
import random  # noqa: E402

random.seed(1)
P = 200
a = [random.getrandbits(P) - (1 << (P - 1)) for _ in range(70)]
b = [random.getrandbits(P) - (1 << (P - 1)) for _ in range(70)]
t0 = time.perf_counter()
n = 0
for rep in range(200):
    for j in range(70):
        s = sum(map(operator.mul, a[:j + 1], b[j::-1]))
        n += j + 1
t1 = time.perf_counter()
print(f"int-Faltung: {1e9 * (t1 - t0) / n:.1f} ns je Term")
try:
    mpmath.mp.prec = P
    am = [mpmath.mpf(x) / 2 ** P for x in a]
    bm = [mpmath.mpf(x) / 2 ** P for x in b]
    t0 = time.perf_counter()
    n = 0
    for rep in range(10):
        for j in range(70):
            s = mpmath.fdot(am[:j + 1], bm[j::-1])
            n += j + 1
    t1 = time.perf_counter()
    print(f"mpf-fdot: {1e9 * (t1 - t0) / n:.1f} ns je Term")
except Exception as e:  # noqa: BLE001
    print("mpf-Probe fehlgeschlagen:", e)
