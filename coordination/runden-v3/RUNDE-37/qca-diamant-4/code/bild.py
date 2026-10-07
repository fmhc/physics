#!/usr/bin/env python3
# QCA-DIAMANT-4, Runde 38: Bilder aus den Laufdateien (nur Darstellung, keine Urteile).
# Aufruf (nur ueber kleintest.sh auf der .69): bild.py AUSGABEORDNER PRAEFIX L1.json [L2.json ...]
import json
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import qca_diamant as q  # noqa: E402

KAT = [("kegel", "Kegel bei k = 0", "#2a7f62"), ("ohne", "Entartung bei 0 ohne Kegel", "#c98b2b"),
       ("keine", "keine Entartung bei 0", "#7a8fb5"), ("trivial", "trivial", "#9a9a9a")]


def zaehle(st):
    z = {"kegel": 0, "ohne": 0, "keine": 0, "trivial": 0}
    for h in st["hits"]:
        k = h["klasse"]
        z["kegel" if k == "Kegel bei 0" else "ohne" if k.startswith("Entartung") else "trivial" if k == "trivial" else "keine"] += 1
    return z


def panel_treffer(ax, d, titel):
    names = list(d["faelle"].keys())
    x = np.arange(len(names))
    bottom = np.zeros(len(names))
    for key, lab, col in KAT:
        v = np.array([zaehle(d["faelle"][n])[key] for n in names], float)
        ax.bar(x, v, bottom=bottom, color=col, label=lab)
        bottom += v
    for i, n in enumerate(names):
        dm = d["faelle"][n]["D_min"]
        ax.text(i, bottom[i] + 1, "leer" if dm is None else f"{dm:.0e}", rotation=90, ha="center", va="bottom", fontsize=6)
    ax.set_xticks(x)
    ax.set_xticklabels([n.split("|", 1)[1] for n in names], rotation=70, ha="right", fontsize=7)
    ax.set_ylim(0, d["starts_je_fall"] * 1.35)
    ax.set_ylabel(f"Treffer (Defekt < 1e-10) von {d['starts_je_fall']} Starts", fontsize=8)
    ax.set_title(titel + " (Zahl ueber dem Balken: kleinster Defekt)", fontsize=9)


def omega_panel(ax, rep, pfad, titel):
    freqs = np.array(rep["freqs"])
    A = np.array(rep["A"]["re"]) + 1j * np.array(rep["A"]["im"])
    x0 = 0.0
    ticks, labs = [0.0], [pfad[0][0]]
    for (la, a), (lb, b) in zip(pfad[:-1], pfad[1:]):
        t = np.linspace(0, 1, 240)
        ks = a[None, :] + t[:, None] * (b - a)[None, :]
        L = np.linalg.norm(b - a)
        ph = np.sort(np.angle(np.linalg.eigvals(q.W_at(freqs, A, ks / q.SQ3))), axis=1)
        for j in range(ph.shape[1]):
            ax.plot(x0 + t * L, ph[:, j], ".", ms=1.2, color=f"C{j}")
        x0 += L
        ticks.append(x0)
        labs.append(lb)
        ax.axvline(x0, color="0.85", lw=0.6)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(-np.pi * 1.03, np.pi * 1.03)
    ax.set_title(titel, fontsize=8)
    ax.set_ylabel("Eigenphasen von W(k)", fontsize=7)


def main():
    outdir, praefix = sys.argv[1], sys.argv[2]
    laeufe = [json.load(open(p)) for p in sys.argv[3:]]
    gruppen = {}
    for d in laeufe:
        key = (d["teil"], d["fassung"] if d["teil"] == "A" else "-", d["variante"] if d["teil"] != "0" else "-")
        if key not in gruppen:
            gruppen[key] = dict(d)
            gruppen[key]["faelle"] = {}
        gruppen[key]["faelle"].update(d["faelle"])
    A = [gruppen[k] for k in sorted(gruppen) if k[0] == "A"]
    B = [gruppen[k] for k in sorted(gruppen) if k[0] == "B"]
    Z = [d for d in laeufe if d["teil"] == "0"]
    if A:
        fig, axs = plt.subplots(2, 2, figsize=(15, 10))
        for ax, d in zip(axs.ravel(), A):
            panel_treffer(ax, d, f"Teil A Diamant s = 4, Fassung {d['fassung']}, Variante {d['variante']}")
        axs[0, 0].legend(fontsize=7, loc="upper left")
        fig.tight_layout()
        fig.savefig(f"{outdir}/{praefix}treffer_teilA.png", dpi=120)
        plt.close(fig)
    if B or Z:
        fig, axs = plt.subplots(1, len(B) + len(Z), figsize=(6 * (len(B) + len(Z)), 5.5))
        axs = np.atleast_1d(axs)
        for ax, d in zip(axs, Z + B):
            ttl = "Teil 0 (Kontrolle s = 2)" if d["teil"] == "0" else f"Teil B BCC s = 4, T, Variante {d['variante']}"
            panel_treffer(ax, d, ttl)
        axs[0].legend(fontsize=7, loc="upper left")
        fig.tight_layout()
        fig.savefig(f"{outdir}/{praefix}treffer_teilB_0.png", dpi=120)
        plt.close(fig)
    for teil, ds, pfad in (("A", A, q.PFAD_FCC), ("B", B, q.PFAD_BCC)):
        reps = []
        for d in ds:
            for k, st in d["faelle"].items():
                if st.get("repr") is not None:
                    ttl = (f"F{d['fassung']} {d['variante']} {k.split('|', 1)[1]}" if teil == "A" else f"{d['variante']} {k.split('|', 1)[1]}")
                    ttl += " (Kegel bei 0)" if st["repr"]["kegel_0"] else " (kein Kegel bei 0)"
                    reps.append((ttl, st["repr"]))
        if not reps:
            continue
        n = len(reps)
        nc = 4
        nr = int(np.ceil(n / nc))
        fig, axs = plt.subplots(nr, nc, figsize=(4.2 * nc, 3.2 * nr), squeeze=False)
        for ax in axs.ravel()[n:]:
            ax.axis("off")
        for ax, (ttl, rep) in zip(axs.ravel(), reps):
            omega_panel(ax, rep, pfad, ttl)
        fig.suptitle(("Teil A: Zweischritt W = X Y auf dem Diamantnetz, Pfad Γ-X-W-L-Γ-K" if teil == "A"
                      else "Teil B: BCC, Pfad Γ-H-N-Γ-P-H") + "; je Fall ein Treffer (bevorzugt mit Kegel bei 0)", fontsize=10)
        fig.tight_layout()
        fig.savefig(f"{outdir}/{praefix}omega_teil{teil}.png", dpi=110)
        plt.close(fig)
    print("bilder fertig", flush=True)


if __name__ == "__main__":
    main()
