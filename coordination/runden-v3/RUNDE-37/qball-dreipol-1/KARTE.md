# QBALL-DREIPOL-1: Q-Baelle mit drei Polen (drei Komponenten mit Richtung) wie auf der Tetraeder-Ebene: welcher Pol gewinnt, und binden drei verschiedene Pole? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 17:14:08 CEST (date), vor jeder
  Rechnung.
- **Finn (04.10., Nachricht zwischen 17:11 und 17:13, woertlich):** "denk mal q-balls auf tetraeder ebene quasi runter,
  also auf 3d/4d als 3 pole bzw ausprägungen mit richtung"
- **Lesart der Leitung [H]:**
  - Ein Q-Ball mit drei komplexen Komponenten Phi = (phi_1, phi_2, phi_3), also drei "Polen". Jede Komponente gehoert zu
    einer der drei Tetraeder-Richtungen (die drei zweizaehligen Achsen bzw. das Biege-Triplett, RUNDE-42/
    FARBE-SCHREIBTISCH.md). Die "Richtung" ist die Drehung der inneren Phase.
  - Ohne Gitter ist das ein U(3)-symmetrischer Q-Ball. Die Tetraeder-Symmetrie gibt eine Anisotropie wie
    g4 Summe_a abs(phi_a)^4 (kubisch, wie x^4 + y^4 + z^4).
  - Literatur [L]: Q-Baelle aus drei farbigen Komponenten gibt es als "B-Baelle" der supersymmetrischen Erweiterung
    (Kusenko/Shaposhnikov 1998; flache Richtung u d d, Farbsingulett ueber eps_abc). Das ist das Vorbild eines
    "Baryon-Q-Balls" aus drei Polen.
- **Ableitbarkeitsprobe [M, Leitung, ungeprueft]:**
  - Fuer eine feste innere Richtung n (Betrag 1) ist der Q-Ball ein gewoehnlicher Q-Ball mit wirksamer Kopplung
    g_eff = g4 Summe_a n_a^4. Diese Groesse liegt zwischen 1/3 (gleich gemischt) und 1 (ein Pol).
  - Welcher Pol bzw. welche Mischung bei fester Ladung gewinnt, folgt also aus dem Vorzeichen von g4 und der bekannten
    Abhaengigkeit E(Q; g). Das ist vorab ableitbar und nur Kontrolle.
  - Nicht ableitbar: die Wechselwirkung zweier Q-Baelle mit verschiedenen Polen gegen gleiche Pole (Abstand,
    Phasenlage), und ob drei Q-Baelle mit drei verschiedenen Polen einen gebundenen, stabilen Verbund bilden.
- **Projektbezug:**
  - QBALL-PYRO-1: Der gewoehnliche Q-Ball merkt das Pyrochlor-Gitter kaum (E und Q 0,8 % unter dem Kontinuum); exakte
    Ringe auf flachen Baendern.
  - QB-BS-2D: drehender Knoten plus Q-Ball nicht gebunden.
  - Q-Ball-Code des Projekts (B.5 bzw. 2+1).
  - Neu ist hier allein die Dreikomponenten-Struktur; Projekt-grep ohne Treffer zu mehrkomponentigen Q-Baellen.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Auftrag (Code-Agent)

1. **Lesen:** QBALL-PYRO-1 (ERGEBNIS, Code), QB-BS-2D (ERGEBNIS, Code), Papier-I-Modell (B.5) nach Projekt-grep. Das
   Q-Ball-Potential des Projekts uebernehmen und nur um drei Komponenten mit U(3)-Kopplung plus Anisotropie g4 erweitern.
2. **Modell in 2+1 (Tempo):**
   - Feld Phi in C^3, Potential U(abs(Phi)^2) + g4 Summe_a abs(phi_a)^4, mit g4 = -0,1, 0, +0,1 (relativ zur
     Selbstkopplung; im Plan festlegen).
3. **Messungen:**
   - (a) Kontrolle: E(Q) fuer ein Pol, zwei Pole, gleich gemischt, und Vergleich mit g_eff.
   - (b) Zwei Q-Baelle in Ruhe im Abstand d (gleiche Pole in Phase, gleiche Pole gegenphasig, verschiedene Pole):
     Wechselwirkungsenergie gegen d aus relaxierten bzw. eingespannten Zustaenden.
   - (c) Drei Q-Baelle mit drei verschiedenen Polen im Dreieck: gebunden gegen drei getrennte; Zeitentwicklung bis
     t = 200 mit kleinem Rauschen.
4. Plan, Rauchlauf, Einfrieren wie ueblich.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QD0 | Kontrolle: E(Q) je innere Richtung folgt g_eff = g4 Summe n_a^4 (Abweichung < 1 %) | 90 % |
| QD1 | [H] Q-Baelle mit verschiedenen Polen wechselwirken schwaecher als gleiche Pole in Phase (Betrag der Wechselwirkungsenergie bei d = 2 Radien mindestens 3-mal kleiner) | 60 % |
| QD2 | [H] Bei der Anisotropie, die das Mischen beguenstigt, ist ein Dreier aus drei verschiedenen Polen gebunden (Energie unter drei getrennten) | 35 % |
| QD3 | [H] Wenn QD2: Der Dreier bleibt bis t = 200 zusammen und zerfaellt nicht in einen Ein-Pol-Q-Ball | 30 % |

**Bedeutung (vorab):**
- **QD2 und QD3 treffen ein:** Ein "Baryon-Q-Ball" aus drei Polen ist im Modell moeglich. Das ist ein Bild fuer drei
  Farben in einem gebundenen Klumpen, noch ohne Eichfeld [H].
- **QD2 verfehlt:** Drei Pole binden nicht von selbst; der Zusammenhalt muesste vom Kleber kommen (GLUONEN-L,
  KOPPLUNG-TETRA-1).

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b, geteilt mit DREIECK-TAKT-1; der Lock
  regelt die Reihenfolge. Je Lauf <= 10 min, 1 Thread. Zeitbox 150 min.
