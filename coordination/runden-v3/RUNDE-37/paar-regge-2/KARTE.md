# PAAR-REGGE-2: Traegt das rotierende Paar mit dem Literatur-Intercept die Gitter-Tensorglueballs? (Runde 46, Finns rotierendes Paar)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 05:41:48 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - Kartenvorschlag aus HISH-GLUEBALL-L (RUNDE-37/hish-glueball-l/DOSSIER.md, Abschnitt 6). Modelle, Daten, Messgroessen, Ableitbarkeitsprobe und Grenzen sind **woertlich bindend**; Vorhersagen und Wahrscheinlichkeiten setzt die Leitung.
  - Finns rotierendes Paar (GLUON-PAAR-L).
  - PAAR-REGGE-1: Endmassen bei festem Intercept 0 bzw. 1/12 tragen die Gitterdaten nicht. Das ist teils literaturbekannt; der Literatur-Intercept fuer rotierende Strings ist 1 bzw. 2 (HISH-GLUEBALL-L).
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Modelle (woertlich, vorab fest)

- (I) geschlossen: zwei gleiche Massen m an den Faltstellen, Spannung 2 sigma, fester Intercept a = 2 (H5 Gl. 1.5).
- (II) offen-adjungiert: Spannung 9/4 sigma, fester Intercept a = 1 (H5 Gl. 1.4; Hellerman/Swanson).
- Variante zu (I): Intercept mit der Korrektur erster Ordnung aus H5 Gl. (7.9). Nur wenn eps1 und eps2 an der Quelle eindeutig definiert sind; das ist vorab zu klaeren.

## Daten (woertlich)

- (A) A&T 2020: 2++ 4,894(22), 4++ 7,60(12)*.
- (B) MT-Gerade wie in PAAR-REGGE-1.
- (C) als Lesart der Zuordnung: 2++* 6,788(40) statt 2++ (S&W-Kette) [S F3 Tab. 17].

## Messgroessen (woertlich)

- bestes m, chi^2 (1 Freiheitsgrad), p, v_end(2), v_end(4)
- Baender wie PAAR-REGGE-1

## Pflicht vor dem Plan

- **(R1) Sharov 2006 bis 2008 im Volltext lesen** (arXiv-Nummern ueber INSPIRE bzw. den HISH-GLUEBALL-L-Ordner; ein bis drei Abrufe). Hat Sharov den Fit schon gemacht, wird die Karte zur Nachrechnung; das steht dann zuerst im Plan.
- H5 (Sonnenschein/Weissman 2020) aus hish-glueball-l/quellen lokal lesen: Gl. (1.4), (1.5), (7.9).

## Ableitbarkeitsprobe (woertlich, dazu Zusatz)

- **Ableitbar, nur Kontrollen [M]:**
  - masselos (I): M(2) = 0, M(4) = sqrt(8 pi) = 5,013
  - masselos (II): M(2) = 3,760, M(4) = 6,512
  - Alle liegen unter den Gitterwerten. Endmassen arbeiten also in die richtige Richtung, anders als bei a = 0 oder 1/12.
- **Nicht ableitbar:** ob EINE Masse beide Punkte trifft. Grob [M]: Die Massenverschiebung bei festem J faellt etwa wie E^(-1/2), (A) braucht aber fast gleiche Verschiebungen (+1,13 und +1,09 fuer (II)). Der Ausgang ist offen; die Karte kann scheitern und bestehen.
- **[Zusatz Leitung]:** Mit einem Parameter (m) und zwei Punkten bleibt ein Freiheitsgrad. Ein p >= 0,05 ist damit eine echte Probe, aber eine schwache: zwei Punkte, 4++ mit Stern.

## Vorhersagen (vor jeder Rechnung, Leitung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| PQ0 | Kontrolle: masselose Werte (I) 0 und 5,013 bzw. (II) 3,760 und 6,512 auf 1e-6 reproduziert | 90 % |
| PQ1 | [H] Modell (I) mit Daten (A): eine Endmasse gibt p >= 0,05 | 35 % |
| PQ2 | [H] Modell (II) mit Daten (A): eine Endmasse gibt p >= 0,05 | 35 % |
| PQ3 | [H] Mit der Zuordnung (C) erreicht mindestens eines der Modelle p >= 0,05 | 45 % |

**Bedeutung (vorab):**
- **PQ1 oder PQ2 trifft ein:** Finns rotierendes Paar traegt die Gitter-Tensoren mit dem Literatur-Intercept und einer Endmasse. Das ist der erste Treffer des Paar-Bilds, unter dem Vorbehalt Look-elsewhere: fuenf Intercepts mal zwei Steigungen sind zehn Kandidaten.
- **Beide verfehlt:** Das Paar-Bild traegt die Gitter-Glueballs auch mit dem Literatur-Intercept nicht. Finns Paar bleibt Bild, nicht Modell.
- **PQ3 allein:** Die Zuordnung der Zustaende entscheidet, nicht das Modell.

## Grenzen (woertlich)

- wie PAAR-REGGE-1: klassisch bei J = 2 bis 4, Gitter synthetisch, 4++ mit Stern
- Look-elsewhere: fuenf Intercepts mal zwei Steigungen sind zehn Kandidaten. Alle zehn werden berichtet.

## Rahmen

- Code-Agent; Code aus paar-regge-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu6. Je Lauf hoechstens 10 min, ein Thread. Zeitbox 90 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
