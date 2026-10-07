# W5c-Zusatz: Wirkung eines B2/B3-Funktionals auf leichte Materie (Spin 0 und 2, Masse m_l < M), CHLPSD (3.8a,b)
# mit berichtigtem Faktor (m_l^4 - 6 m_l^2 p^2 + 6 p^4) (gedruckt: m_l^2 - 6 m_l p^2 + 6 p^4; die Berichtigung
# reproduziert (3.9) fuer F_g3 exakt, siehe Selbsttest). Positiv fuer alle m_l -> Schranke gilt auch mit leichter Materie.
# Aufruf: w5d_materie.py <lp-ausgabe.out>   oder   w5d_materie.py selbsttest
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
import sys
import json
import numpy as np
from numpy.polynomial import polynomial as npp


def integ(c, q, shift=0):
    """Int_0^q p^shift * sum c_k p^k dp"""
    return sum(ck * q ** (k + shift + 1) / (k + shift + 1) for k, ck in enumerate(c))


def matter(psi2, psi3, q, c4=0.0):
    I = {k: integ(psi2, q, k) for k in (0, 2, 4, 6)}
    Jm = {k: integ(psi3, q, k) for k in (0, 2, 4)}
    ml = np.concatenate([np.geomspace(1e-3, 0.1, 50), np.linspace(0.1, 1.0, 901)])
    s0 = 2 * ml**2 * I[0] - I[2] + Jm[0]
    # Spin 2 (mal m_l^4): Int psi2 (2 m^2 - p^2)(m^4 - 6 m^2 p^2 + 6 p^4) + Int psi3 (m^4 - 6 m^2 p^2 + 6 p^4) - c4*12
    s2m4 = (2 * ml**6 * I[0] - 13 * ml**4 * I[2] + 18 * ml**2 * I[4] - 6 * I[6]
            + ml**4 * Jm[0] - 6 * ml**2 * Jm[2] + 6 * Jm[4] - 12.0 * c4)
    k0 = int(np.argmin(s0)); k2 = int(np.argmin(s2m4))
    return {"spin0_min": (float(s0[k0]), float(ml[k0])), "spin2_min_mal_m4": (float(s2m4[k2]), float(ml[k2])),
            "spin2_poly_koeff_m6_m4_m2_m0": [2 * I[0], -13 * I[2] + Jm[0], 18 * I[4] - 6 * Jm[2],
                                             -6 * I[6] + 6 * Jm[4] - 12.0 * c4],
            "spin0_poly_koeff_m2_m0": [2 * I[0], -I[2] + Jm[0]]}


if sys.argv[1] == "selbsttest":
    om3 = npp.polypow([1.0, -1.0], 3)
    psi2 = npp.polymul(om3, [0.0, 65.0, 155.0, 47.0])
    psi3 = npp.polymul(om3, [162.0, -3854.0, 9202.0])
    r = matter(psi2, psi3, 1.0, c4=-5.0)
    r["CHLPSD_3.9_soll"] = {"spin0": [2591 / 210, 1 / 18], "spin2": [2591 / 210, -239 / 18, -64573 / 1540, 330151 / 4004]}
    print(json.dumps(r, indent=1))
else:
    txt = open(sys.argv[1]).read()
    js = json.loads(txt[txt.index("{"): txt.rindex("}") + 1])
    r = matter(np.array(js["psi2"]), np.array(js["psi3"]), float(js.get("q", 1.0)))
    r["datei"] = sys.argv[1]
    print(json.dumps(r, indent=1))
