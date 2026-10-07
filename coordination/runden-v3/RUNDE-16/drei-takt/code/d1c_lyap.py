#!/usr/bin/env python3
"""D1c (Runde 16, drei-takt): endliche Lyapunov-Zahl nahe L4 im elliptischen eingeschraenkten Problem.

Pulsierende Koordinaten, wahre Anomalie f als Zeit:
  x'' - 2 y' = Om_x / (1 + e cos f),  y'' + 2 x' = Om_y / (1 + e cos f)
  Om = (x^2 + y^2)/2 + (1-mu)/r1 + mu/r2
Tangente mit analytischer Hesse-Matrix, Benettin mit Renormierung je Umlauf. Einheit: je Bogenmass f.

Aufruf: python d1c_lyap.py <voll | rauch> <ausgabeordner>
"""
import sys, os, json, time
import numpy as np

MUS = [0.001, 0.01, 0.02, 0.03]
ES = [0.0, 0.05, 0.1, 0.2]


def main():
    modus = sys.argv[1]; aus = sys.argv[2]
    os.makedirs(aus, exist_ok=True)
    spu, uml = (400, 1000) if modus == "voll" else (100, 10)
    deltas = [0.005, 0.02]; ri = np.arange(4) * np.pi / 2
    MU, E, DE, RI = np.meshgrid(np.array(MUS), np.array(ES), np.array(deltas), ri, indexing="ij")
    shp = MU.shape
    mu = MU.ravel(); e = E.ravel(); de = DE.ravel(); r = RI.ravel()
    xL = 0.5 - mu; yL = np.sqrt(3) / 2
    x = xL + de * np.cos(r); y = yL + de * np.sin(r); u = np.zeros_like(x); v = np.zeros_like(x)
    rng = np.random.default_rng(7)
    w = rng.normal(size=(4, x.size)); w /= np.linalg.norm(w, axis=0)
    P = x.size
    idx = np.arange(P)
    summe = np.zeros(P); ende = np.full(P, np.nan); dmax = de.copy()
    h = 2 * np.pi / spu
    s3 = 3.0

    def rhs(f, x, y, u, v, w0, w1, w2, w3, mu, e):
        g = 1.0 / (1.0 + e * np.cos(f))
        d1 = x + mu; d2 = x - 1 + mu; y2 = y * y
        r1s = d1 * d1 + y2; r2s = d2 * d2 + y2
        i1 = 1 / np.sqrt(r1s); i2 = 1 / np.sqrt(r2s)
        q1 = (1 - mu) * i1 ** 3; q2 = mu * i2 ** 3
        p1 = s3 * (1 - mu) * i1 ** 5; p2 = s3 * mu * i2 ** 5
        Ox = x - q1 * d1 - q2 * d2
        Oy = y - (q1 + q2) * y
        Oxx = 1 - q1 - q2 + p1 * d1 * d1 + p2 * d2 * d2
        Oyy = 1 - q1 - q2 + (p1 + p2) * y2
        Oxy = (p1 * d1 + p2 * d2) * y
        return (u, v, 2 * v + g * Ox, -2 * u + g * Oy,
                w2, w3, 2 * w3 + g * (Oxx * w0 + Oxy * w1), -2 * w2 + g * (Oxy * w0 + Oyy * w1))

    t0 = time.time()
    st = [x, y, u, v, w[0], w[1], w[2], w[3]]
    mu_a = mu.copy(); e_a = e.copy(); xLa = xL.copy()
    with np.errstate(all="ignore"):
        for k_uml in range(uml):
            for k in range(spu):
                f = (k_uml * spu + k) * h
                k1 = rhs(f, *st, mu_a, e_a)
                k2 = rhs(f + 0.5 * h, *[a + 0.5 * h * b for a, b in zip(st, k1)], mu_a, e_a)
                k3 = rhs(f + 0.5 * h, *[a + 0.5 * h * b for a, b in zip(st, k2)], mu_a, e_a)
                k4 = rhs(f + h, *[a + h * b for a, b in zip(st, k3)], mu_a, e_a)
                st = [a + (h / 6) * (b1 + 2 * b2 + 2 * b3 + b4) for a, b1, b2, b3, b4 in zip(st, k1, k2, k3, k4)]
            x, y = st[0], st[1]
            dL = np.sqrt((x - xLa) ** 2 + (y - yL) ** 2)
            r2s = (x - 1 + mu_a) ** 2 + y * y
            dmax[idx] = np.maximum(dmax[idx], dL)
            nw = np.sqrt(st[4] ** 2 + st[5] ** 2 + st[6] ** 2 + st[7] ** 2)
            summe[idx] += np.log(nw)
            for j in range(4, 8):
                st[j] = st[j] / nw
            r1s = (x + mu_a) ** 2 + y * y
            tot = (x * x + y * y > 9.0) | (r1s < 0.0025) | (r2s < 0.0025) | ~np.isfinite(dL)
            if tot.any():
                ende[idx[tot]] = k_uml + 1
                keep = ~tot
                idx = idx[keep]; st = [a[keep] for a in st]; mu_a = mu_a[keep]; e_a = e_a[keep]; xLa = xLa[keep]
                if idx.size == 0:
                    break
    sek = time.time() - t0
    T = np.where(np.isnan(ende), uml, ende) * 2 * np.pi
    lam = summe / T
    lam = lam.reshape(shp); ende = ende.reshape(shp); dmax = dmax.reshape(shp)
    np.savez_compressed(os.path.join(aus, f"d1c_{modus}.npz"), mus=np.array(MUS), es=np.array(ES), deltas=np.array(deltas),
                        lam=lam, ende=ende, dmax=dmax)
    tab = []
    for i, m in enumerate(MUS):
        for j, ev in enumerate(ES):
            l = lam[i, j]; en = ende[i, j]; gef = np.isnan(en)
            tab.append(dict(mu=m, e=ev, gefangen=int(gef.sum()), von=int(gef.size),
                            lam_mittel_gefangene=float(l[gef].mean()) if gef.any() else None,
                            lam_max_gefangene=float(l[gef].max()) if gef.any() else None,
                            lam_mittel_d0005=float(l[:, :][0][gef[0]].mean()) if gef[0].any() else None,
                            lam_mittel_d002=float(l[1][gef[1]].mean()) if gef[1].any() else None,
                            dmax_gefangene=float(dmax[i, j][gef].max()) if gef.any() else None))
    res = dict(modus=modus, sek=sek, schritte_je_umlauf=spu, umlaeufe=uml, tabelle=tab,
               referenz_regulaer_ln_T_durch_T=float(np.log(uml * 2 * np.pi) / (uml * 2 * np.pi)))
    with open(os.path.join(aus, f"d1c_{modus}.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1)[:6000])


if __name__ == "__main__":
    main()
