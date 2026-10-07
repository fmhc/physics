#!/usr/bin/env python3
"""HAGEDORN-1: Auswertung nach PLAN.md Abschnitt 3 (Urteilsregeln) und Bilder.

Aufruf (nur ueber kleintest.sh auf der .69):
    auswertung.py --lauf ORDNER_MIT_zeile_*.json --profile ORDNER/zeilen.json --out ORDNER
Ausgabe: auswertung.json ({"urteile": {...}, ...}), bild_max_im.png, bild_ringast.png, bild_E_R.png.
"""
import os

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import datetime
import glob
import json
import math

import numpy as np

M_LISTE = (0, 1, 2, 3, 5, 8)
W2_LISTE = (0.55, 0.70, 0.85, 0.95, 0.99)
IM_INSTABIL = 1e-4
IM_STABIL = 1e-6
NULL_TOL = 1e-6
KONV_TOL = 1e-4
HG1_M, HG1_W2 = (3, 5, 8), (0.95, 0.99)
HG2_M, HG2_W2 = (1, 2, 3, 5, 8), (0.55, 0.70)
HG3_L = (2, 3, 4, 5, 6)
HG3_R2, HG4_TOL = 0.98, 0.15


def wkey(w2):
    return f"{w2:.2f}"


def klasse(im):
    if im > IM_INSTABIL:
        return "instabil"
    if im < IM_STABIL:
        return "stabil"
    return "grau"


def fit(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    A = np.vstack([x, np.ones_like(x)]).T
    (b, a), *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - (a + b * x)
    sst = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - float(np.sum(res ** 2)) / sst if sst > 0 else float("nan")
    return dict(a=float(a), b=float(b), R2=r2, n=int(x.size))


def zeile_auswerten(z):
    s_l = {s["l"]: s for s in z["sektoren"]}
    f_l = {s["l"]: s for s in z.get("fein", {}).get("sektoren", [])}
    max_im = max(s["max_im_gezaehlt"] for s in z["sektoren"])
    l_max = max(z["sektoren"], key=lambda s: s["max_im_gezaehlt"])["l"]
    kl_b = klasse(max_im)
    # fein: gezaehlte Instabilitaeten mit Im > IM_STABIL verfolgt; sonst gilt der Basiswert (< IM_STABIL)
    im_f = []
    konv = []
    for l, s in s_l.items():
        if s["kandidaten"] and s["kandidaten"][0]["omega"][1] > IM_STABIL:
            e = f_l.get(l, {})
            w = e.get("max_im")
            if w is None:
                im_f.append(float("nan"))
                konv.append(dict(art="max_im", l=l, basis=s["kandidaten"][0]["omega"], fein=None, rel=None))
            else:
                im_f.append(w[1])
                konv.append(dict(art="max_im", l=l, basis=s["kandidaten"][0]["omega"], fein=w, rel=e["max_im_rel"]))
        else:
            im_f.append(s["max_im_gezaehlt"])
    if z.get("fein"):
        if any(not math.isfinite(v) for v in im_f):
            kl_f = "nicht konvergiert"
        else:
            kl_f = klasse(max(im_f))
    else:
        kl_f = None
    if kl_f is None:
        kl = kl_b
    elif kl_f == kl_b:
        kl = kl_b
    else:
        kl = "nicht konvergiert"
    ring = {}
    ring_fein = {}
    for l, s in s_l.items():
        if s["ringast"]:
            ring[l] = s["ringast"]["omega"][0]
            e = f_l.get(l, {})
            if e.get("ringast") is not None:
                ring_fein[l] = dict(fein=e["ringast"][0], rel=e["ringast_rel"])
    null_b = [s.get("nullpaar_max_betrag") for l, s in s_l.items() if l in (0, 1)]
    null_f = []
    for l in (0, 1):
        e = f_l.get(l, {})
        if e.get("nullpaar"):
            null_f.append(max(math.hypot(*w) for w in e["nullpaar"]))
    nm = z["nullmoden"]
    return dict(m=z["m"], w2=z["w2"], R_max=z["R_max"], E=z["E"], Q=z["Q"], max_im=max_im, l_max_im=l_max,
                klasse_basis=kl_b, klasse_fein=kl_f, klasse=kl, max_im_fein=max(im_f) if im_f else None,
                ringast=ring, ringast_fein=ring_fein, konv_max_im=konv,
                null_betrag_basis=max(v for v in null_b if v is not None) if any(v is not None for v in null_b)
                else None, null_betrag_fein=max(null_f) if null_f else None,
                res_phase=nm["res_phase_innen"], res_verallgemeinert=nm["res_verallgemeinert_innen"],
                res_phase_ganz=nm["res_phase"], res_verschiebung_ganz=nm["res_verschiebung"],
                res_verallgemeinert_ganz=nm["res_verallgemeinert"], f_omega_abw=nm["f_omega_abw_differenz_gegen_exakt"],
                res_verschiebung=nm["res_verschiebung_innen"], dQ_domega=nm["dQ_domega"],
                dQ_domega_differenz=nm["dQ_domega_differenz"],
                res_fein=dict(phase=z["fein"]["nullmoden"]["res_phase_innen"],
                              verallgemeinert=z["fein"]["nullmoden"]["res_verallgemeinert_innen"],
                              verschiebung=z["fein"]["nullmoden"]["res_verschiebung_innen"]) if z.get("fein") else None,
                randmoden=[(s["l"], r["omega"], r["randanteil"]) for s in z["sektoren"] for r in s["randmoden"]],
                kasten=z.get("kasten"), gitter=z["basis"], n_l=len(z["sektoren"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lauf", required=True)
    ap.add_argument("--profile", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    zeilen = {}
    for p in sorted(glob.glob(os.path.join(args.lauf, "zeile_m*_w*.json"))):
        with open(p) as fh:
            z = json.load(fh)
        if z.get("status") == "gerechnet":
            zeilen[(z["m"], wkey(z["w2"]))] = zeile_auswerten(z)
    with open(args.profile) as fh:
        prof = {(z["m"], wkey(z["w2"])): z for z in json.load(fh)["zeilen"]}
    fehlend = [f"{m}:{w2}" for w2 in W2_LISTE for m in M_LISTE if (m, wkey(w2)) not in zeilen
               or zeilen[(m, wkey(w2))]["n_l"] != 13]
    urteile = {}

    # ---- HG0 ----
    alle = [zeilen[k] for k in sorted(zeilen)]
    # (a) berichtigt: Residuen der Phasen- und Verschiebungsmode im Innenbereich (Basis und fein) <= 1e-6
    a_res = all(max(z["res_phase"], z["res_verschiebung"]) <= NULL_TOL and
                (z["res_fein"] is None or max(z["res_fein"]["phase"], z["res_fein"]["verschiebung"]) <= NULL_TOL)
                for z in alle)
    b_null = all(z["null_betrag_basis"] is not None and z["null_betrag_basis"] <= NULL_TOL for z in alle)
    konv_liste = []
    for z in alle:
        if z["max_im"] > IM_STABIL:
            k = max(z["konv_max_im"], key=lambda e: e["basis"][1]) if z["konv_max_im"] else None
            konv_liste.append(dict(m=z["m"], w2=z["w2"], art="max_im", rel=k["rel"] if k else None))
    hg3_zeilen = [z for z in alle if z["klasse"] == "stabil" and z["m"] >= 2]
    for z in hg3_zeilen:
        for l in HG3_L:
            rf = z["ringast_fein"].get(l)
            konv_liste.append(dict(m=z["m"], w2=z["w2"], art=f"ringast l={l}", rel=rf["rel"] if rf else None))
    c_konv = bool(konv_liste) and all(e["rel"] is not None and e["rel"] <= KONV_TOL for e in konv_liste)
    if not konv_liste:
        c_konv = True
    vk = []
    for w2 in W2_LISTE:
        z = zeilen.get((0, wkey(w2)))
        if z is None:
            vk.append(dict(w2=w2, ok=None))
            continue
        soll = "stabil" if z["dQ_domega"] < 0 else "instabil"
        vk.append(dict(w2=w2, dQ_domega=z["dQ_domega"], klasse=z["klasse"], soll=soll, ok=z["klasse"] == soll))
    d_vk = all(v["ok"] for v in vk) if all(v["ok"] is not None for v in vk) else None
    werte0 = dict(max_res_phase_innen=max(z["res_phase"] for z in alle),
                  max_res_verschiebung_innen=max(z["res_verschiebung"] for z in alle),
                  max_res_verschiebung_innen_fein=max((z["res_fein"]["verschiebung"] for z in alle if z["res_fein"]),
                                                      default=None),
                  max_res_verallgemeinert_innen_beschreibend=max(z["res_verallgemeinert"] for z in alle),
                  max_f_omega_abw_beschreibend=max(z["f_omega_abw"] for z in alle),
                  max_res_phase_ganzer_kasten=max(z["res_phase_ganz"] for z in alle),
                  max_res_verschiebung_ganzer_kasten=max(z["res_verschiebung_ganz"] for z in alle),
        max_nullpaar_betrag_basis=max(z["null_betrag_basis"] for z in alle),
        max_nullpaar_betrag_fein=max((z["null_betrag_fein"] for z in alle if z["null_betrag_fein"] is not None),
                                     default=None),
        konvergenz=konv_liste, max_konvergenz_rel=max((e["rel"] for e in konv_liste if e["rel"] is not None),
                                                      default=None), vk=vk,
        a_residuen=a_res, b_nullpaar_kartenwortlaut=b_null, c_konvergenz=c_konv, d_vk=d_vk)
    if fehlend or d_vk is None:
        u0 = "nicht auswertbar"
    else:
        u0 = "eingetroffen" if (a_res and c_konv and d_vk) else "nicht eingetroffen"
    u0_wort = "nicht auswertbar" if (fehlend or d_vk is None) else (
        "eingetroffen" if (b_null and c_konv and d_vk) else "nicht eingetroffen")
    urteile["HG0"] = dict(urteil=u0, vermerk=f"Urteil nach Kartenwortlaut (Nullmoden als Eigenwertbetrag <= 1e-6): "
                                             f"{u0_wort}. Berichtigte Regel (a) Residuen, PLAN.md Abschnitt 3.",
                          werte=werte0)

    # ---- HG1 ----
    kl1 = {f"{m}:{w2}": (zeilen[(m, wkey(w2))]["klasse"] if (m, wkey(w2)) in zeilen else "fehlt")
           for w2 in HG1_W2 for m in HG1_M}
    w1 = {k: dict(klasse=v, max_im=zeilen[(int(k.split(':')[0]), wkey(float(k.split(':')[1])))]["max_im"]
                  if v != "fehlt" else None) for k, v in kl1.items()}
    if any(v in ("stabil", "grau") for v in kl1.values()):
        u1 = "nicht eingetroffen"
    elif all(v == "instabil" for v in kl1.values()):
        u1 = "eingetroffen"
    else:
        u1 = "nicht auswertbar"
    urteile["HG1"] = dict(urteil=u1, werte=w1)

    # ---- HG2 ----
    kl2 = {f"{m}:{w2}": (zeilen[(m, wkey(w2))]["klasse"] if (m, wkey(w2)) in zeilen else "fehlt")
           for w2 in HG2_W2 for m in HG2_M}
    w2d = {k: dict(klasse=v, max_im=zeilen[(int(k.split(':')[0]), wkey(float(k.split(':')[1])))]["max_im"]
                   if v != "fehlt" else None) for k, v in kl2.items()}
    if any(v == "stabil" for v in kl2.values()):
        u2 = "eingetroffen"
    elif all(v in ("instabil", "grau") for v in kl2.values()):
        u2 = "nicht eingetroffen"
    else:
        u2 = "nicht auswertbar"
    urteile["HG2"] = dict(urteil=u2, werte=w2d)

    # ---- HG3 ----
    w3 = {}
    ergebnisse = []
    for z in hg3_zeilen:
        k = f"{z['m']}:{z['w2']}"
        if all(l in z["ringast"] for l in HG3_L):
            ft = fit(HG3_L, [z["ringast"][l] for l in HG3_L])
            ok = ft["R2"] > HG3_R2 and ft["b"] > 0.0
            w3[k] = dict(fit=ft, ringast={str(l): z["ringast"][l] for l in HG3_L}, R_max=z["R_max"],
                         b_mal_R=ft["b"] * z["R_max"], erfuellt=ok)
            ergebnisse.append(ok)
        else:
            w3[k] = dict(fehlende_l=[l for l in HG3_L if l not in z["ringast"]], erfuellt=None)
            ergebnisse.append(None)
    if any(e is False for e in ergebnisse):
        u3 = "nicht eingetroffen"
    elif ergebnisse and all(e is True for e in ergebnisse):
        u3 = "eingetroffen"
    else:
        u3 = "nicht auswertbar"
    urteile["HG3"] = dict(urteil=u3, werte=dict(zeilen=w3, anzahl_stabil_m_ab_2=len(hg3_zeilen)))

    # ---- HG4 ----
    w4 = {}
    erg4 = []
    for w2 in W2_LISTE:
        st = [zeilen[(m, wkey(w2))] for m in M_LISTE if m >= 1 and (m, wkey(w2)) in zeilen
              and zeilen[(m, wkey(w2))]["klasse"] == "stabil"]
        if len(st) >= 2:
            ft = fit(np.log([z["R_max"] for z in st]), np.log([z["E"] for z in st]))
            ok = abs(ft["b"] - 1.0) <= HG4_TOL
            w4[wkey(w2)] = dict(m=[z["m"] for z in st], steigung=ft["b"], R2=ft["R2"], erfuellt=ok)
            erg4.append(ok)
        else:
            w4[wkey(w2)] = dict(m=[z["m"] for z in st], steigung=None, erfuellt=None)
    if any(e is False for e in erg4):
        u4 = "nicht eingetroffen"
    elif erg4:
        u4 = "eingetroffen"
    else:
        u4 = "nicht auswertbar"
    urteile["HG4"] = dict(urteil=u4, vermerk="Steigung aus RG-1 vorab ableitbar (PLAN.md Abschnitt 0); neu ist nur "
                                             "die Auswahl der stabilen Profile.", werte=w4)

    tabelle = [dict(m=z["m"], w2=z["w2"], klasse=z["klasse"], klasse_basis=z["klasse_basis"],
                    klasse_fein=z["klasse_fein"], max_im=z["max_im"], l_max_im=z["l_max_im"],
                    max_im_fein=z["max_im_fein"], R_max=z["R_max"], E=z["E"], Q=z["Q"],
                    ringast={str(l): v for l, v in sorted(z["ringast"].items())},
                    ringast_fein={str(l): v for l, v in sorted(z["ringast_fein"].items())},
                    null_betrag_basis=z["null_betrag_basis"], null_betrag_fein=z["null_betrag_fein"],
                    res_phase=z["res_phase"], res_verallgemeinert=z["res_verallgemeinert"],
                    res_verschiebung=z["res_verschiebung"], res_fein=z["res_fein"], dQ_domega=z["dQ_domega"],
                    dQ_domega_differenz=z["dQ_domega_differenz"], randmoden=z["randmoden"], kasten=z["kasten"],
                    gitter=z["gitter"]) for z in alle]
    aus = dict(erstellt=datetime.datetime.now().astimezone().isoformat(timespec="seconds"), fehlend=fehlend,
               urteile=urteile, tabelle=tabelle)
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "auswertung.json.tmp"), "w") as fh:
        json.dump(aus, fh, indent=1, ensure_ascii=False, default=float)
    os.replace(os.path.join(args.out, "auswertung.json.tmp"), os.path.join(args.out, "auswertung.json"))
    for k, v in urteile.items():
        print(k, v["urteil"], v.get("vermerk", ""))

    # ---- Bilder ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:  # noqa: BLE001
        print("keine Bilder:", e)
        return
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for m in M_LISTE:
        xs = [w2 for w2 in W2_LISTE if (m, wkey(w2)) in zeilen]
        ys = [max(zeilen[(m, wkey(w2))]["max_im"], 1e-14) for w2 in xs]
        ax.semilogy(xs, ys, "o-", label=f"m = {m}")
    ax.axhline(IM_INSTABIL, color="k", ls="--", lw=0.8)
    ax.axhline(IM_STABIL, color="k", ls=":", lw=0.8)
    ax.set_xlabel("omega^2")
    ax.set_ylabel("max Im Omega (l = 0..12, gezaehlt; Boden 1e-14)")
    ax.set_title("HAGEDORN-1: groesste Anwachsrate je Profil")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(args.out, "bild_max_im.png"), dpi=130)
    plt.close(fig)
    st = [z for z in alle if z["klasse"] == "stabil"]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for z in st:
        ls = sorted(z["ringast"])
        if not ls:
            continue
        ax.plot(ls, [z["ringast"][l] for l in ls], "o-", ms=3, label=f"m = {z['m']}, w2 = {z['w2']}")
    ax.set_xlabel("l")
    ax.set_ylabel("Re Omega (Ringast, kleinste positive Ringmode)")
    ax.set_title("Ringast je stabilem Profil")
    if st:
        ax.legend(fontsize=6, ncol=2)
    fig.tight_layout()
    fig.savefig(os.path.join(args.out, "bild_ringast.png"), dpi=130)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for w2 in W2_LISTE:
        zz = [zeilen[(m, wkey(w2))] for m in M_LISTE if m >= 1 and (m, wkey(w2)) in zeilen]
        if not zz:
            continue
        line, = ax.loglog([z["R_max"] for z in zz], [z["E"] for z in zz], "-", lw=0.8, label=f"w2 = {w2}")
        for z in zz:
            ax.loglog(z["R_max"], z["E"], "o", color=line.get_color(),
                      mfc=line.get_color() if z["klasse"] == "stabil" else "none")
    ax.set_xlabel("R (Ort des Maximums von f)")
    ax.set_ylabel("E")
    ax.set_title("E gegen R bei festem omega (gefuellt: stabil)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(args.out, "bild_E_R.png"), dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    main()
