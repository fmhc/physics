#!/usr/bin/env python3
"""Auswertung D1d: Zungen (mu < mu_R), stabilisierende Fenster (mu > mu_R), f1 gegen f2. Aufruf: python analyse_d1d.py <aus>"""
import sys, os, json, glob
import numpy as np

AUS = sys.argv[1]
TOL = 1e-6
MU_R = (1 - np.sqrt(69) / 9) / 2


def lade(f):
    z = np.load(f)
    return z["mus"], z["epss"], z["Oms"], z["maxabs"]


def intervalle(xs, m):
    out = []; i = 0
    while i < len(xs):
        if m[i]:
            j = i
            while j + 1 < len(xs) and m[j + 1]:
                j += 1
            out.append([round(float(xs[i]), 3), round(float(xs[j]), 3)]); i = j + 1
        else:
            i += 1
    return out


f1 = sorted(glob.glob(os.path.join(AUS, "d1d", "d1d_*_f1.npz")))[0]
mus, epss, Oms, m1 = lade(f1)
res = dict(datei_f1=os.path.basename(f1))
f2s = sorted(glob.glob(os.path.join(AUS, "d1d", "d1d_*_f2.npz")))
if f2s:
    _, _, _, m2 = lade(f2s[0])
    s1 = m1 <= 1 + TOL; s2 = m2 <= 1 + TOL
    res["f1_gegen_f2_abweichungen"] = int((s1 != s2).sum())
    res["f1_gegen_f2_punkte"] = int(s1.size)
    res["f1_gegen_f2_max_abs_diff_maxabs"] = float(np.max(np.abs(m1 - m2)))
    res["f1_gegen_f2_je_mu"] = [int((s1[i] != s2[i]).sum()) for i in range(len(mus))]
st = m1 <= 1 + TOL
pro = {}
for i, mu in enumerate(mus):
    e = {}
    if mu < MU_R:
        c = (27 / 4) * mu * (1 - mu); d = np.sqrt(1 - 4 * c)
        sA = np.sqrt((1 + d) / 2); sB = np.sqrt((1 - d) / 2)
        kand = {"2s1": 2 * sA, "2s2": 2 * sB, "s1 (2s1/2)": sA, "s2 (2s2/2)": sB, "s1-s2": sA - sB,
                "s1+s2": sA + sB, "2s1/3": 2 * sA / 3, "2s2/3": 2 * sB / 3, "(s1-s2)/2": (sA - sB) / 2,
                "(s1+s2)/2": (sA + sB) / 2, "Omega=1": 1.0}
        e["s1_s2"] = [float(sA), float(sB)]
        for ev in (0.02, 0.05, 0.1):
            j = int(np.argmin(np.abs(epss - ev)))
            e[f"instabil_eps{ev}"] = intervalle(Oms, ~st[i, j])
            # max|rho| im Fenster +-0,015 um jede Kandidatenfrequenz
            e[f"maxrho_kandidaten_eps{ev}"] = {k: round(float(m1[i, j][np.abs(Oms - w) <= 0.015].max()), 6)
                                               if (np.abs(Oms - w) <= 0.015).any() else None for k, w in kand.items()}
        e["anteil_instabil_eps0.3"] = float((~st[i, -1]).mean())
        e["anteil_instabil_Omega_gt_3_alle_eps"] = float((~st[i][:, Oms > 3]).mean())
    else:
        for ev in (0.02, 0.05, 0.1, 0.2, 0.3):
            j = int(np.argmin(np.abs(epss - ev)))
            e[f"stabil_eps{ev}"] = intervalle(Oms, st[i, j])
            e[f"anteil_stabil_eps{ev}"] = float(st[i, j].mean())
        # je Omega kleinstes stabiles eps
        epsmin = np.full(len(Oms), np.nan)
        for k in range(len(Oms)):
            z = np.nonzero(st[i, 1:, k])[0]
            if z.size:
                epsmin[k] = epss[1:][z.min()]
        if np.isfinite(epsmin).any():
            kb = int(np.nanargmin(epsmin))
            e["kleinstes_eps_stabil"] = float(epsmin[kb])
            e["Omega_bei_kleinstem_eps"] = [round(float(x), 3) for x in Oms[epsmin == epsmin[kb]]][:20]
        for lo, hi in ((0.2, 0.6), (0.6, 0.8), (0.8, 1.2), (1.2, 1.6), (1.6, 3.0), (3.0, 10.0)):
            sel = (Oms >= lo) & (Oms < hi)
            e[f"anteil_stabil_Omega_{lo}-{hi}"] = float(st[i][1:, sel].mean())
    pro[f"{mu:.4f}"] = e
res["pro_mu"] = pro
with open(os.path.join(AUS, "d1d", "analyse_d1d.json"), "w") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1)[:12000])
