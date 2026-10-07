"""KAUSAL-4D-KERNMASSE-1: Auswertung nach PLAN.md (Urteilsregeln KM0 bis KM2, Abschnitt 7), Bilder, auswertung.json.

Aufruf (nur ueber kleintest.sh):
  kernmasse_auswertung.py <lauf> <kont> <ausgabe> <n_soll> <s2_pole_VJ.json> <s2_lauf> <s1_lauf> <s2_erwartung.npz> [rhos]
    (rhos nur fuer die Pfadprobe vor dem Einfrieren; Hauptlauf ohne, also 4,8,16; KM0-Felder: rhos[2] gegen s2_lauf,
     rhos[1] gegen s1_lauf, Saaten 1 bis n_soll)
    lauf: feld-r{4,8,16}-s*.npz/.json (Varianten VJ, V0, V00, VK)
    kont: kern.json, pole-VK.json, pole-VJ.json (Wiederholung mit schicht2_kont.py), erwartung-VK-a.json/.npz
          (rho = 4, 8, 16), erwartung-VK-b.json/.npz (Kontrollen)
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
import kernmasse_feld as kf  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
NAMEN = list(kf.NAMEN)            # VJ, V0, V00, VK
RHOS = (4.0, 8.0, 16.0)
NP = 9
SCHWELLE_KM2 = -0.2
TOL_RES = 1e-3
TOL_FOURIER = 1e-6
TREFFER_MIN = 15
FARBE = {"VJ": "C0", "V0": "C2", "V00": "C4", "VK": "C3"}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def lade(lauf, rho):
    fs = sorted(glob.glob(os.path.join(lauf, f"feld-r{rho:g}-s*.npz")), key=lambda p: int(p.split("-s")[-1].split(".")[0]))
    d = {"saaten": [], "phi": [], "n": [], "endlich": [], "N": [], "zeit": [], "maxrss": []}
    for f in fs:
        s = int(f.split("-s")[-1].split(".")[0])
        kopf = json.load(open(f.replace(".npz", ".json")))
        d["endlich"].append(bool(kopf["endlich"]))
        if not kopf["endlich"]:
            continue
        z = np.load(f)
        d["saaten"].append(s)
        d["phi"].append(z["phi_p"])                                           # (NV, NC, 26)
        d["n"].append(z["summen"][..., 0].sum(axis=3) / (rho * kd.SCHEIBE_W))  # (NV, NC, 4)
        d["N"].append(kopf["N"])
        d["zeit"].append(kopf["zeit_gesamt_s"])
        d["maxrss"].append(kopf["maxrss_mb"])
    for k in ("phi", "n", "N", "zeit", "maxrss"):
        d[k] = np.array(d[k])
    return d


def statistik(phi, E, K):
    """phi (n, NC, NP) komplex; E, K (NC, NP). Saatmittel, sd, SE, Treffer in 3 SE von E, relative Streuung."""
    n = phi.shape[0]
    m = phi.mean(axis=0)
    sd = np.sqrt(phi.real.var(axis=0, ddof=1) + phi.imag.var(axis=0, ddof=1))
    se = sd / np.sqrt(n)
    abw = np.abs(m - E) / se
    return {"n": int(n), "mittel": m, "sd": sd, "se": se, "abw_E_in_SE": abw, "treffer": int((abw <= 3.0).sum()),
            "max_abw_SE": float(abw.max()), "rel_K": sd / np.abs(K), "rel_E": sd / np.abs(E),
            "s": float(np.exp(np.mean(np.log(sd / np.abs(K))))), "s_E": float(np.exp(np.mean(np.log(sd / np.abs(E))))),
            "abw_K_in_SE": np.abs(m - K) / se}


def steigung(rhos, s):
    return float(np.polyfit(np.log(np.array(rhos)), np.log(np.array(s)), 1)[0])


def main():
    lauf, kont, aus = sys.argv[1], sys.argv[2], sys.argv[3]
    n_soll = int(sys.argv[4])
    s2_pole, s2_lauf, s1_lauf, s2_erw = sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]
    global RHOS
    if len(sys.argv) > 9:
        RHOS = tuple(float(x) for x in sys.argv[9].split(","))
    os.makedirs(aus, exist_ok=True)
    # Teil A: pole-VK*.json und erwartung-VK-a*.json/.npz duerfen auf mehrere Laeufe verteilt sein (je Dichte)
    pv_dateien = sorted(glob.glob(os.path.join(kont, "pole-VK*.json")))
    PV = {"ergebnisse": {}, "probe_windung": None}
    for p in pv_dateien:
        q = json.load(open(p))
        PV["ergebnisse"].update(q["ergebnisse"])
        PV["probe_windung"] = PV["probe_windung"] or q["probe_windung"]
    PJ = json.load(open(os.path.join(kont, "pole-VJ.json")))
    PJ2 = json.load(open(s2_pole))
    KJ = json.load(open(os.path.join(kont, "kern.json")))
    ea_dateien = sorted(glob.glob(os.path.join(kont, "erwartung-VK-a*.json")))
    EA = {"realisierungsfehler": {}}
    EAn = {}
    kappen = []
    for p in ea_dateien:
        EA["realisierungsfehler"].update(json.load(open(p))["realisierungsfehler"])
        z = np.load(p.replace(".json", ".npz"))
        kappen.append(z["quad_kappe"])
        EAn.update({k: z[k] for k in z.files})
    EB = json.load(open(os.path.join(kont, "erwartung-VK-b.json")))
    EBn = np.load(os.path.join(kont, "erwartung-VK-b.npz"))
    S2E = np.load(s2_erw)
    K = kappen[0]                                                            # (NC, 9) gekapptes Kontinuum
    urteile, besch = {}, {}
    besch["quad_kappe_gleich_schicht2"] = bool(np.array_equal(K, S2E["quad_kappe"]))
    besch["quad_kappe_gleich_in_allen_laeufen"] = bool(all(np.array_equal(K, q) for q in kappen + [EBn["quad_kappe"]]))
    besch["teil_A_dateien"] = [os.path.basename(p) for p in pv_dateien + ea_dateien]

    # ---------- KM0 ----------
    def ohne_zeit(d):
        return {k: v for k, v in d.items() if k != "zeit_s"}
    pol_gleich = {}
    for key, ref in PJ2["ergebnisse"].items():
        mine = PJ["ergebnisse"].get(key)
        pol_gleich[key] = bool(mine is not None and ohne_zeit(mine) == ohne_zeit(ref))
    a_ok = bool(len(pol_gleich) == 6 and all(pol_gleich.values()))
    schalen = {key: {"neu": [PJ["ergebnisse"][key]["schale"]["omega_re"], PJ["ergebnisse"][key]["schale"]["omega_im"]],
                     "schicht2": [ref["schale"]["omega_re"], ref["schale"]["omega_im"]]}
               for key, ref in PJ2["ergebnisse"].items() if key in PJ["ergebnisse"]}
    feld_gleich, fehlt = {}, []
    for (rho, refdir, idx) in ((RHOS[2], s2_lauf, (0, 1, 2)), (RHOS[1], s1_lauf, (0, 1))):
        for s in range(1, n_soll + 1):
            fm = os.path.join(lauf, f"feld-r{rho:g}-s{s}.npz")
            fr = os.path.join(refdir, f"feld-r{rho:g}-s{s}.npz")
            if not (os.path.exists(fm) and os.path.exists(fr)):
                fehlt.append(f"r{rho:g}-s{s}")
                continue
            m_, r_ = np.load(fm), np.load(fr)
            feld_gleich[f"r{rho:g}-s{s}"] = {NAMEN[i]: bool(np.array_equal(m_["phi_p"][i], r_["phi_p"][i])
                                                            and np.array_equal(m_["summen"][i], r_["summen"][i]))
                                             for i in idx}
    b_ok = bool(not fehlt and all(all(v.values()) for v in feld_gleich.values()))
    if fehlt or len(pol_gleich) != 6:
        u0 = "nicht auswertbar"
    else:
        u0 = "eingetroffen" if (a_ok and b_ok) else "nicht eingetroffen"
    u0k = ("eingetroffen" if a_ok else "nicht eingetroffen") if len(pol_gleich) == 6 else "nicht auswertbar"
    urteile["KM0"] = {"urteil_plan": u0, "urteil_karte": u0k,
                      "werte": {"pole_bitgleich_je_fall": pol_gleich, "pole_alle_bitgleich": a_ok, "schalen": schalen,
                                "felder_bitgleich_je_saat": feld_gleich, "felder_alle_bitgleich": b_ok, "fehlend": fehlt}}

    # ---------- KM1 ----------
    faelle = PV["ergebnisse"]
    stabil = {k: bool(e["alle_stabil"]) for k, e in faelle.items()}
    pole = {k: e["pole"] for k, e in faelle.items()}
    gezaehlt = {k: {r: e[f"zaehlung_{r}"]["zahl"] for r in ("A", "S", "S0")} for k, e in faelle.items()}
    lokal = {k: {r: len(e[f"nullstellen_{r}"]) for r in ("A", "S", "S0")} for k, e in faelle.items()}
    res = {k: e["residuum_probe"] for k, e in faelle.items()}
    res_ok = bool(all(e["residuum_probe"]["1e-05"][2] <= TOL_RES for e in faelle.values()))
    schranke = {r: KJ["ergebnisse"][f"rho{r:g}"]["schranke"] for r in RHOS}
    schranke_ok = bool(all(v["eingehalten"] for v in schranke.values()))
    fourier = {r: max(v["rel_abw"] for v in KJ["ergebnisse"][f"rho{r:g}"]["fourierprobe"].values()) for r in RHOS}
    fourier_ok = bool(all(v <= TOL_FOURIER for v in fourier.values()))
    alle_stabil = bool(len(faelle) == 6 and all(stabil.values()))
    pol0 = bool(all(v == 0 for p in pole.values() for v in p.values()))
    w1 = {"faelle": len(faelle), "zaehlungen_stabil": stabil, "pole_N_lok_minus_W": pole, "windungszahlen": gezaehlt,
          "lokalisierte_nullstellen": lokal, "residuum_probe": res, "residuum_ok": res_ok, "schranke_t": schranke,
          "schranke_ok": schranke_ok, "fourierprobe_max_rel_abw": fourier, "fourierprobe_ok": fourier_ok}
    if not (alle_stabil and res_ok and schranke_ok and fourier_ok):
        u1 = "nicht auswertbar"
        w1["vermerk"] = "Baufehler-Bedingung verletzt (PLAN 7.2)"
    elif not pol0:
        u1 = "nicht auswertbar"
        w1["vermerk"] = "Polzahl ungleich 0 widerspricht der Ableitung (VORAB 4): Baufehler (PLAN 7.2)"
    else:
        u1 = "eingetroffen"
    k0 = [k for k in faelle if k.endswith("_k0.0000")]
    stab_k = all(stabil[k] for k in k0)
    pk = [pole[k][r] for k in k0 for r in ("S", "S0")]
    if len(k0) != 3 or not stab_k or any(x < 0 for x in pk):
        u1k = "nicht auswertbar"
    else:
        u1k = "eingetroffen" if all(x == 0 for x in pk) else "nicht eingetroffen"
    urteile["KM1"] = {"urteil_plan": u1, "urteil_karte": u1k, "werte": w1}

    # ---------- Teil B: Felder ----------
    daten = {r: lade(lauf, r) for r in RHOS}
    st = {}
    for r in RHOS:
        d = daten[r]
        if len(d["saaten"]) < 2:
            continue
        for iv, v in enumerate(NAMEN):
            if v == "VK":
                E = EAn[f"E_real_rho{r:g}"][:, :NP]
            elif f"E_{v}_rho{r:g}" in S2E.files:
                E = S2E[f"E_{v}_rho{r:g}"][0, :, :NP]
            else:
                continue
            st[(v, r)] = statistik(d["phi"][:, iv, :, :NP], E, K)
    n_ok = bool(all(len(daten[r]["saaten"]) >= n_soll and all(daten[r]["endlich"]) for r in RHOS))
    treffer_vk = {r: (st[("VK", r)]["treffer"] if ("VK", r) in st else None) for r in RHOS}
    bau_ok = bool(all(t is not None and t >= TREFFER_MIN for t in treffer_vk.values()))
    w2 = {"n_saaten": {r: len(daten[r]["saaten"]) for r in RHOS}, "treffer_VK_in_3SE_eigene_erwartung": treffer_vk,
          "bau_ok": bau_ok}
    if n_ok and all(("VK", r) in st for r in RHOS):
        s_vk = [st[("VK", r)]["s"] for r in RHOS]
        beta = steigung(RHOS, s_vk)
        w2.update({"s_VK": dict(zip([str(r) for r in RHOS], s_vk)), "steigung_LSQ": beta,
                   "steigung_4_8": float(np.log(s_vk[1] / s_vk[0]) / np.log(2.0)),
                   "steigung_8_16": float(np.log(s_vk[2] / s_vk[1]) / np.log(2.0)),
                   "monoton_fallend": bool(s_vk[0] > s_vk[1] > s_vk[2]), "schwelle": SCHWELLE_KM2})
        rng = np.random.default_rng(np.random.SeedSequence([20261004, 41, 99]))
        bs = []
        for _ in range(4000):
            sv = []
            for r in RHOS:
                ph = daten[r]["phi"][:, 3, :, :NP]
                idx = rng.integers(0, ph.shape[0], ph.shape[0])
                q = ph[idx]
                sd = np.sqrt(q.real.var(axis=0, ddof=1) + q.imag.var(axis=0, ddof=1))
                sv.append(float(np.exp(np.mean(np.log(np.maximum(sd, 1e-300) / np.abs(K))))))
            bs.append(steigung(RHOS, sv))
        bs = np.array(bs)
        w2["steigung_bootstrap"] = {"p2.5": float(np.percentile(bs, 2.5)), "p16": float(np.percentile(bs, 16)),
                                    "p50": float(np.percentile(bs, 50)), "p84": float(np.percentile(bs, 84)),
                                    "p97.5": float(np.percentile(bs, 97.5)),
                                    "anteil_unter_schwelle": float(np.mean(bs <= SCHWELLE_KM2))}
        if bau_ok:
            u2 = "eingetroffen" if beta <= SCHWELLE_KM2 else "nicht eingetroffen"
        else:
            u2 = "nicht auswertbar"
            w2["vermerk"] = "Baufehler: Saatmittel VK trifft das eigene Mittel nicht (PLAN 7.3)"
        u2k = "eingetroffen" if beta <= SCHWELLE_KM2 else "nicht eingetroffen"
    else:
        u2, u2k = "nicht auswertbar", "nicht auswertbar"
    urteile["KM2"] = {"urteil_plan": u2, "urteil_karte": u2k, "werte": w2}

    # ---------- beschreibend ----------
    tab = {}
    for (v, r), x in st.items():
        tab[f"{v}_rho{r:g}"] = {"n": x["n"], "s": x["s"], "s_gegen_E": x["s_E"], "treffer_3SE_eigene_erwartung": x["treffer"],
                                "max_abw_SE": x["max_abw_SE"], "treffer_3SE_kontinuum": int((x["abw_K_in_SE"] <= 3).sum()),
                                "s_je_t": {f"{t:g}": float(np.exp(np.mean(np.log(x["rel_K"][:, 3 * j:3 * j + 3]))))
                                           for j, t in enumerate(kd.PRUEF_T)},
                                "s_gegen_E_je_t": {f"{t:g}": float(np.exp(np.mean(np.log(x["rel_E"][:, 3 * j:3 * j + 3]))))
                                                   for j, t in enumerate(kd.PRUEF_T)},
                                "rel_streuung_je_punkt": x["rel_K"].ravel().tolist(),
                                "betrag_mittel_zu_K": (np.abs(x["mittel"]) / np.abs(K)).ravel().tolist()}
    besch["streuung_und_treffer"] = tab
    besch["steigungen_LSQ"] = {v: steigung(RHOS, [st[(v, r)]["s"] for r in RHOS]) for v in NAMEN
                               if all((v, r) in st for r in RHOS)}
    vk = {}
    for r in RHOS:
        Ez = EAn[f"E_ziel_rho{r:g}"][:, :NP]
        Er = EAn[f"E_real_rho{r:g}"][:, :NP]
        z = {}
        for c in range(kd.NC):
            for lage, (i0, i1) in {"A": (0, 6), "B": (1, 7), "C": (2, 8)}.items():
                z[f"ziel_eta{kd.ETAS[c]:g}_{lage}"] = float((abs(Ez[c, i1]) / abs(K[c, i1])) / (abs(Ez[c, i0]) / abs(K[c, i0])))
                z[f"real_eta{kd.ETAS[c]:g}_{lage}"] = float((abs(Er[c, i1]) / abs(K[c, i1])) / (abs(Er[c, i0]) / abs(K[c, i0])))
        vk[f"rho{r:g}"] = {"betrag_ziel_zu_K": [float((np.abs(Ez) / np.abs(K)).min()), float((np.abs(Ez) / np.abs(K)).max())],
                           "betrag_real_zu_K": [float((np.abs(Er) / np.abs(K)).min()), float((np.abs(Er) / np.abs(K)).max())],
                           "real_minus_ziel_rel_K_max": float((np.abs(Er - Ez) / np.abs(K)).max()),
                           "phase_ziel_minus_K_rad": [float(np.angle(Ez / K).min()), float(np.angle(Ez / K).max())],
                           "zuwachs_t2_bis_3_2": z}
        if ("VK", r) in st:
            m = st[("VK", r)]["mittel"]
            vk[f"rho{r:g}"]["zuwachs_saatmittel_A"] = {f"eta{kd.ETAS[c]:g}": float((abs(m[c, 6]) / abs(K[c, 6]))
                                                                                  / (abs(m[c, 0]) / abs(K[c, 0])))
                                                       for c in range(kd.NC)}
    besch["VK_mittel"] = vk
    besch["VJ_V0_V00_zuwachs_erwartung"] = {f"{v}_rho{r:g}": float((abs(S2E[f'E_{v}_rho{r:g}'][0, 0, 6]) / abs(K[0, 6]))
                                                                    / (abs(S2E[f'E_{v}_rho{r:g}'][0, 0, 0]) / abs(K[0, 0])))
                                            for v in ("VJ", "V0", "V00") for r in RHOS if f"E_{v}_rho{r:g}" in S2E.files}
    norm = []
    norm_c = S2E["norm_c"]
    for r in RHOS:
        nn = daten[r]["n"]
        if nn.size == 0:
            continue
        for iv, v in enumerate(NAMEN):
            for c in range(kd.NC):
                R = nn[:, iv, c, :].mean(axis=0) / norm_c[c]
                Gs = (nn[:, iv, c, -1] / norm_c[c, -1]) / (nn[:, iv, c, 0] / norm_c[c, 0])
                norm.append({"rho": r, "variante": v, "eta": kd.ETAS[c], "R": R.tolist(), "G": float(R[-1] / R[0]),
                             "G_saat_median": float(np.median(Gs)), "G_saat_min": float(Gs.min()),
                             "G_saat_max": float(Gs.max())})
    besch["norm"] = norm
    besch["pole_VK_ziel"] = {k: {"pole": e["pole"], "windung": {r: e[f"zaehlung_{r}"]["zahl"] for r in ("A", "S", "S0")},
                                 "nullstellen_A": e["nullstellen_A"], "nullstellen_S": e["nullstellen_S"],
                                 "nullstellen_S0": e["nullstellen_S0"], "residuum_probe": e["residuum_probe"],
                                 "newton_auf_1_durch_G": e["newton_auf_1_durch_G"], "max_abs_G_bogen": e["max_abs_G_bogen"],
                                 "quadratur_128_256_rel_max": e["quadratur_128_256_rel_max"]} for k, e in faelle.items()}
    besch["probe_windung_VK"] = PV["probe_windung"]
    besch["kern"] = KJ["ergebnisse"]
    besch["erwartung_kontrollen"] = EB["kontrollen"]
    besch["realisierungsfehler"] = EA["realisierungsfehler"]
    k4 = f"E_ziel_rho{RHOS[0]:g}"
    besch["erwartung_b_gegen_a_rho_min_max_abs"] = float(np.abs(EBn[k4] - EAn[k4]).max()) \
        if k4 in EBn.files else None
    besch["zeit_je_saat"] = {str(r): [float(daten[r]["zeit"].min()), float(daten[r]["zeit"].max())]
                             for r in RHOS if daten[r]["zeit"].size}
    besch["maxrss_mb"] = {str(r): float(daten[r]["maxrss"].max()) for r in RHOS if daten[r]["maxrss"].size}
    besch["N_mittel"] = {str(r): float(daten[r]["N"].mean()) for r in RHOS if daten[r]["N"].size}
    besch["max_abs_phi_pruefpunkte"] = {f"{v}_rho{r:g}": float(np.abs(daten[r]["phi"][:, iv]).max())
                                        for r in RHOS for iv, v in enumerate(NAMEN) if daten[r]["phi"].size}

    # ---------- Bilder ----------
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    a = ax[0]
    for v in NAMEN:
        if all((v, r) in st for r in RHOS):
            y = [st[(v, r)]["s"] for r in RHOS]
            a.plot(RHOS, y, "o-", color=FARBE[v], label=f"{v}: Steigung {steigung(RHOS, y):+.2f}")
    if "s_VK" in w2:
        y0 = w2["s_VK"][str(RHOS[0])]
        a.plot(RHOS, [y0 * (r / RHOS[0]) ** SCHWELLE_KM2 for r in RHOS], ":", color="k", label="Schwelle KM2: rho^-0,2 ab VK(rho_min)")
    a.set_xscale("log")
    a.set_yscale("log")
    a.set_xticks(RHOS)
    a.set_xticklabels([f"{r:g}" for r in RHOS])
    a.set_xlabel("rho")
    a.set_ylabel("s = geom. Mittel sd/|K| (18 Pruefpunkte)")
    a.set_title(f"Einzelnetz-Streuung gegen Dichte, {n_soll} Saaten je Dichte, dieselben Netze je Variante", fontsize=9)
    a.legend(fontsize=7)
    a = ax[1]
    for r, mk in zip(RHOS, ("o", "s", "^")):
        if ("VK", r) not in st:
            continue
        x = st[("VK", r)]
        idx = np.arange(18)
        a.plot(idx, (np.abs(EAn[f"E_ziel_rho{r:g}"][:, :NP]) / np.abs(K)).ravel(), "-", color="C3",
               alpha=0.3 + 0.2 * RHOS.index(r), lw=1)
        a.plot(idx, (np.abs(EAn[f"E_real_rho{r:g}"][:, :NP]) / np.abs(K)).ravel(), "--", color="C1",
               alpha=0.3 + 0.2 * RHOS.index(r), lw=1)
        a.errorbar(idx + 0.1 * RHOS.index(r), (np.abs(x["mittel"]) / np.abs(K)).ravel(), yerr=(x["se"] / np.abs(K)).ravel(),
                   fmt=mk, ms=4, color="k", alpha=0.4 + 0.2 * RHOS.index(r), label=f"Saatmittel VK, rho = {r:g}")
    a.axhline(1.0, color="k", lw=0.6)
    a.set_xlabel("Pruefpunkt (0-8: eta = 0, 9-17: eta = 0,5; je t = 2,0 / 2,6 / 3,2)")
    a.set_ylabel("|E| / |K| (K = gekapptes Kontinuum)")
    a.set_title("VK: Ziel-Mittel (rot), Mittel der Realisierung (orange, gestrichelt), Saatmittel +- SE", fontsize=9)
    a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "streuung_und_mittel.png"), dpi=110)
    plt.close(fig)
    fig, a = plt.subplots(1, 1, figsize=(8, 5))
    ta = EBn["achsenpunkte"][0, :, 0]
    Kax = EBn["E_ziel_rho1e+06"][:, NP:]
    for r, ls in zip(RHOS[::-1], ("-", "--", ":")):
        a.plot(ta, np.abs(EAn[f"E_ziel_rho{r:g}"][0, NP:]) / np.abs(Kax[0]), ls, color="C3", label=f"VK Ziel, rho = {r:g}")
        a.plot(ta, np.abs(EAn[f"E_real_rho{r:g}"][0, NP:]) / np.abs(Kax[0]), ls, color="C1", label=f"VK Realisierung, rho = {r:g}")
        if f"E_VJ_rho{r:g}" in S2E.files:
            a.plot(ta, np.abs(S2E[f"E_VJ_rho{r:g}"][0, 0, 26:]) / np.abs(S2E["phi_k"][0, 26:]), ls, color="C0",
               label=f"VJ (SCHICHT-2), rho = {r:g}")
    a.axhline(1.0, color="k", lw=0.6)
    a.set_yscale("log")
    a.set_xlabel("t (Paketmitte, eta = 0)")
    a.set_ylabel("|E| / |Kontinuum|")
    a.set_title("Mittel auf der Achse: VK gegen Ziel bei rho = 1e6 (gekappt), VJ gegen k-Raum (ungekappt)", fontsize=9)
    a.legend(fontsize=6, ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(aus, "achse_mittel.png"), dpi=110)
    plt.close(fig)

    out = {"urteile": urteile, "beschreibend": besch, "n_saaten_soll": n_soll, "skript_sha256": SKRIPT_SHA,
           "kernmasse_feld_sha256": kf.SKRIPT_SHA,
           "eingaben_sha256": {os.path.basename(p): sha(p) for p in
                               [os.path.join(kont, f) for f in ("kern.json", "pole-VJ.json",
                                                                "erwartung-VK-b.json", "erwartung-VK-b.npz")]
                               + pv_dateien + ea_dateien + [p.replace(".json", ".npz") for p in ea_dateien]
                               + [s2_pole, s2_erw]},
           "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(aus, "auswertung.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps({k: [urteile[k]["urteil_plan"], urteile[k]["urteil_karte"]] for k in urteile}))


if __name__ == "__main__":
    main()
