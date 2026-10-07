#!/usr/bin/env python3
"""D1b (Runde 16, drei-takt): Lebensdauer nahe L4 oberhalb der Routh-Grenze, kreisfoermiges eingeschraenktes Problem.

Mitrotierendes System, m1 = 1 - mu bei (-mu, 0), m2 = mu bei (1 - mu, 0), L4 = (1/2 - mu, sqrt3/2).
  x'' - 2 y' = x - (1-mu)(x+mu)/r1^3 - mu (x-1+mu)/r2^3
  y'' + 2 x' = y - (1-mu) y/r1^3 - mu y/r2^3
Jacobi: C = x^2 + y^2 + 2(1-mu)/r1 + 2 mu/r2 - (x'^2 + y'^2)

Aufruf: python d1b_lebensdauer.py <haupt | halb | rauch> <ausgabeordner>
"""
import sys, os, json, time
import numpy as np

MU_R = (1 - np.sqrt(69) / 9) / 2
MUS = [0.0386, 0.0387, 0.0388, 0.0390, 0.0393, 0.0396, 0.0400, 0.0405, 0.0410, 0.0420, 0.0430, 0.0440, 0.0450,
       0.0475, 0.0500]


def jacobi(x, y, u, v, mu):
    r1 = np.sqrt((x + mu) ** 2 + y ** 2); r2 = np.sqrt((x - 1 + mu) ** 2 + y ** 2)
    return x * x + y * y + 2 * (1 - mu) / r1 + 2 * mu / r2 - (u * u + v * v)


def lauf(mu, delta, richt, schritte_je_umlauf, umlaeufe):
    xL = 0.5 - mu; yL = np.sqrt(3) / 2
    x = xL + delta * np.cos(richt); y = yL + delta * np.sin(richt)
    u = np.zeros_like(x); v = np.zeros_like(x)
    C0 = jacobi(x, y, u, v, mu)
    P = x.size
    ende = np.full(P, np.nan)       # Lebensdauer in Umlaeufen
    grund = np.zeros(P, int)        # 1 = Abstand > 0.5, 2 = r2 < 0.05
    dmax = np.full(P, delta, float)
    Cend = np.full(P, np.nan)
    idx = np.arange(P)
    mu_a = mu.copy(); xLa = xL.copy()
    dt = 2 * np.pi / schritte_je_umlauf
    nsch = schritte_je_umlauf * umlaeufe

    def acc(x, y, u, v, mu):
        d1 = x + mu; d2 = x - 1 + mu; y2 = y * y
        r1s = d1 * d1 + y2; r2s = d2 * d2 + y2
        q1 = (1 - mu) / (r1s * np.sqrt(r1s)); q2 = mu / (r2s * np.sqrt(r2s))
        return 2 * v + x - q1 * d1 - q2 * d2, -2 * u + y - (q1 + q2) * y

    with np.errstate(all="ignore"):
        for k in range(nsch):
            a1, b1 = acc(x, y, u, v, mu_a)
            x2 = x + 0.5 * dt * u; y2 = y + 0.5 * dt * v; u2 = u + 0.5 * dt * a1; v2 = v + 0.5 * dt * b1
            a2, b2 = acc(x2, y2, u2, v2, mu_a)
            x3 = x + 0.5 * dt * u2; y3 = y + 0.5 * dt * v2; u3 = u + 0.5 * dt * a2; v3 = v + 0.5 * dt * b2
            a3, b3 = acc(x3, y3, u3, v3, mu_a)
            x4 = x + dt * u3; y4 = y + dt * v3; u4 = u + dt * a3; v4 = v + dt * b3
            a4, b4 = acc(x4, y4, u4, v4, mu_a)
            x = x + (dt / 6) * (u + 2 * u2 + 2 * u3 + u4)
            y = y + (dt / 6) * (v + 2 * v2 + 2 * v3 + v4)
            u = u + (dt / 6) * (a1 + 2 * a2 + 2 * a3 + a4)
            v = v + (dt / 6) * (b1 + 2 * b2 + 2 * b3 + b4)
            dL2 = (x - xLa) ** 2 + (y - yL) ** 2
            r2s = (x - 1 + mu_a) ** 2 + y * y
            dmax[idx] = np.maximum(dmax[idx], np.sqrt(dL2))
            tot = (dL2 > 0.25) | (r2s < 0.0025) | ~np.isfinite(dL2)
            if tot.any():
                gi = idx[tot]
                ende[gi] = (k + 1) / schritte_je_umlauf
                grund[gi] = np.where(r2s[tot] < 0.0025, 2, 1)
                Cend[gi] = jacobi(x[tot], y[tot], u[tot], v[tot], mu_a[tot])
                keep = ~tot
                idx = idx[keep]; x = x[keep]; y = y[keep]; u = u[keep]; v = v[keep]; mu_a = mu_a[keep]; xLa = xLa[keep]
                if idx.size == 0:
                    break
        if idx.size:
            Cend[idx] = jacobi(x, y, u, v, mu_a)
    return ende, grund, dmax, C0, Cend


def main():
    modus = sys.argv[1]; aus = sys.argv[2]
    os.makedirs(aus, exist_ok=True)
    if modus == "haupt":
        mus = MUS; deltas = [0.005, 0.02]; nr = 64; spu = 400; uml = 1000; ri = np.arange(nr) * 2 * np.pi / nr
    elif modus == "halb":
        mus = [0.0386, 0.0390, 0.0420]; deltas = [0.005, 0.02]; spu = 800; uml = 1000
        ri = np.arange(0, 64, 4) * 2 * np.pi / 64
    elif modus == "kontrolle":
        # PLAN-NACHTRAG-3: gleiches Protokoll unterhalb mu_R (linear stabil)
        mus = [0.030, 0.035, 0.038]; deltas = [0.005, 0.02]; nr = 64; spu = 400; uml = 1000
        ri = np.arange(nr) * 2 * np.pi / nr
    elif modus == "rauch":
        mus = [0.0386, 0.045]; deltas = [0.005, 0.02]; spu = 100; uml = 20; ri = np.arange(0, 64, 16) * 2 * np.pi / 64
    else:
        raise SystemExit("modus")
    MU, DE, RI = np.meshgrid(np.array(mus), np.array(deltas), ri, indexing="ij")
    t0 = time.time()
    ende, grund, dmax, C0, Cend = lauf(MU.ravel(), DE.ravel(), RI.ravel(), spu, uml)
    sek = time.time() - t0
    shp = MU.shape
    ende = ende.reshape(shp); grund = grund.reshape(shp); dmax = dmax.reshape(shp)
    relC = (np.abs(Cend - C0) / np.abs(C0)).reshape(shp)
    np.savez_compressed(os.path.join(aus, f"d1b_{modus}.npz"), mus=np.array(mus), deltas=np.array(deltas), richt=ri,
                        ende=ende, grund=grund, dmax=dmax, relC=relC, spu=spu, uml=uml)
    zeilen = []
    for i, mu in enumerate(mus):
        c = (27 / 4) * mu * (1 - mu)
        lam = np.roots([1, 0, 1, 0, c]); re = float(np.max(lam.real))
        for j, de in enumerate(deltas):
            e = ende[i, j]; gef = np.isnan(e)
            z = dict(mu=mu, delta=de, mu_minus_muR=mu - MU_R, re_lambda=re,
                     T_lin_umlaeufe=float(np.log(0.5 / de) / re / (2 * np.pi)) if re > 0 else None,
                     anteil_gefangen=float(gef.mean()),
                     median_lebensdauer=(lambda m: float(m) if np.isfinite(m) else None)(np.median(np.where(gef, np.inf, e))),
                     min_lebensdauer=float(np.nanmin(e)) if (~gef).any() else None,
                     max_lebensdauer_entkommen=float(np.nanmax(e)) if (~gef).any() else None,
                     anteil_grund_r2=float((grund[i, j] == 2).mean()),
                     dmax_gefangene_max=float(dmax[i, j][gef].max()) if gef.any() else None,
                     dmax_gefangene_median=float(np.median(dmax[i, j][gef])) if gef.any() else None,
                     relC_gefangene_max=float(relC[i, j][gef].max()) if gef.any() else None,
                     relC_alle_median=float(np.median(relC[i, j])))
            zeilen.append(z)
    # Fit nur ueber (mu, delta) mit allen entkommen
    fit = {}
    for j, de in enumerate(deltas):
        a = []; T = []
        for i, mu in enumerate(mus):
            e = ende[i, j]
            if not np.isnan(e).any():
                a.append(mu - MU_R); T.append(np.median(e))
        if len(a) >= 3:
            fit[str(de)] = dict(steigung=float(np.polyfit(np.log(a), np.log(T), 1)[0]), punkte=len(a),
                                mu_min=float(min(a) + MU_R))
    res = dict(modus=modus, sek=sek, schritte_je_umlauf=spu, umlaeufe=uml, zeilen=zeilen, fit_alle_entkommen=fit)
    with open(os.path.join(aus, f"d1b_{modus}.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1)[:8000])


if __name__ == "__main__":
    main()
