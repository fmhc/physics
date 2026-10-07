# DIM-LEITER-QBALL-1: Plan des Code-Agenten (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 18:48:39 CEST (date), Zeitbox 90 min (bis 20:18:39 CEST).
  Plan geschrieben ab 19:05:11 CEST (date). Vorher lief nur ein Rauchtest (Abschn. 10, Offenlegung).
- Gelesen: KARTE.md (ganz, bindend, unveraendert); RUNDE-37/paar-regge-1/ (PLAN, ERGEBNIS Abschn. 9 bis 12, Code-Kopf);
  QB-BS-2D/ERGEBNIS.md; RUNDE-26/kegel-q (Code-Kopf, Radial-Klasse, log-radial.txt); RUNDE-02.md Z. 30 bis 70 und
  RUNDE-02/tests1d/lauf-69/ausgabe/tests1d_bericht.txt Z. 1 bis 70; Papier I main.tex Z. 80 bis 115 und 286 bis 320;
  RUNDE-16/beutel-1/ERGEBNIS.md Z. 160 bis 175; IDEEN-EVOLUTION/GEN-01/G1-07/KARTE.md Z. 1 bis 30;
  RUNDE-16/dim-beutel/KARTE.md (anderes Modell).
- Ordner: lokal RUNDE-37/dim-leiter-qball-1/ (code/, lauf-69/); .69: /home/fmh/fmhc-physics-remote/dim-leiter-qball-1/
  (code/, rauch/, lauf/).
- Kennzeichen: [E] gerechnet (.69), [M] eigene Mathematik von Hand (nicht gegengelesen), [L] Literatur aus dem
  Gedaechtnis, [P] Projektdatei, [H] Hypothese, [F] Festlegung dieses Plans (nicht aus der Karte).
- Vorhersagen und Wahrscheinlichkeiten der Karte (DQ0 85 %, DQ1 70 %, DQ2 35 %, DQ3 10 %) bleiben unveraendert.

## 1. Liegt die D-Leiter schon vor? (Projekt-grep, versiegelte Pfade ausgeschlossen)

- Nein. Weder in model-lab/papers/qball-bic-ladder-20260930/ noch in coordination/resonance-20260930/ noch in runden-v3
  gibt es Q(omega) des Papier-I-Modells fuer D >= 4. RUNDE-16/dim-beutel ist ein anderes Modell (FLS-Beutel).
- Vorhanden sind D = 1, 2, 3 [P]; sie dienen als Kontrollen (Abschn. 3). Gerechnet wird deshalb D = 1 bis 12.

## 2. Was ich vorab schon weiss (Offenlegung, vor jeder Rechnung)

- **[P] aus Projektdateien, also schon gesehen:**
  - D = 3: Q_min = 111,8441 bei omega^2 = 0,9269; duenne Wand VK-stabil, dicke instabil; E/Q > 1 ab omega^2 ~ 0,85
    (RUNDE-02 tests1d). Daraus folgt grob omega_s ~ 0,92 und W(3) ~ 0,73 [M, grob].
  - D = 2: "die 2D-Familien sind monoton" (RUNDE-04.md Z. 61); QB-BS-2D: Ast von q' = 12 (omega 0,988) bis 100,
    E < q ueberall. Also vermutlich kein Wendepunkt und W(2) ~ 1.
  - D = 1: Q -> 0 fuer omega -> 1 (G1-07, Q ~ 4 omega eps). Also kein Wendepunkt und W(1) ~ 1 (s. u.).
  - Folge: Schon vor der Rechnung ist absehbar, dass W(1) und W(2) bei 1 liegen und W(3) darunter. **DQ3 ist damit
    vorab so gut wie entschieden (nicht eingetroffen)**, es sei denn, W(1) oder W(2) liegt unter 1.
- **[M] Schreibtisch, E < Q fuer D = 1, 2:** Entlang des Astes gilt dE/dQ = omega, also d(E - Q)/domega =
  (omega - 1) dQ/domega. Ist dQ/domega < 0 ueberall und E - Q -> 0 fuer omega -> 1 (NLS-Skalierung, D = 1, 2), dann ist
  E < Q auf dem ganzen Fenster.
- **[M] Schreibtisch, die Dicke-Wand-Ableitung der Karte gilt nur fuer D <= 3.**
  - Die kubische NLS -Lap g + g = 2 g^3 hat nur fuer D <= 3 einen lokalisierten Grundzustand. Pohozaev plus Nehari:
    A = Int |grad g|^2, B = Int g^2 erfuellen (D - 4) A = -D B. Fuer D = 4 folgt B = 0, fuer D > 4 A < 0. Also keine
    Loesung fuer D >= 4.
  - D = 4 (Abschaetzung, [M]/[H]): Talenti-Blase mit Masse- und Quintikterm; Skala lambda ~ eps^(-1/2), Q ~ eps^(-1)
    mal Logarithmus. **Erwartung: Exponent in D = 4 nahe -1, nicht -2. Dann ist DQ0 nicht eingetroffen.**
  - D >= 5 (Berestycki-Lions, Nullmassenfall [L]): Fuer omega -> 1 strebt das Profil gegen eine Nullmassen-Loesung mit
    Schwanz r^(2-D); deren Ladung ist endlich. **Erwartung: Q(omega -> 1) endlich fuer D >= 5.** Ob dann noch ein
    inneres Minimum (Wendepunkt) existiert, weiss ich nicht. Bei omega = 1 gilt dort E - Q = (2/D) Int |grad f|^2 > 0
    [M, Pohozaev].
  - Damit ist "Wendepunkt fuer D >= 3 ableitbar" (Karte) fuer D >= 4 nicht gedeckt. DQ1 ist dadurch offener als die
    Karte annimmt. Karte und Vorhersagen bleiben unveraendert; das ist eine Begruendung, keine Aenderung.

## 3. Modell, Konvention und Projektwerte [P]

- Karte woertlich: U(S) = S - S^2 + S^3/2, m = 1, f'' + (D-1)/r f' + omega^2 f - U'(f^2) f = 0.
- Q = 2 omega Int f^2 d^Dx, E = Int (omega^2 f^2 + |grad f|^2 + U) d^Dx, Raumwinkel S_{D-1} = 2 pi^(D/2)/Gamma(D/2)
  (D = 1: ganze Gerade). Wie Papier I (main.tex Gl. 1, 2) und KEGEL-Q/QB-BS-2D.
- Projektwerte fuer DQ0 (Teil c):
  - D = 3, RUNDE-02 tests1d (3D radial, 6 Stellen): omega^2 = 0,55: Q 1,97733e4, E 1,50306e4; 0,70: 473,413, 428,641;
    0,80: 186,110, 181,912; 0,90: 115,642, 117,398; Q_min = 111,8441 (weitere Projektwerte 111,86 beutel-1 und
    111,87733 FM-4 nur berichtet).
  - D = 2, QB-BS-2D S0 (M = 1200): E(q = 13) = 12,969231428; E(21) = 20,097535160; E(100) = 82,139707571.
    KEGEL-Q radial (dr = 0,005): E(50) = 43,56581450; E(100) = 82,13970391; E(200) = 157,30106459; E(400) = 304,95495546.
  - D = 1, RUNDE-02 Anker (nur berichtet): omega^2 = 0,55, 0,70, 0,90.

## 4. Verfahren [F]

- Variationelle Finite-Volumen-Diskretisierung (Verallgemeinerung von KEGEL-Q Radial auf D Dimensionen):
  Zellvolumen V_j = S_{D-1}(r_{j+1/2}^D - r_{j-1/2}^D)/D, Randgewicht A = S_{D-1} r^(D-1)/Abstand. Diskret gilt
  dE/dQ = omega exakt (Kontrolle).
- Gitter: gleichfoermig h bis r_u = max(60, 70,71 (D - 1) + 40) (duenne Wand bei omega^2 = 0,505 plus 40), danach
  exponentiell gestreckt (L = 5) bis R_MAX = 3000 (= 30/eps bei 1 - omega^2 = 1e-4); Dirichlet aussen.
  Zwei Gitter: grob h = 0,025, fein h = 0,0125. **Hauptwerte vom feinen Gitter**, grob/fein-Abstand als Fehlermass.
- Newton bei festem omega^2 (tridiagonal), Ziel max. Residuum 1e-10, Annahme <= 1e-8, knotenfrei, f(0) > 1e-5.
- Start bei omega^2 = 0,75 aus 18 Startprofilen; gewaehlt wird die Loesung kleinster Wirkung E - omega Q
  (Grundzustand). Fortsetzung nach unten (Wandverschiebung als Praediktor) und nach oben (Sekante), Schrittteilung.
- dQ/domega exakt aus J df/domega = 2 omega f. VK-stabil heisst dQ/domega < 0.
- Wurzeln von dQ/domega (omega_c, Art min/max) und von E - Q (omega_s) per Brent zwischen Gitterpunkten mit
  Vorzeichenwechsel.
- Schiessverfahren als Kontrolle ("Schuss-Genauigkeit" der Karte): DOP853 (rtol 1e-12), Bisektion in f(0) bis
  1e-12 relativ, bei omega^2 = 0,70 und 0,95 je D; Vergleich mit f(0) fein, grob und Richardson.

## 5. omega-Gitter [F]

- G1: omega^2 = 0,5 + 0,005 k, k = 1 ... 99 (0,505 bis 0,995).
- G2: 1 - omega^2 = 10^(-4 + 0,25 k), k = 0 ... 7 (1e-4 bis 5,6e-3).
- Zusammen 107 Punkte, je D und je Gitter dieselben.

## 6. Messgroessen [F]

- Je D und Gitterpunkt: Q, E, E/Q, dQ/domega, f(0), R_half (S = S(0)/2), Residuum, Virial, dE/dQ-Probe, Anteil von
  Int f^2 bei r > R_MAX/2.
- omega_c(D), Q_min(D): kleinstes inneres Minimum (Wurzel von dQ/domega mit Wechsel - nach +). Gibt es keines im
  Fenster, ist Q_min(D) der kleinste Gitterwert (Kennzeichen "Rand").
- omega_s(D): kleinste Wurzel von E - Q; Q_s(D) = Q dort (Mindestladung fuer E < Q auf diesem Ast).
- W(D) = Laenge der omega-Menge in (omega_min, 1), auf der dQ/domega < 0 und E < Q, geteilt durch 1 - omega_min
  (Hauptmass, linear in omega wie das Fenster der Karte). Zweitmass W2 in omega^2. Die Randstuecke (omega_min,
  sqrt(0,505)) und (sqrt(0,9999), 1) erben den Zustand des naechsten Gitterpunkts (duenne Wand: VK-stabil und
  E/Q -> omega_min < 1 [M]).
- Exponent p(D): Steigung von ln Q gegen ln eps (eps^2 = 1 - omega^2), kleinste Quadrate ueber 1 - omega^2 = 1e-4 bis
  1e-3 (fuenf G2-Punkte); dazu lokale Steigungen.
- Existenzgrenze: omega_*^2 = Nullstelle der Geraden durch 1/R_half an omega^2 = 0,505, 0,51, 0,515, 0,52 (D >= 2);
  D = 1: f(0)^2 gegen die exakte Amplitude 1 - sqrt(2 omega^2 - 1), die unter omega^2 = 1/2 nicht reell ist [M].

## 7. Urteile und Schwellen (vorab, nicht verschiebbar)

| Nr | Karte | nach Plan [F] | nach Kartenwortlaut [F] |
|---|---|---|---|
| DQ0 | Existenzgrenze 0,7071; Exponent 2 - D in D = 1, 3, 4 auf 10 %; 3D-Werte des Projekts auf 1e-3 | alle Teile: (a1) alle 107 Punkte auf beiden Gittern geloest, (a2) abs(omega_* - 0,70711) <= 0,002 fuer D = 2 bis 12, (a3) D = 1: abs(f(0)^2 - exakt) <= 1e-4 an allen Punkten; (b) abs(p - (2 - D)) <= 0,1 abs(2 - D) fuer D = 1, 3, 4; (c) alle Projektwerte D = 3 (Q und E an vier omega^2, Q_min) und D = 2 (QB-BS-2D und KEGEL-Q) relativ <= 1e-3 | wie Plan, aber (c) nur mit den D = 3-Werten ("3D" woertlich als drei Raumdimensionen) |
| DQ1 | Wendepunkt fuer D = 3 bis 12, Q_min(D) streng monoton steigend | inneres Minimum fuer jedes D = 3 bis 12 und Q_min(D+1) > Q_min(D) fuer D = 3 bis 11 | gleich (der Wendepunkt ist in der Karte als Minimum von Q(omega) definiert) |
| DQ2 | ln Q_min linear in D auf 15 % (D = 3 bis 12) | Fit ln Q_min = a + b D (kleinste Quadrate); max ueber D von abs(Q_min/exp(a + b D) - 1) <= 0,15. Q_min "Rand" zaehlt mit Kennzeichen | max ueber D von abs(ln Q_min - (a + b D))/abs(ln Q_min) <= 0,15 |
| DQ3 | W(D) bei D = 3 oder 4 am groessten | Menge der D mit W = max W (Toleranz 1e-9) liegt in {3, 4} | mit W und W2: beide ja = eingetroffen, beide nein = nicht eingetroffen, sonst uneindeutig |

- Kontrollen ohne Urteil, nur berichtet: Schuss gegen FV (f(0) relativ), grob gegen fein (Q, E, Q_min, omega_c,
  omega_s, W), dE/dQ = omega, Virial, Aussenanteil, D = 1 gegen Quadratur (Q, E) und gegen die RUNDE-02-Anker.

## 8. Dimensionsvergleich (AGENTS.md)

- Stellgroesse ist die Raumdimension D. Alles ist radial (kugelsymmetrisch). VK plus E < m Q ist kein voller
  Stabilitaetsnachweis: Nicht-radiale Stoerungen, Zerfall in mehrere Baelle und Dynamik sind nicht geprueft.
- Synthetische Rechnung im Modell, keine Messdatenbestaetigung.

## 9. Laeufe

- Nur .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu11 und cpu4, 1 Thread,
  RuntimeMaxSec = 600, Logs mit absolutem Pfad.
- Reihenfolge: (1) Rauchtest (Abschn. 10). (2) Einfrieren: dieser Plan und code/dim_leiter.py (sha256 in
  EINGEFROREN-SHA256.txt). (3) Hauptlaeufe: cpu11 D = 1 bis 6, cpu4 D = 7 bis 12. (4) Auswertung und Bilder mit dem
  eingefrorenen Code. Faellt ein Hauptlauf aus (Zeit, Absturz), wird die D-Liste geteilt; jede Codeaenderung nur als
  datierter Nachtrag mit neuem Hash, vor der Sicht auf Hauptergebnisse.

## 10. Rauchtest (Offenlegung)

- Gestartet 17:04:47 UTC (19:04:47 CEST), also bevor dieser Plan fertig war. Inhalt: D = 1, 4, 12 auf dem groben Gitter
  an sechs omega^2. Ausgegeben werden nur Laufzeit, Residuen, dE/dQ-Probe, Aussenanteil, Zahl der Starts, D = 1 gegen
  die exakte Quadratur und fuer D = 12 eine Schussprobe. Keine Q- oder E-Werte.

## 11. Nachtrag 1 nach den Rauchtests (geschrieben ab 19:12 CEST, vor jedem Hauptlauf)

- Rauch 1 (17:04:47 bis 17:05:09 UTC, rc = 1): D = 1 wich von der Quadratur um 100 % ab. Ursache: Newton und Annahme
  mit absolutem Residuum liessen bei kleiner Amplitude (omega^2 = 0,9999) ein fast triviales Profil durch. D = 12:
  kein Start bei omega^2 = 0,75 gefunden.
- Aenderungen am Code (vor dem Einfrieren):
  - Residuum relativ: max|F|/max|f| (Newton-Ziel 1e-10, Annahme 1e-8 relativ). Abschn. 4 gilt mit "relativ".
  - Zusaetzlicher Startkandidat per Schiessen (Bisektion in f(0) zwischen U(S)/S = omega^2 und dem Huegel
    U'(S) = omega^2).
  - Fuer D > 4, wenn kein Start greift: Fortsetzung in der stetigen Dimension von D = 4 aus (Schritt 0,25, Teilung),
    auf demselben Gitter, Praediktor Wandverschiebung. Ergebnis ist ein Kandidat wie die anderen.
- Rauch 2 (17:08:18 bis 17:08:40 UTC, rc = 1): D = 1 gegen Quadratur jetzt dQ 1,2e-5, dS0 7,1e-6 (grobes Gitter);
  D = 4 fertig in 15,3 s; D = 12 Start weiter gescheitert (Schiessen allein reicht dort nicht).
- Rauch 3 (ab 17:09:55 UTC) prueft die D-Fortsetzung. Keine Q- oder E-Werte gesehen.
- Rauch 3 (17:09:55 UTC, cpu11) und Rauch 4 (17:13:48 UTC, cpu4, D = 12 auf dem vollen omega-Gitter, nur Fortschritt)
  von mir per systemctl --user stop beendet (17:14:40 UTC): Der D = 12-Start klappt jetzt (D-Fortsetzung), aber der
  Abstieg zur duennen Wand wurde sehr langsam (R ~ 1/(omega^2 - 1/2), bei 0,505 R ~ 780; Schrittteilungen).

## 12. Nachtrag 2 (geschrieben ab 19:15 CEST, vor jedem Hauptlauf): unteres Gitterende 0,53 statt 0,505

- Grund: Laufzeit (je Lauf <= 10 min). Bei omega^2 = 0,505 braucht D = 12 eine Wand bei r ~ 780.
- G1 neu: omega^2 = 0,5 + 0,005 k, k = 6 ... 99 (0,530 bis 0,995); mit G2 zusammen 102 Punkte. r_u = max(60,
  (D - 1) sqrt2/4 / 0,03 + 40).
- Existenzgrenze (a2) neu: quadratischer Fit von 1/R_half an omega^2 = 0,530, 0,535, 0,540, 0,545, 0,550; omega_*^2 =
  groesste reelle Nullstelle unter 0,530. Schwelle unveraendert abs(omega_* - 0,70711) <= 0,002.
- W(D): Das Randstueck (omega_min, sqrt(0,53)) = (0,70711, 0,72801), also 7,1 % des Fensters, erbt den Zustand bei
  0,53. Begruendung [M]: duenne Wand, Q ~ (omega^2 - 1/2)^(-D) also dQ/domega < 0, und E/Q -> omega_min < 1. Das ist
  eine Annahme aus der Ableitung, keine Rechnung; im Ergebnis gekennzeichnet.
- Alles andere (Schwellen, Urteilsregeln, Referenzwerte; D = 3-Werte liegen bei 0,55 und hoeher) bleibt.
- Rauch 5 (cpu4, D = 12) und Rauch 6 (cpu11, D = 4 und 7), volles neues Gitter, grob, nur Fortschritt und Kontrollen:
  Zeitmessung fuer die Aufteilung der Hauptlaeufe.
- Rauch 5 (cpu4, D = 12) und Rauch 6 (cpu11, D = 4, 7), grobes Gitter, volles neues Gitter, rc = 0: Familien in 29,5 s
  (D = 12), 5,7 s (D = 4), 12,4 s (D = 7); max. relatives Residuum <= 1e-10, dE/dQ-Probe <= 5e-11; Schussprobe
  D = 12 bei 0,75 in 0,7 s. Keine Q- oder E-Werte gesehen.
- Hauptlaeufe deshalb ein Lauf je D: cpu11 D = 1, 3, 5, 7, 9, 11; cpu4 D = 2, 4, 6, 8, 10, 12 (je Spur nacheinander).

## 13. Einfrieren

- Dieser Plan und code/dim_leiter.py werden jetzt eingefroren (EINGEFROREN-SHA256.txt), vor jedem Hauptlauf und vor
  jeder Sicht auf Q-, E-, omega_c-, omega_s- oder W-Werte.
