"""KAUSAL-1 (Runde 37, Leitung claude-primary): Links einer Poisson-Kausalmenge im kausalen Diamanten der 1+1-Raumzeit.

Lichtkegelkoordinaten (u, v) in [0,1]^2; x vor y genau dann, wenn u_x < u_y und v_x < v_y. Ein Link ist ein Paar x vor y
ohne Punkt dazwischen. Nach u sortiert ist ein zukuenftiger Kandidat y von x genau dann ein Link, wenn sein v kleiner ist
als jedes v der Kandidaten davor (laufendes Minimum).

Aufruf (nur ueber kleintest.sh auf der .69): kausal.py <N> <saat> <ausgabe.json>
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy import integrate

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
ETA_KANTEN = np.arange(-4.0, 4.0 + 1e-9, 0.25)
GAMMA_E = 0.5772156649015329


def erwartung_links_je_punkt(N):
    """Exakter Wert von <L>/N = (N - 1) int_0^1 int_0^1 (1-a)(1-b)(1-ab)^(N-2) da db, innere Integrale analytisch."""
    M = N - 2

    def innen(b):
        if b <= 0.0:
            return 0.5  # Grenzwert von F0 - F1 fuer b -> 0
        y = -(M + 1) * np.log1p(-b)
        f0 = -np.expm1(-y) / ((M + 1) * b)
        zaehler = -np.expm1(-y) - np.exp(-y) * (M + 1) * b
        f1 = zaehler / ((M + 1) * (M + 2) * b * b)
        return (1.0 - b) * (f0 - f1)

    punkte = [x / N for x in (1.0, 10.0, 100.0, 1000.0) if x / N < 1.0]
    wert, fehler = integrate.quad(innen, 0.0, 1.0, points=punkte, limit=500, epsabs=0.0, epsrel=1e-12)
    return (N - 1) * wert, (N - 1) * fehler


def main():
    N, saat, ausgabe = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    t0 = time.time()
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 37, N, saat]))
    P = rng.random((N, 2))
    ordnung = np.argsort(P[:, 0])
    u = P[ordnung, 0]
    v = P[ordnung, 1]
    zentrum = (u > 0.4) & (u < 0.6) & (v > 0.4) & (v < 0.6)
    relationen = 0
    links = 0
    grad = np.zeros(N, dtype=np.int64)
    etas = []
    for i in range(N - 1):
        vj = v[i + 1:]
        zuk = vj > v[i]
        nz = int(zuk.sum())
        relationen += nz
        if nz == 0:
            continue
        w = vj[zuk]
        laufmin = np.minimum.accumulate(w)
        ist_link = np.empty(w.size, dtype=bool)
        ist_link[0] = True
        ist_link[1:] = w[1:] < laufmin[:-1]
        stellen = np.nonzero(zuk)[0][ist_link] + i + 1
        links += int(ist_link.sum())
        grad[i] += int(ist_link.sum())
        grad[stellen] += 1
        if zentrum[i]:
            du = u[stellen] - u[i]
            dv = v[stellen] - v[i]
            etas.append(0.5 * np.log(dv / du))
    etas = np.concatenate(etas) if etas else np.zeros(0)
    nzent = int(zentrum.sum())
    hist, _ = np.histogram(etas, bins=ETA_KANTEN)
    dichte = (hist / (nzent * 0.25)).tolist() if nzent else []
    exakt, exakt_fehler = erwartung_links_je_punkt(N)
    werte = {
        "N": N, "saat": saat,
        "relationen_anteil": relationen / (N * (N - 1) / 2.0),
        "links": links, "links_je_punkt": links / N,
        "erwartung_asymptotisch": float(np.log(N) + GAMMA_E - 2.0),
        "erwartung_exakt": float(exakt), "erwartung_exakt_fehler": float(exakt_fehler),
        "grad_mittel": float(grad.mean()), "grad_max": int(grad.max()),
        "zentrum_punkte": nzent, "zentrum_links": int(etas.size),
        "eta_kanten": ETA_KANTEN.tolist(), "eta_dichte_je_einheit": dichte,
        "laufzeit_s": round(time.time() - t0, 2),
        "skript_sha256": SKRIPT_SHA, "numpy": np.__version__,
        "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    with open(ausgabe, "w") as fh:
        json.dump(werte, fh, indent=1)
    print(json.dumps({k: werte[k] for k in ("N", "saat", "relationen_anteil", "links_je_punkt", "erwartung_asymptotisch",
                                            "erwartung_exakt", "grad_max", "zentrum_punkte", "laufzeit_s")}))


if __name__ == "__main__":
    main()
