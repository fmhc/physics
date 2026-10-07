# VOLUMEN-G2-1: Vorab (Rechen-Agent, vor jeder Rechnung)

- Rechen-Agent fuer die Leitung claude-primary. Geschrieben ab 2026-10-07 03:35:14 CEST (date), vor jedem Lauf auf der
  .69. KARTE.md bleibt unveraendert; V0 bis V3 und ihre Wahrscheinlichkeiten sind die der Leitung.
- Kennzeichen: [M] eigene Schreibtischrechnung, [P] Projektdatei, [L] Literatur aus dem Gedaechtnis, ungeprueft, [H]
  Hypothese. Alles synthetisch, keine Messdaten.
- Code: neue Datei vg2.py (Arbeitsordner .69 /home/fmh/fmhc-physics-remote/volumen-g2-1/). Importiert unveraendert nn, td,
  tg, uk, tu aus /home/fmh/fmhc-physics-remote/netz-nichtlinear-1/code (sha256 lokal = .69 geprueft, 03:33).

## Zustand und Bedingung

- Zustand wie td/nn: x (reduziert, m = 469 bis 492), Kantenlaengen l = l0 (1 + S x), Impuls y.
- H(x, y) = 1/2 y^T A_r y + 1/2 x^T B_r x, A_r = S^T M_eff^-1 S, B_r = S^T B S, M_eff und B am gedehnten Netz (nn.NetzG).
- Bedingung: g(x) = V(x) - V0 = 0, V(x) = Summe der Tetraedervolumen aus den Laengen (Cayley-Menger, exakt, nicht
  linearisiert). Lesart wie AG2 global: 4-Volumen einer Lage = Takt x 3-Volumen, bei festem Takt also 3-Volumen fest.
- [M] V0 = |det LV| fuer jede Zerlegung derselben Punktmenge am Hintergrund (x = 0). Das ist eine Kontrolle im Rauchtest.
- Gradient analytisch: dV_t/dl_p = 2 V_t l_p (CM^-1)_(i+1, j+1) [M]; im Rauchtest gegen finite Differenzen.
- Zwangskraft in der Impulsgleichung: -lambda G^T, G = dg/dx = S^T (l0 * dV/dl).
- Startzustand: x = 0, y0 = A_r^-1 omega x_TT (wie nn.lauf), dann auf die Tangente projiziert (G A_r y = 0). Beide Arme
  (mit und ohne Bedingung) starten aus demselben projizierten Zustand, damit sie sich nur in der Dynamik unterscheiden.
  Die Projektion selbst (Aenderung von H0) wird berichtet.

## 1. Integratorwahl

- **Implizite Mitte mit Lagrange-Multiplikator (SHAKE-artige Mitte)**, nicht RATTLE:
  - x1 - x0 = dt A_r y_m, y1 - y0 = -dt (B_r x_m + lambda G(x_m)^T), g(x1) = 0, (x_m, y_m) Mittelwerte.
  - Lineares System (I + dt^2/4 A_r B_r) x_m = ... mit einer LU je dt und Operator; lambda per skalarem Newton, G(x_m)
    per Fixpunkt (bis die Bedingung |g|/V0 < 1e-14 und G stabil ist).
  - Grund [M]: Bei festen Operatoren ist H quadratisch; die implizite Mitte erhaelt quadratische Invarianten exakt
    (bis Rundung), unabhaengig von dt und auch bei indefinitem A_r. RATTLE (Verlet) haette einen Energiefehler
    ~ (omega_TT dt)^2 / 4 relativ; bei der Leapfrog-Schrittweite von nn (omega_max dt = 0,5) sind das ~1e-6, also
    ueber der V0-Schwelle 1e-8.
  - Energiebilanz mit Bedingung [M]: H1 - H0 = -lambda G(x_m) (x1 - x0); die Mittelregel fuer g ist bis dritte Ordnung
    genau, der Rest ist ~ lambda |dx|^3 g''' und sollte weit unter 1e-10 liegen.
  - Ohne Bedingung ist es dieselbe Routine mit lambda = 0.
- Nicht gewaehlt: RATTLE (Grund oben), Fixpunkt-Mitte mit dM/dl-Termen (siehe 3).

## 2. Schrittweitenregel fuer steife Moden

- Grundgitter dt0 = T / NT, NT = ceil(T omega_s0 / h), omega_s = max(omega_max, gamma_max) aus |eig(A_r B_r)| des
  aktuellen Operators (gamma = Wachstumsrate wachsender Moden).
- Nach jedem Operatorwechsel (Zug, Nachfuehrung) wird omega_s neu bestimmt und jeder Grundschritt in
  nsub = ceil(dt0 omega_s / h) Unterschritte geteilt.
- h = 1 im Hauptlauf: Die implizite Mitte ist fuer Schwingungen A-stabil; die steifste Mode bekommt bei h = 1 einen
  Phasenfehler von 7 % (2 atan(1/2) gegen 1) [M], die TT-Mode (omega_TT / omega_max ~ 1/50 bis 1/130) weniger als 1e-4.
  Fuer wachsende Moden haelt h = 1 gamma dt <= 1 < 2 (Cayley-Abbildung bleibt vorzeichenrichtig).
- Kontrolle der Schrittweite in V0: h = 1 gegen h = 0,5 (Energie muss gleich gut bleiben, Bahn der TT-Mode gleich).
- Ereignissuche (Zug) wie nn.lauf: Kandidaten nach jedem Unterschritt, Zeitpunkt per Bisektion auf der freien
  quadratischen Vorhersage, dann Mitte-Teilschritt der Laenge tau.

## 3. Nachfuehrung von M_eff

- Ein voller G2 mit dM/dl in den Kraeften ist nicht im Budget: Eine M_eff-Auswertung kostet ~5 s (nn-Laeufe), die
  Ableitung nach allen ~490 Richtungen also ~40 min je Zerlegung. Das war der Grund, warum G2 in NETZ-NICHTLINEAR-1
  scheiterte.
- Gewaehlt: **stueckweise Nachfuehrung am gedehnten Netz** (nn.NetzG mit f = 1 + S x):
  - bei jedem Zug mit der neuen Zerlegung (wie G1 in nn.lauf, neue Kante aus der flachen Doppelpyramide),
  - zusaetzlich einmal je Periode am aktuellen x (gleiche Zerlegung; S muss gleich bleiben, wird geprueft).
  - Impuls y bleibt bei der Nachfuehrung stetig (Hamilton-Sicht H(l, p)); der Energiesprung
    dH_upd = H_neu(x, y) - H_alt(x, y) wird getrennt gebucht. Er misst die fehlenden dM/dl-Terme.
- Zwischen zwei Nachfuehrungen sind die Operatoren fest. Damit ist das ein G1 mit periodischer Nachfuehrung, kein voller
  G2. Das ist eine Abweichung vom Kartenmodell und wird im Ergebnis so benannt.
- Metrikfehler beim Bau am gedehnten Netz (F_aus_dehnung) beendet den Lauf mit Grund (wie nn), kein stilles Weiterrechnen
  mit altem Operator.
- Zusatz, nur wenn Zeit bleibt: Lesart H (Operatoren am Hintergrund), weil AG2 den Effekt dort gesehen hat.

## 4. Zuege mit Bedingung

- Zug wie nn.lauf Arm b, Lesart P (wie AG2), Abbildung td.abbilden unveraendert.
- Arm mit Bedingung danach:
  1. x auf V(x) = V0 zurueck, per Newton entlang A_r G^T (die Richtung, in die auch die Zwangskraft im Integrator
     schiebt); faellt G A_r G^T zu klein aus, entlang G^T.
  2. y auf die Tangente: y <- y - mu G^T mit G A_r y = 0.
  3. Sprung dH_proj getrennt gebucht; dH_zug wie bisher.
- Auch nach jeder Nachfuehrung wird y neu projiziert (A_r aendert sich, also auch die Tangentenbedingung).
- [M] Am Hintergrund aendert ein 2-3- oder 3-2-Zug das Gesamtvolumen nicht; im gedehnten Netz nur mit O(a^2), weil
  td.abbilden die neue Kante linear fortsetzt.

## Messgroessen

- H(t) zu Proben (20 je Periode), getrennt: Integratordrift = Gesamt minus Summe der gebuchten Spruenge.
- |V - V0| / V0 je Probe (Arm ohne Bedingung: freier Volumenverlauf zum Vergleich).
- Lagrange-Multiplikator: lambda je Schritt, Zwangskraft |lambda G| gegen Netzkraft |B_r x_m|; berichtet als
  max |F_c| / max |F_n| je Periode und als Verhaeltnis der quadratischen Mittel.
- Nach jedem Zug und jeder Nachfuehrung: M_n_neg (M_eff), M_neg auf Kern(c) (c = Volumengradient an den Kanten, wie AG2),
  A_pd, negative kinetische Richtungen und wachsende Moden mit und ohne Bedingung (Spektrum wie AG2: K = Z^T A_r^-1 Z,
  V = Z^T B_r Z, Z = Kern von G), omega_max mit und ohne Bedingung (Versteifung).

## Laufplan

- Spuren cpu2, cpu3, cpu4, je Lauf <= 10 min (Budget im Skript 540 s; laengere Laeufe mit Zwischenstand und Fortsetzung).
- Rauchtest (s2): Volumen bei x = 0 gegen |det LV|, Gradient gegen finite Differenzen, ein Schritt mit und ohne Bedingung.
- V0: Arm a (keine Zuege), s1 bis s4, je mit und ohne Bedingung: Stufe F (Operatoren fest, Integratortest), h = 1 und
  h = 0,5; Stufe P (Nachfuehrung je Periode) h = 1. 10 Perioden, A = 1e-3.
- V1 bis V3: Arm b (Zuege), Lesart P, Stufe P, s1 bis s4, je mit und ohne Bedingung, 10 Perioden, A = 1e-3.
- Ohne bestandenes V0 (Stufe F) keine V1-V3-Laeufe; dann Ursache melden.

## Eigene Erwartungen (vor der Rechnung, scheiterfaehig)

| Nr | Erwartung | So kann sie scheitern | Wahrsch. |
|---|---|---|---|
| E0a | V0 Stufe F: max \|H - H0\|/H0 < 1e-12 ohne Bedingung, < 1e-10 mit; \|V - V0\|/V0 < 1e-13 mit Bedingung; h = 1 und 0,5 gleich gut | Drift darueber oder Newton konvergiert nicht | 80 % |
| E0b | V0 Stufe P: die Nachfuehrung macht Spruenge von 1e-6 bis 1e-3 relativ, Summe ueber 10 Perioden < 1e-3; keine neuen negativen Richtungen (M_n_neg bleibt 128) | Summe >= 1e-3, Metrikfehler oder M_n_neg > 128 | 50 % |
| E1 | s2 mit Bedingung: nach dem Ausnahmezug bleibt mindestens eine wachsende Mode (am gedehnten Netz half die globale Bedingung in AG2 nicht: 2 wachsende in Lesart G1), H waechst auch mit Bedingung | s2 mit Bedingung bleibt beschraenkt (\|H - H0\|/H0 < 1e-3) | 70 % |
| E2 | s1 und s3: Bedingung aendert die Kaskade nicht (Abbruch bzw. Wachstum in beiden Armen, gleiche Zugfolge bis zum ersten Ausnahmezug) | Bedingung stabilisiert s1 oder s3 | 65 % |
| E3 | Zwangskraft vor dem ersten Ausnahmezug < 10 % der Netzkraft (TT-Mode fast tangential, cos 0,004 in AG2); omega_max mit Bedingung nicht groesser als ohne | Verhaeltnis >= 10 % oder omega_max steigt | 60 % |
| E4 | s4 (keine Ausnahmezuege am Hintergrund, aber in G1 10 neue): beide Arme laufen 10 Perioden durch, Bedingung aendert die Energiebilanz um weniger als den Faktor 2 | Abbruch oder Faktor >= 2 | 45 % |
