# REGGE-ZEIT-1: Ruhende Masse im 4D-Laengennetz mit Zeitkanten: Newton und der Lichtablenkungsfaktor gamma (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 03:01:28 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - RUNDE-37/RAUMZEIT-NETZ.md, Karte 1. Bisher ist im Laengenbild nur der raeumliche, zeitsymmetrische Teil gerechnet
    (REGGE-RAND-1, REGGE-SCHAUM-1: psi = 1 + GM/(2r)).
  - REGGE-4D-1 zeigt die Spin-2-Struktur, aber ohne Materie.
  - Offen: Koppelt eine Masse ueber die Zeitkanten (h_00) und gibt das Netz Einsteins Lichtablenkung, also gamma = 1
    (doppelt so stark wie nur Newton)?
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.
- **Ehrlich vorab:** REGGE-4D-1 zeigt fuer lange Wellen Einsteins linearisierte Wirkung auf 0,04 %. Damit ist gamma = 1
  im Kontinuumsgrenzfall weitgehend vorab ableitbar [L/M]. Neu ist die Gitterumsetzung mit einer Weltlinie auf
  Zeitkanten.

## Schreibtisch (vor jeder Rechnung)

- **Netz:** 4D-Kuhn-Gitter wie REGGE-4D-1, euklidisch, eine Achse als Zeit tau.
  - Statisch heisst k_tau = 0: Zeitraeumlich periodisch, alle Zeitschichten gleich.
  - Raeumlich Torus L^3 mit Groessenreihe bzw. Torus-Korrektur wie TENSOR-EIS-N, LAST-1 und REGGE-RAND-1.
- **Materie:** Punktmasse M auf einer Weltlinie entlang tau. Ihre Wirkung ist M mal Eigenzeit, also M mal die Summe der
  Laengen ihrer Zeitkanten.
  - Die Quelle wirkt also nur auf diese Kanten. Das ist die Energiekopplung ueber h_00 [M].
  - Gesamtwirkung S = -(1/(8 pi G)) sum_t A_t eps_t + M sum_Weltlinie l_e (euklidisch; Vorzeichen und Normierung vor
    der Rechnung am Kontinuum festlegen).
- **Loesung:** linear, im Fourierraum bei k_tau = 0 mit M(k) aus REGGE-4D-1.
  - Pseudoinverse auf dem Nicht-Nullraum (4 Eichmoden + Diagonalmode).
  - Die Quelle muss auf dem Nullraum verschwinden (Erhaltung) [M]; pruefen.
- **Messgroessen** (eichunabhaengig): Fehlwinkel delta eps_t der Dreiecke. In Punkten auf der x-Achse (und auf einer
  Diagonale) vergleichen:
  - Dreiecke in der (tau, x)-Ebene ~ R_tauxtaux = d_x d_x Phi
  - Dreiecke in der (y, z)-Ebene ~ R_yzyz = -2 gamma G M/r^3 (linearisiertes Schwarzschild, isotrop [L/M])
  - Auf der x-Achse ist das Verhaeltnis R_yzyz/R_tauxtaux = gamma [M].
  - Beide Dreieckstypen sind unter Achsenvertauschung kongruent (Kuhn-Symmetrie); das ist vor der Rechnung zu pruefen.
    Sonst ueber eine Eichung mit bekannter Kruemmung kalibrieren (glatte Stoerung h mit konstantem Riemann-Tensor).
- **Kontrolle 3D (2+1):** Im 3D-Kuhn-Gitter sind die Fehlwinkel an Kanten.
  - Nach Schlaefli ist die Feldgleichung eps_e = 8 pi G (dS_m/dl_e), also Fehlwinkel nur an der Weltlinie und 0 sonst [M].

## Test (Code-Agent)

- **Codebasis:** RUNDE-36/regge-4d-1/code/regge4d.py und regge4d_auswertung.py (M(k), Schur-Komplement, Nullmoden,
  Schlaefli); dazu RUNDE-36/regge-schaum-1/code/regge_schaum.py (komplexer Schritt fuer d theta/d l).
- **Rechnung:**
  - Raeumliche Groesse L = 16, 24, 32 (soweit in <= 10 min je Lauf).
  - Ausgabe: delta eps fuer alle Dreieckstypen an allen Punkten bis r = L/2 und Torus-korrigierte Profile.
  - gamma(r) und G(r) aus den Achsen- und Diagonalpunkten.
- **Kontrollen:** Quelle orthogonal zum Nullraum; Hermitizitaet; 3D-Kontrolle; Kalibrierung.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| Z0 | Kontrollen: Quelle auf dem Nullraum <= 1e-12 relativ; 3D: Fehlwinkel ausserhalb der Weltlinie <= 1e-12 relativ, an der Weltlinie = 8 pi G M auf 1e-10 | 85 % |
| Z1 | gamma = 1 +- 0,02 auf der x-Achse fuer 6 <= r <= L/2 - 2 (groesstes L, Torus-korrigiert) | 70 % |
| Z2 | Newton: r^3 delta eps(tau, x) konstant auf 2 % fuer 6 <= r <= L/2 - 2; daraus G gleich der Normierung der Wirkung auf 2 % | 60 % |
| Z3 | [H] Auf der Diagonale (1,1,0) gilt ebenfalls gamma = 1 +- 0,03 | 60 % |

**Bedeutung (vorab):**
- **Z1 und Z2 treffen ein:** Im Laengennetz mit Zeitkanten koppelt eine Masse ueber ihre Eigenzeit, also ihre Energie.
  Das Netz gibt Newtons Anziehung und zugleich die raeumliche Kruemmung, die Licht doppelt so stark ablenkt wie Newton
  allein. Das ist Einsteins Messwert von 1919 bzw. Cassini, hier als Modellrechnung [L fuer die Messung].
- **Z1 verfehlt:** Das Gitter bricht die Gleichheit von Raum- und Zeitkruemmung; dann waere zu klaeren, ob ein
  Gitterartefakt (Diagonalmode) oder die Kopplung schuld ist.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
