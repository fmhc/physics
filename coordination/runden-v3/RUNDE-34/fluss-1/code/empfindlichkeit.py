# FLUSS-1 (Runde 34): Empfindlichkeit der Ringform (nachtraeglich geschrieben, nur beschreibend, keine Urteile).
# Rechnet die Ringform von R2(r) (Netz B) und D(r) (Netz A) mit anderen Untergrenzen und Ringbreiten nach.
# Aufruf: empfindlichkeit.py <laufordner> <ausgabe.json> <L>
import sys, os, json, glob
import numpy as np

ordner = sys.argv[1]; ausgabe = sys.argv[2]; L = int(sys.argv[3])
KANTE = np.sqrt(2.0) / 4.0


def kanten_ringe(r1, r2, b):
    k = np.arange(r1, r2 + 1e-9, b)
    if k[-1] < r2 - 1e-9:
        k = np.append(k, r2)
    return k


def idx(r, k):
    j = np.searchsorted(k, r, side="right") - 1
    j[(r == k[-1])] = len(k) - 2
    j[(r < k[0]) | (r > k[-1])] = -1
    return j


def logfit(rq, y, s, k2):
    m = np.isfinite(y) & np.isfinite(s) & (y > 2 * s) & (y > 0)
    if m.sum() < 4:
        return dict(ringe_signifikant=int(m.sum()), grund="weniger als 4")
    Y = np.log(y[m]); out = dict(ringe_signifikant=int(m.sum()))
    for name, X in (("potenz", np.log(rq[m])), ("exponentiell", rq[m])):
        A = np.column_stack([np.ones_like(X), X]); c, *_ = np.linalg.lstsq(A, Y, rcond=None)
        out[name] = dict(steigung=float(c[1]), rss=float(np.sum((Y - A @ c) ** 2)))
    out["p"] = -out["potenz"]["steigung"] / k2
    lam = -out["exponentiell"]["steigung"] / k2
    out["xi"] = 1.0 / lam if lam > 0 else None
    out["xi_kanten"] = out["xi"] / KANTE if out["xi"] else None
    out["exp_besser"] = bool(out["exponentiell"]["rss"] < out["potenz"]["rss"])
    return out


aus = {}
for netz, groesse in (("B", "R2"), ("A", "D")):
    laeufe = [np.load(f) for f in sorted(glob.glob(os.path.join(ordner, "korr_%s_L%d_s*.npz" % (netz, L))))]
    if not laeufe:
        continue
    r = np.sqrt(laeufe[0]["r2"]) / 8.0
    erg = []
    for r1 in (0.8, 0.9, 1.0, 1.2):
        for b in (0.25, 0.5):
            k = kanten_ringe(r1, 0.25 * L, b); j = idx(r, k); nr = len(k) - 1
            ys = []; ss = []; rq = None
            for d in laeufe:
                if groesse == "R2":
                    den = d["den_bar"]; ok = (j >= 0) & (den > 0)
                    ds = np.bincount(j[ok], weights=den[ok], minlength=nr); dn = np.where(ds > 0, ds, 1)
                    rq = np.bincount(j[ok], weights=(den * r)[ok], minlength=nr) / dn
                    y = np.bincount(j[ok], weights=(den * d["R2_alle"])[ok], minlength=nr) / dn
                    jk = np.array([np.bincount(j[ok], weights=(den * x)[ok], minlength=nr) / dn for x in d["R2_alle_jk"]])
                    B = len(jk); s = np.sqrt((B - 1) / B * ((jk - jk.mean(0)) ** 2).sum(0))
                    y = np.where(ds > 0, y, np.nan)
                else:
                    den = d["den_d"]; ok = (j >= 0) & (den > 1e-12)
                    ds = np.bincount(j[ok], weights=den[ok], minlength=nr); dn = np.where(ds > 0, ds, 1)
                    rq = np.bincount(j[ok], weights=(den * r)[ok], minlength=nr) / dn
                    v = np.array([np.bincount(j[ok], weights=x[ok], minlength=nr) for x in d["num_d"]]) / dn
                    y = np.where(ds > 0, v.mean(0), np.nan); s = v.std(0, ddof=1) / np.sqrt(len(v))
                ys.append(y); ss.append(s)
            y = np.mean(ys, 0); s = np.sqrt((np.array(ss) ** 2).sum(0)) / len(ss)
            erg.append(dict(r1=r1, breite=b, ringe=int(nr), fit=logfit(rq, y, s, 2.0 if groesse == "R2" else 1.0)))
    aus[netz] = erg
json.dump(aus, open(ausgabe, "w"), indent=1)
for netz, erg in aus.items():
    for e in erg:
        f = e["fit"]
        print(netz, e["r1"], e["breite"], f.get("ringe_signifikant"), f.get("p"), f.get("xi"),
              f.get("exp_besser"), f.get("potenz", {}).get("rss"), f.get("exponentiell", {}).get("rss"))
