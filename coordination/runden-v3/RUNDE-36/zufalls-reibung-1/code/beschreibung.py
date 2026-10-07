# ZUFALLS-REIBUNG-1: beschreibende Zusatzzahlen nach dem Einfrieren (keine Urteile).
# Teilfenster [400, 900] und [900, 1400]: r_B, r_Q/Q0, mittlere Schnelle; Zweipunkt-/Dreipunkt-Potenz je Teilfenster
# und je v (Saatmittel A, B, nur Laeufe ohne Umkehr).
# Aufruf (ueber kleintest.sh): beschreibung.py <laufordner> <ausgabe.json>
import sys, os, json, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auswertung as aw

ordner = sys.argv[1]; aus = sys.argv[2]
TEILE = ((400.0, 900.0), (900.0, 1400.0))
erg = {"laeufe": {}, "potenz": {}}
for f in sorted(os.listdir(ordner)):
    if not (f.endswith(".json") and f.startswith("v") and "_dt2" not in f):
        continue
    n = f[:-5]
    d = aw.lade(ordner, n)
    if d is None:
        continue
    k = d["kopf"]; t = d["t"]
    v = aw.schnelle(t, d["X"]); Mq, _ = aw.mq_funktion(k)
    Vs = aw.glatt_wie_v(t, d["Vwin"])
    gv = 1.0 / np.sqrt(np.clip(1.0 - v * v, 1e-300, None))
    gc = gv + Vs / Mq(d["Qwin"])
    e = {}
    for a, b in TEILE:
        sel = (t >= a) & (t <= b) & np.isfinite(gc)
        umk = bool(np.min(v[sel]) <= 0)
        bQ, seQ = aw.steigung(t[sel], d["Qwin"][sel])
        r = dict(rQ_rel=-bQ / k["Q_ruhe"], seQ_rel=seQ / k["Q_ruhe"], v_mittel=float(np.mean(v[sel])), umkehr=umk)
        if np.min(gc[sel]) > 1.0:
            bB, seB = aw.steigung(t[sel], 0.5 * np.log(gc[sel] ** 2 - 1.0))
            r.update(rB=-bB, seB=seB, vc_anfang=float(math.sqrt(1 - 1 / gc[sel][0] ** 2)),
                     vc_ende=float(math.sqrt(1 - 1 / gc[sel][-1] ** 2)))
        e["%d-%d" % (a, b)] = r
    # Arbeit des Einschaltens relativ zur Bewegungsenergie
    i400 = int(round(400.0 / k["ds_mess"]))
    e["W_einschalten"] = float(d["W"][-1]); e["E_start"] = k["E_start"]; e["M_ruhe"] = k["M_ruhe"]
    e["X_ende"] = float(d["X"][-1]); e["X_400"] = float(d["X"][i400])
    erg["laeufe"][n] = e
for v in aw.VS:
    for tl in ("%d-%d" % TEILE[0], "%d-%d" % TEILE[1]):
        rs = []
        for s in aw.SIGS:
            vals = []
            for sa in ("A", "B"):
                n = aw.name_von(v, s, sa)
                e = erg["laeufe"].get(n, {}).get(tl, {})
                if e.get("umkehr", True) or "rB" not in e:
                    vals = None; break
                vals.append(e["rB"])
            rs.append(None if vals is None else float(np.mean(vals)))
        p = None; paare = None
        if all(r is not None and r > 0 for r in rs):
            p = float(np.polyfit(np.log(aw.SIGS), np.log(rs), 1)[0])
            paare = [float(math.log(rs[1] / rs[0]) / math.log(2)), float(math.log(rs[2] / rs[1]) / math.log(2))]
        erg["potenz"]["v%g_%s" % (v, tl)] = dict(r=rs, p=p, paare=paare)
json.dump(erg, open(aus, "w"), indent=1)
for kk, vv in erg["potenz"].items():
    print(kk, vv)
for n in ("v0.1_s0.01_A", "v0.1_s0.01_B", "v0.3_s0.04_A", "v0.3_s0.04_B", "v0.5_s0.04_A", "v0.2_s0.01_A"):
    print(n, json.dumps(erg["laeufe"].get(n)))
