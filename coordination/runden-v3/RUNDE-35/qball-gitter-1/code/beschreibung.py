# QBALL-GITTER-1 (Runde 35): beschreibende Zusatzzahlen NACH dem Einfrieren (keine Urteile, keine Schwellen).
# Aufruf (nur ueber kleintest.sh): beschreibung.py <laufordner> <ausgabe.json>
import sys, os, json, math
import numpy as np
import auswertung as aw

ordner = sys.argv[1]; aus = sys.argv[2]


def vg_max(h):
    u = np.linspace(1e-6, math.pi, 200001)
    om = np.sqrt(1.0 + (2.0 / h ** 2) * (1.0 - np.cos(u)))
    vg = np.sin(u) / (h * om)
    i = int(np.argmax(vg))
    return float(vg[i]), float(u[i] / h)


out = {}
for h in aw.HS:
    vm, km = vg_max(h)
    out["vg_max_h%s" % h] = dict(vg_max=vm, gamma=1.0 / math.sqrt(1.0 - vm * vm), k_stern=km)
for n in ["f1_h%s_dt1" % h for h in aw.HS] + ["f2_h%s_dt1" % h for h in aw.HS]:
    d = aw.lade(ordner, n)
    if d is None:
        continue
    k = d["kopf"]; t = d["t"]; q = d["Qwin"] / k["Q0"]
    v = aw.schnelle(t, d["X"], aw.TAU); g = aw.gamma_aus_v(v)
    r = {}
    for schwelle in (0.999, 0.99, 0.9, 0.5):
        i = np.nonzero(q < schwelle)[0]
        if len(i):
            i0 = int(i[0])
            r["Q_unter_%s" % schwelle] = dict(t=float(t[i0]), gamma=float(g[i0]), v=float(v[i0]),
                                              gamma_kontinuum=float(math.sqrt(1 + (k["a0"] * t[i0]) ** 2)))
    ok = np.isfinite(g)
    im = int(np.nanargmax(np.where(ok, g, -1)))
    r["bei_tmax"] = dict(t=float(t[im]), gamma=float(g[im]), v=float(v[im]), Qwin=float(q[im]), W=float(d["W"][im]),
                         Ewin=float(d["Ewin"][im]), breite=float(d["breite"][im]),
                         E_aussen=float(d["H"][im] + d["Eabs"][im] + d["Edrop"][im] - d["Ewin"][im]))
    # Umkehr mit Ladung
    nach = np.nonzero(ok & (np.arange(len(t)) > im) & (v < 0))[0]
    if len(nach):
        r["umkehr"] = dict(t=float(t[nach[0]]), Qwin=float(q[nach[0]]), v_min=float(np.nanmin(v[im:])))
    # Verzoegerung nach dem Maximum: Steigung von v im Abschnitt nach t_max bis Laufende
    sel = ok & (t > t[im] + 50)
    if sel.sum() > 10:
        r["dv_dt_nach_max"] = float(np.polyfit(t[sel], v[sel], 1)[0])
    # Ladung ausserhalb: wie viel ist geschluckt, wie viel noch im Fenster ausserhalb des Balls
    r["ende"] = dict(t=float(t[-1]), Qwin=float(q[-1]), Qabs=float(d["Qabs"][-1] / k["Q0"]),
                     Q_rest_im_Fenster=float((d["Qdom"][-1] - d["Qwin"][-1]) / k["Q0"]),
                     W=float(d["W"][-1]), Eabs=float(d["Eabs"][-1]), Ewin=float(d["Ewin"][-1]), H=float(d["H"][-1]))
    # Vorzeichen der Ladung in der letzten Momentaufnahme ausserhalb des Balls
    sn = np.asarray(d["snaps"][-1], float) * k["h"]
    r["letzte_aufnahme"] = dict(t=float(d["snap_t"][-1]), Q_pos=float(sn[sn > 0].sum() / k["Q0"]),
                                Q_neg=float(sn[sn < 0].sum() / k["Q0"]))
    out[n] = r
json.dump(out, open(aus, "w"), indent=1)
print(json.dumps({n: (v.get("Q_unter_0.99"), v.get("umkehr")) for n, v in out.items() if n.startswith("f")}))
