#!/usr/bin/env python3
"""WEYL-LINEAR-1 (Runde 42, Code-Agent fuer claude-primary): beide Aeste der Weyl-Dispersion auf periodischen
Poisson-Delaunay-Netzen. Netz und Operator unveraendert aus spinnetz.py (SPIN-ZUFALLSNETZ-1/STRICH-NETZ-1,
sha256 460c0af6...). Die Zentrumsbestimmung ist eine woertliche Kopie aus strichnetz.weyl_zentren (STRICH-NETZ-1):
  Jackson-KPM-Dichte der ebenen Welle, Maximum auf [0,3 k; 1,7 k] (3001 Punkte), Fenster +-4 sigma_E
  (sigma_E = pi a/M) um das Maximum, Schwerpunkt im Fenster (1601 Punkte, Trapez).
Ast "plus" (E > 0): Helizitaet sigma.k^ = -1 (U[:, 0], wie STRICH-NETZ-1).
Ast "minus" (E < 0): Helizitaet +1 (U[:, 1]); Momente gespiegelt mu_n -> (-1)^n mu_n (Dichte von -H), danach
  dieselbe Routine. Berichtet wird |E|. Damit ist der Schaetzer exakt spiegelsymmetrisch.
Wellen: m = 0, Verdrillung theta = k L e (e Achse), also k_vec = k e.

Aufruf (nur ueber kleintest.sh auf der .69):
  python weyllinear.py zweig <N> <saaten,komma> <M> <k-liste,komma> <richtungen, z. B. xyz> <aus.json> [a=<feste Skala>]
     Ein k-Eintrag "t0.8" heisst theta = 0,8 (k = 0,8/L).
  python weyllinear.py kontrolle <aus.json> <M> <L_gitter> <k-liste,komma> [a=<feste Skala>]
"""
import json
import math
import os
import resource
import sys
import time

import numpy as np
import scipy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import spinnetz as sz  # noqa: E402  (unveraendert, sha256 460c0af6...)

RICHT = {"x": np.array([1.0, 0.0, 0.0]), "y": np.array([0.0, 1.0, 0.0]), "z": np.array([0.0, 0.0, 1.0]),
         "d": np.ones(3) / math.sqrt(3.0)}
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
js = sz.js


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def speichern(ziel, out):
    tmp = ziel + ".tmp"
    with open(tmp, "w") as f:
        json.dump(js(out), f)
    os.replace(tmp, ziel)


def zentrum(spalte, a, kb, MM):
    """Kopie aus strichnetz.weyl_zentren (Schleifenrumpf fuer ein MM), fuer eine Momentenspalte (Ast E > 0)."""
    g = sz.jackson(MM)
    mu = np.asarray(spalte[:MM], dtype=float)[:, None]
    Eg = np.linspace(0.3 * kb, 1.7 * kb, 3001)
    rho = sz.kpm_dichte(mu, g, a, Eg)[:, 0]
    Em = float(Eg[np.argmax(rho)])
    sE = math.pi * a / MM
    Ew = np.linspace(max(Em - 4 * sE, 1e-6), Em + 4 * sE, 1601)
    rw = sz.kpm_dichte(mu, g, a, Ew)[:, 0]
    W = float(np.trapezoid(rw, Ew))
    return {"E_max": Em, "E_zentrum": float(np.trapezoid(rw * Ew, Ew) / W), "gewicht_fenster": W, "sigma_E": sE}


def wellen_paar(snz, kvec, M, a_fest=None):
    """Beide Helizitaeten der ebenen Welle k_vec (m = 0, theta = k_vec L) in einem KPM-Block."""
    t0 = time.time()
    N, L = snz["N"], snz["L"]
    kvec = np.asarray(kvec, dtype=float)
    th = kvec * L
    H = sz.matrix(snz, th)
    sch = sz.schranke(H)
    a = sch["a"]
    a_fest_ok = None
    if a_fest is not None:
        # feste Skala fuer alle N (gleiche Aufloesung sigma_E = pi a/M); nur zulaessig, wenn sie das Spektrum umfasst
        a_fest_ok = bool(sch["lanczos_ok"] and a_fest >= 1.02 * sch["lanczos_max_betrag"])
        if a_fest_ok:
            a = float(a_fest)
    sq = np.sqrt(snz["V"] / snz["V"].sum())
    kb = float(np.linalg.norm(kvec))
    kh = kvec / kb
    S = kh[0] * SX + kh[1] * SY + kh[2] * SZ
    ew, U = np.linalg.eigh(S)          # ew = (-1, +1)
    ph = sq * np.exp(1j * (snz["pos"] @ kvec))
    Vb = np.zeros((2 * N, 2), dtype=complex)
    for q in range(2):
        Vb[0::2, q] = ph * U[0, q]
        Vb[1::2, q] = ph * U[1, q]
    t1 = time.time()
    mu = sz.kpm_block(H * (1.0 / a), Vb, M)
    t_kpm = time.time() - t1
    vz = (-1.0) ** np.arange(M)
    aeste = {}
    for ast, spalte, hel in (("plus", mu[:, 0], int(round(ew[0]))), ("minus", mu[:, 1] * vz, int(round(ew[1])))):
        z = {MM: zentrum(spalte, a, kb, MM) for MM in (M, M // 2)}
        aeste[ast] = {"helizitaet": hel, "E_betrag_zentrum": z[M]["E_zentrum"], "v": z[M]["E_zentrum"] / kb,
                      "v_halbM": z[M // 2]["E_zentrum"] / kb, "v_max": z[M]["E_max"] / kb,
                      "gewicht_fenster": z[M]["gewicht_fenster"], "gewicht_fenster_halbM": z[M // 2]["gewicht_fenster"],
                      "sigma_E": z[M]["sigma_E"], "erstes_moment_betrag": float(spalte[1] * a)}
    return {"k": kb, "k_vec": kvec, "theta": th, "a": a, "a_fest": a_fest, "a_fest_ok": a_fest_ok, "schranke": sch, "M": M,
            "mu_max": float(np.max(np.abs(mu))), "sek_kpm": t_kpm, "sek": time.time() - t0, "aeste": aeste}


def k_vektor(eintrag, L, e):
    if eintrag.startswith("t"):
        return float(eintrag[1:]) / L * e
    return float(eintrag) * e


def modus_zweig(N, saaten, M, kliste, richtungen, protokoll, a_fest=None):
    out = {"N": N, "M": M, "kliste": kliste, "richtungen": richtungen, "a_fest": a_fest, "saaten": []}
    for saat in saaten:
        t0 = time.time()
        snz = sz.zufallsnetz(N, saat)
        pr = snz["pruefung"]
        protokoll(f"Netz N={N} saat={saat}: L={snz['L']:.4f}, E={pr['E']}, euler {pr['euler']}, "
                  f"{time.time() - t0:.1f} s, RSS {rss_mb():.0f} MB")
        wellen = []
        for r in richtungen:
            e = RICHT[r]
            for kk in kliste:
                w = wellen_paar(snz, k_vektor(kk, snz["L"], e), M, a_fest)
                w["richtung"] = r
                w["k_eintrag"] = kk
                wellen.append(w)
                protokoll(f"  saat {saat} {r} k={w['k']:.5f}: a={w['a']:.3f} (fest ok {w['a_fest_ok']}, Lanczos "
                          f"{w['schranke']['lanczos_max_betrag']:.3f}), KPM {w['sek_kpm']:.1f} s, Gewicht "
                          f"{w['aeste']['plus']['gewicht_fenster']:.3f}/{w['aeste']['minus']['gewicht_fenster']:.3f}, "
                          f"|mu|max {w['mu_max']:.6f}")
        out["saaten"].append({"saat": saat, "L": snz["L"], "pruefung": pr, "wellen": wellen,
                              "sek": time.time() - t0})
    return out


def modus_kontrolle(M, Lg, kliste, protokoll, a_fest=None):
    gz = sz.gitternetz(Lg)
    erg = []
    for kk in kliste:
        kvec = k_vektor(kk, float(Lg), RICHT["x"])
        w = wellen_paar(gz, kvec, M, a_fest)
        Eex = float(np.sqrt(np.sum(np.sin(kvec) ** 2)))
        p, m = w["aeste"]["plus"]["E_betrag_zentrum"], w["aeste"]["minus"]["E_betrag_zentrum"]
        w.update({"E_exakt": Eex, "abw_plus": p - Eex, "abw_minus": m - Eex, "plus_minus": p - m})
        erg.append(w)
        protokoll(f"Gitter L={Lg} k={w['k']:.4f}: abw plus {p - Eex:.2e}, minus {m - Eex:.2e}, plus-minus {p - m:.2e}")
    return {"gitter_L": Lg, "M": M, "wellen": erg,
            "max_abw": float(max(max(abs(x["abw_plus"]), abs(x["abw_minus"])) for x in erg)),
            "max_plus_minus": float(max(abs(x["plus_minus"]) for x in erg))}


def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    out = {"modus": modus, "argv": sys.argv[1:], "numpy": np.__version__, "scipy": scipy.__version__}
    opts = {x.split("=")[0]: x.split("=")[1] for x in sys.argv[2:] if "=" in x}
    pos = [x for x in sys.argv[2:] if "=" not in x]
    a_fest = float(opts["a"]) if "a" in opts else None
    if modus == "zweig":
        N = int(pos[0])
        saaten = [int(x) for x in pos[1].split(",")]
        M = int(pos[2])
        kliste = pos[3].split(",")
        richtungen = list(pos[4])
        ziel = pos[5]
        out.update(modus_zweig(N, saaten, M, kliste, richtungen, protokoll, a_fest))
    elif modus == "kontrolle":
        ziel = pos[0]
        out.update(modus_kontrolle(int(pos[1]), int(pos[2]), pos[3].split(","), protokoll, a_fest))
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["rss_mb"] = rss_mb()
    out["protokoll"] = log
    speichern(ziel, out)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s, RSS {rss_mb():.0f} MB", flush=True)


if __name__ == "__main__":
    main()
