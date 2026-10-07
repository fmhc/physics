# HUELLEN-LEITER-3: Lagebasierter Test der Sprossenregel jenseits R = 39 (Runde 19)

- Leitung: claude-primary. Karte geschrieben ab 2026-10-02 16:09:35 CEST (date).
- Die Vorhersagen sind **unveraendert** aus HUELLEN-LEITER-2 uebernommen (dort geschrieben ab 15:14:11, vor jeder
  Rechnung).
- Herkunft: HUELLEN-LEITER-2 war nicht auswertbar (K0 verfehlt). Die vorzeichenbasierte Zaehlung mit der Kenngroesse s
  kippte durch die Stabilisierung, die Lagen der stillen Stellen (Nullstellen von W) blieben auf 1e-13 gleich.
  - Lehre: Lagen sind robust, Vorzeichenzaehlungen zerbrechlich.
  - Darum ist dieser Test **lagebasiert**.
- **Offengelegte Kontamination:** In HUELLEN-LEITER-2 endete ein ungewerteter Newton-Lauf bei einer echten stillen Stelle
  mit R = 40,49 (Kurve unbestimmt). Vorhergesagt ist fuer k = 1 die Sprosse 40,51. Diese eine Sprosse wird getrennt
  gewertet.
- Explorativ (v3), Hypothesen [H].

## Vorgehen

- Code wie HUELLEN-LEITER-2 (stabilisierte Kopplung chi < 1e-12 -> 0). Die Lagen sind davon nachweislich unberuehrt.
- **K0' (lagebasiert):** Newton auf W reproduziert 12 bekannte Stellen aus Runde 18 auf 1e-8 (je Kurve k = 0 bis 3 die
  drei mit groesstem R). Dazu der aufgeloeste Rechteck-Umlauf **von W** mit dem Vorzeichen aus Runde 18.
- **Kontrolle der Stabilisierung:** An zwei neuen Stellen wird die Lage mit einer zweiten Variante bestaetigt (chi im
  Inneren glatt und positiv fortgesetzt statt geschnitten), auf 1e-8.
- **Test:**
  - Fuer jede vorhergesagte Sprosse (k = 0 bis 3, je die ersten zwei) Newton auf W, mit Start bei omega^2(R_vorhergesagt)
    und rho aus der Fortsetzung der chi-Kurve k von den Daten aus Runde 18.
  - Angenommen wird eine Stelle, wenn W < 1e-10 konvergiert, sie auf Kurve k liegt (Knotenzahl wie im Vorlaeufer), der
    Rechteck-Umlauf von W auf beiden Stufen aufgeloest +-1 ist und die Stufen auf 1e-6 uebereinstimmen.
  - Abweichung Delta R = R_gefunden - R_vorhergesagt.
  - Findet Newton keine Stelle auf Kurve k innerhalb +-0,5 in R, gilt die Sprosse als nicht gefunden.

## Vorhersagen (aus HUELLEN-LEITER-2, unveraendert)

| Kurve k | vorhergesagte Sprossen R |
|---|---|
| 0 | 39,59 / 42,00 |
| 1 | 40,51 (kontaminiert, getrennt) / 42,62 |
| 2 | 40,24 / 42,36 |
| 3 | 39,77 / 41,93 |

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| P1' | Die 7 unkontaminierten Sprossen liegen je innerhalb +-0,10 um den vorhergesagten R-Wert | 60 % |
| P2' | Der Rechteck-Umlauf von W wechselt entlang jeder Kurve das Vorzeichen (von der letzten Stelle aus Runde 18 zur ersten neuen und weiter) | 85 % |

**Bedeutung (vorab, wie HUELLEN-LEITER-2):**
- Treffen P1' und P2' ein: Die Sprossenregel sagt neue stille Stellen voraus [H].
- Abweichungen > 0,3: Die Regel gilt nur im bisherigen Bereich.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu bis cpu4, je <= 10 min.
- Plan vor dem ersten Lauf einfrieren; Nachtraege nur eingefroren. Zeitbox 90 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
