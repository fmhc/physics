"""KAUSAL-4D-SCHICHT-1: Auswertung nach PLAN.md (Urteilsregeln Abschnitt 7), Bilder, auswertung.json.

Aufruf (nur ueber kleintest.sh):
  schicht_auswertung.py <laufordner> <kontordner (pole.json, erwartung.json/.npz)> <ausgabeordner> <rho1,rho2> <n_saaten>
                        [kontinuum.npz von KAUSAL-WELLE-4D, nur Vergleich]
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
import schicht_feld as sf  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
NP = 9
VN = [v[0] for v in sf.VARIANTEN]
FARBE = {"VJ": "C0", "V0": "C2", "VM": "C3"}
RHO_U = 16.0          # Urteilsdichte (PLAN 7)
GAMMA_TOL = 1e-6


def ols(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    return float(np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2))


def lade_felder(lauf, rho):
    fs = sorted(glob.glob(os.path.join(lauf, f"feld-r{rho:g}-s*.npz")), key=lambda p: int(p.split("-s")[-1].split(".")[0]))
    d = {"saaten": [], "phi": [], "n": [], "L0N": [], "L1N": [], "N": [], "maxphi": [], "endlich": [], "zeit": []}
    for f in fs:
        s = int(f.split("-s")[-1].split(".")[0])
        kopf = json.load(open(f.replace(".npz", ".json")))
        z = np.load(f)
        d["endlich"].append(bool(kopf["endlich"]))
        if not kopf["endlich"]:
            continue
        d["saaten"].append(s)
        d["phi"].append(z["phi_p"])                                         # (NV, NC, 26)
        d["n"].append(z["summen"][..., 0].sum(axis=3) / (rho * kd.SCHEIBE_W))  # (NV, NC, 4)
        d["L0N"].append(kopf["L0_je_N"])
        d["L1N"].append(kopf["L1_je_N"])
        d["N"].append(kopf["N"])
        d["maxphi"].append([kopf["max_abs_phi"][v] for v in VN])
        d["zeit"].append(kopf["zeit_gesamt_s"])
    for k in ("phi", "n", "L0N", "L1N", "N", "maxphi", "zeit"):
        d[k] = np.array(d[k])
    return d


def main():
    lauf, kont, aus = sys.argv[1], sys.argv[2], sys.argv[3]
    rhos = [float(r) for r in sys.argv[4].split(",")]
    n_soll = int(sys.argv[5])
    os.makedirs(aus, exist_ok=True)
    PJ = json.load(open(os.path.join(kont, "pole.json")))
    KJ = json.load(open(os.path.join(kont, "erwartung.json")))
    K = np.load(os.path.join(kont, "erwartung.npz"))
    pp = K["pruefpunkte"]
    NPP = pp.shape[1]                     # 9 Pruefpunkte + 17 Profilpunkte = 26 je Konfiguration
    pa = K["achsenpunkte"]
    phi_k = K["phi_k"]
    ref = K["quad_kappe"]
    norm_c = K["norm_c"]
    E = {}
    for key in K.files:
        if key.startswith("E_"):
            E[key[2:]] = K[key]                                              # (2, NC, 54)
    gtest = KJ["kontrollen"]["gamma_gegenprobe_rel_max"]
    daten = {r: lade_felder(lauf, r) for r in rhos}
    vollst = {r: (len(daten[r]["saaten"]) >= n_soll and all(daten[r]["endlich"])) for r in rhos}
    urteile = {}
    besch = {"saaten_je_rho": {str(r): daten[r]["saaten"] for r in rhos}, "vollstaendig_je_rho": {str(r): vollst[r] for r in rhos}}
    # ---------- Pruefpunkt-Tests je Variante und Dichte ----------
    tests = {}
    srel = {}
    srel_e = {}
    for r in rhos:
        P = daten[r]["phi"][:, :, :, :NP]                                   # (n, NV, NC, 9)
        n = P.shape[0]
        for iv, v in enumerate(VN):
            Ev = E[f"{v}_rho{r:g}"][0]
            lst = []
            for c in range(kd.NC):
                for i in range(NP):
                    z = P[:, iv, c, i]
                    m = z.mean()
                    sd = np.sqrt(z.real.var(ddof=1) + z.imag.var(ddof=1))
                    se = sd / np.sqrt(n)
                    e = {"eta": kd.ETAS[c], "t": float(pp[c, i, 0]), "x": float(pp[c, i, 1]), "z": float(pp[c, i, 3]),
                         "mittel": [float(m.real), float(m.imag)], "erwartung": [float(Ev[c, i].real), float(Ev[c, i].imag)],
                         "kontinuum": [float(ref[c, i].real), float(ref[c, i].imag)],
                         "abw_erwartung_in_SE": float(abs(m - Ev[c, i]) / se),
                         "abw_kontinuum_in_SE": float(abs(m - ref[c, i]) / se),
                         "rel_streuung": float(sd / abs(ref[c, i])), "rel_streuung_gegen_E": float(sd / abs(Ev[c, i])),
                         "betrag_mittel_zu_kontinuum": float(abs(m) / abs(ref[c, i])),
                         "betrag_E_zu_kontinuum": float(abs(Ev[c, i]) / abs(ref[c, i]))}
                    lst.append(e)
                    srel[(r, v, c, i)] = sd / abs(ref[c, i])
                    srel_e[(r, v, c, i)] = sd / abs(Ev[c, i])
            tests[f"{v}_rho{r:g}"] = lst
    besch["pruefpunkte"] = tests

    def treffer(v, r):
        return int(sum(e["abw_erwartung_in_SE"] <= 3.0 for e in tests[f"{v}_rho{r:g}"]))

    def gm(v, r, quelle=srel):
        return float(np.exp(np.mean([np.log(quelle[(r, v, c, i)]) for c in range(kd.NC) for i in range(NP)])))

    # ---------- SH0 ----------
    ok_g = gtest.get(f"VJ_rho{RHO_U:g}", np.inf) <= GAMMA_TOL
    t0 = treffer("VJ", RHO_U)
    urteile["SH0"] = {"urteil": ("eingetroffen" if t0 >= 15 else "nicht eingetroffen") if (vollst[RHO_U] and ok_g)
                      else "nicht auswertbar",
                      "werte": {"rho": RHO_U, "treffer_von_18": t0,
                                "abw_in_SE": [e["abw_erwartung_in_SE"] for e in tests[f"VJ_rho{RHO_U:g}"]],
                                "treffer_je_rho": {str(r): treffer("VJ", r) for r in rhos},
                                "gamma_gegenprobe": gtest.get(f"VJ_rho{RHO_U:g}")}}
    # ---------- SH1 ----------
    ks = PJ["ks"]
    erg = PJ["ergebnisse"]

    def key(v, r, k):
        return f"{v}_rho{r:g}_k{k:.4f}"

    prho = [float(r) for r in PJ["rhos"]]
    s16 = erg[key("V0", 16.0, 0.0)]["schale"]
    s4 = erg[key("V0", 4.0, 0.0)]["schale"]
    stabil = all(erg[key(v, r, k)]["zaehlung_A"]["stabil"] and erg[key(v, r, k)]["zaehlung_S"]["stabil"]
                 for v in ("V0", "VM") for r in prho for k in ks)
    weitere = {key(v, r, k): erg[key(v, r, k)]["weitere_in_A"] for v in VN for r in prho for k in ks}
    ns = {key(v, r, k): erg[key(v, r, k)]["zaehlung_S"]["zahl"] for v in VN for r in prho for k in ks}
    na = {key(v, r, k): erg[key(v, r, k)]["zaehlung_A"]["zahl"] for v in VN for r in prho for k in ks}
    inkonsistent = any(weitere[key(v, r, k)] < 0 for v in ("V0", "VM") for r in prho for k in ks)
    if s16 is None or s4 is None or not stabil or inkonsistent:
        u1 = "nicht auswertbar"
        a_ok = b_ok = None
        im16 = im4 = None
        sch1 = None
    else:
        im16 = float(s16["omega_im"])
        im4 = float(s4["omega_im"])
        a_ok = bool(0.0 <= im16 <= 0.05)
        b_ok = bool(im4 >= 3.0 * im16)
        sch1 = None
    c_ok = all(ns[key("VM", r, k)] == 0 for r in prho for k in ks)
    d_ok = all(weitere[key(v, r, k)] == 0 for v in ("V0", "VM") for r in prho for k in ks)
    if s16 is not None and s4 is not None and stabil and not inkonsistent:
        u1 = "eingetroffen" if (a_ok and b_ok and c_ok and d_ok) else "nicht eingetroffen"
        sch1 = bool(im16 > 0.075 or (not c_ok) or (not d_ok))
    v1 = None
    if u1 == "nicht eingetroffen" and sch1 is False:
        v1 = "Graubereich bzw. Teilvorhersage verfehlt; Scheiterregel nicht ausgeloest"
    pol_tab = {}
    for v in VN:
        for r in prho:
            for k in ks:
                e = erg[key(v, r, k)]
                pol_tab[key(v, r, k)] = {"schale": e["schale"], "blatt2": e["blatt2"], "N_A": e["zaehlung_A"]["zahl"],
                                         "N_S": e["zaehlung_S"]["zahl"], "weitere_in_A": e["weitere_in_A"],
                                         "nullstellen_A": e["nullstellen_A"], "nullstellen_S": e["nullstellen_S"],
                                         "stabil_A": e["zaehlung_A"]["stabil"], "stabil_S": e["zaehlung_S"]["stabil"],
                                         "lokalisiert_gleich_gezaehlt": [e["lokalisiert_gleich_gezaehlt_A"],
                                                                         e["lokalisiert_gleich_gezaehlt_S"]]}
    urteile["SH1"] = {"urteil": u1, "werte": {"im_omega_V0_rho16_k0": im16, "im_omega_V0_rho4_k0": im4,
                                              "a_im16_in_0_bis_0_05": a_ok, "b_faellt_um_faktor_3": b_ok,
                                              "faktor_4_zu_16": (im4 / im16) if (im16 not in (None, 0.0) and im4 is not None) else None,
                                              "c_VM_kein_pol_nahe_schale": c_ok, "d_keine_weiteren": d_ok,
                                              "zaehlungen_stabil": stabil, "scheiterregel_ausgeloest": sch1,
                                              "N_S": ns, "N_A": na, "weitere": weitere}}
    if v1:
        urteile["SH1"]["vermerk"] = v1
    besch["pole"] = pol_tab
    # ---------- SH2 ----------
    zuw = {}
    zuw_saat = {}
    for v in VN:
        for r in [x for x in prho]:
            Ev = E[f"{v}_rho{r:g}"][0]
            for c in range(kd.NC):
                for lage, (i0, i1) in {"A": (0, 6), "B": (1, 7), "C": (2, 8)}.items():
                    q = (abs(Ev[c, i1]) / abs(ref[c, i1])) / (abs(Ev[c, i0]) / abs(ref[c, i0]))
                    zuw[f"{v}_rho{r:g}_eta{kd.ETAS[c]:g}_{lage}"] = float(q)
        for r in rhos:
            P = daten[r]["phi"][:, VN.index(v)]
            m = P.mean(axis=0)
            for c in range(kd.NC):
                q = (abs(m[c, 6]) / abs(ref[c, 6])) / (abs(m[c, 0]) / abs(ref[c, 0]))
                zuw_saat[f"{v}_rho{r:g}_eta{kd.ETAS[c]:g}_A"] = float(q)
    Z_V0 = max(zuw[f"V0_rho16_eta{e:g}_A"] for e in kd.ETAS)
    Z_VM = max(zuw[f"VM_rho16_eta{e:g}_A"] for e in kd.ETAS)
    Z_VJ = max(zuw[f"VJ_rho16_eta{e:g}_A"] for e in kd.ETAS)
    t2 = treffer("V0", RHO_U)
    ok_g2 = all(gtest.get(f"{v}_rho{RHO_U:g}", np.inf) <= GAMMA_TOL for v in ("V0", "VM"))
    if vollst[RHO_U] and ok_g2:
        u2 = "eingetroffen" if (t2 >= 15 and Z_V0 <= 1.10 and Z_VM < 1.0) else "nicht eingetroffen"
    else:
        u2 = "nicht auswertbar"
    sch2 = bool(Z_V0 > 1.15)
    urteile["SH2"] = {"urteil": u2, "werte": {"rho": RHO_U, "a_V0_treffer_von_18": t2, "zuwachs_V0_max": Z_V0,
                                              "zuwachs_VM_max": Z_VM, "zuwachs_VJ_max": Z_VJ,
                                              "b_zuwachs_V0_hoechstens_1_10": bool(Z_V0 <= 1.10),
                                              "c_zuwachs_VM_unter_1": bool(Z_VM < 1.0),
                                              "scheiterregel_ausgeloest": sch2,
                                              "abw_V0_in_SE": [e["abw_erwartung_in_SE"] for e in tests[f"V0_rho{RHO_U:g}"]],
                                              "treffer_je_variante_und_rho": {f"{v}_rho{r:g}": treffer(v, r) for v in VN for r in rhos},
                                              "gamma_gegenprobe": {v: gtest.get(f"{v}_rho{RHO_U:g}") for v in VN}}}
    if u2 == "nicht eingetroffen" and not sch2:
        urteile["SH2"]["vermerk"] = "Teilvorhersage verfehlt; Scheiterregel nicht ausgeloest"
    besch["zuwachs_erwartung"] = zuw
    besch["zuwachs_saatmittel"] = zuw_saat
    # ---------- SH3 ----------
    s = {f"{v}_rho{r:g}": gm(v, r) for v in VN for r in rhos}
    s_e = {f"{v}_rho{r:g}": gm(v, r, srel_e) for v in VN for r in rhos}
    sV0 = s["V0_rho16"]
    sVJ = s["VJ_rho16"]
    u3 = ("eingetroffen" if (sV0 > sVJ and 0.5 <= sV0 <= 1.0) else "nicht eingetroffen") if vollst[RHO_U] else "nicht auswertbar"
    urteile["SH3"] = {"urteil": u3, "werte": {"rho": RHO_U, "s_V0": sV0, "s_VJ": sVJ, "s_VM": s["VM_rho16"],
                                              "verhaeltnis_V0_zu_VJ": sV0 / sVJ, "s_je_variante_und_rho": s,
                                              "s_gegen_eigene_erwartung": s_e,
                                              "steigung_8_16": {v: (np.log(s[f"{v}_rho16"]) - np.log(s[f"{v}_rho8"])) / np.log(2.0)
                                                                for v in VN} if 8.0 in rhos else None,
                                              "rel_streuung_je_punkt_rho16": {v: [float(srel[(16.0, v, c, i)])
                                                                                  for c in range(kd.NC) for i in range(NP)] for v in VN}}}
    if sV0 < 0.33:
        urteile["SH3"]["vermerk"] = "Kartenwortlaut: unter 0,33, kein Preis"
    elif sV0 > 1.5:
        urteile["SH3"]["vermerk"] = "Kartenwortlaut: ueber 1,5, unbrauchbar"
    # ---------- beschreibend: Norm, Linkzahlen, max phi ----------
    norm = []
    for r in rhos:
        nn = daten[r]["n"]                                                   # (n, NV, NC, 4)
        for iv, v in enumerate(VN):
            for c in range(kd.NC):
                R = nn[:, iv, c, :].mean(axis=0) / norm_c[c]
                Gs = (nn[:, iv, c, -1] / norm_c[c, -1]) / (nn[:, iv, c, 0] / norm_c[c, 0])
                norm.append({"variante": v, "rho": r, "eta": kd.ETAS[c], "R": R.tolist(), "G": float(R[-1] / R[0]),
                             "G_saat_median": float(np.median(Gs)), "G_saat_max": float(Gs.max()), "G_saat_min": float(Gs.min())})
    besch["norm"] = norm
    lz = {}
    for r in rhos:
        for nm, kk in (("L0N", "linkzahl_L0_je_N"), ("L1N", "linkzahl_L1_je_N")):
            x = daten[r][nm]
            m = float(x.mean())
            se = float(x.std(ddof=1) / np.sqrt(x.size))
            ew = KJ[kk].get(str(r))
            lz[f"{nm}_rho{r:g}"] = {"mittel": m, "SE": se, "erwartung": ew,
                                     "abw_in_SE": (m - ew) / se if ew is not None else None}
    besch["linkzahlen"] = lz
    besch["max_abs_phi"] = {f"{v}_rho{r:g}": float(daten[r]["maxphi"][:, iv].max()) for iv, v in enumerate(VN) for r in rhos}
    besch["zeit_je_saat"] = {str(r): [float(daten[r]["zeit"].min()), float(daten[r]["zeit"].max())] for r in rhos}
    besch["kontrollen_teil_A"] = {"erwartung": KJ["kontrollen"], "probe_windung": PJ["probe_windung"],
                                  "blattprobe": PJ["blattprobe"], "gammas": KJ["gammas"]}
    if len(sys.argv) > 6:                                                   # Vergleich mit KAUSAL-WELLE-4D
        A = np.load(sys.argv[6])
        jr = [float(x) for x in A["johnston_rhos"]]
        vgl = {"quad_kappe_rel_max": float(np.max(np.abs(ref - A["quad_kappe"]) / np.abs(A["quad_kappe"]))),
               "norm_c_rel_max": float(np.max(np.abs(norm_c - A["norm_c"]) / np.abs(A["norm_c"]))),
               "phi_k_rel_max": float(np.max(np.abs(phi_k[:, :NPP] - A["phi_k"]) / np.abs(A["phi_k"])))}
        for r in prho:
            if r in jr:
                alt = A["johnston"][jr.index(r), 0]
                vgl[f"E_VJ_rho{r:g}_rel_max"] = float(np.max(np.abs(E[f"VJ_rho{r:g}"][0, :, :NPP] - alt) / np.abs(alt)))
        besch["vergleich_kausal_welle_4d"] = vgl
    # ---------- Bilder ----------
    # 1) Pole
    fig, ax = plt.subplots(1, 3, figsize=(17, 5))
    mark = {4.0: "o", 8.0: "s", 16.0: "^"}
    xr, yr = 3.0, 1.0
    for ik, k in enumerate(ks):
        a = ax[ik]
        for v in VN:
            for r in prho:
                e = erg[key(v, r, k)]
                zA = np.array(e["nullstellen_A"]) if e["nullstellen_A"] else np.zeros((0, 2))
                zS = np.array(e["nullstellen_S"]) if e["nullstellen_S"] else np.zeros((0, 2))
                Z = np.concatenate([zA, zS]) if zA.size or zS.size else np.zeros((0, 2))
                if Z.size:
                    a.plot(Z[:, 0], Z[:, 1], mark[r], color=FARBE[v], ms=7, alpha=0.8)
                    xr = max(xr, float(np.abs(Z[:, 0]).max()) + 0.5)
                    yr = max(yr, float(Z[:, 1].max()) + 0.3)
                b2 = e["blatt2"]
                if b2["gueltig"]:
                    a.plot([b2["omega_re"]], [b2["omega_im"]], mark[r], mfc="none", color=FARBE[v], ms=8)
        a.axhline(0.0, color="k", lw=0.6)
        a.axhline(0.05, color="grey", lw=0.6, ls=":")
        a.set_title(f"Nullstellen von 1 + m^2 k~_gen, k = {k:.3f} (voll: Blatt I, offen: Blatt II)", fontsize=9)
        a.set_xlabel("Re omega")
        a.set_ylabel("Im omega")
    for ik in range(2):
        ax[ik].set_xlim(-xr, xr)
        ax[ik].set_ylim(-0.4, yr)
    for v in VN:
        ax[0].plot([], [], "o", color=FARBE[v], label=v)
    for r in prho:
        ax[0].plot([], [], mark[r], color="k", label=f"rho = {r:g}")
    ax[0].legend(fontsize=7)
    a = ax[2]
    rr = np.linspace(3.5, 17, 100)
    for v in VN:
        y = []
        for r in prho:
            sh = erg[key(v, r, 0.0)]["schale"]
            y.append(sh["omega_im"] if sh else np.nan)
        a.plot(prho, y, "o-", color=FARBE[v], label=f"{v}: Schalennullstelle (k = 0)")
    eps = np.sqrt(6) / (2 * np.pi * np.sqrt(rr))
    M2 = 1.0 / (1.0 - eps)
    a.plot(rr, np.sqrt(6) / 4 / np.sqrt(rr) / np.sqrt(M2), ":", color=FARBE["VJ"], label="V-J erste Ordnung")
    a.plot(rr, 3 * M2 ** 3 / (16 * rr * np.sqrt(M2)), ":", color=FARBE["V0"], label="V-0: 3 M^6/(16 rho omega)")
    a.plot(rr, -np.sqrt(6) / 4 / np.sqrt(rr), ":", color=FARBE["VM"], label="V-M erste Ordnung")
    a.axhline(0.0, color="k", lw=0.6)
    a.axhspan(0.0, 0.05, color="C2", alpha=0.1, label="SH1 (a): [0; 0,05]")
    a.set_xlabel("rho")
    a.set_ylabel("Im omega der Schalennullstelle")
    a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "pole.png"), dpi=110)
    plt.close(fig)
    # 2) Saatmittel gegen Erwartung und Kontinuum je Variante (Profil t = 3,2, rho = 16)
    rmax = max(rhos)
    fig, ax = plt.subplots(3, 2, figsize=(13, 12))
    for iv, v in enumerate(VN):
        for c in range(kd.NC):
            a = ax[iv, c]
            z = pp[c, NP:NPP, 3]
            P = daten[rmax]["phi"][:, iv, c, NP:NPP]
            m = P.mean(axis=0)
            se_r = P.real.std(axis=0, ddof=1) / np.sqrt(P.shape[0])
            se_i = P.imag.std(axis=0, ddof=1) / np.sqrt(P.shape[0])
            Ev = E[f"{v}_rho{rmax:g}"][0, c, NP:NPP]
            a.errorbar(z, m.real, yerr=se_r, fmt="o", ms=3, color="C0", label="Re, Saatmittel +- SE")
            a.errorbar(z, m.imag, yerr=se_i, fmt="s", ms=3, color="C1", label="Im, Saatmittel +- SE")
            a.plot(z, phi_k[c, NP:NPP].real, "-", color="C0", lw=1, label="Re, Kontinuum")
            a.plot(z, phi_k[c, NP:NPP].imag, "-", color="C1", lw=1, label="Im, Kontinuum")
            a.plot(z, Ev.real, ":", color="C0", lw=1.4, label=f"Re, Erwartung {v} [M]")
            a.plot(z, Ev.imag, ":", color="C1", lw=1.4, label=f"Im, Erwartung {v} [M]")
            a.set_title(f"{v}, eta = {kd.ETAS[c]:g}, t = 3,2, x = y = 0, rho = {rmax:g}, {P.shape[0]} Saaten", fontsize=9)
            a.set_xlabel("z")
            a.legend(fontsize=6)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "saatmittel_erwartung_kontinuum.png"), dpi=100)
    plt.close(fig)
    # 3) Zuwachs gegen t
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    a = ax[0]
    ta = pa[0, :, 0]
    for v in VN:
        for r, ls in ((16.0, "-"), (8.0, "--"), (4.0, ":")):
            if f"{v}_rho{r:g}" not in E:
                continue
            Ev = E[f"{v}_rho{r:g}"][0, 0, NPP:]
            a.plot(ta, np.abs(Ev) / np.abs(phi_k[0, NPP:]), ls, color=FARBE[v], lw=1.2,
                   label=f"{v}, rho = {r:g} (Erwartung)")
        P = daten[rmax]["phi"][:, VN.index(v), 0, :NP]
        m = P.mean(axis=0)
        sd = np.sqrt(P.real.var(axis=0, ddof=1) + P.imag.var(axis=0, ddof=1)) / np.sqrt(P.shape[0])
        idx = [0, 3, 6]
        a.errorbar(pp[0, idx, 0], np.abs(m[idx]) / np.abs(ref[0, idx]), yerr=sd[idx] / np.abs(ref[0, idx]), fmt="o",
                   color=FARBE[v], ms=5)
    a.axhline(1.0, color="k", lw=0.6)
    a.set_yscale("log")
    a.set_xlabel("t (Paketmitte, eta = 0)")
    a.set_ylabel("abs(phi)/abs(Kontinuum)")
    a.set_title("Erwartung (Linien) und Saatmittel rho = 16 (Punkte +- SE)", fontsize=9)
    a.legend(fontsize=6)
    a = ax[1]
    tm = kd.SCHEIBE_T0 + kd.SCHEIBE_W * (np.arange(kd.N_SCHEIBEN) + 0.5)
    for v in VN:
        for r, ls in ((16.0, "-"), (8.0, "--")):
            if r not in rhos:
                continue
            nn = daten[r]["n"][:, VN.index(v), 0, :]
            a.plot(tm, nn.mean(axis=0) / norm_c[0], "o" + ls, color=FARBE[v], label=f"{v}, rho = {r:g}")
    a.axhline(1.0, color="k", lw=0.6)
    a.set_yscale("log")
    a.set_xlabel("t (Scheibenmitte)")
    a.set_ylabel("Saatmittel n_k / n_c,k (eta = 0)")
    a.set_title("Norm je Zeitscheibe gegen Kontinuum", fontsize=9)
    a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "zuwachs_t.png"), dpi=110)
    plt.close(fig)
    # 4) Streuung je Variante
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    for iv, v in enumerate(VN):
        for j, r in enumerate(rhos):
            y = [srel[(r, v, c, i)] for c in range(kd.NC) for i in range(NP)]
            x = np.full(len(y), iv * 3 + j) + np.linspace(-0.25, 0.25, len(y))
            a = ax
            a.plot(x, y, ".", color=FARBE[v], alpha=0.6)
            a.plot([iv * 3 + j - 0.35, iv * 3 + j + 0.35], [s[f"{v}_rho{r:g}"]] * 2, "-", color="k", lw=2)
    ax.set_xticks([iv * 3 + j for iv in range(len(VN)) for j in range(len(rhos))])
    ax.set_xticklabels([f"{v}\nrho={r:g}" for v in VN for r in rhos], fontsize=8)
    ax.axhspan(0.5, 1.0, color="C2", alpha=0.1, label="SH3-Prognose 0,5 bis 1,0")
    ax.axhline(0.33, color="grey", ls=":", label="0,33 (kein Preis)")
    ax.axhline(1.5, color="r", ls=":", label="1,5 (unbrauchbar)")
    ax.set_yscale("log")
    ax.set_ylabel("relative Streuung sd/abs(Kontinuum) je Pruefpunkt (Strich: geom. Mittel)")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "streuung_varianten.png"), dpi=110)
    plt.close(fig)
    out = {"urteile": urteile, "beschreibend": besch, "rhos": rhos, "n_saaten_soll": n_soll, "skript_sha256": SKRIPT_SHA,
           "schicht_feld_sha256": sf.SKRIPT_SHA, "pole_json_sha256": hashlib.sha256(open(os.path.join(kont, "pole.json"), "rb").read()).hexdigest(),
           "erwartung_json_sha256": hashlib.sha256(open(os.path.join(kont, "erwartung.json"), "rb").read()).hexdigest(),
           "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(aus, "auswertung.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps({k: urteile[k]["urteil"] for k in urteile}))


if __name__ == "__main__":
    main()
