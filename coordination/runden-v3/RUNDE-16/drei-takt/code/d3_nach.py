#!/usr/bin/env python3
"""D3-Nachrechnung (PLAN-NACHTRAG-1): Treffer aller Faelle gemeinsam, auf N = 4 aufgefuellt (Maske).

Varianten je Treffer:
  B  urspruengliche Anfangswerte, dt, Messung 2 T (dabei wird auch lambda(T) mitgeschrieben = Code-Pruefung, muss den
     Stichprobenwert wiedergeben)
  C  andere Anfangswerte (Seed + 3000), dt, Messung T
  A  urspruengliche Anfangswerte, dt/2, Messung T
Aufruf:
  python d3_nach.py <modus: BC | A> <ausgabe.json> <max_je_fall> <datei1.npz:schwelle> [<datei2.npz:schwelle> ...]
"""
import sys, os, json, time
import numpy as np

NMAX = 4


def anfangswerte(seed_ab, P, N):
    rng = np.random.default_rng(seed_ab)
    phi = rng.uniform(0, 2 * np.pi, (P, N))
    v = rng.normal(size=(P, N)); v /= np.linalg.norm(v, axis=1, keepdims=True)
    return phi, v


def auffuellen(a, N, wert=0.0):
    out = np.full((a.shape[0], NMAX), wert)
    out[:, :N] = a
    return out


def lauf(K, al, F, dom, Nn, maske, phi, v, dt, T_ein, T_mess_liste, renorm=1.0):
    """Gibt fuer jede Messdauer in T_mess_liste lambda zurueck (Messung beginnt bei T_ein)."""
    K = K[:, None]; al = al[:, None]; F = F[:, None]
    ca = np.cos(al); sa = np.sin(al); KN = K / Nn[:, None]
    m = maske

    def rhs(phi, v):
        c = np.cos(phi) * m; s = np.sin(phi) * m
        C = c.sum(axis=1, keepdims=True); S = s.sum(axis=1, keepdims=True)
        cpa = c * ca - s * sa
        spa = s * ca + c * sa
        dphi = (dom + KN * (S * cpa - C * spa) - F * s) * m
        Wc = (v * c).sum(axis=1, keepdims=True); Ws = (v * s).sum(axis=1, keepdims=True)
        dv = (KN * ((Wc - C * v) * cpa + (Ws - S * v) * spa) - F * c * v) * m
        return dphi, dv

    def schritt(phi, v):
        k1, l1 = rhs(phi, v)
        k2, l2 = rhs(phi + 0.5 * dt * k1, v + 0.5 * dt * l1)
        k3, l3 = rhs(phi + 0.5 * dt * k2, v + 0.5 * dt * l2)
        k4, l4 = rhs(phi + dt * k3, v + dt * l3)
        return phi + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4), v + (dt / 6) * (l1 + 2 * l2 + 2 * l3 + l4)

    nr = int(round(renorm / dt))
    n_ein = int(round(T_ein / dt)) // nr
    ziele = sorted(int(round(T / dt)) // nr for T in T_mess_liste)
    for _ in range(n_ein):
        for _ in range(nr):
            phi, v = schritt(phi, v)
        v /= np.linalg.norm(v, axis=1, keepdims=True)
    summe = np.zeros(phi.shape[0]); erg = {}
    for blk in range(1, ziele[-1] + 1):
        for _ in range(nr):
            phi, v = schritt(phi, v)
        nv = np.linalg.norm(v, axis=1)
        summe += np.log(nv)
        v /= nv[:, None]
        if blk in ziele:
            erg[blk] = summe / (blk * nr * dt)
    return [erg[int(round(T / dt)) // nr] for T in T_mess_liste]


def main():
    modus = sys.argv[1]; ausj = sys.argv[2]; maxj = int(sys.argv[3])
    faelle = []
    for arg in sys.argv[4:]:
        pfad, schw = arg.rsplit(":", 1)
        faelle.append((pfad, float(schw)))
    K = []; al = []; F = []; dom = []; Nn = []; mk = []; phi = []; v = []; info = []
    T_ein = None; T_mess = None; dt = None
    for fi, (pfad, schw) in enumerate(faelle):
        z = np.load(pfad)
        lam = z["lam"]; N = int(z["N"]); seed = int(z["seed"]); P = lam.size
        dt = float(z["dt"]); T_ein = float(z["T_ein"]); T_mess = float(z["T_mess"])
        alle = np.nonzero(lam > schw)[0]
        idx = alle[np.argsort(lam[alle])[::-1]][:maxj]
        info.append(dict(datei=os.path.basename(pfad), N=N, takt=int(z["takt"]), schwelle=schw, P=P,
                         treffer_gesamt=int(alle.size), nachgerechnet=int(idx.size)))
        if idx.size == 0:
            continue
        ph0, v0 = anfangswerte(seed + 1000, P, N)
        ph0 = ph0[idx]; v0 = v0[idx]
        ph1, v1 = anfangswerte(seed + 3000, idx.size, N)
        d = z["omega"][idx] - z["Omega"][idx][:, None]
        varianten = [("orig", ph0, v0)] if modus == "A" else [("orig", ph0, v0), ("andere", ph1, v1)]
        for name, p_, v_ in varianten:
            K.append(z["K"][idx]); al.append(z["alpha"][idx]); F.append(z["F"][idx])
            dom.append(auffuellen(d, N)); Nn.append(np.full(idx.size, N, float))
            mk.append(auffuellen(np.ones((idx.size, N)), N)); phi.append(auffuellen(p_, N)); v.append(auffuellen(v_, N))
            for j, i in enumerate(idx):
                info.append(dict(fall=fi, variante=name, i=int(i), lam_stichprobe=float(lam[i])))
    K = np.concatenate(K); al = np.concatenate(al); F = np.concatenate(F); dom = np.concatenate(dom)
    Nn = np.concatenate(Nn); mk = np.concatenate(mk); phi = np.concatenate(phi); v = np.concatenate(v)
    t0 = time.time()
    if modus == "BC":
        lT, l2T = lauf(K, al, F, dom, Nn, mk, phi, v, dt, T_ein, [T_mess, 2 * T_mess])
        werte = dict(lam_T=lT, lam_2T=l2T)
    else:
        (lT,) = lauf(K, al, F, dom, Nn, mk, phi, v, dt / 2, T_ein, [T_mess])
        werte = dict(lam_dt2=lT)
    sek = time.time() - t0
    zeilen = [x for x in info if "variante" in x]
    for k, z_ in enumerate(zeilen):
        for name, arr in werte.items():
            z_[name] = float(arr[k])
    res = dict(modus=modus, sek=sek, dt=dt, T_ein=T_ein, T_mess=T_mess, faelle=[x for x in info if "variante" not in x],
               zeilen=zeilen)
    with open(ausj, "w") as fh:
        json.dump(res, fh, indent=1)
    kurz = dict(modus=modus, sek=sek, faelle=res["faelle"])
    if modus == "BC":
        orig = [z_ for z_ in zeilen if z_["variante"] == "orig"]
        kurz["max_abw_lamT_gegen_stichprobe"] = max(abs(z_["lam_T"] - z_["lam_stichprobe"]) for z_ in orig) if orig else None
    print(json.dumps(kurz, indent=1))


if __name__ == "__main__":
    main()
