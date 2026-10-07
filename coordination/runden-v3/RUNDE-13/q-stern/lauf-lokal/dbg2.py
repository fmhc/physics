import sys, time, numpy as np
sys.path.insert(0, '.')
import qstern as q
q.ALPHA = float(sys.argv[1])
q.PHI_MISCH = float(sys.argv[2])
q.N_RAMPE = int(sys.argv[3])
orig = q.phi_aus_profil
def pa(m, x, rr, f, p, al=None):
    Ph, c, mq = orig(m, x, rr, f, p, al)
    print("al %.4f f0 %.12f Phi0 %.8f c %.6f t %.1f" % (al, f[0], Ph[0], c, time.perf_counter()), flush=True)
    return Ph, c, mq
q.phi_aus_profil = pa
prot = []
t0 = time.perf_counter()
p = q.profile("kg", [float(sys.argv[4])], 0.02, prot=prot)
print(prot, time.perf_counter() - t0)
if p[0] is not None:
    print("f0", p[0]["f0"], "Phi0", p[0]["Phi0"], "Q", p[0]["Q"], "E", p[0]["E"], "Rw", p[0]["R_w"], "PhiRw", p[0]["Phi_Rw"], "eta", p[0]["eta_schwanz"])
