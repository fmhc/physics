# UEBERGABE-KONFLUENZ-1: Haengt der Zustand nach zwei gleichzeitig faelligen Umklappzuegen von ihrer Reihenfolge ab, mit Feldern? (Runde 48, Church-Rosser fuer Finns Netz)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 11:19:33 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - Finn, 05.10.2026, woertlich: "Und such auch mal in dem subagents nach lambda calculus / church Turing theorem" und "Steckt da unser Spin drin? In der Reihenfolge der Sache?"
  - Kartenvorschlag K1 aus LAMBDA-TURING-L (RUNDE-37/lambda-turing-l/DOSSIER.md, Abschnitt 5), weitgehend woertlich. Zusaetze der Leitung sind mit [Zusatz Leitung] markiert.
- **Projektbefunde [P]:**
  - PACHNER-TAKT-1: Zwei Zeltzuege an Nachbarecken sind ohne Kruemmung vertauschbar (1e-15); mit Kruemmung bleibt D ~ eps (a/L)^2,25. Nur reine Geometrie, keine Felder.
  - LAMBDA-TURING-L, Abschnitt 4.2: Umklappzuege in drei Regimen. Kinetisch hat Delaunay eine eindeutige Normalform; bei grossen Schritten in 3D ist sie nicht eindeutig (Joe); auf dem exakt symmetrischen Netz gilt Konfluenz nur modulo Diagonalwahl (Flip-Flop).
  - Die Reihenfolge der Uebergabe ist im Projekt nicht getestet (grep in TAKT-DYNAMIK-1, HODGE-MASSE-1, UMKLAPP-1 ohne Treffer zur Sache).
  - HODGE-MASSE-1: Im Umklapp-Kasten ist nur A1R1 bzw. A2R1 positiv definit. Die Lund-Regge-Masse (Form B) ist dort nicht startbar (28 bis 46 negative Richtungen).
- Kennzeichen: [M], [E], [P], [S], [L], [H], [ES].

## Bau (aus K1)

- Vorhandener Code aus TAKT-DYNAMIK-1 bzw. HODGE-MASSE-1, Glas-Netz.
- Zwei benachbarte Flaechen werden durch kleine Eckverschiebung gleichzeitig nicht lokal Delaunay. Dafuer zwei Ueberlappungsarten: gemeinsames Tetraeder und gemeinsame Kante.
- Uebergabe in der Reihenfolge XY und YX, je mit und ohne Felder (Skalar-Amplitude 0, 1e-3, 1e-2), Lesart R (Projektion) und P.
- Messgroessen:
  - Delta_s = Abstand der Endzustaende je Sektor (q, p, phi, pi, A, E), relativ
  - Delta_H = abs(H_XY - H_YX)/H
  - Gauss-Rest
- Beschreibend: Anteil der Zeitschritte mit mindestens zwei faelligen Zuegen in einem vorhandenen Lauf (h = 0,5 gegen 0,25).
- Kontrolle Zeitumkehr: Laeuft die Bahn nach dem Zugpaar mit umgekehrten Impulsen zurueck, muss sie die Zuege in umgekehrter Reihenfolge wieder aufheben.

## Ableitbarkeitsprobe

- **Vorab ableitbar [M]:**
  - (a) Disjunkte Traeger vertauschen exakt.
  - (b) In allgemeiner Lage ist die kombinatorische Endzerlegung nach "umklappen bis Delaunay" in beiden Reihenfolgen dieselbe (eindeutige Delaunay-Zerlegung). Die Kombinatorik ist also nur Kontrolle.
  - (c) Ist die Uebergabe je Zug linear und invertierbar auf ihrem Traeger und vertauschen die beiden Abbildungen, dann ist Delta = 0.
  - **(d) [Zusatz Leitung]:** Ist die Feld-Uebergabe bei fester Geometrie linear in den Feldern, dann ist Delta_Feld genau proportional zur Amplitude (Steigung 1). UK2 ist deshalb nur noch eine Kontrolle der Linearitaet; die Wahrscheinlichkeit ist gegenueber dem Entwurf angehoben. Abweichungen kommen nur aus Rueckwirkung der Felder auf die Geometrie.
- **Nicht ableitbar:**
  - Groesse von Delta_Feld je Ueberlappungsart
  - ob R eine groessere Reihenfolgespur hinterlaesst als P
  - Unterschied Form A gegen B
  - Haeufigkeit doppelter Ereignisse je h

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| UK0 | Kontrolle [M]: disjunkte Zuege Delta < 1e-12; ohne Felder kombinatorisch gleiche Endzerlegung | 90 % |
| UK1 | [H] Lesart R, Feldamplitude 1e-3: Delta_Feld > 1e-6 relativ fuer mindestens eine Ueberlappungsart | 60 % |
| UK2 | Kontrolle [M, Zusatz Leitung]: Delta_Feld waechst linear mit der Feldamplitude (Steigung 0,9 bis 1,1 zwischen 1e-3 und 1e-2) | 85 % |
| UK3 | [H] Lesart R hat eine mindestens 10-mal groessere Reihenfolgespur (Delta_Feld) als P | 35 % |
| UK4 | [H] Form A und Form B unterscheiden sich in Delta_p um mehr als Faktor 2. Ist Form B im Kasten nicht startbar, lautet das Urteil "nicht entscheidbar" | 40 % |

**Bedeutung (vorab):**
- **UK1 trifft ein:** Die Uebergabe beim Umklappen ist nicht Church-Rosser. Die Reihenfolge gleichzeitiger Zuege hinterlaesst eine Spur in den Feldern. Die Grundgleichung braucht dann eine Reihenfolgeregel oder eine Uebergabe, die vertauscht (GRUNDGLEICHUNG-SKIZZE, Abschnitt 6).
- **UK1 verfehlt:** Die Uebergabe ist bei kleinen Feldern reihenfolgefest. Dann bleibt als einzige bekannte Reihenfolgespur die Kruemmung (PACHNER-TAKT-1).
- **UK3 trifft ein:** Die Projektion (Lesart R) ist die Quelle der Reihenfolgeabhaengigkeit; das spricht fuer P.
- **[Zusatz Leitung]:** Mit Spin hat das nichts unmittelbar zu tun. Die Karte prueft nur die Reihenfolge, Finns zweite Haelfte der Frage.

## Rahmen

- Code-Agent. Code aus RUNDE-37/takt-dynamik-1/code bzw. RUNDE-37/hodge-masse-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (CPU-Rechnung). Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
