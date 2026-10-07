# HUELLEN-LEITER-2: Sagt die Sprossenregel die naechsten stillen Stellen voraus? (Runde 19)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 15:14:11 CEST (date), vor jeder Rechnung.
- Herkunft: HUELLEN-LEITER (RUNDE-18/huellen-leiter/ERGEBNIS.md) fand 88 stille Stellen auf 10 chi-Kurven bis zum
  Huellenradius R = 39.
  - Sprossen je Kurve fast aequidistant in R.
  - Schreibtisch-Mechanismus [H]: Delta R ~ pi/k_innen; neue Kurve etwa alle 3,9 bis 4,07 in R.
  - Ab R ~ 40 wurde die Kenngroesse rundungsbestimmt (chi < 1e-16 im Inneren).
- Diese Karte ist ein **vorab gewerteter Vorhersagetest** jenseits von R = 39.
- Explorativ (v3), Hypothesen [H].

## Vorgehen

- Code wie HUELLEN-LEITER, mit **stabilisierter Kopplung**: Dort, wo chi < 1e-12 ist, werden die chi-Kopplungsterme
  exakt null gesetzt (Vorschlag des Vorlaeufers).
- **Kontrolle K0:** Der stabilisierte Code muss alle 88 bekannten Stellen (R <= 39) mit unveraenderter Lage (<= 1e-8) und
  gleichem Umlauf wiederfinden. Sonst ist er nicht auswertbar.
- **Suche:** R von 39 bis 46 (omega^2 entsprechend, Hintergrund bis 0,74 sauber), alle Kurven, beide Gitterstufen. Die
  Zellen-Umlauf-Zaehlung wie im Vorlaeufer, mit Stichproben des Rechteck-Umlaufs.

## Vorhersagen (vor jeder Rechnung; aus der Tabelle des Vorlaeufers, letzte Stelle je Kurve plus kleinster gemessener Abstand)

| Kurve k | letzte bekannte Stelle R | Abstand (min, gemessen) | vorhergesagte naechste Sprossen R |
|---|---|---|---|
| 0 | 37,18 | 2,410 | 39,59 / 42,00 / 44,41 |
| 1 | 38,40 | 2,108 | 40,51 / 42,62 / 44,72 |
| 2 | 38,11 | 2,127 | 40,24 / 42,36 / 44,49 |
| 3 | 37,61 | 2,159 | 39,77 / 41,93 / 44,09 |

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| P0 | K0 bestanden: alle 88 bekannten Stellen unveraendert | 90 % |
| P1 | Fuer k = 0 bis 3 liegt jede der ersten zwei neuen Sprossen innerhalb +-0,10 um den vorhergesagten R-Wert (8 Stellen) | 60 % |
| P2 | Der Umlauf wechselt weiter von Sprosse zu Sprosse das Vorzeichen | 85 % |
| P3 | Eine neue Kurve k = 10 beginnt zwischen R = 40,5 und 42,5 (Kurvenabstand 3,9 bis 4,1 nach k = 9 bei 37,65) | 55 % |
| P4 | Die stabilisierte Kopplung beseitigt den gemeinsamen Vorzeichenwechsel aller Kurven ab R ~ 40 | 75 % |

**Bedeutung (vorab):**
- Treffen P1 und P2 ein: Die Sprossenregel sagt neue stille Stellen voraus, die Leiter setzt sich regelmaessig fort.
  Das stuetzt den Mechanismus "Vorzeichenwechsel der Kopplung je halbe Wellenlaenge" [H].
- Verfehlt P1 deutlich (Abweichungen > 0,3): Die Regel gilt nur im bisherigen Bereich; dann den Grund suchen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu bis cpu4, je <= 10 min.
- Plan vor dem ersten Lauf einfrieren; Nachtraege nur eingefroren. Zeitbox 120 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
