#!/usr/bin/env python3
"""Abbildungen fuer drei-takt (Runde 16). Aufruf: python plots.py <aus-ordner> <abb-ordner>"""
import sys, os, json, glob
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AUS = sys.argv[1]; ABB = sys.argv[2]
os.makedirs(ABB, exist_ok=True)
MU_R = (1 - np.sqrt(69) / 9) / 2
MU_Z = (1 - np.sqrt(8 / 9)) / 2
TOL = 1e-6


def d1a():
    f = os.path.join(AUS, "d1a", "d1a_B.npz")
    if not os.path.exists(f):
        return
    z = np.load(f)
    mus, es, mx = z["mus"], z["es"], z["maxabs4000"]
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
    val = np.log10(np.maximum(mx - 1, 1e-12))
    im = ax[0].pcolormesh(mus, es, np.where(mx <= 1 + TOL, np.nan, val), shading="nearest", cmap="magma_r", vmin=-6, vmax=1)
    ax[0].pcolormesh(mus, es, np.where(mx <= 1 + TOL, 1.0, np.nan), shading="nearest", cmap="Greens", vmin=0, vmax=1.5)
    plt.colorbar(im, ax=ax[0], label="log10(max|rho| - 1), instabil")
    ax[0].axvline(MU_R, color="b", lw=0.8, ls="--", label="mu_R = 0,03852")
    ax[0].axvline(MU_Z, color="c", lw=0.8, ls=":", label="Zungenspitze 0,02860")
    fa = os.path.join(AUS, "d1a", "d1a_A.json")
    if os.path.exists(fa):
        b = json.load(open(fa)).get("bisektion_n4000", [])
        if b:
            ax[0].plot([p[1] for p in b], [p[0] for p in b], "k.", ms=3, label="Bisektion (Gitter A, n=4000)")
    ax[0].set_xlabel("mu"); ax[0].set_ylabel("e"); ax[0].legend(fontsize=7, loc="upper left")
    ax[0].set_title("D1a: L4 linear, gruen = stabil (|rho| <= 1 + 1e-6), Gitter B")
    sel = (mus >= 0.034) & (mus <= 0.06)
    ax[1].pcolormesh(mus[sel], es, np.where(mx[:, sel] <= 1 + TOL, 1.0, 0.0), shading="nearest", cmap="Greens", vmin=0, vmax=1.5)
    ax[1].axvline(MU_R, color="b", lw=0.8, ls="--")
    ax[1].set_xlabel("mu"); ax[1].set_ylabel("e"); ax[1].set_title("Ausschnitt mu >= 0,034 (gruen = stabil)")
    fig.tight_layout(); fig.savefig(os.path.join(ABB, "d1a_karte.png"), dpi=130); plt.close(fig)


def d1d():
    fs = sorted(glob.glob(os.path.join(AUS, "d1d", "d1d_*_f1.npz")))
    if not fs:
        return
    mus = []; epss = None; Oms = None; mxs = []
    for f in fs:
        z = np.load(f)
        epss, Oms = z["epss"], z["Oms"]
        for i, m in enumerate(z["mus"]):
            mus.append(float(m)); mxs.append(z["maxabs"][i])
    o = np.argsort(mus)
    fig, axs = plt.subplots(len(mus), 1, figsize=(12, 2.3 * len(mus)), sharex=True)
    axs = np.atleast_1d(axs)
    for a, k in zip(axs, o):
        mu = mus[k]; mx = mxs[k]
        val = np.log10(np.maximum(mx - 1, 1e-12))
        im = a.pcolormesh(Oms, epss, np.where(mx <= 1 + TOL, np.nan, val), shading="nearest", cmap="magma_r", vmin=-6, vmax=1)
        a.pcolormesh(Oms, epss, np.where(mx <= 1 + TOL, 1.0, np.nan), shading="nearest", cmap="Greens", vmin=0, vmax=1.5)
        c = (27 / 4) * mu * (1 - mu); d = 1 - 4 * c
        if d >= 0:
            s1 = np.sqrt((1 + np.sqrt(d)) / 2); s2 = np.sqrt((1 - np.sqrt(d)) / 2)
            for n in (1, 2, 3):
                for w, col in ((2 * s1 / n, "b"), (2 * s2 / n, "c"), ((s1 - s2) / n, "m"), ((s1 + s2) / n, "y")):
                    if 0.2 <= w <= 10:
                        a.axvline(w, color=col, lw=0.6, ls="--")
        a.set_ylabel("eps"); a.set_title(f"mu = {mu:.4f}" + (" (> mu_R)" if mu > MU_R else "") +
                                          "  gruen stabil; Linien: 2s1/n blau, 2s2/n cyan, (s1-s2)/n magenta, (s1+s2)/n gelb", fontsize=8)
        a.set_xscale("log")
    axs[-1].set_xlabel("Omega (log)")
    fig.tight_layout(); fig.savefig(os.path.join(ABB, "d1d_zungen.png"), dpi=120); plt.close(fig)


def d1b():
    f = os.path.join(AUS, "d1b", "d1b_haupt.json")
    if not os.path.exists(f):
        return
    r = json.load(open(f))
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    for de, col in ((0.005, "C0"), (0.02, "C1")):
        zs = [z for z in r["zeilen"] if z["delta"] == de]
        a = np.array([z["mu_minus_muR"] for z in zs])
        med = np.array([z["median_lebensdauer"] if z["median_lebensdauer"] is not None else np.nan for z in zs])
        tl = np.array([z["T_lin_umlaeufe"] for z in zs])
        gef = np.array([z["anteil_gefangen"] for z in zs])
        ax[0].loglog(a, med, "o-", color=col, label=f"Median Lebensdauer, Auslenkung {de}")
        ax[0].loglog(a, tl, ":", color=col, label=f"linear ln(0,5/{de})/Re lambda")
        ax[1].semilogx(a, gef, "o-", color=col, label=f"Auslenkung {de}")
    ax[0].axhline(1000, color="k", lw=0.6)
    ax[0].set_xlabel("mu - mu_R"); ax[0].set_ylabel("Umlaeufe"); ax[0].legend(fontsize=7)
    ax[0].set_title("D1b: Lebensdauer (Abstand L4 > 0,5 oder r2 < 0,05), Median ueber 64 Richtungen", fontsize=9)
    ax[1].set_xlabel("mu - mu_R"); ax[1].set_ylabel("Anteil nach 1000 Umlaeufen noch nahe L4"); ax[1].legend(fontsize=7)
    fig.tight_layout(); fig.savefig(os.path.join(ABB, "d1b_lebensdauer.png"), dpi=130); plt.close(fig)


def d2():
    # PLAN-NACHTRAG-2: D2 in zwei Aufrufen (ab, c)
    fj = os.path.join(AUS, "d2", "d2_voll_ab.json"); fz = os.path.join(AUS, "d2", "d2_voll_ab_b.npz")
    fc = os.path.join(AUS, "d2", "d2_voll_c_c.npz")
    if not (os.path.exists(fj) and os.path.exists(fz)):
        return
    r = json.load(open(fj)); z = dict(np.load(fz))
    if os.path.exists(fc):
        z.update(dict(np.load(fc)))
    else:
        z.update(c_Oms=np.array([0.5, 1.5]), c_Fs=np.array([0, 0.5]), c_lyap=np.zeros((2, 2)))
    fig, ax = plt.subplots(2, 2, figsize=(12, 9))
    for Kv, col in ((0.5, "C0"), (1.0, "C1")):
        zs = [q for q in r["d2a"]["zeilen"] if q["K"] == Kv and q["T_num"] is not None]
        a = np.array([q["abstand"] for q in zs])
        ax[0, 0].loglog(a, [q["T_num"] for q in zs], "o", color=col, label=f"numerisch K = {Kv}")
        ax[0, 0].loglog(a, [q["T_adler"] for q in zs], "-", color=col, lw=0.8, label=f"Adler 2pi/sqrt(D^2-4K^2), K = {Kv}")
    ax[0, 0].set_xlabel("|Delta| - 2K"); ax[0, 0].set_ylabel("Rastdauer (Zeit zwischen Phasenspruengen)")
    ax[0, 0].legend(fontsize=7); ax[0, 0].set_title("D2a: Rastdauer gegen Abstand zur Rastgrenze", fontsize=9)
    ps, Fs, ge, R = z["b_psis"], z["b_Fs"], z["b_gerastet"], z["b_R"]
    ax[0, 1].pcolormesh(ps, Fs, ge.T.astype(float), shading="nearest", cmap="Greens", vmin=0, vmax=1.3)
    ax[0, 1].contour(ps, Fs, R.T, levels=[r["d2b"]["Delta"]], colors="r", linewidths=1)
    ax[0, 1].set_xlabel("psi (Phase des Takts)"); ax[0, 1].set_ylabel("F")
    ax[0, 1].set_title("D2b: Omega = 1, gruen = C rastet an A/B; rot: |2K + F e^{i psi}| = Delta", fontsize=9)
    Om, F2, an, am = z["b_Oms"], z["b_Fs"], z["b_an_AB"], z["b_am_Takt"]
    kl = np.where(an, 2.0, np.where(am, 1.0, 0.0))
    ax[1, 0].pcolormesh(Om, F2, kl.T, shading="nearest", cmap="viridis", vmin=0, vmax=2)
    ax[1, 0].set_xlabel("Omega"); ax[1, 0].set_ylabel("F")
    ax[1, 0].set_title("D2b: psi = 0; gelb = rastet an A/B, gruen = rastet am Takt, lila = sonst", fontsize=9)
    cO, cF, cl = z["c_Oms"], z["c_Fs"], z["c_lyap"]
    im = ax[1, 1].pcolormesh(cO, cF, cl.T, shading="nearest", cmap="coolwarm", vmin=-0.2, vmax=0.2)
    plt.colorbar(im, ax=ax[1, 1], label="Lyapunov-Exponent der C-Phase")
    for w in (0.8, 1.2, 1.1):
        ax[1, 1].axvline(w, color="k", lw=0.6, ls="--")
    ax[1, 1].set_xlabel("Omega"); ax[1, 1].set_ylabel("F")
    ax[1, 1].set_title("D2c: omega_A = 0,8, omega_B = 1,2, omega_C = 1,1, K = 0,15 (blau = C eingefangen)", fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(ABB, "d2_karten.png"), dpi=120); plt.close(fig)


def d3():
    fs = sorted(glob.glob(os.path.join(AUS, "d3", "d3_N*_P*_s*.npz")))
    if not fs:
        return
    fig, ax = plt.subplots(1, len(fs), figsize=(4 * len(fs), 3.8), sharey=True)
    ax = np.atleast_1d(ax)
    for a, f in zip(ax, fs):
        z = np.load(f)
        lam = z["lam"]; N = int(z["N"]); t = int(z["takt"])
        bins = np.linspace(-0.1, 0.25, 71)
        a.hist(np.clip(lam, -0.1, 0.25), bins=bins, color="C0")
        a.set_yscale("log"); a.axvline(0.01, color="r", lw=0.8); a.axvline(0.005, color="orange", lw=0.8, ls=":")
        nf = glob.glob(os.path.join(AUS, "d3", "nach*_" + os.path.basename(f).replace(".npz", ".json")))
        rob = ""
        if nf:
            q = json.load(open(nf[0])); rob = f", robust {q.get('robust')} von {q.get('nachgerechnet')}"
        a.set_title(f"N = {N}, {'mit' if t else 'ohne'} Takt{rob}", fontsize=9)
        a.set_xlabel("lambda_max (auf [-0,1; 0,25] begrenzt)")
    ax[0].set_ylabel("Anzahl Parameterpunkte")
    fig.tight_layout(); fig.savefig(os.path.join(ABB, "d3_lyapunov.png"), dpi=130); plt.close(fig)


for fn in (d1a, d1d, d1b, d2, d3):
    try:
        fn(); print("ok", fn.__name__)
    except Exception as ex:
        print("fehler", fn.__name__, repr(ex))
