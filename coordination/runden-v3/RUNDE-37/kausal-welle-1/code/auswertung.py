"""KAUSAL-WELLE-1: Auswertung nach PLAN.md (Urteilsregeln Abschnitt 6), Bilder, auswertung.json.

Aufruf (nur ueber kleintest.sh): auswertung.py <laufordner> <kontinuumordner> <ausgabeordner> <rho1,rho2,rho3> <n_saaten>
"""
import glob
import hashlib
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal_welle as kw  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


def ols(t, x):
    t = np.asarray(t)
    x = np.asarray(x)
    tm = t.mean()
    b = np.sum((t - tm) * (x - x.mean())) / np.sum((t - tm) ** 2)
    return float(b)


def fenster_idx(W):
    lo = -W - kw.XB_MIN
    hi = W - kw.XB_MIN
    return max(lo, 0), min(hi, kw.XB_N)


def schwerpunkt(b, j0_, j1_):
    """b: (40, 280, >=3) Summen -> <x>_k, <t>_k, Sw_k im Fenster [j0_, j1_)."""
    Sw = b[:, j0_:j1_, 0].sum(axis=1)
    Sx = b[:, j0_:j1_, 1].sum(axis=1)
    St = b[:, j0_:j1_, 2].sum(axis=1)
    return Sx / Sw, St / Sw, Sw


def main():
    lauf, kont, aus = sys.argv[1], sys.argv[2], sys.argv[3]
    rhos = [float(r) for r in sys.argv[4].split(",")]
    n_soll = int(sys.argv[5])
    os.makedirs(aus, exist_ok=True)
    K = np.load(os.path.join(kont, "kontinuum.npz"))
    kb = K["bins"]
    kphi = K["phi_p"]
    kquad = K["quad"]
    vbar = K["vbar"]
    pp = K["pruefpunkte"]
    besch = {}
    # ---------- Kontinuum: Fenster, V_c, Norm, Stichprobenrauschen ----------
    Wc = []
    Vc = []
    Vc_ganz = []
    nc = []
    sx_max = []
    for c in range(kw.NC):
        b = kb[c]
        Sw = b[:, :, 0].sum(axis=1)
        Sx = b[:, :, 1].sum(axis=1)
        Sx2 = b[:, :, 3].sum(axis=1)
        sx = np.sqrt(Sx2 / Sw - (Sx / Sw) ** 2)
        sx_max.append(float(sx.max()))
        W = int(np.ceil(4.0 * sx.max()))
        W = min(W, 140)
        Wc.append(W)
        j0_, j1_ = fenster_idx(W)
        xm, tm, Swf = schwerpunkt(b, j0_, j1_)
        Vc.append(ols(tm, xm))
        xg, tg, _ = schwerpunkt(b, 0, kw.XB_N)
        Vc_ganz.append(ols(tg, xg))
        nc.append(Swf / kw.W_SCHEIBE)
    nc = np.array(nc)
    besch["kontinuum"] = {
        "fenster_halbbreite_W": Wc, "sigma_x_max": sx_max, "V_c_fenster": Vc, "V_c_ganze_scheibe": Vc_ganz,
        "v_analytisch_positive_frequenz": vbar.tolist(), "tanh_eta": kw.VN.tolist(),
        "quadratur_gegen_k_raum_rel": [[float(abs(kquad[c, i] - kphi[c, i]) / abs(kphi[c, i])) for i in range(3)]
                                       for c in range(kw.NC)],
        "norm_c_anfang_ende": [[float(nc[c, :4].mean()), float(nc[c, -4:].mean())] for c in range(kw.NC)]}

    def stichproben_se(c, rho):
        b = kb[c]
        j0_, j1_ = fenster_idx(Wc[c])
        xm, tm, Sw = schwerpunkt(b, j0_, j1_)
        A = b[:, j0_:j1_, 4].sum(axis=1)
        B = b[:, j0_:j1_, 5].sum(axis=1)
        C = b[:, j0_:j1_, 6].sum(axis=1)
        Q = C - 2 * xm * B + xm ** 2 * A
        dx2 = Q / (rho * Sw ** 2)
        tc = tm - tm.mean()
        return float(np.sqrt(np.sum(tc ** 2 * dx2)) / np.sum(tc ** 2))

    # ---------- Kausalmenge ----------
    daten = {}
    for rho in rhos:
        fs = sorted(glob.glob(os.path.join(lauf, f"feld-r{int(rho)}-s*.npz")),
                    key=lambda p: int(p.split("-s")[-1].split(".")[0]))
        saaten = []
        V = []
        Vg = []
        nk = []
        php = []
        xk = []
        Ns = []
        for f in fs:
            z = np.load(f)
            s = int(f.split("-s")[-1].split(".")[0])
            kopf = json.load(open(f.replace(".npz", ".json")))
            if not kopf.get("endlich", False):
                continue
            saaten.append(s)
            Ns.append(kopf["N"])
            summen = z["summen"]
            php.append(z["phi_p"])
            vrow, vgrow, nrow, xrow = [], [], [], []
            for c in range(kw.NC):
                j0_, j1_ = fenster_idx(Wc[c])
                xm, tm, Sw = schwerpunkt(summen[c], j0_, j1_)
                vrow.append(ols(tm, xm))
                xg, tg, _ = schwerpunkt(summen[c], 0, kw.XB_N)
                vgrow.append(ols(tg, xg))
                nrow.append(Sw / (rho * kw.W_SCHEIBE))
                xrow.append(np.stack([tm, xm]))
            V.append(vrow)
            Vg.append(vgrow)
            nk.append(nrow)
            xk.append(xrow)
        daten[rho] = {"saaten": saaten, "V": np.array(V), "Vg": np.array(Vg), "n": np.array(nk),
                      "phi": np.array(php), "xk": np.array(xk), "N": Ns}
    vollst = all(len(daten[r]["saaten"]) >= n_soll for r in rhos)
    urteile = {}
    # ---------- KW0 ----------
    tests = []
    srel = {}
    for rho in rhos:
        P = daten[rho]["phi"]
        n = P.shape[0]
        for c in range(kw.NC):
            for i in range(3):
                z = P[:, c, i]
                m = z.mean()
                sd = np.sqrt(z.real.var(ddof=1) + z.imag.var(ddof=1))
                se = sd / np.sqrt(n)
                d = abs(m - kphi[c, i])
                tests.append({"rho": rho, "sigma": kw.CONFIGS[c][0], "eta": kw.CONFIGS[c][1], "punkt": i,
                              "mittel": [float(m.real), float(m.imag)],
                              "kontinuum": [float(kphi[c, i].real), float(kphi[c, i].imag)],
                              "abw_in_SE": float(d / se), "rel_streuung": float(sd / abs(kphi[c, i]))})
                srel[(rho, c, i)] = sd / abs(kphi[c, i])
    a_ok = all(t["abw_in_SE"] <= 3.0 for t in tests)
    gm = [float(np.exp(np.mean([np.log(srel[(rho, c, i)]) for c in range(kw.NC) for i in range(3)]))) for rho in rhos]
    steig = ols(np.log(rhos), np.log(gm))
    b_ok = -0.6 <= steig <= -0.4
    steig_je = {}
    for c in range(kw.NC):
        g = [np.exp(np.mean([np.log(srel[(rho, c, i)]) for i in range(3)])) for rho in rhos]
        steig_je[f"sigma{kw.CONFIGS[c][0]:g}_eta{kw.CONFIGS[c][1]:g}"] = ols(np.log(rhos), np.log(g))
    urteile["KW0"] = {
        "urteil": ("eingetroffen" if (a_ok and b_ok) else "nicht eingetroffen") if vollst else "nicht auswertbar",
        "werte": {"pruefpunkte_alle_innerhalb_3SE": a_ok, "max_abw_in_SE": max(t["abw_in_SE"] for t in tests),
                  "zahl_tests": len(tests), "zahl_ueber_3SE": int(sum(t["abw_in_SE"] > 3 for t in tests)),
                  "rel_streuung_geom_mittel_je_rho": dict(zip([str(int(r)) for r in rhos], gm)),
                  "steigung_log_rel_streuung_gegen_log_rho": steig, "steigung_im_band": b_ok,
                  "steigung_je_konfiguration": steig_je}}
    besch["KW0_tests"] = tests
    # ---------- KW1 ----------
    kw1 = []
    for rho in rhos:
        V = daten[rho]["V"]
        n = V.shape[0]
        for c in range(kw.NC):
            e = kw.CONFIGS[c][1]
            m = V[:, c].mean()
            se = V[:, c].std(ddof=1) / np.sqrt(n)
            tol = 0.02 if e == 0 else 0.02 * abs(Vc[c])
            kw1.append({"rho": rho, "sigma": kw.CONFIGS[c][0], "eta": e, "V_mittel": float(m), "SE": float(se),
                        "V_c": Vc[c], "abw": float(m - Vc[c]), "toleranz": tol, "ok": bool(abs(m - Vc[c]) <= tol),
                        "V_mittel_ganze_scheibe": float(daten[rho]["Vg"][:, c].mean()),
                        "V_c_ganze_scheibe": Vc_ganz[c]})
    urteile["KW1"] = {"urteil": ("eingetroffen" if all(k["ok"] for k in kw1) else "nicht eingetroffen")
                      if vollst else "nicht auswertbar",
                      "werte": {"zahl_ok": int(sum(k["ok"] for k in kw1)), "zahl": len(kw1), "einzeln": kw1}}
    # ---------- KW2 ----------
    kw2 = {}
    std_tab = {}
    for rho in rhos:
        V = daten[rho]["V"]
        for c in range(kw.NC):
            s, e = kw.CONFIGS[c]
            sv = float(V[:, c].std(ddof=1))
            th = np.arctanh(np.clip(V[:, c], -0.999999, 0.999999))
            std_tab[f"rho{int(rho)}_sigma{s:g}_eta{e:g}"] = {
                "std_V": sv, "std_rapiditaet": float(th.std(ddof=1)),
                "stichproben_se_vorhersage": stichproben_se(c, rho),
                "std_V_ganze_scheibe": float(daten[rho]["Vg"][:, c].std(ddof=1))}
    r200 = 200.0
    ok2 = []
    if r200 in daten:
        for e in kw.ETAS:
            c2 = kw.CONFIGS.index((2.0, e))
            c8 = kw.CONFIGS.index((8.0, e))
            s2 = daten[r200]["V"][:, c2].std(ddof=1)
            s8 = daten[r200]["V"][:, c8].std(ddof=1)
            kw2[f"eta{e:g}"] = {"std_sigma2": float(s2), "std_sigma8": float(s8), "verhaeltnis": float(s8 / s2),
                                "ok": bool(s8 <= 0.5 * s2)}
            ok2.append(s8 <= 0.5 * s2)
    urteile["KW2"] = {"urteil": ("eingetroffen" if (ok2 and all(ok2)) else "nicht eingetroffen")
                      if (vollst and ok2) else "nicht auswertbar", "werte": kw2}
    besch["streuung_V"] = std_tab
    # ---------- KW3 ----------
    kw3 = []
    for rho in rhos:
        nn = daten[rho]["n"]
        for c in range(kw.NC):
            R = nn[:, c, :].mean(axis=0) / nc[c]
            G = R[-4:].mean() / R[:4].mean()
            kw3.append({"rho": rho, "sigma": kw.CONFIGS[c][0], "eta": kw.CONFIGS[c][1], "R_anfang": float(R[:4].mean()),
                        "R_ende": float(R[-4:].mean()), "G": float(G), "R_max": float(R.max()), "ok": bool(G <= 1.5)})
    urteile["KW3"] = {"urteil": ("eingetroffen" if all(k["ok"] for k in kw3) else "nicht eingetroffen")
                      if vollst else "nicht auswertbar",
                      "werte": {"G_max": max(k["G"] for k in kw3), "einzeln": kw3}}
    # ---------- Punktquelle, Probe ----------
    pq = sorted(glob.glob(os.path.join(lauf, "punkt-r*-s*.json")))
    if pq:
        W = np.array([json.load(open(f))["werte"] for f in pq])
        k0 = json.load(open(pq[0]))
        soll = np.array(k0["soll"])
        m = W.mean(axis=0)
        se = W.std(axis=0, ddof=1) / np.sqrt(W.shape[0])
        besch["punktquelle"] = {"zahl_saaten": W.shape[0], "taus": k0["taus"], "zetas": k0["zetas"], "soll": soll.tolist(),
                                "mittel": m.tolist(), "SE": se.tolist(), "abw_in_SE": ((m - soll) / se).tolist(),
                                "rel_streuung": (W.std(axis=0, ddof=1) / np.maximum(abs(soll), 1e-12)).tolist()}
    pr = sorted(glob.glob(os.path.join(lauf, "probe-*.json")))
    if pr:
        besch["probe"] = [json.load(open(f)) for f in pr]
    besch["N_je_rho"] = {str(int(r)): daten[r]["N"] for r in rhos}
    besch["saaten_je_rho"] = {str(int(r)): daten[r]["saaten"] for r in rhos}
    # ---------- Bilder ----------
    rmax = max(rhos)
    fig, ax = plt.subplots(2, 3, figsize=(15, 8))
    for c in range(kw.NC):
        a = ax[c % 2, c // 2]
        x = pp[c, 3:, 1]
        P = daten[rmax]["phi"][:, c, 3:]
        m = P.mean(axis=0)
        se_r = P.real.std(axis=0, ddof=1) / np.sqrt(P.shape[0])
        se_i = P.imag.std(axis=0, ddof=1) / np.sqrt(P.shape[0])
        a.errorbar(x, m.real, yerr=se_r, fmt="o", ms=3, color="C0", label="Re, Saatmittel +- SE")
        a.errorbar(x, m.imag, yerr=se_i, fmt="s", ms=3, color="C1", label="Im, Saatmittel +- SE")
        a.plot(x, kphi[c, 3:].real, "-", color="C0", lw=1, label="Re, Kontinuum")
        a.plot(x, kphi[c, 3:].imag, "-", color="C1", lw=1, label="Im, Kontinuum")
        a.set_title(f"sigma = {kw.CONFIGS[c][0]:g}, eta = {kw.CONFIGS[c][1]:g}, t = {pp[c, 3, 0]:g}, rho = {rmax:g}")
        a.set_xlabel("x")
        if c == 0:
            a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "saatmittel_kontinuum.png"), dpi=110)
    plt.close(fig)
    fig, ax = plt.subplots(2, 3, figsize=(15, 8))
    for c in range(kw.NC):
        a = ax[c % 2, c // 2]
        for k, rho in enumerate(rhos):
            X = daten[rho]["xk"][:, c]  # (n, 2, 40)
            tt = X[:, 0].mean(axis=0)
            dx = X[:, 1] - Vc[c] * X[:, 0]
            m = dx.mean(axis=0)
            s = dx.std(axis=0, ddof=1)
            a.plot(tt, m, color=f"C{k}", label=f"rho = {rho:g}")
            a.fill_between(tt, m - s, m + s, color=f"C{k}", alpha=0.2)
        j0_, j1_ = fenster_idx(Wc[c])
        xm, tm, _ = schwerpunkt(kb[c], j0_, j1_)
        a.plot(tm, xm - Vc[c] * tm, "k--", lw=1, label="Kontinuum")
        a.set_title(f"<x>(t) - V_c t, sigma = {kw.CONFIGS[c][0]:g}, eta = {kw.CONFIGS[c][1]:g} (Band: Streuung ueber Saaten)",
                    fontsize=8)
        a.set_xlabel("t")
        if c == 0:
            a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "x_t.png"), dpi=110)
    plt.close(fig)
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    for ie, e in enumerate(kw.ETAS):
        a = ax[ie]
        for k, rho in enumerate(rhos):
            ss = [std_tab[f"rho{int(rho)}_sigma{s:g}_eta{e:g}"]["std_V"] for s in kw.SIGMAS]
            sp = [std_tab[f"rho{int(rho)}_sigma{s:g}_eta{e:g}"]["stichproben_se_vorhersage"] for s in kw.SIGMAS]
            a.loglog(kw.SIGMAS, ss, "o-", color=f"C{k}", label=f"Streuung V, rho = {rho:g}")
            a.loglog(kw.SIGMAS, sp, ":", color=f"C{k}", label=f"nur Punktstichprobe (Vorhersage), rho = {rho:g}")
        a.set_xlabel("sigma")
        a.set_ylabel("Streuung der Schwerpunktgeschwindigkeit ueber Saaten")
        a.set_title(f"eta = {e:g}")
        a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "streuung_v.png"), dpi=110)
    plt.close(fig)
    fig, ax = plt.subplots(2, 3, figsize=(15, 8))
    for c in range(kw.NC):
        a = ax[c % 2, c // 2]
        for k, rho in enumerate(rhos):
            nn = daten[rho]["n"][:, c, :]
            tt = daten[rho]["xk"][:, c, 0].mean(axis=0)
            a.plot(tt, nn.mean(axis=0) / nc[c], color=f"C{k}", label=f"rho = {rho:g}")
        a.axhline(1.0, color="k", lw=0.8)
        a.set_title(f"Norm / Kontinuum, sigma = {kw.CONFIGS[c][0]:g}, eta = {kw.CONFIGS[c][1]:g}")
        a.set_xlabel("t")
        if c == 0:
            a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "norm_t.png"), dpi=110)
    plt.close(fig)
    out = {"urteile": urteile, "beschreibend": besch, "rhos": rhos, "n_saaten_soll": n_soll,
           "skript_sha256": SKRIPT_SHA, "kausal_welle_sha256": kw.SKRIPT_SHA,
           "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(aus, "auswertung.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: urteile[k]["urteil"] for k in urteile}))


if __name__ == "__main__":
    main()
