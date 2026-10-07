#!/usr/bin/env python3
"""REGGE-RAND-1: mechanische Auswertung der Urteilsregeln (PLAN.md Abschnitte 6 bis 8) und Bilder.
Aufruf: rr_auswertung.py --lauf <ordner>  (liest rr_linear.json und, falls vorhanden, rr_nl.json)."""
import argparse
import json
import math
import os

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

GM = 1.0


def urteil(ok):
    return "eingetroffen" if ok else "nicht eingetroffen"


def sym_at(st, k):
    return sum(v * math.cos(k[0] * d[0] + k[1] * d[1] + k[2] * d[2]) for d, v in st.items())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lauf", required=True)
    ap.add_argument("--L_haupt", default="64")  # nur fuer den Rauchlauf anders
    ap.add_argument("--R_urteil", default="18")  # RR5; nur fuer den Rauchlauf anders
    a = ap.parse_args()
    p_lin = os.path.join(a.lauf, "rr_linear.json")
    U = {}
    Z = {}
    APs = {}
    lin = json.load(open(p_lin)) if os.path.exists(p_lin) else None
    nl = None
    nl_dateien = sorted(f for f in os.listdir(a.lauf) if f.startswith("rr_nl") and f.endswith(".json"))
    for f in nl_dateien:
        part = json.load(open(os.path.join(a.lauf, f)))
        if nl is None:
            nl = part
        else:
            assert part["L"] == nl["L"] and part["a"] == nl["a"] and part["R"] == nl["R"]
            nl["paare"] += part["paare"]
    Z["rr5_dateien"] = nl_dateien
    if lin is None:
        for k in ("RR0", "RR1", "RR2", "RR3", "RR4"):
            U[k] = {"urteil": "nicht auswertbar", "vermerk": "rr_linear.json fehlt"}
    else:
        st = {tuple(int(x) for x in k.strip("()").split(",")): v for k, v in lin["schablone"].items()}
        # RR0
        e8 = lin["rr0_flach_L8"]["max_eps"]
        e64 = lin["rr0_flach_L64"]["max_eps"]
        dn = lin["dicht"]
        symx = max(dn[L]["sym_rel"] for L in dn)
        onex = max(dn[L]["A_mal_1_rel"] for L in dn)
        ok0 = (e8 < 1e-12) and (e64 < 1e-12) and (symx <= 1e-12) and (onex <= 1e-12)
        U["RR0"] = {"urteil": urteil(ok0), "werte": {"max_eps_L8": e8, "max_eps_L64": e64, "max_sym_rel": symx,
                                                    "max_A_mal_1_rel": onex,
                                                    "skaliert_1p3_max_eps": lin["skaliert_1p3_max_eps"]}}
        # RR1
        okd = all(dn[L]["n_null"] == 1 and dn[L]["ueberlapp_konst"] >= 1 - 1e-9 and dn[L]["n_negativ"] == 0
                  for L in dn)
        s64 = lin["symbol_L64"]
        oks = s64["min_k_ungleich_0"] > 1e-9 * s64["max"]
        U["RR1"] = {"urteil": urteil(okd and oks),
                    "werte": {"dicht": {L: {k: dn[L][k] for k in ("n_null", "ueberlapp_konst", "n_negativ", "eig_2",
                                                                 "eig_max", "eig_minus_symbol_max")} for L in dn},
                              "symbol_L64_min_k_ungleich_0": s64["min_k_ungleich_0"], "symbol_L64_max": s64["max"],
                              "zonenrand": lin["symbol_zonenrand"]}}
        s64sol = lin["loesungen"][a.L_haupt]
        P = s64sol["punkt"]
        K = s64sol["kugel6"]
        # RR2
        v2 = P["rr2"]["max_abw_korr"]
        U["RR2"] = {"urteil": urteil(v2 <= 0.03), "werte": P["rr2"]}
        # RR3
        v3 = P["schalen"]["12"]["S_korr"]
        U["RR3"] = {"urteil": urteil(v3 < 0.02), "werte": P["schalen"]["12"]}
        # RR4
        rows = []
        for gp, gk in zip(P["gauss"], K["gauss"]):
            assert gp["R"] == gk["R"]
            rows.append({"R": gp["R"], "M_G_punkt": gp["M_G"], "M_G_kugel": gk["M_G"],
                         "abw": abs(gp["M_G"] / gk["M_G"] - 1), "M_op_punkt": gp["M_op"], "M_op_kugel": gk["M_op"],
                         "M_kugel_punkt": gp["M_kugel"], "M_kugel_kugel": gk["M_kugel"],
                         "M_G_roh_punkt": gp["M_G_roh"], "M_G_roh_kugel": gk["M_G_roh"]})
        rr4 = max(r["abw"] for r in rows if r["R"] >= 10)
        U["RR4"] = {"urteil": urteil(rr4 <= 0.01), "werte": {"max_abw": rr4, "tabelle": rows},
                    "vermerk": "M_op ist eine Identitaet (diskreter Gauss-Satz); bei A = 8(-Laplace_7) auch M_G"}
        # Agenten-Vorhersagen
        aA = st[(1, 0, 0)]
        aF = st[(1, 1, 0)]
        aR = st[(1, 1, 1)]
        dev1 = max(abs(aA + 8), abs(aF), abs(aR))
        APs["AP1"] = {"ok": dev1 <= 1e-10, "werte": {"a_A": aA, "a_F": aF, "a_R": aR, "a_0": st[(0, 0, 0)],
                                                    "max_abw": dev1}}
        d2 = max(abs(dn[L]["eig_2"] / dn[L]["zweitkleinster_soll_8(2-2cos(2pi/L))"] - 1) for L in dn)
        zpi = lin["symbol_zonenrand"]
        kpi = [k for k in zpi if k.startswith("(3.1416, 3.1416, 3.1416")][0]
        d2b = abs(zpi[kpi] / 96 - 1)
        APs["AP2"] = {"ok": d2 <= 1e-9 and d2b <= 1e-9 and abs(s64["max"] / 96 - 1) <= 1e-9,
                      "werte": {"eig2_rel_abw": d2, "A_pipipi": zpi[kpi], "max_L64": s64["max"]}}
        APs["AP3"] = {"ok": v2 <= 0.01, "werte": v2}
        APs["AP4"] = {"ok": v3 <= 0.005, "werte": v3}
        APs["AP5"] = {"ok": rr4 <= 1e-10, "werte": rr4}
        APs["AP7"] = {"ok": P["rr2"]["max_abw_roh"] > 0.5, "werte": P["rr2"]["max_abw_roh"]}
        # Zusatz: Groessenreihe
        gr = {}
        try:
            r64 = P["strahlen"]
            r128 = lin["loesungen"]["128"]["punkt_strahlen_roh"]
            r256 = lin["loesungen"]["256"]["punkt_strahlen_roh"]
            Ls = np.array([64.0, 128.0, 256.0])
            Mx = np.stack([np.ones(3), 1 / Ls, 1 / Ls ** 3], 1)
            devs = []
            xis = []
            tab = {}
            for u in r128:
                lst = []
                for (p64, p128, p256) in zip(r64[u], r128[u], r256[u]):
                    rr_ = p64[0]
                    if rr_ > 16.01:
                        break
                    coef = np.linalg.solve(Mx, np.array([p64[1], p128[1], p256[1]]))
                    fs = coef[0]
                    lst.append([rr_, fs, p64[2], rr_ * fs / (GM / 2)])
                    if rr_ >= 6:
                        devs.append(abs(p64[2] / fs - 1))
                    if rr_ >= 4:
                        xis.append(2 * coef[1] / GM)
                tab[u] = lst
            gr = {"max_rel_korr64_gegen_FS_6bis16": float(max(devs)), "xi_fit_min": float(min(xis)),
                  "xi_fit_max": float(max(xis)), "strahlen": tab}
        except Exception as ex:  # noqa: BLE001
            gr = {"fehler": repr(ex)}
        Z["groessenreihe"] = gr
        Z["normierung_quadratisch"] = lin["normierung_quadratisch"]
        Z["symbol_klein_k_durch_8k2"] = lin["symbol_klein_k_durch_8k2"]
        Z["residuen_L64"] = {k: s64sol[k] for k in s64sol if "residuum" in k}
        Z["residuen_L32"] = {k: lin["loesungen"]["32"][k] for k in lin["loesungen"]["32"] if "residuum" in k}
        Z["L32"] = {"rr2_max_abw_korr_6bis8": lin["loesungen"]["32"]["punkt"]["rr2"]["max_abw_korr"],
                    "gauss_punkt": lin["loesungen"]["32"]["punkt"]["gauss"],
                    "gauss_kugel": lin["loesungen"]["32"]["kugel6"]["gauss"]}
        Z["kugel6_rr2_gleiche_regel"] = K["rr2"]
        Z["kugel6_schale12"] = K["schalen"].get("12")
        Z["schalen_punkt"] = P["schalen"]
        Z["J0"] = lin["J0"]
        Z["J0_symmetrie"] = lin["J0_symmetrie"]
        Z["schlaefli_l_mal_J"] = lin["schlaefli_l_mal_J"]
        Z["J_cs_minus_fd"] = lin["J_cs_minus_fd"]
        # Bilder
        fig, axs = plt.subplots(1, 2, figsize=(12, 4.6), sharey=True)
        for ax, S, tit in ((axs[0], P, "Punktquelle an einer Ecke"), (axs[1], K, "Kugel Radius 6, gleiche Quelle")):
            for u, lst in S["strahlen"].items():
                arr = np.array(lst)
                ax.plot(arr[:, 0], arr[:, 0] * arr[:, 2] / (GM / 2), "-", lw=1, marker=".", ms=3, label=u)
            arr = np.array(S["strahlen"]["(1, 0, 0)"])
            ax.plot(arr[:, 0], arr[:, 0] * arr[:, 1] / (GM / 2), "k--", lw=1, label="(1,0,0) roh")
            ax.axhspan(0.97, 1.03, color="0.9", zorder=0)
            ax.axvline(6, color="0.6", lw=0.8)
            ax.axvline(16, color="0.6", lw=0.8)
            ax.set_xlabel("r (Gitterabstand)")
            ax.set_title(tit + ", L = 64")
            ax.set_ylim(0.0, 1.15)
        axs[0].set_ylabel("r dpsi / (G M / 2), torus-korrigiert")
        axs[1].legend(fontsize=6, ncol=2)
        fig.tight_layout()
        fig.savefig(os.path.join(a.lauf, "bild-r-dpsi.png"), dpi=130)
        plt.close(fig)
        fig, ax = plt.subplots(figsize=(6.5, 4.2))
        sp = P["schale12_punkte"]
        ax.scatter(sp["cos_111"], sp["f_korr"], s=4, c=sp["r"], cmap="viridis")
        ax.axhline(1.0, color="k", lw=0.8)
        ax.set_xlabel("cos(Winkel zur Kuhn-Raumdiagonale (1,1,1))")
        ax.set_ylabel("r dpsi / (G M/2), korrigiert")
        ax.set_title(f"Schale 11,5 <= r <= 12,5 (L = 64), S = {v3:.2e}")
        fig.tight_layout()
        fig.savefig(os.path.join(a.lauf, "bild-richtung.png"), dpi=130)
        plt.close(fig)
        fig, ax = plt.subplots(figsize=(7, 4.4))
        Rr = [r["R"] for r in rows]
        ax.plot(Rr, [r["M_G_punkt"] for r in rows], "o-", label="M_G Punkt (korr.)")
        ax.plot(Rr, [r["M_G_kugel"] for r in rows], "s--", label="M_G Kugel (korr.)")
        ax.plot(Rr, [r["M_kugel_punkt"] for r in rows], "^-", label="Kugelflaeche, Punkt")
        ax.plot(Rr, [r["M_kugel_kugel"] for r in rows], "v--", label="Kugelflaeche, Kugel")
        ax.plot(Rr, [r["M_G_roh_punkt"] for r in rows], "x:", label="M_G Punkt roh (ohne Hintergrund)")
        ax.plot(Rr, [r["M_G_roh_kugel"] for r in rows], "+:", label="M_G Kugel roh")
        ax.axhline(1.0, color="k", lw=0.7)
        ax.set_xlabel("R (Halbkante des Wuerfels bzw. Kugelradius)")
        ax.set_ylabel("Gauss-Masse / M")
        ax.set_title("Randmasse, L = 64")
        ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(os.path.join(a.lauf, "bild-gauss.png"), dpi=130)
        plt.close(fig)
        # Symbol entlang Gamma-X-M-R-Gamma
        pts = [np.zeros(3), np.array([np.pi, 0, 0]), np.array([np.pi, np.pi, 0]), np.array([np.pi, np.pi, np.pi]),
               np.zeros(3)]
        xs, ys, ys7, yk = [], [], [], []
        s0 = 0.0
        for i in range(4):
            for t in np.linspace(0, 1, 60, endpoint=(i == 3)):
                k = pts[i] + t * (pts[i + 1] - pts[i])
                xs.append(s0 + t * np.linalg.norm(pts[i + 1] - pts[i]))
                ys.append(sym_at(st, k))
                ys7.append(8 * sum(2 - 2 * math.cos(x) for x in k))
                yk.append(8 * float(k @ k))
            s0 += np.linalg.norm(pts[i + 1] - pts[i])
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(xs, ys, "b-", lw=2, label="Regge-Eckenoperator (Schablone)")
        ax.plot(xs, ys7, "y--", lw=1, label="8 x 7-Punkt-Laplace")
        ax.plot(xs, yk, "k:", lw=1, label="8 |k|^2 (Kontinuum)")
        ax.set_ylim(0, 110)
        ax.set_xticks([0, np.pi, 2 * np.pi, 2 * np.pi + np.pi * math.sqrt(1), s0])
        ax.set_xticklabels(["G", "X", "M", "R", "G"])
        ax.set_ylabel("A(k)")
        ax.legend(fontsize=8)
        ax.set_title("Symbol des linearisierten Eckenoperators")
        fig.tight_layout()
        fig.savefig(os.path.join(a.lauf, "bild-symbol.png"), dpi=130)
        plt.close(fig)
    # RR5
    if nl is None:
        U["RR5"] = {"urteil": "nicht auswertbar", "vermerk": "nicht gerechnet (rr_nl*.json fehlt)"}
    else:
        Rj = a.R_urteil
        tab = []
        allconv = True
        for e in nl["paare"]:
            conv = all(e[k]["konvergiert"] for k in ("paar", "plus", "minus"))
            allconv = allconv and conv
            K = e["K_kasten"]
            Mp = e["plus"]["rand"][Rj]
            Mm = e["minus"]["rand"][Rj]
            dM = e["paar"]["rand"][Rj] - Mp - Mm
            Q = dM / (-Mp * Mm / e["d"])  # Plan Abschnitt 7 vor Rauchlauf 3: freie Formel, ohne Kastenkorrektur
            Qb = dM / (-Mp * Mm * K)  # geurteilt [A, nach Rauchlauf 3]: Newton-Kern im selben Kasten
            Qs = {}
            for R in [str(x) for x in nl["R"]] + ["summe_m_durch_psi"]:
                mp_ = e["plus"]["rand"][R]
                mm_ = e["minus"]["rand"][R]
                Qs[R] = (e["paar"]["rand"][R] - mp_ - mm_) / (-mp_ * mm_ * K)
            phis = e["plus"]["phi_selbst_mittel"] + e["minus"]["phi_selbst_mittel"]
            Qk = 1 - phis - (Mp + Mm) * K / 2
            tab.append({"d": e["d"], "m": e["m"], "m_durch_d": e["m_durch_d"], "konvergiert": conv, "Q_kasten": Qb,
                        "Q_frei_ohne_korrektur": Q, "d_mal_K_kasten": e["d_mal_K_kasten"], "Q_kasten_alle_R": Qs,
                        "Q_kontinuum_2_ordnung": Qk, "DeltaM": dM, "M_plus": Mp, "M_minus": Mm,
                        "eigenmasse": e["plus"]["rand"]["eigenmasse"],
                        "phi_selbst_plus": e["plus"]["phi_selbst_mittel"],
                        "psi_max_paar": e["paar"]["psi_max"],
                        "iter": [e[k]["iter"] for k in ("paar", "plus", "minus")]})
        haupt = [t for t in tab if any(abs(t["m_durch_d"] - q) < 1e-12 for q in (0.025, 0.05, 0.1))]
        if not allconv or len(haupt) != 9:
            U["RR5"] = {"urteil": "nicht auswertbar", "vermerk": "nicht alle Loesungen konvergiert oder Paare fehlen",
                        "werte": tab}
        else:
            ok5 = all(abs(t["Q_kasten"] - 1) <= 0.20 for t in haupt)
            U["RR5"] = {"urteil": urteil(ok5), "werte": {"R_geurteilt": int(Rj), "max_abw_Q_kasten":
                                                        max(abs(t["Q_kasten"] - 1) for t in haupt), "tabelle": tab},
                        "vermerk": "geurteilt mit Q_kasten (Randkorrektur nach Rauchlauf 3, PLAN Abschnitt 7 und 9)"}
            q01 = [t["Q_frei_ohne_korrektur"] for t in haupt if abs(t["m_durch_d"] - 0.1) < 1e-12]
            q01b = [t["Q_kasten"] for t in haupt if abs(t["m_durch_d"] - 0.1) < 1e-12]
            APs["AP6"] = {"ok": all(q < 0.7 for q in q01), "werte": {"Q_frei": q01, "Q_kasten": q01b,
                                                                     "ok_mit_Q_kasten": all(q < 0.7 for q in q01b)}}
        fig, ax = plt.subplots(figsize=(6.5, 4.2))
        for d in sorted(set(t["d"] for t in tab)):
            tt = sorted([t for t in tab if t["d"] == d], key=lambda t: t["m_durch_d"])
            ln, = ax.plot([t["m_durch_d"] for t in tt], [t["Q_kasten"] for t in tt], "o-", label=f"Gitter d = {d}")
            ax.plot([t["m_durch_d"] for t in tt], [t["Q_kontinuum_2_ordnung"] for t in tt], "x:", color=ln.get_color(),
                    label=f"Kontinuum 2. Ordnung d = {d}")
            ax.plot([t["m_durch_d"] for t in tt], [t["Q_frei_ohne_korrektur"] for t in tt], "s--", color=ln.get_color(),
                    alpha=0.4, ms=3, label=f"ohne Kastenkorrektur d = {d}")
        ax.axhspan(0.8, 1.2, color="0.9", zorder=0)
        ax.set_xlabel("m/d")
        ax.set_ylabel("Q = DeltaM / (-G M+ M- <K>)")
        ax.set_title("RR5: Bindungsenergie als Randgroesse")
        ax.legend(fontsize=6)
        fig.tight_layout()
        fig.savefig(os.path.join(a.lauf, "bild-rr5.png"), dpi=130)
        plt.close(fig)
    out = {"urteile": U, "agenten_vorhersagen": APs, "zusatz": Z}
    with open(os.path.join(a.lauf, "auswertung.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: v["urteil"] for k, v in U.items()}, indent=1))
    print(json.dumps({k: v["ok"] for k, v in APs.items()}, indent=1))


if __name__ == "__main__":
    main()
