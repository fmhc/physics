# PROFILE-1 Gegenprobe n = 1: float-Profil aus PROFILE.json gegen die strenge Integration des BEWEIS-1-Kerns
# (bewkern.py, unveraendert importiert) mit den Zertifikats-Mittelpunkten z0 = (a, c, rho, omega) aus z0.json.
# Ausgabe: GEGENPROBE.json. Nur auf der .69 ueber kleintest.sh.
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

BEWEIS = "/home/fmh/fmhc-physics-remote/runde7-beweis"
sys.path.insert(0, BEWEIS)
from flint import arb, ctx  # noqa: E402
ctx.prec = 256
import bewkern as K  # noqa: E402
import pruef as P  # noqa: E402

T0 = time.time()
HIER = os.path.dirname(os.path.abspath(__file__))


def log(*a):
    print("[%6.1fs]" % (time.time() - T0), *a, flush=True)


def main():
    d = json.load(open(os.path.join(BEWEIS, "z0.json")))
    z = [P.dy_arb(d[k]) for k in ("a", "c", "rho", "om")]
    khat = P.dy_arb(d["khat"])
    par = K.Par(z[0], z[2], z[3], khat)
    prof = json.load(open(os.path.join(HIER, "PROFILE.json")))
    st1 = [s for s in prof["stellen"] if s["name"] == "l0n1"][0]
    r = prof["r"]
    punkte = [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2), Fraction(3), Fraction(4),
              Fraction(5), Fraction(6), Fraction(8), Fraction(10), Fraction(15), Fraction(20)]
    zeilen = []
    for rk in punkte:
        st, infos, _ = K.integrate(par, rk, 40, False, Rmax=1.0, qfac=3)
        fz = st["f"]
        i = int(round(float(rk) / 0.01))
        assert abs(r[i] - float(rk)) < 1e-12
        ff = st1["f"][i]
        diff = abs(float((fz - arb(ff)).mid()))
        zeilen.append({"r": float(rk), "f_zertifikat_mitte": fz.mid().str(25), "f_zertifikat_radius": fz.rad().str(3),
                       "f_profil_float": ff, "abweichung_abs": diff, "abweichung_rel": diff / abs(ff)})
        log("r = %5.2f  f_arb = %s  f_float = %.12g  |d| = %.2e (rel %.2e)" % (float(rk), fz.str(20, radius=True), ff,
                                                                             diff, diff / abs(ff)))
    # f(0) und Schwanzamplitude c = lim r e^{kappa0 r} f(r)
    f0_z = z[0]
    f0_p = st1["f0"]
    kap0 = math.sqrt(1.0 - st1["omega2"])
    c_p = [r[i] * math.exp(kap0 * r[i]) * st1["f"][i] for i in (1800, 2000, 2200)]
    aus = {"stuetzstellen": zeilen, "f0_zertifikat": f0_z.str(25), "f0_profil_float": f0_p,
           "f0_abweichung": abs(float((f0_z - arb(f0_p)).mid())),
           "c_zertifikat": z[1].str(20), "c_profil_r_exp_f_bei_r_18_20_22": c_p,
           "bemerkung": ("f_zertifikat: strenge Kugel aus bewkern.integrate (256 bit) mit a, rho, omega = z0-Mittelpunkte "
                         "aus BEWEIS-1; c ist die Schwanzamplitude f ~ c e^{-kappa0 r}/r (z0), die float-Werte "
                         "r e^{kappa0 r} f(r) naehern c bis auf Korrekturen O(f^2)"),
           "sha256": {"gegenprobe.py": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                      "bewkern.py": hashlib.sha256(open(K.__file__, "rb").read()).hexdigest(),
                      "z0.json": hashlib.sha256(open(os.path.join(BEWEIS, "z0.json"), "rb").read()).hexdigest(),
                      "PROFILE.json": hashlib.sha256(open(os.path.join(HIER, "PROFILE.json"), "rb").read()).hexdigest()}}
    log("f(0): Zertifikat %s  float %.15f  |d| = %.2e" % (f0_z.str(20), f0_p, aus["f0_abweichung"]))
    log("c: Zertifikat %s  float r e^{kappa0 r} f bei r = 18, 20, 22: %s" % (z[1].str(15), c_p))
    with open(os.path.join(HIER, "GEGENPROBE.json"), "w") as fh:
        json.dump(aus, fh, indent=1)
    log("geschrieben GEGENPROBE.json")


if __name__ == "__main__":
    main()
