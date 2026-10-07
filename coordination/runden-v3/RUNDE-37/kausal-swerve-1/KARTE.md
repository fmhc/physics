# KAUSAL-SWERVE-1: Bremst ein Raumzeit-Netz ohne Ruhesystem ein Teilchen, oder laesst es seine Geschwindigkeit nur zittern? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 04:33:49 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - ZUFALLS-REIBUNG-1: Ein raeumlich zufaelliges Netz bremst Q-Baelle und zeichnet damit ein Ruhesystem aus.
  - KAUSAL-1: Ein zufaelliges Raumzeit-Netz (Kausalmenge) hat kein Ruhesystem, aber keine festen Nachbarn.
  - Frage fuer Finns Weiche: Was spuert ein Teilchen, das auf so einem Netz von Punkt zu Punkt laeuft?
  - Literatur [L]: "Swerves" (Dowker/Henson/Sorkin 2004). Teilchen auf Kausalmengen diffundieren im Impuls,
    Lorentz-invariant. Beobachtungen begrenzen das [L: Kaloper/Mattingly 2006].
  - Ideenpool K1.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Netz:** Poisson-Streuung von N Punkten im kausalen Diamanten der 1+1-Raumzeit, (u, v) in [0,1]^2, wie KAUSAL-1.
  Links per laufendem Minimum (KAUSAL-1/code/kausal.py).
- **Laeufer:** startet an einem Punkt nahe der unteren Spitze mit Rapiditaet eta_0.
  - Je Schritt waehlt er unter den zukuenftigen Links seines Punktes denjenigen, dessen Rapiditaet eta_link =
    (1/2) ln(dv/du) der eigenen am naechsten ist. Nur Links mit Eigenzeit tau <= tau_max (fest, etwa 3/sqrt(N)).
  - Dann gilt eta := eta_link: Die Bewegung folgt dem gewaehlten Strich.
- **Erwartung:**
  - [M] Kein Bezugssystem ist ausgezeichnet. Die mittlere Aenderung von eta ist 0, fuer jedes eta_0 (keine Reibung zu
    einem Ruhesystem).
  - [H/L] Die Streuung waechst wie bei einer Irrfahrt: Var(eta_n - eta_0) ~ n sigma^2, mit gleichem sigma^2 fuer alle
    eta_0.
  - [M, folgt daraus] Die mittlere Energie <cosh eta> steigt in jedem Bezugssystem: Das Netz "heizt" statt zu bremsen.
- **Gegenstueck:** ZUFALLS-REIBUNG-1 (raeumlich zufaellig) bremste zu einem Ruhesystem. Der Unterschied ist das
  Kennzeichen der zwei Wege der Weiche.

## Test (Code-Agent)

- N = 16 000 und 64 000, je mehrere Saaten.
- Je eta_0 in {-1; 0; 1} mindestens 200 Laeufer, Startpunkte nahe der unteren Spitze, hoechstens 100 Schritte bzw. bis
  zum oberen Rand.
- Links nur fuer die besuchten Punkte berechnen (O(N) je Schritt).
- **Messgroessen:** <eta_n - eta_0>, Var(eta_n - eta_0) gegen n, <cosh eta_n>, Schrittlaenge in Eigenzeit; Randeffekte
  (Laeufer nahe dem Rand ausschliessen und offenlegen).
- **Kontrolle:** Linkzahl gegen KAUSAL-1 (ln N - 1,42 je Punkt in die Zukunft).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KS0 | Kontrolle: Zukunftslinks je Punkt (fern vom Rand) = ln N - 1,42 +- 0,15 bei N = 64 000 | 85 % |
| KS1 | Keine Reibung: abs(<eta_n - eta_0>) <= 3 Standardfehler bei n = 50, fuer eta_0 = -1, 0, 1 | 75 % |
| KS2 | Irrfahrt: Var(eta_n - eta_0) linear in n (R^2 > 0,98 fuer n = 5 bis 50); die Steigung sigma^2 ist fuer eta_0 = -1, 0, 1 gleich innerhalb 15 % | 55 % |
| KS3 | Heizen: Fuer eta_0 = 0 steigt <cosh eta_n> mit n (bei n = 50 groesser als bei n = 5, ueber 3 Standardfehler) | 65 % |

**Bedeutung (vorab):**
- **KS1 bis KS3 treffen ein:** Ein Raumzeit-Netz ohne Ruhesystem bremst nicht. Es laesst die Geschwindigkeit eines
  Teilchens zittern, gleich in jedem Bezugssystem, und heizt es dadurch langsam auf.
  - Das ist das Gegenstueck zur Reibung im raeumlichen Zufallsnetz (ZUFALLS-REIBUNG-1).
  - Die Staerke des Zitterns pro Netzschritt begrenzt, wie grob das Netz sein darf [L: Swerve-Schranken].
- **KS2 verfehlt (sigma^2 haengt von eta_0 ab):** Die Laeuferregel selbst zeichnet etwas aus (z. B. der Rand des
  Diamanten); dann ist sie zu verbessern.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
