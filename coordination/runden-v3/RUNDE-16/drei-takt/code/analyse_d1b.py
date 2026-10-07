#!/usr/bin/env python3
"""D1b: Vergleich je Teilchen haupt (dt) gegen halb (dt/2), Kontrolle unterhalb mu_R. Aufruf: python analyse_d1b.py <aus>"""
import sys, os, json
import numpy as np

AUS = sys.argv[1]
h = np.load(os.path.join(AUS, "d1b", "d1b_haupt.npz"))
b = np.load(os.path.join(AUS, "d1b", "d1b_halb.npz"))
res = {}
vgl = []
for i, mu in enumerate(b["mus"]):
    ih = int(np.argmin(np.abs(h["mus"] - mu)))
    for j, de in enumerate(b["deltas"]):
        jh = int(np.argmin(np.abs(h["deltas"] - de)))
        idx = np.round(b["richt"] / (2 * np.pi / 64)).astype(int)
        eh = h["ende"][ih, jh][idx]; eb = b["ende"][i, j]
        beide_gef = np.isnan(eh) & np.isnan(eb)
        beide_ent = ~np.isnan(eh) & ~np.isnan(eb)
        ungleich = int((np.isnan(eh) != np.isnan(eb)).sum())
        rel = np.abs(eh[beide_ent] - eb[beide_ent]) / eb[beide_ent] if beide_ent.any() else np.array([np.nan])
        vgl.append(dict(mu=float(mu), delta=float(de), n=int(idx.size), beide_gefangen=int(beide_gef.sum()),
                        beide_entkommen=int(beide_ent.sum()), status_ungleich=ungleich,
                        median_rel_abw_lebensdauer=float(np.nanmedian(rel)),
                        anteil_rel_abw_unter_1proz=float(np.mean(rel < 0.01)) if beide_ent.any() else None))
res["haupt_gegen_halb"] = vgl
fk = os.path.join(AUS, "d1b", "d1b_kontrolle.json")
if os.path.exists(fk):
    k = json.load(open(fk))
    res["kontrolle"] = [dict(mu=z["mu"], delta=z["delta"], anteil_gefangen=z["anteil_gefangen"],
                             median_lebensdauer=z["median_lebensdauer"], min_lebensdauer=z["min_lebensdauer"],
                             dmax_gefangene_max=z["dmax_gefangene_max"], dmax_gefangene_median=z["dmax_gefangene_median"],
                             relC_gefangene_max=z["relC_gefangene_max"]) for z in k["zeilen"]]
with open(os.path.join(AUS, "d1b", "analyse_d1b.json"), "w") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
