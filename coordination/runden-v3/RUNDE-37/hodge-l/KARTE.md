# HODGE-L: Review Hodge-Theorie fuer Finns Netz. Was leisten diskrete Hodge-Zerlegung, Hodge-Stern und FEEC fuer Fluss-Eis, Licht, Schwerewellen und Umklappen? (Runde 46, Finn-Auftrag)

- Leitung claude-primary. Karte und Erwartungen geschrieben ab 2026-10-05 06:00:25 CEST (date), vor jedem Abruf.
- **Finn (05.10., vor 05:58:58), woertlich:** "... Review auch Hodge Theorie"
- Kennzeichen: [S], [S Abstract], [L], [L?], [M], [ES], [H], [P].

## Projektsuche (vor der Karte)

- "Hodge-Gewichte" bzw. "Hodge-Form" stehen in MATERIE-NETZ-1 und LICHT-FINN-NETZ-1 (PLAN), noch ohne Theorie [P]:
  - Mit Gewichten aus den Kantenlaengen spuert das Licht die Laengen.
  - Mit Einheitsgewichten (rein topologisch) spuert es sie nicht, und es gibt nur die halbe Ablenkung.
- Hodge-Zerlegung in 2D bei INDUZIERT-WILSON-2D [P].
- Christiansen/Hu/Lin 2023 (Regge und Torsion) in TORSION-STEIF-1 gelesen [P].
- FEEC kommt im Projekt nur zufaellig vor (688 Treffer, meist Zeichenfolgen in Daten); kein Review.

## Lesart der Leitung: wo Hodge-Theorie Finns Netz direkt beruehrt [H, M]

1. **Fluss-Eis:**
   - Jeder Fluss auf den Kanten zerfaellt eindeutig in Gradient (aus Knotenpotentialen), Wirbel (um Flaechen) und harmonischen Anteil (globale Zyklen, Zahl = Betti-Zahl).
   - Die Eisregel (quellenfrei) laesst nur Wirbel und harmonischen Anteil uebrig. Das ist die Coulomb-Phase.
   - Netzwerk-Literatur: Hodge-Laplace-Operatoren auf Graphen und Simplizialkomplexen.
2. **Licht:**
   - In der diskreten aeusseren Analysis steckt die Metrik nur im Hodge-Stern; Gewichte = duales Volumen/primales Volumen.
   - "Einheitsgewichte" heisst: kein Hodge-Stern, also topologische Feldtheorie.
   - Darum spuert Maxwell mit Hodge-Stern die Kantenlaengen (MATERIE-NETZ-1).
3. **Zufallsnetze und Umklappen:**
   - Der umkreisbasierte Hodge-Stern ist nur auf "gut zentrierten" (in 2D: Delaunay-) Netzen positiv.
   - Rippa 1990 [L?]: In 2D minimiert Delaunay die Dirichlet-Energie ueber alle Triangulierungen. Das waere ein Mechanismus fuer Umklappungen, getrieben von der Feldenergie (Bezug UMKLAPP-1).
   - Gilt das in 3D?
4. **Schwerewellen und Regge:**
   - Linearisierter Regge-Kalkuel ist ein Finite-Elemente-Verfahren im FEEC-Rahmen (Christiansen 2011 [L?]).
   - Exakte diskrete Komplexe (Elastizitaets- bzw. Regge-Komplex) verhindern Scheinmoden.
   - Ist der Spur-Eichdefekt auf Finns gefuelltem Netz (TT-ISO-1, Regel zweiter Klasse) eine fehlende Exaktheit des diskreten Komplexes? [H]
5. **Materie und Abstrahlung:** Ein Materiefeld mit Hodge-Stern-Gewichten koppelt ueber seine Spannungen an alle Kantenlaengen. Genau das braucht Abstrahlung (PUMPE-NETZ-1).

## Ableitbarkeitsprobe

- **Vorab ableitbar [L, M]:**
  - Die Zerlegung Gradient + Wirbel + harmonisch auf endlichen Komplexen (lineare Algebra: Bild d, Bild d^T, Kern Laplace).
  - Zahl der harmonischen Formen = Betti-Zahlen.
  - Metrik nur im Hodge-Stern.
  - Nur Kontrollen bzw. Einordnung.
- **Nicht ableitbar (Literatur):**
  - Positivitaets- und Konvergenzbedingungen des diskreten Hodge-Sterns in 3D (gut zentriert, Delaunay)
  - Rippa in 3D
  - Christiansens Regge-FEEC-Aussagen
  - Bedingungen fuer exakte diskrete Elastizitaets- bzw. Gravitationskomplexe und Scheinmoden
  - Gibt es Arbeiten, die zweite-Klasse-Bedingungen bzw. Spur-Eichdefekte im Regge-Kalkuel ueber Komplexe erklaeren?

## Auftrag (feldforscher)

1. Literatur zu 1 bis 5. Mindestens:
   - Lim 2020 (Hodge-Laplacians on graphs, SIAM Review) bzw. Jiang u. a. 2011 (HodgeRank)
   - Hirani 2003 bzw. Desbrun u. a. 2005 (DEC)
   - Arnold/Falk/Winther 2006/2010 (FEEC)
   - Christiansen 2011 (Regge als FEEC)
   - VanderZee/Hirani u. a. (gut zentrierte Netze)
   - Rippa 1990
2. Je Punkt: was die Literatur sagt [S], was das fuer Finns Netz heisst [H], ob etwas im Projekt schon gerechnet ist [P].
3. Besonders: Frage 4, also ob Spur-Eichdefekt bzw. zweite Klasse und Exaktheit zusammenhaengen. Und Frage 3 (Umklappen ueber Feldenergie in 3D).
4. **Betti-Zahlen von Finns Netzen:** Pyrochlor bzw. gefuelltes Netz V, periodisch auf dem Torus. Wie viele harmonische Fluesse gibt es (globale Zyklen)? Vorab ableitbar [M]: auf dem 3-Torus b1 = 3. Nur Kontrolle.
5. Hoechstens ein Kartenvorschlag, mit Ableitbarkeitsprobe und Projekt-grep.

## Erwartungen (vor jedem Abruf)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| HO1 | [L?] Der umkreisbasierte DEC-Hodge-Stern ist in 3D nur auf gut zentrierten Netzen positiv; Delaunay allein genuegt in 3D nicht | 70 % |
| HO2 | [L?] Rippas Satz (Delaunay minimiert die Dirichlet-Energie) gilt in 2D, in 3D nicht allgemein | 65 % |
| HO3 | [L?] Christiansen zeigt: Linearisierter Regge-Kalkuel ist ein FEEC-Verfahren mit exaktem Komplex (Regge-Elemente) | 70 % |
| HO4 | [H] Eine Arbeit verbindet zweite-Klasse-Bedingungen bzw. gebrochene Eichsymmetrie im Regge-Kalkuel mit Diskretisierung bzw. Komplexen (z. B. Dittrich u. a.) | 50 % |

**Bedeutung (vorab):**
- **HO1 bis HO3 treffen ein:** Die Hodge-Theorie ist die Mathematik hinter Finns Netz.
  - Fluss-Eis ist Wirbel plus harmonisch.
  - Das Licht spuert die Geometrie ueber den Hodge-Stern.
  - Regge ist FEEC.
  - Zufallsnetze brauchen gut zentrierte Zellen, sonst werden Gewichte negativ. Das ist eine Bedingung an den Glas-Zweig.
- **HO4 trifft ein:** Fuer den Spur-Eichdefekt gibt es eine Literaturspur. Das waere ein Weg zu L1 (erster Klasse).

## Rahmen

- feldforscher, Zeitbox 60 min, hoechstens 10 Abrufe (arXiv-API, INSPIRE-API, arxiv.org per WebFetch, freie Verlagsseiten), keine Websuche.
- Erwartung mit date-Zeit vor jedem Abruf in ARBEITSFELD.md.
- Schreiben nur in RUNDE-37/hodge-l/.
