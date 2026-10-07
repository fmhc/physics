"""QBALL-MONOPOL-1: Urteile nach PLAN.md Abschnitt 6 und Bilder. Laeuft nur ueber kleintest.sh auf der .69.

Aufruf: auswertung.py <ordner mit haupt.json, haupt.npz, grob.json, fein-*.json, qmax-*.json> <ausgabe.json>
"""
import glob
import hashlib
import json
import os
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
SCHWELLE_BINDUNG = 1e-3
QM0_SCHWELLE = 1e-3
QM4_BAND = (1.8, 2.2)
FARBEN = {0.0: "#6b7280", 0.5: "#2563eb", 1.0: "#d97706", 2.0: "#059669"}


def lade(p):
    with open(p) as fh:
        return json.load(fh)


def beste(faelle, V0, Q):
    bl = [c for c in faelle if c["V0"] == V0 and abs(c["Q"] - Q) < 1e-9]
    return min(bl, key=lambda c: c["E"]) if bl else None


def haftend(c):
    if c is None or not c["status"].startswith("konvergiert"):
        return False
    if c["kennzahlen"]["anteil_rand"] >= 1e-6:
        return False
    ev = c.get("eigenwerte")
    return ev is not None and min(ev) > -1e-6


def tabelle(H):
    ref = {r["Q"]: r for r in H["referenz"] if r["V0"] == 0.0}
    topf = {(r["Q"], r["V0"]): r["E_topf"] for r in H["referenz"] if r["V0"] != 0.0}
    zeilen = []
    for V0 in H["V0"]:
        for Q in H["Q"]:
            c = beste(H["faelle"], V0, Q)
            if c is None:
                continue
            kz = c["kennzahlen"]
            ef = ref[Q]["E_frei"]
            et = topf.get((Q, V0), ef)
            alle = [x for x in H["faelle"] if x["V0"] == V0 and x["Q"] == Q]
            zeilen.append({"V0": V0, "Q": Q, "E_frei": ef, "E_topf": et, "E_mono": c["E"], "start": c["start"],
                           "status": c["status"], "bindung_frei": ef - c["E"], "bindung_frei_rel": 1 - c["E"] / ef,
                           "bindung_topf": et - c["E"], "topf_allein": ef - et, "z_c": kz["z_c"],
                           "R_halb": ref[Q]["R_halb"], "omega2": kz["omega2"],
                           "winkel_D0_D90": kz.get("winkel_D0_D90"), "punkt_ratio_am_rmax": kz.get("punkt_ratio_am_rmax"),
                           "anteil_r_lt_3": kz["anteil_r_lt_3"], "cos_mittel": kz["cos_mittel"],
                           "J_z": kz["J_z"], "J_materie": kz["J_materie"], "J_kreuz": kz["J_kreuz"],
                           "J_z_plus_Q_halbe_rel": kz["J_z_plus_Q_halbe"] / Q, "exponent_r0": kz.get("exponent_r0"),
                           "eigenwerte": c.get("eigenwerte"), "haftend": haftend(c),
                           "starts": {x["start"]: {"E": x["E"], "status": x["status"], "z_c": x["kennzahlen"]["z_c"],
                                                   "iter": x["iter"]} for x in alle}})
    return zeilen


def urteile(H, art):
    ref = {r["Q"]: r for r in H["referenz"] if r["V0"] == 0.0}
    u = {}
    # QM0
    q = H["qm0"]
    u["QM0"] = {"urteil": "eingetroffen" if abs(q["rel_2d_tabelle"]) <= QM0_SCHWELLE else "nicht eingetroffen",
                "werte": {"E_2d": q["E_2d"], "E_tabelle": q["E_tabelle"], "rel_2d_tabelle": q["rel_2d_tabelle"],
                          "E_1d": q["E_1d"], "rel_1d_tabelle": q["rel_1d_tabelle"], "status": q["status"],
                          "z_c": q["z_c"], "winkel_D0_D90": q["winkel_D0_D90"]}}
    # QM1: Plan (Gitterreferenz E_ref = min(E_frei, E_frei_2D_verschoben)) und Kartenwortlaut (gegen E_frei 1D)
    verl_plan, verl_wort = [], []
    werte = {}
    for Q in H["Q"]:
        c = beste(H["faelle"], 0.0, Q)
        e2 = art[Q]["E_2d_frei_verschoben"] if art.get(Q) is not None else ref[Q]["E_frei"]
        eref = min(ref[Q]["E_frei"], e2)
        werte[str(int(Q))] = {"E_mono": c["E"], "E_frei": ref[Q]["E_frei"], "E_frei_2d_verschoben": e2, "E_ref": eref,
                              "diff_ref": c["E"] - eref, "diff_frei": c["E"] - ref[Q]["E_frei"],
                              "status": c["status"], "z_c": c["kennzahlen"]["z_c"]}
        if c["E"] < eref:
            verl_plan.append(int(Q))
        if c["E"] < ref[Q]["E_frei"]:
            verl_wort.append(int(Q))
    u["QM1"] = {"urteil": "eingetroffen" if not verl_plan else "nicht eingetroffen", "werte": werte,
                "urteil_kartenwortlaut": "eingetroffen" if not verl_wort else "nicht eingetroffen"}
    if verl_plan or verl_wort:
        u["QM1"]["vermerk"] = "unter E_ref bei Q = %s; unter E_frei (1D) bei Q = %s" % (verl_plan, verl_wort)
    # QM2
    geb = {}
    for V0 in H["V0"]:
        if V0 == 0.0:
            continue
        for Q in H["Q"]:
            c = beste(H["faelle"], V0, Q)
            geb[(V0, Q)] = c["E"] < (1 - SCHWELLE_BINDUNG) * ref[Q]["E_frei"]
    treffer = [{"V0": V0, "Q": Q} for (V0, Q), g in geb.items() if g]
    u["QM2"] = {"urteil": "eingetroffen" if treffer else "nicht eingetroffen",
                "werte": {"gebunden": treffer,
                          "bindung_rel": {"%s/%d" % (V0, int(Q)): 1 - beste(H["faelle"], V0, Q)["E"] / ref[Q]["E_frei"]
                                          for (V0, Q) in geb}}}
    # QM3
    qmax = {}
    erfuellt = []
    for V0 in H["V0"]:
        if V0 == 0.0:
            continue
        B = [Q for Q in H["Q"] if geb[(V0, Q)]]
        qmax[str(V0)] = max(B) if B else None
        if B and not geb[(V0, max(H["Q"]))]:
            erfuellt.append(V0)
    u["QM3"] = {"urteil": "eingetroffen" if erfuellt else "nicht eingetroffen",
                "werte": {"Q_max_raster": qmax, "V0_mit_Ende": erfuellt}}
    if not any(qmax.values()):
        u["QM3"]["vermerk"] = "keine Bindung an keinem Rasterpunkt"
    # QM4
    u4 = None
    for Q in H["Q"]:
        st = {}
        for V0 in H["V0"]:
            if V0 == 0.0:
                continue
            c = beste(H["faelle"], V0, Q)
            if haftend(c):
                st[str(V0)] = c["kennzahlen"]["winkel_D0_D90"]
        if st:
            ok = all(QM4_BAND[0] <= v <= QM4_BAND[1] for v in st.values())
            u4 = {"urteil": "eingetroffen" if ok else "nicht eingetroffen",
                  "werte": {"Q": Q, "D0_D90_je_V0": st}}
            break
    if u4 is None:
        u4 = {"urteil": "nicht auswertbar", "vermerk": "kein haftender Zustand im Raster", "werte": {}}
    u["QM4"] = u4
    return u


def bilder(H, ordner, zeilen, weitere):
    os.makedirs(ordner, exist_ok=True)
    # Bild 1: Bindung gegen beide Referenzen
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2), sharex=True)
    for V0 in H["V0"]:
        zz = [z for z in zeilen if z["V0"] == V0]
        Q = [z["Q"] for z in zz]
        ax[0].plot(Q, [z["bindung_frei_rel"] for z in zz], "o-", color=FARBEN.get(V0, "k"), label="V0 = %g" % V0)
        if V0 > 0:
            ax[1].plot(Q, [z["bindung_topf"] / z["E_frei"] for z in zz], "o-", color=FARBEN.get(V0, "k"),
                       label="V0 = %g" % V0)
            ax[1].plot(Q, [z["topf_allein"] / z["E_frei"] for z in zz], ":", color=FARBEN.get(V0, "k"), alpha=0.7)
    for name, G in weitere.items():
        for V0 in G["V0"]:
            zz = [z for z in tabelle(G) if z["V0"] == V0]
            ax[0].plot([z["Q"] for z in zz], [z["bindung_frei_rel"] for z in zz], "x", color=FARBEN.get(V0, "k"),
                       alpha=0.6, ms=6)
    ax[0].axhline(SCHWELLE_BINDUNG, color="#b91c1c", ls="--", lw=1)
    ax[0].axhline(0, color="k", lw=0.6)
    ax[1].axhline(0, color="k", lw=0.6)
    ax[0].set_xscale("log")
    ax[0].set_xlabel("Q")
    ax[1].set_xlabel("Q")
    ax[0].set_ylabel("(E_frei - E_mono) / E_frei")
    ax[1].set_ylabel("(E_topf - E_mono) / E_frei;  punktiert: (E_frei - E_topf) / E_frei")
    ax[0].set_title("Bindung am Monopol gegen freien Ball (gestrichelt: 1e-3)", fontsize=9)
    ax[1].set_title("gegen Ball am Topf ohne Monopol", fontsize=9)
    ax[0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "bild-bindung.png"), dpi=130)
    plt.close(fig)
    # Bild 2: Winkelform D(theta)/D(pi/2)
    t = None
    try:
        npz = np.load(os.path.join(ordner, "haupt.npz"))
        t = npz["gitter_t"]
    except Exception:
        npz = None
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
    for k, Q in enumerate((H["Q"][0], H["Q"][-1])):
        for V0 in H["V0"]:
            c = beste(H["faelle"], V0, Q)
            D = c["kennzahlen"].get("winkel_D_theta")
            if D is None or t is None:
                continue
            axs[k].semilogy(t, np.maximum(D, 1e-12), "-", color=FARBEN.get(V0, "k"),
                            label="V0 = %g (%s, %s)" % (V0, c["start"], c["status"][:11]))
        if t is not None:
            axs[k].semilogy(t, 1 + np.cos(t), "k--", lw=1, label="Mode 1 + cos(theta)")
        axs[k].set_xlabel("theta")
        axs[k].set_ylabel("D(theta)/D(pi/2),  D = int f^2 r^2 dr")
        axs[k].set_title("Winkelform bei Q = %d" % int(Q), fontsize=9)
        axs[k].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "bild-winkel.png"), dpi=130)
    plt.close(fig)
    # Bild 3: Profilschnitt (Meridianebene) f^2(rho, z)
    if npz is not None:
        r = npz["gitter_r"]
        Lr = npz["gitter_Lr"]
        rf = np.concatenate([[0.0], np.cumsum(Lr)])
        tf = np.linspace(0, np.pi, len(t) + 1)
        nq = len(H["Q"])
        vmax = max(H["V0"])
        faelle = [(vmax, H["Q"][min(1, nq - 1)]), (vmax, H["Q"][max(nq - 2, 0)]), (min(H["V0"]), H["Q"][min(1, nq - 1)])]
        fig, axs = plt.subplots(1, 3, figsize=(13, 4.6))
        for k, (V0, Q) in enumerate(faelle):
            c = beste(H["faelle"], V0, Q)
            key = "f_V%s_Q%s_%s" % (V0, int(Q), c["start"])
            if key not in npz:
                continue
            F2 = (npz[key] ** 2).reshape(len(r), len(t))
            RR, TT = np.meshgrid(rf, tf, indexing="ij")
            X = RR * np.sin(TT)
            Z = RR * np.cos(TT)
            for s in (1, -1):
                pc = axs[k].pcolormesh(s * X, Z, F2, shading="flat", cmap="viridis", vmin=0, vmax=max(F2.max(), 1e-9))
            axs[k].plot([0], [0], "r*", ms=9)
            axs[k].plot([0, 0], [0, -12], "r:", lw=1)
            lim = 2.5 * c["kennzahlen"]["z_c"] + 6 if c["kennzahlen"]["z_c"] > 0 else 10
            lim = min(max(lim, 8), 18)
            axs[k].set_xlim(-lim, lim)
            axs[k].set_ylim(-lim, lim)
            axs[k].set_aspect("equal")
            axs[k].set_title("f^2, V0 = %g, Q = %d (%s, %s)" % (V0, int(Q), c["start"], c["status"][:11]), fontsize=8)
            axs[k].set_xlabel("x")
            axs[k].set_ylabel("z")
            fig.colorbar(pc, ax=axs[k], shrink=0.8)
        fig.tight_layout()
        fig.savefig(os.path.join(ordner, "bild-profil.png"), dpi=130)
        plt.close(fig)


def main():
    ordner = sys.argv[1]
    ausgabe = sys.argv[2]
    H = lade(os.path.join(ordner, "haupt.json"))
    art = {a["Q"]: a for a in H.get("artefakt", [])}
    weitere = {}
    for p in sorted(glob.glob(os.path.join(ordner, "grob*.json")) + glob.glob(os.path.join(ordner, "fein*.json"))):
        weitere[os.path.basename(p)] = lade(p)
    zeilen = tabelle(H)
    erg = {"urteile": urteile(H, art), "tabelle_hauptgitter": zeilen, "artefakt": H.get("artefakt"),
           "qm0": H.get("qm0"), "gitter": {"h": H["h"], "Nt": H["Nt"], "n": H.get("n"), "Nr": H.get("Nr")},
           "skript_sha256": SKRIPT_SHA, "haupt_skript_sha256": H.get("skript_sha256")}
    konv = {}
    for name, G in weitere.items():
        konv[name] = {"h": G["h"], "Nt": G["Nt"], "tabelle": [
            {k: z[k] for k in ("V0", "Q", "E_frei", "E_mono", "bindung_frei", "bindung_frei_rel", "bindung_topf",
                               "status", "z_c", "winkel_D0_D90", "start")} for z in tabelle(G)]}
        if "qm0" in G:
            konv[name]["qm0"] = G["qm0"]
    erg["konvergenz"] = konv
    qm = {}
    for p in sorted(glob.glob(os.path.join(ordner, "qmax*.json"))):
        G = lade(p)
        qm[os.path.basename(p)] = G.get("qmax")
    erg["qmax_bisektion"] = qm
    bilder(H, ordner, zeilen, {k: v for k, v in weitere.items() if k.startswith("grob")})
    with open(ausgabe, "w") as fh:
        json.dump(erg, fh, indent=1)
    print(json.dumps({k: v["urteil"] for k, v in erg["urteile"].items()}))


if __name__ == "__main__":
    main()
