"""KAUSAL-SWERVE-1 (Runde 37, Code-Agent fuer die Leitung claude-primary): Laeufer auf einer Poisson-Kausalmenge.

Netz wie KAUSAL-1: N Punkte gleichverteilt im kausalen Diamanten der 1+1-Raumzeit, Lichtkegelkoordinaten (u, v) in
[0,1]^2; x vor y genau dann, wenn u_x < u_y und v_x < v_y. Links per laufendem Minimum: nach u sortiert ist ein
zukuenftiger Kandidat y von x genau dann ein Link, wenn sein v kleiner ist als jedes v der Kandidaten davor.

Laeuferregel (PLAN.md, Abschnitt 2):
- Start: ein eingefuegter Punkt bei (U0, V0) = (0,05; 0,05) plus N - 1 gleichverteilte Punkte (Palm-Verteilung: der
  Startpunkt ist ein typischer Punkt der Streuung an dieser Stelle). Rapiditaet eta_0.
- Je Schritt: alle zukuenftigen Links des aktuellen Punktes; zulaessig sind die mit Eigenzeit tau = sqrt(du dv) <= tau_max
  = 3/sqrt(N). Gewaehlt wird der zulaessige Link mit kleinstem |eta_link - eta|, eta_link = (1/2) ln(dv/du); dann
  eta := eta_link.
- Ende nach 100 Schritten oder wenn kein zulaessiger Link da ist ("bis zum oberen Rand").
- Je Schritt wird notiert, ob er bulk-exakt ist: tau_max e^(eta + d) <= 1 - v und tau_max e^(-eta + d) <= 1 - u mit
  d = |eta_link - eta| (Zustand vor dem Schritt). Dann liegt jeder zulaessige Link mit |eta' - eta| < d im Diamanten,
  und der Schritt ist derselbe wie in einer unbegrenzten Streuung. Die Randregel (Ende beim ersten nicht bulk-exakten
  Schritt) wendet auswertung.py an; hier laeuft der Laeufer fuer die Kontrolle "bis zum Rand" weiter.

Aufrufe (nur ueber kleintest.sh auf der .69):
  swerve.py laeufer <N> <block> <laeufer_je_eta0> <ausgabe.npz>
  swerve.py links <N> <saat> <ausgabe.json>              KS0: Zukunftslinks je Punkt, alle Punkte und Zentrum
  swerve.py bulk <laeufer_je_eta0> <saat> <ausgabe.npz>  Kontrolle: Laeufer in einer unbegrenzten Streuung
"""
import hashlib
import json
import os
import sys
import time

import numpy as np

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
U0, V0 = 0.05, 0.05
NMAX = 100
ETA0S = (-1.0, 0.0, 1.0)
TAU_FAKTOR = 3.0  # tau_max = TAU_FAKTOR / sqrt(N)
SAAT = 20261004
GAMMA_E = 0.5772156649015329


def jetzt():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def speichern_npz(pfad, **arrays):
    tmp = pfad[:-4] + ".tmp.npz"
    np.savez_compressed(tmp, **arrays)
    os.replace(tmp, pfad)


def speichern_json(pfad, werte):
    tmp = pfad + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(werte, fh, indent=1)
    os.replace(tmp, pfad)


def zukunftslinks(u, v, i):
    """Indizes aller zukuenftigen Links von Punkt i (u aufsteigend sortiert), laufendes Minimum wie KAUSAL-1."""
    vj = v[i + 1:]
    k = np.nonzero(vj > v[i])[0]
    if k.size == 0:
        return k
    w = vj[k]
    laufmin = np.minimum.accumulate(w)
    ist = np.empty(w.size, dtype=bool)
    ist[0] = True
    ist[1:] = w[1:] < laufmin[:-1]
    return k[ist] + i + 1


def streuung_mit_start(N, rng):
    """N - 1 gleichverteilte Punkte plus Startpunkt (U0, V0); nach u sortiert. Rueckgabe u, v, Index des Startpunkts."""
    P = rng.random((N - 1, 2))
    uu = np.concatenate(([U0], P[:, 0]))
    vv = np.concatenate(([V0], P[:, 1]))
    o = np.argsort(uu, kind="stable")
    start = int(np.nonzero(o == 0)[0][0])
    return np.ascontiguousarray(uu[o]), np.ascontiguousarray(vv[o]), start


def laeufer(u, v, start, eta0, tmax):
    eta = np.full(NMAX + 1, np.nan)
    uu = np.full(NMAX + 1, np.nan)
    vv = np.full(NMAX + 1, np.nan)
    tau = np.full(NMAX + 1, np.nan)
    bulk = np.full(NMAX + 1, -1, dtype=np.int8)       # Schritt n: 1 bulk-exakt, 0 nicht, -1 kein Schritt
    nl_alle = np.full(NMAX + 1, -1, dtype=np.int32)   # Zukunftslinks am Punkt vor Schritt n (alle)
    nl_zul = np.full(NMAX + 1, -1, dtype=np.int32)    # davon mit tau <= tau_max
    eta[0], uu[0], vv[0] = eta0, u[start], v[start]
    i, e, schritte, grund = start, float(eta0), 0, 0
    for n in range(1, NMAX + 1):
        L = zukunftslinks(u, v, i)
        du = u[L] - u[i]
        dv = v[L] - v[i]
        t = np.sqrt(du * dv)
        zul = t <= tmax
        nl_alle[n] = L.size
        nl_zul[n] = int(zul.sum())
        if nl_zul[n] == 0:
            grund = 1  # kein zulaessiger Link: oberer Rand erreicht
            break
        el = 0.5 * np.log(dv[zul] / du[zul])
        j = int(np.argmin(np.abs(el - e)))
        d = abs(float(el[j]) - e)
        ist_bulk = (tmax * np.exp(e + d) <= 1.0 - v[i]) and (tmax * np.exp(-e + d) <= 1.0 - u[i])
        bulk[n] = 1 if ist_bulk else 0
        tau[n] = t[zul][j]
        i = int(L[zul][j])
        e = float(el[j])
        eta[n], uu[n], vv[n] = e, u[i], v[i]
        schritte = n
    return eta, uu, vv, tau, bulk, nl_alle, nl_zul, schritte, grund


def lauf_laeufer(N, block, anzahl, ausgabe):
    t0 = time.time()
    tmax = TAU_FAKTOR / np.sqrt(N)
    M = len(ETA0S) * anzahl
    namen = ("eta", "uu", "vv", "tau", "bulk", "nl_alle", "nl_zul")
    felder = {
        "eta": np.full((M, NMAX + 1), np.nan), "uu": np.full((M, NMAX + 1), np.nan),
        "vv": np.full((M, NMAX + 1), np.nan), "tau": np.full((M, NMAX + 1), np.nan),
        "bulk": np.full((M, NMAX + 1), -1, dtype=np.int8),
        "nl_alle": np.full((M, NMAX + 1), -1, dtype=np.int32), "nl_zul": np.full((M, NMAX + 1), -1, dtype=np.int32),
    }
    eta0 = np.full(M, np.nan)
    schritte = np.zeros(M, dtype=np.int32)
    grund = np.zeros(M, dtype=np.int8)
    fertig = np.zeros(M, dtype=bool)
    kopf = {"art": "laeufer", "N": N, "block": block, "laeufer_je_eta0": anzahl, "eta0s": list(ETA0S),
            "tau_max": float(tmax), "U0": U0, "V0": V0, "NMAX": NMAX, "skript_sha256": SKRIPT_SHA,
            "numpy": np.__version__, "start_utc": jetzt()}
    m = 0
    for ie, e0 in enumerate(ETA0S):
        for w in range(anzahl):
            rng = np.random.default_rng(np.random.SeedSequence([SAAT, 37, 1, N, block, ie, w]))
            u, v, start = streuung_mit_start(N, rng)
            r = laeufer(u, v, start, e0, tmax)
            for name, wert in zip(namen, r[:7]):
                felder[name][m] = wert
            eta0[m], schritte[m], grund[m], fertig[m] = e0, r[7], r[8], True
            m += 1
            if m % 100 == 0 or m == M:
                kopf.update({"fertig": int(fertig.sum()), "von": M, "laufzeit_s": round(time.time() - t0, 2),
                             "zeit_utc": jetzt(), "status": "fertig" if m == M else "laeuft"})
                speichern_npz(ausgabe, eta0=eta0, schritte=schritte, grund=grund, fertig=fertig, **felder)
                speichern_json(ausgabe[:-4] + ".json", kopf)
                print(json.dumps({k: kopf[k] for k in ("N", "block", "fertig", "von", "laufzeit_s", "status")}),
                      flush=True)


def erwartung_links_je_punkt(N):
    """Exakter Wert von <L>/N (KAUSAL-1/code/kausal.py, unveraendert uebernommen)."""
    from scipy import integrate
    M = N - 2

    def innen(b):
        if b <= 0.0:
            return 0.5
        y = -(M + 1) * np.log1p(-b)
        f0 = -np.expm1(-y) / ((M + 1) * b)
        zaehler = -np.expm1(-y) - np.exp(-y) * (M + 1) * b
        f1 = zaehler / ((M + 1) * (M + 2) * b * b)
        return (1.0 - b) * (f0 - f1)

    punkte = [x / N for x in (1.0, 10.0, 100.0, 1000.0) if x / N < 1.0]
    wert, fehler = integrate.quad(innen, 0.0, 1.0, points=punkte, limit=500, epsabs=0.0, epsrel=1e-12)
    return (N - 1) * wert, (N - 1) * fehler


def lauf_links(N, saat, ausgabe):
    t0 = time.time()
    tmax = TAU_FAKTOR / np.sqrt(N)
    rng = np.random.default_rng(np.random.SeedSequence([SAAT, 37, 2, N, saat]))
    P = rng.random((N, 2))
    o = np.argsort(P[:, 0], kind="stable")
    u = np.ascontiguousarray(P[o, 0])
    v = np.ascontiguousarray(P[o, 1])
    zentrum = (u > 0.4) & (u < 0.6) & (v > 0.4) & (v < 0.6)
    nz = np.zeros(N, dtype=np.int64)
    nz_lang = np.zeros(N, dtype=np.int64)  # Links mit tau > tau_max
    for i in range(N - 1):
        L = zukunftslinks(u, v, i)
        nz[i] = L.size
        if L.size:
            nz_lang[i] = int(np.count_nonzero((u[L] - u[i]) * (v[L] - v[i]) > tmax * tmax))
    H = float(np.sum(1.0 / np.arange(1, N, dtype=np.float64)))  # H_{N-1}
    c = (1.0 - u) * (1.0 - v)
    erw = H + np.log(c)  # Erwartung der Zukunftslinks am Ort (u, v), gut fuer c N >> 1 [M]
    exakt, exakt_fehler = erwartung_links_je_punkt(N)
    gross = c * N > 100.0
    werte = {
        "art": "links", "N": N, "saat": saat, "tau_max": float(tmax),
        "links_je_punkt_alle": float(nz.mean()), "links_gesamt": int(nz.sum()),
        "karte_ln_N_minus_1_42": float(np.log(N) - 1.42),
        "erwartung_exakt_L_durch_N": float(exakt), "erwartung_exakt_fehler": float(exakt_fehler),
        "zentrum_punkte": int(zentrum.sum()), "zentrum_summe": int(nz[zentrum].sum()),
        "zentrum_quadratsumme": int((nz[zentrum].astype(np.float64) ** 2).sum()),
        "zentrum_mittel": float(nz[zentrum].mean()), "zentrum_std": float(nz[zentrum].std(ddof=1)),
        "zentrum_erwartung_ortsabhaengig": float(erw[zentrum].mean()),
        "alle_cN_gross_punkte": int(gross.sum()),
        "alle_cN_gross_mittel_minus_erwartung": float((nz[gross] - erw[gross]).mean()),
        "H_N_minus_1": H,
        "anteil_links_tau_gross_alle": float(nz_lang.sum() / max(nz.sum(), 1)),
        "anteil_links_tau_gross_zentrum": float(nz_lang[zentrum].sum() / max(nz[zentrum].sum(), 1)),
        "grad_zukunft_max": int(nz.max()),
        "laufzeit_s": round(time.time() - t0, 2), "skript_sha256": SKRIPT_SHA, "numpy": np.__version__,
        "zeit_utc": jetzt(), "status": "fertig",
    }
    speichern_json(ausgabe, werte)
    print(json.dumps({k: werte[k] for k in ("N", "saat", "links_je_punkt_alle", "karte_ln_N_minus_1_42",
                                            "erwartung_exakt_L_durch_N", "zentrum_mittel",
                                            "zentrum_erwartung_ortsabhaengig", "laufzeit_s")}), flush=True)


def bulk_schritt(rng, W=8.0, XMAX=9.0):
    """Ein Schritt in einer unbegrenzten Streuung, im Ruhesystem des Laeufers (eta = 0).

    Poisson-Punkte mit Dichte 1 im Gebiet X = N du dv in [0, XMAX] (also tau <= tau_max), |eta| <= W; das Mass ist
    dX deta [M]. Links per laufendem Minimum. Fehlende Sperrpunkte mit |eta| > W betreffen nur Links nahe |eta| = W.
    Rueckgabe: eta des naechsten Links (= Aenderung der Rapiditaet), tau sqrt(N), Zahl der Links mit |eta| <= 6.
    """
    m = rng.poisson(XMAX * 2.0 * W)
    A = rng.random(m) * XMAX
    e = (2.0 * rng.random(m) - 1.0) * W
    a = np.sqrt(A) * np.exp(-e)
    b = np.sqrt(A) * np.exp(e)
    o = np.argsort(a)
    b, e, A = b[o], e[o], A[o]
    laufmin = np.minimum.accumulate(b)
    ist = np.empty(m, dtype=bool)
    ist[0] = True
    ist[1:] = b[1:] < laufmin[:-1]
    el, Al = e[ist], A[ist]
    j = int(np.argmin(np.abs(el)))
    return float(el[j]), float(np.sqrt(Al[j])), int(np.count_nonzero(np.abs(el) <= 6.0))


def lauf_bulk(anzahl, saat, ausgabe):
    t0 = time.time()
    rng = np.random.default_rng(np.random.SeedSequence([SAAT, 37, 3, saat]))
    M = len(ETA0S) * anzahl
    deta = np.zeros((M, NMAX))
    taus = np.zeros((M, NMAX))
    nl6 = np.zeros((M, NMAX), dtype=np.int32)
    eta0 = np.repeat(np.array(ETA0S), anzahl)
    for m in range(M):
        for k in range(NMAX):
            deta[m, k], taus[m, k], nl6[m, k] = bulk_schritt(rng)
    eta = np.concatenate((eta0[:, None], eta0[:, None] + np.cumsum(deta, axis=1)), axis=1)
    speichern_npz(ausgabe, eta0=eta0, eta=eta, deta=deta, tau_sqrtN=taus, nl6=nl6)
    kopf = {"art": "bulk", "saat": saat, "laeufer_je_eta0": anzahl, "NMAX": NMAX, "skript_sha256": SKRIPT_SHA,
            "numpy": np.__version__, "laufzeit_s": round(time.time() - t0, 2), "zeit_utc": jetzt(),
            "status": "fertig", "deta_mittel": float(deta.mean()), "deta_quadrat_mittel": float((deta ** 2).mean()),
            "deta_betrag_mittel": float(np.abs(deta).mean()), "cosh_deta_mittel": float(np.cosh(deta).mean()),
            "links_je_rapiditaetseinheit": float(nl6.mean() / 12.0), "tau_sqrtN_mittel": float(taus.mean())}
    speichern_json(ausgabe[:-4] + ".json", kopf)
    print(json.dumps(kopf), flush=True)


def lauf_spiegel(N, anzahl, ausgabe):
    """Codeprobe: dieselbe Streuung mit u <-> v gespiegelt und eta_0 -> -eta_0 muss eta -> -eta geben, gleiche Kennzeichen."""
    t0 = time.time()
    tmax = TAU_FAKTOR / np.sqrt(N)
    groesste, kennz_gleich, schritte_gleich = 0.0, 0, 0
    for w in range(anzahl):
        rng = np.random.default_rng(np.random.SeedSequence([SAAT, 37, 4, N, w]))
        u, v, start = streuung_mit_start(N, rng)
        e0 = 0.7
        a = laeufer(u, v, start, e0, tmax)
        o = np.argsort(v, kind="stable")
        b = laeufer(np.ascontiguousarray(v[o]), np.ascontiguousarray(u[o]), int(np.nonzero(o == start)[0][0]), -e0,
                    tmax)
        s = np.isfinite(a[0]) & np.isfinite(b[0])
        groesste = max(groesste, float(np.max(np.abs(a[0][s] + b[0][s]))))
        kennz_gleich += int(np.array_equal(a[4], b[4]))
        schritte_gleich += int(a[7] == b[7])
    werte = {"art": "spiegel", "N": N, "anzahl": anzahl, "groesste_abweichung_eta_plus_eta_gespiegelt": groesste,
             "kennzeichen_gleich": kennz_gleich, "schritte_gleich": schritte_gleich,
             "laufzeit_s": round(time.time() - t0, 2), "skript_sha256": SKRIPT_SHA, "zeit_utc": jetzt(),
             "status": "fertig"}
    speichern_json(ausgabe, werte)
    print(json.dumps(werte), flush=True)


def main():
    art = sys.argv[1]
    if art == "spiegel":
        lauf_spiegel(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    elif art == "laeufer":
        lauf_laeufer(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
    elif art == "links":
        lauf_links(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    elif art == "bulk":
        lauf_bulk(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    else:
        raise SystemExit("unbekannte Art: " + art)


if __name__ == "__main__":
    main()
