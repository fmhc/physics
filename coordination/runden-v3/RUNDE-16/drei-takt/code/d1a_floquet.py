#!/usr/bin/env python3
"""D1a (Runde 16, drei-takt): Floquet-Stabilitaet von L4 im elliptischen eingeschraenkten Dreikoerperproblem, linear.

Gleichungen (pulsierende Koordinaten, wahre Anomalie f als Zeit), wie KARTE.md:
  x'' - 2 y' = (Uxx x + Uxy y) / (1 + e cos f)
  y'' + 2 x' = (Uxy x + Uyy y) / (1 + e cos f)
  Uxx = 3/4, Uyy = 9/4, Uxy = (3 sqrt3 / 4)(1 - 2 mu)

Aufruf: python d1a_floquet.py <modus: A | B | rauch> <ausgabeordner>
"""
import sys, os, json, time
import numpy as np

UXX = 0.75
UYY = 2.25
TOL = 1e-6
MU_R = (1 - np.sqrt(69) / 9) / 2
MU_Z = (1 - np.sqrt(8 / 9)) / 2


def monodromie(mu, e, n, chunk=8192):
    mu = np.asarray(mu, float).ravel()
    e = np.asarray(e, float).ravel()
    P = mu.size
    M = np.empty((P, 4, 4))
    h = 2 * np.pi / n
    for s in range(0, P, chunk):
        sl = slice(s, min(P, s + chunk))
        m = mu[sl].size
        b = ((3 * np.sqrt(3) / 4) * (1 - 2 * mu[sl]))[:, None]
        ee = e[sl][:, None]
        x = np.zeros((m, 4)); y = np.zeros((m, 4)); u = np.zeros((m, 4)); v = np.zeros((m, 4))
        x[:, 0] = 1; y[:, 1] = 1; u[:, 2] = 1; v[:, 3] = 1

        def acc(f, x, y, u, v):
            g = 1.0 / (1.0 + ee * np.cos(f))
            return 2 * v + g * (UXX * x + b * y), -2 * u + g * (b * x + UYY * y)

        for k in range(n):
            f0 = k * h
            a1, c1 = acc(f0, x, y, u, v)
            x2 = x + 0.5 * h * u; y2 = y + 0.5 * h * v; u2 = u + 0.5 * h * a1; v2 = v + 0.5 * h * c1
            a2, c2 = acc(f0 + 0.5 * h, x2, y2, u2, v2)
            x3 = x + 0.5 * h * u2; y3 = y + 0.5 * h * v2; u3 = u + 0.5 * h * a2; v3 = v + 0.5 * h * c2
            a3, c3 = acc(f0 + 0.5 * h, x3, y3, u3, v3)
            x4 = x + h * u3; y4 = y + h * v3; u4 = u + h * a3; v4 = v + h * c3
            a4, c4 = acc(f0 + h, x4, y4, u4, v4)
            x = x + (h / 6) * (u + 2 * u2 + 2 * u3 + u4)
            y = y + (h / 6) * (v + 2 * v2 + 2 * v3 + v4)
            u = u + (h / 6) * (a1 + 2 * a2 + 2 * a3 + a4)
            v = v + (h / 6) * (c1 + 2 * c2 + 2 * c3 + c4)
        M[sl, 0, :] = x; M[sl, 1, :] = y; M[sl, 2, :] = u; M[sl, 3, :] = v
    return M


def kennzahlen(M):
    rho = np.linalg.eigvals(M)
    maxabs = np.abs(rho).max(axis=1)
    det = np.linalg.det(M)
    # Gegenprobe ueber das charakteristische Polynom einer symplektischen 4x4-Matrix:
    # rho^4 - a1 rho^3 + a2 rho^2 - a1 rho + 1, sigma = rho + 1/rho: sigma^2 - a1 sigma + (a2 - 2) = 0
    tr = np.trace(M, axis1=1, axis2=2)
    tr2 = np.trace(M @ M, axis1=1, axis2=2)
    a1 = tr
    a2 = 0.5 * (tr ** 2 - tr2)
    D = (a1 ** 2 - 4 * (a2 - 2)).astype(complex)
    sq = np.sqrt(D)
    best = np.zeros(M.shape[0])
    for sig in (0.5 * (a1 + sq), 0.5 * (a1 - sq)):
        w = np.sqrt(sig * sig - 4)
        for r in ((sig + w) / 2, (sig - w) / 2):
            best = np.maximum(best, np.abs(r))
    return rho, maxabs, det, best


def uebergaenge(mus, stabil_zeile):
    out = []
    for i in range(len(mus) - 1):
        if stabil_zeile[i] != stabil_zeile[i + 1]:
            out.append([float(mus[i]), float(mus[i + 1]), "stabil->instabil" if stabil_zeile[i] else "instabil->stabil"])
    return out


def gitter_lauf(mus, es, n):
    MU, E = np.meshgrid(mus, es, indexing="xy")  # Form (len(es), len(mus))
    t0 = time.time()
    M = monodromie(MU.ravel(), E.ravel(), n)
    rho, maxabs, det, best = kennzahlen(M)
    dt = time.time() - t0
    shp = MU.shape
    return dict(maxabs=maxabs.reshape(shp), det=det.reshape(shp), best=best.reshape(shp), sek=dt)


def bisektion(e_liste, mus, stabil, es, n=4000, schritte=14):
    # Uebergaenge je e aus dem Gitter (Zeile mit naechstem e) und Bisektion in mu bei exakt diesem e
    paare = []
    for ev in e_liste:
        j = int(np.argmin(np.abs(es - ev)))
        for lo, hi, art in uebergaenge(mus, stabil[j]):
            paare.append([ev, lo, hi, art])
    if not paare:
        return []
    ev = np.array([p[0] for p in paare]); lo = np.array([p[1] for p in paare]); hi = np.array([p[2] for p in paare])
    s_lo = np.array([p[3].startswith("stabil") for p in paare])  # Zustand am linken Rand
    for _ in range(schritte):
        mid = 0.5 * (lo + hi)
        M = monodromie(mid, ev, n)
        _, mx, _, _ = kennzahlen(M)
        st = mx <= 1 + TOL
        gleich = st == s_lo
        lo = np.where(gleich, mid, lo)
        hi = np.where(gleich, hi, mid)
    return [[float(ev[i]), float(0.5 * (lo[i] + hi[i])), float(hi[i] - lo[i]), paare[i][3]] for i in range(len(paare))]


def kontrollen_e0(n=4000):
    mus = np.array([0.001, 0.01, 0.02, MU_Z, 0.035, 0.038, 0.039, 0.045])
    M = monodromie(mus, np.zeros_like(mus), n)
    rho, mx, det, best = kennzahlen(M)
    erg = []
    for i, mu in enumerate(mus):
        c = (27 / 4) * mu * (1 - mu)
        lam = np.roots([1, 0, 1, 0, c])
        ana = np.exp(2 * np.pi * lam)
        num = rho[i]
        d = max(np.min(np.abs(num - a)) for a in ana)
        erg.append(dict(mu=float(mu), max_abstand_multiplikatoren=float(d), max_abs_rho=float(mx[i]),
                        det_minus_1=float(det[i] - 1), rho=[[float(z.real), float(z.imag)] for z in num]))
    return erg


def main():
    modus = sys.argv[1]
    aus = sys.argv[2]
    os.makedirs(aus, exist_ok=True)
    t_start = time.time()
    res = dict(modus=modus, tol=TOL, mu_R=MU_R, mu_Zunge=MU_Z)
    if modus == "rauch":
        mus = np.linspace(0, 0.06, 7); es = np.linspace(0, 0.6, 5)
        g = gitter_lauf(mus, es, 400)
        res["rauch_sek"] = g["sek"]
        res["kontrollen_e0"] = kontrollen_e0(n=400)
        b = bisektion([0.0], mus, g["maxabs"] <= 1 + TOL, es, n=400, schritte=10)
        res["bisekt_e0"] = b
        print(json.dumps(res, indent=1)[:3000])
        return
    if modus == "A":
        mus = np.round(np.arange(0, 0.06 + 1e-12, 0.0005), 6); es = np.round(np.arange(0, 0.6 + 1e-12, 0.005), 6)
    elif modus == "B":
        mus = np.round(np.arange(0, 0.06 + 1e-12, 0.00025), 6); es = np.round(np.arange(0, 0.6 + 1e-12, 0.0025), 6)
    else:
        raise SystemExit("modus A oder B")
    g2 = gitter_lauf(mus, es, 2000)
    g4 = gitter_lauf(mus, es, 4000)
    st2 = g2["maxabs"] <= 1 + TOL
    st4 = g4["maxabs"] <= 1 + TOL
    st2_tol4 = g2["maxabs"] <= 1 + 1e-4
    st2_br = g2["best"] <= 1 + TOL
    np.savez_compressed(os.path.join(aus, f"d1a_{modus}.npz"), mus=mus, es=es, maxabs2000=g2["maxabs"],
                        maxabs4000=g4["maxabs"], det2000=g2["det"], best2000=g2["best"])
    res.update(dict(
        n_mu=len(mus), n_e=len(es), sek_n2000=g2["sek"], sek_n4000=g4["sek"],
        abweichung_n2000_n4000=int((st2 != st4).sum()),
        abweichung_tol1e6_tol1e4=int((st2 != st2_tol4).sum()),
        abweichung_eigvals_polynom=int((st2 != st2_br).sum()),
        max_det_minus_1=float(np.max(np.abs(g2["det"] - 1))),
        max_det_minus_1_n4000=float(np.max(np.abs(g4["det"] - 1))),
        max_abs_maxabs_diff_n2000_n4000=float(np.max(np.abs(g2["maxabs"] - g4["maxabs"]))),
    ))
    # D1a-1: stabil bei e = 0, instabil bei e > 0 (mu < mu_R)
    st0 = st4[0]
    res["d1a_1_punkte_mu_unter_muR_e0_stabil_aber_e_instabil"] = int(((~st4[1:]) & st0[None, :] & (mus[None, :] < MU_R)).sum())
    # D1a-2: stabil bei mu > mu_R und e > 0
    ober = (mus[None, :] > MU_R) & (es[:, None] > 0)
    res["d1a_2_stabile_punkte_mu_ueber_muR_n2000"] = int((st2 & ober).sum())
    res["d1a_2_stabile_punkte_mu_ueber_muR_n4000"] = int((st4 & ober).sum())
    if (st4 & ober).any():
        jj, ii = np.nonzero(st4 & ober)
        res["d1a_2_groesstes_mu_stabil"] = float(mus[ii].max())
        k = int(np.argmax(mus[ii]))
        res["d1a_2_e_bei_groesstem_mu"] = float(es[jj][k])
        res["d1a_2_e_bereich"] = [float(es[jj].min()), float(es[jj].max())]
    # Grenzen je ausgewaehltem e
    e_sel = [0.0, 0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
    gr = {}
    for ev in e_sel:
        j = int(np.argmin(np.abs(es - ev)))
        gr[f"{es[j]:.4f}"] = uebergaenge(mus, st4[j])
    res["grenzen_gitter_n4000"] = gr
    if modus == "A":
        e_bis = [0.0, 0.005, 0.01] + [round(0.02 * k, 4) for k in range(1, 31)]
        t0 = time.time()
        res["bisektion_n4000"] = bisektion(e_bis, mus, st4, es, n=4000, schritte=14)
        res["bisektion_sek"] = time.time() - t0
        res["kontrollen_e0"] = kontrollen_e0(n=4000)
    res["laufzeit_sek"] = time.time() - t_start
    with open(os.path.join(aus, f"d1a_{modus}.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k not in ("grenzen_gitter_n4000", "bisektion_n4000", "kontrollen_e0")}, indent=1))


if __name__ == "__main__":
    main()
