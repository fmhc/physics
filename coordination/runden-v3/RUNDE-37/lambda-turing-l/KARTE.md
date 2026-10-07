# LAMBDA-TURING-L: Was sagen Lambda-Kalkuel, Church-Rosser und die Church-Turing-These ueber Finns Netz? (Runde 48, Finns Auftrag)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 10:46:39 CEST (date), vor jedem Abruf.
- **Herkunft:** Finn, 05.10.2026, Eingang vor 10:46, woertlich: "Und such auch mal in dem subagents nach lambda calculus / church Turing theorem".
- **Projektbefunde [P]** (nicht als neu fuehren):
  - **TAKT-UMBENENNUNG-L** (RUNDE-37/takt-umbenennung-l/DOSSIER.md):
    - Hojman/Kuchar/Teitelboim 1976: Weg-Unabhaengigkeit (Faltungsfreiheit der Zeitscheiben), Lokalitaet und Ordnung der Gleichungen legen Einsteins Hamilton-Funktion samt lambda = 1 fest, bis auf G und Lambda (nach Sekundaerquellen).
    - Das Wolfram-Bulletin "Confluence and Causal Invariance" war dreimal nicht abrufbar (E6 offen).
  - **PACHNER-TAKT-1 / TAKT-KOMMUTATOR-1** (RUNDE-42): Zwei Zeltzuege an Nachbarecken sind ohne Kruemmung vertauschbar (1e-15). Mit Kruemmung waechst der Unterschied linear mit eps und faellt wie (a/L)^2,25. Ein globaler Takt hebt ihn nicht auf.
  - **WOLFRAM-SCAN-L** (RUNDE-41): Kausalinvarianz nach Gorard als diskrete allgemeine Kovarianz; Lorentz-Invarianz nur durch Vergroeberung; mikroskopisch verstecktes Ruhesystem; kein Spin 1/2, kein 3+1.
  - **RUNDE-22** (geometrie-stand/ERGEBNIS.md): Die Spektralluecke ist unentscheidbar (Cubitt/Perez-Garcia/Wolf; Bausch u. a. in 1D) [L?].
  - **RAUM-GAS-L** (RUNDE-48): Navier-Stokes-Blow-up-Beweis (OpenAI, Lean); Folgearbeiten ordnen ihn den Clay-Faellen (C) und (D) zu.
  - **GRUNDGLEICHUNG-SKIZZE-v2** (RUNDE-48), Abschnitt 4: Die Algebra der Zwangsbedingungen (erste Klasse = Weg-Unabhaengigkeit) ist offen.
- Kennzeichen: [M], [S] an der Quelle gelesen (mit Abschnitt, Gleichung oder Seite), [S Abstract], [L], [P], [ES], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar bzw. bekannt [M/L]:**
  - Konfluenz (Church-Rosser) eines Ersetzungssystems heisst: Verschiedene Reihenfolgen lassen sich wieder zusammenfuehren. Fuer Finns Netz ist das die Frage, ob die Reihenfolge der Umklapp- bzw. Zeltzuege (der oertliche Takt) das Ergebnis aendert.
  - Das ist die diskrete Fassung der Weg-Unabhaengigkeit (HKT) [P, TAKT-UMBENENNUNG-L]. PACHNER-TAKT-1 hat sie fuer zwei Nachbarecken schon gemessen: Mit Kruemmung gibt es eine Nicht-Vertauschbarkeit der Ordnung eps (a/L)^2,25 [P].
  - Lambda-Kalkuel ist nicht umkehrbar (Beta-Reduktion verliert Information). Unsere Netzdynamik ist hamiltonsch, also umkehrbar. Ein Uebertrag braucht umkehrbare Ersetzung [M].
- **Nicht ableitbar:**
  - ob es Arbeiten gibt, die die Hyperflaechen-Verformungsalgebra ausdruecklich mit Church-Rosser bzw. Konfluenz verbinden
  - was genau Gandy, Geroch/Hartle und Nabutovsky/Ben-Av zeigen und unter welchen Annahmen
  - welche Konfluenz- und Erreichbarkeitsaussagen es fuer 3D-Umklappzuege gibt
  - Stand 2024 bis 2026 zur physikalischen Church-Turing-These in der Quantengravitation
- **Kennzahlen-Abgleich:** keine neue Rechnung; PACHNER-TAKT-1 liefert die einzige Projektzahl zur Reihenfolge.

## Fragen

1. **Church-Rosser:** genaue Aussage (Konfluenz, Eindeutigkeit der Normalform, keine starke Normalisierung) und ihre Uebertragung auf Ersetzungssysteme von Graphen und Zerlegungen.
2. **Umklappzuege als Ersetzungssystem:**
   - 2D: Erreicht der Lawson-Algorithmus Delaunay immer?
   - 3D: Kann er stecken bleiben (Joe 1989/1991)?
   - Zusammenhang der Pachner-Graphen und berechenbare Schranken (Mijatovic fuer S^3)
   - Kinetisches Delaunay in 3D: Reichen 2-3- und 3-2-Zuege bei allgemeiner Bewegung?
3. **Konfluenz gegen Kausalinvarianz gegen Weg-Unabhaengigkeit:**
   - Wolfram-Bulletin "Confluence and Causal Invariance" (2020) erneut versuchen: curl mit Browser-User-Agent, web.archive.org, PDF-Fassung.
   - Gorard 2020 (Kausalinvarianz und Kovarianz); gibt es eine ausdrueckliche Bruecke zu Dirac/HKT?
4. **Physikalische Church-Turing-These:**
   - Gandy 1980 ("Church's thesis and principles for mechanisms")
   - Deutsch 1985
   - Pour-El/Richards (Wellengleichung mit berechenbaren Daten, nicht berechenbare Loesung)
   - Geroch/Hartle 1986 (Berechenbarkeit und 4-Mannigfaltigkeiten)
   - Nabutovsky/Ben-Av 1993 (Nichtberechenbarkeit bei dynamischen Triangulierungen)
   - Arbeiten 2024 bis 2026 zur Berechenbarkeit in Quantengravitation bzw. diskreter Raumzeit
   - Tao 2016 (Fluessigkeits-Computer als Weg zum Navier-Stokes-Blow-up); Cardona u. a. 2021 (Turing-vollstaendige Euler-Stroemungen); Bezug zum Blow-up aus RAUM-GAS-L?
5. **Lambda-Chemie und Entstehen:**
   - Fontana/Buss 1994 (AlChemy: Lambda-Ausdruecke als kuenstliche Chemie, selbsterhaltende Organisationen)
   - Aguera y Arcas u. a. 2024 (Selbstreplikatoren aus zufaelligen Programmen) und Nachfolger
   - Gibt es umkehrbare bzw. energieerhaltende Varianten (umkehrbare Zellularautomaten, Margolus; umkehrbare Ersetzung)?
6. **Gegensweep:**
   - Argumente, dass Church-Turing fuer Physik nichts Pruefbares sagt
   - Kritik an Wolframs Kausalinvarianz als Kovarianz
   - 24-Monats-Suche

## Vorhersagen (vor jedem Abruf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LT1 | [L] Kontrolle: Church/Rosser 1936: Beta-Reduktion im ungetypten Lambda-Kalkuel ist konfluent. Die Normalform ist eindeutig, falls es sie gibt; der Kalkuel ist nicht stark normalisierend. | 90 % |
| LT2 | [L] Gandy 1980 beweist: Jede diskrete, deterministische Maschine, die seine Prinzipien I bis IV erfuellt (darunter oertliche Kausalitaet mit begrenzter Ausbreitung), berechnet nur Turing-berechenbare Funktionen. | 85 % |
| LT3 | [L] Geroch/Hartle 1986: Weil 4-Mannigfaltigkeiten nicht algorithmisch klassifizierbar sind (Markov 1958), kann eine Summe ueber 4D-Topologien in der Quantengravitation nicht berechenbar sein. Bei fester Topologie entfaellt dieses Argument. | 75 % |
| LT4 | [L] In 3D kann der Lawson-Umklapp-Algorithmus aus einer beliebigen Zerlegung vor Delaunay stecken bleiben (Joe), in 2D nicht. Die Pachner-Graphen von 3D-Zerlegungen sind zusammenhaengend, mit berechenbarer Schranke fuer S^3 (Mijatovic). | 65 % |
| LT5 | [L?] Das Wolfram-Bulletin unterscheidet Konfluenz (gleiche Endzustaende) von Kausalinvarianz (isomorphe Kausalgraphen) und verbindet nur Letztere mit allgemeiner Kovarianz. | 60 % |
| LT6 | [H] Mindestens eine Arbeit verbindet die Hyperflaechen-Verformungsalgebra (Dirac, HKT) ausdruecklich mit Konfluenz bzw. Kausalinvarianz eines Ersetzungssystems. | 40 % |
| LT7 | [L] In Lambda- bzw. Programm-Suppen entstehen ohne Vorgabe selbsterhaltende Organisationen (Fontana/Buss 1994) bzw. Selbstreplikatoren (Aguera y Arcas u. a. 2024). Eine umkehrbare, energieerhaltende Variante mit demselben Befund ist nicht bekannt. | 55 % |

**Bedeutung (vorab):**
- **LT2 trifft ein:** Finns Netz ist mit endlicher Genauigkeit eine Gandy-Maschine. Es kann nicht mehr berechnen als ein Computer, und es laesst sich im Prinzip exakt simulieren. Das ist eine saubere Einordnung, keine neue Physik.
- **LT3 trifft ein:** Solange die Zuege die Topologie nicht aendern, gilt das Argument nicht. Topologieaenderung (Geonen, Finns Spin-Frage) braeuchte in 4D eine Begrenzung, sonst droht Nichtberechenbarkeit.
- **LT4 und LT6:**
  - Konfluenz der Umklappregeln ist die Ersetzungssprache fuer die Weg-Unabhaengigkeit, also fuer die erste Klasse der Hamilton-Regel (GRUNDGLEICHUNG-SKIZZE-v2, Abschnitt 4).
  - Die Nicht-Vertauschbarkeit ~ eps (a/L)^2,25 aus PACHNER-TAKT-1 waere dann "Church-Rosser bis auf Gitterkorrekturen".
  - Daraus folgt ein moeglicher Test fuer Fassung 2: Konfluenz der Zuege in Form A gegen Form B.
- **LT7 trifft ein:** Lambda-Suppen sind ein Muster fuer Finns "emergente Dynamik". Sie sind aber nicht umkehrbar; uebertragbar ist nur eine umkehrbare Variante [H].

## Rahmen

- feldforscher nach Feld-Regeln:
  - Arbeitsdatei ARBEITSFELD.md, Ergebnis DOSSIER.md, beide in diesem Kartenordner.
  - Erwartung vor jedem Abruf, Gegensweep, Erwartungsverstoesse, Negativliste.
- Hoechstens 20 Abrufe, Zeitbox 90 min. Keine Rechnung.
- Literatur, keine Messdatenbestaetigung.
