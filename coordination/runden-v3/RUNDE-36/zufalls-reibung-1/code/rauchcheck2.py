# ZUFALLS-REIBUNG-1: Rauch-Auskunft mit den Messgroessen der Auswertung (nur Rauch, keine Urteile).
# Aufruf (ueber kleintest.sh): rauchcheck2.py <ordner> <name> [<name> ...]
import sys, os, json, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auswertung as aw

ordner = sys.argv[1]
for name in sys.argv[2:]:
    d = aw.lade(ordner, name)
    if d is None:
        print("==", name, "fehlt/nicht fertig"); continue
    r, _ = aw.kenngroessen(d)
    print("==", name)
    for kk in ("v_TA", "v_mittel", "v_min", "v_ende", "umkehr", "max_rel_dv", "Q_verlust_max_rel", "rA", "seA", "rB", "seB",
               "rC", "seC", "rQ_rel", "seQ", "rP", "seP", "rPw", "sePw", "dQ_rel_fenster", "gc_min", "vc_TA", "vc_ende",
               "bilanz_E_max_rel", "bilanz_Q_max_rel", "min_1_plus_sigma_eta", "wandzeit_s", "T_mess"):
        val = r.get(kk)
        print("   %-20s %s" % (kk, ("%.4e" % val) if isinstance(val, float) else val))
    # Teilfenster
    k = d["kopf"]; t = d["t"]
    v = aw.schnelle(t, d["X"]); Mq, _ = aw.mq_funktion(k)
    Vs = aw.glatt_wie_v(t, d["Vwin"])
    gv = 1.0 / np.sqrt(np.clip(1.0 - v * v, 1e-300, None))
    gc = gv + Vs / Mq(d["Qwin"])
    for a, b in ((400, 800), (800, 1200), (1200, 1600), (400, 1000), (1000, 1600)):
        sel = (t >= a) & (t <= b) & np.isfinite(gc)
        if sel.sum() < 20 or b > t[np.isfinite(v)][-1]:
            continue
        yB = 0.5 * np.log(np.clip(gc[sel] ** 2 - 1.0, 1e-300, None))
        bB, seB = aw.steigung(t[sel], yB)
        bQ, seQ = aw.steigung(t[sel], d["Qwin"][sel])
        print("   Teilfenster [%d,%d]: rB = %.3e +- %.1e ; rQ_rel = %.3e ; v_mittel = %.4f ; vc %.4f -> %.4f" % (
            a, b, -bB, seB, -bQ / k["Q_ruhe"], float(np.mean(v[sel])), math.sqrt(1 - 1 / gc[sel][0] ** 2),
            math.sqrt(max(0.0, 1 - 1 / gc[sel][-1] ** 2))))
