#!/usr/bin/env python3
"""D3 (Runde 16, drei-takt): groesster Lyapunov-Exponent im Kuramoto-Sakaguchi-Modell mit aeusserem Takt.

Mitlaufendes Bild phi_i = theta_i - Omega t (autonom):
  phi_i' = (omega_i - Omega) + (K/N) sum_j sin(phi_j - phi_i - alpha) - F sin(phi_i)     (Summe mit j = i)
Tangente (Mittelfeldform):
  (J v)_i = (K/N) [ (Wc - C v_i) cos(phi_i + alpha) + (Ws - S v_i) sin(phi_i + alpha) ] - F cos(phi_i) v_i
  C = sum cos phi, S = sum sin phi, Wc = sum v cos phi, Ws = sum v sin phi.

Aufruf:
  python d3_kuramoto.py stichprobe <N> <takt 0|1> <P> <seed> <ausgabeordner> [dt T_ein T_mess]
  python d3_kuramoto.py nachrechnen <eingabe.npz> <ausgabeordner> [max_treffer]
"""
import sys, os, json, time
import numpy as np


def ziehe_parameter(N, takt, P, seed):
    rng = np.random.default_rng(seed)
    K = rng.uniform(0, 4, P)
    al = rng.uniform(0, 1.5, P)
    F = rng.uniform(0, 2, P) if takt else np.zeros(P)
    s = rng.uniform(0, 2, P)
    u = rng.uniform(-0.5, 0.5, (P, N))
    om = s[:, None] * u
    d = rng.uniform(-2, 2, P) if takt else np.zeros(P)
    Om = om.mean(axis=1) + d
    return dict(K=K, alpha=al, F=F, s=s, omega=om, Omega=Om, d=d)


def lyapunov(par, N, dt, T_ein, T_mess, seed_ab, renorm=1.0):
    K = par["K"][:, None]; al = par["alpha"][:, None]; F = par["F"][:, None]
    dom = par["omega"] - par["Omega"][:, None]
    P = dom.shape[0]
    rng = np.random.default_rng(seed_ab)
    phi = rng.uniform(0, 2 * np.pi, (P, N))
    v = rng.normal(size=(P, N)); v /= np.linalg.norm(v, axis=1, keepdims=True)
    ca = np.cos(al); sa = np.sin(al)
    KN = K / N

    def rhs(phi, v):
        c = np.cos(phi); s = np.sin(phi)
        C = c.sum(axis=1, keepdims=True); S = s.sum(axis=1, keepdims=True)
        cpa = c * ca - s * sa
        spa = s * ca + c * sa
        dphi = dom + KN * (S * cpa - C * spa) - F * s
        Wc = (v * c).sum(axis=1, keepdims=True); Ws = (v * s).sum(axis=1, keepdims=True)
        dv = KN * ((Wc - C * v) * cpa + (Ws - S * v) * spa) - F * c * v
        return dphi, dv

    def schritt(phi, v):
        k1, l1 = rhs(phi, v)
        k2, l2 = rhs(phi + 0.5 * dt * k1, v + 0.5 * dt * l1)
        k3, l3 = rhs(phi + 0.5 * dt * k2, v + 0.5 * dt * l2)
        k4, l4 = rhs(phi + dt * k3, v + dt * l3)
        return phi + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4), v + (dt / 6) * (l1 + 2 * l2 + 2 * l3 + l4)

    nr = int(round(renorm / dt))
    n_ein = int(round(T_ein / dt)) // nr
    n_mess = int(round(T_mess / dt)) // nr
    for _ in range(n_ein):
        for _ in range(nr):
            phi, v = schritt(phi, v)
        v /= np.linalg.norm(v, axis=1, keepdims=True)
    summe = np.zeros(P)
    for _ in range(n_mess):
        for _ in range(nr):
            phi, v = schritt(phi, v)
        nv = np.linalg.norm(v, axis=1)
        summe += np.log(nv)
        v /= nv[:, None]
    return summe / (n_mess * nr * dt)


def main():
    modus = sys.argv[1]
    if modus == "stichprobe":
        N = int(sys.argv[2]); takt = int(sys.argv[3]); P = int(sys.argv[4]); seed = int(sys.argv[5]); aus = sys.argv[6]
        dt = float(sys.argv[7]) if len(sys.argv) > 7 else 0.02
        T_ein = float(sys.argv[8]) if len(sys.argv) > 8 else 500.0
        T_mess = float(sys.argv[9]) if len(sys.argv) > 9 else 2000.0
        os.makedirs(aus, exist_ok=True)
        t0 = time.time()
        par = ziehe_parameter(N, takt, P, seed)
        lam = lyapunov(par, N, dt, T_ein, T_mess, seed_ab=seed + 1000)
        sek = time.time() - t0
        name = f"d3_N{N}_takt{takt}_P{P}_s{seed}"
        np.savez_compressed(os.path.join(aus, name + ".npz"), lam=lam, N=N, takt=takt, seed=seed, dt=dt,
                            T_ein=T_ein, T_mess=T_mess, **par)
        zus = dict(name=name, N=N, takt=takt, P=P, seed=seed, dt=dt, T_ein=T_ein, T_mess=T_mess, sek=sek,
                   lam_max=float(lam.max()), lam_min=float(lam.min()), lam_median=float(np.median(lam)),
                   anzahl_gt_0005=int((lam > 0.005).sum()), anzahl_gt_001=int((lam > 0.01).sum()),
                   anzahl_gt_005=int((lam > 0.05).sum()), anzahl_lt_m001=int((lam < -0.01).sum()),
                   top10=[float(x) for x in np.sort(lam)[-10:][::-1]])
        with open(os.path.join(aus, name + ".json"), "w") as fh:
            json.dump(zus, fh, indent=1)
        print(json.dumps(zus, indent=1))
    elif modus == "nachrechnen":
        ein = sys.argv[2]; aus = sys.argv[3]
        max_t = int(sys.argv[4]) if len(sys.argv) > 4 else 300
        schwelle = float(sys.argv[5]) if len(sys.argv) > 5 else 0.01
        os.makedirs(aus, exist_ok=True)
        z = np.load(ein)
        lam = z["lam"]; N = int(z["N"]); takt = int(z["takt"]); seed = int(z["seed"]); dt = float(z["dt"])
        T_ein = float(z["T_ein"]); T_mess = float(z["T_mess"])
        idx_alle = np.nonzero(lam > schwelle)[0]
        idx = idx_alle[np.argsort(lam[idx_alle])[::-1]][:max_t]
        res = dict(eingabe=os.path.basename(ein), N=N, takt=takt, schwelle=schwelle, treffer_gesamt=int(idx_alle.size),
                   nachgerechnet=int(idx.size))
        if idx.size == 0:
            res["robust"] = 0
        else:
            par = {k: z[k][idx] for k in ("K", "alpha", "F", "s", "omega", "Omega", "d")}
            t0 = time.time()
            # gleiche Anfangsbedingung wie in der Stichprobe: Zufallsfolge neu ziehen und Teilmenge waehlen
            # (Anfangswerte haengen nur von seed_ab und P ab) -> hier eigene Anfangswerte fuer alle drei Varianten
            # mit festen Seeds; Variante C mit anderem Seed als A und B.
            lam_dt2 = lyapunov(par, N, dt / 2, T_ein, T_mess, seed_ab=seed + 2000)
            lam_T2 = lyapunov(par, N, dt, T_ein, 2 * T_mess, seed_ab=seed + 2000)
            lam_ab = lyapunov(par, N, dt, T_ein, T_mess, seed_ab=seed + 3000)
            rob = (lam_dt2 > schwelle) & (lam_T2 > schwelle) & (lam_ab > schwelle)
            res.update(dict(sek=time.time() - t0, robust=int(rob.sum()),
                            robust_gt_005=int(((lam_dt2 > 0.005) & (lam_T2 > 0.005) & (lam_ab > 0.005)).sum()),
                            max_abw_dt2=float(np.max(np.abs(lam_dt2 - lam[idx]))),
                            median_abw_dt2=float(np.median(np.abs(lam_dt2 - lam[idx])))))
            ordn = np.argsort(np.minimum(np.minimum(lam_dt2, lam_T2), lam_ab))[::-1][:10]
            res["beste_robuste"] = [dict(lam=float(lam[idx][i]), lam_dt2=float(lam_dt2[i]), lam_T2=float(lam_T2[i]),
                                         lam_andereAB=float(lam_ab[i]), K=float(par["K"][i]), alpha=float(par["alpha"][i]),
                                         F=float(par["F"][i]), s=float(par["s"][i]),
                                         omega=[float(w) for w in par["omega"][i]], Omega=float(par["Omega"][i]))
                                    for i in ordn]
            np.savez_compressed(os.path.join(aus, f"nach{schwelle}_" + os.path.basename(ein)), idx=idx, lam=lam[idx],
                                lam_dt2=lam_dt2, lam_T2=lam_T2, lam_ab=lam_ab)
        with open(os.path.join(aus, f"nach{schwelle}_" + os.path.basename(ein).replace(".npz", ".json")), "w") as fh:
            json.dump(res, fh, indent=1)
        print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
