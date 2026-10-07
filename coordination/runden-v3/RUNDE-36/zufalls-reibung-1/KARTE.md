# ZUFALLS-REIBUNG-1: Gleitet ein Q-Ball reibungsfrei durch ein ungeordnetes Netz? (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 01:02:23 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Gedankenexperiment GE5 (RUNDE-36/GEDANKENEXPERIMENTE.md): Ein ungeordnetes Netz kauft Richtungsfreiheit
    (ZUFALLSNETZ-1) mit Reibung.
  - Kausalmengen sagen fuer zufaellig diskrete Raumzeit eine Impulsdiffusion voraus ("swerves", Dowker/Henson/Sorkin
    2004 [L]).
  - Finns Netzbild (Schaum statt Kristall).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Modell:** M1 in 1D auf feinem Gitter (h = 0,1, kontinuumsnah; Code-Basis RUNDE-35/qball-gitter-1/), ohne aeussere
  Kraft. Unordnung als zufaellige oertliche Masse: U_n(S) = (1 + sigma eta_n) S - S^2 + S^3/2, eta_n unabhaengig
  normalverteilt.
  - Ein Q-Ball (omega^2 = 0,7) wird per Lorentz-Boost mit Anfangsschnelle v gestartet.
- **Mechanismus** [H]: Im Ruhesystem des Balls sieht die ruhende Unordnung wie eine zeitabhaengige Stoerung aus, mit
  Frequenzen ~ v q. Abstrahlen kann der Ball nur Quanten mit Energie >= 1 (Massenluecke); er bindet seine mit omega < 1.
  - Ein abgestrahltes Quant kostet also mindestens (1 - omega) ~ 0,16 und muss aus der Bewegung kommen.
  - Kopplung bei grossem q ist durch die glatte Ballform (Breite w ~ 1/sqrt(1 - omega^2) ~ 1,8) gedaempft.
  - Erwartung: Reibung waechst wie sigma^2 (Bornsche Naeherung) und steigt mit v steil an, wie eine Landau-artige
    Schwelle: Langsame Baelle gleiten fast reibungsfrei.
- **Bedeutung fuer Finns Bild** [H]:
  - Gibt es eine Schwelle, ist ein ungeordnetes Netz fuer langsame Materie praktisch unsichtbar.
  - Schnelle Teilchen (kosmische Strahlung, gamma bis ~1e11 [L]) spueren es aber. Ihre fast verlustfreie Ausbreitung
    begrenzt die Unordnung.

## Test (Code-Agent)

- Lange offene Kette (Absorber an den Enden), h = 0,1. Ball bei omega^2 = 0,7, Startschnelle v = 0,1, 0,2, 0,3, 0,5.
  Unordnung sigma = 0 (Kontrolle), 0,01, 0,02, 0,04; je zwei Saaten.
- **Gemessen** ueber eine feste Laufstrecke bzw. Laufzeit:
  - Ladungsschwerpunkt, Schnelle v(t) (glattes Fenster wie QBALL-GITTER-1)
  - Ballladung im Fenster
  - Bewegungsenergie (aus E und Q bzw. aus gamma)
  - Reibungsrate = -d ln(gamma v)/dt im Mittel
  - Ladungsverlustrate
- Gegenprobe: halber Zeitschritt; andere Saat.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| Z0 | Kontrolle sigma = 0: Schnelle konstant (relative Aenderung < 1e-4 ueber die Laufzeit), Ladungsverlust < 1e-8 | 90 % |
| Z1 | Bei v = 0,3: Reibungsrate ~ sigma^p mit p = 2 +- 0,3 (Ausgleich ueber sigma = 0,01; 0,02; 0,04, Saatmittel) | 65 % |
| Z2 | [H] Starke v-Abhaengigkeit: Bei sigma = 0,04 ist die Reibungsrate bei v = 0,5 mindestens 10-mal so gross wie bei v = 0,1 | 55 % |
| Z3 | [H] Ladungsverlust und Abbremsung haengen zusammen: Verhaeltnis (verlorene Ladung)/(verlorener Impuls) ist ueber v und sigma innerhalb Faktor 3 konstant | 40 % |

**Bedeutung (vorab):**
- Z1 und Z2 treffen ein: Ein ungeordnetes Netz bremst bewegte Materie, aber erst bei hoher Geschwindigkeit merklich.
  - Damit waere ein Ruhesystem des Netzes ueber die Reibung schneller Teilchen messbar.
  - Echte kosmische Strahlung legt Mpc-Strecken fast verlustfrei zurueck [L]. Das begrenzt, wie ungeordnet Finns Netz
    sein darf [H].
- Z2 verfehlt (Reibung kaum von v abhaengig): Auch langsame Materie spuert die Unordnung; das waere fuer Finns Bild
  ungeschickter.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6 (nicht cpu2, cpu3, cpu4, cpu5, p4000a,
  p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
