# NETZ-C-1 (Runde 35), Teil B: Antikink in der diskreten Sine-Gordon-Kette (Frenkel-Kontorova).
#   u_n'' = (u_{n+1} - 2 u_n + u_{n-1})/h^2 - sin u_n - eta u_n' + F,   freie Enden, x_n = n h.
# Integrator: Yoshida 4. Ordnung (symplektisch, 3 Kraftauswertungen je Schritt) fuer den Hamilton-Teil,
#   Reibung exakt als p -> p exp(-eta dt/2) vor und nach jedem Schritt (Strang-Teilung).
# Start: Kontinuums-Antikink u = asin F + 4 arctan exp(-g0 (x - X0)), p = 2 v0 g0 sech(g0 (x - X0)), g0 = 1/sqrt(1-v0^2).
#   (Antikink: links 2 pi + asin F, rechts asin F; F > 0 treibt ihn nach rechts.)
# Aufruf (nur ueber kleintest.sh):
#   kette.py <name> <h> <F> <eta> <v0> <t_end> <dt_teiler> <L> <X0> [wand_s]
#   Ausgabe <name>.npz (Zeitreihen) und <name>.json (Kopf); Checkpoint <name>.ckpt.npz bei Wandzeit-Abbruch,
#   ein erneuter Aufruf mit denselben Argumenten setzt fort.
import sys, os, json, time, hashlib
import numpy as np

W1 = 1.0 / (2.0 - 2.0 ** (1.0 / 3.0))
W0 = -(2.0 ** (1.0 / 3.0)) * W1
CS = (W1 / 2, (W0 + W1) / 2, (W0 + W1) / 2, W1 / 2)
DS = (W1, W0, W1)
DS_MESS = 0.5          # Messabstand in Zeiteinheiten
HALB = 4.0             # halbe Fensterbreite um den Kinkort (Laengeneinheiten)
RAND = 30.0            # Abbruch, wenn der Kinkort naeher als RAND am rechten Ende ist
FELDER = ["t", "X", "Xcm", "gs", "gsp", "gE", "Ewin", "Ehinten", "Evorn", "E0", "H", "ncross", "pmax", "dmax"]


def main():
    a = sys.argv
    name = a[1]; h = float(a[2]); F = float(a[3]); eta = float(a[4]); v0 = float(a[5])
    t_end = float(a[6]); teiler = int(a[7]); L = float(a[8]); X0 = float(a[9])
    wand = float(a[10]) if len(a) > 10 else 520.0
    t_wand0 = time.time()
    dt = h / teiler
    nsub = int(round(DS_MESS / dt))
    assert abs(nsub * dt - DS_MESS) < 1e-12, "DS_MESS kein Vielfaches von dt"
    N = int(round(L / h)) + 1
    x = np.arange(N) * h
    us = np.arcsin(F)
    lvl = np.pi + us
    vac_site = 1.0 - np.cos(us)
    h2inv = 1.0 / (h * h)
    ckpt = name + ".ckpt.npz"
    if os.path.exists(ckpt):
        z = np.load(ckpt)
        u = z["u"].copy(); p = z["p"].copy(); k_mess = int(z["k_mess"]); Xprev = float(z["Xprev"])
        reihen = {f: list(z[f]) for f in FELDER}
        abschnitte = int(z["abschnitte"]) + 1
        print("fortgesetzt bei t = %.3f" % (k_mess * DS_MESS), flush=True)
    else:
        g0 = 1.0 / np.sqrt(1.0 - v0 * v0)
        xi = np.clip(-g0 * (x - X0), -700, 700)
        u = us + 4.0 * np.arctan(np.exp(xi))
        p = 2.0 * v0 * g0 / np.cosh(np.clip(g0 * (x - X0), -700, 700))
        k_mess = 0; Xprev = X0
        reihen = {f: [] for f in FELDER}
        abschnitte = 1
    acc = np.empty(N); tmp = np.empty(N)
    dmp = np.exp(-eta * dt / 2) if eta > 0 else 1.0

    def kraft(u, out):
        d = u[1:] - u[:-1]
        out[-1] = 0.0
        out[:-1] = d
        out[1:] -= d
        out *= h2inv
        out -= np.sin(u)
        out += F
        return out

    def messen(t, Xprev):
        w = np.floor((u - us - np.pi) / (2 * np.pi))
        ncross = int(np.abs(np.diff(w)).sum())
        s = (u - lvl)
        idx = np.nonzero(s[:-1] * s[1:] <= 0)[0]
        idx = idx[(u[idx] != u[idx + 1])]
        if len(idx) == 0:
            X = np.nan
        else:
            cand = x[idx] + h * (u[idx] - lvl) / (u[idx] - u[idx + 1])
            X = float(cand[np.argmin(np.abs(cand - Xprev))])
        Xr = X if np.isfinite(X) else Xprev
        i0 = max(0, int(np.floor((Xr - HALB) / h))); i1 = min(N - 1, int(np.ceil((Xr + HALB) / h)))
        es = h * (0.5 * p * p + 1.0 - np.cos(u) - vac_site)
        db = u[1:] - u[:-1]
        eb = db * db / (2 * h)
        Ewin = float(es[i0:i1 + 1].sum() + eb[i0:i1].sum())
        Eh = float(es[:i0].sum() + eb[:i0].sum())
        Ev = float(es[i1 + 1:].sum() + eb[i1:].sum())
        E0 = float(es.sum() + eb.sum())
        H = float((h * (0.5 * p * p + 1.0 - np.cos(u) - F * u)).sum() + eb.sum())
        D = -db[i0:i1] / h
        if len(D) >= 1:
            m = int(np.argmax(D)); gs = float(D[m] / 2)
            if 0 < m < len(D) - 1 and (D[m + 1] - 2 * D[m] + D[m - 1]) < 0:
                gsp = float((D[m] - (D[m + 1] - D[m - 1]) ** 2 / (8 * (D[m + 1] - 2 * D[m] + D[m - 1]))) / 2)
            else:
                gsp = gs
            xm = x[i0:i1] + h / 2
            sw = D.sum()
            Xcm = float((xm * D).sum() / sw) if sw != 0 else np.nan
        else:
            gs = gsp = Xcm = np.nan
        return dict(t=t, X=X, Xcm=Xcm, gs=gs, gsp=gsp, gE=Ewin / 8.0, Ewin=Ewin, Ehinten=Eh, Evorn=Ev, E0=E0, H=H,
                    ncross=ncross, pmax=float(np.abs(p).max()), dmax=float(np.abs(db).max())), Xr

    if k_mess == 0 and len(reihen["t"]) == 0:
        r, Xprev = messen(0.0, Xprev)
        for f in FELDER:
            reihen[f].append(r[f])
    status = "fertig"
    k_ziel = int(round(t_end / DS_MESS))
    while k_mess < k_ziel:
        for _ in range(nsub):
            if eta > 0:
                p *= dmp
            np.multiply(p, CS[0] * dt, out=tmp); u += tmp
            kraft(u, acc); np.multiply(acc, DS[0] * dt, out=tmp); p += tmp
            np.multiply(p, CS[1] * dt, out=tmp); u += tmp
            kraft(u, acc); np.multiply(acc, DS[1] * dt, out=tmp); p += tmp
            np.multiply(p, CS[2] * dt, out=tmp); u += tmp
            kraft(u, acc); np.multiply(acc, DS[2] * dt, out=tmp); p += tmp
            np.multiply(p, CS[3] * dt, out=tmp); u += tmp
            if eta > 0:
                p *= dmp
        k_mess += 1
        r, Xprev = messen(k_mess * DS_MESS, Xprev)
        for f in FELDER:
            reihen[f].append(r[f])
        if np.isfinite(r["X"]) and r["X"] > x[-1] - RAND:
            status = "rand"
            break
        if not np.all(np.isfinite(u)):
            status = "nan"
            break
        if time.time() - t_wand0 > wand and k_mess < k_ziel:
            np.savez(ckpt, u=u, p=p, k_mess=k_mess, Xprev=Xprev, abschnitte=abschnitte,
                     **{f: np.array(reihen[f], float) for f in FELDER})
            status = "unterbrochen"
            break
    kopf = dict(name=os.path.basename(name), h=h, F=F, eta=eta, v0=v0, t_end=t_end, teiler=teiler, dt=dt, L=L, X0=X0,
                N=N, ds_mess=DS_MESS, halb_fenster=HALB, status=status, t_letzt=k_mess * DS_MESS,
                abschnitte=abschnitte, wandzeit_s=time.time() - t_wand0, numpy=np.__version__,
                skript_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                ende_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    if status != "unterbrochen":
        np.savez_compressed(name + ".npz", **{f: np.array(reihen[f], float) for f in FELDER})
        if os.path.exists(ckpt):
            os.replace(ckpt, name + ".ckpt-verbraucht.npz")
    json.dump(kopf, open(name + ".json", "w"), indent=1)
    H = np.array(reihen["H"]); X = np.array(reihen["X"])
    print(json.dumps(dict(status=status, t=k_mess * DS_MESS, X_end=float(X[-1]),
                          H_drift_rel=float(np.max(np.abs(H - H[0])) / abs(H[0])),
                          wand_s=round(time.time() - t_wand0, 1))), flush=True)


if __name__ == "__main__":
    main()
