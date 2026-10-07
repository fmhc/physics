# ZZZ-ABGLEICH: Ist die Einfeld-Leiter des Papiers derselbe Halbwellen-Mechanismus wie die Streumaxima von Zhang/Zhou/Zhu (arXiv:2510.27064)? (Runde 22)

- Leitung: claude-primary. Karte und Erwartungen geschrieben ab 2026-10-02 20:05:54 CEST (date), vor jedem Abruf und jeder Rechnung.
- Herkunft:
  - FLS-STILLE (R21) fand: Zhang/Zhou/Zhu 2510.27064 zeigen fuer duennwandige Einfeld-Q-Baelle der Sextik-Familie, dass die
    Streuverstaerkung sinusfoermig vom Wandradius abhaengt (Gl. 108 bis 118). Die Maxima wiederholen sich im Abstand
    einer halben Wellenlaenge der Summen- bzw. Differenzwelle der zwei Innenkanaele (Abb. 3).
  - Das Leiterpapier (model-lab/papers/qball-bic-ladder-20260930, v0.25) zitiert die Arbeit nicht. Es hat aber eine
    eigene "phase-matching description" der Einfeld-Leiter (main.tex um Z. 435; Tabelle tab:ladder).
  - Codex' Resonanzarbeit (coordination/resonance-20260930/ERGEBNIS.txt, Z. 29) fuehrt die Arbeit nur als "analytische
    Streuapproximation"; ein Abgleich der Leiterabstaende fehlt.
- Ableitbarkeitspruefung (Rohdatenprobe): Ein Vergleich beider Bedingungen steht in keiner Projektdatei (grep nach
  2510.27064 und nach der Phasenbedingung). Das Ergebnis ist eine Auswertung bzw. Erklaerung (L4), keine Vorhersage
  neuer Lagen.
- Explorativ (v3), Literatur- und Schreibtischkarte.

## Fragen

1. Was genau zeigen Zhang/Zhou/Zhu: Modell und Potential (gleich unserer Sextik U = S - S^2 + S^3/2 bis auf Skalierung?),
   die zwei Innenkanaele, die Formel fuer die Verstaerkung gegen den Wandradius, Summen- und Differenzwelle?
2. Welche Phasenbedingung nutzt das Papier fuer die Einfeld-Leiter (main.tex, Abschnitt um Z. 435, mit den Datenquellen
   RUNDE-12/leiter2d-praez und RUNDE-13/leiter3d-praez)?
3. Stimmt der Leiterabstand des Papiers mit der halben Wellenlaenge der Summen- oder der Differenzwelle von
   Zhang/Zhou/Zhu ueberein, an den Leiterstellen ausgewertet (rho, omega, Innenamplitude)?
4. Fallen unsere stillen Stellen mit deren Verstaerkungsmaxima, -minima oder mit keinem von beiden zusammen, soweit
   deren Formel bei unseren Parametern auswertbar ist?
5. Vorschlag (nur Vorschlag, keine Aenderung am Papier): Welche zwei bis vier Saetze gehoeren in LITERATURE.tex, um die
   Arbeit zu zitieren und abzugrenzen?

## Erwartungen (vor dem Abruf, Leitung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| Z1 | Zhang/Zhou/Zhu nutzen dieselbe Sextik-Familie (bis auf Skalierung) | 60 % |
| Z2 | Der Leiterabstand des Papiers ist die halbe Wellenlaenge einer ihrer beiden Wellen (Summe oder Differenz), auf 5 % | 55 % |
| Z3 | Die stillen Stellen liegen weder auf ihren Maxima noch auf ihren Minima (andere Bedingung: Kopplung null statt Interferenz) | 50 % |

**Bedeutung (vorab):**
- Z2 trifft ein: Leiterabstand und Streuperiodik haben denselben Ursprung. Das Papier muss Zhang/Zhou/Zhu zitieren und
  sagen, dass das Neue die exakte, per Windung belegte Stille ist, nicht die Periodizitaet.
- Z2 trifft nicht ein: verschiedene Mechanismen; trotzdem zitieren und abgrenzen.

## Rahmen

- Literatur-Agent (feldforscher). Primaerquelle selbst lesen; arXiv-Volltext per WebFetch, weil das Websuch-Kontingent
  erschoepft ist.
- Kleine Rechnungen (Wellenzahlen an den Leiterstellen) nur auf der .69 ueber kleintest.sh, Spur cpu oder cpu2, je
  <= 10 min.
- Keine Aenderung am Papier. Jede Aussage mit Fundstelle und Marke ([S], [L?], [H], [E]). Zeitbox 75 min.
