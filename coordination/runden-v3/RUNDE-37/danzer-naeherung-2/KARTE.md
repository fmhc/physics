# DANZER-NAEHERUNG-2: Werden die Ikosaeder-Naeherungsnetze mit Takt-Gewichten richtungsgleich, und hat der kubische Rest einen Boden? (Runde 47, Folgekarte zu DANZER-NAEHERUNG-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 08:32:16 CEST (date), vor jeder Rechnung.
- **Finns Weiche (05.10.):** "Kristall/Glas: beide Zweige testen". Dazu gehoert der Quasikristall-Zweig.
- **Herkunft:** DANZER-NAEHERUNG-1 (RUNDE-37/danzer-naeherung-1/ERGEBNIS.md, Abschnitte 2 und 5) [P]:
  - Ammann-Kramer-Naeherungen 1/1, 2/1, 3/2 (32, 136, 576 Ecken je Zelle), periodisches Delaunay.
  - Der kubische l = 4-Anteil beta von a2 faellt (Skalar -0,00345 -> -0,00083 -> -0,00060; Maxwell-Mittel -0,00163 -> -0,00077 -> -0,00043), aber nicht wie die lineare Phason-Kopplung.
  - Das Grundtempo war um 1 bis 7 % richtungsabhaengig. Ursache: Der Zitter loeste Delaunay-Gleichstaende zufaellig auf, und Einheitsgewichte belasteten Kanten mit *1 = 0 voll.
  - Vorschlag dort: DEC-Gewichte (Skalar mit *1, Maxwell mit *2 und *1) und die Naeherung 5/3 (2 440 Ecken je Zelle) fuer den Boden.
- **Neu seit dem Vorschlag:** TAKT-UMKLAPP-1 (HT0): Finns Takt ist 8 d0^T *1 d0, umkreisbasiert. Der Skalar mit *1 ist also genau der Takt bis auf den Faktor 8 [P].
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (Leitung, Bausteine verkettet, mit Kennzahlen-Abgleich)

- **Kennzahlen-Abgleich:** Die Naeherungsnetze gibt es im Projekt nur aus DANZER-NAEHERUNG-1. V, S (= C15), A15 und die Glasnetze haben andere Zellgroessen. Kein Doppel.
- **Vorab ableitbar [M]:**
  - **Gleichstaende:** An einem Gleichstand (5 oder mehr Punkte auf einer Kugel) fallen die Umkreismittelpunkte zusammen. Eine Kante bzw. Flaeche, die es nur in einer der Aufloesungen gibt, hat dann *1 = 0 bzw. *2 = 0. Die DEC-Operatoren haengen also nicht davon ab, wie der Gleichstand aufgeloest wird.
  - **Folgen:**
    - Jede Naeherung behaelt ihre volle kubische Symmetrie.
    - Das Grundtempo (Rang 2) ist exakt isotrop.
    - beta ist von der Zittersaat unabhaengig.
  - Beides ist nur Kontrolle (D2-0).
- **Nicht ableitbar:**
  - Betrag und Abfall von beta mit der Ordnung bei DEC-Gewichten
  - ob ein Boden bleibt
  - ob DEC-Gewichte beta gegenueber Einheitsgewichten verkleinern

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| D2-0 | Kontrolle, vorab ableitbar: Mit DEC-Gewichten ist das Grundtempo auf jeder Naeherung und fuer jede Saat isotrop (Spanne < 1e-10), und beta stimmt ueber die Saaten auf < 1e-10 ueberein | 85 % |
| D2-1 | [H] \|beta(3/2)\| / \|beta(1/1)\| < 1/3 fuer Skalar und Maxwell-Mittel mit DEC-Gewichten | 60 % |
| D2-2 | [H] Kein Boden bis 5/3: \|beta(5/3)\| < 0,6 \|beta(3/2)\| fuer Skalar und Maxwell-Mittel | 50 % |
| D2-3 | [H] Mit DEC-Gewichten ist \|beta\| auf jeder Ordnung kleiner als mit Einheitsgewichten (DANZER-NAEHERUNG-1) | 50 % |

**Bedeutung (vorab):**
- **D2-1 und D2-2 treffen ein:** Mit Finns Takt-Gewichten naehert sich der Quasikristall-Zweig ohne Abstimmung der Isotropie. Er waere damit ein Weg zu einem richtungsgleichen Netz ohne Feinabstimmung, wie sie GW170817 verlangt (~1e-15) [H].
- **D2-2 verfehlt:** Es bleibt ein Boden. Dann braucht auch der Quasikristall-Zweig eine Abstimmung.
- **D2-0 verfehlt:** Fehler im Bau oder ein Gleichstand ohne Kugel-Entartung. Erst klaeren, dann weiter.

## Rahmen

- Code-Agent, Code aus danzer-naeherung-1/code kopieren, dort nichts aendern. Hodge-Sterne umkreisbasiert, wie im takt-umklapp-1/code.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4, ein Thread. Je Lauf hoechstens 10 min; 5/3 vorher per Rauchtest auf Laufzeit pruefen, notfalls in Abschnitte teilen. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
