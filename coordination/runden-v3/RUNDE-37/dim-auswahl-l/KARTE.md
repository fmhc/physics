# DIM-AUSWAHL-L: Warum gerade drei grosse Raumdimensionen? Mechanismen, die Dimensionen auswaehlen, teilweise existieren lassen oder kurzlebig machen (Literaturkarte, Runde 42)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-04 18:46:54 CEST (date), vor jedem Abruf.
- **Finn (04.10., zwischen 18:36 und 18:40), woertlich:** "es müssten ja theoretisch unendlich (kugel) dimensionen
  möglich sein, aber bis zu wie vielen macht was sinn bzw wie sehr teilt sich die wahrscheinlichkeit dazu auf das die
  überhaupt zufällig erscheinen und können wir von einem einpendeln zwischen 3-4 dimensionen oder so die stabil sind
  ausgehen? vllt 12 die partiell existieren können, und mehr nur super kurzlebig?"
- **Projektstand (zuerst lesen, nicht neu abrufen):**
  - coordination/n-dimensionen-grundlagen-20260912.md: Ehrenfest, Tangherlini, Bertrand, Derrick, Huygens, Polya,
    kritische Dimensionen, Anderson, Maxwell, Anyonen, Weyl, Tegmark, Kaluza-Klein.
  - RUNDE-23/dd-spuren/ und RUNDE-41.md (Dark Dimension).
  - RUNDE-24 BAG-DIM (Beutel misst d_s).
  - STRANG-ANKER-L (GW170817 D = 4,02, LHC M_D).
- **Schreibtisch der Leitung [M, nicht gegengelesen]:**
  - Schnittregel: k-dimensionale Gebilde treffen sich in der Zeit generisch nur, wenn 2(k+1) >= D_Raumzeit, also
    D_Raum <= 2k + 1: Punkte 1, Faeden 3, Membranen 5.
  - Finns PU-Bild: Punkte mit Radius r auf einem Gitter mit Abstand a decken den Raum voll bis D = 4 (r/a)^2 und im
    Mittel (V_D (r/a)^D >= 1). Fuer r = a: voll bis 4, im Mittel bis 12. Das passt zu Finns "3-4" und "12", haengt aber
    an der Wahl r = a.
  - V_D = (2 pi / D) V_(D-2) hat sein Maximum bei D ~ 5,26.
- Kennzeichen: [S] an der Quelle gelesen, [S Abstract], [P], [L], [L?], [M], [ES], [H].

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung |
|---|---|
| E1 | Brandenberger/Vafa 1989: In einem Stringgas aus 9 Raumdimensionen koennen nur 3 gross werden, weil Windungsstrings nur dort generisch zusammentreffen und vernichten [L] |
| E2 | Alexander/Brandenberger/Easson 2000: Mit Membranen entsteht eine Hierarchie, 3 grosse und bis zu 2 weitere mittelgrosse Dimensionen [L?] |
| E3 | CDT (Ambjorn/Jurkiewicz/Loll 2004/05): Aus kausalen Triangulierungen entsteht dynamisch eine 4D-Welt; ohne Kausalitaet zerknuellte oder verzweigte Phasen [L] |
| E4 | Spektrale Dimension faellt in mehreren Quantengravitationsansaetzen bei kleinen Abstaenden auf ~2 (Carlip-Uebersicht) [L] |
| E5 | Kompakte Dimensionen vom Radius R geben einen Massenturm m_k = k/R; ihre Anregungen sind schwer und zerfallen schnell; Schranken aus LHC, Newton-Tests, GW170817 [P, L] |
| E6 | Es gibt Arbeiten, die eine Wahrscheinlichkeitsverteilung ueber die Zahl grosser Dimensionen angeben (Landschaft, ewige Inflation, Dekompaktifizierung) [L?] |

## Fragen

1. Welche Mechanismen waehlen 3 grosse Dimensionen aus? Mit Voraussetzungen und Stand: bewiesen, numerisch,
   spekulativ.
2. Gibt es eine Hierarchie "3 bis 4 stabil, einige teilweise (kompakt), der Rest kurzlebig"? Welche Zahlen nennt die
   Literatur, etwa 10, 11, 12 oder 26?
3. Gibt es eine Wahrscheinlichkeitsverteilung ueber die Dimensionszahl, und wie faellt sie fuer grosse D ab?
4. Messanker: Was schliessen Daten aus (GW170817, Newton-Tests, LHC, Kosmologie)?
5. Hoechstens ein Kartenvorschlag mit Ableitbarkeitsprobe, moeglichst als Test in unserem Netz (etwa Faeden auf einem
   Netz mit einstellbarer Dimension, die sich treffen und vernichten).

## Auftrag (feldforscher)

- **Abrufe:**
  - Hoechstens 10 gezielte Abrufe; jeder arXiv-API-Aufruf zaehlt als ein Abruf, auch wenn er mehrere Arbeiten
    liefert.
  - Keine Websuche. Lokale Kopien in quellen/.
- **Projekt-grep** nur mit Ausschluss versiegelter Pfade: --exclude-dir=vertraege-20260925, --exclude-dir=ks-1-dk-lauf,
  --exclude-dir=ks-1-dk-laeufe und Dateien mit VERSIEGELT oder T8-SOLL im Namen.
- **Arbeitsweise:** Feld-Regeln (Erwartung vor Abruf mit date-Zeit, eine Arbeitsdatei ARBEITSFELD.md, Gegensweep) und
  Dimensionsvergleich.
- **Abgabe:** DOSSIER.md mit:
  - Ergebnis zuerst
  - Pruefung des Schreibtischs
  - Erwartungen mit Ausgang
  - Antworten auf die Fragen 1 bis 5
  - Ankertabelle
  - Quellenliste
  - Selbstanzeigen
  - "Einfach gesagt" (3 bis 5 Saetze, fuer Finn)
- **Rahmen:** Zeitbox 75 min. Kein Rechnen; lokal kein python, awk oder perl.
