"""Runde 9, Karte ABSTAND (Finn 07:10): Welches Gesetz haben die Abstaende der stillen Stellen?

Eingabe: omega*^2-Folgen je beta aus RUNDE-07.md und RUNDE-08.md (exakt-Fits bzw. kurve-Feinwerte; beta 0,5 n = 6 aus kurve,
n = 8 aus dem Breitenminimum der Polsuche). Keine neue Physikrechnung, nur Anpassung von sechs Gesetzen mit je zwei freien
Parametern (kleinste Quadrate) und Vergleich der Reste in omega^2. Laeuft in Sekundenbruchteilen.
"""
import json
import math

import numpy as np

DATEN = {
    0.35: {1: 0.621873, 2: 0.476457, 3: 0.416453, 4: 0.384751},
    0.40: {1: 0.699702, 2: 0.566347, 3: 0.508114},
    0.45: {1: 0.755738, 2: 0.633380, 3: 0.577365},
    0.50: {1: 0.797677, 2: 0.685129, 3: 0.631449, 4: 0.601422, 5: 0.582417, 6: 0.569400, 8: 0.552600},
    0.55: {1: 0.829984, 2: 0.726130, 3: 0.674782, 4: 0.645620, 5: 0.627042},
    0.60: {1: 0.855443, 2: 0.759294, 3: 0.710164, 4: 0.681916, 5: 0.663791},
}
PRIM = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def xmin(beta):
    return 1.0 - 1.0 / (4.0 * beta)


def anpassen(beta, werte):
    n = np.array(sorted(werte), dtype=float)
    x = np.array([werte[int(k)] for k in n])
    x0 = xmin(beta)
    y = x - x0
    erg = {}

    def lin(u, v):
        """v = a + b u, kleinste Quadrate; gibt (a, b)."""
        A = np.vstack([np.ones_like(u), u]).T
        return np.linalg.lstsq(A, v, rcond=None)[0]

    def rest(xfit):
        return float(np.sqrt(np.mean((xfit - x) ** 2))), float(np.max(np.abs(xfit - x)))

    a, b = lin(n, x)
    erg["linear"] = {"a": a, "b": b, "rms_max": rest(a + b * n)}
    a, b = lin(n, np.log(y))
    erg["exponentiell"] = {"A": math.exp(a), "r": math.exp(b), "rms_max": rest(x0 + np.exp(a + b * n))}
    a, b = lin(np.log(n), x)
    erg["logarithmisch"] = {"a": a, "b": b, "rms_max": rest(a + b * np.log(n))}
    a, b = lin(np.log(n), np.log(y))
    erg["potenz"] = {"A": math.exp(a), "p": b, "rms_max": rest(x0 + np.exp(a) * n ** b)}
    a, b = lin(n, 1.0 / y)
    erg["kehrwert"] = {"a": a, "b": b, "rms_max": rest(x0 + 1.0 / (a + b * n))}
    p = np.array([PRIM[int(k) - 1] for k in n], dtype=float)
    a, b = lin(p, 1.0 / y)
    erg["primzahlen"] = {"a": a, "b": b, "rms_max": rest(x0 + 1.0 / (a + b * p))}
    # Faktor zwischen Nachbarn und Schritte im Kehrwert
    faktoren = [float(y[i] / y[i + 1]) for i in range(len(y) - 1)]
    schritte = [float(1.0 / y[i + 1] - 1.0 / y[i]) / (n[i + 1] - n[i]) for i in range(len(y) - 1)]
    return {"beta": beta, "x_min": x0, "n": n.tolist(), "x": x.tolist(), "gesetze": erg,
            "faktor_nachbarn": faktoren, "kehrwert_schritt_je_n": schritte}


def main():
    alle = [anpassen(b, w) for b, w in DATEN.items()]
    namen = ["linear", "exponentiell", "logarithmisch", "potenz", "kehrwert", "primzahlen"]
    print("RMS-Rest in omega^2 je Gesetz (2 freie Parameter; x_min = 1 - 1/(4 beta) fest):")
    print("beta | Punkte | " + " | ".join(namen))
    for e in alle:
        print(f"{e['beta']:.2f} | {len(e['n'])} | " + " | ".join(f"{e['gesetze'][g]['rms_max'][0]:.2e}" for g in namen))
    print()
    print("Potenzgesetz-Exponent p und Kehrwert-Schritt b je beta:")
    for e in alle:
        print(f"  beta {e['beta']:.2f}: p = {e['gesetze']['potenz']['p']:.3f}, b = {e['gesetze']['kehrwert']['b']:.3f}, "
              f"a = {e['gesetze']['kehrwert']['a']:.3f}")
    print()
    print("Faktor zwischen Nachbarn (x_n - x_min)/(x_n+1 - x_min) und Kehrwert-Schritt je n:")
    for e in alle:
        print(f"  beta {e['beta']:.2f}: Faktoren " + ", ".join(f"{f:.4f}" for f in e["faktor_nachbarn"])
              + " | Schritte " + ", ".join(f"{s:.3f}" for s in e["kehrwert_schritt_je_n"]))
    with open("abstand_ergebnis.json", "w") as fh:
        json.dump(alle, fh, indent=1, default=float)


if __name__ == "__main__":
    main()
