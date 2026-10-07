"""KAUSAL-WELLE-4D: Auswertung nach PLAN.md (Urteilsregeln Abschnitt 6), Bilder, auswertung.json.

Aufruf (nur ueber kleintest.sh): auswertung4d.py <laufordner> <kontinuumordner> <ausgabeordner> <rho1,rho2,rho3> <n_saaten>
"""
import glob
import hashlib
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal4d as kd  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
NP = 9  # Pruefpunkte je Konfiguration


def ols(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    xm = x.mean()
    return float(np.sum((x - xm) * (y - y.mean())) / np.sum((x - xm) ** 2))


def main():
    lauf, kont, aus = sys.argv[1], sys.argv[2], sys.argv[3]
    rhos = [float(r) for r in sys.argv[4].split(",")]
    n_soll = int(sys.argv[5])
    os.makedirs(aus, exist_ok=True)
    K = np.load(os.path.join(kont, "kontinuum.npz"))
    KJ = json.load(open(os.path.join(kont, "kontinuum.json")))
    pp = K["pruefpunkte"]
    phi_k = K["phi_k"]
    ref = K["quad_kappe"]                      # (NC, 9): Bezug KV1/KV2 (gekappte Quelle, direkte Faltung)
    norm_c = K["norm_c"]
    jo = K["johnston"]                         # (n_rho, n_gamma, NC, npkt)
    jo_rhos = [float(x) for x in K["johnston_rhos"]]
    besch = {"kontinuum": {k: KJ[k] for k in KJ if k not in ("zeiten",)}}
    daten = {}
    for rho in rhos:
        fs = sorted(glob.glob(os.path.join(lauf, f"feld-r{rho:g}-s*.npz")),
                    key=lambda p: int(p.split("-s")[-1].split(".")[0]))
        d = {"saaten": [], "phi": [], "n": [], "LN": [], "N": [], "lz_s": [], "lz_n": [], "maxphi": [], "endlich": []}
        for f in fs:
            s = int(f.split("-s")[-1].split(".")[0])
            kopf = json.load(open(f.replace(".npz", ".json")))
            z = np.load(f)
            d["endlich"].append(bool(kopf["endlich"]))
            if not kopf["endlich"]:
                continue
            d["saaten"].append(s)
            d["phi"].append(z["phi_p"])
            d["n"].append(z["summen"][:, :, :, 0].sum(axis=2) / (rho * kd.SCHEIBE_W))
            d["LN"].append(kopf["L_je_N"])
            d["N"].append(kopf["N"])
            d["lz_s"].append(kopf["linkzahl_zeitklassen_summe"])
            d["lz_n"].append(kopf["linkzahl_zeitklassen_n"])
            d["maxphi"].append(kopf["max_abs_phi"])
        for k in ("phi", "n", "LN", "N", "lz_s", "lz_n", "maxphi"):
            d[k] = np.array(d[k])
        daten[rho] = d
    vollst = all(len(daten[r]["saaten"]) >= n_soll for r in rhos) and all(all(daten[r]["endlich"]) for r in rhos)
    rmax = max(rhos)
    urteile = {}
    # ---------- KV0 ----------
    kv0 = []
    for rho in rhos:
        LN = daten[rho]["LN"]
        m = float(LN.mean())
        se = float(LN.std(ddof=1) / np.sqrt(LN.size))
        E = float(KJ["linkzahl_erwartung"][str(rho)])
        Ef = float(KJ["linkzahl_erwartung_fein"][str(rho)])
        kv0.append({"rho": rho, "N_mittel": float(daten[rho]["N"].mean()), "L_je_N_mittel": m, "SE": se,
                    "erwartung": E, "erwartung_fein": Ef, "integral_rel_abw_fein": abs(E - Ef) / Ef,
                    "abw_in_SE": (m - Ef) / se, "ok": bool(abs(m - Ef) <= 3 * se), "zahl_saaten": int(LN.size)})
    urteile["KV0"] = {"urteil": ("eingetroffen" if all(k["ok"] for k in kv0) else "nicht eingetroffen")
                      if vollst else "nicht auswertbar", "werte": {"je_rho": kv0}}
    # ---------- KV1, KV2 ----------
    tests = {}
    srel = {}
    for rho in rhos:
        P = daten[rho]["phi"][:, :, :NP]          # (n, NC, 9)
        n = P.shape[0]
        lst = []
        ir = jo_rhos.index(rho) if rho in jo_rhos else None
        for c in range(kd.NC):
            for i in range(NP):
                z = P[:, c, i]
                m = z.mean()
                sd = np.sqrt(z.real.var(ddof=1) + z.imag.var(ddof=1))
                se = sd / np.sqrt(n)
                e = {"rho": rho, "eta": kd.ETAS[c], "t": float(pp[c, i, 0]), "x": float(pp[c, i, 1]),
                     "z": float(pp[c, i, 3]), "mittel": [float(m.real), float(m.imag)],
                     "bezug": [float(ref[c, i].real), float(ref[c, i].imag)], "abw_in_SE": float(abs(m - ref[c, i]) / se),
                     "rel_streuung": float(sd / abs(ref[c, i])), "abw_rel": float(abs(m - ref[c, i]) / abs(ref[c, i])),
                     "abw_k_raum_in_SE": float(abs(m - phi_k[c, i]) / se)}
                if ir is not None:
                    jv = jo[ir, 0, c, i]
                    e["johnston_erwartung"] = [float(jv.real), float(jv.imag)]
                    e["abw_johnston_in_SE"] = float(abs(m - jv) / se)
                lst.append(e)
                srel[(rho, c, i)] = sd / abs(ref[c, i])
        tests[str(rho)] = lst
    t1 = tests[str(rmax)]
    anteil = float(np.mean([e["abw_in_SE"] <= 3.0 for e in t1]))
    urteile["KV1"] = {"urteil": ("eingetroffen" if anteil >= 0.8 else "nicht eingetroffen") if vollst else "nicht auswertbar",
                      "werte": {"rho": rmax, "anteil_innerhalb_3SE": anteil, "zahl_punkte": len(t1),
                                "abw_in_SE": [e["abw_in_SE"] for e in t1], "abw_rel": [e["abw_rel"] for e in t1],
                                "anteil_je_rho": {str(r): float(np.mean([e["abw_in_SE"] <= 3.0 for e in tests[str(r)]]))
                                                  for r in rhos},
                                "anteil_gegen_johnston_erwartung_je_rho": {
                                    str(r): float(np.mean([e.get("abw_johnston_in_SE", np.inf) <= 3.0 for e in tests[str(r)]]))
                                    for r in rhos}}}
    gm = [float(np.exp(np.mean([np.log(srel[(r, c, i)]) for c in range(kd.NC) for i in range(NP)]))) for r in rhos]
    faellt = all(gm[i] > gm[i + 1] for i in range(len(gm) - 1))
    klein = gm[rhos.index(rmax)] < 0.5
    alle_klein = all(srel[(rmax, c, i)] < 0.5 for c in range(kd.NC) for i in range(NP))
    urteile["KV2"] = {"urteil": ("eingetroffen" if (faellt and klein) else "nicht eingetroffen") if vollst else "nicht auswertbar",
                      "werte": {"rel_streuung_geom_mittel_je_rho": dict(zip([str(r) for r in rhos], gm)),
                                "faellt_mit_rho": faellt, "kleiner_0_5_bei_rho_max": klein,
                                "steigung_log_gegen_log_rho": ols(np.log(rhos), np.log(gm)),
                                "strenge_lesart_alle_punkte_kleiner_0_5": alle_klein,
                                "rel_streuung_je_punkt_rho_max": [float(srel[(rmax, c, i)]) for c in range(kd.NC)
                                                                  for i in range(NP)]}}
    besch["tests"] = tests
    # ---------- KV3 ----------
    kv3 = []
    for rho in rhos:
        nn = daten[rho]["n"]                      # (n, NC, 4)
        for c in range(kd.NC):
            R = nn[:, c, :].mean(axis=0) / norm_c[c]
            G = float(R[-1] / R[0])
            Gs = (nn[:, c, -1] / norm_c[c, -1]) / (nn[:, c, 0] / norm_c[c, 0])
            kv3.append({"rho": rho, "eta": kd.ETAS[c], "R": R.tolist(), "G": G, "R_max": float(R.max()),
                        "ok": bool(G <= 1.5), "G_einzelsaat_max": float(Gs.max()), "G_einzelsaat_median": float(np.median(Gs))})
    urteile["KV3"] = {"urteil": ("eingetroffen" if all(k["ok"] for k in kv3) else "nicht eingetroffen") if vollst
                      else "nicht auswertbar", "werte": {"G_max": max(k["G"] for k in kv3), "einzeln": kv3}}
    besch["max_abs_phi_je_rho"] = {str(r): float(daten[r]["maxphi"].max()) for r in rhos}
    besch["saaten_je_rho"] = {str(r): daten[r]["saaten"] for r in rhos}
    besch["N_je_rho"] = {str(r): daten[r]["N"].tolist() for r in rhos}
    besch["L_je_N_je_rho"] = {str(r): daten[r]["LN"].tolist() for r in rhos}
    lzk = {}
    for r in rhos:
        s_ = daten[r]["lz_s"].sum(axis=0)
        n_ = daten[r]["lz_n"].sum(axis=0)
        lzk[str(r)] = {"gemessen": (s_ / np.maximum(n_, 1)).tolist(), "elemente": n_.tolist(),
                       "erwartung": KJ["linkzahl_erwartung_zeitklassen"][str(r)]}
    besch["linkzahl_zeitklassen"] = lzk
    # ---------- Bilder ----------
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.8))
    for c in range(kd.NC):
        a = ax[c]
        z = pp[c, NP:, 3]
        P = daten[rmax]["phi"][:, c, NP:]
        m = P.mean(axis=0)
        se_r = P.real.std(axis=0, ddof=1) / np.sqrt(P.shape[0])
        se_i = P.imag.std(axis=0, ddof=1) / np.sqrt(P.shape[0])
        a.errorbar(z, m.real, yerr=se_r, fmt="o", ms=3, color="C0", label="Re, Saatmittel +- SE")
        a.errorbar(z, m.imag, yerr=se_i, fmt="s", ms=3, color="C1", label="Im, Saatmittel +- SE")
        a.plot(z, phi_k[c, NP:].real, "-", color="C0", lw=1, label="Re, Kontinuum (k-Raum)")
        a.plot(z, phi_k[c, NP:].imag, "-", color="C1", lw=1, label="Im, Kontinuum (k-Raum)")
        if rmax in jo_rhos:
            jv = jo[jo_rhos.index(rmax), 0, c, NP:]
            a.plot(z, jv.real, ":", color="C0", lw=1.2, label=f"Re, Johnston-Erwartung rho = {rmax:g} [M]")
            a.plot(z, jv.imag, ":", color="C1", lw=1.2, label=f"Im, Johnston-Erwartung rho = {rmax:g} [M]")
        a.set_title(f"eta = {kd.ETAS[c]:g}, t = {kd.PROFIL_T:g}, x = y = 0, rho = {rmax:g}, {P.shape[0]} Saaten")
        a.set_xlabel("z")
        a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "saatmittel_kontinuum.png"), dpi=110)
    plt.close(fig)
    fig, ax = plt.subplots(1, 1, figsize=(6.5, 4.8))
    for c in range(kd.NC):
        for i in range(NP):
            ax.plot(rhos, [srel[(r, c, i)] for r in rhos], "-", color=f"C{c}", alpha=0.3, lw=0.8)
    ax.plot(rhos, gm, "ko-", lw=2, label="geometrisches Mittel (18 Pruefpunkte)")
    ax.plot(rhos, gm[0] * (np.array(rhos) / rhos[0]) ** -0.5, "k:", label="Steigung -1/2 (Bezug)")
    ax.axhline(0.5, color="r", lw=0.8, label="Schwelle 0,5 (KV2)")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("rho")
    ax.set_ylabel("relative Streuung von phi ueber Saaten")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "streuung_rho.png"), dpi=110)
    plt.close(fig)
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    tm = kd.SCHEIBE_T0 + kd.SCHEIBE_W * (np.arange(kd.N_SCHEIBEN) + 0.5)
    for c in range(kd.NC):
        a = ax[c]
        for k, rho in enumerate(rhos):
            nn = daten[rho]["n"][:, c, :]
            R = nn / norm_c[c][None, :]
            a.plot(tm, R.mean(axis=0), "o-", color=f"C{k}", label=f"rho = {rho:g}: Saatmittel n / n_c")
            a.fill_between(tm, np.percentile(R, 10, axis=0), np.percentile(R, 90, axis=0), color=f"C{k}", alpha=0.15)
        a.axhline(1.0, color="k", lw=0.8)
        a.set_title(f"Norm je Zeitscheibe / Kontinuum, eta = {kd.ETAS[c]:g} (Band: 10-90 % der Saaten)", fontsize=9)
        a.set_xlabel("t")
        a.set_yscale("log")
        a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "norm_t.png"), dpi=110)
    plt.close(fig)
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    for k, rho in enumerate(rhos):
        ax[0].plot(daten[rho]["N"], daten[rho]["LN"], ".", color=f"C{k}", alpha=0.6)
        e = [x for x in kv0 if x["rho"] == rho][0]
        ax[0].errorbar([e["N_mittel"]], [e["L_je_N_mittel"]], yerr=[e["SE"]], fmt="o", color=f"C{k}",
                       label=f"rho = {rho:g}: Saatmittel +- SE")
        ax[0].plot([e["N_mittel"]], [e["erwartung_fein"]], "kx", ms=10)
    ax[0].plot([], [], "kx", label="exakte Erwartung (Integral fuer D)")
    ax[0].set_xscale("log")
    ax[0].set_xlabel("N")
    ax[0].set_ylabel("Links je Element L/N")
    ax[0].legend(fontsize=7)
    tk = kd.LZ_T0 + kd.LZ_W * (np.arange(kd.LZ_N) + 0.5)
    for k, rho in enumerate(rhos):
        ax[1].plot(tk, lzk[str(rho)]["gemessen"], "o", color=f"C{k}", ms=4, label=f"gemessen, rho = {rho:g}")
        ax[1].plot(tk, lzk[str(rho)]["erwartung"], "-", color=f"C{k}", lw=1, label=f"Erwartung, rho = {rho:g}")
    ax[1].set_xlabel("t (Zeitklasse des Elements)")
    ax[1].set_ylabel("Vergangenheitslinks je Element")
    ax[1].set_title("Randeffekt: wenig Links nahe dem unteren Rand von D", fontsize=9)
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "linkzahl_n.png"), dpi=110)
    plt.close(fig)
    out = {"urteile": urteile, "beschreibend": besch, "rhos": rhos, "n_saaten_soll": n_soll,
           "skript_sha256": SKRIPT_SHA, "kausal4d_sha256": kd.SKRIPT_SHA,
           "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(aus, "auswertung.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps({k: urteile[k]["urteil"] for k in urteile}))


if __name__ == "__main__":
    main()
