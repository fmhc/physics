#!/usr/bin/env python3
# QCA-BCC-RUECK-1: Bilder aus den Laufdateien (nur Darstellung, keine Urteile).
# Aufruf (nur ueber kleintest.sh auf der .69): bild.py AUSGABEORDNER PRAEFIX L1.json [L2.json ...]
import json
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import qca_rueck as q  # noqa: E402

KAT = [("rueck+Kegel iso proj", "Rueck (je Block) + Kegel, isotrop, 360 Grad = -1", "#1b7f4c"),
       ("rueck+Kegel", "Rueck (je Block) + Kegel", "#7fbf3f"),
       ("rueck ohne Kegel", "Rueck (je Block), kein Kegel bei 0", "#c9b22b"),
       ("rueck nur Matrix", "Rueck nur als Matrix (entkoppelte Bloecke)", "#d9822b"),
       ("einseitig", "einseitig (nur S+ oder nur S-)", "#c0392b"),
       ("trivial", "trivial", "#9a9a9a"), ("ungueltig", "Defekt nach Politur > 1e-20", "#5d6d7e")]


def panel(ax, faelle, titel):
    names = list(faelle.keys())
    x = np.arange(len(names))
    bottom = np.zeros(len(names))
    for key, lab, col in KAT:
        v = np.array([faelle[n]["kategorien"].get(key, 0) for n in names], float)
        ax.bar(x, v, bottom=bottom, color=col, label=lab)
        bottom += v
    smax = max(faelle[n]["starts"] for n in names)
    for i, n in enumerate(names):
        dm = faelle[n]["D_min"]
        ax.text(i, bottom[i] + 0.01 * smax, "leer" if dm is None else f"{dm:.0e}", rotation=90, ha="center",
                va="bottom", fontsize=5)
    ax.set_xticks(x)
    ax.set_xticklabels([n.split("|", 1)[1] for n in names], rotation=80, ha="right", fontsize=5.5)
    ax.set_ylim(0, smax * 1.45)
    ax.set_ylabel("Treffer (Defekt < 1e-10)", fontsize=7)
    ax.set_title(titel + " (Zahl: kleinster Defekt)", fontsize=8)


def omega_panel(ax, rep, titel):
    freqs = np.array(rep["freqs"])
    A = np.array(rep["A"]["re"]) + 1j * np.array(rep["A"]["im"])
    pfad = q.PFAD_BCC
    x0 = 0.0
    ticks, labs = [0.0], [pfad[0][0]]
    for (la, a), (lb, b) in zip(pfad[:-1], pfad[1:]):
        t = np.linspace(0, 1, 220)
        ks = a[None, :] + t[:, None] * (b - a)[None, :]
        L = np.linalg.norm(b - a)
        ph = np.sort(np.angle(np.linalg.eigvals(q.W_at(freqs, A, ks / q.SQ3))), axis=1)
        for j in range(ph.shape[1]):
            ax.plot(x0 + t * L, ph[:, j], ".", ms=0.8, color=f"C{j % 10}")
        x0 += L
        ticks.append(x0)
        labs.append(lb)
        ax.axvline(x0, color="0.85", lw=0.6)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labs, fontsize=7)
    ax.set_ylim(-np.pi * 1.03, np.pi * 1.03)
    ax.set_title(titel, fontsize=7)
    ax.set_ylabel("Eigenphasen omega(k)", fontsize=6)


def main():
    outdir, praefix = sys.argv[1], sys.argv[2]
    laeufe = [json.load(open(p)) for p in sys.argv[3:]]
    alle, t0 = {}, None
    for d in laeufe:
        alle.update(d["faelle"])
        if d["teil"] == "0":
            t0 = d["teil0"]
    panels = []
    if t0:
        panels.append((t0["qr0_suche"], "Teil 0: L2:Pauli, s = 2 (Kontrolle QR0)"))
    for teil, txt in (("4", "s = 4"), ("8", "s = 8")):
        for form in "NO":
            sub = {k: v for k, v in alle.items() if k.startswith(teil + "|") and k.split("|")[2] == form}
            if sub:
                panels.append((dict(sorted(sub.items(), key=lambda kv: (kv[0].split("|")[3], kv[0]))),
                               f"{txt}, Form {form}"))
    if panels:
        n = len(panels)
        fig, axs = plt.subplots(n, 1, figsize=(15, 3.6 * n), squeeze=False)
        for ax, (sub, ttl) in zip(axs[:, 0], panels):
            panel(ax, sub, ttl)
        axs[0, 0].legend(fontsize=6, loc="upper left", ncol=2)
        fig.tight_layout()
        fig.savefig(f"{outdir}/{praefix}treffer_je_fall.png", dpi=110)
        plt.close(fig)
    reps = []
    if t0:
        reps.append(("Quelle: Weyl A+ (Eq. 24), L_2, s = 2", {"freqs": q.S_BCC.tolist(),
                                                              "A": q.cplx(q.weyl_quelle(1))}))
        st = t0["qr0_suche"].get("L2:Pauli|N|r50")
        if st and st.get("repr"):
            reps.append(("Suche L2:Pauli r50: " + st["repr"]["kategorie"], st["repr"]))
        for k in ("K4_gemischt_0", "K4_direkte_Summe_0", "K5_gemischt_0"):
            if k in t0["konstruktionen"]:
                reps.append((f"Konstruktion {k}: {t0['konstruktionen'][k]['kategorie']}", t0["konstruktionen"][k]["repr"]))
    beste = {}
    for k, st in alle.items():
        if st.get("repr") is None:
            continue
        teil, nm, form, var = k.split("|")
        key = (teil, nm)
        if key not in beste or st["repr"]["rang"] > beste[key][1]["repr"]["rang"]:
            beste[key] = (k, st)
    for key in sorted(beste):
        k, st = beste[key]
        reps.append((f"{k}: {st['repr']['kategorie']}", st["repr"]))
    reps = reps[:24]
    if reps:
        n = len(reps)
        nc = 4
        nr = int(np.ceil(n / nc))
        fig, axs = plt.subplots(nr, nc, figsize=(4.4 * nc, 3.2 * nr), squeeze=False)
        for ax in axs.ravel()[n:]:
            ax.axis("off")
        for ax, (ttl, rep) in zip(axs.ravel(), reps):
            omega_panel(ax, rep, ttl)
        fig.suptitle("Eigenphasen von W(k) laengs Γ-H-N-Γ-P-H (BCC), je Darstellung der beste Treffer", fontsize=10, y=0.997)
        fig.tight_layout(rect=(0, 0, 1, 0.98))
        fig.savefig(f"{outdir}/{praefix}omega_treffer.png", dpi=105)
        plt.close(fig)
    print("bilder fertig", flush=True)


if __name__ == "__main__":
    main()
