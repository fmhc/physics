# SCHWEBUNGSUHR-3: Ergebnis (Leitung, Runde 23, explorativ)

- Gerechnet von der Leitung auf der .69 (kleintest.sh, cpu bis cpu4):
  - vier Laeufe 20:31:29 bis 20:33:01 UTC (22:31 bis 22:33 CEST), alle rc = 0
  - Code unveraendert (schwebung1d.py, gleiche sha256 wie SCHWEBUNGSUHR-2)
- Karte eingefroren 22:31:29 (KARTE.md.eingefroren-20261002-223129), vor dem ersten Lauf.
- Auswertung mit jq auf lauf-69/*.json. Ergebnis geschrieben ab 22:34:10 CEST (date).

## Ergebnis zuerst

1. **Im schwachen Bereich pendelt die Ladung nur. Ob der grosse Ball "gewinnt", entscheidet die Startphase.**
   - Bei Gegenphase (theta = pi) ist Q_1(0) genau das Maximum der Zeitreihe. Das Pendeln liegt unterhalb des Starts, mit
     derselben Spanne wie bei Gleichphase (6,656e-4 gegen 6,647e-4 bei D = 22).
   - Der Takt-Versatz kehrt sein Vorzeichen um: r = -0,18 % (D = 22) und -2,0 % (D = 18), bei Gleichphase +0,18 % und
     +1,9 %.
2. **Bei theta = pi/2 pendelt Q_1 symmetrisch um den Start.**
   - Das Mittel ueber [50; 3000] liegt 0,005 Spannen neben Q_1(0), und r = +0,01 %: Die Uhren behalten ihren freien Takt.
3. **Eine fortlaufende Drift gibt es nicht.** Die Fenstermittel von Q_1 am Anfang und am Ende unterscheiden sich relativ
   um -1,2e-7 (D = 22) und -1,6e-6 (D = 18), und Delta omega ist in allen drei Dritteln gleich.
4. **Auch im starken Bereich setzt die Startphase die Richtung** (D = 12, theta = pi):
   - Der grosse Ball gibt Ladung ab: Q_1 faellt von 3,123 auf 3,004 (-3,8 %).
   - Die Takte ruecken zusammen: Delta omega 0,0127 statt frei 0,0316 (r = -60 %).
   - Die Baelle stossen sich ab und fliegen auseinander (Abstand 25 auf 165). Bei Gleichphase waren es r = +109 % und
     Ladungsgewinn des grossen Balls.
5. **Lesart [H, 1D, M1]:**
   - Zwei Q-Ball-Uhren verhalten sich wie ein bosonischer Josephson-Kontakt. Die Ladung pendelt mit der Differenzfrequenz,
     und der Mittelwert haengt an der Startphase.
   - Nah beieinander gibt es einmal einen schnellen Fluss, dessen Richtung ebenfalls die Phase setzt. Danach trennen sich
     die Baelle, und die Takte frieren ein.
   - Weder "laufen auseinander" noch "synchronisieren" ist ein Gesetz.

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang |
|---|---|---|
| J1 | P22: Q_1(0) praktisch Maximum, Fenster A und E unter Q_1(0) | **eingetroffen**: (max - Q_1(0))/Spanne = 0; A = E = 3,161438 < 3,161771 |
| J2 | P22 und P18: r < 0 | **eingetroffen**: -0,0018 und -0,0196 |
| J3 | P22: Spanne innerhalb +-25 % von 6,647e-4 | **eingetroffen**: 6,656e-4 (+0,1 %) |
| J4 | H22: Mittel innerhalb +-0,15 Spanne um Q_1(0) | **eingetroffen**: +0,005 Spanne |
| J5 | P22: A gegen E relativ < 1e-5; P18: < 1e-4 | **eingetroffen**: -1,2e-7 und -1,6e-6 |
| J6 | P12: Q_1 in Fenster E unter Q_1(0) | **eingetroffen**: 3,00404 < 3,12319 |

**Bedeutung (vorab festgelegt):**
- J1 bis J5: Im schwachen Bereich ist der Takt-Versatz aus SCHWEBUNGSUHR-2 ein Josephson-Pendeln mit Startphasen-Versatz.
  Es gibt keine fortlaufende Drift und keinen Netto-Fluss vom kleinen zum grossen Ball.
- J6: Die Startphase setzt auch die Richtung des einmaligen Anfangsflusses im starken Bereich.

## Nebenbefunde (nicht vorhergesagt)

- H22 hat eine um 31 % groessere Spanne (8,70e-4) als bei theta = 0 und pi. Das einfache Zwei-Moden-Bild sagt gleiche
  Spannen voraus.
  - [H] Bei theta = pi/2 ruecken die Baelle leicht zusammen (Abstand 22,00 auf 21,55), und die Kopplung waechst.
  - Bei theta = 0 und pi bleibt der Abstand gleich bzw. waechst (P18: 18,08 auf 19,49).

## Latten (v3)

- L1: ja
- L2: ja. Vorzeichenumkehr und Zentrierung kamen aus dem Modell der Leitung; die Gleichphasen-Daten zeigten sie nicht.
- L3: teilweise. Nur ein Gitter (dx 0,1); den Gittervergleich hat SCHWEBUNGSUHR-2 bei D = 12, Gleichphase.
- L4: teilweise [L?]:
  - bosonischer Josephson-Kontakt (Smerzi u. a. 1997)
  - phasenabhaengiger Ladungsaustausch zwischen Q-Baellen (Battye/Sutcliffe 2000, Axenides u. a. 2000, nach
    SCHWEBUNGSUHR-2)
- L5: nein

## Selbstanzeigen

- **J1 bis J5 ruhen auf einem Modell, das die Leitung nach dem Blick auf die Gleichphasen-Daten gebildet hat.** Neu
  gegenueber den Daten sind die Vorzeichenumkehr, die Zentrierung und J6, nicht die Form 1 - cos.
- **Meine fruehere Aussage an Finn war zu stark** ("schwach gekoppelte Uhren laufen auseinander", "Ostwald-Reifung", "eine
  gemeinsame Zeit nur durch Verschmelzen"). Die Daten zeigen einen phasengesetzten Versatz, keine Reifung. Ob ein Bad
  Reifung treibt, prueft BAD-TAKT.

## Einfach gesagt

Zwei Wellenpakete tauschen Ladung aus wie zwei Wassertanks, die durch einen duennen Schlauch verbunden sind. Das Wasser
schwappt hin und her, in einem Takt, der aus dem Unterschied ihrer Uhren kommt. Wer am Ende im Mittel etwas mehr hat,
haengt nur davon ab, wie man sie gestartet hat: im Gleichtakt der grosse, im Gegentakt der kleine. Liegen sie sehr nah
beieinander, schwappt einmal viel hinueber, und dann stossen sie sich ab und fliegen auseinander. Die Uhren laufen also
weder von selbst auseinander noch von selbst zusammen.
