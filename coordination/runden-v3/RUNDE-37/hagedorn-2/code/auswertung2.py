#!/usr/bin/env python3
"""HAGEDORN-2: Auswertung nach PLAN.md Abschnitt 3 (Urteilsregeln) und Bilder.

Aufruf (nur ueber kleintest.sh auf der .69):
    auswertung2.py --lauf ORDNER_MIT_zeile_*.json [--dicht ORDNER_DICHTEPROBE] --profile ORDNER/zeilen.json --out ORDNER
Ausgabe: auswertung.json ({"urteile": {...}, ...}), bild_max_im.png, bild_E_R.png, bild_im_l.png.
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

M_LISTE = (3, 5, 8, 12)
W2_LISTE = (0.51, 0.52, 0.53, 0.54, 0.55)
IM_INSTABIL = 1e-4
IM_STABIL = 1e-6
HZ0_TOL = 1e-4
# HAGEDORN-1, lauf-69/auswertung.json (sha256 d7cc8577...069837): max Im Omega bei omega^2 = 0,55, l = 0..12,
# jeweils nur l = 2 instabil
HZ0_REF = {3: 0.004289658539286218, 5: 0.005402169215717179}
HZ1_M, HZ1_W2 = (3, 5, 8), 0.52
HZ2_M = (3, 5, 8)
HZ3_MIN_M, HZ3_TOL = 3, 0.15


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


def zeile_auswerten(z, d=None):
    s_l = {s["l"]: s for s in z["sektoren"]}
    f_l = {s["l"]: s for s in z.get("fein", {}).get("sektoren", [])}
    max_im = max(s["max_im_gezaehlt"] for s in z["sektoren"])
    l_max = max(z["sektoren"], key=lambda s: s["max_im_gezaehlt"])["l"]
    om_max = max(z["sektoren"], key=lambda s: s["max_im_gezaehlt"]).get("max_im_omega")
    kl_b = klasse(max_im)
    im_f = []
    konv = []
    for l, s in s_l.items():
        if s["kandidaten"] and s["kandidaten"][0]["omega"][1] > IM_STABIL:
            e = f_l.get(l, {})
            w = e.get("max_im")
            if w is None:
                im_f.append(float("nan"))
                konv.append(dict(l=l, basis=s["kandidaten"][0]["omega"], fein=None, rel=None))
            else:
                im_f.append(w[1])
                konv.append(dict(l=l, basis=s["kandidaten"][0]["omega"], fein=w, rel=e["max_im_rel"]))
        else:
            im_f.append(s["max_im_gezaehlt"])
    if z.get("fein"):
        kl_f = "nicht konvergiert" if any(not math.isfinite(v) for v in im_f) else klasse(max(im_f))
    else:
        kl_f = None
    kl = kl_b if (kl_f is None or kl_f == kl_b) else "nicht konvergiert"
    dicht = None
    if d is not None:
        d_max = max(s["max_im_gezaehlt"] for s in d["sektoren"])
        d_l = max(d["sektoren"], key=lambda s: s["max_im_gezaehlt"])["l"]
        d_kl = klasse(d_max)
        vollst = sorted(s["l"] for s in d["sektoren"]) == sorted(s["l"] for s in z["sektoren"])
        dicht = dict(max_im=d_max, l_max_im=d_l, klasse=d_kl, vollstaendig=vollst,
                     randmoden=sum(s.get("anzahl_randmoden", 0) for s in d["sektoren"]))
        if vollst and kl != "nicht konvergiert" and d_kl != kl:
            kl = "nicht konvergiert"
    kp = z.get("kasten")
    kasten_rel = None
    if kp:
        rel = [abs(complex(*e["kasten"]) - complex(*e["basis"])) / abs(complex(*e["basis"])) for e in kp["sektoren"]
               if e.get("kasten")]
        kasten_rel = max(rel) if rel else None
    ring = {s["l"]: s["ringast"]["omega"][0] for s in z["sektoren"] if s["ringast"]}
    im_l = {s["l"]: s["max_im_gezaehlt"] for s in z["sektoren"]}
    instab_l = [s["l"] for s in z["sektoren"] if s["max_im_gezaehlt"] > IM_STABIL]
    null_b = [s.get("nullpaar_max_betrag") for s in z["sektoren"] if s["l"] in (0, 1)]
    nm = z["nullmoden"]
    return dict(m=z["m"], w2=z["w2"], quelle=z["quelle"], R_max=z["R_max"], R_innen=z["R_innen"],
                R_aussen=z["R_aussen"], r_mittel=z.get("r_mittel"), E=z["E"], Q=z["Q"], max_im=max_im, l_max_im=l_max,
                omega_max_im=om_max, klasse_basis=kl_b, klasse_fein=kl_f, klasse=kl, dichteprobe=dicht,
                max_im_fein=max(im_f) if im_f else None, konv_max_im=konv,
                max_konv_rel=max((e["rel"] for e in konv if e["rel"] is not None), default=None),
                kasten_max_rel=kasten_rel, kasten=kp,
                max_im_bis_l12=max(s["max_im_gezaehlt"] for s in z["sektoren"] if s["l"] <= 12),
                instabile_l=instab_l, im_je_l={str(k): v for k, v in sorted(im_l.items())},
                ringast={str(k): v for k, v in sorted(ring.items())},
                randmoden=sum(s.get("anzahl_randmoden", 0) for s in z["sektoren"]),
                ungeprueft=sum(len(s.get("kandidaten_ungeprueft", [])) for s in z["sektoren"]),
                null_betrag_basis=max(v for v in null_b if v is not None) if any(v is not None for v in null_b) else None,
                res_phase_fenster=nm["res_phase_fenster"], res_verschiebung_fenster=nm["res_verschiebung_fenster"],
                res_verschiebung_fein=z.get("fein", {}).get("nullmoden", {}).get("res_verschiebung_fenster"),
                dQ_domega=nm["dQ_domega"], E_gitter=nm["gitter_integrale"]["E"], gitter=z["basis"],
                n_l=len(z["sektoren"]), l_soll=3 * z["m"] + 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lauf", required=True)
    ap.add_argument("--dicht", default="")
    ap.add_argument("--profile", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    dicht = {}
    if args.dicht:
        for p in sorted(glob.glob(os.path.join(args.dicht, "zeile_m*_w*.json"))):
            with open(p) as fh:
                d = json.load(fh)
            if d.get("status") == "gerechnet":
                dicht[(d["m"], wkey(d["w2"]))] = d
    zeilen = {}
    for p in sorted(glob.glob(os.path.join(args.lauf, "zeile_m*_w*.json"))):
        with open(p) as fh:
            z = json.load(fh)
        if z.get("status") == "gerechnet":
            zeilen[(z["m"], wkey(z["w2"]))] = zeile_auswerten(z, dicht.get((z["m"], wkey(z["w2"]))))
    with open(args.profile) as fh:
        prof = {(z["m"], wkey(z["w2"])): z for z in json.load(fh)["zeilen"]}
    fehlend = [f"{m}:{w2}" for w2 in W2_LISTE for m in M_LISTE if (m, wkey(w2)) not in zeilen
               or zeilen[(m, wkey(w2))]["n_l"] != zeilen[(m, wkey(w2))]["l_soll"]]

    def kl(m, w2):
        k = (m, wkey(w2))
        if k not in zeilen or zeilen[k]["n_l"] != zeilen[k]["l_soll"]:
            return "fehlt"
        return zeilen[k]["klasse"]

    urteile = {}
    # ---- HZ0: Anschluss an HAGEDORN-1 bei 0,55 (m = 3, 5), gemeinsamer l-Bereich 0..min(12, 3m) ----
    w0 = {}
    ok0 = []
    ok0_wort = []
    for m in (3, 5):
        z = zeilen.get((m, wkey(0.55)))
        if z is None or z["n_l"] != z["l_soll"]:
            w0[str(m)] = dict(fehlt=True)
            ok0.append(None)
            ok0_wort.append(None)
            continue
        d = abs(z["max_im_bis_l12"] - HZ0_REF[m])
        dw = abs(z["max_im"] - HZ0_REF[m])
        w0[str(m)] = dict(hagedorn1=HZ0_REF[m], hagedorn2_l_bis_12=z["max_im_bis_l12"], hagedorn2_l_bis_3m=z["max_im"],
                          l_max_im=z["l_max_im"], differenz=d, differenz_kartenwortlaut=dw, klasse=z["klasse"],
                          erfuellt=d <= HZ0_TOL)
        ok0.append(d <= HZ0_TOL)
        ok0_wort.append(dw <= HZ0_TOL)

    def urteil_alle(oks):
        if any(o is False for o in oks):
            return "nicht eingetroffen"
        if all(o is True for o in oks):
            return "eingetroffen"
        return "nicht auswertbar"

    u0w = urteil_alle(ok0_wort)
    urteile["HZ0"] = dict(urteil=urteil_alle(ok0), vermerk=f"Vergleich im gemeinsamen l-Bereich 0..min(12, 3m) "
                                                           f"(PLAN.md 3.2); nach Kartenwortlaut (l = 0..3m): {u0w}.",
                          werte=w0)

    # ---- HZ1: bei 0,52 sind m = 3, 5, 8 stabil ----
    k1 = {str(m): kl(m, HZ1_W2) for m in HZ1_M}
    w1 = {m: dict(klasse=v, max_im=zeilen[(int(m), wkey(HZ1_W2))]["max_im"] if v != "fehlt" else None,
                  l_max_im=zeilen[(int(m), wkey(HZ1_W2))]["l_max_im"] if v != "fehlt" else None,
                  dichteprobe=zeilen[(int(m), wkey(HZ1_W2))]["dichteprobe"] if v != "fehlt" else None)
          for m, v in k1.items()}
    if any(v in ("instabil", "grau") for v in k1.values()):
        u1 = "nicht eingetroffen"
    elif all(v == "stabil" for v in k1.values()):
        u1 = "eingetroffen"
    else:
        u1 = "nicht auswertbar"
    urteile["HZ1"] = dict(urteil=u1, werte=w1)

    # ---- HZ2: max Im faellt (nicht steigend) mit sinkendem omega^2 von 0,55 bis 0,51, stabil = 0 ----
    w2d = {}
    verstoesse = []
    vollst = True
    for m in HZ2_M:
        reihe = {}
        for w2 in W2_LISTE:
            k = kl(m, w2)
            if k in ("fehlt", "nicht konvergiert"):
                reihe[wkey(w2)] = None
                vollst = False
            elif k == "stabil":
                reihe[wkey(w2)] = 0.0
            else:
                reihe[wkey(w2)] = zeilen[(m, wkey(w2))]["max_im"]
        for wa in W2_LISTE:
            for wb in W2_LISTE:
                if wb < wa and reihe[wkey(wa)] is not None and reihe[wkey(wb)] is not None \
                        and reihe[wkey(wb)] > reihe[wkey(wa)]:
                    verstoesse.append(dict(m=m, hoeher=wkey(wa), tiefer=wkey(wb), wert_hoeher=reihe[wkey(wa)],
                                           wert_tiefer=reihe[wkey(wb)]))
        w2d[str(m)] = reihe
    if verstoesse:
        u2 = "nicht eingetroffen"
    elif vollst:
        u2 = "eingetroffen"
    else:
        u2 = "nicht auswertbar"
    urteile["HZ2"] = dict(urteil=u2, werte=dict(reihen=w2d, verstoesse=verstoesse))

    # ---- HZ3: E ~ R auf stabilen Profilen, je omega^2 mit mindestens drei stabilen m ----
    w3 = {}
    erg3 = []
    beschr = {}
    for w2 in W2_LISTE:
        st = [zeilen[(m, wkey(w2))] for m in M_LISTE if kl(m, w2) == "stabil"]
        alle = [zeilen[(m, wkey(w2))] for m in M_LISTE if (m, wkey(w2)) in zeilen]
        if len(alle) >= 2:
            fa = fit(np.log([z["R_max"] for z in alle]), np.log([z["E"] for z in alle]))
            fm = fit(np.log([z["r_mittel"] for z in alle]), np.log([z["E"] for z in alle]))
            beschr[wkey(w2)] = dict(m=[z["m"] for z in alle], steigung_R_max_alle_m=fa["b"],
                                    steigung_r_mittel_alle_m=fm["b"])
        if len(st) >= HZ3_MIN_M:
            ft = fit(np.log([z["R_max"] for z in st]), np.log([z["E"] for z in st]))
            fm = fit(np.log([z["r_mittel"] for z in st]), np.log([z["E"] for z in st]))
            ok = abs(ft["b"] - 1.0) <= HZ3_TOL
            w3[wkey(w2)] = dict(m=[z["m"] for z in st], steigung=ft["b"], R2=ft["R2"], erfuellt=ok,
                                steigung_r_mittel_beschreibend=fm["b"])
            erg3.append(ok)
        else:
            w3[wkey(w2)] = dict(m=[z["m"] for z in st], steigung=None, erfuellt=None)
    if any(e is False for e in erg3):
        u3 = "nicht eingetroffen"
    elif erg3:
        u3 = "eingetroffen"
    else:
        u3 = "nicht auswertbar"
    urteile["HZ3"] = dict(urteil=u3, vermerk="Steigung bei gegebener Auswahl aus den Profilen vorab ableitbar "
                                             "(PLAN.md 0.3); neu ist nur die Auswahl der stabilen m.",
                          werte=dict(je_omega2=w3, beschreibend_alle_m=beschr))

    tabelle = [zeilen[k] for k in sorted(zeilen, key=lambda k: (float(k[1]), k[0]))]
    aus = dict(erstellt=datetime.datetime.now().astimezone().isoformat(timespec="seconds"), fehlend=fehlend,
               urteile=urteile, tabelle=tabelle,
               profile={f"{k[0]}:{k[1]}": dict(quelle=v.get("quelle"), E=v.get("E"), R_max=v.get("R_max"),
                                                R_innen=v.get("R_innen"), R_aussen=v.get("R_aussen"),
                                                r_mittel=v.get("r_mittel"), Q=v.get("Q"),
                                                vergleich_quellen=v.get("vergleich_quellen"))
                        for k, v in prof.items()})
    os.makedirs(args.out, exist_ok=True)
    tmp = os.path.join(args.out, "auswertung.json.tmp")
    with open(tmp, "w") as fh:
        json.dump(aus, fh, indent=1, ensure_ascii=False, default=float)
    os.replace(tmp, os.path.join(args.out, "auswertung.json"))
    for k, v in urteile.items():
        print(k, v["urteil"], v.get("vermerk", ""))

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:  # noqa: BLE001
        print("keine Bilder:", e)
        return
    boden = 1e-12
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for m in M_LISTE:
        xs = [w2 for w2 in W2_LISTE if (m, wkey(w2)) in zeilen]
        ys = [max(zeilen[(m, wkey(w2))]["max_im"], boden) for w2 in xs]
        line, = ax.semilogy(xs, ys, "o-", label=f"m = {m}")
        for w2, y in zip(xs, ys):
            if zeilen[(m, wkey(w2))]["klasse"] == "nicht konvergiert":
                ax.plot(w2, y, "x", color="k", ms=9)
    ax.axhline(IM_INSTABIL, color="k", ls="--", lw=0.8)
    ax.axhline(IM_STABIL, color="k", ls=":", lw=0.8)
    ax.set_xlabel("omega^2")
    ax.set_ylabel(f"max Im Omega (l = 0..3m, gezaehlt; Boden {boden:g})")
    ax.set_title("HAGEDORN-2: groesste Anwachsrate je Profil")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(args.out, "bild_max_im.png"), dpi=130)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for w2 in W2_LISTE:
        zz = [zeilen[(m, wkey(w2))] for m in M_LISTE if (m, wkey(w2)) in zeilen]
        if not zz:
            continue
        line, = ax.loglog([z["R_max"] for z in zz], [z["E"] for z in zz], "-", lw=0.8, label=f"omega^2 = {w2}")
        for z in zz:
            ax.loglog(z["R_max"], z["E"], "o", color=line.get_color(),
                      mfc=line.get_color() if z["klasse"] == "stabil" else "none")
    rr = np.array([10.0, 150.0])
    ax.loglog(rr, 60.0 * rr, "k:", lw=0.8, label="Steigung 1")
    ax.set_xlabel("R (Ort des Maximums von f)")
    ax.set_ylabel("E")
    ax.set_title("E gegen R bei festem omega (gefuellt: stabil)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(args.out, "bild_E_R.png"), dpi=130)
    plt.close(fig)
    fig, axs = plt.subplots(1, len(W2_LISTE), figsize=(16, 3.8), sharey=True)
    for ax, w2 in zip(axs, W2_LISTE):
        for m in M_LISTE:
            z = zeilen.get((m, wkey(w2)))
            if z is None:
                continue
            ls = sorted(int(k) for k in z["im_je_l"])
            ax.semilogy([l / m for l in ls], [max(z["im_je_l"][str(l)], boden) for l in ls], ".-", ms=3,
                        label=f"m = {m}")
        ax.axhline(IM_STABIL, color="k", ls=":", lw=0.8)
        ax.set_title(f"omega^2 = {w2}")
        ax.set_xlabel("l / m")
    axs[0].set_ylabel("max Im Omega je l (gezaehlt)")
    axs[0].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(args.out, "bild_im_l.png"), dpi=110)
    plt.close(fig)


if __name__ == "__main__":
    main()
