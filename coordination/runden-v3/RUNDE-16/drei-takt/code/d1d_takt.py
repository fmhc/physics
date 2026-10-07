#!/usr/bin/env python3
"""D1d (Runde 16, drei-takt): L4 bei e = 0, U-Terme mal (1 + eps cos(Omega t)), Floquet ueber 2 pi/Omega.

  x'' - 2 y' = (Uxx x + Uxy y)(1 + eps cos Omega t)
  y'' + 2 x' = (Uxy x + Uyy y)(1 + eps cos Omega t)
Zeit tau = Omega t (Periode 2 pi), d/dtau = (1/Omega) d/dt, Zustand (x, y, dx/dt, dy/dt).

Aufruf: python d1d_takt.py <ausgabeordner> <mu-Liste, Komma> <faktor 1|2> [rauch]
"""
import sys, os, json, time
import numpy as np

UXX = 0.75
UYY = 2.25
TOL = 1e-6
MU_R = (1 - np.sqrt(69) / 9) / 2


def monodromie_block(mu, eps, Om, n):
    # mu, eps, Om: 1D gleich lang
    m = mu.size
    b = ((3 * np.sqrt(3) / 4) * (1 - 2 * mu))[:, None]
    ep = eps[:, None]; iO = (1.0 / Om)[:, None]
    x = np.zeros((m, 4)); y = np.zeros((m, 4)); u = np.zeros((m, 4)); v = np.zeros((m, 4))
    x[:, 0] = 1; y[:, 1] = 1; u[:, 2] = 1; v[:, 3] = 1
    h = 2 * np.pi / n

    def d(tau, x, y, u, v):
        g = 1.0 + ep * np.cos(tau)
        return iO * u, iO * v, iO * (2 * v + g * (UXX * x + b * y)), iO * (-2 * u + g * (b * x + UYY * y))

    for k in range(n):
        t0 = k * h
        k1 = d(t0, x, y, u, v)
        k2 = d(t0 + 0.5 * h, x + 0.5 * h * k1[0], y + 0.5 * h * k1[1], u + 0.5 * h * k1[2], v + 0.5 * h * k1[3])
        k3 = d(t0 + 0.5 * h, x + 0.5 * h * k2[0], y + 0.5 * h * k2[1], u + 0.5 * h * k2[2], v + 0.5 * h * k2[3])
        k4 = d(t0 + h, x + h * k3[0], y + h * k3[1], u + h * k3[2], v + h * k3[3])
        x = x + (h / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        y = y + (h / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        u = u + (h / 6) * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
        v = v + (h / 6) * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
    M = np.empty((m, 4, 4))
    M[:, 0, :] = x; M[:, 1, :] = y; M[:, 2, :] = u; M[:, 3, :] = v
    return M


def eigenfrequenzen(mu):
    c = (27 / 4) * mu * (1 - mu)
    disk = 1 - 4 * c
    if disk < 0:
        return None
    s1 = np.sqrt((1 + np.sqrt(disk)) / 2); s2 = np.sqrt((1 - np.sqrt(disk)) / 2)
    return float(s1), float(s2)


def resonanzen(s1, s2):
    r = []
    for n in range(1, 5):
        r.append((f"2 s1/{n}", 2 * s1 / n)); r.append((f"2 s2/{n}", 2 * s2 / n))
    for n in range(1, 4):
        r.append((f"(s1-s2)/{n}", (s1 - s2) / n)); r.append((f"(s1+s2)/{n}", (s1 + s2) / n))
    return r


def main():
    aus = sys.argv[1]
    mu_liste = [float(z) for z in sys.argv[2].split(",")]
    faktor = int(sys.argv[3])
    rauch = len(sys.argv) > 4 and sys.argv[4] == "rauch"
    os.makedirs(aus, exist_ok=True)
    if rauch:
        Oms = np.array([0.5, 1.0, 2.0, 8.0]); epss = np.array([0.0, 0.3]); h_t = 0.05; nmin = 100
    else:
        Oms = np.round(np.arange(0.2, 10.0 + 1e-9, 0.01), 4); epss = np.round(np.arange(0, 0.3 + 1e-9, 0.005), 4)
        h_t = 0.01; nmin = 400
    t_start = time.time()
    maxabs = np.empty((len(mu_liste), len(epss), len(Oms)))
    det = np.empty_like(maxabs)
    chunk = 10
    for c0 in range(0, len(Oms), chunk):
        Oc = Oms[c0:c0 + chunk]
        n = max(nmin, int(np.ceil(2 * np.pi / (Oc.min() * h_t)))) * faktor
        MU, EP, OM = np.meshgrid(np.array(mu_liste), epss, Oc, indexing="ij")
        M = monodromie_block(MU.ravel(), EP.ravel(), OM.ravel(), n)
        rho = np.linalg.eigvals(M)
        maxabs[:, :, c0:c0 + chunk] = np.abs(rho).max(axis=1).reshape(MU.shape)
        det[:, :, c0:c0 + chunk] = np.linalg.det(M).reshape(MU.shape)
    sek = time.time() - t_start
    tag = "_".join(f"{m:.4f}" for m in mu_liste) + f"_f{faktor}" + ("_rauch" if rauch else "")
    np.savez_compressed(os.path.join(aus, f"d1d_{tag}.npz"), mus=np.array(mu_liste), epss=epss, Oms=Oms,
                        maxabs=maxabs, det=det)
    res = dict(mu_liste=mu_liste, faktor=faktor, sek=sek, max_det_minus_1=float(np.max(np.abs(det - 1))))
    st = maxabs <= 1 + TOL
    proMu = {}
    for i, mu in enumerate(mu_liste):
        e = dict()
        ef = eigenfrequenzen(mu)
        e["s1_s2"] = ef
        e["eps0_alle_stabil"] = bool(st[i, 0].all())
        e["eps0_alle_instabil"] = bool((~st[i, 0]).all())
        if mu > MU_R:
            ok = st[i, 1:]
            e["stabile_punkte_eps_gt_0"] = int(ok.sum())
            if ok.any():
                jj, kk = np.nonzero(ok)
                e["stabil_Omega_bereich"] = [float(Oms[kk].min()), float(Oms[kk].max())]
                e["stabil_eps_bereich"] = [float(epss[1:][jj].min()), float(epss[1:][jj].max())]
                # zusammenhaengende Omega-Intervalle bei jedem eps, kompakt: Liste je eps mit stabilen Omega-Intervallen
                iv = {}
                for j in range(1, len(epss)):
                    zeile = st[i, j]
                    if zeile.any():
                        iv[f"{epss[j]:.3f}"] = intervalle(Oms, zeile)
                e["stabil_intervalle_je_eps"] = iv
        else:
            zungen = {}
            for epsv in (0.1, 0.2, 0.3):
                j = int(np.argmin(np.abs(epss - epsv)))
                ivs = intervalle(Oms, ~st[i, j])
                lst = []
                for a, bb in ivs:
                    mitte = 0.5 * (a + bb)
                    if ef is not None:
                        lab, val = min(resonanzen(*ef), key=lambda r: abs(r[1] - mitte))
                    else:
                        lab, val = None, None
                    lst.append(dict(von=a, bis=bb, max_abs_rho=float(maxabs[i, j][(Oms >= a) & (Oms <= bb)].max()),
                                    naechste_resonanz=lab, resonanz_wert=val))
                zungen[f"{epss[j]:.3f}"] = lst
            e["instabil_intervalle"] = zungen
        proMu[f"{mu:.4f}"] = e
    res["pro_mu"] = proMu
    with open(os.path.join(aus, f"d1d_{tag}.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1)[:6000])


def intervalle(xs, maske):
    out = []
    i = 0
    n = len(xs)
    while i < n:
        if maske[i]:
            j = i
            while j + 1 < n and maske[j + 1]:
                j += 1
            out.append([float(xs[i]), float(xs[j])])
            i = j + 1
        else:
            i += 1
    return out


if __name__ == "__main__":
    main()
