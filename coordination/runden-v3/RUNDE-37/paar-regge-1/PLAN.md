# PAAR-REGGE-1: Plan des Code-Agenten (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 18:23:05 CEST (date), Zeitbox 60 min.
  Plan geschrieben ab 18:33:55 CEST (date), vor jeder Rechnung auf der .69.
- Gelesen: KARTE.md (ganz); gluon-paar-l/DOSSIER.md (ganz, Abschn. 6 bindend); gluon-paar-l/ARBEITSFELD.md
  Z. 168-180, 296-310; regge-anschluss-20260912.md Z. 140-162; F2 (Meyer/Teper) Z. 95-165, 240-345;
  F3 (Athenodorou/Teper 2020) Z. 1975-2015; Laufform aus RUNDE-37/takt-rand-4d-1/.
- Ordner: lokal RUNDE-37/paar-regge-1/; .69: /home/fmh/fmhc-physics-remote/paar-regge-1/ (code/, lauf/).
- Kennzeichen: [E] gerechnet (.69), [M] eigene Mathematik von Hand (nicht gegengelesen), [S] an der Quelle gelesen,
  [P] Projektdatei, [L] Gedaechtnis, [H] Hypothese, [F] Festlegung dieses Plans (nicht aus der Karte), [D] Diagnose
  (beschreibend, ohne Urteil).
- Vorhersagen und Wahrscheinlichkeiten der Karte (PR0 90 %, PR1 30 %, PR2 10 %) bleiben unveraendert.

## 1. Quellenpruefung vor der Rechnung

| Groesse | Karte/Dossier | an der Quelle | Kennzeichen |
|---|---|---|---|
| (A) 2++, 4++ | 4,894(22), 7,60(12) | Tab. 17: "2 gs 4.894(22)", "4 gs 7.60(12)*" (Stern = "likely"), F3 Z. 1985-1993 | [S], stimmt |
| (B) Gerade 3+1D | 0,281(22), 0,93(24) | Gl. (3) "2πσα′ = 0.281(22) α0 = 0.93(24)"; Gerade "passes through the lightest J = 2 and J = 4 glueballs", F2 Z. 152-157 | [S], stimmt |
| (B) Punkte | 4,89; 8,29 | M(J) = sqrt(2 pi (J - a0)/s): 4,8913 und 8,2853 | [M], stimmt gerundet; gerechnet wird ungerundet [F] |
| 2+1D-Gerade | 0,384(16), -1,144(71) | Gl. (5), F2 Z. 257 | [S], stimmt |
| masseloser adjungierter String | J = M^2/(2 pi sigma_A), sigma_A = 9/4 sigma | Gl. (7) "J = m^2/(2πσA) ≃ m^2/(4.5πσ)" (pdftotext "49 σ" = 9/4 σ), F2 Z. 310-336 | [S], stimmt |
| Endmassenformeln | "wie in regge-anschluss [P]" | kappa/omega = m v/(1 - v^2); E = 2m/sqrt(1-v^2) + (2 kappa/omega) arcsin v; J = 2 m v^2/(omega sqrt(1-v^2)) + (kappa/omega^2)(arcsin v - v sqrt(1-v^2)), regge-anschluss Z. 146-155 | [P] |
| a = 1/12 = (D - 2)/24 | [L] im Dossier | nicht an einer Quelle geprueft | [L] |

**Befund Q1 [M], vor jeder Rechnung: Die Handrechnung des Dossiers benutzt ein anderes Kraftgleichgewicht als die
[P]-Formel.**
- ARBEITSFELD Z. 174 und 304: "sigma_A = gamma m v^2/R", also kappa/omega = gamma m v. Die [P]-Formel hat
  kappa/omega = m v/(1 - v^2) = gamma^2 m v.
- Herleitung [M]: L = -2 sigma_A Int_0^R sqrt(1 - omega^2 r^2) dr - 2 m sqrt(1 - omega^2 R^2); bei starrer Drehung
  dL/dR = 0, also sigma_A sqrt(1 - v^2) = gamma m v omega. Das ist die [P]-Form: Die Seilkraft am bewegten Ende ist um
  sqrt(1 - v^2) kleiner. [L] Sonnenschein/Weissman 2014 schreiben dieselbe Randbedingung (aus dem Gedaechtnis, nicht
  abgerufen).
- Probe [M] von Hand (m = kappa = 1, v = 0,60 und 0,61): Entlang der Trajektorie muss dE/dJ = omega gelten.
  [P]: 1,0476 gegen omega 1,0480. Dossier-Form: 1,179 gegen 1,316. Die Dossier-Form verletzt diese Bedingung.
- Folgen fuer die Kontrollen (Schreibtisch [M], vor dem Lauf): mit [P] gibt konstantes v = 3/4 bei J = 2, a = 0
  E = 6,331 statt 6,80; die Steigung bei festem v = 3/4 ist 0,314 statt 0,272; der Sonderfall "konstante
  Endgeschwindigkeit" liegt bei v ~ 0,71 (B) und ~ 0,83 (A) statt 0,77 und 0,93. Die Dossier-Form gibt 6,80, 1,04 und
  1,37 genau.
- **Meine Erwartung (vor dem Kontrolllauf):** K1 (masselos) wird mit 5,3174 bestaetigt, K2 (6,80) nicht. PR0 also
  "nicht eingetroffen". Die Rechnung auf der .69 prueft das mit K2 und K3.
- Das Modell der Fits bleibt die [P]-Formel. Die Karte bindet sie ("Endmassenformeln wie in regge-anschluss"), und
  sie besteht K3. Die Dossier-Form laeuft nur als Diagnose [D] mit.

## 2. Modell (Karte, woertlich uebernommen; Ergaenzungen [F])

- Klassischer Nambu-Goto-String, Spannung sigma_A = kappa sigma, zwischen zwei gleichen Punktmassen m, starr rotierend.
  kappa = 9/4 (Hauptfall); Varianten 2,14 und 2,36 (Casimir +-5 %).
- Formeln [P] wie in Abschn. 1. Einheiten sigma = 1 (Massen in sqrt(sigma)), c = 1.
- Intercept a fest, a = 0 und a = 1/12. Konvention [F]: J = J_cl + a, also klassischer Drehimpuls J_cl = J - a.
- Eine freie Groesse: m/sqrt(sigma) >= 0. m = 0 ist der masselose String (E = sqrt(2 pi kappa J_cl)).
- Numerik [F]: v = tanh(eta); fuer jedes J_cl eine Nullstelle (brentq, eta in [1e-9, 60]; J waechst streng mit eta).
  m-Gitter [0; 4] mit 2001 Punkten, dann Verfeinerung (minimize_scalar, bounded) zwischen den Nachbarpunkten des
  Gitterminimums; m = 0 wird immer mitgeprueft. Zahl der lokalen Gitterminima wird ausgegeben.

## 3. Daten und Fehler

- **(A)** A&T 2020: M(2) = 4,894 +- 0,022; M(4) = 7,60 +- 0,12; unabhaengige Zustaende, chi^2 diagonal.
- **(B)** MT-Gerade: s = 2 pi sigma alpha' = 0,281 +- 0,022; a0 = 0,93 +- 0,24. Karte: "Band aus 0,281(22) und
  0,93(24)"; die Korrelation von s und a0 nennt die Quelle nicht.
  - **Hauptlesart R3 [F]:** chi^2 = ((s_mod - 0,281)/0,022)^2 + ((a0_mod - 0,93)/0,24)^2. s_mod und a0_mod sind die
    Sekante des Modells durch seine Massen bei J = 2 und J = 4. Begruendung: Beide Bandpunkte haengen an denselben zwei
    Parametern. R3 ist die exakte Fassung von "Band aus s und a0 mit unabhaengigen Fehlern" und hat wie die Karte
    zwei Datenpunkte und einen freien Parameter.
  - **R2 (Lesart):** Massenraum, volle Kovarianz aus linearer Fortpflanzung der s- und a0-Fehler (Korrelation der
    beiden Punkte rund 0,9 [M]).
  - **R1 (Lesart):** Massenraum, Bandbreite je Punkt als Fehler, ohne Korrelation (dM(2) ~ 0,58, dM(4) ~ 0,46 [M]).
- Freiheitsgrade: 2 Datenpunkte, 1 freier Parameter, also 1 Freiheitsgrad je a (Karte). p = P(chi^2_1 >= chi^2).

## 4. Messgroessen (je Datensatz, a, kappa, Lesart)

- bestes m/sqrt(sigma), chi^2_min, p, 1-sigma-Intervall von m (Delta chi^2 <= 1), Delta chi^2 bei m = 0;
- v_end(2) und v_end(4) beim besten m; v_end(2) an den Raendern des 1-sigma-Intervalls;
- Modellmassen E(2), E(4), Sekante (s_mod, a0_mod), Stringlaenge 2R bei J = 2 und 4.

## 5. Baender (Karte woertlich) und ihre Auswertung [F]

Karte: "(a) traegt": p >= 0,05 und v_end(2) in [0,70; 0,82]. "masselos": p >= 0,05 mit m = 0 innerhalb 1 sigma.
"traegt nicht": p < 0,05 fuer beide a. Je Datensatz getrennt.

Auswertung [F], je Datensatz, mit kappa = 9/4, [P]-Formel und (bei B) Lesart R3:
- "(a) traegt", wenn fuer mindestens ein a gilt: p >= 0,05 und 0,70 <= v_end(2) <= 0,82 (beides beim selben a, v_end
  beim besten m).
- "masselos", wenn fuer mindestens ein a gilt: p >= 0,05 und Delta chi^2(m = 0) <= 1.
- "traegt nicht", wenn fuer beide a p < 0,05.
- "uebrig" [F], wenn keines der drei Baender zutrifft (dann traegt das Modell mit einer Endgeschwindigkeit ausserhalb
  von [0,70; 0,82] und mit Masse; kein Band der Karte).
- Baender koennen zugleich gelten; dann werden alle genannt.
- kappa = 2,14 und 2,36: gleiche Auswertung, nur beschreibend. Aendert sich das Band, heisst der Befund "nicht robust
  gegen Casimir +-5 %".

## 6. Urteile

| Nr | Karte | nach Plan [F] | nach Kartenwortlaut [F] |
|---|---|---|---|
| PR0 | Kontrollen masselos 5,32 und konstantes v = 3/4 6,80 auf 1e-3 reproduziert | beide mit relativer Abweichung <= 1e-3 von 5,32 und 6,80, gerechnet mit der [P]-Formel | dazu die absolute Lesart (Abweichung <= 1e-3); beide Ausgaenge werden genannt |
| PR1 | Datensatz (B): Band "(a) traegt" | Band "(a) traegt" fuer B mit R3 | Band unter R1, R2 und R3: alle ja = eingetroffen, alle nein = nicht eingetroffen, sonst "uneindeutig" |
| PR2 | Datensatz (A): Band "(a) traegt" | Band "(a) traegt" fuer A | wie nach Plan (eine Lesart) |

Die Kontrollen K4 (Sonderfall konstantes v) und K3 (dE/dJ = omega) zaehlen nicht zu PR0; sie werden berichtet.

## 7. Kontrollen (Lauf 1, vor dem Einfrieren der Fits)

- K1 masselos, J = 2, a = 0, kappa = 9/4: geschlossen sqrt(2 pi kappa J) und Grenzwert des allgemeinen Loesers
  (m = 1e-4, 1e-6, 1e-8).
- K2 konstantes v = 3/4, J = 2, a = 0: E, noetige Endmasse, Laenge; [P] und Dossier-Form [D].
- K3 erster Hauptsatz dE/dJ = omega entlang einer Trajektorie mit fester Masse (m = 1, eta = 0,1 ... 3), [P] und
  Dossier-Form.
- K4 Sonderfall konstantes v: v mit Steigung = 0,281 (B) bzw. = Sekante der A-Massen (A), [P] und Dossier-Form.
- Budget: 1000 Loesungen bei beliebigen (m, J), ohne Datensicht.

## 8. Nachtrag 2+1D (beschreibend, ohne Urteil)

- MT-Gerade Gl. (5): s = 0,384(16), a0 = -1,144(71); Punkte bei J = 2 und 4; Lesart R3; kappa = 9/4.
- Intercept [F]: a = 0 und a = (D - 2)/24 = 1/24 fuer D = 3 (dieselbe Formel wie 1/12 in D = 4).
- J = 0 auf der 2+1D-Geraden nicht im Fit: klassisch hat J_cl <= 0 keinen rotierenden Zustand.

## 9. Diagnose [D]

- Dieselben Fits fuer A und B (R3), kappa = 9/4, mit dem Kraftgleichgewicht des Dossiers, nur beschreibend: Zeigt, wie
  stark die Formelwahl v_end verschiebt. Kein Urteil daraus.

## 10. Laeufe und Ablauf

- Nur .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spur cpu11, 1 Thread, je Lauf <= 10 min
  (RuntimeMaxSec = 600 im Starter).
- Reihenfolge: (1) Einfrieren Stufe 1: dieser Plan (sha256) vor dem Kontrolllauf. (2) Kontrolllauf. (3) Einfrieren
  Stufe 2: Plan und Code (sha256) vor dem Fitlauf; Aenderungen nach dem Kontrolllauf nur als datierter Nachtrag am
  Ende dieses Plans. (4) Fitlauf. (5) Bild aus der Fit-Datei (Modus "bild" desselben eingefrorenen Codes).
- Keine Aenderung von Baendern, Lesarten oder Code nach der Sicht auf Fit-Ergebnisse. Fehler danach nur als Selbstanzeige
  und, wenn noetig, als getrennt gekennzeichnete Diagnose.

## 11. Was ich vorab schon weiss (Offenlegung)

- Von Hand [M], beim Pruefen der Fehlerlesart von (B): Der masselose String (m = 0, a = 0) liegt fuer (B) unter R1 bei
  chi^2 ~ 3,1 (p ~ 0,08) und unter R3 bei chi^2 ~ 70. Die Wahl R3 als Hauptlesart ist statistisch begruendet
  (Abschn. 3), faellt aber nach dieser Sicht. Deshalb werden R1 und R2 fuer das Kartenwortlaut-Urteil voll mitgerechnet.
- Fits mit Masse habe ich nicht von Hand gerechnet.

## 12. Nachtrag nach dem Kontrolllauf (geschrieben ab 18:35:42 CEST, date; vor dem Fitlauf)

- Kontrolllauf 16:35:07 bis 16:35:28 UTC, cpu11, rc = 0 (lauf-69/kontrollen.json) [E]:
  - K1 masselos: 5,317362 (relativ 5,0e-4, absolut 2,6e-3 von 5,32); Grenzwert m = 1e-8 gleich auf 1e-12.
  - K2 konstantes v = 3/4: [P] 6,3307 (relativ 6,9e-2 von 6,80); Dossier-Form 6,8007 (1,0e-4), m = 1,375, Laenge 1,039.
  - K3 dE/dJ = omega: [P] bis 3,5e-9 erfuellt; Dossier-Form bis 26 % verletzt.
  - K4 Sonderfall konstantes v: [P] v = 0,706 (B), 0,834 (A); Dossier-Form 0,765 und 0,941.
  - Budget 0,15 ms je Loesung, also rund 1 s je Fit.
- Keine Aenderung an Plan, Baendern, Lesarten oder Code.
