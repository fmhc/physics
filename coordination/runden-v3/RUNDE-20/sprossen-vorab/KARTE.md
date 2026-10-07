# SPROSSEN-VORAB: Vorab gewerteter Test der Sprossenregel mit neuen Sprossen (Runde 20)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 17:07:29 CEST (date), vor jeder Rechnung dieser Karte.
- Herkunft:
  - HUELLEN-LEITER-3 (Runde 19): formal nicht bestanden (Pflichtbedingung Knotenzahl konventionsabhaengig).
    Nachtraeglich lagen alle 8 Sprossen auf <= 0,018.
  - Die Fremdstimme verlangt mit Auflage L4 einen neuen Test mit neuen Sprossen:
    - Kurve nur ueber Rang und Stetigkeit
    - jede Pflichtbedingung vor dem Einfrieren mit genau dem Testcode an bekannten Stellen pruefen
- Explorativ (v3), Hypothesen [H].

## Vorgehen

- Code wie HUELLEN-LEITER-3 (Lagen aus der Schnittvariante, Umlauf aus der Fortsetzungsvariante, Newton auf W,
  Rechteck-Umlauf von W). Hintergruende bis R = 46,5 sauber (HUELLEN-LEITER-2).
- **Annahme einer Sprosse:**
  - Newton auf W konvergiert (|W| <= 1e-9, begruendet in HUELLEN-LEITER-3), mit Rangabfall.
  - Kurvenzuordnung nur ueber **Stetigkeit von rho(R)** entlang der Kurve, d. h. Abstand zur glatten Fortsetzung kleiner
    als ein Zehntel des Abstands zur Nachbarkurve, und Rang.
  - Rechteck-Umlauf von W auf beiden Stufen aufgeloest +-1.
  - Stufen auf 1e-6.
  - Newton-Starts bei R_vorhergesagt und rho aus der Kurvenfortsetzung; Nachstarts bei +-0,25 in R erlaubt.
  - Gefunden heisst: Die angenommene Sprosse liegt innerhalb +-0,5 in R.
- **Pflicht vor dem Einfrieren (L4):** Den Testcode samt Annahmekriterium an bekannten Stellen laufen lassen, an den 8
  Sprossen aus HUELLEN-LEITER-3 und an der jeweils letzten Stelle aus Runde 18 fuer k = 4 bis 7. Alle muessen angenommen
  werden. Sonst Kriterium vor dem Einfrieren berichtigen und erneut pruefen.

## Vorhersagen (vor jeder Rechnung dieser Karte)

Lineare Fortsetzung aus den letzten zwei bekannten Sprossen je Kurve (HUELLEN-LEITER-3 fuer k = 0 bis 3; Runde 18 mit
kleinstem gemessenem Abstand fuer k = 4 bis 7):

| k | bekannte Sprossen R | vorhergesagt R (Toleranz) |
|---|---|---|
| 0 | 39,594 / 42,004 | 44,414 (+-0,06) |
| 1 | 40,506 / 42,613 | 44,720 (+-0,06) |
| 2 | 40,229 / 42,351 | 44,473 (+-0,06) |
| 3 | 39,765 / 41,912 | 44,059 (+-0,06) |
| 4 | 36,92 (Abstand 2,206) | 39,13 / 41,33 (+-0,12) |
| 5 | 38,26 (Abstand 2,248) | 40,51 / 42,76 (+-0,12) |
| 6 | 37,19 (Abstand 2,322) | 39,51 / 41,83 (+-0,12) |
| 7 | 38,27 (Abstand 2,379) | 40,65 / 43,03 (+-0,12) |

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| V0 | Pflichtpruefung L4 bestanden (alle bekannten Stellen angenommen) | 85 % |
| V1 | k = 0 bis 3: alle 4 Sprossen innerhalb +-0,06 | 70 % |
| V2 | k = 4 bis 7: mindestens 7 von 8 Sprossen innerhalb +-0,12 | 60 % |
| V3 | Der Umlauf wechselt entlang jeder Kurve weiter das Vorzeichen | 85 % |

**Bedeutung (vorab):**
- Treffen V1 bis V3 ein: Die Sprossenregel sagt neue stille Stellen vorab gewertet voraus [H, im Modell gestuetzt].
- Bei Abweichungen > 0,3: Die Regel bricht jenseits R ~ 42 zusammen; Grund suchen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu bis cpu4, je <= 10 min.
- Plan nach der Pflichtpruefung einfrieren; Nachtraege nur eingefroren. Zeitbox 90 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
