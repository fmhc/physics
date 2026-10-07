"""SCHACHBRETT-KAUSAL-1: Auswertung nach PLAN.md (Urteilsregeln Abschnitt 5), Bilder, auswertung.json.

Aufruf (nur ueber kleintest.sh): auswertung.py <laufordner> <kontinuumordner> <schachbrettordner> <ausgabeordner>
                                              <rho1,rho2> <n_saaten>
"""
import glob
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.special import j0, j1

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal_dirac as kd  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


def ols(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    xm = x.mean()
    return float(np.sum((x - xm) * (y - y.mean())) / np.sum((x - xm) ** 2))


def fenster(W):
    return max(-W - kd.XB_MIN, 0), min(W - kd.XB_MIN, kd.XB_N)


def csd(z):
    """komplexe Standardabweichung ueber Saaten (Achse 0): sqrt(var Re + var Im), ddof = 1."""
    return np.sqrt(z.real.var(axis=0, ddof=1) + z.imag.var(axis=0, ddof=1))


def main():
    lauf, kont, sbo, aus = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    rhos = [float(r) for r in sys.argv[5].split(",")]
    n_soll = int(sys.argv[6])
    os.makedirs(aus, exist_ok=True)
    urteile = {}
    besch = {}
    # ---------------- SK0: regelmaessiges Schachbrett ----------------
    SB = json.load(open(os.path.join(sbo, "schachbrett.json")))
    eps = np.array(SB["eps"])
    E = np.array([SB["gitter"][str(e)]["E_max"] for e in SB["eps"]])
    steig0 = ols(np.log(eps), np.log(E))
    E001 = float(SB["gitter"]["0.01"]["E_max"])
    ok0 = (E001 <= 1e-2) and (0.8 <= steig0 <= 1.2)
    je_tau = {}
    for e in SB["eps"]:
        g = SB["gitter"][str(e)]
        a = np.maximum(np.array(g["abw_RR"]), np.array(g["abw_LR"]))  # (nz, nt)
        je_tau[str(e)] = a.max(axis=0).tolist()
    urteile["SK0"] = {"urteil": "eingetroffen" if ok0 else "nicht eingetroffen",
                      "werte": {"E_max_je_eps": dict(zip([str(e) for e in SB["eps"]], E.tolist())), "E_max_eps_0.01": E001,
                                "steigung_log_E_gegen_log_eps": steig0, "schwelle": 1e-2, "band_steigung": [0.8, 1.2],
                                "binom_probe_max": max(max(b["abw_R"], b["abw_L"]) for b in SB["binom_probe"])}}
    besch["SK0_max_abw_je_tau"] = {"taus": SB["taus"], "je_eps": je_tau}
    # beschreibend: normiertes Schachbrett, Faktor (1 + m^2 eps^2)^(-t/(2 eps)) (Betrag der Schritt-Eigenwerte)
    krr = np.array(SB["kontinuum_RR"]["re"]) + 1j * np.array(SB["kontinuum_RR"]["im"])
    klr = np.array(SB["kontinuum_LR"]["re"]) + 1j * np.array(SB["kontinuum_LR"]["im"])
    tt0 = np.array(SB["taus"])[None, :] * np.cosh(np.array(SB["zetas"]))[:, None]
    En = []
    for e in SB["eps"]:
        g = SB["gitter"][str(e)]
        f = (1.0 + (kd.M * e) ** 2) ** (-tt0 / (2 * e))
        grr = (np.array(g["RR_re"]) + 1j * np.array(g["RR_im"])) * f
        glr = (np.array(g["LR_re"]) + 1j * np.array(g["LR_im"])) * f
        En.append(float(max(np.abs(grr - krr).max(), np.abs(glr - klr).max())))
    besch["SK0_normiertes_schachbrett"] = {"E_max_je_eps": dict(zip([str(e) for e in SB["eps"]], En)),
                                           "steigung": ols(np.log(eps), np.log(En))}
    # ---------------- Kontinuum der Pakete ----------------
    K = np.load(os.path.join(kont, "kontinuum.npz"))
    kb = K["bins"]
    kpsi = K["psi_p"]
    kquad = K["quad"]
    pp = K["pruefpunkte"]
    Wc = []
    nc = []
    fRc = []
    for c in range(kd.NP):
        b = kb[c]
        Sw = (b[:, :, 0] + b[:, :, 1]).sum(axis=1)
        Sx = b[:, :, 2].sum(axis=1)
        Sx2 = b[:, :, 3].sum(axis=1)
        sx = np.sqrt(np.maximum(Sx2 / Sw - (Sx / Sw) ** 2, 0.0))
        W = int(min(np.ceil(4.0 * sx.max()), 140))
        Wc.append(W)
        j0_, j1_ = fenster(W)
        nR = b[:, j0_:j1_, 0].sum(axis=1)
        nL = b[:, j0_:j1_, 1].sum(axis=1)
        nc.append((nR + nL) / kd.W_SCHEIBE)
        fRc.append(nR / (nR + nL))
    nc = np.array(nc)
    fRc = np.array(fRc)
    tk = np.array([kd.TA[c] + kd.W_SCHEIBE * (np.arange(kd.N_SCHEIBEN) + 0.5) for c in range(kd.NP)])
    besch["kontinuum"] = {"fenster_halbbreite_W": Wc, "norm_c_anfang_ende": [[float(nc[c, :4].mean()), float(nc[c, -4:].mean())]
                                                                         for c in range(kd.NP)],
                          "quad_gegen_k_rel": [[float(np.max(np.abs(kquad[c, i] - kpsi[c, i])) / np.max(np.abs(kpsi[c, i])))
                                                for i in range(3)] for c in range(kd.NP)]}
    # ---------------- Kausalmenge: Daten laden ----------------
    daten = {}
    for rho in rhos:
        fp = sorted(glob.glob(os.path.join(lauf, f"paket-r{int(rho)}-s*.npz")), key=lambda p: int(p.split("-s")[-1].split(".")[0]))
        fq = sorted(glob.glob(os.path.join(lauf, f"punkt-r{int(rho)}-s*.json")), key=lambda p: int(p.split("-s")[-1].split(".")[0]))
        Pp, Sum, sa = [], [], []
        for f in fp:
            kopf = json.load(open(f.replace(".npz", ".json")))
            if not kopf.get("endlich", False):
                continue
            z = np.load(f)
            Pp.append(z["psi_p"])
            Sum.append(z["summen"])
            sa.append(int(f.split("-s")[-1].split(".")[0]))
        Q, sq = [], []
        for f in fq:
            kopf = json.load(open(f))
            if not kopf.get("endlich", False):
                continue
            Q.append(np.stack([np.array(kopf["SRR_re"]) + 1j * np.array(kopf["SRR_im"]),
                               np.array(kopf["SLR_re"]) + 1j * np.array(kopf["SLR_im"])]))
            sq.append(int(f.split("-s")[-1].split(".")[0]))
        daten[rho] = {"paket": np.array(Pp), "summen": np.array(Sum), "punkt": np.array(Q), "saaten_paket": sa,
                      "saaten_punkt": sq}
    vollst = all(len(daten[r]["saaten_paket"]) >= n_soll and len(daten[r]["saaten_punkt"]) >= n_soll for r in rhos)
    # Kontinuum des Propagators an den Pruefpunkten
    TAU = kd.TAUS[None, :] * np.ones((kd.ZETAS.size, 1))
    ZET = kd.ZETAS[:, None] * np.ones((1, kd.TAUS.size))
    kRR = (-(kd.M / 2.0) * np.exp(ZET) * j1(kd.M * TAU)).astype(np.complex128)
    kLR = -0.5j * kd.M * j0(kd.M * TAU)
    kprop = np.stack([kRR, kLR])  # (2, nz, nt)

    def tests_fuer(rho):
        """Liste der Pruefpunkt-Tests: Propagator (2 x 5 x 8) und Pakete (NP x 3 x 2)."""
        out = []
        Q = daten[rho]["punkt"]  # (n, 2, nz, nt)
        n = Q.shape[0]
        for comp in range(2):
            for a in range(kd.ZETAS.size):
                for b in range(kd.TAUS.size):
                    z = Q[:, comp, a, b]
                    m = z.mean()
                    sd = float(np.sqrt(z.real.var(ddof=1) + z.imag.var(ddof=1)))
                    ref = kprop[comp, a, b]
                    out.append({"art": "propagator", "komponente": ["S_RR", "S_LR"][comp], "zeta": float(kd.ZETAS[a]),
                                "tau": float(kd.TAUS[b]), "mittel": [float(m.real), float(m.imag)],
                                "kontinuum": [float(ref.real), float(ref.imag)], "abw_in_SE": float(abs(m - ref) / (sd / np.sqrt(n))),
                                "rel_streuung": float(sd / abs(ref))})
        P = daten[rho]["paket"]  # (n, NP, 24, 2)
        n = P.shape[0]
        for c in range(kd.NP):
            for i in range(3):
                for comp in range(2):
                    z = P[:, c, i, comp]
                    m = z.mean()
                    sd = float(np.sqrt(z.real.var(ddof=1) + z.imag.var(ddof=1)))
                    ref = kpsi[c, i, comp]
                    out.append({"art": "paket", "paket": kd.PAKETE[c]["name"], "punkt": i, "komponente": ["R", "L"][comp],
                                "t": float(pp[c, i, 0]), "x": float(pp[c, i, 1]), "mittel": [float(m.real), float(m.imag)],
                                "kontinuum": [float(ref.real), float(ref.imag)],
                                "abw_in_SE": float(abs(m - ref) / (sd / np.sqrt(n))), "rel_streuung": float(sd / abs(ref))})
        return out
    T = {rho: tests_fuer(rho) for rho in rhos}
    # ---------------- SK1 ----------------
    rmax = max(rhos)
    t1 = T[rmax]
    n_in = int(sum(t["abw_in_SE"] <= 3.0 for t in t1))
    anteil = n_in / len(t1)
    urteile["SK1"] = {"urteil": ("eingetroffen" if anteil >= 0.9 else "nicht eingetroffen") if vollst else "nicht auswertbar",
                      "werte": {"rho": rmax, "zahl_tests": len(t1), "zahl_innerhalb_3SE": n_in, "anteil": anteil,
                                "max_abw_in_SE": max(t["abw_in_SE"] for t in t1),
                                "anteil_propagator": float(np.mean([t["abw_in_SE"] <= 3 for t in t1 if t["art"] == "propagator"])),
                                "anteil_paket": float(np.mean([t["abw_in_SE"] <= 3 for t in t1 if t["art"] == "paket"])),
                                "anteil_je_rho": {str(int(r)): float(np.mean([t["abw_in_SE"] <= 3 for t in T[r]])) for r in rhos}}}
    besch["tests"] = {str(int(r)): T[r] for r in rhos}
    # ---------------- SK2 ----------------
    r_lo, r_hi = min(rhos), max(rhos)
    lr = np.log(np.array([t["rel_streuung"] for t in T[r_hi]])) - np.log(np.array([t["rel_streuung"] for t in T[r_lo]]))
    steig2 = float(lr.mean() / np.log(r_hi / r_lo))
    arten = {}
    for art in ("propagator", "paket"):
        sel = np.array([t["art"] == art for t in T[r_hi]])
        arten[art] = float(lr[sel].mean() / np.log(r_hi / r_lo))
    gm = {str(int(r)): float(np.exp(np.mean(np.log([t["rel_streuung"] for t in T[r]])))) for r in rhos}
    urteile["SK2"] = {"urteil": ("eingetroffen" if -0.65 <= steig2 <= -0.35 else "nicht eingetroffen") if vollst else "nicht auswertbar",
                      "werte": {"steigung": steig2, "band": [-0.65, -0.35], "steigung_je_art": arten,
                                "rel_streuung_geom_mittel_je_rho": gm}}
    # ---------------- SK3 und Komponenten ----------------
    sk3 = []
    nk_all = {}
    fR_all = {}
    for rho in rhos:
        S = daten[rho]["summen"]  # (n, NP, 40, 280, 4)
        for c in range(kd.NP):
            j0_, j1_ = fenster(Wc[c])
            nR = S[:, c, :, j0_:j1_, 0].sum(axis=2) / (rho * kd.W_SCHEIBE)
            nL = S[:, c, :, j0_:j1_, 1].sum(axis=2) / (rho * kd.W_SCHEIBE)
            n = nR + nL
            R = n.mean(axis=0) / nc[c]
            G = float(R[-4:].mean() / R[:4].mean())
            sk3.append({"rho": rho, "paket": kd.PAKETE[c]["name"], "R_anfang": float(R[:4].mean()), "R_ende": float(R[-4:].mean()),
                        "G": G, "R_max": float(R.max()), "ok": bool(G <= 1.5)})
            nk_all[(rho, c)] = (n, R)
            fR_all[(rho, c)] = nR / n
    urteile["SK3"] = {"urteil": ("eingetroffen" if all(k["ok"] for k in sk3) else "nicht eingetroffen") if vollst else "nicht auswertbar",
                      "werte": {"G_max": max(k["G"] for k in sk3), "einzeln": sk3}}
    # Komponentenwechsel (beschreibend): Anteil R im Fenster, Saatmittel gegen Kontinuum; Frequenz aus Nulldurchgaengen
    kompo = {}
    for c in range(kd.NP):
        ent = {"kontinuum_anteil_R": fRc[c].tolist()}
        for rho in rhos:
            f = fR_all[(rho, c)]
            ent[f"rho{int(rho)}_mittel"] = f.mean(axis=0).tolist()
            ent[f"rho{int(rho)}_std"] = f.std(axis=0, ddof=1).tolist()
            ent[f"rho{int(rho)}_max_abw_mittel_gegen_kontinuum"] = float(np.max(np.abs(f.mean(axis=0) - fRc[c])))
        y = fRc[c] - fRc[c].mean()
        zc = np.where(np.diff(np.sign(y)) != 0)[0]
        if zc.size >= 3:
            per = 2 * np.mean(np.diff(tk[c][zc]))
            ent["kontinuum_kreisfrequenz_aus_nulldurchgaengen"] = float(2 * np.pi / per)
        kompo[kd.PAKETE[c]["name"]] = ent
    besch["komponenten"] = kompo
    besch["saaten"] = {str(int(r)): {"paket": daten[r]["saaten_paket"], "punkt": daten[r]["saaten_punkt"]} for r in rhos}
    # ---------------- Bilder ----------------
    # 1 Schachbrett: Fehler gegen Schritt
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    ax[0].loglog(eps, E, "o-", label=f"max. Abweichung (Steigung {steig0:.3f})")
    ax[0].loglog(eps, E[1] * eps / 0.01, "k:", label="Steigung 1")
    ax[0].loglog(eps, En, "s--", label="normiertes Schachbrett (beschreibend)")
    ax[0].axhline(1e-2, color="r", lw=0.8, label="Schwelle 1e-2")
    ax[0].set_xlabel("Schritt eps")
    ax[0].set_ylabel("max |S_eps - S| an 80 Pruefwerten")
    ax[0].legend(fontsize=8)
    ax[0].set_title("SK0: Feynman-Schachbrett gegen Dirac-Propagator")
    for e in SB["eps"]:
        ax[1].semilogy(SB["taus"], je_tau[str(e)], "o-", label=f"eps = {e}")
    ax[1].axhline(1e-2, color="r", lw=0.8)
    ax[1].set_xlabel("tau (Eigenzeit des Pruefpunkts)")
    ax[1].set_ylabel("max Abweichung ueber zeta und Komponente")
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "schachbrett_fehler.png"), dpi=110)
    plt.close(fig)
    # 2 Saatmittel gegen Kontinuum: Propagator je Komponente (rho max), Pakete Profil bei ta + 20
    fig, ax = plt.subplots(2, 3, figsize=(16, 8.5))
    Q = daten[rmax]["punkt"]
    nq = Q.shape[0]
    for comp in range(2):
        for ia, zi in enumerate([0, 2, 4]):
            a = ax[comp, ia] if ia < 2 else ax[comp, 2]
            if ia == 2:
                continue
            for sgn, zz in enumerate([zi]):
                m = Q[:, comp, zz, :].mean(axis=0)
                se = csd(Q[:, comp, zz, :]) / np.sqrt(nq)
                part = (lambda w: w.real) if comp == 0 else (lambda w: w.imag)
                a.errorbar(kd.TAUS, part(m), yerr=se, fmt="o", ms=4, label=f"Kausalmenge rho = {rmax:g}, Mittel +- SE")
                tt = np.linspace(0.05, 16.5, 400)
                if comp == 0:
                    a.plot(tt, -(0.5) * np.exp(kd.ZETAS[zz]) * j1(tt), "k-", lw=1, label="Kontinuum")
                else:
                    a.plot(tt, -0.5 * j0(tt), "k-", lw=1, label="Kontinuum")
                a.set_title(f"{['Re S_RR (glatt)', 'Im S_LR'][comp]}, zeta = {kd.ZETAS[zz]:g}", fontsize=9)
                a.set_xlabel("tau")
                a.legend(fontsize=7)
    for c in range(kd.NP):
        a = ax[c, 2]
        P = daten[rmax]["paket"][:, c, 3:, :]
        x = pp[c, 3:, 1]
        for comp, col in ((0, "C0"), (1, "C1")):
            m = P[:, :, comp].mean(axis=0)
            se = csd(P[:, :, comp]) / np.sqrt(P.shape[0])
            a.errorbar(x, np.abs(m), yerr=se, fmt="o", ms=3, color=col, label=f"|psi_{'RL'[comp]}| Saatmittel")
            a.plot(x, np.abs(kpsi[c, 3:, comp]), "-", color=col, lw=1, label=f"|psi_{'RL'[comp]}| Kontinuum")
        a.set_title(f"Paket {kd.PAKETE[c]['name']}: Profil bei t = {pp[c, 3, 0]:g}, rho = {rmax:g}", fontsize=9)
        a.set_xlabel("x")
        a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "saatmittel_kontinuum.png"), dpi=110)
    plt.close(fig)
    # 3 Streuung gegen rho
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    for k, art in enumerate(("propagator", "paket")):
        a = ax[k]
        sel = [i for i, t in enumerate(T[r_hi]) if t["art"] == art]
        for i in sel:
            a.loglog([r_lo, r_hi], [T[r_lo][i]["rel_streuung"], T[r_hi][i]["rel_streuung"]], "-", color="C0", alpha=0.35, lw=0.8)
        g_lo = np.exp(np.mean([np.log(T[r_lo][i]["rel_streuung"]) for i in sel]))
        g_hi = np.exp(np.mean([np.log(T[r_hi][i]["rel_streuung"]) for i in sel]))
        a.loglog([r_lo, r_hi], [g_lo, g_hi], "o-", color="k", lw=2, label=f"geom. Mittel, Steigung {arten[art]:.3f}")
        a.loglog([r_lo, r_hi], [g_lo, g_lo * (r_hi / r_lo) ** -0.5], "r:", label="Steigung -1/2")
        a.set_xlabel("rho")
        a.set_ylabel("relative Streuung ueber Saaten")
        a.set_title(f"Streuung gegen rho ({art})")
        a.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "streuung_rho.png"), dpi=110)
    plt.close(fig)
    # 4 Norm gegen t
    fig, ax = plt.subplots(1, kd.NP, figsize=(12, 4.5))
    for c in range(kd.NP):
        a = ax[c]
        for k, rho in enumerate(rhos):
            n, R = nk_all[(rho, c)]
            a.plot(tk[c], R, color=f"C{k}", label=f"Saatmittel Norm / Kontinuum, rho = {rho:g}")
        a.axhline(1.0, color="k", lw=0.8)
        a.axhline(1.5, color="r", lw=0.8, ls=":")
        a.set_xlabel("t")
        a.set_title(f"Norm (Fenster) gegen t, Paket {kd.PAKETE[c]['name']}")
        a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "norm_t.png"), dpi=110)
    plt.close(fig)
    # 5 Komponentenwechsel
    fig, ax = plt.subplots(1, kd.NP, figsize=(12, 4.5))
    for c in range(kd.NP):
        a = ax[c]
        a.plot(tk[c], fRc[c], "k-", lw=1.5, label="Kontinuum")
        for k, rho in enumerate(rhos):
            f = fR_all[(rho, c)]
            m = f.mean(axis=0)
            s = f.std(axis=0, ddof=1)
            a.plot(tk[c], m, color=f"C{k}", label=f"Saatmittel, rho = {rho:g}")
            a.fill_between(tk[c], m - s, m + s, color=f"C{k}", alpha=0.2)
        a.set_xlabel("t")
        a.set_ylabel("Anteil |psi_R|^2 an der Norm (Fenster)")
        a.set_title(f"Komponentenwechsel, Paket {kd.PAKETE[c]['name']} (Band: Streuung ueber Saaten)", fontsize=9)
        a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "komponentenwechsel.png"), dpi=110)
    plt.close(fig)
    out = {"urteile": urteile, "beschreibend": besch, "rhos": rhos, "n_saaten_soll": n_soll, "skript_sha256": SKRIPT_SHA,
           "kausal_dirac_sha256": kd.SKRIPT_SHA, "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(aus, "auswertung.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: urteile[k]["urteil"] for k in urteile}))


if __name__ == "__main__":
    main()
