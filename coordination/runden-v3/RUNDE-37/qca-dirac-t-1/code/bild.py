#!/usr/bin/env python3
# QCA-DIRAC-T-1, Runde 38: Bilder aus den Laufdateien (nur Darstellung, keine Urteile).
# Aufruf (nur ueber kleintest.sh auf der .69): bild.py AUSGABEORDNER PRAEFIX L1.json [L2.json ...]
import json
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import qca_dirac as q  # noqa: E402

KAT = [("massiv", "massiv (Luecke, alle Kanten quadratisch)", "#2a7f62"), ("Kegel bei 0", "Kegel bei k = 0 (linear)", "#c98b2b"),
       ("sonst", "sonst", "#7a8fb5"), ("trivial", "trivial (nur Vor-Ort-Term o. ae.)", "#9a9a9a")]


def zaehle(st):
    z = {k: 0 for k, _, _ in KAT}
    for h in st["hits"]:
        z[h["klasse"]] += 1
    return z


def panel_treffer(ax, faelle, titel):
    names = list(faelle.keys())
    x = np.arange(len(names))
    bottom = np.zeros(len(names))
    for key, lab, col in KAT:
        v = np.array([zaehle(faelle[n])[key] for n in names], float)
        ax.bar(x, v, bottom=bottom, color=col, label=lab)
        bottom += v
    smax = max(faelle[n]["starts"] for n in names)
    for i, n in enumerate(names):
        dm = faelle[n]["D_min"]
        ax.text(i, bottom[i] + 0.01 * smax, "leer" if dm is None else f"{dm:.0e}", rotation=90, ha="center",
                va="bottom", fontsize=6)
    ax.set_xticks(x)
    lab = []
    for n in names:
        st = faelle[n]
        lab.append(n.replace("B|", "").replace("A|", "") + ("" if "klasse_K" not in st else " " + q.KLASSEN8[st["klasse_K"]]))
    ax.set_xticklabels(lab, rotation=70, ha="right", fontsize=7)
    ax.set_ylim(0, smax * 1.4)
    ax.set_ylabel("Treffer (Defekt < 1e-10)", fontsize=8)
    ax.set_title(titel + " (Zahl ueber dem Balken: kleinster Defekt)", fontsize=9)


def omega_panel(ax, rep, titel):
    freqs = np.array(rep["freqs"])
    A = np.array(rep["A"]["re"]) + 1j * np.array(rep["A"]["im"])
    pfad = q.PFAD_BCC
    x0 = 0.0
    ticks, labs = [0.0], [pfad[0][0]]
    for (la, a), (lb, b) in zip(pfad[:-1], pfad[1:]):
        t = np.linspace(0, 1, 260)
        ks = a[None, :] + t[:, None] * (b - a)[None, :]
        L = np.linalg.norm(b - a)
        ph = np.sort(np.angle(np.linalg.eigvals(q.W_at(freqs, A, ks / q.SQ3))), axis=1)
        for j in range(ph.shape[1]):
            ax.plot(x0 + t * L, ph[:, j], ".", ms=1.0, color=f"C{j % 10}")
        x0 += L
        ticks.append(x0)
        labs.append(lb)
        ax.axvline(x0, color="0.85", lw=0.6)
    W0 = q.W_at(freqs, A, np.zeros((1, 3)))[0]
    cl, _ = q.cluster_zerlegung(W0)
    phs = sorted(c for c, _ in cl)
    # Luecke bei k = 0 markieren: Phasen der Cluster bei Gamma, kleinster Halbabstand als Band
    for c in phs:
        ax.plot([0, 0.35], [c, c], color="k", lw=0.8)
    if len(phs) >= 2:
        d = [(np.angle(np.exp(1j * (phs[(i + 1) % len(phs)] - phs[i]))) % (2 * np.pi), i) for i in range(len(phs))]
        dm, i = min(d)
        lo = phs[i]
        ax.axhspan(lo, lo + dm, xmin=0, xmax=0.04, color="red", alpha=0.35)
        ax.text(0.4, lo + dm / 2, f"Luecke/2 = {dm / 2:.3g}", fontsize=6, color="red", va="center")
    ax.set_xticks(ticks)
    ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(-np.pi * 1.03, np.pi * 1.03)
    ax.set_title(titel, fontsize=8)
    ax.set_ylabel("Eigenphasen von W(k)", fontsize=7)


def main():
    outdir, praefix = sys.argv[1], sys.argv[2]
    laeufe = [json.load(open(p)) for p in sys.argv[3:]]
    fB, fA, t0 = {}, {}, None
    for d in laeufe:
        if d["teil"] == "B":
            fB.update(d["faelle"])
        elif d["teil"] == "A":
            fA.update(d["faelle"])
        else:
            t0 = d["teil0"]
    panels = []
    if fB:
        for form, txt in (("N", "Form N: 8 Spruenge"), ("O", "Form O: 8 Spruenge + Vor-Ort-Term"),
                          ("P", "Form P: O + Inversion")):
            sub = {k: v for k, v in sorted(fB.items()) if k.split("|")[1] == form}
            if sub:
                panels.append((sub, f"Teil B, s = 8, T, {txt}"))
    if fA or t0:
        sub = dict(fA)
        if t0:
            sub["0|N|T:2+2' (Suchkontrolle)"] = t0["suchkontrolle_T:2+2'"]
        panels.append((sub, "Teil A (T:2+2, s = 4) und Suchkontrolle T:2+2'"))
    if panels:
        fig, axs = plt.subplots(1, len(panels), figsize=(5.2 * len(panels), 5.8), squeeze=False)
        for ax, (sub, ttl) in zip(axs[0], panels):
            panel_treffer(ax, sub, ttl)
        axs[0, 0].legend(fontsize=6, loc="upper left")
        fig.tight_layout()
        fig.savefig(f"{outdir}/{praefix}treffer_je_zerlegung.png", dpi=120)
        plt.close(fig)
    reps = []
    if t0:
        reps.append(("Quelle: Dirac E+ (Eq. 36), m = 0,3, L_2", t0["quelle_dirac"]["E+|m=0.3"]["repr"]))
        for lab, ttl in (("a_spiegel|m=0.3", "Konstruktion a (C = P2 - P2'), m = 0,3"),
                         ("a_allgemein|m=0.3", "Konstruktion a, allgemeines C, m = 0,3"),
                         ("b_muenze_verschiebung|m=0.3", "Konstruktion b (Muenze x Verschiebung), m = 0,3")):
            if lab in t0["konstruktionen"]:
                reps.append((ttl, t0["konstruktionen"][lab]["repr"]))
    for k, st in sorted(fB.items()):
        if st.get("repr") is not None:
            reps.append((f"Suche {k.replace('B|', '')} {q.KLASSEN8[st['klasse_K']]}: {st['repr']['klasse']}", st["repr"]))
    if reps:
        n = len(reps)
        nc = 4
        nr = int(np.ceil(n / nc))
        fig, axs = plt.subplots(nr, nc, figsize=(4.4 * nc, 3.3 * nr), squeeze=False)
        for ax in axs.ravel()[n:]:
            ax.axis("off")
        for ax, (ttl, rep) in zip(axs.ravel(), reps):
            omega_panel(ax, rep, ttl)
        fig.suptitle("Eigenphasen von W(k) laengs Γ-H-N-Γ-P-H (BCC); schwarz: Cluster bei Γ, rot: kleinster Abstand (Luecke)",
                     fontsize=10, y=0.995)
        fig.tight_layout(rect=(0, 0, 1, 0.97))
        fig.savefig(f"{outdir}/{praefix}omega_hochsymmetrie.png", dpi=110)
        plt.close(fig)
    print("bilder fertig", flush=True)


if __name__ == "__main__":
    main()
