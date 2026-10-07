# INDUZIERT-ZUFALL-2D: Mitteln sich die Gitterterme auf einem zufaelligen Netz weg, so dass nur Polyakov bleibt? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 06:16:41 CEST (date), vor jeder Rechnung.
- **Anlass:** INDUZIERT-1 (RUNDE-37/induziert-1/ERGEBNIS.md).
  - Auf dem festen, regelmaessigen Netz erzeugt ein Skalarfeld keine Einstein-Steifigkeit.
  - In 2D steckt Polyakovs universelle Zahl im nicht-analytischen Teil (lambda = 0,996). Sie wird aber von lokalen
    Gittertermen verdeckt: konforme Steifigkeit +0,1249 statt -1/(24 pi), dazu richtungsabhaengig (0,125 / 0,080 /
    0,170).
  - Frage fuer Finns Weiche: Hilft Unordnung?
    - Wenn ja, wird ein zufaelliges Netz (Schaum) Kandidat fuer Ueberleitung 1.
    - Wenn nein, muss das Netz selbst schwanken (Summe ueber Netze) oder von Hand nachgestimmt werden.
- **Schreibtisch [M/H]:**
  - In 2D sind die einzigen lokalen, geometrischen Glieder mit hoechstens zwei Ableitungen Flaeche und Kruemmung. Die
    Kruemmung ist topologisch, gibt also keine k^2-Steifigkeit der konformen Mode.
  - Jede lokale k^2-Steifigkeit ist darum ein Gitterterm, der von der Form der Dreiecke abhaengt.
  - Auf einem zufaelligen Netz mittelt sich die Richtung heraus, aber nicht zwingend der Betrag.
  - Erwartung der Leitung: Ein isotroper Rest bleibt (Formabhaengigkeit), Polyakov bleibt verdeckt.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Test (Code-Agent)

- **Netze:** Poisson-Punkte auf dem 2D-Torus, periodische Delaunay-Triangulierung (z. B. Punkte mit Kopien
  triangulieren und auf den Grundbereich zurueckfalten), N = 4 000, 16 000 und 64 000 Knoten, je mehrere Saaten.
  - Kontrolle: das regelmaessige Netz aus rechtwinkligen Dreiecken aus INDUZIERT-1 Teil A.
- **Materie:** P1-Skalar (Kotangens-Laplace), Konventionen wie INDUZIERT-1 Teil A, also auch dasselbe Flaechenglied bzw.
  det'(M^-1 K). Code dort wiederverwenden.
- **Konforme Mode:**
  - delta l_ij / l_ij = (sigma_i + sigma_j)/2 mit sigma = s cos(k.x).
  - Zweite Ableitung von 1/2 log det' nach s, per symmetrischer Differenz mit duenner LU-Zerlegung (log abs det aus der
    Diagonale).
  - Mehrere k (Vielfache von 2 pi/L) und Richtungen.
  - Gemessen wird die Steifigkeit pro Flaeche und k^2, mit Polyakov -1/(24 pi) = -0,013263 als Bezug.
- **Knotenverschiebungen:** Steifigkeit der zwei Verschiebungsmoden xi = s e cos(k.x) bei gleicher Kantenlaengen-Norm,
  im Vergleich zur konformen Mode.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IZ0 | Kontrolle: Das regelmaessige Netz gibt die konforme Steifigkeit aus INDUZIERT-1 Teil A (+0,1249) auf 1e-3 wieder | 85 % |
| IZ1 | [H] Auf den Zufallsnetzen liegt das Saatmittel der konformen Steifigkeit pro Flaeche und k^2 beim kleinsten k und N = 64 000 innerhalb 20 % von Polyakovs -1/(24 pi) | 25 % |
| IZ2 | Isotropie: Die Richtungsstreuung des Saatmittels ist <= 5 % | 70 % |
| IZ3 | [H] Die Knotenverschiebungs-Moden sind weich: Steifigkeit <= 10 % des Betrags der konformen Steifigkeit beim kleinsten k | 30 % |
| IZ4 | Die Streuung ueber Saaten faellt mit N etwa wie N^(-1/2) (Steigung -0,5 +- 0,15) | 60 % |

**Bedeutung (vorab):**
- **IZ1 und IZ3 treffen ein:** Unordnung loescht die Gitterterme im Mittel. Dann bleibt nur die universelle,
  geometrische Antwort, und ein zufaelliges Netz waere Kandidat fuer Schwerkraft aus Materie, als naechstes in 4D.
- **IZ1 verfehlt, IZ2 trifft ein:** Unordnung macht die Antwort richtungsfrei, aber nicht geometrisch.
  - Ein fester Rest bleibt, der von der Dreiecksform abhaengt.
  - Dann braucht Ueberleitung 1 ein schwankendes Netz (Summe ueber Netze) oder Feinabstimmung.
- **IZ4 verfehlt:** Die Antwort mittelt sich nicht selbst; dann zaehlt jedes einzelne Netz.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
