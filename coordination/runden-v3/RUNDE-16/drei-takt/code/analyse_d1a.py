#!/usr/bin/env python3
"""Auswertung D1a (Gitter A und B) und Querkontrolle D1d bei Omega = 1 gegen D1a. Aufruf: python analyse_d1a.py <aus>"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from d1d_takt import monodromie_block

AUS = sys.argv[1]
TOL = 1e-6
MU_R = (1 - np.sqrt(69) / 9) / 2
res = {}
for g in ("A", "B"):
    f = os.path.join(AUS, "d1a", f"d1a_{g}.npz")
    if not os.path.exists(f):
        continue
    z = np.load(f)
    mus, es, m2, m4, br = z["mus"], z["es"], z["maxabs2000"], z["maxabs4000"], z["best2000"]
    s2 = m2 <= 1 + TOL; s4 = m4 <= 1 + TOL
    d = np.nonzero(s2 != s4)
    r = dict(abweichungen_n=int(d[0].size))
    r["abweichungen_liste_mu_e_m2_m4"] = [[float(mus[i]), float(es[j]), float(m2[j, i]), float(m4[j, i])]
                                          for j, i in zip(*d)][:60]
    r["abweichungen_mu_gleich_0"] = int((mus[d[1]] == 0).sum())
    dbr = np.nonzero(s2 != (br <= 1 + TOL))
    r["eig_vs_polynom_abweichungen"] = int(dbr[0].size)
    r["eig_vs_polynom_davon_mu_0"] = int((mus[dbr[1]] == 0).sum())
    r["max_abs_rho_spalte_mu0"] = float(m4[:, 0].max())
    ober = (mus[None, :] > MU_R) & (es[:, None] > 0) & s4
    jj, ii = np.nonzero(ober)
    r["stabil_ueber_muR_anzahl"] = int(ober.sum())
    if ober.any():
        r["stabil_ueber_muR_mu_max"] = float(mus[ii].max())
        r["stabil_ueber_muR_e_bereich"] = [float(es[jj].min()), float(es[jj].max())]
        # je e: stabile mu > mu_R
        zeilen = {}
        for j in np.unique(jj):
            mm = mus[(mus > MU_R) & s4[j]]
            zeilen[f"{es[j]:.4f}"] = [float(mm.min()), float(mm.max()), int(mm.size)]
        r["stabil_ueber_muR_je_e"] = zeilen
        # Abstand zur Instabilitaet innerhalb des Streifens: kleinstes max|rho| - 1 (sollte ~0) und groesstes Wachstum
    # Anteil instabil bei mu < mu_R (ohne mu = 0) und e > 0, der bei e = 0 stabil ist
    unt = (mus[None, :] < MU_R) & (mus[None, :] > 0) & (es[:, None] > 0)
    r["anteil_instabil_unter_muR_e_gt_0"] = float((~s4 & unt).sum() / unt.sum())
    r["anteil_stabil_ueber_muR_e_gt_0"] = float((s4 & (mus[None, :] > MU_R) & (es[:, None] > 0)).sum() /
                                               ((mus[None, :] > MU_R) & (es[:, None] > 0)).sum())
    res[g] = r
# Gitter A gegen B an gemeinsamen Punkten
try:
    a = np.load(os.path.join(AUS, "d1a", "d1a_A.npz")); b = np.load(os.path.join(AUS, "d1a", "d1a_B.npz"))
    ia = {round(float(m), 6): i for i, m in enumerate(a["mus"])}; ja = {round(float(e), 6): j for j, e in enumerate(a["es"])}
    diff = 0; tot = 0
    for jb, eb in enumerate(b["es"]):
        if round(float(eb), 6) not in ja:
            continue
        for ib, mb in enumerate(b["mus"]):
            if round(float(mb), 6) not in ia:
                continue
            tot += 1
            diff += int((a["maxabs4000"][ja[round(float(eb), 6)], ia[round(float(mb), 6)]] <= 1 + TOL) !=
                        (b["maxabs4000"][jb, ib] <= 1 + TOL))
    res["A_gegen_B_gemeinsame_punkte"] = [tot, diff]
except Exception as ex:
    res["A_gegen_B_fehler"] = repr(ex)

# Querkontrolle: D1d-Gleichung bei Omega = 1, eps = e, Zungenraender nahe 0,0286 gegen D1a (Bisektion bei e = 0,02, 0,04)
def raender(eps):
    mus = np.linspace(0.024, 0.034, 401)
    M = monodromie_block(mus, np.full_like(mus, eps), np.ones_like(mus), 4000)
    mx = np.abs(np.linalg.eigvals(M)).max(axis=1)
    st = mx <= 1 + TOL
    w = np.nonzero(st[:-1] != st[1:])[0]
    return [float(0.5 * (mus[i] + mus[i + 1])) for i in w]

res["d1d_Omega1_zungenraender"] = {str(e): raender(e) for e in (0.02, 0.04, 0.1)}
with open(os.path.join(AUS, "d1a", "analyse_d1a.json"), "w") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1)[:9000])
