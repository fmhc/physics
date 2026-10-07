# HUELLEN-UHR: Schwingt eine stille Stelle mit Huelle im Zeitlauf wirklich ohne Abstrahlung? (Runde 18)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-02 12:44:17 CEST (date), vor jeder Rechnung.
- Herkunft:
  - STILLE-ZWEIFELD fand 15 stille Stellen im Zweifeldmodell M2.
  - ZWEIFELD-NACHBAU fand blind genau die 9 im Fenster 0,83 bis 0,91, allerdings nachtraeglich.
  - Beide arbeiten im Frequenzbereich (lineare Streurechnung), mit derselben Methodenfamilie. Der chi-Teil hat keine
    unabhaengige Kontrolle.
- Diese Karte prueft im **Zeitbereich** mit einem unabhaengig geschriebenen Loeser. Zur Physik vergleiche Codex'
  Q-Ball-Uhr (Peerbus 02.10. 09:54 CEST): Einfeld-BIC, Periode 2 pi/rho, Nullarm ohne Ticks.
- Explorativ (v3), Hypothesen [H].

## Modell und Lauf

- **Modell M2:** psi komplex, chi reell, U = (1/4)(chi^2 - 1)^2 + (1 + chi^2) S - S^2 + S^3/2.
  - Radial, 3D, l = 0: psi_tt = Lap psi - U_S psi und chi_tt = Lap chi - U_chi.
  - Regularitaet bei r = 0, Absorber (Schwammschicht) aussen.
  - Messkugel r_m innerhalb des Absorbers fuer den abgestrahlten Energiefluss in psi und chi.
- **Hintergrund:** Q-Ball mit Huelle bei omega^2 einer stillen Stelle. Zwei Stellen werden gerechnet:
  - S-a: 0,86085981 / 1,06976351, rho-Familie ~ 1,07
  - S-b: 0,84743426 / 1,33956049, rho-Familie ~ 1,34
- **Anregung:**
  - (i) BIC: die lineare Eigenmode der stillen Stelle (a, b, c aus der Streurechnung; Code aus RUNDE-17/stille-zweifeld
    oder RUNDE-17/zweifeld-nachbau darf dazu benutzt werden), Amplitude eps.
  - (ii) Kontrolle "nicht still": dieselbe Modenform, aber vom Hintergrund bei verschobenem omega^2 (+0,01), wo die Stelle
    nicht still ist.
  - (iii) Kontrolle "generisch": ein glatter radialer Stoss in chi derselben Energie.
  - (iv) Nullarm: Hintergrund ohne Anregung.
- **Messung (je eps in {0,002; 0,005}, zwei Gitter):**
  - Anteil der Anregungsenergie, der bis T abgestrahlt ist.
  - Abklingrate der Modenamplitude.
  - Frequenz der Dichte-Ticks im Zentrum.
  - Erhaltung von Energie und Ladung inklusive Absorberfluss.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| H1 | Nullarm: keine Ticks; Energie- und Ladungsbilanz auf < 1e-6 | 95 % |
| H2 | (i) BIC: Dichte-Ticks mit Periode 2 pi/rho auf 1e-3 | 85 % |
| H3 | (i) gegen (ii): abgestrahlter Anteil bis T bei (i) mindestens 30-mal kleiner als bei (ii), bei beiden eps und beiden Stellen | 65 % |
| H4 | (i): Der Rest der Abstrahlung skaliert wie eps^4 (nichtlinear), bei (ii) wie eps^2 (linear) | 55 % |
| H5 | (iii) generischer Stoss strahlt in den ersten Perioden stark ab (> 50 % der Anregungsenergie bis T) | 70 % |

**Bedeutung (vorab):**
- Treffen H2 und H3 ein: Die Huellen-Stellen sind im Zeitbereich unabhaengig bestaetigt. Der chi-Teil der
  Streurechnung stimmt, und die Huelle macht den Ball zu einer Uhr ohne Energieverlust in erster Ordnung [H].
- Trifft H3 nicht ein: Die Frequenzbereichs-Stellen sind fraglich. Suche die Ursache (Modenform, Absorber, Kanal c).

## Rahmen

- Code-Agent, eigener Zeitloeser (numpy). Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu2, je <= 10 min.
- Plan vor dem ersten Lauf einfrieren; Nachtraege nur eingefroren. Zeitbox 120 min.
- Lokal kein python, awk oder bc; Syntax per py_compile auf der .69.
