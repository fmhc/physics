# REGGE-4D-SCHIEF-1: Verschwindet die tote Hyperdiagonale im schiefen 4D-Netz, und wird die Naehe der Masse sauberer? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 04:00:03 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - REGGE-4D-1: Im 4D-Kuhn-Gitter gibt es eine fuenfte Nullmode, die lange Diagonale (1,1,1,1). An allen 14 Dreiecken mit
    ihr liegt ihr ein rechter Winkel gegenueber (Thales).
  - REGGE-ZEIT-1: Diese Mode kostet keine Wirkung, veraendert aber Fehlwinkel. Nahe einer Masse liegt gamma deshalb
    vermutlich einige Prozent neben 1 (gamma(6) = 1,087 auf der x-Achse) [H].
  - REGGE-4D-1 schlug als Folge vor: ein verzerrtes Gitter ohne rechte Winkel.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Netz:** dasselbe periodische 4D-Kuhn-Gitter (gleiche Kombinatorik), aber alle Ecken mit einer festen linearen
  Abbildung A verschoben: X -> A X. Das Netz bleibt flach und periodisch; Fourier-Methoden aus REGGE-4D-1 gelten weiter.
- **Wahl:** A wirkt nur auf die drei Raumachsen, A = 1 + s B mit fester, allgemeiner (nicht symmetrischer) Matrix B
  (Eintraege in [-1, 1], Saat fest), s = 0,1 und 0,2.
  - Die Zeitachse tau bleibt senkrecht, damit die Weltlinie aus REGGE-ZEIT-1 gerade bleibt.
  - Die rechten Winkel an der Hyperdiagonale verschwinden dann allgemein [M, zu pruefen].
- **Erwartung [L]:** Fuer "dicke" Simplizes geht Regges Wirkung im Kontinuumsgrenzfall in Einsteins Wirkung ueber
  (Cheeger/Mueller/Schrader). Die lange-Wellen-Form sollte also in physikalischen Koordinaten (k_phys = A^-T k) wieder
  (1/4) k^2 (P2 - 2 P0) sein.

## Test (Code-Agent)

- **Codebasis:** RUNDE-36/regge-4d-1/code/ (M(k), Nullmoden, Schur-Komplement) und RUNDE-37/regge-zeit-1/code/
  (Weltlinie, Fehlwinkel, gamma, Kalibrierung, Festlegung der Hyperdiagonale).
- **Teil 1, Moden:**
  - Nullmoden bei k = 0 und bei allgemeinem k fuer s = 0; 0,1; 0,2 (s = 0 als Kontrolle gegen REGGE-4D-1: 11 bzw. 5).
  - Lange-Wellen-Form in physikalischen Koordinaten: Spin-2-Werte, konformer Wert, Verhaeltnis, Richtungsstreuung.
- **Teil 2, ruhende Masse:** wie REGGE-ZEIT-1 auf dem schiefen Netz (s = 0,2), L = 32.
  - gamma und G-Staerke auf einer physikalischen Achse fuer r = 6 bis 14.
  - Vergleich mit dem unverzerrten Kuhn-Gitter (Werte aus REGGE-ZEIT-1).
  - Ohne fuenfte Nullmode sollte keine Festlegung der Fehlwinkel mehr noetig sein; pruefen, ob sie eindeutig sind.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SC0 | Kontrollen: Netz flach (<= 1e-12) fuer alle s; M(k) hermitesch (<= 1e-10); s = 0 reproduziert REGGE-4D-1 (11 Nullmoden bei k = 0, 5 bei allgemeinem k) | 85 % |
| SC1 | s = 0,1 und 0,2: Bei k = 0 genau 10 Nullmoden, bei allgemeinem k genau 4 (kleinster Nicht-Eich-Eigenwert > 1e-6 mal Mittel) | 65 % |
| SC2 | s = 0,2, abs(k_phys) = 0,05 bis 0,1: In physikalischen Koordinaten fuenf Spin-2-Werte gleich auf 1 %, Verhaeltnis konform zu Spin 2 = -2 +- 0,02, Richtungsstreuung <= 1 % | 60 % |
| SC3 | [H] Ruhende Masse, s = 0,2: Fehlwinkel ohne Festlegung eindeutig, und abs(gamma(r = 6) - 1) < 0,044, also weniger als die Haelfte der Kuhn-Abweichung | 40 % |

**Bedeutung (vorab):**
- **SC1 und SC2 treffen ein:** Die tote Hyperdiagonale ist ein Kunstprodukt der rechten Winkel im regelmaessigen Gitter.
  Ein schiefes Netz hat sie nicht und zeigt trotzdem Einsteins Fingerabdruck. Fuer Finns Bild hiesse das: Ein
  ungeordnetes Netz ist eher besser als ein Kristall [H].
- **SC3 trifft ein:** Die Abweichung nahe der Masse kam von der toten Diagonale.
- **SC3 verfehlt:** Die Naehe der Masse ist ein allgemeiner Gittereffekt (Masse auf einer einzigen Weltlinie, Feld bei
  wenigen Maschen), nicht die Diagonale.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
