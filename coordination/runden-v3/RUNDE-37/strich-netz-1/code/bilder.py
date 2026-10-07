#!/usr/bin/env python3
"""STRICH-NETZ-1: Bilder fuer Finn (PNG). Liest nur Laufdateien, rechnet nichts Neues.

Aufruf (nur ueber kleintest.sh):  python bilder.py <laufordner>
"""
import glob
import json
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.collections import LineCollection  # noqa: E402

D = sys.argv[1]
NAMEN = {"alle": "alle Paare", "gabriel": "Gabriel (kein Dritter dazwischen)", "delaunay": "Delaunay",
         "beruehrung": "Beruehrung (naechster Nachbar)", "wachstum": "Aufblasen mit Anhalten"}


def lade(p):
    with open(p) as f:
        return json.load(f)


def projektion(X):
    u = np.array([1.0, 0.55, 0.3])
    u /= np.linalg.norm(u)
    e1 = np.cross(u, [0.0, 0.0, 1.0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(u, e1)
    return np.stack([X @ e1, X @ e2], 1)


def bild_A():
    p = os.path.join(D, "teilA-b1.json")
    if not os.path.exists(p):
        return
    b = lade(p)["bild"]
    X = np.array(b["X"])
    P = projektion(X)
    les = [la for la in ("alle", "gabriel", "delaunay", "beruehrung", "wachstum") if la in b["u"]]
    fig, ax = plt.subplots(len(les), 3, figsize=(12, 3.3 * len(les)), constrained_layout=True)
    for r, la in enumerate(les):
        U = np.array(b["u"][la])
        U = U - U.mean(axis=1, keepdims=True)
        E = np.array(b["kanten"][la])
        vmax = np.max(np.abs(U))
        for c in range(3):
            a = ax[r, c]
            seg = np.stack([P[E[:, 0]], P[E[:, 1]]], 1)
            a.add_collection(LineCollection(seg, colors="0.55", linewidths=0.5 if la == "alle" else 1.0,
                                            alpha=0.35 if la == "alle" else 0.8))
            sc = a.scatter(P[:, 0], P[:, 1], c=U[c], cmap="RdBu_r", vmin=-vmax, vmax=vmax, s=70, edgecolors="k",
                           linewidths=0.6, zorder=3)
            a.scatter(P[b["quelle"], 0], P[b["quelle"], 1], marker="*", s=260, facecolors="none", edgecolors="k",
                      linewidths=1.2, zorder=4)
            a.set_aspect("equal")
            a.set_xticks([])
            a.set_yticks([])
            a.set_title(f"t = {b['zeiten'][c]}", fontsize=9)
            if c == 0:
                a.set_ylabel(f"{NAMEN[la]}\n{len(E)} Striche", fontsize=9)
        fig.colorbar(sc, ax=ax[r, :].tolist(), shrink=0.8, label="Auslenkung u")
    fig.suptitle(f"20 Zufallspunkte (Saat {b['saat']}), schraeg von der Seite gesehen; Stoss am Stern; Farbe: Auslenkung minus Mittelwert, "
                 f"Welle u'' = -L u (ungewichtet)", fontsize=11)
    fig.savefig(os.path.join(D, "bild-A-netze.png"), dpi=110)
    plt.close(fig)


def bild_A_zaehlung():
    fs = sorted(glob.glob(os.path.join(D, "teilA-b*.json")))
    if not fs:
        return
    E = {la: [] for la in NAMEN}
    ins = {la: [] for la in NAMEN}
    hist = {"alle": None, "gabriel": None}
    for f in fs:
        z = lade(f)
        for s in z["saaten"]:
            for la in NAMEN:
                E[la].append(s[la]["E"])
                ins[la].append(s[la]["inseln"])
        for la in hist:
            h = np.array(z["hist_kreuz"][la])
            hist[la] = h if hist[la] is None else hist[la] + h
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))
    for la in ("gabriel", "delaunay", "beruehrung", "wachstum"):
        ax[0].hist(E[la], bins=np.arange(0, 140, 2), alpha=0.6, label=f"{NAMEN[la]} (Mittel {np.mean(E[la]):.1f})")
    ax[0].set_xlabel("Zahl der Striche je Saat (alle Paare: 190)")
    ax[0].set_ylabel("Saaten")
    ax[0].legend(fontsize=7)
    for la, a in (("alle", ax[1]), ("gabriel", ax[2])):
        h = hist[la]
        x = np.arange(len(h))
        nz = np.nonzero(h)[0]
        a.bar(x[nz[0]:nz[-1] + 1], h[nz[0]:nz[-1] + 1], width=1.0)
        mit = float(np.sum(x * h) / np.sum(h))
        a.axvline(mit, color="k", ls="--", lw=1)
        a.set_title(f"Kreuzungen je zufaelliger Ansicht: {NAMEN[la]} (Mittel {mit:.1f})", fontsize=9)
        a.set_xlabel("Kreuzungen")
    fig.tight_layout()
    fig.savefig(os.path.join(D, "bild-A-zaehlung.png"), dpi=110)
    plt.close(fig)


def bild_B():
    reihen = [("gabriel", "ungew"), ("delaunay", "ungew"), ("delaunay", "fem"), ("beruehrung", "ungew")]
    da = [(la, fe) for la, fe in reihen if os.path.exists(os.path.join(D, f"welle-{la}-{fe}.npz"))]
    if not da:
        return
    fig, ax = plt.subplots(len(da), 3, figsize=(13, 4.3 * len(da)))
    ax = np.atleast_2d(ax)
    for r, (la, fe) in enumerate(da):
        z = np.load(os.path.join(D, f"welle-{la}-{fe}.npz"))
        j = lade(os.path.join(D, f"welle-{la}-{fe}.json"))
        xy = z["xy"]
        for c in range(3):
            a = ax[r, c]
            if f"u{c}" not in z.files:
                continue
            u = z[f"u{c}"]
            if "kanten" in z.files and len(z["kanten"]):
                K = z["kanten"]
                seg = np.stack([xy[K[:, 0]], xy[K[:, 1]]], 1)
                a.add_collection(LineCollection(seg, colors="0.6", linewidths=0.15, alpha=0.35))
            vm = np.quantile(np.abs(u), 0.995) or 1.0
            a.scatter(xy[:, 0], xy[:, 1], c=u, cmap="RdBu_r", vmin=-vm, vmax=vm, s=3, linewidths=0)
            t = (4.0, 8.0, 12.0)[c]
            th = np.linspace(0, 2 * math.pi, 200)
            a.plot(t * np.cos(th), t * np.sin(th), "k:", lw=0.6)
            a.set_aspect("equal")
            a.set_xlim(-j["N"] ** (1 / 3) / 2, j["N"] ** (1 / 3) / 2)
            a.set_ylim(-j["N"] ** (1 / 3) / 2, j["N"] ** (1 / 3) / 2)
            a.set_title(f"{NAMEN[la]}, Feld {fe}: t = {t}", fontsize=9)
    fig.suptitle("N = 50 000 Zufallspunkte im periodischen Wuerfel: Scheibe |z| < 1 um den Stosspunkt (Mitte); "
                 "gepunkteter Kreis: Radius = t (Tempo 1)", fontsize=10)
    fig.savefig(os.path.join(D, "bild-B-scheiben.png"), dpi=110)
    plt.close(fig)


def bild_B_front():
    fs = sorted(glob.glob(os.path.join(D, "welle-*.json")))
    fs = [f for f in fs if "alle" not in os.path.basename(f)]
    if not fs:
        return
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))
    for f in fs:
        j = lade(f)
        t = np.array([x["t"] for x in j["proben"][0]["reihe"]])
        R = np.mean([[x["R90"] for x in p["reihe"]] for p in j["proben"]], axis=0)
        H = np.mean([[x["H90"] for x in p["reihe"]] for p in j["proben"]], axis=0)
        lab = f"{j['lesart']}/{j['feld']}"
        ax[0].plot(t, R, label=lab)
        ax[1].plot(t, H, label=lab)
    ax[0].plot([0, 16], [0, 16], "k:", lw=0.8, label="Tempo 1")
    ax[0].set_xlabel("Zeit t")
    ax[0].set_ylabel("Frontradius R90 (90 % der Energie innerhalb), echter Abstand")
    ax[1].set_xlabel("Zeit t")
    ax[1].set_ylabel("Front in Netzschritten H90")
    ax[0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(D, "bild-B-front.png"), dpi=110)
    plt.close(fig)


def bild_C():
    fig, ax = plt.subplots(figsize=(10, 6))
    farben = {"fem": "C0", "voronoi": "C1", "ungew": "C2", "laenge": "C3", "weyl": "C4"}
    for f in sorted(glob.glob(os.path.join(D, "eigen-*.json"))):
        j = lade(f)
        for fe, d in j["felder"].items():
            k = [w["k"] for w in d["wellen"]]
            c = [w["c"] for w in d["wellen"]]
            ax.plot(k, c, "o", color=farben[fe], ms=4, alpha=0.7, label=f"{fe} (Eigenpaare)")
    for f in sorted(glob.glob(os.path.join(D, "dicht-1.json"))):
        j = lade(f)
        for key, h in j["homogen"].items():
            fe = key.split("/")[-1]
            if key.startswith("gabriel"):
                continue
            c = h["v_richt13"] if fe == "weyl" else h["c_richt13"]
            ax.errorbar([0.0], [np.mean(c)], yerr=[[np.mean(c) - np.min(c)], [np.max(c) - np.mean(c)]], fmt="s",
                        color=farben[fe], ms=6, capsize=3)
        v = j["kuerzeste"]["delaunay"]["v_mittel"]
        ax.axhline(v, color="k", ls="--", lw=1, label=f"kuerzeste Wege (Delaunay), Fronttempo {v:.3f}")
    for f in sorted(glob.glob(os.path.join(D, "weyl-1-*.json"))):
        j = lade(f)
        for lauf in j["laeufe"]:
            k = [w["k"] for w in lauf["wellen"]]
            v = [w["v"] for w in lauf["wellen"]]
            ax.plot(k, v, "^", color=farben["weyl"], ms=5, alpha=0.8, label="Weyl (KPM-Zentrum)")
    h, l = ax.get_legend_handles_labels()
    u = dict(zip(l, h))
    ax.legend(u.values(), u.keys(), fontsize=8)
    ax.axhline(1.0, color="0.5", lw=0.6)
    ax.set_xlabel("Wellenzahl k (Punktdichte 1); Quadrate bei k = 0: exakter Grenzwert (Homogenisierung)")
    ax.set_ylabel("langwelliges Tempo")
    ax.set_title("Isotacheia-Test auf einem Zufallsnetz (N = 50 000): Tempo je Feld gegen k")
    fig.tight_layout()
    fig.savefig(os.path.join(D, "bild-C-tempo.png"), dpi=110)
    plt.close(fig)


for fn in (bild_A, bild_A_zaehlung, bild_B, bild_B_front, bild_C):
    try:
        fn()
        print("ok", fn.__name__, flush=True)
    except Exception as ex:  # Bilder sind beschreibend; Fehler werden gemeldet, nicht verschwiegen
        print("FEHLER", fn.__name__, repr(ex), flush=True)
