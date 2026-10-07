# STRING-1: Entstehen aus "Punkte ergeben Striche" von selbst Strings, und brechen sie? (Runde 35)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 21:01:34 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn ~19:12: "haben wir diese kraft auch schon wenn wir die stabilen punkte-ergeben-strich-logik folgen, oder werden
    wobbelnde strings automatisch daraus die ggf brechen wenn sie zu lang werden?"
  - Finn ~21:00: "Weiter" (Wahl STRING-1 durch die Leitung, weil es seine eigene Frage ist).
  - Schreibtisch: RUNDE-34/tetra-konzept/STRINGS-PEITSCHE.md, Abschnitte 1 und 2.
- Kennzeichen: [M] Mathematik (vorab ableitbar), [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Modell (Punkte und Striche):**
  - Knoten auf Kette (d = 1), Quadratgitter (d = 2) und kubischem Gitter (d = 3).
  - Auf jeder Kante ein ganzzahliger Fluss n_e, Energie H = (J/2) sum n_e^2, Kopplung K = J/T (gross = Fluss teuer =
    kalt).
  - Gauss-Gesetz an jedem Knoten: Zufluss minus Abfluss = Ladung. Zwei feste Ladungen +1 bei A und -1 bei B im Abstand r.
  - Gemessen wird F(r)/T = -ln[Z(r)/Z(0)].
- **Dualitaet** [M, Poisson-Summe]: Z(r)/Z(0) = <cos(theta_A - theta_B)> im Villain-XY-Modell mit K_V = 1/K.
  - Das ist eine unabhaengige Gegenprobe: Strommodell (Wurm) gegen Winkelmodell (Metropolis).
- **Regime:**

  | d | Fluss teuer (K gross) | Fluss billig (K klein) |
  |---|---|---|
  | 1 | String: F = (J/2) r genau [M] | ebenso (eine Linie kann nicht ausweichen) |
  | 2 | String: F/T = r/xi + (1/2) ln r + c | Logarithmus: F/T = eta ln r + c, eta ~ K/(2 pi) (Spinwellen) |
  | 3 | String: F/T = r/xi + ln r + c | Coulomb: F/T = c - C/r, C ~ 1/(4 pi K_V,R) >= K/(4 pi) |

  - Die Uebergaenge [L?]: d = 2 bei K ~ 1,33 (Villain-BKT bei K_V ~ 0,75), d = 3 bei K ~ 3,0 (Villain-3D-XY bei
    K_V ~ 0,333).
  - **Wobbeln** [M/L, Ornstein-Zernike]: Der String zittert quer. Das gibt den Logarithmus (d - 1)/2 * ln r zusaetzlich
    zum linearen Teil (Vorfaktor r^(-(d-1)/2) der Korrelation).
- **Bruch** [M]: Duerfen sich Ladungspaare bilden (Kosten mu je Ladung), wird ein langer String durch ein Paar ersetzt,
  sobald sigma r > ~2 mu. Also r_c ~ 2 mu/sigma, mit sigma = T/xi.
  - Im Winkelmodell entspricht das einem aeusseren Feld h ~ 2 exp(-mu/T) auf die Winkel [M].
- **Antwort auf Finns Frage (Erwartung):** Ja, Strings entstehen von selbst, sobald Fluss teuer ist. Sie zittern (ln r)
  und brechen, wenn Paarbildung billiger ist. Ist Fluss billig, verteilt er sich: in der Flaeche als Logarithmus, im Raum
  als Coulomb.

## Test (Code-Agent)

- **Strommodell:** Wurm-Algorithmus (Prokof'ev/Svistunov) auf periodischen Gittern. Das Histogramm des Kopf-Schwanz-
  Abstands gibt Z(r)/Z(0) fuer alle r zugleich.
  - d = 2: L = 64 oder groesser, K = 0,5 und 2,5.
  - d = 3: L = 24 oder groesser, K = 1,5 und 4,5.
  - Je zwei Groessen L.
- **Gegenprobe:** Villain-XY im Winkelmodell (Metropolis, Villain-Gewicht mit abgeschnittener Summe, Abschnitt offenlegen)
  fuer je einen K-Wert je d; G(r) muss mit dem Wurm uebereinstimmen.
- **d = 1:**
  - exakt (Uebertragungsmatrix) ohne und mit Paarbildung: J = 1, T = 0,5, mu = 3
  - Vorhersage r_c = 2 mu/sigma = 12; mit Entropie der Paarlage ~11
- **d = 3 mit Paarbildung** (wahlweise, darf "nicht gerechnet" bleiben): K = 4,5, mu so gewaehlt, dass 2 mu/sigma(gemessen)
  ~ 6 ist, im Winkelmodell als Feld h oder als Wurm mit Ladungszuegen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| S0 | Kontrolle: Gauss-Gesetz in jeder Konfiguration exakt; d = 1 ohne Paarbildung: F = (J/2) r genau; Wurm und Winkelmodell stimmen je d in G(r) innerhalb 3 sigma der Statistik ueberein | 90 % |
| S1 | d = 2, K = 2,5: String. Ausgleich r/xi + a ln r + c ist besser als eta ln r + c; a liegt in [0,25; 0,75] | 60 % |
| S2 | d = 2, K = 0,5: Logarithmus. eta liegt in [0,068; 0,092] (K/(2 pi) = 0,0796 +- 15 %) | 70 % |
| S3 | d = 3, K = 4,5: String. Ausgleich r/xi + a ln r + c ist besser als c - C/r; a liegt in [0,6; 1,4] | 55 % |
| S4 | d = 3, K = 1,5: Coulomb. F/T saettigt; c - C/r ist besser als jeder lineare Ausgleich; C liegt in [0,10; 0,36] | 60 % |
| S5 | d = 1 mit Paarbildung (exakt): Der Knick von linear zu flach liegt bei r_c in [10; 13] | 85 % |
| S6 | d = 3 mit Paarbildung (wahlweise): F saettigt ab r ~ r_c (+- 30 %) bei ~2 mu - T * (Lagenentropie) | 50 % |

**Bedeutung (vorab):**
- S1, S3 und S5 treffen ein: Die "Punkte ergeben Striche"-Logik erzeugt von selbst Strings, sobald Fluss teuer ist. Sie
  zittern messbar (ln r) und brechen, wenn ein neues Paar billiger ist als ein langer String.
- S2 und S4 treffen ein: Ist Fluss billig, verteilt er sich, und die Kraft wird Coulomb-artig. Finns Tetraeder-Eis
  (FLUSS-1) liegt in diesem Regime; dort ist der Fluss durch die Eisregel festgelegt, nicht durch Energie.
- Ein Ausgang mit S1 oder S3 verfehlt: Die Uebergangslage [L?] stimmt nicht, oder der Ausgleich unterscheidet die Formen
  auf diesen Groessen nicht. Beschreiben, nicht umdeuten.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu6 (nur diese; ein Lauf zugleich); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min.
