#!/usr/bin/env python3
"""URSUPPE-1 (Runde 22), Leitung claude-primary, 02.10.2026. Karte: RUNDE-22/ursuppe-1/KARTE.md.

Graph-Suppe: N Knoten, Start zufaelliger z-regulaerer Graph (Paarungsmodell mit Wiederholung), gradgleiche
Doppelkanten-Tausche (a-b, c-d) -> (a-c, b-d) oder (a-d, b-c), Metropolis mit geometrisch sinkender Temperatur.
Energien (t_e = Zahl der Dreiecke an Kante e):
  E0   = 0                      (Kontrolle: keine Tausche, zufaelliger Graph)
  tri  = - Sum_e t_e            (moeglichst viele Dreiecke)
  man  = Sum_e (t_e - 2)^2      (Flaechenregel: jede Kante in genau zwei Dreiecken)
Messgroessen: Komponenten, mittlerer Clusterkoeffizient, Anteil t_e = 2, spektrale Dimension aus den Eigenwerten des
kombinatorischen Laplace-Operators: d_s(t) = 2 t Sum l e^(-l t) / Sum e^(-l t); Plateau = Fenster [t, 4t] mit kleinster
relativer Schwankung vor der Endlichkeitszeit (P(t) = Sum e^(-l t)/N > 2 c/N, c = Zahl der Komponenten).
Aufruf: python ursuppe.py <art: E0|tri|man|gitter|zufall> <N> <z> <saat> <tausche> <T0> <T1> <aus.json>
  'gitter' = Dreiecksgitter auf dem Torus (N = n^2, z = 6) als Kontrolle K0; 'zufall' = zufaelliger z-regulaerer Graph.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json
import math
import random
import sys
import time

import numpy as np


def zufall_regulaer(N, z, rng, mischen_je_knoten=100):
    """Zirkulanter Ring C_N(1..z/2) (einfach, z-regulaer), dann durch gueltige gradgleiche Doppelkanten-Tausche gemischt
    (Standard-MCMC fuer zufaellige regulaere Graphen); mischen_je_knoten * N Tauschversuche."""
    if z % 2:
        raise ValueError("z gerade")
    adj = [set() for _ in range(N)]
    for v in range(N):
        for s in range(1, z // 2 + 1):
            w = (v + s) % N
            adj[v].add(w)
            adj[w].add(v)
    klist = kanten(adj)
    pos = {k: i for i, k in enumerate(klist)}
    for _ in range(mischen_je_knoten * N):
        (a, b), (c, d) = klist[rng.randrange(len(klist))], klist[rng.randrange(len(klist))]
        if len({a, b, c, d}) < 4:
            continue
        if rng.random() < 0.5:
            c, d = d, c
        if c in adj[a] or d in adj[b]:
            continue
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(c); adj[c].add(a); adj[b].add(d); adj[d].add(b)
        for ka, kn in (((a, b), (a, c)), ((c, d), (b, d))):
            ka, kn = (min(ka), max(ka)), (min(kn), max(kn))
            i = pos.pop(ka)
            klist[i] = kn
            pos[kn] = i
    return adj


def dreiecksgitter_torus(n):
    N = n * n
    adj = [set() for _ in range(N)]

    def vid(i, j):
        return (i % n) * n + (j % n)

    for i in range(n):
        for j in range(n):
            for di, dj in ((1, 0), (0, 1), (-1, 1)):
                a, b = vid(i, j), vid(i + di, j + dj)
                adj[a].add(b)
                adj[b].add(a)
    return adj


def kanten(adj):
    return [(a, b) for a in range(len(adj)) for b in adj[a] if a < b]


def t_kante(adj, a, b):
    return len(adj[a] & adj[b])


def e_beitrag(art, t):
    if art == "tri":
        return -t
    if art == "man":
        return (t - 2) ** 2
    return 0


def betroffene(adj, kantenliste):
    """Kanten, deren t sich durch Entfernen bzw. Hinzufuegen der Kanten in kantenliste aendern kann."""
    s = set()
    for a, b in kantenliste:
        s.add((min(a, b), max(a, b)))
        for x in adj[a] & adj[b]:
            s.add((min(a, x), max(a, x)))
            s.add((min(b, x), max(b, x)))
    return s


def anneal(adj, art, tausche, T0, T1, rng):
    E_liste = kanten(adj)
    kset = set(E_liste)
    klist = list(E_liste)
    pos = {k: i for i, k in enumerate(klist)}
    E = sum(e_beitrag(art, t_kante(adj, a, b)) for a, b in klist)
    angenommen = 0
    verlauf = []
    for n in range(tausche):
        T = T0 * (T1 / T0) ** (n / max(1, tausche - 1))
        (a, b), (c, d) = klist[rng.randrange(len(klist))], klist[rng.randrange(len(klist))]
        if len({a, b, c, d}) < 4:
            continue
        if rng.random() < 0.5:
            c, d = d, c
        # neu: (a, c), (b, d)
        if c in adj[a] or d in adj[b]:
            continue
        alt = [(a, b), (c, d)]
        neu = [(a, c), (b, d)]
        vorher = betroffene(adj, alt)
        e_vor = sum(e_beitrag(art, t_kante(adj, x, y)) for x, y in vorher)
        # tentativ anwenden
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(c); adj[c].add(a); adj[b].add(d); adj[d].add(b)
        nachher = betroffene(adj, neu)
        # Kanten aus 'vorher', die noch existieren, plus die neuen betroffenen
        alle = {k for k in vorher if k[1] in adj[k[0]]} | nachher
        e_nach = sum(e_beitrag(art, t_kante(adj, x, y)) for x, y in alle)
        # vorher-Summe muss dieselbe Kantenmenge abdecken: fehlende Kanten aus 'nachher' vorher bewerten
        dE = e_nach - e_vor
        zus = [k for k in nachher if k not in vorher and k not in ((min(a, c), max(a, c)), (min(b, d), max(b, d)))]
        if zus:
            # deren Beitrag vor dem Tausch: tentativ zuruecksetzen, messen, wieder anwenden
            adj[a].discard(c); adj[c].discard(a); adj[b].discard(d); adj[d].discard(b)
            adj[a].add(b); adj[b].add(a); adj[c].add(d); adj[d].add(c)
            e_zus_vor = sum(e_beitrag(art, t_kante(adj, x, y)) for x, y in zus)
            adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
            adj[a].add(c); adj[c].add(a); adj[b].add(d); adj[d].add(b)
            dE -= e_zus_vor
        if dE <= 0 or rng.random() < math.exp(-dE / T):
            E += dE
            angenommen += 1
            for k_alt, k_neu in zip(alt, neu):
                ka = (min(k_alt), max(k_alt))
                kn = (min(k_neu), max(k_neu))
                i = pos.pop(ka)
                klist[i] = kn
                pos[kn] = i
                kset.discard(ka)
                kset.add(kn)
        else:
            adj[a].discard(c); adj[c].discard(a); adj[b].discard(d); adj[d].discard(b)
            adj[a].add(b); adj[b].add(a); adj[c].add(d); adj[d].add(c)
        if n % max(1, tausche // 20) == 0:
            verlauf.append({"n": n, "T": T, "E": E})
    E_kontrolle = sum(e_beitrag(art, t_kante(adj, a, b)) for a, b in kanten(adj))
    return {"E_ende": E, "E_kontrolle": E_kontrolle, "angenommen": angenommen, "verlauf": verlauf}


def messen(adj):
    N = len(adj)
    # Komponenten
    gesehen = [False] * N
    komp = []
    for s in range(N):
        if not gesehen[s]:
            stapel, groesse = [s], 0
            gesehen[s] = True
            while stapel:
                v = stapel.pop()
                groesse += 1
                for w in adj[v]:
                    if not gesehen[w]:
                        gesehen[w] = True
                        stapel.append(w)
            komp.append(groesse)
    cl = []
    for v in range(N):
        k = len(adj[v])
        if k >= 2:
            nb = list(adj[v])
            links = sum(1 for i in range(k) for j in range(i + 1, k) if nb[j] in adj[nb[i]])
            cl.append(2.0 * links / (k * (k - 1)))
    ts = [t_kante(adj, a, b) for a, b in kanten(adj)]
    A = np.zeros((N, N))
    for a in range(N):
        for b in adj[a]:
            A[a, b] = 1.0
    L = np.diag(A.sum(1)) - A
    lam = np.linalg.eigvalsh(L)
    lam = np.clip(lam, 0.0, None)
    c = len(komp)
    tg = np.logspace(-1, 4, 400)
    w = np.exp(-np.outer(tg, lam))
    P = w.sum(1) / N
    ds = 2.0 * tg * (w * lam).sum(1) / w.sum(1)
    gut = P > 2.0 * c / N
    best = None
    for i in range(len(tg)):
        if not gut[i] or tg[i] < 0.5:
            continue
        j = np.searchsorted(tg, 4.0 * tg[i])
        if j >= len(tg) or not gut[j]:
            continue
        seg = ds[i:j + 1]
        var = float((seg.max() - seg.min()) / seg.mean())
        if best is None or var < best["schwankung"]:
            best = {"t0": float(tg[i]), "t1": float(tg[j]), "d_s": float(seg.mean()), "schwankung": var}
    return {"komponenten": c, "groessen": sorted(komp, reverse=True)[:5], "cluster": float(np.mean(cl)) if cl else 0.0,
            "anteil_t2": float(np.mean([t == 2 for t in ts])), "t_mittel": float(np.mean(ts)),
            "t_histogramm": {str(k): int(sum(1 for t in ts if t == k)) for k in range(0, 12)},
            "plateau": best, "plateau_ja": bool(best is not None and best["schwankung"] < 0.2),
            "d_s_kurve": {"t": tg[::10].tolist(), "d_s": ds[::10].tolist(), "P": P[::10].tolist()},
            "lambda_2": float(np.sort(lam)[min(c, N - 1)])}


def main():
    art, N, z, saat, tausche, T0, T1, pfad = (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),
                                              int(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), sys.argv[8])
    t_start = time.time()
    rng = random.Random(saat)
    out = {"art": art, "N": N, "z": z, "saat": saat, "tausche": tausche, "T0": T0, "T1": T1}
    if art == "gitter":
        n = int(round(math.sqrt(N)))
        adj = dreiecksgitter_torus(n)
        out["N"] = n * n
    else:
        adj = zufall_regulaer(N, z, rng)
        if art in ("tri", "man"):
            out["anneal"] = anneal(adj, art, tausche, T0, T1, rng)
    out["mess"] = messen(adj)
    out["grade_konstant"] = bool(all(len(s) == z for s in adj)) if art != "gitter" else True
    out["sek"] = time.time() - t_start
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    m = out["mess"]
    print(f"ursuppe fertig: {art} z={z} saat={saat}: komp {m['komponenten']}, cluster {m['cluster']:.3f}, "
          f"t2 {m['anteil_t2']:.3f}, plateau {m['plateau']}, {out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
