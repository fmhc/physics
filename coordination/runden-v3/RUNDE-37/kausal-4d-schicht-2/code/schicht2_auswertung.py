"""KAUSAL-4D-SCHICHT-2: Auswertung nach PLAN.md (Urteilsregeln Abschnitt 7), Bilder, auswertung.json.

Aufruf (nur ueber kleintest.sh):
  schicht2_auswertung.py <laufordner (Felder rho = 16)> <kontordner (erwartung.json/.npz)> <pole1.json,pole2.json>
                         <ausgabeordner> <n_saaten> <schicht1_laufordner> <schicht1_pole.json>
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
import schicht2_feld as sf  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
NP = 9
VN = [v[0] for v in sf.VARIANTEN]
FARBE = {"VJ": "C0", "V0": "C2", "V00": "C4"}
RHO_U = 16.0
GAMMA_TOL = 1e-6
KARTE_S20 = 0.0147      # Kartenwert S2-0
TOL_S20 = 1e-3
SCHWELLE_S21 = 0.004    # Kartenwert S2-1
M = kd.MASSE


def eps(rho):
    return np.sqrt(6.0) / (2 * np.pi * np.sqrt(rho))


def schreibtisch(v, rho, k):
    """Erste nichtverschwindende Ordnung (PLAN Abschnitt 2), omega = sqrt(k^2 + M^2)."""
    e = eps(rho)
    if v == "VJ":
        om = np.sqrt(k * k + M * M)
        return (np.sqrt(6.0) / 4) * M ** 4 / (om * np.sqrt(rho))
    if v == "V0":
        M2 = M * M / (1 - e * M * M)
        return 3 * M2 ** 3 / (16 * rho * np.sqrt(k * k + M2))
    M2 = M * M / (1 - e * M * M / 2)
    return e * M2 ** 4 / (16 * rho * np.sqrt(k * k + M2))


def lade_felder(lauf, rho):
    fs = sorted(glob.glob(os.path.join(lauf, f"feld-r{rho:g}-s*.npz")), key=lambda p: int(p.split("-s")[-1].split(".")[0]))
    d = {"saaten": [], "phi": [], "n": [], "L0N": [], "L1N": [], "L2N": [], "N": [], "maxphi": [], "endlich": [],
         "zeit": [], "summen": []}
    for f in fs:
        s = int(f.split("-s")[-1].split(".")[0])
        kopf = json.load(open(f.replace(".npz", ".json")))
        z = np.load(f)
        d["endlich"].append(bool(kopf["endlich"]))
        if not kopf["endlich"]:
            continue
        d["saaten"].append(s)
        d["phi"].append(z["phi_p"])                                         # (NV, NC, 26)
        d["summen"].append(z["summen"])
        d["n"].append(z["summen"][..., 0].sum(axis=3) / (rho * kd.SCHEIBE_W))  # (NV, NC, 4)
        d["L0N"].append(kopf["L0_je_N"])
        d["L1N"].append(kopf["L1_je_N"])
        d["L2N"].append(kopf["L2_je_N"])
        d["N"].append(kopf["N"])
        d["maxphi"].append([kopf["max_abs_phi"][v] for v in VN])
        d["zeit"].append(kopf["zeit_gesamt_s"])
    for k in ("phi", "n", "L0N", "L1N", "L2N", "N", "maxphi", "zeit"):
        d[k] = np.array(d[k])
    return d


def main():
    lauf, kont, pole_dat, aus = sys.argv[1], sys.argv[2], sys.argv[3].split(","), sys.argv[4]
    n_soll = int(sys.argv[5])
    s1_lauf, s1_pole = sys.argv[6], sys.argv[7]
    os.makedirs(aus, exist_ok=True)
    erg = {}
    for pdat in pole_dat:
        erg.update(json.load(open(pdat))["ergebnisse"])
    PJ0 = json.load(open(pole_dat[0]))
    ks = PJ0["ks"]
    prho = [float(r) for r in PJ0["rhos"]]
    KJ = json.load(open(os.path.join(kont, "erwartung.json")))
    K = np.load(os.path.join(kont, "erwartung.npz"))
    S1P = json.load(open(s1_pole))
    pp = K["pruefpunkte"]
    NPP = pp.shape[1]
    pa = K["achsenpunkte"]
    phi_k = K["phi_k"]
    ref = K["quad_kappe"]
    norm_c = K["norm_c"]
    E = {key[2:]: K[key] for key in K.files if key.startswith("E_")}
    gtest = KJ["kontrollen"]["gamma_gegenprobe_rel_max"]
    rho = RHO_U
    daten = lade_felder(lauf, rho)
    vollst = bool(len(daten["saaten"]) >= n_soll and all(daten["endlich"]))
    urteile = {}
    besch = {"saaten": daten["saaten"], "vollstaendig": vollst}

    def key(v, r, k):
        return f"{v}_rho{r:g}_k{k:.4f}"

    def sch(v, r, k):
        return erg[key(v, r, k)]["schale"]

    # ---------- S2-0 ----------
    e0 = erg[key("V0", 16.0, 0.0)]
    s0 = e0["schale"]
    s1ref = S1P["ergebnisse"][key("V0", 16.0, 0.0)]["schale"]
    if s0 is None or not s0["konsistent"] or not e0["zaehlung_S"]["stabil"]:
        urteile["S2-0"] = {"urteil": "nicht auswertbar", "werte": {"schale": s0}}
    else:
        im = float(s0["omega_im"])
        abw = abs(im - KARTE_S20)
        urteile["S2-0"] = {"urteil": "eingetroffen" if abw <= TOL_S20 else "nicht eingetroffen",
                           "werte": {"im_omega_V0_rho16_k0": im, "re_omega_V0_rho16_k0": float(s0["omega_re"]),
                                     "karte": KARTE_S20, "abw_zur_karte": abw, "toleranz": TOL_S20,
                                     "schicht1_im": s1ref["omega_im"], "schicht1_re": s1ref["omega_re"],
                                     "abw_zu_schicht1_abs": abs(complex(s0["omega_re"], im)
                                                                - complex(s1ref["omega_re"], s1ref["omega_im"])),
                                     "abw_zu_schicht1_rel_im": abs(im - s1ref["omega_im"]) / abs(s1ref["omega_im"]),
                                     "regel_schicht1_gleich": e0["schale_regel_schicht1"]}}
    # ---------- S2-1 ----------
    e16 = erg[key("V00", 16.0, 0.0)]
    e4 = erg[key("V00", 4.0, 0.0)]
    f16 = erg[key("V0", 16.0, 0.0)]
    f4 = erg[key("V0", 4.0, 0.0)]
    stabil1 = all(e[z]["stabil"] for e in (e16, e4) for z in ("zaehlung_A", "zaehlung_S", "zaehlung_S0")) and \
        all(f["zaehlung_S"]["stabil"] for f in (f16, f4))
    lokal1 = all(e["lokalisiert_gleich_gezaehlt_S"] and e["lokalisiert_gleich_gezaehlt_S0"] for e in (e16, e4))
    sch_ok = all(e["schale"] is not None and e["schale"]["konsistent"] for e in (e16, e4, f16, f4))
    w1 = {"zaehlungen_stabil": stabil1, "lokalisiert_gleich_gezaehlt": lokal1, "schalen_bestimmt_und_konsistent": sch_ok}
    u1, v1 = None, None
    if not (stabil1 and lokal1 and sch_ok):
        u1 = "nicht auswertbar"
    else:
        im16 = float(e16["schale"]["omega_im"])
        im4 = float(e4["schale"]["omega_im"])
        j16 = float(f16["schale"]["omega_im"])
        j4 = float(f4["schale"]["omega_im"])
        naehe = [z[1] for z in e16["nullstellen_S"]] + [z[1] for z in e16["nullstellen_S0"]]
        a_ok = bool(im16 < SCHWELLE_S21 and all(y < SCHWELLE_S21 for y in naehe))
        w1.update({"im_V00_rho16_k0": im16, "blatt_V00_rho16_k0": e16["schale"]["blatt"],
                   "im_V00_rho4_k0": im4, "blatt_V00_rho4_k0": e4["schale"]["blatt"],
                   "im_V0_rho16_k0": j16, "im_V0_rho4_k0": j4,
                   "im_nullstellen_S_und_S0_V00_rho16_k0": naehe, "a_unter_0_004": a_ok})
        if j4 <= 0 or j16 <= 0:
            u1 = "nicht auswertbar"
            v1 = "V-0 nicht auf Blatt I, Bezugsfaktor nicht bestimmbar"
        elif im4 <= 0:
            u1 = "nicht auswertbar"
            v1 = "V-00 zerfaellt schon bei rho = 4; 'faellt schneller' nicht anwendbar (PLAN 7.2)"
        else:
            F0 = j4 / j16
            if im16 > 0:
                F00 = im4 / im16
                b_ok = bool(F00 > F0)
            else:
                F00 = None
                b_ok = True
                v1 = "Vorzeichenwechsel zwischen rho = 4 und 16 (Blatt II bei rho = 16), zaehlt als schnellerer Abfall"
            w1.update({"faktor_V0_4_zu_16": F0, "faktor_V00_4_zu_16": F00, "b_faellt_schneller": b_ok})
            u1 = "eingetroffen" if (a_ok and b_ok) else "nicht eingetroffen"
    urteile["S2-1"] = {"urteil": u1, "werte": w1}
    if v1:
        urteile["S2-1"]["vermerk"] = v1
    # ---------- S2-3 ----------
    st3 = all(erg[key("V00", r, k)]["zaehlung_A"]["stabil"] for r in prho for k in ks)
    weit = {key("V00", r, k): erg[key("V00", r, k)]["weitere_in_A"] for r in prho for k in ks}
    lok3 = {key("V00", r, k): erg[key("V00", r, k)]["lokalisiert_gleich_gezaehlt_A"] for r in prho for k in ks}
    gross = {key("V00", r, k): erg[key("V00", r, k)]["max_abs_m2k_bogen"] for r in prho for k in ks}
    if not st3 or any(x < 0 for x in weit.values()):
        u3 = "nicht auswertbar"
    else:
        u3 = "eingetroffen" if all(x == 0 for x in weit.values()) else "nicht eingetroffen"
    urteile["S2-3"] = {"urteil": u3, "werte": {"weitere_in_A": weit, "zaehlungen_A_stabil": st3,
                                               "lokalisiert_gleich_gezaehlt_A": lok3,
                                               "nullstellen_A": {key("V00", r, k): erg[key("V00", r, k)]["nullstellen_A"]
                                                                 for r in prho for k in ks},
                                               "max_abs_m2k_bogen": gross}}
    # ---------- Pruefpunkte und Streuung (Teil B) ----------
    P = daten["phi"][:, :, :, :NP] if vollst or len(daten["saaten"]) > 1 else None
    tests, srel, srel_e = {}, {}, {}
    n = P.shape[0]
    for iv, v in enumerate(VN):
        Ev = E[f"{v}_rho{rho:g}"][0]
        lst = []
        for c in range(kd.NC):
            for i in range(NP):
                z = P[:, iv, c, i]
                m = z.mean()
                sd = np.sqrt(z.real.var(ddof=1) + z.imag.var(ddof=1))
                se = sd / np.sqrt(n)
                lst.append({"eta": kd.ETAS[c], "t": float(pp[c, i, 0]), "x": float(pp[c, i, 1]), "z": float(pp[c, i, 3]),
                            "mittel": [float(m.real), float(m.imag)], "erwartung": [float(Ev[c, i].real), float(Ev[c, i].imag)],
                            "kontinuum": [float(ref[c, i].real), float(ref[c, i].imag)],
                            "abw_erwartung_in_SE": float(abs(m - Ev[c, i]) / se),
                            "abw_kontinuum_in_SE": float(abs(m - ref[c, i]) / se),
                            "rel_streuung": float(sd / abs(ref[c, i])), "rel_streuung_gegen_E": float(sd / abs(Ev[c, i])),
                            "betrag_mittel_zu_kontinuum": float(abs(m) / abs(ref[c, i])),
                            "betrag_E_zu_kontinuum": float(abs(Ev[c, i]) / abs(ref[c, i]))})
                srel[(v, c, i)] = sd / abs(ref[c, i])
                srel_e[(v, c, i)] = sd / abs(Ev[c, i])
        tests[v] = lst
    besch["pruefpunkte_rho16"] = tests

    def gm(v, quelle=srel):
        return float(np.exp(np.mean([np.log(quelle[(v, c, i)]) for c in range(kd.NC) for i in range(NP)])))

    s = {v: gm(v) for v in VN}
    s_e = {v: gm(v, srel_e) for v in VN}
    fin = all(np.isfinite(x) for x in s.values())
    u2 = ("eingetroffen" if s["V00"] > s["V0"] else "nicht eingetroffen") if (vollst and fin) else "nicht auswertbar"
    urteile["S2-2"] = {"urteil": u2, "werte": {"rho": rho, "n_saaten": n, "s_VJ": s["VJ"], "s_V0": s["V0"], "s_V00": s["V00"],
                                               "karte_s_V0": 0.636, "verhaeltnis_V00_zu_V0": s["V00"] / s["V0"],
                                               "verhaeltnis_V0_zu_VJ": s["V0"] / s["VJ"],
                                               "s_gegen_eigene_erwartung": s_e,
                                               "rel_streuung_je_punkt": {v: [float(srel[(v, c, i)]) for c in range(kd.NC)
                                                                             for i in range(NP)] for v in VN}}}
    urteile = {k: urteile[k] for k in ("S2-0", "S2-1", "S2-2", "S2-3")}
    besch["treffer_in_3SE_eigene_erwartung"] = {v: int(sum(e["abw_erwartung_in_SE"] <= 3.0 for e in tests[v])) for v in VN}
    besch["treffer_in_3SE_kontinuum"] = {v: int(sum(e["abw_kontinuum_in_SE"] <= 3.0 for e in tests[v])) for v in VN}
    besch["max_abw_in_SE"] = {v: float(max(e["abw_erwartung_in_SE"] for e in tests[v])) for v in VN}
    besch["betrag_E_zu_K_spanne"] = {v: [float(min(e["betrag_E_zu_kontinuum"] for e in tests[v])),
                                         float(max(e["betrag_E_zu_kontinuum"] for e in tests[v]))] for v in VN}
    besch["betrag_mittel_zu_K_spanne"] = {v: [float(min(e["betrag_mittel_zu_kontinuum"] for e in tests[v])),
                                              float(max(e["betrag_mittel_zu_kontinuum"] for e in tests[v]))] for v in VN}
    besch["gamma_gegenprobe"] = gtest
    # ---------- Pole beschreibend ----------
    pol_tab = {}
    for v in VN:
        for r in prho:
            for k in ks:
                e = erg[key(v, r, k)]
                sh = e["schale"]
                pol_tab[key(v, r, k)] = {"schale": sh, "regel_schicht1": e["schale_regel_schicht1"], "blatt2": e["blatt2"],
                                         "N_A": e["zaehlung_A"]["zahl"], "N_S": e["zaehlung_S"]["zahl"],
                                         "N_S0": e["zaehlung_S0"]["zahl"], "weitere_in_A": e["weitere_in_A"],
                                         "stabil": [e["zaehlung_A"]["stabil"], e["zaehlung_S"]["stabil"], e["zaehlung_S0"]["stabil"]],
                                         "lokalisiert_gleich_gezaehlt": [e["lokalisiert_gleich_gezaehlt_A"],
                                                                         e["lokalisiert_gleich_gezaehlt_S"],
                                                                         e["lokalisiert_gleich_gezaehlt_S0"]],
                                         "nullstellen_A": e["nullstellen_A"], "nullstellen_S": e["nullstellen_S"],
                                         "nullstellen_S0": e["nullstellen_S0"],
                                         "schreibtisch_im": float(schreibtisch(v, r, k)),
                                         "verhaeltnis_numerik_zu_schreibtisch": (sh["omega_im"] / float(schreibtisch(v, r, k))) if sh else None,
                                         "quadratur_schale": e["quadratur_schale"], "max_abs_m2k_bogen": e["max_abs_m2k_bogen"]}
    besch["pole"] = pol_tab
    fall = {}
    for v in VN:
        for k in ks:
            y = {r: (sch(v, r, k)["omega_im"] if sch(v, r, k) else None) for r in prho}
            if all(y[r] is not None and y[r] > 0 for r in (4.0, 8.0, 16.0)):
                fall[f"{v}_k{k:.4f}"] = {"4_zu_16": y[4.0] / y[16.0], "4_zu_8": y[4.0] / y[8.0], "8_zu_16": y[8.0] / y[16.0],
                                         "steigung_log_8_16": float(np.log(y[16.0] / y[8.0]) / np.log(2.0)),
                                         "steigung_log_4_8": float(np.log(y[8.0] / y[4.0]) / np.log(2.0))}
    besch["abfall_mit_rho"] = fall
    besch["proben_teil_A"] = {"probe_windung": PJ0["probe_windung"]}
    for pdat in pole_dat:
        q = json.load(open(pdat))
        besch["proben_teil_A"][os.path.basename(pdat)] = {"momentprobe": q["momentprobe"], "sprungprobe": q["sprungprobe"],
                                                          "blattprobe": q["blattprobe"], "probe_windung": q["probe_windung"]}
    besch["kontrollen_erwartung"] = KJ["kontrollen"]
    besch["gammas"] = KJ["gammas"]
    # ---------- Zuwachs (beschreibend, B2) ----------
    zuw = {}
    for v in VN:
        for r in prho:
            Ev = E[f"{v}_rho{r:g}"][0]
            for c in range(kd.NC):
                for lage, (i0, i1) in {"A": (0, 6), "B": (1, 7), "C": (2, 8)}.items():
                    zuw[f"{v}_rho{r:g}_eta{kd.ETAS[c]:g}_{lage}"] = float((abs(Ev[c, i1]) / abs(ref[c, i1]))
                                                                         / (abs(Ev[c, i0]) / abs(ref[c, i0])))
    zs = {}
    for iv, v in enumerate(VN):
        m = daten["phi"][:, iv].mean(axis=0)
        for c in range(kd.NC):
            zs[f"{v}_eta{kd.ETAS[c]:g}_A"] = float((abs(m[c, 6]) / abs(ref[c, 6])) / (abs(m[c, 0]) / abs(ref[c, 0])))
    besch["zuwachs_erwartung"] = zuw
    besch["zuwachs_saatmittel_rho16"] = zs
    # ---------- Norm ----------
    norm = []
    nn = daten["n"]
    for iv, v in enumerate(VN):
        for c in range(kd.NC):
            R = nn[:, iv, c, :].mean(axis=0) / norm_c[c]
            Gs = (nn[:, iv, c, -1] / norm_c[c, -1]) / (nn[:, iv, c, 0] / norm_c[c, 0])
            norm.append({"variante": v, "eta": kd.ETAS[c], "R": R.tolist(), "G": float(R[-1] / R[0]),
                         "G_saat_median": float(np.median(Gs)), "G_saat_min": float(Gs.min()), "G_saat_max": float(Gs.max())})
    besch["norm"] = norm
    # ---------- Linkzahlen ----------
    lz = {}
    for nm, kk in (("L0N", "linkzahl_L0_je_N"), ("L1N", "linkzahl_L1_je_N"), ("L2N", "linkzahl_L2_je_N")):
        x = daten[nm]
        mw = float(x.mean())
        se = float(x.std(ddof=1) / np.sqrt(x.size))
        ew = KJ[kk].get(str(rho))
        lz[nm] = {"mittel": mw, "SE": se, "erwartung": ew, "abw_in_SE": (mw - ew) / se if ew is not None else None}
    besch["linkzahlen_rho16"] = lz
    besch["N_mittel"] = float(daten["N"].mean())
    besch["max_abs_phi"] = {v: float(daten["maxphi"][:, iv].max()) for iv, v in enumerate(VN)}
    besch["zeit_je_saat"] = [float(daten["zeit"].min()), float(daten["zeit"].max())]
    # ---------- Repro VJ und V0 gegen KAUSAL-4D-SCHICHT-1 (gleiche Saaten) ----------
    rep = {}
    for j, sd_ in enumerate(daten["saaten"]):
        f = os.path.join(s1_lauf, f"feld-r{rho:g}-s{sd_}.npz")
        if not os.path.exists(f):
            rep[str(sd_)] = None
            continue
        alt = np.load(f)
        rep[str(sd_)] = {nm: {"phi_p_bitgleich": bool(np.array_equal(daten["phi"][j][iv], alt["phi_p"][iv])),
                              "summen_bitgleich": bool(np.array_equal(daten["summen"][j][iv], alt["summen"][iv])),
                              "max_abs_abw_phi_p": float(np.abs(daten["phi"][j][iv] - alt["phi_p"][iv]).max())}
                         for iv, nm in ((0, "VJ"), (1, "V0"))}
    besch["repro_schicht1"] = rep
    besch["repro_alle_bitgleich"] = bool(rep and all(x is not None and all(y["phi_p_bitgleich"] and y["summen_bitgleich"]
                                                                          for y in x.values()) for x in rep.values()))
    # ---------- Bilder ----------
    mark = {4.0: "o", 8.0: "s", 16.0: "^"}
    fig, ax = plt.subplots(2, 2, figsize=(15, 11))
    for ik, k in enumerate(ks):
        a = ax[0, ik]
        for v in VN:
            for r in prho:
                e = erg[key(v, r, k)]
                Z = [z for z in e["nullstellen_A"] + e["nullstellen_S"] + e["nullstellen_S0"]]
                if Z:
                    Z = np.array(Z)
                    a.plot(Z[:, 0], Z[:, 1], mark[r], color=FARBE[v], ms=7, alpha=0.8)
                sh = e["schale"]
                if sh is not None:
                    a.plot([sh["omega_re"]], [sh["omega_im"]], mark[r], color=FARBE[v], ms=8,
                           mfc=(FARBE[v] if sh["blatt"] == "I" else "none"))
        a.axhline(0.0, color="k", lw=0.6)
        a.axhline(0.05, color="grey", lw=0.6, ls=":")
        a.set_xlim(-3, 3)
        a.set_ylim(-0.4, 1.0)
        a.set_title(f"Nullstellen von 1 + m^2 k~_gen, k = {k:.3f} (voll: Blatt I, offen: Blatt II)", fontsize=9)
        a.set_xlabel("Re omega")
        a.set_ylabel("Im omega")
    for v in VN:
        ax[0, 0].plot([], [], "o", color=FARBE[v], label=v)
    for r in prho:
        ax[0, 0].plot([], [], mark[r], color="k", label=f"rho = {r:g}")
    ax[0, 0].legend(fontsize=7)
    a = ax[1, 0]
    for v in VN:
        for r in prho:
            sh = sch(v, r, 0.0)
            if sh is not None:
                a.plot([sh["omega_re"]], [sh["omega_im"]], mark[r], color=FARBE[v], ms=8,
                       mfc=(FARBE[v] if sh["blatt"] == "I" else "none"))
    a.set_yscale("symlog", linthresh=1e-4)
    a.axhline(0.0, color="k", lw=0.6)
    a.axhline(SCHWELLE_S21, color="C4", ls="--", lw=0.8, label="S2-1: 0,004")
    a.axhline(0.002, color="grey", ls=":", lw=0.8, label="Grenze S / S0: 0,002")
    a.set_xlabel("Re omega")
    a.set_ylabel("Im omega (symlog)")
    a.set_title("Schalennullstellen bei k = 0 (Lupe, symlog)", fontsize=9)
    a.legend(fontsize=7)
    a = ax[1, 1]
    rr = np.linspace(3.5, 17, 100)
    for v in VN:
        for k, ls in ((0.0, "-"), (ks[1], "--")):
            y = []
            for r in prho:
                sh = sch(v, r, k)
                y.append(sh["omega_im"] if sh else np.nan)
            y = np.array(y)
            a.plot(prho, np.abs(y), "o" + ls, color=FARBE[v], mfc=None if k == 0.0 else "none",
                   label=f"{v}, k = {k:.2f} (Numerik, Betrag)")
        a.plot(rr, [schreibtisch(v, x, 0.0) for x in rr], ":", color=FARBE[v], lw=1.5,
               label=f"{v}: Schreibtisch, k = 0")
    a.axhline(SCHWELLE_S21, color="C4", ls="--", lw=0.8)
    a.set_xscale("log")
    a.set_yscale("log")
    a.set_xlabel("rho")
    a.set_ylabel("abs(Im omega) der Schalennullstelle")
    a.set_title("Im omega gegen rho (alle Werte Blatt I = Wachstum, sonst Vermerk)", fontsize=9)
    a.legend(fontsize=6)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "pole.png"), dpi=110)
    plt.close(fig)
    # Streuung
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    for iv, v in enumerate(VN):
        y = [srel[(v, c, i)] for c in range(kd.NC) for i in range(NP)]
        x = np.full(len(y), iv) + np.linspace(-0.25, 0.25, len(y))
        ax.plot(x, y, ".", color=FARBE[v], alpha=0.7)
        ax.plot([iv - 0.35, iv + 0.35], [s[v]] * 2, "-", color="k", lw=2)
    ax.axhline(0.636, color="C2", ls=":", label="SCHICHT-1: s_V0 = 0,636")
    ax.set_xticks(range(len(VN)))
    ax.set_xticklabels([f"{v}\nrho = 16" for v in VN])
    ax.set_yscale("log")
    ax.set_ylabel("relative Streuung sd/abs(Kontinuum) je Pruefpunkt (Strich: geom. Mittel)")
    ax.set_title(f"Streuung je Saat, {n} Saaten, dieselben Streuungen fuer alle Varianten", fontsize=9)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "streuung_varianten.png"), dpi=110)
    plt.close(fig)
    # Saatmittel gegen Erwartung und Kontinuum
    fig, ax = plt.subplots(3, 2, figsize=(13, 12))
    for iv, v in enumerate(VN):
        for c in range(kd.NC):
            a = ax[iv, c]
            z = pp[c, NP:NPP, 3]
            Pp = daten["phi"][:, iv, c, NP:NPP]
            m = Pp.mean(axis=0)
            se_r = Pp.real.std(axis=0, ddof=1) / np.sqrt(Pp.shape[0])
            se_i = Pp.imag.std(axis=0, ddof=1) / np.sqrt(Pp.shape[0])
            Ev = E[f"{v}_rho{rho:g}"][0, c, NP:NPP]
            a.errorbar(z, m.real, yerr=se_r, fmt="o", ms=3, color="C0", label="Re, Saatmittel +- SE")
            a.errorbar(z, m.imag, yerr=se_i, fmt="s", ms=3, color="C1", label="Im, Saatmittel +- SE")
            a.plot(z, phi_k[c, NP:NPP].real, "-", color="C0", lw=1, label="Re, Kontinuum")
            a.plot(z, phi_k[c, NP:NPP].imag, "-", color="C1", lw=1, label="Im, Kontinuum")
            a.plot(z, Ev.real, ":", color="C0", lw=1.4, label=f"Re, Erwartung {v}")
            a.plot(z, Ev.imag, ":", color="C1", lw=1.4, label=f"Im, Erwartung {v}")
            a.set_title(f"{v}, eta = {kd.ETAS[c]:g}, t = 3,2, x = y = 0, rho = 16, {Pp.shape[0]} Saaten", fontsize=9)
            a.set_xlabel("z")
            a.legend(fontsize=6)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "saatmittel_erwartung_kontinuum.png"), dpi=100)
    plt.close(fig)
    # Zuwachs gegen t
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    a = ax[0]
    ta = pa[0, :, 0]
    for v in VN:
        for r, ls in ((16.0, "-"), (8.0, "--"), (4.0, ":")):
            Ev = E[f"{v}_rho{r:g}"][0, 0, NPP:]
            a.plot(ta, np.abs(Ev) / np.abs(phi_k[0, NPP:]), ls, color=FARBE[v], lw=1.2, label=f"{v}, rho = {r:g}")
        Pq = daten["phi"][:, VN.index(v), 0, :NP]
        m = Pq.mean(axis=0)
        sd = np.sqrt(Pq.real.var(axis=0, ddof=1) + Pq.imag.var(axis=0, ddof=1)) / np.sqrt(Pq.shape[0])
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
        a.plot(tm, daten["n"][:, VN.index(v), 0, :].mean(axis=0) / norm_c[0], "o-", color=FARBE[v], label=f"{v}, rho = 16")
    a.axhline(1.0, color="k", lw=0.6)
    a.set_yscale("log")
    a.set_xlabel("t (Scheibenmitte)")
    a.set_ylabel("Saatmittel n_k / n_c,k (eta = 0)")
    a.set_title("Norm je Zeitscheibe gegen Kontinuum", fontsize=9)
    a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "zuwachs_t.png"), dpi=110)
    plt.close(fig)
    out = {"urteile": urteile, "beschreibend": besch, "n_saaten_soll": n_soll, "skript_sha256": SKRIPT_SHA,
           "schicht2_feld_sha256": sf.SKRIPT_SHA,
           "pole_sha256": [hashlib.sha256(open(pd, "rb").read()).hexdigest() for pd in pole_dat],
           "erwartung_json_sha256": hashlib.sha256(open(os.path.join(kont, "erwartung.json"), "rb").read()).hexdigest(),
           "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(aus, "auswertung.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps({k: urteile[k]["urteil"] for k in urteile}))


if __name__ == "__main__":
    main()
