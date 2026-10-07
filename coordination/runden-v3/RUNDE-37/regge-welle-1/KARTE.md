# REGGE-WELLE-1: Wie schnell laufen Schwerewellen im 4D-Laengennetz, und wie viele gibt es? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 04:18:48 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - REGGE-4D-1 zeigt die Spin-2-Struktur euklidisch fuer lange Wellen. Ungeprueft sind die echte Zeitrichtung, die zwei
    Polarisationen und ihre Geschwindigkeit.
  - Finns Schwerpunkt "Lichtgeschwindigkeit im Netz"; AETHER-UHR-1: Alles muss denselben Lichtkegel haben.
  - Ideenpool R1.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Verfahren:** Die euklidische Hesse-Form M(k) des 4D-Kuhn-Gitters aus REGGE-4D-1 haengt analytisch von e^(i k_mu) ab.
  Mit k_tau = i omega wird sie zur Form fuer echte Zeit [M]. Die Fortsetzung eines euklidischen Gitters ist formal; das
  Kuhn-Gitter haette in Lorentz-Signatur lichtartige Kanten.
- **Laufende Moden:**
  - Frequenzen omega(k_raum), an denen die Form auf dem Komplement der Eichmoden (und der Diagonalmode) einen Nullwert
    bekommt.
  - Im Kontinuum fallen dort alle sechs Nicht-Eich-Werte zugleich auf null (bei omega = abs(k)) [M]. Auf dem Gitter
    koennen sie sich aufspalten.
- **Ehrlich vorab:** Fuer lange Wellen ist v = 1 aus REGGE-4D-1 vorab ableitbar [M]. Neu sind die Dispersion bei
  kuerzeren Wellen, die Richtungsabhaengigkeit und die Frage, wie sich die sechs Werte aufspalten.

## Test (Code-Agent)

- **Codebasis:** RUNDE-36/regge-4d-1/code/ (M(k), Schur-Komplement, Nullmoden); RUNDE-37/regge-zeit-1/code/
  (Fehlwinkel, Eichfestlegung) zum Vergleich.
- **Fortsetzung:** M(k_raum, k_tau = i omega) bauen, die Eich- und Diagonal-Nullvektoren mit fortsetzen (sie bleiben
  Nullvektoren) [M, pruefen].
- **Nullstellen:** fuer abs(k_raum) = 0,05; 0,1; 0,2; 0,4; 0,8 in mindestens 20 Richtungen die reellen omega suchen, an
  denen ein Eigenwert der Form auf dem Komplement durch null geht (bzw. det = 0).
- **Ausgabe:** omega/abs(k) je Mode, Zahl der Nullstellen, Aufspaltung, Richtungsstreuung.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| W0 | Kontrolle: Fortsetzung bei reellem k_tau gibt M(k) aus REGGE-4D-1 auf 1e-12; Eich- und Diagonal-Nullvektoren bleiben bei komplexem k_tau Nullvektoren (<= 1e-10) | 85 % |
| W1 | abs(k) = 0,05 und 0,1: Alle Nullstellen liegen bei omega/abs(k) = 1 +- 0,005, in allen Richtungen | 70 % |
| W2 | abs(k) = 0,8: omega/abs(k) weicht um mindestens 1 % von 1 ab, richtungsabhaengig (Streuung ueber Richtungen >= 0,1 %) | 65 % |
| W3 | [H] Bei abs(k) = 0,4 spalten sich die Nullstellen in Gruppen auf; mindestens eine Gruppe von genau zwei bleibt auf 1e-3 entartet (Kandidat fuer die zwei Polarisationen) | 40 % |

**Bedeutung (vorab):**
- **W1 und W2 treffen ein:** Schwerewellen laufen im Netz fuer lange Wellen mit Lichtgeschwindigkeit. Bei Wellenlaengen
  von wenigen Maschen werden sie langsamer bzw. richtungsabhaengig. Das gaebe eine Gitterschranke zum Vergleich mit
  GW170817 (Geschwindigkeit auf ~1e-15 gleich der des Lichts [L]).
- **W3 trifft ein:** Die zwei Polarisationen sind auch auf dem Gitter als Paar erkennbar.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000b und cpu5 (nur CPU-Rechnung); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
